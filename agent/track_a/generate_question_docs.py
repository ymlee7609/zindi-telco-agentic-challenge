#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Train.json 시나리오를 인간 판독 가능한 Markdown 문서로 변환.

각 문서에 10개 시나리오를 포함. 기술적 설명 + 데이터 테이블 + 정답 분석 포함.

Usage:
    # 처음 10개만 샘플 (questions_001.md)
    python agent/track_a/generate_question_docs.py --sample 10

    # 전체 2000개 (questions_001.md ~ questions_200.md)
    python agent/track_a/generate_question_docs.py --all
"""

from __future__ import annotations

import argparse
import json
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TRAIN_JSON = ROOT / "data" / "Track A" / "data" / "Phase_1" / "train.json"
TEST_JSON = ROOT / "data" / "Track A" / "data" / "Phase_1" / "test.json"
OUT_DIR_TRAIN = ROOT / "docs" / "track_a" / "questions" / "train"
OUT_DIR_TEST = ROOT / "docs" / "track_a" / "questions" / "test"

# 패턴 분류 (analyze_patterns.py 에서 가져옴)
LABEL_PATTERNS = {
    "P1 Late Handover": lambda l: ("decrease" in l) and ("a3" in l or "intrafreqhoa3" in l),
    "P2 Ping-pong": lambda l: ("increase" in l) and ("a3" in l or "intrafreqhoa3" in l),
    "P3 Overshoot (power)": lambda l: ("decrease" in l) and ("power" in l),
    "P3 Overshoot (tilt)": lambda l: ("press" in l) and ("tilt" in l),
    "P4 Coverage (power)": lambda l: ("increase" in l) and ("power" in l),
    "P4 Coverage / P6 Tilt": lambda l: ("lift" in l) and ("tilt" in l),
    "P4 Coverage (azimuth)": lambda l: ("azimuth" in l),
    "P5 Server Issue": lambda l: ("check test server" in l) or ("transmission issues" in l),
    "P7 Insufficient Data": lambda l: ("insufficient data" in l) or ("more data" in l),
    "P8 PDCCH Resource": lambda l: ("pdcch" in l),
    "P9 Missing Neighbor": lambda l: ("add neighbor" in l),
    "P10 Coverage Threshold": lambda l: ("threshold" in l or "thld" in l) and ("a3" not in l),
}


def classify_label(label: str) -> str:
    lw = label.lower()
    for name, matcher in LABEL_PATTERNS.items():
        if matcher(lw):
            return name
    return "Unknown"


def parse_pipe(text: str) -> tuple[list[str], list[list[str]]]:
    """파이프 구분자 CSV를 헤더 + 데이터 행으로 파싱."""
    lines = [ln.rstrip("\r") for ln in (text or "").strip().split("\n") if ln.strip()]
    if not lines:
        return [], []
    headers = lines[0].split("|")
    rows = [ln.split("|") for ln in lines[1:]]
    return headers, rows


def format_table(headers: list[str], rows: list[list[str]], max_cols: int = 12) -> str:
    """Markdown 테이블 생성 (열 수 제한, 긴 값 축약)."""
    if not headers:
        return "(데이터 없음)"

    # 열 수 제한
    h = headers[:max_cols]
    # 헤더 축약
    short_h = []
    for col in h:
        # 긴 헤더 축약
        col = col.replace("5G KPI PCell RF Serving ", "")
        col = col.replace("5G KPI PCell Layer2 MAC DL ", "DL ")
        col = col.replace("5G KPI PCell Layer2 MAC UL ", "UL ")
        col = col.replace("[Mbps]", "(Mbps)")
        col = col.replace("[dBm]", "(dBm)")
        col = col.replace("[dB]", "(dB)")
        if len(col) > 25:
            col = col[:22] + "..."
        short_h.append(col)

    lines = []
    lines.append("| " + " | ".join(short_h) + " |")
    lines.append("| " + " | ".join(["---"] * len(short_h)) + " |")

    for row in rows:
        vals = []
        for i, v in enumerate(row[:max_cols]):
            v = v.strip()
            if len(v) > 30:
                v = v[:27] + "..."
            vals.append(v)
        # 부족한 열 채우기
        while len(vals) < len(short_h):
            vals.append("")
        lines.append("| " + " | ".join(vals) + " |")

    if len(headers) > max_cols:
        lines.append(f"\n> *... {len(headers) - max_cols}개 열 생략 (전체 {len(headers)}열)*")

    return "\n".join(lines)


def render_scenario(idx: int, scenario: dict, source: str = "train") -> str:
    """단일 시나리오를 Markdown으로 렌더링."""
    sid = scenario["scenario_id"]
    tag = scenario["tag"]
    answer = scenario.get("answer", "To be determined")
    task = scenario.get("task", {})
    data = scenario.get("data", {})
    context = scenario.get("context", {})
    opts_map = {o["id"]: o["label"] for o in task.get("options", [])}

    is_test = (source == "test") or answer == "To be determined"

    lines: list[str] = []
    lines.append(f"### 문제 {idx}: `{sid[:12]}...`")
    lines.append("")

    # 기본 정보
    lines.append("| 항목 | 값 |")
    lines.append("| --- | --- |")
    lines.append(f"| Scenario ID | `{sid}` |")
    lines.append(f"| Tag | **{tag}** |")

    if is_test:
        lines.append(f"| 정답 | *(비공개)* |")
    else:
        lines.append(f"| 정답 | **{answer}** |")
        answer_ids = [a.strip() for a in answer.split("|")]
        answer_labels = [(aid, opts_map.get(aid, "?")) for aid in answer_ids]
        answer_patterns = [(aid, label, classify_label(label)) for aid, label in answer_labels]
        for aid, label, pattern in answer_patterns:
            lines.append(f"| {aid} 의미 | {label} |")
        lines.append(f"| 패턴 분류 | **{answer_patterns[0][2]}** |")
    lines.append("")

    # 시각화 이미지 (top-view + 시계열)
    img_name = f"{source}_{idx:04d}.png"
    lines.append(f"**시각화 (기지국 배치 + UE 시계열)**")
    lines.append("")
    lines.append(f"![{source}[{idx}] topology](images/{img_name})")
    lines.append("")

    # Context
    ctx_desc = context.get("description", "")
    wni = context.get("wireless_network_information", {})
    if ctx_desc:
        lines.append(f"> **배경**: {ctx_desc}")
        if wni:
            lines.append(f"> 네트워크: {wni.get('network_type', '?')}, "
                         f"기지국 {wni.get('num_base_stations', '?')}개, "
                         f"시나리오: {wni.get('mobility_scenario', '?')}")
        lines.append("")

    # 옵션 목록
    lines.append("**선택지 (22개)**")
    lines.append("")
    answer_id_set = set()
    if not is_test:
        answer_id_set = {a.strip() for a in answer.split("|")}
    for opt in task.get("options", []):
        marker = " **← 정답**" if opt["id"] in answer_id_set else ""
        lines.append(f"- `{opt['id']}`: {opt['label']}{marker}")
    lines.append("")

    # UE 데이터 (User Plane)
    upd = data.get("user_plane_data", "")
    if upd:
        h, r = parse_pipe(upd)
        lines.append("**UE 측정 데이터 (User Plane)**")
        lines.append("")
        lines.append(format_table(h, r))
        lines.append("")

        # 기술 해석
        lines.append("<details>")
        lines.append("<summary>UE 데이터 해석 가이드</summary>")
        lines.append("")
        lines.append("- **Timestamp**: 측정 시각 (초 단위 정밀도)")
        lines.append("- **SS-RSRP (dBm)**: 참조 신호 수신 전력. -100 이하는 약한 신호")
        lines.append("- **SS-SINR (dB)**: 신호 대 간섭+잡음비. 5 이하는 간섭 심각, 10 이상은 양호")
        lines.append("- **DL Throughput (Mbps)**: 다운링크 처리량. 100 미만은 성능 저하 의심")
        lines.append("- **Serving PCI**: 현재 서빙 셀의 물리적 셀 ID. 값이 바뀌면 핸드오버 발생")
        lines.append("")
        lines.append("</details>")
        lines.append("")

    # 네트워크 구성 데이터
    ncd = data.get("network_configuration_data", "")
    if ncd:
        h, r = parse_pipe(ncd)
        lines.append("**기지국 구성 (Network Configuration)**")
        lines.append("")
        lines.append(format_table(h, r, max_cols=16))
        lines.append("")

        lines.append("<details>")
        lines.append("<summary>기지국 구성 해석 가이드</summary>")
        lines.append("")
        lines.append("- **Mechanical Azimuth**: 안테나 수평 방향 (0°=북, 90°=동)")
        lines.append("- **Mechanical Downtilt + Digital Tilt**: 합계가 안테나 하향각. 20° 이상이면 과도한 downtilt")
        lines.append("- **Transmission Power**: 송신 전력 (dBm). 높을수록 커버리지 넓음")
        lines.append("- **IntraFreqHoA3Offset**: A3 핸드오버 임계값 (0.5dB 단위). 10 이상이면 핸드오버 지연")
        lines.append("- **PdcchOccupiedSymbolNum**: PDCCH 리소스 할당. 1SYM은 기본, 2SYM은 확장")
        lines.append("- **CovInterFreqA2RsrpThld**: Inter-freq 커버리지 임계값. -95가 -105보다 보수적 (높음)")
        lines.append("- **PCell Neighbor Cell**: 설정된 이웃 셀 목록 (핸드오버 후보)")
        lines.append("")
        lines.append("</details>")
        lines.append("")

    # Signaling Events
    spd = data.get("signaling_plane_data", "")
    if spd:
        h, r = parse_pipe(spd)
        lines.append("**시그널링 이벤트 (Signaling Plane)**")
        lines.append("")
        lines.append(format_table(h, r, max_cols=6))
        lines.append("")

    # Traffic Data
    td = data.get("traffic_data", "")
    if td:
        h, r = parse_pipe(td)
        lines.append("**트래픽 통계 (Traffic Data)**")
        lines.append("")
        lines.append(format_table(h, r, max_cols=10))
        lines.append("")

    # MR Data
    mr = data.get("mr_data", "")
    if mr:
        h, r = parse_pipe(mr)
        lines.append("**MR (Measurement Report)**")
        lines.append("")
        lines.append(format_table(h, r, max_cols=12))
        lines.append("")

    lines.append("---")
    lines.append("")

    return "\n".join(lines)


def generate_doc(scenarios: list[dict], start_idx: int, doc_num: int,
                 source: str = "train") -> str:
    """10개 시나리오 묶음을 하나의 Markdown 문서로 생성."""
    end_idx = start_idx + len(scenarios) - 1
    is_test = source == "test"
    src_file = "test.json" if is_test else "train.json"

    lines = [
        f"# Track A 문제 분석 — {source}[{start_idx}]~{source}[{end_idx}]",
        "",
        f"> 자동 생성: `generate_question_docs.py`",
        f"> 원본: `data/Track A/data/Phase_1/{src_file}`",
        f"> 범위: {source}[{start_idx}] ~ {source}[{end_idx}] ({len(scenarios)}개)",
        "",
        "## 목차",
        "",
    ]

    for i, s in enumerate(scenarios):
        idx = start_idx + i
        sid = s["scenario_id"][:12]
        tag = s["tag"]
        answer = s.get("answer", "비공개")
        if is_test or answer == "To be determined":
            lines.append(f"{i+1}. [문제 {idx}: `{sid}...`](#{idx}) — {tag}")
        else:
            lines.append(f"{i+1}. [문제 {idx}: `{sid}...`](#{idx}) — {tag}, 정답: {answer}")

    lines.append("")
    lines.append("---")
    lines.append("")

    for i, s in enumerate(scenarios):
        idx = start_idx + i
        lines.append(render_scenario(idx, s, source=source))

    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description="Train/Test JSON → Markdown 변환")
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--sample", type=int, help="처음 N개만 변환 (샘플)")
    group.add_argument("--all", action="store_true", help="전체 변환")
    ap.add_argument("--source", choices=["train", "test"], default="train",
                    help="데이터 소스 (train.json or test.json)")
    ap.add_argument("--batch-size", type=int, default=10, help="파일당 시나리오 수")
    args = ap.parse_args()

    src_json = TRAIN_JSON if args.source == "train" else TEST_JSON
    out_dir = OUT_DIR_TRAIN if args.source == "train" else OUT_DIR_TEST

    with open(src_json, encoding="utf-8") as f:
        data = json.load(f)

    total = args.sample if args.sample else len(data)
    batch = args.batch_size
    out_dir.mkdir(parents=True, exist_ok=True)

    n_docs = 0
    for start in range(0, total, batch):
        end = min(start + batch, total)
        scenarios = data[start:end]
        doc_num = start // batch + 1
        doc = generate_doc(scenarios, start, doc_num, source=args.source)

        out_path = out_dir / f"questions_{doc_num:03d}.md"
        out_path.write_text(doc, encoding="utf-8")
        n_docs += 1
        print(f"  {out_path.name}: {args.source}[{start}]~{args.source}[{end-1}] ({len(scenarios)}개)")

    print(f"\n완료: {n_docs}개 문서, {total}개 시나리오 → {out_dir}")


if __name__ == "__main__":
    main()
