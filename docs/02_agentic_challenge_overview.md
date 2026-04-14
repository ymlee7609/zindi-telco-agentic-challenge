# Telco Troubleshooting Agentic Challenge

> Zindi 플랫폼: https://zindi.africa/competitions/telco-troubleshooting-agentic-challenge
> 총 상금: EUR 40,000 | 기간: 2026/04/17 ~ 2026/05/18
> 베이스 모델: Qwen3.5-35B-A3B (필수)
> 파트너: GSMA, ETSI, ITU, IEEE GenAINet, TM Forum

## 1. 챌린지 목표

통신 네트워크(무선 + IP) 장애를 진단하고 트러블슈팅하는 **지능형 AI Agent**를 구축한다.
Agentic AI 기법을 활용하여 네트워크 운영/유지보수 업무를 자동화하는 것이 핵심.

### 1차 챌린지 대비 변화

| 구분 | 1차 챌린지 (종료) | Agentic 챌린지 (현재) |
|------|-----------------|---------------------|
| **초점** | LLM 파인튜닝 | AI Agent 시스템 설계 |
| **모델** | Qwen3-32B / 2.5-7B / 2.5-1.5B | **Qwen3.5-35B-A3B** (단일 필수 모델) |
| **트랙** | 3개 (클라우드/미드/엣지) | **2개 (무선/IP 네트워크)** |
| **평가** | Pass@1 정답률 | IoU / Exact Match + **효율성 할인** |
| **상금** | EUR 35,000 | **EUR 40,000** |
| **핵심 기법** | Fine-tuning | Agent, RAG, Tool Use, CoT, Memory |

## 2. 두 개 트랙

### Track A: 무선 네트워크 (Wireless Networks)

- **과제**: Agent Tool Server의 시뮬레이션 인터페이스를 호출하여 장애 진단
- **질문 형식**: 단답형 + 복수 답안 (복수 답은 `|`로 구분, 오름차순 정렬)
- **데이터 규모**:
  - Phase 1: 학습 2,000문제 + 테스트 500문제
  - Phase 2: 새 테스트 500문제
  - Phase 3: 최종 평가 500문제
- **평가 메트릭**: **IoU (Intersection over Union)**
  - `IoU = intersection(answers, ground_truth) / union(answers, ground_truth)`

### Track B: IP 네트워크 (IP Networks)

- **과제**: 멀티벤더 환경(Huawei, Cisco, H3C)에서 개방형 질문 해결
- **질문 형식**: 개방형 (Open-ended)
- **데이터 규모**:
  - Phase 1: 50문제
  - Phase 2: 100문제 (3일마다 20문제씩 배치 공개)
  - Phase 3: 70문제
- **평가 메트릭**: **Exact Match Accuracy** (prediction == ground_truth)
- Phase 2 제출 제한: **최대 3회**

## 3. 상금 구조

각 트랙 동일 배분:

| 순위 | 상금 | 추가 혜택 |
|------|------|----------|
| 1등 | EUR 12,500 | Leader Pass (¥2,995) + 최대 $3,500 항공/숙박 (MWC Shanghai 2026) |
| 2등 | EUR 5,000 | - |
| 3등 | EUR 2,500 | - |
| **총합** | **EUR 40,000** | Zindi Points 10,000 |

- 1인/팀은 **양 트랙 합산 1등 1회만** 가능
- 우승자는 MWC Shanghai 2026 (6/24-26)에서 발표

## 4. 타임라인 (3 Phase)

| Phase | 기간 | 내용 |
|-------|------|------|
| **Phase 1** | 2026/04/03 ~ 05/04 | Agent 설계, 지속적 제출, Public Leaderboard |
| **Phase 2** | 2026/05/04 ~ 05/18 | 새 데이터(동일 분포) 테스트, 트랙별 Top 30 선발, 3회 제출 |
| **Phase 3** | 2026/05/18 ~ 05/29 | 최종 평가 (Top 30만), 효율성 스코어링, 우승자 발표 |

- **제출 시작**: 2026년 4월 17일
- **챌린지 마감**: 2026년 5월 18일
- **Leaderboard**: Public 20-30% / Private 70-80% (종료 시 공개)

## 5. 효율성 할인 (Phase 3)

Phase 3에서는 정확도에 **시간 기반 효율성 할인**이 적용됨:

| 소요 시간 | 점수 배율 |
|-----------|----------|
| < 5분 | 100% |
| 5~10분 | 80% |
| 10~15분 | 60% |
| > 15분 | **0% (실격)** |

-> 정확도뿐 아니라 **응답 속도**가 최종 순위를 결정

## 6. 기술 요구사항

### 필수 베이스 모델
- **Qwen3.5-35B-A3B** (변경 불가)
- 파인튜닝 허용, 파라미터 스케일/아키텍처 변경 금지

### Agent Tool Server
- `server.py`를 통한 시뮬레이션 인터페이스 제공
- 두 가지 접근 방식:
  1. **로컬 서버 배포**: 제공된 코드 + 가이드로 직접 구동
  2. **클라우드 API**: HTTP + Authorization 헤더 (Phase 1: 일 1,000콜 제한, Phase 2: 무제한)

### 핵심 기법
- Agentic AI (자율 에이전트)
- Fine-tuning
- RAG (Retrieval-Augmented Generation)
- Memory Systems
- Skills Design
- Chain-of-Thought (CoT)

### 제약사항
- 오픈소스 언어/도구만 사용 가능
- AutoML 도구 금지
- 유료 서비스/신용카드 체험판 사용 금지
- 노트북 내 커스텀 패키지 금지

## 7. 제출 형식

- **파일**: `result.csv` (답안 포함)
- **제출 선택**: 2개 제출을 Private Leaderboard 평가용으로 선택 (미선택 시 Public 최고 2개 자동 선택)
- **코드 리뷰**: 트랙별 Top 30은 요청 후 48시간 내 코드 제출 필수
- **재현성**: Leaderboard 점수를 정확히 재현해야 함 (랜덤 시드 필수)
- 코드 미제출 시: 6개월 상금 밴 + 2,000 포인트 차감

## 8. 규칙

### 팀 규칙
- 개인 또는 최대 4인 팀
- 다중 계정 금지
- 팀 간 비공개 코드 공유 금지
- 마감 5일 전부터 팀원 추가 불가

### 데이터/저작권
- 라이선스: CC-BY-SA 4.0
- 우승 코드 저작권은 Zindi에 양도

## 9. 참가 현황

- 등록: 399명 (2026/04/14 기준)

## 10. 참고 링크

- **챌린지 페이지**: https://zindi.africa/competitions/telco-troubleshooting-agentic-challenge
- **Global Launch**: https://aiforgood.itu.int/event/telco-troubleshooting-agentic-challenge-global-launch/
- **OTAI 이니셔티브**: https://aiforgood.itu.int/launch-of-the-open-telecom-agent-based-intelligence-initiative/
- **Open Telco AI (GSMA)**: https://www.gsma.com/solutions-and-impact/technologies/artificial-intelligence/open-telco-ai/

## 11. 전략적 고려사항

### CQO 관점에서의 가치
- 무선 + IP 네트워크 장애 진단 자동화는 통신사 품질관리의 핵심
- 멀티벤더(Huawei/Cisco/H3C) 환경은 실제 운영 환경과 동일
- Agentic AI 기반 자율 진단은 MTTR 단축에 직결

### 트랙 선택 고려
- **Track A (무선)**: 데이터 규모 큼 (2,000+), IoU 평가, 시뮬레이션 기반
- **Track B (IP)**: 데이터 규모 작음 (50~100), Exact Match, 멀티벤더, 개방형 질문
- 통신사 NW 운영 경험이 Track B에서 더 직접적인 우위로 작용할 가능성

### 핵심 성공 요인
1. **효율성**: Phase 3에서 15분 초과 시 0점 → 빠른 추론 파이프라인 필수
2. **Tool Use**: Agent Tool Server API를 효과적으로 활용하는 전략
3. **파인튜닝**: Qwen3.5-35B-A3B를 통신 도메인에 특화
4. **RAG/Memory**: 도메인 지식 효과적 활용
5. **재현성**: 시드 관리 및 결정론적 파이프라인 설계
