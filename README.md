# Telco Troubleshooting Agentic Challenge

> [Zindi Competition](https://zindi.africa/competitions/telco-troubleshooting-agentic-challenge) | **Track A (Wireless 5G) + Track B (IP Networks)** | Prize: EUR 40,000

[한국어](README.ko.md)

## Overview

AI agent system for **both tracks** of the Telco Troubleshooting Agentic Challenge (GSMA, ETSI, ITU, IEEE GenAINet, TM Forum).

Both tracks mandate **Qwen3.5-35B-A3B** as the base model and expose scenario-scoped tools through a FastAPI simulator. Track A deals with wireless RAN (drive-test optimization), Track B with IP network O&M (topology / path / fault).

## Two Tracks Side by Side

| | **Track A — Wireless 5G** | **Track B — IP Networks** |
|---|---|---|
| **Domain** | 5G drive-test optimization | IP network O&M on multi-vendor CLI |
| **Data scale** | 2000 train + 500 test scenarios | 50 test questions (Phase 1) |
| **Input** | throughput/RSRP/SINR time-series + cell config | device CLI outputs (Huawei/Cisco/H3C) |
| **Question type** | Pick 1 option (single) or 2–4 options (multi) from C1~C22 | free-form text (Exact Match) |
| **Answer format** | `\boxed{C9}` or `\boxed{C2\|C8\|C11\|C16}` | `node->node->...` / `node;dest;cause` / link list |
| **Scoring** | IoU × time discount | Exact Match × time discount |
| **Tool server** | `localhost:7861` (test) + `localhost:7862` (train, local eval) | `localhost:7860` |
| **Tool count** | 27 (throughput / serving-cell / neighbor / antenna / KPI) | 1 unified (`execute_cli_command`) |
| **Agent** | `agent/track_a/agent.py` | `agent/track_b/agent.py` |
| **Submission** | `submission_v1.csv` (500 rows, RAG v3) | `submission_v6_full_v10.csv` (50 rows) |
| **Current result** | IoU 0.220 on train 50 (+38% over baseline) | 48/50 solved (96%) |

Both tracks output to a **single Zindi submission** `ID, Track A, Track B` with 550 rows.

## Architecture

### Track A (Wireless)

```
                      ┌──────────────────────────┐
                      │  Track A Tool Server     │
                      │  FastAPI :7861 / :7862   │
                      │  27 tools (throughput,   │
                      │  RSRP/SINR, cell_info,   │
                      │  neighbor, antenna...)   │
                      └───────────▲──────────────┘
                                  │ HTTP
┌─────────────────────────────────┴────────────────┐
│  Qwen3.5-35B-A3B Agent (RAG-enhanced)           │
│  - 7-pattern system prompt (P1~P7)              │
│  - Static few-shot × 5 (traces + train 0/1/5)   │
│  - RAG: L2 retrieval top-3 from train 2000      │
│  - XML re-ask + P7 fallback + self-consistency  │
└──────────────────────────────────────────────────┘
```

### Track B (IP Network)

```
                      ┌──────────────────────────┐
                      │  Track B Tool Server     │
                      │  FastAPI :7860           │
                      │  Multi-vendor CLI        │
                      │  Huawei/Cisco/H3C        │
                      │  102K+ output files      │
                      └───────────▲──────────────┘
                                  │ HTTP
┌─────────────────────────────────┴────────────────┐
│  Qwen3.5-35B-A3B Agent                          │
│  - Question-type detection (topology/path/fault)│
│  - Device whitelist + alias guards (PJ area)    │
│  - Parallel tool calls per turn                 │
│  - Forced-answer validation + loop guard        │
└──────────────────────────────────────────────────┘
```

## Key Features

### Track A

- **7-Pattern Library** (P1 Late-HO / P2 Ping-pong / P3 Overshoot / P4 Coverage-hole / P5 Server / P6 Excessive-tilt / P7 Insufficient) derived from Opus manual solving of 10 train + 2 expert traces
- **14-dim RAG** over train 2000: features TP/SINR/RSRP/PCI-changes/A3-offset/max-tilt → Z-score → L2 top-3
- **Dynamic few-shot**: static 5 + RAG-retrieved 3 injected per scenario
- **Self-consistency** (`--num-attempts N`): multi-trial + majority vote (currently disabled — v3 baseline)

### Track B

- **Question-type aware strategy**: topology / path / fault branches with dedicated prompts and hints
- **Device whitelist + alias guards**: PJ area node-alias mapping (TODO-03/08/09) to prevent hallucination
- **HIGH-ALIAS RULE 1~4**: forced-answer validation + XML fallback + line-count guard (TODO-11~15)
- **v10 resolution**: Q29 automatic + Q31/Q32 regression fix

## Quick Start

### 1. Tool Servers

```bash
# Track B server (port 7860)
cd "data/Track B/"
unzip devices_outputs.zip -d devices_outputs/   # first time only
python server.py &

# Track A test server (port 7861)
cd "data/Track A/"
FASTAPI_PORT=7861 python server.py &

# Track A train server for local eval (port 7862)
FASTAPI_PORT=7862 DATA_SPLIT=train python server.py &
```

### 2. LLM API

```bash
# .env at repo root (loaded automatically)
OPENROUTER_API_KEY="sk-or-v1-..."
# Alternative: HF_TOKEN, DASHSCOPE_API_KEY, GROQ_API_KEY, GEMINI_API_KEY
```

### 3. Run Agents

**Track A — Wireless 5G** (~35s/scenario):

```bash
# Precompute RAG cache (first time only, 2000 train scenarios)
python agent/track_a/rag.py --precompute

# Local validation on train 50 (ground truth available)
python agent/track_a/agent.py \
    --server-url http://localhost:7862 \
    --max-samples 50 \
    --save-dir agent/track_a/results_train_eval_50_v3
python agent/track_a/eval_local.py \
    agent/track_a/results_train_eval_50_v3/result.csv --source train

# Full test execution (Pilot 50 + Batch A 200 + Batch B 250 = 500)
python agent/track_a/agent.py --server-url http://localhost:7861 --max-samples 50   --save-dir agent/track_a/results_pilot_v3
python agent/track_a/agent.py --server-url http://localhost:7861 --start-idx 50  --max-samples 200 --save-dir agent/track_a/results_batch_a
python agent/track_a/agent.py --server-url http://localhost:7861 --start-idx 250 --max-samples 250 --save-dir agent/track_a/results_batch_b
```

**Track B — IP Networks** (~180s/scenario):

```bash
# Single question test
python agent/track_b/agent.py -i "data/Track B/data/Phase_1/test.json" --questions 1

# Full evaluation (50 questions, resumes from existing result.csv)
python agent/track_b/agent.py -i "data/Track B/data/Phase_1/test.json"

# Fresh run
python agent/track_b/agent.py -i "data/Track B/data/Phase_1/test.json" --fresh
```

### 4. Build Unified Submission

```bash
# Track A → merges into common/submission/submission_combined.csv
python agent/track_a/generate_submission.py \
    --results agent/track_a/results_pilot_v3/result.csv \
    --override agent/track_a/results_batch_a/result.csv \
    --override agent/track_a/results_batch_b/result.csv \
    --out agent/track_a/submission/submission_v1.csv

# Track B → same combined file, fills Track B column
python agent/track_b/submission/generate_submission.py \
    --results agent/track_b/results_v6_full/result.csv \
    --override agent/track_b/results_v9_test/result.csv \
    --override agent/track_b/results_v10_test/result.csv \
    --out agent/track_b/submission/submission_v6_full_v10.csv

# Verify
python agent/common/submission/merge_submission.py --status
# → Combined: Track A 500/550, Track B 50/550
```

Upload `agent/common/submission/submission_combined.csv` to Zindi.

## Zindi Submission Format Spec (CRITICAL)

**Source of truth**: `agent/common/submission_example.csv` — always consult this file before creating or modifying a submission.

### Track B multi-line answers

Multi-line Track B answers (TOPO multiple links, FAULT multiple reasons, PATH multiple candidates) use a **literal `\n` (two characters: backslash + n)** as the row separator — **not** an actual newline (U+000A).

Correct (matches `submission_example.csv` line 507):
```
Atlas-Prime-01->Gaia-Node-01->Eon-Node-01\nAtlas-Prime-01\nGaia-Node-01->Demeter-Prime-01->Eon-Node-01
```

Incorrect — do NOT convert to real newlines:
```
Atlas-Prime-01->Gaia-Node-01->Eon-Node-01
Atlas-Prime-01
Gaia-Node-01->Demeter-Prime-01->Eon-Node-01
```

### Submission rules

1. Before any submission work, read `agent/common/submission_example.csv` first. It is the authoritative format reference.
2. Never "fix" literal `\n` to real newlines. Zindi's scorer expects literal `\n`.
3. The "no extra whitespace before/after/within each line" clause in the problem statement refers to whitespace **within a single link/reason**, not the `\n` separator.
4. Serial naming for new submissions: `submission_NNN_YYYYMMDD_label.csv`. See `agent/track_b/submission/SUBMISSIONS.md` for the serial registry.

### History (why this matters)

On 2026-04-23, serial 017 was created by converting literal `\n` → real newlines under the wrong hypothesis that `\n` counted as "extra whitespace". It does not. Serial 017 is marked INVALID. Current best submission remains serial 016 (`submission_v12_topofault_rt.csv`, Zindi 0.44).

## Project Structure

```
├── agent/
│   ├── common/
│   │   ├── submission_example.csv        # Zindi 550-row template
│   │   └── submission/
│   │       ├── merge_submission.py       # Track A/B merge helper
│   │       └── submission_combined.csv   # FINAL upload file
│   ├── track_a/                          # Wireless 5G agent
│   │   ├── agent.py                      # Qwen runner (RAG + retry + fallback)
│   │   ├── prompts.py                    # System prompt + 5 few-shot
│   │   ├── rag.py                        # 14-dim feature + train 2000 retrieval
│   │   ├── generate_submission.py        # Track A column filler (auto combined)
│   │   ├── eval_local.py                 # IoU scoring vs train.json answer
│   │   ├── tools/scenario_summary.py
│   │   ├── results_pilot_v3/             # test 0-49
│   │   ├── results_batch_a/              # test 50-249
│   │   ├── results_batch_b/              # test 250-499
│   │   └── submission/submission_v1.csv
│   └── track_b/                          # IP network agent
│       ├── agent.py                      # Main agent (1487 LOC)
│       ├── results_v6_full/              # v6 baseline (47/50 solved)
│       ├── results_v6_retry*/            # Non-solved question retries
│       ├── results_v10_test/             # HIGH-ALIAS fix
│       └── submission/submission_v6_full_v10.csv
├── data/
│   ├── Track A/                          # Wireless data + tool server + 2000+500 scenarios
│   │   ├── server.py, main.py, rag.py    # Provided code (do not modify server.py)
│   │   ├── data/Phase_1/{train,test}.json
│   │   └── examples/traces.json          # Expert solutions (few-shot source)
│   └── Track B/                          # IP data + tool server + 50 scenarios
│       ├── server.py, devices_outputs/   # Provided code + CLI outputs (541 MB)
│       └── data/Phase_1/test.json
├── docs/
│   ├── 00_index.md                       # Master navigation
│   ├── common/                           # Shared challenge/data docs
│   ├── track_a/
│   │   ├── 03-1_architecture.md          # Agent flow (Mermaid)
│   │   ├── 03-2_topology.md              # 5G RAN concepts + A3 formula
│   │   ├── 03-3_problems.md              # 7-pattern + train 2000 stats
│   │   ├── 04_rag_architecture.md        # RAG detailed design
│   │   └── 08_track_a_progress.md        # Execution log
│   └── track_b/
│       ├── 03-1_architecture.md
│       ├── 03-2_topology.md              # + D2/SVG diagrams (Traditional + PJ)
│       ├── 03-3_problems.md              # 50-question answers (v8 mapping)
│       ├── 03-3-1_problems_detail.md
│       ├── 05_track_b_strategy.md
│       ├── 06_progress_report.md
│       └── 07_not_solved_recovery_strategy.md
└── .moai/
    ├── cache/track_a_train_features.json # RAG precompute (1.1 MB)
    └── plans/                            # Session plans + Opus manual solutions
```

## Competition Details

| Item | Value |
|------|-------|
| **Prize Pool** | EUR 40,000 (1st per track: EUR 12,500 + MWC Shanghai trip) |
| **Base Model** | Qwen3.5-35B-A3B (mandatory — fine-tuning allowed, no replacement) |
| **Track A** | Wireless 5G drive-test optimization, 2000 train + 500 test, IoU scoring |
| **Track B** | IP Networks O&M, 50 Phase-1 questions, Exact Match |
| **Phase 1** | Apr 3 – May 4 (open practice, unlimited submissions) |
| **Phase 2** | May 4 – May 18 (elimination, top 30, 3 submissions max) |
| **Phase 3** | May 18 – May 29 (final, single submission with fine-tuned weights) |
| **Partners** | GSMA, ETSI, ITU, IEEE GenAINet, TM Forum |

## Evaluation

- **Phase 1**: Accuracy only, unlimited submissions
- **Phase 2**: Accuracy + efficiency (API call count)
- **Phase 3**: Accuracy × time discount
  - `< 5 min`: 100%
  - `5–10 min`: 80%
  - `10–15 min`: 60%
  - `> 15 min`: **0%** (timeout)

## Current Status (2026-04-23 Day 1 close)

### Track A — Phase 1 submission v1 ready

- Stage A (Opus manual) → **9/10 correct**, derived P1~P7 pattern library
- Stage B (agent/track_a/) → agent.py + prompts.py + rag.py + generate_submission.py
- Stage C (500/500 executed) → Pilot v3 50 + Batch A 200 + Batch B 250
- Local validation (train 50 v3 RAG): **IoU 0.220** (+38% over baseline 0.160)
- Issue: test Batch shows P7 fallback 68.6% (vs 36% on train 50) — improvement options A~D documented in `docs/track_a/08_track_a_progress.md`

### Track B — Zindi 0.44 (22/50), +120% vs v11 baseline

- **v11 baseline** (OpenRouter Qwen3.5, internal 48/50 solved label): Zindi **0.20** (10/50)
- **v12 Deterministic Hybrid** (CLI file parsing + routing-table trace + LLM fallback): **0.44** (22/50)
- New modules (2026-04-23):
  - `agent/track_b/cli_parsers.py` — public LLDP / interface / routing / description parsers
  - `agent/track_b/topology_parser.py` — 4-tier fallback (self LLDP → neighbor LLDP → neighbor desc → ARP)
  - `agent/track_b/fault_analyzer.py` — nexthop chain + reason enum exact match
  - `agent/track_b/path_tracer.py` — routing-table hop-by-hop (beats BFS on -02 paths)
- Submission history (Zindi public):
  - 0.20 v11 → 0.24 v12_topo → 0.12 v12_det_full (BFS rollback) → 0.36 v12_topo_fault → **0.44 v12_topofault_rt**
- Best CSV: `agent/track_b/submission/submission_v12_topofault_rt.csv`
- **Path Traditional Q7~Q16 fully solved** (10/10). Topology hallucinations (Spine/PC) eliminated.
- Day 2 plan: `.moai/plans/track-b-day2-strategy.md` (10 submissions, target 0.55+)
- See `docs/track_b/06_progress_report.md` §11 for full v12 technical breakdown

## License

Competition data: CC-BY-SA 4.0. Agent code: MIT.
