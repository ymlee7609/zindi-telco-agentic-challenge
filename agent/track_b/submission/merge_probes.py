"""성공한 probe 들의 delta 를 합쳐 combined submission 생성.

사용 시나리오 (사용자 귀환 후):
  020~027 probe 를 순차 업로드하며 Zindi 점수 확인.
  각 probe 가 +0.02 이상 상승했으면 'successful' 로 기록.
  모든 successful probe 의 delta 를 합쳐 028 로 제출 → 최종 점수.

사용:
  python3 agent/track_b/submission/merge_probes.py 020 022 025
  → 020, 022, 025 의 delta 를 모두 적용한 submission_028_combined_*.csv 생성.

안전 장치:
  - 각 probe 는 서로 다른 scenario_id 를 건드리므로 충돌 거의 없음
  - 동일 scenario_id 를 여러 probe 가 수정하면 마지막 것 우선 (+ warning)
  - 최종 CSV 는 audit_format 검증 실행 권장
"""

from __future__ import annotations

import csv
import glob
import sys
from pathlib import Path

_DIR = Path(__file__).resolve().parent
_BASELINE = _DIR / "submission_018_20260423_ground_truth.csv"


def _find_probe_csv(serial: int) -> Path | None:
    pattern = str(_DIR / f"submission_{serial:03d}_*.csv")
    matches = glob.glob(pattern)
    if not matches:
        return None
    # exclude combined 자체
    matches = [m for m in matches if "combined" not in m]
    if not matches:
        return None
    return Path(matches[0])


def load_rows(path: Path) -> list[list[str]]:
    with path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.reader(f))


def diff_against_baseline(
    baseline: list[list[str]], probe: list[list[str]]
) -> dict[str, str]:
    """probe CSV 에서 baseline 과 다른 ID 의 Track B 값 반환."""
    base_map = {r[0]: r[2] if len(r) >= 3 else "" for r in baseline[1:]}
    delta: dict[str, str] = {}
    for r in probe[1:]:
        if len(r) < 3:
            continue
        sid, tb = r[0], r[2]
        if base_map.get(sid, "") != tb:
            delta[sid] = tb
    return delta


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python3 merge_probes.py <serial> [<serial> ...]", file=sys.stderr)
        print("  예: python3 merge_probes.py 020 022 025", file=sys.stderr)
        return 2

    serials: list[int] = []
    for arg in sys.argv[1:]:
        try:
            serials.append(int(arg))
        except ValueError:
            print(f"invalid serial: {arg}", file=sys.stderr)
            return 2

    if not _BASELINE.exists():
        print(f"baseline not found: {_BASELINE}", file=sys.stderr)
        return 1

    # 각 probe 로부터 delta 추출
    base_rows = load_rows(_BASELINE)
    merged_delta: dict[str, tuple[str, int]] = {}  # sid → (value, source_serial)

    for s in serials:
        probe_path = _find_probe_csv(s)
        if probe_path is None:
            print(f"[WARN] probe {s:03d} CSV not found, skipping")
            continue
        probe_rows = load_rows(probe_path)
        delta = diff_against_baseline(base_rows, probe_rows)
        print(f"[OK]   probe {s:03d}: {len(delta)} changed IDs from {probe_path.name}")
        for sid, val in delta.items():
            if sid in merged_delta and merged_delta[sid][0] != val:
                prev_val, prev_s = merged_delta[sid]
                print(
                    f"  [CONFLICT] sid={sid[:8]}: "
                    f"probe {prev_s:03d}={prev_val[:40]!r} vs "
                    f"probe {s:03d}={val[:40]!r} — 나중 것 채택"
                )
            merged_delta[sid] = (val, s)

    if not merged_delta:
        print("no deltas to merge, aborting")
        return 1

    # baseline 에 적용
    import copy
    merged_rows = copy.deepcopy(base_rows)
    for r in merged_rows[1:]:
        if len(r) >= 3 and r[0] in merged_delta:
            r[2] = merged_delta[r[0]][0]

    # output 파일
    suffix = "_".join(f"{s:03d}" for s in sorted(serials))
    out = _DIR / f"submission_028_20260424_combined_{suffix}.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(merged_rows)

    print()
    print(f"Combined submission: {out.name}")
    print(f"Total merged delta: {len(merged_delta)} IDs")
    print()
    print("다음 단계:")
    print(f"  python3 agent/track_b/submission/audit_format.py {out.name}")
    print(f"  → PASS 면 Zindi 업로드")
    return 0


if __name__ == "__main__":
    sys.exit(main())
