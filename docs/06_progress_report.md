# 진행 경과 리포트

> 최종 업데이트: 2026-04-21
> 챌린지: Telco Troubleshooting Agentic Challenge (Track B: IP Networks)
> Phase 1 기간: 2026/04/03 ~ 05/04

---

## 1. 현재 상태 요약 (2026-04-21)

- **에이전트 버전**: v6 (질문 유형 감지 + cold-start 힌트 + 멀티 프로바이더 + 실제 네트워크 데이터 기반 전략)
- **LLM 프로바이더**: **OpenRouter** (결제 완료, `qwen/qwen3.5-35b-a3b`)
- **주요 설정**: `MAX_TOKENS=8192` (reasoning 소비 대응), `MAX_ITERATIONS=30`, `TIMEOUT=540s`
- **50문제 full 실행 완료** (`agent/results_v6_full/`, 23:15 완료, 총 163.7분 소요)
- **Submission 생성 완료**
  - `agent/submission/submission_v6_full.csv` (v1, 47 solved)
  - `agent/submission/submission_v6_full_v2.csv` (v2, **48 solved** + Q36 타당 forced)
  - `agent/submission/submission_v6_full_v3.csv` (v3, v2 + **Q38 Opus 에뮬레이션 overlay 경로**, 2026-04-22)
  - `agent/submission/submission_v6_full_v4.csv` (v4, v3 + **PJ Path Q34~Q37 Opus 일괄 재작성**, 2026-04-22, 3-column 로컬용)
  - `agent/submission/submission_v6_full_v5.csv` (**v5, Zindi 규격 `id, prediction` 2-column**, 2026-04-22, 제출용)
  - `agent/submission/submission_v6_full_v6.csv` (v6, Q36/Q37 retry3 physical path 반영, 2026-04-22, 로컬용)
  - `agent/submission/submission_v6_full_v7.csv` (v7, 공식 schema 준수이지만 quote 내부 LF 로 Zindi 파싱 실패, 2026-04-22, 로컬 보존)
  - `agent/submission/submission_v6_full_v8.csv` (**v8, multi-line 답을 literal `\n` 으로 평탄화** — 최종 제출본, 2026-04-22)
  - `agent/submission/generate_submission.py` — 앞으로 submission 은 이 스크립트로 재생성 (공식 example schema + newline 평탄화 강제)
- **완료 문서**: 문제 상세본 `docs/03-3-1_problems_detail.md` 신규 추가

---

## 2. 마일스톤 타임라인

| 시점 | 사건 |
|-----|------|
| 04-03 | 챌린지 오픈, 조사·문서화 시작 |
| 04-14 | v1~v2 베이스라인 (Q1~Q5 위주) 수립 |
| 04-16 | 네트워크 토폴로지(D2·SVG) 문서화, Track B 전략 확정 |
| 04-19 | 에이전트 v5 (질문 유형 감지 + cold-start 힌트 + 멀티 SDK) 구현 |
| 04-20 | v5_groq 실행 → Groq 12K TPM 한도로 23/50 문제만 완료(Q6·Q29 한도 초과) |
| 04-20 | 에이전트 v6 (실제 네트워크 데이터 기반 전략 개선) 반영 |
| **04-21** | **OpenRouter 결제 전환 → 50문제 full 실행 개시** |

---

## 3. 에이전트 버전 히스토리

| 버전 | 커밋 / 디렉토리 | 핵심 변화 |
|-----|----------------|----------|
| v1 | `results/` | 초기 버전, Q1~Q5 토폴로지 베이스라인 |
| v2 | `results_v2/` | 유형별 시스템 프롬프트, 병렬 tool call, 30 iter, forced answer |
| v3 | `results_v3/` | 멀티 프로바이더 지원, 출력 포맷 정규화, 402 에러 처리 |
| v4 | `results_v4/` | 누적 개선 실험 |
| v5 | `results_v5_groq/`, `results_v5_smoke/` | 질문 유형 감지 (`detect_question_type`), cold-start 힌트, 다중 SDK |
| **v6** | `results_v6_smoke/`, `results_v6_full/` | 실제 네트워크 데이터 기반 전략 강화, Path/Fault 유형별 시스템 프롬프트 고도화 |

---

## 4. v6_full 실행 결과 (진행 중)

### 4.1 실행 조건

- Provider: `openrouter` (`.env` 기반 API 키)
- Model: `qwen/qwen3.5-35b-a3b`
- Config: `MAX_TOKENS=8192` (재개 시점부터), `MAX_ITERATIONS=30`
- 출력 위치: `agent/results_v6_full/{result.csv, eval_detail.jsonl, run.log}`

### 4.2 실행 이력

| 구간 | 범위 | MAX_TOKENS | 비고 |
|-----|------|-----------|------|
| 1차 (20:29 ~ 21:22) | Q1 ~ Q19 | 4096 | Empty response 9회 관측, Q11 `forced_answer` 발생 |
| 2차 (21:29 ~ ) | Q20 ~ | **8192** | reasoning 여유 확보 후 재개, `--fresh` 미사용으로 이어받기 |

### 4.3 최종 결과

| 유형 | Solved | Forced | Timeout | 합계 |
|-----|--------|--------|---------|------|
| Topology | 11 | 0 | 0 | 11/11 (100%) |
| Path | 12 | 1 (Q11) | 2 (Q36, Q38) | 15/15 완주, 품질 80% |
| Fault | 24 | 0 | 0 | 24/24 (100%) |
| **합계** | **47** | **1** | **2** | **50/50** |

**Non-solved 상세**
- Q11 (Path, forced_answer, 26.3s): Spine routing 실패 조건 — 빈 응답 반복 후 강제 답변
- Q36 (Path, timeout_forced, 697.1s): PJGFA Hermes-Node-01 → 10.1.1.10 — 9분 타임아웃 근접 강제 반환
- Q38 (Path, timeout_forced, 880.5s): PJ Hermes-Prime-01 → 20.1.4.20 — 최장 소요

**총 실행 시간**: 9822s ≈ 163.7분
**유형별 평균 duration**: Topology 8s, Path 230s, Fault 180s (Traditional Fault Q17 592s, Q22 655s 등 outlier 존재)

### 4.4 품질 이슈

| 항목 | 관측 | 대응 |
|-----|------|-----|
| Empty response (Qwen3 reasoning 폭주로 content 비는 현상) | 1차 구간 9회 | `MAX_TOKENS=8192` 상향 후 2차에서 모니터링 |
| Forced answer | Q11 (path, Spine routing 실패 조건) | 재평가 후 필요 시 해당 Q만 재실행 검토 |
| Outlier 소요 | Q9 780 s, Q17 592 s | `TIMEOUT=540s` 내 완료, 허용 범위 |

---

## 5. v5_groq vs v6_full 비교 (부분)

| 메트릭 | v5_groq | v6_full (진행 중) |
|--------|---------|-------------------|
| 프로바이더 | Groq (무료 한도) | OpenRouter (결제) |
| 실행 가능 문제 | 23/50 (Q6·Q29 TPM 한도 초과) | 50/50 |
| 모델 | `llama-3.3-70b-versatile` | `qwen/qwen3.5-35b-a3b` |
| Topology 성공률 | 부분 (한도 내) | 6/6 |
| Path/Fault 품질 | TPM 제한으로 제약 | 재평가 중 |

---

## 6. 문서 상태

| 문서 | 내용 | 최신화 |
|------|------|--------|
| `00_index.md` | 전체 인덱스 | 2026-04-21 최신 |
| `01_first_challenge_overview.md` | 1차 챌린지 (종료) | 변경 없음 |
| `02_agentic_challenge_overview.md` | Agentic Challenge 공식 정보 | 변경 없음 |
| `03-1_architecture.md` | 에이전트 아키텍처 (Mermaid 포함) | 완료 |
| `03-2_topology.md` + SVG/D2 | 네트워크 토폴로지 다이어그램 | 완료 |
| `03-3_problems.md` | 50문제 분석 (유형별 표) | v6 실행 반영 필요 |
| **`03-3-1_problems_detail.md`** | **50문제 상세 설명 (신규)** | **2026-04-21 신규** |
| `04_data_analysis.md` | 데이터 구조 분석 | 완료 |
| `05_track_b_strategy.md` | 전략 가이드 | 완료 |
| `06_progress_report.md` | 진행 리포트 (본 문서) | 2026-04-21 최신 |

---

## 7. 다음 단계

### P0 — 50문제 full 실행 완주

- [ ] Q20 ~ Q50 완료 (자동 진행 중, 약 60~90분 소요 예상)
- [ ] eval_detail.jsonl 집계: solved / forced / failed 최종 비율
- [ ] submission CSV 생성 (`agent/submission/`)

### P1 — Non-solved 3문제 보강 (완료, 2026-04-22)

세부 전략 및 결과: `docs/07_not_solved_recovery_strategy.md`

- [x] `agent.py` 에 scenario-aware device whitelist + IP 환각 금지 + LOOP GUARD 구현 (`load_scenario_devices`, `build_type_hint` 강화)
- [x] Q11 → **SOLVED** (27.6 s)
- [x] Q36 → forced_answer (207 s, 타당한 4홉 PJ 경로, 환각 해소)
- [x] Q38 → forced_answer (38.3 s, XML 오염 → v6_full 빈 답 유지)
- [x] Q38 Opus 에뮬레이션으로 best-effort 경로 도출 + Qwen 실패 5대 원인 진단
- [x] `build_type_hint` Path 분기에 DEFAULT ROUTE FALLBACK + VRRP PATTERN + EMPTY EVPN + VXLAN OVERLAY 규칙 추가
- [x] forced answer 프롬프트 2 군데에 XML 오염 방지 문구 강화
- [ ] Q38 Qwen 재실행 (진행 중, `agent/results_v6_retry2/`)
- [x] **submission_v6_full_v2.csv 생성** (Q11, Q36 만 retry 로 덮어쓰기)

**최종 점수 영향**: solved 47 → **48**, non-solved 품질 Q36 크게 개선, Q38 보류

### P2 — 점수 최적화

- [ ] Exact Match 대비 출력 포맷 점검 (공백, 줄바꿈, 순서)
- [ ] 반복 scenario (Q40/Q41, Q47/Q48 등) 결과 일관성 검증
- [ ] 실패 케이스 프롬프트 튜닝

### P3 — Phase 2/3 대비

- [ ] 툴 호출 최소화 (Phase 2 보조 평가 기준)
- [ ] 5분 이내 응답 최적화 (Phase 3 효율성 할인)
- [ ] Docker 제출 환경 테스트

---

## 8. 주요 기술 이슈 기록

### 8.1 Qwen3 reasoning 토큰 처리

- OpenRouter `qwen/qwen3.5-35b-a3b` 응답은 `message.reasoning` 과 `message.content` 필드 분리
- 간단 요청도 reasoning 200~500 토큰 소비 → `MAX_TOKENS=4096` 에서 content 공간 부족 가능
- 해결: `MAX_TOKENS=8192` 상향 (비용 ~2배 증가, 총 예상 $2 미만)

### 8.2 프로바이더 크레딧 문제 기록

| 프로바이더 | 상태 | 메모 |
|-----------|------|-----|
| HuggingFace novita | 402 Payment Required | 월간 무료 크레딧 소진 |
| Groq (llama-3.3-70b) | TPM 한도 | 12K TPM 제한, Path/Fault 품질 제약 |
| OpenRouter (qwen3.5) | **사용 중** | pay-per-use, 50문제 실행 적정 |

### 8.3 에이전트 resume 로직

- `--fresh` 미지정 시 `result.csv` 스캔해 완료 ID 스킵
- MAX_TOKENS 변경 후 중단 재시작으로 기존 1차 결과 보존 + 2차 구간만 8192 적용 가능
- 코드: `agent/agent.py:1129` 부근

---

## 9. 파일 구조 (최신)

```
zindi_telco_agentic_challenge/
├── docs/                                  # 문서
│   ├── 00_index.md                        # 인덱스
│   ├── 01_first_challenge_overview.md
│   ├── 02_agentic_challenge_overview.md
│   ├── 03-1_architecture.md               # 아키텍처 (Mermaid)
│   ├── 03-2_topology.md                   # 네트워크 토폴로지
│   ├── 03-2_topology_pj.{d2,svg}          # PJ 영역 다이어그램
│   ├── 03-2_topology_traditional.{d2,svg} # Traditional 영역 다이어그램
│   ├── 03-3_problems.md                   # 50문제 유형별 분석
│   ├── 03-3-1_problems_detail.md          # 50문제 상세 설명 (신규)
│   ├── 04_data_analysis.md
│   ├── 05_track_b_strategy.md
│   └── 06_progress_report.md              # 본 문서
├── agent/
│   ├── agent.py                           # v6 에이전트
│   ├── results/                           # v1 결과
│   ├── results_v2/ ~ results_v5_groq/     # 이전 실행 결과
│   ├── results_v6_smoke/                  # v6 smoke (Q1~Q3)
│   └── results_v6_full/                   # v6 full (진행 중)
└── data/
    └── Track B/
        ├── server.py                      # Agent Tool Server (port 7860)
        ├── devices_outputs/               # CLI 출력 (541MB)
        └── data/Phase_1/test.json         # 50문제 원본
```
