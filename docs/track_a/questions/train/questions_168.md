# Track A 문제 분석 — train[1670]~train[1679]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1670] ~ train[1679] (10개)

## 목차

1. [문제 1670: `fcf7ac22-5ab...`](#1670) — single-answer, 정답: C2
2. [문제 1671: `34bf8364-372...`](#1671) — single-answer, 정답: C11
3. [문제 1672: `af476619-0fb...`](#1672) — multiple-answer, 정답: C16|C20
4. [문제 1673: `26641e02-b6b...`](#1673) — single-answer, 정답: C10
5. [문제 1674: `7e25aa91-c7a...`](#1674) — single-answer, 정답: C1
6. [문제 1675: `48182b0e-e45...`](#1675) — single-answer, 정답: C17
7. [문제 1676: `1612e90d-939...`](#1676) — single-answer, 정답: C22
8. [문제 1677: `2e6654db-4a9...`](#1677) — multiple-answer, 정답: C1|C7
9. [문제 1678: `e5d86b15-2d5...`](#1678) — single-answer, 정답: C2
10. [문제 1679: `5553042a-5a3...`](#1679) — multiple-answer, 정답: C1|C19

---

### 문제 1670: `fcf7ac22-5ab...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fcf7ac22-5ab1-4d74-a231-52cb4c743384` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Add neighbor relationship between 3239473_1 and 3210489_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1670] topology](images/train_1670.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3210489_4 by 6 degrees
- `C2`: Add neighbor relationship between 3239473_1 and 3210489_4 **← 정답**
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Add neighbor relationship between 3240106_3 and 3210489_4
- `C5`: Decrease transmission power for 3210489_4
- `C6`: Press down the tilt angle  of 3210489_4 by 6 degrees
- `C7`: Decrease A3 Offset threshold for 3239473_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210489_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239473_1
- `C10`: Press down the tilt angle of 3239473_1 by 10 degrees
- `C11`: Increase A3 Offset threshold for 3210489_4
- `C12`: Lift the tilt angle of 3239473_1 by 10 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210489_4
- `C14`: Adjust the azimuth of 3239473_1 by 50 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239473_1
- `C16`: Decrease A3 Offset threshold for 3210489_4
- `C17`: Decrease transmission power for 3239473_1
- `C18`: Increase transmission power for 3210489_4
- `C19`: Increase A3 Offset threshold for 3239473_1
- `C20`: Adjust the azimuth of 3210489_4 by 10 degrees
- `C21`: Check test server and transmission issues
- `C22`: Increase transmission power for 3239473_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.290 | MS1 | 121.4656582430 | 31.1446275649 | 737 | 504990 | -83.40 | 16.64 | 491.64 | 0.19 | 2.89 | 1595 |
| 2024-09-20 22:21:32.660 | MS1 | 121.4656684733 | 31.1446310794 | 737 | 504990 | -82.36 | 15.27 | 598.58 | 0.10 | 2.36 | 1573 |
| 2024-09-20 22:21:33.467 | MS1 | 121.4656625510 | 31.1446375216 | 737 | 504990 | -81.83 | 12.15 | 335.38 | 0.16 | 2.40 | 1598 |
| 2024-09-20 22:21:34.608 | MS1 | 121.4656725446 | 31.1446238566 | 737 | 504990 | -86.04 | -0.98 | 58.08 | 0.00 | 1.47 | 1584 |
| 2024-09-20 22:21:35.488 | MS1 | 121.4656728927 | 31.1446203706 | 737 | 504990 | -93.90 | -3.36 | 30.07 | 0.18 | 1.30 | 1592 |
| 2024-09-20 22:21:36.114 | MS1 | 121.4656621880 | 31.1446286892 | 737 | 504990 | -90.47 | -2.71 | 57.78 | 0.16 | 1.15 | 1564 |
| 2024-09-20 22:21:37.320 | MS1 | 121.4656586819 | 31.1446326347 | 737 | 504990 | -88.02 | -1.60 | 63.26 | 0.09 | 1.03 | 1560 |
| 2024-09-20 22:21:38.873 | MS1 | 121.4656619958 | 31.1446191262 | 737 | 504990 | -84.88 | 16.81 | 571.71 | 0.18 | 1.19 | 1572 |
| 2024-09-20 22:21:39.612 | MS1 | 121.4656757133 | 31.1446312974 | 737 | 504990 | -76.58 | 15.52 | 408.18 | 0.04 | 1.34 | 1585 |
| 2024-09-20 22:21:40.158 | MS1 | 121.4656735795 | 31.1446249532 | 737 | 504990 | -79.31 | 14.08 | 416.58 | 0.17 | 2.04 | 1560 |
| 2024-09-20 22:21:41.873 | MS1 | 121.4656689112 | 31.1446338715 | 737 | 504990 | -76.03 | 12.67 | 428.19 | 0.20 | 2.43 | 1596 |
| 2024-09-20 22:21:42.905 | MS1 | 121.4656779553 | 31.1446267992 | 737 | 504990 | -79.46 | 12.21 | 564.82 | 0.01 | 2.86 | 1588 |

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
| 3210489 | 4 | 121.4643149197 | 31.1550188201 | 184 | 4 | 12 | 38.8 | TDD | 215 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3239473 | 1 | 121.4669188629 | 31.1480933214 | 101 | 12 | 2 | 36.7 | TDD | 737 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3240106 | 3 | 121.4662615295 | 31.1542900783 | 299 | 6 | 3 | 34.0 | TDD | 973 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3275770 | 2 | 121.4744856315 | 31.1554949348 | 105 | 6 | 0 | 45.2 | TDD | 122 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.872 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.889 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.994 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.994 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.674 | NREventA3 | measId:2;ServCellPCI:996;Se... |
| 2024-09-20 22:21:35.674 | NREventA3 | measId:2;ServCellPCI:996;Se... |
| 2024-09-20 22:21:36.674 | NREventA3 | measId:2;ServCellPCI:996;Se... |
| 2024-09-20 22:21:39.174 | NRRRCReestablishAttempt | PCI:996 |
| 2024-09-20 22:21:39.193 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.203 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.349 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.349 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239473 | 1 | 18.3390 | 6.0907 | -114.7475 | 7.9598 | 117.4405 | 0.0031 | 0.1710 |
| 2024_09_20 22:00 | 3275770 | 2 | 8.7216 | 19.6663 | -117.4866 | 8.1826 | 182.0397 | 0.0082 | 0.0054 |
| 2024_09_20 22:00 | 3240106 | 3 | 10.7790 | 14.1116 | -117.8520 | 16.9692 | 187.1846 | 0.0178 | 0.0128 |
| 2024_09_20 22:00 | 3210489 | 4 | 14.1651 | 15.0440 | -117.5741 | 12.2152 | 164.1982 | 0.0167 | 0.0019 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412735_0C6C0A7A | 504990 | 737 | -85.8 | 504990 | 215 | -81.5 | 504990 | 973 | -85.1 | 504990 | 122 |
| MR_1774412735_1A148414 | 504990 | 737 | -84.4 | 504990 | 215 | -82.2 | 504990 | 973 | -83.3 | 504990 | 122 |
| MR_1774412735_021936E8 | 504990 | 215 | -82.9 | 504990 | 737 | -87.3 | 504990 | 973 | -83.3 | 504990 | 122 |
| MR_1774412735_6EEABA86 | 504990 | 737 | -84.3 | 504990 | 215 | -80.0 | 504990 | 973 | -86.2 | 504990 | 122 |
| MR_1774412735_2AF983B8 | 504990 | 737 | -85.9 | 504990 | 215 | -81.1 | 504990 | 973 | -82.6 | 504990 | 122 |
| MR_1774412735_07C0C23E | 504990 | 737 | -87.7 | 504990 | 215 | -81.3 | 504990 | 973 | -84.2 | 504990 | 122 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1671: `34bf8364-372...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `34bf8364-3721-483a-a53d-b9c7ddf14bd2` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264711_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1671] topology](images/train_1671.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3278740_5
- `C2`: Press down the tilt angle  of 3278740_5 by 4 degrees
- `C3`: Press down the tilt angle of 3264711_1 by 4 degrees
- `C4`: Lift the tilt angle  of 3278740_5 by 4 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264711_1
- `C6`: Check test server and transmission issues
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278740_5
- `C8`: Lift the tilt angle of 3264711_1 by 4 degrees
- `C9`: Add neighbor relationship between 3264711_1 and 3278740_5
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264711_1 **← 정답**
- `C12`: Decrease transmission power for 3264711_1
- `C13`: Increase transmission power for 3264711_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278740_5
- `C15`: Increase transmission power for 3278740_5
- `C16`: Increase A3 Offset threshold for 3264711_1
- `C17`: Add neighbor relationship between 3239727_11 and 3278740_5
- `C18`: Decrease A3 Offset threshold for 3278740_5
- `C19`: Increase A3 Offset threshold for 3278740_5
- `C20`: Adjust the azimuth of 3278740_5 by 31 degrees
- `C21`: Adjust the azimuth of 3264711_1 by 20 degrees
- `C22`: Decrease A3 Offset threshold for 3264711_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.712 | MS1 | 121.4656711576 | 31.1446236198 | 899 | 504990 | -95.08 | 10.76 | 430.87 | 0.17 | 2.09 | 1573 |
| 2024-09-20 22:21:32.189 | MS1 | 121.4656721991 | 31.1446266869 | 478 | 504990 | -95.59 | 11.13 | 569.69 | 0.17 | 2.70 | 1572 |
| 2024-09-20 22:21:33.333 | MS1 | 121.4656694556 | 31.1446290424 | 372 | 504990 | -93.49 | 9.80 | 356.57 | 0.07 | 2.78 | 1585 |
| 2024-09-20 22:21:34.348 | MS1 | 121.4656600650 | 31.1446281818 | 667 | 152650 | -87.94 | 3.22 | 107.11 | 0.01 | 1.73 | 991 |
| 2024-09-20 22:21:35.223 | MS1 | 121.4656753565 | 31.1446253075 | 235 | 152650 | -94.67 | 4.99 | 55.72 | 0.07 | 2.00 | 990 |
| 2024-09-20 22:21:36.994 | MS1 | 121.4656598280 | 31.1446276756 | 889 | 152650 | -93.74 | 2.77 | 86.44 | 0.19 | 1.64 | 902 |
| 2024-09-20 22:21:37.907 | MS1 | 121.4656656511 | 31.1446276597 | 378 | 152650 | -91.93 | 7.50 | 70.75 | 0.07 | 1.82 | 939 |
| 2024-09-20 22:21:38.928 | MS1 | 121.4656629988 | 31.1446238702 | 667 | 152650 | -87.29 | 6.47 | 68.03 | 0.03 | 1.59 | 907 |
| 2024-09-20 22:21:39.113 | MS1 | 121.4656580855 | 31.1446361444 | 235 | 152650 | -90.87 | 2.27 | 78.06 | 0.18 | 1.54 | 953 |
| 2024-09-20 22:21:40.232 | MS1 | 121.4656684178 | 31.1446370710 | 889 | 152650 | -92.08 | 6.22 | 91.71 | 0.12 | 2.37 | 1586 |
| 2024-09-20 22:21:41.285 | MS1 | 121.4656739933 | 31.1446279076 | 378 | 152650 | -93.64 | 4.94 | 61.89 | 0.16 | 2.05 | 1565 |
| 2024-09-20 22:21:42.203 | MS1 | 121.4656611945 | 31.1446247246 | 667 | 152650 | -91.46 | 6.92 | 54.00 | 0.04 | 2.94 | 1585 |

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
| 3220933 | 10 | 121.4707409386 | 31.1558567165 | 7 | 14 | 6 | 16.7 | FDD | 180 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3223561 | 7 | 121.4727444020 | 31.1476373989 | 35 | 4 | 6 | 24.9 | FDD | 288 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3227143 | 2 | 121.4667527044 | 31.1554776223 | 7 | 7 | 6 | 6.5 | TDD | 205 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3231549 | 6 | 121.4752447929 | 31.1554424952 | 148 | 11 | 0 | 25.2 | TDD | 478 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3239727 | 11 | 121.4752662858 | 31.1478756145 | 322 | 15 | 9 | 18.6 | FDD | 889 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3262280 | 8 | 121.4645853575 | 31.1533756210 | 272 | 6 | 0 | 3.6 | FDD | 969 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3264711 | 1 | 121.4667209878 | 31.1483394713 | 174 | 1 | 12 | 20.8 | TDD | 899 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3266603 | 13 | 121.4685049870 | 31.1501170462 | 52 | 9 | 10 | 0.8 | FDD | 667 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3268378 | 3 | 121.4731059062 | 31.1515437007 | 172 | 10 | 3 | 20.7 | TDD | 115 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3274964 | 9 | 121.4713746746 | 31.1525227024 | 282 | 8 | 9 | 3.6 | FDD | 235 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3276547 | 4 | 121.4712050211 | 31.1511240790 | 32 | 12 | 6 | 4.1 | TDD | 372 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3278740 | 5 | 121.4747200599 | 31.1493012273 | 208 | 3 | 4 | 9.1 | TDD | 573 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3279560 | 12 | 121.4686567012 | 31.1454753361 | 80 | 0 | 8 | 29.7 | FDD | 378 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |

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
| 2024-09-20 22:21:31.479 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.504 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.652 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.652 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.348 | NREventA2 | measId:1;ServCellPCI:350;Se... |
| 2024-09-20 22:21:35.451 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.687 | NREventA5 | measId:3;ServCellPCI:350;Se... |
| 2024-09-20 22:21:35.726 | NRHandoverAttempt | SourcePCI:350;SourceNR-ARFC... |
| 2024-09-20 22:21:35.769 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.780 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.892 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.892 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264711 | 1 | 11.9411 | 5.5985 | -115.7739 | 9.5871 | 196.7183 | 0.0188 | 0.0096 |
| 2024_09_20 22:00 | 3227143 | 2 | 16.0272 | 15.6991 | -117.4681 | 11.1025 | 83.2219 | 0.0038 | 0.0084 |
| 2024_09_20 22:00 | 3268378 | 3 | 12.4537 | 15.1156 | -117.1350 | 10.5536 | 130.7504 | 0.0115 | 0.0180 |
| 2024_09_20 22:00 | 3276547 | 4 | 14.0683 | 16.3700 | -116.6641 | 5.0241 | 150.6057 | 0.0138 | 0.0178 |
| 2024_09_20 22:00 | 3278740 | 5 | 7.7775 | 5.3599 | -116.0539 | 6.4460 | 179.8941 | 0.0172 | 0.0009 |
| 2024_09_20 22:00 | 3231549 | 6 | 12.4814 | 8.2179 | -117.7744 | 7.2216 | 140.5504 | 0.0050 | 0.0054 |
| 2024_09_20 22:00 | 3223561 | 7 | 15.2002 | 13.2742 | -116.5501 | 4.4441 | 53.3599 | 0.0121 | 0.0025 |
| 2024_09_20 22:00 | 3262280 | 8 | 11.9085 | 6.7180 | -116.1444 | 4.7127 | 48.0720 | 0.0016 | 0.0049 |
| 2024_09_20 22:00 | 3274964 | 9 | 7.6576 | 16.4341 | -115.3052 | 4.4590 | 54.3219 | 0.0078 | 0.0019 |
| 2024_09_20 22:00 | 3220933 | 10 | 12.8056 | 15.1982 | -114.2440 | 3.7921 | 24.9616 | 0.0028 | 0.0104 |
| 2024_09_20 22:00 | 3239727 | 11 | 12.3359 | 16.4268 | -116.2306 | 4.0765 | 21.1612 | 0.0151 | 0.0042 |
| 2024_09_20 22:00 | 3279560 | 12 | 8.1723 | 18.4843 | -115.9983 | 4.0026 | 50.5891 | 0.0056 | 0.0106 |
| 2024_09_20 22:00 | 3266603 | 13 | 5.8745 | 11.9740 | -116.4718 | 3.1058 | 38.5898 | 0.0059 | 0.0136 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414179_6DD45402 | 152650 | 235 | -93.7 | 152650 | 288 | -102.5 | 152650 | 969 | -103.9 | 152650 | 180 |
| MR_1774414179_EE5C149B | 504990 | 372 | -95.4 | 504990 | 573 | -94.0 | 504990 | 205 | -97.3 | 504990 | 115 |
| MR_1774414179_92A2A352 | 152650 | 235 | -93.4 | 152650 | 288 | -100.7 | 152650 | 969 | -104.4 | 152650 | 180 |
| MR_1774414179_01F3703A | 504990 | 372 | -95.0 | 504990 | 573 | -94.8 | 504990 | 205 | -96.4 | 504990 | 115 |
| MR_1774414179_5819773B | 504990 | 372 | -93.4 | 504990 | 573 | -97.4 | 504990 | 205 | -99.9 | 504990 | 115 |
| MR_1774414179_E78C9369 | 504990 | 372 | -93.7 | 504990 | 573 | -96.9 | 504990 | 205 | -100.2 | 504990 | 115 |
| MR_1774414179_60D7CD4F | 504990 | 372 | -94.3 | 504990 | 573 | -97.3 | 504990 | 205 | -98.1 | 504990 | 115 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1672: `af476619-0fb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `af476619-0fb6-43cf-adb0-e577abfbcd10` |
| Tag | **multiple-answer** |
| 정답 | **C16|C20** |
| C16 의미 | Increase transmission power for 3274194_3 |
| C20 의미 | Adjust the azimuth of 3274194_3 by 47 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1672] topology](images/train_1672.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3247859_4 and 3230920_1
- `C2`: Press down the tilt angle of 3274194_3 by 10 degrees
- `C3`: Press down the tilt angle  of 3230920_1 by 1 degrees
- `C4`: Adjust the azimuth of 3230920_1 by 33 degrees
- `C5`: Increase A3 Offset threshold for 3274194_3
- `C6`: Decrease A3 Offset threshold for 3274194_3
- `C7`: Lift the tilt angle of 3274194_3 by 10 degrees
- `C8`: Add neighbor relationship between 3274194_3 and 3230920_1
- `C9`: Decrease transmission power for 3230920_1
- `C10`: Check test server and transmission issues
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274194_3
- `C13`: Increase A3 Offset threshold for 3230920_1
- `C14`: Increase transmission power for 3230920_1
- `C15`: Decrease A3 Offset threshold for 3230920_1
- `C16`: Increase transmission power for 3274194_3 **← 정답**
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274194_3
- `C18`: Decrease transmission power for 3274194_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230920_1
- `C20`: Adjust the azimuth of 3274194_3 by 47 degrees **← 정답**
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230920_1
- `C22`: Lift the tilt angle  of 3230920_1 by 1 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.386 | MS1 | 121.4656709993 | 31.1446219653 | 710 | 504990 | -87.58 | 12.44 | 441.65 | 0.18 | 2.83 | 1584 |
| 2024-09-20 22:21:32.803 | MS1 | 121.4656619648 | 31.1446269155 | 710 | 504990 | -87.97 | 17.80 | 348.26 | 0.00 | 2.18 | 1576 |
| 2024-09-20 22:21:33.866 | MS1 | 121.4656755393 | 31.1446236482 | 710 | 504990 | -88.31 | 17.77 | 447.44 | 0.10 | 2.19 | 1562 |
| 2024-09-20 22:21:34.859 | MS1 | 121.4656725727 | 31.1446208018 | 710 | 504990 | -107.23 | 0.95 | 49.36 | 0.15 | 1.32 | 1576 |
| 2024-09-20 22:21:35.821 | MS1 | 121.4656683825 | 31.1446238665 | 710 | 504990 | -104.24 | -1.86 | 34.98 | 0.07 | 1.41 | 1589 |
| 2024-09-20 22:21:36.810 | MS1 | 121.4656656357 | 31.1446188728 | 710 | 504990 | -106.86 | -1.18 | 13.17 | 0.09 | 1.09 | 1587 |
| 2024-09-20 22:21:37.322 | MS1 | 121.4656750562 | 31.1446377883 | 710 | 504990 | -102.82 | 0.71 | 25.21 | 0.04 | 1.11 | 1575 |
| 2024-09-20 22:21:38.667 | MS1 | 121.4656695436 | 31.1446246213 | 710 | 504990 | -100.79 | -1.33 | 27.19 | 0.16 | 1.48 | 1585 |
| 2024-09-20 22:21:39.263 | MS1 | 121.4656600396 | 31.1446268359 | 710 | 504990 | -104.28 | 1.60 | 58.89 | 0.08 | 1.20 | 1562 |
| 2024-09-20 22:21:40.687 | MS1 | 121.4656628502 | 31.1446250074 | 710 | 504990 | -93.46 | 15.09 | 411.48 | 0.18 | 2.02 | 1596 |
| 2024-09-20 22:21:41.773 | MS1 | 121.4656746795 | 31.1446367628 | 710 | 504990 | -91.82 | 16.32 | 466.58 | 0.01 | 2.66 | 1579 |
| 2024-09-20 22:21:42.987 | MS1 | 121.4656694146 | 31.1446264867 | 710 | 504990 | -89.34 | 12.59 | 309.54 | 0.12 | 2.87 | 1572 |

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
| 3230920 | 1 | 121.4758791855 | 31.1555351984 | 252 | 0 | 5 | 25.0 | TDD | 314 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3239320 | 2 | 121.4701159582 | 31.1516814527 | 240 | 6 | 1 | 36.4 | TDD | 997 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3247859 | 4 | 121.4745228055 | 31.1455849825 | 191 | 2 | 10 | 39.5 | TDD | 122 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3274194 | 3 | 121.4725419207 | 31.1450554078 | 219 | 7 | 7 | 43.1 | TDD | 710 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.917 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.063 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.063 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.206 | NREventA2 | measId:1;ServCellPCI:481;Se... |
| 2024-09-20 22:21:34.344 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230920 | 1 | 13.1033 | 12.4975 | -116.8271 | 13.7656 | 177.3822 | 0.0167 | 0.0132 |
| 2024_09_20 22:00 | 3239320 | 2 | 11.7391 | 14.2321 | -117.3385 | 18.1904 | 152.0945 | 0.0034 | 0.0156 |
| 2024_09_20 22:00 | 3274194 | 3 | 14.6993 | 16.1097 | -114.4854 | 6.4943 | 91.8134 | 0.1023 | 0.0018 |
| 2024_09_20 22:00 | 3247859 | 4 | 10.1883 | 12.0030 | -115.1782 | 11.3715 | 87.0378 | 0.0112 | 0.0037 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417074_25C8E70E | 504990 | 710 | -105.7 | 504990 | 314 | -113.9 | 504990 | 122 | -120.5 | 504990 | 997 |
| MR_1774417074_EF578D0F | 504990 | 710 | -106.9 | 504990 | 314 | -115.1 | 504990 | 122 | -121.7 | 504990 | 997 |
| MR_1774417074_1320100F | 504990 | 710 | -106.3 | 504990 | 314 | -112.8 | 504990 | 122 | -120.6 | 504990 | 997 |
| MR_1774417074_59B4A49A | 504990 | 710 | -105.6 | 504990 | 314 | -112.1 | 504990 | 122 | -120.7 | 504990 | 997 |
| MR_1774417074_1388951F | 504990 | 710 | -107.9 | 504990 | 314 | -113.3 | 504990 | 122 | -120.5 | 504990 | 997 |
| MR_1774417074_53955AD8 | 504990 | 710 | -106.1 | 504990 | 314 | -113.2 | 504990 | 122 | -118.5 | 504990 | 997 |
| MR_1774417074_019825B7 | 504990 | 710 | -106.0 | 504990 | 314 | -113.4 | 504990 | 122 | -118.9 | 504990 | 997 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1673: `26641e02-b6b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `26641e02-b6b2-4bbb-9670-9b3ce8b457db` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1673] topology](images/train_1673.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3241761_4 and 3219195_1
- `C2`: Adjust the azimuth of 3241761_4 by 50 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219195_1
- `C4`: Increase A3 Offset threshold for 3241761_4
- `C5`: Decrease transmission power for 3219195_1
- `C6`: Decrease A3 Offset threshold for 3219195_1
- `C7`: Decrease A3 Offset threshold for 3241761_4
- `C8`: Increase transmission power for 3219195_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219195_1
- `C10`: Insufficient data; more data is needed for judgment. **← 정답**
- `C11`: Press down the tilt angle  of 3219195_1 by 2 degrees
- `C12`: Lift the tilt angle  of 3219195_1 by 2 degrees
- `C13`: Check test server and transmission issues
- `C14`: Decrease transmission power for 3241761_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241761_4
- `C16`: Add neighbor relationship between 3215332_3 and 3219195_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241761_4
- `C18`: Increase A3 Offset threshold for 3219195_1
- `C19`: Adjust the azimuth of 3219195_1 by 38 degrees
- `C20`: Press down the tilt angle of 3241761_4 by 7 degrees
- `C21`: Increase transmission power for 3241761_4
- `C22`: Lift the tilt angle of 3241761_4 by 7 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.557 | MS1 | 121.4656744943 | 31.1446270868 | 1007 | 504990 | -85.81 | 13.55 | 433.29 | 0.19 | 2.65 | 1573 |
| 2024-09-20 22:21:32.518 | MS1 | 121.4656594387 | 31.1446327290 | 1007 | 504990 | -87.90 | 13.23 | 341.30 | 0.19 | 2.62 | 1579 |
| 2024-09-20 22:21:33.175 | MS1 | 121.4656628515 | 31.1446308003 | 1007 | 504990 | -85.75 | 13.93 | 511.92 | 0.18 | 2.03 | 1571 |
| 2024-09-20 22:21:34.738 | MS1 | 121.4656697776 | 31.1446339170 | 1007 | 504990 | -86.30 | 17.80 | 74.13 | 0.20 | 2.57 | 1564 |
| 2024-09-20 22:21:35.605 | MS1 | 121.4656599045 | 31.1446241729 | 1007 | 504990 | -90.88 | 13.45 | 109.08 | 0.12 | 2.50 | 1580 |
| 2024-09-20 22:21:36.614 | MS1 | 121.4656682398 | 31.1446241797 | 1007 | 504990 | -88.11 | 13.98 | 104.06 | 0.13 | 2.04 | 1596 |
| 2024-09-20 22:21:37.360 | MS1 | 121.4656691104 | 31.1446350349 | 1007 | 504990 | -91.27 | 11.31 | 67.41 | 0.16 | 2.86 | 1574 |
| 2024-09-20 22:21:38.682 | MS1 | 121.4656726065 | 31.1446218066 | 1007 | 504990 | -92.20 | 10.79 | 60.84 | 0.15 | 2.01 | 1572 |
| 2024-09-20 22:21:39.297 | MS1 | 121.4656681343 | 31.1446330093 | 1007 | 504990 | -90.06 | 8.08 | 95.29 | 0.06 | 2.28 | 1598 |
| 2024-09-20 22:21:40.789 | MS1 | 121.4656694149 | 31.1446300344 | 1007 | 504990 | -92.46 | 8.11 | 581.27 | 0.05 | 2.64 | 1594 |
| 2024-09-20 22:21:41.405 | MS1 | 121.4656716844 | 31.1446302215 | 1007 | 504990 | -91.82 | 12.44 | 387.89 | 0.04 | 2.47 | 1592 |
| 2024-09-20 22:21:42.417 | MS1 | 121.4656592894 | 31.1446276476 | 1007 | 504990 | -90.50 | 12.89 | 332.26 | 0.01 | 2.21 | 1591 |

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
| 3215332 | 3 | 121.4709895449 | 31.1550863576 | 124 | 10 | 6 | 17.6 | TDD | 438 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3219195 | 1 | 121.4740286066 | 31.1440469751 | 313 | 0 | 7 | 33.5 | TDD | 497 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3238163 | 2 | 121.4698244426 | 31.1507578970 | 353 | 3 | 3 | 15.7 | TDD | 300 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3241761 | 4 | 121.4680630876 | 31.1540140471 | 349 | 5 | 0 | 33.2 | TDD | 1007 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.509 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.534 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.656 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.656 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.309 | NREventA3 | measId:2;ServCellPCI:936;Se... |
| 2024-09-20 22:21:38.549 | NRHandoverAttempt | SourcePCI:936;SourceNR-ARFC... |
| 2024-09-20 22:21:38.595 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.610 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.713 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.713 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3219195 | 1 | 89.3164 | 78.9398 | -114.5785 | 11.0376 | 131.3302 | 0.0185 | 0.0108 |
| 2024_09_19 22:00 | 3238163 | 2 | 78.7879 | 94.8891 | -117.3262 | 8.3191 | 133.5111 | 0.0040 | 0.0024 |
| 2024_09_19 22:00 | 3215332 | 3 | 82.8668 | 77.3903 | -114.6150 | 8.0119 | 133.1504 | 0.0137 | 0.0005 |
| 2024_09_19 22:00 | 3241761 | 4 | 89.1409 | 89.1650 | -117.5851 | 18.3663 | 104.4509 | 0.0008 | 0.0113 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416437_12AF6FFD | 504990 | 1007 | -84.3 | 504990 | 497 | -90.8 | 504990 | 438 | -93.9 | 504990 | 300 |
| MR_1774416437_E357ABA5 | 504990 | 1007 | -88.2 | 504990 | 497 | -92.8 | 504990 | 438 | -91.1 | 504990 | 300 |
| MR_1774416437_E2320DC7 | 504990 | 1007 | -88.2 | 504990 | 497 | -91.1 | 504990 | 438 | -94.3 | 504990 | 300 |
| MR_1774416437_4BA885EB | 504990 | 1007 | -85.2 | 504990 | 497 | -90.2 | 504990 | 438 | -91.3 | 504990 | 300 |
| MR_1774416437_03D66BEB | 504990 | 1007 | -85.3 | 504990 | 497 | -91.6 | 504990 | 438 | -93.2 | 504990 | 300 |
| MR_1774416437_E4A6F699 | 504990 | 1007 | -85.4 | 504990 | 497 | -92.4 | 504990 | 438 | -91.2 | 504990 | 300 |
| MR_1774416437_2FA62E44 | 504990 | 1007 | -88.2 | 504990 | 497 | -90.0 | 504990 | 438 | -92.5 | 504990 | 300 |
| MR_1774416437_4F1D5DD4 | 504990 | 1007 | -84.3 | 504990 | 497 | -92.0 | 504990 | 438 | -91.6 | 504990 | 300 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1674: `7e25aa91-c7a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7e25aa91-c7a1-43f3-9f1e-4b8efd9a2f2e` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1674] topology](images/train_1674.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment. **← 정답**
- `C2`: Adjust the azimuth of 3220396_3 by 50 degrees
- `C3`: Increase transmission power for 3226168_2
- `C4`: Increase A3 Offset threshold for 3226168_2
- `C5`: Check test server and transmission issues
- `C6`: Decrease A3 Offset threshold for 3220396_3
- `C7`: Decrease A3 Offset threshold for 3226168_2
- `C8`: Increase A3 Offset threshold for 3220396_3
- `C9`: Press down the tilt angle  of 3226168_2 by 10 degrees
- `C10`: Add neighbor relationship between 3220396_3 and 3226168_2
- `C11`: Adjust the azimuth of 3226168_2 by 50 degrees
- `C12`: Increase transmission power for 3220396_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220396_3
- `C14`: Lift the tilt angle  of 3226168_2 by 10 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226168_2
- `C16`: Lift the tilt angle of 3220396_3 by 2 degrees
- `C17`: Decrease transmission power for 3226168_2
- `C18`: Add neighbor relationship between 3247909_1 and 3226168_2
- `C19`: Decrease transmission power for 3220396_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220396_3
- `C21`: Press down the tilt angle of 3220396_3 by 2 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226168_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.159 | MS1 | 121.4656631910 | 31.1446196620 | 686 | 504990 | -87.08 | 16.01 | 512.23 | 0.12 | 2.02 | 1569 |
| 2024-09-20 22:21:32.568 | MS1 | 121.4656634977 | 31.1446268124 | 686 | 504990 | -87.27 | 12.86 | 360.61 | 0.02 | 2.62 | 1588 |
| 2024-09-20 22:21:33.453 | MS1 | 121.4656755412 | 31.1446314738 | 686 | 504990 | -85.34 | 15.78 | 339.78 | 0.01 | 2.80 | 1578 |
| 2024-09-20 22:21:34.505 | MS1 | 121.4656732407 | 31.1446346213 | 686 | 504990 | -87.24 | 12.25 | 102.06 | 0.03 | 2.25 | 1571 |
| 2024-09-20 22:21:35.504 | MS1 | 121.4656770449 | 31.1446351889 | 686 | 504990 | -85.12 | 15.36 | 57.09 | 0.00 | 2.52 | 1563 |
| 2024-09-20 22:21:36.839 | MS1 | 121.4656625404 | 31.1446254123 | 686 | 504990 | -89.10 | 16.58 | 97.29 | 0.06 | 2.70 | 1562 |
| 2024-09-20 22:21:37.152 | MS1 | 121.4656705118 | 31.1446345358 | 686 | 504990 | -93.91 | 11.70 | 71.34 | 0.20 | 2.25 | 1599 |
| 2024-09-20 22:21:38.161 | MS1 | 121.4656638438 | 31.1446239301 | 686 | 504990 | -93.14 | 8.53 | 84.12 | 0.09 | 2.70 | 1588 |
| 2024-09-20 22:21:39.311 | MS1 | 121.4656659781 | 31.1446373250 | 686 | 504990 | -89.31 | 12.21 | 60.88 | 0.03 | 2.12 | 1584 |
| 2024-09-20 22:21:40.764 | MS1 | 121.4656619715 | 31.1446346882 | 686 | 504990 | -89.65 | 8.41 | 598.14 | 0.05 | 2.19 | 1587 |
| 2024-09-20 22:21:41.278 | MS1 | 121.4656752280 | 31.1446339644 | 686 | 504990 | -90.69 | 8.68 | 315.69 | 0.13 | 2.60 | 1575 |
| 2024-09-20 22:21:42.299 | MS1 | 121.4656724203 | 31.1446354107 | 686 | 504990 | -90.63 | 8.37 | 310.70 | 0.07 | 2.53 | 1577 |

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
| 3220396 | 3 | 121.4707414495 | 31.1528090804 | 16 | 0 | 2 | 38.0 | TDD | 686 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3226168 | 2 | 121.4670791182 | 31.1513930210 | 128 | 15 | 5 | 34.7 | TDD | 362 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3247909 | 1 | 121.4717805665 | 31.1487404106 | 313 | 9 | 4 | 30.7 | TDD | 281 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3261583 | 4 | 121.4706688063 | 31.1554481929 | 293 | 1 | 1 | 26.0 | TDD | 9 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.992 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.011 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.118 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.118 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.879 | NREventA3 | measId:2;ServCellPCI:588;Se... |
| 2024-09-20 22:21:38.119 | NRHandoverAttempt | SourcePCI:588;SourceNR-ARFC... |
| 2024-09-20 22:21:38.150 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.160 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.283 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.283 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3247909 | 1 | 77.0373 | 82.4018 | -114.2048 | 18.1669 | 121.9973 | 0.0096 | 0.0159 |
| 2024_09_19 22:00 | 3226168 | 2 | 88.0182 | 92.5559 | -115.3941 | 15.8616 | 171.8241 | 0.0123 | 0.0047 |
| 2024_09_19 22:00 | 3220396 | 3 | 83.8322 | 86.2194 | -115.5228 | 11.2401 | 179.0591 | 0.0192 | 0.0161 |
| 2024_09_19 22:00 | 3261583 | 4 | 83.4122 | 78.8170 | -117.9768 | 15.1398 | 117.3109 | 0.0038 | 0.0087 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412204_980F67C9 | 504990 | 686 | -85.7 | 504990 | 362 | -93.6 | 504990 | 281 | -96.2 | 504990 | 9 |
| MR_1774412204_5A190167 | 504990 | 686 | -83.9 | 504990 | 362 | -90.5 | 504990 | 281 | -94.4 | 504990 | 9 |
| MR_1774412204_5413C78D | 504990 | 686 | -83.4 | 504990 | 362 | -92.8 | 504990 | 281 | -95.5 | 504990 | 9 |
| MR_1774412204_A9FB2651 | 504990 | 686 | -83.1 | 504990 | 362 | -89.9 | 504990 | 281 | -97.1 | 504990 | 9 |
| MR_1774412204_E9EFB923 | 504990 | 686 | -86.6 | 504990 | 362 | -90.8 | 504990 | 281 | -97.0 | 504990 | 9 |
| MR_1774412204_92908096 | 504990 | 686 | -86.7 | 504990 | 362 | -91.3 | 504990 | 281 | -97.5 | 504990 | 9 |
| MR_1774412204_B2B851D3 | 504990 | 686 | -83.6 | 504990 | 362 | -91.7 | 504990 | 281 | -97.2 | 504990 | 9 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1675: `48182b0e-e45...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `48182b0e-e45c-41bd-bb58-8dc93260c904` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278929_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1675] topology](images/train_1675.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3238158_6
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238158_6
- `C3`: Increase transmission power for 3278929_2
- `C4`: Add neighbor relationship between 3278929_2 and 3238158_6
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278929_2
- `C6`: Increase A3 Offset threshold for 3278929_2
- `C7`: Press down the tilt angle  of 3238158_6 by 3 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238158_6
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Adjust the azimuth of 3278929_2 by 2 degrees
- `C11`: Press down the tilt angle of 3278929_2 by 0 degrees
- `C12`: Increase transmission power for 3238158_6
- `C13`: Decrease A3 Offset threshold for 3278929_2
- `C14`: Lift the tilt angle  of 3238158_6 by 3 degrees
- `C15`: Adjust the azimuth of 3238158_6 by 23 degrees
- `C16`: Decrease A3 Offset threshold for 3238158_6
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278929_2 **← 정답**
- `C18`: Add neighbor relationship between 3226442_9 and 3238158_6
- `C19`: Lift the tilt angle of 3278929_2 by 0 degrees
- `C20`: Decrease transmission power for 3278929_2
- `C21`: Increase A3 Offset threshold for 3238158_6
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.702 | MS1 | 121.4656682452 | 31.1446188248 | 332 | 504990 | -94.54 | 10.23 | 309.53 | 0.17 | 2.72 | 1592 |
| 2024-09-20 22:21:32.355 | MS1 | 121.4656773308 | 31.1446222077 | 398 | 504990 | -94.72 | 14.01 | 460.32 | 0.09 | 2.25 | 1595 |
| 2024-09-20 22:21:33.528 | MS1 | 121.4656703522 | 31.1446197057 | 157 | 504990 | -93.15 | 10.05 | 581.15 | 0.18 | 2.50 | 1600 |
| 2024-09-20 22:21:34.887 | MS1 | 121.4656688739 | 31.1446273082 | 508 | 152650 | -95.41 | 2.18 | 59.34 | 0.11 | 1.60 | 985 |
| 2024-09-20 22:21:35.988 | MS1 | 121.4656734607 | 31.1446248586 | 921 | 152650 | -92.79 | 5.32 | 106.05 | 0.18 | 1.63 | 946 |
| 2024-09-20 22:21:36.289 | MS1 | 121.4656681286 | 31.1446294099 | 680 | 152650 | -93.32 | 6.31 | 100.97 | 0.01 | 1.95 | 957 |
| 2024-09-20 22:21:37.398 | MS1 | 121.4656729328 | 31.1446350731 | 937 | 152650 | -87.71 | 7.07 | 81.20 | 0.03 | 1.71 | 971 |
| 2024-09-20 22:21:38.979 | MS1 | 121.4656768422 | 31.1446189876 | 508 | 152650 | -89.20 | 3.08 | 85.36 | 0.13 | 1.74 | 996 |
| 2024-09-20 22:21:39.366 | MS1 | 121.4656631095 | 31.1446320087 | 921 | 152650 | -92.66 | 5.07 | 59.32 | 0.02 | 1.60 | 951 |
| 2024-09-20 22:21:40.371 | MS1 | 121.4656663719 | 31.1446270482 | 680 | 152650 | -95.46 | 5.18 | 63.54 | 0.19 | 2.05 | 1582 |
| 2024-09-20 22:21:41.332 | MS1 | 121.4656690117 | 31.1446217279 | 937 | 152650 | -96.31 | 3.20 | 84.59 | 0.11 | 2.93 | 1574 |
| 2024-09-20 22:21:42.987 | MS1 | 121.4656582030 | 31.1446374575 | 508 | 152650 | -93.57 | 2.46 | 75.47 | 0.14 | 2.36 | 1574 |

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
| 3210514 | 7 | 121.4684871788 | 31.1496516490 | 90 | 13 | 5 | 9.3 | FDD | 835 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3215903 | 10 | 121.4652803719 | 31.1495019987 | 203 | 9 | 12 | 8.9 | FDD | 937 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3226442 | 9 | 121.4656582514 | 31.1528732346 | 245 | 5 | 3 | 9.3 | FDD | 680 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3233604 | 3 | 121.4683875538 | 31.1445003402 | 71 | 9 | 1 | 21.5 | TDD | 750 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3235238 | 1 | 121.4715436356 | 31.1471732920 | 154 | 15 | 4 | 0.4 | TDD | 765 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3235447 | 5 | 121.4683997225 | 31.1485840848 | 162 | 0 | 1 | 16.9 | TDD | 157 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3238158 | 6 | 121.4659485949 | 31.1489888911 | 160 | 0 | 7 | 26.1 | TDD | 63 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3243001 | 12 | 121.4684715609 | 31.1516222796 | 206 | 0 | 8 | 0.5 | FDD | 921 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3251713 | 8 | 121.4708793865 | 31.1463474954 | 292 | 15 | 10 | 0.8 | FDD | 198 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3257511 | 11 | 121.4647683013 | 31.1554597200 | 327 | 0 | 5 | 17.5 | FDD | 938 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3259593 | 4 | 121.4737384000 | 31.1457212063 | 148 | 7 | 2 | 13.0 | TDD | 398 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3264407 | 13 | 121.4699998671 | 31.1549549761 | 295 | 2 | 4 | 1.9 | FDD | 508 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3278929 | 2 | 121.4655396750 | 31.1478135400 | 176 | 0 | 11 | 1.4 | TDD | 332 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.195 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.217 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.349 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.349 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.095 | NREventA2 | measId:1;ServCellPCI:83;Ser... |
| 2024-09-20 22:21:35.203 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.411 | NREventA5 | measId:3;ServCellPCI:83;Ser... |
| 2024-09-20 22:21:35.445 | NRHandoverAttempt | SourcePCI:83;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.493 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.504 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.652 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.652 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235238 | 1 | 17.2966 | 5.6475 | -117.1101 | 6.1786 | 105.1325 | 0.0084 | 0.0031 |
| 2024_09_20 22:00 | 3278929 | 2 | 6.3761 | 17.6859 | -114.2591 | 11.2728 | 80.6370 | 0.0087 | 0.0110 |
| 2024_09_20 22:00 | 3233604 | 3 | 17.3861 | 8.5701 | -115.1195 | 19.3231 | 139.2823 | 0.0008 | 0.0008 |
| 2024_09_20 22:00 | 3259593 | 4 | 17.4347 | 10.0217 | -117.3858 | 10.8783 | 128.6119 | 0.0114 | 0.0082 |
| 2024_09_20 22:00 | 3235447 | 5 | 7.1213 | 15.2843 | -116.0836 | 14.1164 | 187.9195 | 0.0059 | 0.0028 |
| 2024_09_20 22:00 | 3238158 | 6 | 16.8519 | 12.8534 | -116.9317 | 13.5922 | 199.9860 | 0.0162 | 0.0178 |
| 2024_09_20 22:00 | 3210514 | 7 | 13.9423 | 15.6759 | -114.3410 | 3.8798 | 43.1909 | 0.0176 | 0.0070 |
| 2024_09_20 22:00 | 3251713 | 8 | 12.6007 | 8.1747 | -115.8808 | 3.4689 | 21.8197 | 0.0149 | 0.0094 |
| 2024_09_20 22:00 | 3226442 | 9 | 12.7253 | 10.0809 | -116.2735 | 4.1549 | 41.2403 | 0.0076 | 0.0089 |
| 2024_09_20 22:00 | 3215903 | 10 | 10.8458 | 19.6898 | -114.0602 | 3.6798 | 52.7963 | 0.0140 | 0.0107 |
| 2024_09_20 22:00 | 3257511 | 11 | 6.6893 | 15.3512 | -116.1207 | 3.3284 | 26.3287 | 0.0179 | 0.0003 |
| 2024_09_20 22:00 | 3243001 | 12 | 13.5618 | 18.7219 | -114.6364 | 3.2185 | 31.9503 | 0.0101 | 0.0104 |
| 2024_09_20 22:00 | 3264407 | 13 | 12.7624 | 8.1569 | -116.2317 | 3.1024 | 33.2632 | 0.0124 | 0.0091 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414053_6C0CD57D | 152650 | 508 | -94.2 | 152650 | 198 | -99.3 | 152650 | 835 | -101.0 | 152650 | 938 |
| MR_1774414053_AF6D1D5A | 152650 | 508 | -96.9 | 152650 | 198 | -99.0 | 152650 | 835 | -100.2 | 152650 | 938 |
| MR_1774414053_C6A83820 | 504990 | 157 | -93.9 | 504990 | 63 | -89.0 | 504990 | 750 | -98.4 | 504990 | 765 |
| MR_1774414053_E7F0A38F | 504990 | 157 | -93.2 | 504990 | 63 | -88.0 | 504990 | 750 | -99.8 | 504990 | 765 |
| MR_1774414053_42E9A068 | 152650 | 508 | -95.7 | 152650 | 198 | -97.2 | 152650 | 835 | -102.4 | 152650 | 938 |
| MR_1774414053_586B410F | 152650 | 508 | -95.8 | 152650 | 198 | -100.3 | 152650 | 835 | -102.8 | 152650 | 938 |
| MR_1774414053_2965007B | 504990 | 157 | -93.1 | 504990 | 63 | -87.4 | 504990 | 750 | -100.5 | 504990 | 765 |
| MR_1774414053_6D8F81AC | 152650 | 508 | -94.1 | 152650 | 198 | -99.6 | 152650 | 835 | -100.5 | 152650 | 938 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1676: `1612e90d-939...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1612e90d-939f-46ed-a871-ec1e0598c881` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Lift the tilt angle  of 3252476_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1676] topology](images/train_1676.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3278472_3
- `C2`: Lift the tilt angle of 3278472_3 by 5 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278472_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278472_3
- `C5`: Decrease transmission power for 3278472_3
- `C6`: Press down the tilt angle  of 3252476_1 by 10 degrees
- `C7`: Adjust the azimuth of 3278472_3 by 2 degrees
- `C8`: Add neighbor relationship between 3278472_3 and 3242386_4
- `C9`: Increase A3 Offset threshold for 3242386_4
- `C10`: Decrease A3 Offset threshold for 3278472_3
- `C11`: Decrease transmission power for 3242386_4
- `C12`: Increase transmission power for 3242386_4
- `C13`: Press down the tilt angle of 3278472_3 by 5 degrees
- `C14`: Increase A3 Offset threshold for 3278472_3
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease A3 Offset threshold for 3242386_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242386_4
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242386_4
- `C19`: Adjust the azimuth of 3252476_1 by 2 degrees
- `C20`: Check test server and transmission issues
- `C21`: Add neighbor relationship between 3252476_1 and 3242386_4
- `C22`: Lift the tilt angle  of 3252476_1 by 10 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.873 | MS1 | 121.4656765421 | 31.1446342370 | 53 | 504990 | -86.77 | 15.75 | 305.42 | 0.16 | 2.22 | 1593 |
| 2024-09-20 22:21:32.126 | MS1 | 121.4656664190 | 31.1446226353 | 53 | 504990 | -90.87 | 15.31 | 394.55 | 0.06 | 2.72 | 1583 |
| 2024-09-20 22:21:33.546 | MS1 | 121.4656692312 | 31.1446371743 | 53 | 504990 | -86.16 | 14.46 | 442.52 | 0.06 | 2.12 | 1567 |
| 2024-09-20 22:21:34.890 | MS1 | 121.4656605687 | 31.1446186403 | 53 | 504990 | -86.93 | 14.58 | 57.82 | 0.17 | 2.42 | 1570 |
| 2024-09-20 22:21:35.248 | MS1 | 121.4656610963 | 31.1446344521 | 53 | 504990 | -86.76 | 13.43 | 91.80 | 0.12 | 2.81 | 1578 |
| 2024-09-20 22:21:36.131 | MS1 | 121.4656581252 | 31.1446256432 | 53 | 504990 | -87.31 | 17.36 | 58.96 | 0.08 | 2.97 | 1583 |
| 2024-09-20 22:21:37.606 | MS1 | 121.4656662347 | 31.1446290688 | 53 | 504990 | -93.34 | 11.86 | 79.20 | 0.19 | 2.56 | 1572 |
| 2024-09-20 22:21:38.853 | MS1 | 121.4656737271 | 31.1446284721 | 53 | 504990 | -93.17 | 12.12 | 80.10 | 0.04 | 2.25 | 1566 |
| 2024-09-20 22:21:39.478 | MS1 | 121.4656624254 | 31.1446241179 | 53 | 504990 | -89.59 | 10.02 | 81.04 | 0.04 | 2.70 | 1590 |
| 2024-09-20 22:21:40.840 | MS1 | 121.4656680821 | 31.1446199844 | 53 | 504990 | -93.08 | 7.78 | 538.03 | 0.12 | 2.14 | 1579 |
| 2024-09-20 22:21:41.186 | MS1 | 121.4656656530 | 31.1446219059 | 53 | 504990 | -92.57 | 12.97 | 506.47 | 0.18 | 2.40 | 1571 |
| 2024-09-20 22:21:42.782 | MS1 | 121.4656598158 | 31.1446298540 | 53 | 504990 | -93.79 | 9.75 | 395.27 | 0.06 | 2.60 | 1590 |

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
| 3242386 | 4 | 121.4708993421 | 31.1526218617 | 211 | 9 | 4 | 40.2 | TDD | 999 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3252476 | 1 | 121.4742782355 | 31.1536269965 | 97 | 10 | 5 | 45.7 | TDD | 650 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3278365 | 2 | 121.4694093375 | 31.1536955762 | 180 | 6 | 5 | 22.7 | TDD | 363 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3278472 | 3 | 121.4733040674 | 31.1468663319 | 253 | 2 | 6 | 35.4 | TDD | 53 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.975 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.992 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.111 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.111 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.830 | NREventA3 | measId:2;ServCellPCI:623;Se... |
| 2024-09-20 22:21:38.070 | NRHandoverAttempt | SourcePCI:623;SourceNR-ARFC... |
| 2024-09-20 22:21:38.116 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.127 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.260 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.260 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252476 | 1 | 19.7500 | 9.7303 | -117.2541 | 7.2748 | 102.1455 | 0.0131 | 0.0122 |
| 2024_09_20 22:00 | 3278365 | 2 | 19.9680 | 16.5531 | -114.3045 | 9.3813 | 186.5370 | 0.0035 | 0.0093 |
| 2024_09_20 22:00 | 3278472 | 3 | 76.6794 | 81.2914 | -115.9860 | 6.8037 | 147.3930 | 0.0171 | 0.0155 |
| 2024_09_20 22:00 | 3242386 | 4 | 17.1381 | 16.3302 | -117.5253 | 19.8183 | 114.3364 | 0.0151 | 0.0178 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412759_756C3D6D | 504990 | 53 | -87.2 | 504990 | 999 | -91.0 | 504990 | 650 | -100.7 | 504990 | 363 |
| MR_1774412759_09A5C1FF | 504990 | 53 | -87.3 | 504990 | 999 | -93.5 | 504990 | 650 | -101.9 | 504990 | 363 |
| MR_1774412759_6E9C6C50 | 504990 | 53 | -85.1 | 504990 | 999 | -92.2 | 504990 | 650 | -100.3 | 504990 | 363 |
| MR_1774412759_69F1A26B | 504990 | 53 | -85.2 | 504990 | 999 | -94.5 | 504990 | 650 | -98.7 | 504990 | 363 |
| MR_1774412759_8DAED7B3 | 504990 | 53 | -87.0 | 504990 | 999 | -94.8 | 504990 | 650 | -100.7 | 504990 | 363 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1677: `2e6654db-4a9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2e6654db-4a93-4d1d-9d77-cfda21f0505a` |
| Tag | **multiple-answer** |
| 정답 | **C1|C7** |
| C1 의미 | Press down the tilt angle  of 3225088_4 by 4 degrees |
| C7 의미 | Decrease transmission power for 3225088_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1677] topology](images/train_1677.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3225088_4 by 4 degrees **← 정답**
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225088_4
- `C3`: Lift the tilt angle  of 3225088_4 by 4 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268312_2
- `C5`: Increase transmission power for 3225088_4
- `C6`: Decrease A3 Offset threshold for 3225088_4
- `C7`: Decrease transmission power for 3225088_4 **← 정답**
- `C8`: Decrease A3 Offset threshold for 3268312_2
- `C9`: Check test server and transmission issues
- `C10`: Increase A3 Offset threshold for 3225088_4
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase transmission power for 3268312_2
- `C13`: Adjust the azimuth of 3225088_4 by 4 degrees
- `C14`: Add neighbor relationship between 3268312_2 and 3225088_4
- `C15`: Press down the tilt angle of 3268312_2 by 3 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225088_4
- `C17`: Adjust the azimuth of 3268312_2 by 33 degrees
- `C18`: Decrease transmission power for 3268312_2
- `C19`: Lift the tilt angle of 3268312_2 by 3 degrees
- `C20`: Increase A3 Offset threshold for 3268312_2
- `C21`: Add neighbor relationship between 3276118_1 and 3225088_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268312_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.478 | MS1 | 121.4656696902 | 31.1446224353 | 562 | 504990 | -75.59 | 16.03 | 308.61 | 0.02 | 2.46 | 1588 |
| 2024-09-20 22:21:32.673 | MS1 | 121.4656638478 | 31.1446350765 | 562 | 504990 | -80.93 | 12.79 | 495.88 | 0.14 | 2.68 | 1596 |
| 2024-09-20 22:21:33.487 | MS1 | 121.4656685699 | 31.1446309609 | 562 | 504990 | -82.97 | 14.99 | 540.39 | 0.13 | 2.48 | 1587 |
| 2024-09-20 22:21:34.734 | MS1 | 121.4656667458 | 31.1446258218 | 562 | 504990 | -94.52 | 3.30 | 42.98 | 0.14 | 1.20 | 1571 |
| 2024-09-20 22:21:35.679 | MS1 | 121.4656763895 | 31.1446301819 | 562 | 504990 | -89.77 | 3.12 | 68.77 | 0.16 | 1.39 | 1576 |
| 2024-09-20 22:21:36.190 | MS1 | 121.4656765130 | 31.1446233413 | 562 | 504990 | -92.75 | 1.50 | 63.80 | 0.11 | 1.44 | 1578 |
| 2024-09-20 22:21:37.307 | MS1 | 121.4656639779 | 31.1446250845 | 562 | 504990 | -92.81 | 1.04 | 60.20 | 0.09 | 1.24 | 1569 |
| 2024-09-20 22:21:38.379 | MS1 | 121.4656620694 | 31.1446324424 | 562 | 504990 | -86.55 | 2.50 | 60.90 | 0.10 | 1.35 | 1587 |
| 2024-09-20 22:21:39.991 | MS1 | 121.4656760602 | 31.1446329243 | 562 | 504990 | -88.56 | 2.39 | 56.26 | 0.18 | 1.24 | 1596 |
| 2024-09-20 22:21:40.432 | MS1 | 121.4656615634 | 31.1446185968 | 562 | 504990 | -82.06 | 16.50 | 358.78 | 0.04 | 2.22 | 1570 |
| 2024-09-20 22:21:41.955 | MS1 | 121.4656673128 | 31.1446266655 | 562 | 504990 | -75.76 | 15.37 | 319.77 | 0.19 | 2.94 | 1572 |
| 2024-09-20 22:21:42.542 | MS1 | 121.4656712430 | 31.1446262441 | 562 | 504990 | -79.14 | 17.20 | 399.03 | 0.10 | 2.40 | 1577 |

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
| 3212140 | 3 | 121.4670286691 | 31.1510363777 | 318 | 9 | 5 | 24.2 | TDD | 859 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3225088 | 4 | 121.4739337756 | 31.1518804382 | 220 | 2 | 11 | 30.9 | TDD | 612 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3268312 | 2 | 121.4649868632 | 31.1491468231 | 140 | 0 | 12 | 29.9 | TDD | 562 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3276118 | 1 | 121.4716130668 | 31.1558419573 | 218 | 11 | 4 | 17.1 | TDD | 968 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.964 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.988 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.110 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.110 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276118 | 1 | 10.5451 | 15.1740 | -114.8785 | 15.5946 | 171.8034 | 0.0070 | 0.0174 |
| 2024_09_20 22:00 | 3268312 | 2 | 5.2836 | 9.5554 | -109.5536 | 11.0873 | 191.6930 | 0.0163 | 0.0052 |
| 2024_09_20 22:00 | 3212140 | 3 | 9.4749 | 17.5882 | -115.6816 | 8.0962 | 122.4494 | 0.0144 | 0.0172 |
| 2024_09_20 22:00 | 3225088 | 4 | 13.3226 | 19.7979 | -116.3396 | 15.5479 | 193.3453 | 0.0156 | 0.0186 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413200_6136150B | 504990 | 562 | -96.2 | 504990 | 612 | -91.8 | 504990 | 968 | -97.9 | 504990 | 859 |
| MR_1774413200_97DF168B | 504990 | 562 | -94.3 | 504990 | 612 | -91.1 | 504990 | 968 | -96.6 | 504990 | 859 |
| MR_1774413200_1CD0D0DD | 504990 | 562 | -92.7 | 504990 | 612 | -90.1 | 504990 | 968 | -97.7 | 504990 | 859 |
| MR_1774413200_ACE693E7 | 504990 | 612 | -92.7 | 504990 | 562 | -88.7 | 504990 | 968 | -97.5 | 504990 | 859 |
| MR_1774413200_6AFC01F3 | 504990 | 562 | -96.3 | 504990 | 612 | -90.8 | 504990 | 968 | -98.3 | 504990 | 859 |
| MR_1774413200_ACBA84B1 | 504990 | 562 | -92.6 | 504990 | 612 | -92.2 | 504990 | 968 | -99.0 | 504990 | 859 |
| MR_1774413200_3A10FA99 | 504990 | 562 | -93.0 | 504990 | 612 | -92.4 | 504990 | 968 | -98.5 | 504990 | 859 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1678: `e5d86b15-2d5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e5d86b15-2d59-4ada-a281-d839057fd0b4` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1678] topology](images/train_1678.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3260955_4
- `C2`: Insufficient data; more data is needed for judgment. **← 정답**
- `C3`: Adjust the azimuth of 3260955_4 by 50 degrees
- `C4`: Lift the tilt angle of 3260309_2 by 10 degrees
- `C5`: Add neighbor relationship between 3260309_2 and 3260955_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260955_4
- `C7`: Increase A3 Offset threshold for 3260309_2
- `C8`: Increase transmission power for 3260309_2
- `C9`: Add neighbor relationship between 3251009_3 and 3260955_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260309_2
- `C11`: Press down the tilt angle  of 3260955_4 by 8 degrees
- `C12`: Increase transmission power for 3260955_4
- `C13`: Decrease A3 Offset threshold for 3260955_4
- `C14`: Adjust the azimuth of 3260309_2 by 50 degrees
- `C15`: Lift the tilt angle  of 3260955_4 by 8 degrees
- `C16`: Press down the tilt angle of 3260309_2 by 10 degrees
- `C17`: Check test server and transmission issues
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260309_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260955_4
- `C20`: Decrease transmission power for 3260309_2
- `C21`: Decrease A3 Offset threshold for 3260309_2
- `C22`: Increase A3 Offset threshold for 3260955_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.779 | MS1 | 121.4656617806 | 31.1446202903 | 387 | 504990 | -87.65 | 17.21 | 323.81 | 0.06 | 2.27 | 1594 |
| 2024-09-20 22:21:32.199 | MS1 | 121.4656581889 | 31.1446345865 | 387 | 504990 | -89.29 | 14.40 | 495.23 | 0.16 | 2.18 | 1595 |
| 2024-09-20 22:21:33.327 | MS1 | 121.4656663844 | 31.1446223216 | 387 | 504990 | -88.11 | 15.10 | 334.85 | 0.08 | 2.01 | 1569 |
| 2024-09-20 22:21:34.586 | MS1 | 121.4656741835 | 31.1446235949 | 387 | 504990 | -91.23 | 14.23 | 73.31 | 0.06 | 2.92 | 1563 |
| 2024-09-20 22:21:35.404 | MS1 | 121.4656615773 | 31.1446288926 | 387 | 504990 | -88.34 | 17.30 | 80.47 | 0.08 | 2.92 | 1575 |
| 2024-09-20 22:21:36.798 | MS1 | 121.4656626268 | 31.1446237479 | 387 | 504990 | -89.03 | 16.40 | 57.39 | 0.10 | 2.30 | 1585 |
| 2024-09-20 22:21:37.785 | MS1 | 121.4656692164 | 31.1446263928 | 387 | 504990 | -92.65 | 7.05 | 93.38 | 0.04 | 2.07 | 1598 |
| 2024-09-20 22:21:38.498 | MS1 | 121.4656658144 | 31.1446234555 | 387 | 504990 | -90.30 | 12.93 | 81.03 | 0.00 | 2.27 | 1594 |
| 2024-09-20 22:21:39.723 | MS1 | 121.4656773126 | 31.1446209542 | 387 | 504990 | -91.11 | 10.54 | 78.86 | 0.08 | 2.52 | 1563 |
| 2024-09-20 22:21:40.232 | MS1 | 121.4656750432 | 31.1446223113 | 387 | 504990 | -92.13 | 11.64 | 504.57 | 0.04 | 2.20 | 1565 |
| 2024-09-20 22:21:41.462 | MS1 | 121.4656777725 | 31.1446294778 | 387 | 504990 | -89.55 | 8.23 | 494.82 | 0.17 | 2.02 | 1565 |
| 2024-09-20 22:21:42.271 | MS1 | 121.4656628957 | 31.1446252470 | 387 | 504990 | -91.40 | 7.89 | 302.62 | 0.19 | 2.72 | 1577 |

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
| 3251009 | 3 | 121.4662352044 | 31.1493920029 | 230 | 14 | 6 | 43.4 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3260309 | 2 | 121.4654909360 | 31.1452613624 | 278 | 13 | 0 | 24.6 | TDD | 387 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3260955 | 4 | 121.4689240644 | 31.1539524138 | 38 | 5 | 4 | 48.5 | TDD | 399 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3264088 | 1 | 121.4746755414 | 31.1495642580 | 10 | 5 | 5 | 42.8 | TDD | 802 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.559 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.579 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.688 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.688 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.381 | NREventA3 | measId:2;ServCellPCI:329;Se... |
| 2024-09-20 22:21:38.621 | NRHandoverAttempt | SourcePCI:329;SourceNR-ARFC... |
| 2024-09-20 22:21:38.669 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.683 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.802 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.802 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3264088 | 1 | 88.4427 | 94.7153 | -115.2095 | 10.4552 | 180.8972 | 0.0193 | 0.0178 |
| 2024_09_19 22:00 | 3260309 | 2 | 76.9015 | 88.7219 | -115.2338 | 16.6515 | 177.3007 | 0.0169 | 0.0047 |
| 2024_09_19 22:00 | 3251009 | 3 | 84.7040 | 75.5439 | -114.6144 | 19.5556 | 119.2597 | 0.0045 | 0.0181 |
| 2024_09_19 22:00 | 3260955 | 4 | 93.0744 | 76.6659 | -114.8831 | 19.9339 | 169.0334 | 0.0175 | 0.0032 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414611_11443B9E | 504990 | 387 | -91.1 | 504990 | 399 | -102.0 | 504990 | 309 | -106.2 | 504990 | 802 |
| MR_1774414611_BF19FA75 | 504990 | 387 | -92.8 | 504990 | 399 | -99.3 | 504990 | 309 | -106.2 | 504990 | 802 |
| MR_1774414611_9C32A6E5 | 504990 | 387 | -91.6 | 504990 | 399 | -102.0 | 504990 | 309 | -104.7 | 504990 | 802 |
| MR_1774414611_926BD053 | 504990 | 387 | -89.6 | 504990 | 399 | -100.7 | 504990 | 309 | -105.8 | 504990 | 802 |
| MR_1774414611_0ED73D3F | 504990 | 387 | -90.3 | 504990 | 399 | -100.0 | 504990 | 309 | -104.3 | 504990 | 802 |
| MR_1774414611_A7D44753 | 504990 | 387 | -92.8 | 504990 | 399 | -102.3 | 504990 | 309 | -107.9 | 504990 | 802 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1679: `5553042a-5a3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5553042a-5a3d-4f70-a97e-56c006f27197` |
| Tag | **multiple-answer** |
| 정답 | **C1|C19** |
| C1 의미 | Adjust the azimuth of 3268756_1 by 44 degrees |
| C19 의미 | Increase transmission power for 3268756_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1679] topology](images/train_1679.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3268756_1 by 44 degrees **← 정답**
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Check test server and transmission issues
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268756_1
- `C5`: Decrease A3 Offset threshold for 3268756_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268756_1
- `C7`: Lift the tilt angle of 3268756_1 by 9 degrees
- `C8`: Add neighbor relationship between 3268756_1 and 3264590_2
- `C9`: Increase A3 Offset threshold for 3268756_1
- `C10`: Press down the tilt angle of 3268756_1 by 9 degrees
- `C11`: Increase A3 Offset threshold for 3264590_2
- `C12`: Decrease A3 Offset threshold for 3264590_2
- `C13`: Decrease transmission power for 3264590_2
- `C14`: Add neighbor relationship between 3264538_3 and 3264590_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264590_2
- `C16`: Press down the tilt angle  of 3264590_2 by 1 degrees
- `C17`: Lift the tilt angle  of 3264590_2 by 1 degrees
- `C18`: Adjust the azimuth of 3264590_2 by 29 degrees
- `C19`: Increase transmission power for 3268756_1 **← 정답**
- `C20`: Decrease transmission power for 3268756_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264590_2
- `C22`: Increase transmission power for 3264590_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.117 | MS1 | 121.4656606275 | 31.1446251275 | 208 | 504990 | -87.39 | 17.12 | 487.11 | 0.02 | 2.44 | 1578 |
| 2024-09-20 22:21:32.539 | MS1 | 121.4656761312 | 31.1446336923 | 208 | 504990 | -86.56 | 14.57 | 538.81 | 0.07 | 2.41 | 1595 |
| 2024-09-20 22:21:33.654 | MS1 | 121.4656603516 | 31.1446375524 | 208 | 504990 | -88.20 | 17.56 | 318.62 | 0.05 | 2.87 | 1570 |
| 2024-09-20 22:21:34.999 | MS1 | 121.4656635915 | 31.1446230044 | 208 | 504990 | -109.71 | 0.33 | 33.42 | 0.07 | 1.28 | 1589 |
| 2024-09-20 22:21:35.170 | MS1 | 121.4656672791 | 31.1446326864 | 208 | 504990 | -101.29 | -0.07 | 70.36 | 0.07 | 1.20 | 1581 |
| 2024-09-20 22:21:36.903 | MS1 | 121.4656727310 | 31.1446240790 | 208 | 504990 | -106.70 | 1.49 | 64.99 | 0.07 | 1.44 | 1566 |
| 2024-09-20 22:21:37.387 | MS1 | 121.4656654901 | 31.1446365629 | 208 | 504990 | -103.13 | -0.53 | 45.06 | 0.16 | 1.46 | 1577 |
| 2024-09-20 22:21:38.138 | MS1 | 121.4656777763 | 31.1446303654 | 208 | 504990 | -102.61 | -1.67 | 65.22 | 0.10 | 1.22 | 1572 |
| 2024-09-20 22:21:39.375 | MS1 | 121.4656599134 | 31.1446325706 | 208 | 504990 | -108.28 | -1.98 | 63.79 | 0.11 | 1.42 | 1568 |
| 2024-09-20 22:21:40.310 | MS1 | 121.4656686677 | 31.1446242174 | 208 | 504990 | -94.37 | 14.09 | 538.24 | 0.06 | 2.30 | 1563 |
| 2024-09-20 22:21:41.352 | MS1 | 121.4656718088 | 31.1446336499 | 208 | 504990 | -89.17 | 15.02 | 328.51 | 0.11 | 2.03 | 1574 |
| 2024-09-20 22:21:42.289 | MS1 | 121.4656622399 | 31.1446259362 | 208 | 504990 | -88.62 | 14.14 | 505.25 | 0.15 | 2.86 | 1569 |

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
| 3247948 | 4 | 121.4649973994 | 31.1475563984 | 26 | 11 | 3 | 16.8 | TDD | 431 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3264538 | 3 | 121.4710887792 | 31.1441613449 | 195 | 0 | 5 | 34.0 | TDD | 840 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3264590 | 2 | 121.4755482336 | 31.1500822686 | 266 | 0 | 5 | 16.5 | TDD | 354 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3268756 | 1 | 121.4647824351 | 31.1556720878 | 132 | 8 | 0 | 27.0 | TDD | 208 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.102 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.202 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.202 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.427 | NREventA2 | measId:1;ServCellPCI:640;Se... |
| 2024-09-20 22:21:34.542 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268756 | 1 | 6.7244 | 15.2545 | -117.0275 | 5.3347 | 184.6154 | 0.1405 | 0.0146 |
| 2024_09_20 22:00 | 3264590 | 2 | 9.4472 | 15.1371 | -114.3534 | 5.5156 | 185.3910 | 0.0114 | 0.0006 |
| 2024_09_20 22:00 | 3264538 | 3 | 11.4090 | 11.2807 | -117.0439 | 9.0139 | 185.5802 | 0.0060 | 0.0072 |
| 2024_09_20 22:00 | 3247948 | 4 | 17.8793 | 10.7418 | -114.6190 | 8.8174 | 152.1693 | 0.0013 | 0.0047 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417126_3A7EC786 | 504990 | 208 | -108.1 | 504990 | 354 | -113.2 | 504990 | 840 | -120.7 | 504990 | 431 |
| MR_1774417126_6E69E1F7 | 504990 | 208 | -111.0 | 504990 | 354 | -113.3 | 504990 | 840 | -118.8 | 504990 | 431 |
| MR_1774417126_80FCE369 | 504990 | 208 | -109.2 | 504990 | 354 | -112.6 | 504990 | 840 | -117.1 | 504990 | 431 |
| MR_1774417126_5530FFB3 | 504990 | 208 | -110.4 | 504990 | 354 | -112.4 | 504990 | 840 | -117.2 | 504990 | 431 |
| MR_1774417126_B5E6E8F7 | 504990 | 208 | -110.3 | 504990 | 354 | -114.9 | 504990 | 840 | -118.6 | 504990 | 431 |

> *... 2개 열 생략 (전체 14열)*

---
