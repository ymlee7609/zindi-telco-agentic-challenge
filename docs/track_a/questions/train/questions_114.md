# Track A 문제 분석 — train[1130]~train[1139]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1130] ~ train[1139] (10개)

## 목차

1. [문제 1130: `d30a0f19-fc1...`](#1130) — single-answer, 정답: C17
2. [문제 1131: `d2c1fd11-894...`](#1131) — single-answer, 정답: C12
3. [문제 1132: `c6de170b-dff...`](#1132) — single-answer, 정답: C18
4. [문제 1133: `2e48e33e-4bc...`](#1133) — single-answer, 정답: C9
5. [문제 1134: `d33d7d8c-b4d...`](#1134) — single-answer, 정답: C6
6. [문제 1135: `f6c7ac90-a0e...`](#1135) — single-answer, 정답: C21
7. [문제 1136: `82dc234d-58b...`](#1136) — single-answer, 정답: C15
8. [문제 1137: `30296816-d27...`](#1137) — single-answer, 정답: C9
9. [문제 1138: `861fe916-9dc...`](#1138) — single-answer, 정답: C5
10. [문제 1139: `e3f2b933-117...`](#1139) — single-answer, 정답: C19

---

### 문제 1130: `d30a0f19-fc1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d30a0f19-fc15-47b3-8c7b-e22e50fb293c` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Add neighbor relationship between 3251729_4 and 3263138_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1130] topology](images/train_1130.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Adjust the azimuth of 3251729_4 by 43 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263138_1
- `C4`: Decrease A3 Offset threshold for 3251729_4
- `C5`: Decrease transmission power for 3251729_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251729_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251729_4
- `C8`: Adjust the azimuth of 3263138_1 by 32 degrees
- `C9`: Increase transmission power for 3263138_1
- `C10`: Decrease transmission power for 3263138_1
- `C11`: Press down the tilt angle of 3251729_4 by 10 degrees
- `C12`: Increase A3 Offset threshold for 3251729_4
- `C13`: Increase A3 Offset threshold for 3263138_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Lift the tilt angle of 3251729_4 by 10 degrees
- `C16`: Press down the tilt angle  of 3263138_1 by 4 degrees
- `C17`: Add neighbor relationship between 3251729_4 and 3263138_1 **← 정답**
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263138_1
- `C19`: Decrease A3 Offset threshold for 3263138_1
- `C20`: Lift the tilt angle  of 3263138_1 by 4 degrees
- `C21`: Add neighbor relationship between 3268900_3 and 3263138_1
- `C22`: Increase transmission power for 3251729_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.933 | MS1 | 121.4656699240 | 31.1446315175 | 367 | 504990 | -77.02 | 15.53 | 348.92 | 0.09 | 2.85 | 1598 |
| 2024-09-20 22:21:32.260 | MS1 | 121.4656724447 | 31.1446340503 | 367 | 504990 | -84.50 | 14.20 | 468.06 | 0.19 | 2.24 | 1585 |
| 2024-09-20 22:21:33.471 | MS1 | 121.4656611871 | 31.1446242306 | 367 | 504990 | -83.88 | 12.18 | 453.08 | 0.03 | 2.48 | 1562 |
| 2024-09-20 22:21:34.743 | MS1 | 121.4656772871 | 31.1446323399 | 367 | 504990 | -94.67 | -1.32 | 32.87 | 0.03 | 1.33 | 1584 |
| 2024-09-20 22:21:35.960 | MS1 | 121.4656761369 | 31.1446369761 | 367 | 504990 | -89.82 | -3.68 | 37.35 | 0.20 | 1.46 | 1567 |
| 2024-09-20 22:21:36.343 | MS1 | 121.4656762751 | 31.1446302084 | 367 | 504990 | -85.40 | -3.91 | 54.96 | 0.04 | 1.46 | 1598 |
| 2024-09-20 22:21:37.481 | MS1 | 121.4656751623 | 31.1446375624 | 367 | 504990 | -94.88 | -1.49 | 58.51 | 0.10 | 1.07 | 1563 |
| 2024-09-20 22:21:38.992 | MS1 | 121.4656651307 | 31.1446333493 | 367 | 504990 | -78.36 | 16.04 | 453.41 | 0.07 | 1.02 | 1573 |
| 2024-09-20 22:21:39.779 | MS1 | 121.4656655282 | 31.1446279304 | 367 | 504990 | -83.40 | 13.49 | 585.76 | 0.07 | 1.23 | 1566 |
| 2024-09-20 22:21:40.165 | MS1 | 121.4656584842 | 31.1446272001 | 367 | 504990 | -80.48 | 15.33 | 462.09 | 0.13 | 2.39 | 1587 |
| 2024-09-20 22:21:41.168 | MS1 | 121.4656585478 | 31.1446271005 | 367 | 504990 | -81.30 | 17.67 | 592.83 | 0.18 | 2.71 | 1570 |
| 2024-09-20 22:21:42.385 | MS1 | 121.4656665668 | 31.1446211120 | 367 | 504990 | -82.63 | 13.62 | 422.99 | 0.07 | 2.72 | 1585 |

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
| 3251729 | 4 | 121.4743415924 | 31.1468389960 | 296 | 12 | 3 | 16.5 | TDD | 367 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3263138 | 1 | 121.4734809113 | 31.1506752498 | 196 | 2 | 3 | 36.2 | TDD | 761 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3268900 | 3 | 121.4683777933 | 31.1494580391 | 244 | 14 | 4 | 46.1 | TDD | 212 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3272086 | 2 | 121.4687272397 | 31.1479020677 | 60 | 5 | 3 | 16.2 | TDD | 379 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.041 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.061 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.206 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.206 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.890 | NREventA3 | measId:2;ServCellPCI:323;Se... |
| 2024-09-20 22:21:35.890 | NREventA3 | measId:2;ServCellPCI:323;Se... |
| 2024-09-20 22:21:36.890 | NREventA3 | measId:2;ServCellPCI:323;Se... |
| 2024-09-20 22:21:39.390 | NRRRCReestablishAttempt | PCI:323 |
| 2024-09-20 22:21:39.400 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.415 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.546 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.546 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263138 | 1 | 11.1076 | 5.4729 | -117.1435 | 18.0062 | 184.8867 | 0.0178 | 0.0135 |
| 2024_09_20 22:00 | 3272086 | 2 | 8.6983 | 5.3752 | -116.2926 | 8.5897 | 197.5218 | 0.0003 | 0.0089 |
| 2024_09_20 22:00 | 3268900 | 3 | 19.3014 | 15.4264 | -115.0867 | 19.3482 | 116.3897 | 0.0177 | 0.0175 |
| 2024_09_20 22:00 | 3251729 | 4 | 9.9787 | 10.6497 | -114.8104 | 6.1309 | 157.3404 | 0.0030 | 0.1608 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414145_65D172DD | 504990 | 761 | -88.4 | 504990 | 367 | -95.9 | 504990 | 212 | -90.9 | 504990 | 379 |
| MR_1774414145_19DB2E05 | 504990 | 761 | -88.4 | 504990 | 367 | -94.4 | 504990 | 212 | -90.3 | 504990 | 379 |
| MR_1774414145_17F39F97 | 504990 | 761 | -90.8 | 504990 | 367 | -92.8 | 504990 | 212 | -89.9 | 504990 | 379 |
| MR_1774414145_2C08E029 | 504990 | 761 | -90.4 | 504990 | 367 | -96.4 | 504990 | 212 | -88.9 | 504990 | 379 |
| MR_1774414145_A3BA40F8 | 504990 | 761 | -90.4 | 504990 | 367 | -93.3 | 504990 | 212 | -90.5 | 504990 | 379 |
| MR_1774414145_109AD7CF | 504990 | 761 | -89.8 | 504990 | 367 | -95.3 | 504990 | 212 | -88.8 | 504990 | 379 |
| MR_1774414145_CB5953AA | 504990 | 367 | -95.6 | 504990 | 761 | -88.5 | 504990 | 212 | -91.8 | 504990 | 379 |
| MR_1774414145_90CF6B8C | 504990 | 367 | -93.0 | 504990 | 761 | -87.5 | 504990 | 212 | -90.8 | 504990 | 379 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1131: `d2c1fd11-894...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d2c1fd11-8941-43b9-9f16-7621c53adf24` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Lift the tilt angle  of 3215362_4 by 4 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1131] topology](images/train_1131.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3266196_3
- `C2`: Decrease A3 Offset threshold for 3266196_3
- `C3`: Increase transmission power for 3232878_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Adjust the azimuth of 3232878_2 by 50 degrees
- `C6`: Check test server and transmission issues
- `C7`: Decrease transmission power for 3232878_2
- `C8`: Adjust the azimuth of 3215362_4 by 50 degrees
- `C9`: Increase A3 Offset threshold for 3232878_2
- `C10`: Increase A3 Offset threshold for 3266196_3
- `C11`: Lift the tilt angle of 3232878_2 by 4 degrees
- `C12`: Lift the tilt angle  of 3215362_4 by 4 degrees **← 정답**
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232878_2
- `C14`: Add neighbor relationship between 3232878_2 and 3266196_3
- `C15`: Add neighbor relationship between 3215362_4 and 3266196_3
- `C16`: Press down the tilt angle  of 3215362_4 by 4 degrees
- `C17`: Press down the tilt angle of 3232878_2 by 4 degrees
- `C18`: Increase transmission power for 3266196_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266196_3
- `C20`: Decrease A3 Offset threshold for 3232878_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266196_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232878_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.622 | MS1 | 121.4656761598 | 31.1446292863 | 610 | 504990 | -88.64 | 13.03 | 496.53 | 0.07 | 2.79 | 1572 |
| 2024-09-20 22:21:32.208 | MS1 | 121.4656626441 | 31.1446341259 | 610 | 504990 | -87.03 | 14.77 | 437.22 | 0.04 | 2.29 | 1575 |
| 2024-09-20 22:21:33.138 | MS1 | 121.4656758519 | 31.1446202140 | 610 | 504990 | -91.98 | 16.27 | 568.13 | 0.10 | 2.75 | 1568 |
| 2024-09-20 22:21:34.380 | MS1 | 121.4656602615 | 31.1446196969 | 610 | 504990 | -91.38 | 16.14 | 71.44 | 0.08 | 2.09 | 1599 |
| 2024-09-20 22:21:35.100 | MS1 | 121.4656604335 | 31.1446208651 | 610 | 504990 | -88.36 | 14.98 | 60.05 | 0.07 | 2.67 | 1571 |
| 2024-09-20 22:21:36.334 | MS1 | 121.4656631712 | 31.1446350737 | 610 | 504990 | -89.46 | 17.49 | 54.65 | 0.07 | 2.16 | 1591 |
| 2024-09-20 22:21:37.645 | MS1 | 121.4656703872 | 31.1446290435 | 610 | 504990 | -91.57 | 12.77 | 66.85 | 0.10 | 2.62 | 1580 |
| 2024-09-20 22:21:38.767 | MS1 | 121.4656617479 | 31.1446281757 | 610 | 504990 | -93.76 | 7.48 | 74.49 | 0.17 | 2.18 | 1582 |
| 2024-09-20 22:21:39.875 | MS1 | 121.4656696047 | 31.1446334035 | 610 | 504990 | -92.41 | 8.18 | 76.43 | 0.12 | 2.27 | 1599 |
| 2024-09-20 22:21:40.386 | MS1 | 121.4656766218 | 31.1446325403 | 610 | 504990 | -92.52 | 7.78 | 346.24 | 0.15 | 2.17 | 1593 |
| 2024-09-20 22:21:41.891 | MS1 | 121.4656596358 | 31.1446355943 | 610 | 504990 | -89.12 | 8.47 | 501.81 | 0.19 | 2.41 | 1584 |
| 2024-09-20 22:21:42.570 | MS1 | 121.4656683186 | 31.1446258977 | 610 | 504990 | -91.85 | 10.17 | 318.34 | 0.17 | 2.06 | 1560 |

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
| 3215362 | 4 | 121.4666902448 | 31.1450562982 | 12 | 12 | 2 | 17.2 | TDD | 801 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3232878 | 2 | 121.4730909693 | 31.1517632562 | 172 | 2 | 8 | 41.5 | TDD | 610 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3258330 | 1 | 121.4740707691 | 31.1475107952 | 94 | 0 | 11 | 17.6 | TDD | 577 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3266196 | 3 | 121.4714101419 | 31.1554299600 | 119 | 3 | 1 | 20.2 | TDD | 731 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.990 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.007 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.152 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.152 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.831 | NREventA3 | measId:2;ServCellPCI:368;Se... |
| 2024-09-20 22:21:38.071 | NRHandoverAttempt | SourcePCI:368;SourceNR-ARFC... |
| 2024-09-20 22:21:38.109 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.124 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.268 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.268 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258330 | 1 | 5.3068 | 17.9947 | -117.0071 | 16.6514 | 152.3811 | 0.0062 | 0.0109 |
| 2024_09_20 22:00 | 3232878 | 2 | 80.4371 | 88.2549 | -117.0488 | 13.6746 | 195.5410 | 0.0038 | 0.0074 |
| 2024_09_20 22:00 | 3266196 | 3 | 8.5243 | 5.2462 | -114.5773 | 7.0293 | 193.4661 | 0.0070 | 0.0025 |
| 2024_09_20 22:00 | 3215362 | 4 | 8.7833 | 18.4526 | -115.4651 | 18.7039 | 176.7206 | 0.0034 | 0.0094 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417105_B83B216E | 504990 | 610 | -91.1 | 504990 | 731 | -91.6 | 504990 | 801 | -107.6 | 504990 | 577 |
| MR_1774417105_B77DC982 | 504990 | 610 | -93.0 | 504990 | 731 | -89.8 | 504990 | 801 | -104.6 | 504990 | 577 |
| MR_1774417105_F46E99D7 | 504990 | 610 | -89.9 | 504990 | 731 | -90.9 | 504990 | 801 | -104.0 | 504990 | 577 |
| MR_1774417105_5CE8035B | 504990 | 610 | -93.3 | 504990 | 731 | -92.2 | 504990 | 801 | -104.3 | 504990 | 577 |
| MR_1774417105_46DC33E5 | 504990 | 610 | -93.3 | 504990 | 731 | -91.7 | 504990 | 801 | -107.0 | 504990 | 577 |
| MR_1774417105_61B1402D | 504990 | 610 | -90.5 | 504990 | 731 | -90.7 | 504990 | 801 | -105.8 | 504990 | 577 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1132: `c6de170b-dff...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c6de170b-dffc-4eb9-92e7-ebc56f4fcf06` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Decrease A3 Offset threshold for 3240272_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1132] topology](images/train_1132.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226998_4
- `C2`: Decrease A3 Offset threshold for 3226998_4
- `C3`: Increase A3 Offset threshold for 3226998_4
- `C4`: Add neighbor relationship between 3240272_1 and 3226998_4
- `C5`: Decrease transmission power for 3226998_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240272_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240272_1
- `C8`: Increase transmission power for 3240272_1
- `C9`: Decrease transmission power for 3240272_1
- `C10`: Adjust the azimuth of 3226998_4 by 7 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Lift the tilt angle of 3240272_1 by 10 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226998_4
- `C14`: Press down the tilt angle  of 3226998_4 by 4 degrees
- `C15`: Increase transmission power for 3226998_4
- `C16`: Press down the tilt angle of 3240272_1 by 10 degrees
- `C17`: Adjust the azimuth of 3240272_1 by 50 degrees
- `C18`: Decrease A3 Offset threshold for 3240272_1 **← 정답**
- `C19`: Check test server and transmission issues
- `C20`: Lift the tilt angle  of 3226998_4 by 4 degrees
- `C21`: Increase A3 Offset threshold for 3240272_1
- `C22`: Add neighbor relationship between 3237192_2 and 3226998_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.438 | MS1 | 121.4656719940 | 31.1446213252 | 846 | 504990 | -82.76 | 17.82 | 305.97 | 0.10 | 2.22 | 1593 |
| 2024-09-20 22:21:32.367 | MS1 | 121.4656639981 | 31.1446218355 | 846 | 504990 | -81.32 | 17.44 | 574.37 | 0.11 | 2.61 | 1591 |
| 2024-09-20 22:21:33.480 | MS1 | 121.4656776166 | 31.1446278939 | 846 | 504990 | -78.56 | 12.74 | 364.95 | 0.09 | 2.91 | 1561 |
| 2024-09-20 22:21:34.745 | MS1 | 121.4656771923 | 31.1446246900 | 846 | 504990 | -89.46 | -0.26 | 74.43 | 0.11 | 1.44 | 1574 |
| 2024-09-20 22:21:35.650 | MS1 | 121.4656677378 | 31.1446182460 | 846 | 504990 | -87.62 | -2.40 | 55.57 | 0.20 | 1.29 | 1600 |
| 2024-09-20 22:21:36.899 | MS1 | 121.4656602601 | 31.1446367017 | 846 | 504990 | -85.47 | -3.46 | 73.96 | 0.15 | 1.34 | 1593 |
| 2024-09-20 22:21:37.864 | MS1 | 121.4656680212 | 31.1446214548 | 846 | 504990 | -91.56 | -1.59 | 65.45 | 0.04 | 1.22 | 1586 |
| 2024-09-20 22:21:38.391 | MS1 | 121.4656700923 | 31.1446327898 | 846 | 504990 | -86.12 | -1.50 | 57.42 | 0.07 | 1.36 | 1592 |
| 2024-09-20 22:21:39.856 | MS1 | 121.4656671188 | 31.1446194592 | 103 | 504990 | -75.14 | 13.66 | 264.70 | 0.19 | 1.22 | 1568 |
| 2024-09-20 22:21:40.120 | MS1 | 121.4656588759 | 31.1446275531 | 103 | 504990 | -77.28 | 13.19 | 361.77 | 0.17 | 2.17 | 1583 |
| 2024-09-20 22:21:41.882 | MS1 | 121.4656618194 | 31.1446209418 | 103 | 504990 | -81.31 | 15.72 | 348.25 | 0.12 | 2.76 | 1584 |
| 2024-09-20 22:21:42.190 | MS1 | 121.4656640320 | 31.1446200902 | 103 | 504990 | -82.58 | 12.01 | 315.35 | 0.16 | 2.32 | 1597 |

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
| 3226998 | 4 | 121.4657752863 | 31.1544009305 | 188 | 2 | 9 | 42.6 | TDD | 103 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3229482 | 3 | 121.4759842406 | 31.1508099403 | 215 | 3 | 7 | 28.6 | TDD | 302 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3237192 | 2 | 121.4647656954 | 31.1440112355 | 163 | 10 | 3 | 38.6 | TDD | 484 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3240272 | 1 | 121.4742045152 | 31.1542498418 | 79 | 14 | 3 | 31.3 | TDD | 846 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.807 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.824 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.974 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.974 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.648 | NREventA3 | measId:2;ServCellPCI:148;Se... |
| 2024-09-20 22:21:37.888 | NRHandoverAttempt | SourcePCI:148;SourceNR-ARFC... |
| 2024-09-20 22:21:37.921 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.933 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.080 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.080 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240272 | 1 | 11.6127 | 5.8354 | -115.6943 | 8.1814 | 95.1883 | 0.0029 | 0.1330 |
| 2024_09_20 22:00 | 3237192 | 2 | 19.4875 | 5.8717 | -114.4315 | 9.4017 | 111.9909 | 0.0072 | 0.0035 |
| 2024_09_20 22:00 | 3229482 | 3 | 10.5769 | 7.3290 | -116.5973 | 13.9817 | 195.3449 | 0.0085 | 0.0008 |
| 2024_09_20 22:00 | 3226998 | 4 | 18.4353 | 15.0135 | -115.0961 | 13.2179 | 193.1728 | 0.0155 | 0.0118 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412494_BBE4C1CC | 504990 | 846 | -90.8 | 504990 | 103 | -82.8 | 504990 | 484 | -90.4 | 504990 | 302 |
| MR_1774412494_54860F0E | 504990 | 846 | -90.3 | 504990 | 103 | -85.7 | 504990 | 484 | -89.3 | 504990 | 302 |
| MR_1774412494_2E6DD8E3 | 504990 | 103 | -84.5 | 504990 | 846 | -90.7 | 504990 | 484 | -88.0 | 504990 | 302 |
| MR_1774412494_CA6ADCB7 | 504990 | 846 | -88.1 | 504990 | 103 | -82.8 | 504990 | 484 | -88.1 | 504990 | 302 |
| MR_1774412494_4823BE15 | 504990 | 103 | -84.7 | 504990 | 846 | -88.0 | 504990 | 484 | -90.1 | 504990 | 302 |
| MR_1774412494_173D7B44 | 504990 | 846 | -90.9 | 504990 | 103 | -85.6 | 504990 | 484 | -87.5 | 504990 | 302 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1133: `2e48e33e-4bc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2e48e33e-4bca-4ee8-9ea4-926561cb14e7` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Lift the tilt angle  of 3215131_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1133] topology](images/train_1133.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3236444_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236444_2
- `C4`: Add neighbor relationship between 3215131_3 and 3236444_2
- `C5`: Increase A3 Offset threshold for 3220023_1
- `C6`: Press down the tilt angle of 3220023_1 by 4 degrees
- `C7`: Increase A3 Offset threshold for 3236444_2
- `C8`: Decrease transmission power for 3220023_1
- `C9`: Lift the tilt angle  of 3215131_3 by 10 degrees **← 정답**
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220023_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236444_2
- `C12`: Check test server and transmission issues
- `C13`: Lift the tilt angle of 3220023_1 by 4 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220023_1
- `C15`: Press down the tilt angle  of 3215131_3 by 10 degrees
- `C16`: Decrease A3 Offset threshold for 3236444_2
- `C17`: Add neighbor relationship between 3220023_1 and 3236444_2
- `C18`: Decrease A3 Offset threshold for 3220023_1
- `C19`: Increase transmission power for 3220023_1
- `C20`: Adjust the azimuth of 3215131_3 by 50 degrees
- `C21`: Adjust the azimuth of 3220023_1 by 31 degrees
- `C22`: Increase transmission power for 3236444_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.667 | MS1 | 121.4656720749 | 31.1446199705 | 39 | 504990 | -91.78 | 13.46 | 348.30 | 0.06 | 2.66 | 1573 |
| 2024-09-20 22:21:32.594 | MS1 | 121.4656717753 | 31.1446278134 | 39 | 504990 | -87.94 | 15.06 | 485.70 | 0.12 | 2.10 | 1562 |
| 2024-09-20 22:21:33.140 | MS1 | 121.4656777058 | 31.1446198939 | 39 | 504990 | -85.78 | 13.47 | 520.34 | 0.00 | 2.67 | 1598 |
| 2024-09-20 22:21:34.936 | MS1 | 121.4656587958 | 31.1446180443 | 39 | 504990 | -86.14 | 16.59 | 47.96 | 0.08 | 2.27 | 1591 |
| 2024-09-20 22:21:35.995 | MS1 | 121.4656753371 | 31.1446224215 | 39 | 504990 | -89.71 | 16.88 | 71.96 | 0.01 | 2.18 | 1575 |
| 2024-09-20 22:21:36.559 | MS1 | 121.4656660476 | 31.1446335028 | 39 | 504990 | -86.56 | 17.54 | 99.08 | 0.05 | 2.20 | 1566 |
| 2024-09-20 22:21:37.772 | MS1 | 121.4656754278 | 31.1446230358 | 39 | 504990 | -90.25 | 10.02 | 54.79 | 0.12 | 2.73 | 1592 |
| 2024-09-20 22:21:38.479 | MS1 | 121.4656686983 | 31.1446294454 | 39 | 504990 | -89.54 | 9.77 | 69.31 | 0.20 | 2.07 | 1591 |
| 2024-09-20 22:21:39.922 | MS1 | 121.4656769994 | 31.1446363422 | 39 | 504990 | -90.71 | 11.36 | 70.75 | 0.09 | 2.32 | 1597 |
| 2024-09-20 22:21:40.531 | MS1 | 121.4656706301 | 31.1446243392 | 39 | 504990 | -90.75 | 7.53 | 382.76 | 0.11 | 2.63 | 1587 |
| 2024-09-20 22:21:41.663 | MS1 | 121.4656776864 | 31.1446298432 | 39 | 504990 | -89.48 | 8.21 | 523.38 | 0.04 | 2.09 | 1568 |
| 2024-09-20 22:21:42.530 | MS1 | 121.4656592492 | 31.1446285238 | 39 | 504990 | -91.11 | 7.24 | 342.58 | 0.08 | 2.50 | 1562 |

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
| 3215131 | 3 | 121.4704283877 | 31.1488370407 | 128 | 15 | 5 | 39.6 | TDD | 678 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3220023 | 1 | 121.4740032655 | 31.1479271940 | 276 | 1 | 5 | 41.0 | TDD | 39 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3236444 | 2 | 121.4683384480 | 31.1489329648 | 12 | 8 | 2 | 29.0 | TDD | 805 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3258168 | 4 | 121.4696237843 | 31.1479295373 | 76 | 14 | 2 | 49.3 | TDD | 959 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.577 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.596 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.708 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.708 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.378 | NREventA3 | measId:2;ServCellPCI:246;Se... |
| 2024-09-20 22:21:38.618 | NRHandoverAttempt | SourcePCI:246;SourceNR-ARFC... |
| 2024-09-20 22:21:38.667 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.678 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.811 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.811 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220023 | 1 | 90.4416 | 76.5902 | -114.1816 | 13.4145 | 126.1140 | 0.0101 | 0.0165 |
| 2024_09_20 22:00 | 3236444 | 2 | 11.7603 | 13.7870 | -117.9190 | 11.6916 | 83.7367 | 0.0031 | 0.0190 |
| 2024_09_20 22:00 | 3215131 | 3 | 16.4342 | 19.1751 | -115.2469 | 16.7254 | 111.2429 | 0.0175 | 0.0034 |
| 2024_09_20 22:00 | 3258168 | 4 | 8.1975 | 17.6564 | -117.4940 | 13.8948 | 163.3509 | 0.0049 | 0.0082 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414726_A5D450B1 | 504990 | 39 | -87.8 | 504990 | 805 | -88.0 | 504990 | 678 | -96.0 | 504990 | 959 |
| MR_1774414726_30DD2F99 | 504990 | 39 | -84.6 | 504990 | 805 | -89.3 | 504990 | 678 | -96.6 | 504990 | 959 |
| MR_1774414726_4BB8B24F | 504990 | 39 | -86.0 | 504990 | 805 | -89.6 | 504990 | 678 | -96.0 | 504990 | 959 |
| MR_1774414726_DBF97B7F | 504990 | 39 | -86.6 | 504990 | 805 | -86.0 | 504990 | 678 | -95.4 | 504990 | 959 |
| MR_1774414726_5BC2D3C6 | 504990 | 39 | -87.7 | 504990 | 805 | -87.7 | 504990 | 678 | -98.5 | 504990 | 959 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1134: `d33d7d8c-b4d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d33d7d8c-b4d9-4b21-8795-66b7a197d507` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease A3 Offset threshold for 3278660_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1134] topology](images/train_1134.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3278660_2
- `C2`: Add neighbor relationship between 3265392_1 and 3222440_3
- `C3`: Check test server and transmission issues
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222440_3
- `C5`: Lift the tilt angle  of 3222440_3 by 5 degrees
- `C6`: Decrease A3 Offset threshold for 3278660_2 **← 정답**
- `C7`: Press down the tilt angle  of 3222440_3 by 5 degrees
- `C8`: Adjust the azimuth of 3222440_3 by 16 degrees
- `C9`: Decrease A3 Offset threshold for 3222440_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278660_2
- `C11`: Increase transmission power for 3222440_3
- `C12`: Press down the tilt angle of 3278660_2 by 5 degrees
- `C13`: Lift the tilt angle of 3278660_2 by 5 degrees
- `C14`: Decrease transmission power for 3222440_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222440_3
- `C16`: Increase transmission power for 3278660_2
- `C17`: Adjust the azimuth of 3278660_2 by 23 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278660_2
- `C19`: Increase A3 Offset threshold for 3278660_2
- `C20`: Add neighbor relationship between 3278660_2 and 3222440_3
- `C21`: Increase A3 Offset threshold for 3222440_3
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.478 | MS1 | 121.4656767037 | 31.1446183246 | 129 | 504990 | -84.68 | 15.40 | 458.31 | 0.20 | 2.34 | 1596 |
| 2024-09-20 22:21:32.699 | MS1 | 121.4656726474 | 31.1446247849 | 129 | 504990 | -79.73 | 13.47 | 508.54 | 0.03 | 2.71 | 1571 |
| 2024-09-20 22:21:33.689 | MS1 | 121.4656744104 | 31.1446351579 | 129 | 504990 | -81.39 | 14.35 | 489.43 | 0.13 | 2.27 | 1581 |
| 2024-09-20 22:21:34.990 | MS1 | 121.4656779500 | 31.1446327799 | 129 | 504990 | -90.99 | -2.27 | 68.98 | 0.09 | 1.02 | 1588 |
| 2024-09-20 22:21:35.952 | MS1 | 121.4656696357 | 31.1446293657 | 129 | 504990 | -83.02 | -2.46 | 45.65 | 0.09 | 1.43 | 1569 |
| 2024-09-20 22:21:36.880 | MS1 | 121.4656764344 | 31.1446342718 | 129 | 504990 | -84.86 | -3.21 | 33.34 | 0.09 | 1.06 | 1593 |
| 2024-09-20 22:21:37.780 | MS1 | 121.4656646611 | 31.1446238974 | 129 | 504990 | -92.22 | -3.60 | 63.99 | 0.15 | 1.24 | 1569 |
| 2024-09-20 22:21:38.104 | MS1 | 121.4656605955 | 31.1446375363 | 129 | 504990 | -87.52 | -1.42 | 47.89 | 0.08 | 1.30 | 1596 |
| 2024-09-20 22:21:39.935 | MS1 | 121.4656627616 | 31.1446194988 | 331 | 504990 | -81.28 | 17.56 | 216.24 | 0.01 | 1.05 | 1587 |
| 2024-09-20 22:21:40.172 | MS1 | 121.4656750736 | 31.1446298215 | 331 | 504990 | -80.05 | 13.09 | 412.65 | 0.13 | 2.76 | 1576 |
| 2024-09-20 22:21:41.536 | MS1 | 121.4656729585 | 31.1446311006 | 331 | 504990 | -84.84 | 16.10 | 367.24 | 0.17 | 2.02 | 1590 |
| 2024-09-20 22:21:42.459 | MS1 | 121.4656722142 | 31.1446315470 | 331 | 504990 | -75.86 | 16.79 | 498.59 | 0.17 | 2.04 | 1595 |

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
| 3222440 | 3 | 121.4666349504 | 31.1523071035 | 202 | 4 | 0 | 22.4 | TDD | 331 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3233043 | 4 | 121.4664518807 | 31.1523726280 | 170 | 14 | 9 | 21.8 | TDD | 335 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3265392 | 1 | 121.4652925116 | 31.1464428632 | 76 | 7 | 5 | 41.6 | TDD | 689 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3278660 | 2 | 121.4739874621 | 31.1517428567 | 248 | 3 | 9 | 33.7 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.101 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.124 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.272 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.272 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.990 | NREventA3 | measId:2;ServCellPCI:484;Se... |
| 2024-09-20 22:21:38.230 | NRHandoverAttempt | SourcePCI:484;SourceNR-ARFC... |
| 2024-09-20 22:21:38.275 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.288 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.390 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.390 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265392 | 1 | 9.8002 | 17.3354 | -116.9639 | 17.6476 | 191.5465 | 0.0192 | 0.0174 |
| 2024_09_20 22:00 | 3278660 | 2 | 17.4628 | 5.7332 | -115.2278 | 16.4694 | 169.7658 | 0.0004 | 0.1923 |
| 2024_09_20 22:00 | 3222440 | 3 | 17.0536 | 11.9671 | -117.8701 | 7.4663 | 179.6890 | 0.0048 | 0.0094 |
| 2024_09_20 22:00 | 3233043 | 4 | 16.7153 | 8.3673 | -114.5610 | 15.5643 | 169.5863 | 0.0100 | 0.0098 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417221_597AC90D | 504990 | 331 | -87.4 | 504990 | 129 | -89.4 | 504990 | 689 | -88.5 | 504990 | 335 |
| MR_1774417221_479A7FFF | 504990 | 129 | -91.9 | 504990 | 331 | -88.4 | 504990 | 689 | -88.7 | 504990 | 335 |
| MR_1774417221_17879089 | 504990 | 129 | -91.2 | 504990 | 331 | -88.2 | 504990 | 689 | -87.8 | 504990 | 335 |
| MR_1774417221_08CE9DF3 | 504990 | 129 | -92.0 | 504990 | 331 | -86.2 | 504990 | 689 | -87.7 | 504990 | 335 |
| MR_1774417221_2C87E750 | 504990 | 331 | -85.1 | 504990 | 129 | -92.7 | 504990 | 689 | -86.0 | 504990 | 335 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1135: `f6c7ac90-a0e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f6c7ac90-a0e5-4d36-b176-4a903b2fdcea` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Lift the tilt angle  of 3268348_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1135] topology](images/train_1135.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3210305_2 by 6 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212307_3
- `C3`: Decrease transmission power for 3212307_3
- `C4`: Decrease A3 Offset threshold for 3212307_3
- `C5`: Increase transmission power for 3212307_3
- `C6`: Decrease transmission power for 3210305_2
- `C7`: Increase A3 Offset threshold for 3210305_2
- `C8`: Adjust the azimuth of 3268348_1 by 50 degrees
- `C9`: Lift the tilt angle of 3210305_2 by 6 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Press down the tilt angle  of 3268348_1 by 10 degrees
- `C12`: Add neighbor relationship between 3268348_1 and 3212307_3
- `C13`: Decrease A3 Offset threshold for 3210305_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210305_2
- `C15`: Increase A3 Offset threshold for 3212307_3
- `C16`: Check test server and transmission issues
- `C17`: Adjust the azimuth of 3210305_2 by 10 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212307_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210305_2
- `C20`: Add neighbor relationship between 3210305_2 and 3212307_3
- `C21`: Lift the tilt angle  of 3268348_1 by 10 degrees **← 정답**
- `C22`: Increase transmission power for 3210305_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.161 | MS1 | 121.4656695842 | 31.1446247854 | 13 | 504990 | -91.86 | 16.87 | 408.93 | 0.17 | 2.38 | 1594 |
| 2024-09-20 22:21:32.751 | MS1 | 121.4656705083 | 31.1446357322 | 13 | 504990 | -86.53 | 16.34 | 558.55 | 0.20 | 2.06 | 1564 |
| 2024-09-20 22:21:33.450 | MS1 | 121.4656629894 | 31.1446367727 | 13 | 504990 | -85.59 | 15.06 | 340.23 | 0.08 | 2.36 | 1566 |
| 2024-09-20 22:21:34.566 | MS1 | 121.4656596031 | 31.1446352794 | 13 | 504990 | -89.71 | 17.06 | 74.75 | 0.01 | 2.20 | 1590 |
| 2024-09-20 22:21:35.529 | MS1 | 121.4656605776 | 31.1446330648 | 13 | 504990 | -88.46 | 14.16 | 90.96 | 0.09 | 2.28 | 1580 |
| 2024-09-20 22:21:36.285 | MS1 | 121.4656699524 | 31.1446318511 | 13 | 504990 | -88.78 | 13.28 | 56.86 | 0.17 | 2.92 | 1588 |
| 2024-09-20 22:21:37.193 | MS1 | 121.4656746319 | 31.1446192587 | 13 | 504990 | -89.67 | 8.89 | 77.63 | 0.01 | 2.38 | 1573 |
| 2024-09-20 22:21:38.460 | MS1 | 121.4656629277 | 31.1446269579 | 13 | 504990 | -89.18 | 10.57 | 76.03 | 0.15 | 2.99 | 1600 |
| 2024-09-20 22:21:39.270 | MS1 | 121.4656689111 | 31.1446189727 | 13 | 504990 | -92.58 | 10.92 | 58.26 | 0.11 | 2.89 | 1584 |
| 2024-09-20 22:21:40.638 | MS1 | 121.4656590829 | 31.1446338741 | 13 | 504990 | -89.87 | 8.29 | 373.46 | 0.11 | 2.46 | 1582 |
| 2024-09-20 22:21:41.832 | MS1 | 121.4656684302 | 31.1446201850 | 13 | 504990 | -91.92 | 9.25 | 570.35 | 0.05 | 2.42 | 1599 |
| 2024-09-20 22:21:42.729 | MS1 | 121.4656679784 | 31.1446329234 | 13 | 504990 | -89.81 | 10.22 | 531.94 | 0.02 | 2.13 | 1565 |

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
| 3210305 | 2 | 121.4709987837 | 31.1545035175 | 215 | 4 | 8 | 41.1 | TDD | 13 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3212307 | 3 | 121.4686883683 | 31.1449887059 | 6 | 13 | 12 | 20.1 | TDD | 116 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3245273 | 4 | 121.4743728754 | 31.1559077095 | 47 | 12 | 10 | 30.6 | TDD | 117 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3268348 | 1 | 121.4750734670 | 31.1495442977 | 3 | 7 | 11 | 28.9 | TDD | 968 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.016 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.040 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.167 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.167 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.820 | NREventA3 | measId:2;ServCellPCI:399;Se... |
| 2024-09-20 22:21:38.060 | NRHandoverAttempt | SourcePCI:399;SourceNR-ARFC... |
| 2024-09-20 22:21:38.107 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.120 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.254 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.254 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268348 | 1 | 15.3854 | 11.9528 | -116.2515 | 11.6682 | 157.3447 | 0.0024 | 0.0067 |
| 2024_09_20 22:00 | 3210305 | 2 | 94.2954 | 83.6019 | -117.1991 | 11.6115 | 173.0987 | 0.0083 | 0.0133 |
| 2024_09_20 22:00 | 3212307 | 3 | 13.9749 | 10.6958 | -117.6936 | 15.8357 | 92.5098 | 0.0113 | 0.0180 |
| 2024_09_20 22:00 | 3245273 | 4 | 17.5965 | 17.4009 | -114.8225 | 17.9209 | 123.8261 | 0.0003 | 0.0041 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416841_8EE0397E | 504990 | 13 | -88.7 | 504990 | 116 | -95.5 | 504990 | 968 | -98.8 | 504990 | 117 |
| MR_1774416841_A637CB40 | 504990 | 13 | -90.3 | 504990 | 116 | -94.8 | 504990 | 968 | -98.0 | 504990 | 117 |
| MR_1774416841_F7FCFADE | 504990 | 13 | -91.2 | 504990 | 116 | -96.7 | 504990 | 968 | -98.9 | 504990 | 117 |
| MR_1774416841_1EF3F8D5 | 504990 | 13 | -89.5 | 504990 | 116 | -95.7 | 504990 | 968 | -99.9 | 504990 | 117 |
| MR_1774416841_6F1B4D46 | 504990 | 13 | -88.4 | 504990 | 116 | -95.7 | 504990 | 968 | -99.3 | 504990 | 117 |
| MR_1774416841_1A2A27F6 | 504990 | 13 | -89.7 | 504990 | 116 | -95.4 | 504990 | 968 | -98.4 | 504990 | 117 |
| MR_1774416841_3D2C4860 | 504990 | 13 | -88.9 | 504990 | 116 | -95.0 | 504990 | 968 | -98.9 | 504990 | 117 |
| MR_1774416841_265E530A | 504990 | 13 | -91.1 | 504990 | 116 | -96.1 | 504990 | 968 | -99.0 | 504990 | 117 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1136: `82dc234d-58b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `82dc234d-58b2-4482-93d1-18889182596f` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Add neighbor relationship between 3218625_2 and 3241046_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1136] topology](images/train_1136.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3218625_2
- `C2`: Increase A3 Offset threshold for 3241046_4
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Lift the tilt angle of 3218625_2 by 10 degrees
- `C5`: Lift the tilt angle  of 3241046_4 by 6 degrees
- `C6`: Decrease transmission power for 3241046_4
- `C7`: Increase A3 Offset threshold for 3218625_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218625_2
- `C9`: Adjust the azimuth of 3241046_4 by 12 degrees
- `C10`: Increase transmission power for 3241046_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241046_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218625_2
- `C13`: Press down the tilt angle of 3218625_2 by 10 degrees
- `C14`: Press down the tilt angle  of 3241046_4 by 6 degrees
- `C15`: Add neighbor relationship between 3218625_2 and 3241046_4 **← 정답**
- `C16`: Decrease A3 Offset threshold for 3241046_4
- `C17`: Adjust the azimuth of 3218625_2 by 50 degrees
- `C18`: Add neighbor relationship between 3223536_1 and 3241046_4
- `C19`: Increase transmission power for 3218625_2
- `C20`: Check test server and transmission issues
- `C21`: Decrease A3 Offset threshold for 3218625_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241046_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.865 | MS1 | 121.4656711236 | 31.1446259287 | 942 | 504990 | -76.95 | 12.86 | 319.32 | 0.04 | 2.66 | 1575 |
| 2024-09-20 22:21:32.686 | MS1 | 121.4656623731 | 31.1446352350 | 942 | 504990 | -78.26 | 13.48 | 527.61 | 0.15 | 2.99 | 1589 |
| 2024-09-20 22:21:33.898 | MS1 | 121.4656700322 | 31.1446275420 | 942 | 504990 | -77.20 | 12.95 | 409.72 | 0.07 | 2.96 | 1564 |
| 2024-09-20 22:21:34.888 | MS1 | 121.4656677932 | 31.1446202123 | 942 | 504990 | -93.12 | -3.08 | 41.27 | 0.06 | 1.33 | 1597 |
| 2024-09-20 22:21:35.850 | MS1 | 121.4656756932 | 31.1446293356 | 942 | 504990 | -87.89 | -2.20 | 40.60 | 0.01 | 1.09 | 1566 |
| 2024-09-20 22:21:36.583 | MS1 | 121.4656768130 | 31.1446360713 | 942 | 504990 | -87.12 | -0.32 | 58.63 | 0.17 | 1.24 | 1575 |
| 2024-09-20 22:21:37.784 | MS1 | 121.4656703098 | 31.1446218203 | 942 | 504990 | -89.92 | -0.07 | 62.02 | 0.15 | 1.47 | 1574 |
| 2024-09-20 22:21:38.880 | MS1 | 121.4656668240 | 31.1446239205 | 942 | 504990 | -76.84 | 13.70 | 415.54 | 0.08 | 1.47 | 1592 |
| 2024-09-20 22:21:39.524 | MS1 | 121.4656613723 | 31.1446186892 | 942 | 504990 | -81.60 | 13.20 | 368.06 | 0.13 | 1.24 | 1589 |
| 2024-09-20 22:21:40.557 | MS1 | 121.4656706767 | 31.1446308783 | 942 | 504990 | -77.92 | 12.39 | 407.72 | 0.05 | 2.37 | 1592 |
| 2024-09-20 22:21:41.539 | MS1 | 121.4656671361 | 31.1446284504 | 942 | 504990 | -83.62 | 17.23 | 467.14 | 0.14 | 2.80 | 1574 |
| 2024-09-20 22:21:42.589 | MS1 | 121.4656592956 | 31.1446372436 | 942 | 504990 | -81.50 | 15.76 | 514.55 | 0.11 | 2.72 | 1568 |

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
| 3218625 | 2 | 121.4716834616 | 31.1497829523 | 349 | 7 | 5 | 36.9 | TDD | 942 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3223536 | 1 | 121.4742554641 | 31.1464059360 | 270 | 9 | 7 | 20.8 | TDD | 796 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3224367 | 3 | 121.4656119548 | 31.1472663721 | 245 | 5 | 8 | 43.9 | TDD | 326 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3241046 | 4 | 121.4746256512 | 31.1454432450 | 276 | 4 | 4 | 28.7 | TDD | 695 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.540 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.564 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.698 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.698 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.382 | NREventA3 | measId:2;ServCellPCI:928;Se... |
| 2024-09-20 22:21:36.382 | NREventA3 | measId:2;ServCellPCI:928;Se... |
| 2024-09-20 22:21:37.382 | NREventA3 | measId:2;ServCellPCI:928;Se... |
| 2024-09-20 22:21:39.882 | NRRRCReestablishAttempt | PCI:928 |
| 2024-09-20 22:21:39.893 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.907 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:40.049 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.049 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223536 | 1 | 13.8578 | 18.9034 | -115.6562 | 15.0678 | 117.1213 | 0.0096 | 0.0065 |
| 2024_09_20 22:00 | 3218625 | 2 | 5.8599 | 17.9096 | -116.9899 | 19.4915 | 177.1853 | 0.0134 | 0.1849 |
| 2024_09_20 22:00 | 3224367 | 3 | 12.1081 | 7.6920 | -114.3961 | 18.1542 | 82.0242 | 0.0184 | 0.0112 |
| 2024_09_20 22:00 | 3241046 | 4 | 6.6837 | 14.7113 | -117.1509 | 10.1014 | 111.4662 | 0.0128 | 0.0001 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415954_F40FD3BE | 504990 | 942 | -91.6 | 504990 | 695 | -89.6 | 504990 | 796 | -87.2 | 504990 | 326 |
| MR_1774415954_A6277D33 | 504990 | 942 | -93.9 | 504990 | 695 | -88.8 | 504990 | 796 | -89.0 | 504990 | 326 |
| MR_1774415954_303B2B63 | 504990 | 942 | -94.3 | 504990 | 695 | -88.9 | 504990 | 796 | -90.5 | 504990 | 326 |
| MR_1774415954_A3F7819C | 504990 | 942 | -91.9 | 504990 | 695 | -90.1 | 504990 | 796 | -87.6 | 504990 | 326 |
| MR_1774415954_F6D73126 | 504990 | 695 | -89.4 | 504990 | 942 | -91.6 | 504990 | 796 | -88.8 | 504990 | 326 |
| MR_1774415954_D0F0187E | 504990 | 695 | -88.6 | 504990 | 942 | -92.7 | 504990 | 796 | -88.3 | 504990 | 326 |
| MR_1774415954_F79E3083 | 504990 | 942 | -91.4 | 504990 | 695 | -88.9 | 504990 | 796 | -88.6 | 504990 | 326 |
| MR_1774415954_CC922F48 | 504990 | 695 | -89.2 | 504990 | 942 | -91.8 | 504990 | 796 | -90.4 | 504990 | 326 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1137: `30296816-d27...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `30296816-d271-4eee-9f4b-88df932ce34e` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1137] topology](images/train_1137.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3226827_1
- `C2`: Adjust the azimuth of 3226827_1 by 50 degrees
- `C3`: Add neighbor relationship between 3238719_2 and 3232347_4
- `C4`: Decrease A3 Offset threshold for 3232347_4
- `C5`: Press down the tilt angle  of 3232347_4 by 7 degrees
- `C6`: Decrease transmission power for 3226827_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226827_1
- `C8`: Increase transmission power for 3232347_4
- `C9`: Check test server and transmission issues **← 정답**
- `C10`: Increase A3 Offset threshold for 3226827_1
- `C11`: Decrease transmission power for 3232347_4
- `C12`: Lift the tilt angle of 3226827_1 by 3 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232347_4
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Lift the tilt angle  of 3232347_4 by 7 degrees
- `C16`: Press down the tilt angle of 3226827_1 by 3 degrees
- `C17`: Increase A3 Offset threshold for 3232347_4
- `C18`: Increase transmission power for 3226827_1
- `C19`: Adjust the azimuth of 3232347_4 by 50 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226827_1
- `C21`: Add neighbor relationship between 3226827_1 and 3232347_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232347_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.256 | MS1 | 121.4656777191 | 31.1446287152 | 144 | 504990 | -90.46 | 12.41 | 509.31 | 0.10 | 2.60 | 1585 |
| 2024-09-20 22:21:32.844 | MS1 | 121.4656664438 | 31.1446241394 | 144 | 504990 | -89.24 | 16.88 | 385.62 | 0.09 | 2.04 | 1563 |
| 2024-09-20 22:21:33.485 | MS1 | 121.4656737963 | 31.1446264224 | 144 | 504990 | -87.15 | 13.81 | 402.29 | 0.07 | 2.74 | 1565 |
| 2024-09-20 22:21:34.889 | MS1 | 121.4656626087 | 31.1446244354 | 144 | 504990 | -87.03 | 14.52 | 91.72 | 0.07 | 2.84 | 467 |
| 2024-09-20 22:21:35.285 | MS1 | 121.4656749802 | 31.1446355847 | 144 | 504990 | -90.97 | 12.84 | 59.13 | 0.04 | 2.43 | 399 |
| 2024-09-20 22:21:36.533 | MS1 | 121.4656643753 | 31.1446277038 | 144 | 504990 | -88.87 | 12.08 | 77.69 | 0.10 | 2.09 | 412 |
| 2024-09-20 22:21:37.609 | MS1 | 121.4656669650 | 31.1446208556 | 144 | 504990 | -89.58 | 12.42 | 86.52 | 0.09 | 2.44 | 457 |
| 2024-09-20 22:21:38.481 | MS1 | 121.4656623935 | 31.1446372452 | 144 | 504990 | -93.69 | 10.39 | 55.53 | 0.19 | 2.12 | 419 |
| 2024-09-20 22:21:39.938 | MS1 | 121.4656622755 | 31.1446265566 | 144 | 504990 | -90.38 | 7.76 | 80.33 | 0.14 | 2.60 | 482 |
| 2024-09-20 22:21:40.613 | MS1 | 121.4656688111 | 31.1446361313 | 144 | 504990 | -91.07 | 7.17 | 550.27 | 0.15 | 2.29 | 1597 |
| 2024-09-20 22:21:41.446 | MS1 | 121.4656739046 | 31.1446242093 | 144 | 504990 | -92.98 | 7.01 | 440.74 | 0.16 | 2.21 | 1580 |
| 2024-09-20 22:21:42.382 | MS1 | 121.4656643507 | 31.1446312547 | 144 | 504990 | -93.26 | 10.84 | 315.26 | 0.19 | 2.52 | 1579 |

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
| 3226827 | 1 | 121.4670775838 | 31.1524102110 | 359 | 1 | 9 | 26.7 | TDD | 144 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3231117 | 3 | 121.4709135517 | 31.1512506413 | 312 | 12 | 3 | 41.2 | TDD | 868 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3232347 | 4 | 121.4734952686 | 31.1539347750 | 158 | 5 | 6 | 39.1 | TDD | 645 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3238719 | 2 | 121.4732616886 | 31.1477728220 | 81 | 12 | 5 | 43.5 | TDD | 251 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.914 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.937 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.055 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.055 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.739 | NREventA3 | measId:2;ServCellPCI:950;Se... |
| 2024-09-20 22:21:37.979 | NRHandoverAttempt | SourcePCI:950;SourceNR-ARFC... |
| 2024-09-20 22:21:38.027 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.037 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.154 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.154 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226827 | 1 | 6.2692 | 9.9771 | -115.4761 | 15.6961 | 196.6450 | 0.0141 | 0.0055 |
| 2024_09_20 22:00 | 3238719 | 2 | 16.2999 | 18.6137 | -117.2711 | 9.5009 | 111.9696 | 0.0186 | 0.0152 |
| 2024_09_20 22:00 | 3231117 | 3 | 15.8506 | 11.0847 | -116.0315 | 16.1031 | 122.6795 | 0.0017 | 0.0182 |
| 2024_09_20 22:00 | 3232347 | 4 | 7.4521 | 17.2859 | -117.4267 | 19.9024 | 96.8764 | 0.0139 | 0.0145 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416565_BC813A87 | 504990 | 144 | -88.1 | 504990 | 645 | -92.4 | 504990 | 251 | -94.2 | 504990 | 868 |
| MR_1774416565_25CC211B | 504990 | 144 | -88.9 | 504990 | 645 | -95.3 | 504990 | 251 | -92.8 | 504990 | 868 |
| MR_1774416565_033E247B | 504990 | 144 | -88.6 | 504990 | 645 | -94.0 | 504990 | 251 | -95.3 | 504990 | 868 |
| MR_1774416565_EC39C806 | 504990 | 144 | -86.1 | 504990 | 645 | -93.4 | 504990 | 251 | -96.1 | 504990 | 868 |
| MR_1774416565_F6B95417 | 504990 | 144 | -88.0 | 504990 | 645 | -92.6 | 504990 | 251 | -96.4 | 504990 | 868 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1138: `861fe916-9dc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `861fe916-9dc4-46e8-952d-a6403a254925` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276828_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1138] topology](images/train_1138.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210066_5
- `C2`: Increase transmission power for 3276828_6
- `C3`: Increase A3 Offset threshold for 3276828_6
- `C4`: Press down the tilt angle of 3276828_6 by 3 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276828_6 **← 정답**
- `C6`: Lift the tilt angle  of 3210066_5 by 2 degrees
- `C7`: Adjust the azimuth of 3210066_5 by 39 degrees
- `C8`: Check test server and transmission issues
- `C9`: Lift the tilt angle of 3276828_6 by 3 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210066_5
- `C11`: Increase transmission power for 3210066_5
- `C12`: Press down the tilt angle  of 3210066_5 by 2 degrees
- `C13`: Add neighbor relationship between 3276828_6 and 3210066_5
- `C14`: Decrease transmission power for 3276828_6
- `C15`: Decrease A3 Offset threshold for 3276828_6
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease transmission power for 3210066_5
- `C18`: Add neighbor relationship between 3230158_7 and 3210066_5
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276828_6
- `C20`: Decrease A3 Offset threshold for 3210066_5
- `C21`: Increase A3 Offset threshold for 3210066_5
- `C22`: Adjust the azimuth of 3276828_6 by 43 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.680 | MS1 | 121.4656769014 | 31.1446209817 | 732 | 504990 | -95.54 | 14.05 | 334.48 | 0.13 | 2.73 | 1586 |
| 2024-09-20 22:21:32.464 | MS1 | 121.4656607167 | 31.1446256251 | 685 | 504990 | -94.02 | 14.40 | 472.33 | 0.16 | 2.83 | 1594 |
| 2024-09-20 22:21:33.380 | MS1 | 121.4656600437 | 31.1446194398 | 236 | 504990 | -94.18 | 13.78 | 361.82 | 0.10 | 2.59 | 1574 |
| 2024-09-20 22:21:34.579 | MS1 | 121.4656619173 | 31.1446345294 | 411 | 152650 | -88.33 | 5.27 | 61.67 | 0.14 | 1.90 | 995 |
| 2024-09-20 22:21:35.317 | MS1 | 121.4656662482 | 31.1446262201 | 667 | 152650 | -96.33 | 3.96 | 82.13 | 0.09 | 1.55 | 993 |
| 2024-09-20 22:21:36.646 | MS1 | 121.4656693275 | 31.1446296704 | 707 | 152650 | -88.73 | 2.72 | 76.77 | 0.05 | 1.91 | 969 |
| 2024-09-20 22:21:37.294 | MS1 | 121.4656669453 | 31.1446334939 | 783 | 152650 | -93.03 | 5.56 | 59.92 | 0.02 | 1.71 | 906 |
| 2024-09-20 22:21:38.846 | MS1 | 121.4656688312 | 31.1446330332 | 411 | 152650 | -91.64 | 5.60 | 48.83 | 0.12 | 1.88 | 952 |
| 2024-09-20 22:21:39.434 | MS1 | 121.4656593912 | 31.1446377218 | 667 | 152650 | -95.36 | 2.99 | 79.94 | 0.02 | 1.69 | 906 |
| 2024-09-20 22:21:40.327 | MS1 | 121.4656755960 | 31.1446243994 | 707 | 152650 | -90.95 | 5.09 | 65.96 | 0.14 | 2.21 | 1572 |
| 2024-09-20 22:21:41.834 | MS1 | 121.4656731969 | 31.1446355446 | 783 | 152650 | -90.00 | 7.26 | 72.77 | 0.19 | 2.05 | 1586 |
| 2024-09-20 22:21:42.265 | MS1 | 121.4656695896 | 31.1446280219 | 411 | 152650 | -93.21 | 5.26 | 59.79 | 0.10 | 2.89 | 1566 |

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
| 3210066 | 5 | 121.4699411660 | 31.1559041810 | 159 | 2 | 6 | 10.8 | TDD | 784 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3210202 | 13 | 121.4683482888 | 31.1523830891 | 163 | 12 | 2 | 29.2 | FDD | 667 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3230158 | 7 | 121.4682123480 | 31.1557885511 | 296 | 5 | 3 | 1.6 | FDD | 707 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3248418 | 4 | 121.4714942471 | 31.1446693114 | 321 | 3 | 12 | 1.0 | TDD | 685 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3249221 | 3 | 121.4643535137 | 31.1547212689 | 213 | 1 | 1 | 13.6 | TDD | 236 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3250745 | 9 | 121.4737953962 | 31.1532363709 | 359 | 13 | 0 | 16.9 | FDD | 624 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3252857 | 1 | 121.4679708676 | 31.1495418324 | 220 | 12 | 3 | 26.7 | TDD | 802 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3260319 | 2 | 121.4757074682 | 31.1552803444 | 188 | 8 | 11 | 27.1 | TDD | 134 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3269527 | 11 | 121.4733183024 | 31.1536421458 | 243 | 9 | 0 | 10.1 | FDD | 470 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3270143 | 8 | 121.4647186835 | 31.1502520292 | 50 | 15 | 4 | 6.7 | FDD | 783 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3271980 | 10 | 121.4735794100 | 31.1549869624 | 44 | 5 | 8 | 26.4 | FDD | 308 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3275609 | 12 | 121.4743013389 | 31.1458689459 | 88 | 6 | 7 | 19.6 | FDD | 411 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3276828 | 6 | 121.4691305428 | 31.1511812609 | 161 | 2 | 1 | 18.0 | TDD | 732 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.633 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.649 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.751 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.751 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.460 | NREventA2 | measId:1;ServCellPCI:710;Se... |
| 2024-09-20 22:21:35.605 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.892 | NREventA5 | measId:3;ServCellPCI:710;Se... |
| 2024-09-20 22:21:35.969 | NRHandoverAttempt | SourcePCI:710;SourceNR-ARFC... |
| 2024-09-20 22:21:36.014 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.029 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.150 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.150 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252857 | 1 | 14.3081 | 16.8351 | -114.0944 | 11.9531 | 87.3012 | 0.0050 | 0.0089 |
| 2024_09_20 22:00 | 3260319 | 2 | 15.6915 | 5.0922 | -114.2447 | 11.9408 | 115.3636 | 0.0162 | 0.0098 |
| 2024_09_20 22:00 | 3249221 | 3 | 18.8603 | 19.9725 | -115.5133 | 7.9658 | 116.7976 | 0.0132 | 0.0127 |
| 2024_09_20 22:00 | 3248418 | 4 | 12.6488 | 18.4520 | -114.3248 | 19.7025 | 188.3123 | 0.0079 | 0.0129 |
| 2024_09_20 22:00 | 3210066 | 5 | 17.2034 | 9.2701 | -115.3194 | 18.5344 | 180.9824 | 0.0042 | 0.0090 |
| 2024_09_20 22:00 | 3276828 | 6 | 8.5540 | 10.2271 | -115.2457 | 19.9078 | 133.4174 | 0.0188 | 0.0189 |
| 2024_09_20 22:00 | 3230158 | 7 | 15.1178 | 17.2034 | -117.6030 | 4.2420 | 43.1445 | 0.0169 | 0.0177 |
| 2024_09_20 22:00 | 3270143 | 8 | 11.1036 | 5.0756 | -114.0453 | 3.3422 | 21.8863 | 0.0050 | 0.0068 |
| 2024_09_20 22:00 | 3250745 | 9 | 13.2487 | 8.6147 | -115.6350 | 3.2011 | 49.9316 | 0.0107 | 0.0074 |
| 2024_09_20 22:00 | 3271980 | 10 | 9.3575 | 14.6705 | -114.4754 | 4.9690 | 53.7075 | 0.0002 | 0.0036 |
| 2024_09_20 22:00 | 3269527 | 11 | 14.4479 | 15.0024 | -114.7259 | 3.2867 | 43.6715 | 0.0021 | 0.0088 |
| 2024_09_20 22:00 | 3275609 | 12 | 11.4506 | 14.8932 | -117.6088 | 3.0699 | 20.2172 | 0.0018 | 0.0059 |
| 2024_09_20 22:00 | 3210202 | 13 | 8.4308 | 11.6280 | -116.7864 | 3.6345 | 26.3007 | 0.0098 | 0.0173 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416704_012AD3F0 | 504990 | 236 | -93.8 | 504990 | 784 | -97.8 | 504990 | 134 | -97.4 | 504990 | 802 |
| MR_1774416704_2887FAF4 | 152650 | 411 | -89.4 | 152650 | 308 | -92.6 | 152650 | 624 | -97.3 | 152650 | 470 |
| MR_1774416704_8294DFA2 | 152650 | 411 | -87.8 | 152650 | 308 | -94.1 | 152650 | 624 | -94.0 | 152650 | 470 |
| MR_1774416704_11B832B9 | 504990 | 236 | -93.5 | 504990 | 784 | -95.4 | 504990 | 134 | -96.2 | 504990 | 802 |
| MR_1774416704_1542AE27 | 504990 | 236 | -92.8 | 504990 | 784 | -94.8 | 504990 | 134 | -98.0 | 504990 | 802 |
| MR_1774416704_4CDF54AB | 152650 | 411 | -89.3 | 152650 | 308 | -95.1 | 152650 | 624 | -95.9 | 152650 | 470 |
| MR_1774416704_F17A7B0E | 504990 | 236 | -94.8 | 504990 | 784 | -94.5 | 504990 | 134 | -95.6 | 504990 | 802 |
| MR_1774416704_FD30EE16 | 504990 | 236 | -92.9 | 504990 | 784 | -95.3 | 504990 | 134 | -94.6 | 504990 | 802 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1139: `e3f2b933-117...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e3f2b933-1175-49b0-983d-3cf38aa46f6d` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Decrease A3 Offset threshold for 3233921_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1139] topology](images/train_1139.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3231251_2
- `C2`: Press down the tilt angle  of 3231251_2 by 10 degrees
- `C3`: Increase transmission power for 3231251_2
- `C4`: Lift the tilt angle  of 3231251_2 by 10 degrees
- `C5`: Decrease A3 Offset threshold for 3231251_2
- `C6`: Add neighbor relationship between 3233921_1 and 3231251_2
- `C7`: Increase A3 Offset threshold for 3233921_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233921_1
- `C9`: Lift the tilt angle of 3233921_1 by 10 degrees
- `C10`: Increase transmission power for 3233921_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231251_2
- `C12`: Decrease transmission power for 3231251_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233921_1
- `C14`: Adjust the azimuth of 3233921_1 by 50 degrees
- `C15`: Check test server and transmission issues
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Adjust the azimuth of 3231251_2 by 50 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231251_2
- `C19`: Decrease A3 Offset threshold for 3233921_1 **← 정답**
- `C20`: Add neighbor relationship between 3214840_3 and 3231251_2
- `C21`: Press down the tilt angle of 3233921_1 by 10 degrees
- `C22`: Decrease transmission power for 3233921_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.968 | MS1 | 121.4656662572 | 31.1446285850 | 903 | 504990 | -82.81 | 13.86 | 585.60 | 0.08 | 2.90 | 1595 |
| 2024-09-20 22:21:32.549 | MS1 | 121.4656600056 | 31.1446190724 | 903 | 504990 | -83.43 | 17.91 | 308.65 | 0.05 | 2.70 | 1567 |
| 2024-09-20 22:21:33.177 | MS1 | 121.4656652606 | 31.1446252984 | 903 | 504990 | -79.31 | 13.82 | 447.47 | 0.00 | 2.45 | 1599 |
| 2024-09-20 22:21:34.335 | MS1 | 121.4656608285 | 31.1446338540 | 903 | 504990 | -84.40 | -1.82 | 34.97 | 0.16 | 1.26 | 1586 |
| 2024-09-20 22:21:35.841 | MS1 | 121.4656695614 | 31.1446293644 | 903 | 504990 | -90.24 | -0.28 | 61.31 | 0.04 | 1.04 | 1561 |
| 2024-09-20 22:21:36.234 | MS1 | 121.4656676269 | 31.1446321363 | 903 | 504990 | -90.39 | -2.39 | 30.47 | 0.13 | 1.49 | 1582 |
| 2024-09-20 22:21:37.977 | MS1 | 121.4656622827 | 31.1446269436 | 903 | 504990 | -86.25 | -2.47 | 47.63 | 0.13 | 1.06 | 1564 |
| 2024-09-20 22:21:38.631 | MS1 | 121.4656604534 | 31.1446231552 | 903 | 504990 | -91.53 | -0.46 | 67.90 | 0.08 | 1.23 | 1577 |
| 2024-09-20 22:21:39.211 | MS1 | 121.4656639077 | 31.1446323794 | 921 | 504990 | -79.97 | 14.51 | 171.97 | 0.06 | 1.43 | 1587 |
| 2024-09-20 22:21:40.627 | MS1 | 121.4656738418 | 31.1446242957 | 921 | 504990 | -83.05 | 16.61 | 419.03 | 0.05 | 2.17 | 1569 |
| 2024-09-20 22:21:41.858 | MS1 | 121.4656752648 | 31.1446280102 | 921 | 504990 | -77.67 | 16.67 | 309.38 | 0.02 | 2.55 | 1591 |
| 2024-09-20 22:21:42.699 | MS1 | 121.4656764593 | 31.1446276799 | 921 | 504990 | -75.31 | 15.11 | 520.75 | 0.06 | 2.93 | 1569 |

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
| 3214840 | 3 | 121.4738218758 | 31.1512372830 | 86 | 9 | 11 | 43.8 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3231251 | 2 | 121.4735461157 | 31.1527741364 | 9 | 15 | 0 | 27.0 | TDD | 921 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3233921 | 1 | 121.4745637920 | 31.1544538766 | 269 | 13 | 5 | 21.5 | TDD | 903 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3246083 | 4 | 121.4728974089 | 31.1552119746 | 357 | 4 | 7 | 39.7 | TDD | 983 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.392 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.410 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.520 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.520 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.247 | NREventA3 | measId:2;ServCellPCI:816;Se... |
| 2024-09-20 22:21:38.487 | NRHandoverAttempt | SourcePCI:816;SourceNR-ARFC... |
| 2024-09-20 22:21:38.527 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.538 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.663 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.663 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233921 | 1 | 18.1775 | 5.2253 | -114.1690 | 5.3353 | 80.5672 | 0.0143 | 0.1223 |
| 2024_09_20 22:00 | 3231251 | 2 | 13.4057 | 5.8339 | -114.7046 | 19.6069 | 93.6132 | 0.0092 | 0.0165 |
| 2024_09_20 22:00 | 3214840 | 3 | 8.1212 | 17.8161 | -116.4900 | 11.6754 | 86.9554 | 0.0096 | 0.0004 |
| 2024_09_20 22:00 | 3246083 | 4 | 12.8835 | 6.6425 | -115.2725 | 16.1988 | 176.0922 | 0.0089 | 0.0198 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415902_F5B191FC | 504990 | 903 | -84.0 | 504990 | 921 | -79.5 | 504990 | 382 | -81.8 | 504990 | 983 |
| MR_1774415902_52329194 | 504990 | 903 | -84.8 | 504990 | 921 | -77.5 | 504990 | 382 | -79.7 | 504990 | 983 |
| MR_1774415902_163F8BB8 | 504990 | 903 | -84.1 | 504990 | 921 | -81.2 | 504990 | 382 | -79.2 | 504990 | 983 |
| MR_1774415902_B861FE28 | 504990 | 921 | -80.6 | 504990 | 903 | -83.4 | 504990 | 382 | -78.6 | 504990 | 983 |
| MR_1774415902_B7E8380E | 504990 | 903 | -85.1 | 504990 | 921 | -80.4 | 504990 | 382 | -81.0 | 504990 | 983 |
| MR_1774415902_C8AE7E9D | 504990 | 921 | -80.9 | 504990 | 903 | -82.4 | 504990 | 382 | -79.9 | 504990 | 983 |

> *... 2개 열 생략 (전체 14열)*

---
