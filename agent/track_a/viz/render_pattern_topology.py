#!/usr/bin/env python3
"""Track A 7-pattern 대표 시나리오의 기지국 구성 2D top-view 시각화.

각 시나리오마다 다음을 포함한 PNG 한 장 생성:
- cell 위치(실제 lon/lat → 지역 km offset)에 sector 부채꼴
- Azimuth 방향, Tx power(반경), Total downtilt(색상)
- PCI / A3Offset / 틸트 / 전력 주석
- UE 시계열 경로 + throughput<100 Mbps 구간 빨간 점 강조

Output: docs/track_a/images/P{1-7}_{slug}_train{NNN}.png

Run:
    python agent/track_a/viz/render_pattern_topology.py
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.patches import Wedge

# ---------------------------------------------------------------------------
# 경로
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parents[3]
TRAIN_JSON = REPO_ROOT / "data" / "Track A" / "data" / "Phase_1" / "train.json"
OUT_DIR = REPO_ROOT / "docs" / "track_a" / "images"

# ---------------------------------------------------------------------------
# 7-pattern 대표 시나리오 매핑 (docs/track_a/03-3_problems.md §3 근거)
# ---------------------------------------------------------------------------
# tuple: (code, name, train_idx, trigger_description)
PATTERNS: list[tuple[str, str, int, str]] = [
    ("P1", "Late Handover",        2,  "Serving PCI held + high A3Offset on serving cell -> handover delayed"),
    ("P2", "Ping-pong",             0,  "Serving PCI oscillates between two cells + both have low A3Offset"),
    ("P3", "Overshoot",             10, "SINR < 5 + a distant high-power cell dominates Top-neighbor list"),
    ("P4", "Coverage Hole",         17, "Serving RSRP <= -100 and all neighbors also weak"),
    ("P5", "Server Issue",          1,  "SINR >= 10 (healthy) but throughput varies -- non-RF cause"),
    ("P6", "Excessive Downtilt",    4,  "Neighbor cell Mechanical + Digital Tilt >= 20 deg -> coverage gap"),
    ("P7", "Insufficient Data",     6,  "All metrics within normal range -- no anomaly, no diagnosis"),
]


# ---------------------------------------------------------------------------
# 유틸
# ---------------------------------------------------------------------------
def parse_pipe(text: str) -> list[dict[str, str]]:
    """파이프 구분 문자열 테이블을 dict 리스트로 파싱."""
    lines = [ln.rstrip("\r") for ln in text.strip().split("\n") if ln.strip()]
    if not lines:
        return []
    header = lines[0].split("|")
    return [dict(zip(header, ln.split("|"))) for ln in lines[1:]]


def safe_float(s: str | None, default: float | None = None) -> float | None:
    """공백/'-'/빈 문자열을 None 으로 처리하는 float 파싱."""
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
    """WGS84 lon/lat → 지역 equirectangular km offset (기준점 lon0/lat0)."""
    radius_km = 111.0
    x = (lon - lon0) * radius_km * math.cos(math.radians(lat0))
    y = (lat - lat0) * radius_km
    return x, y


def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


# ---------------------------------------------------------------------------
# 렌더링
# ---------------------------------------------------------------------------
def render_scenario(
    ax: Axes,
    cells: list[dict],
    ue_rows: list[dict],
    code: str,
    name: str,
    idx: int,
    description: str,
    answer: str,
) -> None:
    """한 장의 axes 에 한 시나리오를 그린다."""

    # 기준점: 모든 cell + UE lat/lon 의 평균
    all_lons, all_lats = [], []
    for c in cells:
        lo = safe_float(c.get("Longitude"))
        la = safe_float(c.get("Latitude"))
        if lo is not None and la is not None:
            all_lons.append(lo)
            all_lats.append(la)
    for r in ue_rows:
        lo = safe_float(r.get("Longitude"))
        la = safe_float(r.get("Latitude"))
        if lo is not None and la is not None:
            all_lons.append(lo)
            all_lats.append(la)
    if not all_lons:
        raise ValueError(f"train[{idx}]: 유효한 lon/lat 없음")
    lon0 = float(np.mean(all_lons))
    lat0 = float(np.mean(all_lats))

    # sector 컬러맵: total tilt 0(green) → 25(red)
    tilt_cmap = plt.colormaps["RdYlGn_r"]

    # ---- UE 경로 먼저 (sector 뒤에 깔림) ----
    ue_xy: list[tuple[float, float, dict]] = []
    for r in ue_rows:
        lo = safe_float(r.get("Longitude"))
        la = safe_float(r.get("Latitude"))
        if lo is None or la is None:
            continue
        x, y = to_km(lo, la, lon0, lat0)
        ue_xy.append((x, y, r))

    if ue_xy:
        xs = [p[0] for p in ue_xy]
        ys = [p[1] for p in ue_xy]
        ax.plot(xs, ys, color="steelblue", linewidth=1.6, alpha=0.55, zorder=2, label="UE drive path")

    # ---- sector 부채꼴 ----
    for c in cells:
        lon = safe_float(c.get("Longitude"))
        lat = safe_float(c.get("Latitude"))
        if lon is None or lat is None:
            continue

        x, y = to_km(lon, lat, lon0, lat0)
        mech_az = safe_float(c.get("Mechanical Azimuth"), 0.0) or 0.0
        m_dt = safe_float(c.get("Mechanical Downtilt"), 0.0) or 0.0
        d_dt = safe_float(c.get("Digital Tilt"), 0.0) or 0.0
        total_tilt = m_dt + d_dt
        pwr = safe_float(c.get("Transmission Power"), 20.0) or 20.0
        pci = c.get("PCI", "?")
        a3off_raw = safe_float(c.get("IntraFreqHoA3Offset [0.5dB]"))
        a3off_db = (a3off_raw or 0) * 0.5  # 실효 dB
        height = safe_float(c.get("Height"), 0.0) or 0.0

        # geographic(N=0,E=90,시계) → matplotlib(E=0,N=90,반시계)
        math_center = (90.0 - mech_az) % 360.0
        beamwidth = 65.0  # 일반 sector 안테나 가정
        theta1 = math_center - beamwidth / 2.0
        theta2 = math_center + beamwidth / 2.0

        # power (11~32 dBm) → radius (0.15 ~ 0.95 km) 선형 매핑
        radius = 0.18 + clamp((pwr - 10.0) / 22.0, 0.0, 1.0) * 0.7
        color = tilt_cmap(clamp(total_tilt, 0.0, 25.0) / 25.0)

        wedge = Wedge(
            (x, y), radius, theta1, theta2,
            facecolor=color, edgecolor="black", linewidth=0.9, alpha=0.55, zorder=3,
        )
        ax.add_patch(wedge)
        # 안테나 위치 삼각형
        ax.plot(x, y, marker="^", color="black", markersize=11, markeredgecolor="white",
                markeredgewidth=0.8, zorder=6)

        # 라벨: 부채꼴 끝단 너머에 배치
        tip_x = x + (radius + 0.10) * math.cos(math.radians(math_center))
        tip_y = y + (radius + 0.10) * math.sin(math.radians(math_center))

        a3_text = f"A3Off={int(a3off_raw)}={a3off_db:.1f}dB" if a3off_raw is not None else "A3Off=?"
        label = (f"PCI {pci}\n"
                 f"Az {int(mech_az)}°\n"
                 f"M{int(m_dt)}°+D{int(d_dt)}° (tot={int(total_tilt)}°)\n"
                 f"Pwr {int(pwr)} dBm · h {int(height)}m\n"
                 f"{a3_text}")

        ax.annotate(
            label, xy=(tip_x, tip_y),
            fontsize=6.8, ha="center", va="center", zorder=7,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="gray", alpha=0.9, linewidth=0.6),
        )

    # ---- UE 샘플 점 (throughput 저하 강조) ----
    if ue_xy:
        low_count = 0
        for x, y, r in ue_xy:
            tp = safe_float(r.get("5G KPI PCell Layer2 MAC DL Throughput [Mbps]"))
            if tp is not None and tp < 100:
                low_count += 1
                ax.plot(x, y, "o", color="crimson", markersize=8,
                        markeredgecolor="black", markeredgewidth=0.6, zorder=8)
            else:
                ax.plot(x, y, "o", color="steelblue", markersize=4, zorder=5)

        # START / END 라벨
        ax.annotate(
            "START", xy=(ue_xy[0][0], ue_xy[0][1]),
            xytext=(10, 10), textcoords="offset points",
            fontsize=8, fontweight="bold", color="darkgreen",
            bbox=dict(boxstyle="round,pad=0.2", fc="#e8f8e8", ec="darkgreen", linewidth=0.7),
            zorder=10,
        )
        ax.annotate(
            "END", xy=(ue_xy[-1][0], ue_xy[-1][1]),
            xytext=(10, -14), textcoords="offset points",
            fontsize=8, fontweight="bold", color="darkred",
            bbox=dict(boxstyle="round,pad=0.2", fc="#f8e8e8", ec="darkred", linewidth=0.7),
            zorder=10,
        )

    # ---- 축/제목/캡션 ----
    ax.set_aspect("equal", adjustable="datalim")
    ax.grid(True, linestyle=":", alpha=0.45)
    ax.set_xlabel("East–West offset (km)", fontsize=9)
    ax.set_ylabel("North–South offset (km)", fontsize=9)

    tag_label = "multiple-answer" if "|" in answer else "single-answer"
    ax.set_title(
        f"Track A  {code}  {name}   ——   train[{idx}]   answer={answer}  ({tag_label})",
        fontsize=12, fontweight="bold", pad=10,
    )

    # 뷰포트 여유 확보
    cur_xlim = ax.get_xlim()
    cur_ylim = ax.get_ylim()
    pad_x = (cur_xlim[1] - cur_xlim[0]) * 0.08 + 0.15
    pad_y = (cur_ylim[1] - cur_ylim[0]) * 0.08 + 0.15
    ax.set_xlim(cur_xlim[0] - pad_x, cur_xlim[1] + pad_x)
    ax.set_ylim(cur_ylim[0] - pad_y, cur_ylim[1] + pad_y)

    # Caption box
    caption = (
        f"Pattern trigger: {description}\n"
        f"Triangle = gNodeB antenna  |  Wedge = sector beam (65 deg beamwidth, direction = Mechanical Azimuth)\n"
        f"Wedge radius proportional to Tx Power (11-32 dBm)  |  Color: green = low total tilt (wide cover), "
        f"red = tilt >= 20 deg (narrow)\n"
        f"Blue line/dots = UE drive path (~10 s window)  |  Red dots = UE samples with Throughput < 100 Mbps"
    )
    ax.text(
        0.5, -0.16, caption,
        transform=ax.transAxes, ha="center", va="top",
        fontsize=7.8, color="#333333", style="italic",
        bbox=dict(boxstyle="round,pad=0.4", fc="#fafafa", ec="#cccccc", linewidth=0.6),
    )


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main() -> int:
    if not TRAIN_JSON.exists():
        print(f"ERROR: {TRAIN_JSON} 가 없습니다")
        return 1

    print(f"Loading {TRAIN_JSON.name} ...")
    with TRAIN_JSON.open() as f:
        data = json.load(f)
    print(f"  → {len(data)} scenarios")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Output dir: {OUT_DIR.relative_to(REPO_ROOT)}")

    for code, name, idx, desc in PATTERNS:
        if idx >= len(data):
            print(f"[skip] train[{idx}] 없음")
            continue

        scenario = data[idx]
        cells = parse_pipe(scenario["data"]["network_configuration_data"])
        ue_rows = parse_pipe(scenario["data"]["user_plane_data"])
        answer = scenario.get("answer", "?")

        fig, ax = plt.subplots(figsize=(11, 8.5))
        fig.subplots_adjust(bottom=0.18, top=0.92, left=0.08, right=0.96)

        try:
            render_scenario(ax, cells, ue_rows, code, name, idx, desc, answer)
        except Exception as e:  # noqa: BLE001
            print(f"[error] {code} train[{idx}]: {e}")
            plt.close(fig)
            continue

        slug = name.lower().replace(" ", "_")
        out_path = OUT_DIR / f"{code}_{slug}_train{idx:03d}.png"
        fig.savefig(out_path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        rel = out_path.relative_to(REPO_ROOT)
        print(f"  ✓ {code} {name:<22} → {rel}  (cells={len(cells)}, ue={len(ue_rows)}, answer={answer})")

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
