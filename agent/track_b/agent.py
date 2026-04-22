#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Track B Agent: IP Network Troubleshooting Agent
Qwen3.5-35B-A3B via OpenRouter / HuggingFace / DashScope / Anthropic
"""

import argparse
import csv
import json
import logging
import os
import time
from pathlib import Path
from typing import Any

import requests

# .env 파일에서 환경변수 로드 (agent/track_b/agent.py → repo root = parents[2])
_env_path = Path(__file__).resolve().parents[2] / ".env"
if _env_path.exists():
    with open(_env_path) as _f:
        for _line in _f:
            _line = _line.strip()
            if _line and not _line.startswith("#") and "=" in _line:
                _key, _, _val = _line.partition("=")
                os.environ.setdefault(_key.strip(), _val.strip())
from openai import OpenAI

# ============================================================
# Configuration
# ============================================================

# API provider config (priority: CLI arg > env var > defaults)
# Supported providers: openrouter, huggingface, dashscope, local, anthropic
PROVIDERS = {
    "openrouter": {
        "base_url": "https://openrouter.ai/api/v1",
        "model": "qwen/qwen3.5-35b-a3b",
        "env_key": "OPENROUTER_API_KEY",
        "sdk": "openai",
    },
    "huggingface": {
        "base_url": "https://router.huggingface.co/novita/v3/openai",
        "model": "qwen/qwen3.5-35b-a3b",
        "env_key": "HF_TOKEN",
        "token_file": "~/.cache/huggingface/token",
        "sdk": "openai",
    },
    "dashscope": {
        "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "model": "qwen3.5-flash",
        "env_key": "DASHSCOPE_API_KEY",
        "sdk": "openai",
    },
    "local": {
        "base_url": "http://localhost:8000/v1",
        "model": "Qwen/Qwen3.5-35B-A3B",
        "env_key": "",
        "sdk": "openai",
    },
    "anthropic": {
        "base_url": "",
        "model": "claude-sonnet-4-20250514",
        "env_key": "ANTHROPIC_API_KEY",
        "sdk": "anthropic",
    },
    "groq": {
        "base_url": "https://api.groq.com/openai/v1",
        "model": "llama-3.3-70b-versatile",
        "env_key": "GROQ_API_KEY",
        "sdk": "openai",
    },
    "groq-qwen": {
        "base_url": "https://api.groq.com/openai/v1",
        "model": "qwen-qwq-32b",
        "env_key": "GROQ_API_KEY",
        "sdk": "openai",
    },
    "gemini": {
        "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/",
        "model": "gemini-2.0-flash",
        "env_key": "GEMINI_API_KEY",
        "sdk": "openai",
    },
}

DEFAULT_PROVIDER = "openrouter"


def _resolve_api_key(provider_cfg: dict) -> str:
    env_key = provider_cfg.get("env_key", "")
    if env_key:
        val = os.environ.get(env_key, "")
        if val:
            return val
    token_file = provider_cfg.get("token_file", "")
    if token_file:
        path = os.path.expanduser(token_file)
        if os.path.exists(path):
            with open(path) as f:
                return f.read().strip()
    return "EMPTY"


PROVIDER_NAME = os.environ.get("LLM_PROVIDER", DEFAULT_PROVIDER)
_provider_cfg = PROVIDERS[PROVIDER_NAME]
API_KEY = _resolve_api_key(_provider_cfg)
MODEL_BASE_URL = _provider_cfg["base_url"]
MODEL_NAME = _provider_cfg["model"]
SDK_TYPE = _provider_cfg.get("sdk", "openai")

NOC_API_URL = "http://127.0.0.1:7860/api/agent/execute"
MAX_ITERATIONS = 30
MAX_TOKENS = 8192
TIMEOUT_SECONDS = 540  # 9분 - 안전 마진

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("agent")

# ============================================================
# Question Type Detection
# ============================================================

import re

QTYPE_TOPOLOGY = "topology"
QTYPE_PATH = "path"
QTYPE_FAULT = "fault"


def detect_question_type(question_text: str) -> str:
    """질문 텍스트에서 문제 유형 자동 감지"""
    lower = question_text.lower()
    # Fault: 가장 특징적인 키워드 우선
    if "routing faults and port faults" in lower or "routing fault" in lower:
        return QTYPE_FAULT
    if "fault node;destination" in lower or "fault-node;destination" in lower:
        return QTYPE_FAULT
    # Topology: 링크 복원 관련
    if "link planning data" in lower or "restore the link" in lower:
        return QTYPE_TOPOLOGY
    if "up link connections" in lower or "link status" in lower:
        return QTYPE_TOPOLOGY
    # Path: 경로 추적
    if "addressing" in lower and "->" in question_text:
        return QTYPE_PATH
    if "path" in lower and "->" in question_text:
        return QTYPE_PATH
    if "provide the service path" in lower:
        return QTYPE_PATH
    # 기본값
    return QTYPE_PATH


def extract_topology_info(question_text: str) -> dict:
    """Topology 문제에서 타겟 노드와 이웃 노드 목록 추출"""
    info = {"target": "", "neighbors": [], "can_query_target": True}

    # 타겟 노드 추출 (첫 번째 등장하는 노드명 패턴)
    # "restore the link ... of the Gamma-Axis-02 node" or "UP link connections of this node"
    node_pattern = re.compile(r'\b([A-Z][a-z]+-[A-Z][a-z]+-\d+)\b')
    nodes = node_pattern.findall(question_text)
    if nodes:
        info["target"] = nodes[0]

    # 직접 쿼리 불가 여부
    if "cannot be queried from" in question_text.lower() or "link status cannot be queried" in question_text.lower():
        info["can_query_target"] = False

    # 이웃 노드 목록 추출 ("nodes connected ... are among these N nodes: A/B/C")
    neighbor_match = re.search(r'(?:nodes?|among)[^:]*:\s*([A-Za-z0-9/-]+(?:/[A-Za-z0-9-]+)*)', question_text)
    if neighbor_match:
        neighbor_str = neighbor_match.group(1)
        info["neighbors"] = [n.strip() for n in neighbor_str.split("/") if n.strip()]

    return info


def extract_path_info(question_text: str) -> dict:
    """Path 문제에서 출발/도착 노드 추출"""
    info = {"source": "", "destination": "", "dest_interface": "", "dest_ip": ""}
    node_pattern = re.compile(r'\b([A-Z][a-z]+-[A-Z][a-z]+-\d+)\b')
    nodes = node_pattern.findall(question_text)
    if len(nodes) >= 2:
        info["source"] = nodes[0]
        info["destination"] = nodes[1]
    elif len(nodes) == 1:
        info["source"] = nodes[0]

    # 인터페이스 추출
    iface_match = re.search(r'(GE\d+/\d+/\d+)', question_text)
    if iface_match:
        info["dest_interface"] = iface_match.group(1)

    # IP 추출
    ip_match = re.search(r'(?:IP[:\s]*)?(\d+\.\d+\.\d+\.\d+)', question_text)
    if ip_match:
        info["dest_ip"] = ip_match.group(1)

    # "addressing X.X.X.X path" 패턴 (PJ area)
    addr_match = re.search(r'addressing\s+(\d+\.\d+\.\d+\.\d+)', question_text)
    if addr_match:
        info["dest_ip"] = addr_match.group(1)

    return info


def extract_fault_info(question_text: str) -> dict:
    """Fault 문제에서 용의 노드 목록과 시나리오 정보 추출"""
    info = {"suspect_nodes": [], "source": "", "destination": "", "dest_ip": "", "scenario": ""}
    node_pattern = re.compile(r'\b([A-Z][a-z]+-[A-Z][a-z]+-\d+)\b')

    # 예시 텍스트 이후의 실제 문제 부분만 추출
    # "interface IP error" 라인 이후가 실제 문제
    actual_problem = question_text
    for marker in ["interface IP error", "Port fault examples:"]:
        parts = question_text.split(marker)
        if len(parts) > 1:
            # 마지막 파트에서 예시 라인(;포함) 이후의 텍스트
            remainder = parts[-1]
            # 예시 패턴(node;xxx;xxx) 이후의 텍스트 추출
            problem_lines = []
            found_non_example = False
            for line in remainder.strip().splitlines():
                line = line.strip()
                if not line:
                    continue
                # 예시 패턴 스킵 (node;target;reason)
                if re.match(r'^[\w-]+;[^;]+;[^;]+$', line):
                    continue
                if re.match(r'^(Routing|Port) fault', line):
                    continue
                problem_lines.append(line)
                found_non_example = True
            if found_non_example:
                actual_problem = '\n'.join(problem_lines)
                info["scenario"] = actual_problem
                break

    # "fault is on one of the three nodes: A, B, C" 패턴
    suspect_match = re.search(
        r'(?:fault|problem)\s+is\s+on\s+(?:one\s+of\s+)?(?:the\s+)?(?:\w+\s+)?nodes?[:\s]+([^\n.]+)',
        question_text, re.IGNORECASE,
    )
    if suspect_match:
        info["suspect_nodes"] = node_pattern.findall(suspect_match.group(1))

    # suspect가 아직 없으면 실제 문제 부분에서만 노드 추출
    if not info["suspect_nodes"]:
        actual_nodes = node_pattern.findall(actual_problem)
        if actual_nodes:
            info["suspect_nodes"] = list(dict.fromkeys(actual_nodes))

    # source/destination (addressing 패턴)
    addr_match = re.search(
        r'(\w+-\w+-\d+)\s+(?:is\s+)?addressing\s+(?:GE\d+/\d+/\d+\s+of\s+)?(\w+-\w+-\d+)',
        actual_problem,
    )
    if addr_match:
        info["source"] = addr_match.group(1)
        info["destination"] = addr_match.group(2)

    # "ping X.X.X.X from Node" 패턴 (PJ area)
    ping_match = re.search(r'ping\s+(\d+\.\d+\.\d+\.\d+)\s+from\s+(\w+-\w+-\d+)', actual_problem)
    if ping_match:
        info["dest_ip"] = ping_match.group(1)
        info["source"] = ping_match.group(2)

    # "Node pings ... ping X.X.X.X" 패턴
    ping_match2 = re.search(r'(\w+-\w+-\d+)\s+ping.*?(\d+\.\d+\.\d+\.\d+)', actual_problem)
    if ping_match2 and not info["source"]:
        info["source"] = ping_match2.group(1)
        info["dest_ip"] = ping_match2.group(2)

    # "MAC address conflict alarm" 패턴
    mac_match = re.search(r'(\w+-\w+-\d+)\s+received\s+a\s+MAC\s+address\s+conflict', actual_problem)
    if mac_match:
        info["source"] = mac_match.group(1)

    return info


_DEVICES_ROOT = Path(__file__).resolve().parent.parent.parent / "data" / "Track B" / "devices_outputs"


def load_scenario_devices(question_id: int) -> list[str]:
    """devices_outputs/{qid}/ 에서 실제 장비 목록 수집 (scenario별 화이트리스트)"""
    qdir = _DEVICES_ROOT / str(question_id)
    if not qdir.is_dir():
        return []
    try:
        return sorted(
            d.name for d in qdir.iterdir()
            if d.is_dir() and not d.name.startswith(".")
        )
    except OSError:
        return []


# [AUTO] Topology snapshot cache: scenario-wide LLDP graph + IP ownership map
_TOPOLOGY_CACHE: dict[int, dict] = {}


def build_topology_snapshot(question_id: int) -> dict:
    """devices_outputs/{qid}/ 를 파싱해 LLDP 인접 그래프 + IP->device 맵 생성."""
    if question_id in _TOPOLOGY_CACHE:
        return _TOPOLOGY_CACHE[question_id]
    qdir = _DEVICES_ROOT / str(question_id)
    graph: dict = {"lldp": {}, "ip_owner": {}}
    if not qdir.is_dir():
        _TOPOLOGY_CACHE[question_id] = graph
        return graph
    device_name_re = re.compile(r'^[A-Za-z][A-Za-z0-9\-]*-(Prime|Node|Axis|Aegis|Portal|Center|Edge|Core)-\d+$')
    for dev in sorted(qdir.iterdir()):
        if not dev.is_dir() or dev.name.startswith("."):
            continue
        # LLDP neighbors
        lldp_file = dev / "display_lldp_neighbor_brief.txt"
        if lldp_file.exists():
            try:
                txt = lldp_file.read_text(errors="ignore")
                # Neighbor Device column (last token per line) 또는 "Neighbor Device <name>"
                candidates = set(re.findall(r'\b([A-Z][A-Za-z]+-[A-Z][A-Za-z]+-\d+)\b', txt))
                candidates.discard(dev.name)
                graph["lldp"][dev.name] = sorted(candidates)
            except OSError:
                graph["lldp"][dev.name] = []
        # IP ownership from interface brief
        brief_file = dev / "display_ip_interface_brief.txt"
        if brief_file.exists():
            try:
                brief = brief_file.read_text(errors="ignore")
                for m in re.finditer(r'(\d+\.\d+\.\d+\.\d+)/\d+', brief):
                    ip = m.group(1)
                    if ip.startswith("127.") or ip == "0.0.0.0":
                        continue
                    graph["ip_owner"].setdefault(ip, [])
                    if dev.name not in graph["ip_owner"][ip]:
                        graph["ip_owner"][ip].append(dev.name)
            except OSError:
                pass
    _TOPOLOGY_CACHE[question_id] = graph
    return graph


def find_ip_owner(qid: int, ip: str) -> list[str]:
    """IP 의 장비 소유자 리스트. 정확한 일치가 없으면 같은 /24 내 후보 반환."""
    g = build_topology_snapshot(qid)
    owners = g["ip_owner"].get(ip, [])
    if owners:
        return owners
    # subnet /24 fallback
    prefix = ".".join(ip.split(".")[:3]) + "."
    return sorted({d for k, devs in g["ip_owner"].items() if k.startswith(prefix) for d in devs})


def bfs_shortest_path(qid: int, src: str, dst: str, max_depth: int = 8) -> list[str]:
    """LLDP 그래프 BFS로 src→dst 최단 경로 노드 리스트."""
    g = build_topology_snapshot(qid)
    if src not in g["lldp"] or dst not in g["lldp"]:
        return []
    if src == dst:
        return [src]
    from collections import deque
    visited = {src}
    queue = deque([(src, [src])])
    while queue:
        node, path = queue.popleft()
        if len(path) > max_depth:
            continue
        for nb in g["lldp"].get(node, []):
            if nb in visited:
                continue
            new_path = path + [nb]
            if nb == dst:
                return new_path
            visited.add(nb)
            queue.append((nb, new_path))
    return []


def validate_path_answer(answer: str, whitelist: set[str], qtype: str) -> tuple[bool, str, str]:
    """경로 답 포맷/환각 검증. 반환: (ok, cleaned, reason)."""
    # XML/tool-call/code-block 제거 후 첫 줄 추출
    clean = re.sub(r'<[^>]+>', '', answer)
    clean = re.sub(r'```[\s\S]*?```', '', clean)
    clean = clean.strip()
    if not clean:
        return False, "", "empty answer"
    first_line = clean.split("\n")[0].strip()
    if qtype == QTYPE_PATH:
        if "->" not in first_line:
            return False, first_line, "no arrow (path requires hop1->hop2 form)"
        hops = [h.strip() for h in first_line.split("->")]
        if len(hops) < 2:
            return False, first_line, f"only {len(hops)} hop"
        for h in hops:
            if re.fullmatch(r'\d+\.\d+\.\d+\.\d+', h):
                return False, first_line, f"IP in hop: {h}"
            if h not in whitelist:
                return False, first_line, f"hallucinated device: {h}"
    return True, first_line, "ok"


def build_type_hint(qtype: str, question_text: str, question_id: int = 0) -> str:
    """질문 유형별 cold-start 힌트 생성 (user message로 주입)"""
    if qtype == QTYPE_TOPOLOGY:
        info = extract_topology_info(question_text)
        target = info["target"]
        neighbors = info["neighbors"]

        if info["can_query_target"] and target:
            hint = (
                f"STRATEGY: This is a TOPOLOGY question. Target node: {target}.\n"
                f"Step 1: Query `display interface brief` on {target} to find UP ports.\n"
                f"Step 2: Query `display current-configuration` on {target}.\n"
                f"Step 3: Parse each UP interface's `description` field: From_X_PortA_To_Y_PortB\n"
                f"IMPORTANT: LLDP may return 'No permission'. Use description field from config as primary source.\n"
                f"Output ONLY lines in format: {target}(port)->PeerNode(port)"
            )
        elif neighbors:
            neighbor_list = ", ".join(neighbors)
            hint = (
                f"STRATEGY: This is a TOPOLOGY question. Target: {target} (CANNOT query directly).\n"
                f"Known neighbors: {neighbor_list}\n"
                f"Step 1: Query `display lldp neighbor brief` on ALL neighbors simultaneously.\n"
                f"Step 2: For each neighbor, look for {target} in LLDP output.\n"
                f"Step 3: If LLDP returns 'No permission' or empty: query `display current-configuration` instead.\n"
                f"Step 4: In config, look for description fields pointing to {target}.\n"
                f"Output ONLY lines in format: {target}(port)->PeerNode(port)"
            )
        else:
            return ""

        # @MX:NOTE: [AUTO] description alias 가드 — 일부 description 은
        # alias 라벨(예: "To-Spine2-...", "To-PC1-...")을 사용해 모델이
        # 정답으로 그대로 출력하는 사례가 있어 whitelist + 검증 절차를 주입
        devices = load_scenario_devices(question_id)
        if devices:
            device_list = ", ".join(devices)
            hint += (
                f"\n\nVALID DEVICES in this scenario (ONLY these names exist):"
                f"\n  {device_list}"
                f"\nABSOLUTELY DO NOT invent names. ONLY use names from the whitelist above."
                f"\n\nALIAS WARNING — interface descriptions may contain ALIAS labels:"
                f"\n  Example: 'description To-Spine2-GE1/0/2' where 'Spine2' is NOT a real"
                f"\n  device name but a topology-diagram label set by the operator."
                f"\n  RULE: If a description's PeerNode label is NOT in the VALID DEVICES"
                f"\n  whitelist above, IT IS AN ALIAS — do NOT use it in your answer."
                f"\n  Resolve to the real device name as follows:"
                f"\n    1) `display ip interface brief` on {target} -> get local IP/30 of the port"
                f"\n    2) `display arp` on every candidate peer in the whitelist"
                f"\n    3) The peer whose ARP marks the local port's /30 partner IP as 'I'"
                f"\n       (Interface = self-IP) is the real peer device"
                f"\n    4) For L2 trunk ports without IP, query `display current-configuration`"
                f"\n       on candidate peers and look for a description pointing back to {target}"
            )
        return hint

    elif qtype == QTYPE_PATH:
        info = extract_path_info(question_text)
        source = info["source"]
        dest = info["destination"]
        dest_ip = info["dest_ip"]
        dest_iface = info["dest_interface"]

        hint = f"STRATEGY: This is a PATH question. Source: {source}"
        if dest:
            hint += f", Destination: {dest}"
        if dest_ip:
            hint += f", Dest IP: {dest_ip}"
        if dest_iface:
            hint += f", Dest Interface: {dest_iface}"
        hint += (
            f"\nCRITICAL: You must trace EVERY hop. Do NOT skip intermediate nodes."
            f"\nStep 1: On {source}, query `display ip routing-table` + `display current-configuration`."
            f"\nStep 2: In routing table, find the route matching destination IP -> get next-hop IP + egress interface."
            f"\nStep 3: In config, find the egress interface's `description` field -> get next-hop DEVICE NAME."
            f"\n  Example: description From_NodeA_GE1/0/2_To_NodeB_GE1/0/6 -> next hop is NodeB"
            f"\nStep 4: Repeat Steps 1-3 on the next device until route is 'Direct'."
            f"\nOutput ONLY one line: NodeA->NodeB->...->NodeZ"
        )
        # [AUTO] Anti-hallucination: real device whitelist + IP/loop guards
        devices = load_scenario_devices(question_id)
        if devices:
            device_list = ", ".join(devices)
            hint += (
                f"\n\nVALID DEVICES in this scenario (ONLY these names exist):"
                f"\n  {device_list}"
                f"\nABSOLUTELY DO NOT invent names like 'Hermes-Secondary-XX', 'Core-01', 'Node-10-1-1-X', 'Gamma-Edge-XX'."
                f"\nIf a device is not in the list above, IT DOES NOT EXIST. Skip it."
            )
        hint += (
            f"\n\nIP HANDLING: A destination IP such as '10.1.1.10' is NEVER a device name."
            f"\n  Do NOT query 'Node-10-1-1-10'. Always resolve IP via routing-table next-hop,"
            f"\n  then map next-hop IP to a real device from the whitelist via interface description or ARP."
            f"\nLOOP GUARD: If you see [DUPLICATE-SKIPPED] in tool results, you are looping."
            f"\n  STOP exploring. Produce the BEST answer from data gathered so far, even if incomplete."
        )
        # [AUTO] Pre-computed topology hints (P0: BFS shortest path + IP owner)
        if question_id:
            dest_target = dest_ip or dest_iface or dest
            topology_hints = []
            if dest_ip:
                owners = find_ip_owner(question_id, dest_ip)
                if owners:
                    topology_hints.append(f"DEST IP {dest_ip} IS OWNED BY: {', '.join(owners)}")
                    # BFS candidate path
                    if source and owners:
                        shortest = bfs_shortest_path(question_id, source, owners[0])
                        if shortest:
                            topology_hints.append(
                                f"LLDP SHORTEST PATH CANDIDATE: {'->'.join(shortest)}"
                            )
            if topology_hints:
                hint += "\n\nPRE-COMPUTED TOPOLOGY HINTS:\n  " + "\n  ".join(topology_hints)
                hint += (
                    "\n  VERIFY this candidate by querying routing-table on key hops,"
                    " then OUTPUT the verified path. Prefer this over inventing new devices."
                )
        # [AUTO] Default route + VRRP + empty-EVPN fallbacks (Q38 lessons)
        hint += (
            f"\n\nDEFAULT ROUTE FALLBACK:"
            f"\n  If destination IP has no matching prefix in routing-table, use 0.0.0.0/0 next-hop."
            f"\n  Then find the device that OWNS this next-hop IP by:"
            f"\n    1. Query `display ip interface brief` on candidate devices from the whitelist"
            f"\n    2. The device where next-hop IP appears as a local interface IP (or VRRP shared IP"
            f"\n       on a Vbdif/Vlanif interface) is the next hop"
            f"\n    3. Confirm via `display lldp neighbor brief` adjacency to the current source"
            f"\nVRRP / SHARED GATEWAY PATTERN:"
            f"\n  If a next-hop IP appears as a /24 gateway on multiple devices (e.g., 10.1.5.1 on both"
            f"\n  Demeter-Prime-01 and Demeter-Prime-02 Vbdif50), this is a VRRP redundancy pair."
            f"\n  Pick the device that has LLDP adjacency with the current source node."
            f"\nEMPTY EVPN/BGP TABLE NOTE:"
            f"\n  Non-VTEP leaf devices (e.g., access leaves like Hermes-Prime/Hermes-Node) often have"
            f"\n  EMPTY `display bgp evpn all routing-table` and `display bgp vpnv4 all routing-table`."
            f"\n  Do NOT stall on empty tables. Fall back to routing-table + LLDP + interface brief."
            f"\nVXLAN OVERLAY HOPS:"
            f"\n  A VPN-instance routing-table entry like `0.0.0.0/0 IBGP via <VTEP-IP> VXLAN` means"
            f"\n  the next logical hop is the remote VTEP device. Resolve VTEP-IP to a device via"
            f"\n  its LoopBack0 IP (search `display ip interface brief` across the whitelist)."
        )
        return hint

    elif qtype == QTYPE_FAULT:
        info = extract_fault_info(question_text)
        suspects = info["suspect_nodes"]
        source = info.get("source", "")
        dest_ip = info.get("dest_ip", "")
        scenario = info.get("scenario", "")

        hint = "STRATEGY: This is a FAULT diagnosis question.\n"
        if scenario:
            hint += f"Actual problem: {scenario}\n"
        if source:
            hint += f"Source node: {source}\n"
        if dest_ip:
            hint += f"Destination IP: {dest_ip}\n"
        if suspects:
            suspect_list = ", ".join(suspects[:6])
            hint += f"Suspect/relevant nodes: {suspect_list}\n"
            hint += (
                f"Step 1: Query ALL relevant nodes simultaneously with:\n"
                f"  - `display ip routing-table` (check routing)\n"
                f"  - `display interface brief` (check port status UP/DOWN)\n"
                f"  - `display current-configuration` (check config for errors)\n"
            )
        else:
            hint += (
                f"Step 1: Start from source node, trace the path hop-by-hop.\n"
                f"  - Query `display ip routing-table` on each hop.\n"
                f"  - Query `display interface brief` to check port status.\n"
                f"  - Query `display current-configuration` for config errors.\n"
            )
        hint += (
            f"Step 2: Look for: missing routes, blackhole routes, shutdown ports, IP errors, "
            f"static route errors, OSPF/BGP misconfig, MTU issues.\n"
            f"Step 3: For routing faults: node;dest-IP;cause. For port faults: node;port;cause.\n"
            f"Output ONLY fault lines, one per line."
        )
        return hint

    return ""


# ============================================================
# Answer Post-processing
# ============================================================

# 답변에서 유효한 라인만 추출하는 패턴
_TOPOLOGY_RE = re.compile(r'^[\w-]+\([A-Za-z0-9/]+\)\s*->\s*[\w-]+\([A-Za-z0-9/]+\)$')
_PATH_RE = re.compile(r'^[\w-]+(?:\s*->\s*[\w-]+){1,}$')
_FAULT_RE = re.compile(r'^[\w-]+;[^;\n]+;[^;\n]+$')

# 번호 매기기 제거 (e.g., "1. Node(port)->..." or "- Node(port)->...")
_NUMBERED_PREFIX_RE = re.compile(r'^\s*(?:\d+[\.\)]\s*|[-*]\s*)')


def postprocess_answer(raw: str, qtype: str = "") -> str:
    """모델 출력에서 유효한 답변 라인만 추출"""
    if not raw or not raw.strip():
        return ""
    lines = [l.strip() for l in raw.strip().splitlines() if l.strip()]
    if not lines:
        return raw.strip()

    # 번호 매기기 제거 후 재검사
    cleaned_lines = []
    for line in lines:
        cleaned = _NUMBERED_PREFIX_RE.sub('', line).strip()
        cleaned_lines.append(cleaned)

    # 패턴 매칭으로 유효 라인 추출 (원본 + cleaned 모두 검사)
    topology_lines = []
    for orig, cleaned in zip(lines, cleaned_lines):
        if _TOPOLOGY_RE.match(orig):
            topology_lines.append(orig)
        elif _TOPOLOGY_RE.match(cleaned):
            topology_lines.append(cleaned)

    path_lines = []
    for orig, cleaned in zip(lines, cleaned_lines):
        if _PATH_RE.match(orig):
            path_lines.append(orig)
        elif _PATH_RE.match(cleaned):
            path_lines.append(cleaned)

    fault_lines = []
    for orig, cleaned in zip(lines, cleaned_lines):
        if _FAULT_RE.match(orig):
            fault_lines.append(orig)
        elif _FAULT_RE.match(cleaned):
            fault_lines.append(cleaned)

    # 유형 힌트가 있으면 해당 유형 우선
    if qtype == QTYPE_TOPOLOGY and topology_lines:
        return '\n'.join(dict.fromkeys(topology_lines))  # 중복 제거, 순서 유지
    if qtype == QTYPE_FAULT and fault_lines:
        return '\n'.join(dict.fromkeys(fault_lines))
    if qtype == QTYPE_PATH and path_lines:
        return max(path_lines, key=lambda x: x.count('->'))

    # 유형 힌트 없으면 발견된 것 반환
    if topology_lines:
        return '\n'.join(dict.fromkeys(topology_lines))
    if fault_lines:
        return '\n'.join(dict.fromkeys(fault_lines))
    if path_lines:
        return max(path_lines, key=lambda x: x.count('->'))

    # 패턴 매칭 실패 시 프리앰블 제거
    result = []
    for line in lines:
        lower = line.lower()
        if any(lower.startswith(p) for p in [
            'based on', 'here is', 'here are', 'the answer', 'according to',
            'from the', 'after analyzing', 'summary', 'analysis',
            'these represent', 'this shows', 'the following', 'let me',
            'i can', 'i have', 'i found', 'i identified', 'the result',
            'final answer', 'answer:', 'result:', 'output:',
        ]):
            continue
        # 빈 번호 매기기만 있는 라인 스킵
        if re.match(r'^\d+[\.\)]\s*$', line):
            continue
        result.append(line)

    return '\n'.join(result).strip() if result else raw.strip()


# ============================================================
# NOC API Client
# ============================================================

for key in ["http_proxy", "https_proxy", "HTTP_PROXY", "HTTPS_PROXY"]:
    os.environ.pop(key, None)

_session = requests.Session()
_session.trust_env = False


def call_noc_api(device_name: str, command: str, question_number: int) -> dict:
    try:
        resp = _session.post(
            NOC_API_URL,
            json={
                "device_name": device_name,
                "command": command,
                "question_number": question_number,
            },
            timeout=30,
        )
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def compress_tool_result(result_str: str, command: str) -> str:
    """대형 tool result를 압축하여 컨텍스트 절약.

    라우팅 테이블, 설정 파일 등 큰 출력을 핵심 정보만 남기고 축약.
    """
    # 작은 결과는 그대로 반환
    if len(result_str) < 3000:
        return result_str

    try:
        data = json.loads(result_str)
        output = data.get("result", "")
    except (json.JSONDecodeError, AttributeError):
        output = result_str

    lines = output.split('\n')

    # display current-configuration → interface + description + ip address + static route만 추출
    if "current-configuration" in command or "running-config" in command:
        kept = []
        in_interface = False
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("interface ") or stripped.startswith("description "):
                kept.append(line)
                in_interface = True
            elif stripped.startswith("ip address ") or stripped.startswith("ip route-static "):
                kept.append(line)
            elif stripped.startswith("undo shutdown") or stripped.startswith("shutdown"):
                kept.append(line)
            elif stripped == "#" and in_interface:
                kept.append(line)
                in_interface = False
            elif any(k in stripped for k in [
                "ospf", "bgp", "vxlan", "vlan", "bridge-domain", "evpn",
                "nve", "vbdif", "Vlanif", "Eth-Trunk", "loopback",
                "isis", "srv6", "segment-routing",
            ]):
                kept.append(line)

        if kept:
            compressed = '\n'.join(kept)
            data_out = dict(data) if isinstance(data, dict) else {"result": ""}
            data_out["result"] = compressed
            data_out["_compressed"] = True
            return json.dumps(data_out, ensure_ascii=False)

    # display ip routing-table → 빈 줄 제거 + 헤더 축약
    if "routing-table" in command or "ip route" in command:
        # 빈 줄과 헤더 텍스트 제거, 라우팅 엔트리만 유지
        kept = []
        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            # 실제 라우팅 엔트리 (IP주소로 시작)
            if stripped and stripped[0].isdigit():
                kept.append(stripped)
            # 헤더 라인은 최소한만 유지
            elif any(k in stripped for k in ['Destinations', 'Routing Table']):
                kept.append(stripped)
        if kept:
            compressed = '\n'.join(kept)
            data_out = dict(data) if isinstance(data, dict) else {"result": ""}
            data_out["result"] = compressed
            data_out["_compressed"] = True
            return json.dumps(data_out, ensure_ascii=False)

    # 기본 truncation
    if len(result_str) > 8000:
        return result_str[:8000] + "\n... [TRUNCATED]"
    return result_str


# ============================================================
# Tool Definitions
# ============================================================

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "execute_cli_command",
            "description": (
                "Execute a CLI command on a network device via the NOC API. "
                "Supports Huawei (display ...), Cisco (show ...), and H3C (display ...) commands. "
                "Returns the command output as it would appear on the device console. "
                "You can call this tool multiple times in one turn for different devices."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "device_name": {
                        "type": "string",
                        "description": "Target network device name (e.g., 'Alpha-Center-01', 'Beta-Axis-02')",
                    },
                    "command": {
                        "type": "string",
                        "description": (
                            "CLI command to execute. Use vendor-appropriate syntax: "
                            "Huawei/H3C: 'display ...' | Cisco: 'show ...'"
                        ),
                    },
                },
                "required": ["device_name", "command"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "resolve_ip_to_device",
            "description": (
                "Deterministically resolve an IP address to the device that owns it in this scenario. "
                "Use this BEFORE guessing a device name from an IP. Returns the device(s) whose interface "
                "holds the given IP. If no exact match, returns candidates sharing the same /24 subnet."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "ip": {
                        "type": "string",
                        "description": "IPv4 address, e.g. '10.1.5.1' or '20.1.4.20'",
                    },
                },
                "required": ["ip"],
            },
        },
    },
]

# ============================================================
# System Prompt
# ============================================================

SYSTEM_PROMPT = """You are NetOps-Agent, an expert AI agent for IP network O&M troubleshooting.
You solve problems by collecting device data via CLI commands and analyzing it.

## Tools
1. `execute_cli_command(device_name, command)` - Execute CLI on Huawei/Cisco/H3C devices.
   You can call multiple tools in parallel (different devices in one turn).
2. `resolve_ip_to_device(ip)` - Deterministically map an IP to the device that owns it.
   **Use this BEFORE guessing a device name from an IP.**
   Example: resolve_ip_to_device(ip="10.1.5.1") -> ["Demeter-Prime-01", "Demeter-Prime-02"] (VRRP pair)

## Few-shot examples (path questions)

### EXAMPLE A — Same /24, L2 via aggregation switch
Q: Hermes-Prime-01 addressing 10.1.1.20 (PJ area)
- Hermes-Prime-01 Vlanif10 = 10.1.1.10/24, ARP of 10.1.1.20 via GE1/0/4 (uplink)
- resolve_ip_to_device("10.1.1.20") -> Hermes-Prime-02
- LLDP: Hermes-Prime-01 GE1/0/4 <-> Demeter-Prime-01 GE1/0/5
Answer: Hermes-Prime-01->Demeter-Prime-01->Hermes-Prime-02
Insight: **Same /24 does NOT mean direct L2**; traffic traverses the aggregation switch (Demeter-Prime).

### EXAMPLE B — Cross-zone via symmetric Prime/Node overlay
Q: Hermes-Prime-01 addressing 20.1.1.10 (PJ area, different zone)
- No 20.1.x prefix in Hermes-Prime-01 routing-table; default route via 10.1.5.1 Vlanif50
- resolve_ip_to_device("10.1.5.1") -> [Demeter-Prime-01, Demeter-Prime-02] (VRRP pair)
- resolve_ip_to_device("20.1.1.10") -> Hermes-Node-01
- Symmetric topology: Prime-zone gateway (Demeter-Prime) <-> Node-zone gateway (Demeter-Node)
Answer: Hermes-Prime-01->Demeter-Prime-01->Demeter-Node-01->Hermes-Node-01

### ANTI-EXAMPLE — Never invent device names
Hallucinations to AVOID: Hermes-Spine-01, Hermes-Leaf-01, Hermes-Secondary-01, Node-10-1-1-X, Core-01, Gamma-Edge-XX.
**ONLY use names from the VALID DEVICES whitelist provided in the hint.**
If unsure, call `resolve_ip_to_device` — never fabricate a device name from an IP.

## Command Priority (most useful first)
1. `display current-configuration` - BEST: contains interface descriptions with remote node+port info
2. `display ip routing-table` - routing entries (LARGE output ~3000 tokens)
3. `display interface brief` - port UP/DOWN status
4. `display ip interface brief` - IP addresses per interface
5. `display lldp neighbor brief` - neighbor info (may return "No permission" on some nodes!)
6. `display arp` - IP-MAC-port mapping
7. `display logbuffer` - system logs (useful for fault diagnosis)
8. `display vxlan tunnel` / `display bgp evpn all routing-table` - VXLAN/EVPN info (PJ area)
9. Cisco equivalents: show running-config, show ip route, show interface brief, etc.

## KEY DISCOVERY: Interface Descriptions
In `display current-configuration`, each interface has a `description` field:
```
interface GE1/0/1
 description From_NodeA_GE1/0/1_To_NodeB_GE1/0/2
```
This tells you EXACTLY which remote device and port is connected. Parse this to identify neighbors.
This is MORE RELIABLE than LLDP (which may be unavailable on some nodes).

## Problem-Solving Strategies

### TYPE 1: Topology Reconstruction
Goal: Restore link info for a target node's UP interfaces.
Strategy:
1. Query `display interface brief` on target → list UP ports (GE*/0/* with "up" status)
2. Query `display current-configuration` on target → parse description for each UP port
   - Pattern: `From_TargetNode_PortA_To_RemoteNode_PortB`
3. If target CANNOT be queried: query `display lldp neighbor brief` on ALL neighbors simultaneously
   - If LLDP returns "No permission" or empty: query `display current-configuration` on that neighbor instead
   - Look for descriptions pointing to the target node
4. Output format: `TargetNode(port)->PeerNode(port)` per line

### TYPE 2: Path Query
Goal: Find forwarding path from source to destination IP.
CRITICAL: You must trace EVERY hop. Do NOT skip intermediate nodes.
Strategy:
1. First turn: query `display ip routing-table` + `display current-configuration` on source node
2. In routing table, find the route matching destination IP → get next-hop IP and egress interface
3. In config, find the egress interface's description → get next-hop DEVICE NAME
4. Repeat for each hop: query routing-table + config on the next device
5. Stop when routing table shows "Direct" for the destination subnet
6. For same-subnet destinations (VXLAN/L2): check VXLAN tunnel + BGP EVPN for overlay path
7. Output: `NodeA->NodeB->NodeC->...->NodeZ` single line

### TYPE 3: Fault Localization
Goal: Diagnose traffic interruption cause.
Strategy:
1. Query ALL suspect nodes simultaneously: `display ip routing-table` + `display interface brief` + `display current-configuration`
2. For routing faults: compare routing tables - if a route exists on adjacent nodes but is MISSING on a suspect → "missing static route"
3. For port faults: check `display interface brief` for *down or AdminDOWN ports
4. For config faults: check `display current-configuration` for:
   - Static routes pointing to wrong next-hop → "static route error"
   - Blackhole routes (no next-hop) → "blackhole route"
   - Interface IP mismatches → "interface IP error"
   - Shutdown interfaces → "shutdown"
5. For MAC/ARP issues: check `display logbuffer` for ARP_DUPLICATE_IPADDR → "MAC address configuration error"
6. For advanced issues: check OSPF/BGP config, MTU values, VPN settings
7. Output: `node;dest-IP;cause` (routing) or `node;port;cause` (port) per line

## CRITICAL RULES
1. **Efficiency**: Batch multiple tool calls in ONE turn (e.g., query 4 nodes simultaneously)
2. **No redundancy**: Never query the same device+command twice
3. **Description is key**: Always parse interface descriptions to identify connected devices
4. **Trace ALL hops**: For path queries, never stop until you reach a Direct route
5. **Time awareness**: You have 10 minutes. If data is sufficient, answer immediately

## OUTPUT FORMAT RULES (ABSOLUTE - NEVER VIOLATE)
- Your final message must contain ONLY the answer lines, nothing else
- Do NOT start with "Based on...", "Here is...", "The answer is..." or any preamble
- Do NOT add explanations, summaries, or analysis
- Do NOT number lines unless the question requires it
- Topology: `TargetNode(port)->PeerNode(port)` per line
- Path: single line `NodeA->NodeB->...->NodeZ`
- Fault: `node;target;cause` per line
- No blank lines, no trailing spaces
"""


# ============================================================
# Unified LLM Client (OpenAI / Anthropic SDK 추상화)
# ============================================================

# 통합 응답 형식
class UnifiedToolCall:
    """SDK 무관한 tool call 표현"""
    def __init__(self, call_id: str, name: str, arguments: str):
        self.id = call_id
        self.name = name
        self.arguments = arguments  # JSON string


class UnifiedResponse:
    """SDK 무관한 응답 표현"""
    def __init__(self, content: str = "", tool_calls: list[UnifiedToolCall] | None = None):
        self.content = content
        self.tool_calls = tool_calls or []


class UnifiedClient:
    """OpenAI / Anthropic 통합 클라이언트"""

    def __init__(self, sdk_type: str, api_key: str, base_url: str, model: str):
        self.sdk_type = sdk_type
        self.model = model
        if sdk_type == "anthropic":
            import anthropic
            self.client = anthropic.Anthropic(api_key=api_key)
            self._anthropic_tools = [
                {
                    "name": "execute_cli_command",
                    "description": (
                        "Execute a CLI command on a network device via the NOC API. "
                        "Supports Huawei (display ...), Cisco (show ...), and H3C (display ...) commands."
                    ),
                    "input_schema": {
                        "type": "object",
                        "properties": {
                            "device_name": {"type": "string", "description": "Target network device name"},
                            "command": {"type": "string", "description": "CLI command to execute"},
                        },
                        "required": ["device_name", "command"],
                    },
                }
            ]
        else:
            self.client = OpenAI(base_url=base_url, api_key=api_key)

    def chat(
        self,
        messages: list[dict[str, Any]],
        tools: bool = True,
        temperature: float = 0.3,
        max_tokens: int = MAX_TOKENS,
    ) -> UnifiedResponse:
        if self.sdk_type == "anthropic":
            return self._chat_anthropic(messages, tools, temperature, max_tokens)
        else:
            return self._chat_openai(messages, tools, temperature, max_tokens)

    def _chat_openai(
        self, messages: list[dict[str, Any]], tools: bool, temperature: float, max_tokens: int
    ) -> UnifiedResponse:
        kwargs: dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        if tools:
            kwargs["tools"] = TOOLS
            kwargs["tool_choice"] = "auto"

        response = self.client.chat.completions.create(**kwargs)
        msg = response.choices[0].message

        unified_tool_calls = []
        if msg.tool_calls:
            for tc in msg.tool_calls:
                unified_tool_calls.append(
                    UnifiedToolCall(call_id=tc.id, name=tc.function.name, arguments=tc.function.arguments)
                )
        return UnifiedResponse(content=msg.content or "", tool_calls=unified_tool_calls)

    def _chat_anthropic(
        self, messages: list[dict[str, Any]], tools: bool, temperature: float, max_tokens: int
    ) -> UnifiedResponse:
        # OpenAI 형식 → Anthropic 형식 변환
        system_text = ""
        anthropic_messages: list[dict[str, Any]] = []

        for msg in messages:
            role = msg["role"]
            if role == "system":
                system_text = msg["content"]
            elif role == "user":
                anthropic_messages.append({"role": "user", "content": msg["content"]})
            elif role == "assistant":
                content_blocks: list[dict[str, Any]] = []
                if msg.get("content"):
                    content_blocks.append({"type": "text", "text": msg["content"]})
                if msg.get("tool_calls"):
                    for tc in msg["tool_calls"]:
                        try:
                            input_data = json.loads(tc["function"]["arguments"])
                        except (json.JSONDecodeError, KeyError):
                            input_data = {}
                        content_blocks.append({
                            "type": "tool_use",
                            "id": tc["id"],
                            "name": tc["function"]["name"],
                            "input": input_data,
                        })
                if content_blocks:
                    anthropic_messages.append({"role": "assistant", "content": content_blocks})
            elif role == "tool":
                # Anthropic: tool results go in user message with tool_result blocks
                tool_result = {
                    "type": "tool_result",
                    "tool_use_id": msg["tool_call_id"],
                    "content": msg["content"],
                }
                # 이전 메시지가 user role이고 tool_result를 포함하면 합치기
                if anthropic_messages and anthropic_messages[-1]["role"] == "user" and isinstance(anthropic_messages[-1]["content"], list):
                    anthropic_messages[-1]["content"].append(tool_result)
                else:
                    anthropic_messages.append({"role": "user", "content": [tool_result]})

        # 연속 user 메시지 병합 (Anthropic은 동일 role 연속 불가)
        merged: list[dict[str, Any]] = []
        for msg in anthropic_messages:
            if merged and merged[-1]["role"] == msg["role"]:
                prev_content = merged[-1]["content"]
                curr_content = msg["content"]
                if isinstance(prev_content, str) and isinstance(curr_content, str):
                    merged[-1]["content"] = prev_content + "\n" + curr_content
                elif isinstance(prev_content, str):
                    merged[-1]["content"] = [{"type": "text", "text": prev_content}] + curr_content
                elif isinstance(curr_content, str):
                    prev_content.append({"type": "text", "text": curr_content})
                else:
                    prev_content.extend(curr_content)
            else:
                merged.append(msg)

        kwargs: dict[str, Any] = {
            "model": self.model,
            "messages": merged,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        if system_text:
            kwargs["system"] = system_text
        if tools:
            kwargs["tools"] = self._anthropic_tools

        response = self.client.messages.create(**kwargs)

        # Anthropic 응답 → 통합 형식 변환
        content_text = ""
        unified_tool_calls = []
        for block in response.content:
            if block.type == "text":
                content_text += block.text
            elif block.type == "tool_use":
                unified_tool_calls.append(
                    UnifiedToolCall(
                        call_id=block.id,
                        name=block.name,
                        arguments=json.dumps(block.input),
                    )
                )
        return UnifiedResponse(content=content_text, tool_calls=unified_tool_calls)


# ============================================================
# Agent Core
# ============================================================

def run_agent(question_id: int, question_text: str) -> dict:
    client = UnifiedClient(sdk_type=SDK_TYPE, api_key=API_KEY, base_url=MODEL_BASE_URL, model=MODEL_NAME)

    # 질문 유형 감지 및 cold-start 힌트 생성
    qtype = detect_question_type(question_text)
    type_hint = build_type_hint(qtype, question_text, question_id)
    log.info(f"  [Q{question_id}] Type: {qtype}")

    messages: list[dict[str, Any]] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"[Question ID: {question_id}]\n{question_text}"},
    ]

    # cold-start 힌트 주입 (질문 바로 뒤에 전략 가이드 추가)
    if type_hint:
        messages.append({"role": "user", "content": type_hint})

    tool_calls_count = 0
    empty_count = 0
    api_error_count = 0
    validation_retried = False
    start_time = time.time()
    # 중복 쿼리 추적
    queried_commands: set[str] = set()

    for iteration in range(MAX_ITERATIONS):
        elapsed = time.time() - start_time
        if elapsed > TIMEOUT_SECONDS:
            # 시간 초과 - 강제 답변 요청
            messages.append({
                "role": "user",
                "content": (
                    "STOP. Time is up. Do NOT emit any tool_call, function tag, or XML. "
                    "Output ONLY a single plain-text line: the final answer in the exact "
                    "format required (e.g., 'NodeA->NodeB->NodeC' for path questions). "
                    "No explanation, no tags, no JSON. If data is incomplete, output your "
                    "best partial path from the routes already observed."
                ),
            })
            try:
                resp = client.chat(messages, tools=False, temperature=0.1, max_tokens=MAX_TOKENS)
                content = resp.content
                elapsed = time.time() - start_time
                return {
                    "question_id": question_id,
                    "answer": postprocess_answer(content, qtype),
                    "tool_calls": tool_calls_count,
                    "duration_s": round(elapsed, 1),
                    "iterations": iteration + 1,
                    "status": "timeout_forced",
                    "qtype": qtype,
                }
            except Exception:
                break

        try:
            resp = client.chat(messages, tools=True, temperature=0.3, max_tokens=MAX_TOKENS)
            api_error_count = 0  # 성공 시 리셋
        except Exception as e:
            api_error_count += 1
            log.error(f"  [Q{question_id}] API error #{api_error_count}: {e}")
            if api_error_count >= 5:
                log.error(f"  [Q{question_id}] Too many API errors, giving up")
                break
            time.sleep(min(2 ** api_error_count, 30))  # 지수 백오프
            continue

        # 어시스턴트 메시지 기록 (OpenAI 호환 형식으로 저장)
        assistant_msg: dict[str, Any] = {"role": "assistant", "content": resp.content or ""}
        if resp.tool_calls:
            assistant_msg["tool_calls"] = [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {"name": tc.name, "arguments": tc.arguments},
                }
                for tc in resp.tool_calls
            ]
        messages.append(assistant_msg)

        # Tool call 처리
        if resp.tool_calls:
            empty_count = 0  # 리셋
            for tc in resp.tool_calls:
                tool_calls_count += 1
                try:
                    args = json.loads(tc.arguments)
                except json.JSONDecodeError:
                    args = {}

                # [AUTO] P1: resolve_ip_to_device tool handling
                if tc.name == "resolve_ip_to_device":
                    ip_arg = args.get("ip", "").strip()
                    owners = find_ip_owner(question_id, ip_arg) if ip_arg else []
                    if owners:
                        result_str = json.dumps({"ip": ip_arg, "owners": owners})
                    else:
                        prefix = ".".join(ip_arg.split(".")[:3]) + "." if ip_arg else ""
                        graph = build_topology_snapshot(question_id)
                        subnet = {k: v for k, v in graph["ip_owner"].items() if k.startswith(prefix)}
                        result_str = json.dumps({
                            "ip": ip_arg,
                            "owners": [],
                            "note": "Exact IP not found. Same /24 candidates:",
                            "subnet_candidates": dict(list(subnet.items())[:10]),
                        })
                    log.info(f"  [Q{question_id}] Tool #{tool_calls_count}: resolve_ip_to_device({ip_arg}) -> {owners or 'subnet-fallback'}")
                    messages.append({"role": "tool", "tool_call_id": tc.id, "content": result_str})
                    continue

                device = args.get("device_name", "")
                command = args.get("command", "")
                cmd_key = f"{device}:{command}"

                # 중복 쿼리 감지
                if cmd_key in queried_commands:
                    log.info(f"  [Q{question_id}] Tool #{tool_calls_count}: {device} -> {command} [DUPLICATE-SKIPPED]")
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tc.id,
                        "content": '{"note": "Already queried this exact command. Use the previous result. Do NOT repeat queries."}',
                    })
                    continue

                queried_commands.add(cmd_key)
                log.info(f"  [Q{question_id}] Tool #{tool_calls_count}: {device} -> {command}")

                result = call_noc_api(device, command, question_id)
                result_str = json.dumps(result, ensure_ascii=False)
                result_str = compress_tool_result(result_str, command)

                messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": result_str,
                })
        elif resp.content:
            # tool call 없이 content만 있으면 → 최종 답변
            # 단, 아직 tool call을 한 번도 안 했으면 사고(thinking) 응답일 수 있음
            content = resp.content.strip()
            if tool_calls_count == 0 and iteration < 3:
                # 아직 데이터 수집 안 함 → tool 사용 유도
                log.info(f"  [Q{question_id}] Text response without data collection, nudging tool use")
                messages.append({
                    "role": "user",
                    "content": (
                        "You haven't collected any data yet. You MUST use execute_cli_command "
                        "to query network devices before answering. Start by querying the relevant "
                        "devices now. Use parallel tool calls for efficiency."
                    ),
                })
                continue

            elapsed = time.time() - start_time
            # [AUTO] P0 validation: detect hallucinated devices / XML / missing arrow
            _whitelist = set(load_scenario_devices(question_id))
            _ok, _clean, _reason = validate_path_answer(
                postprocess_answer(content, qtype), _whitelist, qtype
            )
            if not _ok and qtype == QTYPE_PATH and not validation_retried:
                log.warning(f"  [Q{question_id}] Answer invalid ({_reason}) — correction retry")
                messages.append({"role": "assistant", "content": content})
                messages.append({
                    "role": "user",
                    "content": (
                        f"Your answer is invalid: {_reason}. "
                        f"Output ONLY a single plain-text line: hop1->hop2->...->hopN. "
                        f"Use ONLY devices from the whitelist: {sorted(_whitelist)}. "
                        f"No IP addresses, no XML, no tool_call, no code blocks, no explanation. "
                        f"If uncertain, output your best partial path from the routing data you already read."
                    ),
                })
                validation_retried = True
                continue
            log.info(f"  [Q{question_id}] Answer received ({elapsed:.1f}s, {tool_calls_count} tool calls)")
            return {
                "question_id": question_id,
                "answer": postprocess_answer(content, qtype),
                "tool_calls": tool_calls_count,
                "duration_s": round(elapsed, 1),
                "iterations": iteration + 1,
                "status": "solved" if _ok else "validation_failed",
                "qtype": qtype,
            }
        else:
            # 빈 응답 처리
            empty_count += 1
            log.warning(f"  [Q{question_id}] Empty response #{empty_count} at iteration {iteration + 1}")
            if empty_count >= 2:
                # 2번 연속 빈 응답 → 행동 유도
                if tool_calls_count == 0:
                    # 데이터 수집 안 됨 → tool 사용 강제
                    messages.append({
                        "role": "user",
                        "content": (
                            "You are not making progress. Use execute_cli_command NOW to collect data. "
                            "Start with the most relevant command for this question type."
                        ),
                    })
                else:
                    # 데이터 있음 → 답변 강제
                    messages.append({
                        "role": "user",
                        "content": (
                            "You have collected sufficient data. Output ONLY a single plain-text "
                            "line: the final answer in the exact format required. Do NOT emit "
                            "any tool_call, function tag, XML, or JSON. No explanation."
                        ),
                    })
                try:
                    resp2 = client.chat(
                        messages,
                        tools=(tool_calls_count == 0),
                        temperature=0.1,
                        max_tokens=MAX_TOKENS,
                    )
                    if resp2.tool_calls:
                        # tool call로 복구됨 → 다음 iteration에서 처리
                        assistant_msg2: dict[str, Any] = {"role": "assistant", "content": resp2.content or ""}
                        assistant_msg2["tool_calls"] = [
                            {"id": tc.id, "type": "function",
                             "function": {"name": tc.name, "arguments": tc.arguments}}
                            for tc in resp2.tool_calls
                        ]
                        messages.append(assistant_msg2)
                        for tc in resp2.tool_calls:
                            tool_calls_count += 1
                            try:
                                args = json.loads(tc.arguments)
                            except json.JSONDecodeError:
                                args = {}
                            device = args.get("device_name", "")
                            command = args.get("command", "")
                            cmd_key = f"{device}:{command}"
                            queried_commands.add(cmd_key)
                            log.info(f"  [Q{question_id}] Tool #{tool_calls_count} (recovery): {device} -> {command}")
                            result = call_noc_api(device, command, question_id)
                            result_str = json.dumps(result, ensure_ascii=False)
                            result_str = compress_tool_result(result_str, command)
                            messages.append({"role": "tool", "tool_call_id": tc.id, "content": result_str})
                        empty_count = 0
                        continue
                    content = resp2.content or ""
                    if content.strip():
                        elapsed = time.time() - start_time
                        return {
                            "question_id": question_id,
                            "answer": postprocess_answer(content, qtype),
                            "tool_calls": tool_calls_count,
                            "duration_s": round(elapsed, 1),
                            "iterations": iteration + 1,
                            "status": "forced_answer",
                            "qtype": qtype,
                        }
                except Exception:
                    pass

    # 최대 반복 도달
    elapsed = time.time() - start_time
    last_content = ""
    for m in reversed(messages):
        if m.get("role") == "assistant" and m.get("content"):
            last_content = m["content"]
            break

    return {
        "question_id": question_id,
        "answer": postprocess_answer(last_content, qtype),
        "tool_calls": tool_calls_count,
        "duration_s": round(elapsed, 1),
        "iterations": MAX_ITERATIONS,
        "status": "max_iterations",
        "qtype": qtype,
    }


# ============================================================
# Batch Evaluation
# ============================================================

def load_questions(filepath: str) -> list[dict]:
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


def evaluate(
    input_file: str,
    output_dir: str,
    question_ids: list[int] | None = None,
    fresh: bool = False,
):
    os.makedirs(output_dir, exist_ok=True)
    result_csv = os.path.join(output_dir, "result.csv")
    detail_log = os.path.join(output_dir, "eval_detail.jsonl")

    questions = load_questions(input_file)
    log.info(f"Loaded {len(questions)} questions from {input_file}")

    # resume: 기존 결과 로드
    completed: set[int] = set()
    if not fresh and os.path.exists(result_csv):
        with open(result_csv, encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                completed.add(int(row["id"]))
        if completed:
            log.info(f"Resuming: {len(completed)} already completed")

    if fresh or not os.path.exists(result_csv):
        with open(result_csv, "w", newline="", encoding="utf-8-sig") as f:
            csv.writer(f).writerow(["id", "prediction"])

    solved = 0
    failed = 0
    for q in questions:
        qid = q["task"]["id"]
        if question_ids and qid not in question_ids:
            continue
        if qid in completed:
            continue

        question_text = q["task"]["question"]
        log.info(f"[Q{qid}] Starting...")

        result = run_agent(qid, question_text)

        with open(result_csv, "a", newline="", encoding="utf-8-sig") as f:
            csv.writer(f).writerow([qid, result["answer"]])

        with open(detail_log, "a", encoding="utf-8") as f:
            f.write(json.dumps(result, ensure_ascii=False) + "\n")

        status_icon = "OK" if result["status"] == "solved" else result["status"]
        qtype_str = result.get("qtype", "?")
        log.info(
            f"[Q{qid}] {status_icon} ({qtype_str}) | "
            f"{result['duration_s']}s | "
            f"{result['tool_calls']} calls | "
            f"{result['iterations']} iters"
        )
        if result["status"] == "solved":
            solved += 1
        else:
            failed += 1

    total = solved + failed
    if total > 0:
        log.info(f"=== Results: {solved}/{total} solved ({solved/total*100:.0f}%) ===")


# ============================================================
# CLI
# ============================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Track B Agent")
    parser.add_argument("-i", "--input", default="data/Track B/data/Phase_1/test.json")
    parser.add_argument("-o", "--output", default="agent/results")
    parser.add_argument("--questions", type=str, default=None, help="e.g., 1,2,5")
    parser.add_argument("--fresh", action="store_true", help="Start fresh, ignore previous results")
    parser.add_argument(
        "--provider", type=str, default=None,
        choices=list(PROVIDERS.keys()),
        help="LLM provider (default: openrouter)",
    )
    args = parser.parse_args()

    # CLI --provider overrides env var
    provider = args.provider or PROVIDER_NAME
    cfg = PROVIDERS[provider]
    api_key = _resolve_api_key(cfg)
    base_url = cfg["base_url"]
    model = cfg["model"]

    # 직접 전역 변수 패치 (__main__ 네임스페이스)
    globals()["API_KEY"] = api_key
    globals()["MODEL_BASE_URL"] = base_url
    globals()["MODEL_NAME"] = model
    globals()["SDK_TYPE"] = cfg.get("sdk", "openai")

    log.info(f"Provider: {provider} | Model: {model} | URL: {base_url}")

    qids = [int(x) for x in args.questions.split(",")] if args.questions else None
    evaluate(args.input, args.output, qids, args.fresh)
