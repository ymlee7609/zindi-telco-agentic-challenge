# Track A 문제 분석 — train[1090]~train[1099]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1090] ~ train[1099] (10개)

## 목차

1. [문제 1090: `978f3c67-065...`](#1090) — single-answer, 정답: C7
2. [문제 1091: `193b7ddf-101...`](#1091) — single-answer, 정답: C14
3. [문제 1092: `03cfdd3b-568...`](#1092) — single-answer, 정답: C1
4. [문제 1093: `9fd89d49-efd...`](#1093) — single-answer, 정답: C5
5. [문제 1094: `c10823ee-73d...`](#1094) — single-answer, 정답: C22
6. [문제 1095: `d37ff5ce-db1...`](#1095) — multiple-answer, 정답: C4|C6|C7|C10
7. [문제 1096: `fd1b81c0-0ab...`](#1096) — single-answer, 정답: C3
8. [문제 1097: `5c3a8676-8f1...`](#1097) — multiple-answer, 정답: C3|C12
9. [문제 1098: `5d4f8273-1a0...`](#1098) — single-answer, 정답: C22
10. [문제 1099: `970d6b3c-a05...`](#1099) — single-answer, 정답: C13

---

### 문제 1090: `978f3c67-065...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `978f3c67-0656-485c-8647-a2ca5c5dc164` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Lift the tilt angle  of 3256279_3 by 9 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1090] topology](images/train_1090.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265962_2
- `C2`: Add neighbor relationship between 3256279_3 and 3265962_2
- `C3`: Increase transmission power for 3265962_2
- `C4`: Press down the tilt angle of 3234184_1 by 6 degrees
- `C5`: Increase A3 Offset threshold for 3234184_1
- `C6`: Decrease transmission power for 3265962_2
- `C7`: Lift the tilt angle  of 3256279_3 by 9 degrees **← 정답**
- `C8`: Decrease A3 Offset threshold for 3234184_1
- `C9`: Adjust the azimuth of 3256279_3 by 50 degrees
- `C10`: Decrease transmission power for 3234184_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase A3 Offset threshold for 3265962_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234184_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265962_2
- `C15`: Lift the tilt angle of 3234184_1 by 6 degrees
- `C16`: Increase transmission power for 3234184_1
- `C17`: Check test server and transmission issues
- `C18`: Adjust the azimuth of 3234184_1 by 14 degrees
- `C19`: Decrease A3 Offset threshold for 3265962_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234184_1
- `C21`: Press down the tilt angle  of 3256279_3 by 9 degrees
- `C22`: Add neighbor relationship between 3234184_1 and 3265962_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.540 | MS1 | 121.4656748138 | 31.1446379064 | 134 | 504990 | -88.44 | 17.43 | 390.93 | 0.02 | 2.98 | 1599 |
| 2024-09-20 22:21:32.538 | MS1 | 121.4656661978 | 31.1446274888 | 134 | 504990 | -86.82 | 16.79 | 529.37 | 0.12 | 2.01 | 1585 |
| 2024-09-20 22:21:33.437 | MS1 | 121.4656712307 | 31.1446345258 | 134 | 504990 | -91.07 | 16.73 | 574.22 | 0.04 | 2.67 | 1593 |
| 2024-09-20 22:21:34.296 | MS1 | 121.4656583002 | 31.1446307796 | 134 | 504990 | -90.05 | 16.24 | 66.79 | 0.05 | 2.45 | 1590 |
| 2024-09-20 22:21:35.797 | MS1 | 121.4656716023 | 31.1446314044 | 134 | 504990 | -90.22 | 12.95 | 63.61 | 0.10 | 2.96 | 1580 |
| 2024-09-20 22:21:36.480 | MS1 | 121.4656749219 | 31.1446314713 | 134 | 504990 | -87.52 | 17.28 | 99.27 | 0.17 | 2.05 | 1585 |
| 2024-09-20 22:21:37.351 | MS1 | 121.4656657529 | 31.1446238881 | 134 | 504990 | -92.49 | 11.38 | 100.20 | 0.07 | 2.16 | 1589 |
| 2024-09-20 22:21:38.177 | MS1 | 121.4656662257 | 31.1446279879 | 134 | 504990 | -91.22 | 10.43 | 76.95 | 0.18 | 2.34 | 1597 |
| 2024-09-20 22:21:39.757 | MS1 | 121.4656671837 | 31.1446362292 | 134 | 504990 | -92.23 | 8.76 | 86.10 | 0.12 | 2.52 | 1572 |
| 2024-09-20 22:21:40.988 | MS1 | 121.4656605663 | 31.1446306893 | 134 | 504990 | -90.47 | 11.98 | 405.00 | 0.14 | 2.26 | 1569 |
| 2024-09-20 22:21:41.119 | MS1 | 121.4656599676 | 31.1446200482 | 134 | 504990 | -90.90 | 7.70 | 495.64 | 0.17 | 2.80 | 1597 |
| 2024-09-20 22:21:42.674 | MS1 | 121.4656612708 | 31.1446270634 | 134 | 504990 | -92.88 | 11.89 | 493.94 | 0.08 | 2.38 | 1571 |

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
| 3215170 | 4 | 121.4707855401 | 31.1517275492 | 43 | 8 | 10 | 39.5 | TDD | 551 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3234184 | 1 | 121.4672622579 | 31.1500362058 | 208 | 4 | 1 | 18.0 | TDD | 134 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3256279 | 3 | 121.4731827860 | 31.1472058396 | 19 | 12 | 0 | 26.8 | TDD | 918 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3265962 | 2 | 121.4755919062 | 31.1502191892 | 319 | 7 | 3 | 37.9 | TDD | 174 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.574 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.592 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.721 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.721 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.393 | NREventA3 | measId:2;ServCellPCI:905;Se... |
| 2024-09-20 22:21:38.633 | NRHandoverAttempt | SourcePCI:905;SourceNR-ARFC... |
| 2024-09-20 22:21:38.679 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.689 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.811 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.811 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234184 | 1 | 93.4149 | 87.6737 | -116.8595 | 13.9434 | 192.2056 | 0.0126 | 0.0126 |
| 2024_09_20 22:00 | 3265962 | 2 | 8.5867 | 9.0952 | -116.1589 | 13.4352 | 115.3701 | 0.0180 | 0.0148 |
| 2024_09_20 22:00 | 3256279 | 3 | 17.4655 | 11.8500 | -116.6229 | 19.3578 | 162.5537 | 0.0083 | 0.0158 |
| 2024_09_20 22:00 | 3215170 | 4 | 12.8778 | 19.8261 | -114.4268 | 18.2269 | 180.6556 | 0.0003 | 0.0033 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412753_6DECBAD6 | 504990 | 134 | -89.7 | 504990 | 174 | -99.4 | 504990 | 918 | -103.3 | 504990 | 551 |
| MR_1774412753_3C167A80 | 504990 | 134 | -91.6 | 504990 | 174 | -98.0 | 504990 | 918 | -104.9 | 504990 | 551 |
| MR_1774412753_7D33D8C9 | 504990 | 134 | -88.5 | 504990 | 174 | -98.1 | 504990 | 918 | -103.7 | 504990 | 551 |
| MR_1774412753_73D3D7DF | 504990 | 134 | -89.4 | 504990 | 174 | -97.4 | 504990 | 918 | -104.7 | 504990 | 551 |
| MR_1774412753_95F454D8 | 504990 | 134 | -90.6 | 504990 | 174 | -98.4 | 504990 | 918 | -106.0 | 504990 | 551 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1091: `193b7ddf-101...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `193b7ddf-101b-46b4-8bbf-1da4ab34f827` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224979_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1091] topology](images/train_1091.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3224979_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269421_5
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269421_5
- `C4`: Increase transmission power for 3224979_3
- `C5`: Add neighbor relationship between 3224979_3 and 3269421_5
- `C6`: Add neighbor relationship between 3276150_10 and 3269421_5
- `C7`: Decrease A3 Offset threshold for 3224979_3
- `C8`: Increase transmission power for 3269421_5
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224979_3
- `C11`: Adjust the azimuth of 3224979_3 by 22 degrees
- `C12`: Decrease transmission power for 3269421_5
- `C13`: Decrease A3 Offset threshold for 3269421_5
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224979_3 **← 정답**
- `C15`: Press down the tilt angle of 3224979_3 by 5 degrees
- `C16`: Increase A3 Offset threshold for 3224979_3
- `C17`: Lift the tilt angle of 3224979_3 by 5 degrees
- `C18`: Increase A3 Offset threshold for 3269421_5
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle  of 3269421_5 by 5 degrees
- `C21`: Lift the tilt angle  of 3269421_5 by 5 degrees
- `C22`: Adjust the azimuth of 3269421_5 by 13 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.776 | MS1 | 121.4656679047 | 31.1446315446 | 842 | 504990 | -95.69 | 13.63 | 384.73 | 0.13 | 2.92 | 1579 |
| 2024-09-20 22:21:32.978 | MS1 | 121.4656682320 | 31.1446211035 | 345 | 504990 | -95.85 | 11.52 | 340.26 | 0.02 | 2.68 | 1561 |
| 2024-09-20 22:21:33.304 | MS1 | 121.4656616254 | 31.1446245252 | 935 | 504990 | -94.55 | 13.67 | 417.45 | 0.08 | 2.39 | 1600 |
| 2024-09-20 22:21:34.816 | MS1 | 121.4656670839 | 31.1446368904 | 633 | 152650 | -89.81 | 4.12 | 71.84 | 0.04 | 1.54 | 981 |
| 2024-09-20 22:21:35.833 | MS1 | 121.4656582429 | 31.1446331153 | 481 | 152650 | -93.09 | 6.28 | 72.64 | 0.08 | 1.68 | 916 |
| 2024-09-20 22:21:36.804 | MS1 | 121.4656744300 | 31.1446223234 | 179 | 152650 | -92.12 | 5.47 | 76.08 | 0.12 | 1.87 | 985 |
| 2024-09-20 22:21:37.714 | MS1 | 121.4656756121 | 31.1446365424 | 959 | 152650 | -87.22 | 2.41 | 52.19 | 0.02 | 1.90 | 949 |
| 2024-09-20 22:21:38.342 | MS1 | 121.4656698201 | 31.1446360850 | 633 | 152650 | -95.12 | 7.41 | 101.12 | 0.09 | 1.83 | 959 |
| 2024-09-20 22:21:39.169 | MS1 | 121.4656761341 | 31.1446197212 | 481 | 152650 | -90.38 | 7.08 | 72.46 | 0.07 | 1.61 | 979 |
| 2024-09-20 22:21:40.613 | MS1 | 121.4656669484 | 31.1446248970 | 179 | 152650 | -89.85 | 4.85 | 74.49 | 0.06 | 2.11 | 1578 |
| 2024-09-20 22:21:41.767 | MS1 | 121.4656582779 | 31.1446258206 | 959 | 152650 | -88.46 | 6.05 | 66.11 | 0.18 | 2.35 | 1569 |
| 2024-09-20 22:21:42.167 | MS1 | 121.4656678035 | 31.1446279696 | 633 | 152650 | -88.66 | 2.42 | 51.63 | 0.11 | 2.17 | 1595 |

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
| 3211044 | 11 | 121.4643960687 | 31.1470444417 | 8 | 10 | 7 | 14.8 | FDD | 633 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3221581 | 8 | 121.4689715876 | 31.1490631956 | 270 | 15 | 9 | 27.3 | FDD | 257 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3222213 | 9 | 121.4664751732 | 31.1553444776 | 268 | 10 | 1 | 22.3 | FDD | 43 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3224979 | 3 | 121.4721064931 | 31.1486070457 | 212 | 4 | 3 | 7.1 | TDD | 842 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3232113 | 1 | 121.4646662886 | 31.1478283862 | 0 | 9 | 1 | 12.7 | TDD | 935 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3265203 | 12 | 121.4741390152 | 31.1453115109 | 125 | 14 | 10 | 6.0 | FDD | 220 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3269421 | 5 | 121.4710834300 | 31.1497452927 | 209 | 4 | 8 | 7.9 | TDD | 376 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3272264 | 4 | 121.4737924231 | 31.1522483048 | 122 | 13 | 4 | 29.4 | TDD | 331 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3272601 | 6 | 121.4703262521 | 31.1505826711 | 176 | 9 | 2 | 16.5 | TDD | 345 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3272993 | 2 | 121.4739195762 | 31.1540092230 | 322 | 10 | 5 | 29.0 | TDD | 40 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3276150 | 10 | 121.4667183469 | 31.1445106596 | 343 | 9 | 0 | 18.3 | FDD | 179 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3278342 | 7 | 121.4653924006 | 31.1520608058 | 321 | 0 | 10 | 25.5 | FDD | 481 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3279057 | 13 | 121.4678461662 | 31.1516627571 | 92 | 2 | 7 | 0.7 | FDD | 959 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |

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
| 2024-09-20 22:21:30.797 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.820 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.935 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.935 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.673 | NREventA2 | measId:1;ServCellPCI:305;Se... |
| 2024-09-20 22:21:34.791 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.059 | NREventA5 | measId:3;ServCellPCI:305;Se... |
| 2024-09-20 22:21:35.131 | NRHandoverAttempt | SourcePCI:305;SourceNR-ARFC... |
| 2024-09-20 22:21:35.178 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.193 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.320 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.320 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232113 | 1 | 7.1430 | 7.2207 | -116.2768 | 10.8675 | 182.2363 | 0.0044 | 0.0063 |
| 2024_09_20 22:00 | 3272993 | 2 | 11.5931 | 7.5043 | -116.0586 | 19.4811 | 181.8651 | 0.0003 | 0.0057 |
| 2024_09_20 22:00 | 3224979 | 3 | 13.3207 | 13.3834 | -116.8216 | 5.4581 | 192.2838 | 0.0081 | 0.0103 |
| 2024_09_20 22:00 | 3272264 | 4 | 10.3557 | 5.0460 | -114.5718 | 7.3536 | 161.9083 | 0.0192 | 0.0134 |
| 2024_09_20 22:00 | 3269421 | 5 | 12.8870 | 13.8038 | -116.2486 | 9.7195 | 164.1208 | 0.0065 | 0.0022 |
| 2024_09_20 22:00 | 3272601 | 6 | 5.5455 | 13.6267 | -115.3252 | 5.9793 | 178.9955 | 0.0120 | 0.0033 |
| 2024_09_20 22:00 | 3278342 | 7 | 15.4237 | 12.4311 | -117.6567 | 4.3027 | 49.9475 | 0.0040 | 0.0160 |
| 2024_09_20 22:00 | 3221581 | 8 | 12.5240 | 8.2060 | -116.3985 | 4.9121 | 56.4833 | 0.0120 | 0.0191 |
| 2024_09_20 22:00 | 3222213 | 9 | 15.7217 | 5.9462 | -115.9755 | 3.4775 | 25.1364 | 0.0195 | 0.0013 |
| 2024_09_20 22:00 | 3276150 | 10 | 11.1503 | 15.9083 | -114.1356 | 3.6011 | 22.1291 | 0.0001 | 0.0067 |
| 2024_09_20 22:00 | 3211044 | 11 | 9.6320 | 19.6160 | -116.9876 | 4.1224 | 28.8320 | 0.0083 | 0.0094 |
| 2024_09_20 22:00 | 3265203 | 12 | 10.9821 | 8.9912 | -116.1288 | 3.4815 | 56.5990 | 0.0080 | 0.0031 |
| 2024_09_20 22:00 | 3279057 | 13 | 17.0786 | 5.2605 | -115.8623 | 3.0712 | 54.3671 | 0.0194 | 0.0146 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413479_5C3F5A48 | 152650 | 633 | -91.2 | 152650 | 257 | -95.2 | 152650 | 43 | -95.9 | 152650 | 220 |
| MR_1774413479_6ACBD549 | 504990 | 935 | -96.2 | 504990 | 376 | -93.0 | 504990 | 331 | -102.3 | 504990 | 40 |
| MR_1774413479_532C2398 | 504990 | 935 | -93.1 | 504990 | 376 | -93.1 | 504990 | 331 | -102.2 | 504990 | 40 |
| MR_1774413479_6AD28536 | 152650 | 633 | -88.5 | 152650 | 257 | -93.7 | 152650 | 43 | -96.5 | 152650 | 220 |
| MR_1774413479_95407206 | 152650 | 633 | -89.5 | 152650 | 257 | -94.0 | 152650 | 43 | -97.7 | 152650 | 220 |
| MR_1774413479_252D1D20 | 504990 | 935 | -94.8 | 504990 | 376 | -94.1 | 504990 | 331 | -102.3 | 504990 | 40 |
| MR_1774413479_088A44BF | 152650 | 633 | -88.2 | 152650 | 257 | -94.5 | 152650 | 43 | -97.1 | 152650 | 220 |
| MR_1774413479_0EF3F93D | 152650 | 633 | -90.9 | 152650 | 257 | -93.6 | 152650 | 43 | -96.6 | 152650 | 220 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1092: `03cfdd3b-568...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `03cfdd3b-5689-474b-9e95-5cf5e23dbd12` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1092] topology](images/train_1092.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues **← 정답**
- `C2`: Adjust the azimuth of 3265617_2 by 50 degrees
- `C3`: Decrease A3 Offset threshold for 3265617_2
- `C4`: Press down the tilt angle  of 3250130_3 by 5 degrees
- `C5`: Add neighbor relationship between 3265617_2 and 3250130_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265617_2
- `C7`: Press down the tilt angle of 3265617_2 by 10 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250130_3
- `C9`: Increase transmission power for 3265617_2
- `C10`: Decrease A3 Offset threshold for 3250130_3
- `C11`: Decrease transmission power for 3250130_3
- `C12`: Adjust the azimuth of 3250130_3 by 50 degrees
- `C13`: Increase A3 Offset threshold for 3250130_3
- `C14`: Decrease transmission power for 3265617_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250130_3
- `C16`: Increase transmission power for 3250130_3
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Add neighbor relationship between 3215754_1 and 3250130_3
- `C19`: Increase A3 Offset threshold for 3265617_2
- `C20`: Lift the tilt angle of 3265617_2 by 10 degrees
- `C21`: Lift the tilt angle  of 3250130_3 by 5 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265617_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.280 | MS1 | 121.4656594080 | 31.1446183137 | 281 | 504990 | -88.01 | 12.32 | 316.02 | 0.10 | 2.44 | 1589 |
| 2024-09-20 22:21:32.235 | MS1 | 121.4656633379 | 31.1446251506 | 281 | 504990 | -86.01 | 13.71 | 474.03 | 0.01 | 2.98 | 1569 |
| 2024-09-20 22:21:33.198 | MS1 | 121.4656735037 | 31.1446367607 | 281 | 504990 | -90.03 | 12.54 | 537.25 | 0.20 | 2.76 | 1595 |
| 2024-09-20 22:21:34.549 | MS1 | 121.4656655861 | 31.1446307972 | 281 | 504990 | -86.73 | 14.97 | 62.75 | 0.16 | 2.64 | 390 |
| 2024-09-20 22:21:35.548 | MS1 | 121.4656705528 | 31.1446312292 | 281 | 504990 | -87.54 | 14.10 | 100.43 | 0.03 | 2.72 | 464 |
| 2024-09-20 22:21:36.439 | MS1 | 121.4656632359 | 31.1446237669 | 281 | 504990 | -85.56 | 14.90 | 62.39 | 0.01 | 2.39 | 439 |
| 2024-09-20 22:21:37.970 | MS1 | 121.4656729378 | 31.1446337476 | 281 | 504990 | -92.36 | 10.79 | 73.72 | 0.19 | 2.97 | 431 |
| 2024-09-20 22:21:38.805 | MS1 | 121.4656688521 | 31.1446285058 | 281 | 504990 | -93.59 | 12.36 | 98.67 | 0.20 | 2.77 | 365 |
| 2024-09-20 22:21:39.693 | MS1 | 121.4656758088 | 31.1446270983 | 281 | 504990 | -90.11 | 12.18 | 63.49 | 0.19 | 2.62 | 307 |
| 2024-09-20 22:21:40.346 | MS1 | 121.4656636770 | 31.1446217405 | 281 | 504990 | -90.99 | 7.90 | 351.08 | 0.05 | 2.29 | 1576 |
| 2024-09-20 22:21:41.246 | MS1 | 121.4656626091 | 31.1446304452 | 281 | 504990 | -91.32 | 11.10 | 460.22 | 0.16 | 2.28 | 1564 |
| 2024-09-20 22:21:42.783 | MS1 | 121.4656588935 | 31.1446272231 | 281 | 504990 | -93.32 | 9.29 | 348.18 | 0.16 | 2.28 | 1565 |

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
| 3215754 | 1 | 121.4669099503 | 31.1547341022 | 104 | 3 | 12 | 21.9 | TDD | 488 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3222454 | 4 | 121.4655364900 | 31.1538589713 | 325 | 11 | 5 | 43.8 | TDD | 471 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3250130 | 3 | 121.4676075316 | 31.1465573552 | 163 | 0 | 1 | 24.9 | TDD | 123 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3265617 | 2 | 121.4758714020 | 31.1509643827 | 108 | 12 | 11 | 34.7 | TDD | 281 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.363 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.378 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.508 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.508 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.258 | NREventA3 | measId:2;ServCellPCI:469;Se... |
| 2024-09-20 22:21:38.498 | NRHandoverAttempt | SourcePCI:469;SourceNR-ARFC... |
| 2024-09-20 22:21:38.546 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.560 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.701 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.701 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215754 | 1 | 8.7916 | 10.5199 | -117.8579 | 13.4892 | 110.1818 | 0.0090 | 0.0053 |
| 2024_09_20 22:00 | 3265617 | 2 | 9.7434 | 17.2883 | -114.9462 | 15.7934 | 198.2272 | 0.0005 | 0.0006 |
| 2024_09_20 22:00 | 3250130 | 3 | 12.0272 | 19.0043 | -117.1299 | 9.0839 | 117.6022 | 0.0100 | 0.0155 |
| 2024_09_20 22:00 | 3222454 | 4 | 15.6757 | 15.8796 | -116.9896 | 8.6370 | 168.7231 | 0.0113 | 0.0162 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412808_BBD7D724 | 504990 | 281 | -85.1 | 504990 | 123 | -92.8 | 504990 | 488 | -94.8 | 504990 | 471 |
| MR_1774412808_24D2768D | 504990 | 281 | -86.8 | 504990 | 123 | -93.5 | 504990 | 488 | -96.1 | 504990 | 471 |
| MR_1774412808_B096B715 | 504990 | 281 | -88.4 | 504990 | 123 | -92.8 | 504990 | 488 | -93.7 | 504990 | 471 |
| MR_1774412808_B11E0D0E | 504990 | 281 | -84.8 | 504990 | 123 | -93.2 | 504990 | 488 | -96.8 | 504990 | 471 |
| MR_1774412808_B58CB296 | 504990 | 281 | -84.9 | 504990 | 123 | -91.4 | 504990 | 488 | -93.5 | 504990 | 471 |
| MR_1774412808_519F84E4 | 504990 | 281 | -87.4 | 504990 | 123 | -94.8 | 504990 | 488 | -95.4 | 504990 | 471 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1093: `9fd89d49-efd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9fd89d49-efdd-4861-b7fb-05e038be962e` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Decrease A3 Offset threshold for 3238590_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1093] topology](images/train_1093.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250084_1
- `C2`: Lift the tilt angle of 3238590_4 by 10 degrees
- `C3`: Increase A3 Offset threshold for 3238590_4
- `C4`: Increase A3 Offset threshold for 3250084_1
- `C5`: Decrease A3 Offset threshold for 3238590_4 **← 정답**
- `C6`: Decrease A3 Offset threshold for 3250084_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238590_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238590_4
- `C9`: Adjust the azimuth of 3250084_1 by 50 degrees
- `C10`: Increase transmission power for 3250084_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Add neighbor relationship between 3235173_2 and 3250084_1
- `C13`: Press down the tilt angle  of 3250084_1 by 10 degrees
- `C14`: Decrease transmission power for 3238590_4
- `C15`: Lift the tilt angle  of 3250084_1 by 10 degrees
- `C16`: Check test server and transmission issues
- `C17`: Add neighbor relationship between 3238590_4 and 3250084_1
- `C18`: Press down the tilt angle of 3238590_4 by 10 degrees
- `C19`: Decrease transmission power for 3250084_1
- `C20`: Adjust the azimuth of 3238590_4 by 50 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250084_1
- `C22`: Increase transmission power for 3238590_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.182 | MS1 | 121.4656692826 | 31.1446303928 | 671 | 504990 | -79.92 | 15.41 | 349.05 | 0.18 | 2.79 | 1596 |
| 2024-09-20 22:21:32.305 | MS1 | 121.4656627426 | 31.1446258445 | 671 | 504990 | -75.30 | 16.53 | 562.68 | 0.10 | 2.70 | 1569 |
| 2024-09-20 22:21:33.972 | MS1 | 121.4656696614 | 31.1446332606 | 671 | 504990 | -82.51 | 14.35 | 381.61 | 0.08 | 2.21 | 1592 |
| 2024-09-20 22:21:34.156 | MS1 | 121.4656763049 | 31.1446370682 | 671 | 504990 | -89.32 | -3.01 | 42.42 | 0.10 | 1.42 | 1563 |
| 2024-09-20 22:21:35.713 | MS1 | 121.4656606845 | 31.1446310428 | 671 | 504990 | -90.03 | -2.88 | 68.16 | 0.11 | 1.31 | 1591 |
| 2024-09-20 22:21:36.489 | MS1 | 121.4656650061 | 31.1446281585 | 671 | 504990 | -89.23 | -0.41 | 58.32 | 0.12 | 1.07 | 1595 |
| 2024-09-20 22:21:37.630 | MS1 | 121.4656769487 | 31.1446254222 | 671 | 504990 | -91.73 | -3.55 | 60.55 | 0.11 | 1.49 | 1586 |
| 2024-09-20 22:21:38.105 | MS1 | 121.4656601006 | 31.1446290657 | 671 | 504990 | -84.52 | -2.34 | 57.65 | 0.05 | 1.20 | 1582 |
| 2024-09-20 22:21:39.400 | MS1 | 121.4656732696 | 31.1446247666 | 310 | 504990 | -80.31 | 12.42 | 168.80 | 0.05 | 1.28 | 1588 |
| 2024-09-20 22:21:40.155 | MS1 | 121.4656777771 | 31.1446308132 | 310 | 504990 | -84.69 | 12.98 | 594.76 | 0.00 | 2.91 | 1573 |
| 2024-09-20 22:21:41.198 | MS1 | 121.4656655716 | 31.1446246503 | 310 | 504990 | -83.79 | 14.68 | 340.38 | 0.17 | 2.42 | 1586 |
| 2024-09-20 22:21:42.511 | MS1 | 121.4656704937 | 31.1446268635 | 310 | 504990 | -83.98 | 17.12 | 393.12 | 0.13 | 2.72 | 1595 |

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
| 3215681 | 3 | 121.4698522220 | 31.1447717893 | 115 | 10 | 5 | 38.6 | TDD | 617 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3235173 | 2 | 121.4752024317 | 31.1532935598 | 353 | 8 | 5 | 18.3 | TDD | 321 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3238590 | 4 | 121.4673646606 | 31.1479825324 | 72 | 10 | 8 | 40.4 | TDD | 671 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3250084 | 1 | 121.4749477525 | 31.1513446595 | 325 | 9 | 0 | 29.8 | TDD | 310 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.605 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.628 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.759 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.759 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.481 | NREventA3 | measId:2;ServCellPCI:328;Se... |
| 2024-09-20 22:21:38.721 | NRHandoverAttempt | SourcePCI:328;SourceNR-ARFC... |
| 2024-09-20 22:21:38.754 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.765 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.897 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.897 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250084 | 1 | 7.2754 | 5.2794 | -114.0887 | 17.0189 | 196.3864 | 0.0057 | 0.0123 |
| 2024_09_20 22:00 | 3235173 | 2 | 14.2033 | 18.2913 | -115.4197 | 9.6181 | 126.5313 | 0.0055 | 0.0162 |
| 2024_09_20 22:00 | 3215681 | 3 | 7.1921 | 7.6928 | -114.2245 | 15.0217 | 196.7095 | 0.0114 | 0.0171 |
| 2024_09_20 22:00 | 3238590 | 4 | 14.9837 | 5.3481 | -114.8904 | 8.0072 | 132.5939 | 0.0159 | 0.1322 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415129_BEC9BA4D | 504990 | 310 | -83.6 | 504990 | 671 | -91.1 | 504990 | 321 | -88.7 | 504990 | 617 |
| MR_1774415129_1E955DB0 | 504990 | 671 | -87.7 | 504990 | 310 | -83.7 | 504990 | 321 | -86.6 | 504990 | 617 |
| MR_1774415129_CBB94844 | 504990 | 310 | -82.5 | 504990 | 671 | -90.8 | 504990 | 321 | -86.6 | 504990 | 617 |
| MR_1774415129_543DE30E | 504990 | 310 | -84.4 | 504990 | 671 | -90.6 | 504990 | 321 | -86.9 | 504990 | 617 |
| MR_1774415129_00485AD1 | 504990 | 671 | -91.0 | 504990 | 310 | -84.2 | 504990 | 321 | -87.3 | 504990 | 617 |
| MR_1774415129_E88A618F | 504990 | 671 | -90.9 | 504990 | 310 | -84.3 | 504990 | 321 | -85.0 | 504990 | 617 |
| MR_1774415129_3C9BA921 | 504990 | 671 | -88.7 | 504990 | 310 | -84.1 | 504990 | 321 | -86.0 | 504990 | 617 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1094: `c10823ee-73d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c10823ee-73dd-4b9c-a54a-b92fb03652b4` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261539_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1094] topology](images/train_1094.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3235910_1 by 10 degrees
- `C2`: Add neighbor relationship between 3261539_4 and 3235910_1
- `C3`: Increase transmission power for 3261539_4
- `C4`: Decrease transmission power for 3261539_4
- `C5`: Increase transmission power for 3235910_1
- `C6`: Increase A3 Offset threshold for 3261539_4
- `C7`: Decrease A3 Offset threshold for 3235910_1
- `C8`: Increase A3 Offset threshold for 3235910_1
- `C9`: Decrease transmission power for 3235910_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261539_4
- `C11`: Lift the tilt angle of 3261539_4 by 6 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Add neighbor relationship between 3259454_10 and 3235910_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235910_1
- `C15`: Press down the tilt angle  of 3235910_1 by 4 degrees
- `C16`: Check test server and transmission issues
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235910_1
- `C18`: Decrease A3 Offset threshold for 3261539_4
- `C19`: Lift the tilt angle  of 3235910_1 by 4 degrees
- `C20`: Press down the tilt angle of 3261539_4 by 6 degrees
- `C21`: Adjust the azimuth of 3261539_4 by 6 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261539_4 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.242 | MS1 | 121.4656730053 | 31.1446184001 | 980 | 504990 | -95.59 | 12.98 | 416.29 | 0.01 | 2.05 | 1584 |
| 2024-09-20 22:21:32.467 | MS1 | 121.4656619617 | 31.1446346466 | 72 | 504990 | -94.67 | 9.27 | 330.22 | 0.01 | 2.06 | 1581 |
| 2024-09-20 22:21:33.259 | MS1 | 121.4656693260 | 31.1446208302 | 747 | 504990 | -94.01 | 14.25 | 408.19 | 0.04 | 2.31 | 1597 |
| 2024-09-20 22:21:34.188 | MS1 | 121.4656665998 | 31.1446180592 | 804 | 152650 | -87.41 | 7.69 | 84.98 | 0.18 | 1.66 | 918 |
| 2024-09-20 22:21:35.546 | MS1 | 121.4656742623 | 31.1446194331 | 284 | 152650 | -91.70 | 7.30 | 52.20 | 0.19 | 1.88 | 922 |
| 2024-09-20 22:21:36.592 | MS1 | 121.4656612959 | 31.1446186720 | 913 | 152650 | -90.90 | 7.07 | 46.20 | 0.05 | 1.60 | 975 |
| 2024-09-20 22:21:37.976 | MS1 | 121.4656703327 | 31.1446293261 | 130 | 152650 | -91.32 | 7.16 | 102.42 | 0.13 | 1.81 | 972 |
| 2024-09-20 22:21:38.350 | MS1 | 121.4656616366 | 31.1446198401 | 804 | 152650 | -89.40 | 6.58 | 98.76 | 0.04 | 1.61 | 929 |
| 2024-09-20 22:21:39.761 | MS1 | 121.4656666446 | 31.1446334176 | 284 | 152650 | -89.18 | 6.51 | 48.23 | 0.20 | 1.68 | 940 |
| 2024-09-20 22:21:40.826 | MS1 | 121.4656727154 | 31.1446375932 | 913 | 152650 | -88.58 | 2.51 | 62.10 | 0.01 | 2.08 | 1566 |
| 2024-09-20 22:21:41.191 | MS1 | 121.4656659978 | 31.1446298382 | 130 | 152650 | -95.57 | 3.66 | 75.54 | 0.07 | 2.86 | 1563 |
| 2024-09-20 22:21:42.164 | MS1 | 121.4656675255 | 31.1446372096 | 804 | 152650 | -92.89 | 4.91 | 67.21 | 0.08 | 2.02 | 1575 |

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
| 3224929 | 3 | 121.4703883606 | 31.1463009124 | 344 | 8 | 3 | 18.8 | TDD | 747 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3235910 | 1 | 121.4665522113 | 31.1530867258 | 195 | 4 | 5 | 5.1 | TDD | 417 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3242883 | 11 | 121.4682478098 | 31.1502843843 | 92 | 12 | 1 | 29.7 | FDD | 116 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3244442 | 12 | 121.4708459792 | 31.1525801390 | 149 | 0 | 12 | 16.8 | FDD | 983 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3249555 | 8 | 121.4660130929 | 31.1491305665 | 353 | 11 | 1 | 2.2 | FDD | 611 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3258845 | 6 | 121.4643964711 | 31.1500841577 | 2 | 6 | 3 | 12.9 | TDD | 220 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3259454 | 10 | 121.4711046339 | 31.1512784124 | 190 | 5 | 1 | 18.6 | FDD | 913 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3261539 | 4 | 121.4731825817 | 31.1517478435 | 216 | 5 | 1 | 16.7 | TDD | 980 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3262112 | 13 | 121.4654435429 | 31.1483001014 | 135 | 4 | 6 | 11.2 | FDD | 284 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3262771 | 9 | 121.4706639725 | 31.1555040204 | 174 | 14 | 11 | 6.9 | FDD | 804 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3262982 | 2 | 121.4676404913 | 31.1448141874 | 51 | 5 | 0 | 27.2 | TDD | 72 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3264125 | 7 | 121.4740166169 | 31.1529649792 | 255 | 11 | 0 | 7.7 | FDD | 130 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3267919 | 5 | 121.4739700111 | 31.1479470834 | 67 | 9 | 9 | 28.5 | TDD | 631 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.534 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.551 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.700 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.700 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.372 | NREventA2 | measId:1;ServCellPCI:927;Se... |
| 2024-09-20 22:21:35.500 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.758 | NREventA5 | measId:3;ServCellPCI:927;Se... |
| 2024-09-20 22:21:35.817 | NRHandoverAttempt | SourcePCI:927;SourceNR-ARFC... |
| 2024-09-20 22:21:35.864 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.879 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.997 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.997 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235910 | 1 | 16.2038 | 10.8906 | -115.9447 | 5.3206 | 91.5536 | 0.0033 | 0.0165 |
| 2024_09_20 22:00 | 3262982 | 2 | 17.7343 | 12.4823 | -114.9003 | 10.4284 | 190.2041 | 0.0199 | 0.0104 |
| 2024_09_20 22:00 | 3224929 | 3 | 15.5869 | 9.9758 | -114.8436 | 5.6558 | 91.6590 | 0.0121 | 0.0123 |
| 2024_09_20 22:00 | 3261539 | 4 | 18.6704 | 18.0209 | -114.3792 | 18.7899 | 112.1792 | 0.0052 | 0.0009 |
| 2024_09_20 22:00 | 3267919 | 5 | 15.0173 | 6.3628 | -117.3788 | 5.2330 | 86.2330 | 0.0106 | 0.0104 |
| 2024_09_20 22:00 | 3258845 | 6 | 6.8794 | 10.7999 | -116.4977 | 7.4787 | 95.7431 | 0.0044 | 0.0170 |
| 2024_09_20 22:00 | 3264125 | 7 | 9.0717 | 9.9041 | -117.5475 | 3.2998 | 31.3742 | 0.0038 | 0.0041 |
| 2024_09_20 22:00 | 3249555 | 8 | 13.9630 | 13.1423 | -115.7746 | 3.5101 | 38.8889 | 0.0199 | 0.0192 |
| 2024_09_20 22:00 | 3262771 | 9 | 15.0173 | 8.4931 | -117.0085 | 3.5378 | 26.7042 | 0.0120 | 0.0190 |
| 2024_09_20 22:00 | 3259454 | 10 | 11.8876 | 11.4850 | -116.1524 | 3.0633 | 42.1145 | 0.0015 | 0.0047 |
| 2024_09_20 22:00 | 3242883 | 11 | 13.9981 | 19.9355 | -116.4464 | 3.9095 | 54.0111 | 0.0199 | 0.0105 |
| 2024_09_20 22:00 | 3244442 | 12 | 13.0362 | 12.2634 | -115.1199 | 3.7647 | 57.7134 | 0.0101 | 0.0054 |
| 2024_09_20 22:00 | 3262112 | 13 | 18.3971 | 14.4707 | -114.5452 | 4.4284 | 42.1379 | 0.0030 | 0.0031 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414392_9944FEB7 | 152650 | 804 | -87.0 | 152650 | 611 | -97.2 | 152650 | 983 | -99.2 | 152650 | 116 |
| MR_1774414392_B51942AE | 152650 | 804 | -88.9 | 152650 | 611 | -96.1 | 152650 | 983 | -98.7 | 152650 | 116 |
| MR_1774414392_B6DCD9CE | 152650 | 804 | -89.2 | 152650 | 611 | -96.1 | 152650 | 983 | -96.6 | 152650 | 116 |
| MR_1774414392_E884E166 | 504990 | 747 | -94.4 | 504990 | 417 | -97.5 | 504990 | 631 | -99.8 | 504990 | 220 |
| MR_1774414392_99D232E4 | 504990 | 747 | -93.0 | 504990 | 417 | -97.5 | 504990 | 631 | -100.5 | 504990 | 220 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1095: `d37ff5ce-db1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d37ff5ce-db1b-4bab-958c-35ac5b4e2105` |
| Tag | **multiple-answer** |
| 정답 | **C4|C6|C7|C10** |
| C4 의미 | Increase A3 Offset threshold for 3251237_1 |
| C6 의미 | Press down the tilt angle  of 3251237_1 by 1 degrees |
| C7 의미 | Decrease transmission power for 3251237_1 |
| C10 의미 | Increase A3 Offset threshold for 3251876_2 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1095] topology](images/train_1095.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Press down the tilt angle of 3251876_2 by 1 degrees
- `C3`: Adjust the azimuth of 3251876_2 by 16 degrees
- `C4`: Increase A3 Offset threshold for 3251237_1 **← 정답**
- `C5`: Increase transmission power for 3251237_1
- `C6`: Press down the tilt angle  of 3251237_1 by 1 degrees **← 정답**
- `C7`: Decrease transmission power for 3251237_1 **← 정답**
- `C8`: Lift the tilt angle of 3251876_2 by 1 degrees
- `C9`: Adjust the azimuth of 3251237_1 by 46 degrees
- `C10`: Increase A3 Offset threshold for 3251876_2 **← 정답**
- `C11`: Lift the tilt angle  of 3251237_1 by 1 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251237_1
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251237_1
- `C15`: Decrease transmission power for 3251876_2
- `C16`: Add neighbor relationship between 3251876_2 and 3251237_1
- `C17`: Decrease A3 Offset threshold for 3251237_1
- `C18`: Decrease A3 Offset threshold for 3251876_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251876_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251876_2
- `C21`: Add neighbor relationship between 3247817_4 and 3251237_1
- `C22`: Increase transmission power for 3251876_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.349 | MS1 | 121.4656644285 | 31.1446308783 | 530 | 504990 | -79.92 | 15.23 | 381.67 | 0.13 | 2.25 | 1589 |
| 2024-09-20 22:21:32.182 | MS1 | 121.4656685870 | 31.1446190061 | 530 | 504990 | -81.15 | 16.42 | 440.16 | 0.18 | 2.92 | 1561 |
| 2024-09-20 22:21:33.580 | MS1 | 121.4656606428 | 31.1446334896 | 530 | 504990 | -75.51 | 12.16 | 436.66 | 0.07 | 2.71 | 1582 |
| 2024-09-20 22:21:34.300 | MS1 | 121.4656656625 | 31.1446251177 | 602 | 504990 | -89.88 | 1.40 | 70.90 | 0.08 | 1.47 | 1578 |
| 2024-09-20 22:21:35.516 | MS1 | 121.4656624685 | 31.1446217349 | 602 | 504990 | -86.71 | 3.09 | 61.17 | 0.12 | 1.13 | 1566 |
| 2024-09-20 22:21:36.968 | MS1 | 121.4656716023 | 31.1446310266 | 530 | 504990 | -81.26 | 1.38 | 51.22 | 0.15 | 1.07 | 1589 |
| 2024-09-20 22:21:37.428 | MS1 | 121.4656745945 | 31.1446228483 | 530 | 504990 | -84.52 | 2.62 | 74.27 | 0.00 | 1.43 | 1583 |
| 2024-09-20 22:21:38.490 | MS1 | 121.4656670095 | 31.1446343455 | 602 | 504990 | -88.54 | 1.83 | 44.71 | 0.06 | 1.18 | 1585 |
| 2024-09-20 22:21:39.810 | MS1 | 121.4656688584 | 31.1446238794 | 602 | 504990 | -82.92 | 3.05 | 51.68 | 0.15 | 1.01 | 1592 |
| 2024-09-20 22:21:40.279 | MS1 | 121.4656763954 | 31.1446214475 | 602 | 504990 | -78.26 | 17.64 | 476.85 | 0.19 | 2.89 | 1574 |
| 2024-09-20 22:21:41.558 | MS1 | 121.4656714537 | 31.1446255888 | 602 | 504990 | -82.56 | 15.19 | 429.28 | 0.19 | 2.38 | 1577 |
| 2024-09-20 22:21:42.179 | MS1 | 121.4656619476 | 31.1446271221 | 602 | 504990 | -77.72 | 13.94 | 357.68 | 0.11 | 2.19 | 1594 |

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
| 3233677 | 3 | 121.4723841222 | 31.1510574184 | 279 | 10 | 7 | 46.5 | TDD | 602 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3247817 | 4 | 121.4697127435 | 31.1450279772 | 63 | 5 | 8 | 47.5 | TDD | 252 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3251237 | 1 | 121.4757329555 | 31.1442551835 | 319 | 0 | 4 | 24.4 | TDD | 582 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3251876 | 2 | 121.4729367265 | 31.1529462886 | 233 | 0 | 10 | 18.1 | TDD | 530 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3251926 | 5 | 121.4738177662 | 31.1471761293 | 119 | 10 | 6 | 28.0 | TDD | 893 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.611 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.632 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.757 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.757 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.458 | NREventA3 | measId:2;ServCellPCI:928;Se... |
| 2024-09-20 22:21:34.698 | NRHandoverAttempt | SourcePCI:928;SourceNR-ARFC... |
| 2024-09-20 22:21:34.735 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.747 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:34.852 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.852 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.458 | NREventA3 | measId:2;ServCellPCI:1001;S... |
| 2024-09-20 22:21:36.698 | NRHandoverAttempt | SourcePCI:1001;SourceNR-ARF... |
| 2024-09-20 22:21:36.745 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.755 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:36.881 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.881 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.458 | NREventA3 | measId:2;ServCellPCI:928;Se... |
| 2024-09-20 22:21:38.698 | NRHandoverAttempt | SourcePCI:928;SourceNR-ARFC... |
| 2024-09-20 22:21:38.743 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.754 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.904 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.904 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251237 | 1 | 9.5642 | 14.5834 | -115.5473 | 9.3912 | 199.0026 | 0.0075 | 0.0122 |
| 2024_09_20 22:00 | 3251876 | 2 | 7.6512 | 19.4630 | -117.4941 | 15.7700 | 161.8030 | 0.0068 | 0.0183 |
| 2024_09_20 22:00 | 3233677 | 3 | 19.7302 | 6.0227 | -116.4247 | 9.3268 | 104.3382 | 0.0016 | 0.0135 |
| 2024_09_20 22:00 | 3247817 | 4 | 14.1207 | 16.8516 | -117.3155 | 14.3470 | 123.4107 | 0.0120 | 0.0177 |
| 2024_09_20 22:00 | 3251926 | 5 | 18.3561 | 15.0134 | -117.1107 | 16.3876 | 108.0416 | 0.0080 | 0.0154 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415571_D95B49AE | 504990 | 530 | -91.5 | 504990 | 602 | -90.2 | 504990 | 582 | -89.5 | 504990 | 252 |
| MR_1774415571_F6BB55F5 | 504990 | 530 | -89.2 | 504990 | 602 | -90.6 | 504990 | 582 | -89.1 | 504990 | 252 |
| MR_1774415571_55697A42 | 504990 | 530 | -89.1 | 504990 | 602 | -87.7 | 504990 | 582 | -90.3 | 504990 | 252 |
| MR_1774415571_B6F7951D | 504990 | 530 | -91.8 | 504990 | 602 | -90.9 | 504990 | 582 | -91.3 | 504990 | 252 |
| MR_1774415571_6C0DDE79 | 504990 | 602 | -89.2 | 504990 | 530 | -90.4 | 504990 | 582 | -91.7 | 504990 | 252 |
| MR_1774415571_07E21F1A | 504990 | 602 | -90.5 | 504990 | 530 | -89.6 | 504990 | 582 | -90.0 | 504990 | 252 |
| MR_1774415571_9E9C91B0 | 504990 | 530 | -89.1 | 504990 | 602 | -88.1 | 504990 | 582 | -89.8 | 504990 | 252 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1096: `fd1b81c0-0ab...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fd1b81c0-0ab5-40a6-b36e-452fa83b88a2` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Add neighbor relationship between 3274864_3 and 3259823_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1096] topology](images/train_1096.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3259823_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274864_3
- `C3`: Add neighbor relationship between 3274864_3 and 3259823_2 **← 정답**
- `C4`: Check test server and transmission issues
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259823_2
- `C6`: Decrease A3 Offset threshold for 3274864_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274864_3
- `C8`: Press down the tilt angle  of 3259823_2 by 5 degrees
- `C9`: Press down the tilt angle of 3274864_3 by 7 degrees
- `C10`: Adjust the azimuth of 3274864_3 by 50 degrees
- `C11`: Decrease transmission power for 3259823_2
- `C12`: Add neighbor relationship between 3266373_4 and 3259823_2
- `C13`: Increase transmission power for 3274864_3
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Lift the tilt angle of 3274864_3 by 7 degrees
- `C16`: Lift the tilt angle  of 3259823_2 by 5 degrees
- `C17`: Decrease transmission power for 3274864_3
- `C18`: Decrease A3 Offset threshold for 3259823_2
- `C19`: Adjust the azimuth of 3259823_2 by 14 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259823_2
- `C21`: Increase A3 Offset threshold for 3274864_3
- `C22`: Increase A3 Offset threshold for 3259823_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.927 | MS1 | 121.4656739866 | 31.1446261546 | 661 | 504990 | -76.86 | 17.64 | 325.31 | 0.08 | 2.33 | 1565 |
| 2024-09-20 22:21:32.446 | MS1 | 121.4656735932 | 31.1446188006 | 661 | 504990 | -76.81 | 15.70 | 461.48 | 0.12 | 2.51 | 1568 |
| 2024-09-20 22:21:33.858 | MS1 | 121.4656741172 | 31.1446193442 | 661 | 504990 | -75.96 | 13.36 | 425.52 | 0.03 | 2.67 | 1577 |
| 2024-09-20 22:21:34.587 | MS1 | 121.4656608993 | 31.1446250567 | 661 | 504990 | -91.13 | -2.96 | 33.32 | 0.07 | 1.41 | 1572 |
| 2024-09-20 22:21:35.470 | MS1 | 121.4656633820 | 31.1446277640 | 661 | 504990 | -88.56 | -2.36 | 62.66 | 0.11 | 1.19 | 1592 |
| 2024-09-20 22:21:36.444 | MS1 | 121.4656749389 | 31.1446242754 | 661 | 504990 | -92.28 | -1.89 | 65.28 | 0.00 | 1.02 | 1561 |
| 2024-09-20 22:21:37.122 | MS1 | 121.4656614762 | 31.1446360263 | 661 | 504990 | -93.84 | -1.93 | 52.17 | 0.16 | 1.08 | 1596 |
| 2024-09-20 22:21:38.916 | MS1 | 121.4656588261 | 31.1446345265 | 661 | 504990 | -84.09 | 13.43 | 541.57 | 0.08 | 1.43 | 1591 |
| 2024-09-20 22:21:39.727 | MS1 | 121.4656614439 | 31.1446331398 | 661 | 504990 | -82.36 | 15.63 | 406.00 | 0.14 | 1.37 | 1598 |
| 2024-09-20 22:21:40.876 | MS1 | 121.4656660299 | 31.1446259579 | 661 | 504990 | -80.67 | 15.63 | 555.41 | 0.11 | 2.53 | 1599 |
| 2024-09-20 22:21:41.815 | MS1 | 121.4656686889 | 31.1446184580 | 661 | 504990 | -77.77 | 13.65 | 415.50 | 0.02 | 2.26 | 1584 |
| 2024-09-20 22:21:42.492 | MS1 | 121.4656601940 | 31.1446345445 | 661 | 504990 | -76.97 | 14.87 | 390.57 | 0.02 | 2.45 | 1594 |

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
| 3247645 | 1 | 121.4729045429 | 31.1441065349 | 160 | 1 | 3 | 20.9 | TDD | 452 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3259823 | 2 | 121.4644169566 | 31.1545788636 | 160 | 4 | 7 | 23.1 | TDD | 29 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3266373 | 4 | 121.4662163707 | 31.1448862196 | 5 | 1 | 8 | 28.2 | TDD | 439 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3274864 | 3 | 121.4651151576 | 31.1512628216 | 253 | 5 | 2 | 29.2 | TDD | 661 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.850 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.974 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.974 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.711 | NREventA3 | measId:2;ServCellPCI:161;Se... |
| 2024-09-20 22:21:35.711 | NREventA3 | measId:2;ServCellPCI:161;Se... |
| 2024-09-20 22:21:36.711 | NREventA3 | measId:2;ServCellPCI:161;Se... |
| 2024-09-20 22:21:39.211 | NRRRCReestablishAttempt | PCI:161 |
| 2024-09-20 22:21:39.231 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.242 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.369 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.369 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247645 | 1 | 18.8106 | 12.4924 | -117.9089 | 18.6515 | 80.2291 | 0.0118 | 0.0082 |
| 2024_09_20 22:00 | 3259823 | 2 | 18.6979 | 6.8647 | -117.8108 | 19.6514 | 105.2937 | 0.0025 | 0.0061 |
| 2024_09_20 22:00 | 3274864 | 3 | 5.0328 | 12.6821 | -115.6790 | 11.6687 | 155.9346 | 0.0155 | 0.1439 |
| 2024_09_20 22:00 | 3266373 | 4 | 6.1893 | 10.6210 | -115.1096 | 7.8274 | 166.4920 | 0.0168 | 0.0134 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415970_13AEBF08 | 504990 | 29 | -85.5 | 504990 | 661 | -90.7 | 504990 | 439 | -86.2 | 504990 | 452 |
| MR_1774415970_AC4FB88F | 504990 | 29 | -84.9 | 504990 | 661 | -90.0 | 504990 | 439 | -87.3 | 504990 | 452 |
| MR_1774415970_E4560A33 | 504990 | 661 | -92.0 | 504990 | 29 | -87.8 | 504990 | 439 | -87.0 | 504990 | 452 |
| MR_1774415970_963FDD1B | 504990 | 29 | -83.9 | 504990 | 661 | -91.2 | 504990 | 439 | -88.5 | 504990 | 452 |
| MR_1774415970_79036109 | 504990 | 661 | -90.2 | 504990 | 29 | -87.4 | 504990 | 439 | -86.9 | 504990 | 452 |
| MR_1774415970_2C0F6717 | 504990 | 661 | -89.9 | 504990 | 29 | -86.3 | 504990 | 439 | -88.0 | 504990 | 452 |
| MR_1774415970_20B5E744 | 504990 | 661 | -92.1 | 504990 | 29 | -84.6 | 504990 | 439 | -86.8 | 504990 | 452 |
| MR_1774415970_F874F6A1 | 504990 | 661 | -89.2 | 504990 | 29 | -86.5 | 504990 | 439 | -88.6 | 504990 | 452 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1097: `5c3a8676-8f1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5c3a8676-8f19-4308-99f8-4262691b00d6` |
| Tag | **multiple-answer** |
| 정답 | **C3|C12** |
| C3 의미 | Increase transmission power for 3266050_1 |
| C12 의미 | Adjust the azimuth of 3266050_1 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1097] topology](images/train_1097.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266050_1
- `C2`: Adjust the azimuth of 3211589_4 by 18 degrees
- `C3`: Increase transmission power for 3266050_1 **← 정답**
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266050_1
- `C5`: Press down the tilt angle  of 3211589_4 by 4 degrees
- `C6`: Add neighbor relationship between 3266050_1 and 3211589_4
- `C7`: Check test server and transmission issues
- `C8`: Lift the tilt angle  of 3211589_4 by 4 degrees
- `C9`: Increase transmission power for 3211589_4
- `C10`: Decrease A3 Offset threshold for 3211589_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211589_4
- `C12`: Adjust the azimuth of 3266050_1 by 50 degrees **← 정답**
- `C13`: Increase A3 Offset threshold for 3211589_4
- `C14`: Decrease transmission power for 3211589_4
- `C15`: Add neighbor relationship between 3236203_2 and 3211589_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211589_4
- `C17`: Press down the tilt angle of 3266050_1 by 10 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease transmission power for 3266050_1
- `C20`: Increase A3 Offset threshold for 3266050_1
- `C21`: Lift the tilt angle of 3266050_1 by 10 degrees
- `C22`: Decrease A3 Offset threshold for 3266050_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.927 | MS1 | 121.4656748309 | 31.1446316446 | 800 | 504990 | -93.30 | 13.54 | 407.61 | 0.08 | 2.26 | 1595 |
| 2024-09-20 22:21:32.849 | MS1 | 121.4656729624 | 31.1446313852 | 800 | 504990 | -88.43 | 16.24 | 361.83 | 0.05 | 2.07 | 1571 |
| 2024-09-20 22:21:33.813 | MS1 | 121.4656702675 | 31.1446261787 | 800 | 504990 | -86.48 | 13.65 | 411.72 | 0.04 | 2.44 | 1566 |
| 2024-09-20 22:21:34.561 | MS1 | 121.4656594745 | 31.1446297331 | 800 | 504990 | -107.94 | -0.63 | 41.92 | 0.04 | 1.42 | 1596 |
| 2024-09-20 22:21:35.497 | MS1 | 121.4656608600 | 31.1446214397 | 800 | 504990 | -106.54 | 1.01 | 44.63 | 0.12 | 1.01 | 1578 |
| 2024-09-20 22:21:36.631 | MS1 | 121.4656648003 | 31.1446313817 | 800 | 504990 | -100.24 | 0.84 | 54.75 | 0.20 | 1.24 | 1583 |
| 2024-09-20 22:21:37.879 | MS1 | 121.4656630068 | 31.1446354666 | 800 | 504990 | -108.99 | -1.10 | 29.01 | 0.05 | 1.23 | 1571 |
| 2024-09-20 22:21:38.611 | MS1 | 121.4656761366 | 31.1446246125 | 800 | 504990 | -105.81 | -1.13 | 39.84 | 0.11 | 1.27 | 1570 |
| 2024-09-20 22:21:39.851 | MS1 | 121.4656661541 | 31.1446221317 | 800 | 504990 | -100.80 | 1.24 | 74.78 | 0.12 | 1.45 | 1568 |
| 2024-09-20 22:21:40.721 | MS1 | 121.4656735380 | 31.1446218372 | 800 | 504990 | -87.36 | 14.46 | 515.21 | 0.20 | 2.40 | 1593 |
| 2024-09-20 22:21:41.592 | MS1 | 121.4656651465 | 31.1446296827 | 800 | 504990 | -87.36 | 13.95 | 407.92 | 0.13 | 2.36 | 1568 |
| 2024-09-20 22:21:42.907 | MS1 | 121.4656597075 | 31.1446306410 | 800 | 504990 | -91.88 | 17.02 | 528.12 | 0.11 | 2.82 | 1593 |

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
| 3211589 | 4 | 121.4750543393 | 31.1440482617 | 256 | 1 | 2 | 39.2 | TDD | 182 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3236203 | 2 | 121.4750321670 | 31.1448822397 | 308 | 1 | 10 | 30.8 | TDD | 9 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3264519 | 3 | 121.4741385753 | 31.1533451715 | 139 | 1 | 4 | 16.6 | TDD | 604 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3266050 | 1 | 121.4646114662 | 31.1488295446 | 103 | 13 | 2 | 23.8 | TDD | 800 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.512 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.531 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.665 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.665 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.872 | NREventA2 | measId:1;ServCellPCI:298;Se... |
| 2024-09-20 22:21:35.006 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266050 | 1 | 12.8362 | 15.2410 | -116.1013 | 15.5368 | 94.4218 | 0.1738 | 0.0194 |
| 2024_09_20 22:00 | 3236203 | 2 | 11.5619 | 5.7449 | -116.7208 | 5.0831 | 114.1040 | 0.0161 | 0.0171 |
| 2024_09_20 22:00 | 3264519 | 3 | 6.3541 | 6.3532 | -114.7094 | 12.9917 | 119.9788 | 0.0169 | 0.0021 |
| 2024_09_20 22:00 | 3211589 | 4 | 14.3801 | 7.8494 | -114.0268 | 7.1978 | 154.7390 | 0.0195 | 0.0038 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413650_F7F53B16 | 504990 | 800 | -108.3 | 504990 | 182 | -112.4 | 504990 | 9 | -118.3 | 504990 | 604 |
| MR_1774413650_04CA2E8D | 504990 | 800 | -107.1 | 504990 | 182 | -113.8 | 504990 | 9 | -116.1 | 504990 | 604 |
| MR_1774413650_934CEDED | 504990 | 800 | -107.2 | 504990 | 182 | -114.4 | 504990 | 9 | -118.8 | 504990 | 604 |
| MR_1774413650_5F2949DC | 504990 | 800 | -107.0 | 504990 | 182 | -114.2 | 504990 | 9 | -118.6 | 504990 | 604 |
| MR_1774413650_B9A1A78F | 504990 | 800 | -109.5 | 504990 | 182 | -115.3 | 504990 | 9 | -117.1 | 504990 | 604 |
| MR_1774413650_86B83C99 | 504990 | 800 | -108.6 | 504990 | 182 | -114.1 | 504990 | 9 | -116.7 | 504990 | 604 |
| MR_1774413650_1A467AC7 | 504990 | 800 | -106.3 | 504990 | 182 | -114.9 | 504990 | 9 | -115.5 | 504990 | 604 |
| MR_1774413650_A9EFEB92 | 504990 | 800 | -106.1 | 504990 | 182 | -111.7 | 504990 | 9 | -117.6 | 504990 | 604 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1098: `5d4f8273-1a0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5d4f8273-1a02-4de5-9927-08341f34f054` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease A3 Offset threshold for 3276384_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1098] topology](images/train_1098.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3276384_2 and 3231764_1
- `C2`: Increase transmission power for 3231764_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Add neighbor relationship between 3250802_4 and 3231764_1
- `C5`: Press down the tilt angle of 3276384_2 by 10 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231764_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276384_2
- `C8`: Lift the tilt angle of 3276384_2 by 10 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231764_1
- `C10`: Adjust the azimuth of 3276384_2 by 50 degrees
- `C11`: Decrease A3 Offset threshold for 3231764_1
- `C12`: Increase A3 Offset threshold for 3231764_1
- `C13`: Check test server and transmission issues
- `C14`: Adjust the azimuth of 3231764_1 by 50 degrees
- `C15`: Increase transmission power for 3276384_2
- `C16`: Press down the tilt angle  of 3231764_1 by 3 degrees
- `C17`: Decrease transmission power for 3231764_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276384_2
- `C19`: Decrease transmission power for 3276384_2
- `C20`: Increase A3 Offset threshold for 3276384_2
- `C21`: Lift the tilt angle  of 3231764_1 by 3 degrees
- `C22`: Decrease A3 Offset threshold for 3276384_2 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.156 | MS1 | 121.4656733010 | 31.1446377171 | 794 | 504990 | -75.28 | 12.63 | 468.52 | 0.08 | 2.39 | 1587 |
| 2024-09-20 22:21:32.117 | MS1 | 121.4656736981 | 31.1446192961 | 794 | 504990 | -81.72 | 12.33 | 426.90 | 0.18 | 2.79 | 1572 |
| 2024-09-20 22:21:33.326 | MS1 | 121.4656650618 | 31.1446210943 | 794 | 504990 | -79.64 | 15.29 | 321.09 | 0.00 | 2.52 | 1568 |
| 2024-09-20 22:21:34.934 | MS1 | 121.4656669268 | 31.1446228495 | 794 | 504990 | -92.95 | -3.93 | 49.31 | 0.03 | 1.26 | 1585 |
| 2024-09-20 22:21:35.718 | MS1 | 121.4656601792 | 31.1446255391 | 794 | 504990 | -90.77 | -0.80 | 69.77 | 0.19 | 1.39 | 1564 |
| 2024-09-20 22:21:36.624 | MS1 | 121.4656601969 | 31.1446236833 | 794 | 504990 | -92.27 | -3.51 | 53.22 | 0.06 | 1.11 | 1564 |
| 2024-09-20 22:21:37.767 | MS1 | 121.4656765323 | 31.1446328819 | 794 | 504990 | -84.29 | -1.25 | 69.78 | 0.07 | 1.41 | 1598 |
| 2024-09-20 22:21:38.379 | MS1 | 121.4656699036 | 31.1446216734 | 794 | 504990 | -88.40 | -1.73 | 74.93 | 0.15 | 1.10 | 1576 |
| 2024-09-20 22:21:39.173 | MS1 | 121.4656769796 | 31.1446338882 | 1 | 504990 | -77.57 | 14.49 | 180.55 | 0.17 | 1.29 | 1579 |
| 2024-09-20 22:21:40.556 | MS1 | 121.4656724470 | 31.1446365011 | 1 | 504990 | -84.70 | 15.41 | 383.42 | 0.19 | 2.60 | 1565 |
| 2024-09-20 22:21:41.122 | MS1 | 121.4656655814 | 31.1446199055 | 1 | 504990 | -80.71 | 16.64 | 364.20 | 0.19 | 2.44 | 1589 |
| 2024-09-20 22:21:42.217 | MS1 | 121.4656656501 | 31.1446314284 | 1 | 504990 | -81.45 | 14.70 | 533.53 | 0.00 | 2.09 | 1589 |

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
| 3231764 | 1 | 121.4725181420 | 31.1475560904 | 9 | 2 | 6 | 18.8 | TDD | 1 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3250802 | 4 | 121.4648753383 | 31.1546965159 | 349 | 11 | 1 | 18.5 | TDD | 621 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3257143 | 3 | 121.4678870653 | 31.1506552443 | 293 | 8 | 6 | 20.3 | TDD | 153 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3276384 | 2 | 121.4696140153 | 31.1441365511 | 217 | 14 | 6 | 24.6 | TDD | 794 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.452 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.472 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.597 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.597 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.329 | NREventA3 | measId:2;ServCellPCI:404;Se... |
| 2024-09-20 22:21:38.569 | NRHandoverAttempt | SourcePCI:404;SourceNR-ARFC... |
| 2024-09-20 22:21:38.613 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.625 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.746 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.746 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231764 | 1 | 6.8900 | 6.2123 | -115.4877 | 5.5239 | 173.5329 | 0.0159 | 0.0084 |
| 2024_09_20 22:00 | 3276384 | 2 | 8.6776 | 7.6049 | -115.3160 | 15.7417 | 182.3662 | 0.0054 | 0.1044 |
| 2024_09_20 22:00 | 3257143 | 3 | 7.9867 | 8.8326 | -115.2930 | 9.5365 | 196.1062 | 0.0116 | 0.0133 |
| 2024_09_20 22:00 | 3250802 | 4 | 18.7287 | 7.6942 | -114.8499 | 18.0819 | 183.4705 | 0.0140 | 0.0001 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415685_6F6BF550 | 504990 | 1 | -86.7 | 504990 | 794 | -92.8 | 504990 | 621 | -86.0 | 504990 | 153 |
| MR_1774415685_7783F9C4 | 504990 | 794 | -93.9 | 504990 | 1 | -85.6 | 504990 | 621 | -86.9 | 504990 | 153 |
| MR_1774415685_D7E63C72 | 504990 | 794 | -91.1 | 504990 | 1 | -85.6 | 504990 | 621 | -89.2 | 504990 | 153 |
| MR_1774415685_9A1C5E36 | 504990 | 794 | -91.5 | 504990 | 1 | -85.7 | 504990 | 621 | -88.3 | 504990 | 153 |
| MR_1774415685_B0AB06DE | 504990 | 794 | -94.5 | 504990 | 1 | -84.7 | 504990 | 621 | -85.9 | 504990 | 153 |
| MR_1774415685_E1CAC9E2 | 504990 | 1 | -87.6 | 504990 | 794 | -92.9 | 504990 | 621 | -86.6 | 504990 | 153 |
| MR_1774415685_3A4D8E87 | 504990 | 794 | -92.3 | 504990 | 1 | -87.9 | 504990 | 621 | -86.6 | 504990 | 153 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1099: `970d6b3c-a05...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `970d6b3c-a056-499c-a3a3-cbc5659f777c` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease A3 Offset threshold for 3252970_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1099] topology](images/train_1099.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3252970_3 by 10 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238931_2
- `C3`: Increase A3 Offset threshold for 3238931_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252970_3
- `C5`: Increase transmission power for 3252970_3
- `C6`: Lift the tilt angle  of 3238931_2 by 7 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238931_2
- `C8`: Adjust the azimuth of 3238931_2 by 50 degrees
- `C9`: Decrease transmission power for 3252970_3
- `C10`: Add neighbor relationship between 3252970_3 and 3238931_2
- `C11`: Press down the tilt angle of 3252970_3 by 10 degrees
- `C12`: Decrease A3 Offset threshold for 3238931_2
- `C13`: Decrease A3 Offset threshold for 3252970_3 **← 정답**
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252970_3
- `C15`: Increase A3 Offset threshold for 3252970_3
- `C16`: Adjust the azimuth of 3252970_3 by 50 degrees
- `C17`: Press down the tilt angle  of 3238931_2 by 7 degrees
- `C18`: Add neighbor relationship between 3231742_4 and 3238931_2
- `C19`: Decrease transmission power for 3238931_2
- `C20`: Check test server and transmission issues
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Increase transmission power for 3238931_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.346 | MS1 | 121.4656601567 | 31.1446213683 | 378 | 504990 | -80.66 | 14.99 | 406.53 | 0.13 | 2.70 | 1564 |
| 2024-09-20 22:21:32.597 | MS1 | 121.4656609100 | 31.1446329331 | 378 | 504990 | -78.28 | 17.08 | 570.04 | 0.07 | 2.52 | 1585 |
| 2024-09-20 22:21:33.422 | MS1 | 121.4656591119 | 31.1446192529 | 378 | 504990 | -83.83 | 17.73 | 466.48 | 0.20 | 2.76 | 1594 |
| 2024-09-20 22:21:34.709 | MS1 | 121.4656591830 | 31.1446299513 | 378 | 504990 | -87.24 | -3.87 | 58.63 | 0.08 | 1.50 | 1600 |
| 2024-09-20 22:21:35.308 | MS1 | 121.4656695159 | 31.1446256080 | 378 | 504990 | -85.07 | -3.36 | 33.46 | 0.09 | 1.43 | 1594 |
| 2024-09-20 22:21:36.815 | MS1 | 121.4656605665 | 31.1446280366 | 378 | 504990 | -85.13 | -2.53 | 54.06 | 0.15 | 1.08 | 1563 |
| 2024-09-20 22:21:37.357 | MS1 | 121.4656611679 | 31.1446199445 | 378 | 504990 | -92.45 | -3.61 | 30.50 | 0.05 | 1.11 | 1564 |
| 2024-09-20 22:21:38.379 | MS1 | 121.4656618388 | 31.1446377231 | 378 | 504990 | -90.30 | -0.23 | 56.22 | 0.07 | 1.35 | 1586 |
| 2024-09-20 22:21:39.308 | MS1 | 121.4656725716 | 31.1446328528 | 129 | 504990 | -79.85 | 14.74 | 173.32 | 0.06 | 1.03 | 1593 |
| 2024-09-20 22:21:40.433 | MS1 | 121.4656625967 | 31.1446278883 | 129 | 504990 | -75.87 | 15.10 | 555.10 | 0.03 | 2.02 | 1582 |
| 2024-09-20 22:21:41.157 | MS1 | 121.4656627486 | 31.1446194338 | 129 | 504990 | -80.08 | 14.93 | 379.07 | 0.16 | 2.89 | 1576 |
| 2024-09-20 22:21:42.188 | MS1 | 121.4656582763 | 31.1446284217 | 129 | 504990 | -80.18 | 16.13 | 505.27 | 0.00 | 2.16 | 1598 |

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
| 3231742 | 4 | 121.4700334127 | 31.1528480702 | 268 | 12 | 4 | 34.5 | TDD | 175 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3238931 | 2 | 121.4685256260 | 31.1556770832 | 315 | 5 | 9 | 34.3 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3252970 | 3 | 121.4660773782 | 31.1513261920 | 16 | 9 | 5 | 26.6 | TDD | 378 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3279915 | 1 | 121.4650467124 | 31.1555798798 | 311 | 11 | 1 | 36.9 | TDD | 464 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.506 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.529 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.673 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.673 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.378 | NREventA3 | measId:2;ServCellPCI:392;Se... |
| 2024-09-20 22:21:38.618 | NRHandoverAttempt | SourcePCI:392;SourceNR-ARFC... |
| 2024-09-20 22:21:38.652 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.667 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.804 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.804 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279915 | 1 | 15.7498 | 8.8368 | -116.2135 | 18.9320 | 197.4273 | 0.0098 | 0.0121 |
| 2024_09_20 22:00 | 3238931 | 2 | 11.4064 | 10.2436 | -116.6165 | 15.0465 | 193.7920 | 0.0007 | 0.0124 |
| 2024_09_20 22:00 | 3252970 | 3 | 11.8963 | 6.3893 | -117.7936 | 9.1416 | 152.8387 | 0.0011 | 0.1370 |
| 2024_09_20 22:00 | 3231742 | 4 | 5.3717 | 18.1709 | -115.1571 | 11.6091 | 138.7771 | 0.0026 | 0.0115 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412737_98F49464 | 504990 | 378 | -87.5 | 504990 | 129 | -81.8 | 504990 | 175 | -80.3 | 504990 | 464 |
| MR_1774412737_C381AD95 | 504990 | 378 | -87.5 | 504990 | 129 | -82.2 | 504990 | 175 | -80.0 | 504990 | 464 |
| MR_1774412737_36F5701F | 504990 | 378 | -88.5 | 504990 | 129 | -83.3 | 504990 | 175 | -81.0 | 504990 | 464 |
| MR_1774412737_EBE68EC1 | 504990 | 378 | -86.6 | 504990 | 129 | -82.3 | 504990 | 175 | -82.4 | 504990 | 464 |
| MR_1774412737_3DC6D0FA | 504990 | 129 | -82.9 | 504990 | 378 | -88.8 | 504990 | 175 | -83.4 | 504990 | 464 |

> *... 2개 열 생략 (전체 14열)*

---
