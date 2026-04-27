# Track A 문제 분석 — train[80]~train[89]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[80] ~ train[89] (10개)

## 목차

1. [문제 80: `9814b880-3d7...`](#80) — single-answer, 정답: C16
2. [문제 81: `e66afb91-c05...`](#81) — single-answer, 정답: C15
3. [문제 82: `f54b2b10-54b...`](#82) — single-answer, 정답: C8
4. [문제 83: `c3eae2e6-b45...`](#83) — single-answer, 정답: C14
5. [문제 84: `d895057e-6d5...`](#84) — single-answer, 정답: C4
6. [문제 85: `aed8cf54-663...`](#85) — single-answer, 정답: C19
7. [문제 86: `da2c4b4f-26f...`](#86) — single-answer, 정답: C16
8. [문제 87: `c8fcac06-39e...`](#87) — single-answer, 정답: C10
9. [문제 88: `0bbfd745-b28...`](#88) — single-answer, 정답: C18
10. [문제 89: `ebfe7bd4-5ad...`](#89) — single-answer, 정답: C15

---

### 문제 80: `9814b880-3d7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9814b880-3d7a-4ef6-9365-98d612fedde2` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Lift the tilt angle  of 3220352_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[80] topology](images/train_0080.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3220352_2 by 50 degrees
- `C2`: Increase transmission power for 3259449_4
- `C3`: Check test server and transmission issues
- `C4`: Lift the tilt angle of 3259449_4 by 1 degrees
- `C5`: Press down the tilt angle of 3259449_4 by 1 degrees
- `C6`: Decrease transmission power for 3259449_4
- `C7`: Increase A3 Offset threshold for 3259449_4
- `C8`: Add neighbor relationship between 3220352_2 and 3259736_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259449_4
- `C10`: Press down the tilt angle  of 3220352_2 by 10 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259449_4
- `C12`: Add neighbor relationship between 3259449_4 and 3259736_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259736_1
- `C14`: Decrease A3 Offset threshold for 3259736_1
- `C15`: Decrease transmission power for 3259736_1
- `C16`: Lift the tilt angle  of 3220352_2 by 10 degrees **← 정답**
- `C17`: Increase transmission power for 3259736_1
- `C18`: Adjust the azimuth of 3259449_4 by 6 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease A3 Offset threshold for 3259449_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259736_1
- `C22`: Increase A3 Offset threshold for 3259736_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.199 | MS1 | 121.4656609033 | 31.1446187403 | 172 | 504990 | -85.73 | 17.91 | 333.95 | 0.06 | 2.54 | 1590 |
| 2024-09-20 22:21:32.535 | MS1 | 121.4656617209 | 31.1446343620 | 172 | 504990 | -90.15 | 13.26 | 483.57 | 0.15 | 2.08 | 1574 |
| 2024-09-20 22:21:33.744 | MS1 | 121.4656744603 | 31.1446249577 | 172 | 504990 | -90.40 | 17.65 | 547.36 | 0.10 | 2.26 | 1598 |
| 2024-09-20 22:21:34.580 | MS1 | 121.4656756983 | 31.1446287166 | 172 | 504990 | -85.08 | 15.73 | 78.79 | 0.04 | 2.11 | 1579 |
| 2024-09-20 22:21:35.353 | MS1 | 121.4656675172 | 31.1446344375 | 172 | 504990 | -86.72 | 12.93 | 85.06 | 0.15 | 2.02 | 1579 |
| 2024-09-20 22:21:36.906 | MS1 | 121.4656667318 | 31.1446275451 | 172 | 504990 | -90.55 | 15.38 | 101.15 | 0.07 | 2.64 | 1574 |
| 2024-09-20 22:21:37.473 | MS1 | 121.4656722562 | 31.1446199580 | 172 | 504990 | -89.59 | 8.43 | 61.26 | 0.02 | 2.74 | 1595 |
| 2024-09-20 22:21:38.834 | MS1 | 121.4656600529 | 31.1446182512 | 172 | 504990 | -90.62 | 8.56 | 63.91 | 0.18 | 2.21 | 1567 |
| 2024-09-20 22:21:39.995 | MS1 | 121.4656726405 | 31.1446324953 | 172 | 504990 | -92.18 | 7.70 | 66.64 | 0.17 | 2.39 | 1590 |
| 2024-09-20 22:21:40.154 | MS1 | 121.4656719438 | 31.1446184363 | 172 | 504990 | -93.69 | 11.98 | 465.32 | 0.07 | 2.95 | 1568 |
| 2024-09-20 22:21:41.387 | MS1 | 121.4656604403 | 31.1446356668 | 172 | 504990 | -93.01 | 7.19 | 469.83 | 0.17 | 2.80 | 1600 |
| 2024-09-20 22:21:42.981 | MS1 | 121.4656672561 | 31.1446340238 | 172 | 504990 | -93.07 | 10.83 | 582.28 | 0.07 | 2.44 | 1586 |

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
| 3220352 | 2 | 121.4698928776 | 31.1541042381 | 38 | 9 | 10 | 20.4 | TDD | 579 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3234785 | 3 | 121.4672425089 | 31.1540118376 | 122 | 11 | 7 | 24.9 | TDD | 83 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3259449 | 4 | 121.4734528277 | 31.1514184919 | 230 | 0 | 10 | 18.3 | TDD | 172 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3259736 | 1 | 121.4756818156 | 31.1557704570 | 64 | 12 | 12 | 48.8 | TDD | 616 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.241 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.256 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.367 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.367 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.079 | NREventA3 | measId:2;ServCellPCI:680;Se... |
| 2024-09-20 22:21:38.319 | NRHandoverAttempt | SourcePCI:680;SourceNR-ARFC... |
| 2024-09-20 22:21:38.352 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.363 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.488 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.488 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259736 | 1 | 8.3370 | 19.5319 | -116.1486 | 13.8059 | 157.7249 | 0.0052 | 0.0085 |
| 2024_09_20 22:00 | 3220352 | 2 | 6.2133 | 15.2489 | -116.9729 | 18.6448 | 107.2553 | 0.0059 | 0.0181 |
| 2024_09_20 22:00 | 3234785 | 3 | 18.3449 | 12.4675 | -115.9611 | 18.1044 | 141.2453 | 0.0001 | 0.0096 |
| 2024_09_20 22:00 | 3259449 | 4 | 79.3409 | 77.3914 | -116.5848 | 9.6486 | 171.6439 | 0.0155 | 0.0182 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417168_9CBF008F | 504990 | 172 | -87.1 | 504990 | 616 | -84.5 | 504990 | 579 | -98.0 | 504990 | 83 |
| MR_1774417168_E0CB275E | 504990 | 172 | -83.4 | 504990 | 616 | -84.2 | 504990 | 579 | -98.4 | 504990 | 83 |
| MR_1774417168_FF4915DB | 504990 | 172 | -85.9 | 504990 | 616 | -86.4 | 504990 | 579 | -99.0 | 504990 | 83 |
| MR_1774417168_65691439 | 504990 | 172 | -84.6 | 504990 | 616 | -83.8 | 504990 | 579 | -97.9 | 504990 | 83 |
| MR_1774417168_90F491BD | 504990 | 172 | -83.5 | 504990 | 616 | -83.6 | 504990 | 579 | -96.6 | 504990 | 83 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 81: `e66afb91-c05...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e66afb91-c051-4871-86bb-7cca3a9e72b5` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease A3 Offset threshold for 3220587_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[81] topology](images/train_0081.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3232409_1
- `C2`: Decrease transmission power for 3220587_3
- `C3`: Press down the tilt angle of 3220587_3 by 10 degrees
- `C4`: Increase transmission power for 3232409_1
- `C5`: Press down the tilt angle  of 3232409_1 by 10 degrees
- `C6`: Add neighbor relationship between 3260567_4 and 3232409_1
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease A3 Offset threshold for 3232409_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220587_3
- `C10`: Adjust the azimuth of 3232409_1 by 50 degrees
- `C11`: Add neighbor relationship between 3220587_3 and 3232409_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232409_1
- `C13`: Increase A3 Offset threshold for 3220587_3
- `C14`: Lift the tilt angle of 3220587_3 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3220587_3 **← 정답**
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232409_1
- `C17`: Lift the tilt angle  of 3232409_1 by 10 degrees
- `C18`: Adjust the azimuth of 3220587_3 by 50 degrees
- `C19`: Increase transmission power for 3220587_3
- `C20`: Check test server and transmission issues
- `C21`: Decrease transmission power for 3232409_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220587_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.537 | MS1 | 121.4656709103 | 31.1446324380 | 221 | 504990 | -84.00 | 17.74 | 374.76 | 0.03 | 2.82 | 1595 |
| 2024-09-20 22:21:32.110 | MS1 | 121.4656643972 | 31.1446233561 | 221 | 504990 | -77.29 | 12.03 | 405.93 | 0.05 | 2.94 | 1566 |
| 2024-09-20 22:21:33.188 | MS1 | 121.4656710469 | 31.1446358907 | 221 | 504990 | -81.47 | 17.99 | 421.39 | 0.12 | 2.11 | 1568 |
| 2024-09-20 22:21:34.119 | MS1 | 121.4656643929 | 31.1446361321 | 221 | 504990 | -90.77 | -3.58 | 70.87 | 0.04 | 1.31 | 1572 |
| 2024-09-20 22:21:35.262 | MS1 | 121.4656675179 | 31.1446209387 | 221 | 504990 | -88.40 | -0.78 | 42.88 | 0.11 | 1.44 | 1562 |
| 2024-09-20 22:21:36.199 | MS1 | 121.4656624485 | 31.1446374530 | 221 | 504990 | -89.78 | -2.00 | 58.79 | 0.09 | 1.17 | 1560 |
| 2024-09-20 22:21:37.906 | MS1 | 121.4656742579 | 31.1446247589 | 221 | 504990 | -88.88 | -0.15 | 46.93 | 0.08 | 1.09 | 1597 |
| 2024-09-20 22:21:38.407 | MS1 | 121.4656647903 | 31.1446228485 | 221 | 504990 | -91.88 | -0.19 | 48.09 | 0.01 | 1.48 | 1570 |
| 2024-09-20 22:21:39.147 | MS1 | 121.4656655370 | 31.1446283139 | 633 | 504990 | -84.25 | 14.29 | 272.24 | 0.18 | 1.27 | 1585 |
| 2024-09-20 22:21:40.680 | MS1 | 121.4656688609 | 31.1446352495 | 633 | 504990 | -78.74 | 17.37 | 507.20 | 0.16 | 2.14 | 1561 |
| 2024-09-20 22:21:41.928 | MS1 | 121.4656667283 | 31.1446180619 | 633 | 504990 | -84.36 | 12.82 | 451.69 | 0.14 | 2.36 | 1585 |
| 2024-09-20 22:21:42.551 | MS1 | 121.4656615662 | 31.1446226660 | 633 | 504990 | -80.62 | 17.51 | 398.13 | 0.16 | 2.47 | 1560 |

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
| 3220587 | 3 | 121.4687453055 | 31.1480294189 | 90 | 6 | 3 | 48.3 | TDD | 221 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3232409 | 1 | 121.4646298756 | 31.1525886364 | 344 | 7 | 2 | 49.5 | TDD | 633 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3260567 | 4 | 121.4712529537 | 31.1551236006 | 70 | 15 | 5 | 26.2 | TDD | 429 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3263724 | 2 | 121.4720094991 | 31.1470432866 | 158 | 1 | 7 | 21.3 | TDD | 500 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.422 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.439 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.580 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.580 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.224 | NREventA3 | measId:2;ServCellPCI:837;Se... |
| 2024-09-20 22:21:38.464 | NRHandoverAttempt | SourcePCI:837;SourceNR-ARFC... |
| 2024-09-20 22:21:38.501 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.513 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.663 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.663 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232409 | 1 | 12.4363 | 18.9497 | -116.5081 | 6.7575 | 112.1082 | 0.0005 | 0.0052 |
| 2024_09_20 22:00 | 3263724 | 2 | 18.6129 | 6.1935 | -117.7313 | 7.9591 | 159.7671 | 0.0094 | 0.0102 |
| 2024_09_20 22:00 | 3220587 | 3 | 19.7766 | 16.9133 | -116.9400 | 11.6823 | 130.5622 | 0.0100 | 0.1890 |
| 2024_09_20 22:00 | 3260567 | 4 | 14.0161 | 17.2048 | -114.2249 | 14.9334 | 194.1551 | 0.0180 | 0.0126 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415770_6E7F6752 | 504990 | 221 | -90.3 | 504990 | 633 | -83.6 | 504990 | 429 | -85.7 | 504990 | 500 |
| MR_1774415770_9B551ECB | 504990 | 221 | -92.6 | 504990 | 633 | -82.2 | 504990 | 429 | -85.1 | 504990 | 500 |
| MR_1774415770_922156E1 | 504990 | 221 | -89.2 | 504990 | 633 | -84.4 | 504990 | 429 | -86.1 | 504990 | 500 |
| MR_1774415770_A8C35BFE | 504990 | 221 | -91.9 | 504990 | 633 | -83.9 | 504990 | 429 | -85.5 | 504990 | 500 |
| MR_1774415770_482B296D | 504990 | 221 | -89.7 | 504990 | 633 | -81.9 | 504990 | 429 | -84.4 | 504990 | 500 |
| MR_1774415770_21819F60 | 504990 | 633 | -85.4 | 504990 | 221 | -92.6 | 504990 | 429 | -85.1 | 504990 | 500 |
| MR_1774415770_D6BADE07 | 504990 | 221 | -92.3 | 504990 | 633 | -83.1 | 504990 | 429 | -87.6 | 504990 | 500 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 82: `f54b2b10-54b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f54b2b10-54b4-46f9-8988-44bb73789b99` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3269581_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[82] topology](images/train_0082.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269581_3
- `C2`: Increase A3 Offset threshold for 3269581_3
- `C3`: Lift the tilt angle of 3269581_3 by 5 degrees
- `C4`: Decrease A3 Offset threshold for 3269581_3
- `C5`: Increase transmission power for 3237388_1
- `C6`: Increase transmission power for 3269581_3
- `C7`: Add neighbor relationship between 3269581_3 and 3237388_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269581_3 **← 정답**
- `C9`: Press down the tilt angle of 3269581_3 by 5 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237388_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237388_1
- `C12`: Press down the tilt angle  of 3237388_1 by 10 degrees
- `C13`: Adjust the azimuth of 3237388_1 by 50 degrees
- `C14`: Add neighbor relationship between 3216520_2 and 3237388_1
- `C15`: Decrease transmission power for 3237388_1
- `C16`: Decrease transmission power for 3269581_3
- `C17`: Adjust the azimuth of 3269581_3 by 41 degrees
- `C18`: Check test server and transmission issues
- `C19`: Lift the tilt angle  of 3237388_1 by 10 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease A3 Offset threshold for 3237388_1
- `C22`: Increase A3 Offset threshold for 3237388_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.163 | MS1 | 121.4656664616 | 31.1446296906 | 397 | 504990 | -86.94 | 15.67 | 487.27 | 0.16 | 2.19 | 1593 |
| 2024-09-20 22:21:32.278 | MS1 | 121.4656702768 | 31.1446198394 | 397 | 504990 | -89.74 | 13.20 | 426.19 | 0.05 | 2.51 | 1578 |
| 2024-09-20 22:21:33.710 | MS1 | 121.4656612865 | 31.1446235270 | 397 | 504990 | -86.64 | 14.55 | 495.01 | 0.12 | 2.20 | 1575 |
| 2024-09-20 22:21:34.193 | MS1 | 121.4656690296 | 31.1446197668 | 397 | 504990 | -91.01 | 17.75 | 82.34 | 0.51 | 2.76 | 619 |
| 2024-09-20 22:21:35.431 | MS1 | 121.4656585870 | 31.1446258649 | 397 | 504990 | -88.02 | 17.99 | 87.72 | 0.65 | 2.23 | 651 |
| 2024-09-20 22:21:36.770 | MS1 | 121.4656603133 | 31.1446260863 | 397 | 504990 | -91.83 | 12.25 | 76.20 | 0.70 | 2.33 | 589 |
| 2024-09-20 22:21:37.181 | MS1 | 121.4656692569 | 31.1446202101 | 397 | 504990 | -91.01 | 9.49 | 78.31 | 0.66 | 2.05 | 642 |
| 2024-09-20 22:21:38.595 | MS1 | 121.4656665666 | 31.1446202730 | 397 | 504990 | -90.89 | 10.85 | 54.29 | 0.61 | 2.81 | 676 |
| 2024-09-20 22:21:39.418 | MS1 | 121.4656648069 | 31.1446333678 | 397 | 504990 | -92.30 | 9.48 | 85.46 | 0.58 | 2.05 | 611 |
| 2024-09-20 22:21:40.194 | MS1 | 121.4656768889 | 31.1446195382 | 397 | 504990 | -92.16 | 10.33 | 557.51 | 0.00 | 2.54 | 1571 |
| 2024-09-20 22:21:41.447 | MS1 | 121.4656735119 | 31.1446283220 | 397 | 504990 | -92.82 | 11.73 | 518.60 | 0.02 | 2.03 | 1592 |
| 2024-09-20 22:21:42.955 | MS1 | 121.4656768579 | 31.1446258549 | 397 | 504990 | -89.21 | 9.28 | 394.45 | 0.09 | 2.24 | 1566 |

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
| 3216520 | 2 | 121.4754470288 | 31.1445021308 | 144 | 13 | 5 | 26.6 | TDD | 158 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3222977 | 4 | 121.4704638980 | 31.1527230438 | 9 | 5 | 6 | 27.7 | TDD | 438 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3237388 | 1 | 121.4696050738 | 31.1502891881 | 48 | 11 | 11 | 44.0 | TDD | 746 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3269581 | 3 | 121.4749988460 | 31.1517694367 | 187 | 3 | 11 | 44.6 | TDD | 397 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.011 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.032 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.133 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.133 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.849 | NREventA3 | measId:2;ServCellPCI:735;Se... |
| 2024-09-20 22:21:38.089 | NRHandoverAttempt | SourcePCI:735;SourceNR-ARFC... |
| 2024-09-20 22:21:38.136 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.151 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.290 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.290 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237388 | 1 | 14.2783 | 18.0681 | -115.0682 | 18.3914 | 140.2998 | 0.0192 | 0.0188 |
| 2024_09_20 22:00 | 3216520 | 2 | 14.2035 | 16.8947 | -117.5366 | 15.4760 | 124.4633 | 0.0155 | 0.0069 |
| 2024_09_20 22:00 | 3269581 | 3 | 9.1564 | 7.0059 | -116.8481 | 18.8573 | 145.6788 | 0.0120 | 0.0092 |
| 2024_09_20 22:00 | 3222977 | 4 | 15.7573 | 9.9842 | -114.1524 | 11.7982 | 150.3114 | 0.0122 | 0.0160 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416098_48A14674 | 504990 | 397 | -89.8 | 504990 | 746 | -89.0 | 504990 | 158 | -104.9 | 504990 | 438 |
| MR_1774416098_C64C5705 | 504990 | 397 | -89.9 | 504990 | 746 | -89.6 | 504990 | 158 | -104.6 | 504990 | 438 |
| MR_1774416098_48871CD5 | 504990 | 397 | -89.4 | 504990 | 746 | -91.8 | 504990 | 158 | -105.6 | 504990 | 438 |
| MR_1774416098_CE1D1199 | 504990 | 397 | -90.3 | 504990 | 746 | -89.7 | 504990 | 158 | -104.9 | 504990 | 438 |
| MR_1774416098_88B10820 | 504990 | 397 | -90.4 | 504990 | 746 | -89.9 | 504990 | 158 | -105.7 | 504990 | 438 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 83: `c3eae2e6-b45...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c3eae2e6-b45e-476a-8305-246ed918d608` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3210536_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[83] topology](images/train_0083.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3210536_3
- `C2`: Increase transmission power for 3210536_3
- `C3`: Press down the tilt angle of 3210536_3 by 5 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210536_3
- `C5`: Press down the tilt angle  of 3253891_1 by 10 degrees
- `C6`: Check test server and transmission issues
- `C7`: Add neighbor relationship between 3230748_4 and 3253891_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Adjust the azimuth of 3253891_1 by 17 degrees
- `C10`: Increase A3 Offset threshold for 3253891_1
- `C11`: Add neighbor relationship between 3210536_3 and 3253891_1
- `C12`: Adjust the azimuth of 3210536_3 by 46 degrees
- `C13`: Lift the tilt angle  of 3253891_1 by 10 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210536_3 **← 정답**
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253891_1
- `C16`: Decrease A3 Offset threshold for 3210536_3
- `C17`: Decrease A3 Offset threshold for 3253891_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253891_1
- `C19`: Decrease transmission power for 3253891_1
- `C20`: Increase transmission power for 3253891_1
- `C21`: Lift the tilt angle of 3210536_3 by 5 degrees
- `C22`: Increase A3 Offset threshold for 3210536_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.460 | MS1 | 121.4656733503 | 31.1446266157 | 908 | 504990 | -86.90 | 15.52 | 315.60 | 0.18 | 2.15 | 1577 |
| 2024-09-20 22:21:32.548 | MS1 | 121.4656633399 | 31.1446251026 | 908 | 504990 | -86.07 | 17.02 | 309.86 | 0.06 | 2.49 | 1593 |
| 2024-09-20 22:21:33.202 | MS1 | 121.4656648924 | 31.1446292247 | 908 | 504990 | -89.15 | 16.33 | 432.61 | 0.00 | 2.30 | 1592 |
| 2024-09-20 22:21:34.523 | MS1 | 121.4656718398 | 31.1446366234 | 908 | 504990 | -88.47 | 16.84 | 76.81 | 0.67 | 2.32 | 514 |
| 2024-09-20 22:21:35.735 | MS1 | 121.4656676284 | 31.1446333167 | 908 | 504990 | -86.77 | 14.77 | 57.11 | 0.61 | 2.55 | 564 |
| 2024-09-20 22:21:36.472 | MS1 | 121.4656649630 | 31.1446224832 | 908 | 504990 | -90.56 | 14.91 | 60.64 | 0.70 | 2.68 | 614 |
| 2024-09-20 22:21:37.608 | MS1 | 121.4656697675 | 31.1446182992 | 908 | 504990 | -93.04 | 12.86 | 50.31 | 0.63 | 2.32 | 604 |
| 2024-09-20 22:21:38.368 | MS1 | 121.4656675996 | 31.1446344524 | 908 | 504990 | -89.48 | 11.10 | 78.33 | 0.68 | 2.31 | 575 |
| 2024-09-20 22:21:39.773 | MS1 | 121.4656587219 | 31.1446228675 | 908 | 504990 | -92.62 | 11.38 | 67.03 | 0.67 | 2.97 | 647 |
| 2024-09-20 22:21:40.186 | MS1 | 121.4656621189 | 31.1446247668 | 908 | 504990 | -92.15 | 7.96 | 439.85 | 0.19 | 2.70 | 1560 |
| 2024-09-20 22:21:41.626 | MS1 | 121.4656631754 | 31.1446372747 | 908 | 504990 | -91.20 | 12.03 | 364.48 | 0.19 | 2.15 | 1570 |
| 2024-09-20 22:21:42.443 | MS1 | 121.4656648243 | 31.1446253060 | 908 | 504990 | -89.51 | 8.77 | 573.29 | 0.15 | 2.42 | 1588 |

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
| 3210536 | 3 | 121.4648823076 | 31.1556724831 | 131 | 4 | 1 | 25.5 | TDD | 908 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3230748 | 4 | 121.4657303612 | 31.1472528621 | 159 | 10 | 8 | 20.7 | TDD | 854 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3238236 | 2 | 121.4682275592 | 31.1483367118 | 87 | 1 | 8 | 41.8 | TDD | 251 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3253891 | 1 | 121.4723197505 | 31.1479259302 | 257 | 10 | 4 | 21.3 | TDD | 368 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.570 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.586 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.695 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.695 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.379 | NREventA3 | measId:2;ServCellPCI:406;Se... |
| 2024-09-20 22:21:38.619 | NRHandoverAttempt | SourcePCI:406;SourceNR-ARFC... |
| 2024-09-20 22:21:38.657 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.668 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.777 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.777 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253891 | 1 | 14.4051 | 5.7540 | -114.4015 | 5.5899 | 134.0939 | 0.0196 | 0.0006 |
| 2024_09_20 22:00 | 3238236 | 2 | 16.4186 | 8.0026 | -116.6998 | 8.7103 | 141.1885 | 0.0021 | 0.0109 |
| 2024_09_20 22:00 | 3210536 | 3 | 13.4716 | 17.0779 | -114.5342 | 15.9233 | 109.6860 | 0.0152 | 0.0046 |
| 2024_09_20 22:00 | 3230748 | 4 | 9.4769 | 6.0872 | -116.1216 | 14.4801 | 110.8224 | 0.0171 | 0.0186 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413114_5342A74F | 504990 | 908 | -89.6 | 504990 | 368 | -88.9 | 504990 | 854 | -100.2 | 504990 | 251 |
| MR_1774413114_AF3ADBB5 | 504990 | 908 | -88.1 | 504990 | 368 | -91.5 | 504990 | 854 | -100.1 | 504990 | 251 |
| MR_1774413114_6716477C | 504990 | 908 | -90.3 | 504990 | 368 | -88.6 | 504990 | 854 | -101.5 | 504990 | 251 |
| MR_1774413114_52ACA454 | 504990 | 908 | -88.3 | 504990 | 368 | -90.3 | 504990 | 854 | -102.2 | 504990 | 251 |
| MR_1774413114_20E20703 | 504990 | 908 | -89.7 | 504990 | 368 | -89.2 | 504990 | 854 | -101.6 | 504990 | 251 |
| MR_1774413114_CB77AB4E | 504990 | 908 | -86.9 | 504990 | 368 | -89.2 | 504990 | 854 | -101.8 | 504990 | 251 |
| MR_1774413114_65331B00 | 504990 | 908 | -88.5 | 504990 | 368 | -91.0 | 504990 | 854 | -102.0 | 504990 | 251 |
| MR_1774413114_2EF71585 | 504990 | 908 | -88.1 | 504990 | 368 | -89.0 | 504990 | 854 | -99.2 | 504990 | 251 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 84: `d895057e-6d5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d895057e-6d55-488a-89a3-d4de9a9b0e9b` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Lift the tilt angle  of 3216183_3 by 9 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[84] topology](images/train_0084.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3262475_1
- `C2`: Increase transmission power for 3262475_1
- `C3`: Add neighbor relationship between 3251288_4 and 3262475_1
- `C4`: Lift the tilt angle  of 3216183_3 by 9 degrees **← 정답**
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251288_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262475_1
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease A3 Offset threshold for 3251288_4
- `C9`: Increase A3 Offset threshold for 3251288_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251288_4
- `C11`: Lift the tilt angle of 3251288_4 by 3 degrees
- `C12`: Decrease A3 Offset threshold for 3262475_1
- `C13`: Increase transmission power for 3251288_4
- `C14`: Adjust the azimuth of 3216183_3 by 50 degrees
- `C15`: Press down the tilt angle of 3251288_4 by 3 degrees
- `C16`: Adjust the azimuth of 3251288_4 by 21 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262475_1
- `C18`: Decrease transmission power for 3251288_4
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle  of 3216183_3 by 9 degrees
- `C21`: Add neighbor relationship between 3216183_3 and 3262475_1
- `C22`: Increase A3 Offset threshold for 3262475_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.729 | MS1 | 121.4656759635 | 31.1446251968 | 14 | 504990 | -88.16 | 12.15 | 373.46 | 0.19 | 2.25 | 1595 |
| 2024-09-20 22:21:32.187 | MS1 | 121.4656641336 | 31.1446196162 | 14 | 504990 | -89.52 | 12.29 | 458.04 | 0.18 | 2.20 | 1588 |
| 2024-09-20 22:21:33.876 | MS1 | 121.4656688949 | 31.1446192500 | 14 | 504990 | -86.36 | 13.39 | 602.98 | 0.05 | 2.13 | 1569 |
| 2024-09-20 22:21:34.416 | MS1 | 121.4656625767 | 31.1446194261 | 14 | 504990 | -87.77 | 12.89 | 82.89 | 0.12 | 2.51 | 1568 |
| 2024-09-20 22:21:35.194 | MS1 | 121.4656646182 | 31.1446369579 | 14 | 504990 | -85.66 | 15.69 | 78.68 | 0.06 | 2.31 | 1568 |
| 2024-09-20 22:21:36.484 | MS1 | 121.4656687559 | 31.1446352030 | 14 | 504990 | -86.46 | 14.16 | 57.37 | 0.01 | 2.53 | 1597 |
| 2024-09-20 22:21:37.854 | MS1 | 121.4656582194 | 31.1446282438 | 14 | 504990 | -93.95 | 12.81 | 82.00 | 0.11 | 2.91 | 1577 |
| 2024-09-20 22:21:38.647 | MS1 | 121.4656589326 | 31.1446211115 | 14 | 504990 | -89.94 | 10.73 | 79.58 | 0.10 | 2.35 | 1568 |
| 2024-09-20 22:21:39.903 | MS1 | 121.4656772507 | 31.1446234408 | 14 | 504990 | -93.35 | 12.50 | 87.91 | 0.07 | 2.69 | 1585 |
| 2024-09-20 22:21:40.885 | MS1 | 121.4656719054 | 31.1446263471 | 14 | 504990 | -93.79 | 8.24 | 601.09 | 0.01 | 2.04 | 1587 |
| 2024-09-20 22:21:41.343 | MS1 | 121.4656729541 | 31.1446199070 | 14 | 504990 | -91.14 | 9.52 | 341.24 | 0.09 | 2.18 | 1595 |
| 2024-09-20 22:21:42.457 | MS1 | 121.4656733986 | 31.1446184327 | 14 | 504990 | -91.58 | 9.58 | 552.59 | 0.08 | 2.43 | 1587 |

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
| 3216183 | 3 | 121.4698064358 | 31.1538633694 | 322 | 7 | 8 | 31.1 | TDD | 716 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3235926 | 2 | 121.4687102776 | 31.1508884839 | 55 | 3 | 12 | 20.6 | TDD | 283 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3251288 | 4 | 121.4754432703 | 31.1446107272 | 291 | 0 | 5 | 43.3 | TDD | 14 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3262475 | 1 | 121.4677320819 | 31.1539338169 | 261 | 7 | 6 | 32.4 | TDD | 720 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.836 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.854 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.974 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.974 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.715 | NREventA3 | measId:2;ServCellPCI:366;Se... |
| 2024-09-20 22:21:37.955 | NRHandoverAttempt | SourcePCI:366;SourceNR-ARFC... |
| 2024-09-20 22:21:38.003 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.014 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.123 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.123 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262475 | 1 | 7.4422 | 19.3038 | -115.9119 | 19.2949 | 166.0822 | 0.0184 | 0.0115 |
| 2024_09_20 22:00 | 3235926 | 2 | 17.2423 | 6.0296 | -117.7670 | 5.7705 | 187.3902 | 0.0031 | 0.0072 |
| 2024_09_20 22:00 | 3216183 | 3 | 6.9070 | 5.8919 | -116.7596 | 17.2193 | 182.0962 | 0.0005 | 0.0048 |
| 2024_09_20 22:00 | 3251288 | 4 | 83.7966 | 85.0586 | -115.1472 | 19.7073 | 162.3783 | 0.0180 | 0.0061 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413770_7799C04E | 504990 | 14 | -89.7 | 504990 | 720 | -94.0 | 504990 | 716 | -96.4 | 504990 | 283 |
| MR_1774413770_9585136B | 504990 | 14 | -88.6 | 504990 | 720 | -94.1 | 504990 | 716 | -96.7 | 504990 | 283 |
| MR_1774413770_4DF12149 | 504990 | 14 | -86.0 | 504990 | 720 | -94.8 | 504990 | 716 | -95.5 | 504990 | 283 |
| MR_1774413770_7C880E54 | 504990 | 14 | -86.6 | 504990 | 720 | -95.4 | 504990 | 716 | -98.4 | 504990 | 283 |
| MR_1774413770_0FB311A5 | 504990 | 14 | -88.3 | 504990 | 720 | -94.3 | 504990 | 716 | -95.2 | 504990 | 283 |
| MR_1774413770_1049D2D6 | 504990 | 14 | -87.7 | 504990 | 720 | -95.4 | 504990 | 716 | -95.2 | 504990 | 283 |
| MR_1774413770_36B2AC63 | 504990 | 14 | -87.7 | 504990 | 720 | -94.3 | 504990 | 716 | -96.9 | 504990 | 283 |
| MR_1774413770_4A39B1FA | 504990 | 14 | -86.1 | 504990 | 720 | -95.4 | 504990 | 716 | -96.2 | 504990 | 283 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 85: `aed8cf54-663...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `aed8cf54-6631-4adf-b6ef-4c808e983a90` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[85] topology](images/train_0085.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236671_1
- `C2`: Lift the tilt angle  of 3236671_1 by 4 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase transmission power for 3236671_1
- `C5`: Adjust the azimuth of 3236671_1 by 50 degrees
- `C6`: Lift the tilt angle of 3273884_4 by 6 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273884_4
- `C8`: Add neighbor relationship between 3252305_2 and 3236671_1
- `C9`: Increase transmission power for 3273884_4
- `C10`: Decrease transmission power for 3273884_4
- `C11`: Decrease A3 Offset threshold for 3273884_4
- `C12`: Increase A3 Offset threshold for 3273884_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273884_4
- `C14`: Decrease transmission power for 3236671_1
- `C15`: Decrease A3 Offset threshold for 3236671_1
- `C16`: Press down the tilt angle  of 3236671_1 by 4 degrees
- `C17`: Press down the tilt angle of 3273884_4 by 6 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236671_1
- `C19`: Check test server and transmission issues **← 정답**
- `C20`: Add neighbor relationship between 3273884_4 and 3236671_1
- `C21`: Adjust the azimuth of 3273884_4 by 50 degrees
- `C22`: Increase A3 Offset threshold for 3236671_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.825 | MS1 | 121.4656629377 | 31.1446304773 | 383 | 504990 | -89.32 | 12.50 | 516.91 | 0.07 | 2.58 | 1593 |
| 2024-09-20 22:21:32.355 | MS1 | 121.4656707921 | 31.1446287770 | 383 | 504990 | -91.13 | 14.51 | 316.49 | 0.17 | 2.28 | 1595 |
| 2024-09-20 22:21:33.709 | MS1 | 121.4656705708 | 31.1446324071 | 383 | 504990 | -86.72 | 16.41 | 315.19 | 0.17 | 2.15 | 1579 |
| 2024-09-20 22:21:34.499 | MS1 | 121.4656761503 | 31.1446234139 | 383 | 504990 | -86.63 | 13.91 | 60.83 | 0.17 | 2.26 | 480 |
| 2024-09-20 22:21:35.924 | MS1 | 121.4656744072 | 31.1446326066 | 383 | 504990 | -90.26 | 13.06 | 54.27 | 0.12 | 2.46 | 331 |
| 2024-09-20 22:21:36.309 | MS1 | 121.4656591276 | 31.1446324468 | 383 | 504990 | -87.54 | 16.49 | 76.84 | 0.03 | 2.52 | 341 |
| 2024-09-20 22:21:37.765 | MS1 | 121.4656703169 | 31.1446319148 | 383 | 504990 | -91.59 | 11.49 | 65.34 | 0.19 | 2.68 | 333 |
| 2024-09-20 22:21:38.571 | MS1 | 121.4656703871 | 31.1446208685 | 383 | 504990 | -89.91 | 9.94 | 68.64 | 0.13 | 2.44 | 412 |
| 2024-09-20 22:21:39.397 | MS1 | 121.4656724766 | 31.1446336994 | 383 | 504990 | -91.49 | 8.24 | 59.50 | 0.03 | 2.50 | 454 |
| 2024-09-20 22:21:40.973 | MS1 | 121.4656645658 | 31.1446286489 | 383 | 504990 | -89.95 | 11.60 | 506.03 | 0.00 | 2.76 | 1589 |
| 2024-09-20 22:21:41.376 | MS1 | 121.4656670735 | 31.1446310362 | 383 | 504990 | -91.63 | 12.82 | 417.62 | 0.11 | 2.97 | 1584 |
| 2024-09-20 22:21:42.519 | MS1 | 121.4656621740 | 31.1446296300 | 383 | 504990 | -93.02 | 7.61 | 319.86 | 0.14 | 2.13 | 1597 |

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
| 3236671 | 1 | 121.4723776846 | 31.1544942609 | 278 | 2 | 6 | 36.7 | TDD | 34 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3242800 | 3 | 121.4759648028 | 31.1480690270 | 233 | 6 | 7 | 40.8 | TDD | 637 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3252305 | 2 | 121.4669022857 | 31.1530603825 | 28 | 14 | 5 | 46.7 | TDD | 228 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3273884 | 4 | 121.4640991967 | 31.1504959378 | 350 | 4 | 11 | 26.0 | TDD | 383 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.810 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.833 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.945 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.945 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.672 | NREventA3 | measId:2;ServCellPCI:170;Se... |
| 2024-09-20 22:21:37.912 | NRHandoverAttempt | SourcePCI:170;SourceNR-ARFC... |
| 2024-09-20 22:21:37.952 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.964 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.092 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.092 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236671 | 1 | 5.1783 | 17.0539 | -115.6643 | 5.3881 | 188.6485 | 0.0120 | 0.0154 |
| 2024_09_20 22:00 | 3252305 | 2 | 11.9654 | 18.8344 | -116.3894 | 11.4892 | 141.6456 | 0.0153 | 0.0070 |
| 2024_09_20 22:00 | 3242800 | 3 | 12.6979 | 14.6747 | -114.1291 | 12.9339 | 151.2493 | 0.0171 | 0.0020 |
| 2024_09_20 22:00 | 3273884 | 4 | 7.1529 | 19.0529 | -115.6588 | 8.4037 | 97.7283 | 0.0138 | 0.0063 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415612_7171A82F | 504990 | 383 | -87.2 | 504990 | 34 | -88.0 | 504990 | 228 | -97.3 | 504990 | 637 |
| MR_1774415612_DC0730DC | 504990 | 383 | -85.9 | 504990 | 34 | -87.4 | 504990 | 228 | -98.0 | 504990 | 637 |
| MR_1774415612_045176B6 | 504990 | 383 | -86.9 | 504990 | 34 | -87.1 | 504990 | 228 | -97.9 | 504990 | 637 |
| MR_1774415612_4C949BCD | 504990 | 383 | -86.9 | 504990 | 34 | -86.6 | 504990 | 228 | -97.0 | 504990 | 637 |
| MR_1774415612_DAD21C5B | 504990 | 383 | -88.2 | 504990 | 34 | -86.7 | 504990 | 228 | -96.5 | 504990 | 637 |
| MR_1774415612_A211A16B | 504990 | 383 | -88.1 | 504990 | 34 | -89.9 | 504990 | 228 | -98.9 | 504990 | 637 |
| MR_1774415612_FB9B5C88 | 504990 | 383 | -85.8 | 504990 | 34 | -90.3 | 504990 | 228 | -98.2 | 504990 | 637 |
| MR_1774415612_9A7C893B | 504990 | 383 | -87.1 | 504990 | 34 | -89.3 | 504990 | 228 | -95.1 | 504990 | 637 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 86: `da2c4b4f-26f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `da2c4b4f-26fa-4550-b17c-cc44611b5ab3` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease A3 Offset threshold for 3217175_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[86] topology](images/train_0086.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266377_1
- `C2`: Increase transmission power for 3217175_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217175_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217175_2
- `C6`: Increase A3 Offset threshold for 3266377_1
- `C7`: Decrease transmission power for 3217175_2
- `C8`: Increase transmission power for 3266377_1
- `C9`: Decrease A3 Offset threshold for 3266377_1
- `C10`: Check test server and transmission issues
- `C11`: Press down the tilt angle of 3217175_2 by 10 degrees
- `C12`: Adjust the azimuth of 3217175_2 by 50 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266377_1
- `C14`: Decrease transmission power for 3266377_1
- `C15`: Add neighbor relationship between 3270268_3 and 3266377_1
- `C16`: Decrease A3 Offset threshold for 3217175_2 **← 정답**
- `C17`: Adjust the azimuth of 3266377_1 by 50 degrees
- `C18`: Increase A3 Offset threshold for 3217175_2
- `C19`: Lift the tilt angle of 3217175_2 by 10 degrees
- `C20`: Press down the tilt angle  of 3266377_1 by 10 degrees
- `C21`: Add neighbor relationship between 3217175_2 and 3266377_1
- `C22`: Lift the tilt angle  of 3266377_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.587 | MS1 | 121.4656605232 | 31.1446370555 | 907 | 504990 | -78.62 | 13.44 | 335.65 | 0.19 | 2.50 | 1596 |
| 2024-09-20 22:21:32.338 | MS1 | 121.4656590881 | 31.1446240624 | 907 | 504990 | -83.63 | 12.83 | 487.23 | 0.15 | 2.88 | 1583 |
| 2024-09-20 22:21:33.917 | MS1 | 121.4656754695 | 31.1446251202 | 907 | 504990 | -81.84 | 14.73 | 304.53 | 0.01 | 2.42 | 1581 |
| 2024-09-20 22:21:34.616 | MS1 | 121.4656747801 | 31.1446232128 | 907 | 504990 | -92.35 | -2.50 | 63.49 | 0.10 | 1.21 | 1598 |
| 2024-09-20 22:21:35.831 | MS1 | 121.4656765614 | 31.1446196793 | 907 | 504990 | -89.39 | -1.49 | 70.87 | 0.05 | 1.03 | 1561 |
| 2024-09-20 22:21:36.578 | MS1 | 121.4656625526 | 31.1446184165 | 907 | 504990 | -87.73 | -0.86 | 66.29 | 0.06 | 1.18 | 1566 |
| 2024-09-20 22:21:37.163 | MS1 | 121.4656710671 | 31.1446320487 | 907 | 504990 | -84.70 | -3.05 | 57.46 | 0.07 | 1.11 | 1592 |
| 2024-09-20 22:21:38.315 | MS1 | 121.4656670449 | 31.1446378816 | 907 | 504990 | -89.75 | -0.72 | 77.92 | 0.06 | 1.19 | 1568 |
| 2024-09-20 22:21:39.666 | MS1 | 121.4656666574 | 31.1446244465 | 122 | 504990 | -77.95 | 15.09 | 241.22 | 0.09 | 1.18 | 1573 |
| 2024-09-20 22:21:40.817 | MS1 | 121.4656735116 | 31.1446348442 | 122 | 504990 | -84.16 | 15.95 | 443.11 | 0.20 | 2.82 | 1600 |
| 2024-09-20 22:21:41.641 | MS1 | 121.4656779731 | 31.1446369570 | 122 | 504990 | -84.18 | 16.15 | 593.26 | 0.05 | 2.41 | 1569 |
| 2024-09-20 22:21:42.590 | MS1 | 121.4656608951 | 31.1446360400 | 122 | 504990 | -84.18 | 12.01 | 314.71 | 0.13 | 2.44 | 1576 |

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
| 3217175 | 2 | 121.4649895433 | 31.1441836146 | 243 | 0 | 4 | 17.4 | TDD | 907 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3257035 | 4 | 121.4689815192 | 31.1508663196 | 270 | 6 | 11 | 47.8 | TDD | 130 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3266377 | 1 | 121.4649133908 | 31.1447879710 | 36 | 1 | 1 | 33.3 | TDD | 122 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3270268 | 3 | 121.4751144728 | 31.1545999297 | 129 | 12 | 11 | 44.3 | TDD | 211 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.548 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.573 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.692 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.692 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.439 | NREventA3 | measId:2;ServCellPCI:402;Se... |
| 2024-09-20 22:21:38.679 | NRHandoverAttempt | SourcePCI:402;SourceNR-ARFC... |
| 2024-09-20 22:21:38.728 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.738 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.851 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.851 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266377 | 1 | 9.7115 | 11.2652 | -114.3002 | 12.0488 | 165.6963 | 0.0029 | 0.0021 |
| 2024_09_20 22:00 | 3217175 | 2 | 8.1060 | 8.6560 | -115.3773 | 14.2242 | 167.2042 | 0.0167 | 0.1535 |
| 2024_09_20 22:00 | 3270268 | 3 | 11.6308 | 6.4192 | -114.7637 | 5.3970 | 97.9205 | 0.0096 | 0.0148 |
| 2024_09_20 22:00 | 3257035 | 4 | 11.3001 | 15.2003 | -117.2308 | 10.8673 | 127.9647 | 0.0080 | 0.0111 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417104_CD9F69C0 | 504990 | 122 | -86.5 | 504990 | 907 | -93.2 | 504990 | 211 | -88.2 | 504990 | 130 |
| MR_1774417104_8204F443 | 504990 | 907 | -91.9 | 504990 | 122 | -85.4 | 504990 | 211 | -89.8 | 504990 | 130 |
| MR_1774417104_17544336 | 504990 | 907 | -92.5 | 504990 | 122 | -87.1 | 504990 | 211 | -89.0 | 504990 | 130 |
| MR_1774417104_23B3E8FF | 504990 | 122 | -86.6 | 504990 | 907 | -90.7 | 504990 | 211 | -87.0 | 504990 | 130 |
| MR_1774417104_6355865E | 504990 | 122 | -88.2 | 504990 | 907 | -91.8 | 504990 | 211 | -88.7 | 504990 | 130 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 87: `c8fcac06-39e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c8fcac06-39e7-49b1-9f63-3ac6a39ff576` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Lift the tilt angle  of 3214011_3 by 4 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[87] topology](images/train_0087.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3272568_2
- `C2`: Increase A3 Offset threshold for 3273549_1
- `C3`: Adjust the azimuth of 3272568_2 by 14 degrees
- `C4`: Increase transmission power for 3273549_1
- `C5`: Add neighbor relationship between 3214011_3 and 3273549_1
- `C6`: Decrease A3 Offset threshold for 3273549_1
- `C7`: Lift the tilt angle of 3272568_2 by 5 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272568_2
- `C9`: Decrease transmission power for 3273549_1
- `C10`: Lift the tilt angle  of 3214011_3 by 4 degrees **← 정답**
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Adjust the azimuth of 3214011_3 by 50 degrees
- `C13`: Press down the tilt angle of 3272568_2 by 5 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273549_1
- `C15`: Decrease A3 Offset threshold for 3272568_2
- `C16`: Add neighbor relationship between 3272568_2 and 3273549_1
- `C17`: Check test server and transmission issues
- `C18`: Decrease transmission power for 3272568_2
- `C19`: Press down the tilt angle  of 3214011_3 by 4 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273549_1
- `C21`: Increase A3 Offset threshold for 3272568_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272568_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.334 | MS1 | 121.4656779028 | 31.1446317644 | 810 | 504990 | -85.08 | 16.93 | 390.63 | 0.14 | 2.11 | 1574 |
| 2024-09-20 22:21:32.948 | MS1 | 121.4656585215 | 31.1446221634 | 810 | 504990 | -86.06 | 17.75 | 385.68 | 0.13 | 2.17 | 1587 |
| 2024-09-20 22:21:33.215 | MS1 | 121.4656595292 | 31.1446325075 | 810 | 504990 | -87.14 | 13.85 | 470.55 | 0.14 | 2.42 | 1565 |
| 2024-09-20 22:21:34.726 | MS1 | 121.4656648636 | 31.1446359001 | 810 | 504990 | -85.31 | 16.23 | 92.36 | 0.02 | 2.64 | 1560 |
| 2024-09-20 22:21:35.922 | MS1 | 121.4656655239 | 31.1446290905 | 810 | 504990 | -90.34 | 17.27 | 77.12 | 0.08 | 2.73 | 1584 |
| 2024-09-20 22:21:36.832 | MS1 | 121.4656733434 | 31.1446373143 | 810 | 504990 | -91.57 | 16.63 | 94.49 | 0.18 | 2.00 | 1568 |
| 2024-09-20 22:21:37.603 | MS1 | 121.4656704758 | 31.1446190972 | 810 | 504990 | -92.89 | 10.87 | 63.94 | 0.19 | 2.04 | 1568 |
| 2024-09-20 22:21:38.727 | MS1 | 121.4656681265 | 31.1446291130 | 810 | 504990 | -89.40 | 8.96 | 100.61 | 0.16 | 2.14 | 1561 |
| 2024-09-20 22:21:39.990 | MS1 | 121.4656779276 | 31.1446193785 | 810 | 504990 | -90.67 | 11.10 | 52.76 | 0.06 | 2.61 | 1572 |
| 2024-09-20 22:21:40.937 | MS1 | 121.4656637727 | 31.1446320477 | 810 | 504990 | -92.02 | 9.90 | 425.92 | 0.05 | 2.75 | 1580 |
| 2024-09-20 22:21:41.958 | MS1 | 121.4656655896 | 31.1446286322 | 810 | 504990 | -89.61 | 10.84 | 336.03 | 0.05 | 2.30 | 1575 |
| 2024-09-20 22:21:42.394 | MS1 | 121.4656647708 | 31.1446211673 | 810 | 504990 | -89.99 | 7.69 | 496.10 | 0.16 | 2.49 | 1580 |

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
| 3214011 | 3 | 121.4715454420 | 31.1485629200 | 34 | 12 | 3 | 37.2 | TDD | 478 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3272229 | 4 | 121.4700890280 | 31.1480224919 | 313 | 2 | 3 | 35.3 | TDD | 41 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3272568 | 2 | 121.4684880105 | 31.1481841839 | 228 | 0 | 12 | 42.2 | TDD | 810 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3273549 | 1 | 121.4738796846 | 31.1530245263 | 132 | 3 | 4 | 26.0 | TDD | 913 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.586 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.607 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.732 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.732 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.436 | NREventA3 | measId:2;ServCellPCI:305;Se... |
| 2024-09-20 22:21:38.676 | NRHandoverAttempt | SourcePCI:305;SourceNR-ARFC... |
| 2024-09-20 22:21:38.716 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.729 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.866 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.866 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273549 | 1 | 10.3897 | 13.2410 | -117.3453 | 15.4299 | 106.8321 | 0.0147 | 0.0152 |
| 2024_09_20 22:00 | 3272568 | 2 | 75.2373 | 89.3866 | -117.8982 | 9.3822 | 151.8984 | 0.0178 | 0.0000 |
| 2024_09_20 22:00 | 3214011 | 3 | 16.9813 | 12.6076 | -114.1121 | 11.8397 | 110.0549 | 0.0115 | 0.0017 |
| 2024_09_20 22:00 | 3272229 | 4 | 18.4816 | 14.1621 | -117.1795 | 6.5480 | 82.7458 | 0.0006 | 0.0100 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415395_9D15773A | 504990 | 810 | -86.7 | 504990 | 913 | -94.2 | 504990 | 478 | -98.5 | 504990 | 41 |
| MR_1774415395_7F83CBBD | 504990 | 810 | -84.6 | 504990 | 913 | -93.2 | 504990 | 478 | -100.9 | 504990 | 41 |
| MR_1774415395_5E8A181B | 504990 | 810 | -84.6 | 504990 | 913 | -94.8 | 504990 | 478 | -101.9 | 504990 | 41 |
| MR_1774415395_1E12915F | 504990 | 810 | -87.0 | 504990 | 913 | -95.9 | 504990 | 478 | -99.3 | 504990 | 41 |
| MR_1774415395_CE2E1F17 | 504990 | 810 | -85.9 | 504990 | 913 | -93.6 | 504990 | 478 | -102.0 | 504990 | 41 |
| MR_1774415395_82915CF8 | 504990 | 810 | -86.5 | 504990 | 913 | -96.2 | 504990 | 478 | -100.7 | 504990 | 41 |
| MR_1774415395_617CE9E8 | 504990 | 810 | -84.3 | 504990 | 913 | -93.9 | 504990 | 478 | -101.9 | 504990 | 41 |
| MR_1774415395_529250D2 | 504990 | 810 | -86.7 | 504990 | 913 | -95.3 | 504990 | 478 | -101.7 | 504990 | 41 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 88: `0bbfd745-b28...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0bbfd745-b285-4410-a11b-f1bb05b79713` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Add neighbor relationship between 3223478_2 and 3213622_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[88] topology](images/train_0088.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213622_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213622_3
- `C4`: Decrease A3 Offset threshold for 3213622_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223478_2
- `C6`: Decrease transmission power for 3223478_2
- `C7`: Increase A3 Offset threshold for 3223478_2
- `C8`: Increase transmission power for 3223478_2
- `C9`: Press down the tilt angle of 3223478_2 by 10 degrees
- `C10`: Press down the tilt angle  of 3213622_3 by 2 degrees
- `C11`: Decrease A3 Offset threshold for 3223478_2
- `C12`: Increase A3 Offset threshold for 3213622_3
- `C13`: Adjust the azimuth of 3213622_3 by 17 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase transmission power for 3213622_3
- `C16`: Decrease transmission power for 3213622_3
- `C17`: Lift the tilt angle of 3223478_2 by 10 degrees
- `C18`: Add neighbor relationship between 3223478_2 and 3213622_3 **← 정답**
- `C19`: Lift the tilt angle  of 3213622_3 by 2 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223478_2
- `C21`: Add neighbor relationship between 3217592_1 and 3213622_3
- `C22`: Adjust the azimuth of 3223478_2 by 48 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.753 | MS1 | 121.4656735585 | 31.1446292213 | 263 | 504990 | -78.24 | 16.66 | 446.15 | 0.15 | 2.66 | 1597 |
| 2024-09-20 22:21:32.556 | MS1 | 121.4656699720 | 31.1446258520 | 263 | 504990 | -77.66 | 16.81 | 553.72 | 0.07 | 2.05 | 1576 |
| 2024-09-20 22:21:33.173 | MS1 | 121.4656733727 | 31.1446232939 | 263 | 504990 | -77.05 | 16.46 | 443.13 | 0.12 | 2.11 | 1588 |
| 2024-09-20 22:21:34.414 | MS1 | 121.4656744344 | 31.1446239344 | 263 | 504990 | -86.65 | -0.73 | 39.89 | 0.19 | 1.22 | 1568 |
| 2024-09-20 22:21:35.523 | MS1 | 121.4656680752 | 31.1446215191 | 263 | 504990 | -91.90 | -1.34 | 48.74 | 0.11 | 1.42 | 1568 |
| 2024-09-20 22:21:36.887 | MS1 | 121.4656676157 | 31.1446378737 | 263 | 504990 | -87.90 | -0.65 | 56.72 | 0.12 | 1.00 | 1575 |
| 2024-09-20 22:21:37.308 | MS1 | 121.4656708596 | 31.1446214956 | 263 | 504990 | -86.32 | -2.31 | 46.99 | 0.11 | 1.46 | 1561 |
| 2024-09-20 22:21:38.773 | MS1 | 121.4656767452 | 31.1446350107 | 263 | 504990 | -76.08 | 17.29 | 550.41 | 0.15 | 1.17 | 1577 |
| 2024-09-20 22:21:39.655 | MS1 | 121.4656776707 | 31.1446311752 | 263 | 504990 | -82.31 | 15.37 | 371.39 | 0.02 | 1.19 | 1568 |
| 2024-09-20 22:21:40.534 | MS1 | 121.4656652581 | 31.1446277509 | 263 | 504990 | -83.19 | 13.98 | 317.28 | 0.08 | 2.87 | 1563 |
| 2024-09-20 22:21:41.331 | MS1 | 121.4656693527 | 31.1446339004 | 263 | 504990 | -78.74 | 16.05 | 548.69 | 0.10 | 2.39 | 1599 |
| 2024-09-20 22:21:42.872 | MS1 | 121.4656592831 | 31.1446187008 | 263 | 504990 | -84.91 | 13.95 | 516.30 | 0.16 | 2.74 | 1560 |

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
| 3213622 | 3 | 121.4744080314 | 31.1471722776 | 234 | 0 | 1 | 27.9 | TDD | 599 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3217592 | 1 | 121.4654621827 | 31.1440422866 | 135 | 12 | 11 | 22.2 | TDD | 650 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3223478 | 2 | 121.4659445451 | 31.1485256906 | 135 | 11 | 5 | 36.3 | TDD | 263 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3223597 | 4 | 121.4656407342 | 31.1479264221 | 245 | 10 | 4 | 44.5 | TDD | 807 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.798 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.813 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.961 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.961 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.652 | NREventA3 | measId:2;ServCellPCI:118;Se... |
| 2024-09-20 22:21:35.652 | NREventA3 | measId:2;ServCellPCI:118;Se... |
| 2024-09-20 22:21:36.652 | NREventA3 | measId:2;ServCellPCI:118;Se... |
| 2024-09-20 22:21:39.152 | NRRRCReestablishAttempt | PCI:118 |
| 2024-09-20 22:21:39.165 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.178 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.324 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.324 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217592 | 1 | 10.5635 | 16.1868 | -117.3284 | 6.2273 | 189.5496 | 0.0048 | 0.0025 |
| 2024_09_20 22:00 | 3223478 | 2 | 12.8401 | 12.4354 | -116.5846 | 19.2038 | 192.7723 | 0.0014 | 0.1996 |
| 2024_09_20 22:00 | 3213622 | 3 | 13.3874 | 10.1110 | -117.2926 | 15.6392 | 195.6036 | 0.0198 | 0.0038 |
| 2024_09_20 22:00 | 3223597 | 4 | 17.5256 | 18.5864 | -116.3034 | 16.5135 | 89.3589 | 0.0194 | 0.0113 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412539_C42C421B | 504990 | 263 | -84.9 | 504990 | 599 | -81.5 | 504990 | 650 | -83.3 | 504990 | 807 |
| MR_1774412539_03C36A23 | 504990 | 263 | -85.8 | 504990 | 599 | -82.8 | 504990 | 650 | -82.4 | 504990 | 807 |
| MR_1774412539_596E5B73 | 504990 | 599 | -83.2 | 504990 | 263 | -85.7 | 504990 | 650 | -81.7 | 504990 | 807 |
| MR_1774412539_2D094A66 | 504990 | 599 | -81.6 | 504990 | 263 | -88.3 | 504990 | 650 | -81.5 | 504990 | 807 |
| MR_1774412539_776D9997 | 504990 | 599 | -82.5 | 504990 | 263 | -86.4 | 504990 | 650 | -84.5 | 504990 | 807 |
| MR_1774412539_D6BAE248 | 504990 | 263 | -86.0 | 504990 | 599 | -82.6 | 504990 | 650 | -83.6 | 504990 | 807 |
| MR_1774412539_1160C076 | 504990 | 599 | -82.5 | 504990 | 263 | -87.9 | 504990 | 650 | -84.7 | 504990 | 807 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 89: `ebfe7bd4-5ad...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ebfe7bd4-5adf-4820-9eb1-bd1af89961eb` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3256264_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[89] topology](images/train_0089.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3274815_1
- `C2`: Adjust the azimuth of 3274815_1 by 50 degrees
- `C3`: Add neighbor relationship between 3235545_4 and 3274815_1
- `C4`: Lift the tilt angle of 3256264_3 by 6 degrees
- `C5`: Decrease transmission power for 3274815_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274815_1
- `C7`: Increase transmission power for 3274815_1
- `C8`: Press down the tilt angle of 3256264_3 by 6 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Increase transmission power for 3256264_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256264_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274815_1
- `C13`: Increase A3 Offset threshold for 3256264_3
- `C14`: Check test server and transmission issues
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256264_3 **← 정답**
- `C16`: Lift the tilt angle  of 3274815_1 by 9 degrees
- `C17`: Decrease transmission power for 3256264_3
- `C18`: Increase A3 Offset threshold for 3274815_1
- `C19`: Adjust the azimuth of 3256264_3 by 12 degrees
- `C20`: Press down the tilt angle  of 3274815_1 by 9 degrees
- `C21`: Decrease A3 Offset threshold for 3256264_3
- `C22`: Add neighbor relationship between 3256264_3 and 3274815_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.109 | MS1 | 121.4656595196 | 31.1446321990 | 957 | 504990 | -88.24 | 15.91 | 332.62 | 0.05 | 2.39 | 1560 |
| 2024-09-20 22:21:32.549 | MS1 | 121.4656613537 | 31.1446343827 | 957 | 504990 | -88.20 | 13.39 | 379.72 | 0.06 | 2.07 | 1565 |
| 2024-09-20 22:21:33.208 | MS1 | 121.4656720141 | 31.1446224873 | 957 | 504990 | -91.09 | 12.81 | 376.92 | 0.12 | 2.92 | 1561 |
| 2024-09-20 22:21:34.605 | MS1 | 121.4656594022 | 31.1446298947 | 957 | 504990 | -86.79 | 15.62 | 95.18 | 0.50 | 2.72 | 653 |
| 2024-09-20 22:21:35.769 | MS1 | 121.4656623108 | 31.1446188690 | 957 | 504990 | -86.56 | 17.80 | 93.39 | 0.53 | 2.57 | 638 |
| 2024-09-20 22:21:36.534 | MS1 | 121.4656739919 | 31.1446192314 | 957 | 504990 | -89.91 | 13.62 | 75.62 | 0.56 | 2.30 | 640 |
| 2024-09-20 22:21:37.675 | MS1 | 121.4656725025 | 31.1446358077 | 957 | 504990 | -90.77 | 7.54 | 92.55 | 0.67 | 2.80 | 657 |
| 2024-09-20 22:21:38.521 | MS1 | 121.4656717187 | 31.1446186056 | 957 | 504990 | -92.22 | 9.87 | 59.03 | 0.61 | 2.17 | 552 |
| 2024-09-20 22:21:39.539 | MS1 | 121.4656612733 | 31.1446191264 | 957 | 504990 | -89.86 | 10.13 | 89.17 | 0.60 | 2.41 | 607 |
| 2024-09-20 22:21:40.753 | MS1 | 121.4656747748 | 31.1446254949 | 957 | 504990 | -90.85 | 10.39 | 494.61 | 0.03 | 2.86 | 1596 |
| 2024-09-20 22:21:41.680 | MS1 | 121.4656593279 | 31.1446267867 | 957 | 504990 | -89.61 | 8.71 | 355.61 | 0.09 | 2.04 | 1598 |
| 2024-09-20 22:21:42.172 | MS1 | 121.4656655326 | 31.1446354518 | 957 | 504990 | -90.88 | 12.58 | 576.29 | 0.16 | 2.42 | 1574 |

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
| 3223383 | 2 | 121.4699439504 | 31.1525815635 | 269 | 9 | 9 | 30.8 | TDD | 738 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3235545 | 4 | 121.4668014695 | 31.1525414386 | 298 | 2 | 11 | 17.8 | TDD | 440 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3256264 | 3 | 121.4662406183 | 31.1550894286 | 195 | 5 | 2 | 19.7 | TDD | 957 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3274815 | 1 | 121.4752281590 | 31.1490192107 | 74 | 6 | 0 | 46.5 | TDD | 32 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.097 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.117 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.233 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.233 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.928 | NREventA3 | measId:2;ServCellPCI:464;Se... |
| 2024-09-20 22:21:38.168 | NRHandoverAttempt | SourcePCI:464;SourceNR-ARFC... |
| 2024-09-20 22:21:38.214 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.227 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.328 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.328 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274815 | 1 | 19.4150 | 10.8290 | -117.5813 | 17.3082 | 145.9582 | 0.0114 | 0.0124 |
| 2024_09_20 22:00 | 3223383 | 2 | 17.9377 | 6.6674 | -115.7612 | 5.1808 | 96.4126 | 0.0154 | 0.0188 |
| 2024_09_20 22:00 | 3256264 | 3 | 14.2990 | 14.6880 | -114.9904 | 19.4350 | 195.8522 | 0.0118 | 0.0091 |
| 2024_09_20 22:00 | 3235545 | 4 | 9.3538 | 18.0995 | -117.9499 | 6.4458 | 94.6024 | 0.0186 | 0.0177 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413369_3D2B379A | 504990 | 957 | -87.1 | 504990 | 32 | -94.7 | 504990 | 440 | -93.3 | 504990 | 738 |
| MR_1774413369_A87E7803 | 504990 | 957 | -86.6 | 504990 | 32 | -93.5 | 504990 | 440 | -93.6 | 504990 | 738 |
| MR_1774413369_DE498C3D | 504990 | 957 | -87.7 | 504990 | 32 | -93.7 | 504990 | 440 | -94.0 | 504990 | 738 |
| MR_1774413369_CD2C5C87 | 504990 | 957 | -88.5 | 504990 | 32 | -91.9 | 504990 | 440 | -93.9 | 504990 | 738 |
| MR_1774413369_A6418273 | 504990 | 957 | -85.9 | 504990 | 32 | -91.1 | 504990 | 440 | -94.2 | 504990 | 738 |
| MR_1774413369_E133AABB | 504990 | 957 | -86.9 | 504990 | 32 | -92.6 | 504990 | 440 | -94.4 | 504990 | 738 |

> *... 2개 열 생략 (전체 14열)*

---
