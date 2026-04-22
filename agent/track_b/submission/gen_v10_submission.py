#!/usr/bin/env python3
"""v9 submission → v10: best-of merge.

v10 test 결과와 v9 결과를 best-of 로 선별. 기본 정책:
- Q29: v10 채택 (v9 는 XML 수동, v10 은 3/3 자동 정답 도출)
- Q30, Q33: v9 유지 (v10 회귀 또는 미실행)
- Q31, Q32: v9 유지 (v10 HIGH-ALIAS 과잉으로 회귀 — 6/6→4/6, 3/3→2/3)

TODO-14 의 best-of 매핑 표에 따름. 향후 TODO-15 적용 후 재측정 필요.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TEST_JSON = ROOT / "data/Track B/data/Phase_1/test.json"
V9_CSV = ROOT / "agent/track_b/submission/submission_v6_full_v9.csv"
V10_CSV = ROOT / "agent/track_b/submission/submission_v6_full_v10.csv"
V10_DETAIL = ROOT / "agent/track_b/results_v10_test/eval_detail.jsonl"

# Best-of 정책 — v10 으로 갱신할 Q 만 명시
V10_OVERRIDE_QIDS = {29}


def _flatten(text: str) -> str:
    return (text or "").replace("\r\n", "\\n").replace("\r", "\\n").replace("\n", "\\n")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--override-qids",
        default=",".join(str(q) for q in sorted(V10_OVERRIDE_QIDS)),
        help="v10 으로 덮어쓸 Q id (콤마 구분). 기본: 29",
    )
    args = ap.parse_args()
    override_qids = {int(x) for x in args.override_qids.split(",") if x.strip()}

    # 1. task.id → scenario_id 매핑
    with open(TEST_JSON, encoding="utf-8") as f:
        data = json.load(f)
    qid_to_sid = {e["task"]["id"]: e["scenario_id"] for e in data}

    # 2. v10 detail → qid: answer (literal \n flatten). override_qids 만 취함.
    new_answers: dict[int, str] = {}
    with open(V10_DETAIL, encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            qid = r["question_id"]
            if qid not in override_qids:
                continue
            ans = _flatten(r.get("answer", "") or "")
            new_answers[qid] = ans
    print(f"[v10] overrides for Q (from v10_test): {sorted(new_answers.keys())}")
    sid_overrides = {
        qid_to_sid[qid]: ans for qid, ans in new_answers.items() if qid in qid_to_sid
    }

    # 3. v9 rows 복사 + overrides
    with open(V9_CSV, encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    replaced = 0
    for r in rows:
        if len(r) >= 3 and r[0] in sid_overrides:
            old_b = r[2]
            new_b = sid_overrides[r[0]]
            if old_b != new_b:
                r[2] = new_b
                replaced += 1

    V10_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(V10_CSV, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, lineterminator="\r\n")
        w.writerow(header)
        w.writerows(rows)

    print(f"[v10] wrote {V10_CSV}")
    print(f"[v10] rows={len(rows)}, replaced={replaced}")


if __name__ == "__main__":
    main()
