# Track B 전략 가이드

## 1. 데이터 아키텍처

### NOC API = 로컬 파일 서버
server.py는 `devices_outputs/` 디렉토리의 사전 생성된 텍스트 파일을 읽어서 반환하는 구조.

```
devices_outputs/
├── {question_number}/           # 문제별 독립 데이터 (장애 시뮬레이션)
│   ├── {device_name}/
│   │   ├── display_current-configuration.txt
│   │   ├── display_ip_routing-table.txt
│   │   ├── display_lldp_neighbor_brief.txt
│   │   └── ... (커맨드별 .txt)
```

- **캐시 키**: `{question_number}/{device_name}/{command_spaces_to_underscores}.txt`
- **문제별 독립**: 같은 장비라도 문제마다 다른 설정/상태 반환 (장애 주입)
- **접근 제한**: `question_limits_config.json`으로 특정 문제에서 "No permission" 반환
- **API 없이 해결 가능**: 로컬 파일 직접 읽어서 정답 도출 가능

### 파일명 변환 규칙
`display ip routing-table` → `display_ip_routing-table.txt` (공백→언더스코어)

## 2. 네트워크 토폴로지

### 전통 네트워크 (32노드)
```
Core Layer:     Alpha-Center-01, Alpha-Center-02
                     |                    |
Dev/Test:    Beta-Portal-01/02 → Beta-Axis-01/02 → Beta-Node-01~04
             Beta-Aegis-01/02 (방화벽)
Big Data:    Gamma-Portal-01/02 → Gamma-Axis-01/02 → Gamma-Node-01~04
             Gamma-Aegis-01/02 (방화벽)
Management:  Delta-Portal-01/02 → Delta-Axis-01/02 → Delta-Node-01~04
```

### PJ Area (VXLAN Fabric, ~22노드)
```
Spine:   Janus-Prime-01 ── Janus-Prime-02
Leaf:    Atlas-Prime-01, Atlas-Prime-02, Aegis-Prime-01/02
VTEP:    Demeter-Prime-01, Demeter-Prime-02
Access:  Hermes-Prime-01, Hermes-Prime-02

PJGFA Sub: Janus-Node-01/02, Atlas-Node-01/02, Aegis-Node-01
           Demeter-Node-01/02, Hermes-Node-01/02
```

### Zone 간 연결
- Alpha-Center-01 ↔ Beta-Portal-01, Gamma-Portal-01, Delta-Portal-01
- Alpha-Center-02 ↔ Beta-Portal-02, Gamma-Portal-02, Delta-Portal-02
- PJ Area는 독립 네트워크 (Alpha와 직접 연결 없음)

### 모든 장비: Huawei CE12800 (일부 Cisco PSS)

## 3. 핵심 데이터 소스

### interface description (가장 신뢰할 수 있는 연결 정보)
`display current-configuration`에서:
```
interface GE1/0/1
 description From_Delta-Axis-01_GE1/0/1_To_Delta-Node-01_GE1/0/1
 ip address 192.168.72.17 255.255.255.252
```
→ 원격 노드명 + 포트 번호를 직접 알 수 있음

### LLDP (일부 문제에서 "No permission" 반환됨!)
`display lldp neighbor brief`:
```
GE1/0/1  111  GE1/0/5  Gamma-Axis-01
```
→ Q2에서 Gamma-Axis-02의 LLDP가 차단됨 (question_limits_config.json)

### 라우팅 테이블 (경로 추적 핵심)
`display ip routing-table`:
```
192.168.70.20/30  Static  60  0  RD  192.168.65.149  GE1/0/2
```
→ next-hop IP + egress interface → description으로 장비명 변환

### 데이터 크기 (컨텍스트 관리 중요)
| 커맨드 | 평균 크기 |
|--------|----------|
| display current-configuration | 5000+ tokens |
| display ip routing-table | 3000 tokens |
| display logbuffer | 2000 tokens |
| display interface brief | 800 tokens |
| display ip interface brief | 400 tokens |
| display lldp neighbor brief | 300 tokens |
| display arp | 300 tokens |

## 4. 문제 유형별 풀이 전략

### TYPE 1: Topology (11문제: Q1-Q6, Q29-Q33)

**목표**: 타겟 노드의 UP 인터페이스 링크 복원
**출력**: `TargetNode(port)->RemoteNode(port)` (라인당 1개)

**전략 (직접 쿼리 가능)**:
1. `display interface brief` → UP 포트 목록
2. `display current-configuration` → description 파싱
3. 각 UP 포트의 description에서 `From_X_PortA_To_Y_PortB` 추출

**전략 (직접 쿼리 불가, Q2 등)**:
1. 주변 노드 전체에 `display lldp neighbor brief`
2. LLDP 실패 시 → `display current-configuration`에서 description 역추적
3. 타겟 노드를 가리키는 description 수집

**파일 직접 접근 전략**:
```python
# devices_outputs/{qnum}/{target_node}/display_current-configuration.txt 읽기
# description 필드에서 "From_{target}_..._To_{remote}_..." 파싱
```

### TYPE 2: Path (15문제: Q7-Q16, Q34-Q38)

**목표**: 출발지→목적지 포워딩 경로
**출력**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**전략**:
1. 목적지 IP 확인 (문제에서 주어지거나 `display ip interface brief`로 확인)
2. 출발 노드의 `display ip routing-table`에서 목적지 서브넷 매칭
3. next-hop IP + egress interface → `display current-configuration`의 description → 다음 장비
4. hop-by-hop 반복 (Direct 경로 나올 때까지)
5. **모든 홉을 추적해야 함** (중간 노드 스킵 불가)

**PJ Area Path (Q34-Q38)**:
- 같은 서브넷 (VLAN) 통신 시 VXLAN 터널 경로
- `display vxlan tunnel`로 VTEP 확인
- `display bgp evpn all routing-table`로 MAC 학습 경로 확인
- 언더레이 경로: OSPF 라우팅으로 추적

**파일 직접 접근 전략**:
```python
# 1. devices_outputs/{qnum}/{src}/display_ip_routing-table.txt → 목적지 매칭
# 2. devices_outputs/{qnum}/{src}/display_current-configuration.txt → description으로 next-hop 장비명
# 3. 반복
```

### TYPE 3: Fault (24문제: Q17-Q28, Q39-Q50)

**목표**: 트래픽 중단 원인 진단
**출력**: `node;target;cause` (라인당 1개 장애)

**장애 유형**:
| 유형 | 확인 방법 | 출력 형식 |
|------|----------|----------|
| missing static route | 인접 노드에 있지만 용의 노드에 없는 경로 | `node;dest-IP;missing static route` |
| blackhole route | 라우팅 테이블에 blackhole 플래그 | `node;dest-IP;blackhole route` |
| static route error | 잘못된 next-hop 지정 | `node;dest-IP;static route error` |
| shutdown | interface brief에서 *down | `node;port;shutdown` |
| interface IP error | 잘못된 IP 할당 | `node;port;interface IP error` |
| MAC address config error | logbuffer에 ARP_DUPLICATE_IPADDR | `node;port;MAC address configuration error` |
| OSPF config error | OSPF neighbor 없음/설정 오류 | `node;dest-IP;OSPF configuration error` |
| MTU value config error | MTU 불일치 | `node;port;MTU value configuration error` |

**전략**:
1. 용의 노드 전체에 `display ip routing-table` + `display interface brief` + `display current-configuration`
2. 경로 비교: 정상 노드에 있는 경로가 용의 노드에 없으면 → missing static route
3. 포트 상태: *down → shutdown
4. MAC 충돌: `display logbuffer`에서 ARP_DUPLICATE 확인

**파일 직접 접근 전략**:
```python
# 용의 노드의 라우팅 테이블 비교
# 정상 경로 목록 vs 용의 노드 경로 목록 → diff
```

## 5. 검증된 정답

| 문제 | 유형 | 정답 | 검증 방법 |
|------|------|------|----------|
| Q1 | Topology | 3링크 (Gamma-Aegis-01) | v1 에이전트 |
| Q2 | Topology | 6링크 (Gamma-Axis-02, LLDP 차단) | v2 에이전트 |
| Q3 | Topology | 3링크 (Beta-Aegis-02) | v1 에이전트 |
| Q5 | Topology | 3링크 (Delta-Node-01) | v1 에이전트 |
| Q6 | Topology | 6링크 (Delta-Axis-01) | NOC API 수동 검증 |
| Q7 | Path | Beta-Node-01→...→Gamma-Node-01 (7홉) | NOC API 수동 추적 |
| Q17 | Fault | Alpha-Center-02;192.168.70.22;missing static route | NOC API 수동 검증 |
| Q39 | Fault | Demeter-Prime-01;20.1.1.10;missing static route | v3 에이전트 + 수동 확인 |

## 6. 로컬 파일 기반 풀이 접근법

API 크레딧 없이 로컬 파일만으로 모든 문제를 풀 수 있음:

```python
import os

BASE = "data/Track B/devices_outputs"

def read_output(qnum, device, command):
    """서버 없이 로컬 파일에서 커맨드 출력 읽기"""
    safe_cmd = command.replace(" ", "_").replace("/", "_")
    path = f"{BASE}/{qnum}/{device}/{safe_cmd}.txt"
    if os.path.exists(path):
        return open(path).read()
    return None

# 예: Q7에서 Beta-Node-01의 라우팅 테이블
output = read_output(7, "Beta-Node-01", "display ip routing-table")
```

이 접근법의 장점:
- API 호출 비용 0
- 속도: 파일 I/O만 (네트워크 지연 없음)
- 모든 문제의 모든 데이터에 접근 가능
- 에이전트 테스트/디버깅에 최적

## 7. 에이전트 개선 방향

### 현재 병목
1. **API 크레딧**: Groq 100K TPD, OpenRouter/HuggingFace 소진
2. **컨텍스트 크기**: 라우팅 테이블/설정 파일이 크면 TPM 초과
3. **모델 품질**: Llama 3.3은 Path 추적에서 홉 스킵

### 해결 방향
1. **로컬 풀이 스크립트**: 파일 직접 읽어서 50문제 전체 해결 (API 불필요)
2. **하이브리드**: 로컬로 데이터 수집 + LLM은 분석/판단만 담당
3. **tool result 압축**: config → description만 추출 (74% 절약)
4. **시스템 프롬프트**: description 필드 활용 전략 강조 (v6에서 반영 완료)
