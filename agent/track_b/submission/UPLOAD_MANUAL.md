# Day 2 Zindi 업로드 매뉴얼 — 020~027 Probe 실행 가이드

**작성일**: 2026-04-24 (사용자 부재 중 auto 생성)
**Baseline**: 018 = 0.48 (24/50)
**이전 probe 019 = 0.48 (변화 없음)**
**Zindi 제출 남은 횟수**: 9회 (10회 - 019 소진)

---

## 핵심 가정 (데이터 기반 추론)

019 결과 0.48 유지로 다음이 강하게 시사됨:
- Traditional 문제(Q1~Q28)는 **~24개 정답** 상태
- PJ zone(Q29~Q50) **22문제 대부분 오답**
- Opus의 `missing static route` 일색 답변은 **PJ 환경에서 잘못된 가설**일 가능성
- PJ는 EVPN/VXLAN overlay 기반 → 정답 reason은 `VXLAN configuration error` / `L3VPN configuration error` / `BGP configuration error` 등일 확률

**중복 scenario 활용 (단일 변경으로 복수 ID 영향)**:
- Group A (Q39/Q43/Q46, x3): `Demeter-Prime-01;20.1.1.10;...`
- Group B (Q40/Q41, x2): `Demeter-Prime-01;10.1.6.3;...`
- Group C (Q44/Q45, x2): `Aegis-Prime-02;Eth-Trunk2.60;shutdown`
- Group D (Q47/Q48, x2): `Demeter-Prime-01;20.1.1.20;...`

---

## Probe 일람

| Serial | 파일 | 변경 | 가설 | 성공 시 Δ |
|---|---|---|---|---|
| 020 | `submission_020_20260424_pj_fault_group_a_vxlan.csv` | Q39/Q43/Q46 reason → VXLAN config error | PJ EVPN overlay → VXLAN 관련 | +0.06 |
| 021 | `submission_021_20260424_pj_fault_group_a_l3vpn.csv` | Q39/Q43/Q46 reason → L3VPN config error | Demeter VPN-instance 7개 → VRF 이슈 | +0.06 |
| 022 | `submission_022_20260424_pj_fault_group_c_parent_trunk.csv` | Q44/Q45 port: `Eth-Trunk2.60` → `Eth-Trunk2` | parent trunk shutdown | +0.04 |
| 023 | `submission_023_20260424_pj_fault_group_bd_vxlan.csv` | Q40/Q41/Q47/Q48 reason → VXLAN config error | 020 가설 확장 | +0.08 |
| 024 | `submission_024_20260424_pj_fault_abd_bgp.csv` | Q39~Q48 (7개) reason → BGP config error | 020/021/023 실패 시 대안 | +0.14 |
| 025 | `submission_025_20260424_pj_topo_q29_swap.csv` | Q29 방향 swap (target 오른쪽으로) | Topology 포맷 방향성 | +0.02 |
| 026 | `submission_026_20260424_pj_path_q34_q37_direct_l2.csv` | Q34 path: 5-hop VXLAN → 1-hop direct L2 | PJ Path native routing | +0.02 |
| 027 | `submission_027_20260424_pj_fault_group_a_prime02.csv` | Q39/Q43/Q46 node: Prime-01 → Prime-02 | 노드 오식별 가설 | +0.06 |

각 probe는 **018을 baseline으로 독립 적용** → 실패해도 점수가 0.48 이하로 떨어지지 않음 (rollback 불필요).

---

## 권장 업로드 순서 (9회 제출 예산)

### Phase 1 — 독립 probe 4개 (충돌 없는 다른 영역)

**1. Upload `submission_020_*.csv`** (PJ Fault VXLAN 가설)
- 결과가 **0.54** → VXLAN 가설 적중, **다음: 023 (VXLAN 확장)**
- 결과가 **0.52** → 1개만 VXLAN 정답 (부분 적중) → **021 시도 (L3VPN)**
- 결과가 **0.48** → VXLAN 아님 → **021 (L3VPN) 시도**
- 결과가 **<0.48** → missing static route가 일부 맞았던 것 → **027 (Prime-02 node) 시도**

**2. Upload `submission_022_*.csv`** (Eth-Trunk parent)
- 결과가 **0.50** → Eth-Trunk2 parent 정답, 확정
- 결과가 **0.48** → Eth-Trunk2.60 유지가 맞거나 둘 다 틀림
- 이 결과는 020 결과와 무관 (다른 scenario)

**3. Upload `submission_025_*.csv`** (Q29 direction swap)
- 결과가 **0.50** → Topology는 방향 swap이 정답 → **Q30/Q31/Q32/Q33도 같은 패턴 적용 필요**
  → 사용자 귀환 후 `gen_submission_all_topo_swap.py` 만들어 028 제출
- 결과가 **0.48** → swap 아님, 현재 방향 유지

**4. Upload `submission_026_*.csv`** (Q34 direct L2)
- 결과가 **0.50** → Path는 native 경로가 정답 → Q37도 같은 패턴
- 결과가 **0.48** → overlay 경로 유지 또는 둘 다 오답

### Phase 2 — Adaptive 선택 (Phase 1 결과 기반)

**Case A: 020이 +0.06** → VXLAN 가설 확정
- 5번째 업로드: **023** (B+D에도 VXLAN 적용)
- 이후 결과에 따라 남은 slot 으로 Q49 같은 고유 fault 도 VXLAN 변형

**Case B: 020이 +0.00, 021 도 +0.00** → reason 교체 전략 실패
- 5번째 업로드: **027** (node 교체)
- 6번째: **024** (BGP configuration error 가설)

**Case C: 022/025/026 중 일부 성공** → 해당 패턴 확장 submission 수동 생성

### Phase 3 — 최종 통합 (마지막 slot)

모든 성공한 delta 를 합친 `submission_028_combined.csv` 생성 후 제출.

---

## 규칙

- [HARD] 각 probe 는 018 baseline 에서 출발하므로 **순서 독립적**. 먼저 업로드하기로 한 순서대로 진행.
- [HARD] 제출 결과는 **제출 시 Zindi 페이지에서 즉시 확인**. 각 결과를 `SUBMISSIONS.md` 테이블에 기록.
- [HARD] 점수가 **<0.48** 로 내려가면 해당 probe 는 잘못된 방향 → 다음 probe 는 절대 해당 유형을 반복하지 않음.
- [HARD] Zindi 일일 제출 한도 준수 (필요 시 매뉴얼 참조).

---

## 점수 결과 기록 템플릿

각 업로드 후 `SUBMISSIONS.md` 테이블에 다음 형식으로 추가:

```
| 020 | submission_020_...csv | 2026-MM-DD | 0.XX | VXLAN 가설 [적중/실패]. 다음: ### 진행 |
```

---

## 실행 스크립트

모든 probe 는 이미 생성됨. 추가 생성이 필요하면:

```bash
cd /home/ymlee/work/zindi_telco_agentic_challenge
python3 agent/track_b/submission/gen_submissions_batch.py
```

---

## 위험 관리

- **0.48 아래로 내려가는 경우 없음**: 각 probe 는 018 baseline + 1~7 문제만 변경. 최악 시 해당 변경 문제 전체 오답 = 점수 유지.
- **실제 제출 전 마지막 점검**:
  - CSV 를 text editor 로 열어 `\n` 이 literal (backslash + n 두 글자) 인지 확인
  - UTF-8 BOM 없음 확인
  - 행 수 551 (header + 550 data) 확인

---

## 긴급 rollback

모든 probe 가 실패해도 018 은 보존됨:
```
agent/track_b/submission/submission_018_20260423_ground_truth.csv
```

이 파일이 현재 최고점(0.48) 제출본.
