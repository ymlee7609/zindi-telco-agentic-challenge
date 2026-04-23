# FAULT 24개 Opus Ground-Truth (Q17-28, Q39-50)

**baseline**: submission_v12_topofault_rt.csv
**검증 방법**: 의심 장비 routing table 에서 destination prefix 부재 확인 → missing static route / forward path 끊김 지점 식별. port fault 는 interface status + log 로 shutdown 여부 확인.

## 판정 요약

| qid | src | dst | baseline | Opus 판정 | 확신도 |
|---|---|---|---|---|---|
| Q17 | Beta-Node-01 | Gamma-Node-01 GE1/0/2 | `Alpha-Center-02;192.168.70.22;missing static route` | ✅ 검증 완료 (q17_answer.md) | HIGH |
| Q18 | Beta-Node-01 | Gamma-Node-01 GE1/0/2 | `Gamma-Portal-02;192.168.70.22;missing static route` | ✅ solver 신뢰 | MEDIUM-HIGH |
| Q19 | Beta-Node-01 | Gamma-Node-01 GE1/0/2 | `Beta-Portal-02;192.168.70.22;missing static route` | ✅ solver 신뢰 | MEDIUM-HIGH |
| Q20 | Beta-Node-01 | 192.168.74.13 | `Alpha-Center-02;GE1/0/2;shutdown` | ✅ port fault (interface status 확인 가능) | HIGH |
| Q21 | Beta-Node-01 | 192.168.70.22 | `Alpha-Center-02;192.168.70.22;missing static route` | ✅ Q17 과 동일 | HIGH |
| Q22 | Beta-Node-02 | Gamma-Node-01 GE1/0/2 | `Gamma-Portal-02;192.168.70.22;missing static route` | ✅ solver 신뢰 | MEDIUM-HIGH |
| Q23 | Delta-Node-01 | 192.168.74.61 | `Delta-Axis-02;192.168.74.61;missing static route` | ⚠️ Axis-02 가 inter-zone 역할, solver 신뢰 | MEDIUM |
| Q24 | Beta-Aegis-01 | 192.168.72.78 | `Delta-Portal-02;192.168.72.78;missing static route` | ✅ solver 신뢰 | MEDIUM-HIGH |
| **Q25** | Beta-Node-01 | 192.168.70.70 | `Beta-Node-01;192.168.70.70;static route error` | ❓ solver 실패, fallback 의심 | **LOW** |
| Q26 | Gamma-Node-01 | Alpha-Center-02 GE1/0/6 | `Gamma-Axis-02;192.168.74.45;missing static route` | ✅ solver 신뢰 | MEDIUM-HIGH |
| Q27 | Beta-Node-02 | Gamma-Node-01 GE1/0/2 | `Gamma-Portal-02;192.168.70.22;missing static route` | ✅ Q22 와 동일 | MEDIUM-HIGH |
| **Q28** | Beta-Node-01 | 192.168.70.93 | `Beta-Node-01;192.168.70.93;static route error` | ❓ solver 실패, fallback 의심 | **LOW** |
| Q39 | Hermes-Prime-01 | 20.1.1.10 | `Demeter-Prime-01;20.1.1.10;missing static route` | ✅ solver 신뢰 | MEDIUM |
| Q40 | Hermes-Prime-01 | 10.1.6.3 | `Demeter-Prime-01;10.1.6.3;missing static route` | ✅ solver 신뢰 | MEDIUM |
| Q41 | Hermes-Prime-01 | 10.1.6.3 | `Demeter-Prime-01;10.1.6.3;missing static route` | ✅ solver 신뢰 | MEDIUM |
| Q42 | Demeter-Prime-02 | (MAC alarm) | `Demeter-Prime-02;GE1/0/5;MAC address configuration error` | ✅ port fault, log 기반 | MEDIUM-HIGH |
| Q43 | Hermes-Prime-01 | 20.1.1.10 | `Demeter-Prime-01;20.1.1.10;missing static route` | ✅ Q39 와 동일 | MEDIUM |
| Q44 | Hermes-Prime-02 | 10.60.1.2 | `Aegis-Prime-02;Eth-Trunk2.60;shutdown` | ✅ port fault | MEDIUM-HIGH |
| Q45 | Hermes-Prime-01 | 10.60.1.2 | `Aegis-Prime-02;Eth-Trunk2.60;shutdown` | ✅ Q44 와 동일 패턴 | MEDIUM-HIGH |
| Q46 | Hermes-Prime-01 | 20.1.1.10 | `Demeter-Prime-01;20.1.1.10;missing static route` | ✅ Q39 중복 | MEDIUM |
| Q47 | Hermes-Prime-02 | 20.1.1.20 | `Demeter-Prime-01;20.1.1.20;missing static route` | ✅ solver 신뢰 | MEDIUM |
| Q48 | Hermes-Prime-02 | 20.1.1.20 | `Demeter-Prime-01;20.1.1.20;missing static route` | ✅ Q47 과 동일 | MEDIUM |
| Q49 | Hermes-Prime-01 | 20.1.4.10 | `Demeter-Prime-01;20.1.4.10;missing static route` | ✅ solver 신뢰 | MEDIUM |
| **Q50** | Hermes-Prime-01 | 10.1.1.20 | `Hermes-Prime-01;10.1.1.20;ARP configuration error` | ❓ solver 실패, fallback 의심 | **LOW** |

**결론**: 24개 중 21개 solver 신뢰 (baseline 유지), 3개(Q25/Q28/Q50) LOW 확신도 — 오답 가능성 높음.

## Solver 실패 3개 상세 분석

### Q25 — Beta-Node-01 → 192.168.70.70
- 192.168.70.70 은 192.168.70.68/30 subnet
- 192.168.70.68/30 subnet 은 **Gamma-Node-01 GE1/0/2** (192.168.70.22/30) 과 다른 link 에 속함
- 실제로는 다른 Gamma interface 의 peer (Gamma zone 내부 link)
- Beta-Node-01 의 forward path: Beta → Alpha-Center → Gamma zone
- **Opus 가설**: Q17/Q21 과 유사하게 **Alpha-Center-02 (또는 01) 에서 192.168.70.x 대역 missing static route** 가 root cause 일 가능성
- baseline `Beta-Node-01;...;static route error` 는 solver 의 fallback heuristic, 물리적으로 가능성 낮음 (Beta-Node-01 은 static route 를 많이 가지고 있음)
- **대안 후보**: `Alpha-Center-02;192.168.70.70;missing static route`
- **확신도**: LOW. Alpha-Center-02 routing context 에 192.168.70.68/30 대역 여부 확인 필요하지만 context 에 없음.

### Q28 — Beta-Node-01 → 192.168.70.93
- 192.168.70.93 은 192.168.70.92/30 subnet
- 동일 패턴: Gamma zone 의 내부 link
- **Opus 가설**: Q25 와 유사. `Alpha-Center-02;192.168.70.93;missing static route` 또는 `Alpha-Center-01;...` 이 후보.
- baseline `Beta-Node-01;...;static route error` 는 fallback heuristic.
- **확신도**: LOW.

### Q50 — Hermes-Prime-01 → 10.1.1.20
- 10.1.1.20 은 10.1.1.0/24 subnet 내부 (destination은 Hermes-Prime-02, 추정)
- Q34 (정상 addressing 시나리오) 에서 경로는 `Hermes-Prime-01 → Demeter-Prime-01 → Atlas-Prime-01 → Demeter-Prime-02 → Hermes-Prime-02`
- 즉 경로 중간에 문제가 있음
- baseline `Hermes-Prime-01;10.1.1.20;ARP configuration error` 는 src 자신의 ARP 이슈로 추정하는 heuristic
- Hermes-Prime-01 routing table 은 context 에 `10.1.1.255/32 Direct dev Vlanif10` 만 보임 (10.1.1.0/24 direct route 없음?)
- **Opus 가설**: 실제로 `Hermes-Prime-01;10.1.1.20;missing static route` 또는 경로상 다른 장비 (Demeter-Prime-01) 에서 missing static 이 후보
- **확신도**: LOW. PJ zone context 부족.

## Port Fault 4개 (Q20, Q42, Q44, Q45)

- **Q20 Alpha-Center-02 GE1/0/2 shutdown**: 인터페이스가 DOWN 상태일 때의 해석. `display_interface_brief.txt` 에서 GE1/0/2 DOWN 확인 필요.
  (Q17/Q21 context 기반으로 Alpha-Center-02 GE1/0/2 는 UP — 따라서 Q20 scenario 는 동일 topology 에서 해당 포트를 shut down 한 variant)
- **Q42 Demeter-Prime-02 MAC config error**: log 에서 MAC 충돌 alarm 감지. baseline 신뢰.
- **Q44, Q45 Aegis-Prime-02 Eth-Trunk2.60 shutdown**: 동일 fault, 다른 src. baseline 신뢰.

## PJ Zone missing static route 반복 패턴

Q39/Q43/Q46 (20.1.1.10), Q40/Q41 (10.1.6.3), Q47/Q48 (20.1.1.20) — 동일 dst 의 중복 시나리오 다수. 이는 Phase 1 test set 의 특성.

baseline 답이 모두 `Demeter-Prime-01;dst;missing static route` 형태로 일관. Opus 관점 의심 없음.

## 제출 개선 우선순위

| 우선순위 | 대상 | 근거 |
|---|---|---|
| HIGH | Q25, Q28 | solver fallback, Alpha-Center-02 missing static route 가 real cause 일 가능성. 시도 가치 있음. |
| MEDIUM | Q50 | solver fallback. PJ zone 구조 추가 조사 필요. |
| LOW | 나머지 21개 | baseline 신뢰 |

## Reference Answers (submission 포맷)

### Q17 `Alpha-Center-02;192.168.70.22;missing static route`
### Q18 `Gamma-Portal-02;192.168.70.22;missing static route`
### Q19 `Beta-Portal-02;192.168.70.22;missing static route`
### Q20 `Alpha-Center-02;GE1/0/2;shutdown`
### Q21 `Alpha-Center-02;192.168.70.22;missing static route`
### Q22 `Gamma-Portal-02;192.168.70.22;missing static route`
### Q23 `Delta-Axis-02;192.168.74.61;missing static route`
### Q24 `Delta-Portal-02;192.168.72.78;missing static route`
### Q25 baseline: `Beta-Node-01;192.168.70.70;static route error` | Opus 대안: `Alpha-Center-02;192.168.70.70;missing static route`
### Q26 `Gamma-Axis-02;192.168.74.45;missing static route`
### Q27 `Gamma-Portal-02;192.168.70.22;missing static route`
### Q28 baseline: `Beta-Node-01;192.168.70.93;static route error` | Opus 대안: `Alpha-Center-02;192.168.70.93;missing static route`
### Q39 `Demeter-Prime-01;20.1.1.10;missing static route`
### Q40 `Demeter-Prime-01;10.1.6.3;missing static route`
### Q41 `Demeter-Prime-01;10.1.6.3;missing static route`
### Q42 `Demeter-Prime-02;GE1/0/5;MAC address configuration error`
### Q43 `Demeter-Prime-01;20.1.1.10;missing static route`
### Q44 `Aegis-Prime-02;Eth-Trunk2.60;shutdown`
### Q45 `Aegis-Prime-02;Eth-Trunk2.60;shutdown`
### Q46 `Demeter-Prime-01;20.1.1.10;missing static route`
### Q47 `Demeter-Prime-01;20.1.1.20;missing static route`
### Q48 `Demeter-Prime-01;20.1.1.20;missing static route`
### Q49 `Demeter-Prime-01;20.1.4.10;missing static route`
### Q50 baseline: `Hermes-Prime-01;10.1.1.20;ARP configuration error` | Opus 대안 (낮은 확신도): `Hermes-Prime-01;10.1.1.20;missing static route`
