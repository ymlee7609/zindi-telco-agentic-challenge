# Track B 전략 및 실행 계획

## 1. 아키텍처 개요

```
┌─────────────────────────────────────────────┐
│  Track B 에이전트 시스템                       │
│                                             │
│  ┌─────────────┐    ┌─────────────────────┐ │
│  │ OpenClaw    │    │ Qwen3.5-35B-A3B    │ │
│  │ Framework   │◄──►│ (base/fine-tuned)   │ │
│  │             │    │                     │ │
│  │ ┌─────────┐ │    └─────────────────────┘ │
│  │ │ Skills  │ │                             │
│  │ │ ·infra  │ │    ┌─────────────────────┐ │
│  │ │ ·l2_link│ │    │ Agent Tool Server   │ │
│  │ │ ·l3_rout│◄────►│ (CLI Simulator)     │ │
│  │ │ ·adv_tun│ │    │ Huawei/Cisco/H3C    │ │
│  │ └─────────┘ │    └─────────────────────┘ │
│  └─────────────┘                             │
└─────────────────────────────────────────────┘
```

## 2. 문제 유형별 공략 전략

### Type 1: 토폴로지 복원 (Topology Reconstruction)

**목표**: 삭제된 노드의 링크 정보를 복원
**전략**:
1. 대상 노드의 잠재 이웃 노드 목록 파악
2. 각 이웃 노드에서 LLDP neighbor 조회 → 대상 노드 연결 확인
3. LLDP 실패 시 fallback: interface description + ARP 테이블 교차 확인
4. UP 상태 인터페이스만 포함

**필수 스킬**: `infra_maintenance` (lldp, config), `l3_route` (arp, ip_int)
**출력 형식**: `NodeA(port)->NodeB(port)` (한 줄에 하나)

### Type 2: 경로 조회 (Path Query)

**목표**: 소스에서 목적지까지의 포워딩 경로 추적
**전략**:
1. 목적지 IP/서브넷 확인 (ip interface brief)
2. 소스 노드 라우팅 테이블에서 next-hop 확인
3. next-hop IP → 해당 장비 식별 (ARP/interface brief)
4. 재귀적으로 다음 hop 추적 → 직접 연결(directly connected)까지
5. 최종 경로 조합

**필수 스킬**: `l3_route` (route_v4, ip_int, arp, ospf_peer)
**출력 형식**: `NodeA->NodeB->NodeC` (한 줄)

### Type 3: 장애 진단 (Fault Localization)

**목표**: 트래픽 중단 원인 분석 (라우팅/포트 장애)
**전략**:
1. 소스 노드 라우팅 테이블에서 목적지 경로 확인
2. hop-by-hop으로 라우팅 테이블 추적
3. 장애 유형 판별:
   - **라우팅 장애**: blackhole route, missing static route, incorrect static route, incorrect ARP, loop
   - **포트 장애**: shutdown, incorrect interface IP, traffic congestion
4. running-config 확인으로 static route 설정 검증
5. interface brief로 포트 상태 확인

**필수 스킬**: `l3_route` (route_v4, ip_int, arp), `infra_maintenance` (config), `l2_link` (int_brief)
**출력 형식**:
- 라우팅: `노드;목적지IP;원인`
- 포트: `노드;포트;원인`

## 3. 환경 구축 순서

### Step 1: OpenClaw 설치
```bash
# OpenClaw 클론 및 설치 (공식 문서 참조)
# Node.js 필수
```

### Step 2: Agent Tool Server 로컬 배포
```bash
cd data/Track\ B/
# devices_outputs.zip 이미 압축 해제됨
pip install -r requirements.txt
python server.py  # localhost:7860 또는 :5000
```

### Step 3: OpenClaw 설정
```bash
# openclaw_config/ → OpenClaw 프로젝트 설정 디렉토리로 복사
# skills/ → OpenClaw 프로젝트 skills 디렉토리로 복사
```

### Step 4: 테스트 실행
```bash
python agent/evaluate_openclaw.py -i data/Phase_1/test.json --questions 1
```

## 4. 데이터 아키텍처 (server.py 분석)

### NOC API = 로컬 파일 서버
server.py는 `devices_outputs/` 디렉토리의 사전 생성된 텍스트 파일을 읽어서 반환합니다.

```
devices_outputs/
├── {question_number}/           # 문제별 독립 데이터 (장애 시뮬레이션)
│   ├── {device_name}/
│   │   ├── display_current-configuration.txt
│   │   ├── display_ip_routing-table.txt
│   │   └── ... (커맨드별 .txt)
```

- **캐시 키**: `{question_number}/{device_name}/{command_spaces_to_underscores}.txt`
- **문제별 독립**: 같은 장비라도 문제마다 다른 설정/상태 반환 (장애 주입)
- **접근 제한**: `question_limits_config.json`으로 특정 문제에서 "No permission" 반환
- **API 없이 해결 가능**: 로컬 파일 직접 읽어서 정답 도출 가능

### 핵심 데이터 소스

| 커맨드 | 용도 | 평균 크기 |
|--------|------|----------|
| `display current-configuration` | **interface description으로 연결 정보** (가장 신뢰) | 5000+ tokens |
| `display ip routing-table` | 라우팅 경로 추적 | 3000 tokens |
| `display interface brief` | 포트 UP/DOWN 상태 | 800 tokens |
| `display lldp neighbor brief` | 이웃 장비 정보 (일부 문제에서 차단됨!) | 300 tokens |
| `display logbuffer` | 장애 로그 (MAC 충돌 등) | 2000 tokens |
| `display arp` | IP-MAC-포트 매핑 | 300 tokens |

### interface description (핵심 발견)
`display current-configuration`에서 각 인터페이스의 description 필드가 원격 장비와 포트를 직접 명시:
```
interface GE1/0/1
 description From_Delta-Axis-01_GE1/0/1_To_Delta-Node-01_GE1/0/1
```
LLDP보다 **더 신뢰할 수 있는** 연결 정보 소스 (LLDP는 일부 문제에서 "No permission" 반환).

### 로컬 파일 기반 풀이
```python
import os
BASE = "data/Track B/devices_outputs"
def read_output(qnum, device, command):
    safe_cmd = command.replace(" ", "_").replace("/", "_")
    path = f"{BASE}/{qnum}/{device}/{safe_cmd}.txt"
    return open(path).read() if os.path.exists(path) else None
```

## 5. 네트워크 토폴로지

### 금융 네트워크 (32노드, Q1~Q28)
전통적 3-Tier 아키텍처. Core(Alpha-Center) → Aggregation(Portal/Aegis) → Access(Axis/Node).

- **Core**: Alpha-Center-01/02 (Zone 간 백본 라우터)
- **Dev/Test Zone**: Beta-* (10대) — 개발/테스트 환경
- **Big Data Zone**: Gamma-* (10대) — 빅데이터 처리
- **Management Zone**: Delta-* (8대) — 운영 관리
- **프로토콜**: Static Route, OSPF

### PJ Area (22노드, Q29~Q50)
Spine-Leaf VXLAN Fabric. 두 네트워크는 **완전히 독립** (직접 연결 없음).

- **Spine**: Janus-Prime-01/02
- **Leaf**: Atlas-Prime-01/02, Aegis-Prime-01/02
- **VTEP**: Demeter-Prime-01/02 (VXLAN 터널 종단점)
- **Access**: Hermes-Prime-01/02
- **External**: PX1 (WAN 게이트웨이)
- **프로토콜**: VXLAN, BGP EVPN, OSPF (언더레이)

### 검증된 정답 (수동 확인)

| 문제 | 정답 |
|------|------|
| Q6 | Delta-Axis-01: 6링크 (description 기반 도출) |
| Q7 | Beta-Node-01→Beta-Axis-02→Beta-Portal-02→Alpha-Center-02→Gamma-Portal-02→Gamma-Axis-02→Gamma-Node-01 |
| Q17 | Alpha-Center-02;192.168.70.22;missing static route |
| Q39 | Demeter-Prime-01;20.1.1.10;missing static route |

## 7. 최적화 방향

### 단기 (Phase 1 기간)
- [ ] 환경 구축 및 baseline 실행
- [ ] 50문제 전체 실행 → 현재 정확도 측정
- [ ] 문제 유형별 실패 패턴 분석
- [ ] 스킬 프롬프트 최적화 (벤더 식별 정확도 개선)
- [ ] 에러 핸들링 강화 (422 응답 처리)

### 중기 (Phase 2 대비)
- [ ] Qwen3.5-35B-A3B 파인튜닝 (도메인 특화)
- [ ] RAG: devices_outputs를 지식 베이스로 활용
- [ ] 문제 유형 자동 분류기 추가
- [ ] CoT (Chain-of-Thought) 프롬프트 전략
- [ ] API 호출 최소화 전략 (Phase 2 평가 기준: 정확도 + API 호출 수)

### 장기 (Phase 3 대비)
- [ ] 5분 이내 응답을 위한 파이프라인 최적화
- [ ] 64노드 대규모 네트워크 대응
- [ ] SRv6/EVPN 고급 프로토콜 지식 강화
- [ ] Docker 컨테이너 실행 환경 테스트

## 8. 핵심 리스크 및 대응

| 리스크 | 영향 | 대응 |
|--------|------|------|
| OpenClaw 설치 실패 | 프레임워크 사용 불가 | 자체 Python 에이전트로 전환 (main.py 참조) |
| Qwen3.5-35B-A3B GPU 부족 | 모델 로컬 실행 불가 | OpenRouter API 활용 (main.py 기본값) |
| Phase 3 효율성 (15분 제한) | 0점 | 불필요한 API 호출 제거, 캐싱, 병렬화 |
| 멀티벤더 명령어 오류 | 422 응답 | 벤더 자동 감지 + 명령어 매핑 테이블 |
| Exact Match 실패 | 정답이지만 형식 불일치 | 출력 형식 정규화 (공백, 줄바꿈 제거) |

## 9. 시간 계획

| 기간 | 목표 |
|------|------|
| 4/14-4/17 | 환경 구축, OpenClaw 설치, 서버 배포 |
| 4/17-4/24 | Baseline 실행, 실패 분석, 프롬프트 최적화 |
| 4/24-5/04 | 파인튜닝, RAG, 정확도 향상 (Phase 1 마감) |
| 5/04-5/18 | Phase 2: 새 데이터 대응, Top 30 진입 목표 |
| 5/18-5/29 | Phase 3: 효율성 최적화, 최종 제출 |
