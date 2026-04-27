# Track A 문제 분석 — train[1120]~train[1129]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1120] ~ train[1129] (10개)

## 목차

1. [문제 1120: `c4556c4e-c80...`](#1120) — multiple-answer, 정답: C6|C19
2. [문제 1121: `60bd3112-d3c...`](#1121) — single-answer, 정답: C20
3. [문제 1122: `8519b021-c96...`](#1122) — single-answer, 정답: C22
4. [문제 1123: `99baaed0-c68...`](#1123) — single-answer, 정답: C17
5. [문제 1124: `3a2053bc-168...`](#1124) — single-answer, 정답: C10
6. [문제 1125: `2d8f1e7e-06c...`](#1125) — single-answer, 정답: C10
7. [문제 1126: `ccb103e9-99b...`](#1126) — single-answer, 정답: C14
8. [문제 1127: `01713429-65b...`](#1127) — single-answer, 정답: C10
9. [문제 1128: `38977302-7e0...`](#1128) — multiple-answer, 정답: C1|C2
10. [문제 1129: `aa08e309-a55...`](#1129) — single-answer, 정답: C13

---

### 문제 1120: `c4556c4e-c80...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c4556c4e-c802-48b5-b912-12bce04a4505` |
| Tag | **multiple-answer** |
| 정답 | **C6|C19** |
| C6 의미 | Adjust the azimuth of 3227421_3 by 50 degrees |
| C19 의미 | Increase transmission power for 3227421_3 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1120] topology](images/train_1120.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3236073_2 by 39 degrees
- `C2`: Increase transmission power for 3236073_2
- `C3`: Decrease A3 Offset threshold for 3236073_2
- `C4`: Decrease transmission power for 3236073_2
- `C5`: Increase A3 Offset threshold for 3236073_2
- `C6`: Adjust the azimuth of 3227421_3 by 50 degrees **← 정답**
- `C7`: Increase A3 Offset threshold for 3227421_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236073_2
- `C9`: Press down the tilt angle  of 3236073_2 by 6 degrees
- `C10`: Add neighbor relationship between 3259356_4 and 3236073_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227421_3
- `C12`: Check test server and transmission issues
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227421_3
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease transmission power for 3227421_3
- `C16`: Lift the tilt angle  of 3236073_2 by 6 degrees
- `C17`: Add neighbor relationship between 3227421_3 and 3236073_2
- `C18`: Decrease A3 Offset threshold for 3227421_3
- `C19`: Increase transmission power for 3227421_3 **← 정답**
- `C20`: Lift the tilt angle of 3227421_3 by 2 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236073_2
- `C22`: Press down the tilt angle of 3227421_3 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.781 | MS1 | 121.4656630498 | 31.1446372122 | 701 | 504990 | -94.31 | 13.94 | 343.27 | 0.15 | 2.47 | 1567 |
| 2024-09-20 22:21:32.787 | MS1 | 121.4656587308 | 31.1446181834 | 701 | 504990 | -90.56 | 17.03 | 518.40 | 0.00 | 2.38 | 1565 |
| 2024-09-20 22:21:33.692 | MS1 | 121.4656582555 | 31.1446260173 | 701 | 504990 | -92.59 | 16.31 | 522.97 | 0.09 | 2.73 | 1599 |
| 2024-09-20 22:21:34.811 | MS1 | 121.4656714701 | 31.1446222484 | 701 | 504990 | -101.69 | 1.17 | 54.70 | 0.11 | 1.05 | 1594 |
| 2024-09-20 22:21:35.424 | MS1 | 121.4656619451 | 31.1446265293 | 701 | 504990 | -103.84 | 0.69 | 30.18 | 0.11 | 1.07 | 1580 |
| 2024-09-20 22:21:36.716 | MS1 | 121.4656692384 | 31.1446342707 | 701 | 504990 | -109.93 | 1.88 | 46.02 | 0.08 | 1.48 | 1583 |
| 2024-09-20 22:21:37.176 | MS1 | 121.4656737822 | 31.1446301815 | 701 | 504990 | -108.96 | -0.71 | 49.91 | 0.02 | 1.20 | 1567 |
| 2024-09-20 22:21:38.742 | MS1 | 121.4656705032 | 31.1446209944 | 701 | 504990 | -104.35 | -0.42 | 32.43 | 0.04 | 1.05 | 1564 |
| 2024-09-20 22:21:39.553 | MS1 | 121.4656755101 | 31.1446262603 | 701 | 504990 | -103.97 | 0.40 | 29.36 | 0.03 | 1.46 | 1580 |
| 2024-09-20 22:21:40.372 | MS1 | 121.4656739416 | 31.1446295201 | 701 | 504990 | -90.35 | 14.62 | 552.55 | 0.01 | 2.14 | 1595 |
| 2024-09-20 22:21:41.401 | MS1 | 121.4656615533 | 31.1446332002 | 701 | 504990 | -89.94 | 14.65 | 437.32 | 0.18 | 2.31 | 1561 |
| 2024-09-20 22:21:42.868 | MS1 | 121.4656741687 | 31.1446232096 | 701 | 504990 | -92.03 | 17.06 | 308.07 | 0.06 | 2.21 | 1567 |

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
| 3227421 | 3 | 121.4707514808 | 31.1472742440 | 289 | 0 | 4 | 19.5 | TDD | 701 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3231119 | 1 | 121.4726606158 | 31.1518274404 | 112 | 14 | 0 | 17.6 | TDD | 529 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3236073 | 2 | 121.4739767823 | 31.1536488151 | 179 | 4 | 3 | 39.3 | TDD | 842 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3259356 | 4 | 121.4759921587 | 31.1498735007 | 218 | 3 | 7 | 39.6 | TDD | 423 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.971 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.993 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.094 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.094 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.357 | NREventA2 | measId:1;ServCellPCI:296;Se... |
| 2024-09-20 22:21:34.459 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231119 | 1 | 12.8234 | 12.4750 | -114.1984 | 8.5223 | 182.4708 | 0.0196 | 0.0026 |
| 2024_09_20 22:00 | 3236073 | 2 | 18.3316 | 16.1212 | -116.4321 | 10.6956 | 114.9255 | 0.0123 | 0.0057 |
| 2024_09_20 22:00 | 3227421 | 3 | 13.7040 | 19.0854 | -114.0909 | 11.0098 | 114.2758 | 0.1746 | 0.0009 |
| 2024_09_20 22:00 | 3259356 | 4 | 8.6450 | 9.2150 | -114.6807 | 18.2479 | 145.8427 | 0.0117 | 0.0144 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413881_218DC15D | 504990 | 701 | -100.9 | 504990 | 842 | -105.5 | 504990 | 423 | -110.6 | 504990 | 529 |
| MR_1774413881_637381D8 | 504990 | 701 | -103.1 | 504990 | 842 | -106.3 | 504990 | 423 | -113.5 | 504990 | 529 |
| MR_1774413881_CD98D066 | 504990 | 701 | -101.8 | 504990 | 842 | -104.6 | 504990 | 423 | -112.8 | 504990 | 529 |
| MR_1774413881_BAEF9746 | 504990 | 701 | -101.4 | 504990 | 842 | -107.6 | 504990 | 423 | -114.2 | 504990 | 529 |
| MR_1774413881_BAE25071 | 504990 | 701 | -102.7 | 504990 | 842 | -104.1 | 504990 | 423 | -111.2 | 504990 | 529 |
| MR_1774413881_23456447 | 504990 | 701 | -102.8 | 504990 | 842 | -106.1 | 504990 | 423 | -113.3 | 504990 | 529 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1121: `60bd3112-d3c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `60bd3112-d3c0-4137-a4ac-ce2e4d1f37c4` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213382_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1121] topology](images/train_1121.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3262846_3 by 1 degrees
- `C2`: Decrease transmission power for 3262846_3
- `C3`: Decrease A3 Offset threshold for 3213382_5
- `C4`: Decrease A3 Offset threshold for 3262846_3
- `C5`: Increase A3 Offset threshold for 3262846_3
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase transmission power for 3213382_5
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262846_3
- `C9`: Lift the tilt angle of 3213382_5 by 0 degrees
- `C10`: Increase transmission power for 3262846_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262846_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213382_5
- `C13`: Increase A3 Offset threshold for 3213382_5
- `C14`: Check test server and transmission issues
- `C15`: Lift the tilt angle  of 3262846_3 by 1 degrees
- `C16`: Adjust the azimuth of 3262846_3 by 11 degrees
- `C17`: Decrease transmission power for 3213382_5
- `C18`: Add neighbor relationship between 3241512_9 and 3262846_3
- `C19`: Press down the tilt angle of 3213382_5 by 0 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213382_5 **← 정답**
- `C21`: Add neighbor relationship between 3213382_5 and 3262846_3
- `C22`: Adjust the azimuth of 3213382_5 by 43 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.773 | MS1 | 121.4656583431 | 31.1446297051 | 413 | 504990 | -94.95 | 13.44 | 496.92 | 0.09 | 2.60 | 1593 |
| 2024-09-20 22:21:32.336 | MS1 | 121.4656605518 | 31.1446215234 | 1 | 504990 | -93.95 | 12.80 | 470.46 | 0.02 | 2.39 | 1570 |
| 2024-09-20 22:21:33.891 | MS1 | 121.4656685022 | 31.1446273673 | 697 | 504990 | -93.96 | 12.68 | 314.61 | 0.11 | 2.46 | 1596 |
| 2024-09-20 22:21:34.898 | MS1 | 121.4656724754 | 31.1446230205 | 229 | 152650 | -91.71 | 3.15 | 97.66 | 0.06 | 1.70 | 913 |
| 2024-09-20 22:21:35.933 | MS1 | 121.4656630078 | 31.1446304283 | 304 | 152650 | -91.88 | 5.48 | 62.25 | 0.13 | 1.93 | 971 |
| 2024-09-20 22:21:36.850 | MS1 | 121.4656711633 | 31.1446282116 | 586 | 152650 | -89.95 | 4.69 | 79.94 | 0.14 | 1.95 | 946 |
| 2024-09-20 22:21:37.743 | MS1 | 121.4656732224 | 31.1446250964 | 50 | 152650 | -94.78 | 6.72 | 78.67 | 0.18 | 1.86 | 963 |
| 2024-09-20 22:21:38.216 | MS1 | 121.4656660976 | 31.1446345016 | 229 | 152650 | -88.83 | 3.18 | 75.11 | 0.10 | 1.60 | 924 |
| 2024-09-20 22:21:39.838 | MS1 | 121.4656645582 | 31.1446213498 | 304 | 152650 | -95.11 | 2.23 | 77.03 | 0.20 | 1.70 | 906 |
| 2024-09-20 22:21:40.100 | MS1 | 121.4656755127 | 31.1446182309 | 586 | 152650 | -93.42 | 2.65 | 62.75 | 0.15 | 2.92 | 1592 |
| 2024-09-20 22:21:41.121 | MS1 | 121.4656588098 | 31.1446218292 | 50 | 152650 | -88.36 | 2.08 | 84.48 | 0.04 | 2.38 | 1592 |
| 2024-09-20 22:21:42.512 | MS1 | 121.4656606070 | 31.1446333264 | 229 | 152650 | -95.14 | 2.95 | 55.03 | 0.08 | 2.64 | 1589 |

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
| 3213382 | 5 | 121.4752875052 | 31.1451194387 | 224 | 0 | 4 | 0.2 | TDD | 413 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3218930 | 4 | 121.4650429237 | 31.1488433881 | 258 | 6 | 0 | 9.4 | TDD | 697 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3232729 | 13 | 121.4707091745 | 31.1547479734 | 180 | 11 | 7 | 25.9 | FDD | 959 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3234654 | 11 | 121.4734932117 | 31.1520629713 | 286 | 1 | 5 | 23.8 | FDD | 50 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3241512 | 9 | 121.4733904494 | 31.1448054325 | 280 | 14 | 6 | 7.8 | FDD | 586 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3262693 | 2 | 121.4666946989 | 31.1523112102 | 2 | 11 | 1 | 26.6 | TDD | 1 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3262846 | 3 | 121.4671601055 | 31.1533397106 | 199 | 1 | 4 | 1.4 | TDD | 600 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3266026 | 8 | 121.4713845306 | 31.1467137189 | 160 | 4 | 5 | 8.0 | FDD | 938 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3266197 | 12 | 121.4745185975 | 31.1507025119 | 182 | 14 | 5 | 3.9 | FDD | 889 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3269373 | 7 | 121.4657423205 | 31.1536050072 | 7 | 7 | 4 | 26.6 | FDD | 229 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3269395 | 10 | 121.4720840381 | 31.1494190385 | 77 | 13 | 2 | 6.9 | FDD | 304 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3276039 | 6 | 121.4693851559 | 31.1509339953 | 159 | 3 | 1 | 5.5 | TDD | 286 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3276143 | 1 | 121.4744463397 | 31.1484002274 | 64 | 0 | 8 | 24.8 | TDD | 640 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.549 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.565 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.694 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.694 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.383 | NREventA2 | measId:1;ServCellPCI:254;Se... |
| 2024-09-20 22:21:35.495 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.765 | NREventA5 | measId:3;ServCellPCI:254;Se... |
| 2024-09-20 22:21:35.809 | NRHandoverAttempt | SourcePCI:254;SourceNR-ARFC... |
| 2024-09-20 22:21:35.842 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.853 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.966 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.966 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276143 | 1 | 9.6331 | 10.6018 | -117.2610 | 7.0722 | 158.6740 | 0.0129 | 0.0152 |
| 2024_09_20 22:00 | 3262693 | 2 | 10.1119 | 16.3940 | -116.5786 | 15.4312 | 103.7089 | 0.0109 | 0.0125 |
| 2024_09_20 22:00 | 3262846 | 3 | 13.0125 | 11.3972 | -114.9530 | 7.0047 | 95.8392 | 0.0109 | 0.0122 |
| 2024_09_20 22:00 | 3218930 | 4 | 12.2863 | 18.7992 | -114.0077 | 19.1505 | 85.8823 | 0.0168 | 0.0120 |
| 2024_09_20 22:00 | 3213382 | 5 | 5.3484 | 15.0011 | -115.9625 | 5.8273 | 149.0064 | 0.0017 | 0.0035 |
| 2024_09_20 22:00 | 3276039 | 6 | 14.7531 | 17.5516 | -116.7904 | 5.0268 | 90.0358 | 0.0186 | 0.0162 |
| 2024_09_20 22:00 | 3269373 | 7 | 14.2114 | 11.7461 | -114.2312 | 4.4864 | 33.5006 | 0.0041 | 0.0023 |
| 2024_09_20 22:00 | 3266026 | 8 | 16.6056 | 17.8038 | -116.3657 | 3.2997 | 52.8606 | 0.0107 | 0.0177 |
| 2024_09_20 22:00 | 3241512 | 9 | 13.9681 | 13.4899 | -117.2276 | 4.7626 | 59.8938 | 0.0119 | 0.0060 |
| 2024_09_20 22:00 | 3269395 | 10 | 10.3277 | 18.5259 | -115.7922 | 3.1763 | 58.8201 | 0.0002 | 0.0160 |
| 2024_09_20 22:00 | 3234654 | 11 | 10.9626 | 9.5853 | -114.4830 | 4.0059 | 22.4767 | 0.0020 | 0.0197 |
| 2024_09_20 22:00 | 3266197 | 12 | 5.7189 | 13.5756 | -115.3980 | 4.9787 | 41.7903 | 0.0105 | 0.0106 |
| 2024_09_20 22:00 | 3232729 | 13 | 15.4515 | 18.8510 | -115.1003 | 4.6952 | 27.9627 | 0.0027 | 0.0154 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414788_BA0499AE | 504990 | 697 | -93.3 | 504990 | 600 | -89.0 | 504990 | 286 | -96.9 | 504990 | 640 |
| MR_1774414788_0B91D92C | 152650 | 229 | -92.4 | 152650 | 938 | -94.3 | 152650 | 959 | -103.5 | 152650 | 889 |
| MR_1774414788_0526FDF6 | 504990 | 697 | -95.2 | 504990 | 600 | -91.6 | 504990 | 286 | -94.4 | 504990 | 640 |
| MR_1774414788_BF28581C | 152650 | 229 | -90.3 | 152650 | 938 | -96.4 | 152650 | 959 | -100.4 | 152650 | 889 |
| MR_1774414788_E96F2BCF | 152650 | 229 | -91.8 | 152650 | 938 | -94.4 | 152650 | 959 | -101.0 | 152650 | 889 |
| MR_1774414788_15D89B13 | 152650 | 229 | -91.8 | 152650 | 938 | -95.6 | 152650 | 959 | -101.7 | 152650 | 889 |
| MR_1774414788_8422D455 | 504990 | 697 | -92.8 | 504990 | 600 | -91.7 | 504990 | 286 | -97.1 | 504990 | 640 |
| MR_1774414788_48C6955E | 504990 | 697 | -92.5 | 504990 | 600 | -90.5 | 504990 | 286 | -97.3 | 504990 | 640 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1122: `8519b021-c96...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8519b021-c966-467f-90e1-23a923d7db37` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Add neighbor relationship between 3251300_1 and 3265099_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1122] topology](images/train_1122.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3271180_2 and 3265099_4
- `C2`: Lift the tilt angle of 3251300_1 by 10 degrees
- `C3`: Decrease transmission power for 3251300_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265099_4
- `C5`: Adjust the azimuth of 3251300_1 by 50 degrees
- `C6`: Decrease A3 Offset threshold for 3265099_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251300_1
- `C8`: Increase A3 Offset threshold for 3251300_1
- `C9`: Increase transmission power for 3265099_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251300_1
- `C11`: Adjust the azimuth of 3265099_4 by 34 degrees
- `C12`: Increase A3 Offset threshold for 3265099_4
- `C13`: Check test server and transmission issues
- `C14`: Increase transmission power for 3251300_1
- `C15`: Press down the tilt angle of 3251300_1 by 10 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Lift the tilt angle  of 3265099_4 by 6 degrees
- `C18`: Decrease A3 Offset threshold for 3251300_1
- `C19`: Decrease transmission power for 3265099_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265099_4
- `C21`: Press down the tilt angle  of 3265099_4 by 6 degrees
- `C22`: Add neighbor relationship between 3251300_1 and 3265099_4 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.746 | MS1 | 121.4656611536 | 31.1446299441 | 13 | 504990 | -76.60 | 14.59 | 400.93 | 0.06 | 2.72 | 1569 |
| 2024-09-20 22:21:32.279 | MS1 | 121.4656664385 | 31.1446345944 | 13 | 504990 | -78.86 | 13.91 | 456.02 | 0.19 | 2.57 | 1565 |
| 2024-09-20 22:21:33.399 | MS1 | 121.4656601037 | 31.1446187777 | 13 | 504990 | -84.15 | 13.64 | 529.22 | 0.09 | 2.56 | 1596 |
| 2024-09-20 22:21:34.654 | MS1 | 121.4656653630 | 31.1446300850 | 13 | 504990 | -86.42 | -0.13 | 41.06 | 0.07 | 1.14 | 1560 |
| 2024-09-20 22:21:35.869 | MS1 | 121.4656747230 | 31.1446378437 | 13 | 504990 | -93.93 | -0.72 | 46.84 | 0.16 | 1.36 | 1590 |
| 2024-09-20 22:21:36.483 | MS1 | 121.4656762537 | 31.1446242844 | 13 | 504990 | -92.40 | -3.54 | 54.25 | 0.14 | 1.20 | 1571 |
| 2024-09-20 22:21:37.144 | MS1 | 121.4656655504 | 31.1446250818 | 13 | 504990 | -90.51 | -3.41 | 54.41 | 0.16 | 1.22 | 1574 |
| 2024-09-20 22:21:38.127 | MS1 | 121.4656617242 | 31.1446375681 | 13 | 504990 | -76.38 | 13.54 | 556.85 | 0.03 | 1.48 | 1568 |
| 2024-09-20 22:21:39.695 | MS1 | 121.4656584489 | 31.1446322515 | 13 | 504990 | -81.67 | 12.69 | 403.56 | 0.08 | 1.28 | 1578 |
| 2024-09-20 22:21:40.310 | MS1 | 121.4656723668 | 31.1446221872 | 13 | 504990 | -75.88 | 16.49 | 431.10 | 0.20 | 2.04 | 1569 |
| 2024-09-20 22:21:41.916 | MS1 | 121.4656591314 | 31.1446348167 | 13 | 504990 | -84.64 | 12.34 | 356.60 | 0.02 | 2.88 | 1598 |
| 2024-09-20 22:21:42.760 | MS1 | 121.4656635009 | 31.1446262900 | 13 | 504990 | -79.16 | 14.26 | 572.87 | 0.18 | 2.75 | 1563 |

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
| 3251300 | 1 | 121.4729350334 | 31.1445965635 | 180 | 15 | 4 | 29.2 | TDD | 13 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3265099 | 4 | 121.4742858698 | 31.1473837977 | 284 | 4 | 1 | 24.5 | TDD | 189 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3271180 | 2 | 121.4725261620 | 31.1464351356 | 316 | 12 | 0 | 24.7 | TDD | 853 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3276927 | 3 | 121.4715879012 | 31.1551364360 | 295 | 5 | 9 | 38.9 | TDD | 438 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.297 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.314 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.453 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.453 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.164 | NREventA3 | measId:2;ServCellPCI:261;Se... |
| 2024-09-20 22:21:36.164 | NREventA3 | measId:2;ServCellPCI:261;Se... |
| 2024-09-20 22:21:37.164 | NREventA3 | measId:2;ServCellPCI:261;Se... |
| 2024-09-20 22:21:39.664 | NRRRCReestablishAttempt | PCI:261 |
| 2024-09-20 22:21:39.680 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.695 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.826 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.826 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251300 | 1 | 12.5535 | 15.4812 | -117.8300 | 18.3146 | 137.0785 | 0.0161 | 0.1875 |
| 2024_09_20 22:00 | 3271180 | 2 | 14.3297 | 14.3568 | -115.5022 | 14.2245 | 180.3495 | 0.0147 | 0.0128 |
| 2024_09_20 22:00 | 3276927 | 3 | 10.6050 | 10.0569 | -117.6678 | 13.1213 | 127.5387 | 0.0141 | 0.0036 |
| 2024_09_20 22:00 | 3265099 | 4 | 18.9875 | 16.1695 | -114.3417 | 5.8919 | 144.3250 | 0.0157 | 0.0027 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412307_8B7F28DB | 504990 | 189 | -84.0 | 504990 | 13 | -85.2 | 504990 | 853 | -84.9 | 504990 | 438 |
| MR_1774412307_BA0A9E50 | 504990 | 189 | -83.6 | 504990 | 13 | -86.5 | 504990 | 853 | -83.2 | 504990 | 438 |
| MR_1774412307_413DB30B | 504990 | 189 | -81.6 | 504990 | 13 | -84.5 | 504990 | 853 | -83.2 | 504990 | 438 |
| MR_1774412307_605509B8 | 504990 | 13 | -87.4 | 504990 | 189 | -81.0 | 504990 | 853 | -82.5 | 504990 | 438 |
| MR_1774412307_1D7B6145 | 504990 | 13 | -85.5 | 504990 | 189 | -81.8 | 504990 | 853 | -83.2 | 504990 | 438 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1123: `99baaed0-c68...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `99baaed0-c685-406b-827e-172364e58ade` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1123] topology](images/train_1123.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3221285_4 by 10 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262877_3
- `C3`: Adjust the azimuth of 3221285_4 by 50 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262877_3
- `C5`: Decrease A3 Offset threshold for 3262877_3
- `C6`: Increase A3 Offset threshold for 3262877_3
- `C7`: Increase transmission power for 3262877_3
- `C8`: Add neighbor relationship between 3253387_2 and 3262877_3
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Lift the tilt angle  of 3262877_3 by 10 degrees
- `C11`: Increase transmission power for 3221285_4
- `C12`: Decrease transmission power for 3262877_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221285_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221285_4
- `C15`: Press down the tilt angle  of 3262877_3 by 10 degrees
- `C16`: Decrease transmission power for 3221285_4
- `C17`: Check test server and transmission issues **← 정답**
- `C18`: Adjust the azimuth of 3262877_3 by 50 degrees
- `C19`: Increase A3 Offset threshold for 3221285_4
- `C20`: Lift the tilt angle of 3221285_4 by 10 degrees
- `C21`: Decrease A3 Offset threshold for 3221285_4
- `C22`: Add neighbor relationship between 3221285_4 and 3262877_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.493 | MS1 | 121.4656714323 | 31.1446189821 | 701 | 504990 | -87.87 | 13.01 | 390.90 | 0.04 | 2.52 | 1568 |
| 2024-09-20 22:21:32.547 | MS1 | 121.4656666901 | 31.1446293079 | 701 | 504990 | -87.82 | 13.45 | 297.91 | 0.15 | 2.39 | 1589 |
| 2024-09-20 22:21:33.161 | MS1 | 121.4656600064 | 31.1446311713 | 701 | 504990 | -89.26 | 16.08 | 566.56 | 0.16 | 2.93 | 1580 |
| 2024-09-20 22:21:34.396 | MS1 | 121.4656697954 | 31.1446299088 | 701 | 504990 | -86.30 | 17.38 | 47.62 | 0.01 | 2.34 | 345 |
| 2024-09-20 22:21:35.563 | MS1 | 121.4656661322 | 31.1446280166 | 701 | 504990 | -87.24 | 13.66 | 80.09 | 0.17 | 2.48 | 498 |
| 2024-09-20 22:21:36.269 | MS1 | 121.4656592810 | 31.1446364335 | 701 | 504990 | -86.17 | 17.26 | 100.37 | 0.07 | 2.90 | 329 |
| 2024-09-20 22:21:37.914 | MS1 | 121.4656605648 | 31.1446350132 | 701 | 504990 | -93.33 | 7.20 | 54.24 | 0.15 | 2.04 | 443 |
| 2024-09-20 22:21:38.466 | MS1 | 121.4656618689 | 31.1446357469 | 701 | 504990 | -89.71 | 9.96 | 87.23 | 0.16 | 2.46 | 498 |
| 2024-09-20 22:21:39.563 | MS1 | 121.4656772803 | 31.1446271810 | 701 | 504990 | -91.87 | 10.40 | 77.48 | 0.14 | 2.29 | 360 |
| 2024-09-20 22:21:40.548 | MS1 | 121.4656737951 | 31.1446269337 | 701 | 504990 | -91.29 | 11.67 | 417.33 | 0.17 | 2.02 | 1572 |
| 2024-09-20 22:21:41.290 | MS1 | 121.4656731061 | 31.1446290743 | 701 | 504990 | -91.63 | 8.48 | 502.83 | 0.16 | 2.27 | 1568 |
| 2024-09-20 22:21:42.988 | MS1 | 121.4656759553 | 31.1446252797 | 701 | 504990 | -89.01 | 11.62 | 479.86 | 0.08 | 2.82 | 1581 |

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
| 3221285 | 4 | 121.4640319824 | 31.1464336684 | 255 | 12 | 4 | 22.5 | TDD | 701 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3235131 | 1 | 121.4677867047 | 31.1545911825 | 344 | 2 | 3 | 38.0 | TDD | 736 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3253387 | 2 | 121.4745163730 | 31.1553872142 | 307 | 1 | 12 | 38.2 | TDD | 218 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3262877 | 3 | 121.4670949051 | 31.1476958295 | 333 | 13 | 2 | 29.4 | TDD | 747 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.098 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.120 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.252 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.252 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.908 | NREventA3 | measId:2;ServCellPCI:986;Se... |
| 2024-09-20 22:21:38.148 | NRHandoverAttempt | SourcePCI:986;SourceNR-ARFC... |
| 2024-09-20 22:21:38.190 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.204 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.353 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.353 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235131 | 1 | 11.0124 | 18.0982 | -116.7824 | 14.3578 | 93.6835 | 0.0122 | 0.0175 |
| 2024_09_20 22:00 | 3253387 | 2 | 10.1332 | 18.2464 | -116.8867 | 5.0275 | 196.8804 | 0.0128 | 0.0007 |
| 2024_09_20 22:00 | 3262877 | 3 | 18.4780 | 10.7836 | -116.8153 | 19.3669 | 179.5719 | 0.0099 | 0.0167 |
| 2024_09_20 22:00 | 3221285 | 4 | 9.8533 | 13.5754 | -114.5750 | 15.5466 | 155.1721 | 0.0181 | 0.0151 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416861_7A52354D | 504990 | 701 | -85.8 | 504990 | 747 | -89.7 | 504990 | 218 | -92.3 | 504990 | 736 |
| MR_1774416861_B2C11FDC | 504990 | 701 | -87.0 | 504990 | 747 | -92.4 | 504990 | 218 | -93.9 | 504990 | 736 |
| MR_1774416861_5088DF2B | 504990 | 701 | -86.3 | 504990 | 747 | -90.0 | 504990 | 218 | -92.8 | 504990 | 736 |
| MR_1774416861_402AF491 | 504990 | 701 | -86.7 | 504990 | 747 | -90.2 | 504990 | 218 | -93.7 | 504990 | 736 |
| MR_1774416861_7E83DC17 | 504990 | 701 | -86.9 | 504990 | 747 | -88.9 | 504990 | 218 | -95.0 | 504990 | 736 |
| MR_1774416861_3A618E1E | 504990 | 701 | -85.5 | 504990 | 747 | -90.1 | 504990 | 218 | -92.6 | 504990 | 736 |
| MR_1774416861_15E6B83B | 504990 | 701 | -86.4 | 504990 | 747 | -91.8 | 504990 | 218 | -93.3 | 504990 | 736 |
| MR_1774416861_232B727B | 504990 | 701 | -84.9 | 504990 | 747 | -89.9 | 504990 | 218 | -94.9 | 504990 | 736 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1124: `3a2053bc-168...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3a2053bc-168b-4b0d-964b-d274e2043d76` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease A3 Offset threshold for 3252652_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1124] topology](images/train_1124.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3220843_3 by 2 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220843_3
- `C3`: Press down the tilt angle of 3252652_2 by 10 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220843_3
- `C5`: Add neighbor relationship between 3252652_2 and 3220843_3
- `C6`: Increase A3 Offset threshold for 3220843_3
- `C7`: Decrease A3 Offset threshold for 3220843_3
- `C8`: Increase transmission power for 3220843_3
- `C9`: Adjust the azimuth of 3252652_2 by 50 degrees
- `C10`: Decrease A3 Offset threshold for 3252652_2 **← 정답**
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252652_2
- `C12`: Adjust the azimuth of 3220843_3 by 50 degrees
- `C13`: Decrease transmission power for 3220843_3
- `C14`: Check test server and transmission issues
- `C15`: Lift the tilt angle  of 3220843_3 by 2 degrees
- `C16`: Increase transmission power for 3252652_2
- `C17`: Decrease transmission power for 3252652_2
- `C18`: Add neighbor relationship between 3267826_4 and 3220843_3
- `C19`: Increase A3 Offset threshold for 3252652_2
- `C20`: Lift the tilt angle of 3252652_2 by 10 degrees
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252652_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.971 | MS1 | 121.4656764351 | 31.1446276530 | 623 | 504990 | -81.20 | 12.26 | 353.28 | 0.07 | 2.70 | 1597 |
| 2024-09-20 22:21:32.181 | MS1 | 121.4656687876 | 31.1446343810 | 623 | 504990 | -76.20 | 14.11 | 503.53 | 0.16 | 2.22 | 1582 |
| 2024-09-20 22:21:33.285 | MS1 | 121.4656617223 | 31.1446215905 | 623 | 504990 | -80.65 | 17.94 | 453.47 | 0.13 | 2.24 | 1574 |
| 2024-09-20 22:21:34.169 | MS1 | 121.4656652857 | 31.1446191152 | 623 | 504990 | -83.39 | -2.45 | 60.81 | 0.14 | 1.31 | 1563 |
| 2024-09-20 22:21:35.195 | MS1 | 121.4656648886 | 31.1446324244 | 623 | 504990 | -83.50 | -3.85 | 26.97 | 0.07 | 1.24 | 1579 |
| 2024-09-20 22:21:36.858 | MS1 | 121.4656662842 | 31.1446259438 | 623 | 504990 | -88.11 | -1.19 | 67.05 | 0.06 | 1.00 | 1587 |
| 2024-09-20 22:21:37.458 | MS1 | 121.4656693074 | 31.1446186391 | 623 | 504990 | -84.70 | -0.71 | 52.07 | 0.16 | 1.26 | 1597 |
| 2024-09-20 22:21:38.849 | MS1 | 121.4656768188 | 31.1446285132 | 623 | 504990 | -84.29 | -0.95 | 49.00 | 0.07 | 1.09 | 1566 |
| 2024-09-20 22:21:39.455 | MS1 | 121.4656643274 | 31.1446184056 | 366 | 504990 | -76.19 | 17.83 | 160.16 | 0.01 | 1.42 | 1584 |
| 2024-09-20 22:21:40.180 | MS1 | 121.4656626195 | 31.1446339142 | 366 | 504990 | -76.87 | 16.92 | 440.61 | 0.08 | 2.83 | 1593 |
| 2024-09-20 22:21:41.782 | MS1 | 121.4656723732 | 31.1446301710 | 366 | 504990 | -81.47 | 13.62 | 553.24 | 0.10 | 2.61 | 1568 |
| 2024-09-20 22:21:42.337 | MS1 | 121.4656631043 | 31.1446308866 | 366 | 504990 | -77.55 | 16.04 | 361.63 | 0.08 | 2.86 | 1563 |

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
| 3220843 | 3 | 121.4737131402 | 31.1532089495 | 322 | 1 | 4 | 21.0 | TDD | 366 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3252652 | 2 | 121.4686184562 | 31.1527875249 | 358 | 11 | 2 | 22.6 | TDD | 623 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3255644 | 1 | 121.4663880524 | 31.1460483365 | 2 | 4 | 10 | 47.0 | TDD | 898 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3267826 | 4 | 121.4669389088 | 31.1475145343 | 70 | 1 | 11 | 16.6 | TDD | 719 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.011 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.035 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.145 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.145 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.890 | NREventA3 | measId:2;ServCellPCI:199;Se... |
| 2024-09-20 22:21:38.130 | NRHandoverAttempt | SourcePCI:199;SourceNR-ARFC... |
| 2024-09-20 22:21:38.167 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.179 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.310 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.310 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255644 | 1 | 5.1248 | 10.2725 | -114.0386 | 11.8159 | 197.6211 | 0.0068 | 0.0186 |
| 2024_09_20 22:00 | 3252652 | 2 | 17.7288 | 13.9359 | -115.1765 | 13.4129 | 122.5601 | 0.0105 | 0.1129 |
| 2024_09_20 22:00 | 3220843 | 3 | 14.4626 | 11.0429 | -114.3304 | 16.7702 | 99.4597 | 0.0079 | 0.0077 |
| 2024_09_20 22:00 | 3267826 | 4 | 14.7251 | 13.2397 | -116.9289 | 7.7094 | 167.1461 | 0.0065 | 0.0135 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416555_D700F1A3 | 504990 | 623 | -81.7 | 504990 | 366 | -77.7 | 504990 | 719 | -84.6 | 504990 | 898 |
| MR_1774416555_72786D7F | 504990 | 623 | -82.0 | 504990 | 366 | -76.7 | 504990 | 719 | -83.1 | 504990 | 898 |
| MR_1774416555_2D6AC18A | 504990 | 366 | -79.6 | 504990 | 623 | -83.0 | 504990 | 719 | -84.7 | 504990 | 898 |
| MR_1774416555_CE94BDC7 | 504990 | 366 | -78.8 | 504990 | 623 | -82.9 | 504990 | 719 | -83.4 | 504990 | 898 |
| MR_1774416555_1CDE0E6A | 504990 | 623 | -83.0 | 504990 | 366 | -76.9 | 504990 | 719 | -82.6 | 504990 | 898 |
| MR_1774416555_6D3837BD | 504990 | 366 | -77.0 | 504990 | 623 | -81.7 | 504990 | 719 | -83.3 | 504990 | 898 |
| MR_1774416555_465CAA80 | 504990 | 366 | -77.8 | 504990 | 623 | -83.4 | 504990 | 719 | -82.2 | 504990 | 898 |
| MR_1774416555_05A88CCC | 504990 | 366 | -78.7 | 504990 | 623 | -81.5 | 504990 | 719 | -84.6 | 504990 | 898 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1125: `2d8f1e7e-06c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2d8f1e7e-06c2-4799-87cd-75a4a46a9f72` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1125] topology](images/train_1125.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Adjust the azimuth of 3279880_2 by 50 degrees
- `C3`: Increase A3 Offset threshold for 3279880_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279880_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249855_1
- `C6`: Adjust the azimuth of 3249855_1 by 50 degrees
- `C7`: Press down the tilt angle of 3279880_2 by 10 degrees
- `C8`: Press down the tilt angle  of 3249855_1 by 10 degrees
- `C9`: Add neighbor relationship between 3245891_3 and 3249855_1
- `C10`: Check test server and transmission issues **← 정답**
- `C11`: Increase A3 Offset threshold for 3249855_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249855_1
- `C13`: Lift the tilt angle  of 3249855_1 by 10 degrees
- `C14`: Lift the tilt angle of 3279880_2 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3279880_2
- `C16`: Increase transmission power for 3279880_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279880_2
- `C18`: Increase transmission power for 3249855_1
- `C19`: Decrease A3 Offset threshold for 3249855_1
- `C20`: Decrease transmission power for 3279880_2
- `C21`: Add neighbor relationship between 3279880_2 and 3249855_1
- `C22`: Decrease transmission power for 3249855_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.549 | MS1 | 121.4656612931 | 31.1446369302 | 444 | 504990 | -88.95 | 14.68 | 417.37 | 0.09 | 2.18 | 1592 |
| 2024-09-20 22:21:32.309 | MS1 | 121.4656663200 | 31.1446268689 | 444 | 504990 | -88.37 | 16.82 | 364.59 | 0.13 | 2.42 | 1560 |
| 2024-09-20 22:21:33.998 | MS1 | 121.4656753361 | 31.1446327102 | 444 | 504990 | -89.14 | 14.41 | 459.85 | 0.12 | 2.73 | 1587 |
| 2024-09-20 22:21:34.865 | MS1 | 121.4656626423 | 31.1446294450 | 444 | 504990 | -87.12 | 16.71 | 82.36 | 0.08 | 2.21 | 430 |
| 2024-09-20 22:21:35.346 | MS1 | 121.4656723197 | 31.1446265458 | 444 | 504990 | -88.32 | 17.77 | 96.08 | 0.01 | 2.12 | 348 |
| 2024-09-20 22:21:36.498 | MS1 | 121.4656657552 | 31.1446216493 | 444 | 504990 | -90.02 | 16.74 | 80.17 | 0.13 | 2.43 | 306 |
| 2024-09-20 22:21:37.430 | MS1 | 121.4656663230 | 31.1446272984 | 444 | 504990 | -92.04 | 12.80 | 66.90 | 0.04 | 2.87 | 431 |
| 2024-09-20 22:21:38.106 | MS1 | 121.4656620967 | 31.1446217195 | 444 | 504990 | -90.19 | 12.95 | 92.64 | 0.05 | 2.46 | 441 |
| 2024-09-20 22:21:39.314 | MS1 | 121.4656636822 | 31.1446307304 | 444 | 504990 | -93.74 | 9.93 | 85.01 | 0.13 | 2.46 | 369 |
| 2024-09-20 22:21:40.148 | MS1 | 121.4656657971 | 31.1446181411 | 444 | 504990 | -89.84 | 10.04 | 489.21 | 0.12 | 2.39 | 1573 |
| 2024-09-20 22:21:41.889 | MS1 | 121.4656709878 | 31.1446366486 | 444 | 504990 | -91.81 | 9.02 | 432.28 | 0.13 | 2.22 | 1564 |
| 2024-09-20 22:21:42.858 | MS1 | 121.4656594753 | 31.1446182832 | 444 | 504990 | -92.26 | 11.38 | 379.02 | 0.07 | 2.50 | 1568 |

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
| 3245891 | 3 | 121.4726703053 | 31.1457448534 | 128 | 7 | 11 | 22.8 | TDD | 637 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3249855 | 1 | 121.4676119593 | 31.1449919841 | 162 | 10 | 7 | 38.7 | TDD | 256 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3259955 | 4 | 121.4706233697 | 31.1505133347 | 322 | 14 | 11 | 36.3 | TDD | 519 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3279880 | 2 | 121.4658311890 | 31.1468514483 | 4 | 9 | 7 | 21.8 | TDD | 444 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.055 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.074 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.209 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.209 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.939 | NREventA3 | measId:2;ServCellPCI:906;Se... |
| 2024-09-20 22:21:38.179 | NRHandoverAttempt | SourcePCI:906;SourceNR-ARFC... |
| 2024-09-20 22:21:38.222 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.234 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.358 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.358 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249855 | 1 | 18.5137 | 13.4332 | -115.1253 | 13.3538 | 98.8227 | 0.0154 | 0.0052 |
| 2024_09_20 22:00 | 3279880 | 2 | 7.8656 | 6.5598 | -116.7521 | 13.7982 | 146.4507 | 0.0162 | 0.0128 |
| 2024_09_20 22:00 | 3245891 | 3 | 5.1718 | 6.0354 | -115.3393 | 17.5927 | 126.3504 | 0.0161 | 0.0171 |
| 2024_09_20 22:00 | 3259955 | 4 | 17.0915 | 8.7943 | -114.6456 | 11.7561 | 123.0700 | 0.0127 | 0.0074 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413871_B5A16BB0 | 504990 | 444 | -88.9 | 504990 | 256 | -88.0 | 504990 | 637 | -96.0 | 504990 | 519 |
| MR_1774413871_5451FBBD | 504990 | 444 | -86.7 | 504990 | 256 | -89.6 | 504990 | 637 | -95.3 | 504990 | 519 |
| MR_1774413871_CC737C59 | 504990 | 444 | -87.5 | 504990 | 256 | -88.2 | 504990 | 637 | -95.7 | 504990 | 519 |
| MR_1774413871_538D729D | 504990 | 444 | -88.6 | 504990 | 256 | -88.1 | 504990 | 637 | -95.1 | 504990 | 519 |
| MR_1774413871_84EECAC2 | 504990 | 444 | -87.2 | 504990 | 256 | -89.4 | 504990 | 637 | -96.5 | 504990 | 519 |
| MR_1774413871_9D4FDFBD | 504990 | 444 | -87.6 | 504990 | 256 | -90.7 | 504990 | 637 | -95.1 | 504990 | 519 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1126: `ccb103e9-99b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ccb103e9-99bd-4c80-b488-d5230ebffdee` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Lift the tilt angle  of 3264565_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1126] topology](images/train_1126.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3249533_2
- `C2`: Decrease transmission power for 3249533_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249533_2
- `C4`: Increase transmission power for 3249533_2
- `C5`: Decrease A3 Offset threshold for 3276453_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276453_4
- `C7`: Add neighbor relationship between 3264565_1 and 3276453_4
- `C8`: Add neighbor relationship between 3249533_2 and 3276453_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249533_2
- `C10`: Adjust the azimuth of 3249533_2 by 47 degrees
- `C11`: Decrease transmission power for 3276453_4
- `C12`: Press down the tilt angle of 3249533_2 by 4 degrees
- `C13`: Lift the tilt angle of 3249533_2 by 4 degrees
- `C14`: Lift the tilt angle  of 3264565_1 by 10 degrees **← 정답**
- `C15`: Adjust the azimuth of 3264565_1 by 50 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease A3 Offset threshold for 3249533_2
- `C18`: Increase A3 Offset threshold for 3276453_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276453_4
- `C20`: Increase transmission power for 3276453_4
- `C21`: Check test server and transmission issues
- `C22`: Press down the tilt angle  of 3264565_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.166 | MS1 | 121.4656752981 | 31.1446313125 | 34 | 504990 | -91.53 | 14.38 | 399.65 | 0.01 | 2.12 | 1592 |
| 2024-09-20 22:21:32.441 | MS1 | 121.4656662009 | 31.1446302467 | 34 | 504990 | -86.82 | 17.02 | 517.95 | 0.01 | 2.42 | 1589 |
| 2024-09-20 22:21:33.388 | MS1 | 121.4656692853 | 31.1446244390 | 34 | 504990 | -88.92 | 17.17 | 313.10 | 0.09 | 2.58 | 1566 |
| 2024-09-20 22:21:34.527 | MS1 | 121.4656689054 | 31.1446321737 | 34 | 504990 | -89.55 | 12.17 | 76.57 | 0.09 | 2.92 | 1584 |
| 2024-09-20 22:21:35.126 | MS1 | 121.4656640033 | 31.1446362325 | 34 | 504990 | -89.30 | 13.06 | 90.64 | 0.15 | 2.04 | 1581 |
| 2024-09-20 22:21:36.710 | MS1 | 121.4656681974 | 31.1446299201 | 34 | 504990 | -89.67 | 13.46 | 88.90 | 0.05 | 2.61 | 1573 |
| 2024-09-20 22:21:37.287 | MS1 | 121.4656669326 | 31.1446224123 | 34 | 504990 | -90.13 | 10.63 | 89.64 | 0.01 | 2.68 | 1600 |
| 2024-09-20 22:21:38.635 | MS1 | 121.4656679465 | 31.1446314910 | 34 | 504990 | -91.06 | 10.01 | 98.55 | 0.02 | 2.82 | 1573 |
| 2024-09-20 22:21:39.552 | MS1 | 121.4656650353 | 31.1446215067 | 34 | 504990 | -92.88 | 11.62 | 88.81 | 0.09 | 2.25 | 1578 |
| 2024-09-20 22:21:40.954 | MS1 | 121.4656679336 | 31.1446328459 | 34 | 504990 | -92.47 | 10.37 | 306.19 | 0.07 | 2.33 | 1574 |
| 2024-09-20 22:21:41.200 | MS1 | 121.4656713792 | 31.1446287821 | 34 | 504990 | -90.15 | 7.91 | 575.74 | 0.16 | 2.39 | 1568 |
| 2024-09-20 22:21:42.780 | MS1 | 121.4656659118 | 31.1446333480 | 34 | 504990 | -91.07 | 11.06 | 310.33 | 0.13 | 2.22 | 1575 |

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
| 3249533 | 2 | 121.4670760814 | 31.1548965482 | 140 | 2 | 11 | 34.7 | TDD | 34 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3264565 | 1 | 121.4729831542 | 31.1505723355 | 17 | 9 | 5 | 36.5 | TDD | 418 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3270247 | 3 | 121.4646342430 | 31.1488175110 | 226 | 5 | 3 | 30.6 | TDD | 77 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3276453 | 4 | 121.4753322963 | 31.1464430949 | 30 | 14 | 12 | 42.9 | TDD | 87 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.133 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.157 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.268 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.268 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.959 | NREventA3 | measId:2;ServCellPCI:552;Se... |
| 2024-09-20 22:21:38.199 | NRHandoverAttempt | SourcePCI:552;SourceNR-ARFC... |
| 2024-09-20 22:21:38.243 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.253 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.398 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.398 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264565 | 1 | 11.1838 | 19.6839 | -115.8199 | 9.3312 | 197.1368 | 0.0031 | 0.0112 |
| 2024_09_20 22:00 | 3249533 | 2 | 78.4069 | 83.1527 | -115.7670 | 14.7666 | 154.9635 | 0.0092 | 0.0169 |
| 2024_09_20 22:00 | 3270247 | 3 | 16.8291 | 8.7108 | -116.9022 | 11.1117 | 186.9161 | 0.0106 | 0.0161 |
| 2024_09_20 22:00 | 3276453 | 4 | 15.9031 | 15.8950 | -115.2547 | 9.0260 | 99.2163 | 0.0117 | 0.0140 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415829_ED0F2F71 | 504990 | 34 | -88.9 | 504990 | 87 | -93.3 | 504990 | 418 | -104.0 | 504990 | 77 |
| MR_1774415829_4BBF8352 | 504990 | 34 | -90.5 | 504990 | 87 | -91.8 | 504990 | 418 | -106.1 | 504990 | 77 |
| MR_1774415829_E38F585F | 504990 | 34 | -89.3 | 504990 | 87 | -91.9 | 504990 | 418 | -104.9 | 504990 | 77 |
| MR_1774415829_6A8B1A3A | 504990 | 34 | -89.1 | 504990 | 87 | -94.3 | 504990 | 418 | -103.0 | 504990 | 77 |
| MR_1774415829_3B09BDD1 | 504990 | 34 | -88.3 | 504990 | 87 | -91.9 | 504990 | 418 | -104.2 | 504990 | 77 |
| MR_1774415829_B6460D0C | 504990 | 34 | -88.1 | 504990 | 87 | -94.8 | 504990 | 418 | -105.0 | 504990 | 77 |
| MR_1774415829_15F5291C | 504990 | 34 | -88.6 | 504990 | 87 | -94.7 | 504990 | 418 | -102.9 | 504990 | 77 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1127: `01713429-65b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `01713429-65bd-4735-a65e-07d0334a1c40` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3266336_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1127] topology](images/train_1127.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3266336_3
- `C2`: Decrease transmission power for 3261095_1
- `C3`: Press down the tilt angle of 3266336_3 by 4 degrees
- `C4`: Check test server and transmission issues
- `C5`: Lift the tilt angle of 3266336_3 by 4 degrees
- `C6`: Press down the tilt angle  of 3261095_1 by 2 degrees
- `C7`: Adjust the azimuth of 3266336_3 by 17 degrees
- `C8`: Decrease A3 Offset threshold for 3261095_1
- `C9`: Add neighbor relationship between 3234431_4 and 3261095_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266336_3 **← 정답**
- `C11`: Increase A3 Offset threshold for 3261095_1
- `C12`: Adjust the azimuth of 3261095_1 by 50 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Increase transmission power for 3261095_1
- `C15`: Increase transmission power for 3266336_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266336_3
- `C17`: Add neighbor relationship between 3266336_3 and 3261095_1
- `C18`: Increase A3 Offset threshold for 3266336_3
- `C19`: Decrease transmission power for 3266336_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261095_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261095_1
- `C22`: Lift the tilt angle  of 3261095_1 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.393 | MS1 | 121.4656687868 | 31.1446305356 | 692 | 504990 | -87.24 | 17.40 | 604.23 | 0.17 | 2.51 | 1563 |
| 2024-09-20 22:21:32.298 | MS1 | 121.4656754314 | 31.1446253157 | 692 | 504990 | -86.68 | 12.01 | 467.65 | 0.12 | 2.60 | 1590 |
| 2024-09-20 22:21:33.422 | MS1 | 121.4656599686 | 31.1446236747 | 692 | 504990 | -85.48 | 16.76 | 555.73 | 0.03 | 2.18 | 1592 |
| 2024-09-20 22:21:34.161 | MS1 | 121.4656596578 | 31.1446201277 | 692 | 504990 | -88.49 | 12.87 | 69.59 | 0.50 | 2.19 | 562 |
| 2024-09-20 22:21:35.763 | MS1 | 121.4656670357 | 31.1446219916 | 692 | 504990 | -85.91 | 14.01 | 80.62 | 0.66 | 2.85 | 681 |
| 2024-09-20 22:21:36.243 | MS1 | 121.4656696172 | 31.1446312349 | 692 | 504990 | -91.75 | 15.77 | 98.81 | 0.69 | 2.12 | 549 |
| 2024-09-20 22:21:37.181 | MS1 | 121.4656600343 | 31.1446226104 | 692 | 504990 | -91.93 | 7.38 | 58.91 | 0.65 | 2.76 | 591 |
| 2024-09-20 22:21:38.372 | MS1 | 121.4656636958 | 31.1446214680 | 692 | 504990 | -92.96 | 12.76 | 79.95 | 0.57 | 2.87 | 651 |
| 2024-09-20 22:21:39.981 | MS1 | 121.4656643024 | 31.1446313238 | 692 | 504990 | -90.96 | 10.54 | 66.03 | 0.54 | 2.82 | 656 |
| 2024-09-20 22:21:40.291 | MS1 | 121.4656647332 | 31.1446358790 | 692 | 504990 | -92.28 | 9.16 | 379.47 | 0.03 | 2.08 | 1595 |
| 2024-09-20 22:21:41.690 | MS1 | 121.4656668747 | 31.1446377658 | 692 | 504990 | -90.62 | 10.49 | 532.41 | 0.06 | 2.05 | 1566 |
| 2024-09-20 22:21:42.184 | MS1 | 121.4656688687 | 31.1446199454 | 692 | 504990 | -90.61 | 11.82 | 331.03 | 0.00 | 2.49 | 1583 |

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
| 3227400 | 2 | 121.4669312659 | 31.1526548607 | 7 | 1 | 0 | 44.7 | TDD | 283 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3234431 | 4 | 121.4690004052 | 31.1496401746 | 243 | 1 | 12 | 27.5 | TDD | 361 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3261095 | 1 | 121.4648398447 | 31.1524276899 | 17 | 0 | 3 | 35.5 | TDD | 617 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3266336 | 3 | 121.4674465296 | 31.1547300930 | 206 | 2 | 4 | 42.4 | TDD | 692 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.499 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.521 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.625 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.625 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.313 | NREventA3 | measId:2;ServCellPCI:87;Ser... |
| 2024-09-20 22:21:38.553 | NRHandoverAttempt | SourcePCI:87;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.593 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.607 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.749 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.749 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261095 | 1 | 6.8589 | 19.7802 | -116.4422 | 15.7422 | 111.4948 | 0.0120 | 0.0063 |
| 2024_09_20 22:00 | 3227400 | 2 | 13.2506 | 17.4744 | -117.4142 | 10.3434 | 181.6090 | 0.0133 | 0.0047 |
| 2024_09_20 22:00 | 3266336 | 3 | 19.4874 | 18.3933 | -116.9648 | 19.8642 | 158.9073 | 0.0083 | 0.0169 |
| 2024_09_20 22:00 | 3234431 | 4 | 10.9757 | 15.2210 | -116.1829 | 5.1408 | 133.3794 | 0.0041 | 0.0129 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416788_E6C66167 | 504990 | 692 | -90.4 | 504990 | 617 | -91.4 | 504990 | 361 | -98.2 | 504990 | 283 |
| MR_1774416788_1B99DB00 | 504990 | 692 | -89.1 | 504990 | 617 | -93.5 | 504990 | 361 | -97.0 | 504990 | 283 |
| MR_1774416788_91BC83C0 | 504990 | 692 | -88.2 | 504990 | 617 | -92.8 | 504990 | 361 | -97.3 | 504990 | 283 |
| MR_1774416788_99CAAA22 | 504990 | 692 | -89.7 | 504990 | 617 | -93.3 | 504990 | 361 | -95.1 | 504990 | 283 |
| MR_1774416788_311A0EA8 | 504990 | 692 | -89.7 | 504990 | 617 | -93.5 | 504990 | 361 | -96.7 | 504990 | 283 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1128: `38977302-7e0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `38977302-7e00-48bd-bc2e-1c9721ff685f` |
| Tag | **multiple-answer** |
| 정답 | **C1|C2** |
| C1 의미 | Adjust the azimuth of 3272977_4 by 50 degrees |
| C2 의미 | Increase transmission power for 3272977_4 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1128] topology](images/train_1128.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3272977_4 by 50 degrees **← 정답**
- `C2`: Increase transmission power for 3272977_4 **← 정답**
- `C3`: Add neighbor relationship between 3272977_4 and 3261577_3
- `C4`: Decrease transmission power for 3261577_3
- `C5`: Add neighbor relationship between 3249702_1 and 3261577_3
- `C6`: Increase A3 Offset threshold for 3272977_4
- `C7`: Decrease A3 Offset threshold for 3261577_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261577_3
- `C9`: Increase transmission power for 3261577_3
- `C10`: Decrease transmission power for 3272977_4
- `C11`: Press down the tilt angle  of 3261577_3 by 2 degrees
- `C12`: Check test server and transmission issues
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Lift the tilt angle of 3272977_4 by 10 degrees
- `C15`: Adjust the azimuth of 3261577_3 by 33 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272977_4
- `C17`: Lift the tilt angle  of 3261577_3 by 2 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261577_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272977_4
- `C20`: Press down the tilt angle of 3272977_4 by 10 degrees
- `C21`: Decrease A3 Offset threshold for 3272977_4
- `C22`: Increase A3 Offset threshold for 3261577_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.353 | MS1 | 121.4656612508 | 31.1446224705 | 719 | 504990 | -87.04 | 12.76 | 414.80 | 0.13 | 2.50 | 1566 |
| 2024-09-20 22:21:32.152 | MS1 | 121.4656763060 | 31.1446231909 | 719 | 504990 | -85.29 | 17.96 | 342.09 | 0.08 | 2.79 | 1600 |
| 2024-09-20 22:21:33.197 | MS1 | 121.4656591953 | 31.1446361996 | 719 | 504990 | -93.05 | 15.13 | 444.89 | 0.17 | 2.41 | 1566 |
| 2024-09-20 22:21:34.822 | MS1 | 121.4656742189 | 31.1446278635 | 719 | 504990 | -106.59 | 1.26 | 27.68 | 0.03 | 1.21 | 1578 |
| 2024-09-20 22:21:35.492 | MS1 | 121.4656706834 | 31.1446201878 | 719 | 504990 | -103.87 | -0.66 | 73.83 | 0.06 | 1.30 | 1591 |
| 2024-09-20 22:21:36.712 | MS1 | 121.4656636979 | 31.1446356565 | 719 | 504990 | -106.05 | 1.93 | 22.46 | 0.02 | 1.42 | 1566 |
| 2024-09-20 22:21:37.359 | MS1 | 121.4656701600 | 31.1446186172 | 719 | 504990 | -103.61 | -0.13 | 37.13 | 0.05 | 1.30 | 1600 |
| 2024-09-20 22:21:38.906 | MS1 | 121.4656731442 | 31.1446300523 | 719 | 504990 | -109.24 | -0.86 | 36.15 | 0.18 | 1.06 | 1592 |
| 2024-09-20 22:21:39.900 | MS1 | 121.4656760545 | 31.1446290878 | 719 | 504990 | -108.10 | -1.60 | 35.79 | 0.08 | 1.41 | 1577 |
| 2024-09-20 22:21:40.124 | MS1 | 121.4656650458 | 31.1446224415 | 719 | 504990 | -94.65 | 17.38 | 489.46 | 0.18 | 2.15 | 1580 |
| 2024-09-20 22:21:41.406 | MS1 | 121.4656726871 | 31.1446197653 | 719 | 504990 | -87.50 | 16.30 | 362.50 | 0.17 | 2.89 | 1574 |
| 2024-09-20 22:21:42.603 | MS1 | 121.4656754958 | 31.1446369913 | 719 | 504990 | -91.43 | 13.60 | 468.55 | 0.04 | 2.87 | 1590 |

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
| 3249702 | 1 | 121.4729789436 | 31.1498224707 | 355 | 0 | 6 | 29.9 | TDD | 65 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3261577 | 3 | 121.4758902097 | 31.1496902153 | 273 | 0 | 2 | 36.3 | TDD | 764 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3272977 | 4 | 121.4690812193 | 31.1523708799 | 135 | 11 | 0 | 29.5 | TDD | 719 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3274510 | 2 | 121.4707494498 | 31.1513081653 | 43 | 12 | 7 | 28.9 | TDD | 692 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.196 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.215 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.338 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.338 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.523 | NREventA2 | measId:1;ServCellPCI:723;Se... |
| 2024-09-20 22:21:34.630 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249702 | 1 | 19.6254 | 7.9144 | -115.8522 | 7.2642 | 171.5654 | 0.0148 | 0.0064 |
| 2024_09_20 22:00 | 3274510 | 2 | 12.7780 | 7.8789 | -115.9979 | 13.3719 | 99.1284 | 0.0043 | 0.0077 |
| 2024_09_20 22:00 | 3261577 | 3 | 10.9278 | 6.8669 | -116.4371 | 9.1645 | 150.6389 | 0.0107 | 0.0181 |
| 2024_09_20 22:00 | 3272977 | 4 | 15.8691 | 12.2972 | -116.8616 | 9.8335 | 188.7387 | 0.1258 | 0.0005 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412234_C72A348E | 504990 | 719 | -107.6 | 504990 | 764 | -110.8 | 504990 | 65 | -116.8 | 504990 | 692 |
| MR_1774412234_3591B63A | 504990 | 719 | -106.7 | 504990 | 764 | -112.8 | 504990 | 65 | -117.9 | 504990 | 692 |
| MR_1774412234_F8FDAA48 | 504990 | 719 | -105.8 | 504990 | 764 | -110.3 | 504990 | 65 | -117.0 | 504990 | 692 |
| MR_1774412234_C4294C68 | 504990 | 719 | -108.3 | 504990 | 764 | -110.6 | 504990 | 65 | -118.5 | 504990 | 692 |
| MR_1774412234_E6D82280 | 504990 | 719 | -107.2 | 504990 | 764 | -110.4 | 504990 | 65 | -115.5 | 504990 | 692 |
| MR_1774412234_B5811038 | 504990 | 719 | -105.0 | 504990 | 764 | -112.0 | 504990 | 65 | -118.8 | 504990 | 692 |
| MR_1774412234_C3B2FC32 | 504990 | 719 | -106.3 | 504990 | 764 | -109.8 | 504990 | 65 | -115.5 | 504990 | 692 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1129: `aa08e309-a55...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `aa08e309-a55e-457a-8d01-7ccf506b1538` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease A3 Offset threshold for 3238968_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1129] topology](images/train_1129.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3238968_1
- `C2`: Lift the tilt angle of 3238968_1 by 10 degrees
- `C3`: Add neighbor relationship between 3238968_1 and 3253774_3
- `C4`: Increase transmission power for 3253774_3
- `C5`: Add neighbor relationship between 3231950_4 and 3253774_3
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase A3 Offset threshold for 3253774_3
- `C8`: Adjust the azimuth of 3238968_1 by 50 degrees
- `C9`: Decrease transmission power for 3253774_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253774_3
- `C11`: Increase transmission power for 3238968_1
- `C12`: Check test server and transmission issues
- `C13`: Decrease A3 Offset threshold for 3238968_1 **← 정답**
- `C14`: Lift the tilt angle  of 3253774_3 by 3 degrees
- `C15`: Adjust the azimuth of 3253774_3 by 50 degrees
- `C16`: Decrease A3 Offset threshold for 3253774_3
- `C17`: Press down the tilt angle  of 3253774_3 by 3 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238968_1
- `C19`: Press down the tilt angle of 3238968_1 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3238968_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253774_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238968_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.592 | MS1 | 121.4656658783 | 31.1446259408 | 416 | 504990 | -77.04 | 13.77 | 489.12 | 0.05 | 2.02 | 1570 |
| 2024-09-20 22:21:32.966 | MS1 | 121.4656601207 | 31.1446350783 | 416 | 504990 | -76.23 | 16.54 | 370.54 | 0.05 | 2.52 | 1573 |
| 2024-09-20 22:21:33.759 | MS1 | 121.4656691647 | 31.1446252351 | 416 | 504990 | -76.62 | 12.12 | 587.66 | 0.14 | 2.23 | 1593 |
| 2024-09-20 22:21:34.586 | MS1 | 121.4656623497 | 31.1446350926 | 416 | 504990 | -83.70 | -2.01 | 61.94 | 0.08 | 1.32 | 1576 |
| 2024-09-20 22:21:35.930 | MS1 | 121.4656599013 | 31.1446331638 | 416 | 504990 | -86.75 | -2.41 | 64.21 | 0.15 | 1.14 | 1586 |
| 2024-09-20 22:21:36.684 | MS1 | 121.4656773786 | 31.1446211266 | 416 | 504990 | -90.54 | -3.21 | 39.72 | 0.12 | 1.48 | 1566 |
| 2024-09-20 22:21:37.286 | MS1 | 121.4656659925 | 31.1446307465 | 416 | 504990 | -89.49 | -2.54 | 47.45 | 0.01 | 1.23 | 1600 |
| 2024-09-20 22:21:38.572 | MS1 | 121.4656604747 | 31.1446209416 | 416 | 504990 | -86.13 | -3.55 | 53.91 | 0.02 | 1.12 | 1575 |
| 2024-09-20 22:21:39.801 | MS1 | 121.4656685497 | 31.1446248956 | 550 | 504990 | -84.38 | 12.94 | 177.64 | 0.18 | 1.04 | 1599 |
| 2024-09-20 22:21:40.848 | MS1 | 121.4656750520 | 31.1446313272 | 550 | 504990 | -83.60 | 17.13 | 565.67 | 0.16 | 2.90 | 1599 |
| 2024-09-20 22:21:41.981 | MS1 | 121.4656682911 | 31.1446198233 | 550 | 504990 | -81.82 | 16.46 | 530.71 | 0.05 | 2.28 | 1573 |
| 2024-09-20 22:21:42.842 | MS1 | 121.4656584257 | 31.1446203904 | 550 | 504990 | -80.05 | 16.26 | 468.71 | 0.13 | 2.99 | 1587 |

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
| 3229587 | 2 | 121.4731175171 | 31.1547348527 | 217 | 15 | 1 | 49.6 | TDD | 803 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3231950 | 4 | 121.4693756002 | 31.1471156753 | 349 | 2 | 10 | 31.8 | TDD | 63 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3238968 | 1 | 121.4667416608 | 31.1447074782 | 96 | 1 | 11 | 19.2 | TDD | 416 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3253774 | 3 | 121.4706613087 | 31.1476381644 | 13 | 1 | 0 | 16.1 | TDD | 550 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.105 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.123 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.258 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.258 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.964 | NREventA3 | measId:2;ServCellPCI:550;Se... |
| 2024-09-20 22:21:38.204 | NRHandoverAttempt | SourcePCI:550;SourceNR-ARFC... |
| 2024-09-20 22:21:38.240 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.255 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.404 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.404 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238968 | 1 | 12.0920 | 17.1174 | -114.9230 | 15.0439 | 96.4562 | 0.0036 | 0.1408 |
| 2024_09_20 22:00 | 3229587 | 2 | 9.3993 | 17.3960 | -116.2087 | 10.5228 | 154.0044 | 0.0162 | 0.0083 |
| 2024_09_20 22:00 | 3253774 | 3 | 5.0738 | 8.2768 | -115.5174 | 15.7853 | 138.1968 | 0.0004 | 0.0153 |
| 2024_09_20 22:00 | 3231950 | 4 | 7.4964 | 15.3655 | -117.4832 | 13.6666 | 175.5934 | 0.0101 | 0.0114 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412146_0C4148BA | 504990 | 550 | -78.1 | 504990 | 416 | -83.1 | 504990 | 63 | -78.6 | 504990 | 803 |
| MR_1774412146_662B3273 | 504990 | 416 | -84.8 | 504990 | 550 | -78.8 | 504990 | 63 | -79.4 | 504990 | 803 |
| MR_1774412146_0D1E2D67 | 504990 | 416 | -83.5 | 504990 | 550 | -76.8 | 504990 | 63 | -80.7 | 504990 | 803 |
| MR_1774412146_2B917A8E | 504990 | 416 | -82.0 | 504990 | 550 | -76.7 | 504990 | 63 | -77.2 | 504990 | 803 |
| MR_1774412146_82882AB3 | 504990 | 550 | -78.3 | 504990 | 416 | -83.3 | 504990 | 63 | -79.5 | 504990 | 803 |

> *... 2개 열 생략 (전체 14열)*

---
