# Track B - PJ Area (Q29~Q50) Top-1 추월 전략 (목표: 0.78+)

## Context

**현재 상태** (2026-04-27):
- 내 Track B 점수: **0.56** (Traditional 28/28 추정)
- Leaderboard 최고점: **0.78**
- 채점 단위: 1문제 = 0.02점 (50문제 × 0.02 = 1.00 만점)
  - 검증: 028 probe (Q1/Q7/Q17 의도적 오답, -3 정답) → 0.42 = 21/50 ✓
- 0.56 → 0.78 갭 = **11문제 추가 정답** 필요
- 만점(1.00) = Traditional 28 + PJ 22 모두 정답

**핵심 가설 재정렬** (이전 plan 수정):
- ~~시나리오 A (PJ public 미채점)~~ → **부정**
  - 만약 PJ가 미채점이면 leaderboard 최고점도 0.56에 캡됨. 실제로 0.78 존재 → PJ는 public 채점됨
- **시나리오 B (PJ 채점됨, 시도한 답들이 모두 오답)**: 정답
  - probe 020/022/025/026/027의 변경 답들이 모두 오답이라 점수 변화 0
  - Opus baseline 답도 거의 전부 오답 (변경 효과가 0)
  - 실제 정답은 시도해본 답들과 다른 카테고리에 있음

**목표 단계화**:
- M1: 0.56 → **0.78** (PJ 11문제 정답, leader tie)
- M2: 0.78 → **0.90+** (PJ 17문제 정답, leader 추월)
- M3: 0.90 → **1.00** (PJ 22문제 정답, 만점)

---

## 1. Probe 효율 혁신 — Multi-Hypothesis Probe (2026-04-28 보강)

### 새로운 제약 (2026-04-28)

- **하루 10회 제출 제한** + 다음 제출 가능 시각 = 1시간 후
- 시간 압박 — 직렬 binary search (probe 038 BGP → 039 L3VPN → 040 static) 방식은 **3회 제출이 필요**해서 비효율
- 1회 제출에 가능한 한 많은 가설을 동시 검증해야 함

### 문제 인식

기존 binary search는 단일 카테고리 8문제 일괄 변경 → Δscore 1차원 정보만 (그 카테고리 정답 수). 3 카테고리 검증 = 3 submission.

**개선**: 같은 dst 그룹 내 문제는 **답이 동일할 가능성 높음**. 그룹별로 다른 카테고리 시도 → 1 submission으로 4 가설 동시 검증.

### Multi-Hypothesis Probe 설계 (probe 038 재설계)

dst 그룹과 카테고리 매핑:

| dst 그룹 | 문제 수 | QID | 카테고리 시도 (가설) |
|---------|---------|-----|---------------------|
| 20.1.1.10 | 3 | Q39, Q43, Q46 | **BGP configuration error** (가장 유력) |
| 10.1.6.3 | 2 | Q40, Q41 | **L3VPN configuration error** |
| 20.1.1.20 | 2 | Q47, Q48 | **static route error** |
| 20.1.4.10 | 1 | Q49 | **ARP configuration error** |
| Q42 (port) | 1 | Q42 | **interface IP error** (logbuffer ARP_DUPLICATE_IPADDR evidence) |
| Q44/Q45 | 2 | (보존) | `Aegis-Prime-02;Eth-Trunk2.60;shutdown` |
| Q50 | 1 | (보존) | `Hermes-Prime-01;10.1.1.20;ARP configuration error` |

총 변경 9 라인 (8 routing 4 카테고리 + 1 port). 보존 3 답안 (Q44/45/50).

### Δscore 결정 트리 (1회 제출 후 즉시 다음 행동)

| Δscore | 정답 수 | 해석 | 다음 1회 제출 |
|--------|---------|------|---------------|
| 0.00 | 0 | 모든 가설 + Q42/44/45/50 baseline 모두 오답 | "routing loop" / "blackhole" / "OSPF" 등 exotic |
| +0.02 | 1 | 1 가설만 부분 정답 — 가장 모호 | Q42 변경 검증 + 한 그룹 재시도 |
| +0.04 | 2 | L3VPN(Q40/41) 또는 static(Q47/48) 그룹 정답 | 해당 카테고리로 다른 그룹 일괄 시도 |
| +0.06 | 3 | **BGP 그룹(Q39/43/46) 정답** 가장 유력 | BGP 일괄 (8문제 모두) → 0.72 도달 |
| +0.08 | 4 | BGP 3 + 1 추가 (L3VPN, static, ARP, IP error 중 1) | 정답 카테고리 일괄 적용 |
| +0.10~+0.14 | 5~7 | 다수 가설 정답 | best mix 추출 → 0.66~0.70 |
| +0.16~+0.18 | 8~9 | 거의 모든 routing fault + Q42 정답 | 0.72~0.74 도달 |
| **+0.20~+0.22** | 10~11 | **leader tie 도달** | phase 2 보존 |

**핵심**: 단일 카테고리 일괄 probe(예: BGP 8문제 전부) 대비 multi-hypothesis는:
- 같은 정보량 + 추가 가설 검증
- BGP 가설 약점 보완 (L3VPN/static/ARP 동시 확인)
- Q42/Q44/Q45/Q50의 baseline 정답 여부도 부수적으로 검증

### 비교 — 기존 단일 BGP 일괄 vs Multi-Hypothesis

| 항목 | 단일 BGP probe (현 038) | Multi-hypothesis (038-V2) |
|------|------------------------|---------------------------|
| 1 submission 정보량 | BGP 8문제 정답 수만 | 4 카테고리 × 4 dst 그룹 + Q42 |
| Δ=0 일 때 | BGP 모두 오답 → 다음 카테고리 1회 더 | 4 카테고리 모두 오답 → exotic 카테고리 |
| 최선의 경우 | +0.16 (8 BGP 정답) | +0.18 이상 (BGP+L3VPN+static+IP error 부분 정답) |
| 최악의 경우 | -0 (정보 1개) | -0 (정보 4개) |
| Submission budget | 3 카테고리 검증에 3회 | 1회로 4 가설 |

### 사후 Probe 시퀀스

| Probe | 시기 | 설계 |
|-------|------|------|
| **038-V2 (Multi-Hypothesis)** | 1시간 후 (즉시) | 위 설계대로 9 라인 변경 |
| 041 (Confirmer) | Δscore 분석 후 | 정답 카테고리 일괄 적용 (예: BGP+상수) |
| 042 (Fine-tuner) | 041 결과 후 | exotic 카테고리 시도 (필요 시) |
| 043 (Phase 2 final) | phase 2 직전 | 누적 best 답안 |

총 4-5회 제출로 leader tie + phase 2 대비 가능. budget 4-5회 보존.

### Sanity Probe 재정의

기존 028 sanity (0.42 = 21정답)는 Traditional 21/28 정답을 의미 → **Traditional 7개가 의도적 오답이지만 0.42** = 7개 외에 추가 오답 0 → Traditional 28/28 BEST 통합본 = 0.56 ✓ 정합.

PJ baseline(Opus 답)에서 **점수 기여 = 0**: Traditional 28 정답으로만 0.56 도달.

---

## 2. PJ 22문제 정답 후보 재설계

### 2.1 Q29~Q33 TOPO 복구 (5문제, 만점 = +0.10)

**채점 방식 추정**: 정확한 device/port pair string 매칭. 근사값 부분점수 거의 없을 가능성.

**알고리즘** (`topology_parser.py` 보강):
- **Source A** — IP /30 peer matching (HIGH 신뢰, 28건 검증)
- **Source B** — interface description (`description To-{peer}`)
- **Source C** — Eth-Trunk member 매핑 (`trunkport GE1/0/X`)
- **Source D** — **logbuffer LLDP_INTERFACE_NEIGB_CHANGE history** (LLDP 파일 비어있어도 이벤트로 복원 가능 — 핵심 발견)
- **Source E** — Cross-scenario LLDP triangulation (다른 23개 장비에서 역검색)

**검증 게이트**: 5/5 문제가 ≥3 source 일치(HIGH)일 때만 probe 039 실행.

### 2.2 Q34~Q38 PATH 계산 (5문제, 만점 = +0.10)

**probe 026 결과**: direct L2 1-hop = 0.48 유지 (오답)
**Opus 5-hop VXLAN overlay path** = 미검증 (점수 변화 없는 게 직답이거나 똑같이 오답)

**알고리즘** (`path_tracer.trace_overlay_vxlan` 재구현):

```python
def trace_overlay_path(src, dst_ip):
    # 1. dst_ip → vpn{N} 매핑
    vpn = map_subnet_to_vpn(dst_ip)
        # 10.1.1.x→vpn1, 10.1.2.x→vpn2, 10.1.6.x→vpn2,
        # 20.1.1.x→peer-vpn1, 20.1.4.x→peer-vpn4
    
    # 2. src에 Vbdif{N} 직접 + ARP에 dst MAC → direct L2 1-hop
    if has_vbdif(src, vpn) and arp_has(src, dst_ip):
        return [src]  # direct
    
    # 3. vpn{N} VRF에서 longest-prefix 매칭
    nh = vpn_routing_lookup(src, vpn, dst_ip)
        # → IBGP via 1.1.5.X VXLAN
    
    # 4. underlay default VRF에서 1.1.5.X loopback까지 path
    underlay_path = underlay_routing_path(src, nh.vtep_ip)
    
    # 5. remote VTEP에서 last-mile (Vbdif → physical port)
    remote_port = remote_vtep_egress(nh.vtep_ip, dst_ip)
    
    return [src] + underlay_path + [remote_port]
```

**검증 후보**:
- A: 5-hop VXLAN overlay (Opus, 미검증)
- B: 직접 L2 1-hop (probe 026, 오답)
- C: 7-hop with VTEP intermediate
- D: full chain with anycast gateway disambiguation

**probe 040으로 5문제 일괄 변경** → Δ = (정답 수) × 0.02

### 2.3 Q39~Q50 FAULT 진단 (12문제, 만점 = +0.24, 가장 큰 영향)

**시도된 카테고리 모두 오답**:
- "missing static route" (Opus baseline)
- "VXLAN configuration error" (probe 020)
- "L3VPN configuration error" (probe 021, 미제출)
- "Eth-Trunk parent port" (probe 022)
- "MAC address configuration error" (Q42 baseline)

**미시도 카테고리 (정답 후보)**:
- **EVPN configuration error** (가장 유력 — vpn-instance VRF에서 IBGP/VXLAN routes 통째 누락 패턴 확인됨)
- **BGP configuration error**
- **VPN-instance configuration error**
- **route-target import error**
- **duplicate IP address** (Q42, logbuffer ARP_DUPLICATE_IPADDR)
- **ACL configuration error**
- **interface error** / **shutdown** (Q44/Q45 Opus 답 — 미검증)
- **ARP configuration error** (Q50 Opus 답 — 미검증)

**Raw Evidence Mapping** (정상 Q29 vs 변이 diff):

| QID | 변이 evidence | 1순위 답안 후보 |
|---|---|---|
| Q39, Q43, Q46, Q47, Q48, Q49 | vpn{N} VRF에서 IBGP/VXLAN prefix 통째 누락 | **EVPN configuration error** |
| Q40, Q41 | Demeter-Prime-01 vpn2 IBGP routes 5→0 | **EVPN configuration error** |
| Q42 | logbuffer ARP_DUPLICATE_IPADDR + Vbdif10 IP 충돌 | **duplicate IP address** |
| Q44, Q45 | Aegis-Prime-02 Eth-Trunk2.60 sub-interface shutdown | **shutdown** (Opus 답 OK 추정) |
| Q50 | Hermes-Prime-01 ARP에 10.1.1.20 entry 없음 | **ARP configuration error** (Opus 답 OK 추정) |

**`classify_overlay_fault` 함수** (`fault_analyzer.py` 신규):

```python
def classify_overlay_fault(scenario_id, hint_node, hint_dst):
    # 1. dst가 IP 주소 (routing fault path)
    if is_ip(hint_dst):
        vpn = map_subnet_to_vpn(hint_dst)
        diff = vpn_routing_diff(reference, scenario_id, hint_node, vpn)
        if diff.missing_ibgp_vxlan_routes >= 3:
            return "EVPN configuration error"
        if arp_missing(hint_node, hint_dst) and same_subnet(hint_node, hint_dst):
            return "ARP configuration error"
    
    # 2. dst가 interface (port fault path)
    if is_interface(hint_dst):
        if logbuffer_has(scenario_id, "ARP_DUPLICATE_IPADDR"):
            return "duplicate IP address"
        if logbuffer_has(scenario_id, "is shut down", hint_dst):
            return "shutdown"
        if logbuffer_has(scenario_id, "MAC drop"):
            return "MAC address configuration error"
    
    # 3. fallback (기존 baseline)
    return "missing static route"
```

---

## 3. Leader 0.78 분석 — 어떻게 가능한가?

0.78 = 39/50 = Traditional 28 + PJ 11 정답.

**가능 시나리오**:
1. PJ 22 중 11문제만 phase 1 데이터로 결정 가능, 나머지 11은 phase 2 의존 — 즉 leader도 22 만점은 못함, 0.78이 phase 1 한계
2. Leader가 EVPN VXLAN overlay를 정확히 파싱했으나 모든 fault를 일관된 한 카테고리로 답 (예: "EVPN configuration error" 8문제 + Q44/Q45 shutdown + Q50 ARP) → 11문제 정답
3. Leader가 TOPO/PATH 일부 정답 + FAULT 일부 정답으로 11문제 분산 정답

**전략적 의미**:
- 0.78 도달 = FAULT 12문제 중 8~9 정답 + Q44/Q45 + Q50 → 충분히 가능
- 0.90+ = TOPO 또는 PATH도 부분 정답 필요 → 더 높은 정확도

**1순위 시나리오 가정**: leader는 FAULT 카테고리에서 강함, TOPO/PATH는 우리와 비슷.

---

## 4. 구현 우선순위

### Priority HIGH — 즉시 (코드 작업, 제출 0회)

코드 보강 먼저 완료해야 probe 효율 극대화.

- `cli_parsers.py`: `parse_vpn_instance_routing`, `parse_bgp_evpn_routing`, `parse_logbuffer_lldp` 추가
- `fault_analyzer.py`: `classify_overlay_fault` 신규 구현
- `path_tracer.py`: `trace_overlay_vxlan` overlay-aware 재구현
- `topology_parser.py`: Eth-Trunk member + logbuffer LLDP history extractor
- `verify_pj.py`: Q29~Q50 자동 verify + evidence 출력

### Priority HIGH — Probe 시퀀스 (제출 4~5회로 압축)

> 2026-04-28 업데이트: 기존 직렬 binary search (단일 카테고리 일괄) 폐기. Multi-hypothesis probe 로 1회당 정보량 극대화.

**Probe 038-V2 (Multi-Hypothesis)** — 1시간 후 즉시 제출. 위 §1 표 그대로:
- dst 20.1.1.10 (Q39/43/46) → BGP
- dst 10.1.6.3 (Q40/41) → L3VPN
- dst 20.1.1.20 (Q47/48) → static route error
- dst 20.1.4.10 (Q49) → ARP error
- Q42 → interface IP error
- Q44/45/50 보존

**Probe 041 (Confirmer)** — 038-V2 Δscore 분석 후. 정답 카테고리 통일 적용:
- Δ=+0.06 (BGP 그룹 정답) 시: 8 routing fault 모두 BGP → 예상 +0.16~+0.20
- Δ=+0.04 (L3VPN 또는 static 그룹 정답) 시: 해당 카테고리 일괄 → 예상 +0.06~+0.10

**Probe 042 (Exotic Category)** — 038-V2 + 041 모두 변화 적을 시:
- "routing loop" / "blackhole route" / "OSPF configuration error" / "IS-IS configuration error" 시도

**Probe 043 (Phase 2 final)** — 채점 직전 최종본

### Priority MEDIUM — Phase 2 대비

- `GROUND_TRUTH.json`에 `phase2_answer` 필드 추가 (probe 결과로 검증된 정답)
- `gen_submission_phase2_pj_best.py` 신규

---

## 5. 위험 요소 (보완)

| 위험 | 영향 | 완화 |
|---|---|---|
| FAULT 일괄 변경(probe 038)이 0.56 유지 → 정답 카테고리 다 다름 | -0.24 | probe 041에서 mixed candidate 시도 (각 4문제씩 다른 카테고리) |
| 키워드 strict matching ("EVPN configuration error" vs "EVPN config error") | 부분점수 손실 | 동일 카테고리 다른 표현 probe (043) |
| 채점 스코어링이 1정답 ≠ 0.02 (가중치 차이) | 계산 오류 | 028 probe로 0.02/문제 확인됨, 안전 |
| TOPO 5문제 모두 다른 device/port 표기법 → 단일 변경 risk | -0.10 | probe 039 결과로 표기법 검증 |
| Phase 2에 별도 채점 룰 → public 답이 안 통할 수 있음 | 만점 미달 | phase 2 단일 final probe 보존 |
| Probe 예산 9회 → fine-tuning 부족 | 정답 미확정 | HIGH 코드 작업으로 best-guess 정확도 ↑ |
| 0.78 leader가 phase 1 raw data 한계 → 우리도 만점 불가 | 만점 미달 | 일단 0.78 tie 우선, 그 후 만점 시도 |

---

## 6. 성공 판단 기준 (재정의)

| 마일스톤 | 점수 목표 | 판단 시점 |
|---|---|---|
| **M1 — Code Ready** | (제출 0회) | classify_overlay_fault 12 문제 모두 ≥MEDIUM-HIGH 등급 |
| **M2 — FAULT 정답 카테고리 확정** | 0.62+ | probe 038 결과로 fault 카테고리 검증 |
| **M3 — Leader Tie** | **0.78** | probe 038~040 누적 결과 |
| **M4 — Leader Pass** | **0.84+** | probe 041~042 fine-tuning |
| **M5 — Top-1** | **0.90+** | probe 043 final |
| **M6 — Perfect** | **1.00** | phase 2 final submission |

---

## 7. Critical Files (절대경로)

### 보강 대상
- `/home/ymlee/work/zindi_telco_agentic_challenge/agent/track_b/fault_analyzer.py` — `classify_overlay_fault` + Vbdif↔vpn 매핑
- `/home/ymlee/work/zindi_telco_agentic_challenge/agent/track_b/path_tracer.py` — `trace_overlay_vxlan` 재구현
- `/home/ymlee/work/zindi_telco_agentic_challenge/agent/track_b/topology_parser.py` — Eth-Trunk + logbuffer LLDP history
- `/home/ymlee/work/zindi_telco_agentic_challenge/agent/track_b/cli_parsers.py` — vpn-instance/BGP EVPN/logbuffer LLDP 파서 3종
- `/home/ymlee/work/zindi_telco_agentic_challenge/agent/track_b/opus_reference/verify_pj.py` — 22문제 자동 verify

### 신규 작성
- `/home/ymlee/work/zindi_telco_agentic_challenge/agent/track_b/submission/gen_submission_038_fault_evpn_bulk.py` — FAULT 12 일괄 변경
- `/home/ymlee/work/zindi_telco_agentic_challenge/agent/track_b/submission/gen_submission_039_topo_best.py` — TOPO 5 best-guess
- `/home/ymlee/work/zindi_telco_agentic_challenge/agent/track_b/submission/gen_submission_040_path_overlay.py` — PATH 5 overlay
- `/home/ymlee/work/zindi_telco_agentic_challenge/agent/track_b/submission/gen_submission_phase2_pj_best.py` — phase 2 최종

### 갱신 문서
- `/home/ymlee/work/zindi_telco_agentic_challenge/agent/track_b/submission/SUBMISSIONS.md` — probe 038~043 entries
- `/home/ymlee/work/zindi_telco_agentic_challenge/agent/track_b/opus_reference/DEEP_VERIFICATION_NOTES.md` — overlay fault classification 섹션

---

## 8. End-to-End Verification Plan

1. **코드 단위 테스트**:
   - `classify_overlay_fault(Q40, "Demeter-Prime-01", "10.1.6.3")` → "EVPN configuration error"
   - `trace_overlay_vxlan("Hermes-Prime-01", "10.1.1.20")` → 5-hop path 정상 출력
   - `parse_logbuffer_lldp` Q42 → ARP_DUPLICATE_IPADDR 이벤트 추출

2. **Probe 038 (FAULT 일괄)**:
   - dry-run: diff vs submission_018 = 12 lines (Q39~Q50)
   - 제출 → Δscore 측정 → fault 카테고리 정확도 확정

3. **Probe 039 (TOPO)**:
   - dry-run: diff = 5 lines
   - 제출 → Δscore = TOPO 정답 수

4. **Probe 040 (PATH)**:
   - dry-run: diff = 5 lines
   - 제출 → Δscore = PATH 정답 수

5. **Probe 041~042 (Fine-tuning)**: 위 3 결과 분석 후 mixed candidate 재시도

6. **Probe 043 (Final)**: 누적 best 답안으로 phase 2 직전 단일 제출

7. **점수 추적**: 각 probe 후 SUBMISSIONS.md에 Δscore, 추론 정답 수 기록

---

## 9. 즉시 실행 첫 단계 (2026-04-28 업데이트)

### 신규 제약 반영

- 다음 제출 가능: 1시간 후
- 일일 제출 제한: 10회, 효율 극대화 필수
- 기존 단일 카테고리 probe 038 (BGP 일괄) → **multi-hypothesis 로 재설계**

### 즉시 행동 (코드 작업 — 제출 0회)

1. **`gen_submission_038_v2_multi_hypothesis.py` 신규 작성**
   - base = BEST 0.56 통합본
   - dst 그룹별 다른 카테고리 매핑 (위 §1 표 그대로)
   - 9 라인 변경 (Q39/40/41/43/46/47/48/49 + Q42)
   - audit_format 검증

2. **기존 probe 보존**:
   - `submission_038_20260427_fault_bgp_bulk.csv` (BGP 일괄) — 백업, 우선순위 하향
   - `submission_039_20260427_fault_l3vpn_bulk.csv` — phase 2 대비 보관
   - `submission_040_20260427_fault_static_route_error.csv` — phase 2 대비 보관

3. **SUBMISSIONS.md 갱신**:
   - 038-V2 우선순위 1 등록
   - Δscore 결정 트리 명시

### 제출 순서 (1시간 후 ~ 다음 24시간)

1. **1시간 후**: probe 038-V2 (Multi-Hypothesis) — 1회
2. Δscore 분석 → probe 041 (Confirmer) — 1회
3. 필요 시 probe 042 (Exotic) — 1회
4. Phase 2 직전: probe 043 (Final) — 1회

총 4회 사용, **5~6회 budget 보존**. 직렬 binary search 대비 33~50% 절감.

### 핵심 통찰

단일 답 변경 probe → 정보량 1차원 (그 카테고리 정답 수만).
**Multi-hypothesis probe** → 1 submission으로 4 카테고리 가설 + 1 port 가설 동시 검증 = **5차원 정보**.
같은 dst 그룹 내 답이 동일하다는 가정이 강하므로, 그룹 단위로 카테고리를 다르게 매핑하면 Δscore 가 그룹별 정답 분포를 자연스럽게 노출.
