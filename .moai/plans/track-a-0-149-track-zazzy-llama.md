# Track B 개선 플랜 — Zindi 점수 0.18 → 상승 방안

> 파일명은 자동 slug (`track-a-0-149-track-zazzy-llama`) 이나 내용은 **Track B 전용**.
> 작성 일자: 2026-04-23
> 참조: Track A 점수 0.149, Track B 점수 0.18 (Zindi Phase 1 public leaderboard)

---

## Context (왜 이 작업이 필요한가)

- **Zindi Track B Phase 1 public score**: **0.18** (Accuracy only 채점)
- **내부 agent 판정**: v6_full 50문제 중 47 solved / 1 forced / 2 timeout (94% 내부 통과)
- **괴리**: 내부 94% vs 실제 18% = **model 이 답 형식은 맞추었지만 정답 문구 자체가 틀림**
- Track B README (`data/Track B/README.md:639`) 확인: Phase 1 metric = "Scored by accuracy only" — 부분 점수 없음 / Exact Match 또는 line-level IoU 강력 의심
- PJ Topology Q29~Q33 를 TODO-01~15 로 도면 정답까지 끌어올렸으나, **그 이외 45문제 (특히 Fault 24문제)** 품질이 낮음을 이번 분석에서 확인
- 5/4 Phase 1 마감까지 약 11일 남음 — 가장 큰 ROI 에 집중 필요

## 핵심 진단 (근거 데이터)

### 1. Fault 24문제 품질 매우 낮음 (최대 병목)

`submission_v6_full_v10.csv` 의 Fault 24개 라인 분석 (스크립트로 집계):

| 패턴 | 문제 수 | 예시 |
|---|---|---|
| 단일 라인 `node;IP;missing static route` | 16 | Q19/20/21/22/23/24/28/39/40/41/43/44/45/46/49/50 |
| 단일 라인 `node;port;shutdown` | 2 | Q17, Q26 |
| 단일 라인 `node;IP;static route error` | 1 | Q27 |
| 2 라인 `static route error` 반복 | 1 | Q18 |
| 36-라인 shutdown dump | 1 | Q25 (모든 down 인터페이스) |
| 30-라인 shutdown dump | 1 | Q42 |
| 단일 라인 `static route error` port | 1 | Q47/48 (동일 반복) |

문제점:
- **13가지 enumerated fault reason** (routing: blackhole, missing static, static error, ARP, routing loop, BGP, OSPF, loopback conflict, VXLAN, L3VPN, L2VPN, IS-IS, SRV6 / port: shutdown, IP error, 대역폭, MAC, VPN missing, OSPF, MTU) 중 **실제 사용된 건 3개만** (missing static / static route error / shutdown). 심한 under-diagnosis
- Multi-fault scenario 허용됨 (`if there are multiple fault reasons, output each on a new line`) 이나 대부분 1줄 답. 3-5줄 정답인 문제에서 massive 점수 손실
- Q25, Q42 는 반대로 shutdown 덤프 과잉 — 질문이 요구한 specific fault 가 아니라 모든 down interface 나열
- Q39~Q50 (PJ Fault 12개) 답이 모두 `Hermes-Prime-01;IP;missing static route` 템플릿 반복. 시나리오별 다양성 0

### 2. Fault prompt (`agent/track_b/agent.py:654-690`) 가 빈약

현재 FAULT 분기 hint 는 22줄:
- Step 1: routing-table + interface brief + current-config 쿼리
- Step 2: "missing routes, blackhole routes, shutdown ports, IP errors, static route errors, OSPF/BGP misconfig, MTU issues" 문구만 나열
- 13가지 reason 중 6개만 언급, 진단 decision tree 없음
- "multiple faults 가능성" 명시 없음
- Reason 문자열 exact string (`blackhole route`, `missing static route`) 강조 없음
- Port fault vs Routing fault 구분 가이드 없음

### 3. Path 15문제 — 상대적 양호, Q11/Q36/Q38 잔여 이슈

- 12 solved 정답 가능성 높음 (Q7/8 7홉, Q34 3홉 등 합리적 답)
- Q11 4홉 forced — Spine routing 실패 시점에서 조기 종료
- Q36 8홉 (Hermes-Node-01 → Eon-Node-01 path) — timeout_forced, 도면 검증 필요
- Q38 4홉 forced — Opus overlay 적용했지만 도면 truth 와 다를 가능성

### 4. Topology 11문제 — PJ 5 OK, Traditional Q1~Q6 재검증 필요

- Q29~Q33 (PJ) 도면 정답 확정 (TODO-01~15)
- Q1~Q6 (Traditional) v8 solved 상태지만 도면 검증 안 됨 — Q29 처럼 alias 오답 가능성 있음

### 5. 반복 scenario (Q40/Q41, Q47/Q48) 답 identical

- Q40, Q41 정답 동일 (v10): `Hermes-Prime-01;10.1.6.3;missing static route`
- Q47, Q48 정답 동일: `Hermes-Prime-02;20.1.1.20;missing static route`
- 질문이 같은 시나리오 다른 fault 면 문제지만, 실제 question text 비교 필요

---

## 개선 방안 (우선순위)

### Priority 1 — Fault 진단 품질 개선 (최대 ROI)

**목표**: 24/24 Fault 문제에서 multi-fault 탐지 + 13가지 reason 중 맥락 적합한 것 선택.

구체 action:

- **P1-A**: `agent/track_b/agent.py:654-690` 의 FAULT hint 전면 재작성
  - **Reason matrix**: 13개 routing fault + 7개 port fault 를 exact-string + 탐지 CLI 로 매핑
    - `blackhole route` → `display ip routing-table` 에서 next-hop = NULL0
    - `missing static route` → routing table 에 dest 매칭 entry 없음
    - `static route error` → next-hop IP 가 interface 와 불일치
    - `ARP configuration error` → `display arp` 에서 bad mapping / `display current-configuration interface` 에서 `arp static` 오류
    - `routing loop` → `display ip routing-table statistics` 비정상 또는 경로 순환
    - `BGP configuration error` → `display bgp peer` Down / `display current-configuration | include bgp`
    - `OSPF configuration error` → `display ospf peer` Down
    - `loopback IP configuration conflict` → 동일 loopback IP 를 여러 노드가 사용
    - `VXLAN configuration error` → `display vxlan tunnel` 비정상
    - `L3VPN configuration error`, `L2VPN configuration error` → `display ip vpn-instance`, `display mpls l2vc`
    - `IS-IS configuration error` → `display isis peer` Down
    - `SRV6-Policy tunnel planning error` → `display segment-routing ipv6`
    - Port: `shutdown`, `interface IP error`, `traffic congestion on port bandwidth`, `MAC address configuration error`, `VPN configuration missing`, `OSPF configuration error`, `MTU value configuration error`
  - **Multi-fault 강제 스캔**: "After finding one fault, CONTINUE scanning — routing AND port layers can both have faults; multiple routing faults can coexist"
  - **Exact-string 가드**: "Reason MUST be ONE of the exact strings from the question's enumerated list. No paraphrasing (예: 'missing static' → 'missing static route'; 'MAC error' → 'MAC address configuration error')"
  - **Port fault 제한**: "Output port fault lines ONLY for interfaces explicitly mentioned in the question scenario or directly on the traced path; do NOT dump all down interfaces"

- **P1-B**: `validate_fault_answer(answer, question_text)` 신규 헬퍼
  - Reason 문구가 enumerated list 에 속하는지 검증
  - `node;...;reason` 3-field 포맷 검증 (semicolon, trailing whitespace)
  - Multi-fault 기대 수 휴리스틱 (질문에 "multiple" 언급 있으면 최소 2 라인 요구)
  - invalid 시 `validate_topology_answer` 처럼 correction retry 1회

- **P1-C**: Q25 / Q42 shutdown-dump 회귀 방지
  - Fault prompt 에 "scenario 에서 특정 port 를 지목했으면 그 port 만 답" 가드 추가
  - Q25/Q42 질문 text 수동 점검해서 실제로 몇 개 port fault 를 원하는지 확인

예상 효과: Fault 3~5개 정답 복원 (0.18 → 0.24~0.28 추정, Fault 가 50문제 중 48% 비중).

### Priority 2 — 03-3_problems.md 의 Fault/Path "정답" 도면·수동 검증

- 현재 03-3 의 정답 대부분 v8/v9 제출본 self-reference. 실제 도면/ARP/routing 역추적 없음
- Fault 24문제를 3개 그룹으로 나눠 cli.py 수동 검증:
  - Traditional Fault (Q17~Q28, 12개): Beta/Gamma/Alpha zones
  - PJ Fault (Q39~Q50, 12개): PJ zone + Hermes-* pattern
- 각 Q 에 대해 source/dest/suspect 노드에서 `display ip routing-table`, `display interface brief`, `display current-configuration` 를 돌려 ground truth 답을 도출 → 03-3 에 기록
- 이 과정에서 대부분의 "missing static route" 답이 실제로는 **다른 reason** 인 것을 발견할 가능성 높음

산출물:
- `docs/track_b/check/TODO-16_fault_ground_truth.md` — 24문제 수동 검증 결과 + 도면 근거

### Priority 3 — Path Q11/Q36/Q38 재측정 + Topology Q1~Q6 도면 검증

- Q11: `Beta-Node-03 → Alpha-Center-02` 경로. v10 agent 재실행 (TODO-15 RULE 적용) 해서 4홉 완전 정답 도출 시도
- Q36, Q38: Opus overlay 풀이 재점검. 실제 도면 truth 와 대조
- Q1~Q6 Topology Traditional: cli.py 로 각 target 노드의 도면 truth 재확인 (Q29~Q33 처럼 PJ 가 아닌 Traditional 영역도 alias 있을 수 있음)

### Priority 4 — 반복 scenario 답 일관성

- Q40/Q41, Q47/Q48 같은 identical scenario_id 인 경우 답이 당연히 같지만, 다른 scenario 인데 유사 이름 noise 로 같은 답이 나온 경우 question 분석 필요
- test.json 에서 Q39~Q50 의 question text 12개 비교해서 각기 다른 fault 라면 답도 달라야 함

### Priority 5 (Optional) — v11 실행

- P1-A/B/C 적용 후 agent 버전 v11 로 태그
- Fault 24문제 전체 재실행 (`results_v11_fault/`)
- Zindi 테스트 제출 (기간 내 1-2회 추가 시도 가능)

---

## 실행 순서 (3-batch)

### Batch 1 (Priority 1 코드)

1. `agent/track_b/agent.py:654-690` FAULT hint 확장 (Reason matrix + multi-fault + exact-string)
2. 신규 `validate_fault_answer()` 헬퍼 (`agent/track_b/agent.py`, `validate_topology_answer` 근처)
3. 메인 루프 (`run_agent`) 에 Fault validator 분기 + 1회 correction retry 추가
4. Unit 검증: Q17/Q18/Q25 샘플 답을 수동으로 넣어 validator 동작 확인

### Batch 2 (Priority 2 수동 검증)

1. cli.py 로 Q17~Q28 Traditional Fault 12개 ground truth 검증 (필요 시 1시간 이내)
2. Q39~Q50 PJ Fault 12개 ground truth 검증
3. `docs/track_b/check/TODO-16_fault_ground_truth.md` 작성
4. 03-3_problems.md 의 Q17~Q28, Q39~Q50 정답 블록 재갱신

### Batch 3 (v11 실행 + 제출)

1. Fault 24문제 재실행 `results_v11_fault/` (openrouter, 예상 40~60분)
2. v11 submission CSV 생성 (v10 base + Fault 24 overwrite) `submission_v6_full_v11.csv`
3. 로컬 비교: v11 Fault 답이 03-3 수동 검증 ground truth 와 얼마나 일치하는지 집계
4. Zindi 업로드 → 점수 변화 확인

---

## 대상 파일 (핵심)

- `agent/track_b/agent.py:654-690` — FAULT hint
- `agent/track_b/agent.py:438-499` — validator 헬퍼 클러스터 (validate_fault_answer 신규 추가)
- `agent/track_b/agent.py:1355-1412` — 메인 루프 validator 분기
- `docs/track_b/03-3_problems.md:378-732` — Q17~Q50 정답 블록 재갱신
- 신규: `docs/track_b/check/TODO-16_fault_ground_truth.md`
- 신규: `agent/track_b/submission/submission_v6_full_v11.csv`

재사용할 기존 함수:
- `extract_fault_info()` at `agent/track_b/agent.py:213`
- `validate_topology_answer()` pattern at `:438` (validate_fault_answer 구조 참고)
- `postprocess_answer()` at `:676` (fault_lines 추출 이미 지원 `:738`)
- `gen_v10_submission.py` 로직 → `gen_v11_submission.py` 로 복제 후 override_qids 변경

---

## Verification

### 개발 중

- Unit test: `validate_fault_answer()` 가 enumerated reason 만 통과시키는지 Python REPL 에서 확인
- Sanity: Q17/Q18/Q25 질문 text 를 `build_type_hint()` 에 넣어 새 Fault hint 가 exact-string 가이드 포함하는지 print 확인
- Ruff/pyright: 기존 이슈 외 신규 없음 확인

### 통합

- v11 50문제 재실행이 아닌 Fault 24문제만 재실행 (시간 절감)
- `results_v11_fault/eval_detail.jsonl` 에서 24/24 solved 확인
- Fault 답 라인별로 03-3 ground truth 와 diff 스크립트로 일치율 집계 (`tools/diff_fault_ans.py` 1회용)
- Zindi 업로드 후 점수 변화 추적 (target: 0.18 → 0.25 이상)

### 실패 시 롤백

- v11 이 v10 대비 퇴보 (Fault 에서 새 실패 패턴) 시 `gen_v11_submission.py --override-qids` 를 더 좁혀 특정 Q 만 업데이트
- 최악 롤백: `submission_v6_full_v10.csv` 유지

---

## Risk / 주의

- **Fault reason ground truth 가 없어서 수동 검증 필요** — ground truth 가 실제 Zindi 정답과 다를 수 있음. 13가지 reason 중 어느 것을 골라야 하는지 애매한 케이스는 가장 보수적인 `missing static route`/`static route error` 유지가 오히려 안전할 수도
- **openrouter 크레딧 소진 주의** — v10 재실행 시 Q31 만 671s 소요. 24문제 재실행 시 최대 40분, 비용 약 $1~2 추정
- **제출 횟수 제한** — Zindi 일일 제출 제한 (보통 5회) 내에서 점진 평가. 한 번에 큰 변화 넣지 말고 v11 Fault-only 재실행 → 제출 → 점수 확인 → P3/P4 적용 사이클

---

## 요약 (한 줄)

**Fault 24문제 prompt 에 13-reason exact-string matrix + multi-fault 스캔 + Q25/Q42 shutdown-dump 가드 주입 + cli.py 수동 ground truth 검증으로 v11 제출본 생성** — 예상 점수 0.18 → 0.25+ 상승
