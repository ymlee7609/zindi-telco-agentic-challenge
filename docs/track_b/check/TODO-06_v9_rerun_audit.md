# TODO-06 결과 — TODO-03/05 패치 후 Q29~Q33 재실행 audit

| 항목 | 값 |
|---|---|
| 실행 일자 | 2026-04-22 |
| 패치 | TODO-03 (Topology hint 에 whitelist + ALIAS WARNING) + TODO-05 (LINE COUNT GUARD + validate_topology_answer + retry) |
| Provider/Model | openrouter / qwen3.5-35b-a3b |
| 결과 디렉토리 | `agent/track_b/results_v9_test/` |

## 0. 한눈에 보는 결과

| Q | target | UP 포트 | v8 결과 | v9 결과 | 도면 매칭 | 결론 |
|---|---|---|---|---|---|---|
| Q29 | Demeter-Prime-01 | 3 | alias 사용 (Spine2/Spine1/PC1) | **fail (XML 답)** | — | v9 실패 — Q29 만 별도 재시도 필요 |
| Q30 | Atlas-Prime-01 | 4 | 4/4 정확 | **4/4 정확** | 4/4 도면 일치 | v8 = v9 동일 정답 |
| Q31 | Janus-Prime-01 | 6 | 6/6 잘못 (alias·hallucination) | **6/6 정확** | 6/6 도면 일치 | **alias 모두 해소, 도면 100% 일치** |
| Q32 | Aegis-Prime-01 | 0(물리)/Eth-Trunk | 1/3 정확, 2/3 잘못 | **2/3 정확, 1개 의심 (Eon-Node-01)** | 2/3 도면 일치 | 부분 개선 |
| Q33 | Janus-Node-02 | 4 | 1/4 (incomplete) | **4/4 정확** | 4/4 description+도면 일치 | **incomplete → complete, LINE COUNT GUARD 효과** |

## 1. v9 vs v8 라인별 비교

### Q29 / Demeter-Prime-01 — v9 fail

```
v9 answer (XML tool_call 그대로):
<tool_call><function=execute_cli_command><parameter=device_name>Demeter-Prime-01</parameter><parameter=command>display lldp neighbor brief</parameter></function></tool_call>

v9 status=forced_answer, iter=4, tools=4, dur=30.2s
```

**원인**: 모델이 4 iter 만에 답을 도출하지 못하고 tool_call 형식을 답으로 출력. validation_retry 가 작동했어야 하나 forced_answer 분기로 빠진 듯.

**대안 답 (cli.py 검증 결과 — Q29_topology_PJ.md)**:
```
Demeter-Prime-01(GE1/0/0)->Atlas-Prime-01(GE1/0/2)
Demeter-Prime-01(GE1/0/1)->Atlas-Prime-02(GE1/0/2)
Demeter-Prime-01(GE1/0/5)->Hermes-Prime-01(GE1/0/4)
```
ARP MAC 양방향 검증 + 도면 line 51,55-57 일치. **이 답을 v9 제출본의 Q29 로 사용 권장**.

### Q30 / Atlas-Prime-01 — v8 = v9 (둘 다 정확)

```
Atlas-Prime-01(GE1/0/0)->Janus-Prime-01(GE1/0/0)   ← 도면 line 41
Atlas-Prime-01(GE1/0/1)->Janus-Prime-02(GE1/0/0)   ← 도면 line 42
Atlas-Prime-01(GE1/0/2)->Demeter-Prime-01(GE1/0/0) ← 도면 line 56 (역)
Atlas-Prime-01(GE1/0/3)->Demeter-Prime-02(GE1/0/0) ← 도면 line 38 (역)
```

원래 description 이 정확명 사용 → v8/v9 둘 다 무리 없이 도출.

### Q31 / Janus-Prime-01 — v9 6/6 정확, v8 6/6 잘못 ⭐

| 포트 | v8 | v9 | 도면 truth | 평가 |
|---|---|---|---|---|
| GE1/0/0 | Alpha-Center-01 | **Atlas-Prime-01** | Atlas-Prime-01(GE1/0/0) | ✅ alias "Spine1" 해소 |
| GE1/0/1 | Beta-Axis-02 | **Atlas-Prime-02** | Atlas-Prime-02(GE1/0/0) | ✅ alias "Spine2" 해소 |
| GE1/0/2 | Core-01 | **PX1** | PX1(GE1/0/0) | ✅ description 정확명 사용 |
| GE1/0/3 | Core-02 | **Aegis-Prime-02** | Aegis-Prime-02(GE1/0/2) | ✅ description 없는 포트도 도면대로 도출 |
| GE1/0/4 | Core-02 | **Janus-Prime-02** | Janus-Prime-02(GE1/0/4) | ✅ |
| GE1/0/5 | Edge-01 | **Aegis-Prime-01** | Aegis-Prime-01(GE1/0/2) | ✅ |

**TODO-03 (whitelist + ALIAS WARNING) 패치의 결정적 검증 사례**. v8 의 모든 alias/hallucination 이 도면 정답으로 교정됨.

### Q32 / Aegis-Prime-01 — 부분 개선

| 포트 | v8 | v9 | 도면 / description | 평가 |
|---|---|---|---|---|
| GE1/0/0 | Aegis-Prime-02(ETH1/0/0) | **Janus-Prime-02(GE1/0/5)** | 도면 line 50 = Janus-Prime-02 GE1/0/5 | ✅ alias "BorderLeaf2" 해소 |
| GE1/0/1 | Aegis-Prime-02(ETH1/0/1) | Aegis-Prime-02(GE1/0/1) | description 정확명 | ✅ 둘 다 정확 |
| GE1/0/2 | (누락) | (누락) | 도면 line 49 = Janus-Prime-01 GE1/0/5, description 잘림("to") | ❌ 양쪽 모두 누락 |
| GE1/0/3 | Aegis-Prime-02(ETH1/0/1) | **Eon-Node-01(GE1/0/1)** | description = "PJlAN-01-GE1/0/1" (alias) | ❓ Eon-Node-01 이 PJlAN-01 alias 인지 확인 필요 |

부분 개선. GE1/0/2 누락은 description 손상("to" 잘림)과 도면 미반영의 복합 문제.

### Q33 / Janus-Node-02 — v9 4/4 정확, v8 1/4 incomplete ⭐

| 포트 | v8 | v9 | description | 평가 |
|---|---|---|---|---|
| GE1/0/2 | (누락) | **Atlas-Node-01(GE1/0/2)** | description 일치 | ✅ LINE COUNT GUARD 로 추가 |
| GE1/0/3 | (누락) | **Atlas-Node-02(GE1/0/2)** | description 일치 | ✅ |
| GE1/0/4 | Aegis-Node-01(GE1/0/1) | Aegis-Node-01(GE1/0/1) | description 일치 | ✅ 둘 다 정확 |
| GE1/0/5 | (누락) | **Janus-Node-01(GE1/0/5)** | description + 도면 line 58 | ✅ |

**TODO-05 (LINE COUNT GUARD) 패치의 결정적 검증 사례**. incomplete 답이 4 라인 완전 답으로 교정됨. dur=751.7s 로 긴 시간 소요 (validation retry).

## 2. 패치 효과 종합

### TODO-03 (Topology hint whitelist + ALIAS WARNING)
- **명확히 작동**: Q31 의 6/6 alias hallucination 완전 제거
- Q32 의 2/3 alias 해소 (BorderLeaf2 → Janus-Prime-02, PJlAN-01 → Eon-Node-01 [확인 필요])
- 부작용 없음

### TODO-05 (LINE COUNT GUARD + validate_topology_answer + retry)
- **명확히 작동**: Q33 의 1 라인 → 4 라인 incomplete 해결
- Q30 의 forced_answer 도 4 라인 정확 답을 도출 (단 retry 가 너무 길어 forced_answer 처리)
- Q29 에서는 retry 가 약효 없이 fail → **추가 가드 필요 (TODO-07?)**

### Q29 실패의 의미
- agent.py 의 forced_answer 트리거가 validate_topology_answer 의 retry 와 충돌 가능성
- 또는 모델이 4 iter 만에 답 도출 포기 → 조기 종료
- run.log 가 생성되지 않아 자세한 trace 없음

## 3. v9 제출본 생성 권장 (Q29 처리 옵션)

| 옵션 | Q29 답 | 신뢰도 | 비고 |
|---|---|---|---|
| A. cli.py 수동 검증 결과 사용 (권장) | `Demeter-Prime-01->Atlas-Prime-01/02/Hermes-Prime-01` | 높음 (ARP MAC 양방향 + 도면 일치) | 라인 수 3, 도면 100% 일치 |
| B. v8 정답 유지 | `->Spine2/Spine1/PC1` (alias) | 낮음 (alias 사용) | 채점에서 fail 가능성 |
| C. Q29 만 재실행 | (재실행 결과) | 중간 (또 fail 가능) | 추가 시간·토큰 소모 |

**옵션 A 권장** — cli.py 검증 결과는 ARP MAC 양방향 매칭(MAC `3877-7111-0100/0101`) + 도면 직접 매칭으로 가장 객관적 증거.

## 4. 후속 (TODO 추가)

| ID | 제목 | 우선순위 |
|---|---|---|
| TODO-07 | Q29 재실패 원인 분석 (forced_answer 트리거 vs validation retry 충돌) | Medium |
| TODO-08 | Eon-Node-01 / PJlAN-01 alias 매핑 확인 (Q32 GE1/0/3) | Low |
| TODO-09 | description 잘림(예: Aegis-Prime-01 GE1/0/2 = "to") 케이스 별도 처리 | Low |
| TODO-10 | v9 제출본 (CSV) 생성 + Zindi 제출 | Medium |
