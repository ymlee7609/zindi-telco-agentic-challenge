# Telco Troubleshooting Agentic Challenge

> [Zindi 대회 페이지](https://zindi.africa/competitions/telco-troubleshooting-agentic-challenge) | Track B: IP 네트워크 | 총 상금: EUR 40,000

[English](README.md)

## 개요

IP 네트워크 장애를 자율적으로 진단하고 트러블슈팅하는 AI 에이전트 시스템.
GSMA, ETSI, ITU, IEEE GenAINet, TM Forum이 공동 운영하는 **Telco Troubleshooting Agentic Challenge** 참가 프로젝트.

멀티벤더(Huawei/Cisco/H3C) 네트워크 시뮬레이터와 CLI 명령어로 상호작용하며, 3가지 유형의 네트워크 O&M 문제를 해결:

- **토폴로지 복원** — LLDP, ARP, 인터페이스 정보를 활용한 삭제된 링크 복원
- **경로 조회** — 라우팅 테이블 기반 소스→목적지 포워딩 경로 추적
- **장애 진단** — 트래픽 중단 원인 분석 (라우팅 장애/포트 장애)

## 아키텍처

```
┌─────────────────┐     ┌──────────────────────┐
│   Agent (LLM)   │────▶│  Agent Tool Server   │
│ Qwen3.5-35B-A3B │◀────│  (CLI 시뮬레이터)      │
│                 │     │  Huawei/Cisco/H3C    │
│ - 시스템 프롬프트  │     │  102K+ 출력 파일      │
│ - Tool Use      │     └──────────────────────┘
│ - CoT 추론      │
└─────────────────┘
```

## 주요 특징

- **단일 통합 도구**: `execute_cli_command(device_name, command)` 로 모든 벤더 장비 조회
- **병렬 도구 호출**: 한 턴에 여러 장비를 동시 조회하여 효율성 극대화
- **문제 유형별 전략**: 토폴로지/경로/장애 유형에 특화된 프롬프트
- **자동 복구**: 빈 응답, 타임아웃, API 오류 자동 처리
- **이어하기 지원**: 중단된 평가를 이어서 실행 가능

## 빠른 시작

### 1. Agent Tool Server 실행

```bash
cd data/Track\ B/
# 장비 출력 파일 압축 해제 (최초 1회)
unzip devices_outputs.zip -d devices_outputs/
# 서버 시작
python server.py
# http://127.0.0.1:7860 에서 실행
```

### 2. LLM API 설정

HuggingFace 토큰 설정 (Qwen3.5-35B-A3B, novita 프로바이더):

```bash
export HF_TOKEN="hf_your_token_here"
# 또는: hf auth login
```

### 3. 에이전트 실행

```bash
# 단일 문제 테스트
python agent/agent.py -i "data/Track B/data/Phase_1/test.json" --questions 1

# 전체 평가 (50문제)
python agent/agent.py -i "data/Track B/data/Phase_1/test.json"

# 처음부터 실행 (이전 결과 무시)
python agent/agent.py -i "data/Track B/data/Phase_1/test.json" --fresh
```

## 프로젝트 구조

```
├── agent/
│   └── agent.py              # 에이전트 메인 코드
├── data/
│   ├── Track A/              # 무선 네트워크 데이터 (미사용)
│   ├── Track B/              # IP 네트워크 데이터
│   │   ├── server.py         # Agent Tool Server
│   │   ├── devices_outputs/  # CLI 출력 파일 (541MB)
│   │   ├── data/Phase_1/     # 테스트 문제 (50개)
│   │   └── agent/            # OpenClaw 예제 에이전트
│   └── submission/           # 제출 템플릿
└── docs/                     # 문서
    ├── 00_index.md           # 인덱스
    ├── 02_agentic_challenge_overview.md  # 챌린지 상세
    ├── 03_data_analysis.md   # 데이터 분석
    ├── 04_track_b_strategy.md  # 전략
    └── 05_progress_report.md # 진행 경과
```

## 대회 정보

| 항목 | 내용 |
|------|------|
| **총 상금** | EUR 40,000 (1등: EUR 12,500 + MWC Shanghai 초청) |
| **필수 모델** | Qwen3.5-35B-A3B (변경 불가) |
| **Track B** | IP 네트워크, 50문제, Exact Match 평가 |
| **Phase 1** | 4/3 ~ 5/4 (연습, 무제한 제출) |
| **Phase 2** | 5/4 ~ 5/18 (예선, Top 30 선발) |
| **Phase 3** | 5/18 ~ 5/29 (결선, 효율성 스코어링) |
| **파트너** | GSMA, ETSI, ITU, IEEE GenAINet, TM Forum |

## 평가 기준

- **Phase 1**: 정확도만
- **Phase 2**: 정확도 + API 호출 수 (적을수록 유리)
- **Phase 3**: 정확도 × 시간 할인 (5분 미만: 100%, 5~10분: 80%, 10~15분: 60%, 15분 초과: 0%)

## 라이선스

대회 데이터: CC-BY-SA 4.0 | 에이전트 코드: MIT
