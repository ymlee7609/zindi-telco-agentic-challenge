# Track A 문제 분석 — train[1180]~train[1189]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1180] ~ train[1189] (10개)

## 목차

1. [문제 1180: `d5be1518-f4e...`](#1180) — single-answer, 정답: C7
2. [문제 1181: `0ce70000-c9d...`](#1181) — single-answer, 정답: C10
3. [문제 1182: `b3bcf5cc-277...`](#1182) — single-answer, 정답: C14
4. [문제 1183: `12a227f8-9a8...`](#1183) — single-answer, 정답: C13
5. [문제 1184: `c472350e-420...`](#1184) — multiple-answer, 정답: C10|C12
6. [문제 1185: `3bbaf7ad-b67...`](#1185) — single-answer, 정답: C15
7. [문제 1186: `a8fe6f04-590...`](#1186) — single-answer, 정답: C1
8. [문제 1187: `01bdaa3c-41d...`](#1187) — multiple-answer, 정답: C4|C19
9. [문제 1188: `30119bbd-a3f...`](#1188) — single-answer, 정답: C11
10. [문제 1189: `e03cc3a5-57d...`](#1189) — multiple-answer, 정답: C9|C18

---

### 문제 1180: `d5be1518-f4e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d5be1518-f4ee-43b8-9e91-55674b1fc299` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3225532_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1180] topology](images/train_1180.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225532_3
- `C2`: Increase transmission power for 3217518_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217518_1
- `C4`: Decrease A3 Offset threshold for 3225532_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217518_1
- `C6`: Decrease transmission power for 3225532_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225532_3 **← 정답**
- `C8`: Decrease A3 Offset threshold for 3217518_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Increase A3 Offset threshold for 3225532_3
- `C11`: Increase A3 Offset threshold for 3217518_1
- `C12`: Adjust the azimuth of 3217518_1 by 50 degrees
- `C13`: Add neighbor relationship between 3229056_4 and 3217518_1
- `C14`: Check test server and transmission issues
- `C15`: Increase transmission power for 3225532_3
- `C16`: Press down the tilt angle  of 3217518_1 by 10 degrees
- `C17`: Decrease transmission power for 3217518_1
- `C18`: Lift the tilt angle of 3225532_3 by 3 degrees
- `C19`: Press down the tilt angle of 3225532_3 by 3 degrees
- `C20`: Lift the tilt angle  of 3217518_1 by 10 degrees
- `C21`: Add neighbor relationship between 3225532_3 and 3217518_1
- `C22`: Adjust the azimuth of 3225532_3 by 28 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.558 | MS1 | 121.4656705907 | 31.1446253831 | 67 | 504990 | -87.29 | 14.79 | 451.88 | 0.15 | 2.29 | 1575 |
| 2024-09-20 22:21:32.642 | MS1 | 121.4656774234 | 31.1446263821 | 67 | 504990 | -86.58 | 15.36 | 391.33 | 0.14 | 2.97 | 1589 |
| 2024-09-20 22:21:33.178 | MS1 | 121.4656587158 | 31.1446230607 | 67 | 504990 | -86.84 | 16.99 | 567.01 | 0.08 | 2.88 | 1579 |
| 2024-09-20 22:21:34.806 | MS1 | 121.4656744674 | 31.1446218946 | 67 | 504990 | -90.12 | 13.93 | 70.15 | 0.65 | 2.90 | 519 |
| 2024-09-20 22:21:35.591 | MS1 | 121.4656747422 | 31.1446317240 | 67 | 504990 | -85.78 | 15.14 | 59.23 | 0.69 | 2.21 | 554 |
| 2024-09-20 22:21:36.417 | MS1 | 121.4656727289 | 31.1446324936 | 67 | 504990 | -90.50 | 12.77 | 92.02 | 0.67 | 2.46 | 631 |
| 2024-09-20 22:21:37.806 | MS1 | 121.4656688626 | 31.1446220398 | 67 | 504990 | -90.43 | 7.52 | 75.51 | 0.53 | 2.85 | 553 |
| 2024-09-20 22:21:38.408 | MS1 | 121.4656696054 | 31.1446292214 | 67 | 504990 | -90.65 | 8.15 | 94.70 | 0.50 | 2.82 | 535 |
| 2024-09-20 22:21:39.401 | MS1 | 121.4656748915 | 31.1446219474 | 67 | 504990 | -89.08 | 9.21 | 61.28 | 0.55 | 2.56 | 693 |
| 2024-09-20 22:21:40.384 | MS1 | 121.4656769809 | 31.1446306764 | 67 | 504990 | -93.73 | 12.88 | 519.96 | 0.09 | 2.19 | 1571 |
| 2024-09-20 22:21:41.805 | MS1 | 121.4656651796 | 31.1446263705 | 67 | 504990 | -90.25 | 8.06 | 585.60 | 0.08 | 2.44 | 1574 |
| 2024-09-20 22:21:42.666 | MS1 | 121.4656703697 | 31.1446255431 | 67 | 504990 | -89.85 | 7.28 | 384.07 | 0.09 | 2.55 | 1591 |

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
| 3217518 | 1 | 121.4667634619 | 31.1457233295 | 46 | 5 | 2 | 39.5 | TDD | 457 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3225532 | 3 | 121.4740262258 | 31.1519292688 | 196 | 1 | 3 | 44.6 | TDD | 67 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3229056 | 4 | 121.4671842799 | 31.1526072934 | 255 | 13 | 0 | 25.9 | TDD | 125 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3262281 | 2 | 121.4743884996 | 31.1465151910 | 313 | 14 | 0 | 29.7 | TDD | 330 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.395 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.415 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.551 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.551 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.270 | NREventA3 | measId:2;ServCellPCI:134;Se... |
| 2024-09-20 22:21:38.510 | NRHandoverAttempt | SourcePCI:134;SourceNR-ARFC... |
| 2024-09-20 22:21:38.546 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.560 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.685 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.685 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217518 | 1 | 15.9462 | 6.3863 | -116.4466 | 15.3006 | 92.3869 | 0.0121 | 0.0086 |
| 2024_09_20 22:00 | 3262281 | 2 | 18.3539 | 7.6632 | -117.4867 | 8.8119 | 189.0966 | 0.0167 | 0.0175 |
| 2024_09_20 22:00 | 3225532 | 3 | 8.1769 | 8.8487 | -115.7764 | 14.6778 | 163.9499 | 0.0128 | 0.0178 |
| 2024_09_20 22:00 | 3229056 | 4 | 12.4864 | 10.1961 | -116.7995 | 12.6636 | 163.7107 | 0.0050 | 0.0074 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412655_47213393 | 504990 | 67 | -90.6 | 504990 | 457 | -95.7 | 504990 | 125 | -97.6 | 504990 | 330 |
| MR_1774412655_25F6CF38 | 504990 | 67 | -88.5 | 504990 | 457 | -96.0 | 504990 | 125 | -97.5 | 504990 | 330 |
| MR_1774412655_2A866227 | 504990 | 67 | -90.7 | 504990 | 457 | -97.1 | 504990 | 125 | -98.4 | 504990 | 330 |
| MR_1774412655_884B4BB5 | 504990 | 67 | -88.6 | 504990 | 457 | -97.8 | 504990 | 125 | -98.1 | 504990 | 330 |
| MR_1774412655_30EFBBAC | 504990 | 67 | -90.7 | 504990 | 457 | -97.4 | 504990 | 125 | -99.0 | 504990 | 330 |
| MR_1774412655_82503737 | 504990 | 67 | -90.7 | 504990 | 457 | -96.3 | 504990 | 125 | -99.0 | 504990 | 330 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1181: `0ce70000-c9d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0ce70000-c9df-45c6-bdff-38c32380d167` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273580_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1181] topology](images/train_1181.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3229892_13 and 3214150_6
- `C2`: Increase transmission power for 3214150_6
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214150_6
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease transmission power for 3214150_6
- `C6`: Press down the tilt angle of 3273580_1 by 5 degrees
- `C7`: Increase transmission power for 3273580_1
- `C8`: Press down the tilt angle  of 3214150_6 by 4 degrees
- `C9`: Lift the tilt angle  of 3214150_6 by 4 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273580_1 **← 정답**
- `C11`: Check test server and transmission issues
- `C12`: Adjust the azimuth of 3273580_1 by 17 degrees
- `C13`: Decrease transmission power for 3273580_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273580_1
- `C15`: Add neighbor relationship between 3273580_1 and 3214150_6
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214150_6
- `C17`: Lift the tilt angle of 3273580_1 by 5 degrees
- `C18`: Adjust the azimuth of 3214150_6 by 47 degrees
- `C19`: Decrease A3 Offset threshold for 3273580_1
- `C20`: Increase A3 Offset threshold for 3214150_6
- `C21`: Increase A3 Offset threshold for 3273580_1
- `C22`: Decrease A3 Offset threshold for 3214150_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.518 | MS1 | 121.4656610747 | 31.1446359572 | 771 | 504990 | -94.49 | 14.33 | 578.43 | 0.14 | 2.03 | 1567 |
| 2024-09-20 22:21:32.292 | MS1 | 121.4656673421 | 31.1446263866 | 1004 | 504990 | -94.27 | 10.78 | 528.38 | 0.13 | 2.73 | 1597 |
| 2024-09-20 22:21:33.801 | MS1 | 121.4656708639 | 31.1446291755 | 11 | 504990 | -93.15 | 12.09 | 351.30 | 0.10 | 2.90 | 1592 |
| 2024-09-20 22:21:34.396 | MS1 | 121.4656717909 | 31.1446227580 | 435 | 152650 | -90.30 | 7.95 | 50.39 | 0.19 | 1.56 | 900 |
| 2024-09-20 22:21:35.944 | MS1 | 121.4656710988 | 31.1446241504 | 936 | 152650 | -92.90 | 7.98 | 74.00 | 0.05 | 1.51 | 916 |
| 2024-09-20 22:21:36.383 | MS1 | 121.4656693737 | 31.1446236025 | 959 | 152650 | -91.57 | 7.94 | 68.29 | 0.02 | 1.94 | 904 |
| 2024-09-20 22:21:37.780 | MS1 | 121.4656589185 | 31.1446184089 | 59 | 152650 | -90.37 | 4.34 | 78.46 | 0.18 | 1.80 | 924 |
| 2024-09-20 22:21:38.306 | MS1 | 121.4656601385 | 31.1446370056 | 435 | 152650 | -95.26 | 2.33 | 57.61 | 0.07 | 1.98 | 924 |
| 2024-09-20 22:21:39.655 | MS1 | 121.4656676513 | 31.1446340486 | 936 | 152650 | -95.66 | 4.25 | 60.42 | 0.06 | 1.61 | 952 |
| 2024-09-20 22:21:40.260 | MS1 | 121.4656746553 | 31.1446318197 | 959 | 152650 | -93.39 | 6.74 | 58.04 | 0.02 | 2.29 | 1561 |
| 2024-09-20 22:21:41.210 | MS1 | 121.4656697501 | 31.1446181520 | 59 | 152650 | -95.57 | 2.37 | 72.18 | 0.18 | 2.84 | 1574 |
| 2024-09-20 22:21:42.828 | MS1 | 121.4656636300 | 31.1446181249 | 435 | 152650 | -87.56 | 2.08 | 85.67 | 0.06 | 2.94 | 1588 |

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
| 3214150 | 6 | 121.4739121486 | 31.1509260462 | 181 | 3 | 7 | 23.3 | TDD | 27 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3214384 | 8 | 121.4684302666 | 31.1448057031 | 259 | 11 | 10 | 20.6 | FDD | 337 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3218139 | 11 | 121.4689792675 | 31.1539809260 | 140 | 7 | 1 | 13.0 | FDD | 377 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3220184 | 5 | 121.4736299425 | 31.1446950187 | 15 | 1 | 6 | 2.3 | TDD | 47 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3229892 | 13 | 121.4748122512 | 31.1510803465 | 184 | 11 | 6 | 0.5 | FDD | 959 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3235922 | 7 | 121.4750904342 | 31.1469808593 | 178 | 1 | 1 | 15.9 | FDD | 936 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3237219 | 4 | 121.4694766841 | 31.1532011854 | 346 | 1 | 11 | 20.2 | TDD | 123 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3238406 | 2 | 121.4666894469 | 31.1510564990 | 207 | 13 | 12 | 1.7 | TDD | 11 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3261718 | 3 | 121.4729520873 | 31.1461349053 | 14 | 9 | 3 | 1.7 | TDD | 1004 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3270114 | 10 | 121.4648130163 | 31.1446486678 | 347 | 9 | 1 | 20.9 | FDD | 535 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3270383 | 9 | 121.4642577344 | 31.1549767633 | 154 | 8 | 2 | 2.2 | FDD | 435 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3273568 | 12 | 121.4753029844 | 31.1505676309 | 238 | 12 | 4 | 11.8 | FDD | 59 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3273580 | 1 | 121.4729645813 | 31.1525316002 | 235 | 4 | 5 | 17.7 | TDD | 771 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.813 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.831 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.965 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.965 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.647 | NREventA2 | measId:1;ServCellPCI:296;Se... |
| 2024-09-20 22:21:34.782 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.002 | NREventA5 | measId:3;ServCellPCI:296;Se... |
| 2024-09-20 22:21:35.057 | NRHandoverAttempt | SourcePCI:296;SourceNR-ARFC... |
| 2024-09-20 22:21:35.089 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.099 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.231 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.231 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273580 | 1 | 19.3079 | 6.8364 | -115.1496 | 5.2941 | 141.8947 | 0.0054 | 0.0071 |
| 2024_09_20 22:00 | 3238406 | 2 | 9.6252 | 17.8723 | -114.3923 | 18.8268 | 146.4125 | 0.0008 | 0.0197 |
| 2024_09_20 22:00 | 3261718 | 3 | 5.6961 | 19.5143 | -115.7917 | 17.1447 | 97.1534 | 0.0031 | 0.0028 |
| 2024_09_20 22:00 | 3237219 | 4 | 12.1165 | 9.5905 | -114.6707 | 13.5021 | 195.7222 | 0.0142 | 0.0058 |
| 2024_09_20 22:00 | 3220184 | 5 | 13.8409 | 12.2183 | -116.8919 | 13.7804 | 113.5274 | 0.0017 | 0.0163 |
| 2024_09_20 22:00 | 3214150 | 6 | 5.4135 | 18.5329 | -117.6766 | 18.6763 | 137.3442 | 0.0137 | 0.0108 |
| 2024_09_20 22:00 | 3235922 | 7 | 17.7528 | 8.9043 | -115.2269 | 4.8670 | 36.3577 | 0.0148 | 0.0144 |
| 2024_09_20 22:00 | 3214384 | 8 | 15.6052 | 18.3204 | -114.1647 | 4.5730 | 59.4305 | 0.0072 | 0.0116 |
| 2024_09_20 22:00 | 3270383 | 9 | 18.3556 | 10.2019 | -115.2488 | 3.6773 | 52.1262 | 0.0127 | 0.0199 |
| 2024_09_20 22:00 | 3270114 | 10 | 15.7091 | 14.6231 | -116.8376 | 3.1645 | 45.5708 | 0.0162 | 0.0143 |
| 2024_09_20 22:00 | 3218139 | 11 | 8.9616 | 13.4207 | -115.6928 | 3.0136 | 30.4849 | 0.0031 | 0.0171 |
| 2024_09_20 22:00 | 3273568 | 12 | 14.9062 | 10.4479 | -117.4733 | 3.3223 | 25.3045 | 0.0002 | 0.0090 |
| 2024_09_20 22:00 | 3229892 | 13 | 8.8122 | 9.6957 | -117.6981 | 4.5662 | 46.9648 | 0.0055 | 0.0131 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414306_EA61176A | 504990 | 11 | -93.2 | 504990 | 27 | -93.6 | 504990 | 47 | -94.6 | 504990 | 123 |
| MR_1774414306_AEC570C5 | 504990 | 11 | -91.4 | 504990 | 27 | -94.3 | 504990 | 47 | -96.3 | 504990 | 123 |
| MR_1774414306_5E482887 | 504990 | 11 | -92.9 | 504990 | 27 | -91.7 | 504990 | 47 | -93.0 | 504990 | 123 |
| MR_1774414306_A1C0945D | 152650 | 435 | -88.5 | 152650 | 377 | -95.0 | 152650 | 337 | -101.6 | 152650 | 535 |
| MR_1774414306_E166E351 | 504990 | 11 | -92.1 | 504990 | 27 | -92.6 | 504990 | 47 | -93.9 | 504990 | 123 |
| MR_1774414306_C4E3242D | 504990 | 11 | -92.2 | 504990 | 27 | -92.8 | 504990 | 47 | -94.8 | 504990 | 123 |
| MR_1774414306_5C0DCA48 | 152650 | 435 | -90.7 | 152650 | 377 | -96.4 | 152650 | 337 | -98.8 | 152650 | 535 |
| MR_1774414306_0C4626D3 | 504990 | 11 | -93.6 | 504990 | 27 | -91.5 | 504990 | 47 | -95.1 | 504990 | 123 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1182: `b3bcf5cc-277...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b3bcf5cc-2773-423f-a152-085a4a5eb160` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277817_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1182] topology](images/train_1182.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3277817_3
- `C2`: Add neighbor relationship between 3277817_3 and 3214462_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214462_4
- `C4`: Adjust the azimuth of 3214462_4 by 46 degrees
- `C5`: Add neighbor relationship between 3234569_7 and 3214462_4
- `C6`: Decrease A3 Offset threshold for 3277817_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214462_4
- `C8`: Check test server and transmission issues
- `C9`: Lift the tilt angle  of 3214462_4 by 5 degrees
- `C10`: Increase A3 Offset threshold for 3277817_3
- `C11`: Lift the tilt angle of 3277817_3 by 2 degrees
- `C12`: Increase transmission power for 3214462_4
- `C13`: Press down the tilt angle of 3277817_3 by 2 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277817_3 **← 정답**
- `C15`: Adjust the azimuth of 3277817_3 by 6 degrees
- `C16`: Press down the tilt angle  of 3214462_4 by 5 degrees
- `C17`: Decrease A3 Offset threshold for 3214462_4
- `C18`: Increase transmission power for 3277817_3
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277817_3
- `C21`: Decrease transmission power for 3214462_4
- `C22`: Increase A3 Offset threshold for 3214462_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.540 | MS1 | 121.4656628914 | 31.1446320047 | 970 | 504990 | -93.22 | 13.46 | 503.07 | 0.19 | 2.17 | 1583 |
| 2024-09-20 22:21:32.658 | MS1 | 121.4656636567 | 31.1446346396 | 503 | 504990 | -93.27 | 9.58 | 321.20 | 0.17 | 2.85 | 1571 |
| 2024-09-20 22:21:33.165 | MS1 | 121.4656600272 | 31.1446213509 | 640 | 504990 | -94.58 | 13.32 | 418.61 | 0.16 | 2.47 | 1564 |
| 2024-09-20 22:21:34.574 | MS1 | 121.4656619559 | 31.1446210098 | 818 | 152650 | -95.31 | 3.29 | 89.58 | 0.13 | 1.57 | 984 |
| 2024-09-20 22:21:35.964 | MS1 | 121.4656756523 | 31.1446259881 | 889 | 152650 | -94.50 | 7.41 | 52.40 | 0.13 | 1.75 | 996 |
| 2024-09-20 22:21:36.905 | MS1 | 121.4656753171 | 31.1446226406 | 928 | 152650 | -87.70 | 5.14 | 57.75 | 0.08 | 1.64 | 996 |
| 2024-09-20 22:21:37.605 | MS1 | 121.4656681171 | 31.1446339550 | 323 | 152650 | -87.04 | 3.72 | 69.36 | 0.10 | 1.77 | 943 |
| 2024-09-20 22:21:38.644 | MS1 | 121.4656767587 | 31.1446181335 | 818 | 152650 | -88.46 | 5.83 | 58.89 | 0.13 | 1.99 | 989 |
| 2024-09-20 22:21:39.175 | MS1 | 121.4656586594 | 31.1446237305 | 889 | 152650 | -91.58 | 5.27 | 94.55 | 0.07 | 1.90 | 953 |
| 2024-09-20 22:21:40.972 | MS1 | 121.4656753269 | 31.1446336395 | 928 | 152650 | -93.58 | 6.49 | 101.63 | 0.07 | 2.86 | 1587 |
| 2024-09-20 22:21:41.108 | MS1 | 121.4656709405 | 31.1446225383 | 323 | 152650 | -95.45 | 6.91 | 86.57 | 0.06 | 2.79 | 1582 |
| 2024-09-20 22:21:42.265 | MS1 | 121.4656619708 | 31.1446290749 | 818 | 152650 | -88.12 | 4.88 | 53.91 | 0.15 | 2.44 | 1592 |

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
| 3210716 | 13 | 121.4709936477 | 31.1519231753 | 71 | 10 | 3 | 5.5 | FDD | 63 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3213083 | 2 | 121.4686484040 | 31.1557417769 | 81 | 13 | 12 | 7.6 | TDD | 353 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3214462 | 4 | 121.4746417921 | 31.1466083876 | 302 | 4 | 7 | 11.3 | TDD | 491 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3219377 | 10 | 121.4643827738 | 31.1549385524 | 16 | 8 | 0 | 11.1 | FDD | 808 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3223074 | 1 | 121.4757525925 | 31.1477894725 | 294 | 4 | 10 | 3.1 | TDD | 640 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3223212 | 6 | 121.4640542852 | 31.1449818233 | 47 | 14 | 4 | 21.9 | TDD | 988 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3233035 | 11 | 121.4710510397 | 31.1509328764 | 4 | 11 | 11 | 1.1 | FDD | 818 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3234569 | 7 | 121.4677204873 | 31.1544183161 | 292 | 10 | 4 | 8.7 | FDD | 928 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3240707 | 9 | 121.4684957471 | 31.1452829575 | 264 | 10 | 3 | 24.6 | FDD | 262 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3245564 | 5 | 121.4689804016 | 31.1442320719 | 87 | 3 | 11 | 11.1 | TDD | 503 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3255694 | 12 | 121.4663418749 | 31.1446459979 | 183 | 12 | 0 | 3.9 | FDD | 889 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3265867 | 8 | 121.4750653473 | 31.1486061188 | 23 | 0 | 11 | 6.5 | FDD | 323 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3277817 | 3 | 121.4667138212 | 31.1553077247 | 179 | 1 | 7 | 19.5 | TDD | 970 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.022 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.044 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.155 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.155 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.916 | NREventA2 | measId:1;ServCellPCI:399;Se... |
| 2024-09-20 22:21:35.051 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.307 | NREventA5 | measId:3;ServCellPCI:399;Se... |
| 2024-09-20 22:21:35.384 | NRHandoverAttempt | SourcePCI:399;SourceNR-ARFC... |
| 2024-09-20 22:21:35.419 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.431 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.569 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.569 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223074 | 1 | 15.4612 | 15.5300 | -117.1232 | 14.2287 | 161.9956 | 0.0005 | 0.0134 |
| 2024_09_20 22:00 | 3213083 | 2 | 9.9344 | 16.3845 | -115.4787 | 6.3209 | 135.6549 | 0.0126 | 0.0132 |
| 2024_09_20 22:00 | 3277817 | 3 | 14.2228 | 10.0693 | -117.4708 | 14.8525 | 191.0162 | 0.0096 | 0.0021 |
| 2024_09_20 22:00 | 3214462 | 4 | 7.4423 | 9.6283 | -116.3277 | 10.4249 | 142.6652 | 0.0181 | 0.0078 |
| 2024_09_20 22:00 | 3245564 | 5 | 7.5795 | 8.0724 | -114.8601 | 13.6483 | 87.8928 | 0.0198 | 0.0112 |
| 2024_09_20 22:00 | 3223212 | 6 | 5.2848 | 7.1618 | -116.3785 | 16.4422 | 127.2736 | 0.0198 | 0.0012 |
| 2024_09_20 22:00 | 3234569 | 7 | 13.6729 | 16.8075 | -116.7793 | 3.8927 | 54.8444 | 0.0007 | 0.0200 |
| 2024_09_20 22:00 | 3265867 | 8 | 6.7847 | 6.8472 | -116.3315 | 4.1630 | 59.6551 | 0.0054 | 0.0157 |
| 2024_09_20 22:00 | 3240707 | 9 | 10.3990 | 9.0345 | -116.5824 | 3.3704 | 51.6894 | 0.0040 | 0.0080 |
| 2024_09_20 22:00 | 3219377 | 10 | 7.4115 | 6.5763 | -116.8411 | 3.6752 | 54.6689 | 0.0197 | 0.0131 |
| 2024_09_20 22:00 | 3233035 | 11 | 10.6751 | 15.0403 | -114.3917 | 4.0975 | 27.8796 | 0.0113 | 0.0153 |
| 2024_09_20 22:00 | 3255694 | 12 | 14.3555 | 14.8038 | -117.3071 | 3.2647 | 59.0514 | 0.0192 | 0.0169 |
| 2024_09_20 22:00 | 3210716 | 13 | 8.3123 | 18.6591 | -116.1104 | 4.3524 | 31.3760 | 0.0100 | 0.0186 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414017_2B8003D1 | 152650 | 818 | -96.7 | 152650 | 808 | -99.3 | 152650 | 262 | -101.0 | 152650 | 63 |
| MR_1774414017_22A1D4FF | 504990 | 640 | -94.9 | 504990 | 491 | -99.2 | 504990 | 988 | -98.6 | 504990 | 353 |
| MR_1774414017_47DBFC91 | 152650 | 818 | -96.0 | 152650 | 808 | -97.2 | 152650 | 262 | -103.9 | 152650 | 63 |
| MR_1774414017_D4AF027D | 152650 | 818 | -94.8 | 152650 | 808 | -98.4 | 152650 | 262 | -100.5 | 152650 | 63 |
| MR_1774414017_2C7DBE56 | 152650 | 818 | -97.0 | 152650 | 808 | -98.4 | 152650 | 262 | -101.9 | 152650 | 63 |
| MR_1774414017_4E714829 | 152650 | 818 | -94.6 | 152650 | 808 | -97.7 | 152650 | 262 | -103.9 | 152650 | 63 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1183: `12a227f8-9a8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `12a227f8-9a84-44fb-a35e-c17f495ffbb4` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3222829_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1183] topology](images/train_1183.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3222829_1
- `C2`: Decrease A3 Offset threshold for 3242319_2
- `C3`: Press down the tilt angle of 3222829_1 by 3 degrees
- `C4`: Increase transmission power for 3222829_1
- `C5`: Press down the tilt angle  of 3242319_2 by 10 degrees
- `C6`: Check test server and transmission issues
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242319_2
- `C8`: Lift the tilt angle  of 3242319_2 by 10 degrees
- `C9`: Decrease A3 Offset threshold for 3222829_1
- `C10`: Adjust the azimuth of 3222829_1 by 18 degrees
- `C11`: Increase A3 Offset threshold for 3222829_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242319_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222829_1 **← 정답**
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase transmission power for 3242319_2
- `C16`: Lift the tilt angle of 3222829_1 by 3 degrees
- `C17`: Add neighbor relationship between 3222829_1 and 3242319_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222829_1
- `C19`: Increase A3 Offset threshold for 3242319_2
- `C20`: Add neighbor relationship between 3278335_4 and 3242319_2
- `C21`: Adjust the azimuth of 3242319_2 by 50 degrees
- `C22`: Decrease transmission power for 3242319_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.974 | MS1 | 121.4656648257 | 31.1446256606 | 999 | 504990 | -89.88 | 12.84 | 441.43 | 0.03 | 2.47 | 1596 |
| 2024-09-20 22:21:32.678 | MS1 | 121.4656779166 | 31.1446250191 | 999 | 504990 | -85.55 | 13.00 | 330.68 | 0.10 | 2.64 | 1563 |
| 2024-09-20 22:21:33.456 | MS1 | 121.4656653750 | 31.1446359610 | 999 | 504990 | -86.16 | 16.71 | 423.06 | 0.07 | 2.80 | 1587 |
| 2024-09-20 22:21:34.801 | MS1 | 121.4656666264 | 31.1446359531 | 999 | 504990 | -85.54 | 16.76 | 51.76 | 0.57 | 2.65 | 663 |
| 2024-09-20 22:21:35.744 | MS1 | 121.4656682248 | 31.1446266781 | 999 | 504990 | -88.70 | 16.61 | 43.20 | 0.66 | 2.31 | 506 |
| 2024-09-20 22:21:36.307 | MS1 | 121.4656747581 | 31.1446248979 | 999 | 504990 | -90.83 | 12.58 | 53.48 | 0.63 | 2.12 | 542 |
| 2024-09-20 22:21:37.189 | MS1 | 121.4656757962 | 31.1446197857 | 999 | 504990 | -92.79 | 12.65 | 62.65 | 0.66 | 2.32 | 514 |
| 2024-09-20 22:21:38.496 | MS1 | 121.4656641891 | 31.1446335195 | 999 | 504990 | -90.81 | 10.11 | 90.74 | 0.52 | 2.64 | 606 |
| 2024-09-20 22:21:39.836 | MS1 | 121.4656708274 | 31.1446226454 | 999 | 504990 | -90.60 | 8.08 | 81.80 | 0.52 | 2.27 | 587 |
| 2024-09-20 22:21:40.696 | MS1 | 121.4656643060 | 31.1446311735 | 999 | 504990 | -93.55 | 8.83 | 411.04 | 0.20 | 2.52 | 1571 |
| 2024-09-20 22:21:41.304 | MS1 | 121.4656772637 | 31.1446274927 | 999 | 504990 | -89.14 | 10.84 | 488.37 | 0.03 | 2.17 | 1594 |
| 2024-09-20 22:21:42.798 | MS1 | 121.4656696180 | 31.1446308456 | 999 | 504990 | -92.94 | 8.08 | 453.59 | 0.06 | 2.01 | 1564 |

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
| 3222829 | 1 | 121.4729443942 | 31.1523821433 | 237 | 2 | 1 | 27.7 | TDD | 999 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3242319 | 2 | 121.4751548416 | 31.1452456111 | 103 | 11 | 3 | 34.5 | TDD | 11 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3276892 | 3 | 121.4707179974 | 31.1441371904 | 19 | 3 | 5 | 28.3 | TDD | 422 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3278335 | 4 | 121.4647855357 | 31.1494387929 | 313 | 2 | 5 | 27.9 | TDD | 39 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.048 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.068 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.177 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.177 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.881 | NREventA3 | measId:2;ServCellPCI:826;Se... |
| 2024-09-20 22:21:38.121 | NRHandoverAttempt | SourcePCI:826;SourceNR-ARFC... |
| 2024-09-20 22:21:38.158 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.168 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.311 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.311 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222829 | 1 | 19.9688 | 11.7928 | -115.5107 | 18.3672 | 158.6886 | 0.0083 | 0.0159 |
| 2024_09_20 22:00 | 3242319 | 2 | 7.5531 | 13.5183 | -117.6329 | 11.1844 | 140.7991 | 0.0152 | 0.0093 |
| 2024_09_20 22:00 | 3276892 | 3 | 12.3070 | 5.3253 | -114.6201 | 14.9468 | 142.8606 | 0.0183 | 0.0049 |
| 2024_09_20 22:00 | 3278335 | 4 | 6.5151 | 13.2296 | -114.6462 | 17.4559 | 192.4292 | 0.0152 | 0.0084 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412733_5C52EFA0 | 504990 | 999 | -85.6 | 504990 | 11 | -93.3 | 504990 | 39 | -93.9 | 504990 | 422 |
| MR_1774412733_C047110E | 504990 | 999 | -87.2 | 504990 | 11 | -91.8 | 504990 | 39 | -96.9 | 504990 | 422 |
| MR_1774412733_924F4385 | 504990 | 999 | -83.8 | 504990 | 11 | -94.7 | 504990 | 39 | -95.9 | 504990 | 422 |
| MR_1774412733_423560E5 | 504990 | 999 | -83.8 | 504990 | 11 | -92.5 | 504990 | 39 | -96.0 | 504990 | 422 |
| MR_1774412733_D804703D | 504990 | 999 | -86.8 | 504990 | 11 | -94.3 | 504990 | 39 | -94.1 | 504990 | 422 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1184: `c472350e-420...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c472350e-420c-42d0-a069-5b1c55a99296` |
| Tag | **multiple-answer** |
| 정답 | **C10|C12** |
| C10 의미 | Adjust the azimuth of 3216905_3 by 50 degrees |
| C12 의미 | Increase transmission power for 3216905_3 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1184] topology](images/train_1184.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3279725_4 and 3238367_2
- `C2`: Decrease transmission power for 3238367_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216905_3
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Lift the tilt angle  of 3238367_2 by 6 degrees
- `C6`: Increase A3 Offset threshold for 3216905_3
- `C7`: Press down the tilt angle  of 3238367_2 by 6 degrees
- `C8`: Increase A3 Offset threshold for 3238367_2
- `C9`: Adjust the azimuth of 3238367_2 by 28 degrees
- `C10`: Adjust the azimuth of 3216905_3 by 50 degrees **← 정답**
- `C11`: Lift the tilt angle of 3216905_3 by 10 degrees
- `C12`: Increase transmission power for 3216905_3 **← 정답**
- `C13`: Decrease A3 Offset threshold for 3238367_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238367_2
- `C15`: Press down the tilt angle of 3216905_3 by 10 degrees
- `C16`: Increase transmission power for 3238367_2
- `C17`: Decrease transmission power for 3216905_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216905_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238367_2
- `C20`: Decrease A3 Offset threshold for 3216905_3
- `C21`: Check test server and transmission issues
- `C22`: Add neighbor relationship between 3216905_3 and 3238367_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.183 | MS1 | 121.4656643140 | 31.1446205991 | 570 | 504990 | -89.74 | 16.76 | 513.26 | 0.03 | 2.20 | 1579 |
| 2024-09-20 22:21:32.407 | MS1 | 121.4656581864 | 31.1446335468 | 570 | 504990 | -94.39 | 14.21 | 523.86 | 0.15 | 2.57 | 1578 |
| 2024-09-20 22:21:33.376 | MS1 | 121.4656707350 | 31.1446216760 | 570 | 504990 | -90.83 | 17.53 | 324.91 | 0.11 | 2.67 | 1569 |
| 2024-09-20 22:21:34.483 | MS1 | 121.4656771087 | 31.1446378491 | 570 | 504990 | -101.86 | -1.65 | 39.36 | 0.15 | 1.28 | 1598 |
| 2024-09-20 22:21:35.977 | MS1 | 121.4656617651 | 31.1446235508 | 570 | 504990 | -104.40 | 0.42 | 25.13 | 0.12 | 1.38 | 1565 |
| 2024-09-20 22:21:36.561 | MS1 | 121.4656707083 | 31.1446328442 | 570 | 504990 | -104.41 | -1.91 | 39.86 | 0.19 | 1.07 | 1566 |
| 2024-09-20 22:21:37.173 | MS1 | 121.4656698970 | 31.1446223143 | 570 | 504990 | -103.68 | 1.46 | 23.52 | 0.09 | 1.22 | 1595 |
| 2024-09-20 22:21:38.666 | MS1 | 121.4656617354 | 31.1446217477 | 570 | 504990 | -103.22 | -1.34 | 54.96 | 0.09 | 1.26 | 1598 |
| 2024-09-20 22:21:39.387 | MS1 | 121.4656731712 | 31.1446272497 | 570 | 504990 | -109.65 | 0.89 | 39.95 | 0.12 | 1.29 | 1584 |
| 2024-09-20 22:21:40.576 | MS1 | 121.4656583901 | 31.1446288527 | 570 | 504990 | -91.82 | 17.91 | 565.70 | 0.03 | 2.00 | 1596 |
| 2024-09-20 22:21:41.385 | MS1 | 121.4656626912 | 31.1446211367 | 570 | 504990 | -88.15 | 15.85 | 357.30 | 0.14 | 2.73 | 1578 |
| 2024-09-20 22:21:42.655 | MS1 | 121.4656667444 | 31.1446228092 | 570 | 504990 | -90.11 | 17.87 | 494.39 | 0.12 | 2.09 | 1584 |

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
| 3216905 | 3 | 121.4731789157 | 31.1457669922 | 322 | 14 | 3 | 21.4 | TDD | 570 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3230346 | 1 | 121.4725880669 | 31.1489992245 | 42 | 15 | 9 | 46.3 | TDD | 240 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3238367 | 2 | 121.4752958738 | 31.1553756641 | 245 | 5 | 9 | 24.8 | TDD | 889 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3279725 | 4 | 121.4652405892 | 31.1536022327 | 129 | 3 | 9 | 46.8 | TDD | 57 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.381 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.396 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.543 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.543 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.714 | NREventA2 | measId:1;ServCellPCI:232;Se... |
| 2024-09-20 22:21:34.833 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230346 | 1 | 8.1363 | 8.7810 | -115.9108 | 16.3215 | 86.8391 | 0.0035 | 0.0180 |
| 2024_09_20 22:00 | 3238367 | 2 | 12.0327 | 11.1297 | -114.5119 | 16.4884 | 174.4734 | 0.0126 | 0.0045 |
| 2024_09_20 22:00 | 3216905 | 3 | 9.4177 | 11.5154 | -117.0092 | 18.6481 | 105.9914 | 0.1110 | 0.0068 |
| 2024_09_20 22:00 | 3279725 | 4 | 10.3963 | 17.6971 | -115.2645 | 16.7976 | 85.4881 | 0.0097 | 0.0063 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416393_F2BF2B78 | 504990 | 570 | -102.1 | 504990 | 889 | -107.3 | 504990 | 57 | -114.6 | 504990 | 240 |
| MR_1774416393_97942693 | 504990 | 570 | -101.6 | 504990 | 889 | -105.0 | 504990 | 57 | -115.0 | 504990 | 240 |
| MR_1774416393_573B6B67 | 504990 | 570 | -101.0 | 504990 | 889 | -105.8 | 504990 | 57 | -112.5 | 504990 | 240 |
| MR_1774416393_C2CC475F | 504990 | 570 | -102.7 | 504990 | 889 | -106.8 | 504990 | 57 | -114.9 | 504990 | 240 |
| MR_1774416393_49926C35 | 504990 | 570 | -100.9 | 504990 | 889 | -108.4 | 504990 | 57 | -115.2 | 504990 | 240 |
| MR_1774416393_8422A8D6 | 504990 | 570 | -101.3 | 504990 | 889 | -107.3 | 504990 | 57 | -115.0 | 504990 | 240 |
| MR_1774416393_629A5C4B | 504990 | 570 | -101.9 | 504990 | 889 | -107.2 | 504990 | 57 | -115.3 | 504990 | 240 |
| MR_1774416393_393F7308 | 504990 | 570 | -103.2 | 504990 | 889 | -107.2 | 504990 | 57 | -113.7 | 504990 | 240 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1185: `3bbaf7ad-b67...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3bbaf7ad-b67b-44ff-950b-8b47a63478e6` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3249293_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1185] topology](images/train_1185.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3275069_3 and 3217008_2
- `C2`: Press down the tilt angle  of 3217008_2 by 6 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249293_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217008_2
- `C5`: Increase A3 Offset threshold for 3249293_1
- `C6`: Press down the tilt angle of 3249293_1 by 5 degrees
- `C7`: Decrease A3 Offset threshold for 3249293_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217008_2
- `C9`: Increase transmission power for 3217008_2
- `C10`: Add neighbor relationship between 3249293_1 and 3217008_2
- `C11`: Decrease transmission power for 3217008_2
- `C12`: Check test server and transmission issues
- `C13`: Increase A3 Offset threshold for 3217008_2
- `C14`: Decrease A3 Offset threshold for 3217008_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249293_1 **← 정답**
- `C16`: Lift the tilt angle of 3249293_1 by 5 degrees
- `C17`: Adjust the azimuth of 3217008_2 by 50 degrees
- `C18`: Decrease transmission power for 3249293_1
- `C19`: Increase transmission power for 3249293_1
- `C20`: Lift the tilt angle  of 3217008_2 by 6 degrees
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Adjust the azimuth of 3249293_1 by 20 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.195 | MS1 | 121.4656703265 | 31.1446374622 | 584 | 504990 | -86.57 | 12.32 | 593.89 | 0.07 | 2.41 | 1589 |
| 2024-09-20 22:21:32.263 | MS1 | 121.4656779617 | 31.1446189259 | 584 | 504990 | -91.97 | 17.91 | 357.23 | 0.15 | 2.78 | 1596 |
| 2024-09-20 22:21:33.351 | MS1 | 121.4656694318 | 31.1446183466 | 584 | 504990 | -89.73 | 16.69 | 449.79 | 0.07 | 2.20 | 1593 |
| 2024-09-20 22:21:34.104 | MS1 | 121.4656588178 | 31.1446356925 | 584 | 504990 | -87.34 | 13.37 | 107.34 | 0.55 | 2.11 | 526 |
| 2024-09-20 22:21:35.932 | MS1 | 121.4656590647 | 31.1446288946 | 584 | 504990 | -90.83 | 13.73 | 99.51 | 0.70 | 2.33 | 665 |
| 2024-09-20 22:21:36.278 | MS1 | 121.4656709157 | 31.1446228770 | 584 | 504990 | -85.75 | 13.14 | 89.26 | 0.60 | 2.09 | 661 |
| 2024-09-20 22:21:37.946 | MS1 | 121.4656736279 | 31.1446243837 | 584 | 504990 | -90.39 | 9.93 | 73.76 | 0.58 | 2.53 | 535 |
| 2024-09-20 22:21:38.329 | MS1 | 121.4656604758 | 31.1446314642 | 584 | 504990 | -90.81 | 7.90 | 53.45 | 0.69 | 2.47 | 500 |
| 2024-09-20 22:21:39.195 | MS1 | 121.4656589681 | 31.1446350360 | 584 | 504990 | -90.07 | 8.52 | 89.66 | 0.64 | 2.06 | 673 |
| 2024-09-20 22:21:40.765 | MS1 | 121.4656720851 | 31.1446300157 | 584 | 504990 | -91.74 | 11.91 | 432.37 | 0.14 | 2.32 | 1572 |
| 2024-09-20 22:21:41.146 | MS1 | 121.4656600459 | 31.1446184320 | 584 | 504990 | -91.07 | 11.61 | 498.67 | 0.06 | 2.20 | 1589 |
| 2024-09-20 22:21:42.143 | MS1 | 121.4656670109 | 31.1446308257 | 584 | 504990 | -92.10 | 10.37 | 408.43 | 0.10 | 2.69 | 1574 |

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
| 3217008 | 2 | 121.4698691734 | 31.1552708982 | 15 | 5 | 5 | 23.3 | TDD | 704 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3217744 | 4 | 121.4700220858 | 31.1559845642 | 338 | 12 | 5 | 25.7 | TDD | 831 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3249293 | 1 | 121.4734737786 | 31.1531640267 | 198 | 3 | 0 | 48.5 | TDD | 584 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3275069 | 3 | 121.4668895997 | 31.1452232512 | 150 | 1 | 11 | 19.3 | TDD | 245 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.356 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.378 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.498 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.498 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.237 | NREventA3 | measId:2;ServCellPCI:878;Se... |
| 2024-09-20 22:21:38.477 | NRHandoverAttempt | SourcePCI:878;SourceNR-ARFC... |
| 2024-09-20 22:21:38.521 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.536 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.670 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.670 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249293 | 1 | 8.8064 | 19.1379 | -117.9020 | 16.3657 | 108.0595 | 0.0139 | 0.0029 |
| 2024_09_20 22:00 | 3217008 | 2 | 11.3801 | 17.3577 | -114.4422 | 15.3629 | 194.9801 | 0.0097 | 0.0121 |
| 2024_09_20 22:00 | 3275069 | 3 | 19.4317 | 13.7179 | -117.2979 | 5.6744 | 117.4250 | 0.0025 | 0.0182 |
| 2024_09_20 22:00 | 3217744 | 4 | 17.1725 | 15.5622 | -114.7849 | 19.9186 | 173.2962 | 0.0101 | 0.0106 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412663_F0DC4A00 | 504990 | 584 | -90.1 | 504990 | 704 | -97.6 | 504990 | 245 | -102.0 | 504990 | 831 |
| MR_1774412663_50FA7D40 | 504990 | 584 | -90.1 | 504990 | 704 | -99.1 | 504990 | 245 | -102.8 | 504990 | 831 |
| MR_1774412663_F0161DCA | 504990 | 584 | -89.9 | 504990 | 704 | -98.8 | 504990 | 245 | -104.2 | 504990 | 831 |
| MR_1774412663_6CCB6797 | 504990 | 584 | -90.9 | 504990 | 704 | -98.4 | 504990 | 245 | -101.8 | 504990 | 831 |
| MR_1774412663_9E5BD8CB | 504990 | 584 | -91.7 | 504990 | 704 | -96.7 | 504990 | 245 | -102.3 | 504990 | 831 |
| MR_1774412663_64311A6C | 504990 | 584 | -91.4 | 504990 | 704 | -95.6 | 504990 | 245 | -102.8 | 504990 | 831 |
| MR_1774412663_554A1153 | 504990 | 584 | -92.8 | 504990 | 704 | -95.5 | 504990 | 245 | -102.8 | 504990 | 831 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1186: `a8fe6f04-590...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a8fe6f04-590b-4f30-910e-c7ed77c3c4c2` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Decrease A3 Offset threshold for 3215528_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1186] topology](images/train_1186.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3215528_4 **← 정답**
- `C2`: Increase transmission power for 3215528_4
- `C3`: Press down the tilt angle  of 3279638_3 by 5 degrees
- `C4`: Add neighbor relationship between 3238677_2 and 3279638_3
- `C5`: Check test server and transmission issues
- `C6`: Adjust the azimuth of 3215528_4 by 35 degrees
- `C7`: Decrease transmission power for 3279638_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279638_3
- `C9`: Increase A3 Offset threshold for 3215528_4
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease A3 Offset threshold for 3279638_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215528_4
- `C13`: Decrease transmission power for 3215528_4
- `C14`: Press down the tilt angle of 3215528_4 by 10 degrees
- `C15`: Adjust the azimuth of 3279638_3 by 50 degrees
- `C16`: Lift the tilt angle  of 3279638_3 by 5 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215528_4
- `C18`: Increase transmission power for 3279638_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279638_3
- `C20`: Lift the tilt angle of 3215528_4 by 10 degrees
- `C21`: Increase A3 Offset threshold for 3279638_3
- `C22`: Add neighbor relationship between 3215528_4 and 3279638_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.995 | MS1 | 121.4656679207 | 31.1446203662 | 474 | 504990 | -75.21 | 16.11 | 431.65 | 0.12 | 2.25 | 1580 |
| 2024-09-20 22:21:32.863 | MS1 | 121.4656624910 | 31.1446334225 | 474 | 504990 | -75.42 | 13.51 | 588.33 | 0.09 | 2.18 | 1592 |
| 2024-09-20 22:21:33.956 | MS1 | 121.4656660043 | 31.1446299071 | 474 | 504990 | -82.17 | 14.12 | 516.57 | 0.03 | 2.76 | 1575 |
| 2024-09-20 22:21:34.606 | MS1 | 121.4656660893 | 31.1446320470 | 474 | 504990 | -91.71 | -1.09 | 70.76 | 0.12 | 1.21 | 1571 |
| 2024-09-20 22:21:35.876 | MS1 | 121.4656722525 | 31.1446209151 | 474 | 504990 | -83.20 | -1.39 | 64.36 | 0.09 | 1.09 | 1590 |
| 2024-09-20 22:21:36.282 | MS1 | 121.4656701174 | 31.1446222281 | 474 | 504990 | -86.56 | -2.27 | 49.85 | 0.05 | 1.27 | 1584 |
| 2024-09-20 22:21:37.911 | MS1 | 121.4656761021 | 31.1446258912 | 474 | 504990 | -92.20 | -1.41 | 43.49 | 0.01 | 1.50 | 1591 |
| 2024-09-20 22:21:38.274 | MS1 | 121.4656660835 | 31.1446349861 | 474 | 504990 | -87.55 | -0.10 | 63.80 | 0.17 | 1.01 | 1580 |
| 2024-09-20 22:21:39.139 | MS1 | 121.4656731698 | 31.1446250477 | 509 | 504990 | -75.35 | 15.21 | 191.59 | 0.14 | 1.40 | 1575 |
| 2024-09-20 22:21:40.400 | MS1 | 121.4656592412 | 31.1446212726 | 509 | 504990 | -76.20 | 16.16 | 330.86 | 0.06 | 2.97 | 1561 |
| 2024-09-20 22:21:41.850 | MS1 | 121.4656651574 | 31.1446225362 | 509 | 504990 | -84.74 | 12.00 | 480.09 | 0.19 | 2.45 | 1590 |
| 2024-09-20 22:21:42.627 | MS1 | 121.4656740228 | 31.1446181032 | 509 | 504990 | -77.83 | 15.12 | 323.65 | 0.15 | 2.87 | 1590 |

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
| 3215528 | 4 | 121.4728692563 | 31.1530155072 | 251 | 9 | 6 | 24.7 | TDD | 474 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3238677 | 2 | 121.4641687289 | 31.1454670591 | 163 | 9 | 4 | 28.1 | TDD | 690 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3277185 | 1 | 121.4673203494 | 31.1496576698 | 24 | 4 | 4 | 30.7 | TDD | 657 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3279638 | 3 | 121.4726087089 | 31.1465481324 | 127 | 3 | 4 | 25.0 | TDD | 509 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.929 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.954 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.091 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.091 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.792 | NREventA3 | measId:2;ServCellPCI:858;Se... |
| 2024-09-20 22:21:38.032 | NRHandoverAttempt | SourcePCI:858;SourceNR-ARFC... |
| 2024-09-20 22:21:38.069 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.083 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.204 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.204 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277185 | 1 | 16.0371 | 13.0279 | -116.6781 | 7.3356 | 94.5500 | 0.0019 | 0.0048 |
| 2024_09_20 22:00 | 3238677 | 2 | 15.3615 | 5.2441 | -116.4520 | 16.8523 | 122.3747 | 0.0010 | 0.0188 |
| 2024_09_20 22:00 | 3279638 | 3 | 13.6568 | 12.4147 | -117.0024 | 13.1971 | 167.5206 | 0.0123 | 0.0013 |
| 2024_09_20 22:00 | 3215528 | 4 | 16.1452 | 11.4679 | -116.2486 | 18.7942 | 144.3779 | 0.0087 | 0.1180 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412432_D99220E4 | 504990 | 509 | -85.5 | 504990 | 474 | -90.4 | 504990 | 690 | -95.8 | 504990 | 657 |
| MR_1774412432_DECDB9D6 | 504990 | 474 | -93.2 | 504990 | 509 | -86.0 | 504990 | 690 | -93.0 | 504990 | 657 |
| MR_1774412432_E582EA77 | 504990 | 474 | -91.1 | 504990 | 509 | -87.3 | 504990 | 690 | -93.7 | 504990 | 657 |
| MR_1774412432_3E7D8F7A | 504990 | 474 | -91.0 | 504990 | 509 | -85.4 | 504990 | 690 | -93.8 | 504990 | 657 |
| MR_1774412432_282B82D4 | 504990 | 509 | -85.1 | 504990 | 474 | -91.8 | 504990 | 690 | -93.7 | 504990 | 657 |
| MR_1774412432_B1DA4C82 | 504990 | 474 | -91.4 | 504990 | 509 | -87.5 | 504990 | 690 | -92.6 | 504990 | 657 |
| MR_1774412432_7ED5609D | 504990 | 474 | -91.6 | 504990 | 509 | -87.5 | 504990 | 690 | -93.3 | 504990 | 657 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1187: `01bdaa3c-41d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `01bdaa3c-41dc-4df3-ba59-92bda6c14389` |
| Tag | **multiple-answer** |
| 정답 | **C4|C19** |
| C4 의미 | Adjust the azimuth of 3251582_1 by 25 degrees |
| C19 의미 | Increase transmission power for 3251582_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1187] topology](images/train_1187.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3251582_1 by 7 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261097_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251582_1
- `C4`: Adjust the azimuth of 3251582_1 by 25 degrees **← 정답**
- `C5`: Decrease A3 Offset threshold for 3261097_2
- `C6`: Increase transmission power for 3261097_2
- `C7`: Adjust the azimuth of 3261097_2 by 21 degrees
- `C8`: Decrease transmission power for 3251582_1
- `C9`: Increase A3 Offset threshold for 3251582_1
- `C10`: Lift the tilt angle  of 3261097_2 by 3 degrees
- `C11`: Check test server and transmission issues
- `C12`: Increase A3 Offset threshold for 3261097_2
- `C13`: Add neighbor relationship between 3251582_1 and 3261097_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251582_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Lift the tilt angle of 3251582_1 by 7 degrees
- `C17`: Decrease A3 Offset threshold for 3251582_1
- `C18`: Add neighbor relationship between 3249898_3 and 3261097_2
- `C19`: Increase transmission power for 3251582_1 **← 정답**
- `C20`: Decrease transmission power for 3261097_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261097_2
- `C22`: Press down the tilt angle  of 3261097_2 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.969 | MS1 | 121.4656666029 | 31.1446354338 | 776 | 504990 | -90.61 | 13.76 | 535.62 | 0.04 | 2.92 | 1574 |
| 2024-09-20 22:21:32.790 | MS1 | 121.4656720560 | 31.1446272363 | 776 | 504990 | -93.22 | 14.36 | 483.03 | 0.01 | 2.87 | 1573 |
| 2024-09-20 22:21:33.387 | MS1 | 121.4656621749 | 31.1446322063 | 776 | 504990 | -85.15 | 16.14 | 500.11 | 0.15 | 2.47 | 1578 |
| 2024-09-20 22:21:34.465 | MS1 | 121.4656623088 | 31.1446324038 | 776 | 504990 | -108.60 | 0.98 | 61.01 | 0.01 | 1.17 | 1583 |
| 2024-09-20 22:21:35.366 | MS1 | 121.4656716813 | 31.1446330402 | 776 | 504990 | -105.98 | 1.18 | 39.12 | 0.07 | 1.15 | 1561 |
| 2024-09-20 22:21:36.554 | MS1 | 121.4656665665 | 31.1446283392 | 776 | 504990 | -109.84 | 1.22 | 39.33 | 0.15 | 1.49 | 1583 |
| 2024-09-20 22:21:37.955 | MS1 | 121.4656754879 | 31.1446335852 | 776 | 504990 | -105.33 | -1.79 | 55.22 | 0.10 | 1.45 | 1598 |
| 2024-09-20 22:21:38.791 | MS1 | 121.4656620625 | 31.1446378104 | 776 | 504990 | -100.49 | 0.17 | 48.62 | 0.16 | 1.26 | 1587 |
| 2024-09-20 22:21:39.518 | MS1 | 121.4656763447 | 31.1446357512 | 776 | 504990 | -106.41 | -1.37 | 61.64 | 0.08 | 1.44 | 1585 |
| 2024-09-20 22:21:40.817 | MS1 | 121.4656774196 | 31.1446327909 | 776 | 504990 | -92.02 | 12.62 | 458.31 | 0.04 | 2.71 | 1565 |
| 2024-09-20 22:21:41.500 | MS1 | 121.4656617269 | 31.1446323396 | 776 | 504990 | -89.61 | 13.35 | 467.79 | 0.13 | 2.20 | 1592 |
| 2024-09-20 22:21:42.139 | MS1 | 121.4656774426 | 31.1446363011 | 776 | 504990 | -92.28 | 13.42 | 590.76 | 0.04 | 2.40 | 1595 |

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
| 3249898 | 3 | 121.4733136862 | 31.1522520558 | 5 | 15 | 6 | 24.0 | TDD | 51 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3251582 | 1 | 121.4652378587 | 31.1535035802 | 153 | 6 | 11 | 15.0 | TDD | 776 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3255916 | 4 | 121.4687536519 | 31.1521380585 | 150 | 6 | 6 | 16.8 | TDD | 273 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3261097 | 2 | 121.4739678110 | 31.1513777714 | 247 | 1 | 6 | 32.9 | TDD | 577 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.630 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.757 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.757 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.942 | NREventA2 | measId:1;ServCellPCI:446;Se... |
| 2024-09-20 22:21:35.045 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251582 | 1 | 16.1622 | 19.9980 | -117.4730 | 6.8187 | 186.1223 | 0.1081 | 0.0009 |
| 2024_09_20 22:00 | 3261097 | 2 | 7.3792 | 9.3755 | -114.3948 | 16.1027 | 171.8976 | 0.0181 | 0.0100 |
| 2024_09_20 22:00 | 3249898 | 3 | 7.9657 | 6.8013 | -114.9963 | 5.3426 | 129.3562 | 0.0120 | 0.0182 |
| 2024_09_20 22:00 | 3255916 | 4 | 19.8281 | 17.4460 | -116.2017 | 15.1254 | 150.2277 | 0.0075 | 0.0168 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415234_6D24E261 | 504990 | 776 | -107.2 | 504990 | 577 | -112.8 | 504990 | 51 | -120.5 | 504990 | 273 |
| MR_1774415234_1869FE13 | 504990 | 776 | -109.4 | 504990 | 577 | -111.7 | 504990 | 51 | -119.9 | 504990 | 273 |
| MR_1774415234_90353150 | 504990 | 776 | -107.4 | 504990 | 577 | -112.8 | 504990 | 51 | -117.9 | 504990 | 273 |
| MR_1774415234_1C571295 | 504990 | 776 | -106.7 | 504990 | 577 | -111.6 | 504990 | 51 | -120.7 | 504990 | 273 |
| MR_1774415234_26A50653 | 504990 | 776 | -108.2 | 504990 | 577 | -111.7 | 504990 | 51 | -117.7 | 504990 | 273 |
| MR_1774415234_8DD54B47 | 504990 | 776 | -106.6 | 504990 | 577 | -112.3 | 504990 | 51 | -119.2 | 504990 | 273 |
| MR_1774415234_72B0BDB7 | 504990 | 776 | -109.7 | 504990 | 577 | -110.7 | 504990 | 51 | -120.1 | 504990 | 273 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1188: `30119bbd-a3f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `30119bbd-a3fa-4071-9136-fc4ce61c8897` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Lift the tilt angle  of 3262274_4 by 8 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1188] topology](images/train_1188.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3262274_4 by 19 degrees
- `C2`: Increase transmission power for 3211177_3
- `C3`: Press down the tilt angle of 3211177_3 by 3 degrees
- `C4`: Increase A3 Offset threshold for 3211177_3
- `C5`: Increase transmission power for 3213843_1
- `C6`: Add neighbor relationship between 3262274_4 and 3213843_1
- `C7`: Decrease transmission power for 3213843_1
- `C8`: Lift the tilt angle of 3211177_3 by 3 degrees
- `C9`: Press down the tilt angle  of 3262274_4 by 8 degrees
- `C10`: Decrease transmission power for 3211177_3
- `C11`: Lift the tilt angle  of 3262274_4 by 8 degrees **← 정답**
- `C12`: Add neighbor relationship between 3211177_3 and 3213843_1
- `C13`: Check test server and transmission issues
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213843_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211177_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213843_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211177_3
- `C18`: Increase A3 Offset threshold for 3213843_1
- `C19`: Adjust the azimuth of 3211177_3 by 2 degrees
- `C20`: Decrease A3 Offset threshold for 3213843_1
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease A3 Offset threshold for 3211177_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.914 | MS1 | 121.4656679669 | 31.1446368102 | 234 | 504990 | -88.06 | 17.39 | 546.26 | 0.17 | 2.76 | 1577 |
| 2024-09-20 22:21:32.676 | MS1 | 121.4656721506 | 31.1446180922 | 234 | 504990 | -90.70 | 14.81 | 560.24 | 0.09 | 2.64 | 1593 |
| 2024-09-20 22:21:33.955 | MS1 | 121.4656651979 | 31.1446233987 | 234 | 504990 | -91.39 | 12.40 | 553.14 | 0.10 | 2.80 | 1561 |
| 2024-09-20 22:21:34.131 | MS1 | 121.4656699503 | 31.1446208196 | 234 | 504990 | -91.46 | 13.47 | 80.61 | 0.14 | 2.75 | 1585 |
| 2024-09-20 22:21:35.872 | MS1 | 121.4656603391 | 31.1446347281 | 234 | 504990 | -88.43 | 13.25 | 89.37 | 0.03 | 2.22 | 1594 |
| 2024-09-20 22:21:36.183 | MS1 | 121.4656645277 | 31.1446347908 | 234 | 504990 | -85.17 | 14.55 | 45.27 | 0.06 | 2.96 | 1582 |
| 2024-09-20 22:21:37.562 | MS1 | 121.4656705821 | 31.1446306330 | 234 | 504990 | -93.63 | 12.33 | 50.52 | 0.07 | 2.30 | 1565 |
| 2024-09-20 22:21:38.616 | MS1 | 121.4656685639 | 31.1446261156 | 234 | 504990 | -92.08 | 12.41 | 73.05 | 0.01 | 2.40 | 1567 |
| 2024-09-20 22:21:39.739 | MS1 | 121.4656735642 | 31.1446324740 | 234 | 504990 | -92.51 | 9.94 | 77.14 | 0.01 | 2.41 | 1575 |
| 2024-09-20 22:21:40.991 | MS1 | 121.4656601311 | 31.1446232397 | 234 | 504990 | -92.69 | 11.59 | 293.25 | 0.07 | 2.94 | 1560 |
| 2024-09-20 22:21:41.711 | MS1 | 121.4656619430 | 31.1446269080 | 234 | 504990 | -92.62 | 7.69 | 398.41 | 0.02 | 2.69 | 1583 |
| 2024-09-20 22:21:42.521 | MS1 | 121.4656622980 | 31.1446201745 | 234 | 504990 | -91.83 | 7.72 | 363.09 | 0.19 | 2.74 | 1581 |

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
| 3211177 | 3 | 121.4701987085 | 31.1507955977 | 214 | 0 | 6 | 47.0 | TDD | 234 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3213843 | 1 | 121.4647631101 | 31.1509297347 | 192 | 6 | 7 | 20.3 | TDD | 200 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3255110 | 2 | 121.4643244447 | 31.1490070448 | 134 | 14 | 4 | 33.1 | TDD | 49 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3262274 | 4 | 121.4734010290 | 31.1490760000 | 24 | 1 | 0 | 35.8 | TDD | 859 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.549 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.568 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.669 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.669 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.448 | NREventA3 | measId:2;ServCellPCI:793;Se... |
| 2024-09-20 22:21:38.688 | NRHandoverAttempt | SourcePCI:793;SourceNR-ARFC... |
| 2024-09-20 22:21:38.720 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.731 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.859 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.859 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213843 | 1 | 5.8872 | 18.1784 | -117.9654 | 10.9503 | 108.5244 | 0.0105 | 0.0049 |
| 2024_09_20 22:00 | 3255110 | 2 | 18.9875 | 7.8097 | -117.5442 | 11.5349 | 146.5059 | 0.0145 | 0.0187 |
| 2024_09_20 22:00 | 3211177 | 3 | 77.8980 | 89.3407 | -115.4236 | 12.0180 | 125.0894 | 0.0080 | 0.0102 |
| 2024_09_20 22:00 | 3262274 | 4 | 11.7476 | 17.7726 | -117.6329 | 14.2162 | 113.1216 | 0.0043 | 0.0038 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412046_D3EE3C4E | 504990 | 234 | -90.0 | 504990 | 200 | -91.7 | 504990 | 859 | -98.8 | 504990 | 49 |
| MR_1774412046_2161E947 | 504990 | 234 | -89.9 | 504990 | 200 | -92.3 | 504990 | 859 | -99.3 | 504990 | 49 |
| MR_1774412046_CAF50471 | 504990 | 234 | -91.9 | 504990 | 200 | -90.7 | 504990 | 859 | -99.5 | 504990 | 49 |
| MR_1774412046_7772F342 | 504990 | 234 | -91.7 | 504990 | 200 | -92.7 | 504990 | 859 | -99.0 | 504990 | 49 |
| MR_1774412046_3CD42A2D | 504990 | 234 | -90.9 | 504990 | 200 | -93.4 | 504990 | 859 | -100.7 | 504990 | 49 |
| MR_1774412046_0F82CCB9 | 504990 | 234 | -92.9 | 504990 | 200 | -93.1 | 504990 | 859 | -101.5 | 504990 | 49 |
| MR_1774412046_98842B70 | 504990 | 234 | -92.4 | 504990 | 200 | -92.0 | 504990 | 859 | -101.2 | 504990 | 49 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1189: `e03cc3a5-57d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e03cc3a5-57dc-405c-b979-d12539338843` |
| Tag | **multiple-answer** |
| 정답 | **C9|C18** |
| C9 의미 | Adjust the azimuth of 3253135_2 by 50 degrees |
| C18 의미 | Increase transmission power for 3253135_2 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1189] topology](images/train_1189.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259264_3
- `C2`: Add neighbor relationship between 3253135_2 and 3259264_3
- `C3`: Increase A3 Offset threshold for 3253135_2
- `C4`: Lift the tilt angle  of 3259264_3 by 5 degrees
- `C5`: Decrease A3 Offset threshold for 3253135_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253135_2
- `C7`: Decrease transmission power for 3259264_3
- `C8`: Increase A3 Offset threshold for 3259264_3
- `C9`: Adjust the azimuth of 3253135_2 by 50 degrees **← 정답**
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259264_3
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Add neighbor relationship between 3211542_4 and 3259264_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253135_2
- `C14`: Adjust the azimuth of 3259264_3 by 24 degrees
- `C15`: Decrease A3 Offset threshold for 3259264_3
- `C16`: Increase transmission power for 3259264_3
- `C17`: Check test server and transmission issues
- `C18`: Increase transmission power for 3253135_2 **← 정답**
- `C19`: Decrease transmission power for 3253135_2
- `C20`: Press down the tilt angle of 3253135_2 by 7 degrees
- `C21`: Press down the tilt angle  of 3259264_3 by 5 degrees
- `C22`: Lift the tilt angle of 3253135_2 by 7 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.305 | MS1 | 121.4656638901 | 31.1446308808 | 167 | 504990 | -88.84 | 13.27 | 474.22 | 0.01 | 2.38 | 1585 |
| 2024-09-20 22:21:32.512 | MS1 | 121.4656752827 | 31.1446247870 | 167 | 504990 | -88.49 | 14.53 | 513.42 | 0.08 | 2.27 | 1570 |
| 2024-09-20 22:21:33.692 | MS1 | 121.4656585380 | 31.1446201227 | 167 | 504990 | -86.35 | 16.54 | 419.68 | 0.15 | 2.40 | 1584 |
| 2024-09-20 22:21:34.927 | MS1 | 121.4656616975 | 31.1446181117 | 167 | 504990 | -106.09 | 1.91 | 52.65 | 0.10 | 1.37 | 1560 |
| 2024-09-20 22:21:35.968 | MS1 | 121.4656765136 | 31.1446337007 | 167 | 504990 | -106.17 | 1.16 | 34.15 | 0.13 | 1.07 | 1575 |
| 2024-09-20 22:21:36.741 | MS1 | 121.4656747839 | 31.1446213453 | 167 | 504990 | -104.76 | 1.50 | 46.74 | 0.15 | 1.07 | 1575 |
| 2024-09-20 22:21:37.868 | MS1 | 121.4656733597 | 31.1446273469 | 167 | 504990 | -108.72 | -1.66 | 30.67 | 0.19 | 1.24 | 1567 |
| 2024-09-20 22:21:38.592 | MS1 | 121.4656634635 | 31.1446319438 | 167 | 504990 | -106.28 | 0.77 | 41.43 | 0.07 | 1.50 | 1592 |
| 2024-09-20 22:21:39.554 | MS1 | 121.4656587089 | 31.1446379900 | 167 | 504990 | -106.49 | -1.82 | 35.91 | 0.03 | 1.09 | 1564 |
| 2024-09-20 22:21:40.854 | MS1 | 121.4656648494 | 31.1446278368 | 167 | 504990 | -89.85 | 16.40 | 425.14 | 0.09 | 2.30 | 1562 |
| 2024-09-20 22:21:41.685 | MS1 | 121.4656753314 | 31.1446195323 | 167 | 504990 | -94.43 | 13.18 | 319.97 | 0.06 | 2.26 | 1583 |
| 2024-09-20 22:21:42.896 | MS1 | 121.4656607841 | 31.1446325704 | 167 | 504990 | -85.39 | 14.63 | 379.26 | 0.07 | 2.72 | 1591 |

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
| 3211542 | 4 | 121.4751243912 | 31.1556982581 | 303 | 4 | 5 | 24.8 | TDD | 791 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3244385 | 1 | 121.4689763264 | 31.1449899246 | 277 | 1 | 11 | 46.9 | TDD | 704 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3253135 | 2 | 121.4664670180 | 31.1510858965 | 120 | 5 | 7 | 21.5 | TDD | 167 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3259264 | 3 | 121.4730997229 | 31.1474136685 | 270 | 3 | 9 | 23.9 | TDD | 850 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.961 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.984 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.117 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.117 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.337 | NREventA2 | measId:1;ServCellPCI:922;Se... |
| 2024-09-20 22:21:34.475 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244385 | 1 | 18.2421 | 13.3888 | -116.7290 | 17.8231 | 128.7106 | 0.0015 | 0.0088 |
| 2024_09_20 22:00 | 3253135 | 2 | 12.9458 | 8.6646 | -117.3412 | 6.0490 | 127.7953 | 0.1127 | 0.0194 |
| 2024_09_20 22:00 | 3259264 | 3 | 15.6579 | 7.7391 | -117.6484 | 10.8726 | 184.1158 | 0.0089 | 0.0082 |
| 2024_09_20 22:00 | 3211542 | 4 | 6.3042 | 6.8836 | -114.3931 | 19.1328 | 154.7869 | 0.0132 | 0.0072 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412570_675FB58A | 504990 | 167 | -105.2 | 504990 | 850 | -112.1 | 504990 | 791 | -115.0 | 504990 | 704 |
| MR_1774412570_F9C985AA | 504990 | 167 | -105.0 | 504990 | 850 | -112.2 | 504990 | 791 | -117.7 | 504990 | 704 |
| MR_1774412570_0A013A89 | 504990 | 167 | -105.6 | 504990 | 850 | -112.5 | 504990 | 791 | -115.6 | 504990 | 704 |
| MR_1774412570_B2D0BC19 | 504990 | 167 | -106.6 | 504990 | 850 | -113.9 | 504990 | 791 | -116.5 | 504990 | 704 |
| MR_1774412570_571C3125 | 504990 | 167 | -105.0 | 504990 | 850 | -113.5 | 504990 | 791 | -117.2 | 504990 | 704 |

> *... 2개 열 생략 (전체 14열)*

---
