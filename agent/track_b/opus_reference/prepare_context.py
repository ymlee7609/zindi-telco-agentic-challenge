"""Track B Opus Reference Context Extractor.

각 질문 유형(TOPO/PATH/FAULT)에 맞게 구조화된 context 파일을 생성한다.
기존 parser (topology_parser, fault_analyzer, path_tracer, cli_parsers) 를
import 해서 재활용하며, 신규 파싱 로직을 최소화한다.

Usage:
    python3 agent/track_b/opus_reference/prepare_context.py --qids 1 11 17
    python3 agent/track_b/opus_reference/prepare_context.py --all
"""
# pyright: reportMissingImports=false
# @MX:NOTE: sys.path.insert() 이후 import이므로 static analyzer가 경로를 모름. 런타임에는 정상.

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# 경로 설정: agent/track_b 를 sys.path 에 추가 (parser import 용)
# ---------------------------------------------------------------------------
_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_TRACK_B_DIR = _REPO_ROOT / "agent" / "track_b"
sys.path.insert(0, str(_TRACK_B_DIR))

try:
    from cli_parsers import (
        list_devices,
        parse_interface_brief,
        parse_interface_description,
        parse_ip_interface_brief,
        parse_lldp,
        parse_routing_table,
        read_file,
    )
except ImportError as e:
    print(f"[ERROR] cli_parsers import 실패: {e}", file=sys.stderr)
    print(
        "  agent/track_b/cli_parsers.py 를 찾을 수 없습니다. "
        "프로젝트 루트에서 스크립트를 실행하세요.",
        file=sys.stderr,
    )
    sys.exit(1)

try:
    from topology_parser import (
        _TOPOLOGY_TARGETS,
        solve_topology,
        format_answer as topo_format_answer,
    )
except ImportError as e:
    print(f"[ERROR] topology_parser import 실패: {e}", file=sys.stderr)
    sys.exit(1)

try:
    from fault_analyzer import (
        extract_fault_scenarios,
        solve_fault,
    )
except ImportError as e:
    print(f"[ERROR] fault_analyzer import 실패: {e}", file=sys.stderr)
    sys.exit(1)

try:
    from path_tracer import (
        extract_path_info,
        trace_path_by_routing,
    )
except ImportError as e:
    print(f"[ERROR] path_tracer import 실패: {e}", file=sys.stderr)
    sys.exit(1)

# ---------------------------------------------------------------------------
# 상수 정의
# ---------------------------------------------------------------------------
_TEST_JSON = _REPO_ROOT / "data" / "Track B" / "data" / "Phase_1" / "test.json"
_SUBMISSION_CSV = _TRACK_B_DIR / "submission" / "submission_v12_final.csv"
_OUTPUT_DIR = Path(__file__).resolve().parent / "contexts"

# ---------------------------------------------------------------------------
# 질문 유형 분류 (qid → 유형)
# ---------------------------------------------------------------------------
_TOPO_QIDS: frozenset[int] = frozenset(range(1, 7)) | frozenset(range(29, 34))
_PATH_QIDS: frozenset[int] = frozenset(range(7, 17)) | frozenset(range(34, 39))
_FAULT_QIDS: frozenset[int] = frozenset(range(17, 29)) | frozenset(range(39, 51))


def _question_type(qid: int) -> str:
    if qid in _TOPO_QIDS:
        return "TOPO"
    if qid in _PATH_QIDS:
        return "PATH"
    if qid in _FAULT_QIDS:
        return "FAULT"
    return "UNKNOWN"


# ---------------------------------------------------------------------------
# 데이터 로드 유틸
# ---------------------------------------------------------------------------

def load_test_data() -> dict[int, dict]:
    """test.json 로드 → {task_id: item}"""
    if not _TEST_JSON.exists():
        raise FileNotFoundError(f"test.json 없음: {_TEST_JSON}")
    with _TEST_JSON.open(encoding="utf-8") as f:
        raw = json.load(f)
    return {item["task"]["id"]: item for item in raw}


def load_v12_answers() -> dict[str, str]:
    """submission_v12_final.csv 로드 → {scenario_id: track_b_answer}"""
    if not _SUBMISSION_CSV.exists():
        print(f"[WARN] v12 CSV 없음: {_SUBMISSION_CSV}", file=sys.stderr)
        return {}
    result: dict[str, str] = {}
    with _SUBMISSION_CSV.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            result[row["ID"]] = row.get("Track B", "")
    return result


# ---------------------------------------------------------------------------
# 구조화 정보 추출 함수
# ---------------------------------------------------------------------------

def _interface_status_summary(qid: int, device: str) -> str:
    """장비 interface brief 요약 (UP 인터페이스 + IP)."""
    ifaces = parse_interface_brief(qid, device)
    ip_ifaces = parse_ip_interface_brief(qid, device)

    up_ifaces = [i for i in ifaces if i.is_up and "." not in i.name]
    if not up_ifaces:
        return f"  {device}: UP 인터페이스 없음"

    result_lines: list[str] = []
    for iface in up_ifaces[:15]:  # 최대 15개
        ip = ip_ifaces.get(iface.name, "")
        ip_str = f" [{ip}]" if ip else ""
        result_lines.append(f"  {iface.name}{ip_str}")

    if len(up_ifaces) > 15:
        result_lines.append(f"  ... 외 {len(up_ifaces) - 15}개")

    return f"**{device}** UP interfaces:\n" + "\n".join(result_lines)


def _arp_relevant(qid: int, device: str, target_ips: Optional[set[str]] = None) -> list[str]:
    """장비의 ARP 테이블에서 관련 항목 추출."""
    text = read_file(qid, device, "display_arp.txt")
    if not text:
        return []

    lines: list[str] = []
    for line in text.splitlines():
        # ARP 테이블 행 형식: IP MAC Expire VID Interface
        parts = line.split()
        if len(parts) < 4:
            continue
        ip_part = parts[0]
        if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip_part):
            continue
        if target_ips is None or ip_part in target_ips:
            lines.append(f"  {line.strip()}")

    return lines[:20]  # 최대 20행


def _routing_context(qid: int, device: str, relevant_prefixes: Optional[list[str]] = None) -> list[str]:
    """라우팅 테이블 요약 (관련 prefix 필터링)."""
    routes = parse_routing_table(qid, device)
    if not routes:
        return [f"  {device}: 라우팅 테이블 없음"]

    lines: list[str] = []
    for route in routes:
        if relevant_prefixes:
            if not any(route.destination.startswith(p.split("/")[0][:8]) for p in relevant_prefixes):
                continue
        lines.append(
            f"  {route.destination:20s} {route.proto:8s} via {route.nexthop:15s} dev {route.egress_if}"
        )

    if not lines:
        lines = [f"  (관련 경로 없음 — 필터링됨)"]

    return lines[:30]  # 최대 30행


def _interface_description_snippet(qid: int, device: str) -> list[str]:
    """interface description에서 link 정보 추출."""
    descs = parse_interface_description(qid, device)
    result: list[str] = []
    for iface, desc in descs.items():
        if desc.strip():
            result.append(f"  {iface}: {desc.strip()}")

    # PJ zone 장비는 display_interface_description.txt 가 비어있고
    # display_current-configuration.txt 의 `interface X / description Y` 블록에 기록됨
    if not result:
        result = _parse_pj_config_description(qid, device)

    return result[:20]


def _parse_pj_config_description(qid: int, device: str) -> list[str]:
    """PJ zone: display_current-configuration.txt 에서 `interface / description` 추출."""
    text = read_file(qid, device, "display_current-configuration.txt")
    if not text:
        return []

    # 블록 단위로 `interface X` + 다음 빈 줄까지 스캔
    result: list[str] = []
    current_if: Optional[str] = None
    for raw in text.splitlines():
        line = raw.rstrip()
        m = re.match(r"^interface\s+(\S+)", line)
        if m:
            current_if = m.group(1)
            continue
        if current_if and line.startswith(" description "):
            desc = line[len(" description "):].strip()
            if desc:
                result.append(f"  {current_if}: {desc}")
            current_if = None
    return result




# ---------------------------------------------------------------------------
# TOPO context 생성
# ---------------------------------------------------------------------------

def _build_topo_context(
    qid: int,
    item: dict,
    v12_answer: str,
) -> str:
    """TOPO 유형 (링크 복원) context 생성."""
    data_qid, target = _TOPOLOGY_TARGETS.get(qid, (qid, "UNKNOWN"))
    question_text = item["task"]["question"]
    scenario_id = item["scenario_id"]

    # deterministic solver 호출
    try:
        links, confidence, method, resolved, total_up = solve_topology(data_qid, target)
        det_answer = topo_format_answer(target, links)
    except Exception as e:
        det_answer = f"[solver 오류: {e}]"
        confidence = "L"
        method = "error"
        resolved, total_up = 0, 0

    devices = list_devices(data_qid)

    # LLDP 그래프 (타겟 장비 및 1-hop 이웃)
    target_neighbors: set[str] = set()
    lldp_lines: list[str] = []
    for nb in parse_lldp(data_qid, target):
        target_neighbors.add(nb.neighbor_device)
        lldp_lines.append(
            f"  {target} {nb.local_if} <-> {nb.neighbor_device} {nb.neighbor_if}"
        )

    # 역방향: 이웃 장비에서 타겟이 neighbor 로 등장하는지
    reverse_lldp: list[str] = []
    for dev in devices:
        if dev == target:
            continue
        for nb in parse_lldp(data_qid, dev):
            if nb.neighbor_device == target:
                reverse_lldp.append(
                    f"  {dev} {nb.local_if} <-> {target} {nb.neighbor_if}"
                )

    # interface description (타겟 장비)
    desc_lines = _interface_description_snippet(data_qid, target)

    # ARP 맵핑 (타겟 + 주변)
    arp_lines: list[str] = []
    for dev in [target] + list(target_neighbors)[:5]:
        rows = _arp_relevant(data_qid, dev)
        if rows:
            arp_lines.append(f"\n  [{dev}]")
            arp_lines.extend(rows[:10])

    # interface status
    iface_status = _interface_status_summary(data_qid, target)

    # raw 파일 참조
    raw_refs = [
        f"  data/Track B/devices_outputs/{data_qid}/{target}/display_interface_brief.txt",
        f"  data/Track B/devices_outputs/{data_qid}/{target}/display_lldp_neighbor_brief.txt",
        f"  data/Track B/devices_outputs/{data_qid}/{target}/display_interface_description.txt",
        f"  data/Track B/devices_outputs/{data_qid}/{target}/display_arp.txt",
    ]
    for nb in list(target_neighbors)[:3]:
        raw_refs.append(
            f"  data/Track B/devices_outputs/{data_qid}/{nb}/display_lldp_neighbor_brief.txt"
        )

    lines = [
        f"# Q{qid}: TOPO — Link Restore ({target})",
        "",
        f"**scenario_id**: {scenario_id}",
        f"**v12 answer**: {v12_answer.splitlines()[0] if v12_answer else '(없음)'}",
        f"**deterministic solver**: confidence={confidence}, method={method}, "
        f"resolved={resolved}/{total_up} ports",
        "",
        "## Question (from test.json)",
        "",
        question_text,
        "",
        "## Devices in Scenario",
        "",
        f"총 {len(devices)}개 장비: {', '.join(devices[:10])}" + (f" ... 외 {len(devices)-10}개" if len(devices) > 10 else ""),
        f"\n**Target**: `{target}`",
        "",
        "## Topology Snapshot — LLDP Graph",
        "",
        "### 타겟 장비 직접 LLDP neighbors",
        "",
    ]

    if lldp_lines:
        lines.extend(lldp_lines)
    else:
        lines.append("  (LLDP 정보 없음)")

    lines += [
        "",
        "### 역방향 LLDP (타겟이 neighbor로 등장)",
        "",
    ]
    if reverse_lldp:
        lines.extend(reverse_lldp)
    else:
        lines.append("  (역방향 LLDP 없음)")

    lines += [
        "",
        "## Interface Description (타겟 장비)",
        "",
    ]
    if desc_lines:
        lines.extend(desc_lines)
    else:
        lines.append("  (description 없음)")

    lines += [
        "",
        "## Interface Status",
        "",
        iface_status,
        "",
        "## ARP Mappings",
        "",
    ]
    if arp_lines:
        lines.extend(arp_lines)
    else:
        lines.append("  (ARP 정보 없음)")

    lines += [
        "",
        "## Raw File References",
        "",
    ]
    lines.extend(raw_refs)

    lines += [
        "",
        "## Deterministic Solver Result",
        "",
        "```",
        det_answer if det_answer else "(풀이 실패)",
        "```",
        "",
        "## v12 Answer (검증 대상)",
        "",
        "```",
        v12_answer if v12_answer else "(없음)",
        "```",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# PATH context 생성
# ---------------------------------------------------------------------------

def _build_path_context(
    qid: int,
    item: dict,
    v12_answer: str,
) -> str:
    """PATH 유형 (경로 추적) context 생성."""
    question_text = item["task"]["question"]
    scenario_id = item["scenario_id"]

    # path_tracer 에서 src/dst 추출
    try:
        path_info = extract_path_info(question_text)
    except Exception as e:
        path_info = {"src_node": "", "dst_node": None, "dst_ip": None, "dst_port": None}

    src_node = path_info.get("src_node", "")
    dst_node = path_info.get("dst_node")
    dst_ip = path_info.get("dst_ip")
    dst_port = path_info.get("dst_port")

    # deterministic solver 호출
    try:
        det_answer, det_conf = trace_path_by_routing(qid, question_text)
    except Exception as e:
        det_answer = f"[solver 오류: {e}]"
        det_conf = "L"

    devices = list_devices(qid)

    # 관련 장비 추출 (src + dst + 질문에서 언급된 장비)
    _NODE_RE = re.compile(
        r"\b([A-Z][a-z]+-[A-Z][a-z]+-\d+|[A-Z][a-zA-Z]+-[A-Z][a-zA-Z]+-\d+)\b"
    )
    mentioned = set(_NODE_RE.findall(question_text))
    devices_set = set(devices)
    relevant_devices = list((mentioned & devices_set))[:8]

    if src_node and src_node in devices_set and src_node not in relevant_devices:
        relevant_devices.insert(0, src_node)
    if dst_node and dst_node in devices_set and dst_node not in relevant_devices:
        relevant_devices.append(dst_node)

    # LLDP 토폴로지 스냅샷 (관련 장비만)
    lldp_lines: list[str] = []
    seen_links: set[frozenset] = set()
    for dev in relevant_devices:
        for nb in parse_lldp(qid, dev):
            key = frozenset([f"{dev}:{nb.local_if}", f"{nb.neighbor_device}:{nb.neighbor_if}"])
            if key not in seen_links:
                seen_links.add(key)
                lldp_lines.append(
                    f"  {dev} {nb.local_if} <-> {nb.neighbor_device} {nb.neighbor_if}"
                )

    # IP 인터페이스 현황 (관련 장비)
    ip_iface_sections: list[str] = []
    for dev in relevant_devices[:6]:
        ip_ifaces = parse_ip_interface_brief(qid, dev)
        if ip_ifaces:
            ip_lines = [f"    {port}: {ip}" for port, ip in list(ip_ifaces.items())[:8]]
            ip_iface_sections.append(f"  **{dev}**:\n" + "\n".join(ip_lines))

    # 라우팅 컨텍스트 (src → dst 경로 관련)
    routing_sections: list[str] = []
    relevant_prefixes = [dst_ip] if dst_ip else []
    for dev in relevant_devices[:6]:
        rt_lines = _routing_context(qid, dev, relevant_prefixes if relevant_prefixes else None)
        if rt_lines:
            routing_sections.append(
                f"  **{dev}** routing table (관련 경로):\n" + "\n".join(rt_lines[:15])
            )

    # raw 파일 참조
    raw_refs = []
    for dev in relevant_devices[:5]:
        raw_refs.extend([
            f"  data/Track B/devices_outputs/{qid}/{dev}/display_ip_routing-table.txt",
            f"  data/Track B/devices_outputs/{qid}/{dev}/display_ip_interface_brief.txt",
        ])

    lines = [
        f"# Q{qid}: PATH — Addressing Path Trace",
        "",
        f"**scenario_id**: {scenario_id}",
        f"**v12 answer**: {v12_answer.strip()[:100] if v12_answer else '(없음)'}",
        f"**deterministic solver**: {det_answer!r} (conf={det_conf})",
        "",
        "## Question (from test.json)",
        "",
        question_text,
        "",
        "## Path Info Extracted",
        "",
        f"- src_node: `{src_node}`",
        f"- dst_node: `{dst_node}`",
        f"- dst_ip: `{dst_ip}`",
        f"- dst_port: `{dst_port}`",
        "",
        "## Devices in Scenario",
        "",
        f"총 {len(devices)}개 장비 (관련 장비 {len(relevant_devices)}개 중점 분석)",
        f"관련: {', '.join(relevant_devices)}",
        "",
        "## Topology Snapshot — LLDP (관련 장비)",
        "",
    ]

    if lldp_lines:
        lines.extend(lldp_lines[:30])
    else:
        lines.append("  (LLDP 정보 없음)")

    lines += [
        "",
        "## Interface Status (IP 주소 포함)",
        "",
    ]
    if ip_iface_sections:
        for section in ip_iface_sections:
            lines.append(section)
            lines.append("")
    else:
        lines.append("  (IP 인터페이스 정보 없음)")

    lines += [
        "",
        "## Routing Context",
        "",
    ]
    if routing_sections:
        for section in routing_sections:
            lines.append(section)
            lines.append("")
    else:
        lines.append("  (라우팅 정보 없음)")

    lines += [
        "",
        "## Raw File References",
        "",
    ]
    lines.extend(raw_refs)

    lines += [
        "",
        "## Deterministic Solver Result",
        "",
        "```",
        det_answer if det_answer else "(풀이 실패)",
        "```",
        "",
        "## v12 Answer (검증 대상)",
        "",
        "```",
        v12_answer if v12_answer else "(없음)",
        "```",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# FAULT context 생성
# ---------------------------------------------------------------------------

def _build_fault_context(
    qid: int,
    item: dict,
    v12_answer: str,
) -> str:
    """FAULT 유형 (routing/port fault 탐지) context 생성."""
    question_text = item["task"]["question"]
    scenario_id = item["scenario_id"]

    # fault_analyzer solver 호출
    try:
        scenarios = extract_fault_scenarios(question_text)
        det_answer, det_conf = solve_fault(qid, question_text)
    except Exception as e:
        scenarios = []
        det_answer = f"[solver 오류: {e}]"
        det_conf = "L"

    devices = list_devices(qid)

    # 시나리오에서 언급된 장비 추출
    _NODE_RE = re.compile(
        r"\b([A-Z][a-z]+-[A-Z][a-z]+-\d+|[A-Z][a-zA-Z]+-[A-Z][a-zA-Z]+-\d+)\b"
    )
    mentioned = set(_NODE_RE.findall(question_text))
    devices_set = set(devices)
    suspect_devices = list(mentioned & devices_set)[:10]

    # fault scenario에서 IP 수집
    fault_ips: list[str] = []
    for sc in scenarios:
        if sc.get("dst_ip"):
            fault_ips.append(sc["dst_ip"])

    # 의심 장비 라우팅 테이블 + interface 상태
    routing_sections: list[str] = []
    iface_sections: list[str] = []
    for dev in suspect_devices[:8]:
        # 라우팅 테이블
        rt_lines = _routing_context(qid, dev, fault_ips if fault_ips else None)
        if rt_lines:
            routing_sections.append(
                f"  **{dev}** routing table:\n" + "\n".join(rt_lines[:20])
            )

        # interface 상태 (DOWN 포함)
        ifaces = parse_interface_brief(qid, dev)
        ip_ifaces = parse_ip_interface_brief(qid, dev)
        notable = []
        for iface in ifaces:
            if "." in iface.name:
                continue
            ip = ip_ifaces.get(iface.name, "")
            status = "UP" if iface.is_up else f"DOWN(phy={iface.phy},proto={iface.protocol})"
            if ip or not iface.is_up:
                notable.append(f"    {iface.name:20s} {status:30s} {ip}")
        if notable:
            iface_sections.append(f"  **{dev}**:\n" + "\n".join(notable[:12]))

    # LLDP (의심 장비 중심)
    lldp_lines: list[str] = []
    seen_links: set[frozenset] = set()
    for dev in suspect_devices[:6]:
        for nb in parse_lldp(qid, dev):
            key = frozenset([f"{dev}:{nb.local_if}", f"{nb.neighbor_device}:{nb.neighbor_if}"])
            if key not in seen_links:
                seen_links.add(key)
                lldp_lines.append(
                    f"  {dev} {nb.local_if} <-> {nb.neighbor_device} {nb.neighbor_if}"
                )

    # logbuffer 스니핏 (의심 장비 첫 번째)
    log_snippet: str = ""
    for dev in suspect_devices[:3]:
        log_text = read_file(qid, dev, "display_logbuffer.txt")
        if log_text:
            relevant_lines = [
                ln.strip() for ln in log_text.splitlines()
                if any(kw in ln.lower() for kw in ["error", "down", "fail", "unreachable", "timeout"])
            ]
            if relevant_lines:
                log_snippet = f"**{dev}** log (관련 항목):\n" + "\n".join(
                    f"  {ln}" for ln in relevant_lines[:10]
                )
                break

    # raw 파일 참조
    raw_refs = []
    for dev in suspect_devices[:5]:
        raw_refs.extend([
            f"  data/Track B/devices_outputs/{qid}/{dev}/display_ip_routing-table.txt",
            f"  data/Track B/devices_outputs/{qid}/{dev}/display_interface_brief.txt",
            f"  data/Track B/devices_outputs/{qid}/{dev}/display_ip_interface_brief.txt",
        ])

    # fault scenario 요약
    sc_summary_lines: list[str] = []
    for i, sc in enumerate(scenarios, 1):
        sc_summary_lines.append(
            f"  Scenario {i}: src={sc.get('src_node','?')} "
            f"dst_ip={sc.get('dst_ip','?')} "
            f"suspects={sc.get('suspect_nodes', [])}"
        )

    lines = [
        f"# Q{qid}: FAULT — Routing/Port Fault Detection",
        "",
        f"**scenario_id**: {scenario_id}",
        f"**v12 answer**: {v12_answer.splitlines()[0] if v12_answer else '(없음)'}",
        f"**deterministic solver**: conf={det_conf}, scenarios={len(scenarios)}개",
        "",
        "## Question (from test.json)",
        "",
        question_text,
        "",
        "## Fault Scenarios Extracted",
        "",
    ]

    if sc_summary_lines:
        lines.extend(sc_summary_lines)
    else:
        lines.append("  (시나리오 추출 실패)")

    lines += [
        "",
        "## Devices in Scenario",
        "",
        f"총 {len(devices)}개 장비 (의심 장비 {len(suspect_devices)}개 중점 분석)",
        f"의심: {', '.join(suspect_devices)}",
        "",
        "## Topology Snapshot — LLDP (의심 장비)",
        "",
    ]

    if lldp_lines:
        lines.extend(lldp_lines[:25])
    else:
        lines.append("  (LLDP 정보 없음)")

    lines += [
        "",
        "## Interface Status (의심 장비 — DOWN 포함)",
        "",
    ]
    if iface_sections:
        for section in iface_sections:
            lines.append(section)
            lines.append("")
    else:
        lines.append("  (인터페이스 정보 없음)")

    lines += [
        "",
        "## Routing Context (의심 장비)",
        "",
    ]
    if routing_sections:
        for section in routing_sections:
            lines.append(section)
            lines.append("")
    else:
        lines.append("  (라우팅 정보 없음)")

    if log_snippet:
        lines += [
            "",
            "## Log Buffer Snippet (오류 관련)",
            "",
            log_snippet,
        ]

    lines += [
        "",
        "## Raw File References",
        "",
    ]
    lines.extend(raw_refs)

    lines += [
        "",
        "## Deterministic Solver Result",
        "",
        "```",
        det_answer if det_answer else "(풀이 실패)",
        "```",
        "",
        "## v12 Answer (검증 대상)",
        "",
        "```",
        v12_answer if v12_answer else "(없음)",
        "```",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 메인 context 생성 디스패처
# ---------------------------------------------------------------------------

def build_context(
    qid: int,
    test_data: dict[int, dict],
    v12_answers: dict[str, str],
) -> str:
    """qid에 맞는 context 문자열 반환."""
    item = test_data.get(qid)
    if item is None:
        return f"# Q{qid}: 데이터 없음\n\ntest.json 에서 qid={qid} 를 찾을 수 없습니다.\n"

    scenario_id = item["scenario_id"]
    v12_answer = v12_answers.get(scenario_id, "")

    qtype = _question_type(qid)

    if qtype == "TOPO":
        return _build_topo_context(qid, item, v12_answer)
    elif qtype == "PATH":
        return _build_path_context(qid, item, v12_answer)
    elif qtype == "FAULT":
        return _build_fault_context(qid, item, v12_answer)
    else:
        return (
            f"# Q{qid}: UNKNOWN 유형\n\n"
            f"qid={qid} 는 TOPO/PATH/FAULT 유형에 해당하지 않습니다.\n"
        )


# ---------------------------------------------------------------------------
# CLI 진입점
# ---------------------------------------------------------------------------

def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Track B Opus Reference Context Extractor"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--qids",
        nargs="+",
        type=int,
        metavar="QID",
        help="처리할 질문 번호 (예: --qids 1 11 17)",
    )
    group.add_argument(
        "--all",
        action="store_true",
        help="모든 50개 질문 처리 (pilot 시 사용 자제)",
    )
    parser.add_argument(
        "--print-q01",
        action="store_true",
        help="Q01 context 를 stdout 에도 출력 (품질 확인)",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()

    print("[INFO] test.json 로드 중...")
    test_data = load_test_data()
    print(f"[INFO] test.json 로드 완료: {len(test_data)}개 질문")

    print("[INFO] v12 submission CSV 로드 중...")
    v12_answers = load_v12_answers()
    print(f"[INFO] v12 CSV 로드 완료: {len(v12_answers)}개 답변")

    if args.all:
        qids = sorted(test_data.keys())
        print(f"[INFO] 전체 {len(qids)}개 질문 처리")
    else:
        qids = sorted(args.qids)
        print(f"[INFO] 처리 대상 qid: {qids}")

    _OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for qid in qids:
        print(f"[INFO] Q{qid:02d} context 생성 중...", end=" ", flush=True)
        try:
            context = build_context(qid, test_data, v12_answers)
        except Exception as e:
            print(f"ERROR: {e}")
            continue

        out_path = _OUTPUT_DIR / f"q{qid:02d}_context.md"
        out_path.write_text(context, encoding="utf-8")
        byte_count = out_path.stat().st_size
        print(f"완료 ({byte_count:,} bytes → {out_path.name})")

        if args.print_q01 and qid == 1:
            print("\n" + "=" * 60)
            print("Q01 context 전체 내용:")
            print("=" * 60)
            print(context)
            print("=" * 60 + "\n")

    print("\n[완료] 생성된 파일 목록:")
    for qid in qids:
        p = _OUTPUT_DIR / f"q{qid:02d}_context.md"
        if p.exists():
            print(f"  {p}  ({p.stat().st_size:,} bytes)")

    print(f"\n출력 디렉토리: {_OUTPUT_DIR}")


if __name__ == "__main__":
    main()
