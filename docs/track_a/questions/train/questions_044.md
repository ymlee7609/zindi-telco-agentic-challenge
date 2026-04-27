# Track A 문제 분석 — train[430]~train[439]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[430] ~ train[439] (10개)

## 목차

1. [문제 430: `a3f8df4e-9a7...`](#430) — single-answer, 정답: C20
2. [문제 431: `b26dfa8d-a3d...`](#431) — single-answer, 정답: C11
3. [문제 432: `ca06eb3f-57e...`](#432) — multiple-answer, 정답: C14|C21
4. [문제 433: `1fcd3e77-c34...`](#433) — single-answer, 정답: C2
5. [문제 434: `afd6707d-37d...`](#434) — single-answer, 정답: C7
6. [문제 435: `996c2211-f50...`](#435) — single-answer, 정답: C2
7. [문제 436: `a050f289-0f5...`](#436) — single-answer, 정답: C9
8. [문제 437: `622b3ce1-1fd...`](#437) — single-answer, 정답: C17
9. [문제 438: `460e2859-ec6...`](#438) — single-answer, 정답: C14
10. [문제 439: `f937b40d-dbe...`](#439) — single-answer, 정답: C17

---

### 문제 430: `a3f8df4e-9a7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a3f8df4e-9a77-4d30-af2b-6f6b4dfcd0ed` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[430] topology](images/train_0430.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3212194_3
- `C2`: Lift the tilt angle  of 3263113_1 by 10 degrees
- `C3`: Increase transmission power for 3212194_3
- `C4`: Add neighbor relationship between 3265408_4 and 3263113_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212194_3
- `C6`: Increase A3 Offset threshold for 3212194_3
- `C7`: Press down the tilt angle  of 3263113_1 by 10 degrees
- `C8`: Adjust the azimuth of 3212194_3 by 50 degrees
- `C9`: Lift the tilt angle of 3212194_3 by 5 degrees
- `C10`: Check test server and transmission issues
- `C11`: Adjust the azimuth of 3263113_1 by 23 degrees
- `C12`: Decrease transmission power for 3263113_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263113_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263113_1
- `C15`: Decrease A3 Offset threshold for 3263113_1
- `C16`: Press down the tilt angle of 3212194_3 by 5 degrees
- `C17`: Decrease A3 Offset threshold for 3212194_3
- `C18`: Increase transmission power for 3263113_1
- `C19`: Increase A3 Offset threshold for 3263113_1
- `C20`: Insufficient data; more data is needed for judgment. **← 정답**
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212194_3
- `C22`: Add neighbor relationship between 3212194_3 and 3263113_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.844 | MS1 | 121.4656638788 | 31.1446315301 | 444 | 504990 | -88.68 | 15.48 | 407.91 | 0.17 | 2.74 | 1595 |
| 2024-09-20 22:21:32.386 | MS1 | 121.4656746570 | 31.1446313661 | 444 | 504990 | -86.74 | 15.65 | 326.02 | 0.02 | 2.05 | 1574 |
| 2024-09-20 22:21:33.317 | MS1 | 121.4656642304 | 31.1446180583 | 444 | 504990 | -88.01 | 17.93 | 480.56 | 0.07 | 2.98 | 1595 |
| 2024-09-20 22:21:34.838 | MS1 | 121.4656676311 | 31.1446205181 | 444 | 504990 | -88.37 | 14.55 | 47.83 | 0.10 | 2.33 | 1574 |
| 2024-09-20 22:21:35.985 | MS1 | 121.4656659419 | 31.1446371581 | 444 | 504990 | -90.14 | 13.51 | 69.64 | 0.14 | 2.28 | 1584 |
| 2024-09-20 22:21:36.394 | MS1 | 121.4656674511 | 31.1446276781 | 444 | 504990 | -91.09 | 16.90 | 58.36 | 0.18 | 2.69 | 1583 |
| 2024-09-20 22:21:37.452 | MS1 | 121.4656753720 | 31.1446284043 | 444 | 504990 | -92.37 | 12.25 | 93.36 | 0.03 | 2.70 | 1572 |
| 2024-09-20 22:21:38.763 | MS1 | 121.4656666926 | 31.1446324139 | 444 | 504990 | -89.44 | 9.84 | 80.30 | 0.08 | 2.97 | 1566 |
| 2024-09-20 22:21:39.375 | MS1 | 121.4656746345 | 31.1446345325 | 444 | 504990 | -91.82 | 10.90 | 78.44 | 0.12 | 2.63 | 1580 |
| 2024-09-20 22:21:40.840 | MS1 | 121.4656640040 | 31.1446342372 | 444 | 504990 | -93.77 | 7.52 | 388.68 | 0.01 | 2.63 | 1570 |
| 2024-09-20 22:21:41.569 | MS1 | 121.4656672225 | 31.1446336009 | 444 | 504990 | -90.03 | 7.88 | 395.30 | 0.15 | 2.92 | 1570 |
| 2024-09-20 22:21:42.821 | MS1 | 121.4656588898 | 31.1446272749 | 444 | 504990 | -91.67 | 12.19 | 358.94 | 0.01 | 2.47 | 1562 |

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
| 3212194 | 3 | 121.4754292215 | 31.1520177868 | 115 | 3 | 2 | 38.2 | TDD | 444 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3241380 | 2 | 121.4751659229 | 31.1502109094 | 87 | 3 | 5 | 43.8 | TDD | 418 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3263113 | 1 | 121.4675303106 | 31.1539783366 | 167 | 14 | 0 | 41.1 | TDD | 457 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3265408 | 4 | 121.4695405613 | 31.1554883372 | 249 | 5 | 11 | 45.2 | TDD | 68 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.473 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.495 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.631 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.631 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.359 | NREventA3 | measId:2;ServCellPCI:608;Se... |
| 2024-09-20 22:21:38.599 | NRHandoverAttempt | SourcePCI:608;SourceNR-ARFC... |
| 2024-09-20 22:21:38.631 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.643 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.747 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.747 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3263113 | 1 | 86.0570 | 88.8574 | -115.1604 | 14.0021 | 99.4618 | 0.0087 | 0.0068 |
| 2024_09_19 22:00 | 3241380 | 2 | 93.9054 | 89.0400 | -115.4170 | 7.6541 | 164.5075 | 0.0088 | 0.0156 |
| 2024_09_19 22:00 | 3212194 | 3 | 80.0578 | 83.4442 | -115.1092 | 16.6116 | 126.7910 | 0.0073 | 0.0048 |
| 2024_09_19 22:00 | 3265408 | 4 | 90.9846 | 94.5805 | -116.7498 | 17.2382 | 85.1266 | 0.0095 | 0.0197 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417021_C1944286 | 504990 | 444 | -89.1 | 504990 | 457 | -92.0 | 504990 | 68 | -100.8 | 504990 | 418 |
| MR_1774417021_A75A4E98 | 504990 | 444 | -90.4 | 504990 | 457 | -91.1 | 504990 | 68 | -104.1 | 504990 | 418 |
| MR_1774417021_FB7A2FB5 | 504990 | 444 | -90.2 | 504990 | 457 | -93.1 | 504990 | 68 | -102.7 | 504990 | 418 |
| MR_1774417021_C664C4AB | 504990 | 444 | -87.6 | 504990 | 457 | -90.4 | 504990 | 68 | -102.4 | 504990 | 418 |
| MR_1774417021_C51992BC | 504990 | 444 | -89.1 | 504990 | 457 | -90.1 | 504990 | 68 | -103.1 | 504990 | 418 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 431: `b26dfa8d-a3d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b26dfa8d-a3d8-47fc-bac9-407eb1c01aeb` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241873_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[431] topology](images/train_0431.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3259776_4 by 24 degrees
- `C2`: Press down the tilt angle  of 3259776_4 by 5 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259776_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259776_4
- `C5`: Decrease A3 Offset threshold for 3259776_4
- `C6`: Increase transmission power for 3241873_1
- `C7`: Decrease transmission power for 3241873_1
- `C8`: Lift the tilt angle of 3241873_1 by 1 degrees
- `C9`: Add neighbor relationship between 3223130_13 and 3259776_4
- `C10`: Lift the tilt angle  of 3259776_4 by 5 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241873_1 **← 정답**
- `C12`: Decrease A3 Offset threshold for 3241873_1
- `C13`: Press down the tilt angle of 3241873_1 by 1 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase transmission power for 3259776_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241873_1
- `C17`: Increase A3 Offset threshold for 3241873_1
- `C18`: Check test server and transmission issues
- `C19`: Decrease transmission power for 3259776_4
- `C20`: Add neighbor relationship between 3241873_1 and 3259776_4
- `C21`: Adjust the azimuth of 3241873_1 by 6 degrees
- `C22`: Increase A3 Offset threshold for 3259776_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.287 | MS1 | 121.4656612069 | 31.1446327995 | 257 | 504990 | -95.88 | 12.66 | 581.50 | 0.13 | 2.90 | 1560 |
| 2024-09-20 22:21:32.414 | MS1 | 121.4656664107 | 31.1446335150 | 850 | 504990 | -94.35 | 12.31 | 322.15 | 0.02 | 2.68 | 1560 |
| 2024-09-20 22:21:33.813 | MS1 | 121.4656664610 | 31.1446368429 | 400 | 504990 | -93.36 | 11.84 | 584.85 | 0.17 | 2.57 | 1569 |
| 2024-09-20 22:21:34.908 | MS1 | 121.4656632426 | 31.1446287865 | 641 | 152650 | -90.34 | 5.54 | 57.02 | 0.08 | 1.68 | 922 |
| 2024-09-20 22:21:35.392 | MS1 | 121.4656605651 | 31.1446247419 | 605 | 152650 | -89.80 | 4.78 | 87.53 | 0.02 | 1.81 | 912 |
| 2024-09-20 22:21:36.503 | MS1 | 121.4656690511 | 31.1446266528 | 222 | 152650 | -87.59 | 7.13 | 60.78 | 0.08 | 1.77 | 999 |
| 2024-09-20 22:21:37.299 | MS1 | 121.4656739088 | 31.1446272510 | 776 | 152650 | -93.58 | 6.11 | 67.70 | 0.00 | 1.95 | 910 |
| 2024-09-20 22:21:38.256 | MS1 | 121.4656722786 | 31.1446227967 | 641 | 152650 | -88.01 | 7.27 | 100.03 | 0.04 | 1.66 | 979 |
| 2024-09-20 22:21:39.941 | MS1 | 121.4656727352 | 31.1446307789 | 605 | 152650 | -93.56 | 2.57 | 78.67 | 0.03 | 1.97 | 965 |
| 2024-09-20 22:21:40.210 | MS1 | 121.4656745148 | 31.1446349802 | 222 | 152650 | -91.66 | 3.09 | 70.85 | 0.17 | 2.80 | 1592 |
| 2024-09-20 22:21:41.895 | MS1 | 121.4656581469 | 31.1446368958 | 776 | 152650 | -91.12 | 4.56 | 71.49 | 0.19 | 2.06 | 1582 |
| 2024-09-20 22:21:42.427 | MS1 | 121.4656698880 | 31.1446244713 | 641 | 152650 | -87.05 | 7.84 | 50.84 | 0.03 | 2.59 | 1562 |

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
| 3223130 | 13 | 121.4642536215 | 31.1503947657 | 263 | 15 | 9 | 21.7 | FDD | 222 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3224632 | 12 | 121.4664155420 | 31.1449685342 | 125 | 14 | 6 | 3.6 | FDD | 605 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3237018 | 2 | 121.4664838864 | 31.1521816864 | 110 | 14 | 7 | 1.3 | TDD | 141 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3238734 | 7 | 121.4678668398 | 31.1496985226 | 238 | 1 | 9 | 26.7 | FDD | 641 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3240536 | 6 | 121.4687161982 | 31.1556473344 | 94 | 13 | 2 | 14.7 | TDD | 573 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3241873 | 1 | 121.4693555478 | 31.1553721957 | 202 | 1 | 3 | 3.5 | TDD | 257 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3248707 | 3 | 121.4752283187 | 31.1540327606 | 318 | 11 | 9 | 0.6 | TDD | 400 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3251306 | 11 | 121.4659133929 | 31.1517760159 | 320 | 6 | 7 | 28.3 | FDD | 304 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3259776 | 4 | 121.4661029700 | 31.1549607583 | 206 | 4 | 4 | 19.7 | TDD | 241 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3264798 | 9 | 121.4733761268 | 31.1453454229 | 248 | 1 | 11 | 22.3 | FDD | 773 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3269700 | 5 | 121.4739598485 | 31.1508934801 | 67 | 8 | 11 | 14.3 | TDD | 850 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3276101 | 10 | 121.4680263640 | 31.1541622450 | 189 | 0 | 1 | 15.4 | FDD | 776 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3277256 | 8 | 121.4750305271 | 31.1506657535 | 244 | 7 | 7 | 6.9 | FDD | 164 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |

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
| 2024-09-20 22:21:31.234 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.252 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.402 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.402 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.115 | NREventA2 | measId:1;ServCellPCI:153;Se... |
| 2024-09-20 22:21:35.249 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.466 | NREventA5 | measId:3;ServCellPCI:153;Se... |
| 2024-09-20 22:21:35.527 | NRHandoverAttempt | SourcePCI:153;SourceNR-ARFC... |
| 2024-09-20 22:21:35.558 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.572 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.692 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.692 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241873 | 1 | 18.3972 | 8.1100 | -115.7756 | 14.7777 | 116.7866 | 0.0070 | 0.0094 |
| 2024_09_20 22:00 | 3237018 | 2 | 17.8358 | 18.2449 | -115.1815 | 13.5069 | 138.3386 | 0.0003 | 0.0135 |
| 2024_09_20 22:00 | 3248707 | 3 | 7.5362 | 11.2992 | -114.1037 | 10.1153 | 110.8311 | 0.0019 | 0.0040 |
| 2024_09_20 22:00 | 3259776 | 4 | 17.3798 | 13.7195 | -115.8386 | 10.1716 | 85.4700 | 0.0133 | 0.0153 |
| 2024_09_20 22:00 | 3269700 | 5 | 16.2238 | 9.6740 | -115.7480 | 16.0014 | 190.6084 | 0.0184 | 0.0193 |
| 2024_09_20 22:00 | 3240536 | 6 | 19.4535 | 6.5179 | -117.7162 | 14.3292 | 150.7531 | 0.0140 | 0.0178 |
| 2024_09_20 22:00 | 3238734 | 7 | 17.8654 | 12.8323 | -116.2985 | 3.2533 | 53.6405 | 0.0132 | 0.0190 |
| 2024_09_20 22:00 | 3277256 | 8 | 13.5247 | 6.0061 | -114.3057 | 3.8502 | 41.8304 | 0.0075 | 0.0077 |
| 2024_09_20 22:00 | 3264798 | 9 | 19.6475 | 10.9477 | -115.9151 | 3.0020 | 51.7030 | 0.0040 | 0.0021 |
| 2024_09_20 22:00 | 3276101 | 10 | 11.0209 | 17.7605 | -116.2792 | 4.6366 | 32.2539 | 0.0026 | 0.0004 |
| 2024_09_20 22:00 | 3251306 | 11 | 13.9440 | 16.6323 | -116.7522 | 4.2927 | 24.6431 | 0.0060 | 0.0088 |
| 2024_09_20 22:00 | 3224632 | 12 | 7.6749 | 6.5842 | -116.5210 | 4.8553 | 26.4330 | 0.0194 | 0.0080 |
| 2024_09_20 22:00 | 3223130 | 13 | 19.0172 | 14.7439 | -117.1276 | 4.5860 | 58.7327 | 0.0030 | 0.0137 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416313_F6A05115 | 504990 | 400 | -92.3 | 504990 | 241 | -89.9 | 504990 | 573 | -93.6 | 504990 | 141 |
| MR_1774416313_6E272767 | 504990 | 400 | -93.8 | 504990 | 241 | -89.9 | 504990 | 573 | -92.3 | 504990 | 141 |
| MR_1774416313_92E573DB | 152650 | 641 | -89.3 | 152650 | 164 | -94.3 | 152650 | 304 | -96.2 | 152650 | 773 |
| MR_1774416313_9F747FFE | 152650 | 641 | -91.2 | 152650 | 164 | -93.0 | 152650 | 304 | -96.3 | 152650 | 773 |
| MR_1774416313_2FCE619E | 504990 | 400 | -92.8 | 504990 | 241 | -87.0 | 504990 | 573 | -91.6 | 504990 | 141 |
| MR_1774416313_AAEBD80D | 152650 | 641 | -89.9 | 152650 | 164 | -96.0 | 152650 | 304 | -95.1 | 152650 | 773 |
| MR_1774416313_C692BDEC | 504990 | 400 | -91.5 | 504990 | 241 | -88.3 | 504990 | 573 | -91.4 | 504990 | 141 |
| MR_1774416313_37A17657 | 504990 | 400 | -92.6 | 504990 | 241 | -86.6 | 504990 | 573 | -90.7 | 504990 | 141 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 432: `ca06eb3f-57e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ca06eb3f-57e6-44b3-a581-2952c17e0f0b` |
| Tag | **multiple-answer** |
| 정답 | **C14|C21** |
| C14 의미 | Adjust the azimuth of 3220421_3 by 50 degrees |
| C21 의미 | Increase transmission power for 3220421_3 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[432] topology](images/train_0432.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Adjust the azimuth of 3272349_1 by 2 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220421_3
- `C4`: Increase transmission power for 3272349_1
- `C5`: Add neighbor relationship between 3248290_4 and 3272349_1
- `C6`: Increase A3 Offset threshold for 3220421_3
- `C7`: Lift the tilt angle of 3220421_3 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272349_1
- `C9`: Press down the tilt angle of 3220421_3 by 10 degrees
- `C10`: Lift the tilt angle  of 3272349_1 by 3 degrees
- `C11`: Check test server and transmission issues
- `C12`: Decrease A3 Offset threshold for 3272349_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272349_1
- `C14`: Adjust the azimuth of 3220421_3 by 50 degrees **← 정답**
- `C15`: Decrease A3 Offset threshold for 3220421_3
- `C16`: Add neighbor relationship between 3220421_3 and 3272349_1
- `C17`: Decrease transmission power for 3220421_3
- `C18`: Decrease transmission power for 3272349_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220421_3
- `C20`: Press down the tilt angle  of 3272349_1 by 3 degrees
- `C21`: Increase transmission power for 3220421_3 **← 정답**
- `C22`: Increase A3 Offset threshold for 3272349_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.994 | MS1 | 121.4656658478 | 31.1446317413 | 63 | 504990 | -87.06 | 14.26 | 398.72 | 0.06 | 2.45 | 1593 |
| 2024-09-20 22:21:32.820 | MS1 | 121.4656662097 | 31.1446241430 | 63 | 504990 | -92.11 | 15.97 | 387.74 | 0.16 | 2.77 | 1566 |
| 2024-09-20 22:21:33.414 | MS1 | 121.4656615935 | 31.1446265513 | 63 | 504990 | -85.30 | 12.55 | 327.56 | 0.03 | 2.22 | 1579 |
| 2024-09-20 22:21:34.596 | MS1 | 121.4656604352 | 31.1446250896 | 63 | 504990 | -102.79 | -0.80 | 31.36 | 0.08 | 1.45 | 1567 |
| 2024-09-20 22:21:35.148 | MS1 | 121.4656614672 | 31.1446315930 | 63 | 504990 | -105.29 | 0.02 | 56.74 | 0.13 | 1.05 | 1567 |
| 2024-09-20 22:21:36.595 | MS1 | 121.4656606531 | 31.1446187981 | 63 | 504990 | -109.22 | 0.15 | 64.32 | 0.14 | 1.24 | 1566 |
| 2024-09-20 22:21:37.538 | MS1 | 121.4656647078 | 31.1446320177 | 63 | 504990 | -108.32 | -0.08 | 21.44 | 0.09 | 1.29 | 1579 |
| 2024-09-20 22:21:38.314 | MS1 | 121.4656703516 | 31.1446319329 | 63 | 504990 | -105.04 | -0.05 | 37.84 | 0.03 | 1.02 | 1583 |
| 2024-09-20 22:21:39.897 | MS1 | 121.4656604573 | 31.1446227228 | 63 | 504990 | -101.97 | 0.02 | 64.04 | 0.14 | 1.15 | 1572 |
| 2024-09-20 22:21:40.513 | MS1 | 121.4656581185 | 31.1446335376 | 63 | 504990 | -90.93 | 17.65 | 564.78 | 0.10 | 2.35 | 1573 |
| 2024-09-20 22:21:41.277 | MS1 | 121.4656674451 | 31.1446342501 | 63 | 504990 | -93.89 | 12.43 | 593.56 | 0.06 | 2.01 | 1566 |
| 2024-09-20 22:21:42.400 | MS1 | 121.4656752818 | 31.1446213600 | 63 | 504990 | -85.70 | 17.04 | 388.55 | 0.00 | 2.66 | 1589 |

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
| 3213451 | 2 | 121.4693102994 | 31.1481667165 | 268 | 7 | 10 | 17.6 | TDD | 545 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3220421 | 3 | 121.4666649660 | 31.1482664298 | 120 | 14 | 6 | 47.1 | TDD | 63 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3248290 | 4 | 121.4747826645 | 31.1461333187 | 347 | 14 | 12 | 37.8 | TDD | 607 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3272349 | 1 | 121.4724984483 | 31.1474492043 | 246 | 0 | 12 | 44.1 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.541 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.560 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.681 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.681 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.857 | NREventA2 | measId:1;ServCellPCI:934;Se... |
| 2024-09-20 22:21:34.978 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272349 | 1 | 15.4609 | 5.1808 | -116.3247 | 5.9041 | 173.7541 | 0.0063 | 0.0169 |
| 2024_09_20 22:00 | 3213451 | 2 | 10.6864 | 13.5856 | -115.8373 | 12.1696 | 100.7431 | 0.0065 | 0.0162 |
| 2024_09_20 22:00 | 3220421 | 3 | 9.8797 | 15.7578 | -117.9875 | 19.2531 | 130.2220 | 0.1873 | 0.0008 |
| 2024_09_20 22:00 | 3248290 | 4 | 6.4020 | 19.8429 | -116.2256 | 13.3925 | 97.4752 | 0.0110 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414077_942361AB | 504990 | 63 | -103.8 | 504990 | 248 | -106.9 | 504990 | 607 | -115.5 | 504990 | 545 |
| MR_1774414077_B8A00AE8 | 504990 | 63 | -103.2 | 504990 | 248 | -107.1 | 504990 | 607 | -117.1 | 504990 | 545 |
| MR_1774414077_A48A7093 | 504990 | 63 | -102.6 | 504990 | 248 | -105.4 | 504990 | 607 | -115.7 | 504990 | 545 |
| MR_1774414077_905ABA53 | 504990 | 63 | -101.3 | 504990 | 248 | -108.2 | 504990 | 607 | -115.7 | 504990 | 545 |
| MR_1774414077_EF573729 | 504990 | 63 | -103.5 | 504990 | 248 | -107.7 | 504990 | 607 | -116.4 | 504990 | 545 |
| MR_1774414077_FBA84B55 | 504990 | 63 | -104.6 | 504990 | 248 | -108.9 | 504990 | 607 | -114.4 | 504990 | 545 |
| MR_1774414077_33545D2C | 504990 | 63 | -101.5 | 504990 | 248 | -108.2 | 504990 | 607 | -114.9 | 504990 | 545 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 433: `1fcd3e77-c34...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1fcd3e77-c34f-4c5f-a4a9-cb0d7c971f5d` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229682_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[433] topology](images/train_0433.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3229682_6 by 15 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229682_6 **← 정답**
- `C3`: Add neighbor relationship between 3229682_6 and 3257686_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257686_4
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase transmission power for 3257686_4
- `C7`: Decrease A3 Offset threshold for 3257686_4
- `C8`: Decrease A3 Offset threshold for 3229682_6
- `C9`: Increase transmission power for 3229682_6
- `C10`: Adjust the azimuth of 3257686_4 by 40 degrees
- `C11`: Press down the tilt angle of 3229682_6 by 3 degrees
- `C12`: Increase A3 Offset threshold for 3257686_4
- `C13`: Lift the tilt angle  of 3257686_4 by 5 degrees
- `C14`: Add neighbor relationship between 3249187_9 and 3257686_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257686_4
- `C16`: Check test server and transmission issues
- `C17`: Increase A3 Offset threshold for 3229682_6
- `C18`: Lift the tilt angle of 3229682_6 by 3 degrees
- `C19`: Decrease transmission power for 3257686_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229682_6
- `C21`: Press down the tilt angle  of 3257686_4 by 5 degrees
- `C22`: Decrease transmission power for 3229682_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.605 | MS1 | 121.4656672912 | 31.1446299876 | 694 | 504990 | -93.97 | 10.83 | 446.90 | 0.06 | 2.28 | 1566 |
| 2024-09-20 22:21:32.659 | MS1 | 121.4656671041 | 31.1446343631 | 419 | 504990 | -94.72 | 13.24 | 475.53 | 0.18 | 2.62 | 1581 |
| 2024-09-20 22:21:33.162 | MS1 | 121.4656751438 | 31.1446185538 | 900 | 504990 | -93.09 | 11.39 | 316.44 | 0.00 | 2.37 | 1578 |
| 2024-09-20 22:21:34.984 | MS1 | 121.4656661299 | 31.1446319226 | 18 | 152650 | -87.69 | 7.89 | 94.27 | 0.11 | 1.74 | 942 |
| 2024-09-20 22:21:35.245 | MS1 | 121.4656718391 | 31.1446369932 | 69 | 152650 | -96.58 | 6.34 | 59.18 | 0.06 | 1.69 | 976 |
| 2024-09-20 22:21:36.915 | MS1 | 121.4656623022 | 31.1446343758 | 104 | 152650 | -94.45 | 6.85 | 99.14 | 0.12 | 1.92 | 981 |
| 2024-09-20 22:21:37.781 | MS1 | 121.4656584914 | 31.1446240549 | 263 | 152650 | -95.47 | 2.53 | 82.54 | 0.05 | 1.86 | 982 |
| 2024-09-20 22:21:38.893 | MS1 | 121.4656633830 | 31.1446271777 | 18 | 152650 | -91.75 | 5.88 | 82.65 | 0.15 | 1.59 | 965 |
| 2024-09-20 22:21:39.301 | MS1 | 121.4656640486 | 31.1446231260 | 69 | 152650 | -87.32 | 5.37 | 68.60 | 0.15 | 1.86 | 937 |
| 2024-09-20 22:21:40.903 | MS1 | 121.4656717045 | 31.1446203400 | 104 | 152650 | -96.25 | 5.60 | 60.61 | 0.17 | 2.27 | 1566 |
| 2024-09-20 22:21:41.235 | MS1 | 121.4656639174 | 31.1446275306 | 263 | 152650 | -90.71 | 2.94 | 50.98 | 0.19 | 2.98 | 1600 |
| 2024-09-20 22:21:42.161 | MS1 | 121.4656760356 | 31.1446261685 | 18 | 152650 | -87.78 | 3.21 | 83.42 | 0.16 | 2.62 | 1577 |

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
| 3214748 | 5 | 121.4758317861 | 31.1467199570 | 227 | 11 | 11 | 11.2 | TDD | 849 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3219339 | 3 | 121.4654493831 | 31.1514911033 | 131 | 4 | 2 | 29.6 | TDD | 900 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3220666 | 11 | 121.4667116056 | 31.1445482191 | 188 | 9 | 6 | 9.7 | FDD | 18 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3226695 | 10 | 121.4680209879 | 31.1517832070 | 82 | 15 | 0 | 21.2 | FDD | 1006 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3228086 | 12 | 121.4750613860 | 31.1498295039 | 292 | 13 | 9 | 22.7 | FDD | 824 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3229682 | 6 | 121.4729085185 | 31.1486093727 | 222 | 2 | 11 | 18.7 | TDD | 694 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3238742 | 1 | 121.4726015748 | 31.1532985236 | 231 | 3 | 0 | 0.2 | TDD | 993 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3249187 | 9 | 121.4728725907 | 31.1463841881 | 142 | 7 | 10 | 8.6 | FDD | 104 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3251284 | 8 | 121.4704925416 | 31.1449664694 | 305 | 6 | 2 | 27.5 | FDD | 263 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3252001 | 2 | 121.4728385360 | 31.1557651805 | 35 | 8 | 10 | 1.9 | TDD | 419 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3252880 | 13 | 121.4712878659 | 31.1472542566 | 75 | 1 | 3 | 22.8 | FDD | 408 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3256832 | 7 | 121.4745546706 | 31.1491492153 | 148 | 0 | 3 | 16.1 | FDD | 69 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3257686 | 4 | 121.4699390570 | 31.1452785378 | 220 | 2 | 6 | 18.1 | TDD | 141 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.806 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.829 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.979 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.979 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.673 | NREventA2 | measId:1;ServCellPCI:196;Se... |
| 2024-09-20 22:21:34.802 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.083 | NREventA5 | measId:3;ServCellPCI:196;Se... |
| 2024-09-20 22:21:35.156 | NRHandoverAttempt | SourcePCI:196;SourceNR-ARFC... |
| 2024-09-20 22:21:35.203 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.213 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.346 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.346 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238742 | 1 | 9.9190 | 13.6899 | -116.1940 | 15.7491 | 162.4469 | 0.0135 | 0.0036 |
| 2024_09_20 22:00 | 3252001 | 2 | 10.9219 | 13.9866 | -116.9637 | 18.4813 | 92.5994 | 0.0106 | 0.0153 |
| 2024_09_20 22:00 | 3219339 | 3 | 8.4553 | 19.9279 | -117.0482 | 10.4095 | 153.1302 | 0.0086 | 0.0103 |
| 2024_09_20 22:00 | 3257686 | 4 | 11.4136 | 8.6507 | -116.0243 | 18.4187 | 91.2853 | 0.0039 | 0.0184 |
| 2024_09_20 22:00 | 3214748 | 5 | 13.8252 | 8.7176 | -115.8267 | 8.7795 | 109.8235 | 0.0140 | 0.0104 |
| 2024_09_20 22:00 | 3229682 | 6 | 19.6371 | 11.8061 | -116.6450 | 16.5827 | 189.2807 | 0.0037 | 0.0102 |
| 2024_09_20 22:00 | 3256832 | 7 | 12.0078 | 6.1867 | -117.3905 | 4.6650 | 24.6420 | 0.0034 | 0.0122 |
| 2024_09_20 22:00 | 3251284 | 8 | 13.3648 | 6.5486 | -116.7669 | 3.8012 | 43.0322 | 0.0165 | 0.0173 |
| 2024_09_20 22:00 | 3249187 | 9 | 17.8301 | 11.4558 | -115.5158 | 4.6635 | 33.8563 | 0.0113 | 0.0057 |
| 2024_09_20 22:00 | 3226695 | 10 | 9.0235 | 13.1393 | -116.2689 | 4.2891 | 20.6541 | 0.0150 | 0.0031 |
| 2024_09_20 22:00 | 3220666 | 11 | 19.8308 | 17.0955 | -116.1903 | 4.6580 | 59.9223 | 0.0004 | 0.0025 |
| 2024_09_20 22:00 | 3228086 | 12 | 17.2234 | 9.2901 | -116.3539 | 4.0663 | 50.7894 | 0.0078 | 0.0134 |
| 2024_09_20 22:00 | 3252880 | 13 | 10.5567 | 6.3138 | -117.6302 | 3.7724 | 35.9347 | 0.0027 | 0.0189 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413894_3C504297 | 504990 | 900 | -91.9 | 504990 | 141 | -90.3 | 504990 | 993 | -96.3 | 504990 | 849 |
| MR_1774413894_0B18EEE1 | 152650 | 18 | -86.4 | 152650 | 1006 | -95.2 | 152650 | 408 | -93.9 | 152650 | 824 |
| MR_1774413894_62CA4CC3 | 152650 | 18 | -86.7 | 152650 | 1006 | -95.1 | 152650 | 408 | -93.7 | 152650 | 824 |
| MR_1774413894_EC26D0A0 | 504990 | 900 | -91.8 | 504990 | 141 | -93.0 | 504990 | 993 | -98.7 | 504990 | 849 |
| MR_1774413894_97C0D6C0 | 152650 | 18 | -87.4 | 152650 | 1006 | -95.3 | 152650 | 408 | -93.7 | 152650 | 824 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 434: `afd6707d-37d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `afd6707d-37db-4f81-afaa-daaedd59e4c3` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease A3 Offset threshold for 3260417_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[434] topology](images/train_0434.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3260417_2 by 10 degrees
- `C2`: Decrease transmission power for 3221724_3
- `C3`: Press down the tilt angle  of 3221724_3 by 5 degrees
- `C4`: Lift the tilt angle of 3260417_2 by 10 degrees
- `C5`: Adjust the azimuth of 3260417_2 by 50 degrees
- `C6`: Check test server and transmission issues
- `C7`: Decrease A3 Offset threshold for 3260417_2 **← 정답**
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260417_2
- `C10`: Decrease transmission power for 3260417_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221724_3
- `C12`: Adjust the azimuth of 3221724_3 by 50 degrees
- `C13`: Increase A3 Offset threshold for 3260417_2
- `C14`: Add neighbor relationship between 3260417_2 and 3221724_3
- `C15`: Lift the tilt angle  of 3221724_3 by 5 degrees
- `C16`: Increase transmission power for 3260417_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260417_2
- `C18`: Add neighbor relationship between 3263525_1 and 3221724_3
- `C19`: Decrease A3 Offset threshold for 3221724_3
- `C20`: Increase transmission power for 3221724_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221724_3
- `C22`: Increase A3 Offset threshold for 3221724_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.696 | MS1 | 121.4656645852 | 31.1446245604 | 211 | 504990 | -84.45 | 12.32 | 450.81 | 0.15 | 2.12 | 1581 |
| 2024-09-20 22:21:32.268 | MS1 | 121.4656643336 | 31.1446196763 | 211 | 504990 | -77.11 | 13.81 | 308.79 | 0.19 | 2.83 | 1599 |
| 2024-09-20 22:21:33.160 | MS1 | 121.4656683924 | 31.1446192193 | 211 | 504990 | -80.54 | 17.14 | 345.72 | 0.18 | 2.38 | 1600 |
| 2024-09-20 22:21:34.741 | MS1 | 121.4656742214 | 31.1446303626 | 211 | 504990 | -85.46 | -3.17 | 73.51 | 0.09 | 1.07 | 1560 |
| 2024-09-20 22:21:35.168 | MS1 | 121.4656693814 | 31.1446251246 | 211 | 504990 | -89.36 | -2.10 | 35.76 | 0.12 | 1.29 | 1582 |
| 2024-09-20 22:21:36.886 | MS1 | 121.4656701105 | 31.1446369176 | 211 | 504990 | -87.59 | -3.07 | 38.28 | 0.19 | 1.22 | 1585 |
| 2024-09-20 22:21:37.122 | MS1 | 121.4656635772 | 31.1446202533 | 211 | 504990 | -88.17 | -0.93 | 71.43 | 0.01 | 1.15 | 1573 |
| 2024-09-20 22:21:38.368 | MS1 | 121.4656663368 | 31.1446229756 | 211 | 504990 | -86.51 | -0.18 | 55.76 | 0.11 | 1.43 | 1590 |
| 2024-09-20 22:21:39.279 | MS1 | 121.4656615353 | 31.1446181665 | 228 | 504990 | -79.36 | 13.83 | 174.30 | 0.10 | 1.46 | 1582 |
| 2024-09-20 22:21:40.832 | MS1 | 121.4656603973 | 31.1446249530 | 228 | 504990 | -77.33 | 17.93 | 331.86 | 0.04 | 2.76 | 1587 |
| 2024-09-20 22:21:41.471 | MS1 | 121.4656599825 | 31.1446353471 | 228 | 504990 | -83.01 | 12.23 | 402.44 | 0.18 | 2.57 | 1582 |
| 2024-09-20 22:21:42.690 | MS1 | 121.4656625708 | 31.1446189115 | 228 | 504990 | -77.04 | 13.36 | 509.73 | 0.00 | 2.01 | 1593 |

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
| 3221724 | 3 | 121.4723627529 | 31.1507524288 | 53 | 3 | 4 | 36.8 | TDD | 228 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3260417 | 2 | 121.4672286814 | 31.1474263215 | 32 | 12 | 2 | 25.5 | TDD | 211 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3263525 | 1 | 121.4665279439 | 31.1440033218 | 306 | 1 | 5 | 21.1 | TDD | 869 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3267299 | 4 | 121.4645953747 | 31.1459967309 | 18 | 1 | 8 | 28.9 | TDD | 605 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.141 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.164 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.279 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.279 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.983 | NREventA3 | measId:2;ServCellPCI:942;Se... |
| 2024-09-20 22:21:38.223 | NRHandoverAttempt | SourcePCI:942;SourceNR-ARFC... |
| 2024-09-20 22:21:38.253 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.263 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.392 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.392 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263525 | 1 | 6.1370 | 18.0945 | -117.9296 | 9.3311 | 197.7115 | 0.0003 | 0.0127 |
| 2024_09_20 22:00 | 3260417 | 2 | 6.3430 | 7.4050 | -117.2991 | 12.1578 | 85.2345 | 0.0187 | 0.1854 |
| 2024_09_20 22:00 | 3221724 | 3 | 6.6175 | 14.4229 | -116.1162 | 13.4548 | 94.7748 | 0.0173 | 0.0049 |
| 2024_09_20 22:00 | 3267299 | 4 | 10.8859 | 8.9653 | -115.9248 | 15.4988 | 131.0002 | 0.0103 | 0.0193 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413324_A8D430B5 | 504990 | 211 | -87.1 | 504990 | 228 | -81.3 | 504990 | 869 | -83.5 | 504990 | 605 |
| MR_1774413324_45C4F3DE | 504990 | 228 | -81.9 | 504990 | 211 | -83.7 | 504990 | 869 | -80.4 | 504990 | 605 |
| MR_1774413324_922342BC | 504990 | 211 | -85.7 | 504990 | 228 | -80.2 | 504990 | 869 | -80.9 | 504990 | 605 |
| MR_1774413324_C61C3FAF | 504990 | 228 | -82.4 | 504990 | 211 | -84.5 | 504990 | 869 | -81.5 | 504990 | 605 |
| MR_1774413324_E329A95A | 504990 | 228 | -82.4 | 504990 | 211 | -83.8 | 504990 | 869 | -83.7 | 504990 | 605 |
| MR_1774413324_B9CC6135 | 504990 | 228 | -82.3 | 504990 | 211 | -84.8 | 504990 | 869 | -83.3 | 504990 | 605 |
| MR_1774413324_6B4935BE | 504990 | 228 | -81.5 | 504990 | 211 | -85.4 | 504990 | 869 | -81.7 | 504990 | 605 |
| MR_1774413324_898017CC | 504990 | 211 | -87.0 | 504990 | 228 | -81.5 | 504990 | 869 | -83.3 | 504990 | 605 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 435: `996c2211-f50...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `996c2211-f50a-4137-9d9c-3337022d42d5` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236688_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[435] topology](images/train_0435.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234477_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236688_2 **← 정답**
- `C3`: Increase A3 Offset threshold for 3236688_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234477_3
- `C5`: Decrease transmission power for 3234477_3
- `C6`: Press down the tilt angle of 3236688_2 by 3 degrees
- `C7`: Decrease A3 Offset threshold for 3234477_3
- `C8`: Press down the tilt angle  of 3234477_3 by 5 degrees
- `C9`: Adjust the azimuth of 3234477_3 by 41 degrees
- `C10`: Add neighbor relationship between 3236688_2 and 3234477_3
- `C11`: Increase transmission power for 3234477_3
- `C12`: Lift the tilt angle  of 3234477_3 by 5 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236688_2
- `C15`: Add neighbor relationship between 3218174_11 and 3234477_3
- `C16`: Decrease transmission power for 3236688_2
- `C17`: Decrease A3 Offset threshold for 3236688_2
- `C18`: Increase transmission power for 3236688_2
- `C19`: Check test server and transmission issues
- `C20`: Adjust the azimuth of 3236688_2 by 44 degrees
- `C21`: Increase A3 Offset threshold for 3234477_3
- `C22`: Lift the tilt angle of 3236688_2 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.451 | MS1 | 121.4656752637 | 31.1446222205 | 424 | 504990 | -93.69 | 11.94 | 346.94 | 0.16 | 2.62 | 1580 |
| 2024-09-20 22:21:32.832 | MS1 | 121.4656669271 | 31.1446310152 | 657 | 504990 | -93.91 | 9.89 | 489.98 | 0.13 | 2.17 | 1563 |
| 2024-09-20 22:21:33.273 | MS1 | 121.4656732629 | 31.1446287164 | 800 | 504990 | -95.82 | 13.13 | 590.26 | 0.13 | 2.18 | 1589 |
| 2024-09-20 22:21:34.382 | MS1 | 121.4656738259 | 31.1446201399 | 200 | 152650 | -96.12 | 6.90 | 45.15 | 0.18 | 1.66 | 902 |
| 2024-09-20 22:21:35.720 | MS1 | 121.4656643011 | 31.1446269519 | 504 | 152650 | -94.34 | 2.62 | 85.19 | 0.17 | 1.53 | 933 |
| 2024-09-20 22:21:36.274 | MS1 | 121.4656700467 | 31.1446345467 | 336 | 152650 | -88.15 | 4.83 | 59.94 | 0.06 | 1.82 | 923 |
| 2024-09-20 22:21:37.235 | MS1 | 121.4656620621 | 31.1446281616 | 429 | 152650 | -92.77 | 7.08 | 78.44 | 0.07 | 1.85 | 965 |
| 2024-09-20 22:21:38.209 | MS1 | 121.4656734593 | 31.1446306466 | 200 | 152650 | -91.08 | 4.14 | 75.52 | 0.05 | 1.70 | 924 |
| 2024-09-20 22:21:39.378 | MS1 | 121.4656735680 | 31.1446319631 | 504 | 152650 | -94.74 | 6.59 | 46.17 | 0.05 | 1.96 | 951 |
| 2024-09-20 22:21:40.626 | MS1 | 121.4656723764 | 31.1446201082 | 336 | 152650 | -95.06 | 2.10 | 52.59 | 0.00 | 2.05 | 1578 |
| 2024-09-20 22:21:41.283 | MS1 | 121.4656769059 | 31.1446367452 | 429 | 152650 | -89.68 | 7.88 | 77.56 | 0.04 | 2.21 | 1591 |
| 2024-09-20 22:21:42.907 | MS1 | 121.4656614855 | 31.1446192315 | 200 | 152650 | -92.32 | 2.38 | 96.19 | 0.10 | 2.79 | 1577 |

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
| 3210894 | 7 | 121.4648117248 | 31.1544624366 | 67 | 1 | 2 | 19.6 | FDD | 675 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3218151 | 9 | 121.4707962857 | 31.1536298279 | 63 | 4 | 9 | 2.5 | FDD | 200 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3218174 | 11 | 121.4756682400 | 31.1549678087 | 108 | 6 | 11 | 16.9 | FDD | 336 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3229924 | 4 | 121.4720474315 | 31.1465336285 | 171 | 6 | 10 | 18.2 | TDD | 559 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3231713 | 8 | 121.4685328885 | 31.1512853453 | 93 | 11 | 8 | 6.7 | FDD | 37 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3233903 | 12 | 121.4703718540 | 31.1525365052 | 30 | 4 | 1 | 24.0 | FDD | 888 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3234477 | 3 | 121.4744023277 | 31.1484481643 | 202 | 3 | 10 | 28.7 | TDD | 554 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3236688 | 2 | 121.4646678818 | 31.1543640706 | 131 | 3 | 9 | 5.7 | TDD | 424 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3245972 | 13 | 121.4649175603 | 31.1509467812 | 320 | 2 | 0 | 28.8 | FDD | 504 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3256389 | 10 | 121.4750263695 | 31.1469945997 | 337 | 8 | 10 | 7.6 | FDD | 429 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3267088 | 6 | 121.4674946772 | 31.1542891697 | 292 | 14 | 3 | 13.0 | TDD | 662 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3271585 | 5 | 121.4667704176 | 31.1507144513 | 292 | 0 | 11 | 5.4 | TDD | 657 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3278333 | 1 | 121.4719681187 | 31.1456001964 | 269 | 12 | 9 | 1.9 | TDD | 800 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.911 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.927 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.044 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.044 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.806 | NREventA2 | measId:1;ServCellPCI:178;Se... |
| 2024-09-20 22:21:34.936 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.210 | NREventA5 | measId:3;ServCellPCI:178;Se... |
| 2024-09-20 22:21:35.257 | NRHandoverAttempt | SourcePCI:178;SourceNR-ARFC... |
| 2024-09-20 22:21:35.279 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.289 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.390 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.390 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278333 | 1 | 7.7792 | 7.1376 | -115.9731 | 18.2073 | 119.6653 | 0.0062 | 0.0062 |
| 2024_09_20 22:00 | 3236688 | 2 | 8.1146 | 18.4757 | -115.6414 | 16.7546 | 98.1659 | 0.0156 | 0.0145 |
| 2024_09_20 22:00 | 3234477 | 3 | 11.2506 | 17.8447 | -114.7571 | 12.7948 | 171.0742 | 0.0074 | 0.0027 |
| 2024_09_20 22:00 | 3229924 | 4 | 16.7158 | 17.3234 | -116.8564 | 12.9585 | 182.4685 | 0.0068 | 0.0157 |
| 2024_09_20 22:00 | 3271585 | 5 | 8.7418 | 6.0201 | -114.5023 | 16.6790 | 86.3632 | 0.0192 | 0.0079 |
| 2024_09_20 22:00 | 3267088 | 6 | 6.8862 | 19.6288 | -114.8196 | 15.0405 | 98.8791 | 0.0006 | 0.0078 |
| 2024_09_20 22:00 | 3210894 | 7 | 13.1559 | 11.4989 | -115.2529 | 3.8014 | 56.4648 | 0.0189 | 0.0066 |
| 2024_09_20 22:00 | 3231713 | 8 | 7.8215 | 12.7231 | -115.0155 | 4.9725 | 46.9333 | 0.0044 | 0.0139 |
| 2024_09_20 22:00 | 3218151 | 9 | 17.7988 | 13.9951 | -114.9829 | 3.5995 | 40.6053 | 0.0079 | 0.0081 |
| 2024_09_20 22:00 | 3256389 | 10 | 11.2071 | 17.2874 | -114.6707 | 3.3865 | 22.3226 | 0.0049 | 0.0174 |
| 2024_09_20 22:00 | 3218174 | 11 | 9.6687 | 16.4183 | -116.2279 | 3.7090 | 20.1555 | 0.0112 | 0.0118 |
| 2024_09_20 22:00 | 3233903 | 12 | 7.4017 | 18.3945 | -116.5458 | 4.4121 | 44.6048 | 0.0186 | 0.0006 |
| 2024_09_20 22:00 | 3245972 | 13 | 13.0812 | 11.7355 | -117.4794 | 4.1185 | 21.8584 | 0.0075 | 0.0075 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416867_EB9126F7 | 152650 | 200 | -94.6 | 152650 | 675 | -104.5 | 152650 | 37 | -104.1 | 152650 | 888 |
| MR_1774416867_E4C99D26 | 504990 | 800 | -96.2 | 504990 | 554 | -96.4 | 504990 | 662 | -103.6 | 504990 | 559 |
| MR_1774416867_326D3037 | 504990 | 800 | -95.3 | 504990 | 554 | -98.1 | 504990 | 662 | -100.3 | 504990 | 559 |
| MR_1774416867_83DAF6DA | 504990 | 800 | -95.0 | 504990 | 554 | -96.4 | 504990 | 662 | -103.0 | 504990 | 559 |
| MR_1774416867_53CFC1CE | 152650 | 200 | -95.4 | 152650 | 675 | -103.1 | 152650 | 37 | -106.4 | 152650 | 888 |
| MR_1774416867_3548FD85 | 504990 | 800 | -96.1 | 504990 | 554 | -96.7 | 504990 | 662 | -101.1 | 504990 | 559 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 436: `a050f289-0f5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a050f289-0f55-4af0-a643-9f161f1fdbee` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Add neighbor relationship between 3247585_1 and 3275908_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[436] topology](images/train_0436.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3275908_4 by 34 degrees
- `C2`: Decrease A3 Offset threshold for 3247585_1
- `C3`: Increase A3 Offset threshold for 3247585_1
- `C4`: Lift the tilt angle  of 3275908_4 by 2 degrees
- `C5`: Lift the tilt angle of 3247585_1 by 10 degrees
- `C6`: Decrease A3 Offset threshold for 3275908_4
- `C7`: Increase transmission power for 3275908_4
- `C8`: Decrease transmission power for 3247585_1
- `C9`: Add neighbor relationship between 3247585_1 and 3275908_4 **← 정답**
- `C10`: Decrease transmission power for 3275908_4
- `C11`: Adjust the azimuth of 3247585_1 by 31 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275908_4
- `C13`: Check test server and transmission issues
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247585_1
- `C15`: Increase A3 Offset threshold for 3275908_4
- `C16`: Press down the tilt angle  of 3275908_4 by 2 degrees
- `C17`: Press down the tilt angle of 3247585_1 by 10 degrees
- `C18`: Add neighbor relationship between 3273136_2 and 3275908_4
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247585_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275908_4
- `C22`: Increase transmission power for 3247585_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.804 | MS1 | 121.4656595149 | 31.1446203669 | 368 | 504990 | -79.43 | 17.33 | 597.56 | 0.15 | 2.36 | 1576 |
| 2024-09-20 22:21:32.323 | MS1 | 121.4656641051 | 31.1446329032 | 368 | 504990 | -82.55 | 12.25 | 355.35 | 0.08 | 2.82 | 1569 |
| 2024-09-20 22:21:33.773 | MS1 | 121.4656744353 | 31.1446261575 | 368 | 504990 | -76.75 | 15.61 | 435.08 | 0.17 | 2.79 | 1598 |
| 2024-09-20 22:21:34.767 | MS1 | 121.4656642621 | 31.1446202371 | 368 | 504990 | -88.76 | -2.92 | 43.14 | 0.07 | 1.20 | 1572 |
| 2024-09-20 22:21:35.556 | MS1 | 121.4656726616 | 31.1446214835 | 368 | 504990 | -92.39 | -1.99 | 47.62 | 0.07 | 1.34 | 1594 |
| 2024-09-20 22:21:36.789 | MS1 | 121.4656734175 | 31.1446319489 | 368 | 504990 | -94.72 | -2.79 | 54.31 | 0.00 | 1.16 | 1596 |
| 2024-09-20 22:21:37.302 | MS1 | 121.4656725869 | 31.1446344553 | 368 | 504990 | -88.82 | -2.80 | 34.76 | 0.20 | 1.14 | 1598 |
| 2024-09-20 22:21:38.696 | MS1 | 121.4656649796 | 31.1446216889 | 368 | 504990 | -82.65 | 16.47 | 441.45 | 0.06 | 1.00 | 1583 |
| 2024-09-20 22:21:39.291 | MS1 | 121.4656656026 | 31.1446319537 | 368 | 504990 | -78.92 | 17.02 | 320.35 | 0.05 | 1.21 | 1594 |
| 2024-09-20 22:21:40.484 | MS1 | 121.4656703324 | 31.1446264093 | 368 | 504990 | -78.32 | 17.35 | 465.43 | 0.14 | 2.65 | 1570 |
| 2024-09-20 22:21:41.382 | MS1 | 121.4656627422 | 31.1446185720 | 368 | 504990 | -76.43 | 16.43 | 488.43 | 0.16 | 2.70 | 1560 |
| 2024-09-20 22:21:42.669 | MS1 | 121.4656764811 | 31.1446187092 | 368 | 504990 | -76.98 | 16.85 | 415.52 | 0.05 | 2.09 | 1597 |

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
| 3247585 | 1 | 121.4702233371 | 31.1555991123 | 231 | 8 | 7 | 42.7 | TDD | 368 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3267472 | 3 | 121.4731725895 | 31.1481545918 | 196 | 4 | 11 | 20.5 | TDD | 884 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3273136 | 2 | 121.4720390015 | 31.1506079432 | 73 | 13 | 11 | 44.3 | TDD | 876 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3275908 | 4 | 121.4739481127 | 31.1527934297 | 255 | 0 | 10 | 41.8 | TDD | 493 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.576 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.593 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.719 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.719 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.431 | NREventA3 | measId:2;ServCellPCI:924;Se... |
| 2024-09-20 22:21:36.431 | NREventA3 | measId:2;ServCellPCI:924;Se... |
| 2024-09-20 22:21:37.431 | NREventA3 | measId:2;ServCellPCI:924;Se... |
| 2024-09-20 22:21:39.931 | NRRRCReestablishAttempt | PCI:924 |
| 2024-09-20 22:21:39.947 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.958 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:40.087 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.087 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247585 | 1 | 13.4880 | 10.0966 | -116.0015 | 9.8913 | 113.5268 | 0.0046 | 0.1297 |
| 2024_09_20 22:00 | 3273136 | 2 | 5.9316 | 18.0398 | -114.9436 | 18.9656 | 144.2224 | 0.0134 | 0.0140 |
| 2024_09_20 22:00 | 3267472 | 3 | 12.2650 | 14.2863 | -114.8906 | 5.4711 | 157.7419 | 0.0174 | 0.0044 |
| 2024_09_20 22:00 | 3275908 | 4 | 14.9806 | 15.9950 | -115.1965 | 10.6052 | 147.4705 | 0.0103 | 0.0172 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413211_D897AE48 | 504990 | 493 | -83.2 | 504990 | 368 | -89.3 | 504990 | 876 | -89.7 | 504990 | 884 |
| MR_1774413211_2E20A8B1 | 504990 | 368 | -88.3 | 504990 | 493 | -82.2 | 504990 | 876 | -87.2 | 504990 | 884 |
| MR_1774413211_F464635C | 504990 | 368 | -88.7 | 504990 | 493 | -84.0 | 504990 | 876 | -86.6 | 504990 | 884 |
| MR_1774413211_ECBCDB9D | 504990 | 368 | -88.8 | 504990 | 493 | -81.9 | 504990 | 876 | -88.6 | 504990 | 884 |
| MR_1774413211_33545521 | 504990 | 368 | -89.4 | 504990 | 493 | -81.5 | 504990 | 876 | -86.2 | 504990 | 884 |
| MR_1774413211_5758315F | 504990 | 368 | -87.5 | 504990 | 493 | -81.1 | 504990 | 876 | -87.4 | 504990 | 884 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 437: `622b3ce1-1fd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `622b3ce1-1fd4-4a6d-9d93-625ca0575ea5` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3251146_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[437] topology](images/train_0437.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3251146_4
- `C2`: Increase A3 Offset threshold for 3256113_2
- `C3`: Adjust the azimuth of 3256113_2 by 50 degrees
- `C4`: Add neighbor relationship between 3251146_4 and 3256113_2
- `C5`: Increase A3 Offset threshold for 3251146_4
- `C6`: Decrease A3 Offset threshold for 3256113_2
- `C7`: Check test server and transmission issues
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251146_4
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Add neighbor relationship between 3226630_1 and 3256113_2
- `C11`: Increase transmission power for 3256113_2
- `C12`: Lift the tilt angle of 3251146_4 by 5 degrees
- `C13`: Decrease transmission power for 3251146_4
- `C14`: Decrease transmission power for 3256113_2
- `C15`: Decrease A3 Offset threshold for 3251146_4
- `C16`: Lift the tilt angle  of 3256113_2 by 10 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251146_4 **← 정답**
- `C18`: Adjust the azimuth of 3251146_4 by 35 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256113_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256113_2
- `C21`: Press down the tilt angle of 3251146_4 by 5 degrees
- `C22`: Press down the tilt angle  of 3256113_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.680 | MS1 | 121.4656765270 | 31.1446355535 | 726 | 504990 | -86.03 | 13.46 | 599.60 | 0.09 | 2.62 | 1567 |
| 2024-09-20 22:21:32.520 | MS1 | 121.4656727843 | 31.1446188819 | 726 | 504990 | -85.41 | 16.49 | 440.59 | 0.09 | 2.24 | 1564 |
| 2024-09-20 22:21:33.625 | MS1 | 121.4656744310 | 31.1446214652 | 726 | 504990 | -86.55 | 15.45 | 596.41 | 0.08 | 2.45 | 1593 |
| 2024-09-20 22:21:34.328 | MS1 | 121.4656590804 | 31.1446296860 | 726 | 504990 | -88.24 | 13.32 | 84.11 | 0.52 | 2.92 | 550 |
| 2024-09-20 22:21:35.935 | MS1 | 121.4656697251 | 31.1446328272 | 726 | 504990 | -90.77 | 17.05 | 51.30 | 0.55 | 2.47 | 560 |
| 2024-09-20 22:21:36.872 | MS1 | 121.4656773949 | 31.1446315176 | 726 | 504990 | -90.13 | 17.73 | 58.35 | 0.57 | 2.65 | 671 |
| 2024-09-20 22:21:37.768 | MS1 | 121.4656662333 | 31.1446277134 | 726 | 504990 | -93.25 | 10.88 | 71.87 | 0.56 | 2.96 | 632 |
| 2024-09-20 22:21:38.984 | MS1 | 121.4656621862 | 31.1446313814 | 726 | 504990 | -93.81 | 9.09 | 96.92 | 0.58 | 2.88 | 605 |
| 2024-09-20 22:21:39.545 | MS1 | 121.4656703201 | 31.1446240918 | 726 | 504990 | -93.25 | 10.18 | 107.18 | 0.63 | 2.42 | 534 |
| 2024-09-20 22:21:40.173 | MS1 | 121.4656777203 | 31.1446230560 | 726 | 504990 | -93.96 | 8.94 | 493.66 | 0.14 | 2.13 | 1574 |
| 2024-09-20 22:21:41.899 | MS1 | 121.4656695703 | 31.1446277760 | 726 | 504990 | -92.63 | 8.15 | 434.24 | 0.09 | 2.36 | 1589 |
| 2024-09-20 22:21:42.895 | MS1 | 121.4656636915 | 31.1446312264 | 726 | 504990 | -92.17 | 11.55 | 404.42 | 0.00 | 2.15 | 1579 |

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
| 3226630 | 1 | 121.4643236950 | 31.1532672193 | 293 | 10 | 1 | 37.7 | TDD | 809 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3236555 | 3 | 121.4693482149 | 31.1508711142 | 7 | 3 | 7 | 30.4 | TDD | 761 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3251146 | 4 | 121.4729470891 | 31.1441793564 | 239 | 3 | 6 | 23.5 | TDD | 726 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3256113 | 2 | 121.4711998596 | 31.1514610634 | 59 | 11 | 0 | 23.6 | TDD | 427 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.664 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.664 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.356 | NREventA3 | measId:2;ServCellPCI:847;Se... |
| 2024-09-20 22:21:38.596 | NRHandoverAttempt | SourcePCI:847;SourceNR-ARFC... |
| 2024-09-20 22:21:38.638 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.653 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.800 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.800 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226630 | 1 | 18.2441 | 8.0290 | -115.5904 | 16.0951 | 167.9869 | 0.0139 | 0.0031 |
| 2024_09_20 22:00 | 3256113 | 2 | 11.3056 | 11.0851 | -115.1340 | 19.9839 | 160.5607 | 0.0168 | 0.0187 |
| 2024_09_20 22:00 | 3236555 | 3 | 18.5134 | 11.9737 | -116.1900 | 14.6753 | 92.7527 | 0.0087 | 0.0057 |
| 2024_09_20 22:00 | 3251146 | 4 | 18.0194 | 17.7707 | -114.6392 | 6.2889 | 176.4657 | 0.0045 | 0.0138 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413686_3ADF2F66 | 504990 | 726 | -89.9 | 504990 | 427 | -95.2 | 504990 | 809 | -99.8 | 504990 | 761 |
| MR_1774413686_A112FC24 | 504990 | 726 | -89.6 | 504990 | 427 | -94.8 | 504990 | 809 | -98.4 | 504990 | 761 |
| MR_1774413686_080BFE6B | 504990 | 726 | -88.3 | 504990 | 427 | -95.4 | 504990 | 809 | -100.4 | 504990 | 761 |
| MR_1774413686_1E6BFE44 | 504990 | 726 | -89.5 | 504990 | 427 | -96.9 | 504990 | 809 | -97.3 | 504990 | 761 |
| MR_1774413686_A77858CF | 504990 | 726 | -89.3 | 504990 | 427 | -98.1 | 504990 | 809 | -99.2 | 504990 | 761 |
| MR_1774413686_7DCF6312 | 504990 | 726 | -87.1 | 504990 | 427 | -98.0 | 504990 | 809 | -97.5 | 504990 | 761 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 438: `460e2859-ec6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `460e2859-ec64-47ed-94f4-380a3fe79418` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease A3 Offset threshold for 3236710_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[438] topology](images/train_0438.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3236710_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236710_4
- `C3`: Increase transmission power for 3236710_4
- `C4`: Increase transmission power for 3246104_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236710_4
- `C6`: Increase A3 Offset threshold for 3236710_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246104_1
- `C8`: Press down the tilt angle of 3236710_4 by 10 degrees
- `C9`: Add neighbor relationship between 3210103_2 and 3246104_1
- `C10`: Lift the tilt angle  of 3246104_1 by 4 degrees
- `C11`: Increase A3 Offset threshold for 3246104_1
- `C12`: Check test server and transmission issues
- `C13`: Press down the tilt angle  of 3246104_1 by 4 degrees
- `C14`: Decrease A3 Offset threshold for 3236710_4 **← 정답**
- `C15`: Adjust the azimuth of 3246104_1 by 50 degrees
- `C16`: Decrease transmission power for 3246104_1
- `C17`: Add neighbor relationship between 3236710_4 and 3246104_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246104_1
- `C20`: Lift the tilt angle of 3236710_4 by 10 degrees
- `C21`: Decrease A3 Offset threshold for 3246104_1
- `C22`: Adjust the azimuth of 3236710_4 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.596 | MS1 | 121.4656758494 | 31.1446196818 | 743 | 504990 | -79.96 | 16.62 | 574.29 | 0.07 | 2.08 | 1581 |
| 2024-09-20 22:21:32.493 | MS1 | 121.4656726924 | 31.1446303451 | 743 | 504990 | -75.13 | 16.03 | 439.83 | 0.19 | 2.43 | 1580 |
| 2024-09-20 22:21:33.248 | MS1 | 121.4656706822 | 31.1446269859 | 743 | 504990 | -82.21 | 14.06 | 548.78 | 0.09 | 2.21 | 1577 |
| 2024-09-20 22:21:34.825 | MS1 | 121.4656695084 | 31.1446262033 | 743 | 504990 | -92.64 | -2.44 | 68.68 | 0.09 | 1.00 | 1577 |
| 2024-09-20 22:21:35.951 | MS1 | 121.4656670618 | 31.1446308605 | 743 | 504990 | -89.62 | -1.77 | 56.64 | 0.09 | 1.28 | 1600 |
| 2024-09-20 22:21:36.979 | MS1 | 121.4656591893 | 31.1446328185 | 743 | 504990 | -86.41 | -3.96 | 57.18 | 0.13 | 1.28 | 1570 |
| 2024-09-20 22:21:37.829 | MS1 | 121.4656719405 | 31.1446305018 | 743 | 504990 | -89.87 | -1.51 | 58.22 | 0.08 | 1.18 | 1590 |
| 2024-09-20 22:21:38.830 | MS1 | 121.4656580996 | 31.1446270145 | 743 | 504990 | -87.94 | -1.60 | 56.14 | 0.12 | 1.36 | 1597 |
| 2024-09-20 22:21:39.951 | MS1 | 121.4656741830 | 31.1446288991 | 577 | 504990 | -84.76 | 13.44 | 193.38 | 0.02 | 1.35 | 1581 |
| 2024-09-20 22:21:40.826 | MS1 | 121.4656724009 | 31.1446275687 | 577 | 504990 | -78.11 | 16.20 | 352.58 | 0.16 | 2.36 | 1563 |
| 2024-09-20 22:21:41.912 | MS1 | 121.4656723714 | 31.1446315794 | 577 | 504990 | -79.69 | 16.08 | 335.90 | 0.19 | 2.36 | 1595 |
| 2024-09-20 22:21:42.643 | MS1 | 121.4656644393 | 31.1446212410 | 577 | 504990 | -82.97 | 16.95 | 531.42 | 0.11 | 2.37 | 1561 |

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
| 3210103 | 2 | 121.4700362732 | 31.1510727006 | 225 | 15 | 0 | 42.4 | TDD | 886 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3236710 | 4 | 121.4733040096 | 31.1534273203 | 106 | 9 | 2 | 29.5 | TDD | 743 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3245893 | 3 | 121.4731629026 | 31.1547866007 | 128 | 14 | 1 | 18.7 | TDD | 638 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3246104 | 1 | 121.4748577288 | 31.1491598443 | 148 | 2 | 4 | 28.3 | TDD | 577 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.028 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.043 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.183 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.183 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.868 | NREventA3 | measId:2;ServCellPCI:229;Se... |
| 2024-09-20 22:21:38.108 | NRHandoverAttempt | SourcePCI:229;SourceNR-ARFC... |
| 2024-09-20 22:21:38.144 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.158 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.260 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.260 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246104 | 1 | 19.9612 | 15.3564 | -116.9487 | 16.4063 | 183.7083 | 0.0101 | 0.0116 |
| 2024_09_20 22:00 | 3210103 | 2 | 18.5016 | 6.3821 | -114.7884 | 12.8802 | 115.5773 | 0.0074 | 0.0088 |
| 2024_09_20 22:00 | 3245893 | 3 | 16.8672 | 9.3889 | -116.7898 | 18.8935 | 132.6800 | 0.0114 | 0.0147 |
| 2024_09_20 22:00 | 3236710 | 4 | 11.0793 | 15.1492 | -117.0594 | 17.6186 | 121.5296 | 0.0145 | 0.1404 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414049_336D605E | 504990 | 577 | -86.0 | 504990 | 743 | -92.0 | 504990 | 886 | -86.6 | 504990 | 638 |
| MR_1774414049_51916BCB | 504990 | 743 | -92.7 | 504990 | 577 | -85.0 | 504990 | 886 | -87.2 | 504990 | 638 |
| MR_1774414049_71152836 | 504990 | 743 | -91.8 | 504990 | 577 | -86.5 | 504990 | 886 | -88.0 | 504990 | 638 |
| MR_1774414049_23D8A61C | 504990 | 577 | -86.6 | 504990 | 743 | -90.7 | 504990 | 886 | -89.2 | 504990 | 638 |
| MR_1774414049_88971668 | 504990 | 743 | -92.7 | 504990 | 577 | -84.6 | 504990 | 886 | -88.4 | 504990 | 638 |
| MR_1774414049_8ED02592 | 504990 | 577 | -84.4 | 504990 | 743 | -94.5 | 504990 | 886 | -86.8 | 504990 | 638 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 439: `f937b40d-dbe...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f937b40d-dbe6-427b-9f6e-33f82d4f683e` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254070_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[439] topology](images/train_0439.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3254070_2 and 3272855_1
- `C2`: Check test server and transmission issues
- `C3`: Decrease transmission power for 3254070_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272855_1
- `C5`: Increase A3 Offset threshold for 3254070_2
- `C6`: Increase A3 Offset threshold for 3272855_1
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Lift the tilt angle of 3254070_2 by 4 degrees
- `C9`: Press down the tilt angle  of 3272855_1 by 5 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254070_2
- `C11`: Adjust the azimuth of 3254070_2 by 34 degrees
- `C12`: Decrease A3 Offset threshold for 3272855_1
- `C13`: Adjust the azimuth of 3272855_1 by 10 degrees
- `C14`: Lift the tilt angle  of 3272855_1 by 5 degrees
- `C15`: Press down the tilt angle of 3254070_2 by 4 degrees
- `C16`: Decrease A3 Offset threshold for 3254070_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254070_2 **← 정답**
- `C18`: Increase transmission power for 3254070_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272855_1
- `C20`: Decrease transmission power for 3272855_1
- `C21`: Add neighbor relationship between 3257647_7 and 3272855_1
- `C22`: Increase transmission power for 3272855_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.271 | MS1 | 121.4656605300 | 31.1446300773 | 35 | 504990 | -95.92 | 11.58 | 304.99 | 0.09 | 2.92 | 1600 |
| 2024-09-20 22:21:32.224 | MS1 | 121.4656708974 | 31.1446330734 | 124 | 504990 | -93.09 | 13.13 | 446.42 | 0.04 | 2.74 | 1593 |
| 2024-09-20 22:21:33.785 | MS1 | 121.4656678038 | 31.1446216347 | 523 | 504990 | -95.06 | 12.84 | 602.89 | 0.14 | 2.73 | 1577 |
| 2024-09-20 22:21:34.965 | MS1 | 121.4656717226 | 31.1446209029 | 508 | 152650 | -90.92 | 3.99 | 63.25 | 0.18 | 1.64 | 948 |
| 2024-09-20 22:21:35.862 | MS1 | 121.4656633040 | 31.1446335930 | 774 | 152650 | -95.37 | 2.90 | 76.54 | 0.12 | 1.89 | 909 |
| 2024-09-20 22:21:36.267 | MS1 | 121.4656706663 | 31.1446261776 | 483 | 152650 | -91.43 | 3.20 | 87.34 | 0.03 | 1.93 | 957 |
| 2024-09-20 22:21:37.489 | MS1 | 121.4656616967 | 31.1446322035 | 1003 | 152650 | -90.81 | 3.90 | 76.02 | 0.16 | 1.89 | 930 |
| 2024-09-20 22:21:38.105 | MS1 | 121.4656630774 | 31.1446256158 | 508 | 152650 | -87.20 | 7.13 | 52.79 | 0.19 | 1.77 | 974 |
| 2024-09-20 22:21:39.942 | MS1 | 121.4656597607 | 31.1446329956 | 774 | 152650 | -96.18 | 6.21 | 70.53 | 0.19 | 1.93 | 947 |
| 2024-09-20 22:21:40.128 | MS1 | 121.4656740055 | 31.1446306774 | 483 | 152650 | -88.65 | 4.93 | 89.89 | 0.01 | 2.33 | 1594 |
| 2024-09-20 22:21:41.836 | MS1 | 121.4656751425 | 31.1446332555 | 1003 | 152650 | -95.99 | 3.82 | 46.86 | 0.18 | 2.61 | 1578 |
| 2024-09-20 22:21:42.210 | MS1 | 121.4656673070 | 31.1446294442 | 508 | 152650 | -94.16 | 7.12 | 77.29 | 0.19 | 2.04 | 1570 |

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
| 3212648 | 11 | 121.4668151780 | 31.1540126392 | 18 | 14 | 7 | 14.6 | FDD | 438 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3216828 | 12 | 121.4692025963 | 31.1559055260 | 244 | 13 | 5 | 0.3 | FDD | 151 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3231463 | 5 | 121.4714926710 | 31.1481272578 | 180 | 14 | 3 | 23.9 | TDD | 124 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3231702 | 8 | 121.4749334773 | 31.1463581806 | 19 | 14 | 12 | 8.2 | FDD | 774 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3244158 | 10 | 121.4753257090 | 31.1525509327 | 19 | 10 | 6 | 0.5 | FDD | 399 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3246151 | 13 | 121.4686017030 | 31.1456097033 | 234 | 1 | 6 | 16.9 | FDD | 508 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3250177 | 6 | 121.4759697561 | 31.1504008134 | 295 | 11 | 1 | 9.7 | TDD | 957 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3254070 | 2 | 121.4736983516 | 31.1502010869 | 265 | 4 | 3 | 6.7 | TDD | 35 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3255990 | 9 | 121.4662020625 | 31.1553330538 | 212 | 12 | 0 | 14.7 | FDD | 1003 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3257647 | 7 | 121.4746765759 | 31.1448219200 | 137 | 3 | 8 | 2.7 | FDD | 483 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3272855 | 1 | 121.4721655671 | 31.1487772350 | 243 | 3 | 2 | 27.1 | TDD | 673 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3275933 | 3 | 121.4651053239 | 31.1551612643 | 184 | 1 | 3 | 8.9 | TDD | 838 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3276088 | 4 | 121.4702146622 | 31.1555331234 | 176 | 2 | 3 | 1.7 | TDD | 523 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.218 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.218 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.913 | NREventA2 | measId:1;ServCellPCI:309;Se... |
| 2024-09-20 22:21:35.029 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.264 | NREventA5 | measId:3;ServCellPCI:309;Se... |
| 2024-09-20 22:21:35.340 | NRHandoverAttempt | SourcePCI:309;SourceNR-ARFC... |
| 2024-09-20 22:21:35.372 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.384 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.511 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.511 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272855 | 1 | 8.9515 | 7.8280 | -117.2514 | 9.3033 | 150.4113 | 0.0187 | 0.0069 |
| 2024_09_20 22:00 | 3254070 | 2 | 17.4905 | 15.2711 | -116.3652 | 19.4981 | 84.8818 | 0.0132 | 0.0127 |
| 2024_09_20 22:00 | 3275933 | 3 | 18.6418 | 13.3362 | -115.2813 | 18.1061 | 126.4703 | 0.0068 | 0.0075 |
| 2024_09_20 22:00 | 3276088 | 4 | 8.2685 | 11.2758 | -114.8055 | 14.0285 | 142.7896 | 0.0084 | 0.0062 |
| 2024_09_20 22:00 | 3231463 | 5 | 17.9789 | 15.5233 | -116.9042 | 6.8280 | 146.3832 | 0.0197 | 0.0105 |
| 2024_09_20 22:00 | 3250177 | 6 | 17.3535 | 7.1640 | -114.2842 | 6.9782 | 191.1674 | 0.0048 | 0.0184 |
| 2024_09_20 22:00 | 3257647 | 7 | 11.0164 | 6.5239 | -115.4222 | 4.9605 | 35.3287 | 0.0061 | 0.0015 |
| 2024_09_20 22:00 | 3231702 | 8 | 10.5396 | 14.3016 | -114.1766 | 3.0406 | 56.1855 | 0.0018 | 0.0049 |
| 2024_09_20 22:00 | 3255990 | 9 | 16.1895 | 16.4345 | -117.4757 | 3.3029 | 34.2610 | 0.0028 | 0.0133 |
| 2024_09_20 22:00 | 3244158 | 10 | 8.6220 | 13.5185 | -116.2844 | 4.2639 | 44.6908 | 0.0140 | 0.0142 |
| 2024_09_20 22:00 | 3212648 | 11 | 11.0364 | 14.2888 | -115.5148 | 3.2671 | 22.0990 | 0.0071 | 0.0158 |
| 2024_09_20 22:00 | 3216828 | 12 | 8.1347 | 19.5384 | -116.9901 | 3.8593 | 50.9508 | 0.0110 | 0.0174 |
| 2024_09_20 22:00 | 3246151 | 13 | 13.9200 | 16.9457 | -115.6910 | 4.5529 | 31.3041 | 0.0058 | 0.0060 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415795_9C03EFEB | 152650 | 508 | -89.2 | 152650 | 438 | -97.9 | 152650 | 151 | -102.5 | 152650 | 399 |
| MR_1774415795_575D6F3C | 152650 | 508 | -92.5 | 152650 | 438 | -99.4 | 152650 | 151 | -101.6 | 152650 | 399 |
| MR_1774415795_376A6846 | 152650 | 508 | -90.7 | 152650 | 438 | -99.8 | 152650 | 151 | -102.6 | 152650 | 399 |
| MR_1774415795_D2BD3CA6 | 504990 | 523 | -93.7 | 504990 | 673 | -93.8 | 504990 | 957 | -97.1 | 504990 | 838 |
| MR_1774415795_1A2EA7E2 | 152650 | 508 | -89.4 | 152650 | 438 | -97.2 | 152650 | 151 | -101.0 | 152650 | 399 |
| MR_1774415795_C4B34BEA | 504990 | 523 | -96.1 | 504990 | 673 | -93.8 | 504990 | 957 | -96.2 | 504990 | 838 |
| MR_1774415795_7CA39080 | 152650 | 508 | -91.3 | 152650 | 438 | -97.7 | 152650 | 151 | -102.9 | 152650 | 399 |
| MR_1774415795_87AD25FF | 152650 | 508 | -92.0 | 152650 | 438 | -99.5 | 152650 | 151 | -102.5 | 152650 | 399 |

> *... 2개 열 생략 (전체 14열)*

---
