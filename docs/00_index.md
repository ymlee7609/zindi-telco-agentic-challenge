# Zindi Telco Agentic Challenge - 문서 인덱스

## 문서 목록

| # | 파일 | 설명 | 상태 |
|---|------|------|------|
| 01 | [01_first_challenge_overview.md](01_first_challenge_overview.md) | 1차 AI Telco Troubleshooting Challenge (LLM 파인튜닝) | 종료 |
| 02 | [02_agentic_challenge_overview.md](02_agentic_challenge_overview.md) | Agentic Challenge 공식 정보 (트랙/상금/규칙/타임라인) | 완료 |
| 03 | [03_data_analysis.md](03_data_analysis.md) | Track A/B 데이터 구조 및 상세 분석 | 완료 |
| 04 | [04_track_b_strategy.md](04_track_b_strategy.md) | Track B 문제 유형별 전략 및 실행 계획 | 완료 |
| 05 | [05_progress_report.md](05_progress_report.md) | 진행 경과 리포트 (테스트 결과 포함) | 최신 |

## 빠른 요약

- **URL**: https://zindi.africa/competitions/telco-troubleshooting-agentic-challenge
- **참가 트랙**: Track B (IP Networks, Exact Match)
- **상금**: EUR 40,000 (트랙별 1등 EUR 12,500)
- **모델**: Qwen3.5-35B-A3B (필수)
- **Phase 1 마감**: 2026/05/04

## 진행 현황

- [x] 챌린지 조사 및 문서화
- [x] 데이터 다운로드 (HuggingFace)
- [x] Agent Tool Server 로컬 배포 (port 7860)
- [x] Track B 선택, 에이전트 v2 개발 (`agent/agent.py`)
- [x] Baseline 테스트: Topology 문제 5/6 성공
- [ ] **BLOCKED**: LLM API 크레딧 소진 → 해결 필요
- [ ] Path Query / Fault Localization 테스트
- [ ] 50문제 전체 실행
- [ ] 에이전트 최적화 (정확도 + 효율성)
- [ ] Phase 2 제출
