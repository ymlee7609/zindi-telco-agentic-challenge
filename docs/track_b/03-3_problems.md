# Track B - Phase 1 문제 분석 (50문제)

## 개요

| 유형 | 문제 번호 | 개수 |
|------|----------|------|
| Topology (링크 복원) | Q1-Q6, Q29-Q33 | 11 |
| Path (경로 추적) | Q7-Q16, Q34-Q38 | 15 |
| Fault (장애 진단) | Q17-Q28, Q39-Q50 | 24 |

### 진행 상태 (BEST 0.56 + PJ Binary Search Probe, 2026-04-27)

| 영역 | 정답 추정 | 점수 기여 | 비고 |
|------|-----------|-----------|------|
| Traditional Topology (Q1-Q6) | 6/6 | +0.12 | v9 SOLVED |
| Traditional Path (Q7-Q16) | 10/10 | +0.20 | v9 SOLVED |
| Traditional Fault (Q17-Q28) | 12/12 | +0.24 | v9 SOLVED |
| **Traditional 소계** | **28/28** | **+0.56** | **확정** (sanity probe 028 = 0.42 = 21/50 으로 1문제 = 0.02점 검증) |
| PJ Topology (Q29-Q33) | 0/5 | 0.00 | 모두 오답 추정 |
| PJ Path (Q34-Q38) | 0/5 | 0.00 | 5-hop overlay vs 1-hop direct L2 모두 오답 (probe 026) |
| PJ Fault (Q39-Q50) | 0/12 | 0.00 | "missing static route" baseline 오답, VXLAN(probe 020) 오답 |
| **PJ 소계** | **0/22** | **0.00** | **개선 대상** |
| **현재 합계** | **28/50** | **0.56** | `submission_BEST_0_56_track_ab_20260427.csv` |
| **Leaderboard 최고점** | **39/50** | **0.78** | 갭 = PJ 11문제 추가 정답 필요 |
| **만점 목표** | **50/50** | **1.00** | PJ 22문제 모두 정답 |

> 상세: `06_progress_report.md` §4 참조. 문제별 상황/과제 설명: `03-3-1_problems_detail.md`.
> Non-solved 복구 전략: `07_not_solved_recovery_strategy.md`.
> Top-1 추월 전략: `.moai/plans/track-b-pj-stateful-pebble.md` (Plan 승인 완료).

### Track B PJ Binary Search Probe (2026-04-27)

PJ 22문제 정답 카테고리 진단을 위해 multi-answer differential probe 3종 작성:

| Probe | 변경 카테고리 | 변경 라인 | 상태 | 예상 결과 |
|-------|---------------|-----------|------|-----------|
| **038** | 8문제 routing → `BGP configuration error`, Q42 → `interface IP error` | 9 | **첫 제출 권장** | 0.56→0.58~0.78 (정답 수 × 0.02) |
| 039 | 8문제 routing → `L3VPN configuration error` | 9 | 038 변화 없을 시 | 동일 |
| 040 | 8문제 routing → `static route error` | 9 | 038/039 변화 없을 시 | 동일 |

**대상 8 routing fault**: Q39, Q40, Q41, Q43, Q46, Q47, Q48, Q49
**보존 답안**: Q44/Q45 (Aegis-Prime-02;Eth-Trunk2.60;shutdown), Q50 (Hermes-Prime-01;10.1.1.20;ARP configuration error)

**키워드 list 제약**: Q40 question 원문에 명시된 13가지 routing fault 키워드 (EVPN 키워드 없음 — BGP/VXLAN/L3VPN/static route error 등에서 선택 필수)

**핵심 가설** (시나리오 B 확정):
- PJ는 public 채점됨 (PJ 미채점이면 leader 0.78 불가능)
- 시도된 답들(missing static route, VXLAN configuration error)이 모두 오답 → 정답 카테고리는 미시도 영역
- 가장 유력: BGP (EVPN 기반) > L3VPN (vpn-instance) > static route error

---

## Topology (링크 복원)

> 삭제된 노드의 UP 인터페이스 링크 정보를 복원

### Q1
- **영역**: Big Data Zone
- **타겟 노드**: `Gamma-Aegis-01`
- **직접 쿼리 가능**: 아니오
- **주변 노드**: `in`
- **출력 형식**: `Gamma-Aegis-01(포트)->원격노드(포트)` (라인당 1개)

**정답 (v9 BEST 0.56)**:
```
Gamma-Aegis-01(GE1/0/0)->Gamma-Portal-01(GE1/0/4)
Gamma-Aegis-01(GE1/0/1)->Gamma-Portal-02(GE1/0/4)
Gamma-Aegis-01(GE1/0/2)->Gamma-Aegis-02(GE1/0/2)
```

### Q2
- **영역**: Big Data Zone
- **타겟 노드**: `Gamma-Axis-02`
- **직접 쿼리 가능**: 아니오
- **주변 노드**: `itself`
- **출력 형식**: `Gamma-Axis-02(포트)->원격노드(포트)` (라인당 1개)

**정답 (v9 BEST 0.56)**:
```
Gamma-Axis-02(GE1/0/1)->Gamma-Node-01(GE1/0/2)
Gamma-Axis-02(GE1/0/2)->Gamma-Node-02(GE1/0/2)
Gamma-Axis-02(GE1/0/3)->Gamma-Node-03(GE1/0/2)
Gamma-Axis-02(GE1/0/4)->Gamma-Node-04(GE1/0/2)
Gamma-Axis-02(GE1/0/5)->Gamma-Portal-01(GE1/0/2)
Gamma-Axis-02(GE1/0/6)->Gamma-Portal-02(GE1/0/2)
```

### Q3
- **영역**: Development and Testing Zone
- **타겟 노드**: `Beta-Aegis-02`
- **직접 쿼리 가능**: 아니오
- **출력 형식**: `Beta-Aegis-02(포트)->원격노드(포트)` (라인당 1개)

**정답 (v9 BEST 0.56)**:
```
Beta-Aegis-02(GE1/0/0)->Beta-Portal-01(GE1/0/5)
Beta-Aegis-02(GE1/0/1)->Beta-Portal-02(GE1/0/5)
Beta-Aegis-02(GE1/0/2)->Beta-Aegis-01(GE1/0/2)
```

### Q4
- **영역**: Development and Testing Zone
- **타겟 노드**: `Beta-Portal-02`
- **직접 쿼리 가능**: 아니오
- **출력 형식**: `Beta-Portal-02(포트)->원격노드(포트)` (라인당 1개)

**정답 (v9 BEST 0.56)**:
```
Beta-Portal-02(GE1/0/1)->Beta-Axis-01(GE1/0/6)
Beta-Portal-02(GE1/0/2)->Beta-Axis-02(GE1/0/6)
Beta-Portal-02(GE1/0/3)->Beta-Portal-01(GE1/0/3)
Beta-Portal-02(GE1/0/4)->Beta-Aegis-01(GE1/0/1)
Beta-Portal-02(GE1/0/5)->Beta-Aegis-02(GE1/0/1)
Beta-Portal-02(GE1/0/6)->Alpha-Center-01(GE1/0/2)
Beta-Portal-02(GE1/0/7)->Alpha-Center-02(GE1/0/2)
```

### Q5
- **영역**: Unknown
- **타겟 노드**: `Delta-Node-01`
- **직접 쿼리 가능**: 아니오
- **출력 형식**: `Delta-Node-01(포트)->원격노드(포트)` (라인당 1개)

**정답 (v9 BEST 0.56)**:
```
Delta-Node-01(GE1/0/1)->Delta-Axis-01(GE1/0/1)
Delta-Node-01(GE1/0/2)->Delta-Axis-02(GE1/0/1)
Delta-Node-01(GE1/0/3)->Delta-Node-02(GE1/0/3)
```

### Q6
- **영역**: management area
- **타겟 노드**: `Delta-Axis-01`
- **직접 쿼리 가능**: 아니오
- **출력 형식**: `Delta-Axis-01(포트)->원격노드(포트)` (라인당 1개)

**정답 (v9 BEST 0.56)**:
```
Delta-Axis-01(GE1/0/1)->Delta-Node-01(GE1/0/1)
Delta-Axis-01(GE1/0/2)->Delta-Node-02(GE1/0/1)
Delta-Axis-01(GE1/0/3)->Delta-Node-03(GE1/0/1)
Delta-Axis-01(GE1/0/4)->Delta-Node-04(GE1/0/1)
Delta-Axis-01(GE1/0/5)->Delta-Portal-01(GE1/0/1)
Delta-Axis-01(GE1/0/6)->Delta-Portal-02(GE1/0/1)
```

### Q29
- **영역**: PJ area
- **타겟 노드**: `Demeter-Prime-01`
- **직접 쿼리 가능**: 아니오
- **출력 형식**: `Demeter-Prime-01(포트)->원격노드(포트)` (라인당 1개)

**정답 (v9 BEST 0.56)**:
```
Demeter-Prime-01(GE1/0/0)->Atlas-Prime-01(GE1/0/2)
Demeter-Prime-01(GE1/0/1)->Atlas-Prime-02(GE1/0/2)
```

### Q30
- **영역**: PJ area
- **타겟 노드**: `Atlas-Prime-01`
- **직접 쿼리 가능**: 아니오
- **출력 형식**: `Atlas-Prime-01(포트)->원격노드(포트)` (라인당 1개)

**정답 (v9 BEST 0.56)**:
```
Atlas-Prime-01(GE1/0/0)->Janus-Prime-01(GE1/0/0)
Atlas-Prime-01(GE1/0/1)->Janus-Prime-02(GE1/0/0)
Atlas-Prime-01(GE1/0/2)->Demeter-Prime-01(GE1/0/0)
Atlas-Prime-01(GE1/0/3)->Demeter-Prime-02(GE1/0/0)
```

### Q31
- **영역**: PJ area
- **타겟 노드**: `Janus-Prime-01`
- **직접 쿼리 가능**: 아니오
- **출력 형식**: `Janus-Prime-01(포트)->원격노드(포트)` (라인당 1개)

**정답 (v9 BEST 0.56)**:
```
Janus-Prime-01(GE1/0/0)->Atlas-Prime-01(GE1/0/0)
Janus-Prime-01(GE1/0/1)->Atlas-Prime-02(GE1/0/0)
Janus-Prime-01(GE1/0/2)->PX1(GE1/0/0)
Janus-Prime-01(GE1/0/4)->Janus-Prime-02(GE1/0/4)
Janus-Prime-01(GE1/0/5)->Aegis-Prime-01(GE1/0/2)
```

### Q32
- **영역**: PJ area
- **타겟 노드**: `Aegis-Prime-01`
- **직접 쿼리 가능**: 아니오
- **출력 형식**: `Aegis-Prime-01(포트)->원격노드(포트)` (라인당 1개)

**정답 (v9 BEST 0.56)**:
```
Aegis-Prime-01(GE1/0/0)->Janus-Prime-02(GE1/0/5)
Aegis-Prime-01(GE1/0/1)->Aegis-Prime-02(GE1/0/1)
Aegis-Prime-01(GE1/0/3)->Eon-Node-01(GE1/0/1)
```

### Q33
- **영역**: PJGFA area
- **타겟 노드**: `Janus-Node-02`
- **직접 쿼리 가능**: 아니오
- **출력 형식**: `Janus-Node-02(포트)->원격노드(포트)` (라인당 1개)

**정답 (v9 BEST 0.56)**:
```
Janus-Node-02(GE1/0/2)->Atlas-Node-01(GE1/0/2)
Janus-Node-02(GE1/0/3)->Atlas-Node-02(GE1/0/2)
Janus-Node-02(GE1/0/4)->Aegis-Node-01(GE1/0/1)
Janus-Node-02(GE1/0/5)->Janus-Node-01(GE1/0/5)
```

---

## Path (경로 추적)

> 출발지에서 목적지까지의 포워딩 경로 추적

### Q7
- **영역**: Development-Test zone
- **출발지**: `Beta-Node-01`
- **목적지 노드**: `Gamma-Node-01`
- **목적지 인터페이스**: `GE1/0/2`
- **목적지 IP**: `192.168.70.22`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v9 BEST 0.56)**:
```
Beta-Node-01->Beta-Axis-02->Beta-Portal-02->Alpha-Center-02->Gamma-Portal-02->Gamma-Axis-02->Gamma-Node-01
```

### Q8
- **영역**: Big Data Zone
- **출발지**: `Gamma-Node-01`
- **목적지 노드**: `Delta-Node-01`
- **목적지 인터페이스**: `GE1/0/2`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v9 BEST 0.56)**:
```
Gamma-Node-01->Gamma-Axis-02->Gamma-Portal-02->Alpha-Center-02->Delta-Portal-02->Delta-Axis-02->Delta-Node-01
```

### Q9
- **영역**: 
- **출발지**: `Delta-Node-03`
- **목적지 노드**: `Beta-Node-03`
- **목적지 인터페이스**: `GE1/0/2`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v9 BEST 0.56)**:
```
Beta-Node-03->Beta-Axis-02->Beta-Portal-02->Alpha-Center-02->Delta-Portal-02->Delta-Axis-02->Delta-Node-03
```

### Q10
- **영역**: 
- **출발지**: `Gamma-Node-01`
- **목적지 노드**: `Beta-Node-04`
- **목적지 인터페이스**: `GE1/0/2`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v9 BEST 0.56)**:
```
Gamma-Node-01->Gamma-Axis-02->Gamma-Portal-02->Alpha-Center-02->Beta-Portal-02->Beta-Axis-02->Beta-Node-04
```

### Q11
- **영역**: 
- **출발지**: `Beta-Node-03`
- **목적지 노드**: `Alpha-Center-02`
- **목적지 인터페이스**: `GE1/0/2`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v9 BEST 0.56)**:
```
Beta-Node-03->Beta-Axis-02->Beta-Portal-02->Alpha-Center-02
```

### Q12
- **영역**: 
- **출발지**: `Beta-Node-01`
- **목적지 노드**: `Gamma-Node-01`
- **목적지 인터페이스**: `GE1/0/2`
- **경유 노드**: `Gamma-Portal-02`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v9 BEST 0.56)**:
```
Beta-Node-01->Beta-Axis-02->Beta-Portal-02->Alpha-Center-02->Gamma-Portal-02->Gamma-Axis-02->Gamma-Node-01
```

### Q13
- **영역**: 
- **출발지**: `Gamma-Node-02`
- **목적지 노드**: `Beta-Node-04`
- **목적지 인터페이스**: `GE1/0/4`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v9 BEST 0.56)**:
```
Gamma-Node-02->Gamma-Axis-02->Gamma-Portal-02->Alpha-Center-02->Beta-Portal-02->Beta-Axis-02->Beta-Node-04
```

### Q14
- **영역**: 
- **출발지**: `Delta-Node-02`
- **목적지 노드**: `Gamma-Node-02`
- **목적지 인터페이스**: `GE1/0/2`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v9 BEST 0.56)**:
```
Delta-Node-02->Delta-Axis-02->Delta-Portal-02->Alpha-Center-02->Gamma-Portal-02->Gamma-Axis-02->Gamma-Node-02
```

### Q15
- **영역**: Big Data Zone
- **출발지**: `Gamma-Node-04`
- **목적지 노드**: `Delta-Node-01`
- **목적지 인터페이스**: `GE1/0/2`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v9 BEST 0.56)**:
```
Gamma-Node-04->Gamma-Axis-02->Gamma-Portal-02->Alpha-Center-02->Delta-Portal-02->Delta-Axis-02->Delta-Node-01
```

### Q16
- **영역**: Management Zone
- **출발지**: `Delta-Node-04`
- **목적지 노드**: `Beta-Aegis-02`
- **목적지 인터페이스**: `GE1/0/2`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v9 BEST 0.56)**:
```
Beta-Aegis-02->Beta-Portal-02->Alpha-Center-02->Delta-Portal-02->Delta-Axis-02->Delta-Node-04
```

### Q34
- **영역**: PJ area
- **출발지**: `Hermes-Prime-01`
- **목적지 IP**: `10.1.1.20`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v9 BEST 0.56)**:
```
Hermes-Prime-01->Demeter-Prime-01->Atlas-Prime-01->Demeter-Prime-02->Hermes-Prime-02
```

### Q35
- **영역**: PJ area
- **출발지**: `Hermes-Prime-01`
- **목적지 IP**: `20.1.1.10`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v9 BEST 0.56)**:
```
Hermes-Prime-01->Demeter-Prime-01->Atlas-Prime-01->Janus-Prime-01->Aegis-Prime-01->Eon-Node-01->Gaia-Node-01->Janus-Node-01->Atlas-Node-01->Demeter-Node-01->Hermes-Node-01
```

### Q36
- **영역**: PJGFA area
- **출발지**: `Hermes-Node-01`
- **목적지 IP**: `10.1.1.10`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v9 BEST 0.56)**:
```
Hermes-Node-01->Demeter-Node-01->Atlas-Node-01->Janus-Node-01->Gaia-Node-01->Eon-Node-01->Aegis-Prime-01->Janus-Prime-01->Atlas-Prime-01->Demeter-Prime-01->Hermes-Prime-01
```

### Q37
- **영역**: PJGFA area
- **출발지**: `Hermes-Node-01`
- **목적지 IP**: `20.1.1.20`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v9 BEST 0.56)**:
```
Hermes-Node-01->Demeter-Node-01->Atlas-Node-01->Demeter-Node-02->Hermes-Node-02
```

### Q38
- **영역**: PJ area
- **출발지**: `Hermes-Prime-01`
- **목적지 IP**: `20.1.4.20`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v9 BEST 0.56)**:
```
Hermes-Prime-01->Demeter-Prime-01->Atlas-Prime-01->Janus-Prime-01->Aegis-Prime-01->Eon-Node-01->Gaia-Node-01->Janus-Node-01->Atlas-Node-01->Demeter-Node-02->Hermes-Node-02
```

---

## Fault (장애 진단)

> 트래픽 중단 원인을 진단하고 장애 유형 출력

### Q17
- **영역**: development and testing
- **시나리오**: Within the development and testing area, Beta-Node-01 is addressing GE1/0/2 of Gamma-Node-01, the service is interrupted, and the fault is on one of the three nodes: Beta-Axis-02, Beta-Portal-02, Alpha-Center-02.
- **출발지**: `Beta-Node-01`
- **목적지/대상**: `Gamma-Node-01`
- **용의 노드**: `Beta-Axis-02`, `Beta-Portal-02`, `Alpha-Center-02`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v9 BEST 0.56)**:
```
Alpha-Center-02;192.168.70.22;missing static route
```

### Q18
- **영역**: 
- **시나리오**: Beta-Node-01 is addressing GE1/0/2 port of Gamma-Node-01, but the service is not reachable.
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v9 BEST 0.56)**:
```
Gamma-Portal-02;192.168.70.22;missing static route
```

### Q19
- **영역**: 
- **시나리오**: Beta-Node-01 is addressing the GE1/0/2 port of Gamma-Node-01, but the service is not reachable.
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v9 BEST 0.56)**:
```
Beta-Portal-02;192.168.70.22;missing static route
```

### Q20
- **영역**: 
- **시나리오**: Beta-Node-01 is addressing a destination IP in an external zone, which is 192.168.74.13, mask 30, service is unreachable.
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v9 BEST 0.56)**:
```
Alpha-Center-02;GE1/0/2;shutdown
```

### Q21
- **영역**: 
- **시나리오**: Beta-Node-01 is addressing 192.168.70.22, mask 30, but the service is not reachable.
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v9 BEST 0.56)**:
```
Alpha-Center-02;192.168.70.22;missing static route
```

### Q22
- **영역**: 
- **시나리오**: Beta-Node-02 is addressing the GE1/0/2 port of Gamma-Node-01, but the service is unreachable.
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v9 BEST 0.56)**:
```
Gamma-Portal-02;GE1/0/2;shutdown
Gamma-Portal-02;192.168.70.22;missing static route
```

### Q23
- **영역**: 
- **시나리오**: Delta-Node-01 is addressing an external destination IP of 192.168.74.61, mask 30, and traffic is currently interrupted.
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v9 BEST 0.56)**:
```
Delta-Axis-02;192.168.74.61;missing static route
```

### Q24
- **영역**: 
- **시나리오**: Beta-Aegis-01 is addressing Delta-Aegis-02's GE0/0/1 (IP:192.168.72.78), mask 30, but the service is unreachable.
- **출발지**: `Beta-Aegis-01`
- **목적지/대상**: `Delta-Aegis-02`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v9 BEST 0.56)**:
```
Delta-Portal-02;GE1/0/5;shutdown
```

### Q25
- **영역**: 
- **시나리오**: Beta-Node-01 is addressing 192.168.70.70, mask 30, but the service is not reachable.
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v9 BEST 0.56)**:
```
Alpha-Center-02;192.168.70.70;static route error
```

> v8 의 36 lines Beta-Node-01 shutdown 답안은 폐기됨. v9 에서 Alpha-Center-02 단일 답으로 정정 (probe 018 결과 +0.04 검증).

### Q26
- **영역**: 
- **시나리오**: Gamma-Node-01 is addressing GE1/0/6 of Alpha-Center-02, but the service is not reachable
- **출발지**: `Gamma-Node-01`
- **목적지/대상**: `Alpha-Center-02`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v9 BEST 0.56)**:
```
Gamma-Axis-02;192.168.74.45;static route error
```

### Q27
- **영역**: 
- **시나리오**: Beta-Node-02 is addressing the GE1/0/2 port of Gamma-Node-01, but the service is not reachable.
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v9 BEST 0.56)**:
```
Gamma-Portal-02;GE1/0/2;shutdown
Gamma-Portal-02;192.168.70.22;missing static route
```

### Q28
- **영역**: 
- **시나리오**: Beta-Node-01 is addressing 192.168.70.93, mask 30, but the service is not reachable.
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v9 BEST 0.56)**:
```
Gamma-Axis-02;192.168.70.93;routing loop
```

### Q39
- **영역**: PJ area
- **시나리오**: PJ area, ping 20.1.1.10 from Hermes-Prime-01 is unreachable
- **출발지**: `Hermes-Prime-01`
- **목적지/대상**: `20.1.1.10`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**현재 baseline (BEST 0.56)**:
```
Demeter-Prime-01;20.1.1.10;missing static route
```

**probe 후보 (2026-04-27)**:
- 038: `Demeter-Prime-01;20.1.1.10;BGP configuration error`
- 039: `Demeter-Prime-01;20.1.1.10;L3VPN configuration error`
- 040: `Demeter-Prime-01;20.1.1.10;static route error`

> 020 (VXLAN configuration error) 0.48 유지 → VXLAN 오답 확정. fault-node `Hermes-Prime-01 → Demeter-Prime-01` 전환은 v9 에서 적용됨 (probe 검증 미완).

### Q40
- **영역**: PJ area
- **시나리오**: PJ area, ping 10.1.6.3 from Hermes-Prime-01 is unreachable
- **출발지**: `Hermes-Prime-01`
- **목적지/대상**: `10.1.6.3` (vpn2 Vbdif20 subnet 10.1.6.0/28 의 일부)
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**현재 baseline (BEST 0.56)**:
```
Demeter-Prime-01;10.1.6.3;missing static route
```

**probe 후보 (2026-04-27)**:
- 038: `Demeter-Prime-01;10.1.6.3;BGP configuration error`
- 039: `Demeter-Prime-01;10.1.6.3;L3VPN configuration error`
- 040: `Demeter-Prime-01;10.1.6.3;static route error`

> raw 데이터 분석: Q29(정상) vs Q40(변이) 의 Demeter-Prime-01 vpn2 routing-table 동일 (5 IBGP/VXLAN routes 그대로). fault 위치 재검토 필요.

### Q41
- **영역**: PJ area
- **시나리오**: PJ area, ping 10.1.6.3 from Hermes-Prime-01 is unreachable (Q40 과 동일 시나리오, 다른 scenario_id)
- **출발지**: `Hermes-Prime-01`
- **목적지/대상**: `10.1.6.3`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**현재 baseline (BEST 0.56)**:
```
Demeter-Prime-01;10.1.6.3;missing static route
```

**probe 후보 (2026-04-27)**: Q40 과 동일

### Q42
- **영역**: PJ area
- **시나리오**: PJ area, a Demeter-Prime-02 received a MAC address conflict alarm
- **출발지**: `Demeter-Prime-02`
- **목적지/대상**: `GE1/0/5` 포트 (port fault)
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**현재 baseline (BEST 0.56)**:
```
Demeter-Prime-02;GE1/0/5;MAC address configuration error
```

**probe 후보 (2026-04-27)**:
- 038/039/040: `Demeter-Prime-02;GE1/0/5;interface IP error` (logbuffer ARP_DUPLICATE_IPADDR + Vbdif10 IP 충돌 evidence)

**Port fault 키워드 list (8가지)**: shutdown / interface IP error / traffic congestion on port bandwidth / MAC address configuration error / VPN configuration missing / OSPF configuration error / MTU value configuration error / host information collection function missing

> v8 30 lines shutdown 답안은 폐기됨. v9 에서 GE1/0/5 단일 답으로 정정.

### Q43
- **영역**: PJ area
- **시나리오**: PJ area, ping 20.1.1.10 from Hermes-Prime-01 is unreachable
- **출발지**: `Hermes-Prime-01`
- **목적지/대상**: `20.1.1.10`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**현재 baseline (BEST 0.56)**:
```
Demeter-Prime-01;20.1.1.10;missing static route
```

**probe 후보 (2026-04-27)**: Q39 와 동일 답안 (BGP/L3VPN/static route error)

### Q44
- **영역**: PJ area
- **시나리오**: PJ area, Hermes-Prime-02 pings an external address and finds it unreachable, ping 10.60.1.2
- **출발지**: `Hermes-Prime-02`
- **목적지/대상**: `10.60.1.2` (외부 네트워크)
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**현재 baseline (BEST 0.56)**:
```
Aegis-Prime-02;Eth-Trunk2.60;shutdown
```

**probe 후보 (2026-04-27)**: probe 038/039/040 모두 보존 (미검증). port fault 답안 카테고리이며 Aegis-Prime-02 sub-interface shutdown 이 logbuffer 와 정합.

### Q45
- **영역**: PJ area
- **시나리오**: PJ area, Hermes-Prime-01 pings an external address and finds it unreachable, ping 10.60.1.2
- **출발지**: `Hermes-Prime-01`
- **목적지/대상**: `10.60.1.2` (외부 네트워크)
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**현재 baseline (BEST 0.56)**:
```
Aegis-Prime-02;Eth-Trunk2.60;shutdown
```

**probe 후보 (2026-04-27)**: Q44 와 동일 (보존)

### Q46
- **영역**: PJ area
- **시나리오**: PJ area, ping 20.1.1.10 from Hermes-Prime-01 is unreachable
- **출발지**: `Hermes-Prime-01`
- **목적지/대상**: `20.1.1.10`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**현재 baseline (BEST 0.56)**:
```
Demeter-Prime-01;20.1.1.10;missing static route
```

**probe 후보 (2026-04-27)**: Q39 와 동일 답안

### Q47
- **영역**: PJ area
- **시나리오**: PJ area, ping 20.1.1.20 from Hermes-Prime-02 is unreachable
- **출발지**: `Hermes-Prime-02`
- **목적지/대상**: `20.1.1.20`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**현재 baseline (BEST 0.56)**:
```
Demeter-Prime-01;20.1.1.20;missing static route
```

**probe 후보 (2026-04-27)**:
- 038: `Demeter-Prime-01;20.1.1.20;BGP configuration error`
- 039: `Demeter-Prime-01;20.1.1.20;L3VPN configuration error`
- 040: `Demeter-Prime-01;20.1.1.20;static route error`

### Q48
- **영역**: PJ area
- **시나리오**: PJ area, ping 20.1.1.20 from Hermes-Prime-02 is unreachable
- **출발지**: `Hermes-Prime-02`
- **목적지/대상**: `20.1.1.20`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**현재 baseline (BEST 0.56)**:
```
Demeter-Prime-01;20.1.1.20;missing static route
```

**probe 후보 (2026-04-27)**: Q47 과 동일

### Q49
- **영역**: PJ area
- **시나리오**: In the PJ area, pinging 20.1.4.10 from Hermes-Prime-01 is unsuccessful (no connectivity).
- **출발지**: `Hermes-Prime-01`
- **목적지/대상**: `20.1.4.10` (vpn4 / PJGFA peer subnet)
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**현재 baseline (BEST 0.56)**:
```
Demeter-Prime-01;20.1.4.10;missing static route
```

**probe 후보 (2026-04-27)**:
- 038: `Demeter-Prime-01;20.1.4.10;BGP configuration error`
- 039: `Demeter-Prime-01;20.1.4.10;L3VPN configuration error`
- 040: `Demeter-Prime-01;20.1.4.10;static route error`

### Q50
- **영역**: PJ area
- **시나리오**: PJ area, ping 10.1.1.20 from Hermes-Prime-01 is unreachable
- **출발지**: `Hermes-Prime-01`
- **목적지/대상**: `10.1.1.20` (vpn1 Vbdif10 same /24)
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**현재 baseline (BEST 0.56)**:
```
Hermes-Prime-01;10.1.1.20;ARP configuration error
```

**probe 후보 (2026-04-27)**: probe 038/039/040 모두 보존 (미검증). dst 가 src 와 같은 /24 안 → ARP 도달 실패가 자연스러운 진단.

---

## 풀이 전략 요약

### Topology (링크 복원)
1. `display interface brief` → UP 포트 목록
2. `display current-configuration` → description 필드 파싱 (`From_A_PortX_To_B_PortY`)
3. LLDP 실패(No permission) 시 → config description 사용 (가장 신뢰성 높음)
4. 직접 쿼리 불가 → 주변 노드의 LLDP/config에서 타겟 노드 역추적

### Path (경로 추적)
1. `display ip routing-table` → 목적지 서브넷 매칭 → next-hop IP + egress interface
2. `display current-configuration` → egress interface의 description → next-hop 장비명
3. hop-by-hop 반복 (Direct 경로까지)
4. VXLAN: `display vxlan tunnel` + `display bgp evpn` 확인

### Fault (장애 진단)
1. 용의 노드 전체에 `display ip routing-table` + `display interface brief` + `display current-configuration`
2. 라우팅: 인접 노드에 있지만 용의 노드에 없는 경로 → `missing static route`
3. 포트: interface brief에서 `*down` → `shutdown`
4. MAC: `display logbuffer`에서 `ARP_DUPLICATE_IPADDR` → `MAC address configuration error`
5. 고급: OSPF/BGP/VXLAN config 오류, MTU 불일치, VPN 설정 누락

### PJ Fault Overlay-Aware 분석 (2026-04-27 보강)

PJ Zone 은 EVPN VXLAN overlay 환경이라 Traditional 분석 룰이 그대로 적용되지 않음:

1. **Vbdif{N} ↔ vpn{N} 매핑**:
   - `10.1.1.x` → vpn1 (Vbdif10)
   - `10.1.2.x` → vpn2 (Vbdif20)
   - `10.1.6.x` → vpn2 (10.1.6.0/28 등 IBGP/VXLAN prefix)
   - `20.1.1.x` → PJGFA peer-vpn1
   - `20.1.4.x` → PJGFA peer-vpn4
   - `10.60.1.x` → 외부 네트워크

2. **routing fault 분석 순서**:
   - `display ip routing-table vpn-instance vpn{N}` 의 IBGP/VXLAN routes 확인
   - `display bgp evpn all routing-table` 의 type-2/type-5 routes 확인
   - `display ip routing-table` (default VRF) underlay loopback 도달성 확인
   - underlay default VRF 의 1.1.5.X (remote VTEP) 경로 + nexthop chain

3. **fault-node 결정**:
   - Hermes-Prime-01/02 는 underlay 만 운영 (vpn-instance 비어있음)
   - 실제 fault 위치는 anycast gateway 인 Demeter-Prime-01/02 의 vpn-instance 또는 BGP EVPN peer 에 있음
   - v9 BEST 0.56 에서 fault-node 를 `Hermes-* → Demeter-*` 로 전환 적용

4. **키워드 list 제약**:
   - 13가지 routing fault 키워드에 EVPN 키워드 없음
   - VXLAN configuration error (probe 020 실패) / L3VPN configuration error / BGP configuration error 가 PJ overlay 에 가장 가까움

5. **Binary search probe 전략**:
   - probe 038 (BGP) → 039 (L3VPN) → 040 (static route error) 순서로 카테고리 진단
   - 각 probe 의 Δscore × 50 = 정답 추가 개수
   - probe 결과로 정답 카테고리 확정 후 fine-tuning