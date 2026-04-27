# Track A 문제 분석 — train[650]~train[659]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[650] ~ train[659] (10개)

## 목차

1. [문제 650: `4493a284-8bf...`](#650) — multiple-answer, 정답: C8|C14|C17|C22
2. [문제 651: `dc9a0582-391...`](#651) — single-answer, 정답: C4
3. [문제 652: `0e747f73-510...`](#652) — multiple-answer, 정답: C14|C19
4. [문제 653: `c4415023-baa...`](#653) — single-answer, 정답: C6
5. [문제 654: `0145f9c4-6c8...`](#654) — single-answer, 정답: C4
6. [문제 655: `b750b868-591...`](#655) — single-answer, 정답: C10
7. [문제 656: `963ff3e1-571...`](#656) — single-answer, 정답: C17
8. [문제 657: `ea4c0706-cad...`](#657) — single-answer, 정답: C12
9. [문제 658: `2f62bb6a-b3a...`](#658) — multiple-answer, 정답: C2|C4|C18|C20
10. [문제 659: `78d4b233-8f0...`](#659) — multiple-answer, 정답: C2|C10|C11|C15

---

### 문제 650: `4493a284-8bf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4493a284-8bfc-4e1a-8c64-d5763f3f48dc` |
| Tag | **multiple-answer** |
| 정답 | **C8|C14|C17|C22** |
| C8 의미 | Decrease transmission power for 3279209_1 |
| C14 의미 | Increase A3 Offset threshold for 3254025_2 |
| C17 의미 | Press down the tilt angle  of 3279209_1 by 4 degrees |
| C22 의미 | Increase A3 Offset threshold for 3279209_1 |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[650] topology](images/train_0650.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3254025_2 by 3 degrees
- `C2`: Decrease A3 Offset threshold for 3279209_1
- `C3`: Lift the tilt angle  of 3279209_1 by 4 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Adjust the azimuth of 3279209_1 by 20 degrees
- `C6`: Decrease transmission power for 3254025_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279209_1
- `C8`: Decrease transmission power for 3279209_1 **← 정답**
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279209_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254025_2
- `C11`: Decrease A3 Offset threshold for 3254025_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254025_2
- `C13`: Increase transmission power for 3279209_1
- `C14`: Increase A3 Offset threshold for 3254025_2 **← 정답**
- `C15`: Add neighbor relationship between 3254025_2 and 3279209_1
- `C16`: Lift the tilt angle of 3254025_2 by 3 degrees
- `C17`: Press down the tilt angle  of 3279209_1 by 4 degrees **← 정답**
- `C18`: Increase transmission power for 3254025_2
- `C19`: Add neighbor relationship between 3254182_4 and 3279209_1
- `C20`: Adjust the azimuth of 3254025_2 by 26 degrees
- `C21`: Check test server and transmission issues
- `C22`: Increase A3 Offset threshold for 3279209_1 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.198 | MS1 | 121.4656722574 | 31.1446202189 | 336 | 504990 | -82.87 | 13.96 | 520.50 | 0.08 | 2.42 | 1560 |
| 2024-09-20 22:21:32.939 | MS1 | 121.4656750603 | 31.1446193419 | 336 | 504990 | -83.73 | 16.38 | 450.79 | 0.02 | 2.38 | 1598 |
| 2024-09-20 22:21:33.185 | MS1 | 121.4656582614 | 31.1446379719 | 336 | 504990 | -77.10 | 12.93 | 444.05 | 0.01 | 2.92 | 1596 |
| 2024-09-20 22:21:34.780 | MS1 | 121.4656677372 | 31.1446266799 | 690 | 504990 | -83.68 | 2.75 | 64.51 | 0.19 | 1.44 | 1561 |
| 2024-09-20 22:21:35.135 | MS1 | 121.4656683460 | 31.1446369912 | 690 | 504990 | -83.80 | 4.73 | 44.85 | 0.04 | 1.05 | 1563 |
| 2024-09-20 22:21:36.503 | MS1 | 121.4656766094 | 31.1446314163 | 336 | 504990 | -85.62 | 4.58 | 41.82 | 0.07 | 1.39 | 1569 |
| 2024-09-20 22:21:37.115 | MS1 | 121.4656686388 | 31.1446243531 | 336 | 504990 | -83.16 | 3.15 | 79.54 | 0.04 | 1.35 | 1593 |
| 2024-09-20 22:21:38.829 | MS1 | 121.4656751635 | 31.1446335573 | 690 | 504990 | -84.75 | 1.40 | 57.35 | 0.16 | 1.37 | 1593 |
| 2024-09-20 22:21:39.543 | MS1 | 121.4656689021 | 31.1446290974 | 690 | 504990 | -86.95 | 4.58 | 45.39 | 0.07 | 1.01 | 1573 |
| 2024-09-20 22:21:40.667 | MS1 | 121.4656602668 | 31.1446273175 | 690 | 504990 | -76.80 | 13.67 | 593.72 | 0.13 | 2.93 | 1575 |
| 2024-09-20 22:21:41.110 | MS1 | 121.4656646481 | 31.1446198138 | 690 | 504990 | -80.52 | 12.19 | 332.25 | 0.01 | 2.76 | 1562 |
| 2024-09-20 22:21:42.436 | MS1 | 121.4656679139 | 31.1446224291 | 690 | 504990 | -76.43 | 12.45 | 403.17 | 0.19 | 2.97 | 1584 |

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
| 3214024 | 3 | 121.4746770272 | 31.1497110247 | 181 | 0 | 9 | 31.1 | TDD | 690 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3229532 | 5 | 121.4728829946 | 31.1455164720 | 157 | 13 | 8 | 22.4 | TDD | 798 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3254025 | 2 | 121.4670288806 | 31.1546158339 | 213 | 2 | 6 | 20.0 | TDD | 336 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3254182 | 4 | 121.4649752700 | 31.1443193984 | 94 | 7 | 2 | 46.5 | TDD | 892 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3279209 | 1 | 121.4680329483 | 31.1504965081 | 219 | 1 | 6 | 31.3 | TDD | 458 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.136 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.151 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.263 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.263 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.017 | NREventA3 | measId:2;ServCellPCI:950;Se... |
| 2024-09-20 22:21:34.257 | NRHandoverAttempt | SourcePCI:950;SourceNR-ARFC... |
| 2024-09-20 22:21:34.302 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.312 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:34.414 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.414 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.017 | NREventA3 | measId:2;ServCellPCI:538;Se... |
| 2024-09-20 22:21:36.257 | NRHandoverAttempt | SourcePCI:538;SourceNR-ARFC... |
| 2024-09-20 22:21:36.301 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.311 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:36.428 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.428 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.017 | NREventA3 | measId:2;ServCellPCI:950;Se... |
| 2024-09-20 22:21:38.257 | NRHandoverAttempt | SourcePCI:950;SourceNR-ARFC... |
| 2024-09-20 22:21:38.299 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.310 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.419 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.419 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279209 | 1 | 7.7232 | 9.7250 | -115.4399 | 15.4291 | 150.0520 | 0.0063 | 0.0082 |
| 2024_09_20 22:00 | 3254025 | 2 | 18.5830 | 19.9967 | -114.5199 | 5.6619 | 194.8448 | 0.0001 | 0.0189 |
| 2024_09_20 22:00 | 3214024 | 3 | 8.7902 | 5.1495 | -117.3741 | 13.8262 | 148.2481 | 0.0068 | 0.0155 |
| 2024_09_20 22:00 | 3254182 | 4 | 11.6346 | 19.4149 | -114.1002 | 11.0994 | 128.7236 | 0.0146 | 0.0075 |
| 2024_09_20 22:00 | 3229532 | 5 | 6.3371 | 7.6960 | -117.0669 | 12.6572 | 155.6347 | 0.0086 | 0.0093 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416911_8C9A17DA | 504990 | 336 | -84.3 | 504990 | 690 | -83.8 | 504990 | 458 | -87.1 | 504990 | 892 |
| MR_1774416911_21A8B7FA | 504990 | 336 | -85.3 | 504990 | 690 | -82.5 | 504990 | 458 | -85.9 | 504990 | 892 |
| MR_1774416911_A894C160 | 504990 | 336 | -84.8 | 504990 | 690 | -82.9 | 504990 | 458 | -88.1 | 504990 | 892 |
| MR_1774416911_EDF5DC7A | 504990 | 690 | -82.6 | 504990 | 336 | -84.5 | 504990 | 458 | -87.0 | 504990 | 892 |
| MR_1774416911_918F5943 | 504990 | 336 | -83.0 | 504990 | 690 | -83.9 | 504990 | 458 | -89.6 | 504990 | 892 |
| MR_1774416911_50744F08 | 504990 | 336 | -82.3 | 504990 | 690 | -84.0 | 504990 | 458 | -87.6 | 504990 | 892 |
| MR_1774416911_F7D0C40A | 504990 | 336 | -84.7 | 504990 | 690 | -82.5 | 504990 | 458 | -88.3 | 504990 | 892 |
| MR_1774416911_8C00B2A4 | 504990 | 690 | -84.6 | 504990 | 336 | -84.2 | 504990 | 458 | -88.1 | 504990 | 892 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 651: `dc9a0582-391...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dc9a0582-391c-412b-9395-3ea0e4bb1520` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Decrease A3 Offset threshold for 3269905_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[651] topology](images/train_0651.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3269905_1 by 10 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269905_1
- `C3`: Check test server and transmission issues
- `C4`: Decrease A3 Offset threshold for 3269905_1 **← 정답**
- `C5`: Increase A3 Offset threshold for 3269905_1
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease transmission power for 3269905_1
- `C8`: Press down the tilt angle of 3269905_1 by 10 degrees
- `C9`: Adjust the azimuth of 3258292_4 by 40 degrees
- `C10`: Press down the tilt angle  of 3258292_4 by 10 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258292_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258292_4
- `C13`: Decrease A3 Offset threshold for 3258292_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269905_1
- `C15`: Add neighbor relationship between 3269905_1 and 3258292_4
- `C16`: Add neighbor relationship between 3265899_2 and 3258292_4
- `C17`: Decrease transmission power for 3258292_4
- `C18`: Increase transmission power for 3269905_1
- `C19`: Lift the tilt angle  of 3258292_4 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3258292_4
- `C21`: Adjust the azimuth of 3269905_1 by 18 degrees
- `C22`: Increase transmission power for 3258292_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.290 | MS1 | 121.4656714861 | 31.1446226285 | 680 | 504990 | -78.20 | 17.68 | 412.16 | 0.20 | 2.25 | 1585 |
| 2024-09-20 22:21:32.503 | MS1 | 121.4656775456 | 31.1446330645 | 680 | 504990 | -81.95 | 12.95 | 356.31 | 0.20 | 2.90 | 1588 |
| 2024-09-20 22:21:33.331 | MS1 | 121.4656704550 | 31.1446262945 | 680 | 504990 | -77.93 | 13.28 | 456.02 | 0.20 | 2.33 | 1572 |
| 2024-09-20 22:21:34.459 | MS1 | 121.4656769778 | 31.1446224806 | 680 | 504990 | -88.99 | -1.61 | 71.01 | 0.03 | 1.10 | 1591 |
| 2024-09-20 22:21:35.816 | MS1 | 121.4656701656 | 31.1446259283 | 680 | 504990 | -85.74 | -3.63 | 44.25 | 0.17 | 1.31 | 1599 |
| 2024-09-20 22:21:36.901 | MS1 | 121.4656751566 | 31.1446302866 | 680 | 504990 | -86.17 | -2.08 | 53.61 | 0.10 | 1.02 | 1585 |
| 2024-09-20 22:21:37.574 | MS1 | 121.4656661513 | 31.1446226155 | 680 | 504990 | -91.79 | -3.38 | 58.11 | 0.03 | 1.08 | 1599 |
| 2024-09-20 22:21:38.758 | MS1 | 121.4656700330 | 31.1446209300 | 680 | 504990 | -88.13 | -1.92 | 52.18 | 0.04 | 1.40 | 1581 |
| 2024-09-20 22:21:39.113 | MS1 | 121.4656728885 | 31.1446270177 | 340 | 504990 | -80.37 | 14.24 | 283.97 | 0.04 | 1.15 | 1597 |
| 2024-09-20 22:21:40.882 | MS1 | 121.4656656348 | 31.1446271291 | 340 | 504990 | -83.63 | 16.21 | 465.67 | 0.05 | 2.92 | 1562 |
| 2024-09-20 22:21:41.485 | MS1 | 121.4656611343 | 31.1446325650 | 340 | 504990 | -78.76 | 12.88 | 485.42 | 0.09 | 2.82 | 1584 |
| 2024-09-20 22:21:42.746 | MS1 | 121.4656763072 | 31.1446205167 | 340 | 504990 | -81.85 | 15.26 | 335.17 | 0.07 | 2.10 | 1584 |

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
| 3214108 | 3 | 121.4696220809 | 31.1482741736 | 28 | 4 | 11 | 30.1 | TDD | 980 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3258292 | 4 | 121.4671863525 | 31.1533722242 | 148 | 9 | 12 | 29.0 | TDD | 340 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3265899 | 2 | 121.4690144280 | 31.1508808062 | 249 | 7 | 10 | 25.6 | TDD | 204 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3269905 | 1 | 121.4701427067 | 31.1491118895 | 202 | 10 | 12 | 24.1 | TDD | 680 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.092 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.117 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.251 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.251 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.908 | NREventA3 | measId:2;ServCellPCI:553;Se... |
| 2024-09-20 22:21:38.148 | NRHandoverAttempt | SourcePCI:553;SourceNR-ARFC... |
| 2024-09-20 22:21:38.186 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.199 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.338 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.338 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269905 | 1 | 9.4360 | 5.5187 | -117.4459 | 5.9571 | 159.8721 | 0.0163 | 0.1976 |
| 2024_09_20 22:00 | 3265899 | 2 | 12.8920 | 7.1388 | -115.4618 | 5.9053 | 113.4000 | 0.0101 | 0.0182 |
| 2024_09_20 22:00 | 3214108 | 3 | 8.9708 | 17.5617 | -117.4770 | 5.9074 | 164.4759 | 0.0011 | 0.0002 |
| 2024_09_20 22:00 | 3258292 | 4 | 9.0306 | 9.1005 | -114.5718 | 15.3113 | 147.6882 | 0.0084 | 0.0061 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416434_2B2AED11 | 504990 | 340 | -81.5 | 504990 | 680 | -87.8 | 504990 | 204 | -86.8 | 504990 | 980 |
| MR_1774416434_C3CFD72C | 504990 | 340 | -83.2 | 504990 | 680 | -89.3 | 504990 | 204 | -87.3 | 504990 | 980 |
| MR_1774416434_4C5010B0 | 504990 | 680 | -87.0 | 504990 | 340 | -82.9 | 504990 | 204 | -87.0 | 504990 | 980 |
| MR_1774416434_0E0EEDDA | 504990 | 680 | -90.9 | 504990 | 340 | -81.4 | 504990 | 204 | -85.4 | 504990 | 980 |
| MR_1774416434_48A9B29F | 504990 | 680 | -88.7 | 504990 | 340 | -84.8 | 504990 | 204 | -85.0 | 504990 | 980 |
| MR_1774416434_CA072269 | 504990 | 340 | -84.6 | 504990 | 680 | -89.9 | 504990 | 204 | -86.1 | 504990 | 980 |
| MR_1774416434_F2EC439F | 504990 | 340 | -81.8 | 504990 | 680 | -87.4 | 504990 | 204 | -87.5 | 504990 | 980 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 652: `0e747f73-510...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0e747f73-510e-41ec-bd90-c023745734e6` |
| Tag | **multiple-answer** |
| 정답 | **C14|C19** |
| C14 의미 | Increase transmission power for 3242180_4 |
| C19 의미 | Adjust the azimuth of 3242180_4 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[652] topology](images/train_0652.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3242180_4
- `C2`: Add neighbor relationship between 3232024_3 and 3268818_2
- `C3`: Lift the tilt angle  of 3268818_2 by 3 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268818_2
- `C5`: Lift the tilt angle of 3242180_4 by 8 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease transmission power for 3268818_2
- `C8`: Increase A3 Offset threshold for 3268818_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242180_4
- `C10`: Press down the tilt angle  of 3268818_2 by 3 degrees
- `C11`: Adjust the azimuth of 3268818_2 by 9 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268818_2
- `C13`: Add neighbor relationship between 3242180_4 and 3268818_2
- `C14`: Increase transmission power for 3242180_4 **← 정답**
- `C15`: Press down the tilt angle of 3242180_4 by 8 degrees
- `C16`: Increase transmission power for 3268818_2
- `C17`: Decrease transmission power for 3242180_4
- `C18`: Check test server and transmission issues
- `C19`: Adjust the azimuth of 3242180_4 by 50 degrees **← 정답**
- `C20`: Increase A3 Offset threshold for 3242180_4
- `C21`: Decrease A3 Offset threshold for 3268818_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242180_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.880 | MS1 | 121.4656678838 | 31.1446379526 | 919 | 504990 | -93.31 | 17.56 | 572.06 | 0.20 | 2.33 | 1593 |
| 2024-09-20 22:21:32.909 | MS1 | 121.4656700270 | 31.1446222432 | 919 | 504990 | -93.53 | 15.75 | 498.53 | 0.19 | 2.75 | 1573 |
| 2024-09-20 22:21:33.830 | MS1 | 121.4656732929 | 31.1446189421 | 919 | 504990 | -94.44 | 13.77 | 370.00 | 0.07 | 2.78 | 1569 |
| 2024-09-20 22:21:34.618 | MS1 | 121.4656587523 | 31.1446196195 | 919 | 504990 | -109.63 | -0.31 | 55.97 | 0.11 | 1.02 | 1572 |
| 2024-09-20 22:21:35.329 | MS1 | 121.4656614851 | 31.1446209119 | 919 | 504990 | -109.31 | -0.85 | 48.18 | 0.05 | 1.22 | 1595 |
| 2024-09-20 22:21:36.278 | MS1 | 121.4656752083 | 31.1446324179 | 919 | 504990 | -103.80 | -1.23 | 49.01 | 0.14 | 1.34 | 1573 |
| 2024-09-20 22:21:37.572 | MS1 | 121.4656779159 | 31.1446323553 | 919 | 504990 | -102.54 | -0.28 | 72.60 | 0.19 | 1.43 | 1561 |
| 2024-09-20 22:21:38.104 | MS1 | 121.4656703802 | 31.1446239052 | 919 | 504990 | -104.69 | -0.81 | 75.92 | 0.06 | 1.03 | 1569 |
| 2024-09-20 22:21:39.238 | MS1 | 121.4656669059 | 31.1446213586 | 919 | 504990 | -101.06 | -1.82 | 51.12 | 0.16 | 1.03 | 1567 |
| 2024-09-20 22:21:40.477 | MS1 | 121.4656663411 | 31.1446214929 | 919 | 504990 | -89.24 | 17.04 | 591.30 | 0.12 | 2.65 | 1587 |
| 2024-09-20 22:21:41.401 | MS1 | 121.4656764511 | 31.1446362527 | 919 | 504990 | -85.25 | 16.71 | 373.43 | 0.16 | 2.16 | 1572 |
| 2024-09-20 22:21:42.246 | MS1 | 121.4656638660 | 31.1446330901 | 919 | 504990 | -93.61 | 17.02 | 389.21 | 0.13 | 2.63 | 1560 |

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
| 3232024 | 3 | 121.4725023709 | 31.1539397581 | 117 | 6 | 5 | 17.6 | TDD | 937 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3242180 | 4 | 121.4693311973 | 31.1473605560 | 300 | 5 | 6 | 26.6 | TDD | 919 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3258822 | 1 | 121.4746743800 | 31.1490556206 | 140 | 0 | 1 | 42.4 | TDD | 73 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3268818 | 2 | 121.4681969797 | 31.1531173243 | 185 | 2 | 1 | 21.8 | TDD | 657 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.772 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.790 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.903 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.903 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.118 | NREventA2 | measId:1;ServCellPCI:131;Se... |
| 2024-09-20 22:21:34.263 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258822 | 1 | 9.6233 | 14.5836 | -116.6663 | 13.5798 | 102.9141 | 0.0002 | 0.0198 |
| 2024_09_20 22:00 | 3268818 | 2 | 11.6194 | 16.4588 | -116.6771 | 18.5827 | 83.4372 | 0.0198 | 0.0136 |
| 2024_09_20 22:00 | 3232024 | 3 | 13.8565 | 12.0419 | -117.9362 | 14.9264 | 147.3247 | 0.0198 | 0.0081 |
| 2024_09_20 22:00 | 3242180 | 4 | 12.0218 | 5.3249 | -115.6176 | 9.2567 | 175.4530 | 0.1964 | 0.0045 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413344_2A30D74E | 504990 | 919 | -107.7 | 504990 | 657 | -112.7 | 504990 | 937 | -120.8 | 504990 | 73 |
| MR_1774413344_C1ECE50B | 504990 | 919 | -108.8 | 504990 | 657 | -115.3 | 504990 | 937 | -121.7 | 504990 | 73 |
| MR_1774413344_1DA52EEC | 504990 | 919 | -108.1 | 504990 | 657 | -113.3 | 504990 | 937 | -124.0 | 504990 | 73 |
| MR_1774413344_9E8D517B | 504990 | 919 | -109.1 | 504990 | 657 | -112.4 | 504990 | 937 | -123.2 | 504990 | 73 |
| MR_1774413344_29C12279 | 504990 | 919 | -109.1 | 504990 | 657 | -113.9 | 504990 | 937 | -121.3 | 504990 | 73 |
| MR_1774413344_9C1177BA | 504990 | 919 | -111.4 | 504990 | 657 | -116.0 | 504990 | 937 | -121.3 | 504990 | 73 |
| MR_1774413344_AFBDFC40 | 504990 | 919 | -108.6 | 504990 | 657 | -114.6 | 504990 | 937 | -123.7 | 504990 | 73 |
| MR_1774413344_D0097AD2 | 504990 | 919 | -110.9 | 504990 | 657 | -112.4 | 504990 | 937 | -121.4 | 504990 | 73 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 653: `c4415023-baa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c4415023-baa8-4f5e-9795-d96b1198e3c3` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267310_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[653] topology](images/train_0653.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3267310_3 by 26 degrees
- `C2`: Adjust the azimuth of 3242738_4 by 29 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242738_4
- `C4`: Increase transmission power for 3242738_4
- `C5`: Decrease A3 Offset threshold for 3267310_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267310_3 **← 정답**
- `C7`: Check test server and transmission issues
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease A3 Offset threshold for 3242738_4
- `C10`: Add neighbor relationship between 3267310_3 and 3242738_4
- `C11`: Decrease transmission power for 3242738_4
- `C12`: Increase A3 Offset threshold for 3267310_3
- `C13`: Press down the tilt angle  of 3242738_4 by 1 degrees
- `C14`: Press down the tilt angle of 3267310_3 by 5 degrees
- `C15`: Decrease transmission power for 3267310_3
- `C16`: Add neighbor relationship between 3222378_12 and 3242738_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242738_4
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267310_3
- `C19`: Lift the tilt angle of 3267310_3 by 5 degrees
- `C20`: Increase A3 Offset threshold for 3242738_4
- `C21`: Lift the tilt angle  of 3242738_4 by 1 degrees
- `C22`: Increase transmission power for 3267310_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.123 | MS1 | 121.4656589914 | 31.1446259314 | 783 | 504990 | -95.82 | 12.91 | 592.48 | 0.16 | 2.01 | 1589 |
| 2024-09-20 22:21:32.113 | MS1 | 121.4656707221 | 31.1446349178 | 427 | 504990 | -95.95 | 14.23 | 593.58 | 0.14 | 2.40 | 1595 |
| 2024-09-20 22:21:33.410 | MS1 | 121.4656671918 | 31.1446307980 | 228 | 504990 | -94.94 | 10.61 | 407.01 | 0.16 | 2.45 | 1567 |
| 2024-09-20 22:21:34.177 | MS1 | 121.4656641077 | 31.1446290601 | 178 | 152650 | -96.46 | 2.33 | 96.08 | 0.02 | 1.74 | 997 |
| 2024-09-20 22:21:35.719 | MS1 | 121.4656619294 | 31.1446360353 | 189 | 152650 | -89.31 | 7.12 | 80.40 | 0.09 | 1.95 | 976 |
| 2024-09-20 22:21:36.454 | MS1 | 121.4656645372 | 31.1446309868 | 955 | 152650 | -93.97 | 5.38 | 52.50 | 0.19 | 1.54 | 928 |
| 2024-09-20 22:21:37.739 | MS1 | 121.4656710974 | 31.1446291731 | 168 | 152650 | -96.85 | 5.09 | 45.71 | 0.10 | 1.80 | 910 |
| 2024-09-20 22:21:38.505 | MS1 | 121.4656647252 | 31.1446341061 | 178 | 152650 | -87.90 | 5.95 | 62.34 | 0.06 | 1.53 | 940 |
| 2024-09-20 22:21:39.648 | MS1 | 121.4656628722 | 31.1446190195 | 189 | 152650 | -93.34 | 5.96 | 66.08 | 0.01 | 1.99 | 900 |
| 2024-09-20 22:21:40.463 | MS1 | 121.4656753237 | 31.1446245289 | 955 | 152650 | -90.48 | 2.07 | 71.42 | 0.13 | 2.44 | 1583 |
| 2024-09-20 22:21:41.634 | MS1 | 121.4656748603 | 31.1446199443 | 168 | 152650 | -91.19 | 6.27 | 77.38 | 0.20 | 2.00 | 1594 |
| 2024-09-20 22:21:42.855 | MS1 | 121.4656623328 | 31.1446240237 | 178 | 152650 | -96.12 | 6.95 | 83.06 | 0.11 | 2.32 | 1587 |

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
| 3210266 | 7 | 121.4743390265 | 31.1523064752 | 129 | 1 | 6 | 12.5 | FDD | 451 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3210975 | 10 | 121.4716332627 | 31.1466328081 | 184 | 1 | 11 | 29.9 | FDD | 149 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3222378 | 12 | 121.4645262428 | 31.1472659772 | 108 | 1 | 0 | 18.4 | FDD | 955 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3232153 | 6 | 121.4655502652 | 31.1527094023 | 222 | 2 | 1 | 4.8 | TDD | 350 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3235456 | 5 | 121.4752957001 | 31.1488266031 | 143 | 14 | 11 | 10.0 | TDD | 86 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3238442 | 11 | 121.4680480223 | 31.1474575490 | 339 | 2 | 3 | 10.2 | FDD | 890 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3242738 | 4 | 121.4645008660 | 31.1538023619 | 145 | 1 | 2 | 0.4 | TDD | 432 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3247217 | 13 | 121.4660078554 | 31.1449587277 | 13 | 10 | 9 | 24.1 | FDD | 189 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3249695 | 8 | 121.4723969676 | 31.1487363881 | 129 | 8 | 9 | 11.6 | FDD | 168 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3260630 | 2 | 121.4684038196 | 31.1449799632 | 346 | 0 | 10 | 17.6 | TDD | 427 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3262528 | 9 | 121.4653337170 | 31.1466509854 | 289 | 12 | 10 | 6.7 | FDD | 178 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3267310 | 3 | 121.4688446620 | 31.1489439865 | 186 | 4 | 7 | 11.6 | TDD | 783 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3275909 | 1 | 121.4687777089 | 31.1515340923 | 334 | 7 | 12 | 20.0 | TDD | 228 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.981 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.999 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.128 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.128 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.816 | NREventA2 | measId:1;ServCellPCI:467;Se... |
| 2024-09-20 22:21:34.923 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.132 | NREventA5 | measId:3;ServCellPCI:467;Se... |
| 2024-09-20 22:21:35.177 | NRHandoverAttempt | SourcePCI:467;SourceNR-ARFC... |
| 2024-09-20 22:21:35.201 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.214 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.342 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.342 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275909 | 1 | 9.2768 | 12.4773 | -115.6392 | 11.1880 | 152.8175 | 0.0091 | 0.0082 |
| 2024_09_20 22:00 | 3260630 | 2 | 8.1861 | 18.9501 | -114.1324 | 7.7025 | 126.3383 | 0.0005 | 0.0086 |
| 2024_09_20 22:00 | 3267310 | 3 | 19.3899 | 8.4202 | -116.4726 | 18.3458 | 129.0815 | 0.0002 | 0.0168 |
| 2024_09_20 22:00 | 3242738 | 4 | 9.4606 | 15.0630 | -114.0580 | 8.8288 | 106.1824 | 0.0111 | 0.0067 |
| 2024_09_20 22:00 | 3235456 | 5 | 10.5622 | 13.8301 | -117.9262 | 10.8093 | 157.6518 | 0.0145 | 0.0076 |
| 2024_09_20 22:00 | 3232153 | 6 | 9.1925 | 5.4853 | -116.2572 | 13.5263 | 164.1377 | 0.0103 | 0.0162 |
| 2024_09_20 22:00 | 3210266 | 7 | 17.2402 | 6.8819 | -115.3872 | 3.0566 | 52.4465 | 0.0083 | 0.0150 |
| 2024_09_20 22:00 | 3249695 | 8 | 13.1440 | 16.8096 | -114.8274 | 3.0833 | 44.2953 | 0.0002 | 0.0094 |
| 2024_09_20 22:00 | 3262528 | 9 | 15.1986 | 12.8961 | -116.6211 | 4.7861 | 45.5869 | 0.0197 | 0.0048 |
| 2024_09_20 22:00 | 3210975 | 10 | 13.5037 | 5.6431 | -114.1605 | 4.0429 | 22.0790 | 0.0103 | 0.0141 |
| 2024_09_20 22:00 | 3238442 | 11 | 10.1413 | 15.7948 | -114.7185 | 4.3679 | 20.2545 | 0.0085 | 0.0070 |
| 2024_09_20 22:00 | 3222378 | 12 | 19.9647 | 15.2286 | -116.9941 | 4.7575 | 56.6369 | 0.0145 | 0.0039 |
| 2024_09_20 22:00 | 3247217 | 13 | 19.2138 | 12.5510 | -115.3125 | 3.3888 | 33.7307 | 0.0008 | 0.0158 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414049_36F0CCF2 | 152650 | 178 | -96.0 | 152650 | 149 | -101.1 | 152650 | 890 | -105.3 | 152650 | 451 |
| MR_1774414049_7C68D409 | 152650 | 178 | -95.6 | 152650 | 149 | -102.1 | 152650 | 890 | -104.8 | 152650 | 451 |
| MR_1774414049_4121B0F2 | 152650 | 178 | -96.3 | 152650 | 149 | -100.2 | 152650 | 890 | -102.8 | 152650 | 451 |
| MR_1774414049_DDB7F0EC | 152650 | 178 | -98.1 | 152650 | 149 | -102.1 | 152650 | 890 | -105.0 | 152650 | 451 |
| MR_1774414049_D633925C | 152650 | 178 | -96.8 | 152650 | 149 | -102.2 | 152650 | 890 | -104.2 | 152650 | 451 |
| MR_1774414049_497BB9A7 | 152650 | 178 | -95.4 | 152650 | 149 | -100.6 | 152650 | 890 | -103.4 | 152650 | 451 |
| MR_1774414049_7D790365 | 504990 | 228 | -94.1 | 504990 | 432 | -94.8 | 504990 | 350 | -99.9 | 504990 | 86 |
| MR_1774414049_47748901 | 504990 | 228 | -93.2 | 504990 | 432 | -94.5 | 504990 | 350 | -97.6 | 504990 | 86 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 654: `0145f9c4-6c8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0145f9c4-6c8f-4693-931b-60d09a9c26bc` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[654] topology](images/train_0654.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230779_1
- `C2`: Increase A3 Offset threshold for 3275651_3
- `C3`: Add neighbor relationship between 3275651_3 and 3230779_1
- `C4`: Insufficient data; more data is needed for judgment. **← 정답**
- `C5`: Add neighbor relationship between 3210502_2 and 3230779_1
- `C6`: Adjust the azimuth of 3230779_1 by 50 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275651_3
- `C8`: Adjust the azimuth of 3275651_3 by 32 degrees
- `C9`: Lift the tilt angle  of 3230779_1 by 10 degrees
- `C10`: Decrease A3 Offset threshold for 3275651_3
- `C11`: Decrease transmission power for 3230779_1
- `C12`: Press down the tilt angle  of 3230779_1 by 10 degrees
- `C13`: Decrease transmission power for 3275651_3
- `C14`: Press down the tilt angle of 3275651_3 by 7 degrees
- `C15`: Check test server and transmission issues
- `C16`: Decrease A3 Offset threshold for 3230779_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275651_3
- `C18`: Increase transmission power for 3275651_3
- `C19`: Increase A3 Offset threshold for 3230779_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230779_1
- `C21`: Increase transmission power for 3230779_1
- `C22`: Lift the tilt angle of 3275651_3 by 7 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.449 | MS1 | 121.4656669389 | 31.1446242822 | 654 | 504990 | -87.21 | 16.90 | 541.35 | 0.13 | 2.84 | 1599 |
| 2024-09-20 22:21:32.120 | MS1 | 121.4656711739 | 31.1446212936 | 654 | 504990 | -87.51 | 13.05 | 559.34 | 0.12 | 2.61 | 1588 |
| 2024-09-20 22:21:33.726 | MS1 | 121.4656700844 | 31.1446319109 | 654 | 504990 | -85.44 | 14.51 | 558.44 | 0.05 | 2.67 | 1582 |
| 2024-09-20 22:21:34.340 | MS1 | 121.4656595570 | 31.1446311396 | 654 | 504990 | -90.23 | 15.11 | 85.46 | 0.07 | 2.99 | 1572 |
| 2024-09-20 22:21:35.808 | MS1 | 121.4656641544 | 31.1446362771 | 654 | 504990 | -91.61 | 14.91 | 74.69 | 0.04 | 2.43 | 1568 |
| 2024-09-20 22:21:36.462 | MS1 | 121.4656745834 | 31.1446180821 | 654 | 504990 | -85.16 | 16.41 | 53.75 | 0.03 | 2.13 | 1572 |
| 2024-09-20 22:21:37.421 | MS1 | 121.4656674202 | 31.1446262295 | 654 | 504990 | -90.11 | 12.45 | 60.11 | 0.15 | 2.46 | 1594 |
| 2024-09-20 22:21:38.488 | MS1 | 121.4656683875 | 31.1446364073 | 654 | 504990 | -91.94 | 7.51 | 82.21 | 0.20 | 2.56 | 1589 |
| 2024-09-20 22:21:39.220 | MS1 | 121.4656656056 | 31.1446333016 | 654 | 504990 | -93.97 | 10.06 | 68.49 | 0.04 | 2.14 | 1567 |
| 2024-09-20 22:21:40.438 | MS1 | 121.4656729734 | 31.1446347421 | 654 | 504990 | -89.24 | 12.14 | 433.75 | 0.14 | 2.07 | 1597 |
| 2024-09-20 22:21:41.971 | MS1 | 121.4656663870 | 31.1446187404 | 654 | 504990 | -93.28 | 9.35 | 495.64 | 0.11 | 2.89 | 1589 |
| 2024-09-20 22:21:42.398 | MS1 | 121.4656693373 | 31.1446180836 | 654 | 504990 | -91.77 | 8.89 | 392.18 | 0.05 | 2.61 | 1588 |

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
| 3210502 | 2 | 121.4685260452 | 31.1495688105 | 244 | 14 | 9 | 20.4 | TDD | 2 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3230779 | 1 | 121.4713567643 | 31.1532493112 | 134 | 12 | 5 | 32.9 | TDD | 824 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3266222 | 4 | 121.4743864370 | 31.1484501248 | 101 | 2 | 0 | 29.8 | TDD | 31 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3275651 | 3 | 121.4646801552 | 31.1473902374 | 131 | 1 | 5 | 31.4 | TDD | 654 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.495 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.514 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.659 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.659 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.345 | NREventA3 | measId:2;ServCellPCI:686;Se... |
| 2024-09-20 22:21:38.585 | NRHandoverAttempt | SourcePCI:686;SourceNR-ARFC... |
| 2024-09-20 22:21:38.622 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.637 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.768 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.768 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3230779 | 1 | 81.8309 | 84.5590 | -117.3325 | 11.0429 | 94.0837 | 0.0009 | 0.0002 |
| 2024_09_19 22:00 | 3210502 | 2 | 78.3839 | 91.2748 | -114.8463 | 13.7160 | 122.8680 | 0.0010 | 0.0135 |
| 2024_09_19 22:00 | 3275651 | 3 | 78.1718 | 92.4291 | -115.4764 | 6.2078 | 111.1916 | 0.0125 | 0.0128 |
| 2024_09_19 22:00 | 3266222 | 4 | 81.1799 | 93.8365 | -115.7194 | 12.4266 | 108.5072 | 0.0046 | 0.0175 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414270_FA5B72FB | 504990 | 654 | -91.5 | 504990 | 824 | -94.7 | 504990 | 2 | -98.6 | 504990 | 31 |
| MR_1774414270_17EEA52D | 504990 | 654 | -92.2 | 504990 | 824 | -96.9 | 504990 | 2 | -97.6 | 504990 | 31 |
| MR_1774414270_07FA9C1C | 504990 | 654 | -88.4 | 504990 | 824 | -95.4 | 504990 | 2 | -98.1 | 504990 | 31 |
| MR_1774414270_6ABCAEF2 | 504990 | 654 | -91.6 | 504990 | 824 | -97.3 | 504990 | 2 | -98.8 | 504990 | 31 |
| MR_1774414270_420C075A | 504990 | 654 | -90.2 | 504990 | 824 | -94.7 | 504990 | 2 | -99.5 | 504990 | 31 |
| MR_1774414270_2F291259 | 504990 | 654 | -90.9 | 504990 | 824 | -98.4 | 504990 | 2 | -100.3 | 504990 | 31 |
| MR_1774414270_FA703485 | 504990 | 654 | -89.0 | 504990 | 824 | -97.7 | 504990 | 2 | -98.2 | 504990 | 31 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 655: `b750b868-591...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b750b868-591c-46ac-806f-1ca34304dfef` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235430_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[655] topology](images/train_0655.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3253063_3
- `C2`: Increase A3 Offset threshold for 3235430_5
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253063_3
- `C4`: Increase transmission power for 3253063_3
- `C5`: Decrease A3 Offset threshold for 3235430_5
- `C6`: Adjust the azimuth of 3253063_3 by 18 degrees
- `C7`: Decrease transmission power for 3253063_3
- `C8`: Adjust the azimuth of 3235430_5 by 16 degrees
- `C9`: Press down the tilt angle  of 3253063_3 by 1 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235430_5 **← 정답**
- `C11`: Decrease transmission power for 3235430_5
- `C12`: Press down the tilt angle of 3235430_5 by 3 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Lift the tilt angle  of 3253063_3 by 1 degrees
- `C15`: Add neighbor relationship between 3213818_9 and 3253063_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235430_5
- `C17`: Check test server and transmission issues
- `C18`: Increase transmission power for 3235430_5
- `C19`: Lift the tilt angle of 3235430_5 by 3 degrees
- `C20`: Decrease A3 Offset threshold for 3253063_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253063_3
- `C22`: Add neighbor relationship between 3235430_5 and 3253063_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.997 | MS1 | 121.4656639438 | 31.1446290209 | 789 | 504990 | -95.76 | 11.55 | 409.12 | 0.04 | 2.72 | 1576 |
| 2024-09-20 22:21:32.384 | MS1 | 121.4656746435 | 31.1446208586 | 10 | 504990 | -95.45 | 14.53 | 383.46 | 0.07 | 2.46 | 1577 |
| 2024-09-20 22:21:33.601 | MS1 | 121.4656640037 | 31.1446230196 | 340 | 504990 | -93.75 | 9.70 | 528.11 | 0.02 | 2.64 | 1572 |
| 2024-09-20 22:21:34.505 | MS1 | 121.4656633219 | 31.1446358952 | 86 | 152650 | -89.87 | 7.62 | 87.05 | 0.01 | 1.69 | 935 |
| 2024-09-20 22:21:35.614 | MS1 | 121.4656602396 | 31.1446309101 | 794 | 152650 | -94.66 | 2.02 | 61.92 | 0.08 | 1.98 | 945 |
| 2024-09-20 22:21:36.415 | MS1 | 121.4656653055 | 31.1446334432 | 648 | 152650 | -87.94 | 7.95 | 76.18 | 0.06 | 1.67 | 982 |
| 2024-09-20 22:21:37.739 | MS1 | 121.4656715456 | 31.1446184438 | 623 | 152650 | -89.26 | 5.43 | 65.06 | 0.17 | 1.99 | 935 |
| 2024-09-20 22:21:38.154 | MS1 | 121.4656713083 | 31.1446334715 | 86 | 152650 | -88.11 | 5.09 | 72.33 | 0.01 | 1.61 | 975 |
| 2024-09-20 22:21:39.961 | MS1 | 121.4656683688 | 31.1446194263 | 794 | 152650 | -92.88 | 2.46 | 70.24 | 0.09 | 1.97 | 971 |
| 2024-09-20 22:21:40.899 | MS1 | 121.4656707132 | 31.1446247255 | 648 | 152650 | -92.09 | 7.59 | 66.95 | 0.14 | 2.83 | 1598 |
| 2024-09-20 22:21:41.658 | MS1 | 121.4656750427 | 31.1446225393 | 623 | 152650 | -87.31 | 2.33 | 65.36 | 0.10 | 2.92 | 1573 |
| 2024-09-20 22:21:42.673 | MS1 | 121.4656589522 | 31.1446231507 | 86 | 152650 | -89.63 | 7.74 | 67.95 | 0.09 | 2.17 | 1583 |

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
| 3213818 | 9 | 121.4725563983 | 31.1445223063 | 122 | 0 | 11 | 20.3 | FDD | 648 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3215058 | 8 | 121.4707700528 | 31.1502328103 | 204 | 3 | 2 | 23.7 | FDD | 610 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3217851 | 12 | 121.4743204046 | 31.1447661370 | 64 | 14 | 2 | 3.2 | FDD | 86 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3220343 | 4 | 121.4728104899 | 31.1454336736 | 42 | 0 | 7 | 20.7 | TDD | 340 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3235430 | 5 | 121.4757707288 | 31.1461896601 | 244 | 2 | 7 | 17.3 | TDD | 789 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3245759 | 7 | 121.4739610225 | 31.1503394301 | 277 | 12 | 6 | 13.0 | FDD | 736 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3247062 | 10 | 121.4665159192 | 31.1524757913 | 338 | 1 | 7 | 0.5 | FDD | 623 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3252235 | 13 | 121.4702399404 | 31.1450835662 | 123 | 10 | 0 | 11.8 | FDD | 794 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3253063 | 3 | 121.4678505056 | 31.1510216854 | 214 | 1 | 8 | 2.2 | TDD | 147 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3254697 | 11 | 121.4699447792 | 31.1537413986 | 241 | 6 | 5 | 16.9 | FDD | 115 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3266472 | 6 | 121.4700631005 | 31.1459666603 | 0 | 5 | 7 | 24.1 | TDD | 788 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3271434 | 1 | 121.4674155253 | 31.1460655838 | 216 | 14 | 9 | 12.8 | TDD | 10 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3278591 | 2 | 121.4753409898 | 31.1496802549 | 358 | 7 | 7 | 12.7 | TDD | 464 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.222 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.243 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.384 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.384 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.120 | NREventA2 | measId:1;ServCellPCI:728;Se... |
| 2024-09-20 22:21:35.266 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.540 | NREventA5 | measId:3;ServCellPCI:728;Se... |
| 2024-09-20 22:21:35.599 | NRHandoverAttempt | SourcePCI:728;SourceNR-ARFC... |
| 2024-09-20 22:21:35.649 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.662 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.785 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.785 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271434 | 1 | 7.7004 | 7.1584 | -115.2152 | 9.7493 | 99.8627 | 0.0145 | 0.0164 |
| 2024_09_20 22:00 | 3278591 | 2 | 17.8690 | 5.0089 | -115.4836 | 8.7651 | 121.2058 | 0.0015 | 0.0131 |
| 2024_09_20 22:00 | 3253063 | 3 | 9.6750 | 11.5678 | -114.5148 | 19.8998 | 168.6209 | 0.0182 | 0.0141 |
| 2024_09_20 22:00 | 3220343 | 4 | 5.2627 | 10.1356 | -114.9634 | 17.3502 | 184.1358 | 0.0179 | 0.0064 |
| 2024_09_20 22:00 | 3235430 | 5 | 19.2180 | 18.9319 | -114.6076 | 13.4216 | 140.7630 | 0.0004 | 0.0021 |
| 2024_09_20 22:00 | 3266472 | 6 | 12.9885 | 10.3977 | -117.0081 | 7.9951 | 104.3010 | 0.0093 | 0.0119 |
| 2024_09_20 22:00 | 3245759 | 7 | 6.0235 | 8.1468 | -114.8702 | 3.3908 | 39.0642 | 0.0053 | 0.0003 |
| 2024_09_20 22:00 | 3215058 | 8 | 11.6190 | 18.9215 | -117.7022 | 4.7279 | 53.6320 | 0.0083 | 0.0110 |
| 2024_09_20 22:00 | 3213818 | 9 | 5.9104 | 9.3453 | -115.7109 | 3.2849 | 41.7769 | 0.0153 | 0.0156 |
| 2024_09_20 22:00 | 3247062 | 10 | 5.8794 | 5.1612 | -117.2919 | 4.9503 | 32.7927 | 0.0091 | 0.0016 |
| 2024_09_20 22:00 | 3254697 | 11 | 14.5802 | 6.4623 | -114.2958 | 4.4943 | 40.8562 | 0.0099 | 0.0058 |
| 2024_09_20 22:00 | 3217851 | 12 | 9.5994 | 9.0250 | -114.7544 | 4.7372 | 22.3585 | 0.0070 | 0.0029 |
| 2024_09_20 22:00 | 3252235 | 13 | 7.7927 | 16.2666 | -115.0701 | 3.5629 | 58.0042 | 0.0156 | 0.0185 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416887_E83213AD | 152650 | 86 | -88.0 | 152650 | 610 | -92.2 | 152650 | 115 | -99.0 | 152650 | 736 |
| MR_1774416887_9532A87C | 152650 | 86 | -91.4 | 152650 | 610 | -91.3 | 152650 | 115 | -96.9 | 152650 | 736 |
| MR_1774416887_6D674D9C | 152650 | 86 | -91.2 | 152650 | 610 | -91.4 | 152650 | 115 | -98.0 | 152650 | 736 |
| MR_1774416887_B2D4C437 | 504990 | 340 | -93.1 | 504990 | 147 | -93.5 | 504990 | 464 | -100.4 | 504990 | 788 |
| MR_1774416887_E6BCB213 | 504990 | 340 | -95.0 | 504990 | 147 | -95.2 | 504990 | 464 | -100.2 | 504990 | 788 |
| MR_1774416887_94C043D3 | 152650 | 86 | -91.6 | 152650 | 610 | -92.4 | 152650 | 115 | -99.4 | 152650 | 736 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 656: `963ff3e1-571...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `963ff3e1-5718-4449-a978-832cd0ca68c4` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Decrease A3 Offset threshold for 3267402_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[656] topology](images/train_0656.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261837_4
- `C3`: Increase transmission power for 3261837_4
- `C4`: Lift the tilt angle  of 3261837_4 by 5 degrees
- `C5`: Decrease A3 Offset threshold for 3261837_4
- `C6`: Increase A3 Offset threshold for 3267402_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267402_3
- `C8`: Adjust the azimuth of 3267402_3 by 50 degrees
- `C9`: Increase A3 Offset threshold for 3261837_4
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease transmission power for 3261837_4
- `C12`: Lift the tilt angle of 3267402_3 by 7 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267402_3
- `C14`: Adjust the azimuth of 3261837_4 by 0 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261837_4
- `C16`: Press down the tilt angle  of 3261837_4 by 5 degrees
- `C17`: Decrease A3 Offset threshold for 3267402_3 **← 정답**
- `C18`: Add neighbor relationship between 3267402_3 and 3261837_4
- `C19`: Add neighbor relationship between 3249056_1 and 3261837_4
- `C20`: Increase transmission power for 3267402_3
- `C21`: Decrease transmission power for 3267402_3
- `C22`: Press down the tilt angle of 3267402_3 by 7 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.313 | MS1 | 121.4656589235 | 31.1446202250 | 310 | 504990 | -84.88 | 16.94 | 543.82 | 0.11 | 2.73 | 1561 |
| 2024-09-20 22:21:32.863 | MS1 | 121.4656651063 | 31.1446331904 | 310 | 504990 | -81.58 | 17.01 | 417.95 | 0.17 | 2.79 | 1595 |
| 2024-09-20 22:21:33.674 | MS1 | 121.4656687713 | 31.1446331789 | 310 | 504990 | -78.61 | 15.21 | 486.96 | 0.09 | 2.17 | 1582 |
| 2024-09-20 22:21:34.646 | MS1 | 121.4656586671 | 31.1446347770 | 310 | 504990 | -87.13 | -4.00 | 51.01 | 0.13 | 1.13 | 1572 |
| 2024-09-20 22:21:35.420 | MS1 | 121.4656643962 | 31.1446312114 | 310 | 504990 | -87.86 | -0.11 | 69.57 | 0.20 | 1.18 | 1564 |
| 2024-09-20 22:21:36.566 | MS1 | 121.4656717297 | 31.1446317045 | 310 | 504990 | -89.19 | -0.64 | 69.49 | 0.11 | 1.21 | 1588 |
| 2024-09-20 22:21:37.364 | MS1 | 121.4656684162 | 31.1446199519 | 310 | 504990 | -87.87 | -3.58 | 43.26 | 0.17 | 1.15 | 1588 |
| 2024-09-20 22:21:38.341 | MS1 | 121.4656689440 | 31.1446276484 | 310 | 504990 | -91.81 | -0.27 | 33.44 | 0.04 | 1.13 | 1563 |
| 2024-09-20 22:21:39.892 | MS1 | 121.4656738857 | 31.1446207697 | 967 | 504990 | -77.65 | 13.34 | 199.39 | 0.06 | 1.47 | 1569 |
| 2024-09-20 22:21:40.518 | MS1 | 121.4656697691 | 31.1446265901 | 967 | 504990 | -84.65 | 12.28 | 366.83 | 0.19 | 2.08 | 1600 |
| 2024-09-20 22:21:41.924 | MS1 | 121.4656680280 | 31.1446317918 | 967 | 504990 | -75.97 | 16.40 | 390.81 | 0.11 | 2.02 | 1563 |
| 2024-09-20 22:21:42.966 | MS1 | 121.4656643629 | 31.1446355080 | 967 | 504990 | -75.78 | 17.58 | 362.91 | 0.18 | 2.32 | 1577 |

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
| 3240637 | 2 | 121.4755653341 | 31.1556504587 | 272 | 12 | 5 | 38.2 | TDD | 28 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3249056 | 1 | 121.4745268123 | 31.1481295528 | 156 | 10 | 9 | 22.5 | TDD | 65 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3261837 | 4 | 121.4735305920 | 31.1450210220 | 267 | 3 | 5 | 29.8 | TDD | 967 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3267402 | 3 | 121.4712435590 | 31.1485645325 | 129 | 4 | 12 | 32.7 | TDD | 310 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.231 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.248 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.370 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.370 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.089 | NREventA3 | measId:2;ServCellPCI:900;Se... |
| 2024-09-20 22:21:38.329 | NRHandoverAttempt | SourcePCI:900;SourceNR-ARFC... |
| 2024-09-20 22:21:38.375 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.385 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.522 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.522 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249056 | 1 | 16.0695 | 19.5762 | -115.2681 | 6.1717 | 109.3140 | 0.0079 | 0.0167 |
| 2024_09_20 22:00 | 3240637 | 2 | 18.8663 | 11.6220 | -117.3581 | 11.1925 | 191.3143 | 0.0044 | 0.0059 |
| 2024_09_20 22:00 | 3267402 | 3 | 9.5574 | 15.0470 | -116.8546 | 10.2319 | 135.0284 | 0.0164 | 0.1936 |
| 2024_09_20 22:00 | 3261837 | 4 | 10.5330 | 5.3969 | -114.5249 | 5.3220 | 90.3280 | 0.0057 | 0.0097 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415027_230274FE | 504990 | 967 | -83.5 | 504990 | 310 | -87.7 | 504990 | 65 | -90.9 | 504990 | 28 |
| MR_1774415027_8CC24FEE | 504990 | 967 | -81.8 | 504990 | 310 | -86.3 | 504990 | 65 | -88.6 | 504990 | 28 |
| MR_1774415027_C97469EA | 504990 | 310 | -86.5 | 504990 | 967 | -80.7 | 504990 | 65 | -92.1 | 504990 | 28 |
| MR_1774415027_67EF7183 | 504990 | 967 | -80.7 | 504990 | 310 | -87.8 | 504990 | 65 | -91.5 | 504990 | 28 |
| MR_1774415027_49367D22 | 504990 | 310 | -85.3 | 504990 | 967 | -81.5 | 504990 | 65 | -91.6 | 504990 | 28 |
| MR_1774415027_1CCCF4B4 | 504990 | 967 | -82.5 | 504990 | 310 | -88.0 | 504990 | 65 | -91.9 | 504990 | 28 |
| MR_1774415027_ADBA4AC2 | 504990 | 310 | -89.1 | 504990 | 967 | -81.4 | 504990 | 65 | -90.1 | 504990 | 28 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 657: `ea4c0706-cad...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ea4c0706-cad5-41a8-9bb2-3a4889768318` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Lift the tilt angle  of 3258180_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[657] topology](images/train_0657.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3258180_2 by 22 degrees
- `C2`: Press down the tilt angle  of 3258180_2 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223764_1
- `C4`: Decrease A3 Offset threshold for 3259755_4
- `C5`: Decrease transmission power for 3223764_1
- `C6`: Check test server and transmission issues
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259755_4
- `C8`: Increase transmission power for 3223764_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259755_4
- `C10`: Increase A3 Offset threshold for 3223764_1
- `C11`: Press down the tilt angle of 3259755_4 by 4 degrees
- `C12`: Lift the tilt angle  of 3258180_2 by 10 degrees **← 정답**
- `C13`: Decrease A3 Offset threshold for 3223764_1
- `C14`: Increase A3 Offset threshold for 3259755_4
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223764_1
- `C17`: Lift the tilt angle of 3259755_4 by 4 degrees
- `C18`: Add neighbor relationship between 3258180_2 and 3223764_1
- `C19`: Add neighbor relationship between 3259755_4 and 3223764_1
- `C20`: Increase transmission power for 3259755_4
- `C21`: Adjust the azimuth of 3259755_4 by 23 degrees
- `C22`: Decrease transmission power for 3259755_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.935 | MS1 | 121.4656640036 | 31.1446365350 | 951 | 504990 | -86.89 | 15.50 | 436.40 | 0.15 | 2.45 | 1560 |
| 2024-09-20 22:21:32.103 | MS1 | 121.4656662138 | 31.1446290263 | 951 | 504990 | -91.23 | 17.95 | 326.73 | 0.05 | 2.23 | 1585 |
| 2024-09-20 22:21:33.215 | MS1 | 121.4656743124 | 31.1446340138 | 951 | 504990 | -91.69 | 16.32 | 509.82 | 0.15 | 2.75 | 1589 |
| 2024-09-20 22:21:34.726 | MS1 | 121.4656657202 | 31.1446377232 | 951 | 504990 | -87.59 | 12.81 | 55.52 | 0.05 | 2.91 | 1596 |
| 2024-09-20 22:21:35.190 | MS1 | 121.4656674643 | 31.1446212529 | 951 | 504990 | -85.57 | 12.27 | 54.38 | 0.17 | 2.15 | 1599 |
| 2024-09-20 22:21:36.536 | MS1 | 121.4656718400 | 31.1446243241 | 951 | 504990 | -88.53 | 14.70 | 93.30 | 0.13 | 2.70 | 1596 |
| 2024-09-20 22:21:37.274 | MS1 | 121.4656712572 | 31.1446355456 | 951 | 504990 | -90.74 | 7.33 | 44.89 | 0.10 | 2.28 | 1577 |
| 2024-09-20 22:21:38.828 | MS1 | 121.4656635696 | 31.1446214563 | 951 | 504990 | -89.01 | 9.82 | 95.07 | 0.13 | 2.40 | 1568 |
| 2024-09-20 22:21:39.214 | MS1 | 121.4656745810 | 31.1446372337 | 951 | 504990 | -93.67 | 7.29 | 77.18 | 0.01 | 2.96 | 1587 |
| 2024-09-20 22:21:40.753 | MS1 | 121.4656616889 | 31.1446344511 | 951 | 504990 | -91.45 | 9.55 | 345.32 | 0.08 | 2.77 | 1588 |
| 2024-09-20 22:21:41.961 | MS1 | 121.4656727252 | 31.1446213559 | 951 | 504990 | -93.04 | 8.73 | 436.77 | 0.09 | 2.42 | 1596 |
| 2024-09-20 22:21:42.623 | MS1 | 121.4656581440 | 31.1446221532 | 951 | 504990 | -93.60 | 7.93 | 459.78 | 0.01 | 2.14 | 1561 |

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
| 3223764 | 1 | 121.4753752404 | 31.1526679189 | 248 | 12 | 4 | 28.1 | TDD | 336 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3226054 | 3 | 121.4724979830 | 31.1462101772 | 310 | 9 | 8 | 39.1 | TDD | 225 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3258180 | 2 | 121.4660175068 | 31.1540226622 | 62 | 13 | 5 | 23.9 | TDD | 825 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3259755 | 4 | 121.4745670098 | 31.1446018598 | 247 | 3 | 4 | 21.9 | TDD | 951 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.258 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.277 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.379 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.379 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.121 | NREventA3 | measId:2;ServCellPCI:178;Se... |
| 2024-09-20 22:21:38.361 | NRHandoverAttempt | SourcePCI:178;SourceNR-ARFC... |
| 2024-09-20 22:21:38.401 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.415 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.552 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.552 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223764 | 1 | 14.3251 | 8.7491 | -117.7120 | 10.9051 | 190.3694 | 0.0198 | 0.0058 |
| 2024_09_20 22:00 | 3258180 | 2 | 15.9971 | 19.8750 | -115.2319 | 6.0558 | 108.6028 | 0.0178 | 0.0197 |
| 2024_09_20 22:00 | 3226054 | 3 | 18.1613 | 19.8203 | -115.5659 | 6.5155 | 83.0197 | 0.0073 | 0.0100 |
| 2024_09_20 22:00 | 3259755 | 4 | 87.4949 | 88.9800 | -117.8062 | 14.1407 | 192.8956 | 0.0119 | 0.0196 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415505_24767CE6 | 504990 | 951 | -87.3 | 504990 | 336 | -98.8 | 504990 | 825 | -100.0 | 504990 | 225 |
| MR_1774415505_87AC2833 | 504990 | 951 | -87.0 | 504990 | 336 | -96.2 | 504990 | 825 | -101.2 | 504990 | 225 |
| MR_1774415505_4EE9072F | 504990 | 951 | -87.9 | 504990 | 336 | -99.0 | 504990 | 825 | -100.0 | 504990 | 225 |
| MR_1774415505_21FC4990 | 504990 | 951 | -88.1 | 504990 | 336 | -98.9 | 504990 | 825 | -100.8 | 504990 | 225 |
| MR_1774415505_DE158D27 | 504990 | 951 | -88.1 | 504990 | 336 | -98.5 | 504990 | 825 | -100.2 | 504990 | 225 |
| MR_1774415505_0F5BAA07 | 504990 | 951 | -89.4 | 504990 | 336 | -96.4 | 504990 | 825 | -98.4 | 504990 | 225 |
| MR_1774415505_928FFEC0 | 504990 | 951 | -89.1 | 504990 | 336 | -97.2 | 504990 | 825 | -100.0 | 504990 | 225 |
| MR_1774415505_A569AD92 | 504990 | 951 | -87.6 | 504990 | 336 | -96.9 | 504990 | 825 | -101.3 | 504990 | 225 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 658: `2f62bb6a-b3a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2f62bb6a-b3ab-4a0a-823a-ba1d5f618a31` |
| Tag | **multiple-answer** |
| 정답 | **C2|C4|C18|C20** |
| C2 의미 | Press down the tilt angle  of 3219349_4 by 2 degrees |
| C4 의미 | Decrease transmission power for 3219349_4 |
| C18 의미 | Increase A3 Offset threshold for 3219349_4 |
| C20 의미 | Increase A3 Offset threshold for 3268741_3 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[658] topology](images/train_0658.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3268741_3
- `C2`: Press down the tilt angle  of 3219349_4 by 2 degrees **← 정답**
- `C3`: Increase transmission power for 3219349_4
- `C4`: Decrease transmission power for 3219349_4 **← 정답**
- `C5`: Lift the tilt angle  of 3219349_4 by 2 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Add neighbor relationship between 3224870_5 and 3219349_4
- `C8`: Increase transmission power for 3268741_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268741_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219349_4
- `C11`: Adjust the azimuth of 3219349_4 by 2 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268741_3
- `C13`: Press down the tilt angle of 3268741_3 by 5 degrees
- `C14`: Check test server and transmission issues
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219349_4
- `C16`: Decrease A3 Offset threshold for 3219349_4
- `C17`: Add neighbor relationship between 3268741_3 and 3219349_4
- `C18`: Increase A3 Offset threshold for 3219349_4 **← 정답**
- `C19`: Adjust the azimuth of 3268741_3 by 15 degrees
- `C20`: Increase A3 Offset threshold for 3268741_3 **← 정답**
- `C21`: Lift the tilt angle of 3268741_3 by 5 degrees
- `C22`: Decrease A3 Offset threshold for 3268741_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.330 | MS1 | 121.4656661498 | 31.1446355322 | 333 | 504990 | -78.32 | 13.09 | 336.07 | 0.19 | 2.06 | 1592 |
| 2024-09-20 22:21:32.952 | MS1 | 121.4656714655 | 31.1446233844 | 333 | 504990 | -78.66 | 12.77 | 533.82 | 0.07 | 2.12 | 1590 |
| 2024-09-20 22:21:33.891 | MS1 | 121.4656679878 | 31.1446376211 | 333 | 504990 | -82.94 | 15.50 | 403.41 | 0.04 | 2.30 | 1571 |
| 2024-09-20 22:21:34.509 | MS1 | 121.4656751671 | 31.1446268391 | 844 | 504990 | -82.29 | 3.05 | 21.98 | 0.12 | 1.21 | 1583 |
| 2024-09-20 22:21:35.520 | MS1 | 121.4656641592 | 31.1446254198 | 844 | 504990 | -81.49 | 3.33 | 53.55 | 0.00 | 1.47 | 1590 |
| 2024-09-20 22:21:36.154 | MS1 | 121.4656653221 | 31.1446245243 | 333 | 504990 | -88.18 | 2.67 | 57.37 | 0.12 | 1.35 | 1573 |
| 2024-09-20 22:21:37.185 | MS1 | 121.4656708506 | 31.1446295751 | 333 | 504990 | -88.99 | 4.05 | 71.44 | 0.16 | 1.02 | 1574 |
| 2024-09-20 22:21:38.856 | MS1 | 121.4656754115 | 31.1446247270 | 844 | 504990 | -86.97 | 3.58 | 55.48 | 0.07 | 1.18 | 1580 |
| 2024-09-20 22:21:39.290 | MS1 | 121.4656749555 | 31.1446190018 | 844 | 504990 | -83.21 | 1.19 | 57.92 | 0.06 | 1.49 | 1588 |
| 2024-09-20 22:21:40.502 | MS1 | 121.4656639005 | 31.1446264223 | 844 | 504990 | -84.44 | 15.98 | 582.30 | 0.17 | 2.96 | 1581 |
| 2024-09-20 22:21:41.473 | MS1 | 121.4656597209 | 31.1446275380 | 844 | 504990 | -82.27 | 12.15 | 545.47 | 0.10 | 2.88 | 1575 |
| 2024-09-20 22:21:42.730 | MS1 | 121.4656699822 | 31.1446249348 | 844 | 504990 | -75.74 | 16.85 | 561.64 | 0.18 | 2.20 | 1565 |

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
| 3217473 | 1 | 121.4736487540 | 31.1452242123 | 255 | 11 | 12 | 50.0 | TDD | 933 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3219349 | 4 | 121.4749370953 | 31.1501687140 | 237 | 0 | 6 | 29.0 | TDD | 690 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3224870 | 5 | 121.4648001487 | 31.1559993561 | 116 | 8 | 2 | 22.8 | TDD | 758 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3246213 | 2 | 121.4744261661 | 31.1542922425 | 208 | 5 | 8 | 47.4 | TDD | 844 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3268741 | 3 | 121.4692200660 | 31.1462775794 | 256 | 2 | 2 | 21.0 | TDD | 333 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.566 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.590 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.694 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.694 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.431 | NREventA3 | measId:2;ServCellPCI:892;Se... |
| 2024-09-20 22:21:34.671 | NRHandoverAttempt | SourcePCI:892;SourceNR-ARFC... |
| 2024-09-20 22:21:34.701 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.711 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:34.833 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.833 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.431 | NREventA3 | measId:2;ServCellPCI:250;Se... |
| 2024-09-20 22:21:36.671 | NRHandoverAttempt | SourcePCI:250;SourceNR-ARFC... |
| 2024-09-20 22:21:36.718 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.731 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.840 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.840 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.431 | NREventA3 | measId:2;ServCellPCI:892;Se... |
| 2024-09-20 22:21:38.671 | NRHandoverAttempt | SourcePCI:892;SourceNR-ARFC... |
| 2024-09-20 22:21:38.701 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.713 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.861 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.861 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217473 | 1 | 5.9787 | 5.5047 | -114.6539 | 13.4482 | 148.4304 | 0.0060 | 0.0119 |
| 2024_09_20 22:00 | 3246213 | 2 | 6.0730 | 13.4764 | -114.6473 | 5.8844 | 166.4196 | 0.0180 | 0.0139 |
| 2024_09_20 22:00 | 3268741 | 3 | 9.2995 | 12.3582 | -115.7162 | 11.2415 | 88.9995 | 0.0188 | 0.0018 |
| 2024_09_20 22:00 | 3219349 | 4 | 19.9027 | 19.5828 | -114.8759 | 18.1562 | 111.2334 | 0.0062 | 0.0170 |
| 2024_09_20 22:00 | 3224870 | 5 | 10.0203 | 9.3530 | -115.4562 | 19.0721 | 183.7683 | 0.0033 | 0.0173 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415560_A327454C | 504990 | 844 | -82.5 | 504990 | 333 | -82.9 | 504990 | 690 | -87.6 | 504990 | 758 |
| MR_1774415560_5BF69049 | 504990 | 844 | -82.1 | 504990 | 333 | -82.6 | 504990 | 690 | -86.4 | 504990 | 758 |
| MR_1774415560_8998F43C | 504990 | 844 | -80.7 | 504990 | 333 | -84.3 | 504990 | 690 | -86.6 | 504990 | 758 |
| MR_1774415560_23E7D0D5 | 504990 | 844 | -82.9 | 504990 | 333 | -81.8 | 504990 | 690 | -85.4 | 504990 | 758 |
| MR_1774415560_358AA579 | 504990 | 333 | -81.4 | 504990 | 844 | -81.5 | 504990 | 690 | -87.6 | 504990 | 758 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 659: `78d4b233-8f0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `78d4b233-8f06-4dc3-83ce-236548d291c3` |
| Tag | **multiple-answer** |
| 정답 | **C2|C10|C11|C15** |
| C2 의미 | Increase A3 Offset threshold for 3220576_3 |
| C10 의미 | Press down the tilt angle  of 3220576_3 by 3 degrees |
| C11 의미 | Decrease transmission power for 3220576_3 |
| C15 의미 | Increase A3 Offset threshold for 3253316_5 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[659] topology](images/train_0659.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase A3 Offset threshold for 3220576_3 **← 정답**
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220576_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253316_5
- `C5`: Decrease A3 Offset threshold for 3220576_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253316_5
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220576_3
- `C8`: Add neighbor relationship between 3247088_1 and 3220576_3
- `C9`: Adjust the azimuth of 3253316_5 by 6 degrees
- `C10`: Press down the tilt angle  of 3220576_3 by 3 degrees **← 정답**
- `C11`: Decrease transmission power for 3220576_3 **← 정답**
- `C12`: Increase transmission power for 3253316_5
- `C13`: Lift the tilt angle of 3253316_5 by 2 degrees
- `C14`: Adjust the azimuth of 3220576_3 by 20 degrees
- `C15`: Increase A3 Offset threshold for 3253316_5 **← 정답**
- `C16`: Lift the tilt angle  of 3220576_3 by 3 degrees
- `C17`: Decrease A3 Offset threshold for 3253316_5
- `C18`: Press down the tilt angle of 3253316_5 by 2 degrees
- `C19`: Check test server and transmission issues
- `C20`: Increase transmission power for 3220576_3
- `C21`: Decrease transmission power for 3253316_5
- `C22`: Add neighbor relationship between 3253316_5 and 3220576_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.379 | MS1 | 121.4656723122 | 31.1446284255 | 412 | 504990 | -77.51 | 14.35 | 509.18 | 0.06 | 2.22 | 1568 |
| 2024-09-20 22:21:32.945 | MS1 | 121.4656617695 | 31.1446325493 | 412 | 504990 | -79.59 | 12.64 | 526.80 | 0.17 | 2.38 | 1578 |
| 2024-09-20 22:21:33.793 | MS1 | 121.4656743715 | 31.1446376200 | 412 | 504990 | -75.12 | 15.53 | 366.59 | 0.14 | 2.84 | 1576 |
| 2024-09-20 22:21:34.620 | MS1 | 121.4656654288 | 31.1446289810 | 411 | 504990 | -82.19 | 1.66 | 48.01 | 0.20 | 1.38 | 1563 |
| 2024-09-20 22:21:35.404 | MS1 | 121.4656762601 | 31.1446209793 | 411 | 504990 | -88.73 | 4.06 | 50.26 | 0.04 | 1.17 | 1573 |
| 2024-09-20 22:21:36.627 | MS1 | 121.4656592932 | 31.1446223319 | 412 | 504990 | -83.08 | 1.03 | 54.02 | 0.19 | 1.35 | 1567 |
| 2024-09-20 22:21:37.914 | MS1 | 121.4656768253 | 31.1446276650 | 412 | 504990 | -81.79 | 2.02 | 81.82 | 0.14 | 1.33 | 1567 |
| 2024-09-20 22:21:38.625 | MS1 | 121.4656766722 | 31.1446206516 | 411 | 504990 | -88.79 | 3.67 | 74.39 | 0.16 | 1.29 | 1566 |
| 2024-09-20 22:21:39.416 | MS1 | 121.4656629600 | 31.1446214280 | 411 | 504990 | -81.78 | 4.42 | 76.14 | 0.18 | 1.20 | 1583 |
| 2024-09-20 22:21:40.600 | MS1 | 121.4656738561 | 31.1446303131 | 411 | 504990 | -79.86 | 16.63 | 522.72 | 0.20 | 2.37 | 1595 |
| 2024-09-20 22:21:41.499 | MS1 | 121.4656680555 | 31.1446372964 | 411 | 504990 | -78.43 | 14.17 | 573.13 | 0.00 | 2.57 | 1584 |
| 2024-09-20 22:21:42.436 | MS1 | 121.4656581321 | 31.1446378575 | 411 | 504990 | -84.02 | 15.81 | 579.31 | 0.18 | 2.45 | 1561 |

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
| 3220576 | 3 | 121.4697444496 | 31.1472970790 | 213 | 0 | 3 | 29.1 | TDD | 631 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3245680 | 2 | 121.4647182691 | 31.1535979766 | 268 | 7 | 4 | 39.7 | TDD | 273 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3247088 | 1 | 121.4703905867 | 31.1442793053 | 213 | 1 | 7 | 23.5 | TDD | 229 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3253316 | 5 | 121.4743953532 | 31.1512549253 | 234 | 1 | 7 | 29.0 | TDD | 412 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3261175 | 4 | 121.4744712975 | 31.1521772959 | 250 | 12 | 9 | 15.8 | TDD | 411 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.368 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.392 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.493 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.493 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.171 | NREventA3 | measId:2;ServCellPCI:484;Se... |
| 2024-09-20 22:21:34.411 | NRHandoverAttempt | SourcePCI:484;SourceNR-ARFC... |
| 2024-09-20 22:21:34.458 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.469 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:34.573 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.573 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.171 | NREventA3 | measId:2;ServCellPCI:362;Se... |
| 2024-09-20 22:21:36.411 | NRHandoverAttempt | SourcePCI:362;SourceNR-ARFC... |
| 2024-09-20 22:21:36.460 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.474 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.608 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.608 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.171 | NREventA3 | measId:2;ServCellPCI:484;Se... |
| 2024-09-20 22:21:38.411 | NRHandoverAttempt | SourcePCI:484;SourceNR-ARFC... |
| 2024-09-20 22:21:38.444 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.454 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.597 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.597 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247088 | 1 | 5.7205 | 14.1055 | -114.7277 | 19.3619 | 150.1040 | 0.0040 | 0.0006 |
| 2024_09_20 22:00 | 3245680 | 2 | 19.1311 | 5.4315 | -116.2409 | 16.2104 | 110.5811 | 0.0156 | 0.0114 |
| 2024_09_20 22:00 | 3220576 | 3 | 8.2123 | 18.8249 | -117.9394 | 6.5576 | 145.3660 | 0.0081 | 0.0005 |
| 2024_09_20 22:00 | 3261175 | 4 | 7.3928 | 12.2470 | -117.9144 | 17.4934 | 115.1818 | 0.0014 | 0.0023 |
| 2024_09_20 22:00 | 3253316 | 5 | 17.7578 | 10.0896 | -117.9079 | 17.5788 | 182.0032 | 0.0031 | 0.0159 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414262_EA5B1C98 | 504990 | 411 | -81.9 | 504990 | 412 | -81.6 | 504990 | 631 | -86.0 | 504990 | 229 |
| MR_1774414262_CF42367B | 504990 | 411 | -83.5 | 504990 | 412 | -79.4 | 504990 | 631 | -86.3 | 504990 | 229 |
| MR_1774414262_41D17F29 | 504990 | 412 | -83.0 | 504990 | 411 | -80.1 | 504990 | 631 | -87.6 | 504990 | 229 |
| MR_1774414262_5B6BEAFA | 504990 | 412 | -81.0 | 504990 | 411 | -83.1 | 504990 | 631 | -85.2 | 504990 | 229 |
| MR_1774414262_A423BE7C | 504990 | 411 | -81.0 | 504990 | 412 | -79.7 | 504990 | 631 | -87.5 | 504990 | 229 |

> *... 2개 열 생략 (전체 14열)*

---
