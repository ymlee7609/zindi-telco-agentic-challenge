# Track A 문제 분석 — train[1410]~train[1419]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1410] ~ train[1419] (10개)

## 목차

1. [문제 1410: `97608600-1f8...`](#1410) — single-answer, 정답: C6
2. [문제 1411: `28661530-508...`](#1411) — single-answer, 정답: C6
3. [문제 1412: `3f5f9cee-2b0...`](#1412) — single-answer, 정답: C14
4. [문제 1413: `f82e1c6f-770...`](#1413) — single-answer, 정답: C14
5. [문제 1414: `c8886e40-347...`](#1414) — single-answer, 정답: C22
6. [문제 1415: `86a17c4c-891...`](#1415) — single-answer, 정답: C19
7. [문제 1416: `42417230-3be...`](#1416) — multiple-answer, 정답: C16|C22
8. [문제 1417: `c5d2a2dd-8cc...`](#1417) — single-answer, 정답: C20
9. [문제 1418: `73474dfb-698...`](#1418) — multiple-answer, 정답: C1|C15
10. [문제 1419: `24b6b687-93e...`](#1419) — single-answer, 정답: C1

---

### 문제 1410: `97608600-1f8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `97608600-1f82-41af-92d3-33f4860d876d` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Add neighbor relationship between 3217965_3 and 3233533_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1410] topology](images/train_1410.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3233533_4 by 21 degrees
- `C2`: Increase A3 Offset threshold for 3233533_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233533_4
- `C4`: Decrease transmission power for 3217965_3
- `C5`: Add neighbor relationship between 3244894_1 and 3233533_4
- `C6`: Add neighbor relationship between 3217965_3 and 3233533_4 **← 정답**
- `C7`: Increase transmission power for 3217965_3
- `C8`: Check test server and transmission issues
- `C9`: Press down the tilt angle  of 3233533_4 by 5 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217965_3
- `C11`: Lift the tilt angle  of 3233533_4 by 5 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Increase A3 Offset threshold for 3217965_3
- `C14`: Decrease A3 Offset threshold for 3217965_3
- `C15`: Increase transmission power for 3233533_4
- `C16`: Decrease transmission power for 3233533_4
- `C17`: Decrease A3 Offset threshold for 3233533_4
- `C18`: Lift the tilt angle of 3217965_3 by 10 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233533_4
- `C20`: Press down the tilt angle of 3217965_3 by 10 degrees
- `C21`: Adjust the azimuth of 3217965_3 by 50 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217965_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.465 | MS1 | 121.4656768673 | 31.1446228018 | 694 | 504990 | -81.29 | 16.77 | 581.18 | 0.15 | 2.14 | 1582 |
| 2024-09-20 22:21:32.828 | MS1 | 121.4656676467 | 31.1446224608 | 694 | 504990 | -79.10 | 15.07 | 394.12 | 0.08 | 2.51 | 1562 |
| 2024-09-20 22:21:33.469 | MS1 | 121.4656753366 | 31.1446308027 | 694 | 504990 | -80.28 | 16.00 | 364.13 | 0.13 | 2.95 | 1584 |
| 2024-09-20 22:21:34.220 | MS1 | 121.4656607126 | 31.1446218511 | 694 | 504990 | -85.39 | -3.84 | 53.50 | 0.01 | 1.21 | 1569 |
| 2024-09-20 22:21:35.788 | MS1 | 121.4656727609 | 31.1446328962 | 694 | 504990 | -89.11 | -1.92 | 51.93 | 0.08 | 1.44 | 1599 |
| 2024-09-20 22:21:36.577 | MS1 | 121.4656754565 | 31.1446310752 | 694 | 504990 | -92.29 | -0.03 | 46.62 | 0.07 | 1.25 | 1599 |
| 2024-09-20 22:21:37.745 | MS1 | 121.4656636429 | 31.1446204137 | 694 | 504990 | -87.45 | -3.77 | 34.76 | 0.10 | 1.10 | 1590 |
| 2024-09-20 22:21:38.651 | MS1 | 121.4656746618 | 31.1446277096 | 694 | 504990 | -80.66 | 14.06 | 520.20 | 0.07 | 1.06 | 1598 |
| 2024-09-20 22:21:39.267 | MS1 | 121.4656685078 | 31.1446234289 | 694 | 504990 | -78.93 | 12.83 | 315.08 | 0.05 | 1.14 | 1581 |
| 2024-09-20 22:21:40.986 | MS1 | 121.4656620907 | 31.1446327378 | 694 | 504990 | -79.56 | 14.91 | 300.75 | 0.13 | 2.94 | 1568 |
| 2024-09-20 22:21:41.634 | MS1 | 121.4656708056 | 31.1446199568 | 694 | 504990 | -80.30 | 16.42 | 535.40 | 0.06 | 2.07 | 1595 |
| 2024-09-20 22:21:42.427 | MS1 | 121.4656737586 | 31.1446280289 | 694 | 504990 | -81.81 | 16.00 | 402.56 | 0.18 | 2.74 | 1595 |

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
| 3217965 | 3 | 121.4651780295 | 31.1480274707 | 237 | 7 | 2 | 23.4 | TDD | 694 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3233533 | 4 | 121.4716135326 | 31.1448145414 | 289 | 0 | 2 | 48.3 | TDD | 879 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3244894 | 1 | 121.4745089984 | 31.1506679284 | 48 | 11 | 6 | 40.2 | TDD | 170 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3247826 | 2 | 121.4664602676 | 31.1545008183 | 183 | 10 | 9 | 17.8 | TDD | 188 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.566 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.584 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.726 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.726 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.418 | NREventA3 | measId:2;ServCellPCI:992;Se... |
| 2024-09-20 22:21:36.418 | NREventA3 | measId:2;ServCellPCI:992;Se... |
| 2024-09-20 22:21:37.418 | NREventA3 | measId:2;ServCellPCI:992;Se... |
| 2024-09-20 22:21:39.918 | NRRRCReestablishAttempt | PCI:992 |
| 2024-09-20 22:21:39.936 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.949 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:40.086 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.086 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244894 | 1 | 10.4826 | 8.1272 | -117.2091 | 5.0887 | 169.0630 | 0.0149 | 0.0023 |
| 2024_09_20 22:00 | 3247826 | 2 | 8.3999 | 14.7118 | -114.8607 | 7.9358 | 159.9045 | 0.0121 | 0.0175 |
| 2024_09_20 22:00 | 3217965 | 3 | 8.1349 | 18.5352 | -115.2691 | 12.3679 | 183.5615 | 0.0127 | 0.1418 |
| 2024_09_20 22:00 | 3233533 | 4 | 6.2395 | 17.6943 | -116.4561 | 17.5958 | 146.5577 | 0.0131 | 0.0073 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414558_528D2270 | 504990 | 694 | -84.3 | 504990 | 879 | -81.9 | 504990 | 170 | -90.6 | 504990 | 188 |
| MR_1774414558_77F15996 | 504990 | 694 | -84.4 | 504990 | 879 | -79.6 | 504990 | 170 | -89.7 | 504990 | 188 |
| MR_1774414558_6965070C | 504990 | 694 | -87.3 | 504990 | 879 | -81.0 | 504990 | 170 | -90.1 | 504990 | 188 |
| MR_1774414558_C87AC6BA | 504990 | 879 | -78.7 | 504990 | 694 | -83.8 | 504990 | 170 | -90.6 | 504990 | 188 |
| MR_1774414558_F8F047F6 | 504990 | 694 | -85.3 | 504990 | 879 | -81.0 | 504990 | 170 | -90.9 | 504990 | 188 |
| MR_1774414558_C70344B0 | 504990 | 879 | -78.2 | 504990 | 694 | -83.7 | 504990 | 170 | -91.3 | 504990 | 188 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1411: `28661530-508...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `28661530-508e-46c7-8618-2a792fb8829e` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Add neighbor relationship between 3265658_4 and 3277020_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1411] topology](images/train_1411.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265658_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277020_2
- `C3`: Lift the tilt angle  of 3277020_2 by 3 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277020_2
- `C5`: Increase transmission power for 3277020_2
- `C6`: Add neighbor relationship between 3265658_4 and 3277020_2 **← 정답**
- `C7`: Increase transmission power for 3265658_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265658_4
- `C9`: Add neighbor relationship between 3255421_3 and 3277020_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Lift the tilt angle of 3265658_4 by 3 degrees
- `C12`: Check test server and transmission issues
- `C13`: Decrease A3 Offset threshold for 3277020_2
- `C14`: Decrease A3 Offset threshold for 3265658_4
- `C15`: Adjust the azimuth of 3277020_2 by 12 degrees
- `C16`: Adjust the azimuth of 3265658_4 by 50 degrees
- `C17`: Increase A3 Offset threshold for 3265658_4
- `C18`: Increase A3 Offset threshold for 3277020_2
- `C19`: Decrease transmission power for 3265658_4
- `C20`: Press down the tilt angle  of 3277020_2 by 3 degrees
- `C21`: Decrease transmission power for 3277020_2
- `C22`: Press down the tilt angle of 3265658_4 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.161 | MS1 | 121.4656765609 | 31.1446183975 | 799 | 504990 | -82.78 | 13.73 | 330.92 | 0.14 | 2.87 | 1590 |
| 2024-09-20 22:21:32.958 | MS1 | 121.4656708702 | 31.1446354314 | 799 | 504990 | -76.81 | 15.55 | 579.40 | 0.07 | 2.47 | 1590 |
| 2024-09-20 22:21:33.569 | MS1 | 121.4656585632 | 31.1446249001 | 799 | 504990 | -84.34 | 14.82 | 377.57 | 0.12 | 2.12 | 1588 |
| 2024-09-20 22:21:34.253 | MS1 | 121.4656603409 | 31.1446333165 | 799 | 504990 | -94.29 | -2.48 | 53.89 | 0.18 | 1.33 | 1596 |
| 2024-09-20 22:21:35.669 | MS1 | 121.4656721991 | 31.1446333391 | 799 | 504990 | -89.75 | -0.04 | 61.98 | 0.14 | 1.27 | 1599 |
| 2024-09-20 22:21:36.289 | MS1 | 121.4656673758 | 31.1446263879 | 799 | 504990 | -92.55 | -2.71 | 54.78 | 0.18 | 1.14 | 1570 |
| 2024-09-20 22:21:37.694 | MS1 | 121.4656673839 | 31.1446317186 | 799 | 504990 | -89.45 | -1.39 | 46.39 | 0.11 | 1.06 | 1582 |
| 2024-09-20 22:21:38.575 | MS1 | 121.4656725176 | 31.1446269996 | 799 | 504990 | -79.11 | 16.46 | 519.67 | 0.17 | 1.02 | 1587 |
| 2024-09-20 22:21:39.233 | MS1 | 121.4656646284 | 31.1446193508 | 799 | 504990 | -82.35 | 12.19 | 346.43 | 0.12 | 1.18 | 1590 |
| 2024-09-20 22:21:40.989 | MS1 | 121.4656640906 | 31.1446214708 | 799 | 504990 | -78.11 | 12.29 | 385.79 | 0.15 | 2.00 | 1582 |
| 2024-09-20 22:21:41.959 | MS1 | 121.4656646060 | 31.1446205843 | 799 | 504990 | -75.72 | 13.34 | 363.80 | 0.14 | 2.82 | 1591 |
| 2024-09-20 22:21:42.592 | MS1 | 121.4656642249 | 31.1446233923 | 799 | 504990 | -78.67 | 16.03 | 480.05 | 0.17 | 2.54 | 1594 |

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
| 3254464 | 1 | 121.4708430584 | 31.1504323080 | 139 | 6 | 6 | 21.8 | TDD | 448 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3255421 | 3 | 121.4750175434 | 31.1523979391 | 173 | 6 | 8 | 15.6 | TDD | 556 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3265658 | 4 | 121.4684387846 | 31.1476201032 | 120 | 0 | 11 | 18.8 | TDD | 799 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3277020 | 2 | 121.4738729402 | 31.1494305287 | 248 | 2 | 0 | 24.3 | TDD | 812 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.490 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.509 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.630 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.630 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.365 | NREventA3 | measId:2;ServCellPCI:28;Ser... |
| 2024-09-20 22:21:36.365 | NREventA3 | measId:2;ServCellPCI:28;Ser... |
| 2024-09-20 22:21:37.365 | NREventA3 | measId:2;ServCellPCI:28;Ser... |
| 2024-09-20 22:21:39.865 | NRRRCReestablishAttempt | PCI:28 |
| 2024-09-20 22:21:39.882 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.896 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:40.027 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.027 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254464 | 1 | 14.5808 | 17.3493 | -116.6750 | 8.3288 | 168.2936 | 0.0194 | 0.0171 |
| 2024_09_20 22:00 | 3277020 | 2 | 17.3519 | 11.4023 | -115.8939 | 15.8931 | 132.0685 | 0.0127 | 0.0188 |
| 2024_09_20 22:00 | 3255421 | 3 | 11.1205 | 7.0812 | -115.9910 | 12.8608 | 153.1468 | 0.0092 | 0.0008 |
| 2024_09_20 22:00 | 3265658 | 4 | 13.3953 | 7.9432 | -115.2578 | 16.7727 | 157.9994 | 0.0009 | 0.1729 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412557_C15A2044 | 504990 | 799 | -94.5 | 504990 | 812 | -89.5 | 504990 | 556 | -94.2 | 504990 | 448 |
| MR_1774412557_4AE85DD1 | 504990 | 799 | -95.5 | 504990 | 812 | -90.7 | 504990 | 556 | -96.3 | 504990 | 448 |
| MR_1774412557_AA23F420 | 504990 | 799 | -95.8 | 504990 | 812 | -88.6 | 504990 | 556 | -95.1 | 504990 | 448 |
| MR_1774412557_2B5D0C12 | 504990 | 812 | -91.5 | 504990 | 799 | -93.5 | 504990 | 556 | -94.2 | 504990 | 448 |
| MR_1774412557_85F6A4C3 | 504990 | 799 | -92.4 | 504990 | 812 | -88.7 | 504990 | 556 | -96.4 | 504990 | 448 |
| MR_1774412557_4FF4531F | 504990 | 799 | -93.1 | 504990 | 812 | -88.8 | 504990 | 556 | -94.6 | 504990 | 448 |
| MR_1774412557_D34C9FC8 | 504990 | 799 | -93.2 | 504990 | 812 | -88.3 | 504990 | 556 | -95.3 | 504990 | 448 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1412: `3f5f9cee-2b0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3f5f9cee-2b04-4899-a977-eedaf5508789` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Add neighbor relationship between 3277353_1 and 3234680_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1412] topology](images/train_1412.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3277353_1 by 50 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277353_1
- `C3`: Decrease A3 Offset threshold for 3234680_2
- `C4`: Decrease transmission power for 3234680_2
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase A3 Offset threshold for 3277353_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277353_1
- `C8`: Decrease A3 Offset threshold for 3277353_1
- `C9`: Lift the tilt angle of 3277353_1 by 10 degrees
- `C10`: Lift the tilt angle  of 3234680_2 by 5 degrees
- `C11`: Press down the tilt angle  of 3234680_2 by 5 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234680_2
- `C13`: Increase A3 Offset threshold for 3234680_2
- `C14`: Add neighbor relationship between 3277353_1 and 3234680_2 **← 정답**
- `C15`: Add neighbor relationship between 3214811_3 and 3234680_2
- `C16`: Increase transmission power for 3234680_2
- `C17`: Press down the tilt angle of 3277353_1 by 10 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234680_2
- `C19`: Increase transmission power for 3277353_1
- `C20`: Adjust the azimuth of 3234680_2 by 34 degrees
- `C21`: Check test server and transmission issues
- `C22`: Decrease transmission power for 3277353_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.940 | MS1 | 121.4656661295 | 31.1446337969 | 619 | 504990 | -79.35 | 15.81 | 313.91 | 0.07 | 2.11 | 1581 |
| 2024-09-20 22:21:32.873 | MS1 | 121.4656762409 | 31.1446341048 | 619 | 504990 | -76.75 | 17.40 | 427.06 | 0.01 | 2.63 | 1593 |
| 2024-09-20 22:21:33.699 | MS1 | 121.4656602670 | 31.1446224784 | 619 | 504990 | -79.12 | 14.05 | 488.61 | 0.11 | 2.39 | 1565 |
| 2024-09-20 22:21:34.557 | MS1 | 121.4656630288 | 31.1446340520 | 619 | 504990 | -91.48 | -2.72 | 58.51 | 0.12 | 1.16 | 1562 |
| 2024-09-20 22:21:35.398 | MS1 | 121.4656619670 | 31.1446345892 | 619 | 504990 | -93.39 | -3.40 | 28.14 | 0.07 | 1.24 | 1586 |
| 2024-09-20 22:21:36.269 | MS1 | 121.4656667889 | 31.1446350925 | 619 | 504990 | -87.46 | -3.33 | 21.08 | 0.12 | 1.00 | 1577 |
| 2024-09-20 22:21:37.975 | MS1 | 121.4656737475 | 31.1446225112 | 619 | 504990 | -91.24 | -3.67 | 60.05 | 0.16 | 1.50 | 1573 |
| 2024-09-20 22:21:38.668 | MS1 | 121.4656740918 | 31.1446328060 | 619 | 504990 | -79.55 | 17.81 | 471.79 | 0.03 | 1.11 | 1562 |
| 2024-09-20 22:21:39.677 | MS1 | 121.4656719011 | 31.1446267491 | 619 | 504990 | -76.58 | 13.58 | 519.59 | 0.02 | 1.27 | 1568 |
| 2024-09-20 22:21:40.427 | MS1 | 121.4656752707 | 31.1446223114 | 619 | 504990 | -80.15 | 17.01 | 443.46 | 0.11 | 2.28 | 1588 |
| 2024-09-20 22:21:41.726 | MS1 | 121.4656601594 | 31.1446242407 | 619 | 504990 | -75.88 | 13.85 | 510.10 | 0.19 | 2.77 | 1566 |
| 2024-09-20 22:21:42.778 | MS1 | 121.4656687980 | 31.1446265114 | 619 | 504990 | -77.02 | 17.57 | 574.50 | 0.04 | 2.28 | 1568 |

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
| 3214811 | 3 | 121.4691801177 | 31.1534741851 | 240 | 12 | 8 | 44.1 | TDD | 726 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3227079 | 4 | 121.4707380829 | 31.1464838752 | 257 | 11 | 12 | 46.4 | TDD | 526 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3234680 | 2 | 121.4656117863 | 31.1542135091 | 214 | 2 | 2 | 49.1 | TDD | 381 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3277353 | 1 | 121.4723048219 | 31.1442842680 | 153 | 13 | 10 | 19.9 | TDD | 619 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.301 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.326 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.451 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.451 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.189 | NREventA3 | measId:2;ServCellPCI:427;Se... |
| 2024-09-20 22:21:36.189 | NREventA3 | measId:2;ServCellPCI:427;Se... |
| 2024-09-20 22:21:37.189 | NREventA3 | measId:2;ServCellPCI:427;Se... |
| 2024-09-20 22:21:39.689 | NRRRCReestablishAttempt | PCI:427 |
| 2024-09-20 22:21:39.707 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.718 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.851 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.851 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277353 | 1 | 11.1937 | 14.9782 | -115.7872 | 13.5861 | 161.3545 | 0.0068 | 0.1300 |
| 2024_09_20 22:00 | 3234680 | 2 | 10.3081 | 14.0540 | -116.3926 | 16.5551 | 122.4663 | 0.0026 | 0.0067 |
| 2024_09_20 22:00 | 3214811 | 3 | 16.3279 | 11.7422 | -114.2981 | 15.9635 | 118.8325 | 0.0040 | 0.0195 |
| 2024_09_20 22:00 | 3227079 | 4 | 15.5601 | 15.7739 | -117.1756 | 7.4552 | 134.5402 | 0.0024 | 0.0185 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415199_FF9C1781 | 504990 | 619 | -89.7 | 504990 | 381 | -86.9 | 504990 | 726 | -95.3 | 504990 | 526 |
| MR_1774415199_11B0D47F | 504990 | 619 | -93.0 | 504990 | 381 | -83.8 | 504990 | 726 | -98.0 | 504990 | 526 |
| MR_1774415199_91B22349 | 504990 | 619 | -89.6 | 504990 | 381 | -84.5 | 504990 | 726 | -97.2 | 504990 | 526 |
| MR_1774415199_44821965 | 504990 | 619 | -89.6 | 504990 | 381 | -84.6 | 504990 | 726 | -94.8 | 504990 | 526 |
| MR_1774415199_A9554172 | 504990 | 619 | -89.6 | 504990 | 381 | -84.7 | 504990 | 726 | -95.9 | 504990 | 526 |
| MR_1774415199_F10C9BE8 | 504990 | 381 | -86.8 | 504990 | 619 | -90.7 | 504990 | 726 | -97.4 | 504990 | 526 |
| MR_1774415199_383B7EBB | 504990 | 619 | -91.6 | 504990 | 381 | -85.6 | 504990 | 726 | -95.6 | 504990 | 526 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1413: `f82e1c6f-770...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f82e1c6f-7700-4c49-a051-3b4a59465413` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1413] topology](images/train_1413.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3213324_2
- `C2`: Add neighbor relationship between 3213324_2 and 3214698_3
- `C3`: Check test server and transmission issues
- `C4`: Lift the tilt angle  of 3214698_3 by 4 degrees
- `C5`: Increase transmission power for 3213324_2
- `C6`: Increase transmission power for 3214698_3
- `C7`: Adjust the azimuth of 3214698_3 by 50 degrees
- `C8`: Decrease transmission power for 3213324_2
- `C9`: Press down the tilt angle of 3213324_2 by 6 degrees
- `C10`: Increase A3 Offset threshold for 3214698_3
- `C11`: Add neighbor relationship between 3253870_4 and 3214698_3
- `C12`: Decrease A3 Offset threshold for 3213324_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213324_2
- `C14`: Insufficient data; more data is needed for judgment. **← 정답**
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214698_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214698_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213324_2
- `C18`: Adjust the azimuth of 3213324_2 by 50 degrees
- `C19`: Decrease transmission power for 3214698_3
- `C20`: Decrease A3 Offset threshold for 3214698_3
- `C21`: Press down the tilt angle  of 3214698_3 by 4 degrees
- `C22`: Lift the tilt angle of 3213324_2 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.528 | MS1 | 121.4656752740 | 31.1446211461 | 236 | 504990 | -86.62 | 14.87 | 525.31 | 0.12 | 2.20 | 1591 |
| 2024-09-20 22:21:32.405 | MS1 | 121.4656611902 | 31.1446218391 | 236 | 504990 | -88.33 | 12.23 | 343.18 | 0.17 | 2.49 | 1590 |
| 2024-09-20 22:21:33.999 | MS1 | 121.4656746724 | 31.1446352743 | 236 | 504990 | -88.52 | 12.36 | 449.70 | 0.03 | 2.83 | 1562 |
| 2024-09-20 22:21:34.574 | MS1 | 121.4656766060 | 31.1446245524 | 236 | 504990 | -91.27 | 17.09 | 58.27 | 0.00 | 2.27 | 1572 |
| 2024-09-20 22:21:35.392 | MS1 | 121.4656715197 | 31.1446260197 | 236 | 504990 | -87.59 | 16.57 | 54.16 | 0.11 | 2.42 | 1588 |
| 2024-09-20 22:21:36.280 | MS1 | 121.4656712902 | 31.1446274598 | 236 | 504990 | -88.47 | 12.67 | 59.73 | 0.09 | 2.60 | 1592 |
| 2024-09-20 22:21:37.682 | MS1 | 121.4656716151 | 31.1446180229 | 236 | 504990 | -91.17 | 9.86 | 70.29 | 0.12 | 2.37 | 1579 |
| 2024-09-20 22:21:38.454 | MS1 | 121.4656755741 | 31.1446332217 | 236 | 504990 | -90.58 | 12.39 | 83.16 | 0.02 | 2.74 | 1571 |
| 2024-09-20 22:21:39.577 | MS1 | 121.4656597556 | 31.1446199299 | 236 | 504990 | -90.14 | 9.84 | 66.62 | 0.08 | 2.62 | 1600 |
| 2024-09-20 22:21:40.946 | MS1 | 121.4656722604 | 31.1446264091 | 236 | 504990 | -91.22 | 8.08 | 468.10 | 0.13 | 2.50 | 1589 |
| 2024-09-20 22:21:41.882 | MS1 | 121.4656604849 | 31.1446243630 | 236 | 504990 | -90.78 | 12.52 | 379.68 | 0.16 | 2.65 | 1580 |
| 2024-09-20 22:21:42.857 | MS1 | 121.4656655759 | 31.1446276041 | 236 | 504990 | -91.89 | 10.19 | 487.41 | 0.00 | 2.74 | 1560 |

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
| 3213324 | 2 | 121.4649655369 | 31.1532594098 | 6 | 3 | 8 | 46.3 | TDD | 236 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3214698 | 3 | 121.4733260034 | 31.1557805878 | 73 | 3 | 5 | 25.4 | TDD | 348 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3220132 | 1 | 121.4682726688 | 31.1489388504 | 105 | 3 | 1 | 23.0 | TDD | 145 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3253870 | 4 | 121.4746979766 | 31.1524083887 | 223 | 15 | 5 | 22.4 | TDD | 79 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.840 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.855 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.983 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.983 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.652 | NREventA3 | measId:2;ServCellPCI:762;Se... |
| 2024-09-20 22:21:37.892 | NRHandoverAttempt | SourcePCI:762;SourceNR-ARFC... |
| 2024-09-20 22:21:37.929 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.939 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.050 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.050 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3220132 | 1 | 83.6467 | 84.6025 | -116.6021 | 8.7929 | 190.2780 | 0.0088 | 0.0102 |
| 2024_09_19 22:00 | 3213324 | 2 | 82.2410 | 80.3672 | -115.3642 | 8.9911 | 137.0728 | 0.0025 | 0.0119 |
| 2024_09_19 22:00 | 3214698 | 3 | 78.8323 | 81.9163 | -114.9522 | 14.0290 | 109.9981 | 0.0156 | 0.0025 |
| 2024_09_19 22:00 | 3253870 | 4 | 92.9473 | 79.1517 | -114.6206 | 19.1930 | 133.6328 | 0.0200 | 0.0180 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413661_0B22C1DA | 504990 | 236 | -89.6 | 504990 | 348 | -100.2 | 504990 | 79 | -102.3 | 504990 | 145 |
| MR_1774413661_68DEED66 | 504990 | 236 | -93.2 | 504990 | 348 | -99.9 | 504990 | 79 | -103.6 | 504990 | 145 |
| MR_1774413661_E96B1DB1 | 504990 | 236 | -91.6 | 504990 | 348 | -98.0 | 504990 | 79 | -102.7 | 504990 | 145 |
| MR_1774413661_498CDCF9 | 504990 | 236 | -89.6 | 504990 | 348 | -98.5 | 504990 | 79 | -105.3 | 504990 | 145 |
| MR_1774413661_0E71FDB3 | 504990 | 236 | -89.7 | 504990 | 348 | -101.4 | 504990 | 79 | -103.1 | 504990 | 145 |
| MR_1774413661_7532DB6A | 504990 | 236 | -90.9 | 504990 | 348 | -100.5 | 504990 | 79 | -104.9 | 504990 | 145 |
| MR_1774413661_396BFB06 | 504990 | 236 | -92.7 | 504990 | 348 | -101.6 | 504990 | 79 | -105.5 | 504990 | 145 |
| MR_1774413661_38AC8803 | 504990 | 236 | -90.4 | 504990 | 348 | -97.9 | 504990 | 79 | -104.7 | 504990 | 145 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1414: `c8886e40-347...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c8886e40-3477-444f-afc6-4fee8d71205d` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1414] topology](images/train_1414.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3240204_1 and 3258669_4
- `C2`: Increase A3 Offset threshold for 3258669_4
- `C3`: Lift the tilt angle  of 3258669_4 by 10 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258669_4
- `C5`: Decrease transmission power for 3258669_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258669_4
- `C7`: Decrease A3 Offset threshold for 3253431_3
- `C8`: Adjust the azimuth of 3258669_4 by 50 degrees
- `C9`: Adjust the azimuth of 3253431_3 by 50 degrees
- `C10`: Press down the tilt angle of 3253431_3 by 10 degrees
- `C11`: Increase transmission power for 3253431_3
- `C12`: Press down the tilt angle  of 3258669_4 by 10 degrees
- `C13`: Add neighbor relationship between 3253431_3 and 3258669_4
- `C14`: Lift the tilt angle of 3253431_3 by 10 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Increase A3 Offset threshold for 3253431_3
- `C17`: Increase transmission power for 3258669_4
- `C18`: Decrease transmission power for 3253431_3
- `C19`: Decrease A3 Offset threshold for 3258669_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253431_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253431_3
- `C22`: Check test server and transmission issues **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.149 | MS1 | 121.4656745436 | 31.1446279669 | 230 | 504990 | -87.09 | 12.70 | 559.33 | 0.14 | 2.43 | 1587 |
| 2024-09-20 22:21:32.265 | MS1 | 121.4656651466 | 31.1446212657 | 230 | 504990 | -90.41 | 13.96 | 529.93 | 0.09 | 2.06 | 1571 |
| 2024-09-20 22:21:33.981 | MS1 | 121.4656745221 | 31.1446303910 | 230 | 504990 | -90.86 | 16.67 | 322.55 | 0.15 | 2.71 | 1564 |
| 2024-09-20 22:21:34.724 | MS1 | 121.4656769156 | 31.1446309975 | 230 | 504990 | -90.76 | 15.32 | 83.35 | 0.05 | 2.79 | 321 |
| 2024-09-20 22:21:35.113 | MS1 | 121.4656679458 | 31.1446287218 | 230 | 504990 | -88.00 | 12.12 | 64.90 | 0.15 | 2.63 | 487 |
| 2024-09-20 22:21:36.207 | MS1 | 121.4656666261 | 31.1446377933 | 230 | 504990 | -86.48 | 12.03 | 75.09 | 0.20 | 2.54 | 462 |
| 2024-09-20 22:21:37.861 | MS1 | 121.4656694734 | 31.1446240622 | 230 | 504990 | -93.04 | 12.61 | 85.42 | 0.16 | 2.36 | 319 |
| 2024-09-20 22:21:38.143 | MS1 | 121.4656628809 | 31.1446327583 | 230 | 504990 | -90.50 | 11.53 | 94.76 | 0.10 | 2.33 | 411 |
| 2024-09-20 22:21:39.174 | MS1 | 121.4656647256 | 31.1446182602 | 230 | 504990 | -91.01 | 9.68 | 62.90 | 0.19 | 2.36 | 303 |
| 2024-09-20 22:21:40.421 | MS1 | 121.4656776502 | 31.1446359238 | 230 | 504990 | -92.02 | 7.93 | 417.72 | 0.04 | 2.29 | 1571 |
| 2024-09-20 22:21:41.304 | MS1 | 121.4656754509 | 31.1446235503 | 230 | 504990 | -90.37 | 12.93 | 346.53 | 0.12 | 2.35 | 1576 |
| 2024-09-20 22:21:42.455 | MS1 | 121.4656607097 | 31.1446347660 | 230 | 504990 | -91.92 | 9.40 | 600.01 | 0.12 | 2.32 | 1563 |

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
| 3231426 | 2 | 121.4680428349 | 31.1510936802 | 58 | 5 | 12 | 34.1 | TDD | 691 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3240204 | 1 | 121.4710817261 | 31.1475317036 | 42 | 13 | 10 | 18.2 | TDD | 153 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3253431 | 3 | 121.4749611731 | 31.1452663610 | 146 | 14 | 5 | 44.3 | TDD | 230 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3258669 | 4 | 121.4658472341 | 31.1452457517 | 301 | 13 | 5 | 28.8 | TDD | 742 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.626 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.647 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.754 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.754 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.492 | NREventA3 | measId:2;ServCellPCI:243;Se... |
| 2024-09-20 22:21:38.732 | NRHandoverAttempt | SourcePCI:243;SourceNR-ARFC... |
| 2024-09-20 22:21:38.771 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.784 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.926 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.926 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240204 | 1 | 16.5165 | 10.1338 | -116.9504 | 11.5804 | 157.4742 | 0.0089 | 0.0063 |
| 2024_09_20 22:00 | 3231426 | 2 | 6.0236 | 13.2777 | -117.2542 | 13.7092 | 168.2946 | 0.0074 | 0.0075 |
| 2024_09_20 22:00 | 3253431 | 3 | 9.7736 | 13.0432 | -115.8348 | 7.2212 | 99.4403 | 0.0001 | 0.0041 |
| 2024_09_20 22:00 | 3258669 | 4 | 5.6047 | 10.9315 | -116.9775 | 14.2439 | 170.5491 | 0.0005 | 0.0096 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413707_A828410C | 504990 | 230 | -91.9 | 504990 | 742 | -94.4 | 504990 | 153 | -105.8 | 504990 | 691 |
| MR_1774413707_1869CD54 | 504990 | 230 | -91.2 | 504990 | 742 | -94.8 | 504990 | 153 | -103.1 | 504990 | 691 |
| MR_1774413707_E37311DE | 504990 | 230 | -89.9 | 504990 | 742 | -94.1 | 504990 | 153 | -104.5 | 504990 | 691 |
| MR_1774413707_90068D96 | 504990 | 230 | -90.9 | 504990 | 742 | -95.6 | 504990 | 153 | -106.2 | 504990 | 691 |
| MR_1774413707_9E1A188F | 504990 | 230 | -89.4 | 504990 | 742 | -92.2 | 504990 | 153 | -103.8 | 504990 | 691 |
| MR_1774413707_DF7F9708 | 504990 | 230 | -91.7 | 504990 | 742 | -93.6 | 504990 | 153 | -103.3 | 504990 | 691 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1415: `86a17c4c-891...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `86a17c4c-891d-48ee-84d4-f431a8676db2` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1415] topology](images/train_1415.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3219548_1 by 10 degrees
- `C2`: Press down the tilt angle  of 3219548_1 by 10 degrees
- `C3`: Increase A3 Offset threshold for 3219548_1
- `C4`: Increase A3 Offset threshold for 3233030_2
- `C5`: Decrease A3 Offset threshold for 3233030_2
- `C6`: Increase transmission power for 3219548_1
- `C7`: Add neighbor relationship between 3233030_2 and 3219548_1
- `C8`: Decrease transmission power for 3233030_2
- `C9`: Increase transmission power for 3233030_2
- `C10`: Adjust the azimuth of 3233030_2 by 50 degrees
- `C11`: Decrease A3 Offset threshold for 3219548_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219548_1
- `C13`: Press down the tilt angle of 3233030_2 by 10 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233030_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219548_1
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease transmission power for 3219548_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233030_2
- `C19`: Check test server and transmission issues **← 정답**
- `C20`: Lift the tilt angle of 3233030_2 by 10 degrees
- `C21`: Add neighbor relationship between 3263707_3 and 3219548_1
- `C22`: Adjust the azimuth of 3219548_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.886 | MS1 | 121.4656732646 | 31.1446192282 | 756 | 504990 | -87.86 | 14.59 | 406.85 | 0.17 | 2.95 | 1589 |
| 2024-09-20 22:21:32.448 | MS1 | 121.4656730993 | 31.1446252105 | 756 | 504990 | -90.06 | 14.32 | 513.00 | 0.11 | 2.44 | 1599 |
| 2024-09-20 22:21:33.350 | MS1 | 121.4656750509 | 31.1446232834 | 756 | 504990 | -85.62 | 17.22 | 517.14 | 0.10 | 2.80 | 1580 |
| 2024-09-20 22:21:34.513 | MS1 | 121.4656779053 | 31.1446253429 | 756 | 504990 | -91.97 | 12.80 | 63.45 | 0.07 | 2.79 | 332 |
| 2024-09-20 22:21:35.829 | MS1 | 121.4656740456 | 31.1446370047 | 756 | 504990 | -88.90 | 14.31 | 71.71 | 0.19 | 2.93 | 447 |
| 2024-09-20 22:21:36.111 | MS1 | 121.4656721438 | 31.1446327690 | 756 | 504990 | -85.09 | 17.76 | 62.65 | 0.04 | 2.77 | 338 |
| 2024-09-20 22:21:37.407 | MS1 | 121.4656651868 | 31.1446245410 | 756 | 504990 | -89.19 | 8.03 | 93.52 | 0.11 | 2.98 | 373 |
| 2024-09-20 22:21:38.821 | MS1 | 121.4656733650 | 31.1446285646 | 756 | 504990 | -89.98 | 8.31 | 47.72 | 0.06 | 2.23 | 362 |
| 2024-09-20 22:21:39.925 | MS1 | 121.4656672011 | 31.1446188161 | 756 | 504990 | -89.15 | 12.43 | 89.22 | 0.01 | 2.19 | 492 |
| 2024-09-20 22:21:40.721 | MS1 | 121.4656583206 | 31.1446265329 | 756 | 504990 | -93.36 | 9.74 | 429.02 | 0.02 | 2.97 | 1576 |
| 2024-09-20 22:21:41.522 | MS1 | 121.4656629984 | 31.1446333719 | 756 | 504990 | -91.88 | 7.38 | 546.15 | 0.03 | 2.31 | 1578 |
| 2024-09-20 22:21:42.502 | MS1 | 121.4656754206 | 31.1446267989 | 756 | 504990 | -93.03 | 12.12 | 469.82 | 0.14 | 2.42 | 1568 |

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
| 3219548 | 1 | 121.4727821602 | 31.1498463101 | 311 | 15 | 11 | 22.6 | TDD | 121 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3233030 | 2 | 121.4735522682 | 31.1515123924 | 322 | 13 | 8 | 30.8 | TDD | 756 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3249126 | 4 | 121.4660223663 | 31.1529882857 | 178 | 1 | 8 | 28.9 | TDD | 685 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3263707 | 3 | 121.4687570264 | 31.1530976083 | 28 | 13 | 9 | 32.0 | TDD | 973 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.212 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.227 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.361 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.361 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.016 | NREventA3 | measId:2;ServCellPCI:646;Se... |
| 2024-09-20 22:21:38.256 | NRHandoverAttempt | SourcePCI:646;SourceNR-ARFC... |
| 2024-09-20 22:21:38.293 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.308 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.444 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.444 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219548 | 1 | 14.2987 | 5.1079 | -117.9248 | 11.8646 | 142.2224 | 0.0090 | 0.0190 |
| 2024_09_20 22:00 | 3233030 | 2 | 14.4140 | 15.6201 | -116.9072 | 13.9214 | 154.7904 | 0.0111 | 0.0118 |
| 2024_09_20 22:00 | 3263707 | 3 | 7.4048 | 12.8535 | -114.3504 | 18.5367 | 188.4764 | 0.0124 | 0.0144 |
| 2024_09_20 22:00 | 3249126 | 4 | 18.6310 | 5.4569 | -115.8293 | 19.1940 | 164.9700 | 0.0012 | 0.0175 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414639_143AB1DB | 504990 | 756 | -90.3 | 504990 | 121 | -100.3 | 504990 | 973 | -106.5 | 504990 | 685 |
| MR_1774414639_329D7AB5 | 504990 | 756 | -90.5 | 504990 | 121 | -99.1 | 504990 | 973 | -104.4 | 504990 | 685 |
| MR_1774414639_90C26B3A | 504990 | 756 | -91.7 | 504990 | 121 | -101.8 | 504990 | 973 | -103.7 | 504990 | 685 |
| MR_1774414639_22DA8EBC | 504990 | 756 | -91.7 | 504990 | 121 | -101.5 | 504990 | 973 | -104.0 | 504990 | 685 |
| MR_1774414639_9C5D520B | 504990 | 756 | -90.8 | 504990 | 121 | -99.1 | 504990 | 973 | -105.9 | 504990 | 685 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1416: `42417230-3be...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `42417230-3bec-4804-828c-5eeb16690f75` |
| Tag | **multiple-answer** |
| 정답 | **C16|C22** |
| C16 의미 | Increase transmission power for 3278178_1 |
| C22 의미 | Adjust the azimuth of 3278178_1 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1416] topology](images/train_1416.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3278178_1
- `C2`: Lift the tilt angle  of 3278840_3 by 3 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278178_1
- `C4`: Increase A3 Offset threshold for 3278178_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278840_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278178_1
- `C7`: Add neighbor relationship between 3262325_4 and 3278840_3
- `C8`: Press down the tilt angle  of 3278840_3 by 3 degrees
- `C9`: Decrease A3 Offset threshold for 3278840_3
- `C10`: Increase transmission power for 3278840_3
- `C11`: Lift the tilt angle of 3278178_1 by 10 degrees
- `C12`: Decrease transmission power for 3278178_1
- `C13`: Adjust the azimuth of 3278840_3 by 46 degrees
- `C14`: Press down the tilt angle of 3278178_1 by 10 degrees
- `C15`: Add neighbor relationship between 3278178_1 and 3278840_3
- `C16`: Increase transmission power for 3278178_1 **← 정답**
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278840_3
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease transmission power for 3278840_3
- `C20`: Check test server and transmission issues
- `C21`: Increase A3 Offset threshold for 3278840_3
- `C22`: Adjust the azimuth of 3278178_1 by 50 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.827 | MS1 | 121.4656696672 | 31.1446262690 | 760 | 504990 | -92.54 | 14.49 | 574.02 | 0.03 | 2.51 | 1568 |
| 2024-09-20 22:21:32.114 | MS1 | 121.4656649161 | 31.1446250353 | 760 | 504990 | -87.97 | 17.88 | 503.64 | 0.13 | 2.02 | 1573 |
| 2024-09-20 22:21:33.491 | MS1 | 121.4656672216 | 31.1446327629 | 760 | 504990 | -92.36 | 13.19 | 524.28 | 0.12 | 2.81 | 1576 |
| 2024-09-20 22:21:34.730 | MS1 | 121.4656723747 | 31.1446332367 | 760 | 504990 | -109.71 | 0.87 | 55.21 | 0.09 | 1.01 | 1583 |
| 2024-09-20 22:21:35.760 | MS1 | 121.4656700136 | 31.1446290368 | 760 | 504990 | -106.19 | -0.81 | 63.18 | 0.10 | 1.13 | 1593 |
| 2024-09-20 22:21:36.482 | MS1 | 121.4656581031 | 31.1446208727 | 760 | 504990 | -106.74 | 1.60 | 62.35 | 0.11 | 1.40 | 1585 |
| 2024-09-20 22:21:37.210 | MS1 | 121.4656695597 | 31.1446329660 | 760 | 504990 | -104.05 | 0.52 | 81.84 | 0.03 | 1.25 | 1584 |
| 2024-09-20 22:21:38.575 | MS1 | 121.4656710321 | 31.1446275490 | 760 | 504990 | -102.22 | -1.95 | 55.16 | 0.15 | 1.37 | 1592 |
| 2024-09-20 22:21:39.148 | MS1 | 121.4656752208 | 31.1446293851 | 760 | 504990 | -101.94 | 1.29 | 52.96 | 0.02 | 1.22 | 1587 |
| 2024-09-20 22:21:40.145 | MS1 | 121.4656768756 | 31.1446284853 | 760 | 504990 | -91.30 | 13.25 | 328.03 | 0.04 | 2.10 | 1586 |
| 2024-09-20 22:21:41.217 | MS1 | 121.4656615511 | 31.1446225234 | 760 | 504990 | -91.30 | 15.31 | 410.89 | 0.09 | 2.36 | 1590 |
| 2024-09-20 22:21:42.523 | MS1 | 121.4656735270 | 31.1446236297 | 760 | 504990 | -93.97 | 12.18 | 343.86 | 0.04 | 2.40 | 1565 |

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
| 3245864 | 2 | 121.4690741509 | 31.1518523034 | 123 | 2 | 2 | 38.4 | TDD | 64 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3262325 | 4 | 121.4687233557 | 31.1481420810 | 120 | 13 | 2 | 17.4 | TDD | 599 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3278178 | 1 | 121.4643434937 | 31.1458309960 | 190 | 7 | 1 | 40.4 | TDD | 760 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3278840 | 3 | 121.4741419978 | 31.1541090387 | 263 | 1 | 0 | 43.1 | TDD | 525 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.086 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.102 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.219 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.219 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.400 | NREventA2 | measId:1;ServCellPCI:852;Se... |
| 2024-09-20 22:21:34.520 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278178 | 1 | 19.0595 | 5.9501 | -114.1433 | 11.5602 | 128.7316 | 0.1053 | 0.0087 |
| 2024_09_20 22:00 | 3245864 | 2 | 16.8516 | 6.8043 | -114.9072 | 8.1595 | 130.2115 | 0.0086 | 0.0046 |
| 2024_09_20 22:00 | 3278840 | 3 | 6.8796 | 7.3540 | -117.4637 | 17.2780 | 148.9932 | 0.0157 | 0.0035 |
| 2024_09_20 22:00 | 3262325 | 4 | 19.2190 | 7.2453 | -115.1071 | 19.0734 | 122.7091 | 0.0043 | 0.0186 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413770_B149BD1A | 504990 | 760 | -110.3 | 504990 | 525 | -115.0 | 504990 | 599 | -125.1 | 504990 | 64 |
| MR_1774413770_A320C8C8 | 504990 | 760 | -107.8 | 504990 | 525 | -118.0 | 504990 | 599 | -126.6 | 504990 | 64 |
| MR_1774413770_36B1CBC3 | 504990 | 760 | -108.0 | 504990 | 525 | -116.4 | 504990 | 599 | -126.1 | 504990 | 64 |
| MR_1774413770_2763DD38 | 504990 | 760 | -111.7 | 504990 | 525 | -118.0 | 504990 | 599 | -125.5 | 504990 | 64 |
| MR_1774413770_415CC76C | 504990 | 760 | -108.1 | 504990 | 525 | -118.4 | 504990 | 599 | -126.4 | 504990 | 64 |
| MR_1774413770_33BE36C4 | 504990 | 760 | -108.5 | 504990 | 525 | -115.7 | 504990 | 599 | -123.0 | 504990 | 64 |
| MR_1774413770_60104049 | 504990 | 760 | -108.1 | 504990 | 525 | -116.7 | 504990 | 599 | -125.3 | 504990 | 64 |
| MR_1774413770_5D064363 | 504990 | 760 | -108.8 | 504990 | 525 | -117.0 | 504990 | 599 | -125.3 | 504990 | 64 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1417: `c5d2a2dd-8cc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c5d2a2dd-8cc6-4a10-905c-d2ec5da9a9e1` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Add neighbor relationship between 3237791_2 and 3212760_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1417] topology](images/train_1417.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3237791_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Lift the tilt angle  of 3212760_3 by 4 degrees
- `C4`: Increase transmission power for 3237791_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237791_2
- `C6`: Adjust the azimuth of 3212760_3 by 11 degrees
- `C7`: Adjust the azimuth of 3237791_2 by 50 degrees
- `C8`: Check test server and transmission issues
- `C9`: Decrease transmission power for 3237791_2
- `C10`: Decrease transmission power for 3212760_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237791_2
- `C12`: Increase A3 Offset threshold for 3212760_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212760_3
- `C14`: Add neighbor relationship between 3236521_4 and 3212760_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212760_3
- `C16`: Press down the tilt angle of 3237791_2 by 10 degrees
- `C17`: Decrease A3 Offset threshold for 3212760_3
- `C18`: Press down the tilt angle  of 3212760_3 by 4 degrees
- `C19`: Lift the tilt angle of 3237791_2 by 10 degrees
- `C20`: Add neighbor relationship between 3237791_2 and 3212760_3 **← 정답**
- `C21`: Increase transmission power for 3212760_3
- `C22`: Decrease A3 Offset threshold for 3237791_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.114 | MS1 | 121.4656754965 | 31.1446286988 | 745 | 504990 | -84.30 | 17.90 | 432.85 | 0.18 | 2.62 | 1563 |
| 2024-09-20 22:21:32.823 | MS1 | 121.4656618977 | 31.1446281537 | 745 | 504990 | -82.34 | 14.38 | 536.43 | 0.18 | 2.97 | 1592 |
| 2024-09-20 22:21:33.776 | MS1 | 121.4656679481 | 31.1446375616 | 745 | 504990 | -75.16 | 13.52 | 409.87 | 0.05 | 2.57 | 1571 |
| 2024-09-20 22:21:34.204 | MS1 | 121.4656645571 | 31.1446235517 | 745 | 504990 | -87.55 | -1.56 | 41.40 | 0.14 | 1.44 | 1589 |
| 2024-09-20 22:21:35.354 | MS1 | 121.4656703806 | 31.1446213727 | 745 | 504990 | -85.74 | -0.85 | 57.83 | 0.05 | 1.16 | 1572 |
| 2024-09-20 22:21:36.812 | MS1 | 121.4656645231 | 31.1446247761 | 745 | 504990 | -85.07 | -3.57 | 74.53 | 0.07 | 1.21 | 1566 |
| 2024-09-20 22:21:37.427 | MS1 | 121.4656661884 | 31.1446266870 | 745 | 504990 | -85.79 | -1.05 | 51.34 | 0.12 | 1.05 | 1600 |
| 2024-09-20 22:21:38.891 | MS1 | 121.4656714889 | 31.1446283267 | 745 | 504990 | -78.21 | 13.82 | 566.78 | 0.04 | 1.14 | 1571 |
| 2024-09-20 22:21:39.530 | MS1 | 121.4656600669 | 31.1446321707 | 745 | 504990 | -77.04 | 13.17 | 560.42 | 0.13 | 1.38 | 1592 |
| 2024-09-20 22:21:40.809 | MS1 | 121.4656685519 | 31.1446232673 | 745 | 504990 | -81.80 | 14.86 | 354.21 | 0.10 | 2.15 | 1580 |
| 2024-09-20 22:21:41.802 | MS1 | 121.4656737108 | 31.1446367768 | 745 | 504990 | -77.40 | 16.99 | 605.28 | 0.04 | 2.33 | 1562 |
| 2024-09-20 22:21:42.307 | MS1 | 121.4656600937 | 31.1446228403 | 745 | 504990 | -77.16 | 13.46 | 529.72 | 0.13 | 2.17 | 1577 |

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
| 3212760 | 3 | 121.4753148235 | 31.1443773322 | 283 | 1 | 10 | 45.9 | TDD | 327 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3236521 | 4 | 121.4689393273 | 31.1508474943 | 132 | 4 | 11 | 15.2 | TDD | 671 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3237791 | 2 | 121.4749505367 | 31.1454853637 | 153 | 15 | 10 | 23.3 | TDD | 745 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3244574 | 1 | 121.4650119951 | 31.1486086693 | 288 | 2 | 5 | 25.3 | TDD | 440 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.837 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.855 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.997 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.997 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.679 | NREventA3 | measId:2;ServCellPCI:287;Se... |
| 2024-09-20 22:21:35.679 | NREventA3 | measId:2;ServCellPCI:287;Se... |
| 2024-09-20 22:21:36.679 | NREventA3 | measId:2;ServCellPCI:287;Se... |
| 2024-09-20 22:21:39.179 | NRRRCReestablishAttempt | PCI:287 |
| 2024-09-20 22:21:39.189 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.203 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.337 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.337 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244574 | 1 | 18.3475 | 18.3946 | -116.8644 | 6.6456 | 141.9993 | 0.0184 | 0.0024 |
| 2024_09_20 22:00 | 3237791 | 2 | 15.5060 | 9.5749 | -116.3763 | 7.7948 | 162.3845 | 0.0022 | 0.1167 |
| 2024_09_20 22:00 | 3212760 | 3 | 16.3462 | 18.4833 | -117.4653 | 19.9534 | 196.3941 | 0.0004 | 0.0150 |
| 2024_09_20 22:00 | 3236521 | 4 | 15.5147 | 5.4798 | -116.8167 | 15.7831 | 182.9576 | 0.0106 | 0.0199 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414240_874AA771 | 504990 | 327 | -81.2 | 504990 | 745 | -87.3 | 504990 | 671 | -83.6 | 504990 | 440 |
| MR_1774414240_47481CC8 | 504990 | 327 | -84.1 | 504990 | 745 | -86.0 | 504990 | 671 | -83.4 | 504990 | 440 |
| MR_1774414240_D1B5D7A9 | 504990 | 745 | -88.5 | 504990 | 327 | -81.5 | 504990 | 671 | -81.3 | 504990 | 440 |
| MR_1774414240_F91AFE6C | 504990 | 327 | -81.0 | 504990 | 745 | -88.9 | 504990 | 671 | -82.0 | 504990 | 440 |
| MR_1774414240_CA43530F | 504990 | 745 | -87.2 | 504990 | 327 | -83.9 | 504990 | 671 | -82.0 | 504990 | 440 |
| MR_1774414240_B51B7A3C | 504990 | 327 | -83.2 | 504990 | 745 | -86.8 | 504990 | 671 | -84.8 | 504990 | 440 |
| MR_1774414240_428D91C4 | 504990 | 327 | -82.6 | 504990 | 745 | -87.7 | 504990 | 671 | -83.4 | 504990 | 440 |
| MR_1774414240_F40D27D9 | 504990 | 327 | -80.5 | 504990 | 745 | -88.4 | 504990 | 671 | -81.9 | 504990 | 440 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1418: `73474dfb-698...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `73474dfb-6988-481c-baad-2bb292a43c4d` |
| Tag | **multiple-answer** |
| 정답 | **C1|C15** |
| C1 의미 | Press down the tilt angle  of 3229873_3 by 2 degrees |
| C15 의미 | Decrease transmission power for 3229873_3 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1418] topology](images/train_1418.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3229873_3 by 2 degrees **← 정답**
- `C2`: Adjust the azimuth of 3229873_3 by 4 degrees
- `C3`: Decrease transmission power for 3232155_1
- `C4`: Add neighbor relationship between 3232868_2 and 3229873_3
- `C5`: Increase transmission power for 3232155_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232155_1
- `C7`: Decrease A3 Offset threshold for 3232155_1
- `C8`: Increase transmission power for 3229873_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229873_3
- `C10`: Adjust the azimuth of 3232155_1 by 20 degrees
- `C11`: Decrease A3 Offset threshold for 3229873_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232155_1
- `C13`: Lift the tilt angle of 3232155_1 by 1 degrees
- `C14`: Lift the tilt angle  of 3229873_3 by 2 degrees
- `C15`: Decrease transmission power for 3229873_3 **← 정답**
- `C16`: Increase A3 Offset threshold for 3232155_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229873_3
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Press down the tilt angle of 3232155_1 by 1 degrees
- `C20`: Add neighbor relationship between 3232155_1 and 3229873_3
- `C21`: Check test server and transmission issues
- `C22`: Increase A3 Offset threshold for 3229873_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.150 | MS1 | 121.4656776795 | 31.1446262059 | 833 | 504990 | -77.87 | 15.58 | 539.33 | 0.13 | 2.13 | 1595 |
| 2024-09-20 22:21:32.548 | MS1 | 121.4656628651 | 31.1446263117 | 833 | 504990 | -81.36 | 13.93 | 401.56 | 0.07 | 2.62 | 1579 |
| 2024-09-20 22:21:33.309 | MS1 | 121.4656605521 | 31.1446257700 | 833 | 504990 | -78.56 | 12.98 | 334.87 | 0.18 | 2.04 | 1582 |
| 2024-09-20 22:21:34.262 | MS1 | 121.4656735211 | 31.1446195847 | 833 | 504990 | -86.76 | 1.91 | 67.47 | 0.12 | 1.42 | 1595 |
| 2024-09-20 22:21:35.542 | MS1 | 121.4656672348 | 31.1446290386 | 833 | 504990 | -94.13 | 0.58 | 66.67 | 0.08 | 1.44 | 1573 |
| 2024-09-20 22:21:36.633 | MS1 | 121.4656636371 | 31.1446226705 | 833 | 504990 | -87.61 | 1.56 | 66.11 | 0.18 | 1.22 | 1564 |
| 2024-09-20 22:21:37.801 | MS1 | 121.4656698765 | 31.1446273382 | 833 | 504990 | -90.96 | 0.91 | 91.05 | 0.17 | 1.15 | 1594 |
| 2024-09-20 22:21:38.334 | MS1 | 121.4656659342 | 31.1446291367 | 833 | 504990 | -89.26 | 2.63 | 45.49 | 0.13 | 1.20 | 1584 |
| 2024-09-20 22:21:39.124 | MS1 | 121.4656582760 | 31.1446295439 | 833 | 504990 | -85.39 | 3.51 | 81.10 | 0.15 | 1.03 | 1585 |
| 2024-09-20 22:21:40.698 | MS1 | 121.4656640390 | 31.1446279956 | 833 | 504990 | -83.29 | 15.39 | 432.88 | 0.06 | 2.40 | 1598 |
| 2024-09-20 22:21:41.655 | MS1 | 121.4656585114 | 31.1446290498 | 833 | 504990 | -77.91 | 16.25 | 499.39 | 0.13 | 2.44 | 1565 |
| 2024-09-20 22:21:42.593 | MS1 | 121.4656744007 | 31.1446323760 | 833 | 504990 | -83.14 | 15.20 | 464.27 | 0.13 | 2.49 | 1562 |

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
| 3229873 | 3 | 121.4727136640 | 31.1548348209 | 207 | 1 | 1 | 17.6 | TDD | 617 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3232155 | 1 | 121.4704838308 | 31.1505530610 | 235 | 0 | 1 | 18.5 | TDD | 833 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3232868 | 2 | 121.4751179797 | 31.1535383885 | 278 | 6 | 10 | 24.1 | TDD | 765 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3268535 | 4 | 121.4744752177 | 31.1513099170 | 176 | 11 | 9 | 29.6 | TDD | 511 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.149 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.173 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.283 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.283 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232155 | 1 | 10.3057 | 15.8641 | -108.5921 | 10.1972 | 199.9099 | 0.0186 | 0.0134 |
| 2024_09_20 22:00 | 3232868 | 2 | 11.9526 | 9.8250 | -116.4812 | 12.5418 | 178.0658 | 0.0010 | 0.0005 |
| 2024_09_20 22:00 | 3229873 | 3 | 7.8381 | 8.9756 | -115.3472 | 13.7735 | 149.9431 | 0.0135 | 0.0116 |
| 2024_09_20 22:00 | 3268535 | 4 | 5.6135 | 12.3689 | -117.4004 | 16.3559 | 111.3187 | 0.0062 | 0.0053 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416292_04A156AD | 504990 | 833 | -85.3 | 504990 | 617 | -83.3 | 504990 | 765 | -88.2 | 504990 | 511 |
| MR_1774416292_616E83DD | 504990 | 833 | -87.4 | 504990 | 617 | -82.9 | 504990 | 765 | -87.5 | 504990 | 511 |
| MR_1774416292_45D368AB | 504990 | 833 | -87.3 | 504990 | 617 | -85.9 | 504990 | 765 | -89.7 | 504990 | 511 |
| MR_1774416292_9A88E060 | 504990 | 833 | -87.2 | 504990 | 617 | -84.7 | 504990 | 765 | -86.2 | 504990 | 511 |
| MR_1774416292_8F6D9660 | 504990 | 617 | -88.4 | 504990 | 833 | -83.6 | 504990 | 765 | -88.7 | 504990 | 511 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1419: `24b6b687-93e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `24b6b687-93e0-49a1-8810-c577bd2794c6` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Add neighbor relationship between 3251332_1 and 3275492_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1419] topology](images/train_1419.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3251332_1 and 3275492_3 **← 정답**
- `C2`: Check test server and transmission issues
- `C3`: Lift the tilt angle of 3251332_1 by 10 degrees
- `C4`: Increase A3 Offset threshold for 3251332_1
- `C5`: Adjust the azimuth of 3275492_3 by 50 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251332_1
- `C8`: Decrease transmission power for 3275492_3
- `C9`: Adjust the azimuth of 3251332_1 by 50 degrees
- `C10`: Press down the tilt angle of 3251332_1 by 10 degrees
- `C11`: Press down the tilt angle  of 3275492_3 by 4 degrees
- `C12`: Decrease transmission power for 3251332_1
- `C13`: Increase A3 Offset threshold for 3275492_3
- `C14`: Decrease A3 Offset threshold for 3251332_1
- `C15`: Lift the tilt angle  of 3275492_3 by 4 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275492_3
- `C17`: Decrease A3 Offset threshold for 3275492_3
- `C18`: Add neighbor relationship between 3232170_2 and 3275492_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275492_3
- `C20`: Increase transmission power for 3275492_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251332_1
- `C22`: Increase transmission power for 3251332_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.263 | MS1 | 121.4656584314 | 31.1446241598 | 128 | 504990 | -79.64 | 13.13 | 481.30 | 0.03 | 2.65 | 1560 |
| 2024-09-20 22:21:32.134 | MS1 | 121.4656707282 | 31.1446245352 | 128 | 504990 | -79.71 | 16.57 | 381.05 | 0.14 | 2.48 | 1570 |
| 2024-09-20 22:21:33.847 | MS1 | 121.4656648847 | 31.1446355110 | 128 | 504990 | -78.74 | 12.75 | 535.22 | 0.19 | 2.51 | 1562 |
| 2024-09-20 22:21:34.749 | MS1 | 121.4656615228 | 31.1446330307 | 128 | 504990 | -88.51 | -0.78 | 40.30 | 0.02 | 1.41 | 1583 |
| 2024-09-20 22:21:35.554 | MS1 | 121.4656728007 | 31.1446202134 | 128 | 504990 | -86.30 | -0.85 | 43.69 | 0.06 | 1.22 | 1584 |
| 2024-09-20 22:21:36.981 | MS1 | 121.4656760202 | 31.1446271524 | 128 | 504990 | -93.96 | -3.50 | 62.86 | 0.14 | 1.32 | 1566 |
| 2024-09-20 22:21:37.189 | MS1 | 121.4656777192 | 31.1446202271 | 128 | 504990 | -89.54 | -1.97 | 46.59 | 0.14 | 1.26 | 1567 |
| 2024-09-20 22:21:38.227 | MS1 | 121.4656644166 | 31.1446347341 | 128 | 504990 | -78.98 | 17.71 | 570.39 | 0.05 | 1.23 | 1560 |
| 2024-09-20 22:21:39.577 | MS1 | 121.4656740001 | 31.1446341620 | 128 | 504990 | -83.76 | 14.51 | 392.35 | 0.18 | 1.13 | 1591 |
| 2024-09-20 22:21:40.186 | MS1 | 121.4656736700 | 31.1446299799 | 128 | 504990 | -76.26 | 14.70 | 536.27 | 0.06 | 2.77 | 1586 |
| 2024-09-20 22:21:41.746 | MS1 | 121.4656708151 | 31.1446347728 | 128 | 504990 | -75.82 | 12.81 | 498.69 | 0.19 | 2.65 | 1584 |
| 2024-09-20 22:21:42.483 | MS1 | 121.4656671370 | 31.1446355383 | 128 | 504990 | -79.99 | 12.34 | 566.54 | 0.18 | 2.94 | 1569 |

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
| 3232170 | 2 | 121.4696765271 | 31.1484446616 | 100 | 7 | 10 | 33.5 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3250065 | 4 | 121.4664718668 | 31.1524402377 | 334 | 1 | 8 | 48.9 | TDD | 757 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3251332 | 1 | 121.4702572299 | 31.1540120717 | 337 | 13 | 10 | 35.4 | TDD | 128 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3275492 | 3 | 121.4740423277 | 31.1534008290 | 269 | 3 | 12 | 32.8 | TDD | 547 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.451 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.469 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.595 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.595 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.282 | NREventA3 | measId:2;ServCellPCI:473;Se... |
| 2024-09-20 22:21:36.282 | NREventA3 | measId:2;ServCellPCI:473;Se... |
| 2024-09-20 22:21:37.282 | NREventA3 | measId:2;ServCellPCI:473;Se... |
| 2024-09-20 22:21:39.782 | NRRRCReestablishAttempt | PCI:473 |
| 2024-09-20 22:21:39.798 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.812 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.957 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.957 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251332 | 1 | 5.7623 | 10.6208 | -114.2497 | 14.7497 | 112.1588 | 0.0037 | 0.1651 |
| 2024_09_20 22:00 | 3232170 | 2 | 14.6287 | 12.0812 | -114.6246 | 11.5758 | 159.6027 | 0.0023 | 0.0065 |
| 2024_09_20 22:00 | 3275492 | 3 | 17.9824 | 16.3413 | -114.4180 | 10.1981 | 122.2833 | 0.0120 | 0.0156 |
| 2024_09_20 22:00 | 3250065 | 4 | 15.9960 | 6.3244 | -117.1800 | 13.8247 | 106.3907 | 0.0000 | 0.0052 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414602_B27F1F35 | 504990 | 547 | -83.3 | 504990 | 128 | -90.1 | 504990 | 866 | -83.6 | 504990 | 757 |
| MR_1774414602_E0AFB70B | 504990 | 547 | -81.7 | 504990 | 128 | -87.5 | 504990 | 866 | -82.8 | 504990 | 757 |
| MR_1774414602_8EB460B1 | 504990 | 547 | -83.8 | 504990 | 128 | -86.6 | 504990 | 866 | -82.2 | 504990 | 757 |
| MR_1774414602_2EA2A521 | 504990 | 547 | -83.5 | 504990 | 128 | -89.1 | 504990 | 866 | -83.1 | 504990 | 757 |
| MR_1774414602_4EBC3693 | 504990 | 128 | -87.4 | 504990 | 547 | -82.1 | 504990 | 866 | -82.7 | 504990 | 757 |
| MR_1774414602_8F6C8473 | 504990 | 128 | -88.1 | 504990 | 547 | -82.4 | 504990 | 866 | -82.7 | 504990 | 757 |

> *... 2개 열 생략 (전체 14열)*

---
