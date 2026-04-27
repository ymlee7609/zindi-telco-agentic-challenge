# Track A 문제 분석 — train[1710]~train[1719]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1710] ~ train[1719] (10개)

## 목차

1. [문제 1710: `1389a2a8-3bd...`](#1710) — single-answer, 정답: C12
2. [문제 1711: `dd5b9f36-411...`](#1711) — multiple-answer, 정답: C8|C15
3. [문제 1712: `794ca723-f3d...`](#1712) — single-answer, 정답: C19
4. [문제 1713: `a5320a80-9b5...`](#1713) — single-answer, 정답: C3
5. [문제 1714: `f2301a64-2e2...`](#1714) — single-answer, 정답: C8
6. [문제 1715: `6c151a05-322...`](#1715) — multiple-answer, 정답: C5|C16
7. [문제 1716: `84ac1e3b-348...`](#1716) — single-answer, 정답: C21
8. [문제 1717: `ee99a715-821...`](#1717) — single-answer, 정답: C21
9. [문제 1718: `65736b93-af0...`](#1718) — single-answer, 정답: C19
10. [문제 1719: `c590edeb-cf0...`](#1719) — single-answer, 정답: C2

---

### 문제 1710: `1389a2a8-3bd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1389a2a8-3bdf-433a-abcc-221ca4f206d0` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1710] topology](images/train_1710.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275568_1
- `C2`: Increase A3 Offset threshold for 3235756_2
- `C3`: Press down the tilt angle  of 3235756_2 by 10 degrees
- `C4`: Decrease A3 Offset threshold for 3275568_1
- `C5`: Increase transmission power for 3235756_2
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Press down the tilt angle of 3275568_1 by 10 degrees
- `C8`: Decrease transmission power for 3275568_1
- `C9`: Add neighbor relationship between 3216912_4 and 3235756_2
- `C10`: Increase transmission power for 3275568_1
- `C11`: Adjust the azimuth of 3235756_2 by 50 degrees
- `C12`: Check test server and transmission issues **← 정답**
- `C13`: Decrease A3 Offset threshold for 3235756_2
- `C14`: Increase A3 Offset threshold for 3275568_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235756_2
- `C16`: Add neighbor relationship between 3275568_1 and 3235756_2
- `C17`: Adjust the azimuth of 3275568_1 by 18 degrees
- `C18`: Decrease transmission power for 3235756_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275568_1
- `C20`: Lift the tilt angle of 3275568_1 by 10 degrees
- `C21`: Lift the tilt angle  of 3235756_2 by 10 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235756_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.933 | MS1 | 121.4656686636 | 31.1446222743 | 440 | 504990 | -90.32 | 17.28 | 379.32 | 0.01 | 2.26 | 1585 |
| 2024-09-20 22:21:32.806 | MS1 | 121.4656588491 | 31.1446249306 | 440 | 504990 | -91.41 | 15.90 | 527.16 | 0.05 | 2.37 | 1560 |
| 2024-09-20 22:21:33.812 | MS1 | 121.4656721632 | 31.1446253041 | 440 | 504990 | -86.65 | 14.60 | 534.62 | 0.14 | 2.17 | 1562 |
| 2024-09-20 22:21:34.411 | MS1 | 121.4656607726 | 31.1446272167 | 440 | 504990 | -91.86 | 13.16 | 99.91 | 0.06 | 2.02 | 311 |
| 2024-09-20 22:21:35.911 | MS1 | 121.4656584192 | 31.1446219583 | 440 | 504990 | -86.94 | 13.59 | 80.27 | 0.16 | 2.53 | 443 |
| 2024-09-20 22:21:36.418 | MS1 | 121.4656662362 | 31.1446314367 | 440 | 504990 | -90.61 | 15.45 | 48.96 | 0.11 | 2.01 | 447 |
| 2024-09-20 22:21:37.218 | MS1 | 121.4656676080 | 31.1446235798 | 440 | 504990 | -90.84 | 10.40 | 82.64 | 0.06 | 2.50 | 477 |
| 2024-09-20 22:21:38.959 | MS1 | 121.4656686358 | 31.1446205510 | 440 | 504990 | -93.89 | 12.97 | 75.71 | 0.01 | 2.81 | 339 |
| 2024-09-20 22:21:39.888 | MS1 | 121.4656620329 | 31.1446364870 | 440 | 504990 | -92.55 | 8.85 | 60.10 | 0.12 | 2.67 | 378 |
| 2024-09-20 22:21:40.276 | MS1 | 121.4656625080 | 31.1446240469 | 440 | 504990 | -93.53 | 11.64 | 411.99 | 0.10 | 2.82 | 1563 |
| 2024-09-20 22:21:41.148 | MS1 | 121.4656630101 | 31.1446219330 | 440 | 504990 | -93.23 | 9.82 | 487.73 | 0.09 | 2.29 | 1587 |
| 2024-09-20 22:21:42.706 | MS1 | 121.4656591492 | 31.1446223997 | 440 | 504990 | -92.70 | 8.94 | 385.99 | 0.18 | 2.05 | 1561 |

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
| 3216912 | 4 | 121.4755710496 | 31.1501539551 | 311 | 9 | 8 | 47.7 | TDD | 566 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3235756 | 2 | 121.4641132620 | 31.1467675020 | 73 | 11 | 6 | 24.5 | TDD | 617 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3275568 | 1 | 121.4712497623 | 31.1472344323 | 259 | 8 | 11 | 49.3 | TDD | 440 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3276555 | 3 | 121.4740346751 | 31.1476350663 | 165 | 15 | 0 | 18.2 | TDD | 51 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.191 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.210 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.344 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.344 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.042 | NREventA3 | measId:2;ServCellPCI:222;Se... |
| 2024-09-20 22:21:38.282 | NRHandoverAttempt | SourcePCI:222;SourceNR-ARFC... |
| 2024-09-20 22:21:38.330 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.344 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.474 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.474 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275568 | 1 | 7.1928 | 15.6989 | -117.3762 | 18.1496 | 153.8458 | 0.0142 | 0.0197 |
| 2024_09_20 22:00 | 3235756 | 2 | 7.1484 | 11.7116 | -117.7864 | 10.4899 | 105.1826 | 0.0025 | 0.0090 |
| 2024_09_20 22:00 | 3276555 | 3 | 12.3582 | 14.5058 | -115.1621 | 15.1980 | 109.1254 | 0.0099 | 0.0099 |
| 2024_09_20 22:00 | 3216912 | 4 | 6.9331 | 11.2422 | -116.7644 | 7.0906 | 117.7102 | 0.0082 | 0.0088 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413645_FBC1281C | 504990 | 440 | -91.4 | 504990 | 617 | -94.2 | 504990 | 566 | -105.3 | 504990 | 51 |
| MR_1774413645_684E56B5 | 504990 | 440 | -92.7 | 504990 | 617 | -97.3 | 504990 | 566 | -105.5 | 504990 | 51 |
| MR_1774413645_CE025216 | 504990 | 440 | -91.3 | 504990 | 617 | -94.6 | 504990 | 566 | -105.7 | 504990 | 51 |
| MR_1774413645_81FCCED6 | 504990 | 440 | -91.5 | 504990 | 617 | -96.8 | 504990 | 566 | -106.3 | 504990 | 51 |
| MR_1774413645_48D6C2F8 | 504990 | 440 | -91.6 | 504990 | 617 | -96.8 | 504990 | 566 | -103.6 | 504990 | 51 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1711: `dd5b9f36-411...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dd5b9f36-4110-4d01-83f3-0b3e26e23548` |
| Tag | **multiple-answer** |
| 정답 | **C8|C15** |
| C8 의미 | Increase transmission power for 3236885_1 |
| C15 의미 | Adjust the azimuth of 3236885_1 by 40 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1711] topology](images/train_1711.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236885_1
- `C2`: Add neighbor relationship between 3217788_3 and 3240900_2
- `C3`: Lift the tilt angle  of 3240900_2 by 2 degrees
- `C4`: Press down the tilt angle  of 3240900_2 by 2 degrees
- `C5`: Lift the tilt angle of 3236885_1 by 10 degrees
- `C6`: Decrease transmission power for 3236885_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236885_1
- `C8`: Increase transmission power for 3236885_1 **← 정답**
- `C9`: Decrease A3 Offset threshold for 3240900_2
- `C10`: Adjust the azimuth of 3240900_2 by 36 degrees
- `C11`: Increase A3 Offset threshold for 3236885_1
- `C12`: Increase A3 Offset threshold for 3240900_2
- `C13`: Add neighbor relationship between 3236885_1 and 3240900_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240900_2
- `C15`: Adjust the azimuth of 3236885_1 by 40 degrees **← 정답**
- `C16`: Decrease A3 Offset threshold for 3236885_1
- `C17`: Decrease transmission power for 3240900_2
- `C18`: Press down the tilt angle of 3236885_1 by 10 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240900_2
- `C20`: Check test server and transmission issues
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Increase transmission power for 3240900_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.291 | MS1 | 121.4656612545 | 31.1446351859 | 297 | 504990 | -88.13 | 12.67 | 302.87 | 0.04 | 2.30 | 1589 |
| 2024-09-20 22:21:32.548 | MS1 | 121.4656706734 | 31.1446182640 | 297 | 504990 | -91.71 | 12.39 | 519.23 | 0.15 | 2.65 | 1599 |
| 2024-09-20 22:21:33.959 | MS1 | 121.4656711921 | 31.1446325687 | 297 | 504990 | -92.32 | 12.82 | 448.69 | 0.15 | 2.01 | 1593 |
| 2024-09-20 22:21:34.826 | MS1 | 121.4656752572 | 31.1446363131 | 297 | 504990 | -101.12 | 0.61 | 48.84 | 0.00 | 1.19 | 1564 |
| 2024-09-20 22:21:35.723 | MS1 | 121.4656635555 | 31.1446222994 | 297 | 504990 | -105.30 | 0.89 | 57.23 | 0.15 | 1.11 | 1574 |
| 2024-09-20 22:21:36.825 | MS1 | 121.4656657511 | 31.1446221379 | 297 | 504990 | -101.94 | -1.14 | 20.26 | 0.18 | 1.16 | 1597 |
| 2024-09-20 22:21:37.255 | MS1 | 121.4656750499 | 31.1446283916 | 297 | 504990 | -100.95 | -0.37 | 55.26 | 0.10 | 1.45 | 1594 |
| 2024-09-20 22:21:38.367 | MS1 | 121.4656674562 | 31.1446353857 | 297 | 504990 | -103.03 | -1.04 | 67.79 | 0.07 | 1.13 | 1579 |
| 2024-09-20 22:21:39.751 | MS1 | 121.4656722772 | 31.1446370045 | 297 | 504990 | -109.97 | 1.60 | 20.38 | 0.15 | 1.00 | 1593 |
| 2024-09-20 22:21:40.697 | MS1 | 121.4656708812 | 31.1446332309 | 297 | 504990 | -92.29 | 14.33 | 368.31 | 0.05 | 2.89 | 1570 |
| 2024-09-20 22:21:41.702 | MS1 | 121.4656659793 | 31.1446185120 | 297 | 504990 | -89.61 | 12.85 | 332.38 | 0.18 | 2.94 | 1586 |
| 2024-09-20 22:21:42.626 | MS1 | 121.4656617562 | 31.1446181343 | 297 | 504990 | -87.82 | 15.11 | 561.23 | 0.06 | 2.15 | 1575 |

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
| 3217788 | 3 | 121.4742886030 | 31.1468599851 | 353 | 4 | 5 | 30.4 | TDD | 885 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3234597 | 4 | 121.4666453295 | 31.1518576736 | 344 | 2 | 11 | 48.7 | TDD | 887 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3236885 | 1 | 121.4710979365 | 31.1477024255 | 276 | 11 | 11 | 21.8 | TDD | 297 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3240900 | 2 | 121.4689386347 | 31.1548076451 | 159 | 1 | 0 | 18.7 | TDD | 813 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.024 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.045 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.178 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.178 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.403 | NREventA2 | measId:1;ServCellPCI:287;Se... |
| 2024-09-20 22:21:34.549 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236885 | 1 | 18.1431 | 18.1595 | -115.0376 | 8.0478 | 161.7080 | 0.1253 | 0.0164 |
| 2024_09_20 22:00 | 3240900 | 2 | 19.9808 | 15.9203 | -115.0927 | 16.5400 | 197.6104 | 0.0197 | 0.0030 |
| 2024_09_20 22:00 | 3217788 | 3 | 17.4126 | 12.9714 | -114.4498 | 17.0117 | 179.9830 | 0.0080 | 0.0118 |
| 2024_09_20 22:00 | 3234597 | 4 | 19.4959 | 11.9766 | -117.4730 | 12.9915 | 190.3256 | 0.0020 | 0.0105 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416608_7717BC55 | 504990 | 297 | -99.4 | 504990 | 813 | -103.2 | 504990 | 885 | -107.7 | 504990 | 887 |
| MR_1774416608_E3C4502D | 504990 | 297 | -101.3 | 504990 | 813 | -105.6 | 504990 | 885 | -107.2 | 504990 | 887 |
| MR_1774416608_99B24AE5 | 504990 | 297 | -100.7 | 504990 | 813 | -104.3 | 504990 | 885 | -108.4 | 504990 | 887 |
| MR_1774416608_029A3D6D | 504990 | 297 | -103.1 | 504990 | 813 | -102.3 | 504990 | 885 | -108.4 | 504990 | 887 |
| MR_1774416608_E8C5DF0C | 504990 | 297 | -100.1 | 504990 | 813 | -106.0 | 504990 | 885 | -110.8 | 504990 | 887 |
| MR_1774416608_5361CB3C | 504990 | 297 | -100.4 | 504990 | 813 | -103.5 | 504990 | 885 | -108.1 | 504990 | 887 |
| MR_1774416608_2777B3B3 | 504990 | 297 | -100.7 | 504990 | 813 | -105.9 | 504990 | 885 | -107.3 | 504990 | 887 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1712: `794ca723-f3d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `794ca723-f3d6-4d5b-bdcd-d08d840911bd` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236555_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1712] topology](images/train_1712.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3236555_5
- `C2`: Decrease A3 Offset threshold for 3260015_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260015_1
- `C4`: Decrease A3 Offset threshold for 3236555_5
- `C5`: Add neighbor relationship between 3267906_8 and 3260015_1
- `C6`: Lift the tilt angle of 3236555_5 by 4 degrees
- `C7`: Press down the tilt angle  of 3260015_1 by 5 degrees
- `C8`: Adjust the azimuth of 3236555_5 by 22 degrees
- `C9`: Adjust the azimuth of 3260015_1 by 25 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236555_5
- `C11`: Press down the tilt angle of 3236555_5 by 4 degrees
- `C12`: Lift the tilt angle  of 3260015_1 by 5 degrees
- `C13`: Increase transmission power for 3260015_1
- `C14`: Increase A3 Offset threshold for 3236555_5
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260015_1
- `C16`: Decrease transmission power for 3260015_1
- `C17`: Add neighbor relationship between 3236555_5 and 3260015_1
- `C18`: Increase A3 Offset threshold for 3260015_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236555_5 **← 정답**
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase transmission power for 3236555_5
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.636 | MS1 | 121.4656654405 | 31.1446235476 | 861 | 504990 | -93.90 | 13.93 | 437.22 | 0.04 | 2.26 | 1567 |
| 2024-09-20 22:21:32.748 | MS1 | 121.4656598320 | 31.1446357505 | 569 | 504990 | -94.10 | 12.84 | 324.52 | 0.14 | 2.32 | 1600 |
| 2024-09-20 22:21:33.499 | MS1 | 121.4656688779 | 31.1446243276 | 887 | 504990 | -95.11 | 11.45 | 362.76 | 0.15 | 2.36 | 1589 |
| 2024-09-20 22:21:34.662 | MS1 | 121.4656580181 | 31.1446351153 | 523 | 152650 | -94.77 | 4.38 | 100.59 | 0.07 | 1.72 | 912 |
| 2024-09-20 22:21:35.193 | MS1 | 121.4656699978 | 31.1446243425 | 274 | 152650 | -94.77 | 2.31 | 85.61 | 0.12 | 1.78 | 981 |
| 2024-09-20 22:21:36.383 | MS1 | 121.4656742986 | 31.1446360083 | 933 | 152650 | -96.13 | 5.22 | 63.59 | 0.12 | 1.90 | 938 |
| 2024-09-20 22:21:37.312 | MS1 | 121.4656689713 | 31.1446181021 | 62 | 152650 | -87.66 | 2.04 | 71.66 | 0.15 | 1.76 | 986 |
| 2024-09-20 22:21:38.351 | MS1 | 121.4656716656 | 31.1446351899 | 523 | 152650 | -91.90 | 7.41 | 74.91 | 0.11 | 1.70 | 960 |
| 2024-09-20 22:21:39.419 | MS1 | 121.4656685640 | 31.1446211744 | 274 | 152650 | -89.82 | 2.42 | 83.36 | 0.20 | 1.76 | 982 |
| 2024-09-20 22:21:40.230 | MS1 | 121.4656674259 | 31.1446248502 | 933 | 152650 | -93.64 | 2.33 | 67.54 | 0.13 | 2.37 | 1569 |
| 2024-09-20 22:21:41.515 | MS1 | 121.4656595165 | 31.1446365347 | 62 | 152650 | -95.52 | 7.54 | 55.20 | 0.05 | 2.25 | 1576 |
| 2024-09-20 22:21:42.758 | MS1 | 121.4656692670 | 31.1446293789 | 523 | 152650 | -93.93 | 2.50 | 60.90 | 0.06 | 2.62 | 1581 |

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
| 3215003 | 9 | 121.4640057850 | 31.1462186795 | 133 | 2 | 1 | 18.6 | FDD | 523 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3221915 | 3 | 121.4747352335 | 31.1538209160 | 47 | 12 | 11 | 6.8 | TDD | 343 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3224441 | 11 | 121.4689387449 | 31.1527619049 | 18 | 5 | 8 | 1.6 | FDD | 274 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3231411 | 7 | 121.4718329203 | 31.1493324737 | 73 | 7 | 6 | 18.4 | FDD | 357 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3236555 | 5 | 121.4670600718 | 31.1517715058 | 212 | 3 | 0 | 16.4 | TDD | 861 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3238500 | 6 | 121.4719459558 | 31.1537646305 | 15 | 6 | 4 | 16.3 | TDD | 607 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3247020 | 12 | 121.4698176224 | 31.1488964554 | 208 | 12 | 2 | 5.1 | FDD | 370 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3260015 | 1 | 121.4703281657 | 31.1525618095 | 182 | 4 | 12 | 11.8 | TDD | 942 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3261961 | 13 | 121.4659601420 | 31.1482873932 | 197 | 10 | 9 | 29.5 | FDD | 62 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3267906 | 8 | 121.4733379945 | 31.1536638549 | 326 | 13 | 3 | 9.4 | FDD | 933 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3268551 | 2 | 121.4727854902 | 31.1519527910 | 29 | 7 | 6 | 20.6 | TDD | 887 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3273074 | 4 | 121.4731818959 | 31.1556745852 | 219 | 10 | 6 | 16.9 | TDD | 569 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3275440 | 10 | 121.4673326814 | 31.1493902907 | 5 | 11 | 4 | 29.9 | FDD | 766 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |

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
| 2024-09-20 22:21:31.513 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.663 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.663 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.351 | NREventA2 | measId:1;ServCellPCI:437;Se... |
| 2024-09-20 22:21:35.471 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.744 | NREventA5 | measId:3;ServCellPCI:437;Se... |
| 2024-09-20 22:21:35.775 | NRHandoverAttempt | SourcePCI:437;SourceNR-ARFC... |
| 2024-09-20 22:21:35.820 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.835 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.941 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.941 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260015 | 1 | 13.7600 | 11.0238 | -116.8482 | 6.6264 | 189.0692 | 0.0070 | 0.0162 |
| 2024_09_20 22:00 | 3268551 | 2 | 18.2074 | 12.3061 | -116.9433 | 17.0094 | 107.1943 | 0.0166 | 0.0150 |
| 2024_09_20 22:00 | 3221915 | 3 | 12.4476 | 19.1257 | -114.6649 | 14.7199 | 110.5527 | 0.0068 | 0.0026 |
| 2024_09_20 22:00 | 3273074 | 4 | 11.6677 | 14.1872 | -115.5190 | 6.8591 | 146.6153 | 0.0146 | 0.0011 |
| 2024_09_20 22:00 | 3236555 | 5 | 14.4219 | 5.7306 | -116.6958 | 11.4826 | 137.6023 | 0.0146 | 0.0085 |
| 2024_09_20 22:00 | 3238500 | 6 | 15.5765 | 19.3021 | -116.7079 | 7.2921 | 90.6156 | 0.0181 | 0.0084 |
| 2024_09_20 22:00 | 3231411 | 7 | 19.2779 | 7.3642 | -115.2295 | 3.7484 | 50.4329 | 0.0094 | 0.0164 |
| 2024_09_20 22:00 | 3267906 | 8 | 13.6051 | 14.4242 | -117.8435 | 4.3933 | 59.8917 | 0.0020 | 0.0040 |
| 2024_09_20 22:00 | 3215003 | 9 | 7.3412 | 17.8297 | -114.0310 | 4.2414 | 32.4549 | 0.0046 | 0.0130 |
| 2024_09_20 22:00 | 3275440 | 10 | 11.2379 | 11.1374 | -116.4705 | 3.6375 | 25.9995 | 0.0120 | 0.0105 |
| 2024_09_20 22:00 | 3224441 | 11 | 18.5875 | 17.3538 | -115.0475 | 3.6337 | 23.1222 | 0.0030 | 0.0117 |
| 2024_09_20 22:00 | 3247020 | 12 | 6.6460 | 9.9136 | -115.5378 | 4.3806 | 32.4365 | 0.0032 | 0.0113 |
| 2024_09_20 22:00 | 3261961 | 13 | 13.9376 | 14.4241 | -116.8360 | 4.8794 | 37.3601 | 0.0160 | 0.0151 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412241_2152C225 | 504990 | 887 | -96.8 | 504990 | 942 | -95.3 | 504990 | 343 | -101.6 | 504990 | 607 |
| MR_1774412241_0F7D302A | 152650 | 274 | -95.6 | 152650 | 357 | -97.0 | 152650 | 766 | -103.4 | 152650 | 370 |
| MR_1774412241_F9A2F108 | 152650 | 274 | -94.6 | 152650 | 357 | -98.3 | 152650 | 766 | -105.9 | 152650 | 370 |
| MR_1774412241_314B47B4 | 504990 | 887 | -93.3 | 504990 | 942 | -98.0 | 504990 | 343 | -102.7 | 504990 | 607 |
| MR_1774412241_AD6E529E | 504990 | 887 | -95.3 | 504990 | 942 | -95.2 | 504990 | 343 | -102.5 | 504990 | 607 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1713: `a5320a80-9b5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a5320a80-9b52-4857-8af6-2a915a568fb2` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease A3 Offset threshold for 3252809_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1713] topology](images/train_1713.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3252809_1
- `C2`: Check test server and transmission issues
- `C3`: Decrease A3 Offset threshold for 3252809_1 **← 정답**
- `C4`: Adjust the azimuth of 3252809_1 by 50 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238908_3
- `C7`: Decrease transmission power for 3238908_3
- `C8`: Decrease A3 Offset threshold for 3238908_3
- `C9`: Adjust the azimuth of 3238908_3 by 50 degrees
- `C10`: Add neighbor relationship between 3258283_2 and 3238908_3
- `C11`: Increase A3 Offset threshold for 3252809_1
- `C12`: Add neighbor relationship between 3252809_1 and 3238908_3
- `C13`: Increase A3 Offset threshold for 3238908_3
- `C14`: Press down the tilt angle of 3252809_1 by 10 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252809_1
- `C16`: Increase transmission power for 3238908_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238908_3
- `C18`: Lift the tilt angle of 3252809_1 by 10 degrees
- `C19`: Increase transmission power for 3252809_1
- `C20`: Press down the tilt angle  of 3238908_3 by 9 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252809_1
- `C22`: Lift the tilt angle  of 3238908_3 by 9 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.273 | MS1 | 121.4656702203 | 31.1446293801 | 752 | 504990 | -77.16 | 16.15 | 594.82 | 0.01 | 2.30 | 1593 |
| 2024-09-20 22:21:32.883 | MS1 | 121.4656656044 | 31.1446254466 | 752 | 504990 | -80.10 | 14.32 | 362.25 | 0.08 | 2.49 | 1570 |
| 2024-09-20 22:21:33.495 | MS1 | 121.4656731869 | 31.1446234340 | 752 | 504990 | -79.32 | 14.24 | 522.78 | 0.01 | 2.55 | 1570 |
| 2024-09-20 22:21:34.861 | MS1 | 121.4656696255 | 31.1446362100 | 752 | 504990 | -86.04 | -1.30 | 67.41 | 0.01 | 1.41 | 1577 |
| 2024-09-20 22:21:35.862 | MS1 | 121.4656761743 | 31.1446255417 | 752 | 504990 | -88.26 | -0.29 | 46.72 | 0.04 | 1.14 | 1572 |
| 2024-09-20 22:21:36.129 | MS1 | 121.4656676664 | 31.1446185195 | 752 | 504990 | -86.98 | -0.32 | 82.49 | 0.16 | 1.12 | 1562 |
| 2024-09-20 22:21:37.134 | MS1 | 121.4656638175 | 31.1446285002 | 752 | 504990 | -84.89 | -2.28 | 42.49 | 0.17 | 1.06 | 1574 |
| 2024-09-20 22:21:38.421 | MS1 | 121.4656633537 | 31.1446223103 | 752 | 504990 | -92.18 | -1.96 | 66.64 | 0.14 | 1.35 | 1585 |
| 2024-09-20 22:21:39.320 | MS1 | 121.4656642522 | 31.1446183313 | 296 | 504990 | -79.45 | 14.04 | 215.48 | 0.12 | 1.23 | 1597 |
| 2024-09-20 22:21:40.411 | MS1 | 121.4656623419 | 31.1446315533 | 296 | 504990 | -84.45 | 16.26 | 545.70 | 0.12 | 2.91 | 1561 |
| 2024-09-20 22:21:41.874 | MS1 | 121.4656630905 | 31.1446268520 | 296 | 504990 | -75.97 | 13.07 | 532.96 | 0.14 | 2.01 | 1571 |
| 2024-09-20 22:21:42.223 | MS1 | 121.4656724178 | 31.1446288142 | 296 | 504990 | -76.17 | 15.94 | 398.60 | 0.15 | 2.21 | 1600 |

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
| 3238908 | 3 | 121.4642997838 | 31.1492761443 | 356 | 6 | 1 | 30.0 | TDD | 296 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3252809 | 1 | 121.4735690822 | 31.1456916675 | 89 | 14 | 10 | 39.9 | TDD | 752 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3258283 | 2 | 121.4711814216 | 31.1523627466 | 162 | 3 | 3 | 15.3 | TDD | 793 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3279969 | 4 | 121.4722585237 | 31.1486251405 | 31 | 5 | 11 | 35.1 | TDD | 716 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.000 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.019 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.148 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.148 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.860 | NREventA3 | measId:2;ServCellPCI:308;Se... |
| 2024-09-20 22:21:38.100 | NRHandoverAttempt | SourcePCI:308;SourceNR-ARFC... |
| 2024-09-20 22:21:38.141 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.156 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.292 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.292 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252809 | 1 | 13.8052 | 5.8881 | -117.8993 | 5.7449 | 138.8537 | 0.0016 | 0.1839 |
| 2024_09_20 22:00 | 3258283 | 2 | 13.0198 | 10.9911 | -116.1930 | 12.8620 | 82.6094 | 0.0003 | 0.0109 |
| 2024_09_20 22:00 | 3238908 | 3 | 17.6872 | 16.4821 | -117.5122 | 5.5888 | 183.7665 | 0.0025 | 0.0128 |
| 2024_09_20 22:00 | 3279969 | 4 | 16.6610 | 16.5323 | -116.9429 | 19.7743 | 156.1760 | 0.0143 | 0.0117 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416713_65A5E34A | 504990 | 296 | -81.3 | 504990 | 752 | -85.8 | 504990 | 793 | -91.5 | 504990 | 716 |
| MR_1774416713_716C53B3 | 504990 | 296 | -80.1 | 504990 | 752 | -87.9 | 504990 | 793 | -89.5 | 504990 | 716 |
| MR_1774416713_509C2298 | 504990 | 296 | -82.0 | 504990 | 752 | -87.1 | 504990 | 793 | -89.8 | 504990 | 716 |
| MR_1774416713_C31E6648 | 504990 | 752 | -86.0 | 504990 | 296 | -78.7 | 504990 | 793 | -90.2 | 504990 | 716 |
| MR_1774416713_70C5E086 | 504990 | 296 | -80.3 | 504990 | 752 | -86.8 | 504990 | 793 | -89.5 | 504990 | 716 |
| MR_1774416713_B7CE1973 | 504990 | 752 | -84.2 | 504990 | 296 | -79.9 | 504990 | 793 | -89.0 | 504990 | 716 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1714: `f2301a64-2e2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f2301a64-2e2e-422e-b163-c89059a68ea2` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1714] topology](images/train_1714.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3246771_4
- `C2`: Press down the tilt angle of 3246771_4 by 5 degrees
- `C3`: Press down the tilt angle  of 3214760_2 by 10 degrees
- `C4`: Increase transmission power for 3246771_4
- `C5`: Adjust the azimuth of 3214760_2 by 50 degrees
- `C6`: Decrease transmission power for 3246771_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246771_4
- `C8`: Check test server and transmission issues **← 정답**
- `C9`: Lift the tilt angle of 3246771_4 by 5 degrees
- `C10`: Add neighbor relationship between 3265804_1 and 3214760_2
- `C11`: Add neighbor relationship between 3246771_4 and 3214760_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease transmission power for 3214760_2
- `C14`: Increase transmission power for 3214760_2
- `C15`: Decrease A3 Offset threshold for 3214760_2
- `C16`: Increase A3 Offset threshold for 3246771_4
- `C17`: Adjust the azimuth of 3246771_4 by 50 degrees
- `C18`: Lift the tilt angle  of 3214760_2 by 10 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246771_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214760_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214760_2
- `C22`: Increase A3 Offset threshold for 3214760_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.839 | MS1 | 121.4656661001 | 31.1446252104 | 502 | 504990 | -86.40 | 17.82 | 419.35 | 0.19 | 2.71 | 1576 |
| 2024-09-20 22:21:32.935 | MS1 | 121.4656740862 | 31.1446362378 | 502 | 504990 | -91.89 | 13.27 | 434.73 | 0.18 | 2.95 | 1565 |
| 2024-09-20 22:21:33.710 | MS1 | 121.4656640040 | 31.1446276252 | 502 | 504990 | -90.82 | 12.42 | 367.40 | 0.17 | 2.29 | 1588 |
| 2024-09-20 22:21:34.251 | MS1 | 121.4656649281 | 31.1446199346 | 502 | 504990 | -91.18 | 17.44 | 53.89 | 0.02 | 2.94 | 427 |
| 2024-09-20 22:21:35.808 | MS1 | 121.4656699308 | 31.1446260535 | 502 | 504990 | -88.21 | 13.56 | 79.66 | 0.15 | 2.21 | 403 |
| 2024-09-20 22:21:36.785 | MS1 | 121.4656753195 | 31.1446219902 | 502 | 504990 | -85.10 | 13.50 | 85.44 | 0.06 | 2.26 | 497 |
| 2024-09-20 22:21:37.848 | MS1 | 121.4656727843 | 31.1446334758 | 502 | 504990 | -92.93 | 12.45 | 81.38 | 0.07 | 2.74 | 497 |
| 2024-09-20 22:21:38.983 | MS1 | 121.4656662920 | 31.1446326670 | 502 | 504990 | -93.09 | 11.18 | 82.66 | 0.01 | 2.93 | 352 |
| 2024-09-20 22:21:39.952 | MS1 | 121.4656655151 | 31.1446280131 | 502 | 504990 | -90.56 | 10.05 | 67.79 | 0.13 | 2.80 | 444 |
| 2024-09-20 22:21:40.355 | MS1 | 121.4656613320 | 31.1446188464 | 502 | 504990 | -93.61 | 8.28 | 397.48 | 0.00 | 2.44 | 1591 |
| 2024-09-20 22:21:41.155 | MS1 | 121.4656728419 | 31.1446252699 | 502 | 504990 | -90.81 | 11.79 | 506.79 | 0.04 | 2.30 | 1591 |
| 2024-09-20 22:21:42.387 | MS1 | 121.4656769964 | 31.1446312957 | 502 | 504990 | -93.68 | 9.83 | 474.20 | 0.15 | 2.63 | 1582 |

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
| 3214760 | 2 | 121.4719510271 | 31.1477789321 | 19 | 15 | 1 | 16.3 | TDD | 298 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3246771 | 4 | 121.4683223629 | 31.1510675883 | 22 | 3 | 11 | 31.9 | TDD | 502 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3265804 | 1 | 121.4755218523 | 31.1536111831 | 4 | 6 | 3 | 21.2 | TDD | 960 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3271504 | 3 | 121.4653354455 | 31.1471097657 | 33 | 14 | 2 | 36.0 | TDD | 762 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.443 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.468 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.575 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.575 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.275 | NREventA3 | measId:2;ServCellPCI:22;Ser... |
| 2024-09-20 22:21:38.515 | NRHandoverAttempt | SourcePCI:22;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.563 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.574 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.675 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.675 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265804 | 1 | 18.7428 | 15.7100 | -115.2538 | 10.5254 | 117.5730 | 0.0096 | 0.0062 |
| 2024_09_20 22:00 | 3214760 | 2 | 10.2299 | 8.8573 | -115.7505 | 19.8215 | 129.0972 | 0.0078 | 0.0102 |
| 2024_09_20 22:00 | 3271504 | 3 | 15.4147 | 16.1508 | -117.3030 | 13.3179 | 104.8240 | 0.0111 | 0.0118 |
| 2024_09_20 22:00 | 3246771 | 4 | 9.4398 | 16.7144 | -116.7426 | 17.2972 | 175.4335 | 0.0158 | 0.0063 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412826_8C7301FF | 504990 | 502 | -90.1 | 504990 | 298 | -101.5 | 504990 | 960 | -105.3 | 504990 | 762 |
| MR_1774412826_585CB2A1 | 504990 | 502 | -90.6 | 504990 | 298 | -98.6 | 504990 | 960 | -103.7 | 504990 | 762 |
| MR_1774412826_9C85D7FE | 504990 | 502 | -90.0 | 504990 | 298 | -98.9 | 504990 | 960 | -105.2 | 504990 | 762 |
| MR_1774412826_87B68C04 | 504990 | 502 | -89.6 | 504990 | 298 | -98.5 | 504990 | 960 | -104.4 | 504990 | 762 |
| MR_1774412826_7CEABBDA | 504990 | 502 | -89.9 | 504990 | 298 | -99.5 | 504990 | 960 | -105.1 | 504990 | 762 |
| MR_1774412826_EE61C46B | 504990 | 502 | -91.4 | 504990 | 298 | -98.7 | 504990 | 960 | -102.0 | 504990 | 762 |
| MR_1774412826_4ADCBAB7 | 504990 | 502 | -92.1 | 504990 | 298 | -98.6 | 504990 | 960 | -103.2 | 504990 | 762 |
| MR_1774412826_62E46C5C | 504990 | 502 | -91.6 | 504990 | 298 | -99.7 | 504990 | 960 | -104.0 | 504990 | 762 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1715: `6c151a05-322...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6c151a05-3225-421c-8bfb-b37fc1c88fa1` |
| Tag | **multiple-answer** |
| 정답 | **C5|C16** |
| C5 의미 | Adjust the azimuth of 3210896_3 by 35 degrees |
| C16 의미 | Increase transmission power for 3210896_3 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1715] topology](images/train_1715.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3217454_2 by 3 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217454_2
- `C4`: Add neighbor relationship between 3211107_4 and 3217454_2
- `C5`: Adjust the azimuth of 3210896_3 by 35 degrees **← 정답**
- `C6`: Decrease A3 Offset threshold for 3210896_3
- `C7`: Lift the tilt angle of 3210896_3 by 10 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217454_2
- `C9`: Increase transmission power for 3217454_2
- `C10`: Press down the tilt angle  of 3217454_2 by 3 degrees
- `C11`: Decrease transmission power for 3217454_2
- `C12`: Adjust the azimuth of 3217454_2 by 10 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210896_3
- `C14`: Increase A3 Offset threshold for 3217454_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210896_3
- `C16`: Increase transmission power for 3210896_3 **← 정답**
- `C17`: Add neighbor relationship between 3210896_3 and 3217454_2
- `C18`: Increase A3 Offset threshold for 3210896_3
- `C19`: Check test server and transmission issues
- `C20`: Decrease transmission power for 3210896_3
- `C21`: Decrease A3 Offset threshold for 3217454_2
- `C22`: Press down the tilt angle of 3210896_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.449 | MS1 | 121.4656751667 | 31.1446298321 | 420 | 504990 | -90.32 | 15.47 | 465.48 | 0.12 | 2.71 | 1590 |
| 2024-09-20 22:21:32.317 | MS1 | 121.4656641090 | 31.1446263916 | 420 | 504990 | -88.21 | 13.49 | 398.26 | 0.08 | 2.15 | 1597 |
| 2024-09-20 22:21:33.454 | MS1 | 121.4656586828 | 31.1446354562 | 420 | 504990 | -90.87 | 15.92 | 581.31 | 0.18 | 2.53 | 1564 |
| 2024-09-20 22:21:34.455 | MS1 | 121.4656698595 | 31.1446244144 | 420 | 504990 | -108.37 | 1.18 | 13.61 | 0.13 | 1.32 | 1590 |
| 2024-09-20 22:21:35.529 | MS1 | 121.4656626926 | 31.1446248024 | 420 | 504990 | -101.74 | 1.70 | 52.24 | 0.14 | 1.46 | 1561 |
| 2024-09-20 22:21:36.119 | MS1 | 121.4656690731 | 31.1446308455 | 420 | 504990 | -100.48 | -0.68 | 73.95 | 0.14 | 1.12 | 1579 |
| 2024-09-20 22:21:37.781 | MS1 | 121.4656621088 | 31.1446351903 | 420 | 504990 | -102.28 | 1.16 | 25.92 | 0.07 | 1.38 | 1588 |
| 2024-09-20 22:21:38.942 | MS1 | 121.4656676228 | 31.1446370108 | 420 | 504990 | -106.39 | 0.48 | 30.28 | 0.05 | 1.31 | 1593 |
| 2024-09-20 22:21:39.174 | MS1 | 121.4656584969 | 31.1446225674 | 420 | 504990 | -102.86 | -0.73 | 57.29 | 0.10 | 1.31 | 1577 |
| 2024-09-20 22:21:40.125 | MS1 | 121.4656767444 | 31.1446314566 | 420 | 504990 | -94.01 | 15.95 | 354.13 | 0.01 | 2.48 | 1562 |
| 2024-09-20 22:21:41.542 | MS1 | 121.4656696179 | 31.1446375189 | 420 | 504990 | -89.26 | 13.08 | 398.69 | 0.04 | 2.87 | 1570 |
| 2024-09-20 22:21:42.107 | MS1 | 121.4656654581 | 31.1446198554 | 420 | 504990 | -90.75 | 15.56 | 525.61 | 0.09 | 2.59 | 1576 |

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
| 3210896 | 3 | 121.4756624741 | 31.1527214597 | 262 | 9 | 5 | 42.3 | TDD | 420 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3211107 | 4 | 121.4743336903 | 31.1443809420 | 21 | 9 | 3 | 27.8 | TDD | 553 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3217454 | 2 | 121.4647680285 | 31.1508659286 | 183 | 1 | 6 | 26.0 | TDD | 841 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3278609 | 1 | 121.4704599693 | 31.1499768086 | 298 | 4 | 6 | 18.0 | TDD | 768 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.350 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.373 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.492 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.492 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.741 | NREventA2 | measId:1;ServCellPCI:379;Se... |
| 2024-09-20 22:21:34.890 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278609 | 1 | 18.3423 | 16.6886 | -114.8885 | 10.3513 | 191.6455 | 0.0144 | 0.0156 |
| 2024_09_20 22:00 | 3217454 | 2 | 19.6883 | 11.3813 | -114.8408 | 11.3059 | 137.7006 | 0.0113 | 0.0129 |
| 2024_09_20 22:00 | 3210896 | 3 | 14.6786 | 19.7930 | -114.2791 | 15.0562 | 87.5234 | 0.1449 | 0.0156 |
| 2024_09_20 22:00 | 3211107 | 4 | 9.7637 | 7.1885 | -114.1427 | 10.1257 | 121.5511 | 0.0098 | 0.0095 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414788_9ECD741F | 504990 | 420 | -109.1 | 504990 | 841 | -114.1 | 504990 | 553 | -117.5 | 504990 | 768 |
| MR_1774414788_356804F6 | 504990 | 420 | -107.2 | 504990 | 841 | -112.4 | 504990 | 553 | -118.2 | 504990 | 768 |
| MR_1774414788_35AB716E | 504990 | 420 | -107.4 | 504990 | 841 | -111.7 | 504990 | 553 | -116.5 | 504990 | 768 |
| MR_1774414788_C53699D0 | 504990 | 420 | -106.7 | 504990 | 841 | -111.0 | 504990 | 553 | -118.5 | 504990 | 768 |
| MR_1774414788_F526FAE6 | 504990 | 420 | -107.3 | 504990 | 841 | -112.9 | 504990 | 553 | -115.2 | 504990 | 768 |
| MR_1774414788_77C04B7D | 504990 | 420 | -110.2 | 504990 | 841 | -114.5 | 504990 | 553 | -117.9 | 504990 | 768 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1716: `84ac1e3b-348...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `84ac1e3b-3488-4a53-8803-78a173d18107` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3224407_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1716] topology](images/train_1716.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3259463_1
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase transmission power for 3259463_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224407_2
- `C5`: Decrease A3 Offset threshold for 3259463_1
- `C6`: Lift the tilt angle  of 3259463_1 by 10 degrees
- `C7`: Press down the tilt angle of 3224407_2 by 5 degrees
- `C8`: Check test server and transmission issues
- `C9`: Add neighbor relationship between 3224407_2 and 3259463_1
- `C10`: Add neighbor relationship between 3273592_3 and 3259463_1
- `C11`: Adjust the azimuth of 3259463_1 by 50 degrees
- `C12`: Increase transmission power for 3224407_2
- `C13`: Press down the tilt angle  of 3259463_1 by 10 degrees
- `C14`: Decrease transmission power for 3259463_1
- `C15`: Decrease A3 Offset threshold for 3224407_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259463_1
- `C17`: Adjust the azimuth of 3224407_2 by 8 degrees
- `C18`: Lift the tilt angle of 3224407_2 by 5 degrees
- `C19`: Increase A3 Offset threshold for 3224407_2
- `C20`: Decrease transmission power for 3224407_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224407_2 **← 정답**
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259463_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.785 | MS1 | 121.4656705327 | 31.1446188686 | 437 | 504990 | -86.62 | 13.98 | 459.58 | 0.17 | 2.23 | 1589 |
| 2024-09-20 22:21:32.806 | MS1 | 121.4656774754 | 31.1446215790 | 437 | 504990 | -87.74 | 16.63 | 460.21 | 0.00 | 2.84 | 1594 |
| 2024-09-20 22:21:33.737 | MS1 | 121.4656667490 | 31.1446284259 | 437 | 504990 | -86.58 | 12.51 | 424.01 | 0.10 | 2.03 | 1564 |
| 2024-09-20 22:21:34.620 | MS1 | 121.4656652240 | 31.1446180068 | 437 | 504990 | -89.23 | 15.20 | 67.96 | 0.65 | 2.54 | 603 |
| 2024-09-20 22:21:35.447 | MS1 | 121.4656768128 | 31.1446321694 | 437 | 504990 | -88.28 | 17.01 | 68.52 | 0.67 | 2.10 | 700 |
| 2024-09-20 22:21:36.838 | MS1 | 121.4656710936 | 31.1446334228 | 437 | 504990 | -87.08 | 12.64 | 57.29 | 0.52 | 2.70 | 561 |
| 2024-09-20 22:21:37.343 | MS1 | 121.4656630980 | 31.1446225309 | 437 | 504990 | -93.45 | 10.45 | 87.68 | 0.54 | 2.09 | 550 |
| 2024-09-20 22:21:38.967 | MS1 | 121.4656712469 | 31.1446187312 | 437 | 504990 | -93.64 | 7.42 | 61.38 | 0.53 | 2.39 | 639 |
| 2024-09-20 22:21:39.223 | MS1 | 121.4656662365 | 31.1446194308 | 437 | 504990 | -90.69 | 11.37 | 91.05 | 0.50 | 2.49 | 656 |
| 2024-09-20 22:21:40.563 | MS1 | 121.4656685842 | 31.1446282356 | 437 | 504990 | -93.06 | 10.40 | 388.52 | 0.06 | 2.19 | 1577 |
| 2024-09-20 22:21:41.900 | MS1 | 121.4656737583 | 31.1446247889 | 437 | 504990 | -90.62 | 12.69 | 545.84 | 0.12 | 2.88 | 1568 |
| 2024-09-20 22:21:42.446 | MS1 | 121.4656717578 | 31.1446232768 | 437 | 504990 | -93.26 | 8.96 | 443.31 | 0.05 | 2.93 | 1561 |

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
| 3217561 | 4 | 121.4646726378 | 31.1493681019 | 176 | 9 | 6 | 24.6 | TDD | 909 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3224407 | 2 | 121.4722043025 | 31.1555392322 | 199 | 4 | 4 | 30.0 | TDD | 437 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3259463 | 1 | 121.4743645300 | 31.1526858772 | 39 | 10 | 9 | 28.1 | TDD | 194 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3273592 | 3 | 121.4643794429 | 31.1541358634 | 259 | 3 | 0 | 46.8 | TDD | 630 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.892 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.910 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.049 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.049 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.759 | NREventA3 | measId:2;ServCellPCI:762;Se... |
| 2024-09-20 22:21:37.999 | NRHandoverAttempt | SourcePCI:762;SourceNR-ARFC... |
| 2024-09-20 22:21:38.044 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.059 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.178 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.178 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259463 | 1 | 6.4660 | 14.3865 | -117.1385 | 10.2421 | 93.6585 | 0.0083 | 0.0008 |
| 2024_09_20 22:00 | 3224407 | 2 | 7.3050 | 16.8701 | -116.9187 | 13.1903 | 85.9608 | 0.0192 | 0.0067 |
| 2024_09_20 22:00 | 3273592 | 3 | 18.6494 | 6.4666 | -114.4689 | 13.6905 | 190.4723 | 0.0053 | 0.0029 |
| 2024_09_20 22:00 | 3217561 | 4 | 12.4700 | 14.3233 | -114.1391 | 5.0762 | 158.7674 | 0.0185 | 0.0086 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413446_D9291DBB | 504990 | 437 | -90.6 | 504990 | 194 | -94.4 | 504990 | 630 | -103.0 | 504990 | 909 |
| MR_1774413446_53E9E2D2 | 504990 | 437 | -90.3 | 504990 | 194 | -95.1 | 504990 | 630 | -102.2 | 504990 | 909 |
| MR_1774413446_718C62CF | 504990 | 437 | -88.5 | 504990 | 194 | -94.2 | 504990 | 630 | -102.7 | 504990 | 909 |
| MR_1774413446_75554FF3 | 504990 | 437 | -90.0 | 504990 | 194 | -94.0 | 504990 | 630 | -105.0 | 504990 | 909 |
| MR_1774413446_BB44CA19 | 504990 | 437 | -90.1 | 504990 | 194 | -94.6 | 504990 | 630 | -104.1 | 504990 | 909 |
| MR_1774413446_C2780638 | 504990 | 437 | -87.6 | 504990 | 194 | -96.1 | 504990 | 630 | -103.0 | 504990 | 909 |
| MR_1774413446_BE121730 | 504990 | 437 | -87.5 | 504990 | 194 | -94.3 | 504990 | 630 | -104.5 | 504990 | 909 |
| MR_1774413446_3BEE869F | 504990 | 437 | -88.6 | 504990 | 194 | -96.2 | 504990 | 630 | -103.5 | 504990 | 909 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1717: `ee99a715-821...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ee99a715-8216-4590-bc60-4d7747dda7d8` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1717] topology](images/train_1717.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease A3 Offset threshold for 3253238_1
- `C3`: Decrease A3 Offset threshold for 3277730_3
- `C4`: Increase transmission power for 3253238_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277730_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253238_1
- `C7`: Press down the tilt angle of 3253238_1 by 6 degrees
- `C8`: Adjust the azimuth of 3277730_3 by 50 degrees
- `C9`: Add neighbor relationship between 3217660_4 and 3277730_3
- `C10`: Increase transmission power for 3277730_3
- `C11`: Decrease transmission power for 3253238_1
- `C12`: Lift the tilt angle of 3253238_1 by 6 degrees
- `C13`: Increase A3 Offset threshold for 3253238_1
- `C14`: Increase A3 Offset threshold for 3277730_3
- `C15`: Decrease transmission power for 3277730_3
- `C16`: Add neighbor relationship between 3253238_1 and 3277730_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277730_3
- `C18`: Lift the tilt angle  of 3277730_3 by 8 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253238_1
- `C20`: Press down the tilt angle  of 3277730_3 by 8 degrees
- `C21`: Insufficient data; more data is needed for judgment. **← 정답**
- `C22`: Adjust the azimuth of 3253238_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.152 | MS1 | 121.4656618929 | 31.1446296666 | 315 | 504990 | -86.82 | 12.87 | 399.44 | 0.13 | 2.22 | 1582 |
| 2024-09-20 22:21:32.280 | MS1 | 121.4656733789 | 31.1446213648 | 315 | 504990 | -86.49 | 13.98 | 312.58 | 0.14 | 2.34 | 1567 |
| 2024-09-20 22:21:33.386 | MS1 | 121.4656609688 | 31.1446365876 | 315 | 504990 | -89.33 | 13.14 | 436.26 | 0.19 | 2.37 | 1564 |
| 2024-09-20 22:21:34.138 | MS1 | 121.4656636996 | 31.1446340056 | 315 | 504990 | -89.41 | 15.01 | 83.89 | 0.09 | 2.13 | 1599 |
| 2024-09-20 22:21:35.941 | MS1 | 121.4656588528 | 31.1446199778 | 315 | 504990 | -90.05 | 14.03 | 56.59 | 0.10 | 2.08 | 1573 |
| 2024-09-20 22:21:36.218 | MS1 | 121.4656680561 | 31.1446199213 | 315 | 504990 | -86.89 | 17.38 | 85.81 | 0.08 | 2.41 | 1597 |
| 2024-09-20 22:21:37.518 | MS1 | 121.4656745809 | 31.1446252793 | 315 | 504990 | -90.73 | 7.80 | 89.57 | 0.13 | 2.10 | 1571 |
| 2024-09-20 22:21:38.512 | MS1 | 121.4656741928 | 31.1446192352 | 315 | 504990 | -90.85 | 8.58 | 79.66 | 0.13 | 2.52 | 1589 |
| 2024-09-20 22:21:39.297 | MS1 | 121.4656625738 | 31.1446260687 | 315 | 504990 | -93.03 | 12.25 | 94.96 | 0.16 | 2.95 | 1576 |
| 2024-09-20 22:21:40.978 | MS1 | 121.4656754319 | 31.1446314813 | 315 | 504990 | -92.16 | 10.58 | 427.64 | 0.09 | 2.95 | 1569 |
| 2024-09-20 22:21:41.399 | MS1 | 121.4656724910 | 31.1446353584 | 315 | 504990 | -90.54 | 10.20 | 374.35 | 0.04 | 2.49 | 1583 |
| 2024-09-20 22:21:42.459 | MS1 | 121.4656717697 | 31.1446190675 | 315 | 504990 | -90.70 | 9.30 | 508.97 | 0.05 | 2.80 | 1577 |

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
| 3217660 | 4 | 121.4700246647 | 31.1485291792 | 243 | 2 | 0 | 37.0 | TDD | 55 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3221290 | 2 | 121.4647555735 | 31.1451820763 | 179 | 4 | 11 | 22.7 | TDD | 964 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3253238 | 1 | 121.4666912488 | 31.1502064159 | 26 | 3 | 4 | 37.7 | TDD | 315 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3277730 | 3 | 121.4714617869 | 31.1505084255 | 79 | 7 | 5 | 15.9 | TDD | 878 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.115 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.140 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.279 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.279 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.915 | NREventA3 | measId:2;ServCellPCI:972;Se... |
| 2024-09-20 22:21:38.155 | NRHandoverAttempt | SourcePCI:972;SourceNR-ARFC... |
| 2024-09-20 22:21:38.201 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.214 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.364 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.364 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3253238 | 1 | 90.3598 | 82.4238 | -115.8522 | 18.8321 | 192.6483 | 0.0198 | 0.0084 |
| 2024_09_19 22:00 | 3221290 | 2 | 80.7978 | 80.4170 | -115.3849 | 8.6618 | 127.6193 | 0.0053 | 0.0138 |
| 2024_09_19 22:00 | 3277730 | 3 | 76.6237 | 77.5174 | -117.5149 | 7.6825 | 182.2465 | 0.0010 | 0.0137 |
| 2024_09_19 22:00 | 3217660 | 4 | 86.4755 | 80.6090 | -117.9850 | 9.3137 | 144.9359 | 0.0104 | 0.0113 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416754_308BB8C1 | 504990 | 315 | -90.3 | 504990 | 878 | -96.1 | 504990 | 55 | -97.6 | 504990 | 964 |
| MR_1774416754_EBC9EEFA | 504990 | 315 | -91.0 | 504990 | 878 | -98.9 | 504990 | 55 | -98.9 | 504990 | 964 |
| MR_1774416754_D058E1D2 | 504990 | 315 | -90.4 | 504990 | 878 | -98.8 | 504990 | 55 | -100.5 | 504990 | 964 |
| MR_1774416754_A722AD17 | 504990 | 315 | -89.6 | 504990 | 878 | -96.7 | 504990 | 55 | -99.2 | 504990 | 964 |
| MR_1774416754_65A0BB4D | 504990 | 315 | -90.3 | 504990 | 878 | -95.4 | 504990 | 55 | -99.8 | 504990 | 964 |
| MR_1774416754_EAB19F83 | 504990 | 315 | -87.8 | 504990 | 878 | -96.7 | 504990 | 55 | -98.0 | 504990 | 964 |
| MR_1774416754_FF298571 | 504990 | 315 | -90.7 | 504990 | 878 | -98.1 | 504990 | 55 | -99.4 | 504990 | 964 |
| MR_1774416754_49106F69 | 504990 | 315 | -90.7 | 504990 | 878 | -97.0 | 504990 | 55 | -99.2 | 504990 | 964 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1718: `65736b93-af0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `65736b93-af05-4da6-9f0c-3b75baa74392` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Add neighbor relationship between 3220415_1 and 3238571_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1718] topology](images/train_1718.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3220415_1
- `C2`: Increase A3 Offset threshold for 3238571_4
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Check test server and transmission issues
- `C5`: Lift the tilt angle  of 3238571_4 by 6 degrees
- `C6`: Increase A3 Offset threshold for 3220415_1
- `C7`: Adjust the azimuth of 3220415_1 by 50 degrees
- `C8`: Decrease A3 Offset threshold for 3220415_1
- `C9`: Decrease transmission power for 3220415_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220415_1
- `C11`: Decrease A3 Offset threshold for 3238571_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220415_1
- `C13`: Lift the tilt angle of 3220415_1 by 10 degrees
- `C14`: Press down the tilt angle of 3220415_1 by 10 degrees
- `C15`: Increase transmission power for 3238571_4
- `C16`: Adjust the azimuth of 3238571_4 by 20 degrees
- `C17`: Add neighbor relationship between 3218013_3 and 3238571_4
- `C18`: Decrease transmission power for 3238571_4
- `C19`: Add neighbor relationship between 3220415_1 and 3238571_4 **← 정답**
- `C20`: Press down the tilt angle  of 3238571_4 by 6 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238571_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238571_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.853 | MS1 | 121.4656764594 | 31.1446273020 | 977 | 504990 | -78.21 | 13.76 | 344.40 | 0.07 | 2.13 | 1578 |
| 2024-09-20 22:21:32.817 | MS1 | 121.4656635107 | 31.1446245183 | 977 | 504990 | -79.33 | 16.51 | 456.65 | 0.18 | 2.05 | 1581 |
| 2024-09-20 22:21:33.799 | MS1 | 121.4656635468 | 31.1446230607 | 977 | 504990 | -83.20 | 15.92 | 463.23 | 0.16 | 2.22 | 1579 |
| 2024-09-20 22:21:34.522 | MS1 | 121.4656691850 | 31.1446348219 | 977 | 504990 | -87.01 | -0.31 | 44.29 | 0.16 | 1.48 | 1562 |
| 2024-09-20 22:21:35.536 | MS1 | 121.4656755475 | 31.1446215263 | 977 | 504990 | -88.73 | -1.75 | 75.95 | 0.07 | 1.30 | 1567 |
| 2024-09-20 22:21:36.383 | MS1 | 121.4656743589 | 31.1446308958 | 977 | 504990 | -93.27 | -2.11 | 49.24 | 0.03 | 1.17 | 1563 |
| 2024-09-20 22:21:37.303 | MS1 | 121.4656643159 | 31.1446275077 | 977 | 504990 | -90.91 | -0.48 | 43.11 | 0.18 | 1.40 | 1573 |
| 2024-09-20 22:21:38.205 | MS1 | 121.4656726936 | 31.1446374240 | 977 | 504990 | -81.32 | 12.11 | 346.12 | 0.11 | 1.06 | 1587 |
| 2024-09-20 22:21:39.340 | MS1 | 121.4656610420 | 31.1446268855 | 977 | 504990 | -77.72 | 15.45 | 505.64 | 0.06 | 1.19 | 1573 |
| 2024-09-20 22:21:40.953 | MS1 | 121.4656761227 | 31.1446218498 | 977 | 504990 | -80.99 | 15.07 | 367.35 | 0.00 | 2.24 | 1561 |
| 2024-09-20 22:21:41.554 | MS1 | 121.4656636251 | 31.1446339214 | 977 | 504990 | -83.28 | 12.37 | 460.81 | 0.14 | 2.76 | 1573 |
| 2024-09-20 22:21:42.172 | MS1 | 121.4656659652 | 31.1446304156 | 977 | 504990 | -80.43 | 15.03 | 496.45 | 0.08 | 2.97 | 1568 |

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
| 3218013 | 3 | 121.4669225865 | 31.1534741458 | 262 | 12 | 6 | 18.8 | TDD | 885 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3220415 | 1 | 121.4704837815 | 31.1519615823 | 289 | 13 | 4 | 38.4 | TDD | 977 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3236495 | 2 | 121.4737836476 | 31.1512330364 | 108 | 8 | 10 | 33.3 | TDD | 267 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3238571 | 4 | 121.4726127297 | 31.1485943816 | 256 | 3 | 6 | 39.5 | TDD | 825 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.956 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.971 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.086 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.086 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.826 | NREventA3 | measId:2;ServCellPCI:566;Se... |
| 2024-09-20 22:21:35.826 | NREventA3 | measId:2;ServCellPCI:566;Se... |
| 2024-09-20 22:21:36.826 | NREventA3 | measId:2;ServCellPCI:566;Se... |
| 2024-09-20 22:21:39.326 | NRRRCReestablishAttempt | PCI:566 |
| 2024-09-20 22:21:39.342 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.352 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.484 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.484 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220415 | 1 | 17.2845 | 9.5635 | -115.0817 | 12.9519 | 196.0308 | 0.0140 | 0.1785 |
| 2024_09_20 22:00 | 3236495 | 2 | 7.1547 | 14.0527 | -117.8766 | 19.8362 | 155.5534 | 0.0090 | 0.0153 |
| 2024_09_20 22:00 | 3218013 | 3 | 10.3396 | 15.2686 | -115.9456 | 13.0181 | 129.9640 | 0.0130 | 0.0192 |
| 2024_09_20 22:00 | 3238571 | 4 | 9.5225 | 18.6118 | -116.0270 | 9.9169 | 112.5592 | 0.0015 | 0.0196 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412716_0F908DB5 | 504990 | 977 | -87.1 | 504990 | 825 | -81.2 | 504990 | 885 | -89.8 | 504990 | 267 |
| MR_1774412716_04C8D435 | 504990 | 825 | -83.1 | 504990 | 977 | -86.4 | 504990 | 885 | -89.9 | 504990 | 267 |
| MR_1774412716_ECF78BC2 | 504990 | 825 | -79.7 | 504990 | 977 | -88.3 | 504990 | 885 | -89.3 | 504990 | 267 |
| MR_1774412716_7D9E640D | 504990 | 977 | -85.4 | 504990 | 825 | -81.5 | 504990 | 885 | -87.8 | 504990 | 267 |
| MR_1774412716_4E6CF9F9 | 504990 | 825 | -82.1 | 504990 | 977 | -88.1 | 504990 | 885 | -91.3 | 504990 | 267 |
| MR_1774412716_E374E086 | 504990 | 977 | -87.3 | 504990 | 825 | -81.9 | 504990 | 885 | -87.7 | 504990 | 267 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1719: `c590edeb-cf0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c590edeb-cf07-4f62-a2a8-9505c824e486` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1719] topology](images/train_1719.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3266538_2
- `C2`: Check test server and transmission issues **← 정답**
- `C3`: Adjust the azimuth of 3266538_2 by 50 degrees
- `C4`: Lift the tilt angle of 3228401_1 by 7 degrees
- `C5`: Press down the tilt angle of 3228401_1 by 7 degrees
- `C6`: Increase A3 Offset threshold for 3266538_2
- `C7`: Add neighbor relationship between 3228401_1 and 3266538_2
- `C8`: Add neighbor relationship between 3249377_4 and 3266538_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228401_1
- `C10`: Decrease A3 Offset threshold for 3266538_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266538_2
- `C12`: Press down the tilt angle  of 3266538_2 by 5 degrees
- `C13`: Decrease transmission power for 3228401_1
- `C14`: Adjust the azimuth of 3228401_1 by 50 degrees
- `C15`: Decrease transmission power for 3266538_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228401_1
- `C17`: Decrease A3 Offset threshold for 3228401_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266538_2
- `C19`: Lift the tilt angle  of 3266538_2 by 5 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase transmission power for 3228401_1
- `C22`: Increase A3 Offset threshold for 3228401_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.744 | MS1 | 121.4656605178 | 31.1446200997 | 881 | 504990 | -86.48 | 17.79 | 541.22 | 0.14 | 2.32 | 1592 |
| 2024-09-20 22:21:32.291 | MS1 | 121.4656733394 | 31.1446247214 | 881 | 504990 | -88.24 | 13.47 | 376.01 | 0.06 | 2.52 | 1592 |
| 2024-09-20 22:21:33.876 | MS1 | 121.4656698284 | 31.1446221604 | 881 | 504990 | -87.14 | 14.91 | 595.91 | 0.17 | 2.69 | 1581 |
| 2024-09-20 22:21:34.885 | MS1 | 121.4656685874 | 31.1446361265 | 881 | 504990 | -91.70 | 17.54 | 75.14 | 0.19 | 2.55 | 315 |
| 2024-09-20 22:21:35.557 | MS1 | 121.4656699775 | 31.1446183714 | 881 | 504990 | -85.02 | 17.96 | 89.41 | 0.18 | 2.03 | 460 |
| 2024-09-20 22:21:36.140 | MS1 | 121.4656665350 | 31.1446310761 | 881 | 504990 | -86.29 | 14.11 | 75.94 | 0.14 | 2.19 | 373 |
| 2024-09-20 22:21:37.283 | MS1 | 121.4656769113 | 31.1446325590 | 881 | 504990 | -92.00 | 8.58 | 65.94 | 0.16 | 2.95 | 332 |
| 2024-09-20 22:21:38.974 | MS1 | 121.4656773803 | 31.1446373925 | 881 | 504990 | -92.70 | 9.27 | 73.57 | 0.01 | 2.86 | 331 |
| 2024-09-20 22:21:39.218 | MS1 | 121.4656679706 | 31.1446271878 | 881 | 504990 | -91.88 | 10.15 | 41.95 | 0.19 | 2.38 | 361 |
| 2024-09-20 22:21:40.982 | MS1 | 121.4656621077 | 31.1446316983 | 881 | 504990 | -91.10 | 12.59 | 394.65 | 0.20 | 2.60 | 1582 |
| 2024-09-20 22:21:41.259 | MS1 | 121.4656716143 | 31.1446377891 | 881 | 504990 | -92.03 | 7.57 | 556.39 | 0.15 | 2.15 | 1590 |
| 2024-09-20 22:21:42.703 | MS1 | 121.4656686714 | 31.1446292004 | 881 | 504990 | -93.35 | 12.73 | 559.98 | 0.02 | 2.38 | 1561 |

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
| 3228401 | 1 | 121.4729281225 | 31.1473212719 | 103 | 5 | 8 | 23.3 | TDD | 881 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3233108 | 3 | 121.4723049704 | 31.1469450266 | 61 | 10 | 1 | 45.5 | TDD | 100 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3249377 | 4 | 121.4655287992 | 31.1486491045 | 317 | 12 | 8 | 25.3 | TDD | 349 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3266538 | 2 | 121.4700065248 | 31.1548560847 | 272 | 3 | 3 | 42.8 | TDD | 819 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.597 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.622 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.753 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.753 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.409 | NREventA3 | measId:2;ServCellPCI:935;Se... |
| 2024-09-20 22:21:38.649 | NRHandoverAttempt | SourcePCI:935;SourceNR-ARFC... |
| 2024-09-20 22:21:38.693 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.703 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.825 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.825 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228401 | 1 | 15.6479 | 19.3591 | -114.9540 | 10.0356 | 94.2003 | 0.0184 | 0.0114 |
| 2024_09_20 22:00 | 3266538 | 2 | 9.2355 | 14.4933 | -115.1549 | 5.0114 | 156.8787 | 0.0040 | 0.0162 |
| 2024_09_20 22:00 | 3233108 | 3 | 19.8226 | 15.4127 | -116.6713 | 7.7571 | 113.5951 | 0.0010 | 0.0187 |
| 2024_09_20 22:00 | 3249377 | 4 | 5.8848 | 19.6325 | -117.3544 | 14.5940 | 143.5288 | 0.0055 | 0.0159 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412202_1B647A59 | 504990 | 881 | -90.1 | 504990 | 819 | -96.1 | 504990 | 349 | -99.1 | 504990 | 100 |
| MR_1774412202_8CA2E57D | 504990 | 881 | -93.2 | 504990 | 819 | -92.6 | 504990 | 349 | -99.5 | 504990 | 100 |
| MR_1774412202_44725457 | 504990 | 881 | -93.0 | 504990 | 819 | -93.7 | 504990 | 349 | -101.3 | 504990 | 100 |
| MR_1774412202_FE71AE16 | 504990 | 881 | -93.2 | 504990 | 819 | -95.5 | 504990 | 349 | -100.6 | 504990 | 100 |
| MR_1774412202_A6FD4A3E | 504990 | 881 | -90.3 | 504990 | 819 | -92.5 | 504990 | 349 | -99.5 | 504990 | 100 |
| MR_1774412202_2248B063 | 504990 | 881 | -90.1 | 504990 | 819 | -92.5 | 504990 | 349 | -98.5 | 504990 | 100 |

> *... 2개 열 생략 (전체 14열)*

---
