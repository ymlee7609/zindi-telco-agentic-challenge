# 데이터 및 아키텍처 상세 분석

## 1. 전체 데이터 구조

```
data/
├── README.md                          # 챌린지 메타 (MIT 라이선스)
├── Track A/                           # 무선 네트워크 (30MB)
│   ├── README.md                      # Track A 상세 가이드
│   ├── server.py                      # Agent Tool Server (수정 불가)
│   ├── main.py                        # Agent 설계 (수정 가능, 핵심 파일)
│   ├── _types.py                      # ToolCall 타입 정의
│   ├── utils.py                       # 답변 추출, 점수 계산 유틸
│   ├── logger.py                      # 로깅
│   ├── requirements.txt               # 의존성
│   ├── data/Phase_1/
│   │   ├── train.json                 # 학습 2,000문제 (답 포함)
│   │   └── test.json                  # 테스트 500문제 (답 없음)
│   └── examples/traces.json           # 예제 추론 과정 2건
├── Track B/                           # IP 네트워크 (584MB)
│   ├── README.md                      # Track B 상세 가이드
│   ├── server.py                      # Agent Tool Server (로컬 배포)
│   ├── requirements.txt               # 서버 의존성
│   ├── question_limits_config.json    # API 호출 제한 설정
│   ├── devices_outputs.zip            # 멀티벤더 CLI 출력 (541MB 압축 해제)
│   ├── devices_outputs/               # Huawei/Cisco/H3C 장비 출력 파일
│   ├── data/Phase_1/
│   │   └── test.json                  # 테스트 50문제 (답 없음, 학습 데이터 없음)
│   ├── examples/traces.json           # 예제 추론 과정 3건
│   └── agent/                         # OpenClaw 기반 에이전트 예제
│       ├── evaluate_openclaw.py       # 배치 평가 스크립트
│       ├── evaluate_openclaw_guideline.md
│       ├── requirements.txt
│       ├── openclaw_config/           # 에이전트 설정
│       │   ├── IDENTITY.md            # 에이전트 정체성 (NetOps-Agent)
│       │   ├── SOUL.md                # 행동 원칙
│       │   ├── USER.md                # 사용자 시나리오
│       │   ├── AGENTS.md              # 에이전트 협업 설정
│       │   └── TOOLS.md               # 도구 목록 (NOC API)
│       └── skills/                    # 네트워크 O&M 스킬
│           ├── infra_maintenance/     # 인프라 유지보수
│           ├── l2_link/               # L2 링크 O&M
│           ├── l3_route/              # L3 라우팅
│           └── adv_tunnel/            # 고급 터널 (VXLAN/SRv6)
└── submission/Phase_1/
    └── result.csv                     # 제출 템플릿 (Track A + Track B 통합)
```

## 2. Track A 상세 분석

### 데이터 구조

```json
{
  "scenario_id": "UUID",
  "tag": "single-answer | multiple-answer",
  "task": {
    "description": "질문 텍스트 + \\boxed{} 응답 형식 지시",
    "options": [{"id": "C1", "label": "...최적화 방안 설명..."}, ...]
  },
  "answer": "C9 | C2|C8|C11|C16",     // train만 포함
  "context": {
    "description": "시나리오 설명 (5G 드라이브 테스트 등)",
    "wireless_network_information": {...}
  },
  "data": {
    "user_plane_data": {...},
    "network_configuration_data": {...},
    "signaling_plane_data": {...},
    "traffic_data": {...},
    "mr_data": {...},
    "notes": "...",
    "collection_method": "..."
  },
  "tools": {
    "description": "분석 도구 설명",
    "capabilities": ["data retrieval"]
  }
}
```

### 문제 유형 분포

| 유형 | 수량 | 비율 |
|------|------|------|
| single-answer | 1,701 | 85% |
| multiple-answer | 299 | 15% |

### 서버 아키텍처 (Track A)

```
Environment(private dataset) → server.py(tools&simulator, 수정불가)
                                 ↓
                    main.py(Agent 설계) + skills(선택) + Qwen3.5-35B(fine-tuned)
```

**사용 가능 도구 (server.py endpoint)**:
- `get_throughput_logs` - 처리량 로그
- `get_serving_cell_pci` - 서빙 셀 PCI
- `get_serving_cell_rsrp` / `get_serving_cell_sinr` - RSRP/SINR
- `get_cell_info` - 셀 상세 정보 (Config, 파라미터)
- `get_user_location` / `get_gnodeb_location` - 위치 정보
- `get_neighboring_cells_pci` / `get_neighboring_cell_rsrp` - 이웃 셀
- `get_config_data` / `get_user_plane_data` - 설정/사용자 데이터
- `get_signaling_plane_event_log` - 시그널링 이벤트 로그
- `get_kpi_data` / `get_mr_data` - KPI/MR 데이터
- `calculate_*` / `judge_*` - 계산/판단 도구
- `optimize_antenna_gain` - 안테나 이득 최적화

### 예제 추론 과정 (traces.json)

전형적 워크플로:
1. `get_throughput_logs` → 처리량 저하 시점 식별
2. `get_serving_cell_pci` → 저하 시점의 서빙 셀 확인
3. `get_cell_info` → 셀 설정 파라미터 확인 (A3 Offset, 파워 등)
4. `get_serving_cell_rsrp/sinr` → 신호 품질 확인
5. `get_neighboring_cells_pci` → 이웃 셀 존재 확인
6. `get_neighboring_cell_rsrp` → 이웃 셀 신호 강도 비교
7. 분석 → 근본 원인 판단 → `\boxed{C9}` 형태 응답

## 3. Track B 상세 분석

### 데이터 구조

```json
{
  "scenario_id": "UUID",
  "task": {
    "question": "개방형 질문 텍스트 (링크 복원, 경로 조회, 장애 진단 등)",
    "id": 1
  }
}
```

**주요 특징**: 답(answer) 없음, 학습 데이터 없음 → 에이전트 능력으로만 해결

### 문제 유형 분석

| 키워드 | 빈도 | 관련 문제 유형 |
|--------|------|--------------|
| path | 27 | 경로 조회 |
| route | 26 | 라우팅 분석 |
| fault | 24 | 장애 진단 |
| ospf | 24 | OSPF 프로토콜 |
| bgp | 24 | BGP 프로토콜 |
| vxlan | 24 | VXLAN 터널 |
| link | 11 | 링크 상태 |
| topology | 5 | 토폴로지 복원 |

### 3대 문제 유형

1. **토폴로지 복원 (Topology Reconstruction)**
   - 삭제된 링크 정보를 복원
   - LLDP, ARP, interface description 활용
   - 출력 형식: `NodeA(port)->NodeB(port)`

2. **경로 조회 (Path Query)**
   - 소스에서 목적지까지의 포워딩 경로
   - 라우팅 테이블, OSPF, BGP 경로 분석
   - 출력 형식: `NodeA->NodeB->NodeC`

3. **장애 진단 (Fault Localization)**
   - 트래픽 중단 원인 분석
   - 라우팅 장애, 포트 장애 식별
   - 출력 형식: `노드;대상IP;원인` 또는 `노드;포트;원인`

### API 구조 (Track B)

```
POST /api/agent/execute
{
  "device_name": "BoardLeaf1",
  "command": "display ip routing-table",
  "question_number": N
}
```

**지원 벤더**: Huawei (VRP), Cisco (IOS/IOS-XE/NX-OS), H3C (Comware)
**지원 장비**: 라우터, 스위치, 방화벽
**커맨드 카테고리**: 45+ (Config, LLDP, VLAN, OSPF, BGP, VXLAN, SRv6 등)

### OpenClaw 에이전트 프레임워크

Track B는 **OpenClaw** 기반 에이전트 예제 제공:
- `IDENTITY.md`: NetOps-Agent 정의
- `TOOLS.md`: NOC API 호출 규약 + 스킬별 벤더 명령어 매핑
- 4개 스킬: infra_maintenance, l2_link, l3_route, adv_tunnel

## 4. 제출 형식

```csv
scenario_id,Track A,Track B
80e3aa96-...,,              ← Track A 문제 (Track B 비워둠)
535afb0d-...,,              ← Track B 문제 (Track A 비워둠)
```

- 양 트랙 통합 CSV 파일
- 미참여 트랙은 빈 칸
- Track A: `C9` 또는 `C2|C8|C11|C16` (오름차순)
- Track B: 자유 형식 텍스트 (Exact Match)

## 5. 핵심 차이점 요약

| 항목 | Track A (무선) | Track B (IP) |
|------|---------------|-------------|
| 학습 데이터 | 2,000문제 (답 포함) | 없음 (0-shot) |
| 테스트 데이터 | 500문제 | 50문제 |
| 질문 형식 | 객관식 (C1~C22) | 개방형 텍스트 |
| 평가 | IoU | Exact Match |
| 도구 서버 | REST API (simulator) | CLI 시뮬레이터 (POST) |
| 벤더 | N/A (무선 5G) | Huawei/Cisco/H3C |
| 에이전트 예제 | main.py (OpenAI SDK) | OpenClaw 프레임워크 |
| Phase 2 제출 | 3회 | 3회 |
| Phase 3 | 500문제, 조직 GPU | 70문제, Docker 자동 실행 |
| 데이터 크기 | 30MB | 584MB |

## 6. 기술적 시사점

### Track A 전략 포인트
- 학습 데이터 풍부 → **파인튜닝 효과 극대화** 가능
- 5G 무선 네트워크 트러블슈팅 도메인 특화
- Tool use 패턴이 정형화됨 (throughput → PCI → cell info → neighbors)
- 답변 형식 `\boxed{}` 파싱 필요

### Track B 전략 포인트
- 학습 데이터 없음 → **in-context learning + RAG + skill 설계** 핵심
- 멀티벤더 CLI 시뮬레이션 → 벤더별 명령어 매핑 필수
- 3가지 문제 유형에 대한 체계적 접근 전략 필요
- OpenClaw 프레임워크 활용 or 자체 에이전트 구축
- devices_outputs (541MB)를 RAG 소스로 활용 가능
