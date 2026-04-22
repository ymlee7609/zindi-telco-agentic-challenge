# Telco Troubleshooting Agentic Challenge

> [Zindi 대회 페이지](https://zindi.africa/competitions/telco-troubleshooting-agentic-challenge) | **Track A (무선 5G) + Track B (IP 네트워크)** | 총 상금: EUR 40,000

[English](README.md)

## 개요

GSMA, ETSI, ITU, IEEE GenAINet, TM Forum 공동 주최 **Telco Troubleshooting Agentic Challenge** 의 **두 트랙 모두** 참가.

두 트랙 모두 **Qwen3.5-35B-A3B** 를 기반 모델로 사용 (교체 불가). FastAPI 기반 시뮬레이터를 통해 scenario 별 도구를 호출하여 문제 해결. Track A 는 무선 RAN (드라이브 테스트 최적화), Track B 는 IP 네트워크 O&M (토폴로지 / 경로 / 장애).

## Track A vs Track B 비교

| | **Track A — 무선 5G** | **Track B — IP 네트워크** |
|---|---|---|
| **도메인** | 5G 드라이브 테스트 최적화 | 멀티벤더 CLI 기반 IP 네트워크 O&M |
| **데이터 규모** | train 2000 + test 500 scenario | Phase 1 50문제 |
| **입력** | throughput/RSRP/SINR 시계열 + cell config | 장비 CLI 출력 (Huawei/Cisco/H3C) |
| **문제 유형** | C1~C22 중 1개 (single) 또는 2~4개 (multi) 선택 | 자유 텍스트 (Exact Match) |
| **답변 양식** | `\boxed{C9}` 또는 `\boxed{C2\|C8\|C11\|C16}` | `node->node->...` / `node;dest;원인` / 링크 목록 |
| **채점** | IoU × 시간 할인 | Exact Match × 시간 할인 |
| **Tool 서버** | `localhost:7861` (test) + `localhost:7862` (train, 로컬 검증) | `localhost:7860` |
| **Tool 개수** | 27개 (throughput / serving-cell / neighbor / antenna / KPI) | 1개 통합 (`execute_cli_command`) |
| **에이전트** | `agent/track_a/agent.py` | `agent/track_b/agent.py` |
| **제출본** | `submission_v1.csv` (500행, RAG v3) | `submission_v6_full_v10.csv` (50행) |
| **현재 성능** | train 50 IoU 0.220 (baseline 대비 +38%) | 48/50 solved (96%) |

두 트랙의 답변은 **단일 Zindi 제출 파일** `ID, Track A, Track B` 550행 CSV 로 통합 업로드.

## 아키텍처

### Track A (무선)

```
                      ┌──────────────────────────┐
                      │  Track A Tool Server     │
                      │  FastAPI :7861 / :7862   │
                      │  27개 tool (throughput,  │
                      │  RSRP/SINR, cell_info,   │
                      │  neighbor, antenna...)   │
                      └───────────▲──────────────┘
                                  │ HTTP
┌─────────────────────────────────┴────────────────┐
│  Qwen3.5-35B-A3B 에이전트 (RAG 강화)             │
│  - 7-pattern 시스템 프롬프트 (P1~P7)              │
│  - 정적 few-shot × 5 (traces + train 0/1/5)      │
│  - RAG: train 2000 L2 유사도 top-3 동적 주입     │
│  - XML 재질의 + P7 fallback + self-consistency   │
└──────────────────────────────────────────────────┘
```

### Track B (IP 네트워크)

```
                      ┌──────────────────────────┐
                      │  Track B Tool Server     │
                      │  FastAPI :7860           │
                      │  멀티벤더 CLI 시뮬레이터  │
                      │  Huawei/Cisco/H3C        │
                      │  102K+ 출력 파일         │
                      └───────────▲──────────────┘
                                  │ HTTP
┌─────────────────────────────────┴────────────────┐
│  Qwen3.5-35B-A3B 에이전트                       │
│  - 문제 유형 자동 감지 (topology/path/fault)    │
│  - 장비 화이트리스트 + alias guard (PJ area)    │
│  - 턴당 병렬 tool 호출                          │
│  - forced-answer 검증 + 루프 가드                │
└──────────────────────────────────────────────────┘
```

## 주요 특징

### Track A

- **7-Pattern Library** (P1 Late-HO / P2 Ping-pong / P3 Overshoot / P4 Coverage-hole / P5 Server / P6 Excessive-tilt / P7 Insufficient) — Opus 수작업 풀이 (train 10 + traces 2) 로 도출
- **14-dim RAG** over train 2000: TP/SINR/RSRP/PCI변화/A3-offset/max-tilt 특징 → Z-score 정규화 → L2 top-3 검색
- **Dynamic few-shot**: scenario 마다 정적 5개 + RAG 3개 주입
- **Self-consistency** (`--num-attempts N`): multi-trial majority vote (현재는 비활성 — v3 가 baseline)

### Track B

- **문제 유형별 전략**: topology / path / fault 분기로 전용 프롬프트와 힌트
- **장비 whitelist + alias guard**: PJ 영역 노드 환각 방지 (TODO-03/08/09)
- **HIGH-ALIAS RULE 1~4**: forced-answer 검증 + XML fallback + 라인 수 가드 (TODO-11~15)
- **v10 해결**: Q29 자동 도출 + Q31/Q32 회귀 수정

## 빠른 시작

### 1. Tool 서버 기동

```bash
# Track B 서버 (7860)
cd "data/Track B/"
unzip devices_outputs.zip -d devices_outputs/   # 최초 1회
python server.py &

# Track A test 서버 (7861)
cd "data/Track A/"
FASTAPI_PORT=7861 python server.py &

# Track A train 서버 (7862, 로컬 검증 용)
FASTAPI_PORT=7862 DATA_SPLIT=train python server.py &
```

### 2. LLM API 설정

```bash
# 저장소 루트의 .env 파일 (자동 로드)
OPENROUTER_API_KEY="sk-or-v1-..."
# 대안: HF_TOKEN, DASHSCOPE_API_KEY, GROQ_API_KEY, GEMINI_API_KEY
```

### 3. 에이전트 실행

**Track A — 무선 5G** (scenario 당 약 35초):

```bash
# RAG 캐시 사전 계산 (최초 1회, train 2000)
python agent/track_a/rag.py --precompute

# train 50 로컬 검증 (정답 존재)
python agent/track_a/agent.py \
    --server-url http://localhost:7862 \
    --max-samples 50 \
    --save-dir agent/track_a/results_train_eval_50_v3
python agent/track_a/eval_local.py \
    agent/track_a/results_train_eval_50_v3/result.csv --source train

# test 500 전수 실행 (Pilot 50 + Batch A 200 + Batch B 250)
python agent/track_a/agent.py --server-url http://localhost:7861 --max-samples 50   --save-dir agent/track_a/results_pilot_v3
python agent/track_a/agent.py --server-url http://localhost:7861 --start-idx 50  --max-samples 200 --save-dir agent/track_a/results_batch_a
python agent/track_a/agent.py --server-url http://localhost:7861 --start-idx 250 --max-samples 250 --save-dir agent/track_a/results_batch_b
```

**Track B — IP 네트워크** (문제 당 약 180초):

```bash
# 단일 문제 테스트
python agent/track_b/agent.py -i "data/Track B/data/Phase_1/test.json" --questions 1

# 전체 평가 (50문제, 기존 result.csv 이어하기)
python agent/track_b/agent.py -i "data/Track B/data/Phase_1/test.json"

# 처음부터 실행
python agent/track_b/agent.py -i "data/Track B/data/Phase_1/test.json" --fresh
```

### 4. 통합 Submission 생성

```bash
# Track A → common/submission/submission_combined.csv 의 Track A 열 자동 갱신
python agent/track_a/generate_submission.py \
    --results agent/track_a/results_pilot_v3/result.csv \
    --override agent/track_a/results_batch_a/result.csv \
    --override agent/track_a/results_batch_b/result.csv \
    --out agent/track_a/submission/submission_v1.csv

# Track B → 같은 combined 파일의 Track B 열 자동 갱신
python agent/track_b/submission/generate_submission.py \
    --results agent/track_b/results_v6_full/result.csv \
    --override agent/track_b/results_v9_test/result.csv \
    --override agent/track_b/results_v10_test/result.csv \
    --out agent/track_b/submission/submission_v6_full_v10.csv

# 확인
python agent/common/submission/merge_submission.py --status
# → Combined: Track A 500/550, Track B 50/550
```

Zindi 에 `agent/common/submission/submission_combined.csv` 업로드.

## 프로젝트 구조

```
├── agent/
│   ├── common/
│   │   ├── submission_example.csv        # Zindi 공식 550행 템플릿
│   │   └── submission/
│   │       ├── merge_submission.py       # Track A/B merge 헬퍼
│   │       └── submission_combined.csv   # 최종 업로드 파일
│   ├── track_a/                          # 무선 5G 에이전트
│   │   ├── agent.py                      # Qwen runner (RAG + 재질의 + fallback)
│   │   ├── prompts.py                    # 시스템 프롬프트 + 정적 few-shot 5개
│   │   ├── rag.py                        # 14-dim 특징 + train 2000 검색
│   │   ├── generate_submission.py        # Track A 열 채움 (combined 자동 갱신)
│   │   ├── eval_local.py                 # train.json answer 대비 IoU 측정
│   │   ├── tools/scenario_summary.py
│   │   ├── results_pilot_v3/             # test 0-49
│   │   ├── results_batch_a/              # test 50-249
│   │   ├── results_batch_b/              # test 250-499
│   │   └── submission/submission_v1.csv
│   └── track_b/                          # IP 네트워크 에이전트
│       ├── agent.py                      # 메인 에이전트 (1487 LOC)
│       ├── results_v6_full/              # v6 baseline (47/50 solved)
│       ├── results_v6_retry*/            # Non-solved 문제 재실행
│       ├── results_v10_test/             # HIGH-ALIAS 수정본
│       └── submission/submission_v6_full_v10.csv
├── data/
│   ├── Track A/                          # 무선 데이터 + tool server + 2000+500 scenarios
│   │   ├── server.py, main.py            # 공식 제공 코드 (server.py 수정 금지)
│   │   ├── data/Phase_1/{train,test}.json
│   │   └── examples/traces.json          # 전문가 풀이 (few-shot 소스)
│   └── Track B/                          # IP 데이터 + tool server + 50 scenarios
│       ├── server.py, devices_outputs/   # 공식 제공 + CLI 출력 (541MB)
│       └── data/Phase_1/test.json
├── docs/
│   ├── 00_index.md                       # 전체 인덱스
│   ├── common/                           # 챌린지·데이터 공통 문서
│   ├── track_a/
│   │   ├── 03-1_architecture.md          # 에이전트 흐름 (Mermaid)
│   │   ├── 03-2_topology.md              # 5G RAN 개념 + A3 공식
│   │   ├── 03-3_problems.md              # 7-pattern + train 2000 통계
│   │   ├── 04_rag_architecture.md        # RAG 상세 설계
│   │   └── 08_track_a_progress.md        # 실행 로그
│   └── track_b/
│       ├── 03-1_architecture.md
│       ├── 03-2_topology.md              # + D2/SVG 다이어그램 (Traditional + PJ)
│       ├── 03-3_problems.md              # 50문제 답안 (v8 매핑)
│       ├── 03-3-1_problems_detail.md
│       ├── 05_track_b_strategy.md
│       ├── 06_progress_report.md
│       └── 07_not_solved_recovery_strategy.md
└── .moai/
    ├── cache/track_a_train_features.json # RAG precompute (1.1 MB)
    └── plans/                            # 세션 플랜 + Opus 수작업 풀이
```

## 대회 정보

| 항목 | 내용 |
|------|------|
| **총 상금** | EUR 40,000 (트랙별 1등: EUR 12,500 + MWC Shanghai 초청) |
| **필수 모델** | Qwen3.5-35B-A3B (fine-tuning 허용, 모델 교체 불가) |
| **Track A** | 무선 5G 드라이브 테스트 최적화, train 2000 + test 500, IoU 채점 |
| **Track B** | IP 네트워크 O&M, Phase 1 50문제, Exact Match |
| **Phase 1** | 4/3 ~ 5/4 (연습, 무제한 제출) |
| **Phase 2** | 5/4 ~ 5/18 (예선, Top 30, 최대 3회 제출) |
| **Phase 3** | 5/18 ~ 5/29 (결선, fine-tuned weights 동반 1회 제출) |
| **파트너** | GSMA, ETSI, ITU, IEEE GenAINet, TM Forum |

## 평가 기준

- **Phase 1**: 정확도만, 무제한 제출
- **Phase 2**: 정확도 + 효율성 (API 호출 수)
- **Phase 3**: 정확도 × 시간 할인
  - `5분 미만`: 100%
  - `5~10분`: 80%
  - `10~15분`: 60%
  - `15분 초과`: **0%** (타임아웃)

## 현재 진행 상태 (2026-04-23)

### Track A — Phase 1 submission v1 준비 완료

- Stage A (Opus 수작업) → **9/10 정답**, P1~P7 패턴 라이브러리 도출
- Stage B (agent/track_a/) → agent.py + prompts.py + rag.py + generate_submission.py
- Stage C (500/500 실행 완료) → Pilot v3 50 + Batch A 200 + Batch B 250
- 로컬 검증 (train 50 v3 RAG): **IoU 0.220** (baseline 0.160 대비 +38%)
- 이슈: test Batch 에서 P7 fallback 68.6% (train 50 36% 대비 악화) — 개선 선택지 A~D 는 `docs/track_a/08_track_a_progress.md` 참조

### Track B — 48/50 solved, v10 후보 준비 완료

- v6_full 50/50 실행 (47 Qwen solved + 1 forced + 2 timeout)
- Non-solved Q11/Q36/Q38 → 프롬프트 강화 + Opus overlay 로 해결
- v10: Q29 자동 도출 + Q31/Q32 HIGH-ALIAS RULE 1~4 회귀 수정
- 상세: `docs/track_b/06_progress_report.md`, `07_not_solved_recovery_strategy.md`

## 라이선스

대회 데이터: CC-BY-SA 4.0 | 에이전트 코드: MIT
