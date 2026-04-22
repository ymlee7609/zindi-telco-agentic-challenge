# [1차] AI Telco Troubleshooting Challenge (종료)

> Zindi 플랫폼 주최, GSMA/ETSI/ITU/IEEE GenAINet/TM Forum 공동 운영
> 상금 총 EUR 35,000 | 마감: 2026년 2월 1일 (종료됨)
> 후속: Telco Troubleshooting **Agentic** Challenge → [02_agentic_challenge_overview.md](02_agentic_challenge_overview.md)

## 1. 챌린지 목표

통신 네트워크 장애 로그(TeleLogs)를 활용하여 LLM을 파인튜닝하고,
**미지의 네트워크 장애를 탐지/설명**하는 Root Cause Analysis(근본 원인 분석) 모델을 개발한다.

핵심 과제:
- 학습 데이터에 없는 새로운 장애 유형에 대한 **일반화(Generalization)**
- 다양한 네트워크 환경에서의 **강건성(Robustness)**
- 엣지 서버에서의 **배포 효율성(Deployment Efficiency)**
- 파인튜닝 후에도 **일반 지식 유지(Knowledge Retention)**

## 2. 3개 트랙

| 트랙 | 베이스 모델 | 배포 환경 | 핵심 평가 관점 |
|------|-----------|----------|--------------|
| **Track 1** | Qwen3-32B | 클라우드 | Reasoning/일반화 |
| **Track 2** | Qwen2.5-7B-Instruct | 미드-클라우드 | 정확도/효율성 |
| **Track 3** | Qwen2.5-1.5B-Instruct | 엣지-클라우드 | 경량화/엣지 배포 |

- 각 트랙별 독립 평가, 1인/팀은 **하나의 트랙에서만 1등** 가능
- 모든 트랙을 하나의 CSV 파일로 제출 (미참여 트랙은 placeholder)

## 3. 상금 구조

| 순위 | 상금 | 추가 혜택 |
|------|------|----------|
| **1등** (트랙별) | EUR 8,500 | MWC Barcelona 리더 패스($2,750 상당) + 항공/숙박 + 발표 기회 |
| **2등** (트랙별) | 미공개 | - |
| **3등** (트랙별) | 미공개 | - |
| **총 상금** | EUR 35,000 | Zindi Points 10,000 |

## 4. 타임라인

| 일정 | 날짜 |
|------|------|
| 시작 | 2025년 11월 28일 |
| Phase 1 질문 | 2025/11/28 ~ 2026/01/17 |
| Phase 2 질문 | 2026/01/19 ~ 2026/02/02 |
| 챌린지 마감 | 2026년 2월 1일 |
| 결과 발표 | 2026년 2월 2일 |
| 시상식 | MWC26 Barcelona (2026년 3월) |

## 5. 데이터: TeleLogs

- **형식**: 네트워크 장비에서 자동 생성된 장애/이벤트 로그
- **내용**: 약 4,000개 다지선다형 네트워크 트러블슈팅 문제
- **평가 데이터 특성**:
  - 학습 데이터와 다른 구조적 분포를 가진 네트워크 장애
  - 파인튜닝 후 일반 지식 유지 여부를 테스트하는 일반 질문 포함
- **라이선스**: CC-BY SA 4.0 (상업/비상업 모두 허용)

## 6. 평가 메트릭

**Pass@1 (Single-attempt accuracy)**

- 문제당 4개 응답 생성
- 각 샘플에 대한 정답 여부를 평균
- 트러블슈팅 능력 + 일반 지식 정확도 모두 평가

**제출 형식:**
- CSV 파일: `ID, Qwen3-32B, Qwen2.5-7B-Instruct, Qwen2.5-1.5B-Instruct`
- Root cause는 `\boxed{}` 표기법 사용
- 제출 제한: 일 10회, 총 300회

## 7. 규칙 및 제약사항

### 참가 규칙
- 개인 또는 최대 4인 팀
- 오픈소스 패키지만 사용 가능
- AutoML 도구 사용 금지
- 코드 공개: 비공개 공유 금지, 토론 게시판에서만 공개 공유 가능
- 다중 계정/팀 간 협업 적발 시 6개월 밴 + 2,000 포인트 차감

### 모델 제약
- **공식 규칙**: "openly available" 사전학습 모델 허용
- **운영진 명확화**: Qwen 계열 모델만 사용 권장
- 다른 LLM으로 reasoning trace 생성 후 Qwen 학습은 **불허**

### Top 10 요구사항
- 48시간 내 모델 + 코드 + 2페이지 보고서 제출 필수
- 보고서 필수 포함 항목: 데이터 프라이버시, 보안 리스크, 접근 제어, 엣지 컴퓨팅 고려사항, 데이터 거버넌스
- 코드 재현성 필수 (시드 포함)

## 8. 기술 인프라

### ScalarLM 프레임워크
- 챌린지용 커스터마이징된 학습 프레임워크
- GitHub 저장소 제공 (학습 레시피 + 코드 템플릿)
- 사용 옵션:
  1. ScalarLM에서 그대로 사용
  2. 학습 레시피만 복사하여 자체 환경에서 사용
  3. ScalarLM + 챌린지 제공 컴퓨팅 리소스 사용

### 컴퓨팅 리소스
- 학생 대상 제한적 컴퓨팅 리소스 지원
- 신청 마감: 2025년 12월 5일

## 9. 파트너 및 스폰서

| 역할 | 조직 |
|------|------|
| **리드 커뮤니티 파트너** | ETSI, GSMA, IEEE GenAINet, ITU, TM Forum |
| **헤드라인 서포터** | Huawei, InterDigital, NextGCloud, RelationalAI, xFlowResearch |
| **기술 자문** | AT&T |
| **벤치마크** | GSMA Open-Telco LLM Benchmarks 커뮤니티 |

## 10. 참가 현황

- 등록: 1,276명
- 활동 참가자: 253명

## 참고 링크

- 챌린지 페이지: https://zindi.africa/competitions/the-ai-telco-troubleshooting-challenge
- AI for Good: https://aiforgood.itu.int/ai-telco-troubleshooting-challenge/
