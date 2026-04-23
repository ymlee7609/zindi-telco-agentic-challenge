# Track A — Phase 1 문제 분석 (2000 train + 500 test)

> 5G drive test optimization scenarios
> 모든 문제는 동일한 task description 을 공유하지만 데이터가 다름
> 최종 업데이트: 2026-04-22

---

## 1. 개요

| 데이터셋           | scenario 수 | answer 포함                         | 용도                    |
| -------------- | ---------- | --------------------------------- | --------------------- |
| **train.json** | 2000       | YES (예: `C9`, `C2\|C8\|C11\|C16`) | Few-shot, 로컬 정확도 검증   |
| **test.json**  | 500        | placeholder `"To be determined"`  | Phase 1 submission 대상 |

### 1.1 Tag 분포 (train 2000 전수 통계)

| tag | 개수 | 비율 | 답변 양식 |
|-----|------|------|----------|
| `single-answer` | 1701 | 85.0% | `\boxed{C9}` (1 옵션) |
| `multiple-answer` | 299 | 14.9% | `\boxed{C2\|C8\|C11\|C16}` (2 또는 4 옵션, 오름차순) |

**Multiple-answer 옵션 수 분포**:
- **2 options**: 228개 (76%)
- **4 options**: 71개 (24%)
- **3 options**: 0개 ← **3 옵션 답은 없음** (system prompt 에서 강조 가능)

### 1.2 특수 패턴 정답 비율 (train 2000)

| 패턴                                             | 정답 수 | 비율         |
| ---------------------------------------------- | ---- | ---------- |
| P7 "Insufficient data; more data is needed"    | 252  | **12.60%** |
| P5 "Check test server and transmission issues" | 239  | **11.95%** |
| 기타 (P1~P4, P6 조치성 답변)                          | 1509 | 75.45%     |

→ **P7 + P5 합쳐 24.6%** 가 "특수 결정 (정형 action 아님)". 나머지 75% 가 tilt/azimuth/power/A3 조정 중 선택.

### 1.3 Single-answer 값 분포 (top 10)

가장 흔한 single-answer 값 (C1~C22 거의 고르게 분포, 80~94개/2000):

| 답 | 빈도 | 답 | 빈도 |
|----|------|----|----|
| C14 | 94 | C13 | 83 |
| C15 | 91 | C16 | 82 |
| C22 | 87 | C21 | 81 |
| C11 | 85 | C20 | 81 |
| C12 | 84 | C10 | 80 |

→ C# 자체는 각 scenario 에서 무작위 매핑이므로 **답 값 빈도는 분류에 무관**. 의미는 label 에 있음.

---

## 2. 모든 문제의 공통 task

> "Analyze 5G network drive test data.
> Identify actionable steps to mitigate or resolve performance issues arising from
> a significant degradation in user throughput observed during drive testing.
> Select {the most appropriate | two to four possible} optimization solution(s)
> and enclose its/their number(s) in `\\boxed{}`."

22개 안팎의 옵션 (C1~C22) 가 주어지고, 그 중 정답은 1개 (single) 또는 2~4개 (multiple).

---

## 3. 7-Pattern Library (.moai/plans/track-a-opus-solutions.md §4 발췌)

Opus 가 train 10 + traces 2 (총 12개) 를 수작업 풀이 (9/10 정답) 하며 도출한 패턴 분류.

### P1 — LATE HANDOVER (서빙 측 A3 너무 높음)

| 트리거 | 답변 카테고리 |
|--------|--------------|
| Serving PCI 가 throughput 저하 구간 내내 유지 + 서빙 cell A3Offset ≥ 10 (5 dB) + 충분히 강한 neighbor 존재 | **"Decrease A3 Offset threshold for `<serving cell>`"** |

예: traces.json[0] (`C9`), train[2] (`C16`), train[5] (`C8`).

### P2 — PING-PONG (두 셀 사이 왕복)

| 트리거 | 답변 카테고리 |
|--------|--------------|
| Serving PCI 가 A↔B 반복 + 두 셀 모두 A3Offset 낮음 (보통 2 = 1 dB) | **"Increase A3 Offset threshold for `<one or both>`"** |

예: train[0] 의 `C16` (3267220_2 의 A3Off 증가).

### P3 — OVERSHOOT INTERFERENCE (간섭)

| 트리거 | 답변 카테고리 (multiple) |
|--------|------------------------|
| SINR < 5 dB (또는 음수) + 특정 원거리 cell 이 Top neighbor 로 지속 등장 + 그 cell 이 high power / low downtilt | **2~4 옵션 조합**: `Decrease power` + `Press down tilt` + `Increase A3 Offset` (+ 때로 `Adjust azimuth`) |

예: train[0] 의 `C2|C8|C11`, train[10] (`C3|C12`), train[25] (`C3|C4`).

### P4 — COVERAGE HOLE

| 트리거 | 답변 카테고리 (multiple) |
|--------|------------------------|
| Serving RSRP ≤ -100 dBm + 모든 neighbor 도 약함 + 적절한 서빙 cell 의 power 가 max 미만 | `Increase power` + `Adjust azimuth` 조합 (또는 `Lift tilt`) |

예: train[17] (`C3|C14` — Adjust azimuth + Increase power for 3273494_1).

### P5 — SERVER / TRANSMISSION ISSUE

| 트리거 | 답변 |
|--------|------|
| SINR ≥ 10 dB (양호) + Throughput 만 변동 큼 + MR 데이터에 randomness | **"Check test server and transmission issues"** |

예: train[1] (`C9`), train[3] (`C10`).

### P6 — EXCESSIVE DOWNTILT ON COVERAGE NEIGHBOR

| 트리거 | 답변 |
|--------|------|
| SINR 양호하지만 throughput 낮음 + UE 위치 커버해야 할 neighbor cell RSRP ≤ -100 dBm + 그 cell 의 총 downtilt (Mechanical + Digital) ≥ 20° | **"Lift the tilt angle of `<that neighbor cell>`"** |

예: train[4] (`C3` — Lift tilt of 3255225_2 by 7°). 이 패턴이 가장 어려움 — Opus 도 초기엔 P5 로 오판.

### P7 — INSUFFICIENT DATA

| 트리거 | 답변 |
|--------|------|
| 모든 지표 정상 범위, anomaly 없음 | **"Insufficient data; more data is needed for judgment."** |

예: train[6] (`C9`). 억지 진단 금지의 안전망. agent.py 의 fallback 으로도 사용 (prediction 비면 자동 P7 옵션 선택).

---

## 4. 패턴별 옵션 매핑 표

옵션 22개 중 정답이 어떤 패턴에 매핑되는지 결정 트리:

```
1. Throughput 저하 구간 정의 (TP < 100 Mbps 연속 ≥3 샘플)
2. 그 구간의 Serving PCI 추적
   ├─ 같은 PCI 유지 + 강한 neighbor 존재 → P1 Late HO
   ├─ A↔B 반복 → P2 Ping-pong
   └─ 분산
3. SINR 분석
   ├─ < 5 dB or negative → P3 Overshoot (overshooting cell 식별)
   ├─ ≥ 10 dB + Throughput 변동 큼 → P5 Server
   └─ ≥ 10 dB + Coverage 의심 → P4 / P6
4. Serving RSRP
   ├─ ≤ -100 + neighbor 모두 약함 → P4 Coverage hole
   └─ 보통 + 특정 neighbor cell 매우 약함 + 그 cell tilt ≥ 20° → P6
5. 어떤 패턴도 매칭 안 되면 → P7 Insufficient
```

---

## 5. 실행 결과 (Stage C 진행 중)

### 5.1 Smoke 10 (test.json) — 2026-04-22

- 10/10 solved status
- prediction 추출률: **7/10** (3건 empty — XML 오염 + reasoning 폭주 → P7 fallback 도입)
- 평균 latency 35.6s, iterations 4.4, tool calls 7.7
- test 의 answer 가 placeholder 라 정확도 측정 불가

### 5.2 Train eval 10 (baseline v1, 로컬 검증) — 2026-04-22

| 지표 | 값 |
|------|-----|
| Total | 10 |
| Exact match | 3 (30%) |
| Partial IoU | 1 (10%) |
| Wrong (IoU=0) | 6 (60%) |
| Mean IoU | 0.325 |

Smoke 게이트 (≥0.3) 통과.

### 5.3 Train eval 50 (baseline v1) — 2026-04-22 (N=50 의 통계적 신뢰도 ↑)

| 지표 | 값 |
|------|-----|
| Total | 50 |
| Exact match | **8 (16.0%)** |
| Partial IoU | 3 (6%) |
| Wrong (IoU=0) | 39 (78%) |
| P7 fallback 사용 | **19 (38%)** |
| **Mean IoU** | **0.180** ← Pilot 게이트 ≥0.4 실패 |

per-tag:
- single-answer (42): exact 8/42 (19%), mean IoU 0.19
- multiple-answer (8): exact **0/8**, mean IoU 0.125 ← multi 는 완전 실패

### 5.4 오답 패턴 분석 (Wrong 39 / 50)

| 원인 | 빈도 | 대응 |
|------|------|------|
| XML `<tool_call>` 오염 → content 에 XML → empty → P7 fallback | ≈19 | agent.py XML 감지 재질의 추가 (v2) |
| Qwen 이 잘못된 패턴 인식 (evidence 있지만 오판) | ≈15 | RAG 도입 (v3) — 유사 train scenario few-shot 주입 |
| Multi-answer 에서 1개만 답변 (format 오류) | ≈5 | system prompt 의 "multi 는 반드시 2~4" 강조 (v2) |

### 5.5 Pilot 50 (test.json, v1 agent) — 2026-04-22

- 50/50 solved status
- Empty raw prediction: **0** (P7 fallback 23건 = 46%)
- 21 distinct predictions, 모두 single-answer 형식
- 평균 latency 33.9s, iters 4.8, tool calls 8.7
- `submission_pilot_v0.csv` 생성 → `agent/common/submission/submission_combined.csv` Track A 열 50/550

### 5.6 개선 전략 (v4 완료 → Zindi 0.3174 달성)

| 버전 | 변경점 | 실측 효과 (train 50) |
|------|--------|---------------------|
| v1 | baseline (7-pattern system prompt + 5 static few-shot) | IoU 0.160, fb 22/50 |
| v2 | XML 감지 재질의 + multi-answer 강제 규칙 | IoU 0.100 (regression) |
| v3 | RAG 도입 — 14-dim 특징 + train 2000 L2 retrieval | IoU 0.220, fb 18/50 (+38%) |
| **v4 (현재)** | **P0 (XML recovery + multi retry + P7 억제) + P1 (XML budget 분리, max_iter 25) + P2 (RAG 22-dim + feature_hint + SC)** | **IoU 0.3173, fb 5/50** (+44% vs v3, +98% vs v1) |
| v5 (후보) | LoRA fine-tuning on train 2000 | Phase 3 대비 |

### 5.7 Test 500 최종 실행 (submission_v1 → v2_sc 전환, 2026-04-23)

**v1 (구, Zindi 0.149):**
| Batch | 범위 | 실행 | 완료 | P7 fallback | Avg latency |
|-------|------|------|------|-------------|-------------|
| Pilot v3 | test 0-49 | 2026-04-22 | 50/50 | 22 (44%) | 27.4s |
| Batch A | test 50-249 | 2026-04-23 | 200/200 | 134 (67%) | 38.4s |
| Batch B | test 250-499 | 2026-04-23 | 250/250 | 187 (75%) | 31.2s |
| **합계** | test 0-499 | — | 500/500 | **343 (68.6%)** | 32.3s |

**v2_sc (현재, Zindi 0.3174):**
| Batch | 범위 | 실행 | 완료 | fallback_used | Avg latency |
|-------|------|------|------|---------------|-------------|
| Batch v2 A | test 0-249 | 2026-04-23 | 250/250 | - | 85s (serial) |
| Batch v2 B | test 250-499 | 2026-04-23 | 250/250 | - | 57s (serial) |
| v2 base 소계 | test 0-499 | — | 500/500 | **43 (8.6%)** | 75s |
| SC overlay (n=3) | fallback 43건 | 2026-04-23 | 43/43 | **0 (0%)** | (추가 ~1.5h) |
| **v2_sc 최종** | test 0-499 | — | 500/500 | **0 (0%)** | - |

**Multi 예측 분포 변화:**
- v1: 3/500 (0.6%) — 심각한 under-prediction
- v2 base: 62/500 (12.4%)
- **v2_sc: 67/500 (13.4%)** ← test.json 실제 multi=67 과 정확히 일치

**제출물:**
- v1: `agent/track_a/submission/submission_v1.csv` — 보존
- **v2_sc: `agent/track_a/submission/submission_v2_sc.csv` (최종 제출본)**
- 통합: `agent/common/submission/submission_combined.csv` 의 Track A 열이 v2_sc 로 갱신됨

---

## 6. 알려진 어려운 케이스

| 케이스 | 어려운 이유 | 대응 방안 |
|--------|------------|----------|
| P3 Overshoot multi-answer | 4개 옵션 중 정확 조합 매칭이 어려움 (overshoot cell 식별 + 어느 조치 조합) | few-shot 에 train[0] 포함, A3Off + Power + Tilt 의 3-tuple 강조 |
| P6 Excessive downtilt | SINR 양호 + tilt ≥20° 이라는 두 조건을 동시 검출 어려움. P5 Server 와 혼동 | system prompt 의 P6 트리거에 "Mechanical Downtilt + Digital Tilt ≥ 20°" 명시 |
| Insufficient data 옵션 누락 | 모든 scenario 옵션에 P7 카테고리 라벨이 약간씩 다름 | `insufficient_data_option()` 헬퍼가 label 부분 일치 (`"insufficient data" in label.lower()`) 로 식별 |
| `\boxed{}` 미생성 | Qwen 이 reasoning 만 하고 final content 비움 | (1) MAX_TOKENS=8192, (2) forced_answer 재시도, (3) prediction 비면 P7 fallback |
| XML `<tool_call>` 오염 | Qwen 이 native tool_calls 대신 inline XML 생성 → tool 미실행 | system prompt Protocol Rules 에 "NEVER inline XML" 강조 |

---

## 7. 다음 단계 (v2_sc 이후, Phase 1 데드라인 2026-05-04)

**완료된 개선 (v1 0.149 → v2_sc 0.3174):**
1. ✅ P0 XML recovery + multi retry + P7 억제 → fallback 68% → 8.6%
2. ✅ P1 XML budget 분리, max_iter 25, tag별 system prompt → max_iter 소진 55% → 1%
3. ✅ P2 RAG 22-dim + feature_hint + self-consistency → IoU 0.317 (test 0.3174)

**후속 실험 후보:**
1. **RAG feature 추가** (22 → 30+ dim): traffic_data, signaling_plane_data, MR variance
2. **Ensemble**: HuggingFace/DashScope provider 투표 (Qwen 인스턴스 3개)
3. **LoRA fine-tuning**: train 2000 으로 Qwen3.5-35B-A3B 파인튜닝 (Phase 3 대비)
4. **Embedding retrieval**: BAAI/bge-m3 로 scenario JSON → embedding 변환
5. **Self-consistency 전역 적용**: 현재 fallback 43건에만 적용 → 전체 500건 n=3 (비용 3x)

진행 리포트: `08_track_a_progress.md`
개선 계획: `.moai/plans/track-a-0-149-track-shimmying-pascal.md`

---

## 8. 참고 파일

- 원본 데이터: `data/Track A/data/Phase_1/{train,test}.json`
- Opus 풀이 + 패턴 라이브러리: `.moai/plans/track-a-opus-solutions.md`
- 에이전트 구조: `03-1_architecture.md`
- 무선 토폴로지/RF 용어: `03-2_topology.md`
- 진행 리포트: `08_track_a_progress.md`
- 추출 헬퍼: `agent/track_a/tools/scenario_summary.py`
