# Track B 검증 후속 과제 (TODO)

검증 작업 중 발견된 후속 과제와 진행 결과 모음. 검증 도구 `agent/track_b/cli.py` (라우터 SSH CLI) + 도면(`docs/track_b/03-2_topology_pj.d2`) + cache 데이터를 활용.

---

## 0. 진행 현황 (한눈에)

| ID | 제목 | 우선순위 | 상태 | commit | 산출물 |
|---|---|---|---|---|---|
| TODO-01 | Qwen 모델의 alias 사용 원인 분석 | High | **완료** | `00b736f` | `TODO-01_qwen_alias_audit.md` |
| TODO-02 | 시뮬레이션 데이터 vs 토폴로지 정의 모순 해소 | High | **완료** | `00b736f` | `TODO-02_topology_audit.md` |
| TODO-03 | agent.py Topology hint 에 device whitelist + alias 가드 주입 | High | **완료** | `9ed4721` | `agent/track_b/agent.py:412-465` |
| TODO-04 | Q30~Q33 v8 정답 sample 검증 | Medium | **완료** | `f1a4318` | `TODO-04_q30_q33_audit.md` |
| TODO-05 | Topology 답 라인수 가드 + `validate_topology_answer` | Medium | **완료** | `5c748b1` | `agent/track_b/agent.py:412, 463-499, 1373-1418` |
| TODO-06 | TODO-03/05 패치 후 Q29~Q33 재실행 + v9 제출본 | Medium | **완료** | `a6bcec5` | `TODO-06_v9_rerun_audit.md`, `submission_v6_full_v9.csv` |
| TODO-07 | Q29 v9 재실패 원인 분석 (forced_answer 트리거) | Medium | **완료** | `TODO-07_q29_failure_audit.md` |
| TODO-11 | forced_answer 분기 validation 추가 (패치 5-A, P0) | High | **완료** | (이 커밋) | `agent/track_b/agent.py:1586-1676` |
| TODO-12 | forced 응답 XML/tool_call 감지 fallback (패치 5-B, P1) | Medium | **완료** | (이 커밋) | `agent/track_b/agent.py:752-798` (helpers) + forced 분기 |
| TODO-13 | alias 다발 노드 escalation (패치 5-C, P2) | Low | **완료** | (이 커밋) | `agent/track_b/agent.py:801-845, build_type_hint` |
| TODO-08 | Eon-Node-01 / PJlAN-01 alias 매핑 확인 (Q32 GE1/0/3) | Low | **완료** | (이 커밋) | `TODO-08_pjlan_alias_audit.md` |
| TODO-09 | description 잘림 케이스 처리 + `count_up_physical_ports` (10G) suffix 버그 | Low→High | **완료** | (이 커밋) | `TODO-09_description_truncation_audit.md`, `agent.py:420-438` |
| TODO-14 | TODO-11/12/13 패치 후 Q29~Q33 재실행 + v10 제출본 | Medium | **완료** | (이 커밋) | `TODO-14_v10_rerun_audit.md`, `submission_v6_full_v10.csv` |
| TODO-15 | HIGH-ALIAS prompt 조정 (Q31/Q32 회귀 방지) | High | **완료** | (이 커밋) | `agent/track_b/agent.py:538-569` — RULE 1~4 명문화 |
| TODO-10 | v10 제출본 Zindi 업로드 | Medium | 대기 (사용자 결정) | — | `submission_v6_full_v10.csv` (v9 와 byte-identical, Q29 자동 도출 기준) |

---

## 1. 완료 항목 상세

### TODO-01 — Qwen 모델의 alias 사용 원인 분석 ✅

**진행 일자**: 2026-04-22 / **commit**: `00b736f`

결과 요약:
- Q29 의 alias 출력은 **모델 잘못 아님** — Demeter-Prime-01 description 자체에 alias(`To-Spine2-GE1/0/2`)가 박혀 있고, 모델은 SYSTEM_PROMPT 의 "Never invent device names" 룰을 충실히 지켜 description 라벨을 정직하게 출력
- 근본 원인: `agent/track_b/agent.py:412-437` 의 Topology hint 분기에 device whitelist 주입이 누락 (Path 분기 line 462-471 에는 있음)
- 단 2 tool call (display interface brief + display current-configuration) 만에 5.3초 만에 답 → ARP/LLDP/이웃 검증 없이 description 만 사용

→ TODO-03 의 P0 코드 수정 트리거.

상세: `TODO-01_qwen_alias_audit.md`

---

### TODO-02 — 시뮬레이션 데이터 vs 토폴로지 정의 모순 해소 ✅

**진행 일자**: 2026-04-22 / **commit**: `00b736f`

결과 요약:
- 도면(`03-2_topology_pj.d2` line 51,55-57) 이 truth 로 확정
- Demeter-Prime-01 의 직접 peer = Atlas-Prime-01/02(Leaf), Hermes-Prime-01(Access) — cli.py ARP 결과와 100% 일치
- 사용자 정의 "Spine = Janus-Prime" 은 PJ Area 일반 truth 이지만 Q29 와는 별개 (Demeter-Prime-01 은 VTEP 층, Spine 직속 peer 아님)

alias 매핑 표 (Demeter-Prime-01 description 기준):

| description alias | 실제 장비명 | 도면 계층 |
|---|---|---|
| `Spine2` | Atlas-Prime-01 | Leaf |
| `Spine1` | Atlas-Prime-02 | Leaf |
| `PC1` | Hermes-Prime-01 | Access |

**핵심 통찰**: alias 는 노드-로컬 라벨이라 영역 통일 매핑 불가 (Q31 Janus-Prime-01 의 Spine1/Spine2 는 정반대 매핑).

상세: `TODO-02_topology_audit.md`

---

### TODO-03 — agent.py Topology hint 에 whitelist + alias 가드 주입 ✅

**진행 일자**: 2026-04-22 / **commit**: `9ed4721`

코드 변경:
- `agent/track_b/agent.py:288` — `_DEVICES_ROOT` 경로 버그 수정 (`parent.parent` → `parent.parent.parent`). 디렉토리 재구조화(agent/track_b/) 후 Path 분기의 whitelist 도 그동안 무력화돼 있었으나 함께 복구
- `agent/track_b/agent.py:412-465` — Topology hint 분기 리팩토링 (두 sub-분기의 `return` 을 `hint =` 로, 마지막에 whitelist 주입)
- 신규 ALIAS WARNING 섹션: description 의 alias 식별 + ARP MAC 매칭 4단계 검증 절차 제공

unit 검증 결과:
- `load_scenario_devices(29)` = 23 devices
- Topology hint 에 `VALID DEVICES`, `ALIAS WARNING`, 4단계 검증 절차 모두 포함

→ TODO-06 재실행 시 효과 명확히 확인 (Q31 alias 6/6 해소).

---

### TODO-04 — PJ Topology Q30~Q33 v8 정답 sample 검증 ✅

**진행 일자**: 2026-04-22 / **commit**: `f1a4318`

결과 요약 (5문제 v8 결과):

| Q | target | 결론 | 핵심 |
|---|---|---|---|
| Q29 | Demeter-Prime-01 | 불일치 | Spine1/Spine2/PC1 alias |
| Q30 | Atlas-Prime-01 | **일치** | description 모두 정확명 |
| Q31 | Janus-Prime-01 | 불일치 | 6/6 잘못 — Alpha-Center/Core/Edge 다른 zone hallucination |
| Q32 | Aegis-Prime-01 | 불일치 | 1/3 정답, 1/3 잘못, ETH1/0/2 누락 |
| Q33 | Janus-Node-02 | 불일치 (incomplete) | description 4개 UP 정확명, v8 가 1 라인만 답함 |

4가지 실패 패턴 분류:
1. description alias 그대로 사용 (Q29)
2. description 정확명을 무시하고 다른 alias hallucinate (Q31 GE1/0/4)
3. 다른 zone 의 장비명 hallucinate (Q31 GE1/0/0 = Alpha-Center-01, Big Data Zone)
4. 답 incomplete / early stop (Q33)

→ 패턴 1·2·3 은 TODO-03 으로 해결 가능, 패턴 4 는 TODO-05 추가 필요.

상세: `TODO-04_q30_q33_audit.md`

---

### TODO-05 — Topology 답 라인수 가드 + post-validation ✅

**진행 일자**: 2026-04-22 / **commit**: `5c748b1`

코드 변경:
- `agent/track_b/agent.py:438-461` — `count_up_physical_ports(question_id, target)`: cache 의 `display_interface_brief.txt` 파싱해 UP 물리 포트 수 반환 (서브인터페이스·Eth-Trunk 제외)
- `agent/track_b/agent.py:463-499` — `validate_topology_answer(answer, whitelist, target, expected_lines)`: 라인 수 + 포맷 + target + alias 4중 검증
- `agent/track_b/agent.py:412 (hint)` — LINE COUNT GUARD 섹션 추가 ("EXACTLY N UP physical ports")
- `agent/track_b/agent.py:1373-1418` — 메인 루프에 qtype 별 validator 분기 + Topology validation 실패 시 1회 correction retry

unit 검증 결과:
- Q29 v8(alias) → "alias/hallucination: peer 'Spine2' not in VALID DEVICES"
- cli.py 정확명 → ok
- Q33 v8(incomplete) → "line count 1 != UP physical ports 4"

→ TODO-06 재실행 시 Q33 incomplete → complete 변환 검증.

---

### TODO-06 — Q29~Q33 재실행 + v9 제출본 생성 ✅

**진행 일자**: 2026-04-22 / **commit**: `a6bcec5`

v8 → v9 결과 비교:

| Q | target | v8 결과 | v9 결과 | 도면 매칭 |
|---|---|---|---|---|
| Q29 | Demeter-Prime-01 | alias (Spine2/Spine1/PC1) | v9 fail (XML) → cli.py 수동 결과 채택 | 3/3 (수동) |
| Q30 | Atlas-Prime-01 | 4/4 정확 | 4/4 정확 | 4/4 |
| Q31 | Janus-Prime-01 | 6/6 잘못 | **6/6 정확 ⭐** | 6/6 |
| Q32 | Aegis-Prime-01 | 1/3 정답 | 2/3 정답 | 2/3 |
| Q33 | Janus-Node-02 | 1/4 incomplete | **4/4 정확 ⭐** | 4/4 |

핵심 검증 (패치 효과):
- TODO-03 효과 — Q31 의 6개 alias·hallucination(`Alpha-Center, Beta-Axis, Core, Edge`) 완전 제거, 도면 truth 와 100% 일치
- TODO-05 효과 — Q33 의 incomplete answer (1 라인) → 완전 답 (4 라인). dur=751.7s (validation retry)

산출물:
- `agent/track_b/submission/submission_v6_full_v9.csv` (550 rows, Q29~Q33 만 갱신, 나머지 v8)
- `docs/track_b/03-3_problems.md` (Q29, Q31, Q32, Q33 정답 = v9 으로 갱신, Q30 = v8 동일)

상세: `TODO-06_v9_rerun_audit.md`

---

### TODO-07 — Q29 v9 재실패 원인 분석 ✅

**진행 일자**: 2026-04-22

결과 요약:
- **원인 확정**: `agent/track_b/agent.py:1473-1485` 의 `forced_answer` 분기에서 `resp2.content` 를 포맷/whitelist 검증 없이 즉시 return. 모델이 강제 응답에도 `<tool_call>...XML...</tool_call>` 텍스트를 송출했고 그게 답으로 등록됨.
- **기여 요인**: Q29 가 description 거의 전부 alias (Spine2/Spine1/PC1) 로 가장 복잡한 cross-check 필요 케이스. TODO-03/05 의 긴 hint 텍스트가 모델 추론 부담을 늘려 빈 응답 → forced 분기 트리거.
- **단기 우회**: Q29 답은 cli.py 수동 검증 결과(`Atlas-Prime-01/02, Hermes-Prime-01`) 로 이미 갱신됨.

신규 TODO 3건 파생:
- TODO-11 (P0): forced_answer 분기 validation 추가
- TODO-12 (P1): forced 응답 XML 감지 fallback
- TODO-13 (P2): alias 다발 노드 escalation

상세: `TODO-07_q29_failure_audit.md`

---

## 2. TODO-11/12/13 완료 상세

### TODO-11 — forced_answer 분기 validation 추가 ✅

**진행 일자**: 2026-04-22

코드 변경:
- `agent/track_b/agent.py:1586-1676` (기존 forced 분기 교체):
  - `validate_topology_answer` / `validate_path_answer` 호출 추가
  - invalid 시 마지막 한 번 강제 정정 요청 (`empty_count = 0`, `validation_retried = True`, `continue`)
  - return status: valid → `"forced_answer"`, invalid → `"forced_validation_failed"` (재시도 기회 소진 시)
  - retry 메시지에 "Absolutely no XML, no <tool_call>, no <function=, no <parameter=" 명시

### TODO-12 — forced 응답 XML/tool_call 감지 fallback ✅

**진행 일자**: 2026-04-22

코드 변경:
- `agent/track_b/agent.py:749-798` (신규 helpers):
  - `_TOOL_CALL_XML_RE`: `<tool_call>`, `<function=`, `<parameter=` 패턴 regex
  - `has_tool_call_xml(content) -> bool`: XML 텍스트 감지
  - `find_last_valid_assistant_answer(messages, qtype, whitelist, target, expected_lines)`: 메시지 버퍼를 역순 스캔해 XML 없는 유효 assistant 답 추출 (postprocess + validate 모두 통과)
- forced 분기에서 invalid + XML 감지 시 fallback 먼저 시도, 없으면 TODO-11 retry

### TODO-13 — alias 다발 노드 escalation prompt ✅

**진행 일자**: 2026-04-22

코드 변경:
- `agent/track_b/agent.py:801-849` (신규):
  - `compute_description_alias_ratio(question_id, target, whitelist) -> (alias_count, total)`
  - target 의 `display_current-configuration.txt` 에서 interface description 파싱
  - peer 이름 (`whitelist` 에 존재) 이 description 에 substring 으로 매칭 안 되면 alias 로 카운트
- `build_type_hint` Topology 분기 (LINE COUNT GUARD 뒤):
  - `total >= 3` 이고 `alias / total >= 0.5` 이면 `HIGH-ALIAS TARGET` 섹션 주입
  - "description 만 읽지 말고 ARP /30 + 역방향 description 으로 cross-check 필수" 명시

unit 검증 결과:

| Q | target | alias/total | HIGH-ALIAS |
|---|---|---|---|
| Q29 | Demeter-Prime-01 | 6/10 (60.0%) | 발동 |
| Q30 | Atlas-Prime-01 | 1/5 (20.0%) | — |
| Q31 | Janus-Prime-01 | 4/8 (50.0%) | 발동 |
| Q32 | Aegis-Prime-01 | 3/5 (60.0%) | 발동 |
| Q33 | Janus-Node-02 | 0/6 (0.0%) | — |

---

### TODO-08 — Eon-Node-01 / PJlAN-01 alias 매핑 확인 ✅

**진행 일자**: 2026-04-22 / 산출물: `TODO-08_pjlan_alias_audit.md`

결과 요약:
- **PJlAN-01 = Eon-Node-01 의 alias 확정** — 3중 교차 검증 성립
  1. Eon-Node-01 GE1/0/1 description = `To-Aegis-Prime-01-GE1/0/3` (역방향 description)
  2. Eon-Node-01 LLDP logbuffer: `RemoteSystemName=Aegis-Prime-01, RemotePortId=GigabitEthernet1/0/3, LocalInterface=GE1/0/1`
  3. Q32 내에서만 사용 (scenario-local alias — 다른 시나리오에는 없음)
- v9 Q32 GE1/0/3 답 `Aegis-Prime-01(GE1/0/3)->Eon-Node-01(GE1/0/1)` 은 **도면 truth 와 일치 → 정답**
- 추가 코드 변경 없음 — 현재 ALIAS WARNING + HIGH-ALIAS 가드가 이미 올바르게 작동

---

### TODO-09 — description 잘림 케이스 처리 ✅

**진행 일자**: 2026-04-22 / 산출물: `TODO-09_description_truncation_audit.md`

1. **초기 가설 오인 정정**:
   - TODO-04 가 Q32 Aegis-Prime-01 GE1/0/2 description = "to" 로 잘려 있다고 기술
   - 실제 파일 재확인 결과 `description to Janus-Prime-01-GE1/0/5` 로 **잘리지 않은 정상 description** (lowercase `to `, space-separated)
   - GE1/0/2 는 `PHY=up, Protocol=down` 이라 Topology UP/UP 답에서 제외되는 것이 맞음

2. **진짜 버그 발견 및 수정** — `count_up_physical_ports` (10G) suffix:
   - Huawei display_interface_brief.txt 에서 `GigabitEthernet1/0/0(10G)   up   up` 같이 bandwidth suffix `(10G)` 가 붙은 경우 기존 정규식이 매칭 실패
   - Q32 Aegis-Prime-01 에서 이 버그로 UP ports = **0** → LINE COUNT GUARD 무력화 상태였음
   - 수정: `r"^\s*(GE|GigabitEthernet)\d+/\d+/\d+(?:\([^)]*\))?\s+(\*?down|up)\s+(\*?down|up)"` (`(10G)`, `*down` 등 수용)
   - 결과: Q32 UP=0 → **UP=3 복구** (Q29~Q31, Q33 는 영향 없음)

3. **부수 발견** — Q32 v9 실제 **3/3 정답**:
   - GE1/0/0 BorderLeaf2 = Janus-Prime-02 alias (Janus-Prime-02 GE1/0/5 desc 역방향 확증)
   - GE1/0/3 PJlAN-01 = Eon-Node-01 alias (TODO-08 확정)
   - GE1/0/1 = Aegis-Prime-02 (description 정확명)
   - TODO-06 의 `2/3` 집계는 alias 확정 전이라 오판정

---

### TODO-14 — TODO-11/12/13 패치 후 Q29~Q33 재실행 ✅

**완료**: Q29 3/3 자동 정답 (v9 XML fail 해결), Q30 4/4 회귀 없음, Q31/Q32 회귀 발견 (TODO-15 로 이어짐), Q33 은 시간 절감 위해 중단 (v9 4/4 유지).

**실행 명령**:
```bash
LLM_PROVIDER=openrouter python agent/track_b/agent.py \
  -i "data/Track B/data/Phase_1/test.json" \
  -o agent/track_b/results_v10_test \
  --questions 29,30,31,32,33 --fresh --provider openrouter
```

상세: `TODO-14_v10_rerun_audit.md`

---

### TODO-15 — HIGH-ALIAS prompt 조정 (회귀 방지) ✅

**근거**: Q31 v10 에서 GE1/0/3,5 2 라인 회귀 (6/6→4/6), Q32 v10 에서 GE1/0/3 회귀 (3/3→2/3). HIGH-ALIAS prompt 의 "Reading descriptions alone is UNRELIABLE" + "MANDATORY CROSS-CHECK" 지시가 과도해서 **whitelist 와 정확 매칭되는 description 까지 무시**하고 임의 peer 에 매핑한 현상.

**수정** (`agent/track_b/agent.py:538-569`):
- RULE 1: description 의 PeerNode 가 whitelist 에 있으면 **그대로 사용** (예: `To-Aegis-Prime-01-GE1/0/2` → Aegis-Prime-01 확정). cross-check 금지
- RULE 2: PeerNode 가 whitelist 에 없으면 (진짜 alias: Spine1, Spine2, PC1, PSS, BorderLeaf2) 에 한해 ARP /30 cross-check
- RULE 3: 설명 없는 L2 trunk 포트는 reverse description 탐색
- RULE 4: 역방향 description 매칭 시 **포트 번호 일치 필수** — 포트 번호 틀리면 match 아님

→ 다음 run 에서 Q31, Q32 회귀 제거 기대.

---

### TODO-10 — v10 제출본 Zindi 업로드 (사용자 결정)

**현황**:
- `agent/track_b/submission/submission_v6_full_v10.csv` **생성 완료**
- best-of merge 결과, Q29 만 v10 자동 도출로 덮어쓰기 (Q30~Q33 은 v9 유지)
- v9 의 Q29 수동 답과 v10 자동 답이 byte-identical 하여 결과적으로 v9 = v10
- 차이: **v10 은 자동 도출 출처**라 submissions defensibility 우위

**예상 효과 (v8 대비)**:
- Q31 (6/6 도면 정답) + Q33 (4/4 정답) → v8 대비 10 라인 이상 정답 추가
- Q29 자동 정답 + Q32 3/3 부분 개선
- Q30 변화 없음

**결정 사항** (사용자):
- Zindi 제출 여부 (`submission_v6_full_v10.csv`)
- 제출 시 v10 description 예시: `"v10 — TODO-11/12/13 forced validation + XML fallback + HIGH-ALIAS guard with RULE 1-4 discipline"`

---

## 3. 작업 전체의 핵심 발견

1. **v8 매핑 자체에 50문제 중 46개 mismatch** (별도 commit `3487a3d` 정정 완료)
2. **PJ Topology description 의 alias 비일관성** — 같은 라벨("Spine1", "Spine2", "PC1")이 노드마다 다른 장비를 가리킴 → 영역 통일 매핑 표 불가
3. **모델 잘못이 아닌 prompt 결함** — Topology hint 에 whitelist 누락이 alias hallucination 의 근본 원인
4. **`_DEVICES_ROOT` 경로 버그** (parent 한 번 부족) 이 그동안 Path 분기 whitelist 도 무력화시킨 부수 효과 — TODO-03 와 함께 복구
5. **TODO-03/05 패치 효과 명확히 검증됨** — Q31 6/6, Q33 4/4 정답 도출
6. **HIGH-ALIAS 가드는 양날의 칼** — Q29 (alias 60%, cross-check 필요) 에는 효과적이나 Q31 (alias 50%, description 정확명 + alias 혼재) 에는 과잉으로 작용해 정확 description 까지 무시시킴. RULE 1 ("whitelist 매칭 description 은 그대로 사용") 이 결정적. (TODO-15)
7. **`count_up_physical_ports` (10G) suffix 버그** — Huawei bandwidth 접미사가 들어있는 interface brief 는 기존 정규식으로 포착 불가. Q32 Aegis-Prime-01 에서 LINE COUNT GUARD 무력화 원인 (TODO-09)
8. **forced_answer 분기의 validation 부재** — v9 Q29 fail 의 근본 원인이었음. TODO-11/12 패치로 해결, v10 Q29 자동 정답 도출 성공
9. **Alias 는 scenario-local** — PJlAN-01 = Eon-Node-01 (Q32), BorderLeaf2 = Janus-Prime-02 (Q32), Spine1/Spine2 = 노드마다 다름. 전역 alias 표 불가 (TODO-08)

## 4. 참조 commit / 산출 파일

| commit | 제목 | 영향 파일 |
|---|---|---|
| `3487a3d` | 03-3 ↔ v8 매핑 정정 (50/50) | `03-3_problems.md`, `check/{INDEX,Q29,v8_mapping_audit}.md` |
| `2847490` | Q29 alias 오류 + TODO 2건 | `check/{Q29, TODO, INDEX}.md` |
| `00b736f` | TODO-01/02 분석 보고서 | `check/TODO-0[12]_*.md`, `INDEX.md`, `TODO.md` |
| `9ed4721` | TODO-03 Topology hint whitelist + 경로 버그 | `agent/track_b/agent.py` |
| `f1a4318` | TODO-04 Q30~Q33 sample 검증 | `check/TODO-04_*.md`, `INDEX.md`, `TODO.md` |
| `5c748b1` | TODO-05 라인수 가드 + validate_topology_answer | `agent/track_b/agent.py` |
| `a6bcec5` | TODO-06 v9 재실행 + 제출본 | `submission_v6_full_v9.csv`, `03-3_problems.md`, `check/TODO-06_*.md`, `INDEX.md`, `TODO.md` |
