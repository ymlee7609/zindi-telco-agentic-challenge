# TODO-04 결과 — PJ Topology Q30~Q33 v8 정답 sample 검증

| 항목 | 값 |
|---|---|
| 작업 일자 | 2026-04-22 |
| 검증 대상 | Q30~Q33 (PJ area Topology, Q29 와 동일 영역) |
| 검증 방법 | 도면(03-2_topology_pj.d2) + cache description (cli.py 권한 차단으로 cache 직접 읽기) |
| 결론 | **4문제 중 1문제만 v8 정답 정확 (Q30), 나머지 3문제 모두 alias 또는 누락** |

## 0. 한눈에 보는 결과

| Q | target | UP 포트 수 | v8 라인 수 | 결론 | 주요 원인 |
|---|---|---|---|---|---|
| Q30 | Atlas-Prime-01 | 4 | 4 | **일치** | description 이 정확명 (To-Janus-Prime-01-...) |
| Q31 | Janus-Prime-01 | 6(물리) | 6 | **불일치** | v8 답이 description·도면 모두와 다른 alias (Alpha-Center, Core, Edge) — 다른 source 추정 |
| Q32 | Aegis-Prime-01 | (Eth-Trunk) | 3 | **불일치** | 1/3 일치(Aegis-Prime-02), 2/3 잘못(BorderLeaf2 등 alias 사용 안 함), 1개 누락 |
| Q33 | Janus-Node-02 | 4(물리) | 1 | **불일치 (incomplete)** | description 정확명이지만 v8 가 4 UP 중 1 라인만 답함 |

## 1. Q30 / Atlas-Prime-01 — **일치**

### description (cache: `data/Track B/devices_outputs/30/Atlas-Prime-01/display_current-configuration.txt`)
```
GE1/0/0  description To-Janus-Prime-01-GE1/0/0
GE1/0/1  description To-Janus-Prime-02-GE1/0/0
GE1/0/2  description To-Demeter-Prime-01-GE1/0/0
GE1/0/3  description To-Demeter-Prime-02-GE1/0/0
GE1/0/5  description To-H3C-BL3-GE1/0           ← alias, 그러나 GE1/0/5 는 DOWN
```

### UP 포트 (interface brief): GE1/0/0, GE1/0/1, GE1/0/2, GE1/0/3

### v8 정답
```
Atlas-Prime-01(GE1/0/0)->Janus-Prime-01(GE1/0/0)   ✓
Atlas-Prime-01(GE1/0/1)->Janus-Prime-02(GE1/0/0)   ✓
Atlas-Prime-01(GE1/0/2)->Demeter-Prime-01(GE1/0/0) ✓
Atlas-Prime-01(GE1/0/3)->Demeter-Prime-02(GE1/0/0) ✓
```

### 결론
description 이 모두 정확명을 사용했고 v8 가 그대로 옮김. **alias 영향 없음**. GE1/0/5 (alias) 는 DOWN 이라 답에 포함 안 됨 — 정확.

## 2. Q31 / Janus-Prime-01 — **모든 라인 잘못**

### description
```
GE1/0/0  description To-Spine1-GE1/0/0           ← alias
GE1/0/1  description To-Spine2-GE1/0/0           ← alias
GE1/0/2  description To-PX1                      ← 정확명
GE1/0/3  (description 없음)
GE1/0/4  description To-Janus-Prime-02-GE1/0/4   ← 정확명
GE1/0/5  description To-Aegis-Prime-01-GE1/0/2   ← 정확명
```

### 도면 (line 41-49)
```
GE1/0/0 -> Atlas-Prime-01(GE1/0/0)
GE1/0/1 -> Atlas-Prime-02(GE1/0/0)
GE1/0/2 -> PX1(GE1/0/0)
GE1/0/3 -> Aegis-Prime-02(GigabitEthernet1/0/2)
GE1/0/4 -> Janus-Prime-02(GE1/0/4)
GE1/0/5 -> Aegis-Prime-01(GigabitEthernet1/0/2)
```

### v8 정답 vs 도면
| 포트 | v8 | 도면 (truth) | description | 평가 |
|---|---|---|---|---|
| GE1/0/0 | `Alpha-Center-01(GE1/0/0)` | Atlas-Prime-01(GE1/0/0) | "Spine1" | ❌ v8 가 **다른 zone(Big Data) 장비명** 사용 |
| GE1/0/1 | `Beta-Axis-02(GE1/0/1)` | Atlas-Prime-02(GE1/0/0) | "Spine2" | ❌ v8 가 **다른 zone(Dev&Test) 장비명** 사용 |
| GE1/0/2 | `Core-01(GE1/0/1)` | PX1(GE1/0/0) | "PX1" | ❌ v8 가 description 무시하고 alias `Core-01` 생성 |
| GE1/0/3 | `Core-02(GE1/0/2)` | Aegis-Prime-02(GigabitEthernet1/0/2) | (none) | ❌ alias `Core-02` |
| GE1/0/4 | `Core-02(GE1/0/3)` | Janus-Prime-02(GE1/0/4) | "Janus-Prime-02" | ❌ description 무시 + 중복 alias |
| GE1/0/5 | `Edge-01(GE1/0/1)` | Aegis-Prime-01(GigabitEthernet1/0/2) | "Aegis-Prime-01" | ❌ description 무시 + alias `Edge-01` |

### 결론
**6/6 모두 잘못**. 특히 GE1/0/2~5 는 description 이 정확명을 가지고 있는데도 v8 가 무시하고 alias(`Core-01/02`, `Edge-01`) 를 생성. GE1/0/0,1 의 `Alpha-Center-01`, `Beta-Axis-02` 는 PJ 영역에 없는 장비명 — **v8 모델이 다른 zone 의 장비명을 hallucinate 한 것** 또는 다른 source 데이터에서 추출한 것으로 추정.

### 새 alias 매핑 발견 (Q29 결과 보완)

| description alias | 실제 장비 (도면 기준) | 출처 |
|---|---|---|
| Spine1 (Q31 Janus-Prime-01 GE1/0/0) | **Atlas-Prime-01** | 도면 line 41 |
| Spine2 (Q31 Janus-Prime-01 GE1/0/1) | **Atlas-Prime-02** | 도면 line 42 |
| Spine2 (Q29 Demeter-Prime-01 GE1/0/0) | **Atlas-Prime-01** | 도면 line 56 |
| Spine1 (Q29 Demeter-Prime-01 GE1/0/1) | **Atlas-Prime-02** | 도면 line 57 |

→ **alias "Spine1/Spine2" 가 노드마다 다른 장비를 가리킴** (Q29 의 Spine1/2 와 Q31 의 Spine1/2 가 정반대). alias 는 **장비-로컬 라벨**이며 영역 통일 매핑 표가 없음. v8 모델이 이를 인지하지 못함.

## 3. Q32 / Aegis-Prime-01 — **부분 일치 + 누락**

### description
```
Eth-Trunk2             description To-BL2-Eth-Trunk3            ← alias
GigabitEthernet1/0/0   description To-BorderLeaf2-GE1/0/5       ← alias (Janus-Prime-02)
GigabitEthernet1/0/1   description To-Aegis-Prime-02-GE1/0/1    ← 정확명 (도면에는 없음)
GigabitEthernet1/0/2   description to                           ← truncated
GigabitEthernet1/0/3   description To-PJlAN-01-GE1/0/1          ← alias
```

### 도면
```
GigabitEthernet1/0/0 -> Janus-Prime-02(GE1/0/5)   (line 50)
GigabitEthernet1/0/2 -> Janus-Prime-01(GE1/0/5)   (line 49)
```
※ 도면이 incomplete — Aegis-Prime-02 link, Eth-Trunk 등 표시 안 됨

### v8 정답 vs description + 도면

| v8 라인 | description | 도면 | 평가 |
|---|---|---|---|
| `ETH1/0/3->Aegis-Prime-02(ETH1/0/1)` | "PJlAN-01-GE1/0/1" | (없음) | ❌ description 의 alias 무시, Aegis-Prime-02 사용 (도면에 없는 link) |
| `ETH1/0/0->Aegis-Prime-02(ETH1/0/0)` | "BorderLeaf2-GE1/0/5" | Janus-Prime-02 GE1/0/5 | ❌ description·도면 모두 무시 |
| `ETH1/0/1->Aegis-Prime-02(ETH1/0/1)` | "Aegis-Prime-02-GE1/0/1" | (없음) | ✓ description 일치 |

ETH1/0/2 (description truncated, 도면 = Janus-Prime-01) → **v8 답에 누락**

### 결론
**1/3 일치 + 1개 누락 + 2개 잘못**. v8 가 description 과 도면 양쪽에 어긋나는 답을 생성한 라인이 다수.

## 4. Q33 / Janus-Node-02 — **답 incomplete (1/4)**

### description (모두 정확명)
```
GE1/0/2  description To-Atlas-Node-01-GE1/0/2     ← 정확
GE1/0/3  description To-Atlas-Node-02-GE1/0/2     ← 정확
GE1/0/4  description To-Aegis-Node-01-GE1/0/1     ← 정확
GE1/0/5  description To-Janus-Node-01-GE1/0/5     ← 정확
```

### UP 포트 (interface brief): GE1/0/2, GE1/0/3, GE1/0/4, GE1/0/5 + Eth-Trunk

### v8 정답 (단 1 라인)
```
Janus-Node-02(GE1/0/4)->Aegis-Node-01(GE1/0/1)   ✓ description 정확 매칭
```

### 결론
description 이 모두 정확명을 가지고 있으므로 v8 가 4 라인 모두 정확히 답할 수 있었어야 함. 그러나 **GE1/0/4 한 라인만 답하고 GE1/0/2, GE1/0/3, GE1/0/5 누락**. 모델이 답 도출을 도중에 중단한 것으로 추정 (early stop).

## 5. 종합 결론

### 5-1. v8 PJ Topology 신뢰도

| Q | 결론 |
|---|---|
| Q29 | 부분일치 (Q29 의 ARP 매칭으로 사실은 cli.py 결과가 정확, v8 의 alias 그대로 사용) |
| Q30 | **일치** |
| Q31 | **불일치 — 6/6 라인 모두 잘못** |
| Q32 | **불일치 — 1/3 정답, 1/3 잘못, 1/3 누락** |
| Q33 | **불일치 — incomplete (1/4)** |

→ **PJ Topology 5문제 중 1문제만 v8 정답 신뢰 가능**.

### 5-2. 실패 패턴 분류

1. **description alias 그대로 사용** (Q29 Spine1/Spine2/PC1)
2. **description 이 정확명이어도 무시하고 다른 alias hallucinate** (Q31 GE1/0/4 description="Janus-Prime-02" 인데 v8="Core-02")
3. **다른 zone 의 장비명 hallucinate** (Q31 GE1/0/0 v8="Alpha-Center-01" — Big Data Zone 장비)
4. **답 incomplete** (Q33 4 UP 포트 중 1 라인만 답함)

### 5-3. TODO-03 패치 효과 예상

방금 적용한 TODO-03 (Topology hint whitelist + ALIAS WARNING) 패치 효과:
- 패턴 1 (alias 사용): **해결 가능** — whitelist 외 라벨을 alias 로 인식
- 패턴 2 (정확명 무시): **해결 가능** — whitelist 검증으로 description 의 정확명을 확신
- 패턴 3 (다른 zone hallucination): **해결 가능** — whitelist 가 PJ 영역 23 device 만 명시
- 패턴 4 (incomplete answer): **별도 가드 필요** — Topology hint 에 "UP 포트 수와 답 라인 수가 일치해야 함" 명시 필요

→ **추가 TODO-05 권장**: Topology hint 에 "답 라인 수 = UP 물리 포트 수" 검증 가드 추가

## 6. 후속 (TODO 갱신 권장)

| ID | 추가/갱신 | 우선순위 |
|---|---|---|
| TODO-05 (신규) | Topology hint 에 "답 라인 수 = UP 포트 수" 가드 + post-validation | Medium |
| Q29~Q33 재실행 | TODO-03 패치 효과 측정 (v9 제출본 생성) | Medium |
| Q34~Q38 (PJ Path) sample | Path 분기는 이미 whitelist 주입돼 있어 영향 적음 — 1-2개 sample 만 확인 | Low |
