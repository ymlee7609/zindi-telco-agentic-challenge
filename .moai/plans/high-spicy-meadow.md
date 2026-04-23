# Plan: 나머지 17개 scenario HIGH 승격 (MEDIUM 16 + LOW 1)

## Context

Track B ground-truth 현재 분포:
- HIGH 20, MEDIUM-HIGH 13, **MEDIUM 16, LOW 1** (= 승격 대상 17)

1차 검증(2026-04-23)에서 Q25/Q28 을 HIGH 로 승격하면서 "정상 scenario vs 변이 scenario 의 routing table diff" 접근법이 효과적임을 확인했다. 남은 17개는 대부분 **PJ/PJGFA zone** scenario 이며, 기존 `prepare_context.py` 가 Legacy zone 전용 parser 만 가지고 있어 PJ zone 의 LLDP 를 찾지 못해 MEDIUM 에 머물렀다.

Explore 결과 PJ zone 은 `display_lldp_neighbor_brief.txt` 대신 **`display_current-configuration.txt` 에 interface description 이 기록**되어 있다 (예: `interface GE1/0/5 description To-Aegis-Prime-01-GE1/0/2`). 이 파일을 파싱하면 Q29-33 TOPO 는 LLDP 직접 검증 수준으로 확인 가능하다.

**Outcome**: MEDIUM 16 + LOW 1 → HIGH 로 승격된 GROUND_TRUTH.json 완성. submission 018 계획에 사용할 수 있는 신뢰도 높은 reference dataset 확보.

---

## Scope

**승격 대상 17개**:
| 유형 | qid | 검증 방법 |
|---|---|---|
| TOPO PJ | Q29, Q30, Q31, Q32, Q33 | current-config description 파싱 |
| PATH PJ intra | Q34, Q37, Q38 | source routing table trace + destination subnet 매핑 |
| FAULT PJ | Q39, Q40, Q41, Q43, Q46, Q47, Q48, Q49 | 정상 scenario vs 변이 routing diff |
| FAULT Delta | Q23 | forward path 전 구간 routing 확인 |

**비대상**: HIGH 20, MEDIUM-HIGH 13 (이미 충분한 근거 있음)

---

## Approach

### Phase A — prepare_context.py 에 PJ zone parser 추가

**파일**: `agent/track_b/opus_reference/prepare_context.py`

기존 Legacy parser (`parse_lldp`, `parse_interface_description`) 와 별도로 PJ zone 용 함수 추가. 기존 import 들은 그대로 재사용.

새 함수:
- `_parse_pj_interface_description(qid, device)` — `display_current-configuration.txt` 를 읽고 `interface {name}\s+description (.+)` 정규식으로 {port: description} 맵 반환. description 이 `To-{device}-{port}` 형태면 peer 추출.
- `_parse_pj_lldp_from_config(qid, device)` — config 기반 LLDP 대체 데이터 생성. 반환 형식은 기존 `parse_lldp` 와 호환 (`NamedTuple` 재사용).
- TOPO 섹션 생성 로직에서 `parse_lldp` 결과가 비어있으면 `_parse_pj_lldp_from_config` fallback 사용.

**재사용**:
- `cli_parsers.read_file` (raw 파일 읽기)
- `cli_parsers.parse_routing_table`, `parse_ip_interface_brief`, `parse_interface_brief` — 그대로
- `cli_parsers.parse_lldp` 반환 NamedTuple 구조

### Phase B — PJ zone context 재생성 (Q29-33 + Q34-50)

명령: `python3 agent/track_b/opus_reference/prepare_context.py --qids 29 30 31 32 33 34 37 38 39 40 41 43 46 47 48 49`

Q23 도 Delta zone 재확인 위해 포함: `--qids 23 29 30 ...`

### Phase C — TOPO Q29-33 검증

**작업**: 각 scenario 의 target 장비에 대해
1. `_parse_pj_interface_description(qid, target)` 으로 {port: peer} 추출
2. `parse_interface_brief(qid, target)` UP 인터페이스 목록 확인
3. UP 인터페이스 개수 = description 추출 개수 일치 확인
4. 역방향 확인: peer 장비의 description 에 target 이 등장하는지
5. 기존 solver 답과 대조

**성공 조건**: UP 인터페이스 N 개 전부에 대해 description 또는 역방향 매칭 확보 → HIGH

### Phase D — PATH Q34/Q37/Q38 검증

**작업**:
1. source 장비의 `display_ip_routing-table.txt` 에서 destination IP 의 longest-prefix match 찾기 → first hop 확정
2. 첫 hop 장비의 routing 으로 second hop 확인
3. destination 에 도달할 때까지 hop-by-hop 추적
4. solver 답 경로와 비교

**Q34**: Hermes-Prime-01 → 10.1.1.20 (Hermes-Prime-02, same subnet 10.1.1.0/24 Vlanif10) — 직접 연결. path 는 overlay (VXLAN) 구간 경유 가능성 있음. solver 답의 중간 hop (Demeter-Prime-01/02, Atlas-Prime-01) 이 overlay 중재자 역할 확인.
**Q37**: Hermes-Node-01 → 20.1.1.20 (Hermes-Node-02) — Q34 대칭, Node zone 내 intra
**Q38**: Hermes-Prime-01 → 20.1.4.20 (Hermes-Node-02) — cross-zone. Q35 와 마지막 2 hop 만 다름.

**성공 조건**: 각 hop 의 routing entry 증거 확보 + solver 답 경로 재현 → HIGH. destination 이 overlay-only 경우 overlay peer 확인 가능하면 HIGH, 아니면 MEDIUM-HIGH 유지.

### Phase E — FAULT PJ 8개 정상 vs 변이 diff

**작업** (Q25/Q28 방식 재활용):
1. 각 PJ FAULT scenario 에 대해 source → destination forward path 구축 (normal PJ scenario 로 routing 스냅샷. 예: Q34 normal 이 Q39 변이의 기준)
2. 변이 scenario 의 forward path 장비들 routing 비교
3. missing / wrong next-hop / routing loop 발견된 장비 = fault node
4. baseline 답과 대조 → 일치하면 HIGH, 불일치하면 Opus 대안 확정 + HIGH + baseline 수정 대상 표기

**주의**: Q39/Q43/Q46 (20.1.1.10 중복), Q40/Q41 (10.1.6.3 중복), Q47/Q48 (20.1.1.20 중복) 그룹별 동일 분석 적용.

### Phase F — Q23 Delta forward path 확정

**작업**:
1. Delta-Node-01 routing → 192.168.74.60/30 = `via 192.168.72.21 GE1/0/2` (→ Delta-Axis-02) 확인
2. Delta-Axis-02 routing → 192.168.74.60/30 = `via 192.168.72.10 GE1/0/6` (→ Delta-Portal-02) 확인 (**route 존재**)
3. Delta-Portal-02 routing 에서 192.168.74.60/30 확인 — Explore 결과 **부재**
4. 즉 fault node = Delta-Portal-02 (또는 경유 장비)
5. Opus 확정 답: `Delta-Portal-02;192.168.74.61;missing static route` (또는 Delta-Portal-01 — Explore 재확인)

**결과**: Q23 Opus 답변을 baseline 과 다르게 설정. GROUND_TRUTH.json 의 `opus_answer` 업데이트.

### Phase G — GROUND_TRUTH.json + 검증 노트 업데이트

**파일**:
- `agent/track_b/opus_reference/build_ground_truth.py` — VERDICT dict 의 17개 항목 conf 및 notes 업데이트. 일부는 `opus` 필드에 Opus 확정 답 추가.
- `agent/track_b/opus_reference/DEEP_VERIFICATION_NOTES.md` — "3차 검증 (PJ zone 확장)" 섹션 append. 각 qid 의 증거 요약.
- `agent/track_b/opus_reference/GROUND_TRUTH.json` — `build_ground_truth.py` 재실행으로 regenerate.

---

## Critical Files

### 수정 대상
- `agent/track_b/opus_reference/prepare_context.py` — PJ parser 추가 (Phase A)
- `agent/track_b/opus_reference/build_ground_truth.py` — VERDICT dict 17 항목 업데이트 (Phase G)
- `agent/track_b/opus_reference/DEEP_VERIFICATION_NOTES.md` — 3차 검증 섹션 append (Phase G)

### 재생성 대상
- `agent/track_b/opus_reference/contexts/q{23,29-33,34,37-41,43,46-49}_context.md`
- `agent/track_b/opus_reference/GROUND_TRUTH.json`

### 재사용 (수정 금지)
- `agent/track_b/cli_parsers.py` — `read_file`, `parse_routing_table`, `parse_interface_brief`, `parse_ip_interface_brief`, `parse_lldp` NamedTuple
- `agent/track_b/topology_parser.py`, `fault_analyzer.py`, `path_tracer.py`
- `agent/track_b/submission/submission_v12_topofault_rt.csv` (baseline)
- `agent/common/submission_example.csv` (포맷 스펙)

---

## Verification

### 1. prepare_context.py 확장 검증
```bash
python3 agent/track_b/opus_reference/prepare_context.py --qids 29
cat agent/track_b/opus_reference/contexts/q29_context.md | head -40
```
→ LLDP 섹션에 (LLDP 정보 없음) 대신 interface description 기반 link 목록이 나와야 함.

### 2. Phase C/D/E/F 증거 스크린샷 (수동)
각 phase 에서 핵심 routing entry (정상 vs 변이) 를 grep 으로 추출한 결과를 DEEP_VERIFICATION_NOTES.md 에 인용. 예:
```
[Q39 Demeter-Prime-01 routing — 20.1.1.0/24 entry]
  (정상 Q34) 20.1.1.0/24 via 10.1.x.x (Atlas-Prime-01)
  (변이 Q39) 20.1.1.0/24 부재 또는 잘못된 next-hop
```

### 3. 최종 통계 확인
```bash
python3 agent/track_b/opus_reference/build_ground_truth.py
```
기대 출력:
```
by conf: {'HIGH': 37, 'MEDIUM-HIGH': 13, 'MEDIUM': 0, 'LOW': 0}
disagreements (Opus != baseline): 2~5  # Q25, Q28 + PJ FAULT 중 새로 발견되는 것
```

### 4. LOW/MEDIUM 없음 확인
```bash
python3 -c "
import json
d=json.load(open('agent/track_b/opus_reference/GROUND_TRUTH.json'))
low=[e for e in d['entries'] if e['confidence']=='LOW']
med=[e for e in d['entries'] if e['confidence']=='MEDIUM']
assert not low, f'LOW remaining: {[e[\"qid\"] for e in low]}'
assert not med, f'MEDIUM remaining: {[e[\"qid\"] for e in med]}'
print('OK: all MEDIUM/LOW upgraded')
"
```

### 5. Regression 확인
기존 HIGH 20 + MEDIUM-HIGH 13 = 33 개의 answer/confidence 는 **변경 금지**. `git diff GROUND_TRUTH.json` 에서 해당 qid 들의 `opus_answer`, `confidence` 필드 변경 없음 확인.

---

## Risks & Mitigations

| 위험 | 대응 |
|---|---|
| PJ zone description 이 특정 장비에 없음 | ARP 테이블 /30 매핑 으로 2차 추출. 그래도 안 되면 해당 qid 는 MEDIUM-HIGH 로 (HIGH 승격 실패 명시) |
| Q34/Q37 overlay path 가 routing table 로 추적 불가 | BGP EVPN / VXLAN peer 테이블 확인. solver 답 과 overlay peer 일치 시 HIGH, 아니면 MEDIUM-HIGH |
| FAULT 정상 기준 scenario 매칭 오류 | 각 FAULT 에 대해 같은 dst_ip 를 사용한 PATH scenario 를 reference 로 명시 (예: Q39 ↔ Q35 동일 dst 20.1.1.10) |
| PJ parser 가 Legacy zone 에 부작용 | `_parse_pj_interface_description` 은 파일 존재 확인 + 빈 결과 시 빈 리스트 반환. Legacy 경로 비영향 |

---

## Out of Scope

- submission 018 CSV 생성 (별도 작업)
- Q13, MEDIUM-HIGH 13 개 승격 (이미 조건부 HIGH 수준)
- prepare_context.py 의 Legacy zone 로직 개선
- PJ zone 외부 장비 (PX1, PSS) 구조 분석
- Zindi 제출 실행
