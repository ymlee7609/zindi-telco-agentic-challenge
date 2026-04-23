# Q11 Opus Reference Answer

**scenario_id**: 01455e30-c21f-44e0-9ca8-62af01e4e0bb
**type**: PATH (addressing trace)
**target**: Beta-Node-03 → Alpha-Center-02 GE1/0/2 (192.168.74.13)

## Opus Verdict
v12와 deterministic solver **불일치**. Routing table 증거 기반으로 **solver가 맞음**. **v12 수정 필요**.

## Reference Answer
```
Beta-Node-03->Beta-Axis-02->Beta-Portal-02->Alpha-Center-02
```

## Reasoning (증거 기반)

### 1. Destination IP 파악
Alpha-Center-02 `display_ip_interface_brief.txt`:
- **GE1/0/2 = 192.168.74.13/30**
- Subnet: 192.168.74.12/30 (pair: .13 and .14)
- Beta-Portal-02 GE1/0/7 = 192.168.74.14/30 → Beta-Portal-02가 이 L3 링크의 반대편

### 2. Beta-Node-03 routing table 추적
목적지 Alpha-Center-02는 loopback 192.168.65.2/32로 식별됨.

Beta-Node-03 entry:
```
192.168.65.2/32  Static via 192.168.65.165 dev GE1/0/2
```
- next-hop 192.168.65.165 / outgoing iface **GE1/0/2**
- Beta-Node-03 LLDP: GE1/0/2 <-> **Beta-Axis-02** GE1/0/3
- → 첫 홉 = **Beta-Axis-02**, NOT Beta-Axis-01

### 3. Beta-Axis-02 → Beta-Portal-02
LLDP: Beta-Portal-02 GE1/0/2 <-> Beta-Axis-02 GE1/0/6
Beta-Node-03 입장에서 Alpha-Center-02 방향 upstream은 Portal 쪽 → Beta-Axis-02 GE1/0/6 → **Beta-Portal-02**

### 4. Beta-Portal-02 routing table 검증
Beta-Portal-02 entry:
```
192.168.65.2/32  Static via 192.168.74.13 dev GE1/0/7
```
- next-hop 192.168.74.13 = Alpha-Center-02 GE1/0/2
- 이 경로는 destination port로 정확히 도달 ✓

### 5. 질문 힌트 재해석
"Test-Zone1-Spine02 cannot find routing information... connected to Beta-Portal-01 and Beta-Portal-02"

이 힌트는 Spine02 경유를 배제하는 것이 아니라, **있는 라우팅으로만 판단하라**는 의미.
Beta-Node-03 static route는 명시적으로 GE1/0/2 (Axis-02) 방향을 선택함.

### 6. v12 답변 오류 분석
v12 답변: `Beta-Node-03->Beta-Axis-01->Beta-Portal-01->Alpha-Center-02`

- Beta-Node-03 GE1/0/1 <-> Beta-Axis-01 (topologically 가능)
- 하지만 Beta-Node-03 routing table의 192.168.65.2/32 route는 **GE1/0/2 방향만**
- GE1/0/1 경로를 주장하려면 route 증거 필요 — 없음
- Beta-Portal-01 GE1/0/7 IP = 192.168.74.6/30 (Alpha-Center-02 GE1/0/1과 peer)
  - 만약 GE1/0/2가 아니라 GE1/0/1 destination이었다면 v12 경로가 맞았을 것
  - 즉, v12는 **dst_port (GE1/0/2)를 잘못 매핑**함

### 7. 확신도
**High** — Beta-Node-03 routing table의 static entry가 명확히 GE1/0/2 방향을 지정, topology도 일관.

## v12 비교
| 항목 | v12 | Opus Reference |
|---|---|---|
| 1st hop | Beta-Axis-01 (GE1/0/1) | **Beta-Axis-02 (GE1/0/2)** |
| 2nd hop | Beta-Portal-01 | **Beta-Portal-02** |
| last hop | Alpha-Center-02 | Alpha-Center-02 (공통) |

## 제출 개선 권장
- **우선순위**: HIGH
- **조치**: v12의 path_tracer 파이프라인이 dst_port IP를 정확히 매핑하는지 확인. `192.168.74.13`(Alpha-Center-02 GE1/0/2)이 Portal-02 peer인 사실이 반영되어야 함.
- **후보 수정**: `agent/track_b/submission/gen_v12_path.py` 또는 `path_tracer.py`의 destination IP ↔ peer port 매핑 로직 점검
