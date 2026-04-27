# Track A 문제 분석 — train[90]~train[99]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[90] ~ train[99] (10개)

## 목차

1. [문제 90: `2077b531-820...`](#90) — multiple-answer, 정답: C4|C20
2. [문제 91: `5fe1fbf2-618...`](#91) — single-answer, 정답: C20
3. [문제 92: `e54d2633-e5c...`](#92) — single-answer, 정답: C2
4. [문제 93: `60725196-a86...`](#93) — multiple-answer, 정답: C2|C11|C20|C21
5. [문제 94: `bd8bc770-d34...`](#94) — multiple-answer, 정답: C1|C4
6. [문제 95: `8ee445e0-4e3...`](#95) — single-answer, 정답: C12
7. [문제 96: `f2f956b8-5c3...`](#96) — single-answer, 정답: C20
8. [문제 97: `5f3561be-766...`](#97) — single-answer, 정답: C2
9. [문제 98: `638dd303-b78...`](#98) — single-answer, 정답: C11
10. [문제 99: `329d9b23-9cc...`](#99) — single-answer, 정답: C17

---

### 문제 90: `2077b531-820...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2077b531-8209-4074-88b8-a032588fbae7` |
| Tag | **multiple-answer** |
| 정답 | **C4|C20** |
| C4 의미 | Decrease transmission power for 3263007_2 |
| C20 의미 | Press down the tilt angle  of 3263007_2 by 5 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[90] topology](images/train_0090.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3268968_3 and 3263007_2
- `C2`: Press down the tilt angle of 3268968_3 by 5 degrees
- `C3`: Increase transmission power for 3268968_3
- `C4`: Decrease transmission power for 3263007_2 **← 정답**
- `C5`: Check test server and transmission issues
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268968_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268968_3
- `C8`: Lift the tilt angle of 3268968_3 by 5 degrees
- `C9`: Lift the tilt angle  of 3263007_2 by 5 degrees
- `C10`: Decrease transmission power for 3268968_3
- `C11`: Decrease A3 Offset threshold for 3263007_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Adjust the azimuth of 3263007_2 by 26 degrees
- `C14`: Decrease A3 Offset threshold for 3268968_3
- `C15`: Increase transmission power for 3263007_2
- `C16`: Adjust the azimuth of 3268968_3 by 30 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263007_2
- `C18`: Increase A3 Offset threshold for 3268968_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263007_2
- `C20`: Press down the tilt angle  of 3263007_2 by 5 degrees **← 정답**
- `C21`: Add neighbor relationship between 3223932_1 and 3263007_2
- `C22`: Increase A3 Offset threshold for 3263007_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.966 | MS1 | 121.4656720086 | 31.1446290577 | 636 | 504990 | -78.23 | 12.87 | 390.92 | 0.19 | 2.74 | 1577 |
| 2024-09-20 22:21:32.965 | MS1 | 121.4656658437 | 31.1446328604 | 636 | 504990 | -84.41 | 16.74 | 553.40 | 0.07 | 2.76 | 1572 |
| 2024-09-20 22:21:33.136 | MS1 | 121.4656640609 | 31.1446377314 | 636 | 504990 | -82.98 | 12.24 | 448.99 | 0.17 | 2.02 | 1580 |
| 2024-09-20 22:21:34.581 | MS1 | 121.4656740948 | 31.1446372335 | 636 | 504990 | -85.43 | 2.01 | 64.06 | 0.14 | 1.17 | 1592 |
| 2024-09-20 22:21:35.345 | MS1 | 121.4656678921 | 31.1446287569 | 636 | 504990 | -93.58 | 3.36 | 84.45 | 0.07 | 1.16 | 1589 |
| 2024-09-20 22:21:36.338 | MS1 | 121.4656702768 | 31.1446194911 | 636 | 504990 | -88.14 | 2.06 | 64.87 | 0.17 | 1.24 | 1573 |
| 2024-09-20 22:21:37.657 | MS1 | 121.4656756380 | 31.1446261113 | 636 | 504990 | -90.40 | 2.03 | 48.07 | 0.11 | 1.03 | 1589 |
| 2024-09-20 22:21:38.336 | MS1 | 121.4656746882 | 31.1446194060 | 636 | 504990 | -91.25 | 0.90 | 71.93 | 0.04 | 1.48 | 1582 |
| 2024-09-20 22:21:39.414 | MS1 | 121.4656672567 | 31.1446333225 | 636 | 504990 | -93.17 | 0.06 | 41.30 | 0.14 | 1.20 | 1600 |
| 2024-09-20 22:21:40.606 | MS1 | 121.4656745891 | 31.1446216966 | 636 | 504990 | -83.24 | 12.79 | 508.80 | 0.03 | 2.10 | 1589 |
| 2024-09-20 22:21:41.380 | MS1 | 121.4656737759 | 31.1446263649 | 636 | 504990 | -76.79 | 16.98 | 543.77 | 0.09 | 2.97 | 1580 |
| 2024-09-20 22:21:42.424 | MS1 | 121.4656688066 | 31.1446217385 | 636 | 504990 | -77.17 | 15.80 | 354.29 | 0.18 | 2.62 | 1588 |

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
| 3223932 | 1 | 121.4758400370 | 31.1507610033 | 292 | 5 | 5 | 47.1 | TDD | 825 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3239036 | 4 | 121.4736864387 | 31.1441649021 | 339 | 6 | 8 | 32.0 | TDD | 245 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3263007 | 2 | 121.4731210218 | 31.1518762611 | 247 | 3 | 7 | 39.9 | TDD | 347 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3268968 | 3 | 121.4667218305 | 31.1512691255 | 218 | 1 | 2 | 47.7 | TDD | 636 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.430 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.453 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.563 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.563 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223932 | 1 | 6.5246 | 14.2514 | -114.5054 | 16.0471 | 192.9420 | 0.0110 | 0.0139 |
| 2024_09_20 22:00 | 3263007 | 2 | 6.9322 | 10.7843 | -115.2763 | 18.6598 | 131.4993 | 0.0065 | 0.0029 |
| 2024_09_20 22:00 | 3268968 | 3 | 15.0661 | 6.4243 | -109.9226 | 19.8937 | 147.7631 | 0.0159 | 0.0072 |
| 2024_09_20 22:00 | 3239036 | 4 | 6.4618 | 15.3750 | -114.2511 | 6.3588 | 126.2977 | 0.0021 | 0.0115 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412525_E63A1588 | 504990 | 636 | -85.4 | 504990 | 347 | -82.7 | 504990 | 825 | -81.5 | 504990 | 245 |
| MR_1774412525_33725ABC | 504990 | 347 | -84.3 | 504990 | 636 | -81.7 | 504990 | 825 | -83.1 | 504990 | 245 |
| MR_1774412525_F586A3E5 | 504990 | 636 | -85.2 | 504990 | 347 | -79.8 | 504990 | 825 | -83.3 | 504990 | 245 |
| MR_1774412525_B06FE776 | 504990 | 347 | -83.6 | 504990 | 636 | -81.9 | 504990 | 825 | -81.0 | 504990 | 245 |
| MR_1774412525_361E1786 | 504990 | 636 | -86.9 | 504990 | 347 | -82.2 | 504990 | 825 | -80.7 | 504990 | 245 |
| MR_1774412525_F70BB1D4 | 504990 | 347 | -86.6 | 504990 | 636 | -81.1 | 504990 | 825 | -81.1 | 504990 | 245 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 91: `5fe1fbf2-618...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5fe1fbf2-618a-4452-98b7-abe81185c47c` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[91] topology](images/train_0091.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3261006_4
- `C2`: Increase A3 Offset threshold for 3239615_2
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Press down the tilt angle of 3239615_2 by 9 degrees
- `C5`: Increase A3 Offset threshold for 3261006_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239615_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239615_2
- `C8`: Decrease A3 Offset threshold for 3261006_4
- `C9`: Increase transmission power for 3239615_2
- `C10`: Adjust the azimuth of 3239615_2 by 50 degrees
- `C11`: Decrease transmission power for 3261006_4
- `C12`: Adjust the azimuth of 3261006_4 by 8 degrees
- `C13`: Decrease A3 Offset threshold for 3239615_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261006_4
- `C15`: Add neighbor relationship between 3239615_2 and 3261006_4
- `C16`: Decrease transmission power for 3239615_2
- `C17`: Press down the tilt angle  of 3261006_4 by 10 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261006_4
- `C19`: Lift the tilt angle  of 3261006_4 by 10 degrees
- `C20`: Check test server and transmission issues **← 정답**
- `C21`: Lift the tilt angle of 3239615_2 by 9 degrees
- `C22`: Add neighbor relationship between 3228121_1 and 3261006_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.312 | MS1 | 121.4656656731 | 31.1446243532 | 427 | 504990 | -87.89 | 14.16 | 457.49 | 0.07 | 2.22 | 1584 |
| 2024-09-20 22:21:32.509 | MS1 | 121.4656680107 | 31.1446242033 | 427 | 504990 | -85.19 | 17.43 | 415.71 | 0.00 | 2.94 | 1589 |
| 2024-09-20 22:21:33.995 | MS1 | 121.4656657237 | 31.1446302667 | 427 | 504990 | -90.09 | 15.72 | 542.89 | 0.16 | 2.22 | 1574 |
| 2024-09-20 22:21:34.866 | MS1 | 121.4656618134 | 31.1446267197 | 427 | 504990 | -86.97 | 12.99 | 94.70 | 0.13 | 2.80 | 356 |
| 2024-09-20 22:21:35.988 | MS1 | 121.4656642987 | 31.1446209105 | 427 | 504990 | -89.93 | 17.13 | 76.73 | 0.07 | 2.14 | 311 |
| 2024-09-20 22:21:36.896 | MS1 | 121.4656740475 | 31.1446317990 | 427 | 504990 | -87.18 | 13.57 | 58.96 | 0.11 | 2.38 | 318 |
| 2024-09-20 22:21:37.726 | MS1 | 121.4656773718 | 31.1446221698 | 427 | 504990 | -91.20 | 12.98 | 94.68 | 0.08 | 2.51 | 444 |
| 2024-09-20 22:21:38.117 | MS1 | 121.4656710742 | 31.1446261138 | 427 | 504990 | -92.76 | 11.47 | 78.83 | 0.06 | 2.87 | 499 |
| 2024-09-20 22:21:39.321 | MS1 | 121.4656612113 | 31.1446229086 | 427 | 504990 | -92.70 | 12.87 | 55.45 | 0.16 | 2.19 | 347 |
| 2024-09-20 22:21:40.731 | MS1 | 121.4656661391 | 31.1446269575 | 427 | 504990 | -93.95 | 8.00 | 431.13 | 0.10 | 2.26 | 1571 |
| 2024-09-20 22:21:41.175 | MS1 | 121.4656694270 | 31.1446286382 | 427 | 504990 | -92.56 | 11.66 | 427.75 | 0.18 | 2.39 | 1586 |
| 2024-09-20 22:21:42.231 | MS1 | 121.4656739660 | 31.1446281304 | 427 | 504990 | -91.46 | 12.25 | 495.59 | 0.01 | 2.93 | 1592 |

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
| 3215934 | 3 | 121.4736138515 | 31.1536243564 | 41 | 8 | 10 | 32.7 | TDD | 52 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3228121 | 1 | 121.4690890918 | 31.1557225312 | 104 | 9 | 10 | 48.2 | TDD | 73 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3239615 | 2 | 121.4731817291 | 31.1535841286 | 110 | 7 | 8 | 33.2 | TDD | 427 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3261006 | 4 | 121.4685458512 | 31.1440045437 | 276 | 10 | 11 | 44.9 | TDD | 691 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.144 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.169 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.305 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.305 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.968 | NREventA3 | measId:2;ServCellPCI:14;Ser... |
| 2024-09-20 22:21:38.208 | NRHandoverAttempt | SourcePCI:14;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.248 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.259 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.391 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.391 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228121 | 1 | 12.7882 | 14.8485 | -115.6239 | 19.1608 | 199.9980 | 0.0001 | 0.0144 |
| 2024_09_20 22:00 | 3239615 | 2 | 13.8815 | 19.7681 | -115.3466 | 18.3170 | 142.6010 | 0.0186 | 0.0167 |
| 2024_09_20 22:00 | 3215934 | 3 | 11.9831 | 10.3465 | -116.9934 | 9.5539 | 182.0775 | 0.0057 | 0.0071 |
| 2024_09_20 22:00 | 3261006 | 4 | 7.4302 | 5.0183 | -115.7663 | 14.0592 | 142.4361 | 0.0050 | 0.0128 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412915_FC843AFF | 504990 | 427 | -86.6 | 504990 | 691 | -88.1 | 504990 | 73 | -100.5 | 504990 | 52 |
| MR_1774412915_DE88ACFF | 504990 | 427 | -85.1 | 504990 | 691 | -89.4 | 504990 | 73 | -98.1 | 504990 | 52 |
| MR_1774412915_AA451B8E | 504990 | 427 | -85.9 | 504990 | 691 | -85.8 | 504990 | 73 | -99.3 | 504990 | 52 |
| MR_1774412915_82F39130 | 504990 | 427 | -88.3 | 504990 | 691 | -85.6 | 504990 | 73 | -99.5 | 504990 | 52 |
| MR_1774412915_D1D1740D | 504990 | 427 | -85.0 | 504990 | 691 | -88.6 | 504990 | 73 | -98.5 | 504990 | 52 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 92: `e54d2633-e5c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e54d2633-e5c1-4fc6-813b-0a5a40e75349` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[92] topology](images/train_0092.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242297_3
- `C2`: Check test server and transmission issues **← 정답**
- `C3`: Increase transmission power for 3273178_1
- `C4`: Decrease A3 Offset threshold for 3242297_3
- `C5`: Press down the tilt angle  of 3273178_1 by 10 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273178_1
- `C7`: Lift the tilt angle  of 3273178_1 by 10 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase transmission power for 3242297_3
- `C10`: Add neighbor relationship between 3239559_4 and 3273178_1
- `C11`: Increase A3 Offset threshold for 3242297_3
- `C12`: Press down the tilt angle of 3242297_3 by 6 degrees
- `C13`: Increase A3 Offset threshold for 3273178_1
- `C14`: Add neighbor relationship between 3242297_3 and 3273178_1
- `C15`: Decrease transmission power for 3242297_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273178_1
- `C17`: Adjust the azimuth of 3242297_3 by 50 degrees
- `C18`: Adjust the azimuth of 3273178_1 by 4 degrees
- `C19`: Lift the tilt angle of 3242297_3 by 6 degrees
- `C20`: Decrease transmission power for 3273178_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242297_3
- `C22`: Decrease A3 Offset threshold for 3273178_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.644 | MS1 | 121.4656595243 | 31.1446230838 | 965 | 504990 | -86.00 | 13.88 | 488.74 | 0.18 | 2.19 | 1583 |
| 2024-09-20 22:21:32.279 | MS1 | 121.4656702066 | 31.1446243254 | 965 | 504990 | -88.49 | 14.26 | 325.35 | 0.08 | 2.40 | 1573 |
| 2024-09-20 22:21:33.129 | MS1 | 121.4656658308 | 31.1446301712 | 965 | 504990 | -88.97 | 12.01 | 379.39 | 0.14 | 2.19 | 1597 |
| 2024-09-20 22:21:34.924 | MS1 | 121.4656610153 | 31.1446329732 | 965 | 504990 | -88.35 | 16.75 | 60.85 | 0.12 | 2.88 | 441 |
| 2024-09-20 22:21:35.315 | MS1 | 121.4656648852 | 31.1446327318 | 965 | 504990 | -88.75 | 12.83 | 57.70 | 0.09 | 2.54 | 314 |
| 2024-09-20 22:21:36.707 | MS1 | 121.4656754263 | 31.1446340182 | 965 | 504990 | -89.47 | 15.84 | 80.08 | 0.19 | 2.23 | 323 |
| 2024-09-20 22:21:37.118 | MS1 | 121.4656627981 | 31.1446299784 | 965 | 504990 | -93.20 | 9.79 | 92.56 | 0.01 | 2.94 | 441 |
| 2024-09-20 22:21:38.380 | MS1 | 121.4656709922 | 31.1446347047 | 965 | 504990 | -91.01 | 8.67 | 89.68 | 0.19 | 2.53 | 406 |
| 2024-09-20 22:21:39.907 | MS1 | 121.4656647684 | 31.1446323814 | 965 | 504990 | -92.20 | 12.28 | 62.03 | 0.10 | 2.21 | 371 |
| 2024-09-20 22:21:40.414 | MS1 | 121.4656709366 | 31.1446220882 | 965 | 504990 | -92.14 | 10.00 | 553.19 | 0.02 | 2.33 | 1592 |
| 2024-09-20 22:21:41.952 | MS1 | 121.4656740783 | 31.1446337485 | 965 | 504990 | -89.81 | 11.53 | 377.30 | 0.14 | 2.14 | 1575 |
| 2024-09-20 22:21:42.932 | MS1 | 121.4656606145 | 31.1446327583 | 965 | 504990 | -92.04 | 7.37 | 443.66 | 0.09 | 2.99 | 1564 |

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
| 3230540 | 2 | 121.4682541475 | 31.1462392108 | 210 | 6 | 11 | 34.8 | TDD | 818 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3239559 | 4 | 121.4747483381 | 31.1455581631 | 262 | 0 | 5 | 44.4 | TDD | 865 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3242297 | 3 | 121.4675256458 | 31.1485788538 | 344 | 1 | 2 | 43.0 | TDD | 965 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3273178 | 1 | 121.4679129332 | 31.1536789012 | 196 | 7 | 11 | 47.7 | TDD | 529 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.371 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.395 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.524 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.524 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.216 | NREventA3 | measId:2;ServCellPCI:35;Ser... |
| 2024-09-20 22:21:38.456 | NRHandoverAttempt | SourcePCI:35;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.504 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.516 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.622 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.622 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273178 | 1 | 15.8419 | 13.1186 | -117.2483 | 14.0250 | 187.3705 | 0.0046 | 0.0039 |
| 2024_09_20 22:00 | 3230540 | 2 | 17.3167 | 14.3100 | -116.6896 | 13.6626 | 92.6952 | 0.0184 | 0.0132 |
| 2024_09_20 22:00 | 3242297 | 3 | 7.4629 | 5.9072 | -117.2634 | 18.6237 | 196.0619 | 0.0131 | 0.0107 |
| 2024_09_20 22:00 | 3239559 | 4 | 8.0621 | 14.4906 | -114.0109 | 11.9613 | 87.9131 | 0.0150 | 0.0048 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412545_FAF5B551 | 504990 | 965 | -87.5 | 504990 | 529 | -92.1 | 504990 | 865 | -95.0 | 504990 | 818 |
| MR_1774412545_12956EFB | 504990 | 965 | -86.8 | 504990 | 529 | -89.4 | 504990 | 865 | -95.3 | 504990 | 818 |
| MR_1774412545_DC91075A | 504990 | 965 | -89.6 | 504990 | 529 | -92.1 | 504990 | 865 | -95.8 | 504990 | 818 |
| MR_1774412545_9D779910 | 504990 | 965 | -89.1 | 504990 | 529 | -89.5 | 504990 | 865 | -95.3 | 504990 | 818 |
| MR_1774412545_F0587145 | 504990 | 965 | -89.2 | 504990 | 529 | -91.2 | 504990 | 865 | -94.2 | 504990 | 818 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 93: `60725196-a86...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `60725196-a864-4d24-97d2-3ed06582f9a6` |
| Tag | **multiple-answer** |
| 정답 | **C2|C11|C20|C21** |
| C2 의미 | Decrease transmission power for 3218518_1 |
| C11 의미 | Increase A3 Offset threshold for 3218518_1 |
| C20 의미 | Press down the tilt angle  of 3218518_1 by 3 degrees |
| C21 의미 | Increase A3 Offset threshold for 3279337_4 |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[93] topology](images/train_0093.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3218518_1 by 28 degrees
- `C2`: Decrease transmission power for 3218518_1 **← 정답**
- `C3`: Adjust the azimuth of 3279337_4 by 23 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279337_4
- `C5`: Lift the tilt angle  of 3218518_1 by 3 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218518_1
- `C7`: Add neighbor relationship between 3279337_4 and 3218518_1
- `C8`: Press down the tilt angle of 3279337_4 by 6 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218518_1
- `C10`: Decrease transmission power for 3279337_4
- `C11`: Increase A3 Offset threshold for 3218518_1 **← 정답**
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279337_4
- `C13`: Increase transmission power for 3279337_4
- `C14`: Decrease A3 Offset threshold for 3218518_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Lift the tilt angle of 3279337_4 by 6 degrees
- `C17`: Decrease A3 Offset threshold for 3279337_4
- `C18`: Increase transmission power for 3218518_1
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle  of 3218518_1 by 3 degrees **← 정답**
- `C21`: Increase A3 Offset threshold for 3279337_4 **← 정답**
- `C22`: Add neighbor relationship between 3235462_2 and 3218518_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.590 | MS1 | 121.4656775026 | 31.1446315846 | 240 | 504990 | -81.48 | 14.32 | 594.22 | 0.02 | 2.00 | 1583 |
| 2024-09-20 22:21:32.605 | MS1 | 121.4656724690 | 31.1446334432 | 240 | 504990 | -78.57 | 12.95 | 421.32 | 0.08 | 2.28 | 1577 |
| 2024-09-20 22:21:33.678 | MS1 | 121.4656655262 | 31.1446235804 | 240 | 504990 | -82.70 | 16.17 | 464.96 | 0.12 | 2.41 | 1589 |
| 2024-09-20 22:21:34.200 | MS1 | 121.4656671694 | 31.1446328639 | 561 | 504990 | -81.27 | 3.97 | 75.48 | 0.20 | 1.43 | 1577 |
| 2024-09-20 22:21:35.987 | MS1 | 121.4656740599 | 31.1446214183 | 561 | 504990 | -85.63 | 3.09 | 49.06 | 0.18 | 1.22 | 1595 |
| 2024-09-20 22:21:36.249 | MS1 | 121.4656653765 | 31.1446363710 | 240 | 504990 | -85.64 | 1.87 | 43.08 | 0.08 | 1.21 | 1595 |
| 2024-09-20 22:21:37.167 | MS1 | 121.4656660657 | 31.1446318318 | 240 | 504990 | -81.43 | 2.87 | 53.34 | 0.07 | 1.12 | 1591 |
| 2024-09-20 22:21:38.514 | MS1 | 121.4656679779 | 31.1446235874 | 561 | 504990 | -81.49 | 4.95 | 68.36 | 0.15 | 1.36 | 1596 |
| 2024-09-20 22:21:39.274 | MS1 | 121.4656737382 | 31.1446331829 | 561 | 504990 | -88.13 | 4.94 | 55.27 | 0.01 | 1.48 | 1566 |
| 2024-09-20 22:21:40.236 | MS1 | 121.4656607409 | 31.1446295863 | 561 | 504990 | -81.48 | 15.31 | 412.14 | 0.20 | 2.35 | 1574 |
| 2024-09-20 22:21:41.439 | MS1 | 121.4656758161 | 31.1446311629 | 561 | 504990 | -75.64 | 12.28 | 363.09 | 0.09 | 2.46 | 1576 |
| 2024-09-20 22:21:42.928 | MS1 | 121.4656730723 | 31.1446193085 | 561 | 504990 | -76.40 | 17.59 | 366.40 | 0.11 | 2.62 | 1574 |

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
| 3218518 | 1 | 121.4697019160 | 31.1520435623 | 177 | 2 | 10 | 20.5 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3235462 | 2 | 121.4695350363 | 31.1468613939 | 32 | 0 | 9 | 35.0 | TDD | 707 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3236670 | 5 | 121.4658411482 | 31.1535412829 | 27 | 4 | 8 | 32.0 | TDD | 561 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3245975 | 3 | 121.4745475259 | 31.1473763647 | 318 | 0 | 7 | 19.0 | TDD | 646 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3279337 | 4 | 121.4666746423 | 31.1479543735 | 218 | 1 | 11 | 32.5 | TDD | 240 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.866 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.888 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.032 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.032 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.680 | NREventA3 | measId:2;ServCellPCI:435;Se... |
| 2024-09-20 22:21:33.920 | NRHandoverAttempt | SourcePCI:435;SourceNR-ARFC... |
| 2024-09-20 22:21:33.965 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:33.979 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:34.106 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.106 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.680 | NREventA3 | measId:2;ServCellPCI:8;Serv... |
| 2024-09-20 22:21:35.920 | NRHandoverAttempt | SourcePCI:8;SourceNR-ARFCN:... |
| 2024-09-20 22:21:35.955 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.969 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.102 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.102 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.680 | NREventA3 | measId:2;ServCellPCI:435;Se... |
| 2024-09-20 22:21:37.920 | NRHandoverAttempt | SourcePCI:435;SourceNR-ARFC... |
| 2024-09-20 22:21:37.954 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.966 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.095 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.095 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218518 | 1 | 14.2787 | 14.2620 | -115.4503 | 16.6170 | 177.3857 | 0.0144 | 0.0081 |
| 2024_09_20 22:00 | 3235462 | 2 | 16.9656 | 12.5327 | -114.6439 | 8.6937 | 128.4819 | 0.0130 | 0.0134 |
| 2024_09_20 22:00 | 3245975 | 3 | 17.2702 | 14.7905 | -115.1597 | 17.7132 | 130.1803 | 0.0090 | 0.0033 |
| 2024_09_20 22:00 | 3279337 | 4 | 13.0886 | 19.4097 | -114.2564 | 10.6978 | 186.1831 | 0.0034 | 0.0105 |
| 2024_09_20 22:00 | 3236670 | 5 | 11.1460 | 14.3946 | -116.4664 | 13.1189 | 98.8439 | 0.0090 | 0.0119 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414391_37AB0D2B | 504990 | 561 | -80.4 | 504990 | 240 | -84.1 | 504990 | 866 | -84.5 | 504990 | 707 |
| MR_1774414391_3A1C95D0 | 504990 | 561 | -79.6 | 504990 | 240 | -84.0 | 504990 | 866 | -84.8 | 504990 | 707 |
| MR_1774414391_12694BA6 | 504990 | 561 | -81.4 | 504990 | 240 | -83.0 | 504990 | 866 | -85.1 | 504990 | 707 |
| MR_1774414391_9F1F7435 | 504990 | 561 | -82.5 | 504990 | 240 | -82.0 | 504990 | 866 | -88.3 | 504990 | 707 |
| MR_1774414391_6F496FA6 | 504990 | 240 | -81.0 | 504990 | 561 | -83.4 | 504990 | 866 | -87.6 | 504990 | 707 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 94: `bd8bc770-d34...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bd8bc770-d341-4ef1-8ae6-27be09ccc924` |
| Tag | **multiple-answer** |
| 정답 | **C1|C4** |
| C1 의미 | Decrease transmission power for 3219975_3 |
| C4 의미 | Press down the tilt angle  of 3219975_3 by 6 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[94] topology](images/train_0094.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3219975_3 **← 정답**
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270723_4
- `C3`: Increase transmission power for 3270723_4
- `C4`: Press down the tilt angle  of 3219975_3 by 6 degrees **← 정답**
- `C5`: Check test server and transmission issues
- `C6`: Decrease A3 Offset threshold for 3219975_3
- `C7`: Lift the tilt angle  of 3219975_3 by 6 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270723_4
- `C9`: Press down the tilt angle of 3270723_4 by 4 degrees
- `C10`: Add neighbor relationship between 3227487_1 and 3219975_3
- `C11`: Increase A3 Offset threshold for 3219975_3
- `C12`: Increase transmission power for 3219975_3
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Adjust the azimuth of 3219975_3 by 4 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219975_3
- `C16`: Decrease transmission power for 3270723_4
- `C17`: Increase A3 Offset threshold for 3270723_4
- `C18`: Decrease A3 Offset threshold for 3270723_4
- `C19`: Adjust the azimuth of 3270723_4 by 7 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219975_3
- `C21`: Add neighbor relationship between 3270723_4 and 3219975_3
- `C22`: Lift the tilt angle of 3270723_4 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.588 | MS1 | 121.4656735053 | 31.1446259459 | 391 | 504990 | -76.73 | 17.55 | 357.55 | 0.04 | 2.44 | 1576 |
| 2024-09-20 22:21:32.294 | MS1 | 121.4656582859 | 31.1446266792 | 391 | 504990 | -84.54 | 16.64 | 313.28 | 0.19 | 2.47 | 1574 |
| 2024-09-20 22:21:33.364 | MS1 | 121.4656703945 | 31.1446225041 | 391 | 504990 | -78.86 | 16.96 | 411.55 | 0.12 | 2.30 | 1564 |
| 2024-09-20 22:21:34.116 | MS1 | 121.4656587518 | 31.1446261938 | 391 | 504990 | -91.83 | 2.28 | 40.72 | 0.07 | 1.34 | 1569 |
| 2024-09-20 22:21:35.370 | MS1 | 121.4656630171 | 31.1446211789 | 391 | 504990 | -87.89 | 3.07 | 71.87 | 0.08 | 1.23 | 1599 |
| 2024-09-20 22:21:36.868 | MS1 | 121.4656761898 | 31.1446283444 | 391 | 504990 | -89.73 | 2.07 | 65.86 | 0.05 | 1.06 | 1569 |
| 2024-09-20 22:21:37.550 | MS1 | 121.4656673241 | 31.1446235063 | 391 | 504990 | -85.11 | 3.29 | 50.57 | 0.19 | 1.06 | 1564 |
| 2024-09-20 22:21:38.120 | MS1 | 121.4656767702 | 31.1446365334 | 391 | 504990 | -94.86 | 1.82 | 46.41 | 0.08 | 1.34 | 1573 |
| 2024-09-20 22:21:39.882 | MS1 | 121.4656589304 | 31.1446346397 | 391 | 504990 | -91.20 | 0.51 | 39.02 | 0.11 | 1.44 | 1576 |
| 2024-09-20 22:21:40.194 | MS1 | 121.4656639934 | 31.1446222073 | 391 | 504990 | -83.46 | 13.23 | 559.56 | 0.07 | 2.64 | 1572 |
| 2024-09-20 22:21:41.412 | MS1 | 121.4656644452 | 31.1446201715 | 391 | 504990 | -84.22 | 15.65 | 419.08 | 0.06 | 2.13 | 1560 |
| 2024-09-20 22:21:42.448 | MS1 | 121.4656639370 | 31.1446225167 | 391 | 504990 | -78.19 | 15.19 | 596.90 | 0.04 | 2.76 | 1570 |

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
| 3219975 | 3 | 121.4667664466 | 31.1489462401 | 188 | 0 | 1 | 49.8 | TDD | 570 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3227487 | 1 | 121.4649469178 | 31.1462103208 | 71 | 7 | 12 | 32.7 | TDD | 968 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3270723 | 4 | 121.4661935466 | 31.1503447950 | 192 | 1 | 8 | 30.9 | TDD | 391 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3279947 | 2 | 121.4646228603 | 31.1487882700 | 330 | 4 | 0 | 15.2 | TDD | 457 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.117 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.219 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.219 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227487 | 1 | 10.9167 | 15.4669 | -115.3233 | 8.0139 | 154.3618 | 0.0130 | 0.0086 |
| 2024_09_20 22:00 | 3279947 | 2 | 19.4791 | 13.9809 | -116.2027 | 7.0413 | 173.2028 | 0.0144 | 0.0106 |
| 2024_09_20 22:00 | 3219975 | 3 | 7.7581 | 5.4488 | -114.4289 | 8.5711 | 180.1976 | 0.0156 | 0.0099 |
| 2024_09_20 22:00 | 3270723 | 4 | 14.1740 | 16.6393 | -108.2972 | 8.4113 | 192.3096 | 0.0119 | 0.0020 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415574_4733E2D3 | 504990 | 391 | -92.3 | 504990 | 570 | -94.9 | 504990 | 968 | -93.8 | 504990 | 457 |
| MR_1774415574_559E8F35 | 504990 | 570 | -91.5 | 504990 | 391 | -94.6 | 504990 | 968 | -94.2 | 504990 | 457 |
| MR_1774415574_2026E4AA | 504990 | 391 | -92.7 | 504990 | 570 | -94.1 | 504990 | 968 | -92.7 | 504990 | 457 |
| MR_1774415574_CE05611D | 504990 | 570 | -91.8 | 504990 | 391 | -91.6 | 504990 | 968 | -92.1 | 504990 | 457 |
| MR_1774415574_3506978C | 504990 | 391 | -93.5 | 504990 | 570 | -91.4 | 504990 | 968 | -95.8 | 504990 | 457 |
| MR_1774415574_ADD9BCF1 | 504990 | 570 | -91.5 | 504990 | 391 | -92.3 | 504990 | 968 | -94.2 | 504990 | 457 |
| MR_1774415574_E218C5A6 | 504990 | 391 | -91.1 | 504990 | 570 | -94.0 | 504990 | 968 | -94.7 | 504990 | 457 |
| MR_1774415574_5AA17367 | 504990 | 391 | -91.2 | 504990 | 570 | -93.0 | 504990 | 968 | -94.8 | 504990 | 457 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 95: `8ee445e0-4e3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8ee445e0-4e32-4a4d-884c-8af14374c0ed` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Add neighbor relationship between 3240836_2 and 3230308_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[95] topology](images/train_0095.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3230308_1 by 11 degrees
- `C2`: Decrease transmission power for 3240836_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230308_1
- `C4`: Press down the tilt angle of 3240836_2 by 10 degrees
- `C5`: Adjust the azimuth of 3240836_2 by 9 degrees
- `C6`: Decrease transmission power for 3230308_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230308_1
- `C8`: Decrease A3 Offset threshold for 3230308_1
- `C9`: Increase transmission power for 3240836_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240836_2
- `C11`: Check test server and transmission issues
- `C12`: Add neighbor relationship between 3240836_2 and 3230308_1 **← 정답**
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Increase A3 Offset threshold for 3230308_1
- `C15`: Decrease A3 Offset threshold for 3240836_2
- `C16`: Lift the tilt angle  of 3230308_1 by 5 degrees
- `C17`: Add neighbor relationship between 3241013_4 and 3230308_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240836_2
- `C19`: Lift the tilt angle of 3240836_2 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3240836_2
- `C21`: Increase transmission power for 3230308_1
- `C22`: Press down the tilt angle  of 3230308_1 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.302 | MS1 | 121.4656773036 | 31.1446350516 | 618 | 504990 | -77.72 | 14.54 | 344.26 | 0.20 | 2.93 | 1566 |
| 2024-09-20 22:21:32.465 | MS1 | 121.4656715375 | 31.1446348908 | 618 | 504990 | -75.52 | 12.20 | 510.69 | 0.15 | 2.65 | 1567 |
| 2024-09-20 22:21:33.567 | MS1 | 121.4656680346 | 31.1446216315 | 618 | 504990 | -84.40 | 15.74 | 368.43 | 0.06 | 2.53 | 1589 |
| 2024-09-20 22:21:34.223 | MS1 | 121.4656616252 | 31.1446275232 | 618 | 504990 | -91.56 | -2.04 | 59.67 | 0.13 | 1.09 | 1599 |
| 2024-09-20 22:21:35.360 | MS1 | 121.4656607107 | 31.1446262448 | 618 | 504990 | -87.51 | -2.91 | 52.35 | 0.14 | 1.15 | 1561 |
| 2024-09-20 22:21:36.695 | MS1 | 121.4656744451 | 31.1446180606 | 618 | 504990 | -90.64 | -2.06 | 54.61 | 0.17 | 1.15 | 1594 |
| 2024-09-20 22:21:37.256 | MS1 | 121.4656652499 | 31.1446225723 | 618 | 504990 | -89.51 | -1.76 | 39.21 | 0.17 | 1.07 | 1561 |
| 2024-09-20 22:21:38.834 | MS1 | 121.4656771645 | 31.1446369014 | 618 | 504990 | -76.41 | 12.25 | 517.44 | 0.05 | 1.35 | 1592 |
| 2024-09-20 22:21:39.200 | MS1 | 121.4656648690 | 31.1446231051 | 618 | 504990 | -80.04 | 15.65 | 477.85 | 0.15 | 1.27 | 1563 |
| 2024-09-20 22:21:40.625 | MS1 | 121.4656628381 | 31.1446209462 | 618 | 504990 | -80.13 | 15.67 | 549.24 | 0.06 | 2.54 | 1590 |
| 2024-09-20 22:21:41.569 | MS1 | 121.4656776484 | 31.1446220210 | 618 | 504990 | -84.66 | 17.47 | 535.53 | 0.20 | 2.87 | 1597 |
| 2024-09-20 22:21:42.200 | MS1 | 121.4656649011 | 31.1446338511 | 618 | 504990 | -77.92 | 14.85 | 395.22 | 0.17 | 2.44 | 1585 |

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
| 3230308 | 1 | 121.4740035102 | 31.1506123330 | 241 | 4 | 2 | 26.6 | TDD | 849 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3240836 | 2 | 121.4722901580 | 31.1448766545 | 258 | 9 | 8 | 16.9 | TDD | 618 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3241013 | 4 | 121.4642060347 | 31.1453276199 | 232 | 9 | 10 | 23.4 | TDD | 630 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3269534 | 3 | 121.4699736310 | 31.1473492903 | 57 | 13 | 3 | 32.8 | TDD | 34 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.176 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.194 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.328 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.328 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.979 | NREventA3 | measId:2;ServCellPCI:619;Se... |
| 2024-09-20 22:21:35.979 | NREventA3 | measId:2;ServCellPCI:619;Se... |
| 2024-09-20 22:21:36.979 | NREventA3 | measId:2;ServCellPCI:619;Se... |
| 2024-09-20 22:21:39.479 | NRRRCReestablishAttempt | PCI:619 |
| 2024-09-20 22:21:39.495 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.510 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.633 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.633 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230308 | 1 | 12.5239 | 12.3788 | -117.2679 | 19.2347 | 176.6278 | 0.0175 | 0.0146 |
| 2024_09_20 22:00 | 3240836 | 2 | 10.4610 | 8.3455 | -114.5420 | 19.0668 | 104.0117 | 0.0179 | 0.1605 |
| 2024_09_20 22:00 | 3269534 | 3 | 14.4932 | 11.1790 | -116.9570 | 5.2388 | 80.7016 | 0.0017 | 0.0060 |
| 2024_09_20 22:00 | 3241013 | 4 | 19.5838 | 14.3206 | -115.1333 | 18.6968 | 153.1112 | 0.0045 | 0.0200 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417155_81238C0F | 504990 | 849 | -87.5 | 504990 | 618 | -93.0 | 504990 | 630 | -93.1 | 504990 | 34 |
| MR_1774417155_1DF78918 | 504990 | 618 | -93.3 | 504990 | 849 | -86.5 | 504990 | 630 | -94.7 | 504990 | 34 |
| MR_1774417155_91A1A5F7 | 504990 | 618 | -89.9 | 504990 | 849 | -85.4 | 504990 | 630 | -94.5 | 504990 | 34 |
| MR_1774417155_0686092D | 504990 | 618 | -92.4 | 504990 | 849 | -84.5 | 504990 | 630 | -93.2 | 504990 | 34 |
| MR_1774417155_71DB6C6C | 504990 | 618 | -90.6 | 504990 | 849 | -85.2 | 504990 | 630 | -93.2 | 504990 | 34 |
| MR_1774417155_E7CE5EE7 | 504990 | 618 | -93.5 | 504990 | 849 | -84.6 | 504990 | 630 | -92.9 | 504990 | 34 |
| MR_1774417155_38A1A18F | 504990 | 849 | -85.7 | 504990 | 618 | -92.8 | 504990 | 630 | -92.7 | 504990 | 34 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 96: `f2f956b8-5c3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f2f956b8-5c30-4522-825d-f8b93ab7a1c2` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[96] topology](images/train_0096.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3265657_4 by 38 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255358_2
- `C3`: Increase A3 Offset threshold for 3255358_2
- `C4`: Lift the tilt angle of 3255358_2 by 10 degrees
- `C5`: Decrease transmission power for 3255358_2
- `C6`: Increase transmission power for 3255358_2
- `C7`: Adjust the azimuth of 3255358_2 by 48 degrees
- `C8`: Press down the tilt angle  of 3265657_4 by 2 degrees
- `C9`: Decrease transmission power for 3265657_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265657_4
- `C11`: Lift the tilt angle  of 3265657_4 by 2 degrees
- `C12`: Decrease A3 Offset threshold for 3265657_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255358_2
- `C14`: Add neighbor relationship between 3213255_1 and 3265657_4
- `C15`: Increase A3 Offset threshold for 3265657_4
- `C16`: Increase transmission power for 3265657_4
- `C17`: Add neighbor relationship between 3255358_2 and 3265657_4
- `C18`: Press down the tilt angle of 3255358_2 by 10 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265657_4
- `C20`: Check test server and transmission issues **← 정답**
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease A3 Offset threshold for 3255358_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.647 | MS1 | 121.4656640945 | 31.1446371361 | 801 | 504990 | -88.22 | 16.12 | 505.28 | 0.15 | 2.58 | 1569 |
| 2024-09-20 22:21:32.238 | MS1 | 121.4656636996 | 31.1446269009 | 801 | 504990 | -90.97 | 17.91 | 368.03 | 0.19 | 2.72 | 1596 |
| 2024-09-20 22:21:33.503 | MS1 | 121.4656651145 | 31.1446371437 | 801 | 504990 | -91.69 | 16.76 | 503.68 | 0.12 | 2.39 | 1599 |
| 2024-09-20 22:21:34.839 | MS1 | 121.4656592222 | 31.1446247658 | 801 | 504990 | -88.44 | 12.16 | 83.97 | 0.02 | 2.75 | 492 |
| 2024-09-20 22:21:35.807 | MS1 | 121.4656581836 | 31.1446220805 | 801 | 504990 | -85.98 | 13.98 | 43.76 | 0.04 | 2.52 | 308 |
| 2024-09-20 22:21:36.173 | MS1 | 121.4656685019 | 31.1446376136 | 801 | 504990 | -87.74 | 17.76 | 53.98 | 0.01 | 2.78 | 422 |
| 2024-09-20 22:21:37.742 | MS1 | 121.4656651417 | 31.1446262123 | 801 | 504990 | -91.01 | 7.33 | 61.44 | 0.13 | 2.43 | 465 |
| 2024-09-20 22:21:38.941 | MS1 | 121.4656724701 | 31.1446290240 | 801 | 504990 | -92.70 | 12.83 | 79.73 | 0.13 | 2.52 | 433 |
| 2024-09-20 22:21:39.311 | MS1 | 121.4656698831 | 31.1446329538 | 801 | 504990 | -89.52 | 8.51 | 93.69 | 0.15 | 2.11 | 308 |
| 2024-09-20 22:21:40.615 | MS1 | 121.4656742879 | 31.1446261778 | 801 | 504990 | -91.92 | 10.75 | 430.08 | 0.17 | 2.75 | 1580 |
| 2024-09-20 22:21:41.217 | MS1 | 121.4656645521 | 31.1446272672 | 801 | 504990 | -89.05 | 9.65 | 331.38 | 0.09 | 2.55 | 1593 |
| 2024-09-20 22:21:42.499 | MS1 | 121.4656634333 | 31.1446188387 | 801 | 504990 | -91.84 | 10.91 | 374.85 | 0.18 | 2.48 | 1575 |

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
| 3213255 | 1 | 121.4715086978 | 31.1474481535 | 146 | 6 | 6 | 29.7 | TDD | 224 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3218848 | 3 | 121.4708405306 | 31.1450262464 | 319 | 1 | 1 | 20.7 | TDD | 747 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3255358 | 2 | 121.4662385954 | 31.1455759492 | 256 | 5 | 3 | 17.0 | TDD | 801 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3265657 | 4 | 121.4716156765 | 31.1504343335 | 183 | 0 | 2 | 31.6 | TDD | 150 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.955 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.976 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.119 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.119 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.829 | NREventA3 | measId:2;ServCellPCI:109;Se... |
| 2024-09-20 22:21:38.069 | NRHandoverAttempt | SourcePCI:109;SourceNR-ARFC... |
| 2024-09-20 22:21:38.112 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.123 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.263 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.263 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213255 | 1 | 12.8798 | 9.0056 | -117.1113 | 10.8963 | 158.7679 | 0.0031 | 0.0142 |
| 2024_09_20 22:00 | 3255358 | 2 | 19.3088 | 10.5235 | -114.5067 | 15.6547 | 167.5433 | 0.0094 | 0.0193 |
| 2024_09_20 22:00 | 3218848 | 3 | 6.6179 | 16.1097 | -115.5751 | 7.9538 | 168.1626 | 0.0064 | 0.0099 |
| 2024_09_20 22:00 | 3265657 | 4 | 7.4837 | 8.8275 | -115.3646 | 6.5202 | 114.9703 | 0.0185 | 0.0087 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412743_C8F2F555 | 504990 | 801 | -89.7 | 504990 | 150 | -92.4 | 504990 | 224 | -100.8 | 504990 | 747 |
| MR_1774412743_512DAD0C | 504990 | 801 | -89.7 | 504990 | 150 | -91.7 | 504990 | 224 | -100.5 | 504990 | 747 |
| MR_1774412743_668E66F6 | 504990 | 801 | -88.5 | 504990 | 150 | -89.8 | 504990 | 224 | -101.4 | 504990 | 747 |
| MR_1774412743_A0F27441 | 504990 | 801 | -89.7 | 504990 | 150 | -90.1 | 504990 | 224 | -99.8 | 504990 | 747 |
| MR_1774412743_78CF32B2 | 504990 | 801 | -86.5 | 504990 | 150 | -92.2 | 504990 | 224 | -100.9 | 504990 | 747 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 97: `5f3561be-766...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5f3561be-7661-4a9c-bc13-9d7753ea4f39` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[97] topology](images/train_0097.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3264571_1
- `C2`: Insufficient data; more data is needed for judgment. **← 정답**
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264571_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264571_1
- `C5`: Add neighbor relationship between 3231662_3 and 3264571_1
- `C6`: Add neighbor relationship between 3262115_2 and 3264571_1
- `C7`: Press down the tilt angle of 3231662_3 by 3 degrees
- `C8`: Increase A3 Offset threshold for 3231662_3
- `C9`: Press down the tilt angle  of 3264571_1 by 10 degrees
- `C10`: Decrease A3 Offset threshold for 3231662_3
- `C11`: Increase transmission power for 3264571_1
- `C12`: Decrease transmission power for 3231662_3
- `C13`: Increase transmission power for 3231662_3
- `C14`: Check test server and transmission issues
- `C15`: Decrease A3 Offset threshold for 3264571_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231662_3
- `C17`: Lift the tilt angle  of 3264571_1 by 10 degrees
- `C18`: Adjust the azimuth of 3264571_1 by 50 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231662_3
- `C20`: Decrease transmission power for 3264571_1
- `C21`: Lift the tilt angle of 3231662_3 by 3 degrees
- `C22`: Adjust the azimuth of 3231662_3 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.516 | MS1 | 121.4656630656 | 31.1446285095 | 782 | 504990 | -88.22 | 14.07 | 312.45 | 0.13 | 2.06 | 1579 |
| 2024-09-20 22:21:32.770 | MS1 | 121.4656683763 | 31.1446256439 | 782 | 504990 | -90.39 | 15.07 | 549.59 | 0.06 | 2.67 | 1599 |
| 2024-09-20 22:21:33.738 | MS1 | 121.4656620370 | 31.1446231102 | 782 | 504990 | -89.99 | 16.14 | 557.03 | 0.08 | 2.05 | 1566 |
| 2024-09-20 22:21:34.583 | MS1 | 121.4656733835 | 31.1446223624 | 782 | 504990 | -87.95 | 13.20 | 85.66 | 0.15 | 2.91 | 1572 |
| 2024-09-20 22:21:35.773 | MS1 | 121.4656778183 | 31.1446299928 | 782 | 504990 | -87.93 | 12.03 | 51.20 | 0.02 | 2.63 | 1581 |
| 2024-09-20 22:21:36.255 | MS1 | 121.4656639886 | 31.1446240558 | 782 | 504990 | -90.28 | 12.93 | 90.69 | 0.11 | 2.59 | 1567 |
| 2024-09-20 22:21:37.492 | MS1 | 121.4656766671 | 31.1446301228 | 782 | 504990 | -89.77 | 9.55 | 68.99 | 0.08 | 2.23 | 1592 |
| 2024-09-20 22:21:38.213 | MS1 | 121.4656770770 | 31.1446208008 | 782 | 504990 | -93.34 | 11.01 | 61.69 | 0.14 | 2.34 | 1590 |
| 2024-09-20 22:21:39.427 | MS1 | 121.4656720888 | 31.1446184676 | 782 | 504990 | -92.68 | 7.59 | 93.19 | 0.09 | 2.27 | 1572 |
| 2024-09-20 22:21:40.882 | MS1 | 121.4656730495 | 31.1446375584 | 782 | 504990 | -91.05 | 11.93 | 587.35 | 0.07 | 2.00 | 1562 |
| 2024-09-20 22:21:41.322 | MS1 | 121.4656694450 | 31.1446349472 | 782 | 504990 | -90.28 | 11.64 | 502.59 | 0.20 | 2.68 | 1568 |
| 2024-09-20 22:21:42.498 | MS1 | 121.4656763172 | 31.1446197704 | 782 | 504990 | -91.48 | 12.19 | 380.41 | 0.05 | 2.03 | 1580 |

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
| 3230476 | 4 | 121.4740300186 | 31.1541123257 | 196 | 3 | 0 | 17.9 | TDD | 543 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3231662 | 3 | 121.4749873617 | 31.1521131175 | 285 | 1 | 6 | 44.2 | TDD | 782 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3262115 | 2 | 121.4708416536 | 31.1535276921 | 95 | 3 | 12 | 18.1 | TDD | 693 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3264571 | 1 | 121.4693739790 | 31.1477471402 | 112 | 9 | 7 | 16.8 | TDD | 760 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.199 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.311 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.311 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.016 | NREventA3 | measId:2;ServCellPCI:564;Se... |
| 2024-09-20 22:21:38.256 | NRHandoverAttempt | SourcePCI:564;SourceNR-ARFC... |
| 2024-09-20 22:21:38.304 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.317 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.422 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.422 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3264571 | 1 | 85.0813 | 84.4898 | -117.7255 | 11.2023 | 91.0849 | 0.0057 | 0.0053 |
| 2024_09_19 22:00 | 3262115 | 2 | 93.4713 | 77.2946 | -116.0209 | 17.8134 | 121.6600 | 0.0054 | 0.0036 |
| 2024_09_19 22:00 | 3231662 | 3 | 82.4023 | 86.5742 | -115.3398 | 12.9170 | 146.6747 | 0.0083 | 0.0016 |
| 2024_09_19 22:00 | 3230476 | 4 | 93.5561 | 94.4047 | -117.4570 | 19.4286 | 129.8561 | 0.0147 | 0.0061 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413990_4B96B8CC | 504990 | 782 | -87.0 | 504990 | 760 | -87.9 | 504990 | 693 | -100.1 | 504990 | 543 |
| MR_1774413990_918761CF | 504990 | 782 | -87.9 | 504990 | 760 | -90.3 | 504990 | 693 | -101.8 | 504990 | 543 |
| MR_1774413990_0F7E372C | 504990 | 782 | -89.6 | 504990 | 760 | -89.1 | 504990 | 693 | -102.0 | 504990 | 543 |
| MR_1774413990_2069A2E0 | 504990 | 782 | -86.9 | 504990 | 760 | -88.0 | 504990 | 693 | -98.4 | 504990 | 543 |
| MR_1774413990_A25F3DAB | 504990 | 782 | -88.3 | 504990 | 760 | -88.1 | 504990 | 693 | -100.3 | 504990 | 543 |
| MR_1774413990_80612E74 | 504990 | 782 | -88.6 | 504990 | 760 | -88.2 | 504990 | 693 | -99.9 | 504990 | 543 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 98: `638dd303-b78...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `638dd303-b782-4df8-872d-435722b06098` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[98] topology](images/train_0098.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3279412_4
- `C2`: Add neighbor relationship between 3248382_3 and 3279412_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248382_3
- `C4`: Press down the tilt angle of 3248382_3 by 10 degrees
- `C5`: Decrease A3 Offset threshold for 3248382_3
- `C6`: Decrease transmission power for 3248382_3
- `C7`: Press down the tilt angle  of 3279412_4 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279412_4
- `C9`: Decrease transmission power for 3279412_4
- `C10`: Add neighbor relationship between 3240327_1 and 3279412_4
- `C11`: Insufficient data; more data is needed for judgment. **← 정답**
- `C12`: Lift the tilt angle of 3248382_3 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3279412_4
- `C14`: Lift the tilt angle  of 3279412_4 by 10 degrees
- `C15`: Adjust the azimuth of 3279412_4 by 50 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248382_3
- `C17`: Increase A3 Offset threshold for 3248382_3
- `C18`: Adjust the azimuth of 3248382_3 by 50 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279412_4
- `C20`: Check test server and transmission issues
- `C21`: Increase transmission power for 3248382_3
- `C22`: Increase transmission power for 3279412_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.405 | MS1 | 121.4656660065 | 31.1446212488 | 414 | 504990 | -85.11 | 15.69 | 419.92 | 0.14 | 2.17 | 1585 |
| 2024-09-20 22:21:32.680 | MS1 | 121.4656759712 | 31.1446266232 | 414 | 504990 | -86.10 | 17.17 | 388.46 | 0.08 | 2.76 | 1560 |
| 2024-09-20 22:21:33.443 | MS1 | 121.4656705450 | 31.1446218333 | 414 | 504990 | -88.59 | 13.29 | 323.80 | 0.10 | 2.92 | 1560 |
| 2024-09-20 22:21:34.179 | MS1 | 121.4656710937 | 31.1446299698 | 414 | 504990 | -91.92 | 14.26 | 101.57 | 0.15 | 2.67 | 1569 |
| 2024-09-20 22:21:35.911 | MS1 | 121.4656622854 | 31.1446254915 | 414 | 504990 | -88.18 | 13.89 | 89.94 | 0.02 | 2.07 | 1580 |
| 2024-09-20 22:21:36.919 | MS1 | 121.4656689010 | 31.1446239791 | 414 | 504990 | -91.57 | 14.75 | 82.33 | 0.04 | 2.97 | 1588 |
| 2024-09-20 22:21:37.445 | MS1 | 121.4656581180 | 31.1446321430 | 414 | 504990 | -90.46 | 9.29 | 92.96 | 0.09 | 2.74 | 1594 |
| 2024-09-20 22:21:38.726 | MS1 | 121.4656628491 | 31.1446328404 | 414 | 504990 | -91.82 | 11.11 | 72.77 | 0.08 | 2.39 | 1581 |
| 2024-09-20 22:21:39.715 | MS1 | 121.4656681718 | 31.1446218454 | 414 | 504990 | -89.79 | 8.19 | 92.02 | 0.17 | 2.76 | 1598 |
| 2024-09-20 22:21:40.597 | MS1 | 121.4656779365 | 31.1446260528 | 414 | 504990 | -92.47 | 10.79 | 426.54 | 0.06 | 2.11 | 1592 |
| 2024-09-20 22:21:41.477 | MS1 | 121.4656608368 | 31.1446313040 | 414 | 504990 | -92.53 | 8.77 | 564.55 | 0.12 | 2.73 | 1585 |
| 2024-09-20 22:21:42.123 | MS1 | 121.4656618851 | 31.1446225000 | 414 | 504990 | -93.73 | 9.79 | 343.93 | 0.02 | 2.99 | 1570 |

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
| 3240327 | 1 | 121.4750805768 | 31.1530068917 | 207 | 9 | 11 | 15.7 | TDD | 34 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3248382 | 3 | 121.4699622391 | 31.1504793690 | 77 | 12 | 1 | 22.2 | TDD | 414 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3273279 | 2 | 121.4758739096 | 31.1496090486 | 21 | 6 | 4 | 27.9 | TDD | 883 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3279412 | 4 | 121.4676874251 | 31.1445632258 | 39 | 9 | 3 | 38.9 | TDD | 991 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.043 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.064 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.210 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.210 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.926 | NREventA3 | measId:2;ServCellPCI:520;Se... |
| 2024-09-20 22:21:38.166 | NRHandoverAttempt | SourcePCI:520;SourceNR-ARFC... |
| 2024-09-20 22:21:38.204 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.218 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.340 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.340 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3240327 | 1 | 80.1795 | 82.2240 | -115.0108 | 14.5256 | 86.4794 | 0.0041 | 0.0093 |
| 2024_09_19 22:00 | 3273279 | 2 | 77.6032 | 87.8880 | -117.6536 | 12.1068 | 107.7117 | 0.0020 | 0.0005 |
| 2024_09_19 22:00 | 3248382 | 3 | 80.9730 | 90.5609 | -116.3582 | 9.6284 | 135.5524 | 0.0134 | 0.0147 |
| 2024_09_19 22:00 | 3279412 | 4 | 80.8602 | 88.4248 | -116.7311 | 6.3608 | 178.9003 | 0.0108 | 0.0087 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412459_B3921517 | 504990 | 414 | -88.9 | 504990 | 991 | -95.9 | 504990 | 34 | -103.4 | 504990 | 883 |
| MR_1774412459_301756EF | 504990 | 414 | -87.2 | 504990 | 991 | -98.5 | 504990 | 34 | -99.9 | 504990 | 883 |
| MR_1774412459_E73C2C9E | 504990 | 414 | -87.4 | 504990 | 991 | -96.6 | 504990 | 34 | -101.5 | 504990 | 883 |
| MR_1774412459_38595B2A | 504990 | 414 | -88.2 | 504990 | 991 | -96.5 | 504990 | 34 | -101.6 | 504990 | 883 |
| MR_1774412459_D37D0B78 | 504990 | 414 | -86.9 | 504990 | 991 | -95.9 | 504990 | 34 | -101.7 | 504990 | 883 |
| MR_1774412459_F14B8447 | 504990 | 414 | -87.7 | 504990 | 991 | -95.5 | 504990 | 34 | -100.7 | 504990 | 883 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 99: `329d9b23-9cc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `329d9b23-9cc2-4a3c-879e-f1bcfac6289e` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[99] topology](images/train_0099.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224419_2
- `C3`: Decrease transmission power for 3249452_4
- `C4`: Adjust the azimuth of 3224419_2 by 50 degrees
- `C5`: Decrease transmission power for 3224419_2
- `C6`: Lift the tilt angle  of 3224419_2 by 10 degrees
- `C7`: Increase A3 Offset threshold for 3249452_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249452_4
- `C9`: Increase A3 Offset threshold for 3224419_2
- `C10`: Add neighbor relationship between 3249452_4 and 3224419_2
- `C11`: Increase transmission power for 3249452_4
- `C12`: Adjust the azimuth of 3249452_4 by 50 degrees
- `C13`: Add neighbor relationship between 3236542_1 and 3224419_2
- `C14`: Press down the tilt angle  of 3224419_2 by 10 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224419_2
- `C16`: Decrease A3 Offset threshold for 3224419_2
- `C17`: Check test server and transmission issues **← 정답**
- `C18`: Increase transmission power for 3224419_2
- `C19`: Press down the tilt angle of 3249452_4 by 4 degrees
- `C20`: Lift the tilt angle of 3249452_4 by 4 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249452_4
- `C22`: Decrease A3 Offset threshold for 3249452_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.252 | MS1 | 121.4656734456 | 31.1446281248 | 14 | 504990 | -87.22 | 13.89 | 401.57 | 0.10 | 2.82 | 1565 |
| 2024-09-20 22:21:32.219 | MS1 | 121.4656693744 | 31.1446187310 | 14 | 504990 | -89.54 | 17.53 | 464.30 | 0.13 | 2.65 | 1588 |
| 2024-09-20 22:21:33.325 | MS1 | 121.4656583962 | 31.1446372779 | 14 | 504990 | -85.89 | 13.77 | 512.89 | 0.17 | 2.59 | 1596 |
| 2024-09-20 22:21:34.138 | MS1 | 121.4656732542 | 31.1446324800 | 14 | 504990 | -90.08 | 16.83 | 87.09 | 0.11 | 2.57 | 421 |
| 2024-09-20 22:21:35.527 | MS1 | 121.4656738514 | 31.1446209532 | 14 | 504990 | -85.77 | 16.92 | 98.00 | 0.07 | 2.45 | 395 |
| 2024-09-20 22:21:36.775 | MS1 | 121.4656722144 | 31.1446377865 | 14 | 504990 | -87.74 | 12.94 | 81.54 | 0.20 | 2.69 | 401 |
| 2024-09-20 22:21:37.771 | MS1 | 121.4656687184 | 31.1446299238 | 14 | 504990 | -93.91 | 12.72 | 83.98 | 0.12 | 2.90 | 310 |
| 2024-09-20 22:21:38.903 | MS1 | 121.4656685434 | 31.1446241845 | 14 | 504990 | -93.60 | 11.19 | 71.32 | 0.14 | 2.32 | 354 |
| 2024-09-20 22:21:39.651 | MS1 | 121.4656635384 | 31.1446318154 | 14 | 504990 | -91.73 | 9.62 | 76.62 | 0.08 | 2.23 | 463 |
| 2024-09-20 22:21:40.319 | MS1 | 121.4656705966 | 31.1446304505 | 14 | 504990 | -92.97 | 9.38 | 343.08 | 0.10 | 2.66 | 1599 |
| 2024-09-20 22:21:41.887 | MS1 | 121.4656728510 | 31.1446302274 | 14 | 504990 | -91.63 | 12.73 | 494.45 | 0.14 | 2.28 | 1574 |
| 2024-09-20 22:21:42.893 | MS1 | 121.4656633512 | 31.1446221056 | 14 | 504990 | -93.40 | 10.69 | 549.60 | 0.10 | 2.68 | 1581 |

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
| 3224419 | 2 | 121.4642140614 | 31.1535422042 | 334 | 13 | 9 | 22.4 | TDD | 604 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3236542 | 1 | 121.4723104212 | 31.1509626534 | 139 | 4 | 9 | 44.7 | TDD | 867 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3249452 | 4 | 121.4667624114 | 31.1493574343 | 342 | 0 | 6 | 40.3 | TDD | 14 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3252674 | 3 | 121.4643757837 | 31.1468683277 | 347 | 5 | 4 | 29.8 | TDD | 38 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.521 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.542 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.682 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.682 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.368 | NREventA3 | measId:2;ServCellPCI:904;Se... |
| 2024-09-20 22:21:38.608 | NRHandoverAttempt | SourcePCI:904;SourceNR-ARFC... |
| 2024-09-20 22:21:38.638 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.649 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.771 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.771 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236542 | 1 | 13.6352 | 10.7477 | -114.8738 | 5.9966 | 172.3367 | 0.0107 | 0.0064 |
| 2024_09_20 22:00 | 3224419 | 2 | 14.1720 | 14.9682 | -115.2067 | 11.7092 | 147.6621 | 0.0059 | 0.0158 |
| 2024_09_20 22:00 | 3252674 | 3 | 14.7744 | 7.3428 | -116.3402 | 16.8755 | 110.9457 | 0.0013 | 0.0006 |
| 2024_09_20 22:00 | 3249452 | 4 | 8.3939 | 11.0103 | -115.1393 | 7.2157 | 96.0535 | 0.0089 | 0.0084 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414506_0C0EA81F | 504990 | 14 | -91.5 | 504990 | 604 | -91.3 | 504990 | 867 | -104.4 | 504990 | 38 |
| MR_1774414506_F124A7D6 | 504990 | 14 | -90.2 | 504990 | 604 | -92.4 | 504990 | 867 | -103.2 | 504990 | 38 |
| MR_1774414506_77E552F1 | 504990 | 14 | -90.3 | 504990 | 604 | -94.1 | 504990 | 867 | -103.7 | 504990 | 38 |
| MR_1774414506_D123CE9A | 504990 | 14 | -91.7 | 504990 | 604 | -92.1 | 504990 | 867 | -102.2 | 504990 | 38 |
| MR_1774414506_A7AD67D8 | 504990 | 14 | -92.0 | 504990 | 604 | -94.5 | 504990 | 867 | -105.1 | 504990 | 38 |

> *... 2개 열 생략 (전체 14열)*

---
