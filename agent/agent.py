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

# .env 파일에서 환경변수 로드
_env_path = Path(__file__).resolve().parent.parent / ".env"
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
MAX_TOKENS = 4096
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


def build_type_hint(qtype: str, question_text: str) -> str:
    """질문 유형별 cold-start 힌트 생성 (user message로 주입)"""
    if qtype == QTYPE_TOPOLOGY:
        info = extract_topology_info(question_text)
        target = info["target"]
        neighbors = info["neighbors"]

        if info["can_query_target"] and target:
            return (
                f"STRATEGY: This is a TOPOLOGY question. Target node: {target}.\n"
                f"Step 1: Query `display lldp neighbor brief` and `display interface brief` on {target}.\n"
                f"Step 2: Cross-reference to build link list.\n"
                f"Output ONLY lines in format: {target}(port)->PeerNode(port)"
            )
        elif neighbors:
            neighbor_list = ", ".join(neighbors)
            return (
                f"STRATEGY: This is a TOPOLOGY question. Target: {target} (CANNOT query directly).\n"
                f"Known neighbors: {neighbor_list}\n"
                f"Step 1: Query `display lldp neighbor brief` on ALL neighbors simultaneously (batch tool calls).\n"
                f"Step 2: For each neighbor, look for {target} in LLDP output.\n"
                f"Step 3: If LLDP empty, fallback to `display arp` + `display interface brief`.\n"
                f"Output ONLY lines in format: {target}(port)->PeerNode(port)"
            )
        return ""

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
            f"\nStep 1: Get destination IP - query `display ip interface brief` on {dest or 'destination node'}."
            f"\nStep 2: On {source}, query `display ip routing-table` to find next-hop."
            f"\nStep 3: Trace hop-by-hop until destination reached."
            f"\nBatch tool calls: query routing tables on multiple nodes simultaneously."
            f"\nOutput ONLY one line: NodeA->NodeB->NodeC"
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
    }
]

# ============================================================
# System Prompt
# ============================================================

SYSTEM_PROMPT = """You are NetOps-Agent, an expert AI agent for IP network O&M troubleshooting.
You solve problems by collecting device data via CLI commands and analyzing it.

## Tool
`execute_cli_command(device_name, command)` - Execute CLI on Huawei/Cisco/H3C devices.
You can call multiple tools in parallel (different devices in one turn).

## Command Reference (use ONLY these)

### Huawei / H3C
display current-configuration | display logbuffer | display lldp neighbor brief
display interface brief | display ip interface brief | display ip routing-table
display arp | display ipv6 neighbors | display ospf peer | display ospf routing
display ospf lsdb | display bgp evpn all routing-table | display bgp vpnv4 all routing-table
display vxlan tunnel | display vrrp verbose | display bfd session all
display srv6-te policy status | display segment-routing ipv6 local-sid end forwarding

### Cisco
show running-config | show logging | show lldp neighbors
show ip interface brief | show interface brief | show ip route | show ip arp
show ip ospf neighbor | show ip route ospf | show ip ospf database
show bgp l2vpn evpn | show bgp vpnv4 unicast all
show nve vni | show nve peers | show vrrp detail | show bfd neighbors

### H3C-specific differences
display lldp neighbor-information (not neighbor brief) | display arp all (not arp)

## Problem-Solving Strategies

### TYPE 1: Topology Reconstruction
Goal: Restore link info for a target node's UP interfaces.
Strategy:
1. If you CAN query the target node: `display lldp neighbor brief` + `display interface brief`
2. If you CANNOT query the target node (stated in question):
   - Query LLDP on ALL listed neighbor nodes to find links to target
   - For each neighbor: `display lldp neighbor brief` → look for target node entries
   - If LLDP is empty on a neighbor, use fallback: check `display interface brief` for UP ports, then cross-reference with `display arp` and target node's ARP
3. Output format: `TargetNode(port)->PeerNode(port)` per line, no extra text

### TYPE 2: Path Query
Goal: Find forwarding path from source to destination IP.
Strategy:
1. Get destination IP from `display ip interface brief` on destination node
2. On source node: `display ip routing-table` → find matching route → next-hop IP
3. Identify next-hop device: check `display ip interface brief` on candidate devices
4. Repeat hop-by-hop until destination is directly connected
5. Output format: `NodeA->NodeB->NodeC` single line, no extra text

### TYPE 3: Fault Localization
Goal: Diagnose traffic interruption cause.
Strategy:
1. Start from source node: `display ip routing-table` for destination route
2. Trace hop-by-hop, checking each node's routing table
3. Check for: missing routes, blackhole routes, incorrect static routes, shutdown ports
4. Use `display current-configuration` to verify static route config
5. Use `display interface brief` to check port status (UP/DOWN/AdminDOWN)
6. Routing faults: `node;dest-IP;cause` | Port faults: `node;port;cause`

## CRITICAL RULES
1. **Efficiency**: Batch multiple tool calls in ONE turn when possible (e.g., query LLDP on 4 nodes simultaneously)
2. **No redundancy**: Never query the same device+command twice
3. **Format compliance**: Output ONLY the final answer in the EXACT format the question requires
4. **No explanation**: Do NOT include reasoning, analysis, or extra text in the answer
5. **Time awareness**: You have 10 minutes. If data is sufficient, answer immediately
6. **Error handling**: If a command returns error/empty, try alternative commands or skip
7. **Vendor detection**: Determine vendor from device name patterns or question context

## OUTPUT FORMAT RULES (ABSOLUTE - NEVER VIOLATE)
- Your final message must contain ONLY the answer lines, nothing else
- Do NOT start with "Based on...", "Here is...", "The answer is...", or any preamble
- Do NOT add explanations, summaries, or analysis after the answer
- Do NOT number the lines (1., 2., etc.) unless the question explicitly requires it
- For topology: each line is `TargetNode(port)->PeerNode(port)` and NOTHING else
- For path: single line `NodeA->NodeB->NodeC` and NOTHING else
- For fault: each line is `node;target;cause` and NOTHING else
- No blank lines at start or end
- No trailing spaces or extra whitespace
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
    type_hint = build_type_hint(qtype, question_text)
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
                    "TIME IS ALMOST UP. Based on ALL data collected so far, "
                    "provide your FINAL ANSWER NOW. Output ONLY the answer "
                    "in the exact format required. No explanation."
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

                if len(result_str) > 12000:
                    result_str = result_str[:12000] + "\n... [TRUNCATED]"

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
            log.info(f"  [Q{question_id}] Answer received ({elapsed:.1f}s, {tool_calls_count} tool calls)")
            return {
                "question_id": question_id,
                "answer": postprocess_answer(content, qtype),
                "tool_calls": tool_calls_count,
                "duration_s": round(elapsed, 1),
                "iterations": iteration + 1,
                "status": "solved",
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
                            "You have collected sufficient data. Provide your FINAL ANSWER NOW. "
                            "Output ONLY the answer in the exact format required. No explanation."
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
                            if len(result_str) > 12000:
                                result_str = result_str[:12000] + "\n... [TRUNCATED]"
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
