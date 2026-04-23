# Deep Verification Notes (2026-04-23 2nd pass)

사용자 요청에 따라 MEDIUM/LOW 20개 raw device_outputs 파일 직접 분석. 결과를 요약하고 남은 한계를 명시한다.

## 핵심 발견 (HIGH 로 upgrade 된 항목)

### Q25 — Alpha-Center-02 static route error (BREAKTHROUGH)

**상태 변화**: LOW (Opus 가설) → **HIGH (routing table 증거 확정)**

정상 vs 변이 비교:
```
정상 (Q17 등): Alpha-Center-02 routing
  192.168.70.68/30  Static  via 192.168.74.46  dev GE1/0/6    ← Gamma-Portal-02 방향

이상 (Q25):     Alpha-Center-02 routing
  192.168.70.68/30  Static  via 192.168.74.54  dev GE1/0/3    ← Delta-Portal-01 방향
```

Gamma zone 주소를 Delta zone 으로 forward → static route error. baseline 답(`Beta-Node-01;...`)은 **장비 이름이 틀림**.

**Opus 확정**: `Alpha-Center-02;192.168.70.70;static route error`

### Q28 — Gamma-Axis-02 routing loop (BREAKTHROUGH)

**상태 변화**: LOW (Opus 가설 `missing static route`) → **HIGH (routing loop 증거 확정)**

Gamma-Axis-02 routing 비교:
```
정상 (Q17): 192.168.70.92/30  Static  via 192.168.70.46  GE1/0/4  ← Gamma-Node-04
이상 (Q28): 192.168.70.92/30  Static  via 192.168.70.14  GE1/0/6  ← Gamma-Portal-02
```

Gamma-Portal-02 routing (Q28) 은 192.168.70.92/30 을 다시 Gamma-Axis-02 로 forward:
```
Gamma-Portal-02: 192.168.70.92/30  Static  via 192.168.70.13  GE1/0/2  ← Gamma-Axis-02
```

즉 Axis-02 ↔ Portal-02 간 **routing loop** 형성.

**Opus 확정**: `Gamma-Axis-02;192.168.70.93;routing loop`

### Q50 — baseline `ARP configuration error` 확인 (Opus 이전 가설 철회)

**상태 변화**: LOW (Opus 가설 `missing static route`) → **MEDIUM-HIGH (baseline 유지)**

검증:
- 10.1.1.0/24 는 Hermes-Prime-01 (Vlanif10 10.1.1.10) ↔ Hermes-Prime-02 (Vlanif10 10.1.1.20) 간 **direct-connected L2 subnet**
- Hermes-Prime-01 ARP 테이블에 10.1.1.20 entry **부재** → L2 통신 장애
- `missing static route` 가설은 잘못됨 (direct route 존재함)

baseline `Hermes-Prime-01;10.1.1.20;ARP configuration error` 가 적절.

## 새로 발견된 의심 (LOW confidence downgrade)

### Q23 — baseline 답 부정확 가능성

- Delta-Axis-02 routing 에 192.168.74.60/30 경로 **존재** (`via 192.168.72.10 GE1/0/6`)
- 즉 baseline `Delta-Axis-02;...;missing static route` 는 "missing" 이 틀림 (경로 있음)
- Delta-Portal-01 routing 에는 관련 경로 부재 → 실제 fault node 는 Delta-Portal-01 가능성
- 완전 검증 미완 (forward path 확인 안 됨). 후속 조사 필요.

## PJ zone 검증 한계

**대상**: Q29-33 TOPO 5개, Q34-38 PATH 5개, Q39-49 FAULT 10여개

**한계 원인**:
1. `display_lldp_neighbor_brief.txt` 파일이 **거의 비어있음** (헤더만 존재)
2. `display_interface_description.txt` 도 헤더만
3. 즉 PJ zone 장비는 Huawei NE 시리즈로 추정되며 다른 명령어(`display current-configuration`, `display bgp evpn`, `display vxlan tunnel` 등)로 링크 확인 필요

**현재 전략**: PJ zone 17개는 **solver 답 (baseline) 신뢰 유지** (MEDIUM confidence).

**완전 검증 필요 작업** (향후):
- `display_current-configuration.txt` 파싱으로 interface peer 추론
- VXLAN tunnel 설정 분석
- BGP EVPN neighbor 테이블 확인
- prepare_context.py 에 PJ zone 전용 parser 추가

## 최종 확신도 분포

| confidence | 수 | 의미 |
|---|---|---|
| HIGH | 20 | routing table / LLDP 직접 증거 |
| MEDIUM-HIGH | 13 | 대칭성 / 간접 증거 |
| MEDIUM | 16 | solver 답 수용 (독립 검증 부족) |
| LOW | 1 (Q23) | baseline 답 의심, 완전 검증 미완 |

## Opus vs baseline 최종 불일치 (2건)

| qid | baseline | Opus | 확신도 |
|---|---|---|---|
| Q25 | Beta-Node-01;192.168.70.70;static route error | **Alpha-Center-02;192.168.70.70;static route error** | HIGH |
| Q28 | Beta-Node-01;192.168.70.93;static route error | **Gamma-Axis-02;192.168.70.93;routing loop** | HIGH |

## 다음 단계 권고

1. **submission 018**: Q25, Q28 두 건을 Opus 확정 답으로 교체 → Zindi 제출. 최대 +0.04 (50문제 중 2문제)
2. **Q23 심층**: Delta zone forward path 완전 trace 로 fault 장비 확정
3. **PJ zone parser 확장**: prepare_context.py 개선 후 재분석

## 정직한 완성도

- 사용자 요청한 "진짜 ground truth 50/50 HIGH" 는 **달성 못 함**
- 실제 달성: HIGH 20, MEDIUM-HIGH 13, MEDIUM 16, LOW 1
- 핵심 돌파구 2건(Q25, Q28)은 점수 개선 가치 확정
- PJ zone 17개는 raw 파일 구조 한계로 추가 작업 필요
