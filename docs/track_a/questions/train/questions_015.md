# Track A 문제 분석 — train[140]~train[149]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[140] ~ train[149] (10개)

## 목차

1. [문제 140: `1dad2b9a-03f...`](#140) — single-answer, 정답: C16
2. [문제 141: `dbd58b5f-950...`](#141) — single-answer, 정답: C10
3. [문제 142: `b56a8930-c59...`](#142) — single-answer, 정답: C12
4. [문제 143: `89279e22-9e9...`](#143) — single-answer, 정답: C20
5. [문제 144: `f116a3d9-3d5...`](#144) — single-answer, 정답: C19
6. [문제 145: `778c4291-7fd...`](#145) — single-answer, 정답: C19
7. [문제 146: `e6811e56-33d...`](#146) — single-answer, 정답: C15
8. [문제 147: `da3d9337-0d6...`](#147) — single-answer, 정답: C1
9. [문제 148: `3da2462e-a0e...`](#148) — multiple-answer, 정답: C9|C13|C14|C16
10. [문제 149: `b2847ab1-3cc...`](#149) — multiple-answer, 정답: C15|C21

---

### 문제 140: `1dad2b9a-03f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1dad2b9a-03f4-4843-b75c-936b2e717fe1` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Add neighbor relationship between 3244557_1 and 3273175_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[140] topology](images/train_0140.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3273175_3 by 3 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273175_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244557_1
- `C4`: Decrease A3 Offset threshold for 3244557_1
- `C5`: Lift the tilt angle of 3244557_1 by 10 degrees
- `C6`: Adjust the azimuth of 3273175_3 by 6 degrees
- `C7`: Press down the tilt angle of 3244557_1 by 10 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase A3 Offset threshold for 3273175_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244557_1
- `C11`: Decrease transmission power for 3244557_1
- `C12`: Decrease A3 Offset threshold for 3273175_3
- `C13`: Check test server and transmission issues
- `C14`: Lift the tilt angle  of 3273175_3 by 3 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273175_3
- `C16`: Add neighbor relationship between 3244557_1 and 3273175_3 **← 정답**
- `C17`: Add neighbor relationship between 3259168_4 and 3273175_3
- `C18`: Increase transmission power for 3244557_1
- `C19`: Increase A3 Offset threshold for 3244557_1
- `C20`: Decrease transmission power for 3273175_3
- `C21`: Increase transmission power for 3273175_3
- `C22`: Adjust the azimuth of 3244557_1 by 34 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.789 | MS1 | 121.4656763628 | 31.1446354571 | 801 | 504990 | -76.18 | 12.60 | 368.54 | 0.02 | 2.14 | 1570 |
| 2024-09-20 22:21:32.496 | MS1 | 121.4656634975 | 31.1446353013 | 801 | 504990 | -83.61 | 15.46 | 555.03 | 0.13 | 2.19 | 1571 |
| 2024-09-20 22:21:33.200 | MS1 | 121.4656652578 | 31.1446292084 | 801 | 504990 | -77.07 | 17.91 | 561.71 | 0.10 | 2.09 | 1563 |
| 2024-09-20 22:21:34.285 | MS1 | 121.4656737748 | 31.1446348641 | 801 | 504990 | -92.68 | -2.48 | 42.86 | 0.14 | 1.46 | 1576 |
| 2024-09-20 22:21:35.360 | MS1 | 121.4656602236 | 31.1446376453 | 801 | 504990 | -91.93 | -0.48 | 64.84 | 0.11 | 1.05 | 1573 |
| 2024-09-20 22:21:36.494 | MS1 | 121.4656765412 | 31.1446288066 | 801 | 504990 | -93.45 | -1.54 | 56.48 | 0.03 | 1.27 | 1579 |
| 2024-09-20 22:21:37.679 | MS1 | 121.4656739092 | 31.1446185141 | 801 | 504990 | -89.41 | -0.95 | 60.99 | 0.15 | 1.35 | 1586 |
| 2024-09-20 22:21:38.484 | MS1 | 121.4656718720 | 31.1446267612 | 801 | 504990 | -83.40 | 15.30 | 535.48 | 0.16 | 1.05 | 1576 |
| 2024-09-20 22:21:39.114 | MS1 | 121.4656602013 | 31.1446376244 | 801 | 504990 | -84.83 | 13.05 | 293.92 | 0.14 | 1.20 | 1599 |
| 2024-09-20 22:21:40.937 | MS1 | 121.4656765101 | 31.1446216933 | 801 | 504990 | -75.71 | 16.35 | 422.69 | 0.06 | 2.61 | 1592 |
| 2024-09-20 22:21:41.925 | MS1 | 121.4656673324 | 31.1446265413 | 801 | 504990 | -83.40 | 12.44 | 307.52 | 0.09 | 2.82 | 1581 |
| 2024-09-20 22:21:42.540 | MS1 | 121.4656667740 | 31.1446277300 | 801 | 504990 | -84.86 | 15.62 | 546.53 | 0.12 | 2.79 | 1598 |

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
| 3242902 | 2 | 121.4662059791 | 31.1552340724 | 323 | 3 | 10 | 42.5 | TDD | 850 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3244557 | 1 | 121.4654949092 | 31.1463037037 | 141 | 1 | 7 | 37.0 | TDD | 801 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3259168 | 4 | 121.4744920526 | 31.1463414231 | 307 | 2 | 4 | 25.9 | TDD | 943 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3273175 | 3 | 121.4695642102 | 31.1506144056 | 203 | 0 | 4 | 34.0 | TDD | 773 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.568 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.593 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.719 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.719 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.392 | NREventA3 | measId:2;ServCellPCI:68;Ser... |
| 2024-09-20 22:21:36.392 | NREventA3 | measId:2;ServCellPCI:68;Ser... |
| 2024-09-20 22:21:37.392 | NREventA3 | measId:2;ServCellPCI:68;Ser... |
| 2024-09-20 22:21:39.892 | NRRRCReestablishAttempt | PCI:68 |
| 2024-09-20 22:21:39.912 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.922 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:40.046 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.046 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244557 | 1 | 7.0907 | 18.9496 | -114.8685 | 6.1256 | 119.8164 | 0.0139 | 0.1362 |
| 2024_09_20 22:00 | 3242902 | 2 | 18.4378 | 10.6195 | -117.0884 | 12.7839 | 129.0850 | 0.0054 | 0.0036 |
| 2024_09_20 22:00 | 3273175 | 3 | 9.7606 | 8.2376 | -115.9489 | 6.1370 | 87.2165 | 0.0068 | 0.0045 |
| 2024_09_20 22:00 | 3259168 | 4 | 16.4132 | 19.5345 | -114.7040 | 13.6229 | 161.3263 | 0.0124 | 0.0002 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412521_4FF0843D | 504990 | 801 | -91.3 | 504990 | 773 | -87.6 | 504990 | 943 | -91.9 | 504990 | 850 |
| MR_1774412521_6C17E290 | 504990 | 801 | -94.6 | 504990 | 773 | -88.1 | 504990 | 943 | -92.6 | 504990 | 850 |
| MR_1774412521_60132733 | 504990 | 801 | -92.8 | 504990 | 773 | -88.1 | 504990 | 943 | -91.4 | 504990 | 850 |
| MR_1774412521_EF6AE76B | 504990 | 801 | -91.0 | 504990 | 773 | -86.0 | 504990 | 943 | -92.4 | 504990 | 850 |
| MR_1774412521_BDAD7564 | 504990 | 773 | -88.9 | 504990 | 801 | -93.1 | 504990 | 943 | -90.5 | 504990 | 850 |
| MR_1774412521_A4302072 | 504990 | 801 | -92.1 | 504990 | 773 | -86.2 | 504990 | 943 | -89.7 | 504990 | 850 |
| MR_1774412521_665B2F9E | 504990 | 801 | -94.6 | 504990 | 773 | -88.2 | 504990 | 943 | -90.0 | 504990 | 850 |
| MR_1774412521_8B2E0861 | 504990 | 801 | -93.8 | 504990 | 773 | -87.2 | 504990 | 943 | -90.2 | 504990 | 850 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 141: `dbd58b5f-950...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dbd58b5f-950e-4e83-868b-3bdcb8583637` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Lift the tilt angle  of 3261232_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[141] topology](images/train_0141.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262501_1
- `C2`: Add neighbor relationship between 3261232_4 and 3276353_3
- `C3`: Decrease A3 Offset threshold for 3262501_1
- `C4`: Press down the tilt angle of 3262501_1 by 6 degrees
- `C5`: Add neighbor relationship between 3262501_1 and 3276353_3
- `C6`: Decrease transmission power for 3276353_3
- `C7`: Decrease transmission power for 3262501_1
- `C8`: Increase A3 Offset threshold for 3276353_3
- `C9`: Press down the tilt angle  of 3261232_4 by 10 degrees
- `C10`: Lift the tilt angle  of 3261232_4 by 10 degrees **← 정답**
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase transmission power for 3276353_3
- `C13`: Decrease A3 Offset threshold for 3276353_3
- `C14`: Increase transmission power for 3262501_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262501_1
- `C16`: Increase A3 Offset threshold for 3262501_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276353_3
- `C18`: Lift the tilt angle of 3262501_1 by 6 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276353_3
- `C20`: Adjust the azimuth of 3262501_1 by 4 degrees
- `C21`: Adjust the azimuth of 3261232_4 by 49 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.665 | MS1 | 121.4656762698 | 31.1446286236 | 280 | 504990 | -90.98 | 12.80 | 484.86 | 0.19 | 2.98 | 1591 |
| 2024-09-20 22:21:32.419 | MS1 | 121.4656772123 | 31.1446217823 | 280 | 504990 | -86.29 | 12.36 | 553.23 | 0.01 | 2.21 | 1578 |
| 2024-09-20 22:21:33.924 | MS1 | 121.4656621782 | 31.1446331100 | 280 | 504990 | -89.02 | 14.92 | 383.49 | 0.18 | 2.85 | 1584 |
| 2024-09-20 22:21:34.282 | MS1 | 121.4656654832 | 31.1446357655 | 280 | 504990 | -87.89 | 12.31 | 88.52 | 0.04 | 2.73 | 1574 |
| 2024-09-20 22:21:35.946 | MS1 | 121.4656765628 | 31.1446311050 | 280 | 504990 | -89.86 | 12.34 | 93.51 | 0.14 | 2.67 | 1573 |
| 2024-09-20 22:21:36.483 | MS1 | 121.4656703902 | 31.1446242782 | 280 | 504990 | -89.62 | 17.23 | 72.49 | 0.19 | 2.16 | 1588 |
| 2024-09-20 22:21:37.319 | MS1 | 121.4656720663 | 31.1446218142 | 280 | 504990 | -93.45 | 9.56 | 90.81 | 0.06 | 2.36 | 1564 |
| 2024-09-20 22:21:38.355 | MS1 | 121.4656638238 | 31.1446258664 | 280 | 504990 | -93.73 | 11.18 | 55.57 | 0.08 | 2.96 | 1573 |
| 2024-09-20 22:21:39.323 | MS1 | 121.4656763032 | 31.1446255492 | 280 | 504990 | -92.24 | 7.40 | 64.18 | 0.05 | 2.98 | 1574 |
| 2024-09-20 22:21:40.782 | MS1 | 121.4656660258 | 31.1446295268 | 280 | 504990 | -90.79 | 12.64 | 438.86 | 0.04 | 2.85 | 1560 |
| 2024-09-20 22:21:41.607 | MS1 | 121.4656716017 | 31.1446266043 | 280 | 504990 | -89.28 | 12.16 | 440.40 | 0.06 | 2.46 | 1590 |
| 2024-09-20 22:21:42.998 | MS1 | 121.4656655914 | 31.1446356617 | 280 | 504990 | -92.06 | 12.98 | 350.86 | 0.08 | 2.01 | 1569 |

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
| 3230911 | 2 | 121.4743133208 | 31.1467890167 | 335 | 8 | 10 | 18.8 | TDD | 626 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3261232 | 4 | 121.4670429358 | 31.1533081390 | 83 | 5 | 12 | 42.2 | TDD | 77 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3262501 | 1 | 121.4692301465 | 31.1493269477 | 209 | 3 | 8 | 29.1 | TDD | 280 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3276353 | 3 | 121.4703964894 | 31.1467765386 | 291 | 11 | 9 | 30.0 | TDD | 716 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.473 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.493 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.636 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.636 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.300 | NREventA3 | measId:2;ServCellPCI:525;Se... |
| 2024-09-20 22:21:38.540 | NRHandoverAttempt | SourcePCI:525;SourceNR-ARFC... |
| 2024-09-20 22:21:38.571 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.583 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.723 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.723 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262501 | 1 | 76.8058 | 89.8995 | -114.9802 | 18.6750 | 108.0684 | 0.0115 | 0.0167 |
| 2024_09_20 22:00 | 3230911 | 2 | 17.9707 | 13.8560 | -117.4553 | 13.7090 | 100.7149 | 0.0184 | 0.0141 |
| 2024_09_20 22:00 | 3276353 | 3 | 16.5896 | 14.8250 | -116.6451 | 8.4815 | 190.8532 | 0.0132 | 0.0171 |
| 2024_09_20 22:00 | 3261232 | 4 | 8.8423 | 19.2237 | -116.5959 | 17.0104 | 95.2908 | 0.0190 | 0.0133 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415906_5C27DBD6 | 504990 | 280 | -88.0 | 504990 | 716 | -87.7 | 504990 | 77 | -100.9 | 504990 | 626 |
| MR_1774415906_95B75D0D | 504990 | 280 | -86.6 | 504990 | 716 | -89.4 | 504990 | 77 | -100.7 | 504990 | 626 |
| MR_1774415906_4F067C9D | 504990 | 280 | -89.4 | 504990 | 716 | -85.8 | 504990 | 77 | -99.7 | 504990 | 626 |
| MR_1774415906_42C00924 | 504990 | 280 | -87.7 | 504990 | 716 | -88.8 | 504990 | 77 | -100.1 | 504990 | 626 |
| MR_1774415906_A5203906 | 504990 | 280 | -88.3 | 504990 | 716 | -89.4 | 504990 | 77 | -102.7 | 504990 | 626 |
| MR_1774415906_C7CEC517 | 504990 | 280 | -89.5 | 504990 | 716 | -89.3 | 504990 | 77 | -99.5 | 504990 | 626 |
| MR_1774415906_AE74A4D6 | 504990 | 280 | -86.1 | 504990 | 716 | -86.4 | 504990 | 77 | -101.4 | 504990 | 626 |
| MR_1774415906_C95BA42F | 504990 | 280 | -89.3 | 504990 | 716 | -87.3 | 504990 | 77 | -101.3 | 504990 | 626 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 142: `b56a8930-c59...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b56a8930-c59d-48ed-b246-67be7edd85a9` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3263669_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[142] topology](images/train_0142.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227352_2
- `C2`: Decrease transmission power for 3263669_1
- `C3`: Increase A3 Offset threshold for 3263669_1
- `C4`: Press down the tilt angle of 3263669_1 by 3 degrees
- `C5`: Decrease A3 Offset threshold for 3263669_1
- `C6`: Lift the tilt angle of 3263669_1 by 3 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227352_2
- `C8`: Lift the tilt angle  of 3227352_2 by 10 degrees
- `C9`: Increase transmission power for 3227352_2
- `C10`: Decrease A3 Offset threshold for 3227352_2
- `C11`: Adjust the azimuth of 3263669_1 by 20 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263669_1 **← 정답**
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263669_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Check test server and transmission issues
- `C16`: Increase A3 Offset threshold for 3227352_2
- `C17`: Press down the tilt angle  of 3227352_2 by 10 degrees
- `C18`: Decrease transmission power for 3227352_2
- `C19`: Adjust the azimuth of 3227352_2 by 50 degrees
- `C20`: Increase transmission power for 3263669_1
- `C21`: Add neighbor relationship between 3263669_1 and 3227352_2
- `C22`: Add neighbor relationship between 3244356_3 and 3227352_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.997 | MS1 | 121.4656709238 | 31.1446337415 | 808 | 504990 | -88.77 | 12.18 | 387.23 | 0.05 | 2.23 | 1595 |
| 2024-09-20 22:21:32.959 | MS1 | 121.4656587753 | 31.1446370423 | 808 | 504990 | -88.76 | 17.19 | 512.94 | 0.14 | 2.68 | 1564 |
| 2024-09-20 22:21:33.663 | MS1 | 121.4656715990 | 31.1446249535 | 808 | 504990 | -85.28 | 17.04 | 568.10 | 0.12 | 2.16 | 1561 |
| 2024-09-20 22:21:34.165 | MS1 | 121.4656662993 | 31.1446306345 | 808 | 504990 | -90.33 | 13.77 | 62.08 | 0.70 | 2.22 | 523 |
| 2024-09-20 22:21:35.991 | MS1 | 121.4656744400 | 31.1446238010 | 808 | 504990 | -86.85 | 16.47 | 80.69 | 0.54 | 2.42 | 696 |
| 2024-09-20 22:21:36.430 | MS1 | 121.4656779039 | 31.1446285049 | 808 | 504990 | -87.97 | 13.27 | 77.52 | 0.67 | 2.71 | 623 |
| 2024-09-20 22:21:37.339 | MS1 | 121.4656713437 | 31.1446244249 | 808 | 504990 | -92.54 | 11.07 | 90.00 | 0.60 | 2.94 | 579 |
| 2024-09-20 22:21:38.342 | MS1 | 121.4656736580 | 31.1446209016 | 808 | 504990 | -90.54 | 10.63 | 82.60 | 0.54 | 2.33 | 660 |
| 2024-09-20 22:21:39.966 | MS1 | 121.4656712603 | 31.1446285838 | 808 | 504990 | -93.96 | 12.22 | 65.14 | 0.52 | 2.32 | 508 |
| 2024-09-20 22:21:40.918 | MS1 | 121.4656637656 | 31.1446202731 | 808 | 504990 | -90.22 | 11.10 | 426.82 | 0.07 | 2.50 | 1570 |
| 2024-09-20 22:21:41.117 | MS1 | 121.4656606876 | 31.1446219720 | 808 | 504990 | -91.42 | 8.07 | 573.36 | 0.01 | 2.52 | 1572 |
| 2024-09-20 22:21:42.941 | MS1 | 121.4656701667 | 31.1446360382 | 808 | 504990 | -93.42 | 10.62 | 361.39 | 0.15 | 2.24 | 1562 |

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
| 3218981 | 4 | 121.4708428961 | 31.1447415709 | 84 | 12 | 3 | 30.1 | TDD | 29 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3227352 | 2 | 121.4688238831 | 31.1504178276 | 59 | 11 | 8 | 19.3 | TDD | 562 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3244356 | 3 | 121.4709269332 | 31.1463133128 | 134 | 15 | 5 | 15.3 | TDD | 109 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3263669 | 1 | 121.4715302657 | 31.1556192083 | 225 | 1 | 3 | 45.5 | TDD | 808 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.870 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.987 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.987 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.723 | NREventA3 | measId:2;ServCellPCI:413;Se... |
| 2024-09-20 22:21:37.963 | NRHandoverAttempt | SourcePCI:413;SourceNR-ARFC... |
| 2024-09-20 22:21:38.011 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.023 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.166 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.166 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263669 | 1 | 10.3518 | 13.9922 | -114.2510 | 12.0220 | 197.3897 | 0.0142 | 0.0190 |
| 2024_09_20 22:00 | 3227352 | 2 | 17.9944 | 15.5176 | -117.8761 | 9.2331 | 187.8233 | 0.0070 | 0.0164 |
| 2024_09_20 22:00 | 3244356 | 3 | 10.4259 | 12.9183 | -117.0481 | 11.0772 | 158.2074 | 0.0194 | 0.0123 |
| 2024_09_20 22:00 | 3218981 | 4 | 9.3426 | 19.7552 | -117.5142 | 18.4671 | 103.8951 | 0.0093 | 0.0135 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414360_7C7BF9D9 | 504990 | 808 | -91.1 | 504990 | 562 | -96.1 | 504990 | 109 | -100.7 | 504990 | 29 |
| MR_1774414360_7297D018 | 504990 | 808 | -89.8 | 504990 | 562 | -94.0 | 504990 | 109 | -101.7 | 504990 | 29 |
| MR_1774414360_FA6F1301 | 504990 | 808 | -91.9 | 504990 | 562 | -96.8 | 504990 | 109 | -100.6 | 504990 | 29 |
| MR_1774414360_82D62A94 | 504990 | 808 | -90.0 | 504990 | 562 | -97.0 | 504990 | 109 | -100.6 | 504990 | 29 |
| MR_1774414360_CF25C0E0 | 504990 | 808 | -88.4 | 504990 | 562 | -94.5 | 504990 | 109 | -103.7 | 504990 | 29 |
| MR_1774414360_972D3C0F | 504990 | 808 | -90.5 | 504990 | 562 | -93.2 | 504990 | 109 | -100.1 | 504990 | 29 |
| MR_1774414360_C585C826 | 504990 | 808 | -91.1 | 504990 | 562 | -93.1 | 504990 | 109 | -103.3 | 504990 | 29 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 143: `89279e22-9e9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `89279e22-9e99-4a39-aede-f18d263dc3b6` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease A3 Offset threshold for 3269349_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[143] topology](images/train_0143.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3269349_1
- `C2`: Add neighbor relationship between 3225308_3 and 3229508_2
- `C3`: Press down the tilt angle  of 3229508_2 by 10 degrees
- `C4`: Add neighbor relationship between 3269349_1 and 3229508_2
- `C5`: Increase transmission power for 3229508_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269349_1
- `C7`: Increase A3 Offset threshold for 3269349_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229508_2
- `C9`: Lift the tilt angle  of 3229508_2 by 10 degrees
- `C10`: Decrease A3 Offset threshold for 3229508_2
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase transmission power for 3269349_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229508_2
- `C14`: Adjust the azimuth of 3269349_1 by 50 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269349_1
- `C16`: Check test server and transmission issues
- `C17`: Increase A3 Offset threshold for 3229508_2
- `C18`: Press down the tilt angle of 3269349_1 by 3 degrees
- `C19`: Adjust the azimuth of 3229508_2 by 50 degrees
- `C20`: Decrease A3 Offset threshold for 3269349_1 **← 정답**
- `C21`: Lift the tilt angle of 3269349_1 by 3 degrees
- `C22`: Decrease transmission power for 3229508_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.578 | MS1 | 121.4656650771 | 31.1446227195 | 721 | 504990 | -83.13 | 17.62 | 562.06 | 0.16 | 2.12 | 1596 |
| 2024-09-20 22:21:32.776 | MS1 | 121.4656662042 | 31.1446192778 | 721 | 504990 | -84.06 | 12.94 | 457.91 | 0.14 | 2.65 | 1588 |
| 2024-09-20 22:21:33.938 | MS1 | 121.4656687133 | 31.1446205559 | 721 | 504990 | -77.67 | 12.51 | 385.00 | 0.14 | 2.33 | 1597 |
| 2024-09-20 22:21:34.411 | MS1 | 121.4656658605 | 31.1446352309 | 721 | 504990 | -85.14 | -2.07 | 44.70 | 0.17 | 1.01 | 1571 |
| 2024-09-20 22:21:35.279 | MS1 | 121.4656612942 | 31.1446350901 | 721 | 504990 | -83.81 | -0.84 | 44.66 | 0.06 | 1.45 | 1587 |
| 2024-09-20 22:21:36.779 | MS1 | 121.4656698567 | 31.1446337452 | 721 | 504990 | -83.99 | -3.70 | 38.78 | 0.14 | 1.23 | 1560 |
| 2024-09-20 22:21:37.336 | MS1 | 121.4656685234 | 31.1446284696 | 721 | 504990 | -87.42 | -1.77 | 62.66 | 0.16 | 1.32 | 1560 |
| 2024-09-20 22:21:38.463 | MS1 | 121.4656664736 | 31.1446257844 | 721 | 504990 | -87.43 | -1.56 | 74.07 | 0.02 | 1.18 | 1586 |
| 2024-09-20 22:21:39.484 | MS1 | 121.4656730640 | 31.1446252445 | 203 | 504990 | -84.97 | 12.19 | 171.95 | 0.07 | 1.16 | 1567 |
| 2024-09-20 22:21:40.886 | MS1 | 121.4656699166 | 31.1446332370 | 203 | 504990 | -84.18 | 17.17 | 440.57 | 0.01 | 2.32 | 1571 |
| 2024-09-20 22:21:41.541 | MS1 | 121.4656600489 | 31.1446243409 | 203 | 504990 | -78.96 | 15.19 | 387.90 | 0.15 | 2.24 | 1581 |
| 2024-09-20 22:21:42.722 | MS1 | 121.4656581132 | 31.1446236552 | 203 | 504990 | -77.69 | 13.94 | 398.66 | 0.04 | 2.79 | 1560 |

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
| 3225308 | 3 | 121.4688404326 | 31.1556889057 | 267 | 14 | 3 | 17.0 | TDD | 139 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3229508 | 2 | 121.4688598642 | 31.1443821625 | 55 | 4 | 12 | 29.4 | TDD | 203 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3252733 | 4 | 121.4687579009 | 31.1448016656 | 269 | 5 | 1 | 46.0 | TDD | 119 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3269349 | 1 | 121.4758412877 | 31.1502410272 | 322 | 2 | 5 | 27.2 | TDD | 721 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.823 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.847 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.957 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.957 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.631 | NREventA3 | measId:2;ServCellPCI:166;Se... |
| 2024-09-20 22:21:37.871 | NRHandoverAttempt | SourcePCI:166;SourceNR-ARFC... |
| 2024-09-20 22:21:37.905 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.917 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.025 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.025 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269349 | 1 | 19.5835 | 16.1176 | -115.1358 | 5.1197 | 136.2816 | 0.0136 | 0.1137 |
| 2024_09_20 22:00 | 3229508 | 2 | 8.1480 | 18.3496 | -116.3336 | 5.8257 | 139.8150 | 0.0064 | 0.0190 |
| 2024_09_20 22:00 | 3225308 | 3 | 19.5190 | 11.1180 | -114.3917 | 14.8204 | 154.7547 | 0.0004 | 0.0159 |
| 2024_09_20 22:00 | 3252733 | 4 | 17.8181 | 9.6619 | -114.4308 | 14.3927 | 192.7585 | 0.0080 | 0.0041 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415804_FD4D3A8C | 504990 | 721 | -86.9 | 504990 | 203 | -80.3 | 504990 | 139 | -88.2 | 504990 | 119 |
| MR_1774415804_62951806 | 504990 | 203 | -80.6 | 504990 | 721 | -85.6 | 504990 | 139 | -86.9 | 504990 | 119 |
| MR_1774415804_C5FC5228 | 504990 | 203 | -78.4 | 504990 | 721 | -86.0 | 504990 | 139 | -88.4 | 504990 | 119 |
| MR_1774415804_4EE4DB32 | 504990 | 721 | -85.3 | 504990 | 203 | -82.3 | 504990 | 139 | -87.5 | 504990 | 119 |
| MR_1774415804_880F7839 | 504990 | 203 | -81.0 | 504990 | 721 | -84.2 | 504990 | 139 | -85.7 | 504990 | 119 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 144: `f116a3d9-3d5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f116a3d9-3d58-4fa0-994a-4b089b17a627` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[144] topology](images/train_0144.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3254878_3
- `C2`: Adjust the azimuth of 3257721_2 by 50 degrees
- `C3`: Add neighbor relationship between 3254878_3 and 3257721_2
- `C4`: Lift the tilt angle of 3254878_3 by 10 degrees
- `C5`: Decrease A3 Offset threshold for 3254878_3
- `C6`: Increase transmission power for 3257721_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254878_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257721_2
- `C9`: Press down the tilt angle of 3254878_3 by 10 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257721_2
- `C11`: Lift the tilt angle  of 3257721_2 by 10 degrees
- `C12`: Add neighbor relationship between 3246966_4 and 3257721_2
- `C13`: Increase A3 Offset threshold for 3257721_2
- `C14`: Press down the tilt angle  of 3257721_2 by 10 degrees
- `C15`: Adjust the azimuth of 3254878_3 by 50 degrees
- `C16`: Decrease transmission power for 3257721_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254878_3
- `C18`: Check test server and transmission issues
- `C19`: Insufficient data; more data is needed for judgment. **← 정답**
- `C20`: Increase transmission power for 3254878_3
- `C21`: Increase A3 Offset threshold for 3254878_3
- `C22`: Decrease A3 Offset threshold for 3257721_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.147 | MS1 | 121.4656775045 | 31.1446254421 | 862 | 504990 | -90.67 | 15.65 | 321.65 | 0.09 | 2.26 | 1563 |
| 2024-09-20 22:21:32.351 | MS1 | 121.4656638069 | 31.1446298302 | 862 | 504990 | -85.32 | 13.17 | 490.66 | 0.07 | 2.27 | 1575 |
| 2024-09-20 22:21:33.821 | MS1 | 121.4656776434 | 31.1446266278 | 862 | 504990 | -85.47 | 14.38 | 586.94 | 0.12 | 2.58 | 1590 |
| 2024-09-20 22:21:34.513 | MS1 | 121.4656624984 | 31.1446368101 | 862 | 504990 | -86.38 | 14.61 | 95.28 | 0.13 | 2.73 | 1598 |
| 2024-09-20 22:21:35.449 | MS1 | 121.4656738080 | 31.1446227792 | 862 | 504990 | -90.59 | 15.99 | 48.76 | 0.18 | 2.38 | 1575 |
| 2024-09-20 22:21:36.103 | MS1 | 121.4656663255 | 31.1446264888 | 862 | 504990 | -89.68 | 14.47 | 70.43 | 0.04 | 2.63 | 1580 |
| 2024-09-20 22:21:37.317 | MS1 | 121.4656583590 | 31.1446301774 | 862 | 504990 | -89.16 | 7.44 | 91.04 | 0.09 | 2.36 | 1575 |
| 2024-09-20 22:21:38.100 | MS1 | 121.4656619884 | 31.1446353125 | 862 | 504990 | -89.50 | 10.37 | 65.02 | 0.03 | 2.47 | 1600 |
| 2024-09-20 22:21:39.936 | MS1 | 121.4656585679 | 31.1446309371 | 862 | 504990 | -93.77 | 9.60 | 87.65 | 0.01 | 2.32 | 1590 |
| 2024-09-20 22:21:40.999 | MS1 | 121.4656684019 | 31.1446362725 | 862 | 504990 | -93.11 | 9.83 | 565.48 | 0.20 | 2.99 | 1576 |
| 2024-09-20 22:21:41.316 | MS1 | 121.4656686434 | 31.1446372021 | 862 | 504990 | -90.87 | 7.99 | 589.18 | 0.19 | 2.43 | 1568 |
| 2024-09-20 22:21:42.258 | MS1 | 121.4656683232 | 31.1446367791 | 862 | 504990 | -92.47 | 11.85 | 545.47 | 0.04 | 2.90 | 1584 |

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
| 3241782 | 1 | 121.4690296719 | 31.1539637334 | 273 | 13 | 10 | 47.3 | TDD | 297 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3246966 | 4 | 121.4720787756 | 31.1548903563 | 207 | 11 | 1 | 41.6 | TDD | 535 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3254878 | 3 | 121.4719006865 | 31.1471574121 | 296 | 7 | 8 | 40.1 | TDD | 862 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3257721 | 2 | 121.4715667874 | 31.1443376220 | 29 | 12 | 7 | 41.5 | TDD | 20 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.443 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.464 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.586 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.586 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.333 | NREventA3 | measId:2;ServCellPCI:174;Se... |
| 2024-09-20 22:21:38.573 | NRHandoverAttempt | SourcePCI:174;SourceNR-ARFC... |
| 2024-09-20 22:21:38.604 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.617 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.735 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.735 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3241782 | 1 | 83.2181 | 85.3255 | -115.4157 | 8.7465 | 162.2023 | 0.0040 | 0.0085 |
| 2024_09_19 22:00 | 3257721 | 2 | 84.7290 | 77.5017 | -116.7033 | 5.4301 | 183.0014 | 0.0038 | 0.0113 |
| 2024_09_19 22:00 | 3254878 | 3 | 92.3712 | 94.9653 | -116.5771 | 14.7296 | 107.9562 | 0.0001 | 0.0072 |
| 2024_09_19 22:00 | 3246966 | 4 | 86.6745 | 89.1242 | -114.0712 | 5.6489 | 133.6586 | 0.0074 | 0.0111 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413525_2F4B26A2 | 504990 | 862 | -85.5 | 504990 | 20 | -90.3 | 504990 | 535 | -95.2 | 504990 | 297 |
| MR_1774413525_2EAA8F9B | 504990 | 862 | -84.9 | 504990 | 20 | -91.0 | 504990 | 535 | -98.0 | 504990 | 297 |
| MR_1774413525_8576A4C9 | 504990 | 862 | -86.3 | 504990 | 20 | -93.2 | 504990 | 535 | -97.5 | 504990 | 297 |
| MR_1774413525_72E371B7 | 504990 | 862 | -87.2 | 504990 | 20 | -93.3 | 504990 | 535 | -97.4 | 504990 | 297 |
| MR_1774413525_FF736B94 | 504990 | 862 | -87.2 | 504990 | 20 | -93.3 | 504990 | 535 | -96.9 | 504990 | 297 |
| MR_1774413525_8EEAC5D6 | 504990 | 862 | -87.8 | 504990 | 20 | -93.2 | 504990 | 535 | -96.0 | 504990 | 297 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 145: `778c4291-7fd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `778c4291-7fdc-4b40-b281-d5854268c1ae` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Lift the tilt angle  of 3261653_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[145] topology](images/train_0145.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3277858_1 by 6 degrees
- `C2`: Add neighbor relationship between 3277858_1 and 3238151_4
- `C3`: Add neighbor relationship between 3261653_2 and 3238151_4
- `C4`: Increase A3 Offset threshold for 3238151_4
- `C5`: Press down the tilt angle of 3277858_1 by 6 degrees
- `C6`: Adjust the azimuth of 3261653_2 by 12 degrees
- `C7`: Press down the tilt angle  of 3261653_2 by 10 degrees
- `C8`: Decrease transmission power for 3277858_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277858_1
- `C10`: Adjust the azimuth of 3277858_1 by 21 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238151_4
- `C12`: Decrease A3 Offset threshold for 3277858_1
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Increase transmission power for 3277858_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277858_1
- `C16`: Increase A3 Offset threshold for 3277858_1
- `C17`: Increase transmission power for 3238151_4
- `C18`: Check test server and transmission issues
- `C19`: Lift the tilt angle  of 3261653_2 by 10 degrees **← 정답**
- `C20`: Decrease A3 Offset threshold for 3238151_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238151_4
- `C22`: Decrease transmission power for 3238151_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.138 | MS1 | 121.4656767528 | 31.1446282979 | 793 | 504990 | -85.78 | 12.60 | 328.39 | 0.16 | 2.85 | 1566 |
| 2024-09-20 22:21:32.126 | MS1 | 121.4656584366 | 31.1446194634 | 793 | 504990 | -91.75 | 13.81 | 587.02 | 0.15 | 2.81 | 1592 |
| 2024-09-20 22:21:33.872 | MS1 | 121.4656592707 | 31.1446328351 | 793 | 504990 | -89.81 | 17.02 | 430.78 | 0.14 | 2.69 | 1566 |
| 2024-09-20 22:21:34.394 | MS1 | 121.4656633627 | 31.1446203778 | 793 | 504990 | -86.21 | 14.66 | 80.68 | 0.06 | 2.30 | 1573 |
| 2024-09-20 22:21:35.237 | MS1 | 121.4656586727 | 31.1446364648 | 793 | 504990 | -86.91 | 13.94 | 76.50 | 0.02 | 2.99 | 1581 |
| 2024-09-20 22:21:36.611 | MS1 | 121.4656698161 | 31.1446349189 | 793 | 504990 | -86.72 | 13.15 | 89.64 | 0.17 | 2.63 | 1568 |
| 2024-09-20 22:21:37.527 | MS1 | 121.4656636195 | 31.1446377893 | 793 | 504990 | -89.68 | 12.36 | 90.97 | 0.14 | 2.91 | 1596 |
| 2024-09-20 22:21:38.876 | MS1 | 121.4656769363 | 31.1446231185 | 793 | 504990 | -90.81 | 12.71 | 87.93 | 0.06 | 2.17 | 1595 |
| 2024-09-20 22:21:39.451 | MS1 | 121.4656609539 | 31.1446342706 | 793 | 504990 | -89.23 | 12.10 | 77.56 | 0.16 | 2.30 | 1573 |
| 2024-09-20 22:21:40.765 | MS1 | 121.4656694422 | 31.1446363241 | 793 | 504990 | -92.69 | 12.23 | 379.06 | 0.02 | 2.60 | 1596 |
| 2024-09-20 22:21:41.918 | MS1 | 121.4656729597 | 31.1446245074 | 793 | 504990 | -90.34 | 8.97 | 585.96 | 0.09 | 2.01 | 1576 |
| 2024-09-20 22:21:42.254 | MS1 | 121.4656643705 | 31.1446185812 | 793 | 504990 | -92.59 | 7.68 | 557.79 | 0.12 | 2.56 | 1590 |

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
| 3213954 | 3 | 121.4723711235 | 31.1493021181 | 77 | 15 | 2 | 49.6 | TDD | 238 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3238151 | 4 | 121.4669828532 | 31.1515629264 | 201 | 11 | 3 | 19.5 | TDD | 513 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3261653 | 2 | 121.4712480190 | 31.1513376484 | 324 | 8 | 8 | 41.7 | TDD | 887 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3277858 | 1 | 121.4755834436 | 31.1543420786 | 200 | 4 | 10 | 46.1 | TDD | 793 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.862 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.886 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.993 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.993 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.678 | NREventA3 | measId:2;ServCellPCI:284;Se... |
| 2024-09-20 22:21:37.918 | NRHandoverAttempt | SourcePCI:284;SourceNR-ARFC... |
| 2024-09-20 22:21:37.963 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.975 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.112 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.112 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277858 | 1 | 91.1102 | 77.5670 | -115.6793 | 14.6150 | 189.9131 | 0.0032 | 0.0137 |
| 2024_09_20 22:00 | 3261653 | 2 | 14.8489 | 7.2040 | -115.9243 | 13.2774 | 153.1014 | 0.0084 | 0.0043 |
| 2024_09_20 22:00 | 3213954 | 3 | 8.6800 | 10.5780 | -117.4181 | 8.3140 | 143.6713 | 0.0186 | 0.0082 |
| 2024_09_20 22:00 | 3238151 | 4 | 7.9688 | 18.0538 | -117.6176 | 19.8939 | 158.9160 | 0.0097 | 0.0081 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414733_ED3CA2F7 | 504990 | 793 | -85.7 | 504990 | 513 | -97.5 | 504990 | 887 | -97.0 | 504990 | 238 |
| MR_1774414733_6D2F9E52 | 504990 | 793 | -84.9 | 504990 | 513 | -97.2 | 504990 | 887 | -98.9 | 504990 | 238 |
| MR_1774414733_D9F8C6E0 | 504990 | 793 | -85.8 | 504990 | 513 | -94.1 | 504990 | 887 | -99.7 | 504990 | 238 |
| MR_1774414733_74A4C615 | 504990 | 793 | -86.7 | 504990 | 513 | -96.2 | 504990 | 887 | -96.5 | 504990 | 238 |
| MR_1774414733_68AA5AC1 | 504990 | 793 | -85.0 | 504990 | 513 | -97.5 | 504990 | 887 | -97.1 | 504990 | 238 |
| MR_1774414733_4EA32949 | 504990 | 793 | -86.0 | 504990 | 513 | -95.3 | 504990 | 887 | -99.2 | 504990 | 238 |
| MR_1774414733_9AFF83F2 | 504990 | 793 | -87.1 | 504990 | 513 | -95.7 | 504990 | 887 | -98.6 | 504990 | 238 |
| MR_1774414733_21DE9890 | 504990 | 793 | -86.3 | 504990 | 513 | -96.2 | 504990 | 887 | -97.9 | 504990 | 238 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 146: `e6811e56-33d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e6811e56-33dc-48a9-ae09-9fb3bce2293d` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease A3 Offset threshold for 3255836_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[146] topology](images/train_0146.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Lift the tilt angle of 3255836_1 by 10 degrees
- `C3`: Decrease A3 Offset threshold for 3265356_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255836_1
- `C5`: Adjust the azimuth of 3255836_1 by 50 degrees
- `C6`: Add neighbor relationship between 3255836_1 and 3265356_3
- `C7`: Check test server and transmission issues
- `C8`: Increase A3 Offset threshold for 3255836_1
- `C9`: Add neighbor relationship between 3222375_4 and 3265356_3
- `C10`: Decrease transmission power for 3265356_3
- `C11`: Increase A3 Offset threshold for 3265356_3
- `C12`: Increase transmission power for 3265356_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265356_3
- `C14`: Decrease transmission power for 3255836_1
- `C15`: Decrease A3 Offset threshold for 3255836_1 **← 정답**
- `C16`: Increase transmission power for 3255836_1
- `C17`: Adjust the azimuth of 3265356_3 by 50 degrees
- `C18`: Press down the tilt angle of 3255836_1 by 10 degrees
- `C19`: Press down the tilt angle  of 3265356_3 by 10 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265356_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255836_1
- `C22`: Lift the tilt angle  of 3265356_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.739 | MS1 | 121.4656580972 | 31.1446313998 | 680 | 504990 | -83.99 | 17.72 | 541.32 | 0.08 | 2.41 | 1597 |
| 2024-09-20 22:21:32.820 | MS1 | 121.4656617845 | 31.1446226074 | 680 | 504990 | -84.63 | 15.08 | 358.99 | 0.13 | 2.97 | 1598 |
| 2024-09-20 22:21:33.406 | MS1 | 121.4656624904 | 31.1446189011 | 680 | 504990 | -83.17 | 14.80 | 538.02 | 0.05 | 2.31 | 1577 |
| 2024-09-20 22:21:34.362 | MS1 | 121.4656777199 | 31.1446237895 | 680 | 504990 | -91.32 | -3.40 | 33.22 | 0.01 | 1.05 | 1591 |
| 2024-09-20 22:21:35.565 | MS1 | 121.4656704078 | 31.1446281079 | 680 | 504990 | -89.42 | -3.34 | 36.32 | 0.04 | 1.12 | 1598 |
| 2024-09-20 22:21:36.355 | MS1 | 121.4656642424 | 31.1446321266 | 680 | 504990 | -86.32 | -3.41 | 73.96 | 0.14 | 1.34 | 1564 |
| 2024-09-20 22:21:37.217 | MS1 | 121.4656659140 | 31.1446225527 | 680 | 504990 | -83.46 | -0.18 | 35.83 | 0.07 | 1.16 | 1598 |
| 2024-09-20 22:21:38.960 | MS1 | 121.4656725454 | 31.1446362004 | 680 | 504990 | -90.10 | -3.98 | 61.29 | 0.04 | 1.26 | 1591 |
| 2024-09-20 22:21:39.604 | MS1 | 121.4656760020 | 31.1446243489 | 734 | 504990 | -75.13 | 15.71 | 235.82 | 0.13 | 1.06 | 1583 |
| 2024-09-20 22:21:40.428 | MS1 | 121.4656609151 | 31.1446375274 | 734 | 504990 | -75.63 | 15.89 | 566.04 | 0.15 | 2.22 | 1574 |
| 2024-09-20 22:21:41.577 | MS1 | 121.4656767011 | 31.1446214910 | 734 | 504990 | -84.45 | 13.91 | 396.15 | 0.13 | 2.60 | 1575 |
| 2024-09-20 22:21:42.748 | MS1 | 121.4656624343 | 31.1446199548 | 734 | 504990 | -77.80 | 15.46 | 513.50 | 0.12 | 2.05 | 1598 |

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
| 3222375 | 4 | 121.4696929563 | 31.1461739276 | 347 | 11 | 2 | 33.7 | TDD | 647 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3255836 | 1 | 121.4668454720 | 31.1531723894 | 132 | 13 | 11 | 25.1 | TDD | 680 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3258184 | 2 | 121.4721113631 | 31.1524164667 | 141 | 14 | 11 | 19.6 | TDD | 635 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3265356 | 3 | 121.4732851882 | 31.1529479142 | 317 | 10 | 12 | 39.6 | TDD | 734 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.175 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.199 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.310 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.310 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.999 | NREventA3 | measId:2;ServCellPCI:182;Se... |
| 2024-09-20 22:21:38.239 | NRHandoverAttempt | SourcePCI:182;SourceNR-ARFC... |
| 2024-09-20 22:21:38.285 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.296 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.436 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.436 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255836 | 1 | 12.8406 | 13.8771 | -115.2461 | 18.4153 | 86.5040 | 0.0132 | 0.1739 |
| 2024_09_20 22:00 | 3258184 | 2 | 13.5941 | 13.8895 | -115.9489 | 5.3920 | 86.2835 | 0.0027 | 0.0055 |
| 2024_09_20 22:00 | 3265356 | 3 | 10.1052 | 8.5829 | -116.7570 | 6.4147 | 85.1974 | 0.0173 | 0.0011 |
| 2024_09_20 22:00 | 3222375 | 4 | 12.2880 | 17.4930 | -114.3523 | 12.6909 | 125.8231 | 0.0014 | 0.0103 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414749_F6E950A1 | 504990 | 680 | -92.8 | 504990 | 734 | -87.0 | 504990 | 647 | -90.6 | 504990 | 635 |
| MR_1774414749_089AB47B | 504990 | 680 | -91.2 | 504990 | 734 | -87.3 | 504990 | 647 | -90.8 | 504990 | 635 |
| MR_1774414749_989F931F | 504990 | 680 | -90.0 | 504990 | 734 | -85.3 | 504990 | 647 | -91.2 | 504990 | 635 |
| MR_1774414749_91932F79 | 504990 | 734 | -86.0 | 504990 | 680 | -89.7 | 504990 | 647 | -91.2 | 504990 | 635 |
| MR_1774414749_02F696EA | 504990 | 680 | -92.0 | 504990 | 734 | -86.5 | 504990 | 647 | -89.6 | 504990 | 635 |
| MR_1774414749_A6710A5B | 504990 | 680 | -92.7 | 504990 | 734 | -86.0 | 504990 | 647 | -89.9 | 504990 | 635 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 147: `da3d9337-0d6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `da3d9337-0d6b-436d-853b-f2a5abffaf06` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[147] topology](images/train_0147.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment. **← 정답**
- `C2`: Increase A3 Offset threshold for 3210355_3
- `C3`: Lift the tilt angle  of 3247135_4 by 10 degrees
- `C4`: Adjust the azimuth of 3247135_4 by 50 degrees
- `C5`: Adjust the azimuth of 3210355_3 by 50 degrees
- `C6`: Increase transmission power for 3247135_4
- `C7`: Add neighbor relationship between 3210355_3 and 3247135_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210355_3
- `C9`: Press down the tilt angle  of 3247135_4 by 10 degrees
- `C10`: Add neighbor relationship between 3254816_1 and 3247135_4
- `C11`: Decrease A3 Offset threshold for 3210355_3
- `C12`: Check test server and transmission issues
- `C13`: Lift the tilt angle of 3210355_3 by 5 degrees
- `C14`: Increase A3 Offset threshold for 3247135_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210355_3
- `C16`: Press down the tilt angle of 3210355_3 by 5 degrees
- `C17`: Decrease transmission power for 3210355_3
- `C18`: Decrease A3 Offset threshold for 3247135_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247135_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247135_4
- `C21`: Decrease transmission power for 3247135_4
- `C22`: Increase transmission power for 3210355_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.229 | MS1 | 121.4656682174 | 31.1446295816 | 604 | 504990 | -87.95 | 12.04 | 455.33 | 0.14 | 2.80 | 1585 |
| 2024-09-20 22:21:32.640 | MS1 | 121.4656591568 | 31.1446329864 | 604 | 504990 | -89.87 | 12.34 | 398.35 | 0.16 | 2.07 | 1579 |
| 2024-09-20 22:21:33.120 | MS1 | 121.4656767205 | 31.1446344135 | 604 | 504990 | -89.68 | 14.52 | 468.86 | 0.16 | 2.64 | 1563 |
| 2024-09-20 22:21:34.741 | MS1 | 121.4656689236 | 31.1446298484 | 604 | 504990 | -87.21 | 15.47 | 72.69 | 0.02 | 2.16 | 1598 |
| 2024-09-20 22:21:35.314 | MS1 | 121.4656627809 | 31.1446309769 | 604 | 504990 | -85.42 | 13.19 | 84.67 | 0.15 | 2.98 | 1589 |
| 2024-09-20 22:21:36.978 | MS1 | 121.4656608785 | 31.1446342138 | 604 | 504990 | -86.05 | 14.42 | 57.91 | 0.13 | 2.30 | 1581 |
| 2024-09-20 22:21:37.726 | MS1 | 121.4656599444 | 31.1446252362 | 604 | 504990 | -91.40 | 9.97 | 61.26 | 0.07 | 2.82 | 1583 |
| 2024-09-20 22:21:38.760 | MS1 | 121.4656724805 | 31.1446278703 | 604 | 504990 | -90.07 | 12.56 | 103.36 | 0.13 | 2.39 | 1585 |
| 2024-09-20 22:21:39.121 | MS1 | 121.4656615098 | 31.1446376516 | 604 | 504990 | -91.95 | 9.60 | 84.71 | 0.20 | 2.14 | 1572 |
| 2024-09-20 22:21:40.336 | MS1 | 121.4656750892 | 31.1446241764 | 604 | 504990 | -91.83 | 9.03 | 430.03 | 0.11 | 2.43 | 1562 |
| 2024-09-20 22:21:41.946 | MS1 | 121.4656740017 | 31.1446316025 | 604 | 504990 | -89.40 | 8.49 | 367.55 | 0.07 | 2.29 | 1597 |
| 2024-09-20 22:21:42.305 | MS1 | 121.4656598151 | 31.1446356244 | 604 | 504990 | -91.49 | 8.24 | 316.72 | 0.08 | 2.42 | 1574 |

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
| 3210355 | 3 | 121.4738890985 | 31.1497080527 | 321 | 2 | 11 | 49.5 | TDD | 604 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3247135 | 4 | 121.4691380684 | 31.1449047934 | 122 | 6 | 8 | 34.7 | TDD | 22 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3254816 | 1 | 121.4738108841 | 31.1516651311 | 39 | 2 | 0 | 20.4 | TDD | 577 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3255327 | 2 | 121.4726158312 | 31.1490967381 | 142 | 6 | 1 | 18.0 | TDD | 27 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.460 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.484 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.610 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.610 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.352 | NREventA3 | measId:2;ServCellPCI:7;Serv... |
| 2024-09-20 22:21:38.592 | NRHandoverAttempt | SourcePCI:7;SourceNR-ARFCN:... |
| 2024-09-20 22:21:38.626 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.641 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.790 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.790 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3254816 | 1 | 86.7532 | 79.7830 | -114.8277 | 16.7500 | 135.0246 | 0.0029 | 0.0153 |
| 2024_09_19 22:00 | 3255327 | 2 | 76.6570 | 89.5263 | -117.0100 | 7.5231 | 82.1614 | 0.0070 | 0.0096 |
| 2024_09_19 22:00 | 3210355 | 3 | 82.6186 | 93.8007 | -116.3898 | 13.1397 | 136.5489 | 0.0068 | 0.0084 |
| 2024_09_19 22:00 | 3247135 | 4 | 84.2180 | 81.0353 | -114.5509 | 5.0579 | 169.1509 | 0.0146 | 0.0116 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414434_B8BC9268 | 504990 | 604 | -87.3 | 504990 | 22 | -91.4 | 504990 | 577 | -98.4 | 504990 | 27 |
| MR_1774414434_8D947831 | 504990 | 604 | -85.4 | 504990 | 22 | -93.8 | 504990 | 577 | -98.8 | 504990 | 27 |
| MR_1774414434_16936CEE | 504990 | 604 | -86.7 | 504990 | 22 | -90.5 | 504990 | 577 | -97.4 | 504990 | 27 |
| MR_1774414434_A971F1BB | 504990 | 604 | -87.6 | 504990 | 22 | -93.3 | 504990 | 577 | -99.7 | 504990 | 27 |
| MR_1774414434_A3753FCB | 504990 | 604 | -88.4 | 504990 | 22 | -93.0 | 504990 | 577 | -98.6 | 504990 | 27 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 148: `3da2462e-a0e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3da2462e-a0e1-415f-814a-130b8bb10a6b` |
| Tag | **multiple-answer** |
| 정답 | **C9|C13|C14|C16** |
| C9 의미 | Press down the tilt angle  of 3273708_5 by 6 degrees |
| C13 의미 | Increase A3 Offset threshold for 3214335_2 |
| C14 의미 | Increase A3 Offset threshold for 3273708_5 |
| C16 의미 | Decrease transmission power for 3273708_5 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[148] topology](images/train_0148.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3214335_2
- `C2`: Decrease transmission power for 3214335_2
- `C3`: Add neighbor relationship between 3224663_1 and 3273708_5
- `C4`: Decrease A3 Offset threshold for 3273708_5
- `C5`: Adjust the azimuth of 3273708_5 by 29 degrees
- `C6`: Increase transmission power for 3273708_5
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214335_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214335_2
- `C9`: Press down the tilt angle  of 3273708_5 by 6 degrees **← 정답**
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273708_5
- `C11`: Press down the tilt angle of 3214335_2 by 5 degrees
- `C12`: Increase transmission power for 3214335_2
- `C13`: Increase A3 Offset threshold for 3214335_2 **← 정답**
- `C14`: Increase A3 Offset threshold for 3273708_5 **← 정답**
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease transmission power for 3273708_5 **← 정답**
- `C17`: Adjust the azimuth of 3214335_2 by 25 degrees
- `C18`: Add neighbor relationship between 3214335_2 and 3273708_5
- `C19`: Lift the tilt angle  of 3273708_5 by 6 degrees
- `C20`: Check test server and transmission issues
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273708_5
- `C22`: Lift the tilt angle of 3214335_2 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.156 | MS1 | 121.4656624446 | 31.1446273245 | 867 | 504990 | -81.65 | 17.09 | 314.92 | 0.06 | 2.93 | 1584 |
| 2024-09-20 22:21:32.320 | MS1 | 121.4656657569 | 31.1446378563 | 867 | 504990 | -75.23 | 16.66 | 451.30 | 0.05 | 2.76 | 1570 |
| 2024-09-20 22:21:33.825 | MS1 | 121.4656600068 | 31.1446304658 | 867 | 504990 | -77.99 | 16.20 | 575.99 | 0.14 | 2.92 | 1596 |
| 2024-09-20 22:21:34.300 | MS1 | 121.4656760554 | 31.1446224236 | 942 | 504990 | -88.22 | 3.27 | 57.62 | 0.19 | 1.25 | 1583 |
| 2024-09-20 22:21:35.665 | MS1 | 121.4656647018 | 31.1446338995 | 942 | 504990 | -89.16 | 2.49 | 79.12 | 0.16 | 1.16 | 1574 |
| 2024-09-20 22:21:36.454 | MS1 | 121.4656596167 | 31.1446314332 | 867 | 504990 | -82.12 | 3.56 | 49.09 | 0.12 | 1.10 | 1566 |
| 2024-09-20 22:21:37.431 | MS1 | 121.4656617476 | 31.1446354293 | 867 | 504990 | -81.71 | 2.18 | 68.05 | 0.13 | 1.35 | 1561 |
| 2024-09-20 22:21:38.876 | MS1 | 121.4656696760 | 31.1446331298 | 942 | 504990 | -88.70 | 4.12 | 46.89 | 0.14 | 1.00 | 1568 |
| 2024-09-20 22:21:39.499 | MS1 | 121.4656735313 | 31.1446195287 | 942 | 504990 | -82.71 | 1.26 | 80.39 | 0.01 | 1.35 | 1579 |
| 2024-09-20 22:21:40.455 | MS1 | 121.4656734853 | 31.1446358869 | 942 | 504990 | -82.95 | 15.26 | 498.32 | 0.13 | 2.23 | 1568 |
| 2024-09-20 22:21:41.594 | MS1 | 121.4656708145 | 31.1446187107 | 942 | 504990 | -77.59 | 15.66 | 573.54 | 0.07 | 2.68 | 1577 |
| 2024-09-20 22:21:42.950 | MS1 | 121.4656701629 | 31.1446186309 | 942 | 504990 | -83.03 | 16.78 | 380.16 | 0.16 | 2.11 | 1567 |

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
| 3214335 | 2 | 121.4747074269 | 31.1545105202 | 193 | 3 | 0 | 37.1 | TDD | 867 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3215138 | 3 | 121.4675421032 | 31.1460305898 | 353 | 7 | 4 | 48.6 | TDD | 942 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3224663 | 1 | 121.4726816835 | 31.1493929628 | 60 | 8 | 5 | 34.8 | TDD | 609 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3250721 | 4 | 121.4655844886 | 31.1474900097 | 178 | 4 | 11 | 36.6 | TDD | 723 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3273708 | 5 | 121.4723655808 | 31.1555639072 | 179 | 5 | 12 | 17.8 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.476 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.495 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.629 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.629 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.364 | NREventA3 | measId:2;ServCellPCI:154;Se... |
| 2024-09-20 22:21:34.604 | NRHandoverAttempt | SourcePCI:154;SourceNR-ARFC... |
| 2024-09-20 22:21:34.647 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.659 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:34.792 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.792 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.364 | NREventA3 | measId:2;ServCellPCI:277;Se... |
| 2024-09-20 22:21:36.604 | NRHandoverAttempt | SourcePCI:277;SourceNR-ARFC... |
| 2024-09-20 22:21:36.652 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.667 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.814 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.814 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.364 | NREventA3 | measId:2;ServCellPCI:154;Se... |
| 2024-09-20 22:21:38.604 | NRHandoverAttempt | SourcePCI:154;SourceNR-ARFC... |
| 2024-09-20 22:21:38.647 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.660 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.807 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.807 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224663 | 1 | 6.3679 | 16.6656 | -115.7416 | 7.2015 | 115.4836 | 0.0001 | 0.0062 |
| 2024_09_20 22:00 | 3214335 | 2 | 13.2268 | 10.7359 | -116.6364 | 9.8028 | 196.7047 | 0.0108 | 0.0070 |
| 2024_09_20 22:00 | 3215138 | 3 | 15.6383 | 18.7721 | -117.4619 | 12.2204 | 122.4977 | 0.0011 | 0.0079 |
| 2024_09_20 22:00 | 3250721 | 4 | 5.1016 | 18.9550 | -116.3079 | 10.7565 | 171.7019 | 0.0017 | 0.0040 |
| 2024_09_20 22:00 | 3273708 | 5 | 6.2799 | 15.1982 | -114.3956 | 12.3137 | 96.8004 | 0.0115 | 0.0032 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415952_53454D17 | 504990 | 942 | -88.6 | 504990 | 867 | -83.2 | 504990 | 441 | -85.5 | 504990 | 609 |
| MR_1774415952_0FA62793 | 504990 | 942 | -88.1 | 504990 | 867 | -85.5 | 504990 | 441 | -85.1 | 504990 | 609 |
| MR_1774415952_8403419A | 504990 | 942 | -87.8 | 504990 | 867 | -83.6 | 504990 | 441 | -87.6 | 504990 | 609 |
| MR_1774415952_FEFA10E0 | 504990 | 942 | -89.8 | 504990 | 867 | -83.7 | 504990 | 441 | -86.2 | 504990 | 609 |
| MR_1774415952_88AD23FD | 504990 | 867 | -88.3 | 504990 | 942 | -86.3 | 504990 | 441 | -86.8 | 504990 | 609 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 149: `b2847ab1-3cc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b2847ab1-3cc1-4ae1-b6cc-6307447a5d6a` |
| Tag | **multiple-answer** |
| 정답 | **C15|C21** |
| C15 의미 | Decrease transmission power for 3267028_1 |
| C21 의미 | Press down the tilt angle  of 3267028_1 by 5 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[149] topology](images/train_0149.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3245357_2 by 3 degrees
- `C2`: Add neighbor relationship between 3259852_4 and 3267028_1
- `C3`: Increase A3 Offset threshold for 3245357_2
- `C4`: Add neighbor relationship between 3245357_2 and 3267028_1
- `C5`: Decrease A3 Offset threshold for 3245357_2
- `C6`: Increase A3 Offset threshold for 3267028_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245357_2
- `C8`: Increase transmission power for 3245357_2
- `C9`: Lift the tilt angle  of 3267028_1 by 5 degrees
- `C10`: Check test server and transmission issues
- `C11`: Press down the tilt angle of 3245357_2 by 3 degrees
- `C12`: Increase transmission power for 3267028_1
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245357_2
- `C15`: Decrease transmission power for 3267028_1 **← 정답**
- `C16`: Decrease A3 Offset threshold for 3267028_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267028_1
- `C18`: Decrease transmission power for 3245357_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267028_1
- `C20`: Adjust the azimuth of 3245357_2 by 15 degrees
- `C21`: Press down the tilt angle  of 3267028_1 by 5 degrees **← 정답**
- `C22`: Adjust the azimuth of 3267028_1 by 22 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.874 | MS1 | 121.4656695739 | 31.1446293283 | 668 | 504990 | -79.77 | 16.16 | 516.18 | 0.00 | 2.90 | 1571 |
| 2024-09-20 22:21:32.239 | MS1 | 121.4656626493 | 31.1446353944 | 668 | 504990 | -82.89 | 14.02 | 458.52 | 0.16 | 2.16 | 1562 |
| 2024-09-20 22:21:33.428 | MS1 | 121.4656718804 | 31.1446328595 | 668 | 504990 | -80.72 | 13.35 | 491.94 | 0.07 | 2.53 | 1581 |
| 2024-09-20 22:21:34.124 | MS1 | 121.4656745184 | 31.1446239584 | 668 | 504990 | -90.15 | 3.32 | 74.64 | 0.11 | 1.25 | 1585 |
| 2024-09-20 22:21:35.398 | MS1 | 121.4656650835 | 31.1446327851 | 668 | 504990 | -85.46 | 2.23 | 55.04 | 0.09 | 1.32 | 1598 |
| 2024-09-20 22:21:36.858 | MS1 | 121.4656621583 | 31.1446256368 | 668 | 504990 | -85.43 | 3.93 | 66.51 | 0.10 | 1.11 | 1599 |
| 2024-09-20 22:21:37.166 | MS1 | 121.4656720815 | 31.1446217706 | 668 | 504990 | -94.24 | 0.31 | 78.26 | 0.01 | 1.09 | 1574 |
| 2024-09-20 22:21:38.957 | MS1 | 121.4656760533 | 31.1446328213 | 668 | 504990 | -90.91 | 2.26 | 85.10 | 0.12 | 1.15 | 1581 |
| 2024-09-20 22:21:39.847 | MS1 | 121.4656613292 | 31.1446222415 | 668 | 504990 | -85.21 | 0.83 | 53.68 | 0.06 | 1.19 | 1573 |
| 2024-09-20 22:21:40.588 | MS1 | 121.4656590314 | 31.1446220872 | 668 | 504990 | -77.76 | 12.84 | 431.49 | 0.01 | 2.98 | 1583 |
| 2024-09-20 22:21:41.913 | MS1 | 121.4656738320 | 31.1446371800 | 668 | 504990 | -78.08 | 14.12 | 436.23 | 0.16 | 2.76 | 1581 |
| 2024-09-20 22:21:42.487 | MS1 | 121.4656638381 | 31.1446200552 | 668 | 504990 | -83.71 | 17.82 | 459.86 | 0.17 | 2.84 | 1575 |

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
| 3245357 | 2 | 121.4721670351 | 31.1478981039 | 255 | 1 | 2 | 25.4 | TDD | 668 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3259852 | 4 | 121.4759394718 | 31.1526870860 | 295 | 7 | 3 | 43.8 | TDD | 300 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3267028 | 1 | 121.4744168093 | 31.1521681756 | 247 | 3 | 1 | 45.2 | TDD | 231 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3279758 | 3 | 121.4742493139 | 31.1552292880 | 302 | 11 | 2 | 33.5 | TDD | 918 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.557 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.577 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.697 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.697 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267028 | 1 | 16.5136 | 13.2847 | -115.9301 | 16.3386 | 180.0152 | 0.0014 | 0.0096 |
| 2024_09_20 22:00 | 3245357 | 2 | 19.8827 | 8.7495 | -109.3405 | 12.0080 | 147.1992 | 0.0093 | 0.0023 |
| 2024_09_20 22:00 | 3279758 | 3 | 18.4650 | 15.8397 | -116.5733 | 13.4873 | 185.6083 | 0.0177 | 0.0196 |
| 2024_09_20 22:00 | 3259852 | 4 | 14.2922 | 9.2625 | -116.9119 | 15.3814 | 177.3207 | 0.0119 | 0.0163 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412680_25100230 | 504990 | 231 | -90.4 | 504990 | 668 | -86.0 | 504990 | 300 | -86.4 | 504990 | 918 |
| MR_1774412680_C32AC0DE | 504990 | 668 | -88.6 | 504990 | 231 | -85.0 | 504990 | 300 | -86.1 | 504990 | 918 |
| MR_1774412680_FFC369CE | 504990 | 668 | -88.7 | 504990 | 231 | -88.0 | 504990 | 300 | -88.3 | 504990 | 918 |
| MR_1774412680_1A113DB0 | 504990 | 668 | -91.0 | 504990 | 231 | -86.0 | 504990 | 300 | -87.0 | 504990 | 918 |
| MR_1774412680_D812D6A6 | 504990 | 668 | -90.6 | 504990 | 231 | -86.8 | 504990 | 300 | -85.1 | 504990 | 918 |
| MR_1774412680_F25A748C | 504990 | 668 | -89.3 | 504990 | 231 | -87.4 | 504990 | 300 | -87.0 | 504990 | 918 |

> *... 2개 열 생략 (전체 14열)*

---
