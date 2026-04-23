"""Track B Path 경로 추적기 (Q7~Q16, Q34~Q38).

cli_parsers.py 의 공용 함수를 활용해 deterministic 경로를 생성한다.
LLM 추론 없이 LLDP BFS + routing hop-by-hop 방식.

답변 포맷: NodeA->NodeB->...->NodeZ (한 줄, 공백 없음, -> 구분)
"""

from __future__ import annotations

import json
import re
from collections import deque
from pathlib import Path

from cli_parsers import (
    find_ip_owner,
    list_devices,
    lookup_longest_prefix,
    parse_ip_interface_brief,
    parse_lldp,
    reverse_description_lookup,
)


def _resolve_interface_ip(qid: int, device: str, interface: str) -> str | None:
    """device 의 특정 interface 에 할당된 IP 주소 조회 (mask 제외)."""
    ip_map = parse_ip_interface_brief(qid, device)
    ip_full = ip_map.get(interface)
    if not ip_full:
        return None
    return ip_full.split("/", 1)[0]

# 프로젝트 루트 (path_tracer.py 기준 상위 3단계)
_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Q7~Q16: Traditional zone (qid 직접 매핑)
# Q34~Q38: PJ/PJGFA zone (qid 직접 매핑)
_PATH_QIDS = list(range(7, 17)) + list(range(34, 39))

# # @MX:ANCHOR: [AUTO] trace_path 는 Q7~Q38 모든 경로 질문의 진입점 (fan_in=외부 호출다수)
# # @MX:REASON: gen_v12_path.py, solve_all_paths, smoke test 등 여러 곳에서 호출


# ---------------------------------------------------------------------------
# 1. 질문 파싱
# ---------------------------------------------------------------------------

# Traditional zone node 패턴 (예: Beta-Node-01, Alpha-Center-01)
_NODE_PATTERN = re.compile(
    r'\b([A-Z][a-z]+-[A-Z][a-z]+-\d+|[A-Z][a-z]+-[A-Z][a-z]+-\d{2})\b'
)

# PJ zone node 패턴 (예: Hermes-Prime-01, Atlas-Node-01)
_PJ_NODE_PATTERN = re.compile(
    r'\b([A-Z][a-z]+-(?:Prime|Node|Axis|Aegis|Portal|Center|Edge|Core)-\d+)\b'
)

_IP_PATTERN = re.compile(r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\b')
_IFACE_PATTERN = re.compile(r'\b(GE\d+/\d+/\d+|GigabitEthernet\d+/\d+/\d+)\b')


def extract_path_info(question_text: str) -> dict:
    """Path 문제에서 src/dst 노드, dst IP, dst port 추출.

    반환:
        {
            "src_node": str,
            "dst_node": str | None,
            "dst_ip": str | None,
            "dst_port": str | None,
        }
    """
    info: dict = {
        "src_node": "",
        "dst_node": None,
        "dst_ip": None,
        "dst_port": None,
    }

    # 노드 이름 추출 (Traditional + PJ 패턴 통합)
    nodes_trad = _NODE_PATTERN.findall(question_text)
    nodes_pj = _PJ_NODE_PATTERN.findall(question_text)

    # 두 패턴을 합치되 중복 제거, 출현 순서 유지
    seen: set[str] = set()
    nodes: list[str] = []
    for n in nodes_trad + nodes_pj:
        if n not in seen:
            seen.add(n)
            nodes.append(n)

    if nodes:
        info["src_node"] = nodes[0]
    if len(nodes) >= 2:
        info["dst_node"] = nodes[1]

    # "path from X" 또는 "addressed from X" 패턴에서 명시적 src 추출
    # 예: "Delta-Node-03 ... addressed from Beta-Node-03" -> src = Beta-Node-03
    from_match = re.search(
        r'(?:path\s+from|addressed\s+from)\s+([A-Z][a-z]+-[A-Z][a-z]+-\d+)',
        question_text,
    )
    if from_match:
        explicit_src = from_match.group(1)
        if explicit_src in nodes and explicit_src != info["src_node"]:
            # src/dst 교체
            info["dst_node"] = info["src_node"]
            info["src_node"] = explicit_src

    # 인터페이스 추출
    iface_match = _IFACE_PATTERN.search(question_text)
    if iface_match:
        info["dst_port"] = iface_match.group(1)

    # IP 추출: "addressing X.X.X.X" 패턴 우선, 그 다음 "IP:X.X.X.X" 패턴
    addr_match = re.search(r'addressing\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', question_text)
    if addr_match:
        info["dst_ip"] = addr_match.group(1)
    else:
        ip_ctx = re.search(r'(?:IP[:\s]+|address\s+)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', question_text)
        if ip_ctx:
            info["dst_ip"] = ip_ctx.group(1)
        else:
            ip_any = _IP_PATTERN.search(question_text)
            if ip_any:
                info["dst_ip"] = ip_any.group(1)

    # "{Node}'s {Interface}" 패턴 (예: "Delta-Node-01's GE1/0/2")
    # dst_ip 가 아직 없으면 해당 interface 의 IP 를 조회
    ns_match = re.search(
        r"([A-Z][A-Za-z]+-[A-Za-z]+-\d+)(?:'s|\s+)+"
        r"((?:GE|XGE|10GE|25GE|40GE|100GE)\d+/\d+/\d+)",
        question_text,
    )
    if ns_match:
        info.setdefault("dst_node", ns_match.group(1))
        info.setdefault("dst_port", ns_match.group(2))

    return info


# ---------------------------------------------------------------------------
# 2. Underlay 그래프 구성 (LLDP + description 역추적)
# ---------------------------------------------------------------------------

# # @MX:ANCHOR: [AUTO] build_underlay_graph는 BFS 의 핵심 adjacency 소스
# # @MX:REASON: bfs_shortest_path, trace_path 에서 공통 사용

def build_underlay_graph(qid: int) -> dict[str, set[str]]:
    """전체 device LLDP + description 역추적 기반 양방향 adjacency.

    반환: dict[device_name, set[neighbor_name]]
    """
    graph: dict[str, set[str]] = {}
    devices = list_devices(qid)

    # 모든 device 초기화
    for dev in devices:
        graph[dev] = set()

    # LLDP 직접 인접
    for dev in devices:
        for nb in parse_lldp(qid, dev):
            peer = nb.neighbor_device
            if peer in graph:
                graph[dev].add(peer)
                graph[peer].add(dev)
            # peer 가 list_devices 에 없는 경우도 허용 (데이터 불일치 방어)
            else:
                graph.setdefault(peer, set())
                graph[dev].add(peer)
                graph[peer].add(dev)

    # description 역추적 fallback (LLDP 비어있는 장비 보완)
    for dev in devices:
        for (src_dev, _src_port, _tgt_port) in reverse_description_lookup(qid, dev):
            graph[dev].add(src_dev)
            graph.setdefault(src_dev, set()).add(dev)

    return graph


# ---------------------------------------------------------------------------
# 3. BFS 최단 경로
# ---------------------------------------------------------------------------

def bfs_shortest_path(
    graph: dict[str, set[str]],
    src: str,
    dst: str,
    forbidden: set[str] | None = None,
    max_depth: int = 15,
) -> list[str]:
    """BFS 최단 경로 (nodes 리스트, 양 끝 포함).

    Args:
        graph: build_underlay_graph 결과
        src: 출발 device 이름
        dst: 도착 device 이름
        forbidden: 경유 금지 장비 집합 (Q15 등 특정 노드 제외)
        max_depth: 최대 hop 수 (기본 15)

    Returns:
        경로 리스트. 경로 없으면 [].
    """
    if not src or not dst:
        return []
    if src == dst:
        return [src]

    forbidden = forbidden or set()
    visited: set[str] = {src} | forbidden
    queue: deque[tuple[str, list[str]]] = deque([(src, [src])])

    while queue:
        node, path = queue.popleft()
        if len(path) > max_depth:
            continue
        for nb in sorted(graph.get(node, [])):  # sorted: deterministic
            if nb not in visited:
                new_path = path + [nb]
                if nb == dst:
                    return new_path
                visited.add(nb)
                queue.append((nb, new_path))

    return []


# ---------------------------------------------------------------------------
# 4. Routing hop-by-hop 경로 (fallback)
# ---------------------------------------------------------------------------

def _routing_hop_by_hop(
    qid: int,
    graph: dict[str, set[str]],
    src: str,
    dst_ip: str,
    dst_node: str,
    max_hops: int = 12,
) -> list[str]:
    """routing table 기반 hop-by-hop 경로 추적.

    각 노드에서 lookup_longest_prefix 로 egress interface 를 찾고,
    LLDP 그래프에서 해당 인터페이스의 neighbor 를 다음 홉으로 사용.
    """
    # 각 device 의 LLDP 정보를 포트 기준으로 미리 구축
    port_to_neighbor: dict[str, dict[str, str]] = {}
    for dev in list_devices(qid):
        port_to_neighbor[dev] = {}
        for nb in parse_lldp(qid, dev):
            port_to_neighbor[dev][nb.local_if] = nb.neighbor_device

    hops = [src]
    cur = src
    visited_set = {src}

    for _ in range(max_hops):
        if cur == dst_node:
            break

        route = lookup_longest_prefix(qid, cur, dst_ip)
        if not route:
            break

        egress_if = route.egress_if
        # 직결 인터페이스 (Direct 경로) -> 목적지가 현재 노드에 있음
        if route.proto == "Direct" and route.nexthop.startswith("127."):
            hops.append(dst_node)
            break

        # egress 인터페이스로 연결된 neighbor 탐색
        next_dev = port_to_neighbor.get(cur, {}).get(egress_if)
        if not next_dev:
            # Vlanif 등 L3 SVI 인터페이스: nexthop IP 의 소유자를 next hop 으로
            nexthop_owners = find_ip_owner(qid, route.nexthop)
            next_dev = nexthop_owners[0] if nexthop_owners else None

        if not next_dev or next_dev in visited_set:
            break

        hops.append(next_dev)
        visited_set.add(next_dev)
        cur = next_dev

    return hops if hops[-1] == dst_node else hops


# ---------------------------------------------------------------------------
# 5. 질문에서 금지 노드 파싱 (Q11, Q15 등 "X node cannot find routing")
# ---------------------------------------------------------------------------

def _extract_forbidden_nodes(question_text: str, all_devices: list[str]) -> set[str]:
    """질문 텍스트에서 사용 금지 노드 추출.

    "X node cannot find routing information" 또는
    "X route is not reachable" 패턴 처리.
    """
    forbidden: set[str] = set()
    # "X node cannot find routing" 패턴
    for m in re.finditer(
        r'([\w\-]+-[\w\-]+-\d+)\s+node\s+cannot\s+find\s+routing', question_text
    ):
        node = m.group(1)
        if node in all_devices:
            forbidden.add(node)
    # "X route is not reachable" 패턴
    for m in re.finditer(
        r'([\w\-]+-[\w\-]+-\d+)\s+route\s+is\s+not\s+reachable', question_text
    ):
        node = m.group(1)
        if node in all_devices:
            forbidden.add(node)
    return forbidden


# ---------------------------------------------------------------------------
# 6. trace_path 메인 함수
# ---------------------------------------------------------------------------

# # @MX:ANCHOR: [AUTO] trace_path: 경로 문제 핵심 진입점
# # @MX:REASON: solve_all_paths 와 gen_v12_path.py 에서 공통 호출

def trace_path(qid: int, question_text: str) -> tuple[str, str]:
    """경로 추적 메인 함수.

    Args:
        qid: 질문 ID (1~50)
        question_text: 원문 질문 텍스트

    Returns:
        (답변 문자열, 확신도 "H"/"M"/"L")
        답변 형식: "NodeA->NodeB->...->NodeZ"
    """
    all_devices = list_devices(qid)
    if not all_devices:
        return ("", "L")

    info = extract_path_info(question_text)
    src = info["src_node"]
    dst_ip = info["dst_ip"]
    dst_node = info["dst_node"]

    # src 가 실존 device 인지 확인
    if src not in all_devices:
        return ("", "L")

    # dst_ip 로 dst_node 확정
    if dst_ip:
        owners = find_ip_owner(qid, dst_ip)
        if owners:
            dst_node = owners[0]

    if not dst_node or dst_node not in all_devices:
        return ("", "L")

    # 동일 장비
    if src == dst_node:
        return (src, "H")

    # 금지 노드 추출 (Q11, Q15 등)
    forbidden = _extract_forbidden_nodes(question_text, all_devices)

    # 경유 노드(waypoint) 추출 (Q12 등 "passes through X node")
    wp_match = re.search(
        r'passes\s+through\s+(?:the\s+)?([\w\-]+-[\w\-]+-\d+)\s+node',
        question_text,
    )
    waypoint = wp_match.group(1) if wp_match and wp_match.group(1) in all_devices else None

    # underlay BFS
    graph = build_underlay_graph(qid)

    if waypoint:
        # waypoint BFS: src -> waypoint -> dst
        p1 = bfs_shortest_path(graph, src, waypoint, forbidden=forbidden)
        p2 = bfs_shortest_path(graph, waypoint, dst_node, forbidden=forbidden)
        path = (p1 + p2[1:]) if (p1 and p2) else []
    else:
        path = bfs_shortest_path(graph, src, dst_node, forbidden=forbidden)

    if path and path[-1] == dst_node:
        conf = "H"
    else:
        # routing hop-by-hop fallback (dst_ip 있을 때만)
        if dst_ip:
            path = _routing_hop_by_hop(qid, graph, src, dst_ip, dst_node)
        conf = "M" if (path and path[-1] == dst_node) else "L"

    if not path:
        return ("", "L")

    # 환각 방지: 모든 hop 이 실존 device 인지 검증
    valid_set = set(all_devices)
    path = [h for h in path if h in valid_set]

    if not path:
        return ("", "L")

    answer = "->".join(path)
    return (answer, conf)


# ---------------------------------------------------------------------------
# 7. 전체 Path Q 순회
# ---------------------------------------------------------------------------

# # @MX:NOTE: [AUTO] trace_path_by_routing 은 BFS 역효과 확인 후 추가된 대체 경로
# # Zindi 실측: BFS 기반 trace_path 는 0.12 점수 기여 (역효과), routing-table 우선은 0.36 복구 목표

def trace_path_by_routing(qid: int, question_text: str) -> tuple[str, str]:
    """routing-table hop-by-hop 우선, BFS 는 최후 fallback.

    이유: BFS 최단경로는 alphabetical 정렬로 -01 장비 선호하지만,
    실제 라우팅은 routing-table 의 nexthop IP 가 결정한다.
    """
    all_devices = list_devices(qid)
    if not all_devices:
        return ("", "L")

    info = extract_path_info(question_text)
    src = info["src_node"]
    dst_ip = info["dst_ip"]
    dst_node = info["dst_node"]

    if src not in all_devices:
        return ("", "L")

    if dst_ip:
        owners = find_ip_owner(qid, dst_ip)
        if owners:
            dst_node = owners[0]

    # dst_ip 가 비어있지만 dst_node + dst_port 있으면 interface IP 조회
    if not dst_ip and dst_node and info.get("dst_port"):
        resolved = _resolve_interface_ip(qid, dst_node, info["dst_port"])
        if resolved:
            dst_ip = resolved
            info["dst_ip"] = resolved

    if not dst_node or dst_node not in all_devices:
        return ("", "L")

    if src == dst_node:
        return (src, "H")

    graph = build_underlay_graph(qid)

    # 1순위: routing-table hop-by-hop
    if dst_ip:
        routing_path = _routing_hop_by_hop(qid, graph, src, dst_ip, dst_node)
        if routing_path and routing_path[-1] == dst_node and len(routing_path) >= 2:
            valid = set(all_devices)
            routing_path = [h for h in routing_path if h in valid]
            if routing_path and routing_path[0] == src and routing_path[-1] == dst_node:
                return ("->".join(routing_path), "H")

    # 2순위: 금지/waypoint 반영 BFS (routing trace 실패 시에만)
    forbidden = _extract_forbidden_nodes(question_text, all_devices)
    wp_match = re.search(
        r'passes\s+through\s+(?:the\s+)?([\w\-]+-[\w\-]+-\d+)\s+node',
        question_text,
    )
    waypoint = wp_match.group(1) if wp_match and wp_match.group(1) in all_devices else None

    if waypoint:
        p1 = bfs_shortest_path(graph, src, waypoint, forbidden=forbidden)
        p2 = bfs_shortest_path(graph, waypoint, dst_node, forbidden=forbidden)
        path = (p1 + p2[1:]) if (p1 and p2) else []
    else:
        path = bfs_shortest_path(graph, src, dst_node, forbidden=forbidden)

    valid = set(all_devices)
    path = [h for h in path if h in valid]

    if path and path[0] == src and path[-1] == dst_node:
        return ("->".join(path), "M")
    return ("", "L")


def solve_all_paths_by_routing() -> dict[int, dict]:
    """routing-table 우선 경로 결과. BFS 버전과 분리 유지 (제출 비교용)."""
    test_file = _PROJECT_ROOT / "data" / "Track B" / "data" / "Phase_1" / "test.json"
    with test_file.open(encoding="utf-8") as f:
        test_data = json.load(f)

    qid_to_question: dict[int, str] = {
        item["task"]["id"]: item["task"]["question"]
        for item in test_data
    }

    results: dict[int, dict] = {}
    for qid in _PATH_QIDS:
        q_text = qid_to_question.get(qid, "")
        if not q_text:
            results[qid] = {"answer": "", "confidence": "L"}
            continue
        info = extract_path_info(q_text)
        answer, conf = trace_path_by_routing(qid, q_text)
        results[qid] = {
            "answer": answer,
            "confidence": conf,
            "src": info.get("src_node", ""),
            "dst_ip": info.get("dst_ip", "") or "",
        }
    return results


def solve_all_paths() -> dict[int, dict]:
    """Q7~Q16, Q34~Q38 모두 순회하여 경로 답변 생성.

    Returns:
        {qid: {"answer": str, "confidence": str, "src": str, "dst": str}}
    """
    test_file = _PROJECT_ROOT / "data" / "Track B" / "data" / "Phase_1" / "test.json"
    with test_file.open(encoding="utf-8") as f:
        test_data = json.load(f)

    qid_to_question: dict[int, str] = {
        item["task"]["id"]: item["task"]["question"]
        for item in test_data
    }

    results: dict[int, dict] = {}
    for qid in _PATH_QIDS:
        q_text = qid_to_question.get(qid, "")
        if not q_text:
            results[qid] = {"answer": "", "confidence": "L", "src": "", "dst": ""}
            continue

        info = extract_path_info(q_text)
        answer, conf = trace_path(qid, q_text)
        results[qid] = {
            "answer": answer,
            "confidence": conf,
            "src": info.get("src_node", ""),
            "dst": info.get("dst_node", "") or "",
            "dst_ip": info.get("dst_ip", "") or "",
        }

    return results


# ---------------------------------------------------------------------------
# 8. Smoke test
# ---------------------------------------------------------------------------

def _smoke_test() -> None:
    """Q7, Q34, Q36 세 가지 대표 케이스 smoke test."""
    print("=== Path Tracer Smoke Test ===\n")

    # Q7: Traditional cross-zone
    ans7, conf7 = trace_path(7, (
        "Development-Test zone Beta-Node-01 addressing Big-Data zone "
        "Gamma-Node-01 node's GE1/0/2 (IP:192.168.70.22), the subnet mask of this interface is 30"
    ))
    print(f"Q7  [{conf7}]: {ans7}")
    assert ans7.startswith("Beta-Node-01"), f"Q7 src 오류: {ans7}"
    assert ans7.endswith("Gamma-Node-01"), f"Q7 dst 오류: {ans7}"
    # 환각 방지 확인
    hops7 = ans7.split("->")
    devs7 = list_devices(7)
    for h in hops7:
        assert h in devs7, f"Q7 환각 device: {h}"
    print(f"   hops={len(hops7)}, 환각 0건 OK")

    # Q34: PJ zone, Prime->Prime
    ans34, conf34 = trace_path(34, "PJ area, Hermes-Prime-01 addressing 10.1.1.20 path")
    print(f"Q34 [{conf34}]: {ans34}")
    assert ans34.startswith("Hermes-Prime-01"), f"Q34 src 오류: {ans34}"
    assert ans34.endswith("Hermes-Prime-02"), f"Q34 dst 오류: {ans34}"
    hops34 = ans34.split("->")
    devs34 = list_devices(34)
    for h in hops34:
        assert h in devs34, f"Q34 환각 device: {h}"
    print(f"   hops={len(hops34)}, 환각 0건 OK")

    # Q36: PJGFA zone, Node->Prime cross-zone
    ans36, conf36 = trace_path(36, (
        "PJGFA area, the path from Hermes-Node-01 to address 10.1.1.10"
    ))
    print(f"Q36 [{conf36}]: {ans36}")
    assert ans36.startswith("Hermes-Node-01"), f"Q36 src 오류: {ans36}"
    assert ans36.endswith("Hermes-Prime-01"), f"Q36 dst 오류: {ans36}"
    hops36 = ans36.split("->")
    devs36 = list_devices(36)
    for h in hops36:
        assert h in devs36, f"Q36 환각 device: {h}"
    # "Node-10" 같은 환각 패턴 없음
    assert not any("Node-10" in h or "Spine" in h for h in hops36), \
        f"Q36 환각 패턴 검출: {hops36}"
    print(f"   hops={len(hops36)}, 환각 0건 OK")

    print("\n전체 smoke test 통과")


if __name__ == "__main__":
    _smoke_test()

    print("\n=== 전체 Q7~Q16, Q34~Q38 경로 ===\n")
    results = solve_all_paths()
    for qid in sorted(results.keys()):
        r = results[qid]
        conf = r["confidence"]
        ans = r["answer"]
        print(f"Q{qid:2d} [{conf}]: {ans}")
