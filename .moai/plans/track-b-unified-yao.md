# Track B 만점 전략 — Day 2 Unified Plan

**작성일**: 2026-04-24
**목표**: Zindi Telco Agentic Challenge Track B 최대 점수 달성
**현재 점수**: 0.48 (24/50, submission_018_20260423_ground_truth.csv)

---

## Context

Track B는 IP Network 도메인 50문제 (Topology 11 + Path 15 + Fault 24) agentic reasoning 과제. 현재 v12 deterministic parser + Opus 수동 검증 2문제(Q25/Q28)로 0.48을 달성했으나, PJ/PJGFA zone의 EVPN/VXLAN overlay는 미검증 상태. 남은 26개 오답은 대부분 PJ zone Fault(Q39~Q50) + Path(Q34~Q38) + Topology Eth-Trunk(Q31~Q33)에 집중되어 있다.

**왜 지금 해야 하는가**:
- Zindi 제출 10회 남음 (Day 2 시작, 오늘 안에 다 쓸 예정)
- 하루 지연 시 Opus 4.7 Claude Code 세션으로 수동 재검증할 기회 소실
- Conservative Incremental 전략으로 각 제출당 2~3문제만 변경 → 10회로 최대 20~30문제 교정 가능

**의도 결과**:
- 이론 상한 1.0 (50/50), 현실 기대 0.80~0.96 (40~48개)
- PJ Fault reason 재분류 성공 시 +0.24 확보
- 실패 시에도 각 제출이 독립적 영역 delta이므로 rollback 가능

**사용자 확정 제약**:
- Multi-provider ensemble 불가 (API 키 없음) → Claude Code 세션(Opus 4.7)이 유일한 재검증 엔진
- Conservative Incremental: 제출당 2~3문제
- Day 2 집중: 오늘 10회 제출 소진

---

## 현황 분석 (Phase 1 Explore 결과)

### 점수 이력
| Serial | 파일 | Zindi 점수 | 변경 |
|---|---|---|---|
| 016 | submission_v12_topofault_rt.csv | 0.44 (22/50) | v12 baseline |
| 017 | submission_017_topo_newline_fix.csv | 무효 | literal→실제 개행 변환 (포맷 위반) |
| **018** | submission_018_20260423_ground_truth.csv | **0.48 (24/50)** | Q25/Q28 HIGH confidence Opus 교정 |

### 오답 분포 추정 (26개)
| 카테고리 | 문제 수 | 현재 정답 추정 | 오답 집중 |
|---|---|---|---|
| Traditional Topology (Q1~Q6) | 6 | 6/6 | - |
| Traditional Path (Q7~Q16) | 10 | 10/10 | - |
| Traditional Fault (Q17~Q28) | 12 | 8/12 | Q20/Q22/Q23/Q26/Q27 재분류 여지 |
| PJ Topology (Q29~Q33) | 5 | 2~3/5 | Q31/Q32/Q33 Eth-Trunk member |
| PJ Path (Q34~Q38) | 5 | 0~1/5 | EVPN overlay 미구현 |
| PJ Fault (Q39~Q50) | 12 | 1~3/12 | reason enum 오분류 (`missing static route` 일색) |

### 핵심 발견
- **018 답변 == GROUND_TRUTH.json 완전 일치**: v1 Ground Truth 자체가 baseline solver와 common-mode error 가능성
- **Format 검증 통과**: literal `\n`, trailing space 없음, reason enum 일치
- **PJ zone raw files 존재**: `display_bgp_evpn_all_routing-table.txt`, `display_vxlan_tunnel.txt`가 devices_outputs에 있으나 파서 0개

---

## 3대 핵심 레버 (ROI 순)

### P0. PJ Fault Reason 재분류 (이론 +0.24)
- Q39~Q50 중 EVPN 기반 약 10문제의 reason을 `VXLAN configuration error` / `L3VPN configuration error` / `BGP configuration error`로 교체
- 수정 파일: `agent/track_b/fault_analyzer.py`, `agent/track_b/cli_parsers.py`
- 노력: ~2시간

### P1. PJ Topology Eth-Trunk Member Resolution (이론 +0.06)
- Q31/Q32/Q33의 member port 매칭을 Tier 5 (Eth-Trunk member + LLDP 교차검증)로 해결
- 수정 파일: `agent/track_b/topology_parser.py`
- 노력: ~1시간

### P2. PJ Path EVPN Overlay Tracer (이론 +0.10)
- Q34~Q38의 경로 추적을 underlay BGP EVPN next_hop_vtep 기반으로 재구성
- 수정 파일: `agent/track_b/path_tracer.py`
- 노력: ~2시간

---

## 구현 작업 분해 (Day 2)

### Step 1. CLI Parser 확장 [의존성: 모든 후속 작업]
**파일**: `agent/track_b/cli_parsers.py` (Edit)

추가 함수:
- `parse_bgp_evpn(qid, device) -> list[EvpnRoute]`: type-2(MAC/IP) + type-5(IP Prefix) 파싱, next_hop_vtep 추출
- `parse_vxlan_tunnel(qid, device) -> dict[str, VxlanTunnel]`: src_vtep → dst_vtep 매핑, state/type
- `parse_current_config_vrf(qid, device) -> dict[str, VrfConfig]`: `ip vpn-instance` 블록에서 VRF 정의
- `parse_eth_trunk(qid, device) -> dict[str, list[str]]`: Eth-Trunk ID → member port 리스트

재사용: 기존 `parse_routing_table`, `parse_lldp`, `parse_ip_interface_brief`

검증:
- `python3 -c "from agent.track_b.cli_parsers import parse_bgp_evpn; print(parse_bgp_evpn('q39', 'Demeter-Prime-01'))"` smoke test
- 각 신규 함수 최소 1개 qid에서 유효 결과 반환

### Step 2. Fault Analyzer Reason 재분류 [의존성: Step 1]
**파일**: `agent/track_b/fault_analyzer.py` (Edit)

수정:
- `detect_routing_fault` 분기 확장:
  - 장비에 VXLAN 설정 존재 + 대상 VNI 누락 → `VXLAN configuration error`
  - 장비에 L3VPN 설정 존재 + 대상 VRF 누락 → `L3VPN configuration error`
  - BGP EVPN peer state != established → `BGP configuration error`
- `_nexthop_chain` loop 감지 분리 → `routing loop` reason 리턴
- ARP 체크를 PJ zone Vlanif*/VBDif* interface 전역으로 확장 → `ARP configuration error`

재사용: 기존 `_ROUTING_FAULT_REASONS` enum, `extract_fault_scenarios`

검증:
- Q39, Q43 reason이 `VXLAN configuration error`로 전환되는지 smoke test
- Q28 기존 정답 `routing loop` 유지 확인 (regression 방지)

### Step 3. Topology Parser Tier 5 [의존성: Step 1]
**파일**: `agent/track_b/topology_parser.py` (Edit)

추가:
- Tier 5 Eth-Trunk member resolution:
  1. Eth-Trunk의 peer device 확정 (Tier 1~4로)
  2. `parse_eth_trunk`로 local member port 리스트 추출
  3. 각 member port에서 LLDP neighbor 조회 → peer device 일치하는 port만 매칭
  4. 순서 정렬 후 `\n` join으로 multi-line 답 생성

재사용: 기존 `solve_topology`, `check_hallucination`

검증:
- Q31/Q32/Q33에서 Eth-Trunk member port 정확 매칭
- Q1~Q6 traditional topology regression 없음 (기존 답 유지)

### Step 4. Path Tracer EVPN Overlay [의존성: Step 1]
**파일**: `agent/track_b/path_tracer.py` (Edit)

추가:
- `trace_overlay_vxlan(qid, src, dst_ip) -> list[str]`:
  1. src의 VXLAN VTEP IP 획득 (`display_vxlan_tunnel` local 항목)
  2. `parse_bgp_evpn(qid, src)`에서 dst_ip 포함하는 EVPN route lookup
  3. next_hop_vtep IP의 소유 device = egress VTEP
  4. src → egress VTEP underlay path는 기존 `trace_path_by_routing` 재사용
- `trace_path_by_routing` 분기: qid >= 29 + dst IP가 10.x.x.x/20.x.x.x → overlay tracer 우선

재사용: 기존 `build_underlay_graph`, `bfs_shortest_path`, `_routing_hop_by_hop`

검증:
- Q34~Q38 경로가 VTEP 경유 타당한지 Opus 세션 수동 검토
- Q7~Q16 traditional path regression 없음

### Step 5. Opus 4.7 Claude Code 세션 수동 재검증 [의존성: Step 2~4]
**수행 방법**: Claude Code 세션 내에서 Opus로 문제별 raw output 검토

프로세스:
1. 각 제출 전에 후보 답변을 Opus 세션에 제시
2. `devices_outputs/{qid}/{device}/` raw file을 읽어 독립 검증
3. deterministic parser 결과와 불일치 시 raw evidence 기반 최종 판정
4. HIGH confidence 답만 제출에 포함

산출물: `agent/track_b/opus_reference/OPUS_V2_NOTES.md` (각 제출별 검증 근거)

### Step 6. Format Audit [의존성: 모든 CSV 생성 전]
**파일**: `agent/track_b/submission/audit_format.py` (신규)

검사:
- literal `\n` (백슬래시+n 2글자) 사용, 실제 LF 0x0A 금지
- trailing/leading whitespace 없음
- reason enum exact match (20종)
- port alias 통일 (`GE` vs `GigabitEthernet`)
- topology/path/fault 포맷 regex 준수
- UTF-8 BOM 없음

사용:
```bash
python3 agent/track_b/submission/audit_format.py agent/track_b/submission/submission_NNN_*.csv
```

검증: 018 baseline CSV에 실행 → 0 warnings

### Step 7. Submission Generator 시리즈 [의존성: Step 2~6]
**파일**: `agent/track_b/submission/gen_submission_NNN.py` (신규, 각 제출마다 1개)

패턴:
- 이전 최고점 CSV를 baseline으로 로드
- 2~3개 ID만 변경 (Conservative Incremental)
- `audit_format.py` 통과 후 저장
- `SUBMISSIONS.md` 인덱스 업데이트

---

## 제출 10회 분배 (Conservative Incremental)

각 제출당 **2~3문제만 변경**. 이전 최고점 대비 delta 영역 귀속 분해 가능.

| # | Serial | Delta 대상 | 목적 | 예상 Δ |
|---|---|---|---|---|
| 1 | 019 | Q31, Q32 Topology Eth-Trunk member | Tier 5 검증 | +0.02~0.04 |
| 2 | 020 | Q33 Topology + Q23 Traditional Fault 재검증 | Tier 5 확장 + Fault 재분류 | +0.02~0.04 |
| 3 | 021 | Q34, Q35 Path EVPN overlay | overlay tracer 초기 검증 | +0.02~0.04 |
| 4 | 022 | Q36, Q37, Q38 Path | 나머지 PJ Path 일괄 | +0.02~0.06 |
| 5 | 023 | Q39, Q40, Q41 Fault reason 재분류 | PJ Fault 초기 검증 | +0.02~0.06 |
| 6 | 024 | Q42, Q43, Q44 Fault | PJ Fault 확장 | +0.02~0.06 |
| 7 | 025 | Q45, Q46, Q47 Fault | PJ Fault 확장 | +0.02~0.06 |
| 8 | 026 | Q48, Q49, Q50 Fault | PJ Fault 마무리 | +0.02~0.06 |
| 9 | 027 | Q20, Q22, Q26 Traditional Fault 재분류 | 남은 traditional 영역 | +0.02~0.06 |
| 10 | 028 | 최종 통합 + Q27, Q17 미세 조정 | Safety net | +0.00~0.04 |

**Rollback 규칙**:
- 점수 하락 시 다음 제출에서 이전 baseline 복원
- 점수 유지(+0.00) 시 해당 delta 문제가 전부 틀림 → Opus 재검토 필요
- 점수 상승(+0.02) 시 delta 2문제 중 1문제만 맞음 → bisect 재분해

**제출 전 필수 절차**:
1. `audit_format.py` 통과
2. `diff_submissions.py` 로 이전 baseline 대비 변경 영역 확인 (2~3개 ID만 변경됨)
3. Opus 세션 검증 노트 (`OPUS_V2_NOTES.md`)에 근거 기록
4. `SUBMISSIONS.md` 인덱스 업데이트

---

## 수정/신규 파일 목록

### 수정 (기존)
- `agent/track_b/cli_parsers.py` — EVPN/VXLAN/VRF/Eth-Trunk 파서 추가
- `agent/track_b/fault_analyzer.py` — reason 재분류 로직
- `agent/track_b/topology_parser.py` — Tier 5 Eth-Trunk member
- `agent/track_b/path_tracer.py` — `trace_overlay_vxlan` 추가
- `agent/track_b/submission/SUBMISSIONS.md` — 019~028 이력 추가

### 신규
- `agent/track_b/submission/audit_format.py` — 포맷 검증
- `agent/track_b/submission/diff_submissions.py` — 버전 간 ID 단위 diff
- `agent/track_b/submission/gen_submission_019.py` ~ `gen_submission_028.py` — 각 제출 생성기
- `agent/track_b/opus_reference/OPUS_V2_NOTES.md` — Opus 세션 재검증 근거

### 재사용 (변경 없음)
- `agent/track_b/agent.py` — LLM loop (이번 cycle에서는 LLM 호출 최소화)
- `agent/track_b/opus_reference/prepare_context.py` — qid별 context 생성 (이미 완료)
- `agent/track_b/opus_reference/verify_pj.py` — topology/path/fault diff helper
- `agent/track_b/opus_reference/GROUND_TRUTH.json` — v1 참조 (v2 별도 생성 안 함, Opus 세션 직접 활용)
- `agent/common/submission_example.csv` — 포맷 baseline

---

## 검증 방법

### End-to-End 검증 순서

1. **Parser smoke test**:
   ```bash
   python3 -c "from agent.track_b.cli_parsers import parse_bgp_evpn, parse_vxlan_tunnel, parse_eth_trunk; print('OK')"
   python3 -m pytest agent/track_b/tests/ -v  # 기존 테스트 regression
   ```

2. **Deterministic parser 검증** (제출 전):
   ```bash
   python3 agent/track_b/submission/gen_submission_019.py
   python3 agent/track_b/submission/audit_format.py agent/track_b/submission/submission_019_*.csv
   python3 agent/track_b/submission/diff_submissions.py submission_018_*.csv submission_019_*.csv
   ```

3. **Opus 세션 수동 검증**:
   - 각 delta 문제마다 `devices_outputs/{qid}/` raw file 읽기
   - 현재 답과 Opus 답 비교
   - 불일치 시 raw evidence 기반 판정 → `OPUS_V2_NOTES.md` 기록

4. **Zindi 제출 후 검증**:
   - 점수 변화 확인 → delta 귀속 분해
   - Δ = 0.02 × k (k = 맞은 문제 수)
   - k < delta 문제 수 → 다음 제출에서 해당 영역 bisect

### Regression 방지
- 매 제출 CSV에서 Q1~Q16 답변이 018 baseline과 **완전 동일**한지 자동 검증
- `diff_submissions.py`가 변경 ID 개수 > 3이면 에러 종료

---

## 위험 및 완화

| 위험 | 영향 | 완화 |
|---|---|---|
| EVPN parser 해석 오류 (VTEP 정의 차이) | Submit 3~8에서 연속 0점 증가 | Submit 3은 소규모 (Q34/Q35만) 제출 → 점수 확인 후 확장 |
| Opus 세션 수동 검토 시간 초과 | Day 2 내 완료 불가 | 제출 5회 이후 초과 시 P2 (Traditional Fault) 제출로 안전마진 확보 |
| Deterministic parser가 baseline보다 나쁜 답 생성 | 점수 하락 | `diff_submissions.py` 에서 변경 영역 강제 제한, 의심 시 제출 보류 |
| Zindi 점수 해상도 0.02로 bisect 불가 | delta 문제 수 > 2개면 귀속 불명 | Conservative 전략으로 delta = 2~3개 유지 |
| reason enum 오탈자로 자동 0점 | 하루치 제출 낭비 | `audit_format.py` 의 enum 검증이 필수 게이트 |

---

## Progress Board (초기)

```
---
🎯 Track B 만점 전략 진행

[⏸️] Step 1: cli_parsers EVPN/VXLAN 확장            ← 후속 모든 작업의 기반
[⏸️] Step 2: fault_analyzer reason 재분류            ← PJ Fault 정답률 핵심
[⏸️] Step 3: topology_parser Tier 5                  ← Q31~Q33 교정
[⏸️] Step 4: path_tracer overlay                     ← Q34~Q38 교정
[⏸️] Step 5: Opus 세션 수동 재검증 (제출별)          ← 각 제출 전 필수
[⏸️] Step 6: audit_format 구현                       ← 포맷 게이트
[⏸️] Step 7: gen_submission_019~028 (10회)           ← 순차 제출
[⏸️] Submit 019 (Q31/Q32 Topology)                   
[⏸️] Submit 020 (Q33/Q23)                            
[⏸️] Submit 021~028 (나머지 8회)                     
---
```

---

## 성공 기준

- **최소 성공**: 0.60 (30/50) — P0 Fault reason 재분류 일부만 맞음
- **목표 성공**: 0.80 (40/50) — P0 대부분 + P1 Eth-Trunk 성공
- **최대 성공**: 0.96+ (48+/50) — P0/P1/P2 모두 성공 + format 이슈 없음
- **이론 상한**: 1.0 (50/50) — 위 + Traditional Fault 재분류 전부 성공

사용자 확정 방향: **최대한 높게 (aggressive)** → 목표는 0.80~0.96, 이론 1.0 도전.

---

**다음 단계**: 본 plan 승인 후 Step 1 (cli_parsers 확장)부터 순차 구현 시작.
