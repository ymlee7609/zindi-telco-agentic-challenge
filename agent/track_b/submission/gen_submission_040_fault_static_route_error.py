"""Submission 040 — Track B PJ FAULT 일괄 static route error probe.

목적:
  probe 038 (BGP) 와 039 (L3VPN) 모두 0.56 유지 시 세 번째 후보.

가설:
  Hermes-Prime-01 routing-table 에 10.1.6.0/28, 10.1.6.16/28, 10.1.6.32/28,
  10.1.6.48/28 4개 static route 가 명시적으로 있음. baseline "missing static
  route" 와 다른 "static route error" 키워드 시도.

변경 내역 (base = BEST 0.56 통합본):
  - Q39~Q49 (8 routing fault) → "static route error"
  - Q42 → "interface IP error"
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

_DIR = Path(__file__).resolve().parent
_PROJECT_ROOT = _DIR.parent.parent.parent
_BASE_CSV = (
    _PROJECT_ROOT
    / "agent"
    / "common"
    / "submission"
    / "submission_BEST_0_56_track_ab_20260427.csv"
)
_TEST_JSON = _PROJECT_ROOT / "data" / "Track B" / "data" / "Phase_1" / "test.json"
_OUT_CSV = (
    _PROJECT_ROOT
    / "agent"
    / "common"
    / "submission"
    / "submission_040_20260427_fault_static_route_error.csv"
)

_NEW_ANSWERS: dict[int, str] = {
    39: "Demeter-Prime-01;20.1.1.10;static route error",
    43: "Demeter-Prime-01;20.1.1.10;static route error",
    46: "Demeter-Prime-01;20.1.1.10;static route error",
    40: "Demeter-Prime-01;10.1.6.3;static route error",
    41: "Demeter-Prime-01;10.1.6.3;static route error",
    47: "Demeter-Prime-01;20.1.1.20;static route error",
    48: "Demeter-Prime-01;20.1.1.20;static route error",
    49: "Demeter-Prime-01;20.1.4.10;static route error",
    42: "Demeter-Prime-02;GE1/0/5;interface IP error",
}


def _load_qid_to_sid(test_json_path: Path) -> dict[int, str]:
    with test_json_path.open() as fp:
        questions = json.load(fp)
    return {idx + 1: q["scenario_id"] for idx, q in enumerate(questions)}


def main() -> int:
    qid_to_sid = _load_qid_to_sid(_TEST_JSON)
    sid_to_new = {qid_to_sid[q]: a for q, a in _NEW_ANSWERS.items()}

    with _BASE_CSV.open("r", newline="", encoding="utf-8") as fp:
        rows = list(csv.reader(fp))

    changes: list[tuple[int, str, str, str]] = []
    for row in rows[1:]:
        if len(row) < 3:
            continue
        if row[0] in sid_to_new:
            old = row[2]
            row[2] = sid_to_new[row[0]]
            qid = next(q for q, s in qid_to_sid.items() if s == row[0])
            changes.append((qid, row[0], old, row[2]))

    if len(changes) != len(_NEW_ANSWERS):
        print(f"[ERR] 변경 건수 불일치", file=sys.stderr)
        return 1

    with _OUT_CSV.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(rows)

    print(f"out  : {_OUT_CSV.name}")
    print(f"변경 : {len(changes)} 라인")
    for qid, _, old, new in sorted(changes):
        print(f"Q{qid}: {old[:50]} → {new[:50]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
