#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Track A Qwen 용 System Prompt + Few-shot 정의.

Opus 4.7 수작업 풀이 (`.moai/plans/track-a-opus-solutions.md`) 에서 증류한
7-pattern library + A3 offset 공식 + tool 사용 순서를 encoding.
"""

from __future__ import annotations


SYSTEM_PROMPT = """You are an expert 5G radio-access-network (RAN) optimization engineer.
Your task is to analyze 5G network drive test data (user plane time-series, cell configuration,
signaling events, traffic KPIs, MR reports) and select the correct optimization action(s)
from a list of candidate options (C1 ~ C22).

# Handover Threshold Formula (critical)
A3 event triggers when:
    Neighbor_RSRP > Serving_RSRP + (A3Offset × 0.5 dB) + (A3Hyst × 0.5 dB)
Cell config values `IntraFreqHoA3Offset` and `IntraFreqHoA3Hyst` are in 0.5 dB units.
Examples: offset=2 → 1 dB, offset=6 → 3 dB, offset=10 → 5 dB.

# Tool Call Guidance
When you need more data, call tools in this order (skip if already known from context):
1. get_throughput_logs — find low-throughput time window (< 100 Mbps, usually several seconds)
2. get_serving_cell_pci(time) at 2-3 times within the window — determine if serving PCI is stable, changing, or ping-ponging
3. get_cell_info(pci) — for the serving PCI and any repeatedly appearing neighbor PCI; read A3Offset, Power, Tilt (Mechanical+Digital), Azimuth, PdcchOccupiedSymbolNum, CovInterFreqA2RsrpThld, neighbor list
4. get_serving_cell_rsrp(time), get_serving_cell_sinr(time) — confirm RF quality at the degradation point
5. get_neighboring_cells_pci(time), get_neighboring_cell_rsrp(time, pci) — quantify interfering/dominant neighbors
6. calculate_tilt_angle(time, pci) — IMPORTANT for P6 detection! Call this for EACH cell PCI
   at a degradation timestamp. Returns the geometric ideal tilt angle from cell to UE.
   Compare with actual tilt: if actual >> |ideal|, that cell has excessive downtilt (P6).
   Example: calculate_tilt_angle returns -4° but actual tilt is 24° → P6 on that cell.

After gathering evidence, REASON about which pattern matches, then answer.

# 7-Pattern Diagnostic Checklist
Check each pattern against the evidence. Pick the best-fitting pattern.

P1 LATE HANDOVER (A3 too high on serving)
  - Serving PCI stays on one cell during degradation
  - A3Offset of serving cell >= 10 (5 dB) or effectively blocking handover
  - A neighbor cell is clearly stronger than serving + threshold would allow
  → Answer: "Decrease A3 Offset threshold for <serving_cell>"

P2 PING-PONG BETWEEN TWO CELLS
  - Serving PCI alternates A ↔ B repeatedly within the window
  - Both cells have low A3Offset (e.g., 2 = 1 dB)
  → Answer: "Increase A3 Offset threshold for <one or both ping-pong cells>"

P3 OVERSHOOT INTERFERENCE
  - SINR is low (< 5 dB or negative) during degradation
  - A specific distant cell (not the geographically appropriate serving) keeps appearing as
    Top-1/2 neighbor with comparable RSRP
  - That cell has high power (>= 25 dBm), small downtilt (Mechanical Downtilt <= 2), or wide azimuth
  → Answer: 2-4 actions on the OVERSHOOTING cell — some combination of:
      "Decrease transmission power for <cell>",
      "Press down the tilt angle of <cell>",
      "Increase A3 Offset threshold for <cell>",
      "Adjust the azimuth of <cell>"

P4 COVERAGE HOLE
  - Serving RSRP <= -100 dBm
  - All measured neighbors also weak (most <= -100 dBm)
  - The geographically correct serving cell has power below max (< 30)
  → Answer: 2-4 actions to boost coverage —
      "Increase transmission power for <cell>",
      "Adjust the azimuth of <cell> by X degrees",
      "Lift the tilt angle of <cell>" (reduce downtilt)

P5 SERVER / TRANSMISSION ISSUE
  - SINR is healthy (>= 10 dB) throughout the degradation window
  - Throughput fluctuates wildly or drops to near zero with no RF anomaly
  - MR data shows random low-throughput samples (e.g., 3 Mbps next to 200 Mbps under same RSRP)
  MANDATORY BEFORE CHOOSING P5: You MUST call calculate_tilt_angle(time, pci) for ALL cell PCIs
  first. If any cell shows actual_tilt >> |returned_angle|, choose P6 instead of P5.
  Only choose P5 if calculate_tilt_angle confirms NO cell has excessive tilt discrepancy.
  → Answer: "Check test server and transmission issues"

P6 EXCESSIVE DOWNTILT ON A CELL (VERY SIMILAR TO P5 — use calculate_tilt_angle to distinguish!)
  - SINR is generally healthy but throughput is degraded
  - CRITICAL: Use calculate_tilt_angle(time, pci) for EACH cell to get the ideal tilt angle
  - Compare the ideal tilt from calculate_tilt_angle with the cell's actual total downtilt:
    * If actual_tilt >> |ideal_tilt| (e.g., actual=24° but ideal=-19°) → excessive downtilt → P6
    * If no cell shows excessive tilt discrepancy → P5 (server issue)
  - The cell with the biggest tilt discrepancy is the one that needs "Lift tilt"
  → Answer: "Lift the tilt angle of <that cell> by X degrees"
  HOW TO CHECK: After gathering basic evidence (throughput, SINR, RSRP, PCI), if SINR >= 5 dB
  and the pattern is unclear between P5/P6/P8, call calculate_tilt_angle for each cell PCI.
  The cell whose actual tilt most exceeds the ideal is the P6 candidate.

P7 INSUFFICIENT DATA (use ONLY when ALL of these are true)
  - SINR consistently >= 10 dB (no interference)
  - RSRP consistently > -100 dBm (good coverage)
  - Throughput is mostly normal with only minor dips (NOT sustained degradation)
  - A3Offset is normal (< 10), CovInterFreqA2RsrpThld = -105 (standard)
  - All neighbors are in the neighbor list, no cell has total tilt >= 20°
  IMPORTANT: P7 should be rare (~12% of scenarios). If you find yourself choosing P7 often,
  you are likely missing patterns. Re-check P8-P10 before defaulting to P7.
  → Answer: "Insufficient data; more data is needed for judgment."

P8 PDCCH RESOURCE (diagnosis of exclusion — check LAST, before P7)
  - P1-P6, P9, P10 all ruled out, but throughput is consistently degraded (not random like P5)
  → Answer: "Modify PdcchOccupiedSymbolNum to 2SYM for <serving cell>"

P9 MISSING NEIGHBOR
  - A strong neighbor (RSRP >= -90) appears in get_neighboring_cells_pci() but is NOT in the
    serving cell's configured "PCell Neighbor Cell" list (from get_cell_info)
  → Answer: "Add neighbor relationship between <serving cell> and <strong neighbor>"

P10 COVERAGE THRESHOLD TOO HIGH
  - get_cell_info shows CovInterFreqA2RsrpThld = -95 dBm (standard is -105 dBm)
  - Higher threshold = inter-freq measurement too conservative
  → Answer: "Decrease CovInterFreqA2RsrpThld ... thresholds for <cell>"

# Decision Tree (10-Pattern, ordered by check priority)
For SINGLE-ANSWER questions, walk through this tree top-to-bottom. STOP at the first match.

Step 1: Check Serving PCI stability during degradation
  - PCI alternates A ↔ B repeatedly → P2 PING-PONG
  - PCI stable → continue to Step 2

Step 2: Check A3Offset of serving cell
  - Serving cell A3Offset >= 10 (5 dB) + a stronger neighbor exists → P1 LATE HANDOVER
  - A3Offset normal → continue to Step 3

Step 3: Check SINR
  - SINR < 5 dB or negative → P3 OVERSHOOT (identify the overshooting cell)
  - SINR >= 5 dB → continue to Step 4

Step 4: Check cell config for P10 and P9 (SINR is acceptable from here)
  4a. CovInterFreqA2RsrpThld significantly above -105 dBm (e.g., -95 or -100 dBm)?
      → YES: P10 COVERAGE THRESHOLD (decrease threshold)
  4b. A strong neighbor cell (RSRP >= -90) appears in drive test but is NOT in the serving
      cell's configured neighbor list?
      → YES: P9 MISSING NEIGHBOR (add neighbor relationship)
  4c. If none of 4a-4b match → continue to Step 5

Step 5: Use calculate_tilt_angle to distinguish P5 vs P6 vs P8
  IMPORTANT: Call calculate_tilt_angle(time, pci) for EACH cell PCI at a degradation timestamp.
  This returns the geometric tilt angle from the cell to the UE position.
  Compare this with the cell's actual total downtilt (Mechanical Downtilt + Digital Tilt):
  - If ANY cell's actual_downtilt significantly exceeds |returned_tilt_angle|
    (e.g., actual=24° but calculate_tilt returns -19°, or actual=12° but ideal=-4°)
    → P6 EXCESSIVE DOWNTILT on that cell → "Lift the tilt angle of <cell> by X degrees"
  - If NO cell has excessive tilt discrepancy:
    - Throughput fluctuates WILDLY and RANDOMLY → P5 SERVER ISSUE
    - Throughput is consistently degraded (not random) → P8 PDCCH RESOURCE

Step 6: If no pattern matches → P7 INSUFFICIENT DATA

# Decision Rules
- Walk through the Decision Tree above BEFORE picking an answer.
- Prefer PATTERN match over partial reasoning. One strong pattern match > weak combination.
- For single-answer questions, pick the SINGLE option whose text corresponds to the top pattern.
- For multiple-answer questions, pick **2 to 4 options** that address the SAME ROOT CAUSE.
  MULTIPLE-ANSWER RULES (STRICT):
  * The task description explicitly says "two to four" — picking 1 option is WRONG.
  * Common multi-answer combinations (see few-shot):
    - P3 Overshoot: `Decrease power` + `Press down tilt` + `Increase A3 Offset` (+ optional `Adjust azimuth`) on the SAME overshoot cell
    - P4 Coverage hole: `Adjust azimuth` + `Increase power` (+ optional `Lift tilt`) on the SAME weak cell
    - Mixed: P3 on overshoot cell + P2 (A3 Offset up) on a ping-pong cell
  * IDs must be in ASCENDING order (e.g., `C2|C8|C11|C16` — not `C11|C2|C8|C16`).
- If no pattern matches cleanly → P7 Insufficient data (single-answer only; multi-answer never uses P7).

# Answer Format (MANDATORY)
End your response with exactly ONE of:
  \\boxed{C#}                    (single-answer, e.g., \\boxed{C9})
  \\boxed{C#|C#|C#|C#}          (multiple-answer, 2-4 options, IDs in ASCENDING order, e.g., \\boxed{C2|C8|C11|C16})

Do NOT use bold, markdown, or extra punctuation around the answer. Only \\boxed{...}.

# Protocol Rules (STRICT)
- ALWAYS use the native tool_calls protocol provided by the API (there is a `tools` parameter
  with OpenAI-style function schemas). NEVER write inline XML like <tool_call>,
  <function=...>, or <parameter=...> in your message content — the client IGNORES such text
  and your answer will be lost.
- Do NOT fabricate tool results. If a tool returned an error, adjust arguments and retry
  rather than guessing.
- If after gathering evidence you still cannot determine a clear cause for a SINGLE-ANSWER
  question, pick the option whose label is literally "Insufficient data; more data is
  needed for judgment." (pattern P7). NEVER leave the answer blank.
- For MULTIPLE-ANSWER questions, NEVER pick only 1 option. Pick 2-4 (see Decision Rules).
"""


# Few-shot examples: (user_message, assistant_response). Derived from
# examples/traces.json (traces[0], traces[1]) and train[0] (multi-answer).
# Kept concise — include only essential evidence and the final \\boxed answer.

FEW_SHOT_EXAMPLES: list[dict[str, str]] = [
    {
        "role": "user",
        "content": (
            "Analyze 5G network drive test data.\n"
            "Identify actionable steps to mitigate or resolve performance issues arising from "
            "a significant degradation in user throughput observed during drive testing. "
            "Select the most appropriate optimization solution and enclose its number in "
            "\\boxed{{}} in the final answer, e.g., \\boxed{C5}.\n\n"
            "Options:\n"
            "C1: Increase transmission power for 3225568_1\n"
            "C2: Decrease A3 Offset threshold for 3265067_3\n"
            "C3: Decrease CovInterFreq thresholds for 3265067_3\n"
            "C8: Increase A3 Offset threshold for 3265067_3\n"
            "C9: Decrease A3 Offset threshold for 3225568_1\n"
            "C18: Decrease transmission power for 3265067_3\n"
            "(... and more)"
        ),
    },
    {
        "role": "assistant",
        "content": (
            "Evidence:\n"
            "1. get_throughput_logs → throughput dropped from ~300-400 Mbps to ~27-60 Mbps "
            "between 21:33:47 and 21:33:51, then recovered to 230-440 Mbps.\n"
            "2. get_serving_cell_pci at 21:33:47.5, 49.5, 51.5 → PCI=328 (constant). UE did NOT "
            "handover despite throughput drop.\n"
            "3. get_cell_info(328) → gNodeB 3225568 Cell 1, IntraFreqHoA3Offset=10 (5 dB), "
            "A3Hyst=2 (1 dB), total handover threshold = 6 dB. Power=26, PdcchOccupiedSymbolNum=1SYM.\n"
            "4. Neighbor list has valid relations (3276821, 3265067, 3253526).\n\n"
            "Pattern match: P1 LATE HANDOVER. Serving cell 3225568_1 has A3Offset=10 which is too "
            "high; the UE remains on a degrading cell as throughput collapses. Decreasing the A3 "
            "Offset on the serving cell will let the UE hand over earlier to a stronger neighbor.\n\n"
            "\\boxed{C9}"
        ),
    },
    {
        "role": "user",
        "content": (
            "Analyze 5G network drive test data.\n"
            "Select two to four possible optimization solutions and enclose their numbers in "
            "\\boxed{{}}, e.g., \\boxed{C3|C5}.\n\n"
            "Options:\n"
            "C2: Decrease transmission power for 3279943_1\n"
            "C8: Press down the tilt angle of 3279943_1 by 4 degrees\n"
            "C11: Increase A3 Offset threshold for 3279943_1\n"
            "C16: Increase A3 Offset threshold for 3267220_2\n"
            "C17: Decrease transmission power for 3267220_2\n"
            "(... 17 more options)"
        ),
    },
    {
        "role": "assistant",
        "content": (
            "Evidence:\n"
            "1. get_throughput_logs → low-throughput window with 6 samples (TP 25-82 Mbps).\n"
            "2. get_serving_cell_pci(...) → serving PCI alternates 166 ↔ 966 repeatedly (ping-pong).\n"
            "3. get_cell_info for PCI 166 (3239249_3) and PCI 966 (3267220_2): both have A3Offset=2 "
            "(1 dB) — very low threshold causes frequent handover.\n"
            "4. Top neighbor during window is consistently PCI 420 (3279943_1) with RSRP ~-83 to -89 dBm, "
            "indicating overshoot from a cell 1+ km away. 3279943_1 has Power=18, Mechanical Downtilt=1 "
            "(almost horizontal) — overshooting beam.\n"
            "5. SINR 1-3 dB during degradation → heavy interference from overshoot.\n\n"
            "Pattern match: P3 OVERSHOOT on 3279943_1 + P2 PING-PONG between 166/966. Multi-answer "
            "treats both root causes:\n"
            "- 3279943_1 overshoot → Decrease power (C2), Press down tilt (C8), Increase A3 Offset (C11)\n"
            "- 166/966 ping-pong → Increase A3 Offset for 3267220_2 (C16)\n\n"
            "\\boxed{C2|C8|C11|C16}"
        ),
    },
    {
        "role": "user",
        "content": (
            "Analyze 5G network drive test data.\n"
            "Select the most appropriate optimization solution and enclose its number in \\boxed{{}}.\n\n"
            "Options:\n"
            "C9: Check test server and transmission issues\n"
            "C16: Decrease A3 Offset threshold for 3213863_2\n"
            "(... more)"
        ),
    },
    {
        "role": "assistant",
        "content": (
            "Evidence:\n"
            "1. get_throughput_logs → 6 low samples (TP 25-80 Mbps).\n"
            "2. Serving PCI 546 (3213751_2) maintained throughout, RSRP -85 to -93 dBm, SINR 8 to 17 dB (healthy RF).\n"
            "3. Top neighbor RSRP -90 to -96 dBm (weaker than serving, no handover candidate).\n"
            "4. MR data shows extreme throughput variance: 224 Mbps, 65 Mbps, 3.9 Mbps at similar RSRP → "
            "not an RF issue.\n\n"
            "Pattern match: P5 SERVER/TRANSMISSION ISSUE. Healthy SINR with fluctuating throughput indicates "
            "backhaul or test server instability, not radio problems.\n\n"
            "\\boxed{C9}"
        ),
    },
    # P10: Coverage Threshold 예제 (train[15], answer=C14)
    {
        "role": "user",
        "content": (
            "Analyze 5G network drive test data.\n"
            "Select the most appropriate optimization solution and enclose its number in \\boxed{{}}.\n\n"
            "Options:\n"
            "C14: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225965_6\n"
            "C15: Modify PdcchOccupiedSymbolNum to 2SYM for 3225965_6\n"
            "(... more)"
        ),
    },
    {
        "role": "assistant",
        "content": (
            "Evidence:\n"
            "1. get_throughput_logs → sustained low throughput (< 100 Mbps) across multiple samples.\n"
            "2. Serving PCI changes multiple times — frequent handovers between cells.\n"
            "3. get_cell_info for serving cells → CovInterFreqA2RsrpThld = -95 dBm for all cells "
            "(standard is -105 dBm). This high threshold delays inter-frequency coverage measurement.\n"
            "4. A3Offset is normal (6 = 3 dB), no cell has excessive tilt.\n\n"
            "Pattern match: P10 COVERAGE THRESHOLD TOO HIGH. CovInterFreqA2RsrpThld = -95 is "
            "significantly above the standard -105 dBm. Lowering the threshold will allow the UE "
            "to detect alternative frequencies earlier.\n\n"
            "\\boxed{C14}"
        ),
    },
    # P9: Missing Neighbor 예제 (train[20], answer=C2)
    {
        "role": "user",
        "content": (
            "Analyze 5G network drive test data.\n"
            "Select the most appropriate optimization solution and enclose its number in \\boxed{{}}.\n\n"
            "Options:\n"
            "C2: Add neighbor relationship between 3241057_2 and 3266648_3\n"
            "C9: Modify PdcchOccupiedSymbolNum to 2SYM for 3241057_2\n"
            "(... more)"
        ),
    },
    {
        "role": "assistant",
        "content": (
            "Evidence:\n"
            "1. get_throughput_logs → throughput dips to ~50-90 Mbps in degradation window.\n"
            "2. Serving PCI 441 (3241057_2) maintained throughout. SINR drops to 0 dB at worst.\n"
            "3. get_neighboring_cells_pci → cell with PCI 655 (3266648_3) consistently appears with "
            "strong RSRP ~-80 dBm.\n"
            "4. get_cell_info(441) → PCell Neighbor Cell list does NOT contain 3266648. "
            "The strong neighbor 3266648_3 is not in the configured neighbor list!\n"
            "5. A3Offset=6, CovThld=-105 (standard), no excessive tilt.\n\n"
            "Pattern match: P9 MISSING NEIGHBOR. Cell 3266648_3 is a strong candidate for handover "
            "(RSRP -80 dBm) but is absent from 3241057_2's neighbor list, preventing handover.\n\n"
            "\\boxed{C2}"
        ),
    },
    # P8: PDCCH Resource 예제 (train[13], answer=C15)
    {
        "role": "user",
        "content": (
            "Analyze 5G network drive test data.\n"
            "Select the most appropriate optimization solution and enclose its number in \\boxed{{}}.\n\n"
            "Options:\n"
            "C15: Modify PdcchOccupiedSymbolNum to 2SYM for 3236632_3\n"
            "C4: Check test server and transmission issues\n"
            "(... more)"
        ),
    },
    {
        "role": "assistant",
        "content": (
            "Evidence:\n"
            "1. get_throughput_logs → moderate throughput degradation ~80-100 Mbps (not extreme).\n"
            "2. Serving PCI 566 stable. SINR 8-16 dB (healthy). RSRP -88 to -92 dBm (acceptable).\n"
            "3. A3Offset=6 (normal), CovInterFreqA2RsrpThld=-105 (standard).\n"
            "4. All neighbors are in the serving cell's neighbor list. No cell has tilt >= 20°.\n"
            "5. Throughput is consistently degraded (not randomly fluctuating like P5).\n"
            "6. After ruling out P1-P6, P9, P10: PdcchOccupiedSymbolNum=1SYM → P8.\n\n"
            "Pattern match: P8 PDCCH RESOURCE. All other patterns eliminated. The steady (not random) "
            "throughput degradation with healthy RF suggests PDCCH control channel bottleneck.\n\n"
            "\\boxed{C15}"
        ),
    },
]


# P1-3: Multi-answer 전용 강조 프롬프트 (base SYSTEM_PROMPT 뒤에 append).
# single-answer 시에는 base 만 사용. 현재 submission_v1 의 3/500 multi 예측 문제 해결용.
MULTI_ANSWER_EMPHASIS = """

# CURRENT QUESTION IS MULTIPLE-ANSWER (STRICT)
This specific question is tagged 'multiple-answer' — you MUST return 2-4 options.
NEVER return a single option for this question. The task description itself says "two to four".

Common multi-answer patterns to remember:
- P3 Overshoot on cell X: combine `Decrease power for X` + `Press down tilt for X` + `Increase A3 offset for X` (+ optional `Adjust azimuth for X`)
- P4 Coverage hole on weak cell X: combine `Adjust azimuth for X` + `Increase power for X` (+ optional `Lift tilt for X`)
- Mixed P3 + P2: Overshoot on X + Ping-pong fix (Increase A3 offset) on a separate cell Y/Z
- Mixed P3 + P6: Overshoot on cell A + excessive downtilt on cell B

Output format: \\boxed{C2|C8|C11|C16} with IDs in ASCENDING order, 2-4 items.
"""


def build_system_prompt(tag: str) -> str:
    """P1-3: tag 에 따른 system prompt 선택.

    - single-answer: base SYSTEM_PROMPT (기존)
    - multiple-answer: base + MULTI_ANSWER_EMPHASIS (multi 강조 preamble 추가)
    """
    if tag == "multiple-answer":
        return SYSTEM_PROMPT + MULTI_ANSWER_EMPHASIS
    return SYSTEM_PROMPT


def build_messages(question: str, tag: str = "single-answer") -> list[dict]:
    """Assemble the full message list for a single scenario.

    Structure:
      [ system, <few-shot user/assistant pairs>, user (current question) ]
    """
    messages: list[dict] = [{"role": "system", "content": build_system_prompt(tag)}]
    messages.extend(FEW_SHOT_EXAMPLES)
    messages.append({"role": "user", "content": question})
    return messages


def forced_answer_prompt(tag: str, options_block: str, allow_p7: bool = True) -> str:
    """Prompt used when the model failed to provide a \\boxed{} answer
    after max_iterations. Port of main.py free_mode forced prompts.

    Args:
        tag: "single-answer" 또는 "multiple-answer"
        options_block: "C1:label\\nC2:label\\n..." 형식
        allow_p7: False 이면 "Insufficient data" (P7) 옵션 선택을 명시적으로 금지
                  (single-answer 시 1차 forced 재시도용). 최종 safety net 에서는 True 로 허용.
    """
    # P7 억제 문구 — single-answer 에서만 의미 있음 (multi 는 P7 이 정답일 수 없음)
    p7_exclusion = ""
    if not allow_p7 and tag == "single-answer":
        p7_exclusion = (
            "IMPORTANT: DO NOT pick the 'Insufficient data; more data is needed for judgment.' "
            "option. Review the evidence gathered through your tool calls and pick the option "
            "whose text most closely matches the observed pattern (late handover, ping-pong, "
            "overshoot, coverage hole, server issue, excessive downtilt). If no pattern "
            "dominates, pick the option most consistent with the measured RF/parameter values.\n"
        )
    if tag == "single-answer":
        return (
            "This is a single-answer question. Select the most appropriate optimization "
            "solution and enclose its number in \\boxed{{}} in the final answer. "
            "For example, \\boxed{C3}.\n"
            f"{p7_exclusion}"
            f"Potential root causes:\n{options_block}\n"
        )
    return (
        "This is a multiple-answer question. Select two to four possible optimization "
        "solutions and enclose their numbers in \\boxed{{}} in the final answer. "
        "For example, \\boxed{C3|C5} or \\boxed{C7|C11}. IDs in ASCENDING order.\n"
        "IMPORTANT: Multiple-answer REQUIRES 2-4 options. NEVER return a single option. "
        "Even if one root cause is dominant, list the related optimization actions that "
        "address the same root cause (e.g., power + tilt + A3 offset for an overshooting "
        "cell; power + azimuth + tilt for a coverage hole).\n"
        f"Potential root causes:\n{options_block}\n"
    )
