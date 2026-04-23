"""Track A + Track B 병합 → submission_combined.csv.

소스:
- Track A: agent/track_a/submission/submission_v2.csv (500 answers)
- Track B: agent/track_b/submission/submission_018_20260423_ground_truth.csv (50 answers)

출력:
- agent/common/submission/submission_combined.csv (550 rows, Track A+B 완성)

기존 merge_submission.update_track 재사용. literal `\n` 포맷 유지.
"""
# pyright: reportMissingImports=false

from __future__ import annotations

import csv
import sys
from pathlib import Path

_THIS = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS))

from merge_submission import update_track, status, COMBINED  # type: ignore

_PROJECT_ROOT = _THIS.parent.parent.parent
_TRACK_A_CSV = _PROJECT_ROOT / "agent" / "track_a" / "submission" / "submission_v2.csv"
_TRACK_B_CSV = _PROJECT_ROOT / "agent" / "track_b" / "submission" / "submission_018_20260423_ground_truth.csv"


def _load_track(path: Path, col: str) -> dict[str, str]:
    """CSV 에서 {ID: track_column} 추출 (비어있지 않은 값만)."""
    result: dict[str, str] = {}
    with path.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            val = (row.get(col) or "").strip()
            if val:
                result[row["ID"]] = val
    return result


def main() -> int:
    if not _TRACK_A_CSV.exists():
        print(f"[ERROR] Track A CSV 없음: {_TRACK_A_CSV}", file=sys.stderr)
        return 1
    if not _TRACK_B_CSV.exists():
        print(f"[ERROR] Track B CSV 없음: {_TRACK_B_CSV}", file=sys.stderr)
        return 1

    preds_a = _load_track(_TRACK_A_CSV, "Track A")
    preds_b = _load_track(_TRACK_B_CSV, "Track B")

    print(f"[INFO] Track A preds: {len(preds_a)} from {_TRACK_A_CSV.name}")
    print(f"[INFO] Track B preds: {len(preds_b)} from {_TRACK_B_CSV.name}")

    # 기존 combined 에 덮어쓰기
    update_track("A", preds_a, verbose=True)
    update_track("B", preds_b, verbose=True)

    print()
    print("[FINAL]")
    status()
    print(f"\n[OUTPUT] {COMBINED}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
