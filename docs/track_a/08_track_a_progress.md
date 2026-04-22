# Track A 진행 경과 리포트

> 최종 업데이트: 2026-04-22 (Stage C Smoke 실행 중)
> 챌린지: Telco Troubleshooting Agentic Challenge — Track A (Wireless 5G Optimization)
> Phase 1 기간: 2026-04-03 ~ 2026-05-04 (submission unlimited)

---

## 1. 현재 상태 요약

- **전략 채택**: Track B 에서 검증된 "Opus 에뮬레이션 → Qwen 실행" 패턴을 Track A 로 이식
- **Phase 1 접근**: Qwen 단독 v1 + Opus overlay v2 2단 제출
- **코드 위치**: `agent/track_a/` (Track B `agent/track_b/agent.py` 와 격리)
- **LLM**: OpenRouter `qwen/qwen3.5-35b-a3b`, MAX_TOKENS=8192, MAX_ITERATIONS=20
- **서버**: `data/Track A/server.py` — `FASTAPI_PORT=7861` (test), `FASTAPI_PORT=7862 DATA_SPLIT=train` (로컬 검증용)

---

## 2. Stage 별 진행

### Stage A — Opus 에뮬레이션 수작업 풀이 (2026-04-22, 완료)

- 샘플: train[0, 1, 2, 3, 4, 5, 6, 10, 17, 25] + `examples/traces.json` 2건 = **총 12개**
- 결과: 내 예측 **9/10 정답** (train[4] 만 coverage tilt 패턴을 초기에 server issue 로 오판)
- 산출물: `.moai/plans/track-a-opus-solutions.md`
- 패턴 라이브러리 도출: **P1~P7** (Late handover, Ping-pong, Overshoot, Coverage hole, Server issue, Excessive downtilt, Insufficient data)

### Stage B — `agent/track_a/` 디렉토리 구축 (2026-04-22, 완료)

새로 작성한 파일:
- `agent/track_a/agent.py` — Qwen runner (Track A main.py Environment 재사용 + OpenRouter client + prompts 분리)
- `agent/track_a/prompts.py` — System prompt (A3 공식 + 7-pattern checklist + tool 순서) + 5 few-shot (traces 2 + train[0, 5, (1)])
- `agent/track_a/generate_submission.py` — Track A 전용 submission CSV 생성기 (Track A 열 채움)
- `agent/track_a/eval_local.py` — IoU 기반 로컬 정확도 측정기
- `agent/track_a/tools/scenario_summary.py` — scenario inline data 추출 헬퍼 (Stage A 에서 사용)

### Stage C — Qwen 본 실행 (진행 중)

| 단계 | 문제 수 | 결과 디렉토리 | 상태 |
|------|---------|--------------|------|
| Smoke | 10 | `agent/track_a/results_smoke/` | **실행 중** (test.json) |
| Smoke-train-eval | 30 | `agent/track_a/results_smoke_train/` | 대기 (train.json 로컬 검증) |
| Pilot | 50 | `agent/track_a/results_pilot/` | 대기 |
| Batch A | 200 | `agent/track_a/results_batch_a/` | 대기 |
| Batch B | 250 | `agent/track_a/results_batch_b/` | 대기 |

통과 기준:
- Smoke: tool 체인 정상 작동 (empty response ≤3, 평균 latency <90s)
- Smoke-train-eval: 로컬 accuracy (IoU mean) ≥ 0.3
- Pilot: 로컬 accuracy ≥ 0.4 → 미달 시 Stage B 프롬프트 튜닝 루프로 복귀
- Batch A/B: 완주 (timeout <10%)

---

## 3. 주요 발견 (Stage C 실행 중)

### 3.1 test.json 은 answer placeholder
- test.json 의 500 scenario 모두 `"answer": "To be determined"` — 공식 submission 대상
- **로컬 accuracy 측정은 train.json (2000, answer 실제값) 으로만 가능**
- → agent.py 에 `--source {server,test,train}` 옵션 추가; train server 는 `FASTAPI_PORT=7862 DATA_SPLIT=train` 으로 별도 기동

### 3.2 Qwen3.5-35B-A3B 관측된 특징 (Smoke 1건 기준)
- scenario 당 평균 15 tool_calls, 8 iterations
- latency ~90s (8k tokens 설정)
- `\boxed{C#}` 포맷 준수 양호 (few-shot 5건 효과)

### 3.3 포트 분리
- Track B 서버: 7860 (기존, Track B submission 완료 후에도 유지)
- Track A test: 7861
- Track A train: 7862

---

## 4. 다음 단계

- [x] Smoke 10 실행 개시
- [ ] Smoke 10 완료 → 결과 분석 (prediction 추출률, tool call 분포, latency 분포)
- [ ] Smoke-train-eval 30 실행 → 로컬 accuracy 측정 (IoU mean)
- [ ] Pilot 50 실행 (test.json)
- [ ] Batch A 200 + Batch B 250 → 500 전수
- [ ] Submission v1 생성 → Zindi 업로드
- [ ] Opus overlay 대상 선정 (v1 에서 실패/오답 의심 scenario ≤50)
- [ ] Submission v2 생성 (v1 + overlay)

---

## 5. 파일 구조 (Track A 관련)

```
agent/track_a/
├── agent.py                            # Qwen runner
├── prompts.py                          # system prompt + few-shot
├── generate_submission.py              # result.csv → Zindi CSV
├── eval_local.py                       # train 기반 로컬 accuracy
├── tools/
│   └── scenario_summary.py             # Stage A helper (scenario inline data 요약)
├── results_smoke_1/                    # 1 scenario smoke-of-smoke (검증)
├── results_smoke/                      # Smoke 10 (실행 중)
├── results_pilot/                      # Pilot 50 (대기)
├── results_batch_a/                    # Batch A 200 (대기)
├── results_batch_b/                    # Batch B 250 (대기)
└── submission/                         # Zindi CSV 저장소

docs/track_a/
└── 08_track_a_progress.md              # 본 문서

.moai/plans/
├── track-a-opus-typed-glacier.md       # 전체 플랜
└── track-a-opus-solutions.md           # Stage A 수작업 풀이 + P1~P7 패턴 라이브러리
```
