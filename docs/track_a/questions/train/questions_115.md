# Track A 문제 분석 — train[1140]~train[1149]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1140] ~ train[1149] (10개)

## 목차

1. [문제 1140: `14f6078d-20d...`](#1140) — single-answer, 정답: C12
2. [문제 1141: `cdf49c8a-795...`](#1141) — multiple-answer, 정답: C3|C10
3. [문제 1142: `5500c8df-8e7...`](#1142) — single-answer, 정답: C1
4. [문제 1143: `87846670-36b...`](#1143) — single-answer, 정답: C11
5. [문제 1144: `b6426d34-4e9...`](#1144) — single-answer, 정답: C19
6. [문제 1145: `7ff6866a-178...`](#1145) — multiple-answer, 정답: C13|C22
7. [문제 1146: `dbf92c4d-da5...`](#1146) — single-answer, 정답: C20
8. [문제 1147: `d50c0c8f-b24...`](#1147) — multiple-answer, 정답: C6|C20
9. [문제 1148: `2ba7f60f-a34...`](#1148) — single-answer, 정답: C13
10. [문제 1149: `68c16290-7cc...`](#1149) — single-answer, 정답: C16

---

### 문제 1140: `14f6078d-20d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `14f6078d-20d6-4926-989c-4b77aafa0023` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3210032_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1140] topology](images/train_1140.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3264569_4 by 10 degrees
- `C2`: Check test server and transmission issues
- `C3`: Add neighbor relationship between 3263655_3 and 3264569_4
- `C4`: Decrease transmission power for 3264569_4
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase transmission power for 3264569_4
- `C7`: Lift the tilt angle of 3210032_1 by 1 degrees
- `C8`: Increase transmission power for 3210032_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264569_4
- `C10`: Press down the tilt angle of 3210032_1 by 1 degrees
- `C11`: Lift the tilt angle  of 3264569_4 by 10 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210032_1 **← 정답**
- `C13`: Decrease A3 Offset threshold for 3210032_1
- `C14`: Adjust the azimuth of 3210032_1 by 8 degrees
- `C15`: Add neighbor relationship between 3210032_1 and 3264569_4
- `C16`: Increase A3 Offset threshold for 3264569_4
- `C17`: Decrease A3 Offset threshold for 3264569_4
- `C18`: Decrease transmission power for 3210032_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210032_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264569_4
- `C21`: Adjust the azimuth of 3264569_4 by 50 degrees
- `C22`: Increase A3 Offset threshold for 3210032_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.149 | MS1 | 121.4656642339 | 31.1446284939 | 717 | 504990 | -89.93 | 12.76 | 566.74 | 0.20 | 2.44 | 1589 |
| 2024-09-20 22:21:32.978 | MS1 | 121.4656639855 | 31.1446337856 | 717 | 504990 | -88.33 | 14.39 | 393.82 | 0.17 | 2.48 | 1588 |
| 2024-09-20 22:21:33.412 | MS1 | 121.4656777975 | 31.1446223755 | 717 | 504990 | -91.57 | 14.69 | 493.58 | 0.10 | 2.46 | 1582 |
| 2024-09-20 22:21:34.323 | MS1 | 121.4656656608 | 31.1446241160 | 717 | 504990 | -91.74 | 15.12 | 86.68 | 0.66 | 2.02 | 532 |
| 2024-09-20 22:21:35.394 | MS1 | 121.4656722254 | 31.1446305393 | 717 | 504990 | -85.71 | 15.13 | 72.54 | 0.59 | 2.58 | 525 |
| 2024-09-20 22:21:36.648 | MS1 | 121.4656715967 | 31.1446209809 | 717 | 504990 | -89.67 | 14.09 | 89.56 | 0.52 | 2.05 | 613 |
| 2024-09-20 22:21:37.489 | MS1 | 121.4656721710 | 31.1446251744 | 717 | 504990 | -89.82 | 9.73 | 93.83 | 0.57 | 2.69 | 506 |
| 2024-09-20 22:21:38.745 | MS1 | 121.4656671263 | 31.1446327352 | 717 | 504990 | -90.31 | 12.21 | 69.31 | 0.55 | 2.37 | 671 |
| 2024-09-20 22:21:39.447 | MS1 | 121.4656596948 | 31.1446219877 | 717 | 504990 | -93.96 | 7.41 | 59.46 | 0.55 | 2.74 | 535 |
| 2024-09-20 22:21:40.165 | MS1 | 121.4656735656 | 31.1446186685 | 717 | 504990 | -90.63 | 7.26 | 390.17 | 0.13 | 2.41 | 1571 |
| 2024-09-20 22:21:41.328 | MS1 | 121.4656630835 | 31.1446213698 | 717 | 504990 | -89.04 | 12.16 | 592.16 | 0.13 | 2.62 | 1566 |
| 2024-09-20 22:21:42.971 | MS1 | 121.4656593858 | 31.1446312118 | 717 | 504990 | -91.71 | 11.04 | 555.35 | 0.14 | 2.62 | 1562 |

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
| 3210032 | 1 | 121.4663010994 | 31.1551625737 | 175 | 0 | 8 | 20.7 | TDD | 717 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3215036 | 2 | 121.4689570439 | 31.1500545520 | 355 | 1 | 7 | 48.3 | TDD | 283 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3263655 | 3 | 121.4741624806 | 31.1511489114 | 332 | 12 | 9 | 30.3 | TDD | 365 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3264569 | 4 | 121.4716314149 | 31.1454901850 | 133 | 11 | 5 | 18.1 | TDD | 511 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.750 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.770 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.910 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.910 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.606 | NREventA3 | measId:2;ServCellPCI:745;Se... |
| 2024-09-20 22:21:37.846 | NRHandoverAttempt | SourcePCI:745;SourceNR-ARFC... |
| 2024-09-20 22:21:37.881 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.894 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.037 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.037 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210032 | 1 | 9.1602 | 10.7903 | -116.3841 | 7.3164 | 130.1286 | 0.0186 | 0.0103 |
| 2024_09_20 22:00 | 3215036 | 2 | 6.1136 | 18.5256 | -114.0076 | 17.5250 | 169.3447 | 0.0101 | 0.0168 |
| 2024_09_20 22:00 | 3263655 | 3 | 16.2246 | 7.7082 | -116.4157 | 6.6013 | 111.8645 | 0.0030 | 0.0014 |
| 2024_09_20 22:00 | 3264569 | 4 | 14.0700 | 10.0622 | -117.8673 | 5.6111 | 85.9592 | 0.0137 | 0.0061 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415509_832C31DE | 504990 | 717 | -91.9 | 504990 | 511 | -96.6 | 504990 | 365 | -102.2 | 504990 | 283 |
| MR_1774415509_B65C2029 | 504990 | 717 | -90.5 | 504990 | 511 | -96.4 | 504990 | 365 | -100.9 | 504990 | 283 |
| MR_1774415509_C39DCAF4 | 504990 | 717 | -93.4 | 504990 | 511 | -98.0 | 504990 | 365 | -100.9 | 504990 | 283 |
| MR_1774415509_E65AE990 | 504990 | 717 | -90.7 | 504990 | 511 | -95.8 | 504990 | 365 | -99.5 | 504990 | 283 |
| MR_1774415509_13F299D5 | 504990 | 717 | -92.0 | 504990 | 511 | -95.7 | 504990 | 365 | -101.5 | 504990 | 283 |
| MR_1774415509_16E96B9E | 504990 | 717 | -91.0 | 504990 | 511 | -94.3 | 504990 | 365 | -100.4 | 504990 | 283 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1141: `cdf49c8a-795...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cdf49c8a-7953-43e5-8062-e5b6db5f6f23` |
| Tag | **multiple-answer** |
| 정답 | **C3|C10** |
| C3 의미 | Press down the tilt angle  of 3250790_2 by 5 degrees |
| C10 의미 | Decrease transmission power for 3250790_2 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1141] topology](images/train_1141.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3240492_1
- `C2`: Adjust the azimuth of 3240492_1 by 24 degrees
- `C3`: Press down the tilt angle  of 3250790_2 by 5 degrees **← 정답**
- `C4`: Increase A3 Offset threshold for 3240492_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240492_1
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250790_2
- `C8`: Check test server and transmission issues
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250790_2
- `C10`: Decrease transmission power for 3250790_2 **← 정답**
- `C11`: Decrease transmission power for 3240492_1
- `C12`: Add neighbor relationship between 3240492_1 and 3250790_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240492_1
- `C14`: Increase transmission power for 3250790_2
- `C15`: Add neighbor relationship between 3224797_4 and 3250790_2
- `C16`: Lift the tilt angle  of 3250790_2 by 5 degrees
- `C17`: Decrease A3 Offset threshold for 3250790_2
- `C18`: Adjust the azimuth of 3250790_2 by 14 degrees
- `C19`: Increase transmission power for 3240492_1
- `C20`: Lift the tilt angle of 3240492_1 by 4 degrees
- `C21`: Press down the tilt angle of 3240492_1 by 4 degrees
- `C22`: Increase A3 Offset threshold for 3250790_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.509 | MS1 | 121.4656595749 | 31.1446335079 | 369 | 504990 | -78.77 | 12.63 | 318.69 | 0.14 | 2.03 | 1586 |
| 2024-09-20 22:21:32.855 | MS1 | 121.4656613298 | 31.1446316878 | 369 | 504990 | -84.95 | 15.24 | 553.14 | 0.09 | 2.95 | 1581 |
| 2024-09-20 22:21:33.919 | MS1 | 121.4656768014 | 31.1446207931 | 369 | 504990 | -76.92 | 15.44 | 557.76 | 0.01 | 2.14 | 1591 |
| 2024-09-20 22:21:34.449 | MS1 | 121.4656749106 | 31.1446240414 | 369 | 504990 | -88.34 | 3.53 | 94.15 | 0.16 | 1.42 | 1585 |
| 2024-09-20 22:21:35.472 | MS1 | 121.4656691441 | 31.1446320795 | 369 | 504990 | -90.13 | 2.83 | 61.24 | 0.01 | 1.07 | 1560 |
| 2024-09-20 22:21:36.192 | MS1 | 121.4656586357 | 31.1446269375 | 369 | 504990 | -93.40 | 2.61 | 69.55 | 0.11 | 1.14 | 1565 |
| 2024-09-20 22:21:37.928 | MS1 | 121.4656668527 | 31.1446182861 | 369 | 504990 | -91.50 | 3.33 | 58.43 | 0.11 | 1.30 | 1595 |
| 2024-09-20 22:21:38.510 | MS1 | 121.4656700898 | 31.1446341452 | 369 | 504990 | -90.06 | 2.69 | 68.73 | 0.06 | 1.49 | 1584 |
| 2024-09-20 22:21:39.621 | MS1 | 121.4656741431 | 31.1446309164 | 369 | 504990 | -85.88 | 1.28 | 59.90 | 0.15 | 1.36 | 1594 |
| 2024-09-20 22:21:40.841 | MS1 | 121.4656679282 | 31.1446367067 | 369 | 504990 | -75.99 | 17.97 | 540.67 | 0.10 | 2.16 | 1575 |
| 2024-09-20 22:21:41.884 | MS1 | 121.4656626923 | 31.1446271948 | 369 | 504990 | -78.66 | 14.33 | 573.11 | 0.19 | 2.32 | 1566 |
| 2024-09-20 22:21:42.332 | MS1 | 121.4656657425 | 31.1446180526 | 369 | 504990 | -82.30 | 13.19 | 470.30 | 0.00 | 2.21 | 1562 |

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
| 3224797 | 4 | 121.4680722994 | 31.1546300685 | 251 | 11 | 7 | 36.9 | TDD | 127 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3225556 | 3 | 121.4662923149 | 31.1449309151 | 288 | 2 | 12 | 43.4 | TDD | 702 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3240492 | 1 | 121.4755816734 | 31.1545931410 | 244 | 3 | 12 | 37.7 | TDD | 369 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3250790 | 2 | 121.4653014027 | 31.1498925899 | 191 | 3 | 11 | 24.3 | TDD | 678 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.248 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.264 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.365 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.365 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240492 | 1 | 14.6487 | 10.1995 | -108.6025 | 7.2252 | 189.2469 | 0.0014 | 0.0142 |
| 2024_09_20 22:00 | 3250790 | 2 | 5.1211 | 8.1903 | -115.0523 | 16.6182 | 194.5921 | 0.0006 | 0.0197 |
| 2024_09_20 22:00 | 3225556 | 3 | 16.3571 | 12.4818 | -116.5671 | 18.6995 | 181.0098 | 0.0196 | 0.0031 |
| 2024_09_20 22:00 | 3224797 | 4 | 15.2355 | 13.5212 | -115.3083 | 14.4373 | 195.3868 | 0.0082 | 0.0125 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414976_5EFC4E31 | 504990 | 369 | -86.4 | 504990 | 678 | -89.3 | 504990 | 127 | -90.5 | 504990 | 702 |
| MR_1774414976_7359E3F0 | 504990 | 369 | -89.1 | 504990 | 678 | -89.1 | 504990 | 127 | -87.5 | 504990 | 702 |
| MR_1774414976_0466D80D | 504990 | 678 | -87.8 | 504990 | 369 | -86.7 | 504990 | 127 | -87.8 | 504990 | 702 |
| MR_1774414976_DE1A0037 | 504990 | 369 | -90.2 | 504990 | 678 | -86.8 | 504990 | 127 | -90.1 | 504990 | 702 |
| MR_1774414976_AED0D63A | 504990 | 369 | -89.5 | 504990 | 678 | -89.9 | 504990 | 127 | -88.7 | 504990 | 702 |
| MR_1774414976_C122162D | 504990 | 369 | -87.9 | 504990 | 678 | -89.2 | 504990 | 127 | -90.2 | 504990 | 702 |
| MR_1774414976_790F57D6 | 504990 | 369 | -89.0 | 504990 | 678 | -90.0 | 504990 | 127 | -90.3 | 504990 | 702 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1142: `5500c8df-8e7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5500c8df-8e72-49fa-bd6d-325ac9345766` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Lift the tilt angle  of 3220501_4 by 9 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1142] topology](images/train_1142.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3220501_4 by 9 degrees **← 정답**
- `C2`: Decrease A3 Offset threshold for 3241936_3
- `C3`: Decrease transmission power for 3268911_1
- `C4`: Press down the tilt angle  of 3220501_4 by 9 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Press down the tilt angle of 3268911_1 by 3 degrees
- `C7`: Increase transmission power for 3241936_3
- `C8`: Increase A3 Offset threshold for 3268911_1
- `C9`: Add neighbor relationship between 3268911_1 and 3241936_3
- `C10`: Decrease transmission power for 3241936_3
- `C11`: Increase transmission power for 3268911_1
- `C12`: Add neighbor relationship between 3220501_4 and 3241936_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241936_3
- `C14`: Lift the tilt angle of 3268911_1 by 3 degrees
- `C15`: Adjust the azimuth of 3268911_1 by 44 degrees
- `C16`: Decrease A3 Offset threshold for 3268911_1
- `C17`: Check test server and transmission issues
- `C18`: Increase A3 Offset threshold for 3241936_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268911_1
- `C20`: Adjust the azimuth of 3220501_4 by 50 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241936_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268911_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.544 | MS1 | 121.4656773737 | 31.1446288729 | 329 | 504990 | -85.27 | 16.73 | 570.67 | 0.15 | 2.63 | 1593 |
| 2024-09-20 22:21:32.713 | MS1 | 121.4656640971 | 31.1446306197 | 329 | 504990 | -89.06 | 12.66 | 501.81 | 0.07 | 2.86 | 1588 |
| 2024-09-20 22:21:33.929 | MS1 | 121.4656652557 | 31.1446377993 | 329 | 504990 | -86.76 | 17.62 | 428.74 | 0.20 | 2.91 | 1582 |
| 2024-09-20 22:21:34.923 | MS1 | 121.4656777273 | 31.1446327280 | 329 | 504990 | -91.34 | 12.54 | 81.87 | 0.07 | 2.49 | 1583 |
| 2024-09-20 22:21:35.626 | MS1 | 121.4656631839 | 31.1446379907 | 329 | 504990 | -91.13 | 13.93 | 80.03 | 0.10 | 2.73 | 1592 |
| 2024-09-20 22:21:36.719 | MS1 | 121.4656613108 | 31.1446361804 | 329 | 504990 | -90.28 | 15.78 | 82.29 | 0.15 | 2.32 | 1592 |
| 2024-09-20 22:21:37.227 | MS1 | 121.4656638927 | 31.1446226214 | 329 | 504990 | -90.91 | 8.57 | 71.66 | 0.01 | 2.59 | 1583 |
| 2024-09-20 22:21:38.233 | MS1 | 121.4656743706 | 31.1446287639 | 329 | 504990 | -90.33 | 9.47 | 85.22 | 0.09 | 2.87 | 1571 |
| 2024-09-20 22:21:39.639 | MS1 | 121.4656606659 | 31.1446257501 | 329 | 504990 | -91.22 | 10.37 | 80.81 | 0.07 | 2.06 | 1573 |
| 2024-09-20 22:21:40.683 | MS1 | 121.4656779970 | 31.1446302656 | 329 | 504990 | -92.37 | 8.83 | 414.85 | 0.05 | 2.04 | 1598 |
| 2024-09-20 22:21:41.384 | MS1 | 121.4656719398 | 31.1446193017 | 329 | 504990 | -90.22 | 7.03 | 591.33 | 0.19 | 2.96 | 1577 |
| 2024-09-20 22:21:42.532 | MS1 | 121.4656667547 | 31.1446186701 | 329 | 504990 | -90.79 | 10.31 | 355.95 | 0.14 | 2.53 | 1568 |

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
| 3220501 | 4 | 121.4645282083 | 31.1509635610 | 314 | 5 | 10 | 34.6 | TDD | 983 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3241936 | 3 | 121.4756492949 | 31.1478550001 | 45 | 6 | 1 | 47.5 | TDD | 950 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3268911 | 1 | 121.4675905039 | 31.1479127603 | 163 | 1 | 5 | 17.0 | TDD | 329 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3277798 | 2 | 121.4745678538 | 31.1534460799 | 309 | 6 | 1 | 33.2 | TDD | 748 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.211 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.232 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.351 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.351 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.043 | NREventA3 | measId:2;ServCellPCI:393;Se... |
| 2024-09-20 22:21:38.283 | NRHandoverAttempt | SourcePCI:393;SourceNR-ARFC... |
| 2024-09-20 22:21:38.315 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.325 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.438 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.438 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268911 | 1 | 80.1140 | 84.0278 | -115.9000 | 19.0688 | 194.1330 | 0.0020 | 0.0134 |
| 2024_09_20 22:00 | 3277798 | 2 | 14.4403 | 9.1647 | -117.7911 | 14.3501 | 185.1051 | 0.0073 | 0.0115 |
| 2024_09_20 22:00 | 3241936 | 3 | 17.9097 | 9.5493 | -116.0439 | 16.1039 | 162.1184 | 0.0194 | 0.0122 |
| 2024_09_20 22:00 | 3220501 | 4 | 6.0910 | 15.0126 | -117.9387 | 6.8277 | 156.5452 | 0.0166 | 0.0169 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412867_7A337456 | 504990 | 329 | -91.1 | 504990 | 950 | -91.7 | 504990 | 983 | -100.5 | 504990 | 748 |
| MR_1774412867_CAC23109 | 504990 | 329 | -93.0 | 504990 | 950 | -93.4 | 504990 | 983 | -103.3 | 504990 | 748 |
| MR_1774412867_B8874FCA | 504990 | 329 | -90.2 | 504990 | 950 | -93.8 | 504990 | 983 | -100.4 | 504990 | 748 |
| MR_1774412867_2A8DD1CB | 504990 | 329 | -93.1 | 504990 | 950 | -93.0 | 504990 | 983 | -103.2 | 504990 | 748 |
| MR_1774412867_A80D973B | 504990 | 329 | -92.0 | 504990 | 950 | -90.3 | 504990 | 983 | -103.3 | 504990 | 748 |
| MR_1774412867_53632E52 | 504990 | 329 | -92.0 | 504990 | 950 | -90.5 | 504990 | 983 | -101.9 | 504990 | 748 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1143: `87846670-36b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `87846670-36b3-4858-a6b0-d267c1aadf83` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Add neighbor relationship between 3225666_1 and 3235136_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1143] topology](images/train_1143.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225666_1
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease A3 Offset threshold for 3225666_1
- `C4`: Press down the tilt angle  of 3235136_3 by 5 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225666_1
- `C6`: Adjust the azimuth of 3225666_1 by 50 degrees
- `C7`: Press down the tilt angle of 3225666_1 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235136_3
- `C9`: Check test server and transmission issues
- `C10`: Increase transmission power for 3225666_1
- `C11`: Add neighbor relationship between 3225666_1 and 3235136_3 **← 정답**
- `C12`: Adjust the azimuth of 3235136_3 by 22 degrees
- `C13`: Increase A3 Offset threshold for 3235136_3
- `C14`: Decrease transmission power for 3225666_1
- `C15`: Decrease transmission power for 3235136_3
- `C16`: Lift the tilt angle of 3225666_1 by 10 degrees
- `C17`: Decrease A3 Offset threshold for 3235136_3
- `C18`: Increase transmission power for 3235136_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235136_3
- `C20`: Lift the tilt angle  of 3235136_3 by 5 degrees
- `C21`: Add neighbor relationship between 3266488_2 and 3235136_3
- `C22`: Increase A3 Offset threshold for 3225666_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.684 | MS1 | 121.4656766024 | 31.1446349560 | 570 | 504990 | -77.38 | 12.60 | 414.22 | 0.12 | 2.54 | 1590 |
| 2024-09-20 22:21:32.660 | MS1 | 121.4656584181 | 31.1446324994 | 570 | 504990 | -79.43 | 17.34 | 350.99 | 0.15 | 2.47 | 1588 |
| 2024-09-20 22:21:33.853 | MS1 | 121.4656710418 | 31.1446308507 | 570 | 504990 | -84.63 | 13.62 | 456.26 | 0.10 | 2.70 | 1572 |
| 2024-09-20 22:21:34.704 | MS1 | 121.4656748912 | 31.1446368990 | 570 | 504990 | -90.38 | -0.52 | 54.76 | 0.11 | 1.03 | 1571 |
| 2024-09-20 22:21:35.234 | MS1 | 121.4656662676 | 31.1446254462 | 570 | 504990 | -90.00 | -1.23 | 41.20 | 0.01 | 1.42 | 1571 |
| 2024-09-20 22:21:36.517 | MS1 | 121.4656722251 | 31.1446244114 | 570 | 504990 | -87.68 | -1.46 | 58.88 | 0.02 | 1.09 | 1562 |
| 2024-09-20 22:21:37.381 | MS1 | 121.4656649451 | 31.1446231973 | 570 | 504990 | -85.42 | -1.23 | 62.00 | 0.00 | 1.32 | 1593 |
| 2024-09-20 22:21:38.984 | MS1 | 121.4656670027 | 31.1446311097 | 570 | 504990 | -76.02 | 15.38 | 386.96 | 0.20 | 1.02 | 1560 |
| 2024-09-20 22:21:39.739 | MS1 | 121.4656607556 | 31.1446357426 | 570 | 504990 | -76.22 | 16.63 | 551.54 | 0.06 | 1.00 | 1590 |
| 2024-09-20 22:21:40.639 | MS1 | 121.4656760524 | 31.1446370123 | 570 | 504990 | -78.33 | 12.20 | 448.41 | 0.15 | 2.41 | 1564 |
| 2024-09-20 22:21:41.335 | MS1 | 121.4656633592 | 31.1446371851 | 570 | 504990 | -76.20 | 16.50 | 426.92 | 0.08 | 2.00 | 1579 |
| 2024-09-20 22:21:42.722 | MS1 | 121.4656592466 | 31.1446223697 | 570 | 504990 | -83.33 | 12.87 | 385.97 | 0.05 | 2.29 | 1581 |

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
| 3211520 | 4 | 121.4727085285 | 31.1477495500 | 183 | 14 | 8 | 36.8 | TDD | 655 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3225666 | 1 | 121.4656230734 | 31.1469129406 | 57 | 7 | 0 | 45.0 | TDD | 570 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3235136 | 3 | 121.4701237699 | 31.1546500443 | 179 | 3 | 8 | 45.0 | TDD | 106 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3266488 | 2 | 121.4715825172 | 31.1495951985 | 142 | 5 | 2 | 41.4 | TDD | 47 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.417 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.433 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.577 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.577 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.233 | NREventA3 | measId:2;ServCellPCI:497;Se... |
| 2024-09-20 22:21:36.233 | NREventA3 | measId:2;ServCellPCI:497;Se... |
| 2024-09-20 22:21:37.233 | NREventA3 | measId:2;ServCellPCI:497;Se... |
| 2024-09-20 22:21:39.733 | NRRRCReestablishAttempt | PCI:497 |
| 2024-09-20 22:21:39.745 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.760 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.906 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.906 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225666 | 1 | 9.6209 | 19.2672 | -116.3115 | 8.3291 | 113.1274 | 0.0103 | 0.1159 |
| 2024_09_20 22:00 | 3266488 | 2 | 10.2435 | 8.0741 | -117.1276 | 15.7383 | 161.0533 | 0.0082 | 0.0060 |
| 2024_09_20 22:00 | 3235136 | 3 | 9.0839 | 19.3230 | -114.0232 | 10.5237 | 146.6604 | 0.0054 | 0.0178 |
| 2024_09_20 22:00 | 3211520 | 4 | 14.3041 | 8.7079 | -117.1703 | 7.2763 | 80.3657 | 0.0040 | 0.0080 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417169_B4F559C2 | 504990 | 570 | -88.9 | 504990 | 106 | -87.6 | 504990 | 47 | -90.9 | 504990 | 655 |
| MR_1774417169_34AD3414 | 504990 | 570 | -90.8 | 504990 | 106 | -85.0 | 504990 | 47 | -91.5 | 504990 | 655 |
| MR_1774417169_1ABF624E | 504990 | 106 | -85.7 | 504990 | 570 | -92.1 | 504990 | 47 | -89.7 | 504990 | 655 |
| MR_1774417169_A8D5061E | 504990 | 106 | -87.6 | 504990 | 570 | -90.1 | 504990 | 47 | -90.5 | 504990 | 655 |
| MR_1774417169_F29B40B3 | 504990 | 106 | -87.4 | 504990 | 570 | -89.6 | 504990 | 47 | -91.2 | 504990 | 655 |
| MR_1774417169_A0DB5440 | 504990 | 106 | -85.1 | 504990 | 570 | -90.8 | 504990 | 47 | -93.1 | 504990 | 655 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1144: `b6426d34-4e9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b6426d34-4e96-47e7-9a3a-fc9b11e01c97` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1144] topology](images/train_1144.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3245243_2
- `C2`: Increase A3 Offset threshold for 3225739_4
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Press down the tilt angle  of 3245243_2 by 10 degrees
- `C5`: Add neighbor relationship between 3225739_4 and 3245243_2
- `C6`: Add neighbor relationship between 3212361_3 and 3245243_2
- `C7`: Lift the tilt angle  of 3245243_2 by 10 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245243_2
- `C9`: Adjust the azimuth of 3245243_2 by 50 degrees
- `C10`: Decrease A3 Offset threshold for 3225739_4
- `C11`: Adjust the azimuth of 3225739_4 by 50 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225739_4
- `C13`: Increase A3 Offset threshold for 3245243_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245243_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225739_4
- `C16`: Decrease transmission power for 3245243_2
- `C17`: Press down the tilt angle of 3225739_4 by 10 degrees
- `C18`: Decrease transmission power for 3225739_4
- `C19`: Check test server and transmission issues **← 정답**
- `C20`: Increase transmission power for 3245243_2
- `C21`: Increase transmission power for 3225739_4
- `C22`: Lift the tilt angle of 3225739_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.300 | MS1 | 121.4656723640 | 31.1446203592 | 324 | 504990 | -89.29 | 17.63 | 363.15 | 0.11 | 2.12 | 1561 |
| 2024-09-20 22:21:32.853 | MS1 | 121.4656678164 | 31.1446225975 | 324 | 504990 | -87.17 | 14.19 | 577.00 | 0.16 | 2.30 | 1570 |
| 2024-09-20 22:21:33.295 | MS1 | 121.4656667371 | 31.1446210479 | 324 | 504990 | -90.70 | 14.63 | 519.56 | 0.20 | 2.29 | 1582 |
| 2024-09-20 22:21:34.719 | MS1 | 121.4656775703 | 31.1446231143 | 324 | 504990 | -88.66 | 14.97 | 84.19 | 0.02 | 2.22 | 403 |
| 2024-09-20 22:21:35.404 | MS1 | 121.4656760195 | 31.1446221063 | 324 | 504990 | -91.25 | 13.38 | 75.36 | 0.18 | 2.25 | 432 |
| 2024-09-20 22:21:36.809 | MS1 | 121.4656648147 | 31.1446376608 | 324 | 504990 | -87.39 | 17.82 | 106.48 | 0.05 | 2.38 | 432 |
| 2024-09-20 22:21:37.508 | MS1 | 121.4656774556 | 31.1446190152 | 324 | 504990 | -93.44 | 7.93 | 50.55 | 0.09 | 2.69 | 480 |
| 2024-09-20 22:21:38.207 | MS1 | 121.4656624306 | 31.1446359111 | 324 | 504990 | -92.11 | 8.89 | 73.68 | 0.02 | 2.92 | 425 |
| 2024-09-20 22:21:39.145 | MS1 | 121.4656666749 | 31.1446180174 | 324 | 504990 | -90.69 | 10.37 | 73.90 | 0.11 | 2.48 | 425 |
| 2024-09-20 22:21:40.398 | MS1 | 121.4656746323 | 31.1446333995 | 324 | 504990 | -89.86 | 11.13 | 387.84 | 0.00 | 2.62 | 1575 |
| 2024-09-20 22:21:41.527 | MS1 | 121.4656616229 | 31.1446214344 | 324 | 504990 | -89.95 | 12.12 | 327.47 | 0.09 | 2.91 | 1574 |
| 2024-09-20 22:21:42.202 | MS1 | 121.4656758498 | 31.1446315887 | 324 | 504990 | -93.89 | 9.34 | 421.39 | 0.04 | 2.34 | 1570 |

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
| 3212361 | 3 | 121.4694048210 | 31.1501124701 | 112 | 11 | 12 | 46.8 | TDD | 837 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3225739 | 4 | 121.4711151937 | 31.1470963789 | 22 | 11 | 9 | 24.9 | TDD | 324 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3245243 | 2 | 121.4652461349 | 31.1451221663 | 250 | 8 | 7 | 29.0 | TDD | 964 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3279443 | 1 | 121.4721603341 | 31.1554454761 | 107 | 15 | 6 | 16.1 | TDD | 685 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.454 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.471 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.574 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.574 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.255 | NREventA3 | measId:2;ServCellPCI:572;Se... |
| 2024-09-20 22:21:38.495 | NRHandoverAttempt | SourcePCI:572;SourceNR-ARFC... |
| 2024-09-20 22:21:38.544 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.556 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.705 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.705 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279443 | 1 | 19.1823 | 10.5546 | -114.9343 | 7.5705 | 191.3486 | 0.0010 | 0.0094 |
| 2024_09_20 22:00 | 3245243 | 2 | 7.1760 | 6.4070 | -115.8038 | 13.0335 | 130.4402 | 0.0178 | 0.0178 |
| 2024_09_20 22:00 | 3212361 | 3 | 18.3409 | 16.3180 | -115.5876 | 16.0459 | 97.0363 | 0.0048 | 0.0107 |
| 2024_09_20 22:00 | 3225739 | 4 | 18.0139 | 18.0390 | -114.3991 | 14.8074 | 157.9291 | 0.0064 | 0.0101 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415085_0F4B1738 | 504990 | 324 | -90.1 | 504990 | 964 | -98.1 | 504990 | 837 | -100.2 | 504990 | 685 |
| MR_1774415085_E6E7F947 | 504990 | 324 | -89.7 | 504990 | 964 | -94.5 | 504990 | 837 | -103.4 | 504990 | 685 |
| MR_1774415085_7758004F | 504990 | 324 | -89.9 | 504990 | 964 | -94.6 | 504990 | 837 | -100.4 | 504990 | 685 |
| MR_1774415085_DBFD0589 | 504990 | 324 | -90.5 | 504990 | 964 | -95.8 | 504990 | 837 | -101.3 | 504990 | 685 |
| MR_1774415085_E2D8AAE5 | 504990 | 324 | -87.0 | 504990 | 964 | -96.6 | 504990 | 837 | -100.3 | 504990 | 685 |
| MR_1774415085_8EC76FDB | 504990 | 324 | -87.4 | 504990 | 964 | -94.9 | 504990 | 837 | -100.1 | 504990 | 685 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1145: `7ff6866a-178...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7ff6866a-178c-4431-ab21-267163ee4fee` |
| Tag | **multiple-answer** |
| 정답 | **C13|C22** |
| C13 의미 | Adjust the azimuth of 3232455_1 by 25 degrees |
| C22 의미 | Increase transmission power for 3232455_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1145] topology](images/train_1145.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263386_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263386_3
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Lift the tilt angle of 3232455_1 by 10 degrees
- `C5`: Increase transmission power for 3263386_3
- `C6`: Check test server and transmission issues
- `C7`: Increase A3 Offset threshold for 3232455_1
- `C8`: Decrease transmission power for 3263386_3
- `C9`: Press down the tilt angle of 3232455_1 by 10 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232455_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232455_1
- `C12`: Decrease transmission power for 3232455_1
- `C13`: Adjust the azimuth of 3232455_1 by 25 degrees **← 정답**
- `C14`: Lift the tilt angle  of 3263386_3 by 1 degrees
- `C15`: Adjust the azimuth of 3263386_3 by 48 degrees
- `C16`: Decrease A3 Offset threshold for 3232455_1
- `C17`: Increase A3 Offset threshold for 3263386_3
- `C18`: Add neighbor relationship between 3232455_1 and 3263386_3
- `C19`: Press down the tilt angle  of 3263386_3 by 1 degrees
- `C20`: Decrease A3 Offset threshold for 3263386_3
- `C21`: Add neighbor relationship between 3263451_2 and 3263386_3
- `C22`: Increase transmission power for 3232455_1 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.192 | MS1 | 121.4656585233 | 31.1446272378 | 504 | 504990 | -89.50 | 17.87 | 334.23 | 0.05 | 2.43 | 1600 |
| 2024-09-20 22:21:32.753 | MS1 | 121.4656700283 | 31.1446235302 | 504 | 504990 | -93.74 | 17.69 | 430.80 | 0.19 | 2.29 | 1589 |
| 2024-09-20 22:21:33.323 | MS1 | 121.4656650547 | 31.1446320130 | 504 | 504990 | -87.57 | 17.79 | 445.04 | 0.16 | 2.37 | 1572 |
| 2024-09-20 22:21:34.806 | MS1 | 121.4656586488 | 31.1446289465 | 504 | 504990 | -107.52 | -0.25 | 55.07 | 0.16 | 1.40 | 1597 |
| 2024-09-20 22:21:35.157 | MS1 | 121.4656773678 | 31.1446359149 | 504 | 504990 | -107.78 | 1.97 | 40.32 | 0.14 | 1.06 | 1589 |
| 2024-09-20 22:21:36.482 | MS1 | 121.4656732565 | 31.1446291273 | 504 | 504990 | -101.60 | -1.58 | 82.00 | 0.17 | 1.16 | 1587 |
| 2024-09-20 22:21:37.639 | MS1 | 121.4656728774 | 31.1446207022 | 504 | 504990 | -101.85 | 0.58 | 63.71 | 0.03 | 1.47 | 1594 |
| 2024-09-20 22:21:38.185 | MS1 | 121.4656748515 | 31.1446348188 | 504 | 504990 | -100.05 | 0.28 | 67.63 | 0.04 | 1.25 | 1567 |
| 2024-09-20 22:21:39.634 | MS1 | 121.4656739408 | 31.1446367113 | 504 | 504990 | -102.30 | 1.15 | 74.19 | 0.05 | 1.15 | 1562 |
| 2024-09-20 22:21:40.710 | MS1 | 121.4656614977 | 31.1446356033 | 504 | 504990 | -87.03 | 13.71 | 457.70 | 0.05 | 2.97 | 1598 |
| 2024-09-20 22:21:41.248 | MS1 | 121.4656612439 | 31.1446350695 | 504 | 504990 | -89.71 | 17.25 | 478.20 | 0.12 | 2.47 | 1586 |
| 2024-09-20 22:21:42.748 | MS1 | 121.4656594042 | 31.1446234610 | 504 | 504990 | -89.45 | 15.58 | 523.36 | 0.15 | 2.77 | 1568 |

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
| 3232455 | 1 | 121.4749886081 | 31.1442162251 | 298 | 9 | 12 | 35.0 | TDD | 504 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3263386 | 3 | 121.4731643477 | 31.1505511455 | 179 | 0 | 12 | 15.4 | TDD | 468 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3263451 | 2 | 121.4717256315 | 31.1460043610 | 72 | 5 | 7 | 17.6 | TDD | 801 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3276388 | 4 | 121.4647585163 | 31.1464093244 | 10 | 5 | 12 | 19.4 | TDD | 180 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.798 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.818 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.937 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.937 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.110 | NREventA2 | measId:1;ServCellPCI:295;Se... |
| 2024-09-20 22:21:34.241 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232455 | 1 | 18.3449 | 15.4769 | -114.4440 | 17.2050 | 93.0533 | 0.1603 | 0.0012 |
| 2024_09_20 22:00 | 3263451 | 2 | 17.3188 | 7.7371 | -114.5942 | 15.0150 | 108.1633 | 0.0011 | 0.0171 |
| 2024_09_20 22:00 | 3263386 | 3 | 12.7249 | 17.4765 | -117.1746 | 8.5143 | 183.4684 | 0.0015 | 0.0024 |
| 2024_09_20 22:00 | 3276388 | 4 | 18.6780 | 5.0413 | -115.8742 | 8.0718 | 159.4475 | 0.0053 | 0.0113 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414392_9C35B08C | 504990 | 504 | -108.3 | 504990 | 468 | -112.7 | 504990 | 801 | -117.8 | 504990 | 180 |
| MR_1774414392_40302F07 | 504990 | 504 | -107.3 | 504990 | 468 | -112.7 | 504990 | 801 | -120.0 | 504990 | 180 |
| MR_1774414392_E0435551 | 504990 | 504 | -106.9 | 504990 | 468 | -112.3 | 504990 | 801 | -117.1 | 504990 | 180 |
| MR_1774414392_AE70E5E4 | 504990 | 504 | -107.2 | 504990 | 468 | -113.0 | 504990 | 801 | -118.4 | 504990 | 180 |
| MR_1774414392_5240EDE1 | 504990 | 504 | -108.2 | 504990 | 468 | -112.4 | 504990 | 801 | -119.1 | 504990 | 180 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1146: `dbf92c4d-da5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dbf92c4d-da55-41f2-a142-8c9bac83e31f` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Add neighbor relationship between 3253594_3 and 3257859_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1146] topology](images/train_1146.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3257859_4
- `C2`: Increase transmission power for 3253594_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253594_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257859_4
- `C5`: Press down the tilt angle  of 3257859_4 by 5 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Lift the tilt angle of 3253594_3 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3253594_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253594_3
- `C10`: Check test server and transmission issues
- `C11`: Increase transmission power for 3257859_4
- `C12`: Adjust the azimuth of 3257859_4 by 8 degrees
- `C13`: Decrease transmission power for 3253594_3
- `C14`: Add neighbor relationship between 3270047_1 and 3257859_4
- `C15`: Decrease transmission power for 3257859_4
- `C16`: Lift the tilt angle  of 3257859_4 by 5 degrees
- `C17`: Increase A3 Offset threshold for 3253594_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257859_4
- `C19`: Decrease A3 Offset threshold for 3257859_4
- `C20`: Add neighbor relationship between 3253594_3 and 3257859_4 **← 정답**
- `C21`: Press down the tilt angle of 3253594_3 by 10 degrees
- `C22`: Adjust the azimuth of 3253594_3 by 49 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.113 | MS1 | 121.4656665189 | 31.1446224016 | 805 | 504990 | -84.38 | 14.31 | 390.86 | 0.08 | 2.40 | 1590 |
| 2024-09-20 22:21:32.918 | MS1 | 121.4656629477 | 31.1446260161 | 805 | 504990 | -77.12 | 12.65 | 382.46 | 0.01 | 2.56 | 1595 |
| 2024-09-20 22:21:33.112 | MS1 | 121.4656719054 | 31.1446251005 | 805 | 504990 | -80.65 | 14.55 | 416.10 | 0.02 | 2.07 | 1560 |
| 2024-09-20 22:21:34.862 | MS1 | 121.4656609005 | 31.1446282879 | 805 | 504990 | -86.30 | -0.39 | 56.46 | 0.08 | 1.18 | 1588 |
| 2024-09-20 22:21:35.290 | MS1 | 121.4656770363 | 31.1446224044 | 805 | 504990 | -91.00 | -1.69 | 52.76 | 0.20 | 1.36 | 1585 |
| 2024-09-20 22:21:36.365 | MS1 | 121.4656766739 | 31.1446206684 | 805 | 504990 | -86.29 | -2.54 | 43.43 | 0.02 | 1.15 | 1583 |
| 2024-09-20 22:21:37.266 | MS1 | 121.4656753325 | 31.1446215200 | 805 | 504990 | -91.65 | -2.03 | 67.80 | 0.11 | 1.30 | 1560 |
| 2024-09-20 22:21:38.811 | MS1 | 121.4656728191 | 31.1446241202 | 805 | 504990 | -80.86 | 13.77 | 394.12 | 0.02 | 1.05 | 1568 |
| 2024-09-20 22:21:39.465 | MS1 | 121.4656730770 | 31.1446330190 | 805 | 504990 | -76.77 | 15.50 | 416.21 | 0.18 | 1.04 | 1571 |
| 2024-09-20 22:21:40.281 | MS1 | 121.4656760984 | 31.1446192643 | 805 | 504990 | -79.52 | 13.53 | 516.51 | 0.03 | 2.43 | 1595 |
| 2024-09-20 22:21:41.764 | MS1 | 121.4656667979 | 31.1446205178 | 805 | 504990 | -78.82 | 17.85 | 421.38 | 0.18 | 2.09 | 1578 |
| 2024-09-20 22:21:42.823 | MS1 | 121.4656752487 | 31.1446233549 | 805 | 504990 | -80.06 | 17.40 | 438.66 | 0.07 | 2.48 | 1562 |

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
| 3215670 | 2 | 121.4692382469 | 31.1529075023 | 309 | 0 | 8 | 21.2 | TDD | 10 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3253594 | 3 | 121.4710378113 | 31.1474798609 | 189 | 15 | 1 | 40.4 | TDD | 805 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3257859 | 4 | 121.4705617965 | 31.1460487305 | 259 | 2 | 1 | 25.8 | TDD | 358 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3270047 | 1 | 121.4669814151 | 31.1449916297 | 341 | 2 | 3 | 31.0 | TDD | 584 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.880 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.905 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.051 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.051 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.775 | NREventA3 | measId:2;ServCellPCI:11;Ser... |
| 2024-09-20 22:21:35.775 | NREventA3 | measId:2;ServCellPCI:11;Ser... |
| 2024-09-20 22:21:36.775 | NREventA3 | measId:2;ServCellPCI:11;Ser... |
| 2024-09-20 22:21:39.275 | NRRRCReestablishAttempt | PCI:11 |
| 2024-09-20 22:21:39.286 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.300 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.420 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.420 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270047 | 1 | 16.3845 | 12.9854 | -117.8286 | 18.0212 | 190.0496 | 0.0120 | 0.0011 |
| 2024_09_20 22:00 | 3215670 | 2 | 16.0760 | 12.8791 | -116.3244 | 18.1294 | 141.0297 | 0.0059 | 0.0142 |
| 2024_09_20 22:00 | 3253594 | 3 | 16.9980 | 14.3933 | -114.9803 | 19.2405 | 162.6944 | 0.0016 | 0.1532 |
| 2024_09_20 22:00 | 3257859 | 4 | 15.7537 | 6.0469 | -117.5938 | 11.5306 | 105.8898 | 0.0107 | 0.0096 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413656_85F49E25 | 504990 | 358 | -80.7 | 504990 | 805 | -84.9 | 504990 | 584 | -84.6 | 504990 | 10 |
| MR_1774413656_950E1565 | 504990 | 805 | -86.2 | 504990 | 358 | -80.1 | 504990 | 584 | -87.2 | 504990 | 10 |
| MR_1774413656_44FD1D61 | 504990 | 358 | -81.2 | 504990 | 805 | -85.0 | 504990 | 584 | -84.8 | 504990 | 10 |
| MR_1774413656_F486DB87 | 504990 | 805 | -88.3 | 504990 | 358 | -80.7 | 504990 | 584 | -86.3 | 504990 | 10 |
| MR_1774413656_95105A07 | 504990 | 805 | -85.5 | 504990 | 358 | -83.0 | 504990 | 584 | -85.9 | 504990 | 10 |
| MR_1774413656_699DB5DA | 504990 | 358 | -80.8 | 504990 | 805 | -84.8 | 504990 | 584 | -83.5 | 504990 | 10 |
| MR_1774413656_BCCE9AC0 | 504990 | 805 | -87.0 | 504990 | 358 | -80.2 | 504990 | 584 | -87.1 | 504990 | 10 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1147: `d50c0c8f-b24...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d50c0c8f-b245-4a15-977a-820e55744156` |
| Tag | **multiple-answer** |
| 정답 | **C6|C20** |
| C6 의미 | Increase transmission power for 3221114_1 |
| C20 의미 | Adjust the azimuth of 3221114_1 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1147] topology](images/train_1147.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3249419_4 by 7 degrees
- `C2`: Lift the tilt angle  of 3249419_4 by 4 degrees
- `C3`: Increase A3 Offset threshold for 3221114_1
- `C4`: Decrease transmission power for 3221114_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249419_4
- `C6`: Increase transmission power for 3221114_1 **← 정답**
- `C7`: Add neighbor relationship between 3267156_3 and 3249419_4
- `C8`: Check test server and transmission issues
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249419_4
- `C10`: Decrease transmission power for 3249419_4
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Press down the tilt angle  of 3249419_4 by 4 degrees
- `C13`: Lift the tilt angle of 3221114_1 by 10 degrees
- `C14`: Increase transmission power for 3249419_4
- `C15`: Press down the tilt angle of 3221114_1 by 10 degrees
- `C16`: Add neighbor relationship between 3221114_1 and 3249419_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221114_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221114_1
- `C19`: Decrease A3 Offset threshold for 3249419_4
- `C20`: Adjust the azimuth of 3221114_1 by 50 degrees **← 정답**
- `C21`: Increase A3 Offset threshold for 3249419_4
- `C22`: Decrease A3 Offset threshold for 3221114_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.382 | MS1 | 121.4656583669 | 31.1446363480 | 544 | 504990 | -92.56 | 12.89 | 555.36 | 0.01 | 2.07 | 1566 |
| 2024-09-20 22:21:32.919 | MS1 | 121.4656645424 | 31.1446317117 | 544 | 504990 | -89.80 | 12.58 | 567.32 | 0.17 | 2.76 | 1579 |
| 2024-09-20 22:21:33.508 | MS1 | 121.4656766857 | 31.1446201441 | 544 | 504990 | -90.46 | 17.95 | 561.99 | 0.13 | 2.11 | 1563 |
| 2024-09-20 22:21:34.726 | MS1 | 121.4656756154 | 31.1446221881 | 544 | 504990 | -100.93 | -1.87 | 40.05 | 0.04 | 1.30 | 1562 |
| 2024-09-20 22:21:35.576 | MS1 | 121.4656682071 | 31.1446180702 | 544 | 504990 | -101.62 | -1.61 | 40.25 | 0.06 | 1.43 | 1565 |
| 2024-09-20 22:21:36.657 | MS1 | 121.4656764788 | 31.1446242397 | 544 | 504990 | -103.52 | -0.66 | 82.76 | 0.13 | 1.48 | 1565 |
| 2024-09-20 22:21:37.590 | MS1 | 121.4656736450 | 31.1446251595 | 544 | 504990 | -109.93 | -0.24 | 50.34 | 0.03 | 1.03 | 1560 |
| 2024-09-20 22:21:38.449 | MS1 | 121.4656712061 | 31.1446323053 | 544 | 504990 | -102.59 | -1.50 | 20.48 | 0.11 | 1.31 | 1572 |
| 2024-09-20 22:21:39.310 | MS1 | 121.4656775999 | 31.1446375237 | 544 | 504990 | -106.96 | -0.45 | 17.58 | 0.09 | 1.02 | 1566 |
| 2024-09-20 22:21:40.238 | MS1 | 121.4656617910 | 31.1446219840 | 544 | 504990 | -86.98 | 13.13 | 316.60 | 0.09 | 2.48 | 1562 |
| 2024-09-20 22:21:41.494 | MS1 | 121.4656581599 | 31.1446273742 | 544 | 504990 | -94.19 | 16.45 | 491.77 | 0.06 | 2.36 | 1592 |
| 2024-09-20 22:21:42.550 | MS1 | 121.4656748310 | 31.1446369100 | 544 | 504990 | -90.71 | 16.20 | 570.44 | 0.13 | 2.85 | 1573 |

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
| 3221114 | 1 | 121.4670590286 | 31.1469423456 | 154 | 6 | 12 | 28.1 | TDD | 544 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3249419 | 4 | 121.4731195499 | 31.1553857692 | 204 | 3 | 11 | 30.2 | TDD | 87 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3264579 | 2 | 121.4710010867 | 31.1498254420 | 170 | 13 | 0 | 44.2 | TDD | 51 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3267156 | 3 | 121.4658483411 | 31.1536396969 | 0 | 15 | 3 | 35.0 | TDD | 96 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.441 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.465 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.567 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.567 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.785 | NREventA2 | measId:1;ServCellPCI:910;Se... |
| 2024-09-20 22:21:34.907 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221114 | 1 | 7.3239 | 14.3939 | -117.1688 | 8.1476 | 186.0215 | 0.1163 | 0.0163 |
| 2024_09_20 22:00 | 3264579 | 2 | 12.0482 | 13.9899 | -117.3007 | 12.0047 | 131.6280 | 0.0057 | 0.0067 |
| 2024_09_20 22:00 | 3267156 | 3 | 18.3239 | 12.0123 | -114.5095 | 9.6178 | 121.3924 | 0.0082 | 0.0052 |
| 2024_09_20 22:00 | 3249419 | 4 | 17.1207 | 16.6650 | -114.9782 | 15.8778 | 153.1025 | 0.0060 | 0.0183 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415217_B454FB34 | 504990 | 544 | -100.8 | 504990 | 87 | -110.5 | 504990 | 96 | -114.2 | 504990 | 51 |
| MR_1774415217_E1447E4B | 504990 | 544 | -101.0 | 504990 | 87 | -109.2 | 504990 | 96 | -115.2 | 504990 | 51 |
| MR_1774415217_97D7F471 | 504990 | 544 | -101.3 | 504990 | 87 | -107.3 | 504990 | 96 | -113.6 | 504990 | 51 |
| MR_1774415217_88AE3ED6 | 504990 | 544 | -102.2 | 504990 | 87 | -109.1 | 504990 | 96 | -115.4 | 504990 | 51 |
| MR_1774415217_99EB0438 | 504990 | 544 | -102.9 | 504990 | 87 | -110.2 | 504990 | 96 | -114.1 | 504990 | 51 |
| MR_1774415217_EE3C6EEC | 504990 | 544 | -100.8 | 504990 | 87 | -109.3 | 504990 | 96 | -115.2 | 504990 | 51 |
| MR_1774415217_F88A515A | 504990 | 544 | -100.9 | 504990 | 87 | -109.4 | 504990 | 96 | -113.9 | 504990 | 51 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1148: `2ba7f60f-a34...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2ba7f60f-a34f-48b6-be3e-a5f7a06f4c89` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3263588_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1148] topology](images/train_1148.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3243511_1
- `C2`: Decrease transmission power for 3243511_1
- `C3`: Increase transmission power for 3263588_4
- `C4`: Increase A3 Offset threshold for 3243511_1
- `C5`: Add neighbor relationship between 3225607_3 and 3243511_1
- `C6`: Increase A3 Offset threshold for 3263588_4
- `C7`: Press down the tilt angle of 3263588_4 by 5 degrees
- `C8`: Lift the tilt angle  of 3243511_1 by 10 degrees
- `C9`: Add neighbor relationship between 3263588_4 and 3243511_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243511_1
- `C11`: Decrease transmission power for 3263588_4
- `C12`: Press down the tilt angle  of 3243511_1 by 10 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263588_4 **← 정답**
- `C14`: Decrease A3 Offset threshold for 3263588_4
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Adjust the azimuth of 3243511_1 by 50 degrees
- `C17`: Check test server and transmission issues
- `C18`: Lift the tilt angle of 3263588_4 by 5 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263588_4
- `C20`: Decrease A3 Offset threshold for 3243511_1
- `C21`: Adjust the azimuth of 3263588_4 by 33 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243511_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.868 | MS1 | 121.4656761874 | 31.1446351997 | 323 | 504990 | -90.33 | 13.33 | 369.82 | 0.13 | 2.09 | 1589 |
| 2024-09-20 22:21:32.916 | MS1 | 121.4656649238 | 31.1446215466 | 323 | 504990 | -90.72 | 16.94 | 391.76 | 0.13 | 2.16 | 1571 |
| 2024-09-20 22:21:33.632 | MS1 | 121.4656672451 | 31.1446201280 | 323 | 504990 | -87.54 | 12.74 | 424.50 | 0.14 | 2.99 | 1575 |
| 2024-09-20 22:21:34.262 | MS1 | 121.4656594690 | 31.1446255733 | 323 | 504990 | -87.92 | 16.38 | 85.29 | 0.53 | 2.87 | 556 |
| 2024-09-20 22:21:35.102 | MS1 | 121.4656737748 | 31.1446276617 | 323 | 504990 | -91.85 | 15.38 | 73.39 | 0.60 | 2.03 | 523 |
| 2024-09-20 22:21:36.769 | MS1 | 121.4656718849 | 31.1446309754 | 323 | 504990 | -85.62 | 13.80 | 64.17 | 0.59 | 2.67 | 534 |
| 2024-09-20 22:21:37.402 | MS1 | 121.4656731847 | 31.1446276272 | 323 | 504990 | -93.07 | 12.99 | 88.07 | 0.69 | 2.31 | 649 |
| 2024-09-20 22:21:38.701 | MS1 | 121.4656669090 | 31.1446245693 | 323 | 504990 | -92.00 | 8.88 | 71.88 | 0.51 | 2.66 | 626 |
| 2024-09-20 22:21:39.820 | MS1 | 121.4656703243 | 31.1446201590 | 323 | 504990 | -91.40 | 7.46 | 75.99 | 0.63 | 2.96 | 610 |
| 2024-09-20 22:21:40.603 | MS1 | 121.4656657784 | 31.1446270674 | 323 | 504990 | -92.05 | 10.12 | 547.61 | 0.08 | 2.29 | 1571 |
| 2024-09-20 22:21:41.822 | MS1 | 121.4656693727 | 31.1446292916 | 323 | 504990 | -90.72 | 8.94 | 558.10 | 0.12 | 2.72 | 1579 |
| 2024-09-20 22:21:42.451 | MS1 | 121.4656683470 | 31.1446224310 | 323 | 504990 | -90.22 | 11.04 | 344.79 | 0.04 | 2.12 | 1577 |

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
| 3225607 | 3 | 121.4755632142 | 31.1447733679 | 148 | 11 | 4 | 26.3 | TDD | 626 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3243511 | 1 | 121.4681751707 | 31.1496975710 | 148 | 14 | 5 | 21.2 | TDD | 232 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3254722 | 2 | 121.4657197388 | 31.1442764440 | 113 | 0 | 9 | 28.0 | TDD | 609 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3263588 | 4 | 121.4744704751 | 31.1484915400 | 276 | 3 | 1 | 27.2 | TDD | 323 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.134 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.149 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.269 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.269 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.961 | NREventA3 | measId:2;ServCellPCI:348;Se... |
| 2024-09-20 22:21:38.201 | NRHandoverAttempt | SourcePCI:348;SourceNR-ARFC... |
| 2024-09-20 22:21:38.244 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.254 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.390 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.390 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243511 | 1 | 15.6382 | 5.2222 | -114.6652 | 19.9252 | 190.1929 | 0.0082 | 0.0178 |
| 2024_09_20 22:00 | 3254722 | 2 | 5.1895 | 14.6906 | -117.9593 | 18.4671 | 95.5838 | 0.0069 | 0.0067 |
| 2024_09_20 22:00 | 3225607 | 3 | 8.4967 | 14.9055 | -117.4869 | 13.5928 | 178.2953 | 0.0156 | 0.0135 |
| 2024_09_20 22:00 | 3263588 | 4 | 12.7290 | 13.2746 | -115.2626 | 11.1615 | 166.3371 | 0.0106 | 0.0154 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414333_96E63222 | 504990 | 323 | -88.6 | 504990 | 232 | -94.1 | 504990 | 626 | -96.0 | 504990 | 609 |
| MR_1774414333_7A50332D | 504990 | 323 | -89.6 | 504990 | 232 | -94.1 | 504990 | 626 | -94.7 | 504990 | 609 |
| MR_1774414333_EDC214BC | 504990 | 323 | -86.4 | 504990 | 232 | -90.5 | 504990 | 626 | -94.8 | 504990 | 609 |
| MR_1774414333_8EA69209 | 504990 | 323 | -88.0 | 504990 | 232 | -90.9 | 504990 | 626 | -97.1 | 504990 | 609 |
| MR_1774414333_7C3D4902 | 504990 | 323 | -88.1 | 504990 | 232 | -92.0 | 504990 | 626 | -94.0 | 504990 | 609 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1149: `68c16290-7cc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `68c16290-7cc6-408f-9076-527f7a57731d` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3275912_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1149] topology](images/train_1149.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3275912_1
- `C2`: Lift the tilt angle  of 3255727_3 by 10 degrees
- `C3`: Add neighbor relationship between 3275912_1 and 3255727_3
- `C4`: Decrease A3 Offset threshold for 3255727_3
- `C5`: Press down the tilt angle of 3275912_1 by 4 degrees
- `C6`: Increase A3 Offset threshold for 3255727_3
- `C7`: Adjust the azimuth of 3275912_1 by 24 degrees
- `C8`: Press down the tilt angle  of 3255727_3 by 10 degrees
- `C9`: Decrease transmission power for 3255727_3
- `C10`: Increase transmission power for 3255727_3
- `C11`: Adjust the azimuth of 3255727_3 by 50 degrees
- `C12`: Increase A3 Offset threshold for 3275912_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255727_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275912_1
- `C15`: Increase transmission power for 3275912_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275912_1 **← 정답**
- `C17`: Add neighbor relationship between 3240405_2 and 3255727_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255727_3
- `C19`: Lift the tilt angle of 3275912_1 by 4 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Check test server and transmission issues
- `C22`: Decrease A3 Offset threshold for 3275912_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.256 | MS1 | 121.4656745345 | 31.1446271238 | 873 | 504990 | -90.93 | 16.05 | 422.00 | 0.15 | 2.64 | 1589 |
| 2024-09-20 22:21:32.224 | MS1 | 121.4656675648 | 31.1446311983 | 873 | 504990 | -85.52 | 12.40 | 406.10 | 0.11 | 2.70 | 1586 |
| 2024-09-20 22:21:33.217 | MS1 | 121.4656619436 | 31.1446346631 | 873 | 504990 | -89.87 | 15.31 | 410.97 | 0.15 | 2.23 | 1568 |
| 2024-09-20 22:21:34.234 | MS1 | 121.4656685523 | 31.1446276964 | 873 | 504990 | -88.08 | 17.66 | 52.83 | 0.54 | 2.98 | 548 |
| 2024-09-20 22:21:35.512 | MS1 | 121.4656752773 | 31.1446372442 | 873 | 504990 | -87.98 | 16.02 | 81.49 | 0.57 | 2.38 | 634 |
| 2024-09-20 22:21:36.210 | MS1 | 121.4656673900 | 31.1446220546 | 873 | 504990 | -90.40 | 17.33 | 80.47 | 0.56 | 2.19 | 695 |
| 2024-09-20 22:21:37.964 | MS1 | 121.4656683568 | 31.1446215426 | 873 | 504990 | -93.80 | 11.74 | 92.23 | 0.63 | 2.47 | 531 |
| 2024-09-20 22:21:38.136 | MS1 | 121.4656699396 | 31.1446191634 | 873 | 504990 | -90.83 | 9.30 | 51.08 | 0.53 | 2.20 | 694 |
| 2024-09-20 22:21:39.476 | MS1 | 121.4656750465 | 31.1446314115 | 873 | 504990 | -91.10 | 10.00 | 92.44 | 0.60 | 2.35 | 665 |
| 2024-09-20 22:21:40.191 | MS1 | 121.4656706289 | 31.1446362738 | 873 | 504990 | -93.21 | 12.52 | 543.74 | 0.00 | 2.40 | 1585 |
| 2024-09-20 22:21:41.790 | MS1 | 121.4656644328 | 31.1446299900 | 873 | 504990 | -91.22 | 10.98 | 431.11 | 0.04 | 2.46 | 1574 |
| 2024-09-20 22:21:42.937 | MS1 | 121.4656759304 | 31.1446321315 | 873 | 504990 | -91.95 | 12.14 | 401.61 | 0.14 | 2.16 | 1598 |

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
| 3240405 | 2 | 121.4658124303 | 31.1473428659 | 131 | 3 | 5 | 43.3 | TDD | 788 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3247446 | 4 | 121.4712009577 | 31.1444533052 | 122 | 1 | 7 | 26.2 | TDD | 159 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3255727 | 3 | 121.4651495132 | 31.1441798492 | 107 | 1 | 2 | 21.6 | TDD | 573 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3275912 | 1 | 121.4728461002 | 31.1518975726 | 196 | 3 | 8 | 25.4 | TDD | 873 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.293 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.308 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.434 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.434 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.139 | NREventA3 | measId:2;ServCellPCI:468;Se... |
| 2024-09-20 22:21:38.379 | NRHandoverAttempt | SourcePCI:468;SourceNR-ARFC... |
| 2024-09-20 22:21:38.411 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.423 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.543 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.543 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275912 | 1 | 17.7924 | 7.5594 | -115.7460 | 6.9639 | 183.3150 | 0.0018 | 0.0052 |
| 2024_09_20 22:00 | 3240405 | 2 | 16.2523 | 11.4952 | -117.7060 | 16.6957 | 114.0624 | 0.0144 | 0.0131 |
| 2024_09_20 22:00 | 3255727 | 3 | 18.7695 | 15.5503 | -116.3050 | 16.7884 | 100.1653 | 0.0193 | 0.0143 |
| 2024_09_20 22:00 | 3247446 | 4 | 17.3598 | 18.2621 | -117.9273 | 15.4042 | 195.7164 | 0.0151 | 0.0067 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416120_18C088E1 | 504990 | 873 | -87.3 | 504990 | 573 | -87.5 | 504990 | 788 | -94.9 | 504990 | 159 |
| MR_1774416120_A22E76D8 | 504990 | 873 | -86.2 | 504990 | 573 | -90.0 | 504990 | 788 | -95.9 | 504990 | 159 |
| MR_1774416120_66734992 | 504990 | 873 | -88.8 | 504990 | 573 | -87.2 | 504990 | 788 | -95.2 | 504990 | 159 |
| MR_1774416120_E7C0F66C | 504990 | 873 | -88.8 | 504990 | 573 | -90.0 | 504990 | 788 | -93.7 | 504990 | 159 |
| MR_1774416120_FA5FE8C1 | 504990 | 873 | -86.2 | 504990 | 573 | -87.7 | 504990 | 788 | -96.3 | 504990 | 159 |
| MR_1774416120_D6F74C50 | 504990 | 873 | -87.5 | 504990 | 573 | -87.7 | 504990 | 788 | -96.4 | 504990 | 159 |
| MR_1774416120_8A19FE26 | 504990 | 873 | -88.6 | 504990 | 573 | -86.8 | 504990 | 788 | -95.8 | 504990 | 159 |

> *... 2개 열 생략 (전체 14열)*

---
