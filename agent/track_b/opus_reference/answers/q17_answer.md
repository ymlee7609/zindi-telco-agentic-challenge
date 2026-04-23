# Q17 Opus Reference Answer

**scenario_id**: a643f2d3-a4af-46ae-aa5d-8c63b3804658
**type**: FAULT (routing fault root cause)
**source**: Beta-Node-01
**destination**: Gamma-Node-01 GE1/0/2 (192.168.70.22)
**suspects**: Beta-Axis-02, Beta-Portal-02, Alpha-Center-02

## Opus Verdict
v12와 deterministic solver **일치**. Opus 분석 결과도 동일. **제출 개선 불필요**.

## Reference Answer
```
Alpha-Center-02;192.168.70.22;missing static route
```

## Reasoning (증거 기반)

### 1. Destination IP 식별
Gamma-Node-01 `display_ip_interface_brief.txt`:
```
GE1/0/2  UP  192.168.70.22/30
```
→ Target IP = **192.168.70.22**, subnet = 192.168.70.20/30

### 2. 예상 forward path (Beta → Gamma)
토폴로지 분석:
- Beta-Node-01 → Beta-Axis-02 (GE1/0/2) → Beta-Portal-02 (GE1/0/6 or GE1/0/2 path) → Alpha-Center-02 (GE1/0/2) → Gamma-Portal-01 or Gamma-Portal-02 → Gamma-Axis → Gamma-Node-01

Alpha-Center-02의 남쪽 링크:
- GE1/0/5 <-> Gamma-Portal-01 GE1/0/7
- GE1/0/6 <-> Gamma-Portal-02 GE1/0/7

### 3. 의심 장비별 routing table 점검

**Beta-Axis-02**:
- 192.168.70.x 대역 경로 = **없음**
- 하지만 Alpha-Center-02 loopback (192.168.65.2/32)로는 잘 forward됨
- → 내부 Beta zone에서 forward만 담당, Gamma zone route 필요 없음

**Beta-Portal-02**:
- 192.168.70.x 대역 경로 = **없음**
- Alpha-Center-02 loopback으로 OK
- → Spine 역할이지만 Gamma zone route 필요 없음 (다음 홉이 라우팅)

**Alpha-Center-02** (핵심 장비):
- 192.168.65.1/32 → via 192.168.74.46 dev GE1/0/6 (Gamma zone)
- 192.168.65.2/32 → Direct (자기 loopback)
- **192.168.70.20/30 경로 완전 부재**
- **192.168.70.22/32 경로 완전 부재**
- Gamma-Node-01 interface subnet을 모름 → forward 실패

### 4. Root cause 확정
Beta → Gamma forward path에서 Alpha-Center-02는 inter-zone gateway 역할. 이 노드에서 destination 192.168.70.22로 가는 static route 누락 → 패킷 드롭.

→ **Alpha-Center-02;192.168.70.22;missing static route**

### 5. Port fault 가능성 배제
- Alpha-Center-02의 Gamma 방향 port (GE1/0/5, GE1/0/6) 모두 UP
- Beta 방향 port (GE1/0/1, GE1/0/2) 모두 UP
- Log buffer에 shutdown/link-down 이상 없음 (Gamma-Node-01의 GE1/0/1-3는 최종 UP 상태로 복원됨)
- → port fault 아님

### 6. 다른 fault reason 배제
- blackhole route: 해당 prefix로 Null0 route 없음
- static route error: 경로 자체가 부재, 잘못된 게 아님
- ARP config error: 관련 ARP 이슈 관찰 안 됨
- routing loop: 경로가 없으므로 loop 불가
- BGP/OSPF/IS-IS config error: static 기반 네트워크, dynamic 미사용
- → **missing static route** 단일 원인 확정

## v12 비교
완전 일치 — v12와 solver가 동일한 reason enum에 도달. Opus 재확인 결과도 동일.

## 제출 개선 권장
- **우선순위**: NONE (이미 정답)
- **확신도**: HIGH

## Fault 문제 일반화 관찰
Q17의 패턴이 다른 FAULT 문제에도 적용 가능:
1. src → dst IP의 forward path 구성
2. path상 각 의심 장비의 routing table에서 dst prefix 경로 존재 확인
3. 경로가 끊기는 첫 장비 = fault node
4. 경로 없음 → `missing static route`
5. Null0 route → `blackhole route`
6. 잘못된 next-hop → `static route error`
