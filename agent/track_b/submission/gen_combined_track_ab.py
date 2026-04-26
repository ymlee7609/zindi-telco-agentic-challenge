"""Track A + Track B 통합 제출본 생성기.

소스 (2026-04-27 갱신):
  - Track A best: agent/common/submission/submission_042_20260427_v9_018.csv
                   (Track A 500개 v9 답 + Track B 50개 채워진 상태)
  - Track B best: agent/track_b/submission/submission_018_20260423_ground_truth.csv
                   (Zindi 0.48 = 24/50)

검증:
  042 v9 의 Track B 50 == submission_018 의 Track B 50 (100% 일치 확인됨)

출력:
  agent/submission_combined_track_ab_20260425.csv
  - Track A: 042 v9 답
  - Track B: 018 강제 sync (정합성 보장)
  - 550 rows, audit_format PASS 보장
"""

from __future__ import annotations

import csv
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_TRACK_A = _ROOT / "agent" / "common" / "submission" / "submission_042_20260427_v9_018.csv"
_TRACK_B = _ROOT / "agent" / "track_b" / "submission" / "submission_018_20260423_ground_truth.csv"
_OUT = _ROOT / "agent" / "submission_combined_track_ab_20260425.csv"


def main() -> None:
    if not _TRACK_A.exists():
        raise SystemExit(f"Track A source not found: {_TRACK_A}")
    if not _TRACK_B.exists():
        raise SystemExit(f"Track B source not found: {_TRACK_B}")

    # Track B 답 로드
    with _TRACK_B.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        b_map = {r["ID"]: r["Track B"] for r in reader}

    # Track A 기반 + Track B 강제 sync
    with _TRACK_A.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    header = rows[0]
    assert header[:3] == ["ID", "Track A", "Track B"], f"unexpected header: {header}"

    track_b_changed = 0
    for r in rows[1:]:
        if len(r) < 3:
            continue
        sid = r[0]
        if sid in b_map:
            new_tb = b_map[sid]
            if r[2] != new_tb:
                r[2] = new_tb
                track_b_changed += 1

    # 카운트
    ta_count = sum(1 for r in rows[1:] if len(r) >= 2 and r[1].strip())
    tb_count = sum(1 for r in rows[1:] if len(r) >= 3 and r[2].strip())

    # 출력
    _OUT.parent.mkdir(parents=True, exist_ok=True)
    with _OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(rows)

    print(f"Combined CSV: {_OUT}")
    print(f"  Total rows: {len(rows) - 1} data rows")
    print(f"  Track A filled: {ta_count}/500")
    print(f"  Track B filled: {tb_count}/50")
    print(f"  Track B sync changes: {track_b_changed}")


if __name__ == "__main__":
    main()
