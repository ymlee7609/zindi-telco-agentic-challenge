# Track A 문제 분석 — train[850]~train[859]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[850] ~ train[859] (10개)

## 목차

1. [문제 850: `bf2e7ef1-fa6...`](#850) — single-answer, 정답: C14
2. [문제 851: `aef2ea69-2cc...`](#851) — single-answer, 정답: C14
3. [문제 852: `103fc0b3-0cd...`](#852) — single-answer, 정답: C18
4. [문제 853: `cdcf3ac0-4e2...`](#853) — single-answer, 정답: C1
5. [문제 854: `92c9fdfe-47f...`](#854) — single-answer, 정답: C8
6. [문제 855: `ed06a391-d3c...`](#855) — single-answer, 정답: C10
7. [문제 856: `4c18c218-a31...`](#856) — single-answer, 정답: C22
8. [문제 857: `1fbe97e5-9a8...`](#857) — single-answer, 정답: C15
9. [문제 858: `5d44b0b4-254...`](#858) — single-answer, 정답: C3
10. [문제 859: `d9c96983-9e8...`](#859) — single-answer, 정답: C22

---

### 문제 850: `bf2e7ef1-fa6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bf2e7ef1-fa6e-472e-a215-06fc9e19c97b` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[850] topology](images/train_0850.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3216829_1 and 3227207_2
- `C2`: Adjust the azimuth of 3227207_2 by 50 degrees
- `C3`: Increase A3 Offset threshold for 3266361_4
- `C4`: Decrease A3 Offset threshold for 3227207_2
- `C5`: Decrease transmission power for 3227207_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266361_4
- `C7`: Add neighbor relationship between 3266361_4 and 3227207_2
- `C8`: Adjust the azimuth of 3266361_4 by 50 degrees
- `C9`: Increase transmission power for 3227207_2
- `C10`: Increase A3 Offset threshold for 3227207_2
- `C11`: Check test server and transmission issues
- `C12`: Decrease transmission power for 3266361_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266361_4
- `C14`: Insufficient data; more data is needed for judgment. **← 정답**
- `C15`: Press down the tilt angle  of 3227207_2 by 4 degrees
- `C16`: Decrease A3 Offset threshold for 3266361_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227207_2
- `C18`: Press down the tilt angle of 3266361_4 by 7 degrees
- `C19`: Lift the tilt angle  of 3227207_2 by 4 degrees
- `C20`: Lift the tilt angle of 3266361_4 by 7 degrees
- `C21`: Increase transmission power for 3266361_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227207_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.938 | MS1 | 121.4656721922 | 31.1446341428 | 166 | 504990 | -89.41 | 14.71 | 345.78 | 0.20 | 2.10 | 1574 |
| 2024-09-20 22:21:32.278 | MS1 | 121.4656677343 | 31.1446228310 | 166 | 504990 | -88.90 | 15.24 | 456.84 | 0.19 | 2.44 | 1565 |
| 2024-09-20 22:21:33.418 | MS1 | 121.4656635010 | 31.1446367466 | 166 | 504990 | -87.43 | 12.14 | 527.19 | 0.01 | 2.75 | 1578 |
| 2024-09-20 22:21:34.476 | MS1 | 121.4656716196 | 31.1446336402 | 166 | 504990 | -91.87 | 16.16 | 88.80 | 0.15 | 2.26 | 1592 |
| 2024-09-20 22:21:35.128 | MS1 | 121.4656655722 | 31.1446340572 | 166 | 504990 | -87.63 | 14.41 | 63.26 | 0.18 | 2.67 | 1582 |
| 2024-09-20 22:21:36.532 | MS1 | 121.4656665132 | 31.1446329112 | 166 | 504990 | -90.36 | 15.59 | 98.93 | 0.10 | 2.77 | 1564 |
| 2024-09-20 22:21:37.545 | MS1 | 121.4656660776 | 31.1446283893 | 166 | 504990 | -92.37 | 11.12 | 58.72 | 0.10 | 2.20 | 1598 |
| 2024-09-20 22:21:38.501 | MS1 | 121.4656752971 | 31.1446249896 | 166 | 504990 | -93.60 | 7.84 | 79.97 | 0.01 | 2.09 | 1568 |
| 2024-09-20 22:21:39.467 | MS1 | 121.4656606128 | 31.1446278997 | 166 | 504990 | -91.96 | 10.62 | 78.75 | 0.18 | 2.01 | 1566 |
| 2024-09-20 22:21:40.227 | MS1 | 121.4656677584 | 31.1446274918 | 166 | 504990 | -93.38 | 9.65 | 591.98 | 0.19 | 2.27 | 1597 |
| 2024-09-20 22:21:41.373 | MS1 | 121.4656580507 | 31.1446213615 | 166 | 504990 | -93.43 | 10.47 | 483.53 | 0.07 | 2.56 | 1579 |
| 2024-09-20 22:21:42.513 | MS1 | 121.4656725892 | 31.1446257628 | 166 | 504990 | -92.58 | 7.32 | 457.25 | 0.04 | 2.44 | 1591 |

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
| 3216829 | 1 | 121.4698628768 | 31.1474626819 | 37 | 5 | 4 | 45.2 | TDD | 793 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3227207 | 2 | 121.4739339625 | 31.1530886122 | 357 | 2 | 8 | 33.5 | TDD | 323 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3242741 | 3 | 121.4693024229 | 31.1505207455 | 22 | 5 | 12 | 31.2 | TDD | 292 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3266361 | 4 | 121.4705556855 | 31.1461030683 | 147 | 3 | 7 | 34.7 | TDD | 166 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.519 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.540 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.686 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.686 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.363 | NREventA3 | measId:2;ServCellPCI:270;Se... |
| 2024-09-20 22:21:38.603 | NRHandoverAttempt | SourcePCI:270;SourceNR-ARFC... |
| 2024-09-20 22:21:38.651 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.661 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.796 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.796 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3216829 | 1 | 90.6407 | 88.5607 | -116.6220 | 7.2075 | 168.3614 | 0.0173 | 0.0105 |
| 2024_09_19 22:00 | 3227207 | 2 | 81.5696 | 90.4844 | -114.5048 | 13.8621 | 93.0377 | 0.0070 | 0.0162 |
| 2024_09_19 22:00 | 3242741 | 3 | 82.9111 | 75.8390 | -115.8204 | 9.6331 | 154.9043 | 0.0149 | 0.0176 |
| 2024_09_19 22:00 | 3266361 | 4 | 90.1408 | 87.1345 | -114.2537 | 17.5049 | 176.3966 | 0.0146 | 0.0073 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415076_B1DCBAB8 | 504990 | 166 | -93.2 | 504990 | 323 | -93.0 | 504990 | 793 | -101.9 | 504990 | 292 |
| MR_1774415076_F5A6679A | 504990 | 166 | -90.0 | 504990 | 323 | -92.6 | 504990 | 793 | -102.1 | 504990 | 292 |
| MR_1774415076_8684D068 | 504990 | 166 | -92.8 | 504990 | 323 | -94.0 | 504990 | 793 | -100.5 | 504990 | 292 |
| MR_1774415076_23E46D26 | 504990 | 166 | -89.9 | 504990 | 323 | -92.7 | 504990 | 793 | -102.1 | 504990 | 292 |
| MR_1774415076_99D911BD | 504990 | 166 | -90.6 | 504990 | 323 | -91.9 | 504990 | 793 | -101.8 | 504990 | 292 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 851: `aef2ea69-2cc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `aef2ea69-2cc7-4389-98c7-216314d0c3d2` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[851] topology](images/train_0851.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3246522_4
- `C2`: Lift the tilt angle  of 3246522_4 by 10 degrees
- `C3`: Add neighbor relationship between 3272887_1 and 3246522_4
- `C4`: Adjust the azimuth of 3246522_4 by 50 degrees
- `C5`: Press down the tilt angle  of 3246522_4 by 10 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272887_1
- `C7`: Increase transmission power for 3246522_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272887_1
- `C9`: Increase transmission power for 3272887_1
- `C10`: Decrease A3 Offset threshold for 3272887_1
- `C11`: Increase A3 Offset threshold for 3272887_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246522_4
- `C13`: Adjust the azimuth of 3272887_1 by 14 degrees
- `C14`: Insufficient data; more data is needed for judgment. **← 정답**
- `C15`: Increase A3 Offset threshold for 3246522_4
- `C16`: Check test server and transmission issues
- `C17`: Press down the tilt angle of 3272887_1 by 3 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246522_4
- `C19`: Add neighbor relationship between 3211766_2 and 3246522_4
- `C20`: Lift the tilt angle of 3272887_1 by 3 degrees
- `C21`: Decrease transmission power for 3272887_1
- `C22`: Decrease transmission power for 3246522_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.762 | MS1 | 121.4656669535 | 31.1446227028 | 786 | 504990 | -87.75 | 13.54 | 378.56 | 0.16 | 2.66 | 1567 |
| 2024-09-20 22:21:32.190 | MS1 | 121.4656764187 | 31.1446305287 | 786 | 504990 | -86.97 | 17.77 | 309.95 | 0.15 | 2.91 | 1578 |
| 2024-09-20 22:21:33.550 | MS1 | 121.4656662287 | 31.1446313333 | 786 | 504990 | -90.62 | 14.38 | 394.45 | 0.02 | 2.31 | 1571 |
| 2024-09-20 22:21:34.546 | MS1 | 121.4656656589 | 31.1446256627 | 786 | 504990 | -87.07 | 14.52 | 86.66 | 0.15 | 2.15 | 1588 |
| 2024-09-20 22:21:35.718 | MS1 | 121.4656632232 | 31.1446350180 | 786 | 504990 | -89.77 | 13.86 | 65.79 | 0.19 | 2.90 | 1592 |
| 2024-09-20 22:21:36.993 | MS1 | 121.4656700186 | 31.1446259920 | 786 | 504990 | -88.88 | 12.24 | 73.17 | 0.11 | 2.34 | 1599 |
| 2024-09-20 22:21:37.514 | MS1 | 121.4656594016 | 31.1446251373 | 786 | 504990 | -91.10 | 9.71 | 79.11 | 0.13 | 2.30 | 1582 |
| 2024-09-20 22:21:38.606 | MS1 | 121.4656619152 | 31.1446373133 | 786 | 504990 | -90.51 | 8.83 | 70.02 | 0.07 | 2.01 | 1575 |
| 2024-09-20 22:21:39.701 | MS1 | 121.4656580580 | 31.1446254781 | 786 | 504990 | -90.01 | 11.43 | 69.58 | 0.14 | 2.68 | 1584 |
| 2024-09-20 22:21:40.522 | MS1 | 121.4656624810 | 31.1446257445 | 786 | 504990 | -89.70 | 8.03 | 532.77 | 0.14 | 2.03 | 1579 |
| 2024-09-20 22:21:41.909 | MS1 | 121.4656713426 | 31.1446304410 | 786 | 504990 | -90.14 | 11.55 | 577.63 | 0.18 | 2.53 | 1561 |
| 2024-09-20 22:21:42.309 | MS1 | 121.4656634473 | 31.1446375958 | 786 | 504990 | -89.99 | 9.13 | 344.62 | 0.07 | 2.30 | 1569 |

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
| 3211766 | 2 | 121.4696629389 | 31.1451388687 | 270 | 2 | 10 | 35.5 | TDD | 762 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3246522 | 4 | 121.4754346352 | 31.1518039735 | 66 | 14 | 5 | 40.0 | TDD | 658 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3272887 | 1 | 121.4756219638 | 31.1478182709 | 264 | 1 | 0 | 29.5 | TDD | 786 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3279150 | 3 | 121.4730169160 | 31.1452336872 | 312 | 10 | 8 | 40.0 | TDD | 612 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.178 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.202 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.303 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.303 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.990 | NREventA3 | measId:2;ServCellPCI:983;Se... |
| 2024-09-20 22:21:38.230 | NRHandoverAttempt | SourcePCI:983;SourceNR-ARFC... |
| 2024-09-20 22:21:38.268 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.283 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.404 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.404 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3272887 | 1 | 92.9995 | 80.2163 | -115.8560 | 15.9204 | 175.0451 | 0.0180 | 0.0029 |
| 2024_09_19 22:00 | 3211766 | 2 | 81.8621 | 88.8185 | -115.6121 | 13.0057 | 162.4179 | 0.0023 | 0.0013 |
| 2024_09_19 22:00 | 3279150 | 3 | 85.1336 | 77.2895 | -117.5622 | 10.0866 | 106.2496 | 0.0114 | 0.0168 |
| 2024_09_19 22:00 | 3246522 | 4 | 88.3099 | 90.3090 | -116.1027 | 7.6275 | 168.1288 | 0.0131 | 0.0037 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417060_2A137B07 | 504990 | 786 | -88.3 | 504990 | 658 | -90.3 | 504990 | 762 | -99.7 | 504990 | 612 |
| MR_1774417060_FCC1804A | 504990 | 786 | -85.6 | 504990 | 658 | -93.6 | 504990 | 762 | -99.7 | 504990 | 612 |
| MR_1774417060_B4BA7130 | 504990 | 786 | -88.3 | 504990 | 658 | -93.9 | 504990 | 762 | -101.1 | 504990 | 612 |
| MR_1774417060_DE6B3151 | 504990 | 786 | -85.2 | 504990 | 658 | -92.9 | 504990 | 762 | -101.3 | 504990 | 612 |
| MR_1774417060_A28919FB | 504990 | 786 | -89.0 | 504990 | 658 | -94.0 | 504990 | 762 | -101.0 | 504990 | 612 |
| MR_1774417060_5E9D7E57 | 504990 | 786 | -86.3 | 504990 | 658 | -91.2 | 504990 | 762 | -100.7 | 504990 | 612 |
| MR_1774417060_9F6FAFB1 | 504990 | 786 | -85.4 | 504990 | 658 | -91.6 | 504990 | 762 | -98.9 | 504990 | 612 |
| MR_1774417060_3057F74B | 504990 | 786 | -85.6 | 504990 | 658 | -92.9 | 504990 | 762 | -97.8 | 504990 | 612 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 852: `103fc0b3-0cd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `103fc0b3-0cd3-4e00-aebd-2ee33c15a485` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[852] topology](images/train_0852.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3220325_2 by 4 degrees
- `C2`: Adjust the azimuth of 3220325_2 by 50 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267108_3
- `C4`: Increase A3 Offset threshold for 3267108_3
- `C5`: Press down the tilt angle  of 3220325_2 by 4 degrees
- `C6`: Add neighbor relationship between 3267108_3 and 3220325_2
- `C7`: Decrease transmission power for 3267108_3
- `C8`: Increase transmission power for 3267108_3
- `C9`: Lift the tilt angle of 3267108_3 by 10 degrees
- `C10`: Increase transmission power for 3220325_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267108_3
- `C12`: Press down the tilt angle of 3267108_3 by 10 degrees
- `C13`: Add neighbor relationship between 3211277_4 and 3220325_2
- `C14`: Adjust the azimuth of 3267108_3 by 50 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220325_2
- `C16`: Decrease transmission power for 3220325_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220325_2
- `C18`: Check test server and transmission issues **← 정답**
- `C19`: Decrease A3 Offset threshold for 3267108_3
- `C20`: Decrease A3 Offset threshold for 3220325_2
- `C21`: Increase A3 Offset threshold for 3220325_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.221 | MS1 | 121.4656683398 | 31.1446262022 | 242 | 504990 | -89.30 | 17.84 | 596.12 | 0.09 | 2.79 | 1574 |
| 2024-09-20 22:21:32.317 | MS1 | 121.4656718325 | 31.1446272156 | 242 | 504990 | -89.67 | 16.08 | 491.71 | 0.07 | 2.05 | 1577 |
| 2024-09-20 22:21:33.103 | MS1 | 121.4656636141 | 31.1446228569 | 242 | 504990 | -89.52 | 14.80 | 376.97 | 0.08 | 2.79 | 1596 |
| 2024-09-20 22:21:34.511 | MS1 | 121.4656756327 | 31.1446259526 | 242 | 504990 | -89.80 | 15.82 | 103.44 | 0.16 | 2.77 | 450 |
| 2024-09-20 22:21:35.845 | MS1 | 121.4656763987 | 31.1446264028 | 242 | 504990 | -86.57 | 15.49 | 89.79 | 0.20 | 2.60 | 443 |
| 2024-09-20 22:21:36.194 | MS1 | 121.4656723423 | 31.1446374344 | 242 | 504990 | -88.27 | 15.64 | 62.78 | 0.16 | 2.28 | 355 |
| 2024-09-20 22:21:37.748 | MS1 | 121.4656736028 | 31.1446335285 | 242 | 504990 | -93.02 | 9.81 | 80.53 | 0.14 | 2.07 | 406 |
| 2024-09-20 22:21:38.772 | MS1 | 121.4656773153 | 31.1446277857 | 242 | 504990 | -93.01 | 12.96 | 99.06 | 0.07 | 2.33 | 366 |
| 2024-09-20 22:21:39.676 | MS1 | 121.4656598206 | 31.1446360653 | 242 | 504990 | -92.99 | 12.00 | 86.30 | 0.13 | 2.19 | 491 |
| 2024-09-20 22:21:40.227 | MS1 | 121.4656626312 | 31.1446245349 | 242 | 504990 | -89.96 | 8.86 | 353.95 | 0.02 | 2.42 | 1576 |
| 2024-09-20 22:21:41.123 | MS1 | 121.4656595786 | 31.1446189612 | 242 | 504990 | -91.81 | 8.92 | 355.62 | 0.03 | 2.75 | 1600 |
| 2024-09-20 22:21:42.889 | MS1 | 121.4656643245 | 31.1446310887 | 242 | 504990 | -90.91 | 11.44 | 505.11 | 0.14 | 2.77 | 1588 |

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
| 3211277 | 4 | 121.4651984109 | 31.1445519299 | 202 | 13 | 7 | 34.2 | TDD | 438 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3219688 | 1 | 121.4756996767 | 31.1452517784 | 166 | 4 | 11 | 18.5 | TDD | 824 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3220325 | 2 | 121.4744319177 | 31.1512480105 | 46 | 3 | 0 | 20.9 | TDD | 809 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3267108 | 3 | 121.4708669694 | 31.1457631060 | 44 | 13 | 12 | 38.3 | TDD | 242 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.098 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.113 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.239 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.239 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.908 | NREventA3 | measId:2;ServCellPCI:395;Se... |
| 2024-09-20 22:21:38.148 | NRHandoverAttempt | SourcePCI:395;SourceNR-ARFC... |
| 2024-09-20 22:21:38.184 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.196 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.342 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.342 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219688 | 1 | 19.6716 | 19.9926 | -115.7863 | 12.5309 | 85.7659 | 0.0154 | 0.0011 |
| 2024_09_20 22:00 | 3220325 | 2 | 7.4426 | 15.5671 | -114.9122 | 9.2092 | 85.4075 | 0.0164 | 0.0048 |
| 2024_09_20 22:00 | 3267108 | 3 | 15.7903 | 16.4128 | -115.3479 | 8.5489 | 175.0311 | 0.0110 | 0.0200 |
| 2024_09_20 22:00 | 3211277 | 4 | 13.6170 | 5.0947 | -116.3486 | 10.6276 | 166.7526 | 0.0180 | 0.0056 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413758_42016C99 | 504990 | 242 | -87.4 | 504990 | 809 | -88.3 | 504990 | 438 | -94.6 | 504990 | 824 |
| MR_1774413758_A83CF1B3 | 504990 | 242 | -87.8 | 504990 | 809 | -85.6 | 504990 | 438 | -92.6 | 504990 | 824 |
| MR_1774413758_08776B15 | 504990 | 242 | -88.0 | 504990 | 809 | -88.0 | 504990 | 438 | -91.6 | 504990 | 824 |
| MR_1774413758_CBC15169 | 504990 | 242 | -84.6 | 504990 | 809 | -88.8 | 504990 | 438 | -94.7 | 504990 | 824 |
| MR_1774413758_0AA7D270 | 504990 | 242 | -87.5 | 504990 | 809 | -85.8 | 504990 | 438 | -92.1 | 504990 | 824 |
| MR_1774413758_6703188A | 504990 | 242 | -87.0 | 504990 | 809 | -86.1 | 504990 | 438 | -91.5 | 504990 | 824 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 853: `cdcf3ac0-4e2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cdcf3ac0-4e22-4381-bd8c-145f21faef6f` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Decrease A3 Offset threshold for 3258202_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[853] topology](images/train_0853.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3258202_4 **← 정답**
- `C2`: Press down the tilt angle  of 3217032_1 by 10 degrees
- `C3`: Decrease A3 Offset threshold for 3217032_1
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Increase A3 Offset threshold for 3258202_4
- `C6`: Lift the tilt angle of 3258202_4 by 10 degrees
- `C7`: Decrease transmission power for 3217032_1
- `C8`: Increase transmission power for 3217032_1
- `C9`: Add neighbor relationship between 3265711_3 and 3217032_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258202_4
- `C11`: Increase transmission power for 3258202_4
- `C12`: Decrease transmission power for 3258202_4
- `C13`: Increase A3 Offset threshold for 3217032_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217032_1
- `C15`: Check test server and transmission issues
- `C16`: Lift the tilt angle  of 3217032_1 by 10 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217032_1
- `C18`: Press down the tilt angle of 3258202_4 by 10 degrees
- `C19`: Adjust the azimuth of 3258202_4 by 50 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258202_4
- `C21`: Add neighbor relationship between 3258202_4 and 3217032_1
- `C22`: Adjust the azimuth of 3217032_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.280 | MS1 | 121.4656744254 | 31.1446198312 | 389 | 504990 | -80.85 | 17.20 | 485.22 | 0.14 | 2.27 | 1591 |
| 2024-09-20 22:21:32.158 | MS1 | 121.4656692219 | 31.1446218888 | 389 | 504990 | -77.17 | 14.68 | 533.72 | 0.20 | 2.34 | 1588 |
| 2024-09-20 22:21:33.751 | MS1 | 121.4656768949 | 31.1446266261 | 389 | 504990 | -80.39 | 14.54 | 428.58 | 0.06 | 2.34 | 1566 |
| 2024-09-20 22:21:34.528 | MS1 | 121.4656641203 | 31.1446368346 | 389 | 504990 | -90.41 | -3.85 | 75.79 | 0.07 | 1.12 | 1580 |
| 2024-09-20 22:21:35.693 | MS1 | 121.4656687849 | 31.1446240617 | 389 | 504990 | -83.19 | -2.32 | 36.79 | 0.12 | 1.49 | 1578 |
| 2024-09-20 22:21:36.173 | MS1 | 121.4656675984 | 31.1446284293 | 389 | 504990 | -88.92 | -3.71 | 43.08 | 0.20 | 1.09 | 1584 |
| 2024-09-20 22:21:37.300 | MS1 | 121.4656676561 | 31.1446219410 | 389 | 504990 | -90.22 | -0.69 | 59.58 | 0.17 | 1.09 | 1573 |
| 2024-09-20 22:21:38.597 | MS1 | 121.4656625349 | 31.1446279537 | 389 | 504990 | -83.67 | -0.93 | 60.12 | 0.18 | 1.14 | 1586 |
| 2024-09-20 22:21:39.806 | MS1 | 121.4656639793 | 31.1446183153 | 708 | 504990 | -75.75 | 12.47 | 169.23 | 0.06 | 1.32 | 1583 |
| 2024-09-20 22:21:40.251 | MS1 | 121.4656672000 | 31.1446344086 | 708 | 504990 | -84.14 | 16.25 | 388.94 | 0.10 | 2.70 | 1598 |
| 2024-09-20 22:21:41.948 | MS1 | 121.4656595899 | 31.1446336351 | 708 | 504990 | -78.17 | 17.00 | 359.85 | 0.12 | 2.32 | 1560 |
| 2024-09-20 22:21:42.854 | MS1 | 121.4656762047 | 31.1446236546 | 708 | 504990 | -84.99 | 15.20 | 557.47 | 0.10 | 2.63 | 1578 |

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
| 3217032 | 1 | 121.4685639947 | 31.1464380874 | 142 | 9 | 9 | 18.0 | TDD | 708 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3258202 | 4 | 121.4665561027 | 31.1553155260 | 335 | 15 | 12 | 30.1 | TDD | 389 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3265711 | 3 | 121.4669160487 | 31.1502616552 | 92 | 13 | 0 | 33.2 | TDD | 13 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3277441 | 2 | 121.4750918531 | 31.1440120796 | 201 | 7 | 11 | 28.7 | TDD | 452 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.271 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.295 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.444 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.444 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.162 | NREventA3 | measId:2;ServCellPCI:894;Se... |
| 2024-09-20 22:21:38.402 | NRHandoverAttempt | SourcePCI:894;SourceNR-ARFC... |
| 2024-09-20 22:21:38.443 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.453 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.581 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.581 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217032 | 1 | 16.1783 | 5.0104 | -117.0978 | 15.9636 | 154.1633 | 0.0131 | 0.0052 |
| 2024_09_20 22:00 | 3277441 | 2 | 17.9260 | 11.1137 | -115.9784 | 7.9732 | 115.8096 | 0.0174 | 0.0002 |
| 2024_09_20 22:00 | 3265711 | 3 | 14.9051 | 8.9868 | -114.9604 | 11.3989 | 181.5524 | 0.0012 | 0.0132 |
| 2024_09_20 22:00 | 3258202 | 4 | 8.6482 | 16.2509 | -114.0851 | 17.3423 | 183.7645 | 0.0049 | 0.1312 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412522_AD7DD1F0 | 504990 | 389 | -90.5 | 504990 | 708 | -84.0 | 504990 | 13 | -84.8 | 504990 | 452 |
| MR_1774412522_7B38059D | 504990 | 389 | -90.5 | 504990 | 708 | -86.3 | 504990 | 13 | -85.8 | 504990 | 452 |
| MR_1774412522_3A470F55 | 504990 | 708 | -87.2 | 504990 | 389 | -90.2 | 504990 | 13 | -86.2 | 504990 | 452 |
| MR_1774412522_6D2B2A17 | 504990 | 708 | -83.7 | 504990 | 389 | -89.1 | 504990 | 13 | -87.9 | 504990 | 452 |
| MR_1774412522_88215CD5 | 504990 | 708 | -87.4 | 504990 | 389 | -89.7 | 504990 | 13 | -84.2 | 504990 | 452 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 854: `92c9fdfe-47f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `92c9fdfe-47f3-4c9f-9d7d-d6f84665c22b` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[854] topology](images/train_0854.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3244382_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213110_2
- `C3`: Increase A3 Offset threshold for 3244382_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244382_1
- `C5`: Decrease transmission power for 3213110_2
- `C6`: Lift the tilt angle  of 3213110_2 by 10 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244382_1
- `C8`: Insufficient data; more data is needed for judgment. **← 정답**
- `C9`: Decrease A3 Offset threshold for 3244382_1
- `C10`: Press down the tilt angle of 3244382_1 by 2 degrees
- `C11`: Increase transmission power for 3213110_2
- `C12`: Adjust the azimuth of 3213110_2 by 50 degrees
- `C13`: Add neighbor relationship between 3240895_3 and 3213110_2
- `C14`: Lift the tilt angle of 3244382_1 by 2 degrees
- `C15`: Decrease A3 Offset threshold for 3213110_2
- `C16`: Increase transmission power for 3244382_1
- `C17`: Add neighbor relationship between 3244382_1 and 3213110_2
- `C18`: Adjust the azimuth of 3244382_1 by 50 degrees
- `C19`: Press down the tilt angle  of 3213110_2 by 10 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213110_2
- `C21`: Increase A3 Offset threshold for 3213110_2
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.256 | MS1 | 121.4656608852 | 31.1446207634 | 210 | 504990 | -91.06 | 13.90 | 534.33 | 0.09 | 2.47 | 1561 |
| 2024-09-20 22:21:32.405 | MS1 | 121.4656668095 | 31.1446360574 | 210 | 504990 | -85.80 | 13.20 | 394.31 | 0.14 | 2.80 | 1580 |
| 2024-09-20 22:21:33.176 | MS1 | 121.4656678644 | 31.1446343693 | 210 | 504990 | -88.80 | 17.88 | 515.97 | 0.15 | 2.95 | 1569 |
| 2024-09-20 22:21:34.152 | MS1 | 121.4656636543 | 31.1446319003 | 210 | 504990 | -89.31 | 17.11 | 63.42 | 0.04 | 2.07 | 1580 |
| 2024-09-20 22:21:35.891 | MS1 | 121.4656622474 | 31.1446239483 | 210 | 504990 | -90.48 | 15.58 | 56.72 | 0.08 | 2.97 | 1597 |
| 2024-09-20 22:21:36.150 | MS1 | 121.4656754719 | 31.1446312982 | 210 | 504990 | -89.72 | 14.67 | 90.63 | 0.03 | 2.04 | 1599 |
| 2024-09-20 22:21:37.994 | MS1 | 121.4656763824 | 31.1446367656 | 210 | 504990 | -92.33 | 12.03 | 73.39 | 0.10 | 2.86 | 1591 |
| 2024-09-20 22:21:38.246 | MS1 | 121.4656679952 | 31.1446247698 | 210 | 504990 | -93.60 | 9.87 | 107.62 | 0.20 | 2.03 | 1565 |
| 2024-09-20 22:21:39.586 | MS1 | 121.4656648769 | 31.1446210745 | 210 | 504990 | -91.01 | 11.76 | 65.14 | 0.09 | 2.94 | 1592 |
| 2024-09-20 22:21:40.498 | MS1 | 121.4656650132 | 31.1446284689 | 210 | 504990 | -90.61 | 7.74 | 458.29 | 0.10 | 2.74 | 1591 |
| 2024-09-20 22:21:41.417 | MS1 | 121.4656662058 | 31.1446251296 | 210 | 504990 | -91.43 | 9.14 | 506.65 | 0.13 | 2.63 | 1560 |
| 2024-09-20 22:21:42.948 | MS1 | 121.4656740206 | 31.1446337925 | 210 | 504990 | -91.66 | 11.47 | 348.40 | 0.11 | 2.89 | 1575 |

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
| 3213110 | 2 | 121.4667900842 | 31.1515525604 | 359 | 14 | 6 | 39.4 | TDD | 127 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3240895 | 3 | 121.4652542794 | 31.1487270482 | 274 | 4 | 3 | 22.0 | TDD | 358 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3244382 | 1 | 121.4695931194 | 31.1488305032 | 335 | 0 | 5 | 23.8 | TDD | 210 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3249180 | 4 | 121.4656374765 | 31.1507223430 | 101 | 0 | 5 | 43.0 | TDD | 247 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.077 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.102 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.213 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.213 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.949 | NREventA3 | measId:2;ServCellPCI:874;Se... |
| 2024-09-20 22:21:38.189 | NRHandoverAttempt | SourcePCI:874;SourceNR-ARFC... |
| 2024-09-20 22:21:38.230 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.245 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.392 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.392 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3244382 | 1 | 88.8023 | 79.3259 | -116.7164 | 18.7344 | 194.9721 | 0.0027 | 0.0153 |
| 2024_09_19 22:00 | 3213110 | 2 | 84.8031 | 86.1752 | -114.6917 | 18.0399 | 143.8083 | 0.0136 | 0.0107 |
| 2024_09_19 22:00 | 3240895 | 3 | 91.4239 | 79.2522 | -116.4660 | 19.2532 | 163.2113 | 0.0132 | 0.0059 |
| 2024_09_19 22:00 | 3249180 | 4 | 89.6099 | 85.5055 | -114.3252 | 5.2539 | 159.8733 | 0.0009 | 0.0109 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415793_65DA9834 | 504990 | 210 | -89.9 | 504990 | 127 | -94.5 | 504990 | 358 | -98.1 | 504990 | 247 |
| MR_1774415793_CDEDA8B3 | 504990 | 210 | -89.9 | 504990 | 127 | -91.4 | 504990 | 358 | -99.8 | 504990 | 247 |
| MR_1774415793_E922E593 | 504990 | 210 | -90.5 | 504990 | 127 | -92.7 | 504990 | 358 | -98.1 | 504990 | 247 |
| MR_1774415793_E4B73112 | 504990 | 210 | -90.0 | 504990 | 127 | -93.7 | 504990 | 358 | -97.3 | 504990 | 247 |
| MR_1774415793_6178B40E | 504990 | 210 | -91.1 | 504990 | 127 | -94.2 | 504990 | 358 | -99.2 | 504990 | 247 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 855: `ed06a391-d3c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ed06a391-d3cf-4987-9d3b-c672aa65129c` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease A3 Offset threshold for 3243636_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[855] topology](images/train_0855.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3243636_2 by 7 degrees
- `C2`: Decrease transmission power for 3243636_2
- `C3`: Increase A3 Offset threshold for 3228621_4
- `C4`: Decrease transmission power for 3228621_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228621_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228621_4
- `C7`: Lift the tilt angle  of 3228621_4 by 7 degrees
- `C8`: Increase transmission power for 3228621_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243636_2
- `C10`: Decrease A3 Offset threshold for 3243636_2 **← 정답**
- `C11`: Add neighbor relationship between 3243636_2 and 3228621_4
- `C12`: Adjust the azimuth of 3228621_4 by 35 degrees
- `C13`: Increase A3 Offset threshold for 3243636_2
- `C14`: Check test server and transmission issues
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease A3 Offset threshold for 3228621_4
- `C17`: Add neighbor relationship between 3218081_1 and 3228621_4
- `C18`: Press down the tilt angle  of 3228621_4 by 7 degrees
- `C19`: Increase transmission power for 3243636_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243636_2
- `C21`: Press down the tilt angle of 3243636_2 by 7 degrees
- `C22`: Adjust the azimuth of 3243636_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.787 | MS1 | 121.4656618127 | 31.1446375398 | 273 | 504990 | -76.10 | 16.00 | 584.01 | 0.16 | 2.85 | 1594 |
| 2024-09-20 22:21:32.509 | MS1 | 121.4656581526 | 31.1446273586 | 273 | 504990 | -75.07 | 13.45 | 471.04 | 0.11 | 2.62 | 1581 |
| 2024-09-20 22:21:33.528 | MS1 | 121.4656615117 | 31.1446344521 | 273 | 504990 | -83.44 | 13.39 | 310.74 | 0.20 | 2.25 | 1573 |
| 2024-09-20 22:21:34.395 | MS1 | 121.4656611756 | 31.1446321824 | 273 | 504990 | -88.92 | -2.79 | 49.38 | 0.12 | 1.35 | 1592 |
| 2024-09-20 22:21:35.626 | MS1 | 121.4656627194 | 31.1446182649 | 273 | 504990 | -88.50 | -2.53 | 28.20 | 0.02 | 1.20 | 1571 |
| 2024-09-20 22:21:36.243 | MS1 | 121.4656711964 | 31.1446228884 | 273 | 504990 | -92.67 | -0.16 | 67.52 | 0.01 | 1.50 | 1586 |
| 2024-09-20 22:21:37.147 | MS1 | 121.4656701683 | 31.1446191181 | 273 | 504990 | -86.23 | -3.08 | 42.08 | 0.14 | 1.11 | 1581 |
| 2024-09-20 22:21:38.251 | MS1 | 121.4656767525 | 31.1446348316 | 273 | 504990 | -86.93 | -3.69 | 50.15 | 0.14 | 1.12 | 1599 |
| 2024-09-20 22:21:39.182 | MS1 | 121.4656648347 | 31.1446364506 | 263 | 504990 | -82.08 | 14.10 | 148.17 | 0.08 | 1.07 | 1565 |
| 2024-09-20 22:21:40.249 | MS1 | 121.4656664525 | 31.1446256214 | 263 | 504990 | -75.98 | 15.52 | 485.92 | 0.14 | 2.45 | 1596 |
| 2024-09-20 22:21:41.902 | MS1 | 121.4656608410 | 31.1446352583 | 263 | 504990 | -79.21 | 12.85 | 303.95 | 0.00 | 2.75 | 1576 |
| 2024-09-20 22:21:42.817 | MS1 | 121.4656679813 | 31.1446203829 | 263 | 504990 | -82.42 | 15.65 | 464.02 | 0.04 | 2.28 | 1591 |

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
| 3218081 | 1 | 121.4669333238 | 31.1510807669 | 13 | 8 | 6 | 42.3 | TDD | 752 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3228621 | 4 | 121.4684359678 | 31.1488385782 | 174 | 5 | 11 | 16.8 | TDD | 263 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3243636 | 2 | 121.4650427031 | 31.1479452653 | 95 | 4 | 7 | 21.7 | TDD | 273 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3250424 | 3 | 121.4757400172 | 31.1457896288 | 115 | 3 | 5 | 17.9 | TDD | 328 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.258 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.363 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.363 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.042 | NREventA3 | measId:2;ServCellPCI:280;Se... |
| 2024-09-20 22:21:38.282 | NRHandoverAttempt | SourcePCI:280;SourceNR-ARFC... |
| 2024-09-20 22:21:38.316 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.328 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.475 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.475 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218081 | 1 | 9.7878 | 18.8448 | -116.3645 | 11.1141 | 173.1481 | 0.0013 | 0.0105 |
| 2024_09_20 22:00 | 3243636 | 2 | 8.0750 | 10.7115 | -114.8339 | 13.9447 | 110.0849 | 0.0178 | 0.1109 |
| 2024_09_20 22:00 | 3250424 | 3 | 17.4463 | 13.3359 | -115.6867 | 14.8459 | 82.0156 | 0.0154 | 0.0190 |
| 2024_09_20 22:00 | 3228621 | 4 | 11.4519 | 16.7609 | -117.4409 | 18.1222 | 185.0555 | 0.0150 | 0.0003 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415630_2153FD32 | 504990 | 273 | -88.5 | 504990 | 263 | -82.2 | 504990 | 752 | -84.1 | 504990 | 328 |
| MR_1774415630_8D32E7B1 | 504990 | 273 | -87.7 | 504990 | 263 | -81.6 | 504990 | 752 | -86.5 | 504990 | 328 |
| MR_1774415630_50B3A620 | 504990 | 273 | -87.0 | 504990 | 263 | -84.9 | 504990 | 752 | -86.1 | 504990 | 328 |
| MR_1774415630_5FC2EBDB | 504990 | 273 | -87.9 | 504990 | 263 | -81.8 | 504990 | 752 | -84.6 | 504990 | 328 |
| MR_1774415630_E917F609 | 504990 | 273 | -89.7 | 504990 | 263 | -83.9 | 504990 | 752 | -84.5 | 504990 | 328 |
| MR_1774415630_E23073F5 | 504990 | 263 | -81.8 | 504990 | 273 | -88.7 | 504990 | 752 | -84.4 | 504990 | 328 |
| MR_1774415630_61177AC4 | 504990 | 273 | -88.5 | 504990 | 263 | -83.7 | 504990 | 752 | -83.7 | 504990 | 328 |
| MR_1774415630_23259B76 | 504990 | 273 | -89.0 | 504990 | 263 | -81.7 | 504990 | 752 | -86.7 | 504990 | 328 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 856: `4c18c218-a31...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4c18c218-a318-4186-9a43-52bf0f396971` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Lift the tilt angle  of 3264164_4 by 5 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[856] topology](images/train_0856.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease A3 Offset threshold for 3277239_3
- `C3`: Press down the tilt angle of 3277239_3 by 2 degrees
- `C4`: Increase A3 Offset threshold for 3277239_3
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Add neighbor relationship between 3277239_3 and 3270871_1
- `C7`: Increase transmission power for 3270871_1
- `C8`: Decrease transmission power for 3277239_3
- `C9`: Decrease A3 Offset threshold for 3270871_1
- `C10`: Add neighbor relationship between 3264164_4 and 3270871_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270871_1
- `C12`: Adjust the azimuth of 3277239_3 by 48 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277239_3
- `C14`: Adjust the azimuth of 3264164_4 by 28 degrees
- `C15`: Increase A3 Offset threshold for 3270871_1
- `C16`: Lift the tilt angle of 3277239_3 by 2 degrees
- `C17`: Press down the tilt angle  of 3264164_4 by 5 degrees
- `C18`: Increase transmission power for 3277239_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277239_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270871_1
- `C21`: Decrease transmission power for 3270871_1
- `C22`: Lift the tilt angle  of 3264164_4 by 5 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.108 | MS1 | 121.4656703289 | 31.1446297806 | 355 | 504990 | -86.93 | 14.12 | 349.94 | 0.14 | 2.50 | 1589 |
| 2024-09-20 22:21:32.657 | MS1 | 121.4656630881 | 31.1446200973 | 355 | 504990 | -91.56 | 17.73 | 562.55 | 0.06 | 2.19 | 1578 |
| 2024-09-20 22:21:33.745 | MS1 | 121.4656620217 | 31.1446255416 | 355 | 504990 | -91.70 | 15.84 | 364.71 | 0.05 | 2.69 | 1600 |
| 2024-09-20 22:21:34.716 | MS1 | 121.4656645731 | 31.1446322380 | 355 | 504990 | -86.51 | 15.69 | 98.99 | 0.11 | 2.42 | 1561 |
| 2024-09-20 22:21:35.290 | MS1 | 121.4656643021 | 31.1446243771 | 355 | 504990 | -88.62 | 17.68 | 86.71 | 0.14 | 2.66 | 1583 |
| 2024-09-20 22:21:36.627 | MS1 | 121.4656757612 | 31.1446261891 | 355 | 504990 | -91.67 | 17.54 | 98.05 | 0.11 | 2.47 | 1599 |
| 2024-09-20 22:21:37.624 | MS1 | 121.4656715115 | 31.1446322620 | 355 | 504990 | -93.36 | 9.06 | 87.83 | 0.01 | 2.67 | 1592 |
| 2024-09-20 22:21:38.628 | MS1 | 121.4656636255 | 31.1446358185 | 355 | 504990 | -92.26 | 8.17 | 100.93 | 0.04 | 2.92 | 1570 |
| 2024-09-20 22:21:39.576 | MS1 | 121.4656754881 | 31.1446190947 | 355 | 504990 | -93.31 | 9.84 | 52.08 | 0.03 | 2.28 | 1577 |
| 2024-09-20 22:21:40.738 | MS1 | 121.4656639971 | 31.1446359468 | 355 | 504990 | -91.31 | 9.53 | 377.70 | 0.02 | 2.17 | 1573 |
| 2024-09-20 22:21:41.692 | MS1 | 121.4656605550 | 31.1446260101 | 355 | 504990 | -91.65 | 7.93 | 547.17 | 0.06 | 2.30 | 1572 |
| 2024-09-20 22:21:42.170 | MS1 | 121.4656670318 | 31.1446308550 | 355 | 504990 | -93.61 | 10.58 | 482.90 | 0.15 | 2.55 | 1590 |

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
| 3232861 | 2 | 121.4707744421 | 31.1489102016 | 141 | 10 | 11 | 15.9 | TDD | 530 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3264164 | 4 | 121.4685850213 | 31.1545556923 | 56 | 14 | 7 | 20.6 | TDD | 473 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3270871 | 1 | 121.4738298720 | 31.1544294283 | 187 | 3 | 9 | 49.1 | TDD | 145 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3277239 | 3 | 121.4650751529 | 31.1522913527 | 224 | 0 | 6 | 32.3 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.173 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.188 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.309 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.309 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.023 | NREventA3 | measId:2;ServCellPCI:672;Se... |
| 2024-09-20 22:21:38.263 | NRHandoverAttempt | SourcePCI:672;SourceNR-ARFC... |
| 2024-09-20 22:21:38.311 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.321 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.422 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.422 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270871 | 1 | 10.4753 | 7.2019 | -117.8341 | 19.6176 | 181.8795 | 0.0191 | 0.0022 |
| 2024_09_20 22:00 | 3232861 | 2 | 19.0475 | 15.9054 | -117.9171 | 18.3135 | 115.4232 | 0.0099 | 0.0060 |
| 2024_09_20 22:00 | 3277239 | 3 | 84.3826 | 85.2767 | -114.2123 | 14.5493 | 110.3404 | 0.0175 | 0.0036 |
| 2024_09_20 22:00 | 3264164 | 4 | 9.9724 | 17.8777 | -115.9186 | 14.5364 | 165.4190 | 0.0156 | 0.0130 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416536_9980F73A | 504990 | 355 | -87.1 | 504990 | 145 | -96.0 | 504990 | 473 | -99.2 | 504990 | 530 |
| MR_1774416536_3A545AF0 | 504990 | 355 | -86.3 | 504990 | 145 | -95.7 | 504990 | 473 | -96.7 | 504990 | 530 |
| MR_1774416536_15E6A541 | 504990 | 355 | -87.5 | 504990 | 145 | -95.6 | 504990 | 473 | -99.2 | 504990 | 530 |
| MR_1774416536_A0FFF09C | 504990 | 355 | -85.5 | 504990 | 145 | -93.9 | 504990 | 473 | -98.5 | 504990 | 530 |
| MR_1774416536_25D06B7D | 504990 | 355 | -87.2 | 504990 | 145 | -96.5 | 504990 | 473 | -98.0 | 504990 | 530 |
| MR_1774416536_5C7A3BAD | 504990 | 355 | -85.1 | 504990 | 145 | -94.5 | 504990 | 473 | -97.2 | 504990 | 530 |
| MR_1774416536_06417745 | 504990 | 355 | -84.9 | 504990 | 145 | -93.0 | 504990 | 473 | -96.8 | 504990 | 530 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 857: `1fbe97e5-9a8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1fbe97e5-9a86-4136-b80e-765bf535c273` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277932_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[857] topology](images/train_0857.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233018_6
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277932_4
- `C4`: Press down the tilt angle  of 3233018_6 by 4 degrees
- `C5`: Press down the tilt angle of 3277932_4 by 3 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233018_6
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Adjust the azimuth of 3277932_4 by 45 degrees
- `C9`: Increase transmission power for 3233018_6
- `C10`: Decrease transmission power for 3233018_6
- `C11`: Add neighbor relationship between 3214059_9 and 3233018_6
- `C12`: Adjust the azimuth of 3233018_6 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3277932_4
- `C14`: Increase A3 Offset threshold for 3233018_6
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277932_4 **← 정답**
- `C16`: Lift the tilt angle of 3277932_4 by 3 degrees
- `C17`: Increase A3 Offset threshold for 3277932_4
- `C18`: Increase transmission power for 3277932_4
- `C19`: Add neighbor relationship between 3277932_4 and 3233018_6
- `C20`: Decrease transmission power for 3277932_4
- `C21`: Lift the tilt angle  of 3233018_6 by 4 degrees
- `C22`: Decrease A3 Offset threshold for 3233018_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.667 | MS1 | 121.4656642406 | 31.1446206365 | 560 | 504990 | -94.89 | 12.94 | 399.93 | 0.09 | 2.71 | 1580 |
| 2024-09-20 22:21:32.969 | MS1 | 121.4656657539 | 31.1446205573 | 512 | 504990 | -94.62 | 13.72 | 553.93 | 0.15 | 2.88 | 1599 |
| 2024-09-20 22:21:33.470 | MS1 | 121.4656773586 | 31.1446267181 | 414 | 504990 | -95.13 | 10.73 | 568.67 | 0.11 | 2.46 | 1587 |
| 2024-09-20 22:21:34.983 | MS1 | 121.4656667703 | 31.1446378438 | 679 | 152650 | -90.11 | 7.64 | 92.12 | 0.20 | 1.62 | 935 |
| 2024-09-20 22:21:35.595 | MS1 | 121.4656675463 | 31.1446213502 | 288 | 152650 | -89.71 | 5.03 | 97.50 | 0.14 | 1.74 | 996 |
| 2024-09-20 22:21:36.538 | MS1 | 121.4656634117 | 31.1446221327 | 871 | 152650 | -90.70 | 6.97 | 90.80 | 0.15 | 1.73 | 997 |
| 2024-09-20 22:21:37.131 | MS1 | 121.4656675271 | 31.1446335293 | 802 | 152650 | -92.80 | 3.10 | 56.86 | 0.00 | 1.80 | 920 |
| 2024-09-20 22:21:38.500 | MS1 | 121.4656771328 | 31.1446356596 | 679 | 152650 | -91.02 | 2.13 | 57.98 | 0.07 | 1.64 | 923 |
| 2024-09-20 22:21:39.188 | MS1 | 121.4656752452 | 31.1446246101 | 288 | 152650 | -96.62 | 6.05 | 92.05 | 0.17 | 1.80 | 952 |
| 2024-09-20 22:21:40.522 | MS1 | 121.4656704986 | 31.1446187208 | 871 | 152650 | -88.39 | 6.99 | 45.26 | 0.14 | 2.10 | 1573 |
| 2024-09-20 22:21:41.877 | MS1 | 121.4656676042 | 31.1446290766 | 802 | 152650 | -90.84 | 3.61 | 79.64 | 0.14 | 2.23 | 1592 |
| 2024-09-20 22:21:42.272 | MS1 | 121.4656672177 | 31.1446363847 | 679 | 152650 | -95.25 | 6.08 | 49.96 | 0.12 | 2.07 | 1595 |

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
| 3214059 | 9 | 121.4656638069 | 31.1559318397 | 112 | 8 | 9 | 4.4 | FDD | 871 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3215699 | 8 | 121.4645759345 | 31.1486787833 | 122 | 15 | 12 | 5.3 | FDD | 802 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3226167 | 13 | 121.4674101360 | 31.1528961731 | 24 | 2 | 4 | 25.2 | FDD | 594 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3233018 | 6 | 121.4659311937 | 31.1546546427 | 191 | 3 | 11 | 16.1 | TDD | 638 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3235634 | 1 | 121.4666922829 | 31.1468101400 | 94 | 0 | 7 | 2.6 | TDD | 512 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3248825 | 12 | 121.4741282912 | 31.1479774591 | 337 | 13 | 3 | 5.8 | FDD | 526 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3250337 | 2 | 121.4756068861 | 31.1544617859 | 178 | 0 | 12 | 2.7 | TDD | 414 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3252362 | 11 | 121.4672839233 | 31.1556243914 | 66 | 15 | 0 | 8.2 | FDD | 839 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3269228 | 5 | 121.4730523743 | 31.1543348602 | 300 | 3 | 2 | 17.9 | TDD | 884 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3271162 | 10 | 121.4640731046 | 31.1488570265 | 43 | 6 | 2 | 10.6 | FDD | 679 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3273928 | 3 | 121.4756270711 | 31.1559873867 | 232 | 5 | 1 | 22.4 | TDD | 427 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3277932 | 4 | 121.4748798853 | 31.1473701773 | 206 | 2 | 9 | 10.4 | TDD | 560 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3278151 | 7 | 121.4683128164 | 31.1544085981 | 134 | 11 | 0 | 3.9 | FDD | 288 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |

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
| 2024-09-20 22:21:30.826 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.849 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.953 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.953 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.675 | NREventA2 | measId:1;ServCellPCI:813;Se... |
| 2024-09-20 22:21:34.799 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.079 | NREventA5 | measId:3;ServCellPCI:813;Se... |
| 2024-09-20 22:21:35.112 | NRHandoverAttempt | SourcePCI:813;SourceNR-ARFC... |
| 2024-09-20 22:21:35.158 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.170 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.299 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.299 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235634 | 1 | 10.8569 | 9.1864 | -117.9069 | 12.7472 | 157.0398 | 0.0015 | 0.0194 |
| 2024_09_20 22:00 | 3250337 | 2 | 6.6408 | 5.2684 | -117.9699 | 19.4123 | 177.4155 | 0.0073 | 0.0189 |
| 2024_09_20 22:00 | 3273928 | 3 | 13.0446 | 19.9169 | -114.0692 | 16.3211 | 90.3228 | 0.0171 | 0.0190 |
| 2024_09_20 22:00 | 3277932 | 4 | 8.5220 | 16.2716 | -114.3791 | 19.4627 | 113.7579 | 0.0089 | 0.0140 |
| 2024_09_20 22:00 | 3269228 | 5 | 5.6809 | 16.5666 | -115.0241 | 14.9795 | 176.7153 | 0.0098 | 0.0097 |
| 2024_09_20 22:00 | 3233018 | 6 | 8.7642 | 18.4294 | -115.1781 | 17.0684 | 83.0800 | 0.0054 | 0.0158 |
| 2024_09_20 22:00 | 3278151 | 7 | 5.1769 | 7.8862 | -114.6794 | 4.2980 | 47.0345 | 0.0086 | 0.0016 |
| 2024_09_20 22:00 | 3215699 | 8 | 17.6666 | 8.3869 | -114.5595 | 4.1749 | 25.8804 | 0.0150 | 0.0010 |
| 2024_09_20 22:00 | 3214059 | 9 | 15.2684 | 16.0551 | -117.0164 | 4.8022 | 32.6887 | 0.0096 | 0.0031 |
| 2024_09_20 22:00 | 3271162 | 10 | 17.3978 | 8.8076 | -116.8570 | 3.6221 | 28.4169 | 0.0041 | 0.0125 |
| 2024_09_20 22:00 | 3252362 | 11 | 16.4959 | 9.6502 | -114.4535 | 4.1719 | 25.4051 | 0.0196 | 0.0041 |
| 2024_09_20 22:00 | 3248825 | 12 | 11.4125 | 9.1705 | -117.9000 | 3.6177 | 58.3440 | 0.0156 | 0.0131 |
| 2024_09_20 22:00 | 3226167 | 13 | 11.6463 | 6.7615 | -116.8893 | 3.2626 | 47.4579 | 0.0159 | 0.0132 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416045_8CE23351 | 152650 | 679 | -91.7 | 152650 | 526 | -94.5 | 152650 | 594 | -95.7 | 152650 | 839 |
| MR_1774416045_E6B4F285 | 504990 | 414 | -97.0 | 504990 | 638 | -95.1 | 504990 | 427 | -101.5 | 504990 | 884 |
| MR_1774416045_9C5AA570 | 152650 | 679 | -90.2 | 152650 | 526 | -93.8 | 152650 | 594 | -97.9 | 152650 | 839 |
| MR_1774416045_8FD0E16E | 152650 | 679 | -88.1 | 152650 | 526 | -93.5 | 152650 | 594 | -97.0 | 152650 | 839 |
| MR_1774416045_01A0CA25 | 504990 | 414 | -94.1 | 504990 | 638 | -95.2 | 504990 | 427 | -100.0 | 504990 | 884 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 858: `5d44b0b4-254...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5d44b0b4-2549-4cac-94f9-29899aaf67e0` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3216132_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[858] topology](images/train_0858.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3262684_2
- `C2`: Decrease A3 Offset threshold for 3262684_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216132_3 **← 정답**
- `C4`: Lift the tilt angle of 3216132_3 by 4 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262684_2
- `C6`: Lift the tilt angle  of 3262684_2 by 4 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216132_3
- `C9`: Adjust the azimuth of 3216132_3 by 42 degrees
- `C10`: Add neighbor relationship between 3216132_3 and 3262684_2
- `C11`: Adjust the azimuth of 3262684_2 by 50 degrees
- `C12`: Increase transmission power for 3262684_2
- `C13`: Press down the tilt angle  of 3262684_2 by 4 degrees
- `C14`: Press down the tilt angle of 3216132_3 by 4 degrees
- `C15`: Add neighbor relationship between 3218067_1 and 3262684_2
- `C16`: Decrease transmission power for 3216132_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262684_2
- `C18`: Increase A3 Offset threshold for 3262684_2
- `C19`: Check test server and transmission issues
- `C20`: Increase transmission power for 3216132_3
- `C21`: Decrease A3 Offset threshold for 3216132_3
- `C22`: Increase A3 Offset threshold for 3216132_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.598 | MS1 | 121.4656615718 | 31.1446364563 | 84 | 504990 | -85.75 | 16.86 | 401.66 | 0.18 | 2.09 | 1573 |
| 2024-09-20 22:21:32.668 | MS1 | 121.4656658390 | 31.1446305861 | 84 | 504990 | -87.52 | 12.82 | 464.57 | 0.08 | 2.08 | 1575 |
| 2024-09-20 22:21:33.336 | MS1 | 121.4656668991 | 31.1446212917 | 84 | 504990 | -86.85 | 17.97 | 471.93 | 0.02 | 2.09 | 1583 |
| 2024-09-20 22:21:34.832 | MS1 | 121.4656750432 | 31.1446305004 | 84 | 504990 | -91.14 | 16.85 | 76.37 | 0.67 | 2.45 | 514 |
| 2024-09-20 22:21:35.935 | MS1 | 121.4656712880 | 31.1446315412 | 84 | 504990 | -91.66 | 15.90 | 79.26 | 0.52 | 2.48 | 526 |
| 2024-09-20 22:21:36.171 | MS1 | 121.4656616789 | 31.1446184828 | 84 | 504990 | -89.04 | 12.97 | 79.99 | 0.70 | 2.37 | 556 |
| 2024-09-20 22:21:37.365 | MS1 | 121.4656629114 | 31.1446212779 | 84 | 504990 | -91.74 | 9.64 | 54.95 | 0.70 | 2.25 | 653 |
| 2024-09-20 22:21:38.928 | MS1 | 121.4656711906 | 31.1446295793 | 84 | 504990 | -89.57 | 9.96 | 51.78 | 0.69 | 2.98 | 597 |
| 2024-09-20 22:21:39.115 | MS1 | 121.4656669830 | 31.1446261116 | 84 | 504990 | -90.22 | 9.96 | 55.68 | 0.53 | 2.68 | 572 |
| 2024-09-20 22:21:40.560 | MS1 | 121.4656629743 | 31.1446296579 | 84 | 504990 | -93.99 | 7.46 | 445.48 | 0.18 | 2.09 | 1580 |
| 2024-09-20 22:21:41.932 | MS1 | 121.4656731697 | 31.1446214866 | 84 | 504990 | -90.88 | 10.66 | 463.92 | 0.12 | 2.46 | 1576 |
| 2024-09-20 22:21:42.658 | MS1 | 121.4656625492 | 31.1446280516 | 84 | 504990 | -91.38 | 7.86 | 404.90 | 0.16 | 2.41 | 1572 |

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
| 3216132 | 3 | 121.4667889549 | 31.1543455805 | 144 | 1 | 7 | 48.3 | TDD | 84 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3218067 | 1 | 121.4702787083 | 31.1518275131 | 86 | 2 | 5 | 43.9 | TDD | 237 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3218384 | 4 | 121.4672105253 | 31.1530928936 | 282 | 5 | 4 | 32.1 | TDD | 53 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3262684 | 2 | 121.4751543874 | 31.1447760834 | 124 | 1 | 8 | 41.7 | TDD | 706 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.614 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.632 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.765 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.765 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.493 | NREventA3 | measId:2;ServCellPCI:313;Se... |
| 2024-09-20 22:21:38.733 | NRHandoverAttempt | SourcePCI:313;SourceNR-ARFC... |
| 2024-09-20 22:21:38.769 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.781 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.881 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.881 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218067 | 1 | 18.1962 | 9.2254 | -116.0052 | 17.5867 | 90.4409 | 0.0105 | 0.0158 |
| 2024_09_20 22:00 | 3262684 | 2 | 16.9144 | 17.2646 | -116.7964 | 8.4030 | 159.6327 | 0.0052 | 0.0029 |
| 2024_09_20 22:00 | 3216132 | 3 | 6.9108 | 9.9946 | -116.3290 | 6.5116 | 141.6645 | 0.0170 | 0.0010 |
| 2024_09_20 22:00 | 3218384 | 4 | 13.6170 | 8.9748 | -115.3471 | 11.1400 | 97.3339 | 0.0051 | 0.0044 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412534_EC5CE3A3 | 504990 | 84 | -92.8 | 504990 | 706 | -93.5 | 504990 | 237 | -104.6 | 504990 | 53 |
| MR_1774412534_707A506E | 504990 | 84 | -90.9 | 504990 | 706 | -93.3 | 504990 | 237 | -107.0 | 504990 | 53 |
| MR_1774412534_A08EBFF9 | 504990 | 84 | -92.1 | 504990 | 706 | -93.9 | 504990 | 237 | -106.3 | 504990 | 53 |
| MR_1774412534_198E8834 | 504990 | 84 | -90.0 | 504990 | 706 | -92.8 | 504990 | 237 | -103.7 | 504990 | 53 |
| MR_1774412534_36430997 | 504990 | 84 | -89.3 | 504990 | 706 | -93.7 | 504990 | 237 | -104.1 | 504990 | 53 |
| MR_1774412534_F7BDAB50 | 504990 | 84 | -90.8 | 504990 | 706 | -91.8 | 504990 | 237 | -105.5 | 504990 | 53 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 859: `d9c96983-9e8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d9c96983-9e88-45d5-ae5e-af7fb3511add` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3248091_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[859] topology](images/train_0859.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245501_3
- `C2`: Decrease transmission power for 3245501_3
- `C3`: Decrease A3 Offset threshold for 3248091_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245501_3
- `C5`: Adjust the azimuth of 3248091_1 by 40 degrees
- `C6`: Press down the tilt angle of 3248091_1 by 3 degrees
- `C7`: Increase transmission power for 3245501_3
- `C8`: Increase A3 Offset threshold for 3245501_3
- `C9`: Decrease transmission power for 3248091_1
- `C10`: Add neighbor relationship between 3265307_4 and 3245501_3
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease A3 Offset threshold for 3245501_3
- `C13`: Lift the tilt angle  of 3245501_3 by 8 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248091_1
- `C15`: Increase transmission power for 3248091_1
- `C16`: Lift the tilt angle of 3248091_1 by 3 degrees
- `C17`: Add neighbor relationship between 3248091_1 and 3245501_3
- `C18`: Check test server and transmission issues
- `C19`: Press down the tilt angle  of 3245501_3 by 8 degrees
- `C20`: Adjust the azimuth of 3245501_3 by 50 degrees
- `C21`: Increase A3 Offset threshold for 3248091_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248091_1 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.913 | MS1 | 121.4656724159 | 31.1446368973 | 618 | 504990 | -91.24 | 12.07 | 468.51 | 0.09 | 2.73 | 1596 |
| 2024-09-20 22:21:32.548 | MS1 | 121.4656679948 | 31.1446295565 | 618 | 504990 | -89.93 | 17.62 | 370.93 | 0.07 | 2.57 | 1572 |
| 2024-09-20 22:21:33.616 | MS1 | 121.4656700741 | 31.1446373143 | 618 | 504990 | -88.96 | 17.66 | 382.00 | 0.15 | 2.06 | 1596 |
| 2024-09-20 22:21:34.123 | MS1 | 121.4656743699 | 31.1446326620 | 618 | 504990 | -85.64 | 17.93 | 72.23 | 0.50 | 2.16 | 670 |
| 2024-09-20 22:21:35.374 | MS1 | 121.4656599095 | 31.1446284247 | 618 | 504990 | -87.60 | 12.72 | 51.63 | 0.58 | 2.46 | 506 |
| 2024-09-20 22:21:36.682 | MS1 | 121.4656691196 | 31.1446266721 | 618 | 504990 | -85.73 | 16.91 | 51.59 | 0.65 | 2.05 | 670 |
| 2024-09-20 22:21:37.160 | MS1 | 121.4656624135 | 31.1446249666 | 618 | 504990 | -90.92 | 8.31 | 87.68 | 0.51 | 2.56 | 603 |
| 2024-09-20 22:21:38.540 | MS1 | 121.4656688600 | 31.1446201497 | 618 | 504990 | -93.47 | 11.40 | 54.36 | 0.67 | 2.61 | 582 |
| 2024-09-20 22:21:39.575 | MS1 | 121.4656603100 | 31.1446216783 | 618 | 504990 | -91.04 | 12.72 | 86.68 | 0.51 | 2.70 | 685 |
| 2024-09-20 22:21:40.127 | MS1 | 121.4656601916 | 31.1446312311 | 618 | 504990 | -93.29 | 9.18 | 541.03 | 0.03 | 2.05 | 1573 |
| 2024-09-20 22:21:41.720 | MS1 | 121.4656701371 | 31.1446208927 | 618 | 504990 | -89.31 | 12.02 | 414.45 | 0.09 | 2.49 | 1578 |
| 2024-09-20 22:21:42.366 | MS1 | 121.4656677759 | 31.1446272885 | 618 | 504990 | -93.02 | 11.37 | 434.03 | 0.05 | 2.45 | 1578 |

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
| 3228614 | 2 | 121.4672248134 | 31.1557754248 | 215 | 0 | 7 | 20.3 | TDD | 547 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3245501 | 3 | 121.4645921363 | 31.1546365418 | 98 | 6 | 5 | 40.6 | TDD | 171 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3248091 | 1 | 121.4754558809 | 31.1486056080 | 285 | 1 | 8 | 37.4 | TDD | 618 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3265307 | 4 | 121.4742460242 | 31.1549768112 | 184 | 12 | 9 | 30.2 | TDD | 631 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.809 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.834 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.943 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.943 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.618 | NREventA3 | measId:2;ServCellPCI:540;Se... |
| 2024-09-20 22:21:37.858 | NRHandoverAttempt | SourcePCI:540;SourceNR-ARFC... |
| 2024-09-20 22:21:37.898 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.908 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.048 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.048 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248091 | 1 | 19.5313 | 6.3643 | -117.5584 | 9.2194 | 97.3641 | 0.0050 | 0.0121 |
| 2024_09_20 22:00 | 3228614 | 2 | 5.0733 | 10.8674 | -115.2639 | 18.3112 | 102.4224 | 0.0020 | 0.0093 |
| 2024_09_20 22:00 | 3245501 | 3 | 11.0975 | 16.2266 | -117.0645 | 18.7585 | 88.3216 | 0.0114 | 0.0134 |
| 2024_09_20 22:00 | 3265307 | 4 | 18.3747 | 9.5235 | -117.9893 | 10.3220 | 190.6983 | 0.0172 | 0.0069 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413581_83031BF3 | 504990 | 618 | -87.0 | 504990 | 171 | -93.7 | 504990 | 631 | -94.9 | 504990 | 547 |
| MR_1774413581_DC9A8A9B | 504990 | 618 | -87.3 | 504990 | 171 | -93.5 | 504990 | 631 | -97.5 | 504990 | 547 |
| MR_1774413581_C22531E3 | 504990 | 618 | -85.1 | 504990 | 171 | -95.6 | 504990 | 631 | -95.1 | 504990 | 547 |
| MR_1774413581_C1DA1ADE | 504990 | 618 | -84.8 | 504990 | 171 | -96.0 | 504990 | 631 | -96.2 | 504990 | 547 |
| MR_1774413581_78F23C36 | 504990 | 618 | -84.0 | 504990 | 171 | -94.8 | 504990 | 631 | -95.6 | 504990 | 547 |

> *... 2개 열 생략 (전체 14열)*

---
