# Track A 문제 분석 — train[1330]~train[1339]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1330] ~ train[1339] (10개)

## 목차

1. [문제 1330: `5c8aa8d7-6ba...`](#1330) — single-answer, 정답: C7
2. [문제 1331: `e18d9d0d-003...`](#1331) — single-answer, 정답: C12
3. [문제 1332: `2929ca46-d1b...`](#1332) — single-answer, 정답: C20
4. [문제 1333: `12b4a596-bd9...`](#1333) — single-answer, 정답: C17
5. [문제 1334: `2cb06c21-e33...`](#1334) — multiple-answer, 정답: C5|C6|C14|C19
6. [문제 1335: `945156cb-29c...`](#1335) — single-answer, 정답: C13
7. [문제 1336: `d06fb648-d4c...`](#1336) — single-answer, 정답: C21
8. [문제 1337: `a8e4eaf2-9be...`](#1337) — single-answer, 정답: C16
9. [문제 1338: `867e0e5b-fc9...`](#1338) — single-answer, 정답: C5
10. [문제 1339: `58f13558-a2b...`](#1339) — multiple-answer, 정답: C5|C12

---

### 문제 1330: `5c8aa8d7-6ba...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5c8aa8d7-6ba0-4519-a944-23b9bb48db86` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223914_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1330] topology](images/train_1330.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease transmission power for 3223914_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229353_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229353_2
- `C5`: Press down the tilt angle  of 3229353_2 by 6 degrees
- `C6`: Decrease A3 Offset threshold for 3223914_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223914_1 **← 정답**
- `C8`: Adjust the azimuth of 3229353_2 by 32 degrees
- `C9`: Decrease A3 Offset threshold for 3229353_2
- `C10`: Press down the tilt angle of 3223914_1 by 4 degrees
- `C11`: Lift the tilt angle  of 3229353_2 by 6 degrees
- `C12`: Add neighbor relationship between 3223914_1 and 3229353_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223914_1
- `C14`: Lift the tilt angle of 3223914_1 by 4 degrees
- `C15`: Increase transmission power for 3229353_2
- `C16`: Adjust the azimuth of 3223914_1 by 2 degrees
- `C17`: Increase transmission power for 3223914_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Increase A3 Offset threshold for 3223914_1
- `C20`: Decrease transmission power for 3229353_2
- `C21`: Increase A3 Offset threshold for 3229353_2
- `C22`: Add neighbor relationship between 3276344_11 and 3229353_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.796 | MS1 | 121.4656663480 | 31.1446274758 | 289 | 504990 | -94.73 | 12.08 | 434.41 | 0.08 | 2.64 | 1596 |
| 2024-09-20 22:21:32.892 | MS1 | 121.4656668964 | 31.1446234909 | 540 | 504990 | -95.97 | 13.17 | 505.95 | 0.09 | 2.29 | 1569 |
| 2024-09-20 22:21:33.911 | MS1 | 121.4656614989 | 31.1446238632 | 798 | 504990 | -93.55 | 13.19 | 349.97 | 0.13 | 2.39 | 1583 |
| 2024-09-20 22:21:34.220 | MS1 | 121.4656733616 | 31.1446366730 | 680 | 152650 | -90.53 | 2.05 | 78.17 | 0.01 | 1.73 | 931 |
| 2024-09-20 22:21:35.955 | MS1 | 121.4656708714 | 31.1446286503 | 372 | 152650 | -94.52 | 2.87 | 62.41 | 0.14 | 1.79 | 932 |
| 2024-09-20 22:21:36.902 | MS1 | 121.4656748086 | 31.1446256939 | 889 | 152650 | -96.27 | 5.23 | 101.34 | 0.05 | 1.94 | 996 |
| 2024-09-20 22:21:37.867 | MS1 | 121.4656678899 | 31.1446324549 | 430 | 152650 | -92.60 | 5.30 | 88.76 | 0.02 | 1.97 | 923 |
| 2024-09-20 22:21:38.616 | MS1 | 121.4656694535 | 31.1446360974 | 680 | 152650 | -95.97 | 6.18 | 93.28 | 0.07 | 1.71 | 907 |
| 2024-09-20 22:21:39.500 | MS1 | 121.4656618028 | 31.1446185431 | 372 | 152650 | -90.37 | 3.49 | 96.84 | 0.17 | 1.50 | 946 |
| 2024-09-20 22:21:40.339 | MS1 | 121.4656623694 | 31.1446267346 | 889 | 152650 | -96.93 | 4.26 | 65.48 | 0.02 | 2.71 | 1581 |
| 2024-09-20 22:21:41.261 | MS1 | 121.4656604176 | 31.1446356373 | 430 | 152650 | -96.82 | 4.88 | 74.86 | 0.09 | 2.74 | 1570 |
| 2024-09-20 22:21:42.627 | MS1 | 121.4656682104 | 31.1446195279 | 680 | 152650 | -91.49 | 4.41 | 73.54 | 0.11 | 2.46 | 1594 |

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
| 3210270 | 13 | 121.4727541636 | 31.1542835271 | 13 | 5 | 2 | 28.8 | FDD | 255 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3212245 | 8 | 121.4740843577 | 31.1472944318 | 251 | 10 | 12 | 25.3 | FDD | 620 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3213079 | 6 | 121.4703536209 | 31.1520985138 | 252 | 6 | 8 | 25.4 | TDD | 671 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3216561 | 7 | 121.4645480779 | 31.1559158860 | 185 | 12 | 11 | 7.7 | FDD | 680 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3222637 | 12 | 121.4668098739 | 31.1508312670 | 77 | 13 | 12 | 20.8 | FDD | 346 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3223914 | 1 | 121.4735316592 | 31.1527241690 | 218 | 4 | 0 | 5.7 | TDD | 289 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3229353 | 2 | 121.4644863796 | 31.1544972120 | 142 | 5 | 4 | 15.6 | TDD | 834 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3238396 | 3 | 121.4757176477 | 31.1516728043 | 205 | 12 | 11 | 8.4 | TDD | 730 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3248970 | 5 | 121.4756329766 | 31.1517839984 | 139 | 0 | 11 | 18.8 | TDD | 798 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3263346 | 9 | 121.4695875371 | 31.1458590392 | 223 | 3 | 8 | 13.1 | FDD | 430 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3274176 | 10 | 121.4662552072 | 31.1452732273 | 157 | 4 | 11 | 21.7 | FDD | 372 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3274292 | 4 | 121.4670351364 | 31.1550458991 | 17 | 15 | 5 | 23.2 | TDD | 540 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3276344 | 11 | 121.4708959390 | 31.1543599029 | 155 | 6 | 4 | 9.4 | FDD | 889 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |

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
| 2024-09-20 22:21:31.472 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.487 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.611 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.611 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.369 | NREventA2 | measId:1;ServCellPCI:174;Se... |
| 2024-09-20 22:21:35.508 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.746 | NREventA5 | measId:3;ServCellPCI:174;Se... |
| 2024-09-20 22:21:35.798 | NRHandoverAttempt | SourcePCI:174;SourceNR-ARFC... |
| 2024-09-20 22:21:35.828 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.842 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.990 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.990 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223914 | 1 | 9.6347 | 12.1566 | -115.9349 | 5.8233 | 144.9548 | 0.0040 | 0.0011 |
| 2024_09_20 22:00 | 3229353 | 2 | 18.8142 | 7.0893 | -114.1500 | 5.8655 | 173.5602 | 0.0024 | 0.0078 |
| 2024_09_20 22:00 | 3238396 | 3 | 17.4351 | 19.5207 | -116.4438 | 12.9182 | 128.7424 | 0.0015 | 0.0094 |
| 2024_09_20 22:00 | 3274292 | 4 | 10.0600 | 6.7571 | -114.4292 | 9.6856 | 135.4344 | 0.0148 | 0.0072 |
| 2024_09_20 22:00 | 3248970 | 5 | 7.5934 | 18.1702 | -114.1236 | 8.2510 | 124.9709 | 0.0068 | 0.0154 |
| 2024_09_20 22:00 | 3213079 | 6 | 8.2787 | 12.2571 | -117.3528 | 7.0935 | 113.8942 | 0.0034 | 0.0190 |
| 2024_09_20 22:00 | 3216561 | 7 | 13.7177 | 9.5149 | -115.4252 | 4.7818 | 47.7459 | 0.0044 | 0.0143 |
| 2024_09_20 22:00 | 3212245 | 8 | 9.4128 | 11.2848 | -115.1461 | 4.0155 | 35.5522 | 0.0151 | 0.0051 |
| 2024_09_20 22:00 | 3263346 | 9 | 19.4009 | 18.3331 | -117.0665 | 3.9636 | 55.4021 | 0.0165 | 0.0114 |
| 2024_09_20 22:00 | 3274176 | 10 | 13.7094 | 18.7750 | -117.4690 | 3.8570 | 23.4457 | 0.0190 | 0.0110 |
| 2024_09_20 22:00 | 3276344 | 11 | 19.9723 | 9.2400 | -115.6272 | 4.8741 | 43.8150 | 0.0107 | 0.0049 |
| 2024_09_20 22:00 | 3222637 | 12 | 13.5933 | 16.4646 | -114.5391 | 4.0221 | 28.9046 | 0.0039 | 0.0018 |
| 2024_09_20 22:00 | 3210270 | 13 | 18.1356 | 14.1290 | -114.9607 | 3.8650 | 45.6154 | 0.0167 | 0.0015 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414247_C68ECC33 | 152650 | 680 | -89.7 | 152650 | 255 | -99.1 | 152650 | 346 | -100.6 | 152650 | 620 |
| MR_1774414247_CAFB8C1F | 504990 | 798 | -93.5 | 504990 | 834 | -94.1 | 504990 | 671 | -94.2 | 504990 | 730 |
| MR_1774414247_FCB0F07D | 504990 | 798 | -91.6 | 504990 | 834 | -95.5 | 504990 | 671 | -96.0 | 504990 | 730 |
| MR_1774414247_FF3C08DF | 504990 | 798 | -94.2 | 504990 | 834 | -94.4 | 504990 | 671 | -97.2 | 504990 | 730 |
| MR_1774414247_ADB512EA | 152650 | 680 | -92.5 | 152650 | 255 | -98.9 | 152650 | 346 | -99.9 | 152650 | 620 |
| MR_1774414247_B84B9DC3 | 504990 | 798 | -92.5 | 504990 | 834 | -93.0 | 504990 | 671 | -94.9 | 504990 | 730 |
| MR_1774414247_12761688 | 504990 | 798 | -93.6 | 504990 | 834 | -93.4 | 504990 | 671 | -96.8 | 504990 | 730 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1331: `e18d9d0d-003...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e18d9d0d-0037-4be5-9c38-a6aeccb8d677` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1331] topology](images/train_1331.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3256631_4
- `C2`: Decrease A3 Offset threshold for 3274481_2
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256631_4
- `C5`: Lift the tilt angle of 3256631_4 by 5 degrees
- `C6`: Decrease transmission power for 3274481_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274481_2
- `C8`: Add neighbor relationship between 3277034_1 and 3274481_2
- `C9`: Press down the tilt angle of 3256631_4 by 5 degrees
- `C10`: Adjust the azimuth of 3256631_4 by 50 degrees
- `C11`: Increase transmission power for 3274481_2
- `C12`: Check test server and transmission issues **← 정답**
- `C13`: Increase transmission power for 3256631_4
- `C14`: Increase A3 Offset threshold for 3256631_4
- `C15`: Add neighbor relationship between 3256631_4 and 3274481_2
- `C16`: Decrease transmission power for 3256631_4
- `C17`: Adjust the azimuth of 3274481_2 by 50 degrees
- `C18`: Lift the tilt angle  of 3274481_2 by 10 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274481_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256631_4
- `C21`: Press down the tilt angle  of 3274481_2 by 10 degrees
- `C22`: Increase A3 Offset threshold for 3274481_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.418 | MS1 | 121.4656763641 | 31.1446187404 | 487 | 504990 | -85.29 | 12.09 | 554.45 | 0.05 | 2.84 | 1574 |
| 2024-09-20 22:21:32.608 | MS1 | 121.4656715135 | 31.1446244959 | 487 | 504990 | -85.98 | 17.19 | 452.40 | 0.13 | 2.91 | 1591 |
| 2024-09-20 22:21:33.922 | MS1 | 121.4656756390 | 31.1446251426 | 487 | 504990 | -85.86 | 14.07 | 311.37 | 0.15 | 2.23 | 1577 |
| 2024-09-20 22:21:34.596 | MS1 | 121.4656624208 | 31.1446274259 | 487 | 504990 | -91.65 | 13.47 | 46.81 | 0.12 | 2.51 | 330 |
| 2024-09-20 22:21:35.584 | MS1 | 121.4656581803 | 31.1446293476 | 487 | 504990 | -90.81 | 17.16 | 101.21 | 0.09 | 2.83 | 349 |
| 2024-09-20 22:21:36.236 | MS1 | 121.4656727451 | 31.1446269125 | 487 | 504990 | -91.57 | 15.73 | 53.77 | 0.11 | 2.63 | 329 |
| 2024-09-20 22:21:37.242 | MS1 | 121.4656668327 | 31.1446214029 | 487 | 504990 | -92.17 | 8.16 | 92.64 | 0.00 | 2.86 | 318 |
| 2024-09-20 22:21:38.892 | MS1 | 121.4656654699 | 31.1446335560 | 487 | 504990 | -91.77 | 10.46 | 64.85 | 0.07 | 2.86 | 361 |
| 2024-09-20 22:21:39.939 | MS1 | 121.4656617409 | 31.1446197563 | 487 | 504990 | -93.98 | 10.03 | 59.46 | 0.01 | 2.03 | 345 |
| 2024-09-20 22:21:40.939 | MS1 | 121.4656638132 | 31.1446363620 | 487 | 504990 | -93.69 | 9.91 | 488.93 | 0.07 | 2.95 | 1596 |
| 2024-09-20 22:21:41.310 | MS1 | 121.4656756398 | 31.1446303226 | 487 | 504990 | -92.99 | 10.48 | 498.06 | 0.03 | 2.84 | 1566 |
| 2024-09-20 22:21:42.557 | MS1 | 121.4656684346 | 31.1446284256 | 487 | 504990 | -90.63 | 12.15 | 397.47 | 0.20 | 2.24 | 1571 |

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
| 3236311 | 3 | 121.4651055760 | 31.1525196974 | 323 | 15 | 0 | 21.5 | TDD | 614 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3256631 | 4 | 121.4727444404 | 31.1488202857 | 16 | 2 | 10 | 50.0 | TDD | 487 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3274481 | 2 | 121.4684803275 | 31.1516703231 | 4 | 13 | 11 | 49.0 | TDD | 764 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3277034 | 1 | 121.4727957556 | 31.1478185049 | 180 | 5 | 12 | 45.3 | TDD | 122 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.811 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.826 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.960 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.960 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.676 | NREventA3 | measId:2;ServCellPCI:610;Se... |
| 2024-09-20 22:21:37.916 | NRHandoverAttempt | SourcePCI:610;SourceNR-ARFC... |
| 2024-09-20 22:21:37.952 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.967 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.116 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.116 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277034 | 1 | 17.3032 | 10.2103 | -117.7230 | 16.7136 | 156.0752 | 0.0164 | 0.0074 |
| 2024_09_20 22:00 | 3274481 | 2 | 6.6147 | 15.3790 | -117.6390 | 9.6619 | 92.1272 | 0.0176 | 0.0026 |
| 2024_09_20 22:00 | 3236311 | 3 | 7.4582 | 7.5624 | -116.4081 | 9.0800 | 199.0840 | 0.0075 | 0.0179 |
| 2024_09_20 22:00 | 3256631 | 4 | 13.2778 | 18.8408 | -115.2989 | 14.7060 | 193.7657 | 0.0001 | 0.0161 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412779_17B658A0 | 504990 | 487 | -93.5 | 504990 | 764 | -91.9 | 504990 | 122 | -104.0 | 504990 | 614 |
| MR_1774412779_5FA7708B | 504990 | 487 | -92.9 | 504990 | 764 | -91.4 | 504990 | 122 | -105.7 | 504990 | 614 |
| MR_1774412779_CE4B7DDB | 504990 | 487 | -92.9 | 504990 | 764 | -93.5 | 504990 | 122 | -105.8 | 504990 | 614 |
| MR_1774412779_745F0D7A | 504990 | 487 | -91.7 | 504990 | 764 | -93.6 | 504990 | 122 | -103.8 | 504990 | 614 |
| MR_1774412779_2B52D818 | 504990 | 487 | -91.0 | 504990 | 764 | -93.3 | 504990 | 122 | -106.8 | 504990 | 614 |
| MR_1774412779_455F2973 | 504990 | 487 | -93.0 | 504990 | 764 | -92.1 | 504990 | 122 | -105.6 | 504990 | 614 |
| MR_1774412779_06B3D152 | 504990 | 487 | -91.9 | 504990 | 764 | -93.4 | 504990 | 122 | -106.9 | 504990 | 614 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1332: `2929ca46-d1b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2929ca46-d1b3-4d85-af76-a2f9809cb0cd` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease A3 Offset threshold for 3276241_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1332] topology](images/train_1332.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3276241_2 by 6 degrees
- `C2`: Check test server and transmission issues
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease A3 Offset threshold for 3275687_3
- `C5`: Increase A3 Offset threshold for 3276241_2
- `C6`: Increase transmission power for 3275687_3
- `C7`: Increase transmission power for 3276241_2
- `C8`: Decrease transmission power for 3276241_2
- `C9`: Lift the tilt angle of 3276241_2 by 6 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275687_3
- `C11`: Increase A3 Offset threshold for 3275687_3
- `C12`: Adjust the azimuth of 3276241_2 by 50 degrees
- `C13`: Add neighbor relationship between 3276241_2 and 3275687_3
- `C14`: Add neighbor relationship between 3268260_1 and 3275687_3
- `C15`: Adjust the azimuth of 3275687_3 by 50 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275687_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276241_2
- `C18`: Decrease transmission power for 3275687_3
- `C19`: Press down the tilt angle  of 3275687_3 by 10 degrees
- `C20`: Decrease A3 Offset threshold for 3276241_2 **← 정답**
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276241_2
- `C22`: Lift the tilt angle  of 3275687_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.170 | MS1 | 121.4656740726 | 31.1446280083 | 755 | 504990 | -79.43 | 16.27 | 584.10 | 0.14 | 2.49 | 1563 |
| 2024-09-20 22:21:32.298 | MS1 | 121.4656592869 | 31.1446266802 | 755 | 504990 | -79.42 | 15.44 | 469.64 | 0.08 | 2.28 | 1584 |
| 2024-09-20 22:21:33.753 | MS1 | 121.4656587613 | 31.1446181803 | 755 | 504990 | -78.40 | 13.52 | 519.66 | 0.05 | 2.47 | 1570 |
| 2024-09-20 22:21:34.921 | MS1 | 121.4656750924 | 31.1446356287 | 755 | 504990 | -85.51 | -2.22 | 40.49 | 0.00 | 1.22 | 1581 |
| 2024-09-20 22:21:35.798 | MS1 | 121.4656695609 | 31.1446316533 | 755 | 504990 | -88.75 | -0.48 | 71.57 | 0.04 | 1.35 | 1571 |
| 2024-09-20 22:21:36.368 | MS1 | 121.4656623511 | 31.1446277339 | 755 | 504990 | -86.59 | -3.08 | 57.82 | 0.01 | 1.03 | 1597 |
| 2024-09-20 22:21:37.734 | MS1 | 121.4656610602 | 31.1446196736 | 755 | 504990 | -87.10 | -3.17 | 64.58 | 0.15 | 1.29 | 1570 |
| 2024-09-20 22:21:38.830 | MS1 | 121.4656629576 | 31.1446288550 | 755 | 504990 | -89.22 | -1.55 | 55.60 | 0.14 | 1.42 | 1564 |
| 2024-09-20 22:21:39.464 | MS1 | 121.4656589245 | 31.1446312882 | 916 | 504990 | -82.44 | 17.42 | 255.81 | 0.18 | 1.42 | 1579 |
| 2024-09-20 22:21:40.602 | MS1 | 121.4656686605 | 31.1446375851 | 916 | 504990 | -76.12 | 15.53 | 416.76 | 0.04 | 2.39 | 1565 |
| 2024-09-20 22:21:41.418 | MS1 | 121.4656594982 | 31.1446242529 | 916 | 504990 | -80.56 | 17.47 | 346.25 | 0.06 | 2.52 | 1565 |
| 2024-09-20 22:21:42.617 | MS1 | 121.4656761598 | 31.1446209693 | 916 | 504990 | -80.94 | 17.75 | 351.33 | 0.15 | 2.92 | 1564 |

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
| 3268260 | 1 | 121.4653480059 | 31.1449170444 | 57 | 9 | 2 | 49.0 | TDD | 402 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3269646 | 4 | 121.4665367048 | 31.1478006433 | 1 | 15 | 12 | 38.7 | TDD | 197 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3275687 | 3 | 121.4751840746 | 31.1506221376 | 5 | 8 | 0 | 37.1 | TDD | 916 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3276241 | 2 | 121.4720552920 | 31.1495116673 | 46 | 3 | 10 | 43.6 | TDD | 755 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.639 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.743 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.743 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.488 | NREventA3 | measId:2;ServCellPCI:217;Se... |
| 2024-09-20 22:21:38.728 | NRHandoverAttempt | SourcePCI:217;SourceNR-ARFC... |
| 2024-09-20 22:21:38.776 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.791 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.891 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.891 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268260 | 1 | 9.7479 | 16.2693 | -115.7273 | 19.8786 | 98.7169 | 0.0068 | 0.0020 |
| 2024_09_20 22:00 | 3276241 | 2 | 10.8620 | 17.3468 | -115.0430 | 7.9473 | 142.0947 | 0.0057 | 0.1003 |
| 2024_09_20 22:00 | 3275687 | 3 | 17.8317 | 8.5690 | -114.8182 | 15.3190 | 157.0945 | 0.0061 | 0.0130 |
| 2024_09_20 22:00 | 3269646 | 4 | 14.0306 | 9.2253 | -116.6441 | 9.7899 | 101.4991 | 0.0188 | 0.0042 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413910_A1B30836 | 504990 | 755 | -86.4 | 504990 | 916 | -76.6 | 504990 | 402 | -81.9 | 504990 | 197 |
| MR_1774413910_98250599 | 504990 | 755 | -84.3 | 504990 | 916 | -78.3 | 504990 | 402 | -81.7 | 504990 | 197 |
| MR_1774413910_A51E27C1 | 504990 | 755 | -86.1 | 504990 | 916 | -77.6 | 504990 | 402 | -79.8 | 504990 | 197 |
| MR_1774413910_F535931B | 504990 | 755 | -86.3 | 504990 | 916 | -80.1 | 504990 | 402 | -80.0 | 504990 | 197 |
| MR_1774413910_E0C62C01 | 504990 | 916 | -79.2 | 504990 | 755 | -83.7 | 504990 | 402 | -80.4 | 504990 | 197 |
| MR_1774413910_697250E5 | 504990 | 916 | -78.9 | 504990 | 755 | -83.8 | 504990 | 402 | -78.2 | 504990 | 197 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1333: `12b4a596-bd9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `12b4a596-bd98-4e6f-a9b1-338d5e150299` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1333] topology](images/train_1333.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226197_4
- `C2`: Check test server and transmission issues
- `C3`: Decrease transmission power for 3222900_1
- `C4`: Increase transmission power for 3222900_1
- `C5`: Increase A3 Offset threshold for 3222900_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226197_4
- `C7`: Press down the tilt angle of 3226197_4 by 8 degrees
- `C8`: Add neighbor relationship between 3226737_2 and 3222900_1
- `C9`: Lift the tilt angle of 3226197_4 by 8 degrees
- `C10`: Increase transmission power for 3226197_4
- `C11`: Decrease transmission power for 3226197_4
- `C12`: Add neighbor relationship between 3226197_4 and 3222900_1
- `C13`: Increase A3 Offset threshold for 3226197_4
- `C14`: Press down the tilt angle  of 3222900_1 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3222900_1
- `C16`: Decrease A3 Offset threshold for 3226197_4
- `C17`: Insufficient data; more data is needed for judgment. **← 정답**
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222900_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222900_1
- `C20`: Adjust the azimuth of 3226197_4 by 30 degrees
- `C21`: Lift the tilt angle  of 3222900_1 by 10 degrees
- `C22`: Adjust the azimuth of 3222900_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.491 | MS1 | 121.4656602953 | 31.1446236283 | 910 | 504990 | -90.64 | 17.51 | 477.37 | 0.16 | 2.24 | 1564 |
| 2024-09-20 22:21:32.826 | MS1 | 121.4656617659 | 31.1446180903 | 910 | 504990 | -86.79 | 12.70 | 471.70 | 0.15 | 2.84 | 1569 |
| 2024-09-20 22:21:33.550 | MS1 | 121.4656585930 | 31.1446337648 | 910 | 504990 | -90.77 | 12.19 | 475.73 | 0.06 | 2.66 | 1575 |
| 2024-09-20 22:21:34.485 | MS1 | 121.4656655712 | 31.1446329820 | 910 | 504990 | -85.56 | 17.90 | 67.20 | 0.15 | 2.20 | 1593 |
| 2024-09-20 22:21:35.255 | MS1 | 121.4656757141 | 31.1446283959 | 910 | 504990 | -85.75 | 14.97 | 90.22 | 0.19 | 2.02 | 1592 |
| 2024-09-20 22:21:36.448 | MS1 | 121.4656713115 | 31.1446367621 | 910 | 504990 | -88.52 | 17.63 | 87.49 | 0.02 | 2.91 | 1582 |
| 2024-09-20 22:21:37.638 | MS1 | 121.4656586987 | 31.1446358432 | 910 | 504990 | -91.89 | 11.52 | 69.07 | 0.03 | 2.19 | 1575 |
| 2024-09-20 22:21:38.544 | MS1 | 121.4656667889 | 31.1446311468 | 910 | 504990 | -91.32 | 9.69 | 60.81 | 0.16 | 2.26 | 1585 |
| 2024-09-20 22:21:39.450 | MS1 | 121.4656635654 | 31.1446298618 | 910 | 504990 | -93.42 | 11.43 | 95.57 | 0.05 | 2.31 | 1597 |
| 2024-09-20 22:21:40.361 | MS1 | 121.4656743611 | 31.1446377143 | 910 | 504990 | -90.18 | 11.96 | 331.83 | 0.19 | 2.36 | 1565 |
| 2024-09-20 22:21:41.268 | MS1 | 121.4656638010 | 31.1446253166 | 910 | 504990 | -90.54 | 9.23 | 582.00 | 0.20 | 2.21 | 1573 |
| 2024-09-20 22:21:42.765 | MS1 | 121.4656735323 | 31.1446309346 | 910 | 504990 | -93.61 | 9.33 | 593.95 | 0.18 | 2.37 | 1589 |

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
| 3222900 | 1 | 121.4664895112 | 31.1495144952 | 274 | 14 | 9 | 35.9 | TDD | 312 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3226197 | 4 | 121.4758932712 | 31.1491913740 | 212 | 7 | 0 | 23.5 | TDD | 910 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3226737 | 2 | 121.4742743663 | 31.1535137054 | 61 | 10 | 8 | 40.5 | TDD | 419 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3252338 | 3 | 121.4679350851 | 31.1464452950 | 39 | 15 | 10 | 47.9 | TDD | 493 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.277 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.296 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.437 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.437 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.177 | NREventA3 | measId:2;ServCellPCI:375;Se... |
| 2024-09-20 22:21:38.417 | NRHandoverAttempt | SourcePCI:375;SourceNR-ARFC... |
| 2024-09-20 22:21:38.461 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.474 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.603 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.603 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3222900 | 1 | 90.0034 | 94.2939 | -116.3739 | 12.8267 | 82.6162 | 0.0143 | 0.0046 |
| 2024_09_19 22:00 | 3226737 | 2 | 87.5495 | 82.6351 | -115.9064 | 5.8655 | 96.5312 | 0.0121 | 0.0065 |
| 2024_09_19 22:00 | 3252338 | 3 | 82.1585 | 93.6276 | -114.0033 | 18.6804 | 183.6714 | 0.0056 | 0.0131 |
| 2024_09_19 22:00 | 3226197 | 4 | 94.4784 | 91.1486 | -115.0859 | 14.9931 | 123.6461 | 0.0119 | 0.0150 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415444_B5EC8C57 | 504990 | 910 | -86.4 | 504990 | 312 | -88.4 | 504990 | 419 | -90.3 | 504990 | 493 |
| MR_1774415444_080BABC9 | 504990 | 910 | -85.4 | 504990 | 312 | -91.6 | 504990 | 419 | -93.3 | 504990 | 493 |
| MR_1774415444_53808FC3 | 504990 | 910 | -86.8 | 504990 | 312 | -90.6 | 504990 | 419 | -91.1 | 504990 | 493 |
| MR_1774415444_DF50D504 | 504990 | 910 | -85.0 | 504990 | 312 | -90.8 | 504990 | 419 | -93.3 | 504990 | 493 |
| MR_1774415444_2D8A9587 | 504990 | 910 | -85.1 | 504990 | 312 | -88.0 | 504990 | 419 | -91.8 | 504990 | 493 |
| MR_1774415444_75BA755D | 504990 | 910 | -87.2 | 504990 | 312 | -90.4 | 504990 | 419 | -93.2 | 504990 | 493 |
| MR_1774415444_0BF26CC4 | 504990 | 910 | -83.6 | 504990 | 312 | -91.5 | 504990 | 419 | -92.5 | 504990 | 493 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1334: `2cb06c21-e33...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2cb06c21-e33f-410a-8f1f-813604af8f79` |
| Tag | **multiple-answer** |
| 정답 | **C5|C6|C14|C19** |
| C5 의미 | Increase A3 Offset threshold for 3219204_4 |
| C6 의미 | Increase A3 Offset threshold for 3239484_3 |
| C14 의미 | Decrease transmission power for 3219204_4 |
| C19 의미 | Press down the tilt angle  of 3219204_4 by 6 degrees |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1334] topology](images/train_1334.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3239484_3 by 5 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Adjust the azimuth of 3239484_3 by 41 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239484_3
- `C5`: Increase A3 Offset threshold for 3219204_4 **← 정답**
- `C6`: Increase A3 Offset threshold for 3239484_3 **← 정답**
- `C7`: Increase transmission power for 3219204_4
- `C8`: Add neighbor relationship between 3239484_3 and 3219204_4
- `C9`: Check test server and transmission issues
- `C10`: Decrease A3 Offset threshold for 3239484_3
- `C11`: Increase transmission power for 3239484_3
- `C12`: Lift the tilt angle  of 3219204_4 by 6 degrees
- `C13`: Adjust the azimuth of 3219204_4 by 35 degrees
- `C14`: Decrease transmission power for 3219204_4 **← 정답**
- `C15`: Decrease transmission power for 3239484_3
- `C16`: Decrease A3 Offset threshold for 3219204_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239484_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219204_4
- `C19`: Press down the tilt angle  of 3219204_4 by 6 degrees **← 정답**
- `C20`: Add neighbor relationship between 3225882_2 and 3219204_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219204_4
- `C22`: Lift the tilt angle of 3239484_3 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.663 | MS1 | 121.4656759487 | 31.1446328295 | 937 | 504990 | -83.63 | 12.78 | 427.36 | 0.02 | 2.31 | 1583 |
| 2024-09-20 22:21:32.265 | MS1 | 121.4656732713 | 31.1446251116 | 937 | 504990 | -77.82 | 16.25 | 562.07 | 0.16 | 2.51 | 1596 |
| 2024-09-20 22:21:33.499 | MS1 | 121.4656652679 | 31.1446330993 | 937 | 504990 | -81.80 | 12.34 | 417.57 | 0.03 | 2.85 | 1573 |
| 2024-09-20 22:21:34.523 | MS1 | 121.4656634604 | 31.1446224461 | 845 | 504990 | -80.21 | 1.19 | 68.49 | 0.17 | 1.31 | 1577 |
| 2024-09-20 22:21:35.542 | MS1 | 121.4656633718 | 31.1446329293 | 845 | 504990 | -86.15 | 1.73 | 62.40 | 0.02 | 1.31 | 1575 |
| 2024-09-20 22:21:36.312 | MS1 | 121.4656588782 | 31.1446233813 | 937 | 504990 | -84.31 | 1.60 | 29.16 | 0.10 | 1.29 | 1591 |
| 2024-09-20 22:21:37.373 | MS1 | 121.4656672200 | 31.1446216522 | 937 | 504990 | -89.66 | 2.47 | 51.48 | 0.13 | 1.46 | 1585 |
| 2024-09-20 22:21:38.218 | MS1 | 121.4656767434 | 31.1446282219 | 845 | 504990 | -89.64 | 2.27 | 41.63 | 0.05 | 1.43 | 1580 |
| 2024-09-20 22:21:39.393 | MS1 | 121.4656720447 | 31.1446181395 | 845 | 504990 | -86.56 | 4.50 | 64.07 | 0.01 | 1.48 | 1575 |
| 2024-09-20 22:21:40.939 | MS1 | 121.4656688594 | 31.1446252387 | 845 | 504990 | -82.57 | 17.26 | 545.37 | 0.19 | 2.50 | 1586 |
| 2024-09-20 22:21:41.946 | MS1 | 121.4656753101 | 31.1446332436 | 845 | 504990 | -79.70 | 17.60 | 316.62 | 0.04 | 2.91 | 1577 |
| 2024-09-20 22:21:42.414 | MS1 | 121.4656585680 | 31.1446375359 | 845 | 504990 | -77.09 | 17.16 | 423.52 | 0.04 | 2.85 | 1598 |

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
| 3214740 | 1 | 121.4714760926 | 31.1463237821 | 92 | 13 | 0 | 18.6 | TDD | 513 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3219204 | 4 | 121.4654146744 | 31.1546216222 | 214 | 4 | 0 | 35.1 | TDD | 457 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3225882 | 2 | 121.4757518521 | 31.1493945637 | 125 | 2 | 2 | 33.2 | TDD | 647 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3237661 | 5 | 121.4730852205 | 31.1556721324 | 90 | 1 | 3 | 29.2 | TDD | 845 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3239484 | 3 | 121.4699893851 | 31.1553907989 | 240 | 4 | 2 | 18.1 | TDD | 937 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.689 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.706 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.826 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.826 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.492 | NREventA3 | measId:2;ServCellPCI:96;Ser... |
| 2024-09-20 22:21:34.732 | NRHandoverAttempt | SourcePCI:96;SourceNR-ARFCN... |
| 2024-09-20 22:21:34.779 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.792 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:34.897 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.897 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.492 | NREventA3 | measId:2;ServCellPCI:180;Se... |
| 2024-09-20 22:21:36.732 | NRHandoverAttempt | SourcePCI:180;SourceNR-ARFC... |
| 2024-09-20 22:21:36.781 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.794 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.942 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.942 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.492 | NREventA3 | measId:2;ServCellPCI:96;Ser... |
| 2024-09-20 22:21:38.732 | NRHandoverAttempt | SourcePCI:96;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.776 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.788 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.888 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.888 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214740 | 1 | 8.6326 | 6.7022 | -117.1458 | 19.2836 | 186.5790 | 0.0118 | 0.0195 |
| 2024_09_20 22:00 | 3225882 | 2 | 17.7487 | 18.7709 | -116.1243 | 16.3965 | 145.1641 | 0.0069 | 0.0174 |
| 2024_09_20 22:00 | 3239484 | 3 | 12.8819 | 7.7011 | -114.6685 | 19.7376 | 133.7321 | 0.0180 | 0.0059 |
| 2024_09_20 22:00 | 3219204 | 4 | 18.9559 | 10.6671 | -117.7931 | 6.0878 | 179.4341 | 0.0014 | 0.0189 |
| 2024_09_20 22:00 | 3237661 | 5 | 8.6997 | 13.7149 | -114.1023 | 12.5751 | 126.6055 | 0.0183 | 0.0081 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411982_DAEC593E | 504990 | 937 | -79.7 | 504990 | 845 | -79.4 | 504990 | 457 | -80.9 | 504990 | 647 |
| MR_1774411982_7457ABEE | 504990 | 845 | -79.8 | 504990 | 937 | -81.8 | 504990 | 457 | -83.1 | 504990 | 647 |
| MR_1774411982_782C4C84 | 504990 | 845 | -81.7 | 504990 | 937 | -79.8 | 504990 | 457 | -80.4 | 504990 | 647 |
| MR_1774411982_4B0AE549 | 504990 | 845 | -81.7 | 504990 | 937 | -80.2 | 504990 | 457 | -79.4 | 504990 | 647 |
| MR_1774411982_E17A3BFE | 504990 | 937 | -81.1 | 504990 | 845 | -81.2 | 504990 | 457 | -80.8 | 504990 | 647 |
| MR_1774411982_02C8942D | 504990 | 845 | -79.6 | 504990 | 937 | -80.4 | 504990 | 457 | -80.6 | 504990 | 647 |
| MR_1774411982_A40E7763 | 504990 | 845 | -80.6 | 504990 | 937 | -81.3 | 504990 | 457 | -80.0 | 504990 | 647 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1335: `945156cb-29c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `945156cb-29ce-4234-bdbd-50259bfe810c` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Add neighbor relationship between 3236406_3 and 3274657_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1335] topology](images/train_1335.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274657_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274657_2
- `C3`: Add neighbor relationship between 3224465_1 and 3274657_2
- `C4`: Lift the tilt angle  of 3274657_2 by 5 degrees
- `C5`: Press down the tilt angle  of 3274657_2 by 5 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236406_3
- `C7`: Lift the tilt angle of 3236406_3 by 4 degrees
- `C8`: Decrease A3 Offset threshold for 3274657_2
- `C9`: Decrease transmission power for 3236406_3
- `C10`: Adjust the azimuth of 3236406_3 by 50 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236406_3
- `C12`: Press down the tilt angle of 3236406_3 by 4 degrees
- `C13`: Add neighbor relationship between 3236406_3 and 3274657_2 **← 정답**
- `C14`: Adjust the azimuth of 3274657_2 by 42 degrees
- `C15`: Increase A3 Offset threshold for 3236406_3
- `C16`: Increase transmission power for 3236406_3
- `C17`: Increase transmission power for 3274657_2
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease transmission power for 3274657_2
- `C20`: Check test server and transmission issues
- `C21`: Increase A3 Offset threshold for 3274657_2
- `C22`: Decrease A3 Offset threshold for 3236406_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.643 | MS1 | 121.4656769003 | 31.1446226190 | 679 | 504990 | -83.45 | 17.26 | 461.35 | 0.03 | 2.51 | 1568 |
| 2024-09-20 22:21:32.635 | MS1 | 121.4656673610 | 31.1446288028 | 679 | 504990 | -83.59 | 12.94 | 357.51 | 0.17 | 2.27 | 1586 |
| 2024-09-20 22:21:33.729 | MS1 | 121.4656667194 | 31.1446328752 | 679 | 504990 | -77.00 | 17.19 | 367.11 | 0.17 | 2.47 | 1596 |
| 2024-09-20 22:21:34.181 | MS1 | 121.4656625929 | 31.1446368054 | 679 | 504990 | -89.09 | -3.46 | 41.35 | 0.07 | 1.26 | 1573 |
| 2024-09-20 22:21:35.396 | MS1 | 121.4656726941 | 31.1446311900 | 679 | 504990 | -94.58 | -1.14 | 56.36 | 0.03 | 1.23 | 1600 |
| 2024-09-20 22:21:36.685 | MS1 | 121.4656699083 | 31.1446287083 | 679 | 504990 | -94.26 | -2.84 | 38.24 | 0.08 | 1.39 | 1599 |
| 2024-09-20 22:21:37.102 | MS1 | 121.4656661252 | 31.1446285327 | 679 | 504990 | -94.13 | -3.72 | 71.47 | 0.06 | 1.12 | 1598 |
| 2024-09-20 22:21:38.771 | MS1 | 121.4656729907 | 31.1446277413 | 679 | 504990 | -79.92 | 14.44 | 416.69 | 0.04 | 1.43 | 1563 |
| 2024-09-20 22:21:39.996 | MS1 | 121.4656757188 | 31.1446228430 | 679 | 504990 | -79.90 | 12.31 | 429.38 | 0.18 | 1.12 | 1566 |
| 2024-09-20 22:21:40.630 | MS1 | 121.4656621174 | 31.1446185870 | 679 | 504990 | -83.55 | 12.85 | 545.82 | 0.12 | 2.79 | 1561 |
| 2024-09-20 22:21:41.211 | MS1 | 121.4656675324 | 31.1446208568 | 679 | 504990 | -83.13 | 15.83 | 582.93 | 0.02 | 2.39 | 1571 |
| 2024-09-20 22:21:42.544 | MS1 | 121.4656716857 | 31.1446271757 | 679 | 504990 | -82.54 | 16.77 | 521.82 | 0.03 | 2.28 | 1573 |

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
| 3224465 | 1 | 121.4754755858 | 31.1517594824 | 85 | 13 | 6 | 27.3 | TDD | 273 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3236406 | 3 | 121.4663167943 | 31.1530103549 | 26 | 3 | 9 | 16.3 | TDD | 679 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3257847 | 4 | 121.4756459282 | 31.1497354039 | 46 | 8 | 1 | 27.2 | TDD | 255 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3274657 | 2 | 121.4677561142 | 31.1538066540 | 233 | 3 | 10 | 43.7 | TDD | 931 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.391 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.412 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.529 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.529 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.210 | NREventA3 | measId:2;ServCellPCI:672;Se... |
| 2024-09-20 22:21:36.210 | NREventA3 | measId:2;ServCellPCI:672;Se... |
| 2024-09-20 22:21:37.210 | NREventA3 | measId:2;ServCellPCI:672;Se... |
| 2024-09-20 22:21:39.710 | NRRRCReestablishAttempt | PCI:672 |
| 2024-09-20 22:21:39.729 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.741 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.885 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.885 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224465 | 1 | 6.2972 | 7.5149 | -116.1067 | 11.6942 | 98.5668 | 0.0065 | 0.0149 |
| 2024_09_20 22:00 | 3274657 | 2 | 7.0485 | 8.6338 | -117.8355 | 19.6044 | 128.9785 | 0.0140 | 0.0045 |
| 2024_09_20 22:00 | 3236406 | 3 | 12.1051 | 5.3902 | -117.4772 | 18.8047 | 145.7092 | 0.0078 | 0.1763 |
| 2024_09_20 22:00 | 3257847 | 4 | 10.0853 | 16.4549 | -116.7578 | 15.6136 | 102.6110 | 0.0056 | 0.0156 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412779_5B1E8A53 | 504990 | 931 | -83.7 | 504990 | 679 | -89.5 | 504990 | 273 | -93.6 | 504990 | 255 |
| MR_1774412779_97DD04CB | 504990 | 679 | -90.4 | 504990 | 931 | -85.9 | 504990 | 273 | -92.9 | 504990 | 255 |
| MR_1774412779_4230D91D | 504990 | 931 | -84.4 | 504990 | 679 | -89.6 | 504990 | 273 | -91.6 | 504990 | 255 |
| MR_1774412779_D8A27AD5 | 504990 | 931 | -86.3 | 504990 | 679 | -88.8 | 504990 | 273 | -91.0 | 504990 | 255 |
| MR_1774412779_47D3D9FA | 504990 | 931 | -86.0 | 504990 | 679 | -89.2 | 504990 | 273 | -93.5 | 504990 | 255 |
| MR_1774412779_13B8D8B8 | 504990 | 679 | -89.8 | 504990 | 931 | -84.0 | 504990 | 273 | -92.5 | 504990 | 255 |
| MR_1774412779_843D209B | 504990 | 679 | -88.8 | 504990 | 931 | -85.1 | 504990 | 273 | -91.6 | 504990 | 255 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1336: `d06fb648-d4c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d06fb648-d4c4-450f-bd05-9cadc2380149` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease A3 Offset threshold for 3279768_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1336] topology](images/train_1336.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3271712_3
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271712_3
- `C4`: Decrease transmission power for 3271712_3
- `C5`: Decrease transmission power for 3279768_1
- `C6`: Increase A3 Offset threshold for 3279768_1
- `C7`: Increase transmission power for 3271712_3
- `C8`: Increase A3 Offset threshold for 3271712_3
- `C9`: Adjust the azimuth of 3271712_3 by 50 degrees
- `C10`: Press down the tilt angle of 3279768_1 by 1 degrees
- `C11`: Lift the tilt angle of 3279768_1 by 1 degrees
- `C12`: Add neighbor relationship between 3267201_4 and 3271712_3
- `C13`: Check test server and transmission issues
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279768_1
- `C15`: Increase transmission power for 3279768_1
- `C16`: Add neighbor relationship between 3279768_1 and 3271712_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271712_3
- `C18`: Lift the tilt angle  of 3271712_3 by 10 degrees
- `C19`: Adjust the azimuth of 3279768_1 by 50 degrees
- `C20`: Press down the tilt angle  of 3271712_3 by 10 degrees
- `C21`: Decrease A3 Offset threshold for 3279768_1 **← 정답**
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279768_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.191 | MS1 | 121.4656690555 | 31.1446283576 | 90 | 504990 | -77.96 | 13.02 | 327.65 | 0.19 | 2.44 | 1600 |
| 2024-09-20 22:21:32.766 | MS1 | 121.4656650630 | 31.1446328808 | 90 | 504990 | -79.62 | 15.52 | 591.70 | 0.16 | 2.67 | 1561 |
| 2024-09-20 22:21:33.269 | MS1 | 121.4656759097 | 31.1446262996 | 90 | 504990 | -79.86 | 12.91 | 502.67 | 0.04 | 2.68 | 1580 |
| 2024-09-20 22:21:34.733 | MS1 | 121.4656665500 | 31.1446238333 | 90 | 504990 | -84.77 | -2.22 | 68.13 | 0.13 | 1.20 | 1600 |
| 2024-09-20 22:21:35.521 | MS1 | 121.4656755480 | 31.1446334164 | 90 | 504990 | -83.05 | -1.06 | 67.19 | 0.09 | 1.02 | 1578 |
| 2024-09-20 22:21:36.679 | MS1 | 121.4656739274 | 31.1446182640 | 90 | 504990 | -91.68 | -0.55 | 39.48 | 0.16 | 1.38 | 1578 |
| 2024-09-20 22:21:37.107 | MS1 | 121.4656592949 | 31.1446346185 | 90 | 504990 | -89.95 | -3.51 | 73.41 | 0.12 | 1.38 | 1574 |
| 2024-09-20 22:21:38.934 | MS1 | 121.4656626779 | 31.1446379366 | 90 | 504990 | -87.94 | -3.49 | 46.71 | 0.10 | 1.20 | 1562 |
| 2024-09-20 22:21:39.718 | MS1 | 121.4656580998 | 31.1446253857 | 286 | 504990 | -84.08 | 16.73 | 266.58 | 0.07 | 1.07 | 1592 |
| 2024-09-20 22:21:40.396 | MS1 | 121.4656624683 | 31.1446278321 | 286 | 504990 | -84.49 | 12.12 | 442.69 | 0.00 | 2.39 | 1596 |
| 2024-09-20 22:21:41.915 | MS1 | 121.4656696744 | 31.1446350960 | 286 | 504990 | -80.41 | 17.39 | 510.09 | 0.17 | 2.25 | 1578 |
| 2024-09-20 22:21:42.304 | MS1 | 121.4656683354 | 31.1446352690 | 286 | 504990 | -75.75 | 15.76 | 465.37 | 0.17 | 2.52 | 1594 |

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
| 3262699 | 2 | 121.4747300951 | 31.1507119699 | 254 | 0 | 7 | 42.2 | TDD | 316 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3267201 | 4 | 121.4711212705 | 31.1490434876 | 198 | 15 | 10 | 17.1 | TDD | 238 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3271712 | 3 | 121.4710166160 | 31.1506406494 | 91 | 7 | 0 | 40.4 | TDD | 286 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3279768 | 1 | 121.4678870318 | 31.1555023244 | 130 | 0 | 0 | 29.4 | TDD | 90 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.487 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.502 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.637 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.637 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.360 | NREventA3 | measId:2;ServCellPCI:406;Se... |
| 2024-09-20 22:21:38.600 | NRHandoverAttempt | SourcePCI:406;SourceNR-ARFC... |
| 2024-09-20 22:21:38.635 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.649 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.778 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.778 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279768 | 1 | 10.2662 | 14.0053 | -116.3766 | 9.0390 | 150.7036 | 0.0005 | 0.1969 |
| 2024_09_20 22:00 | 3262699 | 2 | 5.2507 | 8.0943 | -114.3218 | 19.5477 | 156.3203 | 0.0176 | 0.0027 |
| 2024_09_20 22:00 | 3271712 | 3 | 10.5861 | 12.7123 | -116.4687 | 9.8846 | 97.0336 | 0.0012 | 0.0191 |
| 2024_09_20 22:00 | 3267201 | 4 | 11.3432 | 19.2013 | -115.1834 | 15.0446 | 175.1807 | 0.0133 | 0.0153 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412787_085780E9 | 504990 | 286 | -80.9 | 504990 | 90 | -86.5 | 504990 | 238 | -83.8 | 504990 | 316 |
| MR_1774412787_908664B4 | 504990 | 286 | -81.7 | 504990 | 90 | -84.8 | 504990 | 238 | -86.5 | 504990 | 316 |
| MR_1774412787_1FFC2138 | 504990 | 90 | -84.9 | 504990 | 286 | -79.0 | 504990 | 238 | -83.1 | 504990 | 316 |
| MR_1774412787_F29E9C6F | 504990 | 90 | -83.4 | 504990 | 286 | -79.3 | 504990 | 238 | -86.1 | 504990 | 316 |
| MR_1774412787_2843F5EC | 504990 | 286 | -81.3 | 504990 | 90 | -86.1 | 504990 | 238 | -86.2 | 504990 | 316 |
| MR_1774412787_C292D11A | 504990 | 286 | -82.4 | 504990 | 90 | -83.5 | 504990 | 238 | -86.0 | 504990 | 316 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1337: `a8e4eaf2-9be...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a8e4eaf2-9bed-4d99-9c4e-2abe900578ec` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease A3 Offset threshold for 3221613_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1337] topology](images/train_1337.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3246090_3 and 3214224_1
- `C2`: Adjust the azimuth of 3214224_1 by 20 degrees
- `C3`: Lift the tilt angle  of 3214224_1 by 10 degrees
- `C4`: Check test server and transmission issues
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221613_2
- `C6`: Add neighbor relationship between 3221613_2 and 3214224_1
- `C7`: Decrease A3 Offset threshold for 3214224_1
- `C8`: Increase A3 Offset threshold for 3221613_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221613_2
- `C10`: Decrease transmission power for 3214224_1
- `C11`: Increase A3 Offset threshold for 3214224_1
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Increase transmission power for 3214224_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214224_1
- `C15`: Increase transmission power for 3221613_2
- `C16`: Decrease A3 Offset threshold for 3221613_2 **← 정답**
- `C17`: Press down the tilt angle  of 3214224_1 by 10 degrees
- `C18`: Press down the tilt angle of 3221613_2 by 10 degrees
- `C19`: Decrease transmission power for 3221613_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214224_1
- `C21`: Adjust the azimuth of 3221613_2 by 50 degrees
- `C22`: Lift the tilt angle of 3221613_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.192 | MS1 | 121.4656748336 | 31.1446190025 | 830 | 504990 | -76.97 | 16.79 | 335.70 | 0.16 | 2.90 | 1577 |
| 2024-09-20 22:21:32.576 | MS1 | 121.4656751623 | 31.1446293285 | 830 | 504990 | -78.78 | 13.04 | 416.21 | 0.10 | 2.31 | 1568 |
| 2024-09-20 22:21:33.466 | MS1 | 121.4656665116 | 31.1446322768 | 830 | 504990 | -77.75 | 17.66 | 509.86 | 0.04 | 2.40 | 1587 |
| 2024-09-20 22:21:34.340 | MS1 | 121.4656635078 | 31.1446375479 | 830 | 504990 | -90.05 | -3.19 | 76.08 | 0.09 | 1.13 | 1591 |
| 2024-09-20 22:21:35.235 | MS1 | 121.4656590295 | 31.1446230432 | 830 | 504990 | -85.92 | -0.50 | 50.83 | 0.10 | 1.37 | 1579 |
| 2024-09-20 22:21:36.318 | MS1 | 121.4656714988 | 31.1446184804 | 830 | 504990 | -92.11 | -2.24 | 39.87 | 0.05 | 1.01 | 1591 |
| 2024-09-20 22:21:37.917 | MS1 | 121.4656764656 | 31.1446346709 | 830 | 504990 | -87.09 | -3.66 | 55.12 | 0.13 | 1.25 | 1578 |
| 2024-09-20 22:21:38.386 | MS1 | 121.4656700061 | 31.1446355540 | 830 | 504990 | -92.93 | -2.09 | 29.22 | 0.04 | 1.19 | 1564 |
| 2024-09-20 22:21:39.883 | MS1 | 121.4656726916 | 31.1446284708 | 264 | 504990 | -82.41 | 14.68 | 280.53 | 0.08 | 1.11 | 1596 |
| 2024-09-20 22:21:40.830 | MS1 | 121.4656658460 | 31.1446321325 | 264 | 504990 | -76.97 | 15.94 | 455.01 | 0.01 | 2.92 | 1585 |
| 2024-09-20 22:21:41.884 | MS1 | 121.4656731309 | 31.1446208940 | 264 | 504990 | -79.01 | 13.23 | 521.72 | 0.18 | 2.59 | 1580 |
| 2024-09-20 22:21:42.815 | MS1 | 121.4656770674 | 31.1446319276 | 264 | 504990 | -76.22 | 14.66 | 419.27 | 0.05 | 2.93 | 1568 |

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
| 3214224 | 1 | 121.4681757605 | 31.1529102797 | 215 | 11 | 2 | 16.1 | TDD | 264 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3221613 | 2 | 121.4645749016 | 31.1557008016 | 346 | 14 | 3 | 24.1 | TDD | 830 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3246090 | 3 | 121.4680269924 | 31.1454995286 | 235 | 5 | 2 | 18.5 | TDD | 590 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3255370 | 4 | 121.4720745504 | 31.1507461416 | 293 | 12 | 6 | 25.7 | TDD | 279 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.558 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.580 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.693 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.693 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.439 | NREventA3 | measId:2;ServCellPCI:234;Se... |
| 2024-09-20 22:21:38.679 | NRHandoverAttempt | SourcePCI:234;SourceNR-ARFC... |
| 2024-09-20 22:21:38.720 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.734 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.881 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.881 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214224 | 1 | 16.6479 | 12.2019 | -117.5437 | 8.6607 | 170.0502 | 0.0098 | 0.0113 |
| 2024_09_20 22:00 | 3221613 | 2 | 16.4927 | 7.6442 | -114.8646 | 9.5724 | 94.1170 | 0.0007 | 0.1517 |
| 2024_09_20 22:00 | 3246090 | 3 | 12.2384 | 5.0036 | -115.8440 | 16.3151 | 123.6760 | 0.0108 | 0.0143 |
| 2024_09_20 22:00 | 3255370 | 4 | 14.5310 | 17.3845 | -117.7917 | 18.8433 | 198.9043 | 0.0137 | 0.0065 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415184_75061C28 | 504990 | 830 | -90.9 | 504990 | 264 | -83.2 | 504990 | 590 | -88.8 | 504990 | 279 |
| MR_1774415184_02305EDC | 504990 | 830 | -91.2 | 504990 | 264 | -85.9 | 504990 | 590 | -91.2 | 504990 | 279 |
| MR_1774415184_5029B01F | 504990 | 264 | -85.9 | 504990 | 830 | -90.6 | 504990 | 590 | -90.7 | 504990 | 279 |
| MR_1774415184_6C5279B8 | 504990 | 830 | -88.8 | 504990 | 264 | -82.7 | 504990 | 590 | -87.5 | 504990 | 279 |
| MR_1774415184_0112223F | 504990 | 264 | -82.4 | 504990 | 830 | -89.0 | 504990 | 590 | -91.0 | 504990 | 279 |
| MR_1774415184_A0D39F15 | 504990 | 264 | -83.8 | 504990 | 830 | -90.6 | 504990 | 590 | -91.1 | 504990 | 279 |
| MR_1774415184_80233381 | 504990 | 264 | -84.7 | 504990 | 830 | -91.5 | 504990 | 590 | -88.1 | 504990 | 279 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1338: `867e0e5b-fc9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `867e0e5b-fc9e-4162-8d82-627aebb3b648` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Add neighbor relationship between 3259747_4 and 3272468_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1338] topology](images/train_1338.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259747_4
- `C2`: Adjust the azimuth of 3259747_4 by 50 degrees
- `C3`: Adjust the azimuth of 3272468_1 by 9 degrees
- `C4`: Lift the tilt angle of 3259747_4 by 10 degrees
- `C5`: Add neighbor relationship between 3259747_4 and 3272468_1 **← 정답**
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272468_1
- `C7`: Decrease transmission power for 3272468_1
- `C8`: Add neighbor relationship between 3255597_2 and 3272468_1
- `C9`: Lift the tilt angle  of 3272468_1 by 2 degrees
- `C10`: Decrease A3 Offset threshold for 3272468_1
- `C11`: Decrease A3 Offset threshold for 3259747_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259747_4
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Check test server and transmission issues
- `C15`: Increase A3 Offset threshold for 3272468_1
- `C16`: Increase A3 Offset threshold for 3259747_4
- `C17`: Decrease transmission power for 3259747_4
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272468_1
- `C19`: Increase transmission power for 3259747_4
- `C20`: Increase transmission power for 3272468_1
- `C21`: Press down the tilt angle  of 3272468_1 by 2 degrees
- `C22`: Press down the tilt angle of 3259747_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.241 | MS1 | 121.4656684074 | 31.1446353185 | 789 | 504990 | -79.98 | 16.70 | 384.47 | 0.08 | 2.08 | 1600 |
| 2024-09-20 22:21:32.813 | MS1 | 121.4656673748 | 31.1446342529 | 789 | 504990 | -81.82 | 13.52 | 387.54 | 0.07 | 2.98 | 1569 |
| 2024-09-20 22:21:33.934 | MS1 | 121.4656582333 | 31.1446228099 | 789 | 504990 | -83.78 | 14.50 | 434.37 | 0.03 | 2.15 | 1587 |
| 2024-09-20 22:21:34.597 | MS1 | 121.4656652308 | 31.1446230746 | 789 | 504990 | -90.97 | -2.68 | 50.88 | 0.04 | 1.06 | 1597 |
| 2024-09-20 22:21:35.608 | MS1 | 121.4656598026 | 31.1446371194 | 789 | 504990 | -94.88 | -1.74 | 46.03 | 0.01 | 1.17 | 1566 |
| 2024-09-20 22:21:36.778 | MS1 | 121.4656695096 | 31.1446376199 | 789 | 504990 | -91.17 | -3.42 | 55.59 | 0.00 | 1.43 | 1591 |
| 2024-09-20 22:21:37.130 | MS1 | 121.4656654901 | 31.1446281106 | 789 | 504990 | -88.91 | -0.20 | 45.73 | 0.00 | 1.25 | 1598 |
| 2024-09-20 22:21:38.735 | MS1 | 121.4656655654 | 31.1446208237 | 789 | 504990 | -77.68 | 12.61 | 527.77 | 0.09 | 1.41 | 1584 |
| 2024-09-20 22:21:39.328 | MS1 | 121.4656750440 | 31.1446354102 | 789 | 504990 | -77.84 | 15.46 | 438.37 | 0.11 | 1.40 | 1592 |
| 2024-09-20 22:21:40.576 | MS1 | 121.4656586301 | 31.1446356075 | 789 | 504990 | -82.49 | 16.37 | 478.81 | 0.10 | 2.75 | 1589 |
| 2024-09-20 22:21:41.365 | MS1 | 121.4656734467 | 31.1446211310 | 789 | 504990 | -82.65 | 14.33 | 438.92 | 0.05 | 2.41 | 1590 |
| 2024-09-20 22:21:42.215 | MS1 | 121.4656636867 | 31.1446304883 | 789 | 504990 | -78.76 | 13.37 | 558.00 | 0.11 | 2.96 | 1598 |

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
| 3212619 | 3 | 121.4674928686 | 31.1537491030 | 105 | 12 | 4 | 42.8 | TDD | 427 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3255597 | 2 | 121.4716645280 | 31.1531282402 | 134 | 10 | 11 | 35.2 | TDD | 537 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3259747 | 4 | 121.4664423454 | 31.1519179223 | 97 | 7 | 5 | 42.6 | TDD | 789 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3272468 | 1 | 121.4723270867 | 31.1534344997 | 204 | 0 | 10 | 38.5 | TDD | 363 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.884 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.902 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.043 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.043 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.705 | NREventA3 | measId:2;ServCellPCI:602;Se... |
| 2024-09-20 22:21:35.705 | NREventA3 | measId:2;ServCellPCI:602;Se... |
| 2024-09-20 22:21:36.705 | NREventA3 | measId:2;ServCellPCI:602;Se... |
| 2024-09-20 22:21:39.205 | NRRRCReestablishAttempt | PCI:602 |
| 2024-09-20 22:21:39.217 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.232 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.358 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.358 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272468 | 1 | 7.8544 | 12.2400 | -116.6948 | 19.2672 | 199.9489 | 0.0181 | 0.0055 |
| 2024_09_20 22:00 | 3255597 | 2 | 18.2210 | 6.1947 | -115.9793 | 10.5237 | 173.9442 | 0.0082 | 0.0197 |
| 2024_09_20 22:00 | 3212619 | 3 | 19.3383 | 5.7053 | -115.2913 | 8.0682 | 95.6234 | 0.0019 | 0.0101 |
| 2024_09_20 22:00 | 3259747 | 4 | 15.8853 | 7.8544 | -115.0563 | 7.5817 | 93.3426 | 0.0165 | 0.1355 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412020_029F9F6D | 504990 | 789 | -91.5 | 504990 | 363 | -84.0 | 504990 | 537 | -93.3 | 504990 | 427 |
| MR_1774412020_2B7FEC51 | 504990 | 363 | -84.0 | 504990 | 789 | -89.3 | 504990 | 537 | -94.5 | 504990 | 427 |
| MR_1774412020_A65C2FF5 | 504990 | 363 | -87.5 | 504990 | 789 | -92.5 | 504990 | 537 | -93.5 | 504990 | 427 |
| MR_1774412020_1362CAAE | 504990 | 789 | -91.6 | 504990 | 363 | -85.2 | 504990 | 537 | -95.5 | 504990 | 427 |
| MR_1774412020_DA26B51A | 504990 | 363 | -83.8 | 504990 | 789 | -91.2 | 504990 | 537 | -93.4 | 504990 | 427 |
| MR_1774412020_A8AEE499 | 504990 | 363 | -85.2 | 504990 | 789 | -92.2 | 504990 | 537 | -93.1 | 504990 | 427 |
| MR_1774412020_5E8B415D | 504990 | 363 | -87.7 | 504990 | 789 | -89.9 | 504990 | 537 | -93.7 | 504990 | 427 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1339: `58f13558-a2b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `58f13558-a2b2-44c3-bc74-595bf0003430` |
| Tag | **multiple-answer** |
| 정답 | **C5|C12** |
| C5 의미 | Increase transmission power for 3214100_4 |
| C12 의미 | Adjust the azimuth of 3214100_4 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1339] topology](images/train_1339.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease transmission power for 3248069_3
- `C3`: Lift the tilt angle  of 3248069_3 by 6 degrees
- `C4`: Add neighbor relationship between 3214100_4 and 3248069_3
- `C5`: Increase transmission power for 3214100_4 **← 정답**
- `C6`: Check test server and transmission issues
- `C7`: Increase A3 Offset threshold for 3214100_4
- `C8`: Press down the tilt angle  of 3248069_3 by 6 degrees
- `C9`: Increase transmission power for 3248069_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214100_4
- `C11`: Adjust the azimuth of 3248069_3 by 7 degrees
- `C12`: Adjust the azimuth of 3214100_4 by 50 degrees **← 정답**
- `C13`: Add neighbor relationship between 3236071_2 and 3248069_3
- `C14`: Decrease A3 Offset threshold for 3248069_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248069_3
- `C16`: Decrease transmission power for 3214100_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214100_4
- `C18`: Decrease A3 Offset threshold for 3214100_4
- `C19`: Lift the tilt angle of 3214100_4 by 7 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248069_3
- `C21`: Press down the tilt angle of 3214100_4 by 7 degrees
- `C22`: Increase A3 Offset threshold for 3248069_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.305 | MS1 | 121.4656713061 | 31.1446249267 | 239 | 504990 | -85.94 | 13.42 | 550.90 | 0.17 | 2.26 | 1595 |
| 2024-09-20 22:21:32.553 | MS1 | 121.4656745797 | 31.1446368469 | 239 | 504990 | -94.27 | 14.95 | 486.20 | 0.03 | 2.77 | 1597 |
| 2024-09-20 22:21:33.602 | MS1 | 121.4656701130 | 31.1446207274 | 239 | 504990 | -85.29 | 13.40 | 506.15 | 0.04 | 2.17 | 1567 |
| 2024-09-20 22:21:34.456 | MS1 | 121.4656775282 | 31.1446229812 | 239 | 504990 | -103.78 | 0.60 | 22.81 | 0.04 | 1.31 | 1573 |
| 2024-09-20 22:21:35.586 | MS1 | 121.4656702373 | 31.1446204540 | 239 | 504990 | -104.96 | 1.39 | 56.68 | 0.17 | 1.16 | 1583 |
| 2024-09-20 22:21:36.330 | MS1 | 121.4656752316 | 31.1446283037 | 239 | 504990 | -103.32 | -1.74 | 26.55 | 0.14 | 1.26 | 1572 |
| 2024-09-20 22:21:37.544 | MS1 | 121.4656596590 | 31.1446266192 | 239 | 504990 | -100.10 | -0.22 | 53.85 | 0.03 | 1.43 | 1564 |
| 2024-09-20 22:21:38.330 | MS1 | 121.4656680037 | 31.1446212838 | 239 | 504990 | -107.04 | 0.83 | 61.28 | 0.05 | 1.27 | 1586 |
| 2024-09-20 22:21:39.367 | MS1 | 121.4656628620 | 31.1446272193 | 239 | 504990 | -109.96 | -1.44 | 73.00 | 0.14 | 1.31 | 1589 |
| 2024-09-20 22:21:40.416 | MS1 | 121.4656719412 | 31.1446230054 | 239 | 504990 | -89.36 | 12.89 | 342.72 | 0.18 | 2.11 | 1560 |
| 2024-09-20 22:21:41.321 | MS1 | 121.4656740277 | 31.1446315497 | 239 | 504990 | -85.89 | 17.09 | 498.61 | 0.14 | 2.51 | 1568 |
| 2024-09-20 22:21:42.589 | MS1 | 121.4656599712 | 31.1446214168 | 239 | 504990 | -90.15 | 12.88 | 531.96 | 0.13 | 2.33 | 1574 |

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
| 3214100 | 4 | 121.4755832139 | 31.1463176956 | 321 | 6 | 12 | 19.4 | TDD | 239 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3219680 | 1 | 121.4665229021 | 31.1518496425 | 131 | 7 | 7 | 28.8 | TDD | 25 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3236071 | 2 | 121.4738268852 | 31.1442272429 | 73 | 0 | 0 | 18.2 | TDD | 836 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3248069 | 3 | 121.4669700848 | 31.1528860246 | 195 | 3 | 4 | 40.6 | TDD | 485 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.392 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.413 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.516 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.516 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.751 | NREventA2 | measId:1;ServCellPCI:688;Se... |
| 2024-09-20 22:21:34.887 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219680 | 1 | 8.5510 | 19.3652 | -115.9583 | 18.2732 | 158.0781 | 0.0105 | 0.0174 |
| 2024_09_20 22:00 | 3236071 | 2 | 19.1172 | 5.7222 | -117.4851 | 13.4932 | 160.4816 | 0.0051 | 0.0020 |
| 2024_09_20 22:00 | 3248069 | 3 | 8.8450 | 6.2482 | -116.6872 | 17.4155 | 136.2771 | 0.0198 | 0.0149 |
| 2024_09_20 22:00 | 3214100 | 4 | 13.0048 | 15.6744 | -116.2786 | 15.2841 | 173.1534 | 0.1791 | 0.0133 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414043_67948246 | 504990 | 239 | -103.3 | 504990 | 485 | -111.6 | 504990 | 836 | -114.5 | 504990 | 25 |
| MR_1774414043_EC3218FF | 504990 | 239 | -102.0 | 504990 | 485 | -109.6 | 504990 | 836 | -112.7 | 504990 | 25 |
| MR_1774414043_D1B5265A | 504990 | 239 | -105.4 | 504990 | 485 | -109.6 | 504990 | 836 | -114.6 | 504990 | 25 |
| MR_1774414043_A00E4F70 | 504990 | 239 | -102.0 | 504990 | 485 | -112.9 | 504990 | 836 | -113.1 | 504990 | 25 |
| MR_1774414043_28B960C2 | 504990 | 239 | -102.9 | 504990 | 485 | -110.4 | 504990 | 836 | -113.3 | 504990 | 25 |

> *... 2개 열 생략 (전체 14열)*

---
