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
| TODO-11 | forced_answer 분기 validation 추가 (패치 5-A, P0) | High | 미착수 | — |
| TODO-12 | forced 응답 XML/tool_call 감지 fallback (패치 5-B, P1) | Medium | 미착수 | — |
| TODO-13 | alias 다발 노드 escalation (패치 5-C, P2) | Low | 미착수 | — | — |
| TODO-08 | Eon-Node-01 / PJlAN-01 alias 매핑 확인 (Q32 GE1/0/3) | Low | 미착수 | — | — |
| TODO-09 | description 잘림 케이스 별도 처리 (Q32 GE1/0/2 = "to") | Low | 미착수 | — | — |
| TODO-10 | v9 제출본 Zindi 업로드 | Medium | 대기 (사용자 결정) | — | `submission_v6_full_v9.csv` 준비 완료 |

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

## 2. 미착수 TODO 상세

### TODO-11 — forced_answer 분기 validation 추가 (P0)

**근거**: TODO-07 §4 결함 A (forced_answer 분기에 응답 검증 부재).

**패치 5-A**: `agent/track_b/agent.py:1480` 의 forced 분기에 `validate_topology_answer` / `validate_path_answer` 호출 추가. invalid 면 한 번 더 강제 정정 요청 (empty_count 리셋 + continue).

상세: `TODO-07_q29_failure_audit.md` §5

### TODO-12 — forced 응답 XML/tool_call 감지 fallback (P1)

**근거**: Q29 가 강제 응답에도 XML 을 송출한 패턴은 모델 행동 이슈.

**패치 5-B**: `postprocess_answer` 또는 신규 함수에서 `<tool_call>|<function=|<parameter=` 패턴 감지 시 마지막 정상 assistant message 로 fallback.

상세: `TODO-07_q29_failure_audit.md` §5

### TODO-13 — alias 다발 노드 escalation (P2)

**근거**: Q29 의 description 이 거의 모두 alias (Spine2/Spine1/PC1) — 모델에게 추가 cross-check 가 필요한 케이스임을 명시 필요.

**패치 5-C**: description 의 alias 비율이 높으면 prompt 에 "이 노드는 description 대부분이 alias 임. 직접 cross-check 필수" 명시.

상세: `TODO-07_q29_failure_audit.md` §5

---

### TODO-08 — Eon-Node-01 / PJlAN-01 alias 매핑 확인 (Low)

**현상**: Q32 v9 답 `Aegis-Prime-01(GE1/0/3)->Eon-Node-01(GE1/0/1)` — description 은 `To-PJlAN-01-GE1/0/1`. 모델이 PJlAN-01 을 whitelist 의 Eon-Node-01 로 매핑.

**조사 항목**:
- [ ] PJlAN-01 이 Eon-Node-01 의 alias 인지 확인 (도면·다른 노드 description 으로 cross-check)
- [ ] Eon-Node-01 의 ARP/description 에서 Aegis-Prime-01 GE1/0/3 매칭 검증
- [ ] 모델이 무엇을 근거로 매핑했는지 (Eon-Node-01 만 whitelist 에 남았기 때문일 가능성)

---

### TODO-09 — description 잘림 케이스 처리 (Low)

**현상**: Q32 의 Aegis-Prime-01 GigabitEthernet1/0/2 의 description 이 `to` 로 잘려 있음. 모델이 답에 누락. 도면 truth = Janus-Prime-01 GE1/0/5.

**조사 항목**:
- [ ] description 잘림 패턴이 다른 노드/문제에도 있는지 grep
- [ ] agent.py 의 prompt 또는 후처리에 "description 이 비정상적으로 짧으면 도면/ARP 로 fallback" 가드 추가 검토
- [ ] 잘린 description 자동 감지 (length < 5 또는 단어 1개) 후 cross-check 명령 트리거

---

### TODO-10 — v9 제출본 Zindi 업로드 (Medium, 사용자 결정)

**현황**: `agent/track_b/submission/submission_v6_full_v9.csv` 생성 완료. v8 대비 Q29~Q33 5개 row 만 갱신.

**예상 효과**:
- Q31 (6/6 도면 정답) + Q33 (4/4 정답) 에서 v8 대비 10 라인 정답 추가
- Q29 (수동) + Q32 (2/3) 에서 부분 개선
- Q30 은 변화 없음

**결정 사항**:
- Zindi 제출 여부 (사용자 판단)
- 제출 시 v9 description (예: "v9 — TODO-03/05 patch with manual Q29")

---

## 3. 작업 전체의 핵심 발견

1. **v8 매핑 자체에 50문제 중 46개 mismatch** (별도 commit `3487a3d` 정정 완료)
2. **PJ Topology description 의 alias 비일관성** — 같은 라벨("Spine1", "Spine2", "PC1")이 노드마다 다른 장비를 가리킴 → 영역 통일 매핑 표 불가
3. **모델 잘못이 아닌 prompt 결함** — Topology hint 에 whitelist 누락이 alias hallucination 의 근본 원인
4. **`_DEVICES_ROOT` 경로 버그** (parent 한 번 부족) 이 그동안 Path 분기 whitelist 도 무력화시킨 부수 효과 — TODO-03 와 함께 복구
5. **TODO-03/05 패치 효과 명확히 검증됨** — Q31 6/6, Q33 4/4 정답 도출

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
