# Track B 점수 0.20 → 0.60+ 급상승 플랜 (misty-summit)

작성일: 2026-04-23
대상: Zindi Telco Agentic Challenge — Track B (IP Networks)
현재 점수: Zindi public LB **0.20** (10/50 정답)
목표: **0.60+** (리더보드 1위 0.78 추격)

---

## 1. Context — 왜 이 변경이 필요한가

현재 에이전트는 내부적으로 48/50 문제를 "solved" 라벨로 반환하지만, Zindi 점수는 0.20 (10/50). 이 괴리의 근본 원인은 **Exact Match 평가에서 형식 통과 ≠ 정답**이라는 점이다.

Phase 1 탐색으로 확인된 3대 결함:

1. **Topology (Q29~Q33 PJ 영역) alias 환각**: LLM이 `display_lldp_neighbor_brief.txt`의 System Name 필드를 정확히 읽지 않고 `Spine1/Spine2/PC1` 같은 가짜 이름 생성. 실제 정답(`Atlas-Prime-01`, `Hermes-Prime-01` 등)은 CLI 파일에 그대로 적혀 있음.
2. **Fault (Q17~Q28, Q39~Q50) 노드 특정 오류**: reason enum 문자열은 맞추지만 (node, target, reason) 조합의 노드/IP/포트 지정 자체가 추론 오류. 경로상 upstream 노드까지 검증하는 로직 부재.
3. **Path (Q36/Q38 PJ VXLAN) timeout + 환각**: destination IP를 노드명으로 오해해 `Node-10-1-1-X` 같은 존재하지 않는 장비 조회, 30 iteration 내 수렴 실패.

정답 근거가 `data/Track B/devices_outputs/` 102K 파일에 이미 명시되어 있으므로, **deterministic CLI 파서 + LLM 하이브리드**가 ROI 가장 높음.

사용자 결정 (2026-04-23 인터뷰):
- 접근법: **CLI 파싱 + LLM 하이브리드**
- 모델: **Opus 4.7 전면 재실행 허용** (Anthropic SDK는 agent.py에 이미 통합)
- 우선순위: **Topology → Fault → Path 순차 전 영역**

---

## 2. 수정/생성 파일

| Stage | 경로 | 종류 | 예상 LOC |
|---|---|---|---|
| 공용 | `agent/track_b/cli_parsers.py` | 신규 (regex 유틸) | ~180 |
| 1 | `agent/track_b/topology_parser.py` | 신규 | ~250 |
| 2 | `agent/track_b/fault_analyzer.py` | 신규 | ~350 |
| 2 | `agent/track_b/agent.py` | 수정 (fault prompt에 후보 주입) | +50 |
| 3 | `agent/track_b/path_tracer.py` | 신규 | ~300 |
| 4 | `agent/track_b/submission/gen_v12_hybrid.py` | 신규 | ~200 |
| 4 | `agent/track_b/agent.py` | 수정 (Opus 분기 + 3-vote) | +80 |
| 전체 | `docs/track_b/answers_ledger.md` | 신규 (근거 원장) | — |

절대 건드리지 않을 파일 (회귀 방지):
- `agent/track_b/submission/submission_v6_full_v11.csv` (현재 0.20 제출본, 보존)
- `agent/track_b/results_v11_fault/` (과거 결과, 보존)

---

## 3. 재사용 대상 기존 함수 (agent.py)

구현 시 그대로 호출 — 새로 만들지 말 것:

- `load_scenario_devices(qid)` — 해당 Q의 device 목록
- `build_topology_snapshot(qid)` — LLDP 그래프 dict (존재 여부 확인 필요, 없으면 cli_parsers.py로 보완)
- `find_ip_owner(qid, ip)` — IP → 노드명
- `bfs_shortest_path(qid, src, dst)` — Path/Fault 공용 BFS
- `count_up_physical_ports(qid, target)` — Topology UP 포트 개수
- `validate_topology_answer()` / `validate_fault_answer()` / `validate_path_answer()` — 포맷 검증, 모든 신규 모듈이 최종 반환 전 호출
- `postprocess_answer()` — CSV 직전 정규화
- `UnifiedClient` (L1284) — provider/model 스위치만 추가

> 실구현 빌더 에이전트는 먼저 `Grep`으로 각 함수 실제 시그니처를 확인해야 함. 라인 번호는 추정이며 변경 가능.

---

## 4. Stage 1 — Topology 결정론적 파서 (목표 +8~11점)

**의도**: 11문제를 LLM 없이 deterministic 답 생성. Q29~Q33 PJ alias 환각 완전 제거.

**핵심 로직**:
1. `display_lldp_neighbor_brief.txt` 파싱 → `(local_if, peer_system_name, peer_if)` 리스트
   - regex 2~3종 fallback (포맷이 Q마다 다를 수 있음)
   - `LLDP disabled` / 대시 라인 skip
2. `display_interface_brief.txt` → UP 물리 포트 집합 (`*Ethernet*/*`, `Eth-Trunk*`)
3. `display_interface_description.txt` → peer 힌트 (교차 검증용, 불일치 시 LLDP가 truth)
4. `UP ∩ LLDP` → `Target(port)->Peer(port)` 라인, 포트번호 natural sort
5. `validate_topology_answer()` 통과 확인

**완료 기준**:
- Q1~Q6 + Q29~Q33 11문제 전부 파서 출력이 validator 통과
- Q29~Q33 결과 문자열에 `grep -iE "spine|pc[0-9]|core"` 0건 (환각 alias 없음)
- `docs/track_b/answers_ledger.md` 에 11문제 (답, 근거 파일 경로, 확신도 H/M/L) 기록
- CSV 생성: `submission_v12_topo.csv` — Track B 50행 중 Topology만 교체, 나머지는 v11 유지
- **체크포인트 제출**: Zindi 업로드 → 0.36~0.42 예상

---

## 5. Stage 2 — Fault 경로 추적 기반 재특정 (목표 +8~15점)

**의도**: 24문제 중 다수가 노드/IP/포트 특정 오류. Path BFS 재사용하여 경로상 모든 hop 검증.

**핵심 로직**:
1. 질문 텍스트에서 source/destination IP 추출 (기존 `extract_fault_info` 재사용)
2. BFS로 예상 경로 도출
3. 경로상 각 hop 마다:
   - `display_ip_routing-table[_vpn-instance_*].txt` → destination route 존재 검사
   - `display_interface_brief.txt` → next-hop egress IF UP/DOWN
   - `display_current-configuration.txt` → VPN/VNI/MTU/OSPF/BGP 설정 regex
4. 첫 anomaly hop을 후보로 반환, reason은 20개 enum (agent.py:442-471) 중 정확 일치만
5. deterministic 실패 시에만 Stage 4 LLM으로 위임

**프롬프트 개선 (agent.py)**:
- system prompt에 "destination 은 IP이며 노드명으로 변환해 쿼리하지 말 것" 명시
- fault_analyzer가 찾은 후보를 `[CANDIDATE: node;target;reason (confidence=...)]` 형태로 user 메시지 상단 주입
- LLM은 후보 채택 or rejection 이유 제시

**완료 기준**:
- 24문제 중 ≥15문제가 deterministic 후보 반환
- `validate_fault_answer` 통과율 100%
- `answers_ledger.md` 에 24문제 기록, low-confidence 항목 표시
- CSV: `submission_v12_topo_fault.csv`
- **체크포인트 제출**: 0.50~0.58 예상

---

## 6. Stage 3 — Path BFS + VXLAN overlay (목표 +5~8점)

**의도**: Q36/Q38 timeout 제거. Q7~Q16도 LLM 대신 deterministic.

**핵심 로직**:
1. `build_underlay_graph(qid)`: 모든 device LLDP 합쳐 adjacency dict
2. `detect_overlay(qid, src_ip, dst_ip)`: `display_bgp_evpn_all_routing-table.txt` + current-configuration 의 VNI/VTEP 매칭
3. `trace_path(qid, src_ip, dst_ip)`:
   - overlay 감지 시: 2-hop VTEP 경로만 반환 (규칙 확정 후 일관 적용)
   - underlay: BFS 최단 경로
4. `validate_path_answer` 통과, 모든 hop 실 장비명

**제출 실험 (unlimited Phase 1 활용)**:
- underlay-only 버전과 overlay-prefer 버전 2종 CSV 생성
- 둘 다 업로드하여 점수 비교 → 이긴 쪽 채택

**완료 기준**:
- 15문제 전부 validator 통과, `Node-10-*` 환각 문자열 0건
- Q36/Q38 timeout 0 (LLM 루프 제거)
- CSV: `submission_v12_det_full.csv` (+ `_overlay.csv`)
- **체크포인트 제출**: 0.56~0.64 예상

---

## 7. Stage 4 — Opus 4.7 + 3-vote Ensemble (목표 +3~7점)

**의도**: Stage 1~3 deterministic 실패분 (low-confidence) 만 Opus로 정교하게 재풀이.

**핵심 로직**:
1. `gen_v12_hybrid.py`가 50문제를 순회
2. ledger 확신도 H → deterministic 답 그대로 채택
3. 확신도 M/L → `claude-opus-4-7`로 3회 호출, majority vote
4. 3회가 모두 다르면 `effort=high` 1회 추가 후 최다 득표 선택
5. `UnifiedClient` 에 prompt caching 적용 (system + device snapshot `cache_control: ephemeral`)

**완료 기준**:
- 최종 CSV: `submission_v12_hybrid.csv`
- ledger 에 모든 50문제 최종 근거 기록
- **최종 제출**: 0.60~0.68 예상

---

## 8. 병렬화 전략

Stage 1 / 2 / 3 은 **상호 독립**. 공용 의존은 `cli_parsers.py` 하나뿐이므로 3개 빌더 에이전트 병렬 가능.

실행 순서:
1. **Sequential (선행)**: `cli_parsers.py` 단독 작성 및 unit 테스트
2. **Parallel (3 agents)**: Stage 1, 2, 3 동시 진행 — 각자 독립 파일
3. **Sequential**: Stage 4 (Stage 1~3 결과 통합)

---

## 9. 리스크와 완화책

| 리스크 | 완화책 |
|---|---|
| LLDP 포맷이 Q마다 다름 (컬럼폭, 라벨) | `cli_parsers.py`에 2~3종 regex fallback chain, 실패 시 `parse_failed` 마커 → Stage 4 LLM |
| description 필드에 Spine-1 등 자유 라벨 혼재 | LLDP System Name을 truth로 고정, description은 교차 경고용 |
| BFS 그래프 불연결 (management plane 분리) | BFS 실패 시 routing-table next-hop 기반 hop-by-hop trace fallback |
| Opus 4.7 비용 폭증 | deterministic 커버리지 ≥70% 목표, LLM 호출 전 ledger 확신도 체크 |
| agent.py 수정이 기존 기능 회귀 | Stage 4 는 기존 `run_agent` 시그니처 불변, 새 함수만 추가 |
| Zindi 점수가 예상과 다를 때 | 체크포인트 제출로 조기 피드백, Stage별 rollback 가능 |

---

## 10. End-to-end 검증

1. **Unit sanity**: Q1 / Q7 / Q17 / Q29 / Q36 다섯 문제를 각 모듈의 `if __name__ == "__main__"` 에서 호출, `answers_ledger.md` 에 (답, 근거 파일 경로, 확신도) 수기 기록
2. **Manual cross-check**: ledger 내 5문제 근거 파일을 직접 열어 LLDP System Name / UP 포트 / routing-table 일치 확인
3. **Regression diff**: 새 CSV vs `submission_v6_full_v11.csv` 의 변경 행만 비교. 변경이 전부 개선 방향인지 ledger 로 확증
4. **Zindi 체크포인트 업로드**: 매 Stage 완료 시 CSV 제출하여 실제 public LB 점수 확인. 점수 하락 시 해당 Stage rollback 후 원인 분석
5. **최종 검증**: Stage 4 업로드 후 0.60 미달이면 ledger의 low-confidence 항목을 Opus high-effort로 재실행

---

## Critical Files (구현 시 열어볼 순서)

1. `/home/ymlee/work/zindi_telco_agentic_challenge/agent/track_b/agent.py` — 기존 함수 시그니처 확인 (L291, L309, L351, L362, L411, L442, L480, L539, L1284)
2. `/home/ymlee/work/zindi_telco_agentic_challenge/data/Track B/devices_outputs/29/Demeter-Prime-01/display_lldp_neighbor_brief.txt` — LLDP 포맷 샘플
3. `/home/ymlee/work/zindi_telco_agentic_challenge/data/Track B/data/Phase_1/test.json` — 50문제 원본
4. `/home/ymlee/work/zindi_telco_agentic_challenge/agent/track_b/submission/submission_v6_full_v11.csv` — 현 베이스라인
5. `/home/ymlee/work/zindi_telco_agentic_challenge/docs/track_b/07_not_solved_recovery_strategy.md` — 과거 분석 재활용

---

## 실행 준비 체크리스트

- [ ] ANTHROPIC_API_KEY 설정됨 (.env 또는 환경변수, Opus 4.7 호출용)
- [ ] NOC API 서버 기동 (localhost:7860) — Stage 1~3은 불필요, Stage 4 LLM 호출 시에만
- [ ] 기존 v11 CSV 백업 확인 (`submission_v6_full_v11.csv`)
- [ ] Zindi 계정 로그인 + 일일 제출 횟수 여유 확인
