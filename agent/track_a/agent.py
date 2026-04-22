#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Track A Qwen3.5-35B-A3B Agent.

Track A main.py 의 Environment / tool 인터페이스를 재사용하고, LLM 호출은
OpenRouter (Qwen) 을 사용. System prompt + few-shot 은 prompts.py 에 분리.

Usage:
    python agent/track_a/agent.py --max-samples 10 --save-dir agent/track_a/results_smoke/
    python agent/track_a/agent.py --provider openrouter --max-samples 50 --save-dir agent/track_a/results_pilot/
    python agent/track_a/agent.py --resume --max-samples 250 --start-idx 50 --save-dir agent/track_a/results_batch_a/
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import os
import re
import sys
import time
import traceback
from pathlib import Path
from typing import Any

import httpx
import requests

# load .env at repo root
_repo_root = Path(__file__).resolve().parents[2]
_env_path = _repo_root / ".env"
if _env_path.exists():
    with open(_env_path) as _f:
        for _line in _f:
            _line = _line.strip()
            if _line and not _line.startswith("#") and "=" in _line:
                _key, _, _val = _line.partition("=")
                os.environ.setdefault(_key.strip(), _val.strip())

# import Track A provided modules from data/Track A/
_track_a_src = _repo_root / "data" / "Track A"
sys.path.insert(0, str(_track_a_src))
from _types import ToolCall  # noqa: E402
from utils import extract_answer, extract_answer_all, compute_score  # noqa: E402

# import prompts from the same package directory
sys.path.insert(0, str(Path(__file__).resolve().parent))
from prompts import SYSTEM_PROMPT, FEW_SHOT_EXAMPLES, forced_answer_prompt  # noqa: E402
from rag import retrieve_similar, format_few_shot_from_retrieval  # noqa: E402

from openai import OpenAI, RateLimitError, APIConnectionError, APITimeoutError, APIError  # noqa: E402


# ---------------------------------------------------------------------------
# Provider config (포팅: Track B agent.py 의 PROVIDERS)
# ---------------------------------------------------------------------------

PROVIDERS = {
    "openrouter": {
        "base_url": "https://openrouter.ai/api/v1",
        "model": "qwen/qwen3.5-35b-a3b",
        "env_key": "OPENROUTER_API_KEY",
    },
    "huggingface": {
        "base_url": "https://router.huggingface.co/novita/v3/openai",
        "model": "qwen/qwen3.5-35b-a3b",
        "env_key": "HF_TOKEN",
    },
    "dashscope": {
        "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "model": "qwen3.5-flash",
        "env_key": "DASHSCOPE_API_KEY",
    },
    "groq": {
        "base_url": "https://api.groq.com/openai/v1",
        "model": "llama-3.3-70b-versatile",
        "env_key": "GROQ_API_KEY",
    },
    "local": {
        "base_url": "http://localhost:8000/v1",
        "model": "Qwen/Qwen3.5-35B-A3B",
        "env_key": "",
    },
}


def _resolve_api_key(cfg: dict) -> str:
    key = cfg.get("env_key", "")
    if key:
        v = os.environ.get(key, "")
        if v:
            return v
    return "EMPTY"


# ---------------------------------------------------------------------------
# Environment (Track A main.py 의 Environment 재사용 — 동일 endpoint_mapper)
# ---------------------------------------------------------------------------

ENDPOINT_MAPPER = {
    "get_all_scenario": "/scenario/all",
    "get_config_data": "/config-data",
    "get_user_plane_data": "/user-plane-data",
    "get_throughput_logs": "/throughput-logs",
    "get_cell_info": "/cell-info",
    "get_gnodeb_location": "/gnodeb-location",
    "get_user_location": "/user-location",
    "get_serving_cell_pci": "/serving-cell-pci",
    "get_serving_cell_rsrp": "/serving-cell-rsrp",
    "get_serving_cell_sinr": "/serving-cell-sinr",
    "get_rbs_allocated_to_user": "/rbs-allocated-to-user",
    "get_neighboring_cells_pci": "/neighboring-cells-pci",
    "get_neighboring_cell_rsrp": "/neighboring-cell-rsrp",
    "get_signaling_plane_event_log": "/signaling-plane-event-log",
    "get_all_cells_pci": "/all-cells-pci",
    "get_available_tools": "/tools",
    "health": "/health",
    "judge_mainlobe_or_not": "/judge_mainlobe",
    "calculate_horizontal_angle": "/calculate_horizontal_angle",
    "calculate_tilt_angle": "/calculate_tilt_angle",
    "calculate_pathloss": "/calculate_pathloss",
    "calculate_overlap_ratio": "/calculate_overlap_ratio",
    "get_kpi_data": "/get_kpi_data",
    "get_mr_data": "/get_mr_data",
    "optimize_antenna_gain": "/optimize_antenna_gain",
}


class Environment:
    def __init__(self, server_url: str, timeout: float = 15.0) -> None:
        self.server_url = server_url.rstrip("/")
        self.timeout = timeout

    def _call(self, name: str, scenario_id: str | None = None, **params: Any) -> Any:
        ep = ENDPOINT_MAPPER.get(name)
        if ep is None:
            return {"error": f"Unknown tool '{name}'"}
        url = f"{self.server_url}{ep}"
        headers = {"Content-Type": "application/json"}
        if scenario_id:
            headers["X-Scenario-Id"] = scenario_id
        r: requests.Response | None = None
        try:
            r = requests.get(url, params=params, headers=headers, timeout=self.timeout)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.HTTPError:
            detail = ""
            if r is not None:
                try:
                    detail = r.json().get("detail", r.text)
                except Exception:
                    detail = r.text
            return {"error": detail}
        except Exception as e:
            return {"error": str(e)}

    def get_tools(self) -> list[dict]:
        t = self._call("get_available_tools")
        return t if isinstance(t, list) else []

    def get_scenarios(self) -> list[dict]:
        s = self._call("get_all_scenario")
        return s if isinstance(s, list) else []

    def execute(self, tool_call: ToolCall, scenario_id: str | None = None) -> str:
        try:
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments or "{}")
            result = self._call(name, scenario_id=scenario_id, **args)
            return json.dumps(result, ensure_ascii=False)
        except json.JSONDecodeError:
            return json.dumps({"error": f"Tool parameter parsing failed: {tool_call.function.arguments}"}, ensure_ascii=False)
        except Exception as e:
            return json.dumps({"error": f"Tool invocation failed: {e}"}, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

log = logging.getLogger("track_a")


class QwenRunner:
    def __init__(
        self,
        env: Environment,
        provider: str,
        model_override: str | None,
        max_tokens: int,
        max_iterations: int,
        max_retries: int = 3,
        use_rag: bool = True,
        rag_k: int = 3,
    ) -> None:
        self.env = env
        cfg = PROVIDERS[provider]
        self.base_url = cfg["base_url"]
        self.model = model_override or cfg["model"]
        self.api_key = _resolve_api_key(cfg)
        self.max_tokens = max_tokens
        self.max_iterations = max_iterations
        self.max_retries = max_retries
        self.use_rag = use_rag
        self.rag_k = rag_k
        self.client = OpenAI(
            base_url=self.base_url,
            api_key=self.api_key,
            http_client=httpx.Client(verify=False, timeout=600.0),
        )

    def _call_model(self, messages: list[dict], tools: list[dict] | None,
                    temperature: float = 0.0):
        kwargs: dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "max_tokens": self.max_tokens,
            "temperature": temperature,
        }
        if tools:
            kwargs["tools"] = tools
            kwargs["tool_choice"] = "auto"

        base_wait = 1.0
        for attempt in range(1, self.max_retries + 1):
            try:
                resp = self.client.chat.completions.create(**kwargs)
                return resp.choices[0].message
            except (RateLimitError, APIConnectionError, APITimeoutError, APIError) as e:
                status = getattr(e, "status_code", None)
                if status and 400 <= status < 500 and status != 429:
                    log.error("Non-retriable API error %s: %s", status, e)
                    return None
                if attempt == self.max_retries:
                    log.error("Final API failure after %s attempts: %s", self.max_retries, e)
                    return None
                wait = base_wait * (2 ** (attempt - 1))
                log.warning("API retry %s/%s in %.1fs: %s", attempt, self.max_retries, wait, e)
                time.sleep(wait)
            except Exception as e:
                log.error("Unhandled API exception: %s\n%s", e, traceback.format_exc())
                return None
        return None

    def run(self, scenario: dict, temperature: float = 0.0) -> dict:
        sid = scenario.get("scenario_id")
        task = scenario.get("task", {})
        options = task.get("options", [])
        opts_block = "\n".join(f"{o['id']}:{o['label']}" for o in options)
        question = f"{task.get('description', '')}\nOptions:\n{opts_block}"

        tool_defs = self.env.get_tools()
        if not tool_defs:
            return {"scenario_id": sid, "status": "unresolved", "reason": "No tools"}

        messages: list[dict] = [{"role": "system", "content": SYSTEM_PROMPT}]
        # Static few-shot (P1/P3/P5 exemplars)
        messages.extend(FEW_SHOT_EXAMPLES)
        # Dynamic RAG few-shot: top-k similar train scenarios (same-tag filter)
        rag_info: list[dict] = []
        if self.use_rag:
            try:
                rag_info = retrieve_similar(scenario, k=self.rag_k,
                                            same_tag_only=True,
                                            exclude_sid=sid)
                rag_messages = format_few_shot_from_retrieval(rag_info)
                messages.extend(rag_messages)
            except Exception as e:
                log.warning("RAG retrieval failed: %s", e)
                rag_info = []
        messages.append({"role": "user", "content": question})

        tool_calls_log: list[dict] = []
        num_tool_calls = 0
        status: str | None = None
        reason: str | None = None
        last_msg = None
        i = 0

        for i in range(self.max_iterations):
            msg = self._call_model(messages, tools=tool_defs, temperature=temperature)
            if msg is None:
                continue
            last_msg = msg
            messages.append({"role": "assistant", "content": msg.content or "", "tool_calls": msg.tool_calls})

            if msg.tool_calls:
                num_tool_calls += len(msg.tool_calls)
                for j, tc in enumerate(msg.tool_calls):
                    result = self.env.execute(tc, scenario_id=sid)
                    messages.append({"role": "tool", "content": result, "tool_call_id": tc.id})
                    tool_calls_log.append(
                        {
                            "turn": i + 1,
                            "order": j + 1,
                            "function_name": tc.function.name,
                            "arguments": tc.function.arguments,
                            "has_failed": "error" in result,
                        }
                    )
            elif msg.content:
                content = msg.content
                # XML tool_call 오염 감지: Qwen 이 content 에 <tool_call>/<function=> 를 작성하는 경우
                xml_polluted = ("<tool_call>" in content or "<function=" in content)
                has_boxed = ("\\boxed" in content)
                if xml_polluted and not has_boxed:
                    # 오염 감지 → 재질의 (iteration 계속)
                    messages.append({
                        "role": "user",
                        "content": (
                            "Your previous response contained inline `<tool_call>` / `<function=...>` XML, "
                            "which this client IGNORES. "
                            "To call a tool, use the NATIVE tool_calls protocol (the API provides a "
                            "`tools` parameter — do not write XML). "
                            "To finalize your answer, END your message with \\boxed{C#} (single-answer) "
                            "or \\boxed{C#|C#|...} (multiple-answer, 2-4 IDs in ASCENDING order). "
                            "Please retry now."
                        ),
                    })
                    continue
                status = "solved"
                break
            else:
                status = "unresolved"
                reason = "Empty response from model"
                break

        if status is None:
            status = "unresolved"
            reason = f"Max iterations ({self.max_iterations}) reached"

        # free_mode forced answer if content is empty / missing \boxed{}
        last_answer = getattr(last_msg, "content", "") if last_msg else ""
        last_traces = getattr(last_msg, "reasoning_content", "") if last_msg else ""
        extracted = extract_answer(last_answer) or extract_answer(last_traces)
        if not extracted and last_msg is not None:
            tag = scenario.get("tag", "single-answer")
            forced = forced_answer_prompt(tag, opts_block)
            messages.append({"role": "user", "content": forced})
            msg2 = self._call_model(messages, tools=None, temperature=temperature)
            if msg2 is not None:
                last_msg = msg2
                last_answer = getattr(msg2, "content", "") or ""
                last_traces = getattr(msg2, "reasoning_content", "") or ""
                status = "solved"

        final_content = last_answer or last_traces
        return {
            "scenario_id": sid,
            "num_iterations": i + 1,
            "num_tool_calls": num_tool_calls,
            "tool_calls": tool_calls_log,
            "status": status,
            "reason": reason,
            "answer": final_content,
            "traces": last_traces,
            "rag_neighbors": rag_info,
        }


# ---------------------------------------------------------------------------
# Normalization of extracted answer
# ---------------------------------------------------------------------------

_ANSWER_RE = re.compile(r"\bC\d+\b")
_BOXED_RE = re.compile(r"\\boxed\{([^}]+)\}")


def normalize_answer(raw: str) -> str:
    """Produce the final prediction string.

    Priority:
      1. extract_answer_all (Track A util, expects \\boxed{...}) → '|'-joined
      2. regex \\boxed{...} fallback (util may miss edge cases)
      3. bare C## tokens scanned from raw text
    """
    if not raw:
        return ""
    v = extract_answer_all(raw) or ""
    if v:
        parts = [p for p in v.split("|") if p.strip()]
    else:
        boxed = _BOXED_RE.findall(raw)
        if boxed:
            parts = _ANSWER_RE.findall(boxed[-1])
        else:
            parts = _ANSWER_RE.findall(raw)
    if not parts:
        return ""
    dedup = list(dict.fromkeys(parts))
    try:
        dedup.sort(key=lambda s: int(s.lstrip("C")))
    except ValueError:
        pass
    return "|".join(dedup)


def insufficient_data_option(options: list[dict]) -> str:
    """Return the C# id whose label is the 'Insufficient data' fallback option.

    Each scenario has exactly one such option (pattern P7). If absent, return empty.
    """
    for opt in options:
        label = (opt.get("label") or "").lower()
        if "insufficient data" in label:
            return opt.get("id", "")
    return ""


def majority_vote(predictions: list[str], tag: str) -> str:
    """Vote across N self-consistency predictions.

    single-answer: pick most-voted single C# (tie = first)
    multi-answer: per-option voting. Keep options appearing in ceil(N/2)+
                  attempts; clamp to [2, 4] by top-count fallback. Ascending IDs.
    """
    from collections import Counter
    pred_sets = [
        [x.strip() for x in (p or "").split("|") if x.strip()]
        for p in predictions
    ]
    pred_sets = [s for s in pred_sets if s]
    if not pred_sets:
        return ""

    if tag == "single-answer":
        firsts = [s[0] for s in pred_sets]
        return Counter(firsts).most_common(1)[0][0]

    # multi
    opt_counts: Counter[str] = Counter()
    for s in pred_sets:
        for opt in s:
            opt_counts[opt] += 1
    n = len(pred_sets)
    threshold = (n + 1) // 2  # majority (ceil)
    winners = [o for o, c in opt_counts.items() if c >= threshold]
    if len(winners) < 2:
        winners = [o for o, _ in opt_counts.most_common(2)]
    elif len(winners) > 4:
        winners = [o for o, _ in opt_counts.most_common(4)]
    try:
        winners.sort(key=lambda s: int(s.lstrip("C")))
    except ValueError:
        pass
    return "|".join(winners)


# ---------------------------------------------------------------------------
# CLI / benchmark loop
# ---------------------------------------------------------------------------


def load_done(save_dir: Path) -> set[str]:
    csv_path = save_dir / "result.csv"
    if not csv_path.exists():
        return set()
    done: set[str] = set()
    with open(csv_path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            sid = row.get("scenario_id")
            if sid:
                done.add(sid)
    return done


def append_result(save_dir: Path, sid: str, pred: str) -> None:
    save_dir.mkdir(parents=True, exist_ok=True)
    csv_path = save_dir / "result.csv"
    new_file = not csv_path.exists()
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(["scenario_id", "prediction"])
        w.writerow([sid, pred])


def append_eval_detail(save_dir: Path, detail: dict) -> None:
    save_dir.mkdir(parents=True, exist_ok=True)
    with open(save_dir / "eval_detail.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(detail, ensure_ascii=False) + "\n")


def load_scenarios_from_json(source: str) -> list[dict]:
    """Load scenarios directly from train.json or test.json for local accuracy measurement.

    Server scenarios have the same content but are loaded via /scenario/all endpoint.
    When using source=train, we bypass the server scenario list and feed train.json
    entries (still calling server tool endpoints per-scenario with X-Scenario-Id header).
    """
    repo_root = Path(__file__).resolve().parents[2]
    path = repo_root / "data" / "Track A" / "data" / "Phase_1" / f"{source}.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--server-url", default="http://localhost:7860")
    ap.add_argument("--provider", default=os.environ.get("LLM_PROVIDER", "openrouter"),
                    choices=list(PROVIDERS.keys()))
    ap.add_argument("--model", default=None, help="Override provider default model")
    ap.add_argument("--max-tokens", type=int, default=8192)
    ap.add_argument("--max-iterations", type=int, default=20)
    ap.add_argument("--start-idx", type=int, default=0, help="Slice scenarios from this index")
    ap.add_argument("--max-samples", type=int, default=10)
    ap.add_argument("--save-dir", required=True, type=Path)
    ap.add_argument("--fresh", action="store_true", help="Ignore existing result.csv and redo")
    ap.add_argument("--source", choices=["server", "test", "train"], default="server",
                    help="Scenario source: 'server' uses /scenario/all (test set on official server), "
                         "'test' or 'train' loads directly from data/Track A/data/Phase_1/*.json "
                         "(useful for local validation when server only serves test)")
    ap.add_argument("--no-rag", action="store_true", help="Disable RAG retrieval few-shot")
    ap.add_argument("--rag-k", type=int, default=3, help="Number of retrieved neighbors for RAG")
    ap.add_argument("--num-attempts", type=int, default=1,
                    help="Self-consistency: run each scenario N times and majority-vote")
    ap.add_argument("--temperature", type=float, default=0.0,
                    help="Sampling temperature for attempts > 1 (default 0.0, but raised to 0.5 "
                         "when num-attempts > 1 for diversity)")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    )

    env = Environment(args.server_url)
    runner = QwenRunner(
        env=env,
        provider=args.provider,
        model_override=args.model,
        max_tokens=args.max_tokens,
        max_iterations=args.max_iterations,
        use_rag=not args.no_rag,
        rag_k=args.rag_k,
    )

    if args.source == "server":
        scenarios = env.get_scenarios()
        if not scenarios:
            log.error("No scenarios from server %s/scenario/all", args.server_url)
            sys.exit(1)
        log.info("Loaded %d scenarios from server", len(scenarios))
    else:
        scenarios = load_scenarios_from_json(args.source)
        log.info("Loaded %d scenarios from %s.json", len(scenarios), args.source)

    end_idx = min(args.start_idx + args.max_samples, len(scenarios))
    slice_ = scenarios[args.start_idx:end_idx]
    log.info("Processing [%d:%d] = %d scenarios", args.start_idx, end_idx, len(slice_))

    done: set[str] = set() if args.fresh else load_done(args.save_dir)
    log.info("Already done: %d", len(done))

    solved = forced = 0
    for idx, scenario in enumerate(slice_):
        sid = scenario.get("scenario_id")
        if not sid:
            log.warning("[%d/%d] scenario missing scenario_id, skipping", idx + 1, len(slice_))
            continue
        if not args.fresh and sid in done:
            log.info("[%d/%d] skip %s (already done)", idx + 1, len(slice_), sid)
            continue

        t0 = time.time()
        log.info("[%d/%d] %s start (attempts=%d)", idx + 1, len(slice_), sid, args.num_attempts)

        attempts_preds: list[str] = []
        attempts_meta: list[dict] = []
        last_resp: dict = {"answer": "", "traces": ""}

        # Use diverse temperature for multiple attempts to encourage variance
        effective_temp = args.temperature if args.num_attempts == 1 else max(args.temperature, 0.5)

        for att in range(args.num_attempts):
            try:
                resp = runner.run(scenario, temperature=effective_temp if att > 0 else args.temperature)
            except Exception as e:
                log.error("Runner exception for %s (att %d): %s\n%s",
                          sid, att + 1, e, traceback.format_exc())
                resp = {"scenario_id": sid, "status": "unresolved", "reason": str(e),
                        "answer": "", "traces": ""}
            last_resp = resp
            att_pred = normalize_answer(resp.get("answer", "") or resp.get("traces", ""))
            attempts_preds.append(att_pred)
            attempts_meta.append({
                "attempt": att + 1,
                "prediction": att_pred,
                "status": resp.get("status"),
                "num_iterations": resp.get("num_iterations"),
                "num_tool_calls": resp.get("num_tool_calls"),
            })

        # Voting / consolidation
        if args.num_attempts > 1:
            tag = scenario.get("tag", "single-answer")
            non_empty = [p for p in attempts_preds if p]
            prediction = majority_vote(non_empty, tag) if non_empty else ""
        else:
            prediction = attempts_preds[0] if attempts_preds else ""

        latency = round(time.time() - t0, 2)

        fallback_used = False
        if not prediction:
            fb = insufficient_data_option(scenario.get("task", {}).get("options", []))
            if fb:
                prediction = fb
                fallback_used = True
                log.warning("[%d/%d] %s empty prediction → P7 fallback %s",
                            idx + 1, len(slice_), sid, fb)

        ground_truth = scenario.get("answer", "")
        score = compute_score(prediction, ground_truth) if ground_truth else None

        resp = last_resp

        append_result(args.save_dir, sid, prediction)
        raw_answer = (resp.get("answer") or "")[:800]
        raw_traces = (resp.get("traces") or "")[:800]
        append_eval_detail(
            args.save_dir,
            {
                "scenario_id": sid,
                "status": resp.get("status"),
                "reason": resp.get("reason"),
                "prediction": prediction,
                "fallback_used": fallback_used,
                "ground_truth": ground_truth,
                "score": score,
                "num_iterations": resp.get("num_iterations"),
                "num_tool_calls": resp.get("num_tool_calls"),
                "latency_s": latency,
                "attempts": attempts_meta if args.num_attempts > 1 else None,
                "raw_answer_head": raw_answer,
                "raw_traces_head": raw_traces,
            },
        )

        if resp.get("status") == "solved":
            solved += 1
        else:
            forced += 1

        log.info(
            "[%d/%d] %s -> pred=%s gt=%s score=%s lat=%.1fs status=%s",
            idx + 1, len(slice_), sid, prediction, ground_truth, score, latency, resp.get("status"),
        )

    log.info("Done. solved=%d forced/unresolved=%d", solved, forced)


if __name__ == "__main__":
    main()
