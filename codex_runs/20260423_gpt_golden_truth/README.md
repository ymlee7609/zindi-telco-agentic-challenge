# 2026-04-23 GPT Golden Truth Run

This directory contains an isolated Codex-run baseline for the current project.

## Project understanding

- Track A is the wireless 5G troubleshooting agent in `agent/track_a/agent.py`.
- Track B is the IP-network troubleshooting agent in `agent/track_b/agent.py`.
- Both agents call local simulators and rely on an external LLM API for reasoning.
- Existing repo outputs under `agent/track_a/results_*` and `agent/track_b/results_*` were left untouched.

## Why these truth references

- Track A does not expose hidden test labels. The only defensible ground truth is the labeled train split.
- Track B already has a curated truth reference in `agent/track_b/opus_reference/GROUND_TRUTH.json`.

## Artifacts

- `track_a/train_ground_truth/result.csv`
  Track A direct truth materialized from `data/Track A/data/Phase_1/train.json` (2000 rows).
- `track_a/gpt_sim_train_50/result.csv`
  GPT simulation on the first 50 Track A train scenarios.
- `track_a/gpt_sim_train_50/eval_detail.jsonl`
  Per-scenario Track A detail log.
- `track_b/ground_truth_reference/result.csv`
  Track B curated truth materialized from `agent/track_b/opus_reference/GROUND_TRUTH.json` (50 rows).
- `track_b/gpt_sim_test_50/result.csv`
  GPT simulation on all 50 Track B test questions.
- `track_b/gpt_sim_test_50/eval_detail.jsonl`
  Per-question Track B detail log.
- `logs/`
  Session-specific server and inline run logs.

## Model/runtime used

- GPT simulation model: `openai/gpt-4o-mini` via OpenRouter.
- Track A was run against the local train simulator.
- Track B was run against the local CLI simulator.

## Results summary

- Track A GPT simulation scope: 50 train scenarios.
- Track A exact match: `7/50` (14.00%).
- Track A mean IoU: `0.1617`.
- Track B GPT simulation scope: 50 test questions.
- Track B agent status counts: `solved=47`, `max_iterations=2`, `validation_failed=1`.
- Track B exact match vs curated truth (raw): `1/50`.
- Track B exact match vs curated truth after newline normalization: `3/50`.
- Track B normalized exact-match QIDs: `5, 6, 37`.

## Notes

- Track B `result.csv` contains actual embedded newlines for multi-line answers, while the curated submission-style truth uses literal `\n`. The normalized comparison above compensates for that formatting difference.
- The low Track B agreement is not just formatting; many answers are substantively different from the curated truth reference.
- Notable non-solved Track B cases in this run: Q8 and Q16 hit `max_iterations`, Q32 ended in `validation_failed`.
