# Track A 문제 분석 — train[680]~train[689]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[680] ~ train[689] (10개)

## 목차

1. [문제 680: `d8ad83dc-e5f...`](#680) — single-answer, 정답: C20
2. [문제 681: `bb5d04dd-774...`](#681) — single-answer, 정답: C22
3. [문제 682: `440c87a9-933...`](#682) — single-answer, 정답: C5
4. [문제 683: `89c37da0-172...`](#683) — multiple-answer, 정답: C11|C22
5. [문제 684: `6b9348e6-22c...`](#684) — single-answer, 정답: C22
6. [문제 685: `02371c8e-e01...`](#685) — single-answer, 정답: C11
7. [문제 686: `120c0516-601...`](#686) — single-answer, 정답: C21
8. [문제 687: `22e0ad0d-0f7...`](#687) — single-answer, 정답: C1
9. [문제 688: `ff8ebed6-d2b...`](#688) — single-answer, 정답: C20
10. [문제 689: `596dc986-ef9...`](#689) — multiple-answer, 정답: C13|C14

---

### 문제 680: `d8ad83dc-e5f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d8ad83dc-e5f0-4525-a6a1-36e360f82c99` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Add neighbor relationship between 3233795_1 and 3231764_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[680] topology](images/train_0680.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3231764_3
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase A3 Offset threshold for 3233795_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231764_3
- `C5`: Decrease transmission power for 3231764_3
- `C6`: Lift the tilt angle of 3233795_1 by 10 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233795_1
- `C8`: Press down the tilt angle of 3233795_1 by 10 degrees
- `C9`: Decrease A3 Offset threshold for 3233795_1
- `C10`: Adjust the azimuth of 3231764_3 by 36 degrees
- `C11`: Decrease transmission power for 3233795_1
- `C12`: Increase transmission power for 3233795_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233795_1
- `C14`: Add neighbor relationship between 3266406_4 and 3231764_3
- `C15`: Adjust the azimuth of 3233795_1 by 1 degrees
- `C16`: Increase A3 Offset threshold for 3231764_3
- `C17`: Check test server and transmission issues
- `C18`: Increase transmission power for 3231764_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231764_3
- `C20`: Add neighbor relationship between 3233795_1 and 3231764_3 **← 정답**
- `C21`: Press down the tilt angle  of 3231764_3 by 5 degrees
- `C22`: Lift the tilt angle  of 3231764_3 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.283 | MS1 | 121.4656732439 | 31.1446329267 | 912 | 504990 | -78.67 | 13.42 | 596.92 | 0.18 | 2.61 | 1594 |
| 2024-09-20 22:21:32.125 | MS1 | 121.4656716325 | 31.1446317815 | 912 | 504990 | -80.20 | 15.70 | 422.76 | 0.10 | 2.34 | 1590 |
| 2024-09-20 22:21:33.889 | MS1 | 121.4656661863 | 31.1446337430 | 912 | 504990 | -80.23 | 16.97 | 388.33 | 0.13 | 2.84 | 1596 |
| 2024-09-20 22:21:34.979 | MS1 | 121.4656624536 | 31.1446334296 | 912 | 504990 | -86.16 | -0.60 | 69.31 | 0.20 | 1.32 | 1578 |
| 2024-09-20 22:21:35.193 | MS1 | 121.4656765969 | 31.1446261474 | 912 | 504990 | -91.35 | -2.75 | 56.67 | 0.18 | 1.21 | 1573 |
| 2024-09-20 22:21:36.949 | MS1 | 121.4656715690 | 31.1446335726 | 912 | 504990 | -91.12 | -0.70 | 53.12 | 0.18 | 1.05 | 1578 |
| 2024-09-20 22:21:37.557 | MS1 | 121.4656771171 | 31.1446231579 | 912 | 504990 | -86.83 | -1.85 | 59.60 | 0.08 | 1.03 | 1562 |
| 2024-09-20 22:21:38.859 | MS1 | 121.4656690517 | 31.1446348481 | 912 | 504990 | -82.73 | 14.23 | 347.91 | 0.16 | 1.17 | 1588 |
| 2024-09-20 22:21:39.928 | MS1 | 121.4656702570 | 31.1446183843 | 912 | 504990 | -75.17 | 13.54 | 424.57 | 0.03 | 1.04 | 1561 |
| 2024-09-20 22:21:40.795 | MS1 | 121.4656667785 | 31.1446366532 | 912 | 504990 | -84.67 | 16.07 | 568.67 | 0.20 | 2.33 | 1591 |
| 2024-09-20 22:21:41.171 | MS1 | 121.4656775583 | 31.1446315040 | 912 | 504990 | -83.00 | 16.03 | 324.14 | 0.05 | 2.03 | 1567 |
| 2024-09-20 22:21:42.720 | MS1 | 121.4656605340 | 31.1446349581 | 912 | 504990 | -78.89 | 13.02 | 298.96 | 0.03 | 2.43 | 1560 |

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
| 3231764 | 3 | 121.4732038186 | 31.1524965303 | 183 | 4 | 5 | 28.2 | TDD | 276 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3233795 | 1 | 121.4744567007 | 31.1529445269 | 223 | 10 | 5 | 36.1 | TDD | 912 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3237418 | 2 | 121.4726945083 | 31.1543079211 | 45 | 14 | 6 | 20.9 | TDD | 482 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3266406 | 4 | 121.4651821459 | 31.1451378380 | 135 | 13 | 5 | 41.2 | TDD | 324 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.353 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.375 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.489 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.489 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.173 | NREventA3 | measId:2;ServCellPCI:115;Se... |
| 2024-09-20 22:21:36.173 | NREventA3 | measId:2;ServCellPCI:115;Se... |
| 2024-09-20 22:21:37.173 | NREventA3 | measId:2;ServCellPCI:115;Se... |
| 2024-09-20 22:21:39.673 | NRRRCReestablishAttempt | PCI:115 |
| 2024-09-20 22:21:39.686 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.697 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.840 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.840 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233795 | 1 | 9.0172 | 5.5240 | -114.0729 | 12.2810 | 170.2994 | 0.0025 | 0.1081 |
| 2024_09_20 22:00 | 3237418 | 2 | 17.7538 | 6.2974 | -117.1420 | 9.2593 | 111.7511 | 0.0125 | 0.0085 |
| 2024_09_20 22:00 | 3231764 | 3 | 17.9762 | 18.5894 | -114.2972 | 10.4180 | 113.5079 | 0.0178 | 0.0141 |
| 2024_09_20 22:00 | 3266406 | 4 | 8.4926 | 6.8573 | -114.2374 | 15.6060 | 156.8330 | 0.0007 | 0.0059 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416584_16A1667F | 504990 | 276 | -81.1 | 504990 | 912 | -86.8 | 504990 | 324 | -81.2 | 504990 | 482 |
| MR_1774416584_6308F46C | 504990 | 912 | -87.4 | 504990 | 276 | -82.4 | 504990 | 324 | -83.2 | 504990 | 482 |
| MR_1774416584_1772E51A | 504990 | 276 | -80.1 | 504990 | 912 | -87.8 | 504990 | 324 | -82.8 | 504990 | 482 |
| MR_1774416584_02AAF54E | 504990 | 912 | -84.8 | 504990 | 276 | -79.6 | 504990 | 324 | -82.7 | 504990 | 482 |
| MR_1774416584_127326D9 | 504990 | 276 | -80.4 | 504990 | 912 | -85.2 | 504990 | 324 | -82.1 | 504990 | 482 |
| MR_1774416584_82B65FCA | 504990 | 912 | -85.5 | 504990 | 276 | -82.9 | 504990 | 324 | -82.0 | 504990 | 482 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 681: `bb5d04dd-774...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bb5d04dd-7746-459f-a4a6-e715ef9b99fa` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264600_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[681] topology](images/train_0681.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3234915_4
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Lift the tilt angle  of 3234915_4 by 4 degrees
- `C4`: Decrease A3 Offset threshold for 3264600_3
- `C5`: Increase transmission power for 3234915_4
- `C6`: Decrease transmission power for 3264600_3
- `C7`: Add neighbor relationship between 3264600_3 and 3234915_4
- `C8`: Press down the tilt angle  of 3234915_4 by 4 degrees
- `C9`: Decrease A3 Offset threshold for 3234915_4
- `C10`: Check test server and transmission issues
- `C11`: Decrease transmission power for 3234915_4
- `C12`: Increase transmission power for 3264600_3
- `C13`: Adjust the azimuth of 3234915_4 by 8 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264600_3
- `C15`: Add neighbor relationship between 3261069_7 and 3234915_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234915_4
- `C17`: Increase A3 Offset threshold for 3264600_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234915_4
- `C19`: Adjust the azimuth of 3264600_3 by 18 degrees
- `C20`: Lift the tilt angle of 3264600_3 by 3 degrees
- `C21`: Press down the tilt angle of 3264600_3 by 3 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264600_3 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.912 | MS1 | 121.4656591259 | 31.1446237321 | 336 | 504990 | -94.10 | 9.46 | 394.08 | 0.01 | 2.52 | 1589 |
| 2024-09-20 22:21:32.166 | MS1 | 121.4656703637 | 31.1446221636 | 558 | 504990 | -96.00 | 14.02 | 331.53 | 0.03 | 2.96 | 1563 |
| 2024-09-20 22:21:33.126 | MS1 | 121.4656671263 | 31.1446330854 | 614 | 504990 | -93.58 | 11.04 | 486.66 | 0.04 | 2.54 | 1593 |
| 2024-09-20 22:21:34.357 | MS1 | 121.4656645686 | 31.1446321245 | 502 | 152650 | -91.46 | 5.39 | 75.09 | 0.11 | 1.86 | 912 |
| 2024-09-20 22:21:35.890 | MS1 | 121.4656751264 | 31.1446335335 | 678 | 152650 | -88.38 | 2.48 | 83.39 | 0.09 | 1.60 | 970 |
| 2024-09-20 22:21:36.458 | MS1 | 121.4656749137 | 31.1446338808 | 421 | 152650 | -90.74 | 3.71 | 89.46 | 0.05 | 1.66 | 922 |
| 2024-09-20 22:21:37.701 | MS1 | 121.4656607030 | 31.1446239978 | 811 | 152650 | -88.33 | 5.07 | 53.37 | 0.16 | 1.54 | 947 |
| 2024-09-20 22:21:38.795 | MS1 | 121.4656659059 | 31.1446326668 | 502 | 152650 | -93.64 | 3.68 | 81.23 | 0.04 | 1.82 | 994 |
| 2024-09-20 22:21:39.140 | MS1 | 121.4656704393 | 31.1446339438 | 678 | 152650 | -93.35 | 4.08 | 100.34 | 0.01 | 1.90 | 938 |
| 2024-09-20 22:21:40.371 | MS1 | 121.4656737389 | 31.1446332947 | 421 | 152650 | -96.62 | 4.63 | 82.84 | 0.05 | 2.49 | 1572 |
| 2024-09-20 22:21:41.258 | MS1 | 121.4656721858 | 31.1446301641 | 811 | 152650 | -90.91 | 7.59 | 81.63 | 0.09 | 2.15 | 1592 |
| 2024-09-20 22:21:42.645 | MS1 | 121.4656723667 | 31.1446287640 | 502 | 152650 | -95.07 | 7.10 | 95.05 | 0.06 | 2.90 | 1577 |

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
| 3213315 | 5 | 121.4691794737 | 31.1546134352 | 171 | 13 | 3 | 3.5 | TDD | 665 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3219371 | 6 | 121.4653226609 | 31.1557933942 | 295 | 0 | 6 | 22.8 | TDD | 572 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3224094 | 11 | 121.4709242851 | 31.1539264205 | 243 | 0 | 10 | 20.2 | FDD | 502 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3234519 | 2 | 121.4734027764 | 31.1479433854 | 6 | 1 | 7 | 23.2 | TDD | 558 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3234915 | 4 | 121.4740183279 | 31.1441709255 | 282 | 4 | 12 | 1.7 | TDD | 438 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3247426 | 13 | 121.4722891502 | 31.1458422839 | 247 | 14 | 9 | 3.6 | FDD | 920 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3251787 | 8 | 121.4716800030 | 31.1549688770 | 272 | 9 | 11 | 26.6 | FDD | 678 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3254921 | 10 | 121.4685658790 | 31.1476586127 | 245 | 12 | 4 | 9.1 | FDD | 235 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3261069 | 7 | 121.4721343479 | 31.1527268935 | 144 | 9 | 0 | 5.5 | FDD | 421 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3264600 | 3 | 121.4690388701 | 31.1548085937 | 214 | 3 | 3 | 1.7 | TDD | 336 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3266640 | 1 | 121.4721674108 | 31.1524915804 | 337 | 14 | 6 | 28.5 | TDD | 614 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3272655 | 12 | 121.4712425651 | 31.1489811091 | 36 | 2 | 11 | 21.8 | FDD | 855 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3273475 | 9 | 121.4674225210 | 31.1485054131 | 327 | 10 | 5 | 0.8 | FDD | 811 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |

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
| 2024-09-20 22:21:31.361 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.381 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.497 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.497 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.193 | NREventA2 | measId:1;ServCellPCI:30;Ser... |
| 2024-09-20 22:21:35.297 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.557 | NREventA5 | measId:3;ServCellPCI:30;Ser... |
| 2024-09-20 22:21:35.601 | NRHandoverAttempt | SourcePCI:30;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.631 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.643 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.772 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.772 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266640 | 1 | 18.4023 | 12.5510 | -114.4812 | 16.8249 | 179.0808 | 0.0108 | 0.0089 |
| 2024_09_20 22:00 | 3234519 | 2 | 12.5491 | 12.3509 | -117.3831 | 5.9201 | 162.1375 | 0.0042 | 0.0152 |
| 2024_09_20 22:00 | 3264600 | 3 | 7.0809 | 18.6381 | -116.6818 | 19.8095 | 87.0842 | 0.0133 | 0.0181 |
| 2024_09_20 22:00 | 3234915 | 4 | 16.4617 | 7.5997 | -114.9617 | 11.8758 | 133.0440 | 0.0144 | 0.0153 |
| 2024_09_20 22:00 | 3213315 | 5 | 11.5142 | 17.3247 | -114.6064 | 7.1848 | 121.6665 | 0.0022 | 0.0157 |
| 2024_09_20 22:00 | 3219371 | 6 | 6.4003 | 13.2842 | -114.6926 | 10.0579 | 104.1502 | 0.0001 | 0.0159 |
| 2024_09_20 22:00 | 3261069 | 7 | 15.7272 | 7.0757 | -114.7013 | 4.6671 | 53.5504 | 0.0154 | 0.0048 |
| 2024_09_20 22:00 | 3251787 | 8 | 15.9117 | 9.7477 | -114.0021 | 4.2374 | 33.7323 | 0.0056 | 0.0076 |
| 2024_09_20 22:00 | 3273475 | 9 | 18.0959 | 5.9410 | -114.1291 | 4.2476 | 34.7932 | 0.0014 | 0.0189 |
| 2024_09_20 22:00 | 3254921 | 10 | 11.0442 | 13.2813 | -114.9886 | 4.1849 | 31.9797 | 0.0052 | 0.0073 |
| 2024_09_20 22:00 | 3224094 | 11 | 9.2840 | 17.8337 | -115.3434 | 4.5883 | 53.9440 | 0.0111 | 0.0013 |
| 2024_09_20 22:00 | 3272655 | 12 | 10.7972 | 8.3578 | -117.7432 | 3.0875 | 57.5910 | 0.0025 | 0.0018 |
| 2024_09_20 22:00 | 3247426 | 13 | 15.6303 | 13.7211 | -117.0954 | 3.8382 | 24.4266 | 0.0117 | 0.0032 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414765_4A7EA8C7 | 152650 | 502 | -92.1 | 152650 | 855 | -93.4 | 152650 | 920 | -101.0 | 152650 | 235 |
| MR_1774414765_0EBD948A | 504990 | 614 | -92.5 | 504990 | 438 | -94.8 | 504990 | 665 | -95.8 | 504990 | 572 |
| MR_1774414765_94BE290F | 152650 | 502 | -93.0 | 152650 | 855 | -93.4 | 152650 | 920 | -103.6 | 152650 | 235 |
| MR_1774414765_DBDCF7B5 | 504990 | 614 | -94.9 | 504990 | 438 | -93.8 | 504990 | 665 | -95.6 | 504990 | 572 |
| MR_1774414765_6D4CF63C | 152650 | 502 | -90.6 | 152650 | 855 | -94.0 | 152650 | 920 | -101.8 | 152650 | 235 |
| MR_1774414765_9151B1F0 | 152650 | 502 | -93.2 | 152650 | 855 | -95.0 | 152650 | 920 | -104.4 | 152650 | 235 |
| MR_1774414765_5734FF81 | 152650 | 502 | -90.7 | 152650 | 855 | -94.7 | 152650 | 920 | -104.4 | 152650 | 235 |
| MR_1774414765_8741EAF2 | 504990 | 614 | -94.3 | 504990 | 438 | -95.3 | 504990 | 665 | -96.9 | 504990 | 572 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 682: `440c87a9-933...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `440c87a9-933b-4a12-b4d4-0c587534bd64` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Lift the tilt angle  of 3219332_4 by 5 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[682] topology](images/train_0682.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260499_3
- `C2`: Increase transmission power for 3214169_1
- `C3`: Press down the tilt angle  of 3219332_4 by 5 degrees
- `C4`: Decrease A3 Offset threshold for 3260499_3
- `C5`: Lift the tilt angle  of 3219332_4 by 5 degrees **← 정답**
- `C6`: Increase transmission power for 3260499_3
- `C7`: Check test server and transmission issues
- `C8`: Adjust the azimuth of 3219332_4 by 50 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260499_3
- `C11`: Decrease transmission power for 3260499_3
- `C12`: Decrease transmission power for 3214169_1
- `C13`: Increase A3 Offset threshold for 3260499_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214169_1
- `C15`: Lift the tilt angle of 3214169_1 by 3 degrees
- `C16`: Increase A3 Offset threshold for 3214169_1
- `C17`: Add neighbor relationship between 3214169_1 and 3260499_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214169_1
- `C19`: Adjust the azimuth of 3214169_1 by 8 degrees
- `C20`: Add neighbor relationship between 3219332_4 and 3260499_3
- `C21`: Press down the tilt angle of 3214169_1 by 3 degrees
- `C22`: Decrease A3 Offset threshold for 3214169_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.339 | MS1 | 121.4656767190 | 31.1446210822 | 834 | 504990 | -88.76 | 16.60 | 507.82 | 0.14 | 2.15 | 1575 |
| 2024-09-20 22:21:32.711 | MS1 | 121.4656672831 | 31.1446369932 | 834 | 504990 | -89.65 | 15.25 | 325.37 | 0.05 | 2.34 | 1568 |
| 2024-09-20 22:21:33.996 | MS1 | 121.4656588827 | 31.1446271914 | 834 | 504990 | -85.31 | 15.62 | 524.29 | 0.15 | 2.59 | 1572 |
| 2024-09-20 22:21:34.633 | MS1 | 121.4656586306 | 31.1446217700 | 834 | 504990 | -90.61 | 13.10 | 45.98 | 0.14 | 2.50 | 1571 |
| 2024-09-20 22:21:35.261 | MS1 | 121.4656772019 | 31.1446279307 | 834 | 504990 | -91.47 | 13.29 | 83.07 | 0.03 | 2.49 | 1586 |
| 2024-09-20 22:21:36.747 | MS1 | 121.4656732610 | 31.1446247337 | 834 | 504990 | -87.77 | 14.48 | 74.63 | 0.16 | 2.27 | 1571 |
| 2024-09-20 22:21:37.562 | MS1 | 121.4656682778 | 31.1446296781 | 834 | 504990 | -91.96 | 7.97 | 89.87 | 0.20 | 2.20 | 1579 |
| 2024-09-20 22:21:38.720 | MS1 | 121.4656697961 | 31.1446325234 | 834 | 504990 | -91.54 | 10.53 | 59.03 | 0.02 | 2.20 | 1600 |
| 2024-09-20 22:21:39.495 | MS1 | 121.4656696251 | 31.1446246003 | 834 | 504990 | -91.36 | 8.80 | 88.67 | 0.17 | 2.82 | 1599 |
| 2024-09-20 22:21:40.506 | MS1 | 121.4656681749 | 31.1446200202 | 834 | 504990 | -93.11 | 7.41 | 301.33 | 0.02 | 2.34 | 1580 |
| 2024-09-20 22:21:41.377 | MS1 | 121.4656720749 | 31.1446195372 | 834 | 504990 | -90.18 | 10.75 | 330.57 | 0.13 | 2.16 | 1565 |
| 2024-09-20 22:21:42.732 | MS1 | 121.4656764288 | 31.1446235862 | 834 | 504990 | -90.73 | 11.76 | 532.34 | 0.18 | 2.43 | 1597 |

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
| 3214169 | 1 | 121.4655839264 | 31.1506595536 | 187 | 0 | 1 | 33.6 | TDD | 834 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3219332 | 4 | 121.4707839693 | 31.1466110919 | 65 | 13 | 6 | 21.4 | TDD | 983 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3225256 | 2 | 121.4723986026 | 31.1472970080 | 300 | 2 | 11 | 36.8 | TDD | 83 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3260499 | 3 | 121.4690563962 | 31.1552655282 | 70 | 3 | 0 | 43.1 | TDD | 614 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.830 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.849 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.992 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.992 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.687 | NREventA3 | measId:2;ServCellPCI:942;Se... |
| 2024-09-20 22:21:37.927 | NRHandoverAttempt | SourcePCI:942;SourceNR-ARFC... |
| 2024-09-20 22:21:37.958 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.971 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.108 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.108 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214169 | 1 | 75.2728 | 81.0978 | -117.5709 | 13.5398 | 132.0084 | 0.0080 | 0.0025 |
| 2024_09_20 22:00 | 3225256 | 2 | 19.4942 | 15.4599 | -115.4229 | 9.0036 | 153.6839 | 0.0041 | 0.0185 |
| 2024_09_20 22:00 | 3260499 | 3 | 11.4562 | 5.7795 | -116.3846 | 13.9550 | 186.4660 | 0.0032 | 0.0185 |
| 2024_09_20 22:00 | 3219332 | 4 | 18.1161 | 9.0356 | -115.9312 | 6.3182 | 153.0780 | 0.0163 | 0.0170 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414820_80762A11 | 504990 | 834 | -92.4 | 504990 | 614 | -96.2 | 504990 | 983 | -100.0 | 504990 | 83 |
| MR_1774414820_24869C00 | 504990 | 834 | -91.7 | 504990 | 614 | -93.5 | 504990 | 983 | -98.6 | 504990 | 83 |
| MR_1774414820_537ECE0E | 504990 | 834 | -92.2 | 504990 | 614 | -95.7 | 504990 | 983 | -100.2 | 504990 | 83 |
| MR_1774414820_2A80D6C2 | 504990 | 834 | -92.2 | 504990 | 614 | -96.2 | 504990 | 983 | -97.6 | 504990 | 83 |
| MR_1774414820_B6F6C710 | 504990 | 834 | -88.8 | 504990 | 614 | -95.0 | 504990 | 983 | -99.0 | 504990 | 83 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 683: `89c37da0-172...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `89c37da0-172c-4893-b24f-9a8b77396afb` |
| Tag | **multiple-answer** |
| 정답 | **C11|C22** |
| C11 의미 | Adjust the azimuth of 3258021_1 by 47 degrees |
| C22 의미 | Increase transmission power for 3258021_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[683] topology](images/train_0683.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3258021_1
- `C2`: Increase A3 Offset threshold for 3258021_1
- `C3`: Adjust the azimuth of 3270445_2 by 46 degrees
- `C4`: Press down the tilt angle of 3258021_1 by 10 degrees
- `C5`: Add neighbor relationship between 3258178_3 and 3270445_2
- `C6`: Decrease A3 Offset threshold for 3258021_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270445_2
- `C8`: Decrease A3 Offset threshold for 3270445_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258021_1
- `C10`: Lift the tilt angle  of 3270445_2 by 2 degrees
- `C11`: Adjust the azimuth of 3258021_1 by 47 degrees **← 정답**
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258021_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270445_2
- `C14`: Increase A3 Offset threshold for 3270445_2
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Lift the tilt angle of 3258021_1 by 10 degrees
- `C17`: Check test server and transmission issues
- `C18`: Press down the tilt angle  of 3270445_2 by 2 degrees
- `C19`: Add neighbor relationship between 3258021_1 and 3270445_2
- `C20`: Increase transmission power for 3270445_2
- `C21`: Decrease transmission power for 3270445_2
- `C22`: Increase transmission power for 3258021_1 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.498 | MS1 | 121.4656581880 | 31.1446247085 | 106 | 504990 | -94.83 | 17.97 | 396.55 | 0.07 | 2.23 | 1592 |
| 2024-09-20 22:21:32.738 | MS1 | 121.4656679157 | 31.1446365033 | 106 | 504990 | -89.90 | 15.92 | 437.13 | 0.03 | 2.81 | 1573 |
| 2024-09-20 22:21:33.318 | MS1 | 121.4656652718 | 31.1446282411 | 106 | 504990 | -92.74 | 15.96 | 589.46 | 0.18 | 2.44 | 1596 |
| 2024-09-20 22:21:34.567 | MS1 | 121.4656673307 | 31.1446287695 | 106 | 504990 | -101.25 | 0.47 | 45.79 | 0.18 | 1.24 | 1561 |
| 2024-09-20 22:21:35.225 | MS1 | 121.4656656241 | 31.1446194708 | 106 | 504990 | -107.92 | 1.43 | 63.03 | 0.09 | 1.04 | 1579 |
| 2024-09-20 22:21:36.951 | MS1 | 121.4656742344 | 31.1446204658 | 106 | 504990 | -108.52 | -0.75 | 54.88 | 0.14 | 1.35 | 1585 |
| 2024-09-20 22:21:37.376 | MS1 | 121.4656666128 | 31.1446301486 | 106 | 504990 | -102.40 | 0.62 | 57.42 | 0.19 | 1.21 | 1582 |
| 2024-09-20 22:21:38.549 | MS1 | 121.4656586762 | 31.1446324890 | 106 | 504990 | -102.56 | -1.51 | 33.61 | 0.03 | 1.38 | 1593 |
| 2024-09-20 22:21:39.586 | MS1 | 121.4656767435 | 31.1446226086 | 106 | 504990 | -102.19 | 1.81 | 65.93 | 0.03 | 1.22 | 1573 |
| 2024-09-20 22:21:40.836 | MS1 | 121.4656610231 | 31.1446181810 | 106 | 504990 | -87.90 | 17.55 | 554.59 | 0.05 | 2.14 | 1582 |
| 2024-09-20 22:21:41.848 | MS1 | 121.4656657365 | 31.1446185184 | 106 | 504990 | -92.65 | 17.99 | 401.56 | 0.05 | 2.98 | 1577 |
| 2024-09-20 22:21:42.420 | MS1 | 121.4656685368 | 31.1446367841 | 106 | 504990 | -94.67 | 15.64 | 374.44 | 0.01 | 2.49 | 1600 |

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
| 3234432 | 4 | 121.4659850798 | 31.1497863103 | 93 | 3 | 1 | 32.9 | TDD | 68 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3258021 | 1 | 121.4678520304 | 31.1470200895 | 265 | 10 | 3 | 41.0 | TDD | 106 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3258178 | 3 | 121.4644382533 | 31.1486263829 | 245 | 10 | 9 | 36.2 | TDD | 126 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3270445 | 2 | 121.4673905337 | 31.1552842156 | 142 | 0 | 9 | 49.7 | TDD | 268 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.659 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.677 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.824 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.824 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.974 | NREventA2 | measId:1;ServCellPCI:194;Se... |
| 2024-09-20 22:21:35.103 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258021 | 1 | 15.8128 | 8.1428 | -117.2661 | 18.9068 | 118.3962 | 0.1600 | 0.0132 |
| 2024_09_20 22:00 | 3270445 | 2 | 19.9553 | 8.9843 | -114.8043 | 18.2293 | 120.7521 | 0.0150 | 0.0019 |
| 2024_09_20 22:00 | 3258178 | 3 | 19.7737 | 11.2311 | -115.0768 | 5.4699 | 169.2321 | 0.0021 | 0.0051 |
| 2024_09_20 22:00 | 3234432 | 4 | 7.7953 | 12.9006 | -115.9403 | 17.8835 | 137.7176 | 0.0097 | 0.0096 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412330_88DB10C5 | 504990 | 106 | -100.8 | 504990 | 268 | -109.5 | 504990 | 126 | -113.6 | 504990 | 68 |
| MR_1774412330_A9428A30 | 504990 | 106 | -102.0 | 504990 | 268 | -110.2 | 504990 | 126 | -115.8 | 504990 | 68 |
| MR_1774412330_499E259B | 504990 | 106 | -100.5 | 504990 | 268 | -107.4 | 504990 | 126 | -114.9 | 504990 | 68 |
| MR_1774412330_DF27BDC1 | 504990 | 106 | -100.3 | 504990 | 268 | -107.7 | 504990 | 126 | -112.8 | 504990 | 68 |
| MR_1774412330_2F90ACC6 | 504990 | 106 | -102.6 | 504990 | 268 | -109.9 | 504990 | 126 | -115.6 | 504990 | 68 |
| MR_1774412330_A4C53A4C | 504990 | 106 | -101.6 | 504990 | 268 | -106.5 | 504990 | 126 | -112.4 | 504990 | 68 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 684: `6b9348e6-22c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6b9348e6-22cf-47e8-9f1c-c19fe438f8e2` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[684] topology](images/train_0684.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3245107_3 by 16 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245107_3
- `C3`: Increase A3 Offset threshold for 3212046_1
- `C4`: Add neighbor relationship between 3212046_1 and 3245107_3
- `C5`: Lift the tilt angle of 3212046_1 by 8 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245107_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212046_1
- `C8`: Increase transmission power for 3212046_1
- `C9`: Lift the tilt angle  of 3245107_3 by 7 degrees
- `C10`: Add neighbor relationship between 3223599_4 and 3245107_3
- `C11`: Press down the tilt angle  of 3245107_3 by 7 degrees
- `C12`: Increase A3 Offset threshold for 3245107_3
- `C13`: Decrease transmission power for 3212046_1
- `C14`: Decrease transmission power for 3245107_3
- `C15`: Adjust the azimuth of 3212046_1 by 50 degrees
- `C16`: Press down the tilt angle of 3212046_1 by 8 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212046_1
- `C18`: Check test server and transmission issues
- `C19`: Decrease A3 Offset threshold for 3212046_1
- `C20`: Decrease A3 Offset threshold for 3245107_3
- `C21`: Increase transmission power for 3245107_3
- `C22`: Insufficient data; more data is needed for judgment. **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.176 | MS1 | 121.4656759178 | 31.1446260257 | 616 | 504990 | -87.54 | 12.21 | 548.00 | 0.02 | 2.94 | 1575 |
| 2024-09-20 22:21:32.179 | MS1 | 121.4656755737 | 31.1446198539 | 616 | 504990 | -91.06 | 14.24 | 331.80 | 0.19 | 2.20 | 1600 |
| 2024-09-20 22:21:33.579 | MS1 | 121.4656713520 | 31.1446255804 | 616 | 504990 | -89.91 | 16.98 | 378.49 | 0.01 | 2.88 | 1587 |
| 2024-09-20 22:21:34.740 | MS1 | 121.4656636736 | 31.1446285412 | 616 | 504990 | -91.21 | 16.95 | 98.99 | 0.02 | 2.56 | 1569 |
| 2024-09-20 22:21:35.348 | MS1 | 121.4656614469 | 31.1446217390 | 616 | 504990 | -89.11 | 14.20 | 51.07 | 0.07 | 2.88 | 1579 |
| 2024-09-20 22:21:36.650 | MS1 | 121.4656667541 | 31.1446302074 | 616 | 504990 | -85.94 | 12.73 | 60.42 | 0.10 | 2.18 | 1589 |
| 2024-09-20 22:21:37.602 | MS1 | 121.4656599019 | 31.1446316229 | 616 | 504990 | -93.95 | 8.72 | 84.39 | 0.15 | 2.06 | 1560 |
| 2024-09-20 22:21:38.574 | MS1 | 121.4656770380 | 31.1446377625 | 616 | 504990 | -91.25 | 7.55 | 63.84 | 0.02 | 2.95 | 1564 |
| 2024-09-20 22:21:39.158 | MS1 | 121.4656581883 | 31.1446192880 | 616 | 504990 | -90.46 | 10.30 | 92.42 | 0.13 | 2.86 | 1565 |
| 2024-09-20 22:21:40.673 | MS1 | 121.4656674724 | 31.1446354704 | 616 | 504990 | -91.65 | 11.91 | 501.03 | 0.14 | 2.86 | 1590 |
| 2024-09-20 22:21:41.309 | MS1 | 121.4656766110 | 31.1446322670 | 616 | 504990 | -90.50 | 7.78 | 317.29 | 0.13 | 2.71 | 1563 |
| 2024-09-20 22:21:42.746 | MS1 | 121.4656658765 | 31.1446225284 | 616 | 504990 | -92.78 | 8.02 | 389.93 | 0.01 | 2.94 | 1591 |

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
| 3212046 | 1 | 121.4689589115 | 31.1553899360 | 123 | 7 | 1 | 29.5 | TDD | 616 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3223599 | 4 | 121.4749142252 | 31.1515423016 | 299 | 10 | 3 | 40.5 | TDD | 502 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3234535 | 2 | 121.4739121607 | 31.1521963843 | 15 | 6 | 7 | 39.9 | TDD | 427 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3245107 | 3 | 121.4642787467 | 31.1503815462 | 184 | 5 | 0 | 21.3 | TDD | 878 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.535 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.560 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.669 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.669 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.370 | NREventA3 | measId:2;ServCellPCI:614;Se... |
| 2024-09-20 22:21:38.610 | NRHandoverAttempt | SourcePCI:614;SourceNR-ARFC... |
| 2024-09-20 22:21:38.654 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.665 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.772 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.772 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3212046 | 1 | 75.3655 | 77.6968 | -116.8734 | 16.0396 | 169.3715 | 0.0193 | 0.0106 |
| 2024_09_19 22:00 | 3234535 | 2 | 79.7809 | 75.6367 | -116.6944 | 8.1587 | 141.9780 | 0.0177 | 0.0120 |
| 2024_09_19 22:00 | 3245107 | 3 | 81.0371 | 91.2945 | -115.5909 | 12.7497 | 197.9133 | 0.0083 | 0.0170 |
| 2024_09_19 22:00 | 3223599 | 4 | 84.8719 | 87.7283 | -116.9525 | 16.1716 | 80.6417 | 0.0017 | 0.0161 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413996_BA7A6C8F | 504990 | 616 | -90.1 | 504990 | 878 | -99.7 | 504990 | 502 | -101.4 | 504990 | 427 |
| MR_1774413996_393E5562 | 504990 | 616 | -92.7 | 504990 | 878 | -101.5 | 504990 | 502 | -100.1 | 504990 | 427 |
| MR_1774413996_B6329442 | 504990 | 616 | -89.6 | 504990 | 878 | -102.0 | 504990 | 502 | -102.8 | 504990 | 427 |
| MR_1774413996_4C140791 | 504990 | 616 | -90.1 | 504990 | 878 | -101.2 | 504990 | 502 | -99.9 | 504990 | 427 |
| MR_1774413996_F526FB13 | 504990 | 616 | -91.6 | 504990 | 878 | -100.1 | 504990 | 502 | -101.9 | 504990 | 427 |
| MR_1774413996_938FAC16 | 504990 | 616 | -91.0 | 504990 | 878 | -102.2 | 504990 | 502 | -102.5 | 504990 | 427 |
| MR_1774413996_F50FFAE0 | 504990 | 616 | -90.3 | 504990 | 878 | -99.5 | 504990 | 502 | -102.2 | 504990 | 427 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 685: `02371c8e-e01...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `02371c8e-e013-4bfd-9f2e-af53d3f3ec45` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225773_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[685] topology](images/train_0685.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3225773_6
- `C2`: Decrease transmission power for 3222751_2
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225773_6
- `C5`: Lift the tilt angle  of 3222751_2 by 1 degrees
- `C6`: Increase A3 Offset threshold for 3225773_6
- `C7`: Press down the tilt angle of 3225773_6 by 1 degrees
- `C8`: Add neighbor relationship between 3225773_6 and 3222751_2
- `C9`: Decrease A3 Offset threshold for 3222751_2
- `C10`: Increase transmission power for 3222751_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225773_6 **← 정답**
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222751_2
- `C13`: Decrease A3 Offset threshold for 3225773_6
- `C14`: Add neighbor relationship between 3261548_13 and 3222751_2
- `C15`: Lift the tilt angle of 3225773_6 by 1 degrees
- `C16`: Adjust the azimuth of 3222751_2 by 32 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222751_2
- `C18`: Increase transmission power for 3225773_6
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle  of 3222751_2 by 1 degrees
- `C21`: Increase A3 Offset threshold for 3222751_2
- `C22`: Adjust the azimuth of 3225773_6 by 1 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.435 | MS1 | 121.4656733379 | 31.1446312264 | 847 | 504990 | -95.58 | 12.59 | 594.29 | 0.10 | 2.82 | 1598 |
| 2024-09-20 22:21:32.368 | MS1 | 121.4656709382 | 31.1446331580 | 649 | 504990 | -95.60 | 10.85 | 449.02 | 0.11 | 2.85 | 1596 |
| 2024-09-20 22:21:33.264 | MS1 | 121.4656622820 | 31.1446228101 | 683 | 504990 | -93.85 | 11.94 | 547.44 | 0.08 | 2.39 | 1598 |
| 2024-09-20 22:21:34.977 | MS1 | 121.4656696171 | 31.1446284657 | 346 | 152650 | -95.70 | 5.79 | 88.82 | 0.12 | 1.88 | 912 |
| 2024-09-20 22:21:35.905 | MS1 | 121.4656703054 | 31.1446278792 | 881 | 152650 | -88.87 | 5.17 | 91.79 | 0.07 | 1.89 | 915 |
| 2024-09-20 22:21:36.726 | MS1 | 121.4656628645 | 31.1446192727 | 990 | 152650 | -95.70 | 4.58 | 77.28 | 0.19 | 1.84 | 938 |
| 2024-09-20 22:21:37.920 | MS1 | 121.4656714050 | 31.1446314077 | 265 | 152650 | -95.17 | 7.64 | 95.95 | 0.02 | 1.90 | 998 |
| 2024-09-20 22:21:38.300 | MS1 | 121.4656580930 | 31.1446282668 | 346 | 152650 | -88.64 | 2.72 | 61.38 | 0.09 | 1.94 | 909 |
| 2024-09-20 22:21:39.468 | MS1 | 121.4656659105 | 31.1446295622 | 881 | 152650 | -89.57 | 7.43 | 74.84 | 0.05 | 1.73 | 925 |
| 2024-09-20 22:21:40.772 | MS1 | 121.4656654083 | 31.1446191109 | 990 | 152650 | -88.35 | 4.51 | 55.77 | 0.05 | 2.31 | 1596 |
| 2024-09-20 22:21:41.582 | MS1 | 121.4656673018 | 31.1446319491 | 265 | 152650 | -93.19 | 2.67 | 85.37 | 0.02 | 2.36 | 1575 |
| 2024-09-20 22:21:42.579 | MS1 | 121.4656733763 | 31.1446268388 | 346 | 152650 | -87.47 | 2.18 | 95.87 | 0.09 | 2.69 | 1566 |

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
| 3216954 | 5 | 121.4746522369 | 31.1549057837 | 281 | 9 | 4 | 3.3 | TDD | 587 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3217788 | 1 | 121.4726330887 | 31.1496665566 | 229 | 9 | 2 | 2.2 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3221926 | 12 | 121.4648025239 | 31.1494948334 | 338 | 9 | 10 | 20.4 | FDD | 346 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3222751 | 2 | 121.4674990694 | 31.1463309548 | 255 | 0 | 4 | 4.7 | TDD | 4 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3223569 | 7 | 121.4676831231 | 31.1476665282 | 180 | 4 | 6 | 13.8 | FDD | 934 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3224533 | 4 | 121.4691413277 | 31.1500759466 | 301 | 7 | 11 | 29.3 | TDD | 683 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3225773 | 6 | 121.4653241911 | 31.1528394529 | 179 | 0 | 2 | 16.0 | TDD | 847 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3236105 | 9 | 121.4728355167 | 31.1544395355 | 88 | 14 | 6 | 22.6 | FDD | 7 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3241391 | 3 | 121.4660758754 | 31.1494901685 | 155 | 14 | 7 | 2.6 | TDD | 649 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3244519 | 8 | 121.4757538312 | 31.1458193105 | 31 | 7 | 12 | 27.3 | FDD | 167 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3253169 | 10 | 121.4746549866 | 31.1539047961 | 323 | 3 | 6 | 28.9 | FDD | 265 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3261548 | 13 | 121.4682289677 | 31.1440232107 | 156 | 12 | 4 | 13.7 | FDD | 990 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3262402 | 11 | 121.4674630572 | 31.1548656515 | 217 | 9 | 7 | 18.7 | FDD | 881 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |

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
| 2024-09-20 22:21:31.126 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.151 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.258 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.258 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.990 | NREventA2 | measId:1;ServCellPCI:600;Se... |
| 2024-09-20 22:21:35.092 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.348 | NREventA5 | measId:3;ServCellPCI:600;Se... |
| 2024-09-20 22:21:35.379 | NRHandoverAttempt | SourcePCI:600;SourceNR-ARFC... |
| 2024-09-20 22:21:35.404 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.416 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.541 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.541 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217788 | 1 | 19.4614 | 9.0622 | -114.6768 | 10.8429 | 182.5239 | 0.0144 | 0.0146 |
| 2024_09_20 22:00 | 3222751 | 2 | 11.2826 | 12.3054 | -116.3575 | 15.7609 | 83.7553 | 0.0098 | 0.0156 |
| 2024_09_20 22:00 | 3241391 | 3 | 14.8351 | 10.1692 | -116.3019 | 7.3541 | 97.4678 | 0.0162 | 0.0008 |
| 2024_09_20 22:00 | 3224533 | 4 | 6.0123 | 12.1356 | -114.4086 | 16.8191 | 144.8306 | 0.0044 | 0.0144 |
| 2024_09_20 22:00 | 3216954 | 5 | 10.9445 | 7.1153 | -116.6860 | 6.2500 | 192.6667 | 0.0176 | 0.0155 |
| 2024_09_20 22:00 | 3225773 | 6 | 16.7208 | 15.0929 | -116.6242 | 17.1820 | 192.5530 | 0.0158 | 0.0003 |
| 2024_09_20 22:00 | 3223569 | 7 | 15.1112 | 14.3825 | -114.2643 | 4.6448 | 31.7986 | 0.0007 | 0.0112 |
| 2024_09_20 22:00 | 3244519 | 8 | 14.9859 | 13.3154 | -114.5306 | 3.5519 | 43.0220 | 0.0052 | 0.0042 |
| 2024_09_20 22:00 | 3236105 | 9 | 6.6936 | 6.8717 | -117.9338 | 3.5260 | 41.5892 | 0.0122 | 0.0026 |
| 2024_09_20 22:00 | 3253169 | 10 | 5.1993 | 17.4334 | -114.7741 | 4.6032 | 59.8074 | 0.0019 | 0.0036 |
| 2024_09_20 22:00 | 3262402 | 11 | 11.7571 | 7.0545 | -116.7839 | 3.7477 | 30.4461 | 0.0039 | 0.0007 |
| 2024_09_20 22:00 | 3221926 | 12 | 13.0089 | 17.9512 | -116.5765 | 3.5867 | 43.1134 | 0.0125 | 0.0180 |
| 2024_09_20 22:00 | 3261548 | 13 | 13.6216 | 9.7665 | -117.7952 | 3.2014 | 23.7291 | 0.0028 | 0.0004 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414814_B4756E4C | 152650 | 346 | -94.9 | 152650 | 934 | -102.6 | 152650 | 167 | -105.0 | 152650 | 7 |
| MR_1774414814_205186D9 | 504990 | 683 | -92.6 | 504990 | 4 | -94.7 | 504990 | 258 | -102.0 | 504990 | 587 |
| MR_1774414814_5F156E9F | 504990 | 683 | -93.5 | 504990 | 4 | -96.9 | 504990 | 258 | -101.2 | 504990 | 587 |
| MR_1774414814_9FEED391 | 152650 | 346 | -94.3 | 152650 | 934 | -102.8 | 152650 | 167 | -105.0 | 152650 | 7 |
| MR_1774414814_8E80C45D | 504990 | 683 | -94.1 | 504990 | 4 | -97.0 | 504990 | 258 | -102.0 | 504990 | 587 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 686: `120c0516-601...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `120c0516-601a-4a1e-8dc2-514b82edb9c8` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease A3 Offset threshold for 3228039_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[686] topology](images/train_0686.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234907_2
- `C2`: Decrease A3 Offset threshold for 3234907_2
- `C3`: Increase transmission power for 3228039_3
- `C4`: Add neighbor relationship between 3217399_1 and 3234907_2
- `C5`: Check test server and transmission issues
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228039_3
- `C7`: Decrease transmission power for 3228039_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228039_3
- `C9`: Adjust the azimuth of 3228039_3 by 22 degrees
- `C10`: Increase A3 Offset threshold for 3234907_2
- `C11`: Decrease transmission power for 3234907_2
- `C12`: Add neighbor relationship between 3228039_3 and 3234907_2
- `C13`: Lift the tilt angle  of 3234907_2 by 10 degrees
- `C14`: Press down the tilt angle of 3228039_3 by 10 degrees
- `C15`: Increase A3 Offset threshold for 3228039_3
- `C16`: Increase transmission power for 3234907_2
- `C17`: Lift the tilt angle of 3228039_3 by 10 degrees
- `C18`: Press down the tilt angle  of 3234907_2 by 10 degrees
- `C19`: Adjust the azimuth of 3234907_2 by 38 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease A3 Offset threshold for 3228039_3 **← 정답**
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234907_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.585 | MS1 | 121.4656595488 | 31.1446244744 | 319 | 504990 | -83.23 | 17.62 | 568.23 | 0.03 | 2.52 | 1565 |
| 2024-09-20 22:21:32.728 | MS1 | 121.4656702326 | 31.1446368196 | 319 | 504990 | -84.73 | 15.85 | 439.23 | 0.03 | 2.16 | 1593 |
| 2024-09-20 22:21:33.506 | MS1 | 121.4656648375 | 31.1446185698 | 319 | 504990 | -81.37 | 14.00 | 395.82 | 0.19 | 2.79 | 1577 |
| 2024-09-20 22:21:34.478 | MS1 | 121.4656768132 | 31.1446356804 | 319 | 504990 | -89.87 | -1.79 | 30.95 | 0.09 | 1.22 | 1598 |
| 2024-09-20 22:21:35.671 | MS1 | 121.4656668945 | 31.1446276788 | 319 | 504990 | -87.90 | -3.55 | 55.89 | 0.04 | 1.09 | 1576 |
| 2024-09-20 22:21:36.907 | MS1 | 121.4656657825 | 31.1446334325 | 319 | 504990 | -90.59 | -1.01 | 76.74 | 0.17 | 1.06 | 1564 |
| 2024-09-20 22:21:37.429 | MS1 | 121.4656669286 | 31.1446210017 | 319 | 504990 | -84.20 | -2.03 | 68.03 | 0.01 | 1.42 | 1585 |
| 2024-09-20 22:21:38.389 | MS1 | 121.4656746191 | 31.1446196178 | 319 | 504990 | -91.52 | -3.63 | 57.70 | 0.01 | 1.43 | 1591 |
| 2024-09-20 22:21:39.678 | MS1 | 121.4656731047 | 31.1446320581 | 868 | 504990 | -75.29 | 12.41 | 219.32 | 0.14 | 1.11 | 1573 |
| 2024-09-20 22:21:40.835 | MS1 | 121.4656609753 | 31.1446335779 | 868 | 504990 | -80.76 | 17.88 | 339.19 | 0.00 | 2.43 | 1579 |
| 2024-09-20 22:21:41.434 | MS1 | 121.4656665491 | 31.1446236105 | 868 | 504990 | -76.62 | 17.46 | 452.08 | 0.07 | 2.20 | 1594 |
| 2024-09-20 22:21:42.933 | MS1 | 121.4656700475 | 31.1446359744 | 868 | 504990 | -79.69 | 14.59 | 432.73 | 0.07 | 2.87 | 1588 |

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
| 3217399 | 1 | 121.4751191969 | 31.1506176125 | 0 | 0 | 11 | 49.9 | TDD | 656 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3228039 | 3 | 121.4643269522 | 31.1458659585 | 115 | 10 | 1 | 28.1 | TDD | 319 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3234907 | 2 | 121.4745975765 | 31.1559194764 | 176 | 10 | 11 | 24.7 | TDD | 868 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3272685 | 4 | 121.4749744258 | 31.1488342902 | 52 | 1 | 11 | 15.5 | TDD | 15 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.749 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.769 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.909 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.909 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.613 | NREventA3 | measId:2;ServCellPCI:270;Se... |
| 2024-09-20 22:21:37.853 | NRHandoverAttempt | SourcePCI:270;SourceNR-ARFC... |
| 2024-09-20 22:21:37.888 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.898 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.023 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.023 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217399 | 1 | 5.7142 | 14.1730 | -117.6731 | 9.2105 | 154.9701 | 0.0091 | 0.0087 |
| 2024_09_20 22:00 | 3234907 | 2 | 15.1606 | 19.6037 | -116.2286 | 15.0063 | 121.9739 | 0.0068 | 0.0129 |
| 2024_09_20 22:00 | 3228039 | 3 | 19.3166 | 17.8817 | -115.9300 | 13.7845 | 86.8546 | 0.0123 | 0.1010 |
| 2024_09_20 22:00 | 3272685 | 4 | 17.1667 | 18.9616 | -114.8611 | 17.1989 | 192.1003 | 0.0046 | 0.0014 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416929_7E76F7E5 | 504990 | 868 | -85.1 | 504990 | 319 | -88.4 | 504990 | 656 | -89.9 | 504990 | 15 |
| MR_1774416929_0B86DEF0 | 504990 | 319 | -88.9 | 504990 | 868 | -84.1 | 504990 | 656 | -89.7 | 504990 | 15 |
| MR_1774416929_DF3E3CA9 | 504990 | 868 | -83.6 | 504990 | 319 | -88.8 | 504990 | 656 | -88.6 | 504990 | 15 |
| MR_1774416929_6021F3C5 | 504990 | 868 | -85.2 | 504990 | 319 | -89.8 | 504990 | 656 | -88.7 | 504990 | 15 |
| MR_1774416929_9B903BEF | 504990 | 868 | -86.6 | 504990 | 319 | -88.1 | 504990 | 656 | -91.6 | 504990 | 15 |
| MR_1774416929_3F6706DB | 504990 | 319 | -88.3 | 504990 | 868 | -84.3 | 504990 | 656 | -91.7 | 504990 | 15 |
| MR_1774416929_5901DFED | 504990 | 868 | -86.7 | 504990 | 319 | -89.3 | 504990 | 656 | -88.5 | 504990 | 15 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 687: `22e0ad0d-0f7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `22e0ad0d-0f79-4bca-8323-2d3bd7247b0c` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[687] topology](images/train_0687.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment. **← 정답**
- `C2`: Adjust the azimuth of 3266564_3 by 42 degrees
- `C3`: Decrease transmission power for 3266564_3
- `C4`: Decrease A3 Offset threshold for 3266564_3
- `C5`: Adjust the azimuth of 3253112_1 by 50 degrees
- `C6`: Lift the tilt angle of 3266564_3 by 4 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266564_3
- `C8`: Add neighbor relationship between 3266564_3 and 3253112_1
- `C9`: Increase A3 Offset threshold for 3253112_1
- `C10`: Decrease A3 Offset threshold for 3253112_1
- `C11`: Lift the tilt angle  of 3253112_1 by 10 degrees
- `C12`: Increase transmission power for 3253112_1
- `C13`: Add neighbor relationship between 3236021_4 and 3253112_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253112_1
- `C15`: Decrease transmission power for 3253112_1
- `C16`: Check test server and transmission issues
- `C17`: Press down the tilt angle  of 3253112_1 by 10 degrees
- `C18`: Increase transmission power for 3266564_3
- `C19`: Press down the tilt angle of 3266564_3 by 4 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253112_1
- `C21`: Increase A3 Offset threshold for 3266564_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266564_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.334 | MS1 | 121.4656702776 | 31.1446332733 | 84 | 504990 | -89.82 | 17.94 | 590.09 | 0.09 | 2.93 | 1563 |
| 2024-09-20 22:21:32.275 | MS1 | 121.4656584285 | 31.1446252798 | 84 | 504990 | -85.03 | 12.52 | 584.61 | 0.03 | 2.44 | 1595 |
| 2024-09-20 22:21:33.575 | MS1 | 121.4656612742 | 31.1446253849 | 84 | 504990 | -89.12 | 16.24 | 376.86 | 0.18 | 2.16 | 1590 |
| 2024-09-20 22:21:34.921 | MS1 | 121.4656691783 | 31.1446354172 | 84 | 504990 | -89.09 | 13.05 | 57.60 | 0.10 | 2.28 | 1561 |
| 2024-09-20 22:21:35.794 | MS1 | 121.4656660252 | 31.1446316193 | 84 | 504990 | -90.44 | 14.72 | 69.21 | 0.05 | 2.05 | 1569 |
| 2024-09-20 22:21:36.533 | MS1 | 121.4656772263 | 31.1446234508 | 84 | 504990 | -88.32 | 15.99 | 99.78 | 0.14 | 2.59 | 1575 |
| 2024-09-20 22:21:37.468 | MS1 | 121.4656757053 | 31.1446217910 | 84 | 504990 | -93.24 | 7.43 | 81.45 | 0.08 | 2.90 | 1571 |
| 2024-09-20 22:21:38.872 | MS1 | 121.4656717264 | 31.1446262082 | 84 | 504990 | -92.49 | 7.08 | 65.09 | 0.13 | 2.43 | 1576 |
| 2024-09-20 22:21:39.428 | MS1 | 121.4656585145 | 31.1446298581 | 84 | 504990 | -93.49 | 12.82 | 63.79 | 0.08 | 2.51 | 1569 |
| 2024-09-20 22:21:40.303 | MS1 | 121.4656643699 | 31.1446283488 | 84 | 504990 | -91.24 | 12.94 | 598.81 | 0.17 | 2.25 | 1560 |
| 2024-09-20 22:21:41.717 | MS1 | 121.4656597395 | 31.1446281589 | 84 | 504990 | -91.77 | 10.44 | 572.17 | 0.17 | 2.00 | 1564 |
| 2024-09-20 22:21:42.370 | MS1 | 121.4656654565 | 31.1446367804 | 84 | 504990 | -89.89 | 8.34 | 440.86 | 0.10 | 2.81 | 1580 |

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
| 3236021 | 4 | 121.4718684390 | 31.1538417300 | 307 | 12 | 4 | 16.3 | TDD | 31 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3253112 | 1 | 121.4689326672 | 31.1456809790 | 347 | 7 | 11 | 34.3 | TDD | 922 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3266564 | 3 | 121.4725575141 | 31.1527799365 | 258 | 2 | 7 | 41.6 | TDD | 84 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3279969 | 2 | 121.4651518936 | 31.1459605900 | 44 | 13 | 12 | 38.1 | TDD | 347 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.456 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.473 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.581 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.581 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.273 | NREventA3 | measId:2;ServCellPCI:448;Se... |
| 2024-09-20 22:21:38.513 | NRHandoverAttempt | SourcePCI:448;SourceNR-ARFC... |
| 2024-09-20 22:21:38.547 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.558 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.663 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.663 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3253112 | 1 | 92.2037 | 75.4126 | -117.4752 | 10.8973 | 136.2753 | 0.0141 | 0.0073 |
| 2024_09_19 22:00 | 3279969 | 2 | 94.6220 | 80.3405 | -115.2819 | 17.3352 | 164.2083 | 0.0194 | 0.0166 |
| 2024_09_19 22:00 | 3266564 | 3 | 78.9542 | 79.2075 | -117.9855 | 7.8406 | 172.4361 | 0.0013 | 0.0161 |
| 2024_09_19 22:00 | 3236021 | 4 | 76.8428 | 79.3519 | -117.1427 | 16.0547 | 102.3407 | 0.0149 | 0.0168 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414256_FB483A6F | 504990 | 84 | -87.8 | 504990 | 922 | -91.5 | 504990 | 31 | -102.9 | 504990 | 347 |
| MR_1774414256_442645F9 | 504990 | 84 | -88.8 | 504990 | 922 | -91.2 | 504990 | 31 | -102.0 | 504990 | 347 |
| MR_1774414256_7B7D016D | 504990 | 84 | -87.4 | 504990 | 922 | -92.2 | 504990 | 31 | -101.6 | 504990 | 347 |
| MR_1774414256_3675FE26 | 504990 | 84 | -90.1 | 504990 | 922 | -89.9 | 504990 | 31 | -104.7 | 504990 | 347 |
| MR_1774414256_DEEF611A | 504990 | 84 | -91.1 | 504990 | 922 | -91.8 | 504990 | 31 | -104.0 | 504990 | 347 |
| MR_1774414256_5FBFD617 | 504990 | 84 | -88.7 | 504990 | 922 | -92.3 | 504990 | 31 | -101.5 | 504990 | 347 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 688: `ff8ebed6-d2b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ff8ebed6-d2be-4f43-8d4a-b5407f548b25` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[688] topology](images/train_0688.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3269212_2 by 10 degrees
- `C2`: Increase transmission power for 3269212_2
- `C3`: Press down the tilt angle  of 3245913_1 by 10 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245913_1
- `C5`: Add neighbor relationship between 3269212_2 and 3245913_1
- `C6`: Lift the tilt angle  of 3245913_1 by 10 degrees
- `C7`: Adjust the azimuth of 3269212_2 by 24 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269212_2
- `C9`: Decrease transmission power for 3269212_2
- `C10`: Check test server and transmission issues
- `C11`: Press down the tilt angle of 3269212_2 by 10 degrees
- `C12`: Increase A3 Offset threshold for 3269212_2
- `C13`: Decrease transmission power for 3245913_1
- `C14`: Increase transmission power for 3245913_1
- `C15`: Decrease A3 Offset threshold for 3245913_1
- `C16`: Add neighbor relationship between 3270195_3 and 3245913_1
- `C17`: Decrease A3 Offset threshold for 3269212_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245913_1
- `C19`: Adjust the azimuth of 3245913_1 by 0 degrees
- `C20`: Insufficient data; more data is needed for judgment. **← 정답**
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269212_2
- `C22`: Increase A3 Offset threshold for 3245913_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.345 | MS1 | 121.4656646418 | 31.1446186264 | 252 | 504990 | -85.93 | 17.03 | 414.21 | 0.02 | 2.09 | 1569 |
| 2024-09-20 22:21:32.685 | MS1 | 121.4656669834 | 31.1446198417 | 252 | 504990 | -90.63 | 17.17 | 342.43 | 0.06 | 2.09 | 1571 |
| 2024-09-20 22:21:33.532 | MS1 | 121.4656604101 | 31.1446311483 | 252 | 504990 | -88.23 | 12.63 | 353.15 | 0.08 | 2.69 | 1582 |
| 2024-09-20 22:21:34.533 | MS1 | 121.4656580421 | 31.1446305641 | 252 | 504990 | -86.81 | 17.07 | 53.15 | 0.00 | 2.83 | 1585 |
| 2024-09-20 22:21:35.470 | MS1 | 121.4656651038 | 31.1446360268 | 252 | 504990 | -87.49 | 14.28 | 53.04 | 0.04 | 2.74 | 1571 |
| 2024-09-20 22:21:36.353 | MS1 | 121.4656712313 | 31.1446364791 | 252 | 504990 | -85.75 | 15.58 | 99.15 | 0.12 | 2.25 | 1589 |
| 2024-09-20 22:21:37.445 | MS1 | 121.4656719131 | 31.1446357883 | 252 | 504990 | -93.54 | 10.46 | 85.46 | 0.13 | 2.45 | 1592 |
| 2024-09-20 22:21:38.165 | MS1 | 121.4656667111 | 31.1446336484 | 252 | 504990 | -91.51 | 11.28 | 84.08 | 0.18 | 2.26 | 1585 |
| 2024-09-20 22:21:39.759 | MS1 | 121.4656613513 | 31.1446347642 | 252 | 504990 | -93.36 | 9.42 | 106.70 | 0.10 | 2.98 | 1599 |
| 2024-09-20 22:21:40.616 | MS1 | 121.4656730014 | 31.1446266364 | 252 | 504990 | -91.58 | 12.11 | 480.02 | 0.15 | 2.84 | 1575 |
| 2024-09-20 22:21:41.859 | MS1 | 121.4656743918 | 31.1446202905 | 252 | 504990 | -91.63 | 7.30 | 339.41 | 0.18 | 2.38 | 1569 |
| 2024-09-20 22:21:42.990 | MS1 | 121.4656759261 | 31.1446278026 | 252 | 504990 | -89.92 | 7.88 | 404.66 | 0.03 | 2.93 | 1577 |

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
| 3245913 | 1 | 121.4654830855 | 31.1516394949 | 179 | 9 | 12 | 26.5 | TDD | 692 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3251077 | 4 | 121.4668644443 | 31.1485884479 | 339 | 2 | 10 | 37.0 | TDD | 68 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3269212 | 2 | 121.4667757686 | 31.1477276309 | 173 | 11 | 10 | 16.5 | TDD | 252 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3270195 | 3 | 121.4653961818 | 31.1529859650 | 214 | 10 | 10 | 34.3 | TDD | 790 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.465 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.488 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.637 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.637 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.292 | NREventA3 | measId:2;ServCellPCI:69;Ser... |
| 2024-09-20 22:21:38.532 | NRHandoverAttempt | SourcePCI:69;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.567 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.578 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.705 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.705 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3245913 | 1 | 94.8283 | 89.5291 | -116.3211 | 16.8272 | 175.5517 | 0.0126 | 0.0128 |
| 2024_09_19 22:00 | 3269212 | 2 | 87.4238 | 85.6843 | -115.7503 | 5.9159 | 181.1677 | 0.0175 | 0.0016 |
| 2024_09_19 22:00 | 3270195 | 3 | 76.7161 | 75.7759 | -117.8293 | 6.3091 | 146.8155 | 0.0182 | 0.0013 |
| 2024_09_19 22:00 | 3251077 | 4 | 91.8311 | 94.7143 | -114.4507 | 9.9634 | 148.2221 | 0.0048 | 0.0010 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412505_CACD2B79 | 504990 | 252 | -88.5 | 504990 | 692 | -87.5 | 504990 | 790 | -92.4 | 504990 | 68 |
| MR_1774412505_0074FE67 | 504990 | 252 | -88.8 | 504990 | 692 | -88.2 | 504990 | 790 | -94.6 | 504990 | 68 |
| MR_1774412505_548A0CF4 | 504990 | 252 | -85.7 | 504990 | 692 | -89.6 | 504990 | 790 | -93.6 | 504990 | 68 |
| MR_1774412505_97191C6E | 504990 | 252 | -88.5 | 504990 | 692 | -88.6 | 504990 | 790 | -92.0 | 504990 | 68 |
| MR_1774412505_0D5CC4AB | 504990 | 252 | -88.0 | 504990 | 692 | -90.0 | 504990 | 790 | -91.9 | 504990 | 68 |
| MR_1774412505_82E538F5 | 504990 | 252 | -88.3 | 504990 | 692 | -88.5 | 504990 | 790 | -93.2 | 504990 | 68 |
| MR_1774412505_B4FDB5E9 | 504990 | 252 | -86.3 | 504990 | 692 | -87.1 | 504990 | 790 | -92.3 | 504990 | 68 |
| MR_1774412505_62490D34 | 504990 | 252 | -87.0 | 504990 | 692 | -89.8 | 504990 | 790 | -91.2 | 504990 | 68 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 689: `596dc986-ef9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `596dc986-ef9c-4389-9374-457260f8bd75` |
| Tag | **multiple-answer** |
| 정답 | **C13|C14** |
| C13 의미 | Adjust the azimuth of 3221097_1 by 50 degrees |
| C14 의미 | Increase transmission power for 3221097_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[689] topology](images/train_0689.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229041_3
- `C2`: Decrease A3 Offset threshold for 3221097_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229041_3
- `C4`: Decrease transmission power for 3221097_1
- `C5`: Adjust the azimuth of 3229041_3 by 46 degrees
- `C6`: Decrease transmission power for 3229041_3
- `C7`: Press down the tilt angle of 3221097_1 by 3 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221097_1
- `C9`: Increase A3 Offset threshold for 3221097_1
- `C10`: Add neighbor relationship between 3221097_1 and 3229041_3
- `C11`: Increase A3 Offset threshold for 3229041_3
- `C12`: Lift the tilt angle of 3221097_1 by 3 degrees
- `C13`: Adjust the azimuth of 3221097_1 by 50 degrees **← 정답**
- `C14`: Increase transmission power for 3221097_1 **← 정답**
- `C15`: Lift the tilt angle  of 3229041_3 by 5 degrees
- `C16`: Increase transmission power for 3229041_3
- `C17`: Add neighbor relationship between 3225215_2 and 3229041_3
- `C18`: Decrease A3 Offset threshold for 3229041_3
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221097_1
- `C21`: Press down the tilt angle  of 3229041_3 by 5 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.197 | MS1 | 121.4656733304 | 31.1446285087 | 32 | 504990 | -94.66 | 12.66 | 316.60 | 0.11 | 2.37 | 1566 |
| 2024-09-20 22:21:32.234 | MS1 | 121.4656741357 | 31.1446361118 | 32 | 504990 | -94.00 | 15.53 | 473.57 | 0.14 | 2.86 | 1587 |
| 2024-09-20 22:21:33.393 | MS1 | 121.4656711922 | 31.1446223584 | 32 | 504990 | -85.82 | 12.73 | 490.44 | 0.05 | 2.13 | 1569 |
| 2024-09-20 22:21:34.754 | MS1 | 121.4656673906 | 31.1446189481 | 32 | 504990 | -100.31 | -0.80 | 19.24 | 0.15 | 1.04 | 1573 |
| 2024-09-20 22:21:35.416 | MS1 | 121.4656684786 | 31.1446210208 | 32 | 504990 | -102.31 | 1.13 | 48.27 | 0.04 | 1.43 | 1569 |
| 2024-09-20 22:21:36.738 | MS1 | 121.4656582914 | 31.1446256143 | 32 | 504990 | -100.25 | -1.72 | 19.84 | 0.14 | 1.23 | 1580 |
| 2024-09-20 22:21:37.256 | MS1 | 121.4656627350 | 31.1446295959 | 32 | 504990 | -100.45 | 0.64 | 18.54 | 0.07 | 1.16 | 1576 |
| 2024-09-20 22:21:38.776 | MS1 | 121.4656653157 | 31.1446220388 | 32 | 504990 | -106.50 | 0.22 | 21.48 | 0.09 | 1.36 | 1577 |
| 2024-09-20 22:21:39.309 | MS1 | 121.4656774151 | 31.1446327179 | 32 | 504990 | -101.05 | -0.74 | 53.18 | 0.04 | 1.03 | 1590 |
| 2024-09-20 22:21:40.607 | MS1 | 121.4656647943 | 31.1446350719 | 32 | 504990 | -90.70 | 16.99 | 370.25 | 0.16 | 2.57 | 1585 |
| 2024-09-20 22:21:41.487 | MS1 | 121.4656746007 | 31.1446377125 | 32 | 504990 | -87.89 | 14.99 | 569.15 | 0.14 | 2.82 | 1590 |
| 2024-09-20 22:21:42.364 | MS1 | 121.4656767914 | 31.1446181392 | 32 | 504990 | -89.80 | 17.64 | 422.18 | 0.04 | 2.39 | 1568 |

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
| 3221097 | 1 | 121.4642538326 | 31.1539853673 | 236 | 1 | 5 | 38.3 | TDD | 32 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3225215 | 2 | 121.4693896190 | 31.1533703178 | 252 | 14 | 0 | 15.3 | TDD | 321 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3229041 | 3 | 121.4702755196 | 31.1450276518 | 310 | 1 | 4 | 27.5 | TDD | 927 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3264623 | 4 | 121.4680315331 | 31.1441951484 | 159 | 9 | 1 | 21.8 | TDD | 519 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.093 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.110 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.259 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.259 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.402 | NREventA2 | measId:1;ServCellPCI:351;Se... |
| 2024-09-20 22:21:34.529 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221097 | 1 | 10.7320 | 18.8330 | -117.4826 | 5.9997 | 191.5614 | 0.1717 | 0.0016 |
| 2024_09_20 22:00 | 3225215 | 2 | 16.5054 | 16.7366 | -115.6644 | 19.8601 | 157.2229 | 0.0156 | 0.0036 |
| 2024_09_20 22:00 | 3229041 | 3 | 16.0345 | 18.8863 | -116.1071 | 9.7251 | 167.6880 | 0.0132 | 0.0037 |
| 2024_09_20 22:00 | 3264623 | 4 | 8.4108 | 16.1929 | -115.4357 | 16.8266 | 124.0556 | 0.0175 | 0.0179 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415713_25BD382D | 504990 | 32 | -101.4 | 504990 | 927 | -104.6 | 504990 | 321 | -107.6 | 504990 | 519 |
| MR_1774415713_07530025 | 504990 | 32 | -99.9 | 504990 | 927 | -106.3 | 504990 | 321 | -107.0 | 504990 | 519 |
| MR_1774415713_1562FEAD | 504990 | 32 | -100.9 | 504990 | 927 | -105.0 | 504990 | 321 | -107.8 | 504990 | 519 |
| MR_1774415713_AADB9391 | 504990 | 32 | -100.7 | 504990 | 927 | -104.5 | 504990 | 321 | -106.9 | 504990 | 519 |
| MR_1774415713_6B60CF49 | 504990 | 32 | -98.8 | 504990 | 927 | -102.4 | 504990 | 321 | -107.0 | 504990 | 519 |
| MR_1774415713_ABE6AC87 | 504990 | 32 | -98.3 | 504990 | 927 | -106.0 | 504990 | 321 | -107.5 | 504990 | 519 |
| MR_1774415713_63D79AC7 | 504990 | 32 | -99.4 | 504990 | 927 | -106.3 | 504990 | 321 | -108.6 | 504990 | 519 |

> *... 2개 열 생략 (전체 14열)*

---
