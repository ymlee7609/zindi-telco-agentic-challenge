"""Submission serial 017 생성.

목적: TOPO 답변의 literal `\\n` 을 실제 개행으로 변환
베이스: submission_v12_topofault_rt.csv (Zindi serial 016, 점수 0.44)
변경: TOPO 11개 (Q01-06, Q29-33) 의 Track B 답변에서 `\\n` → 실제 개행
결과: submission_017_20260423_topo_newline_fix.csv

이유: submission_v12_topofault_rt.csv 의 TOPO 답변이 literal `\\n` (backslash-n 문자)
      형태로 저장되어 있음. Zindi 질문이 "each line represents one link,
      no extra whitespace characters before/after/within each line" 를 요구하므로
      literal `\\n` 이 채점기에서 "추가 whitespace" 로 간주되어 오답 처리될 가능성.

Usage:
    python3 agent/track_b/submission/gen_submission_017.py --dry-run
    python3 agent/track_b/submission/gen_submission_017.py
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# 경로
# ---------------------------------------------------------------------------

_THIS_DIR = Path(__file__).resolve().parent
_PROJECT_ROOT = _THIS_DIR.parent.parent.parent

_TEST_JSON = _PROJECT_ROOT / "data" / "Track B" / "data" / "Phase_1" / "test.json"
_BASE_CSV = _THIS_DIR / "submission_v12_topofault_rt.csv"
_OUT_CSV = _THIS_DIR / "submission_017_20260423_topo_newline_fix.csv"

# TOPO qid (link restoration 유형)
_TOPO_QIDS = [1, 2, 3, 4, 5, 6, 29, 30, 31, 32, 33]


def _load_topo_sid_set() -> set[str]:
    with open(_TEST_JSON, encoding="utf-8") as f:
        scenarios = json.load(f)
    qid2sid = {s["task"]["id"]: s["scenario_id"] for s in scenarios}
    return {qid2sid[q] for q in _TOPO_QIDS if q in qid2sid}


def _fix_newlines(text: str) -> str:
    """literal `\\n` (backslash + n) → 실제 개행."""
    return text.replace("\\n", "\n")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="submission 017 생성 (TOPO literal \\n → real newline)"
    )
    parser.add_argument("--dry-run", action="store_true", help="저장 없이 변경 사항만 출력")
    args = parser.parse_args()

    if not _BASE_CSV.exists():
        print(f"[ERROR] base CSV 없음: {_BASE_CSV}", file=sys.stderr)
        return 1

    topo_sids = _load_topo_sid_set()
    print(f"[INFO] TOPO scenarios: {len(topo_sids)}")

    with open(_BASE_CSV, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []

    changes: list[tuple[str, str, str]] = []
    for row in rows:
        sid = row["ID"]
        if sid not in topo_sids:
            continue
        original = row.get("Track B", "") or ""
        if not original:
            continue
        fixed = _fix_newlines(original)
        if fixed != original:
            changes.append((sid, original, fixed))
            if not args.dry_run:
                row["Track B"] = fixed

    print(f"\n[PLAN] 수정 예정: {len(changes)}")
    for sid, old, new in changes:
        old_escaped = old.replace("\n", " ").replace("\\n", r"\n")
        new_lines = new.count("\n") + 1
        print(f"\n--- {sid} ---")
        print(f"  before (repr, first 140): {old_escaped[:140]}")
        print(f"  after : {new_lines} lines")

    if args.dry_run:
        print("\n[DRY-RUN] 파일 저장 안 함.")
        return 0

    with open(_OUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n[SAVED] {_OUT_CSV}")
    print(f"        rows={len(rows)}, fixed={len(changes)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
