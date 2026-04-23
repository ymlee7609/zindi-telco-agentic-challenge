"""Track B Fault Analyzer — CLI 파일 기반 deterministic 분석.

Q17~Q28 (Traditional) + Q39~Q50 (PJ) 총 24문제 대상.
LLM 호출 없이 routing table / interface brief / LLDP 파일만 사용.
"""

from __future__ import annotations

import ipaddress
import json
import re
from collections import deque
from pathlib import Path
from typing import Optional

from cli_parsers import (
    DEVICES_ROOT,
    find_ip_owner,
    list_devices,
    lookup_longest_prefix,
    parse_interface_brief,
    parse_interface_description,
    parse_ip_interface_brief,
    parse_lldp,
    parse_routing_table,
    qdir,
    read_file,
)

# ---------------------------------------------------------------------------
# Reason enum (agent.py L442-465 과 동일)
# ---------------------------------------------------------------------------
_ROUTING_FAULT_REASONS: frozenset[str] = frozenset({
    "blackhole route",
    "missing static route",
    "static route error",
    "ARP configuration error",
    "routing loop",
    "BGP configuration error",
    "OSPF configuration error",
    "loopback IP configuration conflict",
    "VXLAN configuration error",
    "L3VPN configuration error",
    "L2VPN configuration error",
    "IS-IS configuration error",
    "SRV6-Policy tunnel planning error",
})
_PORT_FAULT_REASONS: frozenset[str] = frozenset({
    "shutdown",
    "interface IP error",
    "traffic congestion on port bandwidth",
    "MAC address configuration error",
    "VPN configuration missing",
    "OSPF configuration error",
    "MTU value configuration error",
})

_PORT_TOKEN_RE = re.compile(
    r"^((?:GE|XGE|10GE|25GE|40GE|100GE|GigabitEthernet|XGigabitEthernet|Ethernet)\d+/\d+/\d+(?:\.\d+)?"
    r"|Eth-Trunk\d+(?:\.\d+)?"
    r"|MEth\d+/\d+/\d+)$"
)
_IPV4_RE = re.compile(r"^\d{1,3}(?:\.\d{1,3}){3}$")


# ---------------------------------------------------------------------------
# BFS 그래프 빌더 (LLDP 기반)
# ---------------------------------------------------------------------------

def build_underlay_graph(qid: int) -> dict[str, set[str]]:
    """LLDP neighbor 정보로 undirected adjacency dict 빌드.

    Stage 3 Path tracer 와 공유 가능한 시그니처.
    """
    graph: dict[str, set[str]] = {}
    for dev in list_devices(qid):
        if dev not in graph:
            graph[dev] = set()
        for nb in parse_lldp(qid, dev):
            graph[dev].add(nb.neighbor_device)
            if nb.neighbor_device not in graph:
                graph[nb.neighbor_device] = set()
            graph[nb.neighbor_device].add(dev)
    return graph


def bfs_shortest_path(graph: dict[str, set[str]], src: str, dst: str) -> list[str]:
    """BFS 로 src → dst 최단 경로 반환. 경로 없으면 빈 리스트.

    Stage 3 Path tracer 와 공유 가능한 시그니처.
    """
    if src not in graph or dst not in graph:
        return []
    if src == dst:
        return [src]
    visited = {src}
    queue: deque[list[str]] = deque([[src]])
    while queue:
        path = queue.popleft()
        node = path[-1]
        for neighbor in graph.get(node, set()):
            if neighbor == dst:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return []


# ---------------------------------------------------------------------------
# 시나리오 텍스트 파싱
# ---------------------------------------------------------------------------

_NODE_RE = re.compile(r"\b([A-Z][a-z]+-[A-Z][a-z]+-\d+)\b")
_IP_RE = re.compile(r"\b(\d+\.\d+\.\d+\.\d+)\b")
_PORT_INLINE_RE = re.compile(r"\b(GE\d+/\d+/\d+|Eth-Trunk\d+|XGE\d+/\d+/\d+|GE\d+/\d+/\d+)\b")
_GE_PORT_RE = re.compile(r"\b(GE\d+/\d+/\d+)\b")


def _extract_scenario_text(question_text: str) -> str:
    """질문에서 예시 이후 실제 시나리오 부분 추출."""
    # 마지막 예시 라인(interface IP error 포함) 이후가 실제 시나리오
    marker = "interface IP error"
    if marker in question_text:
        parts = question_text.split(marker)
        remainder = parts[-1]
        lines = []
        for line in remainder.strip().splitlines():
            l = line.strip()
            if not l:
                continue
            # 예시 패턴 (node;target;reason) 스킵
            if re.match(r"^[\w-]+;[^;]+;[^;]+$", l):
                continue
            if l.startswith("Please ") or l.startswith("For ") or l.startswith("There is"):
                continue
            lines.append(l)
        return " ".join(lines)
    return question_text[-400:]


def extract_fault_scenarios(question_text: str) -> list[dict]:
    """질문에서 개별 fault 시나리오 추출.

    반환: [{"src_node", "dst_ip", "dst_port", "dst_node", "hint", "raw", "suspect_nodes"}]
    """
    scenario_text = _extract_scenario_text(question_text)

    scenarios = []
    # Q17 스타일: "fault is on one of the three nodes: A, B, C"
    suspect_nodes: list[str] = []
    suspect_match = re.search(
        r"fault\s+is\s+on\s+(?:one\s+of\s+)?(?:the\s+)?(?:\w+\s+)?nodes?[:\s]+([^\n.]+)",
        question_text, re.IGNORECASE,
    )
    if suspect_match:
        suspect_nodes = _NODE_RE.findall(suspect_match.group(1))

    # ping X.X.X.X from Node (PJ)
    ping_match = re.search(r"ping\s+(\d+\.\d+\.\d+\.\d+)\s+from\s+([A-Z][a-z]+-[A-Z][a-z]+-\d+)", scenario_text)
    if ping_match:
        scenarios.append({
            "src_node": ping_match.group(2),
            "dst_ip": ping_match.group(1),
            "dst_port": None,
            "dst_node": None,
            "hint": "ping",
            "raw": scenario_text,
            "suspect_nodes": suspect_nodes,
        })
        return scenarios

    # Node pings ... (PJ 변형)
    ping_match2 = re.search(
        r"([A-Z][a-z]+-[A-Z][a-z]+-\d+)\s+pings?\s+.*?(\d+\.\d+\.\d+\.\d+)",
        scenario_text,
    )
    if ping_match2:
        scenarios.append({
            "src_node": ping_match2.group(1),
            "dst_ip": ping_match2.group(2),
            "dst_port": None,
            "dst_node": None,
            "hint": "ping",
            "raw": scenario_text,
            "suspect_nodes": suspect_nodes,
        })
        return scenarios

    # MAC address conflict (Q42 스타일)
    mac_match = re.search(r"([A-Z][a-z]+-[A-Z][a-z]+-\d+)\s+received\s+a\s+MAC\s+address\s+conflict", scenario_text)
    if mac_match:
        scenarios.append({
            "src_node": mac_match.group(1),
            "dst_ip": None,
            "dst_port": None,
            "dst_node": None,
            "hint": "MAC conflict",
            "raw": scenario_text,
            "suspect_nodes": suspect_nodes,
        })
        return scenarios

    # Traditional: "Node addressing GE*/IP of RemoteNode"
    # "Beta-Node-01 is addressing GE1/0/2 of Gamma-Node-01"
    trad_match = re.search(
        r"([A-Z][a-z]+-[A-Z][a-z]+-\d+)\s+is\s+addressing\s+"
        r"(?:the\s+)?(GE\d+/\d+/\d+|XGE\d+/\d+/\d+)\s+(?:port\s+)?of\s+([A-Z][a-z]+-[A-Z][a-z]+-\d+)",
        scenario_text,
    )
    if trad_match:
        src = trad_match.group(1)
        port = trad_match.group(2)
        dst_node = trad_match.group(3)
        # dst_ip 는 dst_node 의 해당 port IP
        scenarios.append({
            "src_node": src,
            "dst_ip": None,  # 나중에 resolve
            "dst_port": port,
            "dst_node": dst_node,
            "hint": "addressing_port",
            "raw": scenario_text,
            "suspect_nodes": suspect_nodes,
        })
        return scenarios

    # "addressing IP:X.X.X.X" or "addressing X.X.X.X"
    trad_ip_match = re.search(
        r"([A-Z][a-z]+-[A-Z][a-z]+-\d+)\s+is\s+addressing\s+.*?(\d+\.\d+\.\d+\.\d+)",
        scenario_text,
    )
    if trad_ip_match:
        scenarios.append({
            "src_node": trad_ip_match.group(1),
            "dst_ip": trad_ip_match.group(2),
            "dst_port": None,
            "dst_node": None,
            "hint": "addressing_ip",
            "raw": scenario_text,
            "suspect_nodes": suspect_nodes,
        })
        return scenarios

    # 폴백: IP 와 node 만 추출
    nodes = _NODE_RE.findall(scenario_text)
    ips = _IP_RE.findall(scenario_text)
    if nodes or ips:
        scenarios.append({
            "src_node": nodes[0] if nodes else None,
            "dst_ip": ips[0] if ips else None,
            "dst_port": None,
            "dst_node": nodes[1] if len(nodes) > 1 else None,
            "hint": "fallback",
            "raw": scenario_text,
            "suspect_nodes": suspect_nodes,
        })
    return scenarios


# ---------------------------------------------------------------------------
# 포트 fault 탐지
# ---------------------------------------------------------------------------

def detect_port_fault(
    qid: int, node: str, port: str
) -> tuple[str, str, str, str] | None:
    """포트 상태 기반 port fault 탐지.

    반환: (node, port, reason, confidence H/M/L) or None
    """
    ifaces = {i.name: i for i in parse_interface_brief(qid, node)}
    iface = ifaces.get(port)
    if iface is None:
        return None

    # phy=*down (admin down) → shutdown
    if "*down" in iface.phy.lower():
        return (node, port, "shutdown", "H")

    # phy=down (link down, not admin) but protocol also down → shutdown or physical
    if iface.phy.lower() in ("down", "^down"):
        # description 에서 shutdown 명시 확인
        descs = parse_interface_description(qid, node)
        desc = descs.get(port, "")
        if "shutdown" in desc.lower():
            return (node, port, "shutdown", "H")
        return (node, port, "shutdown", "M")

    # protocol=down 이지만 phy=up → interface IP error
    if iface.phy.lower() == "up" and iface.protocol.lower() == "down":
        return (node, port, "interface IP error", "M")

    return None


# ---------------------------------------------------------------------------
# Routing fault 탐지 (경로 추적)
# ---------------------------------------------------------------------------

def _check_arp_reachability(qid: int, node: str, dst_ip: str) -> bool:
    """ARP table 에서 dst_ip 항목 존재 여부 확인 (Direct route 검증용)."""
    text = read_file(qid, node, "display_arp.txt")
    for line in text.splitlines():
        if dst_ip in line:
            return True
    return False


def _nexthop_chain(
    qid: int, src: str, dst_ip: str, max_hops: int = 20
) -> list[str]:
    """실제 라우팅 nexthop 체인 추적으로 경로 도출.

    각 hop 에서 lookup_longest_prefix 로 nexthop 을 구하고,
    nexthop IP 의 소유 device 로 이동하여 경로 반환.
    루프 감지 (visited 중복) 시 중단.
    """
    devices = set(list_devices(qid))
    path = [src]
    visited = {src}

    for _ in range(max_hops):
        current = path[-1]
        if current not in devices:
            break
        route = lookup_longest_prefix(qid, current, dst_ip)
        if route is None:
            break
        if route.nexthop in ("127.0.0.1", "0.0.0.0"):
            break
        # nexthop device 찾기
        nexthop_owners = find_ip_owner(qid, route.nexthop)
        if not nexthop_owners:
            break
        next_dev = nexthop_owners[0]
        if next_dev in visited:
            break  # 루프
        path.append(next_dev)
        visited.add(next_dev)
        # 목적지 도달 확인
        dst_route = lookup_longest_prefix(qid, next_dev, dst_ip)
        if dst_route and dst_route.nexthop == "127.0.0.1":
            break
    return path


def detect_routing_fault(
    qid: int, src: str, dst_ip: str, suspect_nodes: list[str] | None = None
) -> list[tuple[str, str, str, str]]:
    """Nexthop 체인 추적 + 라우팅 테이블 분석으로 routing fault 탐지.

    suspect_nodes 없으면: nexthop chain 으로 실제 경로 추적, 경로상 첫 fault 반환.
    suspect_nodes 있으면: 해당 노드만 점검.

    반환: [(node, dst_ip, reason, confidence), ...]
    """
    # @MX:ANCHOR: [AUTO] detect_routing_fault — nexthop chain 기반 fault 탐지
    # @MX:REASON: [AUTO] 복수 caller (analyze_single_fault, solve_fault) + 핵심 로직
    results: list[tuple[str, str, str, str]] = []
    devices = set(list_devices(qid))

    # suspect_nodes 가 있으면 해당 노드만 점검
    if suspect_nodes:
        for node in suspect_nodes:
            if node not in devices:
                continue
            route = lookup_longest_prefix(qid, node, dst_ip)
            if route is None:
                results.append((node, dst_ip, "missing static route", "H"))
            elif "NULL" in route.egress_if:
                results.append((node, dst_ip, "blackhole route", "H"))
            else:
                nexthop_owners = find_ip_owner(qid, route.nexthop)
                if not nexthop_owners and route.nexthop not in ("0.0.0.0", "127.0.0.1"):
                    results.append((node, dst_ip, "static route error", "M"))
        return results

    # nexthop chain 으로 실제 경로 추적
    chain = _nexthop_chain(qid, src, dst_ip)

    for node in chain:
        if node not in devices:
            continue
        route = lookup_longest_prefix(qid, node, dst_ip)
        if route is None:
            results.append((node, dst_ip, "missing static route", "H"))
            return results

        # NULL interface → blackhole
        if "NULL" in route.egress_if:
            results.append((node, dst_ip, "blackhole route", "H"))
            return results

        # nexthop IP 소유자 없음 → static route error
        if route.nexthop not in ("0.0.0.0", "127.0.0.1"):
            nexthop_owners = find_ip_owner(qid, route.nexthop)
            if not nexthop_owners:
                results.append((node, dst_ip, "static route error", "H"))
                return results

        # egress interface down → port fault 경로, 계속
        ifaces = {i.name: i for i in parse_interface_brief(qid, node)}
        egress = ifaces.get(route.egress_if)
        if egress and not egress.is_up:
            continue

    return results


# ---------------------------------------------------------------------------
# 단일 시나리오 분석
# ---------------------------------------------------------------------------

def analyze_single_fault(
    qid: int, scenario: dict
) -> tuple[str, str, str, str] | None:
    """단일 시나리오 분석.

    반환: (node, target, reason, confidence H/M/L) or None
    """
    src = scenario.get("src_node")
    dst_ip = scenario.get("dst_ip")
    dst_port = scenario.get("dst_port")
    dst_node = scenario.get("dst_node")
    hint = scenario.get("hint", "")
    suspects = scenario.get("suspect_nodes", [])

    # MAC address conflict → reason 고정, 포트는 VLAN trunk(sub-interface 다수) 또는 PC 연결 우선
    # @MX:NOTE: [AUTO] MAC conflict 는 VLAN trunk 의 MAC 설정 문제가 전형적
    if hint == "MAC conflict" and src:
        ifaces = parse_interface_brief(qid, src)
        desc = parse_interface_description(qid, src)
        desc_names = set(desc.keys())

        # 1순위: UP + sub-interface 2개 이상 (VLAN trunk, MAC 설정 문제 최적)
        for i in ifaces:
            if (
                i.is_up
                and i.name.startswith(("GE", "XGE"))
                and _PORT_TOKEN_RE.match(i.name)
            ):
                sub_count = sum(1 for n in desc_names if n.startswith(i.name + "."))
                if sub_count >= 2:
                    return (src, i.name, "MAC address configuration error", "H")

        # 2순위: UP + description 에 host/PC/Server 연결 흔적
        for i in ifaces:
            if (
                i.is_up
                and i.name.startswith(("GE", "XGE"))
                and _PORT_TOKEN_RE.match(i.name)
            ):
                d = desc.get(i.name, "")
                if any(kw in d for kw in ("PC", "Server", "server", "Host", "host")):
                    return (src, i.name, "MAC address configuration error", "H")

        # 3순위: DOWN GE 포트 (link down by MAC conflict)
        for i in ifaces:
            if not i.is_up and i.name.startswith(("GE", "XGE")) and _PORT_TOKEN_RE.match(i.name):
                return (src, i.name, "MAC address configuration error", "M")

        # 4순위: UP GE 첫 포트 fallback
        for i in ifaces:
            if i.is_up and i.name.startswith("GE") and _PORT_TOKEN_RE.match(i.name):
                return (src, i.name, "MAC address configuration error", "L")
        return (src, "GE1/0/5", "MAC address configuration error", "L")

    # dst_port 가 지정된 경우 → dst_node 의 해당 port IP 가져오기
    if dst_port and dst_node and not dst_ip:
        ips = parse_ip_interface_brief(qid, dst_node)
        dst_ip_with_mask = ips.get(dst_port)
        if dst_ip_with_mask:
            dst_ip = dst_ip_with_mask.split("/")[0]  # 마스크 제거

    if not dst_ip:
        return None

    # suspect nodes 가 지정된 경우: routing fault 우선, 없으면 port fault
    if suspects:
        routing_faults = detect_routing_fault(qid, src or "", dst_ip, suspect_nodes=suspects)
        if routing_faults:
            return routing_faults[0]

        # port fault 점검 (egress interface 기준)
        for node in suspects:
            ifaces_dict = {i.name: i for i in parse_interface_brief(qid, node)}
            route = lookup_longest_prefix(qid, node, dst_ip)
            if route:
                egress = ifaces_dict.get(route.egress_if)
                if egress and not egress.is_up:
                    result = detect_port_fault(qid, node, route.egress_if)
                    if result:
                        return result
            # egress 없어도 DOWN GE port 확인
            for iface in parse_interface_brief(qid, node):
                if _PORT_TOKEN_RE.match(iface.name) and not iface.is_up:
                    result = detect_port_fault(qid, node, iface.name)
                    if result:
                        return result
        return None

    # src 에서 경로 추적 (nexthop chain)
    if src:
        # 1. 목적지 IP 가 직접 연결 interface 인지 확인 → port fault
        dst_owners = find_ip_owner(qid, dst_ip)
        for dst_owner in dst_owners:
            ips = parse_ip_interface_brief(qid, dst_owner)
            for port, ip_mask in ips.items():
                if ip_mask.split("/")[0] == dst_ip:
                    # 목적지 interface 자체가 DOWN?
                    result = detect_port_fault(qid, dst_owner, port)
                    if result:
                        return result

        # 2. nexthop chain 경로 routing fault 확인
        routing_faults = detect_routing_fault(qid, src, dst_ip)
        if routing_faults:
            return routing_faults[0]

        # 3. nexthop chain 경로상 egress port fault 확인
        chain = _nexthop_chain(qid, src, dst_ip)
        devices_set = set(list_devices(qid))
        for node in chain:
            if node not in devices_set:
                continue
            route = lookup_longest_prefix(qid, node, dst_ip)
            if route:
                ifaces_dict = {i.name: i for i in parse_interface_brief(qid, node)}
                egress = ifaces_dict.get(route.egress_if)
                if egress and not egress.is_up:
                    result = detect_port_fault(qid, node, route.egress_if)
                    if result:
                        return result

    return None


# ---------------------------------------------------------------------------
# 메인 solver
# ---------------------------------------------------------------------------

def solve_fault(qid: int, question_text: str) -> tuple[str, str]:
    """Fault 문제 풀이.

    반환: (답변 문자열 (여러 줄), 평균 확신도 H/M/L)
    """
    scenarios = extract_fault_scenarios(question_text)
    if not scenarios:
        return ("", "L")

    answer_lines: list[str] = []
    confidences: list[str] = []

    for sc in scenarios:
        result = analyze_single_fault(qid, sc)
        if result:
            node, target, reason, conf = result
            answer_lines.append(f"{node};{target};{reason}")
            confidences.append(conf)

    if not answer_lines:
        return ("", "L")

    # confidence 집계: H > M > L
    conf_rank = {"H": 2, "M": 1, "L": 0}
    avg = sum(conf_rank.get(c, 0) for c in confidences) / len(confidences)
    avg_conf = "H" if avg >= 1.5 else ("M" if avg >= 0.5 else "L")

    return ("\n".join(answer_lines), avg_conf)


def solve_all_faults() -> dict[int, dict]:
    """Q17~Q28, Q39~Q50 전체 풀이.

    반환: {qid: {"answer": str, "confidence": str, "scenarios": int}}
    """
    # test.json 로드
    test_json = Path(__file__).resolve().parent.parent.parent / "data" / "Track B" / "data" / "Phase_1" / "test.json"
    with test_json.open() as f:
        data = json.load(f)

    fault_ids = set(range(17, 29)) | set(range(39, 51))
    results: dict[int, dict] = {}

    for item in data:
        qid = item["task"]["id"]
        if qid not in fault_ids:
            continue
        q_text = item["task"]["question"]
        scenarios = extract_fault_scenarios(q_text)
        answer, conf = solve_fault(qid, q_text)
        results[qid] = {
            "scenario_id": item["scenario_id"],
            "answer": answer,
            "confidence": conf,
            "scenarios": len(scenarios),
            "question": q_text[-200:],
        }

    return results


# ---------------------------------------------------------------------------
# Smoke test
# ---------------------------------------------------------------------------

def _smoke_test() -> None:
    """Q17 (복수 fault) + Q39 (단일 fault) smoke test."""
    import json as _json

    test_json = Path(__file__).resolve().parent.parent.parent / "data" / "Track B" / "data" / "Phase_1" / "test.json"
    with test_json.open() as f:
        data = _json.load(f)

    questions = {item["task"]["id"]: item["task"]["question"] for item in data}

    print("=" * 60)
    print("Q17 smoke test")
    print("=" * 60)
    q17 = questions[17]
    scenarios_17 = extract_fault_scenarios(q17)
    print(f"Scenarios detected: {len(scenarios_17)}")
    for sc in scenarios_17:
        print(f"  src={sc['src_node']}, dst_ip={sc['dst_ip']}, suspects={sc['suspect_nodes']}")

    ans17, conf17 = solve_fault(17, q17)
    print(f"Answer (conf={conf17}):\n{ans17}")

    print()
    print("=" * 60)
    print("Q39 smoke test")
    print("=" * 60)
    q39 = questions[39]
    scenarios_39 = extract_fault_scenarios(q39)
    print(f"Scenarios detected: {len(scenarios_39)}")
    for sc in scenarios_39:
        print(f"  src={sc['src_node']}, dst_ip={sc['dst_ip']}")

    ans39, conf39 = solve_fault(39, q39)
    print(f"Answer (conf={conf39}):\n{ans39}")

    print()
    print("=" * 60)
    print("전체 요약 (Q17~Q28, Q39~Q50)")
    print("=" * 60)
    all_results = solve_all_faults()
    h_count = sum(1 for r in all_results.values() if r["confidence"] == "H")
    m_count = sum(1 for r in all_results.values() if r["confidence"] == "M")
    l_count = sum(1 for r in all_results.values() if r["confidence"] == "L")
    empty_count = sum(1 for r in all_results.values() if not r["answer"])
    print(f"H/M/L 분포: H={h_count}, M={m_count}, L={l_count}")
    print(f"Deterministic 해결: {len(all_results) - empty_count}/{len(all_results)}")
    print(f"LLM fallback 필요: {empty_count}")
    print()
    for qid in sorted(all_results.keys()):
        r = all_results[qid]
        print(f"  Q{qid} [{r['confidence']}]: {r['answer'] or '(empty)'}")


if __name__ == "__main__":
    _smoke_test()
