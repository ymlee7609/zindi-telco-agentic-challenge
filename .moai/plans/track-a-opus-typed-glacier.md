# Track A — Opus 에뮬레이션 풀이 → Qwen 실행 전략 → Qwen 실행

> 상태: Plan (Phase 1~2 탐색 완료, Phase 3 Review 진행 중)
> 작성: 2026-04-22
> 챌린지: Track A — Telco Troubleshooting and Optimization Agentic Challenge
> 기간: Phase 1 Open Practice (2026-04-03 ~ 05-04), submission unlimited

---

## 1. Context

### 1.1 왜 지금 Track A인가
- Track B (IP Networks, 50문제) 는 v6 full + Opus overlay 로 `submission_v6_full_v8.csv` (48/50 solved) 제출 완료
- Track A 는 아직 미착수. Phase 1 마감 2026-05-04 까지 약 12일 남음
- 이미 Track B 에서 검증된 **Opus 에뮬레이션 → Qwen 전략 수립 → Qwen 실행** 패턴을 Track A 에 이식

### 1.2 Track A 특징 (Track B 와 결정적 차이)
- **도메인**: 무선 5G 드라이브 테스트 최적화 (Track B 는 IP 네트워크 CLI 토폴로지/경로/장애)
- **문제 규모**: 2000 train + 500 test (Track B 는 50) → **40배 규모**
- **문제 형식 통일**: 모든 시나리오가 "drive test throughput degradation → optimization option 선택" 패턴
  - 선택지 C1~C22 전후로 구성
  - single-answer (\boxed{C9}) / multiple-answer (\boxed{C3|C5})
- **정답 내장**: train 뿐 아니라 **test.json 에도 `answer` 필드 존재** → 로컬 정확도 측정 가능 (제출 전 검증 루프 가능)
- **도구 풀**: 27개 tool (gNodeB location, cell-info, PCI/RSRP/SINR, throughput-logs, antenna gain/tilt/azimuth 계산 등)
- **제공 코드**: `data/Track A/main.py` (Agent runner), `server.py` (tool server, 수정 불가), `_types.py`, `utils.py`, `logger.py`
- **Few-shot 자원**: `data/Track A/examples/traces.json` 에 전문가 풀이 2건 (tool call trace + 완전한 추론 + `\boxed{C9}`, `\boxed{C22}`)

### 1.3 의도하는 결과
- Phase 1 submission: `result.csv` (id, prediction) 500행
- 로컬 검증 기준 정확도 최소 0.55 이상 (Track B 에서 Qwen3.5 단독 부정확 구간을 Opus overlay 로 커버했던 패턴과 동일한 보강 여지 확보)
- Phase 2/3 에서 재사용 가능한 agent/main.py 골격

---

## 2. Phase 1 — Exploration 결과 (완료)

### 2.1 파일 구조
```
data/Track A/
├── README.md                        # 챌린지 공식 설명
├── _types.py                        # 165 LOC, OpenAI-like ToolCall dataclass
├── logger.py                        # 56 LOC
├── main.py                          # 493 LOC, Environment + AgentsRunner (수정 대상)
├── server.py                        # 987 LOC, tool server (수정 불가)
├── utils.py                         # 169 LOC, extract_answer / compute_score
├── requirements.txt
├── data/Phase_1/
│   ├── train.json                   # 2000 scenarios (answer 포함)
│   └── test.json                    # 500 scenarios (answer 포함)
└── examples/traces.json             # 전문가 풀이 2건 (few-shot)
```

### 2.2 Scenario 스키마
```json
{
  "scenario_id": "UUID",
  "tag": "single-answer | multiple-answer",
  "task": {
    "description": "Analyze 5G network drive test data...\\boxed{{C5}}",
    "options": [{"id": "C1", "label": "..."}, ...],
    "allowed_tools": "all"
  },
  "answer": "C9" or "C2|C8|C11|C16",
  "context": {"description": "..."},
  "data": {...},
  "tools": [...]
}
```

### 2.3 27개 tool (main.py `endpoint_mapper`)
| 그룹 | Tool |
|------|------|
| Meta | get_available_tools, health, get_all_scenario |
| Cell 구성 | get_config_data, get_cell_info, get_gnodeb_location, get_all_cells_pci |
| User plane | get_user_plane_data, get_throughput_logs, get_user_location |
| Serving cell | get_serving_cell_pci, get_serving_cell_rsrp, get_serving_cell_sinr, get_rbs_allocated_to_user |
| Neighbor cell | get_neighboring_cells_pci, get_neighboring_cell_rsrp |
| Signaling | get_signaling_plane_event_log |
| 계산 유틸 | judge_mainlobe_or_not, calculate_horizontal_angle, calculate_tilt_angle, calculate_pathloss, calculate_overlap_ratio |
| KPI/MR | get_kpi_data, get_mr_data |
| Action | optimize_antenna_gain |

### 2.4 AgentsRunner.run() 흐름 (main.py:248~370)
1. `task.description + options` → user message
2. 최대 `max_iterations` 반복 (기본 10, Track B 경험상 15~30 권장)
3. LLM tool_calls → Environment.execute → tool result 누적
4. tool_calls 없으면 최종 답변으로 간주 → `status=solved`
5. `free_mode`: 최종 답이 공란이면 single/multiple-answer 프롬프트로 강제 양식 재요청
6. `extract_answer` → `\boxed{...}` 추출

### 2.5 examples/traces.json 의 정석 풀이 패턴
두 샘플에서 공통된 tool 사용 순서:
1. `get_throughput_logs` — throughput 급락 구간 감지
2. `get_serving_cell_pci(time=degradation window)` — PCI 유지 여부 (=late handover 가능성)
3. `get_cell_info(pci)` — A3 Offset, Power, PdcchOccupiedSymbolNum, Neighbor 목록 확인
4. `get_serving_cell_rsrp`, `get_serving_cell_sinr` — 신호 품질
5. `get_neighboring_cells_pci`, `get_neighboring_cell_rsrp` — 강한 이웃 셀 존재 여부
6. 추론: `neighbor_rsrp - serving_rsrp vs. A3 Offset + Hysteresis` → handover 실패 원인 → 해당 Option 선택

→ 핵심은 **A3 Offset handover 임계치 평가 공식**: `Neighbor_RSRP > Serving_RSRP + Offset + Hysteresis` (미충족 시 C22 "Decrease A3 Offset" 같은 조정 선택).

### 2.6 Track B 재사용 가능 / 재사용 불가 자산
| Track B 자산 | Track A 에 재사용? |
|-------------|-------------------|
| `agent/track_b/agent.py` (1200+ LOC, v6) | 부분 재사용 (resume, MAX_TOKENS=8192, OpenRouter client, Empty response 대응) |
| `detect_question_type` / Topology/Path/Fault 분기 | **재사용 불가** — 문제 패턴이 완전히 다름 |
| `load_scenario_devices` IP 화이트리스트 | **재사용 불가** — Track A 는 장비 식별자 대신 PCI/gNodeB ID |
| `build_type_hint` 전략 힌트 | **아이디어는 재사용** — Track A 전용 힌트 (drive test 정석 흐름) 로 새로 작성 |
| OpenRouter 결제/엔드포인트/모델 설정 | 완전 재사용 |
| submission CSV generator (`generate_submission.py`) | 포맷 살짝 수정 후 재사용 (id, prediction 2-column, newline 평탄화) |

---

## 3. Phase 2 — Design (Opus 에뮬레이션 → Qwen 전략 → Qwen 실행)

### 3.1 Stage A: Opus 에뮬레이션 풀이 (오프라인, LLM 호출 없음)

목적: 내가 (Opus 4.7) 직접 문제를 수작업으로 풀어보며 **최적 tool 호출 시퀀스** 와 **추론 골격** 을 뽑아내, Qwen 이 흉내낼 수 있는 형태로 문서화.

대상 문제 (확정):
- **train.json 앞 10개 샘플** (answer 있음, 정확도 피드백 가능)
- `examples/traces.json` 전문가 풀이 2건 포함 → **총 12개 풀이 데이터** 확보
- 범주 분산 목표: single-answer 5개 + multiple-answer 5개 (train 샘플 스캔 후 tag 분포 확인해 조정)

절차:
1. 각 샘플에 대해 task description / options 읽기
2. "만약 내가 LLM 이라면 어떤 tool 을 어떤 순서로 부를까?" 직접 계획 (실제 API 호출은 아직 안 함)
3. scenario 의 `context`, `data`, `tools` 필드에 미리 계산된 값이 있는지 확인 → tool call 수 최소화 경로 파악
4. ground truth 대비 내 추론 정답 여부 자체 기록
5. 결과물: `.moai/plans/track-a-opus-solutions.md` (샘플 ID, 선택 이유, tool sequence, 최종 답안, 매칭 여부)

산출물: **Qwen 시스템 프롬프트 초안** + **few-shot messages** + **tool 호출 가이드**

### 3.2 Stage B: Qwen 실행 전략 수립

Stage A 결과를 코드로 옮김. 새 파일 `agent/track_a/agent.py` (Track B 와 격리) 에 다음 반영:

1. **System prompt** (영어): drive test degradation 분석 정석 흐름 + A3 offset 공식 + PCI 유지/변경 케이스 구분 + 최종 `\boxed{}` 양식 강조
2. **Few-shot**: `examples/traces.json` 2건을 `messages` 앞부분에 user/assistant 쌍으로 삽입
3. **Tool 사용 가이드** (system prompt 내): "throughput 로그 먼저 → PCI 시계열 → cell_info → RSRP/SINR → neighbor" 순서 제안
4. **Option parser hardening**: Track B 경험 - `\boxed{}` 외 pattern (bare `C9`, `**C9**`) 도 `extract_answer` 로 폴백
5. **Empty response 대응**: MAX_TOKENS=8192, 빈 응답 반복 시 free_mode forced 프롬프트
6. **Multiple-answer 특수처리**: `|` 구분, 오름차순 (C11|C2 → C2|C11) 강제
7. **Resume / idempotent**: `result.csv` 스캔 후 미완 scenario 만 실행 (Track B `--fresh` 패턴)
8. **Dry-run 검증**: test set 20~30 샘플만 먼저 돌려 로컬 accuracy 확인 → 문제 시 시스템 프롬프트/few-shot 튜닝 루프
9. **서버 구동**: `cd data/Track\ A && python server.py` 별도 tmux 세션 (port 7860, Track B 와 동일 포트 주의 → Track B 서버는 중지 후 실행)

추가 산출물:
- `agent/track_a/generate_submission.py` — Track B 의 `generate_submission.py` 포크, 2-column 공식 스키마 강제, newline 평탄화
- `agent/track_a/prompts.py` — system prompt / few-shot 분리 관리

### 3.3 Stage C: Qwen 본 실행 (확정)

단계적 스케일업 **Smoke 10 → Pilot 50 → Batch A 250 → Batch B 250** (Track B 의 8192 토큰 교훈 적용):
1. **Smoke (10 문제)**: test.json 앞 10개 → 로컬 accuracy, empty response 빈도, 평균 latency 확인. 결과 `agent/track_a/results_smoke/`
2. **Pilot (50 문제)**: test 0~49 → 정확도 타입별 분포 점검, timeout 조정. 결과 `agent/track_a/results_pilot/`
3. **Batch A (test 50~249, 200 문제)**: 결과 `agent/track_a/results_batch_a/`
4. **Batch B (test 250~499, 250 문제)**: 결과 `agent/track_a/results_batch_b/`
5. **Retry pass**: forced_answer / timeout 발생 문제만 별도 `results_retry/` 에서 재실행
6. **Opus overlay pass**: Qwen 이 명백히 틀린 문제만 Opus 에뮬레이션으로 재풀이 → overlay CSV 작성 (4.4 참조)

각 단계 통과 기준:
- Smoke: 10개 중 tool 체인이 정상 동작 (empty response 3건 이하, 평균 latency <90s), 로컬 accuracy ≥ 0.3
- Pilot: 50개 로컬 accuracy ≥ 0.4 → 미달 시 Stage B 프롬프트 튜닝 루프로 복귀
- Batch A/B: 완주 (timeout 비율 <10%)

### 3.4 결과물 스펙 (확정: Qwen 단독 v1 + Opus overlay v2)
- `agent/track_a/submission/submission_v1.csv` — Qwen 단독 500행, Batch B 완주 직후 생성, 1차 제출
- `agent/track_a/submission/submission_v2.csv` — Qwen v1 + Opus overlay (틀린 문제만 보강), 2차 제출
- `agent/track_a/submission/generate_submission.py` (재생성 스크립트, Track B 포크)
- 진행 리포트 `docs/08_track_a_progress.md`

---

## 4. Phase 3 — Review (사용자 확정 반영)

### 4.1 사용자 결정 요약 (완료)
1. Opus 에뮬레이션 샘플: **train 10개 + traces 2개 = 총 12개 few-shot 자원**
2. Qwen 스케일업: **Smoke 10 → Pilot 50 → Batch 250 × 2**
3. 코드 분리: **`agent/track_a/` 신규 디렉토리** (Track B 의 `agent/track_b/agent.py` 건드리지 않음)
4. Phase 1 제출: **v1 (Qwen 단독) + v2 (Opus overlay) 2단 제출**

### 4.2 Critical files to be modified / created
| 경로 | 액션 | 비고 |
|------|------|------|
| `agent/track_a/agent.py` | **신규** | main.py 파생, Qwen 전용 |
| `agent/track_a/prompts.py` | **신규** | system prompt + few-shot |
| `agent/track_a/generate_submission.py` | **신규** | Track B 포크 |
| `agent/track_a/results_smoke/` | 런타임 생성 | |
| `agent/track_a/results_pilot/` | 런타임 생성 | |
| `agent/track_a/results_batch_{a,b}/` | 런타임 생성 | |
| `agent/track_a/submission/` | 런타임 생성 | |
| `.moai/plans/track-a-opus-solutions.md` | **신규** | Stage A 수작업 풀이 로그 |
| `docs/08_track_a_progress.md` | **신규** | 진행 리포트 |
| `data/Track A/main.py` | **수정 안 함** | 공식 제출 때 복사 후 개조 |

### 4.3 재사용 함수 (Track B → Track A)
- `agent/track_b/agent.py` 의 OpenRouter client + resume scan 로직 → 동일 구조로 복사
- `agent/track_b/submission/generate_submission.py` 의 CSV quoting + newline flatten → 거의 그대로 사용
- `utils.py` (`extract_answer`, `compute_score`) 는 Track A 측 것 그대로 사용

### 4.4 End-to-end 검증 절차
1. `cd data/Track\ A && python server.py &` → `curl http://localhost:7860/health` 로 기동 확인
2. `cd data/Track\ A && curl -s http://localhost:7860/tools | jq length` → 27 이어야 함
3. Stage A: `.moai/plans/track-a-opus-solutions.md` 수작업 작성 후 리뷰
4. Stage B: `python agent/track_a/agent.py --max-samples 3 --save-dir agent/track_a/results_smoke/` → 3문제 smoke
5. 로컬 accuracy: `python agent/track_a/eval_local.py agent/track_a/results_smoke/result.csv` (간단 스크립트, test.json answer 와 매칭)
6. 정확도 ≥ 2/3 이면 Stage C 스케일업, 미만이면 Stage B 프롬프트 튜닝 루프로 돌아감
7. 최종 submission: `python agent/track_a/generate_submission.py --from agent/track_a/results_batch_b/result.csv --out agent/track_a/submission/submission_v1.csv`

### 4.5 리스크 / 완화
| 리스크 | 완화 |
|-------|-----|
| 500문제 × 평균 30초 = 4시간+ OpenRouter 비용 | 단계적 실행, pilot 결과로 ROI 판단 후 진행 |
| 포트 7860 Track B 서버와 충돌 | Track B 서버 정지 후 실행 or Track A 서버 별도 포트 옵션 |
| Qwen 무선 도메인 지식 부족 (A3 offset 계산 등) | few-shot 2건 + system prompt 에 공식 명시 |
| Empty response / reasoning 폭주 | MAX_TOKENS=8192 + free_mode forced 재질의 |
| Multiple-answer 순서/구분자 불일치 | `extract_answer_all` 에서 split → sort → rejoin 강제 |

---

### 4.6 Opus Overlay 정책 (Stage C 후반부)

Qwen v1 결과 중 overlay 대상 선정 기준:
1. **status != "solved"** (timeout_forced, empty_response, unresolved)
2. **local accuracy = 0** (test.json answer 와 불일치) — test 에 answer 있으므로 가능
3. **tool_calls 수가 비정상적으로 적음 (<3)** — context 부족 의심
4. overlay 상한: v1 에서 실패/오답으로 분류된 상위 50 문제까지만 (비용 통제)

Overlay 절차:
- 각 대상 scenario 에 대해 나 (Opus) 가 `.moai/plans/track-a-opus-solutions.md` 포맷으로 수작업 풀이
- `agent/track_a/submission/overlay_patch.csv` 에 (scenario_id, prediction) 기록
- `generate_submission.py --base submission_v1.csv --overlay overlay_patch.csv --out submission_v2.csv` 로 병합

---

## 5. 상태 / 다음 액션

- [x] Phase 1 Exploration 완료 (파일 구조, 문제 스키마, traces.json, main.py 흐름 파악)
- [x] Phase 3 사용자 확인 1 라운드 (4 질문 확정)
- [x] 본 플랜 finalize
- [ ] ExitPlanMode 승인 대기
- [ ] 승인 후: Stage A (train 10 + traces 2 수작업 풀이 → `.moai/plans/track-a-opus-solutions.md`)
- [ ] Stage B: `agent/track_a/` 디렉토리 구현 (agent.py, prompts.py, generate_submission.py)
- [ ] Stage C: Smoke 10 → Pilot 50 → Batch A/B 250×2
- [ ] v1 제출 → Opus overlay → v2 제출
- [ ] `docs/08_track_a_progress.md` 진행 리포트 작성
