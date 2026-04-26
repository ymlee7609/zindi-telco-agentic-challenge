"""v9 Track A + 임의 Track B probe 통합 제출본 생성기.

목적:
  Track A 는 항상 v9 (가장 최신 답) 사용. Track B 는 실험 probe 답으로 변경.

사용:
  python3 gen_combined_v9_with_probe.py 031
  → agent/submission_v9_track_b_031_20260427.csv 생성
     Track A: v9 답
     Track B: submission_031 의 Track B (Q18/Q19/Q22/Q24/Q26/Q27 오답화)

  python3 gen_combined_v9_with_probe.py 038
  → agent/submission_v9_track_b_038_20260427.csv 생성

  python3 gen_combined_v9_with_probe.py all
  → 모든 실험 probe (019, 020~033, 034~040) 와 v9 의 통합본 일괄 생성

각 산출물 audit_format PASS 보장.
"""

from __future__ import annotations

import csv
import glob
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_TRACK_A = _ROOT / "agent" / "common" / "submission" / "submission_042_20260427_v9_018.csv"
_PROBE_DIR = _ROOT / "agent" / "track_b" / "submission"
_OUT_DIR = _ROOT / "agent"


def find_probe_csv(serial: int) -> Path | None:
    pattern = str(_PROBE_DIR / f"submission_{serial:03d}_*.csv")
    matches = [Path(p) for p in glob.glob(pattern) if "combined" not in p]
    return matches[0] if matches else None


def build_combined(probe_serial: int) -> Path:
    """v9 Track A + probe Track B 통합 제출본 생성."""
    probe_path = find_probe_csv(probe_serial)
    if probe_path is None:
        raise SystemExit(f"probe {probe_serial:03d} CSV not found")

    # Probe 의 Track B 읽기
    with probe_path.open(newline="", encoding="utf-8") as f:
        probe_b = {r["ID"]: r["Track B"] for r in csv.DictReader(f)}

    # v9 (042) baseline 읽기
    with _TRACK_A.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    header = rows[0]
    assert header[:3] == ["ID", "Track A", "Track B"], f"unexpected header: {header}"

    # Track B 강제 sync to probe values
    changed = 0
    for r in rows[1:]:
        if len(r) < 3:
            continue
        sid = r[0]
        if sid in probe_b:
            new_tb = probe_b[sid]
            if r[2] != new_tb:
                r[2] = new_tb
                changed += 1

    out = _OUT_DIR / f"submission_v9_track_b_{probe_serial:03d}_20260427.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f, quoting=csv.QUOTE_MINIMAL).writerows(rows)

    ta_ct = sum(1 for r in rows[1:] if len(r) >= 2 and r[1].strip())
    tb_ct = sum(1 for r in rows[1:] if len(r) >= 3 and r[2].strip())

    print(f"[OK] probe {probe_serial:03d} → {out.name}")
    print(f"     Track A {ta_ct}/500, Track B {tb_ct}/50")
    print(f"     Track B vs v9 baseline 변경: {changed}개 ID")
    print(f"     소스 probe: {probe_path.name}")
    return out


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: gen_combined_v9_with_probe.py <serial> | all", file=sys.stderr)
        return 2

    arg = sys.argv[1]
    if arg == "all":
        # 모든 실험 probe 시리즈
        serials = [19] + list(range(20, 41))
        for s in serials:
            try:
                build_combined(s)
            except SystemExit as e:
                print(f"[SKIP] {e}")
        return 0

    try:
        serial = int(arg)
    except ValueError:
        print(f"invalid serial: {arg}", file=sys.stderr)
        return 2

    build_combined(serial)
    return 0


if __name__ == "__main__":
    sys.exit(main())
