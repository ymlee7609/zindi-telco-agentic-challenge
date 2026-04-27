# Track A 문제 분석 — train[310]~train[319]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[310] ~ train[319] (10개)

## 목차

1. [문제 310: `2984f3f4-bb0...`](#310) — multiple-answer, 정답: C13|C22
2. [문제 311: `4b984b37-253...`](#311) — single-answer, 정답: C4
3. [문제 312: `fe7293d5-c0f...`](#312) — single-answer, 정답: C10
4. [문제 313: `1160d740-bab...`](#313) — single-answer, 정답: C20
5. [문제 314: `b67643bc-15d...`](#314) — single-answer, 정답: C10
6. [문제 315: `9c882599-395...`](#315) — single-answer, 정답: C22
7. [문제 316: `7529ac63-933...`](#316) — single-answer, 정답: C8
8. [문제 317: `378819a1-ce7...`](#317) — single-answer, 정답: C9
9. [문제 318: `df66899a-c28...`](#318) — single-answer, 정답: C18
10. [문제 319: `4adfa6c0-124...`](#319) — single-answer, 정답: C14

---

### 문제 310: `2984f3f4-bb0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2984f3f4-bb0b-41cf-9a7b-ef880025c94f` |
| Tag | **multiple-answer** |
| 정답 | **C13|C22** |
| C13 의미 | Press down the tilt angle  of 3272013_4 by 3 degrees |
| C22 의미 | Decrease transmission power for 3272013_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[310] topology](images/train_0310.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272013_4
- `C2`: Adjust the azimuth of 3254905_1 by 12 degrees
- `C3`: Lift the tilt angle of 3254905_1 by 3 degrees
- `C4`: Increase A3 Offset threshold for 3254905_1
- `C5`: Decrease A3 Offset threshold for 3272013_4
- `C6`: Check test server and transmission issues
- `C7`: Increase transmission power for 3254905_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Add neighbor relationship between 3245884_3 and 3272013_4
- `C10`: Add neighbor relationship between 3254905_1 and 3272013_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272013_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254905_1
- `C13`: Press down the tilt angle  of 3272013_4 by 3 degrees **← 정답**
- `C14`: Press down the tilt angle of 3254905_1 by 3 degrees
- `C15`: Increase A3 Offset threshold for 3272013_4
- `C16`: Decrease A3 Offset threshold for 3254905_1
- `C17`: Lift the tilt angle  of 3272013_4 by 3 degrees
- `C18`: Decrease transmission power for 3254905_1
- `C19`: Adjust the azimuth of 3272013_4 by 6 degrees
- `C20`: Increase transmission power for 3272013_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254905_1
- `C22`: Decrease transmission power for 3272013_4 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.925 | MS1 | 121.4656638434 | 31.1446236934 | 937 | 504990 | -84.28 | 13.75 | 511.34 | 0.12 | 2.99 | 1579 |
| 2024-09-20 22:21:32.183 | MS1 | 121.4656698640 | 31.1446188861 | 937 | 504990 | -84.00 | 12.84 | 584.61 | 0.19 | 2.14 | 1589 |
| 2024-09-20 22:21:33.674 | MS1 | 121.4656759038 | 31.1446334208 | 937 | 504990 | -77.25 | 17.53 | 384.56 | 0.08 | 2.53 | 1588 |
| 2024-09-20 22:21:34.180 | MS1 | 121.4656634645 | 31.1446229712 | 937 | 504990 | -87.31 | 1.76 | 70.84 | 0.07 | 1.33 | 1561 |
| 2024-09-20 22:21:35.467 | MS1 | 121.4656646120 | 31.1446351818 | 937 | 504990 | -87.58 | 0.78 | 84.61 | 0.16 | 1.12 | 1577 |
| 2024-09-20 22:21:36.167 | MS1 | 121.4656751803 | 31.1446322137 | 937 | 504990 | -90.60 | 2.23 | 56.27 | 0.11 | 1.12 | 1594 |
| 2024-09-20 22:21:37.373 | MS1 | 121.4656746936 | 31.1446192252 | 937 | 504990 | -86.90 | 2.63 | 68.25 | 0.16 | 1.34 | 1597 |
| 2024-09-20 22:21:38.693 | MS1 | 121.4656670451 | 31.1446370337 | 937 | 504990 | -94.93 | 0.44 | 84.05 | 0.14 | 1.10 | 1599 |
| 2024-09-20 22:21:39.571 | MS1 | 121.4656627682 | 31.1446344998 | 937 | 504990 | -88.37 | 1.35 | 67.88 | 0.04 | 1.02 | 1590 |
| 2024-09-20 22:21:40.325 | MS1 | 121.4656666315 | 31.1446346701 | 937 | 504990 | -78.07 | 13.29 | 351.49 | 0.17 | 2.82 | 1572 |
| 2024-09-20 22:21:41.691 | MS1 | 121.4656593268 | 31.1446285115 | 937 | 504990 | -79.27 | 17.45 | 490.62 | 0.13 | 2.15 | 1560 |
| 2024-09-20 22:21:42.938 | MS1 | 121.4656642597 | 31.1446182464 | 937 | 504990 | -83.58 | 16.06 | 470.92 | 0.00 | 2.66 | 1564 |

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
| 3221490 | 2 | 121.4650240990 | 31.1498740284 | 265 | 2 | 12 | 26.7 | TDD | 42 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3245884 | 3 | 121.4681669875 | 31.1508261117 | 246 | 13 | 5 | 38.9 | TDD | 147 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3254905 | 1 | 121.4720740722 | 31.1492991012 | 242 | 2 | 7 | 20.6 | TDD | 937 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3272013 | 4 | 121.4738309742 | 31.1489933653 | 232 | 2 | 9 | 21.0 | TDD | 212 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.180 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.200 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.303 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.303 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254905 | 1 | 6.7427 | 18.1437 | -108.8052 | 7.3599 | 80.8365 | 0.0103 | 0.0153 |
| 2024_09_20 22:00 | 3221490 | 2 | 5.0387 | 19.3116 | -116.3011 | 5.2294 | 170.5212 | 0.0153 | 0.0082 |
| 2024_09_20 22:00 | 3245884 | 3 | 9.6862 | 13.6460 | -114.2934 | 11.3762 | 151.7012 | 0.0138 | 0.0109 |
| 2024_09_20 22:00 | 3272013 | 4 | 13.3363 | 7.5418 | -117.8723 | 17.3445 | 181.6280 | 0.0053 | 0.0177 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414291_4D72AA37 | 504990 | 212 | -86.1 | 504990 | 937 | -84.3 | 504990 | 147 | -88.2 | 504990 | 42 |
| MR_1774414291_DCA355F7 | 504990 | 937 | -86.2 | 504990 | 212 | -86.2 | 504990 | 147 | -88.6 | 504990 | 42 |
| MR_1774414291_A53CAF99 | 504990 | 212 | -86.0 | 504990 | 937 | -82.7 | 504990 | 147 | -88.1 | 504990 | 42 |
| MR_1774414291_30217C0C | 504990 | 937 | -86.8 | 504990 | 212 | -86.0 | 504990 | 147 | -86.7 | 504990 | 42 |
| MR_1774414291_D75570D8 | 504990 | 212 | -88.2 | 504990 | 937 | -84.4 | 504990 | 147 | -85.3 | 504990 | 42 |
| MR_1774414291_59B942D9 | 504990 | 937 | -86.0 | 504990 | 212 | -83.6 | 504990 | 147 | -86.1 | 504990 | 42 |
| MR_1774414291_3DCD4BD5 | 504990 | 937 | -85.3 | 504990 | 212 | -84.9 | 504990 | 147 | -85.5 | 504990 | 42 |
| MR_1774414291_3867E306 | 504990 | 937 | -86.6 | 504990 | 212 | -84.3 | 504990 | 147 | -87.3 | 504990 | 42 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 311: `4b984b37-253...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4b984b37-2530-43ef-b4dd-9ccff102245e` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[311] topology](images/train_0311.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3227267_2 by 10 degrees
- `C2`: Increase transmission power for 3272470_1
- `C3`: Check test server and transmission issues
- `C4`: Insufficient data; more data is needed for judgment. **← 정답**
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272470_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227267_2
- `C7`: Adjust the azimuth of 3227267_2 by 50 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227267_2
- `C9`: Press down the tilt angle  of 3272470_1 by 10 degrees
- `C10`: Add neighbor relationship between 3242082_4 and 3272470_1
- `C11`: Decrease A3 Offset threshold for 3227267_2
- `C12`: Lift the tilt angle  of 3272470_1 by 10 degrees
- `C13`: Increase A3 Offset threshold for 3227267_2
- `C14`: Lift the tilt angle of 3227267_2 by 10 degrees
- `C15`: Add neighbor relationship between 3227267_2 and 3272470_1
- `C16`: Adjust the azimuth of 3272470_1 by 31 degrees
- `C17`: Increase transmission power for 3227267_2
- `C18`: Decrease A3 Offset threshold for 3272470_1
- `C19`: Decrease transmission power for 3272470_1
- `C20`: Increase A3 Offset threshold for 3272470_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272470_1
- `C22`: Decrease transmission power for 3227267_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.673 | MS1 | 121.4656767155 | 31.1446330339 | 795 | 504990 | -86.63 | 14.83 | 555.11 | 0.06 | 2.84 | 1571 |
| 2024-09-20 22:21:32.231 | MS1 | 121.4656676411 | 31.1446201783 | 795 | 504990 | -85.60 | 13.55 | 471.31 | 0.07 | 2.70 | 1562 |
| 2024-09-20 22:21:33.161 | MS1 | 121.4656698617 | 31.1446188092 | 795 | 504990 | -89.61 | 15.69 | 312.26 | 0.15 | 2.70 | 1598 |
| 2024-09-20 22:21:34.549 | MS1 | 121.4656676158 | 31.1446227748 | 795 | 504990 | -89.54 | 16.45 | 71.58 | 0.17 | 2.84 | 1567 |
| 2024-09-20 22:21:35.877 | MS1 | 121.4656701835 | 31.1446311014 | 795 | 504990 | -85.99 | 17.52 | 83.08 | 0.03 | 2.09 | 1578 |
| 2024-09-20 22:21:36.211 | MS1 | 121.4656724098 | 31.1446216696 | 795 | 504990 | -91.58 | 12.80 | 63.64 | 0.11 | 2.57 | 1575 |
| 2024-09-20 22:21:37.408 | MS1 | 121.4656662709 | 31.1446354710 | 795 | 504990 | -90.57 | 9.90 | 62.11 | 0.15 | 2.65 | 1562 |
| 2024-09-20 22:21:38.473 | MS1 | 121.4656695382 | 31.1446378814 | 795 | 504990 | -93.93 | 10.99 | 68.17 | 0.00 | 2.20 | 1577 |
| 2024-09-20 22:21:39.399 | MS1 | 121.4656778439 | 31.1446194831 | 795 | 504990 | -90.20 | 11.55 | 50.20 | 0.08 | 2.74 | 1578 |
| 2024-09-20 22:21:40.119 | MS1 | 121.4656621510 | 31.1446313993 | 795 | 504990 | -93.76 | 9.57 | 440.30 | 0.04 | 2.98 | 1590 |
| 2024-09-20 22:21:41.754 | MS1 | 121.4656617756 | 31.1446360456 | 795 | 504990 | -89.02 | 11.40 | 478.21 | 0.14 | 2.02 | 1588 |
| 2024-09-20 22:21:42.934 | MS1 | 121.4656748603 | 31.1446351803 | 795 | 504990 | -93.98 | 12.75 | 544.04 | 0.01 | 2.31 | 1584 |

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
| 3227267 | 2 | 121.4685976741 | 31.1457766880 | 159 | 5 | 1 | 48.0 | TDD | 795 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3242082 | 4 | 121.4696935276 | 31.1507378281 | 98 | 12 | 2 | 43.0 | TDD | 191 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3266940 | 3 | 121.4694741860 | 31.1463109529 | 109 | 0 | 0 | 16.0 | TDD | 453 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3272470 | 1 | 121.4680916902 | 31.1469067441 | 191 | 12 | 10 | 28.9 | TDD | 517 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.436 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.459 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.597 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.597 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.288 | NREventA3 | measId:2;ServCellPCI:9;Serv... |
| 2024-09-20 22:21:38.528 | NRHandoverAttempt | SourcePCI:9;SourceNR-ARFCN:... |
| 2024-09-20 22:21:38.561 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.574 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.684 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.684 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3272470 | 1 | 86.4084 | 83.9753 | -115.8804 | 17.9516 | 122.3694 | 0.0067 | 0.0066 |
| 2024_09_19 22:00 | 3227267 | 2 | 78.9973 | 79.2721 | -114.8128 | 13.4219 | 183.1091 | 0.0013 | 0.0165 |
| 2024_09_19 22:00 | 3266940 | 3 | 90.0369 | 78.1449 | -116.0867 | 19.1090 | 150.4823 | 0.0168 | 0.0176 |
| 2024_09_19 22:00 | 3242082 | 4 | 86.7040 | 92.6228 | -115.9187 | 11.2668 | 101.5877 | 0.0149 | 0.0017 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413449_96127586 | 504990 | 795 | -89.8 | 504990 | 517 | -92.5 | 504990 | 191 | -101.6 | 504990 | 453 |
| MR_1774413449_0D78E858 | 504990 | 795 | -88.2 | 504990 | 517 | -90.5 | 504990 | 191 | -99.7 | 504990 | 453 |
| MR_1774413449_27F90421 | 504990 | 795 | -90.2 | 504990 | 517 | -91.3 | 504990 | 191 | -101.4 | 504990 | 453 |
| MR_1774413449_1EE5ADE3 | 504990 | 795 | -90.3 | 504990 | 517 | -92.3 | 504990 | 191 | -102.5 | 504990 | 453 |
| MR_1774413449_902678DE | 504990 | 795 | -90.3 | 504990 | 517 | -90.1 | 504990 | 191 | -102.5 | 504990 | 453 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 312: `fe7293d5-c0f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fe7293d5-c0fd-46c6-99a4-97ee0308f394` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3254106_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[312] topology](images/train_0312.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3254106_1
- `C2`: Decrease transmission power for 3278847_3
- `C3`: Decrease transmission power for 3254106_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278847_3
- `C5`: Decrease A3 Offset threshold for 3278847_3
- `C6`: Increase transmission power for 3278847_3
- `C7`: Lift the tilt angle of 3254106_1 by 6 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278847_3
- `C9`: Adjust the azimuth of 3254106_1 by 9 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254106_1 **← 정답**
- `C11`: Press down the tilt angle of 3254106_1 by 6 degrees
- `C12`: Add neighbor relationship between 3254106_1 and 3278847_3
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Adjust the azimuth of 3278847_3 by 50 degrees
- `C15`: Decrease A3 Offset threshold for 3254106_1
- `C16`: Press down the tilt angle  of 3278847_3 by 10 degrees
- `C17`: Increase transmission power for 3254106_1
- `C18`: Check test server and transmission issues
- `C19`: Add neighbor relationship between 3237553_4 and 3278847_3
- `C20`: Lift the tilt angle  of 3278847_3 by 10 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254106_1
- `C22`: Increase A3 Offset threshold for 3278847_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.532 | MS1 | 121.4656775752 | 31.1446331736 | 529 | 504990 | -87.54 | 16.11 | 475.07 | 0.09 | 2.75 | 1587 |
| 2024-09-20 22:21:32.977 | MS1 | 121.4656745786 | 31.1446266043 | 529 | 504990 | -86.78 | 14.47 | 479.80 | 0.11 | 2.47 | 1573 |
| 2024-09-20 22:21:33.437 | MS1 | 121.4656745790 | 31.1446327757 | 529 | 504990 | -90.09 | 13.33 | 325.22 | 0.07 | 2.77 | 1563 |
| 2024-09-20 22:21:34.268 | MS1 | 121.4656618032 | 31.1446223138 | 529 | 504990 | -89.99 | 16.78 | 62.59 | 0.67 | 2.21 | 660 |
| 2024-09-20 22:21:35.790 | MS1 | 121.4656762800 | 31.1446355303 | 529 | 504990 | -91.39 | 17.12 | 90.35 | 0.66 | 2.34 | 613 |
| 2024-09-20 22:21:36.814 | MS1 | 121.4656634871 | 31.1446294264 | 529 | 504990 | -88.21 | 17.11 | 67.66 | 0.54 | 2.15 | 513 |
| 2024-09-20 22:21:37.480 | MS1 | 121.4656674012 | 31.1446214907 | 529 | 504990 | -91.74 | 12.52 | 98.98 | 0.59 | 2.68 | 581 |
| 2024-09-20 22:21:38.868 | MS1 | 121.4656602704 | 31.1446345342 | 529 | 504990 | -90.60 | 11.76 | 56.33 | 0.56 | 2.56 | 583 |
| 2024-09-20 22:21:39.673 | MS1 | 121.4656614424 | 31.1446181670 | 529 | 504990 | -91.00 | 8.44 | 65.65 | 0.54 | 2.77 | 633 |
| 2024-09-20 22:21:40.555 | MS1 | 121.4656766973 | 31.1446187907 | 529 | 504990 | -91.49 | 8.38 | 443.12 | 0.17 | 2.44 | 1581 |
| 2024-09-20 22:21:41.657 | MS1 | 121.4656708119 | 31.1446214216 | 529 | 504990 | -92.54 | 12.91 | 428.80 | 0.16 | 2.54 | 1572 |
| 2024-09-20 22:21:42.147 | MS1 | 121.4656768718 | 31.1446267612 | 529 | 504990 | -92.98 | 11.93 | 477.57 | 0.07 | 2.99 | 1561 |

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
| 3237553 | 4 | 121.4755609569 | 31.1462072401 | 54 | 0 | 7 | 16.0 | TDD | 711 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3250375 | 2 | 121.4703123339 | 31.1536157579 | 337 | 13 | 11 | 42.8 | TDD | 330 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3254106 | 1 | 121.4671676806 | 31.1548812018 | 196 | 4 | 10 | 34.9 | TDD | 529 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3278847 | 3 | 121.4672115378 | 31.1498504288 | 347 | 12 | 7 | 19.1 | TDD | 611 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.224 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.247 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.353 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.353 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.036 | NREventA3 | measId:2;ServCellPCI:401;Se... |
| 2024-09-20 22:21:38.276 | NRHandoverAttempt | SourcePCI:401;SourceNR-ARFC... |
| 2024-09-20 22:21:38.307 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.317 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.427 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.427 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254106 | 1 | 9.2642 | 13.8465 | -117.4250 | 16.7375 | 148.2274 | 0.0040 | 0.0065 |
| 2024_09_20 22:00 | 3250375 | 2 | 15.5107 | 5.6716 | -117.3037 | 17.4376 | 102.1688 | 0.0033 | 0.0193 |
| 2024_09_20 22:00 | 3278847 | 3 | 5.2342 | 13.7032 | -114.5708 | 6.5785 | 91.6546 | 0.0183 | 0.0117 |
| 2024_09_20 22:00 | 3237553 | 4 | 7.2216 | 10.6468 | -117.7679 | 19.2804 | 181.5550 | 0.0066 | 0.0112 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416376_4D105A6E | 504990 | 529 | -91.9 | 504990 | 611 | -91.2 | 504990 | 711 | -98.7 | 504990 | 330 |
| MR_1774416376_6731F732 | 504990 | 529 | -89.8 | 504990 | 611 | -90.9 | 504990 | 711 | -99.6 | 504990 | 330 |
| MR_1774416376_25DB79F3 | 504990 | 529 | -88.1 | 504990 | 611 | -92.0 | 504990 | 711 | -99.8 | 504990 | 330 |
| MR_1774416376_82928891 | 504990 | 529 | -88.7 | 504990 | 611 | -93.1 | 504990 | 711 | -97.7 | 504990 | 330 |
| MR_1774416376_1C53C5C9 | 504990 | 529 | -89.6 | 504990 | 611 | -89.6 | 504990 | 711 | -98.9 | 504990 | 330 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 313: `1160d740-bab...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1160d740-bab1-40e4-81e0-45c00d008e78` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[313] topology](images/train_0313.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264023_2
- `C2`: Lift the tilt angle  of 3264023_2 by 7 degrees
- `C3`: Decrease A3 Offset threshold for 3221970_1
- `C4`: Increase A3 Offset threshold for 3264023_2
- `C5`: Add neighbor relationship between 3221970_1 and 3264023_2
- `C6`: Decrease transmission power for 3264023_2
- `C7`: Adjust the azimuth of 3221970_1 by 50 degrees
- `C8`: Press down the tilt angle of 3221970_1 by 5 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221970_1
- `C10`: Adjust the azimuth of 3264023_2 by 46 degrees
- `C11`: Add neighbor relationship between 3256970_4 and 3264023_2
- `C12`: Press down the tilt angle  of 3264023_2 by 7 degrees
- `C13`: Increase transmission power for 3264023_2
- `C14`: Decrease transmission power for 3221970_1
- `C15`: Decrease A3 Offset threshold for 3264023_2
- `C16`: Check test server and transmission issues
- `C17`: Lift the tilt angle of 3221970_1 by 5 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221970_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264023_2
- `C20`: Insufficient data; more data is needed for judgment. **← 정답**
- `C21`: Increase transmission power for 3221970_1
- `C22`: Increase A3 Offset threshold for 3221970_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.290 | MS1 | 121.4656695756 | 31.1446325298 | 425 | 504990 | -91.36 | 15.56 | 428.89 | 0.16 | 2.61 | 1574 |
| 2024-09-20 22:21:32.629 | MS1 | 121.4656646887 | 31.1446222814 | 425 | 504990 | -88.11 | 12.66 | 433.43 | 0.19 | 2.70 | 1568 |
| 2024-09-20 22:21:33.557 | MS1 | 121.4656702591 | 31.1446371826 | 425 | 504990 | -91.12 | 12.62 | 499.50 | 0.01 | 2.52 | 1594 |
| 2024-09-20 22:21:34.345 | MS1 | 121.4656721197 | 31.1446352526 | 425 | 504990 | -91.62 | 17.07 | 79.91 | 0.11 | 2.48 | 1580 |
| 2024-09-20 22:21:35.583 | MS1 | 121.4656602248 | 31.1446342117 | 425 | 504990 | -90.85 | 16.57 | 67.09 | 0.03 | 2.64 | 1570 |
| 2024-09-20 22:21:36.552 | MS1 | 121.4656676149 | 31.1446260528 | 425 | 504990 | -86.51 | 13.66 | 72.94 | 0.09 | 2.45 | 1599 |
| 2024-09-20 22:21:37.898 | MS1 | 121.4656665453 | 31.1446216027 | 425 | 504990 | -90.46 | 11.17 | 98.77 | 0.15 | 2.51 | 1590 |
| 2024-09-20 22:21:38.478 | MS1 | 121.4656673182 | 31.1446359449 | 425 | 504990 | -89.39 | 8.72 | 76.21 | 0.18 | 2.47 | 1592 |
| 2024-09-20 22:21:39.355 | MS1 | 121.4656612754 | 31.1446281792 | 425 | 504990 | -91.81 | 8.62 | 65.04 | 0.12 | 2.40 | 1597 |
| 2024-09-20 22:21:40.699 | MS1 | 121.4656702267 | 31.1446267163 | 425 | 504990 | -89.67 | 7.25 | 476.55 | 0.18 | 2.02 | 1571 |
| 2024-09-20 22:21:41.218 | MS1 | 121.4656654705 | 31.1446360702 | 425 | 504990 | -92.31 | 9.91 | 547.69 | 0.06 | 2.66 | 1592 |
| 2024-09-20 22:21:42.437 | MS1 | 121.4656712141 | 31.1446281221 | 425 | 504990 | -89.24 | 9.94 | 506.41 | 0.02 | 2.82 | 1570 |

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
| 3221970 | 1 | 121.4715975398 | 31.1471676699 | 145 | 1 | 8 | 48.5 | TDD | 425 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3248907 | 3 | 121.4659426911 | 31.1527311968 | 80 | 14 | 3 | 24.7 | TDD | 187 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3256970 | 4 | 121.4710740567 | 31.1461254159 | 296 | 8 | 12 | 27.8 | TDD | 459 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3264023 | 2 | 121.4712541101 | 31.1483864243 | 278 | 5 | 7 | 19.7 | TDD | 139 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.579 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.595 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.707 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.707 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.398 | NREventA3 | measId:2;ServCellPCI:931;Se... |
| 2024-09-20 22:21:38.638 | NRHandoverAttempt | SourcePCI:931;SourceNR-ARFC... |
| 2024-09-20 22:21:38.677 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.691 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.813 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.813 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3221970 | 1 | 92.5990 | 94.6516 | -116.1544 | 8.8414 | 185.2562 | 0.0148 | 0.0025 |
| 2024_09_19 22:00 | 3264023 | 2 | 79.1526 | 93.1685 | -114.2609 | 8.9048 | 103.9299 | 0.0128 | 0.0137 |
| 2024_09_19 22:00 | 3248907 | 3 | 81.7786 | 93.0784 | -114.7512 | 9.1318 | 193.4025 | 0.0029 | 0.0082 |
| 2024_09_19 22:00 | 3256970 | 4 | 93.1049 | 94.3830 | -114.6776 | 6.5247 | 121.7178 | 0.0161 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416893_A18E1575 | 504990 | 425 | -92.5 | 504990 | 139 | -93.2 | 504990 | 459 | -105.9 | 504990 | 187 |
| MR_1774416893_7196A66E | 504990 | 425 | -92.4 | 504990 | 139 | -95.8 | 504990 | 459 | -105.5 | 504990 | 187 |
| MR_1774416893_60BD94AF | 504990 | 425 | -92.4 | 504990 | 139 | -93.5 | 504990 | 459 | -102.7 | 504990 | 187 |
| MR_1774416893_E897EEBA | 504990 | 425 | -92.7 | 504990 | 139 | -95.8 | 504990 | 459 | -102.6 | 504990 | 187 |
| MR_1774416893_0B0E63C5 | 504990 | 425 | -93.0 | 504990 | 139 | -94.3 | 504990 | 459 | -104.3 | 504990 | 187 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 314: `b67643bc-15d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b67643bc-15d4-4444-b774-4c2a648237cd` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Lift the tilt angle  of 3242769_2 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[314] topology](images/train_0314.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237670_1
- `C2`: Increase transmission power for 3233346_4
- `C3`: Increase transmission power for 3237670_1
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Add neighbor relationship between 3233346_4 and 3237670_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233346_4
- `C7`: Adjust the azimuth of 3233346_4 by 49 degrees
- `C8`: Press down the tilt angle  of 3242769_2 by 7 degrees
- `C9`: Adjust the azimuth of 3242769_2 by 50 degrees
- `C10`: Lift the tilt angle  of 3242769_2 by 7 degrees **← 정답**
- `C11`: Increase A3 Offset threshold for 3233346_4
- `C12`: Decrease transmission power for 3237670_1
- `C13`: Decrease transmission power for 3233346_4
- `C14`: Add neighbor relationship between 3242769_2 and 3237670_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233346_4
- `C16`: Decrease A3 Offset threshold for 3233346_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237670_1
- `C18`: Increase A3 Offset threshold for 3237670_1
- `C19`: Press down the tilt angle of 3233346_4 by 4 degrees
- `C20`: Decrease A3 Offset threshold for 3237670_1
- `C21`: Lift the tilt angle of 3233346_4 by 4 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.336 | MS1 | 121.4656618037 | 31.1446351038 | 820 | 504990 | -86.87 | 13.31 | 312.54 | 0.16 | 2.13 | 1571 |
| 2024-09-20 22:21:32.913 | MS1 | 121.4656727417 | 31.1446267787 | 820 | 504990 | -90.96 | 15.37 | 506.28 | 0.15 | 2.45 | 1592 |
| 2024-09-20 22:21:33.742 | MS1 | 121.4656675855 | 31.1446244897 | 820 | 504990 | -88.41 | 12.08 | 415.88 | 0.06 | 2.50 | 1584 |
| 2024-09-20 22:21:34.545 | MS1 | 121.4656639628 | 31.1446276734 | 820 | 504990 | -86.77 | 13.71 | 83.34 | 0.00 | 2.90 | 1576 |
| 2024-09-20 22:21:35.788 | MS1 | 121.4656696251 | 31.1446294617 | 820 | 504990 | -87.16 | 15.58 | 86.95 | 0.16 | 2.75 | 1575 |
| 2024-09-20 22:21:36.608 | MS1 | 121.4656727659 | 31.1446261291 | 820 | 504990 | -86.01 | 12.23 | 91.92 | 0.04 | 2.35 | 1600 |
| 2024-09-20 22:21:37.876 | MS1 | 121.4656703764 | 31.1446199500 | 820 | 504990 | -90.37 | 10.37 | 100.98 | 0.15 | 2.18 | 1587 |
| 2024-09-20 22:21:38.794 | MS1 | 121.4656663606 | 31.1446260542 | 820 | 504990 | -90.47 | 9.70 | 61.38 | 0.02 | 2.51 | 1600 |
| 2024-09-20 22:21:39.789 | MS1 | 121.4656598938 | 31.1446201108 | 820 | 504990 | -91.85 | 8.39 | 52.91 | 0.03 | 2.83 | 1575 |
| 2024-09-20 22:21:40.690 | MS1 | 121.4656701007 | 31.1446373946 | 820 | 504990 | -92.72 | 11.42 | 501.64 | 0.18 | 2.74 | 1569 |
| 2024-09-20 22:21:41.991 | MS1 | 121.4656686205 | 31.1446207688 | 820 | 504990 | -91.96 | 7.67 | 444.15 | 0.19 | 2.41 | 1571 |
| 2024-09-20 22:21:42.912 | MS1 | 121.4656631663 | 31.1446249881 | 820 | 504990 | -91.55 | 10.70 | 305.43 | 0.19 | 2.64 | 1573 |

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
| 3233346 | 4 | 121.4725801108 | 31.1486858444 | 285 | 2 | 7 | 30.6 | TDD | 820 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3237670 | 1 | 121.4677003791 | 31.1514150154 | 328 | 5 | 8 | 32.3 | TDD | 976 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3242769 | 2 | 121.4660459570 | 31.1449647806 | 167 | 7 | 12 | 24.7 | TDD | 700 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3259652 | 3 | 121.4702727717 | 31.1550450056 | 77 | 10 | 2 | 48.3 | TDD | 53 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.259 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.276 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.384 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.384 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.148 | NREventA3 | measId:2;ServCellPCI:811;Se... |
| 2024-09-20 22:21:38.388 | NRHandoverAttempt | SourcePCI:811;SourceNR-ARFC... |
| 2024-09-20 22:21:38.425 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.439 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.581 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.581 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237670 | 1 | 13.5876 | 9.1161 | -115.4793 | 8.8118 | 146.0551 | 0.0044 | 0.0001 |
| 2024_09_20 22:00 | 3242769 | 2 | 17.0542 | 8.8618 | -117.0982 | 19.3230 | 82.7703 | 0.0136 | 0.0103 |
| 2024_09_20 22:00 | 3259652 | 3 | 17.6551 | 6.6832 | -114.7510 | 17.3059 | 181.9064 | 0.0123 | 0.0039 |
| 2024_09_20 22:00 | 3233346 | 4 | 93.9448 | 91.5732 | -114.8828 | 9.1957 | 88.7525 | 0.0002 | 0.0198 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412081_3EC81BF4 | 504990 | 820 | -86.1 | 504990 | 976 | -92.4 | 504990 | 700 | -97.8 | 504990 | 53 |
| MR_1774412081_0BC16469 | 504990 | 820 | -86.2 | 504990 | 976 | -93.8 | 504990 | 700 | -98.2 | 504990 | 53 |
| MR_1774412081_C2D32B5C | 504990 | 820 | -86.6 | 504990 | 976 | -94.3 | 504990 | 700 | -95.4 | 504990 | 53 |
| MR_1774412081_64AF0C5B | 504990 | 820 | -88.3 | 504990 | 976 | -93.1 | 504990 | 700 | -97.5 | 504990 | 53 |
| MR_1774412081_48199D6A | 504990 | 820 | -85.7 | 504990 | 976 | -91.7 | 504990 | 700 | -95.0 | 504990 | 53 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 315: `9c882599-395...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9c882599-395f-4a54-b879-0dc8df83ebc1` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Add neighbor relationship between 3249388_2 and 3229698_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[315] topology](images/train_0315.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3249388_2 by 8 degrees
- `C2`: Decrease transmission power for 3229698_1
- `C3`: Decrease A3 Offset threshold for 3249388_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249388_2
- `C5`: Increase A3 Offset threshold for 3249388_2
- `C6`: Decrease A3 Offset threshold for 3229698_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229698_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229698_1
- `C9`: Check test server and transmission issues
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249388_2
- `C11`: Add neighbor relationship between 3231701_4 and 3229698_1
- `C12`: Increase A3 Offset threshold for 3229698_1
- `C13`: Adjust the azimuth of 3249388_2 by 50 degrees
- `C14`: Increase transmission power for 3249388_2
- `C15`: Decrease transmission power for 3249388_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase transmission power for 3229698_1
- `C18`: Lift the tilt angle  of 3229698_1 by 4 degrees
- `C19`: Lift the tilt angle of 3249388_2 by 8 degrees
- `C20`: Adjust the azimuth of 3229698_1 by 33 degrees
- `C21`: Press down the tilt angle  of 3229698_1 by 4 degrees
- `C22`: Add neighbor relationship between 3249388_2 and 3229698_1 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.586 | MS1 | 121.4656761089 | 31.1446359146 | 217 | 504990 | -80.98 | 15.19 | 380.57 | 0.03 | 2.41 | 1594 |
| 2024-09-20 22:21:32.215 | MS1 | 121.4656741292 | 31.1446232564 | 217 | 504990 | -84.06 | 14.60 | 558.13 | 0.16 | 2.37 | 1578 |
| 2024-09-20 22:21:33.995 | MS1 | 121.4656601214 | 31.1446367918 | 217 | 504990 | -77.44 | 14.82 | 346.34 | 0.07 | 2.00 | 1596 |
| 2024-09-20 22:21:34.599 | MS1 | 121.4656707710 | 31.1446315549 | 217 | 504990 | -89.89 | -2.97 | 30.58 | 0.16 | 1.27 | 1589 |
| 2024-09-20 22:21:35.902 | MS1 | 121.4656745917 | 31.1446246973 | 217 | 504990 | -92.75 | -3.88 | 48.82 | 0.07 | 1.43 | 1580 |
| 2024-09-20 22:21:36.152 | MS1 | 121.4656608469 | 31.1446241900 | 217 | 504990 | -90.04 | -1.75 | 33.69 | 0.01 | 1.02 | 1595 |
| 2024-09-20 22:21:37.302 | MS1 | 121.4656595173 | 31.1446201942 | 217 | 504990 | -89.90 | -1.36 | 50.43 | 0.19 | 1.40 | 1567 |
| 2024-09-20 22:21:38.945 | MS1 | 121.4656674136 | 31.1446351174 | 217 | 504990 | -82.10 | 17.32 | 450.83 | 0.06 | 1.39 | 1589 |
| 2024-09-20 22:21:39.334 | MS1 | 121.4656677030 | 31.1446377552 | 217 | 504990 | -82.87 | 16.57 | 485.27 | 0.12 | 1.38 | 1598 |
| 2024-09-20 22:21:40.687 | MS1 | 121.4656693317 | 31.1446201935 | 217 | 504990 | -77.21 | 13.37 | 415.15 | 0.03 | 2.54 | 1576 |
| 2024-09-20 22:21:41.133 | MS1 | 121.4656606848 | 31.1446299415 | 217 | 504990 | -83.70 | 12.78 | 390.84 | 0.08 | 2.14 | 1565 |
| 2024-09-20 22:21:42.664 | MS1 | 121.4656692461 | 31.1446343849 | 217 | 504990 | -83.77 | 16.39 | 547.02 | 0.12 | 2.80 | 1598 |

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
| 3229698 | 1 | 121.4697854202 | 31.1481831736 | 258 | 1 | 9 | 31.9 | TDD | 981 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3231701 | 4 | 121.4654131471 | 31.1525413715 | 46 | 7 | 2 | 20.9 | TDD | 365 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3249388 | 2 | 121.4753094172 | 31.1516100660 | 160 | 6 | 9 | 33.1 | TDD | 217 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3250693 | 3 | 121.4685825211 | 31.1553617165 | 107 | 0 | 8 | 29.1 | TDD | 572 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.277 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.301 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.408 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.408 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.156 | NREventA3 | measId:2;ServCellPCI:743;Se... |
| 2024-09-20 22:21:36.156 | NREventA3 | measId:2;ServCellPCI:743;Se... |
| 2024-09-20 22:21:37.156 | NREventA3 | measId:2;ServCellPCI:743;Se... |
| 2024-09-20 22:21:39.656 | NRRRCReestablishAttempt | PCI:743 |
| 2024-09-20 22:21:39.667 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.682 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.809 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.809 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229698 | 1 | 7.5394 | 5.3541 | -117.6483 | 13.9262 | 143.6761 | 0.0113 | 0.0036 |
| 2024_09_20 22:00 | 3249388 | 2 | 13.5003 | 6.8063 | -117.3160 | 19.3510 | 97.2614 | 0.0031 | 0.1576 |
| 2024_09_20 22:00 | 3250693 | 3 | 13.1494 | 8.8921 | -116.2298 | 18.2694 | 187.3352 | 0.0026 | 0.0026 |
| 2024_09_20 22:00 | 3231701 | 4 | 9.2631 | 14.4006 | -116.2950 | 18.0308 | 123.1853 | 0.0194 | 0.0168 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412076_014ABB28 | 504990 | 217 | -88.6 | 504990 | 981 | -86.5 | 504990 | 365 | -89.5 | 504990 | 572 |
| MR_1774412076_63D9363B | 504990 | 217 | -88.8 | 504990 | 981 | -85.2 | 504990 | 365 | -88.4 | 504990 | 572 |
| MR_1774412076_355A17F6 | 504990 | 217 | -90.3 | 504990 | 981 | -85.9 | 504990 | 365 | -88.7 | 504990 | 572 |
| MR_1774412076_B3372C3B | 504990 | 981 | -84.2 | 504990 | 217 | -89.8 | 504990 | 365 | -88.9 | 504990 | 572 |
| MR_1774412076_C8C8F1FB | 504990 | 217 | -88.3 | 504990 | 981 | -83.6 | 504990 | 365 | -90.2 | 504990 | 572 |
| MR_1774412076_43F44EDB | 504990 | 217 | -91.5 | 504990 | 981 | -84.2 | 504990 | 365 | -89.7 | 504990 | 572 |
| MR_1774412076_D6ACECCD | 504990 | 217 | -88.3 | 504990 | 981 | -83.5 | 504990 | 365 | -88.6 | 504990 | 572 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 316: `7529ac63-933...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7529ac63-9331-4d92-b20c-779e22258a8d` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease A3 Offset threshold for 3266969_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[316] topology](images/train_0316.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229375_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266969_4
- `C3`: Increase A3 Offset threshold for 3229375_3
- `C4`: Press down the tilt angle of 3266969_4 by 10 degrees
- `C5`: Increase transmission power for 3229375_3
- `C6`: Decrease transmission power for 3266969_4
- `C7`: Lift the tilt angle  of 3229375_3 by 6 degrees
- `C8`: Decrease A3 Offset threshold for 3266969_4 **← 정답**
- `C9`: Adjust the azimuth of 3266969_4 by 37 degrees
- `C10`: Add neighbor relationship between 3250996_2 and 3229375_3
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Lift the tilt angle of 3266969_4 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3229375_3
- `C14`: Increase transmission power for 3266969_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266969_4
- `C16`: Add neighbor relationship between 3266969_4 and 3229375_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229375_3
- `C18`: Decrease transmission power for 3229375_3
- `C19`: Press down the tilt angle  of 3229375_3 by 6 degrees
- `C20`: Increase A3 Offset threshold for 3266969_4
- `C21`: Adjust the azimuth of 3229375_3 by 50 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.947 | MS1 | 121.4656748132 | 31.1446306423 | 238 | 504990 | -83.05 | 12.15 | 545.90 | 0.07 | 2.15 | 1572 |
| 2024-09-20 22:21:32.941 | MS1 | 121.4656711619 | 31.1446374745 | 238 | 504990 | -80.60 | 13.21 | 389.06 | 0.05 | 2.41 | 1570 |
| 2024-09-20 22:21:33.928 | MS1 | 121.4656744702 | 31.1446298940 | 238 | 504990 | -75.89 | 16.68 | 342.84 | 0.13 | 2.85 | 1594 |
| 2024-09-20 22:21:34.168 | MS1 | 121.4656718503 | 31.1446341930 | 238 | 504990 | -89.00 | -3.86 | 59.45 | 0.17 | 1.16 | 1561 |
| 2024-09-20 22:21:35.902 | MS1 | 121.4656648258 | 31.1446317658 | 238 | 504990 | -85.57 | -0.33 | 38.44 | 0.02 | 1.48 | 1582 |
| 2024-09-20 22:21:36.833 | MS1 | 121.4656724334 | 31.1446346203 | 238 | 504990 | -92.36 | -2.99 | 52.34 | 0.17 | 1.02 | 1581 |
| 2024-09-20 22:21:37.219 | MS1 | 121.4656666215 | 31.1446288397 | 238 | 504990 | -83.88 | -2.03 | 28.92 | 0.06 | 1.45 | 1575 |
| 2024-09-20 22:21:38.700 | MS1 | 121.4656667345 | 31.1446330854 | 238 | 504990 | -91.22 | -3.49 | 62.08 | 0.19 | 1.30 | 1584 |
| 2024-09-20 22:21:39.533 | MS1 | 121.4656643607 | 31.1446360183 | 884 | 504990 | -75.09 | 15.32 | 233.44 | 0.20 | 1.32 | 1584 |
| 2024-09-20 22:21:40.480 | MS1 | 121.4656727803 | 31.1446326823 | 884 | 504990 | -81.77 | 12.28 | 403.37 | 0.01 | 2.01 | 1563 |
| 2024-09-20 22:21:41.104 | MS1 | 121.4656769571 | 31.1446246483 | 884 | 504990 | -77.58 | 12.38 | 408.88 | 0.10 | 2.58 | 1589 |
| 2024-09-20 22:21:42.183 | MS1 | 121.4656644678 | 31.1446233588 | 884 | 504990 | -84.15 | 17.70 | 336.88 | 0.18 | 2.57 | 1571 |

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
| 3229375 | 3 | 121.4670360032 | 31.1524286477 | 29 | 4 | 1 | 28.6 | TDD | 884 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3248467 | 1 | 121.4707478764 | 31.1533945000 | 174 | 1 | 12 | 17.1 | TDD | 457 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3250996 | 2 | 121.4692962927 | 31.1496507022 | 354 | 0 | 6 | 15.3 | TDD | 523 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3266969 | 4 | 121.4712368648 | 31.1461102339 | 290 | 6 | 10 | 37.9 | TDD | 238 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.203 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.228 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.370 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.370 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.018 | NREventA3 | measId:2;ServCellPCI:62;Ser... |
| 2024-09-20 22:21:38.258 | NRHandoverAttempt | SourcePCI:62;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.288 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.303 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.404 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.404 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248467 | 1 | 9.7580 | 10.1495 | -117.2752 | 11.1948 | 118.7481 | 0.0116 | 0.0085 |
| 2024_09_20 22:00 | 3250996 | 2 | 9.7870 | 15.2865 | -116.2976 | 8.2560 | 149.1335 | 0.0188 | 0.0053 |
| 2024_09_20 22:00 | 3229375 | 3 | 16.1710 | 16.2124 | -117.2380 | 9.8908 | 149.7795 | 0.0182 | 0.0051 |
| 2024_09_20 22:00 | 3266969 | 4 | 13.4246 | 5.3894 | -117.5195 | 9.1512 | 133.6990 | 0.0055 | 0.1378 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413251_2818123B | 504990 | 884 | -82.5 | 504990 | 238 | -88.9 | 504990 | 523 | -85.9 | 504990 | 457 |
| MR_1774413251_49CC50F1 | 504990 | 884 | -81.6 | 504990 | 238 | -88.7 | 504990 | 523 | -84.2 | 504990 | 457 |
| MR_1774413251_07EADF61 | 504990 | 884 | -80.9 | 504990 | 238 | -87.3 | 504990 | 523 | -83.3 | 504990 | 457 |
| MR_1774413251_3557B6C2 | 504990 | 238 | -88.8 | 504990 | 884 | -80.8 | 504990 | 523 | -85.8 | 504990 | 457 |
| MR_1774413251_2085A5FC | 504990 | 884 | -80.7 | 504990 | 238 | -88.2 | 504990 | 523 | -86.3 | 504990 | 457 |
| MR_1774413251_37603E92 | 504990 | 238 | -88.5 | 504990 | 884 | -83.3 | 504990 | 523 | -84.8 | 504990 | 457 |
| MR_1774413251_AFE75746 | 504990 | 884 | -82.3 | 504990 | 238 | -89.3 | 504990 | 523 | -84.8 | 504990 | 457 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 317: `378819a1-ce7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `378819a1-ce7f-4a9e-82f8-70b5f8ccfa58` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3210554_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[317] topology](images/train_0317.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3210554_3
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Adjust the azimuth of 3277648_1 by 50 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210554_3
- `C5`: Increase A3 Offset threshold for 3210554_3
- `C6`: Lift the tilt angle of 3210554_3 by 5 degrees
- `C7`: Press down the tilt angle of 3210554_3 by 5 degrees
- `C8`: Increase transmission power for 3277648_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210554_3 **← 정답**
- `C10`: Adjust the azimuth of 3210554_3 by 24 degrees
- `C11`: Decrease transmission power for 3210554_3
- `C12`: Add neighbor relationship between 3210554_3 and 3277648_1
- `C13`: Decrease A3 Offset threshold for 3277648_1
- `C14`: Press down the tilt angle  of 3277648_1 by 10 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277648_1
- `C16`: Lift the tilt angle  of 3277648_1 by 10 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277648_1
- `C18`: Check test server and transmission issues
- `C19`: Increase A3 Offset threshold for 3277648_1
- `C20`: Add neighbor relationship between 3235862_4 and 3277648_1
- `C21`: Decrease transmission power for 3277648_1
- `C22`: Decrease A3 Offset threshold for 3210554_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.418 | MS1 | 121.4656627171 | 31.1446225457 | 460 | 504990 | -85.61 | 17.03 | 389.29 | 0.12 | 2.99 | 1569 |
| 2024-09-20 22:21:32.341 | MS1 | 121.4656606782 | 31.1446365570 | 460 | 504990 | -87.20 | 15.41 | 523.22 | 0.18 | 2.62 | 1595 |
| 2024-09-20 22:21:33.774 | MS1 | 121.4656769007 | 31.1446276809 | 460 | 504990 | -90.37 | 12.76 | 328.24 | 0.05 | 2.81 | 1571 |
| 2024-09-20 22:21:34.122 | MS1 | 121.4656772741 | 31.1446306817 | 460 | 504990 | -87.04 | 13.79 | 91.70 | 0.65 | 2.52 | 640 |
| 2024-09-20 22:21:35.748 | MS1 | 121.4656770064 | 31.1446225268 | 460 | 504990 | -85.28 | 17.58 | 75.80 | 0.61 | 2.34 | 526 |
| 2024-09-20 22:21:36.922 | MS1 | 121.4656638821 | 31.1446310308 | 460 | 504990 | -88.58 | 17.80 | 76.58 | 0.57 | 2.36 | 521 |
| 2024-09-20 22:21:37.284 | MS1 | 121.4656751045 | 31.1446308444 | 460 | 504990 | -92.27 | 7.10 | 84.40 | 0.51 | 2.88 | 583 |
| 2024-09-20 22:21:38.324 | MS1 | 121.4656580267 | 31.1446291513 | 460 | 504990 | -90.22 | 9.53 | 75.27 | 0.60 | 2.15 | 551 |
| 2024-09-20 22:21:39.625 | MS1 | 121.4656724639 | 31.1446243555 | 460 | 504990 | -91.13 | 12.01 | 59.28 | 0.57 | 2.33 | 617 |
| 2024-09-20 22:21:40.283 | MS1 | 121.4656671728 | 31.1446312148 | 460 | 504990 | -93.98 | 8.65 | 515.74 | 0.13 | 2.47 | 1567 |
| 2024-09-20 22:21:41.420 | MS1 | 121.4656616680 | 31.1446362189 | 460 | 504990 | -91.46 | 11.20 | 376.61 | 0.11 | 2.77 | 1596 |
| 2024-09-20 22:21:42.984 | MS1 | 121.4656639663 | 31.1446183754 | 460 | 504990 | -89.22 | 10.61 | 473.23 | 0.19 | 2.87 | 1578 |

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
| 3210554 | 3 | 121.4676819257 | 31.1555108857 | 213 | 4 | 2 | 15.7 | TDD | 460 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3233071 | 2 | 121.4744218881 | 31.1555721209 | 263 | 15 | 10 | 43.8 | TDD | 955 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3235862 | 4 | 121.4723706721 | 31.1529846094 | 264 | 13 | 2 | 34.7 | TDD | 861 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3277648 | 1 | 121.4663861600 | 31.1534283339 | 19 | 8 | 10 | 41.7 | TDD | 169 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.595 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.610 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.755 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.755 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.395 | NREventA3 | measId:2;ServCellPCI:749;Se... |
| 2024-09-20 22:21:38.635 | NRHandoverAttempt | SourcePCI:749;SourceNR-ARFC... |
| 2024-09-20 22:21:38.667 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.680 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.813 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.813 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277648 | 1 | 18.7077 | 10.9767 | -114.6384 | 13.3372 | 194.3692 | 0.0148 | 0.0200 |
| 2024_09_20 22:00 | 3233071 | 2 | 11.1154 | 16.1561 | -115.9386 | 12.2617 | 120.8048 | 0.0111 | 0.0034 |
| 2024_09_20 22:00 | 3210554 | 3 | 15.6641 | 14.3386 | -115.1863 | 8.0900 | 85.3769 | 0.0122 | 0.0002 |
| 2024_09_20 22:00 | 3235862 | 4 | 15.8312 | 19.2602 | -116.0614 | 14.3996 | 145.5209 | 0.0126 | 0.0114 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415766_16775AFA | 504990 | 460 | -87.3 | 504990 | 169 | -94.7 | 504990 | 861 | -97.3 | 504990 | 955 |
| MR_1774415766_8D0585C2 | 504990 | 460 | -87.3 | 504990 | 169 | -93.3 | 504990 | 861 | -97.2 | 504990 | 955 |
| MR_1774415766_E9D30FAC | 504990 | 460 | -87.3 | 504990 | 169 | -93.2 | 504990 | 861 | -98.3 | 504990 | 955 |
| MR_1774415766_044AACF1 | 504990 | 460 | -87.8 | 504990 | 169 | -93.6 | 504990 | 861 | -98.7 | 504990 | 955 |
| MR_1774415766_EE951D2E | 504990 | 460 | -85.5 | 504990 | 169 | -94.8 | 504990 | 861 | -97.9 | 504990 | 955 |
| MR_1774415766_8DA5B897 | 504990 | 460 | -85.7 | 504990 | 169 | -91.9 | 504990 | 861 | -99.4 | 504990 | 955 |
| MR_1774415766_23C26390 | 504990 | 460 | -85.9 | 504990 | 169 | -93.3 | 504990 | 861 | -96.1 | 504990 | 955 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 318: `df66899a-c28...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `df66899a-c289-4df4-9405-f494290b0c48` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Lift the tilt angle  of 3238985_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[318] topology](images/train_0318.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3277564_1
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Lift the tilt angle of 3277564_1 by 5 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276588_3
- `C5`: Add neighbor relationship between 3277564_1 and 3276588_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276588_3
- `C7`: Increase A3 Offset threshold for 3276588_3
- `C8`: Increase A3 Offset threshold for 3277564_1
- `C9`: Check test server and transmission issues
- `C10`: Decrease transmission power for 3276588_3
- `C11`: Decrease A3 Offset threshold for 3276588_3
- `C12`: Decrease transmission power for 3277564_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277564_1
- `C14`: Add neighbor relationship between 3238985_2 and 3276588_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277564_1
- `C16`: Press down the tilt angle of 3277564_1 by 5 degrees
- `C17`: Adjust the azimuth of 3238985_2 by 50 degrees
- `C18`: Lift the tilt angle  of 3238985_2 by 10 degrees **← 정답**
- `C19`: Press down the tilt angle  of 3238985_2 by 10 degrees
- `C20`: Increase transmission power for 3276588_3
- `C21`: Adjust the azimuth of 3277564_1 by 47 degrees
- `C22`: Decrease A3 Offset threshold for 3277564_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.425 | MS1 | 121.4656644117 | 31.1446296332 | 511 | 504990 | -87.67 | 12.49 | 475.53 | 0.20 | 2.22 | 1571 |
| 2024-09-20 22:21:32.802 | MS1 | 121.4656666528 | 31.1446310605 | 511 | 504990 | -90.78 | 13.50 | 516.05 | 0.13 | 2.29 | 1565 |
| 2024-09-20 22:21:33.797 | MS1 | 121.4656700109 | 31.1446361518 | 511 | 504990 | -88.28 | 14.95 | 456.83 | 0.12 | 2.09 | 1591 |
| 2024-09-20 22:21:34.979 | MS1 | 121.4656672600 | 31.1446298798 | 511 | 504990 | -87.98 | 17.90 | 63.49 | 0.06 | 2.32 | 1588 |
| 2024-09-20 22:21:35.115 | MS1 | 121.4656717021 | 31.1446356367 | 511 | 504990 | -90.34 | 12.22 | 99.22 | 0.10 | 2.63 | 1570 |
| 2024-09-20 22:21:36.367 | MS1 | 121.4656692366 | 31.1446250307 | 511 | 504990 | -90.06 | 15.23 | 88.97 | 0.20 | 2.15 | 1578 |
| 2024-09-20 22:21:37.450 | MS1 | 121.4656687918 | 31.1446324234 | 511 | 504990 | -91.06 | 12.03 | 60.77 | 0.04 | 2.40 | 1580 |
| 2024-09-20 22:21:38.849 | MS1 | 121.4656732867 | 31.1446244313 | 511 | 504990 | -91.52 | 10.90 | 74.52 | 0.19 | 2.96 | 1566 |
| 2024-09-20 22:21:39.496 | MS1 | 121.4656744199 | 31.1446241603 | 511 | 504990 | -91.49 | 10.41 | 75.36 | 0.15 | 2.45 | 1584 |
| 2024-09-20 22:21:40.247 | MS1 | 121.4656586776 | 31.1446349494 | 511 | 504990 | -92.76 | 11.56 | 321.04 | 0.17 | 2.30 | 1591 |
| 2024-09-20 22:21:41.972 | MS1 | 121.4656651205 | 31.1446190331 | 511 | 504990 | -89.80 | 9.74 | 563.94 | 0.09 | 2.73 | 1577 |
| 2024-09-20 22:21:42.928 | MS1 | 121.4656714336 | 31.1446275763 | 511 | 504990 | -93.63 | 11.64 | 324.20 | 0.19 | 2.10 | 1589 |

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
| 3238985 | 2 | 121.4675374203 | 31.1489839314 | 90 | 3 | 4 | 47.3 | TDD | 613 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3267463 | 4 | 121.4742302618 | 31.1462661154 | 138 | 14 | 7 | 27.8 | TDD | 831 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3276588 | 3 | 121.4666488512 | 31.1524016935 | 347 | 9 | 9 | 38.5 | TDD | 750 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3277564 | 1 | 121.4673884873 | 31.1551025821 | 235 | 3 | 11 | 43.8 | TDD | 511 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.360 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.379 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.520 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.520 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.245 | NREventA3 | measId:2;ServCellPCI:889;Se... |
| 2024-09-20 22:21:38.485 | NRHandoverAttempt | SourcePCI:889;SourceNR-ARFC... |
| 2024-09-20 22:21:38.528 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.543 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.662 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.662 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277564 | 1 | 85.4795 | 81.2492 | -117.5097 | 14.5455 | 116.4344 | 0.0066 | 0.0091 |
| 2024_09_20 22:00 | 3238985 | 2 | 11.4464 | 18.8622 | -117.6144 | 12.8170 | 165.9410 | 0.0176 | 0.0185 |
| 2024_09_20 22:00 | 3276588 | 3 | 11.2018 | 12.7634 | -114.1515 | 10.5186 | 151.6015 | 0.0139 | 0.0142 |
| 2024_09_20 22:00 | 3267463 | 4 | 10.4770 | 14.9473 | -115.6696 | 12.1285 | 194.6797 | 0.0122 | 0.0110 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415281_B3A3C05A | 504990 | 511 | -89.8 | 504990 | 750 | -93.3 | 504990 | 613 | -96.8 | 504990 | 831 |
| MR_1774415281_AA934900 | 504990 | 511 | -86.8 | 504990 | 750 | -94.0 | 504990 | 613 | -95.0 | 504990 | 831 |
| MR_1774415281_56D97ADE | 504990 | 511 | -88.0 | 504990 | 750 | -93.9 | 504990 | 613 | -94.5 | 504990 | 831 |
| MR_1774415281_922D87A6 | 504990 | 511 | -86.6 | 504990 | 750 | -94.8 | 504990 | 613 | -94.3 | 504990 | 831 |
| MR_1774415281_E38CCC9F | 504990 | 511 | -88.3 | 504990 | 750 | -94.6 | 504990 | 613 | -97.1 | 504990 | 831 |
| MR_1774415281_FAC00013 | 504990 | 511 | -86.6 | 504990 | 750 | -96.3 | 504990 | 613 | -95.0 | 504990 | 831 |
| MR_1774415281_F9D63307 | 504990 | 511 | -89.3 | 504990 | 750 | -96.2 | 504990 | 613 | -94.3 | 504990 | 831 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 319: `4adfa6c0-124...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4adfa6c0-1243-43f9-9ce7-f4297d5f9364` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Lift the tilt angle  of 3240383_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[319] topology](images/train_0319.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3219398_1 by 46 degrees
- `C2`: Press down the tilt angle  of 3240383_2 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276640_4
- `C4`: Increase transmission power for 3219398_1
- `C5`: Add neighbor relationship between 3219398_1 and 3276640_4
- `C6`: Lift the tilt angle of 3219398_1 by 5 degrees
- `C7`: Increase transmission power for 3276640_4
- `C8`: Decrease A3 Offset threshold for 3219398_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276640_4
- `C10`: Increase A3 Offset threshold for 3276640_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219398_1
- `C12`: Decrease transmission power for 3219398_1
- `C13`: Adjust the azimuth of 3240383_2 by 50 degrees
- `C14`: Lift the tilt angle  of 3240383_2 by 10 degrees **← 정답**
- `C15`: Check test server and transmission issues
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase A3 Offset threshold for 3219398_1
- `C18`: Decrease transmission power for 3276640_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219398_1
- `C20`: Press down the tilt angle of 3219398_1 by 5 degrees
- `C21`: Add neighbor relationship between 3240383_2 and 3276640_4
- `C22`: Decrease A3 Offset threshold for 3276640_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.524 | MS1 | 121.4656608037 | 31.1446190135 | 89 | 504990 | -90.81 | 17.63 | 410.94 | 0.05 | 2.37 | 1586 |
| 2024-09-20 22:21:32.427 | MS1 | 121.4656658268 | 31.1446329171 | 89 | 504990 | -91.02 | 17.39 | 431.03 | 0.15 | 2.00 | 1562 |
| 2024-09-20 22:21:33.778 | MS1 | 121.4656633825 | 31.1446245060 | 89 | 504990 | -87.40 | 13.27 | 461.01 | 0.16 | 2.21 | 1568 |
| 2024-09-20 22:21:34.439 | MS1 | 121.4656626438 | 31.1446231392 | 89 | 504990 | -91.98 | 16.73 | 88.03 | 0.06 | 2.80 | 1577 |
| 2024-09-20 22:21:35.526 | MS1 | 121.4656740572 | 31.1446196161 | 89 | 504990 | -91.40 | 13.64 | 82.22 | 0.02 | 2.05 | 1595 |
| 2024-09-20 22:21:36.556 | MS1 | 121.4656739731 | 31.1446374837 | 89 | 504990 | -87.62 | 15.48 | 95.44 | 0.06 | 2.86 | 1588 |
| 2024-09-20 22:21:37.775 | MS1 | 121.4656691010 | 31.1446228266 | 89 | 504990 | -93.97 | 7.45 | 72.62 | 0.02 | 2.53 | 1597 |
| 2024-09-20 22:21:38.334 | MS1 | 121.4656681937 | 31.1446248081 | 89 | 504990 | -90.48 | 10.71 | 85.46 | 0.14 | 2.32 | 1593 |
| 2024-09-20 22:21:39.653 | MS1 | 121.4656590917 | 31.1446253678 | 89 | 504990 | -89.34 | 7.79 | 58.77 | 0.04 | 2.57 | 1596 |
| 2024-09-20 22:21:40.927 | MS1 | 121.4656642549 | 31.1446186104 | 89 | 504990 | -92.38 | 8.27 | 347.20 | 0.04 | 2.90 | 1589 |
| 2024-09-20 22:21:41.328 | MS1 | 121.4656633821 | 31.1446212153 | 89 | 504990 | -93.79 | 10.32 | 393.28 | 0.04 | 2.48 | 1596 |
| 2024-09-20 22:21:42.677 | MS1 | 121.4656766385 | 31.1446241265 | 89 | 504990 | -90.68 | 9.19 | 549.72 | 0.08 | 2.43 | 1565 |

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
| 3219398 | 1 | 121.4719571228 | 31.1546882185 | 254 | 4 | 10 | 19.1 | TDD | 89 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3240383 | 2 | 121.4647754229 | 31.1444427881 | 248 | 6 | 0 | 46.2 | TDD | 386 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3264125 | 3 | 121.4662079624 | 31.1459508612 | 228 | 13 | 8 | 41.2 | TDD | 989 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3276640 | 4 | 121.4699229334 | 31.1544225197 | 282 | 9 | 9 | 21.8 | TDD | 439 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.435 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.451 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.584 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.584 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.312 | NREventA3 | measId:2;ServCellPCI:602;Se... |
| 2024-09-20 22:21:38.552 | NRHandoverAttempt | SourcePCI:602;SourceNR-ARFC... |
| 2024-09-20 22:21:38.584 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.597 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.723 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.723 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219398 | 1 | 88.9396 | 76.5424 | -115.8421 | 12.9019 | 128.9059 | 0.0066 | 0.0125 |
| 2024_09_20 22:00 | 3240383 | 2 | 7.0108 | 9.2876 | -114.8199 | 19.8373 | 185.7264 | 0.0047 | 0.0056 |
| 2024_09_20 22:00 | 3264125 | 3 | 14.0929 | 10.1659 | -116.9153 | 16.0772 | 186.0698 | 0.0077 | 0.0199 |
| 2024_09_20 22:00 | 3276640 | 4 | 9.1468 | 7.0345 | -115.6343 | 19.3424 | 102.5632 | 0.0164 | 0.0129 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414157_9FA5374B | 504990 | 89 | -91.1 | 504990 | 439 | -98.1 | 504990 | 386 | -104.4 | 504990 | 989 |
| MR_1774414157_E232FEC6 | 504990 | 89 | -90.2 | 504990 | 439 | -99.5 | 504990 | 386 | -107.8 | 504990 | 989 |
| MR_1774414157_72FF597A | 504990 | 89 | -91.9 | 504990 | 439 | -101.5 | 504990 | 386 | -105.2 | 504990 | 989 |
| MR_1774414157_AEB057C5 | 504990 | 89 | -90.8 | 504990 | 439 | -98.6 | 504990 | 386 | -106.9 | 504990 | 989 |
| MR_1774414157_AE3378CF | 504990 | 89 | -92.2 | 504990 | 439 | -101.3 | 504990 | 386 | -106.2 | 504990 | 989 |
| MR_1774414157_B114431B | 504990 | 89 | -90.7 | 504990 | 439 | -100.4 | 504990 | 386 | -106.1 | 504990 | 989 |
| MR_1774414157_101DFF2E | 504990 | 89 | -92.9 | 504990 | 439 | -101.4 | 504990 | 386 | -106.4 | 504990 | 989 |
| MR_1774414157_C9E4A603 | 504990 | 89 | -93.5 | 504990 | 439 | -97.8 | 504990 | 386 | -107.8 | 504990 | 989 |

> *... 2개 열 생략 (전체 14열)*

---
