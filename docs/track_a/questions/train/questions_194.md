# Track A 문제 분석 — train[1930]~train[1939]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1930] ~ train[1939] (10개)

## 목차

1. [문제 1930: `ecdb2c7e-d69...`](#1930) — single-answer, 정답: C20
2. [문제 1931: `f98a5115-26a...`](#1931) — single-answer, 정답: C13
3. [문제 1932: `72c9ec14-4ce...`](#1932) — single-answer, 정답: C9
4. [문제 1933: `03d2eb30-769...`](#1933) — single-answer, 정답: C21
5. [문제 1934: `0c23bce5-fb3...`](#1934) — single-answer, 정답: C8
6. [문제 1935: `8538b074-c00...`](#1935) — single-answer, 정답: C15
7. [문제 1936: `09f323e2-39a...`](#1936) — single-answer, 정답: C15
8. [문제 1937: `70c5893c-a34...`](#1937) — single-answer, 정답: C8
9. [문제 1938: `f4fe3e8e-77a...`](#1938) — single-answer, 정답: C14
10. [문제 1939: `73de42c4-cd4...`](#1939) — single-answer, 정답: C14

---

### 문제 1930: `ecdb2c7e-d69...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ecdb2c7e-d695-4c6e-ba60-eded63cc27c1` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1930] topology](images/train_1930.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3210015_2 by 9 degrees
- `C2`: Adjust the azimuth of 3210015_2 by 50 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210015_2
- `C4`: Decrease transmission power for 3240932_1
- `C5`: Increase A3 Offset threshold for 3210015_2
- `C6`: Add neighbor relationship between 3214832_4 and 3210015_2
- `C7`: Press down the tilt angle  of 3210015_2 by 9 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240932_1
- `C9`: Increase A3 Offset threshold for 3240932_1
- `C10`: Decrease A3 Offset threshold for 3240932_1
- `C11`: Add neighbor relationship between 3240932_1 and 3210015_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240932_1
- `C13`: Decrease transmission power for 3210015_2
- `C14`: Adjust the azimuth of 3240932_1 by 50 degrees
- `C15`: Decrease A3 Offset threshold for 3210015_2
- `C16`: Lift the tilt angle of 3240932_1 by 8 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase transmission power for 3210015_2
- `C19`: Press down the tilt angle of 3240932_1 by 8 degrees
- `C20`: Check test server and transmission issues **← 정답**
- `C21`: Increase transmission power for 3240932_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210015_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.783 | MS1 | 121.4656754823 | 31.1446355342 | 724 | 504990 | -85.60 | 15.95 | 425.79 | 0.05 | 2.15 | 1599 |
| 2024-09-20 22:21:32.755 | MS1 | 121.4656602088 | 31.1446198746 | 724 | 504990 | -90.29 | 12.86 | 502.82 | 0.18 | 2.80 | 1594 |
| 2024-09-20 22:21:33.163 | MS1 | 121.4656587812 | 31.1446292534 | 724 | 504990 | -85.89 | 13.69 | 585.83 | 0.00 | 2.72 | 1598 |
| 2024-09-20 22:21:34.511 | MS1 | 121.4656597039 | 31.1446186402 | 724 | 504990 | -90.91 | 13.60 | 62.29 | 0.03 | 2.82 | 413 |
| 2024-09-20 22:21:35.561 | MS1 | 121.4656642231 | 31.1446299778 | 724 | 504990 | -86.76 | 14.78 | 92.45 | 0.16 | 2.78 | 426 |
| 2024-09-20 22:21:36.761 | MS1 | 121.4656620766 | 31.1446333050 | 724 | 504990 | -89.18 | 12.35 | 69.90 | 0.11 | 2.60 | 496 |
| 2024-09-20 22:21:37.595 | MS1 | 121.4656773093 | 31.1446276664 | 724 | 504990 | -89.62 | 12.88 | 93.14 | 0.01 | 2.65 | 399 |
| 2024-09-20 22:21:38.320 | MS1 | 121.4656743511 | 31.1446272341 | 724 | 504990 | -90.36 | 10.69 | 61.88 | 0.18 | 2.37 | 360 |
| 2024-09-20 22:21:39.856 | MS1 | 121.4656750953 | 31.1446294503 | 724 | 504990 | -91.14 | 12.93 | 73.72 | 0.07 | 2.88 | 496 |
| 2024-09-20 22:21:40.442 | MS1 | 121.4656666887 | 31.1446323594 | 724 | 504990 | -89.39 | 7.65 | 312.66 | 0.17 | 2.87 | 1576 |
| 2024-09-20 22:21:41.198 | MS1 | 121.4656760729 | 31.1446243378 | 724 | 504990 | -91.33 | 7.49 | 502.03 | 0.12 | 2.87 | 1565 |
| 2024-09-20 22:21:42.946 | MS1 | 121.4656734415 | 31.1446271810 | 724 | 504990 | -89.43 | 11.88 | 548.67 | 0.19 | 2.06 | 1563 |

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
| 3210015 | 2 | 121.4728158513 | 31.1502508205 | 134 | 8 | 1 | 23.4 | TDD | 259 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3214832 | 4 | 121.4684100713 | 31.1505745460 | 211 | 1 | 3 | 23.2 | TDD | 13 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3240932 | 1 | 121.4649947010 | 31.1489499485 | 29 | 3 | 6 | 45.3 | TDD | 724 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3261740 | 3 | 121.4749410417 | 31.1546245595 | 325 | 7 | 12 | 30.1 | TDD | 708 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.530 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.555 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.681 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.681 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.422 | NREventA3 | measId:2;ServCellPCI:592;Se... |
| 2024-09-20 22:21:38.662 | NRHandoverAttempt | SourcePCI:592;SourceNR-ARFC... |
| 2024-09-20 22:21:38.707 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.718 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.843 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.843 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240932 | 1 | 9.8947 | 16.3750 | -117.1698 | 10.3343 | 117.3088 | 0.0012 | 0.0022 |
| 2024_09_20 22:00 | 3210015 | 2 | 17.5725 | 12.6193 | -114.0754 | 12.7428 | 132.4524 | 0.0190 | 0.0085 |
| 2024_09_20 22:00 | 3261740 | 3 | 13.5978 | 9.9212 | -116.4012 | 14.4510 | 198.8477 | 0.0037 | 0.0031 |
| 2024_09_20 22:00 | 3214832 | 4 | 9.7691 | 7.8045 | -114.4517 | 14.1069 | 133.1596 | 0.0067 | 0.0071 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416524_069CC0F8 | 504990 | 724 | -91.4 | 504990 | 259 | -96.0 | 504990 | 13 | -101.1 | 504990 | 708 |
| MR_1774416524_7D5E0BC0 | 504990 | 724 | -92.3 | 504990 | 259 | -94.1 | 504990 | 13 | -101.4 | 504990 | 708 |
| MR_1774416524_EBC1FFEF | 504990 | 724 | -92.0 | 504990 | 259 | -93.4 | 504990 | 13 | -101.2 | 504990 | 708 |
| MR_1774416524_249C6544 | 504990 | 724 | -92.4 | 504990 | 259 | -93.1 | 504990 | 13 | -103.9 | 504990 | 708 |
| MR_1774416524_057D4C99 | 504990 | 724 | -92.0 | 504990 | 259 | -94.5 | 504990 | 13 | -102.1 | 504990 | 708 |
| MR_1774416524_E5B84A06 | 504990 | 724 | -90.0 | 504990 | 259 | -92.9 | 504990 | 13 | -101.6 | 504990 | 708 |
| MR_1774416524_813CE552 | 504990 | 724 | -91.4 | 504990 | 259 | -93.2 | 504990 | 13 | -104.9 | 504990 | 708 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1931: `f98a5115-26a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f98a5115-26a2-4800-a9bd-f70d7a090424` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3257137_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1931] topology](images/train_1931.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3211263_2
- `C2`: Increase transmission power for 3211263_2
- `C3`: Increase A3 Offset threshold for 3211263_2
- `C4`: Increase A3 Offset threshold for 3257137_1
- `C5`: Decrease A3 Offset threshold for 3211263_2
- `C6`: Check test server and transmission issues
- `C7`: Decrease A3 Offset threshold for 3257137_1
- `C8`: Lift the tilt angle  of 3211263_2 by 10 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257137_1
- `C10`: Adjust the azimuth of 3211263_2 by 50 degrees
- `C11`: Decrease transmission power for 3257137_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211263_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257137_1 **← 정답**
- `C14`: Increase transmission power for 3257137_1
- `C15`: Press down the tilt angle of 3257137_1 by 5 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Lift the tilt angle of 3257137_1 by 5 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211263_2
- `C19`: Add neighbor relationship between 3276009_4 and 3211263_2
- `C20`: Add neighbor relationship between 3257137_1 and 3211263_2
- `C21`: Press down the tilt angle  of 3211263_2 by 10 degrees
- `C22`: Adjust the azimuth of 3257137_1 by 45 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.511 | MS1 | 121.4656750640 | 31.1446303339 | 467 | 504990 | -89.96 | 16.55 | 433.40 | 0.16 | 2.53 | 1568 |
| 2024-09-20 22:21:32.252 | MS1 | 121.4656657359 | 31.1446205328 | 467 | 504990 | -90.69 | 15.43 | 314.89 | 0.08 | 2.24 | 1600 |
| 2024-09-20 22:21:33.986 | MS1 | 121.4656655942 | 31.1446364118 | 467 | 504990 | -90.18 | 15.70 | 452.66 | 0.04 | 2.55 | 1574 |
| 2024-09-20 22:21:34.719 | MS1 | 121.4656718754 | 31.1446207076 | 467 | 504990 | -88.17 | 15.26 | 58.20 | 0.53 | 2.87 | 684 |
| 2024-09-20 22:21:35.514 | MS1 | 121.4656664919 | 31.1446278795 | 467 | 504990 | -89.42 | 17.64 | 59.64 | 0.58 | 2.33 | 582 |
| 2024-09-20 22:21:36.785 | MS1 | 121.4656614495 | 31.1446248046 | 467 | 504990 | -88.43 | 12.56 | 83.85 | 0.67 | 2.11 | 602 |
| 2024-09-20 22:21:37.830 | MS1 | 121.4656720572 | 31.1446309481 | 467 | 504990 | -90.83 | 8.91 | 88.75 | 0.67 | 2.67 | 583 |
| 2024-09-20 22:21:38.958 | MS1 | 121.4656747969 | 31.1446224695 | 467 | 504990 | -89.81 | 12.47 | 68.42 | 0.62 | 2.44 | 631 |
| 2024-09-20 22:21:39.866 | MS1 | 121.4656706610 | 31.1446358894 | 467 | 504990 | -91.48 | 9.07 | 75.82 | 0.62 | 2.94 | 689 |
| 2024-09-20 22:21:40.134 | MS1 | 121.4656733090 | 31.1446239554 | 467 | 504990 | -91.48 | 12.10 | 600.45 | 0.05 | 2.78 | 1574 |
| 2024-09-20 22:21:41.541 | MS1 | 121.4656631425 | 31.1446187866 | 467 | 504990 | -92.66 | 12.96 | 447.92 | 0.20 | 2.15 | 1599 |
| 2024-09-20 22:21:42.558 | MS1 | 121.4656732860 | 31.1446188613 | 467 | 504990 | -89.22 | 7.80 | 587.90 | 0.04 | 2.52 | 1585 |

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
| 3211263 | 2 | 121.4699559460 | 31.1452936553 | 9 | 14 | 9 | 18.9 | TDD | 995 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3235727 | 3 | 121.4660992203 | 31.1513358605 | 88 | 3 | 11 | 31.0 | TDD | 414 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3257137 | 1 | 121.4695804115 | 31.1524320967 | 158 | 3 | 4 | 29.7 | TDD | 467 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3276009 | 4 | 121.4738523309 | 31.1542589613 | 206 | 15 | 2 | 44.8 | TDD | 502 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.501 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.524 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.645 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.645 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.326 | NREventA3 | measId:2;ServCellPCI:139;Se... |
| 2024-09-20 22:21:38.566 | NRHandoverAttempt | SourcePCI:139;SourceNR-ARFC... |
| 2024-09-20 22:21:38.602 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.617 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.764 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.764 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257137 | 1 | 9.0518 | 13.8568 | -116.1440 | 9.5372 | 191.0167 | 0.0165 | 0.0158 |
| 2024_09_20 22:00 | 3211263 | 2 | 7.8966 | 11.3764 | -116.3246 | 18.2953 | 149.2792 | 0.0034 | 0.0140 |
| 2024_09_20 22:00 | 3235727 | 3 | 12.7291 | 10.5900 | -116.3546 | 8.9405 | 81.5465 | 0.0102 | 0.0001 |
| 2024_09_20 22:00 | 3276009 | 4 | 10.8777 | 12.3283 | -114.8775 | 10.9945 | 178.9187 | 0.0187 | 0.0054 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411982_9CCD7612 | 504990 | 467 | -88.4 | 504990 | 995 | -88.4 | 504990 | 502 | -97.5 | 504990 | 414 |
| MR_1774411982_D9D08228 | 504990 | 467 | -88.8 | 504990 | 995 | -87.9 | 504990 | 502 | -95.7 | 504990 | 414 |
| MR_1774411982_3C1B8BB0 | 504990 | 467 | -86.3 | 504990 | 995 | -90.3 | 504990 | 502 | -98.9 | 504990 | 414 |
| MR_1774411982_BD685EFA | 504990 | 467 | -89.4 | 504990 | 995 | -88.3 | 504990 | 502 | -96.0 | 504990 | 414 |
| MR_1774411982_C6940DAC | 504990 | 467 | -89.1 | 504990 | 995 | -90.9 | 504990 | 502 | -97.8 | 504990 | 414 |
| MR_1774411982_EDAD862C | 504990 | 467 | -86.5 | 504990 | 995 | -89.2 | 504990 | 502 | -97.0 | 504990 | 414 |
| MR_1774411982_82F44621 | 504990 | 467 | -89.7 | 504990 | 995 | -87.5 | 504990 | 502 | -98.8 | 504990 | 414 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1932: `72c9ec14-4ce...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `72c9ec14-4ce9-4f1c-9bce-c074119e0a2d` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1932] topology](images/train_1932.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3269367_1 by 10 degrees
- `C2`: Lift the tilt angle  of 3269243_3 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269367_1
- `C4`: Lift the tilt angle of 3269367_1 by 10 degrees
- `C5`: Adjust the azimuth of 3269243_3 by 50 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269367_1
- `C7`: Increase A3 Offset threshold for 3269243_3
- `C8`: Add neighbor relationship between 3269367_1 and 3269243_3
- `C9`: Insufficient data; more data is needed for judgment. **← 정답**
- `C10`: Check test server and transmission issues
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269243_3
- `C12`: Increase A3 Offset threshold for 3269367_1
- `C13`: Decrease transmission power for 3269243_3
- `C14`: Decrease A3 Offset threshold for 3269367_1
- `C15`: Increase transmission power for 3269243_3
- `C16`: Press down the tilt angle  of 3269243_3 by 10 degrees
- `C17`: Decrease A3 Offset threshold for 3269243_3
- `C18`: Increase transmission power for 3269367_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269243_3
- `C20`: Adjust the azimuth of 3269367_1 by 50 degrees
- `C21`: Add neighbor relationship between 3239434_4 and 3269243_3
- `C22`: Decrease transmission power for 3269367_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.815 | MS1 | 121.4656629700 | 31.1446235214 | 601 | 504990 | -89.51 | 15.15 | 527.36 | 0.09 | 2.36 | 1574 |
| 2024-09-20 22:21:32.479 | MS1 | 121.4656593569 | 31.1446312273 | 601 | 504990 | -89.85 | 14.88 | 568.36 | 0.14 | 2.19 | 1569 |
| 2024-09-20 22:21:33.361 | MS1 | 121.4656660124 | 31.1446330483 | 601 | 504990 | -88.15 | 13.17 | 525.57 | 0.20 | 2.36 | 1600 |
| 2024-09-20 22:21:34.815 | MS1 | 121.4656748946 | 31.1446327428 | 601 | 504990 | -86.39 | 14.53 | 86.60 | 0.17 | 2.15 | 1594 |
| 2024-09-20 22:21:35.776 | MS1 | 121.4656626747 | 31.1446284761 | 601 | 504990 | -90.91 | 17.41 | 77.09 | 0.17 | 2.11 | 1596 |
| 2024-09-20 22:21:36.310 | MS1 | 121.4656699535 | 31.1446369461 | 601 | 504990 | -87.88 | 17.91 | 87.44 | 0.01 | 2.50 | 1579 |
| 2024-09-20 22:21:37.219 | MS1 | 121.4656714895 | 31.1446249928 | 601 | 504990 | -90.27 | 11.36 | 86.98 | 0.17 | 2.72 | 1565 |
| 2024-09-20 22:21:38.845 | MS1 | 121.4656636889 | 31.1446253960 | 601 | 504990 | -93.45 | 7.75 | 66.47 | 0.07 | 2.44 | 1571 |
| 2024-09-20 22:21:39.198 | MS1 | 121.4656714524 | 31.1446302474 | 601 | 504990 | -91.89 | 11.48 | 66.80 | 0.09 | 2.79 | 1582 |
| 2024-09-20 22:21:40.323 | MS1 | 121.4656777690 | 31.1446191187 | 601 | 504990 | -93.89 | 9.85 | 467.07 | 0.12 | 2.12 | 1568 |
| 2024-09-20 22:21:41.126 | MS1 | 121.4656772525 | 31.1446243756 | 601 | 504990 | -92.60 | 7.11 | 562.13 | 0.17 | 2.53 | 1597 |
| 2024-09-20 22:21:42.219 | MS1 | 121.4656645158 | 31.1446271138 | 601 | 504990 | -89.90 | 10.25 | 352.60 | 0.09 | 2.56 | 1599 |

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
| 3239434 | 4 | 121.4729257941 | 31.1537979917 | 114 | 4 | 9 | 23.2 | TDD | 447 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3250371 | 2 | 121.4724223495 | 31.1457259756 | 325 | 14 | 11 | 34.0 | TDD | 4 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3269243 | 3 | 121.4722338642 | 31.1444669982 | 204 | 14 | 3 | 45.9 | TDD | 481 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3269367 | 1 | 121.4695237777 | 31.1559057603 | 141 | 15 | 1 | 37.7 | TDD | 601 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.928 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.951 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.061 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.061 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.798 | NREventA3 | measId:2;ServCellPCI:831;Se... |
| 2024-09-20 22:21:38.038 | NRHandoverAttempt | SourcePCI:831;SourceNR-ARFC... |
| 2024-09-20 22:21:38.074 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.089 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.220 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.220 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3269367 | 1 | 88.4650 | 82.9831 | -116.9711 | 7.9292 | 132.8418 | 0.0026 | 0.0070 |
| 2024_09_19 22:00 | 3250371 | 2 | 82.5008 | 78.7826 | -116.6882 | 7.4177 | 126.4320 | 0.0009 | 0.0027 |
| 2024_09_19 22:00 | 3269243 | 3 | 80.7238 | 80.5082 | -114.0361 | 14.2083 | 163.9047 | 0.0001 | 0.0149 |
| 2024_09_19 22:00 | 3239434 | 4 | 90.2144 | 89.1096 | -114.2817 | 15.8729 | 103.7867 | 0.0106 | 0.0121 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415979_A86D3524 | 504990 | 601 | -88.2 | 504990 | 481 | -91.0 | 504990 | 447 | -98.3 | 504990 | 4 |
| MR_1774415979_4C47955A | 504990 | 601 | -88.0 | 504990 | 481 | -90.7 | 504990 | 447 | -97.3 | 504990 | 4 |
| MR_1774415979_AB832425 | 504990 | 601 | -87.2 | 504990 | 481 | -88.8 | 504990 | 447 | -97.3 | 504990 | 4 |
| MR_1774415979_C5453985 | 504990 | 601 | -88.0 | 504990 | 481 | -90.1 | 504990 | 447 | -96.8 | 504990 | 4 |
| MR_1774415979_B89A2DA6 | 504990 | 601 | -87.2 | 504990 | 481 | -90.9 | 504990 | 447 | -99.3 | 504990 | 4 |
| MR_1774415979_3D51114D | 504990 | 601 | -87.0 | 504990 | 481 | -92.5 | 504990 | 447 | -97.2 | 504990 | 4 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1933: `03d2eb30-769...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `03d2eb30-769c-45c2-8455-283334a91ea0` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1933] topology](images/train_1933.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3232176_3 by 50 degrees
- `C2`: Decrease transmission power for 3239464_1
- `C3`: Decrease A3 Offset threshold for 3239464_1
- `C4`: Press down the tilt angle of 3239464_1 by 9 degrees
- `C5`: Increase transmission power for 3239464_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239464_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232176_3
- `C8`: Decrease transmission power for 3232176_3
- `C9`: Lift the tilt angle  of 3232176_3 by 10 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239464_1
- `C11`: Adjust the azimuth of 3239464_1 by 50 degrees
- `C12`: Increase transmission power for 3232176_3
- `C13`: Add neighbor relationship between 3239464_1 and 3232176_3
- `C14`: Check test server and transmission issues
- `C15`: Lift the tilt angle of 3239464_1 by 9 degrees
- `C16`: Add neighbor relationship between 3235354_4 and 3232176_3
- `C17`: Decrease A3 Offset threshold for 3232176_3
- `C18`: Increase A3 Offset threshold for 3232176_3
- `C19`: Increase A3 Offset threshold for 3239464_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232176_3
- `C21`: Insufficient data; more data is needed for judgment. **← 정답**
- `C22`: Press down the tilt angle  of 3232176_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.363 | MS1 | 121.4656640328 | 31.1446364929 | 89 | 504990 | -86.70 | 16.31 | 361.79 | 0.15 | 2.96 | 1591 |
| 2024-09-20 22:21:32.781 | MS1 | 121.4656708273 | 31.1446345323 | 89 | 504990 | -86.35 | 15.49 | 388.02 | 0.17 | 2.96 | 1598 |
| 2024-09-20 22:21:33.736 | MS1 | 121.4656648973 | 31.1446213842 | 89 | 504990 | -87.48 | 12.29 | 354.24 | 0.10 | 2.64 | 1589 |
| 2024-09-20 22:21:34.111 | MS1 | 121.4656640102 | 31.1446231466 | 89 | 504990 | -91.98 | 14.69 | 94.67 | 0.07 | 2.19 | 1599 |
| 2024-09-20 22:21:35.765 | MS1 | 121.4656622588 | 31.1446272446 | 89 | 504990 | -91.77 | 13.82 | 63.45 | 0.13 | 2.47 | 1598 |
| 2024-09-20 22:21:36.191 | MS1 | 121.4656760224 | 31.1446324672 | 89 | 504990 | -90.95 | 13.64 | 98.24 | 0.18 | 2.02 | 1562 |
| 2024-09-20 22:21:37.921 | MS1 | 121.4656629327 | 31.1446366097 | 89 | 504990 | -89.02 | 8.78 | 88.82 | 0.17 | 2.21 | 1590 |
| 2024-09-20 22:21:38.916 | MS1 | 121.4656601789 | 31.1446193920 | 89 | 504990 | -91.67 | 9.45 | 63.34 | 0.18 | 2.39 | 1566 |
| 2024-09-20 22:21:39.933 | MS1 | 121.4656588657 | 31.1446279012 | 89 | 504990 | -91.34 | 7.90 | 55.60 | 0.15 | 2.44 | 1588 |
| 2024-09-20 22:21:40.315 | MS1 | 121.4656685088 | 31.1446308537 | 89 | 504990 | -90.78 | 10.09 | 419.56 | 0.07 | 2.65 | 1569 |
| 2024-09-20 22:21:41.140 | MS1 | 121.4656758733 | 31.1446375330 | 89 | 504990 | -92.16 | 7.87 | 577.34 | 0.19 | 2.06 | 1573 |
| 2024-09-20 22:21:42.788 | MS1 | 121.4656672758 | 31.1446304977 | 89 | 504990 | -91.54 | 11.16 | 471.78 | 0.09 | 2.80 | 1594 |

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
| 3232176 | 3 | 121.4753771278 | 31.1520568705 | 59 | 10 | 7 | 27.1 | TDD | 929 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3235354 | 4 | 121.4726458295 | 31.1459412149 | 44 | 1 | 0 | 47.6 | TDD | 623 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3239464 | 1 | 121.4731339534 | 31.1464790847 | 76 | 6 | 8 | 40.8 | TDD | 89 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3253475 | 2 | 121.4750671164 | 31.1455352403 | 6 | 3 | 5 | 22.9 | TDD | 706 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.057 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.078 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.206 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.206 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.860 | NREventA3 | measId:2;ServCellPCI:623;Se... |
| 2024-09-20 22:21:38.100 | NRHandoverAttempt | SourcePCI:623;SourceNR-ARFC... |
| 2024-09-20 22:21:38.146 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.157 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.259 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.259 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3239464 | 1 | 79.8782 | 87.7500 | -115.3229 | 6.7624 | 168.3049 | 0.0128 | 0.0194 |
| 2024_09_19 22:00 | 3253475 | 2 | 78.5260 | 80.5649 | -116.3020 | 14.2786 | 98.0000 | 0.0033 | 0.0067 |
| 2024_09_19 22:00 | 3232176 | 3 | 93.7822 | 84.5739 | -117.0676 | 13.0759 | 166.5353 | 0.0150 | 0.0092 |
| 2024_09_19 22:00 | 3235354 | 4 | 83.2021 | 88.8097 | -114.9097 | 18.7364 | 95.8077 | 0.0001 | 0.0018 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415569_D6CAAA8F | 504990 | 89 | -92.5 | 504990 | 929 | -92.2 | 504990 | 623 | -101.4 | 504990 | 706 |
| MR_1774415569_14530A8E | 504990 | 89 | -91.9 | 504990 | 929 | -92.9 | 504990 | 623 | -103.1 | 504990 | 706 |
| MR_1774415569_8C60202F | 504990 | 89 | -92.0 | 504990 | 929 | -90.6 | 504990 | 623 | -100.9 | 504990 | 706 |
| MR_1774415569_C07A19E2 | 504990 | 89 | -93.6 | 504990 | 929 | -93.7 | 504990 | 623 | -100.7 | 504990 | 706 |
| MR_1774415569_BFF330DD | 504990 | 89 | -91.6 | 504990 | 929 | -90.9 | 504990 | 623 | -102.6 | 504990 | 706 |
| MR_1774415569_96EAD8C1 | 504990 | 89 | -91.8 | 504990 | 929 | -93.9 | 504990 | 623 | -102.0 | 504990 | 706 |
| MR_1774415569_1B6737E2 | 504990 | 89 | -92.4 | 504990 | 929 | -94.0 | 504990 | 623 | -100.9 | 504990 | 706 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1934: `0c23bce5-fb3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0c23bce5-fb3f-4073-a8fb-731083b496d5` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1934] topology](images/train_1934.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease A3 Offset threshold for 3262096_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259166_3
- `C4`: Add neighbor relationship between 3261452_4 and 3259166_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262096_2
- `C6`: Increase A3 Offset threshold for 3259166_3
- `C7`: Increase transmission power for 3259166_3
- `C8`: Insufficient data; more data is needed for judgment. **← 정답**
- `C9`: Adjust the azimuth of 3262096_2 by 41 degrees
- `C10`: Press down the tilt angle  of 3259166_3 by 7 degrees
- `C11`: Increase A3 Offset threshold for 3262096_2
- `C12`: Increase transmission power for 3262096_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259166_3
- `C14`: Decrease A3 Offset threshold for 3259166_3
- `C15`: Press down the tilt angle of 3262096_2 by 10 degrees
- `C16`: Adjust the azimuth of 3259166_3 by 50 degrees
- `C17`: Add neighbor relationship between 3262096_2 and 3259166_3
- `C18`: Decrease transmission power for 3262096_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262096_2
- `C20`: Decrease transmission power for 3259166_3
- `C21`: Lift the tilt angle  of 3259166_3 by 7 degrees
- `C22`: Lift the tilt angle of 3262096_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.680 | MS1 | 121.4656708568 | 31.1446249678 | 889 | 504990 | -87.29 | 16.12 | 562.39 | 0.05 | 2.87 | 1571 |
| 2024-09-20 22:21:32.636 | MS1 | 121.4656756650 | 31.1446287928 | 889 | 504990 | -86.58 | 12.19 | 377.77 | 0.03 | 2.41 | 1573 |
| 2024-09-20 22:21:33.359 | MS1 | 121.4656726509 | 31.1446309384 | 889 | 504990 | -88.28 | 14.38 | 572.75 | 0.03 | 2.75 | 1592 |
| 2024-09-20 22:21:34.569 | MS1 | 121.4656600393 | 31.1446219600 | 889 | 504990 | -91.57 | 14.11 | 63.55 | 0.04 | 2.19 | 1560 |
| 2024-09-20 22:21:35.473 | MS1 | 121.4656735718 | 31.1446311271 | 889 | 504990 | -91.09 | 15.21 | 46.48 | 0.19 | 2.35 | 1577 |
| 2024-09-20 22:21:36.985 | MS1 | 121.4656589936 | 31.1446182542 | 889 | 504990 | -89.85 | 17.34 | 85.48 | 0.14 | 2.69 | 1589 |
| 2024-09-20 22:21:37.178 | MS1 | 121.4656769807 | 31.1446223031 | 889 | 504990 | -89.25 | 9.16 | 81.07 | 0.16 | 2.86 | 1566 |
| 2024-09-20 22:21:38.338 | MS1 | 121.4656710830 | 31.1446284871 | 889 | 504990 | -93.57 | 7.49 | 83.77 | 0.07 | 2.12 | 1587 |
| 2024-09-20 22:21:39.519 | MS1 | 121.4656631978 | 31.1446201509 | 889 | 504990 | -93.61 | 8.93 | 71.49 | 0.11 | 2.74 | 1572 |
| 2024-09-20 22:21:40.226 | MS1 | 121.4656606661 | 31.1446284206 | 889 | 504990 | -89.80 | 8.52 | 606.99 | 0.16 | 2.22 | 1588 |
| 2024-09-20 22:21:41.535 | MS1 | 121.4656623449 | 31.1446250107 | 889 | 504990 | -90.22 | 11.70 | 554.78 | 0.08 | 2.61 | 1566 |
| 2024-09-20 22:21:42.929 | MS1 | 121.4656609740 | 31.1446341554 | 889 | 504990 | -90.24 | 8.38 | 455.87 | 0.07 | 2.91 | 1561 |

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
| 3259166 | 3 | 121.4719508026 | 31.1521961868 | 162 | 5 | 7 | 30.9 | TDD | 509 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3261452 | 4 | 121.4640227068 | 31.1546366145 | 64 | 6 | 10 | 18.3 | TDD | 990 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3262096 | 2 | 121.4716518010 | 31.1462679285 | 211 | 10 | 5 | 21.9 | TDD | 889 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3274682 | 1 | 121.4722211321 | 31.1534598768 | 108 | 6 | 4 | 28.1 | TDD | 824 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.302 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.324 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.452 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.452 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.175 | NREventA3 | measId:2;ServCellPCI:426;Se... |
| 2024-09-20 22:21:38.415 | NRHandoverAttempt | SourcePCI:426;SourceNR-ARFC... |
| 2024-09-20 22:21:38.450 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.462 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.568 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.568 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3274682 | 1 | 81.0868 | 93.0171 | -117.4328 | 15.5069 | 83.7028 | 0.0198 | 0.0150 |
| 2024_09_19 22:00 | 3262096 | 2 | 87.0680 | 87.1284 | -114.7143 | 16.8315 | 190.7566 | 0.0016 | 0.0001 |
| 2024_09_19 22:00 | 3259166 | 3 | 76.4955 | 80.6775 | -117.6655 | 19.3711 | 188.2181 | 0.0017 | 0.0193 |
| 2024_09_19 22:00 | 3261452 | 4 | 84.4929 | 80.1726 | -114.5886 | 10.3603 | 187.1315 | 0.0079 | 0.0015 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412682_43BDD3B1 | 504990 | 889 | -93.1 | 504990 | 509 | -96.6 | 504990 | 990 | -97.9 | 504990 | 824 |
| MR_1774412682_73F2E4D4 | 504990 | 889 | -93.1 | 504990 | 509 | -94.8 | 504990 | 990 | -98.7 | 504990 | 824 |
| MR_1774412682_E9F6BB25 | 504990 | 889 | -92.7 | 504990 | 509 | -96.9 | 504990 | 990 | -97.5 | 504990 | 824 |
| MR_1774412682_FFEC7FA9 | 504990 | 889 | -93.1 | 504990 | 509 | -94.2 | 504990 | 990 | -97.3 | 504990 | 824 |
| MR_1774412682_5337815F | 504990 | 889 | -91.1 | 504990 | 509 | -97.4 | 504990 | 990 | -99.3 | 504990 | 824 |
| MR_1774412682_84A3B53B | 504990 | 889 | -92.8 | 504990 | 509 | -97.4 | 504990 | 990 | -97.1 | 504990 | 824 |
| MR_1774412682_35836BAF | 504990 | 889 | -90.1 | 504990 | 509 | -95.1 | 504990 | 990 | -98.7 | 504990 | 824 |
| MR_1774412682_EB14D5BF | 504990 | 889 | -90.2 | 504990 | 509 | -94.6 | 504990 | 990 | -97.8 | 504990 | 824 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1935: `8538b074-c00...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8538b074-c009-4cb5-97ed-01c3da593101` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1935] topology](images/train_1935.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3232399_4
- `C2`: Decrease A3 Offset threshold for 3235419_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232399_4
- `C4`: Adjust the azimuth of 3232399_4 by 50 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235419_1
- `C6`: Increase A3 Offset threshold for 3235419_1
- `C7`: Press down the tilt angle  of 3232399_4 by 10 degrees
- `C8`: Lift the tilt angle  of 3232399_4 by 10 degrees
- `C9`: Press down the tilt angle of 3235419_1 by 10 degrees
- `C10`: Check test server and transmission issues
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232399_4
- `C12`: Decrease A3 Offset threshold for 3232399_4
- `C13`: Add neighbor relationship between 3275854_3 and 3232399_4
- `C14`: Increase transmission power for 3232399_4
- `C15`: Insufficient data; more data is needed for judgment. **← 정답**
- `C16`: Increase transmission power for 3235419_1
- `C17`: Lift the tilt angle of 3235419_1 by 10 degrees
- `C18`: Adjust the azimuth of 3235419_1 by 50 degrees
- `C19`: Decrease transmission power for 3235419_1
- `C20`: Add neighbor relationship between 3235419_1 and 3232399_4
- `C21`: Decrease transmission power for 3232399_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235419_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.531 | MS1 | 121.4656614794 | 31.1446211550 | 777 | 504990 | -86.29 | 16.16 | 556.20 | 0.15 | 2.58 | 1575 |
| 2024-09-20 22:21:32.374 | MS1 | 121.4656612265 | 31.1446293175 | 777 | 504990 | -86.03 | 15.05 | 361.51 | 0.18 | 2.74 | 1598 |
| 2024-09-20 22:21:33.964 | MS1 | 121.4656687725 | 31.1446288484 | 777 | 504990 | -90.85 | 16.48 | 533.95 | 0.13 | 2.39 | 1592 |
| 2024-09-20 22:21:34.350 | MS1 | 121.4656741903 | 31.1446242882 | 777 | 504990 | -86.85 | 15.96 | 86.14 | 0.18 | 2.92 | 1593 |
| 2024-09-20 22:21:35.756 | MS1 | 121.4656618453 | 31.1446277693 | 777 | 504990 | -89.06 | 17.57 | 68.74 | 0.05 | 2.75 | 1576 |
| 2024-09-20 22:21:36.548 | MS1 | 121.4656701387 | 31.1446278183 | 777 | 504990 | -89.51 | 17.89 | 96.53 | 0.00 | 2.62 | 1593 |
| 2024-09-20 22:21:37.723 | MS1 | 121.4656581520 | 31.1446277144 | 777 | 504990 | -90.02 | 11.43 | 48.95 | 0.17 | 2.39 | 1581 |
| 2024-09-20 22:21:38.943 | MS1 | 121.4656690206 | 31.1446333098 | 777 | 504990 | -92.32 | 7.21 | 63.40 | 0.15 | 3.00 | 1561 |
| 2024-09-20 22:21:39.915 | MS1 | 121.4656660035 | 31.1446372231 | 777 | 504990 | -93.91 | 9.13 | 48.72 | 0.15 | 2.94 | 1598 |
| 2024-09-20 22:21:40.889 | MS1 | 121.4656674818 | 31.1446186289 | 777 | 504990 | -89.84 | 8.44 | 492.61 | 0.10 | 2.89 | 1566 |
| 2024-09-20 22:21:41.680 | MS1 | 121.4656596914 | 31.1446342534 | 777 | 504990 | -91.67 | 11.77 | 415.28 | 0.12 | 2.02 | 1569 |
| 2024-09-20 22:21:42.771 | MS1 | 121.4656640601 | 31.1446229417 | 777 | 504990 | -89.07 | 12.22 | 491.62 | 0.06 | 2.72 | 1594 |

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
| 3231472 | 2 | 121.4685093082 | 31.1507719591 | 275 | 14 | 6 | 16.0 | TDD | 873 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3232399 | 4 | 121.4683418344 | 31.1540774918 | 292 | 10 | 12 | 33.7 | TDD | 105 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3235419 | 1 | 121.4641390997 | 31.1513754869 | 294 | 11 | 5 | 35.0 | TDD | 777 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3275854 | 3 | 121.4647174920 | 31.1552612195 | 297 | 7 | 4 | 16.5 | TDD | 366 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.937 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.960 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.060 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.060 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.757 | NREventA3 | measId:2;ServCellPCI:245;Se... |
| 2024-09-20 22:21:37.997 | NRHandoverAttempt | SourcePCI:245;SourceNR-ARFC... |
| 2024-09-20 22:21:38.028 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.039 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.162 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.162 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3235419 | 1 | 86.1846 | 91.2443 | -116.8952 | 18.2168 | 167.9441 | 0.0125 | 0.0128 |
| 2024_09_19 22:00 | 3231472 | 2 | 91.5184 | 85.4933 | -117.7452 | 9.3276 | 100.6760 | 0.0041 | 0.0047 |
| 2024_09_19 22:00 | 3275854 | 3 | 91.3569 | 79.6131 | -114.8321 | 9.5765 | 82.3700 | 0.0140 | 0.0088 |
| 2024_09_19 22:00 | 3232399 | 4 | 79.0074 | 78.2328 | -114.8224 | 10.8203 | 80.0347 | 0.0180 | 0.0070 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416984_796118F8 | 504990 | 777 | -88.0 | 504990 | 105 | -93.9 | 504990 | 366 | -95.4 | 504990 | 873 |
| MR_1774416984_124D3C71 | 504990 | 777 | -85.8 | 504990 | 105 | -91.8 | 504990 | 366 | -93.7 | 504990 | 873 |
| MR_1774416984_8566633C | 504990 | 777 | -86.7 | 504990 | 105 | -94.2 | 504990 | 366 | -95.5 | 504990 | 873 |
| MR_1774416984_694396F6 | 504990 | 777 | -88.2 | 504990 | 105 | -92.1 | 504990 | 366 | -93.7 | 504990 | 873 |
| MR_1774416984_812162AF | 504990 | 777 | -87.3 | 504990 | 105 | -92.2 | 504990 | 366 | -93.8 | 504990 | 873 |
| MR_1774416984_66B2E9B0 | 504990 | 777 | -84.9 | 504990 | 105 | -92.9 | 504990 | 366 | -96.9 | 504990 | 873 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1936: `09f323e2-39a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `09f323e2-39ac-419d-aaa7-dcbe3de06c77` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3245917_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1936] topology](images/train_1936.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3240183_4 by 10 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245917_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240183_4
- `C4`: Press down the tilt angle of 3245917_2 by 5 degrees
- `C5`: Decrease A3 Offset threshold for 3240183_4
- `C6`: Check test server and transmission issues
- `C7`: Increase A3 Offset threshold for 3245917_2
- `C8`: Increase A3 Offset threshold for 3240183_4
- `C9`: Increase transmission power for 3240183_4
- `C10`: Add neighbor relationship between 3227421_1 and 3240183_4
- `C11`: Decrease transmission power for 3240183_4
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Lift the tilt angle of 3245917_2 by 5 degrees
- `C14`: Adjust the azimuth of 3245917_2 by 6 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245917_2 **← 정답**
- `C16`: Adjust the azimuth of 3240183_4 by 50 degrees
- `C17`: Decrease A3 Offset threshold for 3245917_2
- `C18`: Press down the tilt angle  of 3240183_4 by 10 degrees
- `C19`: Add neighbor relationship between 3245917_2 and 3240183_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240183_4
- `C21`: Increase transmission power for 3245917_2
- `C22`: Decrease transmission power for 3245917_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.923 | MS1 | 121.4656614612 | 31.1446313293 | 409 | 504990 | -90.09 | 17.54 | 490.80 | 0.00 | 2.59 | 1598 |
| 2024-09-20 22:21:32.147 | MS1 | 121.4656671563 | 31.1446355489 | 409 | 504990 | -89.97 | 14.21 | 589.61 | 0.10 | 2.74 | 1571 |
| 2024-09-20 22:21:33.696 | MS1 | 121.4656774954 | 31.1446336622 | 409 | 504990 | -86.68 | 12.99 | 432.92 | 0.14 | 2.81 | 1579 |
| 2024-09-20 22:21:34.520 | MS1 | 121.4656753667 | 31.1446236055 | 409 | 504990 | -88.33 | 17.70 | 54.89 | 0.56 | 2.54 | 571 |
| 2024-09-20 22:21:35.317 | MS1 | 121.4656666534 | 31.1446339751 | 409 | 504990 | -86.13 | 13.04 | 55.14 | 0.57 | 2.61 | 597 |
| 2024-09-20 22:21:36.136 | MS1 | 121.4656776984 | 31.1446203924 | 409 | 504990 | -87.70 | 16.66 | 85.77 | 0.61 | 2.59 | 638 |
| 2024-09-20 22:21:37.641 | MS1 | 121.4656690459 | 31.1446329481 | 409 | 504990 | -89.13 | 7.69 | 60.07 | 0.64 | 2.28 | 657 |
| 2024-09-20 22:21:38.877 | MS1 | 121.4656636587 | 31.1446197913 | 409 | 504990 | -91.00 | 12.81 | 73.67 | 0.67 | 2.38 | 668 |
| 2024-09-20 22:21:39.216 | MS1 | 121.4656652806 | 31.1446251321 | 409 | 504990 | -91.26 | 8.98 | 81.16 | 0.65 | 2.34 | 616 |
| 2024-09-20 22:21:40.115 | MS1 | 121.4656705913 | 31.1446211242 | 409 | 504990 | -91.10 | 7.55 | 389.93 | 0.16 | 2.58 | 1568 |
| 2024-09-20 22:21:41.981 | MS1 | 121.4656610111 | 31.1446244461 | 409 | 504990 | -91.26 | 8.99 | 543.31 | 0.18 | 2.10 | 1587 |
| 2024-09-20 22:21:42.211 | MS1 | 121.4656610019 | 31.1446300367 | 409 | 504990 | -91.76 | 7.34 | 554.00 | 0.08 | 2.93 | 1581 |

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
| 3227421 | 1 | 121.4718711310 | 31.1538984360 | 203 | 15 | 9 | 32.0 | TDD | 976 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3240183 | 4 | 121.4641990445 | 31.1532222258 | 36 | 8 | 7 | 36.1 | TDD | 399 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3245561 | 3 | 121.4700944178 | 31.1532269611 | 302 | 11 | 5 | 43.2 | TDD | 668 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3245917 | 2 | 121.4694703783 | 31.1459640889 | 254 | 0 | 11 | 30.8 | TDD | 409 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.821 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.844 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.974 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.974 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.631 | NREventA3 | measId:2;ServCellPCI:976;Se... |
| 2024-09-20 22:21:37.871 | NRHandoverAttempt | SourcePCI:976;SourceNR-ARFC... |
| 2024-09-20 22:21:37.915 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.928 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.030 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.030 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227421 | 1 | 18.5270 | 10.4652 | -117.2390 | 19.6160 | 124.6939 | 0.0192 | 0.0002 |
| 2024_09_20 22:00 | 3245917 | 2 | 17.2374 | 13.8946 | -115.3116 | 16.6992 | 100.2586 | 0.0083 | 0.0112 |
| 2024_09_20 22:00 | 3245561 | 3 | 15.7975 | 18.5558 | -115.5350 | 12.1003 | 193.7205 | 0.0190 | 0.0042 |
| 2024_09_20 22:00 | 3240183 | 4 | 19.7424 | 7.0396 | -117.9196 | 19.1610 | 81.1735 | 0.0053 | 0.0079 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415520_96AB4738 | 504990 | 409 | -87.5 | 504990 | 399 | -91.9 | 504990 | 976 | -99.0 | 504990 | 668 |
| MR_1774415520_0F9D0EB0 | 504990 | 409 | -89.1 | 504990 | 399 | -90.1 | 504990 | 976 | -99.2 | 504990 | 668 |
| MR_1774415520_1E25A4FA | 504990 | 409 | -90.1 | 504990 | 399 | -92.0 | 504990 | 976 | -100.4 | 504990 | 668 |
| MR_1774415520_CC45997D | 504990 | 409 | -86.5 | 504990 | 399 | -90.2 | 504990 | 976 | -99.7 | 504990 | 668 |
| MR_1774415520_263145EE | 504990 | 409 | -88.0 | 504990 | 399 | -89.6 | 504990 | 976 | -102.2 | 504990 | 668 |
| MR_1774415520_E69B970F | 504990 | 409 | -88.0 | 504990 | 399 | -89.6 | 504990 | 976 | -99.7 | 504990 | 668 |
| MR_1774415520_4984670C | 504990 | 409 | -89.3 | 504990 | 399 | -91.7 | 504990 | 976 | -101.8 | 504990 | 668 |
| MR_1774415520_1BAC1ED8 | 504990 | 409 | -88.6 | 504990 | 399 | -90.3 | 504990 | 976 | -102.0 | 504990 | 668 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1937: `70c5893c-a34...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `70c5893c-a343-4041-a0aa-46f9deff4562` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Lift the tilt angle  of 3216090_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1937] topology](images/train_1937.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3259467_4
- `C2`: Increase A3 Offset threshold for 3259467_4
- `C3`: Check test server and transmission issues
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Press down the tilt angle  of 3216090_3 by 10 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218237_1
- `C7`: Adjust the azimuth of 3218237_1 by 18 degrees
- `C8`: Lift the tilt angle  of 3216090_3 by 10 degrees **← 정답**
- `C9`: Press down the tilt angle of 3218237_1 by 4 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259467_4
- `C11`: Add neighbor relationship between 3216090_3 and 3259467_4
- `C12`: Increase transmission power for 3218237_1
- `C13`: Increase A3 Offset threshold for 3218237_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259467_4
- `C15`: Add neighbor relationship between 3218237_1 and 3259467_4
- `C16`: Decrease transmission power for 3259467_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218237_1
- `C18`: Adjust the azimuth of 3216090_3 by 50 degrees
- `C19`: Decrease transmission power for 3218237_1
- `C20`: Decrease A3 Offset threshold for 3259467_4
- `C21`: Decrease A3 Offset threshold for 3218237_1
- `C22`: Lift the tilt angle of 3218237_1 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.634 | MS1 | 121.4656695170 | 31.1446301585 | 865 | 504990 | -89.53 | 12.80 | 352.22 | 0.01 | 2.43 | 1597 |
| 2024-09-20 22:21:32.529 | MS1 | 121.4656701384 | 31.1446229582 | 865 | 504990 | -90.94 | 15.40 | 571.23 | 0.10 | 2.10 | 1588 |
| 2024-09-20 22:21:33.890 | MS1 | 121.4656663062 | 31.1446324759 | 865 | 504990 | -88.40 | 14.51 | 413.75 | 0.01 | 2.29 | 1572 |
| 2024-09-20 22:21:34.579 | MS1 | 121.4656743940 | 31.1446275072 | 865 | 504990 | -88.21 | 16.92 | 61.73 | 0.02 | 2.53 | 1587 |
| 2024-09-20 22:21:35.135 | MS1 | 121.4656646091 | 31.1446254240 | 865 | 504990 | -90.01 | 17.50 | 100.50 | 0.03 | 2.55 | 1583 |
| 2024-09-20 22:21:36.586 | MS1 | 121.4656753110 | 31.1446194422 | 865 | 504990 | -87.61 | 12.31 | 67.91 | 0.03 | 2.83 | 1563 |
| 2024-09-20 22:21:37.911 | MS1 | 121.4656767402 | 31.1446247616 | 865 | 504990 | -93.13 | 9.50 | 64.17 | 0.08 | 2.60 | 1594 |
| 2024-09-20 22:21:38.966 | MS1 | 121.4656629289 | 31.1446307028 | 865 | 504990 | -91.56 | 10.17 | 92.50 | 0.10 | 2.54 | 1597 |
| 2024-09-20 22:21:39.613 | MS1 | 121.4656626520 | 31.1446253330 | 865 | 504990 | -89.33 | 11.82 | 92.34 | 0.04 | 2.33 | 1590 |
| 2024-09-20 22:21:40.186 | MS1 | 121.4656585173 | 31.1446241585 | 865 | 504990 | -90.72 | 7.38 | 449.34 | 0.08 | 2.81 | 1566 |
| 2024-09-20 22:21:41.240 | MS1 | 121.4656672774 | 31.1446253227 | 865 | 504990 | -90.70 | 7.15 | 365.53 | 0.06 | 2.96 | 1596 |
| 2024-09-20 22:21:42.235 | MS1 | 121.4656748263 | 31.1446196784 | 865 | 504990 | -89.81 | 11.60 | 407.05 | 0.11 | 2.60 | 1598 |

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
| 3211246 | 2 | 121.4711233381 | 31.1476938322 | 233 | 13 | 6 | 45.8 | TDD | 354 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3216090 | 3 | 121.4673968478 | 31.1463497366 | 18 | 12 | 3 | 25.7 | TDD | 339 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3218237 | 1 | 121.4640721277 | 31.1490099134 | 181 | 0 | 7 | 37.7 | TDD | 865 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3259467 | 4 | 121.4686862102 | 31.1558741430 | 60 | 9 | 2 | 39.8 | TDD | 5 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.296 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.318 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.436 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.436 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.145 | NREventA3 | measId:2;ServCellPCI:251;Se... |
| 2024-09-20 22:21:38.385 | NRHandoverAttempt | SourcePCI:251;SourceNR-ARFC... |
| 2024-09-20 22:21:38.427 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.439 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.552 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.552 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218237 | 1 | 88.1890 | 85.5302 | -114.8019 | 18.6969 | 159.5688 | 0.0089 | 0.0085 |
| 2024_09_20 22:00 | 3211246 | 2 | 6.5770 | 18.6622 | -115.8107 | 8.1503 | 151.4233 | 0.0062 | 0.0174 |
| 2024_09_20 22:00 | 3216090 | 3 | 9.1531 | 13.1653 | -116.4666 | 6.8511 | 196.8459 | 0.0113 | 0.0143 |
| 2024_09_20 22:00 | 3259467 | 4 | 7.2214 | 7.1428 | -114.0032 | 10.7814 | 94.8026 | 0.0180 | 0.0084 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417149_2B509985 | 504990 | 865 | -89.3 | 504990 | 5 | -92.9 | 504990 | 339 | -94.5 | 504990 | 354 |
| MR_1774417149_A6E602D9 | 504990 | 865 | -88.1 | 504990 | 5 | -94.1 | 504990 | 339 | -93.4 | 504990 | 354 |
| MR_1774417149_26FA7FE1 | 504990 | 865 | -88.6 | 504990 | 5 | -92.9 | 504990 | 339 | -94.2 | 504990 | 354 |
| MR_1774417149_3A213B5F | 504990 | 865 | -89.1 | 504990 | 5 | -94.5 | 504990 | 339 | -94.1 | 504990 | 354 |
| MR_1774417149_984C2490 | 504990 | 865 | -86.7 | 504990 | 5 | -93.7 | 504990 | 339 | -94.6 | 504990 | 354 |
| MR_1774417149_8D09E59B | 504990 | 865 | -86.2 | 504990 | 5 | -94.4 | 504990 | 339 | -93.4 | 504990 | 354 |
| MR_1774417149_13824854 | 504990 | 865 | -86.6 | 504990 | 5 | -92.7 | 504990 | 339 | -95.7 | 504990 | 354 |
| MR_1774417149_1FD74825 | 504990 | 865 | -87.3 | 504990 | 5 | -94.2 | 504990 | 339 | -95.4 | 504990 | 354 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1938: `f4fe3e8e-77a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f4fe3e8e-77aa-4caf-a30c-21ab9003aa5d` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Add neighbor relationship between 3221064_4 and 3217924_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1938] topology](images/train_1938.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3217924_1 by 17 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217924_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221064_4
- `C4`: Increase A3 Offset threshold for 3217924_1
- `C5`: Increase A3 Offset threshold for 3221064_4
- `C6`: Add neighbor relationship between 3240425_3 and 3217924_1
- `C7`: Lift the tilt angle  of 3217924_1 by 4 degrees
- `C8`: Decrease transmission power for 3221064_4
- `C9`: Lift the tilt angle of 3221064_4 by 2 degrees
- `C10`: Press down the tilt angle  of 3217924_1 by 4 degrees
- `C11`: Increase transmission power for 3221064_4
- `C12`: Decrease A3 Offset threshold for 3221064_4
- `C13`: Check test server and transmission issues
- `C14`: Add neighbor relationship between 3221064_4 and 3217924_1 **← 정답**
- `C15`: Adjust the azimuth of 3221064_4 by 50 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217924_1
- `C17`: Decrease A3 Offset threshold for 3217924_1
- `C18`: Decrease transmission power for 3217924_1
- `C19`: Press down the tilt angle of 3221064_4 by 2 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221064_4
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Increase transmission power for 3217924_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.159 | MS1 | 121.4656741409 | 31.1446200410 | 7 | 504990 | -78.22 | 12.47 | 510.23 | 0.12 | 2.41 | 1591 |
| 2024-09-20 22:21:32.852 | MS1 | 121.4656752855 | 31.1446200511 | 7 | 504990 | -80.30 | 13.38 | 498.31 | 0.08 | 2.78 | 1584 |
| 2024-09-20 22:21:33.332 | MS1 | 121.4656776514 | 31.1446317500 | 7 | 504990 | -80.79 | 14.69 | 395.96 | 0.18 | 2.56 | 1560 |
| 2024-09-20 22:21:34.732 | MS1 | 121.4656632349 | 31.1446270598 | 7 | 504990 | -92.65 | -1.66 | 60.32 | 0.07 | 1.30 | 1580 |
| 2024-09-20 22:21:35.631 | MS1 | 121.4656701661 | 31.1446379459 | 7 | 504990 | -89.09 | -0.31 | 71.43 | 0.18 | 1.25 | 1571 |
| 2024-09-20 22:21:36.304 | MS1 | 121.4656622757 | 31.1446298052 | 7 | 504990 | -89.94 | -1.80 | 57.86 | 0.18 | 1.33 | 1588 |
| 2024-09-20 22:21:37.309 | MS1 | 121.4656691101 | 31.1446213014 | 7 | 504990 | -93.60 | -1.21 | 31.37 | 0.05 | 1.42 | 1575 |
| 2024-09-20 22:21:38.163 | MS1 | 121.4656611338 | 31.1446263665 | 7 | 504990 | -75.24 | 15.91 | 368.29 | 0.00 | 1.37 | 1581 |
| 2024-09-20 22:21:39.288 | MS1 | 121.4656758858 | 31.1446301237 | 7 | 504990 | -78.90 | 17.01 | 403.47 | 0.19 | 1.18 | 1581 |
| 2024-09-20 22:21:40.585 | MS1 | 121.4656600316 | 31.1446329045 | 7 | 504990 | -84.82 | 12.93 | 393.80 | 0.13 | 2.33 | 1576 |
| 2024-09-20 22:21:41.410 | MS1 | 121.4656770636 | 31.1446299974 | 7 | 504990 | -81.08 | 17.36 | 496.64 | 0.14 | 2.05 | 1598 |
| 2024-09-20 22:21:42.716 | MS1 | 121.4656725950 | 31.1446228278 | 7 | 504990 | -80.41 | 12.77 | 564.82 | 0.16 | 2.93 | 1560 |

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
| 3217924 | 1 | 121.4705969761 | 31.1524117867 | 225 | 2 | 9 | 35.0 | TDD | 481 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3221064 | 4 | 121.4690451056 | 31.1492143545 | 116 | 0 | 10 | 26.0 | TDD | 7 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3240425 | 3 | 121.4715326192 | 31.1441393922 | 103 | 2 | 1 | 42.3 | TDD | 622 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3267707 | 2 | 121.4661040593 | 31.1453735186 | 109 | 2 | 11 | 30.4 | TDD | 125 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.374 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.392 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.515 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.515 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.200 | NREventA3 | measId:2;ServCellPCI:522;Se... |
| 2024-09-20 22:21:36.200 | NREventA3 | measId:2;ServCellPCI:522;Se... |
| 2024-09-20 22:21:37.200 | NREventA3 | measId:2;ServCellPCI:522;Se... |
| 2024-09-20 22:21:39.700 | NRRRCReestablishAttempt | PCI:522 |
| 2024-09-20 22:21:39.719 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.730 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.871 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.871 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217924 | 1 | 16.1559 | 6.1115 | -117.0762 | 13.9647 | 120.9680 | 0.0033 | 0.0126 |
| 2024_09_20 22:00 | 3267707 | 2 | 17.9381 | 9.1693 | -117.2991 | 5.4065 | 193.8488 | 0.0045 | 0.0045 |
| 2024_09_20 22:00 | 3240425 | 3 | 17.0347 | 7.8039 | -115.2797 | 18.3782 | 115.8333 | 0.0065 | 0.0012 |
| 2024_09_20 22:00 | 3221064 | 4 | 6.9887 | 10.3335 | -117.5604 | 9.2429 | 101.3909 | 0.0037 | 0.1409 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414360_678BA16C | 504990 | 7 | -93.9 | 504990 | 481 | -87.5 | 504990 | 622 | -91.7 | 504990 | 125 |
| MR_1774414360_6ABF35F9 | 504990 | 7 | -91.3 | 504990 | 481 | -87.3 | 504990 | 622 | -88.1 | 504990 | 125 |
| MR_1774414360_6441006E | 504990 | 481 | -87.8 | 504990 | 7 | -92.9 | 504990 | 622 | -90.3 | 504990 | 125 |
| MR_1774414360_0478EB0E | 504990 | 7 | -93.4 | 504990 | 481 | -89.2 | 504990 | 622 | -91.1 | 504990 | 125 |
| MR_1774414360_53D038BE | 504990 | 7 | -91.9 | 504990 | 481 | -89.6 | 504990 | 622 | -91.4 | 504990 | 125 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1939: `73de42c4-cd4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `73de42c4-cd4b-4f4a-9a43-c27a1b497dc8` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1939] topology](images/train_1939.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215122_3
- `C2`: Increase A3 Offset threshold for 3233324_4
- `C3`: Decrease A3 Offset threshold for 3233324_4
- `C4`: Check test server and transmission issues
- `C5`: Add neighbor relationship between 3237570_2 and 3233324_4
- `C6`: Increase transmission power for 3233324_4
- `C7`: Adjust the azimuth of 3233324_4 by 50 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215122_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233324_4
- `C10`: Decrease transmission power for 3233324_4
- `C11`: Decrease A3 Offset threshold for 3215122_3
- `C12`: Press down the tilt angle  of 3233324_4 by 7 degrees
- `C13`: Adjust the azimuth of 3215122_3 by 42 degrees
- `C14`: Insufficient data; more data is needed for judgment. **← 정답**
- `C15`: Add neighbor relationship between 3215122_3 and 3233324_4
- `C16`: Increase A3 Offset threshold for 3215122_3
- `C17`: Increase transmission power for 3215122_3
- `C18`: Press down the tilt angle of 3215122_3 by 10 degrees
- `C19`: Lift the tilt angle  of 3233324_4 by 7 degrees
- `C20`: Decrease transmission power for 3215122_3
- `C21`: Lift the tilt angle of 3215122_3 by 10 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233324_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.740 | MS1 | 121.4656732008 | 31.1446355241 | 414 | 504990 | -89.93 | 15.94 | 343.12 | 0.07 | 2.18 | 1567 |
| 2024-09-20 22:21:32.929 | MS1 | 121.4656667606 | 31.1446349973 | 414 | 504990 | -88.25 | 16.20 | 445.20 | 0.17 | 2.88 | 1565 |
| 2024-09-20 22:21:33.283 | MS1 | 121.4656718136 | 31.1446185408 | 414 | 504990 | -88.20 | 12.76 | 309.64 | 0.18 | 2.93 | 1569 |
| 2024-09-20 22:21:34.231 | MS1 | 121.4656747705 | 31.1446267430 | 414 | 504990 | -85.55 | 14.79 | 68.17 | 0.12 | 2.35 | 1572 |
| 2024-09-20 22:21:35.836 | MS1 | 121.4656660960 | 31.1446235342 | 414 | 504990 | -90.16 | 15.30 | 66.54 | 0.02 | 2.42 | 1596 |
| 2024-09-20 22:21:36.612 | MS1 | 121.4656664238 | 31.1446318750 | 414 | 504990 | -87.42 | 15.85 | 62.56 | 0.02 | 2.02 | 1587 |
| 2024-09-20 22:21:37.236 | MS1 | 121.4656586323 | 31.1446278693 | 414 | 504990 | -91.32 | 7.17 | 88.09 | 0.10 | 2.67 | 1591 |
| 2024-09-20 22:21:38.211 | MS1 | 121.4656653654 | 31.1446276092 | 414 | 504990 | -93.00 | 10.22 | 103.93 | 0.12 | 2.31 | 1589 |
| 2024-09-20 22:21:39.435 | MS1 | 121.4656709997 | 31.1446378134 | 414 | 504990 | -89.84 | 9.47 | 82.77 | 0.10 | 2.38 | 1565 |
| 2024-09-20 22:21:40.341 | MS1 | 121.4656757726 | 31.1446377245 | 414 | 504990 | -89.44 | 10.29 | 487.15 | 0.09 | 2.34 | 1564 |
| 2024-09-20 22:21:41.241 | MS1 | 121.4656776960 | 31.1446346003 | 414 | 504990 | -93.40 | 8.01 | 544.09 | 0.13 | 2.50 | 1591 |
| 2024-09-20 22:21:42.548 | MS1 | 121.4656606707 | 31.1446263733 | 414 | 504990 | -92.17 | 10.63 | 588.63 | 0.01 | 2.43 | 1572 |

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
| 3215122 | 3 | 121.4724713069 | 31.1475020198 | 202 | 12 | 1 | 48.9 | TDD | 414 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3233324 | 4 | 121.4669420478 | 31.1490796116 | 290 | 4 | 9 | 28.9 | TDD | 447 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3237570 | 2 | 121.4688960165 | 31.1440231117 | 216 | 11 | 9 | 49.3 | TDD | 778 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3238105 | 1 | 121.4694290518 | 31.1555723218 | 345 | 12 | 9 | 17.7 | TDD | 344 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.851 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.876 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.979 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.979 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.652 | NREventA3 | measId:2;ServCellPCI:618;Se... |
| 2024-09-20 22:21:37.892 | NRHandoverAttempt | SourcePCI:618;SourceNR-ARFC... |
| 2024-09-20 22:21:37.939 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.952 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.098 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.098 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3238105 | 1 | 77.7646 | 80.0829 | -114.4323 | 6.0148 | 159.9617 | 0.0177 | 0.0045 |
| 2024_09_19 22:00 | 3237570 | 2 | 92.7043 | 90.5344 | -116.7892 | 7.3187 | 173.2188 | 0.0162 | 0.0160 |
| 2024_09_19 22:00 | 3215122 | 3 | 78.4939 | 80.2976 | -114.7365 | 10.5037 | 110.3074 | 0.0009 | 0.0135 |
| 2024_09_19 22:00 | 3233324 | 4 | 80.5464 | 93.2837 | -117.9507 | 6.2257 | 101.0166 | 0.0149 | 0.0112 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416529_68F3237C | 504990 | 414 | -85.8 | 504990 | 447 | -89.4 | 504990 | 778 | -101.8 | 504990 | 344 |
| MR_1774416529_1F965C14 | 504990 | 414 | -86.5 | 504990 | 447 | -89.1 | 504990 | 778 | -101.9 | 504990 | 344 |
| MR_1774416529_BE76F18E | 504990 | 414 | -84.6 | 504990 | 447 | -87.1 | 504990 | 778 | -100.1 | 504990 | 344 |
| MR_1774416529_F1219ED6 | 504990 | 414 | -83.8 | 504990 | 447 | -87.5 | 504990 | 778 | -101.2 | 504990 | 344 |
| MR_1774416529_8DB5087C | 504990 | 414 | -86.9 | 504990 | 447 | -87.5 | 504990 | 778 | -100.2 | 504990 | 344 |
| MR_1774416529_E3E42211 | 504990 | 414 | -86.4 | 504990 | 447 | -90.4 | 504990 | 778 | -99.1 | 504990 | 344 |

> *... 2개 열 생략 (전체 14열)*

---
