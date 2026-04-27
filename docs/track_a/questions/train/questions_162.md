# Track A 문제 분석 — train[1610]~train[1619]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1610] ~ train[1619] (10개)

## 목차

1. [문제 1610: `b967a706-d25...`](#1610) — single-answer, 정답: C13
2. [문제 1611: `2ab21f3b-0f4...`](#1611) — multiple-answer, 정답: C5|C6|C16|C20
3. [문제 1612: `187de91d-4c5...`](#1612) — single-answer, 정답: C10
4. [문제 1613: `b6707eeb-8aa...`](#1613) — single-answer, 정답: C7
5. [문제 1614: `f9c9cfef-011...`](#1614) — single-answer, 정답: C1
6. [문제 1615: `f5c3fd9d-145...`](#1615) — single-answer, 정답: C3
7. [문제 1616: `f3d672a4-1d0...`](#1616) — multiple-answer, 정답: C17|C20
8. [문제 1617: `35eae4cb-5a6...`](#1617) — single-answer, 정답: C11
9. [문제 1618: `2cc6aa04-f45...`](#1618) — single-answer, 정답: C19
10. [문제 1619: `cc3238b2-865...`](#1619) — single-answer, 정답: C3

---

### 문제 1610: `b967a706-d25...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b967a706-d254-448d-a1e9-87930cdf97a8` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease A3 Offset threshold for 3252385_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1610] topology](images/train_1610.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3252385_1 by 10 degrees
- `C2`: Decrease transmission power for 3252385_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Lift the tilt angle  of 3248586_3 by 10 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252385_1
- `C6`: Press down the tilt angle  of 3248586_3 by 10 degrees
- `C7`: Increase A3 Offset threshold for 3252385_1
- `C8`: Lift the tilt angle of 3252385_1 by 10 degrees
- `C9`: Increase transmission power for 3252385_1
- `C10`: Add neighbor relationship between 3252385_1 and 3248586_3
- `C11`: Adjust the azimuth of 3252385_1 by 50 degrees
- `C12`: Adjust the azimuth of 3248586_3 by 50 degrees
- `C13`: Decrease A3 Offset threshold for 3252385_1 **← 정답**
- `C14`: Increase transmission power for 3248586_3
- `C15`: Decrease transmission power for 3248586_3
- `C16`: Add neighbor relationship between 3261970_4 and 3248586_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248586_3
- `C18`: Check test server and transmission issues
- `C19`: Decrease A3 Offset threshold for 3248586_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252385_1
- `C21`: Increase A3 Offset threshold for 3248586_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248586_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.508 | MS1 | 121.4656763887 | 31.1446364471 | 635 | 504990 | -80.17 | 15.84 | 327.71 | 0.14 | 2.63 | 1580 |
| 2024-09-20 22:21:32.677 | MS1 | 121.4656742729 | 31.1446356066 | 635 | 504990 | -75.92 | 15.48 | 597.07 | 0.13 | 2.92 | 1569 |
| 2024-09-20 22:21:33.141 | MS1 | 121.4656599695 | 31.1446290042 | 635 | 504990 | -75.19 | 17.27 | 319.85 | 0.03 | 2.47 | 1600 |
| 2024-09-20 22:21:34.991 | MS1 | 121.4656734418 | 31.1446184941 | 635 | 504990 | -88.79 | -0.72 | 34.05 | 0.17 | 1.08 | 1571 |
| 2024-09-20 22:21:35.854 | MS1 | 121.4656600351 | 31.1446362396 | 635 | 504990 | -85.02 | -2.55 | 42.30 | 0.12 | 1.35 | 1595 |
| 2024-09-20 22:21:36.495 | MS1 | 121.4656631318 | 31.1446364245 | 635 | 504990 | -83.18 | -3.91 | 58.59 | 0.14 | 1.33 | 1566 |
| 2024-09-20 22:21:37.310 | MS1 | 121.4656767085 | 31.1446206266 | 635 | 504990 | -85.77 | -3.81 | 53.53 | 0.02 | 1.28 | 1562 |
| 2024-09-20 22:21:38.605 | MS1 | 121.4656668086 | 31.1446185248 | 635 | 504990 | -90.72 | -0.41 | 62.47 | 0.07 | 1.44 | 1560 |
| 2024-09-20 22:21:39.142 | MS1 | 121.4656603759 | 31.1446262697 | 748 | 504990 | -78.35 | 15.97 | 265.89 | 0.18 | 1.23 | 1571 |
| 2024-09-20 22:21:40.533 | MS1 | 121.4656609838 | 31.1446315665 | 748 | 504990 | -80.34 | 17.47 | 398.55 | 0.00 | 2.53 | 1582 |
| 2024-09-20 22:21:41.538 | MS1 | 121.4656776130 | 31.1446359508 | 748 | 504990 | -83.06 | 17.37 | 435.89 | 0.16 | 2.22 | 1575 |
| 2024-09-20 22:21:42.139 | MS1 | 121.4656714800 | 31.1446266002 | 748 | 504990 | -83.16 | 16.03 | 404.12 | 0.09 | 2.92 | 1590 |

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
| 3231283 | 2 | 121.4721152027 | 31.1449913544 | 252 | 2 | 8 | 22.1 | TDD | 396 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3248586 | 3 | 121.4737982356 | 31.1488666428 | 355 | 8 | 12 | 40.3 | TDD | 748 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3252385 | 1 | 121.4729549070 | 31.1468418848 | 353 | 12 | 8 | 19.0 | TDD | 635 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3261970 | 4 | 121.4692636143 | 31.1527044578 | 167 | 8 | 5 | 23.0 | TDD | 38 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.967 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.982 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.127 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.127 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.847 | NREventA3 | measId:2;ServCellPCI:597;Se... |
| 2024-09-20 22:21:38.087 | NRHandoverAttempt | SourcePCI:597;SourceNR-ARFC... |
| 2024-09-20 22:21:38.125 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.137 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.269 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.269 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252385 | 1 | 12.6860 | 19.1688 | -116.5812 | 5.0225 | 88.6663 | 0.0076 | 0.1818 |
| 2024_09_20 22:00 | 3231283 | 2 | 16.8890 | 14.7108 | -117.6032 | 8.8470 | 194.5190 | 0.0165 | 0.0154 |
| 2024_09_20 22:00 | 3248586 | 3 | 7.3934 | 12.0191 | -114.6855 | 15.9809 | 164.1442 | 0.0025 | 0.0135 |
| 2024_09_20 22:00 | 3261970 | 4 | 6.9691 | 6.7706 | -116.5233 | 7.9203 | 142.2033 | 0.0186 | 0.0024 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412960_1045043F | 504990 | 635 | -88.6 | 504990 | 748 | -83.6 | 504990 | 38 | -91.4 | 504990 | 396 |
| MR_1774412960_73331FB8 | 504990 | 635 | -88.7 | 504990 | 748 | -83.4 | 504990 | 38 | -90.2 | 504990 | 396 |
| MR_1774412960_977B2ACF | 504990 | 748 | -84.3 | 504990 | 635 | -88.6 | 504990 | 38 | -90.1 | 504990 | 396 |
| MR_1774412960_19FBA542 | 504990 | 635 | -89.5 | 504990 | 748 | -83.2 | 504990 | 38 | -89.7 | 504990 | 396 |
| MR_1774412960_34C6CBF4 | 504990 | 635 | -90.1 | 504990 | 748 | -83.6 | 504990 | 38 | -89.0 | 504990 | 396 |
| MR_1774412960_F484FF80 | 504990 | 635 | -89.4 | 504990 | 748 | -81.8 | 504990 | 38 | -91.5 | 504990 | 396 |
| MR_1774412960_5A675279 | 504990 | 635 | -90.6 | 504990 | 748 | -83.8 | 504990 | 38 | -89.5 | 504990 | 396 |
| MR_1774412960_9CBD3376 | 504990 | 635 | -88.8 | 504990 | 748 | -85.2 | 504990 | 38 | -90.5 | 504990 | 396 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1611: `2ab21f3b-0f4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2ab21f3b-0f44-4620-b20f-b184cbf3e18c` |
| Tag | **multiple-answer** |
| 정답 | **C5|C6|C16|C20** |
| C5 의미 | Increase A3 Offset threshold for 3227340_1 |
| C6 의미 | Decrease transmission power for 3243296_5 |
| C16 의미 | Press down the tilt angle  of 3243296_5 by 4 degrees |
| C20 의미 | Increase A3 Offset threshold for 3243296_5 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1611] topology](images/train_1611.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3227340_1
- `C2`: Lift the tilt angle  of 3243296_5 by 4 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243296_5
- `C4`: Add neighbor relationship between 3224036_3 and 3243296_5
- `C5`: Increase A3 Offset threshold for 3227340_1 **← 정답**
- `C6`: Decrease transmission power for 3243296_5 **← 정답**
- `C7`: Lift the tilt angle of 3227340_1 by 6 degrees
- `C8`: Adjust the azimuth of 3243296_5 by 43 degrees
- `C9`: Add neighbor relationship between 3227340_1 and 3243296_5
- `C10`: Adjust the azimuth of 3227340_1 by 7 degrees
- `C11`: Check test server and transmission issues
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243296_5
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227340_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase transmission power for 3243296_5
- `C16`: Press down the tilt angle  of 3243296_5 by 4 degrees **← 정답**
- `C17`: Decrease A3 Offset threshold for 3243296_5
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227340_1
- `C19`: Decrease transmission power for 3227340_1
- `C20`: Increase A3 Offset threshold for 3243296_5 **← 정답**
- `C21`: Decrease A3 Offset threshold for 3227340_1
- `C22`: Press down the tilt angle of 3227340_1 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.714 | MS1 | 121.4656726780 | 31.1446257647 | 610 | 504990 | -84.49 | 13.69 | 360.87 | 0.17 | 2.03 | 1596 |
| 2024-09-20 22:21:32.291 | MS1 | 121.4656756589 | 31.1446298028 | 610 | 504990 | -75.60 | 16.61 | 316.55 | 0.05 | 2.02 | 1565 |
| 2024-09-20 22:21:33.873 | MS1 | 121.4656756078 | 31.1446202399 | 610 | 504990 | -81.17 | 14.44 | 554.01 | 0.19 | 2.41 | 1572 |
| 2024-09-20 22:21:34.153 | MS1 | 121.4656675639 | 31.1446184833 | 978 | 504990 | -87.21 | 1.29 | 62.49 | 0.17 | 1.03 | 1565 |
| 2024-09-20 22:21:35.513 | MS1 | 121.4656698177 | 31.1446184061 | 978 | 504990 | -83.83 | 4.10 | 66.49 | 0.05 | 1.31 | 1592 |
| 2024-09-20 22:21:36.674 | MS1 | 121.4656681558 | 31.1446195511 | 610 | 504990 | -84.77 | 3.81 | 35.48 | 0.20 | 1.19 | 1573 |
| 2024-09-20 22:21:37.374 | MS1 | 121.4656709160 | 31.1446314409 | 610 | 504990 | -85.96 | 3.02 | 67.87 | 0.17 | 1.16 | 1598 |
| 2024-09-20 22:21:38.992 | MS1 | 121.4656779223 | 31.1446192816 | 978 | 504990 | -86.13 | 2.49 | 78.33 | 0.14 | 1.43 | 1580 |
| 2024-09-20 22:21:39.273 | MS1 | 121.4656666697 | 31.1446378213 | 978 | 504990 | -85.72 | 3.33 | 82.97 | 0.19 | 1.22 | 1582 |
| 2024-09-20 22:21:40.761 | MS1 | 121.4656727672 | 31.1446185919 | 978 | 504990 | -83.46 | 14.12 | 491.66 | 0.03 | 2.28 | 1597 |
| 2024-09-20 22:21:41.639 | MS1 | 121.4656754593 | 31.1446354391 | 978 | 504990 | -81.15 | 16.99 | 328.70 | 0.07 | 2.22 | 1595 |
| 2024-09-20 22:21:42.455 | MS1 | 121.4656649055 | 31.1446227422 | 978 | 504990 | -78.22 | 15.87 | 316.97 | 0.08 | 2.21 | 1572 |

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
| 3210012 | 4 | 121.4680561350 | 31.1456804575 | 117 | 2 | 11 | 32.4 | TDD | 978 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3224036 | 3 | 121.4732323044 | 31.1445472766 | 33 | 9 | 10 | 33.2 | TDD | 880 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3227340 | 1 | 121.4666951723 | 31.1478221876 | 202 | 3 | 4 | 18.8 | TDD | 610 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3243296 | 5 | 121.4753999742 | 31.1479126547 | 205 | 3 | 3 | 20.0 | TDD | 861 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3260904 | 2 | 121.4715125155 | 31.1505704400 | 195 | 13 | 6 | 47.9 | TDD | 941 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.883 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.987 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.987 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.713 | NREventA3 | measId:2;ServCellPCI:308;Se... |
| 2024-09-20 22:21:33.953 | NRHandoverAttempt | SourcePCI:308;SourceNR-ARFC... |
| 2024-09-20 22:21:33.996 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.011 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.150 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.150 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.713 | NREventA3 | measId:2;ServCellPCI:919;Se... |
| 2024-09-20 22:21:35.953 | NRHandoverAttempt | SourcePCI:919;SourceNR-ARFC... |
| 2024-09-20 22:21:35.983 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.998 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.139 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.139 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.713 | NREventA3 | measId:2;ServCellPCI:308;Se... |
| 2024-09-20 22:21:37.953 | NRHandoverAttempt | SourcePCI:308;SourceNR-ARFC... |
| 2024-09-20 22:21:37.991 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.001 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.124 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.124 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227340 | 1 | 12.9210 | 10.3362 | -117.9185 | 6.6893 | 160.2288 | 0.0058 | 0.0005 |
| 2024_09_20 22:00 | 3260904 | 2 | 5.2845 | 8.0205 | -116.2581 | 15.9499 | 81.3577 | 0.0121 | 0.0095 |
| 2024_09_20 22:00 | 3224036 | 3 | 17.7623 | 7.2157 | -117.8760 | 17.7655 | 94.9315 | 0.0015 | 0.0020 |
| 2024_09_20 22:00 | 3210012 | 4 | 7.5960 | 19.5999 | -116.9756 | 13.5211 | 120.1303 | 0.0041 | 0.0104 |
| 2024_09_20 22:00 | 3243296 | 5 | 15.1076 | 19.1614 | -116.4934 | 11.0527 | 141.8581 | 0.0006 | 0.0088 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414231_0F1A42C1 | 504990 | 978 | -85.3 | 504990 | 610 | -84.0 | 504990 | 861 | -85.4 | 504990 | 880 |
| MR_1774414231_2B4A5A87 | 504990 | 610 | -88.1 | 504990 | 978 | -87.2 | 504990 | 861 | -85.0 | 504990 | 880 |
| MR_1774414231_7E0DE622 | 504990 | 610 | -85.8 | 504990 | 978 | -85.1 | 504990 | 861 | -85.9 | 504990 | 880 |
| MR_1774414231_F2709FA6 | 504990 | 978 | -86.0 | 504990 | 610 | -84.1 | 504990 | 861 | -87.8 | 504990 | 880 |
| MR_1774414231_57A41DB5 | 504990 | 610 | -85.3 | 504990 | 978 | -86.7 | 504990 | 861 | -84.5 | 504990 | 880 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1612: `187de91d-4c5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `187de91d-4c5d-4eac-a93e-0e381e8d26b5` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3247648_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1612] topology](images/train_1612.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3245118_1 by 10 degrees
- `C2`: Increase A3 Offset threshold for 3247648_4
- `C3`: Check test server and transmission issues
- `C4`: Decrease transmission power for 3245118_1
- `C5`: Increase transmission power for 3245118_1
- `C6`: Increase A3 Offset threshold for 3245118_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245118_1
- `C8`: Adjust the azimuth of 3245118_1 by 50 degrees
- `C9`: Adjust the azimuth of 3247648_4 by 3 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247648_4 **← 정답**
- `C11`: Lift the tilt angle of 3247648_4 by 5 degrees
- `C12`: Add neighbor relationship between 3247648_4 and 3245118_1
- `C13`: Press down the tilt angle of 3247648_4 by 5 degrees
- `C14`: Increase transmission power for 3247648_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245118_1
- `C16`: Press down the tilt angle  of 3245118_1 by 10 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease A3 Offset threshold for 3245118_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247648_4
- `C20`: Decrease transmission power for 3247648_4
- `C21`: Decrease A3 Offset threshold for 3247648_4
- `C22`: Add neighbor relationship between 3254389_3 and 3245118_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.157 | MS1 | 121.4656689606 | 31.1446204211 | 494 | 504990 | -87.37 | 13.59 | 330.90 | 0.03 | 2.24 | 1572 |
| 2024-09-20 22:21:32.785 | MS1 | 121.4656750344 | 31.1446221297 | 494 | 504990 | -86.07 | 15.09 | 512.44 | 0.06 | 2.44 | 1571 |
| 2024-09-20 22:21:33.608 | MS1 | 121.4656633637 | 31.1446298224 | 494 | 504990 | -88.24 | 14.51 | 369.16 | 0.01 | 2.00 | 1567 |
| 2024-09-20 22:21:34.972 | MS1 | 121.4656581956 | 31.1446341088 | 494 | 504990 | -86.13 | 15.14 | 63.11 | 0.56 | 2.28 | 606 |
| 2024-09-20 22:21:35.415 | MS1 | 121.4656671832 | 31.1446218807 | 494 | 504990 | -85.57 | 12.89 | 55.65 | 0.53 | 2.76 | 619 |
| 2024-09-20 22:21:36.256 | MS1 | 121.4656717771 | 31.1446278663 | 494 | 504990 | -88.30 | 13.25 | 48.14 | 0.50 | 2.08 | 700 |
| 2024-09-20 22:21:37.220 | MS1 | 121.4656683252 | 31.1446364752 | 494 | 504990 | -89.41 | 12.83 | 56.43 | 0.68 | 2.92 | 579 |
| 2024-09-20 22:21:38.862 | MS1 | 121.4656768210 | 31.1446261845 | 494 | 504990 | -91.81 | 8.79 | 64.70 | 0.53 | 2.54 | 688 |
| 2024-09-20 22:21:39.762 | MS1 | 121.4656768510 | 31.1446296012 | 494 | 504990 | -89.81 | 9.36 | 94.30 | 0.69 | 2.14 | 528 |
| 2024-09-20 22:21:40.678 | MS1 | 121.4656670829 | 31.1446326872 | 494 | 504990 | -91.19 | 10.33 | 448.24 | 0.01 | 2.50 | 1567 |
| 2024-09-20 22:21:41.150 | MS1 | 121.4656711642 | 31.1446359610 | 494 | 504990 | -90.98 | 8.12 | 533.72 | 0.01 | 2.97 | 1598 |
| 2024-09-20 22:21:42.235 | MS1 | 121.4656689512 | 31.1446316886 | 494 | 504990 | -90.94 | 11.30 | 467.03 | 0.00 | 2.62 | 1586 |

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
| 3245118 | 1 | 121.4680253544 | 31.1493210570 | 19 | 13 | 6 | 16.9 | TDD | 72 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3247648 | 4 | 121.4725270767 | 31.1522096536 | 215 | 3 | 7 | 38.4 | TDD | 494 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3254389 | 3 | 121.4713718804 | 31.1557918827 | 272 | 7 | 4 | 35.5 | TDD | 997 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3278437 | 2 | 121.4687326539 | 31.1528241587 | 212 | 4 | 11 | 28.3 | TDD | 162 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.502 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.521 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.661 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.661 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.380 | NREventA3 | measId:2;ServCellPCI:401;Se... |
| 2024-09-20 22:21:38.620 | NRHandoverAttempt | SourcePCI:401;SourceNR-ARFC... |
| 2024-09-20 22:21:38.661 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.673 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.792 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.792 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245118 | 1 | 19.0820 | 12.9908 | -115.6027 | 17.9205 | 108.7425 | 0.0149 | 0.0146 |
| 2024_09_20 22:00 | 3278437 | 2 | 13.1767 | 7.8951 | -117.4425 | 17.3856 | 99.3264 | 0.0155 | 0.0042 |
| 2024_09_20 22:00 | 3254389 | 3 | 19.5415 | 15.2889 | -114.1199 | 12.6898 | 151.6048 | 0.0104 | 0.0189 |
| 2024_09_20 22:00 | 3247648 | 4 | 17.9545 | 12.1462 | -115.8940 | 5.2492 | 126.8227 | 0.0045 | 0.0100 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416844_87C1FBD8 | 504990 | 494 | -87.3 | 504990 | 72 | -88.4 | 504990 | 997 | -92.0 | 504990 | 162 |
| MR_1774416844_DB2EAC7D | 504990 | 494 | -87.6 | 504990 | 72 | -86.7 | 504990 | 997 | -92.8 | 504990 | 162 |
| MR_1774416844_2F400989 | 504990 | 494 | -87.2 | 504990 | 72 | -88.2 | 504990 | 997 | -92.0 | 504990 | 162 |
| MR_1774416844_35473580 | 504990 | 494 | -86.0 | 504990 | 72 | -87.5 | 504990 | 997 | -94.5 | 504990 | 162 |
| MR_1774416844_205A9539 | 504990 | 494 | -86.7 | 504990 | 72 | -85.1 | 504990 | 997 | -93.6 | 504990 | 162 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1613: `b6707eeb-8aa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b6707eeb-8aac-406a-9a1f-f26ea8cf589b` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1613] topology](images/train_1613.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3220033_3 by 50 degrees
- `C2`: Add neighbor relationship between 3220033_3 and 3213332_4
- `C3`: Press down the tilt angle of 3220033_3 by 8 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220033_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213332_4
- `C6`: Increase transmission power for 3213332_4
- `C7`: Insufficient data; more data is needed for judgment. **← 정답**
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213332_4
- `C9`: Decrease transmission power for 3213332_4
- `C10`: Decrease transmission power for 3220033_3
- `C11`: Decrease A3 Offset threshold for 3220033_3
- `C12`: Check test server and transmission issues
- `C13`: Add neighbor relationship between 3214757_2 and 3213332_4
- `C14`: Lift the tilt angle  of 3213332_4 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3213332_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220033_3
- `C17`: Increase transmission power for 3220033_3
- `C18`: Lift the tilt angle of 3220033_3 by 8 degrees
- `C19`: Adjust the azimuth of 3213332_4 by 36 degrees
- `C20`: Increase A3 Offset threshold for 3220033_3
- `C21`: Press down the tilt angle  of 3213332_4 by 10 degrees
- `C22`: Increase A3 Offset threshold for 3213332_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.714 | MS1 | 121.4656626070 | 31.1446336202 | 590 | 504990 | -87.55 | 16.45 | 396.25 | 0.16 | 2.34 | 1596 |
| 2024-09-20 22:21:32.893 | MS1 | 121.4656632035 | 31.1446267155 | 590 | 504990 | -86.57 | 13.21 | 443.48 | 0.18 | 2.97 | 1563 |
| 2024-09-20 22:21:33.767 | MS1 | 121.4656716013 | 31.1446316125 | 590 | 504990 | -86.77 | 17.03 | 302.79 | 0.17 | 2.30 | 1584 |
| 2024-09-20 22:21:34.338 | MS1 | 121.4656615427 | 31.1446314433 | 590 | 504990 | -88.26 | 13.14 | 71.82 | 0.07 | 2.70 | 1583 |
| 2024-09-20 22:21:35.362 | MS1 | 121.4656623445 | 31.1446244327 | 590 | 504990 | -86.25 | 16.58 | 97.40 | 0.05 | 2.44 | 1571 |
| 2024-09-20 22:21:36.369 | MS1 | 121.4656600473 | 31.1446344268 | 590 | 504990 | -86.31 | 12.85 | 94.38 | 0.03 | 2.74 | 1567 |
| 2024-09-20 22:21:37.955 | MS1 | 121.4656685470 | 31.1446338173 | 590 | 504990 | -91.92 | 12.91 | 62.34 | 0.13 | 2.63 | 1582 |
| 2024-09-20 22:21:38.362 | MS1 | 121.4656681183 | 31.1446308256 | 590 | 504990 | -92.50 | 10.80 | 58.34 | 0.11 | 2.57 | 1578 |
| 2024-09-20 22:21:39.930 | MS1 | 121.4656643112 | 31.1446315170 | 590 | 504990 | -92.15 | 8.73 | 90.98 | 0.11 | 2.44 | 1584 |
| 2024-09-20 22:21:40.104 | MS1 | 121.4656728263 | 31.1446214865 | 590 | 504990 | -89.25 | 11.06 | 384.83 | 0.13 | 2.90 | 1562 |
| 2024-09-20 22:21:41.361 | MS1 | 121.4656734054 | 31.1446370874 | 590 | 504990 | -93.72 | 10.40 | 329.30 | 0.09 | 2.73 | 1585 |
| 2024-09-20 22:21:42.295 | MS1 | 121.4656628858 | 31.1446323143 | 590 | 504990 | -91.00 | 7.36 | 572.72 | 0.19 | 2.53 | 1571 |

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
| 3211302 | 1 | 121.4677744565 | 31.1461506683 | 134 | 0 | 7 | 30.9 | TDD | 371 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3213332 | 4 | 121.4714872579 | 31.1550365953 | 170 | 13 | 3 | 47.0 | TDD | 863 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3214757 | 2 | 121.4751822198 | 31.1447802846 | 354 | 6 | 6 | 39.5 | TDD | 156 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3220033 | 3 | 121.4688922681 | 31.1536597225 | 21 | 7 | 4 | 26.0 | TDD | 590 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.081 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.097 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.231 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.231 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.894 | NREventA3 | measId:2;ServCellPCI:483;Se... |
| 2024-09-20 22:21:38.134 | NRHandoverAttempt | SourcePCI:483;SourceNR-ARFC... |
| 2024-09-20 22:21:38.176 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.187 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.305 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.305 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3211302 | 1 | 90.1306 | 89.4305 | -115.3455 | 19.5183 | 88.0290 | 0.0150 | 0.0057 |
| 2024_09_19 22:00 | 3214757 | 2 | 85.1200 | 81.5188 | -117.9980 | 8.2574 | 86.8419 | 0.0066 | 0.0015 |
| 2024_09_19 22:00 | 3220033 | 3 | 76.9652 | 80.9992 | -115.4207 | 13.3718 | 196.1192 | 0.0079 | 0.0152 |
| 2024_09_19 22:00 | 3213332 | 4 | 87.9807 | 75.9760 | -117.8883 | 6.2523 | 88.3798 | 0.0115 | 0.0092 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414494_B8AAD706 | 504990 | 590 | -87.1 | 504990 | 863 | -92.6 | 504990 | 156 | -102.1 | 504990 | 371 |
| MR_1774414494_AA928662 | 504990 | 590 | -89.5 | 504990 | 863 | -95.7 | 504990 | 156 | -101.9 | 504990 | 371 |
| MR_1774414494_E731644D | 504990 | 590 | -88.8 | 504990 | 863 | -94.8 | 504990 | 156 | -102.4 | 504990 | 371 |
| MR_1774414494_69DFE7E9 | 504990 | 590 | -89.2 | 504990 | 863 | -95.1 | 504990 | 156 | -99.7 | 504990 | 371 |
| MR_1774414494_59A35B6D | 504990 | 590 | -88.0 | 504990 | 863 | -92.0 | 504990 | 156 | -99.4 | 504990 | 371 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1614: `f9c9cfef-011...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f9c9cfef-0110-442b-b5d7-1f9d5651f700` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Lift the tilt angle  of 3249751_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1614] topology](images/train_1614.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3249751_3 by 10 degrees **← 정답**
- `C2`: Decrease transmission power for 3243462_2
- `C3`: Press down the tilt angle  of 3249751_3 by 10 degrees
- `C4`: Press down the tilt angle of 3243462_2 by 6 degrees
- `C5`: Lift the tilt angle of 3243462_2 by 6 degrees
- `C6`: Check test server and transmission issues
- `C7`: Add neighbor relationship between 3249751_3 and 3247910_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243462_2
- `C9`: Decrease transmission power for 3247910_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247910_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247910_1
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Adjust the azimuth of 3249751_3 by 50 degrees
- `C14`: Add neighbor relationship between 3243462_2 and 3247910_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243462_2
- `C16`: Increase A3 Offset threshold for 3247910_1
- `C17`: Decrease A3 Offset threshold for 3243462_2
- `C18`: Adjust the azimuth of 3243462_2 by 23 degrees
- `C19`: Decrease A3 Offset threshold for 3247910_1
- `C20`: Increase A3 Offset threshold for 3243462_2
- `C21`: Increase transmission power for 3247910_1
- `C22`: Increase transmission power for 3243462_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.671 | MS1 | 121.4656611900 | 31.1446291960 | 837 | 504990 | -87.87 | 16.48 | 356.09 | 0.10 | 2.68 | 1596 |
| 2024-09-20 22:21:32.330 | MS1 | 121.4656603146 | 31.1446219428 | 837 | 504990 | -86.78 | 17.04 | 567.31 | 0.15 | 2.08 | 1565 |
| 2024-09-20 22:21:33.264 | MS1 | 121.4656636683 | 31.1446241790 | 837 | 504990 | -88.68 | 17.49 | 301.95 | 0.02 | 2.38 | 1595 |
| 2024-09-20 22:21:34.370 | MS1 | 121.4656727865 | 31.1446237266 | 837 | 504990 | -88.54 | 12.91 | 98.05 | 0.00 | 2.19 | 1589 |
| 2024-09-20 22:21:35.528 | MS1 | 121.4656617182 | 31.1446269566 | 837 | 504990 | -85.42 | 13.71 | 98.04 | 0.07 | 2.56 | 1567 |
| 2024-09-20 22:21:36.792 | MS1 | 121.4656594981 | 31.1446256640 | 837 | 504990 | -90.90 | 12.78 | 58.52 | 0.16 | 2.39 | 1586 |
| 2024-09-20 22:21:37.768 | MS1 | 121.4656580974 | 31.1446285883 | 837 | 504990 | -91.27 | 8.05 | 93.60 | 0.00 | 2.50 | 1587 |
| 2024-09-20 22:21:38.460 | MS1 | 121.4656719483 | 31.1446378852 | 837 | 504990 | -90.76 | 11.14 | 64.26 | 0.15 | 2.53 | 1565 |
| 2024-09-20 22:21:39.280 | MS1 | 121.4656587666 | 31.1446337563 | 837 | 504990 | -93.71 | 11.05 | 57.71 | 0.04 | 2.18 | 1598 |
| 2024-09-20 22:21:40.808 | MS1 | 121.4656602746 | 31.1446374446 | 837 | 504990 | -92.75 | 7.89 | 329.72 | 0.12 | 2.07 | 1577 |
| 2024-09-20 22:21:41.283 | MS1 | 121.4656659330 | 31.1446277387 | 837 | 504990 | -90.80 | 12.92 | 427.52 | 0.10 | 2.22 | 1597 |
| 2024-09-20 22:21:42.506 | MS1 | 121.4656662697 | 31.1446311258 | 837 | 504990 | -92.16 | 7.48 | 307.62 | 0.07 | 2.74 | 1563 |

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
| 3243462 | 2 | 121.4663736230 | 31.1530368338 | 207 | 4 | 10 | 27.6 | TDD | 837 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3247910 | 1 | 121.4647137773 | 31.1517048850 | 119 | 12 | 2 | 44.5 | TDD | 602 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3249751 | 3 | 121.4755110905 | 31.1542420257 | 358 | 1 | 9 | 48.4 | TDD | 134 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3263476 | 4 | 121.4733181950 | 31.1503874737 | 17 | 4 | 11 | 44.4 | TDD | 647 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.498 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.514 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.646 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.646 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.336 | NREventA3 | measId:2;ServCellPCI:427;Se... |
| 2024-09-20 22:21:38.576 | NRHandoverAttempt | SourcePCI:427;SourceNR-ARFC... |
| 2024-09-20 22:21:38.623 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.636 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.762 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.762 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247910 | 1 | 5.4639 | 10.3189 | -117.9826 | 13.6141 | 185.4812 | 0.0147 | 0.0064 |
| 2024_09_20 22:00 | 3243462 | 2 | 76.3815 | 91.5448 | -116.1251 | 10.6725 | 92.7716 | 0.0189 | 0.0123 |
| 2024_09_20 22:00 | 3249751 | 3 | 8.7194 | 10.8902 | -116.3910 | 15.6975 | 138.1363 | 0.0123 | 0.0043 |
| 2024_09_20 22:00 | 3263476 | 4 | 14.6370 | 16.8383 | -114.8440 | 18.7175 | 196.4714 | 0.0146 | 0.0019 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416593_5CAB6668 | 504990 | 837 | -87.6 | 504990 | 602 | -93.8 | 504990 | 134 | -96.9 | 504990 | 647 |
| MR_1774416593_E4E0FA0A | 504990 | 837 | -89.3 | 504990 | 602 | -92.8 | 504990 | 134 | -97.8 | 504990 | 647 |
| MR_1774416593_0BC7467B | 504990 | 837 | -88.3 | 504990 | 602 | -92.0 | 504990 | 134 | -96.4 | 504990 | 647 |
| MR_1774416593_4E7C2574 | 504990 | 837 | -88.2 | 504990 | 602 | -91.1 | 504990 | 134 | -95.3 | 504990 | 647 |
| MR_1774416593_279E56F8 | 504990 | 837 | -88.6 | 504990 | 602 | -93.8 | 504990 | 134 | -96.4 | 504990 | 647 |
| MR_1774416593_1C3F51B4 | 504990 | 837 | -88.7 | 504990 | 602 | -91.8 | 504990 | 134 | -94.4 | 504990 | 647 |
| MR_1774416593_337CF62E | 504990 | 837 | -90.4 | 504990 | 602 | -91.1 | 504990 | 134 | -97.2 | 504990 | 647 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1615: `f5c3fd9d-145...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f5c3fd9d-1454-447c-bd93-78e9de84db94` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1615] topology](images/train_1615.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260451_1
- `C2`: Increase A3 Offset threshold for 3260451_1
- `C3`: Check test server and transmission issues **← 정답**
- `C4`: Decrease transmission power for 3260451_1
- `C5`: Adjust the azimuth of 3240708_4 by 50 degrees
- `C6`: Increase transmission power for 3260451_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240708_4
- `C8`: Add neighbor relationship between 3214473_2 and 3260451_1
- `C9`: Lift the tilt angle  of 3260451_1 by 10 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase A3 Offset threshold for 3240708_4
- `C12`: Decrease A3 Offset threshold for 3260451_1
- `C13`: Increase transmission power for 3240708_4
- `C14`: Press down the tilt angle  of 3260451_1 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3240708_4
- `C16`: Lift the tilt angle of 3240708_4 by 2 degrees
- `C17`: Press down the tilt angle of 3240708_4 by 2 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260451_1
- `C19`: Decrease transmission power for 3240708_4
- `C20`: Adjust the azimuth of 3260451_1 by 23 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240708_4
- `C22`: Add neighbor relationship between 3240708_4 and 3260451_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.417 | MS1 | 121.4656630279 | 31.1446238231 | 182 | 504990 | -87.12 | 14.34 | 401.27 | 0.03 | 2.60 | 1571 |
| 2024-09-20 22:21:32.938 | MS1 | 121.4656745506 | 31.1446223662 | 182 | 504990 | -89.50 | 15.71 | 469.78 | 0.07 | 2.04 | 1563 |
| 2024-09-20 22:21:33.684 | MS1 | 121.4656777717 | 31.1446356820 | 182 | 504990 | -91.56 | 14.96 | 542.76 | 0.12 | 2.68 | 1593 |
| 2024-09-20 22:21:34.603 | MS1 | 121.4656665731 | 31.1446188400 | 182 | 504990 | -88.12 | 14.63 | 96.91 | 0.18 | 2.40 | 400 |
| 2024-09-20 22:21:35.242 | MS1 | 121.4656772207 | 31.1446282793 | 182 | 504990 | -88.42 | 12.17 | 45.87 | 0.14 | 2.10 | 366 |
| 2024-09-20 22:21:36.575 | MS1 | 121.4656769608 | 31.1446291994 | 182 | 504990 | -86.90 | 15.64 | 58.88 | 0.05 | 2.00 | 424 |
| 2024-09-20 22:21:37.250 | MS1 | 121.4656749051 | 31.1446228347 | 182 | 504990 | -93.11 | 7.03 | 87.48 | 0.07 | 2.57 | 386 |
| 2024-09-20 22:21:38.215 | MS1 | 121.4656655624 | 31.1446359307 | 182 | 504990 | -91.29 | 11.16 | 42.92 | 0.02 | 2.15 | 360 |
| 2024-09-20 22:21:39.762 | MS1 | 121.4656632201 | 31.1446360431 | 182 | 504990 | -91.18 | 8.52 | 70.95 | 0.04 | 2.86 | 322 |
| 2024-09-20 22:21:40.334 | MS1 | 121.4656666573 | 31.1446198116 | 182 | 504990 | -92.09 | 11.89 | 431.74 | 0.13 | 2.28 | 1560 |
| 2024-09-20 22:21:41.944 | MS1 | 121.4656600683 | 31.1446261338 | 182 | 504990 | -92.41 | 8.77 | 586.63 | 0.09 | 2.04 | 1586 |
| 2024-09-20 22:21:42.224 | MS1 | 121.4656684191 | 31.1446372488 | 182 | 504990 | -90.42 | 12.56 | 524.17 | 0.10 | 2.79 | 1571 |

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
| 3214473 | 2 | 121.4700531851 | 31.1460878275 | 184 | 2 | 8 | 40.3 | TDD | 938 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3232164 | 3 | 121.4660398801 | 31.1481932038 | 327 | 15 | 5 | 43.2 | TDD | 253 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3240708 | 4 | 121.4674048217 | 31.1540499521 | 137 | 0 | 7 | 43.2 | TDD | 182 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3260451 | 1 | 121.4687321518 | 31.1500034552 | 183 | 10 | 9 | 31.5 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.882 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.001 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.001 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.713 | NREventA3 | measId:2;ServCellPCI:176;Se... |
| 2024-09-20 22:21:37.953 | NRHandoverAttempt | SourcePCI:176;SourceNR-ARFC... |
| 2024-09-20 22:21:38.001 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.013 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.152 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.152 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260451 | 1 | 13.2931 | 16.3484 | -115.5472 | 19.4924 | 195.2138 | 0.0101 | 0.0078 |
| 2024_09_20 22:00 | 3214473 | 2 | 6.0218 | 8.1633 | -114.7995 | 18.9646 | 93.5564 | 0.0104 | 0.0019 |
| 2024_09_20 22:00 | 3232164 | 3 | 10.0678 | 13.5937 | -115.9343 | 11.9145 | 195.2675 | 0.0188 | 0.0142 |
| 2024_09_20 22:00 | 3240708 | 4 | 8.5544 | 7.5945 | -116.2866 | 16.8481 | 126.6787 | 0.0162 | 0.0107 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414594_AF441C8A | 504990 | 182 | -88.6 | 504990 | 129 | -92.1 | 504990 | 938 | -98.2 | 504990 | 253 |
| MR_1774414594_EFC41960 | 504990 | 182 | -86.6 | 504990 | 129 | -91.6 | 504990 | 938 | -98.3 | 504990 | 253 |
| MR_1774414594_7DEC9DB4 | 504990 | 182 | -89.0 | 504990 | 129 | -94.2 | 504990 | 938 | -99.9 | 504990 | 253 |
| MR_1774414594_737EF9AE | 504990 | 182 | -86.2 | 504990 | 129 | -93.4 | 504990 | 938 | -99.6 | 504990 | 253 |
| MR_1774414594_F1FD8C8E | 504990 | 182 | -87.5 | 504990 | 129 | -92.5 | 504990 | 938 | -97.6 | 504990 | 253 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1616: `f3d672a4-1d0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f3d672a4-1d04-4950-ad2b-1a6ac0c0d9ee` |
| Tag | **multiple-answer** |
| 정답 | **C17|C20** |
| C17 의미 | Increase transmission power for 3259646_3 |
| C20 의미 | Adjust the azimuth of 3259646_3 by 35 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1616] topology](images/train_1616.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3213628_2
- `C2`: Decrease transmission power for 3259646_3
- `C3`: Press down the tilt angle  of 3213628_2 by 5 degrees
- `C4`: Increase A3 Offset threshold for 3213628_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259646_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259646_3
- `C7`: Add neighbor relationship between 3214031_4 and 3213628_2
- `C8`: Decrease A3 Offset threshold for 3259646_3
- `C9`: Check test server and transmission issues
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Press down the tilt angle of 3259646_3 by 10 degrees
- `C12`: Adjust the azimuth of 3213628_2 by 42 degrees
- `C13`: Lift the tilt angle  of 3213628_2 by 5 degrees
- `C14`: Decrease transmission power for 3213628_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213628_2
- `C16`: Increase transmission power for 3213628_2
- `C17`: Increase transmission power for 3259646_3 **← 정답**
- `C18`: Add neighbor relationship between 3259646_3 and 3213628_2
- `C19`: Increase A3 Offset threshold for 3259646_3
- `C20`: Adjust the azimuth of 3259646_3 by 35 degrees **← 정답**
- `C21`: Lift the tilt angle of 3259646_3 by 10 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213628_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.719 | MS1 | 121.4656747397 | 31.1446189039 | 709 | 504990 | -89.51 | 12.30 | 571.22 | 0.04 | 2.34 | 1585 |
| 2024-09-20 22:21:32.465 | MS1 | 121.4656695613 | 31.1446310085 | 709 | 504990 | -94.22 | 14.81 | 558.27 | 0.04 | 2.72 | 1575 |
| 2024-09-20 22:21:33.306 | MS1 | 121.4656734606 | 31.1446180530 | 709 | 504990 | -85.37 | 16.21 | 554.77 | 0.13 | 2.78 | 1566 |
| 2024-09-20 22:21:34.214 | MS1 | 121.4656623906 | 31.1446265934 | 709 | 504990 | -100.13 | 0.10 | 68.09 | 0.08 | 1.02 | 1590 |
| 2024-09-20 22:21:35.110 | MS1 | 121.4656699788 | 31.1446252419 | 709 | 504990 | -103.24 | 1.11 | 40.25 | 0.20 | 1.40 | 1593 |
| 2024-09-20 22:21:36.411 | MS1 | 121.4656713638 | 31.1446291032 | 709 | 504990 | -103.53 | -1.31 | 24.96 | 0.12 | 1.49 | 1565 |
| 2024-09-20 22:21:37.173 | MS1 | 121.4656618046 | 31.1446243406 | 709 | 504990 | -103.39 | -1.14 | 72.08 | 0.02 | 1.07 | 1589 |
| 2024-09-20 22:21:38.123 | MS1 | 121.4656779837 | 31.1446341845 | 709 | 504990 | -105.81 | -0.11 | 54.95 | 0.00 | 1.47 | 1573 |
| 2024-09-20 22:21:39.666 | MS1 | 121.4656619942 | 31.1446196708 | 709 | 504990 | -102.14 | 0.41 | 47.13 | 0.20 | 1.27 | 1561 |
| 2024-09-20 22:21:40.699 | MS1 | 121.4656636301 | 31.1446334818 | 709 | 504990 | -86.34 | 16.13 | 536.52 | 0.13 | 2.52 | 1590 |
| 2024-09-20 22:21:41.452 | MS1 | 121.4656748284 | 31.1446295304 | 709 | 504990 | -90.95 | 13.62 | 454.92 | 0.15 | 2.80 | 1585 |
| 2024-09-20 22:21:42.262 | MS1 | 121.4656721306 | 31.1446274536 | 709 | 504990 | -90.26 | 13.62 | 334.80 | 0.02 | 2.93 | 1585 |

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
| 3213628 | 2 | 121.4667618306 | 31.1474671811 | 240 | 2 | 0 | 18.8 | TDD | 500 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3214031 | 4 | 121.4674006146 | 31.1449991275 | 120 | 3 | 11 | 35.5 | TDD | 710 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3250170 | 1 | 121.4729779906 | 31.1532766308 | 213 | 12 | 1 | 18.6 | TDD | 506 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3259646 | 3 | 121.4642072700 | 31.1547449955 | 138 | 11 | 10 | 15.7 | TDD | 709 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.067 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.088 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.226 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.226 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.449 | NREventA2 | measId:1;ServCellPCI:978;Se... |
| 2024-09-20 22:21:34.597 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250170 | 1 | 14.0129 | 9.6665 | -116.1305 | 13.0177 | 138.6612 | 0.0187 | 0.0129 |
| 2024_09_20 22:00 | 3213628 | 2 | 18.1760 | 10.3097 | -115.9117 | 19.9707 | 198.9023 | 0.0189 | 0.0168 |
| 2024_09_20 22:00 | 3259646 | 3 | 16.4722 | 18.5287 | -115.7455 | 9.6931 | 152.3905 | 0.1833 | 0.0051 |
| 2024_09_20 22:00 | 3214031 | 4 | 8.0561 | 14.0563 | -116.5622 | 15.6897 | 89.7091 | 0.0089 | 0.0172 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413571_914710BC | 504990 | 709 | -101.2 | 504990 | 500 | -103.9 | 504990 | 710 | -113.6 | 504990 | 506 |
| MR_1774413571_F9C247AA | 504990 | 709 | -101.4 | 504990 | 500 | -104.3 | 504990 | 710 | -112.2 | 504990 | 506 |
| MR_1774413571_63E274E7 | 504990 | 709 | -98.5 | 504990 | 500 | -107.2 | 504990 | 710 | -113.6 | 504990 | 506 |
| MR_1774413571_D9D66DF5 | 504990 | 709 | -99.7 | 504990 | 500 | -104.7 | 504990 | 710 | -112.7 | 504990 | 506 |
| MR_1774413571_93965CEB | 504990 | 709 | -99.0 | 504990 | 500 | -105.5 | 504990 | 710 | -113.2 | 504990 | 506 |
| MR_1774413571_AAC2099F | 504990 | 709 | -101.9 | 504990 | 500 | -106.1 | 504990 | 710 | -111.7 | 504990 | 506 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1617: `35eae4cb-5a6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `35eae4cb-5a64-49fd-b86c-e8720f80db8e` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1617] topology](images/train_1617.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251981_4
- `C2`: Adjust the azimuth of 3251981_4 by 50 degrees
- `C3`: Decrease transmission power for 3231567_2
- `C4`: Lift the tilt angle  of 3231567_2 by 10 degrees
- `C5`: Increase transmission power for 3251981_4
- `C6`: Adjust the azimuth of 3231567_2 by 50 degrees
- `C7`: Check test server and transmission issues
- `C8`: Increase A3 Offset threshold for 3231567_2
- `C9`: Lift the tilt angle of 3251981_4 by 10 degrees
- `C10`: Add neighbor relationship between 3251981_4 and 3231567_2
- `C11`: Insufficient data; more data is needed for judgment. **← 정답**
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231567_2
- `C13`: Decrease A3 Offset threshold for 3251981_4
- `C14`: Increase transmission power for 3231567_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231567_2
- `C16`: Press down the tilt angle  of 3231567_2 by 10 degrees
- `C17`: Press down the tilt angle of 3251981_4 by 10 degrees
- `C18`: Decrease A3 Offset threshold for 3231567_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251981_4
- `C20`: Increase A3 Offset threshold for 3251981_4
- `C21`: Add neighbor relationship between 3246428_1 and 3231567_2
- `C22`: Decrease transmission power for 3251981_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.530 | MS1 | 121.4656690988 | 31.1446373983 | 284 | 504990 | -88.57 | 17.26 | 306.59 | 0.01 | 2.12 | 1573 |
| 2024-09-20 22:21:32.469 | MS1 | 121.4656671943 | 31.1446336224 | 284 | 504990 | -87.74 | 17.70 | 318.71 | 0.20 | 2.36 | 1579 |
| 2024-09-20 22:21:33.141 | MS1 | 121.4656776342 | 31.1446327463 | 284 | 504990 | -89.77 | 14.59 | 348.55 | 0.17 | 2.18 | 1562 |
| 2024-09-20 22:21:34.548 | MS1 | 121.4656717287 | 31.1446340496 | 284 | 504990 | -86.26 | 15.99 | 59.77 | 0.08 | 2.08 | 1568 |
| 2024-09-20 22:21:35.655 | MS1 | 121.4656703676 | 31.1446255536 | 284 | 504990 | -88.89 | 15.83 | 100.67 | 0.15 | 2.39 | 1587 |
| 2024-09-20 22:21:36.654 | MS1 | 121.4656650773 | 31.1446189096 | 284 | 504990 | -91.54 | 16.44 | 66.26 | 0.09 | 2.88 | 1579 |
| 2024-09-20 22:21:37.181 | MS1 | 121.4656634518 | 31.1446367322 | 284 | 504990 | -93.24 | 10.36 | 44.10 | 0.13 | 2.55 | 1581 |
| 2024-09-20 22:21:38.847 | MS1 | 121.4656712140 | 31.1446366560 | 284 | 504990 | -89.45 | 8.27 | 56.83 | 0.10 | 2.89 | 1591 |
| 2024-09-20 22:21:39.300 | MS1 | 121.4656738753 | 31.1446288761 | 284 | 504990 | -90.99 | 10.75 | 81.52 | 0.14 | 2.01 | 1600 |
| 2024-09-20 22:21:40.669 | MS1 | 121.4656736033 | 31.1446208072 | 284 | 504990 | -93.14 | 11.53 | 335.00 | 0.06 | 2.19 | 1596 |
| 2024-09-20 22:21:41.608 | MS1 | 121.4656756409 | 31.1446260224 | 284 | 504990 | -90.67 | 9.88 | 543.79 | 0.17 | 2.26 | 1588 |
| 2024-09-20 22:21:42.309 | MS1 | 121.4656648912 | 31.1446285801 | 284 | 504990 | -93.56 | 11.04 | 525.67 | 0.10 | 2.20 | 1588 |

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
| 3212247 | 3 | 121.4757427851 | 31.1500173016 | 146 | 1 | 10 | 46.6 | TDD | 66 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3231567 | 2 | 121.4650838879 | 31.1473991406 | 84 | 5 | 12 | 43.8 | TDD | 337 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3246428 | 1 | 121.4737490141 | 31.1478826280 | 41 | 13 | 2 | 35.7 | TDD | 864 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3251981 | 4 | 121.4681980028 | 31.1486999626 | 130 | 13 | 8 | 33.5 | TDD | 284 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.346 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.473 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.473 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.193 | NREventA3 | measId:2;ServCellPCI:10;Ser... |
| 2024-09-20 22:21:38.433 | NRHandoverAttempt | SourcePCI:10;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.482 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.494 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.629 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.629 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3246428 | 1 | 79.6351 | 94.1354 | -116.0877 | 5.3554 | 110.5015 | 0.0125 | 0.0028 |
| 2024_09_19 22:00 | 3231567 | 2 | 78.9353 | 84.5594 | -115.1586 | 12.4002 | 86.3289 | 0.0081 | 0.0159 |
| 2024_09_19 22:00 | 3212247 | 3 | 93.3656 | 86.1817 | -117.2017 | 17.1232 | 140.9097 | 0.0152 | 0.0085 |
| 2024_09_19 22:00 | 3251981 | 4 | 93.9724 | 85.3147 | -116.2289 | 12.7965 | 158.4555 | 0.0087 | 0.0186 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416207_6DBD70EE | 504990 | 284 | -85.3 | 504990 | 337 | -90.9 | 504990 | 864 | -97.4 | 504990 | 66 |
| MR_1774416207_D7CD83F3 | 504990 | 284 | -86.2 | 504990 | 337 | -91.5 | 504990 | 864 | -96.2 | 504990 | 66 |
| MR_1774416207_C9FFB2DF | 504990 | 284 | -84.5 | 504990 | 337 | -93.0 | 504990 | 864 | -99.5 | 504990 | 66 |
| MR_1774416207_B620CC5E | 504990 | 284 | -84.6 | 504990 | 337 | -93.9 | 504990 | 864 | -97.1 | 504990 | 66 |
| MR_1774416207_4FE925A8 | 504990 | 284 | -88.2 | 504990 | 337 | -91.9 | 504990 | 864 | -96.7 | 504990 | 66 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1618: `2cc6aa04-f45...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2cc6aa04-f451-4d21-893c-66a3c2b38b8c` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3255221_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1618] topology](images/train_1618.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3255221_1 by 41 degrees
- `C2`: Increase A3 Offset threshold for 3255221_1
- `C3`: Decrease A3 Offset threshold for 3255221_1
- `C4`: Check test server and transmission issues
- `C5`: Press down the tilt angle  of 3276280_3 by 10 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276280_3
- `C7`: Increase A3 Offset threshold for 3276280_3
- `C8`: Decrease A3 Offset threshold for 3276280_3
- `C9`: Decrease transmission power for 3255221_1
- `C10`: Add neighbor relationship between 3242192_2 and 3276280_3
- `C11`: Decrease transmission power for 3276280_3
- `C12`: Adjust the azimuth of 3276280_3 by 31 degrees
- `C13`: Add neighbor relationship between 3255221_1 and 3276280_3
- `C14`: Press down the tilt angle of 3255221_1 by 2 degrees
- `C15`: Lift the tilt angle  of 3276280_3 by 10 degrees
- `C16`: Increase transmission power for 3276280_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276280_3
- `C18`: Increase transmission power for 3255221_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255221_1 **← 정답**
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255221_1
- `C22`: Lift the tilt angle of 3255221_1 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.836 | MS1 | 121.4656642675 | 31.1446361601 | 1 | 504990 | -89.92 | 13.17 | 421.20 | 0.17 | 2.09 | 1564 |
| 2024-09-20 22:21:32.506 | MS1 | 121.4656669435 | 31.1446192978 | 1 | 504990 | -91.04 | 17.25 | 588.07 | 0.08 | 2.50 | 1560 |
| 2024-09-20 22:21:33.381 | MS1 | 121.4656705176 | 31.1446230579 | 1 | 504990 | -85.91 | 12.51 | 402.37 | 0.07 | 2.89 | 1573 |
| 2024-09-20 22:21:34.501 | MS1 | 121.4656686978 | 31.1446315752 | 1 | 504990 | -85.83 | 15.63 | 51.37 | 0.60 | 2.18 | 512 |
| 2024-09-20 22:21:35.671 | MS1 | 121.4656702031 | 31.1446248617 | 1 | 504990 | -89.53 | 16.28 | 51.25 | 0.65 | 2.32 | 640 |
| 2024-09-20 22:21:36.377 | MS1 | 121.4656765094 | 31.1446237486 | 1 | 504990 | -90.10 | 13.24 | 80.10 | 0.65 | 2.47 | 540 |
| 2024-09-20 22:21:37.919 | MS1 | 121.4656611641 | 31.1446190814 | 1 | 504990 | -89.24 | 10.20 | 71.95 | 0.65 | 2.61 | 502 |
| 2024-09-20 22:21:38.266 | MS1 | 121.4656600863 | 31.1446320572 | 1 | 504990 | -93.43 | 10.80 | 60.30 | 0.55 | 2.61 | 527 |
| 2024-09-20 22:21:39.797 | MS1 | 121.4656653774 | 31.1446379263 | 1 | 504990 | -92.70 | 10.12 | 59.80 | 0.68 | 2.57 | 696 |
| 2024-09-20 22:21:40.679 | MS1 | 121.4656697301 | 31.1446288182 | 1 | 504990 | -92.82 | 10.26 | 361.19 | 0.01 | 2.19 | 1593 |
| 2024-09-20 22:21:41.907 | MS1 | 121.4656676771 | 31.1446330000 | 1 | 504990 | -89.97 | 11.22 | 349.99 | 0.13 | 2.50 | 1595 |
| 2024-09-20 22:21:42.959 | MS1 | 121.4656602769 | 31.1446226010 | 1 | 504990 | -89.81 | 12.27 | 598.43 | 0.18 | 2.11 | 1574 |

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
| 3242192 | 2 | 121.4734857889 | 31.1536604952 | 21 | 11 | 6 | 34.1 | TDD | 953 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3255221 | 1 | 121.4672553844 | 31.1540035013 | 147 | 0 | 10 | 44.4 | TDD | 1 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3264331 | 4 | 121.4704016529 | 31.1447709913 | 270 | 11 | 2 | 35.8 | TDD | 511 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3276280 | 3 | 121.4747545864 | 31.1513706672 | 260 | 14 | 4 | 48.9 | TDD | 708 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.993 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.008 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.132 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.132 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.847 | NREventA3 | measId:2;ServCellPCI:736;Se... |
| 2024-09-20 22:21:38.087 | NRHandoverAttempt | SourcePCI:736;SourceNR-ARFC... |
| 2024-09-20 22:21:38.136 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.147 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.248 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.248 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255221 | 1 | 7.7021 | 9.7581 | -116.3761 | 17.2527 | 90.9665 | 0.0039 | 0.0120 |
| 2024_09_20 22:00 | 3242192 | 2 | 14.9837 | 8.8323 | -114.5956 | 16.3159 | 116.5030 | 0.0196 | 0.0027 |
| 2024_09_20 22:00 | 3276280 | 3 | 14.9264 | 8.0309 | -116.2636 | 12.0277 | 193.5058 | 0.0038 | 0.0144 |
| 2024_09_20 22:00 | 3264331 | 4 | 17.0220 | 14.9449 | -116.1139 | 6.4704 | 100.5593 | 0.0096 | 0.0008 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413338_C8EEC865 | 504990 | 1 | -84.3 | 504990 | 708 | -93.5 | 504990 | 953 | -96.0 | 504990 | 511 |
| MR_1774413338_C1BEE48D | 504990 | 1 | -83.8 | 504990 | 708 | -93.8 | 504990 | 953 | -93.7 | 504990 | 511 |
| MR_1774413338_F2892FE9 | 504990 | 1 | -86.4 | 504990 | 708 | -91.6 | 504990 | 953 | -94.8 | 504990 | 511 |
| MR_1774413338_4A190FC9 | 504990 | 1 | -87.8 | 504990 | 708 | -94.4 | 504990 | 953 | -94.0 | 504990 | 511 |
| MR_1774413338_2B86BD7D | 504990 | 1 | -87.3 | 504990 | 708 | -94.3 | 504990 | 953 | -96.1 | 504990 | 511 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1619: `cc3238b2-865...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cc3238b2-8655-47a7-8322-a4ec5c06a4a5` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211050_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1619] topology](images/train_1619.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3242486_6
- `C2`: Decrease transmission power for 3211050_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211050_1 **← 정답**
- `C4`: Lift the tilt angle of 3211050_1 by 2 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242486_6
- `C6`: Decrease A3 Offset threshold for 3211050_1
- `C7`: Increase transmission power for 3242486_6
- `C8`: Check test server and transmission issues
- `C9`: Adjust the azimuth of 3211050_1 by 19 degrees
- `C10`: Add neighbor relationship between 3211050_1 and 3242486_6
- `C11`: Increase transmission power for 3211050_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211050_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242486_6
- `C14`: Decrease A3 Offset threshold for 3242486_6
- `C15`: Adjust the azimuth of 3242486_6 by 26 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Press down the tilt angle  of 3242486_6 by 3 degrees
- `C18`: Lift the tilt angle  of 3242486_6 by 3 degrees
- `C19`: Add neighbor relationship between 3231850_7 and 3242486_6
- `C20`: Press down the tilt angle of 3211050_1 by 2 degrees
- `C21`: Increase A3 Offset threshold for 3211050_1
- `C22`: Increase A3 Offset threshold for 3242486_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.480 | MS1 | 121.4656608061 | 31.1446346639 | 548 | 504990 | -94.32 | 10.76 | 396.65 | 0.18 | 2.53 | 1591 |
| 2024-09-20 22:21:32.272 | MS1 | 121.4656743592 | 31.1446240028 | 1005 | 504990 | -93.10 | 13.73 | 497.40 | 0.20 | 2.12 | 1586 |
| 2024-09-20 22:21:33.983 | MS1 | 121.4656658548 | 31.1446315297 | 307 | 504990 | -93.50 | 10.63 | 523.59 | 0.06 | 2.75 | 1582 |
| 2024-09-20 22:21:34.716 | MS1 | 121.4656605673 | 31.1446181881 | 523 | 152650 | -92.32 | 7.59 | 62.20 | 0.04 | 1.63 | 925 |
| 2024-09-20 22:21:35.529 | MS1 | 121.4656618924 | 31.1446219514 | 587 | 152650 | -87.28 | 5.79 | 88.84 | 0.16 | 1.74 | 919 |
| 2024-09-20 22:21:36.759 | MS1 | 121.4656702244 | 31.1446238180 | 674 | 152650 | -92.47 | 6.89 | 83.07 | 0.09 | 1.83 | 993 |
| 2024-09-20 22:21:37.396 | MS1 | 121.4656747456 | 31.1446342385 | 303 | 152650 | -93.88 | 5.29 | 56.55 | 0.13 | 1.98 | 908 |
| 2024-09-20 22:21:38.457 | MS1 | 121.4656725464 | 31.1446215999 | 523 | 152650 | -92.97 | 2.73 | 74.14 | 0.01 | 1.80 | 990 |
| 2024-09-20 22:21:39.935 | MS1 | 121.4656675104 | 31.1446235226 | 587 | 152650 | -95.24 | 4.65 | 84.18 | 0.17 | 1.51 | 963 |
| 2024-09-20 22:21:40.493 | MS1 | 121.4656766945 | 31.1446358199 | 674 | 152650 | -94.83 | 3.76 | 69.92 | 0.05 | 2.50 | 1562 |
| 2024-09-20 22:21:41.743 | MS1 | 121.4656683695 | 31.1446319041 | 303 | 152650 | -94.05 | 5.42 | 49.13 | 0.18 | 2.89 | 1597 |
| 2024-09-20 22:21:42.154 | MS1 | 121.4656771040 | 31.1446274930 | 523 | 152650 | -89.17 | 7.71 | 87.02 | 0.04 | 2.56 | 1586 |

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
| 3211050 | 1 | 121.4710825505 | 31.1541342182 | 225 | 1 | 12 | 24.8 | TDD | 548 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3217905 | 4 | 121.4724663304 | 31.1471019818 | 81 | 15 | 1 | 28.6 | TDD | 633 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3227853 | 11 | 121.4725850287 | 31.1554017228 | 64 | 0 | 7 | 22.1 | FDD | 303 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3230467 | 13 | 121.4687247697 | 31.1558932456 | 147 | 5 | 2 | 18.6 | FDD | 445 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3231338 | 12 | 121.4740883302 | 31.1481868587 | 35 | 6 | 8 | 1.5 | FDD | 848 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3231850 | 7 | 121.4654746000 | 31.1518930726 | 332 | 4 | 2 | 15.2 | FDD | 674 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3235528 | 9 | 121.4756338294 | 31.1464794786 | 146 | 7 | 8 | 18.1 | FDD | 587 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3236713 | 5 | 121.4730690576 | 31.1554676484 | 115 | 11 | 0 | 7.2 | TDD | 307 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3242486 | 6 | 121.4688225947 | 31.1523717429 | 225 | 2 | 11 | 11.5 | TDD | 665 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3255634 | 10 | 121.4660913828 | 31.1474786406 | 268 | 0 | 4 | 25.6 | FDD | 523 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3257524 | 3 | 121.4729779045 | 31.1454665336 | 22 | 11 | 9 | 13.5 | TDD | 1005 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3259125 | 2 | 121.4719659131 | 31.1517658923 | 30 | 0 | 6 | 5.9 | TDD | 549 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3261922 | 8 | 121.4665739285 | 31.1553710345 | 125 | 10 | 6 | 0.3 | FDD | 162 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |

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
| 2024-09-20 22:21:30.785 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.802 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.920 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.920 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.639 | NREventA2 | measId:1;ServCellPCI:583;Se... |
| 2024-09-20 22:21:34.744 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.021 | NREventA5 | measId:3;ServCellPCI:583;Se... |
| 2024-09-20 22:21:35.082 | NRHandoverAttempt | SourcePCI:583;SourceNR-ARFC... |
| 2024-09-20 22:21:35.111 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.124 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.270 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.270 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211050 | 1 | 17.7293 | 6.0946 | -115.2557 | 18.8467 | 129.6201 | 0.0052 | 0.0045 |
| 2024_09_20 22:00 | 3259125 | 2 | 17.7520 | 10.9946 | -115.4275 | 9.5365 | 171.4220 | 0.0019 | 0.0156 |
| 2024_09_20 22:00 | 3257524 | 3 | 17.8074 | 19.9552 | -114.4367 | 14.8001 | 198.7414 | 0.0191 | 0.0010 |
| 2024_09_20 22:00 | 3217905 | 4 | 9.8439 | 8.9117 | -117.6912 | 10.5215 | 188.8008 | 0.0015 | 0.0106 |
| 2024_09_20 22:00 | 3236713 | 5 | 9.1615 | 13.7712 | -115.4896 | 5.0310 | 100.2703 | 0.0195 | 0.0004 |
| 2024_09_20 22:00 | 3242486 | 6 | 7.3950 | 6.2801 | -114.7235 | 9.7040 | 98.7576 | 0.0050 | 0.0073 |
| 2024_09_20 22:00 | 3231850 | 7 | 19.8261 | 6.6493 | -117.0881 | 3.3032 | 34.9830 | 0.0148 | 0.0175 |
| 2024_09_20 22:00 | 3261922 | 8 | 15.4126 | 11.5870 | -115.4354 | 3.5526 | 46.0660 | 0.0087 | 0.0200 |
| 2024_09_20 22:00 | 3235528 | 9 | 13.0617 | 12.9655 | -116.5623 | 3.8191 | 48.6292 | 0.0160 | 0.0000 |
| 2024_09_20 22:00 | 3255634 | 10 | 7.4550 | 16.0964 | -115.2548 | 3.0557 | 54.5369 | 0.0118 | 0.0121 |
| 2024_09_20 22:00 | 3227853 | 11 | 13.4611 | 8.1247 | -116.4810 | 4.8866 | 31.8930 | 0.0147 | 0.0127 |
| 2024_09_20 22:00 | 3231338 | 12 | 6.5660 | 7.4427 | -117.9787 | 3.6231 | 42.3074 | 0.0084 | 0.0181 |
| 2024_09_20 22:00 | 3230467 | 13 | 12.4180 | 16.5737 | -115.6035 | 3.9178 | 48.7729 | 0.0121 | 0.0113 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415793_B358D8AF | 152650 | 523 | -93.9 | 152650 | 445 | -100.9 | 152650 | 848 | -100.0 | 152650 | 162 |
| MR_1774415793_A7D54527 | 152650 | 523 | -91.7 | 152650 | 445 | -100.6 | 152650 | 848 | -101.2 | 152650 | 162 |
| MR_1774415793_56D9A535 | 504990 | 307 | -93.1 | 504990 | 665 | -90.4 | 504990 | 633 | -98.0 | 504990 | 549 |
| MR_1774415793_D985D098 | 152650 | 523 | -92.5 | 152650 | 445 | -99.3 | 152650 | 848 | -99.9 | 152650 | 162 |
| MR_1774415793_042DA98F | 152650 | 523 | -90.8 | 152650 | 445 | -97.8 | 152650 | 848 | -103.2 | 152650 | 162 |
| MR_1774415793_22BDC7DD | 504990 | 307 | -94.9 | 504990 | 665 | -91.2 | 504990 | 633 | -98.9 | 504990 | 549 |
| MR_1774415793_368347C0 | 504990 | 307 | -91.7 | 504990 | 665 | -90.9 | 504990 | 633 | -96.7 | 504990 | 549 |
| MR_1774415793_829A01FB | 152650 | 523 | -92.1 | 152650 | 445 | -98.1 | 152650 | 848 | -101.0 | 152650 | 162 |

> *... 2개 열 생략 (전체 14열)*

---
