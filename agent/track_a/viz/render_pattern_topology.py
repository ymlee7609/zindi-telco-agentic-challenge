#!/usr/bin/env python3
"""Track A 10-pattern 대표 시나리오의 기지국 구성 2D top-view + UE 시계열 시각화.

각 시나리오마다 2-패널 PNG:
- 왼쪽(top-view): cell lon/lat → km offset, sector 부채꼴(Azimuth/Tx power/tilt), UE drive path
- 오른쪽(4단 시계열): Throughput, SS-RSRP, SS-SINR, Serving PCI (시간축)

Output: docs/track_a/images/P{1-10}_{slug}_train{NNN}.png

Run:
    python agent/track_a/viz/render_pattern_topology.py
"""

from __future__ import annotations

import json
import math
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.patches import Wedge

# ---------------------------------------------------------------------------
# 경로
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parents[3]
TRAIN_JSON = REPO_ROOT / "data" / "Track A" / "data" / "Phase_1" / "train.json"
OUT_DIR = REPO_ROOT / "docs" / "track_a" / "images"

# ---------------------------------------------------------------------------
# 10-pattern 대표 시나리오 매핑 (docs/track_a/03-3_problems.md §3 + §5-ter 근거)
# ---------------------------------------------------------------------------
PATTERNS: list[tuple[str, str, int, str]] = [
    ("P1", "Late Handover",        2,  "Serving PCI held + high A3Offset on serving cell -> handover delayed"),
    ("P2", "Ping-pong",             0,  "Serving PCI oscillates between two cells + both have low A3Offset"),
    ("P3", "Overshoot",             10, "SINR < 5 + a distant high-power cell dominates Top-neighbor list"),
    ("P4", "Coverage Hole",         17, "Serving RSRP <= -100 and all neighbors also weak"),
    ("P5", "Server Issue",          1,  "SINR >= 10 (healthy) but throughput varies -- non-RF cause"),
    ("P6", "Excessive Downtilt",    4,  "Neighbor cell Mechanical + Digital Tilt >= 20 deg -> coverage gap"),
    ("P7", "Insufficient Data",     6,  "All metrics within normal range -- no anomaly, no diagnosis"),
    ("P8", "PDCCH Resource",       13, "PdcchOccupiedSymbolNum=1SYM on serving cell -- PDCCH resource bottleneck"),
    ("P9", "Missing Neighbor",     20, "Strong neighbor cell NOT in serving cell's configured neighbor list"),
    ("P10", "Coverage Threshold",   15, "CovInterFreqA2RsrpThld=-95 dBm (too high vs standard -105 dBm)"),
]

# PCI 색상 테이블 (cell 순서대로 qualitative palette)
PCI_PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
               "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"]

# 임계선
TP_THRESHOLD_MBPS = 100.0
RSRP_THRESHOLD_DBM = -100.0
SINR_THRESHOLD_DB = 5.0


# ---------------------------------------------------------------------------
# 파싱 유틸
# ---------------------------------------------------------------------------
def parse_pipe(text: str) -> list[dict[str, str]]:
    lines = [ln.rstrip("\r") for ln in text.strip().split("\n") if ln.strip()]
    if not lines:
        return []
    header = lines[0].split("|")
    return [dict(zip(header, ln.split("|"))) for ln in lines[1:]]


def safe_float(s: str | None, default: float | None = None) -> float | None:
    if s is None:
        return default
    s = str(s).strip()
    if not s or s == "-":
        return default
    try:
        return float(s)
    except ValueError:
        return default


def to_km(lon: float, lat: float, lon0: float, lat0: float) -> tuple[float, float]:
    radius_km = 111.0
    x = (lon - lon0) * radius_km * math.cos(math.radians(lat0))
    y = (lat - lat0) * radius_km
    return x, y


def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


def parse_timestamp(s: str) -> datetime | None:
    s = (s or "").strip()
    for fmt in ("%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(s, fmt)
        except (ValueError, TypeError):
            continue
    return None


# ---------------------------------------------------------------------------
# Top-view 패널
# ---------------------------------------------------------------------------
def render_topview(
    ax: Axes,
    cells: list[dict],
    ue_rows: list[dict],
    pci_color: dict[str, str],
) -> None:
    """왼쪽 top-view 패널: cell sector + UE drive path."""

    # 기준점 계산
    all_lons, all_lats = [], []
    for c in cells:
        lo, la = safe_float(c.get("Longitude")), safe_float(c.get("Latitude"))
        if lo is not None and la is not None:
            all_lons.append(lo)
            all_lats.append(la)
    for r in ue_rows:
        lo, la = safe_float(r.get("Longitude")), safe_float(r.get("Latitude"))
        if lo is not None and la is not None:
            all_lons.append(lo)
            all_lats.append(la)
    if not all_lons:
        raise ValueError("유효한 lon/lat 없음")
    lon0 = float(np.mean(all_lons))
    lat0 = float(np.mean(all_lats))

    tilt_cmap = plt.colormaps["RdYlGn_r"]

    # UE 경로 먼저 깔기
    ue_xy: list[tuple[float, float, dict]] = []
    for r in ue_rows:
        lo, la = safe_float(r.get("Longitude")), safe_float(r.get("Latitude"))
        if lo is None or la is None:
            continue
        x, y = to_km(lo, la, lon0, lat0)
        ue_xy.append((x, y, r))

    if ue_xy:
        xs = [p[0] for p in ue_xy]
        ys = [p[1] for p in ue_xy]
        ax.plot(xs, ys, color="steelblue", linewidth=1.8, alpha=0.55, zorder=2)

    # Sector 부채꼴 + 라벨 (라벨은 beam 뒤쪽에 배치하여 UE 경로와 겹침 회피)
    for c in cells:
        lon, lat = safe_float(c.get("Longitude")), safe_float(c.get("Latitude"))
        if lon is None or lat is None:
            continue
        x, y = to_km(lon, lat, lon0, lat0)
        mech_az = safe_float(c.get("Mechanical Azimuth"), 0.0) or 0.0
        m_dt = safe_float(c.get("Mechanical Downtilt"), 0.0) or 0.0
        d_dt = safe_float(c.get("Digital Tilt"), 0.0) or 0.0
        total_tilt = m_dt + d_dt
        pwr = safe_float(c.get("Transmission Power"), 20.0) or 20.0
        pci = str(c.get("PCI", "?"))
        a3off_raw = safe_float(c.get("IntraFreqHoA3Offset [0.5dB]"))
        a3off_db = (a3off_raw or 0) * 0.5
        height = safe_float(c.get("Height"), 0.0) or 0.0

        math_center = (90.0 - mech_az) % 360.0
        beamwidth = 65.0
        theta1 = math_center - beamwidth / 2.0
        theta2 = math_center + beamwidth / 2.0

        radius = 0.18 + clamp((pwr - 10.0) / 22.0, 0.0, 1.0) * 0.7
        fill_color = tilt_cmap(clamp(total_tilt, 0.0, 25.0) / 25.0)
        edge_color = pci_color.get(pci, "black")

        wedge = Wedge(
            (x, y), radius, theta1, theta2,
            facecolor=fill_color, edgecolor=edge_color, linewidth=1.8, alpha=0.55, zorder=3,
        )
        ax.add_patch(wedge)

        # 안테나 삼각형 (PCI 색상으로 테두리)
        ax.plot(x, y, marker="^", color=edge_color, markersize=12, markeredgecolor="black",
                markeredgewidth=0.8, zorder=6)

        # 라벨: beam 뒤쪽(안테나의 null 영역)에 배치
        back_angle_rad = math.radians((math_center + 180.0) % 360.0)
        label_dist = 0.18
        lx = x + label_dist * math.cos(back_angle_rad)
        ly = y + label_dist * math.sin(back_angle_rad)

        a3_text = f"A3Off={int(a3off_raw)}={a3off_db:.1f}dB" if a3off_raw is not None else "A3Off=?"
        label = (f"PCI {pci}\n"
                 f"Az {int(mech_az)}\u00b0\n"
                 f"M{int(m_dt)}\u00b0+D{int(d_dt)}\u00b0 (tot={int(total_tilt)}\u00b0)\n"
                 f"Pwr {int(pwr)} dBm \u00b7 h {int(height)}m\n"
                 f"{a3_text}")

        ax.annotate(
            label, xy=(lx, ly),
            fontsize=6.8, ha="center", va="center", zorder=7,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=edge_color,
                      alpha=0.92, linewidth=1.0),
        )

    # UE 샘플 점: serving PCI 색상 + 시간 순서 번호 + throughput 저하 강조
    if ue_xy:
        # UE 이동 범위 계산 (겹침 감지)
        ue_xs = [p[0] for p in ue_xy]
        ue_ys = [p[1] for p in ue_xy]
        ue_range = max(max(ue_xs) - min(ue_xs), max(ue_ys) - min(ue_ys))
        is_clustered = ue_range < 0.05  # 50m 미만이면 밀집

        for i, (x, y, r) in enumerate(ue_xy):
            tp = safe_float(r.get("5G KPI PCell Layer2 MAC DL Throughput [Mbps]"))
            serving_pci = str(r.get("5G KPI PCell RF Serving PCI", "?")).strip()
            dot_color = pci_color.get(serving_pci, "steelblue")

            is_low_tp = tp is not None and tp < TP_THRESHOLD_MBPS

            # 밀집 시 점을 원형으로 분산 배치 (시계 방향)
            if is_clustered and len(ue_xy) > 1:
                angle = 2 * math.pi * i / len(ue_xy)
                spread = 0.04 + 0.01 * len(ue_xy)  # 점 수에 비례
                dx = spread * math.cos(angle)
                dy = spread * math.sin(angle)
            else:
                dx, dy = 0, 0

            px, py = x + dx, y + dy

            if is_low_tp:
                ax.plot(px, py, "o", color=dot_color, markersize=11,
                        markeredgecolor="red", markeredgewidth=2.0, zorder=8)
            else:
                ax.plot(px, py, "o", color=dot_color, markersize=9,
                        markeredgecolor="black", markeredgewidth=0.7, zorder=5)

            # 시간 순서 번호 (점 위에 표시)
            tp_text = f"{int(tp)}" if tp is not None else "?"
            ax.annotate(
                f"t{i}", xy=(px, py),
                xytext=(0, 7), textcoords="offset points",
                fontsize=5.5, ha="center", va="bottom", color="#333",
                fontweight="bold", zorder=9,
            )

        # 밀집 시 원래 위치에 십자 마커로 실제 UE 위치 표시
        if is_clustered:
            cx = float(np.mean(ue_xs))
            cy = float(np.mean(ue_ys))
            ax.plot(cx, cy, "+", color="black", markersize=14, markeredgewidth=2.5, zorder=4)
            ax.annotate(
                "Actual UE pos\n(dots spread for visibility)",
                xy=(cx, cy),
                xytext=(15, -20), textcoords="offset points",
                fontsize=7, ha="left", color="#555",
                arrowprops=dict(arrowstyle="->", color="#999", lw=0.8),
                bbox=dict(boxstyle="round,pad=0.2", fc="#f8f8f8", ec="#ccc", alpha=0.9),
                zorder=10,
            )

        ax.annotate(
            f"t0 START", xy=(ue_xy[0][0] + (0.04 if is_clustered else 0),
                             ue_xy[0][1] + (0.04 if is_clustered else 0)),
            xytext=(12, 12), textcoords="offset points",
            fontsize=8, fontweight="bold", color="darkgreen",
            bbox=dict(boxstyle="round,pad=0.2", fc="#e8f8e8", ec="darkgreen", linewidth=0.7),
            zorder=10,
        )
        last_i = len(ue_xy) - 1
        if is_clustered:
            angle_last = 2 * math.pi * last_i / len(ue_xy)
            spread = 0.04 + 0.01 * len(ue_xy)
            end_x = ue_xy[-1][0] + spread * math.cos(angle_last)
            end_y = ue_xy[-1][1] + spread * math.sin(angle_last)
        else:
            end_x, end_y = ue_xy[-1][0], ue_xy[-1][1]
        ax.annotate(
            f"t{last_i} END", xy=(end_x, end_y),
            xytext=(12, -14), textcoords="offset points",
            fontsize=8, fontweight="bold", color="darkred",
            bbox=dict(boxstyle="round,pad=0.2", fc="#f8e8e8", ec="darkred", linewidth=0.7),
            zorder=10,
        )

    ax.set_aspect("equal", adjustable="datalim")
    ax.grid(True, linestyle=":", alpha=0.45)
    ax.set_xlabel("East-West offset (km)", fontsize=9)
    ax.set_ylabel("North-South offset (km)", fontsize=9)
    ax.set_title("Top-view (real lon/lat -> local km)", fontsize=10)

    # 여백
    cur_xlim = ax.get_xlim()
    cur_ylim = ax.get_ylim()
    pad_x = (cur_xlim[1] - cur_xlim[0]) * 0.10 + 0.20
    pad_y = (cur_ylim[1] - cur_ylim[0]) * 0.10 + 0.20
    ax.set_xlim(cur_xlim[0] - pad_x, cur_xlim[1] + pad_x)
    ax.set_ylim(cur_ylim[0] - pad_y, cur_ylim[1] + pad_y)


# ---------------------------------------------------------------------------
# 시계열 패널
# ---------------------------------------------------------------------------
def render_timeseries(
    ax_tp: Axes,
    ax_rsrp: Axes,
    ax_sinr: Axes,
    ax_pci: Axes,
    ue_rows: list[dict],
    pci_color: dict[str, str],
) -> None:
    """오른쪽 4단 시계열: Throughput / RSRP / SINR / Serving PCI."""

    # 데이터 추출
    t0: datetime | None = None
    times: list[float] = []
    tps: list[float | None] = []
    rsrps: list[float | None] = []
    sinrs: list[float | None] = []
    scis: list[str] = []

    for r in ue_rows:
        ts = parse_timestamp(r.get("Timestamp", ""))
        if ts is None:
            continue
        if t0 is None:
            t0 = ts
        times.append((ts - t0).total_seconds())
        tps.append(safe_float(r.get("5G KPI PCell Layer2 MAC DL Throughput [Mbps]")))
        rsrps.append(safe_float(r.get("5G KPI PCell RF Serving SS-RSRP [dBm]")))
        sinrs.append(safe_float(r.get("5G KPI PCell RF Serving SS-SINR [dB]")))
        scis.append(str(r.get("5G KPI PCell RF Serving PCI", "?")).strip())

    # --- Throughput ---
    ax_tp.plot(times, [v if v is not None else np.nan for v in tps],
               marker="o", color="steelblue", linewidth=1.3, markersize=4)
    low_t = [t for t, v in zip(times, tps) if v is not None and v < TP_THRESHOLD_MBPS]
    low_v = [v for v in tps if v is not None and v < TP_THRESHOLD_MBPS]
    if low_t:
        ax_tp.plot(low_t, low_v, "o", color="crimson", markersize=7, markeredgecolor="black",
                   markeredgewidth=0.6, zorder=5)
    ax_tp.axhline(TP_THRESHOLD_MBPS, color="crimson", linestyle="--", linewidth=0.8, alpha=0.6)
    ax_tp.set_ylabel("Throughput\n(Mbps)", fontsize=8)
    ax_tp.grid(True, linestyle=":", alpha=0.4)
    ax_tp.tick_params(axis="both", labelsize=7)
    ax_tp.set_title("UE time series", fontsize=10)

    # --- RSRP ---
    ax_rsrp.plot(times, [v if v is not None else np.nan for v in rsrps],
                 marker="o", color="#2ca02c", linewidth=1.3, markersize=4)
    ax_rsrp.axhline(RSRP_THRESHOLD_DBM, color="crimson", linestyle="--", linewidth=0.8, alpha=0.6)
    ax_rsrp.set_ylabel("SS-RSRP\n(dBm)", fontsize=8)
    ax_rsrp.grid(True, linestyle=":", alpha=0.4)
    ax_rsrp.tick_params(axis="both", labelsize=7)

    # --- SINR ---
    ax_sinr.plot(times, [v if v is not None else np.nan for v in sinrs],
                 marker="o", color="#9467bd", linewidth=1.3, markersize=4)
    ax_sinr.axhline(SINR_THRESHOLD_DB, color="crimson", linestyle="--", linewidth=0.8, alpha=0.6)
    ax_sinr.set_ylabel("SS-SINR\n(dB)", fontsize=8)
    ax_sinr.grid(True, linestyle=":", alpha=0.4)
    ax_sinr.tick_params(axis="both", labelsize=7)

    # --- Serving PCI (categorical) ---
    unique_pcis = sorted({p for p in scis if p and p != "?"}, key=lambda s: int(s) if s.isdigit() else 0)
    pci_y = {p: i for i, p in enumerate(unique_pcis)}

    for i, p in enumerate(scis):
        if p not in pci_y:
            continue
        ax_pci.plot(times[i], pci_y[p], "o", color=pci_color.get(p, "#444"),
                    markersize=8, markeredgecolor="black", markeredgewidth=0.5)

    # 전환선 (handover 발생 지점)
    for i in range(1, len(scis)):
        if scis[i] and scis[i-1] and scis[i] != scis[i-1] and scis[i] in pci_y and scis[i-1] in pci_y:
            ax_pci.plot([times[i-1], times[i]], [pci_y[scis[i-1]], pci_y[scis[i]]],
                        color="gray", linewidth=0.8, alpha=0.6)

    ax_pci.set_yticks(list(pci_y.values()))
    ax_pci.set_yticklabels([f"PCI {p}" for p in pci_y.keys()], fontsize=7)
    ax_pci.set_ylabel("Serving\nPCI", fontsize=8)
    ax_pci.set_xlabel("Time (s from first sample)", fontsize=8)
    ax_pci.grid(True, linestyle=":", alpha=0.4, axis="x")
    ax_pci.tick_params(axis="x", labelsize=7)
    if pci_y:
        ax_pci.set_ylim(-0.5, len(pci_y) - 0.5)


# ---------------------------------------------------------------------------
# 시나리오 1개 렌더 (figure 단위)
# ---------------------------------------------------------------------------
def render_scenario_figure(
    fig: Figure,
    cells: list[dict],
    ue_rows: list[dict],
    code: str,
    name: str,
    idx: int,
    description: str,
    answer: str,
) -> None:
    # cell 순서대로 PCI → 색상 매핑
    pci_color: dict[str, str] = {}
    for i, c in enumerate(cells):
        pci = str(c.get("PCI", "?"))
        pci_color[pci] = PCI_PALETTE[i % len(PCI_PALETTE)]

    # gridspec: 좌(top-view, 세로 풀) / 우(4단 시계열 stacked)
    gs = fig.add_gridspec(
        nrows=4, ncols=2,
        width_ratios=[1.55, 1.0],
        hspace=0.22, wspace=0.12,
        left=0.06, right=0.975, top=0.90, bottom=0.13,
    )
    ax_top = fig.add_subplot(gs[:, 0])
    ax_tp = fig.add_subplot(gs[0, 1])
    ax_rsrp = fig.add_subplot(gs[1, 1], sharex=ax_tp)
    ax_sinr = fig.add_subplot(gs[2, 1], sharex=ax_tp)
    ax_pci = fig.add_subplot(gs[3, 1], sharex=ax_tp)

    render_topview(ax_top, cells, ue_rows, pci_color)
    render_timeseries(ax_tp, ax_rsrp, ax_sinr, ax_pci, ue_rows, pci_color)

    # 첫 3단의 x-tick 라벨 숨기기
    for a in (ax_tp, ax_rsrp, ax_sinr):
        plt.setp(a.get_xticklabels(), visible=False)

    # Figure-level 제목
    tag_label = "multiple-answer" if "|" in answer else "single-answer"
    fig.suptitle(
        f"Track A  {code}  {name}   --   train[{idx}]   answer={answer}  ({tag_label})",
        fontsize=13, fontweight="bold", y=0.97,
    )

    # 하단 캡션
    caption = (
        f"Pattern trigger: {description}\n"
        f"Triangle = gNodeB antenna  |  Wedge = sector beam (65 deg beamwidth, direction = Mechanical Azimuth)  |  "
        f"Wedge radius proportional to Tx Power\n"
        f"Wedge color: green = low total tilt (wide cover), red = tilt >= 20 deg (narrow)  |  "
        f"UE dots colored by serving PCI (matches time-series PCI color)\n"
        f"t0,t1,... = time-ordered UE samples  |  Red ring = throughput < 100 Mbps  |  "
        f"Clustered UE: + marks actual position, dots are spread for visibility"
    )
    fig.text(
        0.5, 0.025, caption,
        ha="center", va="bottom", fontsize=7.6, color="#333", style="italic",
        bbox=dict(boxstyle="round,pad=0.35", fc="#fafafa", ec="#cccccc", linewidth=0.6),
    )


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main() -> int:
    if not TRAIN_JSON.exists():
        print(f"ERROR: {TRAIN_JSON} not found")
        return 1

    print(f"Loading {TRAIN_JSON.name} ...")
    with TRAIN_JSON.open() as f:
        data = json.load(f)
    print(f"  -> {len(data)} scenarios")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Output dir: {OUT_DIR.relative_to(REPO_ROOT)}")

    for code, name, idx, desc in PATTERNS:
        if idx >= len(data):
            print(f"[skip] train[{idx}] missing")
            continue

        scenario = data[idx]
        cells = parse_pipe(scenario["data"]["network_configuration_data"])
        ue_rows = parse_pipe(scenario["data"]["user_plane_data"])
        answer = scenario.get("answer", "?")

        fig = plt.figure(figsize=(16.0, 9.5))
        try:
            render_scenario_figure(fig, cells, ue_rows, code, name, idx, desc, answer)
        except Exception as e:  # noqa: BLE001
            print(f"[error] {code} train[{idx}]: {e}")
            plt.close(fig)
            continue

        slug = name.lower().replace(" ", "_")
        out_path = OUT_DIR / f"{code}_{slug}_train{idx:03d}.png"
        fig.savefig(out_path, dpi=140, bbox_inches="tight")
        plt.close(fig)
        rel = out_path.relative_to(REPO_ROOT)
        print(f"  OK  {code} {name:<22} -> {rel}  (cells={len(cells)}, ue={len(ue_rows)}, answer={answer})")

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
