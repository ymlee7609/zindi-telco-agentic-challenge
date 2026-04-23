"""PJ zone 17개 scenario (Q23/29-33/34/37/38/39-49) HIGH 승격 자동 검증.

각 scenario 에서 증거 기반 verdict 산출:
- TOPO: target 장비 UP interface IP → /30 peer IP → peer device lookup
        + description + LLDP 역방향 3 중 교차 증거 수집
- PATH: source routing table 에서 dst_ip longest-prefix match chain trace
- FAULT: 정상(PATH 대응) scenario 대비 forward path 장비 routing diff
- Q23 Delta: forward path 의 장비별 192.168.74.60/30 entry 존재 확인

Usage:
    python3 agent/track_b/opus_reference/verify_pj.py
"""
# pyright: reportMissingImports=false

from __future__ import annotations

import ipaddress
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(_REPO_ROOT / "agent" / "track_b"))

from cli_parsers import (  # type: ignore
    Route,
    list_devices,
    parse_interface_brief,
    parse_ip_interface_brief,
    parse_lldp,
    parse_routing_table,
)


# port name 정규화: GigabitEthernet1/0/X <-> GE1/0/X
def _norm_port(p: str) -> str:
    return (
        p.replace("GigabitEthernet", "GE")
         .replace("XGigabitEthernet", "XGE")
         .strip()
    )


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def ip_owner_map(qid: int) -> dict[str, tuple[str, str]]:
    """모든 장비의 IP → (device, port) 매핑."""
    owner: dict[str, tuple[str, str]] = {}
    for dev in list_devices(qid):
        for port, ip in parse_ip_interface_brief(qid, dev).items():
            addr = ip.split("/")[0] if "/" in ip else ip
            owner[addr] = (dev, port)
    return owner


def peer_ip(ip_with_mask: str) -> str | None:
    """ IP/mask 의 /30 /31 peer IP 계산. """
    try:
        net = ipaddress.ip_interface(ip_with_mask).network
        my_ip = ipaddress.ip_interface(ip_with_mask).ip
        for host in net.hosts():
            if host != my_ip:
                return str(host)
    except ValueError:
        return None
    return None


def longest_prefix_match(routes: list[Route], dst_ip: str) -> Route | None:
    """dst_ip 에 대해 longest prefix match 한 Route 반환."""
    try:
        target = ipaddress.ip_address(dst_ip)
    except ValueError:
        return None
    best: Route | None = None
    best_len = -1
    for r in routes:
        try:
            net = ipaddress.ip_network(r.destination, strict=False)
        except ValueError:
            continue
        if target in net and net.prefixlen > best_len:
            best_len = net.prefixlen
            best = r
    return best


def verify_topo(qid: int, target: str, solver_links: list[tuple[str, str, str]]) -> dict:
    """TOPO 검증: target UP interfaces → peer IP → peer device 매핑으로 solver 답 검증.

    solver_links: [(local_port, peer_dev, peer_port), ...]
    """
    ip_ifaces = parse_ip_interface_brief(qid, target)
    up_ifaces = [i for i in parse_interface_brief(qid, target) if i.is_up and "." not in i.name]
    owner = ip_owner_map(qid)

    # LLDP forward
    lldp_map = {_norm_port(nb.local_if): (nb.neighbor_device, _norm_port(nb.neighbor_if))
                for nb in parse_lldp(qid, target)}

    # Reverse LLDP: 전체 장비 스캔, target 을 neighbor 로 하는 것
    reverse_map: dict[str, tuple[str, str]] = {}
    for dev in list_devices(qid):
        if dev == target:
            continue
        for nb in parse_lldp(qid, dev):
            if nb.neighbor_device == target:
                # reverse_map key = target 의 port, value = (peer_dev, peer_port)
                reverse_map[_norm_port(nb.neighbor_if)] = (dev, _norm_port(nb.local_if))

    evidence = []
    hits = 0
    for local_port, claimed_dev, claimed_port in solver_links:
        lp_n, cp_n = _norm_port(local_port), _norm_port(claimed_port)
        srcs = []
        # 1) LLDP forward
        fwd = lldp_map.get(lp_n)
        if fwd and fwd[0] == claimed_dev and fwd[1] == cp_n:
            srcs.append("LLDP-fwd")
        # 2) LLDP reverse
        rev = reverse_map.get(lp_n)
        if rev and rev[0] == claimed_dev and rev[1] == cp_n:
            srcs.append("LLDP-rev")
        # 3) IP /30 peer
        ip = ip_ifaces.get(local_port, "")
        if ip:
            pip = peer_ip(ip)
            if pip and pip in owner:
                p_dev, p_port = owner[pip]
                if p_dev == claimed_dev and p_port == claimed_port:
                    srcs.append(f"IP-peer({pip})")
        if srcs:
            hits += 1
        evidence.append({"local": local_port, "claim": f"{claimed_dev}({claimed_port})",
                         "evidence": srcs or ["NONE"]})

    return {
        "target": target,
        "up_iface_count": len(up_ifaces),
        "solver_link_count": len(solver_links),
        "verified_links": hits,
        "all_verified": hits == len(solver_links) and len(solver_links) > 0,
        "details": evidence,
    }


def parse_solver_topo_answer(answer: str, target: str) -> list[tuple[str, str, str]]:
    """ solver 답을 [(local_port, peer_dev, peer_port), ...] 로 파싱. """
    import re
    result = []
    for line in answer.split("\\n") + answer.splitlines():
        line = line.strip()
        m = re.match(rf"{re.escape(target)}\((\S+?)\)->(\S+?)\((\S+?)\)", line)
        if m:
            result.append((m.group(1), m.group(2), m.group(3)))
    # dedup
    seen = set()
    out = []
    for t in result:
        if t in seen:
            continue
        seen.add(t)
        out.append(t)
    return out


def verify_path(qid: int, src: str, dst_ip: str, solver_path: list[str]) -> dict:
    """PATH 검증: src routing → longest prefix match → next-hop chain."""
    owner = ip_owner_map(qid)
    current = src
    visited = [src]
    evidence = []
    max_hops = 12
    while current and len(visited) < max_hops:
        routes = parse_routing_table(qid, current)
        r = longest_prefix_match(routes, dst_ip)
        if r is None:
            evidence.append(f"{current}: no route for {dst_ip}")
            break
        evidence.append(f"{current}: {r.destination} via {r.nexthop} dev {r.egress_if}")
        # next hop device (owner of r.nexthop)
        if r.nexthop in owner:
            next_dev = owner[r.nexthop][0]
            if next_dev == current:
                # direct
                break
            if next_dev in visited:
                evidence.append(f"LOOP detected: {next_dev} already visited")
                break
            visited.append(next_dev)
            current = next_dev
        else:
            # Direct or unknown next-hop
            evidence.append(f"  (direct or unknown next-hop {r.nexthop})")
            break
    match = (visited == solver_path)
    return {
        "src": src,
        "dst_ip": dst_ip,
        "traced": "->".join(visited),
        "solver": "->".join(solver_path),
        "match": match,
        "evidence": evidence,
    }


def verify_fault_diff(qid: int, normal_qid: int, src: str, dst_ip: str) -> dict:
    """FAULT 검증: 정상 scenario 대비 forward path 장비들의 routing diff."""
    owner = ip_owner_map(qid)

    # 정상 scenario 에서 forward path 구성
    current = src
    visited = [src]
    diffs = []
    max_hops = 8
    while current and len(visited) < max_hops:
        r_normal_list = parse_routing_table(normal_qid, current)
        r_normal = longest_prefix_match(r_normal_list, dst_ip)
        if r_normal is None:
            diffs.append(f"[{current}] 정상 scenario 에도 경로 없음")
            break
        r_fault_list = parse_routing_table(qid, current)
        r_fault = longest_prefix_match(r_fault_list, dst_ip)
        if r_fault is None:
            diffs.append(f"[{current}] 변이: 경로 삭제 (정상: {r_normal.destination} via {r_normal.nexthop})")
            return {"fault_node": current, "reason": "missing static route", "diffs": diffs,
                    "traced": "->".join(visited)}
        if r_normal.nexthop != r_fault.nexthop or r_normal.egress_if != r_fault.egress_if:
            diffs.append(f"[{current}] 변이: next-hop 변경 "
                         f"(정상: {r_normal.nexthop}/{r_normal.egress_if} → "
                         f"변이: {r_fault.nexthop}/{r_fault.egress_if})")
            return {"fault_node": current, "reason": "static route error or routing loop",
                    "diffs": diffs, "traced": "->".join(visited)}

        # 다음 hop 으로
        if r_fault.nexthop in owner:
            next_dev = owner[r_fault.nexthop][0]
            if next_dev == current or next_dev in visited:
                break
            visited.append(next_dev)
            current = next_dev
        else:
            break

    return {"fault_node": "UNCERTAIN", "reason": "no diff detected in traced path",
            "diffs": diffs, "traced": "->".join(visited)}


# ---------------------------------------------------------------------------
# Main verification batch
# ---------------------------------------------------------------------------

def main():
    # TOPO 대상 + solver 답 (baseline CSV 참조)
    import csv
    import json

    with (_REPO_ROOT / "data" / "Track B" / "data" / "Phase_1" / "test.json").open() as f:
        scenarios = json.load(f)
    qid2sid = {s["task"]["id"]: s["scenario_id"] for s in scenarios}

    baseline = {}
    with (_REPO_ROOT / "agent" / "track_b" / "submission" / "submission_v12_topofault_rt.csv").open() as f:
        for r in csv.DictReader(f):
            tb = r.get("Track B", "").strip()
            if tb:
                baseline[r["ID"]] = tb

    # TOPO target 매핑 (q29-33)
    topo_targets = {
        29: "Demeter-Prime-01",
        30: "Atlas-Prime-01",
        31: "Janus-Prime-01",
        32: "Aegis-Prime-01",
        33: "Janus-Node-02",
    }

    print("===== TOPO Q29-33 검증 =====\n")
    for qid, target in topo_targets.items():
        ans = baseline.get(qid2sid[qid], "")
        links = parse_solver_topo_answer(ans, target)
        result = verify_topo(qid, target, links)
        print(f"Q{qid:02d} [{target}]: {result['verified_links']}/{result['solver_link_count']} links verified, "
              f"all_verified={result['all_verified']}, UP_ifaces={result['up_iface_count']}")
        for d in result["details"]:
            srcs = ", ".join(d["evidence"])
            print(f"  {d['local']} -> {d['claim']}: {srcs}")
        print()

    # PATH Q34/37/38
    path_targets = {
        34: ("Hermes-Prime-01", "10.1.1.20"),
        37: ("Hermes-Node-01", "20.1.1.20"),
        38: ("Hermes-Prime-01", "20.1.4.20"),
    }
    print("===== PATH Q34/37/38 검증 =====\n")
    for qid, (src, dst_ip) in path_targets.items():
        ans = baseline.get(qid2sid[qid], "")
        solver_path = ans.split("->") if ans else []
        result = verify_path(qid, src, dst_ip, solver_path)
        print(f"Q{qid:02d}: {src} -> {dst_ip}")
        print(f"  traced: {result['traced']}")
        print(f"  solver: {result['solver']}")
        print(f"  match: {result['match']}")
        for e in result["evidence"][:8]:
            print(f"    {e}")
        print()

    # FAULT PJ: 정상/변이 매칭
    fault_pairs = [
        (39, 35, "Hermes-Prime-01", "20.1.1.10"),
        (40, 35, "Hermes-Prime-01", "10.1.6.3"),  # 임시 매핑, 수정 필요
        (41, 35, "Hermes-Prime-01", "10.1.6.3"),
        (43, 35, "Hermes-Prime-01", "20.1.1.10"),
        (46, 35, "Hermes-Prime-01", "20.1.1.10"),
        (47, 35, "Hermes-Prime-02", "20.1.1.20"),
        (48, 35, "Hermes-Prime-02", "20.1.1.20"),
        (49, 38, "Hermes-Prime-01", "20.1.4.10"),
    ]
    print("===== FAULT Q39-49 (PJ) 검증 =====\n")
    for qid, normal_qid, src, dst in fault_pairs:
        result = verify_fault_diff(qid, normal_qid, src, dst)
        print(f"Q{qid:02d}: {src} -> {dst} (baseline: {baseline.get(qid2sid[qid], '')[:80]})")
        print(f"  fault_node={result['fault_node']}, reason={result['reason']}")
        print(f"  traced: {result['traced']}")
        for d in result["diffs"][:5]:
            print(f"    {d}")
        print()

    # Q23 Delta
    print("===== Q23 Delta zone 검증 =====\n")
    q23_dst = "192.168.74.61"
    for dev in ["Delta-Node-01", "Delta-Axis-01", "Delta-Axis-02",
                "Delta-Portal-01", "Delta-Portal-02"]:
        r = longest_prefix_match(parse_routing_table(23, dev), q23_dst)
        if r:
            print(f"  [{dev}] {r.destination} via {r.nexthop} dev {r.egress_if}")
        else:
            print(f"  [{dev}] NO ROUTE for {q23_dst}")


if __name__ == "__main__":
    main()
