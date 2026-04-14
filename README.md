# Telco Troubleshooting Agentic Challenge

> [Zindi Competition](https://zindi.africa/competitions/telco-troubleshooting-agentic-challenge) | Track B: IP Networks | Prize: EUR 40,000

[한국어](README.ko.md)

## Overview

AI agent system for autonomous IP network fault diagnosis and troubleshooting. Built for the **Telco Troubleshooting Agentic Challenge** organized by GSMA, ETSI, ITU, IEEE GenAINet, and TM Forum.

The agent interacts with a multi-vendor network simulator (Huawei/Cisco/H3C) via CLI commands, analyzes device outputs, and solves three types of network O&M problems:

- **Topology Reconstruction** — Restore deleted link information using LLDP, ARP, and interface data
- **Path Query** — Trace forwarding paths from source to destination via routing tables
- **Fault Localization** — Diagnose traffic interruption causes (routing/port faults)

## Architecture

```
┌─────────────────┐     ┌──────────────────────┐
│   Agent (LLM)   │────▶│  Agent Tool Server   │
│ Qwen3.5-35B-A3B │◀────│  (CLI Simulator)     │
│                 │     │  Huawei/Cisco/H3C    │
│ - System Prompt │     │  102K+ output files  │
│ - Tool Use      │     └──────────────────────┘
│ - CoT Reasoning │
└─────────────────┘
```

## Key Features

- **Single unified tool**: `execute_cli_command(device_name, command)` for all vendor interactions
- **Parallel tool calls**: Query multiple devices simultaneously in one turn
- **Problem-type strategies**: Specialized prompts for topology/path/fault problems
- **Auto-recovery**: Handles empty responses, timeouts, and API errors gracefully
- **Resume support**: Can continue from interrupted evaluation runs

## Quick Start

### 1. Setup Agent Tool Server

```bash
cd data/Track\ B/
# Unzip device outputs (if not already done)
unzip devices_outputs.zip -d devices_outputs/
# Start server
python server.py
# Server runs at http://127.0.0.1:7860
```

### 2. Configure LLM API

Set your HuggingFace token (for Qwen3.5-35B-A3B via novita provider):

```bash
export HF_TOKEN="hf_your_token_here"
# Or login: hf auth login
```

### 3. Run Agent

```bash
# Single question test
python agent/agent.py -i "data/Track B/data/Phase_1/test.json" --questions 1

# Full evaluation (50 questions)
python agent/agent.py -i "data/Track B/data/Phase_1/test.json"

# Fresh run (ignore previous results)
python agent/agent.py -i "data/Track B/data/Phase_1/test.json" --fresh
```

## Project Structure

```
├── agent/
│   └── agent.py              # Main agent implementation
├── data/
│   ├── Track A/              # Wireless network data (unused)
│   ├── Track B/              # IP network data
│   │   ├── server.py         # Agent Tool Server
│   │   ├── devices_outputs/  # CLI output files (541MB)
│   │   ├── data/Phase_1/     # Test questions (50)
│   │   └── agent/            # OpenClaw example agent
│   └── submission/           # Submission template
└── docs/                     # Documentation
    ├── 00_index.md
    ├── 02_agentic_challenge_overview.md
    ├── 03_data_analysis.md
    ├── 04_track_b_strategy.md
    └── 05_progress_report.md
```

## Competition Details

| Item | Value |
|------|-------|
| **Prize Pool** | EUR 40,000 (1st: EUR 12,500 + MWC Shanghai trip) |
| **Base Model** | Qwen3.5-35B-A3B (mandatory) |
| **Track B** | IP Networks, 50 questions, Exact Match |
| **Phase 1** | Apr 3 – May 4 (open practice) |
| **Phase 2** | May 4 – May 18 (elimination, top 30) |
| **Phase 3** | May 18 – May 29 (final, efficiency scoring) |
| **Partners** | GSMA, ETSI, ITU, IEEE GenAINet, TM Forum |

## Evaluation

- **Phase 1**: Accuracy only
- **Phase 2**: Accuracy + API call count (fewer = better)
- **Phase 3**: Accuracy × time discount (< 5min: 100%, 5-10min: 80%, 10-15min: 60%, > 15min: 0%)

## License

Competition data is licensed under CC-BY-SA 4.0. Agent code is MIT licensed.
