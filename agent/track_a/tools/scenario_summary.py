#!/usr/bin/env python3
"""Track A scenario 요약 추출기.

각 scenario 의 throughput 급락 구간, serving PCI 시계열, cell config,
neighbor RSRP 관계를 추출해 Opus 수작업 풀이 / few-shot 증류에 사용.

Usage:
    python scenario_summary.py --train-idx 0
    python scenario_summary.py --train-idx 0,1,2,3,4
    python scenario_summary.py --scenario-id <uuid>
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


TRAIN_JSON = Path(__file__).resolve().parents[3] / "data" / "Track A" / "data" / "Phase_1" / "train.json"
TEST_JSON = Path(__file__).resolve().parents[3] / "data" / "Track A" / "data" / "Phase_1" / "test.json"


def parse_pipe_csv(text: str) -> list[dict[str, str]]:
    lines = [ln.rstrip("\r") for ln in text.strip().split("\n") if ln.strip()]
    if not lines:
        return []
    header = lines[0].split("|")
    return [dict(zip(header, ln.split("|"))) for ln in lines[1:]]


def summarize_throughput(user_plane_rows: list[dict]) -> dict:
    """Throughput 급락 구간 탐지.

    정의: 연속 3개 이상 샘플에서 Throughput < 100 Mbps 이면 degradation window.
    """
    tps = []
    for r in user_plane_rows:
        t = r.get("Timestamp", "")
        tp = r.get("5G KPI PCell Layer2 MAC DL Throughput [Mbps]", "")
        pci = r.get("5G KPI PCell RF Serving PCI", "")
        rsrp = r.get("5G KPI PCell RF Serving SS-RSRP [dBm]", "")
        sinr = r.get("5G KPI PCell RF Serving SS-SINR [dB]", "")
        try:
            tpf = float(tp)
        except (ValueError, TypeError):
            tpf = None
        tps.append(
            {
                "ts": t,
                "tp": tpf,
                "pci": pci,
                "rsrp": rsrp,
                "sinr": sinr,
                "n1_pci": r.get("Measurement PCell Neighbor Cell Top Set(Cell Level) Top 1 PCI", ""),
                "n1_rsrp": r.get("Measurement PCell Neighbor Cell Top Set(Cell Level) Top 1 Filtered Tx BRSRP [dBm]", ""),
                "n2_pci": r.get("Measurement PCell Neighbor Cell Top Set(Cell Level) Top 2 PCI", ""),
                "n2_rsrp": r.get("Measurement PCell Neighbor Cell Top Set(Cell Level) Top 2 Filtered Tx BRSRP [dBm]", ""),
            }
        )
    lows = [r for r in tps if r["tp"] is not None and r["tp"] < 100]
    return {"all_samples": tps, "low_samples": lows, "total": len(tps)}


def cell_config_by_pci(ncd_rows: list[dict]) -> dict[str, dict]:
    return {r.get("PCI", ""): r for r in ncd_rows}


def pretty_degradation(tps: dict) -> str:
    """Throughput 급락 구간을 사람 읽기 쉽게 포맷."""
    lines = []
    low = tps["low_samples"]
    if not low:
        return "(no throughput samples < 100 Mbps)"
    # cluster consecutive
    clusters = []
    current = [low[0]]
    for r in low[1:]:
        current.append(r)
    clusters.append(current) if current else None
    for cluster in clusters:
        lines.append(f"Low-throughput window: {len(cluster)} samples")
        for r in cluster[:15]:
            lines.append(
                f"  {r['ts']} PCI={r['pci']:>4} RSRP={r['rsrp']:>6} SINR={r['sinr']:>5} "
                f"TP={r['tp']:>6.2f} N1:PCI={r['n1_pci']:>4} RSRP={r['n1_rsrp']:>6} "
                f"N2:PCI={r['n2_pci']:>4} RSRP={r['n2_rsrp']:>6}"
            )
        if len(cluster) > 15:
            lines.append(f"  ... ({len(cluster) - 15} more)")
    return "\n".join(lines)


def summarize_scenario(s: dict, idx: "int | str | None" = None) -> str:
    lines = []
    sid = s["scenario_id"]
    tag = s["tag"]
    ans = s["answer"]
    lines.append("=" * 80)
    lines.append(f"[{idx}] scenario_id={sid}")
    lines.append(f"    tag={tag}  ground_truth={ans}")
    lines.append(f"    description: {s['task']['description'][:150]!r}")
    lines.append("")
    lines.append("OPTIONS:")
    for opt in s["task"]["options"]:
        marker = "  >> " if opt["id"] in ans.split("|") else "     "
        lines.append(f"{marker}{opt['id']}: {opt['label']}")
    lines.append("")

    # parse data
    upd = parse_pipe_csv(s["data"]["user_plane_data"])
    ncd = parse_pipe_csv(s["data"]["network_configuration_data"])
    spd = parse_pipe_csv(s["data"].get("signaling_plane_data", ""))
    td = parse_pipe_csv(s["data"].get("traffic_data", ""))
    mr = parse_pipe_csv(s["data"].get("mr_data", ""))

    tps = summarize_throughput(upd)
    cfg = cell_config_by_pci(ncd)

    lines.append(f"DATA: {len(upd)} user_plane_rows, {len(ncd)} cells, "
                 f"{len(spd)} signaling events, {len(td)} traffic rows, {len(mr)} MR rows")
    lines.append("")
    lines.append("--- CELL CONFIG (PCI -> {gNodeB_Cell, Azimuth/Tilt, Power, A3Offset, PdcchSym, NeighborList}) ---")
    for pci, cc in cfg.items():
        neighbors = cc.get("PCell Neighbor Cell (gNodeBID_ARFCN_PCI)", "")
        lines.append(
            f"  PCI={pci} gNB={cc.get('gNodeB ID')}_{cc.get('Cell ID')} "
            f"Az={cc.get('Mechanical Azimuth'):>4} Mtilt={cc.get('Mechanical Downtilt')} Dtilt={cc.get('Digital Tilt')} "
            f"Pwr={cc.get('Transmission Power')} "
            f"A3Off={cc.get('IntraFreqHoA3Offset [0.5dB]')} A3Hyst={cc.get('IntraFreqHoA3Hyst [0.5dB]')} "
            f"Pdcch={cc.get('PdcchOccupiedSymbolNum')}"
        )
        lines.append(f"         NBList={neighbors}")
    lines.append("")
    lines.append("--- THROUGHPUT DEGRADATION WINDOW ---")
    lines.append(pretty_degradation(tps))
    lines.append("")

    if spd:
        lines.append("--- SIGNALING EVENTS (first 12) ---")
        for ev in spd[:12]:
            lines.append(f"  {ev.get('Timestamp')} | {ev.get('Event Name')} | {ev.get('Event Content')}")
        lines.append("")

    if mr:
        lines.append("--- MR DATA (first 5) ---")
        for m in mr[:5]:
            lines.append(
                f"  Serv PCI={m.get('Serving PCI')} RSRP={m.get('Serving RSRP(dBm)')} "
                f"TP={m.get('Throughput(Mbps)')} | "
                f"N1 PCI={m.get('Neighbor 1 PCI')} RSRP={m.get('Neighbor 1 RSRP(dBm)')} | "
                f"N2 PCI={m.get('Neighbor 2 PCI')} RSRP={m.get('Neighbor 2 RSRP(dBm)')}"
            )
        lines.append("")

    if td:
        lines.append("--- TRAFFIC DATA (hourly KPI) ---")
        for t in td[:8]:
            lines.append(
                f"  {t.get('Day\\Hour'):>16} gNB={t.get('gNodeB_ID')}_{t.get('Cell_ID')} "
                f"DL_PRB={t.get('Downlink PRB utilization(%)'):>8} UL_PRB={t.get('Uplink PRB utilization(%)'):>8} "
                f"DL_TP={t.get('User Downlink Throughput(Mbps)'):>8}"
            )
        lines.append("")

    lines.append("--- NOTES ---")
    lines.append(str(s["data"].get("notes", "(empty)"))[:400])
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-idx", type=str, help="Comma-separated train indices, e.g. 0,1,2")
    parser.add_argument("--test-idx", type=str, help="Comma-separated test indices")
    parser.add_argument("--scenario-id", type=str, help="Explicit scenario UUID")
    parser.add_argument("--out", type=str, default=None, help="Output file (default stdout)")
    args = parser.parse_args()

    out_lines: list[str] = []
    if args.train_idx:
        with TRAIN_JSON.open() as f:
            data = json.load(f)
        for i in [int(x) for x in args.train_idx.split(",")]:
            out_lines.append(summarize_scenario(data[i], idx=i))
    if args.test_idx:
        with TEST_JSON.open() as f:
            data = json.load(f)
        for i in [int(x) for x in args.test_idx.split(",")]:
            out_lines.append(summarize_scenario(data[i], idx=i))
    if args.scenario_id:
        for path in [TRAIN_JSON, TEST_JSON]:
            with path.open() as f:
                d = json.load(f)
            for i, s in enumerate(d):
                if s["scenario_id"] == args.scenario_id:
                    out_lines.append(summarize_scenario(s, idx=f"{path.name}:{i}"))
                    break

    out = "\n".join(out_lines) or "(no scenarios selected)"
    if args.out:
        Path(args.out).write_text(out)
        print(f"Wrote {len(out)} bytes to {args.out}", file=sys.stderr)
    else:
        print(out)


if __name__ == "__main__":
    main()
