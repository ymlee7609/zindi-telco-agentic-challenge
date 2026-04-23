# Track A Agent Architecture

> 대상: `agent/track_a/agent.py` 구조 설명서
> 최종 업데이트: 2026-04-23 | 버전: **v4 (P0+P1+P2, Zindi public 0.3174)**
> 주요 변경: XML 복구, multi retry, P7 억제, XML budget 분리, RAG 22-dim, self-consistency overlay

## 1. 전체 흐름

```mermaid
flowchart TD
    START([CLI run]) --> ENV[Load .env OPENROUTER_API_KEY]
    ENV --> INIT[Environment client to server 7861 or 7862]
    INIT --> RUNNER[QwenRunner: provider + OpenAI client]

    RUNNER --> LOAD{scenario source}
    LOAD -->|server| SVRGET[GET scenario all]
    LOAD -->|train| FILE[load train.json]
    LOAD -->|test| FILE2[load test.json]

    SVRGET --> SLICE[slice start_idx to start_idx plus max_samples]
    FILE --> SLICE
    FILE2 --> SLICE

    SLICE --> FILT{--rerun-fallback?}
    FILT -->|yes| FBFILTER[eval_detail.jsonl 로드<br/>fallback_used/unresolved/empty sid 만 필터]
    FILT -->|no| RESUME{result.csv exists and not fresh}
    FBFILTER --> RESUME
    RESUME -->|done| NEXT[next scenario]
    RESUME -->|pending| RUN[runner.run scenario]

    RUN --> PROMPT[build_system_prompt tag<br/>single/multi variant]
    PROMPT --> MSGS[messages: system + static 5 + RAG top-3 + user]
    MSGS --> LOOP{iteration loop max 25<br/>iter_num separate from xml_retry_budget}

    LOOP -->|tool_calls| TOOL[Environment.execute: HTTP GET tool endpoint]
    TOOL --> LOOP

    LOOP -->|content with boxed| EXTRACT[normalize_answer via boxed regex]
    LOOP -->|xml polluted content| XMLB{xml_retry_budget > 0?}
    XMLB -->|yes| RE_ASK[coach no-XML re-ask<br/>iter_num 증가 X]
    RE_ASK --> LOOP
    XMLB -->|no| BREAK[loop break]
    LOOP -->|max iter| BREAK

    BREAK --> RECOV[find_last_valid_boxed_answer<br/>scenario_start_idx 이후 assistant 스캔]
    RECOV -->|찾음| EXTRACT
    RECOV -->|없음| FORCED_NP7[forced_answer_prompt allow_p7=False]

    FORCED_NP7 --> CALL2[1차 forced LLM call]
    CALL2 --> MULTI{tag=multi-answer<br/>& norm lacks '|'?}
    MULTI -->|yes| MRETRY[multi-answer retry max 2x<br/>'2-4 options로 다시 제출']
    MRETRY --> MULTI
    MULTI -->|no| STILLEMPTY{extracted empty?}
    STILLEMPTY -->|yes| FORCED_P7[forced_answer_prompt allow_p7=True<br/>final safety net]
    FORCED_P7 --> EXTRACT
    STILLEMPTY -->|no| EXTRACT

    EXTRACT --> EMPTY{prediction empty}
    EMPTY -->|yes| FB[insufficient_data_option C#]
    EMPTY -->|no| SC{--num-attempts>1?}
    SC -->|yes| VOTE[majority_vote across N attempts]
    SC -->|no| WRITE
    VOTE --> WRITE
    FB --> WRITE[result.csv + eval_detail.jsonl]
    WRITE --> NEXT
    NEXT --> SLICE

    style START fill:#4CAF50,color:#fff
    style WRITE fill:#2196F3,color:#fff
    style TOOL fill:#FF9800,color:#fff
    style FORCED_NP7 fill:#9C27B0,color:#fff
    style FORCED_P7 fill:#673AB7,color:#fff
    style FB fill:#f44336,color:#fff
    style RE_ASK fill:#607D8B,color:#fff
    style RECOV fill:#009688,color:#fff
    style MRETRY fill:#E91E63,color:#fff
    style VOTE fill:#FFC107
```

## 2. 디렉토리 구조

```
agent/track_a/
├── agent.py                 # 본 문서 대상 — Qwen runner 메인 (XML recovery + multi retry + SC)
├── prompts.py               # SYSTEM_PROMPT + MULTI_ANSWER_EMPHASIS + forced_answer_prompt(allow_p7)
├── rag.py                   # 22-dim feature + L2 retrieval + feature_hint
├── generate_submission.py   # result.csv → Zindi submission CSV (Track A 열)
├── eval_local.py            # IoU 기반 로컬 정확도 측정 (train.json answer 와 비교)
├── tools/
│   └── scenario_summary.py  # scenario inline data 추출 헬퍼 (Stage A)
├── results_smoke_1/         # 1 scenario 검증
├── results_smoke/           # Smoke 10 (test.json)
├── results_train_eval/      # train 10 (v1 baseline)
├── results_train_eval_50/   # train 50 (v1)
├── results_train_eval_50_v2/ # train 50 (v2 XML+multi 시도)
├── results_train_eval_50_v3/ # train 50 (v3 RAG 14-dim) ← 이전 채택
├── results_train_eval_50_v4/ # train 50 (v4 P0+P1+P2) ← 최신 검증 IoU 0.3173
├── results_pilot_v3/        # Pilot 50 (v3)
├── results_batch_a/         # Batch A 200 (v3, test 50-249)
├── results_batch_b/         # Batch B 250 (v3, test 250-499)
├── results_batch_v2_a/      # Batch v2 A 250 (P0+P1+P2, test 0-249)
├── results_batch_v2_b/      # Batch v2 B 250 (P0+P1+P2, test 250-499)
├── results_batch_v2_a_sc/   # SC n=3 on fallback 23건 (part A)
├── results_batch_v2_b_sc/   # SC n=3 on fallback 20건 (part B)
└── submission/
    ├── submission_v1.csv      # Zindi 0.149
    ├── submission_v2.csv      # v2 base (SC 없음)
    └── submission_v2_sc.csv   # v2 final (SC overlay) — Zindi 0.3174
```

## 3. Provider 설정

`agent/track_a/agent.py:PROVIDERS` (Track B 의 PROVIDERS 일부 포팅):

| provider | base_url | model | env_key |
|----------|----------|-------|---------|
| **openrouter** (default) | `openrouter.ai/api/v1` | `qwen/qwen3.5-35b-a3b` | `OPENROUTER_API_KEY` |
| huggingface | `router.huggingface.co/novita/v3/openai` | `qwen/qwen3.5-35b-a3b` | `HF_TOKEN` |
| dashscope | `dashscope.aliyuncs.com/...` | `qwen3.5-flash` | `DASHSCOPE_API_KEY` |
| groq | `api.groq.com/openai/v1` | `llama-3.3-70b-versatile` | `GROQ_API_KEY` |
| local | `localhost:8000/v1` | `Qwen/Qwen3.5-35B-A3B` | (없음) |

CLI: `--provider openrouter --model <override>` 또는 `LLM_PROVIDER` env var.

## 4. Tool Server 통합

Track A 공식 server (`data/Track A/server.py`) 가 27개 tool 엔드포인트 노출 (`/tools` 에서 20개 동적 반환).

| Group | Tools |
|-------|-------|
| Throughput | `get_throughput_logs`, `get_user_plane_data` |
| Serving cell | `get_serving_cell_pci`, `get_serving_cell_rsrp`, `get_serving_cell_sinr`, `get_rbs_allocated_to_user` |
| Neighbor | `get_neighboring_cells_pci`, `get_neighboring_cell_rsrp` |
| Cell config | `get_cell_info`, `get_config_data`, `get_gnodeb_location`, `get_all_cells_pci` |
| User | `get_user_location` |
| Signaling | `get_signaling_plane_event_log` |
| KPI/MR | `get_kpi_data`, `get_mr_data` |
| 계산 유틸 | `judge_mainlobe_or_not`, `calculate_horizontal_angle`, `calculate_tilt_angle`, `calculate_pathloss`, `calculate_overlap_ratio` |
| Action | `optimize_antenna_gain` |
| Meta | `get_available_tools`, `health`, `get_all_scenario` |

각 tool 은 HTTP GET `/{endpoint}?param=value` 형식. `X-Scenario-Id` header 로 시나리오 격리.

서버 기동:
```bash
cd "data/Track A"
FASTAPI_PORT=7861 python3 server.py                       # test (default)
FASTAPI_PORT=7862 DATA_SPLIT=train python3 server.py      # 로컬 정확도 검증용
```

## 5. 프롬프트 전략 (`prompts.py`)

### SYSTEM_PROMPT 핵심 섹션

1. **역할** — 5G RAN optimization expert
2. **A3 Handover 공식**
   `Neighbor_RSRP > Serving_RSRP + (A3Offset × 0.5 dB) + (A3Hyst × 0.5 dB)`
3. **Tool 호출 권장 순서** — throughput → serving PCI → cell_info → RSRP/SINR → neighbors
4. **7-Pattern 진단 체크리스트** (P1~P7) — `.moai/plans/track-a-opus-solutions.md` §4 의 패턴 라이브러리
5. **답변 포맷 강제** — `\boxed{C#}` (single) / `\boxed{C#|C#|...}` (multiple, 오름차순)
6. **Protocol Rules** — 네이티브 tool_calls 사용 강제 (XML `<tool_call>` 금지), Insufficient data fallback 의무

### P1-3: Tag 별 system prompt 분기 (`build_system_prompt(tag)`)

- `tag == "single-answer"` → SYSTEM_PROMPT 그대로 사용
- `tag == "multiple-answer"` → SYSTEM_PROMPT + **MULTI_ANSWER_EMPHASIS** (multi 강조 preamble)
  - "YOU MUST return 2-4 options. NEVER return a single option."
  - P3 Overshoot / P4 Coverage hole / Mixed 조합 예시를 상단 재배치

### FEW_SHOT_EXAMPLES (5건, 정적)

| # | 출처 | 패턴 | 답 |
|---|------|------|-----|
| 1 | traces.json[0] | P1 Late handover | `\boxed{C9}` |
| 2 | train[0] | P2+P3 Ping-pong + Overshoot | `\boxed{C2|C8|C11|C16}` |
| 3 | train[1] | P5 Server issue | `\boxed{C9}` |

(traces.json[1] 와 train[5] 는 system prompt 의 패턴 설명에 흡수)

### Dynamic RAG few-shot (22-dim + feature_hint)

정적 few-shot 뒤에 RAG top-3 neighbor 가 동적으로 붙음 (`agent.py:QwenRunner.run()`):
- `retrieve_similar(scenario, k=3, same_tag_only=True, exclude_sid=sid)`
- `format_few_shot_from_retrieval()` 가 P2-3 으로 pattern hint 주입:
  - 예: `(Similar pattern: ping-pong (PCI trans=3, low A3=2.5)) \boxed{C19}`

### forced_answer_prompt(tag, options_block, allow_p7=True)

답변 추출 실패 시 `single-answer` / `multiple-answer` 별 강제 양식 재요청.

**P0-3: `allow_p7=False` 모드** (1차 forced 재시도에서 사용) — "Insufficient data" 옵션 선택을 명시적으로 금지.
2차 safety net 시에만 `allow_p7=True` 로 허용하여 fallback 억제.

## 6. Resume / Idempotency

- `result.csv` (scenario_id, prediction) 헤더 + 행
- 기본 동작: 기존 result.csv 의 scenario_id 를 skip
- `--fresh` flag: 기존 결과 무시, 처음부터 재실행
- `--start-idx N --max-samples M`: scenario 슬라이스 (Pilot/Batch 분할 실행)
- **`--rerun-fallback PATH`**: 지정된 eval_detail.jsonl 에서 `fallback_used=True`
  / `status=unresolved` / empty prediction sid 를 필터링하여 그 시나리오만 재실행.
  P2-2 self-consistency 용도 (`--num-attempts 3 --temperature 0.5` 와 조합).

## 6.1 XML Recovery / Multi-retry / Forced Fallback 계층 (P0)

`QwenRunner.run()` 의 iteration 루프 종료 후 다음 안전망이 순서대로 동작:

1. **P0-2 XML recovery** — `find_last_valid_boxed_answer(messages, scan_from_idx)`
   가 현재 scenario user 메시지 이후 (`scenario_start_idx`) 의 assistant 메시지 중
   XML 오염 없고 `\boxed{...}` 포함 + extract_answer 성공하는 것을 찾아 복구 →
   `status="recovered"` 설정.
   (버그 주의: RAG few-shot 의 `(Similar solved example) \boxed{...}` 메시지를 잘못
   복구하지 않도록 scan_from_idx 필수)

2. **P0-3 1차 forced** — `forced_answer_prompt(tag, opts_block, allow_p7=False)`
   로 P7 억제 프롬프트 전송, 1회 LLM 호출.

3. **P0-1 Multi retry** — tag 가 `multiple-answer` 인데 응답에 `|` 없으면
   "2-4 개로 다시 제출" 메시지로 최대 2회 재시도.

4. **Final safety net** — 여전히 extract_answer 가 빈 경우 `allow_p7=True` 로
   마지막 forced 호출 (P7 선택도 허용).

5. **insufficient_data_option fallback** — 위 단계에서도 prediction 이 비면
   옵션 목록에서 "Insufficient data" 라벨의 C# 를 자동 선택하고
   `fallback_used=True` 마킹.

## 6.2 XML Retry Budget (P1-1)

기존 구조 (for 루프 기반 `iter in range(max_iterations)`) 는 XML 오염 재질의가
iteration 에 카운트되어 max_iter 를 빠르게 소진. v4 에서는 while 루프 + 별도
`xml_retry_budget=5` 카운터로 분리:

- Tool_call 또는 최종 답변 step → `iter_num += 1`
- XML 오염 재질의 → `xml_retry_budget -= 1` (iter_num 증가 X)
- `xml_retry_budget <= 0` 시 루프 break 후 복구 단계로 이동

`max_iterations` 기본값도 20 → **25** 로 상향.

## 7. 평가 / 정확도 측정

`agent/track_a/eval_local.py result.csv --source train`:

- **IoU score**: `|pred ∩ truth| / |pred ∪ truth|`, single 정확 일치 = 1.0, multiple partial 부분 점수
- 통계: Total / Exact / Partial / Wrong / Empty / Mean IoU / Per-tag breakdown
- test.json 은 모든 answer 가 `"To be determined"` 이므로 실제 채점은 Zindi 서버에서만 가능

## 8. 진행 상태 (Stage D 완료)

| 단계 | 결과 | 비고 |
|------|------|------|
| Smoke 10 (test) | 10/10 solved, empty 3건 | XML 오염 발견 |
| Train eval 50 v1 | IoU 0.160, P7 fallback 22/50 | baseline |
| Train eval 50 v3 (RAG 14-dim) | IoU 0.220, P7 fallback 18/50 | RAG 최초 도입 |
| **Train eval 50 v4 (P0+P1+P2)** | **IoU 0.3173, P7 fallback 5/50** | **G3 게이트 통과** |
| Pilot v3 50 (test 0-49) | - | 완료, 병합됨 |
| Batch A/B (test, 구) | v1 submission 기반, Zindi 0.149 | 아카이브 |
| **Batch v2 A/B 500 (test)** | fallback 43/500 (8.6%), multi 62/500 | 병렬 2분할 serial |
| **Batch v2 SC (fallback 43건)** | 전원 유효 답 생성 (fallback 0) | n=3 voting |
| **submission_v2_sc (최종)** | multi 67/500 (실제 67 정확 일치) | **Zindi public 0.3174** |

## 9. 알려진 한계 / 향후 개선

### 해결된 한계 (v1 → v4)
- ~~XML 오염으로 답변 누락~~ → P0-2 XML recovery + P1-1 XML retry budget 분리
- ~~Multi-answer 예측 부재 (3/500)~~ → P0-1 multi retry + P1-3 tag별 system prompt
- ~~P7 fallback 과잉 (68.6%)~~ → P0-3 allow_p7=False 1차 forced

### 잔존 한계
- 로컬 train IoU 0.3173 = Zindi 0.3174 → 추가 개선 여지는 모델 성능 자체에 의존
- 22-dim feature 에도 반영 안되는 패턴: neighbor PCI별 동적 RSRP trend, MR 데이터 variance 정밀도
- Single-answer 오답 29/42 (69%) → pattern 구분이 여전히 어려운 영역 존재

### 향후 가능 실험
1. RAG feature 확장 (22 → 30 dim): traffic_data, signaling_plane, MR 추가
2. LoRA fine-tuning (Phase 3 대비): train 2000 으로 Qwen3.5-35B-A3B 파인튜닝
3. Embedding 기반 retrieval: BAAI/bge-m3 등 LLM embedding 활용
4. Ensemble: 다른 provider (HF/DashScope) 와 투표
