# TODO-07 결과 — Q29 v9 재실패 원인 분석

| 항목 | 값 |
|---|---|
| 작업 일자 | 2026-04-22 |
| 대상 | Q29 (PJ Topology, target=Demeter-Prime-01) v9 재실행 |
| 결과 | **`forced_answer` 분기의 응답 검증 부재가 원인 — XML 텍스트가 그대로 답으로 사용됨** |

## 1. 한눈에 결론

`agent/track_b/agent.py:1473-1485` 의 forced_answer 분기는 모델에게 "STOP, output answer only" 강제 요청을 보낸 후 받은 응답(`resp2.content`)을 **포맷·whitelist 검증 없이 즉시 return**. Q29 의 모델이 이 강제 요청에 대해 `<tool_call>...XML...</tool_call>` 텍스트로 응답했고, 그 텍스트가 `postprocess_answer` 만 거쳐 답으로 등록됨 (status="forced_answer", iterations=4).

→ Q29 의 답이 정확한 풀이 결과가 아니라 **모델의 잘못된 응답 형식 그대로**.

## 2. eval_detail 실증

```json
{
  "question_id": 29,
  "answer": "<tool_call>\n<function=execute_cli_command>\n<parameter=device_name>\nDemeter-Prime-01\n</parameter>\n<parameter=command>\ndisplay lldp neighbor brief\n</parameter>\n</function>\n</tool_call>",
  "tool_calls": 4,
  "duration_s": 30.2,
  "iterations": 4,
  "status": "forced_answer",
  "qtype": "topology"
}
```

- `iterations=4` → forced_answer 분기 트리거
- `tool_calls=4` → 4번의 tool_call 은 정상 처리
- `answer` 가 XML tool_call 텍스트 → forced 응답 그대로

## 3. 코드 추적 (실패 흐름)

`agent/track_b/agent.py` 의 메인 루프 (`run_agent`) 구조:

```
for iteration in range(MAX_ITERATIONS):
    ...
    resp = client.chat(...)

    if resp.tool_calls:
        empty_count = 0    # 리셋
        # tool_call 처리
        continue

    content = resp.content or ""
    if content.strip():
        # validate_topology_answer / validate_path_answer
        if not _ok and qtype == TOPOLOGY and not validation_retried:
            # 1회 correction retry
            validation_retried = True
            continue
        return {... "status": "solved"|"validation_failed", "answer": ..., "iterations": iteration+1}
    else:
        empty_count += 1
        if empty_count >= 2:
            messages.append({role: user, content: "STOP. Output ONLY answer."})
            resp2 = client.chat(messages, tools=False, ...)
            if resp2.tool_calls:
                # 다시 tool_call 처리 후 continue
                continue
            if resp2.content.strip():
                return {... "status": "forced_answer",
                        "answer": postprocess_answer(resp2.content, qtype), ...}   # ← 여기!
                # 검증 없음
```

### Q29 의 추정 흐름 (iter 0~3)

| iter | resp | empty_count | tool_calls | 결과 |
|---|---|---|---|---|
| 0 | empty | 1 | 0 | continue |
| 1 | empty | 2 → forced! | 0 | resp2.tool_calls 발생 (4개 tool_call) → 처리 후 continue |
| 2 | empty | 1 (forced 분기에서 0 으로 리셋되었을 수 있음) | 4 | continue |
| 3 | empty | 2 → forced! | 4 | resp2.content = `<tool_call>...XML...</tool_call>` → **return forced_answer** |

(정확한 trace 는 run.log 가 없어 추정. background output 도 `tail -80` 으로 잘려 Q29 부분 누락. 핵심: forced 분기 안의 resp2.content 가 XML 일 때 별도 검증 없음)

## 4. 핵심 결함

### 결함 A — forced_answer 분기에 응답 검증 부재 (Critical)

`agent.py:1480` 부근:

```python
content = resp2.content or ""
if content.strip():
    elapsed = time.time() - start_time
    return {
        "question_id": question_id,
        "answer": postprocess_answer(content, qtype),   # ← XML 도 그대로 통과
        ...
        "status": "forced_answer",
        "qtype": qtype,
    }
```

문제:
- `validate_topology_answer` / `validate_path_answer` 호출 없음
- `postprocess_answer` 가 XML 태그 stripping 을 일부 수행하지만 `<tool_call>...XML...</tool_call>` 같이 잘못 닫힌 또는 비표준 XML 은 통과시킬 수 있음
- 결과: 모델이 강제 응답에 또 XML 을 넣어도 그대로 답으로 등록

### 결함 B — Topology 가 처음 4 iter 동안 답을 못 도출

Q29 는 5.3초만에 답한 v8 와 달리 4 iter, 30.2초 걸리고도 답 못함. 가설:
- TODO-03 의 ALIAS WARNING (긴 가이드 텍스트) + TODO-05 의 LINE COUNT GUARD 로 hint 가 길어져 prompt 토큰 증가
- 모델이 더 신중해지면서 ARP/이웃 검증 시도 → 4 tool_call 사용
- 그러나 답을 정해진 라인 수(3)에 맞춰 출력하는 데 실패 → empty 응답 반복
- 또는 모델이 작업을 내부적으로 미완성으로 판단해 빈 응답 송출

### 결함 C — Q29 만 fail (Q30~Q33 은 동일 패치로 성공)

- Q30: description 정확명만 사용 → 추론 부담 적음 → 정상
- Q31: description 일부 alias, 일부 정확명 → ALIAS WARNING + ARP 검증으로 정상 도출
- Q32: description 일부 alias → 부분 도출
- Q33: description 정확명, 라인 수 가드로 4/4 도출
- Q29: description **전부 alias 또는 자기-라우터 description (다른 노드의 ARP 역추적 필요)** → 가장 어려운 케이스
  - GE1/0/0,1: description="Spine2/Spine1" alias → ARP 매칭 필요 (Atlas-Prime-01/02)
  - GE1/0/5: description="PC1" alias, L2 trunk (IP 없음) → 도면이나 역방향 description 필요

→ Q29 는 prompt 가이드대로 했어도 추가 cross-check 가 필요한 가장 복잡한 케이스. 모델이 "할 일이 너무 많다" 고 인식하고 빈 응답으로 도피했을 가능성.

## 5. 권장 수정 (TODO-11 으로 신규 등록)

### 패치 5-A (P0) — forced_answer 분기에 validation 적용

```python
# agent.py:1480 근처
content = resp2.content or ""
if content.strip():
    _processed = postprocess_answer(content, qtype)
    # forced 분기에서도 동일 validator 호출
    if qtype == QTYPE_TOPOLOGY:
        _ok, _clean, _ = validate_topology_answer(
            _processed, _whitelist, _target, _expected
        )
    else:
        _ok, _clean, _ = validate_path_answer(_processed, _whitelist, qtype)
    if not _ok:
        # 한 번 더 강제 정정 요청 (정정 reason 포함)
        messages.append({"role": "assistant", "content": content})
        messages.append({
            "role": "user",
            "content": (
                f"Your forced answer is STILL invalid: {_reason}. "
                f"This is your FINAL chance. Output the answer in the exact format. "
                f"Use ONLY device names from: {sorted(_whitelist)}."
            ),
        })
        empty_count = 0   # 리셋
        continue
    return {... "status": "forced_answer", "answer": _processed, ...}
```

### 패치 5-B (P1) — forced 분기 응답이 비정상적으로 길거나 XML 패턴이면 truncate + 경고

XML/tool_call 패턴 감지 후 buffer 에서 첫 정상 라인만 추출:

```python
# postprocess_answer 또는 신규 함수
if re.search(r'<tool_call>|<function=|<parameter=', content):
    log.warning(f"[Q{question_id}] forced response contains tool_call XML — fallback to last assistant message")
    # 마지막 정상 assistant message 검색
    ...
```

### 패치 5-C (P2) — Q29 같은 alias 다발 케이스 자동 escalation

description 의 alias 비율이 높으면 (50% 이상), prompt 에 "이 노드는 거의 모든 description 이 alias 임. 직접 cross-check 가 필요함" 명시.

## 6. 단기 우회

코드 패치 없이 즉시 가능한 우회:
- v9 제출본의 Q29 답을 **cli.py 수동 검증 결과(`Demeter-Prime-01->Atlas-Prime-01/02/Hermes-Prime-01`)** 로 수동 갱신 (이미 적용됨, `submission_v6_full_v9.csv`)
- 03-3_problems.md 의 Q29 도 동일 (이미 적용됨)

## 7. 후속

- TODO-11 (신규, P0): forced_answer 분기 validation 추가 (패치 5-A)
- TODO-12 (신규, P1): forced 응답 XML 감지 fallback (패치 5-B)
- TODO-13 (신규, P2): alias 다발 노드 escalation (패치 5-C)
- run.log 자동 생성 활성화 검토 (현재 logging.basicConfig 만 있어 stdout 만 — FileHandler 추가 시 trace 영구 보존)
