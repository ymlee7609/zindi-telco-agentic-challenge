#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Track A RAG (Retrieval-Augmented Generation).

각 scenario 를 14-dim 수치 특징 벡터로 변환하고, train 2000 의 사전 계산된 feature 를
이용해 가장 유사한 top-k scenario 를 검색. 검색된 scenario 와 그 정답을 dynamic
few-shot 으로 agent 에 주입하면 패턴 인식이 강화된다.

특징 (14-dim):
  [0] TP min, [1] TP max, [2] TP avg, [3] TP drop ratio (max-min)/max
  [4] SINR min, [5] SINR max, [6] SINR avg
  [7] RSRP min, [8] RSRP max, [9] RSRP avg
  [10] Unique serving PCI count (1=stable, >1=pingpong/handover)
  [11] Cell 수 (ncd rows)
  [12] Avg A3 Offset (over all cells, in 0.5dB units)
  [13] Max total downtilt (Mechanical + Digital)

Usage (CLI):
    python rag.py --precompute        # train.json → .moai/cache/track_a_train_features.json
    python rag.py --query <sid>       # find top-3 similar train scenarios for a scenario
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
TRAIN_JSON = ROOT / "data" / "Track A" / "data" / "Phase_1" / "train.json"
TEST_JSON = ROOT / "data" / "Track A" / "data" / "Phase_1" / "test.json"
CACHE_FILE = ROOT / ".moai" / "cache" / "track_a_train_features.json"


def parse_pipe_csv(text: str) -> list[dict[str, str]]:
    lines = [ln.rstrip("\r") for ln in (text or "").strip().split("\n") if ln.strip()]
    if not lines:
        return []
    header = lines[0].split("|")
    return [dict(zip(header, ln.split("|"))) for ln in lines[1:]]


def _safe_float(v: Any, default: float = 0.0) -> float:
    try:
        return float(v)
    except (TypeError, ValueError):
        return default


def _safe_int(v: Any, default: int = 0) -> int:
    try:
        return int(v)
    except (TypeError, ValueError):
        return default


def extract_features(scenario: dict) -> list[float]:
    """14-dim numeric feature vector for a scenario."""
    data = scenario.get("data", {})
    upd = parse_pipe_csv(data.get("user_plane_data", ""))
    ncd = parse_pipe_csv(data.get("network_configuration_data", ""))

    tp_col = "5G KPI PCell Layer2 MAC DL Throughput [Mbps]"
    sinr_col = "5G KPI PCell RF Serving SS-SINR [dB]"
    rsrp_col = "5G KPI PCell RF Serving SS-RSRP [dBm]"
    pci_col = "5G KPI PCell RF Serving PCI"

    tps = [_safe_float(r.get(tp_col)) for r in upd if r.get(tp_col)]
    sinrs = [_safe_float(r.get(sinr_col)) for r in upd if r.get(sinr_col)]
    rsrps = [_safe_float(r.get(rsrp_col)) for r in upd if r.get(rsrp_col)]
    pcis = [r.get(pci_col) for r in upd if r.get(pci_col)]

    tp_min = min(tps) if tps else 0.0
    tp_max = max(tps) if tps else 0.0
    tp_avg = sum(tps) / len(tps) if tps else 0.0
    tp_drop = (tp_max - tp_min) / tp_max if tp_max > 0 else 0.0

    sinr_min = min(sinrs) if sinrs else 0.0
    sinr_max = max(sinrs) if sinrs else 0.0
    sinr_avg = sum(sinrs) / len(sinrs) if sinrs else 0.0

    rsrp_min = min(rsrps) if rsrps else -120.0
    rsrp_max = max(rsrps) if rsrps else -60.0
    rsrp_avg = sum(rsrps) / len(rsrps) if rsrps else -90.0

    unique_pci = len(set(pcis)) if pcis else 1
    n_cells = len(ncd)

    a3_vals = [_safe_int(c.get("IntraFreqHoA3Offset [0.5dB]"), 6) for c in ncd]
    avg_a3 = sum(a3_vals) / len(a3_vals) if a3_vals else 6.0

    total_tilts = [
        _safe_int(c.get("Mechanical Downtilt")) + _safe_int(c.get("Digital Tilt"))
        for c in ncd
    ]
    max_tilt = max(total_tilts) if total_tilts else 0

    return [
        tp_min, tp_max, tp_avg, tp_drop,
        sinr_min, sinr_max, sinr_avg,
        rsrp_min, rsrp_max, rsrp_avg,
        float(unique_pci), float(n_cells),
        avg_a3, float(max_tilt),
    ]


# Z-score normalization params computed once from train set
_STATS_KEY = "_stats"


def _compute_stats(all_features: list[list[float]]) -> dict:
    n = len(all_features)
    if n == 0:
        return {"mean": [0.0] * 14, "std": [1.0] * 14}
    dim = len(all_features[0])
    means = [sum(f[i] for f in all_features) / n for i in range(dim)]
    stds = [
        math.sqrt(sum((f[i] - means[i]) ** 2 for f in all_features) / n) or 1.0
        for i in range(dim)
    ]
    return {"mean": means, "std": stds}


def _normalize(vec: list[float], stats: dict) -> list[float]:
    return [(v - m) / s for v, m, s in zip(vec, stats["mean"], stats["std"])]


def l2_distance(a: list[float], b: list[float]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def precompute_train() -> None:
    """Extract features for all train scenarios and save to cache."""
    print(f"Loading {TRAIN_JSON}")
    with TRAIN_JSON.open(encoding="utf-8") as f:
        train = json.load(f)

    entries: list[dict] = []
    raw_features: list[list[float]] = []
    for idx, s in enumerate(train):
        feat = extract_features(s)
        raw_features.append(feat)
        entries.append({
            "idx": idx,
            "scenario_id": s["scenario_id"],
            "tag": s["tag"],
            "answer": s["answer"],
            "features": feat,
        })

    stats = _compute_stats(raw_features)
    # Also store normalized features for quick retrieval
    for e in entries:
        e["normalized"] = _normalize(e["features"], stats)

    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with CACHE_FILE.open("w", encoding="utf-8") as f:
        json.dump({_STATS_KEY: stats, "entries": entries}, f)
    print(f"Saved {len(entries)} train features to {CACHE_FILE}")
    print(f"Feature dim: {len(raw_features[0]) if raw_features else 0}")


_CACHE: dict[str, Any] | None = None


def _load_cache() -> dict[str, Any]:
    global _CACHE
    if _CACHE is None:
        if not CACHE_FILE.exists():
            raise FileNotFoundError(
                f"{CACHE_FILE} not found. Run `python agent/track_a/rag.py --precompute` first."
            )
        with CACHE_FILE.open(encoding="utf-8") as f:
            _CACHE = json.load(f)
    assert _CACHE is not None
    return _CACHE


def retrieve_similar(scenario: dict, k: int = 3,
                     same_tag_only: bool = True,
                     exclude_sid: str | None = None) -> list[dict]:
    """Return top-k similar train entries.

    Args:
        scenario: current scenario dict
        k: number of neighbors
        same_tag_only: if True, restrict to entries with same tag (single vs multi)
        exclude_sid: skip this scenario_id (avoid retrieving self when querying train)

    Returns:
        list of dicts with keys: scenario_id, answer, tag, distance, reasoning_seed
    """
    cache = _load_cache()
    stats = cache[_STATS_KEY]
    entries = cache["entries"]

    test_vec = _normalize(extract_features(scenario), stats)
    target_tag = scenario.get("tag")

    ranked = []
    for e in entries:
        if exclude_sid and e["scenario_id"] == exclude_sid:
            continue
        if same_tag_only and e["tag"] != target_tag:
            continue
        d = l2_distance(test_vec, e["normalized"])
        ranked.append((d, e))
    ranked.sort(key=lambda x: x[0])
    return [
        {
            "scenario_id": e["scenario_id"],
            "answer": e["answer"],
            "tag": e["tag"],
            "distance": round(d, 4),
            "train_idx": e["idx"],
        }
        for d, e in ranked[:k]
    ]


def format_few_shot_from_retrieval(retrieved: list[dict]) -> list[dict]:
    """Convert top-k retrieved train entries into user/assistant few-shot messages.

    Each pair:
      user: very short "Similar drive-test scenario" header + task description + options
      assistant: minimal evidence + \\boxed{answer}
    """
    with TRAIN_JSON.open(encoding="utf-8") as f:
        train = json.load(f)
    train_by_id = {s["scenario_id"]: s for s in train}

    messages: list[dict] = []
    for r in retrieved:
        s = train_by_id.get(r["scenario_id"])
        if not s:
            continue
        task = s.get("task", {})
        opts = task.get("options", [])
        opts_block = "\n".join(f"{o['id']}:{o['label']}" for o in opts)
        user_content = (
            f"[Similar scenario — feature-space distance {r['distance']}]\n"
            f"{task.get('description', '')}\n"
            f"Options:\n{opts_block}"
        )
        # Minimal assistant response (no multi-paragraph evidence — keep tokens tight)
        answer = r["answer"]
        assistant_content = f"(Similar solved example) \\boxed{{{answer}}}"
        messages.append({"role": "user", "content": user_content})
        messages.append({"role": "assistant", "content": assistant_content})
    return messages


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--precompute", action="store_true", help="Compute train features cache")
    ap.add_argument("--query", type=str, help="Scenario ID to query top-k neighbors (train or test)")
    ap.add_argument("--k", type=int, default=3)
    ap.add_argument("--source", choices=["train", "test"], default="train",
                    help="Source to look up the query scenario_id in")
    args = ap.parse_args()

    if args.precompute:
        precompute_train()
        return

    if args.query:
        src_path = TRAIN_JSON if args.source == "train" else TEST_JSON
        with src_path.open(encoding="utf-8") as f:
            data = json.load(f)
        scenario = next((s for s in data if s["scenario_id"] == args.query), None)
        if not scenario:
            print(f"{args.query} not found in {args.source}.json")
            return
        print(f"Query: {args.query}  tag={scenario['tag']}  "
              f"answer={scenario.get('answer', '(placeholder)')}")
        print(f"Features: {extract_features(scenario)}")
        print()
        neighbors = retrieve_similar(
            scenario, k=args.k, same_tag_only=True,
            exclude_sid=args.query if args.source == "train" else None,
        )
        print(f"Top-{args.k} similar train scenarios:")
        for n in neighbors:
            print(f"  d={n['distance']:.4f}  train[{n['train_idx']:>4}] "
                  f"tag={n['tag']:<16}  answer={n['answer']}")
        return

    ap.print_help()


if __name__ == "__main__":
    main()
