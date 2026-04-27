# Track A 문제 분석 — train[1690]~train[1699]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1690] ~ train[1699] (10개)

## 목차

1. [문제 1690: `579a9317-8c4...`](#1690) — single-answer, 정답: C21
2. [문제 1691: `53b63c28-c43...`](#1691) — multiple-answer, 정답: C5|C10
3. [문제 1692: `fb9a5eb7-4a5...`](#1692) — single-answer, 정답: C21
4. [문제 1693: `6d03ea41-e84...`](#1693) — multiple-answer, 정답: C18|C22
5. [문제 1694: `2576c14e-df6...`](#1694) — single-answer, 정답: C9
6. [문제 1695: `ed2e142e-3e9...`](#1695) — multiple-answer, 정답: C2|C7|C12|C14
7. [문제 1696: `07dfe092-b61...`](#1696) — single-answer, 정답: C9
8. [문제 1697: `aa32270b-6f3...`](#1697) — single-answer, 정답: C10
9. [문제 1698: `b0899b25-630...`](#1698) — single-answer, 정답: C2
10. [문제 1699: `1726e0f0-8ad...`](#1699) — single-answer, 정답: C3

---

### 문제 1690: `579a9317-8c4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `579a9317-8c4a-4a0f-b590-001dc0f4d850` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1690] topology](images/train_1690.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214537_3
- `C2`: Increase transmission power for 3222136_2
- `C3`: Add neighbor relationship between 3258026_1 and 3214537_3
- `C4`: Decrease A3 Offset threshold for 3222136_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222136_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222136_2
- `C7`: Press down the tilt angle of 3222136_2 by 6 degrees
- `C8`: Decrease transmission power for 3214537_3
- `C9`: Increase A3 Offset threshold for 3214537_3
- `C10`: Adjust the azimuth of 3222136_2 by 50 degrees
- `C11`: Adjust the azimuth of 3214537_3 by 50 degrees
- `C12`: Increase A3 Offset threshold for 3222136_2
- `C13`: Press down the tilt angle  of 3214537_3 by 9 degrees
- `C14`: Decrease A3 Offset threshold for 3214537_3
- `C15`: Decrease transmission power for 3222136_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214537_3
- `C17`: Lift the tilt angle of 3222136_2 by 6 degrees
- `C18`: Increase transmission power for 3214537_3
- `C19`: Lift the tilt angle  of 3214537_3 by 9 degrees
- `C20`: Add neighbor relationship between 3222136_2 and 3214537_3
- `C21`: Check test server and transmission issues **← 정답**
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.646 | MS1 | 121.4656690841 | 31.1446265582 | 186 | 504990 | -88.09 | 16.31 | 386.56 | 0.07 | 2.84 | 1587 |
| 2024-09-20 22:21:32.673 | MS1 | 121.4656689633 | 31.1446374752 | 186 | 504990 | -87.80 | 13.42 | 563.63 | 0.17 | 2.25 | 1576 |
| 2024-09-20 22:21:33.432 | MS1 | 121.4656663246 | 31.1446338995 | 186 | 504990 | -90.93 | 15.18 | 410.64 | 0.03 | 2.17 | 1592 |
| 2024-09-20 22:21:34.386 | MS1 | 121.4656604758 | 31.1446265307 | 186 | 504990 | -85.54 | 15.30 | 90.06 | 0.12 | 2.52 | 357 |
| 2024-09-20 22:21:35.385 | MS1 | 121.4656692345 | 31.1446255603 | 186 | 504990 | -91.84 | 15.43 | 58.12 | 0.00 | 2.06 | 454 |
| 2024-09-20 22:21:36.496 | MS1 | 121.4656761856 | 31.1446197123 | 186 | 504990 | -88.13 | 15.30 | 55.29 | 0.17 | 2.64 | 456 |
| 2024-09-20 22:21:37.840 | MS1 | 121.4656696217 | 31.1446331900 | 186 | 504990 | -93.40 | 12.13 | 72.28 | 0.07 | 2.65 | 346 |
| 2024-09-20 22:21:38.670 | MS1 | 121.4656682534 | 31.1446379070 | 186 | 504990 | -90.58 | 10.58 | 72.38 | 0.13 | 2.78 | 388 |
| 2024-09-20 22:21:39.503 | MS1 | 121.4656654351 | 31.1446272475 | 186 | 504990 | -91.11 | 11.59 | 70.23 | 0.03 | 2.00 | 411 |
| 2024-09-20 22:21:40.943 | MS1 | 121.4656603034 | 31.1446366460 | 186 | 504990 | -93.65 | 8.03 | 343.85 | 0.01 | 2.15 | 1597 |
| 2024-09-20 22:21:41.653 | MS1 | 121.4656741568 | 31.1446210921 | 186 | 504990 | -92.96 | 8.00 | 445.60 | 0.03 | 2.93 | 1595 |
| 2024-09-20 22:21:42.288 | MS1 | 121.4656756744 | 31.1446270039 | 186 | 504990 | -91.16 | 9.19 | 570.88 | 0.00 | 2.79 | 1592 |

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
| 3214537 | 3 | 121.4745571140 | 31.1545776958 | 277 | 8 | 10 | 16.9 | TDD | 508 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3222136 | 2 | 121.4656569782 | 31.1525722327 | 314 | 3 | 8 | 45.7 | TDD | 186 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3240359 | 4 | 121.4748528644 | 31.1479350443 | 22 | 10 | 8 | 16.5 | TDD | 148 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3258026 | 1 | 121.4659580885 | 31.1539215070 | 302 | 9 | 3 | 34.9 | TDD | 681 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.849 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.867 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.986 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.986 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.655 | NREventA3 | measId:2;ServCellPCI:514;Se... |
| 2024-09-20 22:21:37.895 | NRHandoverAttempt | SourcePCI:514;SourceNR-ARFC... |
| 2024-09-20 22:21:37.943 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.955 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.076 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.076 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258026 | 1 | 13.9732 | 15.1243 | -114.9348 | 18.2583 | 104.5470 | 0.0016 | 0.0029 |
| 2024_09_20 22:00 | 3222136 | 2 | 11.6619 | 6.4703 | -115.7333 | 16.2921 | 91.5974 | 0.0128 | 0.0030 |
| 2024_09_20 22:00 | 3214537 | 3 | 10.1387 | 19.3886 | -114.2492 | 13.5149 | 186.5617 | 0.0086 | 0.0046 |
| 2024_09_20 22:00 | 3240359 | 4 | 11.6206 | 10.5108 | -117.5941 | 15.2807 | 197.4757 | 0.0000 | 0.0168 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413744_D7E23A5A | 504990 | 186 | -84.1 | 504990 | 508 | -91.2 | 504990 | 681 | -100.0 | 504990 | 148 |
| MR_1774413744_3EAE1A48 | 504990 | 186 | -85.0 | 504990 | 508 | -90.8 | 504990 | 681 | -100.4 | 504990 | 148 |
| MR_1774413744_03C36C9B | 504990 | 186 | -86.2 | 504990 | 508 | -89.2 | 504990 | 681 | -99.8 | 504990 | 148 |
| MR_1774413744_B8AD3742 | 504990 | 186 | -86.6 | 504990 | 508 | -91.3 | 504990 | 681 | -100.2 | 504990 | 148 |
| MR_1774413744_96664A76 | 504990 | 186 | -85.4 | 504990 | 508 | -89.7 | 504990 | 681 | -98.9 | 504990 | 148 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1691: `53b63c28-c43...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `53b63c28-c436-4a37-8769-11596c639a69` |
| Tag | **multiple-answer** |
| 정답 | **C5|C10** |
| C5 의미 | Decrease transmission power for 3225018_2 |
| C10 의미 | Press down the tilt angle  of 3225018_2 by 2 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1691] topology](images/train_1691.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225018_2
- `C2`: Increase transmission power for 3225018_2
- `C3`: Add neighbor relationship between 3276438_3 and 3225018_2
- `C4`: Adjust the azimuth of 3225018_2 by 15 degrees
- `C5`: Decrease transmission power for 3225018_2 **← 정답**
- `C6`: Lift the tilt angle of 3212696_4 by 3 degrees
- `C7`: Decrease A3 Offset threshold for 3225018_2
- `C8`: Add neighbor relationship between 3212696_4 and 3225018_2
- `C9`: Check test server and transmission issues
- `C10`: Press down the tilt angle  of 3225018_2 by 2 degrees **← 정답**
- `C11`: Increase A3 Offset threshold for 3212696_4
- `C12`: Press down the tilt angle of 3212696_4 by 3 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Increase transmission power for 3212696_4
- `C15`: Decrease transmission power for 3212696_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225018_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212696_4
- `C18`: Adjust the azimuth of 3212696_4 by 11 degrees
- `C19`: Decrease A3 Offset threshold for 3212696_4
- `C20`: Lift the tilt angle  of 3225018_2 by 2 degrees
- `C21`: Increase A3 Offset threshold for 3225018_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212696_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.745 | MS1 | 121.4656778006 | 31.1446271889 | 723 | 504990 | -83.35 | 16.34 | 496.31 | 0.07 | 2.66 | 1597 |
| 2024-09-20 22:21:32.537 | MS1 | 121.4656585886 | 31.1446366164 | 723 | 504990 | -78.20 | 15.27 | 321.87 | 0.07 | 2.81 | 1562 |
| 2024-09-20 22:21:33.885 | MS1 | 121.4656758325 | 31.1446245933 | 723 | 504990 | -76.96 | 17.70 | 351.26 | 0.09 | 2.15 | 1560 |
| 2024-09-20 22:21:34.429 | MS1 | 121.4656588155 | 31.1446237867 | 723 | 504990 | -88.67 | 1.03 | 50.92 | 0.06 | 1.19 | 1560 |
| 2024-09-20 22:21:35.980 | MS1 | 121.4656590355 | 31.1446227247 | 723 | 504990 | -85.96 | 2.56 | 94.39 | 0.19 | 1.02 | 1599 |
| 2024-09-20 22:21:36.998 | MS1 | 121.4656609442 | 31.1446213217 | 723 | 504990 | -90.92 | 0.31 | 89.36 | 0.18 | 1.44 | 1590 |
| 2024-09-20 22:21:37.310 | MS1 | 121.4656737802 | 31.1446331435 | 723 | 504990 | -86.45 | 0.56 | 56.04 | 0.10 | 1.49 | 1577 |
| 2024-09-20 22:21:38.785 | MS1 | 121.4656664275 | 31.1446298735 | 723 | 504990 | -86.00 | 0.08 | 46.92 | 0.12 | 1.22 | 1581 |
| 2024-09-20 22:21:39.942 | MS1 | 121.4656614650 | 31.1446344550 | 723 | 504990 | -94.61 | 1.75 | 87.73 | 0.17 | 1.21 | 1575 |
| 2024-09-20 22:21:40.833 | MS1 | 121.4656648282 | 31.1446278564 | 723 | 504990 | -77.33 | 15.37 | 477.75 | 0.16 | 2.70 | 1593 |
| 2024-09-20 22:21:41.891 | MS1 | 121.4656759176 | 31.1446294392 | 723 | 504990 | -81.46 | 13.00 | 375.89 | 0.04 | 2.30 | 1577 |
| 2024-09-20 22:21:42.928 | MS1 | 121.4656690478 | 31.1446191519 | 723 | 504990 | -84.79 | 14.24 | 306.36 | 0.15 | 2.04 | 1579 |

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
| 3212696 | 4 | 121.4659862121 | 31.1512691961 | 193 | 1 | 11 | 25.7 | TDD | 723 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3225018 | 2 | 121.4726285101 | 31.1546203864 | 226 | 1 | 3 | 27.8 | TDD | 662 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3228952 | 1 | 121.4668207103 | 31.1535802116 | 252 | 13 | 4 | 15.4 | TDD | 872 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3276438 | 3 | 121.4689506751 | 31.1446439479 | 44 | 15 | 6 | 22.8 | TDD | 267 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.573 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.588 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.708 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.708 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228952 | 1 | 17.7648 | 12.8174 | -117.4187 | 5.3269 | 180.5473 | 0.0142 | 0.0148 |
| 2024_09_20 22:00 | 3225018 | 2 | 8.9986 | 16.4035 | -115.8886 | 14.5365 | 155.4948 | 0.0028 | 0.0145 |
| 2024_09_20 22:00 | 3276438 | 3 | 7.9085 | 8.4789 | -115.6594 | 7.4543 | 191.1863 | 0.0145 | 0.0085 |
| 2024_09_20 22:00 | 3212696 | 4 | 14.0761 | 8.0450 | -109.4834 | 6.8567 | 167.4191 | 0.0174 | 0.0190 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416276_D7C18068 | 504990 | 662 | -89.9 | 504990 | 723 | -88.9 | 504990 | 267 | -87.4 | 504990 | 872 |
| MR_1774416276_784A9BD1 | 504990 | 723 | -89.2 | 504990 | 662 | -88.8 | 504990 | 267 | -90.5 | 504990 | 872 |
| MR_1774416276_1C1FF867 | 504990 | 662 | -86.8 | 504990 | 723 | -87.4 | 504990 | 267 | -90.9 | 504990 | 872 |
| MR_1774416276_C6658086 | 504990 | 723 | -90.4 | 504990 | 662 | -89.7 | 504990 | 267 | -87.6 | 504990 | 872 |
| MR_1774416276_589A1480 | 504990 | 723 | -88.1 | 504990 | 662 | -91.0 | 504990 | 267 | -90.9 | 504990 | 872 |
| MR_1774416276_F935C4CD | 504990 | 662 | -90.3 | 504990 | 723 | -90.5 | 504990 | 267 | -88.5 | 504990 | 872 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1692: `fb9a5eb7-4a5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fb9a5eb7-4a52-4606-84b2-c6c0e3704f37` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Lift the tilt angle  of 3240729_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1692] topology](images/train_1692.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250062_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250062_2
- `C4`: Press down the tilt angle of 3250062_2 by 6 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211659_1
- `C6`: Adjust the azimuth of 3240729_4 by 11 degrees
- `C7`: Decrease transmission power for 3211659_1
- `C8`: Increase transmission power for 3211659_1
- `C9`: Press down the tilt angle  of 3240729_4 by 10 degrees
- `C10`: Adjust the azimuth of 3250062_2 by 41 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211659_1
- `C12`: Increase A3 Offset threshold for 3211659_1
- `C13`: Add neighbor relationship between 3240729_4 and 3211659_1
- `C14`: Increase transmission power for 3250062_2
- `C15`: Check test server and transmission issues
- `C16`: Decrease A3 Offset threshold for 3211659_1
- `C17`: Decrease transmission power for 3250062_2
- `C18`: Increase A3 Offset threshold for 3250062_2
- `C19`: Add neighbor relationship between 3250062_2 and 3211659_1
- `C20`: Lift the tilt angle of 3250062_2 by 6 degrees
- `C21`: Lift the tilt angle  of 3240729_4 by 10 degrees **← 정답**
- `C22`: Decrease A3 Offset threshold for 3250062_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.360 | MS1 | 121.4656732938 | 31.1446319529 | 563 | 504990 | -87.23 | 13.86 | 533.47 | 0.13 | 2.02 | 1578 |
| 2024-09-20 22:21:32.984 | MS1 | 121.4656743232 | 31.1446220035 | 563 | 504990 | -91.65 | 15.56 | 565.86 | 0.18 | 2.56 | 1568 |
| 2024-09-20 22:21:33.948 | MS1 | 121.4656735302 | 31.1446330616 | 563 | 504990 | -91.97 | 17.56 | 447.24 | 0.10 | 2.16 | 1578 |
| 2024-09-20 22:21:34.548 | MS1 | 121.4656632443 | 31.1446239882 | 563 | 504990 | -89.30 | 17.81 | 59.67 | 0.02 | 2.21 | 1581 |
| 2024-09-20 22:21:35.322 | MS1 | 121.4656619125 | 31.1446239968 | 563 | 504990 | -85.61 | 13.96 | 76.66 | 0.06 | 2.95 | 1571 |
| 2024-09-20 22:21:36.511 | MS1 | 121.4656712744 | 31.1446188577 | 563 | 504990 | -86.86 | 17.29 | 64.24 | 0.05 | 2.86 | 1575 |
| 2024-09-20 22:21:37.662 | MS1 | 121.4656649155 | 31.1446254834 | 563 | 504990 | -89.19 | 12.28 | 88.11 | 0.19 | 2.14 | 1564 |
| 2024-09-20 22:21:38.971 | MS1 | 121.4656723088 | 31.1446196323 | 563 | 504990 | -93.14 | 12.12 | 77.25 | 0.12 | 2.19 | 1570 |
| 2024-09-20 22:21:39.672 | MS1 | 121.4656736697 | 31.1446365637 | 563 | 504990 | -90.56 | 12.84 | 87.55 | 0.14 | 2.21 | 1594 |
| 2024-09-20 22:21:40.524 | MS1 | 121.4656699197 | 31.1446293125 | 563 | 504990 | -91.18 | 8.91 | 476.83 | 0.12 | 2.24 | 1563 |
| 2024-09-20 22:21:41.528 | MS1 | 121.4656671167 | 31.1446280669 | 563 | 504990 | -90.85 | 10.79 | 414.04 | 0.01 | 2.23 | 1600 |
| 2024-09-20 22:21:42.103 | MS1 | 121.4656596107 | 31.1446260902 | 563 | 504990 | -89.91 | 11.46 | 299.04 | 0.14 | 2.57 | 1563 |

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
| 3211659 | 1 | 121.4716567426 | 31.1534757077 | 199 | 10 | 1 | 46.0 | TDD | 838 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3240729 | 4 | 121.4640256426 | 31.1517145788 | 297 | 9 | 10 | 31.0 | TDD | 751 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3250062 | 2 | 121.4737795541 | 31.1495716159 | 194 | 4 | 3 | 31.8 | TDD | 563 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3264829 | 3 | 121.4691952270 | 31.1535915090 | 291 | 10 | 7 | 42.7 | TDD | 638 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.615 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.630 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.773 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.773 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.472 | NREventA3 | measId:2;ServCellPCI:898;Se... |
| 2024-09-20 22:21:38.712 | NRHandoverAttempt | SourcePCI:898;SourceNR-ARFC... |
| 2024-09-20 22:21:38.745 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.756 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.889 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.889 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211659 | 1 | 10.2071 | 15.8101 | -117.8773 | 9.1122 | 166.9937 | 0.0055 | 0.0063 |
| 2024_09_20 22:00 | 3250062 | 2 | 92.2221 | 85.9230 | -114.5286 | 11.6842 | 199.0236 | 0.0113 | 0.0132 |
| 2024_09_20 22:00 | 3264829 | 3 | 12.6604 | 7.6701 | -117.5799 | 18.1487 | 91.3050 | 0.0194 | 0.0148 |
| 2024_09_20 22:00 | 3240729 | 4 | 19.4114 | 15.9523 | -115.2757 | 18.0968 | 93.2034 | 0.0112 | 0.0112 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414114_2D34ADBA | 504990 | 563 | -90.9 | 504990 | 838 | -92.9 | 504990 | 751 | -102.9 | 504990 | 638 |
| MR_1774414114_1DF0E26C | 504990 | 563 | -90.0 | 504990 | 838 | -89.4 | 504990 | 751 | -100.1 | 504990 | 638 |
| MR_1774414114_1D90D9DF | 504990 | 563 | -88.0 | 504990 | 838 | -89.8 | 504990 | 751 | -100.9 | 504990 | 638 |
| MR_1774414114_ED3B3E08 | 504990 | 563 | -88.9 | 504990 | 838 | -91.5 | 504990 | 751 | -99.8 | 504990 | 638 |
| MR_1774414114_E5700BE6 | 504990 | 563 | -90.4 | 504990 | 838 | -92.6 | 504990 | 751 | -103.0 | 504990 | 638 |
| MR_1774414114_A7C32FF9 | 504990 | 563 | -88.6 | 504990 | 838 | -90.2 | 504990 | 751 | -102.5 | 504990 | 638 |
| MR_1774414114_483F4916 | 504990 | 563 | -89.0 | 504990 | 838 | -90.9 | 504990 | 751 | -103.2 | 504990 | 638 |
| MR_1774414114_9E8D1B88 | 504990 | 563 | -87.9 | 504990 | 838 | -93.2 | 504990 | 751 | -100.0 | 504990 | 638 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1693: `6d03ea41-e84...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6d03ea41-e84c-47e3-a34f-2434a2216d3f` |
| Tag | **multiple-answer** |
| 정답 | **C18|C22** |
| C18 의미 | Press down the tilt angle  of 3240849_2 by 4 degrees |
| C22 의미 | Decrease transmission power for 3240849_2 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1693] topology](images/train_1693.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3240849_2
- `C2`: Increase A3 Offset threshold for 3265561_1
- `C3`: Decrease transmission power for 3265561_1
- `C4`: Adjust the azimuth of 3240849_2 by 0 degrees
- `C5`: Increase transmission power for 3265561_1
- `C6`: Decrease A3 Offset threshold for 3265561_1
- `C7`: Adjust the azimuth of 3265561_1 by 9 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265561_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Lift the tilt angle  of 3240849_2 by 4 degrees
- `C11`: Check test server and transmission issues
- `C12`: Lift the tilt angle of 3265561_1 by 3 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240849_2
- `C14`: Increase A3 Offset threshold for 3240849_2
- `C15`: Press down the tilt angle of 3265561_1 by 3 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240849_2
- `C17`: Increase transmission power for 3240849_2
- `C18`: Press down the tilt angle  of 3240849_2 by 4 degrees **← 정답**
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265561_1
- `C20`: Add neighbor relationship between 3265561_1 and 3240849_2
- `C21`: Add neighbor relationship between 3264926_4 and 3240849_2
- `C22`: Decrease transmission power for 3240849_2 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.910 | MS1 | 121.4656679446 | 31.1446321715 | 736 | 504990 | -79.19 | 13.80 | 577.44 | 0.03 | 2.61 | 1600 |
| 2024-09-20 22:21:32.537 | MS1 | 121.4656748437 | 31.1446285463 | 736 | 504990 | -79.00 | 12.43 | 532.42 | 0.12 | 2.25 | 1570 |
| 2024-09-20 22:21:33.141 | MS1 | 121.4656668833 | 31.1446269735 | 736 | 504990 | -78.78 | 15.90 | 573.09 | 0.03 | 2.43 | 1588 |
| 2024-09-20 22:21:34.445 | MS1 | 121.4656663682 | 31.1446293288 | 736 | 504990 | -89.93 | 2.74 | 58.34 | 0.14 | 1.27 | 1568 |
| 2024-09-20 22:21:35.803 | MS1 | 121.4656759661 | 31.1446189404 | 736 | 504990 | -92.60 | 1.50 | 39.64 | 0.08 | 1.34 | 1562 |
| 2024-09-20 22:21:36.813 | MS1 | 121.4656739033 | 31.1446231901 | 736 | 504990 | -89.98 | 2.98 | 83.53 | 0.16 | 1.23 | 1564 |
| 2024-09-20 22:21:37.918 | MS1 | 121.4656770008 | 31.1446187489 | 736 | 504990 | -85.85 | 2.20 | 64.04 | 0.20 | 1.18 | 1570 |
| 2024-09-20 22:21:38.430 | MS1 | 121.4656685408 | 31.1446203807 | 736 | 504990 | -92.14 | 0.17 | 76.89 | 0.12 | 1.41 | 1573 |
| 2024-09-20 22:21:39.113 | MS1 | 121.4656754584 | 31.1446259574 | 736 | 504990 | -92.41 | 0.35 | 83.30 | 0.03 | 1.08 | 1584 |
| 2024-09-20 22:21:40.686 | MS1 | 121.4656668158 | 31.1446321619 | 736 | 504990 | -76.73 | 13.65 | 519.60 | 0.02 | 2.36 | 1596 |
| 2024-09-20 22:21:41.834 | MS1 | 121.4656678435 | 31.1446211432 | 736 | 504990 | -83.57 | 13.81 | 563.04 | 0.15 | 2.08 | 1580 |
| 2024-09-20 22:21:42.738 | MS1 | 121.4656590052 | 31.1446339996 | 736 | 504990 | -79.21 | 17.49 | 429.06 | 0.01 | 2.99 | 1593 |

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
| 3229767 | 3 | 121.4675523757 | 31.1555166336 | 330 | 2 | 3 | 37.2 | TDD | 4 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3240849 | 2 | 121.4653159832 | 31.1556256294 | 178 | 3 | 2 | 23.1 | TDD | 250 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3264926 | 4 | 121.4667353707 | 31.1513070656 | 44 | 2 | 9 | 41.6 | TDD | 694 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3265561 | 1 | 121.4709075591 | 31.1531683033 | 199 | 1 | 8 | 35.1 | TDD | 736 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.997 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.012 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.152 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.152 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265561 | 1 | 10.2371 | 15.0288 | -109.4543 | 10.9065 | 189.7725 | 0.0184 | 0.0102 |
| 2024_09_20 22:00 | 3240849 | 2 | 6.5533 | 14.0298 | -115.3055 | 15.6139 | 127.2104 | 0.0182 | 0.0035 |
| 2024_09_20 22:00 | 3229767 | 3 | 18.0001 | 5.1699 | -117.5476 | 6.1340 | 117.0487 | 0.0191 | 0.0191 |
| 2024_09_20 22:00 | 3264926 | 4 | 11.6304 | 9.3729 | -114.6123 | 8.2793 | 137.4199 | 0.0090 | 0.0032 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413867_260A3E30 | 504990 | 250 | -90.4 | 504990 | 736 | -87.7 | 504990 | 694 | -89.2 | 504990 | 4 |
| MR_1774413867_3A0C7552 | 504990 | 736 | -91.3 | 504990 | 250 | -89.9 | 504990 | 694 | -92.2 | 504990 | 4 |
| MR_1774413867_BEC8A3F0 | 504990 | 250 | -90.0 | 504990 | 736 | -86.0 | 504990 | 694 | -89.2 | 504990 | 4 |
| MR_1774413867_9D37C02B | 504990 | 250 | -90.2 | 504990 | 736 | -88.0 | 504990 | 694 | -89.4 | 504990 | 4 |
| MR_1774413867_ADA0D684 | 504990 | 736 | -91.9 | 504990 | 250 | -86.7 | 504990 | 694 | -92.7 | 504990 | 4 |
| MR_1774413867_F752C33F | 504990 | 736 | -91.0 | 504990 | 250 | -86.5 | 504990 | 694 | -89.8 | 504990 | 4 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1694: `2576c14e-df6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2576c14e-df65-413d-934f-955a94dc27ac` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1694] topology](images/train_1694.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3230356_2
- `C2`: Lift the tilt angle  of 3230356_2 by 5 degrees
- `C3`: Add neighbor relationship between 3223768_3 and 3230356_2
- `C4`: Increase A3 Offset threshold for 3230356_2
- `C5`: Decrease A3 Offset threshold for 3230356_2
- `C6`: Adjust the azimuth of 3230356_2 by 50 degrees
- `C7`: Increase A3 Offset threshold for 3223768_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223768_3
- `C9`: Insufficient data; more data is needed for judgment. **← 정답**
- `C10`: Check test server and transmission issues
- `C11`: Decrease transmission power for 3223768_3
- `C12`: Adjust the azimuth of 3223768_3 by 50 degrees
- `C13`: Add neighbor relationship between 3269372_1 and 3230356_2
- `C14`: Increase transmission power for 3230356_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230356_2
- `C16`: Lift the tilt angle of 3223768_3 by 10 degrees
- `C17`: Increase transmission power for 3223768_3
- `C18`: Press down the tilt angle of 3223768_3 by 10 degrees
- `C19`: Decrease A3 Offset threshold for 3223768_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223768_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230356_2
- `C22`: Press down the tilt angle  of 3230356_2 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.644 | MS1 | 121.4656597776 | 31.1446331772 | 430 | 504990 | -87.09 | 17.01 | 555.48 | 0.09 | 2.67 | 1582 |
| 2024-09-20 22:21:32.719 | MS1 | 121.4656765554 | 31.1446377771 | 430 | 504990 | -89.08 | 15.51 | 505.96 | 0.18 | 2.47 | 1582 |
| 2024-09-20 22:21:33.513 | MS1 | 121.4656769606 | 31.1446202641 | 430 | 504990 | -90.42 | 14.62 | 396.67 | 0.16 | 2.85 | 1585 |
| 2024-09-20 22:21:34.581 | MS1 | 121.4656732680 | 31.1446193997 | 430 | 504990 | -87.41 | 17.58 | 98.40 | 0.16 | 2.75 | 1598 |
| 2024-09-20 22:21:35.972 | MS1 | 121.4656589658 | 31.1446367629 | 430 | 504990 | -91.72 | 12.91 | 96.34 | 0.07 | 2.58 | 1567 |
| 2024-09-20 22:21:36.453 | MS1 | 121.4656641346 | 31.1446285220 | 430 | 504990 | -89.49 | 13.28 | 69.41 | 0.20 | 2.16 | 1577 |
| 2024-09-20 22:21:37.628 | MS1 | 121.4656624264 | 31.1446244482 | 430 | 504990 | -92.79 | 9.72 | 54.87 | 0.04 | 2.39 | 1582 |
| 2024-09-20 22:21:38.797 | MS1 | 121.4656679040 | 31.1446367881 | 430 | 504990 | -91.77 | 7.75 | 83.13 | 0.01 | 2.15 | 1593 |
| 2024-09-20 22:21:39.852 | MS1 | 121.4656632474 | 31.1446350447 | 430 | 504990 | -89.14 | 8.44 | 94.43 | 0.08 | 2.27 | 1589 |
| 2024-09-20 22:21:40.472 | MS1 | 121.4656653690 | 31.1446317692 | 430 | 504990 | -89.58 | 11.20 | 425.99 | 0.12 | 2.82 | 1586 |
| 2024-09-20 22:21:41.187 | MS1 | 121.4656644565 | 31.1446371362 | 430 | 504990 | -92.41 | 7.91 | 483.29 | 0.07 | 2.57 | 1576 |
| 2024-09-20 22:21:42.546 | MS1 | 121.4656642289 | 31.1446361073 | 430 | 504990 | -91.53 | 9.65 | 405.09 | 0.11 | 2.57 | 1568 |

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
| 3223768 | 3 | 121.4716950148 | 31.1441745326 | 210 | 8 | 7 | 44.3 | TDD | 430 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3230356 | 2 | 121.4753671526 | 31.1517048031 | 46 | 4 | 12 | 30.3 | TDD | 1001 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3237365 | 4 | 121.4750033171 | 31.1474518118 | 173 | 15 | 12 | 24.4 | TDD | 566 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3269372 | 1 | 121.4662002931 | 31.1474929473 | 198 | 3 | 11 | 34.9 | TDD | 776 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.808 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.829 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.942 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.942 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.698 | NREventA3 | measId:2;ServCellPCI:155;Se... |
| 2024-09-20 22:21:37.938 | NRHandoverAttempt | SourcePCI:155;SourceNR-ARFC... |
| 2024-09-20 22:21:37.970 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.985 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.125 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.125 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3269372 | 1 | 86.5282 | 84.1105 | -117.6403 | 10.2905 | 168.9640 | 0.0146 | 0.0150 |
| 2024_09_19 22:00 | 3230356 | 2 | 89.8458 | 82.5696 | -114.5667 | 18.7282 | 125.5233 | 0.0041 | 0.0195 |
| 2024_09_19 22:00 | 3223768 | 3 | 77.4308 | 84.8501 | -116.5309 | 7.2055 | 157.3190 | 0.0095 | 0.0090 |
| 2024_09_19 22:00 | 3237365 | 4 | 76.7184 | 78.9880 | -114.3335 | 6.4380 | 179.6017 | 0.0084 | 0.0179 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413515_4887BBD4 | 504990 | 430 | -85.9 | 504990 | 1001 | -94.1 | 504990 | 776 | -102.6 | 504990 | 566 |
| MR_1774413515_C1F09481 | 504990 | 430 | -86.1 | 504990 | 1001 | -95.8 | 504990 | 776 | -100.0 | 504990 | 566 |
| MR_1774413515_4BA208AC | 504990 | 430 | -88.7 | 504990 | 1001 | -92.1 | 504990 | 776 | -103.1 | 504990 | 566 |
| MR_1774413515_963B2FA9 | 504990 | 430 | -85.7 | 504990 | 1001 | -92.2 | 504990 | 776 | -100.7 | 504990 | 566 |
| MR_1774413515_B71574ED | 504990 | 430 | -86.6 | 504990 | 1001 | -95.2 | 504990 | 776 | -102.0 | 504990 | 566 |
| MR_1774413515_DAB416FB | 504990 | 430 | -85.4 | 504990 | 1001 | -95.9 | 504990 | 776 | -99.4 | 504990 | 566 |
| MR_1774413515_CDE6B039 | 504990 | 430 | -85.6 | 504990 | 1001 | -94.8 | 504990 | 776 | -100.1 | 504990 | 566 |
| MR_1774413515_711F504D | 504990 | 430 | -87.3 | 504990 | 1001 | -92.4 | 504990 | 776 | -101.8 | 504990 | 566 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1695: `ed2e142e-3e9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ed2e142e-3e97-43bb-9f45-197641c4bcaf` |
| Tag | **multiple-answer** |
| 정답 | **C2|C7|C12|C14** |
| C2 의미 | Decrease transmission power for 3249707_5 |
| C7 의미 | Press down the tilt angle  of 3249707_5 by 5 degrees |
| C12 의미 | Increase A3 Offset threshold for 3266008_4 |
| C14 의미 | Increase A3 Offset threshold for 3249707_5 |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1695] topology](images/train_1695.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249707_5
- `C2`: Decrease transmission power for 3249707_5 **← 정답**
- `C3`: Decrease A3 Offset threshold for 3266008_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249707_5
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266008_4
- `C6`: Increase transmission power for 3249707_5
- `C7`: Press down the tilt angle  of 3249707_5 by 5 degrees **← 정답**
- `C8`: Add neighbor relationship between 3266008_4 and 3249707_5
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266008_4
- `C10`: Adjust the azimuth of 3266008_4 by 12 degrees
- `C11`: Increase transmission power for 3266008_4
- `C12`: Increase A3 Offset threshold for 3266008_4 **← 정답**
- `C13`: Decrease A3 Offset threshold for 3249707_5
- `C14`: Increase A3 Offset threshold for 3249707_5 **← 정답**
- `C15`: Decrease transmission power for 3266008_4
- `C16`: Lift the tilt angle of 3266008_4 by 1 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Press down the tilt angle of 3266008_4 by 1 degrees
- `C19`: Adjust the azimuth of 3249707_5 by 28 degrees
- `C20`: Check test server and transmission issues
- `C21`: Lift the tilt angle  of 3249707_5 by 5 degrees
- `C22`: Add neighbor relationship between 3211582_3 and 3249707_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.919 | MS1 | 121.4656691352 | 31.1446277647 | 203 | 504990 | -84.37 | 13.92 | 465.09 | 0.11 | 2.13 | 1591 |
| 2024-09-20 22:21:32.442 | MS1 | 121.4656616498 | 31.1446201553 | 203 | 504990 | -82.18 | 14.08 | 352.16 | 0.14 | 2.45 | 1595 |
| 2024-09-20 22:21:33.859 | MS1 | 121.4656581834 | 31.1446354934 | 203 | 504990 | -75.26 | 16.47 | 559.08 | 0.16 | 2.61 | 1593 |
| 2024-09-20 22:21:34.607 | MS1 | 121.4656688299 | 31.1446207835 | 199 | 504990 | -87.70 | 4.70 | 59.06 | 0.15 | 1.08 | 1600 |
| 2024-09-20 22:21:35.823 | MS1 | 121.4656743256 | 31.1446227375 | 199 | 504990 | -84.63 | 4.56 | 77.55 | 0.14 | 1.03 | 1588 |
| 2024-09-20 22:21:36.318 | MS1 | 121.4656746981 | 31.1446234977 | 203 | 504990 | -83.29 | 4.42 | 38.58 | 0.03 | 1.04 | 1576 |
| 2024-09-20 22:21:37.386 | MS1 | 121.4656599153 | 31.1446375530 | 203 | 504990 | -89.74 | 4.54 | 26.97 | 0.16 | 1.08 | 1561 |
| 2024-09-20 22:21:38.435 | MS1 | 121.4656734464 | 31.1446195273 | 199 | 504990 | -80.73 | 4.21 | 62.62 | 0.19 | 1.33 | 1575 |
| 2024-09-20 22:21:39.599 | MS1 | 121.4656667210 | 31.1446269423 | 199 | 504990 | -88.08 | 4.35 | 62.27 | 0.12 | 1.22 | 1579 |
| 2024-09-20 22:21:40.784 | MS1 | 121.4656599073 | 31.1446255627 | 199 | 504990 | -81.59 | 12.80 | 446.53 | 0.10 | 2.76 | 1560 |
| 2024-09-20 22:21:41.771 | MS1 | 121.4656624734 | 31.1446234901 | 199 | 504990 | -79.85 | 13.49 | 496.69 | 0.09 | 2.50 | 1594 |
| 2024-09-20 22:21:42.945 | MS1 | 121.4656649569 | 31.1446343575 | 199 | 504990 | -81.49 | 16.42 | 523.28 | 0.00 | 2.29 | 1571 |

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
| 3211582 | 3 | 121.4664337875 | 31.1503979468 | 50 | 11 | 2 | 42.4 | TDD | 9 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3249707 | 5 | 121.4646890799 | 31.1542694948 | 203 | 4 | 7 | 20.8 | TDD | 223 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3253320 | 2 | 121.4660231674 | 31.1510601507 | 84 | 7 | 4 | 43.2 | TDD | 199 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3257035 | 1 | 121.4703193960 | 31.1440114493 | 205 | 3 | 6 | 49.6 | TDD | 195 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3266008 | 4 | 121.4669161069 | 31.1552246157 | 174 | 0 | 10 | 22.6 | TDD | 203 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.255 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.279 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.381 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.381 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.136 | NREventA3 | measId:2;ServCellPCI:171;Se... |
| 2024-09-20 22:21:34.376 | NRHandoverAttempt | SourcePCI:171;SourceNR-ARFC... |
| 2024-09-20 22:21:34.408 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.420 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:34.565 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.565 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.136 | NREventA3 | measId:2;ServCellPCI:635;Se... |
| 2024-09-20 22:21:36.376 | NRHandoverAttempt | SourcePCI:635;SourceNR-ARFC... |
| 2024-09-20 22:21:36.411 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.424 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.530 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.530 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.136 | NREventA3 | measId:2;ServCellPCI:171;Se... |
| 2024-09-20 22:21:38.376 | NRHandoverAttempt | SourcePCI:171;SourceNR-ARFC... |
| 2024-09-20 22:21:38.410 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.423 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.565 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.565 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257035 | 1 | 14.2311 | 18.7025 | -116.4333 | 9.2628 | 115.4009 | 0.0058 | 0.0019 |
| 2024_09_20 22:00 | 3253320 | 2 | 14.2664 | 19.9163 | -114.3483 | 5.9393 | 135.5753 | 0.0093 | 0.0014 |
| 2024_09_20 22:00 | 3211582 | 3 | 5.5343 | 5.4895 | -117.7454 | 5.2092 | 157.2885 | 0.0001 | 0.0112 |
| 2024_09_20 22:00 | 3266008 | 4 | 6.5693 | 12.3169 | -115.5404 | 12.1846 | 108.4069 | 0.0041 | 0.0082 |
| 2024_09_20 22:00 | 3249707 | 5 | 6.9130 | 7.9040 | -116.2845 | 10.3640 | 158.9671 | 0.0033 | 0.0149 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416324_70C441A9 | 504990 | 203 | -88.0 | 504990 | 199 | -87.4 | 504990 | 223 | -89.3 | 504990 | 9 |
| MR_1774416324_51D59A87 | 504990 | 199 | -88.2 | 504990 | 203 | -86.4 | 504990 | 223 | -88.9 | 504990 | 9 |
| MR_1774416324_6996D30B | 504990 | 199 | -88.0 | 504990 | 203 | -85.4 | 504990 | 223 | -88.5 | 504990 | 9 |
| MR_1774416324_4FBC08A8 | 504990 | 199 | -85.8 | 504990 | 203 | -85.5 | 504990 | 223 | -88.4 | 504990 | 9 |
| MR_1774416324_5E4494CC | 504990 | 203 | -86.1 | 504990 | 199 | -84.8 | 504990 | 223 | -92.2 | 504990 | 9 |
| MR_1774416324_F3D3C989 | 504990 | 199 | -89.2 | 504990 | 203 | -86.8 | 504990 | 223 | -90.0 | 504990 | 9 |
| MR_1774416324_7250CDC2 | 504990 | 203 | -86.0 | 504990 | 199 | -88.5 | 504990 | 223 | -90.6 | 504990 | 9 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1696: `07dfe092-b61...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `07dfe092-b611-4d89-89b5-11464189e6ee` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1696] topology](images/train_1696.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3239717_1
- `C2`: Decrease transmission power for 3239717_1
- `C3`: Lift the tilt angle of 3239717_1 by 10 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239717_1
- `C5`: Increase A3 Offset threshold for 3229497_3
- `C6`: Adjust the azimuth of 3239717_1 by 47 degrees
- `C7`: Add neighbor relationship between 3239717_1 and 3229497_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229497_3
- `C9`: Insufficient data; more data is needed for judgment. **← 정답**
- `C10`: Adjust the azimuth of 3229497_3 by 11 degrees
- `C11`: Decrease A3 Offset threshold for 3239717_1
- `C12`: Decrease transmission power for 3229497_3
- `C13`: Increase transmission power for 3229497_3
- `C14`: Lift the tilt angle  of 3229497_3 by 10 degrees
- `C15`: Press down the tilt angle  of 3229497_3 by 10 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239717_1
- `C17`: Add neighbor relationship between 3267224_2 and 3229497_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229497_3
- `C19`: Press down the tilt angle of 3239717_1 by 10 degrees
- `C20`: Decrease A3 Offset threshold for 3229497_3
- `C21`: Increase transmission power for 3239717_1
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.850 | MS1 | 121.4656727561 | 31.1446286085 | 912 | 504990 | -88.47 | 17.03 | 459.29 | 0.01 | 2.35 | 1582 |
| 2024-09-20 22:21:32.950 | MS1 | 121.4656734561 | 31.1446218988 | 912 | 504990 | -89.79 | 12.44 | 478.61 | 0.02 | 2.91 | 1577 |
| 2024-09-20 22:21:33.214 | MS1 | 121.4656705741 | 31.1446202500 | 912 | 504990 | -91.67 | 13.58 | 311.42 | 0.18 | 2.22 | 1584 |
| 2024-09-20 22:21:34.636 | MS1 | 121.4656713367 | 31.1446356044 | 912 | 504990 | -88.30 | 16.99 | 51.97 | 0.02 | 2.26 | 1600 |
| 2024-09-20 22:21:35.883 | MS1 | 121.4656603337 | 31.1446281451 | 912 | 504990 | -91.89 | 16.12 | 80.57 | 0.04 | 2.16 | 1599 |
| 2024-09-20 22:21:36.944 | MS1 | 121.4656639082 | 31.1446257719 | 912 | 504990 | -89.42 | 14.03 | 87.85 | 0.11 | 2.67 | 1574 |
| 2024-09-20 22:21:37.161 | MS1 | 121.4656620782 | 31.1446248954 | 912 | 504990 | -93.01 | 11.16 | 74.59 | 0.07 | 2.62 | 1565 |
| 2024-09-20 22:21:38.349 | MS1 | 121.4656656759 | 31.1446350782 | 912 | 504990 | -91.76 | 7.59 | 92.69 | 0.11 | 2.26 | 1588 |
| 2024-09-20 22:21:39.640 | MS1 | 121.4656717349 | 31.1446187035 | 912 | 504990 | -90.55 | 12.50 | 58.51 | 0.19 | 2.73 | 1577 |
| 2024-09-20 22:21:40.816 | MS1 | 121.4656742335 | 31.1446378026 | 912 | 504990 | -89.15 | 12.82 | 593.40 | 0.07 | 2.86 | 1566 |
| 2024-09-20 22:21:41.790 | MS1 | 121.4656617495 | 31.1446193087 | 912 | 504990 | -92.23 | 11.79 | 540.66 | 0.09 | 2.07 | 1569 |
| 2024-09-20 22:21:42.933 | MS1 | 121.4656613320 | 31.1446274632 | 912 | 504990 | -93.83 | 7.43 | 551.00 | 0.17 | 2.86 | 1598 |

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
| 3229497 | 3 | 121.4671081154 | 31.1483827952 | 209 | 4 | 1 | 47.8 | TDD | 563 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3239717 | 1 | 121.4645919420 | 31.1455278300 | 181 | 13 | 10 | 46.1 | TDD | 912 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3243517 | 4 | 121.4741583093 | 31.1451450887 | 157 | 11 | 10 | 46.0 | TDD | 207 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3267224 | 2 | 121.4726698447 | 31.1512934660 | 198 | 5 | 9 | 38.3 | TDD | 801 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.417 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.432 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.560 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.560 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.237 | NREventA3 | measId:2;ServCellPCI:111;Se... |
| 2024-09-20 22:21:38.477 | NRHandoverAttempt | SourcePCI:111;SourceNR-ARFC... |
| 2024-09-20 22:21:38.518 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.528 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.664 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.664 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3239717 | 1 | 86.7710 | 93.9868 | -117.4315 | 14.3150 | 150.1060 | 0.0012 | 0.0198 |
| 2024_09_19 22:00 | 3267224 | 2 | 76.6225 | 81.7701 | -117.0908 | 18.1319 | 127.1974 | 0.0023 | 0.0074 |
| 2024_09_19 22:00 | 3229497 | 3 | 78.2898 | 76.9968 | -117.2622 | 10.5348 | 163.7148 | 0.0118 | 0.0099 |
| 2024_09_19 22:00 | 3243517 | 4 | 79.1644 | 81.1501 | -116.9622 | 19.2459 | 135.8463 | 0.0167 | 0.0030 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412990_51BA8B43 | 504990 | 912 | -87.6 | 504990 | 563 | -92.0 | 504990 | 801 | -98.2 | 504990 | 207 |
| MR_1774412990_90F03B6A | 504990 | 912 | -86.9 | 504990 | 563 | -93.4 | 504990 | 801 | -95.0 | 504990 | 207 |
| MR_1774412990_D1544CE1 | 504990 | 912 | -90.0 | 504990 | 563 | -95.1 | 504990 | 801 | -95.0 | 504990 | 207 |
| MR_1774412990_4F8A96AA | 504990 | 912 | -88.8 | 504990 | 563 | -94.6 | 504990 | 801 | -95.8 | 504990 | 207 |
| MR_1774412990_0886D085 | 504990 | 912 | -89.6 | 504990 | 563 | -93.7 | 504990 | 801 | -96.1 | 504990 | 207 |
| MR_1774412990_4E608520 | 504990 | 912 | -87.2 | 504990 | 563 | -93.9 | 504990 | 801 | -95.4 | 504990 | 207 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1697: `aa32270b-6f3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `aa32270b-6f3f-4314-8a3e-913f5de678bb` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease A3 Offset threshold for 3216129_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1697] topology](images/train_1697.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3279387_1 by 50 degrees
- `C2`: Decrease transmission power for 3216129_3
- `C3`: Check test server and transmission issues
- `C4`: Increase transmission power for 3279387_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216129_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279387_1
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Add neighbor relationship between 3216129_3 and 3279387_1
- `C9`: Lift the tilt angle of 3216129_3 by 6 degrees
- `C10`: Decrease A3 Offset threshold for 3216129_3 **← 정답**
- `C11`: Press down the tilt angle of 3216129_3 by 6 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279387_1
- `C13`: Increase transmission power for 3216129_3
- `C14`: Press down the tilt angle  of 3279387_1 by 7 degrees
- `C15`: Decrease A3 Offset threshold for 3279387_1
- `C16`: Increase A3 Offset threshold for 3216129_3
- `C17`: Add neighbor relationship between 3270303_4 and 3279387_1
- `C18`: Increase A3 Offset threshold for 3279387_1
- `C19`: Decrease transmission power for 3279387_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216129_3
- `C21`: Lift the tilt angle  of 3279387_1 by 7 degrees
- `C22`: Adjust the azimuth of 3216129_3 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.560 | MS1 | 121.4656583865 | 31.1446308775 | 68 | 504990 | -80.31 | 12.63 | 389.92 | 0.05 | 2.91 | 1592 |
| 2024-09-20 22:21:32.542 | MS1 | 121.4656631856 | 31.1446250405 | 68 | 504990 | -80.54 | 15.81 | 567.08 | 0.19 | 2.40 | 1594 |
| 2024-09-20 22:21:33.720 | MS1 | 121.4656771078 | 31.1446366299 | 68 | 504990 | -79.03 | 16.98 | 413.89 | 0.07 | 2.13 | 1600 |
| 2024-09-20 22:21:34.608 | MS1 | 121.4656731046 | 31.1446241883 | 68 | 504990 | -91.96 | -2.65 | 55.50 | 0.08 | 1.14 | 1587 |
| 2024-09-20 22:21:35.205 | MS1 | 121.4656638013 | 31.1446213766 | 68 | 504990 | -84.58 | -3.89 | 42.68 | 0.04 | 1.26 | 1600 |
| 2024-09-20 22:21:36.788 | MS1 | 121.4656737662 | 31.1446286581 | 68 | 504990 | -91.71 | -0.65 | 55.57 | 0.13 | 1.49 | 1594 |
| 2024-09-20 22:21:37.102 | MS1 | 121.4656623196 | 31.1446273772 | 68 | 504990 | -92.39 | -3.68 | 71.28 | 0.03 | 1.26 | 1599 |
| 2024-09-20 22:21:38.637 | MS1 | 121.4656597234 | 31.1446260780 | 68 | 504990 | -90.72 | -0.81 | 57.44 | 0.14 | 1.47 | 1586 |
| 2024-09-20 22:21:39.938 | MS1 | 121.4656665560 | 31.1446224005 | 937 | 504990 | -78.90 | 13.95 | 302.63 | 0.14 | 1.46 | 1586 |
| 2024-09-20 22:21:40.164 | MS1 | 121.4656646738 | 31.1446355807 | 937 | 504990 | -80.92 | 16.05 | 573.87 | 0.09 | 2.46 | 1580 |
| 2024-09-20 22:21:41.667 | MS1 | 121.4656755421 | 31.1446364965 | 937 | 504990 | -76.41 | 17.02 | 567.21 | 0.11 | 2.26 | 1583 |
| 2024-09-20 22:21:42.746 | MS1 | 121.4656602007 | 31.1446247201 | 937 | 504990 | -75.83 | 16.98 | 431.57 | 0.12 | 2.74 | 1585 |

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
| 3216129 | 3 | 121.4676964495 | 31.1527389667 | 359 | 3 | 6 | 46.5 | TDD | 68 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3245623 | 2 | 121.4755631034 | 31.1462544282 | 359 | 7 | 0 | 21.5 | TDD | 913 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3270303 | 4 | 121.4717342848 | 31.1548290039 | 26 | 14 | 9 | 40.7 | TDD | 799 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3279387 | 1 | 121.4693291484 | 31.1455526871 | 313 | 2 | 10 | 34.2 | TDD | 937 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.575 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.599 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.733 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.733 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.452 | NREventA3 | measId:2;ServCellPCI:372;Se... |
| 2024-09-20 22:21:38.692 | NRHandoverAttempt | SourcePCI:372;SourceNR-ARFC... |
| 2024-09-20 22:21:38.726 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.737 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.859 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.859 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279387 | 1 | 16.1394 | 10.9926 | -114.6719 | 5.7198 | 154.8681 | 0.0099 | 0.0112 |
| 2024_09_20 22:00 | 3245623 | 2 | 12.1657 | 15.2667 | -114.4096 | 13.5917 | 173.2858 | 0.0000 | 0.0108 |
| 2024_09_20 22:00 | 3216129 | 3 | 8.1703 | 15.3847 | -114.2100 | 13.2716 | 159.0963 | 0.0072 | 0.1796 |
| 2024_09_20 22:00 | 3270303 | 4 | 14.4184 | 13.1658 | -114.5154 | 10.7374 | 118.4603 | 0.0130 | 0.0020 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413286_9E7E004A | 504990 | 68 | -91.0 | 504990 | 937 | -86.7 | 504990 | 799 | -93.8 | 504990 | 913 |
| MR_1774413286_B61295F7 | 504990 | 68 | -92.3 | 504990 | 937 | -86.7 | 504990 | 799 | -93.8 | 504990 | 913 |
| MR_1774413286_AB357E70 | 504990 | 937 | -84.7 | 504990 | 68 | -90.1 | 504990 | 799 | -92.5 | 504990 | 913 |
| MR_1774413286_79AE493F | 504990 | 68 | -90.2 | 504990 | 937 | -87.1 | 504990 | 799 | -93.5 | 504990 | 913 |
| MR_1774413286_AE4AD3DA | 504990 | 68 | -90.9 | 504990 | 937 | -85.0 | 504990 | 799 | -93.4 | 504990 | 913 |
| MR_1774413286_FA756B52 | 504990 | 68 | -93.1 | 504990 | 937 | -86.7 | 504990 | 799 | -90.7 | 504990 | 913 |
| MR_1774413286_5A39F57A | 504990 | 937 | -87.8 | 504990 | 68 | -91.5 | 504990 | 799 | -92.3 | 504990 | 913 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1698: `b0899b25-630...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b0899b25-6308-498f-a189-5404bb4d433b` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Lift the tilt angle  of 3275847_3 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1698] topology](images/train_1698.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3275847_3 and 3244176_1
- `C2`: Lift the tilt angle  of 3275847_3 by 7 degrees **← 정답**
- `C3`: Press down the tilt angle of 3216248_2 by 4 degrees
- `C4`: Adjust the azimuth of 3275847_3 by 17 degrees
- `C5`: Press down the tilt angle  of 3275847_3 by 7 degrees
- `C6`: Increase transmission power for 3216248_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Adjust the azimuth of 3216248_2 by 38 degrees
- `C9`: Increase transmission power for 3244176_1
- `C10`: Increase A3 Offset threshold for 3216248_2
- `C11`: Check test server and transmission issues
- `C12`: Lift the tilt angle of 3216248_2 by 4 degrees
- `C13`: Decrease A3 Offset threshold for 3244176_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216248_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216248_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244176_1
- `C17`: Add neighbor relationship between 3216248_2 and 3244176_1
- `C18`: Decrease transmission power for 3244176_1
- `C19`: Decrease A3 Offset threshold for 3216248_2
- `C20`: Increase A3 Offset threshold for 3244176_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244176_1
- `C22`: Decrease transmission power for 3216248_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.316 | MS1 | 121.4656645961 | 31.1446235990 | 193 | 504990 | -87.58 | 17.66 | 432.06 | 0.18 | 2.09 | 1584 |
| 2024-09-20 22:21:32.375 | MS1 | 121.4656733307 | 31.1446369011 | 193 | 504990 | -90.95 | 17.91 | 566.62 | 0.12 | 2.15 | 1593 |
| 2024-09-20 22:21:33.885 | MS1 | 121.4656712451 | 31.1446233080 | 193 | 504990 | -91.81 | 17.90 | 411.28 | 0.12 | 2.24 | 1594 |
| 2024-09-20 22:21:34.630 | MS1 | 121.4656660861 | 31.1446342918 | 193 | 504990 | -86.67 | 14.00 | 85.50 | 0.20 | 2.13 | 1571 |
| 2024-09-20 22:21:35.588 | MS1 | 121.4656686905 | 31.1446249471 | 193 | 504990 | -91.97 | 15.97 | 62.45 | 0.20 | 2.64 | 1592 |
| 2024-09-20 22:21:36.641 | MS1 | 121.4656723150 | 31.1446185748 | 193 | 504990 | -86.36 | 17.51 | 99.44 | 0.19 | 2.64 | 1591 |
| 2024-09-20 22:21:37.842 | MS1 | 121.4656688367 | 31.1446372928 | 193 | 504990 | -92.86 | 12.22 | 55.58 | 0.06 | 2.06 | 1577 |
| 2024-09-20 22:21:38.805 | MS1 | 121.4656607324 | 31.1446198075 | 193 | 504990 | -93.19 | 8.54 | 91.68 | 0.04 | 2.31 | 1575 |
| 2024-09-20 22:21:39.999 | MS1 | 121.4656599208 | 31.1446324344 | 193 | 504990 | -93.19 | 12.22 | 82.73 | 0.03 | 2.86 | 1567 |
| 2024-09-20 22:21:40.849 | MS1 | 121.4656713873 | 31.1446268792 | 193 | 504990 | -91.70 | 11.25 | 479.82 | 0.17 | 2.30 | 1570 |
| 2024-09-20 22:21:41.129 | MS1 | 121.4656729745 | 31.1446281281 | 193 | 504990 | -92.84 | 12.75 | 388.67 | 0.11 | 2.39 | 1585 |
| 2024-09-20 22:21:42.887 | MS1 | 121.4656623513 | 31.1446356769 | 193 | 504990 | -91.86 | 9.08 | 396.49 | 0.03 | 2.69 | 1563 |

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
| 3216248 | 2 | 121.4643518479 | 31.1529540755 | 210 | 2 | 8 | 40.3 | TDD | 193 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3244176 | 1 | 121.4749320524 | 31.1447155557 | 286 | 6 | 0 | 15.4 | TDD | 240 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3253207 | 4 | 121.4696532464 | 31.1509474478 | 292 | 1 | 10 | 25.1 | TDD | 49 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3275847 | 3 | 121.4681819747 | 31.1444418761 | 20 | 0 | 5 | 24.4 | TDD | 634 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.611 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.611 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.283 | NREventA3 | measId:2;ServCellPCI:623;Se... |
| 2024-09-20 22:21:38.523 | NRHandoverAttempt | SourcePCI:623;SourceNR-ARFC... |
| 2024-09-20 22:21:38.570 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.580 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.681 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.681 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244176 | 1 | 11.4650 | 18.8105 | -116.6869 | 9.5530 | 164.9878 | 0.0002 | 0.0183 |
| 2024_09_20 22:00 | 3216248 | 2 | 85.8748 | 90.9280 | -116.5227 | 14.4554 | 139.7056 | 0.0125 | 0.0062 |
| 2024_09_20 22:00 | 3275847 | 3 | 19.1461 | 13.4396 | -116.0449 | 13.5724 | 166.2609 | 0.0011 | 0.0041 |
| 2024_09_20 22:00 | 3253207 | 4 | 17.3895 | 9.7560 | -114.4817 | 19.1295 | 168.1539 | 0.0198 | 0.0166 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412333_DB8B0135 | 504990 | 193 | -85.5 | 504990 | 240 | -97.3 | 504990 | 634 | -96.1 | 504990 | 49 |
| MR_1774412333_E98D7CC5 | 504990 | 193 | -88.4 | 504990 | 240 | -95.4 | 504990 | 634 | -95.5 | 504990 | 49 |
| MR_1774412333_28B4222B | 504990 | 193 | -85.7 | 504990 | 240 | -94.8 | 504990 | 634 | -99.0 | 504990 | 49 |
| MR_1774412333_96F5D086 | 504990 | 193 | -85.3 | 504990 | 240 | -95.1 | 504990 | 634 | -95.3 | 504990 | 49 |
| MR_1774412333_CA8E830D | 504990 | 193 | -86.3 | 504990 | 240 | -93.9 | 504990 | 634 | -98.3 | 504990 | 49 |
| MR_1774412333_B39224B4 | 504990 | 193 | -87.4 | 504990 | 240 | -96.2 | 504990 | 634 | -98.0 | 504990 | 49 |
| MR_1774412333_C841D345 | 504990 | 193 | -87.6 | 504990 | 240 | -94.2 | 504990 | 634 | -98.7 | 504990 | 49 |
| MR_1774412333_6C16BAEC | 504990 | 193 | -87.9 | 504990 | 240 | -95.6 | 504990 | 634 | -95.4 | 504990 | 49 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1699: `1726e0f0-8ad...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1726e0f0-8adb-46b5-8ef9-e934c635272d` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Add neighbor relationship between 3267691_1 and 3221258_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1699] topology](images/train_1699.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3267691_1
- `C2`: Press down the tilt angle  of 3221258_3 by 3 degrees
- `C3`: Add neighbor relationship between 3267691_1 and 3221258_3 **← 정답**
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267691_1
- `C6`: Decrease transmission power for 3221258_3
- `C7`: Decrease A3 Offset threshold for 3267691_1
- `C8`: Increase transmission power for 3221258_3
- `C9`: Press down the tilt angle of 3267691_1 by 10 degrees
- `C10`: Adjust the azimuth of 3221258_3 by 34 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221258_3
- `C12`: Increase A3 Offset threshold for 3221258_3
- `C13`: Decrease A3 Offset threshold for 3221258_3
- `C14`: Increase transmission power for 3267691_1
- `C15`: Adjust the azimuth of 3267691_1 by 50 degrees
- `C16`: Increase A3 Offset threshold for 3267691_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221258_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267691_1
- `C19`: Add neighbor relationship between 3234177_4 and 3221258_3
- `C20`: Lift the tilt angle  of 3221258_3 by 3 degrees
- `C21`: Check test server and transmission issues
- `C22`: Lift the tilt angle of 3267691_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.816 | MS1 | 121.4656774288 | 31.1446293825 | 644 | 504990 | -81.31 | 17.21 | 563.44 | 0.09 | 2.54 | 1600 |
| 2024-09-20 22:21:32.531 | MS1 | 121.4656594985 | 31.1446220039 | 644 | 504990 | -84.97 | 17.51 | 551.59 | 0.06 | 2.21 | 1583 |
| 2024-09-20 22:21:33.483 | MS1 | 121.4656588796 | 31.1446275147 | 644 | 504990 | -81.83 | 13.12 | 581.74 | 0.12 | 2.64 | 1584 |
| 2024-09-20 22:21:34.291 | MS1 | 121.4656779659 | 31.1446368581 | 644 | 504990 | -91.25 | -0.32 | 23.24 | 0.16 | 1.29 | 1564 |
| 2024-09-20 22:21:35.786 | MS1 | 121.4656583671 | 31.1446374895 | 644 | 504990 | -94.72 | -1.32 | 64.36 | 0.15 | 1.32 | 1585 |
| 2024-09-20 22:21:36.138 | MS1 | 121.4656647885 | 31.1446333559 | 644 | 504990 | -93.23 | -3.37 | 58.44 | 0.05 | 1.40 | 1572 |
| 2024-09-20 22:21:37.786 | MS1 | 121.4656685209 | 31.1446184563 | 644 | 504990 | -90.61 | -0.56 | 66.29 | 0.05 | 1.34 | 1564 |
| 2024-09-20 22:21:38.596 | MS1 | 121.4656653165 | 31.1446305881 | 644 | 504990 | -76.36 | 16.34 | 463.41 | 0.04 | 1.02 | 1571 |
| 2024-09-20 22:21:39.469 | MS1 | 121.4656718742 | 31.1446255600 | 644 | 504990 | -78.52 | 12.52 | 354.90 | 0.05 | 1.11 | 1561 |
| 2024-09-20 22:21:40.702 | MS1 | 121.4656775148 | 31.1446345411 | 644 | 504990 | -76.24 | 13.55 | 443.25 | 0.13 | 2.36 | 1575 |
| 2024-09-20 22:21:41.301 | MS1 | 121.4656717135 | 31.1446331709 | 644 | 504990 | -82.57 | 15.24 | 440.99 | 0.20 | 2.74 | 1577 |
| 2024-09-20 22:21:42.236 | MS1 | 121.4656611786 | 31.1446235230 | 644 | 504990 | -82.55 | 17.34 | 523.96 | 0.08 | 2.15 | 1580 |

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
| 3221258 | 3 | 121.4731122094 | 31.1524476595 | 185 | 2 | 4 | 16.7 | TDD | 327 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3234177 | 4 | 121.4666452310 | 31.1516722338 | 225 | 15 | 8 | 26.3 | TDD | 799 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3267691 | 1 | 121.4652488433 | 31.1472859809 | 256 | 8 | 8 | 49.5 | TDD | 644 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3276887 | 2 | 121.4745979410 | 31.1479348948 | 52 | 15 | 6 | 29.8 | TDD | 869 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.113 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.248 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.248 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.915 | NREventA3 | measId:2;ServCellPCI:968;Se... |
| 2024-09-20 22:21:35.915 | NREventA3 | measId:2;ServCellPCI:968;Se... |
| 2024-09-20 22:21:36.915 | NREventA3 | measId:2;ServCellPCI:968;Se... |
| 2024-09-20 22:21:39.415 | NRRRCReestablishAttempt | PCI:968 |
| 2024-09-20 22:21:39.425 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.437 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.570 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.570 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267691 | 1 | 11.7069 | 7.5108 | -117.8263 | 18.5660 | 118.2186 | 0.0154 | 0.1282 |
| 2024_09_20 22:00 | 3276887 | 2 | 8.8041 | 11.7153 | -115.4904 | 9.9025 | 176.6858 | 0.0123 | 0.0085 |
| 2024_09_20 22:00 | 3221258 | 3 | 8.8226 | 6.3730 | -116.4173 | 6.1358 | 146.4465 | 0.0168 | 0.0094 |
| 2024_09_20 22:00 | 3234177 | 4 | 10.6931 | 19.7113 | -114.0395 | 19.8735 | 140.9065 | 0.0148 | 0.0009 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416708_1D47CBE5 | 504990 | 327 | -87.3 | 504990 | 644 | -92.1 | 504990 | 799 | -90.2 | 504990 | 869 |
| MR_1774416708_B78C938D | 504990 | 644 | -89.3 | 504990 | 327 | -88.8 | 504990 | 799 | -92.5 | 504990 | 869 |
| MR_1774416708_6899D257 | 504990 | 644 | -89.8 | 504990 | 327 | -88.1 | 504990 | 799 | -89.8 | 504990 | 869 |
| MR_1774416708_10E958AA | 504990 | 644 | -90.5 | 504990 | 327 | -86.9 | 504990 | 799 | -91.9 | 504990 | 869 |
| MR_1774416708_ED387D00 | 504990 | 644 | -91.0 | 504990 | 327 | -87.5 | 504990 | 799 | -89.8 | 504990 | 869 |
| MR_1774416708_C946195B | 504990 | 644 | -92.6 | 504990 | 327 | -87.1 | 504990 | 799 | -91.0 | 504990 | 869 |

> *... 2개 열 생략 (전체 14열)*

---
