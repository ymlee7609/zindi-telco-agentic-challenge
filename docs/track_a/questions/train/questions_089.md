# Track A 문제 분석 — train[880]~train[889]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[880] ~ train[889] (10개)

## 목차

1. [문제 880: `4654006d-1a7...`](#880) — single-answer, 정답: C16
2. [문제 881: `37d4c5ce-19a...`](#881) — single-answer, 정답: C3
3. [문제 882: `2a765196-374...`](#882) — single-answer, 정답: C7
4. [문제 883: `d415f6ce-fca...`](#883) — single-answer, 정답: C13
5. [문제 884: `bd48acc8-73a...`](#884) — single-answer, 정답: C16
6. [문제 885: `0430384d-11d...`](#885) — single-answer, 정답: C15
7. [문제 886: `70eaac8a-b06...`](#886) — single-answer, 정답: C22
8. [문제 887: `a6b1b747-f0d...`](#887) — single-answer, 정답: C7
9. [문제 888: `d7ee6d02-91f...`](#888) — multiple-answer, 정답: C5|C11
10. [문제 889: `894b732f-70a...`](#889) — single-answer, 정답: C14

---

### 문제 880: `4654006d-1a7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4654006d-1a77-4a97-b019-dfb7662af6ef` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Lift the tilt angle  of 3275801_2 by 4 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[880] topology](images/train_0880.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249216_4
- `C2`: Press down the tilt angle of 3217300_1 by 4 degrees
- `C3`: Increase transmission power for 3217300_1
- `C4`: Adjust the azimuth of 3217300_1 by 20 degrees
- `C5`: Check test server and transmission issues
- `C6`: Add neighbor relationship between 3275801_2 and 3249216_4
- `C7`: Decrease A3 Offset threshold for 3249216_4
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase A3 Offset threshold for 3217300_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249216_4
- `C11`: Increase A3 Offset threshold for 3249216_4
- `C12`: Increase transmission power for 3249216_4
- `C13`: Adjust the azimuth of 3275801_2 by 50 degrees
- `C14`: Decrease transmission power for 3249216_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217300_1
- `C16`: Lift the tilt angle  of 3275801_2 by 4 degrees **← 정답**
- `C17`: Add neighbor relationship between 3217300_1 and 3249216_4
- `C18`: Decrease A3 Offset threshold for 3217300_1
- `C19`: Press down the tilt angle  of 3275801_2 by 4 degrees
- `C20`: Lift the tilt angle of 3217300_1 by 4 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217300_1
- `C22`: Decrease transmission power for 3217300_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.928 | MS1 | 121.4656686862 | 31.1446234197 | 320 | 504990 | -88.93 | 14.31 | 403.58 | 0.10 | 2.77 | 1571 |
| 2024-09-20 22:21:32.511 | MS1 | 121.4656757265 | 31.1446257278 | 320 | 504990 | -85.17 | 14.17 | 429.40 | 0.11 | 2.23 | 1596 |
| 2024-09-20 22:21:33.874 | MS1 | 121.4656752101 | 31.1446216199 | 320 | 504990 | -91.16 | 12.55 | 486.72 | 0.02 | 2.18 | 1577 |
| 2024-09-20 22:21:34.119 | MS1 | 121.4656595297 | 31.1446184745 | 320 | 504990 | -91.25 | 17.26 | 88.46 | 0.02 | 2.19 | 1565 |
| 2024-09-20 22:21:35.996 | MS1 | 121.4656678751 | 31.1446213977 | 320 | 504990 | -88.01 | 16.49 | 80.06 | 0.18 | 2.88 | 1563 |
| 2024-09-20 22:21:36.869 | MS1 | 121.4656733144 | 31.1446308230 | 320 | 504990 | -89.82 | 14.31 | 96.34 | 0.10 | 2.75 | 1598 |
| 2024-09-20 22:21:37.772 | MS1 | 121.4656659114 | 31.1446190859 | 320 | 504990 | -90.79 | 12.04 | 54.47 | 0.15 | 2.80 | 1598 |
| 2024-09-20 22:21:38.512 | MS1 | 121.4656768734 | 31.1446266079 | 320 | 504990 | -92.38 | 8.13 | 87.78 | 0.04 | 2.54 | 1598 |
| 2024-09-20 22:21:39.976 | MS1 | 121.4656738243 | 31.1446375936 | 320 | 504990 | -93.60 | 10.78 | 61.55 | 0.11 | 2.25 | 1573 |
| 2024-09-20 22:21:40.569 | MS1 | 121.4656597768 | 31.1446353456 | 320 | 504990 | -91.51 | 9.88 | 311.23 | 0.17 | 2.09 | 1598 |
| 2024-09-20 22:21:41.855 | MS1 | 121.4656723009 | 31.1446356440 | 320 | 504990 | -92.79 | 7.99 | 403.55 | 0.18 | 2.53 | 1589 |
| 2024-09-20 22:21:42.634 | MS1 | 121.4656745215 | 31.1446332530 | 320 | 504990 | -92.28 | 7.19 | 589.69 | 0.19 | 2.28 | 1583 |

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
| 3217300 | 1 | 121.4749233401 | 31.1467719747 | 275 | 2 | 8 | 36.3 | TDD | 320 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3226363 | 3 | 121.4683053824 | 31.1499671961 | 133 | 14 | 9 | 19.7 | TDD | 430 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3249216 | 4 | 121.4758669505 | 31.1448438149 | 199 | 2 | 3 | 39.9 | TDD | 311 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3275801 | 2 | 121.4661315384 | 31.1443279056 | 182 | 14 | 11 | 32.1 | TDD | 610 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.066 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.088 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.191 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.191 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.916 | NREventA3 | measId:2;ServCellPCI:334;Se... |
| 2024-09-20 22:21:38.156 | NRHandoverAttempt | SourcePCI:334;SourceNR-ARFC... |
| 2024-09-20 22:21:38.195 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.207 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.315 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.315 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217300 | 1 | 94.1622 | 94.8154 | -115.1394 | 13.3483 | 184.9765 | 0.0115 | 0.0065 |
| 2024_09_20 22:00 | 3275801 | 2 | 6.7882 | 9.7968 | -116.9633 | 14.1870 | 127.4545 | 0.0108 | 0.0085 |
| 2024_09_20 22:00 | 3226363 | 3 | 5.9671 | 13.4527 | -117.1976 | 19.9831 | 129.4929 | 0.0159 | 0.0180 |
| 2024_09_20 22:00 | 3249216 | 4 | 19.0527 | 14.4481 | -116.3838 | 5.3742 | 188.3224 | 0.0012 | 0.0129 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414816_B91194A4 | 504990 | 320 | -89.7 | 504990 | 311 | -96.5 | 504990 | 610 | -103.0 | 504990 | 430 |
| MR_1774414816_DFE1E85E | 504990 | 320 | -90.0 | 504990 | 311 | -95.7 | 504990 | 610 | -100.7 | 504990 | 430 |
| MR_1774414816_B48E2BA3 | 504990 | 320 | -90.6 | 504990 | 311 | -95.6 | 504990 | 610 | -100.4 | 504990 | 430 |
| MR_1774414816_C7C6864D | 504990 | 320 | -92.2 | 504990 | 311 | -95.6 | 504990 | 610 | -101.1 | 504990 | 430 |
| MR_1774414816_3B0D3423 | 504990 | 320 | -92.4 | 504990 | 311 | -97.8 | 504990 | 610 | -101.5 | 504990 | 430 |
| MR_1774414816_E01F56C4 | 504990 | 320 | -92.4 | 504990 | 311 | -96.1 | 504990 | 610 | -100.4 | 504990 | 430 |
| MR_1774414816_EFF177D4 | 504990 | 320 | -90.4 | 504990 | 311 | -98.3 | 504990 | 610 | -100.7 | 504990 | 430 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 881: `37d4c5ce-19a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `37d4c5ce-19a0-4fbc-9c5a-db750382f196` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Lift the tilt angle  of 3229481_4 by 4 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[881] topology](images/train_0881.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3235140_2
- `C2`: Increase A3 Offset threshold for 3268943_1
- `C3`: Lift the tilt angle  of 3229481_4 by 4 degrees **← 정답**
- `C4`: Decrease transmission power for 3235140_2
- `C5`: Decrease A3 Offset threshold for 3235140_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235140_2
- `C7`: Increase transmission power for 3268943_1
- `C8`: Increase transmission power for 3235140_2
- `C9`: Adjust the azimuth of 3229481_4 by 50 degrees
- `C10`: Press down the tilt angle  of 3229481_4 by 4 degrees
- `C11`: Press down the tilt angle of 3235140_2 by 3 degrees
- `C12`: Add neighbor relationship between 3235140_2 and 3268943_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235140_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268943_1
- `C15`: Lift the tilt angle of 3235140_2 by 3 degrees
- `C16`: Decrease A3 Offset threshold for 3268943_1
- `C17`: Check test server and transmission issues
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268943_1
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Add neighbor relationship between 3229481_4 and 3268943_1
- `C21`: Decrease transmission power for 3268943_1
- `C22`: Adjust the azimuth of 3235140_2 by 29 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.409 | MS1 | 121.4656707483 | 31.1446274591 | 339 | 504990 | -91.22 | 17.78 | 344.83 | 0.07 | 2.07 | 1570 |
| 2024-09-20 22:21:32.838 | MS1 | 121.4656725798 | 31.1446279859 | 339 | 504990 | -91.78 | 12.74 | 440.78 | 0.01 | 2.21 | 1567 |
| 2024-09-20 22:21:33.636 | MS1 | 121.4656660452 | 31.1446271005 | 339 | 504990 | -87.26 | 17.53 | 340.05 | 0.08 | 2.20 | 1567 |
| 2024-09-20 22:21:34.418 | MS1 | 121.4656721101 | 31.1446341508 | 339 | 504990 | -87.32 | 17.77 | 77.13 | 0.16 | 2.95 | 1581 |
| 2024-09-20 22:21:35.374 | MS1 | 121.4656703211 | 31.1446333510 | 339 | 504990 | -88.23 | 17.32 | 107.13 | 0.08 | 2.70 | 1580 |
| 2024-09-20 22:21:36.567 | MS1 | 121.4656704028 | 31.1446203015 | 339 | 504990 | -91.83 | 15.27 | 76.52 | 0.14 | 2.29 | 1597 |
| 2024-09-20 22:21:37.617 | MS1 | 121.4656607108 | 31.1446373584 | 339 | 504990 | -90.61 | 10.11 | 50.94 | 0.18 | 2.57 | 1570 |
| 2024-09-20 22:21:38.758 | MS1 | 121.4656602104 | 31.1446233699 | 339 | 504990 | -89.70 | 9.70 | 59.32 | 0.08 | 2.73 | 1599 |
| 2024-09-20 22:21:39.681 | MS1 | 121.4656685174 | 31.1446324511 | 339 | 504990 | -92.76 | 11.71 | 68.94 | 0.08 | 2.62 | 1569 |
| 2024-09-20 22:21:40.101 | MS1 | 121.4656692277 | 31.1446214199 | 339 | 504990 | -91.50 | 7.83 | 311.31 | 0.20 | 2.32 | 1593 |
| 2024-09-20 22:21:41.741 | MS1 | 121.4656681439 | 31.1446182743 | 339 | 504990 | -91.99 | 10.22 | 468.33 | 0.13 | 2.47 | 1570 |
| 2024-09-20 22:21:42.364 | MS1 | 121.4656723741 | 31.1446227761 | 339 | 504990 | -93.55 | 11.18 | 592.61 | 0.10 | 2.53 | 1560 |

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
| 3224213 | 3 | 121.4720633095 | 31.1462052316 | 256 | 11 | 6 | 43.7 | TDD | 756 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3229481 | 4 | 121.4699401464 | 31.1558852380 | 75 | 10 | 6 | 27.4 | TDD | 492 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3235140 | 2 | 121.4705351826 | 31.1558838655 | 229 | 2 | 2 | 20.7 | TDD | 339 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3268943 | 1 | 121.4699496183 | 31.1556020833 | 101 | 3 | 12 | 20.4 | TDD | 916 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.434 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.452 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.602 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.602 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.275 | NREventA3 | measId:2;ServCellPCI:69;Ser... |
| 2024-09-20 22:21:38.515 | NRHandoverAttempt | SourcePCI:69;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.560 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.575 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.698 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.698 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268943 | 1 | 13.6682 | 13.1831 | -114.6297 | 8.5919 | 105.8869 | 0.0147 | 0.0151 |
| 2024_09_20 22:00 | 3235140 | 2 | 82.8586 | 76.8305 | -115.3998 | 19.5400 | 137.9861 | 0.0096 | 0.0065 |
| 2024_09_20 22:00 | 3224213 | 3 | 5.9311 | 6.2994 | -115.0853 | 7.2405 | 176.8415 | 0.0109 | 0.0158 |
| 2024_09_20 22:00 | 3229481 | 4 | 18.4724 | 10.4385 | -116.7704 | 19.2745 | 130.1021 | 0.0162 | 0.0139 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415302_68D333E8 | 504990 | 339 | -86.9 | 504990 | 916 | -87.7 | 504990 | 492 | -93.2 | 504990 | 756 |
| MR_1774415302_4F097EB6 | 504990 | 339 | -88.7 | 504990 | 916 | -89.8 | 504990 | 492 | -95.7 | 504990 | 756 |
| MR_1774415302_3AADE507 | 504990 | 339 | -89.3 | 504990 | 916 | -87.8 | 504990 | 492 | -95.5 | 504990 | 756 |
| MR_1774415302_43B068A8 | 504990 | 339 | -88.6 | 504990 | 916 | -87.5 | 504990 | 492 | -93.5 | 504990 | 756 |
| MR_1774415302_DA06FA54 | 504990 | 339 | -87.2 | 504990 | 916 | -89.0 | 504990 | 492 | -96.8 | 504990 | 756 |
| MR_1774415302_190D2B5C | 504990 | 339 | -88.7 | 504990 | 916 | -88.6 | 504990 | 492 | -94.9 | 504990 | 756 |
| MR_1774415302_E18666BE | 504990 | 339 | -86.5 | 504990 | 916 | -88.0 | 504990 | 492 | -94.9 | 504990 | 756 |
| MR_1774415302_F86DF575 | 504990 | 339 | -86.1 | 504990 | 916 | -90.2 | 504990 | 492 | -96.3 | 504990 | 756 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 882: `2a765196-374...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2a765196-374f-48b5-95b0-c2e204d66e48` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250818_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[882] topology](images/train_0882.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3250818_6
- `C2`: Increase A3 Offset threshold for 3235321_4
- `C3`: Adjust the azimuth of 3235321_4 by 40 degrees
- `C4`: Adjust the azimuth of 3250818_6 by 10 degrees
- `C5`: Add neighbor relationship between 3250818_6 and 3235321_4
- `C6`: Lift the tilt angle of 3250818_6 by 5 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250818_6 **← 정답**
- `C8`: Add neighbor relationship between 3229621_12 and 3235321_4
- `C9`: Decrease A3 Offset threshold for 3235321_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235321_4
- `C11`: Lift the tilt angle  of 3235321_4 by 1 degrees
- `C12`: Decrease transmission power for 3235321_4
- `C13`: Press down the tilt angle  of 3235321_4 by 1 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235321_4
- `C15`: Increase transmission power for 3235321_4
- `C16`: Increase transmission power for 3250818_6
- `C17`: Press down the tilt angle of 3250818_6 by 5 degrees
- `C18`: Check test server and transmission issues
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250818_6
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease transmission power for 3250818_6
- `C22`: Increase A3 Offset threshold for 3250818_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.391 | MS1 | 121.4656631980 | 31.1446275348 | 215 | 504990 | -95.93 | 14.34 | 578.35 | 0.15 | 2.31 | 1571 |
| 2024-09-20 22:21:32.880 | MS1 | 121.4656595735 | 31.1446351742 | 104 | 504990 | -94.03 | 12.06 | 442.17 | 0.13 | 2.49 | 1600 |
| 2024-09-20 22:21:33.813 | MS1 | 121.4656615174 | 31.1446364724 | 626 | 504990 | -93.20 | 13.09 | 324.31 | 0.18 | 2.23 | 1583 |
| 2024-09-20 22:21:34.584 | MS1 | 121.4656677352 | 31.1446185156 | 332 | 152650 | -87.82 | 5.44 | 97.71 | 0.10 | 1.99 | 977 |
| 2024-09-20 22:21:35.336 | MS1 | 121.4656638165 | 31.1446214004 | 177 | 152650 | -96.75 | 6.35 | 54.19 | 0.01 | 1.72 | 965 |
| 2024-09-20 22:21:36.633 | MS1 | 121.4656674144 | 31.1446328483 | 660 | 152650 | -94.43 | 3.41 | 95.15 | 0.14 | 1.69 | 952 |
| 2024-09-20 22:21:37.653 | MS1 | 121.4656729778 | 31.1446235732 | 816 | 152650 | -95.22 | 4.77 | 88.27 | 0.04 | 1.59 | 939 |
| 2024-09-20 22:21:38.478 | MS1 | 121.4656736855 | 31.1446325462 | 332 | 152650 | -95.69 | 2.65 | 50.35 | 0.17 | 1.78 | 942 |
| 2024-09-20 22:21:39.917 | MS1 | 121.4656659019 | 31.1446238720 | 177 | 152650 | -93.57 | 7.74 | 96.40 | 0.07 | 1.64 | 948 |
| 2024-09-20 22:21:40.994 | MS1 | 121.4656712952 | 31.1446196003 | 660 | 152650 | -90.04 | 3.71 | 43.55 | 0.05 | 2.58 | 1577 |
| 2024-09-20 22:21:41.581 | MS1 | 121.4656630508 | 31.1446371938 | 816 | 152650 | -90.19 | 2.21 | 91.98 | 0.03 | 2.61 | 1569 |
| 2024-09-20 22:21:42.391 | MS1 | 121.4656682359 | 31.1446325017 | 332 | 152650 | -88.97 | 5.18 | 63.59 | 0.09 | 2.41 | 1579 |

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
| 3213015 | 10 | 121.4713334404 | 31.1558425426 | 316 | 0 | 9 | 7.3 | FDD | 816 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3213194 | 8 | 121.4736384435 | 31.1472129425 | 203 | 14 | 6 | 14.5 | FDD | 197 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3227219 | 7 | 121.4662886258 | 31.1471810474 | 172 | 0 | 3 | 27.1 | FDD | 450 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3229621 | 12 | 121.4679390569 | 31.1532124750 | 108 | 13 | 6 | 16.8 | FDD | 660 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3235321 | 4 | 121.4709651179 | 31.1557478182 | 242 | 1 | 9 | 11.1 | TDD | 726 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3244500 | 1 | 121.4759868423 | 31.1497892473 | 298 | 2 | 6 | 13.6 | TDD | 104 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3248558 | 2 | 121.4662359622 | 31.1456451714 | 111 | 9 | 6 | 18.5 | TDD | 270 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3250818 | 6 | 121.4708959153 | 31.1543089571 | 195 | 5 | 4 | 4.1 | TDD | 215 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3254030 | 3 | 121.4652869916 | 31.1464972431 | 215 | 14 | 7 | 23.3 | TDD | 626 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3261747 | 5 | 121.4644569957 | 31.1460341296 | 305 | 6 | 2 | 2.8 | TDD | 855 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3267274 | 9 | 121.4648429559 | 31.1465968189 | 181 | 12 | 2 | 18.0 | FDD | 332 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3274381 | 11 | 121.4735214988 | 31.1484021375 | 296 | 13 | 0 | 8.3 | FDD | 177 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3275169 | 13 | 121.4709908113 | 31.1530157610 | 272 | 3 | 2 | 14.3 | FDD | 990 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |

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
| 2024-09-20 22:21:31.078 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.102 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.228 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.228 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.927 | NREventA2 | measId:1;ServCellPCI:490;Se... |
| 2024-09-20 22:21:35.045 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.302 | NREventA5 | measId:3;ServCellPCI:490;Se... |
| 2024-09-20 22:21:35.373 | NRHandoverAttempt | SourcePCI:490;SourceNR-ARFC... |
| 2024-09-20 22:21:35.411 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.425 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.551 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.551 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244500 | 1 | 6.9247 | 13.2082 | -114.0733 | 7.6748 | 95.3757 | 0.0136 | 0.0166 |
| 2024_09_20 22:00 | 3248558 | 2 | 5.3711 | 6.4742 | -115.5642 | 18.8636 | 121.6671 | 0.0007 | 0.0118 |
| 2024_09_20 22:00 | 3254030 | 3 | 7.4154 | 15.4125 | -116.6745 | 10.2644 | 155.2828 | 0.0169 | 0.0006 |
| 2024_09_20 22:00 | 3235321 | 4 | 12.0101 | 11.8357 | -116.8345 | 8.2161 | 108.6038 | 0.0089 | 0.0002 |
| 2024_09_20 22:00 | 3261747 | 5 | 17.6275 | 11.2749 | -114.5903 | 15.6387 | 188.5232 | 0.0038 | 0.0037 |
| 2024_09_20 22:00 | 3250818 | 6 | 19.9312 | 6.3029 | -116.4474 | 5.0935 | 186.3148 | 0.0079 | 0.0114 |
| 2024_09_20 22:00 | 3227219 | 7 | 11.5935 | 8.5657 | -116.2527 | 4.1049 | 52.0926 | 0.0176 | 0.0154 |
| 2024_09_20 22:00 | 3213194 | 8 | 19.6450 | 18.8656 | -117.5176 | 3.1688 | 25.9555 | 0.0018 | 0.0132 |
| 2024_09_20 22:00 | 3267274 | 9 | 19.4203 | 10.1492 | -114.7795 | 3.1946 | 41.4252 | 0.0025 | 0.0022 |
| 2024_09_20 22:00 | 3213015 | 10 | 14.4256 | 15.5370 | -117.7256 | 4.0800 | 30.6970 | 0.0126 | 0.0034 |
| 2024_09_20 22:00 | 3274381 | 11 | 16.4508 | 9.6487 | -116.0263 | 4.7903 | 59.9088 | 0.0143 | 0.0171 |
| 2024_09_20 22:00 | 3229621 | 12 | 13.3540 | 7.9539 | -116.0610 | 4.1614 | 59.0444 | 0.0026 | 0.0167 |
| 2024_09_20 22:00 | 3275169 | 13 | 14.9319 | 17.8070 | -116.6246 | 3.7066 | 31.9357 | 0.0173 | 0.0187 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412559_EEFD2F9D | 152650 | 332 | -87.4 | 152650 | 450 | -92.4 | 152650 | 990 | -101.5 | 152650 | 197 |
| MR_1774412559_3B06AEF2 | 152650 | 332 | -87.2 | 152650 | 450 | -92.8 | 152650 | 990 | -99.7 | 152650 | 197 |
| MR_1774412559_E20874CA | 504990 | 626 | -92.0 | 504990 | 726 | -90.4 | 504990 | 855 | -97.2 | 504990 | 270 |
| MR_1774412559_C080DB6A | 504990 | 626 | -91.3 | 504990 | 726 | -89.8 | 504990 | 855 | -97.3 | 504990 | 270 |
| MR_1774412559_3AB22866 | 152650 | 332 | -87.1 | 152650 | 450 | -96.0 | 152650 | 990 | -97.9 | 152650 | 197 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 883: `d415f6ce-fca...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d415f6ce-fca8-4624-88ec-b13ac9e878de` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3258035_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[883] topology](images/train_0883.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217849_1
- `C2`: Decrease transmission power for 3258035_3
- `C3`: Press down the tilt angle  of 3217849_1 by 10 degrees
- `C4`: Adjust the azimuth of 3217849_1 by 50 degrees
- `C5`: Check test server and transmission issues
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217849_1
- `C7`: Add neighbor relationship between 3252082_2 and 3217849_1
- `C8`: Adjust the azimuth of 3258035_3 by 7 degrees
- `C9`: Lift the tilt angle  of 3217849_1 by 10 degrees
- `C10`: Increase transmission power for 3258035_3
- `C11`: Increase A3 Offset threshold for 3258035_3
- `C12`: Press down the tilt angle of 3258035_3 by 6 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258035_3 **← 정답**
- `C14`: Lift the tilt angle of 3258035_3 by 6 degrees
- `C15`: Increase transmission power for 3217849_1
- `C16`: Decrease A3 Offset threshold for 3258035_3
- `C17`: Decrease transmission power for 3217849_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Increase A3 Offset threshold for 3217849_1
- `C20`: Add neighbor relationship between 3258035_3 and 3217849_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258035_3
- `C22`: Decrease A3 Offset threshold for 3217849_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.110 | MS1 | 121.4656618047 | 31.1446324388 | 940 | 504990 | -90.68 | 12.93 | 450.02 | 0.05 | 2.86 | 1588 |
| 2024-09-20 22:21:32.567 | MS1 | 121.4656616352 | 31.1446363714 | 940 | 504990 | -85.64 | 14.90 | 549.87 | 0.12 | 2.75 | 1582 |
| 2024-09-20 22:21:33.953 | MS1 | 121.4656744439 | 31.1446362002 | 940 | 504990 | -87.78 | 13.71 | 330.64 | 0.09 | 2.40 | 1586 |
| 2024-09-20 22:21:34.844 | MS1 | 121.4656715414 | 31.1446373015 | 940 | 504990 | -88.86 | 14.36 | 67.12 | 0.61 | 2.57 | 657 |
| 2024-09-20 22:21:35.574 | MS1 | 121.4656735446 | 31.1446235507 | 940 | 504990 | -86.33 | 17.80 | 62.91 | 0.50 | 2.56 | 626 |
| 2024-09-20 22:21:36.678 | MS1 | 121.4656748991 | 31.1446192341 | 940 | 504990 | -88.86 | 15.88 | 83.87 | 0.56 | 2.99 | 648 |
| 2024-09-20 22:21:37.124 | MS1 | 121.4656738715 | 31.1446191728 | 940 | 504990 | -89.33 | 9.28 | 91.57 | 0.68 | 2.33 | 641 |
| 2024-09-20 22:21:38.798 | MS1 | 121.4656726774 | 31.1446284253 | 940 | 504990 | -92.14 | 7.29 | 91.62 | 0.51 | 2.39 | 501 |
| 2024-09-20 22:21:39.270 | MS1 | 121.4656653287 | 31.1446234004 | 940 | 504990 | -90.42 | 7.94 | 67.09 | 0.63 | 2.39 | 526 |
| 2024-09-20 22:21:40.928 | MS1 | 121.4656605585 | 31.1446300364 | 940 | 504990 | -91.17 | 8.40 | 448.14 | 0.06 | 2.38 | 1579 |
| 2024-09-20 22:21:41.675 | MS1 | 121.4656662963 | 31.1446196017 | 940 | 504990 | -93.37 | 12.47 | 437.04 | 0.14 | 2.94 | 1595 |
| 2024-09-20 22:21:42.215 | MS1 | 121.4656586489 | 31.1446367556 | 940 | 504990 | -93.47 | 9.18 | 311.12 | 0.16 | 2.75 | 1581 |

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
| 3217849 | 1 | 121.4655381989 | 31.1447007075 | 50 | 3 | 8 | 36.6 | TDD | 802 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3247452 | 4 | 121.4657383186 | 31.1533666491 | 103 | 12 | 2 | 23.1 | TDD | 675 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3252082 | 2 | 121.4663668755 | 31.1467576832 | 9 | 11 | 4 | 37.2 | TDD | 187 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3258035 | 3 | 121.4745887113 | 31.1481011929 | 238 | 3 | 6 | 41.5 | TDD | 940 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.943 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.962 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.069 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.069 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.762 | NREventA3 | measId:2;ServCellPCI:999;Se... |
| 2024-09-20 22:21:38.002 | NRHandoverAttempt | SourcePCI:999;SourceNR-ARFC... |
| 2024-09-20 22:21:38.046 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.060 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.198 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.198 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217849 | 1 | 15.1842 | 17.4417 | -117.0308 | 18.1499 | 144.0843 | 0.0158 | 0.0137 |
| 2024_09_20 22:00 | 3252082 | 2 | 19.8065 | 12.6336 | -114.5201 | 11.7013 | 144.2063 | 0.0123 | 0.0056 |
| 2024_09_20 22:00 | 3258035 | 3 | 15.3626 | 14.3798 | -117.5566 | 7.9135 | 194.0138 | 0.0129 | 0.0077 |
| 2024_09_20 22:00 | 3247452 | 4 | 8.2498 | 14.5482 | -117.2552 | 14.6093 | 155.6074 | 0.0118 | 0.0067 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414706_BCE097C9 | 504990 | 940 | -89.0 | 504990 | 802 | -92.5 | 504990 | 187 | -98.6 | 504990 | 675 |
| MR_1774414706_97CE9A83 | 504990 | 940 | -88.4 | 504990 | 802 | -92.5 | 504990 | 187 | -98.2 | 504990 | 675 |
| MR_1774414706_90438F94 | 504990 | 940 | -90.3 | 504990 | 802 | -94.5 | 504990 | 187 | -99.2 | 504990 | 675 |
| MR_1774414706_39AD0287 | 504990 | 940 | -88.6 | 504990 | 802 | -95.0 | 504990 | 187 | -98.9 | 504990 | 675 |
| MR_1774414706_4E2863B5 | 504990 | 940 | -87.3 | 504990 | 802 | -93.2 | 504990 | 187 | -98.9 | 504990 | 675 |
| MR_1774414706_FAB7843D | 504990 | 940 | -86.9 | 504990 | 802 | -94.8 | 504990 | 187 | -99.3 | 504990 | 675 |
| MR_1774414706_9B661265 | 504990 | 940 | -89.6 | 504990 | 802 | -92.2 | 504990 | 187 | -99.7 | 504990 | 675 |
| MR_1774414706_97177371 | 504990 | 940 | -90.5 | 504990 | 802 | -95.0 | 504990 | 187 | -97.1 | 504990 | 675 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 884: `bd48acc8-73a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bd48acc8-73a3-43d1-943c-4f0f35418274` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Add neighbor relationship between 3219429_1 and 3217976_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[884] topology](images/train_0884.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3219429_1 by 3 degrees
- `C2`: Add neighbor relationship between 3238168_4 and 3217976_2
- `C3`: Increase transmission power for 3217976_2
- `C4`: Decrease transmission power for 3217976_2
- `C5`: Decrease A3 Offset threshold for 3217976_2
- `C6`: Lift the tilt angle  of 3217976_2 by 5 degrees
- `C7`: Increase transmission power for 3219429_1
- `C8`: Decrease transmission power for 3219429_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219429_1
- `C10`: Increase A3 Offset threshold for 3219429_1
- `C11`: Decrease A3 Offset threshold for 3219429_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217976_2
- `C13`: Check test server and transmission issues
- `C14`: Adjust the azimuth of 3219429_1 by 50 degrees
- `C15`: Press down the tilt angle  of 3217976_2 by 5 degrees
- `C16`: Add neighbor relationship between 3219429_1 and 3217976_2 **← 정답**
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217976_2
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Lift the tilt angle of 3219429_1 by 3 degrees
- `C20`: Increase A3 Offset threshold for 3217976_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219429_1
- `C22`: Adjust the azimuth of 3217976_2 by 39 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.478 | MS1 | 121.4656691870 | 31.1446367041 | 832 | 504990 | -81.82 | 16.55 | 602.41 | 0.16 | 2.15 | 1577 |
| 2024-09-20 22:21:32.921 | MS1 | 121.4656584270 | 31.1446191589 | 832 | 504990 | -77.68 | 13.01 | 584.57 | 0.06 | 2.76 | 1570 |
| 2024-09-20 22:21:33.590 | MS1 | 121.4656616584 | 31.1446367312 | 832 | 504990 | -78.09 | 13.75 | 361.92 | 0.18 | 2.86 | 1584 |
| 2024-09-20 22:21:34.318 | MS1 | 121.4656731323 | 31.1446362390 | 832 | 504990 | -87.05 | -1.16 | 57.06 | 0.04 | 1.40 | 1589 |
| 2024-09-20 22:21:35.244 | MS1 | 121.4656656323 | 31.1446299356 | 832 | 504990 | -92.08 | -0.16 | 68.85 | 0.06 | 1.03 | 1581 |
| 2024-09-20 22:21:36.225 | MS1 | 121.4656663604 | 31.1446281401 | 832 | 504990 | -86.15 | -1.51 | 44.50 | 0.07 | 1.33 | 1590 |
| 2024-09-20 22:21:37.105 | MS1 | 121.4656734818 | 31.1446195643 | 832 | 504990 | -86.66 | -0.22 | 65.12 | 0.02 | 1.17 | 1599 |
| 2024-09-20 22:21:38.303 | MS1 | 121.4656647633 | 31.1446338086 | 832 | 504990 | -80.58 | 13.61 | 433.19 | 0.15 | 1.10 | 1582 |
| 2024-09-20 22:21:39.464 | MS1 | 121.4656712227 | 31.1446289919 | 832 | 504990 | -81.49 | 15.95 | 339.81 | 0.03 | 1.34 | 1560 |
| 2024-09-20 22:21:40.550 | MS1 | 121.4656657915 | 31.1446378747 | 832 | 504990 | -76.95 | 16.72 | 365.81 | 0.02 | 2.88 | 1592 |
| 2024-09-20 22:21:41.459 | MS1 | 121.4656662269 | 31.1446318057 | 832 | 504990 | -76.65 | 15.45 | 476.11 | 0.04 | 2.77 | 1590 |
| 2024-09-20 22:21:42.491 | MS1 | 121.4656694239 | 31.1446196684 | 832 | 504990 | -83.00 | 17.62 | 492.72 | 0.18 | 2.19 | 1589 |

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
| 3217976 | 2 | 121.4730351242 | 31.1485314755 | 199 | 2 | 1 | 37.0 | TDD | 439 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3219429 | 1 | 121.4698602615 | 31.1539840292 | 70 | 1 | 3 | 35.7 | TDD | 832 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3232198 | 3 | 121.4706829051 | 31.1513764924 | 193 | 2 | 7 | 16.0 | TDD | 446 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3238168 | 4 | 121.4655033808 | 31.1456581065 | 217 | 6 | 3 | 38.5 | TDD | 55 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.218 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.235 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.365 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.365 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.028 | NREventA3 | measId:2;ServCellPCI:56;Ser... |
| 2024-09-20 22:21:36.028 | NREventA3 | measId:2;ServCellPCI:56;Ser... |
| 2024-09-20 22:21:37.028 | NREventA3 | measId:2;ServCellPCI:56;Ser... |
| 2024-09-20 22:21:39.528 | NRRRCReestablishAttempt | PCI:56 |
| 2024-09-20 22:21:39.545 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.560 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.698 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.698 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219429 | 1 | 18.2588 | 8.6172 | -115.7448 | 7.8264 | 84.3498 | 0.0035 | 0.1628 |
| 2024_09_20 22:00 | 3217976 | 2 | 11.3225 | 5.9146 | -114.5955 | 14.7700 | 133.9791 | 0.0044 | 0.0164 |
| 2024_09_20 22:00 | 3232198 | 3 | 10.7498 | 9.9571 | -117.1946 | 11.4967 | 137.2687 | 0.0182 | 0.0039 |
| 2024_09_20 22:00 | 3238168 | 4 | 17.9330 | 12.6607 | -115.1075 | 17.8108 | 159.3353 | 0.0188 | 0.0067 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413579_E422E14B | 504990 | 439 | -85.0 | 504990 | 832 | -87.6 | 504990 | 55 | -84.3 | 504990 | 446 |
| MR_1774413579_8E53D94D | 504990 | 439 | -84.4 | 504990 | 832 | -85.8 | 504990 | 55 | -82.4 | 504990 | 446 |
| MR_1774413579_F2317C4F | 504990 | 439 | -84.5 | 504990 | 832 | -85.7 | 504990 | 55 | -81.6 | 504990 | 446 |
| MR_1774413579_0C3688BD | 504990 | 439 | -82.1 | 504990 | 832 | -85.9 | 504990 | 55 | -82.1 | 504990 | 446 |
| MR_1774413579_733249C8 | 504990 | 439 | -83.5 | 504990 | 832 | -86.4 | 504990 | 55 | -84.0 | 504990 | 446 |
| MR_1774413579_4BC600A8 | 504990 | 439 | -83.5 | 504990 | 832 | -86.1 | 504990 | 55 | -82.0 | 504990 | 446 |
| MR_1774413579_1DEACE19 | 504990 | 832 | -85.8 | 504990 | 439 | -84.7 | 504990 | 55 | -83.0 | 504990 | 446 |
| MR_1774413579_C54620CD | 504990 | 832 | -86.0 | 504990 | 439 | -82.6 | 504990 | 55 | -83.2 | 504990 | 446 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 885: `0430384d-11d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0430384d-11dc-4be4-a76c-68c29b4e42c8` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Add neighbor relationship between 3262595_4 and 3239178_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[885] topology](images/train_0885.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3262595_4 by 10 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239178_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase A3 Offset threshold for 3239178_1
- `C5`: Increase transmission power for 3262595_4
- `C6`: Increase transmission power for 3239178_1
- `C7`: Lift the tilt angle  of 3239178_1 by 4 degrees
- `C8`: Lift the tilt angle of 3262595_4 by 10 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262595_4
- `C10`: Add neighbor relationship between 3228853_2 and 3239178_1
- `C11`: Press down the tilt angle  of 3239178_1 by 4 degrees
- `C12`: Decrease transmission power for 3262595_4
- `C13`: Decrease A3 Offset threshold for 3239178_1
- `C14`: Increase A3 Offset threshold for 3262595_4
- `C15`: Add neighbor relationship between 3262595_4 and 3239178_1 **← 정답**
- `C16`: Adjust the azimuth of 3262595_4 by 50 degrees
- `C17`: Check test server and transmission issues
- `C18`: Decrease A3 Offset threshold for 3262595_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239178_1
- `C20`: Decrease transmission power for 3239178_1
- `C21`: Adjust the azimuth of 3239178_1 by 5 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262595_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.306 | MS1 | 121.4656695120 | 31.1446237248 | 671 | 504990 | -80.59 | 14.58 | 428.07 | 0.20 | 2.33 | 1600 |
| 2024-09-20 22:21:32.367 | MS1 | 121.4656689467 | 31.1446218810 | 671 | 504990 | -75.10 | 12.62 | 397.63 | 0.06 | 2.99 | 1561 |
| 2024-09-20 22:21:33.638 | MS1 | 121.4656775630 | 31.1446267326 | 671 | 504990 | -82.20 | 16.78 | 307.85 | 0.04 | 2.75 | 1590 |
| 2024-09-20 22:21:34.878 | MS1 | 121.4656603418 | 31.1446192963 | 671 | 504990 | -86.05 | -3.09 | 30.41 | 0.06 | 1.02 | 1569 |
| 2024-09-20 22:21:35.583 | MS1 | 121.4656750632 | 31.1446313049 | 671 | 504990 | -94.93 | -2.12 | 27.05 | 0.17 | 1.28 | 1570 |
| 2024-09-20 22:21:36.884 | MS1 | 121.4656629221 | 31.1446280043 | 671 | 504990 | -89.07 | -3.79 | 37.81 | 0.11 | 1.33 | 1562 |
| 2024-09-20 22:21:37.189 | MS1 | 121.4656735157 | 31.1446316706 | 671 | 504990 | -86.70 | -1.48 | 64.88 | 0.19 | 1.35 | 1595 |
| 2024-09-20 22:21:38.716 | MS1 | 121.4656616974 | 31.1446318873 | 671 | 504990 | -81.75 | 14.15 | 473.23 | 0.07 | 1.38 | 1578 |
| 2024-09-20 22:21:39.921 | MS1 | 121.4656612648 | 31.1446185756 | 671 | 504990 | -78.96 | 13.64 | 474.66 | 0.12 | 1.48 | 1573 |
| 2024-09-20 22:21:40.134 | MS1 | 121.4656713278 | 31.1446244438 | 671 | 504990 | -80.56 | 16.11 | 391.10 | 0.13 | 2.10 | 1578 |
| 2024-09-20 22:21:41.549 | MS1 | 121.4656684473 | 31.1446261825 | 671 | 504990 | -79.63 | 17.81 | 347.92 | 0.01 | 2.43 | 1587 |
| 2024-09-20 22:21:42.496 | MS1 | 121.4656644201 | 31.1446308713 | 671 | 504990 | -83.42 | 13.10 | 516.84 | 0.17 | 2.57 | 1591 |

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
| 3228853 | 2 | 121.4712269312 | 31.1532515323 | 247 | 5 | 12 | 20.0 | TDD | 939 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3239178 | 1 | 121.4740086558 | 31.1552453357 | 209 | 3 | 11 | 33.4 | TDD | 66 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3262595 | 4 | 121.4666710313 | 31.1476662244 | 90 | 6 | 1 | 27.1 | TDD | 671 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3270197 | 3 | 121.4655433410 | 31.1473764743 | 131 | 2 | 12 | 47.7 | TDD | 596 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.560 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.579 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.702 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.702 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.411 | NREventA3 | measId:2;ServCellPCI:166;Se... |
| 2024-09-20 22:21:36.411 | NREventA3 | measId:2;ServCellPCI:166;Se... |
| 2024-09-20 22:21:37.411 | NREventA3 | measId:2;ServCellPCI:166;Se... |
| 2024-09-20 22:21:39.911 | NRRRCReestablishAttempt | PCI:166 |
| 2024-09-20 22:21:39.931 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.943 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:40.070 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.070 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239178 | 1 | 16.5790 | 18.6029 | -114.8548 | 14.6926 | 95.9330 | 0.0136 | 0.0117 |
| 2024_09_20 22:00 | 3228853 | 2 | 19.0916 | 10.3816 | -116.6181 | 10.2854 | 86.0797 | 0.0069 | 0.0177 |
| 2024_09_20 22:00 | 3270197 | 3 | 9.4476 | 10.6961 | -117.8005 | 12.0196 | 82.9629 | 0.0076 | 0.0175 |
| 2024_09_20 22:00 | 3262595 | 4 | 9.9554 | 9.5844 | -115.1650 | 17.8983 | 140.5467 | 0.0123 | 0.1716 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414861_A09F322F | 504990 | 671 | -85.0 | 504990 | 66 | -78.6 | 504990 | 939 | -88.8 | 504990 | 596 |
| MR_1774414861_7B84619C | 504990 | 66 | -80.9 | 504990 | 671 | -84.6 | 504990 | 939 | -88.2 | 504990 | 596 |
| MR_1774414861_AF9FA293 | 504990 | 66 | -82.2 | 504990 | 671 | -84.1 | 504990 | 939 | -88.8 | 504990 | 596 |
| MR_1774414861_FF0B7E09 | 504990 | 671 | -87.3 | 504990 | 66 | -78.6 | 504990 | 939 | -87.1 | 504990 | 596 |
| MR_1774414861_7F5FA974 | 504990 | 66 | -81.1 | 504990 | 671 | -87.8 | 504990 | 939 | -87.7 | 504990 | 596 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 886: `70eaac8a-b06...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `70eaac8a-b06e-4c91-8a61-45bf1c35d15b` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Add neighbor relationship between 3278153_1 and 3277570_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[886] topology](images/train_0886.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Increase A3 Offset threshold for 3277570_2
- `C3`: Decrease A3 Offset threshold for 3278153_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277570_2
- `C5`: Increase transmission power for 3278153_1
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Adjust the azimuth of 3278153_1 by 50 degrees
- `C8`: Adjust the azimuth of 3277570_2 by 20 degrees
- `C9`: Press down the tilt angle  of 3277570_2 by 2 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277570_2
- `C11`: Decrease A3 Offset threshold for 3277570_2
- `C12`: Press down the tilt angle of 3278153_1 by 10 degrees
- `C13`: Lift the tilt angle of 3278153_1 by 10 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278153_1
- `C15`: Lift the tilt angle  of 3277570_2 by 2 degrees
- `C16`: Add neighbor relationship between 3270246_3 and 3277570_2
- `C17`: Increase transmission power for 3277570_2
- `C18`: Decrease transmission power for 3278153_1
- `C19`: Decrease transmission power for 3277570_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278153_1
- `C21`: Increase A3 Offset threshold for 3278153_1
- `C22`: Add neighbor relationship between 3278153_1 and 3277570_2 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.793 | MS1 | 121.4656737495 | 31.1446218422 | 704 | 504990 | -81.58 | 14.09 | 334.39 | 0.18 | 2.76 | 1590 |
| 2024-09-20 22:21:32.242 | MS1 | 121.4656605936 | 31.1446321354 | 704 | 504990 | -82.22 | 16.60 | 528.37 | 0.15 | 2.60 | 1593 |
| 2024-09-20 22:21:33.110 | MS1 | 121.4656736385 | 31.1446261212 | 704 | 504990 | -84.73 | 15.02 | 431.28 | 0.15 | 2.17 | 1594 |
| 2024-09-20 22:21:34.346 | MS1 | 121.4656737736 | 31.1446365717 | 704 | 504990 | -89.08 | -3.42 | 60.76 | 0.16 | 1.48 | 1584 |
| 2024-09-20 22:21:35.595 | MS1 | 121.4656711815 | 31.1446302640 | 704 | 504990 | -90.87 | -0.38 | 51.41 | 0.08 | 1.27 | 1561 |
| 2024-09-20 22:21:36.884 | MS1 | 121.4656624870 | 31.1446361583 | 704 | 504990 | -91.28 | -3.15 | 39.82 | 0.01 | 1.13 | 1565 |
| 2024-09-20 22:21:37.861 | MS1 | 121.4656596654 | 31.1446283555 | 704 | 504990 | -85.64 | -0.90 | 49.71 | 0.14 | 1.12 | 1566 |
| 2024-09-20 22:21:38.467 | MS1 | 121.4656631967 | 31.1446292857 | 704 | 504990 | -78.49 | 13.65 | 367.16 | 0.06 | 1.28 | 1561 |
| 2024-09-20 22:21:39.766 | MS1 | 121.4656609631 | 31.1446281945 | 704 | 504990 | -84.18 | 16.53 | 315.37 | 0.07 | 1.45 | 1574 |
| 2024-09-20 22:21:40.641 | MS1 | 121.4656644197 | 31.1446224538 | 704 | 504990 | -78.88 | 16.95 | 499.61 | 0.17 | 2.42 | 1578 |
| 2024-09-20 22:21:41.473 | MS1 | 121.4656612732 | 31.1446284639 | 704 | 504990 | -81.51 | 13.94 | 373.63 | 0.10 | 2.08 | 1560 |
| 2024-09-20 22:21:42.904 | MS1 | 121.4656602791 | 31.1446321414 | 704 | 504990 | -83.98 | 13.89 | 388.16 | 0.00 | 2.13 | 1569 |

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
| 3234615 | 4 | 121.4720576951 | 31.1536603373 | 162 | 10 | 4 | 44.2 | TDD | 574 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3270246 | 3 | 121.4687920408 | 31.1522729758 | 77 | 9 | 6 | 18.6 | TDD | 206 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3277570 | 2 | 121.4746768042 | 31.1550511033 | 237 | 0 | 3 | 49.4 | TDD | 995 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3278153 | 1 | 121.4698810444 | 31.1558441674 | 295 | 14 | 7 | 37.6 | TDD | 704 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.363 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.381 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.519 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.519 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.231 | NREventA3 | measId:2;ServCellPCI:61;Ser... |
| 2024-09-20 22:21:36.231 | NREventA3 | measId:2;ServCellPCI:61;Ser... |
| 2024-09-20 22:21:37.231 | NREventA3 | measId:2;ServCellPCI:61;Ser... |
| 2024-09-20 22:21:39.731 | NRRRCReestablishAttempt | PCI:61 |
| 2024-09-20 22:21:39.749 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.762 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.908 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.908 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278153 | 1 | 10.9856 | 14.8944 | -116.7760 | 5.6157 | 131.8494 | 0.0136 | 0.1787 |
| 2024_09_20 22:00 | 3277570 | 2 | 6.9719 | 11.5253 | -116.1213 | 12.7525 | 127.8863 | 0.0028 | 0.0085 |
| 2024_09_20 22:00 | 3270246 | 3 | 8.1293 | 16.2576 | -115.1979 | 14.8696 | 182.9256 | 0.0129 | 0.0141 |
| 2024_09_20 22:00 | 3234615 | 4 | 14.3076 | 13.3911 | -117.3264 | 5.0869 | 91.9138 | 0.0083 | 0.0036 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413663_EEAFDE59 | 504990 | 704 | -90.1 | 504990 | 995 | -83.6 | 504990 | 206 | -89.1 | 504990 | 574 |
| MR_1774413663_EA4791AA | 504990 | 995 | -85.1 | 504990 | 704 | -90.7 | 504990 | 206 | -88.7 | 504990 | 574 |
| MR_1774413663_1C2B9258 | 504990 | 995 | -85.1 | 504990 | 704 | -89.0 | 504990 | 206 | -87.1 | 504990 | 574 |
| MR_1774413663_5EE6F23E | 504990 | 704 | -89.9 | 504990 | 995 | -84.0 | 504990 | 206 | -89.5 | 504990 | 574 |
| MR_1774413663_F65FCB9F | 504990 | 704 | -90.0 | 504990 | 995 | -84.9 | 504990 | 206 | -89.7 | 504990 | 574 |
| MR_1774413663_5C9BFEEC | 504990 | 704 | -90.2 | 504990 | 995 | -84.7 | 504990 | 206 | -87.1 | 504990 | 574 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 887: `a6b1b747-f0d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a6b1b747-f0d9-4293-8f6a-bf8b8674ccc0` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Add neighbor relationship between 3260085_1 and 3250034_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[887] topology](images/train_0887.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3250034_4
- `C2`: Decrease transmission power for 3260085_1
- `C3`: Decrease A3 Offset threshold for 3250034_4
- `C4`: Increase A3 Offset threshold for 3260085_1
- `C5`: Add neighbor relationship between 3228251_3 and 3250034_4
- `C6`: Increase transmission power for 3260085_1
- `C7`: Add neighbor relationship between 3260085_1 and 3250034_4 **← 정답**
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250034_4
- `C9`: Increase transmission power for 3250034_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250034_4
- `C11`: Press down the tilt angle  of 3250034_4 by 1 degrees
- `C12`: Lift the tilt angle  of 3250034_4 by 1 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease transmission power for 3250034_4
- `C15`: Adjust the azimuth of 3260085_1 by 50 degrees
- `C16`: Decrease A3 Offset threshold for 3260085_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260085_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260085_1
- `C19`: Lift the tilt angle of 3260085_1 by 9 degrees
- `C20`: Press down the tilt angle of 3260085_1 by 9 degrees
- `C21`: Adjust the azimuth of 3250034_4 by 8 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.771 | MS1 | 121.4656673523 | 31.1446358348 | 937 | 504990 | -82.28 | 15.90 | 580.15 | 0.09 | 2.14 | 1564 |
| 2024-09-20 22:21:32.795 | MS1 | 121.4656659097 | 31.1446299539 | 937 | 504990 | -82.79 | 14.00 | 311.68 | 0.11 | 2.93 | 1592 |
| 2024-09-20 22:21:33.877 | MS1 | 121.4656634460 | 31.1446281988 | 937 | 504990 | -83.50 | 14.39 | 361.05 | 0.15 | 2.71 | 1586 |
| 2024-09-20 22:21:34.386 | MS1 | 121.4656767448 | 31.1446343419 | 937 | 504990 | -92.91 | -3.96 | 43.34 | 0.05 | 1.24 | 1583 |
| 2024-09-20 22:21:35.839 | MS1 | 121.4656750832 | 31.1446210774 | 937 | 504990 | -92.31 | -1.17 | 64.35 | 0.12 | 1.36 | 1566 |
| 2024-09-20 22:21:36.194 | MS1 | 121.4656683218 | 31.1446295219 | 937 | 504990 | -89.81 | -2.94 | 54.39 | 0.08 | 1.44 | 1590 |
| 2024-09-20 22:21:37.206 | MS1 | 121.4656650849 | 31.1446357943 | 937 | 504990 | -91.33 | -0.00 | 51.78 | 0.19 | 1.31 | 1563 |
| 2024-09-20 22:21:38.281 | MS1 | 121.4656684645 | 31.1446319045 | 937 | 504990 | -80.22 | 16.05 | 336.80 | 0.06 | 1.00 | 1587 |
| 2024-09-20 22:21:39.699 | MS1 | 121.4656758961 | 31.1446241840 | 937 | 504990 | -84.59 | 17.87 | 562.88 | 0.10 | 1.50 | 1599 |
| 2024-09-20 22:21:40.284 | MS1 | 121.4656620636 | 31.1446196971 | 937 | 504990 | -82.87 | 12.29 | 344.33 | 0.10 | 2.94 | 1579 |
| 2024-09-20 22:21:41.897 | MS1 | 121.4656717581 | 31.1446213840 | 937 | 504990 | -84.02 | 15.58 | 366.62 | 0.07 | 2.49 | 1593 |
| 2024-09-20 22:21:42.133 | MS1 | 121.4656746479 | 31.1446291787 | 937 | 504990 | -83.27 | 16.59 | 371.84 | 0.10 | 2.13 | 1600 |

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
| 3228251 | 3 | 121.4683417345 | 31.1509720385 | 233 | 15 | 9 | 39.3 | TDD | 107 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3229594 | 2 | 121.4706301461 | 31.1510791155 | 188 | 8 | 10 | 48.1 | TDD | 658 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3250034 | 4 | 121.4640193572 | 31.1556880299 | 165 | 0 | 0 | 15.4 | TDD | 761 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3260085 | 1 | 121.4713004747 | 31.1456402121 | 180 | 6 | 0 | 26.6 | TDD | 937 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.019 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.037 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.139 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.139 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.835 | NREventA3 | measId:2;ServCellPCI:229;Se... |
| 2024-09-20 22:21:35.835 | NREventA3 | measId:2;ServCellPCI:229;Se... |
| 2024-09-20 22:21:36.835 | NREventA3 | measId:2;ServCellPCI:229;Se... |
| 2024-09-20 22:21:39.335 | NRRRCReestablishAttempt | PCI:229 |
| 2024-09-20 22:21:39.345 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.357 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.487 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.487 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260085 | 1 | 8.6236 | 8.3154 | -114.1990 | 9.9030 | 87.2344 | 0.0031 | 0.1162 |
| 2024_09_20 22:00 | 3229594 | 2 | 18.7927 | 5.0093 | -114.0144 | 6.3349 | 129.3838 | 0.0035 | 0.0086 |
| 2024_09_20 22:00 | 3228251 | 3 | 11.9178 | 9.1008 | -117.8646 | 19.9510 | 165.8970 | 0.0198 | 0.0137 |
| 2024_09_20 22:00 | 3250034 | 4 | 5.4134 | 10.4225 | -116.2843 | 19.3975 | 109.5143 | 0.0028 | 0.0010 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412618_3A80FD5C | 504990 | 761 | -88.8 | 504990 | 937 | -93.4 | 504990 | 107 | -95.0 | 504990 | 658 |
| MR_1774412618_46C18B33 | 504990 | 937 | -94.4 | 504990 | 761 | -87.1 | 504990 | 107 | -94.0 | 504990 | 658 |
| MR_1774412618_E45292EF | 504990 | 937 | -94.3 | 504990 | 761 | -89.6 | 504990 | 107 | -91.9 | 504990 | 658 |
| MR_1774412618_737FF186 | 504990 | 761 | -87.4 | 504990 | 937 | -91.7 | 504990 | 107 | -94.5 | 504990 | 658 |
| MR_1774412618_5A5FCF04 | 504990 | 761 | -86.5 | 504990 | 937 | -92.2 | 504990 | 107 | -92.2 | 504990 | 658 |
| MR_1774412618_111A9CB5 | 504990 | 761 | -87.1 | 504990 | 937 | -92.9 | 504990 | 107 | -93.6 | 504990 | 658 |
| MR_1774412618_C2BCAB11 | 504990 | 937 | -92.9 | 504990 | 761 | -87.0 | 504990 | 107 | -92.0 | 504990 | 658 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 888: `d7ee6d02-91f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d7ee6d02-91f5-4df9-be75-3559aad0a8c4` |
| Tag | **multiple-answer** |
| 정답 | **C5|C11** |
| C5 의미 | Adjust the azimuth of 3273674_2 by 50 degrees |
| C11 의미 | Increase transmission power for 3273674_2 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[888] topology](images/train_0888.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273674_2
- `C2`: Decrease transmission power for 3271696_4
- `C3`: Add neighbor relationship between 3273674_2 and 3271696_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271696_4
- `C5`: Adjust the azimuth of 3273674_2 by 50 degrees **← 정답**
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271696_4
- `C7`: Lift the tilt angle of 3273674_2 by 10 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase A3 Offset threshold for 3273674_2
- `C10`: Add neighbor relationship between 3254302_3 and 3271696_4
- `C11`: Increase transmission power for 3273674_2 **← 정답**
- `C12`: Increase A3 Offset threshold for 3271696_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273674_2
- `C14`: Check test server and transmission issues
- `C15`: Decrease A3 Offset threshold for 3273674_2
- `C16`: Press down the tilt angle  of 3271696_4 by 3 degrees
- `C17`: Decrease A3 Offset threshold for 3271696_4
- `C18`: Lift the tilt angle  of 3271696_4 by 3 degrees
- `C19`: Decrease transmission power for 3273674_2
- `C20`: Increase transmission power for 3271696_4
- `C21`: Press down the tilt angle of 3273674_2 by 10 degrees
- `C22`: Adjust the azimuth of 3271696_4 by 22 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.976 | MS1 | 121.4656720469 | 31.1446257331 | 711 | 504990 | -92.95 | 16.95 | 572.69 | 0.09 | 2.72 | 1598 |
| 2024-09-20 22:21:32.236 | MS1 | 121.4656760639 | 31.1446212694 | 711 | 504990 | -92.74 | 12.29 | 402.52 | 0.07 | 2.68 | 1564 |
| 2024-09-20 22:21:33.274 | MS1 | 121.4656636177 | 31.1446243602 | 711 | 504990 | -93.22 | 13.55 | 582.50 | 0.17 | 2.07 | 1569 |
| 2024-09-20 22:21:34.531 | MS1 | 121.4656624373 | 31.1446256521 | 711 | 504990 | -107.34 | -1.22 | 58.37 | 0.13 | 1.16 | 1585 |
| 2024-09-20 22:21:35.639 | MS1 | 121.4656754953 | 31.1446284622 | 711 | 504990 | -100.97 | 0.33 | 80.47 | 0.14 | 1.37 | 1579 |
| 2024-09-20 22:21:36.459 | MS1 | 121.4656644922 | 31.1446237988 | 711 | 504990 | -100.73 | -1.69 | 59.07 | 0.10 | 1.40 | 1573 |
| 2024-09-20 22:21:37.989 | MS1 | 121.4656709097 | 31.1446367929 | 711 | 504990 | -105.52 | -1.56 | 56.47 | 0.15 | 1.01 | 1587 |
| 2024-09-20 22:21:38.815 | MS1 | 121.4656742099 | 31.1446190712 | 711 | 504990 | -105.25 | 1.66 | 75.22 | 0.04 | 1.02 | 1560 |
| 2024-09-20 22:21:39.251 | MS1 | 121.4656606030 | 31.1446209983 | 711 | 504990 | -108.99 | 1.72 | 17.41 | 0.17 | 1.05 | 1582 |
| 2024-09-20 22:21:40.706 | MS1 | 121.4656753618 | 31.1446218517 | 711 | 504990 | -94.97 | 12.15 | 358.71 | 0.09 | 2.19 | 1588 |
| 2024-09-20 22:21:41.741 | MS1 | 121.4656732867 | 31.1446254127 | 711 | 504990 | -91.02 | 13.71 | 352.49 | 0.05 | 2.19 | 1564 |
| 2024-09-20 22:21:42.246 | MS1 | 121.4656641312 | 31.1446231254 | 711 | 504990 | -92.14 | 13.72 | 307.94 | 0.00 | 2.92 | 1595 |

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
| 3211615 | 1 | 121.4698033311 | 31.1442136836 | 82 | 12 | 2 | 45.6 | TDD | 881 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3254302 | 3 | 121.4698482537 | 31.1504173578 | 312 | 5 | 5 | 17.4 | TDD | 615 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3271696 | 4 | 121.4743935961 | 31.1516848866 | 249 | 1 | 11 | 49.0 | TDD | 975 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3273674 | 2 | 121.4649758823 | 31.1464624944 | 89 | 13 | 4 | 42.3 | TDD | 711 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.411 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.428 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.547 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.547 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.796 | NREventA2 | measId:1;ServCellPCI:225;Se... |
| 2024-09-20 22:21:34.923 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211615 | 1 | 10.3358 | 12.4558 | -115.5470 | 19.4701 | 110.2320 | 0.0188 | 0.0041 |
| 2024_09_20 22:00 | 3273674 | 2 | 14.1403 | 10.7131 | -117.4774 | 18.3207 | 194.3380 | 0.1358 | 0.0143 |
| 2024_09_20 22:00 | 3254302 | 3 | 7.4737 | 6.9095 | -114.5551 | 17.1518 | 159.3439 | 0.0150 | 0.0058 |
| 2024_09_20 22:00 | 3271696 | 4 | 10.9122 | 13.8159 | -114.5231 | 7.0680 | 87.9011 | 0.0117 | 0.0013 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416040_B21D63DA | 504990 | 711 | -108.2 | 504990 | 975 | -113.6 | 504990 | 615 | -120.6 | 504990 | 881 |
| MR_1774416040_9686DF89 | 504990 | 711 | -107.6 | 504990 | 975 | -112.4 | 504990 | 615 | -120.5 | 504990 | 881 |
| MR_1774416040_553B8EF6 | 504990 | 711 | -108.5 | 504990 | 975 | -111.4 | 504990 | 615 | -117.5 | 504990 | 881 |
| MR_1774416040_E83A094A | 504990 | 711 | -105.8 | 504990 | 975 | -112.4 | 504990 | 615 | -116.9 | 504990 | 881 |
| MR_1774416040_F659D050 | 504990 | 711 | -107.4 | 504990 | 975 | -114.8 | 504990 | 615 | -120.3 | 504990 | 881 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 889: `894b732f-70a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `894b732f-70ab-4d88-9745-92c8d1e357e0` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3259333_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[889] topology](images/train_0889.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3259333_4 by 5 degrees
- `C2`: Decrease transmission power for 3259333_4
- `C3`: Adjust the azimuth of 3259333_4 by 7 degrees
- `C4`: Press down the tilt angle  of 3276702_1 by 7 degrees
- `C5`: Adjust the azimuth of 3276702_1 by 50 degrees
- `C6`: Increase transmission power for 3259333_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259333_4
- `C8`: Decrease A3 Offset threshold for 3276702_1
- `C9`: Lift the tilt angle of 3259333_4 by 5 degrees
- `C10`: Add neighbor relationship between 3267145_2 and 3276702_1
- `C11`: Add neighbor relationship between 3259333_4 and 3276702_1
- `C12`: Lift the tilt angle  of 3276702_1 by 7 degrees
- `C13`: Increase transmission power for 3276702_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259333_4 **← 정답**
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276702_1
- `C16`: Increase A3 Offset threshold for 3276702_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276702_1
- `C18`: Decrease transmission power for 3276702_1
- `C19`: Check test server and transmission issues
- `C20`: Increase A3 Offset threshold for 3259333_4
- `C21`: Decrease A3 Offset threshold for 3259333_4
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.636 | MS1 | 121.4656613823 | 31.1446296177 | 693 | 504990 | -85.33 | 17.64 | 363.09 | 0.17 | 2.42 | 1571 |
| 2024-09-20 22:21:32.307 | MS1 | 121.4656683451 | 31.1446340573 | 693 | 504990 | -91.78 | 16.58 | 521.40 | 0.06 | 2.19 | 1574 |
| 2024-09-20 22:21:33.239 | MS1 | 121.4656591239 | 31.1446319888 | 693 | 504990 | -86.36 | 16.23 | 423.70 | 0.03 | 2.57 | 1561 |
| 2024-09-20 22:21:34.262 | MS1 | 121.4656600297 | 31.1446351071 | 693 | 504990 | -85.46 | 17.97 | 69.47 | 0.68 | 2.96 | 522 |
| 2024-09-20 22:21:35.871 | MS1 | 121.4656744378 | 31.1446248680 | 693 | 504990 | -87.86 | 17.07 | 68.50 | 0.62 | 2.63 | 622 |
| 2024-09-20 22:21:36.403 | MS1 | 121.4656776791 | 31.1446209307 | 693 | 504990 | -91.43 | 16.38 | 78.61 | 0.60 | 2.84 | 638 |
| 2024-09-20 22:21:37.512 | MS1 | 121.4656735826 | 31.1446315741 | 693 | 504990 | -89.94 | 10.79 | 64.25 | 0.51 | 2.25 | 559 |
| 2024-09-20 22:21:38.219 | MS1 | 121.4656661014 | 31.1446338749 | 693 | 504990 | -91.72 | 7.89 | 104.08 | 0.50 | 2.79 | 648 |
| 2024-09-20 22:21:39.927 | MS1 | 121.4656629286 | 31.1446376258 | 693 | 504990 | -92.11 | 8.93 | 60.88 | 0.57 | 2.87 | 616 |
| 2024-09-20 22:21:40.667 | MS1 | 121.4656690266 | 31.1446281403 | 693 | 504990 | -93.67 | 12.31 | 400.64 | 0.02 | 2.37 | 1589 |
| 2024-09-20 22:21:41.904 | MS1 | 121.4656769871 | 31.1446222888 | 693 | 504990 | -89.23 | 11.19 | 580.23 | 0.09 | 2.54 | 1585 |
| 2024-09-20 22:21:42.357 | MS1 | 121.4656669996 | 31.1446359043 | 693 | 504990 | -91.45 | 8.01 | 485.59 | 0.01 | 2.08 | 1576 |

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
| 3259333 | 4 | 121.4750611097 | 31.1445339261 | 278 | 3 | 0 | 26.6 | TDD | 693 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3267145 | 2 | 121.4660158201 | 31.1459431821 | 272 | 6 | 10 | 40.8 | TDD | 834 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3267150 | 3 | 121.4693132586 | 31.1482726386 | 308 | 5 | 9 | 16.0 | TDD | 94 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3276702 | 1 | 121.4698072293 | 31.1477403950 | 75 | 3 | 8 | 32.7 | TDD | 650 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.731 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.752 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.892 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.892 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.630 | NREventA3 | measId:2;ServCellPCI:295;Se... |
| 2024-09-20 22:21:37.870 | NRHandoverAttempt | SourcePCI:295;SourceNR-ARFC... |
| 2024-09-20 22:21:37.920 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.933 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.077 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.077 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276702 | 1 | 15.3352 | 7.4500 | -115.0161 | 13.3623 | 176.3489 | 0.0058 | 0.0026 |
| 2024_09_20 22:00 | 3267145 | 2 | 18.1391 | 13.7429 | -115.6693 | 16.4479 | 101.4024 | 0.0023 | 0.0197 |
| 2024_09_20 22:00 | 3267150 | 3 | 16.0544 | 18.8517 | -115.6170 | 11.5182 | 110.0993 | 0.0191 | 0.0019 |
| 2024_09_20 22:00 | 3259333 | 4 | 8.2344 | 12.9243 | -114.7554 | 16.3532 | 101.6812 | 0.0010 | 0.0141 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415156_938E37B6 | 504990 | 693 | -87.4 | 504990 | 650 | -88.4 | 504990 | 834 | -95.0 | 504990 | 94 |
| MR_1774415156_C3B2510A | 504990 | 693 | -86.4 | 504990 | 650 | -88.9 | 504990 | 834 | -96.5 | 504990 | 94 |
| MR_1774415156_A0884F6D | 504990 | 693 | -87.1 | 504990 | 650 | -86.6 | 504990 | 834 | -97.6 | 504990 | 94 |
| MR_1774415156_7B0BE5AB | 504990 | 693 | -84.1 | 504990 | 650 | -87.0 | 504990 | 834 | -98.7 | 504990 | 94 |
| MR_1774415156_ED0B4B98 | 504990 | 693 | -84.5 | 504990 | 650 | -87.7 | 504990 | 834 | -95.0 | 504990 | 94 |
| MR_1774415156_3C73681A | 504990 | 693 | -85.1 | 504990 | 650 | -89.7 | 504990 | 834 | -96.7 | 504990 | 94 |
| MR_1774415156_53BB7510 | 504990 | 693 | -87.1 | 504990 | 650 | -88.2 | 504990 | 834 | -95.2 | 504990 | 94 |
| MR_1774415156_B0D38DD9 | 504990 | 693 | -87.1 | 504990 | 650 | -86.2 | 504990 | 834 | -95.8 | 504990 | 94 |

> *... 2개 열 생략 (전체 14열)*

---
