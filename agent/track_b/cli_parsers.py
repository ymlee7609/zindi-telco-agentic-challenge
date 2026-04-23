"""Track B 공용 CLI 출력 파서 유틸.

devices_outputs/{qid}/{device}/display_*.txt 파일들을 regex 로 파싱하여
Topology / Fault / Path 모듈이 공통으로 사용하는 구조화 데이터를 반환한다.

LLM 추론 없이 deterministic. 포맷 차이에 대비해 fallback regex 를 3종까지 구비한다.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import NamedTuple

# 프로젝트 루트 = cli_parsers.py 기준 상위 2단계
#   agent/track_b/cli_parsers.py -> agent/track_b -> agent -> <root>
DEVICES_ROOT = (
    Path(__file__).resolve().parent.parent.parent / "data" / "Track B" / "devices_outputs"
)


class LldpNeighbor(NamedTuple):
    local_if: str
    neighbor_if: str
    neighbor_device: str


class InterfacePhy(NamedTuple):
    name: str
    phy: str  # "up" / "*down" / "^down" / "down"
    protocol: str  # "up" / "down"

    @property
    def is_up(self) -> bool:
        return self.phy.lower() == "up" and self.protocol.lower() == "up"


class Route(NamedTuple):
    destination: str  # "192.168.70.20/30"
    proto: str  # Direct / Static / BGP / OSPF / IS-IS / VXLAN 등
    nexthop: str  # "192.168.70.21"
    egress_if: str  # "GE1/0/2", "InLoopBack0"

    @property
    def prefix_len(self) -> int:
        try:
            return int(self.destination.split("/", 1)[1])
        except (IndexError, ValueError):
            return 0


def qdir(qid: int) -> Path:
    return DEVICES_ROOT / str(qid)


def read_file(qid: int, device: str, filename: str) -> str:
    p = qdir(qid) / device / filename
    if not p.exists():
        return ""
    try:
        return p.read_text(errors="replace")
    except OSError:
        return ""


def list_devices(qid: int) -> list[str]:
    d = qdir(qid)
    if not d.exists():
        return []
    return sorted(p.name for p in d.iterdir() if p.is_dir())


# ---------------------------------------------------------------------------
# LLDP neighbor brief
# ---------------------------------------------------------------------------

# 정규 포맷: "Local IF  Exptime  Neighbor IF  Neighbor Device"
_LLDP_PRIMARY = re.compile(
    r"^\s*(\S+)\s+"   # Local Interface
    r"\d+\s+"          # Exptime
    r"(\S+)\s+"        # Neighbor Interface
    r"(\S+)\s*$"       # Neighbor Device
)

# Fallback (일부 벤더는 Exptime 누락)
_LLDP_FALLBACK_3COL = re.compile(r"^\s*(\S+)\s+(\S+)\s+(\S+)\s*$")

def parse_lldp(qid: int, device: str) -> list[LldpNeighbor]:
    text = read_file(qid, device, "display_lldp_neighbor_brief.txt")
    results: list[LldpNeighbor] = []
    header_seen = False
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        # 헤더 라인
        if "Local Interface" in line and "Neighbor" in line:
            header_seen = True
            continue
        if line.startswith("---") or line.startswith("==="):
            continue
        if line.startswith("display"):
            continue
        if not header_seen:
            continue

        m = _LLDP_PRIMARY.match(raw)
        if not m:
            # Fallback (Exptime 없는 변형)
            m = _LLDP_FALLBACK_3COL.match(raw)
            if not m:
                continue
            local_if, nb_if, nb_dev = m.group(1), m.group(2), m.group(3)
        else:
            local_if, nb_if, nb_dev = m.group(1), m.group(2), m.group(3)

        if nb_dev in ("--", "-", "N/A", ""):
            continue
        if "disabled" in nb_dev.lower():
            continue
        # 숫자만인 경우 (Exptime 오인) 스킵
        if nb_dev.isdigit():
            continue
        results.append(LldpNeighbor(local_if, nb_if, nb_dev))
    return results


def reverse_lldp_lookup(qid: int, target_device: str) -> list[tuple[str, LldpNeighbor]]:
    """주변 device 들의 LLDP 에서 Neighbor Device == target 인 라인 추출.

    Q29~Q33 처럼 타겟 본인의 LLDP 가 비어있는 경우에 사용.
    """
    results: list[tuple[str, LldpNeighbor]] = []
    for dev in list_devices(qid):
        if dev == target_device:
            continue
        for nb in parse_lldp(qid, dev):
            if nb.neighbor_device == target_device:
                results.append((dev, nb))
    return results


# ---------------------------------------------------------------------------
# Interface brief (PHY / Protocol 상태)
# ---------------------------------------------------------------------------

_LEGEND_TOKENS = {
    "PHY:", "*down:", "^down:", "(l):", "(s):", "(b):", "(e):", "(d):",
    "(p):", "(dl):", "(c):", "(sd):", "(ed):", "InUti/OutUti:",
}


def parse_interface_brief(qid: int, device: str) -> list[InterfacePhy]:
    text = read_file(qid, device, "display_interface_brief.txt")
    results: list[InterfacePhy] = []
    header_seen = False
    for raw in text.splitlines():
        s = raw.rstrip()
        if not s.strip():
            continue
        if "Interface" in s and "PHY" in s and "Protocol" in s:
            header_seen = True
            continue
        if not header_seen:
            continue
        parts = s.split()
        if len(parts) < 3:
            continue
        name, phy, protocol = parts[0], parts[1], parts[2]
        if name in _LEGEND_TOKENS:
            continue
        # 보호: name 이 interface 형태인지
        if not re.match(r"^[A-Za-z][\w\.\-]*\d?(/\d+)*$", name):
            continue
        results.append(InterfacePhy(name, phy, protocol))
    return results


def up_physical_ports(qid: int, device: str) -> list[str]:
    """UP(Phy=up, Proto=up) 상태의 물리 포트만 포트번호 순으로 반환."""
    ifaces = parse_interface_brief(qid, device)
    physicals = [
        i.name
        for i in ifaces
        if i.is_up
        and (
            i.name.startswith(("GE", "10GE", "25GE", "40GE", "100GE", "XGE"))
            or i.name.startswith("Eth-Trunk")
        )
    ]
    return sorted(physicals, key=port_sort_key)


# ---------------------------------------------------------------------------
# Interface description (peer 힌트용)
# ---------------------------------------------------------------------------

# "Interface   PHY   Protocol   Description"
_DESC_PRIMARY = re.compile(
    r"^\s*(\S+)\s+"                # Interface
    r"(up|down|\*down|\^down)\s+"  # PHY
    r"(up|down)\s+"                # Protocol
    r"(.*?)\s*$"                   # Description
)


def parse_interface_description(qid: int, device: str) -> dict[str, str]:
    text = read_file(qid, device, "display_interface_description.txt")
    result: dict[str, str] = {}
    header_seen = False
    for raw in text.splitlines():
        s = raw.rstrip()
        if not s.strip():
            continue
        if "Interface" in s and ("PHY" in s or "Phy" in s) and "Description" in s:
            header_seen = True
            continue
        if not header_seen:
            continue
        m = _DESC_PRIMARY.match(raw)
        if not m:
            continue
        name, desc = m.group(1), m.group(4).strip()
        if name in _LEGEND_TOKENS:
            continue
        result[name] = desc
    return result


# ---------------------------------------------------------------------------
# IP interface brief (IP 주소 할당)
# ---------------------------------------------------------------------------

_IP_IF_LINE = re.compile(
    r"^\s*(\S+)\s+"                               # Interface
    r"(\d+\.\d+\.\d+\.\d+(?:/\d+)?|unassigned)"   # IP 주소 or unassigned
)


def parse_ip_interface_brief(qid: int, device: str) -> dict[str, str]:
    """Interface -> IP 주소 dict. 'unassigned' 는 생략."""
    text = read_file(qid, device, "display_ip_interface_brief.txt")
    result: dict[str, str] = {}
    for raw in text.splitlines():
        m = _IP_IF_LINE.match(raw)
        if not m:
            continue
        name, ip = m.group(1), m.group(2)
        if ip == "unassigned":
            continue
        # 'Interface' 헤더 자체 스킵
        if name.lower() == "interface":
            continue
        result[name] = ip
    return result


def find_ip_owner(qid: int, target_ip: str) -> list[str]:
    """해당 IP 를 interface 에 할당한 device 리스트. 마스크 없이 정확 매칭."""
    owners: list[str] = []
    target = target_ip.split("/", 1)[0]
    for dev in list_devices(qid):
        for ip in parse_ip_interface_brief(qid, dev).values():
            if ip.split("/", 1)[0] == target:
                owners.append(dev)
                break
    return owners


# ---------------------------------------------------------------------------
# Description 기반 peer 복원 (Q29~Q33 PJ 영역 핵심)
# ---------------------------------------------------------------------------

# Traditional 포맷: "From_{self}_{self_port}_To_{peer}_{peer_port}"
_DESC_TRAD = re.compile(
    r"^From_[\w\-]+_\S+?_To_([\w\-]+)_(\S+?)\s*$"
)
# PJ 포맷: "To-{peer}-{peer_port}" (peer 이름에 hyphen 포함 가능)
_DESC_PJ = re.compile(
    r"^To-([A-Za-z][\w\-]*[A-Za-z\d])-((?:GE|XGE|10GE|25GE|40GE|100GE|Eth-Trunk)\S*)\s*$"
)


def parse_peer_from_description(desc: str) -> tuple[str, str] | None:
    """description 문자열에서 (peer_device, peer_port) 추출.

    성공: ('Atlas-Prime-01', 'GE1/0/2')
    실패: None (빈 description, 벤더 alias, 다운포트 등)
    """
    if not desc:
        return None
    d = desc.strip()
    if not d:
        return None

    m = _DESC_TRAD.match(d)
    if m:
        return m.group(1), m.group(2)

    m = _DESC_PJ.match(d)
    if m:
        return m.group(1), m.group(2)

    return None


def reverse_description_lookup(
    qid: int, target_device: str
) -> list[tuple[str, str, str]]:
    """주변 device 의 description 에서 target 을 peer 로 언급하는 항목 추출.

    반환: [(source_device, source_port, target_port), ...]
    예: Q29 target=Demeter-Prime-01
        -> [('Atlas-Prime-01', 'GE1/0/2', 'GE1/0/0'),
            ('Atlas-Prime-02', 'GE1/0/2', 'GE1/0/1'), ...]
    """
    results: list[tuple[str, str, str]] = []
    for dev in list_devices(qid):
        if dev == target_device:
            continue
        iface_phy = {i.name: i for i in parse_interface_brief(qid, dev)}
        for src_port, desc in parse_interface_description(qid, dev).items():
            parsed = parse_peer_from_description(desc)
            if parsed is None:
                continue
            peer_dev, peer_port = parsed
            if peer_dev != target_device:
                continue
            # source 포트가 UP 상태인지 확인 (DOWN 링크는 복원 대상 아님)
            phy = iface_phy.get(src_port)
            if phy is None or not phy.is_up:
                continue
            results.append((dev, src_port, peer_port))
    return results


# ---------------------------------------------------------------------------
# IP routing-table
# ---------------------------------------------------------------------------

# "Destination/Mask    Proto    Pre  Cost     Flags  NextHop           Interface"
_ROUTE_LINE = re.compile(
    r"^\s*(\d+\.\d+\.\d+\.\d+/\d+)"  # destination/mask
    r"\s+(\S+)"                       # proto
    r"\s+\d+\s+\d+"                   # pre, cost
    r"\s+(\S+)"                       # flags
    r"\s+(\d+\.\d+\.\d+\.\d+)"        # nexthop
    r"\s+(\S+)\s*$"                   # egress interface
)


def parse_routing_table(
    qid: int,
    device: str,
    filename: str = "display_ip_routing-table.txt",
) -> list[Route]:
    text = read_file(qid, device, filename)
    results: list[Route] = []
    for raw in text.splitlines():
        m = _ROUTE_LINE.match(raw)
        if not m:
            continue
        results.append(Route(m.group(1), m.group(2), m.group(4), m.group(5)))
    return results


def lookup_longest_prefix(qid: int, device: str, dst_ip: str) -> Route | None:
    """destination 으로 가는 최장 prefix 매칭 route 반환. 없으면 None."""
    try:
        import ipaddress
        target = ipaddress.ip_address(dst_ip)
    except (ValueError, ImportError):
        return None

    best: Route | None = None
    for r in parse_routing_table(qid, device):
        try:
            net = ipaddress.ip_network(r.destination, strict=False)
        except ValueError:
            continue
        if target in net:
            if best is None or r.prefix_len > best.prefix_len:
                best = r
    return best


# ---------------------------------------------------------------------------
# Port natural sort
# ---------------------------------------------------------------------------

_PORT_NUM_RE = re.compile(r"(\d+)")


def port_sort_key(port: str) -> tuple:
    """GE1/0/10 이 GE1/0/2 뒤로 가도록 정렬하는 natural key."""
    parts = _PORT_NUM_RE.split(port)
    key: list = []
    for p in parts:
        if p.isdigit():
            key.append(int(p))
        elif p:
            key.append(p)
    return tuple(key)


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

def _smoke_test() -> None:
    """Q1, Q29, Q34 세 가지 대표 케이스 smoke test."""
    # Q1 Gamma-Portal-01: 정상 LLDP + interface brief
    q1_lldp = parse_lldp(1, "Gamma-Portal-01")
    assert len(q1_lldp) >= 5, f"Q1 LLDP 너무 적음: {q1_lldp}"
    assert all(nb.neighbor_device.startswith(("Gamma", "Alpha", "Beta", "Delta"))
               for nb in q1_lldp), f"Q1 LLDP 이상 device: {q1_lldp}"
    print(f"[Q1] Gamma-Portal-01 LLDP: {len(q1_lldp)} entries OK")
    print(f"     예시: {q1_lldp[0]}")

    q1_up = up_physical_ports(1, "Gamma-Portal-01")
    assert len(q1_up) >= 5, f"Q1 UP 포트 너무 적음: {q1_up}"
    print(f"[Q1] Gamma-Portal-01 UP ports: {q1_up}")

    # Q29 Demeter-Prime-01: LLDP empty -> reverse lookup 필요
    q29_lldp = parse_lldp(29, "Demeter-Prime-01")
    print(f"[Q29] Demeter-Prime-01 LLDP 직접: {len(q29_lldp)} entries (empty 기대)")

    q29_reverse_lldp = reverse_lldp_lookup(29, "Demeter-Prime-01")
    print(f"[Q29] LLDP 역추적: {len(q29_reverse_lldp)} entries (0 기대, PJ는 description 필요)")

    q29_reverse_desc = reverse_description_lookup(29, "Demeter-Prime-01")
    assert len(q29_reverse_desc) >= 2, f"Q29 description 역추적 실패: {q29_reverse_desc}"
    rev_devices = sorted({src for src, _, _ in q29_reverse_desc})
    print(f"[Q29] Demeter-Prime-01 description 역참조 devices: {rev_devices}")
    for src, src_port, tgt_port in q29_reverse_desc:
        print(f"     {src}({src_port}) <-> Demeter-Prime-01({tgt_port})")
    # 환각 방지 확인: Spine/PC 같은 alias 없어야 함
    assert not any(
        any(alias in d for alias in ("Spine", "PC1", "PC2", "Core-0"))
        for d in rev_devices
    ), f"환각 alias 검출: {rev_devices}"
    print(f"[Q29] 환각 alias 0건 확인 OK")

    # Q29 Demeter-Prime-01 UP 물리 포트 (자체 interface_brief 살아있음)
    q29_up = up_physical_ports(29, "Demeter-Prime-01")
    print(f"[Q29] Demeter-Prime-01 UP 물리 포트: {q29_up}")

    # Q7 Beta-Node-01 routing table
    routes = parse_routing_table(7, "Beta-Node-01")
    assert len(routes) > 10, f"Q7 routes 너무 적음: {len(routes)}"
    print(f"[Q7] Beta-Node-01 routes: {len(routes)}")
    print(f"     예시: {routes[0]}")

    # Q34 Hermes-Node-01
    q34_lldp = parse_lldp(34, "Hermes-Node-01")
    print(f"[Q34] Hermes-Node-01 LLDP: {len(q34_lldp)} entries")
    if q34_lldp:
        print(f"     예시: {q34_lldp[0]}")

    # IP owner test (Q7 question: 192.168.70.22)
    owners = find_ip_owner(7, "192.168.70.22")
    print(f"[Q7] 192.168.70.22 owner: {owners}")

    print("\n전체 smoke test 통과")


if __name__ == "__main__":
    _smoke_test()
