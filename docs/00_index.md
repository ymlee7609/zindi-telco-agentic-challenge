# Zindi Telco Agentic Challenge — 문서 인덱스

> 최종 업데이트: 2026-04-22
> 문서 구조: **공통 / Track A / Track B** 3영역 분리

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
| 06 | [track_b/06_progress_report.md](track_b/06_progress_report.md) | Track B 진행 경과 리포트 | 최신 (2026-04-22) |
| 07 | [track_b/07_not_solved_recovery_strategy.md](track_b/07_not_solved_recovery_strategy.md) | Non-solved 3문제 해결 전략 (Q11, Q36, Q38 ultrathink + Opus overlay) | 완료 (2026-04-22) |

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
- [ ] Phase 2 대비 에이전트 최적화

### Track A (Wireless 5G Optimization) — **진행 중**

- [x] Challenge README 및 main.py/server.py 구조 파악
- [x] train 2000 + test 500 scenario 스키마 확인 (inline data, answer 포함)
- [x] **Stage A — Opus 수작업 풀이 (train 10 + traces 2)** → 9/10 정답, P1~P7 패턴 라이브러리 도출
- [x] **Stage B — `agent/track_a/` 디렉토리 구축** (agent.py, prompts.py)
- [ ] Stage B — generate_submission.py, eval_local.py
- [ ] Stage C — Smoke 10 / Pilot 50 / Batch 250 × 2
- [ ] Submission v1 (Qwen 단독) + v2 (Opus overlay)

---

## 최신 실행 환경

| 항목 | 값 |
|------|-----|
| Provider | OpenRouter |
| Model | `qwen/qwen3.5-35b-a3b` |
| MAX_TOKENS | 8192 (Qwen3 reasoning 대응) |
| MAX_ITERATIONS | 30 (Track B) / 20 (Track A) |
| Track A 출력 | `agent/track_a/results_*` |
| Track B 출력 | `agent/track_b/results_v6_full/` |
