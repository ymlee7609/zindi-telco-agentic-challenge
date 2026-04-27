# Track A 문제 분석 — train[600]~train[609]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[600] ~ train[609] (10개)

## 목차

1. [문제 600: `0fc3eae2-805...`](#600) — single-answer, 정답: C5
2. [문제 601: `5dac7d2e-455...`](#601) — single-answer, 정답: C4
3. [문제 602: `7c702cde-5a6...`](#602) — multiple-answer, 정답: C1|C22
4. [문제 603: `1614c5bf-30b...`](#603) — single-answer, 정답: C22
5. [문제 604: `984285c9-091...`](#604) — single-answer, 정답: C2
6. [문제 605: `7bf89b4c-6ad...`](#605) — single-answer, 정답: C7
7. [문제 606: `13585e24-fb5...`](#606) — multiple-answer, 정답: C6|C15
8. [문제 607: `240425f6-c9d...`](#607) — multiple-answer, 정답: C14|C21
9. [문제 608: `96f982c1-60a...`](#608) — single-answer, 정답: C11
10. [문제 609: `a848ac40-913...`](#609) — single-answer, 정답: C2

---

### 문제 600: `0fc3eae2-805...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0fc3eae2-805e-42c4-bb04-329cf50b7cc5` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[600] topology](images/train_0600.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213128_3
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213128_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258174_2
- `C5`: Check test server and transmission issues **← 정답**
- `C6`: Adjust the azimuth of 3213128_3 by 50 degrees
- `C7`: Add neighbor relationship between 3220366_1 and 3213128_3
- `C8`: Adjust the azimuth of 3258174_2 by 50 degrees
- `C9`: Increase A3 Offset threshold for 3213128_3
- `C10`: Increase A3 Offset threshold for 3258174_2
- `C11`: Increase transmission power for 3213128_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258174_2
- `C13`: Decrease A3 Offset threshold for 3213128_3
- `C14`: Increase transmission power for 3258174_2
- `C15`: Decrease transmission power for 3258174_2
- `C16`: Press down the tilt angle  of 3213128_3 by 10 degrees
- `C17`: Lift the tilt angle of 3258174_2 by 3 degrees
- `C18`: Decrease A3 Offset threshold for 3258174_2
- `C19`: Press down the tilt angle of 3258174_2 by 3 degrees
- `C20`: Decrease transmission power for 3213128_3
- `C21`: Lift the tilt angle  of 3213128_3 by 10 degrees
- `C22`: Add neighbor relationship between 3258174_2 and 3213128_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.797 | MS1 | 121.4656702892 | 31.1446358348 | 130 | 504990 | -87.00 | 12.63 | 579.95 | 0.19 | 2.15 | 1561 |
| 2024-09-20 22:21:32.854 | MS1 | 121.4656623375 | 31.1446320134 | 130 | 504990 | -86.10 | 16.66 | 393.49 | 0.09 | 2.73 | 1594 |
| 2024-09-20 22:21:33.265 | MS1 | 121.4656699133 | 31.1446330732 | 130 | 504990 | -89.75 | 14.47 | 379.61 | 0.17 | 2.49 | 1566 |
| 2024-09-20 22:21:34.976 | MS1 | 121.4656759558 | 31.1446337150 | 130 | 504990 | -91.15 | 14.67 | 69.01 | 0.14 | 2.92 | 436 |
| 2024-09-20 22:21:35.456 | MS1 | 121.4656602320 | 31.1446361601 | 130 | 504990 | -85.23 | 17.41 | 92.48 | 0.02 | 2.81 | 425 |
| 2024-09-20 22:21:36.290 | MS1 | 121.4656727807 | 31.1446373015 | 130 | 504990 | -89.07 | 16.74 | 97.91 | 0.13 | 2.47 | 342 |
| 2024-09-20 22:21:37.661 | MS1 | 121.4656652145 | 31.1446317745 | 130 | 504990 | -90.03 | 7.73 | 73.84 | 0.17 | 2.81 | 385 |
| 2024-09-20 22:21:38.711 | MS1 | 121.4656592662 | 31.1446322143 | 130 | 504990 | -89.89 | 9.35 | 64.27 | 0.04 | 2.37 | 379 |
| 2024-09-20 22:21:39.423 | MS1 | 121.4656718927 | 31.1446351285 | 130 | 504990 | -91.74 | 12.82 | 77.83 | 0.06 | 2.33 | 437 |
| 2024-09-20 22:21:40.361 | MS1 | 121.4656703852 | 31.1446319955 | 130 | 504990 | -91.25 | 10.34 | 374.05 | 0.03 | 2.83 | 1594 |
| 2024-09-20 22:21:41.518 | MS1 | 121.4656669183 | 31.1446302220 | 130 | 504990 | -92.84 | 8.56 | 327.56 | 0.19 | 2.65 | 1576 |
| 2024-09-20 22:21:42.564 | MS1 | 121.4656634946 | 31.1446375996 | 130 | 504990 | -90.42 | 8.81 | 600.83 | 0.14 | 2.95 | 1562 |

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
| 3213128 | 3 | 121.4719820935 | 31.1521983345 | 3 | 13 | 1 | 23.7 | TDD | 558 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3220366 | 1 | 121.4673907387 | 31.1489743665 | 113 | 15 | 10 | 45.5 | TDD | 776 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3257774 | 4 | 121.4717162916 | 31.1490024750 | 159 | 1 | 9 | 45.5 | TDD | 526 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3258174 | 2 | 121.4737103466 | 31.1546857714 | 81 | 2 | 3 | 34.3 | TDD | 130 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.512 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.643 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.643 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.329 | NREventA3 | measId:2;ServCellPCI:839;Se... |
| 2024-09-20 22:21:38.569 | NRHandoverAttempt | SourcePCI:839;SourceNR-ARFC... |
| 2024-09-20 22:21:38.618 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.632 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.757 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.757 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220366 | 1 | 14.4923 | 19.3960 | -116.0402 | 17.5413 | 113.9940 | 0.0098 | 0.0121 |
| 2024_09_20 22:00 | 3258174 | 2 | 19.8631 | 16.9926 | -114.4351 | 7.9523 | 179.2247 | 0.0007 | 0.0146 |
| 2024_09_20 22:00 | 3213128 | 3 | 14.3530 | 18.0102 | -117.6722 | 11.3913 | 135.4069 | 0.0125 | 0.0106 |
| 2024_09_20 22:00 | 3257774 | 4 | 11.8293 | 10.1481 | -116.3377 | 15.7778 | 143.2785 | 0.0093 | 0.0066 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414675_5FE8142D | 504990 | 130 | -89.6 | 504990 | 558 | -98.8 | 504990 | 776 | -100.6 | 504990 | 526 |
| MR_1774414675_F56800C1 | 504990 | 130 | -92.0 | 504990 | 558 | -97.4 | 504990 | 776 | -101.3 | 504990 | 526 |
| MR_1774414675_9F779F55 | 504990 | 130 | -90.3 | 504990 | 558 | -96.9 | 504990 | 776 | -101.6 | 504990 | 526 |
| MR_1774414675_3A9EC03B | 504990 | 130 | -92.4 | 504990 | 558 | -96.7 | 504990 | 776 | -99.0 | 504990 | 526 |
| MR_1774414675_D9210944 | 504990 | 130 | -90.9 | 504990 | 558 | -96.2 | 504990 | 776 | -101.8 | 504990 | 526 |
| MR_1774414675_30267DEB | 504990 | 130 | -89.8 | 504990 | 558 | -99.0 | 504990 | 776 | -102.1 | 504990 | 526 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 601: `5dac7d2e-455...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5dac7d2e-455b-4721-9884-e58fb393ddac` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Add neighbor relationship between 3248135_4 and 3269301_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[601] topology](images/train_0601.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269301_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248135_4
- `C3`: Press down the tilt angle  of 3269301_2 by 2 degrees
- `C4`: Add neighbor relationship between 3248135_4 and 3269301_2 **← 정답**
- `C5`: Check test server and transmission issues
- `C6`: Adjust the azimuth of 3248135_4 by 50 degrees
- `C7`: Press down the tilt angle of 3248135_4 by 10 degrees
- `C8`: Decrease transmission power for 3269301_2
- `C9`: Lift the tilt angle  of 3269301_2 by 2 degrees
- `C10`: Decrease A3 Offset threshold for 3269301_2
- `C11`: Add neighbor relationship between 3232335_3 and 3269301_2
- `C12`: Increase transmission power for 3269301_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269301_2
- `C14`: Increase A3 Offset threshold for 3269301_2
- `C15`: Increase A3 Offset threshold for 3248135_4
- `C16`: Decrease transmission power for 3248135_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248135_4
- `C18`: Increase transmission power for 3248135_4
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Adjust the azimuth of 3269301_2 by 45 degrees
- `C21`: Lift the tilt angle of 3248135_4 by 10 degrees
- `C22`: Decrease A3 Offset threshold for 3248135_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.121 | MS1 | 121.4656599724 | 31.1446334990 | 822 | 504990 | -78.32 | 17.85 | 569.64 | 0.13 | 2.04 | 1563 |
| 2024-09-20 22:21:32.205 | MS1 | 121.4656635778 | 31.1446264283 | 822 | 504990 | -78.13 | 17.77 | 507.12 | 0.05 | 2.08 | 1567 |
| 2024-09-20 22:21:33.483 | MS1 | 121.4656629474 | 31.1446182362 | 822 | 504990 | -82.56 | 12.81 | 476.14 | 0.06 | 2.28 | 1572 |
| 2024-09-20 22:21:34.215 | MS1 | 121.4656732292 | 31.1446309255 | 822 | 504990 | -94.97 | -0.50 | 69.79 | 0.18 | 1.42 | 1563 |
| 2024-09-20 22:21:35.438 | MS1 | 121.4656637248 | 31.1446275893 | 822 | 504990 | -93.30 | -0.42 | 73.94 | 0.04 | 1.15 | 1565 |
| 2024-09-20 22:21:36.732 | MS1 | 121.4656706031 | 31.1446327787 | 822 | 504990 | -87.51 | -1.93 | 46.37 | 0.12 | 1.02 | 1564 |
| 2024-09-20 22:21:37.527 | MS1 | 121.4656629647 | 31.1446298074 | 822 | 504990 | -94.68 | -1.23 | 38.77 | 0.17 | 1.13 | 1592 |
| 2024-09-20 22:21:38.938 | MS1 | 121.4656760581 | 31.1446262762 | 822 | 504990 | -77.53 | 17.33 | 392.86 | 0.19 | 1.13 | 1585 |
| 2024-09-20 22:21:39.291 | MS1 | 121.4656661694 | 31.1446345575 | 822 | 504990 | -77.68 | 16.73 | 535.59 | 0.07 | 1.44 | 1586 |
| 2024-09-20 22:21:40.514 | MS1 | 121.4656742882 | 31.1446288939 | 822 | 504990 | -80.25 | 13.89 | 390.76 | 0.12 | 2.36 | 1573 |
| 2024-09-20 22:21:41.314 | MS1 | 121.4656631834 | 31.1446312493 | 822 | 504990 | -80.79 | 17.26 | 455.56 | 0.19 | 2.25 | 1596 |
| 2024-09-20 22:21:42.778 | MS1 | 121.4656669730 | 31.1446224194 | 822 | 504990 | -84.47 | 13.22 | 398.61 | 0.08 | 2.89 | 1581 |

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
| 3232335 | 3 | 121.4671402620 | 31.1548032709 | 195 | 9 | 10 | 40.5 | TDD | 669 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3241274 | 1 | 121.4686960271 | 31.1464815331 | 287 | 2 | 5 | 21.7 | TDD | 241 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3248135 | 4 | 121.4667158125 | 31.1459220118 | 114 | 7 | 4 | 38.3 | TDD | 822 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3269301 | 2 | 121.4713471586 | 31.1548625420 | 250 | 0 | 5 | 46.2 | TDD | 515 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.409 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.425 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.561 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.561 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.217 | NREventA3 | measId:2;ServCellPCI:888;Se... |
| 2024-09-20 22:21:36.217 | NREventA3 | measId:2;ServCellPCI:888;Se... |
| 2024-09-20 22:21:37.217 | NREventA3 | measId:2;ServCellPCI:888;Se... |
| 2024-09-20 22:21:39.717 | NRRRCReestablishAttempt | PCI:888 |
| 2024-09-20 22:21:39.727 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.741 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.865 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.865 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241274 | 1 | 13.4587 | 10.9023 | -116.9078 | 17.1996 | 189.0097 | 0.0019 | 0.0112 |
| 2024_09_20 22:00 | 3269301 | 2 | 10.7591 | 12.4953 | -116.3880 | 9.5414 | 114.9819 | 0.0163 | 0.0104 |
| 2024_09_20 22:00 | 3232335 | 3 | 10.3732 | 10.7868 | -114.5136 | 13.0186 | 178.8769 | 0.0110 | 0.0042 |
| 2024_09_20 22:00 | 3248135 | 4 | 14.7440 | 6.6255 | -116.0558 | 8.1170 | 146.3839 | 0.0187 | 0.1726 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411984_0841E2B9 | 504990 | 822 | -94.6 | 504990 | 515 | -88.3 | 504990 | 669 | -98.1 | 504990 | 241 |
| MR_1774411984_3217DEC1 | 504990 | 515 | -89.2 | 504990 | 822 | -96.6 | 504990 | 669 | -97.1 | 504990 | 241 |
| MR_1774411984_D3912B5F | 504990 | 822 | -94.5 | 504990 | 515 | -91.0 | 504990 | 669 | -98.5 | 504990 | 241 |
| MR_1774411984_A75B9395 | 504990 | 515 | -87.9 | 504990 | 822 | -96.4 | 504990 | 669 | -99.5 | 504990 | 241 |
| MR_1774411984_BB228E5D | 504990 | 822 | -94.3 | 504990 | 515 | -88.8 | 504990 | 669 | -97.7 | 504990 | 241 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 602: `7c702cde-5a6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7c702cde-5a63-4bf4-898a-f37f6c82ecb9` |
| Tag | **multiple-answer** |
| 정답 | **C1|C22** |
| C1 의미 | Increase transmission power for 3257361_1 |
| C22 의미 | Adjust the azimuth of 3257361_1 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[602] topology](images/train_0602.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3257361_1 **← 정답**
- `C2`: Increase transmission power for 3238730_4
- `C3`: Press down the tilt angle of 3257361_1 by 9 degrees
- `C4`: Adjust the azimuth of 3238730_4 by 24 degrees
- `C5`: Increase A3 Offset threshold for 3257361_1
- `C6`: Decrease transmission power for 3257361_1
- `C7`: Decrease transmission power for 3238730_4
- `C8`: Lift the tilt angle of 3257361_1 by 9 degrees
- `C9`: Decrease A3 Offset threshold for 3257361_1
- `C10`: Lift the tilt angle  of 3238730_4 by 4 degrees
- `C11`: Add neighbor relationship between 3257361_1 and 3238730_4
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Press down the tilt angle  of 3238730_4 by 4 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257361_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257361_1
- `C16`: Increase A3 Offset threshold for 3238730_4
- `C17`: Decrease A3 Offset threshold for 3238730_4
- `C18`: Add neighbor relationship between 3214932_2 and 3238730_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238730_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238730_4
- `C21`: Check test server and transmission issues
- `C22`: Adjust the azimuth of 3257361_1 by 50 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.209 | MS1 | 121.4656779564 | 31.1446183210 | 598 | 504990 | -86.95 | 15.01 | 422.73 | 0.18 | 2.81 | 1578 |
| 2024-09-20 22:21:32.705 | MS1 | 121.4656774069 | 31.1446221293 | 598 | 504990 | -86.66 | 16.84 | 332.54 | 0.02 | 2.16 | 1593 |
| 2024-09-20 22:21:33.158 | MS1 | 121.4656602194 | 31.1446240773 | 598 | 504990 | -87.93 | 14.54 | 313.45 | 0.08 | 2.90 | 1566 |
| 2024-09-20 22:21:34.183 | MS1 | 121.4656669703 | 31.1446368313 | 598 | 504990 | -101.15 | -1.92 | 68.69 | 0.10 | 1.24 | 1574 |
| 2024-09-20 22:21:35.629 | MS1 | 121.4656718953 | 31.1446221169 | 598 | 504990 | -109.27 | 1.43 | 52.82 | 0.12 | 1.33 | 1600 |
| 2024-09-20 22:21:36.667 | MS1 | 121.4656629818 | 31.1446272002 | 598 | 504990 | -102.41 | 0.67 | 28.99 | 0.01 | 1.34 | 1581 |
| 2024-09-20 22:21:37.811 | MS1 | 121.4656732905 | 31.1446223325 | 598 | 504990 | -103.27 | -0.10 | 18.77 | 0.19 | 1.39 | 1569 |
| 2024-09-20 22:21:38.207 | MS1 | 121.4656706826 | 31.1446367859 | 598 | 504990 | -107.09 | -0.81 | 29.78 | 0.01 | 1.03 | 1577 |
| 2024-09-20 22:21:39.437 | MS1 | 121.4656704321 | 31.1446355270 | 598 | 504990 | -105.20 | -0.64 | 21.20 | 0.16 | 1.50 | 1588 |
| 2024-09-20 22:21:40.133 | MS1 | 121.4656581991 | 31.1446292892 | 598 | 504990 | -92.55 | 15.34 | 372.52 | 0.15 | 2.95 | 1584 |
| 2024-09-20 22:21:41.687 | MS1 | 121.4656613758 | 31.1446283168 | 598 | 504990 | -88.39 | 17.42 | 462.49 | 0.02 | 2.22 | 1582 |
| 2024-09-20 22:21:42.511 | MS1 | 121.4656761232 | 31.1446346195 | 598 | 504990 | -94.90 | 14.02 | 490.52 | 0.11 | 2.48 | 1568 |

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
| 3214932 | 2 | 121.4652531347 | 31.1466659214 | 84 | 8 | 2 | 23.6 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3226677 | 3 | 121.4640611005 | 31.1543997618 | 284 | 12 | 5 | 38.4 | TDD | 506 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3238730 | 4 | 121.4661447032 | 31.1500146422 | 160 | 1 | 2 | 33.1 | TDD | 982 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3257361 | 1 | 121.4709870881 | 31.1535954427 | 281 | 8 | 4 | 21.1 | TDD | 598 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.190 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.190 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.435 | NREventA2 | measId:1;ServCellPCI:822;Se... |
| 2024-09-20 22:21:34.545 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257361 | 1 | 16.1261 | 7.3823 | -114.3862 | 10.7858 | 114.7612 | 0.1372 | 0.0185 |
| 2024_09_20 22:00 | 3214932 | 2 | 15.0549 | 18.3675 | -114.3817 | 16.4446 | 93.6229 | 0.0118 | 0.0013 |
| 2024_09_20 22:00 | 3226677 | 3 | 6.9916 | 7.1744 | -115.2510 | 15.4906 | 162.7303 | 0.0077 | 0.0080 |
| 2024_09_20 22:00 | 3238730 | 4 | 17.3376 | 19.9574 | -115.1139 | 5.9387 | 124.4471 | 0.0128 | 0.0146 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412449_EA93D991 | 504990 | 598 | -102.4 | 504990 | 982 | -104.7 | 504990 | 258 | -111.8 | 504990 | 506 |
| MR_1774412449_B531E0DA | 504990 | 598 | -101.9 | 504990 | 982 | -104.2 | 504990 | 258 | -111.9 | 504990 | 506 |
| MR_1774412449_D32E0387 | 504990 | 598 | -100.8 | 504990 | 982 | -103.1 | 504990 | 258 | -113.3 | 504990 | 506 |
| MR_1774412449_AB3BE223 | 504990 | 598 | -102.8 | 504990 | 982 | -105.7 | 504990 | 258 | -113.5 | 504990 | 506 |
| MR_1774412449_9C9C359E | 504990 | 598 | -101.2 | 504990 | 982 | -104.8 | 504990 | 258 | -113.4 | 504990 | 506 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 603: `1614c5bf-30b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1614c5bf-30be-430c-ba7b-31f3c86d507c` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[603] topology](images/train_0603.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263470_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263470_1
- `C3`: Increase transmission power for 3263470_1
- `C4`: Increase A3 Offset threshold for 3239953_4
- `C5`: Decrease A3 Offset threshold for 3263470_1
- `C6`: Add neighbor relationship between 3222432_2 and 3239953_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239953_4
- `C8`: Decrease transmission power for 3239953_4
- `C9`: Decrease transmission power for 3263470_1
- `C10`: Increase A3 Offset threshold for 3263470_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239953_4
- `C12`: Adjust the azimuth of 3263470_1 by 50 degrees
- `C13`: Check test server and transmission issues
- `C14`: Increase transmission power for 3239953_4
- `C15`: Add neighbor relationship between 3263470_1 and 3239953_4
- `C16`: Adjust the azimuth of 3239953_4 by 21 degrees
- `C17`: Press down the tilt angle  of 3239953_4 by 7 degrees
- `C18`: Press down the tilt angle of 3263470_1 by 10 degrees
- `C19`: Lift the tilt angle  of 3239953_4 by 7 degrees
- `C20`: Decrease A3 Offset threshold for 3239953_4
- `C21`: Lift the tilt angle of 3263470_1 by 10 degrees
- `C22`: Insufficient data; more data is needed for judgment. **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.113 | MS1 | 121.4656600670 | 31.1446335119 | 341 | 504990 | -88.66 | 17.30 | 381.70 | 0.15 | 2.60 | 1564 |
| 2024-09-20 22:21:32.608 | MS1 | 121.4656694133 | 31.1446367441 | 341 | 504990 | -88.77 | 13.15 | 457.99 | 0.08 | 2.28 | 1573 |
| 2024-09-20 22:21:33.351 | MS1 | 121.4656657101 | 31.1446336150 | 341 | 504990 | -90.62 | 15.82 | 569.04 | 0.15 | 2.44 | 1599 |
| 2024-09-20 22:21:34.977 | MS1 | 121.4656764923 | 31.1446281845 | 341 | 504990 | -88.87 | 15.40 | 94.24 | 0.16 | 2.45 | 1599 |
| 2024-09-20 22:21:35.753 | MS1 | 121.4656656884 | 31.1446239213 | 341 | 504990 | -89.39 | 16.62 | 64.83 | 0.06 | 2.03 | 1600 |
| 2024-09-20 22:21:36.879 | MS1 | 121.4656700607 | 31.1446314167 | 341 | 504990 | -88.82 | 16.79 | 86.80 | 0.14 | 2.62 | 1598 |
| 2024-09-20 22:21:37.551 | MS1 | 121.4656679992 | 31.1446317775 | 341 | 504990 | -89.55 | 11.53 | 102.49 | 0.06 | 2.34 | 1596 |
| 2024-09-20 22:21:38.978 | MS1 | 121.4656644641 | 31.1446218759 | 341 | 504990 | -93.37 | 10.24 | 66.39 | 0.01 | 2.39 | 1566 |
| 2024-09-20 22:21:39.469 | MS1 | 121.4656725854 | 31.1446251519 | 341 | 504990 | -92.99 | 9.10 | 100.55 | 0.15 | 2.93 | 1600 |
| 2024-09-20 22:21:40.308 | MS1 | 121.4656739550 | 31.1446271704 | 341 | 504990 | -89.56 | 10.96 | 453.57 | 0.17 | 2.72 | 1565 |
| 2024-09-20 22:21:41.817 | MS1 | 121.4656645413 | 31.1446305539 | 341 | 504990 | -91.22 | 10.60 | 499.97 | 0.19 | 2.21 | 1569 |
| 2024-09-20 22:21:42.639 | MS1 | 121.4656748291 | 31.1446286179 | 341 | 504990 | -92.52 | 11.21 | 468.68 | 0.19 | 2.47 | 1562 |

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
| 3222432 | 2 | 121.4647907550 | 31.1472670851 | 359 | 4 | 7 | 23.0 | TDD | 468 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3234144 | 3 | 121.4663764215 | 31.1479432457 | 353 | 8 | 6 | 36.8 | TDD | 388 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3239953 | 4 | 121.4667290295 | 31.1499108101 | 211 | 5 | 7 | 23.9 | TDD | 796 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3263470 | 1 | 121.4752215395 | 31.1465205658 | 91 | 11 | 9 | 38.7 | TDD | 341 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.209 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.350 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.350 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.068 | NREventA3 | measId:2;ServCellPCI:827;Se... |
| 2024-09-20 22:21:38.308 | NRHandoverAttempt | SourcePCI:827;SourceNR-ARFC... |
| 2024-09-20 22:21:38.347 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.359 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.506 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.506 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3263470 | 1 | 87.8242 | 81.0352 | -117.7168 | 13.7874 | 125.2975 | 0.0110 | 0.0137 |
| 2024_09_19 22:00 | 3222432 | 2 | 85.2091 | 84.2524 | -117.7998 | 9.5827 | 131.5943 | 0.0150 | 0.0119 |
| 2024_09_19 22:00 | 3234144 | 3 | 88.3487 | 94.0257 | -116.1281 | 6.1835 | 184.7358 | 0.0155 | 0.0190 |
| 2024_09_19 22:00 | 3239953 | 4 | 76.7796 | 85.4120 | -117.0939 | 11.6977 | 163.7810 | 0.0066 | 0.0032 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414233_61135421 | 504990 | 341 | -87.7 | 504990 | 796 | -93.9 | 504990 | 468 | -98.0 | 504990 | 388 |
| MR_1774414233_163EC049 | 504990 | 341 | -90.6 | 504990 | 796 | -97.1 | 504990 | 468 | -97.8 | 504990 | 388 |
| MR_1774414233_60B2FCD4 | 504990 | 341 | -90.1 | 504990 | 796 | -95.0 | 504990 | 468 | -95.7 | 504990 | 388 |
| MR_1774414233_430E61D6 | 504990 | 341 | -87.8 | 504990 | 796 | -94.8 | 504990 | 468 | -95.0 | 504990 | 388 |
| MR_1774414233_9244D123 | 504990 | 341 | -87.0 | 504990 | 796 | -94.4 | 504990 | 468 | -94.8 | 504990 | 388 |
| MR_1774414233_9096431D | 504990 | 341 | -89.0 | 504990 | 796 | -95.4 | 504990 | 468 | -94.5 | 504990 | 388 |
| MR_1774414233_BA51F7E9 | 504990 | 341 | -89.7 | 504990 | 796 | -97.1 | 504990 | 468 | -95.5 | 504990 | 388 |
| MR_1774414233_014874B8 | 504990 | 341 | -88.7 | 504990 | 796 | -97.5 | 504990 | 468 | -97.0 | 504990 | 388 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 604: `984285c9-091...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `984285c9-0916-409a-9b00-a33951583d3d` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[604] topology](images/train_0604.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3219910_1
- `C2`: Insufficient data; more data is needed for judgment. **← 정답**
- `C3`: Lift the tilt angle  of 3247198_3 by 10 degrees
- `C4`: Decrease A3 Offset threshold for 3219910_1
- `C5`: Increase transmission power for 3247198_3
- `C6`: Add neighbor relationship between 3245649_2 and 3247198_3
- `C7`: Add neighbor relationship between 3219910_1 and 3247198_3
- `C8`: Adjust the azimuth of 3247198_3 by 20 degrees
- `C9`: Adjust the azimuth of 3219910_1 by 50 degrees
- `C10`: Decrease transmission power for 3219910_1
- `C11`: Increase A3 Offset threshold for 3219910_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247198_3
- `C13`: Lift the tilt angle of 3219910_1 by 2 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219910_1
- `C15`: Check test server and transmission issues
- `C16`: Decrease A3 Offset threshold for 3247198_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219910_1
- `C18`: Decrease transmission power for 3247198_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247198_3
- `C20`: Press down the tilt angle of 3219910_1 by 2 degrees
- `C21`: Press down the tilt angle  of 3247198_3 by 10 degrees
- `C22`: Increase A3 Offset threshold for 3247198_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.998 | MS1 | 121.4656768052 | 31.1446305497 | 94 | 504990 | -86.48 | 17.57 | 586.75 | 0.17 | 2.50 | 1574 |
| 2024-09-20 22:21:32.292 | MS1 | 121.4656602367 | 31.1446207548 | 94 | 504990 | -85.34 | 16.54 | 587.60 | 0.04 | 2.60 | 1561 |
| 2024-09-20 22:21:33.135 | MS1 | 121.4656697897 | 31.1446361071 | 94 | 504990 | -91.34 | 17.79 | 501.25 | 0.04 | 2.92 | 1573 |
| 2024-09-20 22:21:34.797 | MS1 | 121.4656662447 | 31.1446296001 | 94 | 504990 | -90.45 | 16.31 | 75.69 | 0.15 | 2.06 | 1573 |
| 2024-09-20 22:21:35.471 | MS1 | 121.4656591643 | 31.1446246631 | 94 | 504990 | -91.49 | 12.93 | 50.78 | 0.06 | 2.28 | 1565 |
| 2024-09-20 22:21:36.112 | MS1 | 121.4656703907 | 31.1446251880 | 94 | 504990 | -89.89 | 17.69 | 78.32 | 0.03 | 2.87 | 1568 |
| 2024-09-20 22:21:37.655 | MS1 | 121.4656591969 | 31.1446301655 | 94 | 504990 | -93.26 | 11.69 | 72.62 | 0.01 | 2.59 | 1596 |
| 2024-09-20 22:21:38.131 | MS1 | 121.4656678334 | 31.1446223590 | 94 | 504990 | -90.59 | 9.64 | 59.79 | 0.11 | 2.62 | 1564 |
| 2024-09-20 22:21:39.254 | MS1 | 121.4656652380 | 31.1446209832 | 94 | 504990 | -90.55 | 7.61 | 76.74 | 0.17 | 2.37 | 1591 |
| 2024-09-20 22:21:40.606 | MS1 | 121.4656598264 | 31.1446193093 | 94 | 504990 | -90.21 | 10.29 | 577.31 | 0.19 | 3.00 | 1591 |
| 2024-09-20 22:21:41.396 | MS1 | 121.4656724220 | 31.1446293293 | 94 | 504990 | -92.24 | 7.28 | 387.31 | 0.16 | 2.13 | 1589 |
| 2024-09-20 22:21:42.640 | MS1 | 121.4656664184 | 31.1446317448 | 94 | 504990 | -93.71 | 8.01 | 517.43 | 0.19 | 2.62 | 1598 |

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
| 3219910 | 1 | 121.4754312252 | 31.1482813665 | 62 | 0 | 12 | 34.8 | TDD | 94 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3245649 | 2 | 121.4749724936 | 31.1483058272 | 245 | 6 | 1 | 38.9 | TDD | 581 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3247198 | 3 | 121.4742360093 | 31.1516614740 | 246 | 11 | 11 | 38.4 | TDD | 702 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3252554 | 4 | 121.4645599061 | 31.1548664103 | 295 | 2 | 12 | 18.2 | TDD | 230 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.273 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.295 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.429 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.429 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.151 | NREventA3 | measId:2;ServCellPCI:549;Se... |
| 2024-09-20 22:21:38.391 | NRHandoverAttempt | SourcePCI:549;SourceNR-ARFC... |
| 2024-09-20 22:21:38.439 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.450 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.569 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.569 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3219910 | 1 | 81.4166 | 75.8389 | -117.9848 | 5.8745 | 122.6985 | 0.0200 | 0.0117 |
| 2024_09_19 22:00 | 3245649 | 2 | 93.8802 | 76.1913 | -117.6475 | 17.1593 | 166.1913 | 0.0154 | 0.0139 |
| 2024_09_19 22:00 | 3247198 | 3 | 80.1064 | 77.5385 | -114.1144 | 11.4271 | 104.8678 | 0.0158 | 0.0079 |
| 2024_09_19 22:00 | 3252554 | 4 | 80.1030 | 85.0360 | -116.3278 | 8.0235 | 131.5014 | 0.0065 | 0.0041 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412581_985CF028 | 504990 | 94 | -91.7 | 504990 | 702 | -98.3 | 504990 | 581 | -104.4 | 504990 | 230 |
| MR_1774412581_64C920A0 | 504990 | 94 | -91.8 | 504990 | 702 | -98.6 | 504990 | 581 | -105.0 | 504990 | 230 |
| MR_1774412581_67DDAB21 | 504990 | 94 | -92.1 | 504990 | 702 | -98.8 | 504990 | 581 | -104.4 | 504990 | 230 |
| MR_1774412581_1EF7ADF8 | 504990 | 94 | -90.9 | 504990 | 702 | -99.8 | 504990 | 581 | -104.9 | 504990 | 230 |
| MR_1774412581_616ADB18 | 504990 | 94 | -92.3 | 504990 | 702 | -96.8 | 504990 | 581 | -103.4 | 504990 | 230 |
| MR_1774412581_26B25419 | 504990 | 94 | -92.4 | 504990 | 702 | -97.4 | 504990 | 581 | -106.5 | 504990 | 230 |
| MR_1774412581_F39ECA96 | 504990 | 94 | -92.1 | 504990 | 702 | -96.8 | 504990 | 581 | -104.5 | 504990 | 230 |
| MR_1774412581_A57FF89A | 504990 | 94 | -90.4 | 504990 | 702 | -99.9 | 504990 | 581 | -103.2 | 504990 | 230 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 605: `7bf89b4c-6ad...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7bf89b4c-6ad8-46ba-a67a-8680d62b57c2` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217403_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[605] topology](images/train_0605.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3253675_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217403_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253675_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253675_2
- `C5`: Press down the tilt angle of 3217403_1 by 2 degrees
- `C6`: Press down the tilt angle  of 3253675_2 by 2 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217403_1 **← 정답**
- `C8`: Lift the tilt angle  of 3253675_2 by 2 degrees
- `C9`: Increase A3 Offset threshold for 3217403_1
- `C10`: Adjust the azimuth of 3217403_1 by 34 degrees
- `C11`: Decrease A3 Offset threshold for 3253675_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Add neighbor relationship between 3247304_8 and 3253675_2
- `C14`: Add neighbor relationship between 3217403_1 and 3253675_2
- `C15`: Increase transmission power for 3253675_2
- `C16`: Decrease A3 Offset threshold for 3217403_1
- `C17`: Increase transmission power for 3217403_1
- `C18`: Lift the tilt angle of 3217403_1 by 2 degrees
- `C19`: Decrease transmission power for 3253675_2
- `C20`: Decrease transmission power for 3217403_1
- `C21`: Check test server and transmission issues
- `C22`: Adjust the azimuth of 3253675_2 by 37 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.681 | MS1 | 121.4656656900 | 31.1446201724 | 100 | 504990 | -93.57 | 10.76 | 324.43 | 0.05 | 2.58 | 1562 |
| 2024-09-20 22:21:32.879 | MS1 | 121.4656776280 | 31.1446292697 | 818 | 504990 | -93.20 | 11.31 | 474.12 | 0.15 | 2.95 | 1567 |
| 2024-09-20 22:21:33.344 | MS1 | 121.4656760190 | 31.1446337843 | 763 | 504990 | -95.68 | 9.77 | 413.83 | 0.09 | 2.51 | 1583 |
| 2024-09-20 22:21:34.370 | MS1 | 121.4656735498 | 31.1446300942 | 201 | 152650 | -88.27 | 3.54 | 97.65 | 0.05 | 1.61 | 906 |
| 2024-09-20 22:21:35.541 | MS1 | 121.4656693184 | 31.1446372191 | 514 | 152650 | -88.38 | 7.30 | 69.65 | 0.13 | 1.51 | 903 |
| 2024-09-20 22:21:36.695 | MS1 | 121.4656639339 | 31.1446201537 | 903 | 152650 | -89.08 | 2.80 | 65.33 | 0.13 | 1.73 | 926 |
| 2024-09-20 22:21:37.652 | MS1 | 121.4656634301 | 31.1446300500 | 468 | 152650 | -91.22 | 6.46 | 83.31 | 0.16 | 1.78 | 971 |
| 2024-09-20 22:21:38.941 | MS1 | 121.4656583059 | 31.1446356399 | 201 | 152650 | -90.42 | 3.23 | 59.28 | 0.06 | 1.95 | 969 |
| 2024-09-20 22:21:39.873 | MS1 | 121.4656635569 | 31.1446182908 | 514 | 152650 | -87.60 | 7.51 | 83.22 | 0.15 | 1.51 | 956 |
| 2024-09-20 22:21:40.192 | MS1 | 121.4656719111 | 31.1446353237 | 903 | 152650 | -91.85 | 5.78 | 80.05 | 0.07 | 2.65 | 1583 |
| 2024-09-20 22:21:41.845 | MS1 | 121.4656663345 | 31.1446235900 | 468 | 152650 | -87.23 | 7.01 | 87.49 | 0.02 | 2.64 | 1573 |
| 2024-09-20 22:21:42.827 | MS1 | 121.4656583442 | 31.1446192853 | 201 | 152650 | -88.79 | 4.83 | 95.97 | 0.09 | 2.13 | 1562 |

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
| 3213601 | 7 | 121.4688805762 | 31.1440978974 | 102 | 12 | 1 | 1.4 | FDD | 514 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3215181 | 11 | 121.4742428218 | 31.1487670824 | 302 | 14 | 9 | 10.2 | FDD | 440 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3217403 | 1 | 121.4677848842 | 31.1483574346 | 240 | 1 | 2 | 4.1 | TDD | 100 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3226368 | 5 | 121.4645010010 | 31.1557516201 | 16 | 6 | 4 | 20.5 | TDD | 818 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3233061 | 4 | 121.4689497057 | 31.1517314762 | 296 | 12 | 12 | 17.5 | TDD | 843 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3240637 | 9 | 121.4734208930 | 31.1553784010 | 346 | 3 | 4 | 7.4 | FDD | 201 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3242439 | 3 | 121.4725162957 | 31.1483196676 | 189 | 14 | 6 | 7.3 | TDD | 9 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3247304 | 8 | 121.4755631692 | 31.1446257840 | 161 | 15 | 0 | 12.8 | FDD | 903 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3250234 | 10 | 121.4718275590 | 31.1479071732 | 152 | 2 | 1 | 0.4 | FDD | 468 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3253572 | 12 | 121.4661063283 | 31.1532151740 | 2 | 9 | 10 | 18.3 | FDD | 348 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3253675 | 2 | 121.4663593648 | 31.1463435883 | 162 | 2 | 1 | 0.9 | TDD | 841 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3258305 | 13 | 121.4725568373 | 31.1499177663 | 327 | 13 | 5 | 5.9 | FDD | 509 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3270952 | 6 | 121.4689218502 | 31.1559910181 | 283 | 2 | 6 | 18.6 | TDD | 763 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.119 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.135 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.239 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.239 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.967 | NREventA2 | measId:1;ServCellPCI:995;Se... |
| 2024-09-20 22:21:35.075 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.372 | NREventA5 | measId:3;ServCellPCI:995;Se... |
| 2024-09-20 22:21:35.438 | NRHandoverAttempt | SourcePCI:995;SourceNR-ARFC... |
| 2024-09-20 22:21:35.482 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.497 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.622 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.622 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217403 | 1 | 19.3977 | 14.5371 | -114.1201 | 17.4510 | 162.2258 | 0.0185 | 0.0150 |
| 2024_09_20 22:00 | 3253675 | 2 | 12.1113 | 14.6516 | -115.1870 | 14.4182 | 124.0574 | 0.0098 | 0.0060 |
| 2024_09_20 22:00 | 3242439 | 3 | 18.0859 | 6.1111 | -116.3087 | 8.3583 | 128.2630 | 0.0065 | 0.0180 |
| 2024_09_20 22:00 | 3233061 | 4 | 14.7311 | 17.1953 | -114.5004 | 16.1725 | 160.8434 | 0.0059 | 0.0017 |
| 2024_09_20 22:00 | 3226368 | 5 | 7.1614 | 11.2364 | -117.3031 | 16.7454 | 129.8174 | 0.0001 | 0.0082 |
| 2024_09_20 22:00 | 3270952 | 6 | 5.8191 | 14.8603 | -115.6445 | 12.3042 | 98.2418 | 0.0059 | 0.0064 |
| 2024_09_20 22:00 | 3213601 | 7 | 9.7771 | 8.9718 | -117.1982 | 3.1493 | 20.2944 | 0.0151 | 0.0001 |
| 2024_09_20 22:00 | 3247304 | 8 | 19.6941 | 7.0716 | -114.0076 | 4.7025 | 26.9941 | 0.0175 | 0.0182 |
| 2024_09_20 22:00 | 3240637 | 9 | 19.1465 | 9.4580 | -116.6232 | 3.1419 | 38.8706 | 0.0014 | 0.0057 |
| 2024_09_20 22:00 | 3250234 | 10 | 9.9394 | 12.1828 | -114.1396 | 4.5850 | 22.1379 | 0.0177 | 0.0026 |
| 2024_09_20 22:00 | 3215181 | 11 | 12.4376 | 15.9256 | -117.0230 | 4.1207 | 30.0318 | 0.0176 | 0.0072 |
| 2024_09_20 22:00 | 3253572 | 12 | 7.9483 | 16.1117 | -114.9527 | 3.3176 | 48.1365 | 0.0070 | 0.0058 |
| 2024_09_20 22:00 | 3258305 | 13 | 12.6767 | 11.5359 | -115.7502 | 4.1594 | 44.5431 | 0.0046 | 0.0039 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413883_8CD62CF7 | 152650 | 201 | -86.7 | 152650 | 440 | -93.1 | 152650 | 509 | -97.5 | 152650 | 348 |
| MR_1774413883_7725CC62 | 152650 | 201 | -87.6 | 152650 | 440 | -90.9 | 152650 | 509 | -95.0 | 152650 | 348 |
| MR_1774413883_D68A5779 | 152650 | 201 | -86.3 | 152650 | 440 | -93.2 | 152650 | 509 | -94.0 | 152650 | 348 |
| MR_1774413883_7DAEB6A3 | 152650 | 201 | -86.5 | 152650 | 440 | -93.1 | 152650 | 509 | -95.4 | 152650 | 348 |
| MR_1774413883_DBD40B5C | 504990 | 763 | -95.9 | 504990 | 841 | -98.0 | 504990 | 843 | -98.4 | 504990 | 9 |
| MR_1774413883_9194E9C3 | 504990 | 763 | -94.6 | 504990 | 841 | -97.4 | 504990 | 843 | -99.5 | 504990 | 9 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 606: `13585e24-fb5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `13585e24-fb5c-4c77-9735-3ff4695b39b0` |
| Tag | **multiple-answer** |
| 정답 | **C6|C15** |
| C6 의미 | Adjust the azimuth of 3269522_2 by 50 degrees |
| C15 의미 | Increase transmission power for 3269522_2 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[606] topology](images/train_0606.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269522_2
- `C2`: Lift the tilt angle of 3269522_2 by 10 degrees
- `C3`: Increase A3 Offset threshold for 3269522_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Add neighbor relationship between 3226085_3 and 3226411_1
- `C6`: Adjust the azimuth of 3269522_2 by 50 degrees **← 정답**
- `C7`: Check test server and transmission issues
- `C8`: Increase transmission power for 3226411_1
- `C9`: Lift the tilt angle  of 3226411_1 by 5 degrees
- `C10`: Press down the tilt angle  of 3226411_1 by 5 degrees
- `C11`: Decrease transmission power for 3226411_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226411_1
- `C13`: Add neighbor relationship between 3269522_2 and 3226411_1
- `C14`: Decrease transmission power for 3269522_2
- `C15`: Increase transmission power for 3269522_2 **← 정답**
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269522_2
- `C17`: Increase A3 Offset threshold for 3226411_1
- `C18`: Decrease A3 Offset threshold for 3269522_2
- `C19`: Decrease A3 Offset threshold for 3226411_1
- `C20`: Adjust the azimuth of 3226411_1 by 21 degrees
- `C21`: Press down the tilt angle of 3269522_2 by 10 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226411_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.124 | MS1 | 121.4656777201 | 31.1446301175 | 98 | 504990 | -94.98 | 14.95 | 573.66 | 0.13 | 2.68 | 1581 |
| 2024-09-20 22:21:32.975 | MS1 | 121.4656593536 | 31.1446324885 | 98 | 504990 | -88.42 | 16.65 | 463.89 | 0.16 | 2.22 | 1599 |
| 2024-09-20 22:21:33.583 | MS1 | 121.4656768174 | 31.1446181362 | 98 | 504990 | -94.13 | 12.48 | 437.93 | 0.04 | 2.29 | 1597 |
| 2024-09-20 22:21:34.201 | MS1 | 121.4656618154 | 31.1446211681 | 98 | 504990 | -103.07 | 1.27 | 31.31 | 0.01 | 1.04 | 1593 |
| 2024-09-20 22:21:35.548 | MS1 | 121.4656749134 | 31.1446350211 | 98 | 504990 | -106.37 | -1.75 | 45.95 | 0.02 | 1.48 | 1564 |
| 2024-09-20 22:21:36.833 | MS1 | 121.4656769613 | 31.1446280913 | 98 | 504990 | -109.74 | 1.89 | 48.88 | 0.13 | 1.19 | 1569 |
| 2024-09-20 22:21:37.368 | MS1 | 121.4656719387 | 31.1446255230 | 98 | 504990 | -106.42 | -1.31 | 52.14 | 0.06 | 1.35 | 1574 |
| 2024-09-20 22:21:38.275 | MS1 | 121.4656663146 | 31.1446196179 | 98 | 504990 | -109.00 | 1.99 | 52.36 | 0.19 | 1.32 | 1561 |
| 2024-09-20 22:21:39.174 | MS1 | 121.4656584941 | 31.1446228970 | 98 | 504990 | -104.56 | 1.59 | 20.84 | 0.08 | 1.35 | 1581 |
| 2024-09-20 22:21:40.753 | MS1 | 121.4656774870 | 31.1446196048 | 98 | 504990 | -89.42 | 13.01 | 485.72 | 0.14 | 2.36 | 1572 |
| 2024-09-20 22:21:41.575 | MS1 | 121.4656731299 | 31.1446329655 | 98 | 504990 | -92.99 | 15.67 | 308.63 | 0.12 | 2.36 | 1571 |
| 2024-09-20 22:21:42.638 | MS1 | 121.4656706928 | 31.1446304886 | 98 | 504990 | -89.97 | 14.20 | 527.55 | 0.00 | 2.31 | 1587 |

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
| 3226085 | 3 | 121.4682494213 | 31.1498872311 | 291 | 4 | 1 | 36.9 | TDD | 301 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3226411 | 1 | 121.4657881634 | 31.1511999592 | 160 | 2 | 8 | 38.4 | TDD | 433 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3264109 | 4 | 121.4701207388 | 31.1508425884 | 179 | 8 | 2 | 46.8 | TDD | 97 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3269522 | 2 | 121.4746435808 | 31.1482849782 | 298 | 8 | 0 | 48.4 | TDD | 98 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.524 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.539 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.689 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.689 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.834 | NREventA2 | measId:1;ServCellPCI:190;Se... |
| 2024-09-20 22:21:34.961 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226411 | 1 | 8.3501 | 5.0838 | -114.0989 | 19.1881 | 197.1746 | 0.0146 | 0.0158 |
| 2024_09_20 22:00 | 3269522 | 2 | 15.4993 | 19.6758 | -115.9470 | 10.5736 | 180.5587 | 0.1212 | 0.0134 |
| 2024_09_20 22:00 | 3226085 | 3 | 19.0597 | 15.8581 | -115.0639 | 17.9432 | 98.5343 | 0.0080 | 0.0135 |
| 2024_09_20 22:00 | 3264109 | 4 | 14.2713 | 8.7533 | -117.5658 | 15.2909 | 199.9970 | 0.0131 | 0.0020 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415747_E13B6F3E | 504990 | 98 | -102.8 | 504990 | 433 | -107.5 | 504990 | 301 | -114.8 | 504990 | 97 |
| MR_1774415747_57011955 | 504990 | 98 | -101.4 | 504990 | 433 | -104.3 | 504990 | 301 | -114.4 | 504990 | 97 |
| MR_1774415747_662D8A40 | 504990 | 98 | -101.3 | 504990 | 433 | -104.1 | 504990 | 301 | -114.6 | 504990 | 97 |
| MR_1774415747_0EBB17D0 | 504990 | 98 | -101.2 | 504990 | 433 | -105.7 | 504990 | 301 | -112.3 | 504990 | 97 |
| MR_1774415747_90636A2E | 504990 | 98 | -103.6 | 504990 | 433 | -107.8 | 504990 | 301 | -112.2 | 504990 | 97 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 607: `240425f6-c9d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `240425f6-c9d3-4f22-8fcf-ab0002781f3e` |
| Tag | **multiple-answer** |
| 정답 | **C14|C21** |
| C14 의미 | Adjust the azimuth of 3274771_1 by 50 degrees |
| C21 의미 | Increase transmission power for 3274771_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[607] topology](images/train_0607.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3272452_2
- `C2`: Adjust the azimuth of 3272452_2 by 25 degrees
- `C3`: Lift the tilt angle of 3274771_1 by 5 degrees
- `C4`: Add neighbor relationship between 3273439_3 and 3272452_2
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274771_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274771_1
- `C8`: Increase transmission power for 3272452_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272452_2
- `C10`: Check test server and transmission issues
- `C11`: Press down the tilt angle of 3274771_1 by 5 degrees
- `C12`: Decrease A3 Offset threshold for 3272452_2
- `C13`: Increase A3 Offset threshold for 3272452_2
- `C14`: Adjust the azimuth of 3274771_1 by 50 degrees **← 정답**
- `C15`: Press down the tilt angle  of 3272452_2 by 5 degrees
- `C16`: Decrease A3 Offset threshold for 3274771_1
- `C17`: Decrease transmission power for 3274771_1
- `C18`: Add neighbor relationship between 3274771_1 and 3272452_2
- `C19`: Lift the tilt angle  of 3272452_2 by 5 degrees
- `C20`: Increase A3 Offset threshold for 3274771_1
- `C21`: Increase transmission power for 3274771_1 **← 정답**
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272452_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.753 | MS1 | 121.4656623898 | 31.1446299322 | 911 | 504990 | -88.61 | 13.83 | 435.36 | 0.09 | 2.71 | 1581 |
| 2024-09-20 22:21:32.522 | MS1 | 121.4656608806 | 31.1446286809 | 911 | 504990 | -94.66 | 13.45 | 446.95 | 0.09 | 2.03 | 1598 |
| 2024-09-20 22:21:33.407 | MS1 | 121.4656696541 | 31.1446290065 | 911 | 504990 | -88.87 | 17.49 | 510.45 | 0.19 | 2.29 | 1564 |
| 2024-09-20 22:21:34.581 | MS1 | 121.4656688666 | 31.1446274338 | 911 | 504990 | -107.24 | 0.43 | 48.89 | 0.15 | 1.10 | 1600 |
| 2024-09-20 22:21:35.536 | MS1 | 121.4656683483 | 31.1446231805 | 911 | 504990 | -100.56 | -0.05 | 21.43 | 0.08 | 1.40 | 1589 |
| 2024-09-20 22:21:36.691 | MS1 | 121.4656606024 | 31.1446330171 | 911 | 504990 | -105.52 | 0.45 | 38.47 | 0.05 | 1.38 | 1584 |
| 2024-09-20 22:21:37.662 | MS1 | 121.4656624507 | 31.1446220056 | 911 | 504990 | -108.21 | 1.19 | 20.89 | 0.17 | 1.23 | 1570 |
| 2024-09-20 22:21:38.931 | MS1 | 121.4656657204 | 31.1446359614 | 911 | 504990 | -106.34 | 0.91 | 20.55 | 0.08 | 1.05 | 1586 |
| 2024-09-20 22:21:39.614 | MS1 | 121.4656588650 | 31.1446213402 | 911 | 504990 | -101.54 | -1.58 | 25.19 | 0.20 | 1.38 | 1586 |
| 2024-09-20 22:21:40.232 | MS1 | 121.4656714887 | 31.1446379632 | 911 | 504990 | -86.76 | 15.68 | 324.86 | 0.11 | 2.74 | 1588 |
| 2024-09-20 22:21:41.316 | MS1 | 121.4656685826 | 31.1446367660 | 911 | 504990 | -89.12 | 17.29 | 347.98 | 0.01 | 2.63 | 1592 |
| 2024-09-20 22:21:42.628 | MS1 | 121.4656681951 | 31.1446215896 | 911 | 504990 | -85.41 | 15.01 | 570.02 | 0.04 | 2.85 | 1574 |

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
| 3253354 | 4 | 121.4725111990 | 31.1460250898 | 114 | 7 | 12 | 20.4 | TDD | 631 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3272452 | 2 | 121.4648318563 | 31.1526788890 | 150 | 4 | 5 | 15.5 | TDD | 139 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3273439 | 3 | 121.4732938290 | 31.1542462987 | 15 | 8 | 0 | 35.5 | TDD | 517 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3274771 | 1 | 121.4726934668 | 31.1447281214 | 194 | 1 | 6 | 49.5 | TDD | 911 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.894 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.913 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.020 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.020 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.282 | NREventA2 | measId:1;ServCellPCI:214;Se... |
| 2024-09-20 22:21:34.422 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274771 | 1 | 13.4764 | 18.7948 | -116.8600 | 17.8602 | 111.0876 | 0.1181 | 0.0024 |
| 2024_09_20 22:00 | 3272452 | 2 | 14.8117 | 8.0930 | -114.2600 | 14.4705 | 121.2517 | 0.0126 | 0.0131 |
| 2024_09_20 22:00 | 3273439 | 3 | 7.4887 | 12.1225 | -117.2927 | 6.0621 | 97.3775 | 0.0197 | 0.0101 |
| 2024_09_20 22:00 | 3253354 | 4 | 17.6314 | 11.9745 | -116.0542 | 7.8751 | 137.8391 | 0.0166 | 0.0066 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416609_79BC1897 | 504990 | 911 | -106.4 | 504990 | 139 | -109.8 | 504990 | 517 | -115.8 | 504990 | 631 |
| MR_1774416609_B07FCFC2 | 504990 | 911 | -106.0 | 504990 | 139 | -110.1 | 504990 | 517 | -116.4 | 504990 | 631 |
| MR_1774416609_A2FABB1F | 504990 | 911 | -106.4 | 504990 | 139 | -108.7 | 504990 | 517 | -113.7 | 504990 | 631 |
| MR_1774416609_BC0289A0 | 504990 | 911 | -107.6 | 504990 | 139 | -110.7 | 504990 | 517 | -114.1 | 504990 | 631 |
| MR_1774416609_4DF7D732 | 504990 | 911 | -105.5 | 504990 | 139 | -109.3 | 504990 | 517 | -115.1 | 504990 | 631 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 608: `96f982c1-60a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `96f982c1-60ac-4fd2-83b8-87ea8242211d` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Add neighbor relationship between 3254688_2 and 3231421_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[608] topology](images/train_0608.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3254688_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase transmission power for 3231421_3
- `C4`: Lift the tilt angle of 3254688_2 by 10 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254688_2
- `C6`: Decrease A3 Offset threshold for 3231421_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231421_3
- `C8`: Check test server and transmission issues
- `C9`: Press down the tilt angle  of 3231421_3 by 3 degrees
- `C10`: Decrease transmission power for 3231421_3
- `C11`: Add neighbor relationship between 3254688_2 and 3231421_3 **← 정답**
- `C12`: Increase A3 Offset threshold for 3231421_3
- `C13`: Increase A3 Offset threshold for 3254688_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231421_3
- `C15`: Add neighbor relationship between 3253968_4 and 3231421_3
- `C16`: Adjust the azimuth of 3254688_2 by 50 degrees
- `C17`: Adjust the azimuth of 3231421_3 by 42 degrees
- `C18`: Increase transmission power for 3254688_2
- `C19`: Lift the tilt angle  of 3231421_3 by 3 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254688_2
- `C21`: Press down the tilt angle of 3254688_2 by 10 degrees
- `C22`: Decrease transmission power for 3254688_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.383 | MS1 | 121.4656726106 | 31.1446315867 | 657 | 504990 | -80.78 | 13.48 | 524.08 | 0.03 | 2.39 | 1587 |
| 2024-09-20 22:21:32.194 | MS1 | 121.4656744787 | 31.1446269735 | 657 | 504990 | -80.60 | 16.50 | 488.28 | 0.09 | 2.79 | 1600 |
| 2024-09-20 22:21:33.911 | MS1 | 121.4656735002 | 31.1446351245 | 657 | 504990 | -76.78 | 17.85 | 594.40 | 0.01 | 2.07 | 1572 |
| 2024-09-20 22:21:34.941 | MS1 | 121.4656708779 | 31.1446331005 | 657 | 504990 | -92.28 | -1.89 | 60.79 | 0.09 | 1.42 | 1568 |
| 2024-09-20 22:21:35.624 | MS1 | 121.4656581760 | 31.1446328200 | 657 | 504990 | -87.43 | -3.46 | 58.35 | 0.06 | 1.24 | 1563 |
| 2024-09-20 22:21:36.536 | MS1 | 121.4656581259 | 31.1446195568 | 657 | 504990 | -92.35 | -0.88 | 29.33 | 0.06 | 1.08 | 1573 |
| 2024-09-20 22:21:37.971 | MS1 | 121.4656625237 | 31.1446185763 | 657 | 504990 | -85.65 | -2.45 | 56.90 | 0.04 | 1.31 | 1566 |
| 2024-09-20 22:21:38.633 | MS1 | 121.4656763750 | 31.1446212832 | 657 | 504990 | -76.85 | 13.95 | 440.06 | 0.09 | 1.35 | 1575 |
| 2024-09-20 22:21:39.606 | MS1 | 121.4656689731 | 31.1446361629 | 657 | 504990 | -75.10 | 15.10 | 316.73 | 0.09 | 1.16 | 1570 |
| 2024-09-20 22:21:40.499 | MS1 | 121.4656600846 | 31.1446360770 | 657 | 504990 | -82.36 | 14.71 | 455.85 | 0.18 | 2.41 | 1588 |
| 2024-09-20 22:21:41.590 | MS1 | 121.4656661894 | 31.1446324550 | 657 | 504990 | -79.70 | 15.63 | 555.92 | 0.04 | 2.89 | 1567 |
| 2024-09-20 22:21:42.452 | MS1 | 121.4656769870 | 31.1446346233 | 657 | 504990 | -80.98 | 13.98 | 486.86 | 0.02 | 2.04 | 1586 |

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
| 3231421 | 3 | 121.4711065420 | 31.1497515939 | 180 | 0 | 11 | 38.9 | TDD | 180 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3232368 | 1 | 121.4740572604 | 31.1474169120 | 359 | 1 | 6 | 35.4 | TDD | 568 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3253968 | 4 | 121.4672320784 | 31.1441170012 | 84 | 6 | 12 | 45.9 | TDD | 172 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3254688 | 2 | 121.4736415389 | 31.1454991402 | 143 | 14 | 6 | 44.2 | TDD | 657 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.524 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.541 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.658 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.658 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.398 | NREventA3 | measId:2;ServCellPCI:606;Se... |
| 2024-09-20 22:21:36.398 | NREventA3 | measId:2;ServCellPCI:606;Se... |
| 2024-09-20 22:21:37.398 | NREventA3 | measId:2;ServCellPCI:606;Se... |
| 2024-09-20 22:21:39.898 | NRRRCReestablishAttempt | PCI:606 |
| 2024-09-20 22:21:39.918 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.930 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:40.079 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.079 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232368 | 1 | 10.8822 | 7.0475 | -117.2107 | 7.7542 | 178.2360 | 0.0180 | 0.0126 |
| 2024_09_20 22:00 | 3254688 | 2 | 10.8893 | 16.9907 | -114.1438 | 5.4099 | 199.7571 | 0.0029 | 0.1858 |
| 2024_09_20 22:00 | 3231421 | 3 | 11.7983 | 17.8105 | -115.6334 | 12.4313 | 105.2804 | 0.0164 | 0.0048 |
| 2024_09_20 22:00 | 3253968 | 4 | 16.1815 | 14.6427 | -115.3039 | 12.2722 | 197.2625 | 0.0044 | 0.0046 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412909_C5C6A9EE | 504990 | 180 | -87.2 | 504990 | 657 | -92.6 | 504990 | 172 | -87.6 | 504990 | 568 |
| MR_1774412909_0DA41416 | 504990 | 657 | -92.0 | 504990 | 180 | -85.5 | 504990 | 172 | -87.0 | 504990 | 568 |
| MR_1774412909_461B1646 | 504990 | 180 | -86.6 | 504990 | 657 | -94.1 | 504990 | 172 | -88.9 | 504990 | 568 |
| MR_1774412909_40C1FE2A | 504990 | 657 | -91.6 | 504990 | 180 | -86.1 | 504990 | 172 | -86.7 | 504990 | 568 |
| MR_1774412909_8DCBD5AA | 504990 | 180 | -85.9 | 504990 | 657 | -91.6 | 504990 | 172 | -89.9 | 504990 | 568 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 609: `a848ac40-913...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a848ac40-9132-4889-8b0a-6e54e2aefd54` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[609] topology](images/train_0609.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3246056_1
- `C2`: Check test server and transmission issues **← 정답**
- `C3`: Lift the tilt angle  of 3249232_2 by 5 degrees
- `C4`: Increase transmission power for 3249232_2
- `C5`: Adjust the azimuth of 3246056_1 by 50 degrees
- `C6`: Increase A3 Offset threshold for 3246056_1
- `C7`: Decrease A3 Offset threshold for 3249232_2
- `C8`: Add neighbor relationship between 3246056_1 and 3249232_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246056_1
- `C10`: Decrease transmission power for 3249232_2
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Add neighbor relationship between 3262960_4 and 3249232_2
- `C13`: Lift the tilt angle of 3246056_1 by 2 degrees
- `C14`: Press down the tilt angle  of 3249232_2 by 5 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249232_2
- `C16`: Adjust the azimuth of 3249232_2 by 50 degrees
- `C17`: Increase A3 Offset threshold for 3249232_2
- `C18`: Increase transmission power for 3246056_1
- `C19`: Decrease transmission power for 3246056_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249232_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246056_1
- `C22`: Press down the tilt angle of 3246056_1 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.122 | MS1 | 121.4656651920 | 31.1446319642 | 64 | 504990 | -87.20 | 17.72 | 435.02 | 0.10 | 2.97 | 1573 |
| 2024-09-20 22:21:32.961 | MS1 | 121.4656614760 | 31.1446307213 | 64 | 504990 | -89.57 | 15.39 | 588.94 | 0.20 | 2.06 | 1599 |
| 2024-09-20 22:21:33.389 | MS1 | 121.4656740730 | 31.1446208734 | 64 | 504990 | -88.33 | 14.62 | 436.43 | 0.09 | 2.46 | 1599 |
| 2024-09-20 22:21:34.151 | MS1 | 121.4656631086 | 31.1446307148 | 64 | 504990 | -89.52 | 17.95 | 61.33 | 0.06 | 2.96 | 326 |
| 2024-09-20 22:21:35.372 | MS1 | 121.4656583852 | 31.1446292102 | 64 | 504990 | -90.08 | 14.79 | 53.59 | 0.15 | 2.72 | 425 |
| 2024-09-20 22:21:36.529 | MS1 | 121.4656606756 | 31.1446307364 | 64 | 504990 | -85.92 | 14.95 | 63.29 | 0.14 | 2.88 | 307 |
| 2024-09-20 22:21:37.922 | MS1 | 121.4656751428 | 31.1446231657 | 64 | 504990 | -93.04 | 12.66 | 66.53 | 0.13 | 2.68 | 473 |
| 2024-09-20 22:21:38.661 | MS1 | 121.4656762716 | 31.1446376682 | 64 | 504990 | -91.18 | 8.35 | 72.45 | 0.01 | 2.95 | 437 |
| 2024-09-20 22:21:39.738 | MS1 | 121.4656626957 | 31.1446218740 | 64 | 504990 | -93.86 | 10.70 | 76.42 | 0.09 | 2.43 | 493 |
| 2024-09-20 22:21:40.867 | MS1 | 121.4656688983 | 31.1446287305 | 64 | 504990 | -89.17 | 7.33 | 581.17 | 0.14 | 2.74 | 1588 |
| 2024-09-20 22:21:41.234 | MS1 | 121.4656685568 | 31.1446372463 | 64 | 504990 | -93.62 | 9.35 | 583.34 | 0.20 | 2.87 | 1599 |
| 2024-09-20 22:21:42.512 | MS1 | 121.4656584339 | 31.1446328619 | 64 | 504990 | -92.49 | 11.56 | 312.97 | 0.05 | 2.35 | 1585 |

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
| 3246056 | 1 | 121.4651328881 | 31.1556068257 | 80 | 0 | 0 | 45.9 | TDD | 64 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3246701 | 3 | 121.4678991801 | 31.1513829515 | 1 | 11 | 1 | 18.1 | TDD | 409 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3249232 | 2 | 121.4691846420 | 31.1452851839 | 179 | 0 | 10 | 32.9 | TDD | 905 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3262960 | 4 | 121.4741368361 | 31.1510752877 | 256 | 5 | 7 | 46.1 | TDD | 21 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.090 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.115 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.249 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.249 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.918 | NREventA3 | measId:2;ServCellPCI:723;Se... |
| 2024-09-20 22:21:38.158 | NRHandoverAttempt | SourcePCI:723;SourceNR-ARFC... |
| 2024-09-20 22:21:38.197 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.210 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.339 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.339 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246056 | 1 | 17.1987 | 14.8595 | -114.2488 | 9.0803 | 171.1487 | 0.0005 | 0.0174 |
| 2024_09_20 22:00 | 3249232 | 2 | 5.6541 | 17.3643 | -114.7796 | 14.6378 | 131.6455 | 0.0048 | 0.0061 |
| 2024_09_20 22:00 | 3246701 | 3 | 9.9132 | 8.0973 | -117.1852 | 11.2319 | 118.4953 | 0.0035 | 0.0029 |
| 2024_09_20 22:00 | 3262960 | 4 | 13.7367 | 19.6585 | -115.1288 | 16.3854 | 158.5098 | 0.0152 | 0.0077 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416984_F33961C8 | 504990 | 64 | -88.9 | 504990 | 905 | -99.6 | 504990 | 21 | -103.4 | 504990 | 409 |
| MR_1774416984_DF982175 | 504990 | 64 | -90.1 | 504990 | 905 | -97.7 | 504990 | 21 | -103.1 | 504990 | 409 |
| MR_1774416984_6230B64F | 504990 | 64 | -90.3 | 504990 | 905 | -98.4 | 504990 | 21 | -104.3 | 504990 | 409 |
| MR_1774416984_7CACB0C7 | 504990 | 64 | -91.0 | 504990 | 905 | -97.4 | 504990 | 21 | -102.9 | 504990 | 409 |
| MR_1774416984_E8D79B00 | 504990 | 64 | -88.3 | 504990 | 905 | -96.1 | 504990 | 21 | -102.4 | 504990 | 409 |
| MR_1774416984_C2B9C6CA | 504990 | 64 | -90.8 | 504990 | 905 | -97.8 | 504990 | 21 | -104.4 | 504990 | 409 |
| MR_1774416984_244C3539 | 504990 | 64 | -90.1 | 504990 | 905 | -98.2 | 504990 | 21 | -101.7 | 504990 | 409 |

> *... 2개 열 생략 (전체 14열)*

---
