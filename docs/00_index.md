# Zindi Telco Agentic Challenge — 문서 인덱스

> 최종 업데이트: 2026-04-23 (Day 1 저녁, Opus 검증 종결 후)
> 문서 구조: **공통 / Track A / Track B** 3영역 분리
> **Track B 최고점**: Zindi **0.48** (serial 018, v11 baseline 0.20 대비 +140%) — Opus 검증으로 Q25/Q28 정답 교체
> **Track A 점수**: Zindi Public **0.3174** (serial v1 RAG 기준)

---

## 디렉토리 구조

```
docs/
├── 00_index.md                         # 본 인덱스 (전체 네비게이션)
├── common/                             # 챌린지 전반 공통 자료
├── track_a/                            # Track A (Wireless 5G Optimization)
└── track_b/                            # Track B (IP Network Troubleshooting)
```

---

## 공통 (docs/common/)

챌린지 전반에 걸쳐 참조되는 문서. Track A/B 에 무관하게 유효.

| # | 파일 | 설명 | 상태 |
|---|------|------|------|
| 01 | [common/01_first_challenge_overview.md](common/01_first_challenge_overview.md) | 1차 AI Telco Troubleshooting Challenge (LLM 파인튜닝, 종료) | 종료 |
| 02 | [common/02_agentic_challenge_overview.md](common/02_agentic_challenge_overview.md) | Agentic Challenge 공식 정보 (트랙/상금/규칙/타임라인) | 완료 |
| 04 | [common/04_data_analysis.md](common/04_data_analysis.md) | Track A + Track B 데이터 구조 및 상세 분석 (submission_example 포함) | 완료 |

---

## Track A (docs/track_a/)

무선 5G 드라이브 테스트 최적화 트랙. 2000 train + 500 test scenarios, 22 options per question,
single / multiple answer.

| # | 파일 | 설명 | 상태 |
|---|------|------|------|
| 03-1 | [track_a/03-1_architecture.md](track_a/03-1_architecture.md) | Track A 에이전트 아키텍처 (Mermaid + provider/tool/prompt 흐름) | 완료 |
| 03-2 | [track_a/03-2_topology.md](track_a/03-2_topology.md) | 무선 5G 네트워크 토폴로지 (gNodeB/PCI/RSRP/SINR/A3 handover) | 완료 |
| 03-3 | [track_a/03-3_problems.md](track_a/03-3_problems.md) | Phase 1 문제 분석 + 7-pattern library (P1~P7) | 완료 |
| 04 | [track_a/04_rag_architecture.md](track_a/04_rag_architecture.md) | RAG 동작 구조 (22-dim feature + retrieval + feature_hint + SC overlay) | 22-dim 확장 |
| 08 | [track_a/08_track_a_progress.md](track_a/08_track_a_progress.md) | Track A 진행 리포트 | 최신 |

관련 자원 (repo 내):
- 풀이 로그: `.moai/plans/track-a-opus-solutions.md` — train 10 + traces 2 Opus 수작업 풀이 (9/10 정확, P1~P7 패턴 라이브러리)
- 플랜: `.moai/plans/track-a-opus-typed-glacier.md` — Stage A/B/C 실행 플랜
- 에이전트: `agent/track_a/agent.py`, `agent/track_a/prompts.py`
- 결과: `agent/track_a/results_{smoke,pilot,batch_a,batch_b}/` (실행 중 생성)

---

## Track B (docs/track_b/)

IP 네트워크 토폴로지 / 경로 / 장애 트랙. Phase 1 50문제, Exact Match 채점.

| # | 파일 | 설명 | 상태 |
|---|------|------|------|
| 03-1 | [track_b/03-1_architecture.md](track_b/03-1_architecture.md) | Track B 에이전트 아키텍처 (Mermaid) | 완료 |
| 03-2 | [track_b/03-2_topology.md](track_b/03-2_topology.md) | IP 네트워크 토폴로지 설명 + D2/SVG (Traditional + PJ) | 완료 |
| 03-3 | [track_b/03-3_problems.md](track_b/03-3_problems.md) | 50문제 유형별 분석 (Topology/Path/Fault) | 완료 |
| 03-3-1 | [track_b/03-3-1_problems_detail.md](track_b/03-3-1_problems_detail.md) | 50문제 상황·과제·단서 상세 | 완료 |
| 05 | [track_b/05_track_b_strategy.md](track_b/05_track_b_strategy.md) | Track B 전략 가이드 | 완료 |
| 06 | [track_b/06_progress_report.md](track_b/06_progress_report.md) | Track B 진행 경과 리포트 (v1~v12, **Zindi 0.20→0.44**) | 최신 (2026-04-23 Day 1) |
| - | [track_b/answers_ledger.md](track_b/answers_ledger.md) | 50문제 답변 원장 (Q25/Q28 Opus 교체 반영) | 최신 (2026-04-23) |
| 07 | [track_b/07_not_solved_recovery_strategy.md](track_b/07_not_solved_recovery_strategy.md) | Non-solved 3문제 해결 전략 (Q11, Q36, Q38 ultrathink + Opus overlay) | 완료 (2026-04-22) |
| check | [track_b/check/INDEX.md](track_b/check/INDEX.md) | v8 매핑 정정 + TODO-01~15 검증 산출물 색인 | 최신 (2026-04-22) |
| check | [track_b/check/TODO.md](track_b/check/TODO.md) | TODO-01~15 진행 현황 / 완료 상세 | 최신 (2026-04-22) |

### Opus Reference Pipeline (2026-04-23 신규)

`agent/track_b/opus_reference/` — Track B 50문제에 대한 Opus 독립 검증 파이프라인.

| 파일 | 설명 |
|---|---|
| [opus_reference/GROUND_TRUTH.json](../agent/track_b/opus_reference/GROUND_TRUTH.json) | 50 entries 통합 ground-truth (qid, type, opus_answer, baseline_answer, confidence, notes) |
| [opus_reference/PILOT_REPORT.md](../agent/track_b/opus_reference/PILOT_REPORT.md) | 파일럿 3개(Q01/Q11/Q17) 결과 |
| [opus_reference/VERDICT_50.md](../agent/track_b/opus_reference/VERDICT_50.md) | 50 전체 verdict 요약표 |
| [opus_reference/DEEP_VERIFICATION_NOTES.md](../agent/track_b/opus_reference/DEEP_VERIFICATION_NOTES.md) | 2차/3차 raw routing 검증 상세 (Q25/Q28 돌파구 포함) |
| prepare_context.py | 50개 context 추출기 (Legacy + PJ zone) |
| verify_pj.py | PJ zone 자동 검증 스크립트 (LLDP/IP-peer/routing diff 3중) |
| build_ground_truth.py | VERDICT dict → JSON regenerate |

최종 확신도 분포: **HIGH 23 · MEDIUM-HIGH 27 · MEDIUM/LOW 0**.
Opus vs baseline 불일치 2건 (Q25 Alpha-Center-02 static route error, Q28 Gamma-Axis-02 routing loop) 은 Zindi 018 제출에서 정답 입증.

---

## 빠른 요약

- **URL**: https://zindi.africa/competitions/telco-troubleshooting-agentic-challenge
- **상금**: EUR 40,000 (트랙별 1등 EUR 12,500)
- **Phase 1 마감**: 2026/05/04
- **공통 모델**: Qwen3.5-35B-A3B (OpenRouter 경유 권장)
- **참가 트랙**: **Track A + Track B 모두 진행**

---

## 진행 현황

### Track B (IP Networks)

- [x] 챌린지 조사 및 문서화
- [x] 데이터 다운로드 (HuggingFace)
- [x] Agent Tool Server 로컬 배포 (`localhost:7860`)
- [x] Track B 에이전트 v1 → v6 개발 (`agent/track_b/agent.py`)
- [x] 네트워크 토폴로지 문서화 (D2/SVG, Traditional + PJ)
- [x] 50문제 상세 분석 문서 작성 (03-3-1)
- [x] **v6_full 50문제 실행 완료** (50/50, solved 47 / forced 1 / timeout 2)
- [x] **Non-solved 3문제 보강**: Q11 SOLVED, Q36 타당한 forced, Q38 Opus overlay
- [x] **Qwen P0/P1/P2 개선안 구현** (topology snapshot, resolve_ip_to_device tool, few-shot, answer validation)
- [x] **submission_v6_full_v8.csv** (Qwen + Opus overlay) — Zindi 제출 완료
- [x] **v8 매핑 감사 / 50문제 → 03-3 재매핑** (commit `3487a3d`)
- [x] **PJ Topology Q29~Q33 sample 검증** + alias 원인 분석 (TODO-01~04)
- [x] **Topology hint 에 whitelist + ALIAS WARNING + LINE COUNT GUARD 주입** (TODO-03/05)
- [x] **submission_v6_full_v9.csv** (Q29 수동 + Q31/Q32/Q33 재실행 정답) — Zindi 제출 후보
- [x] **forced_answer 분기 validation + XML fallback + HIGH-ALIAS prompt** (TODO-11/12/13)
- [x] **count_up_physical_ports (10G) suffix 버그 수정** + PJlAN-01/BorderLeaf2 alias 확증 (TODO-08/09)
- [x] **submission_v6_full_v10.csv** (Q29 자동 정답 도출) — 최종 제출 후보 (v9 와 byte-identical)
- [x] **HIGH-ALIAS prompt RULE 1~4 명문화** (Q31/Q32 회귀 원인 해소 패치, TODO-15)
- [x] **v11 Fault reason matrix** + `validate_fault_answer` — 1차 제출 Zindi **0.20** (2026-04-23)
- [x] **v12 Deterministic Hybrid** (2026-04-23) — cli_parsers / topology_parser / fault_analyzer / path_tracer 4종 신규 모듈
  - v12_topo.csv → **Zindi 0.24** (+0.04, Topology 환각 제거)
  - v12_det_full.csv → 0.12 (BFS Path 역효과, 롤백)
  - v12_topo_fault.csv → **Zindi 0.36** (+0.16, Path=v11 유지)
  - **v12_topofault_rt.csv** (serial 016) → **Zindi 0.44** (+0.08, Path routing-table trace, Traditional 10/10 완전 정복)
- [x] **Opus GROUND_TRUTH 파이프라인 (2026-04-23 저녁)** — Track B 50문 독립 검증
  - 파일럿 3 (Q01/Q11/Q17) → 확장 12 (Q07-17) → 전체 50 → PJ zone 3차 심층
  - 최종 분포: HIGH 23 · MEDIUM-HIGH 27 · MEDIUM/LOW 0
  - Q25 baseline `Beta-Node-01;...` 오답 발견 → `Alpha-Center-02;192.168.70.70;static route error`
  - Q28 baseline `Beta-Node-01;...` 오답 발견 → `Gamma-Axis-02;192.168.70.93;routing loop`
- [x] **submission 017 INVALID** — literal `\n` → 실제 개행 변환 시도 (Zindi 공식 포맷 위반, 제출 금지 표기)
- [x] **submission 018 = Zindi 0.48** (+0.04 정확 적중) — base=016, Q25/Q28 Opus 교체 2건만. GROUND_TRUTH 기반
- [ ] **Day 2 (2026-04-24)**: MEDIUM-HIGH 27건 중 PJ FAULT 재검토 (EVPN parser 추가) + 대안 가설 실험 → 목표 0.55+
- [ ] Phase 2 대비 에이전트 최적화

### Track A (Wireless 5G Optimization) — **Phase 1 submission v2_sc 제출 완료 · Zindi 0.3174 (2026-04-23)**

- [x] Challenge README 및 main.py/server.py 구조 파악
- [x] train 2000 + test 500 scenario 스키마 확인 (inline data; test answer 는 `"To be determined"` placeholder)
- [x] **Stage A — Opus 수작업 풀이 (train 10 + traces 2)** → 9/10 정답, P1~P7 패턴 라이브러리 도출 (`.moai/plans/track-a-opus-solutions.md`)
- [x] **Stage B — `agent/track_a/` 디렉토리 구축** (`agent.py`, `prompts.py`, `rag.py`, `generate_submission.py`, `eval_local.py`, `tools/scenario_summary.py`)
- [x] **RAG 도입 (v3)**: train 2000 precompute 14-dim feature cache → L2 retrieval top-3 → dynamic few-shot
- [x] **Stage C — Qwen 500/500 실행 (v1 제출)** → **Zindi 0.149** (P7 fallback 68.6%, multi 예측 3/500)
- [x] **Stage D — v2 공격적 개선 (2026-04-23)**
  - [x] P0: XML 복구 (find_last_valid_boxed_answer) + multi retry + P7 억제 forced (allow_p7=False)
  - [x] P1: XML retry budget 분리 / max_iter 25 / multi tag preamble / `--rerun-fallback` CLI
  - [x] P2: RAG 14→22 dim 확장 + feature_hint + self-consistency (fallback 43건, n=3)
  - [x] Train eval 50 v4 검증: **IoU 0.3173** (v1 baseline 0.160 대비 +98%, G3 gate 0.28 초과)
  - [x] Test 500 batch v2 실행 (병렬 2분할 serial): fallback 43/500 (8.6%), multi 62/500
  - [x] SC overlay on fallback 43 → `submission_v2_sc.csv` 생성 (multi 67/500 실제와 정확 일치, fallback 0)
- [x] **Zindi public leaderboard 확인: 0.3174 (+113% vs v1)**
  - 로컬 train IoU 0.3173 ≈ Zindi 0.3174 → 검증 방법론 거의 완벽 일치
  - 공격적 목표 0.30 초과 달성
- [ ] (선택) 추가 실험: RAG 30 dim 확장 / ensemble / LoRA fine-tuning (Phase 3)

---

## 최신 실행 환경

| 항목 | 값 |
|------|-----|
| Provider | OpenRouter |
| Model | `qwen/qwen3.5-35b-a3b` |
| MAX_TOKENS | 8192 (Qwen3 reasoning 대응) |
| MAX_ITERATIONS | 30 (Track B) / **25 (Track A v4)** — XML retry budget 별도 5회 |
| Track A 서버 | `localhost:7861` (test) + `localhost:7862` (train, DATA_SPLIT=train) |
| Track A 출력 | `agent/track_a/results_batch_v2_{a,b}/`, `results_batch_v2_{a,b}_sc/`, `results_train_eval_50_v4/` |
| Track B 서버 | `localhost:7860` |
| Track B 출력 | `agent/track_b/results_v6_full/`, `results_v9_test/`, `results_v10_test/` |
| Track B 최고점 제출본 | `agent/track_b/submission/submission_018_20260423_ground_truth.csv` (**Zindi 0.48**, serial 018, 2026-04-23 저녁) |
| Track B 이전 baseline | `agent/track_b/submission/submission_v12_topofault_rt.csv` (serial 016, Zindi 0.44) |
| Track B v11 baseline | `agent/track_b/submission/submission_v6_full_v11.csv` (Zindi 0.20) |
| Track B submission 인덱스 | [`agent/track_b/submission/SUBMISSIONS.md`](../agent/track_b/submission/SUBMISSIONS.md) — serial 명명 규칙 + 진실의 원천 |
| Track B Day 2 전략 | [`.moai/plans/track-b-day2-strategy.md`](../.moai/plans/track-b-day2-strategy.md) — 10회 제출 계획 |
| **Track A 최종 제출본** | **`agent/track_a/submission/submission_v2_sc.csv`** (P0+P1+P2 + SC, 500 scenarios, **Zindi 0.3174**) |
| Track A v1 제출본 (참조) | `agent/track_a/submission/submission_v1.csv` (Zindi 0.149) |
| 통합 submission | `agent/common/submission/submission_combined.csv` (550 rows, Track A v2_sc + Track B 018, Zindi 제출 대상) |

## Zindi 제출 현황 (Track B)

| 날짜 | Serial | 제출 | 점수 | 누적 개선 |
|---|---|---|---|---|
| 2026-04-22 | — | v6_full_v8 (초기) | 0.18 | — |
| 2026-04-23 09:25 | — | v6_full_v11 (Fault reason matrix) | **0.20** | +0.02 |
| 2026-04-23 14:00 | 012 | v12_topo (Topology deterministic) | **0.24** | +0.04 |
| 2026-04-23 14:30 | 013 | v12_det_full (BFS Path 역효과) | 0.12 | -0.12 |
| 2026-04-23 15:00 | 015 | v12_topo_fault (Path=v11 복원) | **0.36** | +0.16 |
| 2026-04-23 15:30 | 016 | **v12_topofault_rt (routing-trace)** | **0.44** | +0.08 |
| 2026-04-23 17:00 | — | Q42 MAC fix 시도 | 0.44 | 0 |
| 2026-04-23 저녁 | **018** | **ground_truth (Opus Q25/Q28 교체)** | **0.48** | +0.04 |
| **일일 누적** | — | 7-8회 제출 / 10회 제한 | — | **+140% total** |

핵심 돌파: Opus 3차 raw routing 검증이 baseline 의 장비 이름 오답 2건(Q25/Q28)을 찾아내 정답 교체 → Zindi 정답 입증.

다음 Action (2026-04-24): MEDIUM-HIGH 27건 중 PJ FAULT 재검토 (EVPN/VXLAN parser 추가) + 대안 가설 실험. 상세 [`.moai/plans/track-b-day2-strategy.md`](../.moai/plans/track-b-day2-strategy.md).

## Zindi 제출 현황 (Track A)

| 날짜 | 제출 | 점수 | 개선 | 비고 |
|---|---|---|---|---|
| 2026-04-23 (초기) | `submission_v1.csv` (RAG v3 14-dim) | 0.149 | baseline | fallback 343/500 (68.6%), multi 3/500 |
| 2026-04-23 (Stage D) | `submission_v2_sc.csv` (P0+P1+P2 + SC) | **0.3174** | **+113%** | fallback 0, multi 67/500 (실제와 정확 일치) |

핵심 개선 전략: Track B 의 XML recovery + forced validation 패턴을 Track A 로 이식 + RAG 14→22 dim 확장 + self-consistency overlay.
로컬 train eval IoU (0.3173) ≈ Zindi public (0.3174) → 검증 방법론 신뢰성 확보 (차이 0.0001).

개선 계획 상세: [`.moai/plans/track-a-0-149-track-shimmying-pascal.md`](../.moai/plans/track-a-0-149-track-shimmying-pascal.md)
