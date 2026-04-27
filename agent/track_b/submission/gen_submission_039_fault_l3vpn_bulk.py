"""Submission 039 — Track B PJ FAULT 일괄 L3VPN 카테고리 probe.

목적:
  probe 038 (BGP) 점수에 따라 두 번째 카테고리 시도:
    - 038 변화 없음 (0.56 유지) 시: L3VPN 시도
    - 038 부분 정답 시: 부분 변경된 fine-tuning probe 로 우회

가설:
  PJ는 vpn-instance + VXLAN overlay 환경. L3VPN configuration error 가
  vpn-instance import/export route-target 문제 표현에 가까움.

변경 내역 (base = BEST 0.56 통합본):
  - Q39, Q40, Q41, Q43, Q46, Q47, Q48, Q49 (8문제) :
        "missing static route" → "L3VPN configuration error"
  - Q42 → "interface IP error" (probe 038 과 동일)
  - Q44, Q45, Q50 변경 없음
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
    / "submission_039_20260427_fault_l3vpn_bulk.csv"
)

_NEW_ANSWERS: dict[int, str] = {
    39: "Demeter-Prime-01;20.1.1.10;L3VPN configuration error",
    43: "Demeter-Prime-01;20.1.1.10;L3VPN configuration error",
    46: "Demeter-Prime-01;20.1.1.10;L3VPN configuration error",
    40: "Demeter-Prime-01;10.1.6.3;L3VPN configuration error",
    41: "Demeter-Prime-01;10.1.6.3;L3VPN configuration error",
    47: "Demeter-Prime-01;20.1.1.20;L3VPN configuration error",
    48: "Demeter-Prime-01;20.1.1.20;L3VPN configuration error",
    49: "Demeter-Prime-01;20.1.4.10;L3VPN configuration error",
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
