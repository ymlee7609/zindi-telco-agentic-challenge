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

### Stage C — Qwen 본 실행 (Batch 완료 + 이슈 발견)

| 단계 | 문제 수 | 결과 디렉토리 | 완료 | P7 fallback | Avg latency |
|------|---------|--------------|------|-------------|-------------|
| Smoke | 10 | `results_smoke/` | 2026-04-22 | 3/10 (30%) | 35.6s |
| Train eval 10 (v1) | 10 | `results_train_eval/` | 2026-04-22 | 6/10 (60%) | 28.2s |
| Train eval 50 (v1) | 50 | `results_train_eval_50/` | 2026-04-22 | 22/50 (44%) | 46.1s |
| Train eval 50 (v2) | 50 | `results_train_eval_50_v2/` | 2026-04-22 | 22/50 (44%) | 61.8s |
| **Train eval 50 (v3 RAG)** | 50 | `results_train_eval_50_v3/` | 2026-04-22 | **18/50 (36%)** | **34.6s** |
| Train eval 10 (v4 RAG+n=3) | 10 | `results_train_eval_v4/` | 2026-04-22 | **0/10** | 140s (5x cost) |
| Pilot v3 (0-49) | 50 | `results_pilot_v3/` | 2026-04-22 | 22/50 (44%) | 27.4s |
| **Batch A (50-249)** | 200 | `results_batch_a/` | 2026-04-23 | **134/200 (67%)** | 38.4s |
| **Batch B (250-499)** | 250 | `results_batch_b/` | 2026-04-23 | **187/250 (75%)** | 31.2s |

### Stage C 이슈 — Batch Fallback 급증

Train eval 50 v3 에서 fallback 18/50 (36%) 이던 것이 test Batch A/B 에서
**67% / 75% 로 급증**. 원인 가설:

1. **Train-Test 분포 차이**: train 2000 의 RAG precompute 로 유사도 매칭 → test scenario 는 train 에 직접 매칭이 안 되어 retrieval 품질 저하
2. **병렬 실행 시 OpenRouter latency 증가** — max iteration 도달 전에 Qwen reasoning 이 끝나지 않아 XML 오염 패턴 재발
3. **Long-tail test scenarios** — 특수 패턴 (P6 excessive tilt) 비율이 test 에 더 높을 가능성

**영향**: Submission v1 은 500/500 채워졌으나 실제 정확도는 train 검증 (IoU 0.22) 보다
낮을 가능성. 로컬 검증 불가 (test answer placeholder).

**대응 (Phase 1 남은 기간)**:
- Batch 단독 직렬 재실행 (OpenRouter rate 여유) → fallback 감소 검증
- v4 self-consistency 를 실패 의심 scenario 에만 적용
- Feature 확장 (traffic/signaling 추가)
- Phase 3 대비 Qwen fine-tuning (LoRA on train 2000)

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

### 4.1 완료 (2026-04-22 ~ 04-23)

- [x] Smoke 10 실행 / 분석 — prediction 7/10, empty 3 원인 XML 오염
- [x] Train eval 10/50 (baseline v1) — IoU 0.160
- [x] Train eval 10/50 (v2 XML+multi) — IoU 0.100 (regression)
- [x] **RAG 구현** (`agent/track_a/rag.py`) + v3 train eval 50 — **IoU 0.220 +38%**
- [x] **Self-consistency v4** — train 10 에서 fallback 0, 비용 5x 로 채택 X
- [x] Pilot v3 50 (test 0-49)
- [x] Batch A (test 50-249, 200 scenarios)
- [x] Batch B (test 250-499, 250 scenarios)
- [x] **Submission v1 생성** (500/500) — `agent/track_a/submission/submission_v1.csv`
- [x] **통합 submission** (Track A 500 + Track B 50) — `agent/common/submission/submission_combined.csv`
- [x] docs 전 영역 반영 (00_index, 03-1/03-2/03-3, 04_rag_architecture, 08_progress)

### 4.2 진행 예정 (Zindi 점수 확인 후)

- [ ] Zindi 사이트 `submission_combined.csv` 업로드 → Public leaderboard 점수 확인
- [ ] Challenge rule 재확인: Opus overlay 금지, Qwen 단독만 제출 가능
- [ ] Batch 개선 실험 (택 1 또는 복수):
  - **(A) Batch 직렬 재실행**: 병렬 latency 제거로 fallback 감소 검증 (비용 0)
  - **(B) Feature 확장**: traffic_data / signaling_plane_data 를 14-dim → 20-dim+ 로 확장 (RAG 품질 향상)
  - **(C) Self-consistency 선택 적용**: v1 에서 P7 fallback 된 343 scenario 만 n=3 재실행 (비용 1.5x)
  - **(D) LoRA fine-tuning**: train 2000 으로 Qwen3.5-35B-A3B 파인튜닝 (Phase 3 대비, 가장 큰 개선)

---

## 5. 파일 구조 (Track A 관련, 최종)

```
agent/
├── common/
│   ├── submission_example.csv           # Zindi 공식 550-row 템플릿
│   └── submission/
│       ├── merge_submission.py          # Track A/B 통합 merge 헬퍼
│       ├── submission_combined.csv      # 최종 제출 CSV (Track A 500 + Track B 50)
│       └── README.md
└── track_a/
    ├── agent.py                         # Qwen runner (RAG + XML re-ask + P7 fallback + self-consistency)
    ├── prompts.py                       # system prompt + 5 static few-shot + forced prompt
    ├── rag.py                           # 14-dim feature + train 2000 precompute + L2 retrieval
    ├── generate_submission.py           # result.csv → Zindi CSV (combined 자동 갱신)
    ├── eval_local.py                    # train 기반 IoU 측정
    ├── tools/
    │   └── scenario_summary.py          # Stage A scenario inline data 추출 헬퍼
    ├── results_smoke/                   # Smoke 10 (test 0-9)
    ├── results_smoke_1/                 # Smoke-of-smoke (1 scenario 검증)
    ├── results_train_eval/              # Train eval 10 (v1 baseline)
    ├── results_train_eval_v2/           # Train eval 10 (v2 XML+multi)
    ├── results_train_eval_v3/           # Train eval 10 (v3 RAG)
    ├── results_train_eval_v4/           # Train eval 10 (v4 RAG+n=3)
    ├── results_train_eval_50/           # Train eval 50 (v1)
    ├── results_train_eval_50_v2/        # Train eval 50 (v2)
    ├── results_train_eval_50_v3/        # Train eval 50 (v3 RAG) ← 채택된 버전
    ├── results_pilot/                   # Pilot 50 (v1, 구)
    ├── results_pilot_v3/                # Pilot 50 (v3 RAG, test 0-49) ← submission 기반
    ├── results_batch_a/                 # Batch A 200 (v3 RAG, test 50-249)
    ├── results_batch_b/                 # Batch B 250 (v3 RAG, test 250-499)
    └── submission/
        └── submission_v1.csv            # Track A 최종 제출본 (v3 RAG)

docs/track_a/
├── 03-1_architecture.md                 # Agent 아키텍처 (Mermaid, Obsidian 호환)
├── 03-2_topology.md                     # 무선 5G 토폴로지 (gNodeB/PCI/RSRP/SINR/A3 공식)
├── 03-3_problems.md                     # 2000 train 통계 + 7-pattern + Stage C 결과
├── 04_rag_architecture.md               # RAG 14-dim feature + retrieval + few-shot
└── 08_track_a_progress.md               # 본 문서 (진행 리포트)

.moai/
├── cache/
│   └── track_a_train_features.json      # RAG precompute (2000 entries, 14-dim + normalized)
└── plans/
    ├── track-a-opus-typed-glacier.md    # 전체 플랜
    └── track-a-opus-solutions.md        # Stage A 수작업 풀이 + P1~P7 패턴 라이브러리
```

## 6. 주요 수치 요약

| 항목 | 값 |
|------|-----|
| Train eval 50 (v3 RAG) IoU | **0.220** (v1 baseline 0.160 대비 +38%) |
| Train eval 50 (v3 RAG) exact | 11/50 (22%) |
| Train eval 50 (v3 RAG) P7 fallback | 18/50 (36%) |
| Test 500 scenarios 실행 | 500/500 완료 |
| Test 500 P7 fallback | 343/500 (68.6%) — train 검증 대비 악화 |
| Submission v1 평균 latency | 32.3s/scenario |
| RAG cache 크기 | 1.1 MB (2000 entries × 14-dim + stats) |
