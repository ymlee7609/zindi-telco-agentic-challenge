#!/usr/bin/env python3
"""v10 vs v11 Fault 답 차이 요약. Reason 변화 / 라인 수 변화 집계."""
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TEST_JSON = ROOT / "data/Track B/data/Phase_1/test.json"
V10_CSV = ROOT / "agent/track_b/submission/submission_v6_full_v10.csv"
V11_CSV = ROOT / "agent/track_b/submission/submission_v6_full_v11.csv"

FAULT_QIDS = list(range(17, 29)) + list(range(39, 51))


def load_map(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    with open(path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            out[row["ID"]] = row.get("Track B", "") or ""
    return out


def split_lines(cell: str) -> list[str]:
    return [x for x in cell.split("\\n") if x]


def reason_of(line: str) -> str:
    parts = line.split(";")
    return parts[2] if len(parts) >= 3 else "<malformed>"


def main() -> None:
    with open(TEST_JSON, encoding="utf-8") as f:
        data = json.load(f)
    qid_to_sid = {e["task"]["id"]: e["scenario_id"] for e in data}

    v10 = load_map(V10_CSV)
    v11 = load_map(V11_CSV)

    print(f"{'Q':>3}  {'v10_lines':>9}  {'v11_lines':>9}  {'same':>4}  reason_delta")
    v10_reasons: Counter[str] = Counter()
    v11_reasons: Counter[str] = Counter()
    for qid in FAULT_QIDS:
        sid = qid_to_sid.get(qid)
        if not sid:
            continue
        a = split_lines(v10.get(sid, ""))
        b = split_lines(v11.get(sid, ""))
        same = "yes" if v10.get(sid) == v11.get(sid) else "no"
        v10r = [reason_of(x) for x in a]
        v11r = [reason_of(x) for x in b]
        v10_reasons.update(v10r)
        v11_reasons.update(v11r)
        delta = ""
        if v10r != v11r:
            delta = f"{set(v10r) - set(v11r) or '{}'} -> {set(v11r) - set(v10r) or '{}'}"
        print(f"Q{qid:>2}  {len(a):>9}  {len(b):>9}  {same:>4}  {delta}")

    print()
    print("=== v10 reason distribution ===")
    for r, c in v10_reasons.most_common():
        print(f"  {c:>3}  {r}")
    print()
    print("=== v11 reason distribution ===")
    for r, c in v11_reasons.most_common():
        print(f"  {c:>3}  {r}")


if __name__ == "__main__":
    main()
