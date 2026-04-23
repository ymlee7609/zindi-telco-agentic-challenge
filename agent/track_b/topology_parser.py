"""Track B Topology 문제 (Q1~Q6, Q29~Q33) 전용 deterministic 파서.

링크 복원 4단계 Tier:
  Tier 0: 타겟 자체 description (To-Peer-Port 포맷)
  Tier 1: 타겟 자체 LLDP neighbor brief
  Tier 2: 주변 device 의 LLDP 역추적 (타겟이 neighbor 로 등장)
  Tier 3: 주변 device 의 description 역추적 (타겟이 peer 로 기재)
LLM 추론 없이 CLI 출력 파일에서만 답을 결정한다.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from cli_parsers import (
    list_devices,
    parse_interface_brief,
    parse_interface_description,
    parse_lldp,
    parse_peer_from_description,
    port_sort_key,
    read_file,
    reverse_description_lookup,
    reverse_lldp_lookup,
    up_physical_ports,
)

# ---------------------------------------------------------------------------
# 포트명 정규화 (괄호 접미사 제거: 'GE1/0/0(10G)' -> 'GE1/0/0')
# ---------------------------------------------------------------------------

_PORT_SUFFIX_RE = re.compile(r"\([^)]+\)$")


def _normalize_port(name: str) -> str:
    return _PORT_SUFFIX_RE.sub("", name).strip()


# ---------------------------------------------------------------------------
# UP 물리 포트 목록 (GigabitEthernet/GE 포맷 혼재 및 들여쓰기 포맷 처리)
# ---------------------------------------------------------------------------

_GE_PREFIX = re.compile(
    r"^(GigabitEthernet|XGigabitEthernet|10GE|25GE|40GE|100GE|GE|XGE|Eth-Trunk)"
)


def _up_physical_ports_extended(qid: int, device: str) -> set[str]:
    """UP 물리 포트를 수집.

    cli_parsers.up_physical_ports 가 처리하지 못하는 포맷도 커버:
    - 'GigabitEthernet1/0/0(10G)' 포맷 (들여쓰기 포함)
    - Eth-Trunk 의 멤버 포트 (들여쓰기 행) 도 포함
    sub-interface (.X) 제외.
    """
    # 기본 cli_parsers 결과 수집 (Eth-Trunk 및 서브인터페이스 제외)
    base = {
        p for p in up_physical_ports(qid, device)
        if not p.startswith("Eth-Trunk") and "." not in p
    }

    # interface brief 파일 직접 파싱으로 보완
    text = read_file(qid, device, "display_interface_brief.txt")
    extra: set[str] = set()
    for line in text.splitlines():
        parts = line.split()
        if len(parts) < 3:
            continue
        raw_name = parts[0]
        phy, proto = parts[1], parts[2]
        if phy != "up" or proto != "up":
            continue
        name = _normalize_port(raw_name)
        # GigabitEthernet -> GE 변환
        name = re.sub(r"^GigabitEthernet", "GE", name)
        name = re.sub(r"^XGigabitEthernet", "XGE", name)
        # sub-interface 제외
        if "." in name:
            continue
        # Eth-Trunk 자체는 제외 (논리 인터페이스); 멤버 포트 (GE 등) 는 포함
        if name.startswith("Eth-Trunk"):
            continue
        if _GE_PREFIX.match(name):
            extra.add(name)

    return base | extra


# ---------------------------------------------------------------------------
# 자체 description 에서 peer 파싱 (대소문자 무관 'to' 처리 포함)
# ---------------------------------------------------------------------------

# 소문자 'to' 패턴도 지원
_DESC_SELF_PJ_LC = re.compile(
    r"^[Tt]o-([A-Za-z][\w\-]*[A-Za-z\d])-((?:GE|XGE|10GE|25GE|40GE|100GE|Eth-Trunk)\S*)\s*$"
)
_DESC_SELF_TRAD = re.compile(
    r"^From_[\w\-]+_\S+?_To_([\w\-]+)_(\S+?)\s*$"
)


def _parse_peer_extended(desc: str) -> tuple[str, str] | None:
    """대소문자 무관 peer 파싱 (cli_parsers.parse_peer_from_description 확장)."""
    if not desc:
        return None
    d = desc.strip()
    # 기본 파서 먼저 시도
    result = parse_peer_from_description(d)
    if result:
        return result
    # 소문자 'to-' 패턴
    m = _DESC_SELF_PJ_LC.match(d)
    if m:
        return m.group(1), m.group(2)
    # Traditional 포맷
    m = _DESC_SELF_TRAD.match(d)
    if m:
        return m.group(1), m.group(2)
    return None


# ---------------------------------------------------------------------------
# 환각 alias 필터
# ---------------------------------------------------------------------------

# 실제 네트워크에 존재하지 않는 alias (CLI 출력 오류 또는 잘못된 description)
_HALLUCINATION_ALIASES = re.compile(
    r"\b(Spine\d*|PC\d+|Core-\d+|BorderLeaf\d*|BL\d+|H3C-\S+|PJlAN-\S+|LB\d+|server\b)\b",
    re.IGNORECASE,
)


def _is_hallucination(peer_dev: str) -> bool:
    """peer_dev 가 환각 alias 이면 True."""
    return bool(_HALLUCINATION_ALIASES.search(peer_dev))


# ---------------------------------------------------------------------------
# Tier 0: 타겟 자체 description 기반 복원
# ---------------------------------------------------------------------------


def _tier0_self_description(qid: int, target: str) -> list[tuple[str, str, str]]:
    """타겟 자체 description 에서 peer 를 직접 추출.

    'To-Peer-Port' 또는 'From_..._To_Peer_Port' 포맷을 파싱.
    환각 alias (Spine, PC, BL 등) 는 제외.
    """
    links: list[tuple[str, str, str]] = []
    desc_map = parse_interface_description(qid, target)
    for raw_port, desc in desc_map.items():
        local_port = _normalize_port(raw_port)
        if "." in local_port:
            continue
        parsed = _parse_peer_extended(desc)
        if parsed is None:
            continue
        peer_dev, peer_port = parsed
        if _is_hallucination(peer_dev):
            continue
        links.append((local_port, peer_dev, peer_port))
    return links


# ---------------------------------------------------------------------------
# Tier 1: 타겟 자체 LLDP
# ---------------------------------------------------------------------------


def _tier1_direct_lldp(qid: int, target: str) -> list[tuple[str, str, str]]:
    links: list[tuple[str, str, str]] = []
    for nb in parse_lldp(qid, target):
        links.append((nb.local_if, nb.neighbor_device, nb.neighbor_if))
    return links


# ---------------------------------------------------------------------------
# Tier 2: LLDP 역추적
# ---------------------------------------------------------------------------


def _tier2_reverse_lldp(qid: int, target: str) -> list[tuple[str, str, str]]:
    links: list[tuple[str, str, str]] = []
    for src_dev, nb in reverse_lldp_lookup(qid, target):
        # 타겟 입장: local_if=nb.neighbor_if, peer_dev=src_dev, peer_if=nb.local_if
        links.append((nb.neighbor_if, src_dev, nb.local_if))
    return links


# ---------------------------------------------------------------------------
# Tier 3: description 역추적 (포트명 정규화 포함)
# ---------------------------------------------------------------------------


def _tier3_reverse_description(qid: int, target: str) -> list[tuple[str, str, str]]:
    """주변 device 의 description 에서 target 을 peer 로 언급하는 항목 역추적.

    cli_parsers.reverse_description_lookup 을 사용하되,
    'GE1/0/2(10G)' 같은 포트명 suffix 를 제거하여 포트 매칭 정확도를 높인다.
    """
    links: list[tuple[str, str, str]] = []
    # cli_parsers 기본 역추적
    for src_dev, src_port, tgt_port in reverse_description_lookup(qid, target):
        src_port_norm = _normalize_port(src_port)
        tgt_port_norm = _normalize_port(tgt_port)
        links.append((tgt_port_norm, src_dev, src_port_norm))

    # cli_parsers 가 놓친 케이스 보완: UP 검사를 포트명 정규화로 재시도
    for dev in list_devices(qid):
        if dev == target:
            continue
        iface_phy = {
            _normalize_port(i.name): i
            for i in parse_interface_brief(qid, dev)
        }
        for raw_port, desc in parse_interface_description(qid, dev).items():
            src_port_norm = _normalize_port(raw_port)
            if "." in src_port_norm:
                continue
            parsed = _parse_peer_extended(desc)
            if parsed is None:
                continue
            peer_dev, peer_port = parsed
            if peer_dev != target:
                continue
            # UP 확인
            phy = iface_phy.get(src_port_norm)
            if phy is None or not phy.is_up:
                continue
            peer_port_norm = _normalize_port(peer_port)
            entry = (peer_port_norm, dev, src_port_norm)
            if entry not in links:
                links.append(entry)

    return links


# ---------------------------------------------------------------------------
# 중복 제거 (local_port 기준 first-win)
# ---------------------------------------------------------------------------


def _deduplicate(links: list[tuple[str, str, str]]) -> list[tuple[str, str, str]]:
    seen: set[str] = set()
    result: list[tuple[str, str, str]] = []
    for local_if, peer_dev, peer_if in links:
        if local_if not in seen:
            seen.add(local_if)
            result.append((local_if, peer_dev, peer_if))
    return result


# ---------------------------------------------------------------------------
# 질문에서 타겟 노드명 추출
# ---------------------------------------------------------------------------

_TARGET_PATTERNS = [
    re.compile(r"\bof\s+([\w][\w\-]*?\d+)\s+(?:within|in\s+the|in\b|has\b)"),
    re.compile(r"\bof\s+([\w][\w\-]*?\d+)[,\.\s]"),
    re.compile(r"data\s+of\s+([\w][\w\-]*?\d+)"),
]


# @MX:ANCHOR: [AUTO] extract_target_node — topology_parser, gen_v12_topo 등 3곳 호출
# @MX:REASON: [AUTO] 질문 원문에서 타겟 노드명 추출 공개 진입점
def extract_target_node(question_text: str) -> str | None:
    """질문에서 타겟 노드명 추출.

    예: 'data of Gamma-Aegis-01 within...' -> 'Gamma-Aegis-01'
    """
    for pat in _TARGET_PATTERNS:
        m = pat.search(question_text)
        if m:
            candidate = m.group(1).strip().rstrip(".,;)")
            if re.search(r"[A-Za-z]", candidate) and re.search(r"\d", candidate):
                return candidate
    return None


# ---------------------------------------------------------------------------
# 메인 복원 함수
# ---------------------------------------------------------------------------

# @MX:ANCHOR: [AUTO] solve_topology — gen_v12_topo, smoke test 등 3곳 호출
# @MX:REASON: [AUTO] Topology 복원 4-Tier 로직 캡슐화 메인 진입점
def solve_topology(
    qid: int, target: str
) -> tuple[list[tuple[str, str, str]], str, str, int, int]:
    """타겟 노드의 UP 포트 링크를 복원한다.

    반환: (links, confidence, method, resolved_ports, total_up_ports)
    - links: [(local_port, peer_dev, peer_port), ...] — port natural sort
    - confidence: "H" / "M" / "L"
    - method: "self_desc" / "lldp" / "reverse_lldp" / "desc" / "mixed" / "none"
    - resolved_ports: 확정된 포트 수
    - total_up_ports: UP 물리 포트 총 수
    """
    up_ports = _up_physical_ports_extended(qid, target)
    total_up = len(up_ports)

    # 각 tier 결과를 port 기준 dict 로 수집 (나중 tier 가 먼저 tier 를 덮어씀 방지)
    collected: dict[str, tuple[str, str]] = {}  # local_port -> (peer_dev, peer_if)
    methods_used: list[str] = []

    # --- Tier 0: 자체 description ---
    t0 = _tier0_self_description(qid, target)
    for lp, pd, pi in t0:
        if lp not in collected:
            collected[lp] = (pd, pi)
    if t0:
        methods_used.append("self_desc")

    # --- Tier 1: 자체 LLDP ---
    t1 = _tier1_direct_lldp(qid, target)
    for lp, pd, pi in t1:
        if lp not in collected:
            collected[lp] = (pd, pi)
    if t1:
        # LLDP 는 description 보다 신뢰도 높음 → 덮어씀
        for lp, pd, pi in t1:
            collected[lp] = (pd, pi)
        methods_used.append("lldp")

    # --- 미확정 포트 계산 ---
    missing = up_ports - set(collected.keys())

    # --- Tier 2: LLDP 역추적 (미확정 포트 보충) ---
    t2 = _tier2_reverse_lldp(qid, target)
    for lp, pd, pi in t2:
        if lp in missing:
            collected[lp] = (pd, pi)
            missing.discard(lp)
    if t2:
        methods_used.append("reverse_lldp")

    # --- Tier 3: description 역추적 (미확정 포트 보충) ---
    t3 = _tier3_reverse_description(qid, target)
    for lp, pd, pi in t3:
        if lp in missing:
            collected[lp] = (pd, pi)
            missing.discard(lp)
    if t3:
        methods_used.append("desc")

    # --- UP 포트 필터 적용 ---
    if up_ports:
        links_raw = [
            (lp, pd, pi)
            for lp, (pd, pi) in collected.items()
            if lp in up_ports
        ]
    else:
        links_raw = [(lp, pd, pi) for lp, (pd, pi) in collected.items()]

    # --- Natural sort ---
    links_raw.sort(key=lambda t: port_sort_key(t[0]))

    resolved = len(links_raw)

    # --- Method 요약 ---
    if not methods_used:
        method = "none"
    elif len(methods_used) == 1:
        method = methods_used[0]
    else:
        method = "mixed"

    # --- Confidence ---
    if total_up == 0:
        confidence = "L"
    elif resolved == 0:
        confidence = "L"
    elif resolved >= total_up:
        confidence = "H"
    else:
        confidence = "M"

    return links_raw, confidence, method, resolved, total_up


# ---------------------------------------------------------------------------
# 답 포맷 변환
# ---------------------------------------------------------------------------


def format_answer(target: str, links: list[tuple[str, str, str]]) -> str:
    """links 를 제출용 문자열로 변환.

    포맷: "Target(port)->Peer(port)" 줄마다, 끝에 newline 없음.
    """
    if not links:
        return ""
    return "\n".join(f"{target}({lp})->{pd}({pi})" for lp, pd, pi in links)


# ---------------------------------------------------------------------------
# Q1~Q6, Q29~Q33 일괄 처리
# ---------------------------------------------------------------------------

# 질문 번호 -> (데이터 qid 폴더, 타겟 노드명) 정적 매핑
_TOPOLOGY_TARGETS: dict[int, tuple[int, str]] = {
    1: (1, "Gamma-Aegis-01"),
    2: (2, "Gamma-Axis-02"),
    3: (3, "Beta-Aegis-02"),
    4: (4, "Beta-Portal-02"),
    5: (5, "Delta-Node-01"),
    6: (6, "Delta-Axis-01"),
    29: (29, "Demeter-Prime-01"),
    30: (30, "Atlas-Prime-01"),
    31: (31, "Janus-Prime-01"),
    32: (32, "Aegis-Prime-01"),
    33: (33, "Janus-Node-02"),
}


# @MX:ANCHOR: [AUTO] solve_all_topology — gen_v12_topo 단독 호출
# @MX:REASON: [AUTO] 11문제 전체 배치 처리 최상위 함수
def solve_all_topology() -> dict[int, dict]:
    """Q1~Q6, Q29~Q33 11문제를 순회하며 답변을 생성한다.

    반환:
        {qid: {
            "answer": str,
            "confidence": str,       # H / M / L
            "target": str,
            "method": str,
            "resolved_ports": int,
            "total_up_ports": int,
            "links": list[tuple],
        }}
    """
    results: dict[int, dict] = {}
    for qnum, (data_qid, target) in _TOPOLOGY_TARGETS.items():
        links, confidence, method, resolved, total_up = solve_topology(
            data_qid, target
        )
        answer = format_answer(target, links)
        results[qnum] = {
            "answer": answer,
            "confidence": confidence,
            "target": target,
            "method": method,
            "resolved_ports": resolved,
            "total_up_ports": total_up,
            "links": links,
        }
    return results


# ---------------------------------------------------------------------------
# 환각 alias 검사
# ---------------------------------------------------------------------------

_HALLUCINATION_PATTERNS = re.compile(
    r"\b(Spine[12]?|PC[0-9]|Core-[0-9])\b", re.IGNORECASE
)


def check_hallucination(text: str) -> list[str]:
    """결과 텍스트에서 환각 alias 검출. 발견된 alias 리스트 반환."""
    return _HALLUCINATION_PATTERNS.findall(text)


# ---------------------------------------------------------------------------
# Smoke test
# ---------------------------------------------------------------------------


def _smoke() -> None:
    """Q1 (Tier 1 LLDP), Q29 (Tier 3 description) 대표 케이스 검증."""
    print("=" * 60)
    print("Topology Parser — Smoke Test")
    print("=" * 60)

    for qnum in [1, 29, 30, 31, 32, 33]:
        data_qid, target = _TOPOLOGY_TARGETS[qnum]
        links, conf, method, resolved, total_up = solve_topology(data_qid, target)
        answer = format_answer(target, links)
        hall = check_hallucination(answer)

        print(f"\nQ{qnum} — {target}")
        print(f"  method     : {method}")
        print(f"  confidence : {conf}")
        print(f"  resolved   : {resolved}/{total_up} UP ports")
        if hall:
            print(f"  [WARN] 환각 alias 검출: {hall}")
        else:
            print("  환각 alias : 0건 OK")
        print("  answer (첫 5줄):")
        for line in answer.split("\n")[:5]:
            print(f"    {line}")

    print("\nSmoke test 완료")


if __name__ == "__main__":
    _smoke()
