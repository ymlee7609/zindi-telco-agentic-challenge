# Track A 문제 분석 — train[1650]~train[1659]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1650] ~ train[1659] (10개)

## 목차

1. [문제 1650: `173728ea-56e...`](#1650) — single-answer, 정답: C3
2. [문제 1651: `396b05e3-f94...`](#1651) — multiple-answer, 정답: C11|C20
3. [문제 1652: `d8b67895-51d...`](#1652) — multiple-answer, 정답: C1|C9|C10|C17
4. [문제 1653: `55930031-86a...`](#1653) — multiple-answer, 정답: C3|C7
5. [문제 1654: `ac885f0b-9d9...`](#1654) — single-answer, 정답: C21
6. [문제 1655: `e4b87b03-d77...`](#1655) — single-answer, 정답: C8
7. [문제 1656: `265de73d-69f...`](#1656) — single-answer, 정답: C11
8. [문제 1657: `9de6f9bd-838...`](#1657) — single-answer, 정답: C22
9. [문제 1658: `aaff6a96-c83...`](#1658) — single-answer, 정답: C17
10. [문제 1659: `4a7ac1ce-8aa...`](#1659) — multiple-answer, 정답: C3|C18

---

### 문제 1650: `173728ea-56e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `173728ea-56e2-4388-a6a4-662c6b6eb5d5` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3238595_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1650] topology](images/train_1650.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3242063_3 and 3246426_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246426_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238595_1 **← 정답**
- `C4`: Decrease transmission power for 3246426_4
- `C5`: Decrease transmission power for 3238595_1
- `C6`: Press down the tilt angle  of 3246426_4 by 10 degrees
- `C7`: Check test server and transmission issues
- `C8`: Lift the tilt angle  of 3246426_4 by 10 degrees
- `C9`: Decrease A3 Offset threshold for 3238595_1
- `C10`: Increase transmission power for 3238595_1
- `C11`: Increase transmission power for 3246426_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238595_1
- `C13`: Adjust the azimuth of 3246426_4 by 50 degrees
- `C14`: Add neighbor relationship between 3238595_1 and 3246426_4
- `C15`: Press down the tilt angle of 3238595_1 by 1 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Adjust the azimuth of 3238595_1 by 16 degrees
- `C18`: Lift the tilt angle of 3238595_1 by 1 degrees
- `C19`: Increase A3 Offset threshold for 3238595_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246426_4
- `C21`: Decrease A3 Offset threshold for 3246426_4
- `C22`: Increase A3 Offset threshold for 3246426_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.235 | MS1 | 121.4656733426 | 31.1446354157 | 11 | 504990 | -91.84 | 15.89 | 357.21 | 0.01 | 2.37 | 1562 |
| 2024-09-20 22:21:32.733 | MS1 | 121.4656703922 | 31.1446234829 | 11 | 504990 | -89.11 | 15.47 | 457.01 | 0.04 | 2.90 | 1581 |
| 2024-09-20 22:21:33.342 | MS1 | 121.4656648061 | 31.1446350972 | 11 | 504990 | -90.96 | 12.07 | 339.26 | 0.09 | 2.40 | 1599 |
| 2024-09-20 22:21:34.350 | MS1 | 121.4656630073 | 31.1446312953 | 11 | 504990 | -85.88 | 17.07 | 89.94 | 0.67 | 2.23 | 688 |
| 2024-09-20 22:21:35.304 | MS1 | 121.4656608377 | 31.1446243798 | 11 | 504990 | -85.17 | 12.29 | 66.03 | 0.67 | 2.01 | 645 |
| 2024-09-20 22:21:36.764 | MS1 | 121.4656690810 | 31.1446371525 | 11 | 504990 | -88.96 | 15.65 | 65.32 | 0.60 | 2.83 | 616 |
| 2024-09-20 22:21:37.463 | MS1 | 121.4656589799 | 31.1446194030 | 11 | 504990 | -90.56 | 7.16 | 48.95 | 0.66 | 2.45 | 550 |
| 2024-09-20 22:21:38.962 | MS1 | 121.4656628113 | 31.1446197101 | 11 | 504990 | -89.66 | 11.55 | 101.78 | 0.57 | 2.22 | 627 |
| 2024-09-20 22:21:39.633 | MS1 | 121.4656779023 | 31.1446294256 | 11 | 504990 | -89.92 | 9.66 | 97.09 | 0.60 | 2.57 | 617 |
| 2024-09-20 22:21:40.215 | MS1 | 121.4656651106 | 31.1446217337 | 11 | 504990 | -91.39 | 11.40 | 594.66 | 0.07 | 2.68 | 1562 |
| 2024-09-20 22:21:41.893 | MS1 | 121.4656724728 | 31.1446254990 | 11 | 504990 | -92.73 | 11.42 | 403.32 | 0.03 | 2.87 | 1589 |
| 2024-09-20 22:21:42.619 | MS1 | 121.4656701775 | 31.1446335381 | 11 | 504990 | -90.16 | 8.99 | 549.78 | 0.19 | 2.97 | 1572 |

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
| 3238595 | 1 | 121.4734809968 | 31.1530417567 | 234 | 0 | 4 | 24.3 | TDD | 11 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3242063 | 3 | 121.4741487484 | 31.1528354326 | 206 | 2 | 11 | 27.4 | TDD | 771 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3246426 | 4 | 121.4640199966 | 31.1449195274 | 333 | 13 | 10 | 48.8 | TDD | 610 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3263636 | 2 | 121.4665259797 | 31.1446112700 | 142 | 0 | 2 | 42.8 | TDD | 162 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.299 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.318 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.424 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.424 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.123 | NREventA3 | measId:2;ServCellPCI:25;Ser... |
| 2024-09-20 22:21:38.363 | NRHandoverAttempt | SourcePCI:25;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.397 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.410 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.532 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.532 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238595 | 1 | 14.6697 | 9.8763 | -114.7920 | 15.9922 | 191.2893 | 0.0069 | 0.0036 |
| 2024_09_20 22:00 | 3263636 | 2 | 14.4160 | 8.9087 | -115.6539 | 14.5800 | 168.2159 | 0.0111 | 0.0032 |
| 2024_09_20 22:00 | 3242063 | 3 | 18.4363 | 12.3604 | -114.2150 | 17.6472 | 120.1745 | 0.0141 | 0.0005 |
| 2024_09_20 22:00 | 3246426 | 4 | 18.2491 | 6.2712 | -115.2076 | 5.8583 | 98.0358 | 0.0068 | 0.0189 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416478_47927136 | 504990 | 11 | -87.8 | 504990 | 610 | -94.8 | 504990 | 771 | -97.9 | 504990 | 162 |
| MR_1774416478_50238BBA | 504990 | 11 | -84.6 | 504990 | 610 | -94.5 | 504990 | 771 | -95.0 | 504990 | 162 |
| MR_1774416478_9380FADC | 504990 | 11 | -87.0 | 504990 | 610 | -92.9 | 504990 | 771 | -96.2 | 504990 | 162 |
| MR_1774416478_690DD90F | 504990 | 11 | -84.7 | 504990 | 610 | -94.7 | 504990 | 771 | -98.6 | 504990 | 162 |
| MR_1774416478_AB6B6CC4 | 504990 | 11 | -84.3 | 504990 | 610 | -92.0 | 504990 | 771 | -96.4 | 504990 | 162 |
| MR_1774416478_02738BE3 | 504990 | 11 | -86.3 | 504990 | 610 | -94.5 | 504990 | 771 | -95.1 | 504990 | 162 |
| MR_1774416478_1AFCE707 | 504990 | 11 | -84.3 | 504990 | 610 | -91.8 | 504990 | 771 | -95.3 | 504990 | 162 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1651: `396b05e3-f94...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `396b05e3-f946-4268-beb2-a44c4286f070` |
| Tag | **multiple-answer** |
| 정답 | **C11|C20** |
| C11 의미 | Increase transmission power for 3276259_2 |
| C20 의미 | Adjust the azimuth of 3276259_2 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1651] topology](images/train_1651.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276259_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276259_2
- `C3`: Add neighbor relationship between 3246473_1 and 3244367_4
- `C4`: Decrease A3 Offset threshold for 3244367_4
- `C5`: Press down the tilt angle  of 3244367_4 by 6 degrees
- `C6`: Check test server and transmission issues
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244367_4
- `C8`: Increase transmission power for 3244367_4
- `C9`: Lift the tilt angle  of 3244367_4 by 6 degrees
- `C10`: Add neighbor relationship between 3276259_2 and 3244367_4
- `C11`: Increase transmission power for 3276259_2 **← 정답**
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244367_4
- `C13`: Adjust the azimuth of 3244367_4 by 35 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase A3 Offset threshold for 3276259_2
- `C16`: Lift the tilt angle of 3276259_2 by 10 degrees
- `C17`: Decrease transmission power for 3244367_4
- `C18`: Decrease transmission power for 3276259_2
- `C19`: Press down the tilt angle of 3276259_2 by 10 degrees
- `C20`: Adjust the azimuth of 3276259_2 by 50 degrees **← 정답**
- `C21`: Increase A3 Offset threshold for 3244367_4
- `C22`: Decrease A3 Offset threshold for 3276259_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.369 | MS1 | 121.4656745165 | 31.1446371052 | 481 | 504990 | -91.84 | 12.49 | 448.27 | 0.08 | 2.18 | 1572 |
| 2024-09-20 22:21:32.574 | MS1 | 121.4656734664 | 31.1446236777 | 481 | 504990 | -90.49 | 12.63 | 447.46 | 0.12 | 2.80 | 1577 |
| 2024-09-20 22:21:33.294 | MS1 | 121.4656587404 | 31.1446364703 | 481 | 504990 | -93.38 | 12.30 | 476.57 | 0.08 | 2.60 | 1597 |
| 2024-09-20 22:21:34.712 | MS1 | 121.4656580022 | 31.1446360450 | 481 | 504990 | -100.52 | -0.37 | 56.83 | 0.01 | 1.11 | 1566 |
| 2024-09-20 22:21:35.677 | MS1 | 121.4656715651 | 31.1446197108 | 481 | 504990 | -107.27 | 1.50 | 30.62 | 0.03 | 1.31 | 1586 |
| 2024-09-20 22:21:36.258 | MS1 | 121.4656607208 | 31.1446290142 | 481 | 504990 | -103.64 | -1.55 | 35.66 | 0.07 | 1.03 | 1587 |
| 2024-09-20 22:21:37.752 | MS1 | 121.4656672252 | 31.1446204789 | 481 | 504990 | -106.62 | 0.16 | 47.58 | 0.19 | 1.42 | 1575 |
| 2024-09-20 22:21:38.384 | MS1 | 121.4656636440 | 31.1446288165 | 481 | 504990 | -107.36 | 1.33 | 24.47 | 0.12 | 1.14 | 1569 |
| 2024-09-20 22:21:39.427 | MS1 | 121.4656709835 | 31.1446308546 | 481 | 504990 | -106.47 | -1.47 | 37.17 | 0.17 | 1.18 | 1575 |
| 2024-09-20 22:21:40.454 | MS1 | 121.4656662786 | 31.1446276123 | 481 | 504990 | -89.54 | 13.14 | 332.26 | 0.16 | 2.31 | 1586 |
| 2024-09-20 22:21:41.674 | MS1 | 121.4656690155 | 31.1446341150 | 481 | 504990 | -86.14 | 13.81 | 421.48 | 0.02 | 2.08 | 1570 |
| 2024-09-20 22:21:42.521 | MS1 | 121.4656773416 | 31.1446289127 | 481 | 504990 | -85.60 | 14.46 | 409.42 | 0.03 | 2.36 | 1600 |

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
| 3244367 | 4 | 121.4684228870 | 31.1467445570 | 193 | 3 | 2 | 17.9 | TDD | 237 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3245574 | 3 | 121.4668172691 | 31.1525195296 | 315 | 1 | 0 | 31.1 | TDD | 659 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3246473 | 1 | 121.4759238874 | 31.1455555233 | 151 | 9 | 2 | 18.5 | TDD | 104 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3276259 | 2 | 121.4746321553 | 31.1450159034 | 330 | 10 | 8 | 35.9 | TDD | 481 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.942 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.967 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.073 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.073 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.308 | NREventA2 | measId:1;ServCellPCI:685;Se... |
| 2024-09-20 22:21:34.413 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246473 | 1 | 13.4930 | 14.3104 | -115.6366 | 6.4448 | 134.3646 | 0.0036 | 0.0056 |
| 2024_09_20 22:00 | 3276259 | 2 | 6.8817 | 10.7595 | -116.0807 | 16.9303 | 106.8101 | 0.1558 | 0.0093 |
| 2024_09_20 22:00 | 3245574 | 3 | 12.7729 | 15.3953 | -114.5077 | 18.2642 | 118.6214 | 0.0089 | 0.0073 |
| 2024_09_20 22:00 | 3244367 | 4 | 17.9871 | 5.1636 | -114.7886 | 9.9101 | 155.4081 | 0.0112 | 0.0001 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416707_368EC33D | 504990 | 481 | -101.7 | 504990 | 237 | -105.3 | 504990 | 104 | -112.9 | 504990 | 659 |
| MR_1774416707_C6C337C9 | 504990 | 481 | -102.2 | 504990 | 237 | -107.2 | 504990 | 104 | -111.9 | 504990 | 659 |
| MR_1774416707_CA8442AF | 504990 | 481 | -98.7 | 504990 | 237 | -108.6 | 504990 | 104 | -109.3 | 504990 | 659 |
| MR_1774416707_503F1324 | 504990 | 481 | -102.4 | 504990 | 237 | -105.5 | 504990 | 104 | -111.6 | 504990 | 659 |
| MR_1774416707_57C578BE | 504990 | 481 | -100.6 | 504990 | 237 | -105.1 | 504990 | 104 | -111.3 | 504990 | 659 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1652: `d8b67895-51d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d8b67895-51da-4ba1-8c1c-97dd8e61eb3a` |
| Tag | **multiple-answer** |
| 정답 | **C1|C9|C10|C17** |
| C1 의미 | Increase A3 Offset threshold for 3214973_5 |
| C9 의미 | Press down the tilt angle  of 3226846_4 by 5 degrees |
| C10 의미 | Increase A3 Offset threshold for 3226846_4 |
| C17 의미 | Decrease transmission power for 3226846_4 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1652] topology](images/train_1652.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3214973_5 **← 정답**
- `C2`: Add neighbor relationship between 3214973_5 and 3226846_4
- `C3`: Decrease A3 Offset threshold for 3214973_5
- `C4`: Increase transmission power for 3214973_5
- `C5`: Check test server and transmission issues
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214973_5
- `C7`: Lift the tilt angle of 3214973_5 by 6 degrees
- `C8`: Decrease transmission power for 3214973_5
- `C9`: Press down the tilt angle  of 3226846_4 by 5 degrees **← 정답**
- `C10`: Increase A3 Offset threshold for 3226846_4 **← 정답**
- `C11`: Add neighbor relationship between 3214351_2 and 3226846_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226846_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226846_4
- `C14`: Press down the tilt angle of 3214973_5 by 6 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Lift the tilt angle  of 3226846_4 by 5 degrees
- `C17`: Decrease transmission power for 3226846_4 **← 정답**
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214973_5
- `C19`: Adjust the azimuth of 3214973_5 by 35 degrees
- `C20`: Increase transmission power for 3226846_4
- `C21`: Adjust the azimuth of 3226846_4 by 34 degrees
- `C22`: Decrease A3 Offset threshold for 3226846_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.709 | MS1 | 121.4656584620 | 31.1446348029 | 989 | 504990 | -77.81 | 17.93 | 537.64 | 0.14 | 2.65 | 1575 |
| 2024-09-20 22:21:32.966 | MS1 | 121.4656662686 | 31.1446185773 | 989 | 504990 | -84.96 | 13.16 | 533.32 | 0.03 | 2.27 | 1561 |
| 2024-09-20 22:21:33.479 | MS1 | 121.4656628514 | 31.1446248582 | 989 | 504990 | -83.47 | 12.08 | 512.03 | 0.04 | 2.37 | 1599 |
| 2024-09-20 22:21:34.694 | MS1 | 121.4656717495 | 31.1446187011 | 643 | 504990 | -83.98 | 2.46 | 62.32 | 0.10 | 1.23 | 1569 |
| 2024-09-20 22:21:35.754 | MS1 | 121.4656705497 | 31.1446199711 | 643 | 504990 | -88.13 | 1.75 | 38.84 | 0.04 | 1.33 | 1594 |
| 2024-09-20 22:21:36.897 | MS1 | 121.4656737975 | 31.1446255681 | 989 | 504990 | -81.24 | 2.09 | 55.38 | 0.19 | 1.28 | 1593 |
| 2024-09-20 22:21:37.978 | MS1 | 121.4656602402 | 31.1446209074 | 989 | 504990 | -88.42 | 2.30 | 53.47 | 0.12 | 1.45 | 1571 |
| 2024-09-20 22:21:38.955 | MS1 | 121.4656724787 | 31.1446194670 | 643 | 504990 | -89.09 | 1.09 | 81.61 | 0.20 | 1.27 | 1578 |
| 2024-09-20 22:21:39.734 | MS1 | 121.4656673559 | 31.1446378480 | 643 | 504990 | -80.31 | 4.51 | 49.67 | 0.05 | 1.42 | 1594 |
| 2024-09-20 22:21:40.799 | MS1 | 121.4656719115 | 31.1446230720 | 643 | 504990 | -83.28 | 13.33 | 459.24 | 0.18 | 2.35 | 1579 |
| 2024-09-20 22:21:41.253 | MS1 | 121.4656654098 | 31.1446221596 | 643 | 504990 | -82.91 | 12.11 | 395.59 | 0.18 | 2.13 | 1577 |
| 2024-09-20 22:21:42.648 | MS1 | 121.4656632128 | 31.1446374266 | 643 | 504990 | -78.85 | 13.09 | 525.97 | 0.14 | 2.23 | 1592 |

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
| 3214351 | 2 | 121.4662293511 | 31.1471296548 | 17 | 5 | 5 | 28.1 | TDD | 817 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3214973 | 5 | 121.4676614699 | 31.1463759483 | 189 | 0 | 10 | 28.2 | TDD | 989 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3226846 | 4 | 121.4688119461 | 31.1519190963 | 166 | 3 | 6 | 26.2 | TDD | 218 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3235065 | 3 | 121.4671515456 | 31.1499370550 | 199 | 10 | 5 | 36.3 | TDD | 121 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3259127 | 1 | 121.4665450607 | 31.1559049866 | 302 | 0 | 10 | 33.0 | TDD | 643 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.095 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.111 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.231 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.231 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.901 | NREventA3 | measId:2;ServCellPCI:427;Se... |
| 2024-09-20 22:21:34.141 | NRHandoverAttempt | SourcePCI:427;SourceNR-ARFC... |
| 2024-09-20 22:21:34.177 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.187 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:34.298 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.298 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.901 | NREventA3 | measId:2;ServCellPCI:441;Se... |
| 2024-09-20 22:21:36.141 | NRHandoverAttempt | SourcePCI:441;SourceNR-ARFC... |
| 2024-09-20 22:21:36.171 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.185 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.329 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.329 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.901 | NREventA3 | measId:2;ServCellPCI:427;Se... |
| 2024-09-20 22:21:38.141 | NRHandoverAttempt | SourcePCI:427;SourceNR-ARFC... |
| 2024-09-20 22:21:38.175 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.189 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.303 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.303 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259127 | 1 | 19.4173 | 6.8499 | -117.6683 | 11.9141 | 191.0619 | 0.0111 | 0.0091 |
| 2024_09_20 22:00 | 3214351 | 2 | 15.9377 | 12.4259 | -115.0169 | 10.6266 | 108.8080 | 0.0008 | 0.0028 |
| 2024_09_20 22:00 | 3235065 | 3 | 6.2829 | 16.1437 | -115.1517 | 17.9042 | 94.7735 | 0.0188 | 0.0044 |
| 2024_09_20 22:00 | 3226846 | 4 | 13.6580 | 9.5567 | -114.0118 | 8.4400 | 108.1860 | 0.0141 | 0.0114 |
| 2024_09_20 22:00 | 3214973 | 5 | 18.3868 | 10.8848 | -116.0097 | 17.6458 | 98.1045 | 0.0090 | 0.0154 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415932_FA30ABB0 | 504990 | 989 | -84.9 | 504990 | 643 | -83.9 | 504990 | 218 | -87.7 | 504990 | 817 |
| MR_1774415932_C95E93B2 | 504990 | 643 | -85.9 | 504990 | 989 | -84.9 | 504990 | 218 | -86.5 | 504990 | 817 |
| MR_1774415932_2C2FE607 | 504990 | 989 | -82.8 | 504990 | 643 | -83.9 | 504990 | 218 | -86.7 | 504990 | 817 |
| MR_1774415932_EF2176EF | 504990 | 989 | -84.9 | 504990 | 643 | -84.2 | 504990 | 218 | -87.5 | 504990 | 817 |
| MR_1774415932_73E209F3 | 504990 | 643 | -85.8 | 504990 | 989 | -84.1 | 504990 | 218 | -84.3 | 504990 | 817 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1653: `55930031-86a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `55930031-86ae-43e6-bea4-38a3146b4b0b` |
| Tag | **multiple-answer** |
| 정답 | **C3|C7** |
| C3 의미 | Decrease transmission power for 3228555_1 |
| C7 의미 | Press down the tilt angle  of 3228555_1 by 5 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1653] topology](images/train_1653.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3264649_4 by 6 degrees
- `C2`: Press down the tilt angle of 3264649_4 by 6 degrees
- `C3`: Decrease transmission power for 3228555_1 **← 정답**
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264649_4
- `C5`: Adjust the azimuth of 3228555_1 by 0 degrees
- `C6`: Decrease A3 Offset threshold for 3264649_4
- `C7`: Press down the tilt angle  of 3228555_1 by 5 degrees **← 정답**
- `C8`: Add neighbor relationship between 3273983_2 and 3228555_1
- `C9`: Increase A3 Offset threshold for 3264649_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228555_1
- `C11`: Decrease A3 Offset threshold for 3228555_1
- `C12`: Increase transmission power for 3264649_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228555_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Check test server and transmission issues
- `C16`: Add neighbor relationship between 3264649_4 and 3228555_1
- `C17`: Decrease transmission power for 3264649_4
- `C18`: Increase A3 Offset threshold for 3228555_1
- `C19`: Increase transmission power for 3228555_1
- `C20`: Lift the tilt angle  of 3228555_1 by 5 degrees
- `C21`: Adjust the azimuth of 3264649_4 by 15 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264649_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.594 | MS1 | 121.4656636986 | 31.1446191616 | 758 | 504990 | -81.23 | 13.07 | 335.90 | 0.09 | 2.50 | 1595 |
| 2024-09-20 22:21:32.249 | MS1 | 121.4656714433 | 31.1446263519 | 758 | 504990 | -81.23 | 12.39 | 575.77 | 0.02 | 2.11 | 1588 |
| 2024-09-20 22:21:33.105 | MS1 | 121.4656694146 | 31.1446308993 | 758 | 504990 | -79.45 | 16.75 | 388.20 | 0.15 | 2.97 | 1567 |
| 2024-09-20 22:21:34.799 | MS1 | 121.4656678707 | 31.1446305079 | 758 | 504990 | -92.93 | 3.37 | 73.34 | 0.12 | 1.42 | 1588 |
| 2024-09-20 22:21:35.523 | MS1 | 121.4656626858 | 31.1446225245 | 758 | 504990 | -93.95 | 2.88 | 74.31 | 0.02 | 1.17 | 1570 |
| 2024-09-20 22:21:36.598 | MS1 | 121.4656770889 | 31.1446317299 | 758 | 504990 | -93.37 | 3.21 | 46.44 | 0.14 | 1.44 | 1592 |
| 2024-09-20 22:21:37.675 | MS1 | 121.4656769320 | 31.1446329417 | 758 | 504990 | -86.19 | 0.80 | 44.10 | 0.05 | 1.23 | 1587 |
| 2024-09-20 22:21:38.725 | MS1 | 121.4656774330 | 31.1446221804 | 758 | 504990 | -94.84 | 3.81 | 62.03 | 0.09 | 1.02 | 1586 |
| 2024-09-20 22:21:39.258 | MS1 | 121.4656585886 | 31.1446311590 | 758 | 504990 | -94.36 | 2.74 | 90.04 | 0.17 | 1.49 | 1586 |
| 2024-09-20 22:21:40.374 | MS1 | 121.4656693437 | 31.1446229128 | 758 | 504990 | -83.50 | 17.97 | 524.81 | 0.01 | 2.27 | 1584 |
| 2024-09-20 22:21:41.517 | MS1 | 121.4656614947 | 31.1446347760 | 758 | 504990 | -77.80 | 13.85 | 410.76 | 0.04 | 2.05 | 1598 |
| 2024-09-20 22:21:42.935 | MS1 | 121.4656598838 | 31.1446219227 | 758 | 504990 | -84.75 | 15.26 | 340.80 | 0.01 | 2.58 | 1581 |

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
| 3212563 | 3 | 121.4705384030 | 31.1466718430 | 355 | 13 | 12 | 47.5 | TDD | 134 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3228555 | 1 | 121.4684973311 | 31.1471699982 | 224 | 0 | 0 | 33.4 | TDD | 920 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3264649 | 4 | 121.4740444914 | 31.1484693638 | 227 | 4 | 4 | 25.9 | TDD | 758 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3273983 | 2 | 121.4758786370 | 31.1550330447 | 135 | 10 | 2 | 31.3 | TDD | 115 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.413 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.432 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.545 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.545 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228555 | 1 | 10.4982 | 8.0150 | -115.0626 | 15.3826 | 186.1932 | 0.0136 | 0.0165 |
| 2024_09_20 22:00 | 3273983 | 2 | 12.1366 | 9.4940 | -115.0013 | 11.0975 | 190.5311 | 0.0132 | 0.0100 |
| 2024_09_20 22:00 | 3212563 | 3 | 8.1691 | 19.1379 | -116.1872 | 13.5657 | 86.3838 | 0.0019 | 0.0065 |
| 2024_09_20 22:00 | 3264649 | 4 | 11.8345 | 18.1103 | -108.5686 | 11.5527 | 127.8346 | 0.0129 | 0.0157 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415760_6D71D5F5 | 504990 | 758 | -92.3 | 504990 | 920 | -92.0 | 504990 | 115 | -93.3 | 504990 | 134 |
| MR_1774415760_DB1A03EA | 504990 | 758 | -91.4 | 504990 | 920 | -91.6 | 504990 | 115 | -90.5 | 504990 | 134 |
| MR_1774415760_6CADC1EB | 504990 | 758 | -92.0 | 504990 | 920 | -92.3 | 504990 | 115 | -92.1 | 504990 | 134 |
| MR_1774415760_73F653E4 | 504990 | 920 | -91.2 | 504990 | 758 | -89.7 | 504990 | 115 | -93.2 | 504990 | 134 |
| MR_1774415760_20CEC4A3 | 504990 | 758 | -91.9 | 504990 | 920 | -89.3 | 504990 | 115 | -90.9 | 504990 | 134 |
| MR_1774415760_95A51914 | 504990 | 920 | -92.4 | 504990 | 758 | -90.3 | 504990 | 115 | -91.8 | 504990 | 134 |
| MR_1774415760_E86B489C | 504990 | 758 | -93.2 | 504990 | 920 | -91.6 | 504990 | 115 | -91.1 | 504990 | 134 |
| MR_1774415760_C1A32692 | 504990 | 758 | -93.0 | 504990 | 920 | -89.3 | 504990 | 115 | -90.7 | 504990 | 134 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1654: `ac885f0b-9d9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ac885f0b-9d9c-4347-9b2f-7df22382e982` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease A3 Offset threshold for 3256658_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1654] topology](images/train_1654.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224571_1
- `C2`: Adjust the azimuth of 3256658_2 by 50 degrees
- `C3`: Add neighbor relationship between 3260665_4 and 3224571_1
- `C4`: Lift the tilt angle  of 3224571_1 by 10 degrees
- `C5`: Increase A3 Offset threshold for 3224571_1
- `C6`: Increase transmission power for 3256658_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Add neighbor relationship between 3256658_2 and 3224571_1
- `C9`: Increase transmission power for 3224571_1
- `C10`: Increase A3 Offset threshold for 3256658_2
- `C11`: Check test server and transmission issues
- `C12`: Decrease A3 Offset threshold for 3224571_1
- `C13`: Decrease transmission power for 3224571_1
- `C14`: Adjust the azimuth of 3224571_1 by 50 degrees
- `C15`: Lift the tilt angle of 3256658_2 by 10 degrees
- `C16`: Press down the tilt angle  of 3224571_1 by 10 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256658_2
- `C18`: Press down the tilt angle of 3256658_2 by 10 degrees
- `C19`: Decrease transmission power for 3256658_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224571_1
- `C21`: Decrease A3 Offset threshold for 3256658_2 **← 정답**
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256658_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.129 | MS1 | 121.4656647003 | 31.1446352358 | 1005 | 504990 | -79.70 | 14.08 | 438.64 | 0.05 | 2.30 | 1574 |
| 2024-09-20 22:21:32.730 | MS1 | 121.4656622687 | 31.1446366699 | 1005 | 504990 | -78.02 | 14.21 | 401.08 | 0.02 | 2.15 | 1576 |
| 2024-09-20 22:21:33.946 | MS1 | 121.4656683911 | 31.1446288679 | 1005 | 504990 | -75.35 | 16.02 | 415.35 | 0.00 | 2.12 | 1581 |
| 2024-09-20 22:21:34.520 | MS1 | 121.4656609969 | 31.1446302482 | 1005 | 504990 | -84.28 | -3.09 | 60.11 | 0.12 | 1.41 | 1598 |
| 2024-09-20 22:21:35.501 | MS1 | 121.4656747524 | 31.1446273056 | 1005 | 504990 | -87.91 | -1.60 | 57.57 | 0.16 | 1.29 | 1579 |
| 2024-09-20 22:21:36.211 | MS1 | 121.4656748071 | 31.1446283908 | 1005 | 504990 | -92.57 | -3.91 | 58.46 | 0.03 | 1.48 | 1597 |
| 2024-09-20 22:21:37.324 | MS1 | 121.4656707057 | 31.1446199947 | 1005 | 504990 | -88.20 | -1.57 | 55.70 | 0.10 | 1.06 | 1563 |
| 2024-09-20 22:21:38.658 | MS1 | 121.4656694896 | 31.1446296924 | 1005 | 504990 | -91.17 | -2.89 | 64.31 | 0.06 | 1.03 | 1584 |
| 2024-09-20 22:21:39.981 | MS1 | 121.4656658152 | 31.1446210171 | 120 | 504990 | -81.83 | 16.42 | 236.24 | 0.08 | 1.30 | 1563 |
| 2024-09-20 22:21:40.780 | MS1 | 121.4656711207 | 31.1446214113 | 120 | 504990 | -82.93 | 15.62 | 484.57 | 0.16 | 2.44 | 1577 |
| 2024-09-20 22:21:41.165 | MS1 | 121.4656770238 | 31.1446277126 | 120 | 504990 | -84.81 | 16.91 | 599.09 | 0.18 | 2.06 | 1600 |
| 2024-09-20 22:21:42.142 | MS1 | 121.4656666209 | 31.1446331767 | 120 | 504990 | -82.51 | 13.28 | 411.40 | 0.00 | 2.21 | 1588 |

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
| 3224571 | 1 | 121.4651715156 | 31.1469445185 | 77 | 11 | 4 | 24.2 | TDD | 120 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3256658 | 2 | 121.4654872039 | 31.1470226933 | 9 | 6 | 4 | 26.1 | TDD | 1005 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3260665 | 4 | 121.4700351624 | 31.1538032677 | 266 | 3 | 12 | 26.4 | TDD | 293 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3276860 | 3 | 121.4682028846 | 31.1556404573 | 280 | 9 | 5 | 26.7 | TDD | 43 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.336 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.355 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.483 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.483 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.143 | NREventA3 | measId:2;ServCellPCI:788;Se... |
| 2024-09-20 22:21:38.383 | NRHandoverAttempt | SourcePCI:788;SourceNR-ARFC... |
| 2024-09-20 22:21:38.416 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.428 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.544 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.544 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224571 | 1 | 6.2059 | 12.5723 | -116.8202 | 5.9855 | 119.4816 | 0.0129 | 0.0079 |
| 2024_09_20 22:00 | 3256658 | 2 | 19.7082 | 16.3898 | -117.3859 | 17.3055 | 83.7803 | 0.0151 | 0.1486 |
| 2024_09_20 22:00 | 3276860 | 3 | 13.9434 | 12.4617 | -115.9008 | 19.3467 | 117.6726 | 0.0045 | 0.0037 |
| 2024_09_20 22:00 | 3260665 | 4 | 6.7083 | 19.4231 | -116.8576 | 18.0682 | 183.9522 | 0.0005 | 0.0031 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413834_9A2321A7 | 504990 | 120 | -78.9 | 504990 | 1005 | -83.5 | 504990 | 293 | -80.9 | 504990 | 43 |
| MR_1774413834_908DAEAF | 504990 | 1005 | -83.8 | 504990 | 120 | -79.4 | 504990 | 293 | -80.1 | 504990 | 43 |
| MR_1774413834_06D10DC2 | 504990 | 120 | -78.4 | 504990 | 1005 | -85.1 | 504990 | 293 | -80.4 | 504990 | 43 |
| MR_1774413834_BCA15CD2 | 504990 | 120 | -79.9 | 504990 | 1005 | -83.5 | 504990 | 293 | -80.8 | 504990 | 43 |
| MR_1774413834_5BBB34C4 | 504990 | 1005 | -82.9 | 504990 | 120 | -78.1 | 504990 | 293 | -81.0 | 504990 | 43 |
| MR_1774413834_90478C93 | 504990 | 120 | -78.2 | 504990 | 1005 | -82.8 | 504990 | 293 | -81.4 | 504990 | 43 |
| MR_1774413834_1A2C431F | 504990 | 120 | -77.1 | 504990 | 1005 | -85.6 | 504990 | 293 | -79.3 | 504990 | 43 |
| MR_1774413834_66749AE4 | 504990 | 120 | -77.2 | 504990 | 1005 | -82.5 | 504990 | 293 | -81.5 | 504990 | 43 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1655: `e4b87b03-d77...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e4b87b03-d77f-45e7-bc88-e51addd2b6f4` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3218399_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1655] topology](images/train_1655.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3218399_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Check test server and transmission issues
- `C4`: Adjust the azimuth of 3256194_1 by 50 degrees
- `C5`: Press down the tilt angle of 3218399_2 by 4 degrees
- `C6`: Decrease A3 Offset threshold for 3218399_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256194_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218399_2 **← 정답**
- `C9`: Press down the tilt angle  of 3256194_1 by 7 degrees
- `C10`: Decrease transmission power for 3256194_1
- `C11`: Increase transmission power for 3218399_2
- `C12`: Increase A3 Offset threshold for 3218399_2
- `C13`: Add neighbor relationship between 3211882_4 and 3256194_1
- `C14`: Adjust the azimuth of 3218399_2 by 32 degrees
- `C15`: Decrease A3 Offset threshold for 3256194_1
- `C16`: Lift the tilt angle  of 3256194_1 by 7 degrees
- `C17`: Add neighbor relationship between 3218399_2 and 3256194_1
- `C18`: Increase A3 Offset threshold for 3256194_1
- `C19`: Increase transmission power for 3256194_1
- `C20`: Lift the tilt angle of 3218399_2 by 4 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256194_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218399_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.935 | MS1 | 121.4656682570 | 31.1446363877 | 346 | 504990 | -88.94 | 15.28 | 317.77 | 0.14 | 2.34 | 1563 |
| 2024-09-20 22:21:32.169 | MS1 | 121.4656688404 | 31.1446334180 | 346 | 504990 | -87.76 | 14.67 | 336.73 | 0.20 | 2.90 | 1570 |
| 2024-09-20 22:21:33.599 | MS1 | 121.4656656998 | 31.1446366788 | 346 | 504990 | -89.41 | 13.21 | 387.76 | 0.01 | 2.72 | 1592 |
| 2024-09-20 22:21:34.689 | MS1 | 121.4656673375 | 31.1446191450 | 346 | 504990 | -87.83 | 15.13 | 99.85 | 0.54 | 2.05 | 615 |
| 2024-09-20 22:21:35.996 | MS1 | 121.4656763933 | 31.1446207747 | 346 | 504990 | -89.39 | 14.83 | 105.96 | 0.53 | 2.40 | 521 |
| 2024-09-20 22:21:36.241 | MS1 | 121.4656658470 | 31.1446272040 | 346 | 504990 | -85.92 | 14.39 | 75.60 | 0.61 | 2.41 | 570 |
| 2024-09-20 22:21:37.779 | MS1 | 121.4656748813 | 31.1446213272 | 346 | 504990 | -92.73 | 11.57 | 101.02 | 0.55 | 2.41 | 598 |
| 2024-09-20 22:21:38.634 | MS1 | 121.4656773078 | 31.1446362545 | 346 | 504990 | -93.06 | 11.18 | 42.96 | 0.51 | 2.08 | 672 |
| 2024-09-20 22:21:39.567 | MS1 | 121.4656601972 | 31.1446207579 | 346 | 504990 | -89.66 | 7.01 | 71.42 | 0.53 | 2.74 | 633 |
| 2024-09-20 22:21:40.530 | MS1 | 121.4656648066 | 31.1446325718 | 346 | 504990 | -93.67 | 12.86 | 437.72 | 0.07 | 2.98 | 1573 |
| 2024-09-20 22:21:41.756 | MS1 | 121.4656708552 | 31.1446373181 | 346 | 504990 | -90.78 | 12.79 | 502.44 | 0.18 | 2.10 | 1563 |
| 2024-09-20 22:21:42.425 | MS1 | 121.4656702947 | 31.1446207087 | 346 | 504990 | -90.65 | 12.06 | 567.77 | 0.09 | 2.11 | 1560 |

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
| 3211882 | 4 | 121.4722373300 | 31.1461265373 | 73 | 15 | 7 | 48.5 | TDD | 885 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3218399 | 2 | 121.4740243600 | 31.1496411202 | 267 | 2 | 5 | 36.0 | TDD | 346 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3225206 | 3 | 121.4756094695 | 31.1443038298 | 265 | 4 | 2 | 26.1 | TDD | 779 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3256194 | 1 | 121.4666592397 | 31.1521359680 | 96 | 4 | 2 | 45.7 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.458 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.477 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.616 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.616 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.319 | NREventA3 | measId:2;ServCellPCI:691;Se... |
| 2024-09-20 22:21:38.559 | NRHandoverAttempt | SourcePCI:691;SourceNR-ARFC... |
| 2024-09-20 22:21:38.608 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.621 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.756 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.756 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256194 | 1 | 16.9150 | 11.9520 | -116.7550 | 13.3892 | 164.2853 | 0.0012 | 0.0196 |
| 2024_09_20 22:00 | 3218399 | 2 | 5.7720 | 10.7819 | -114.3405 | 15.9637 | 127.2077 | 0.0050 | 0.0020 |
| 2024_09_20 22:00 | 3225206 | 3 | 17.4921 | 15.8862 | -116.3568 | 9.3271 | 163.5496 | 0.0129 | 0.0005 |
| 2024_09_20 22:00 | 3211882 | 4 | 15.8432 | 15.1665 | -115.6546 | 9.0897 | 131.7835 | 0.0158 | 0.0167 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414407_AB2E15A2 | 504990 | 346 | -87.5 | 504990 | 258 | -91.5 | 504990 | 885 | -95.3 | 504990 | 779 |
| MR_1774414407_21022111 | 504990 | 346 | -87.3 | 504990 | 258 | -89.0 | 504990 | 885 | -95.6 | 504990 | 779 |
| MR_1774414407_7822839E | 504990 | 346 | -87.0 | 504990 | 258 | -91.5 | 504990 | 885 | -96.5 | 504990 | 779 |
| MR_1774414407_94A3163A | 504990 | 346 | -88.6 | 504990 | 258 | -89.7 | 504990 | 885 | -97.0 | 504990 | 779 |
| MR_1774414407_0884BF58 | 504990 | 346 | -85.9 | 504990 | 258 | -90.4 | 504990 | 885 | -96.1 | 504990 | 779 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1656: `265de73d-69f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `265de73d-69fb-490d-969d-d6108f7f021c` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease A3 Offset threshold for 3252070_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1656] topology](images/train_1656.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3239021_1
- `C2`: Increase A3 Offset threshold for 3239021_1
- `C3`: Add neighbor relationship between 3252070_2 and 3239021_1
- `C4`: Decrease transmission power for 3239021_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252070_2
- `C6`: Press down the tilt angle  of 3239021_1 by 6 degrees
- `C7`: Check test server and transmission issues
- `C8`: Increase A3 Offset threshold for 3252070_2
- `C9`: Decrease transmission power for 3252070_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease A3 Offset threshold for 3252070_2 **← 정답**
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239021_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239021_1
- `C14`: Press down the tilt angle of 3252070_2 by 3 degrees
- `C15`: Add neighbor relationship between 3273045_3 and 3239021_1
- `C16`: Lift the tilt angle  of 3239021_1 by 6 degrees
- `C17`: Increase transmission power for 3252070_2
- `C18`: Adjust the azimuth of 3239021_1 by 26 degrees
- `C19`: Lift the tilt angle of 3252070_2 by 3 degrees
- `C20`: Increase transmission power for 3239021_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252070_2
- `C22`: Adjust the azimuth of 3252070_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.710 | MS1 | 121.4656627544 | 31.1446256738 | 523 | 504990 | -81.23 | 16.10 | 533.90 | 0.01 | 2.58 | 1600 |
| 2024-09-20 22:21:32.589 | MS1 | 121.4656709276 | 31.1446308126 | 523 | 504990 | -79.74 | 16.76 | 478.70 | 0.11 | 2.45 | 1587 |
| 2024-09-20 22:21:33.696 | MS1 | 121.4656765622 | 31.1446357238 | 523 | 504990 | -82.50 | 12.87 | 559.77 | 0.10 | 2.98 | 1580 |
| 2024-09-20 22:21:34.979 | MS1 | 121.4656721637 | 31.1446287236 | 523 | 504990 | -91.30 | -3.30 | 67.38 | 0.13 | 1.04 | 1564 |
| 2024-09-20 22:21:35.891 | MS1 | 121.4656581444 | 31.1446230284 | 523 | 504990 | -89.94 | -2.10 | 59.73 | 0.17 | 1.16 | 1593 |
| 2024-09-20 22:21:36.704 | MS1 | 121.4656687127 | 31.1446261722 | 523 | 504990 | -91.08 | -0.71 | 50.05 | 0.19 | 1.04 | 1572 |
| 2024-09-20 22:21:37.927 | MS1 | 121.4656594585 | 31.1446193610 | 523 | 504990 | -86.59 | -0.94 | 30.82 | 0.17 | 1.08 | 1582 |
| 2024-09-20 22:21:38.656 | MS1 | 121.4656642322 | 31.1446215109 | 523 | 504990 | -85.14 | -3.05 | 62.84 | 0.17 | 1.20 | 1583 |
| 2024-09-20 22:21:39.461 | MS1 | 121.4656634562 | 31.1446281517 | 72 | 504990 | -77.67 | 13.99 | 264.54 | 0.07 | 1.44 | 1586 |
| 2024-09-20 22:21:40.739 | MS1 | 121.4656760324 | 31.1446308143 | 72 | 504990 | -75.74 | 15.05 | 315.73 | 0.04 | 2.93 | 1564 |
| 2024-09-20 22:21:41.265 | MS1 | 121.4656693416 | 31.1446256398 | 72 | 504990 | -79.40 | 15.06 | 453.80 | 0.11 | 2.89 | 1584 |
| 2024-09-20 22:21:42.361 | MS1 | 121.4656679494 | 31.1446223114 | 72 | 504990 | -75.21 | 16.50 | 390.96 | 0.19 | 2.47 | 1594 |

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
| 3221325 | 4 | 121.4694141624 | 31.1553718305 | 326 | 10 | 9 | 16.2 | TDD | 463 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3239021 | 1 | 121.4684131021 | 31.1483972562 | 186 | 1 | 7 | 47.4 | TDD | 72 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3252070 | 2 | 121.4660154758 | 31.1476237479 | 336 | 0 | 7 | 16.1 | TDD | 523 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3273045 | 3 | 121.4712758467 | 31.1479894461 | 126 | 1 | 1 | 49.8 | TDD | 639 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.934 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.952 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.073 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.073 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.816 | NREventA3 | measId:2;ServCellPCI:481;Se... |
| 2024-09-20 22:21:38.056 | NRHandoverAttempt | SourcePCI:481;SourceNR-ARFC... |
| 2024-09-20 22:21:38.090 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.101 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.201 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.201 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239021 | 1 | 15.4748 | 15.8550 | -117.9950 | 16.3990 | 155.5436 | 0.0067 | 0.0199 |
| 2024_09_20 22:00 | 3252070 | 2 | 14.6342 | 5.8497 | -115.5985 | 18.0383 | 139.8415 | 0.0103 | 0.1977 |
| 2024_09_20 22:00 | 3273045 | 3 | 15.0097 | 17.9969 | -115.5321 | 10.6419 | 100.7608 | 0.0024 | 0.0136 |
| 2024_09_20 22:00 | 3221325 | 4 | 12.2848 | 17.7409 | -116.0575 | 7.2323 | 80.6485 | 0.0030 | 0.0020 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413270_2FC96FEB | 504990 | 72 | -85.0 | 504990 | 523 | -91.9 | 504990 | 639 | -87.9 | 504990 | 463 |
| MR_1774413270_F4C62921 | 504990 | 72 | -83.2 | 504990 | 523 | -89.4 | 504990 | 639 | -86.5 | 504990 | 463 |
| MR_1774413270_EA642D22 | 504990 | 72 | -84.9 | 504990 | 523 | -91.9 | 504990 | 639 | -86.4 | 504990 | 463 |
| MR_1774413270_8C4ACD84 | 504990 | 523 | -90.3 | 504990 | 72 | -83.3 | 504990 | 639 | -87.7 | 504990 | 463 |
| MR_1774413270_CF6590FF | 504990 | 523 | -90.2 | 504990 | 72 | -82.7 | 504990 | 639 | -85.5 | 504990 | 463 |
| MR_1774413270_CA841D50 | 504990 | 523 | -92.2 | 504990 | 72 | -83.3 | 504990 | 639 | -89.3 | 504990 | 463 |
| MR_1774413270_4CF83A5C | 504990 | 72 | -84.8 | 504990 | 523 | -93.3 | 504990 | 639 | -88.3 | 504990 | 463 |
| MR_1774413270_68D25065 | 504990 | 72 | -85.0 | 504990 | 523 | -90.2 | 504990 | 639 | -88.7 | 504990 | 463 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1657: `9de6f9bd-838...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9de6f9bd-838e-4926-97be-386a000e0aee` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Lift the tilt angle  of 3241218_1 by 4 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1657] topology](images/train_1657.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3241218_1 by 50 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Check test server and transmission issues
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241445_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276760_4
- `C6`: Add neighbor relationship between 3241445_2 and 3276760_4
- `C7`: Increase A3 Offset threshold for 3241445_2
- `C8`: Decrease A3 Offset threshold for 3276760_4
- `C9`: Increase transmission power for 3241445_2
- `C10`: Decrease A3 Offset threshold for 3241445_2
- `C11`: Increase transmission power for 3276760_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276760_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241445_2
- `C14`: Increase A3 Offset threshold for 3276760_4
- `C15`: Decrease transmission power for 3276760_4
- `C16`: Press down the tilt angle  of 3241218_1 by 4 degrees
- `C17`: Lift the tilt angle of 3241445_2 by 3 degrees
- `C18`: Decrease transmission power for 3241445_2
- `C19`: Adjust the azimuth of 3241445_2 by 11 degrees
- `C20`: Add neighbor relationship between 3241218_1 and 3276760_4
- `C21`: Press down the tilt angle of 3241445_2 by 3 degrees
- `C22`: Lift the tilt angle  of 3241218_1 by 4 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.706 | MS1 | 121.4656646305 | 31.1446261482 | 242 | 504990 | -86.06 | 17.25 | 490.40 | 0.04 | 2.81 | 1572 |
| 2024-09-20 22:21:32.416 | MS1 | 121.4656634210 | 31.1446355828 | 242 | 504990 | -90.32 | 14.26 | 407.44 | 0.04 | 2.65 | 1566 |
| 2024-09-20 22:21:33.712 | MS1 | 121.4656733932 | 31.1446370701 | 242 | 504990 | -85.33 | 17.53 | 554.03 | 0.19 | 2.92 | 1581 |
| 2024-09-20 22:21:34.794 | MS1 | 121.4656634533 | 31.1446287508 | 242 | 504990 | -88.10 | 12.13 | 86.84 | 0.02 | 2.03 | 1569 |
| 2024-09-20 22:21:35.677 | MS1 | 121.4656731388 | 31.1446185952 | 242 | 504990 | -87.39 | 16.06 | 68.23 | 0.06 | 2.65 | 1598 |
| 2024-09-20 22:21:36.590 | MS1 | 121.4656686871 | 31.1446279640 | 242 | 504990 | -86.65 | 16.53 | 68.07 | 0.19 | 2.39 | 1591 |
| 2024-09-20 22:21:37.919 | MS1 | 121.4656713789 | 31.1446260150 | 242 | 504990 | -90.90 | 7.73 | 103.30 | 0.01 | 2.92 | 1563 |
| 2024-09-20 22:21:38.573 | MS1 | 121.4656687678 | 31.1446340321 | 242 | 504990 | -89.67 | 11.33 | 70.48 | 0.13 | 2.53 | 1588 |
| 2024-09-20 22:21:39.517 | MS1 | 121.4656719912 | 31.1446297182 | 242 | 504990 | -93.23 | 12.78 | 52.51 | 0.19 | 2.90 | 1590 |
| 2024-09-20 22:21:40.566 | MS1 | 121.4656726291 | 31.1446207503 | 242 | 504990 | -91.99 | 8.02 | 341.66 | 0.18 | 2.15 | 1594 |
| 2024-09-20 22:21:41.429 | MS1 | 121.4656656483 | 31.1446371561 | 242 | 504990 | -89.59 | 12.48 | 576.72 | 0.19 | 2.90 | 1594 |
| 2024-09-20 22:21:42.571 | MS1 | 121.4656631120 | 31.1446369058 | 242 | 504990 | -90.30 | 8.08 | 370.86 | 0.04 | 2.60 | 1600 |

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
| 3227222 | 3 | 121.4738595981 | 31.1440391163 | 142 | 1 | 8 | 47.3 | TDD | 667 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3241218 | 1 | 121.4648681001 | 31.1473051298 | 49 | 10 | 9 | 34.1 | TDD | 977 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3241445 | 2 | 121.4747112789 | 31.1489115136 | 252 | 0 | 8 | 48.8 | TDD | 242 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3276760 | 4 | 121.4730069832 | 31.1494360523 | 164 | 3 | 7 | 16.9 | TDD | 917 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.227 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.243 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.350 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.350 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.042 | NREventA3 | measId:2;ServCellPCI:196;Se... |
| 2024-09-20 22:21:38.282 | NRHandoverAttempt | SourcePCI:196;SourceNR-ARFC... |
| 2024-09-20 22:21:38.323 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.336 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.439 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.439 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241218 | 1 | 7.1616 | 18.7240 | -117.8249 | 8.2730 | 156.2846 | 0.0164 | 0.0084 |
| 2024_09_20 22:00 | 3241445 | 2 | 91.9410 | 86.0832 | -115.3789 | 9.0733 | 145.2271 | 0.0198 | 0.0017 |
| 2024_09_20 22:00 | 3227222 | 3 | 16.3525 | 7.1038 | -117.5859 | 5.0141 | 196.1567 | 0.0117 | 0.0085 |
| 2024_09_20 22:00 | 3276760 | 4 | 13.6833 | 10.5000 | -115.9907 | 10.1042 | 185.3154 | 0.0129 | 0.0146 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413560_7B0C1E75 | 504990 | 242 | -89.4 | 504990 | 917 | -94.2 | 504990 | 977 | -95.6 | 504990 | 667 |
| MR_1774413560_BE57DC3E | 504990 | 242 | -88.8 | 504990 | 917 | -93.0 | 504990 | 977 | -95.1 | 504990 | 667 |
| MR_1774413560_D5FA1E0A | 504990 | 242 | -89.0 | 504990 | 917 | -92.5 | 504990 | 977 | -95.5 | 504990 | 667 |
| MR_1774413560_57CE6F5A | 504990 | 242 | -86.6 | 504990 | 917 | -95.0 | 504990 | 977 | -95.6 | 504990 | 667 |
| MR_1774413560_23E325C3 | 504990 | 242 | -87.4 | 504990 | 917 | -94.9 | 504990 | 977 | -96.7 | 504990 | 667 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1658: `aaff6a96-c83...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `aaff6a96-c839-4492-8ef3-2d4d276378fa` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1658] topology](images/train_1658.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3269074_3 and 3269467_4
- `C2`: Press down the tilt angle of 3259516_2 by 10 degrees
- `C3`: Add neighbor relationship between 3259516_2 and 3269467_4
- `C4`: Adjust the azimuth of 3259516_2 by 50 degrees
- `C5`: Lift the tilt angle of 3259516_2 by 10 degrees
- `C6`: Increase transmission power for 3259516_2
- `C7`: Increase transmission power for 3269467_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269467_4
- `C9`: Increase A3 Offset threshold for 3269467_4
- `C10`: Decrease transmission power for 3269467_4
- `C11`: Decrease transmission power for 3259516_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259516_2
- `C13`: Decrease A3 Offset threshold for 3259516_2
- `C14`: Adjust the azimuth of 3269467_4 by 10 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259516_2
- `C16`: Increase A3 Offset threshold for 3259516_2
- `C17`: Insufficient data; more data is needed for judgment. **← 정답**
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269467_4
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle  of 3269467_4 by 8 degrees
- `C21`: Decrease A3 Offset threshold for 3269467_4
- `C22`: Lift the tilt angle  of 3269467_4 by 8 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.733 | MS1 | 121.4656643358 | 31.1446318364 | 298 | 504990 | -90.21 | 14.06 | 552.90 | 0.10 | 2.75 | 1562 |
| 2024-09-20 22:21:32.489 | MS1 | 121.4656706944 | 31.1446181368 | 298 | 504990 | -86.63 | 14.24 | 363.10 | 0.17 | 2.02 | 1563 |
| 2024-09-20 22:21:33.400 | MS1 | 121.4656694683 | 31.1446317107 | 298 | 504990 | -89.56 | 15.57 | 588.46 | 0.15 | 2.91 | 1595 |
| 2024-09-20 22:21:34.405 | MS1 | 121.4656698988 | 31.1446370576 | 298 | 504990 | -87.80 | 13.05 | 58.49 | 0.20 | 2.68 | 1570 |
| 2024-09-20 22:21:35.209 | MS1 | 121.4656610019 | 31.1446323929 | 298 | 504990 | -89.14 | 12.16 | 67.75 | 0.18 | 2.19 | 1563 |
| 2024-09-20 22:21:36.284 | MS1 | 121.4656585275 | 31.1446333275 | 298 | 504990 | -88.00 | 16.23 | 70.16 | 0.04 | 2.21 | 1587 |
| 2024-09-20 22:21:37.796 | MS1 | 121.4656704216 | 31.1446194194 | 298 | 504990 | -93.97 | 11.82 | 89.76 | 0.15 | 2.52 | 1574 |
| 2024-09-20 22:21:38.908 | MS1 | 121.4656627674 | 31.1446288503 | 298 | 504990 | -93.79 | 7.06 | 74.00 | 0.03 | 2.80 | 1568 |
| 2024-09-20 22:21:39.500 | MS1 | 121.4656702157 | 31.1446286934 | 298 | 504990 | -93.59 | 11.19 | 107.01 | 0.03 | 2.32 | 1590 |
| 2024-09-20 22:21:40.411 | MS1 | 121.4656706866 | 31.1446265376 | 298 | 504990 | -93.37 | 11.74 | 520.26 | 0.13 | 2.86 | 1578 |
| 2024-09-20 22:21:41.391 | MS1 | 121.4656726622 | 31.1446213176 | 298 | 504990 | -90.15 | 11.80 | 470.62 | 0.10 | 2.39 | 1589 |
| 2024-09-20 22:21:42.401 | MS1 | 121.4656779441 | 31.1446270002 | 298 | 504990 | -93.72 | 10.21 | 522.07 | 0.06 | 2.52 | 1578 |

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
| 3248505 | 1 | 121.4709522737 | 31.1495604271 | 27 | 0 | 8 | 27.3 | TDD | 457 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3259516 | 2 | 121.4737800717 | 31.1472796835 | 179 | 12 | 2 | 26.7 | TDD | 298 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3269074 | 3 | 121.4665279997 | 31.1521476732 | 21 | 2 | 11 | 26.9 | TDD | 250 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3269467 | 4 | 121.4645306867 | 31.1515651888 | 162 | 7 | 2 | 15.7 | TDD | 114 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.605 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.628 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.758 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.758 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.420 | NREventA3 | measId:2;ServCellPCI:129;Se... |
| 2024-09-20 22:21:38.660 | NRHandoverAttempt | SourcePCI:129;SourceNR-ARFC... |
| 2024-09-20 22:21:38.691 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.703 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.818 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.818 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3248505 | 1 | 89.7448 | 80.0734 | -117.9379 | 13.5521 | 127.4570 | 0.0096 | 0.0103 |
| 2024_09_19 22:00 | 3259516 | 2 | 88.3893 | 75.1629 | -116.0289 | 14.2963 | 190.5162 | 0.0161 | 0.0092 |
| 2024_09_19 22:00 | 3269074 | 3 | 88.4499 | 89.2072 | -116.3504 | 5.5487 | 107.2125 | 0.0026 | 0.0181 |
| 2024_09_19 22:00 | 3269467 | 4 | 77.6253 | 75.5558 | -114.6175 | 12.5979 | 149.2071 | 0.0031 | 0.0145 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414415_CA0EEFD0 | 504990 | 298 | -87.3 | 504990 | 114 | -96.0 | 504990 | 250 | -98.2 | 504990 | 457 |
| MR_1774414415_1F8F6738 | 504990 | 298 | -88.5 | 504990 | 114 | -96.4 | 504990 | 250 | -97.7 | 504990 | 457 |
| MR_1774414415_7CD7AB8B | 504990 | 298 | -88.7 | 504990 | 114 | -97.8 | 504990 | 250 | -98.7 | 504990 | 457 |
| MR_1774414415_3A59440D | 504990 | 298 | -86.6 | 504990 | 114 | -98.4 | 504990 | 250 | -96.1 | 504990 | 457 |
| MR_1774414415_CCD34978 | 504990 | 298 | -89.2 | 504990 | 114 | -96.8 | 504990 | 250 | -98.7 | 504990 | 457 |
| MR_1774414415_F7F763A4 | 504990 | 298 | -89.6 | 504990 | 114 | -95.8 | 504990 | 250 | -98.7 | 504990 | 457 |
| MR_1774414415_6411DBDD | 504990 | 298 | -86.3 | 504990 | 114 | -98.1 | 504990 | 250 | -98.2 | 504990 | 457 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1659: `4a7ac1ce-8aa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4a7ac1ce-8aa1-4d4e-a982-33071d368d4e` |
| Tag | **multiple-answer** |
| 정답 | **C3|C18** |
| C3 의미 | Press down the tilt angle  of 3234518_2 by 4 degrees |
| C18 의미 | Decrease transmission power for 3234518_2 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1659] topology](images/train_1659.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3269254_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234518_2
- `C3`: Press down the tilt angle  of 3234518_2 by 4 degrees **← 정답**
- `C4`: Add neighbor relationship between 3222264_4 and 3234518_2
- `C5`: Press down the tilt angle of 3269254_3 by 6 degrees
- `C6`: Adjust the azimuth of 3234518_2 by 16 degrees
- `C7`: Decrease A3 Offset threshold for 3234518_2
- `C8`: Lift the tilt angle  of 3234518_2 by 4 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234518_2
- `C10`: Check test server and transmission issues
- `C11`: Increase transmission power for 3234518_2
- `C12`: Increase A3 Offset threshold for 3234518_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269254_3
- `C14`: Lift the tilt angle of 3269254_3 by 6 degrees
- `C15`: Add neighbor relationship between 3269254_3 and 3234518_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase transmission power for 3269254_3
- `C18`: Decrease transmission power for 3234518_2 **← 정답**
- `C19`: Adjust the azimuth of 3269254_3 by 33 degrees
- `C20`: Increase A3 Offset threshold for 3269254_3
- `C21`: Decrease transmission power for 3269254_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269254_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.283 | MS1 | 121.4656656194 | 31.1446200531 | 878 | 504990 | -75.10 | 13.64 | 343.12 | 0.12 | 2.32 | 1576 |
| 2024-09-20 22:21:32.399 | MS1 | 121.4656710749 | 31.1446300896 | 878 | 504990 | -77.96 | 17.97 | 491.06 | 0.10 | 2.80 | 1565 |
| 2024-09-20 22:21:33.589 | MS1 | 121.4656680057 | 31.1446327861 | 878 | 504990 | -81.03 | 13.12 | 329.21 | 0.08 | 2.54 | 1564 |
| 2024-09-20 22:21:34.152 | MS1 | 121.4656656145 | 31.1446195919 | 878 | 504990 | -91.49 | 2.88 | 45.05 | 0.15 | 1.26 | 1592 |
| 2024-09-20 22:21:35.633 | MS1 | 121.4656739089 | 31.1446307516 | 878 | 504990 | -88.37 | 1.51 | 75.25 | 0.02 | 1.16 | 1570 |
| 2024-09-20 22:21:36.489 | MS1 | 121.4656735423 | 31.1446284876 | 878 | 504990 | -89.99 | 0.50 | 60.20 | 0.01 | 1.12 | 1582 |
| 2024-09-20 22:21:37.289 | MS1 | 121.4656591464 | 31.1446347178 | 878 | 504990 | -85.94 | 1.41 | 82.88 | 0.15 | 1.30 | 1580 |
| 2024-09-20 22:21:38.574 | MS1 | 121.4656670447 | 31.1446239462 | 878 | 504990 | -90.60 | 0.42 | 46.27 | 0.16 | 1.07 | 1584 |
| 2024-09-20 22:21:39.466 | MS1 | 121.4656660692 | 31.1446271827 | 878 | 504990 | -91.12 | 3.53 | 46.67 | 0.18 | 1.20 | 1580 |
| 2024-09-20 22:21:40.324 | MS1 | 121.4656724599 | 31.1446345263 | 878 | 504990 | -78.98 | 15.89 | 393.64 | 0.09 | 2.12 | 1568 |
| 2024-09-20 22:21:41.764 | MS1 | 121.4656743255 | 31.1446186321 | 878 | 504990 | -83.64 | 13.88 | 601.12 | 0.03 | 2.97 | 1580 |
| 2024-09-20 22:21:42.832 | MS1 | 121.4656700070 | 31.1446194560 | 878 | 504990 | -82.45 | 16.95 | 445.48 | 0.17 | 2.53 | 1592 |

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
| 3222264 | 4 | 121.4681192501 | 31.1462231521 | 250 | 1 | 9 | 40.8 | TDD | 159 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3233311 | 1 | 121.4722035099 | 31.1505059714 | 142 | 3 | 9 | 50.0 | TDD | 338 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3234518 | 2 | 121.4746928338 | 31.1457782421 | 277 | 2 | 4 | 35.5 | TDD | 413 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3269254 | 3 | 121.4714804504 | 31.1510580008 | 251 | 5 | 0 | 15.6 | TDD | 878 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.084 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.106 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.247 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.247 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233311 | 1 | 7.6059 | 6.7647 | -117.8477 | 11.5486 | 185.3603 | 0.0118 | 0.0106 |
| 2024_09_20 22:00 | 3234518 | 2 | 17.8547 | 14.3468 | -116.0422 | 11.0506 | 82.1501 | 0.0054 | 0.0148 |
| 2024_09_20 22:00 | 3269254 | 3 | 19.3229 | 18.1970 | -109.0422 | 6.7279 | 127.2249 | 0.0006 | 0.0015 |
| 2024_09_20 22:00 | 3222264 | 4 | 7.3372 | 9.7239 | -116.8867 | 7.0577 | 199.9444 | 0.0174 | 0.0113 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413726_91472841 | 504990 | 878 | -91.7 | 504990 | 413 | -89.5 | 504990 | 159 | -89.8 | 504990 | 338 |
| MR_1774413726_69F6CAC6 | 504990 | 878 | -90.0 | 504990 | 413 | -87.7 | 504990 | 159 | -89.1 | 504990 | 338 |
| MR_1774413726_7B98B686 | 504990 | 878 | -92.2 | 504990 | 413 | -88.7 | 504990 | 159 | -90.2 | 504990 | 338 |
| MR_1774413726_26DCDEC0 | 504990 | 878 | -91.7 | 504990 | 413 | -89.3 | 504990 | 159 | -91.0 | 504990 | 338 |
| MR_1774413726_2CBE9AFE | 504990 | 878 | -90.8 | 504990 | 413 | -87.6 | 504990 | 159 | -91.0 | 504990 | 338 |
| MR_1774413726_AFA6EA03 | 504990 | 413 | -90.3 | 504990 | 878 | -90.0 | 504990 | 159 | -88.8 | 504990 | 338 |
| MR_1774413726_03D3CF17 | 504990 | 413 | -92.1 | 504990 | 878 | -86.9 | 504990 | 159 | -90.3 | 504990 | 338 |
| MR_1774413726_B73B525B | 504990 | 878 | -90.1 | 504990 | 413 | -87.7 | 504990 | 159 | -88.7 | 504990 | 338 |

> *... 2개 열 생략 (전체 14열)*

---
