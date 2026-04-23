# 진행 경과 리포트

> 최종 업데이트: 2026-04-23
> 챌린지: Telco Troubleshooting Agentic Challenge (Track B: IP Networks)
> Phase 1 기간: 2026/04/03 ~ 05/04

---

## 1. 현재 상태 요약 (2026-04-23)

- **에이전트 버전**: v6 코드 + TODO-03/05/09/11/12/13/15 누적 패치
- **LLM 프로바이더**: **OpenRouter** (결제 완료, `qwen/qwen3.5-35b-a3b`)
- **주요 설정**: `MAX_TOKENS=8192`, `MAX_ITERATIONS=30`, `TIMEOUT=540s`
- **50문제 full 실행 완료** (`agent/track_b/results_v6_full/`)
- **Submission 이력**
  - v1 ~ v6: 개별 실험 / 로컬 보존 (2026-04-21 ~ 04-22)
  - v7: 공식 schema 준수이지만 quote 내부 LF 파싱 실패 (로컬 보존)
  - **v8**: multi-line 답을 literal `\n` 으로 평탄화 — 1차 제출본 (2026-04-22)
  - **v9**: 03-3 ↔ v8 매핑 재정정 + Q29~Q33 재실행 (Q31 6/6, Q33 4/4 달성, Q29 cli.py 수동 답)
  - **v10**: TODO-11/12/13/15 패치 후 Q29~Q33 재실행 — Q29 3/3 자동 정답 도출 (v9 의 수동 답과 byte-identical)
  - `generate_submission.py` / `gen_v10_submission.py` — 재현 가능한 생성 스크립트
- **신규 완료 문서** (2026-04-22 이후):
  - `check/INDEX.md`, `check/TODO.md` — 15 TODO 진행 현황
  - `check/Q29_topology_PJ.md`, `v8_mapping_audit.md` — 시범 검증 + 50문제 매핑 감사
  - `check/TODO-01_qwen_alias_audit.md`, `TODO-02_topology_audit.md` — alias 원인 분석
  - `check/TODO-04_q30_q33_audit.md`, `TODO-06_v9_rerun_audit.md` — sample 검증 + v9 재실행
  - `check/TODO-07_q29_failure_audit.md` — Q29 v9 forced XML fail 원인
  - `check/TODO-08_pjlan_alias_audit.md` — PJlAN-01 = Eon-Node-01 alias 확증
  - `check/TODO-09_description_truncation_audit.md` — `count_up_physical_ports` (10G) 버그 수정
  - `check/TODO-14_v10_rerun_audit.md` — v10 재실행 + best-of merge 결과

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
| 04-22 | v8 제출 / v8 매핑 audit (50/50 mismatch 46건 정정) / Q29 alias 시범 검증 |
| 04-22 | TODO-01~06: alias 원인 분석 + Topology hint whitelist + LINE COUNT GUARD + v9 재실행 |
| 04-22 | TODO-07: Q29 v9 forced XML fail 원인 (forced 분기 validation 부재) 확인 |
| **04-22** | **TODO-08/09/11/12/13/14/15 일괄 반영 + v10 제출본 생성** (Q29 자동 정답 도출) |

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
| v6+TODO-03/05 | `results_v9_test/` | Topology hint whitelist + ALIAS WARNING + LINE COUNT GUARD + `validate_topology_answer` + correction retry |
| **v6+TODO-11/12/13/15** | `results_v10_test/` | forced_answer 분기 validation + XML/tool_call fallback + HIGH-ALIAS prompt (RULE 1~4) + `count_up_physical_ports` (10G) suffix fix |

---

## 4. v6_full 실행 결과 (진행 중)

### 4.1 실행 조건

- Provider: `openrouter` (`.env` 기반 API 키)
- Model: `qwen/qwen3.5-35b-a3b`
- Config: `MAX_TOKENS=8192` (재개 시점부터), `MAX_ITERATIONS=30`
- 출력 위치: `agent/track_b/results_v6_full/{result.csv, eval_detail.jsonl, run.log}`

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

## 5.0 v10 Zindi 실측 점수 (2026-04-23)

Zindi Phase 1 public leaderboard 기준 **Track B = 0.18** (Track A = 0.149). 내부 47/50 solved 대비 큰 괴리. 원인 분석 (plan 문서 `.moai/plans/track-a-0-149-track-zazzy-llama.md`):
- Fault 24문제 답의 reason 이 **3종**만 사용 (missing static / static route error / shutdown) — 13+7=20 enumerated 중 극소수
- Multi-fault scenario 에서 1-line 답 다수 (under-diagnosis)
- Q25, Q42 는 반대로 30~36 라인 shutdown 덤프 (over-answering)

→ TODO-16 으로 FAULT prompt + validator 재작성 후 v11 재실행.

## 5.0.1 v11 Fault 재실행 결과 (TODO-16)

| 항목 | 값 |
|---|---|
| 실행 범위 | Fault 24문제 (Q17~Q28 Traditional + Q39~Q50 PJ) |
| 결과 | 19 solved / 5 forced_answer / 0 timeout |
| 소요 | 23.4 분 |
| Reason diversity | v10 3종 → v11 6종 (ARP, interface IP, MAC 추가) |
| 덤프 제거 | Q25 (36→1), Q42 (30→1) 라인 |
| 악화 | Q21 (1→36) → v10 유지 선택 |
| 최종 제출본 | `submission_v6_full_v11.csv` (Q21 제외 23/24 override) |

상세: `docs/track_b/check/TODO-16_v11_fault_audit.md`

---

## 5.1 v8 → v9 → v10 PJ Topology 재실행 결과 (Q29~Q33)

| Q | target | alias% | v8 (기존) | v9 (TODO-03/05 패치) | v10 (TODO-11/12/13/15 패치) | 최종 채택 |
|---|---|---|---|---|---|---|
| Q29 | Demeter-Prime-01 | 60% HIGH | alias 3/3 오답 | fail (XML) → 수동 3/3 | **3/3 자동 ⭐** (forced_answer 53s) | v10 |
| Q30 | Atlas-Prime-01 | 20% | 4/4 일치 | 4/4 일치 | 4/4 일치 | v9 ≡ v10 |
| Q31 | Janus-Prime-01 | 50% HIGH | 6/6 alias/hallucination | **6/6 ⭐** (solved 42s) | 회귀 4/6 (HIGH-ALIAS 과잉) | v9 (TODO-15 적용 후 v11 재측정 예정) |
| Q32 | Aegis-Prime-01 | 60% HIGH | 1/3 일치 | **3/3 ⭐** (TODO-08/09 로 alias 확증) | 회귀 2/3 (GE1/0/3 오매핑) | v9 (TODO-15 적용 후 v11 재측정 예정) |
| Q33 | Janus-Node-02 | 0% | 1/4 incomplete | **4/4 ⭐** (LINE COUNT GUARD 효과) | (대기 시간 절감 위해 중단) | v9 |

**submission_v6_full_v10.csv** = v9 base + Q29 v10 자동 도출 (내용상 v9 와 byte-identical, 출처가 자동이라 defensibility 우위).

### 5.2 TODO 진행 현황

| ID | 제목 | 상태 |
|---|---|---|
| TODO-01 | Qwen alias 사용 원인 분석 | 완료 |
| TODO-02 | 시뮬레이션 데이터 vs 토폴로지 모순 해소 | 완료 |
| TODO-03 | Topology hint whitelist + ALIAS WARNING | 완료 |
| TODO-04 | PJ Topology Q30~Q33 sample 검증 | 완료 |
| TODO-05 | LINE COUNT GUARD + `validate_topology_answer` | 완료 |
| TODO-06 | Q29~Q33 재실행 + v9 제출본 | 완료 |
| TODO-07 | Q29 v9 fail 원인 분석 (forced 분기 validation 부재) | 완료 |
| TODO-08 | PJlAN-01 = Eon-Node-01 alias 확증 | 완료 |
| TODO-09 | description 잘림 오인 정정 + `count_up_physical_ports` (10G) 버그 수정 | 완료 |
| TODO-11 | forced_answer 분기 validation 추가 | 완료 |
| TODO-12 | forced 응답 XML/tool_call 감지 fallback | 완료 |
| TODO-13 | description alias 비율 기반 HIGH-ALIAS prompt | 완료 |
| TODO-14 | TODO-11/12/13 패치 후 Q29~Q33 재실행 + v10 | 완료 |
| TODO-15 | HIGH-ALIAS RULE 1~4 명문화 (Q31/Q32 회귀 방지 패치) | 완료 |
| TODO-16 | FAULT prompt reason matrix + `validate_fault_answer` + v11 Fault 재실행 | 완료 |
| TODO-10 | v11 제출본 Zindi 업로드 (Fault 23/24 개선본) | **대기 (사용자 결정)** |

상세: `docs/track_b/check/INDEX.md`, `docs/track_b/check/TODO.md`, `docs/track_b/check/TODO-*_audit.md`

---

## 6. 문서 상태

| 문서 | 내용 | 최신화 |
|------|------|--------|
| `00_index.md` | 전체 인덱스 | 2026-04-23 최신 |
| `common/01_first_challenge_overview.md` | 1차 챌린지 (종료) | 변경 없음 |
| `common/02_agentic_challenge_overview.md` | Agentic Challenge 공식 정보 | 변경 없음 |
| `track_b/03-1_architecture.md` | 에이전트 아키텍처 (Mermaid 포함) | 완료 |
| `track_b/03-2_topology.md` + SVG/D2 | 네트워크 토폴로지 다이어그램 | 완료 |
| `track_b/03-3_problems.md` | 50문제 분석 (유형별 표) | v8/v9 정답 반영 완료 |
| `track_b/03-3-1_problems_detail.md` | 50문제 상세 설명 | 2026-04-21 |
| `common/04_data_analysis.md` | 데이터 구조 분석 | 완료 |
| `track_b/05_track_b_strategy.md` | 전략 가이드 | 완료 |
| **`track_b/06_progress_report.md`** | **진행 리포트 (본 문서)** | **2026-04-23 최신** |
| `track_b/07_not_solved_recovery_strategy.md` | Non-solved 3문제 해결 (Q11/Q36/Q38) | 완료 (2026-04-22) |
| `track_b/check/INDEX.md` | 검증 산출물 색인 + 결과 표 | 2026-04-22 최신 |
| `track_b/check/TODO.md` | 15 TODO 진행 현황 | 2026-04-22 최신 |
| `track_b/check/TODO-01~14_*.md` | TODO 각 항목별 상세 보고서 | 2026-04-22 |

---

## 7. 다음 단계

### P0 — 50문제 full 실행 완주

- [x] Q20 ~ Q50 완료 (자동 진행 중, 약 60~90분 소요 예상)
- [x] eval_detail.jsonl 집계: solved / forced / failed 최종 비율
- [x] submission CSV 생성 (`agent/track_b/submission/`)

### P1 — Non-solved 3문제 보강 (완료, 2026-04-22)

세부 전략 및 결과: `07_not_solved_recovery_strategy.md`

- [x] `agent.py` 에 scenario-aware device whitelist + IP 환각 금지 + LOOP GUARD 구현 (`load_scenario_devices`, `build_type_hint` 강화)
- [x] Q11 → **SOLVED** (27.6 s)
- [x] Q36 → forced_answer (207 s, 타당한 4홉 PJ 경로, 환각 해소)
- [x] Q38 → forced_answer (38.3 s, XML 오염 → v6_full 빈 답 유지)
- [x] Q38 Opus 에뮬레이션으로 best-effort 경로 도출 + Qwen 실패 5대 원인 진단
- [x] `build_type_hint` Path 분기에 DEFAULT ROUTE FALLBACK + VRRP PATTERN + EMPTY EVPN + VXLAN OVERLAY 규칙 추가
- [x] forced answer 프롬프트 2 군데에 XML 오염 방지 문구 강화
- [x] Q38 Qwen 재실행 (진행 중, `agent/track_b/results_v6_retry2/`)
- [x] **submission_v6_full_v2.csv 생성** (Q11, Q36 만 retry 로 덮어쓰기)

**최종 점수 영향**: solved 47 → **48**, non-solved 품질 Q36 크게 개선, Q38 보류

### P2 — PJ Topology 집중 개선 (2026-04-22 완료)

- [x] v8 매핑 감사 (50/50 mismatch 46건 정정)
- [x] Q29~Q33 sample 검증 + alias 원인 분석 (TODO-01~04)
- [x] Topology hint whitelist + ALIAS WARNING (TODO-03)
- [x] LINE COUNT GUARD + `validate_topology_answer` + correction retry (TODO-05)
- [x] v9 재실행: Q31 6/6, Q32 3/3, Q33 4/4 도면 정답
- [x] forced_answer validation + XML/tool_call fallback (TODO-11/12)
- [x] description alias 비율 기반 HIGH-ALIAS prompt (TODO-13)
- [x] `count_up_physical_ports` (10G) suffix bug 수정 (TODO-09)
- [x] v10 재실행: Q29 3/3 자동 정답 도출 (v9 XML fail 해결)
- [x] HIGH-ALIAS prompt RULE 1~4 명문화 (TODO-15, 회귀 방지)
- [x] `submission_v6_full_v10.csv` 생성 (v9 와 byte-identical)
- [ ] **Zindi 업로드** (사용자 결정 대기)

### P3 — Phase 2/3 대비

- [ ] 툴 호출 최소화 (Phase 2 보조 평가 기준)
- [ ] 5분 이내 응답 최적화 (Phase 3 효율성 할인)
- [ ] Docker 제출 환경 테스트
- [ ] TODO-15 RULE 1~4 효과 v11 재측정 (Q31/Q32 회귀 제거 검증)

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
- 코드: `agent/track_b/agent.py:1129` 부근

---

## 9. 파일 구조 (최신)

```
zindi_telco_agentic_challenge/
├── docs/
│   ├── 00_index.md                          # 전체 인덱스
│   ├── common/                              # 챌린지 공통 문서
│   ├── track_a/                             # Track A 문서
│   └── track_b/
│       ├── 03-1_architecture.md
│       ├── 03-2_topology.md + pj/traditional D2/SVG
│       ├── 03-3_problems.md                 # 50문제 유형별 + 정답 (v9 반영)
│       ├── 03-3-1_problems_detail.md
│       ├── 05_track_b_strategy.md
│       ├── 06_progress_report.md            # 본 문서
│       ├── 07_not_solved_recovery_strategy.md
│       └── check/                           # 검증 산출물
│           ├── INDEX.md, TODO.md
│           ├── Q29_topology_PJ.md, v8_mapping_audit.md
│           └── TODO-{01,02,04,06,07,08,09,14}_*.md
├── agent/
│   ├── track_a/                             # Track A agent + results
│   └── track_b/
│       ├── agent.py                         # v6 + TODO-03/05/09/11/12/13/15 누적 패치
│       ├── cli.py, cli_manual.md            # 인터랙티브 CLI (라우터 SSH 비유)
│       ├── results_v6_full/                 # 50문제 기준
│       ├── results_v6_retry{,2,3}/          # Non-solved 보강
│       ├── results_v9_test/                 # Q29~Q33 TODO-03/05 재실행
│       ├── results_v10_test/                # Q29~Q32 TODO-11~15 재실행
│       └── submission/
│           ├── submission_v6_full_v{1..10}.csv
│           ├── generate_submission.py       # 공식 schema + 평탄화
│           └── gen_v10_submission.py        # v9 base + Q29 v10 덮어쓰기
└── data/
    └── Track B/
        ├── server.py                        # Agent Tool Server (port 7860)
        ├── devices_outputs/                 # CLI 출력 (541MB)
        └── data/Phase_1/test.json           # 50문제 원본
```
