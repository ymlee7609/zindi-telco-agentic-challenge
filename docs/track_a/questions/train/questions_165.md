# Track A 문제 분석 — train[1640]~train[1649]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1640] ~ train[1649] (10개)

## 목차

1. [문제 1640: `61998ff8-a05...`](#1640) — multiple-answer, 정답: C4|C10
2. [문제 1641: `eb4dafac-40f...`](#1641) — single-answer, 정답: C7
3. [문제 1642: `c863c6f6-541...`](#1642) — single-answer, 정답: C16
4. [문제 1643: `f9272266-bc6...`](#1643) — single-answer, 정답: C3
5. [문제 1644: `3db4928a-7d3...`](#1644) — single-answer, 정답: C10
6. [문제 1645: `b27461cd-cce...`](#1645) — single-answer, 정답: C16
7. [문제 1646: `ec4053bc-19d...`](#1646) — single-answer, 정답: C11
8. [문제 1647: `772a6e3d-cef...`](#1647) — multiple-answer, 정답: C4|C18
9. [문제 1648: `ae8cc132-59a...`](#1648) — single-answer, 정답: C10
10. [문제 1649: `f86de2b9-9ab...`](#1649) — single-answer, 정답: C2

---

### 문제 1640: `61998ff8-a05...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `61998ff8-a054-4135-8054-5088e3c4f58a` |
| Tag | **multiple-answer** |
| 정답 | **C4|C10** |
| C4 의미 | Decrease transmission power for 3233286_4 |
| C10 의미 | Press down the tilt angle  of 3233286_4 by 5 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1640] topology](images/train_1640.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272830_1
- `C2`: Add neighbor relationship between 3272830_1 and 3233286_4
- `C3`: Lift the tilt angle of 3272830_1 by 1 degrees
- `C4`: Decrease transmission power for 3233286_4 **← 정답**
- `C5`: Adjust the azimuth of 3233286_4 by 13 degrees
- `C6`: Press down the tilt angle of 3272830_1 by 1 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Increase transmission power for 3272830_1
- `C9`: Check test server and transmission issues
- `C10`: Press down the tilt angle  of 3233286_4 by 5 degrees **← 정답**
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272830_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233286_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233286_4
- `C14`: Adjust the azimuth of 3272830_1 by 16 degrees
- `C15`: Increase A3 Offset threshold for 3272830_1
- `C16`: Lift the tilt angle  of 3233286_4 by 5 degrees
- `C17`: Decrease A3 Offset threshold for 3272830_1
- `C18`: Increase transmission power for 3233286_4
- `C19`: Add neighbor relationship between 3242568_2 and 3233286_4
- `C20`: Decrease A3 Offset threshold for 3233286_4
- `C21`: Increase A3 Offset threshold for 3233286_4
- `C22`: Decrease transmission power for 3272830_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.244 | MS1 | 121.4656648041 | 31.1446264194 | 218 | 504990 | -75.12 | 14.19 | 309.14 | 0.17 | 2.21 | 1579 |
| 2024-09-20 22:21:32.577 | MS1 | 121.4656705227 | 31.1446239645 | 218 | 504990 | -77.94 | 12.88 | 491.10 | 0.11 | 2.78 | 1568 |
| 2024-09-20 22:21:33.855 | MS1 | 121.4656583634 | 31.1446333532 | 218 | 504990 | -75.42 | 15.90 | 478.41 | 0.15 | 2.60 | 1582 |
| 2024-09-20 22:21:34.435 | MS1 | 121.4656727888 | 31.1446232674 | 218 | 504990 | -93.97 | 0.47 | 88.86 | 0.13 | 1.10 | 1600 |
| 2024-09-20 22:21:35.528 | MS1 | 121.4656646266 | 31.1446327136 | 218 | 504990 | -86.05 | 1.47 | 40.36 | 0.07 | 1.49 | 1564 |
| 2024-09-20 22:21:36.464 | MS1 | 121.4656617078 | 31.1446273043 | 218 | 504990 | -91.62 | 0.65 | 87.79 | 0.11 | 1.41 | 1595 |
| 2024-09-20 22:21:37.198 | MS1 | 121.4656725326 | 31.1446336755 | 218 | 504990 | -94.57 | 2.10 | 39.49 | 0.09 | 1.13 | 1574 |
| 2024-09-20 22:21:38.182 | MS1 | 121.4656658423 | 31.1446200460 | 218 | 504990 | -88.00 | 0.30 | 35.80 | 0.12 | 1.04 | 1572 |
| 2024-09-20 22:21:39.415 | MS1 | 121.4656682349 | 31.1446377760 | 218 | 504990 | -92.17 | 0.38 | 78.50 | 0.11 | 1.14 | 1589 |
| 2024-09-20 22:21:40.468 | MS1 | 121.4656629806 | 31.1446324146 | 218 | 504990 | -76.96 | 14.99 | 479.14 | 0.04 | 2.55 | 1567 |
| 2024-09-20 22:21:41.734 | MS1 | 121.4656704503 | 31.1446325950 | 218 | 504990 | -79.49 | 15.37 | 556.49 | 0.03 | 2.50 | 1570 |
| 2024-09-20 22:21:42.608 | MS1 | 121.4656685998 | 31.1446211836 | 218 | 504990 | -84.75 | 14.93 | 332.84 | 0.20 | 2.73 | 1599 |

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
| 3233286 | 4 | 121.4659118183 | 31.1541912150 | 194 | 4 | 6 | 27.4 | TDD | 106 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3242568 | 2 | 121.4686383902 | 31.1475799726 | 111 | 7 | 11 | 22.8 | TDD | 194 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3255783 | 3 | 121.4752798237 | 31.1463555142 | 193 | 3 | 4 | 26.7 | TDD | 884 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3272830 | 1 | 121.4717833801 | 31.1503145181 | 239 | 0 | 0 | 19.0 | TDD | 218 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.595 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.611 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.760 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.760 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272830 | 1 | 6.1541 | 18.1951 | -109.3827 | 12.2384 | 190.3640 | 0.0128 | 0.0070 |
| 2024_09_20 22:00 | 3242568 | 2 | 13.4382 | 5.7978 | -115.3345 | 16.1898 | 167.6518 | 0.0038 | 0.0115 |
| 2024_09_20 22:00 | 3255783 | 3 | 6.8514 | 17.0873 | -114.3351 | 9.5968 | 181.1664 | 0.0139 | 0.0071 |
| 2024_09_20 22:00 | 3233286 | 4 | 5.4045 | 7.3416 | -114.2872 | 13.1469 | 110.4779 | 0.0159 | 0.0190 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417121_DE6A8088 | 504990 | 218 | -94.7 | 504990 | 106 | -94.6 | 504990 | 194 | -94.3 | 504990 | 884 |
| MR_1774417121_DC77FC38 | 504990 | 218 | -95.5 | 504990 | 106 | -92.8 | 504990 | 194 | -95.9 | 504990 | 884 |
| MR_1774417121_3574759A | 504990 | 218 | -95.3 | 504990 | 106 | -92.3 | 504990 | 194 | -94.2 | 504990 | 884 |
| MR_1774417121_C8C06744 | 504990 | 218 | -92.6 | 504990 | 106 | -92.6 | 504990 | 194 | -96.5 | 504990 | 884 |
| MR_1774417121_217AB1A8 | 504990 | 106 | -95.3 | 504990 | 218 | -95.3 | 504990 | 194 | -97.1 | 504990 | 884 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1641: `eb4dafac-40f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `eb4dafac-40f7-4ce3-9b52-c0026315571c` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3254468_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1641] topology](images/train_1641.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3238440_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238440_2
- `C3`: Check test server and transmission issues
- `C4`: Increase transmission power for 3254468_4
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Adjust the azimuth of 3238440_2 by 50 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254468_4 **← 정답**
- `C8`: Increase transmission power for 3238440_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238440_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254468_4
- `C11`: Decrease A3 Offset threshold for 3254468_4
- `C12`: Increase A3 Offset threshold for 3254468_4
- `C13`: Press down the tilt angle  of 3238440_2 by 9 degrees
- `C14`: Press down the tilt angle of 3254468_4 by 4 degrees
- `C15`: Increase A3 Offset threshold for 3238440_2
- `C16`: Lift the tilt angle  of 3238440_2 by 9 degrees
- `C17`: Adjust the azimuth of 3254468_4 by 38 degrees
- `C18`: Decrease transmission power for 3254468_4
- `C19`: Decrease transmission power for 3238440_2
- `C20`: Add neighbor relationship between 3225524_3 and 3238440_2
- `C21`: Add neighbor relationship between 3254468_4 and 3238440_2
- `C22`: Lift the tilt angle of 3254468_4 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.931 | MS1 | 121.4656652510 | 31.1446246087 | 183 | 504990 | -85.55 | 14.39 | 473.85 | 0.09 | 2.26 | 1591 |
| 2024-09-20 22:21:32.603 | MS1 | 121.4656635320 | 31.1446284430 | 183 | 504990 | -90.33 | 17.70 | 487.29 | 0.03 | 2.24 | 1600 |
| 2024-09-20 22:21:33.967 | MS1 | 121.4656623532 | 31.1446303937 | 183 | 504990 | -88.23 | 17.51 | 563.69 | 0.18 | 2.93 | 1569 |
| 2024-09-20 22:21:34.936 | MS1 | 121.4656714199 | 31.1446200602 | 183 | 504990 | -87.70 | 13.86 | 52.23 | 0.58 | 2.05 | 606 |
| 2024-09-20 22:21:35.747 | MS1 | 121.4656593671 | 31.1446217496 | 183 | 504990 | -90.87 | 16.46 | 80.44 | 0.70 | 2.55 | 598 |
| 2024-09-20 22:21:36.111 | MS1 | 121.4656678073 | 31.1446372842 | 183 | 504990 | -87.27 | 17.76 | 67.79 | 0.51 | 2.71 | 575 |
| 2024-09-20 22:21:37.271 | MS1 | 121.4656731688 | 31.1446206290 | 183 | 504990 | -89.29 | 7.58 | 70.23 | 0.58 | 2.16 | 668 |
| 2024-09-20 22:21:38.775 | MS1 | 121.4656763683 | 31.1446293760 | 183 | 504990 | -93.18 | 10.24 | 73.37 | 0.61 | 2.84 | 584 |
| 2024-09-20 22:21:39.859 | MS1 | 121.4656714378 | 31.1446233991 | 183 | 504990 | -92.49 | 9.99 | 67.62 | 0.65 | 2.01 | 515 |
| 2024-09-20 22:21:40.496 | MS1 | 121.4656690626 | 31.1446321624 | 183 | 504990 | -91.66 | 10.80 | 307.02 | 0.17 | 2.23 | 1583 |
| 2024-09-20 22:21:41.949 | MS1 | 121.4656609276 | 31.1446218463 | 183 | 504990 | -92.04 | 11.62 | 312.31 | 0.09 | 2.52 | 1577 |
| 2024-09-20 22:21:42.897 | MS1 | 121.4656767321 | 31.1446358714 | 183 | 504990 | -92.92 | 12.94 | 467.03 | 0.11 | 2.64 | 1580 |

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
| 3225524 | 3 | 121.4687761053 | 31.1469156078 | 269 | 10 | 2 | 30.4 | TDD | 515 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3238440 | 2 | 121.4752127910 | 31.1478474132 | 304 | 7 | 5 | 37.1 | TDD | 523 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3254468 | 4 | 121.4695429880 | 31.1527694210 | 164 | 2 | 5 | 32.1 | TDD | 183 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3269956 | 1 | 121.4640416798 | 31.1446040848 | 63 | 12 | 12 | 47.2 | TDD | 512 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.392 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.522 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.522 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.218 | NREventA3 | measId:2;ServCellPCI:637;Se... |
| 2024-09-20 22:21:38.458 | NRHandoverAttempt | SourcePCI:637;SourceNR-ARFC... |
| 2024-09-20 22:21:38.505 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.520 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.638 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.638 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269956 | 1 | 13.1440 | 5.4953 | -116.1366 | 16.2326 | 127.4139 | 0.0050 | 0.0117 |
| 2024_09_20 22:00 | 3238440 | 2 | 11.2942 | 10.0952 | -114.1865 | 8.8383 | 87.5438 | 0.0147 | 0.0009 |
| 2024_09_20 22:00 | 3225524 | 3 | 15.5972 | 12.1949 | -116.7361 | 12.7416 | 89.4334 | 0.0082 | 0.0183 |
| 2024_09_20 22:00 | 3254468 | 4 | 18.5579 | 7.9855 | -114.5559 | 16.6642 | 96.1270 | 0.0198 | 0.0074 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414228_28426DB0 | 504990 | 183 | -88.9 | 504990 | 523 | -96.4 | 504990 | 515 | -95.1 | 504990 | 512 |
| MR_1774414228_FAA1AC53 | 504990 | 183 | -86.8 | 504990 | 523 | -96.9 | 504990 | 515 | -94.7 | 504990 | 512 |
| MR_1774414228_218F0884 | 504990 | 183 | -88.9 | 504990 | 523 | -96.9 | 504990 | 515 | -96.6 | 504990 | 512 |
| MR_1774414228_E5DCB3C1 | 504990 | 183 | -86.8 | 504990 | 523 | -97.3 | 504990 | 515 | -96.4 | 504990 | 512 |
| MR_1774414228_F1D40DDB | 504990 | 183 | -88.5 | 504990 | 523 | -94.1 | 504990 | 515 | -95.5 | 504990 | 512 |
| MR_1774414228_377C9864 | 504990 | 183 | -89.3 | 504990 | 523 | -97.0 | 504990 | 515 | -98.5 | 504990 | 512 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1642: `c863c6f6-541...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c863c6f6-5418-452e-b28a-8114332f62df` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1642] topology](images/train_1642.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3257035_1 by 50 degrees
- `C2`: Lift the tilt angle of 3257035_1 by 9 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257035_1
- `C4`: Press down the tilt angle of 3257035_1 by 9 degrees
- `C5`: Increase A3 Offset threshold for 3279618_2
- `C6`: Increase transmission power for 3257035_1
- `C7`: Decrease A3 Offset threshold for 3257035_1
- `C8`: Increase A3 Offset threshold for 3257035_1
- `C9`: Lift the tilt angle  of 3279618_2 by 10 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279618_2
- `C11`: Adjust the azimuth of 3279618_2 by 50 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257035_1
- `C13`: Decrease A3 Offset threshold for 3279618_2
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Add neighbor relationship between 3257035_1 and 3279618_2
- `C16`: Check test server and transmission issues **← 정답**
- `C17`: Decrease transmission power for 3257035_1
- `C18`: Decrease transmission power for 3279618_2
- `C19`: Increase transmission power for 3279618_2
- `C20`: Add neighbor relationship between 3238231_3 and 3279618_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279618_2
- `C22`: Press down the tilt angle  of 3279618_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.894 | MS1 | 121.4656664964 | 31.1446224098 | 109 | 504990 | -91.99 | 12.71 | 470.98 | 0.11 | 2.72 | 1599 |
| 2024-09-20 22:21:32.289 | MS1 | 121.4656587775 | 31.1446201172 | 109 | 504990 | -90.78 | 13.62 | 377.77 | 0.02 | 2.78 | 1576 |
| 2024-09-20 22:21:33.422 | MS1 | 121.4656771818 | 31.1446213477 | 109 | 504990 | -87.65 | 15.23 | 361.50 | 0.16 | 2.78 | 1595 |
| 2024-09-20 22:21:34.796 | MS1 | 121.4656681600 | 31.1446238219 | 109 | 504990 | -85.90 | 17.27 | 58.44 | 0.13 | 2.80 | 460 |
| 2024-09-20 22:21:35.111 | MS1 | 121.4656718944 | 31.1446214250 | 109 | 504990 | -91.36 | 12.49 | 64.39 | 0.15 | 2.59 | 401 |
| 2024-09-20 22:21:36.488 | MS1 | 121.4656673502 | 31.1446184103 | 109 | 504990 | -89.96 | 13.79 | 67.27 | 0.18 | 2.02 | 463 |
| 2024-09-20 22:21:37.592 | MS1 | 121.4656614367 | 31.1446375137 | 109 | 504990 | -89.39 | 8.27 | 95.51 | 0.05 | 2.91 | 475 |
| 2024-09-20 22:21:38.976 | MS1 | 121.4656659781 | 31.1446376494 | 109 | 504990 | -89.16 | 12.01 | 63.89 | 0.04 | 2.31 | 345 |
| 2024-09-20 22:21:39.206 | MS1 | 121.4656729017 | 31.1446197672 | 109 | 504990 | -93.56 | 7.89 | 101.37 | 0.10 | 2.11 | 301 |
| 2024-09-20 22:21:40.294 | MS1 | 121.4656598402 | 31.1446326354 | 109 | 504990 | -89.54 | 7.81 | 504.51 | 0.01 | 2.86 | 1581 |
| 2024-09-20 22:21:41.727 | MS1 | 121.4656737691 | 31.1446352190 | 109 | 504990 | -89.73 | 7.60 | 427.76 | 0.09 | 2.62 | 1567 |
| 2024-09-20 22:21:42.950 | MS1 | 121.4656739618 | 31.1446183123 | 109 | 504990 | -93.34 | 10.36 | 419.81 | 0.02 | 2.95 | 1597 |

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
| 3213115 | 4 | 121.4755838446 | 31.1507340179 | 38 | 8 | 11 | 35.7 | TDD | 995 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3238231 | 3 | 121.4666559691 | 31.1559558876 | 2 | 2 | 5 | 34.5 | TDD | 285 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3257035 | 1 | 121.4657338560 | 31.1478883434 | 356 | 4 | 0 | 33.9 | TDD | 109 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3279618 | 2 | 121.4744081493 | 31.1553544223 | 113 | 14 | 12 | 31.9 | TDD | 611 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.996 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.015 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.117 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.117 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.878 | NREventA3 | measId:2;ServCellPCI:224;Se... |
| 2024-09-20 22:21:38.118 | NRHandoverAttempt | SourcePCI:224;SourceNR-ARFC... |
| 2024-09-20 22:21:38.159 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.170 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.276 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.276 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257035 | 1 | 7.7236 | 19.1555 | -117.4477 | 14.8780 | 109.1413 | 0.0134 | 0.0126 |
| 2024_09_20 22:00 | 3279618 | 2 | 13.2445 | 19.3735 | -116.9312 | 9.1540 | 121.3044 | 0.0055 | 0.0153 |
| 2024_09_20 22:00 | 3238231 | 3 | 7.8314 | 14.9985 | -116.6274 | 18.9384 | 90.6774 | 0.0125 | 0.0152 |
| 2024_09_20 22:00 | 3213115 | 4 | 18.9608 | 13.5000 | -117.3684 | 15.2510 | 156.1951 | 0.0067 | 0.0108 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415800_9B13C251 | 504990 | 109 | -87.2 | 504990 | 611 | -94.7 | 504990 | 285 | -96.2 | 504990 | 995 |
| MR_1774415800_E0BD9246 | 504990 | 109 | -85.9 | 504990 | 611 | -96.4 | 504990 | 285 | -95.7 | 504990 | 995 |
| MR_1774415800_CB22C72B | 504990 | 109 | -84.5 | 504990 | 611 | -94.7 | 504990 | 285 | -96.1 | 504990 | 995 |
| MR_1774415800_3064C901 | 504990 | 109 | -86.6 | 504990 | 611 | -96.3 | 504990 | 285 | -96.3 | 504990 | 995 |
| MR_1774415800_586269F1 | 504990 | 109 | -87.8 | 504990 | 611 | -95.0 | 504990 | 285 | -96.8 | 504990 | 995 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1643: `f9272266-bc6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f9272266-bc66-4490-9f26-12f1dee2a540` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1643] topology](images/train_1643.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268831_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268831_1
- `C3`: Check test server and transmission issues **← 정답**
- `C4`: Press down the tilt angle  of 3279296_3 by 10 degrees
- `C5`: Decrease A3 Offset threshold for 3279296_3
- `C6`: Decrease transmission power for 3279296_3
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease A3 Offset threshold for 3268831_1
- `C9`: Increase A3 Offset threshold for 3279296_3
- `C10`: Lift the tilt angle  of 3279296_3 by 10 degrees
- `C11`: Increase transmission power for 3268831_1
- `C12`: Press down the tilt angle of 3268831_1 by 7 degrees
- `C13`: Lift the tilt angle of 3268831_1 by 7 degrees
- `C14`: Increase transmission power for 3279296_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279296_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279296_3
- `C17`: Add neighbor relationship between 3268831_1 and 3279296_3
- `C18`: Decrease transmission power for 3268831_1
- `C19`: Increase A3 Offset threshold for 3268831_1
- `C20`: Adjust the azimuth of 3279296_3 by 50 degrees
- `C21`: Add neighbor relationship between 3273935_2 and 3279296_3
- `C22`: Adjust the azimuth of 3268831_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.835 | MS1 | 121.4656604228 | 31.1446315264 | 256 | 504990 | -85.68 | 14.37 | 336.46 | 0.18 | 2.42 | 1594 |
| 2024-09-20 22:21:32.936 | MS1 | 121.4656712934 | 31.1446311791 | 256 | 504990 | -91.09 | 15.24 | 325.02 | 0.00 | 2.98 | 1584 |
| 2024-09-20 22:21:33.242 | MS1 | 121.4656679463 | 31.1446339881 | 256 | 504990 | -89.84 | 14.33 | 346.10 | 0.08 | 2.11 | 1578 |
| 2024-09-20 22:21:34.352 | MS1 | 121.4656618290 | 31.1446377233 | 256 | 504990 | -85.26 | 13.43 | 66.99 | 0.05 | 2.90 | 302 |
| 2024-09-20 22:21:35.241 | MS1 | 121.4656722882 | 31.1446358054 | 256 | 504990 | -91.41 | 15.19 | 96.56 | 0.15 | 2.27 | 323 |
| 2024-09-20 22:21:36.749 | MS1 | 121.4656749030 | 31.1446309250 | 256 | 504990 | -86.04 | 12.12 | 70.75 | 0.18 | 2.47 | 386 |
| 2024-09-20 22:21:37.530 | MS1 | 121.4656623428 | 31.1446237208 | 256 | 504990 | -91.29 | 10.76 | 86.06 | 0.05 | 2.99 | 479 |
| 2024-09-20 22:21:38.498 | MS1 | 121.4656733758 | 31.1446291284 | 256 | 504990 | -92.31 | 8.05 | 99.67 | 0.13 | 2.10 | 361 |
| 2024-09-20 22:21:39.743 | MS1 | 121.4656704902 | 31.1446330734 | 256 | 504990 | -90.64 | 12.65 | 46.18 | 0.07 | 2.36 | 438 |
| 2024-09-20 22:21:40.846 | MS1 | 121.4656580824 | 31.1446347496 | 256 | 504990 | -93.63 | 12.98 | 363.25 | 0.06 | 2.75 | 1585 |
| 2024-09-20 22:21:41.153 | MS1 | 121.4656653407 | 31.1446300105 | 256 | 504990 | -91.00 | 8.47 | 516.83 | 0.06 | 2.58 | 1599 |
| 2024-09-20 22:21:42.494 | MS1 | 121.4656724842 | 31.1446186330 | 256 | 504990 | -91.06 | 8.09 | 505.74 | 0.05 | 2.51 | 1568 |

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
| 3262315 | 4 | 121.4741285023 | 31.1495433306 | 70 | 15 | 0 | 30.5 | TDD | 302 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3268831 | 1 | 121.4669085310 | 31.1533046247 | 103 | 5 | 3 | 31.8 | TDD | 256 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3273935 | 2 | 121.4689649391 | 31.1501933572 | 43 | 7 | 1 | 43.1 | TDD | 1004 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3279296 | 3 | 121.4644464272 | 31.1465163841 | 69 | 9 | 6 | 33.5 | TDD | 797 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.197 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.218 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.318 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.318 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.054 | NREventA3 | measId:2;ServCellPCI:365;Se... |
| 2024-09-20 22:21:38.294 | NRHandoverAttempt | SourcePCI:365;SourceNR-ARFC... |
| 2024-09-20 22:21:38.338 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.353 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.463 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.463 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268831 | 1 | 6.3688 | 9.2239 | -116.8389 | 12.1386 | 86.8074 | 0.0076 | 0.0154 |
| 2024_09_20 22:00 | 3273935 | 2 | 19.8879 | 7.4705 | -116.0348 | 19.0476 | 189.4093 | 0.0094 | 0.0168 |
| 2024_09_20 22:00 | 3279296 | 3 | 8.9646 | 15.9062 | -117.6461 | 19.7489 | 86.2593 | 0.0176 | 0.0052 |
| 2024_09_20 22:00 | 3262315 | 4 | 14.2141 | 17.7520 | -117.7622 | 19.8389 | 163.8492 | 0.0011 | 0.0137 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413266_423A4911 | 504990 | 256 | -84.0 | 504990 | 797 | -87.3 | 504990 | 1004 | -93.9 | 504990 | 302 |
| MR_1774413266_04D94EC6 | 504990 | 256 | -84.2 | 504990 | 797 | -89.3 | 504990 | 1004 | -93.7 | 504990 | 302 |
| MR_1774413266_66C508D3 | 504990 | 256 | -86.6 | 504990 | 797 | -90.4 | 504990 | 1004 | -96.1 | 504990 | 302 |
| MR_1774413266_34CB7557 | 504990 | 256 | -85.5 | 504990 | 797 | -89.6 | 504990 | 1004 | -97.0 | 504990 | 302 |
| MR_1774413266_F0F5C46C | 504990 | 256 | -85.5 | 504990 | 797 | -88.2 | 504990 | 1004 | -95.2 | 504990 | 302 |
| MR_1774413266_9981C514 | 504990 | 256 | -84.7 | 504990 | 797 | -89.1 | 504990 | 1004 | -96.9 | 504990 | 302 |
| MR_1774413266_25396005 | 504990 | 256 | -85.3 | 504990 | 797 | -87.8 | 504990 | 1004 | -96.4 | 504990 | 302 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1644: `3db4928a-7d3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3db4928a-7d31-49ca-96cc-8ee8048c6c7e` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease A3 Offset threshold for 3219181_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1644] topology](images/train_1644.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3277397_1
- `C2`: Lift the tilt angle  of 3277397_1 by 10 degrees
- `C3`: Decrease transmission power for 3277397_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277397_1
- `C5`: Press down the tilt angle  of 3277397_1 by 10 degrees
- `C6`: Add neighbor relationship between 3253087_4 and 3277397_1
- `C7`: Press down the tilt angle of 3219181_2 by 10 degrees
- `C8`: Increase transmission power for 3219181_2
- `C9`: Adjust the azimuth of 3277397_1 by 50 degrees
- `C10`: Decrease A3 Offset threshold for 3219181_2 **← 정답**
- `C11`: Lift the tilt angle of 3219181_2 by 10 degrees
- `C12`: Adjust the azimuth of 3219181_2 by 40 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277397_1
- `C14`: Add neighbor relationship between 3219181_2 and 3277397_1
- `C15`: Decrease transmission power for 3219181_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease A3 Offset threshold for 3277397_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219181_2
- `C19`: Increase transmission power for 3277397_1
- `C20`: Check test server and transmission issues
- `C21`: Increase A3 Offset threshold for 3219181_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219181_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.937 | MS1 | 121.4656746802 | 31.1446277771 | 482 | 504990 | -83.09 | 14.07 | 568.90 | 0.18 | 2.40 | 1563 |
| 2024-09-20 22:21:32.383 | MS1 | 121.4656653613 | 31.1446279168 | 482 | 504990 | -76.99 | 12.96 | 345.01 | 0.01 | 2.18 | 1564 |
| 2024-09-20 22:21:33.347 | MS1 | 121.4656672951 | 31.1446297086 | 482 | 504990 | -75.26 | 14.69 | 457.09 | 0.01 | 2.44 | 1567 |
| 2024-09-20 22:21:34.318 | MS1 | 121.4656689445 | 31.1446239489 | 482 | 504990 | -85.77 | -0.11 | 60.17 | 0.02 | 1.41 | 1596 |
| 2024-09-20 22:21:35.897 | MS1 | 121.4656738195 | 31.1446367390 | 482 | 504990 | -88.65 | -2.95 | 48.11 | 0.09 | 1.33 | 1594 |
| 2024-09-20 22:21:36.547 | MS1 | 121.4656716958 | 31.1446266222 | 482 | 504990 | -91.34 | -2.07 | 54.84 | 0.13 | 1.31 | 1586 |
| 2024-09-20 22:21:37.350 | MS1 | 121.4656698500 | 31.1446183885 | 482 | 504990 | -85.59 | -3.51 | 30.57 | 0.20 | 1.29 | 1584 |
| 2024-09-20 22:21:38.198 | MS1 | 121.4656630542 | 31.1446272968 | 482 | 504990 | -91.43 | -0.83 | 67.37 | 0.01 | 1.37 | 1582 |
| 2024-09-20 22:21:39.441 | MS1 | 121.4656601184 | 31.1446289709 | 177 | 504990 | -82.51 | 16.26 | 293.16 | 0.01 | 1.43 | 1586 |
| 2024-09-20 22:21:40.322 | MS1 | 121.4656759773 | 31.1446217708 | 177 | 504990 | -82.92 | 14.83 | 338.01 | 0.15 | 2.26 | 1586 |
| 2024-09-20 22:21:41.426 | MS1 | 121.4656684257 | 31.1446186080 | 177 | 504990 | -77.80 | 14.34 | 579.24 | 0.04 | 2.70 | 1566 |
| 2024-09-20 22:21:42.859 | MS1 | 121.4656671473 | 31.1446362572 | 177 | 504990 | -83.24 | 16.27 | 487.90 | 0.07 | 2.57 | 1594 |

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
| 3219181 | 2 | 121.4750791596 | 31.1476372901 | 289 | 14 | 12 | 18.3 | TDD | 482 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3253087 | 4 | 121.4698886394 | 31.1472717740 | 214 | 10 | 12 | 16.7 | TDD | 622 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3266853 | 3 | 121.4701775522 | 31.1557234837 | 83 | 6 | 10 | 20.8 | TDD | 259 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3277397 | 1 | 121.4668032338 | 31.1456053942 | 328 | 11 | 12 | 34.3 | TDD | 177 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.173 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.314 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.314 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.967 | NREventA3 | measId:2;ServCellPCI:258;Se... |
| 2024-09-20 22:21:38.207 | NRHandoverAttempt | SourcePCI:258;SourceNR-ARFC... |
| 2024-09-20 22:21:38.250 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.262 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.399 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.399 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277397 | 1 | 14.8560 | 19.2170 | -115.3994 | 15.6607 | 178.1430 | 0.0054 | 0.0014 |
| 2024_09_20 22:00 | 3219181 | 2 | 13.6798 | 13.0144 | -114.5689 | 12.6623 | 90.0613 | 0.0114 | 0.1742 |
| 2024_09_20 22:00 | 3266853 | 3 | 15.1810 | 15.6519 | -116.6256 | 19.4406 | 108.7656 | 0.0023 | 0.0191 |
| 2024_09_20 22:00 | 3253087 | 4 | 8.2752 | 5.8116 | -115.1474 | 5.9448 | 192.7987 | 0.0058 | 0.0139 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414043_E064EA16 | 504990 | 482 | -84.2 | 504990 | 177 | -83.4 | 504990 | 622 | -87.3 | 504990 | 259 |
| MR_1774414043_ABADF0F7 | 504990 | 482 | -84.2 | 504990 | 177 | -83.4 | 504990 | 622 | -87.1 | 504990 | 259 |
| MR_1774414043_BE3BFB4F | 504990 | 177 | -82.5 | 504990 | 482 | -87.4 | 504990 | 622 | -89.3 | 504990 | 259 |
| MR_1774414043_52E710FA | 504990 | 482 | -86.9 | 504990 | 177 | -80.7 | 504990 | 622 | -89.0 | 504990 | 259 |
| MR_1774414043_BC9A23C5 | 504990 | 177 | -80.6 | 504990 | 482 | -86.9 | 504990 | 622 | -88.0 | 504990 | 259 |
| MR_1774414043_F59903EB | 504990 | 482 | -83.9 | 504990 | 177 | -80.3 | 504990 | 622 | -87.4 | 504990 | 259 |
| MR_1774414043_3743C841 | 504990 | 482 | -87.3 | 504990 | 177 | -82.7 | 504990 | 622 | -88.0 | 504990 | 259 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1645: `b27461cd-cce...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b27461cd-cce3-4448-a90e-f387e12f19de` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1645] topology](images/train_1645.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3210478_4 and 3229759_3
- `C2`: Add neighbor relationship between 3248061_2 and 3229759_3
- `C3`: Increase A3 Offset threshold for 3248061_2
- `C4`: Adjust the azimuth of 3248061_2 by 41 degrees
- `C5`: Check test server and transmission issues
- `C6`: Decrease A3 Offset threshold for 3229759_3
- `C7`: Decrease transmission power for 3229759_3
- `C8`: Press down the tilt angle  of 3229759_3 by 10 degrees
- `C9`: Decrease transmission power for 3248061_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248061_2
- `C11`: Decrease A3 Offset threshold for 3248061_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229759_3
- `C13`: Increase A3 Offset threshold for 3229759_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248061_2
- `C15`: Lift the tilt angle  of 3229759_3 by 10 degrees
- `C16`: Insufficient data; more data is needed for judgment. **← 정답**
- `C17`: Adjust the azimuth of 3229759_3 by 2 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229759_3
- `C19`: Lift the tilt angle of 3248061_2 by 3 degrees
- `C20`: Increase transmission power for 3248061_2
- `C21`: Press down the tilt angle of 3248061_2 by 3 degrees
- `C22`: Increase transmission power for 3229759_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.467 | MS1 | 121.4656706484 | 31.1446355108 | 932 | 504990 | -86.29 | 14.86 | 315.72 | 0.11 | 2.42 | 1593 |
| 2024-09-20 22:21:32.453 | MS1 | 121.4656673002 | 31.1446281814 | 932 | 504990 | -87.41 | 16.40 | 580.01 | 0.06 | 2.83 | 1583 |
| 2024-09-20 22:21:33.973 | MS1 | 121.4656665707 | 31.1446302385 | 932 | 504990 | -89.18 | 12.41 | 496.99 | 0.20 | 2.55 | 1592 |
| 2024-09-20 22:21:34.315 | MS1 | 121.4656723836 | 31.1446332120 | 932 | 504990 | -90.40 | 16.11 | 71.01 | 0.04 | 2.40 | 1563 |
| 2024-09-20 22:21:35.939 | MS1 | 121.4656743098 | 31.1446347380 | 932 | 504990 | -91.90 | 15.87 | 85.61 | 0.15 | 2.26 | 1576 |
| 2024-09-20 22:21:36.257 | MS1 | 121.4656777596 | 31.1446332261 | 932 | 504990 | -90.68 | 13.51 | 74.85 | 0.18 | 2.89 | 1599 |
| 2024-09-20 22:21:37.438 | MS1 | 121.4656646087 | 31.1446361176 | 932 | 504990 | -89.89 | 11.99 | 93.71 | 0.08 | 2.12 | 1561 |
| 2024-09-20 22:21:38.789 | MS1 | 121.4656688171 | 31.1446183926 | 932 | 504990 | -93.48 | 11.74 | 69.25 | 0.01 | 2.40 | 1599 |
| 2024-09-20 22:21:39.853 | MS1 | 121.4656729775 | 31.1446307216 | 932 | 504990 | -91.71 | 8.79 | 67.44 | 0.03 | 2.97 | 1591 |
| 2024-09-20 22:21:40.814 | MS1 | 121.4656774363 | 31.1446266489 | 932 | 504990 | -90.75 | 11.13 | 321.47 | 0.04 | 2.94 | 1599 |
| 2024-09-20 22:21:41.934 | MS1 | 121.4656648307 | 31.1446276912 | 932 | 504990 | -92.93 | 7.53 | 514.84 | 0.03 | 2.69 | 1589 |
| 2024-09-20 22:21:42.229 | MS1 | 121.4656634766 | 31.1446321716 | 932 | 504990 | -90.30 | 12.61 | 607.87 | 0.05 | 2.56 | 1576 |

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
| 3210478 | 4 | 121.4750359728 | 31.1550208155 | 12 | 14 | 10 | 48.0 | TDD | 934 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3229759 | 3 | 121.4703716799 | 31.1480475974 | 232 | 15 | 3 | 48.2 | TDD | 174 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3248061 | 2 | 121.4695653616 | 31.1516378508 | 164 | 0 | 3 | 41.6 | TDD | 932 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3253527 | 1 | 121.4724328330 | 31.1512905305 | 326 | 4 | 7 | 33.7 | TDD | 40 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.465 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.490 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.629 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.629 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.302 | NREventA3 | measId:2;ServCellPCI:399;Se... |
| 2024-09-20 22:21:38.542 | NRHandoverAttempt | SourcePCI:399;SourceNR-ARFC... |
| 2024-09-20 22:21:38.583 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.598 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.718 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.718 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3253527 | 1 | 85.3698 | 90.1331 | -117.2201 | 9.0117 | 184.7974 | 0.0173 | 0.0169 |
| 2024_09_19 22:00 | 3248061 | 2 | 86.8772 | 83.8604 | -115.0464 | 5.2078 | 110.1815 | 0.0027 | 0.0159 |
| 2024_09_19 22:00 | 3229759 | 3 | 77.6442 | 86.9615 | -114.3216 | 19.4524 | 181.5592 | 0.0190 | 0.0006 |
| 2024_09_19 22:00 | 3210478 | 4 | 80.9341 | 76.8822 | -116.0942 | 13.1960 | 115.1208 | 0.0054 | 0.0178 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413242_AE546677 | 504990 | 932 | -91.3 | 504990 | 174 | -89.6 | 504990 | 934 | -99.9 | 504990 | 40 |
| MR_1774413242_715BE619 | 504990 | 932 | -90.4 | 504990 | 174 | -92.0 | 504990 | 934 | -99.6 | 504990 | 40 |
| MR_1774413242_BFD9B3FF | 504990 | 932 | -89.2 | 504990 | 174 | -91.0 | 504990 | 934 | -102.8 | 504990 | 40 |
| MR_1774413242_3E36A41B | 504990 | 932 | -90.2 | 504990 | 174 | -91.8 | 504990 | 934 | -102.5 | 504990 | 40 |
| MR_1774413242_2BC152D7 | 504990 | 932 | -90.1 | 504990 | 174 | -92.5 | 504990 | 934 | -101.7 | 504990 | 40 |
| MR_1774413242_0EC2346A | 504990 | 932 | -88.9 | 504990 | 174 | -90.8 | 504990 | 934 | -102.3 | 504990 | 40 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1646: `ec4053bc-19d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ec4053bc-19d0-455a-8c50-8704a48b2140` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Lift the tilt angle  of 3237313_2 by 4 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1646] topology](images/train_1646.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269061_1
- `C2`: Increase transmission power for 3260328_3
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Adjust the azimuth of 3237313_2 by 50 degrees
- `C5`: Add neighbor relationship between 3269061_1 and 3260328_3
- `C6`: Increase transmission power for 3269061_1
- `C7`: Add neighbor relationship between 3237313_2 and 3260328_3
- `C8`: Increase A3 Offset threshold for 3269061_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260328_3
- `C10`: Decrease A3 Offset threshold for 3260328_3
- `C11`: Lift the tilt angle  of 3237313_2 by 4 degrees **← 정답**
- `C12`: Decrease transmission power for 3260328_3
- `C13`: Adjust the azimuth of 3269061_1 by 42 degrees
- `C14`: Press down the tilt angle of 3269061_1 by 2 degrees
- `C15`: Decrease A3 Offset threshold for 3269061_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260328_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269061_1
- `C18`: Lift the tilt angle of 3269061_1 by 2 degrees
- `C19`: Press down the tilt angle  of 3237313_2 by 4 degrees
- `C20`: Decrease transmission power for 3269061_1
- `C21`: Check test server and transmission issues
- `C22`: Increase A3 Offset threshold for 3260328_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.274 | MS1 | 121.4656634090 | 31.1446288926 | 832 | 504990 | -91.35 | 12.66 | 307.60 | 0.19 | 2.76 | 1573 |
| 2024-09-20 22:21:32.934 | MS1 | 121.4656743222 | 31.1446359628 | 832 | 504990 | -86.78 | 13.92 | 433.63 | 0.03 | 2.04 | 1572 |
| 2024-09-20 22:21:33.785 | MS1 | 121.4656609530 | 31.1446224186 | 832 | 504990 | -89.27 | 13.14 | 456.95 | 0.09 | 2.27 | 1599 |
| 2024-09-20 22:21:34.480 | MS1 | 121.4656779254 | 31.1446377694 | 832 | 504990 | -89.51 | 16.55 | 89.91 | 0.08 | 2.16 | 1578 |
| 2024-09-20 22:21:35.187 | MS1 | 121.4656676861 | 31.1446379268 | 832 | 504990 | -91.89 | 13.96 | 59.15 | 0.02 | 2.05 | 1572 |
| 2024-09-20 22:21:36.247 | MS1 | 121.4656643240 | 31.1446284352 | 832 | 504990 | -91.14 | 17.39 | 90.52 | 0.04 | 2.59 | 1562 |
| 2024-09-20 22:21:37.586 | MS1 | 121.4656673861 | 31.1446327381 | 832 | 504990 | -90.73 | 8.36 | 80.07 | 0.05 | 2.67 | 1578 |
| 2024-09-20 22:21:38.159 | MS1 | 121.4656724895 | 31.1446286821 | 832 | 504990 | -89.29 | 8.83 | 43.74 | 0.06 | 2.42 | 1599 |
| 2024-09-20 22:21:39.816 | MS1 | 121.4656588340 | 31.1446288081 | 832 | 504990 | -90.65 | 9.59 | 84.33 | 0.08 | 2.73 | 1567 |
| 2024-09-20 22:21:40.486 | MS1 | 121.4656636529 | 31.1446260019 | 832 | 504990 | -92.78 | 12.87 | 475.03 | 0.18 | 2.86 | 1584 |
| 2024-09-20 22:21:41.672 | MS1 | 121.4656698583 | 31.1446247629 | 832 | 504990 | -91.96 | 7.24 | 533.23 | 0.01 | 2.06 | 1594 |
| 2024-09-20 22:21:42.390 | MS1 | 121.4656702408 | 31.1446329135 | 832 | 504990 | -91.08 | 7.49 | 402.37 | 0.13 | 2.07 | 1583 |

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
| 3237313 | 2 | 121.4700336344 | 31.1496224386 | 60 | 15 | 5 | 39.4 | TDD | 311 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3260328 | 3 | 121.4755308692 | 31.1440664658 | 85 | 2 | 4 | 38.4 | TDD | 805 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3269061 | 1 | 121.4747207125 | 31.1459977013 | 218 | 0 | 3 | 36.8 | TDD | 832 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3273221 | 4 | 121.4716558600 | 31.1498174572 | 254 | 5 | 8 | 33.8 | TDD | 975 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.496 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.515 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.631 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.631 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.340 | NREventA3 | measId:2;ServCellPCI:252;Se... |
| 2024-09-20 22:21:38.580 | NRHandoverAttempt | SourcePCI:252;SourceNR-ARFC... |
| 2024-09-20 22:21:38.614 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.624 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.739 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.739 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269061 | 1 | 85.6212 | 75.4762 | -115.0977 | 16.8744 | 182.0029 | 0.0185 | 0.0193 |
| 2024_09_20 22:00 | 3237313 | 2 | 5.2399 | 11.3697 | -117.0145 | 16.4388 | 143.4311 | 0.0115 | 0.0142 |
| 2024_09_20 22:00 | 3260328 | 3 | 12.2900 | 9.0713 | -117.9862 | 11.3583 | 188.9565 | 0.0138 | 0.0056 |
| 2024_09_20 22:00 | 3273221 | 4 | 12.6395 | 19.0353 | -116.0751 | 14.7303 | 148.4994 | 0.0130 | 0.0005 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415542_7EB9BF11 | 504990 | 832 | -89.5 | 504990 | 805 | -97.4 | 504990 | 311 | -101.2 | 504990 | 975 |
| MR_1774415542_17093FC3 | 504990 | 832 | -90.9 | 504990 | 805 | -99.4 | 504990 | 311 | -102.9 | 504990 | 975 |
| MR_1774415542_2A5B33AD | 504990 | 832 | -88.6 | 504990 | 805 | -97.8 | 504990 | 311 | -102.6 | 504990 | 975 |
| MR_1774415542_7060B5DD | 504990 | 832 | -91.5 | 504990 | 805 | -98.2 | 504990 | 311 | -104.0 | 504990 | 975 |
| MR_1774415542_13A1D40C | 504990 | 832 | -88.5 | 504990 | 805 | -98.5 | 504990 | 311 | -102.7 | 504990 | 975 |
| MR_1774415542_EF6B9A24 | 504990 | 832 | -89.5 | 504990 | 805 | -96.0 | 504990 | 311 | -102.5 | 504990 | 975 |
| MR_1774415542_72F7B61E | 504990 | 832 | -89.7 | 504990 | 805 | -97.1 | 504990 | 311 | -100.5 | 504990 | 975 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1647: `772a6e3d-cef...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `772a6e3d-cef1-488d-85cf-e5ec7fc99f8f` |
| Tag | **multiple-answer** |
| 정답 | **C4|C18** |
| C4 의미 | Adjust the azimuth of 3273116_4 by 35 degrees |
| C18 의미 | Increase transmission power for 3273116_4 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1647] topology](images/train_1647.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3273116_4
- `C2`: Increase transmission power for 3266909_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266909_2
- `C4`: Adjust the azimuth of 3273116_4 by 35 degrees **← 정답**
- `C5`: Decrease A3 Offset threshold for 3266909_2
- `C6`: Add neighbor relationship between 3273116_4 and 3266909_2
- `C7`: Decrease transmission power for 3273116_4
- `C8`: Increase A3 Offset threshold for 3273116_4
- `C9`: Lift the tilt angle  of 3266909_2 by 3 degrees
- `C10`: Decrease transmission power for 3266909_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273116_4
- `C12`: Press down the tilt angle  of 3266909_2 by 3 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Lift the tilt angle of 3273116_4 by 10 degrees
- `C15`: Adjust the azimuth of 3266909_2 by 45 degrees
- `C16`: Add neighbor relationship between 3212608_1 and 3266909_2
- `C17`: Increase A3 Offset threshold for 3266909_2
- `C18`: Increase transmission power for 3273116_4 **← 정답**
- `C19`: Check test server and transmission issues
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266909_2
- `C21`: Press down the tilt angle of 3273116_4 by 10 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273116_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.261 | MS1 | 121.4656687522 | 31.1446256534 | 534 | 504990 | -91.11 | 17.96 | 445.07 | 0.14 | 2.40 | 1590 |
| 2024-09-20 22:21:32.914 | MS1 | 121.4656678915 | 31.1446195761 | 534 | 504990 | -92.49 | 14.45 | 587.50 | 0.14 | 2.45 | 1581 |
| 2024-09-20 22:21:33.142 | MS1 | 121.4656659887 | 31.1446355627 | 534 | 504990 | -89.01 | 15.50 | 490.51 | 0.10 | 2.75 | 1593 |
| 2024-09-20 22:21:34.636 | MS1 | 121.4656687628 | 31.1446247575 | 534 | 504990 | -106.27 | 0.91 | 52.66 | 0.11 | 1.30 | 1577 |
| 2024-09-20 22:21:35.773 | MS1 | 121.4656584992 | 31.1446209832 | 534 | 504990 | -101.76 | -0.37 | 68.10 | 0.15 | 1.47 | 1576 |
| 2024-09-20 22:21:36.193 | MS1 | 121.4656613462 | 31.1446295702 | 534 | 504990 | -109.82 | 1.54 | 30.61 | 0.02 | 1.19 | 1578 |
| 2024-09-20 22:21:37.525 | MS1 | 121.4656708851 | 31.1446193065 | 534 | 504990 | -102.37 | -0.83 | 45.64 | 0.02 | 1.06 | 1583 |
| 2024-09-20 22:21:38.246 | MS1 | 121.4656719522 | 31.1446349553 | 534 | 504990 | -108.90 | -0.81 | 25.45 | 0.17 | 1.14 | 1583 |
| 2024-09-20 22:21:39.852 | MS1 | 121.4656615361 | 31.1446265141 | 534 | 504990 | -106.99 | -1.41 | 50.57 | 0.01 | 1.32 | 1571 |
| 2024-09-20 22:21:40.850 | MS1 | 121.4656656030 | 31.1446246437 | 534 | 504990 | -94.08 | 12.56 | 452.76 | 0.17 | 2.13 | 1585 |
| 2024-09-20 22:21:41.618 | MS1 | 121.4656764079 | 31.1446266517 | 534 | 504990 | -90.79 | 13.65 | 533.77 | 0.10 | 2.98 | 1597 |
| 2024-09-20 22:21:42.104 | MS1 | 121.4656601307 | 31.1446360697 | 534 | 504990 | -88.65 | 15.96 | 421.95 | 0.01 | 2.33 | 1581 |

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
| 3212608 | 1 | 121.4716412435 | 31.1555184040 | 179 | 8 | 3 | 42.4 | TDD | 561 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3266909 | 2 | 121.4656111344 | 31.1557921192 | 135 | 2 | 2 | 23.6 | TDD | 853 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3273116 | 4 | 121.4746992498 | 31.1459037450 | 226 | 12 | 11 | 26.6 | TDD | 534 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3274186 | 3 | 121.4704872328 | 31.1534223133 | 264 | 10 | 7 | 26.7 | TDD | 581 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.008 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.025 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.148 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.148 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.386 | NREventA2 | measId:1;ServCellPCI:395;Se... |
| 2024-09-20 22:21:34.487 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212608 | 1 | 7.0056 | 11.7675 | -114.3646 | 10.5317 | 133.6823 | 0.0178 | 0.0197 |
| 2024_09_20 22:00 | 3266909 | 2 | 17.1202 | 18.0645 | -117.8045 | 19.1373 | 145.0697 | 0.0176 | 0.0150 |
| 2024_09_20 22:00 | 3274186 | 3 | 9.8935 | 7.6667 | -116.2527 | 12.1336 | 102.2050 | 0.0179 | 0.0178 |
| 2024_09_20 22:00 | 3273116 | 4 | 17.6394 | 16.3075 | -115.8271 | 13.3621 | 96.4690 | 0.1816 | 0.0039 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416463_EFEB5000 | 504990 | 534 | -106.7 | 504990 | 853 | -110.9 | 504990 | 561 | -119.1 | 504990 | 581 |
| MR_1774416463_406BDED1 | 504990 | 534 | -104.3 | 504990 | 853 | -114.2 | 504990 | 561 | -117.6 | 504990 | 581 |
| MR_1774416463_58E8FACA | 504990 | 534 | -105.7 | 504990 | 853 | -113.6 | 504990 | 561 | -116.9 | 504990 | 581 |
| MR_1774416463_F1A9EB16 | 504990 | 534 | -108.0 | 504990 | 853 | -113.5 | 504990 | 561 | -116.9 | 504990 | 581 |
| MR_1774416463_98C3A8E5 | 504990 | 534 | -107.1 | 504990 | 853 | -110.8 | 504990 | 561 | -119.5 | 504990 | 581 |
| MR_1774416463_52C9A580 | 504990 | 534 | -107.5 | 504990 | 853 | -111.0 | 504990 | 561 | -118.0 | 504990 | 581 |
| MR_1774416463_F9C5A0D4 | 504990 | 534 | -105.3 | 504990 | 853 | -114.5 | 504990 | 561 | -118.0 | 504990 | 581 |
| MR_1774416463_5FA27BB1 | 504990 | 534 | -104.5 | 504990 | 853 | -111.1 | 504990 | 561 | -119.0 | 504990 | 581 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1648: `ae8cc132-59a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ae8cc132-59a9-4d4a-b5fd-0afbfeb5db01` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Add neighbor relationship between 3267310_3 and 3270592_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1648] topology](images/train_1648.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267310_3
- `C2`: Lift the tilt angle  of 3270592_1 by 4 degrees
- `C3`: Increase A3 Offset threshold for 3270592_1
- `C4`: Adjust the azimuth of 3270592_1 by 29 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270592_1
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Lift the tilt angle of 3267310_3 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3270592_1
- `C9`: Press down the tilt angle of 3267310_3 by 10 degrees
- `C10`: Add neighbor relationship between 3267310_3 and 3270592_1 **← 정답**
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267310_3
- `C12`: Press down the tilt angle  of 3270592_1 by 4 degrees
- `C13`: Decrease transmission power for 3267310_3
- `C14`: Add neighbor relationship between 3264662_2 and 3270592_1
- `C15`: Increase transmission power for 3270592_1
- `C16`: Increase transmission power for 3267310_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270592_1
- `C18`: Check test server and transmission issues
- `C19`: Adjust the azimuth of 3267310_3 by 50 degrees
- `C20`: Decrease A3 Offset threshold for 3267310_3
- `C21`: Increase A3 Offset threshold for 3267310_3
- `C22`: Decrease transmission power for 3270592_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.917 | MS1 | 121.4656660667 | 31.1446269739 | 166 | 504990 | -75.29 | 15.11 | 433.18 | 0.15 | 2.49 | 1592 |
| 2024-09-20 22:21:32.736 | MS1 | 121.4656594192 | 31.1446222066 | 166 | 504990 | -77.10 | 17.59 | 370.57 | 0.05 | 2.50 | 1574 |
| 2024-09-20 22:21:33.296 | MS1 | 121.4656729788 | 31.1446326069 | 166 | 504990 | -82.06 | 14.41 | 298.36 | 0.07 | 2.25 | 1573 |
| 2024-09-20 22:21:34.733 | MS1 | 121.4656680699 | 31.1446298558 | 166 | 504990 | -93.46 | -2.49 | 68.68 | 0.11 | 1.22 | 1587 |
| 2024-09-20 22:21:35.864 | MS1 | 121.4656672205 | 31.1446256922 | 166 | 504990 | -90.76 | -3.36 | 30.17 | 0.13 | 1.46 | 1590 |
| 2024-09-20 22:21:36.815 | MS1 | 121.4656678782 | 31.1446183943 | 166 | 504990 | -93.53 | -2.53 | 65.70 | 0.04 | 1.32 | 1560 |
| 2024-09-20 22:21:37.545 | MS1 | 121.4656588216 | 31.1446210437 | 166 | 504990 | -89.80 | -0.01 | 65.48 | 0.18 | 1.10 | 1593 |
| 2024-09-20 22:21:38.769 | MS1 | 121.4656657428 | 31.1446250023 | 166 | 504990 | -79.49 | 14.01 | 470.17 | 0.06 | 1.11 | 1583 |
| 2024-09-20 22:21:39.366 | MS1 | 121.4656684619 | 31.1446334766 | 166 | 504990 | -81.72 | 17.34 | 441.79 | 0.18 | 1.13 | 1561 |
| 2024-09-20 22:21:40.157 | MS1 | 121.4656683784 | 31.1446227342 | 166 | 504990 | -76.00 | 16.37 | 506.95 | 0.16 | 2.14 | 1599 |
| 2024-09-20 22:21:41.916 | MS1 | 121.4656610273 | 31.1446295029 | 166 | 504990 | -80.56 | 13.16 | 515.20 | 0.08 | 2.54 | 1565 |
| 2024-09-20 22:21:42.710 | MS1 | 121.4656758692 | 31.1446330209 | 166 | 504990 | -80.42 | 13.01 | 460.57 | 0.00 | 2.08 | 1588 |

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
| 3264326 | 4 | 121.4667941587 | 31.1494615493 | 221 | 6 | 9 | 16.7 | TDD | 247 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3264662 | 2 | 121.4649012049 | 31.1517117142 | 261 | 10 | 3 | 15.5 | TDD | 115 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3267310 | 3 | 121.4657772918 | 31.1477324914 | 101 | 10 | 2 | 28.0 | TDD | 166 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3270592 | 1 | 121.4755329955 | 31.1513767407 | 202 | 2 | 2 | 38.9 | TDD | 513 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.116 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.135 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.272 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.272 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.948 | NREventA3 | measId:2;ServCellPCI:503;Se... |
| 2024-09-20 22:21:35.948 | NREventA3 | measId:2;ServCellPCI:503;Se... |
| 2024-09-20 22:21:36.948 | NREventA3 | measId:2;ServCellPCI:503;Se... |
| 2024-09-20 22:21:39.448 | NRRRCReestablishAttempt | PCI:503 |
| 2024-09-20 22:21:39.465 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.475 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.613 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.613 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270592 | 1 | 13.2482 | 18.7231 | -116.6110 | 9.9372 | 170.7273 | 0.0162 | 0.0050 |
| 2024_09_20 22:00 | 3264662 | 2 | 19.4312 | 11.9563 | -114.7774 | 19.2926 | 131.8172 | 0.0137 | 0.0084 |
| 2024_09_20 22:00 | 3267310 | 3 | 16.7111 | 17.7634 | -114.1080 | 16.6541 | 187.2204 | 0.0096 | 0.1026 |
| 2024_09_20 22:00 | 3264326 | 4 | 11.7037 | 11.4617 | -114.6585 | 11.1524 | 143.1997 | 0.0152 | 0.0062 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413510_CE56F2CD | 504990 | 166 | -94.8 | 504990 | 513 | -87.8 | 504990 | 115 | -92.3 | 504990 | 247 |
| MR_1774413510_12265F19 | 504990 | 166 | -94.5 | 504990 | 513 | -87.8 | 504990 | 115 | -90.7 | 504990 | 247 |
| MR_1774413510_226B88C6 | 504990 | 513 | -86.8 | 504990 | 166 | -94.2 | 504990 | 115 | -92.7 | 504990 | 247 |
| MR_1774413510_789B19BB | 504990 | 166 | -92.5 | 504990 | 513 | -87.4 | 504990 | 115 | -91.9 | 504990 | 247 |
| MR_1774413510_253F9FD9 | 504990 | 166 | -95.2 | 504990 | 513 | -88.4 | 504990 | 115 | -92.5 | 504990 | 247 |
| MR_1774413510_99ADAB67 | 504990 | 513 | -87.6 | 504990 | 166 | -94.9 | 504990 | 115 | -90.8 | 504990 | 247 |
| MR_1774413510_AB84921C | 504990 | 166 | -92.6 | 504990 | 513 | -88.2 | 504990 | 115 | -90.4 | 504990 | 247 |
| MR_1774413510_3EDD3543 | 504990 | 166 | -95.3 | 504990 | 513 | -88.9 | 504990 | 115 | -92.5 | 504990 | 247 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1649: `f86de2b9-9ab...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f86de2b9-9abb-4a0b-8c75-f3f54947a708` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Add neighbor relationship between 3218428_4 and 3263515_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1649] topology](images/train_1649.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3263515_2 by 5 degrees
- `C2`: Add neighbor relationship between 3218428_4 and 3263515_2 **← 정답**
- `C3`: Add neighbor relationship between 3246190_1 and 3263515_2
- `C4`: Press down the tilt angle of 3218428_4 by 10 degrees
- `C5`: Decrease A3 Offset threshold for 3263515_2
- `C6`: Increase transmission power for 3263515_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Lift the tilt angle of 3218428_4 by 10 degrees
- `C9`: Increase A3 Offset threshold for 3218428_4
- `C10`: Adjust the azimuth of 3218428_4 by 43 degrees
- `C11`: Decrease transmission power for 3218428_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218428_4
- `C13`: Check test server and transmission issues
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218428_4
- `C15`: Decrease A3 Offset threshold for 3218428_4
- `C16`: Press down the tilt angle  of 3263515_2 by 5 degrees
- `C17`: Adjust the azimuth of 3263515_2 by 12 degrees
- `C18`: Increase A3 Offset threshold for 3263515_2
- `C19`: Decrease transmission power for 3263515_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263515_2
- `C21`: Increase transmission power for 3218428_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263515_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.262 | MS1 | 121.4656747292 | 31.1446247975 | 951 | 504990 | -78.93 | 16.68 | 315.12 | 0.11 | 2.70 | 1587 |
| 2024-09-20 22:21:32.869 | MS1 | 121.4656678086 | 31.1446343924 | 951 | 504990 | -77.68 | 13.74 | 492.33 | 0.17 | 2.01 | 1566 |
| 2024-09-20 22:21:33.230 | MS1 | 121.4656684132 | 31.1446247877 | 951 | 504990 | -83.75 | 13.62 | 509.65 | 0.11 | 2.64 | 1589 |
| 2024-09-20 22:21:34.556 | MS1 | 121.4656632408 | 31.1446196741 | 951 | 504990 | -88.28 | -3.75 | 64.01 | 0.04 | 1.24 | 1578 |
| 2024-09-20 22:21:35.570 | MS1 | 121.4656736741 | 31.1446186985 | 951 | 504990 | -88.75 | -0.59 | 40.24 | 0.19 | 1.23 | 1564 |
| 2024-09-20 22:21:36.752 | MS1 | 121.4656722026 | 31.1446372511 | 951 | 504990 | -94.20 | -0.78 | 68.51 | 0.04 | 1.25 | 1576 |
| 2024-09-20 22:21:37.251 | MS1 | 121.4656711572 | 31.1446252256 | 951 | 504990 | -92.49 | -0.13 | 43.01 | 0.11 | 1.10 | 1599 |
| 2024-09-20 22:21:38.944 | MS1 | 121.4656624048 | 31.1446228893 | 951 | 504990 | -81.93 | 14.95 | 360.21 | 0.20 | 1.46 | 1574 |
| 2024-09-20 22:21:39.365 | MS1 | 121.4656680526 | 31.1446269926 | 951 | 504990 | -82.49 | 16.73 | 448.53 | 0.02 | 1.03 | 1598 |
| 2024-09-20 22:21:40.367 | MS1 | 121.4656654416 | 31.1446330885 | 951 | 504990 | -84.46 | 13.70 | 470.28 | 0.05 | 2.71 | 1568 |
| 2024-09-20 22:21:41.203 | MS1 | 121.4656639507 | 31.1446344324 | 951 | 504990 | -76.72 | 12.63 | 483.68 | 0.18 | 2.66 | 1590 |
| 2024-09-20 22:21:42.401 | MS1 | 121.4656619058 | 31.1446307745 | 951 | 504990 | -79.18 | 12.36 | 428.58 | 0.00 | 2.79 | 1582 |

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
| 3218428 | 4 | 121.4671953304 | 31.1445132408 | 232 | 9 | 2 | 35.1 | TDD | 951 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3246190 | 1 | 121.4667103928 | 31.1550127409 | 187 | 0 | 1 | 40.6 | TDD | 800 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3263515 | 2 | 121.4649356932 | 31.1501738220 | 186 | 3 | 0 | 18.2 | TDD | 107 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3276672 | 3 | 121.4720229723 | 31.1442108607 | 140 | 7 | 8 | 29.3 | TDD | 69 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.466 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.481 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.599 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.599 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.291 | NREventA3 | measId:2;ServCellPCI:276;Se... |
| 2024-09-20 22:21:36.291 | NREventA3 | measId:2;ServCellPCI:276;Se... |
| 2024-09-20 22:21:37.291 | NREventA3 | measId:2;ServCellPCI:276;Se... |
| 2024-09-20 22:21:39.791 | NRRRCReestablishAttempt | PCI:276 |
| 2024-09-20 22:21:39.807 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.822 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.968 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.968 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246190 | 1 | 15.1472 | 13.1781 | -115.7409 | 18.3999 | 178.5482 | 0.0144 | 0.0092 |
| 2024_09_20 22:00 | 3263515 | 2 | 7.1359 | 7.5411 | -115.9266 | 16.9174 | 184.1556 | 0.0068 | 0.0094 |
| 2024_09_20 22:00 | 3276672 | 3 | 13.4222 | 13.2265 | -115.1314 | 19.9615 | 180.3803 | 0.0047 | 0.0119 |
| 2024_09_20 22:00 | 3218428 | 4 | 18.2301 | 9.1067 | -116.9397 | 5.8588 | 179.7457 | 0.0061 | 0.1039 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414611_4B0EC238 | 504990 | 107 | -83.1 | 504990 | 951 | -87.6 | 504990 | 800 | -88.1 | 504990 | 69 |
| MR_1774414611_926045FF | 504990 | 951 | -87.9 | 504990 | 107 | -81.5 | 504990 | 800 | -86.1 | 504990 | 69 |
| MR_1774414611_356917CF | 504990 | 951 | -88.9 | 504990 | 107 | -83.9 | 504990 | 800 | -86.3 | 504990 | 69 |
| MR_1774414611_929C12C9 | 504990 | 951 | -88.3 | 504990 | 107 | -81.8 | 504990 | 800 | -85.9 | 504990 | 69 |
| MR_1774414611_370316FA | 504990 | 951 | -88.6 | 504990 | 107 | -81.6 | 504990 | 800 | -88.2 | 504990 | 69 |
| MR_1774414611_55F51879 | 504990 | 951 | -86.8 | 504990 | 107 | -84.7 | 504990 | 800 | -87.2 | 504990 | 69 |
| MR_1774414611_5026458A | 504990 | 951 | -88.9 | 504990 | 107 | -84.3 | 504990 | 800 | -87.5 | 504990 | 69 |
| MR_1774414611_A9A60911 | 504990 | 951 | -89.4 | 504990 | 107 | -81.3 | 504990 | 800 | -84.7 | 504990 | 69 |

> *... 2개 열 생략 (전체 14열)*

---
