# Track A 문제 분석 — train[510]~train[519]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[510] ~ train[519] (10개)

## 목차

1. [문제 510: `8b3bbc2d-dfd...`](#510) — multiple-answer, 정답: C9|C21
2. [문제 511: `36f91437-4f7...`](#511) — single-answer, 정답: C8
3. [문제 512: `f7c7c4ec-32e...`](#512) — single-answer, 정답: C14
4. [문제 513: `61c8e42d-92c...`](#513) — single-answer, 정답: C11
5. [문제 514: `a8e205b7-5be...`](#514) — single-answer, 정답: C16
6. [문제 515: `7eb4f1d8-36e...`](#515) — single-answer, 정답: C7
7. [문제 516: `6e33e036-f81...`](#516) — multiple-answer, 정답: C2|C4
8. [문제 517: `b5b928a8-8e4...`](#517) — single-answer, 정답: C13
9. [문제 518: `3628824d-93a...`](#518) — single-answer, 정답: C7
10. [문제 519: `f4b53cc8-d13...`](#519) — single-answer, 정답: C11

---

### 문제 510: `8b3bbc2d-dfd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8b3bbc2d-dfde-4e67-a5b7-2ddd9cc85181` |
| Tag | **multiple-answer** |
| 정답 | **C9|C21** |
| C9 의미 | Increase transmission power for 3246811_4 |
| C21 의미 | Adjust the azimuth of 3246811_4 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[510] topology](images/train_0510.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246811_4
- `C2`: Decrease A3 Offset threshold for 3215678_2
- `C3`: Decrease transmission power for 3246811_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215678_2
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Adjust the azimuth of 3215678_2 by 10 degrees
- `C7`: Increase A3 Offset threshold for 3215678_2
- `C8`: Press down the tilt angle  of 3215678_2 by 1 degrees
- `C9`: Increase transmission power for 3246811_4 **← 정답**
- `C10`: Decrease transmission power for 3215678_2
- `C11`: Lift the tilt angle of 3246811_4 by 10 degrees
- `C12`: Press down the tilt angle of 3246811_4 by 10 degrees
- `C13`: Add neighbor relationship between 3246811_4 and 3215678_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246811_4
- `C15`: Increase transmission power for 3215678_2
- `C16`: Check test server and transmission issues
- `C17`: Add neighbor relationship between 3211278_1 and 3215678_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215678_2
- `C19`: Lift the tilt angle  of 3215678_2 by 1 degrees
- `C20`: Increase A3 Offset threshold for 3246811_4
- `C21`: Adjust the azimuth of 3246811_4 by 50 degrees **← 정답**
- `C22`: Decrease A3 Offset threshold for 3246811_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.578 | MS1 | 121.4656632266 | 31.1446339776 | 694 | 504990 | -92.67 | 17.23 | 513.44 | 0.18 | 2.51 | 1584 |
| 2024-09-20 22:21:32.470 | MS1 | 121.4656734916 | 31.1446237776 | 694 | 504990 | -88.01 | 13.90 | 385.69 | 0.14 | 2.62 | 1577 |
| 2024-09-20 22:21:33.232 | MS1 | 121.4656649639 | 31.1446190986 | 694 | 504990 | -85.04 | 16.43 | 307.89 | 0.19 | 2.67 | 1585 |
| 2024-09-20 22:21:34.801 | MS1 | 121.4656610152 | 31.1446266644 | 694 | 504990 | -100.51 | 0.15 | 40.04 | 0.06 | 1.40 | 1562 |
| 2024-09-20 22:21:35.155 | MS1 | 121.4656603126 | 31.1446201399 | 694 | 504990 | -102.17 | 0.38 | 64.47 | 0.07 | 1.37 | 1580 |
| 2024-09-20 22:21:36.111 | MS1 | 121.4656587971 | 31.1446279749 | 694 | 504990 | -104.53 | -1.56 | 29.69 | 0.09 | 1.24 | 1560 |
| 2024-09-20 22:21:37.518 | MS1 | 121.4656656137 | 31.1446330307 | 694 | 504990 | -105.42 | 0.13 | 34.75 | 0.06 | 1.17 | 1573 |
| 2024-09-20 22:21:38.231 | MS1 | 121.4656774547 | 31.1446245795 | 694 | 504990 | -104.28 | 0.08 | 46.35 | 0.12 | 1.01 | 1570 |
| 2024-09-20 22:21:39.245 | MS1 | 121.4656731009 | 31.1446300363 | 694 | 504990 | -106.90 | -0.73 | 33.09 | 0.05 | 1.22 | 1595 |
| 2024-09-20 22:21:40.886 | MS1 | 121.4656698414 | 31.1446216259 | 694 | 504990 | -88.30 | 12.66 | 364.59 | 0.17 | 2.41 | 1582 |
| 2024-09-20 22:21:41.185 | MS1 | 121.4656753125 | 31.1446368472 | 694 | 504990 | -93.11 | 17.96 | 599.17 | 0.11 | 2.61 | 1581 |
| 2024-09-20 22:21:42.875 | MS1 | 121.4656726321 | 31.1446253447 | 694 | 504990 | -86.54 | 13.40 | 312.41 | 0.14 | 2.23 | 1583 |

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
| 3211278 | 1 | 121.4676528582 | 31.1491914449 | 138 | 6 | 10 | 41.7 | TDD | 40 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3215678 | 2 | 121.4662786907 | 31.1525470895 | 194 | 0 | 3 | 16.2 | TDD | 529 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3237218 | 3 | 121.4752941470 | 31.1536620085 | 106 | 3 | 5 | 24.0 | TDD | 292 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3246811 | 4 | 121.4744496713 | 31.1481021198 | 305 | 11 | 5 | 17.3 | TDD | 694 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.213 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.229 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.332 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.332 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.606 | NREventA2 | measId:1;ServCellPCI:919;Se... |
| 2024-09-20 22:21:34.717 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211278 | 1 | 15.9285 | 17.2635 | -117.8900 | 15.5109 | 195.4801 | 0.0081 | 0.0115 |
| 2024_09_20 22:00 | 3215678 | 2 | 10.2026 | 6.6602 | -116.8164 | 10.4592 | 175.1517 | 0.0106 | 0.0018 |
| 2024_09_20 22:00 | 3237218 | 3 | 17.9151 | 12.5064 | -116.8207 | 6.5140 | 186.7648 | 0.0181 | 0.0151 |
| 2024_09_20 22:00 | 3246811 | 4 | 17.7147 | 17.7635 | -114.3594 | 16.6301 | 125.9441 | 0.1042 | 0.0183 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412434_B97AC9A8 | 504990 | 694 | -102.2 | 504990 | 529 | -103.7 | 504990 | 40 | -108.9 | 504990 | 292 |
| MR_1774412434_26A8A4D6 | 504990 | 694 | -101.7 | 504990 | 529 | -103.0 | 504990 | 40 | -107.3 | 504990 | 292 |
| MR_1774412434_8DB95B8D | 504990 | 694 | -99.2 | 504990 | 529 | -102.6 | 504990 | 40 | -107.4 | 504990 | 292 |
| MR_1774412434_80AD4E41 | 504990 | 694 | -100.9 | 504990 | 529 | -101.7 | 504990 | 40 | -106.0 | 504990 | 292 |
| MR_1774412434_D455F383 | 504990 | 694 | -100.2 | 504990 | 529 | -101.7 | 504990 | 40 | -106.0 | 504990 | 292 |
| MR_1774412434_2EDBC1EA | 504990 | 694 | -101.8 | 504990 | 529 | -103.6 | 504990 | 40 | -109.3 | 504990 | 292 |
| MR_1774412434_EF890234 | 504990 | 694 | -101.8 | 504990 | 529 | -102.4 | 504990 | 40 | -107.7 | 504990 | 292 |
| MR_1774412434_194CACA0 | 504990 | 694 | -100.8 | 504990 | 529 | -101.7 | 504990 | 40 | -106.1 | 504990 | 292 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 511: `36f91437-4f7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `36f91437-4f7e-4867-8da6-b9fed91e95a4` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252266_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[511] topology](images/train_0511.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3252266_2 by 2 degrees
- `C2`: Lift the tilt angle  of 3257062_1 by 4 degrees
- `C3`: Increase A3 Offset threshold for 3252266_2
- `C4`: Increase A3 Offset threshold for 3257062_1
- `C5`: Press down the tilt angle of 3252266_2 by 2 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease transmission power for 3257062_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252266_2 **← 정답**
- `C9`: Decrease A3 Offset threshold for 3252266_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252266_2
- `C11`: Add neighbor relationship between 3252266_2 and 3257062_1
- `C12`: Adjust the azimuth of 3257062_1 by 28 degrees
- `C13`: Check test server and transmission issues
- `C14`: Add neighbor relationship between 3242535_12 and 3257062_1
- `C15`: Increase transmission power for 3252266_2
- `C16`: Increase transmission power for 3257062_1
- `C17`: Decrease transmission power for 3252266_2
- `C18`: Decrease A3 Offset threshold for 3257062_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257062_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257062_1
- `C21`: Press down the tilt angle  of 3257062_1 by 4 degrees
- `C22`: Adjust the azimuth of 3252266_2 by 24 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.965 | MS1 | 121.4656767156 | 31.1446353087 | 876 | 504990 | -95.35 | 12.43 | 420.17 | 0.05 | 2.02 | 1562 |
| 2024-09-20 22:21:32.242 | MS1 | 121.4656658414 | 31.1446211877 | 253 | 504990 | -95.94 | 12.16 | 525.26 | 0.09 | 2.10 | 1597 |
| 2024-09-20 22:21:33.854 | MS1 | 121.4656666548 | 31.1446223444 | 857 | 504990 | -94.84 | 12.19 | 361.52 | 0.12 | 2.05 | 1584 |
| 2024-09-20 22:21:34.197 | MS1 | 121.4656656905 | 31.1446325813 | 686 | 152650 | -90.62 | 2.67 | 61.72 | 0.11 | 1.92 | 900 |
| 2024-09-20 22:21:35.242 | MS1 | 121.4656679082 | 31.1446274954 | 12 | 152650 | -95.49 | 4.99 | 54.56 | 0.00 | 1.86 | 925 |
| 2024-09-20 22:21:36.257 | MS1 | 121.4656633958 | 31.1446363173 | 188 | 152650 | -94.95 | 6.18 | 95.06 | 0.01 | 1.95 | 961 |
| 2024-09-20 22:21:37.351 | MS1 | 121.4656648681 | 31.1446206048 | 365 | 152650 | -89.00 | 3.49 | 66.55 | 0.08 | 1.94 | 983 |
| 2024-09-20 22:21:38.573 | MS1 | 121.4656600118 | 31.1446187162 | 686 | 152650 | -92.87 | 2.58 | 96.30 | 0.02 | 1.51 | 965 |
| 2024-09-20 22:21:39.951 | MS1 | 121.4656735155 | 31.1446307580 | 12 | 152650 | -90.91 | 2.36 | 87.15 | 0.08 | 1.53 | 923 |
| 2024-09-20 22:21:40.551 | MS1 | 121.4656598966 | 31.1446315811 | 188 | 152650 | -96.16 | 6.53 | 70.80 | 0.19 | 2.07 | 1583 |
| 2024-09-20 22:21:41.239 | MS1 | 121.4656619374 | 31.1446246624 | 365 | 152650 | -91.06 | 2.67 | 87.95 | 0.10 | 2.58 | 1579 |
| 2024-09-20 22:21:42.216 | MS1 | 121.4656702927 | 31.1446188621 | 686 | 152650 | -96.85 | 7.16 | 88.24 | 0.04 | 2.92 | 1577 |

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
| 3218473 | 3 | 121.4653797310 | 31.1502966419 | 38 | 3 | 10 | 8.5 | TDD | 815 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3226685 | 4 | 121.4651033459 | 31.1530334781 | 215 | 9 | 8 | 29.5 | TDD | 857 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3242535 | 12 | 121.4664332291 | 31.1460274946 | 49 | 0 | 3 | 2.9 | FDD | 188 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3243281 | 8 | 121.4665554666 | 31.1550667766 | 253 | 1 | 5 | 18.0 | FDD | 12 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3252266 | 2 | 121.4734388135 | 31.1482614984 | 217 | 0 | 12 | 25.6 | TDD | 876 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3252307 | 13 | 121.4646873867 | 31.1497250852 | 357 | 4 | 8 | 6.1 | FDD | 766 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3257062 | 1 | 121.4703424669 | 31.1552234050 | 229 | 3 | 6 | 23.2 | TDD | 100 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3257371 | 11 | 121.4705134458 | 31.1500751629 | 83 | 12 | 4 | 25.7 | FDD | 114 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3262733 | 10 | 121.4749810850 | 31.1445431532 | 262 | 7 | 0 | 7.1 | FDD | 686 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3263010 | 7 | 121.4713025493 | 31.1522979260 | 196 | 2 | 0 | 11.4 | FDD | 553 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3266535 | 6 | 121.4668155440 | 31.1518754975 | 273 | 6 | 8 | 10.2 | TDD | 253 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3274600 | 9 | 121.4710525312 | 31.1446345608 | 252 | 12 | 5 | 8.7 | FDD | 365 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3277583 | 5 | 121.4696402409 | 31.1530595022 | 25 | 1 | 1 | 15.3 | TDD | 218 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.735 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.751 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:30.889 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.889 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.615 | NREventA2 | measId:1;ServCellPCI:473;Se... |
| 2024-09-20 22:21:34.763 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.030 | NREventA5 | measId:3;ServCellPCI:473;Se... |
| 2024-09-20 22:21:35.098 | NRHandoverAttempt | SourcePCI:473;SourceNR-ARFC... |
| 2024-09-20 22:21:35.118 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.129 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.252 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.252 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257062 | 1 | 14.0305 | 17.4403 | -116.0036 | 19.2668 | 197.8585 | 0.0119 | 0.0139 |
| 2024_09_20 22:00 | 3252266 | 2 | 9.4840 | 14.3787 | -115.8536 | 8.4525 | 160.0657 | 0.0020 | 0.0191 |
| 2024_09_20 22:00 | 3218473 | 3 | 19.2145 | 7.0000 | -115.7591 | 5.9362 | 113.8974 | 0.0046 | 0.0061 |
| 2024_09_20 22:00 | 3226685 | 4 | 19.7635 | 19.5915 | -115.5682 | 19.3346 | 199.6628 | 0.0064 | 0.0094 |
| 2024_09_20 22:00 | 3277583 | 5 | 15.3227 | 7.9519 | -114.8255 | 13.1664 | 173.1990 | 0.0155 | 0.0150 |
| 2024_09_20 22:00 | 3266535 | 6 | 7.9772 | 12.0312 | -115.7375 | 10.5537 | 136.5518 | 0.0171 | 0.0079 |
| 2024_09_20 22:00 | 3263010 | 7 | 5.3935 | 19.0281 | -116.2702 | 3.5313 | 53.7670 | 0.0018 | 0.0074 |
| 2024_09_20 22:00 | 3243281 | 8 | 18.7324 | 14.9418 | -115.5379 | 3.7978 | 32.0998 | 0.0180 | 0.0168 |
| 2024_09_20 22:00 | 3274600 | 9 | 12.8915 | 12.1811 | -117.3420 | 3.2077 | 33.5414 | 0.0101 | 0.0022 |
| 2024_09_20 22:00 | 3262733 | 10 | 9.9143 | 6.6324 | -116.8679 | 4.2769 | 50.2546 | 0.0127 | 0.0099 |
| 2024_09_20 22:00 | 3257371 | 11 | 14.5177 | 5.2924 | -114.0962 | 3.9461 | 53.6234 | 0.0105 | 0.0137 |
| 2024_09_20 22:00 | 3242535 | 12 | 10.7242 | 7.3916 | -115.6204 | 4.6230 | 29.6233 | 0.0199 | 0.0170 |
| 2024_09_20 22:00 | 3252307 | 13 | 16.4376 | 7.3749 | -114.1771 | 3.2843 | 22.7735 | 0.0139 | 0.0006 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412069_E7207FF6 | 152650 | 686 | -92.2 | 152650 | 766 | -95.7 | 152650 | 114 | -103.0 | 152650 | 553 |
| MR_1774412069_F1C90B74 | 152650 | 686 | -91.1 | 152650 | 766 | -97.9 | 152650 | 114 | -100.5 | 152650 | 553 |
| MR_1774412069_4A33E5E8 | 504990 | 857 | -96.2 | 504990 | 100 | -92.5 | 504990 | 815 | -94.1 | 504990 | 218 |
| MR_1774412069_FEECB854 | 152650 | 686 | -91.1 | 152650 | 766 | -97.4 | 152650 | 114 | -102.4 | 152650 | 553 |
| MR_1774412069_019904EE | 152650 | 686 | -90.5 | 152650 | 766 | -97.0 | 152650 | 114 | -101.7 | 152650 | 553 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 512: `f7c7c4ec-32e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f7c7c4ec-32e2-4add-863e-6bd10f9cd8e9` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3216083_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[512] topology](images/train_0512.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3216390_1 by 10 degrees
- `C2`: Lift the tilt angle  of 3216390_1 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216083_4
- `C4`: Press down the tilt angle of 3216083_4 by 5 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase A3 Offset threshold for 3216390_1
- `C7`: Add neighbor relationship between 3254105_2 and 3216390_1
- `C8`: Increase transmission power for 3216390_1
- `C9`: Lift the tilt angle of 3216083_4 by 5 degrees
- `C10`: Adjust the azimuth of 3216083_4 by 35 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216390_1
- `C12`: Decrease transmission power for 3216083_4
- `C13`: Add neighbor relationship between 3216083_4 and 3216390_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216083_4 **← 정답**
- `C15`: Decrease transmission power for 3216390_1
- `C16`: Adjust the azimuth of 3216390_1 by 50 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216390_1
- `C18`: Increase transmission power for 3216083_4
- `C19`: Increase A3 Offset threshold for 3216083_4
- `C20`: Check test server and transmission issues
- `C21`: Decrease A3 Offset threshold for 3216390_1
- `C22`: Decrease A3 Offset threshold for 3216083_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.797 | MS1 | 121.4656741354 | 31.1446203057 | 886 | 504990 | -90.83 | 15.79 | 572.56 | 0.03 | 2.04 | 1562 |
| 2024-09-20 22:21:32.576 | MS1 | 121.4656600538 | 31.1446253402 | 886 | 504990 | -88.91 | 14.12 | 317.55 | 0.06 | 2.55 | 1576 |
| 2024-09-20 22:21:33.721 | MS1 | 121.4656651081 | 31.1446264508 | 886 | 504990 | -85.33 | 16.44 | 459.00 | 0.16 | 2.49 | 1567 |
| 2024-09-20 22:21:34.986 | MS1 | 121.4656693409 | 31.1446258412 | 886 | 504990 | -87.50 | 16.38 | 74.71 | 0.59 | 2.81 | 506 |
| 2024-09-20 22:21:35.309 | MS1 | 121.4656682102 | 31.1446239116 | 886 | 504990 | -88.29 | 12.57 | 79.44 | 0.54 | 2.42 | 602 |
| 2024-09-20 22:21:36.137 | MS1 | 121.4656666211 | 31.1446287868 | 886 | 504990 | -89.22 | 17.13 | 52.52 | 0.51 | 2.73 | 606 |
| 2024-09-20 22:21:37.992 | MS1 | 121.4656733196 | 31.1446328805 | 886 | 504990 | -89.71 | 8.17 | 97.97 | 0.50 | 2.66 | 628 |
| 2024-09-20 22:21:38.920 | MS1 | 121.4656653611 | 31.1446216840 | 886 | 504990 | -89.77 | 9.97 | 80.75 | 0.63 | 2.68 | 609 |
| 2024-09-20 22:21:39.274 | MS1 | 121.4656723449 | 31.1446217694 | 886 | 504990 | -93.28 | 9.73 | 89.45 | 0.52 | 2.32 | 527 |
| 2024-09-20 22:21:40.764 | MS1 | 121.4656687682 | 31.1446350655 | 886 | 504990 | -90.39 | 11.22 | 564.51 | 0.13 | 2.79 | 1564 |
| 2024-09-20 22:21:41.173 | MS1 | 121.4656734567 | 31.1446344906 | 886 | 504990 | -91.70 | 9.30 | 485.88 | 0.14 | 2.01 | 1594 |
| 2024-09-20 22:21:42.140 | MS1 | 121.4656749409 | 31.1446270083 | 886 | 504990 | -93.15 | 7.32 | 386.56 | 0.09 | 2.10 | 1569 |

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
| 3216083 | 4 | 121.4715781876 | 31.1539475992 | 173 | 3 | 5 | 31.4 | TDD | 886 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3216390 | 1 | 121.4703480001 | 31.1455061208 | 87 | 7 | 11 | 49.4 | TDD | 184 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3254105 | 2 | 121.4667776261 | 31.1547325571 | 7 | 6 | 7 | 46.5 | TDD | 241 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3273624 | 3 | 121.4694091227 | 31.1517023231 | 225 | 2 | 10 | 44.9 | TDD | 921 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.275 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.292 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.419 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.419 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.156 | NREventA3 | measId:2;ServCellPCI:865;Se... |
| 2024-09-20 22:21:38.396 | NRHandoverAttempt | SourcePCI:865;SourceNR-ARFC... |
| 2024-09-20 22:21:38.430 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.444 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.553 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.553 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216390 | 1 | 9.8024 | 9.0136 | -117.7127 | 15.6199 | 122.4220 | 0.0143 | 0.0124 |
| 2024_09_20 22:00 | 3254105 | 2 | 17.5414 | 10.1481 | -117.8998 | 6.9695 | 125.0066 | 0.0176 | 0.0016 |
| 2024_09_20 22:00 | 3273624 | 3 | 9.2971 | 6.8348 | -116.2495 | 7.3600 | 80.3943 | 0.0086 | 0.0175 |
| 2024_09_20 22:00 | 3216083 | 4 | 8.4834 | 13.6937 | -114.3146 | 17.3895 | 186.1724 | 0.0015 | 0.0001 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415619_206AD818 | 504990 | 886 | -87.1 | 504990 | 184 | -89.4 | 504990 | 241 | -101.2 | 504990 | 921 |
| MR_1774415619_559F5B40 | 504990 | 886 | -87.2 | 504990 | 184 | -87.1 | 504990 | 241 | -100.9 | 504990 | 921 |
| MR_1774415619_5C891D7E | 504990 | 886 | -86.3 | 504990 | 184 | -86.8 | 504990 | 241 | -100.7 | 504990 | 921 |
| MR_1774415619_6CB5E671 | 504990 | 886 | -86.4 | 504990 | 184 | -87.3 | 504990 | 241 | -99.4 | 504990 | 921 |
| MR_1774415619_45BEE546 | 504990 | 886 | -88.1 | 504990 | 184 | -87.8 | 504990 | 241 | -99.4 | 504990 | 921 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 513: `61c8e42d-92c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `61c8e42d-92c8-4d3f-afef-e9b7124c82ce` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218336_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[513] topology](images/train_0513.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3218336_1 by 6 degrees
- `C2`: Press down the tilt angle of 3218336_1 by 6 degrees
- `C3`: Increase A3 Offset threshold for 3250323_2
- `C4`: Lift the tilt angle  of 3250323_2 by 2 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218336_1
- `C6`: Press down the tilt angle  of 3250323_2 by 2 degrees
- `C7`: Decrease A3 Offset threshold for 3218336_1
- `C8`: Adjust the azimuth of 3218336_1 by 12 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250323_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250323_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218336_1 **← 정답**
- `C12`: Decrease transmission power for 3250323_2
- `C13`: Decrease transmission power for 3218336_1
- `C14`: Add neighbor relationship between 3218336_1 and 3250323_2
- `C15`: Adjust the azimuth of 3250323_2 by 43 degrees
- `C16`: Decrease A3 Offset threshold for 3250323_2
- `C17`: Add neighbor relationship between 3245898_11 and 3250323_2
- `C18`: Increase transmission power for 3250323_2
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Check test server and transmission issues
- `C21`: Increase A3 Offset threshold for 3218336_1
- `C22`: Increase transmission power for 3218336_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.304 | MS1 | 121.4656738759 | 31.1446243102 | 512 | 504990 | -95.65 | 9.50 | 317.93 | 0.09 | 2.32 | 1566 |
| 2024-09-20 22:21:32.291 | MS1 | 121.4656734094 | 31.1446305261 | 446 | 504990 | -95.12 | 14.94 | 345.13 | 0.18 | 2.57 | 1598 |
| 2024-09-20 22:21:33.846 | MS1 | 121.4656664019 | 31.1446311420 | 517 | 504990 | -95.29 | 9.39 | 346.55 | 0.10 | 2.54 | 1579 |
| 2024-09-20 22:21:34.700 | MS1 | 121.4656643341 | 31.1446320544 | 36 | 152650 | -91.41 | 6.95 | 97.81 | 0.19 | 1.96 | 908 |
| 2024-09-20 22:21:35.521 | MS1 | 121.4656727527 | 31.1446205134 | 814 | 152650 | -89.39 | 7.73 | 88.94 | 0.12 | 1.98 | 989 |
| 2024-09-20 22:21:36.972 | MS1 | 121.4656600034 | 31.1446191113 | 324 | 152650 | -91.63 | 4.94 | 68.51 | 0.18 | 1.73 | 971 |
| 2024-09-20 22:21:37.464 | MS1 | 121.4656675901 | 31.1446361610 | 98 | 152650 | -93.68 | 6.61 | 90.67 | 0.04 | 1.58 | 902 |
| 2024-09-20 22:21:38.887 | MS1 | 121.4656682499 | 31.1446305775 | 36 | 152650 | -90.39 | 5.56 | 65.60 | 0.20 | 1.94 | 911 |
| 2024-09-20 22:21:39.609 | MS1 | 121.4656755733 | 31.1446376393 | 814 | 152650 | -91.22 | 3.27 | 65.58 | 0.13 | 1.52 | 942 |
| 2024-09-20 22:21:40.293 | MS1 | 121.4656751447 | 31.1446368595 | 324 | 152650 | -92.43 | 7.45 | 82.71 | 0.16 | 2.34 | 1567 |
| 2024-09-20 22:21:41.252 | MS1 | 121.4656629606 | 31.1446237849 | 98 | 152650 | -89.67 | 3.17 | 90.42 | 0.07 | 2.31 | 1591 |
| 2024-09-20 22:21:42.306 | MS1 | 121.4656590970 | 31.1446355513 | 36 | 152650 | -92.08 | 3.47 | 58.49 | 0.03 | 2.81 | 1562 |

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
| 3210346 | 3 | 121.4702811619 | 31.1452730345 | 44 | 7 | 9 | 9.2 | TDD | 517 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3218336 | 1 | 121.4653454944 | 31.1510616952 | 166 | 4 | 0 | 19.1 | TDD | 512 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3232954 | 12 | 121.4718357292 | 31.1458748858 | 261 | 12 | 6 | 0.5 | FDD | 814 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3236980 | 8 | 121.4717766846 | 31.1443137403 | 142 | 1 | 0 | 17.9 | FDD | 98 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3244748 | 5 | 121.4698388259 | 31.1460937551 | 275 | 3 | 4 | 22.2 | TDD | 977 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3245898 | 11 | 121.4667046903 | 31.1492815350 | 162 | 8 | 5 | 7.6 | FDD | 324 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3246067 | 10 | 121.4730994683 | 31.1479309142 | 186 | 6 | 3 | 23.2 | FDD | 36 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3248150 | 4 | 121.4734411057 | 31.1450552608 | 181 | 1 | 12 | 2.0 | TDD | 750 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3250323 | 2 | 121.4728001936 | 31.1516494142 | 178 | 2 | 4 | 1.6 | TDD | 128 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3251277 | 9 | 121.4668344938 | 31.1521963546 | 1 | 9 | 2 | 7.9 | FDD | 131 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3253594 | 13 | 121.4712303689 | 31.1530069912 | 22 | 12 | 3 | 7.7 | FDD | 954 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3260561 | 6 | 121.4706732198 | 31.1461913343 | 273 | 1 | 0 | 21.0 | TDD | 446 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3270149 | 7 | 121.4748477008 | 31.1515278024 | 224 | 15 | 10 | 29.7 | FDD | 224 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |

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
| 2024-09-20 22:21:31.145 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.165 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.288 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.288 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.034 | NREventA2 | measId:1;ServCellPCI:75;Ser... |
| 2024-09-20 22:21:35.161 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.456 | NREventA5 | measId:3;ServCellPCI:75;Ser... |
| 2024-09-20 22:21:35.489 | NRHandoverAttempt | SourcePCI:75;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.530 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.543 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.686 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.686 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218336 | 1 | 12.9946 | 7.3017 | -114.1600 | 11.7941 | 93.3696 | 0.0073 | 0.0171 |
| 2024_09_20 22:00 | 3250323 | 2 | 15.9215 | 5.5983 | -114.5308 | 11.2836 | 166.2038 | 0.0192 | 0.0034 |
| 2024_09_20 22:00 | 3210346 | 3 | 19.4789 | 8.3822 | -116.5787 | 9.7046 | 121.2782 | 0.0187 | 0.0067 |
| 2024_09_20 22:00 | 3248150 | 4 | 10.2921 | 5.4771 | -116.6902 | 18.3982 | 179.5058 | 0.0074 | 0.0138 |
| 2024_09_20 22:00 | 3244748 | 5 | 13.2901 | 13.8907 | -116.2704 | 6.6864 | 147.4851 | 0.0070 | 0.0047 |
| 2024_09_20 22:00 | 3260561 | 6 | 10.1895 | 10.9216 | -116.1629 | 15.8805 | 159.9856 | 0.0015 | 0.0023 |
| 2024_09_20 22:00 | 3270149 | 7 | 10.2342 | 19.9840 | -117.4410 | 3.9441 | 42.3859 | 0.0167 | 0.0002 |
| 2024_09_20 22:00 | 3236980 | 8 | 5.9448 | 10.7275 | -115.8628 | 3.9474 | 21.5414 | 0.0087 | 0.0148 |
| 2024_09_20 22:00 | 3251277 | 9 | 8.1730 | 6.2747 | -116.2836 | 3.1062 | 34.2778 | 0.0027 | 0.0190 |
| 2024_09_20 22:00 | 3246067 | 10 | 8.2694 | 17.1784 | -117.3343 | 3.0655 | 58.5217 | 0.0001 | 0.0064 |
| 2024_09_20 22:00 | 3245898 | 11 | 6.3719 | 9.3099 | -117.5473 | 4.2401 | 37.0802 | 0.0081 | 0.0168 |
| 2024_09_20 22:00 | 3232954 | 12 | 12.0030 | 6.7850 | -116.0384 | 3.6803 | 20.1490 | 0.0027 | 0.0184 |
| 2024_09_20 22:00 | 3253594 | 13 | 5.2269 | 8.5316 | -114.7391 | 4.4061 | 21.7596 | 0.0066 | 0.0075 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412115_F350E201 | 152650 | 36 | -93.1 | 152650 | 224 | -97.5 | 152650 | 954 | -100.1 | 152650 | 131 |
| MR_1774412115_C3127107 | 152650 | 36 | -92.0 | 152650 | 224 | -97.6 | 152650 | 954 | -99.1 | 152650 | 131 |
| MR_1774412115_DD82168C | 152650 | 36 | -92.6 | 152650 | 224 | -98.9 | 152650 | 954 | -97.4 | 152650 | 131 |
| MR_1774412115_DFC51425 | 504990 | 517 | -96.9 | 504990 | 128 | -94.5 | 504990 | 750 | -100.5 | 504990 | 977 |
| MR_1774412115_1FB142B2 | 504990 | 517 | -95.2 | 504990 | 128 | -95.1 | 504990 | 750 | -99.8 | 504990 | 977 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 514: `a8e205b7-5be...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a8e205b7-5beb-45df-acbc-2b0905806af3` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[514] topology](images/train_0514.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261156_1
- `C2`: Decrease transmission power for 3234612_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261156_1
- `C4`: Add neighbor relationship between 3261156_1 and 3234612_4
- `C5`: Lift the tilt angle of 3261156_1 by 2 degrees
- `C6`: Adjust the azimuth of 3261156_1 by 19 degrees
- `C7`: Increase transmission power for 3261156_1
- `C8`: Press down the tilt angle of 3261156_1 by 2 degrees
- `C9`: Increase A3 Offset threshold for 3234612_4
- `C10`: Increase A3 Offset threshold for 3261156_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234612_4
- `C12`: Adjust the azimuth of 3234612_4 by 50 degrees
- `C13`: Decrease A3 Offset threshold for 3234612_4
- `C14`: Decrease A3 Offset threshold for 3261156_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Check test server and transmission issues **← 정답**
- `C17`: Decrease transmission power for 3261156_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234612_4
- `C19`: Increase transmission power for 3234612_4
- `C20`: Press down the tilt angle  of 3234612_4 by 7 degrees
- `C21`: Add neighbor relationship between 3211975_3 and 3234612_4
- `C22`: Lift the tilt angle  of 3234612_4 by 7 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.608 | MS1 | 121.4656632015 | 31.1446354884 | 781 | 504990 | -88.34 | 12.84 | 592.16 | 0.00 | 2.90 | 1597 |
| 2024-09-20 22:21:32.547 | MS1 | 121.4656629060 | 31.1446188466 | 781 | 504990 | -91.32 | 17.24 | 461.10 | 0.05 | 2.19 | 1572 |
| 2024-09-20 22:21:33.250 | MS1 | 121.4656637000 | 31.1446195754 | 781 | 504990 | -91.10 | 14.84 | 380.46 | 0.20 | 2.15 | 1586 |
| 2024-09-20 22:21:34.132 | MS1 | 121.4656599802 | 31.1446255769 | 781 | 504990 | -86.61 | 13.23 | 65.04 | 0.09 | 2.15 | 431 |
| 2024-09-20 22:21:35.753 | MS1 | 121.4656584237 | 31.1446370274 | 781 | 504990 | -89.06 | 15.19 | 60.43 | 0.02 | 2.92 | 407 |
| 2024-09-20 22:21:36.920 | MS1 | 121.4656683609 | 31.1446369726 | 781 | 504990 | -89.46 | 15.71 | 69.31 | 0.06 | 2.94 | 320 |
| 2024-09-20 22:21:37.501 | MS1 | 121.4656591465 | 31.1446376398 | 781 | 504990 | -92.87 | 12.20 | 65.74 | 0.16 | 2.79 | 345 |
| 2024-09-20 22:21:38.831 | MS1 | 121.4656696600 | 31.1446222540 | 781 | 504990 | -90.59 | 9.50 | 68.90 | 0.12 | 2.23 | 419 |
| 2024-09-20 22:21:39.762 | MS1 | 121.4656581303 | 31.1446314301 | 781 | 504990 | -89.73 | 7.08 | 75.43 | 0.19 | 2.46 | 366 |
| 2024-09-20 22:21:40.738 | MS1 | 121.4656750878 | 31.1446269354 | 781 | 504990 | -90.33 | 9.27 | 591.32 | 0.18 | 2.19 | 1585 |
| 2024-09-20 22:21:41.371 | MS1 | 121.4656759139 | 31.1446312031 | 781 | 504990 | -90.10 | 9.20 | 489.25 | 0.10 | 2.19 | 1561 |
| 2024-09-20 22:21:42.410 | MS1 | 121.4656742876 | 31.1446363562 | 781 | 504990 | -92.63 | 8.78 | 444.67 | 0.07 | 2.10 | 1571 |

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
| 3211975 | 3 | 121.4701821734 | 31.1440338052 | 39 | 1 | 12 | 29.0 | TDD | 227 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3234612 | 4 | 121.4758768857 | 31.1466770314 | 131 | 4 | 2 | 45.2 | TDD | 845 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3240566 | 2 | 121.4647257849 | 31.1517935226 | 64 | 0 | 11 | 47.1 | TDD | 906 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3261156 | 1 | 121.4658277862 | 31.1545992287 | 200 | 0 | 12 | 36.7 | TDD | 781 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.387 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.403 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.548 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.548 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.228 | NREventA3 | measId:2;ServCellPCI:291;Se... |
| 2024-09-20 22:21:38.468 | NRHandoverAttempt | SourcePCI:291;SourceNR-ARFC... |
| 2024-09-20 22:21:38.500 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.511 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.613 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.613 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261156 | 1 | 11.9399 | 17.2169 | -115.1717 | 19.6608 | 171.6411 | 0.0152 | 0.0043 |
| 2024_09_20 22:00 | 3240566 | 2 | 16.3962 | 12.0226 | -115.2670 | 19.2665 | 159.8971 | 0.0020 | 0.0065 |
| 2024_09_20 22:00 | 3211975 | 3 | 10.3200 | 5.1755 | -115.0211 | 14.7882 | 112.6853 | 0.0149 | 0.0187 |
| 2024_09_20 22:00 | 3234612 | 4 | 8.6983 | 5.3932 | -114.0648 | 19.4972 | 140.1525 | 0.0168 | 0.0024 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414120_31297974 | 504990 | 781 | -85.7 | 504990 | 845 | -89.0 | 504990 | 227 | -91.2 | 504990 | 906 |
| MR_1774414120_C534FF7E | 504990 | 781 | -87.7 | 504990 | 845 | -87.1 | 504990 | 227 | -93.9 | 504990 | 906 |
| MR_1774414120_5A434113 | 504990 | 781 | -86.7 | 504990 | 845 | -86.2 | 504990 | 227 | -94.8 | 504990 | 906 |
| MR_1774414120_F973A64C | 504990 | 781 | -86.2 | 504990 | 845 | -86.5 | 504990 | 227 | -91.6 | 504990 | 906 |
| MR_1774414120_9367F92B | 504990 | 781 | -85.3 | 504990 | 845 | -86.3 | 504990 | 227 | -92.8 | 504990 | 906 |
| MR_1774414120_AAD8E7E9 | 504990 | 781 | -87.8 | 504990 | 845 | -87.3 | 504990 | 227 | -94.0 | 504990 | 906 |
| MR_1774414120_06C8F690 | 504990 | 781 | -86.7 | 504990 | 845 | -85.7 | 504990 | 227 | -94.1 | 504990 | 906 |
| MR_1774414120_EA541F32 | 504990 | 781 | -85.4 | 504990 | 845 | -89.2 | 504990 | 227 | -92.2 | 504990 | 906 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 515: `7eb4f1d8-36e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7eb4f1d8-36e0-4db7-b64f-8f0c08d59063` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Lift the tilt angle  of 3261051_4 by 5 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[515] topology](images/train_0515.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3254361_1
- `C2`: Add neighbor relationship between 3233989_2 and 3254361_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Adjust the azimuth of 3233989_2 by 2 degrees
- `C5`: Increase transmission power for 3233989_2
- `C6`: Lift the tilt angle of 3233989_2 by 4 degrees
- `C7`: Lift the tilt angle  of 3261051_4 by 5 degrees **← 정답**
- `C8`: Check test server and transmission issues
- `C9`: Press down the tilt angle  of 3261051_4 by 5 degrees
- `C10`: Increase A3 Offset threshold for 3254361_1
- `C11`: Add neighbor relationship between 3261051_4 and 3254361_1
- `C12`: Press down the tilt angle of 3233989_2 by 4 degrees
- `C13`: Increase A3 Offset threshold for 3233989_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254361_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254361_1
- `C16`: Decrease A3 Offset threshold for 3254361_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233989_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233989_2
- `C19`: Adjust the azimuth of 3261051_4 by 50 degrees
- `C20`: Decrease transmission power for 3233989_2
- `C21`: Decrease A3 Offset threshold for 3233989_2
- `C22`: Increase transmission power for 3254361_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.732 | MS1 | 121.4656760116 | 31.1446270423 | 530 | 504990 | -88.65 | 12.72 | 425.16 | 0.18 | 2.44 | 1568 |
| 2024-09-20 22:21:32.352 | MS1 | 121.4656768268 | 31.1446356807 | 530 | 504990 | -91.12 | 16.95 | 531.24 | 0.06 | 2.43 | 1568 |
| 2024-09-20 22:21:33.254 | MS1 | 121.4656584848 | 31.1446213546 | 530 | 504990 | -86.68 | 12.87 | 309.09 | 0.04 | 2.23 | 1587 |
| 2024-09-20 22:21:34.284 | MS1 | 121.4656665332 | 31.1446318248 | 530 | 504990 | -85.23 | 14.15 | 91.40 | 0.10 | 2.54 | 1561 |
| 2024-09-20 22:21:35.281 | MS1 | 121.4656582745 | 31.1446369122 | 530 | 504990 | -90.17 | 13.49 | 95.66 | 0.14 | 2.12 | 1570 |
| 2024-09-20 22:21:36.976 | MS1 | 121.4656669831 | 31.1446270490 | 530 | 504990 | -87.59 | 15.33 | 65.98 | 0.01 | 2.93 | 1584 |
| 2024-09-20 22:21:37.529 | MS1 | 121.4656657992 | 31.1446242940 | 530 | 504990 | -92.28 | 8.12 | 84.61 | 0.15 | 2.58 | 1594 |
| 2024-09-20 22:21:38.759 | MS1 | 121.4656747186 | 31.1446229786 | 530 | 504990 | -89.22 | 11.12 | 68.38 | 0.02 | 2.72 | 1567 |
| 2024-09-20 22:21:39.784 | MS1 | 121.4656712589 | 31.1446236725 | 530 | 504990 | -90.22 | 9.19 | 94.27 | 0.16 | 2.71 | 1579 |
| 2024-09-20 22:21:40.215 | MS1 | 121.4656726823 | 31.1446370887 | 530 | 504990 | -89.36 | 8.87 | 503.35 | 0.09 | 2.01 | 1586 |
| 2024-09-20 22:21:41.694 | MS1 | 121.4656689207 | 31.1446250218 | 530 | 504990 | -93.46 | 9.97 | 424.27 | 0.16 | 2.65 | 1572 |
| 2024-09-20 22:21:42.204 | MS1 | 121.4656727035 | 31.1446376684 | 530 | 504990 | -89.18 | 12.91 | 390.82 | 0.13 | 2.10 | 1565 |

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
| 3233989 | 2 | 121.4739662416 | 31.1457020550 | 263 | 3 | 12 | 16.6 | TDD | 530 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3254361 | 1 | 121.4717216320 | 31.1456731352 | 312 | 2 | 6 | 27.1 | TDD | 936 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3261051 | 4 | 121.4737142082 | 31.1550915333 | 89 | 3 | 3 | 46.3 | TDD | 501 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3266317 | 3 | 121.4675956026 | 31.1525439013 | 92 | 11 | 3 | 34.1 | TDD | 611 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.094 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.118 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.247 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.247 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.975 | NREventA3 | measId:2;ServCellPCI:528;Se... |
| 2024-09-20 22:21:38.215 | NRHandoverAttempt | SourcePCI:528;SourceNR-ARFC... |
| 2024-09-20 22:21:38.264 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.274 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.420 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.420 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254361 | 1 | 10.7056 | 14.5430 | -114.6918 | 7.4082 | 125.4881 | 0.0047 | 0.0198 |
| 2024_09_20 22:00 | 3233989 | 2 | 81.6731 | 83.3479 | -115.9838 | 7.8232 | 98.2020 | 0.0023 | 0.0112 |
| 2024_09_20 22:00 | 3266317 | 3 | 17.1462 | 18.1063 | -116.2901 | 11.8600 | 189.8476 | 0.0155 | 0.0113 |
| 2024_09_20 22:00 | 3261051 | 4 | 7.4422 | 17.4827 | -117.6937 | 18.2118 | 148.4800 | 0.0017 | 0.0155 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413399_33F80BCE | 504990 | 530 | -86.1 | 504990 | 936 | -87.2 | 504990 | 501 | -98.5 | 504990 | 611 |
| MR_1774413399_1660242E | 504990 | 530 | -86.0 | 504990 | 936 | -87.2 | 504990 | 501 | -96.5 | 504990 | 611 |
| MR_1774413399_6F57B99E | 504990 | 530 | -86.3 | 504990 | 936 | -86.1 | 504990 | 501 | -96.7 | 504990 | 611 |
| MR_1774413399_9B2E933D | 504990 | 530 | -85.5 | 504990 | 936 | -87.2 | 504990 | 501 | -98.5 | 504990 | 611 |
| MR_1774413399_5EDB3160 | 504990 | 530 | -86.0 | 504990 | 936 | -88.3 | 504990 | 501 | -99.3 | 504990 | 611 |
| MR_1774413399_0455535A | 504990 | 530 | -83.4 | 504990 | 936 | -86.1 | 504990 | 501 | -98.3 | 504990 | 611 |
| MR_1774413399_2D7EF791 | 504990 | 530 | -85.7 | 504990 | 936 | -86.6 | 504990 | 501 | -98.0 | 504990 | 611 |
| MR_1774413399_17BDF33B | 504990 | 530 | -85.5 | 504990 | 936 | -87.1 | 504990 | 501 | -100.2 | 504990 | 611 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 516: `6e33e036-f81...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6e33e036-f810-408d-ba7a-bf681269d915` |
| Tag | **multiple-answer** |
| 정답 | **C2|C4** |
| C2 의미 | Increase transmission power for 3228950_4 |
| C4 의미 | Adjust the azimuth of 3228950_4 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[516] topology](images/train_0516.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228950_4
- `C2`: Increase transmission power for 3228950_4 **← 정답**
- `C3`: Decrease transmission power for 3228950_4
- `C4`: Adjust the azimuth of 3228950_4 by 50 degrees **← 정답**
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228950_4
- `C6`: Decrease A3 Offset threshold for 3213938_2
- `C7`: Increase A3 Offset threshold for 3228950_4
- `C8`: Increase A3 Offset threshold for 3213938_2
- `C9`: Press down the tilt angle  of 3213938_2 by 6 degrees
- `C10`: Decrease A3 Offset threshold for 3228950_4
- `C11`: Lift the tilt angle of 3228950_4 by 10 degrees
- `C12`: Check test server and transmission issues
- `C13`: Increase transmission power for 3213938_2
- `C14`: Press down the tilt angle of 3228950_4 by 10 degrees
- `C15`: Decrease transmission power for 3213938_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213938_2
- `C18`: Add neighbor relationship between 3215484_1 and 3213938_2
- `C19`: Lift the tilt angle  of 3213938_2 by 6 degrees
- `C20`: Add neighbor relationship between 3228950_4 and 3213938_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213938_2
- `C22`: Adjust the azimuth of 3213938_2 by 27 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.650 | MS1 | 121.4656597918 | 31.1446243979 | 599 | 504990 | -93.80 | 17.45 | 553.75 | 0.06 | 2.30 | 1568 |
| 2024-09-20 22:21:32.317 | MS1 | 121.4656667094 | 31.1446187549 | 599 | 504990 | -87.95 | 17.84 | 507.55 | 0.19 | 2.61 | 1563 |
| 2024-09-20 22:21:33.722 | MS1 | 121.4656673307 | 31.1446249437 | 599 | 504990 | -85.28 | 13.28 | 299.09 | 0.07 | 2.05 | 1573 |
| 2024-09-20 22:21:34.850 | MS1 | 121.4656621683 | 31.1446191353 | 599 | 504990 | -109.29 | 1.65 | 69.88 | 0.10 | 1.31 | 1576 |
| 2024-09-20 22:21:35.576 | MS1 | 121.4656631191 | 31.1446377078 | 599 | 504990 | -100.67 | 0.36 | 39.40 | 0.05 | 1.24 | 1589 |
| 2024-09-20 22:21:36.496 | MS1 | 121.4656656047 | 31.1446364782 | 599 | 504990 | -106.27 | -0.02 | 50.29 | 0.06 | 1.37 | 1593 |
| 2024-09-20 22:21:37.269 | MS1 | 121.4656648597 | 31.1446209615 | 599 | 504990 | -107.78 | -0.26 | 44.94 | 0.07 | 1.37 | 1563 |
| 2024-09-20 22:21:38.210 | MS1 | 121.4656675341 | 31.1446327096 | 599 | 504990 | -101.27 | -1.24 | 30.23 | 0.04 | 1.26 | 1600 |
| 2024-09-20 22:21:39.608 | MS1 | 121.4656663924 | 31.1446293157 | 599 | 504990 | -109.31 | 1.78 | 60.06 | 0.14 | 1.44 | 1578 |
| 2024-09-20 22:21:40.164 | MS1 | 121.4656721975 | 31.1446234523 | 599 | 504990 | -90.81 | 16.75 | 397.79 | 0.11 | 2.41 | 1593 |
| 2024-09-20 22:21:41.390 | MS1 | 121.4656695846 | 31.1446313691 | 599 | 504990 | -93.44 | 14.51 | 501.49 | 0.15 | 2.66 | 1566 |
| 2024-09-20 22:21:42.558 | MS1 | 121.4656580617 | 31.1446217143 | 599 | 504990 | -92.36 | 17.70 | 481.83 | 0.13 | 2.05 | 1580 |

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
| 3213938 | 2 | 121.4743619478 | 31.1549691110 | 243 | 5 | 11 | 20.8 | TDD | 323 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3215484 | 1 | 121.4675710775 | 31.1556667523 | 348 | 6 | 3 | 25.5 | TDD | 865 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3224301 | 3 | 121.4713449798 | 31.1484333500 | 354 | 13 | 10 | 44.9 | TDD | 614 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3228950 | 4 | 121.4646021559 | 31.1476390281 | 94 | 7 | 2 | 38.0 | TDD | 599 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.304 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.321 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.439 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.439 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.665 | NREventA2 | measId:1;ServCellPCI:761;Se... |
| 2024-09-20 22:21:34.784 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215484 | 1 | 8.3535 | 11.6597 | -117.3227 | 5.4071 | 188.6296 | 0.0096 | 0.0101 |
| 2024_09_20 22:00 | 3213938 | 2 | 5.1434 | 16.6250 | -115.1465 | 14.0180 | 163.2428 | 0.0110 | 0.0011 |
| 2024_09_20 22:00 | 3224301 | 3 | 10.2043 | 9.4210 | -116.7381 | 5.9616 | 81.6358 | 0.0175 | 0.0120 |
| 2024_09_20 22:00 | 3228950 | 4 | 8.4428 | 7.4474 | -116.7698 | 6.2990 | 81.0448 | 0.1077 | 0.0016 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414020_F1330564 | 504990 | 599 | -109.8 | 504990 | 323 | -110.5 | 504990 | 865 | -119.2 | 504990 | 614 |
| MR_1774414020_8444CFD0 | 504990 | 599 | -107.7 | 504990 | 323 | -114.3 | 504990 | 865 | -118.3 | 504990 | 614 |
| MR_1774414020_B54C67CC | 504990 | 599 | -110.7 | 504990 | 323 | -112.7 | 504990 | 865 | -118.9 | 504990 | 614 |
| MR_1774414020_E5578CA2 | 504990 | 599 | -110.1 | 504990 | 323 | -112.2 | 504990 | 865 | -116.7 | 504990 | 614 |
| MR_1774414020_CF5FBE2F | 504990 | 599 | -110.8 | 504990 | 323 | -110.8 | 504990 | 865 | -118.5 | 504990 | 614 |
| MR_1774414020_5EDC5F20 | 504990 | 599 | -108.2 | 504990 | 323 | -110.9 | 504990 | 865 | -116.3 | 504990 | 614 |
| MR_1774414020_11C34D67 | 504990 | 599 | -107.9 | 504990 | 323 | -114.3 | 504990 | 865 | -118.3 | 504990 | 614 |
| MR_1774414020_691D9F3E | 504990 | 599 | -109.4 | 504990 | 323 | -110.8 | 504990 | 865 | -118.7 | 504990 | 614 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 517: `b5b928a8-8e4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b5b928a8-8e48-4a87-b2b0-74886e47cc23` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3249173_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[517] topology](images/train_0517.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3249173_4 and 3261425_3
- `C2`: Decrease A3 Offset threshold for 3261425_3
- `C3`: Adjust the azimuth of 3249173_4 by 27 degrees
- `C4`: Add neighbor relationship between 3237938_1 and 3261425_3
- `C5`: Press down the tilt angle of 3249173_4 by 3 degrees
- `C6`: Check test server and transmission issues
- `C7`: Lift the tilt angle  of 3261425_3 by 2 degrees
- `C8`: Lift the tilt angle of 3249173_4 by 3 degrees
- `C9`: Decrease A3 Offset threshold for 3249173_4
- `C10`: Increase A3 Offset threshold for 3249173_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249173_4
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249173_4 **← 정답**
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261425_3
- `C15`: Press down the tilt angle  of 3261425_3 by 2 degrees
- `C16`: Increase transmission power for 3261425_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261425_3
- `C18`: Decrease transmission power for 3249173_4
- `C19`: Increase A3 Offset threshold for 3261425_3
- `C20`: Adjust the azimuth of 3261425_3 by 50 degrees
- `C21`: Decrease transmission power for 3261425_3
- `C22`: Increase transmission power for 3249173_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.191 | MS1 | 121.4656620829 | 31.1446193437 | 362 | 504990 | -87.31 | 15.75 | 410.54 | 0.20 | 2.75 | 1584 |
| 2024-09-20 22:21:32.410 | MS1 | 121.4656640779 | 31.1446348248 | 362 | 504990 | -89.30 | 16.07 | 494.18 | 0.02 | 2.87 | 1589 |
| 2024-09-20 22:21:33.721 | MS1 | 121.4656703086 | 31.1446222255 | 362 | 504990 | -88.85 | 16.69 | 491.45 | 0.01 | 2.56 | 1587 |
| 2024-09-20 22:21:34.645 | MS1 | 121.4656593946 | 31.1446331311 | 362 | 504990 | -90.93 | 15.35 | 56.71 | 0.57 | 2.17 | 565 |
| 2024-09-20 22:21:35.937 | MS1 | 121.4656607756 | 31.1446248846 | 362 | 504990 | -85.73 | 13.89 | 88.59 | 0.59 | 2.98 | 692 |
| 2024-09-20 22:21:36.438 | MS1 | 121.4656721118 | 31.1446317507 | 362 | 504990 | -91.24 | 13.08 | 48.93 | 0.64 | 2.31 | 527 |
| 2024-09-20 22:21:37.224 | MS1 | 121.4656707812 | 31.1446250016 | 362 | 504990 | -93.74 | 12.38 | 42.85 | 0.52 | 2.31 | 601 |
| 2024-09-20 22:21:38.503 | MS1 | 121.4656735539 | 31.1446191257 | 362 | 504990 | -89.27 | 11.13 | 75.12 | 0.65 | 2.78 | 649 |
| 2024-09-20 22:21:39.757 | MS1 | 121.4656679186 | 31.1446195216 | 362 | 504990 | -91.18 | 7.70 | 85.70 | 0.58 | 2.51 | 697 |
| 2024-09-20 22:21:40.825 | MS1 | 121.4656745923 | 31.1446339092 | 362 | 504990 | -93.02 | 10.25 | 384.58 | 0.05 | 2.17 | 1594 |
| 2024-09-20 22:21:41.660 | MS1 | 121.4656724617 | 31.1446304490 | 362 | 504990 | -90.02 | 8.46 | 350.50 | 0.11 | 2.22 | 1565 |
| 2024-09-20 22:21:42.604 | MS1 | 121.4656628605 | 31.1446252822 | 362 | 504990 | -90.16 | 9.52 | 432.18 | 0.01 | 2.29 | 1599 |

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
| 3237938 | 1 | 121.4699110540 | 31.1477907641 | 90 | 6 | 7 | 18.2 | TDD | 86 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3249173 | 4 | 121.4642145102 | 31.1510782036 | 142 | 1 | 12 | 29.8 | TDD | 362 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3261425 | 3 | 121.4662196754 | 31.1515293061 | 320 | 0 | 7 | 30.2 | TDD | 4 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3279286 | 2 | 121.4755110371 | 31.1482657413 | 199 | 12 | 8 | 49.0 | TDD | 210 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.380 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.395 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.532 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.532 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.276 | NREventA3 | measId:2;ServCellPCI:744;Se... |
| 2024-09-20 22:21:38.516 | NRHandoverAttempt | SourcePCI:744;SourceNR-ARFC... |
| 2024-09-20 22:21:38.563 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.576 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.722 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.722 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237938 | 1 | 7.7374 | 5.3136 | -115.3220 | 7.4236 | 173.5533 | 0.0039 | 0.0094 |
| 2024_09_20 22:00 | 3279286 | 2 | 5.0637 | 7.3459 | -117.4161 | 15.3202 | 93.7325 | 0.0188 | 0.0094 |
| 2024_09_20 22:00 | 3261425 | 3 | 6.3366 | 5.2182 | -114.0598 | 11.1791 | 142.8768 | 0.0073 | 0.0079 |
| 2024_09_20 22:00 | 3249173 | 4 | 15.8146 | 8.7434 | -114.4507 | 15.6877 | 169.3585 | 0.0082 | 0.0107 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415298_7EF3B32E | 504990 | 362 | -90.2 | 504990 | 4 | -95.8 | 504990 | 86 | -99.5 | 504990 | 210 |
| MR_1774415298_588B4A21 | 504990 | 362 | -92.5 | 504990 | 4 | -96.0 | 504990 | 86 | -99.7 | 504990 | 210 |
| MR_1774415298_A8D2F996 | 504990 | 362 | -92.3 | 504990 | 4 | -95.5 | 504990 | 86 | -98.4 | 504990 | 210 |
| MR_1774415298_3624F737 | 504990 | 362 | -89.0 | 504990 | 4 | -93.9 | 504990 | 86 | -101.1 | 504990 | 210 |
| MR_1774415298_C1BACCEA | 504990 | 362 | -92.4 | 504990 | 4 | -95.1 | 504990 | 86 | -100.5 | 504990 | 210 |
| MR_1774415298_1C35B733 | 504990 | 362 | -89.9 | 504990 | 4 | -95.1 | 504990 | 86 | -98.3 | 504990 | 210 |
| MR_1774415298_8D1613AF | 504990 | 362 | -92.1 | 504990 | 4 | -95.2 | 504990 | 86 | -99.8 | 504990 | 210 |
| MR_1774415298_81CEDE27 | 504990 | 362 | -90.6 | 504990 | 4 | -92.7 | 504990 | 86 | -100.6 | 504990 | 210 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 518: `3628824d-93a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3628824d-93a8-41fd-a50b-2e72fe2f948c` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[518] topology](images/train_0518.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3274884_3 and 3224978_2
- `C2`: Increase transmission power for 3224978_2
- `C3`: Press down the tilt angle  of 3224978_2 by 5 degrees
- `C4`: Adjust the azimuth of 3224978_2 by 31 degrees
- `C5`: Decrease A3 Offset threshold for 3274884_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274884_3
- `C7`: Check test server and transmission issues **← 정답**
- `C8`: Decrease transmission power for 3224978_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224978_2
- `C10`: Adjust the azimuth of 3274884_3 by 47 degrees
- `C11`: Lift the tilt angle  of 3224978_2 by 5 degrees
- `C12`: Lift the tilt angle of 3274884_3 by 10 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274884_3
- `C14`: Increase A3 Offset threshold for 3224978_2
- `C15`: Increase transmission power for 3274884_3
- `C16`: Increase A3 Offset threshold for 3274884_3
- `C17`: Decrease transmission power for 3274884_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224978_2
- `C19`: Decrease A3 Offset threshold for 3224978_2
- `C20`: Add neighbor relationship between 3240809_1 and 3224978_2
- `C21`: Press down the tilt angle of 3274884_3 by 10 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.638 | MS1 | 121.4656589721 | 31.1446297316 | 883 | 504990 | -89.58 | 15.96 | 424.88 | 0.08 | 2.20 | 1576 |
| 2024-09-20 22:21:32.810 | MS1 | 121.4656766743 | 31.1446317048 | 883 | 504990 | -85.03 | 13.73 | 430.16 | 0.06 | 2.21 | 1584 |
| 2024-09-20 22:21:33.862 | MS1 | 121.4656585116 | 31.1446217475 | 883 | 504990 | -88.08 | 14.68 | 440.19 | 0.01 | 2.27 | 1583 |
| 2024-09-20 22:21:34.194 | MS1 | 121.4656736129 | 31.1446240228 | 883 | 504990 | -91.47 | 13.17 | 78.11 | 0.17 | 2.38 | 300 |
| 2024-09-20 22:21:35.871 | MS1 | 121.4656684425 | 31.1446282558 | 883 | 504990 | -85.58 | 14.63 | 61.92 | 0.09 | 2.75 | 445 |
| 2024-09-20 22:21:36.145 | MS1 | 121.4656742074 | 31.1446291461 | 883 | 504990 | -87.39 | 12.22 | 67.61 | 0.14 | 2.44 | 464 |
| 2024-09-20 22:21:37.372 | MS1 | 121.4656741409 | 31.1446290667 | 883 | 504990 | -93.92 | 8.44 | 89.69 | 0.10 | 2.12 | 430 |
| 2024-09-20 22:21:38.565 | MS1 | 121.4656642886 | 31.1446188152 | 883 | 504990 | -91.07 | 12.44 | 91.10 | 0.12 | 2.95 | 457 |
| 2024-09-20 22:21:39.265 | MS1 | 121.4656643645 | 31.1446242932 | 883 | 504990 | -93.90 | 12.28 | 55.11 | 0.16 | 2.37 | 321 |
| 2024-09-20 22:21:40.807 | MS1 | 121.4656733822 | 31.1446363489 | 883 | 504990 | -89.31 | 12.95 | 475.47 | 0.12 | 2.25 | 1585 |
| 2024-09-20 22:21:41.847 | MS1 | 121.4656651390 | 31.1446369369 | 883 | 504990 | -90.44 | 10.39 | 359.28 | 0.00 | 2.97 | 1589 |
| 2024-09-20 22:21:42.461 | MS1 | 121.4656741682 | 31.1446371459 | 883 | 504990 | -90.21 | 7.30 | 508.72 | 0.14 | 2.55 | 1598 |

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
| 3224978 | 2 | 121.4738522323 | 31.1485739579 | 210 | 3 | 5 | 32.9 | TDD | 490 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3235444 | 4 | 121.4686390845 | 31.1469114800 | 256 | 11 | 12 | 34.1 | TDD | 725 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3240809 | 1 | 121.4685373407 | 31.1535460185 | 40 | 12 | 12 | 39.6 | TDD | 801 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3274884 | 3 | 121.4737472971 | 31.1540087289 | 169 | 15 | 6 | 43.7 | TDD | 883 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.246 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.268 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.401 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.401 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.064 | NREventA3 | measId:2;ServCellPCI:208;Se... |
| 2024-09-20 22:21:38.304 | NRHandoverAttempt | SourcePCI:208;SourceNR-ARFC... |
| 2024-09-20 22:21:38.339 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.351 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.471 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.471 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240809 | 1 | 13.4945 | 12.0592 | -114.3214 | 12.5082 | 110.3902 | 0.0084 | 0.0170 |
| 2024_09_20 22:00 | 3224978 | 2 | 17.7100 | 13.6773 | -116.5651 | 5.8800 | 143.9750 | 0.0059 | 0.0171 |
| 2024_09_20 22:00 | 3274884 | 3 | 15.3943 | 11.0857 | -114.5618 | 14.6434 | 186.0149 | 0.0190 | 0.0193 |
| 2024_09_20 22:00 | 3235444 | 4 | 11.0056 | 10.1294 | -117.7583 | 9.9123 | 95.9274 | 0.0050 | 0.0029 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415780_75AF3FD3 | 504990 | 883 | -93.1 | 504990 | 490 | -97.2 | 504990 | 801 | -97.3 | 504990 | 725 |
| MR_1774415780_70739031 | 504990 | 883 | -93.4 | 504990 | 490 | -98.4 | 504990 | 801 | -98.5 | 504990 | 725 |
| MR_1774415780_D4E1AECD | 504990 | 883 | -92.0 | 504990 | 490 | -94.9 | 504990 | 801 | -99.6 | 504990 | 725 |
| MR_1774415780_73F28C81 | 504990 | 883 | -90.7 | 504990 | 490 | -96.7 | 504990 | 801 | -99.0 | 504990 | 725 |
| MR_1774415780_98E881C5 | 504990 | 883 | -90.1 | 504990 | 490 | -95.2 | 504990 | 801 | -98.7 | 504990 | 725 |
| MR_1774415780_CAC1303C | 504990 | 883 | -91.6 | 504990 | 490 | -95.6 | 504990 | 801 | -99.1 | 504990 | 725 |
| MR_1774415780_8331B487 | 504990 | 883 | -92.8 | 504990 | 490 | -98.4 | 504990 | 801 | -97.2 | 504990 | 725 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 519: `f4b53cc8-d13...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f4b53cc8-d138-4e0e-8520-ab155a3cb3c3` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[519] topology](images/train_0519.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3246175_3
- `C2`: Check test server and transmission issues
- `C3`: Decrease A3 Offset threshold for 3246175_3
- `C4`: Press down the tilt angle  of 3246175_3 by 9 degrees
- `C5`: Decrease transmission power for 3246175_3
- `C6`: Increase A3 Offset threshold for 3246175_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262056_1
- `C8`: Increase transmission power for 3262056_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262056_1
- `C10`: Decrease A3 Offset threshold for 3262056_1
- `C11`: Insufficient data; more data is needed for judgment. **← 정답**
- `C12`: Press down the tilt angle of 3262056_1 by 2 degrees
- `C13`: Add neighbor relationship between 3262056_1 and 3246175_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246175_3
- `C15`: Adjust the azimuth of 3246175_3 by 50 degrees
- `C16`: Increase A3 Offset threshold for 3262056_1
- `C17`: Lift the tilt angle  of 3246175_3 by 9 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246175_3
- `C19`: Add neighbor relationship between 3235505_2 and 3246175_3
- `C20`: Adjust the azimuth of 3262056_1 by 50 degrees
- `C21`: Lift the tilt angle of 3262056_1 by 2 degrees
- `C22`: Decrease transmission power for 3262056_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.313 | MS1 | 121.4656585490 | 31.1446261440 | 385 | 504990 | -87.20 | 15.43 | 309.30 | 0.10 | 2.64 | 1565 |
| 2024-09-20 22:21:32.215 | MS1 | 121.4656763493 | 31.1446279850 | 385 | 504990 | -91.20 | 15.89 | 575.73 | 0.15 | 2.61 | 1565 |
| 2024-09-20 22:21:33.560 | MS1 | 121.4656742814 | 31.1446301403 | 385 | 504990 | -91.11 | 17.07 | 315.41 | 0.15 | 2.55 | 1560 |
| 2024-09-20 22:21:34.685 | MS1 | 121.4656704771 | 31.1446300155 | 385 | 504990 | -86.84 | 15.86 | 49.53 | 0.09 | 2.65 | 1598 |
| 2024-09-20 22:21:35.328 | MS1 | 121.4656672461 | 31.1446356068 | 385 | 504990 | -88.90 | 12.10 | 96.15 | 0.11 | 2.60 | 1568 |
| 2024-09-20 22:21:36.286 | MS1 | 121.4656768643 | 31.1446186477 | 385 | 504990 | -88.40 | 15.49 | 96.18 | 0.02 | 2.87 | 1594 |
| 2024-09-20 22:21:37.921 | MS1 | 121.4656609350 | 31.1446289457 | 385 | 504990 | -93.14 | 12.69 | 86.73 | 0.09 | 2.25 | 1564 |
| 2024-09-20 22:21:38.747 | MS1 | 121.4656752052 | 31.1446282880 | 385 | 504990 | -90.47 | 12.33 | 62.02 | 0.06 | 2.74 | 1579 |
| 2024-09-20 22:21:39.793 | MS1 | 121.4656752428 | 31.1446310544 | 385 | 504990 | -93.89 | 8.64 | 94.49 | 0.14 | 2.63 | 1592 |
| 2024-09-20 22:21:40.369 | MS1 | 121.4656668084 | 31.1446358511 | 385 | 504990 | -90.02 | 12.26 | 373.38 | 0.06 | 2.38 | 1582 |
| 2024-09-20 22:21:41.854 | MS1 | 121.4656761158 | 31.1446242801 | 385 | 504990 | -91.84 | 9.56 | 468.25 | 0.02 | 2.86 | 1570 |
| 2024-09-20 22:21:42.614 | MS1 | 121.4656779928 | 31.1446301357 | 385 | 504990 | -93.53 | 12.35 | 326.01 | 0.20 | 2.71 | 1562 |

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
| 3217959 | 4 | 121.4691368044 | 31.1554887839 | 262 | 1 | 9 | 31.6 | TDD | 982 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3235505 | 2 | 121.4663049838 | 31.1557404439 | 204 | 12 | 10 | 15.1 | TDD | 363 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3246175 | 3 | 121.4731278610 | 31.1536374874 | 348 | 8 | 10 | 26.5 | TDD | 525 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3262056 | 1 | 121.4681121442 | 31.1545343744 | 16 | 1 | 5 | 20.4 | TDD | 385 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.623 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.644 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.793 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.793 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.451 | NREventA3 | measId:2;ServCellPCI:687;Se... |
| 2024-09-20 22:21:38.691 | NRHandoverAttempt | SourcePCI:687;SourceNR-ARFC... |
| 2024-09-20 22:21:38.729 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.741 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.869 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.869 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3262056 | 1 | 77.4691 | 90.2760 | -116.0064 | 10.2485 | 85.4010 | 0.0104 | 0.0082 |
| 2024_09_19 22:00 | 3235505 | 2 | 75.3201 | 79.6783 | -116.2747 | 5.5121 | 192.6187 | 0.0139 | 0.0132 |
| 2024_09_19 22:00 | 3246175 | 3 | 94.7231 | 78.9772 | -115.8218 | 12.2658 | 186.8020 | 0.0118 | 0.0134 |
| 2024_09_19 22:00 | 3217959 | 4 | 85.6505 | 79.5218 | -114.6004 | 18.4440 | 119.8206 | 0.0078 | 0.0132 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416739_BC3CEA65 | 504990 | 385 | -87.2 | 504990 | 525 | -93.9 | 504990 | 363 | -99.9 | 504990 | 982 |
| MR_1774416739_E253F763 | 504990 | 385 | -87.6 | 504990 | 525 | -96.8 | 504990 | 363 | -98.1 | 504990 | 982 |
| MR_1774416739_B54D7C2A | 504990 | 385 | -87.4 | 504990 | 525 | -94.0 | 504990 | 363 | -100.1 | 504990 | 982 |
| MR_1774416739_8B3E6E03 | 504990 | 385 | -87.2 | 504990 | 525 | -94.4 | 504990 | 363 | -99.5 | 504990 | 982 |
| MR_1774416739_D7604A32 | 504990 | 385 | -86.8 | 504990 | 525 | -95.5 | 504990 | 363 | -99.9 | 504990 | 982 |
| MR_1774416739_F8DF1323 | 504990 | 385 | -85.8 | 504990 | 525 | -93.5 | 504990 | 363 | -101.2 | 504990 | 982 |
| MR_1774416739_B45BA8E3 | 504990 | 385 | -85.6 | 504990 | 525 | -93.5 | 504990 | 363 | -100.1 | 504990 | 982 |

> *... 2개 열 생략 (전체 14열)*

---
