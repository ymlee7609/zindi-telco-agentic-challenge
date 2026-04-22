#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Track A 로컬 정확도 측정기.

result.csv (scenario_id, prediction) 와 test.json 의 answer 를 비교하여
IoU (intersection-over-union) 기반 accuracy 를 계산.

Usage:
    python agent/track_a/eval_local.py agent/track_a/results_smoke/result.csv
    python agent/track_a/eval_local.py agent/track_a/results_pilot/result.csv --source train
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TEST_JSON = ROOT / "data" / "Track A" / "data" / "Phase_1" / "test.json"
TRAIN_JSON = ROOT / "data" / "Track A" / "data" / "Phase_1" / "train.json"


def iou_score(pred: str, truth: str) -> float:
    """Intersection over Union of answer option sets.

    pred and truth are pipe-separated (e.g., 'C9' or 'C2|C8|C11|C16').
    Empty pred or truth → 0.0.
    """
    if not pred or not truth:
        return 0.0
    p = {x.strip() for x in pred.split("|") if x.strip()}
    t = {x.strip() for x in truth.split("|") if x.strip()}
    if not p or not t:
        return 0.0
    inter = len(p & t)
    union = len(p | t)
    return inter / union if union else 0.0


def load_answers(source_json: Path) -> dict[str, dict]:
    with open(source_json, encoding="utf-8") as f:
        data = json.load(f)
    return {s["scenario_id"]: s for s in data}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("result_csv", type=Path)
    ap.add_argument("--source", choices=["test", "train"], default="test",
                    help="Ground truth source (test.json or train.json)")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    src = TEST_JSON if args.source == "test" else TRAIN_JSON
    answers = load_answers(src)

    total = 0
    matched = 0
    exact = 0
    partial = 0
    wrong = 0
    empty = 0
    score_sum = 0.0
    per_tag: dict[str, list[tuple[float, int]]] = {}

    wrongs: list[dict] = []

    with open(args.result_csv, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            sid = row.get("scenario_id", "")
            pred = (row.get("prediction") or "").strip()
            if sid not in answers:
                continue
            gt = answers[sid].get("answer", "")
            tag = answers[sid].get("tag", "unknown")
            total += 1
            if not pred:
                empty += 1
                wrongs.append({"sid": sid, "pred": pred, "gt": gt, "score": 0.0, "tag": tag})
                per_tag.setdefault(tag, []).append((0.0, 0))
                continue
            score = iou_score(pred, gt)
            score_sum += score
            if score == 1.0:
                exact += 1
                matched += 1
                per_tag.setdefault(tag, []).append((1.0, 1))
            elif score > 0:
                partial += 1
                per_tag.setdefault(tag, []).append((score, 0))
            else:
                wrong += 1
                wrongs.append({"sid": sid, "pred": pred, "gt": gt, "score": 0.0, "tag": tag})
                per_tag.setdefault(tag, []).append((0.0, 0))

    if total == 0:
        print("No scenarios matched ground-truth source. Is --source correct?")
        sys.exit(1)

    print(f"=== Local evaluation: {args.result_csv} vs {args.source}.json ===")
    print(f"Total: {total}")
    print(f"  Exact match: {exact} ({exact / total:.2%})")
    print(f"  Partial IoU: {partial}")
    print(f"  Wrong (IoU 0): {wrong}")
    print(f"  Empty: {empty}")
    print(f"Mean IoU: {score_sum / total:.4f}")
    print()
    print("Per-tag breakdown:")
    for tag, scores in per_tag.items():
        n = len(scores)
        mean_iou = sum(s for s, _ in scores) / n if n else 0.0
        n_exact = sum(x for _, x in scores)
        print(f"  {tag:>18}: n={n:>3} exact={n_exact:>3} mean_iou={mean_iou:.4f}")

    if args.verbose and wrongs:
        print()
        print("Wrong / empty predictions (up to 20):")
        for w in wrongs[:20]:
            print(f"  {w['sid']} [{w['tag']:>16}] pred={w['pred']!r:>30} gt={w['gt']!r}")


if __name__ == "__main__":
    main()
