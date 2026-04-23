#!/usr/bin/env python3
"""v10 submission → v11: Fault 24문제 (Q17~Q28, Q39~Q50) 만 v11_fault 결과로 갱신.

v10 과 byte-identical 인 v9 base + Q29 v10 자동 + Q17~28,39~50 v11 개선 Fault.
TODO-16 FAULT prompt + validate_fault_answer 효과 반영.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TEST_JSON = ROOT / "data/Track B/data/Phase_1/test.json"
V10_CSV = ROOT / "agent/track_b/submission/submission_v6_full_v10.csv"
V11_CSV = ROOT / "agent/track_b/submission/submission_v6_full_v11.csv"
V11_DETAIL = ROOT / "agent/track_b/results_v11_fault/eval_detail.jsonl"

FAULT_QIDS = frozenset(list(range(17, 29)) + list(range(39, 51)))


def _flatten(text: str) -> str:
    return (text or "").replace("\r\n", "\\n").replace("\r", "\\n").replace("\n", "\\n")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--override-qids",
        default=",".join(str(q) for q in sorted(FAULT_QIDS)),
        help=f"v11 로 덮어쓸 Q id (콤마 구분). 기본: Fault 24개 {sorted(FAULT_QIDS)}",
    )
    args = ap.parse_args()
    override_qids = {int(x) for x in args.override_qids.split(",") if x.strip()}

    with open(TEST_JSON, encoding="utf-8") as f:
        data = json.load(f)
    qid_to_sid = {e["task"]["id"]: e["scenario_id"] for e in data}

    new_answers: dict[int, str] = {}
    with open(V11_DETAIL, encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            qid = r["question_id"]
            if qid not in override_qids:
                continue
            ans = _flatten(r.get("answer", "") or "")
            new_answers[qid] = ans
    print(f"[v11] overrides for Q (from v11_fault): {sorted(new_answers.keys())}")

    sid_overrides = {
        qid_to_sid[qid]: ans for qid, ans in new_answers.items() if qid in qid_to_sid
    }

    with open(V10_CSV, encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    replaced = 0
    same = 0
    for r in rows:
        if len(r) >= 3 and r[0] in sid_overrides:
            old_b = r[2]
            new_b = sid_overrides[r[0]]
            if old_b != new_b:
                r[2] = new_b
                replaced += 1
            else:
                same += 1

    V11_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(V11_CSV, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, lineterminator="\r\n")
        w.writerow(header)
        w.writerows(rows)

    print(f"[v11] wrote {V11_CSV}")
    print(f"[v11] rows={len(rows)}, replaced={replaced}, same_as_v10={same}")


if __name__ == "__main__":
    main()
