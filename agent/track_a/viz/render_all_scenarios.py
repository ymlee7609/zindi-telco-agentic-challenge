#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Train 2000 전체 시나리오 시각화 이미지 배치 생성.

각 시나리오마다 2-패널 PNG (top-view + 시계열).
기존 render_pattern_topology.py의 render_scenario_figure() 재사용.

Output: docs/track_a/questions/images/train_{NNN}.png (0-padded 4자리)

Usage:
    # 처음 10개 샘플
    python agent/track_a/viz/render_all_scenarios.py --sample 10

    # 전체 2000개
    python agent/track_a/viz/render_all_scenarios.py --all

    # 특정 범위
    python agent/track_a/viz/render_all_scenarios.py --start 100 --end 200
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# 같은 디렉토리의 렌더러 임포트
sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_pattern_topology import parse_pipe, render_scenario_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
TRAIN_JSON = REPO_ROOT / "data" / "Track A" / "data" / "Phase_1" / "train.json"
TEST_JSON = REPO_ROOT / "data" / "Track A" / "data" / "Phase_1" / "test.json"
OUT_DIR_TRAIN = REPO_ROOT / "docs" / "track_a" / "questions" / "train" / "images"
OUT_DIR_TEST = REPO_ROOT / "docs" / "track_a" / "questions" / "test" / "images"

# analyze_patterns.py에서 가져온 패턴 분류
LABEL_PATTERNS = {
    "P1_Late_HO": lambda l: ("decrease" in l) and ("a3" in l or "intrafreqhoa3" in l),
    "P2_Pingpong": lambda l: ("increase" in l) and ("a3" in l or "intrafreqhoa3" in l),
    "P3_Overshoot": lambda l: (("decrease" in l) and ("power" in l)) or (("press" in l) and ("tilt" in l)),
    "P4_Coverage": lambda l: (("increase" in l) and ("power" in l)) or (("lift" in l) and ("tilt" in l)) or ("azimuth" in l),
    "P5_Server": lambda l: ("check test server" in l) or ("transmission issues" in l),
    "P7_Insufficient": lambda l: ("insufficient data" in l) or ("more data" in l),
    "P8_PDCCH": lambda l: ("pdcch" in l),
    "P9_Neighbor": lambda l: ("add neighbor" in l),
    "P10_Threshold": lambda l: ("threshold" in l or "thld" in l) and ("a3" not in l),
}


def classify_answer(scenario: dict) -> str:
    answer = scenario.get("answer", "To be determined")
    if answer == "To be determined":
        return "Test"
    aids = [a.strip() for a in answer.split("|")]
    opts = {o["id"]: o["label"].lower() for o in scenario.get("task", {}).get("options", [])}
    label = opts.get(aids[0], "")
    for name, matcher in LABEL_PATTERNS.items():
        if matcher(label):
            return name
    return "Unknown"


def main() -> int:
    ap = argparse.ArgumentParser(description="Train/Test 전수 시각화 배치 생성")
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--sample", type=int, help="처음 N개만")
    group.add_argument("--all", action="store_true", help="전체 변환")
    group.add_argument("--start", type=int, help="시작 인덱스 (--end와 함께)")
    ap.add_argument("--end", type=int, help="종료 인덱스 (exclusive)")
    ap.add_argument("--source", choices=["train", "test"], default="train",
                    help="데이터 소스 (train.json or test.json)")
    ap.add_argument("--dpi", type=int, default=100, help="이미지 DPI (기본 100)")
    ap.add_argument("--skip-existing", action="store_true", help="이미 존재하는 이미지 건너뛰기")
    args = ap.parse_args()

    src_json = TRAIN_JSON if args.source == "train" else TEST_JSON
    out_dir = OUT_DIR_TRAIN if args.source == "train" else OUT_DIR_TEST

    print(f"Loading {src_json.name} ...")
    with src_json.open() as f:
        data = json.load(f)
    print(f"  -> {len(data)} scenarios ({args.source})")

    out_dir.mkdir(parents=True, exist_ok=True)

    if args.sample:
        start, end = 0, min(args.sample, len(data))
    elif args.all:
        start, end = 0, len(data)
    else:
        start = args.start or 0
        end = args.end or len(data)

    total = end - start
    success = skip = fail = 0
    t_start = time.time()

    for idx in range(start, end):
        out_path = out_dir / f"{args.source}_{idx:04d}.png"

        if args.skip_existing and out_path.exists():
            skip += 1
            continue

        scenario = data[idx]
        pattern = classify_answer(scenario)
        answer = scenario.get("answer", "?")
        tag = scenario.get("tag", "?")

        try:
            cells = parse_pipe(scenario["data"]["network_configuration_data"])
            ue_rows = parse_pipe(scenario["data"]["user_plane_data"])

            fig = plt.figure(figsize=(16.0, 9.5))
            render_scenario_figure(
                fig, cells, ue_rows,
                code=pattern,
                name=f"{args.source}[{idx}]",
                idx=idx,
                description=f"{tag} | {pattern}",
                answer=answer,
            )
            fig.savefig(out_path, dpi=args.dpi, bbox_inches="tight")
            plt.close(fig)
            success += 1

        except Exception as e:
            plt.close("all")
            fail += 1
            print(f"  [FAIL] {args.source}[{idx}]: {e}")
            continue

        # 진행률 (50개마다 출력)
        done = success + skip + fail
        if done % 50 == 0 or done == total:
            elapsed = time.time() - t_start
            rate = done / elapsed if elapsed > 0 else 0
            eta = (total - done) / rate if rate > 0 else 0
            print(f"  [{done}/{total}] ok={success} skip={skip} fail={fail} "
                  f"({elapsed:.0f}s elapsed, ETA {eta:.0f}s)")

    elapsed = time.time() - t_start
    print(f"\nDone: {success} rendered, {skip} skipped, {fail} failed ({elapsed:.0f}s)")
    print(f"Output: {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
