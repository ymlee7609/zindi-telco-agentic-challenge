#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Track A RAG (Retrieval-Augmented Generation).

각 scenario 를 22-dim 수치 특징 벡터로 변환하고, train 2000 의 사전 계산된 feature 를
이용해 가장 유사한 top-k scenario 를 검색. 검색된 scenario 와 그 정답을 dynamic
few-shot 으로 agent 에 주입하면 패턴 인식이 강화된다.

특징 (26-dim, P2-1 + P8/P9/P10 확장):
  # Throughput
  [0] TP min, [1] TP max, [2] TP avg, [3] TP drop ratio (max-min)/max
  # SINR
  [4] SINR min, [5] SINR max, [6] SINR avg
  # RSRP
  [7] RSRP min, [8] RSRP max, [9] RSRP avg
  # Mobility
  [10] Unique serving PCI count (1=stable, >1=pingpong/handover)
  [11] Cell 수 (ncd rows)
  # Parameters
  [12] Avg A3 Offset (over all cells, in 0.5dB units)
  [13] Max total downtilt (Mechanical + Digital)
  # P2-1 확장 (+8 dim) — pattern-level discriminators
  [14] SINR variance (P5 server issue vs P3 overshoot 구분)
  [15] PCI transitions (consecutive PCI 변화 횟수, P2 ping-pong 강도)
  [16] A3Offset variance across cells
  [17] Tilt variance (max - min total downtilt across cells)
  [18] Max cell power (P4 coverage hole: power < 30 여부 판단)
  [19] Min cell power
  [20] Throughput recovery flag (0=no recovery, 1=has recovery pattern)
  [21] Dominant neighbor RSRP vs serving RSRP delta (P3 overshoot 지표)
  # P8/P9/P10 확장 (+4 dim) — 신규 패턴 판별
  [22] Max CovInterFreqA2RsrpThld (P10: -95 vs -105 dBm 차이)
  [23] Neighbor completeness (P9: 1.0=완전, <0.8=이웃 누락 가능)
  [24] PDCCH 1SYM ratio (P8: 1.0=전체 1SYM)
  [25] TP variance (P5 server=극단적 variance vs P8 pdcch=moderate)

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


def _variance(vals: list[float]) -> float:
    """Simple population variance. 0 if less than 2 values."""
    n = len(vals)
    if n < 2:
        return 0.0
    m = sum(vals) / n
    return sum((v - m) ** 2 for v in vals) / n


def _pci_transitions(pcis: list[str]) -> int:
    """Consecutive PCI 변화 횟수 (P2 ping-pong 강도)."""
    if len(pcis) < 2:
        return 0
    return sum(1 for a, b in zip(pcis[:-1], pcis[1:]) if a != b and a and b)


def _throughput_recovery_flag(tps: list[float]) -> float:
    """TP 가 저점 → 회복 패턴을 보이면 1.0, 아니면 0.0.

    Heuristic: TP 시퀀스에서 max → dip (≤ 50% of max) → recovery (≥ 80% of max) 패턴.
    """
    if len(tps) < 5:
        return 0.0
    mx = max(tps)
    if mx <= 0:
        return 0.0
    low_threshold = mx * 0.5
    high_threshold = mx * 0.8
    state = 0  # 0=init, 1=saw_dip, 2=saw_recovery
    for v in tps:
        if state == 0 and v <= low_threshold:
            state = 1
        elif state == 1 and v >= high_threshold:
            state = 2
            break
    return 1.0 if state == 2 else 0.0


def extract_features(scenario: dict) -> list[float]:
    """22-dim numeric feature vector for a scenario (P2-1 확장)."""
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
    pcis = [r.get(pci_col) or "" for r in upd]

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

    unique_pci = len(set(p for p in pcis if p)) if pcis else 1
    n_cells = len(ncd)

    a3_vals = [_safe_int(c.get("IntraFreqHoA3Offset [0.5dB]"), 6) for c in ncd]
    avg_a3 = sum(a3_vals) / len(a3_vals) if a3_vals else 6.0

    total_tilts = [
        _safe_int(c.get("Mechanical Downtilt")) + _safe_int(c.get("Digital Tilt"))
        for c in ncd
    ]
    max_tilt = max(total_tilts) if total_tilts else 0

    # --- P2-1 확장 (+8 dim) ---
    # [14] SINR variance
    sinr_var = _variance(sinrs)
    # [15] PCI transitions (consecutive changes)
    pci_trans = _pci_transitions(pcis)
    # [16] A3Offset variance across cells
    a3_var = _variance([float(v) for v in a3_vals]) if a3_vals else 0.0
    # [17] Tilt range (max - min)
    tilt_range = float((max(total_tilts) - min(total_tilts))) if total_tilts else 0.0
    # [18] Max cell power
    powers = [_safe_int(c.get("Power")) for c in ncd]
    max_power = float(max(powers)) if powers else 0.0
    # [19] Min cell power
    min_power = float(min(powers)) if powers else 0.0
    # [20] Throughput recovery flag
    tp_recovery = _throughput_recovery_flag(tps)
    # [21] Dominant neighbor RSRP vs serving RSRP delta
    # Approximation: if serving_rsrp_avg 와 neighbor rsrp 데이터 기반 비교 곤란 시 0
    # 간단 proxy: rsrp_max (best snapshot) 가 avg 보다 크게 높으면 neighbor 경쟁 있음
    serving_spread = rsrp_max - rsrp_avg

    # --- P8/P9/P10 확장 (+4 dim) ---
    # [22] P10: CovInterFreqA2RsrpThld max (= 가장 높은 threshold; -95 vs -105 차이)
    cov_thresholds = [
        _safe_float(c.get("CovInterFreqA2RsrpThld [dBm]"), -105.0) for c in ncd
    ]
    max_cov_threshold = max(cov_thresholds) if cov_thresholds else -105.0

    # [23] P9: neighbor_completeness — serving cell의 neighbor list에 포함된 셀 비율
    # 비율이 낮으면 강한 이웃 셀이 neighbor list에서 누락되어 핸드오버 불가 가능성
    neighbor_completeness = 1.0
    if ncd:
        all_pcis = {c.get("PCI", "").strip() for c in ncd if c.get("PCI", "").strip()}
        neighbor_lists = []
        for c in ncd:
            nlist = c.get("PCell Neighbor Cell (gNodeBID_ARFCN_PCI)", "")
            # 포맷: [3279943_504990_420,3267220_504990_966,...]
            npci = set()
            for entry in nlist.strip("[]").split(","):
                parts = entry.strip().split("_")
                if len(parts) >= 3:
                    npci.add(parts[2])  # PCI 부분
            neighbor_lists.append(npci)
        # 각 cell의 neighbor list에 다른 cell들의 PCI가 포함되어 있는지 확인
        coverage_scores = []
        for i, c in enumerate(ncd):
            my_pci = c.get("PCI", "").strip()
            other_pcis = all_pcis - {my_pci}
            if not other_pcis:
                continue
            covered = sum(1 for p in other_pcis if p in neighbor_lists[i])
            coverage_scores.append(covered / len(other_pcis) if other_pcis else 1.0)
        neighbor_completeness = (
            sum(coverage_scores) / len(coverage_scores)
            if coverage_scores else 1.0
        )

    # [24] P8: pdcch_1sym_ratio — PdcchOccupiedSymbolNum이 1SYM인 셀 비율
    pdcch_values = [c.get("PdcchOccupiedSymbolNum", "").strip() for c in ncd]
    pdcch_1sym = sum(1 for v in pdcch_values if v == "1SYM")
    pdcch_1sym_ratio = pdcch_1sym / len(pdcch_values) if pdcch_values else 0.0

    # [25] TP variance (P5 server vs P8 pdcch 구분 — server issue는 극단적 variance)
    tp_var = _variance(tps)

    return [
        tp_min, tp_max, tp_avg, tp_drop,
        sinr_min, sinr_max, sinr_avg,
        rsrp_min, rsrp_max, rsrp_avg,
        float(unique_pci), float(n_cells),
        avg_a3, float(max_tilt),
        # P2-1 확장
        sinr_var, float(pci_trans), a3_var, tilt_range,
        max_power, min_power, tp_recovery, serving_spread,
        # P8/P9/P10 확장
        max_cov_threshold, neighbor_completeness, pdcch_1sym_ratio, tp_var,
    ]


# 특징 벡터 차원 수 상수 (precompute/_compute_stats 에서 사용)
FEATURE_DIM = 26


# Z-score normalization params computed once from train set
_STATS_KEY = "_stats"


def _compute_stats(all_features: list[list[float]]) -> dict:
    n = len(all_features)
    if n == 0:
        return {"mean": [0.0] * FEATURE_DIM, "std": [1.0] * FEATURE_DIM}
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


def _feature_hint(scenario: dict) -> str:
    """P2-3: 특징 벡터에서 pattern hint 를 간략 추출 (assistant few-shot 증강용).

    50 토큰 이하의 짧은 힌트로 RAG neighbor 의 패턴 정답성을 설명. 예:
      "ping-pong (PCI transitions=8), low A3 offset" → \\boxed{C16}
    """
    try:
        f = extract_features(scenario)
    except Exception:
        return ""
    # [0]tp_min [2]tp_avg [3]tp_drop [5]sinr_max [6]sinr_avg [7]rsrp_min [9]rsrp_avg
    # [10]unique_pci [12]avg_a3 [13]max_tilt [14]sinr_var [15]pci_trans [18]max_power
    sinr_avg = f[6]
    rsrp_avg = f[9]
    unique_pci = int(f[10])
    avg_a3 = f[12]
    max_tilt = int(f[13])
    pci_trans = int(f[15])
    max_power = int(f[18])
    tp_recovery = f[20]

    hints: list[str] = []

    # P8/P9/P10 확장 features
    max_cov_threshold = f[22] if len(f) > 22 else -105.0
    neighbor_comp = f[23] if len(f) > 23 else 1.0
    pdcch_1sym = f[24] if len(f) > 24 else 0.0
    tp_var = f[25] if len(f) > 25 else 0.0

    # P2 Ping-pong: multiple PCI transitions + low A3
    if pci_trans >= 2 and avg_a3 <= 3:
        hints.append(f"ping-pong (PCI trans={pci_trans}, low A3={avg_a3:.1f})")
    # P1 Late handover: stable PCI + high A3
    elif unique_pci == 1 and avg_a3 >= 8:
        hints.append(f"late handover (stable PCI, high A3={avg_a3:.1f})")
    # P3 Overshoot: low SINR + high power
    elif sinr_avg <= 5 and max_power >= 25:
        hints.append(f"possible overshoot (SINR={sinr_avg:.1f}, max_power={max_power})")
    # P4 Coverage hole: very low RSRP + low power
    elif rsrp_avg <= -100 and max_power < 30:
        hints.append(f"coverage hole (RSRP={rsrp_avg:.1f}, max_power={max_power})")
    # P10 Coverage threshold too high
    elif max_cov_threshold > -100:
        hints.append(f"high coverage threshold ({max_cov_threshold:.0f} dBm, may need decrease)")
    # P9 Missing neighbor
    elif neighbor_comp < 0.8:
        hints.append(f"possible missing neighbor (completeness={neighbor_comp:.2f})")
    # P5 Server issue: healthy SINR + tp recovery pattern
    elif sinr_avg >= 10 and tp_recovery > 0:
        hints.append(f"server-issue-like (SINR={sinr_avg:.1f} healthy, TP recovery)")
    # P6 Excessive downtilt
    elif max_tilt >= 20:
        hints.append(f"excessive downtilt ({max_tilt} deg)")
    # P8 PDCCH resource
    elif pdcch_1sym > 0.5 and sinr_avg >= 5:
        hints.append(f"PDCCH 1SYM (ratio={pdcch_1sym:.1f}, may need 2SYM)")

    return "; ".join(hints) if hints else ""


def format_few_shot_from_retrieval(retrieved: list[dict]) -> list[dict]:
    """Convert top-k retrieved train entries into user/assistant few-shot messages.

    Each pair:
      user: very short "Similar drive-test scenario" header + task description + options
      assistant: minimal evidence + \\boxed{answer}

    P2-3: assistant content 에 feature-based pattern hint 추가 (50토큰 이하).
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
        # P2-3: pattern hint 주입 (간략 evidence)
        answer = r["answer"]
        hint = _feature_hint(s)
        if hint:
            assistant_content = f"(Similar pattern: {hint}) \\boxed{{{answer}}}"
        else:
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
