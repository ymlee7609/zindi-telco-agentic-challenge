# Track A 문제 분석 — train[260]~train[269]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[260] ~ train[269] (10개)

## 목차

1. [문제 260: `dbeaa819-f11...`](#260) — single-answer, 정답: C8
2. [문제 261: `b0f716f0-220...`](#261) — single-answer, 정답: C9
3. [문제 262: `c1ada848-e27...`](#262) — multiple-answer, 정답: C6|C7
4. [문제 263: `b1bdea5a-506...`](#263) — single-answer, 정답: C16
5. [문제 264: `3ae75103-6af...`](#264) — single-answer, 정답: C16
6. [문제 265: `f9bab469-977...`](#265) — single-answer, 정답: C21
7. [문제 266: `2e4e0bf3-bf1...`](#266) — single-answer, 정답: C21
8. [문제 267: `6f2a33f8-500...`](#267) — multiple-answer, 정답: C1|C16
9. [문제 268: `59e62190-f05...`](#268) — single-answer, 정답: C14
10. [문제 269: `9d082f00-4e6...`](#269) — single-answer, 정답: C13

---

### 문제 260: `dbeaa819-f11...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dbeaa819-f115-4b7c-a96f-8eb20f224985` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Lift the tilt angle  of 3210447_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[260] topology](images/train_0260.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3219551_2 by 32 degrees
- `C2`: Add neighbor relationship between 3219551_2 and 3246386_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219551_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246386_4
- `C5`: Check test server and transmission issues
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219551_2
- `C7`: Increase transmission power for 3246386_4
- `C8`: Lift the tilt angle  of 3210447_1 by 10 degrees **← 정답**
- `C9`: Increase A3 Offset threshold for 3219551_2
- `C10`: Lift the tilt angle of 3219551_2 by 5 degrees
- `C11`: Decrease A3 Offset threshold for 3219551_2
- `C12`: Decrease transmission power for 3246386_4
- `C13`: Increase transmission power for 3219551_2
- `C14`: Decrease transmission power for 3219551_2
- `C15`: Press down the tilt angle of 3219551_2 by 5 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246386_4
- `C17`: Adjust the azimuth of 3210447_1 by 50 degrees
- `C18`: Press down the tilt angle  of 3210447_1 by 10 degrees
- `C19`: Decrease A3 Offset threshold for 3246386_4
- `C20`: Add neighbor relationship between 3210447_1 and 3246386_4
- `C21`: Increase A3 Offset threshold for 3246386_4
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.980 | MS1 | 121.4656684440 | 31.1446321134 | 602 | 504990 | -89.53 | 12.59 | 524.09 | 0.00 | 2.22 | 1588 |
| 2024-09-20 22:21:32.753 | MS1 | 121.4656736139 | 31.1446180957 | 602 | 504990 | -89.89 | 15.73 | 484.03 | 0.13 | 2.04 | 1570 |
| 2024-09-20 22:21:33.458 | MS1 | 121.4656719583 | 31.1446352149 | 602 | 504990 | -86.97 | 17.87 | 567.70 | 0.11 | 2.57 | 1593 |
| 2024-09-20 22:21:34.187 | MS1 | 121.4656643621 | 31.1446303926 | 602 | 504990 | -90.19 | 15.76 | 92.52 | 0.05 | 2.98 | 1583 |
| 2024-09-20 22:21:35.572 | MS1 | 121.4656756302 | 31.1446306182 | 602 | 504990 | -86.24 | 15.67 | 65.34 | 0.13 | 2.73 | 1589 |
| 2024-09-20 22:21:36.327 | MS1 | 121.4656662084 | 31.1446255417 | 602 | 504990 | -87.45 | 13.43 | 87.23 | 0.03 | 2.58 | 1585 |
| 2024-09-20 22:21:37.657 | MS1 | 121.4656685539 | 31.1446360931 | 602 | 504990 | -90.46 | 8.25 | 91.33 | 0.06 | 2.03 | 1574 |
| 2024-09-20 22:21:38.658 | MS1 | 121.4656778823 | 31.1446313208 | 602 | 504990 | -93.38 | 8.31 | 69.50 | 0.16 | 2.64 | 1572 |
| 2024-09-20 22:21:39.730 | MS1 | 121.4656708232 | 31.1446274631 | 602 | 504990 | -91.64 | 7.76 | 71.28 | 0.13 | 2.35 | 1561 |
| 2024-09-20 22:21:40.102 | MS1 | 121.4656748288 | 31.1446309203 | 602 | 504990 | -90.75 | 8.87 | 480.04 | 0.01 | 2.45 | 1571 |
| 2024-09-20 22:21:41.149 | MS1 | 121.4656743642 | 31.1446217963 | 602 | 504990 | -92.08 | 8.60 | 547.73 | 0.13 | 2.00 | 1597 |
| 2024-09-20 22:21:42.211 | MS1 | 121.4656772311 | 31.1446319678 | 602 | 504990 | -92.17 | 9.03 | 355.55 | 0.02 | 2.89 | 1580 |

> *... 20개 열 생략 (전체 32열)*

<details>
<summary>UE 데이터 해석 가이드</summary>

- **Timestamp**: 측정 시각 (초 단위 정밀도)
- **SS-RSRP (dBm)**: 참조 신호 수신 전력. -100 이하는 약한 신호
- **SS-SINR (dB)**: 신호 대 간섭+잡음비. 5 이하는 간섭 심각, 10 이상은 양호
- **DL Throughput (Mbps)**: 다운링크 처리량. 100 미만은 성능 저하 의심
- **Serving PCI**: 현재 서빙 셀의 물리적 셀 ID. 값이 바뀌면 핸드오버 발생

</details>

**기지국 구성 (Network Configuration)**

| gNodeB ID | Cell ID | Longitude | Latitude | Mechanical Azimuth | Mechanical Downtilt | Digital Tilt | Height | Duplex Mode | PCI | Band | DL ARFCN | BW [MHz] | TxRx Mode | Transmission Power | ARFCN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3210447 | 1 | 121.4658459924 | 31.1449637786 | 134 | 1 | 0 | 27.2 | TDD | 88 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3219551 | 2 | 121.4652452613 | 31.1553078201 | 210 | 3 | 7 | 41.9 | TDD | 602 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3246386 | 4 | 121.4687411463 | 31.1462162286 | 130 | 5 | 2 | 40.2 | TDD | 661 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3259649 | 3 | 121.4660484198 | 31.1557642355 | 352 | 12 | 8 | 44.0 | TDD | 244 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

> *... 12개 열 생략 (전체 28열)*

<details>
<summary>기지국 구성 해석 가이드</summary>

- **Mechanical Azimuth**: 안테나 수평 방향 (0°=북, 90°=동)
- **Mechanical Downtilt + Digital Tilt**: 합계가 안테나 하향각. 20° 이상이면 과도한 downtilt
- **Transmission Power**: 송신 전력 (dBm). 높을수록 커버리지 넓음
- **IntraFreqHoA3Offset**: A3 핸드오버 임계값 (0.5dB 단위). 10 이상이면 핸드오버 지연
- **PdcchOccupiedSymbolNum**: PDCCH 리소스 할당. 1SYM은 기본, 2SYM은 확장
- **CovInterFreqA2RsrpThld**: Inter-freq 커버리지 임계값. -95가 -105보다 보수적 (높음)
- **PCell Neighbor Cell**: 설정된 이웃 셀 목록 (핸드오버 후보)

</details>

**시그널링 이벤트 (Signaling Plane)**

| Timestamp | Event Name | Event Content |
| --- | --- | --- |
| 2024-09-20 22:21:31.436 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.457 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.572 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.572 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.331 | NREventA3 | measId:2;ServCellPCI:266;Se... |
| 2024-09-20 22:21:38.571 | NRHandoverAttempt | SourcePCI:266;SourceNR-ARFC... |
| 2024-09-20 22:21:38.601 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.612 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.712 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.712 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210447 | 1 | 7.5440 | 5.1169 | -117.8465 | 19.6329 | 162.9394 | 0.0084 | 0.0095 |
| 2024_09_20 22:00 | 3219551 | 2 | 85.9696 | 82.6185 | -117.0526 | 7.1931 | 138.7617 | 0.0186 | 0.0183 |
| 2024_09_20 22:00 | 3259649 | 3 | 16.1042 | 11.0221 | -116.6513 | 6.5598 | 162.6248 | 0.0026 | 0.0182 |
| 2024_09_20 22:00 | 3246386 | 4 | 18.0380 | 16.8958 | -117.4446 | 7.4062 | 104.8080 | 0.0198 | 0.0103 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412219_08F702AE | 504990 | 602 | -89.9 | 504990 | 661 | -97.4 | 504990 | 88 | -100.1 | 504990 | 244 |
| MR_1774412219_E243245D | 504990 | 602 | -91.3 | 504990 | 661 | -97.4 | 504990 | 88 | -98.6 | 504990 | 244 |
| MR_1774412219_5D51FD67 | 504990 | 602 | -91.7 | 504990 | 661 | -95.5 | 504990 | 88 | -100.2 | 504990 | 244 |
| MR_1774412219_C5EBD174 | 504990 | 602 | -89.3 | 504990 | 661 | -97.9 | 504990 | 88 | -98.7 | 504990 | 244 |
| MR_1774412219_359DFA7E | 504990 | 602 | -88.4 | 504990 | 661 | -97.6 | 504990 | 88 | -99.3 | 504990 | 244 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 261: `b0f716f0-220...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b0f716f0-2206-4ae7-8dc7-2b3b421d37ac` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[261] topology](images/train_0261.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3238083_3 and 3211605_4
- `C2`: Decrease A3 Offset threshold for 3211605_4
- `C3`: Adjust the azimuth of 3211605_4 by 50 degrees
- `C4`: Decrease A3 Offset threshold for 3275669_1
- `C5`: Lift the tilt angle of 3275669_1 by 10 degrees
- `C6`: Press down the tilt angle of 3275669_1 by 10 degrees
- `C7`: Increase transmission power for 3211605_4
- `C8`: Add neighbor relationship between 3275669_1 and 3211605_4
- `C9`: Check test server and transmission issues **← 정답**
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275669_1
- `C12`: Increase A3 Offset threshold for 3211605_4
- `C13`: Decrease transmission power for 3275669_1
- `C14`: Press down the tilt angle  of 3211605_4 by 10 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211605_4
- `C16`: Increase A3 Offset threshold for 3275669_1
- `C17`: Decrease transmission power for 3211605_4
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211605_4
- `C19`: Increase transmission power for 3275669_1
- `C20`: Adjust the azimuth of 3275669_1 by 23 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275669_1
- `C22`: Lift the tilt angle  of 3211605_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.100 | MS1 | 121.4656643232 | 31.1446306326 | 625 | 504990 | -89.82 | 17.11 | 538.99 | 0.03 | 2.24 | 1584 |
| 2024-09-20 22:21:32.287 | MS1 | 121.4656701098 | 31.1446234726 | 625 | 504990 | -87.50 | 16.99 | 326.33 | 0.05 | 2.74 | 1569 |
| 2024-09-20 22:21:33.273 | MS1 | 121.4656682631 | 31.1446307264 | 625 | 504990 | -89.98 | 16.94 | 436.53 | 0.10 | 2.61 | 1561 |
| 2024-09-20 22:21:34.829 | MS1 | 121.4656647577 | 31.1446315763 | 625 | 504990 | -87.40 | 12.34 | 95.39 | 0.16 | 2.12 | 306 |
| 2024-09-20 22:21:35.539 | MS1 | 121.4656726784 | 31.1446236273 | 625 | 504990 | -85.52 | 12.31 | 47.28 | 0.11 | 2.93 | 392 |
| 2024-09-20 22:21:36.124 | MS1 | 121.4656759605 | 31.1446370425 | 625 | 504990 | -91.14 | 17.44 | 86.36 | 0.01 | 2.17 | 445 |
| 2024-09-20 22:21:37.401 | MS1 | 121.4656673341 | 31.1446309620 | 625 | 504990 | -91.60 | 7.55 | 62.09 | 0.15 | 2.55 | 390 |
| 2024-09-20 22:21:38.557 | MS1 | 121.4656649431 | 31.1446279835 | 625 | 504990 | -93.48 | 12.58 | 63.23 | 0.06 | 2.52 | 444 |
| 2024-09-20 22:21:39.410 | MS1 | 121.4656758409 | 31.1446264409 | 625 | 504990 | -92.75 | 9.87 | 80.93 | 0.03 | 2.26 | 437 |
| 2024-09-20 22:21:40.391 | MS1 | 121.4656720249 | 31.1446194495 | 625 | 504990 | -92.47 | 12.91 | 560.91 | 0.06 | 2.52 | 1562 |
| 2024-09-20 22:21:41.501 | MS1 | 121.4656694732 | 31.1446195499 | 625 | 504990 | -92.08 | 12.33 | 600.63 | 0.00 | 2.50 | 1562 |
| 2024-09-20 22:21:42.940 | MS1 | 121.4656596418 | 31.1446245485 | 625 | 504990 | -93.61 | 10.99 | 380.47 | 0.19 | 2.47 | 1580 |

> *... 20개 열 생략 (전체 32열)*

<details>
<summary>UE 데이터 해석 가이드</summary>

- **Timestamp**: 측정 시각 (초 단위 정밀도)
- **SS-RSRP (dBm)**: 참조 신호 수신 전력. -100 이하는 약한 신호
- **SS-SINR (dB)**: 신호 대 간섭+잡음비. 5 이하는 간섭 심각, 10 이상은 양호
- **DL Throughput (Mbps)**: 다운링크 처리량. 100 미만은 성능 저하 의심
- **Serving PCI**: 현재 서빙 셀의 물리적 셀 ID. 값이 바뀌면 핸드오버 발생

</details>

**기지국 구성 (Network Configuration)**

| gNodeB ID | Cell ID | Longitude | Latitude | Mechanical Azimuth | Mechanical Downtilt | Digital Tilt | Height | Duplex Mode | PCI | Band | DL ARFCN | BW [MHz] | TxRx Mode | Transmission Power | ARFCN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3211605 | 4 | 121.4732697449 | 31.1548844994 | 66 | 15 | 9 | 22.2 | TDD | 598 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3238083 | 3 | 121.4755796199 | 31.1440154347 | 254 | 10 | 3 | 38.6 | TDD | 461 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3275669 | 1 | 121.4714727628 | 31.1503649073 | 244 | 9 | 6 | 29.0 | TDD | 625 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3275851 | 2 | 121.4725685192 | 31.1518845752 | 329 | 12 | 12 | 27.7 | TDD | 426 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

> *... 12개 열 생략 (전체 28열)*

<details>
<summary>기지국 구성 해석 가이드</summary>

- **Mechanical Azimuth**: 안테나 수평 방향 (0°=북, 90°=동)
- **Mechanical Downtilt + Digital Tilt**: 합계가 안테나 하향각. 20° 이상이면 과도한 downtilt
- **Transmission Power**: 송신 전력 (dBm). 높을수록 커버리지 넓음
- **IntraFreqHoA3Offset**: A3 핸드오버 임계값 (0.5dB 단위). 10 이상이면 핸드오버 지연
- **PdcchOccupiedSymbolNum**: PDCCH 리소스 할당. 1SYM은 기본, 2SYM은 확장
- **CovInterFreqA2RsrpThld**: Inter-freq 커버리지 임계값. -95가 -105보다 보수적 (높음)
- **PCell Neighbor Cell**: 설정된 이웃 셀 목록 (핸드오버 후보)

</details>

**시그널링 이벤트 (Signaling Plane)**

| Timestamp | Event Name | Event Content |
| --- | --- | --- |
| 2024-09-20 22:21:31.078 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.094 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.235 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.235 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.939 | NREventA3 | measId:2;ServCellPCI:144;Se... |
| 2024-09-20 22:21:38.179 | NRHandoverAttempt | SourcePCI:144;SourceNR-ARFC... |
| 2024-09-20 22:21:38.220 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.235 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.356 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.356 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275669 | 1 | 16.8224 | 16.5085 | -116.5679 | 9.2597 | 162.8449 | 0.0143 | 0.0088 |
| 2024_09_20 22:00 | 3275851 | 2 | 6.0259 | 12.7748 | -117.1543 | 17.7560 | 192.4359 | 0.0120 | 0.0095 |
| 2024_09_20 22:00 | 3238083 | 3 | 18.2951 | 18.3598 | -114.7737 | 10.1571 | 155.8271 | 0.0043 | 0.0162 |
| 2024_09_20 22:00 | 3211605 | 4 | 14.8215 | 8.5384 | -116.3601 | 16.0763 | 137.9912 | 0.0119 | 0.0126 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413598_F4D7DD1B | 504990 | 625 | -87.2 | 504990 | 598 | -85.9 | 504990 | 461 | -94.1 | 504990 | 426 |
| MR_1774413598_1C365EB3 | 504990 | 625 | -87.6 | 504990 | 598 | -88.0 | 504990 | 461 | -96.6 | 504990 | 426 |
| MR_1774413598_7EE526F2 | 504990 | 625 | -87.0 | 504990 | 598 | -87.7 | 504990 | 461 | -94.3 | 504990 | 426 |
| MR_1774413598_6F60E5C0 | 504990 | 625 | -88.5 | 504990 | 598 | -87.3 | 504990 | 461 | -96.4 | 504990 | 426 |
| MR_1774413598_16C26131 | 504990 | 625 | -87.4 | 504990 | 598 | -86.1 | 504990 | 461 | -96.4 | 504990 | 426 |
| MR_1774413598_22A48662 | 504990 | 625 | -85.6 | 504990 | 598 | -85.4 | 504990 | 461 | -93.9 | 504990 | 426 |
| MR_1774413598_57E6E27A | 504990 | 625 | -85.6 | 504990 | 598 | -88.4 | 504990 | 461 | -95.8 | 504990 | 426 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 262: `c1ada848-e27...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c1ada848-e27f-46eb-bc56-e100264fa365` |
| Tag | **multiple-answer** |
| 정답 | **C6|C7** |
| C6 의미 | Increase transmission power for 3213439_3 |
| C7 의미 | Adjust the azimuth of 3213439_3 by 23 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[262] topology](images/train_0262.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3252808_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213439_3
- `C3`: Add neighbor relationship between 3263034_2 and 3252808_4
- `C4`: Lift the tilt angle  of 3252808_4 by 6 degrees
- `C5`: Increase A3 Offset threshold for 3252808_4
- `C6`: Increase transmission power for 3213439_3 **← 정답**
- `C7`: Adjust the azimuth of 3213439_3 by 23 degrees **← 정답**
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213439_3
- `C10`: Increase transmission power for 3252808_4
- `C11`: Adjust the azimuth of 3252808_4 by 1 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252808_4
- `C13`: Press down the tilt angle of 3213439_3 by 7 degrees
- `C14`: Decrease A3 Offset threshold for 3213439_3
- `C15`: Increase A3 Offset threshold for 3213439_3
- `C16`: Check test server and transmission issues
- `C17`: Press down the tilt angle  of 3252808_4 by 6 degrees
- `C18`: Decrease transmission power for 3213439_3
- `C19`: Lift the tilt angle of 3213439_3 by 7 degrees
- `C20`: Add neighbor relationship between 3213439_3 and 3252808_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252808_4
- `C22`: Decrease transmission power for 3252808_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.306 | MS1 | 121.4656665985 | 31.1446282835 | 341 | 504990 | -90.15 | 16.63 | 319.21 | 0.11 | 2.91 | 1589 |
| 2024-09-20 22:21:32.362 | MS1 | 121.4656741477 | 31.1446379408 | 341 | 504990 | -90.47 | 16.00 | 469.30 | 0.13 | 2.95 | 1568 |
| 2024-09-20 22:21:33.512 | MS1 | 121.4656677894 | 31.1446310015 | 341 | 504990 | -86.18 | 14.90 | 461.82 | 0.15 | 2.57 | 1591 |
| 2024-09-20 22:21:34.733 | MS1 | 121.4656772475 | 31.1446364000 | 341 | 504990 | -109.89 | 0.52 | 43.36 | 0.17 | 1.30 | 1595 |
| 2024-09-20 22:21:35.807 | MS1 | 121.4656751175 | 31.1446256237 | 341 | 504990 | -105.39 | 1.98 | 22.21 | 0.16 | 1.22 | 1571 |
| 2024-09-20 22:21:36.598 | MS1 | 121.4656729634 | 31.1446343975 | 341 | 504990 | -102.03 | -0.75 | 49.21 | 0.09 | 1.07 | 1580 |
| 2024-09-20 22:21:37.242 | MS1 | 121.4656661305 | 31.1446213588 | 341 | 504990 | -105.67 | 1.72 | 80.63 | 0.09 | 1.34 | 1593 |
| 2024-09-20 22:21:38.712 | MS1 | 121.4656765185 | 31.1446232446 | 341 | 504990 | -101.38 | 0.95 | 21.81 | 0.07 | 1.49 | 1599 |
| 2024-09-20 22:21:39.598 | MS1 | 121.4656632944 | 31.1446258285 | 341 | 504990 | -105.11 | -1.26 | 33.38 | 0.18 | 1.50 | 1573 |
| 2024-09-20 22:21:40.636 | MS1 | 121.4656747449 | 31.1446307563 | 341 | 504990 | -92.59 | 14.81 | 531.91 | 0.16 | 2.70 | 1581 |
| 2024-09-20 22:21:41.996 | MS1 | 121.4656737506 | 31.1446338718 | 341 | 504990 | -86.85 | 15.36 | 490.90 | 0.10 | 2.07 | 1592 |
| 2024-09-20 22:21:42.617 | MS1 | 121.4656598405 | 31.1446279775 | 341 | 504990 | -92.82 | 14.98 | 416.37 | 0.18 | 2.37 | 1592 |

> *... 20개 열 생략 (전체 32열)*

<details>
<summary>UE 데이터 해석 가이드</summary>

- **Timestamp**: 측정 시각 (초 단위 정밀도)
- **SS-RSRP (dBm)**: 참조 신호 수신 전력. -100 이하는 약한 신호
- **SS-SINR (dB)**: 신호 대 간섭+잡음비. 5 이하는 간섭 심각, 10 이상은 양호
- **DL Throughput (Mbps)**: 다운링크 처리량. 100 미만은 성능 저하 의심
- **Serving PCI**: 현재 서빙 셀의 물리적 셀 ID. 값이 바뀌면 핸드오버 발생

</details>

**기지국 구성 (Network Configuration)**

| gNodeB ID | Cell ID | Longitude | Latitude | Mechanical Azimuth | Mechanical Downtilt | Digital Tilt | Height | Duplex Mode | PCI | Band | DL ARFCN | BW [MHz] | TxRx Mode | Transmission Power | ARFCN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3213439 | 3 | 121.4642638484 | 31.1471568380 | 177 | 1 | 8 | 32.1 | TDD | 341 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3238602 | 1 | 121.4694633918 | 31.1555615186 | 36 | 3 | 4 | 35.9 | TDD | 891 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3252808 | 4 | 121.4723894275 | 31.1553709945 | 209 | 5 | 3 | 21.8 | TDD | 886 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3263034 | 2 | 121.4664772308 | 31.1557652106 | 1 | 11 | 11 | 24.5 | TDD | 380 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

> *... 12개 열 생략 (전체 28열)*

<details>
<summary>기지국 구성 해석 가이드</summary>

- **Mechanical Azimuth**: 안테나 수평 방향 (0°=북, 90°=동)
- **Mechanical Downtilt + Digital Tilt**: 합계가 안테나 하향각. 20° 이상이면 과도한 downtilt
- **Transmission Power**: 송신 전력 (dBm). 높을수록 커버리지 넓음
- **IntraFreqHoA3Offset**: A3 핸드오버 임계값 (0.5dB 단위). 10 이상이면 핸드오버 지연
- **PdcchOccupiedSymbolNum**: PDCCH 리소스 할당. 1SYM은 기본, 2SYM은 확장
- **CovInterFreqA2RsrpThld**: Inter-freq 커버리지 임계값. -95가 -105보다 보수적 (높음)
- **PCell Neighbor Cell**: 설정된 이웃 셀 목록 (핸드오버 후보)

</details>

**시그널링 이벤트 (Signaling Plane)**

| Timestamp | Event Name | Event Content |
| --- | --- | --- |
| 2024-09-20 22:21:30.775 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.797 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.930 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.930 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.103 | NREventA2 | measId:1;ServCellPCI:123;Se... |
| 2024-09-20 22:21:34.251 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238602 | 1 | 19.1543 | 5.8465 | -115.5822 | 17.3179 | 140.6654 | 0.0069 | 0.0143 |
| 2024_09_20 22:00 | 3263034 | 2 | 17.6740 | 16.0127 | -114.9233 | 5.0121 | 154.0933 | 0.0104 | 0.0177 |
| 2024_09_20 22:00 | 3213439 | 3 | 12.2951 | 6.7248 | -117.4617 | 13.0337 | 168.6413 | 0.1226 | 0.0103 |
| 2024_09_20 22:00 | 3252808 | 4 | 15.2015 | 17.7556 | -117.2815 | 6.8714 | 106.9579 | 0.0172 | 0.0148 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416273_17C30749 | 504990 | 341 | -110.5 | 504990 | 886 | -117.9 | 504990 | 380 | -122.3 | 504990 | 891 |
| MR_1774416273_F93105FD | 504990 | 341 | -111.0 | 504990 | 886 | -115.1 | 504990 | 380 | -123.5 | 504990 | 891 |
| MR_1774416273_1D6E8D16 | 504990 | 341 | -111.8 | 504990 | 886 | -116.8 | 504990 | 380 | -123.7 | 504990 | 891 |
| MR_1774416273_93D9D5A4 | 504990 | 341 | -108.8 | 504990 | 886 | -116.9 | 504990 | 380 | -123.4 | 504990 | 891 |
| MR_1774416273_7A1F50E8 | 504990 | 341 | -109.9 | 504990 | 886 | -114.8 | 504990 | 380 | -123.8 | 504990 | 891 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 263: `b1bdea5a-506...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b1bdea5a-506c-4b3b-ab03-cfe79d5cbfd8` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3265885_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[263] topology](images/train_0263.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3265885_1 by 3 degrees
- `C2`: Increase transmission power for 3222454_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265885_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222454_3
- `C5`: Increase A3 Offset threshold for 3265885_1
- `C6`: Add neighbor relationship between 3261028_2 and 3222454_3
- `C7`: Lift the tilt angle of 3265885_1 by 4 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222454_3
- `C9`: Increase transmission power for 3265885_1
- `C10`: Decrease transmission power for 3265885_1
- `C11`: Adjust the azimuth of 3222454_3 by 50 degrees
- `C12`: Increase A3 Offset threshold for 3222454_3
- `C13`: Decrease A3 Offset threshold for 3265885_1
- `C14`: Add neighbor relationship between 3265885_1 and 3222454_3
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265885_1 **← 정답**
- `C17`: Press down the tilt angle of 3265885_1 by 4 degrees
- `C18`: Press down the tilt angle  of 3222454_3 by 10 degrees
- `C19`: Lift the tilt angle  of 3222454_3 by 10 degrees
- `C20`: Decrease A3 Offset threshold for 3222454_3
- `C21`: Decrease transmission power for 3222454_3
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.144 | MS1 | 121.4656693889 | 31.1446275312 | 96 | 504990 | -89.62 | 13.26 | 565.31 | 0.14 | 2.57 | 1591 |
| 2024-09-20 22:21:32.903 | MS1 | 121.4656614307 | 31.1446203874 | 96 | 504990 | -85.11 | 13.62 | 459.93 | 0.02 | 2.94 | 1586 |
| 2024-09-20 22:21:33.440 | MS1 | 121.4656586726 | 31.1446248369 | 96 | 504990 | -87.33 | 15.51 | 491.40 | 0.07 | 2.61 | 1580 |
| 2024-09-20 22:21:34.338 | MS1 | 121.4656636242 | 31.1446266006 | 96 | 504990 | -88.30 | 17.97 | 83.10 | 0.52 | 2.42 | 633 |
| 2024-09-20 22:21:35.274 | MS1 | 121.4656583978 | 31.1446312607 | 96 | 504990 | -87.59 | 16.34 | 104.24 | 0.61 | 2.59 | 543 |
| 2024-09-20 22:21:36.173 | MS1 | 121.4656735137 | 31.1446291254 | 96 | 504990 | -90.13 | 17.51 | 97.37 | 0.58 | 2.68 | 626 |
| 2024-09-20 22:21:37.786 | MS1 | 121.4656647325 | 31.1446329054 | 96 | 504990 | -89.21 | 7.92 | 77.76 | 0.65 | 2.78 | 620 |
| 2024-09-20 22:21:38.711 | MS1 | 121.4656765431 | 31.1446186268 | 96 | 504990 | -89.97 | 7.64 | 86.14 | 0.57 | 2.96 | 622 |
| 2024-09-20 22:21:39.527 | MS1 | 121.4656702683 | 31.1446233195 | 96 | 504990 | -89.34 | 9.88 | 64.47 | 0.55 | 2.40 | 586 |
| 2024-09-20 22:21:40.442 | MS1 | 121.4656633111 | 31.1446318342 | 96 | 504990 | -92.81 | 8.29 | 550.98 | 0.20 | 2.42 | 1594 |
| 2024-09-20 22:21:41.253 | MS1 | 121.4656704042 | 31.1446332095 | 96 | 504990 | -90.33 | 8.62 | 353.43 | 0.12 | 2.84 | 1586 |
| 2024-09-20 22:21:42.463 | MS1 | 121.4656654779 | 31.1446355425 | 96 | 504990 | -93.07 | 11.01 | 423.94 | 0.02 | 2.35 | 1580 |

> *... 20개 열 생략 (전체 32열)*

<details>
<summary>UE 데이터 해석 가이드</summary>

- **Timestamp**: 측정 시각 (초 단위 정밀도)
- **SS-RSRP (dBm)**: 참조 신호 수신 전력. -100 이하는 약한 신호
- **SS-SINR (dB)**: 신호 대 간섭+잡음비. 5 이하는 간섭 심각, 10 이상은 양호
- **DL Throughput (Mbps)**: 다운링크 처리량. 100 미만은 성능 저하 의심
- **Serving PCI**: 현재 서빙 셀의 물리적 셀 ID. 값이 바뀌면 핸드오버 발생

</details>

**기지국 구성 (Network Configuration)**

| gNodeB ID | Cell ID | Longitude | Latitude | Mechanical Azimuth | Mechanical Downtilt | Digital Tilt | Height | Duplex Mode | PCI | Band | DL ARFCN | BW [MHz] | TxRx Mode | Transmission Power | ARFCN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3222454 | 3 | 121.4645467328 | 31.1558407783 | 328 | 14 | 12 | 36.4 | TDD | 483 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3253157 | 4 | 121.4751263657 | 31.1520122328 | 44 | 15 | 11 | 18.5 | TDD | 575 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3261028 | 2 | 121.4675803955 | 31.1539047030 | 339 | 15 | 1 | 49.7 | TDD | 146 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3265885 | 1 | 121.4668455035 | 31.1555892965 | 182 | 3 | 6 | 26.4 | TDD | 96 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

> *... 12개 열 생략 (전체 28열)*

<details>
<summary>기지국 구성 해석 가이드</summary>

- **Mechanical Azimuth**: 안테나 수평 방향 (0°=북, 90°=동)
- **Mechanical Downtilt + Digital Tilt**: 합계가 안테나 하향각. 20° 이상이면 과도한 downtilt
- **Transmission Power**: 송신 전력 (dBm). 높을수록 커버리지 넓음
- **IntraFreqHoA3Offset**: A3 핸드오버 임계값 (0.5dB 단위). 10 이상이면 핸드오버 지연
- **PdcchOccupiedSymbolNum**: PDCCH 리소스 할당. 1SYM은 기본, 2SYM은 확장
- **CovInterFreqA2RsrpThld**: Inter-freq 커버리지 임계값. -95가 -105보다 보수적 (높음)
- **PCell Neighbor Cell**: 설정된 이웃 셀 목록 (핸드오버 후보)

</details>

**시그널링 이벤트 (Signaling Plane)**

| Timestamp | Event Name | Event Content |
| --- | --- | --- |
| 2024-09-20 22:21:31.174 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.199 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.337 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.337 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.000 | NREventA3 | measId:2;ServCellPCI:345;Se... |
| 2024-09-20 22:21:38.240 | NRHandoverAttempt | SourcePCI:345;SourceNR-ARFC... |
| 2024-09-20 22:21:38.277 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.288 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.436 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.436 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265885 | 1 | 5.7399 | 7.4579 | -114.8112 | 18.3955 | 177.0527 | 0.0199 | 0.0143 |
| 2024_09_20 22:00 | 3261028 | 2 | 18.4666 | 13.9544 | -115.3264 | 14.6459 | 133.9578 | 0.0148 | 0.0143 |
| 2024_09_20 22:00 | 3222454 | 3 | 7.0636 | 10.3511 | -117.6670 | 8.5146 | 169.9780 | 0.0050 | 0.0077 |
| 2024_09_20 22:00 | 3253157 | 4 | 6.3149 | 6.6303 | -115.6833 | 15.2522 | 129.8182 | 0.0179 | 0.0066 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416103_A95EC108 | 504990 | 96 | -90.3 | 504990 | 483 | -94.0 | 504990 | 146 | -96.7 | 504990 | 575 |
| MR_1774416103_F0B61975 | 504990 | 96 | -86.5 | 504990 | 483 | -95.7 | 504990 | 146 | -97.4 | 504990 | 575 |
| MR_1774416103_AA936E70 | 504990 | 96 | -88.6 | 504990 | 483 | -95.8 | 504990 | 146 | -97.7 | 504990 | 575 |
| MR_1774416103_4F727C7F | 504990 | 96 | -87.0 | 504990 | 483 | -95.5 | 504990 | 146 | -95.7 | 504990 | 575 |
| MR_1774416103_973CA488 | 504990 | 96 | -89.2 | 504990 | 483 | -92.9 | 504990 | 146 | -98.2 | 504990 | 575 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 264: `3ae75103-6af...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3ae75103-6af8-401e-9d1c-7b819a5710ba` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease A3 Offset threshold for 3228202_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[264] topology](images/train_0264.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228202_1
- `C2`: Decrease transmission power for 3265330_3
- `C3`: Increase A3 Offset threshold for 3228202_1
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Increase transmission power for 3228202_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265330_3
- `C7`: Increase transmission power for 3265330_3
- `C8`: Add neighbor relationship between 3228202_1 and 3265330_3
- `C9`: Check test server and transmission issues
- `C10`: Add neighbor relationship between 3271864_4 and 3265330_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228202_1
- `C12`: Lift the tilt angle  of 3265330_3 by 10 degrees
- `C13`: Lift the tilt angle of 3228202_1 by 10 degrees
- `C14`: Press down the tilt angle  of 3265330_3 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3265330_3
- `C16`: Decrease A3 Offset threshold for 3228202_1 **← 정답**
- `C17`: Increase A3 Offset threshold for 3265330_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265330_3
- `C19`: Adjust the azimuth of 3228202_1 by 50 degrees
- `C20`: Press down the tilt angle of 3228202_1 by 10 degrees
- `C21`: Decrease transmission power for 3228202_1
- `C22`: Adjust the azimuth of 3265330_3 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.286 | MS1 | 121.4656683516 | 31.1446341243 | 777 | 504990 | -84.03 | 15.54 | 548.10 | 0.00 | 2.79 | 1592 |
| 2024-09-20 22:21:32.378 | MS1 | 121.4656622173 | 31.1446335890 | 777 | 504990 | -76.85 | 17.15 | 544.23 | 0.02 | 2.06 | 1570 |
| 2024-09-20 22:21:33.222 | MS1 | 121.4656580303 | 31.1446258321 | 777 | 504990 | -83.04 | 12.32 | 409.89 | 0.04 | 2.26 | 1579 |
| 2024-09-20 22:21:34.343 | MS1 | 121.4656743246 | 31.1446319303 | 777 | 504990 | -92.72 | -1.04 | 49.06 | 0.10 | 1.36 | 1594 |
| 2024-09-20 22:21:35.113 | MS1 | 121.4656659748 | 31.1446280333 | 777 | 504990 | -83.21 | -2.44 | 68.57 | 0.10 | 1.35 | 1580 |
| 2024-09-20 22:21:36.610 | MS1 | 121.4656706294 | 31.1446193900 | 777 | 504990 | -92.82 | -1.93 | 40.33 | 0.16 | 1.08 | 1590 |
| 2024-09-20 22:21:37.964 | MS1 | 121.4656718627 | 31.1446369392 | 777 | 504990 | -86.03 | -2.81 | 40.70 | 0.13 | 1.21 | 1586 |
| 2024-09-20 22:21:38.360 | MS1 | 121.4656688568 | 31.1446356898 | 777 | 504990 | -89.71 | -2.90 | 67.41 | 0.18 | 1.44 | 1564 |
| 2024-09-20 22:21:39.908 | MS1 | 121.4656667546 | 31.1446339378 | 197 | 504990 | -78.40 | 17.04 | 265.84 | 0.08 | 1.14 | 1565 |
| 2024-09-20 22:21:40.501 | MS1 | 121.4656737515 | 31.1446308161 | 197 | 504990 | -80.43 | 12.22 | 584.86 | 0.16 | 2.86 | 1583 |
| 2024-09-20 22:21:41.170 | MS1 | 121.4656652084 | 31.1446311990 | 197 | 504990 | -82.14 | 12.72 | 587.36 | 0.16 | 2.60 | 1561 |
| 2024-09-20 22:21:42.950 | MS1 | 121.4656673603 | 31.1446369977 | 197 | 504990 | -83.03 | 17.11 | 441.36 | 0.07 | 2.06 | 1577 |

> *... 20개 열 생략 (전체 32열)*

<details>
<summary>UE 데이터 해석 가이드</summary>

- **Timestamp**: 측정 시각 (초 단위 정밀도)
- **SS-RSRP (dBm)**: 참조 신호 수신 전력. -100 이하는 약한 신호
- **SS-SINR (dB)**: 신호 대 간섭+잡음비. 5 이하는 간섭 심각, 10 이상은 양호
- **DL Throughput (Mbps)**: 다운링크 처리량. 100 미만은 성능 저하 의심
- **Serving PCI**: 현재 서빙 셀의 물리적 셀 ID. 값이 바뀌면 핸드오버 발생

</details>

**기지국 구성 (Network Configuration)**

| gNodeB ID | Cell ID | Longitude | Latitude | Mechanical Azimuth | Mechanical Downtilt | Digital Tilt | Height | Duplex Mode | PCI | Band | DL ARFCN | BW [MHz] | TxRx Mode | Transmission Power | ARFCN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3228202 | 1 | 121.4715413945 | 31.1494419063 | 281 | 14 | 12 | 37.5 | TDD | 777 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3244553 | 2 | 121.4757666657 | 31.1539357681 | 220 | 2 | 4 | 17.8 | TDD | 619 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3265330 | 3 | 121.4719533817 | 31.1458331545 | 319 | 7 | 11 | 30.2 | TDD | 197 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3271864 | 4 | 121.4647033406 | 31.1535813143 | 301 | 5 | 5 | 39.5 | TDD | 685 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

> *... 12개 열 생략 (전체 28열)*

<details>
<summary>기지국 구성 해석 가이드</summary>

- **Mechanical Azimuth**: 안테나 수평 방향 (0°=북, 90°=동)
- **Mechanical Downtilt + Digital Tilt**: 합계가 안테나 하향각. 20° 이상이면 과도한 downtilt
- **Transmission Power**: 송신 전력 (dBm). 높을수록 커버리지 넓음
- **IntraFreqHoA3Offset**: A3 핸드오버 임계값 (0.5dB 단위). 10 이상이면 핸드오버 지연
- **PdcchOccupiedSymbolNum**: PDCCH 리소스 할당. 1SYM은 기본, 2SYM은 확장
- **CovInterFreqA2RsrpThld**: Inter-freq 커버리지 임계값. -95가 -105보다 보수적 (높음)
- **PCell Neighbor Cell**: 설정된 이웃 셀 목록 (핸드오버 후보)

</details>

**시그널링 이벤트 (Signaling Plane)**

| Timestamp | Event Name | Event Content |
| --- | --- | --- |
| 2024-09-20 22:21:30.953 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.975 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.103 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.103 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.754 | NREventA3 | measId:2;ServCellPCI:108;Se... |
| 2024-09-20 22:21:37.994 | NRHandoverAttempt | SourcePCI:108;SourceNR-ARFC... |
| 2024-09-20 22:21:38.039 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.054 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.182 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.182 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228202 | 1 | 7.8797 | 10.9496 | -117.3695 | 8.3612 | 191.3901 | 0.0100 | 0.1257 |
| 2024_09_20 22:00 | 3244553 | 2 | 10.7283 | 14.2355 | -117.9189 | 13.4852 | 178.3654 | 0.0028 | 0.0197 |
| 2024_09_20 22:00 | 3265330 | 3 | 19.6054 | 12.1706 | -115.7801 | 6.8970 | 80.1229 | 0.0014 | 0.0166 |
| 2024_09_20 22:00 | 3271864 | 4 | 5.2173 | 13.1591 | -117.1430 | 13.3711 | 181.7979 | 0.0146 | 0.0157 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416288_C843AD6F | 504990 | 197 | -86.7 | 504990 | 777 | -92.0 | 504990 | 685 | -91.7 | 504990 | 619 |
| MR_1774416288_1788F4C5 | 504990 | 777 | -90.8 | 504990 | 197 | -85.4 | 504990 | 685 | -93.7 | 504990 | 619 |
| MR_1774416288_E8E34726 | 504990 | 777 | -92.6 | 504990 | 197 | -87.0 | 504990 | 685 | -94.1 | 504990 | 619 |
| MR_1774416288_D5B33B1D | 504990 | 777 | -93.8 | 504990 | 197 | -87.8 | 504990 | 685 | -92.2 | 504990 | 619 |
| MR_1774416288_0ACCA112 | 504990 | 777 | -93.5 | 504990 | 197 | -87.6 | 504990 | 685 | -94.2 | 504990 | 619 |
| MR_1774416288_67DDD926 | 504990 | 777 | -93.2 | 504990 | 197 | -86.0 | 504990 | 685 | -91.8 | 504990 | 619 |
| MR_1774416288_4E0012F2 | 504990 | 777 | -90.8 | 504990 | 197 | -86.3 | 504990 | 685 | -94.1 | 504990 | 619 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 265: `f9bab469-977...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f9bab469-977f-49a3-81c5-e043daf4ee99` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[265] topology](images/train_0265.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3258372_3 by 50 degrees
- `C2`: Increase transmission power for 3258372_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258372_3
- `C4`: Decrease A3 Offset threshold for 3258372_3
- `C5`: Increase transmission power for 3253629_1
- `C6`: Lift the tilt angle of 3258372_3 by 10 degrees
- `C7`: Press down the tilt angle  of 3253629_1 by 10 degrees
- `C8`: Add neighbor relationship between 3217238_2 and 3253629_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258372_3
- `C11`: Lift the tilt angle  of 3253629_1 by 10 degrees
- `C12`: Decrease A3 Offset threshold for 3253629_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253629_1
- `C14`: Press down the tilt angle of 3258372_3 by 10 degrees
- `C15`: Add neighbor relationship between 3258372_3 and 3253629_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253629_1
- `C17`: Increase A3 Offset threshold for 3258372_3
- `C18`: Increase A3 Offset threshold for 3253629_1
- `C19`: Decrease transmission power for 3258372_3
- `C20`: Decrease transmission power for 3253629_1
- `C21`: Check test server and transmission issues **← 정답**
- `C22`: Adjust the azimuth of 3253629_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.653 | MS1 | 121.4656772682 | 31.1446377033 | 879 | 504990 | -88.07 | 13.23 | 364.29 | 0.02 | 2.49 | 1595 |
| 2024-09-20 22:21:32.229 | MS1 | 121.4656695973 | 31.1446186190 | 879 | 504990 | -85.87 | 12.63 | 463.05 | 0.10 | 2.88 | 1567 |
| 2024-09-20 22:21:33.141 | MS1 | 121.4656761643 | 31.1446367556 | 879 | 504990 | -85.76 | 16.78 | 355.54 | 0.18 | 2.81 | 1579 |
| 2024-09-20 22:21:34.967 | MS1 | 121.4656718251 | 31.1446222884 | 879 | 504990 | -85.00 | 16.75 | 69.40 | 0.04 | 2.15 | 375 |
| 2024-09-20 22:21:35.820 | MS1 | 121.4656595655 | 31.1446272260 | 879 | 504990 | -89.82 | 16.11 | 80.85 | 0.06 | 2.33 | 436 |
| 2024-09-20 22:21:36.470 | MS1 | 121.4656725050 | 31.1446206482 | 879 | 504990 | -91.52 | 15.21 | 71.35 | 0.18 | 2.98 | 420 |
| 2024-09-20 22:21:37.434 | MS1 | 121.4656615591 | 31.1446264302 | 879 | 504990 | -92.88 | 7.80 | 48.34 | 0.07 | 2.12 | 413 |
| 2024-09-20 22:21:38.714 | MS1 | 121.4656592169 | 31.1446263037 | 879 | 504990 | -91.30 | 8.10 | 91.08 | 0.03 | 2.66 | 471 |
| 2024-09-20 22:21:39.139 | MS1 | 121.4656601092 | 31.1446260889 | 879 | 504990 | -89.50 | 8.51 | 66.02 | 0.13 | 2.67 | 382 |
| 2024-09-20 22:21:40.224 | MS1 | 121.4656749954 | 31.1446211444 | 879 | 504990 | -93.09 | 11.17 | 514.40 | 0.03 | 2.80 | 1578 |
| 2024-09-20 22:21:41.992 | MS1 | 121.4656750551 | 31.1446294644 | 879 | 504990 | -91.87 | 10.23 | 336.55 | 0.12 | 2.42 | 1570 |
| 2024-09-20 22:21:42.153 | MS1 | 121.4656611382 | 31.1446371127 | 879 | 504990 | -93.46 | 9.08 | 327.66 | 0.05 | 2.66 | 1567 |

> *... 20개 열 생략 (전체 32열)*

<details>
<summary>UE 데이터 해석 가이드</summary>

- **Timestamp**: 측정 시각 (초 단위 정밀도)
- **SS-RSRP (dBm)**: 참조 신호 수신 전력. -100 이하는 약한 신호
- **SS-SINR (dB)**: 신호 대 간섭+잡음비. 5 이하는 간섭 심각, 10 이상은 양호
- **DL Throughput (Mbps)**: 다운링크 처리량. 100 미만은 성능 저하 의심
- **Serving PCI**: 현재 서빙 셀의 물리적 셀 ID. 값이 바뀌면 핸드오버 발생

</details>

**기지국 구성 (Network Configuration)**

| gNodeB ID | Cell ID | Longitude | Latitude | Mechanical Azimuth | Mechanical Downtilt | Digital Tilt | Height | Duplex Mode | PCI | Band | DL ARFCN | BW [MHz] | TxRx Mode | Transmission Power | ARFCN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3215871 | 4 | 121.4749708182 | 31.1465091322 | 86 | 7 | 9 | 36.2 | TDD | 7 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3217238 | 2 | 121.4670693536 | 31.1457844770 | 178 | 9 | 7 | 49.5 | TDD | 82 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3253629 | 1 | 121.4691753019 | 31.1471292669 | 129 | 14 | 4 | 17.0 | TDD | 489 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3258372 | 3 | 121.4730725502 | 31.1492938534 | 348 | 14 | 9 | 49.2 | TDD | 879 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

> *... 12개 열 생략 (전체 28열)*

<details>
<summary>기지국 구성 해석 가이드</summary>

- **Mechanical Azimuth**: 안테나 수평 방향 (0°=북, 90°=동)
- **Mechanical Downtilt + Digital Tilt**: 합계가 안테나 하향각. 20° 이상이면 과도한 downtilt
- **Transmission Power**: 송신 전력 (dBm). 높을수록 커버리지 넓음
- **IntraFreqHoA3Offset**: A3 핸드오버 임계값 (0.5dB 단위). 10 이상이면 핸드오버 지연
- **PdcchOccupiedSymbolNum**: PDCCH 리소스 할당. 1SYM은 기본, 2SYM은 확장
- **CovInterFreqA2RsrpThld**: Inter-freq 커버리지 임계값. -95가 -105보다 보수적 (높음)
- **PCell Neighbor Cell**: 설정된 이웃 셀 목록 (핸드오버 후보)

</details>

**시그널링 이벤트 (Signaling Plane)**

| Timestamp | Event Name | Event Content |
| --- | --- | --- |
| 2024-09-20 22:21:30.874 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.891 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.006 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.006 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.758 | NREventA3 | measId:2;ServCellPCI:670;Se... |
| 2024-09-20 22:21:37.998 | NRHandoverAttempt | SourcePCI:670;SourceNR-ARFC... |
| 2024-09-20 22:21:38.047 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.062 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.199 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.199 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253629 | 1 | 12.4044 | 13.5912 | -114.8397 | 16.2487 | 178.0449 | 0.0020 | 0.0172 |
| 2024_09_20 22:00 | 3217238 | 2 | 12.8283 | 12.8992 | -117.7878 | 16.3299 | 156.7604 | 0.0070 | 0.0187 |
| 2024_09_20 22:00 | 3258372 | 3 | 10.1739 | 7.9519 | -116.0467 | 11.1616 | 175.7411 | 0.0038 | 0.0154 |
| 2024_09_20 22:00 | 3215871 | 4 | 7.8719 | 14.5489 | -116.0262 | 7.8203 | 125.6206 | 0.0149 | 0.0014 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412876_8EA35FAF | 504990 | 879 | -85.4 | 504990 | 489 | -91.5 | 504990 | 82 | -100.1 | 504990 | 7 |
| MR_1774412876_41EF9A3A | 504990 | 879 | -86.2 | 504990 | 489 | -92.9 | 504990 | 82 | -98.8 | 504990 | 7 |
| MR_1774412876_A44CD0CE | 504990 | 879 | -86.0 | 504990 | 489 | -91.8 | 504990 | 82 | -100.9 | 504990 | 7 |
| MR_1774412876_22563D67 | 504990 | 879 | -86.4 | 504990 | 489 | -91.2 | 504990 | 82 | -100.2 | 504990 | 7 |
| MR_1774412876_2289290D | 504990 | 879 | -85.9 | 504990 | 489 | -94.0 | 504990 | 82 | -97.7 | 504990 | 7 |
| MR_1774412876_DB5B77A0 | 504990 | 879 | -85.5 | 504990 | 489 | -94.6 | 504990 | 82 | -98.3 | 504990 | 7 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 266: `2e4e0bf3-bf1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2e4e0bf3-bf10-4a8e-b768-148139ffae12` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease A3 Offset threshold for 3267094_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[266] topology](images/train_0266.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262008_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267094_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267094_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262008_3
- `C6`: Adjust the azimuth of 3267094_2 by 50 degrees
- `C7`: Add neighbor relationship between 3230117_1 and 3262008_3
- `C8`: Increase transmission power for 3267094_2
- `C9`: Lift the tilt angle of 3267094_2 by 7 degrees
- `C10`: Add neighbor relationship between 3267094_2 and 3262008_3
- `C11`: Press down the tilt angle  of 3262008_3 by 10 degrees
- `C12`: Adjust the azimuth of 3262008_3 by 24 degrees
- `C13`: Increase A3 Offset threshold for 3267094_2
- `C14`: Increase transmission power for 3262008_3
- `C15`: Decrease A3 Offset threshold for 3262008_3
- `C16`: Check test server and transmission issues
- `C17`: Decrease transmission power for 3267094_2
- `C18`: Press down the tilt angle of 3267094_2 by 7 degrees
- `C19`: Decrease transmission power for 3262008_3
- `C20`: Lift the tilt angle  of 3262008_3 by 10 degrees
- `C21`: Decrease A3 Offset threshold for 3267094_2 **← 정답**
- `C22`: Increase A3 Offset threshold for 3262008_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.872 | MS1 | 121.4656616400 | 31.1446223429 | 67 | 504990 | -82.42 | 15.91 | 410.08 | 0.04 | 2.60 | 1594 |
| 2024-09-20 22:21:32.636 | MS1 | 121.4656658313 | 31.1446322802 | 67 | 504990 | -79.32 | 14.38 | 527.73 | 0.14 | 2.83 | 1562 |
| 2024-09-20 22:21:33.859 | MS1 | 121.4656726331 | 31.1446198414 | 67 | 504990 | -82.89 | 13.15 | 344.33 | 0.13 | 2.90 | 1568 |
| 2024-09-20 22:21:34.515 | MS1 | 121.4656605455 | 31.1446217326 | 67 | 504990 | -89.97 | -3.87 | 48.08 | 0.11 | 1.08 | 1586 |
| 2024-09-20 22:21:35.365 | MS1 | 121.4656627673 | 31.1446313415 | 67 | 504990 | -88.23 | -3.37 | 43.17 | 0.18 | 1.47 | 1584 |
| 2024-09-20 22:21:36.719 | MS1 | 121.4656751833 | 31.1446307829 | 67 | 504990 | -89.73 | -2.40 | 63.04 | 0.11 | 1.00 | 1582 |
| 2024-09-20 22:21:37.768 | MS1 | 121.4656646362 | 31.1446370972 | 67 | 504990 | -87.95 | -1.31 | 58.10 | 0.05 | 1.30 | 1567 |
| 2024-09-20 22:21:38.981 | MS1 | 121.4656773491 | 31.1446339307 | 67 | 504990 | -87.61 | -0.95 | 45.40 | 0.11 | 1.20 | 1587 |
| 2024-09-20 22:21:39.565 | MS1 | 121.4656599802 | 31.1446215521 | 365 | 504990 | -76.46 | 14.95 | 259.23 | 0.14 | 1.21 | 1580 |
| 2024-09-20 22:21:40.443 | MS1 | 121.4656603030 | 31.1446219369 | 365 | 504990 | -80.20 | 15.78 | 307.00 | 0.12 | 2.73 | 1562 |
| 2024-09-20 22:21:41.123 | MS1 | 121.4656762349 | 31.1446327656 | 365 | 504990 | -82.40 | 12.83 | 374.20 | 0.00 | 2.58 | 1561 |
| 2024-09-20 22:21:42.281 | MS1 | 121.4656747160 | 31.1446367670 | 365 | 504990 | -79.07 | 13.83 | 568.55 | 0.18 | 2.65 | 1595 |

> *... 20개 열 생략 (전체 32열)*

<details>
<summary>UE 데이터 해석 가이드</summary>

- **Timestamp**: 측정 시각 (초 단위 정밀도)
- **SS-RSRP (dBm)**: 참조 신호 수신 전력. -100 이하는 약한 신호
- **SS-SINR (dB)**: 신호 대 간섭+잡음비. 5 이하는 간섭 심각, 10 이상은 양호
- **DL Throughput (Mbps)**: 다운링크 처리량. 100 미만은 성능 저하 의심
- **Serving PCI**: 현재 서빙 셀의 물리적 셀 ID. 값이 바뀌면 핸드오버 발생

</details>

**기지국 구성 (Network Configuration)**

| gNodeB ID | Cell ID | Longitude | Latitude | Mechanical Azimuth | Mechanical Downtilt | Digital Tilt | Height | Duplex Mode | PCI | Band | DL ARFCN | BW [MHz] | TxRx Mode | Transmission Power | ARFCN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3230117 | 1 | 121.4742076321 | 31.1460918372 | 40 | 3 | 5 | 41.1 | TDD | 984 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3262008 | 3 | 121.4648943087 | 31.1494820770 | 148 | 12 | 7 | 36.5 | TDD | 365 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3265287 | 4 | 121.4750436399 | 31.1505608464 | 346 | 14 | 3 | 47.3 | TDD | 598 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3267094 | 2 | 121.4704343603 | 31.1553988032 | 135 | 6 | 5 | 16.1 | TDD | 67 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

> *... 12개 열 생략 (전체 28열)*

<details>
<summary>기지국 구성 해석 가이드</summary>

- **Mechanical Azimuth**: 안테나 수평 방향 (0°=북, 90°=동)
- **Mechanical Downtilt + Digital Tilt**: 합계가 안테나 하향각. 20° 이상이면 과도한 downtilt
- **Transmission Power**: 송신 전력 (dBm). 높을수록 커버리지 넓음
- **IntraFreqHoA3Offset**: A3 핸드오버 임계값 (0.5dB 단위). 10 이상이면 핸드오버 지연
- **PdcchOccupiedSymbolNum**: PDCCH 리소스 할당. 1SYM은 기본, 2SYM은 확장
- **CovInterFreqA2RsrpThld**: Inter-freq 커버리지 임계값. -95가 -105보다 보수적 (높음)
- **PCell Neighbor Cell**: 설정된 이웃 셀 목록 (핸드오버 후보)

</details>

**시그널링 이벤트 (Signaling Plane)**

| Timestamp | Event Name | Event Content |
| --- | --- | --- |
| 2024-09-20 22:21:30.991 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.015 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.124 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.124 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.862 | NREventA3 | measId:2;ServCellPCI:100;Se... |
| 2024-09-20 22:21:38.102 | NRHandoverAttempt | SourcePCI:100;SourceNR-ARFC... |
| 2024-09-20 22:21:38.142 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.157 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.283 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.283 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230117 | 1 | 9.9368 | 11.2226 | -115.3711 | 10.3509 | 97.9882 | 0.0004 | 0.0043 |
| 2024_09_20 22:00 | 3267094 | 2 | 9.0883 | 15.7989 | -114.4610 | 10.2913 | 180.6533 | 0.0099 | 0.1836 |
| 2024_09_20 22:00 | 3262008 | 3 | 11.1938 | 13.8135 | -114.5225 | 15.2171 | 128.0994 | 0.0042 | 0.0025 |
| 2024_09_20 22:00 | 3265287 | 4 | 5.9914 | 9.5000 | -117.4597 | 11.1255 | 166.4671 | 0.0180 | 0.0173 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415518_10DA43A1 | 504990 | 67 | -90.7 | 504990 | 365 | -81.7 | 504990 | 984 | -84.9 | 504990 | 598 |
| MR_1774415518_B0688F74 | 504990 | 67 | -89.3 | 504990 | 365 | -84.4 | 504990 | 984 | -87.0 | 504990 | 598 |
| MR_1774415518_29D76E2B | 504990 | 365 | -82.3 | 504990 | 67 | -91.9 | 504990 | 984 | -84.3 | 504990 | 598 |
| MR_1774415518_78D9C9FC | 504990 | 67 | -91.6 | 504990 | 365 | -84.3 | 504990 | 984 | -87.5 | 504990 | 598 |
| MR_1774415518_CF25F46C | 504990 | 365 | -84.4 | 504990 | 67 | -91.9 | 504990 | 984 | -84.0 | 504990 | 598 |
| MR_1774415518_FC6C1396 | 504990 | 67 | -88.2 | 504990 | 365 | -81.6 | 504990 | 984 | -85.4 | 504990 | 598 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 267: `6f2a33f8-500...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6f2a33f8-500f-49d4-bb85-9f0a7e647f89` |
| Tag | **multiple-answer** |
| 정답 | **C1|C16** |
| C1 의미 | Increase transmission power for 3239559_4 |
| C16 의미 | Adjust the azimuth of 3239559_4 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[267] topology](images/train_0267.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3239559_4 **← 정답**
- `C2`: Add neighbor relationship between 3239559_4 and 3267698_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267698_1
- `C4`: Lift the tilt angle  of 3267698_1 by 2 degrees
- `C5`: Increase transmission power for 3267698_1
- `C6`: Decrease A3 Offset threshold for 3239559_4
- `C7`: Decrease transmission power for 3239559_4
- `C8`: Decrease A3 Offset threshold for 3267698_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239559_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239559_4
- `C11`: Adjust the azimuth of 3267698_1 by 50 degrees
- `C12`: Lift the tilt angle of 3239559_4 by 10 degrees
- `C13`: Increase A3 Offset threshold for 3267698_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Add neighbor relationship between 3225792_3 and 3267698_1
- `C16`: Adjust the azimuth of 3239559_4 by 50 degrees **← 정답**
- `C17`: Increase A3 Offset threshold for 3239559_4
- `C18`: Check test server and transmission issues
- `C19`: Press down the tilt angle of 3239559_4 by 10 degrees
- `C20`: Press down the tilt angle  of 3267698_1 by 2 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267698_1
- `C22`: Decrease transmission power for 3267698_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.556 | MS1 | 121.4656633245 | 31.1446310861 | 613 | 504990 | -94.61 | 15.56 | 502.48 | 0.06 | 2.99 | 1566 |
| 2024-09-20 22:21:32.610 | MS1 | 121.4656770108 | 31.1446361220 | 613 | 504990 | -86.72 | 14.00 | 442.85 | 0.03 | 2.86 | 1590 |
| 2024-09-20 22:21:33.554 | MS1 | 121.4656723665 | 31.1446203954 | 613 | 504990 | -89.06 | 13.20 | 522.38 | 0.02 | 2.92 | 1598 |
| 2024-09-20 22:21:34.119 | MS1 | 121.4656727475 | 31.1446253293 | 613 | 504990 | -106.65 | 0.59 | 62.60 | 0.10 | 1.33 | 1579 |
| 2024-09-20 22:21:35.513 | MS1 | 121.4656609123 | 31.1446373536 | 613 | 504990 | -100.68 | 1.11 | 28.63 | 0.05 | 1.21 | 1576 |
| 2024-09-20 22:21:36.611 | MS1 | 121.4656768677 | 31.1446346536 | 613 | 504990 | -101.69 | 0.32 | 54.18 | 0.15 | 1.17 | 1577 |
| 2024-09-20 22:21:37.976 | MS1 | 121.4656735115 | 31.1446214456 | 613 | 504990 | -108.59 | 0.68 | 78.19 | 0.09 | 1.06 | 1588 |
| 2024-09-20 22:21:38.861 | MS1 | 121.4656758877 | 31.1446369365 | 613 | 504990 | -106.13 | -0.57 | 25.32 | 0.13 | 1.03 | 1577 |
| 2024-09-20 22:21:39.548 | MS1 | 121.4656602850 | 31.1446331993 | 613 | 504990 | -104.34 | -0.08 | 54.56 | 0.20 | 1.32 | 1594 |
| 2024-09-20 22:21:40.955 | MS1 | 121.4656643897 | 31.1446196480 | 613 | 504990 | -86.40 | 12.68 | 423.23 | 0.18 | 2.14 | 1578 |
| 2024-09-20 22:21:41.463 | MS1 | 121.4656697523 | 31.1446362509 | 613 | 504990 | -89.76 | 17.61 | 536.26 | 0.02 | 2.77 | 1564 |
| 2024-09-20 22:21:42.879 | MS1 | 121.4656662808 | 31.1446253422 | 613 | 504990 | -90.43 | 15.36 | 550.22 | 0.17 | 2.42 | 1567 |

> *... 20개 열 생략 (전체 32열)*

<details>
<summary>UE 데이터 해석 가이드</summary>

- **Timestamp**: 측정 시각 (초 단위 정밀도)
- **SS-RSRP (dBm)**: 참조 신호 수신 전력. -100 이하는 약한 신호
- **SS-SINR (dB)**: 신호 대 간섭+잡음비. 5 이하는 간섭 심각, 10 이상은 양호
- **DL Throughput (Mbps)**: 다운링크 처리량. 100 미만은 성능 저하 의심
- **Serving PCI**: 현재 서빙 셀의 물리적 셀 ID. 값이 바뀌면 핸드오버 발생

</details>

**기지국 구성 (Network Configuration)**

| gNodeB ID | Cell ID | Longitude | Latitude | Mechanical Azimuth | Mechanical Downtilt | Digital Tilt | Height | Duplex Mode | PCI | Band | DL ARFCN | BW [MHz] | TxRx Mode | Transmission Power | ARFCN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3225792 | 3 | 121.4725741551 | 31.1476108691 | 236 | 6 | 8 | 44.1 | TDD | 1004 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3239559 | 4 | 121.4740484238 | 31.1493584964 | 297 | 15 | 9 | 22.3 | TDD | 613 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3267698 | 1 | 121.4731062258 | 31.1548471933 | 162 | 1 | 1 | 26.7 | TDD | 898 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3275701 | 2 | 121.4722507273 | 31.1486267107 | 287 | 3 | 8 | 43.2 | TDD | 155 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

> *... 12개 열 생략 (전체 28열)*

<details>
<summary>기지국 구성 해석 가이드</summary>

- **Mechanical Azimuth**: 안테나 수평 방향 (0°=북, 90°=동)
- **Mechanical Downtilt + Digital Tilt**: 합계가 안테나 하향각. 20° 이상이면 과도한 downtilt
- **Transmission Power**: 송신 전력 (dBm). 높을수록 커버리지 넓음
- **IntraFreqHoA3Offset**: A3 핸드오버 임계값 (0.5dB 단위). 10 이상이면 핸드오버 지연
- **PdcchOccupiedSymbolNum**: PDCCH 리소스 할당. 1SYM은 기본, 2SYM은 확장
- **CovInterFreqA2RsrpThld**: Inter-freq 커버리지 임계값. -95가 -105보다 보수적 (높음)
- **PCell Neighbor Cell**: 설정된 이웃 셀 목록 (핸드오버 후보)

</details>

**시그널링 이벤트 (Signaling Plane)**

| Timestamp | Event Name | Event Content |
| --- | --- | --- |
| 2024-09-20 22:21:30.913 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.933 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.079 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.079 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.308 | NREventA2 | measId:1;ServCellPCI:434;Se... |
| 2024-09-20 22:21:34.426 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267698 | 1 | 18.5020 | 6.8274 | -117.9498 | 17.9966 | 112.9628 | 0.0134 | 0.0002 |
| 2024_09_20 22:00 | 3275701 | 2 | 7.6683 | 8.3457 | -115.0852 | 9.5363 | 92.7348 | 0.0194 | 0.0151 |
| 2024_09_20 22:00 | 3225792 | 3 | 9.7582 | 9.3156 | -115.5290 | 17.8454 | 164.2033 | 0.0019 | 0.0010 |
| 2024_09_20 22:00 | 3239559 | 4 | 12.6450 | 15.5123 | -117.9565 | 13.4108 | 191.0597 | 0.1567 | 0.0178 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417025_E82564F0 | 504990 | 613 | -108.0 | 504990 | 898 | -112.2 | 504990 | 1004 | -120.7 | 504990 | 155 |
| MR_1774417025_0C2D43B2 | 504990 | 613 | -105.9 | 504990 | 898 | -115.2 | 504990 | 1004 | -119.1 | 504990 | 155 |
| MR_1774417025_580DC258 | 504990 | 613 | -106.5 | 504990 | 898 | -113.7 | 504990 | 1004 | -118.6 | 504990 | 155 |
| MR_1774417025_3BCE5089 | 504990 | 613 | -105.5 | 504990 | 898 | -114.2 | 504990 | 1004 | -121.9 | 504990 | 155 |
| MR_1774417025_7AFC15E4 | 504990 | 613 | -105.4 | 504990 | 898 | -115.0 | 504990 | 1004 | -118.4 | 504990 | 155 |
| MR_1774417025_462130DA | 504990 | 613 | -106.1 | 504990 | 898 | -112.9 | 504990 | 1004 | -121.4 | 504990 | 155 |
| MR_1774417025_CE2468E5 | 504990 | 613 | -105.2 | 504990 | 898 | -112.2 | 504990 | 1004 | -118.7 | 504990 | 155 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 268: `59e62190-f05...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `59e62190-f052-40db-b460-db48522b3111` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease A3 Offset threshold for 3261199_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[268] topology](images/train_0268.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3261199_2 by 10 degrees
- `C2`: Add neighbor relationship between 3224147_4 and 3241327_1
- `C3`: Increase A3 Offset threshold for 3241327_1
- `C4`: Increase transmission power for 3241327_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261199_2
- `C6`: Adjust the azimuth of 3241327_1 by 50 degrees
- `C7`: Decrease transmission power for 3261199_2
- `C8`: Increase A3 Offset threshold for 3261199_2
- `C9`: Lift the tilt angle of 3261199_2 by 10 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241327_1
- `C11`: Increase transmission power for 3261199_2
- `C12`: Press down the tilt angle  of 3241327_1 by 10 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease A3 Offset threshold for 3261199_2 **← 정답**
- `C15`: Decrease A3 Offset threshold for 3241327_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241327_1
- `C17`: Adjust the azimuth of 3261199_2 by 50 degrees
- `C18`: Decrease transmission power for 3241327_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261199_2
- `C20`: Lift the tilt angle  of 3241327_1 by 10 degrees
- `C21`: Check test server and transmission issues
- `C22`: Add neighbor relationship between 3261199_2 and 3241327_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.436 | MS1 | 121.4656675796 | 31.1446320495 | 324 | 504990 | -83.34 | 14.56 | 520.44 | 0.10 | 2.28 | 1594 |
| 2024-09-20 22:21:32.105 | MS1 | 121.4656650262 | 31.1446332872 | 324 | 504990 | -79.25 | 17.66 | 463.13 | 0.20 | 2.50 | 1591 |
| 2024-09-20 22:21:33.986 | MS1 | 121.4656693066 | 31.1446305286 | 324 | 504990 | -76.74 | 12.09 | 486.62 | 0.01 | 2.31 | 1583 |
| 2024-09-20 22:21:34.457 | MS1 | 121.4656766712 | 31.1446363410 | 324 | 504990 | -86.23 | -1.60 | 29.28 | 0.14 | 1.24 | 1578 |
| 2024-09-20 22:21:35.521 | MS1 | 121.4656778470 | 31.1446183824 | 324 | 504990 | -85.53 | -1.37 | 54.28 | 0.13 | 1.48 | 1571 |
| 2024-09-20 22:21:36.465 | MS1 | 121.4656657016 | 31.1446224457 | 324 | 504990 | -91.52 | -1.10 | 55.16 | 0.06 | 1.36 | 1600 |
| 2024-09-20 22:21:37.873 | MS1 | 121.4656642910 | 31.1446290851 | 324 | 504990 | -83.94 | -1.36 | 42.26 | 0.17 | 1.08 | 1583 |
| 2024-09-20 22:21:38.914 | MS1 | 121.4656721257 | 31.1446188356 | 324 | 504990 | -87.32 | -1.87 | 81.21 | 0.11 | 1.27 | 1569 |
| 2024-09-20 22:21:39.679 | MS1 | 121.4656629525 | 31.1446215343 | 488 | 504990 | -83.01 | 16.60 | 193.08 | 0.00 | 1.03 | 1595 |
| 2024-09-20 22:21:40.117 | MS1 | 121.4656636409 | 31.1446271491 | 488 | 504990 | -83.85 | 13.60 | 535.10 | 0.06 | 2.03 | 1589 |
| 2024-09-20 22:21:41.578 | MS1 | 121.4656620133 | 31.1446365103 | 488 | 504990 | -81.85 | 14.34 | 523.99 | 0.17 | 2.39 | 1568 |
| 2024-09-20 22:21:42.560 | MS1 | 121.4656702998 | 31.1446248712 | 488 | 504990 | -79.55 | 17.47 | 575.34 | 0.09 | 2.17 | 1598 |

> *... 20개 열 생략 (전체 32열)*

<details>
<summary>UE 데이터 해석 가이드</summary>

- **Timestamp**: 측정 시각 (초 단위 정밀도)
- **SS-RSRP (dBm)**: 참조 신호 수신 전력. -100 이하는 약한 신호
- **SS-SINR (dB)**: 신호 대 간섭+잡음비. 5 이하는 간섭 심각, 10 이상은 양호
- **DL Throughput (Mbps)**: 다운링크 처리량. 100 미만은 성능 저하 의심
- **Serving PCI**: 현재 서빙 셀의 물리적 셀 ID. 값이 바뀌면 핸드오버 발생

</details>

**기지국 구성 (Network Configuration)**

| gNodeB ID | Cell ID | Longitude | Latitude | Mechanical Azimuth | Mechanical Downtilt | Digital Tilt | Height | Duplex Mode | PCI | Band | DL ARFCN | BW [MHz] | TxRx Mode | Transmission Power | ARFCN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3224147 | 4 | 121.4653154454 | 31.1458852918 | 89 | 11 | 12 | 27.9 | TDD | 767 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3234188 | 3 | 121.4703823862 | 31.1471778101 | 212 | 9 | 3 | 26.7 | TDD | 654 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3241327 | 1 | 121.4711284230 | 31.1468030743 | 324 | 10 | 11 | 27.8 | TDD | 488 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3261199 | 2 | 121.4665484301 | 31.1532634568 | 299 | 15 | 7 | 46.9 | TDD | 324 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

> *... 12개 열 생략 (전체 28열)*

<details>
<summary>기지국 구성 해석 가이드</summary>

- **Mechanical Azimuth**: 안테나 수평 방향 (0°=북, 90°=동)
- **Mechanical Downtilt + Digital Tilt**: 합계가 안테나 하향각. 20° 이상이면 과도한 downtilt
- **Transmission Power**: 송신 전력 (dBm). 높을수록 커버리지 넓음
- **IntraFreqHoA3Offset**: A3 핸드오버 임계값 (0.5dB 단위). 10 이상이면 핸드오버 지연
- **PdcchOccupiedSymbolNum**: PDCCH 리소스 할당. 1SYM은 기본, 2SYM은 확장
- **CovInterFreqA2RsrpThld**: Inter-freq 커버리지 임계값. -95가 -105보다 보수적 (높음)
- **PCell Neighbor Cell**: 설정된 이웃 셀 목록 (핸드오버 후보)

</details>

**시그널링 이벤트 (Signaling Plane)**

| Timestamp | Event Name | Event Content |
| --- | --- | --- |
| 2024-09-20 22:21:31.374 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.398 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.516 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.516 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.259 | NREventA3 | measId:2;ServCellPCI:405;Se... |
| 2024-09-20 22:21:38.499 | NRHandoverAttempt | SourcePCI:405;SourceNR-ARFC... |
| 2024-09-20 22:21:38.547 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.562 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.697 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.697 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241327 | 1 | 9.1660 | 16.6246 | -114.8658 | 18.3945 | 102.1164 | 0.0100 | 0.0052 |
| 2024_09_20 22:00 | 3261199 | 2 | 15.0728 | 14.8874 | -115.2765 | 10.6978 | 141.5253 | 0.0001 | 0.1716 |
| 2024_09_20 22:00 | 3234188 | 3 | 16.8448 | 8.3214 | -115.1902 | 14.7209 | 102.6060 | 0.0102 | 0.0081 |
| 2024_09_20 22:00 | 3224147 | 4 | 11.8196 | 9.1192 | -115.6189 | 16.8781 | 82.1287 | 0.0145 | 0.0075 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417115_1B7F6285 | 504990 | 324 | -84.4 | 504990 | 488 | -82.8 | 504990 | 767 | -90.3 | 504990 | 654 |
| MR_1774417115_0DF0B4AC | 504990 | 324 | -84.8 | 504990 | 488 | -80.7 | 504990 | 767 | -89.1 | 504990 | 654 |
| MR_1774417115_37AB4EBA | 504990 | 324 | -84.3 | 504990 | 488 | -81.4 | 504990 | 767 | -87.9 | 504990 | 654 |
| MR_1774417115_E3631CED | 504990 | 324 | -84.5 | 504990 | 488 | -83.2 | 504990 | 767 | -88.1 | 504990 | 654 |
| MR_1774417115_F4C1482C | 504990 | 324 | -85.6 | 504990 | 488 | -83.8 | 504990 | 767 | -90.1 | 504990 | 654 |
| MR_1774417115_E5574ECB | 504990 | 324 | -85.2 | 504990 | 488 | -81.8 | 504990 | 767 | -87.4 | 504990 | 654 |
| MR_1774417115_0F65EA86 | 504990 | 324 | -87.2 | 504990 | 488 | -81.1 | 504990 | 767 | -90.4 | 504990 | 654 |
| MR_1774417115_21E4338E | 504990 | 488 | -81.0 | 504990 | 324 | -87.0 | 504990 | 767 | -89.2 | 504990 | 654 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 269: `9d082f00-4e6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9d082f00-4e6a-478c-a340-8284324775a7` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248909_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[269] topology](images/train_0269.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3236626_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236626_2
- `C4`: Press down the tilt angle  of 3236626_2 by 4 degrees
- `C5`: Check test server and transmission issues
- `C6`: Lift the tilt angle of 3248909_5 by 6 degrees
- `C7`: Press down the tilt angle of 3248909_5 by 6 degrees
- `C8`: Adjust the azimuth of 3236626_2 by 14 degrees
- `C9`: Increase A3 Offset threshold for 3248909_5
- `C10`: Decrease A3 Offset threshold for 3248909_5
- `C11`: Add neighbor relationship between 3248909_5 and 3236626_2
- `C12`: Lift the tilt angle  of 3236626_2 by 4 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248909_5 **← 정답**
- `C14`: Increase transmission power for 3248909_5
- `C15`: Add neighbor relationship between 3218159_13 and 3236626_2
- `C16`: Adjust the azimuth of 3248909_5 by 40 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248909_5
- `C18`: Increase A3 Offset threshold for 3236626_2
- `C19`: Decrease transmission power for 3248909_5
- `C20`: Decrease transmission power for 3236626_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236626_2
- `C22`: Decrease A3 Offset threshold for 3236626_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.538 | MS1 | 121.4656628847 | 31.1446328775 | 826 | 504990 | -93.69 | 11.74 | 574.31 | 0.08 | 2.39 | 1596 |
| 2024-09-20 22:21:32.540 | MS1 | 121.4656768176 | 31.1446283144 | 916 | 504990 | -94.21 | 12.01 | 328.36 | 0.07 | 2.43 | 1590 |
| 2024-09-20 22:21:33.719 | MS1 | 121.4656767610 | 31.1446205441 | 534 | 504990 | -95.17 | 10.97 | 353.36 | 0.17 | 2.74 | 1599 |
| 2024-09-20 22:21:34.840 | MS1 | 121.4656744727 | 31.1446196159 | 1007 | 152650 | -94.93 | 3.15 | 82.83 | 0.16 | 1.54 | 985 |
| 2024-09-20 22:21:35.819 | MS1 | 121.4656741848 | 31.1446377722 | 456 | 152650 | -89.85 | 6.50 | 64.44 | 0.20 | 1.55 | 998 |
| 2024-09-20 22:21:36.652 | MS1 | 121.4656708995 | 31.1446207525 | 509 | 152650 | -87.63 | 7.71 | 100.58 | 0.14 | 1.63 | 905 |
| 2024-09-20 22:21:37.267 | MS1 | 121.4656596997 | 31.1446320775 | 706 | 152650 | -93.00 | 7.43 | 60.00 | 0.02 | 1.94 | 924 |
| 2024-09-20 22:21:38.884 | MS1 | 121.4656686691 | 31.1446303796 | 1007 | 152650 | -91.06 | 2.26 | 71.20 | 0.11 | 1.63 | 917 |
| 2024-09-20 22:21:39.794 | MS1 | 121.4656615437 | 31.1446309563 | 456 | 152650 | -95.95 | 2.64 | 48.28 | 0.19 | 1.70 | 973 |
| 2024-09-20 22:21:40.153 | MS1 | 121.4656644821 | 31.1446214516 | 509 | 152650 | -91.11 | 4.87 | 49.53 | 0.12 | 2.59 | 1560 |
| 2024-09-20 22:21:41.148 | MS1 | 121.4656779185 | 31.1446189459 | 706 | 152650 | -93.07 | 4.02 | 64.60 | 0.17 | 2.90 | 1566 |
| 2024-09-20 22:21:42.352 | MS1 | 121.4656676043 | 31.1446180068 | 1007 | 152650 | -92.53 | 4.41 | 79.56 | 0.20 | 2.04 | 1575 |

> *... 20개 열 생략 (전체 32열)*

<details>
<summary>UE 데이터 해석 가이드</summary>

- **Timestamp**: 측정 시각 (초 단위 정밀도)
- **SS-RSRP (dBm)**: 참조 신호 수신 전력. -100 이하는 약한 신호
- **SS-SINR (dB)**: 신호 대 간섭+잡음비. 5 이하는 간섭 심각, 10 이상은 양호
- **DL Throughput (Mbps)**: 다운링크 처리량. 100 미만은 성능 저하 의심
- **Serving PCI**: 현재 서빙 셀의 물리적 셀 ID. 값이 바뀌면 핸드오버 발생

</details>

**기지국 구성 (Network Configuration)**

| gNodeB ID | Cell ID | Longitude | Latitude | Mechanical Azimuth | Mechanical Downtilt | Digital Tilt | Height | Duplex Mode | PCI | Band | DL ARFCN | BW [MHz] | TxRx Mode | Transmission Power | ARFCN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3218159 | 13 | 121.4684738417 | 31.1552423079 | 348 | 14 | 0 | 10.6 | FDD | 509 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3225577 | 9 | 121.4642846009 | 31.1456491473 | 81 | 7 | 0 | 13.9 | FDD | 456 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3226681 | 4 | 121.4712817092 | 31.1546102841 | 358 | 6 | 11 | 5.1 | TDD | 534 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3228594 | 8 | 121.4718251448 | 31.1522621399 | 226 | 0 | 1 | 25.5 | FDD | 227 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3230687 | 1 | 121.4652823752 | 31.1505472136 | 60 | 9 | 0 | 17.0 | TDD | 387 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3234058 | 3 | 121.4691293894 | 31.1490632911 | 31 | 4 | 12 | 17.8 | TDD | 916 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3234674 | 6 | 121.4646838597 | 31.1500147202 | 26 | 3 | 12 | 0.3 | TDD | 701 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3236626 | 2 | 121.4659093495 | 31.1542540780 | 195 | 4 | 0 | 1.5 | TDD | 168 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3245287 | 12 | 121.4723816294 | 31.1500767948 | 38 | 14 | 10 | 13.7 | FDD | 312 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3247158 | 11 | 121.4670180302 | 31.1509187252 | 126 | 13 | 10 | 1.0 | FDD | 146 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3248909 | 5 | 121.4666100849 | 31.1470666448 | 238 | 5 | 12 | 3.8 | TDD | 826 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3272030 | 10 | 121.4668606646 | 31.1470940533 | 144 | 2 | 3 | 21.6 | FDD | 1007 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3279017 | 7 | 121.4755985408 | 31.1509915095 | 88 | 1 | 11 | 4.2 | FDD | 706 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |

> *... 12개 열 생략 (전체 28열)*

<details>
<summary>기지국 구성 해석 가이드</summary>

- **Mechanical Azimuth**: 안테나 수평 방향 (0°=북, 90°=동)
- **Mechanical Downtilt + Digital Tilt**: 합계가 안테나 하향각. 20° 이상이면 과도한 downtilt
- **Transmission Power**: 송신 전력 (dBm). 높을수록 커버리지 넓음
- **IntraFreqHoA3Offset**: A3 핸드오버 임계값 (0.5dB 단위). 10 이상이면 핸드오버 지연
- **PdcchOccupiedSymbolNum**: PDCCH 리소스 할당. 1SYM은 기본, 2SYM은 확장
- **CovInterFreqA2RsrpThld**: Inter-freq 커버리지 임계값. -95가 -105보다 보수적 (높음)
- **PCell Neighbor Cell**: 설정된 이웃 셀 목록 (핸드오버 후보)

</details>

**시그널링 이벤트 (Signaling Plane)**

| Timestamp | Event Name | Event Content |
| --- | --- | --- |
| 2024-09-20 22:21:31.131 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.148 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.291 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.291 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.939 | NREventA2 | measId:1;ServCellPCI:227;Se... |
| 2024-09-20 22:21:35.077 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.296 | NREventA5 | measId:3;ServCellPCI:227;Se... |
| 2024-09-20 22:21:35.330 | NRHandoverAttempt | SourcePCI:227;SourceNR-ARFC... |
| 2024-09-20 22:21:35.375 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.390 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.520 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.520 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230687 | 1 | 13.2097 | 14.4511 | -116.5207 | 13.9455 | 87.9008 | 0.0175 | 0.0004 |
| 2024_09_20 22:00 | 3236626 | 2 | 15.7297 | 11.5406 | -114.7019 | 6.3789 | 189.4118 | 0.0070 | 0.0104 |
| 2024_09_20 22:00 | 3234058 | 3 | 13.7504 | 12.1515 | -115.5064 | 10.1586 | 100.9943 | 0.0067 | 0.0001 |
| 2024_09_20 22:00 | 3226681 | 4 | 16.4454 | 11.0127 | -117.7300 | 9.3293 | 135.5727 | 0.0072 | 0.0189 |
| 2024_09_20 22:00 | 3248909 | 5 | 10.9769 | 5.7413 | -116.2594 | 14.9036 | 127.4445 | 0.0133 | 0.0170 |
| 2024_09_20 22:00 | 3234674 | 6 | 8.5760 | 10.5799 | -115.9950 | 16.5483 | 148.5581 | 0.0174 | 0.0060 |
| 2024_09_20 22:00 | 3279017 | 7 | 13.9948 | 10.9982 | -116.8423 | 3.7032 | 25.6544 | 0.0072 | 0.0155 |
| 2024_09_20 22:00 | 3228594 | 8 | 19.1532 | 8.0733 | -117.2249 | 3.7574 | 28.2398 | 0.0103 | 0.0148 |
| 2024_09_20 22:00 | 3225577 | 9 | 10.8550 | 12.9451 | -117.9117 | 3.6123 | 51.3690 | 0.0029 | 0.0072 |
| 2024_09_20 22:00 | 3272030 | 10 | 13.2820 | 10.4627 | -116.4678 | 4.5839 | 58.8913 | 0.0143 | 0.0015 |
| 2024_09_20 22:00 | 3247158 | 11 | 6.9376 | 18.2020 | -115.3223 | 3.7339 | 27.8494 | 0.0102 | 0.0197 |
| 2024_09_20 22:00 | 3245287 | 12 | 12.0967 | 19.3649 | -116.7180 | 4.8410 | 29.8000 | 0.0005 | 0.0033 |
| 2024_09_20 22:00 | 3218159 | 13 | 17.3043 | 15.1025 | -114.0888 | 3.3707 | 50.6009 | 0.0118 | 0.0171 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413027_EA0DE829 | 504990 | 534 | -97.0 | 504990 | 168 | -99.7 | 504990 | 387 | -101.1 | 504990 | 701 |
| MR_1774413027_260B9596 | 152650 | 1007 | -93.9 | 152650 | 227 | -100.1 | 152650 | 146 | -106.2 | 152650 | 312 |
| MR_1774413027_55E16428 | 152650 | 1007 | -96.3 | 152650 | 227 | -98.5 | 152650 | 146 | -108.5 | 152650 | 312 |
| MR_1774413027_5339BE09 | 504990 | 534 | -96.1 | 504990 | 168 | -97.2 | 504990 | 387 | -101.9 | 504990 | 701 |
| MR_1774413027_C262CB9C | 504990 | 534 | -96.3 | 504990 | 168 | -98.3 | 504990 | 387 | -102.9 | 504990 | 701 |
| MR_1774413027_D2BB155C | 504990 | 534 | -93.8 | 504990 | 168 | -96.2 | 504990 | 387 | -104.7 | 504990 | 701 |

> *... 2개 열 생략 (전체 14열)*

---
