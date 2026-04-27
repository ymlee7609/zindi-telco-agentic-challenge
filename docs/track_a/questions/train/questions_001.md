# Track A 문제 분석 — train[0]~train[9]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[0] ~ train[9] (10개)

## 목차

1. [문제 0: `08e221e5-3ed...`](#0) — multiple-answer, 정답: C2|C8|C11|C16
2. [문제 1: `0cd874c0-eab...`](#1) — single-answer, 정답: C9
3. [문제 2: `ac53a506-f1d...`](#2) — single-answer, 정답: C16
4. [문제 3: `39bb305f-5d4...`](#3) — single-answer, 정답: C10
5. [문제 4: `0ec53773-5b5...`](#4) — single-answer, 정답: C3
6. [문제 5: `01511464-4a9...`](#5) — single-answer, 정답: C8
7. [문제 6: `af48c90d-a33...`](#6) — single-answer, 정답: C9
8. [문제 7: `a60de966-400...`](#7) — single-answer, 정답: C10
9. [문제 8: `be9c0764-b59...`](#8) — single-answer, 정답: C13
10. [문제 9: `8fbe9492-d54...`](#9) — single-answer, 정답: C16

---

### 문제 0: `08e221e5-3ed...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `08e221e5-3ed8-42ed-b7b3-0fd9dfd8d99e` |
| Tag | **multiple-answer** |
| 정답 | **C2|C8|C11|C16** |
| C2 의미 | Decrease transmission power for 3279943_1 |
| C8 의미 | Press down the tilt angle  of 3279943_1 by 4 degrees |
| C11 의미 | Increase A3 Offset threshold for 3279943_1 |
| C16 의미 | Increase A3 Offset threshold for 3267220_2 |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[0] topology](images/train_0000.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3267220_2 and 3279943_1
- `C2`: Decrease transmission power for 3279943_1 **← 정답**
- `C3`: Increase transmission power for 3267220_2
- `C4`: Check test server and transmission issues
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279943_1
- `C6`: Add neighbor relationship between 3239189_4 and 3279943_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267220_2
- `C8`: Press down the tilt angle  of 3279943_1 by 4 degrees **← 정답**
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279943_1
- `C10`: Adjust the azimuth of 3279943_1 by 37 degrees
- `C11`: Increase A3 Offset threshold for 3279943_1 **← 정답**
- `C12`: Press down the tilt angle of 3267220_2 by 4 degrees
- `C13`: Lift the tilt angle of 3267220_2 by 4 degrees
- `C14`: Decrease A3 Offset threshold for 3279943_1
- `C15`: Lift the tilt angle  of 3279943_1 by 4 degrees
- `C16`: Increase A3 Offset threshold for 3267220_2 **← 정답**
- `C17`: Decrease transmission power for 3267220_2
- `C18`: Increase transmission power for 3279943_1
- `C19`: Adjust the azimuth of 3267220_2 by 24 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267220_2
- `C22`: Decrease A3 Offset threshold for 3267220_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.944 | MS1 | 121.4656654223 | 31.1446319241 | 966 | 504990 | -78.80 | 12.56 | 520.90 | 0.17 | 2.94 | 1565 |
| 2024-09-20 22:21:32.210 | MS1 | 121.4656651935 | 31.1446228141 | 966 | 504990 | -76.16 | 13.19 | 552.14 | 0.12 | 2.30 | 1564 |
| 2024-09-20 22:21:33.676 | MS1 | 121.4656732788 | 31.1446323063 | 966 | 504990 | -83.26 | 16.61 | 393.59 | 0.10 | 2.20 | 1567 |
| 2024-09-20 22:21:34.362 | MS1 | 121.4656753664 | 31.1446187375 | 166 | 504990 | -87.37 | 2.42 | 81.73 | 0.17 | 1.41 | 1591 |
| 2024-09-20 22:21:35.701 | MS1 | 121.4656728805 | 31.1446372044 | 166 | 504990 | -81.19 | 1.45 | 37.22 | 0.03 | 1.36 | 1566 |
| 2024-09-20 22:21:36.226 | MS1 | 121.4656760830 | 31.1446256539 | 966 | 504990 | -88.87 | 1.15 | 62.04 | 0.18 | 1.23 | 1597 |
| 2024-09-20 22:21:37.967 | MS1 | 121.4656612638 | 31.1446376291 | 966 | 504990 | -81.82 | 3.18 | 25.61 | 0.16 | 1.14 | 1583 |
| 2024-09-20 22:21:38.260 | MS1 | 121.4656766345 | 31.1446245719 | 166 | 504990 | -88.60 | 3.13 | 59.12 | 0.17 | 1.42 | 1590 |
| 2024-09-20 22:21:39.204 | MS1 | 121.4656667775 | 31.1446309475 | 166 | 504990 | -84.63 | 3.44 | 47.99 | 0.20 | 1.06 | 1598 |
| 2024-09-20 22:21:40.781 | MS1 | 121.4656754437 | 31.1446303987 | 166 | 504990 | -75.03 | 16.33 | 591.14 | 0.19 | 2.22 | 1590 |
| 2024-09-20 22:21:41.981 | MS1 | 121.4656639691 | 31.1446242389 | 166 | 504990 | -78.58 | 17.78 | 340.47 | 0.02 | 2.25 | 1562 |
| 2024-09-20 22:21:42.696 | MS1 | 121.4656607678 | 31.1446345195 | 166 | 504990 | -81.12 | 12.29 | 399.52 | 0.08 | 2.25 | 1582 |

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
| 3239189 | 4 | 121.4683982125 | 31.1469861244 | 217 | 10 | 2 | 16.8 | TDD | 362 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3239249 | 3 | 121.4713147472 | 31.1447758717 | 67 | 3 | 11 | 45.9 | TDD | 166 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3267220 | 2 | 121.4749365910 | 31.1449528248 | 292 | 1 | 3 | 45.7 | TDD | 966 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3272070 | 5 | 121.4644941561 | 31.1520726905 | 234 | 6 | 0 | 41.4 | TDD | 240 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3279943 | 1 | 121.4683960708 | 31.1511680711 | 237 | 1 | 10 | 35.3 | TDD | 420 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.452 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.556 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.556 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.299 | NREventA3 | measId:2;ServCellPCI:536;Se... |
| 2024-09-20 22:21:34.539 | NRHandoverAttempt | SourcePCI:536;SourceNR-ARFC... |
| 2024-09-20 22:21:34.588 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.602 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:34.717 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.717 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.299 | NREventA3 | measId:2;ServCellPCI:556;Se... |
| 2024-09-20 22:21:36.539 | NRHandoverAttempt | SourcePCI:556;SourceNR-ARFC... |
| 2024-09-20 22:21:36.573 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.588 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.714 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.714 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.299 | NREventA3 | measId:2;ServCellPCI:536;Se... |
| 2024-09-20 22:21:38.539 | NRHandoverAttempt | SourcePCI:536;SourceNR-ARFC... |
| 2024-09-20 22:21:38.583 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.594 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.731 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.731 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279943 | 1 | 16.3972 | 6.1545 | -117.7622 | 6.6330 | 121.2933 | 0.0043 | 0.0002 |
| 2024_09_20 22:00 | 3267220 | 2 | 13.2599 | 11.8413 | -116.7481 | 14.0018 | 98.3430 | 0.0132 | 0.0049 |
| 2024_09_20 22:00 | 3239249 | 3 | 10.0212 | 9.7507 | -116.7627 | 7.7267 | 103.5642 | 0.0050 | 0.0080 |
| 2024_09_20 22:00 | 3239189 | 4 | 6.4362 | 9.3677 | -114.3050 | 11.5378 | 133.5889 | 0.0013 | 0.0183 |
| 2024_09_20 22:00 | 3272070 | 5 | 12.1971 | 11.9963 | -117.2390 | 18.0155 | 167.0118 | 0.0116 | 0.0055 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416414_2763D587 | 504990 | 166 | -88.5 | 504990 | 966 | -86.6 | 504990 | 420 | -90.0 | 504990 | 362 |
| MR_1774416414_F97651A9 | 504990 | 166 | -88.4 | 504990 | 966 | -86.6 | 504990 | 420 | -90.5 | 504990 | 362 |
| MR_1774416414_50EBF103 | 504990 | 966 | -86.9 | 504990 | 166 | -86.6 | 504990 | 420 | -89.1 | 504990 | 362 |
| MR_1774416414_D8E4432B | 504990 | 166 | -87.8 | 504990 | 966 | -86.4 | 504990 | 420 | -88.6 | 504990 | 362 |
| MR_1774416414_D044C984 | 504990 | 166 | -88.2 | 504990 | 966 | -86.3 | 504990 | 420 | -91.1 | 504990 | 362 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1: `0cd874c0-eab...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0cd874c0-eab3-4963-a51f-28fc5e004ed8` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1] topology](images/train_0001.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3213751_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244912_3
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Adjust the azimuth of 3244912_3 by 50 degrees
- `C5`: Increase transmission power for 3244912_3
- `C6`: Adjust the azimuth of 3213751_2 by 50 degrees
- `C7`: Decrease transmission power for 3244912_3
- `C8`: Increase A3 Offset threshold for 3213751_2
- `C9`: Check test server and transmission issues **← 정답**
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213751_2
- `C11`: Decrease transmission power for 3213751_2
- `C12`: Press down the tilt angle of 3213751_2 by 1 degrees
- `C13`: Add neighbor relationship between 3213751_2 and 3244912_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244912_3
- `C15`: Lift the tilt angle of 3213751_2 by 1 degrees
- `C16`: Lift the tilt angle  of 3244912_3 by 7 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213751_2
- `C18`: Press down the tilt angle  of 3244912_3 by 7 degrees
- `C19`: Decrease A3 Offset threshold for 3244912_3
- `C20`: Increase A3 Offset threshold for 3244912_3
- `C21`: Decrease A3 Offset threshold for 3213751_2
- `C22`: Add neighbor relationship between 3211532_1 and 3244912_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.357 | MS1 | 121.4656607904 | 31.1446204376 | 546 | 504990 | -85.81 | 14.64 | 466.35 | 0.12 | 2.46 | 1567 |
| 2024-09-20 22:21:32.734 | MS1 | 121.4656674721 | 31.1446301267 | 546 | 504990 | -87.43 | 16.43 | 569.87 | 0.15 | 2.88 | 1573 |
| 2024-09-20 22:21:33.635 | MS1 | 121.4656756479 | 31.1446231376 | 546 | 504990 | -87.59 | 14.32 | 410.34 | 0.14 | 2.53 | 1587 |
| 2024-09-20 22:21:34.219 | MS1 | 121.4656596293 | 31.1446340899 | 546 | 504990 | -85.83 | 17.78 | 70.51 | 0.10 | 2.56 | 417 |
| 2024-09-20 22:21:35.683 | MS1 | 121.4656659624 | 31.1446259788 | 546 | 504990 | -90.33 | 15.15 | 51.10 | 0.08 | 2.35 | 365 |
| 2024-09-20 22:21:36.489 | MS1 | 121.4656613939 | 31.1446364286 | 546 | 504990 | -86.06 | 17.56 | 89.24 | 0.18 | 2.24 | 427 |
| 2024-09-20 22:21:37.633 | MS1 | 121.4656618930 | 31.1446324587 | 546 | 504990 | -93.11 | 7.92 | 65.27 | 0.17 | 2.09 | 343 |
| 2024-09-20 22:21:38.455 | MS1 | 121.4656643690 | 31.1446284485 | 546 | 504990 | -89.65 | 12.17 | 79.39 | 0.11 | 2.05 | 478 |
| 2024-09-20 22:21:39.806 | MS1 | 121.4656609795 | 31.1446257510 | 546 | 504990 | -91.70 | 8.88 | 53.91 | 0.07 | 2.86 | 366 |
| 2024-09-20 22:21:40.115 | MS1 | 121.4656686445 | 31.1446287832 | 546 | 504990 | -92.08 | 12.18 | 426.80 | 0.11 | 2.29 | 1574 |
| 2024-09-20 22:21:41.921 | MS1 | 121.4656702359 | 31.1446298152 | 546 | 504990 | -90.90 | 11.35 | 431.26 | 0.14 | 2.39 | 1581 |
| 2024-09-20 22:21:42.637 | MS1 | 121.4656707182 | 31.1446264489 | 546 | 504990 | -93.52 | 11.87 | 471.50 | 0.05 | 2.26 | 1589 |

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
| 3211532 | 1 | 121.4720425044 | 31.1535240093 | 123 | 3 | 4 | 22.7 | TDD | 344 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3213751 | 2 | 121.4736068325 | 31.1460110535 | 131 | 0 | 4 | 15.8 | TDD | 546 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3244912 | 3 | 121.4752629661 | 31.1505829287 | 184 | 5 | 7 | 33.7 | TDD | 494 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3274217 | 4 | 121.4642090633 | 31.1516892721 | 217 | 11 | 0 | 44.3 | TDD | 583 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.166 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.182 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.292 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.292 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.990 | NREventA3 | measId:2;ServCellPCI:995;Se... |
| 2024-09-20 22:21:38.230 | NRHandoverAttempt | SourcePCI:995;SourceNR-ARFC... |
| 2024-09-20 22:21:38.273 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.288 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.394 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.394 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211532 | 1 | 13.2170 | 16.4515 | -114.7737 | 7.2875 | 190.0613 | 0.0194 | 0.0096 |
| 2024_09_20 22:00 | 3213751 | 2 | 6.5308 | 5.9009 | -116.3808 | 14.4610 | 101.0707 | 0.0188 | 0.0173 |
| 2024_09_20 22:00 | 3244912 | 3 | 19.1996 | 12.0061 | -117.2225 | 19.0515 | 194.7099 | 0.0151 | 0.0077 |
| 2024_09_20 22:00 | 3274217 | 4 | 11.8198 | 10.2861 | -117.9438 | 13.7565 | 105.2796 | 0.0185 | 0.0036 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412622_61B1F29B | 504990 | 546 | -85.8 | 504990 | 494 | -93.8 | 504990 | 344 | -98.0 | 504990 | 583 |
| MR_1774412622_19C5683F | 504990 | 546 | -87.3 | 504990 | 494 | -93.5 | 504990 | 344 | -96.2 | 504990 | 583 |
| MR_1774412622_A3AABB7B | 504990 | 546 | -85.1 | 504990 | 494 | -94.1 | 504990 | 344 | -98.7 | 504990 | 583 |
| MR_1774412622_422B044E | 504990 | 546 | -84.0 | 504990 | 494 | -93.4 | 504990 | 344 | -97.2 | 504990 | 583 |
| MR_1774412622_88957C74 | 504990 | 546 | -87.6 | 504990 | 494 | -93.6 | 504990 | 344 | -97.1 | 504990 | 583 |
| MR_1774412622_0E56E069 | 504990 | 546 | -85.5 | 504990 | 494 | -94.1 | 504990 | 344 | -95.9 | 504990 | 583 |
| MR_1774412622_B35E16BC | 504990 | 546 | -87.7 | 504990 | 494 | -92.9 | 504990 | 344 | -97.5 | 504990 | 583 |
| MR_1774412622_842877AA | 504990 | 546 | -85.4 | 504990 | 494 | -91.8 | 504990 | 344 | -96.3 | 504990 | 583 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 2: `ac53a506-f1d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ac53a506-f1dd-404f-bb93-1ffb337ce0e6` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease A3 Offset threshold for 3213863_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[2] topology](images/train_0002.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3213863_2
- `C2`: Press down the tilt angle of 3213863_2 by 10 degrees
- `C3`: Check test server and transmission issues
- `C4`: Increase A3 Offset threshold for 3211229_4
- `C5`: Add neighbor relationship between 3213863_2 and 3211229_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211229_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211229_4
- `C8`: Decrease transmission power for 3213863_2
- `C9`: Adjust the azimuth of 3211229_4 by 50 degrees
- `C10`: Add neighbor relationship between 3254533_1 and 3211229_4
- `C11`: Lift the tilt angle  of 3211229_4 by 10 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease A3 Offset threshold for 3211229_4
- `C14`: Press down the tilt angle  of 3211229_4 by 10 degrees
- `C15`: Decrease transmission power for 3211229_4
- `C16`: Decrease A3 Offset threshold for 3213863_2 **← 정답**
- `C17`: Increase A3 Offset threshold for 3213863_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213863_2
- `C19`: Increase transmission power for 3211229_4
- `C20`: Lift the tilt angle of 3213863_2 by 10 degrees
- `C21`: Adjust the azimuth of 3213863_2 by 50 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213863_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.523 | MS1 | 121.4656681262 | 31.1446250354 | 156 | 504990 | -75.63 | 13.12 | 549.92 | 0.05 | 2.97 | 1570 |
| 2024-09-20 22:21:32.397 | MS1 | 121.4656624648 | 31.1446283872 | 156 | 504990 | -77.03 | 13.19 | 354.51 | 0.13 | 2.56 | 1567 |
| 2024-09-20 22:21:33.333 | MS1 | 121.4656774681 | 31.1446194879 | 156 | 504990 | -83.51 | 16.03 | 405.21 | 0.11 | 2.56 | 1569 |
| 2024-09-20 22:21:34.197 | MS1 | 121.4656715130 | 31.1446378787 | 156 | 504990 | -84.73 | -2.82 | 75.01 | 0.01 | 1.41 | 1575 |
| 2024-09-20 22:21:35.155 | MS1 | 121.4656598477 | 31.1446181564 | 156 | 504990 | -88.54 | -1.05 | 26.45 | 0.18 | 1.18 | 1581 |
| 2024-09-20 22:21:36.377 | MS1 | 121.4656673147 | 31.1446299190 | 156 | 504990 | -87.93 | -1.05 | 51.69 | 0.15 | 1.18 | 1580 |
| 2024-09-20 22:21:37.734 | MS1 | 121.4656644486 | 31.1446316664 | 156 | 504990 | -87.39 | -1.61 | 25.17 | 0.08 | 1.47 | 1594 |
| 2024-09-20 22:21:38.508 | MS1 | 121.4656702695 | 31.1446275105 | 156 | 504990 | -88.10 | -1.85 | 45.08 | 0.07 | 1.13 | 1568 |
| 2024-09-20 22:21:39.455 | MS1 | 121.4656698503 | 31.1446240856 | 236 | 504990 | -83.99 | 17.33 | 185.60 | 0.17 | 1.34 | 1585 |
| 2024-09-20 22:21:40.675 | MS1 | 121.4656724481 | 31.1446277950 | 236 | 504990 | -75.05 | 14.41 | 488.22 | 0.11 | 2.99 | 1567 |
| 2024-09-20 22:21:41.159 | MS1 | 121.4656691361 | 31.1446326152 | 236 | 504990 | -84.49 | 16.19 | 480.02 | 0.14 | 2.84 | 1562 |
| 2024-09-20 22:21:42.335 | MS1 | 121.4656694698 | 31.1446282089 | 236 | 504990 | -80.59 | 17.87 | 314.56 | 0.08 | 2.81 | 1587 |

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
| 3211229 | 4 | 121.4657129346 | 31.1547560133 | 98 | 13 | 3 | 49.4 | TDD | 236 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3213863 | 2 | 121.4665584695 | 31.1449241774 | 33 | 6 | 3 | 39.1 | TDD | 156 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3254533 | 1 | 121.4741034203 | 31.1532964447 | 138 | 8 | 1 | 31.1 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3278143 | 3 | 121.4670098052 | 31.1526268035 | 96 | 13 | 2 | 32.9 | TDD | 352 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.185 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.200 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.344 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.344 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.065 | NREventA3 | measId:2;ServCellPCI:847;Se... |
| 2024-09-20 22:21:38.305 | NRHandoverAttempt | SourcePCI:847;SourceNR-ARFC... |
| 2024-09-20 22:21:38.348 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.362 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.469 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.469 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254533 | 1 | 17.3244 | 7.7626 | -116.6513 | 11.5149 | 161.2718 | 0.0008 | 0.0120 |
| 2024_09_20 22:00 | 3213863 | 2 | 14.9181 | 19.4642 | -116.5173 | 16.6615 | 81.8725 | 0.0130 | 0.1707 |
| 2024_09_20 22:00 | 3278143 | 3 | 8.1420 | 11.5032 | -116.5785 | 5.1629 | 158.9610 | 0.0106 | 0.0101 |
| 2024_09_20 22:00 | 3211229 | 4 | 16.5397 | 13.9408 | -115.9763 | 8.2821 | 127.6811 | 0.0150 | 0.0157 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413529_0E2794AF | 504990 | 236 | -78.3 | 504990 | 156 | -82.9 | 504990 | 176 | -84.5 | 504990 | 352 |
| MR_1774413529_2574F88D | 504990 | 156 | -84.1 | 504990 | 236 | -80.8 | 504990 | 176 | -86.2 | 504990 | 352 |
| MR_1774413529_C2A70A13 | 504990 | 156 | -85.8 | 504990 | 236 | -78.9 | 504990 | 176 | -85.5 | 504990 | 352 |
| MR_1774413529_D249F2C2 | 504990 | 156 | -85.1 | 504990 | 236 | -77.6 | 504990 | 176 | -85.4 | 504990 | 352 |
| MR_1774413529_674EBACA | 504990 | 236 | -79.8 | 504990 | 156 | -85.5 | 504990 | 176 | -84.1 | 504990 | 352 |
| MR_1774413529_EDA94563 | 504990 | 236 | -80.8 | 504990 | 156 | -85.3 | 504990 | 176 | -87.2 | 504990 | 352 |
| MR_1774413529_D92E36EB | 504990 | 236 | -78.4 | 504990 | 156 | -83.4 | 504990 | 176 | -86.4 | 504990 | 352 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 3: `39bb305f-5d4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `39bb305f-5d41-4b58-8e88-c69023dc7ebc` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[3] topology](images/train_0003.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease A3 Offset threshold for 3244278_4
- `C3`: Increase A3 Offset threshold for 3238149_1
- `C4`: Increase A3 Offset threshold for 3244278_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244278_4
- `C6`: Lift the tilt angle  of 3238149_1 by 7 degrees
- `C7`: Add neighbor relationship between 3213061_3 and 3238149_1
- `C8`: Adjust the azimuth of 3244278_4 by 40 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238149_1
- `C10`: Check test server and transmission issues **← 정답**
- `C11`: Decrease transmission power for 3238149_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238149_1
- `C13`: Increase transmission power for 3244278_4
- `C14`: Add neighbor relationship between 3244278_4 and 3238149_1
- `C15`: Press down the tilt angle  of 3238149_1 by 7 degrees
- `C16`: Press down the tilt angle of 3244278_4 by 10 degrees
- `C17`: Adjust the azimuth of 3238149_1 by 50 degrees
- `C18`: Decrease transmission power for 3244278_4
- `C19`: Increase transmission power for 3238149_1
- `C20`: Decrease A3 Offset threshold for 3238149_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244278_4
- `C22`: Lift the tilt angle of 3244278_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.495 | MS1 | 121.4656718987 | 31.1446351278 | 588 | 504990 | -86.40 | 14.51 | 310.10 | 0.13 | 3.00 | 1570 |
| 2024-09-20 22:21:32.415 | MS1 | 121.4656719261 | 31.1446246103 | 588 | 504990 | -87.79 | 14.31 | 340.22 | 0.07 | 2.14 | 1561 |
| 2024-09-20 22:21:33.938 | MS1 | 121.4656750105 | 31.1446282571 | 588 | 504990 | -86.11 | 13.31 | 462.63 | 0.02 | 2.42 | 1598 |
| 2024-09-20 22:21:34.792 | MS1 | 121.4656623849 | 31.1446283336 | 588 | 504990 | -87.09 | 17.91 | 98.39 | 0.12 | 2.88 | 306 |
| 2024-09-20 22:21:35.599 | MS1 | 121.4656689873 | 31.1446206012 | 588 | 504990 | -89.95 | 12.96 | 60.37 | 0.19 | 2.40 | 394 |
| 2024-09-20 22:21:36.497 | MS1 | 121.4656715022 | 31.1446374119 | 588 | 504990 | -88.89 | 14.75 | 64.86 | 0.13 | 2.01 | 489 |
| 2024-09-20 22:21:37.793 | MS1 | 121.4656623520 | 31.1446221855 | 588 | 504990 | -89.33 | 9.75 | 87.00 | 0.02 | 2.53 | 421 |
| 2024-09-20 22:21:38.476 | MS1 | 121.4656610292 | 31.1446278180 | 588 | 504990 | -92.60 | 7.40 | 60.28 | 0.01 | 2.88 | 301 |
| 2024-09-20 22:21:39.930 | MS1 | 121.4656646694 | 31.1446273604 | 588 | 504990 | -91.96 | 10.32 | 90.32 | 0.14 | 3.00 | 458 |
| 2024-09-20 22:21:40.641 | MS1 | 121.4656731727 | 31.1446293266 | 588 | 504990 | -93.50 | 11.33 | 357.30 | 0.10 | 2.85 | 1564 |
| 2024-09-20 22:21:41.682 | MS1 | 121.4656648137 | 31.1446346458 | 588 | 504990 | -91.77 | 11.27 | 301.10 | 0.12 | 2.59 | 1599 |
| 2024-09-20 22:21:42.552 | MS1 | 121.4656752206 | 31.1446350706 | 588 | 504990 | -93.49 | 7.69 | 501.94 | 0.02 | 2.51 | 1560 |

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
| 3213061 | 3 | 121.4680718688 | 31.1498892872 | 152 | 3 | 11 | 41.6 | TDD | 686 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3226772 | 2 | 121.4746417795 | 31.1550351672 | 193 | 7 | 9 | 47.2 | TDD | 220 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3238149 | 1 | 121.4676886788 | 31.1490564775 | 347 | 4 | 12 | 28.5 | TDD | 513 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3244278 | 4 | 121.4750467151 | 31.1509168782 | 272 | 10 | 6 | 25.7 | TDD | 588 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.747 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.765 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.912 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.912 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.604 | NREventA3 | measId:2;ServCellPCI:298;Se... |
| 2024-09-20 22:21:37.844 | NRHandoverAttempt | SourcePCI:298;SourceNR-ARFC... |
| 2024-09-20 22:21:37.887 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.900 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.001 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.001 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238149 | 1 | 13.0482 | 18.6172 | -114.4797 | 12.0953 | 140.5196 | 0.0148 | 0.0150 |
| 2024_09_20 22:00 | 3226772 | 2 | 5.4235 | 19.6890 | -117.5074 | 11.8507 | 175.9593 | 0.0135 | 0.0099 |
| 2024_09_20 22:00 | 3213061 | 3 | 17.9769 | 15.0794 | -114.7163 | 19.0700 | 190.6320 | 0.0101 | 0.0069 |
| 2024_09_20 22:00 | 3244278 | 4 | 7.3594 | 13.6964 | -114.9945 | 15.5841 | 141.0874 | 0.0142 | 0.0150 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415152_F6C4E5BC | 504990 | 588 | -87.9 | 504990 | 513 | -93.6 | 504990 | 686 | -103.7 | 504990 | 220 |
| MR_1774415152_15D5F6FA | 504990 | 588 | -85.3 | 504990 | 513 | -90.4 | 504990 | 686 | -102.6 | 504990 | 220 |
| MR_1774415152_4AF29412 | 504990 | 588 | -87.8 | 504990 | 513 | -91.3 | 504990 | 686 | -101.1 | 504990 | 220 |
| MR_1774415152_526DF707 | 504990 | 588 | -86.4 | 504990 | 513 | -90.8 | 504990 | 686 | -101.0 | 504990 | 220 |
| MR_1774415152_1543EAF3 | 504990 | 588 | -88.6 | 504990 | 513 | -91.1 | 504990 | 686 | -102.5 | 504990 | 220 |
| MR_1774415152_321C6ACE | 504990 | 588 | -87.0 | 504990 | 513 | -91.4 | 504990 | 686 | -102.5 | 504990 | 220 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 4: `0ec53773-5b5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0ec53773-5b55-4777-b506-aab4bd9d53fc` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Lift the tilt angle  of 3255225_2 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[4] topology](images/train_0004.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3230652_1 and 3240495_4
- `C2`: Lift the tilt angle of 3230652_1 by 4 degrees
- `C3`: Lift the tilt angle  of 3255225_2 by 7 degrees **← 정답**
- `C4`: Press down the tilt angle of 3230652_1 by 4 degrees
- `C5`: Decrease transmission power for 3230652_1
- `C6`: Increase transmission power for 3230652_1
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Adjust the azimuth of 3255225_2 by 50 degrees
- `C9`: Decrease transmission power for 3240495_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230652_1
- `C11`: Press down the tilt angle  of 3255225_2 by 7 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230652_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240495_4
- `C14`: Increase transmission power for 3240495_4
- `C15`: Decrease A3 Offset threshold for 3240495_4
- `C16`: Check test server and transmission issues
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240495_4
- `C18`: Increase A3 Offset threshold for 3240495_4
- `C19`: Increase A3 Offset threshold for 3230652_1
- `C20`: Adjust the azimuth of 3230652_1 by 37 degrees
- `C21`: Decrease A3 Offset threshold for 3230652_1
- `C22`: Add neighbor relationship between 3255225_2 and 3240495_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.688 | MS1 | 121.4656663794 | 31.1446282212 | 840 | 504990 | -87.97 | 17.14 | 567.43 | 0.18 | 2.85 | 1561 |
| 2024-09-20 22:21:32.120 | MS1 | 121.4656756499 | 31.1446205493 | 840 | 504990 | -87.53 | 15.99 | 494.36 | 0.06 | 2.35 | 1564 |
| 2024-09-20 22:21:33.882 | MS1 | 121.4656600018 | 31.1446295006 | 840 | 504990 | -90.57 | 14.75 | 327.99 | 0.01 | 2.76 | 1584 |
| 2024-09-20 22:21:34.110 | MS1 | 121.4656665109 | 31.1446334711 | 840 | 504990 | -90.37 | 17.93 | 71.25 | 0.08 | 2.64 | 1564 |
| 2024-09-20 22:21:35.289 | MS1 | 121.4656692073 | 31.1446234069 | 840 | 504990 | -86.71 | 13.71 | 68.04 | 0.18 | 2.11 | 1583 |
| 2024-09-20 22:21:36.907 | MS1 | 121.4656598380 | 31.1446229473 | 840 | 504990 | -89.36 | 15.99 | 94.86 | 0.01 | 2.65 | 1599 |
| 2024-09-20 22:21:37.876 | MS1 | 121.4656654366 | 31.1446292181 | 840 | 504990 | -92.89 | 7.32 | 89.72 | 0.02 | 2.30 | 1575 |
| 2024-09-20 22:21:38.395 | MS1 | 121.4656737751 | 31.1446279957 | 840 | 504990 | -91.14 | 10.58 | 68.74 | 0.08 | 2.52 | 1580 |
| 2024-09-20 22:21:39.460 | MS1 | 121.4656740057 | 31.1446288987 | 840 | 504990 | -90.20 | 11.55 | 92.50 | 0.01 | 2.28 | 1589 |
| 2024-09-20 22:21:40.304 | MS1 | 121.4656732608 | 31.1446287446 | 840 | 504990 | -89.58 | 9.13 | 302.79 | 0.01 | 2.12 | 1582 |
| 2024-09-20 22:21:41.518 | MS1 | 121.4656681425 | 31.1446241527 | 840 | 504990 | -91.91 | 7.07 | 587.92 | 0.15 | 2.15 | 1574 |
| 2024-09-20 22:21:42.616 | MS1 | 121.4656589058 | 31.1446370623 | 840 | 504990 | -90.94 | 11.68 | 600.65 | 0.00 | 2.28 | 1561 |

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
| 3230652 | 1 | 121.4699842769 | 31.1485260462 | 186 | 1 | 9 | 28.5 | TDD | 840 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3240495 | 4 | 121.4663196090 | 31.1547778502 | 254 | 6 | 2 | 23.7 | TDD | 127 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3255225 | 2 | 121.4694757663 | 31.1473575778 | 348 | 15 | 9 | 40.1 | TDD | 488 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3277550 | 3 | 121.4697435464 | 31.1527102818 | 304 | 6 | 7 | 27.2 | TDD | 549 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.325 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.340 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.457 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.457 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.129 | NREventA3 | measId:2;ServCellPCI:757;Se... |
| 2024-09-20 22:21:38.369 | NRHandoverAttempt | SourcePCI:757;SourceNR-ARFC... |
| 2024-09-20 22:21:38.400 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.412 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.561 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.561 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230652 | 1 | 87.6347 | 82.2997 | -114.9380 | 11.3647 | 194.9547 | 0.0190 | 0.0087 |
| 2024_09_20 22:00 | 3255225 | 2 | 16.4043 | 6.5568 | -116.2085 | 16.5713 | 122.2897 | 0.0044 | 0.0093 |
| 2024_09_20 22:00 | 3277550 | 3 | 16.4398 | 8.0284 | -114.5146 | 16.0122 | 82.5645 | 0.0172 | 0.0019 |
| 2024_09_20 22:00 | 3240495 | 4 | 7.9067 | 12.9461 | -114.1516 | 12.2125 | 177.4092 | 0.0198 | 0.0025 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412433_F3507A49 | 504990 | 840 | -88.9 | 504990 | 127 | -97.4 | 504990 | 488 | -103.9 | 504990 | 549 |
| MR_1774412433_40D7A455 | 504990 | 840 | -88.6 | 504990 | 127 | -96.8 | 504990 | 488 | -102.9 | 504990 | 549 |
| MR_1774412433_8FE1C113 | 504990 | 840 | -91.4 | 504990 | 127 | -96.8 | 504990 | 488 | -104.9 | 504990 | 549 |
| MR_1774412433_8DB673A5 | 504990 | 840 | -90.0 | 504990 | 127 | -94.3 | 504990 | 488 | -105.8 | 504990 | 549 |
| MR_1774412433_1EE02CDC | 504990 | 840 | -88.6 | 504990 | 127 | -96.0 | 504990 | 488 | -104.2 | 504990 | 549 |
| MR_1774412433_43786375 | 504990 | 840 | -90.3 | 504990 | 127 | -96.6 | 504990 | 488 | -102.7 | 504990 | 549 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 5: `01511464-4a9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `01511464-4a9e-4bfd-a019-b56847d3d394` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease A3 Offset threshold for 3257709_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[5] topology](images/train_0005.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3257709_1
- `C2`: Decrease transmission power for 3262328_2
- `C3`: Increase A3 Offset threshold for 3262328_2
- `C4`: Decrease A3 Offset threshold for 3262328_2
- `C5`: Increase transmission power for 3257709_1
- `C6`: Adjust the azimuth of 3262328_2 by 50 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease A3 Offset threshold for 3257709_1 **← 정답**
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257709_1
- `C10`: Lift the tilt angle  of 3262328_2 by 10 degrees
- `C11`: Increase transmission power for 3262328_2
- `C12`: Add neighbor relationship between 3257709_1 and 3262328_2
- `C13`: Press down the tilt angle of 3257709_1 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262328_2
- `C15`: Adjust the azimuth of 3257709_1 by 50 degrees
- `C16`: Check test server and transmission issues
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257709_1
- `C18`: Increase A3 Offset threshold for 3257709_1
- `C19`: Lift the tilt angle of 3257709_1 by 10 degrees
- `C20`: Add neighbor relationship between 3274253_3 and 3262328_2
- `C21`: Press down the tilt angle  of 3262328_2 by 10 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262328_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.876 | MS1 | 121.4656606563 | 31.1446208340 | 385 | 504990 | -75.04 | 15.66 | 455.36 | 0.01 | 2.73 | 1591 |
| 2024-09-20 22:21:32.693 | MS1 | 121.4656697580 | 31.1446328270 | 385 | 504990 | -75.86 | 16.29 | 516.32 | 0.20 | 2.21 | 1576 |
| 2024-09-20 22:21:33.618 | MS1 | 121.4656736702 | 31.1446263461 | 385 | 504990 | -77.78 | 17.83 | 603.69 | 0.19 | 2.48 | 1584 |
| 2024-09-20 22:21:34.866 | MS1 | 121.4656690088 | 31.1446356915 | 385 | 504990 | -87.21 | -2.70 | 57.29 | 0.18 | 1.15 | 1560 |
| 2024-09-20 22:21:35.149 | MS1 | 121.4656645991 | 31.1446340402 | 385 | 504990 | -90.35 | -2.21 | 55.28 | 0.11 | 1.41 | 1600 |
| 2024-09-20 22:21:36.338 | MS1 | 121.4656679023 | 31.1446226369 | 385 | 504990 | -92.72 | -3.95 | 67.40 | 0.02 | 1.49 | 1588 |
| 2024-09-20 22:21:37.491 | MS1 | 121.4656728116 | 31.1446274713 | 385 | 504990 | -88.85 | -3.48 | 78.66 | 0.10 | 1.30 | 1582 |
| 2024-09-20 22:21:38.249 | MS1 | 121.4656734189 | 31.1446355729 | 385 | 504990 | -87.53 | -3.33 | 42.77 | 0.14 | 1.18 | 1585 |
| 2024-09-20 22:21:39.828 | MS1 | 121.4656663282 | 31.1446284838 | 821 | 504990 | -77.81 | 14.04 | 228.98 | 0.00 | 1.16 | 1568 |
| 2024-09-20 22:21:40.973 | MS1 | 121.4656649204 | 31.1446305618 | 821 | 504990 | -84.07 | 15.10 | 598.48 | 0.19 | 2.02 | 1597 |
| 2024-09-20 22:21:41.234 | MS1 | 121.4656723915 | 31.1446232094 | 821 | 504990 | -75.77 | 17.82 | 537.90 | 0.14 | 2.32 | 1569 |
| 2024-09-20 22:21:42.405 | MS1 | 121.4656581322 | 31.1446235611 | 821 | 504990 | -79.99 | 16.77 | 345.44 | 0.14 | 3.00 | 1582 |

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
| 3234922 | 4 | 121.4696682245 | 31.1484303404 | 64 | 4 | 6 | 29.6 | TDD | 470 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3257709 | 1 | 121.4689228291 | 31.1459625341 | 141 | 13 | 8 | 15.2 | TDD | 385 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3262328 | 2 | 121.4759341241 | 31.1513274560 | 73 | 14 | 8 | 22.6 | TDD | 821 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3274253 | 3 | 121.4751723566 | 31.1453866298 | 2 | 3 | 0 | 22.9 | TDD | 477 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.252 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.267 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.383 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.383 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.053 | NREventA3 | measId:2;ServCellPCI:207;Se... |
| 2024-09-20 22:21:38.293 | NRHandoverAttempt | SourcePCI:207;SourceNR-ARFC... |
| 2024-09-20 22:21:38.340 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.354 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.459 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.459 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257709 | 1 | 13.9504 | 17.8508 | -115.9285 | 11.3263 | 151.8610 | 0.0169 | 0.1333 |
| 2024_09_20 22:00 | 3262328 | 2 | 5.0532 | 5.4136 | -117.5034 | 9.3116 | 194.0501 | 0.0182 | 0.0091 |
| 2024_09_20 22:00 | 3274253 | 3 | 18.9103 | 19.1383 | -116.3234 | 17.9812 | 187.4474 | 0.0132 | 0.0034 |
| 2024_09_20 22:00 | 3234922 | 4 | 5.9434 | 8.9845 | -117.9971 | 6.3162 | 195.9724 | 0.0041 | 0.0131 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414465_7612DF57 | 504990 | 385 | -86.1 | 504990 | 821 | -80.7 | 504990 | 477 | -82.9 | 504990 | 470 |
| MR_1774414465_39D60AC3 | 504990 | 821 | -83.6 | 504990 | 385 | -88.5 | 504990 | 477 | -86.7 | 504990 | 470 |
| MR_1774414465_D5454389 | 504990 | 821 | -83.0 | 504990 | 385 | -88.9 | 504990 | 477 | -85.0 | 504990 | 470 |
| MR_1774414465_C9E4AE65 | 504990 | 821 | -81.0 | 504990 | 385 | -87.4 | 504990 | 477 | -84.0 | 504990 | 470 |
| MR_1774414465_776A213A | 504990 | 385 | -87.8 | 504990 | 821 | -83.1 | 504990 | 477 | -86.0 | 504990 | 470 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 6: `af48c90d-a33...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `af48c90d-a335-4864-aef9-792bd80169ff` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[6] topology](images/train_0006.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3240491_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240491_1
- `C3`: Add neighbor relationship between 3276319_3 and 3279919_2
- `C4`: Adjust the azimuth of 3240491_1 by 20 degrees
- `C5`: Increase transmission power for 3279919_2
- `C6`: Increase A3 Offset threshold for 3240491_1
- `C7`: Press down the tilt angle  of 3279919_2 by 10 degrees
- `C8`: Increase A3 Offset threshold for 3279919_2
- `C9`: Insufficient data; more data is needed for judgment. **← 정답**
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279919_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279919_2
- `C12`: Add neighbor relationship between 3240491_1 and 3279919_2
- `C13`: Decrease A3 Offset threshold for 3279919_2
- `C14`: Lift the tilt angle  of 3279919_2 by 10 degrees
- `C15`: Increase transmission power for 3240491_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240491_1
- `C17`: Decrease transmission power for 3279919_2
- `C18`: Adjust the azimuth of 3279919_2 by 46 degrees
- `C19`: Check test server and transmission issues
- `C20`: Decrease A3 Offset threshold for 3240491_1
- `C21`: Lift the tilt angle of 3240491_1 by 9 degrees
- `C22`: Press down the tilt angle of 3240491_1 by 9 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.150 | MS1 | 121.4656760352 | 31.1446201703 | 809 | 504990 | -86.39 | 15.48 | 511.51 | 0.15 | 2.07 | 1560 |
| 2024-09-20 22:21:32.647 | MS1 | 121.4656721080 | 31.1446323168 | 809 | 504990 | -91.60 | 15.48 | 335.22 | 0.02 | 2.69 | 1566 |
| 2024-09-20 22:21:33.267 | MS1 | 121.4656771107 | 31.1446353517 | 809 | 504990 | -90.55 | 16.50 | 379.44 | 0.19 | 2.98 | 1582 |
| 2024-09-20 22:21:34.258 | MS1 | 121.4656686700 | 31.1446363377 | 809 | 504990 | -88.18 | 16.96 | 74.85 | 0.12 | 2.03 | 1593 |
| 2024-09-20 22:21:35.455 | MS1 | 121.4656658375 | 31.1446180470 | 809 | 504990 | -86.96 | 13.69 | 74.35 | 0.10 | 2.73 | 1564 |
| 2024-09-20 22:21:36.946 | MS1 | 121.4656733759 | 31.1446315339 | 809 | 504990 | -86.64 | 15.26 | 79.55 | 0.04 | 2.57 | 1577 |
| 2024-09-20 22:21:37.654 | MS1 | 121.4656720049 | 31.1446290045 | 809 | 504990 | -93.99 | 10.05 | 56.02 | 0.04 | 2.64 | 1582 |
| 2024-09-20 22:21:38.936 | MS1 | 121.4656630237 | 31.1446262766 | 809 | 504990 | -91.96 | 10.30 | 88.44 | 0.18 | 2.48 | 1593 |
| 2024-09-20 22:21:39.221 | MS1 | 121.4656778659 | 31.1446324289 | 809 | 504990 | -92.11 | 10.87 | 80.84 | 0.19 | 2.29 | 1593 |
| 2024-09-20 22:21:40.718 | MS1 | 121.4656658320 | 31.1446222611 | 809 | 504990 | -90.00 | 7.73 | 482.37 | 0.01 | 2.68 | 1567 |
| 2024-09-20 22:21:41.246 | MS1 | 121.4656581985 | 31.1446209271 | 809 | 504990 | -93.07 | 11.81 | 442.23 | 0.19 | 2.22 | 1567 |
| 2024-09-20 22:21:42.692 | MS1 | 121.4656607912 | 31.1446365208 | 809 | 504990 | -93.94 | 10.35 | 416.41 | 0.09 | 2.32 | 1562 |

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
| 3220184 | 4 | 121.4699991614 | 31.1466022761 | 90 | 2 | 6 | 38.6 | TDD | 201 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3240491 | 1 | 121.4733087853 | 31.1519988417 | 242 | 7 | 12 | 29.0 | TDD | 809 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3276319 | 3 | 121.4663730960 | 31.1549387771 | 263 | 13 | 7 | 43.3 | TDD | 108 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3279919 | 2 | 121.4646604872 | 31.1522777852 | 220 | 13 | 1 | 46.1 | TDD | 67 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.459 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.479 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.616 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.616 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.321 | NREventA3 | measId:2;ServCellPCI:159;Se... |
| 2024-09-20 22:21:38.561 | NRHandoverAttempt | SourcePCI:159;SourceNR-ARFC... |
| 2024-09-20 22:21:38.599 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.612 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.733 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.733 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3240491 | 1 | 79.8711 | 81.4947 | -117.8081 | 9.5572 | 104.1072 | 0.0094 | 0.0120 |
| 2024_09_19 22:00 | 3279919 | 2 | 81.2130 | 91.0213 | -115.1481 | 7.7405 | 91.0928 | 0.0171 | 0.0199 |
| 2024_09_19 22:00 | 3276319 | 3 | 77.0082 | 86.7813 | -117.2898 | 8.6221 | 180.2687 | 0.0094 | 0.0151 |
| 2024_09_19 22:00 | 3220184 | 4 | 88.0918 | 75.0999 | -117.9061 | 5.1672 | 147.6747 | 0.0189 | 0.0015 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414471_140ED67B | 504990 | 809 | -89.2 | 504990 | 67 | -94.4 | 504990 | 108 | -97.1 | 504990 | 201 |
| MR_1774414471_4A0A00B7 | 504990 | 809 | -89.8 | 504990 | 67 | -93.3 | 504990 | 108 | -96.1 | 504990 | 201 |
| MR_1774414471_EE4FC0A1 | 504990 | 809 | -86.6 | 504990 | 67 | -96.1 | 504990 | 108 | -98.2 | 504990 | 201 |
| MR_1774414471_1F684AB0 | 504990 | 809 | -86.7 | 504990 | 67 | -93.1 | 504990 | 108 | -97.3 | 504990 | 201 |
| MR_1774414471_6244269D | 504990 | 809 | -87.2 | 504990 | 67 | -93.1 | 504990 | 108 | -96.0 | 504990 | 201 |
| MR_1774414471_4D94C0BF | 504990 | 809 | -86.8 | 504990 | 67 | -93.8 | 504990 | 108 | -94.5 | 504990 | 201 |
| MR_1774414471_2057ACCD | 504990 | 809 | -89.2 | 504990 | 67 | -94.7 | 504990 | 108 | -96.0 | 504990 | 201 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 7: `a60de966-400...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a60de966-4009-4609-b1e3-4c40e6a61366` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[7] topology](images/train_0007.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3251703_1
- `C2`: Press down the tilt angle  of 3213695_4 by 10 degrees
- `C3`: Press down the tilt angle of 3251703_1 by 10 degrees
- `C4`: Add neighbor relationship between 3251703_1 and 3213695_4
- `C5`: Increase A3 Offset threshold for 3251703_1
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Lift the tilt angle  of 3213695_4 by 10 degrees
- `C8`: Lift the tilt angle of 3251703_1 by 10 degrees
- `C9`: Increase A3 Offset threshold for 3213695_4
- `C10`: Check test server and transmission issues **← 정답**
- `C11`: Adjust the azimuth of 3251703_1 by 15 degrees
- `C12`: Increase transmission power for 3251703_1
- `C13`: Add neighbor relationship between 3261305_2 and 3213695_4
- `C14`: Increase transmission power for 3213695_4
- `C15`: Decrease A3 Offset threshold for 3213695_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213695_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251703_1
- `C18`: Adjust the azimuth of 3213695_4 by 50 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213695_4
- `C20`: Decrease transmission power for 3251703_1
- `C21`: Decrease transmission power for 3213695_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251703_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.449 | MS1 | 121.4656633114 | 31.1446190641 | 736 | 504990 | -89.15 | 13.54 | 319.11 | 0.18 | 2.31 | 1596 |
| 2024-09-20 22:21:32.457 | MS1 | 121.4656747672 | 31.1446325094 | 736 | 504990 | -87.54 | 14.56 | 435.01 | 0.14 | 2.98 | 1565 |
| 2024-09-20 22:21:33.333 | MS1 | 121.4656687850 | 31.1446293325 | 736 | 504990 | -91.52 | 12.51 | 551.84 | 0.18 | 2.97 | 1593 |
| 2024-09-20 22:21:34.447 | MS1 | 121.4656655152 | 31.1446247999 | 736 | 504990 | -86.43 | 15.52 | 80.92 | 0.02 | 2.01 | 406 |
| 2024-09-20 22:21:35.181 | MS1 | 121.4656617723 | 31.1446186842 | 736 | 504990 | -86.69 | 13.52 | 84.37 | 0.04 | 2.86 | 353 |
| 2024-09-20 22:21:36.877 | MS1 | 121.4656714360 | 31.1446211979 | 736 | 504990 | -87.54 | 16.39 | 98.91 | 0.10 | 2.39 | 371 |
| 2024-09-20 22:21:37.813 | MS1 | 121.4656757515 | 31.1446220070 | 736 | 504990 | -90.20 | 12.50 | 84.29 | 0.02 | 2.23 | 368 |
| 2024-09-20 22:21:38.869 | MS1 | 121.4656697801 | 31.1446353049 | 736 | 504990 | -91.87 | 12.21 | 84.21 | 0.06 | 2.84 | 500 |
| 2024-09-20 22:21:39.553 | MS1 | 121.4656762369 | 31.1446357550 | 736 | 504990 | -91.23 | 12.61 | 100.98 | 0.07 | 2.48 | 362 |
| 2024-09-20 22:21:40.896 | MS1 | 121.4656619197 | 31.1446329660 | 736 | 504990 | -89.30 | 11.98 | 446.74 | 0.12 | 2.23 | 1595 |
| 2024-09-20 22:21:41.329 | MS1 | 121.4656679398 | 31.1446279793 | 736 | 504990 | -89.76 | 9.10 | 322.14 | 0.20 | 2.09 | 1564 |
| 2024-09-20 22:21:42.946 | MS1 | 121.4656744672 | 31.1446357835 | 736 | 504990 | -91.11 | 7.22 | 575.93 | 0.10 | 2.47 | 1587 |

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
| 3212823 | 3 | 121.4716775118 | 31.1541289327 | 298 | 4 | 2 | 20.7 | TDD | 947 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3213695 | 4 | 121.4686844977 | 31.1517949525 | 120 | 14 | 12 | 27.8 | TDD | 847 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3251703 | 1 | 121.4645416307 | 31.1477611968 | 178 | 6 | 10 | 41.1 | TDD | 736 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3261305 | 2 | 121.4673663834 | 31.1483336861 | 70 | 9 | 6 | 48.8 | TDD | 185 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.286 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.309 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.453 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.453 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.151 | NREventA3 | measId:2;ServCellPCI:298;Se... |
| 2024-09-20 22:21:38.391 | NRHandoverAttempt | SourcePCI:298;SourceNR-ARFC... |
| 2024-09-20 22:21:38.425 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.439 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.568 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.568 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251703 | 1 | 6.9008 | 12.7440 | -117.2934 | 17.9719 | 115.6401 | 0.0060 | 0.0084 |
| 2024_09_20 22:00 | 3261305 | 2 | 8.6977 | 7.4586 | -114.7346 | 15.6117 | 171.3728 | 0.0096 | 0.0147 |
| 2024_09_20 22:00 | 3212823 | 3 | 11.5891 | 13.0256 | -114.4295 | 13.3051 | 88.2685 | 0.0131 | 0.0167 |
| 2024_09_20 22:00 | 3213695 | 4 | 18.2741 | 7.4972 | -115.7986 | 15.3911 | 158.6867 | 0.0004 | 0.0026 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414279_C60F5764 | 504990 | 736 | -85.7 | 504990 | 847 | -90.8 | 504990 | 185 | -98.6 | 504990 | 947 |
| MR_1774414279_F63B0205 | 504990 | 736 | -87.3 | 504990 | 847 | -89.4 | 504990 | 185 | -98.1 | 504990 | 947 |
| MR_1774414279_641CADF1 | 504990 | 736 | -86.2 | 504990 | 847 | -91.4 | 504990 | 185 | -100.5 | 504990 | 947 |
| MR_1774414279_2BCCC370 | 504990 | 736 | -86.5 | 504990 | 847 | -88.7 | 504990 | 185 | -100.3 | 504990 | 947 |
| MR_1774414279_F609D235 | 504990 | 736 | -86.7 | 504990 | 847 | -89.1 | 504990 | 185 | -101.9 | 504990 | 947 |
| MR_1774414279_35655FA7 | 504990 | 736 | -86.4 | 504990 | 847 | -88.7 | 504990 | 185 | -100.0 | 504990 | 947 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 8: `be9c0764-b59...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `be9c0764-b59e-4020-914c-b0baec18dd8b` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Lift the tilt angle  of 3239893_2 by 8 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[8] topology](images/train_0008.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3239893_2 by 8 degrees
- `C2`: Decrease transmission power for 3230193_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230193_3
- `C4`: Increase transmission power for 3247813_1
- `C5`: Decrease A3 Offset threshold for 3247813_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247813_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247813_1
- `C8`: Adjust the azimuth of 3230193_3 by 16 degrees
- `C9`: Increase transmission power for 3230193_3
- `C10`: Add neighbor relationship between 3230193_3 and 3247813_1
- `C11`: Press down the tilt angle of 3230193_3 by 5 degrees
- `C12`: Lift the tilt angle of 3230193_3 by 5 degrees
- `C13`: Lift the tilt angle  of 3239893_2 by 8 degrees **← 정답**
- `C14`: Increase A3 Offset threshold for 3247813_1
- `C15`: Check test server and transmission issues
- `C16`: Increase A3 Offset threshold for 3230193_3
- `C17`: Decrease A3 Offset threshold for 3230193_3
- `C18`: Adjust the azimuth of 3239893_2 by 50 degrees
- `C19`: Add neighbor relationship between 3239893_2 and 3247813_1
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease transmission power for 3247813_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230193_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.682 | MS1 | 121.4656768706 | 31.1446232562 | 693 | 504990 | -85.25 | 14.94 | 387.32 | 0.07 | 2.09 | 1578 |
| 2024-09-20 22:21:32.404 | MS1 | 121.4656669053 | 31.1446201291 | 693 | 504990 | -88.26 | 15.91 | 461.62 | 0.17 | 2.57 | 1592 |
| 2024-09-20 22:21:33.712 | MS1 | 121.4656645930 | 31.1446310875 | 693 | 504990 | -87.86 | 17.41 | 478.90 | 0.20 | 2.09 | 1574 |
| 2024-09-20 22:21:34.884 | MS1 | 121.4656748456 | 31.1446319241 | 693 | 504990 | -88.66 | 12.38 | 76.75 | 0.14 | 2.36 | 1578 |
| 2024-09-20 22:21:35.360 | MS1 | 121.4656772661 | 31.1446265767 | 693 | 504990 | -91.94 | 14.99 | 97.48 | 0.02 | 2.76 | 1590 |
| 2024-09-20 22:21:36.808 | MS1 | 121.4656582162 | 31.1446277505 | 693 | 504990 | -89.71 | 15.57 | 85.12 | 0.05 | 2.04 | 1574 |
| 2024-09-20 22:21:37.349 | MS1 | 121.4656677287 | 31.1446298338 | 693 | 504990 | -89.57 | 10.80 | 61.36 | 0.06 | 2.32 | 1563 |
| 2024-09-20 22:21:38.678 | MS1 | 121.4656603326 | 31.1446343216 | 693 | 504990 | -90.02 | 11.21 | 98.00 | 0.04 | 2.26 | 1578 |
| 2024-09-20 22:21:39.467 | MS1 | 121.4656754947 | 31.1446270394 | 693 | 504990 | -90.11 | 10.94 | 55.25 | 0.14 | 2.05 | 1564 |
| 2024-09-20 22:21:40.936 | MS1 | 121.4656670925 | 31.1446231233 | 693 | 504990 | -91.23 | 8.55 | 459.00 | 0.03 | 2.57 | 1569 |
| 2024-09-20 22:21:41.567 | MS1 | 121.4656771521 | 31.1446281638 | 693 | 504990 | -94.00 | 11.22 | 461.74 | 0.14 | 2.30 | 1582 |
| 2024-09-20 22:21:42.619 | MS1 | 121.4656611974 | 31.1446232838 | 693 | 504990 | -91.25 | 11.52 | 423.20 | 0.12 | 2.02 | 1572 |

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
| 3230193 | 3 | 121.4713592684 | 31.1497076213 | 208 | 4 | 5 | 15.3 | TDD | 693 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3232154 | 4 | 121.4649908703 | 31.1547540730 | 171 | 1 | 10 | 39.7 | TDD | 631 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3239893 | 2 | 121.4756695962 | 31.1510565872 | 64 | 1 | 4 | 16.3 | TDD | 841 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3247813 | 1 | 121.4715634552 | 31.1461574452 | 321 | 6 | 6 | 18.2 | TDD | 608 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.851 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.874 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.995 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.995 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.655 | NREventA3 | measId:2;ServCellPCI:416;Se... |
| 2024-09-20 22:21:37.895 | NRHandoverAttempt | SourcePCI:416;SourceNR-ARFC... |
| 2024-09-20 22:21:37.937 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.949 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.049 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.049 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247813 | 1 | 11.3685 | 16.9060 | -115.6139 | 8.0149 | 115.8071 | 0.0037 | 0.0057 |
| 2024_09_20 22:00 | 3239893 | 2 | 13.8536 | 6.6474 | -115.7727 | 19.4837 | 147.1758 | 0.0068 | 0.0045 |
| 2024_09_20 22:00 | 3230193 | 3 | 86.5085 | 92.1145 | -115.3098 | 16.2616 | 124.5245 | 0.0051 | 0.0087 |
| 2024_09_20 22:00 | 3232154 | 4 | 18.8561 | 16.0378 | -114.6386 | 9.8051 | 186.6835 | 0.0155 | 0.0046 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414846_0940F271 | 504990 | 693 | -90.4 | 504990 | 608 | -90.1 | 504990 | 841 | -96.7 | 504990 | 631 |
| MR_1774414846_B0EFFC1D | 504990 | 693 | -88.1 | 504990 | 608 | -87.4 | 504990 | 841 | -96.1 | 504990 | 631 |
| MR_1774414846_256EFD56 | 504990 | 693 | -89.1 | 504990 | 608 | -87.2 | 504990 | 841 | -97.8 | 504990 | 631 |
| MR_1774414846_EDBBAA71 | 504990 | 693 | -88.2 | 504990 | 608 | -90.3 | 504990 | 841 | -94.8 | 504990 | 631 |
| MR_1774414846_66EE1459 | 504990 | 693 | -87.1 | 504990 | 608 | -87.5 | 504990 | 841 | -94.4 | 504990 | 631 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 9: `8fbe9492-d54...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8fbe9492-d54a-4507-adb1-2a2bdd5ae757` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[9] topology](images/train_0009.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3271925_3
- `C2`: Lift the tilt angle  of 3271925_3 by 10 degrees
- `C3`: Add neighbor relationship between 3225098_1 and 3271925_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271925_3
- `C5`: Increase A3 Offset threshold for 3271925_3
- `C6`: Adjust the azimuth of 3271925_3 by 50 degrees
- `C7`: Add neighbor relationship between 3257710_4 and 3271925_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271925_3
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease A3 Offset threshold for 3225098_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225098_1
- `C12`: Press down the tilt angle of 3225098_1 by 6 degrees
- `C13`: Decrease A3 Offset threshold for 3271925_3
- `C14`: Increase A3 Offset threshold for 3225098_1
- `C15`: Decrease transmission power for 3271925_3
- `C16`: Check test server and transmission issues **← 정답**
- `C17`: Decrease transmission power for 3225098_1
- `C18`: Adjust the azimuth of 3225098_1 by 50 degrees
- `C19`: Lift the tilt angle of 3225098_1 by 6 degrees
- `C20`: Increase transmission power for 3225098_1
- `C21`: Press down the tilt angle  of 3271925_3 by 10 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225098_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.858 | MS1 | 121.4656733204 | 31.1446276824 | 197 | 504990 | -88.80 | 16.71 | 461.28 | 0.17 | 2.32 | 1588 |
| 2024-09-20 22:21:32.902 | MS1 | 121.4656776138 | 31.1446311613 | 197 | 504990 | -85.43 | 17.63 | 580.72 | 0.03 | 2.37 | 1574 |
| 2024-09-20 22:21:33.460 | MS1 | 121.4656714145 | 31.1446180379 | 197 | 504990 | -85.07 | 14.73 | 349.78 | 0.13 | 2.80 | 1574 |
| 2024-09-20 22:21:34.112 | MS1 | 121.4656618902 | 31.1446317640 | 197 | 504990 | -90.66 | 13.37 | 90.87 | 0.08 | 2.39 | 442 |
| 2024-09-20 22:21:35.520 | MS1 | 121.4656702287 | 31.1446250526 | 197 | 504990 | -86.40 | 16.51 | 76.11 | 0.18 | 2.92 | 465 |
| 2024-09-20 22:21:36.234 | MS1 | 121.4656683780 | 31.1446332731 | 197 | 504990 | -88.59 | 13.02 | 68.48 | 0.02 | 2.02 | 428 |
| 2024-09-20 22:21:37.368 | MS1 | 121.4656731256 | 31.1446275210 | 197 | 504990 | -92.02 | 11.84 | 89.53 | 0.09 | 2.51 | 499 |
| 2024-09-20 22:21:38.842 | MS1 | 121.4656714238 | 31.1446326916 | 197 | 504990 | -93.85 | 8.63 | 47.15 | 0.01 | 2.59 | 478 |
| 2024-09-20 22:21:39.235 | MS1 | 121.4656689616 | 31.1446214645 | 197 | 504990 | -92.97 | 11.86 | 62.27 | 0.06 | 2.43 | 323 |
| 2024-09-20 22:21:40.387 | MS1 | 121.4656669082 | 31.1446338742 | 197 | 504990 | -92.68 | 10.17 | 388.87 | 0.09 | 2.69 | 1599 |
| 2024-09-20 22:21:41.235 | MS1 | 121.4656751300 | 31.1446321283 | 197 | 504990 | -93.77 | 12.65 | 441.50 | 0.18 | 2.84 | 1589 |
| 2024-09-20 22:21:42.232 | MS1 | 121.4656686332 | 31.1446207319 | 197 | 504990 | -93.36 | 9.50 | 334.21 | 0.18 | 2.17 | 1576 |

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
| 3213779 | 2 | 121.4742287076 | 31.1478406362 | 5 | 0 | 10 | 27.2 | TDD | 795 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3225098 | 1 | 121.4749398815 | 31.1469343293 | 184 | 4 | 5 | 30.8 | TDD | 197 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3257710 | 4 | 121.4755478415 | 31.1506434227 | 234 | 14 | 2 | 47.9 | TDD | 317 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3271925 | 3 | 121.4640987473 | 31.1543509059 | 232 | 13 | 7 | 32.0 | TDD | 740 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.553 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.577 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.682 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.682 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.360 | NREventA3 | measId:2;ServCellPCI:947;Se... |
| 2024-09-20 22:21:38.600 | NRHandoverAttempt | SourcePCI:947;SourceNR-ARFC... |
| 2024-09-20 22:21:38.645 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.657 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.800 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.800 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225098 | 1 | 10.2676 | 14.3728 | -115.2517 | 15.1749 | 173.3995 | 0.0099 | 0.0168 |
| 2024_09_20 22:00 | 3213779 | 2 | 11.9924 | 6.2493 | -117.7247 | 16.5072 | 161.5478 | 0.0077 | 0.0036 |
| 2024_09_20 22:00 | 3271925 | 3 | 5.8327 | 12.3230 | -115.9839 | 14.8553 | 97.7999 | 0.0121 | 0.0060 |
| 2024_09_20 22:00 | 3257710 | 4 | 14.9642 | 7.4309 | -115.3454 | 14.4616 | 151.4326 | 0.0200 | 0.0121 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413708_B53596D5 | 504990 | 197 | -90.4 | 504990 | 740 | -91.6 | 504990 | 317 | -101.6 | 504990 | 795 |
| MR_1774413708_8372320E | 504990 | 197 | -91.8 | 504990 | 740 | -90.9 | 504990 | 317 | -99.4 | 504990 | 795 |
| MR_1774413708_62ED1AF5 | 504990 | 197 | -92.2 | 504990 | 740 | -92.1 | 504990 | 317 | -100.6 | 504990 | 795 |
| MR_1774413708_1F1C075D | 504990 | 197 | -92.0 | 504990 | 740 | -94.4 | 504990 | 317 | -98.2 | 504990 | 795 |
| MR_1774413708_C531D953 | 504990 | 197 | -90.9 | 504990 | 740 | -92.9 | 504990 | 317 | -99.6 | 504990 | 795 |

> *... 2개 열 생략 (전체 14열)*

---
