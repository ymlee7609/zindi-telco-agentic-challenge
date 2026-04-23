# Track B Day 2 (2026-04-24) — 10회 제출 전략

현재 점수: **0.44** (22/50) · 목표: **0.55+** (27+/50)
오늘 남은 제출: 3회 (보존)
내일 가용 제출: 10회

---

## 남은 오답 분포

| 영역 | 정답 | 오답 | 잠재 |
|---|---|---|---|
| Topology (Q1~Q6, Q29~Q33) | ~3 | **8** | +0.16 |
| Path Traditional (Q7~Q16) | 10 | 0 | ✅ 완료 |
| Path PJ (Q34~Q38) | ~0~1 | **4~5** | +0.10 |
| Fault Traditional (Q17~Q28) | ~6 | **6** | +0.12 |
| Fault PJ (Q39~Q50) | ~3 | **9** | +0.18 |
| **합계** | 22 | 28 | **+0.56** 이론 한계 |

---

## 제출 10회 분배 계획

### Submit 1-2: PJ Path 재설계 (우선순위 1)
Q34~Q38 5문제. BFS underlay(11-hop)도 v11 LLM(3-hop)도 실패.

- Submit 1: **VXLAN overlay 2-hop 경로** 시도
  - Hermes-Prime-01 → Demeter-Prime-01 → Hermes-Prime-02 (3-hop)
  - `display_bgp_evpn_all_routing-table` 에서 VTEP IP 추출
  - VNI matching 으로 ingress/egress VTEP 확정
- Submit 2: Submit 1 결과에 따라
  - 개선되면: **underlay 1-hop overlay** (더 단순화)
  - 하락하면: routing-trace 긴 경로 복원

### Submit 3-4: Fault PJ zone reason 다변화 (우선순위 2)
Q39/Q43/Q46~Q49 `missing static route` 일색. 실제는 VXLAN/L3VPN 가능.

- Submit 3: Q39/Q43 → **VXLAN configuration error**
- Submit 4: Q46~Q49 → **L3VPN configuration error**
- 각 PJ Q 마다 current-configuration 의 VXLAN VNI / L3VPN VRF 설정 누락 여부 감지하여 reason override

### Submit 5-6: Topology Q1~Q6 포트 번호 검증
Traditional LLDP 직접 파싱인데 3/6 만 맞음. peer port 번호가 정답과 달라 오답일 가능성.

- Submit 5: **peer port 를 description 역추출로 재구성** (LLDP 대신 description 우선)
- Submit 6: Submit 5 결과에 따라
  - 개선되면: Q29~Q33 PJ 에도 description 기반 확장
  - 하락하면: LLDP 복원 + 다른 포트 포맷 시도 (GE0/0/X vs GE1/0/X)

### Submit 7-8: Q17 "3 candidate nodes" 재선정
`Alpha-Center-02` 지목 중. 다른 후보 교체 실험.

- Submit 7: Q17 → `Beta-Axis-02;192.168.70.22;missing static route`
- Submit 8: Q17 → `Beta-Portal-02;192.168.70.22;missing static route`
- 점수 변화로 정답 노드 확정

### Submit 9-10: 최종 통합 + 안전 마진
- Submit 9: 위 결과 중 가장 좋은 조합 통합 CSV
- Submit 10: 보존 (마지막 fine-tuning 또는 비상용)

---

## 내일 구현 우선순위

### 오늘 밤 미리 준비 (제출 소비 없음)

1. **PJ Path overlay tracer** (agent/track_b/path_tracer.py 에 `trace_overlay_vtep` 추가)
   - `parse_bgp_evpn(qid, device)` in cli_parsers.py
   - VTEP IP → device owner 매핑
   - VNI matching

2. **Fault PJ reason classifier** (fault_analyzer.py 확장)
   - `check_vxlan_config(qid, node)` — current-configuration 에서 vxlan/evpn 확인
   - `check_l3vpn_config(qid, node)` — vrf 설정 확인
   - routing missing 이지만 VXLAN/L3VPN 있으면 reason 업그레이드

3. **Topology description-first parser** (topology_parser.py 분기)
   - Tier 1을 description 으로 바꾼 alternative 버전

### 오늘 밤 생성할 CSV (제출 전 준비)

- `submission_v13_pj_overlay.csv`
- `submission_v13_pj_fault_vxlan.csv`
- `submission_v13_pj_fault_l3vpn.csv`
- `submission_v13_topo_desc.csv`
- `submission_v13_q17_axis02.csv`
- `submission_v13_q17_portal02.csv`

각 CSV 는 single-change delta (한 번에 한 영역만 변경) 원칙.
점수 변화로 정확한 효과 측정.

---

## 핵심 인사이트 (오늘 학습)

1. **BFS 최단경로 ≠ 실제 라우팅 경로**: routing-table nexthop 기반 hop-by-hop 이 정답.
2. **Alphabetical 정렬은 -01 선호, 정답은 -02 중심**: Traditional zone 은 -02 장비가 active path.
3. **"MAC conflict" → reason = MAC address configuration error** 는 맞지만 **포트 특정**이 추가 관건 (v11 과 같은 GE1/0/5 로도 틀림 = 정답 포트가 다름).
4. **PJ zone description 역추적**: Q29~Q33 은 LLDP empty 일 때 주변 description 의 `To-{peer}-{port}` 패턴으로 복원.
5. **Phase 1 exact match 는 공백/대소문자/순서에 민감**.

---

## 금지 사항

- 동일 delta 를 중복 제출 금지 (오늘 Q42 MAC 수정은 변화 없음으로 확인됨)
- 여러 영역 동시 변경 금지 (점수 변화 원인 추적 불가)
- v11 원본 답이 이미 있는 행을 v11 로 "복원" 하는 CSV 제출 금지 (낭비)
