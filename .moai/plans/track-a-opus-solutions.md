# Track A — Opus 에뮬레이션 수작업 풀이 (Stage A 산출물)

> 작성: 2026-04-22
> 목적: train 10개 + traces 2개를 Opus 4.7 수작업으로 풀어보며 Qwen 용 system prompt, few-shot, 풀이 정석을 증류
> 샘플: train[0, 1, 2, 3, 4, 5, 6, 10, 17, 25] + examples/traces.json 2건
> 결과 요약: **내 예측 9/10 정답** (train[4] 만 Opus 도 처음엔 server 문제로 오판 — coverage tilt lift 패턴 추가 학습 필요)

---

## 1. 문제 패턴 공통 구조

모든 scenario 는 동일한 user message 를 가진다:

> "Analyze 5G network drive test data. Identify actionable steps to mitigate or resolve performance issues arising from a significant degradation in user throughput observed during drive testing. Select {the most appropriate | two to four possible} optimization solution(s) and enclose its/their number(s) in \\boxed{{}}."

Options 는 C1~C22 (때로 C20) 범위, 공통 카테고리:
- **Tilt 조정**: Lift / Press down, X degrees, 해당 cell
- **Azimuth 조정**: Adjust by X degrees, 해당 cell
- **Transmission Power**: Increase / Decrease, 해당 cell
- **A3 Offset**: Increase / Decrease, 해당 cell (handover threshold)
- **Cov Thld**: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds
- **PdcchOccupiedSymbolNum**: Modify to 2SYM (PDCCH capacity)
- **Neighbor Relation**: Add neighbor relationship between X and Y
- **Server**: "Check test server and transmission issues"
- **Insufficient**: "Insufficient data; more data is needed for judgment."

Scenario 는 2~5 cell 정보 + drive test CSV 시계열 (10~15 샘플) + signaling events + hourly traffic KPI + mobile report (MR) 데이터를 포함. **모든 데이터 inline** — train/test 모두 scenario.data 필드에 self-contained.

---

## 2. 풀이 정석 (Decision Tree)

```
1. Drive test throughput 시계열에서 저역 (< 100 Mbps) 구간 탐지
2. 저역 구간의 Serving PCI 추적 (유지 vs 변경)
3. Serving RSRP/SINR 패턴 확인:
   - SINR < 5 dB 또는 음수  → 간섭 (interference) 문제
   - SINR ≥ 10 dB 이면서 Throughput 낮음 → (a) 서버/백홀 문제 or (b) coverage 문제
4. Neighbor PCI RSRP 확인:
   - Neighbor RSRP > Serving RSRP + (A3Offset × 0.5) + (A3Hyst × 0.5)  → Handover 가 트리거되었어야 함
   - 서빙 유지 + 강한 이웃 존재 → Late handover → A3 Offset 조정
5. Ping-pong: serving PCI 가 A↔B 반복 → A3 Offset 증가
6. Overshoot: 특정 원거리 cell이 Top neighbor로 반복 등장 + SINR 저하 → 해당 cell 의 Power↓ / Tilt↓ / A3Off↑
7. Coverage hole: Serving RSRP ≤ -100 dBm, 모든 Neighbor 도 약함 → 가장 가까운 cell azimuth 재조정 / Power↑
8. 판별 불가 (SINR 적당 + RSRP 적당 + 모든 지표 안정) → "Insufficient data"
```

**핵심 공식**: A3 이벤트 조건 `Neighbor_RSRP > Serving_RSRP + (A3Offset × 0.5) + (A3Hyst × 0.5)`

| A3Offset (0.5dB unit) | Effective dB |
|-----------------------|--------------|
| 2 | 1.0 dB |
| 6 | 3.0 dB |
| 10 | 5.0 dB |

---

## 3. 10개 train 샘플 풀이

### train[0] — multi-answer — **정답 C2|C8|C11|C16 — 내 예측 ✓**

5 cell. Low throughput 6 samples, serving PCI 가 **166 ↔ 966 ping-pong** (둘 다 A3Off=2, 1 dB로 매우 낮음 → 빈번 handover).
Neighbor top 1/2 에 **PCI 420 (3279943_1)** 가 반복 등장 (원거리 overshoot), Power 18, Dtilt 10 이지만 Mtilt 만 1.

- **C2** Decrease power for 3279943_1 → overshoot 감소
- **C8** Press down tilt for 3279943_1 (by 4°) → 빔 하향
- **C11** Increase A3 Offset for 3279943_1 → handover 를 3279943_1 쪽으로 덜 가게
- **C16** Increase A3 Offset for 3267220_2 (PCI 966) → ping-pong 완화

### train[1] — single-answer — **정답 C9 "Check test server and transmission issues" — ✓**

Serving PCI 546 유지, RSRP -85~-93, **SINR 8~17 (양호)**. N1 RSRP -90~-96 (약함).
MR 데이터: TP 3.9, 15.9, 68.5, 224.6 (극심한 변동). RF 는 정상인데 throughput 이 randomly 튐 → **백홀/서버 불안정**.

### train[2] — single-answer — **정답 C16 "Decrease A3 Offset for 3213863_2" — ✓**

Serving PCI 156 (3213863_2), **A3Off=10 (5 dB)** 매우 높음. Neighbor PCI 236 RSRP -79~-83 (Serving -84~-88 보다 5~8 dB 강함). **SINR -1~-2 (매우 나쁨 — interference)**.
Neighbor 가 5 dB 강하지만 A3 조건 `neighbor - serving > 5+1 = 6 dB` 미달 → late handover → C16 decrease A3 offset.

### train[3] — single-answer — **정답 C10 "Check test server and transmission issues" — ✓**

Serving PCI 588 유지, RSRP -87~-92, **SINR 7~17 (양호)**. Neighbor 모두 약함 (-90~-102).
MR TP 13, 95, 83, 66 (변동) → train[1]과 동일 패턴의 server issue.

### train[4] — single-answer — **정답 C3 "Lift tilt of 3255225_2 by 7 degrees" — ❌ (Opus 초기 오판)**

Serving PCI 840, RSRP -86~-93, **SINR 7~18 (양호)**. 내 초기 예측은 C16 server issue.
**올바른 해석**: Neighbor PCI 488 (3255225_2) RSRP -99~-107 (매우 약함). 이 cell 은 **Mtilt 15 + Dtilt 9 = 총 24° downtilt** (극단적).
→ Coverage hole: PCI 488이 커버해야 할 영역에서 tilt 과다로 약함 → **Lift tilt** 로 coverage 회복.

**학습 포인트**: SINR 양호 + 이웃 cell RSRP 매우 약함 + 해당 이웃 cell 총 tilt ≥ 20° → **Lift tilt on that cell** 을 고려.

### train[5] — single-answer — **정답 C8 "Decrease A3 Offset for 3257709_1" — ✓**

Serving PCI 385 (3257709_1), **A3Off=10**. Neighbor PCI 821 RSRP -79~-85 (Serving -87~-92 보다 6~13 dB 강함). **SINR -2~-4**.
Serving A3 Offset 이 높아 handover 지연 → C8 decrease A3 offset. (train[2]와 유사 패턴, Serving 측 A3 조정)

### train[6] — single-answer — **정답 C9 "Insufficient data" — ✓**

Serving PCI 809, RSRP -86~-94, **SINR 10~17 (양호)**. Neighbor PCI 67 RSRP -87~-94 (서빙과 비슷). A3Off 모두 6 (3 dB) 정상.
어떤 지표도 명확한 이상 없음 → **Insufficient data** 선택.

**학습 포인트**: 명확한 anomaly 없으면 "Insufficient data" 가 정답. 억지 진단 금지.

### train[10] — multi-answer — **정답 C3|C12 "Decrease power + Press down tilt for 3220643_4" — ✓**

Serving PCI 866, **SINR 0~3 (간섭)**. Neighbor PCI 213 (3220643_4) RSRP -81~-88 (서빙과 비슷하게 강함 — overshoot 의심).
3220643_4 Pwr=24, Mtilt=0, Dtilt=8. Mtilt 0 이 특히 문제 (수평) → power down + tilt down 으로 간섭 축소.

### train[17] — multi-answer — **정답 C3|C14 "Adjust azimuth + Increase power for 3273494_1" — ✓**

Serving PCI 827 (3273494_1), **RSRP -100~-109 (매우 약함)**, SINR -1~2. 모든 neighbor 도 약함 (≤-103).
**Coverage hole**. 3273494_1 Az=307, Power 25 (max 30 아직 여유). UE 방향에 beam 안 향함 → **Azimuth 재조정 + Power 증가**.

### train[25] — multi-answer — **정답 C3|C4 "Decrease power + Press down tilt for 3232166_1" — ✓**

Serving PCI 422, **SINR 1~3 (간섭)**. Neighbor PCI 185 (3232166_1) RSRP -83~-91 (비슷).
3232166_1 **Pwr=30 (MAX!)** Mtilt=1 Dtilt=6 → overshoot 강함 → power down + tilt down.

### traces.json[0] — single-answer — **정답 C9 "Decrease A3 Offset for 3225568_1" — 전문가 풀이 참조**

Serving PCI 328 (3225568_1) 유지하면서 throughput 30~60 Mbps 로 저하. **Late handover**: A3Off=10 (5dB) 이 지나치게 높음 + Hyst 1dB = 6 dB 로 handover 미발생. → Decrease A3 Offset.

### traces.json[1] — single-answer — **정답 C22 "Decrease A3 Offset for 3216262_3" — 전문가 풀이 참조**

Serving PCI 343 (3216262_3), **SINR -0.35 (매우 나쁨)**. Neighbor PCI 505 RSRP -77 (서빙 -83 보다 6 dB 강함). A3Off+Hyst = 5+1 = 6 dB 로 "Neighbor > Serving + 6" 미충족 (6=6) → late handover. → Decrease A3 Offset.

---

## 4. 풀이 패턴 분류 (Pattern Library)

| # | Pattern 이름 | Trigger | 정답 카테고리 |
|---|-------------|---------|---------------|
| P1 | Late handover (A3 Offset 높음) | Serving A3Off ≥ 10, Neighbor RSRP > Serving + 실제 threshold 미만 | Decrease A3 Offset for **serving cell** |
| P2 | Ping-pong between 2 cells | Serving PCI A↔B 반복, 둘 다 A3Off 낮음 (~2) | Increase A3 Offset (보통 2개 셀 모두 또는 1개) |
| P3 | Overshoot interference | Neighbor cell이 반복 등장 + SINR 저하 + 해당 cell Pwr 높음/Tilt 작음 | Decrease Power + Press down Tilt + Increase A3 Offset (for the overshooting cell) |
| P4 | Coverage hole | Serving RSRP ≤ -100, 모든 Neighbor 도 약함 | Adjust azimuth + Increase power (or Lift tilt) |
| P5 | Server/transmission issue | SINR 양호 (≥10), Throughput 변동 큼, MR 에서 randomness | Check test server and transmission issues |
| P6 | Excessive downtilt on neighbor | SINR 양호, Neighbor RSRP 매우 약함 + 해당 cell 총 tilt ≥ 20° | Lift tilt on that neighbor cell |
| P7 | Insufficient data | 모든 지표 정상 범위, anomaly 없음 | Insufficient data; more data is needed |

Multiple-answer 문제는 P3 (Overshoot) 또는 P4 (Coverage hole) 가 대부분 2~4개 조치로 구성됨.

---

## 5. Qwen 용 System Prompt 초안 (다음 단계로 이관)

위 Decision Tree + Pattern Library 를 근거로 `agent/track_a/prompts.py` 에 다음 system prompt 를 인코딩:

1. 역할 정의 (5G drive test optimization expert)
2. A3 offset 공식 명시 (`Neighbor_RSRP > Serving_RSRP + A3Offset × 0.5 + A3Hyst × 0.5`)
3. Tool 호출 권장 순서 (throughput_logs → serving_pci 시계열 → cell_info → neighbor RSRP → signaling)
4. 7-pattern checklist 로 진단
5. 최종 답변은 반드시 `\boxed{C#}` 또는 `\boxed{C#|C#}` (오름차순)

Few-shot 으로 traces.json 2건 + train[0, 5, 10] 3건 = **5 examples** 주입 (single 3 + multiple 2, P1/P2/P3 패턴 커버).
