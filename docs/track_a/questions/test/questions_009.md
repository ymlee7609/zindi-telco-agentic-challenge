# Track A 문제 분석 — test[80]~test[89]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[80] ~ test[89] (10개)

## 목차

1. [문제 80: `77d3f5dc-c22...`](#80) — single-answer
2. [문제 81: `b5bae666-8ee...`](#81) — single-answer
3. [문제 82: `5b201c1f-ee2...`](#82) — single-answer
4. [문제 83: `a076ba35-44f...`](#83) — single-answer
5. [문제 84: `9e437b0e-5f2...`](#84) — single-answer
6. [문제 85: `c01e3a7d-43e...`](#85) — single-answer
7. [문제 86: `adda9a54-7e7...`](#86) — single-answer
8. [문제 87: `fa4937c5-34b...`](#87) — single-answer
9. [문제 88: `1c282cf8-9d8...`](#88) — single-answer
10. [문제 89: `446ed34a-944...`](#89) — single-answer

---

### 문제 80: `77d3f5dc-c22...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `77d3f5dc-c229-4480-86f4-f915b2771bbf` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[80] topology](images/test_0080.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3276702_1 and 3251701_4
- `C2`: Lift the tilt angle of 3261501_2 by 10 degrees
- `C3`: Decrease transmission power for 3251701_4
- `C4`: Add neighbor relationship between 3261501_2 and 3251701_4
- `C5`: Decrease transmission power for 3261501_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261501_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251701_4
- `C8`: Check test server and transmission issues
- `C9`: Increase transmission power for 3261501_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251701_4
- `C11`: Press down the tilt angle of 3261501_2 by 10 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease A3 Offset threshold for 3261501_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261501_2
- `C15`: Increase A3 Offset threshold for 3261501_2
- `C16`: Press down the tilt angle  of 3251701_4 by 8 degrees
- `C17`: Lift the tilt angle  of 3251701_4 by 8 degrees
- `C18`: Increase A3 Offset threshold for 3251701_4
- `C19`: Increase transmission power for 3251701_4
- `C20`: Adjust the azimuth of 3261501_2 by 50 degrees
- `C21`: Adjust the azimuth of 3251701_4 by 20 degrees
- `C22`: Decrease A3 Offset threshold for 3251701_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.929 | MS1 | 121.4656710923 | 31.1446297913 | 290 | 504990 | -83.63 | 13.79 | 570.54 | 0.18 | 2.76 | 1598 |
| 2024-09-20 22:21:32.459 | MS1 | 121.4656709370 | 31.1446207257 | 290 | 504990 | -84.89 | 12.83 | 414.70 | 0.15 | 2.03 | 1580 |
| 2024-09-20 22:21:33.167 | MS1 | 121.4656611811 | 31.1446358520 | 290 | 504990 | -83.24 | 14.39 | 524.07 | 0.03 | 2.18 | 1584 |
| 2024-09-20 22:21:34.782 | MS1 | 121.4656673010 | 31.1446205410 | 290 | 504990 | -87.46 | -2.08 | 72.78 | 0.19 | 1.00 | 1583 |
| 2024-09-20 22:21:35.232 | MS1 | 121.4656725746 | 31.1446184201 | 290 | 504990 | -91.83 | -2.07 | 60.29 | 0.15 | 1.34 | 1583 |
| 2024-09-20 22:21:36.337 | MS1 | 121.4656778557 | 31.1446285250 | 290 | 504990 | -87.06 | -3.19 | 72.51 | 0.10 | 1.28 | 1571 |
| 2024-09-20 22:21:37.437 | MS1 | 121.4656730362 | 31.1446324769 | 290 | 504990 | -85.59 | -3.35 | 57.79 | 0.10 | 1.17 | 1561 |
| 2024-09-20 22:21:38.599 | MS1 | 121.4656686845 | 31.1446368772 | 290 | 504990 | -83.17 | -3.11 | 56.82 | 0.20 | 1.31 | 1571 |
| 2024-09-20 22:21:39.804 | MS1 | 121.4656623683 | 31.1446232426 | 691 | 504990 | -83.06 | 16.16 | 237.61 | 0.10 | 1.46 | 1591 |
| 2024-09-20 22:21:40.436 | MS1 | 121.4656749813 | 31.1446197385 | 691 | 504990 | -76.71 | 15.76 | 579.50 | 0.14 | 2.75 | 1585 |
| 2024-09-20 22:21:41.392 | MS1 | 121.4656581617 | 31.1446329482 | 691 | 504990 | -83.93 | 12.85 | 507.63 | 0.04 | 2.06 | 1564 |
| 2024-09-20 22:21:42.542 | MS1 | 121.4656778853 | 31.1446325336 | 691 | 504990 | -77.88 | 12.11 | 524.97 | 0.02 | 2.85 | 1598 |

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
| 3214740 | 3 | 121.4662308258 | 31.1485672249 | 332 | 9 | 2 | 33.8 | TDD | 867 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3251701 | 4 | 121.4754672013 | 31.1504151593 | 215 | 6 | 5 | 37.3 | TDD | 691 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3261501 | 2 | 121.4726644218 | 31.1510842117 | 2 | 11 | 12 | 25.7 | TDD | 290 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3276702 | 1 | 121.4661659171 | 31.1550648481 | 34 | 6 | 10 | 49.7 | TDD | 344 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.152 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.167 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.273 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.273 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.953 | NREventA3 | measId:2;ServCellPCI:525;Se... |
| 2024-09-20 22:21:38.193 | NRHandoverAttempt | SourcePCI:525;SourceNR-ARFC... |
| 2024-09-20 22:21:38.233 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.244 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.383 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.383 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276702 | 1 | 6.9017 | 6.2934 | -117.2219 | 7.2342 | 183.6957 | 0.0180 | 0.0138 |
| 2024_09_20 22:00 | 3261501 | 2 | 18.0674 | 6.0660 | -114.1178 | 8.5176 | 107.0263 | 0.0149 | 0.1688 |
| 2024_09_20 22:00 | 3214740 | 3 | 9.9754 | 10.4759 | -117.3308 | 5.9458 | 85.5850 | 0.0127 | 0.0107 |
| 2024_09_20 22:00 | 3251701 | 4 | 12.6055 | 19.6707 | -117.2974 | 14.1738 | 130.9022 | 0.0053 | 0.0178 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416378_907D9707 | 504990 | 691 | -80.4 | 504990 | 290 | -89.2 | 504990 | 344 | -85.2 | 504990 | 867 |
| MR_1774416378_324A5B6E | 504990 | 691 | -83.5 | 504990 | 290 | -85.9 | 504990 | 344 | -85.7 | 504990 | 867 |
| MR_1774416378_868FAEE7 | 504990 | 290 | -86.4 | 504990 | 691 | -80.0 | 504990 | 344 | -84.4 | 504990 | 867 |
| MR_1774416378_8883DEE9 | 504990 | 691 | -79.7 | 504990 | 290 | -89.4 | 504990 | 344 | -84.6 | 504990 | 867 |
| MR_1774416378_07BA7000 | 504990 | 691 | -83.3 | 504990 | 290 | -88.6 | 504990 | 344 | -83.9 | 504990 | 867 |
| MR_1774416378_6348D5DD | 504990 | 290 | -88.8 | 504990 | 691 | -81.0 | 504990 | 344 | -85.8 | 504990 | 867 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 81: `b5bae666-8ee...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b5bae666-8ee8-47e3-8d60-8ffaa4792755` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[81] topology](images/test_0081.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3278061_4
- `C2`: Adjust the azimuth of 3222338_5 by 12 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Lift the tilt angle of 3222338_5 by 2 degrees
- `C5`: Press down the tilt angle of 3222338_5 by 2 degrees
- `C6`: Add neighbor relationship between 3273335_9 and 3278061_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222338_5
- `C8`: Decrease A3 Offset threshold for 3222338_5
- `C9`: Increase transmission power for 3278061_4
- `C10`: Decrease transmission power for 3222338_5
- `C11`: Increase A3 Offset threshold for 3222338_5
- `C12`: Decrease transmission power for 3278061_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278061_4
- `C14`: Check test server and transmission issues
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222338_5
- `C16`: Lift the tilt angle  of 3278061_4 by 5 degrees
- `C17`: Add neighbor relationship between 3222338_5 and 3278061_4
- `C18`: Adjust the azimuth of 3278061_4 by 48 degrees
- `C19`: Decrease A3 Offset threshold for 3278061_4
- `C20`: Press down the tilt angle  of 3278061_4 by 5 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278061_4
- `C22`: Increase transmission power for 3222338_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.386 | MS1 | 121.4656600850 | 31.1446275432 | 121 | 504990 | -95.69 | 14.96 | 462.08 | 0.16 | 2.64 | 1582 |
| 2024-09-20 22:21:32.958 | MS1 | 121.4656764408 | 31.1446199636 | 720 | 504990 | -93.74 | 13.57 | 317.37 | 0.19 | 2.57 | 1593 |
| 2024-09-20 22:21:33.647 | MS1 | 121.4656589629 | 31.1446357934 | 77 | 504990 | -93.77 | 12.96 | 393.79 | 0.01 | 2.86 | 1585 |
| 2024-09-20 22:21:34.650 | MS1 | 121.4656746150 | 31.1446249861 | 126 | 152650 | -94.86 | 2.44 | 70.85 | 0.05 | 1.95 | 914 |
| 2024-09-20 22:21:35.152 | MS1 | 121.4656752283 | 31.1446194130 | 277 | 152650 | -88.41 | 4.59 | 74.19 | 0.13 | 1.79 | 914 |
| 2024-09-20 22:21:36.475 | MS1 | 121.4656594575 | 31.1446268434 | 616 | 152650 | -88.03 | 6.08 | 85.75 | 0.07 | 1.55 | 950 |
| 2024-09-20 22:21:37.254 | MS1 | 121.4656715434 | 31.1446347158 | 771 | 152650 | -88.65 | 6.71 | 94.04 | 0.08 | 1.57 | 972 |
| 2024-09-20 22:21:38.749 | MS1 | 121.4656622667 | 31.1446340408 | 126 | 152650 | -92.62 | 4.04 | 61.60 | 0.04 | 1.97 | 939 |
| 2024-09-20 22:21:39.526 | MS1 | 121.4656745918 | 31.1446362302 | 277 | 152650 | -89.75 | 2.78 | 65.57 | 0.09 | 1.83 | 908 |
| 2024-09-20 22:21:40.327 | MS1 | 121.4656695576 | 31.1446238964 | 616 | 152650 | -93.30 | 3.05 | 102.82 | 0.10 | 2.07 | 1594 |
| 2024-09-20 22:21:41.459 | MS1 | 121.4656695402 | 31.1446377909 | 771 | 152650 | -89.30 | 2.00 | 65.31 | 0.07 | 2.30 | 1562 |
| 2024-09-20 22:21:42.164 | MS1 | 121.4656715210 | 31.1446350243 | 126 | 152650 | -94.42 | 6.30 | 52.39 | 0.07 | 2.50 | 1571 |

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
| 3217962 | 7 | 121.4675463825 | 31.1553430531 | 218 | 1 | 8 | 17.8 | FDD | 608 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3218558 | 1 | 121.4714896821 | 31.1507728048 | 166 | 6 | 10 | 14.1 | TDD | 994 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3222338 | 5 | 121.4699490194 | 31.1555121637 | 187 | 1 | 11 | 24.3 | TDD | 121 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3232909 | 12 | 121.4722648548 | 31.1532290264 | 154 | 4 | 4 | 1.4 | FDD | 126 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3239094 | 8 | 121.4699837797 | 31.1534775923 | 272 | 12 | 6 | 18.7 | FDD | 771 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3244601 | 2 | 121.4716402942 | 31.1555296976 | 234 | 8 | 10 | 23.9 | TDD | 77 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3245807 | 6 | 121.4712204243 | 31.1450172335 | 185 | 12 | 8 | 17.5 | TDD | 991 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3254375 | 11 | 121.4729685581 | 31.1532918479 | 144 | 8 | 12 | 6.6 | FDD | 632 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3255785 | 13 | 121.4656468358 | 31.1467575464 | 288 | 5 | 4 | 27.9 | FDD | 319 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3260867 | 3 | 121.4715387836 | 31.1547096010 | 141 | 6 | 1 | 2.8 | TDD | 720 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3273270 | 10 | 121.4644104684 | 31.1466239929 | 267 | 7 | 10 | 27.1 | FDD | 277 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3273335 | 9 | 121.4746377372 | 31.1488815545 | 38 | 11 | 8 | 23.4 | FDD | 616 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3278061 | 4 | 121.4671674492 | 31.1479790642 | 153 | 1 | 2 | 29.0 | TDD | 918 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.845 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.862 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.976 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.976 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.645 | NREventA2 | measId:1;ServCellPCI:820;Se... |
| 2024-09-20 22:21:34.782 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:34.983 | NREventA5 | measId:3;ServCellPCI:820;Se... |
| 2024-09-20 22:21:35.043 | NRHandoverAttempt | SourcePCI:820;SourceNR-ARFC... |
| 2024-09-20 22:21:35.086 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.099 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.222 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.222 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218558 | 1 | 14.8029 | 13.2989 | -116.5436 | 10.3737 | 122.2637 | 0.0103 | 0.0060 |
| 2024_09_20 22:00 | 3244601 | 2 | 11.4934 | 9.8823 | -115.4316 | 15.5962 | 176.0228 | 0.0094 | 0.0155 |
| 2024_09_20 22:00 | 3260867 | 3 | 19.7075 | 12.4750 | -117.1166 | 14.2919 | 166.8233 | 0.0005 | 0.0108 |
| 2024_09_20 22:00 | 3278061 | 4 | 16.2080 | 10.8533 | -115.4799 | 19.6530 | 148.5407 | 0.0166 | 0.0129 |
| 2024_09_20 22:00 | 3222338 | 5 | 6.3020 | 11.7242 | -115.7868 | 12.1190 | 182.6072 | 0.0039 | 0.0030 |
| 2024_09_20 22:00 | 3245807 | 6 | 11.2374 | 14.7752 | -117.6265 | 5.7622 | 134.7406 | 0.0124 | 0.0026 |
| 2024_09_20 22:00 | 3217962 | 7 | 9.2667 | 13.7637 | -114.7092 | 3.4886 | 25.9394 | 0.0122 | 0.0032 |
| 2024_09_20 22:00 | 3239094 | 8 | 15.1699 | 19.4936 | -114.2245 | 4.0665 | 47.6390 | 0.0145 | 0.0037 |
| 2024_09_20 22:00 | 3273335 | 9 | 16.6746 | 12.6714 | -116.3342 | 3.3235 | 49.3387 | 0.0060 | 0.0169 |
| 2024_09_20 22:00 | 3273270 | 10 | 6.3692 | 19.4032 | -114.1877 | 4.5816 | 36.1880 | 0.0053 | 0.0011 |
| 2024_09_20 22:00 | 3254375 | 11 | 7.6138 | 15.8510 | -116.1143 | 4.6993 | 43.3173 | 0.0095 | 0.0027 |
| 2024_09_20 22:00 | 3232909 | 12 | 6.8558 | 18.1115 | -116.1875 | 3.6569 | 31.1970 | 0.0002 | 0.0091 |
| 2024_09_20 22:00 | 3255785 | 13 | 8.4174 | 5.3332 | -117.8607 | 4.3874 | 32.0043 | 0.0096 | 0.0029 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416975_5255E1A8 | 504990 | 77 | -92.1 | 504990 | 918 | -93.2 | 504990 | 994 | -100.5 | 504990 | 991 |
| MR_1774416975_33354675 | 152650 | 126 | -96.4 | 152650 | 632 | -101.4 | 152650 | 319 | -104.4 | 152650 | 608 |
| MR_1774416975_B260298A | 504990 | 77 | -91.8 | 504990 | 918 | -92.4 | 504990 | 994 | -98.8 | 504990 | 991 |
| MR_1774416975_8E7FE442 | 152650 | 126 | -96.5 | 152650 | 632 | -101.0 | 152650 | 319 | -103.4 | 152650 | 608 |
| MR_1774416975_977820E0 | 504990 | 77 | -95.3 | 504990 | 918 | -91.6 | 504990 | 994 | -99.2 | 504990 | 991 |
| MR_1774416975_3E078818 | 504990 | 77 | -93.9 | 504990 | 918 | -90.9 | 504990 | 994 | -100.2 | 504990 | 991 |
| MR_1774416975_D56A48C7 | 152650 | 126 | -96.5 | 152650 | 632 | -99.2 | 152650 | 319 | -104.7 | 152650 | 608 |
| MR_1774416975_13340212 | 152650 | 126 | -94.9 | 152650 | 632 | -100.9 | 152650 | 319 | -102.8 | 152650 | 608 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 82: `5b201c1f-ee2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5b201c1f-ee21-446f-ad95-9dcc553c8c96` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[82] topology](images/test_0082.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3278058_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252512_1
- `C3`: Increase transmission power for 3278058_3
- `C4`: Add neighbor relationship between 3278058_3 and 3252512_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278058_3
- `C6`: Lift the tilt angle of 3278058_3 by 10 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252512_1
- `C8`: Decrease A3 Offset threshold for 3252512_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Adjust the azimuth of 3278058_3 by 42 degrees
- `C11`: Increase transmission power for 3252512_1
- `C12`: Increase A3 Offset threshold for 3252512_1
- `C13`: Increase A3 Offset threshold for 3278058_3
- `C14`: Press down the tilt angle of 3278058_3 by 10 degrees
- `C15`: Check test server and transmission issues
- `C16`: Decrease transmission power for 3252512_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278058_3
- `C18`: Press down the tilt angle  of 3252512_1 by 5 degrees
- `C19`: Decrease transmission power for 3278058_3
- `C20`: Add neighbor relationship between 3263249_4 and 3252512_1
- `C21`: Lift the tilt angle  of 3252512_1 by 5 degrees
- `C22`: Adjust the azimuth of 3252512_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.403 | MS1 | 121.4656627038 | 31.1446361368 | 58 | 504990 | -77.91 | 16.08 | 479.53 | 0.11 | 2.53 | 1577 |
| 2024-09-20 22:21:32.395 | MS1 | 121.4656739847 | 31.1446290026 | 58 | 504990 | -84.34 | 13.42 | 338.57 | 0.07 | 2.49 | 1568 |
| 2024-09-20 22:21:33.739 | MS1 | 121.4656681438 | 31.1446355598 | 58 | 504990 | -83.99 | 16.04 | 502.06 | 0.20 | 2.60 | 1577 |
| 2024-09-20 22:21:34.747 | MS1 | 121.4656671814 | 31.1446216294 | 58 | 504990 | -86.19 | -3.76 | 72.14 | 0.19 | 1.09 | 1578 |
| 2024-09-20 22:21:35.715 | MS1 | 121.4656652287 | 31.1446309451 | 58 | 504990 | -91.23 | -0.47 | 64.14 | 0.04 | 1.31 | 1586 |
| 2024-09-20 22:21:36.128 | MS1 | 121.4656630036 | 31.1446193976 | 58 | 504990 | -92.91 | -3.18 | 44.67 | 0.13 | 1.02 | 1585 |
| 2024-09-20 22:21:37.944 | MS1 | 121.4656772295 | 31.1446359418 | 58 | 504990 | -88.33 | -0.33 | 48.74 | 0.17 | 1.45 | 1599 |
| 2024-09-20 22:21:38.296 | MS1 | 121.4656768750 | 31.1446260849 | 58 | 504990 | -92.86 | -2.87 | 24.81 | 0.17 | 1.27 | 1579 |
| 2024-09-20 22:21:39.495 | MS1 | 121.4656766826 | 31.1446220985 | 465 | 504990 | -84.55 | 15.11 | 218.70 | 0.16 | 1.17 | 1572 |
| 2024-09-20 22:21:40.854 | MS1 | 121.4656665306 | 31.1446228291 | 465 | 504990 | -80.13 | 14.64 | 469.31 | 0.08 | 2.90 | 1569 |
| 2024-09-20 22:21:41.948 | MS1 | 121.4656676973 | 31.1446351424 | 465 | 504990 | -83.91 | 13.19 | 314.99 | 0.02 | 2.21 | 1595 |
| 2024-09-20 22:21:42.288 | MS1 | 121.4656656618 | 31.1446316553 | 465 | 504990 | -80.39 | 17.38 | 577.90 | 0.08 | 2.32 | 1564 |

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
| 3236112 | 2 | 121.4671195776 | 31.1526298684 | 358 | 12 | 10 | 32.7 | TDD | 938 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3252512 | 1 | 121.4640808121 | 31.1502414354 | 19 | 2 | 10 | 35.4 | TDD | 465 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3263249 | 4 | 121.4677037740 | 31.1507164827 | 221 | 5 | 2 | 38.7 | TDD | 295 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3278058 | 3 | 121.4695686917 | 31.1441012806 | 237 | 7 | 7 | 22.7 | TDD | 58 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.289 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.308 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.456 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.456 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.151 | NREventA3 | measId:2;ServCellPCI:661;Se... |
| 2024-09-20 22:21:38.391 | NRHandoverAttempt | SourcePCI:661;SourceNR-ARFC... |
| 2024-09-20 22:21:38.423 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.436 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.567 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.567 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252512 | 1 | 18.6326 | 8.6479 | -116.4913 | 8.8775 | 193.2360 | 0.0091 | 0.0050 |
| 2024_09_20 22:00 | 3236112 | 2 | 9.6023 | 15.2212 | -117.2882 | 9.5227 | 106.8432 | 0.0034 | 0.0018 |
| 2024_09_20 22:00 | 3278058 | 3 | 5.1094 | 14.6691 | -116.9253 | 19.8846 | 169.3970 | 0.0194 | 0.1762 |
| 2024_09_20 22:00 | 3263249 | 4 | 19.0499 | 12.3568 | -115.9989 | 8.7609 | 159.7922 | 0.0046 | 0.0146 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415837_176A5DF4 | 504990 | 465 | -82.8 | 504990 | 58 | -85.4 | 504990 | 295 | -86.7 | 504990 | 938 |
| MR_1774415837_DDF2E7AD | 504990 | 465 | -83.9 | 504990 | 58 | -87.5 | 504990 | 295 | -87.2 | 504990 | 938 |
| MR_1774415837_65857C28 | 504990 | 58 | -87.8 | 504990 | 465 | -80.7 | 504990 | 295 | -86.1 | 504990 | 938 |
| MR_1774415837_616EBCAA | 504990 | 465 | -81.9 | 504990 | 58 | -85.4 | 504990 | 295 | -87.0 | 504990 | 938 |
| MR_1774415837_51F94A2F | 504990 | 465 | -80.5 | 504990 | 58 | -86.6 | 504990 | 295 | -87.7 | 504990 | 938 |
| MR_1774415837_098D7A86 | 504990 | 58 | -84.5 | 504990 | 465 | -83.8 | 504990 | 295 | -86.6 | 504990 | 938 |
| MR_1774415837_9305E518 | 504990 | 465 | -80.4 | 504990 | 58 | -85.5 | 504990 | 295 | -87.2 | 504990 | 938 |
| MR_1774415837_DFB5C046 | 504990 | 58 | -85.1 | 504990 | 465 | -81.4 | 504990 | 295 | -87.9 | 504990 | 938 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 83: `a076ba35-44f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a076ba35-44fa-42c0-bd84-921b3b55c432` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[83] topology](images/test_0083.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3268681_2 by 10 degrees
- `C2`: Decrease transmission power for 3268681_2
- `C3`: Increase transmission power for 3268681_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268681_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244587_3
- `C6`: Check test server and transmission issues
- `C7`: Decrease transmission power for 3244587_3
- `C8`: Decrease A3 Offset threshold for 3268681_2
- `C9`: Increase transmission power for 3244587_3
- `C10`: Add neighbor relationship between 3223122_1 and 3244587_3
- `C11`: Increase A3 Offset threshold for 3244587_3
- `C12`: Increase A3 Offset threshold for 3268681_2
- `C13`: Adjust the azimuth of 3244587_3 by 31 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268681_2
- `C15`: Decrease A3 Offset threshold for 3244587_3
- `C16`: Press down the tilt angle of 3268681_2 by 10 degrees
- `C17`: Lift the tilt angle  of 3244587_3 by 10 degrees
- `C18`: Adjust the azimuth of 3268681_2 by 50 degrees
- `C19`: Press down the tilt angle  of 3244587_3 by 10 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244587_3
- `C22`: Add neighbor relationship between 3268681_2 and 3244587_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.650 | MS1 | 121.4656634012 | 31.1446251688 | 996 | 504990 | -86.39 | 14.69 | 297.97 | 0.05 | 2.89 | 1585 |
| 2024-09-20 22:21:32.336 | MS1 | 121.4656775308 | 31.1446221582 | 996 | 504990 | -87.66 | 17.66 | 547.55 | 0.07 | 2.43 | 1571 |
| 2024-09-20 22:21:33.265 | MS1 | 121.4656617617 | 31.1446197122 | 996 | 504990 | -91.95 | 13.40 | 602.68 | 0.19 | 2.46 | 1574 |
| 2024-09-20 22:21:34.481 | MS1 | 121.4656646982 | 31.1446330460 | 996 | 504990 | -91.80 | 15.06 | 62.26 | 0.03 | 2.16 | 1574 |
| 2024-09-20 22:21:35.526 | MS1 | 121.4656672826 | 31.1446232072 | 996 | 504990 | -89.94 | 17.91 | 97.20 | 0.08 | 2.64 | 1585 |
| 2024-09-20 22:21:36.204 | MS1 | 121.4656655477 | 31.1446274864 | 996 | 504990 | -87.99 | 17.30 | 79.88 | 0.09 | 2.07 | 1566 |
| 2024-09-20 22:21:37.353 | MS1 | 121.4656607350 | 31.1446315160 | 996 | 504990 | -92.72 | 7.69 | 65.53 | 0.16 | 2.68 | 1591 |
| 2024-09-20 22:21:38.777 | MS1 | 121.4656774980 | 31.1446305462 | 996 | 504990 | -92.23 | 7.77 | 99.18 | 0.17 | 2.20 | 1597 |
| 2024-09-20 22:21:39.980 | MS1 | 121.4656734063 | 31.1446374829 | 996 | 504990 | -90.59 | 12.21 | 68.23 | 0.04 | 2.38 | 1573 |
| 2024-09-20 22:21:40.732 | MS1 | 121.4656768979 | 31.1446365482 | 996 | 504990 | -90.45 | 11.42 | 581.44 | 0.07 | 2.74 | 1575 |
| 2024-09-20 22:21:41.627 | MS1 | 121.4656761570 | 31.1446357721 | 996 | 504990 | -91.76 | 11.05 | 454.82 | 0.05 | 2.44 | 1564 |
| 2024-09-20 22:21:42.419 | MS1 | 121.4656633778 | 31.1446266231 | 996 | 504990 | -91.53 | 8.14 | 582.45 | 0.13 | 2.52 | 1564 |

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
| 3223122 | 1 | 121.4688195699 | 31.1509615944 | 274 | 13 | 3 | 29.3 | TDD | 59 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3244587 | 3 | 121.4640747650 | 31.1540666794 | 141 | 13 | 10 | 31.4 | TDD | 540 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3267357 | 4 | 121.4669608040 | 31.1462019844 | 75 | 5 | 5 | 39.8 | TDD | 451 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3268681 | 2 | 121.4652582321 | 31.1500458099 | 118 | 8 | 2 | 20.1 | TDD | 996 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.344 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.360 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.505 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.505 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.174 | NREventA3 | measId:2;ServCellPCI:553;Se... |
| 2024-09-20 22:21:38.414 | NRHandoverAttempt | SourcePCI:553;SourceNR-ARFC... |
| 2024-09-20 22:21:38.464 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.474 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.590 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.590 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3223122 | 1 | 78.7935 | 78.1870 | -116.4568 | 17.5892 | 127.1217 | 0.0036 | 0.0145 |
| 2024_09_19 22:00 | 3268681 | 2 | 91.3800 | 91.6243 | -116.1309 | 10.5532 | 175.0348 | 0.0120 | 0.0193 |
| 2024_09_19 22:00 | 3244587 | 3 | 91.6222 | 89.1832 | -114.3129 | 6.9987 | 127.6629 | 0.0094 | 0.0039 |
| 2024_09_19 22:00 | 3267357 | 4 | 86.0077 | 93.7967 | -115.4723 | 8.9718 | 83.9643 | 0.0165 | 0.0117 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414343_698CDE52 | 504990 | 996 | -91.5 | 504990 | 540 | -96.5 | 504990 | 59 | -105.6 | 504990 | 451 |
| MR_1774414343_41A1D718 | 504990 | 996 | -91.9 | 504990 | 540 | -97.7 | 504990 | 59 | -107.9 | 504990 | 451 |
| MR_1774414343_A0EC528A | 504990 | 996 | -93.4 | 504990 | 540 | -99.2 | 504990 | 59 | -107.3 | 504990 | 451 |
| MR_1774414343_DDF2588F | 504990 | 996 | -93.7 | 504990 | 540 | -99.3 | 504990 | 59 | -106.6 | 504990 | 451 |
| MR_1774414343_6817EE48 | 504990 | 996 | -90.2 | 504990 | 540 | -96.2 | 504990 | 59 | -106.4 | 504990 | 451 |
| MR_1774414343_4882B15D | 504990 | 996 | -91.6 | 504990 | 540 | -95.5 | 504990 | 59 | -104.3 | 504990 | 451 |
| MR_1774414343_A8CDF51C | 504990 | 996 | -91.1 | 504990 | 540 | -97.5 | 504990 | 59 | -104.6 | 504990 | 451 |
| MR_1774414343_F55018E3 | 504990 | 996 | -91.9 | 504990 | 540 | -96.8 | 504990 | 59 | -106.1 | 504990 | 451 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 84: `9e437b0e-5f2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9e437b0e-5f27-4473-93e6-0c514f6e35be` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[84] topology](images/test_0084.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238869_1
- `C2`: Add neighbor relationship between 3242697_3 and 3238869_1
- `C3`: Adjust the azimuth of 3242697_3 by 50 degrees
- `C4`: Increase transmission power for 3238869_1
- `C5`: Check test server and transmission issues
- `C6`: Decrease A3 Offset threshold for 3235509_4
- `C7`: Increase transmission power for 3235509_4
- `C8`: Lift the tilt angle  of 3242697_3 by 10 degrees
- `C9`: Lift the tilt angle of 3235509_4 by 5 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238869_1
- `C11`: Increase A3 Offset threshold for 3235509_4
- `C12`: Increase A3 Offset threshold for 3238869_1
- `C13`: Decrease A3 Offset threshold for 3238869_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235509_4
- `C15`: Add neighbor relationship between 3235509_4 and 3238869_1
- `C16`: Press down the tilt angle  of 3242697_3 by 10 degrees
- `C17`: Decrease transmission power for 3238869_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235509_4
- `C19`: Press down the tilt angle of 3235509_4 by 5 degrees
- `C20`: Decrease transmission power for 3235509_4
- `C21`: Adjust the azimuth of 3235509_4 by 22 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.708 | MS1 | 121.4656607657 | 31.1446348608 | 862 | 504990 | -88.11 | 16.01 | 400.69 | 0.08 | 2.26 | 1562 |
| 2024-09-20 22:21:32.983 | MS1 | 121.4656627395 | 31.1446320027 | 862 | 504990 | -87.85 | 16.11 | 386.09 | 0.18 | 2.92 | 1584 |
| 2024-09-20 22:21:33.880 | MS1 | 121.4656676410 | 31.1446326562 | 862 | 504990 | -88.47 | 15.26 | 433.29 | 0.10 | 2.32 | 1569 |
| 2024-09-20 22:21:34.367 | MS1 | 121.4656707273 | 31.1446234290 | 862 | 504990 | -87.58 | 12.29 | 61.46 | 0.19 | 2.05 | 1579 |
| 2024-09-20 22:21:35.191 | MS1 | 121.4656602407 | 31.1446204822 | 862 | 504990 | -88.73 | 15.88 | 96.34 | 0.07 | 2.01 | 1598 |
| 2024-09-20 22:21:36.492 | MS1 | 121.4656746691 | 31.1446262977 | 862 | 504990 | -89.67 | 17.99 | 78.10 | 0.07 | 2.89 | 1583 |
| 2024-09-20 22:21:37.890 | MS1 | 121.4656601435 | 31.1446250084 | 862 | 504990 | -92.13 | 12.82 | 64.57 | 0.03 | 2.44 | 1586 |
| 2024-09-20 22:21:38.935 | MS1 | 121.4656587516 | 31.1446278095 | 862 | 504990 | -89.84 | 9.24 | 78.57 | 0.02 | 2.89 | 1577 |
| 2024-09-20 22:21:39.150 | MS1 | 121.4656662174 | 31.1446229839 | 862 | 504990 | -91.42 | 11.28 | 62.98 | 0.02 | 2.04 | 1580 |
| 2024-09-20 22:21:40.255 | MS1 | 121.4656722859 | 31.1446304429 | 862 | 504990 | -91.98 | 8.00 | 464.81 | 0.10 | 2.59 | 1578 |
| 2024-09-20 22:21:41.630 | MS1 | 121.4656761998 | 31.1446219970 | 862 | 504990 | -93.03 | 7.68 | 579.31 | 0.13 | 2.23 | 1598 |
| 2024-09-20 22:21:42.594 | MS1 | 121.4656774894 | 31.1446242056 | 862 | 504990 | -92.27 | 10.26 | 352.12 | 0.10 | 2.48 | 1579 |

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
| 3223248 | 2 | 121.4711495297 | 31.1457535786 | 109 | 6 | 3 | 36.0 | TDD | 916 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3235509 | 4 | 121.4672132334 | 31.1532401400 | 211 | 3 | 5 | 28.9 | TDD | 862 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3238869 | 1 | 121.4721896053 | 31.1487399320 | 67 | 14 | 1 | 19.5 | TDD | 731 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3242697 | 3 | 121.4733391940 | 31.1494011651 | 339 | 9 | 6 | 26.4 | TDD | 268 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.917 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.938 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.076 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.076 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.759 | NREventA3 | measId:2;ServCellPCI:874;Se... |
| 2024-09-20 22:21:37.999 | NRHandoverAttempt | SourcePCI:874;SourceNR-ARFC... |
| 2024-09-20 22:21:38.032 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.046 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.155 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.155 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238869 | 1 | 12.7998 | 15.7596 | -117.8718 | 5.6223 | 174.5994 | 0.0191 | 0.0073 |
| 2024_09_20 22:00 | 3223248 | 2 | 11.4708 | 16.4964 | -116.3656 | 16.3659 | 134.7150 | 0.0183 | 0.0075 |
| 2024_09_20 22:00 | 3242697 | 3 | 14.2616 | 13.4342 | -115.7241 | 15.9216 | 174.3344 | 0.0179 | 0.0046 |
| 2024_09_20 22:00 | 3235509 | 4 | 87.3192 | 78.0936 | -116.5056 | 7.0390 | 173.2592 | 0.0172 | 0.0098 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413370_4FF471FB | 504990 | 862 | -88.5 | 504990 | 731 | -92.1 | 504990 | 268 | -95.2 | 504990 | 916 |
| MR_1774413370_FEFFA6A8 | 504990 | 862 | -87.9 | 504990 | 731 | -92.5 | 504990 | 268 | -96.9 | 504990 | 916 |
| MR_1774413370_73014DA3 | 504990 | 862 | -87.5 | 504990 | 731 | -92.7 | 504990 | 268 | -97.7 | 504990 | 916 |
| MR_1774413370_C5BEEF93 | 504990 | 862 | -88.4 | 504990 | 731 | -91.1 | 504990 | 268 | -94.9 | 504990 | 916 |
| MR_1774413370_10208EE7 | 504990 | 862 | -88.4 | 504990 | 731 | -92.3 | 504990 | 268 | -94.9 | 504990 | 916 |
| MR_1774413370_FADF27F0 | 504990 | 862 | -89.1 | 504990 | 731 | -93.6 | 504990 | 268 | -94.2 | 504990 | 916 |
| MR_1774413370_3DB621B2 | 504990 | 862 | -87.1 | 504990 | 731 | -91.3 | 504990 | 268 | -94.4 | 504990 | 916 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 85: `c01e3a7d-43e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c01e3a7d-43ef-4b92-af0b-20f9971f55ad` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[85] topology](images/test_0085.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3247387_4 by 10 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275303_2
- `C3`: Increase transmission power for 3247387_4
- `C4`: Adjust the azimuth of 3275303_2 by 50 degrees
- `C5`: Increase A3 Offset threshold for 3275303_2
- `C6`: Press down the tilt angle  of 3247387_4 by 10 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247387_4
- `C8`: Press down the tilt angle of 3275303_2 by 10 degrees
- `C9`: Lift the tilt angle of 3275303_2 by 10 degrees
- `C10`: Add neighbor relationship between 3214311_3 and 3247387_4
- `C11`: Decrease transmission power for 3247387_4
- `C12`: Increase transmission power for 3275303_2
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease transmission power for 3275303_2
- `C15`: Add neighbor relationship between 3275303_2 and 3247387_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275303_2
- `C17`: Adjust the azimuth of 3247387_4 by 50 degrees
- `C18`: Decrease A3 Offset threshold for 3247387_4
- `C19`: Check test server and transmission issues
- `C20`: Decrease A3 Offset threshold for 3275303_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247387_4
- `C22`: Increase A3 Offset threshold for 3247387_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.962 | MS1 | 121.4656753039 | 31.1446279232 | 740 | 504990 | -87.23 | 13.27 | 589.21 | 0.09 | 2.22 | 1585 |
| 2024-09-20 22:21:32.621 | MS1 | 121.4656680786 | 31.1446287779 | 740 | 504990 | -86.34 | 17.77 | 539.01 | 0.03 | 2.96 | 1569 |
| 2024-09-20 22:21:33.113 | MS1 | 121.4656650120 | 31.1446293832 | 740 | 504990 | -89.31 | 16.60 | 418.64 | 0.04 | 2.52 | 1594 |
| 2024-09-20 22:21:34.915 | MS1 | 121.4656610141 | 31.1446255508 | 740 | 504990 | -88.83 | 14.32 | 61.45 | 0.12 | 2.31 | 1563 |
| 2024-09-20 22:21:35.243 | MS1 | 121.4656763299 | 31.1446296127 | 740 | 504990 | -85.87 | 17.91 | 70.90 | 0.12 | 2.38 | 1578 |
| 2024-09-20 22:21:36.379 | MS1 | 121.4656611308 | 31.1446360385 | 740 | 504990 | -88.74 | 17.91 | 76.60 | 0.16 | 2.83 | 1593 |
| 2024-09-20 22:21:37.651 | MS1 | 121.4656691380 | 31.1446296902 | 740 | 504990 | -93.81 | 7.17 | 63.01 | 0.09 | 2.65 | 1584 |
| 2024-09-20 22:21:38.154 | MS1 | 121.4656779097 | 31.1446261333 | 740 | 504990 | -89.35 | 10.36 | 56.67 | 0.05 | 2.75 | 1565 |
| 2024-09-20 22:21:39.698 | MS1 | 121.4656680610 | 31.1446214649 | 740 | 504990 | -91.88 | 8.95 | 87.90 | 0.11 | 2.10 | 1596 |
| 2024-09-20 22:21:40.221 | MS1 | 121.4656731342 | 31.1446315096 | 740 | 504990 | -92.07 | 8.24 | 603.44 | 0.12 | 2.67 | 1584 |
| 2024-09-20 22:21:41.293 | MS1 | 121.4656684213 | 31.1446335893 | 740 | 504990 | -92.45 | 11.20 | 435.19 | 0.20 | 2.85 | 1581 |
| 2024-09-20 22:21:42.138 | MS1 | 121.4656647419 | 31.1446228537 | 740 | 504990 | -93.27 | 9.97 | 386.53 | 0.12 | 2.38 | 1585 |

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
| 3214311 | 3 | 121.4728877551 | 31.1510165440 | 196 | 7 | 12 | 35.4 | TDD | 846 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3215733 | 1 | 121.4671439485 | 31.1482990819 | 71 | 10 | 4 | 48.4 | TDD | 106 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3247387 | 4 | 121.4717302714 | 31.1553777674 | 79 | 14 | 12 | 19.8 | TDD | 71 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3275303 | 2 | 121.4642550983 | 31.1543512048 | 301 | 14 | 8 | 24.9 | TDD | 740 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.309 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.332 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.477 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.477 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.158 | NREventA3 | measId:2;ServCellPCI:650;Se... |
| 2024-09-20 22:21:38.398 | NRHandoverAttempt | SourcePCI:650;SourceNR-ARFC... |
| 2024-09-20 22:21:38.447 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.462 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.565 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.565 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3215733 | 1 | 80.1237 | 89.1065 | -114.0875 | 11.6246 | 175.2172 | 0.0181 | 0.0124 |
| 2024_09_19 22:00 | 3275303 | 2 | 93.3694 | 92.9756 | -114.9262 | 17.4647 | 182.0049 | 0.0044 | 0.0051 |
| 2024_09_19 22:00 | 3214311 | 3 | 89.1482 | 86.1840 | -116.3138 | 12.9268 | 109.5776 | 0.0189 | 0.0132 |
| 2024_09_19 22:00 | 3247387 | 4 | 80.4699 | 85.3250 | -115.9145 | 16.3334 | 188.6304 | 0.0027 | 0.0155 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412389_44BD39EC | 504990 | 740 | -89.7 | 504990 | 71 | -90.8 | 504990 | 846 | -101.6 | 504990 | 106 |
| MR_1774412389_D9567A6E | 504990 | 740 | -90.6 | 504990 | 71 | -90.5 | 504990 | 846 | -104.4 | 504990 | 106 |
| MR_1774412389_73DB72AE | 504990 | 740 | -87.3 | 504990 | 71 | -89.0 | 504990 | 846 | -100.9 | 504990 | 106 |
| MR_1774412389_2D993CA5 | 504990 | 740 | -88.4 | 504990 | 71 | -91.5 | 504990 | 846 | -104.0 | 504990 | 106 |
| MR_1774412389_B7D42FD9 | 504990 | 740 | -88.4 | 504990 | 71 | -91.0 | 504990 | 846 | -101.4 | 504990 | 106 |
| MR_1774412389_76582C4D | 504990 | 740 | -87.7 | 504990 | 71 | -89.6 | 504990 | 846 | -103.5 | 504990 | 106 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 86: `adda9a54-7e7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `adda9a54-7e7b-4d3f-8849-78bd5d5a9e40` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[86] topology](images/test_0086.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3242698_2
- `C2`: Lift the tilt angle of 3219366_4 by 5 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Add neighbor relationship between 3263360_1 and 3242698_2
- `C5`: Decrease A3 Offset threshold for 3242698_2
- `C6`: Press down the tilt angle of 3219366_4 by 5 degrees
- `C7`: Decrease transmission power for 3219366_4
- `C8`: Increase transmission power for 3242698_2
- `C9`: Add neighbor relationship between 3219366_4 and 3242698_2
- `C10`: Increase A3 Offset threshold for 3219366_4
- `C11`: Press down the tilt angle  of 3242698_2 by 6 degrees
- `C12`: Increase transmission power for 3219366_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242698_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242698_2
- `C15`: Decrease transmission power for 3242698_2
- `C16`: Check test server and transmission issues
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219366_4
- `C18`: Adjust the azimuth of 3242698_2 by 50 degrees
- `C19`: Adjust the azimuth of 3219366_4 by 50 degrees
- `C20`: Decrease A3 Offset threshold for 3219366_4
- `C21`: Lift the tilt angle  of 3242698_2 by 6 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219366_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.662 | MS1 | 121.4656694691 | 31.1446204312 | 262 | 504990 | -89.45 | 17.36 | 555.70 | 0.11 | 2.61 | 1567 |
| 2024-09-20 22:21:32.818 | MS1 | 121.4656746392 | 31.1446331477 | 262 | 504990 | -87.02 | 13.69 | 456.63 | 0.19 | 2.66 | 1590 |
| 2024-09-20 22:21:33.634 | MS1 | 121.4656619022 | 31.1446217187 | 262 | 504990 | -87.98 | 15.48 | 313.81 | 0.02 | 2.43 | 1596 |
| 2024-09-20 22:21:34.906 | MS1 | 121.4656627559 | 31.1446237343 | 262 | 504990 | -88.10 | 12.70 | 59.91 | 0.06 | 2.62 | 1570 |
| 2024-09-20 22:21:35.208 | MS1 | 121.4656721745 | 31.1446346966 | 262 | 504990 | -85.87 | 17.03 | 105.81 | 0.18 | 2.76 | 1561 |
| 2024-09-20 22:21:36.614 | MS1 | 121.4656760152 | 31.1446240948 | 262 | 504990 | -88.74 | 13.30 | 54.25 | 0.00 | 2.29 | 1561 |
| 2024-09-20 22:21:37.341 | MS1 | 121.4656776541 | 31.1446214506 | 262 | 504990 | -92.48 | 10.09 | 69.94 | 0.19 | 2.01 | 1577 |
| 2024-09-20 22:21:38.277 | MS1 | 121.4656654663 | 31.1446260635 | 262 | 504990 | -93.98 | 11.94 | 71.93 | 0.03 | 2.82 | 1572 |
| 2024-09-20 22:21:39.325 | MS1 | 121.4656639402 | 31.1446184388 | 262 | 504990 | -92.77 | 8.15 | 69.48 | 0.19 | 2.06 | 1591 |
| 2024-09-20 22:21:40.676 | MS1 | 121.4656771169 | 31.1446330381 | 262 | 504990 | -93.90 | 11.92 | 602.10 | 0.06 | 2.71 | 1567 |
| 2024-09-20 22:21:41.171 | MS1 | 121.4656761648 | 31.1446258519 | 262 | 504990 | -90.31 | 12.44 | 423.91 | 0.10 | 2.48 | 1600 |
| 2024-09-20 22:21:42.344 | MS1 | 121.4656726690 | 31.1446308684 | 262 | 504990 | -89.49 | 11.68 | 320.04 | 0.20 | 2.63 | 1574 |

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
| 3219366 | 4 | 121.4727442877 | 31.1494215627 | 163 | 2 | 10 | 39.0 | TDD | 262 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3242698 | 2 | 121.4693902657 | 31.1493879228 | 23 | 4 | 10 | 22.9 | TDD | 611 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3263360 | 1 | 121.4682475407 | 31.1448681810 | 120 | 2 | 4 | 37.0 | TDD | 729 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3264652 | 3 | 121.4644478945 | 31.1479741325 | 349 | 12 | 2 | 35.8 | TDD | 757 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.513 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.529 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.678 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.678 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.353 | NREventA3 | measId:2;ServCellPCI:513;Se... |
| 2024-09-20 22:21:38.593 | NRHandoverAttempt | SourcePCI:513;SourceNR-ARFC... |
| 2024-09-20 22:21:38.627 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.638 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.784 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.784 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3263360 | 1 | 84.6403 | 88.8577 | -115.1957 | 17.8325 | 105.7987 | 0.0022 | 0.0155 |
| 2024_09_19 22:00 | 3242698 | 2 | 76.2489 | 91.5204 | -115.3559 | 5.9427 | 145.6901 | 0.0004 | 0.0156 |
| 2024_09_19 22:00 | 3264652 | 3 | 79.4767 | 91.6940 | -117.8944 | 7.2563 | 144.7033 | 0.0089 | 0.0123 |
| 2024_09_19 22:00 | 3219366 | 4 | 79.3546 | 85.6867 | -114.8362 | 11.4542 | 105.8557 | 0.0102 | 0.0165 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412136_FADAC062 | 504990 | 262 | -87.4 | 504990 | 611 | -88.8 | 504990 | 729 | -99.9 | 504990 | 757 |
| MR_1774412136_EA81C431 | 504990 | 262 | -89.6 | 504990 | 611 | -91.2 | 504990 | 729 | -99.3 | 504990 | 757 |
| MR_1774412136_48F00303 | 504990 | 262 | -89.6 | 504990 | 611 | -90.7 | 504990 | 729 | -97.6 | 504990 | 757 |
| MR_1774412136_4EB6E09E | 504990 | 262 | -89.4 | 504990 | 611 | -88.8 | 504990 | 729 | -97.2 | 504990 | 757 |
| MR_1774412136_3A43D81E | 504990 | 262 | -89.4 | 504990 | 611 | -90.3 | 504990 | 729 | -100.1 | 504990 | 757 |
| MR_1774412136_E0D32B73 | 504990 | 262 | -88.5 | 504990 | 611 | -88.2 | 504990 | 729 | -97.2 | 504990 | 757 |
| MR_1774412136_B04C50BE | 504990 | 262 | -87.4 | 504990 | 611 | -90.2 | 504990 | 729 | -98.4 | 504990 | 757 |
| MR_1774412136_2CBD429C | 504990 | 262 | -87.1 | 504990 | 611 | -91.5 | 504990 | 729 | -98.1 | 504990 | 757 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 87: `fa4937c5-34b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fa4937c5-34b1-4257-a863-2fc1efdb5e51` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[87] topology](images/test_0087.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease A3 Offset threshold for 3276941_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243725_1
- `C4`: Press down the tilt angle  of 3243725_1 by 8 degrees
- `C5`: Decrease transmission power for 3276941_3
- `C6`: Increase A3 Offset threshold for 3243725_1
- `C7`: Decrease A3 Offset threshold for 3243725_1
- `C8`: Add neighbor relationship between 3226954_2 and 3243725_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Increase A3 Offset threshold for 3276941_3
- `C11`: Press down the tilt angle of 3276941_3 by 10 degrees
- `C12`: Adjust the azimuth of 3276941_3 by 50 degrees
- `C13`: Adjust the azimuth of 3243725_1 by 50 degrees
- `C14`: Decrease transmission power for 3243725_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276941_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243725_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276941_3
- `C18`: Lift the tilt angle  of 3243725_1 by 8 degrees
- `C19`: Lift the tilt angle of 3276941_3 by 10 degrees
- `C20`: Add neighbor relationship between 3276941_3 and 3243725_1
- `C21`: Increase transmission power for 3243725_1
- `C22`: Increase transmission power for 3276941_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.975 | MS1 | 121.4656583983 | 31.1446216882 | 52 | 504990 | -89.16 | 14.54 | 305.32 | 0.16 | 2.57 | 1562 |
| 2024-09-20 22:21:32.808 | MS1 | 121.4656779291 | 31.1446221669 | 52 | 504990 | -85.29 | 15.43 | 338.45 | 0.07 | 2.40 | 1588 |
| 2024-09-20 22:21:33.889 | MS1 | 121.4656641423 | 31.1446231886 | 52 | 504990 | -89.76 | 13.24 | 501.55 | 0.01 | 2.49 | 1564 |
| 2024-09-20 22:21:34.687 | MS1 | 121.4656740982 | 31.1446299568 | 52 | 504990 | -86.70 | 16.60 | 77.28 | 0.17 | 2.67 | 1578 |
| 2024-09-20 22:21:35.754 | MS1 | 121.4656704342 | 31.1446242668 | 52 | 504990 | -87.00 | 13.30 | 88.73 | 0.10 | 2.47 | 1567 |
| 2024-09-20 22:21:36.646 | MS1 | 121.4656610643 | 31.1446280776 | 52 | 504990 | -91.67 | 16.14 | 81.12 | 0.08 | 2.13 | 1576 |
| 2024-09-20 22:21:37.410 | MS1 | 121.4656660747 | 31.1446322685 | 52 | 504990 | -89.38 | 8.69 | 85.51 | 0.07 | 2.40 | 1561 |
| 2024-09-20 22:21:38.794 | MS1 | 121.4656690006 | 31.1446333589 | 52 | 504990 | -89.25 | 8.74 | 83.90 | 0.20 | 2.21 | 1600 |
| 2024-09-20 22:21:39.589 | MS1 | 121.4656678082 | 31.1446249022 | 52 | 504990 | -90.69 | 9.99 | 47.43 | 0.18 | 2.78 | 1575 |
| 2024-09-20 22:21:40.963 | MS1 | 121.4656717570 | 31.1446213421 | 52 | 504990 | -89.92 | 8.56 | 467.45 | 0.15 | 2.39 | 1582 |
| 2024-09-20 22:21:41.343 | MS1 | 121.4656644535 | 31.1446264909 | 52 | 504990 | -92.70 | 12.06 | 476.72 | 0.20 | 2.86 | 1575 |
| 2024-09-20 22:21:42.932 | MS1 | 121.4656658699 | 31.1446333288 | 52 | 504990 | -90.09 | 10.73 | 415.71 | 0.01 | 2.44 | 1578 |

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
| 3226954 | 2 | 121.4653204273 | 31.1512993507 | 116 | 13 | 5 | 35.3 | TDD | 371 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3243725 | 1 | 121.4722567103 | 31.1491231255 | 358 | 5 | 8 | 37.2 | TDD | 162 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3248993 | 4 | 121.4695589673 | 31.1501206679 | 21 | 12 | 1 | 41.5 | TDD | 796 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3276941 | 3 | 121.4676978981 | 31.1465020144 | 56 | 15 | 10 | 47.0 | TDD | 52 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.178 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.194 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.339 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.339 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.000 | NREventA3 | measId:2;ServCellPCI:295;Se... |
| 2024-09-20 22:21:38.240 | NRHandoverAttempt | SourcePCI:295;SourceNR-ARFC... |
| 2024-09-20 22:21:38.279 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.291 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.431 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.431 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3243725 | 1 | 76.9117 | 83.8120 | -116.4403 | 12.8282 | 178.2033 | 0.0195 | 0.0009 |
| 2024_09_19 22:00 | 3226954 | 2 | 75.0704 | 91.4760 | -116.7011 | 11.6568 | 163.5484 | 0.0140 | 0.0097 |
| 2024_09_19 22:00 | 3276941 | 3 | 93.4295 | 91.8503 | -115.9250 | 9.3350 | 119.3184 | 0.0019 | 0.0136 |
| 2024_09_19 22:00 | 3248993 | 4 | 88.9869 | 79.3458 | -116.5265 | 6.1017 | 92.3910 | 0.0041 | 0.0191 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416353_205595EB | 504990 | 52 | -85.5 | 504990 | 162 | -87.2 | 504990 | 371 | -96.0 | 504990 | 796 |
| MR_1774416353_D55C27C9 | 504990 | 52 | -87.7 | 504990 | 162 | -88.7 | 504990 | 371 | -98.5 | 504990 | 796 |
| MR_1774416353_02F9C931 | 504990 | 52 | -88.0 | 504990 | 162 | -87.9 | 504990 | 371 | -98.0 | 504990 | 796 |
| MR_1774416353_B83EC892 | 504990 | 52 | -88.1 | 504990 | 162 | -90.1 | 504990 | 371 | -98.8 | 504990 | 796 |
| MR_1774416353_412BDE18 | 504990 | 52 | -85.0 | 504990 | 162 | -88.1 | 504990 | 371 | -96.2 | 504990 | 796 |
| MR_1774416353_9D1FEB32 | 504990 | 52 | -85.4 | 504990 | 162 | -87.6 | 504990 | 371 | -98.0 | 504990 | 796 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 88: `1c282cf8-9d8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1c282cf8-9d81-4246-9dea-4c0332edd152` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[88] topology](images/test_0088.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Press down the tilt angle of 3268321_1 by 10 degrees
- `C3`: Adjust the azimuth of 3268321_1 by 50 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239571_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268321_1
- `C6`: Increase A3 Offset threshold for 3239571_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268321_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239571_2
- `C9`: Decrease A3 Offset threshold for 3268321_1
- `C10`: Press down the tilt angle  of 3239571_2 by 10 degrees
- `C11`: Add neighbor relationship between 3255898_3 and 3239571_2
- `C12`: Lift the tilt angle of 3268321_1 by 10 degrees
- `C13`: Add neighbor relationship between 3268321_1 and 3239571_2
- `C14`: Increase transmission power for 3268321_1
- `C15`: Check test server and transmission issues
- `C16`: Decrease transmission power for 3268321_1
- `C17`: Decrease A3 Offset threshold for 3239571_2
- `C18`: Increase A3 Offset threshold for 3268321_1
- `C19`: Decrease transmission power for 3239571_2
- `C20`: Adjust the azimuth of 3239571_2 by 50 degrees
- `C21`: Lift the tilt angle  of 3239571_2 by 10 degrees
- `C22`: Increase transmission power for 3239571_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.794 | MS1 | 121.4656712104 | 31.1446198250 | 835 | 504990 | -87.20 | 13.83 | 314.08 | 0.07 | 2.83 | 1574 |
| 2024-09-20 22:21:32.321 | MS1 | 121.4656628264 | 31.1446295563 | 835 | 504990 | -89.27 | 15.18 | 544.10 | 0.05 | 2.82 | 1577 |
| 2024-09-20 22:21:33.167 | MS1 | 121.4656580790 | 31.1446317017 | 835 | 504990 | -88.70 | 13.16 | 452.38 | 0.14 | 2.32 | 1596 |
| 2024-09-20 22:21:34.946 | MS1 | 121.4656620645 | 31.1446364997 | 835 | 504990 | -88.26 | 17.11 | 84.15 | 0.12 | 2.61 | 413 |
| 2024-09-20 22:21:35.427 | MS1 | 121.4656619206 | 31.1446303001 | 835 | 504990 | -87.61 | 16.39 | 76.88 | 0.11 | 2.44 | 370 |
| 2024-09-20 22:21:36.815 | MS1 | 121.4656582386 | 31.1446238935 | 835 | 504990 | -91.18 | 15.42 | 74.51 | 0.18 | 2.00 | 328 |
| 2024-09-20 22:21:37.631 | MS1 | 121.4656704728 | 31.1446333953 | 835 | 504990 | -93.93 | 7.05 | 77.35 | 0.08 | 2.77 | 488 |
| 2024-09-20 22:21:38.737 | MS1 | 121.4656715858 | 31.1446252553 | 835 | 504990 | -91.09 | 8.22 | 55.89 | 0.19 | 2.07 | 445 |
| 2024-09-20 22:21:39.822 | MS1 | 121.4656601383 | 31.1446185365 | 835 | 504990 | -92.70 | 10.33 | 62.93 | 0.15 | 2.98 | 439 |
| 2024-09-20 22:21:40.221 | MS1 | 121.4656624979 | 31.1446349402 | 835 | 504990 | -93.11 | 11.22 | 292.50 | 0.03 | 2.21 | 1588 |
| 2024-09-20 22:21:41.732 | MS1 | 121.4656690097 | 31.1446184743 | 835 | 504990 | -92.67 | 9.27 | 419.87 | 0.17 | 2.87 | 1578 |
| 2024-09-20 22:21:42.904 | MS1 | 121.4656639511 | 31.1446207588 | 835 | 504990 | -92.26 | 8.67 | 460.32 | 0.17 | 2.94 | 1571 |

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
| 3239571 | 2 | 121.4688453328 | 31.1499196676 | 149 | 13 | 8 | 20.9 | TDD | 437 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3245814 | 4 | 121.4687203420 | 31.1508440689 | 334 | 15 | 10 | 17.8 | TDD | 927 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3255898 | 3 | 121.4723234304 | 31.1527860456 | 135 | 8 | 1 | 21.6 | TDD | 669 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3268321 | 1 | 121.4728905706 | 31.1548381812 | 160 | 15 | 2 | 47.2 | TDD | 835 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.887 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.911 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.011 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.011 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.766 | NREventA3 | measId:2;ServCellPCI:707;Se... |
| 2024-09-20 22:21:38.006 | NRHandoverAttempt | SourcePCI:707;SourceNR-ARFC... |
| 2024-09-20 22:21:38.051 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.066 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.209 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.209 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268321 | 1 | 8.5148 | 14.4892 | -116.3028 | 14.9017 | 171.5296 | 0.0142 | 0.0065 |
| 2024_09_20 22:00 | 3239571 | 2 | 8.3339 | 11.5452 | -117.1638 | 10.3319 | 167.3961 | 0.0123 | 0.0187 |
| 2024_09_20 22:00 | 3255898 | 3 | 12.4709 | 13.4064 | -115.4425 | 11.7560 | 84.4977 | 0.0073 | 0.0078 |
| 2024_09_20 22:00 | 3245814 | 4 | 19.0909 | 15.5123 | -115.9288 | 13.2090 | 137.4683 | 0.0141 | 0.0138 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413671_BF9C65C2 | 504990 | 835 | -89.9 | 504990 | 437 | -87.8 | 504990 | 669 | -101.2 | 504990 | 927 |
| MR_1774413671_B5B70D2B | 504990 | 835 | -89.9 | 504990 | 437 | -88.2 | 504990 | 669 | -100.8 | 504990 | 927 |
| MR_1774413671_D7DB17C1 | 504990 | 835 | -89.0 | 504990 | 437 | -89.0 | 504990 | 669 | -100.1 | 504990 | 927 |
| MR_1774413671_A4EFE42A | 504990 | 835 | -89.3 | 504990 | 437 | -88.5 | 504990 | 669 | -101.2 | 504990 | 927 |
| MR_1774413671_F05567F1 | 504990 | 835 | -88.0 | 504990 | 437 | -89.7 | 504990 | 669 | -99.1 | 504990 | 927 |
| MR_1774413671_2A678387 | 504990 | 835 | -88.7 | 504990 | 437 | -88.6 | 504990 | 669 | -102.2 | 504990 | 927 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 89: `446ed34a-944...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `446ed34a-944e-40ae-80d1-8d0a99f10294` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[89] topology](images/test_0089.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3237782_2
- `C2`: Check test server and transmission issues
- `C3`: Lift the tilt angle of 3247513_4 by 9 degrees
- `C4`: Lift the tilt angle  of 3237782_2 by 4 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Add neighbor relationship between 3268395_1 and 3237782_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237782_2
- `C8`: Decrease A3 Offset threshold for 3247513_4
- `C9`: Press down the tilt angle  of 3237782_2 by 4 degrees
- `C10`: Decrease A3 Offset threshold for 3237782_2
- `C11`: Decrease transmission power for 3237782_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247513_4
- `C13`: Increase transmission power for 3247513_4
- `C14`: Increase A3 Offset threshold for 3237782_2
- `C15`: Add neighbor relationship between 3247513_4 and 3237782_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247513_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237782_2
- `C18`: Adjust the azimuth of 3237782_2 by 31 degrees
- `C19`: Decrease transmission power for 3247513_4
- `C20`: Adjust the azimuth of 3247513_4 by 50 degrees
- `C21`: Press down the tilt angle of 3247513_4 by 9 degrees
- `C22`: Increase A3 Offset threshold for 3247513_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.537 | MS1 | 121.4656676373 | 31.1446378273 | 375 | 504990 | -82.70 | 15.40 | 300.43 | 0.18 | 2.13 | 1571 |
| 2024-09-20 22:21:32.655 | MS1 | 121.4656617487 | 31.1446366685 | 375 | 504990 | -76.18 | 13.88 | 408.39 | 0.06 | 2.92 | 1594 |
| 2024-09-20 22:21:33.331 | MS1 | 121.4656634004 | 31.1446375852 | 375 | 504990 | -84.53 | 16.37 | 490.40 | 0.18 | 2.44 | 1586 |
| 2024-09-20 22:21:34.507 | MS1 | 121.4656584218 | 31.1446335493 | 375 | 504990 | -89.78 | -1.80 | 48.17 | 0.19 | 1.36 | 1572 |
| 2024-09-20 22:21:35.769 | MS1 | 121.4656608805 | 31.1446379844 | 375 | 504990 | -90.67 | -1.49 | 57.68 | 0.07 | 1.42 | 1582 |
| 2024-09-20 22:21:36.545 | MS1 | 121.4656770412 | 31.1446184039 | 375 | 504990 | -88.89 | -1.20 | 40.86 | 0.17 | 1.30 | 1577 |
| 2024-09-20 22:21:37.806 | MS1 | 121.4656655315 | 31.1446245741 | 375 | 504990 | -88.90 | -1.99 | 36.60 | 0.14 | 1.21 | 1580 |
| 2024-09-20 22:21:38.399 | MS1 | 121.4656711219 | 31.1446268263 | 375 | 504990 | -80.35 | 16.43 | 494.32 | 0.05 | 1.29 | 1572 |
| 2024-09-20 22:21:39.783 | MS1 | 121.4656743697 | 31.1446359646 | 375 | 504990 | -78.82 | 17.91 | 503.11 | 0.02 | 1.34 | 1588 |
| 2024-09-20 22:21:40.482 | MS1 | 121.4656638659 | 31.1446299671 | 375 | 504990 | -78.38 | 17.62 | 322.35 | 0.01 | 2.19 | 1568 |
| 2024-09-20 22:21:41.240 | MS1 | 121.4656764527 | 31.1446182378 | 375 | 504990 | -77.61 | 16.68 | 544.47 | 0.09 | 2.89 | 1567 |
| 2024-09-20 22:21:42.116 | MS1 | 121.4656653741 | 31.1446197707 | 375 | 504990 | -79.65 | 17.01 | 325.22 | 0.05 | 2.60 | 1578 |

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
| 3217303 | 3 | 121.4683182358 | 31.1467871382 | 160 | 14 | 4 | 22.2 | TDD | 982 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3237782 | 2 | 121.4690375527 | 31.1522536799 | 170 | 1 | 10 | 46.1 | TDD | 643 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3247513 | 4 | 121.4734087299 | 31.1536653405 | 28 | 7 | 12 | 37.5 | TDD | 375 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3268395 | 1 | 121.4755738728 | 31.1528392785 | 38 | 9 | 12 | 25.9 | TDD | 579 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.890 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.905 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.022 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.022 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.772 | NREventA3 | measId:2;ServCellPCI:965;Se... |
| 2024-09-20 22:21:35.772 | NREventA3 | measId:2;ServCellPCI:965;Se... |
| 2024-09-20 22:21:36.772 | NREventA3 | measId:2;ServCellPCI:965;Se... |
| 2024-09-20 22:21:39.272 | NRRRCReestablishAttempt | PCI:965 |
| 2024-09-20 22:21:39.285 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.299 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.443 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.443 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268395 | 1 | 6.4869 | 13.7344 | -117.0132 | 7.1634 | 176.1522 | 0.0182 | 0.0057 |
| 2024_09_20 22:00 | 3237782 | 2 | 5.9212 | 6.1555 | -115.9031 | 7.7246 | 192.2546 | 0.0082 | 0.0137 |
| 2024_09_20 22:00 | 3217303 | 3 | 14.8521 | 15.7835 | -115.6498 | 14.8067 | 117.9854 | 0.0183 | 0.0087 |
| 2024_09_20 22:00 | 3247513 | 4 | 7.6629 | 7.1177 | -114.7803 | 17.5163 | 152.1419 | 0.0132 | 0.1674 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415625_A3E4130F | 504990 | 643 | -84.8 | 504990 | 375 | -91.4 | 504990 | 579 | -86.1 | 504990 | 982 |
| MR_1774415625_B88C70EF | 504990 | 375 | -87.9 | 504990 | 643 | -84.7 | 504990 | 579 | -85.3 | 504990 | 982 |
| MR_1774415625_0FA653DA | 504990 | 643 | -87.2 | 504990 | 375 | -90.1 | 504990 | 579 | -85.7 | 504990 | 982 |
| MR_1774415625_0F4F450D | 504990 | 643 | -85.6 | 504990 | 375 | -90.7 | 504990 | 579 | -87.3 | 504990 | 982 |
| MR_1774415625_F9397632 | 504990 | 375 | -90.5 | 504990 | 643 | -84.1 | 504990 | 579 | -87.3 | 504990 | 982 |

> *... 2개 열 생략 (전체 14열)*

---
