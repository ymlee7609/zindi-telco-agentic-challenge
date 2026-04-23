# TODO-16 / v11 결과 — Fault 24문제 재실행 + FAULT prompt 개선

| 항목 | 값 |
|---|---|
| 작업 일자 | 2026-04-23 |
| 대상 | Q17~Q28 Traditional Fault + Q39~Q50 PJ Fault (총 24문제) |
| 코드 변경 | `agent/track_b/agent.py:654-720` FAULT hint + `:441-534` `validate_fault_answer` + 메인 루프 / forced 분기 |
| 산출물 | `agent/track_b/results_v11_fault/`, `submission_v6_full_v11.csv` |
| 트리거 | Zindi 점수 0.18 (50문제 중 9 추정) — Fault 24/24 "solved" 인데 정답률 낮음 |

## 1. 진단 (Plan §1)

v10 Fault 답변 패턴 (매우 획일적):

- `node;IP;missing static route` — 16문제 (Q19/20/21/22/23/24/28/39/40/41/43/44/45/46/49/50)
- `node;port;shutdown` — 2문제 (Q17, Q26)
- `node;IP;static route error` — 1문제 (Q27)
- 2 라인 routing fault — 1 (Q18)
- 36/30 라인 shutdown 덤프 — 2 (Q25, Q42)
- 13 + 7 = 20 가지 enumerated reason 중 **실제 사용된 건 3종** (static/missing/shutdown)

→ 대량 under-diagnosis + dump 과잉이 0.18 의 주 원인 추정.

## 2. 코드 변경 요약

### 2.1 FAULT prompt 재작성 (`agent/track_b/agent.py:654-720`)

초기판 4844자 → Q17 empty #5 반복 / 684s timeout → 축약판 2060자:
- OUTPUT FORMAT (strict): semicolon 3-field, multi-fault 라인별
- **20가지 exact-string reason 매트릭스** (routing 13 + port 7)
- 4-step diagnosis protocol
- Port-fault 제한: 질문에 명시된 인터페이스 또는 경로 상 인터페이스만
- Paraphrase 금지 (예: `missing static` INVALID)

### 2.2 `validate_fault_answer()` 헬퍼 신규 (`:441-534`)

- 3-field semicolon 검증
- whitelist 포함 여부 (hallucination 차단)
- reason ∈ `_ROUTING_FAULT_REASONS ∪ _PORT_FAULT_REASONS` (20 exact string)
- routing reason → target IPv4 / port reason → port token 엄격 매핑
- OSPF configuration error 는 양쪽 허용 (ambiguous)
- Port token regex: GE/XGE/10~100GE/GigabitEthernet/XGigabitEthernet/Ethernet/Eth-Trunk/MEth + `.subinterface`

### 2.3 메인 루프 + forced 분기 연결

- `run_agent` 메인 루프에 `QTYPE_FAULT` validator 분기 + 1회 correction retry
- forced_answer 분기 (empty_count>=2 이후) 에 Fault validation + TODO-12 XML fallback + retry
- `find_last_valid_assistant_answer` 도 Fault 지원 추가

### 2.4 알려진 제약

- `Vbdif10` (Huawei VLAN BDIF) 같은 가상 인터페이스는 port regex 에 미포함 → Q42 에서 1회 retry 트리거됐으나 retry 답으로 해결. 필요 시 regex 확장 가능

## 3. v11 실행 결과 (24문제)

- 19 solved / 5 forced_answer / 0 timeout
- 총 소요 23.4 분
- Q42 한 번 validator retry 후 통과 (`Vbdif10` → 다른 port 로 정정)

### 3.1 v10 vs v11 Reason Diversity

| Reason | v10 count | v11 count |
|---|---|---|
| shutdown | 68 | 38 |
| missing static route | 18 | 14 |
| static route error | 3 | 4 |
| ARP configuration error | 0 | 2 |
| interface IP error | 0 | 1 |
| MAC address configuration error | 0 | 1 |

→ v10 3종 → v11 6종. Diversity 2배.

### 3.2 v10 vs v11 라인별 변화

```
Q17 v10: Beta-Portal-02;GE1/0/7;shutdown        → v11: Beta-Axis-02;GE1/0/0;shutdown
Q18 v10: Beta/Gamma;GE1/0/2;static route error  → v11: Beta-Node-01;GE1/0/2;interface IP error
Q19 same (1 line)
Q20 same
Q21 v10: 1-line missing static route            → v11: 36-line shutdown dump  [악화 → v11 제외]
Q22 v10: missing static route  → v11: static route error
Q23 v10: missing static route  → v11: static route error
Q24 v10: missing static route  → v11: ARP configuration error
Q25 v10: 36-line shutdown dump → v11: 1-line static route error  [개선]
Q26 v10: 1 line                → v11: 2 lines multi-fault (missing static route 추가)
Q27 v10: static route error    → v11: missing static route
Q28 v10: missing static route  → v11: static route error
Q39 same
Q40 forced (same content)
Q41 forced (same content)
Q42 v10: 30-line shutdown dump → v11: 1-line MAC address configuration error  [개선]
Q43 same (forced)
Q44 same
Q45 same
Q46 forced (same)
Q47 same
Q48 forced (same)
Q49 v10: missing static route  → v11: static route error?
Q50 v10: missing static route  → v11: ARP configuration error
```

### 3.3 Best-of 채택 (Q21 만 제외)

- **명백한 개선 (v11 채택)**: Q25, Q42 dump 제거 → 1-line; Q26 multi-fault 감지
- **명백한 악화 (v10 유지)**: Q21 v11 이 routing 문제를 port-dump 로 회귀
- **중간 (v11 채택)**: 나머지 reason 재해석 — Zindi 점수로 검증

최종 override: 23문제 (Q21 제외).

## 4. 산출물

```bash
python agent/track_b/submission/gen_v11_submission.py \
    --override-qids 17,18,19,20,22,23,24,25,26,27,28,39,40,41,42,43,44,45,46,47,48,49,50
# [v11] rows=550, replaced=16, same_as_v10=7
```

- `agent/track_b/submission/submission_v6_full_v11.csv` — Zindi 업로드 후보
- `agent/track_b/submission/gen_v11_submission.py` — best-of merger (--override-qids 옵션)
- `agent/track_b/submission/diff_v10_v11_fault.py` — v10↔v11 Fault 비교 리포트

## 5. 기대 효과

**낙관적** (v11 Fault 재해석의 절반이 맞고 v10 이 틀린 경우):
- 0.18 → 0.22~0.28 예상 (Fault 에서 3~5문제 정답 복원)

**비관적** (v11 재해석이 대부분 오히려 틀리는 경우):
- 0.18 → 0.10~0.15 퇴보 위험. 이 경우 roll back to v10

→ Zindi 업로드 후 점수 확인 필수. 제출 description: `"v11 — TODO-16 FAULT reason matrix + multi-fault + port-dump guard"`

## 6. 후속 TODO

- TODO-17 수동 ground truth 검증 — 실용적 이유로 skip (cli.py 로 24문제 × 3~5 CLI 호출 시간 많이 소요). Zindi 점수로 대체 검증
- `validate_fault_answer` port regex 에 `Vbdif\d+`, `Vlanif\d+`, `Tunnel\d+` 등 가상 인터페이스 추가 검토
- Q17 초기 timeout 의 원인이었던 과도한 prompt (4844→2060 축약) 교훈: prompt 품질 ≠ 길이
- Q40/Q41/Q43/Q46/Q48 forced_answer (empty 반복 후 강제 출력) 케이스 — 모델 reasoning 소진 패턴, 추가 프롬프트 튜닝 여지

## 7. 변경 파일

- `agent/track_b/agent.py` — FAULT hint / validator / loop 연결 (TODO-16)
- `agent/track_b/submission/gen_v11_submission.py` (신규)
- `agent/track_b/submission/diff_v10_v11_fault.py` (신규)
- `agent/track_b/submission/submission_v6_full_v11.csv` (신규)
- `agent/track_b/results_v11_fault/` (신규, trace 보존)
- `docs/track_b/check/TODO-16_v11_fault_audit.md` (본 문서, 신규)
