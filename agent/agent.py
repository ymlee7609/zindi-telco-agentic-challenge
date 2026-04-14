#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Track B Agent: IP Network Troubleshooting Agent
HuggingFace Inference API (novita) + Qwen3.5-35B-A3B
"""

import argparse
import csv
import json
import logging
import os
import time
from typing import Any

import requests
from openai import OpenAI

# ============================================================
# Configuration
# ============================================================

HF_TOKEN = os.environ.get("HF_TOKEN", "")
if not HF_TOKEN:
    token_path = os.path.expanduser("~/.cache/huggingface/token")
    if os.path.exists(token_path):
        with open(token_path) as f:
            HF_TOKEN = f.read().strip()

MODEL_BASE_URL = "https://router.huggingface.co/novita/v3/openai"
MODEL_NAME = "qwen/qwen3.5-35b-a3b"

NOC_API_URL = "http://127.0.0.1:7860/api/agent/execute"
MAX_ITERATIONS = 30
MAX_TOKENS = 16000
TIMEOUT_SECONDS = 540  # 9분 - 안전 마진

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("agent")

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
"""


# ============================================================
# Agent Core
# ============================================================

def run_agent(question_id: int, question_text: str) -> dict:
    client = OpenAI(base_url=MODEL_BASE_URL, api_key=HF_TOKEN)

    messages: list[dict[str, Any]] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"[Question ID: {question_id}]\n{question_text}"},
    ]

    tool_calls_count = 0
    empty_count = 0
    start_time = time.time()

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
                response = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=messages,
                    max_tokens=MAX_TOKENS,
                    temperature=0.1,
                )
                content = response.choices[0].message.content or ""
                elapsed = time.time() - start_time
                return {
                    "question_id": question_id,
                    "answer": content.strip(),
                    "tool_calls": tool_calls_count,
                    "duration_s": round(elapsed, 1),
                    "iterations": iteration + 1,
                    "status": "timeout_forced",
                }
            except Exception:
                break

        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                tools=TOOLS,
                tool_choice="auto",
                max_tokens=MAX_TOKENS,
                temperature=0.3,
            )
        except Exception as e:
            log.error(f"  [Q{question_id}] API error: {e}")
            time.sleep(2)
            continue

        msg = response.choices[0].message

        # 어시스턴트 메시지 기록
        assistant_msg: dict[str, Any] = {"role": "assistant", "content": msg.content or ""}
        if msg.tool_calls:
            assistant_msg["tool_calls"] = [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {"name": tc.function.name, "arguments": tc.function.arguments},
                }
                for tc in msg.tool_calls
            ]
        messages.append(assistant_msg)

        # Tool call 처리
        if msg.tool_calls:
            empty_count = 0  # 리셋
            for tc in msg.tool_calls:
                tool_calls_count += 1
                try:
                    args = json.loads(tc.function.arguments)
                except json.JSONDecodeError:
                    args = {}

                device = args.get("device_name", "")
                command = args.get("command", "")
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
        elif msg.content:
            # 최종 답변
            elapsed = time.time() - start_time
            log.info(f"  [Q{question_id}] Answer received ({elapsed:.1f}s, {tool_calls_count} tool calls)")
            return {
                "question_id": question_id,
                "answer": msg.content.strip(),
                "tool_calls": tool_calls_count,
                "duration_s": round(elapsed, 1),
                "iterations": iteration + 1,
                "status": "solved",
            }
        else:
            # 빈 응답 처리
            empty_count += 1
            log.warning(f"  [Q{question_id}] Empty response #{empty_count} at iteration {iteration + 1}")
            if empty_count >= 3:
                # 3번 연속 빈 응답 → 강제 답변 요청
                messages.append({
                    "role": "user",
                    "content": (
                        "You must provide an answer now. Based on the data collected, "
                        "output ONLY the final answer in the required format. "
                        "Do not call any more tools."
                    ),
                })
                try:
                    response = client.chat.completions.create(
                        model=MODEL_NAME,
                        messages=messages,
                        max_tokens=MAX_TOKENS,
                        temperature=0.1,
                    )
                    content = response.choices[0].message.content or ""
                    if content:
                        elapsed = time.time() - start_time
                        return {
                            "question_id": question_id,
                            "answer": content.strip(),
                            "tool_calls": tool_calls_count,
                            "duration_s": round(elapsed, 1),
                            "iterations": iteration + 1,
                            "status": "forced_answer",
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
        "answer": last_content.strip(),
        "tool_calls": tool_calls_count,
        "duration_s": round(elapsed, 1),
        "iterations": MAX_ITERATIONS,
        "status": "max_iterations",
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
        log.info(
            f"[Q{qid}] {status_icon} | "
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
    args = parser.parse_args()

    qids = [int(x) for x in args.questions.split(",")] if args.questions else None
    evaluate(args.input, args.output, qids, args.fresh)
