# Track B - Phase 1 문제 분석 (50문제)

## 개요

| 유형 | 문제 번호 | 개수 |
|------|----------|------|
| Topology (링크 복원) | Q1-Q6, Q29-Q33 | 11 |
| Path (경로 추적) | Q7-Q16, Q34-Q38 | 15 |
| Fault (장애 진단) | Q17-Q28, Q39-Q50 | 24 |

### 진행 상태 (v6_full + Opus overlay, 2026-04-22, **50/50 답변 완성**)

| 상태 | 개수 | 비고 |
|------|------|------|
| SOLVED (Qwen) | 47 | v6_full 에서 직접 답변 추출 |
| FORCED (Qwen) | 1 | Q11 (Path, forced_answer, 타당한 4홉) |
| Opus overlay | 2 | Q36, Q38 (PJ Path, Opus 에뮬레이션으로 best-effort 답변) |
| **총 제출 답변** | **50/50** | `submission_v6_full_v8.csv` (Zindi 제출 완료) |

> 상세: `06_progress_report.md` §4 참조. 문제별 상황/과제 설명: `03-3-1_problems_detail.md`.
> Non-solved 복구 전략: `07_not_solved_recovery_strategy.md`.

---

## Topology (링크 복원)

> 삭제된 노드의 UP 인터페이스 링크 정보를 복원

### Q1
- **영역**: Big Data Zone
- **타겟 노드**: `Gamma-Aegis-01`
- **직접 쿼리 가능**: 아니오
- **주변 노드**: `in`
- **출력 형식**: `Gamma-Aegis-01(포트)->원격노드(포트)` (라인당 1개)

**현재 답변 (v1, 미검증):**
```
Gamma-Aegis-01(GE1/0/0)->Gamma-Portal-01(GE1/0/4)
Gamma-Aegis-01(GE1/0/1)->Gamma-Portal-02(GE1/0/4)
Gamma-Aegis-01(GE1/0/2)->Gamma-Aegis-02(GE0/0/2)
```

### Q2
- **영역**: Big Data Zone
- **타겟 노드**: `Gamma-Axis-02`
- **직접 쿼리 가능**: 아니오
- **주변 노드**: `itself`
- **출력 형식**: `Gamma-Axis-02(포트)->원격노드(포트)` (라인당 1개)

**현재 답변 (v2, 미검증):**
```
Gamma-Axis-02(GE1/0/5)->Gamma-Portal-01(GE1/0/2)
Gamma-Axis-02(GE1/0/6)->Gamma-Portal-02(GE1/0/2)
Gamma-Axis-02(GE1/0/1)->Gamma-Node-01(GE1/0/2)
Gamma-Axis-02(GE1/0/2)->Gamma-Node-02(GE1/0/2)
Gamma-Axis-02(GE1/0/3)->Gamma-Node-03(GE1/0/2)
Gamma-Axis-02(GE1/0/4)->Gamma-Node-04(GE1/0/2)
```

### Q3
- **영역**: Development and Testing Zone
- **타겟 노드**: `Beta-Aegis-02`
- **직접 쿼리 가능**: 아니오
- **출력 형식**: `Beta-Aegis-02(포트)->원격노드(포트)` (라인당 1개)

**현재 답변 (v1, 미검증):**
```
Beta-Aegis-02(GE1/0/0)->Beta-Portal-01(GE1/0/5)
Beta-Aegis-02(GE1/0/1)->Beta-Portal-02(GE1/0/5)
Beta-Aegis-02(GE1/0/2)->Beta-Aegis-01(GE0/0/2)
```

### Q4
- **영역**: Development and Testing Zone
- **타겟 노드**: `Beta-Portal-02`
- **직접 쿼리 가능**: 아니오
- **출력 형식**: `Beta-Portal-02(포트)->원격노드(포트)` (라인당 1개)

**현재 답변 (v1, 미검증):**
```
Beta-Portal-02(GE1/0/1)->Beta-Axis-01(GE1/0/1)
Beta-Portal-02(GE1/0/2)->Beta-Axis-02(GE1/0/1)
Beta-Portal-02(GE1/0/3)->Beta-Portal-01(GE1/0/3)
Beta-Portal-02(GE1/0/4)->Beta-Aegis-01(GE0/0/1)
Beta-Portal-02(GE1/0/5)->Beta-Aegis-02(GE0/0/1)
Beta-Portal-02(GE1/0/6)->Alpha-Center-01(GE1/0/2)
Beta-Portal-02(GE1/0/7)->Alpha-Center-02(GE1/0/2)
```

### Q5
- **영역**: Unknown
- **타겟 노드**: `Delta-Node-01`
- **직접 쿼리 가능**: 아니오
- **출력 형식**: `Delta-Node-01(포트)->원격노드(포트)` (라인당 1개)

**현재 답변 (v1, 미검증):**
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

**정답 (수동 검증):**
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

**정답 (v8 제출본)**:
```
Demeter-Prime-01(GE1/0/0)->Atlas-Prime-01(GE1/0/2)
Demeter-Prime-01(GE1/0/1)->Atlas-Prime-02(GE1/0/2)
Demeter-Prime-01(GE1/0/5)->Hermes-Prime-01(GE1/0/4)
```

### Q30
- **영역**: PJ area
- **타겟 노드**: `Atlas-Prime-01`
- **직접 쿼리 가능**: 아니오
- **출력 형식**: `Atlas-Prime-01(포트)->원격노드(포트)` (라인당 1개)

**정답 (v8 제출본)**:
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

**정답 (v8 제출본)**:
```
Janus-Prime-01(GE1/0/0)->Atlas-Prime-01(GE1/0/0)
Janus-Prime-01(GE1/0/1)->Atlas-Prime-02(GE1/0/0)
Janus-Prime-01(GE1/0/2)->PX1(GE1/0/0)
Janus-Prime-01(GE1/0/3)->Aegis-Prime-02(GE1/0/2)
Janus-Prime-01(GE1/0/4)->Janus-Prime-02(GE1/0/4)
Janus-Prime-01(GE1/0/5)->Aegis-Prime-01(GE1/0/2)
```

### Q32
- **영역**: PJ area
- **타겟 노드**: `Aegis-Prime-01`
- **직접 쿼리 가능**: 아니오
- **출력 형식**: `Aegis-Prime-01(포트)->원격노드(포트)` (라인당 1개)

**정답 (v8 제출본)**:
```
Aegis-Prime-01(GE1/0/3)->Eon-Node-01(GE1/0/1)
Aegis-Prime-01(GE1/0/0)->Janus-Prime-02(GE1/0/5)
Aegis-Prime-01(GE1/0/1)->Aegis-Prime-02(GE1/0/1)
```

### Q33
- **영역**: PJGFA area
- **타겟 노드**: `Janus-Node-02`
- **직접 쿼리 가능**: 아니오
- **출력 형식**: `Janus-Node-02(포트)->원격노드(포트)` (라인당 1개)

**정답 (v8 제출본)**:
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

**정답 (수동 검증):**
```
Beta-Node-01->Beta-Axis-02->Beta-Portal-02->Alpha-Center-02->Gamma-Portal-02->Gamma-Axis-02->Gamma-Node-01
```

### Q8
- **영역**: Big Data Zone
- **출발지**: `Gamma-Node-01`
- **목적지 노드**: `Delta-Node-01`
- **목적지 인터페이스**: `GE1/0/2`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v8 제출본)**:
```
Gamma-Node-01->Gamma-Axis-02->Gamma-Portal-02->Alpha-Center-02->Delta-Portal-01->Delta-Axis-02->Delta-Node-01
```

### Q9
- **영역**: 
- **출발지**: `Delta-Node-03`
- **목적지 노드**: `Beta-Node-03`
- **목적지 인터페이스**: `GE1/0/2`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v8 제출본)**:
```
Beta-Node-03->Beta-Axis-02->Beta-Portal-02->Alpha-Center-01->Delta-Portal-02->Delta-Axis-02->Delta-Node-03
```

### Q10
- **영역**: 
- **출발지**: `Gamma-Node-01`
- **목적지 노드**: `Beta-Node-04`
- **목적지 인터페이스**: `GE1/0/2`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v8 제출본)**:
```
Gamma-Node-01->Gamma-Axis-02->Gamma-Portal-02->Alpha-Center-02->Beta-Portal-02->Beta-Axis-02->Beta-Node-04
```

### Q11
- **영역**: 
- **출발지**: `Beta-Node-03`
- **목적지 노드**: `Alpha-Center-02`
- **목적지 인터페이스**: `GE1/0/2`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v8 제출본)**:
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

**정답 (v8 제출본)**:
```
Beta-Node-01->Beta-Axis-02->Beta-Portal-02->Alpha-Center-02->Gamma-Portal-02->Gamma-Axis-02->Gamma-Node-01
```

### Q13
- **영역**: 
- **출발지**: `Gamma-Node-02`
- **목적지 노드**: `Beta-Node-04`
- **목적지 인터페이스**: `GE1/0/4`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v8 제출본)**:
```
Gamma-Node-02->Gamma-Axis-02->Gamma-Portal-02->Alpha-Center-02->Beta-Portal-02->Beta-Axis-02->Beta-Node-03->Beta-Node-04
```

### Q14
- **영역**: 
- **출발지**: `Delta-Node-02`
- **목적지 노드**: `Gamma-Node-02`
- **목적지 인터페이스**: `GE1/0/2`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v8 제출본)**:
```
Delta-Node-02->Delta-Axis-02->Delta-Portal-02->Alpha-Center-02->Gamma-Portal-02->Gamma-Axis-02->Gamma-Node-02
```

### Q15
- **영역**: Big Data Zone
- **출발지**: `Gamma-Node-04`
- **목적지 노드**: `Delta-Node-01`
- **목적지 인터페이스**: `GE1/0/2`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v8 제출본)**:
```
Gamma-Node-04->Gamma-Axis-02->Gamma-Portal-02->Alpha-Center-02->Delta-Portal-02->Delta-Axis-02->Delta-Node-01
```

### Q16
- **영역**: Management Zone
- **출발지**: `Delta-Node-04`
- **목적지 노드**: `Beta-Aegis-02`
- **목적지 인터페이스**: `GE1/0/2`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v8 제출본)**:
```
Beta-Aegis-02->Alpha-Center-02->Delta-Portal-02->Delta-Axis-01->Delta-Node-04
```

### Q34
- **영역**: PJ area
- **출발지**: `Hermes-Prime-01`
- **목적지 IP**: `10.1.1.20`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v8 제출본)**:
```
Hermes-Prime-01->Demeter-Prime-01->Hermes-Prime-02
```

### Q35
- **영역**: PJ area
- **출발지**: `Hermes-Prime-01`
- **목적지 IP**: `20.1.1.10`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v8 제출본)**:
```
Hermes-Prime-01->Demeter-Prime-01->Demeter-Node-01->Hermes-Node-01
```

### Q36
- **영역**: PJGFA area
- **출발지**: `Hermes-Node-01`
- **목적지 IP**: `10.1.1.10`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v8 제출본)**:
```
Hermes-Node-01->Demeter-Node-01->Atlas-Node-01->Janus-Node-01->Gaia-Node-01->Eon-Node-01->Aegis-Prime-01->Hermes-Prime-01
```

### Q37
- **영역**: PJGFA area
- **출발지**: `Hermes-Node-01`
- **목적지 IP**: `20.1.1.20`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v8 제출본)**:
```
Hermes-Node-01->Demeter-Node-01->Atlas-Node-01->Demeter-Node-02->Hermes-Node-02
```

### Q38
- **영역**: PJ area
- **출발지**: `Hermes-Prime-01`
- **목적지 IP**: `20.1.4.20`
- **출력 형식**: `NodeA->NodeB->...->NodeZ` (단일 라인)

**정답 (v8 제출본)**:
```
Hermes-Prime-01->Demeter-Prime-01->Demeter-Node-02->Hermes-Node-02
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

**정답 (수동 검증):**
```
Beta-Portal-02;GE1/0/7;shutdown
```

### Q18
- **영역**: 
- **시나리오**: Beta-Node-01 is addressing GE1/0/2 port of Gamma-Node-01, but the service is not reachable.
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Beta-Node-01;GE1/0/2;static route error
Gamma-Node-01;GE1/0/2;static route error
```

### Q19
- **영역**: 
- **시나리오**: Beta-Node-01 is addressing the GE1/0/2 port of Gamma-Node-01, but the service is not reachable.
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Beta-Node-01;192.168.70.22;missing static route
```

### Q20
- **영역**: 
- **시나리오**: Beta-Node-01 is addressing a destination IP in an external zone, which is 192.168.74.13, mask 30, service is unreachable.
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Beta-Node-01;192.168.74.13;missing static route
```

### Q21
- **영역**: 
- **시나리오**: Beta-Node-01 is addressing 192.168.70.22, mask 30, but the service is not reachable.
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Beta-Node-01;192.168.70.22;missing static route
```

### Q22
- **영역**: 
- **시나리오**: Beta-Node-02 is addressing the GE1/0/2 port of Gamma-Node-01, but the service is unreachable.
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Beta-Node-02;192.168.70.22;missing static route
```

### Q23
- **영역**: 
- **시나리오**: Delta-Node-01 is addressing an external destination IP of 192.168.74.61, mask 30, and traffic is currently interrupted.
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Delta-Node-01;192.168.74.61;missing static route
```

### Q24
- **영역**: 
- **시나리오**: Beta-Aegis-01 is addressing Delta-Aegis-02's GE0/0/1 (IP:192.168.72.78), mask 30, but the service is unreachable.
- **출발지**: `Beta-Aegis-01`
- **목적지/대상**: `Delta-Aegis-02`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Beta-Aegis-01;192.168.72.78;missing static route
```

### Q25
- **영역**: 
- **시나리오**: Beta-Node-01 is addressing 192.168.70.70, mask 30, but the service is not reachable.
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Beta-Node-01;GE1/0/0;shutdown
Beta-Node-01;GE1/0/5;shutdown
Beta-Node-01;GE1/0/6;shutdown
Beta-Node-01;GE1/0/7;shutdown
Beta-Node-01;GE1/0/8;shutdown
Beta-Node-01;GE1/0/9;shutdown
Beta-Node-01;GE1/1/0;shutdown
Beta-Node-01;GE1/1/1;shutdown
Beta-Node-01;GE1/1/2;shutdown
Beta-Node-01;GE1/1/3;shutdown
Beta-Node-01;GE1/1/4;shutdown
Beta-Node-01;GE1/1/5;shutdown
Beta-Node-01;GE1/1/6;shutdown
Beta-Node-01;GE1/1/7;shutdown
Beta-Node-01;GE1/1/8;shutdown
Beta-Node-01;GE1/1/9;shutdown
Beta-Node-01;GE2/0/0;shutdown
Beta-Node-01;GE2/0/1;shutdown
Beta-Node-01;GE2/0/2;shutdown
Beta-Node-01;GE2/0/3;shutdown
Beta-Node-01;GE2/0/4;shutdown
Beta-Node-01;GE2/0/5;shutdown
Beta-Node-01;GE2/0/6;shutdown
Beta-Node-01;GE2/0/7;shutdown
Beta-Node-01;GE2/0/8;shutdown
Beta-Node-01;GE2/0/9;shutdown
Beta-Node-01;GE2/1/0;shutdown
Beta-Node-01;GE2/1/1;shutdown
Beta-Node-01;GE2/1/2;shutdown
Beta-Node-01;GE2/1/3;shutdown
Beta-Node-01;GE2/1/4;shutdown
Beta-Node-01;GE2/1/5;shutdown
Beta-Node-01;GE2/1/6;shutdown
Beta-Node-01;GE2/1/7;shutdown
Beta-Node-01;GE2/1/8;shutdown
Beta-Node-01;GE2/1/9;shutdown
```

### Q26
- **영역**: 
- **시나리오**: Gamma-Node-01 is addressing GE1/0/6 of Alpha-Center-02, but the service is not reachable
- **출발지**: `Gamma-Node-01`
- **목적지/대상**: `Alpha-Center-02`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Gamma-Node-01;GE1/0/6;shutdown
```

### Q27
- **영역**: 
- **시나리오**: Beta-Node-02 is addressing the GE1/0/2 port of Gamma-Node-01, but the service is not reachable.
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Beta-Node-02;192.168.65.157;static route error
```

### Q28
- **영역**: 
- **시나리오**: Beta-Node-01 is addressing 192.168.70.93, mask 30, but the service is not reachable.
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Beta-Node-01;192.168.70.93;missing static route
```

### Q39
- **영역**: PJ area
- **시나리오**: PJ area, ping 20.1.1.10 from Hermes-Prime-01 is unreachable
- **출발지**: `Hermes-Prime-01`
- **목적지/대상**: `20.1.1.10`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (수동 검증):**
```
Hermes-Prime-01;20.1.1.10;missing static route
```

### Q40
- **영역**: PJ area
- **시나리오**: PJ area, ping 10.1.6.3 from Hermes-Prime-01 is unreachable
- **출발지**: `Hermes-Prime-01`
- **목적지/대상**: `10.1.6.3`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Hermes-Prime-01;10.1.6.3;missing static route
```

### Q41
- **영역**: PJ area
- **시나리오**: PJ area, ping 10.1.6.3 from Hermes-Prime-01 is unreachable
- **출발지**: `Hermes-Prime-01`
- **목적지/대상**: `10.1.6.3`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Hermes-Prime-01;10.1.6.3;missing static route
```

### Q42
- **영역**: PJ area
- **시나리오**: PJ area, a Demeter-Prime-02 received a MAC address conflict alarm
- **출발지**: `Demeter-Prime-02`
- **목적지/대상**: `MAC 충돌`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Demeter-Prime-02;GE1/1/0;shutdown
Demeter-Prime-02;GE1/1/1;shutdown
Demeter-Prime-02;GE1/1/2;shutdown
Demeter-Prime-02;GE1/1/3;shutdown
Demeter-Prime-02;GE1/1/4;shutdown
Demeter-Prime-02;GE1/1/5;shutdown
Demeter-Prime-02;GE1/1/6;shutdown
Demeter-Prime-02;GE1/1/7;shutdown
Demeter-Prime-02;GE1/1/8;shutdown
Demeter-Prime-02;GE1/1/9;shutdown
Demeter-Prime-02;GE2/0/0;shutdown
Demeter-Prime-02;GE2/0/1;shutdown
Demeter-Prime-02;GE2/0/2;shutdown
Demeter-Prime-02;GE2/0/3;shutdown
Demeter-Prime-02;GE2/0/4;shutdown
Demeter-Prime-02;GE2/0/5;shutdown
Demeter-Prime-02;GE2/0/6;shutdown
Demeter-Prime-02;GE2/0/7;shutdown
Demeter-Prime-02;GE2/0/8;shutdown
Demeter-Prime-02;GE2/0/9;shutdown
Demeter-Prime-02;GE2/1/0;shutdown
Demeter-Prime-02;GE2/1/1;shutdown
Demeter-Prime-02;GE2/1/2;shutdown
Demeter-Prime-02;GE2/1/3;shutdown
Demeter-Prime-02;GE2/1/4;shutdown
Demeter-Prime-02;GE2/1/5;shutdown
Demeter-Prime-02;GE2/1/6;shutdown
Demeter-Prime-02;GE2/1/7;shutdown
Demeter-Prime-02;GE2/1/8;shutdown
Demeter-Prime-02;GE2/1/9;shutdown
```

### Q43
- **영역**: PJ area
- **시나리오**: PJ area, ping 20.1.1.10 from Hermes-Prime-01 is unreachable
- **출발지**: `Hermes-Prime-01`
- **목적지/대상**: `20.1.1.10`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Hermes-Prime-01;20.1.1.10;missing static route
```

### Q44
- **영역**: PJ area
- **시나리오**: PJ area, Hermes-Prime-02 pings an external address and finds it unreachable, ping 10.60.1.2
- **출발지**: `Hermes-Prime-02`
- **목적지/대상**: `10.60.1.2`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Hermes-Prime-02;10.60.1.2;missing static route
```

### Q45
- **영역**: PJ area
- **시나리오**: PJ area, Hermes-Prime-01 pings an external address and finds it unreachable, ping 10.60.1.2
- **출발지**: `Hermes-Prime-01`
- **목적지/대상**: `10.60.1.2`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Hermes-Prime-01;10.60.1.2;missing static route
```

### Q46
- **영역**: PJ area
- **시나리오**: PJ area, ping 20.1.1.10 from Hermes-Prime-01 is unreachable
- **출발지**: `Hermes-Prime-01`
- **목적지/대상**: `20.1.1.10`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Hermes-Prime-01;20.1.1.10;missing static route
```

### Q47
- **영역**: PJ area
- **시나리오**: PJ area, ping 20.1.1.20 from Hermes-Prime-02 is unreachable
- **출발지**: `Hermes-Prime-02`
- **목적지/대상**: `20.1.1.20`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Hermes-Prime-02;20.1.1.20;missing static route
```

### Q48
- **영역**: PJ area
- **시나리오**: PJ area, ping 20.1.1.20 from Hermes-Prime-02 is unreachable
- **출발지**: `Hermes-Prime-02`
- **목적지/대상**: `20.1.1.20`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Hermes-Prime-02;20.1.1.20;missing static route
```

### Q49
- **영역**: PJ area
- **시나리오**: In the PJ area, pinging 20.1.4.10 from Hermes-Prime-01 is unsuccessful (no connectivity).
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Hermes-Prime-01;20.1.4.10;missing static route
```

### Q50
- **영역**: PJ area
- **시나리오**: PJ area, ping 10.1.1.20 from Hermes-Prime-01 is unreachable
- **출발지**: `Hermes-Prime-01`
- **목적지/대상**: `10.1.1.20`
- **출력 형식**: `노드;대상;원인` (라인당 1개 장애)

**정답 (v8 제출본)**:
```
Hermes-Prime-01;10.1.1.20;missing static route
```

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