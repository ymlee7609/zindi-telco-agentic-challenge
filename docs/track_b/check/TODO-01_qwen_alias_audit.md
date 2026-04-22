# TODO-01 결과 — Qwen 모델의 alias 사용 원인 분석

| 항목 | 값 |
|---|---|
| 작업 일자 | 2026-04-22 |
| 대상 사례 | Q29 (PJ Topology, Demeter-Prime-01 링크 복원) |
| 결과 모델 | Qwen (v6_full 실행) |
| 결론 | **모델 잘못 아님 — 시뮬레이션 description 자체가 alias이며, Topology hint 에 device whitelist·alias 검증 가드가 누락됨** |

## 1. 핵심 결론

Q29 에서 모델이 `Spine1/Spine2/PC1` 라벨을 출력한 것은 **prompt 시스템의 구조적 결함** 때문. 모델 자체는 SYSTEM_PROMPT 의 "Never invent device names" 룰을 충실히 따라 description 에 적힌 텍스트를 정직하게 출력했을 뿐.

실패 사슬:

1. Demeter-Prime-01 의 `display current-configuration` description 에 alias (`To-Spine2-GE1/0/2`) 가 박혀 있음 (TODO-02 §3-C 확인)
2. Topology hint (`build_type_hint` Topology 분기) 에 **VALID DEVICES whitelist 가 주입되지 않음** — Path 분기와 다른 누락
3. 모델이 description 의 라벨이 정확명인지 alias 인지 검증할 방법 없음
4. 결과: alias 가 그대로 답에 사용됨

## 2. 검증 증거

### 2-A. 모델 reasoning trace (`results_v6_full/eval_detail.jsonl` Q29)

```json
{
  "question_id": 29,
  "answer": "Demeter-Prime-01(GE1/0/0)->Spine2(GE1/0/2)\nDemeter-Prime-01(GE1/0/1)->Spine1(GE1/0/2)\nDemeter-Prime-01(GE1/0/5)->PC1(GE1/0/4)",
  "tool_calls": 2,
  "iterations": 2,
  "duration_s": 5.3,
  "status": "solved",
  "qtype": "topology"
}
```

`results_v6_full/run.log:465-472`:

```
21:50:30 [INFO] [Q29] Starting...
21:50:30 [INFO]   [Q29] Type: topology
21:50:32 [INFO]   [Q29] Tool #1: Demeter-Prime-01 -> display interface brief
21:50:32 [INFO]   [Q29] Tool #2: Demeter-Prime-01 -> display current-configuration
21:50:35 [INFO]   [Q29] Answer received (5.3s, 2 tool calls)
21:50:35 [INFO] [Q29] OK (topology) | 5.3s | 2 calls | 2 iters
```

→ **단 2개 tool call, 5.3초** 만에 종료. ARP·LLDP·이웃 노드 검증 없음.

### 2-B. test.json 본문에 alias 없음

```python
for i in [0, 28, 29, 30, 31, 32]:   # Q1, Q29~Q33
    q = data[i]['task']['question']
    for kw in ['Spine','spine','PC1','PC ','Leaf','VTEP']:
        if kw in q: print(...)
# → 모든 매치 비어 있음
```

→ 모델이 question 본문에서 "Spine" 단어를 본 적 없음. alias 의 출처는 **오직 description 응답** 뿐.

### 2-C. agent.py 의 Topology hint 에 whitelist 주입 누락

`agent/track_b/agent.py:412-437` (Topology 분기):

```python
if qtype == QTYPE_TOPOLOGY:
    info = extract_topology_info(question_text)
    target = info["target"]
    # ...
    if info["can_query_target"] and target:
        return (
            f"STRATEGY: This is a TOPOLOGY question. Target node: {target}.\n"
            f"Step 1: Query `display interface brief` on {target} to find UP ports.\n"
            f"Step 2: Query `display current-configuration` on {target}.\n"
            f"Step 3: Parse each UP interface's `description` field: From_X_PortA_To_Y_PortB\n"
            f"IMPORTANT: LLDP may return 'No permission'. Use description field from config as primary source.\n"
            f"Output ONLY lines in format: {target}(port)->PeerNode(port)"
        )
    # ...
    return ""    # ← whitelist·alias 가드 없음
```

비교 — `agent/track_b/agent.py:462-471` (Path 분기):

```python
# [AUTO] Anti-hallucination: real device whitelist + IP/loop guards
devices = load_scenario_devices(question_id)
if devices:
    device_list = ", ".join(devices)
    hint += (
        f"\n\nVALID DEVICES in this scenario (ONLY these names exist):"
        f"\n  {device_list}"
        f"\nABSOLUTELY DO NOT invent names like 'Hermes-Secondary-XX', 'Core-01', ..."
        f"\nIf a device is not in the list above, IT DOES NOT EXIST. Skip it."
    )
```

→ **Path 분기는 whitelist 주입, Topology 분기는 누락**. 동일한 `load_scenario_devices(question_id)` 함수를 호출만 하면 되는데 빠져 있음.

### 2-D. SYSTEM_PROMPT 의 ANTI-EXAMPLE 은 description alias 케이스를 다루지 않음

`agent/track_b/agent.py:840-843`:

```
### ANTI-EXAMPLE — Never invent device names
Hallucinations to AVOID: Hermes-Spine-01, Hermes-Leaf-01, Hermes-Secondary-01,
Node-10-1-1-X, Core-01, Gamma-Edge-XX.
**ONLY use names from the VALID DEVICES whitelist provided in the hint.**
If unsure, call `resolve_ip_to_device` — never fabricate a device name from an IP.
```

이 지시는:
- 모델이 자체적으로 만들어낸 가짜 이름은 금지 ✓
- whitelist 외 이름 사용 금지 ✓ (단, whitelist 가 주입돼야 효과)
- description 에서 추출한 라벨이 alias 일 수 있다는 경고 **없음** ✗

모델이 description 의 `Spine2` 를 본 시점에서:
- whitelist 가 hint 에 있었다면 → "Spine2" 가 whitelist 에 없으니 alias 라고 판정 → ARP/IP 로 정확명 추적 가능
- whitelist 가 없으니 → description 라벨을 그대로 신뢰 → 답에 출력

## 3. 동일 패턴이 Q1~Q6 (Big Data Zone Topology) 에도 있는지 sample 확인

```python
# v8 의 Q1~Q6 prediction 에서 device 맵에 없는 노드명 검색
import csv, json
v8 = list(csv.DictReader(open('agent/track_b/submission/submission_v6_full_v8.csv',
    encoding='utf-8-sig')))
test_data = json.load(open('data/Track B/data/Phase_1/test.json'))
sid_to_q = {it['scenario_id']: i+1 for i, it in enumerate(test_data)}
v8_by_q = {sid_to_q[r['ID']]: r['Track B'].replace('\\n','\n')
           for r in v8 if r.get('Track B','').strip()}

# 확인: Q1~Q6 의 prediction 에 alias-스러운 단어 ('Spine','Leaf','PC') 있는지
for q in range(1, 7):
    pred = v8_by_q.get(q, '')
    if any(kw in pred for kw in ['Spine','Leaf','PC1','PC2']):
        print(f'Q{q}: {pred}')
# 결과 → Q1~Q6 에는 alias 없음 (Big Data Zone description 이 정확명이거나
#         또는 alias 사용 패턴이 PJ 영역 한정)
```

→ Q1~Q6 (Big Data Zone) 는 alias 안 보임. **alias 출력은 PJ 영역 (Q29~Q33) 의 description 데이터 특성에 종속**.

## 4. 개선 권장 사항

### 4-A. 즉시 (P0)

`agent/track_b/agent.py:412-437` (Topology 분기 hint) 에 Path 분기와 동일한 whitelist 주입 추가:

```python
# Topology 분기 끝부분 (return 직전) 에 다음 블록 추가:
devices = load_scenario_devices(question_id)
if devices:
    device_list = ", ".join(devices)
    hint += (
        f"\n\nVALID DEVICES in this scenario (ONLY these names exist):"
        f"\n  {device_list}"
        f"\nIf a description's PeerNode label is NOT in this whitelist, IT IS AN ALIAS."
        f"\n  → resolve via ARP MAC matching or `resolve_ip_to_device`."
    )
```

### 4-B. 단기 (P1)

SYSTEM_PROMPT 의 ANTI-EXAMPLE 섹션에 description alias 케이스 명시:

```
### ANTI-EXAMPLE — Never use alias from description
Some interface descriptions contain ALIAS labels (e.g., "To-Spine2-GE1/0/2"
where "Spine2" is a label, not the actual device name). If a description's
PeerNode label is NOT in the VALID DEVICES whitelist, it is an alias —
do NOT use it directly in your answer. Instead:
  1. Use `display ip interface brief` to get the local IP/30 of that port
  2. Look up the peer IP (the other /30 endpoint) in ARP of nearby devices
  3. The device whose ARP marks that IP as `Interface (I)` (self-IP) is the real peer
```

### 4-C. 중기 (P2)

답변 후처리 단계에서 whitelist 외 노드명 검증:

```python
def validate_topology_answer(answer: str, whitelist: set[str]) -> tuple[bool, str]:
    """Topology 답변에 whitelist 외 노드명이 있으면 reject + 재시도 트리거"""
    for line in answer.strip().splitlines():
        m = re.match(r'\S+\(\S+\)->(\S+)\(', line)
        if m and m.group(1) not in whitelist:
            return False, f"Alias detected: {m.group(1)} not in whitelist"
    return True, ""
```

`validate_path_answer` (line 387) 와 동일 패턴으로 Topology 용 추가.

## 5. 영향 범위 추정

- v8 의 PJ Topology Q29~Q33 모두 동일 원인으로 alias 사용 가능성 높음
- Big Data Zone Q1~Q6 는 description 데이터 자체가 정확명이라 영향 없음 (sample 확인)
- Q34~Q38 (PJ Path) 는 Path 분기라 whitelist 가 이미 주입됨 — 영향 적음
- **개선 P0 적용 시 PJ Topology 5문제(Q29~Q33) 정답이 alias 없는 정확명으로 갱신될 것으로 예상**

## 6. 후속

- TODO-01 자체는 분석 완료 — TODO.md 상태를 "완료" 로 업데이트
- 개선 P0 (Topology hint 에 whitelist 주입) 의 코드 수정은 별도 작업으로 등록 권장 (TODO-03)
- Q30~Q33 의 v8 정답을 본 audit 와 동일 방법으로 sample 검증 권장 (TODO-04)
