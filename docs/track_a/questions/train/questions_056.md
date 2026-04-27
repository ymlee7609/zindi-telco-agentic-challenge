# Track A 문제 분석 — train[550]~train[559]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[550] ~ train[559] (10개)

## 목차

1. [문제 550: `d1dfdc2a-afb...`](#550) — multiple-answer, 정답: C15|C21
2. [문제 551: `b2cc52a6-665...`](#551) — single-answer, 정답: C22
3. [문제 552: `0433ecdb-346...`](#552) — single-answer, 정답: C22
4. [문제 553: `5f852fa4-a39...`](#553) — single-answer, 정답: C17
5. [문제 554: `cd145796-c30...`](#554) — single-answer, 정답: C2
6. [문제 555: `75675c0d-105...`](#555) — single-answer, 정답: C20
7. [문제 556: `35cab5e0-a9b...`](#556) — single-answer, 정답: C16
8. [문제 557: `a33f37f6-a97...`](#557) — single-answer, 정답: C19
9. [문제 558: `0b316bf5-28c...`](#558) — single-answer, 정답: C3
10. [문제 559: `0936e665-8c4...`](#559) — single-answer, 정답: C8

---

### 문제 550: `d1dfdc2a-afb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d1dfdc2a-afb6-4650-a86b-1553a2b7ae6f` |
| Tag | **multiple-answer** |
| 정답 | **C15|C21** |
| C15 의미 | Press down the tilt angle  of 3248493_2 by 4 degrees |
| C21 의미 | Decrease transmission power for 3248493_2 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[550] topology](images/train_0550.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3221455_1
- `C2`: Increase transmission power for 3221455_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221455_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248493_2
- `C5`: Decrease A3 Offset threshold for 3248493_2
- `C6`: Increase A3 Offset threshold for 3221455_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248493_2
- `C8`: Add neighbor relationship between 3273568_3 and 3248493_2
- `C9`: Press down the tilt angle of 3221455_1 by 2 degrees
- `C10`: Lift the tilt angle of 3221455_1 by 2 degrees
- `C11`: Adjust the azimuth of 3221455_1 by 31 degrees
- `C12`: Lift the tilt angle  of 3248493_2 by 4 degrees
- `C13`: Add neighbor relationship between 3221455_1 and 3248493_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221455_1
- `C15`: Press down the tilt angle  of 3248493_2 by 4 degrees **← 정답**
- `C16`: Increase transmission power for 3248493_2
- `C17`: Adjust the azimuth of 3248493_2 by 11 degrees
- `C18`: Check test server and transmission issues
- `C19`: Increase A3 Offset threshold for 3248493_2
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease transmission power for 3248493_2 **← 정답**
- `C22`: Decrease transmission power for 3221455_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.540 | MS1 | 121.4656770424 | 31.1446220205 | 636 | 504990 | -81.31 | 14.28 | 382.39 | 0.14 | 2.17 | 1566 |
| 2024-09-20 22:21:32.589 | MS1 | 121.4656608310 | 31.1446376547 | 636 | 504990 | -80.76 | 15.47 | 473.49 | 0.08 | 2.86 | 1570 |
| 2024-09-20 22:21:33.179 | MS1 | 121.4656629929 | 31.1446213872 | 636 | 504990 | -84.54 | 13.64 | 366.21 | 0.04 | 2.89 | 1581 |
| 2024-09-20 22:21:34.492 | MS1 | 121.4656696320 | 31.1446250895 | 636 | 504990 | -90.37 | 2.40 | 66.10 | 0.10 | 1.02 | 1564 |
| 2024-09-20 22:21:35.380 | MS1 | 121.4656667134 | 31.1446227784 | 636 | 504990 | -93.24 | 2.37 | 53.17 | 0.02 | 1.14 | 1581 |
| 2024-09-20 22:21:36.718 | MS1 | 121.4656771669 | 31.1446305606 | 636 | 504990 | -85.58 | 3.83 | 84.80 | 0.03 | 1.41 | 1596 |
| 2024-09-20 22:21:37.496 | MS1 | 121.4656649690 | 31.1446345274 | 636 | 504990 | -85.44 | 0.88 | 73.31 | 0.10 | 1.34 | 1560 |
| 2024-09-20 22:21:38.575 | MS1 | 121.4656682248 | 31.1446275964 | 636 | 504990 | -88.40 | 2.89 | 67.25 | 0.01 | 1.49 | 1565 |
| 2024-09-20 22:21:39.858 | MS1 | 121.4656707952 | 31.1446184332 | 636 | 504990 | -89.37 | 0.95 | 64.23 | 0.17 | 1.46 | 1579 |
| 2024-09-20 22:21:40.774 | MS1 | 121.4656696528 | 31.1446267436 | 636 | 504990 | -75.40 | 13.60 | 483.28 | 0.10 | 2.95 | 1578 |
| 2024-09-20 22:21:41.158 | MS1 | 121.4656763085 | 31.1446203494 | 636 | 504990 | -78.55 | 14.24 | 556.40 | 0.07 | 2.51 | 1561 |
| 2024-09-20 22:21:42.204 | MS1 | 121.4656702425 | 31.1446261357 | 636 | 504990 | -75.15 | 17.62 | 302.63 | 0.02 | 2.30 | 1570 |

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
| 3216201 | 4 | 121.4737110322 | 31.1472117576 | 354 | 8 | 7 | 39.1 | TDD | 124 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3221455 | 1 | 121.4717554130 | 31.1559406980 | 174 | 0 | 12 | 40.9 | TDD | 636 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3248493 | 2 | 121.4740516630 | 31.1464659193 | 245 | 1 | 5 | 38.6 | TDD | 858 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3273568 | 3 | 121.4675499682 | 31.1515582364 | 123 | 13 | 1 | 23.8 | TDD | 347 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.732 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.749 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.888 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.888 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221455 | 1 | 13.2676 | 15.7841 | -108.8979 | 16.4145 | 154.0203 | 0.0127 | 0.0010 |
| 2024_09_20 22:00 | 3248493 | 2 | 10.5946 | 10.9064 | -114.2406 | 14.5807 | 93.2388 | 0.0093 | 0.0104 |
| 2024_09_20 22:00 | 3273568 | 3 | 16.2363 | 18.8294 | -115.1454 | 11.9578 | 139.7607 | 0.0042 | 0.0087 |
| 2024_09_20 22:00 | 3216201 | 4 | 19.3416 | 16.3899 | -116.8062 | 11.8733 | 130.7153 | 0.0002 | 0.0058 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414038_8B26AFB4 | 504990 | 636 | -91.6 | 504990 | 858 | -90.4 | 504990 | 347 | -91.2 | 504990 | 124 |
| MR_1774414038_C510ECBD | 504990 | 858 | -89.6 | 504990 | 636 | -86.8 | 504990 | 347 | -89.6 | 504990 | 124 |
| MR_1774414038_F7CEB19A | 504990 | 636 | -90.5 | 504990 | 858 | -90.2 | 504990 | 347 | -92.3 | 504990 | 124 |
| MR_1774414038_65AAAD6B | 504990 | 858 | -88.8 | 504990 | 636 | -88.2 | 504990 | 347 | -89.3 | 504990 | 124 |
| MR_1774414038_CE7C72F9 | 504990 | 858 | -90.2 | 504990 | 636 | -89.3 | 504990 | 347 | -91.6 | 504990 | 124 |
| MR_1774414038_334C017A | 504990 | 858 | -88.4 | 504990 | 636 | -89.8 | 504990 | 347 | -89.3 | 504990 | 124 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 551: `b2cc52a6-665...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b2cc52a6-6656-4014-9206-47e1eb4a7fd9` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238276_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[551] topology](images/train_0551.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3238276_1 by 4 degrees
- `C2`: Press down the tilt angle  of 3251495_3 by 6 degrees
- `C3`: Add neighbor relationship between 3262633_9 and 3251495_3
- `C4`: Lift the tilt angle  of 3251495_3 by 6 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238276_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251495_3
- `C7`: Adjust the azimuth of 3251495_3 by 4 degrees
- `C8`: Press down the tilt angle of 3238276_1 by 4 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251495_3
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase transmission power for 3251495_3
- `C12`: Decrease transmission power for 3238276_1
- `C13`: Add neighbor relationship between 3238276_1 and 3251495_3
- `C14`: Check test server and transmission issues
- `C15`: Increase A3 Offset threshold for 3238276_1
- `C16`: Decrease A3 Offset threshold for 3238276_1
- `C17`: Decrease A3 Offset threshold for 3251495_3
- `C18`: Adjust the azimuth of 3238276_1 by 5 degrees
- `C19`: Increase A3 Offset threshold for 3251495_3
- `C20`: Increase transmission power for 3238276_1
- `C21`: Decrease transmission power for 3251495_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238276_1 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.627 | MS1 | 121.4656706507 | 31.1446274636 | 588 | 504990 | -95.97 | 9.40 | 557.11 | 0.16 | 2.65 | 1578 |
| 2024-09-20 22:21:32.460 | MS1 | 121.4656695079 | 31.1446334015 | 283 | 504990 | -93.47 | 9.18 | 389.78 | 0.20 | 2.14 | 1590 |
| 2024-09-20 22:21:33.653 | MS1 | 121.4656600370 | 31.1446338373 | 533 | 504990 | -95.04 | 9.35 | 447.96 | 0.08 | 2.72 | 1575 |
| 2024-09-20 22:21:34.673 | MS1 | 121.4656761849 | 31.1446306279 | 465 | 152650 | -96.54 | 5.83 | 84.45 | 0.08 | 1.52 | 966 |
| 2024-09-20 22:21:35.696 | MS1 | 121.4656631140 | 31.1446371932 | 296 | 152650 | -88.26 | 3.25 | 91.11 | 0.02 | 1.93 | 993 |
| 2024-09-20 22:21:36.556 | MS1 | 121.4656682019 | 31.1446223479 | 358 | 152650 | -93.64 | 7.54 | 86.31 | 0.09 | 1.72 | 928 |
| 2024-09-20 22:21:37.914 | MS1 | 121.4656601246 | 31.1446205054 | 903 | 152650 | -88.80 | 6.87 | 66.15 | 0.10 | 1.97 | 986 |
| 2024-09-20 22:21:38.744 | MS1 | 121.4656733675 | 31.1446363173 | 465 | 152650 | -89.93 | 5.99 | 67.39 | 0.11 | 1.97 | 965 |
| 2024-09-20 22:21:39.749 | MS1 | 121.4656683364 | 31.1446378481 | 296 | 152650 | -89.74 | 3.10 | 99.36 | 0.11 | 1.51 | 977 |
| 2024-09-20 22:21:40.787 | MS1 | 121.4656699874 | 31.1446230540 | 358 | 152650 | -87.33 | 2.13 | 56.31 | 0.16 | 2.86 | 1596 |
| 2024-09-20 22:21:41.688 | MS1 | 121.4656650974 | 31.1446358086 | 903 | 152650 | -92.92 | 3.45 | 83.43 | 0.09 | 2.24 | 1569 |
| 2024-09-20 22:21:42.493 | MS1 | 121.4656647107 | 31.1446239002 | 465 | 152650 | -87.89 | 3.65 | 73.55 | 0.06 | 2.39 | 1585 |

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
| 3238276 | 1 | 121.4660551149 | 31.1545196145 | 177 | 3 | 12 | 20.5 | TDD | 588 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3240922 | 2 | 121.4705524842 | 31.1550704675 | 196 | 8 | 5 | 2.1 | TDD | 208 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3243914 | 13 | 121.4659338112 | 31.1552313082 | 351 | 15 | 2 | 4.6 | FDD | 118 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3247549 | 10 | 121.4750730983 | 31.1549859148 | 137 | 2 | 4 | 8.5 | FDD | 903 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3251495 | 3 | 121.4750390521 | 31.1506397769 | 229 | 5 | 7 | 12.3 | TDD | 884 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3255105 | 8 | 121.4646922931 | 31.1496495566 | 217 | 2 | 2 | 19.5 | FDD | 963 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3258587 | 7 | 121.4676864981 | 31.1504306811 | 352 | 1 | 11 | 10.6 | FDD | 160 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3262633 | 9 | 121.4659454549 | 31.1523929010 | 221 | 11 | 8 | 26.2 | FDD | 358 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3263849 | 6 | 121.4690103827 | 31.1521275885 | 13 | 13 | 10 | 7.2 | TDD | 283 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3264647 | 12 | 121.4653695618 | 31.1484777897 | 50 | 5 | 12 | 0.8 | FDD | 465 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3268235 | 5 | 121.4733320277 | 31.1543876276 | 156 | 1 | 2 | 13.7 | TDD | 437 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3271039 | 4 | 121.4681374620 | 31.1486573785 | 256 | 5 | 8 | 24.5 | TDD | 533 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3271929 | 11 | 121.4650405218 | 31.1442694673 | 128 | 11 | 8 | 16.8 | FDD | 296 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |

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
| 2024-09-20 22:21:31.427 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.449 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.587 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.587 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.243 | NREventA2 | measId:1;ServCellPCI:932;Se... |
| 2024-09-20 22:21:35.346 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.599 | NREventA5 | measId:3;ServCellPCI:932;Se... |
| 2024-09-20 22:21:35.668 | NRHandoverAttempt | SourcePCI:932;SourceNR-ARFC... |
| 2024-09-20 22:21:35.711 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.722 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.865 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.865 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238276 | 1 | 13.8114 | 7.1893 | -114.4698 | 14.0278 | 175.0572 | 0.0052 | 0.0165 |
| 2024_09_20 22:00 | 3240922 | 2 | 11.7055 | 18.8232 | -115.8623 | 16.5350 | 195.3672 | 0.0012 | 0.0125 |
| 2024_09_20 22:00 | 3251495 | 3 | 17.6240 | 7.2117 | -116.8277 | 14.5332 | 102.8152 | 0.0020 | 0.0188 |
| 2024_09_20 22:00 | 3271039 | 4 | 16.3138 | 15.3011 | -116.3605 | 7.9570 | 147.0694 | 0.0164 | 0.0061 |
| 2024_09_20 22:00 | 3268235 | 5 | 10.1387 | 5.3049 | -117.5991 | 5.8520 | 151.8690 | 0.0048 | 0.0143 |
| 2024_09_20 22:00 | 3263849 | 6 | 15.5543 | 19.5256 | -115.6710 | 6.9064 | 162.3440 | 0.0041 | 0.0122 |
| 2024_09_20 22:00 | 3258587 | 7 | 10.0049 | 11.8695 | -116.2029 | 4.2834 | 25.2846 | 0.0191 | 0.0058 |
| 2024_09_20 22:00 | 3255105 | 8 | 18.1118 | 5.5124 | -117.9858 | 3.6218 | 39.0619 | 0.0156 | 0.0016 |
| 2024_09_20 22:00 | 3262633 | 9 | 8.4933 | 15.3884 | -117.8159 | 3.2939 | 37.1630 | 0.0072 | 0.0122 |
| 2024_09_20 22:00 | 3247549 | 10 | 6.4303 | 17.9540 | -117.3988 | 3.0243 | 34.5988 | 0.0176 | 0.0031 |
| 2024_09_20 22:00 | 3271929 | 11 | 13.2894 | 14.7399 | -117.0086 | 3.0053 | 55.2061 | 0.0153 | 0.0178 |
| 2024_09_20 22:00 | 3264647 | 12 | 9.0276 | 10.1599 | -114.1911 | 4.5875 | 59.1339 | 0.0183 | 0.0168 |
| 2024_09_20 22:00 | 3243914 | 13 | 19.0186 | 7.1032 | -116.4542 | 4.3265 | 22.0370 | 0.0196 | 0.0085 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414412_6991DA54 | 504990 | 533 | -93.6 | 504990 | 884 | -88.9 | 504990 | 208 | -97.4 | 504990 | 437 |
| MR_1774414412_BF86A0C4 | 152650 | 465 | -94.9 | 152650 | 118 | -105.0 | 152650 | 963 | -107.2 | 152650 | 160 |
| MR_1774414412_1FD3E6FF | 152650 | 465 | -96.6 | 152650 | 118 | -101.7 | 152650 | 963 | -105.2 | 152650 | 160 |
| MR_1774414412_857EBDD7 | 152650 | 465 | -98.2 | 152650 | 118 | -102.2 | 152650 | 963 | -107.3 | 152650 | 160 |
| MR_1774414412_52787AF6 | 152650 | 465 | -95.9 | 152650 | 118 | -104.4 | 152650 | 963 | -104.8 | 152650 | 160 |
| MR_1774414412_42DBC366 | 504990 | 533 | -93.5 | 504990 | 884 | -90.4 | 504990 | 208 | -97.4 | 504990 | 437 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 552: `0433ecdb-346...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0433ecdb-3463-4c51-9133-ba2820cf6740` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226387_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[552] topology](images/train_0552.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3257978_13 and 3232082_6
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226387_5
- `C3`: Increase A3 Offset threshold for 3226387_5
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232082_6
- `C5`: Decrease transmission power for 3226387_5
- `C6`: Decrease A3 Offset threshold for 3232082_6
- `C7`: Decrease transmission power for 3232082_6
- `C8`: Add neighbor relationship between 3226387_5 and 3232082_6
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232082_6
- `C11`: Press down the tilt angle of 3226387_5 by 4 degrees
- `C12`: Adjust the azimuth of 3226387_5 by 14 degrees
- `C13`: Increase A3 Offset threshold for 3232082_6
- `C14`: Lift the tilt angle of 3226387_5 by 4 degrees
- `C15`: Press down the tilt angle  of 3232082_6 by 3 degrees
- `C16`: Check test server and transmission issues
- `C17`: Increase transmission power for 3232082_6
- `C18`: Increase transmission power for 3226387_5
- `C19`: Adjust the azimuth of 3232082_6 by 18 degrees
- `C20`: Lift the tilt angle  of 3232082_6 by 3 degrees
- `C21`: Decrease A3 Offset threshold for 3226387_5
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226387_5 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.884 | MS1 | 121.4656777538 | 31.1446221831 | 805 | 504990 | -94.81 | 14.60 | 545.21 | 0.07 | 2.68 | 1597 |
| 2024-09-20 22:21:32.988 | MS1 | 121.4656761849 | 31.1446278957 | 771 | 504990 | -95.97 | 12.06 | 376.08 | 0.07 | 2.18 | 1571 |
| 2024-09-20 22:21:33.605 | MS1 | 121.4656585382 | 31.1446291548 | 1 | 504990 | -93.36 | 12.95 | 558.21 | 0.05 | 2.29 | 1588 |
| 2024-09-20 22:21:34.429 | MS1 | 121.4656704683 | 31.1446247448 | 308 | 152650 | -88.61 | 7.87 | 79.48 | 0.20 | 1.66 | 970 |
| 2024-09-20 22:21:35.546 | MS1 | 121.4656690758 | 31.1446181461 | 379 | 152650 | -87.88 | 4.96 | 55.02 | 0.01 | 1.70 | 945 |
| 2024-09-20 22:21:36.162 | MS1 | 121.4656677440 | 31.1446330930 | 862 | 152650 | -94.72 | 4.40 | 53.89 | 0.04 | 1.97 | 920 |
| 2024-09-20 22:21:37.579 | MS1 | 121.4656705813 | 31.1446240457 | 384 | 152650 | -89.93 | 7.21 | 88.14 | 0.06 | 1.98 | 919 |
| 2024-09-20 22:21:38.299 | MS1 | 121.4656605589 | 31.1446185651 | 308 | 152650 | -91.74 | 5.51 | 74.16 | 0.15 | 1.88 | 937 |
| 2024-09-20 22:21:39.108 | MS1 | 121.4656771364 | 31.1446356285 | 379 | 152650 | -87.81 | 3.70 | 73.87 | 0.01 | 1.76 | 952 |
| 2024-09-20 22:21:40.317 | MS1 | 121.4656592191 | 31.1446291219 | 862 | 152650 | -92.87 | 7.80 | 88.95 | 0.09 | 2.70 | 1560 |
| 2024-09-20 22:21:41.133 | MS1 | 121.4656625818 | 31.1446260801 | 384 | 152650 | -88.30 | 7.59 | 68.53 | 0.11 | 2.85 | 1565 |
| 2024-09-20 22:21:42.536 | MS1 | 121.4656694390 | 31.1446346901 | 308 | 152650 | -94.56 | 7.36 | 81.43 | 0.07 | 2.37 | 1583 |

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
| 3226387 | 5 | 121.4732256518 | 31.1490479803 | 250 | 3 | 9 | 16.7 | TDD | 805 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3230046 | 9 | 121.4736102742 | 31.1500675572 | 166 | 8 | 3 | 3.6 | FDD | 234 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3231350 | 1 | 121.4684956671 | 31.1504984322 | 225 | 5 | 10 | 29.7 | TDD | 960 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3232082 | 6 | 121.4758801271 | 31.1480733058 | 267 | 2 | 3 | 17.2 | TDD | 696 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3240619 | 7 | 121.4734046093 | 31.1479985253 | 279 | 10 | 7 | 2.0 | FDD | 384 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3242519 | 2 | 121.4647944574 | 31.1514570165 | 30 | 11 | 10 | 7.4 | TDD | 1 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3246056 | 4 | 121.4751115275 | 31.1521345571 | 223 | 6 | 12 | 24.9 | TDD | 771 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3247084 | 10 | 121.4648600274 | 31.1542927991 | 172 | 6 | 10 | 11.0 | FDD | 308 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3247903 | 8 | 121.4728634922 | 31.1544029715 | 224 | 6 | 11 | 10.1 | FDD | 649 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3248641 | 12 | 121.4751064086 | 31.1495153462 | 205 | 8 | 12 | 12.2 | FDD | 379 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3257574 | 3 | 121.4696011740 | 31.1543478491 | 230 | 12 | 11 | 26.2 | TDD | 448 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3257978 | 13 | 121.4758628377 | 31.1462095137 | 348 | 6 | 0 | 7.8 | FDD | 862 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3259519 | 11 | 121.4650524733 | 31.1487711326 | 290 | 10 | 5 | 16.4 | FDD | 372 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |

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
| 2024-09-20 22:21:31.300 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.321 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.428 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.428 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.144 | NREventA2 | measId:1;ServCellPCI:474;Se... |
| 2024-09-20 22:21:35.285 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.550 | NREventA5 | measId:3;ServCellPCI:474;Se... |
| 2024-09-20 22:21:35.591 | NRHandoverAttempt | SourcePCI:474;SourceNR-ARFC... |
| 2024-09-20 22:21:35.627 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.638 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.756 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.756 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231350 | 1 | 19.2707 | 13.8800 | -116.3155 | 14.4181 | 159.1102 | 0.0143 | 0.0062 |
| 2024_09_20 22:00 | 3242519 | 2 | 15.5699 | 12.8898 | -116.4882 | 8.6114 | 150.7479 | 0.0067 | 0.0070 |
| 2024_09_20 22:00 | 3257574 | 3 | 12.3935 | 18.9248 | -115.6317 | 11.1873 | 141.0369 | 0.0025 | 0.0096 |
| 2024_09_20 22:00 | 3246056 | 4 | 18.0312 | 18.4233 | -117.7937 | 16.2909 | 180.8430 | 0.0064 | 0.0194 |
| 2024_09_20 22:00 | 3226387 | 5 | 8.1166 | 6.5698 | -116.0066 | 19.2776 | 159.2749 | 0.0118 | 0.0197 |
| 2024_09_20 22:00 | 3232082 | 6 | 9.8473 | 15.2848 | -115.2125 | 17.5019 | 143.7229 | 0.0163 | 0.0136 |
| 2024_09_20 22:00 | 3240619 | 7 | 17.7045 | 11.2892 | -115.4378 | 3.2303 | 51.1358 | 0.0176 | 0.0052 |
| 2024_09_20 22:00 | 3247903 | 8 | 5.2985 | 12.2816 | -114.7661 | 3.9146 | 42.5920 | 0.0158 | 0.0012 |
| 2024_09_20 22:00 | 3230046 | 9 | 14.3894 | 5.5993 | -114.4893 | 4.4581 | 30.6207 | 0.0061 | 0.0169 |
| 2024_09_20 22:00 | 3247084 | 10 | 12.4008 | 12.9593 | -115.8709 | 4.4054 | 27.9920 | 0.0134 | 0.0055 |
| 2024_09_20 22:00 | 3259519 | 11 | 5.3683 | 13.0146 | -117.3678 | 3.1185 | 38.2988 | 0.0167 | 0.0135 |
| 2024_09_20 22:00 | 3248641 | 12 | 6.9013 | 18.2827 | -116.6142 | 3.6664 | 48.8561 | 0.0177 | 0.0179 |
| 2024_09_20 22:00 | 3257978 | 13 | 15.7735 | 13.5926 | -114.1002 | 3.4645 | 45.6576 | 0.0155 | 0.0154 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414507_FF1A9171 | 504990 | 1 | -93.0 | 504990 | 696 | -90.3 | 504990 | 960 | -95.3 | 504990 | 448 |
| MR_1774414507_54178F54 | 504990 | 1 | -92.8 | 504990 | 696 | -89.8 | 504990 | 960 | -94.0 | 504990 | 448 |
| MR_1774414507_88B3D387 | 152650 | 308 | -88.7 | 152650 | 234 | -92.6 | 152650 | 649 | -95.0 | 152650 | 372 |
| MR_1774414507_A47E322E | 152650 | 308 | -88.9 | 152650 | 234 | -91.7 | 152650 | 649 | -94.6 | 152650 | 372 |
| MR_1774414507_A8390E4C | 504990 | 1 | -95.0 | 504990 | 696 | -89.1 | 504990 | 960 | -96.7 | 504990 | 448 |
| MR_1774414507_75145CF6 | 152650 | 308 | -87.4 | 152650 | 234 | -93.6 | 152650 | 649 | -95.6 | 152650 | 372 |
| MR_1774414507_7B1F0F60 | 504990 | 1 | -91.6 | 504990 | 696 | -90.1 | 504990 | 960 | -94.3 | 504990 | 448 |
| MR_1774414507_C82EFF89 | 504990 | 1 | -91.6 | 504990 | 696 | -91.5 | 504990 | 960 | -94.1 | 504990 | 448 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 553: `5f852fa4-a39...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5f852fa4-a395-49cc-aa93-1ac80f3d21ab` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Decrease A3 Offset threshold for 3272875_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[553] topology](images/train_0553.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3272875_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265934_2
- `C3`: Add neighbor relationship between 3265617_1 and 3265934_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272875_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265934_2
- `C6`: Decrease A3 Offset threshold for 3265934_2
- `C7`: Check test server and transmission issues
- `C8`: Lift the tilt angle of 3272875_4 by 10 degrees
- `C9`: Add neighbor relationship between 3272875_4 and 3265934_2
- `C10`: Press down the tilt angle of 3272875_4 by 10 degrees
- `C11`: Increase A3 Offset threshold for 3265934_2
- `C12`: Increase A3 Offset threshold for 3272875_4
- `C13`: Press down the tilt angle  of 3265934_2 by 10 degrees
- `C14`: Adjust the azimuth of 3272875_4 by 50 degrees
- `C15`: Lift the tilt angle  of 3265934_2 by 10 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease A3 Offset threshold for 3272875_4 **← 정답**
- `C18`: Decrease transmission power for 3265934_2
- `C19`: Increase transmission power for 3265934_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272875_4
- `C21`: Decrease transmission power for 3272875_4
- `C22`: Adjust the azimuth of 3265934_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.281 | MS1 | 121.4656731143 | 31.1446301540 | 467 | 504990 | -76.49 | 12.29 | 571.45 | 0.04 | 2.99 | 1579 |
| 2024-09-20 22:21:32.228 | MS1 | 121.4656681341 | 31.1446355829 | 467 | 504990 | -79.39 | 17.94 | 519.10 | 0.08 | 2.46 | 1572 |
| 2024-09-20 22:21:33.477 | MS1 | 121.4656687619 | 31.1446379679 | 467 | 504990 | -82.23 | 16.83 | 594.62 | 0.07 | 2.28 | 1563 |
| 2024-09-20 22:21:34.383 | MS1 | 121.4656651339 | 31.1446186380 | 467 | 504990 | -86.09 | -1.08 | 33.89 | 0.05 | 1.36 | 1580 |
| 2024-09-20 22:21:35.114 | MS1 | 121.4656727675 | 31.1446301795 | 467 | 504990 | -91.93 | -1.11 | 71.86 | 0.13 | 1.00 | 1584 |
| 2024-09-20 22:21:36.910 | MS1 | 121.4656726476 | 31.1446299779 | 467 | 504990 | -84.38 | -1.36 | 61.12 | 0.17 | 1.12 | 1596 |
| 2024-09-20 22:21:37.447 | MS1 | 121.4656639426 | 31.1446209357 | 467 | 504990 | -87.19 | -1.49 | 50.91 | 0.08 | 1.14 | 1594 |
| 2024-09-20 22:21:38.661 | MS1 | 121.4656605126 | 31.1446279736 | 467 | 504990 | -83.36 | -1.06 | 37.51 | 0.12 | 1.35 | 1598 |
| 2024-09-20 22:21:39.616 | MS1 | 121.4656615297 | 31.1446365742 | 611 | 504990 | -79.64 | 13.83 | 155.28 | 0.20 | 1.42 | 1560 |
| 2024-09-20 22:21:40.533 | MS1 | 121.4656767485 | 31.1446368531 | 611 | 504990 | -81.56 | 12.10 | 308.71 | 0.02 | 2.12 | 1573 |
| 2024-09-20 22:21:41.163 | MS1 | 121.4656682592 | 31.1446197729 | 611 | 504990 | -79.79 | 13.54 | 378.79 | 0.19 | 2.44 | 1583 |
| 2024-09-20 22:21:42.433 | MS1 | 121.4656658699 | 31.1446377672 | 611 | 504990 | -83.42 | 17.77 | 564.68 | 0.01 | 2.91 | 1567 |

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
| 3215496 | 3 | 121.4750106460 | 31.1507440854 | 45 | 11 | 7 | 28.4 | TDD | 411 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3265617 | 1 | 121.4667928334 | 31.1558168345 | 191 | 8 | 9 | 35.6 | TDD | 57 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3265934 | 2 | 121.4673489918 | 31.1495211867 | 54 | 12 | 7 | 48.9 | TDD | 611 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3272875 | 4 | 121.4671096713 | 31.1555962700 | 254 | 13 | 9 | 34.6 | TDD | 467 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.871 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.889 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.999 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.999 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.748 | NREventA3 | measId:2;ServCellPCI:835;Se... |
| 2024-09-20 22:21:37.988 | NRHandoverAttempt | SourcePCI:835;SourceNR-ARFC... |
| 2024-09-20 22:21:38.037 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.047 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.197 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.197 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265617 | 1 | 18.6460 | 5.1618 | -117.3811 | 19.4442 | 159.8701 | 0.0035 | 0.0072 |
| 2024_09_20 22:00 | 3265934 | 2 | 11.6674 | 5.4444 | -116.8133 | 8.2783 | 113.5585 | 0.0122 | 0.0047 |
| 2024_09_20 22:00 | 3215496 | 3 | 6.4287 | 10.1860 | -116.0803 | 15.8293 | 155.5683 | 0.0038 | 0.0122 |
| 2024_09_20 22:00 | 3272875 | 4 | 13.6211 | 12.4869 | -115.6845 | 11.1402 | 136.1484 | 0.0000 | 0.1202 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412940_9769A8D4 | 504990 | 467 | -85.5 | 504990 | 611 | -80.1 | 504990 | 57 | -84.9 | 504990 | 411 |
| MR_1774412940_8C149D6C | 504990 | 467 | -84.4 | 504990 | 611 | -81.2 | 504990 | 57 | -86.3 | 504990 | 411 |
| MR_1774412940_FF754BFB | 504990 | 467 | -86.1 | 504990 | 611 | -79.4 | 504990 | 57 | -85.6 | 504990 | 411 |
| MR_1774412940_959F59B0 | 504990 | 467 | -87.1 | 504990 | 611 | -81.0 | 504990 | 57 | -87.9 | 504990 | 411 |
| MR_1774412940_03182E14 | 504990 | 611 | -82.6 | 504990 | 467 | -87.6 | 504990 | 57 | -88.3 | 504990 | 411 |
| MR_1774412940_C4E1F822 | 504990 | 467 | -87.4 | 504990 | 611 | -81.9 | 504990 | 57 | -86.4 | 504990 | 411 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 554: `cd145796-c30...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cd145796-c304-4379-ac74-74fd23dae04f` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Lift the tilt angle  of 3229699_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[554] topology](images/train_0554.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3238864_1
- `C2`: Lift the tilt angle  of 3229699_4 by 10 degrees **← 정답**
- `C3`: Lift the tilt angle of 3238864_1 by 5 degrees
- `C4`: Increase transmission power for 3253041_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238864_1
- `C6`: Add neighbor relationship between 3229699_4 and 3253041_2
- `C7`: Decrease transmission power for 3253041_2
- `C8`: Adjust the azimuth of 3238864_1 by 7 degrees
- `C9`: Increase A3 Offset threshold for 3253041_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Press down the tilt angle  of 3229699_4 by 10 degrees
- `C12`: Decrease A3 Offset threshold for 3253041_2
- `C13`: Press down the tilt angle of 3238864_1 by 5 degrees
- `C14`: Increase A3 Offset threshold for 3238864_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238864_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253041_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253041_2
- `C18`: Check test server and transmission issues
- `C19`: Adjust the azimuth of 3229699_4 by 41 degrees
- `C20`: Add neighbor relationship between 3238864_1 and 3253041_2
- `C21`: Decrease A3 Offset threshold for 3238864_1
- `C22`: Decrease transmission power for 3238864_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.561 | MS1 | 121.4656669141 | 31.1446305765 | 717 | 504990 | -91.66 | 16.33 | 429.09 | 0.15 | 2.33 | 1573 |
| 2024-09-20 22:21:32.571 | MS1 | 121.4656672130 | 31.1446311336 | 717 | 504990 | -91.42 | 12.14 | 300.64 | 0.14 | 2.65 | 1572 |
| 2024-09-20 22:21:33.290 | MS1 | 121.4656769787 | 31.1446273278 | 717 | 504990 | -87.61 | 16.83 | 539.85 | 0.04 | 2.52 | 1574 |
| 2024-09-20 22:21:34.440 | MS1 | 121.4656742229 | 31.1446275950 | 717 | 504990 | -85.68 | 16.83 | 85.34 | 0.18 | 2.46 | 1600 |
| 2024-09-20 22:21:35.876 | MS1 | 121.4656641458 | 31.1446239368 | 717 | 504990 | -88.00 | 13.26 | 67.36 | 0.20 | 2.60 | 1598 |
| 2024-09-20 22:21:36.264 | MS1 | 121.4656700946 | 31.1446192727 | 717 | 504990 | -87.65 | 12.98 | 56.27 | 0.14 | 2.72 | 1594 |
| 2024-09-20 22:21:37.618 | MS1 | 121.4656590989 | 31.1446379093 | 717 | 504990 | -89.69 | 8.72 | 64.32 | 0.09 | 2.26 | 1582 |
| 2024-09-20 22:21:38.413 | MS1 | 121.4656692167 | 31.1446269375 | 717 | 504990 | -89.16 | 11.20 | 54.61 | 0.01 | 2.90 | 1581 |
| 2024-09-20 22:21:39.853 | MS1 | 121.4656709702 | 31.1446352813 | 717 | 504990 | -90.43 | 12.40 | 75.10 | 0.07 | 2.71 | 1574 |
| 2024-09-20 22:21:40.849 | MS1 | 121.4656584881 | 31.1446278848 | 717 | 504990 | -90.84 | 10.38 | 421.14 | 0.10 | 2.58 | 1568 |
| 2024-09-20 22:21:41.488 | MS1 | 121.4656612605 | 31.1446365183 | 717 | 504990 | -92.47 | 7.07 | 511.49 | 0.04 | 2.31 | 1593 |
| 2024-09-20 22:21:42.399 | MS1 | 121.4656616469 | 31.1446257213 | 717 | 504990 | -92.67 | 12.43 | 367.92 | 0.19 | 2.18 | 1581 |

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
| 3214505 | 3 | 121.4648494508 | 31.1536267118 | 187 | 0 | 3 | 43.7 | TDD | 197 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3229699 | 4 | 121.4697286306 | 31.1457431021 | 67 | 14 | 6 | 19.6 | TDD | 154 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3238864 | 1 | 121.4683160952 | 31.1483737629 | 204 | 3 | 0 | 20.1 | TDD | 717 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3253041 | 2 | 121.4678628806 | 31.1446534789 | 310 | 7 | 3 | 19.7 | TDD | 546 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.272 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.287 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.423 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.423 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.107 | NREventA3 | measId:2;ServCellPCI:858;Se... |
| 2024-09-20 22:21:38.347 | NRHandoverAttempt | SourcePCI:858;SourceNR-ARFC... |
| 2024-09-20 22:21:38.378 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.390 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.495 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.495 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238864 | 1 | 75.8855 | 86.7207 | -116.0672 | 18.1303 | 139.5249 | 0.0040 | 0.0005 |
| 2024_09_20 22:00 | 3253041 | 2 | 18.2916 | 7.9327 | -116.5087 | 16.2918 | 106.6583 | 0.0010 | 0.0097 |
| 2024_09_20 22:00 | 3214505 | 3 | 12.0631 | 17.1613 | -114.2791 | 5.0771 | 179.2765 | 0.0197 | 0.0110 |
| 2024_09_20 22:00 | 3229699 | 4 | 16.3042 | 16.0603 | -115.2758 | 6.6424 | 155.1498 | 0.0010 | 0.0132 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413110_CED260C2 | 504990 | 717 | -83.8 | 504990 | 546 | -87.5 | 504990 | 154 | -97.6 | 504990 | 197 |
| MR_1774413110_DFBD93FC | 504990 | 717 | -85.8 | 504990 | 546 | -86.6 | 504990 | 154 | -95.0 | 504990 | 197 |
| MR_1774413110_0062D9F3 | 504990 | 717 | -83.9 | 504990 | 546 | -87.9 | 504990 | 154 | -98.2 | 504990 | 197 |
| MR_1774413110_0CCA63C2 | 504990 | 717 | -84.4 | 504990 | 546 | -85.9 | 504990 | 154 | -97.4 | 504990 | 197 |
| MR_1774413110_A496BEA5 | 504990 | 717 | -86.1 | 504990 | 546 | -87.2 | 504990 | 154 | -97.2 | 504990 | 197 |
| MR_1774413110_A1E27E7C | 504990 | 717 | -84.5 | 504990 | 546 | -84.2 | 504990 | 154 | -96.3 | 504990 | 197 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 555: `75675c0d-105...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `75675c0d-1052-403b-aeda-78e653481f41` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3243211_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[555] topology](images/train_0555.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3275379_3 by 10 degrees
- `C2`: Adjust the azimuth of 3243211_4 by 33 degrees
- `C3`: Add neighbor relationship between 3230995_2 and 3275379_3
- `C4`: Lift the tilt angle of 3243211_4 by 1 degrees
- `C5`: Increase A3 Offset threshold for 3243211_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243211_4
- `C7`: Add neighbor relationship between 3243211_4 and 3275379_3
- `C8`: Check test server and transmission issues
- `C9`: Increase transmission power for 3243211_4
- `C10`: Increase transmission power for 3275379_3
- `C11`: Lift the tilt angle  of 3275379_3 by 10 degrees
- `C12`: Press down the tilt angle of 3243211_4 by 1 degrees
- `C13`: Decrease transmission power for 3243211_4
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease A3 Offset threshold for 3243211_4
- `C16`: Decrease A3 Offset threshold for 3275379_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275379_3
- `C18`: Adjust the azimuth of 3275379_3 by 50 degrees
- `C19`: Decrease transmission power for 3275379_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243211_4 **← 정답**
- `C21`: Increase A3 Offset threshold for 3275379_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275379_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.542 | MS1 | 121.4656739215 | 31.1446333794 | 39 | 504990 | -90.91 | 16.73 | 375.73 | 0.04 | 2.86 | 1569 |
| 2024-09-20 22:21:32.422 | MS1 | 121.4656644883 | 31.1446187736 | 39 | 504990 | -88.10 | 14.50 | 336.74 | 0.12 | 2.87 | 1588 |
| 2024-09-20 22:21:33.841 | MS1 | 121.4656642520 | 31.1446311529 | 39 | 504990 | -85.88 | 17.01 | 530.96 | 0.04 | 2.01 | 1599 |
| 2024-09-20 22:21:34.723 | MS1 | 121.4656582117 | 31.1446218322 | 39 | 504990 | -86.25 | 16.24 | 62.04 | 0.54 | 2.75 | 657 |
| 2024-09-20 22:21:35.590 | MS1 | 121.4656718216 | 31.1446258257 | 39 | 504990 | -88.49 | 13.97 | 75.69 | 0.66 | 2.31 | 673 |
| 2024-09-20 22:21:36.416 | MS1 | 121.4656763995 | 31.1446231809 | 39 | 504990 | -86.88 | 17.40 | 61.41 | 0.60 | 2.16 | 515 |
| 2024-09-20 22:21:37.864 | MS1 | 121.4656765479 | 31.1446356590 | 39 | 504990 | -91.20 | 12.06 | 85.57 | 0.67 | 2.91 | 572 |
| 2024-09-20 22:21:38.483 | MS1 | 121.4656720484 | 31.1446241970 | 39 | 504990 | -90.53 | 8.79 | 87.65 | 0.56 | 2.07 | 522 |
| 2024-09-20 22:21:39.475 | MS1 | 121.4656661433 | 31.1446314722 | 39 | 504990 | -93.15 | 12.52 | 72.79 | 0.69 | 2.76 | 682 |
| 2024-09-20 22:21:40.572 | MS1 | 121.4656755485 | 31.1446357323 | 39 | 504990 | -91.57 | 10.65 | 371.52 | 0.08 | 2.66 | 1586 |
| 2024-09-20 22:21:41.957 | MS1 | 121.4656713811 | 31.1446192198 | 39 | 504990 | -91.80 | 12.07 | 372.55 | 0.07 | 2.14 | 1584 |
| 2024-09-20 22:21:42.116 | MS1 | 121.4656737744 | 31.1446251375 | 39 | 504990 | -90.29 | 7.05 | 442.92 | 0.18 | 2.05 | 1592 |

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
| 3230995 | 2 | 121.4691275238 | 31.1534530615 | 65 | 7 | 10 | 19.4 | TDD | 396 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3243211 | 4 | 121.4737013864 | 31.1542207455 | 249 | 0 | 4 | 32.3 | TDD | 39 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3266087 | 1 | 121.4712618506 | 31.1524477278 | 89 | 10 | 3 | 44.1 | TDD | 433 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3275379 | 3 | 121.4668574304 | 31.1471988008 | 18 | 7 | 8 | 17.4 | TDD | 140 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.835 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.855 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.956 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.956 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.674 | NREventA3 | measId:2;ServCellPCI:430;Se... |
| 2024-09-20 22:21:37.914 | NRHandoverAttempt | SourcePCI:430;SourceNR-ARFC... |
| 2024-09-20 22:21:37.957 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.971 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.084 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.084 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266087 | 1 | 14.9368 | 10.8700 | -114.2761 | 18.6495 | 162.3233 | 0.0119 | 0.0082 |
| 2024_09_20 22:00 | 3230995 | 2 | 7.7619 | 18.8401 | -114.1391 | 12.4538 | 166.7818 | 0.0018 | 0.0000 |
| 2024_09_20 22:00 | 3275379 | 3 | 17.5046 | 12.8052 | -117.7435 | 7.3030 | 137.2820 | 0.0162 | 0.0027 |
| 2024_09_20 22:00 | 3243211 | 4 | 12.7385 | 5.5025 | -114.6639 | 8.0056 | 121.4006 | 0.0132 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417180_15EC009F | 504990 | 39 | -87.5 | 504990 | 140 | -89.2 | 504990 | 396 | -99.3 | 504990 | 433 |
| MR_1774417180_C7130F2F | 504990 | 39 | -85.9 | 504990 | 140 | -87.6 | 504990 | 396 | -97.2 | 504990 | 433 |
| MR_1774417180_AFC74C67 | 504990 | 39 | -87.4 | 504990 | 140 | -90.1 | 504990 | 396 | -96.8 | 504990 | 433 |
| MR_1774417180_54D079BC | 504990 | 39 | -86.4 | 504990 | 140 | -91.2 | 504990 | 396 | -95.5 | 504990 | 433 |
| MR_1774417180_7B8794AA | 504990 | 39 | -84.3 | 504990 | 140 | -87.6 | 504990 | 396 | -96.1 | 504990 | 433 |
| MR_1774417180_A4270915 | 504990 | 39 | -86.0 | 504990 | 140 | -89.9 | 504990 | 396 | -97.4 | 504990 | 433 |
| MR_1774417180_76148742 | 504990 | 39 | -87.1 | 504990 | 140 | -89.2 | 504990 | 396 | -99.2 | 504990 | 433 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 556: `35cab5e0-a9b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `35cab5e0-a9b9-43d9-8a83-a4278f4e8ecd` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Add neighbor relationship between 3278471_2 and 3268369_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[556] topology](images/train_0556.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Press down the tilt angle  of 3268369_3 by 3 degrees
- `C3`: Increase A3 Offset threshold for 3268369_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268369_3
- `C5`: Increase A3 Offset threshold for 3278471_2
- `C6`: Decrease transmission power for 3268369_3
- `C7`: Adjust the azimuth of 3278471_2 by 50 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278471_2
- `C9`: Add neighbor relationship between 3250013_4 and 3268369_3
- `C10`: Adjust the azimuth of 3268369_3 by 49 degrees
- `C11`: Press down the tilt angle of 3278471_2 by 6 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278471_2
- `C13`: Decrease transmission power for 3278471_2
- `C14`: Lift the tilt angle  of 3268369_3 by 3 degrees
- `C15`: Increase transmission power for 3268369_3
- `C16`: Add neighbor relationship between 3278471_2 and 3268369_3 **← 정답**
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268369_3
- `C19`: Decrease A3 Offset threshold for 3278471_2
- `C20`: Lift the tilt angle of 3278471_2 by 6 degrees
- `C21`: Increase transmission power for 3278471_2
- `C22`: Decrease A3 Offset threshold for 3268369_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.870 | MS1 | 121.4656752373 | 31.1446360378 | 613 | 504990 | -78.24 | 13.94 | 480.62 | 0.06 | 2.29 | 1567 |
| 2024-09-20 22:21:32.746 | MS1 | 121.4656651116 | 31.1446217641 | 613 | 504990 | -84.71 | 17.72 | 503.55 | 0.18 | 2.74 | 1584 |
| 2024-09-20 22:21:33.912 | MS1 | 121.4656616200 | 31.1446257613 | 613 | 504990 | -79.21 | 15.43 | 337.09 | 0.19 | 2.96 | 1570 |
| 2024-09-20 22:21:34.348 | MS1 | 121.4656771720 | 31.1446362219 | 613 | 504990 | -85.88 | -3.27 | 26.37 | 0.17 | 1.07 | 1574 |
| 2024-09-20 22:21:35.757 | MS1 | 121.4656676012 | 31.1446276289 | 613 | 504990 | -90.72 | -3.47 | 73.96 | 0.08 | 1.17 | 1563 |
| 2024-09-20 22:21:36.925 | MS1 | 121.4656630325 | 31.1446279697 | 613 | 504990 | -89.77 | -2.41 | 25.66 | 0.13 | 1.24 | 1583 |
| 2024-09-20 22:21:37.229 | MS1 | 121.4656751957 | 31.1446331198 | 613 | 504990 | -89.79 | -0.77 | 63.79 | 0.10 | 1.00 | 1589 |
| 2024-09-20 22:21:38.190 | MS1 | 121.4656737822 | 31.1446290520 | 613 | 504990 | -84.07 | 14.30 | 445.27 | 0.13 | 1.19 | 1572 |
| 2024-09-20 22:21:39.432 | MS1 | 121.4656685226 | 31.1446265873 | 613 | 504990 | -80.33 | 14.39 | 296.71 | 0.06 | 1.24 | 1600 |
| 2024-09-20 22:21:40.376 | MS1 | 121.4656679569 | 31.1446210476 | 613 | 504990 | -77.12 | 16.84 | 322.77 | 0.02 | 2.48 | 1565 |
| 2024-09-20 22:21:41.952 | MS1 | 121.4656710866 | 31.1446321847 | 613 | 504990 | -75.99 | 15.82 | 527.16 | 0.03 | 2.09 | 1570 |
| 2024-09-20 22:21:42.627 | MS1 | 121.4656582368 | 31.1446262621 | 613 | 504990 | -78.56 | 16.91 | 452.54 | 0.16 | 2.33 | 1574 |

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
| 3245052 | 1 | 121.4672397658 | 31.1463710216 | 189 | 8 | 5 | 45.7 | TDD | 914 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3250013 | 4 | 121.4710107750 | 31.1487279322 | 159 | 4 | 11 | 20.3 | TDD | 711 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3268369 | 3 | 121.4757162275 | 31.1492828941 | 291 | 2 | 11 | 23.6 | TDD | 846 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3278471 | 2 | 121.4721130098 | 31.1558877690 | 76 | 4 | 7 | 46.0 | TDD | 613 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.567 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.588 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.710 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.710 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.394 | NREventA3 | measId:2;ServCellPCI:747;Se... |
| 2024-09-20 22:21:36.394 | NREventA3 | measId:2;ServCellPCI:747;Se... |
| 2024-09-20 22:21:37.394 | NREventA3 | measId:2;ServCellPCI:747;Se... |
| 2024-09-20 22:21:39.894 | NRRRCReestablishAttempt | PCI:747 |
| 2024-09-20 22:21:39.904 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.918 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:40.063 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.063 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245052 | 1 | 11.1937 | 11.1887 | -115.4901 | 7.7131 | 158.4033 | 0.0186 | 0.0002 |
| 2024_09_20 22:00 | 3278471 | 2 | 5.5125 | 19.3290 | -115.4801 | 7.8574 | 107.9592 | 0.0012 | 0.1522 |
| 2024_09_20 22:00 | 3268369 | 3 | 8.1708 | 17.4456 | -115.4357 | 17.9726 | 156.6387 | 0.0095 | 0.0092 |
| 2024_09_20 22:00 | 3250013 | 4 | 7.3537 | 15.3283 | -116.6447 | 16.1317 | 183.2774 | 0.0060 | 0.0102 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413719_CE0F030C | 504990 | 846 | -81.3 | 504990 | 613 | -87.3 | 504990 | 711 | -89.9 | 504990 | 914 |
| MR_1774413719_02FEDB77 | 504990 | 613 | -84.7 | 504990 | 846 | -82.7 | 504990 | 711 | -91.6 | 504990 | 914 |
| MR_1774413719_03742865 | 504990 | 613 | -84.8 | 504990 | 846 | -82.8 | 504990 | 711 | -89.2 | 504990 | 914 |
| MR_1774413719_D207C52A | 504990 | 846 | -82.6 | 504990 | 613 | -86.7 | 504990 | 711 | -91.6 | 504990 | 914 |
| MR_1774413719_C8057105 | 504990 | 846 | -79.7 | 504990 | 613 | -84.7 | 504990 | 711 | -88.8 | 504990 | 914 |
| MR_1774413719_14D2BA26 | 504990 | 846 | -82.1 | 504990 | 613 | -85.2 | 504990 | 711 | -90.8 | 504990 | 914 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 557: `a33f37f6-a97...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a33f37f6-a973-4651-a2c4-535b04f33647` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Decrease A3 Offset threshold for 3269431_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[557] topology](images/train_0557.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3269431_3
- `C2`: Press down the tilt angle  of 3271734_2 by 5 degrees
- `C3`: Lift the tilt angle  of 3271734_2 by 5 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269431_3
- `C5`: Decrease transmission power for 3271734_2
- `C6`: Add neighbor relationship between 3220421_4 and 3271734_2
- `C7`: Adjust the azimuth of 3271734_2 by 50 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Check test server and transmission issues
- `C10`: Decrease A3 Offset threshold for 3271734_2
- `C11`: Decrease transmission power for 3269431_3
- `C12`: Increase A3 Offset threshold for 3271734_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271734_2
- `C14`: Increase transmission power for 3269431_3
- `C15`: Adjust the azimuth of 3269431_3 by 23 degrees
- `C16`: Lift the tilt angle of 3269431_3 by 8 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271734_2
- `C18`: Increase transmission power for 3271734_2
- `C19`: Decrease A3 Offset threshold for 3269431_3 **← 정답**
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269431_3
- `C21`: Press down the tilt angle of 3269431_3 by 8 degrees
- `C22`: Add neighbor relationship between 3269431_3 and 3271734_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.935 | MS1 | 121.4656688304 | 31.1446316238 | 644 | 504990 | -81.02 | 12.17 | 539.12 | 0.09 | 2.29 | 1589 |
| 2024-09-20 22:21:32.111 | MS1 | 121.4656777519 | 31.1446237445 | 644 | 504990 | -81.83 | 12.35 | 328.79 | 0.20 | 2.48 | 1572 |
| 2024-09-20 22:21:33.860 | MS1 | 121.4656685985 | 31.1446286271 | 644 | 504990 | -80.32 | 17.04 | 553.98 | 0.15 | 2.70 | 1565 |
| 2024-09-20 22:21:34.709 | MS1 | 121.4656757130 | 31.1446215181 | 644 | 504990 | -85.92 | -1.63 | 52.89 | 0.13 | 1.12 | 1591 |
| 2024-09-20 22:21:35.156 | MS1 | 121.4656625839 | 31.1446180189 | 644 | 504990 | -85.14 | -1.91 | 28.33 | 0.02 | 1.06 | 1570 |
| 2024-09-20 22:21:36.306 | MS1 | 121.4656617734 | 31.1446303306 | 644 | 504990 | -92.00 | -2.19 | 80.15 | 0.15 | 1.06 | 1578 |
| 2024-09-20 22:21:37.909 | MS1 | 121.4656752341 | 31.1446368807 | 644 | 504990 | -83.60 | -0.61 | 66.91 | 0.03 | 1.43 | 1567 |
| 2024-09-20 22:21:38.192 | MS1 | 121.4656734230 | 31.1446272530 | 644 | 504990 | -89.59 | -3.78 | 48.67 | 0.06 | 1.23 | 1566 |
| 2024-09-20 22:21:39.289 | MS1 | 121.4656631892 | 31.1446360702 | 490 | 504990 | -78.75 | 17.33 | 223.65 | 0.17 | 1.34 | 1564 |
| 2024-09-20 22:21:40.418 | MS1 | 121.4656644445 | 31.1446305812 | 490 | 504990 | -78.71 | 15.68 | 381.65 | 0.07 | 2.72 | 1570 |
| 2024-09-20 22:21:41.645 | MS1 | 121.4656596201 | 31.1446367886 | 490 | 504990 | -84.39 | 16.98 | 476.85 | 0.01 | 2.91 | 1600 |
| 2024-09-20 22:21:42.199 | MS1 | 121.4656673132 | 31.1446379480 | 490 | 504990 | -76.25 | 12.63 | 385.95 | 0.19 | 2.21 | 1579 |

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
| 3220421 | 4 | 121.4662907887 | 31.1463335176 | 112 | 8 | 9 | 47.9 | TDD | 437 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3251349 | 1 | 121.4743933812 | 31.1462107341 | 112 | 8 | 9 | 43.1 | TDD | 992 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3269431 | 3 | 121.4659195461 | 31.1496996493 | 205 | 5 | 0 | 29.6 | TDD | 644 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3271734 | 2 | 121.4695501133 | 31.1554439258 | 95 | 4 | 5 | 15.4 | TDD | 490 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.962 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.987 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.092 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.092 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.861 | NREventA3 | measId:2;ServCellPCI:880;Se... |
| 2024-09-20 22:21:38.101 | NRHandoverAttempt | SourcePCI:880;SourceNR-ARFC... |
| 2024-09-20 22:21:38.142 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.157 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.306 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.306 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251349 | 1 | 9.1295 | 10.4650 | -115.2352 | 12.1981 | 131.9017 | 0.0079 | 0.0046 |
| 2024_09_20 22:00 | 3271734 | 2 | 14.6233 | 19.1977 | -114.7889 | 19.6477 | 88.9450 | 0.0016 | 0.0070 |
| 2024_09_20 22:00 | 3269431 | 3 | 17.1887 | 14.6081 | -116.3167 | 5.0125 | 152.6888 | 0.0140 | 0.1192 |
| 2024_09_20 22:00 | 3220421 | 4 | 6.6039 | 16.6121 | -116.4895 | 14.2046 | 158.1236 | 0.0136 | 0.0053 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417211_63553ADB | 504990 | 644 | -86.8 | 504990 | 490 | -79.2 | 504990 | 437 | -80.3 | 504990 | 992 |
| MR_1774417211_45FD66C7 | 504990 | 644 | -86.9 | 504990 | 490 | -82.3 | 504990 | 437 | -81.7 | 504990 | 992 |
| MR_1774417211_E83A9297 | 504990 | 644 | -87.5 | 504990 | 490 | -79.9 | 504990 | 437 | -82.2 | 504990 | 992 |
| MR_1774417211_0F13241D | 504990 | 644 | -86.4 | 504990 | 490 | -78.5 | 504990 | 437 | -81.0 | 504990 | 992 |
| MR_1774417211_FE25A10A | 504990 | 490 | -80.3 | 504990 | 644 | -85.8 | 504990 | 437 | -82.2 | 504990 | 992 |
| MR_1774417211_BC42DF4F | 504990 | 490 | -79.4 | 504990 | 644 | -87.3 | 504990 | 437 | -79.7 | 504990 | 992 |
| MR_1774417211_615FBAEE | 504990 | 490 | -79.9 | 504990 | 644 | -87.8 | 504990 | 437 | -79.6 | 504990 | 992 |
| MR_1774417211_BF020031 | 504990 | 644 | -86.6 | 504990 | 490 | -79.4 | 504990 | 437 | -81.4 | 504990 | 992 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 558: `0b316bf5-28c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0b316bf5-28c8-45a8-8de0-d62f8078a9b3` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease A3 Offset threshold for 3254074_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[558] topology](images/train_0558.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3247577_3 by 10 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254074_2
- `C3`: Decrease A3 Offset threshold for 3254074_2 **← 정답**
- `C4`: Decrease transmission power for 3254074_2
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase transmission power for 3247577_3
- `C7`: Decrease A3 Offset threshold for 3247577_3
- `C8`: Increase A3 Offset threshold for 3247577_3
- `C9`: Add neighbor relationship between 3268167_4 and 3247577_3
- `C10`: Press down the tilt angle  of 3247577_3 by 10 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247577_3
- `C12`: Lift the tilt angle of 3254074_2 by 5 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254074_2
- `C14`: Decrease transmission power for 3247577_3
- `C15`: Increase A3 Offset threshold for 3254074_2
- `C16`: Press down the tilt angle of 3254074_2 by 5 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247577_3
- `C18`: Add neighbor relationship between 3254074_2 and 3247577_3
- `C19`: Increase transmission power for 3254074_2
- `C20`: Adjust the azimuth of 3247577_3 by 50 degrees
- `C21`: Adjust the azimuth of 3254074_2 by 50 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.699 | MS1 | 121.4656705872 | 31.1446254289 | 841 | 504990 | -78.70 | 16.35 | 375.87 | 0.16 | 2.39 | 1598 |
| 2024-09-20 22:21:32.745 | MS1 | 121.4656640033 | 31.1446239906 | 841 | 504990 | -80.58 | 16.00 | 426.90 | 0.14 | 2.06 | 1593 |
| 2024-09-20 22:21:33.245 | MS1 | 121.4656762798 | 31.1446272702 | 841 | 504990 | -83.59 | 12.75 | 353.97 | 0.14 | 2.94 | 1583 |
| 2024-09-20 22:21:34.375 | MS1 | 121.4656638248 | 31.1446236723 | 841 | 504990 | -89.78 | -2.14 | 56.85 | 0.01 | 1.45 | 1596 |
| 2024-09-20 22:21:35.717 | MS1 | 121.4656767505 | 31.1446237207 | 841 | 504990 | -91.00 | -3.16 | 59.28 | 0.12 | 1.29 | 1585 |
| 2024-09-20 22:21:36.547 | MS1 | 121.4656668429 | 31.1446227638 | 841 | 504990 | -91.10 | -3.52 | 30.66 | 0.00 | 1.14 | 1592 |
| 2024-09-20 22:21:37.799 | MS1 | 121.4656747463 | 31.1446192276 | 841 | 504990 | -91.52 | -1.30 | 76.62 | 0.13 | 1.40 | 1573 |
| 2024-09-20 22:21:38.442 | MS1 | 121.4656654548 | 31.1446357400 | 841 | 504990 | -83.20 | -1.00 | 49.36 | 0.16 | 1.28 | 1577 |
| 2024-09-20 22:21:39.129 | MS1 | 121.4656600981 | 31.1446306012 | 154 | 504990 | -75.49 | 13.03 | 249.48 | 0.13 | 1.01 | 1575 |
| 2024-09-20 22:21:40.375 | MS1 | 121.4656739402 | 31.1446274281 | 154 | 504990 | -75.77 | 12.34 | 590.52 | 0.05 | 3.00 | 1576 |
| 2024-09-20 22:21:41.122 | MS1 | 121.4656651847 | 31.1446244101 | 154 | 504990 | -79.61 | 12.71 | 597.48 | 0.08 | 2.81 | 1569 |
| 2024-09-20 22:21:42.220 | MS1 | 121.4656635778 | 31.1446364314 | 154 | 504990 | -80.63 | 16.17 | 410.28 | 0.01 | 2.67 | 1564 |

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
| 3230828 | 1 | 121.4673529691 | 31.1526079788 | 3 | 12 | 7 | 43.8 | TDD | 808 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3247577 | 3 | 121.4645034925 | 31.1546670923 | 94 | 11 | 8 | 39.7 | TDD | 154 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3254074 | 2 | 121.4662600553 | 31.1558838591 | 39 | 4 | 9 | 23.7 | TDD | 841 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3268167 | 4 | 121.4742072345 | 31.1470332173 | 135 | 6 | 12 | 15.0 | TDD | 487 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.516 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.533 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.654 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.654 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.384 | NREventA3 | measId:2;ServCellPCI:592;Se... |
| 2024-09-20 22:21:38.624 | NRHandoverAttempt | SourcePCI:592;SourceNR-ARFC... |
| 2024-09-20 22:21:38.658 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.668 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.770 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.770 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230828 | 1 | 16.1981 | 7.6580 | -114.7979 | 5.9455 | 183.6922 | 0.0133 | 0.0158 |
| 2024_09_20 22:00 | 3254074 | 2 | 10.1604 | 14.9209 | -114.3344 | 12.7360 | 175.6612 | 0.0142 | 0.1293 |
| 2024_09_20 22:00 | 3247577 | 3 | 6.6597 | 13.1905 | -116.9546 | 6.9072 | 117.2542 | 0.0077 | 0.0072 |
| 2024_09_20 22:00 | 3268167 | 4 | 13.3477 | 17.7712 | -116.2451 | 12.2749 | 178.4753 | 0.0091 | 0.0058 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414516_9D1101B6 | 504990 | 841 | -88.1 | 504990 | 154 | -83.6 | 504990 | 487 | -82.9 | 504990 | 808 |
| MR_1774414516_39D8F689 | 504990 | 841 | -91.4 | 504990 | 154 | -82.7 | 504990 | 487 | -82.8 | 504990 | 808 |
| MR_1774414516_83709000 | 504990 | 841 | -90.0 | 504990 | 154 | -84.0 | 504990 | 487 | -83.8 | 504990 | 808 |
| MR_1774414516_70C3F504 | 504990 | 841 | -89.8 | 504990 | 154 | -85.4 | 504990 | 487 | -82.1 | 504990 | 808 |
| MR_1774414516_1B6A7C74 | 504990 | 154 | -84.9 | 504990 | 841 | -91.0 | 504990 | 487 | -84.6 | 504990 | 808 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 559: `0936e665-8c4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0936e665-8c4c-43aa-9439-06415aa23848` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277058_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[559] topology](images/train_0559.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253630_1
- `C2`: Add neighbor relationship between 3226757_9 and 3253630_1
- `C3`: Press down the tilt angle of 3277058_5 by 6 degrees
- `C4`: Adjust the azimuth of 3277058_5 by 2 degrees
- `C5`: Increase transmission power for 3277058_5
- `C6`: Check test server and transmission issues
- `C7`: Adjust the azimuth of 3253630_1 by 33 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277058_5 **← 정답**
- `C9`: Press down the tilt angle  of 3253630_1 by 4 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253630_1
- `C12`: Lift the tilt angle  of 3253630_1 by 4 degrees
- `C13`: Decrease transmission power for 3253630_1
- `C14`: Increase A3 Offset threshold for 3253630_1
- `C15`: Decrease A3 Offset threshold for 3277058_5
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277058_5
- `C17`: Increase transmission power for 3253630_1
- `C18`: Increase A3 Offset threshold for 3277058_5
- `C19`: Decrease A3 Offset threshold for 3253630_1
- `C20`: Add neighbor relationship between 3277058_5 and 3253630_1
- `C21`: Lift the tilt angle of 3277058_5 by 6 degrees
- `C22`: Decrease transmission power for 3277058_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.983 | MS1 | 121.4656656074 | 31.1446366355 | 730 | 504990 | -94.67 | 9.03 | 392.93 | 0.18 | 2.93 | 1568 |
| 2024-09-20 22:21:32.269 | MS1 | 121.4656643495 | 31.1446336585 | 756 | 504990 | -95.81 | 14.91 | 332.27 | 0.11 | 2.94 | 1576 |
| 2024-09-20 22:21:33.386 | MS1 | 121.4656657188 | 31.1446341373 | 443 | 504990 | -95.38 | 10.04 | 533.20 | 0.14 | 2.50 | 1582 |
| 2024-09-20 22:21:34.863 | MS1 | 121.4656583215 | 31.1446274275 | 707 | 152650 | -91.14 | 2.20 | 101.33 | 0.10 | 1.74 | 956 |
| 2024-09-20 22:21:35.951 | MS1 | 121.4656625267 | 31.1446213234 | 790 | 152650 | -89.53 | 6.43 | 65.54 | 0.17 | 1.76 | 970 |
| 2024-09-20 22:21:36.384 | MS1 | 121.4656765482 | 31.1446251624 | 519 | 152650 | -94.89 | 3.90 | 59.01 | 0.06 | 1.86 | 978 |
| 2024-09-20 22:21:37.806 | MS1 | 121.4656735103 | 31.1446364648 | 261 | 152650 | -88.41 | 7.97 | 63.37 | 0.10 | 1.84 | 994 |
| 2024-09-20 22:21:38.650 | MS1 | 121.4656640579 | 31.1446201795 | 707 | 152650 | -89.58 | 2.81 | 92.41 | 0.17 | 1.60 | 962 |
| 2024-09-20 22:21:39.534 | MS1 | 121.4656725146 | 31.1446379438 | 790 | 152650 | -96.10 | 5.96 | 75.09 | 0.03 | 1.78 | 912 |
| 2024-09-20 22:21:40.555 | MS1 | 121.4656774249 | 31.1446258637 | 519 | 152650 | -95.61 | 4.45 | 68.12 | 0.13 | 2.67 | 1591 |
| 2024-09-20 22:21:41.547 | MS1 | 121.4656605507 | 31.1446197499 | 261 | 152650 | -92.67 | 3.35 | 60.34 | 0.09 | 2.07 | 1591 |
| 2024-09-20 22:21:42.816 | MS1 | 121.4656724923 | 31.1446191651 | 707 | 152650 | -88.36 | 5.74 | 80.10 | 0.17 | 2.38 | 1560 |

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
| 3213305 | 2 | 121.4730888387 | 31.1457939643 | 295 | 9 | 5 | 27.4 | TDD | 273 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3213744 | 10 | 121.4646751614 | 31.1480542237 | 91 | 12 | 12 | 22.9 | FDD | 790 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3226757 | 9 | 121.4709321708 | 31.1557151457 | 19 | 14 | 7 | 10.4 | FDD | 519 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3229456 | 3 | 121.4707029386 | 31.1497856293 | 89 | 5 | 8 | 0.2 | TDD | 370 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3231433 | 6 | 121.4678491855 | 31.1522865590 | 238 | 9 | 5 | 7.6 | TDD | 443 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3236091 | 13 | 121.4681063560 | 31.1527966480 | 182 | 10 | 10 | 0.9 | FDD | 633 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3237461 | 8 | 121.4667981225 | 31.1500412407 | 348 | 2 | 2 | 21.4 | FDD | 261 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3240274 | 4 | 121.4702734687 | 31.1458656006 | 33 | 12 | 0 | 27.3 | TDD | 756 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3247489 | 11 | 121.4672667272 | 31.1551055257 | 153 | 11 | 10 | 12.2 | FDD | 55 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3253630 | 1 | 121.4667274146 | 31.1504474963 | 156 | 2 | 3 | 26.2 | TDD | 395 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3262252 | 7 | 121.4726616581 | 31.1494635035 | 92 | 0 | 11 | 17.4 | FDD | 707 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3262462 | 12 | 121.4716944528 | 31.1546599254 | 92 | 7 | 0 | 19.8 | FDD | 54 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3277058 | 5 | 121.4730436006 | 31.1469764417 | 248 | 4 | 12 | 22.6 | TDD | 730 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.442 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.457 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.580 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.580 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.284 | NREventA2 | measId:1;ServCellPCI:810;Se... |
| 2024-09-20 22:21:35.388 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.600 | NREventA5 | measId:3;ServCellPCI:810;Se... |
| 2024-09-20 22:21:35.651 | NRHandoverAttempt | SourcePCI:810;SourceNR-ARFC... |
| 2024-09-20 22:21:35.699 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.712 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.830 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.830 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253630 | 1 | 9.6852 | 15.9155 | -116.1435 | 5.4604 | 99.1425 | 0.0071 | 0.0109 |
| 2024_09_20 22:00 | 3213305 | 2 | 5.9891 | 14.7682 | -115.6204 | 19.1291 | 165.0543 | 0.0121 | 0.0028 |
| 2024_09_20 22:00 | 3229456 | 3 | 17.8997 | 11.5531 | -117.1623 | 5.5944 | 135.7462 | 0.0080 | 0.0161 |
| 2024_09_20 22:00 | 3240274 | 4 | 13.3628 | 17.9655 | -116.0768 | 18.2058 | 172.6893 | 0.0017 | 0.0124 |
| 2024_09_20 22:00 | 3277058 | 5 | 14.1875 | 7.8380 | -115.9349 | 15.7037 | 133.2086 | 0.0039 | 0.0074 |
| 2024_09_20 22:00 | 3231433 | 6 | 15.6665 | 18.6520 | -115.2927 | 18.3198 | 188.5678 | 0.0060 | 0.0196 |
| 2024_09_20 22:00 | 3262252 | 7 | 9.1794 | 15.9283 | -115.2034 | 3.0261 | 46.6907 | 0.0089 | 0.0122 |
| 2024_09_20 22:00 | 3237461 | 8 | 11.6166 | 11.2357 | -116.0183 | 4.0884 | 33.7326 | 0.0081 | 0.0006 |
| 2024_09_20 22:00 | 3226757 | 9 | 10.7503 | 12.9404 | -116.4415 | 3.9344 | 30.1660 | 0.0052 | 0.0013 |
| 2024_09_20 22:00 | 3213744 | 10 | 10.8736 | 18.2190 | -117.3940 | 4.8673 | 25.0276 | 0.0009 | 0.0159 |
| 2024_09_20 22:00 | 3247489 | 11 | 18.0992 | 18.6264 | -114.2906 | 3.3414 | 55.2928 | 0.0096 | 0.0057 |
| 2024_09_20 22:00 | 3262462 | 12 | 9.5868 | 15.5320 | -117.8642 | 3.1344 | 56.1949 | 0.0095 | 0.0010 |
| 2024_09_20 22:00 | 3236091 | 13 | 12.3041 | 19.7300 | -116.9100 | 4.0196 | 50.7365 | 0.0107 | 0.0019 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413318_09CF5A13 | 152650 | 790 | -91.4 | 152650 | 55 | -93.9 | 152650 | 54 | -100.8 | 152650 | 633 |
| MR_1774413318_AC73354D | 504990 | 443 | -96.7 | 504990 | 395 | -97.4 | 504990 | 370 | -101.3 | 504990 | 273 |
| MR_1774413318_AB5ACC69 | 152650 | 790 | -87.8 | 152650 | 55 | -93.0 | 152650 | 54 | -101.1 | 152650 | 633 |
| MR_1774413318_E08EA8E2 | 504990 | 443 | -95.0 | 504990 | 395 | -98.4 | 504990 | 370 | -99.5 | 504990 | 273 |
| MR_1774413318_124A7D70 | 152650 | 790 | -90.5 | 152650 | 55 | -93.5 | 152650 | 54 | -101.8 | 152650 | 633 |
| MR_1774413318_45C799FB | 504990 | 443 | -95.8 | 504990 | 395 | -95.7 | 504990 | 370 | -102.5 | 504990 | 273 |
| MR_1774413318_D70F2DD6 | 152650 | 790 | -89.8 | 152650 | 55 | -93.9 | 152650 | 54 | -100.8 | 152650 | 633 |

> *... 2개 열 생략 (전체 14열)*

---
