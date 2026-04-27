#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Track A 패턴 분석기.

train.json의 2000 정답을 10-pattern으로 자동 분류하고,
eval_detail.jsonl 결과와 매칭하여 패턴별 정확도/오분류 매트릭스를 생성.

Usage:
    # 패턴 분포만 분석
    python agent/track_a/analyze_patterns.py

    # eval_detail.jsonl과 매칭하여 패턴별 정확도 분석
    python agent/track_a/analyze_patterns.py --eval agent/track_a/results_train_eval_50_v4/eval_detail.jsonl

    # 오분류 상세 출력
    python agent/track_a/analyze_patterns.py --eval <path> --verbose
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
TRAIN_JSON = ROOT / "data" / "Track A" / "data" / "Phase_1" / "train.json"


# --- 10-Pattern 분류 (7-pattern 확장) ---

LABEL_PATTERNS = {
    # 기존 7-pattern
    "P1_late_HO": lambda l: ("decrease" in l) and ("a3" in l or "intrafreqhoa3" in l),
    "P2_pingpong": lambda l: ("increase" in l) and ("a3" in l or "intrafreqhoa3" in l),
    "P3_overshoot_power": lambda l: ("decrease" in l) and ("power" in l),
    "P3_overshoot_tilt": lambda l: ("press" in l) and ("tilt" in l),
    "P4_coverage_power": lambda l: ("increase" in l) and ("power" in l),
    "P4_coverage_tilt": lambda l: ("lift" in l) and ("tilt" in l),
    "P4_coverage_azimuth": lambda l: ("azimuth" in l),
    "P5_server": lambda l: ("check test server" in l) or ("transmission issues" in l),
    "P7_insufficient": lambda l: ("insufficient data" in l) or ("more data" in l),
    # 신규 3 패턴 (7-pattern 라이브러리에서 누락됨)
    "P8_pdcch": lambda l: ("pdcch" in l),
    "P9_add_neighbor": lambda l: ("add neighbor" in l),
    "P10_coverage_threshold": lambda l: ("threshold" in l or "thld" in l) and ("a3" not in l),
}


def classify_label(label: str) -> str:
    """단일 옵션 라벨을 패턴으로 분류."""
    lw = label.lower()
    for pattern_name, matcher in LABEL_PATTERNS.items():
        if matcher(lw):
            return pattern_name
    return "UNKNOWN"


def classify_scenario(scenario: dict[str, Any]) -> str:
    """시나리오의 정답을 기반으로 패턴 분류."""
    answer_ids = [a.strip() for a in scenario["answer"].split("|")]
    opts = {o["id"]: o["label"] for o in scenario.get("task", {}).get("options", [])}
    labels = [opts.get(aid, "") for aid in answer_ids]
    patterns = [classify_label(l) for l in labels]

    tag = scenario["tag"]
    n = len(answer_ids)

    if n == 1:
        return patterns[0]
    else:
        # multi-answer: 주요 액션 그룹으로 분류
        unique_groups = set()
        for p in patterns:
            # P3 계열 (overshoot combo)
            if p.startswith("P3_") or (p == "P2_pingpong"):
                unique_groups.add("P3")
            # P4 계열 (coverage combo)
            elif p.startswith("P4_"):
                unique_groups.add("P4")
            elif p.startswith("P1_"):
                unique_groups.add("P1")
            else:
                unique_groups.add(p)

        if "P3" in unique_groups:
            return "P3_overshoot_multi"
        elif "P4" in unique_groups:
            return "P4_coverage_multi"
        elif "P1" in unique_groups:
            return "P1_multi"
        else:
            return "MULTI_mixed"


def classify_prediction(prediction: str, scenario: dict[str, Any]) -> str:
    """예측값을 기반으로 패턴 분류 (정답 옵션 매핑 사용)."""
    if not prediction:
        return "EMPTY"
    pred_ids = [p.strip() for p in prediction.split("|")]
    opts = {o["id"]: o["label"] for o in scenario.get("task", {}).get("options", [])}
    labels = [opts.get(pid, "") for pid in pred_ids]
    patterns = [classify_label(l) for l in labels if l]

    if not patterns:
        return "UNKNOWN_PRED"

    if len(patterns) == 1:
        return patterns[0]
    else:
        unique_groups = set()
        for p in patterns:
            if p.startswith("P3_") or p == "P2_pingpong":
                unique_groups.add("P3")
            elif p.startswith("P4_"):
                unique_groups.add("P4")
            elif p.startswith("P1_"):
                unique_groups.add("P1")
            else:
                unique_groups.add(p)

        if "P3" in unique_groups:
            return "P3_overshoot_multi"
        elif "P4" in unique_groups:
            return "P4_coverage_multi"
        else:
            return "MULTI_mixed"


def iou_score(pred: str, truth: str) -> float:
    """IoU 계산."""
    if not pred or not truth:
        return 0.0
    p = {x.strip() for x in pred.split("|") if x.strip()}
    t = {x.strip() for x in truth.split("|") if x.strip()}
    if not p or not t:
        return 0.0
    return len(p & t) / len(p | t)


def load_train() -> dict[str, dict]:
    """train.json 로드."""
    with open(TRAIN_JSON, encoding="utf-8") as f:
        data = json.load(f)
    return {s["scenario_id"]: s for s in data}


def load_eval_detail(path: Path) -> dict[str, dict]:
    """eval_detail.jsonl 로드."""
    results = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            sid = d.get("scenario_id")
            if sid:
                results[sid] = d
    return results


def analyze_distribution(train: dict[str, dict]) -> None:
    """패턴 분포 분석."""
    pattern_counts: Counter = Counter()
    pattern_tag: dict[str, Counter] = {}

    for sid, s in train.items():
        p = classify_scenario(s)
        pattern_counts[p] += 1
        pattern_tag.setdefault(p, Counter())[s["tag"]] += 1

    print("=" * 70)
    print("패턴 분포 (Train 2000)")
    print("=" * 70)
    print(f"{'Pattern':<25} {'Count':>6} {'Pct':>6}  {'Tags'}")
    print("-" * 70)

    # 기존 7-pattern 먼저
    known_7 = ["P1_late_HO", "P2_pingpong", "P3_overshoot_multi",
                "P4_coverage_multi", "P4_coverage_tilt", "P5_server",
                "P6_excessive_downtilt", "P7_insufficient"]

    for p, c in sorted(pattern_counts.items(), key=lambda x: -x[1]):
        pct = c / len(train) * 100
        tags_str = ", ".join(f"{t}={n}" for t, n in pattern_tag.get(p, {}).items())
        marker = "" if any(p.startswith(k[:2]) for k in known_7) else " *** NEW"
        print(f"  {p:<23} {c:>6} {pct:>5.1f}%  {tags_str}{marker}")

    print(f"  {'TOTAL':<23} {sum(pattern_counts.values()):>6}")
    print()

    # 7-pattern 커버리지
    covered = sum(c for p, c in pattern_counts.items()
                  if any(p.startswith(f"P{i}") for i in [1, 2, 3, 4, 5, 7]))
    # P6는 P4_coverage_tilt의 single이 P6
    p6_count = pattern_counts.get("P4_coverage_tilt", 0)
    covered += p6_count
    new_count = sum(c for p, c in pattern_counts.items()
                    if p.startswith(("P8_", "P9_", "P10_")))
    print(f"기존 7-pattern 커버리지: {covered - p6_count}/{len(train)} ({(covered-p6_count)/len(train)*100:.1f}%)")
    print(f"신규 패턴 (P8/P9/P10): {new_count}/{len(train)} ({new_count/len(train)*100:.1f}%)")
    print()
    return pattern_counts


def analyze_eval(train: dict, eval_results: dict, verbose: bool = False) -> None:
    """패턴별 정확도 및 오분류 분석."""
    # 패턴별 통계
    stats: dict[str, dict] = defaultdict(lambda: {
        "total": 0, "exact": 0, "partial": 0, "wrong": 0, "empty": 0,
        "iou_sum": 0.0, "fallback": 0,
    })
    # 오분류 매트릭스: truth_pattern -> pred_pattern -> count
    confusion: dict[str, Counter] = defaultdict(Counter)
    # 상세 오답 목록
    wrong_details: list[dict] = []

    for sid, ev in eval_results.items():
        if sid not in train:
            continue
        scenario = train[sid]
        truth_pattern = classify_scenario(scenario)
        pred = (ev.get("prediction") or "").strip()
        gt = scenario["answer"]
        score = iou_score(pred, gt)

        s = stats[truth_pattern]
        s["total"] += 1
        s["iou_sum"] += score

        if ev.get("fallback_used"):
            s["fallback"] += 1

        if not pred:
            s["empty"] += 1
            confusion[truth_pattern]["EMPTY"] += 1
        elif score == 1.0:
            s["exact"] += 1
            confusion[truth_pattern][truth_pattern] += 1  # correct
        elif score > 0:
            s["partial"] += 1
            pred_pattern = classify_prediction(pred, scenario)
            confusion[truth_pattern][pred_pattern] += 1
        else:
            s["wrong"] += 1
            pred_pattern = classify_prediction(pred, scenario)
            confusion[truth_pattern][pred_pattern] += 1
            wrong_details.append({
                "sid": sid[:12],
                "truth_pattern": truth_pattern,
                "pred_pattern": pred_pattern,
                "gt": gt,
                "pred": pred,
                "tag": scenario["tag"],
                "fallback": ev.get("fallback_used", False),
            })

    print("=" * 80)
    print("패턴별 정확도 분석")
    print("=" * 80)
    print(f"{'Pattern':<25} {'N':>4} {'Exact':>6} {'Part':>5} {'Wrong':>6} {'Empty':>5} {'FB':>4} {'IoU':>7}")
    print("-" * 80)

    total_n = total_exact = total_iou = 0
    for p in sorted(stats.keys()):
        s = stats[p]
        n = s["total"]
        if n == 0:
            continue
        mean_iou = s["iou_sum"] / n
        exact_pct = s["exact"] / n * 100
        print(f"  {p:<23} {n:>4} {s['exact']:>3}({exact_pct:>4.0f}%) {s['partial']:>5} "
              f"{s['wrong']:>3}     {s['empty']:>3}   {s['fallback']:>3} {mean_iou:>6.3f}")
        total_n += n
        total_exact += s["exact"]
        total_iou += s["iou_sum"]

    if total_n:
        print("-" * 80)
        print(f"  {'TOTAL':<23} {total_n:>4} {total_exact:>3}({total_exact/total_n*100:>4.0f}%) "
              f"{'':>5} {'':>6} {'':>5} {'':>4} {total_iou/total_n:>6.3f}")

    # 오분류 매트릭스 (주요 혼동 패턴)
    print()
    print("=" * 80)
    print("오분류 매트릭스 (Truth → Predicted, top confusions)")
    print("=" * 80)
    for truth_p in sorted(confusion.keys()):
        entries = confusion[truth_p]
        # 자기 자신(correct) 제외, 상위 혼동 패턴
        wrong_entries = {k: v for k, v in entries.items() if k != truth_p}
        if wrong_entries:
            top = sorted(wrong_entries.items(), key=lambda x: -x[1])[:5]
            correct = entries.get(truth_p, 0)
            total_for_p = sum(entries.values())
            print(f"  {truth_p}")
            print(f"    Correct: {correct}/{total_for_p}")
            for pred_p, cnt in top:
                print(f"    → {pred_p}: {cnt}")
            print()

    # 상세 오답 (verbose)
    if verbose and wrong_details:
        print()
        print("=" * 80)
        print(f"오답 상세 (총 {len(wrong_details)}건, 상위 30)")
        print("=" * 80)
        for w in wrong_details[:30]:
            print(f"  {w['sid']} [{w['tag']:>16}] "
                  f"truth={w['truth_pattern']:<23} pred_pat={w['pred_pattern']:<23} "
                  f"gt={w['gt']!r:<15} pred={w['pred']!r:<15} fb={w['fallback']}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Track A 패턴 분석기")
    ap.add_argument("--eval", type=Path, default=None,
                    help="eval_detail.jsonl path for accuracy analysis")
    ap.add_argument("--verbose", "-v", action="store_true",
                    help="Show detailed wrong predictions")
    args = ap.parse_args()

    train = load_train()
    print(f"Train scenarios loaded: {len(train)}")
    print()

    analyze_distribution(train)

    if args.eval:
        if not args.eval.exists():
            print(f"ERROR: {args.eval} not found")
            sys.exit(1)
        eval_results = load_eval_detail(args.eval)
        print(f"Eval results loaded: {len(eval_results)}")
        print()
        analyze_eval(train, eval_results, verbose=args.verbose)


if __name__ == "__main__":
    main()
