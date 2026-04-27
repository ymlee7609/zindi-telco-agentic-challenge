# Track A 문제 분석 — train[1850]~train[1859]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1850] ~ train[1859] (10개)

## 목차

1. [문제 1850: `e3b04ad6-9b3...`](#1850) — multiple-answer, 정답: C3|C7
2. [문제 1851: `43708107-781...`](#1851) — single-answer, 정답: C5
3. [문제 1852: `82852b4b-363...`](#1852) — single-answer, 정답: C6
4. [문제 1853: `e78bb270-01a...`](#1853) — multiple-answer, 정답: C7|C13
5. [문제 1854: `cdce2b9d-9b6...`](#1854) — single-answer, 정답: C11
6. [문제 1855: `85545a36-150...`](#1855) — single-answer, 정답: C19
7. [문제 1856: `d99ce32d-dee...`](#1856) — single-answer, 정답: C15
8. [문제 1857: `10f26d88-72c...`](#1857) — single-answer, 정답: C11
9. [문제 1858: `3c031fab-984...`](#1858) — single-answer, 정답: C16
10. [문제 1859: `68d9cc76-086...`](#1859) — single-answer, 정답: C11

---

### 문제 1850: `e3b04ad6-9b3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e3b04ad6-9b36-4790-a0e4-f48c11fb19fa` |
| Tag | **multiple-answer** |
| 정답 | **C3|C7** |
| C3 의미 | Adjust the azimuth of 3265431_4 by 50 degrees |
| C7 의미 | Increase transmission power for 3265431_4 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1850] topology](images/train_1850.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3259137_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259137_2
- `C3`: Adjust the azimuth of 3265431_4 by 50 degrees **← 정답**
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259137_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265431_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase transmission power for 3265431_4 **← 정답**
- `C8`: Press down the tilt angle of 3265431_4 by 3 degrees
- `C9`: Increase transmission power for 3259137_2
- `C10`: Decrease A3 Offset threshold for 3265431_4
- `C11`: Lift the tilt angle of 3265431_4 by 3 degrees
- `C12`: Press down the tilt angle  of 3259137_2 by 4 degrees
- `C13`: Add neighbor relationship between 3248521_1 and 3259137_2
- `C14`: Check test server and transmission issues
- `C15`: Add neighbor relationship between 3265431_4 and 3259137_2
- `C16`: Increase A3 Offset threshold for 3259137_2
- `C17`: Decrease A3 Offset threshold for 3259137_2
- `C18`: Decrease transmission power for 3265431_4
- `C19`: Increase A3 Offset threshold for 3265431_4
- `C20`: Adjust the azimuth of 3259137_2 by 42 degrees
- `C21`: Lift the tilt angle  of 3259137_2 by 4 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265431_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.739 | MS1 | 121.4656598835 | 31.1446221185 | 485 | 504990 | -89.32 | 17.01 | 475.19 | 0.07 | 2.94 | 1570 |
| 2024-09-20 22:21:32.612 | MS1 | 121.4656623508 | 31.1446305612 | 485 | 504990 | -88.99 | 12.65 | 373.24 | 0.02 | 2.97 | 1582 |
| 2024-09-20 22:21:33.136 | MS1 | 121.4656672545 | 31.1446258123 | 485 | 504990 | -85.56 | 16.24 | 583.42 | 0.17 | 2.88 | 1597 |
| 2024-09-20 22:21:34.994 | MS1 | 121.4656628870 | 31.1446327719 | 485 | 504990 | -108.30 | -1.76 | 26.85 | 0.14 | 1.31 | 1587 |
| 2024-09-20 22:21:35.111 | MS1 | 121.4656614887 | 31.1446289057 | 485 | 504990 | -102.23 | 1.69 | 41.25 | 0.04 | 1.44 | 1592 |
| 2024-09-20 22:21:36.936 | MS1 | 121.4656604879 | 31.1446184215 | 485 | 504990 | -100.04 | 1.65 | 82.07 | 0.04 | 1.19 | 1560 |
| 2024-09-20 22:21:37.323 | MS1 | 121.4656735956 | 31.1446360701 | 485 | 504990 | -109.92 | -0.19 | 65.36 | 0.09 | 1.08 | 1564 |
| 2024-09-20 22:21:38.491 | MS1 | 121.4656678546 | 31.1446286876 | 485 | 504990 | -107.57 | -0.89 | 87.36 | 0.01 | 1.49 | 1586 |
| 2024-09-20 22:21:39.892 | MS1 | 121.4656635120 | 31.1446207691 | 485 | 504990 | -103.35 | 1.76 | 59.60 | 0.07 | 1.42 | 1587 |
| 2024-09-20 22:21:40.852 | MS1 | 121.4656590271 | 31.1446375830 | 485 | 504990 | -91.64 | 14.27 | 464.87 | 0.00 | 2.51 | 1590 |
| 2024-09-20 22:21:41.134 | MS1 | 121.4656665169 | 31.1446187599 | 485 | 504990 | -93.29 | 14.85 | 482.63 | 0.08 | 2.04 | 1562 |
| 2024-09-20 22:21:42.668 | MS1 | 121.4656685967 | 31.1446273035 | 485 | 504990 | -89.00 | 15.73 | 587.49 | 0.05 | 2.46 | 1577 |

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
| 3248521 | 1 | 121.4745304926 | 31.1527960907 | 174 | 1 | 0 | 37.2 | TDD | 120 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3259137 | 2 | 121.4666048852 | 31.1481858002 | 151 | 1 | 4 | 23.7 | TDD | 218 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3265431 | 4 | 121.4686499679 | 31.1559781286 | 244 | 2 | 11 | 18.5 | TDD | 485 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3268297 | 3 | 121.4747521722 | 31.1555026735 | 255 | 0 | 0 | 44.0 | TDD | 540 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.320 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.335 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.455 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.455 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.697 | NREventA2 | measId:1;ServCellPCI:427;Se... |
| 2024-09-20 22:21:34.828 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248521 | 1 | 8.2517 | 19.5755 | -116.7183 | 10.5898 | 100.4072 | 0.0111 | 0.0028 |
| 2024_09_20 22:00 | 3259137 | 2 | 6.2175 | 6.6746 | -114.3238 | 13.7245 | 162.8537 | 0.0164 | 0.0183 |
| 2024_09_20 22:00 | 3268297 | 3 | 7.4398 | 6.5417 | -116.5342 | 14.5505 | 114.9368 | 0.0047 | 0.0094 |
| 2024_09_20 22:00 | 3265431 | 4 | 9.8017 | 8.6671 | -115.8402 | 12.7534 | 152.3587 | 0.1218 | 0.0032 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416579_FA8E8BDF | 504990 | 485 | -106.5 | 504990 | 218 | -113.2 | 504990 | 120 | -118.0 | 504990 | 540 |
| MR_1774416579_D75DB70D | 504990 | 485 | -107.7 | 504990 | 218 | -113.1 | 504990 | 120 | -119.1 | 504990 | 540 |
| MR_1774416579_C96A6EC1 | 504990 | 485 | -109.6 | 504990 | 218 | -109.3 | 504990 | 120 | -119.2 | 504990 | 540 |
| MR_1774416579_12B8AE1A | 504990 | 485 | -108.2 | 504990 | 218 | -112.7 | 504990 | 120 | -118.2 | 504990 | 540 |
| MR_1774416579_97593495 | 504990 | 485 | -107.3 | 504990 | 218 | -113.0 | 504990 | 120 | -116.9 | 504990 | 540 |
| MR_1774416579_D5C8CB30 | 504990 | 485 | -108.6 | 504990 | 218 | -112.4 | 504990 | 120 | -118.5 | 504990 | 540 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1851: `43708107-781...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `43708107-781e-4038-a6f6-71da92acd16f` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Add neighbor relationship between 3220103_4 and 3242567_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1851] topology](images/train_1851.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3242567_2 by 39 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220103_4
- `C3`: Decrease A3 Offset threshold for 3242567_2
- `C4`: Check test server and transmission issues
- `C5`: Add neighbor relationship between 3220103_4 and 3242567_2 **← 정답**
- `C6`: Press down the tilt angle  of 3242567_2 by 6 degrees
- `C7`: Increase A3 Offset threshold for 3242567_2
- `C8`: Lift the tilt angle  of 3242567_2 by 6 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Adjust the azimuth of 3220103_4 by 50 degrees
- `C11`: Increase A3 Offset threshold for 3220103_4
- `C12`: Increase transmission power for 3220103_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242567_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242567_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220103_4
- `C16`: Decrease transmission power for 3220103_4
- `C17`: Add neighbor relationship between 3239613_3 and 3242567_2
- `C18`: Decrease A3 Offset threshold for 3220103_4
- `C19`: Lift the tilt angle of 3220103_4 by 6 degrees
- `C20`: Increase transmission power for 3242567_2
- `C21`: Press down the tilt angle of 3220103_4 by 6 degrees
- `C22`: Decrease transmission power for 3242567_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.157 | MS1 | 121.4656678754 | 31.1446291487 | 326 | 504990 | -79.93 | 17.05 | 445.73 | 0.10 | 2.53 | 1586 |
| 2024-09-20 22:21:32.912 | MS1 | 121.4656585517 | 31.1446351131 | 326 | 504990 | -75.31 | 13.04 | 555.42 | 0.04 | 2.34 | 1574 |
| 2024-09-20 22:21:33.870 | MS1 | 121.4656657621 | 31.1446375029 | 326 | 504990 | -77.67 | 14.79 | 362.99 | 0.01 | 2.02 | 1582 |
| 2024-09-20 22:21:34.718 | MS1 | 121.4656667935 | 31.1446180050 | 326 | 504990 | -94.00 | -1.75 | 34.64 | 0.07 | 1.41 | 1574 |
| 2024-09-20 22:21:35.782 | MS1 | 121.4656743639 | 31.1446342229 | 326 | 504990 | -85.09 | -1.24 | 61.42 | 0.06 | 1.15 | 1590 |
| 2024-09-20 22:21:36.152 | MS1 | 121.4656640274 | 31.1446290660 | 326 | 504990 | -87.45 | -0.94 | 26.00 | 0.18 | 1.24 | 1581 |
| 2024-09-20 22:21:37.258 | MS1 | 121.4656779900 | 31.1446321212 | 326 | 504990 | -89.18 | -1.79 | 44.50 | 0.05 | 1.44 | 1568 |
| 2024-09-20 22:21:38.795 | MS1 | 121.4656636341 | 31.1446302625 | 326 | 504990 | -76.88 | 15.30 | 601.80 | 0.02 | 1.47 | 1576 |
| 2024-09-20 22:21:39.513 | MS1 | 121.4656730588 | 31.1446223074 | 326 | 504990 | -81.63 | 14.19 | 319.77 | 0.14 | 1.37 | 1587 |
| 2024-09-20 22:21:40.364 | MS1 | 121.4656666083 | 31.1446193310 | 326 | 504990 | -79.23 | 16.52 | 552.72 | 0.03 | 2.14 | 1587 |
| 2024-09-20 22:21:41.978 | MS1 | 121.4656584084 | 31.1446308037 | 326 | 504990 | -78.64 | 14.52 | 396.77 | 0.15 | 2.57 | 1575 |
| 2024-09-20 22:21:42.256 | MS1 | 121.4656679900 | 31.1446181455 | 326 | 504990 | -75.62 | 17.33 | 348.09 | 0.12 | 2.31 | 1599 |

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
| 3220103 | 4 | 121.4689561089 | 31.1489858677 | 322 | 2 | 0 | 44.4 | TDD | 326 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3230194 | 1 | 121.4700102743 | 31.1498570916 | 124 | 10 | 2 | 43.7 | TDD | 800 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3239613 | 3 | 121.4737741848 | 31.1470569370 | 165 | 13 | 9 | 24.1 | TDD | 891 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3242567 | 2 | 121.4711319280 | 31.1526312792 | 249 | 3 | 1 | 49.4 | TDD | 745 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.197 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.213 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.341 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.341 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.065 | NREventA3 | measId:2;ServCellPCI:393;Se... |
| 2024-09-20 22:21:36.065 | NREventA3 | measId:2;ServCellPCI:393;Se... |
| 2024-09-20 22:21:37.065 | NREventA3 | measId:2;ServCellPCI:393;Se... |
| 2024-09-20 22:21:39.565 | NRRRCReestablishAttempt | PCI:393 |
| 2024-09-20 22:21:39.577 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.588 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.720 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.720 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230194 | 1 | 11.8374 | 17.2124 | -114.3954 | 16.9390 | 107.7803 | 0.0177 | 0.0001 |
| 2024_09_20 22:00 | 3242567 | 2 | 10.4088 | 5.6955 | -116.1766 | 17.9883 | 134.9755 | 0.0173 | 0.0043 |
| 2024_09_20 22:00 | 3239613 | 3 | 13.8222 | 15.7923 | -115.8016 | 9.4455 | 98.4853 | 0.0162 | 0.0019 |
| 2024_09_20 22:00 | 3220103 | 4 | 11.4617 | 10.3060 | -115.8374 | 6.5499 | 102.7415 | 0.0097 | 0.1991 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416679_8E177F14 | 504990 | 326 | -95.6 | 504990 | 745 | -89.6 | 504990 | 891 | -90.9 | 504990 | 800 |
| MR_1774416679_B7E6488C | 504990 | 326 | -93.6 | 504990 | 745 | -86.2 | 504990 | 891 | -91.6 | 504990 | 800 |
| MR_1774416679_20B49CFA | 504990 | 326 | -94.2 | 504990 | 745 | -88.7 | 504990 | 891 | -90.9 | 504990 | 800 |
| MR_1774416679_477719F0 | 504990 | 326 | -92.8 | 504990 | 745 | -89.7 | 504990 | 891 | -92.8 | 504990 | 800 |
| MR_1774416679_C33086FA | 504990 | 326 | -94.1 | 504990 | 745 | -86.9 | 504990 | 891 | -90.4 | 504990 | 800 |
| MR_1774416679_52A7C4C7 | 504990 | 745 | -88.2 | 504990 | 326 | -92.2 | 504990 | 891 | -93.1 | 504990 | 800 |
| MR_1774416679_6596A951 | 504990 | 326 | -95.2 | 504990 | 745 | -88.7 | 504990 | 891 | -91.3 | 504990 | 800 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1852: `82852b4b-363...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `82852b4b-3638-4784-a48c-b9505c1bfe56` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1852] topology](images/train_1852.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3244486_1 by 50 degrees
- `C2`: Press down the tilt angle of 3244486_1 by 10 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217840_4
- `C4`: Decrease transmission power for 3217840_4
- `C5`: Decrease A3 Offset threshold for 3217840_4
- `C6`: Insufficient data; more data is needed for judgment. **← 정답**
- `C7`: Decrease transmission power for 3244486_1
- `C8`: Lift the tilt angle  of 3217840_4 by 10 degrees
- `C9`: Lift the tilt angle of 3244486_1 by 10 degrees
- `C10`: Increase A3 Offset threshold for 3217840_4
- `C11`: Press down the tilt angle  of 3217840_4 by 10 degrees
- `C12`: Increase transmission power for 3244486_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244486_1
- `C14`: Check test server and transmission issues
- `C15`: Increase A3 Offset threshold for 3244486_1
- `C16`: Add neighbor relationship between 3272496_2 and 3217840_4
- `C17`: Decrease A3 Offset threshold for 3244486_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217840_4
- `C19`: Add neighbor relationship between 3244486_1 and 3217840_4
- `C20`: Increase transmission power for 3217840_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244486_1
- `C22`: Adjust the azimuth of 3217840_4 by 42 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.726 | MS1 | 121.4656645379 | 31.1446312058 | 160 | 504990 | -90.62 | 13.11 | 369.00 | 0.07 | 2.48 | 1560 |
| 2024-09-20 22:21:32.822 | MS1 | 121.4656705020 | 31.1446294339 | 160 | 504990 | -89.03 | 14.83 | 429.27 | 0.15 | 2.55 | 1566 |
| 2024-09-20 22:21:33.169 | MS1 | 121.4656731958 | 31.1446308940 | 160 | 504990 | -88.96 | 12.81 | 589.33 | 0.17 | 2.46 | 1586 |
| 2024-09-20 22:21:34.503 | MS1 | 121.4656638371 | 31.1446261384 | 160 | 504990 | -91.40 | 14.83 | 95.86 | 0.10 | 2.41 | 1571 |
| 2024-09-20 22:21:35.186 | MS1 | 121.4656603314 | 31.1446228154 | 160 | 504990 | -91.00 | 13.91 | 88.09 | 0.03 | 2.59 | 1573 |
| 2024-09-20 22:21:36.285 | MS1 | 121.4656723937 | 31.1446235000 | 160 | 504990 | -85.42 | 12.12 | 81.03 | 0.13 | 2.27 | 1577 |
| 2024-09-20 22:21:37.486 | MS1 | 121.4656618050 | 31.1446250443 | 160 | 504990 | -91.60 | 8.47 | 65.52 | 0.02 | 2.51 | 1595 |
| 2024-09-20 22:21:38.675 | MS1 | 121.4656611242 | 31.1446293782 | 160 | 504990 | -91.01 | 10.10 | 81.06 | 0.06 | 2.21 | 1586 |
| 2024-09-20 22:21:39.452 | MS1 | 121.4656613208 | 31.1446328752 | 160 | 504990 | -93.92 | 12.06 | 90.42 | 0.12 | 2.18 | 1577 |
| 2024-09-20 22:21:40.202 | MS1 | 121.4656643161 | 31.1446355823 | 160 | 504990 | -90.58 | 9.21 | 306.50 | 0.19 | 2.69 | 1596 |
| 2024-09-20 22:21:41.325 | MS1 | 121.4656687990 | 31.1446346821 | 160 | 504990 | -92.35 | 12.20 | 366.89 | 0.16 | 2.75 | 1579 |
| 2024-09-20 22:21:42.360 | MS1 | 121.4656580146 | 31.1446255017 | 160 | 504990 | -92.26 | 11.99 | 493.95 | 0.14 | 2.56 | 1587 |

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
| 3217840 | 4 | 121.4650415802 | 31.1525143684 | 218 | 14 | 10 | 35.9 | TDD | 150 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3244486 | 1 | 121.4688073764 | 31.1459949092 | 353 | 8 | 9 | 21.0 | TDD | 160 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3272496 | 2 | 121.4644541331 | 31.1498729949 | 324 | 10 | 12 | 31.1 | TDD | 658 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3273652 | 3 | 121.4724940059 | 31.1479779661 | 153 | 4 | 3 | 44.5 | TDD | 996 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.179 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.195 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.321 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.321 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.023 | NREventA3 | measId:2;ServCellPCI:437;Se... |
| 2024-09-20 22:21:38.263 | NRHandoverAttempt | SourcePCI:437;SourceNR-ARFC... |
| 2024-09-20 22:21:38.296 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.306 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.429 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.429 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3244486 | 1 | 92.5972 | 91.3968 | -117.1110 | 10.0687 | 139.6258 | 0.0154 | 0.0167 |
| 2024_09_19 22:00 | 3272496 | 2 | 75.9823 | 88.0787 | -117.7405 | 7.6089 | 80.4886 | 0.0108 | 0.0084 |
| 2024_09_19 22:00 | 3273652 | 3 | 77.3702 | 90.3285 | -114.0351 | 10.3593 | 193.1358 | 0.0045 | 0.0110 |
| 2024_09_19 22:00 | 3217840 | 4 | 75.5001 | 93.0933 | -115.9500 | 6.4582 | 116.8351 | 0.0050 | 0.0190 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413159_4A2AF47D | 504990 | 160 | -91.8 | 504990 | 150 | -92.7 | 504990 | 658 | -103.4 | 504990 | 996 |
| MR_1774413159_E72D7365 | 504990 | 160 | -92.5 | 504990 | 150 | -96.0 | 504990 | 658 | -106.0 | 504990 | 996 |
| MR_1774413159_30F7D981 | 504990 | 160 | -91.0 | 504990 | 150 | -93.1 | 504990 | 658 | -104.9 | 504990 | 996 |
| MR_1774413159_9A05565C | 504990 | 160 | -89.4 | 504990 | 150 | -95.4 | 504990 | 658 | -103.4 | 504990 | 996 |
| MR_1774413159_4045409C | 504990 | 160 | -92.5 | 504990 | 150 | -96.2 | 504990 | 658 | -105.3 | 504990 | 996 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1853: `e78bb270-01a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e78bb270-01a1-425e-b692-58e593b5317e` |
| Tag | **multiple-answer** |
| 정답 | **C7|C13** |
| C7 의미 | Decrease transmission power for 3246569_1 |
| C13 의미 | Press down the tilt angle  of 3246569_1 by 2 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1853] topology](images/train_1853.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Adjust the azimuth of 3223434_2 by 16 degrees
- `C3`: Increase A3 Offset threshold for 3246569_1
- `C4`: Lift the tilt angle  of 3246569_1 by 2 degrees
- `C5`: Check test server and transmission issues
- `C6`: Decrease transmission power for 3223434_2
- `C7`: Decrease transmission power for 3246569_1 **← 정답**
- `C8`: Add neighbor relationship between 3244806_3 and 3246569_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223434_2
- `C10`: Press down the tilt angle of 3223434_2 by 2 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246569_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246569_1
- `C13`: Press down the tilt angle  of 3246569_1 by 2 degrees **← 정답**
- `C14`: Adjust the azimuth of 3246569_1 by 1 degrees
- `C15`: Add neighbor relationship between 3223434_2 and 3246569_1
- `C16`: Decrease A3 Offset threshold for 3246569_1
- `C17`: Lift the tilt angle of 3223434_2 by 2 degrees
- `C18`: Increase transmission power for 3246569_1
- `C19`: Increase transmission power for 3223434_2
- `C20`: Increase A3 Offset threshold for 3223434_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223434_2
- `C22`: Decrease A3 Offset threshold for 3223434_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.687 | MS1 | 121.4656692761 | 31.1446333690 | 541 | 504990 | -84.30 | 12.29 | 550.68 | 0.12 | 2.65 | 1590 |
| 2024-09-20 22:21:32.361 | MS1 | 121.4656772168 | 31.1446312507 | 541 | 504990 | -83.71 | 16.59 | 327.86 | 0.19 | 2.36 | 1600 |
| 2024-09-20 22:21:33.295 | MS1 | 121.4656717784 | 31.1446239196 | 541 | 504990 | -76.53 | 16.24 | 550.41 | 0.11 | 2.62 | 1594 |
| 2024-09-20 22:21:34.165 | MS1 | 121.4656608693 | 31.1446190300 | 541 | 504990 | -93.45 | 2.25 | 37.95 | 0.01 | 1.26 | 1561 |
| 2024-09-20 22:21:35.731 | MS1 | 121.4656722699 | 31.1446248577 | 541 | 504990 | -85.32 | 1.05 | 63.53 | 0.15 | 1.09 | 1588 |
| 2024-09-20 22:21:36.327 | MS1 | 121.4656755190 | 31.1446232902 | 541 | 504990 | -90.06 | 0.53 | 83.32 | 0.05 | 1.31 | 1597 |
| 2024-09-20 22:21:37.136 | MS1 | 121.4656734248 | 31.1446245634 | 541 | 504990 | -85.98 | 1.81 | 58.80 | 0.18 | 1.04 | 1590 |
| 2024-09-20 22:21:38.658 | MS1 | 121.4656638946 | 31.1446197392 | 541 | 504990 | -89.88 | 3.80 | 76.16 | 0.11 | 1.28 | 1581 |
| 2024-09-20 22:21:39.709 | MS1 | 121.4656628695 | 31.1446199342 | 541 | 504990 | -85.89 | 2.08 | 92.03 | 0.04 | 1.14 | 1582 |
| 2024-09-20 22:21:40.232 | MS1 | 121.4656734098 | 31.1446213600 | 541 | 504990 | -83.01 | 15.85 | 427.53 | 0.19 | 2.80 | 1591 |
| 2024-09-20 22:21:41.251 | MS1 | 121.4656629057 | 31.1446262401 | 541 | 504990 | -83.40 | 14.38 | 376.16 | 0.11 | 2.38 | 1575 |
| 2024-09-20 22:21:42.513 | MS1 | 121.4656733126 | 31.1446188171 | 541 | 504990 | -78.13 | 16.97 | 471.87 | 0.16 | 2.19 | 1569 |

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
| 3210327 | 4 | 121.4678732508 | 31.1463032880 | 60 | 8 | 5 | 35.1 | TDD | 278 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3223434 | 2 | 121.4732394390 | 31.1547223024 | 197 | 1 | 3 | 22.8 | TDD | 541 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3244806 | 3 | 121.4741314482 | 31.1531165177 | 286 | 8 | 4 | 25.2 | TDD | 338 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3246569 | 1 | 121.4655092209 | 31.1488811908 | 177 | 0 | 12 | 19.5 | TDD | 602 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.950 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.052 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.052 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246569 | 1 | 18.8623 | 19.6016 | -116.9615 | 16.6974 | 111.4803 | 0.0091 | 0.0110 |
| 2024_09_20 22:00 | 3223434 | 2 | 5.4407 | 13.2658 | -109.8229 | 15.8857 | 166.2917 | 0.0013 | 0.0177 |
| 2024_09_20 22:00 | 3244806 | 3 | 7.2444 | 9.9231 | -114.4122 | 11.3558 | 151.5155 | 0.0025 | 0.0174 |
| 2024_09_20 22:00 | 3210327 | 4 | 10.9882 | 6.4709 | -114.8669 | 14.0370 | 197.7770 | 0.0131 | 0.0001 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412669_A8A9B79D | 504990 | 602 | -92.8 | 504990 | 541 | -94.1 | 504990 | 338 | -96.2 | 504990 | 278 |
| MR_1774412669_E50AA178 | 504990 | 541 | -92.2 | 504990 | 602 | -94.8 | 504990 | 338 | -96.6 | 504990 | 278 |
| MR_1774412669_E6915EDF | 504990 | 602 | -94.2 | 504990 | 541 | -91.4 | 504990 | 338 | -93.3 | 504990 | 278 |
| MR_1774412669_CE385BA7 | 504990 | 541 | -93.5 | 504990 | 602 | -93.4 | 504990 | 338 | -94.5 | 504990 | 278 |
| MR_1774412669_BAA9C584 | 504990 | 602 | -93.2 | 504990 | 541 | -94.6 | 504990 | 338 | -96.4 | 504990 | 278 |
| MR_1774412669_41B69AEE | 504990 | 541 | -93.9 | 504990 | 602 | -92.9 | 504990 | 338 | -95.7 | 504990 | 278 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1854: `cdce2b9d-9b6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cdce2b9d-9b67-4f22-86bc-61f08cf19925` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1854] topology](images/train_1854.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3246413_2
- `C2`: Decrease transmission power for 3262546_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262546_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246413_2
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease A3 Offset threshold for 3246413_2
- `C7`: Increase transmission power for 3246413_2
- `C8`: Adjust the azimuth of 3246413_2 by 50 degrees
- `C9`: Decrease transmission power for 3246413_2
- `C10`: Add neighbor relationship between 3262546_4 and 3246413_2
- `C11`: Check test server and transmission issues **← 정답**
- `C12`: Adjust the azimuth of 3262546_4 by 50 degrees
- `C13`: Add neighbor relationship between 3271339_1 and 3246413_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262546_4
- `C15`: Decrease A3 Offset threshold for 3262546_4
- `C16`: Press down the tilt angle of 3262546_4 by 10 degrees
- `C17`: Lift the tilt angle of 3262546_4 by 10 degrees
- `C18`: Increase transmission power for 3262546_4
- `C19`: Press down the tilt angle  of 3246413_2 by 4 degrees
- `C20`: Lift the tilt angle  of 3246413_2 by 4 degrees
- `C21`: Increase A3 Offset threshold for 3262546_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246413_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.372 | MS1 | 121.4656696785 | 31.1446257149 | 455 | 504990 | -90.24 | 15.27 | 372.84 | 0.03 | 2.92 | 1584 |
| 2024-09-20 22:21:32.388 | MS1 | 121.4656614660 | 31.1446368621 | 455 | 504990 | -85.38 | 13.29 | 307.04 | 0.06 | 2.48 | 1574 |
| 2024-09-20 22:21:33.207 | MS1 | 121.4656731595 | 31.1446324519 | 455 | 504990 | -91.70 | 17.07 | 461.47 | 0.06 | 2.67 | 1585 |
| 2024-09-20 22:21:34.174 | MS1 | 121.4656723601 | 31.1446250757 | 455 | 504990 | -88.39 | 15.26 | 82.44 | 0.13 | 2.77 | 327 |
| 2024-09-20 22:21:35.754 | MS1 | 121.4656684043 | 31.1446286322 | 455 | 504990 | -88.93 | 17.53 | 67.67 | 0.19 | 2.71 | 425 |
| 2024-09-20 22:21:36.939 | MS1 | 121.4656664475 | 31.1446324582 | 455 | 504990 | -87.46 | 12.17 | 76.45 | 0.14 | 2.31 | 389 |
| 2024-09-20 22:21:37.815 | MS1 | 121.4656707078 | 31.1446306718 | 455 | 504990 | -90.16 | 7.75 | 80.13 | 0.09 | 2.15 | 368 |
| 2024-09-20 22:21:38.414 | MS1 | 121.4656656561 | 31.1446206341 | 455 | 504990 | -91.54 | 12.70 | 56.61 | 0.17 | 2.73 | 359 |
| 2024-09-20 22:21:39.561 | MS1 | 121.4656692510 | 31.1446359530 | 455 | 504990 | -92.40 | 10.85 | 63.52 | 0.08 | 2.90 | 349 |
| 2024-09-20 22:21:40.966 | MS1 | 121.4656769079 | 31.1446180479 | 455 | 504990 | -92.67 | 7.12 | 522.53 | 0.11 | 2.88 | 1597 |
| 2024-09-20 22:21:41.877 | MS1 | 121.4656638066 | 31.1446307336 | 455 | 504990 | -89.54 | 8.14 | 562.92 | 0.11 | 2.24 | 1577 |
| 2024-09-20 22:21:42.578 | MS1 | 121.4656624078 | 31.1446290650 | 455 | 504990 | -91.88 | 9.08 | 505.41 | 0.12 | 2.31 | 1567 |

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
| 3246413 | 2 | 121.4734060050 | 31.1453467934 | 37 | 2 | 7 | 30.8 | TDD | 196 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3260967 | 3 | 121.4677416247 | 31.1558432705 | 161 | 12 | 5 | 17.7 | TDD | 414 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3262546 | 4 | 121.4681055611 | 31.1467556422 | 326 | 3 | 2 | 44.5 | TDD | 455 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3271339 | 1 | 121.4682647307 | 31.1502008934 | 104 | 12 | 11 | 25.9 | TDD | 472 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.563 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.583 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.694 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.694 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.430 | NREventA3 | measId:2;ServCellPCI:305;Se... |
| 2024-09-20 22:21:38.670 | NRHandoverAttempt | SourcePCI:305;SourceNR-ARFC... |
| 2024-09-20 22:21:38.708 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.722 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.846 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.846 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271339 | 1 | 11.9754 | 7.3327 | -116.2186 | 15.9337 | 99.7529 | 0.0186 | 0.0005 |
| 2024_09_20 22:00 | 3246413 | 2 | 14.3233 | 13.5491 | -114.8589 | 9.9726 | 175.5068 | 0.0044 | 0.0068 |
| 2024_09_20 22:00 | 3260967 | 3 | 16.1097 | 10.6698 | -117.7844 | 12.3128 | 90.7455 | 0.0032 | 0.0187 |
| 2024_09_20 22:00 | 3262546 | 4 | 14.5016 | 9.1449 | -117.1108 | 5.9616 | 108.2474 | 0.0113 | 0.0183 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412888_33D3356B | 504990 | 455 | -89.4 | 504990 | 196 | -93.4 | 504990 | 472 | -98.0 | 504990 | 414 |
| MR_1774412888_E4556F32 | 504990 | 455 | -88.5 | 504990 | 196 | -94.3 | 504990 | 472 | -96.6 | 504990 | 414 |
| MR_1774412888_3834A5F2 | 504990 | 455 | -89.3 | 504990 | 196 | -94.0 | 504990 | 472 | -97.6 | 504990 | 414 |
| MR_1774412888_349431B5 | 504990 | 455 | -89.6 | 504990 | 196 | -93.4 | 504990 | 472 | -97.3 | 504990 | 414 |
| MR_1774412888_10040FB5 | 504990 | 455 | -88.6 | 504990 | 196 | -95.8 | 504990 | 472 | -94.9 | 504990 | 414 |
| MR_1774412888_FF4F11AC | 504990 | 455 | -89.0 | 504990 | 196 | -96.0 | 504990 | 472 | -96.2 | 504990 | 414 |
| MR_1774412888_F6D6E8E6 | 504990 | 455 | -87.2 | 504990 | 196 | -93.0 | 504990 | 472 | -95.0 | 504990 | 414 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1855: `85545a36-150...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `85545a36-1504-41c5-bdf9-9fcba43c7d39` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Add neighbor relationship between 3252088_4 and 3224448_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1855] topology](images/train_1855.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252088_4
- `C2`: Decrease A3 Offset threshold for 3252088_4
- `C3`: Lift the tilt angle of 3252088_4 by 4 degrees
- `C4`: Lift the tilt angle  of 3224448_3 by 6 degrees
- `C5`: Add neighbor relationship between 3236120_1 and 3224448_3
- `C6`: Increase transmission power for 3224448_3
- `C7`: Decrease transmission power for 3252088_4
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Adjust the azimuth of 3252088_4 by 50 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252088_4
- `C11`: Press down the tilt angle of 3252088_4 by 4 degrees
- `C12`: Check test server and transmission issues
- `C13`: Adjust the azimuth of 3224448_3 by 18 degrees
- `C14`: Press down the tilt angle  of 3224448_3 by 6 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224448_3
- `C16`: Increase A3 Offset threshold for 3224448_3
- `C17`: Increase transmission power for 3252088_4
- `C18`: Decrease transmission power for 3224448_3
- `C19`: Add neighbor relationship between 3252088_4 and 3224448_3 **← 정답**
- `C20`: Decrease A3 Offset threshold for 3224448_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224448_3
- `C22`: Increase A3 Offset threshold for 3252088_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.801 | MS1 | 121.4656587829 | 31.1446320662 | 631 | 504990 | -79.78 | 17.80 | 344.52 | 0.02 | 2.81 | 1594 |
| 2024-09-20 22:21:32.282 | MS1 | 121.4656609213 | 31.1446257473 | 631 | 504990 | -82.81 | 15.24 | 389.49 | 0.09 | 2.86 | 1592 |
| 2024-09-20 22:21:33.717 | MS1 | 121.4656645570 | 31.1446189540 | 631 | 504990 | -76.39 | 14.73 | 495.48 | 0.13 | 2.14 | 1597 |
| 2024-09-20 22:21:34.432 | MS1 | 121.4656745026 | 31.1446251411 | 631 | 504990 | -86.32 | -1.03 | 44.65 | 0.20 | 1.17 | 1582 |
| 2024-09-20 22:21:35.177 | MS1 | 121.4656626439 | 31.1446358909 | 631 | 504990 | -91.75 | -2.38 | 68.12 | 0.16 | 1.21 | 1573 |
| 2024-09-20 22:21:36.681 | MS1 | 121.4656724821 | 31.1446362877 | 631 | 504990 | -94.36 | -3.92 | 44.52 | 0.09 | 1.13 | 1568 |
| 2024-09-20 22:21:37.957 | MS1 | 121.4656657604 | 31.1446347973 | 631 | 504990 | -89.24 | -0.25 | 39.33 | 0.17 | 1.34 | 1594 |
| 2024-09-20 22:21:38.969 | MS1 | 121.4656627421 | 31.1446305514 | 631 | 504990 | -77.74 | 15.86 | 520.86 | 0.01 | 1.35 | 1595 |
| 2024-09-20 22:21:39.410 | MS1 | 121.4656669680 | 31.1446221863 | 631 | 504990 | -82.29 | 14.26 | 403.60 | 0.20 | 1.19 | 1600 |
| 2024-09-20 22:21:40.123 | MS1 | 121.4656645495 | 31.1446346390 | 631 | 504990 | -83.43 | 17.38 | 347.32 | 0.19 | 2.23 | 1575 |
| 2024-09-20 22:21:41.410 | MS1 | 121.4656696702 | 31.1446293710 | 631 | 504990 | -80.27 | 16.58 | 449.63 | 0.14 | 2.22 | 1565 |
| 2024-09-20 22:21:42.155 | MS1 | 121.4656609784 | 31.1446279012 | 631 | 504990 | -78.77 | 13.12 | 359.92 | 0.17 | 2.06 | 1563 |

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
| 3213462 | 2 | 121.4641755020 | 31.1447623585 | 343 | 5 | 7 | 44.4 | TDD | 946 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3224448 | 3 | 121.4687217626 | 31.1510167703 | 220 | 3 | 12 | 35.9 | TDD | 260 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3236120 | 1 | 121.4640820390 | 31.1506707318 | 256 | 11 | 5 | 36.8 | TDD | 712 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3252088 | 4 | 121.4749661592 | 31.1555159346 | 18 | 2 | 11 | 43.0 | TDD | 631 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.138 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.284 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.284 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.942 | NREventA3 | measId:2;ServCellPCI:821;Se... |
| 2024-09-20 22:21:35.942 | NREventA3 | measId:2;ServCellPCI:821;Se... |
| 2024-09-20 22:21:36.942 | NREventA3 | measId:2;ServCellPCI:821;Se... |
| 2024-09-20 22:21:39.442 | NRRRCReestablishAttempt | PCI:821 |
| 2024-09-20 22:21:39.456 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.471 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.598 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.598 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236120 | 1 | 15.8567 | 11.1336 | -115.2615 | 8.2791 | 96.1070 | 0.0078 | 0.0169 |
| 2024_09_20 22:00 | 3213462 | 2 | 5.8849 | 9.0472 | -117.9276 | 11.7610 | 158.5032 | 0.0159 | 0.0130 |
| 2024_09_20 22:00 | 3224448 | 3 | 17.8618 | 13.1246 | -116.9167 | 13.4790 | 153.3636 | 0.0111 | 0.0104 |
| 2024_09_20 22:00 | 3252088 | 4 | 9.4019 | 13.8870 | -114.7602 | 6.7245 | 123.8295 | 0.0026 | 0.1711 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412047_B6C8849C | 504990 | 260 | -81.8 | 504990 | 631 | -85.8 | 504990 | 712 | -91.6 | 504990 | 946 |
| MR_1774412047_72C8E96C | 504990 | 631 | -87.0 | 504990 | 260 | -81.6 | 504990 | 712 | -90.8 | 504990 | 946 |
| MR_1774412047_C07398EB | 504990 | 631 | -86.4 | 504990 | 260 | -81.9 | 504990 | 712 | -89.3 | 504990 | 946 |
| MR_1774412047_80B764B7 | 504990 | 631 | -87.7 | 504990 | 260 | -83.6 | 504990 | 712 | -92.2 | 504990 | 946 |
| MR_1774412047_32447EF9 | 504990 | 260 | -81.3 | 504990 | 631 | -87.1 | 504990 | 712 | -88.7 | 504990 | 946 |
| MR_1774412047_594FE60C | 504990 | 631 | -84.8 | 504990 | 260 | -81.6 | 504990 | 712 | -92.4 | 504990 | 946 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1856: `d99ce32d-dee...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d99ce32d-deee-48fe-82e2-83b4a1783c57` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1856] topology](images/train_1856.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3229272_3
- `C2`: Increase A3 Offset threshold for 3229272_3
- `C3`: Add neighbor relationship between 3268634_4 and 3229272_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229272_3
- `C5`: Decrease transmission power for 3229272_3
- `C6`: Add neighbor relationship between 3233875_2 and 3229272_3
- `C7`: Increase A3 Offset threshold for 3233875_2
- `C8`: Increase transmission power for 3233875_2
- `C9`: Adjust the azimuth of 3229272_3 by 50 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233875_2
- `C11`: Press down the tilt angle  of 3229272_3 by 3 degrees
- `C12`: Lift the tilt angle  of 3229272_3 by 3 degrees
- `C13`: Increase transmission power for 3229272_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229272_3
- `C15`: Check test server and transmission issues **← 정답**
- `C16`: Lift the tilt angle of 3233875_2 by 2 degrees
- `C17`: Decrease A3 Offset threshold for 3233875_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233875_2
- `C19`: Decrease transmission power for 3233875_2
- `C20`: Press down the tilt angle of 3233875_2 by 2 degrees
- `C21`: Adjust the azimuth of 3233875_2 by 50 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.122 | MS1 | 121.4656738930 | 31.1446224764 | 714 | 504990 | -91.82 | 13.89 | 423.41 | 0.01 | 2.65 | 1585 |
| 2024-09-20 22:21:32.173 | MS1 | 121.4656767514 | 31.1446327412 | 714 | 504990 | -91.21 | 16.67 | 482.95 | 0.08 | 2.36 | 1574 |
| 2024-09-20 22:21:33.570 | MS1 | 121.4656763062 | 31.1446367702 | 714 | 504990 | -85.75 | 12.77 | 400.26 | 0.10 | 2.08 | 1597 |
| 2024-09-20 22:21:34.962 | MS1 | 121.4656762082 | 31.1446236462 | 714 | 504990 | -90.47 | 17.21 | 104.30 | 0.07 | 2.52 | 348 |
| 2024-09-20 22:21:35.488 | MS1 | 121.4656684424 | 31.1446228826 | 714 | 504990 | -86.33 | 14.72 | 59.75 | 0.07 | 2.83 | 407 |
| 2024-09-20 22:21:36.268 | MS1 | 121.4656752217 | 31.1446248581 | 714 | 504990 | -90.06 | 17.32 | 86.43 | 0.05 | 2.03 | 370 |
| 2024-09-20 22:21:37.716 | MS1 | 121.4656677993 | 31.1446268115 | 714 | 504990 | -92.35 | 10.51 | 59.22 | 0.05 | 2.46 | 306 |
| 2024-09-20 22:21:38.547 | MS1 | 121.4656666093 | 31.1446347338 | 714 | 504990 | -90.22 | 10.20 | 96.44 | 0.19 | 2.93 | 456 |
| 2024-09-20 22:21:39.561 | MS1 | 121.4656741036 | 31.1446351919 | 714 | 504990 | -93.63 | 11.65 | 92.94 | 0.08 | 2.60 | 428 |
| 2024-09-20 22:21:40.452 | MS1 | 121.4656678760 | 31.1446207146 | 714 | 504990 | -89.31 | 9.97 | 605.36 | 0.08 | 2.09 | 1594 |
| 2024-09-20 22:21:41.673 | MS1 | 121.4656693415 | 31.1446326061 | 714 | 504990 | -93.46 | 10.14 | 292.53 | 0.16 | 2.34 | 1579 |
| 2024-09-20 22:21:42.585 | MS1 | 121.4656597836 | 31.1446327020 | 714 | 504990 | -92.77 | 11.88 | 535.87 | 0.20 | 2.73 | 1584 |

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
| 3229272 | 3 | 121.4699341488 | 31.1464685532 | 33 | 0 | 12 | 25.8 | TDD | 349 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3233875 | 2 | 121.4753280618 | 31.1520208051 | 56 | 0 | 6 | 33.4 | TDD | 714 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3263798 | 1 | 121.4733556600 | 31.1552116377 | 246 | 1 | 1 | 26.1 | TDD | 448 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3268634 | 4 | 121.4673485896 | 31.1479691191 | 340 | 6 | 12 | 44.7 | TDD | 346 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.110 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.130 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.277 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.277 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.958 | NREventA3 | measId:2;ServCellPCI:7;Serv... |
| 2024-09-20 22:21:38.198 | NRHandoverAttempt | SourcePCI:7;SourceNR-ARFCN:... |
| 2024-09-20 22:21:38.232 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.246 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.349 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.349 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263798 | 1 | 7.3411 | 17.1730 | -114.1182 | 14.7806 | 99.8451 | 0.0048 | 0.0094 |
| 2024_09_20 22:00 | 3233875 | 2 | 16.1452 | 7.7405 | -116.9729 | 13.2082 | 127.3847 | 0.0169 | 0.0113 |
| 2024_09_20 22:00 | 3229272 | 3 | 16.4325 | 11.5858 | -115.1477 | 8.4843 | 149.7726 | 0.0003 | 0.0093 |
| 2024_09_20 22:00 | 3268634 | 4 | 12.0995 | 9.5592 | -114.2769 | 7.9057 | 146.8059 | 0.0162 | 0.0090 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414739_C19DA267 | 504990 | 714 | -85.7 | 504990 | 349 | -90.7 | 504990 | 346 | -95.7 | 504990 | 448 |
| MR_1774414739_AF69F8A5 | 504990 | 714 | -84.9 | 504990 | 349 | -90.6 | 504990 | 346 | -97.7 | 504990 | 448 |
| MR_1774414739_00EBD3C0 | 504990 | 714 | -84.7 | 504990 | 349 | -92.4 | 504990 | 346 | -94.7 | 504990 | 448 |
| MR_1774414739_45F269E2 | 504990 | 714 | -85.3 | 504990 | 349 | -92.9 | 504990 | 346 | -97.6 | 504990 | 448 |
| MR_1774414739_092A9E57 | 504990 | 714 | -85.4 | 504990 | 349 | -92.4 | 504990 | 346 | -97.8 | 504990 | 448 |
| MR_1774414739_B4E35C29 | 504990 | 714 | -84.8 | 504990 | 349 | -91.4 | 504990 | 346 | -97.0 | 504990 | 448 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1857: `10f26d88-72c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `10f26d88-72c6-4e29-82f0-49f301655ca2` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Add neighbor relationship between 3239540_4 and 3278646_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1857] topology](images/train_1857.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3278646_2 by 3 degrees
- `C2`: Increase transmission power for 3278646_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239540_4
- `C4`: Add neighbor relationship between 3241768_3 and 3278646_2
- `C5`: Press down the tilt angle  of 3278646_2 by 3 degrees
- `C6`: Check test server and transmission issues
- `C7`: Increase transmission power for 3239540_4
- `C8`: Adjust the azimuth of 3278646_2 by 11 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239540_4
- `C10`: Adjust the azimuth of 3239540_4 by 7 degrees
- `C11`: Add neighbor relationship between 3239540_4 and 3278646_2 **← 정답**
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278646_2
- `C13`: Decrease transmission power for 3239540_4
- `C14`: Lift the tilt angle of 3239540_4 by 7 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278646_2
- `C16`: Increase A3 Offset threshold for 3239540_4
- `C17`: Decrease A3 Offset threshold for 3278646_2
- `C18`: Increase A3 Offset threshold for 3278646_2
- `C19`: Decrease transmission power for 3278646_2
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease A3 Offset threshold for 3239540_4
- `C22`: Press down the tilt angle of 3239540_4 by 7 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.987 | MS1 | 121.4656670380 | 31.1446210330 | 534 | 504990 | -84.43 | 12.89 | 370.04 | 0.08 | 2.17 | 1599 |
| 2024-09-20 22:21:32.717 | MS1 | 121.4656633863 | 31.1446331082 | 534 | 504990 | -75.12 | 16.73 | 555.61 | 0.06 | 2.78 | 1565 |
| 2024-09-20 22:21:33.305 | MS1 | 121.4656728739 | 31.1446254825 | 534 | 504990 | -82.41 | 15.96 | 395.50 | 0.11 | 2.08 | 1593 |
| 2024-09-20 22:21:34.899 | MS1 | 121.4656591692 | 31.1446288825 | 534 | 504990 | -87.99 | -3.35 | 60.55 | 0.15 | 1.33 | 1597 |
| 2024-09-20 22:21:35.131 | MS1 | 121.4656623376 | 31.1446340615 | 534 | 504990 | -93.85 | -3.22 | 42.80 | 0.04 | 1.00 | 1592 |
| 2024-09-20 22:21:36.696 | MS1 | 121.4656666141 | 31.1446298191 | 534 | 504990 | -91.31 | -1.27 | 45.73 | 0.07 | 1.07 | 1580 |
| 2024-09-20 22:21:37.832 | MS1 | 121.4656707736 | 31.1446243407 | 534 | 504990 | -88.74 | -2.39 | 43.12 | 0.19 | 1.30 | 1563 |
| 2024-09-20 22:21:38.614 | MS1 | 121.4656737241 | 31.1446230091 | 534 | 504990 | -78.90 | 16.07 | 328.80 | 0.08 | 1.13 | 1572 |
| 2024-09-20 22:21:39.609 | MS1 | 121.4656697517 | 31.1446331103 | 534 | 504990 | -84.35 | 16.91 | 460.92 | 0.14 | 1.33 | 1583 |
| 2024-09-20 22:21:40.801 | MS1 | 121.4656747629 | 31.1446336164 | 534 | 504990 | -82.18 | 13.73 | 414.11 | 0.06 | 2.24 | 1598 |
| 2024-09-20 22:21:41.649 | MS1 | 121.4656630516 | 31.1446327230 | 534 | 504990 | -84.16 | 12.28 | 338.90 | 0.05 | 2.89 | 1574 |
| 2024-09-20 22:21:42.714 | MS1 | 121.4656750824 | 31.1446240981 | 534 | 504990 | -76.33 | 14.22 | 481.25 | 0.11 | 2.97 | 1565 |

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
| 3239540 | 4 | 121.4640851725 | 31.1494946847 | 157 | 3 | 0 | 42.7 | TDD | 534 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3241768 | 3 | 121.4705108433 | 31.1474017576 | 337 | 2 | 8 | 27.2 | TDD | 989 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3272202 | 1 | 121.4745507141 | 31.1462762832 | 36 | 1 | 4 | 26.7 | TDD | 424 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3278646 | 2 | 121.4754926747 | 31.1448924039 | 257 | 1 | 3 | 27.1 | TDD | 748 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.924 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.945 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.076 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.076 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.748 | NREventA3 | measId:2;ServCellPCI:417;Se... |
| 2024-09-20 22:21:35.748 | NREventA3 | measId:2;ServCellPCI:417;Se... |
| 2024-09-20 22:21:36.748 | NREventA3 | measId:2;ServCellPCI:417;Se... |
| 2024-09-20 22:21:39.248 | NRRRCReestablishAttempt | PCI:417 |
| 2024-09-20 22:21:39.258 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.269 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.389 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.389 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272202 | 1 | 16.8134 | 12.1471 | -117.0963 | 5.2731 | 188.6648 | 0.0158 | 0.0000 |
| 2024_09_20 22:00 | 3278646 | 2 | 17.4237 | 14.4737 | -116.7836 | 6.9894 | 145.3908 | 0.0144 | 0.0011 |
| 2024_09_20 22:00 | 3241768 | 3 | 19.8259 | 13.5967 | -114.9408 | 14.1778 | 80.4518 | 0.0096 | 0.0076 |
| 2024_09_20 22:00 | 3239540 | 4 | 9.7870 | 18.7419 | -115.0658 | 11.0240 | 121.7690 | 0.0124 | 0.1144 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413957_D008B1D5 | 504990 | 748 | -83.7 | 504990 | 534 | -87.8 | 504990 | 989 | -91.2 | 504990 | 424 |
| MR_1774413957_9AAA9A78 | 504990 | 748 | -81.3 | 504990 | 534 | -88.4 | 504990 | 989 | -90.9 | 504990 | 424 |
| MR_1774413957_3ECDF015 | 504990 | 534 | -89.2 | 504990 | 748 | -81.6 | 504990 | 989 | -91.4 | 504990 | 424 |
| MR_1774413957_B5A151F8 | 504990 | 534 | -86.6 | 504990 | 748 | -82.2 | 504990 | 989 | -89.5 | 504990 | 424 |
| MR_1774413957_C7AFBFF0 | 504990 | 534 | -90.0 | 504990 | 748 | -83.7 | 504990 | 989 | -89.3 | 504990 | 424 |
| MR_1774413957_E792A5EC | 504990 | 748 | -82.2 | 504990 | 534 | -89.8 | 504990 | 989 | -89.1 | 504990 | 424 |
| MR_1774413957_85B88FA5 | 504990 | 534 | -87.9 | 504990 | 748 | -82.1 | 504990 | 989 | -91.8 | 504990 | 424 |
| MR_1774413957_4EC38FDE | 504990 | 748 | -83.1 | 504990 | 534 | -88.8 | 504990 | 989 | -92.4 | 504990 | 424 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1858: `3c031fab-984...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3c031fab-984f-43f7-8585-da79e6af4b18` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3267865_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1858] topology](images/train_1858.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3267865_1 by 38 degrees
- `C2`: Press down the tilt angle of 3267865_1 by 4 degrees
- `C3`: Add neighbor relationship between 3255148_4 and 3265566_2
- `C4`: Decrease A3 Offset threshold for 3265566_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265566_2
- `C6`: Lift the tilt angle of 3267865_1 by 4 degrees
- `C7`: Decrease transmission power for 3265566_2
- `C8`: Lift the tilt angle  of 3265566_2 by 5 degrees
- `C9`: Increase A3 Offset threshold for 3265566_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265566_2
- `C11`: Adjust the azimuth of 3265566_2 by 50 degrees
- `C12`: Press down the tilt angle  of 3265566_2 by 5 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267865_1
- `C14`: Decrease A3 Offset threshold for 3267865_1
- `C15`: Add neighbor relationship between 3267865_1 and 3265566_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267865_1 **← 정답**
- `C17`: Increase A3 Offset threshold for 3267865_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Check test server and transmission issues
- `C20`: Decrease transmission power for 3267865_1
- `C21`: Increase transmission power for 3265566_2
- `C22`: Increase transmission power for 3267865_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.258 | MS1 | 121.4656642843 | 31.1446379592 | 253 | 504990 | -90.81 | 17.60 | 393.07 | 0.13 | 2.27 | 1596 |
| 2024-09-20 22:21:32.288 | MS1 | 121.4656689750 | 31.1446367065 | 253 | 504990 | -87.94 | 15.74 | 517.03 | 0.02 | 2.57 | 1582 |
| 2024-09-20 22:21:33.921 | MS1 | 121.4656743991 | 31.1446278355 | 253 | 504990 | -90.00 | 15.95 | 446.72 | 0.05 | 2.30 | 1565 |
| 2024-09-20 22:21:34.370 | MS1 | 121.4656733518 | 31.1446268241 | 253 | 504990 | -91.94 | 14.97 | 80.07 | 0.52 | 2.48 | 575 |
| 2024-09-20 22:21:35.730 | MS1 | 121.4656676156 | 31.1446325515 | 253 | 504990 | -87.46 | 16.08 | 93.37 | 0.57 | 2.80 | 663 |
| 2024-09-20 22:21:36.420 | MS1 | 121.4656610853 | 31.1446351137 | 253 | 504990 | -86.96 | 13.86 | 81.36 | 0.59 | 2.77 | 696 |
| 2024-09-20 22:21:37.253 | MS1 | 121.4656649495 | 31.1446193342 | 253 | 504990 | -91.10 | 10.60 | 48.52 | 0.53 | 2.93 | 582 |
| 2024-09-20 22:21:38.843 | MS1 | 121.4656777128 | 31.1446349418 | 253 | 504990 | -89.85 | 11.02 | 88.67 | 0.65 | 2.69 | 598 |
| 2024-09-20 22:21:39.943 | MS1 | 121.4656734777 | 31.1446272609 | 253 | 504990 | -90.98 | 12.12 | 69.75 | 0.56 | 2.24 | 641 |
| 2024-09-20 22:21:40.727 | MS1 | 121.4656582747 | 31.1446313971 | 253 | 504990 | -93.04 | 7.45 | 443.96 | 0.13 | 2.46 | 1588 |
| 2024-09-20 22:21:41.574 | MS1 | 121.4656689672 | 31.1446190394 | 253 | 504990 | -91.10 | 8.36 | 377.73 | 0.09 | 2.21 | 1583 |
| 2024-09-20 22:21:42.941 | MS1 | 121.4656610966 | 31.1446321684 | 253 | 504990 | -90.37 | 12.46 | 332.18 | 0.10 | 2.76 | 1588 |

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
| 3229273 | 3 | 121.4653602959 | 31.1537310438 | 4 | 1 | 7 | 46.6 | TDD | 325 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3255148 | 4 | 121.4666799541 | 31.1509670063 | 127 | 11 | 1 | 16.3 | TDD | 846 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3265566 | 2 | 121.4653497309 | 31.1512661371 | 24 | 2 | 11 | 42.9 | TDD | 214 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3267865 | 1 | 121.4702636481 | 31.1462209251 | 210 | 0 | 4 | 34.4 | TDD | 253 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.306 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.324 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.452 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.452 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.147 | NREventA3 | measId:2;ServCellPCI:974;Se... |
| 2024-09-20 22:21:38.387 | NRHandoverAttempt | SourcePCI:974;SourceNR-ARFC... |
| 2024-09-20 22:21:38.421 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.432 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.579 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.579 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267865 | 1 | 8.1693 | 19.6334 | -117.6482 | 19.8605 | 97.9446 | 0.0134 | 0.0185 |
| 2024_09_20 22:00 | 3265566 | 2 | 17.1830 | 13.6851 | -114.8304 | 19.5129 | 133.4649 | 0.0061 | 0.0192 |
| 2024_09_20 22:00 | 3229273 | 3 | 9.2092 | 8.8489 | -117.2497 | 8.7184 | 82.4856 | 0.0003 | 0.0086 |
| 2024_09_20 22:00 | 3255148 | 4 | 14.8948 | 8.2934 | -117.1668 | 7.8040 | 168.2453 | 0.0184 | 0.0047 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417017_C6EF2CF8 | 504990 | 253 | -92.9 | 504990 | 214 | -94.7 | 504990 | 846 | -103.1 | 504990 | 325 |
| MR_1774417017_E17FB109 | 504990 | 253 | -92.9 | 504990 | 214 | -94.2 | 504990 | 846 | -105.5 | 504990 | 325 |
| MR_1774417017_7748FD21 | 504990 | 253 | -93.6 | 504990 | 214 | -95.1 | 504990 | 846 | -104.0 | 504990 | 325 |
| MR_1774417017_AD39CABA | 504990 | 253 | -91.0 | 504990 | 214 | -94.2 | 504990 | 846 | -104.8 | 504990 | 325 |
| MR_1774417017_B9B86CC8 | 504990 | 253 | -91.5 | 504990 | 214 | -94.0 | 504990 | 846 | -102.8 | 504990 | 325 |
| MR_1774417017_74DA38A0 | 504990 | 253 | -92.9 | 504990 | 214 | -95.5 | 504990 | 846 | -103.8 | 504990 | 325 |
| MR_1774417017_6D4BBE4F | 504990 | 253 | -92.8 | 504990 | 214 | -92.6 | 504990 | 846 | -105.5 | 504990 | 325 |
| MR_1774417017_B88D7ADC | 504990 | 253 | -93.0 | 504990 | 214 | -95.3 | 504990 | 846 | -105.1 | 504990 | 325 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1859: `68d9cc76-086...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `68d9cc76-0862-42ee-a54c-407009b93b0b` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Lift the tilt angle  of 3263759_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1859] topology](images/train_1859.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3277127_4
- `C2`: Add neighbor relationship between 3263759_3 and 3258842_2
- `C3`: Increase A3 Offset threshold for 3258842_2
- `C4`: Adjust the azimuth of 3263759_3 by 38 degrees
- `C5`: Decrease transmission power for 3258842_2
- `C6`: Decrease A3 Offset threshold for 3258842_2
- `C7`: Check test server and transmission issues
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Press down the tilt angle  of 3263759_3 by 10 degrees
- `C10`: Increase transmission power for 3277127_4
- `C11`: Lift the tilt angle  of 3263759_3 by 10 degrees **← 정답**
- `C12`: Increase transmission power for 3258842_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258842_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277127_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277127_4
- `C16`: Press down the tilt angle of 3277127_4 by 2 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258842_2
- `C18`: Decrease transmission power for 3277127_4
- `C19`: Add neighbor relationship between 3277127_4 and 3258842_2
- `C20`: Increase A3 Offset threshold for 3277127_4
- `C21`: Lift the tilt angle of 3277127_4 by 2 degrees
- `C22`: Adjust the azimuth of 3277127_4 by 14 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.989 | MS1 | 121.4656690646 | 31.1446240078 | 804 | 504990 | -86.76 | 13.49 | 295.40 | 0.01 | 2.91 | 1573 |
| 2024-09-20 22:21:32.997 | MS1 | 121.4656590228 | 31.1446209319 | 804 | 504990 | -89.93 | 15.79 | 381.07 | 0.19 | 2.37 | 1580 |
| 2024-09-20 22:21:33.260 | MS1 | 121.4656650417 | 31.1446272023 | 804 | 504990 | -85.46 | 13.02 | 509.94 | 0.18 | 2.90 | 1564 |
| 2024-09-20 22:21:34.140 | MS1 | 121.4656693727 | 31.1446290782 | 804 | 504990 | -88.71 | 15.88 | 76.79 | 0.18 | 2.99 | 1570 |
| 2024-09-20 22:21:35.640 | MS1 | 121.4656598985 | 31.1446355938 | 804 | 504990 | -86.59 | 12.64 | 79.85 | 0.01 | 2.14 | 1577 |
| 2024-09-20 22:21:36.936 | MS1 | 121.4656706630 | 31.1446207258 | 804 | 504990 | -91.47 | 16.42 | 85.57 | 0.06 | 2.58 | 1572 |
| 2024-09-20 22:21:37.689 | MS1 | 121.4656637804 | 31.1446316410 | 804 | 504990 | -91.63 | 10.66 | 63.45 | 0.10 | 2.96 | 1567 |
| 2024-09-20 22:21:38.400 | MS1 | 121.4656640250 | 31.1446308760 | 804 | 504990 | -90.08 | 7.90 | 85.33 | 0.06 | 2.65 | 1588 |
| 2024-09-20 22:21:39.735 | MS1 | 121.4656745033 | 31.1446316198 | 804 | 504990 | -93.37 | 9.47 | 68.46 | 0.11 | 2.82 | 1571 |
| 2024-09-20 22:21:40.243 | MS1 | 121.4656712566 | 31.1446195493 | 804 | 504990 | -89.73 | 9.09 | 396.18 | 0.06 | 2.07 | 1594 |
| 2024-09-20 22:21:41.221 | MS1 | 121.4656730582 | 31.1446372253 | 804 | 504990 | -90.89 | 7.60 | 301.70 | 0.19 | 2.43 | 1590 |
| 2024-09-20 22:21:42.581 | MS1 | 121.4656585720 | 31.1446196172 | 804 | 504990 | -93.71 | 8.47 | 309.92 | 0.00 | 2.50 | 1589 |

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
| 3242710 | 1 | 121.4659536404 | 31.1539908066 | 347 | 14 | 12 | 23.6 | TDD | 840 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3258842 | 2 | 121.4652572019 | 31.1541936509 | 140 | 15 | 12 | 42.4 | TDD | 642 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3263759 | 3 | 121.4720390805 | 31.1498914909 | 18 | 13 | 10 | 32.6 | TDD | 563 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3277127 | 4 | 121.4653915045 | 31.1549407868 | 165 | 1 | 3 | 28.2 | TDD | 804 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.452 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.473 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.601 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.601 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.281 | NREventA3 | measId:2;ServCellPCI:285;Se... |
| 2024-09-20 22:21:38.521 | NRHandoverAttempt | SourcePCI:285;SourceNR-ARFC... |
| 2024-09-20 22:21:38.551 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.562 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.691 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.691 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242710 | 1 | 5.0331 | 19.1468 | -116.5019 | 6.0290 | 91.4978 | 0.0086 | 0.0131 |
| 2024_09_20 22:00 | 3258842 | 2 | 7.1973 | 17.9164 | -114.1669 | 16.0990 | 137.0976 | 0.0086 | 0.0063 |
| 2024_09_20 22:00 | 3263759 | 3 | 19.4074 | 6.9426 | -114.0550 | 14.4156 | 174.5035 | 0.0019 | 0.0076 |
| 2024_09_20 22:00 | 3277127 | 4 | 78.7863 | 81.6858 | -117.1756 | 10.6259 | 106.2389 | 0.0200 | 0.0113 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412807_0A4974D6 | 504990 | 804 | -88.4 | 504990 | 642 | -91.6 | 504990 | 563 | -99.2 | 504990 | 840 |
| MR_1774412807_D1201929 | 504990 | 804 | -88.3 | 504990 | 642 | -91.2 | 504990 | 563 | -97.6 | 504990 | 840 |
| MR_1774412807_5CB2FBA1 | 504990 | 804 | -87.6 | 504990 | 642 | -90.9 | 504990 | 563 | -97.2 | 504990 | 840 |
| MR_1774412807_15DAFC36 | 504990 | 804 | -89.7 | 504990 | 642 | -93.1 | 504990 | 563 | -97.3 | 504990 | 840 |
| MR_1774412807_931E3458 | 504990 | 804 | -90.1 | 504990 | 642 | -94.1 | 504990 | 563 | -97.3 | 504990 | 840 |
| MR_1774412807_B378CF8E | 504990 | 804 | -88.9 | 504990 | 642 | -92.6 | 504990 | 563 | -99.0 | 504990 | 840 |
| MR_1774412807_F3E7FA4F | 504990 | 804 | -87.3 | 504990 | 642 | -92.2 | 504990 | 563 | -100.0 | 504990 | 840 |
| MR_1774412807_932421E3 | 504990 | 804 | -89.1 | 504990 | 642 | -92.3 | 504990 | 563 | -98.8 | 504990 | 840 |

> *... 2개 열 생략 (전체 14열)*

---
