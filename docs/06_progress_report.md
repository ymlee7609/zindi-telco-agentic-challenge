# 진행 경과 리포트

> 작성일: 2026-04-14
> 챌린지: Telco Troubleshooting Agentic Challenge (Track B: IP Networks)
> Phase 1 기간: 2026/04/03 ~ 05/04

---

## 1. 완료 작업

### 1.1 챌린지 조사 및 문서화

| 문서 | 내용 | 상태 |
|------|------|------|
| `01_first_challenge_overview.md` | 1차 챌린지 (LLM Fine-tuning, 종료) | 완료 |
| `02_agentic_challenge_overview.md` | Agentic 챌린지 공식 정보 정리 | 완료 |
| `03_data_analysis.md` | Track A/B 데이터 구조 상세 분석 | 완료 |
| `04_track_b_strategy.md` | Track B 전략 및 실행 계획 | 완료 |

### 1.2 데이터 다운로드

- HuggingFace (`netop/Telco-Troubleshooting-Agentic-Challenge`) 전체 다운로드 완료
- 저장 위치: `data/`
- Track B `devices_outputs.zip` 압축 해제 완료 (541MB, 102,886 CLI 출력 파일)

### 1.3 Agent Tool Server 배포

- `data/Track B/server.py` 로컬 배포 완료
- URL: `http://127.0.0.1:7860/api/agent/execute`
- 102,886개 CLI 출력 파일 메모리 로드, 50개 문제 디렉토리
- Huawei/Cisco/H3C 멀티벤더 API 정상 동작 확인

### 1.4 에이전트 개발 (v2)

- 파일: `agent/agent.py`
- 아키텍처: OpenAI SDK + Qwen3.5-35B-A3B (HF Inference/novita)
- 단일 도구: `execute_cli_command(device_name, command)`

---

## 2. Baseline 테스트 결과

### 2.1 v1 (초기 버전) - Q1~Q5

| Q# | 유형 | 상태 | 시간 | Tool Calls | 결과 |
|----|------|------|------|-----------|------|
| Q1 | Topology | solved | 8.3s | 2 | 3 링크 복원 |
| Q2 | Topology (LLDP 불가) | **실패** | 82s | 13 | 빈 응답 반복 |
| Q3 | Topology | solved | 15.3s | 2 | 3 링크 복원 |
| Q4 | Topology | solved | 26.6s | 13 | 7 링크 복원 |
| Q5 | Topology | solved | 7.7s | 2 | 3 링크 복원 |

**v1 성공률: 4/5 (80%)**

### 2.2 v2 (개선 버전) - Q2 재테스트

| Q# | 유형 | 상태 | 시간 | Tool Calls | 결과 |
|----|------|------|------|-----------|------|
| Q2 | Topology (LLDP 불가) | **solved** | 29.5s | 15 | 6 링크 복원 |
| Q7 | Path Query | 크레딧 소진 | - | 6 | 미완료 |
| Q39 | Fault Diagnosis | 크레딧 소진 | - | 2 | 미완료 |

**Q2 개선: 실패 → 29.5초에 해결 (9개 이웃 LLDP 병렬 조회)**

---

## 3. v1 → v2 개선 사항

### 시스템 프롬프트

| 항목 | v1 | v2 |
|------|-----|-----|
| 문제 유형 전략 | 일반적 설명만 | **유형별 구체적 단계** (Topology/Path/Fault) |
| 병렬 조회 | 언급 없음 | **"Batch multiple tool calls in ONE turn"** 강조 |
| 벤더 명령어 | 기본 나열 | **H3C 차이점 명시** (neighbor-information, arp all) |
| 출력 규칙 | 간단한 지시 | **7개 Critical Rules** (효율/중복금지/형식/설명금지/시간/에러/벤더) |

### 에이전트 로직

| 항목 | v1 | v2 |
|------|-----|-----|
| MAX_ITERATIONS | 15 | **30** |
| 빈 응답 처리 | 로그만 | **3회 연속 → 강제 답변 요청** |
| 타임아웃 | 9분 후 단순 메시지 | **9분 후 tools 제외 강제 답변 + 즉시 반환** |
| 결과 truncate | 8,000자 | **12,000자** |
| resume | 기본 | **--fresh 옵션 추가** |
| 결과 통계 | 없음 | **solved/total 요약 출력** |

---

## 4. 50문제 유형 분포

| 유형 | 수량 | 문제 ID | 비고 |
|------|------|---------|------|
| **Topology Reconstruction** | 11 | Q1-Q6, ... | 링크 정보 복원 |
| **Path Query** | 27 | Q7-Q38 | 소스→목적지 경로 추적 |
| **Fault Localization** | 12 | Q39-Q50 | 장애 원인 진단 |

---

## 5. 현재 차단 이슈

### 이슈: HuggingFace Inference 무료 크레딧 소진

- **원인**: novita 프로바이더 월간 무료 크레딧 소진 (402 Payment Required)
- **영향**: Path Query(Q7+), Fault(Q39+) 테스트 불가
- **해결 옵션**:

| 옵션 | 비용 | 장점 | 단점 |
|------|------|------|------|
| **HF PRO 구독** | $9/월 | 20배 크레딧, 즉시 가능 | 월 구독 |
| **OpenRouter API** | pay-per-use | 유연한 과금, 대회 예제도 사용 | API 키 필요, 비용 발생 |
| **로컬 vLLM** | 무료 | 무제한, 최종 배포와 동일 | GPU 필요 (A3B MoE → ~10GB VRAM) |
| **대회 제공 API** | 무료 | 공식 지원 | 일 1,000콜 제한, 레이턴시 |

대회에서 제공하는 클라우드 API도 있음:
- Hong Kong: `124.71.227.61`
- China: `120.46.145.77`
- 단, 이는 Agent Tool Server API이며 LLM API가 아님

---

## 6. 다음 단계 (우선순위)

### P0: API 접근 해결
- [ ] LLM API 접근 방법 확정 (HF PRO / OpenRouter / 로컬 vLLM)
- [ ] agent.py에 선택된 API 반영

### P1: 전 유형 Baseline 확보
- [ ] Path Query 문제 테스트 (Q7~Q38 중 샘플)
- [ ] Fault Localization 문제 테스트 (Q39~Q50 중 샘플)
- [ ] 50문제 전체 실행 → 전체 정확도 측정

### P2: 정확도 향상
- [ ] 실패 패턴 분석 및 프롬프트 최적화
- [ ] 벤더 자동 감지 개선 (Huawei/Cisco/H3C 명령어 매핑)
- [ ] 출력 형식 정규화 (Exact Match 대비)
- [ ] 402/rate limit 에러 조기 종료 로직 추가

### P3: Phase 2/3 대비
- [ ] Qwen3.5-35B-A3B 파인튜닝 검토
- [ ] API 호출 최소화 (Phase 2 보조 평가 기준)
- [ ] 5분 이내 응답 최적화 (Phase 3 효율성 할인)
- [ ] Docker 환경 테스트

---

## 7. 파일 구조

```
zindi_telco_agentic_challenge/
├── docs/                          # 문서
│   ├── 00_index.md               # 인덱스 + TODO
│   ├── 01_first_challenge_overview.md  # 1차 챌린지 (종료)
│   ├── 02_agentic_challenge_overview.md  # Agentic 챌린지 공식 정보
│   ├── 03_data_analysis.md       # 데이터 상세 분석
│   ├── 04_track_b_strategy.md    # Track B 전략
│   └── 05_progress_report.md     # 진행 경과 (본 문서)
├── agent/                         # 에이전트 코드
│   ├── agent.py                  # Track B 에이전트 (v2)
│   ├── results/                  # v1 테스트 결과 (Q1-5)
│   └── results_v2/              # v2 테스트 결과 (Q2,7,39)
├── data/                          # HuggingFace 다운로드 데이터
│   ├── Track A/                  # 무선 (미사용)
│   ├── Track B/                  # IP 네트워크
│   │   ├── server.py            # Agent Tool Server
│   │   ├── devices_outputs/     # CLI 출력 (541MB)
│   │   ├── data/Phase_1/        # 문제 데이터
│   │   └── agent/               # OpenClaw 예제
│   └── submission/              # 제출 템플릿
└── CLAUDE.md                     # MoAI 설정
```

---

## 8. 주요 발견 사항

1. **Qwen3.5-35B-A3B의 tool use 능력이 우수함**: 적절한 프롬프트로 멀티벤더 CLI 명령어를 정확하게 생성
2. **병렬 tool call 지원**: 한 턴에 여러 장비를 동시 조회하여 효율성 크게 향상
3. **reasoning_content 포함**: CoT 추론 과정이 별도 필드로 반환되어 디버깅에 유용
4. **Topology 문제에서 높은 성공률**: LLDP 기반 복원은 거의 완벽하게 동작
5. **LLDP 불가 노드 처리**: v2에서 이웃 노드 역방향 조회로 해결
6. **Exact Match 평가**: 출력 형식 (공백, 줄바꿈, 순서)이 매우 중요 → 형식 정규화 필요
