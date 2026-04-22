# Track B Phase 1 - 50문제 상세 정리

> `data/Track B/data/Phase_1/test.json` 전수 분석

본 문서는 03-3_problems.md의 확장판으로, **각 문제의 상황·과제·단서·출력 포맷**을 문제 단위로 기술한다. 에이전트 프롬프트 튜닝 및 유형별 전략 수립의 1차 레퍼런스.

---

## 1. 전체 구성

### 1.1 유형별 분포

| 유형 | 범위 | 개수 | 비중 |
|------|------|-----|------|
| **Topology** (링크 복원) | Q1–Q6, Q29–Q33 | 11 | 22% |
| **Path** (경로 추적) | Q7–Q16, Q34–Q38 | 15 | 30% |
| **Fault** (장애 진단) | Q17–Q28, Q39–Q50 | 24 | 48% |

### 1.2 네트워크 영역별 분포

| 영역 | 노드 prefix | 문제 | 개수 |
|------|------------|------|------|
| **Traditional** (Alpha/Beta/Gamma/Delta 존) | `Alpha-*`, `Beta-*`, `Gamma-*`, `Delta-*` | Q1–Q28 | 28 |
| **PJ / PJGFA** (Prime/Hermes 계열) | `Demeter-*`, `Atlas-*`, `Janus-*`, `Aegis-Prime-*`, `Hermes-*` | Q29–Q50 | 22 |

### 1.3 Traditional Zone 구성

- **Big Data Zone**: `Gamma-*` 계열
- **Development & Testing Zone**: `Beta-*` 계열
- **Management Zone**: `Delta-*` 계열
- **Core**: `Alpha-Center-01`, `Alpha-Center-02` (존 간 경유지)

---

## 2. Topology 문제 (11개) - 링크 복원

### 2.1 공통 규격

- **목적**: 특정 노드의 "planning data" 가 삭제된 상태에서, **UP 상태 인터페이스의 링크 정보**를 복원
- **권장 쿼리 순서**
  1. `display lldp neighbor brief` (직접 조회) — 1순위
  2. 불가능 시: `display interface description` + 로컬/원격 노드의 `display arp`
  3. 인터페이스 description 과 ARP 정보가 다르면 **ARP 우선**
- **출력 포맷**: `LocalNode(LocalPort)->RemoteNode(RemotePort)` 한 줄에 한 링크, 앞뒤·중간 공백 금지

### 2.2 문제별 설명

#### Q1 — `Gamma-Aegis-01` 링크 복원 (Big Data Zone)

- **상황**: Big Data Zone의 `Gamma-Aegis-01` 노드 "planning data"(링크 계획 자료)가 실수로 삭제됨.
- **해결 과제**: 이 노드에서 **상태가 UP인 인터페이스**들의 peer 측 연결 정보를 원복해 링크 목록을 산출.
- **단서**: LLDP 직접 조회 가능한 전형적 케이스.
- **출력 예**: `Gamma-Aegis-01(GE1/0/0)->Gamma-Portal-01(GE1/0/4)`

#### Q2 — `Gamma-Axis-02` 링크 복원 (Big Data Zone, LLDP 불가)

- **상황**: `Gamma-Axis-02` planning data 삭제. 단, **이 노드 자체에서는 LLDP 조회 불가**.
- **해결 과제**: 주변 9개 노드(`Gamma-Portal-01/02`, `Gamma-Aegis-01/02`, `Gamma-Axis-01`, `Gamma-Node-01~04`)에 LLDP를 돌려 역추적, UP 링크 복원.
- **단서**: 이웃 후보 9개가 명시됨. 전부에 `display lldp neighbor brief` 던지면 `Gamma-Axis-02` 연결 엔트리만 뽑아내면 됨.

#### Q3 — `Beta-Aegis-02` 링크 복원 (Dev & Test Zone)

- **상황**: 개발·테스트 영역 `Beta-Aegis-02` planning data 삭제.
- **해결 과제**: UP 인터페이스 링크 복원.
- **단서**: Q1과 같은 표준 케이스.

#### Q4 — `Beta-Portal-02` 링크 복원 (Dev & Test Zone)

- **상황**: `Beta-Portal-02` planning data 삭제.
- **해결 과제**: 토폴로지 상의 UP 링크 기록 복원.
- **단서**: 표준 케이스.

#### Q5 — `Delta-Node-01` 링크 복원 (Management Zone)

- **상황**: 관리 구역 `Delta-Node-01` planning data 삭제.
- **해결 과제**: 해당 노드 UP 인터페이스 링크 복원.
- **단서**: 표준 케이스.

#### Q6 — `Delta-Axis-01` 링크 복원 (Management Zone)

- **상황**: 관리 구역 `Delta-Axis-01` planning data 삭제.
- **해결 과제**: UP 인터페이스 링크 복원.
- **단서**: 표준 케이스.

### 2.3 PJ 영역 (Q29–Q33)

> PJ 영역은 "Query link neighbor status" 표현을 사용하지만 실질 의미는 LLDP와 동일.

#### Q29 — `Demeter-Prime-01` 링크 복원 (PJ)

- **상황**: PJ 영역 prime 노드 `Demeter-Prime-01` planning data 삭제.
- **해결 과제**: UP 링크 복원. 링크 이웃 상태 직접 조회가 1순위, 불가 시 interface description + ARP 조합.

#### Q30 — `Atlas-Prime-01` 링크 복원 (PJ)

- **상황**: PJ 영역 `Atlas-Prime-01` planning data 삭제.
- **해결 과제**: UP 링크 복원. 표준 PJ 케이스.

#### Q31 — `Janus-Prime-01` 링크 복원 (PJ)

- **상황**: `Janus-Prime-01` planning data 삭제.
- **해결 과제**: UP 링크 복원.

#### Q32 — `Aegis-Prime-01` 링크 복원 (PJ)

- **상황**: `Aegis-Prime-01` planning data 삭제.
- **해결 과제**: UP 링크 복원.

#### Q33 — `Janus-Node-02` 링크 복원 (PJGFA sub)

- **상황**: PJGFA 영역 sub-node `Janus-Node-02` planning data 삭제.
- **해결 과제**: UP 링크 복원. Prime 계층 대신 하위 node 레벨.

---

## 3. Path 문제 (15개) - 경로 추적

### 3.1 공통 규격

- **목적**: 소스 노드가 특정 목적지(IP 또는 인터페이스)를 addressing 할 때의 **실제 포워딩 경로** 기술
- **권장 쿼리 순서**
  1. 소스 노드의 `display ip routing-table` + `display current-configuration`
  2. 매칭 route의 next-hop IP / egress interface 확인
  3. 인접 노드로 이동하여 2단계 반복 (**모든 홉을 기술**, 중간 노드 생략 금지)
- **출력 포맷**: `NodeA->NodeB->NodeC` 한 줄, 공백 금지

### 3.2 Traditional 영역 문제별 설명 (Q7–Q16)

#### Q7 — `Beta-Node-01` → `Gamma-Node-01` GE1/0/2 (192.168.70.22/30)

- **상황**: Dev&Test Zone의 Beta-Node-01 에서 Big Data Zone의 Gamma-Node-01 특정 인터페이스 IP까지 경로 확인.
- **해결 과제**: 존 간 경유지(보통 Alpha-Center-\*)를 지나는 전체 홉 경로 기술.
- **단서**: 목적지 서브넷 마스크 /30 명시.

#### Q8 — `Gamma-Node-01` → `Delta-Node-01` GE1/0/2 (/30)

- **상황**: Big Data Zone → Management Zone 간 addressing.
- **해결 과제**: Gamma → (코어 경유) → Delta 경로 기록.

#### Q9 — `Beta-Node-03` → `Delta-Node-03` GE1/0/2 (/30)

- **상황**: Dev&Test → Management 간 addressing.
- **해결 과제**: Beta-Node-03 에서 시작해 Delta-Node-03 도달 경로 추적.
- **주의**: v6 smoke에서 이 문제가 780초까지 소요(긴 reasoning).

#### Q10 — `Gamma-Node-01` → `Beta-Node-04` GE1/0/2

- **상황**: Big Data → Dev&Test 역방향 addressing.
- **해결 과제**: 경로 기술.

#### Q11 — `Beta-Node-03` → `Alpha-Center-02` GE1/0/2 (Spine routing 실패)

- **상황**: `Test-Zone1-Spine02` 가 **routing 정보를 찾지 못함**. 이 Spine은 `Beta-Portal-01/02` 와 연결된 장비.
- **해결 과제**: Spine02 경유 불가능한 상황에서 Beta-Portal-01(또는 대안)을 통한 우회 경로 산출.
- **단서**: Spine02 이름이 test.json 에 별도 등장 — 단순 routing table 조회로는 안 보일 수 있으므로 토폴로지 추론 필요.

#### Q12 — `Beta-Node-01` → `Gamma-Node-01` GE1/0/2 (Portal 경유, 중간 1개)

- **상황**: 경로가 `Gamma-Portal-02` 를 반드시 지나며, Portal-02 ↔ Gamma-Node-01 사이에 **중간 노드가 정확히 1개**.
- **해결 과제**: 해당 제약을 만족하는 유일한 경로를 찾아 기술.
- **단서**: 제약 힌트는 탐색 공간 축소 + 후보 검증용.

#### Q13 — `Gamma-Node-02` → `Beta-Node-04` GE1/0/4

- **상황**: Big Data → Dev&Test addressing.
- **해결 과제**: Beta-Node-04 최종 홉 진입 경로. 힌트로 Beta-Node-04 이웃(Axis-01/02, Node-03) 제공.
- **단서**: 최종 접근 인터페이스는 Beta-Node-04 측 중 힌트에 맞는 peer로 판정.

#### Q14 — `Delta-Node-02` → `Gamma-Node-02` GE1/0/2

- **상황**: Management → Big Data addressing.
- **해결 과제**: Gamma-Node-02 도달. 힌트로 Gamma-Node-02 이웃(Node-01, Axis-01/02) 제공.
- **단서**: 목적 노드 접근 인터페이스 후보 제한.

#### Q15 — `Gamma-Node-04` → `Delta-Node-01` GE1/0/2 (/30, Delta-Axis-02 불가)

- **상황**: `Delta-Axis-02` 라우트 불가. 이 Axis는 `Delta-Node-01/02`, `Delta-Axis-01` 과 연결.
- **해결 과제**: Delta-Axis-02 우회 경로로 Delta-Node-01 도달.
- **단서**: Q11 와 유사하게 **금지 노드** 조건이 주어진 재라우팅 문제.

#### Q16 — `Beta-Aegis-02` → `Delta-Node-04` GE1/0/2 (/30)

- **상황**: Dev&Test 코어(Aegis) → Management 노드 addressing.
- **해결 과제**: Beta-Aegis-02 에서 시작해 Delta-Node-04 까지의 전체 경로.

### 3.3 PJ 영역 문제별 설명 (Q34–Q38)

#### Q34 — `Hermes-Prime-01` → 10.1.1.20 (PJ)

- **상황**: PJ 영역 내부 IP 10.1.1.20 addressing.
- **해결 과제**: Hermes-Prime-01 routing 기준 목적지 IP의 forwarding 경로.

#### Q35 — `Hermes-Prime-01` → 20.1.1.10 (PJ)

- **상황**: 목적 IP 대역이 다른 PJ 서브넷.
- **해결 과제**: 동일 PJ 내 혹은 PJGFA 경유 경로.

#### Q36 — `Hermes-Node-01` → 10.1.1.10 (PJGFA)

- **상황**: PJGFA 노드에서 시작. PJ 혹은 자신의 하위망 IP 도달.
- **해결 과제**: 경로 기술.

#### Q37 — `Hermes-Node-01` → 20.1.1.20 (PJGFA)

- **상황**: PJGFA 소스, 20.x 대역 목적지.
- **해결 과제**: 경로 기술.

#### Q38 — `Hermes-Prime-01` → 20.1.4.20 (PJ)

- **상황**: 20.1.4.x 서브넷 목적지.
- **해결 과제**: PJ 내부 혹은 외부 경유 경로.

---

## 4. Fault 문제 (24개) - 장애 진단

### 4.1 공통 규격

모든 Fault 문제는 **Routing Fault** 와 **Port Fault** 두 카테고리 중 하나 또는 둘의 조합으로 진단 결과를 출력.

#### 출력 포맷

- **Routing Fault**: `fault-node;destination-IP;fault-reason`
- **Port Fault**: `fault-node;fault-port;fault-reason`
- 각 줄 = 1 fault, 빈 줄 금지, 공백 금지, 모든 기호는 영문
- 복수 원인은 줄마다 반복

#### 예시

```
Beta-Axis-01;192.168.1.1;blackhole route
Alpha-Center-02;192.168.1.2;missing static route
Beta-Portal-01;GE1/0/1;shutdown
Beta-Node-01;GE1/0/2;interface IP error
```

### 4.2 Fault Reason 카탈로그

#### Routing Fault Reasons (13종, Traditional·PJ 공통)

1. blackhole route
2. missing static route
3. static route error
4. ARP configuration error
5. routing loop
6. BGP configuration error
7. OSPF configuration error
8. loopback IP configuration conflict
9. VXLAN configuration error
10. L3VPN configuration error
11. L2VPN configuration error
12. IS-IS configuration error
13. SRV6-Policy tunnel planning error

#### Port Fault Reasons

| # | Traditional (Q17–Q28, 7종) | PJ (Q39–Q50, 8종) |
|---|---------------------------|-------------------|
| 1 | shutdown | shutdown |
| 2 | interface IP error | interface IP error |
| 3 | traffic congestion on port bandwidth | traffic congestion on port bandwidth |
| 4 | MAC address configuration error | MAC address configuration error |
| 5 | VPN configuration missing | VPN configuration missing |
| 6 | OSPF configuration error | OSPF configuration error |
| 7 | MTU value configuration error | MTU value configuration error |
| 8 | — | **host information collection function missing** (PJ 전용) |

### 4.3 Traditional 영역 문제별 설명 (Q17–Q28)

#### Q17 — Beta-Node-01 → Gamma-Node-01 GE1/0/2 서비스 단절 (3-노드 용의자)

- **상황**: Dev&Test 영역 Beta-Node-01 이 Big Data Zone Gamma-Node-01 GE1/0/2 로 접근하는데 **서비스가 끊김**.
- **해결 과제**: `Beta-Axis-02`, `Beta-Portal-02`, `Alpha-Center-02` **세 노드 중** 장애 유발 노드를 찾아 원인 판정.
- **진단 가이드**: 각 용의 노드에서 routing/interface/OSPF/BGP 상태 확인. 인터페이스 down, route black-hole, protocol 설정 오류 중 어느 것인지 식별.

#### Q18 — Beta-Node-01 → Gamma-Node-01 GE1/0/2 (unreachable)

- **상황**: Q17과 같은 source/destination 쌍이지만 용의자 지정 없음.
- **해결 과제**: 전체 경로에서 fault 원인 탐색.
- **단서**: 여러 fault 동시 가능.

#### Q19 — Beta-Node-01 → Gamma-Node-01 GE1/0/2 (다른 시나리오)

- **상황**: Q18과 지문 유사, scenario_id 다름.
- **해결 과제**: 동일 패턴 진단 수행. 실제 시뮬 상태는 다를 수 있으므로 재쿼리 필수.

#### Q20 — Beta-Node-01 → 외부 IP 192.168.74.13/30 (단일 노드 fault)

- **상황**: 외부 대역 접근 실패. **fault 노드는 정확히 1개**.
- **해결 과제**: 루트 홉부터 외부 게이트웨이까지 탐색해 단일 원인 노드 식별.
- **단서**: "fault 노드 1개" 제약은 출력 줄 수 검증에 사용.

#### Q21 — Beta-Node-01 → 192.168.70.22/30 (unreachable)

- **상황**: 내부 서브넷 addressing 실패.
- **해결 과제**: routing/port fault 진단.

#### Q22 — Beta-Node-02 → Gamma-Node-01 GE1/0/2 (단일 노드 fault)

- **상황**: source가 Beta-Node-02 로 바뀜. **단일 fault**.
- **해결 과제**: 경로상 단일 장애 노드 확정.

#### Q23 — Delta-Node-01 → 외부 IP 192.168.74.61/30

- **상황**: Management Zone 에서 외부 addressing 트래픽 단절.
- **해결 과제**: Delta 존 출구 및 코어 경유지 점검.

#### Q24 — Beta-Aegis-01 → Delta-Aegis-02 GE0/0/1 (192.168.72.78/30)

- **상황**: 존 간 aegis 수준 상호 addressing 실패.
- **해결 과제**: OSPF/BGP 인접, interface, L3VPN 점검.

#### Q25 — Beta-Node-01 → 192.168.70.70/30

- **상황**: 70.70/30 대역 unreachable.
- **해결 과제**: Q21과 유사 패턴.

#### Q26 — Gamma-Node-01 → Alpha-Center-02 GE1/0/6

- **상황**: Big Data → Core interface 접근 실패.
- **해결 과제**: Gamma 출구 + Alpha-Center-02 입력 포트 상태 점검.

#### Q27 — Beta-Node-02 → Gamma-Node-01 GE1/0/2 (Q22 변형)

- **상황**: Q22와 유사하나 단일 fault 조건 명시 없음.
- **해결 과제**: 경로 전체 진단.

#### Q28 — Beta-Node-01 → 192.168.70.93/30

- **상황**: 70.93/30 addressing 실패.
- **해결 과제**: routing/port fault 추적.

### 4.4 PJ 영역 문제별 설명 (Q39–Q50)

> PJ 영역은 port fault 원인에 `host information collection function missing` 이 추가된다.

#### Q39 — Hermes-Prime-01 → ping 20.1.1.10 실패

- **상황**: PJ 영역 prime 노드에서 20.1.1.10 ping 불가.
- **해결 과제**: routing 경로 + port 설정 점검으로 fault 원인 출력.

#### Q40 — Hermes-Prime-01 → ping 10.1.6.3 실패

- **상황**: 10.1.6.x 대역 unreachable.
- **해결 과제**: 해당 대역 static/dynamic route, ARP, interface 점검.

#### Q41 — Hermes-Prime-01 → ping 10.1.6.3 실패 (Q40 반복)

- **상황**: Q40과 같은 문구지만 별도 scenario_id.
- **해결 과제**: 동일 패턴 재진단. 시뮬 상태가 다를 수 있으니 **결과 캐싱 금지**.

#### Q42 — Demeter-Prime-02 MAC 주소 충돌 알람

- **상황**: `Demeter-Prime-02` 가 MAC address conflict 알람 수신.
- **해결 과제**: MAC 충돌 원인 노드·포트 식별 → port fault `MAC address configuration error` 또는 routing 쪽의 ARP 이슈 점검.
- **특이**: 다른 문제들과 달리 **ping unreachable 이 아닌 alarm-driven 진단**.

#### Q43 — Hermes-Prime-01 → ping 20.1.1.10 (Q39 반복)

- **상황**: Q39와 동일 지문, 다른 scenario_id.
- **해결 과제**: 재진단.

#### Q44 — Hermes-Prime-02 → ping 10.60.1.2 (외부 주소)

- **상황**: `Hermes-Prime-02` 에서 외부 10.60.1.2 ping 실패.
- **해결 과제**: PJ 영역 출구 (우회 라우팅/BGP peer/ L3VPN) 및 port 상태 검증.

#### Q45 — Hermes-Prime-01 → ping 10.60.1.2 (외부)

- **상황**: source가 Prime-01 로 바뀜.
- **해결 과제**: Q44와 유사하게 외부 addressing 경로 점검.

#### Q46 — Hermes-Prime-01 → ping 20.1.1.10 (Q39/Q43 반복)

- **상황**: Q39 시나리오 3번째 반복.
- **해결 과제**: 재진단.

#### Q47 — Hermes-Prime-02 → ping 20.1.1.20 실패

- **상황**: 20.1.1.20 unreachable.
- **해결 과제**: routing/port 점검.

#### Q48 — Hermes-Prime-02 → ping 20.1.1.20 (Q47 반복)

- **상황**: Q47과 같은 문구.
- **해결 과제**: 재진단.

#### Q49 — Hermes-Prime-01 → ping 20.1.4.10 실패

- **상황**: 20.1.4.x 서브넷 unreachable.
- **해결 과제**: Path Q38(20.1.4.20 경로)과 같은 경로 상의 fault 여부 확인.

#### Q50 — Hermes-Prime-01 → ping 10.1.1.20 실패

- **상황**: Path Q34(10.1.1.20 경로)의 fault 버전.
- **해결 과제**: Q34 경로에 장애가 주입된 상태 진단.

---

## 5. 유형별 난이도·전략 요약

### 5.1 Topology (난이도 ★☆☆)

- 평균 2~3회 tool call
- 1순위: `display lldp neighbor brief` 직접 조회
- 실패 케이스 (Q2): 이웃 9개에 동일 쿼리 병렬로 던지고 ARP cross-check
- **Risk**: 인터페이스가 admin-up 이지만 실제 peer 쪽 링크 down 인 경우 걸러내야 함

### 5.2 Path (난이도 ★★☆)

- 평균 5~15회 tool call, 홉 수만큼 반복
- **반드시 모든 홉 기술** (중간 생략 금지) — evaluator가 정확 일치로 채점할 가능성 높음
- 힌트가 주어진 경우 (Q11, Q12, Q13, Q14, Q15): 힌트를 우선 반영해 탐색 공간 축소
- Qwen3 reasoning 토큰 소비가 큼 → `MAX_TOKENS=8192` 권장

### 5.3 Fault (난이도 ★★★)

- 평균 6~15회 tool call, 가장 오래 걸리는 유형 (Q17: 592초 측정)
- 증상 → 가설 → 검증 루프 필요 (라우팅 테이블, 인터페이스, OSPF neighbor, BGP peer, ARP 등 다각 점검)
- **다중 fault 가능성** 염두 (한 시나리오에 다른 reason 여러 줄 출력)
- PJ 영역은 `host information collection function missing` 원인 추가 숙지 필수
- 반복 시나리오 (Q40/Q41, Q47/Q48 등)는 동일 답일 가능성이 높으나 scenario_id 별 장비 상태가 다를 수 있으므로 **캐싱 지양**

---

## 6. 에이전트 구현 시 체크리스트

- [ ] 질문 유형 자동 감지 (`detect_question_type`)에서 키워드 기반 분류 적중 여부 확인
  - Topology: "planning data", "restore", "link", "UP interface"
  - Path: "->", "path", "addressing", "trace"
  - Fault: "fault", "service", "unreachable", "ping", "interrupt"
- [ ] 출력 포맷 규약을 system prompt 에 강조 (공백/빈 줄 엄격 금지)
- [ ] Path 문제: next-hop 재귀 탐색 템플릿 적용
- [ ] Fault 문제: routing + port 두 카테고리 병렬 검토
- [ ] PJ 영역: node prefix 로 감지해 fault-reason 카탈로그 8종으로 확장
- [ ] 반복 scenario 감지 시 재쿼리 보장 (시드 결과 캐싱 금지)

---

## 7. 참고 파일

- 원본 데이터: `data/Track B/data/Phase_1/test.json`
- 상위 분석: `docs/03-3_problems.md`
- 네트워크 구조: `docs/03-2_topology.md`, `docs/03-2_topology_pj.svg`, `docs/03-2_topology_traditional.svg`
- 전략: `docs/05_track_b_strategy.md`
- 진행 리포트: `docs/06_progress_report.md`
