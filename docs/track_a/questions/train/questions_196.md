# Track A 문제 분석 — train[1950]~train[1959]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1950] ~ train[1959] (10개)

## 목차

1. [문제 1950: `e4335f91-f20...`](#1950) — single-answer, 정답: C4
2. [문제 1951: `770a72d8-981...`](#1951) — single-answer, 정답: C12
3. [문제 1952: `b5354f10-c2f...`](#1952) — single-answer, 정답: C6
4. [문제 1953: `30a2a3fc-941...`](#1953) — single-answer, 정답: C19
5. [문제 1954: `1a0ad911-981...`](#1954) — single-answer, 정답: C16
6. [문제 1955: `73eb26df-276...`](#1955) — single-answer, 정답: C8
7. [문제 1956: `10bbe13d-290...`](#1956) — single-answer, 정답: C22
8. [문제 1957: `17ddd75f-b17...`](#1957) — single-answer, 정답: C10
9. [문제 1958: `86e78886-421...`](#1958) — multiple-answer, 정답: C5|C18
10. [문제 1959: `a3c2a91b-e93...`](#1959) — single-answer, 정답: C15

---

### 문제 1950: `e4335f91-f20...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e4335f91-f202-41b3-bfd8-17c20ca5b4c1` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Add neighbor relationship between 3261073_3 and 3220093_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1950] topology](images/train_1950.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3220093_2 by 2 degrees
- `C2`: Decrease transmission power for 3220093_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220093_2
- `C4`: Add neighbor relationship between 3261073_3 and 3220093_2 **← 정답**
- `C5`: Decrease A3 Offset threshold for 3261073_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261073_3
- `C7`: Adjust the azimuth of 3220093_2 by 3 degrees
- `C8`: Add neighbor relationship between 3252953_1 and 3220093_2
- `C9`: Decrease transmission power for 3261073_3
- `C10`: Increase A3 Offset threshold for 3261073_3
- `C11`: Increase transmission power for 3220093_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261073_3
- `C13`: Increase A3 Offset threshold for 3220093_2
- `C14`: Increase transmission power for 3261073_3
- `C15`: Check test server and transmission issues
- `C16`: Adjust the azimuth of 3261073_3 by 50 degrees
- `C17`: Decrease A3 Offset threshold for 3220093_2
- `C18`: Press down the tilt angle of 3261073_3 by 6 degrees
- `C19`: Lift the tilt angle  of 3220093_2 by 2 degrees
- `C20`: Lift the tilt angle of 3261073_3 by 6 degrees
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220093_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.857 | MS1 | 121.4656698690 | 31.1446234329 | 1005 | 504990 | -75.64 | 16.58 | 426.21 | 0.12 | 2.81 | 1584 |
| 2024-09-20 22:21:32.214 | MS1 | 121.4656684241 | 31.1446363776 | 1005 | 504990 | -75.50 | 16.71 | 358.82 | 0.14 | 2.95 | 1586 |
| 2024-09-20 22:21:33.542 | MS1 | 121.4656664104 | 31.1446305575 | 1005 | 504990 | -80.10 | 16.82 | 322.78 | 0.14 | 2.78 | 1582 |
| 2024-09-20 22:21:34.218 | MS1 | 121.4656748413 | 31.1446183898 | 1005 | 504990 | -92.23 | -2.21 | 42.45 | 0.14 | 1.12 | 1579 |
| 2024-09-20 22:21:35.100 | MS1 | 121.4656652425 | 31.1446272191 | 1005 | 504990 | -94.17 | -2.69 | 66.21 | 0.06 | 1.21 | 1599 |
| 2024-09-20 22:21:36.591 | MS1 | 121.4656712484 | 31.1446312934 | 1005 | 504990 | -87.40 | -0.94 | 46.60 | 0.09 | 1.26 | 1576 |
| 2024-09-20 22:21:37.558 | MS1 | 121.4656744684 | 31.1446245680 | 1005 | 504990 | -86.03 | -3.59 | 57.59 | 0.01 | 1.44 | 1560 |
| 2024-09-20 22:21:38.610 | MS1 | 121.4656597965 | 31.1446348849 | 1005 | 504990 | -78.32 | 16.89 | 344.80 | 0.13 | 1.35 | 1598 |
| 2024-09-20 22:21:39.741 | MS1 | 121.4656634351 | 31.1446295449 | 1005 | 504990 | -76.57 | 16.39 | 503.27 | 0.12 | 1.47 | 1560 |
| 2024-09-20 22:21:40.191 | MS1 | 121.4656638879 | 31.1446362304 | 1005 | 504990 | -83.11 | 14.33 | 522.94 | 0.04 | 2.11 | 1566 |
| 2024-09-20 22:21:41.682 | MS1 | 121.4656669642 | 31.1446199890 | 1005 | 504990 | -79.21 | 14.85 | 484.32 | 0.19 | 2.31 | 1583 |
| 2024-09-20 22:21:42.498 | MS1 | 121.4656692688 | 31.1446199952 | 1005 | 504990 | -81.47 | 14.37 | 496.57 | 0.08 | 2.88 | 1596 |

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
| 3217523 | 4 | 121.4669240844 | 31.1496909237 | 70 | 11 | 4 | 37.2 | TDD | 982 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3220093 | 2 | 121.4707406390 | 31.1489754739 | 228 | 1 | 5 | 16.0 | TDD | 499 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3252953 | 1 | 121.4647469909 | 31.1493419456 | 21 | 0 | 5 | 41.0 | TDD | 344 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3261073 | 3 | 121.4704155991 | 31.1491950289 | 8 | 2 | 11 | 43.6 | TDD | 1005 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.123 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.144 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.259 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.259 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.973 | NREventA3 | measId:2;ServCellPCI:453;Se... |
| 2024-09-20 22:21:35.973 | NREventA3 | measId:2;ServCellPCI:453;Se... |
| 2024-09-20 22:21:36.973 | NREventA3 | measId:2;ServCellPCI:453;Se... |
| 2024-09-20 22:21:39.473 | NRRRCReestablishAttempt | PCI:453 |
| 2024-09-20 22:21:39.485 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.496 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.644 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.644 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252953 | 1 | 10.4157 | 10.9316 | -114.9352 | 18.1499 | 108.0641 | 0.0110 | 0.0080 |
| 2024_09_20 22:00 | 3220093 | 2 | 17.5696 | 19.1006 | -116.1132 | 16.2165 | 162.7313 | 0.0037 | 0.0156 |
| 2024_09_20 22:00 | 3261073 | 3 | 7.2749 | 16.9679 | -114.8232 | 17.5306 | 104.9830 | 0.0133 | 0.1689 |
| 2024_09_20 22:00 | 3217523 | 4 | 16.8151 | 6.0040 | -114.5474 | 10.1961 | 149.7160 | 0.0090 | 0.0190 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416804_27FDE562 | 504990 | 499 | -85.9 | 504990 | 1005 | -92.0 | 504990 | 344 | -91.1 | 504990 | 982 |
| MR_1774416804_8B3C4E83 | 504990 | 1005 | -94.0 | 504990 | 499 | -87.3 | 504990 | 344 | -90.3 | 504990 | 982 |
| MR_1774416804_E7B6CCFA | 504990 | 499 | -88.1 | 504990 | 1005 | -91.8 | 504990 | 344 | -89.4 | 504990 | 982 |
| MR_1774416804_6FD9B2E3 | 504990 | 499 | -88.6 | 504990 | 1005 | -91.4 | 504990 | 344 | -89.7 | 504990 | 982 |
| MR_1774416804_B11EF48A | 504990 | 1005 | -93.6 | 504990 | 499 | -85.1 | 504990 | 344 | -90.5 | 504990 | 982 |
| MR_1774416804_4C488149 | 504990 | 1005 | -90.3 | 504990 | 499 | -86.9 | 504990 | 344 | -89.7 | 504990 | 982 |
| MR_1774416804_39CA6F15 | 504990 | 499 | -87.6 | 504990 | 1005 | -93.8 | 504990 | 344 | -91.4 | 504990 | 982 |
| MR_1774416804_9E0AA6BA | 504990 | 499 | -86.7 | 504990 | 1005 | -93.0 | 504990 | 344 | -91.5 | 504990 | 982 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1951: `770a72d8-981...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `770a72d8-981a-4475-9170-7e375799b610` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279013_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1951] topology](images/train_1951.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3279013_4 by 5 degrees
- `C2`: Increase A3 Offset threshold for 3236376_3
- `C3`: Lift the tilt angle  of 3236376_3 by 1 degrees
- `C4`: Increase A3 Offset threshold for 3279013_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236376_3
- `C6`: Adjust the azimuth of 3279013_4 by 22 degrees
- `C7`: Increase transmission power for 3236376_3
- `C8`: Add neighbor relationship between 3234733_13 and 3236376_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236376_3
- `C10`: Decrease A3 Offset threshold for 3236376_3
- `C11`: Decrease A3 Offset threshold for 3279013_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279013_4 **← 정답**
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279013_4
- `C14`: Press down the tilt angle  of 3236376_3 by 1 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Add neighbor relationship between 3279013_4 and 3236376_3
- `C17`: Adjust the azimuth of 3236376_3 by 44 degrees
- `C18`: Increase transmission power for 3279013_4
- `C19`: Check test server and transmission issues
- `C20`: Decrease transmission power for 3279013_4
- `C21`: Press down the tilt angle of 3279013_4 by 5 degrees
- `C22`: Decrease transmission power for 3236376_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.132 | MS1 | 121.4656642107 | 31.1446231279 | 820 | 504990 | -93.41 | 10.64 | 534.62 | 0.16 | 2.83 | 1570 |
| 2024-09-20 22:21:32.561 | MS1 | 121.4656770368 | 31.1446322172 | 982 | 504990 | -95.92 | 12.67 | 389.47 | 0.10 | 2.65 | 1576 |
| 2024-09-20 22:21:33.778 | MS1 | 121.4656728551 | 31.1446372453 | 535 | 504990 | -93.63 | 13.01 | 507.48 | 0.01 | 2.50 | 1566 |
| 2024-09-20 22:21:34.428 | MS1 | 121.4656675203 | 31.1446294987 | 963 | 152650 | -93.14 | 2.27 | 66.57 | 0.16 | 1.67 | 916 |
| 2024-09-20 22:21:35.305 | MS1 | 121.4656721955 | 31.1446275354 | 146 | 152650 | -88.45 | 7.88 | 74.46 | 0.05 | 1.99 | 960 |
| 2024-09-20 22:21:36.742 | MS1 | 121.4656723417 | 31.1446360296 | 121 | 152650 | -93.80 | 2.29 | 80.18 | 0.17 | 1.66 | 993 |
| 2024-09-20 22:21:37.932 | MS1 | 121.4656619374 | 31.1446229414 | 406 | 152650 | -96.14 | 7.30 | 64.15 | 0.08 | 1.88 | 980 |
| 2024-09-20 22:21:38.380 | MS1 | 121.4656745621 | 31.1446368265 | 963 | 152650 | -95.05 | 2.08 | 49.46 | 0.11 | 1.69 | 901 |
| 2024-09-20 22:21:39.466 | MS1 | 121.4656606802 | 31.1446285883 | 146 | 152650 | -89.98 | 5.37 | 78.91 | 0.11 | 1.92 | 939 |
| 2024-09-20 22:21:40.123 | MS1 | 121.4656766397 | 31.1446292334 | 121 | 152650 | -87.14 | 4.10 | 58.66 | 0.09 | 2.71 | 1588 |
| 2024-09-20 22:21:41.932 | MS1 | 121.4656679091 | 31.1446279423 | 406 | 152650 | -87.37 | 5.50 | 82.17 | 0.12 | 2.72 | 1592 |
| 2024-09-20 22:21:42.931 | MS1 | 121.4656757040 | 31.1446376459 | 963 | 152650 | -94.92 | 5.47 | 68.48 | 0.12 | 2.57 | 1597 |

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
| 3212327 | 6 | 121.4662468578 | 31.1528555162 | 30 | 13 | 8 | 0.1 | TDD | 535 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3221609 | 12 | 121.4682999439 | 31.1553473452 | 149 | 6 | 4 | 8.8 | FDD | 406 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3226293 | 8 | 121.4649128114 | 31.1523235480 | 175 | 12 | 10 | 0.9 | FDD | 963 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3234733 | 13 | 121.4734002608 | 31.1522291173 | 264 | 0 | 7 | 8.2 | FDD | 121 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3236376 | 3 | 121.4689356072 | 31.1487080846 | 258 | 1 | 3 | 2.4 | TDD | 719 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3241389 | 2 | 121.4651830240 | 31.1458171646 | 204 | 5 | 1 | 29.5 | TDD | 420 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3243285 | 11 | 121.4715112492 | 31.1522714696 | 41 | 1 | 3 | 6.4 | FDD | 146 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3243574 | 9 | 121.4730254163 | 31.1448914899 | 184 | 12 | 7 | 22.7 | FDD | 938 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3258865 | 1 | 121.4643125922 | 31.1549461002 | 116 | 8 | 11 | 3.5 | TDD | 224 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3259202 | 10 | 121.4690062551 | 31.1513987812 | 145 | 5 | 12 | 2.3 | FDD | 912 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3259307 | 7 | 121.4661112703 | 31.1538206430 | 53 | 0 | 8 | 15.0 | FDD | 96 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3261921 | 5 | 121.4680191547 | 31.1528132636 | 48 | 1 | 10 | 12.0 | TDD | 982 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3279013 | 4 | 121.4750765610 | 31.1468384605 | 233 | 4 | 10 | 13.5 | TDD | 820 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.578 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.602 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.703 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.703 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.428 | NREventA2 | measId:1;ServCellPCI:119;Se... |
| 2024-09-20 22:21:35.559 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.811 | NREventA5 | measId:3;ServCellPCI:119;Se... |
| 2024-09-20 22:21:35.883 | NRHandoverAttempt | SourcePCI:119;SourceNR-ARFC... |
| 2024-09-20 22:21:35.925 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.936 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.059 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.059 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258865 | 1 | 19.1653 | 14.5172 | -115.3142 | 10.0130 | 147.6905 | 0.0037 | 0.0112 |
| 2024_09_20 22:00 | 3241389 | 2 | 15.3059 | 15.9716 | -114.7182 | 13.4475 | 195.1537 | 0.0036 | 0.0131 |
| 2024_09_20 22:00 | 3236376 | 3 | 8.4569 | 17.7572 | -114.0773 | 15.7067 | 84.6542 | 0.0162 | 0.0183 |
| 2024_09_20 22:00 | 3279013 | 4 | 7.9700 | 10.0449 | -115.2487 | 12.4148 | 80.2718 | 0.0062 | 0.0028 |
| 2024_09_20 22:00 | 3261921 | 5 | 19.1153 | 11.0716 | -116.4457 | 8.5686 | 117.0226 | 0.0187 | 0.0050 |
| 2024_09_20 22:00 | 3212327 | 6 | 6.2440 | 7.2383 | -117.8385 | 7.3560 | 192.1157 | 0.0048 | 0.0095 |
| 2024_09_20 22:00 | 3259307 | 7 | 17.7206 | 6.3542 | -116.3861 | 4.1548 | 23.3782 | 0.0075 | 0.0065 |
| 2024_09_20 22:00 | 3226293 | 8 | 7.9164 | 10.5478 | -117.8389 | 3.4652 | 50.4997 | 0.0028 | 0.0089 |
| 2024_09_20 22:00 | 3243574 | 9 | 19.7757 | 18.1955 | -115.6903 | 3.2755 | 26.2370 | 0.0004 | 0.0128 |
| 2024_09_20 22:00 | 3259202 | 10 | 17.9603 | 15.8634 | -115.0273 | 3.2466 | 21.1249 | 0.0065 | 0.0152 |
| 2024_09_20 22:00 | 3243285 | 11 | 7.4319 | 19.1470 | -114.4822 | 4.2399 | 38.0423 | 0.0105 | 0.0080 |
| 2024_09_20 22:00 | 3221609 | 12 | 12.9406 | 11.5573 | -117.7793 | 3.2823 | 20.9592 | 0.0048 | 0.0077 |
| 2024_09_20 22:00 | 3234733 | 13 | 17.4813 | 19.2744 | -114.7143 | 4.9769 | 50.4931 | 0.0007 | 0.0162 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415998_70827E19 | 152650 | 963 | -93.8 | 152650 | 938 | -98.9 | 152650 | 912 | -102.6 | 152650 | 96 |
| MR_1774415998_29C81DDA | 152650 | 963 | -92.9 | 152650 | 938 | -96.6 | 152650 | 912 | -104.7 | 152650 | 96 |
| MR_1774415998_E38F0A39 | 152650 | 963 | -94.2 | 152650 | 938 | -96.9 | 152650 | 912 | -105.1 | 152650 | 96 |
| MR_1774415998_ABB3FCB3 | 152650 | 963 | -92.3 | 152650 | 938 | -96.0 | 152650 | 912 | -105.7 | 152650 | 96 |
| MR_1774415998_3681D3D7 | 504990 | 535 | -91.7 | 504990 | 719 | -92.6 | 504990 | 420 | -96.3 | 504990 | 224 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1952: `b5354f10-c2f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b5354f10-c2ff-4605-886c-d75e25e9d355` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217743_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1952] topology](images/train_1952.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3217743_1 and 3249832_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249832_2
- `C3`: Add neighbor relationship between 3245704_9 and 3249832_2
- `C4`: Increase transmission power for 3249832_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249832_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217743_1 **← 정답**
- `C7`: Increase A3 Offset threshold for 3217743_1
- `C8`: Adjust the azimuth of 3217743_1 by 49 degrees
- `C9`: Check test server and transmission issues
- `C10`: Lift the tilt angle  of 3249832_2 by 5 degrees
- `C11`: Decrease transmission power for 3249832_2
- `C12`: Lift the tilt angle of 3217743_1 by 2 degrees
- `C13`: Decrease A3 Offset threshold for 3217743_1
- `C14`: Increase A3 Offset threshold for 3249832_2
- `C15`: Press down the tilt angle  of 3249832_2 by 5 degrees
- `C16`: Press down the tilt angle of 3217743_1 by 2 degrees
- `C17`: Adjust the azimuth of 3249832_2 by 50 degrees
- `C18`: Decrease A3 Offset threshold for 3249832_2
- `C19`: Increase transmission power for 3217743_1
- `C20`: Decrease transmission power for 3217743_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217743_1
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.564 | MS1 | 121.4656606471 | 31.1446256769 | 417 | 504990 | -95.76 | 9.40 | 472.11 | 0.11 | 2.99 | 1598 |
| 2024-09-20 22:21:32.613 | MS1 | 121.4656583167 | 31.1446187242 | 603 | 504990 | -93.99 | 11.35 | 583.04 | 0.08 | 2.09 | 1563 |
| 2024-09-20 22:21:33.648 | MS1 | 121.4656589547 | 31.1446343381 | 466 | 504990 | -94.84 | 12.57 | 342.07 | 0.17 | 2.45 | 1586 |
| 2024-09-20 22:21:34.200 | MS1 | 121.4656626136 | 31.1446227794 | 507 | 152650 | -89.68 | 6.68 | 82.82 | 0.05 | 1.60 | 991 |
| 2024-09-20 22:21:35.432 | MS1 | 121.4656749497 | 31.1446256416 | 253 | 152650 | -87.30 | 7.14 | 53.07 | 0.05 | 1.65 | 909 |
| 2024-09-20 22:21:36.279 | MS1 | 121.4656623093 | 31.1446199671 | 251 | 152650 | -87.74 | 2.07 | 61.12 | 0.18 | 1.94 | 963 |
| 2024-09-20 22:21:37.535 | MS1 | 121.4656754049 | 31.1446331702 | 212 | 152650 | -95.85 | 6.09 | 58.94 | 0.13 | 1.67 | 1000 |
| 2024-09-20 22:21:38.535 | MS1 | 121.4656621266 | 31.1446275169 | 507 | 152650 | -87.66 | 5.69 | 89.93 | 0.04 | 1.86 | 914 |
| 2024-09-20 22:21:39.769 | MS1 | 121.4656758635 | 31.1446255307 | 253 | 152650 | -89.79 | 7.15 | 52.74 | 0.12 | 1.81 | 921 |
| 2024-09-20 22:21:40.402 | MS1 | 121.4656583207 | 31.1446185088 | 251 | 152650 | -96.78 | 7.49 | 91.87 | 0.06 | 2.20 | 1585 |
| 2024-09-20 22:21:41.853 | MS1 | 121.4656703212 | 31.1446361142 | 212 | 152650 | -87.68 | 5.13 | 51.98 | 0.16 | 2.07 | 1568 |
| 2024-09-20 22:21:42.990 | MS1 | 121.4656754384 | 31.1446346035 | 507 | 152650 | -88.89 | 4.82 | 57.15 | 0.16 | 2.25 | 1586 |

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
| 3213961 | 12 | 121.4653430278 | 31.1493324550 | 41 | 11 | 7 | 0.7 | FDD | 507 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3214561 | 7 | 121.4714065343 | 31.1458901333 | 99 | 1 | 9 | 28.9 | FDD | 233 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3217743 | 1 | 121.4654864974 | 31.1475896329 | 226 | 1 | 10 | 8.4 | TDD | 417 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3226278 | 5 | 121.4740784874 | 31.1456060263 | 327 | 3 | 7 | 20.8 | TDD | 470 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3226312 | 4 | 121.4667392856 | 31.1518680998 | 144 | 11 | 0 | 27.7 | TDD | 466 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3234726 | 11 | 121.4732171482 | 31.1457815221 | 64 | 13 | 8 | 11.8 | FDD | 212 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3238046 | 3 | 121.4675411608 | 31.1517822588 | 197 | 3 | 12 | 18.3 | TDD | 584 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3245704 | 9 | 121.4733465778 | 31.1515097079 | 314 | 9 | 11 | 7.4 | FDD | 251 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3246380 | 13 | 121.4682433117 | 31.1452621435 | 289 | 10 | 12 | 19.2 | FDD | 253 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3249832 | 2 | 121.4749670287 | 31.1548599163 | 168 | 5 | 3 | 9.2 | TDD | 358 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3255989 | 10 | 121.4754912976 | 31.1532756135 | 52 | 2 | 3 | 17.8 | FDD | 499 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3260871 | 6 | 121.4710817284 | 31.1512471351 | 117 | 8 | 12 | 15.7 | TDD | 603 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3275737 | 8 | 121.4748950943 | 31.1441869787 | 79 | 7 | 11 | 7.3 | FDD | 649 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |

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
| 2024-09-20 22:21:31.446 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.467 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.613 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.613 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.250 | NREventA2 | measId:1;ServCellPCI:310;Se... |
| 2024-09-20 22:21:35.398 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.691 | NREventA5 | measId:3;ServCellPCI:310;Se... |
| 2024-09-20 22:21:35.724 | NRHandoverAttempt | SourcePCI:310;SourceNR-ARFC... |
| 2024-09-20 22:21:35.760 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.772 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.911 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.911 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217743 | 1 | 6.1034 | 19.5263 | -114.1230 | 17.7914 | 85.5390 | 0.0122 | 0.0196 |
| 2024_09_20 22:00 | 3249832 | 2 | 5.4628 | 6.6832 | -114.4353 | 16.0339 | 95.3401 | 0.0147 | 0.0066 |
| 2024_09_20 22:00 | 3238046 | 3 | 18.7568 | 10.3326 | -117.3681 | 16.7403 | 87.9012 | 0.0163 | 0.0069 |
| 2024_09_20 22:00 | 3226312 | 4 | 8.7333 | 9.0766 | -116.8518 | 10.5962 | 91.8474 | 0.0098 | 0.0125 |
| 2024_09_20 22:00 | 3226278 | 5 | 8.1057 | 6.0010 | -115.8863 | 19.3858 | 132.3608 | 0.0165 | 0.0039 |
| 2024_09_20 22:00 | 3260871 | 6 | 6.8066 | 16.3560 | -114.5864 | 14.0666 | 134.4659 | 0.0093 | 0.0151 |
| 2024_09_20 22:00 | 3214561 | 7 | 14.1350 | 12.9011 | -114.2216 | 3.3478 | 52.2811 | 0.0173 | 0.0161 |
| 2024_09_20 22:00 | 3275737 | 8 | 19.7841 | 18.1914 | -114.2546 | 3.9929 | 20.7828 | 0.0052 | 0.0138 |
| 2024_09_20 22:00 | 3245704 | 9 | 10.2207 | 18.4949 | -116.1983 | 3.6390 | 49.3544 | 0.0114 | 0.0044 |
| 2024_09_20 22:00 | 3255989 | 10 | 15.7942 | 14.7342 | -116.4433 | 3.3775 | 38.9855 | 0.0160 | 0.0196 |
| 2024_09_20 22:00 | 3234726 | 11 | 18.7525 | 11.8843 | -114.6650 | 4.7924 | 20.1925 | 0.0074 | 0.0026 |
| 2024_09_20 22:00 | 3213961 | 12 | 6.0477 | 16.5841 | -116.5234 | 3.5923 | 41.8697 | 0.0130 | 0.0141 |
| 2024_09_20 22:00 | 3246380 | 13 | 16.7902 | 14.5260 | -116.0597 | 4.5479 | 55.5972 | 0.0110 | 0.0159 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413637_6E8C28EA | 152650 | 507 | -88.8 | 152650 | 233 | -96.8 | 152650 | 499 | -99.3 | 152650 | 649 |
| MR_1774413637_75F5DB1C | 504990 | 466 | -95.1 | 504990 | 358 | -97.1 | 504990 | 470 | -102.0 | 504990 | 584 |
| MR_1774413637_CB830AAE | 504990 | 466 | -93.0 | 504990 | 358 | -97.2 | 504990 | 470 | -99.5 | 504990 | 584 |
| MR_1774413637_5D77568F | 152650 | 507 | -90.4 | 152650 | 233 | -94.7 | 152650 | 499 | -101.2 | 152650 | 649 |
| MR_1774413637_A4ED14A7 | 504990 | 466 | -93.5 | 504990 | 358 | -96.8 | 504990 | 470 | -102.4 | 504990 | 584 |
| MR_1774413637_4DBB9507 | 504990 | 466 | -95.3 | 504990 | 358 | -96.5 | 504990 | 470 | -101.5 | 504990 | 584 |
| MR_1774413637_DE824FCA | 504990 | 466 | -94.2 | 504990 | 358 | -97.4 | 504990 | 470 | -102.4 | 504990 | 584 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1953: `30a2a3fc-941...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `30a2a3fc-9416-4e7c-a69e-d6005bdeb05b` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Lift the tilt angle  of 3256629_3 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1953] topology](images/train_1953.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3273643_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276931_1
- `C3`: Adjust the azimuth of 3256629_3 by 14 degrees
- `C4`: Decrease transmission power for 3273643_2
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273643_2
- `C7`: Adjust the azimuth of 3273643_2 by 17 degrees
- `C8`: Decrease A3 Offset threshold for 3276931_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273643_2
- `C10`: Decrease transmission power for 3276931_1
- `C11`: Check test server and transmission issues
- `C12`: Increase transmission power for 3276931_1
- `C13`: Increase A3 Offset threshold for 3273643_2
- `C14`: Press down the tilt angle of 3273643_2 by 2 degrees
- `C15`: Lift the tilt angle of 3273643_2 by 2 degrees
- `C16`: Add neighbor relationship between 3256629_3 and 3276931_1
- `C17`: Increase A3 Offset threshold for 3276931_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276931_1
- `C19`: Lift the tilt angle  of 3256629_3 by 7 degrees **← 정답**
- `C20`: Add neighbor relationship between 3273643_2 and 3276931_1
- `C21`: Press down the tilt angle  of 3256629_3 by 7 degrees
- `C22`: Decrease A3 Offset threshold for 3273643_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.581 | MS1 | 121.4656679565 | 31.1446314136 | 194 | 504990 | -85.97 | 12.91 | 319.33 | 0.19 | 2.24 | 1566 |
| 2024-09-20 22:21:32.198 | MS1 | 121.4656625555 | 31.1446355058 | 194 | 504990 | -90.47 | 16.78 | 551.44 | 0.11 | 2.46 | 1563 |
| 2024-09-20 22:21:33.792 | MS1 | 121.4656695846 | 31.1446225815 | 194 | 504990 | -85.14 | 13.49 | 392.19 | 0.03 | 2.09 | 1574 |
| 2024-09-20 22:21:34.226 | MS1 | 121.4656702355 | 31.1446259913 | 194 | 504990 | -86.32 | 17.42 | 55.50 | 0.14 | 2.01 | 1574 |
| 2024-09-20 22:21:35.357 | MS1 | 121.4656722910 | 31.1446238190 | 194 | 504990 | -85.73 | 16.34 | 93.93 | 0.00 | 2.05 | 1594 |
| 2024-09-20 22:21:36.507 | MS1 | 121.4656590778 | 31.1446329169 | 194 | 504990 | -86.87 | 13.47 | 65.46 | 0.14 | 2.55 | 1578 |
| 2024-09-20 22:21:37.241 | MS1 | 121.4656599795 | 31.1446231752 | 194 | 504990 | -92.89 | 11.98 | 103.89 | 0.14 | 2.08 | 1585 |
| 2024-09-20 22:21:38.950 | MS1 | 121.4656749681 | 31.1446333285 | 194 | 504990 | -89.15 | 12.81 | 53.35 | 0.08 | 2.16 | 1596 |
| 2024-09-20 22:21:39.698 | MS1 | 121.4656744508 | 31.1446325479 | 194 | 504990 | -93.34 | 12.29 | 97.27 | 0.06 | 2.31 | 1598 |
| 2024-09-20 22:21:40.835 | MS1 | 121.4656753328 | 31.1446259300 | 194 | 504990 | -92.71 | 7.19 | 314.73 | 0.02 | 3.00 | 1578 |
| 2024-09-20 22:21:41.533 | MS1 | 121.4656614669 | 31.1446260592 | 194 | 504990 | -90.51 | 12.19 | 593.89 | 0.04 | 2.30 | 1577 |
| 2024-09-20 22:21:42.882 | MS1 | 121.4656653746 | 31.1446264204 | 194 | 504990 | -89.37 | 8.18 | 424.49 | 0.06 | 2.70 | 1583 |

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
| 3212790 | 4 | 121.4709538120 | 31.1521645319 | 200 | 0 | 2 | 16.2 | TDD | 437 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3256629 | 3 | 121.4672946486 | 31.1483869639 | 338 | 10 | 1 | 24.5 | TDD | 636 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3273643 | 2 | 121.4759128777 | 31.1526586893 | 211 | 1 | 12 | 28.5 | TDD | 194 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3276931 | 1 | 121.4674535163 | 31.1549144753 | 174 | 6 | 11 | 25.4 | TDD | 545 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.486 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.510 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.656 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.656 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.333 | NREventA3 | measId:2;ServCellPCI:109;Se... |
| 2024-09-20 22:21:38.573 | NRHandoverAttempt | SourcePCI:109;SourceNR-ARFC... |
| 2024-09-20 22:21:38.612 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.625 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.735 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.735 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276931 | 1 | 14.5416 | 8.2378 | -117.2317 | 18.4021 | 164.2676 | 0.0196 | 0.0115 |
| 2024_09_20 22:00 | 3273643 | 2 | 90.6843 | 92.1510 | -116.4828 | 17.6257 | 182.8017 | 0.0135 | 0.0183 |
| 2024_09_20 22:00 | 3256629 | 3 | 7.2537 | 7.0136 | -115.2534 | 6.6632 | 89.4598 | 0.0182 | 0.0108 |
| 2024_09_20 22:00 | 3212790 | 4 | 18.8291 | 5.0184 | -114.9264 | 13.5927 | 170.1992 | 0.0193 | 0.0104 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416615_8BDF02A4 | 504990 | 194 | -85.1 | 504990 | 545 | -94.4 | 504990 | 636 | -97.4 | 504990 | 437 |
| MR_1774416615_6326F88F | 504990 | 194 | -85.5 | 504990 | 545 | -96.5 | 504990 | 636 | -94.4 | 504990 | 437 |
| MR_1774416615_09E4A727 | 504990 | 194 | -85.3 | 504990 | 545 | -95.0 | 504990 | 636 | -95.6 | 504990 | 437 |
| MR_1774416615_018F5216 | 504990 | 194 | -85.9 | 504990 | 545 | -96.4 | 504990 | 636 | -94.5 | 504990 | 437 |
| MR_1774416615_1A58C99B | 504990 | 194 | -84.4 | 504990 | 545 | -95.6 | 504990 | 636 | -97.2 | 504990 | 437 |
| MR_1774416615_077C0ADC | 504990 | 194 | -86.4 | 504990 | 545 | -94.5 | 504990 | 636 | -96.6 | 504990 | 437 |
| MR_1774416615_F9B474B5 | 504990 | 194 | -84.6 | 504990 | 545 | -95.2 | 504990 | 636 | -94.8 | 504990 | 437 |
| MR_1774416615_38136FD5 | 504990 | 194 | -87.8 | 504990 | 545 | -95.4 | 504990 | 636 | -94.1 | 504990 | 437 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1954: `1a0ad911-981...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1a0ad911-981b-4962-9d70-d3e1166e3bfe` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1954] topology](images/train_1954.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3236188_2
- `C2`: Lift the tilt angle of 3231204_1 by 4 degrees
- `C3`: Decrease A3 Offset threshold for 3236188_2
- `C4`: Decrease transmission power for 3231204_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231204_1
- `C6`: Check test server and transmission issues
- `C7`: Add neighbor relationship between 3231204_1 and 3236188_2
- `C8`: Press down the tilt angle  of 3236188_2 by 10 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236188_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231204_1
- `C11`: Increase A3 Offset threshold for 3231204_1
- `C12`: Increase transmission power for 3236188_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236188_2
- `C14`: Lift the tilt angle  of 3236188_2 by 10 degrees
- `C15`: Increase A3 Offset threshold for 3236188_2
- `C16`: Insufficient data; more data is needed for judgment. **← 정답**
- `C17`: Add neighbor relationship between 3247763_4 and 3236188_2
- `C18`: Press down the tilt angle of 3231204_1 by 4 degrees
- `C19`: Adjust the azimuth of 3231204_1 by 50 degrees
- `C20`: Decrease A3 Offset threshold for 3231204_1
- `C21`: Adjust the azimuth of 3236188_2 by 50 degrees
- `C22`: Increase transmission power for 3231204_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.736 | MS1 | 121.4656748735 | 31.1446312842 | 616 | 504990 | -91.78 | 15.29 | 589.52 | 0.14 | 2.12 | 1592 |
| 2024-09-20 22:21:32.716 | MS1 | 121.4656621236 | 31.1446264172 | 616 | 504990 | -85.52 | 12.10 | 480.16 | 0.07 | 2.98 | 1574 |
| 2024-09-20 22:21:33.324 | MS1 | 121.4656729057 | 31.1446334995 | 616 | 504990 | -86.10 | 12.28 | 575.17 | 0.05 | 2.71 | 1571 |
| 2024-09-20 22:21:34.927 | MS1 | 121.4656614471 | 31.1446181359 | 616 | 504990 | -91.52 | 12.85 | 88.98 | 0.16 | 2.50 | 1586 |
| 2024-09-20 22:21:35.396 | MS1 | 121.4656599550 | 31.1446226148 | 616 | 504990 | -87.11 | 13.94 | 74.26 | 0.01 | 2.26 | 1582 |
| 2024-09-20 22:21:36.735 | MS1 | 121.4656624491 | 31.1446302011 | 616 | 504990 | -91.25 | 17.97 | 92.71 | 0.04 | 2.77 | 1561 |
| 2024-09-20 22:21:37.541 | MS1 | 121.4656738930 | 31.1446213456 | 616 | 504990 | -90.51 | 7.47 | 56.72 | 0.06 | 2.01 | 1593 |
| 2024-09-20 22:21:38.350 | MS1 | 121.4656667653 | 31.1446275473 | 616 | 504990 | -91.05 | 9.87 | 78.88 | 0.18 | 2.34 | 1560 |
| 2024-09-20 22:21:39.534 | MS1 | 121.4656772881 | 31.1446346868 | 616 | 504990 | -90.83 | 9.30 | 82.16 | 0.14 | 2.58 | 1598 |
| 2024-09-20 22:21:40.967 | MS1 | 121.4656687927 | 31.1446241914 | 616 | 504990 | -92.34 | 7.29 | 352.95 | 0.02 | 2.35 | 1598 |
| 2024-09-20 22:21:41.430 | MS1 | 121.4656654060 | 31.1446337132 | 616 | 504990 | -92.14 | 9.76 | 483.74 | 0.13 | 2.56 | 1562 |
| 2024-09-20 22:21:42.823 | MS1 | 121.4656707705 | 31.1446318067 | 616 | 504990 | -89.89 | 8.94 | 463.93 | 0.11 | 2.32 | 1595 |

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
| 3231204 | 1 | 121.4719729699 | 31.1455500230 | 185 | 1 | 12 | 33.3 | TDD | 616 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3235198 | 3 | 121.4721888886 | 31.1544042066 | 310 | 13 | 12 | 43.5 | TDD | 38 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3236188 | 2 | 121.4758347794 | 31.1481196984 | 301 | 10 | 1 | 20.9 | TDD | 173 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3247763 | 4 | 121.4693850487 | 31.1504049632 | 326 | 3 | 7 | 50.0 | TDD | 669 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.604 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.622 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.741 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.741 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.435 | NREventA3 | measId:2;ServCellPCI:929;Se... |
| 2024-09-20 22:21:38.675 | NRHandoverAttempt | SourcePCI:929;SourceNR-ARFC... |
| 2024-09-20 22:21:38.725 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.735 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.874 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.874 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3231204 | 1 | 88.0153 | 78.4028 | -117.4167 | 17.6316 | 183.8869 | 0.0148 | 0.0078 |
| 2024_09_19 22:00 | 3236188 | 2 | 84.5240 | 77.5035 | -114.3634 | 12.8294 | 86.8550 | 0.0133 | 0.0003 |
| 2024_09_19 22:00 | 3235198 | 3 | 84.9516 | 81.3304 | -116.4102 | 18.9259 | 83.7942 | 0.0168 | 0.0120 |
| 2024_09_19 22:00 | 3247763 | 4 | 88.7428 | 89.3312 | -114.5079 | 19.2576 | 196.5514 | 0.0054 | 0.0126 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414346_C54B6241 | 504990 | 616 | -91.2 | 504990 | 173 | -101.6 | 504990 | 669 | -103.3 | 504990 | 38 |
| MR_1774414346_5F4DEBD0 | 504990 | 616 | -91.5 | 504990 | 173 | -98.8 | 504990 | 669 | -101.9 | 504990 | 38 |
| MR_1774414346_C8D584A6 | 504990 | 616 | -90.6 | 504990 | 173 | -99.3 | 504990 | 669 | -103.6 | 504990 | 38 |
| MR_1774414346_989003C7 | 504990 | 616 | -91.9 | 504990 | 173 | -99.6 | 504990 | 669 | -103.0 | 504990 | 38 |
| MR_1774414346_7786874E | 504990 | 616 | -92.0 | 504990 | 173 | -100.9 | 504990 | 669 | -102.8 | 504990 | 38 |
| MR_1774414346_DC41874E | 504990 | 616 | -89.6 | 504990 | 173 | -99.2 | 504990 | 669 | -103.5 | 504990 | 38 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1955: `73eb26df-276...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `73eb26df-276c-41ad-bb17-c2b692e67922` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Add neighbor relationship between 3279897_1 and 3250141_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1955] topology](images/train_1955.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3250141_2
- `C2`: Decrease transmission power for 3250141_2
- `C3`: Press down the tilt angle of 3279897_1 by 10 degrees
- `C4`: Adjust the azimuth of 3250141_2 by 13 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279897_1
- `C6`: Press down the tilt angle  of 3250141_2 by 3 degrees
- `C7`: Add neighbor relationship between 3239733_4 and 3250141_2
- `C8`: Add neighbor relationship between 3279897_1 and 3250141_2 **← 정답**
- `C9`: Increase A3 Offset threshold for 3250141_2
- `C10`: Lift the tilt angle of 3279897_1 by 10 degrees
- `C11`: Decrease transmission power for 3279897_1
- `C12`: Adjust the azimuth of 3279897_1 by 50 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease A3 Offset threshold for 3279897_1
- `C15`: Increase A3 Offset threshold for 3279897_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250141_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250141_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279897_1
- `C19`: Decrease A3 Offset threshold for 3250141_2
- `C20`: Increase transmission power for 3279897_1
- `C21`: Lift the tilt angle  of 3250141_2 by 3 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.920 | MS1 | 121.4656768244 | 31.1446302392 | 976 | 504990 | -77.22 | 17.17 | 534.41 | 0.10 | 2.03 | 1569 |
| 2024-09-20 22:21:32.983 | MS1 | 121.4656613560 | 31.1446263575 | 976 | 504990 | -79.92 | 16.09 | 560.10 | 0.01 | 2.68 | 1586 |
| 2024-09-20 22:21:33.263 | MS1 | 121.4656666357 | 31.1446220592 | 976 | 504990 | -84.97 | 15.46 | 580.80 | 0.05 | 2.89 | 1598 |
| 2024-09-20 22:21:34.195 | MS1 | 121.4656696331 | 31.1446355679 | 976 | 504990 | -91.80 | -1.57 | 51.90 | 0.12 | 1.15 | 1589 |
| 2024-09-20 22:21:35.241 | MS1 | 121.4656706114 | 31.1446232561 | 976 | 504990 | -86.03 | -1.09 | 57.33 | 0.07 | 1.45 | 1592 |
| 2024-09-20 22:21:36.707 | MS1 | 121.4656693151 | 31.1446218260 | 976 | 504990 | -88.91 | -3.42 | 73.01 | 0.19 | 1.25 | 1576 |
| 2024-09-20 22:21:37.629 | MS1 | 121.4656643109 | 31.1446295571 | 976 | 504990 | -93.77 | -3.79 | 72.29 | 0.17 | 1.14 | 1593 |
| 2024-09-20 22:21:38.287 | MS1 | 121.4656647937 | 31.1446270204 | 976 | 504990 | -77.19 | 12.03 | 348.93 | 0.09 | 1.06 | 1588 |
| 2024-09-20 22:21:39.556 | MS1 | 121.4656582174 | 31.1446262189 | 976 | 504990 | -83.93 | 17.10 | 294.20 | 0.09 | 1.16 | 1572 |
| 2024-09-20 22:21:40.645 | MS1 | 121.4656750890 | 31.1446318027 | 976 | 504990 | -78.47 | 12.77 | 369.02 | 0.14 | 2.86 | 1564 |
| 2024-09-20 22:21:41.930 | MS1 | 121.4656682645 | 31.1446212829 | 976 | 504990 | -83.36 | 16.67 | 374.89 | 0.03 | 2.50 | 1599 |
| 2024-09-20 22:21:42.121 | MS1 | 121.4656612158 | 31.1446261886 | 976 | 504990 | -81.98 | 15.04 | 549.45 | 0.19 | 2.31 | 1580 |

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
| 3239733 | 4 | 121.4677702058 | 31.1524338728 | 185 | 14 | 4 | 26.3 | TDD | 519 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3250141 | 2 | 121.4712885562 | 31.1524340847 | 199 | 2 | 4 | 20.3 | TDD | 810 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3259887 | 3 | 121.4745535723 | 31.1462207908 | 310 | 6 | 0 | 21.2 | TDD | 597 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3279897 | 1 | 121.4640243786 | 31.1447833809 | 271 | 5 | 1 | 39.9 | TDD | 976 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.347 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.364 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.466 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.466 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.174 | NREventA3 | measId:2;ServCellPCI:922;Se... |
| 2024-09-20 22:21:36.174 | NREventA3 | measId:2;ServCellPCI:922;Se... |
| 2024-09-20 22:21:37.174 | NREventA3 | measId:2;ServCellPCI:922;Se... |
| 2024-09-20 22:21:39.674 | NRRRCReestablishAttempt | PCI:922 |
| 2024-09-20 22:21:39.692 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.706 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.850 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.850 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279897 | 1 | 9.9569 | 19.6100 | -117.4652 | 17.4555 | 112.5497 | 0.0100 | 0.1169 |
| 2024_09_20 22:00 | 3250141 | 2 | 7.7013 | 5.1854 | -116.9846 | 10.5004 | 96.0679 | 0.0187 | 0.0063 |
| 2024_09_20 22:00 | 3259887 | 3 | 13.5975 | 10.0647 | -115.8244 | 19.4064 | 98.2942 | 0.0083 | 0.0043 |
| 2024_09_20 22:00 | 3239733 | 4 | 7.3919 | 16.4269 | -117.6308 | 16.1574 | 161.4634 | 0.0027 | 0.0120 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415628_455A17B3 | 504990 | 810 | -86.9 | 504990 | 976 | -93.4 | 504990 | 519 | -90.7 | 504990 | 597 |
| MR_1774415628_D5BDB489 | 504990 | 976 | -91.0 | 504990 | 810 | -87.1 | 504990 | 519 | -92.8 | 504990 | 597 |
| MR_1774415628_CA90E70E | 504990 | 810 | -86.4 | 504990 | 976 | -90.0 | 504990 | 519 | -92.2 | 504990 | 597 |
| MR_1774415628_187691FD | 504990 | 810 | -85.7 | 504990 | 976 | -91.9 | 504990 | 519 | -91.7 | 504990 | 597 |
| MR_1774415628_8DFD8250 | 504990 | 976 | -90.5 | 504990 | 810 | -89.3 | 504990 | 519 | -93.0 | 504990 | 597 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1956: `10bbe13d-290...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `10bbe13d-290e-4ab8-b020-14f89efad775` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245145_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1956] topology](images/train_1956.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3245145_4
- `C2`: Increase A3 Offset threshold for 3245145_4
- `C3`: Increase transmission power for 3219927_2
- `C4`: Check test server and transmission issues
- `C5`: Increase transmission power for 3245145_4
- `C6`: Adjust the azimuth of 3219927_2 by 35 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219927_2
- `C8`: Decrease transmission power for 3219927_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219927_2
- `C10`: Decrease A3 Offset threshold for 3219927_2
- `C11`: Add neighbor relationship between 3251144_11 and 3219927_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245145_4
- `C13`: Add neighbor relationship between 3245145_4 and 3219927_2
- `C14`: Press down the tilt angle of 3245145_4 by 1 degrees
- `C15`: Lift the tilt angle of 3245145_4 by 1 degrees
- `C16`: Lift the tilt angle  of 3219927_2 by 3 degrees
- `C17`: Adjust the azimuth of 3245145_4 by 39 degrees
- `C18`: Increase A3 Offset threshold for 3219927_2
- `C19`: Decrease transmission power for 3245145_4
- `C20`: Press down the tilt angle  of 3219927_2 by 3 degrees
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245145_4 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.580 | MS1 | 121.4656618537 | 31.1446218253 | 462 | 504990 | -94.79 | 11.24 | 569.58 | 0.01 | 2.20 | 1584 |
| 2024-09-20 22:21:32.400 | MS1 | 121.4656746910 | 31.1446353561 | 547 | 504990 | -94.81 | 11.64 | 299.53 | 0.09 | 2.89 | 1563 |
| 2024-09-20 22:21:33.261 | MS1 | 121.4656679416 | 31.1446372028 | 420 | 504990 | -93.84 | 14.19 | 332.12 | 0.13 | 2.11 | 1571 |
| 2024-09-20 22:21:34.837 | MS1 | 121.4656648714 | 31.1446221971 | 901 | 152650 | -96.99 | 5.94 | 63.15 | 0.17 | 1.59 | 991 |
| 2024-09-20 22:21:35.417 | MS1 | 121.4656752163 | 31.1446270987 | 367 | 152650 | -89.43 | 6.86 | 80.43 | 0.17 | 1.73 | 951 |
| 2024-09-20 22:21:36.187 | MS1 | 121.4656621690 | 31.1446196942 | 885 | 152650 | -91.83 | 4.86 | 67.86 | 0.19 | 1.78 | 928 |
| 2024-09-20 22:21:37.962 | MS1 | 121.4656750076 | 31.1446180430 | 258 | 152650 | -87.60 | 5.40 | 77.54 | 0.17 | 1.87 | 917 |
| 2024-09-20 22:21:38.864 | MS1 | 121.4656696423 | 31.1446214322 | 901 | 152650 | -94.35 | 3.27 | 52.25 | 0.08 | 1.94 | 919 |
| 2024-09-20 22:21:39.609 | MS1 | 121.4656599360 | 31.1446232574 | 367 | 152650 | -88.75 | 5.75 | 93.58 | 0.01 | 1.64 | 971 |
| 2024-09-20 22:21:40.569 | MS1 | 121.4656711620 | 31.1446219931 | 885 | 152650 | -87.97 | 2.43 | 47.29 | 0.09 | 2.97 | 1570 |
| 2024-09-20 22:21:41.454 | MS1 | 121.4656703454 | 31.1446203406 | 258 | 152650 | -91.72 | 5.21 | 88.17 | 0.18 | 2.58 | 1568 |
| 2024-09-20 22:21:42.378 | MS1 | 121.4656697120 | 31.1446317163 | 901 | 152650 | -93.33 | 7.15 | 68.21 | 0.15 | 2.04 | 1570 |

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
| 3210705 | 5 | 121.4759166773 | 31.1541401916 | 104 | 1 | 7 | 8.9 | TDD | 763 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3211538 | 8 | 121.4698320621 | 31.1483434116 | 76 | 15 | 8 | 20.0 | FDD | 901 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3211916 | 7 | 121.4753392167 | 31.1507747254 | 273 | 6 | 11 | 28.6 | FDD | 258 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3212760 | 13 | 121.4667868534 | 31.1498674505 | 346 | 6 | 1 | 24.7 | FDD | 183 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3214792 | 1 | 121.4663708712 | 31.1543699002 | 82 | 9 | 6 | 9.9 | TDD | 547 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3219927 | 2 | 121.4741773354 | 31.1476185545 | 213 | 1 | 10 | 29.4 | TDD | 868 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3224872 | 6 | 121.4666589675 | 31.1528646068 | 107 | 10 | 2 | 20.5 | TDD | 831 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3245145 | 4 | 121.4733819169 | 31.1511713650 | 186 | 0 | 3 | 14.5 | TDD | 462 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3246528 | 3 | 121.4654971587 | 31.1520792380 | 116 | 15 | 3 | 13.9 | TDD | 420 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3251144 | 11 | 121.4653846871 | 31.1550572542 | 135 | 5 | 9 | 25.4 | FDD | 885 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3256089 | 10 | 121.4647252650 | 31.1500500777 | 342 | 11 | 2 | 10.9 | FDD | 367 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3260363 | 9 | 121.4664160978 | 31.1509538941 | 164 | 8 | 4 | 10.9 | FDD | 493 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3270664 | 12 | 121.4718477697 | 31.1492535534 | 64 | 3 | 5 | 3.8 | FDD | 151 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |

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
| 2024-09-20 22:21:31.012 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.112 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.112 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.856 | NREventA2 | measId:1;ServCellPCI:290;Se... |
| 2024-09-20 22:21:34.969 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.262 | NREventA5 | measId:3;ServCellPCI:290;Se... |
| 2024-09-20 22:21:35.320 | NRHandoverAttempt | SourcePCI:290;SourceNR-ARFC... |
| 2024-09-20 22:21:35.346 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.359 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.487 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.487 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214792 | 1 | 14.2111 | 17.5066 | -115.5398 | 7.1161 | 96.9350 | 0.0034 | 0.0036 |
| 2024_09_20 22:00 | 3219927 | 2 | 11.4182 | 14.3892 | -116.6855 | 12.3902 | 153.2312 | 0.0054 | 0.0069 |
| 2024_09_20 22:00 | 3246528 | 3 | 9.1008 | 7.1498 | -116.2710 | 5.6305 | 116.4996 | 0.0058 | 0.0169 |
| 2024_09_20 22:00 | 3245145 | 4 | 7.4000 | 18.7037 | -115.4615 | 5.9131 | 87.0565 | 0.0095 | 0.0126 |
| 2024_09_20 22:00 | 3210705 | 5 | 6.1797 | 15.6033 | -114.2799 | 17.3930 | 146.1752 | 0.0174 | 0.0076 |
| 2024_09_20 22:00 | 3224872 | 6 | 13.8292 | 7.1216 | -117.3005 | 6.9120 | 176.5790 | 0.0115 | 0.0125 |
| 2024_09_20 22:00 | 3211916 | 7 | 19.3998 | 15.8598 | -115.1388 | 4.8165 | 50.1012 | 0.0122 | 0.0189 |
| 2024_09_20 22:00 | 3211538 | 8 | 6.1508 | 13.5968 | -117.8479 | 3.3583 | 47.5262 | 0.0143 | 0.0113 |
| 2024_09_20 22:00 | 3260363 | 9 | 5.5436 | 6.4278 | -114.6125 | 4.8419 | 58.8660 | 0.0188 | 0.0181 |
| 2024_09_20 22:00 | 3256089 | 10 | 10.3159 | 18.9942 | -114.8809 | 4.2010 | 38.1058 | 0.0151 | 0.0154 |
| 2024_09_20 22:00 | 3251144 | 11 | 11.8987 | 14.7399 | -114.2669 | 4.3354 | 29.1694 | 0.0049 | 0.0040 |
| 2024_09_20 22:00 | 3270664 | 12 | 13.5418 | 17.2875 | -117.4176 | 3.7346 | 55.7638 | 0.0070 | 0.0131 |
| 2024_09_20 22:00 | 3212760 | 13 | 15.2751 | 9.3504 | -117.9525 | 4.1132 | 42.8143 | 0.0045 | 0.0049 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413643_42768B81 | 504990 | 420 | -93.1 | 504990 | 868 | -93.0 | 504990 | 831 | -97.6 | 504990 | 763 |
| MR_1774413643_7185A7F8 | 504990 | 420 | -94.2 | 504990 | 868 | -92.8 | 504990 | 831 | -97.1 | 504990 | 763 |
| MR_1774413643_3B9CECDA | 152650 | 901 | -98.2 | 152650 | 493 | -104.5 | 152650 | 151 | -105.6 | 152650 | 183 |
| MR_1774413643_A0715844 | 152650 | 901 | -98.9 | 152650 | 493 | -105.3 | 152650 | 151 | -105.1 | 152650 | 183 |
| MR_1774413643_F7C10B24 | 152650 | 901 | -95.4 | 152650 | 493 | -104.0 | 152650 | 151 | -106.1 | 152650 | 183 |
| MR_1774413643_39673955 | 504990 | 420 | -95.5 | 504990 | 868 | -90.9 | 504990 | 831 | -97.0 | 504990 | 763 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1957: `17ddd75f-b17...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `17ddd75f-b17e-4288-ad41-7dad460222a5` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease A3 Offset threshold for 3229111_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1957] topology](images/train_1957.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease A3 Offset threshold for 3246023_1
- `C3`: Add neighbor relationship between 3276715_3 and 3246023_1
- `C4`: Adjust the azimuth of 3229111_2 by 3 degrees
- `C5`: Increase A3 Offset threshold for 3229111_2
- `C6`: Press down the tilt angle  of 3246023_1 by 10 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229111_2
- `C8`: Increase transmission power for 3229111_2
- `C9`: Decrease transmission power for 3229111_2
- `C10`: Decrease A3 Offset threshold for 3229111_2 **← 정답**
- `C11`: Increase A3 Offset threshold for 3246023_1
- `C12`: Press down the tilt angle of 3229111_2 by 10 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246023_1
- `C14`: Lift the tilt angle of 3229111_2 by 10 degrees
- `C15`: Add neighbor relationship between 3229111_2 and 3246023_1
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229111_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246023_1
- `C19`: Lift the tilt angle  of 3246023_1 by 10 degrees
- `C20`: Adjust the azimuth of 3246023_1 by 50 degrees
- `C21`: Decrease transmission power for 3246023_1
- `C22`: Increase transmission power for 3246023_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.388 | MS1 | 121.4656717703 | 31.1446325068 | 258 | 504990 | -80.69 | 12.01 | 421.87 | 0.12 | 2.19 | 1562 |
| 2024-09-20 22:21:32.589 | MS1 | 121.4656728707 | 31.1446316545 | 258 | 504990 | -81.51 | 17.02 | 460.84 | 0.06 | 2.22 | 1593 |
| 2024-09-20 22:21:33.347 | MS1 | 121.4656617874 | 31.1446292763 | 258 | 504990 | -77.66 | 13.90 | 558.39 | 0.00 | 2.51 | 1560 |
| 2024-09-20 22:21:34.613 | MS1 | 121.4656762368 | 31.1446259619 | 258 | 504990 | -89.90 | -1.26 | 30.53 | 0.05 | 1.28 | 1574 |
| 2024-09-20 22:21:35.419 | MS1 | 121.4656608124 | 31.1446319017 | 258 | 504990 | -85.69 | -2.38 | 28.23 | 0.10 | 1.00 | 1591 |
| 2024-09-20 22:21:36.927 | MS1 | 121.4656727925 | 31.1446367155 | 258 | 504990 | -86.34 | -0.77 | 66.91 | 0.03 | 1.26 | 1564 |
| 2024-09-20 22:21:37.683 | MS1 | 121.4656726380 | 31.1446241368 | 258 | 504990 | -85.47 | -3.43 | 69.67 | 0.09 | 1.28 | 1591 |
| 2024-09-20 22:21:38.755 | MS1 | 121.4656619638 | 31.1446213007 | 258 | 504990 | -85.08 | -2.54 | 29.76 | 0.18 | 1.46 | 1561 |
| 2024-09-20 22:21:39.357 | MS1 | 121.4656683749 | 31.1446307173 | 240 | 504990 | -75.05 | 15.87 | 165.13 | 0.17 | 1.49 | 1568 |
| 2024-09-20 22:21:40.110 | MS1 | 121.4656686327 | 31.1446325291 | 240 | 504990 | -83.76 | 12.74 | 458.71 | 0.14 | 2.90 | 1572 |
| 2024-09-20 22:21:41.230 | MS1 | 121.4656644566 | 31.1446370274 | 240 | 504990 | -78.70 | 14.72 | 385.32 | 0.14 | 2.61 | 1600 |
| 2024-09-20 22:21:42.346 | MS1 | 121.4656589917 | 31.1446247418 | 240 | 504990 | -81.25 | 16.06 | 511.27 | 0.11 | 2.99 | 1593 |

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
| 3229111 | 2 | 121.4708951748 | 31.1531714114 | 211 | 10 | 6 | 22.1 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3246023 | 1 | 121.4716937190 | 31.1510436739 | 13 | 15 | 7 | 19.7 | TDD | 240 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3266379 | 4 | 121.4651594934 | 31.1511928221 | 113 | 11 | 8 | 30.8 | TDD | 653 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3276715 | 3 | 121.4657015165 | 31.1442081323 | 105 | 8 | 6 | 32.7 | TDD | 42 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.187 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.202 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.314 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.314 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.008 | NREventA3 | measId:2;ServCellPCI:909;Se... |
| 2024-09-20 22:21:38.248 | NRHandoverAttempt | SourcePCI:909;SourceNR-ARFC... |
| 2024-09-20 22:21:38.279 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.291 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.435 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.435 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246023 | 1 | 10.4831 | 10.9214 | -117.8799 | 5.6421 | 120.3069 | 0.0055 | 0.0055 |
| 2024_09_20 22:00 | 3229111 | 2 | 16.4563 | 5.9087 | -114.0350 | 10.0212 | 117.4357 | 0.0104 | 0.1860 |
| 2024_09_20 22:00 | 3276715 | 3 | 5.6227 | 8.3085 | -116.6526 | 13.2062 | 173.4930 | 0.0006 | 0.0043 |
| 2024_09_20 22:00 | 3266379 | 4 | 11.6553 | 6.9665 | -117.5095 | 12.6717 | 81.0307 | 0.0190 | 0.0048 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413665_7C33E076 | 504990 | 258 | -90.2 | 504990 | 240 | -85.9 | 504990 | 42 | -92.6 | 504990 | 653 |
| MR_1774413665_9A8ACDF2 | 504990 | 258 | -90.6 | 504990 | 240 | -83.1 | 504990 | 42 | -93.7 | 504990 | 653 |
| MR_1774413665_A1D8E6F0 | 504990 | 258 | -88.1 | 504990 | 240 | -84.5 | 504990 | 42 | -94.6 | 504990 | 653 |
| MR_1774413665_8337E8AC | 504990 | 258 | -90.7 | 504990 | 240 | -83.6 | 504990 | 42 | -91.6 | 504990 | 653 |
| MR_1774413665_5F6EA6E3 | 504990 | 258 | -90.1 | 504990 | 240 | -86.7 | 504990 | 42 | -92.0 | 504990 | 653 |
| MR_1774413665_44FD325C | 504990 | 258 | -89.0 | 504990 | 240 | -84.9 | 504990 | 42 | -91.5 | 504990 | 653 |
| MR_1774413665_D956F9B0 | 504990 | 258 | -90.6 | 504990 | 240 | -84.2 | 504990 | 42 | -91.5 | 504990 | 653 |
| MR_1774413665_655C0B72 | 504990 | 240 | -83.5 | 504990 | 258 | -88.2 | 504990 | 42 | -93.1 | 504990 | 653 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1958: `86e78886-421...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `86e78886-4219-4227-b8c3-9601224828cd` |
| Tag | **multiple-answer** |
| 정답 | **C5|C18** |
| C5 의미 | Press down the tilt angle  of 3252513_4 by 4 degrees |
| C18 의미 | Decrease transmission power for 3252513_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1958] topology](images/train_1958.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3218079_3 and 3252513_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252513_4
- `C3`: Lift the tilt angle of 3218079_3 by 5 degrees
- `C4`: Adjust the azimuth of 3218079_3 by 20 degrees
- `C5`: Press down the tilt angle  of 3252513_4 by 4 degrees **← 정답**
- `C6`: Lift the tilt angle  of 3252513_4 by 4 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218079_3
- `C9`: Increase transmission power for 3252513_4
- `C10`: Check test server and transmission issues
- `C11`: Increase A3 Offset threshold for 3252513_4
- `C12`: Add neighbor relationship between 3226966_1 and 3252513_4
- `C13`: Adjust the azimuth of 3252513_4 by 10 degrees
- `C14`: Decrease A3 Offset threshold for 3252513_4
- `C15`: Decrease A3 Offset threshold for 3218079_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218079_3
- `C17`: Increase transmission power for 3218079_3
- `C18`: Decrease transmission power for 3252513_4 **← 정답**
- `C19`: Press down the tilt angle of 3218079_3 by 5 degrees
- `C20`: Increase A3 Offset threshold for 3218079_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252513_4
- `C22`: Decrease transmission power for 3218079_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.658 | MS1 | 121.4656684657 | 31.1446206258 | 221 | 504990 | -77.74 | 12.63 | 572.38 | 0.02 | 2.25 | 1564 |
| 2024-09-20 22:21:32.939 | MS1 | 121.4656697924 | 31.1446185908 | 221 | 504990 | -83.43 | 17.24 | 421.99 | 0.15 | 2.17 | 1584 |
| 2024-09-20 22:21:33.232 | MS1 | 121.4656600649 | 31.1446201739 | 221 | 504990 | -77.26 | 15.55 | 294.22 | 0.20 | 2.97 | 1574 |
| 2024-09-20 22:21:34.670 | MS1 | 121.4656715559 | 31.1446347460 | 221 | 504990 | -89.08 | 3.88 | 51.14 | 0.02 | 1.24 | 1586 |
| 2024-09-20 22:21:35.641 | MS1 | 121.4656666852 | 31.1446188914 | 221 | 504990 | -93.50 | 3.07 | 46.33 | 0.17 | 1.20 | 1561 |
| 2024-09-20 22:21:36.326 | MS1 | 121.4656729927 | 31.1446367421 | 221 | 504990 | -89.45 | 2.18 | 78.13 | 0.13 | 1.34 | 1560 |
| 2024-09-20 22:21:37.601 | MS1 | 121.4656631036 | 31.1446270083 | 221 | 504990 | -85.60 | 2.78 | 66.23 | 0.04 | 1.11 | 1576 |
| 2024-09-20 22:21:38.152 | MS1 | 121.4656680676 | 31.1446281829 | 221 | 504990 | -85.52 | 3.77 | 68.88 | 0.19 | 1.21 | 1578 |
| 2024-09-20 22:21:39.440 | MS1 | 121.4656641744 | 31.1446234889 | 221 | 504990 | -85.16 | 1.84 | 73.09 | 0.03 | 1.15 | 1586 |
| 2024-09-20 22:21:40.294 | MS1 | 121.4656699737 | 31.1446236650 | 221 | 504990 | -84.61 | 12.22 | 417.03 | 0.17 | 2.31 | 1563 |
| 2024-09-20 22:21:41.652 | MS1 | 121.4656699955 | 31.1446231320 | 221 | 504990 | -78.79 | 12.10 | 563.90 | 0.07 | 2.84 | 1578 |
| 2024-09-20 22:21:42.262 | MS1 | 121.4656651290 | 31.1446252375 | 221 | 504990 | -75.37 | 13.52 | 450.64 | 0.07 | 2.11 | 1575 |

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
| 3218079 | 3 | 121.4672075882 | 31.1508412962 | 212 | 1 | 10 | 48.6 | TDD | 221 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3226966 | 1 | 121.4697207374 | 31.1523678296 | 204 | 15 | 3 | 48.3 | TDD | 960 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3242304 | 2 | 121.4690688697 | 31.1458437170 | 284 | 13 | 8 | 32.7 | TDD | 659 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3252513 | 4 | 121.4751315403 | 31.1523187712 | 216 | 3 | 2 | 29.1 | TDD | 903 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.801 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.823 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.957 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.957 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226966 | 1 | 5.0143 | 14.3892 | -115.2589 | 17.3042 | 148.9889 | 0.0157 | 0.0064 |
| 2024_09_20 22:00 | 3242304 | 2 | 19.1995 | 19.8898 | -117.8558 | 16.2165 | 106.3539 | 0.0133 | 0.0128 |
| 2024_09_20 22:00 | 3218079 | 3 | 9.1471 | 14.3863 | -109.8019 | 19.8362 | 91.9540 | 0.0053 | 0.0088 |
| 2024_09_20 22:00 | 3252513 | 4 | 5.7928 | 6.7565 | -115.3956 | 10.3755 | 153.5271 | 0.0126 | 0.0037 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416255_5305CB9C | 504990 | 221 | -87.4 | 504990 | 903 | -86.4 | 504990 | 960 | -88.7 | 504990 | 659 |
| MR_1774416255_6C0E2060 | 504990 | 221 | -90.1 | 504990 | 903 | -86.4 | 504990 | 960 | -89.5 | 504990 | 659 |
| MR_1774416255_EBED9D01 | 504990 | 903 | -90.2 | 504990 | 221 | -87.4 | 504990 | 960 | -88.2 | 504990 | 659 |
| MR_1774416255_D194490C | 504990 | 221 | -90.7 | 504990 | 903 | -85.7 | 504990 | 960 | -87.5 | 504990 | 659 |
| MR_1774416255_807BB223 | 504990 | 903 | -88.3 | 504990 | 221 | -85.6 | 504990 | 960 | -87.8 | 504990 | 659 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1959: `a3c2a91b-e93...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a3c2a91b-e939-48b6-a1af-c50809247f82` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223573_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1959] topology](images/train_1959.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease A3 Offset threshold for 3223573_2
- `C3`: Increase transmission power for 3223573_2
- `C4`: Press down the tilt angle  of 3246968_1 by 2 degrees
- `C5`: Increase A3 Offset threshold for 3246968_1
- `C6`: Increase transmission power for 3246968_1
- `C7`: Increase A3 Offset threshold for 3223573_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246968_1
- `C9`: Add neighbor relationship between 3223573_2 and 3246968_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246968_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Press down the tilt angle of 3223573_2 by 3 degrees
- `C13`: Lift the tilt angle  of 3246968_1 by 2 degrees
- `C14`: Adjust the azimuth of 3246968_1 by 16 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223573_2 **← 정답**
- `C16`: Add neighbor relationship between 3232493_8 and 3246968_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223573_2
- `C18`: Decrease A3 Offset threshold for 3246968_1
- `C19`: Decrease transmission power for 3223573_2
- `C20`: Adjust the azimuth of 3223573_2 by 10 degrees
- `C21`: Lift the tilt angle of 3223573_2 by 3 degrees
- `C22`: Decrease transmission power for 3246968_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.406 | MS1 | 121.4656584272 | 31.1446257355 | 932 | 504990 | -93.25 | 14.12 | 313.35 | 0.09 | 2.59 | 1571 |
| 2024-09-20 22:21:32.935 | MS1 | 121.4656608717 | 31.1446188633 | 429 | 504990 | -94.83 | 9.39 | 573.95 | 0.07 | 2.77 | 1595 |
| 2024-09-20 22:21:33.206 | MS1 | 121.4656699094 | 31.1446324780 | 508 | 504990 | -93.87 | 12.22 | 486.50 | 0.06 | 2.23 | 1590 |
| 2024-09-20 22:21:34.647 | MS1 | 121.4656594103 | 31.1446271080 | 389 | 152650 | -94.94 | 6.77 | 54.42 | 0.09 | 1.79 | 952 |
| 2024-09-20 22:21:35.982 | MS1 | 121.4656592886 | 31.1446345649 | 719 | 152650 | -91.55 | 4.01 | 94.27 | 0.05 | 1.92 | 982 |
| 2024-09-20 22:21:36.617 | MS1 | 121.4656653107 | 31.1446197316 | 39 | 152650 | -90.98 | 4.36 | 95.98 | 0.16 | 1.67 | 966 |
| 2024-09-20 22:21:37.231 | MS1 | 121.4656702692 | 31.1446217530 | 127 | 152650 | -96.09 | 6.54 | 99.58 | 0.12 | 1.97 | 907 |
| 2024-09-20 22:21:38.488 | MS1 | 121.4656744450 | 31.1446252866 | 389 | 152650 | -93.49 | 7.86 | 42.96 | 0.08 | 1.51 | 979 |
| 2024-09-20 22:21:39.430 | MS1 | 121.4656759877 | 31.1446211653 | 719 | 152650 | -87.79 | 7.43 | 80.71 | 0.16 | 1.68 | 923 |
| 2024-09-20 22:21:40.991 | MS1 | 121.4656618292 | 31.1446344410 | 39 | 152650 | -89.06 | 5.32 | 65.74 | 0.12 | 2.27 | 1573 |
| 2024-09-20 22:21:41.211 | MS1 | 121.4656716165 | 31.1446188816 | 127 | 152650 | -92.81 | 5.71 | 49.57 | 0.08 | 2.24 | 1560 |
| 2024-09-20 22:21:42.533 | MS1 | 121.4656665231 | 31.1446261252 | 389 | 152650 | -93.31 | 5.55 | 80.95 | 0.20 | 2.87 | 1560 |

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
| 3215177 | 13 | 121.4713049974 | 31.1491578479 | 287 | 5 | 9 | 25.5 | FDD | 127 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3216322 | 7 | 121.4696014965 | 31.1506613995 | 211 | 5 | 11 | 21.6 | FDD | 389 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3223573 | 2 | 121.4675265687 | 31.1546776939 | 179 | 3 | 0 | 1.9 | TDD | 932 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3232493 | 8 | 121.4704422439 | 31.1531126019 | 74 | 10 | 7 | 25.4 | FDD | 39 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3234416 | 11 | 121.4652356030 | 31.1512088119 | 183 | 12 | 10 | 12.0 | FDD | 559 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3236653 | 4 | 121.4658571583 | 31.1540316036 | 328 | 15 | 9 | 16.9 | TDD | 429 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3246968 | 1 | 121.4728310306 | 31.1476502965 | 228 | 2 | 7 | 1.9 | TDD | 291 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3252105 | 3 | 121.4693968776 | 31.1469500483 | 161 | 13 | 2 | 24.2 | TDD | 1004 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3252830 | 10 | 121.4751415992 | 31.1506732564 | 333 | 4 | 9 | 26.8 | FDD | 719 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3255244 | 5 | 121.4648728295 | 31.1473654186 | 353 | 9 | 7 | 21.7 | TDD | 115 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3270245 | 12 | 121.4656958460 | 31.1554315657 | 125 | 2 | 11 | 23.2 | FDD | 980 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3274513 | 9 | 121.4734274939 | 31.1500790984 | 228 | 6 | 2 | 27.3 | FDD | 395 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3279140 | 6 | 121.4675915374 | 31.1536490428 | 180 | 8 | 0 | 11.2 | TDD | 508 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.822 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.843 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.981 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.981 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.655 | NREventA2 | measId:1;ServCellPCI:504;Se... |
| 2024-09-20 22:21:34.789 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.032 | NREventA5 | measId:3;ServCellPCI:504;Se... |
| 2024-09-20 22:21:35.063 | NRHandoverAttempt | SourcePCI:504;SourceNR-ARFC... |
| 2024-09-20 22:21:35.093 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.106 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.236 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.236 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246968 | 1 | 17.5679 | 6.1270 | -116.2601 | 18.7567 | 127.1762 | 0.0055 | 0.0043 |
| 2024_09_20 22:00 | 3223573 | 2 | 15.6693 | 8.3256 | -115.9291 | 19.2054 | 188.5888 | 0.0141 | 0.0184 |
| 2024_09_20 22:00 | 3252105 | 3 | 12.7744 | 5.7904 | -116.4387 | 7.7403 | 186.2247 | 0.0042 | 0.0091 |
| 2024_09_20 22:00 | 3236653 | 4 | 10.1661 | 18.8056 | -116.1681 | 15.1574 | 142.2811 | 0.0106 | 0.0156 |
| 2024_09_20 22:00 | 3255244 | 5 | 18.0545 | 16.2992 | -116.6456 | 9.8020 | 87.4251 | 0.0141 | 0.0001 |
| 2024_09_20 22:00 | 3279140 | 6 | 11.0136 | 19.4683 | -115.7772 | 5.1002 | 123.5813 | 0.0155 | 0.0086 |
| 2024_09_20 22:00 | 3216322 | 7 | 5.1287 | 10.8795 | -114.7151 | 3.3995 | 21.8498 | 0.0181 | 0.0078 |
| 2024_09_20 22:00 | 3232493 | 8 | 14.2992 | 14.4835 | -114.7821 | 3.5228 | 26.3977 | 0.0102 | 0.0003 |
| 2024_09_20 22:00 | 3274513 | 9 | 18.0988 | 7.4202 | -114.6572 | 3.0321 | 51.6544 | 0.0083 | 0.0120 |
| 2024_09_20 22:00 | 3252830 | 10 | 14.2674 | 11.3613 | -116.7807 | 3.1147 | 36.0343 | 0.0175 | 0.0098 |
| 2024_09_20 22:00 | 3234416 | 11 | 9.9914 | 11.9385 | -114.6141 | 4.3671 | 50.8782 | 0.0101 | 0.0008 |
| 2024_09_20 22:00 | 3270245 | 12 | 9.1234 | 19.9496 | -117.4205 | 4.3954 | 34.5044 | 0.0150 | 0.0051 |
| 2024_09_20 22:00 | 3215177 | 13 | 10.9679 | 8.0926 | -117.4188 | 4.5574 | 49.7561 | 0.0046 | 0.0127 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413031_D1C4C269 | 152650 | 389 | -96.7 | 152650 | 395 | -95.6 | 152650 | 980 | -103.3 | 152650 | 559 |
| MR_1774413031_98A67923 | 152650 | 389 | -94.2 | 152650 | 395 | -95.4 | 152650 | 980 | -100.8 | 152650 | 559 |
| MR_1774413031_D6C66FED | 152650 | 389 | -95.2 | 152650 | 395 | -95.2 | 152650 | 980 | -103.7 | 152650 | 559 |
| MR_1774413031_8D175D41 | 152650 | 389 | -96.6 | 152650 | 395 | -96.7 | 152650 | 980 | -101.0 | 152650 | 559 |
| MR_1774413031_6EA48DC0 | 152650 | 389 | -94.2 | 152650 | 395 | -97.4 | 152650 | 980 | -100.9 | 152650 | 559 |

> *... 2개 열 생략 (전체 14열)*

---
