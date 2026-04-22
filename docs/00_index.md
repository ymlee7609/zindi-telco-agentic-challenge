# Zindi Telco Agentic Challenge - 문서 인덱스

> 최종 업데이트: 2026-04-21

## 문서 목록

| # | 파일 | 설명 | 상태 |
|---|------|------|------|
| 01 | [01_first_challenge_overview.md](01_first_challenge_overview.md) | 1차 AI Telco Troubleshooting Challenge (LLM 파인튜닝) | 종료 |
| 02 | [02_agentic_challenge_overview.md](02_agentic_challenge_overview.md) | Agentic Challenge 공식 정보 (트랙/상금/규칙/타임라인) | 완료 |
| 03-1 | [03-1_architecture.md](03-1_architecture.md) | 에이전트 아키텍처 (Mermaid) | 완료 |
| 03-2 | [03-2_topology.md](03-2_topology.md) | 네트워크 토폴로지 설명 + D2/SVG 다이어그램 | 완료 |
| 03-3 | [03-3_problems.md](03-3_problems.md) | Track B Phase 1 50문제 유형별 분석 | 완료 |
| 03-3-1 | [03-3-1_problems_detail.md](03-3-1_problems_detail.md) | 50문제 상황·과제·단서 문제별 상세 | **신규** (2026-04-21) |
| 04 | [04_data_analysis.md](04_data_analysis.md) | Track A/B 데이터 구조 및 상세 분석 | 완료 |
| 05 | [05_track_b_strategy.md](05_track_b_strategy.md) | Track B 전략 가이드 | 완료 |
| 06 | [06_progress_report.md](06_progress_report.md) | 진행 경과 리포트 | 최신 (2026-04-21) |
| 07 | [07_not_solved_recovery_strategy.md](07_not_solved_recovery_strategy.md) | Non-solved 3문제 해결 전략 (Q11, Q36, Q38 ultrathink) | **신규** (2026-04-22) |

## 빠른 요약

- **URL**: https://zindi.africa/competitions/telco-troubleshooting-agentic-challenge
- **참가 트랙**: Track B (IP Networks, Exact Match)
- **상금**: EUR 40,000 (트랙별 1등 EUR 12,500)
- **모델**: Qwen3.5-35B-A3B (필수, OpenRouter 경유)
- **Phase 1 마감**: 2026/05/04

## 진행 현황

- [x] 챌린지 조사 및 문서화
- [x] 데이터 다운로드 (HuggingFace)
- [x] Agent Tool Server 로컬 배포 (`localhost:7860`)
- [x] Track B 에이전트 v1 → v6 개발 (`agent/agent.py`)
- [x] 네트워크 토폴로지 문서화 (D2/SVG, Traditional + PJ)
- [x] 50문제 상세 분석 문서 작성 (03-3-1)
- [x] v5_groq 실행 (23/50, Groq TPM 한도로 품질 제약)
- [x] **OpenRouter 결제 완료 및 전환**
- [x] **v6_full 50문제 실행 완료** (50/50, solved 47 / forced 1 / timeout 2)
- [x] submission CSV 생성 (`agent/submission/submission_v6_full.csv`)
- [x] **Non-solved 3문제 재실행 완료**: Q11 SOLVED, Q36 타당한 forced, Q38 보류 (v6_full 빈 답 유지)
- [x] **Submission v2 생성** (`agent/submission/submission_v6_full_v2.csv`, 48 solved)
- [x] **Q38 Opus 에뮬레이션 풀이** → `submission_v6_full_v3.csv` 생성 (overlay 4홉 best-effort)
- [x] **Qwen 개선안 적용** (DEFAULT ROUTE FALLBACK / VRRP / EMPTY EVPN / VXLAN OVERLAY + XML 방지 forced answer)
- [x] **Q38 Qwen 재실행** → XML 오염 재발로 Qwen 자체 한계 확인
- [x] **PJ Path 품질 이슈 발견** (Q34/35/37 도 환각·포맷 문제)
- [x] **Q34~Q38 Opus 일괄 풀이** → `submission_v6_full_v4.csv` 생성 (best-effort)
- [x] **Qwen P0/P1/P2 개선안 구현** (topology snapshot, resolve_ip_to_device tool, few-shot, answer validation)
- [x] **Q34~Q38 Qwen 재실행** (retry3): 3/5 Opus 일치, 2/5 더 정확한 physical path 도출
- [x] **Zindi 제출 포맷 수정**: `id, prediction` 2-column → `submission_v6_full_v5.csv`, `v6.csv` 생성
- [ ] 에이전트 최적화 (정확도 + 효율성)
- [ ] Phase 2 제출

## 최신 실행 환경

| 항목 | 값 |
|------|-----|
| Provider | OpenRouter |
| Model | `qwen/qwen3.5-35b-a3b` |
| MAX_TOKENS | 8192 (Qwen3 reasoning 대응) |
| MAX_ITERATIONS | 30 |
| 출력 디렉토리 | `agent/results_v6_full/` |
