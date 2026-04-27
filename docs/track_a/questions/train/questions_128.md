# Track A 문제 분석 — train[1270]~train[1279]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1270] ~ train[1279] (10개)

## 목차

1. [문제 1270: `a8c76546-b77...`](#1270) — single-answer, 정답: C14
2. [문제 1271: `5aab1066-e65...`](#1271) — single-answer, 정답: C18
3. [문제 1272: `42a9fce0-f9d...`](#1272) — single-answer, 정답: C3
4. [문제 1273: `669daa93-742...`](#1273) — single-answer, 정답: C2
5. [문제 1274: `6e9c94c2-ad9...`](#1274) — single-answer, 정답: C13
6. [문제 1275: `cbd0255e-5af...`](#1275) — single-answer, 정답: C16
7. [문제 1276: `623730aa-941...`](#1276) — multiple-answer, 정답: C19|C21
8. [문제 1277: `4fb84364-e4f...`](#1277) — single-answer, 정답: C18
9. [문제 1278: `b765e7ea-2b4...`](#1278) — multiple-answer, 정답: C7|C8|C12|C20
10. [문제 1279: `fcddc2fe-866...`](#1279) — single-answer, 정답: C19

---

### 문제 1270: `a8c76546-b77...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a8c76546-b777-41e6-8464-5337564df546` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1270] topology](images/train_1270.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3212673_4 by 28 degrees
- `C2`: Decrease transmission power for 3220746_1
- `C3`: Adjust the azimuth of 3220746_1 by 50 degrees
- `C4`: Increase transmission power for 3220746_1
- `C5`: Lift the tilt angle  of 3212673_4 by 10 degrees
- `C6`: Increase A3 Offset threshold for 3212673_4
- `C7`: Decrease transmission power for 3212673_4
- `C8`: Decrease A3 Offset threshold for 3212673_4
- `C9`: Press down the tilt angle of 3220746_1 by 10 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220746_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220746_1
- `C12`: Decrease A3 Offset threshold for 3220746_1
- `C13`: Lift the tilt angle of 3220746_1 by 10 degrees
- `C14`: Insufficient data; more data is needed for judgment. **← 정답**
- `C15`: Increase transmission power for 3212673_4
- `C16`: Add neighbor relationship between 3220746_1 and 3212673_4
- `C17`: Check test server and transmission issues
- `C18`: Add neighbor relationship between 3265453_3 and 3212673_4
- `C19`: Press down the tilt angle  of 3212673_4 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3220746_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212673_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212673_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.862 | MS1 | 121.4656698862 | 31.1446303215 | 440 | 504990 | -90.74 | 13.10 | 533.87 | 0.16 | 2.26 | 1572 |
| 2024-09-20 22:21:32.398 | MS1 | 121.4656752729 | 31.1446195806 | 440 | 504990 | -85.38 | 17.15 | 371.17 | 0.06 | 2.29 | 1568 |
| 2024-09-20 22:21:33.415 | MS1 | 121.4656707168 | 31.1446313517 | 440 | 504990 | -89.12 | 13.05 | 354.83 | 0.05 | 2.75 | 1563 |
| 2024-09-20 22:21:34.135 | MS1 | 121.4656767432 | 31.1446273729 | 440 | 504990 | -90.41 | 13.74 | 61.77 | 0.14 | 2.83 | 1563 |
| 2024-09-20 22:21:35.628 | MS1 | 121.4656676089 | 31.1446233913 | 440 | 504990 | -89.65 | 13.41 | 47.52 | 0.07 | 2.84 | 1570 |
| 2024-09-20 22:21:36.751 | MS1 | 121.4656703278 | 31.1446245869 | 440 | 504990 | -86.93 | 15.33 | 90.46 | 0.18 | 2.86 | 1560 |
| 2024-09-20 22:21:37.747 | MS1 | 121.4656636824 | 31.1446219055 | 440 | 504990 | -89.07 | 9.42 | 55.54 | 0.08 | 2.28 | 1587 |
| 2024-09-20 22:21:38.899 | MS1 | 121.4656627540 | 31.1446230275 | 440 | 504990 | -90.35 | 10.99 | 67.26 | 0.04 | 2.32 | 1589 |
| 2024-09-20 22:21:39.657 | MS1 | 121.4656706449 | 31.1446277061 | 440 | 504990 | -93.10 | 10.57 | 93.96 | 0.03 | 2.94 | 1567 |
| 2024-09-20 22:21:40.591 | MS1 | 121.4656601602 | 31.1446327786 | 440 | 504990 | -91.04 | 11.11 | 593.12 | 0.12 | 2.30 | 1583 |
| 2024-09-20 22:21:41.387 | MS1 | 121.4656704667 | 31.1446285423 | 440 | 504990 | -90.19 | 11.74 | 433.96 | 0.09 | 2.15 | 1595 |
| 2024-09-20 22:21:42.751 | MS1 | 121.4656743472 | 31.1446318947 | 440 | 504990 | -93.01 | 9.86 | 552.84 | 0.12 | 2.15 | 1576 |

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
| 3212673 | 4 | 121.4644378644 | 31.1544065493 | 202 | 15 | 11 | 35.0 | TDD | 957 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3220746 | 1 | 121.4668973797 | 31.1545464613 | 93 | 15 | 6 | 20.8 | TDD | 440 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3229571 | 2 | 121.4689559763 | 31.1549469773 | 257 | 3 | 8 | 22.2 | TDD | 877 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3265453 | 3 | 121.4758785501 | 31.1455697609 | 259 | 1 | 2 | 39.3 | TDD | 869 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.071 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.089 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.215 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.215 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.880 | NREventA3 | measId:2;ServCellPCI:391;Se... |
| 2024-09-20 22:21:38.120 | NRHandoverAttempt | SourcePCI:391;SourceNR-ARFC... |
| 2024-09-20 22:21:38.158 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.173 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.302 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.302 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3220746 | 1 | 82.2480 | 89.0185 | -117.8521 | 7.1414 | 85.4777 | 0.0039 | 0.0087 |
| 2024_09_19 22:00 | 3229571 | 2 | 82.2320 | 75.0321 | -117.0105 | 19.5109 | 154.3079 | 0.0126 | 0.0111 |
| 2024_09_19 22:00 | 3265453 | 3 | 75.9487 | 82.2025 | -114.2354 | 10.9417 | 87.1611 | 0.0088 | 0.0022 |
| 2024_09_19 22:00 | 3212673 | 4 | 82.8143 | 85.1976 | -117.5716 | 11.8398 | 98.3513 | 0.0051 | 0.0046 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415270_27DECB8C | 504990 | 440 | -89.6 | 504990 | 957 | -95.0 | 504990 | 869 | -97.2 | 504990 | 877 |
| MR_1774415270_2BB6AEFD | 504990 | 440 | -89.5 | 504990 | 957 | -96.8 | 504990 | 869 | -98.9 | 504990 | 877 |
| MR_1774415270_C7B5900D | 504990 | 440 | -91.9 | 504990 | 957 | -95.3 | 504990 | 869 | -98.9 | 504990 | 877 |
| MR_1774415270_52EE4CE0 | 504990 | 440 | -90.0 | 504990 | 957 | -97.3 | 504990 | 869 | -96.9 | 504990 | 877 |
| MR_1774415270_4AD23456 | 504990 | 440 | -88.7 | 504990 | 957 | -95.0 | 504990 | 869 | -99.3 | 504990 | 877 |
| MR_1774415270_F7008C91 | 504990 | 440 | -90.7 | 504990 | 957 | -94.9 | 504990 | 869 | -99.5 | 504990 | 877 |
| MR_1774415270_21BE3126 | 504990 | 440 | -91.3 | 504990 | 957 | -97.2 | 504990 | 869 | -98.1 | 504990 | 877 |
| MR_1774415270_E8D5A3E6 | 504990 | 440 | -88.8 | 504990 | 957 | -95.0 | 504990 | 869 | -99.4 | 504990 | 877 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1271: `5aab1066-e65...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5aab1066-e650-43a7-ab8f-c0c45f4d5023` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Add neighbor relationship between 3264038_1 and 3267846_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1271] topology](images/train_1271.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267846_4
- `C2`: Lift the tilt angle  of 3267846_4 by 5 degrees
- `C3`: Decrease A3 Offset threshold for 3264038_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264038_1
- `C5`: Lift the tilt angle of 3264038_1 by 10 degrees
- `C6`: Decrease transmission power for 3264038_1
- `C7`: Increase A3 Offset threshold for 3264038_1
- `C8`: Decrease A3 Offset threshold for 3267846_4
- `C9`: Add neighbor relationship between 3260271_2 and 3267846_4
- `C10`: Press down the tilt angle  of 3267846_4 by 5 degrees
- `C11`: Increase transmission power for 3267846_4
- `C12`: Adjust the azimuth of 3267846_4 by 31 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264038_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267846_4
- `C16`: Check test server and transmission issues
- `C17`: Decrease transmission power for 3267846_4
- `C18`: Add neighbor relationship between 3264038_1 and 3267846_4 **← 정답**
- `C19`: Increase A3 Offset threshold for 3267846_4
- `C20`: Press down the tilt angle of 3264038_1 by 10 degrees
- `C21`: Increase transmission power for 3264038_1
- `C22`: Adjust the azimuth of 3264038_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.272 | MS1 | 121.4656623370 | 31.1446188176 | 554 | 504990 | -78.66 | 12.71 | 506.26 | 0.03 | 2.69 | 1560 |
| 2024-09-20 22:21:32.856 | MS1 | 121.4656617921 | 31.1446229084 | 554 | 504990 | -78.53 | 14.30 | 300.95 | 0.09 | 2.82 | 1585 |
| 2024-09-20 22:21:33.788 | MS1 | 121.4656743953 | 31.1446278503 | 554 | 504990 | -84.18 | 12.83 | 344.61 | 0.18 | 2.02 | 1590 |
| 2024-09-20 22:21:34.880 | MS1 | 121.4656603695 | 31.1446327645 | 554 | 504990 | -91.99 | -0.04 | 64.58 | 0.08 | 1.48 | 1593 |
| 2024-09-20 22:21:35.675 | MS1 | 121.4656670145 | 31.1446249830 | 554 | 504990 | -89.83 | -1.99 | 47.42 | 0.02 | 1.20 | 1573 |
| 2024-09-20 22:21:36.340 | MS1 | 121.4656759109 | 31.1446246749 | 554 | 504990 | -86.44 | -0.40 | 49.45 | 0.18 | 1.19 | 1569 |
| 2024-09-20 22:21:37.437 | MS1 | 121.4656674858 | 31.1446260533 | 554 | 504990 | -86.33 | -0.07 | 47.67 | 0.07 | 1.44 | 1568 |
| 2024-09-20 22:21:38.540 | MS1 | 121.4656608484 | 31.1446368912 | 554 | 504990 | -76.07 | 16.52 | 451.45 | 0.05 | 1.39 | 1576 |
| 2024-09-20 22:21:39.845 | MS1 | 121.4656629576 | 31.1446238001 | 554 | 504990 | -76.77 | 13.22 | 570.02 | 0.15 | 1.12 | 1596 |
| 2024-09-20 22:21:40.238 | MS1 | 121.4656733024 | 31.1446230573 | 554 | 504990 | -83.91 | 14.93 | 537.73 | 0.04 | 2.32 | 1581 |
| 2024-09-20 22:21:41.918 | MS1 | 121.4656687659 | 31.1446304450 | 554 | 504990 | -83.38 | 14.68 | 527.00 | 0.06 | 2.01 | 1561 |
| 2024-09-20 22:21:42.656 | MS1 | 121.4656604261 | 31.1446264726 | 554 | 504990 | -82.79 | 13.32 | 318.19 | 0.15 | 2.98 | 1574 |

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
| 3245370 | 3 | 121.4756528868 | 31.1460599107 | 176 | 2 | 0 | 26.0 | TDD | 378 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3260271 | 2 | 121.4653864977 | 31.1546191235 | 96 | 7 | 5 | 48.8 | TDD | 499 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3264038 | 1 | 121.4671061062 | 31.1486646295 | 2 | 7 | 10 | 43.0 | TDD | 554 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3267846 | 4 | 121.4721403486 | 31.1525078031 | 246 | 3 | 11 | 38.0 | TDD | 759 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.799 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.818 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.924 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.924 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.674 | NREventA3 | measId:2;ServCellPCI:148;Se... |
| 2024-09-20 22:21:35.674 | NREventA3 | measId:2;ServCellPCI:148;Se... |
| 2024-09-20 22:21:36.674 | NREventA3 | measId:2;ServCellPCI:148;Se... |
| 2024-09-20 22:21:39.174 | NRRRCReestablishAttempt | PCI:148 |
| 2024-09-20 22:21:39.188 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.203 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.345 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.345 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264038 | 1 | 18.2114 | 7.6095 | -117.0313 | 14.8239 | 171.9301 | 0.0040 | 0.1723 |
| 2024_09_20 22:00 | 3260271 | 2 | 5.9794 | 6.6025 | -114.3956 | 8.9433 | 177.7533 | 0.0115 | 0.0169 |
| 2024_09_20 22:00 | 3245370 | 3 | 5.0775 | 16.1216 | -114.4037 | 11.7285 | 125.5796 | 0.0051 | 0.0032 |
| 2024_09_20 22:00 | 3267846 | 4 | 11.8092 | 7.4941 | -114.9140 | 5.7182 | 92.9584 | 0.0188 | 0.0096 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416327_997E4DDB | 504990 | 759 | -85.1 | 504990 | 554 | -92.5 | 504990 | 499 | -86.7 | 504990 | 378 |
| MR_1774416327_BCC95B69 | 504990 | 759 | -87.2 | 504990 | 554 | -91.8 | 504990 | 499 | -88.8 | 504990 | 378 |
| MR_1774416327_4BD5EE56 | 504990 | 759 | -87.8 | 504990 | 554 | -91.5 | 504990 | 499 | -86.3 | 504990 | 378 |
| MR_1774416327_CAD8DC2B | 504990 | 554 | -90.7 | 504990 | 759 | -87.4 | 504990 | 499 | -86.0 | 504990 | 378 |
| MR_1774416327_DC96C2DA | 504990 | 759 | -85.4 | 504990 | 554 | -93.7 | 504990 | 499 | -87.8 | 504990 | 378 |
| MR_1774416327_784F2924 | 504990 | 554 | -93.0 | 504990 | 759 | -85.0 | 504990 | 499 | -85.3 | 504990 | 378 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1272: `42a9fce0-f9d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `42a9fce0-f9d6-479d-be7d-8c5b8362ac7a` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Lift the tilt angle  of 3246180_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1272] topology](images/train_1272.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3226145_1
- `C2`: Decrease A3 Offset threshold for 3226145_1
- `C3`: Lift the tilt angle  of 3246180_4 by 10 degrees **← 정답**
- `C4`: Add neighbor relationship between 3246180_4 and 3226145_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248357_3
- `C6`: Press down the tilt angle  of 3246180_4 by 10 degrees
- `C7`: Adjust the azimuth of 3246180_4 by 18 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226145_1
- `C9`: Decrease transmission power for 3248357_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248357_3
- `C11`: Decrease A3 Offset threshold for 3248357_3
- `C12`: Check test server and transmission issues
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Lift the tilt angle of 3248357_3 by 2 degrees
- `C15`: Add neighbor relationship between 3248357_3 and 3226145_1
- `C16`: Increase transmission power for 3248357_3
- `C17`: Press down the tilt angle of 3248357_3 by 2 degrees
- `C18`: Increase transmission power for 3226145_1
- `C19`: Adjust the azimuth of 3248357_3 by 12 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226145_1
- `C21`: Increase A3 Offset threshold for 3248357_3
- `C22`: Decrease transmission power for 3226145_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.428 | MS1 | 121.4656760838 | 31.1446357378 | 764 | 504990 | -88.81 | 15.62 | 389.97 | 0.19 | 2.75 | 1592 |
| 2024-09-20 22:21:32.727 | MS1 | 121.4656735612 | 31.1446252048 | 764 | 504990 | -88.04 | 15.59 | 400.42 | 0.15 | 2.21 | 1576 |
| 2024-09-20 22:21:33.423 | MS1 | 121.4656623078 | 31.1446235118 | 764 | 504990 | -89.96 | 13.94 | 446.18 | 0.18 | 2.65 | 1595 |
| 2024-09-20 22:21:34.579 | MS1 | 121.4656625852 | 31.1446278828 | 764 | 504990 | -90.40 | 15.45 | 79.13 | 0.11 | 2.68 | 1561 |
| 2024-09-20 22:21:35.367 | MS1 | 121.4656653332 | 31.1446269576 | 764 | 504990 | -85.53 | 15.77 | 75.01 | 0.17 | 2.33 | 1588 |
| 2024-09-20 22:21:36.951 | MS1 | 121.4656589594 | 31.1446245986 | 764 | 504990 | -85.01 | 13.91 | 94.92 | 0.10 | 2.83 | 1579 |
| 2024-09-20 22:21:37.473 | MS1 | 121.4656582707 | 31.1446302723 | 764 | 504990 | -92.29 | 9.55 | 76.68 | 0.06 | 2.08 | 1591 |
| 2024-09-20 22:21:38.632 | MS1 | 121.4656598736 | 31.1446261463 | 764 | 504990 | -92.60 | 11.18 | 68.07 | 0.20 | 2.80 | 1567 |
| 2024-09-20 22:21:39.258 | MS1 | 121.4656628858 | 31.1446326800 | 764 | 504990 | -91.92 | 11.98 | 66.76 | 0.02 | 2.88 | 1571 |
| 2024-09-20 22:21:40.636 | MS1 | 121.4656754186 | 31.1446221652 | 764 | 504990 | -93.92 | 8.85 | 472.82 | 0.07 | 2.15 | 1579 |
| 2024-09-20 22:21:41.212 | MS1 | 121.4656670523 | 31.1446345321 | 764 | 504990 | -90.28 | 12.17 | 360.82 | 0.03 | 2.98 | 1578 |
| 2024-09-20 22:21:42.158 | MS1 | 121.4656599493 | 31.1446263409 | 764 | 504990 | -92.93 | 7.63 | 480.46 | 0.12 | 2.58 | 1579 |

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
| 3226145 | 1 | 121.4717270834 | 31.1496630027 | 208 | 12 | 4 | 20.3 | TDD | 729 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3243742 | 2 | 121.4655938951 | 31.1557484280 | 173 | 0 | 4 | 49.4 | TDD | 708 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3246180 | 4 | 121.4758241437 | 31.1440635918 | 106 | 7 | 7 | 46.3 | TDD | 246 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3248357 | 3 | 121.4749836892 | 31.1493723194 | 227 | 1 | 2 | 22.6 | TDD | 764 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.236 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.255 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.360 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.360 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.122 | NREventA3 | measId:2;ServCellPCI:157;Se... |
| 2024-09-20 22:21:38.362 | NRHandoverAttempt | SourcePCI:157;SourceNR-ARFC... |
| 2024-09-20 22:21:38.399 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.411 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.551 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.551 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226145 | 1 | 16.0922 | 8.1618 | -114.9956 | 9.0161 | 106.6430 | 0.0172 | 0.0013 |
| 2024_09_20 22:00 | 3243742 | 2 | 15.4761 | 15.8369 | -115.7882 | 13.9093 | 137.1854 | 0.0040 | 0.0110 |
| 2024_09_20 22:00 | 3248357 | 3 | 93.2490 | 94.0760 | -115.2713 | 9.5730 | 158.4593 | 0.0101 | 0.0017 |
| 2024_09_20 22:00 | 3246180 | 4 | 5.2613 | 15.5759 | -116.6153 | 15.2711 | 184.0386 | 0.0111 | 0.0180 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416644_7CFA3292 | 504990 | 764 | -89.2 | 504990 | 729 | -93.8 | 504990 | 246 | -102.4 | 504990 | 708 |
| MR_1774416644_6B7DF968 | 504990 | 764 | -90.9 | 504990 | 729 | -93.4 | 504990 | 246 | -101.7 | 504990 | 708 |
| MR_1774416644_8E0FBD39 | 504990 | 764 | -90.2 | 504990 | 729 | -96.0 | 504990 | 246 | -104.9 | 504990 | 708 |
| MR_1774416644_F591778A | 504990 | 764 | -92.0 | 504990 | 729 | -95.3 | 504990 | 246 | -103.5 | 504990 | 708 |
| MR_1774416644_8D29741F | 504990 | 764 | -90.2 | 504990 | 729 | -93.4 | 504990 | 246 | -104.0 | 504990 | 708 |
| MR_1774416644_620FEE34 | 504990 | 764 | -90.3 | 504990 | 729 | -95.5 | 504990 | 246 | -101.8 | 504990 | 708 |
| MR_1774416644_C60D0A2E | 504990 | 764 | -92.3 | 504990 | 729 | -94.1 | 504990 | 246 | -105.1 | 504990 | 708 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1273: `669daa93-742...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `669daa93-742d-4198-a73f-b7e620518aa8` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1273] topology](images/train_1273.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3232629_4 and 3233584_2
- `C2`: Insufficient data; more data is needed for judgment. **← 정답**
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221729_1
- `C4`: Increase transmission power for 3221729_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221729_1
- `C6`: Lift the tilt angle  of 3233584_2 by 9 degrees
- `C7`: Adjust the azimuth of 3233584_2 by 36 degrees
- `C8`: Check test server and transmission issues
- `C9`: Lift the tilt angle of 3221729_1 by 10 degrees
- `C10`: Press down the tilt angle of 3221729_1 by 10 degrees
- `C11`: Decrease transmission power for 3233584_2
- `C12`: Increase transmission power for 3233584_2
- `C13`: Increase A3 Offset threshold for 3233584_2
- `C14`: Decrease transmission power for 3221729_1
- `C15`: Increase A3 Offset threshold for 3221729_1
- `C16`: Decrease A3 Offset threshold for 3233584_2
- `C17`: Press down the tilt angle  of 3233584_2 by 9 degrees
- `C18`: Adjust the azimuth of 3221729_1 by 50 degrees
- `C19`: Decrease A3 Offset threshold for 3221729_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233584_2
- `C21`: Add neighbor relationship between 3221729_1 and 3233584_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233584_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.291 | MS1 | 121.4656632757 | 31.1446322682 | 304 | 504990 | -88.47 | 17.62 | 492.21 | 0.13 | 2.30 | 1562 |
| 2024-09-20 22:21:32.905 | MS1 | 121.4656651624 | 31.1446279245 | 304 | 504990 | -85.30 | 16.80 | 557.99 | 0.04 | 2.10 | 1564 |
| 2024-09-20 22:21:33.660 | MS1 | 121.4656725497 | 31.1446217057 | 304 | 504990 | -88.60 | 14.75 | 433.45 | 0.01 | 2.50 | 1570 |
| 2024-09-20 22:21:34.985 | MS1 | 121.4656687033 | 31.1446225648 | 304 | 504990 | -89.13 | 16.85 | 90.10 | 0.07 | 2.85 | 1584 |
| 2024-09-20 22:21:35.131 | MS1 | 121.4656764129 | 31.1446327587 | 304 | 504990 | -90.70 | 14.95 | 56.75 | 0.10 | 2.98 | 1596 |
| 2024-09-20 22:21:36.864 | MS1 | 121.4656610076 | 31.1446361590 | 304 | 504990 | -88.81 | 17.31 | 71.39 | 0.06 | 2.84 | 1590 |
| 2024-09-20 22:21:37.686 | MS1 | 121.4656624775 | 31.1446241861 | 304 | 504990 | -91.96 | 9.05 | 58.27 | 0.16 | 2.48 | 1598 |
| 2024-09-20 22:21:38.365 | MS1 | 121.4656662603 | 31.1446294886 | 304 | 504990 | -89.88 | 7.74 | 83.81 | 0.18 | 2.11 | 1586 |
| 2024-09-20 22:21:39.942 | MS1 | 121.4656774291 | 31.1446224575 | 304 | 504990 | -90.95 | 9.65 | 62.36 | 0.15 | 2.39 | 1573 |
| 2024-09-20 22:21:40.891 | MS1 | 121.4656735701 | 31.1446277610 | 304 | 504990 | -89.93 | 11.42 | 489.10 | 0.11 | 2.58 | 1570 |
| 2024-09-20 22:21:41.197 | MS1 | 121.4656709031 | 31.1446229252 | 304 | 504990 | -91.31 | 7.11 | 369.06 | 0.06 | 2.01 | 1599 |
| 2024-09-20 22:21:42.376 | MS1 | 121.4656675951 | 31.1446357706 | 304 | 504990 | -91.22 | 12.79 | 443.43 | 0.19 | 2.05 | 1590 |

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
| 3221729 | 1 | 121.4743056683 | 31.1505823252 | 327 | 14 | 1 | 33.7 | TDD | 304 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3232629 | 4 | 121.4680949953 | 31.1442627598 | 253 | 10 | 4 | 48.3 | TDD | 87 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3233584 | 2 | 121.4722644405 | 31.1519202380 | 254 | 8 | 3 | 22.8 | TDD | 189 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3279390 | 3 | 121.4643486990 | 31.1454447930 | 132 | 15 | 12 | 49.3 | TDD | 854 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.230 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.230 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.907 | NREventA3 | measId:2;ServCellPCI:167;Se... |
| 2024-09-20 22:21:38.147 | NRHandoverAttempt | SourcePCI:167;SourceNR-ARFC... |
| 2024-09-20 22:21:38.181 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.195 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.300 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.300 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3221729 | 1 | 87.7095 | 78.9210 | -115.2391 | 10.7679 | 145.8821 | 0.0049 | 0.0182 |
| 2024_09_19 22:00 | 3233584 | 2 | 94.1740 | 93.0126 | -115.2132 | 19.5867 | 165.0571 | 0.0094 | 0.0127 |
| 2024_09_19 22:00 | 3279390 | 3 | 77.9625 | 87.8665 | -115.0451 | 10.0120 | 130.0876 | 0.0163 | 0.0163 |
| 2024_09_19 22:00 | 3232629 | 4 | 81.5636 | 93.8987 | -115.8637 | 8.9259 | 83.1363 | 0.0156 | 0.0005 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413875_5D7085F3 | 504990 | 304 | -89.0 | 504990 | 189 | -90.1 | 504990 | 87 | -97.9 | 504990 | 854 |
| MR_1774413875_02B4F2B1 | 504990 | 304 | -87.2 | 504990 | 189 | -89.6 | 504990 | 87 | -94.9 | 504990 | 854 |
| MR_1774413875_7ED85F5F | 504990 | 304 | -88.7 | 504990 | 189 | -90.1 | 504990 | 87 | -94.5 | 504990 | 854 |
| MR_1774413875_7286D07C | 504990 | 304 | -90.3 | 504990 | 189 | -87.6 | 504990 | 87 | -94.4 | 504990 | 854 |
| MR_1774413875_057FC8E9 | 504990 | 304 | -90.3 | 504990 | 189 | -90.6 | 504990 | 87 | -95.1 | 504990 | 854 |
| MR_1774413875_ECD6EE0C | 504990 | 304 | -91.0 | 504990 | 189 | -87.5 | 504990 | 87 | -95.2 | 504990 | 854 |
| MR_1774413875_BAD96B53 | 504990 | 304 | -89.3 | 504990 | 189 | -90.5 | 504990 | 87 | -95.9 | 504990 | 854 |
| MR_1774413875_CA625CE1 | 504990 | 304 | -87.7 | 504990 | 189 | -90.1 | 504990 | 87 | -95.5 | 504990 | 854 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1274: `6e9c94c2-ad9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6e9c94c2-ad93-485b-9ddd-1d4b473b0c66` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1274] topology](images/train_1274.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease transmission power for 3259349_4
- `C3`: Decrease transmission power for 3273407_2
- `C4`: Increase A3 Offset threshold for 3259349_4
- `C5`: Decrease A3 Offset threshold for 3273407_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273407_2
- `C7`: Increase A3 Offset threshold for 3273407_2
- `C8`: Lift the tilt angle  of 3259349_4 by 10 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259349_4
- `C10`: Increase transmission power for 3273407_2
- `C11`: Adjust the azimuth of 3273407_2 by 50 degrees
- `C12`: Add neighbor relationship between 3259795_3 and 3259349_4
- `C13`: Check test server and transmission issues **← 정답**
- `C14`: Press down the tilt angle  of 3259349_4 by 10 degrees
- `C15`: Add neighbor relationship between 3273407_2 and 3259349_4
- `C16`: Lift the tilt angle of 3273407_2 by 9 degrees
- `C17`: Adjust the azimuth of 3259349_4 by 3 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273407_2
- `C19`: Increase transmission power for 3259349_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259349_4
- `C21`: Press down the tilt angle of 3273407_2 by 9 degrees
- `C22`: Decrease A3 Offset threshold for 3259349_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.113 | MS1 | 121.4656688220 | 31.1446289929 | 18 | 504990 | -87.80 | 15.81 | 421.42 | 0.05 | 2.89 | 1578 |
| 2024-09-20 22:21:32.943 | MS1 | 121.4656665972 | 31.1446355797 | 18 | 504990 | -85.43 | 12.69 | 394.22 | 0.07 | 2.24 | 1599 |
| 2024-09-20 22:21:33.464 | MS1 | 121.4656595552 | 31.1446181032 | 18 | 504990 | -89.60 | 14.37 | 348.76 | 0.19 | 2.76 | 1577 |
| 2024-09-20 22:21:34.679 | MS1 | 121.4656756768 | 31.1446225512 | 18 | 504990 | -89.45 | 14.33 | 67.36 | 0.01 | 2.74 | 302 |
| 2024-09-20 22:21:35.834 | MS1 | 121.4656701453 | 31.1446235384 | 18 | 504990 | -86.38 | 16.55 | 108.96 | 0.02 | 2.38 | 401 |
| 2024-09-20 22:21:36.735 | MS1 | 121.4656672579 | 31.1446220440 | 18 | 504990 | -90.08 | 16.19 | 93.88 | 0.06 | 2.99 | 379 |
| 2024-09-20 22:21:37.531 | MS1 | 121.4656688337 | 31.1446270896 | 18 | 504990 | -91.29 | 8.85 | 77.23 | 0.04 | 2.03 | 327 |
| 2024-09-20 22:21:38.120 | MS1 | 121.4656615430 | 31.1446311729 | 18 | 504990 | -92.81 | 7.94 | 72.43 | 0.19 | 2.34 | 364 |
| 2024-09-20 22:21:39.910 | MS1 | 121.4656764480 | 31.1446291952 | 18 | 504990 | -91.87 | 9.68 | 52.56 | 0.10 | 2.88 | 311 |
| 2024-09-20 22:21:40.825 | MS1 | 121.4656696639 | 31.1446280734 | 18 | 504990 | -90.94 | 9.95 | 314.72 | 0.11 | 2.93 | 1598 |
| 2024-09-20 22:21:41.325 | MS1 | 121.4656586050 | 31.1446297562 | 18 | 504990 | -89.77 | 12.40 | 537.38 | 0.16 | 2.14 | 1576 |
| 2024-09-20 22:21:42.540 | MS1 | 121.4656761205 | 31.1446297816 | 18 | 504990 | -93.14 | 11.20 | 575.73 | 0.01 | 2.66 | 1572 |

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
| 3239919 | 1 | 121.4738815025 | 31.1441492784 | 235 | 6 | 7 | 21.7 | TDD | 345 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3259349 | 4 | 121.4700292588 | 31.1551498795 | 196 | 11 | 3 | 45.2 | TDD | 588 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3259795 | 3 | 121.4657264366 | 31.1503113045 | 139 | 11 | 6 | 29.5 | TDD | 425 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3273407 | 2 | 121.4721570833 | 31.1477368178 | 75 | 5 | 12 | 47.2 | TDD | 18 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.941 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.961 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.106 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.106 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.784 | NREventA3 | measId:2;ServCellPCI:59;Ser... |
| 2024-09-20 22:21:38.024 | NRHandoverAttempt | SourcePCI:59;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.070 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.084 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.189 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.189 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239919 | 1 | 17.5695 | 18.2482 | -114.1897 | 18.1112 | 108.4055 | 0.0134 | 0.0015 |
| 2024_09_20 22:00 | 3273407 | 2 | 10.9210 | 12.7493 | -116.7326 | 12.5779 | 93.8475 | 0.0197 | 0.0126 |
| 2024_09_20 22:00 | 3259795 | 3 | 17.5866 | 9.7190 | -115.0410 | 8.0757 | 145.3798 | 0.0114 | 0.0145 |
| 2024_09_20 22:00 | 3259349 | 4 | 18.3254 | 9.2270 | -115.6541 | 14.1589 | 198.2490 | 0.0177 | 0.0003 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413471_02AFE005 | 504990 | 18 | -88.4 | 504990 | 588 | -97.4 | 504990 | 425 | -95.8 | 504990 | 345 |
| MR_1774413471_C34BDA9B | 504990 | 18 | -90.6 | 504990 | 588 | -95.8 | 504990 | 425 | -95.9 | 504990 | 345 |
| MR_1774413471_037727F0 | 504990 | 18 | -90.5 | 504990 | 588 | -96.1 | 504990 | 425 | -98.8 | 504990 | 345 |
| MR_1774413471_BA265797 | 504990 | 18 | -91.0 | 504990 | 588 | -97.6 | 504990 | 425 | -98.6 | 504990 | 345 |
| MR_1774413471_65498E37 | 504990 | 18 | -88.9 | 504990 | 588 | -97.5 | 504990 | 425 | -97.1 | 504990 | 345 |
| MR_1774413471_5EBF6D6C | 504990 | 18 | -90.1 | 504990 | 588 | -96.7 | 504990 | 425 | -96.4 | 504990 | 345 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1275: `cbd0255e-5af...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cbd0255e-5af6-4b34-a7e1-8cf0fa5761e4` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243633_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1275] topology](images/train_1275.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3243633_1
- `C2`: Increase A3 Offset threshold for 3255615_4
- `C3`: Add neighbor relationship between 3243633_1 and 3255615_4
- `C4`: Decrease A3 Offset threshold for 3255615_4
- `C5`: Adjust the azimuth of 3255615_4 by 13 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255615_4
- `C7`: Decrease A3 Offset threshold for 3243633_1
- `C8`: Press down the tilt angle  of 3255615_4 by 2 degrees
- `C9`: Increase transmission power for 3255615_4
- `C10`: Lift the tilt angle of 3243633_1 by 1 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase A3 Offset threshold for 3243633_1
- `C13`: Increase transmission power for 3243633_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255615_4
- `C15`: Lift the tilt angle  of 3255615_4 by 2 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243633_1 **← 정답**
- `C17`: Press down the tilt angle of 3243633_1 by 1 degrees
- `C18`: Adjust the azimuth of 3243633_1 by 30 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243633_1
- `C20`: Check test server and transmission issues
- `C21`: Add neighbor relationship between 3262787_12 and 3255615_4
- `C22`: Decrease transmission power for 3255615_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.513 | MS1 | 121.4656694553 | 31.1446257098 | 389 | 504990 | -94.38 | 12.77 | 449.32 | 0.09 | 2.65 | 1565 |
| 2024-09-20 22:21:32.397 | MS1 | 121.4656665780 | 31.1446345714 | 571 | 504990 | -93.66 | 13.77 | 419.46 | 0.06 | 2.11 | 1575 |
| 2024-09-20 22:21:33.688 | MS1 | 121.4656752943 | 31.1446263897 | 909 | 504990 | -94.45 | 9.54 | 524.99 | 0.18 | 2.86 | 1562 |
| 2024-09-20 22:21:34.193 | MS1 | 121.4656618183 | 31.1446334298 | 479 | 152650 | -95.70 | 7.13 | 98.33 | 0.03 | 1.95 | 930 |
| 2024-09-20 22:21:35.968 | MS1 | 121.4656638750 | 31.1446364959 | 981 | 152650 | -94.28 | 3.77 | 77.70 | 0.17 | 1.83 | 960 |
| 2024-09-20 22:21:36.502 | MS1 | 121.4656592428 | 31.1446266038 | 954 | 152650 | -92.83 | 2.89 | 91.27 | 0.06 | 1.83 | 957 |
| 2024-09-20 22:21:37.952 | MS1 | 121.4656701297 | 31.1446189765 | 455 | 152650 | -88.08 | 3.15 | 56.03 | 0.09 | 1.59 | 925 |
| 2024-09-20 22:21:38.530 | MS1 | 121.4656594652 | 31.1446288357 | 479 | 152650 | -95.93 | 6.34 | 53.46 | 0.05 | 1.71 | 936 |
| 2024-09-20 22:21:39.471 | MS1 | 121.4656636316 | 31.1446312644 | 981 | 152650 | -91.77 | 7.28 | 97.32 | 0.13 | 1.96 | 927 |
| 2024-09-20 22:21:40.918 | MS1 | 121.4656708794 | 31.1446236213 | 954 | 152650 | -91.70 | 5.59 | 67.43 | 0.14 | 2.60 | 1598 |
| 2024-09-20 22:21:41.458 | MS1 | 121.4656636142 | 31.1446325510 | 455 | 152650 | -96.74 | 2.30 | 68.68 | 0.07 | 2.00 | 1572 |
| 2024-09-20 22:21:42.354 | MS1 | 121.4656607074 | 31.1446318454 | 479 | 152650 | -96.62 | 7.14 | 56.63 | 0.04 | 2.14 | 1570 |

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
| 3215040 | 7 | 121.4662300074 | 31.1447939881 | 314 | 2 | 1 | 21.3 | FDD | 455 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3218422 | 8 | 121.4693534756 | 31.1541354104 | 189 | 10 | 0 | 8.7 | FDD | 844 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3227214 | 10 | 121.4747292236 | 31.1453355807 | 237 | 15 | 2 | 18.9 | FDD | 625 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3228533 | 3 | 121.4709218150 | 31.1452499057 | 258 | 3 | 2 | 22.6 | TDD | 909 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3241940 | 5 | 121.4693088349 | 31.1490783536 | 22 | 4 | 2 | 29.4 | TDD | 122 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3243633 | 1 | 121.4714154072 | 31.1544408383 | 177 | 0 | 7 | 29.9 | TDD | 389 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3250605 | 13 | 121.4659231095 | 31.1554485185 | 9 | 13 | 10 | 7.2 | FDD | 479 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3255615 | 4 | 121.4733446393 | 31.1447830805 | 282 | 0 | 10 | 23.1 | TDD | 663 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3259290 | 6 | 121.4689078528 | 31.1482601769 | 145 | 5 | 3 | 2.2 | TDD | 571 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3262787 | 12 | 121.4702203491 | 31.1486488233 | 64 | 8 | 5 | 16.3 | FDD | 954 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3272222 | 11 | 121.4719561350 | 31.1553125819 | 339 | 12 | 11 | 11.4 | FDD | 981 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3276714 | 9 | 121.4757322170 | 31.1537421743 | 215 | 6 | 8 | 21.8 | FDD | 397 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3278434 | 2 | 121.4743544045 | 31.1488332810 | 279 | 5 | 7 | 14.0 | TDD | 236 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.590 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.611 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.750 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.750 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.453 | NREventA2 | measId:1;ServCellPCI:204;Se... |
| 2024-09-20 22:21:35.567 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.845 | NREventA5 | measId:3;ServCellPCI:204;Se... |
| 2024-09-20 22:21:35.889 | NRHandoverAttempt | SourcePCI:204;SourceNR-ARFC... |
| 2024-09-20 22:21:35.932 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.945 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.086 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.086 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243633 | 1 | 12.5832 | 7.8638 | -116.5971 | 14.4702 | 195.7468 | 0.0137 | 0.0134 |
| 2024_09_20 22:00 | 3278434 | 2 | 7.9883 | 14.8203 | -115.0507 | 7.3659 | 136.2586 | 0.0183 | 0.0156 |
| 2024_09_20 22:00 | 3228533 | 3 | 7.0002 | 16.1415 | -115.1820 | 7.1840 | 136.9793 | 0.0168 | 0.0027 |
| 2024_09_20 22:00 | 3255615 | 4 | 12.2375 | 18.0597 | -117.3487 | 6.2417 | 124.5701 | 0.0066 | 0.0141 |
| 2024_09_20 22:00 | 3241940 | 5 | 5.7992 | 9.5857 | -117.0761 | 18.8228 | 81.8129 | 0.0192 | 0.0034 |
| 2024_09_20 22:00 | 3259290 | 6 | 16.2590 | 13.3251 | -117.6722 | 11.1319 | 171.1720 | 0.0130 | 0.0057 |
| 2024_09_20 22:00 | 3215040 | 7 | 5.6781 | 19.7513 | -114.6534 | 3.9660 | 43.9802 | 0.0183 | 0.0157 |
| 2024_09_20 22:00 | 3218422 | 8 | 7.2569 | 9.4486 | -114.3633 | 3.5312 | 38.0491 | 0.0066 | 0.0145 |
| 2024_09_20 22:00 | 3276714 | 9 | 11.7871 | 14.4535 | -114.6518 | 3.8444 | 38.4041 | 0.0180 | 0.0030 |
| 2024_09_20 22:00 | 3227214 | 10 | 12.7080 | 19.7476 | -115.4068 | 4.8398 | 51.9212 | 0.0190 | 0.0119 |
| 2024_09_20 22:00 | 3272222 | 11 | 6.4585 | 8.6931 | -116.1736 | 4.3539 | 34.5622 | 0.0124 | 0.0127 |
| 2024_09_20 22:00 | 3262787 | 12 | 13.5675 | 16.4024 | -114.9956 | 4.3011 | 37.4315 | 0.0151 | 0.0198 |
| 2024_09_20 22:00 | 3250605 | 13 | 16.5482 | 8.8236 | -116.3641 | 3.3946 | 57.9025 | 0.0078 | 0.0163 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414938_D990D8AD | 504990 | 909 | -95.2 | 504990 | 663 | -91.7 | 504990 | 236 | -91.9 | 504990 | 122 |
| MR_1774414938_053175D9 | 152650 | 479 | -93.9 | 152650 | 397 | -98.3 | 152650 | 844 | -103.4 | 152650 | 625 |
| MR_1774414938_6A2E06A1 | 152650 | 479 | -95.1 | 152650 | 397 | -99.2 | 152650 | 844 | -103.1 | 152650 | 625 |
| MR_1774414938_0FEF37A7 | 504990 | 909 | -94.1 | 504990 | 663 | -88.9 | 504990 | 236 | -94.6 | 504990 | 122 |
| MR_1774414938_4ADA28E6 | 152650 | 479 | -93.8 | 152650 | 397 | -97.1 | 152650 | 844 | -102.1 | 152650 | 625 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1276: `623730aa-941...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `623730aa-9414-4cf8-87e1-a36b9d96b2f2` |
| Tag | **multiple-answer** |
| 정답 | **C19|C21** |
| C19 의미 | Increase transmission power for 3228903_1 |
| C21 의미 | Adjust the azimuth of 3228903_1 by 38 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1276] topology](images/train_1276.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3228903_1 and 3268767_4
- `C2`: Increase transmission power for 3268767_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268767_4
- `C4`: Decrease A3 Offset threshold for 3228903_1
- `C5`: Press down the tilt angle  of 3268767_4 by 6 degrees
- `C6`: Adjust the azimuth of 3268767_4 by 45 degrees
- `C7`: Decrease A3 Offset threshold for 3268767_4
- `C8`: Decrease transmission power for 3228903_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Lift the tilt angle  of 3268767_4 by 6 degrees
- `C11`: Check test server and transmission issues
- `C12`: Decrease transmission power for 3268767_4
- `C13`: Press down the tilt angle of 3228903_1 by 8 degrees
- `C14`: Increase A3 Offset threshold for 3228903_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228903_1
- `C16`: Lift the tilt angle of 3228903_1 by 8 degrees
- `C17`: Increase A3 Offset threshold for 3268767_4
- `C18`: Add neighbor relationship between 3248277_2 and 3268767_4
- `C19`: Increase transmission power for 3228903_1 **← 정답**
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228903_1
- `C21`: Adjust the azimuth of 3228903_1 by 38 degrees **← 정답**
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268767_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.338 | MS1 | 121.4656605068 | 31.1446379636 | 345 | 504990 | -94.15 | 15.80 | 521.13 | 0.09 | 2.59 | 1594 |
| 2024-09-20 22:21:32.164 | MS1 | 121.4656760795 | 31.1446281289 | 345 | 504990 | -91.57 | 12.96 | 363.45 | 0.01 | 2.49 | 1575 |
| 2024-09-20 22:21:33.680 | MS1 | 121.4656733967 | 31.1446253069 | 345 | 504990 | -91.61 | 15.73 | 374.75 | 0.10 | 2.70 | 1585 |
| 2024-09-20 22:21:34.258 | MS1 | 121.4656752933 | 31.1446327747 | 345 | 504990 | -100.07 | -0.62 | 62.28 | 0.08 | 1.04 | 1590 |
| 2024-09-20 22:21:35.144 | MS1 | 121.4656628250 | 31.1446191569 | 345 | 504990 | -106.52 | 1.37 | 26.13 | 0.08 | 1.25 | 1598 |
| 2024-09-20 22:21:36.990 | MS1 | 121.4656750026 | 31.1446367735 | 345 | 504990 | -104.41 | -0.44 | 46.97 | 0.19 | 1.24 | 1562 |
| 2024-09-20 22:21:37.285 | MS1 | 121.4656724854 | 31.1446267184 | 345 | 504990 | -103.56 | -0.75 | 32.97 | 0.07 | 1.46 | 1582 |
| 2024-09-20 22:21:38.511 | MS1 | 121.4656642489 | 31.1446259009 | 345 | 504990 | -107.00 | 1.36 | 61.39 | 0.15 | 1.10 | 1597 |
| 2024-09-20 22:21:39.821 | MS1 | 121.4656609423 | 31.1446344929 | 345 | 504990 | -106.58 | -0.19 | 57.37 | 0.03 | 1.21 | 1566 |
| 2024-09-20 22:21:40.729 | MS1 | 121.4656770777 | 31.1446211671 | 345 | 504990 | -90.90 | 15.61 | 356.76 | 0.09 | 2.73 | 1571 |
| 2024-09-20 22:21:41.335 | MS1 | 121.4656779177 | 31.1446260350 | 345 | 504990 | -90.66 | 12.52 | 483.02 | 0.05 | 2.45 | 1585 |
| 2024-09-20 22:21:42.517 | MS1 | 121.4656647302 | 31.1446222748 | 345 | 504990 | -86.68 | 16.45 | 386.96 | 0.17 | 2.28 | 1560 |

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
| 3228903 | 1 | 121.4697985197 | 31.1544656988 | 162 | 6 | 7 | 47.5 | TDD | 345 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3248277 | 2 | 121.4703173629 | 31.1449005349 | 0 | 12 | 8 | 47.7 | TDD | 788 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3251624 | 3 | 121.4744687831 | 31.1557176784 | 329 | 0 | 0 | 46.9 | TDD | 365 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3268767 | 4 | 121.4712246089 | 31.1459487319 | 299 | 2 | 6 | 34.2 | TDD | 198 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.062 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.083 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.225 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.225 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.408 | NREventA2 | measId:1;ServCellPCI:664;Se... |
| 2024-09-20 22:21:34.554 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228903 | 1 | 9.5216 | 6.9853 | -115.4948 | 14.2612 | 98.9968 | 0.1685 | 0.0085 |
| 2024_09_20 22:00 | 3248277 | 2 | 9.2541 | 8.2942 | -114.2479 | 7.0316 | 119.5189 | 0.0065 | 0.0039 |
| 2024_09_20 22:00 | 3251624 | 3 | 7.1629 | 15.2951 | -115.4476 | 8.6114 | 132.6942 | 0.0028 | 0.0069 |
| 2024_09_20 22:00 | 3268767 | 4 | 18.1273 | 8.4422 | -117.9102 | 16.0035 | 148.9855 | 0.0029 | 0.0092 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413581_5B8AECB4 | 504990 | 345 | -99.6 | 504990 | 198 | -104.7 | 504990 | 788 | -109.6 | 504990 | 365 |
| MR_1774413581_657A0CB6 | 504990 | 345 | -98.4 | 504990 | 198 | -104.5 | 504990 | 788 | -111.4 | 504990 | 365 |
| MR_1774413581_0A2262C6 | 504990 | 345 | -98.7 | 504990 | 198 | -102.5 | 504990 | 788 | -111.4 | 504990 | 365 |
| MR_1774413581_BCF1881F | 504990 | 345 | -99.0 | 504990 | 198 | -104.0 | 504990 | 788 | -111.7 | 504990 | 365 |
| MR_1774413581_4806ACA3 | 504990 | 345 | -101.2 | 504990 | 198 | -102.2 | 504990 | 788 | -111.9 | 504990 | 365 |
| MR_1774413581_610B85E2 | 504990 | 345 | -99.8 | 504990 | 198 | -101.4 | 504990 | 788 | -110.5 | 504990 | 365 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1277: `4fb84364-e4f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4fb84364-e4fa-48be-809d-e5ae56193f4e` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Decrease A3 Offset threshold for 3261519_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1277] topology](images/train_1277.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3261519_2 by 8 degrees
- `C2`: Decrease transmission power for 3261519_2
- `C3`: Decrease A3 Offset threshold for 3250680_1
- `C4`: Increase transmission power for 3261519_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261519_2
- `C6`: Increase A3 Offset threshold for 3250680_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261519_2
- `C8`: Press down the tilt angle of 3261519_2 by 8 degrees
- `C9`: Increase A3 Offset threshold for 3261519_2
- `C10`: Adjust the azimuth of 3250680_1 by 50 degrees
- `C11`: Press down the tilt angle  of 3250680_1 by 7 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250680_1
- `C14`: Lift the tilt angle  of 3250680_1 by 7 degrees
- `C15`: Add neighbor relationship between 3258065_4 and 3250680_1
- `C16`: Check test server and transmission issues
- `C17`: Increase transmission power for 3250680_1
- `C18`: Decrease A3 Offset threshold for 3261519_2 **← 정답**
- `C19`: Decrease transmission power for 3250680_1
- `C20`: Adjust the azimuth of 3261519_2 by 19 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250680_1
- `C22`: Add neighbor relationship between 3261519_2 and 3250680_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.107 | MS1 | 121.4656742534 | 31.1446325278 | 265 | 504990 | -82.71 | 17.19 | 351.65 | 0.12 | 2.13 | 1564 |
| 2024-09-20 22:21:32.721 | MS1 | 121.4656581883 | 31.1446305929 | 265 | 504990 | -84.36 | 15.96 | 439.61 | 0.07 | 2.51 | 1571 |
| 2024-09-20 22:21:33.237 | MS1 | 121.4656731871 | 31.1446234059 | 265 | 504990 | -78.96 | 13.41 | 547.13 | 0.00 | 2.23 | 1584 |
| 2024-09-20 22:21:34.927 | MS1 | 121.4656592350 | 31.1446309024 | 265 | 504990 | -90.35 | -3.40 | 52.38 | 0.13 | 1.12 | 1600 |
| 2024-09-20 22:21:35.136 | MS1 | 121.4656622090 | 31.1446213767 | 265 | 504990 | -90.30 | -2.79 | 42.79 | 0.11 | 1.23 | 1579 |
| 2024-09-20 22:21:36.694 | MS1 | 121.4656608225 | 31.1446290288 | 265 | 504990 | -84.58 | -1.35 | 49.49 | 0.10 | 1.24 | 1560 |
| 2024-09-20 22:21:37.370 | MS1 | 121.4656593750 | 31.1446258604 | 265 | 504990 | -90.14 | -3.35 | 38.11 | 0.17 | 1.09 | 1598 |
| 2024-09-20 22:21:38.563 | MS1 | 121.4656759901 | 31.1446354791 | 265 | 504990 | -91.82 | -0.53 | 72.01 | 0.10 | 1.45 | 1566 |
| 2024-09-20 22:21:39.845 | MS1 | 121.4656753774 | 31.1446306607 | 416 | 504990 | -76.38 | 14.47 | 151.22 | 0.02 | 1.24 | 1571 |
| 2024-09-20 22:21:40.893 | MS1 | 121.4656713569 | 31.1446252733 | 416 | 504990 | -80.34 | 16.44 | 390.98 | 0.05 | 2.51 | 1589 |
| 2024-09-20 22:21:41.698 | MS1 | 121.4656707645 | 31.1446238680 | 416 | 504990 | -78.03 | 17.64 | 460.58 | 0.18 | 2.04 | 1570 |
| 2024-09-20 22:21:42.105 | MS1 | 121.4656591143 | 31.1446330307 | 416 | 504990 | -83.14 | 13.49 | 312.44 | 0.15 | 2.26 | 1597 |

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
| 3226129 | 3 | 121.4673338363 | 31.1529611011 | 250 | 6 | 4 | 36.7 | TDD | 434 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3250680 | 1 | 121.4667910348 | 31.1530818875 | 341 | 6 | 6 | 15.0 | TDD | 416 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3258065 | 4 | 121.4644763037 | 31.1527592518 | 170 | 8 | 9 | 20.3 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3261519 | 2 | 121.4738384474 | 31.1452950944 | 284 | 5 | 9 | 44.0 | TDD | 265 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.856 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.876 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.024 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.024 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.669 | NREventA3 | measId:2;ServCellPCI:368;Se... |
| 2024-09-20 22:21:37.909 | NRHandoverAttempt | SourcePCI:368;SourceNR-ARFC... |
| 2024-09-20 22:21:37.942 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.955 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.102 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.102 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250680 | 1 | 7.7396 | 13.2877 | -115.0663 | 17.0223 | 170.3944 | 0.0077 | 0.0128 |
| 2024_09_20 22:00 | 3261519 | 2 | 19.2111 | 9.2193 | -117.0937 | 18.9050 | 187.1411 | 0.0195 | 0.1293 |
| 2024_09_20 22:00 | 3226129 | 3 | 18.3754 | 19.0254 | -116.3046 | 12.3907 | 127.1482 | 0.0106 | 0.0152 |
| 2024_09_20 22:00 | 3258065 | 4 | 5.7653 | 15.1892 | -114.2610 | 19.8114 | 142.3348 | 0.0161 | 0.0117 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413257_26581977 | 504990 | 416 | -85.9 | 504990 | 265 | -89.4 | 504990 | 382 | -86.0 | 504990 | 434 |
| MR_1774413257_83CC0573 | 504990 | 265 | -90.7 | 504990 | 416 | -84.6 | 504990 | 382 | -86.4 | 504990 | 434 |
| MR_1774413257_F9E32E81 | 504990 | 416 | -86.9 | 504990 | 265 | -92.3 | 504990 | 382 | -86.2 | 504990 | 434 |
| MR_1774413257_F3F88C89 | 504990 | 265 | -89.5 | 504990 | 416 | -83.8 | 504990 | 382 | -88.1 | 504990 | 434 |
| MR_1774413257_A30204B5 | 504990 | 416 | -87.7 | 504990 | 265 | -88.7 | 504990 | 382 | -87.9 | 504990 | 434 |
| MR_1774413257_1B8E86B3 | 504990 | 265 | -91.4 | 504990 | 416 | -87.1 | 504990 | 382 | -85.1 | 504990 | 434 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1278: `b765e7ea-2b4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b765e7ea-2b43-4356-8a21-0febd334d22b` |
| Tag | **multiple-answer** |
| 정답 | **C7|C8|C12|C20** |
| C7 의미 | Increase A3 Offset threshold for 3277073_5 |
| C8 의미 | Press down the tilt angle  of 3277073_5 by 2 degrees |
| C12 의미 | Decrease transmission power for 3277073_5 |
| C20 의미 | Increase A3 Offset threshold for 3229369_1 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1278] topology](images/train_1278.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3229369_1
- `C2`: Check test server and transmission issues
- `C3`: Add neighbor relationship between 3253385_4 and 3277073_5
- `C4`: Decrease A3 Offset threshold for 3277073_5
- `C5`: Increase transmission power for 3277073_5
- `C6`: Lift the tilt angle  of 3277073_5 by 2 degrees
- `C7`: Increase A3 Offset threshold for 3277073_5 **← 정답**
- `C8`: Press down the tilt angle  of 3277073_5 by 2 degrees **← 정답**
- `C9`: Increase transmission power for 3229369_1
- `C10`: Lift the tilt angle of 3229369_1 by 4 degrees
- `C11`: Adjust the azimuth of 3277073_5 by 47 degrees
- `C12`: Decrease transmission power for 3277073_5 **← 정답**
- `C13`: Decrease A3 Offset threshold for 3229369_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Add neighbor relationship between 3229369_1 and 3277073_5
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277073_5
- `C17`: Press down the tilt angle of 3229369_1 by 4 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277073_5
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229369_1
- `C20`: Increase A3 Offset threshold for 3229369_1 **← 정답**
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229369_1
- `C22`: Adjust the azimuth of 3229369_1 by 19 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.590 | MS1 | 121.4656720046 | 31.1446211691 | 960 | 504990 | -84.51 | 13.69 | 600.24 | 0.16 | 2.63 | 1573 |
| 2024-09-20 22:21:32.833 | MS1 | 121.4656639607 | 31.1446320678 | 960 | 504990 | -83.95 | 16.09 | 469.31 | 0.06 | 2.17 | 1560 |
| 2024-09-20 22:21:33.272 | MS1 | 121.4656732014 | 31.1446315593 | 960 | 504990 | -77.13 | 14.14 | 359.52 | 0.07 | 2.35 | 1560 |
| 2024-09-20 22:21:34.406 | MS1 | 121.4656748528 | 31.1446375210 | 355 | 504990 | -85.25 | 4.75 | 46.57 | 0.20 | 1.32 | 1576 |
| 2024-09-20 22:21:35.838 | MS1 | 121.4656683122 | 31.1446308317 | 355 | 504990 | -81.97 | 4.38 | 59.15 | 0.10 | 1.28 | 1592 |
| 2024-09-20 22:21:36.533 | MS1 | 121.4656675223 | 31.1446275922 | 960 | 504990 | -88.35 | 1.90 | 62.40 | 0.14 | 1.35 | 1573 |
| 2024-09-20 22:21:37.972 | MS1 | 121.4656744167 | 31.1446355650 | 960 | 504990 | -89.79 | 1.86 | 58.55 | 0.17 | 1.08 | 1578 |
| 2024-09-20 22:21:38.881 | MS1 | 121.4656620375 | 31.1446377047 | 355 | 504990 | -82.94 | 4.04 | 39.42 | 0.20 | 1.34 | 1576 |
| 2024-09-20 22:21:39.421 | MS1 | 121.4656619186 | 31.1446340469 | 355 | 504990 | -84.14 | 1.73 | 62.35 | 0.13 | 1.00 | 1594 |
| 2024-09-20 22:21:40.471 | MS1 | 121.4656778165 | 31.1446318080 | 355 | 504990 | -81.43 | 15.18 | 307.52 | 0.15 | 2.43 | 1590 |
| 2024-09-20 22:21:41.384 | MS1 | 121.4656685617 | 31.1446313518 | 355 | 504990 | -76.93 | 14.51 | 561.26 | 0.11 | 2.98 | 1588 |
| 2024-09-20 22:21:42.715 | MS1 | 121.4656604408 | 31.1446214027 | 355 | 504990 | -84.83 | 12.25 | 552.88 | 0.13 | 2.37 | 1565 |

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
| 3229369 | 1 | 121.4687670487 | 31.1503835765 | 186 | 2 | 2 | 30.3 | TDD | 960 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3244227 | 2 | 121.4672901176 | 31.1496483826 | 297 | 10 | 11 | 26.5 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3249154 | 3 | 121.4722945896 | 31.1531135100 | 188 | 0 | 11 | 28.5 | TDD | 616 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3253385 | 4 | 121.4720578362 | 31.1464815985 | 108 | 4 | 7 | 45.1 | TDD | 877 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3277073 | 5 | 121.4725394983 | 31.1465432903 | 205 | 0 | 8 | 19.4 | TDD | 861 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.378 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.393 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.500 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.500 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.236 | NREventA3 | measId:2;ServCellPCI:7;Serv... |
| 2024-09-20 22:21:34.476 | NRHandoverAttempt | SourcePCI:7;SourceNR-ARFCN:... |
| 2024-09-20 22:21:34.516 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.528 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:34.629 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.629 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.236 | NREventA3 | measId:2;ServCellPCI:500;Se... |
| 2024-09-20 22:21:36.476 | NRHandoverAttempt | SourcePCI:500;SourceNR-ARFC... |
| 2024-09-20 22:21:36.515 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.525 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:36.660 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.660 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.236 | NREventA3 | measId:2;ServCellPCI:7;Serv... |
| 2024-09-20 22:21:38.476 | NRHandoverAttempt | SourcePCI:7;SourceNR-ARFCN:... |
| 2024-09-20 22:21:38.524 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.539 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.642 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.642 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229369 | 1 | 10.7174 | 10.5596 | -115.5292 | 5.1874 | 166.2658 | 0.0012 | 0.0045 |
| 2024_09_20 22:00 | 3244227 | 2 | 19.5517 | 14.0633 | -117.0243 | 14.6481 | 183.3132 | 0.0049 | 0.0008 |
| 2024_09_20 22:00 | 3249154 | 3 | 5.8583 | 17.8067 | -114.1865 | 16.0951 | 148.2578 | 0.0184 | 0.0182 |
| 2024_09_20 22:00 | 3253385 | 4 | 5.6524 | 9.1726 | -116.2171 | 7.8728 | 90.4326 | 0.0106 | 0.0040 |
| 2024_09_20 22:00 | 3277073 | 5 | 17.2123 | 14.9198 | -117.2494 | 15.0807 | 173.9833 | 0.0068 | 0.0017 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412652_E27D11AA | 504990 | 355 | -85.2 | 504990 | 960 | -83.3 | 504990 | 861 | -85.6 | 504990 | 877 |
| MR_1774412652_69DBFE34 | 504990 | 960 | -85.6 | 504990 | 355 | -84.7 | 504990 | 861 | -84.4 | 504990 | 877 |
| MR_1774412652_1CE4D92E | 504990 | 355 | -87.0 | 504990 | 960 | -85.4 | 504990 | 861 | -87.6 | 504990 | 877 |
| MR_1774412652_18FEA5A5 | 504990 | 960 | -85.2 | 504990 | 355 | -83.1 | 504990 | 861 | -86.8 | 504990 | 877 |
| MR_1774412652_B2ACDD9F | 504990 | 355 | -86.6 | 504990 | 960 | -83.6 | 504990 | 861 | -87.8 | 504990 | 877 |
| MR_1774412652_3E27CEF9 | 504990 | 960 | -84.6 | 504990 | 355 | -85.9 | 504990 | 861 | -87.6 | 504990 | 877 |
| MR_1774412652_6F5D4B9C | 504990 | 355 | -86.8 | 504990 | 960 | -82.7 | 504990 | 861 | -87.5 | 504990 | 877 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1279: `fcddc2fe-866...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fcddc2fe-8669-4eea-9c89-e32a70c628e3` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Add neighbor relationship between 3231189_1 and 3247342_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1279] topology](images/train_1279.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247342_3
- `C2`: Increase transmission power for 3231189_1
- `C3`: Check test server and transmission issues
- `C4`: Adjust the azimuth of 3247342_3 by 48 degrees
- `C5`: Decrease transmission power for 3231189_1
- `C6`: Add neighbor relationship between 3231076_4 and 3247342_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231189_1
- `C8`: Lift the tilt angle  of 3247342_3 by 2 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Adjust the azimuth of 3231189_1 by 50 degrees
- `C11`: Lift the tilt angle of 3231189_1 by 6 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231189_1
- `C13`: Decrease transmission power for 3247342_3
- `C14`: Increase A3 Offset threshold for 3231189_1
- `C15`: Increase A3 Offset threshold for 3247342_3
- `C16`: Increase transmission power for 3247342_3
- `C17`: Press down the tilt angle  of 3247342_3 by 2 degrees
- `C18`: Press down the tilt angle of 3231189_1 by 6 degrees
- `C19`: Add neighbor relationship between 3231189_1 and 3247342_3 **← 정답**
- `C20`: Decrease A3 Offset threshold for 3247342_3
- `C21`: Decrease A3 Offset threshold for 3231189_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247342_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.650 | MS1 | 121.4656777238 | 31.1446345870 | 361 | 504990 | -81.08 | 17.08 | 561.95 | 0.20 | 2.98 | 1595 |
| 2024-09-20 22:21:32.283 | MS1 | 121.4656580266 | 31.1446196094 | 361 | 504990 | -84.65 | 14.80 | 570.79 | 0.04 | 2.77 | 1563 |
| 2024-09-20 22:21:33.337 | MS1 | 121.4656707060 | 31.1446321005 | 361 | 504990 | -76.67 | 16.15 | 471.76 | 0.16 | 2.22 | 1576 |
| 2024-09-20 22:21:34.320 | MS1 | 121.4656662746 | 31.1446261302 | 361 | 504990 | -91.97 | -1.31 | 60.44 | 0.14 | 1.33 | 1567 |
| 2024-09-20 22:21:35.131 | MS1 | 121.4656593509 | 31.1446316840 | 361 | 504990 | -85.44 | -1.34 | 65.79 | 0.17 | 1.47 | 1565 |
| 2024-09-20 22:21:36.397 | MS1 | 121.4656722598 | 31.1446365093 | 361 | 504990 | -93.92 | -0.04 | 29.52 | 0.11 | 1.06 | 1586 |
| 2024-09-20 22:21:37.686 | MS1 | 121.4656765357 | 31.1446307363 | 361 | 504990 | -88.05 | -0.37 | 68.37 | 0.06 | 1.21 | 1598 |
| 2024-09-20 22:21:38.951 | MS1 | 121.4656659184 | 31.1446331740 | 361 | 504990 | -78.11 | 13.52 | 512.91 | 0.00 | 1.04 | 1563 |
| 2024-09-20 22:21:39.495 | MS1 | 121.4656714199 | 31.1446312105 | 361 | 504990 | -83.06 | 16.98 | 457.93 | 0.15 | 1.27 | 1589 |
| 2024-09-20 22:21:40.668 | MS1 | 121.4656610279 | 31.1446191871 | 361 | 504990 | -80.92 | 13.20 | 565.48 | 0.01 | 2.17 | 1568 |
| 2024-09-20 22:21:41.168 | MS1 | 121.4656761204 | 31.1446265062 | 361 | 504990 | -78.73 | 16.73 | 582.28 | 0.02 | 2.79 | 1592 |
| 2024-09-20 22:21:42.630 | MS1 | 121.4656663527 | 31.1446198399 | 361 | 504990 | -78.51 | 16.75 | 546.77 | 0.04 | 2.63 | 1563 |

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
| 3212420 | 2 | 121.4666291305 | 31.1505742513 | 19 | 10 | 0 | 17.1 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3231076 | 4 | 121.4718595332 | 31.1541008126 | 69 | 7 | 7 | 35.9 | TDD | 175 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3231189 | 1 | 121.4746687013 | 31.1484998399 | 46 | 4 | 3 | 28.1 | TDD | 361 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3247342 | 3 | 121.4713741539 | 31.1520114477 | 261 | 0 | 2 | 33.8 | TDD | 420 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.622 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.641 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.765 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.765 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.477 | NREventA3 | measId:2;ServCellPCI:598;Se... |
| 2024-09-20 22:21:36.477 | NREventA3 | measId:2;ServCellPCI:598;Se... |
| 2024-09-20 22:21:37.477 | NREventA3 | measId:2;ServCellPCI:598;Se... |
| 2024-09-20 22:21:39.977 | NRRRCReestablishAttempt | PCI:598 |
| 2024-09-20 22:21:39.996 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:40.010 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:40.146 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.146 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231189 | 1 | 15.7208 | 17.4363 | -117.1894 | 19.1601 | 159.8258 | 0.0108 | 0.1817 |
| 2024_09_20 22:00 | 3212420 | 2 | 11.0409 | 12.2297 | -114.3803 | 9.3417 | 114.8639 | 0.0097 | 0.0098 |
| 2024_09_20 22:00 | 3247342 | 3 | 12.4200 | 10.4792 | -115.4516 | 10.7641 | 195.0104 | 0.0007 | 0.0049 |
| 2024_09_20 22:00 | 3231076 | 4 | 8.4177 | 10.6731 | -116.7330 | 9.2200 | 151.0915 | 0.0160 | 0.0047 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412355_07280DEF | 504990 | 361 | -92.3 | 504990 | 420 | -86.2 | 504990 | 175 | -89.1 | 504990 | 129 |
| MR_1774412355_4624DA9F | 504990 | 420 | -85.6 | 504990 | 361 | -90.5 | 504990 | 175 | -90.7 | 504990 | 129 |
| MR_1774412355_657FC0DB | 504990 | 361 | -93.8 | 504990 | 420 | -85.8 | 504990 | 175 | -90.9 | 504990 | 129 |
| MR_1774412355_28B51484 | 504990 | 420 | -88.3 | 504990 | 361 | -92.9 | 504990 | 175 | -91.6 | 504990 | 129 |
| MR_1774412355_1D26AB18 | 504990 | 361 | -93.7 | 504990 | 420 | -86.3 | 504990 | 175 | -89.3 | 504990 | 129 |

> *... 2개 열 생략 (전체 14열)*

---
