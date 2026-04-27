# Track A 문제 분석 — train[1560]~train[1569]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1560] ~ train[1569] (10개)

## 목차

1. [문제 1560: `46bb2e87-b82...`](#1560) — single-answer, 정답: C12
2. [문제 1561: `0d21d1b5-9ed...`](#1561) — single-answer, 정답: C1
3. [문제 1562: `7ada5500-793...`](#1562) — single-answer, 정답: C5
4. [문제 1563: `ee5fb869-ee3...`](#1563) — multiple-answer, 정답: C10|C19
5. [문제 1564: `62697688-e8b...`](#1564) — single-answer, 정답: C17
6. [문제 1565: `2c82ebe4-df9...`](#1565) — multiple-answer, 정답: C2|C10
7. [문제 1566: `e7bbe20d-aa7...`](#1566) — single-answer, 정답: C16
8. [문제 1567: `eb0c5c4f-b0a...`](#1567) — single-answer, 정답: C15
9. [문제 1568: `bc400845-55d...`](#1568) — single-answer, 정답: C19
10. [문제 1569: `0af440cf-72f...`](#1569) — single-answer, 정답: C19

---

### 문제 1560: `46bb2e87-b82...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `46bb2e87-b82a-47af-894e-5c29f6fe7903` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3276844_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1560] topology](images/train_1560.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3276844_1
- `C2`: Decrease A3 Offset threshold for 3263578_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276844_1
- `C4`: Lift the tilt angle of 3276844_1 by 6 degrees
- `C5`: Add neighbor relationship between 3276844_1 and 3263578_2
- `C6`: Increase A3 Offset threshold for 3276844_1
- `C7`: Increase A3 Offset threshold for 3263578_2
- `C8`: Check test server and transmission issues
- `C9`: Add neighbor relationship between 3228978_4 and 3263578_2
- `C10`: Increase transmission power for 3276844_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263578_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276844_1 **← 정답**
- `C13`: Decrease transmission power for 3263578_2
- `C14`: Lift the tilt angle  of 3263578_2 by 10 degrees
- `C15`: Adjust the azimuth of 3263578_2 by 34 degrees
- `C16`: Adjust the azimuth of 3276844_1 by 26 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease transmission power for 3276844_1
- `C19`: Increase transmission power for 3263578_2
- `C20`: Press down the tilt angle  of 3263578_2 by 10 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263578_2
- `C22`: Press down the tilt angle of 3276844_1 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.419 | MS1 | 121.4656703596 | 31.1446217512 | 890 | 504990 | -91.40 | 14.76 | 503.63 | 0.12 | 2.61 | 1596 |
| 2024-09-20 22:21:32.245 | MS1 | 121.4656669098 | 31.1446198502 | 890 | 504990 | -87.03 | 16.13 | 378.03 | 0.11 | 2.48 | 1577 |
| 2024-09-20 22:21:33.827 | MS1 | 121.4656719537 | 31.1446311075 | 890 | 504990 | -85.31 | 14.08 | 500.45 | 0.17 | 2.68 | 1570 |
| 2024-09-20 22:21:34.666 | MS1 | 121.4656621916 | 31.1446313077 | 890 | 504990 | -86.74 | 16.43 | 86.23 | 0.54 | 2.96 | 621 |
| 2024-09-20 22:21:35.824 | MS1 | 121.4656582074 | 31.1446358554 | 890 | 504990 | -89.25 | 13.29 | 75.69 | 0.59 | 2.41 | 548 |
| 2024-09-20 22:21:36.490 | MS1 | 121.4656773234 | 31.1446210552 | 890 | 504990 | -91.32 | 17.71 | 61.55 | 0.63 | 2.68 | 620 |
| 2024-09-20 22:21:37.805 | MS1 | 121.4656762055 | 31.1446242327 | 890 | 504990 | -92.23 | 9.26 | 53.03 | 0.52 | 2.05 | 506 |
| 2024-09-20 22:21:38.447 | MS1 | 121.4656744972 | 31.1446232878 | 890 | 504990 | -92.08 | 7.48 | 87.53 | 0.67 | 2.67 | 571 |
| 2024-09-20 22:21:39.839 | MS1 | 121.4656729218 | 31.1446299431 | 890 | 504990 | -89.02 | 12.51 | 50.40 | 0.53 | 2.92 | 691 |
| 2024-09-20 22:21:40.795 | MS1 | 121.4656611609 | 31.1446231207 | 890 | 504990 | -91.37 | 8.14 | 343.76 | 0.04 | 2.59 | 1597 |
| 2024-09-20 22:21:41.712 | MS1 | 121.4656678907 | 31.1446273249 | 890 | 504990 | -89.28 | 10.48 | 518.98 | 0.02 | 2.92 | 1597 |
| 2024-09-20 22:21:42.125 | MS1 | 121.4656642029 | 31.1446249959 | 890 | 504990 | -93.87 | 7.80 | 384.16 | 0.08 | 2.64 | 1583 |

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
| 3228978 | 4 | 121.4715375928 | 31.1502909017 | 344 | 13 | 6 | 33.2 | TDD | 925 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3248200 | 3 | 121.4736868697 | 31.1503635425 | 258 | 12 | 8 | 33.1 | TDD | 629 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3263578 | 2 | 121.4748909239 | 31.1545570344 | 252 | 8 | 1 | 45.5 | TDD | 459 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3276844 | 1 | 121.4671753063 | 31.1459855450 | 197 | 1 | 11 | 16.8 | TDD | 890 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.841 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.857 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:30.997 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.997 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.703 | NREventA3 | measId:2;ServCellPCI:57;Ser... |
| 2024-09-20 22:21:37.943 | NRHandoverAttempt | SourcePCI:57;SourceNR-ARFCN... |
| 2024-09-20 22:21:37.978 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.992 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.108 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.108 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276844 | 1 | 17.2269 | 17.5752 | -116.6252 | 11.4658 | 181.0723 | 0.0073 | 0.0001 |
| 2024_09_20 22:00 | 3263578 | 2 | 13.3436 | 11.1962 | -117.8971 | 8.7006 | 180.5376 | 0.0172 | 0.0052 |
| 2024_09_20 22:00 | 3248200 | 3 | 14.3870 | 6.7510 | -116.0236 | 6.2544 | 82.1389 | 0.0027 | 0.0135 |
| 2024_09_20 22:00 | 3228978 | 4 | 14.3425 | 15.9303 | -115.6781 | 8.1032 | 191.3063 | 0.0100 | 0.0012 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415949_E3F1937D | 504990 | 890 | -85.5 | 504990 | 459 | -93.0 | 504990 | 925 | -93.8 | 504990 | 629 |
| MR_1774415949_F90EEA44 | 504990 | 890 | -88.7 | 504990 | 459 | -93.3 | 504990 | 925 | -95.3 | 504990 | 629 |
| MR_1774415949_C773D360 | 504990 | 890 | -86.3 | 504990 | 459 | -93.5 | 504990 | 925 | -95.4 | 504990 | 629 |
| MR_1774415949_B3D05C8A | 504990 | 890 | -85.0 | 504990 | 459 | -91.9 | 504990 | 925 | -95.0 | 504990 | 629 |
| MR_1774415949_BE0B1DAE | 504990 | 890 | -87.1 | 504990 | 459 | -95.5 | 504990 | 925 | -94.7 | 504990 | 629 |
| MR_1774415949_06FD3833 | 504990 | 890 | -85.9 | 504990 | 459 | -94.7 | 504990 | 925 | -93.9 | 504990 | 629 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1561: `0d21d1b5-9ed...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0d21d1b5-9ed9-4b48-976b-a31f1dbae1f7` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Add neighbor relationship between 3249490_1 and 3218289_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1561] topology](images/train_1561.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3249490_1 and 3218289_3 **← 정답**
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Press down the tilt angle of 3249490_1 by 4 degrees
- `C4`: Lift the tilt angle of 3249490_1 by 4 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218289_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249490_1
- `C7`: Lift the tilt angle  of 3218289_3 by 5 degrees
- `C8`: Increase transmission power for 3218289_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249490_1
- `C10`: Adjust the azimuth of 3218289_3 by 43 degrees
- `C11`: Adjust the azimuth of 3249490_1 by 50 degrees
- `C12`: Decrease A3 Offset threshold for 3249490_1
- `C13`: Check test server and transmission issues
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218289_3
- `C15`: Increase transmission power for 3249490_1
- `C16`: Decrease A3 Offset threshold for 3218289_3
- `C17`: Add neighbor relationship between 3278093_4 and 3218289_3
- `C18`: Increase A3 Offset threshold for 3249490_1
- `C19`: Increase A3 Offset threshold for 3218289_3
- `C20`: Decrease transmission power for 3249490_1
- `C21`: Press down the tilt angle  of 3218289_3 by 5 degrees
- `C22`: Decrease transmission power for 3218289_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.477 | MS1 | 121.4656660919 | 31.1446360974 | 857 | 504990 | -82.26 | 15.48 | 413.96 | 0.18 | 2.86 | 1578 |
| 2024-09-20 22:21:32.920 | MS1 | 121.4656595599 | 31.1446343525 | 857 | 504990 | -81.98 | 17.74 | 535.85 | 0.19 | 2.19 | 1592 |
| 2024-09-20 22:21:33.131 | MS1 | 121.4656644491 | 31.1446265239 | 857 | 504990 | -75.67 | 13.01 | 434.62 | 0.10 | 2.80 | 1576 |
| 2024-09-20 22:21:34.965 | MS1 | 121.4656742434 | 31.1446195625 | 857 | 504990 | -88.46 | -2.24 | 64.41 | 0.17 | 1.44 | 1595 |
| 2024-09-20 22:21:35.644 | MS1 | 121.4656747031 | 31.1446266935 | 857 | 504990 | -88.82 | -3.56 | 69.09 | 0.03 | 1.39 | 1588 |
| 2024-09-20 22:21:36.829 | MS1 | 121.4656746442 | 31.1446220143 | 857 | 504990 | -93.69 | -0.14 | 47.08 | 0.19 | 1.39 | 1569 |
| 2024-09-20 22:21:37.794 | MS1 | 121.4656654060 | 31.1446326839 | 857 | 504990 | -93.72 | -0.46 | 38.10 | 0.04 | 1.24 | 1595 |
| 2024-09-20 22:21:38.660 | MS1 | 121.4656750202 | 31.1446326831 | 857 | 504990 | -79.75 | 15.24 | 481.29 | 0.18 | 1.01 | 1570 |
| 2024-09-20 22:21:39.577 | MS1 | 121.4656695788 | 31.1446226678 | 857 | 504990 | -84.99 | 16.86 | 371.22 | 0.00 | 1.26 | 1572 |
| 2024-09-20 22:21:40.485 | MS1 | 121.4656703724 | 31.1446199577 | 857 | 504990 | -78.00 | 15.89 | 439.79 | 0.20 | 2.99 | 1585 |
| 2024-09-20 22:21:41.409 | MS1 | 121.4656725559 | 31.1446275677 | 857 | 504990 | -82.74 | 15.30 | 543.61 | 0.01 | 2.09 | 1568 |
| 2024-09-20 22:21:42.302 | MS1 | 121.4656668500 | 31.1446376194 | 857 | 504990 | -80.45 | 17.79 | 375.13 | 0.14 | 2.14 | 1599 |

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
| 3218289 | 3 | 121.4726841406 | 31.1551145040 | 253 | 3 | 8 | 40.6 | TDD | 497 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3222621 | 2 | 121.4696928703 | 31.1499072517 | 25 | 0 | 4 | 29.3 | TDD | 620 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3249490 | 1 | 121.4724391986 | 31.1493996189 | 26 | 2 | 12 | 32.4 | TDD | 857 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3278093 | 4 | 121.4753468022 | 31.1534844560 | 61 | 2 | 2 | 31.6 | TDD | 566 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.091 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.106 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.253 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.253 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.930 | NREventA3 | measId:2;ServCellPCI:33;Ser... |
| 2024-09-20 22:21:35.930 | NREventA3 | measId:2;ServCellPCI:33;Ser... |
| 2024-09-20 22:21:36.930 | NREventA3 | measId:2;ServCellPCI:33;Ser... |
| 2024-09-20 22:21:39.430 | NRRRCReestablishAttempt | PCI:33 |
| 2024-09-20 22:21:39.442 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.453 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.585 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.585 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249490 | 1 | 10.5304 | 17.9701 | -115.2177 | 7.9320 | 135.4659 | 0.0090 | 0.1827 |
| 2024_09_20 22:00 | 3222621 | 2 | 7.7702 | 8.7624 | -115.3769 | 5.9252 | 187.8479 | 0.0115 | 0.0029 |
| 2024_09_20 22:00 | 3218289 | 3 | 12.6498 | 19.6932 | -114.6875 | 6.7298 | 142.4174 | 0.0013 | 0.0164 |
| 2024_09_20 22:00 | 3278093 | 4 | 8.1408 | 5.7534 | -114.9086 | 11.2476 | 173.9356 | 0.0023 | 0.0173 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414843_9E2F3385 | 504990 | 857 | -90.1 | 504990 | 497 | -83.4 | 504990 | 566 | -93.6 | 504990 | 620 |
| MR_1774414843_1118BB2D | 504990 | 857 | -87.5 | 504990 | 497 | -83.8 | 504990 | 566 | -91.6 | 504990 | 620 |
| MR_1774414843_43A1DDE7 | 504990 | 857 | -89.7 | 504990 | 497 | -82.8 | 504990 | 566 | -93.1 | 504990 | 620 |
| MR_1774414843_38C055A5 | 504990 | 497 | -84.2 | 504990 | 857 | -88.2 | 504990 | 566 | -93.8 | 504990 | 620 |
| MR_1774414843_1C7208E5 | 504990 | 857 | -90.1 | 504990 | 497 | -80.8 | 504990 | 566 | -92.3 | 504990 | 620 |
| MR_1774414843_8EB2A3C7 | 504990 | 857 | -90.4 | 504990 | 497 | -82.8 | 504990 | 566 | -91.3 | 504990 | 620 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1562: `7ada5500-793...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7ada5500-793b-400a-a6d0-64a28c586a3e` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1562] topology](images/train_1562.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3219605_1 by 7 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215152_2
- `C3`: Decrease transmission power for 3215152_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215152_2
- `C5`: Insufficient data; more data is needed for judgment. **← 정답**
- `C6`: Decrease transmission power for 3219605_1
- `C7`: Increase transmission power for 3215152_2
- `C8`: Press down the tilt angle of 3215152_2 by 10 degrees
- `C9`: Increase transmission power for 3219605_1
- `C10`: Add neighbor relationship between 3245062_3 and 3219605_1
- `C11`: Decrease A3 Offset threshold for 3215152_2
- `C12`: Adjust the azimuth of 3219605_1 by 50 degrees
- `C13`: Increase A3 Offset threshold for 3215152_2
- `C14`: Lift the tilt angle of 3215152_2 by 10 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219605_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219605_1
- `C17`: Adjust the azimuth of 3215152_2 by 50 degrees
- `C18`: Decrease A3 Offset threshold for 3219605_1
- `C19`: Check test server and transmission issues
- `C20`: Lift the tilt angle  of 3219605_1 by 7 degrees
- `C21`: Add neighbor relationship between 3215152_2 and 3219605_1
- `C22`: Increase A3 Offset threshold for 3219605_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.286 | MS1 | 121.4656749053 | 31.1446360203 | 285 | 504990 | -89.32 | 12.25 | 538.83 | 0.18 | 2.26 | 1591 |
| 2024-09-20 22:21:32.127 | MS1 | 121.4656624564 | 31.1446325177 | 285 | 504990 | -85.53 | 16.14 | 398.86 | 0.04 | 2.56 | 1563 |
| 2024-09-20 22:21:33.543 | MS1 | 121.4656745593 | 31.1446328933 | 285 | 504990 | -91.54 | 17.20 | 416.63 | 0.02 | 2.32 | 1575 |
| 2024-09-20 22:21:34.808 | MS1 | 121.4656589190 | 31.1446185104 | 285 | 504990 | -86.97 | 12.39 | 60.98 | 0.14 | 2.18 | 1573 |
| 2024-09-20 22:21:35.237 | MS1 | 121.4656673564 | 31.1446330867 | 285 | 504990 | -89.18 | 17.96 | 109.27 | 0.12 | 2.10 | 1573 |
| 2024-09-20 22:21:36.430 | MS1 | 121.4656752786 | 31.1446224472 | 285 | 504990 | -90.95 | 12.52 | 102.06 | 0.05 | 2.24 | 1566 |
| 2024-09-20 22:21:37.400 | MS1 | 121.4656673003 | 31.1446232352 | 285 | 504990 | -89.68 | 9.47 | 69.44 | 0.00 | 2.73 | 1585 |
| 2024-09-20 22:21:38.631 | MS1 | 121.4656599967 | 31.1446331315 | 285 | 504990 | -93.27 | 7.42 | 66.95 | 0.03 | 2.92 | 1570 |
| 2024-09-20 22:21:39.884 | MS1 | 121.4656720835 | 31.1446334760 | 285 | 504990 | -92.94 | 9.43 | 91.19 | 0.01 | 2.61 | 1562 |
| 2024-09-20 22:21:40.359 | MS1 | 121.4656630824 | 31.1446227068 | 285 | 504990 | -89.01 | 10.50 | 316.56 | 0.15 | 2.16 | 1589 |
| 2024-09-20 22:21:41.285 | MS1 | 121.4656689184 | 31.1446206080 | 285 | 504990 | -92.31 | 9.58 | 443.31 | 0.03 | 2.64 | 1586 |
| 2024-09-20 22:21:42.244 | MS1 | 121.4656739226 | 31.1446256151 | 285 | 504990 | -89.04 | 11.10 | 351.05 | 0.10 | 2.84 | 1592 |

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
| 3215152 | 2 | 121.4654466238 | 31.1471850844 | 105 | 12 | 3 | 41.6 | TDD | 285 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3219605 | 1 | 121.4753495701 | 31.1498144665 | 321 | 6 | 10 | 15.5 | TDD | 360 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3245062 | 3 | 121.4741463096 | 31.1471061609 | 324 | 6 | 6 | 21.1 | TDD | 432 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3274593 | 4 | 121.4703335389 | 31.1483956558 | 263 | 1 | 4 | 34.8 | TDD | 495 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.588 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.606 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.748 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.748 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.478 | NREventA3 | measId:2;ServCellPCI:162;Se... |
| 2024-09-20 22:21:38.718 | NRHandoverAttempt | SourcePCI:162;SourceNR-ARFC... |
| 2024-09-20 22:21:38.766 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.777 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.905 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.905 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3219605 | 1 | 76.7661 | 76.8626 | -116.2923 | 15.0871 | 184.0667 | 0.0159 | 0.0073 |
| 2024_09_19 22:00 | 3215152 | 2 | 85.7149 | 83.5608 | -114.5458 | 8.2598 | 81.2230 | 0.0073 | 0.0024 |
| 2024_09_19 22:00 | 3245062 | 3 | 91.7479 | 75.8157 | -115.1429 | 9.3115 | 81.9029 | 0.0120 | 0.0115 |
| 2024_09_19 22:00 | 3274593 | 4 | 81.6145 | 90.5504 | -116.4621 | 8.2246 | 172.9038 | 0.0095 | 0.0151 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412473_266B25F4 | 504990 | 285 | -87.8 | 504990 | 360 | -87.5 | 504990 | 432 | -92.7 | 504990 | 495 |
| MR_1774412473_F025B6D4 | 504990 | 285 | -88.9 | 504990 | 360 | -89.8 | 504990 | 432 | -93.2 | 504990 | 495 |
| MR_1774412473_159CD7C3 | 504990 | 285 | -87.8 | 504990 | 360 | -87.5 | 504990 | 432 | -95.3 | 504990 | 495 |
| MR_1774412473_B12C699E | 504990 | 285 | -85.9 | 504990 | 360 | -86.8 | 504990 | 432 | -93.5 | 504990 | 495 |
| MR_1774412473_8DF832AD | 504990 | 285 | -85.5 | 504990 | 360 | -88.2 | 504990 | 432 | -95.5 | 504990 | 495 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1563: `ee5fb869-ee3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ee5fb869-ee3b-4eff-bdb2-46d00e571fa0` |
| Tag | **multiple-answer** |
| 정답 | **C10|C19** |
| C10 의미 | Increase transmission power for 3243203_1 |
| C19 의미 | Adjust the azimuth of 3243203_1 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1563] topology](images/train_1563.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Lift the tilt angle of 3243203_1 by 3 degrees
- `C3`: Lift the tilt angle  of 3263353_3 by 5 degrees
- `C4`: Decrease transmission power for 3263353_3
- `C5`: Press down the tilt angle  of 3263353_3 by 5 degrees
- `C6`: Increase transmission power for 3263353_3
- `C7`: Check test server and transmission issues
- `C8`: Decrease A3 Offset threshold for 3243203_1
- `C9`: Adjust the azimuth of 3263353_3 by 8 degrees
- `C10`: Increase transmission power for 3243203_1 **← 정답**
- `C11`: Increase A3 Offset threshold for 3243203_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263353_3
- `C13`: Decrease transmission power for 3243203_1
- `C14`: Add neighbor relationship between 3244308_4 and 3263353_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263353_3
- `C16`: Add neighbor relationship between 3243203_1 and 3263353_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243203_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243203_1
- `C19`: Adjust the azimuth of 3243203_1 by 50 degrees **← 정답**
- `C20`: Press down the tilt angle of 3243203_1 by 3 degrees
- `C21`: Decrease A3 Offset threshold for 3263353_3
- `C22`: Increase A3 Offset threshold for 3263353_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.837 | MS1 | 121.4656758637 | 31.1446224493 | 648 | 504990 | -85.73 | 17.89 | 502.33 | 0.06 | 2.63 | 1563 |
| 2024-09-20 22:21:32.422 | MS1 | 121.4656662526 | 31.1446347973 | 648 | 504990 | -93.84 | 16.15 | 601.53 | 0.09 | 2.71 | 1577 |
| 2024-09-20 22:21:33.206 | MS1 | 121.4656679152 | 31.1446357467 | 648 | 504990 | -91.76 | 15.07 | 515.96 | 0.08 | 2.66 | 1574 |
| 2024-09-20 22:21:34.855 | MS1 | 121.4656687781 | 31.1446359087 | 648 | 504990 | -107.48 | -1.45 | 72.23 | 0.11 | 1.01 | 1563 |
| 2024-09-20 22:21:35.729 | MS1 | 121.4656600846 | 31.1446216759 | 648 | 504990 | -108.29 | -0.95 | 51.60 | 0.13 | 1.15 | 1585 |
| 2024-09-20 22:21:36.554 | MS1 | 121.4656640654 | 31.1446265255 | 648 | 504990 | -106.18 | 0.13 | 38.34 | 0.02 | 1.08 | 1572 |
| 2024-09-20 22:21:37.514 | MS1 | 121.4656702053 | 31.1446334008 | 648 | 504990 | -108.22 | -1.23 | 17.72 | 0.12 | 1.37 | 1568 |
| 2024-09-20 22:21:38.925 | MS1 | 121.4656662347 | 31.1446292202 | 648 | 504990 | -101.86 | -1.92 | 71.67 | 0.06 | 1.13 | 1595 |
| 2024-09-20 22:21:39.598 | MS1 | 121.4656664283 | 31.1446211258 | 648 | 504990 | -105.04 | 1.28 | 54.36 | 0.20 | 1.07 | 1583 |
| 2024-09-20 22:21:40.815 | MS1 | 121.4656669722 | 31.1446185789 | 648 | 504990 | -92.40 | 13.31 | 436.57 | 0.03 | 2.54 | 1597 |
| 2024-09-20 22:21:41.909 | MS1 | 121.4656635849 | 31.1446313438 | 648 | 504990 | -93.32 | 17.64 | 500.83 | 0.12 | 2.68 | 1572 |
| 2024-09-20 22:21:42.297 | MS1 | 121.4656753552 | 31.1446271461 | 648 | 504990 | -87.74 | 16.42 | 326.55 | 0.16 | 2.98 | 1597 |

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
| 3243203 | 1 | 121.4741518376 | 31.1543032606 | 142 | 1 | 12 | 37.9 | TDD | 648 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3244308 | 4 | 121.4654129665 | 31.1497795864 | 113 | 6 | 8 | 30.0 | TDD | 103 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3263353 | 3 | 121.4714187365 | 31.1459545730 | 263 | 1 | 11 | 37.0 | TDD | 101 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3275932 | 2 | 121.4686449329 | 31.1482885673 | 318 | 13 | 12 | 24.0 | TDD | 849 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.334 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.359 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.479 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.479 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.669 | NREventA2 | measId:1;ServCellPCI:270;Se... |
| 2024-09-20 22:21:34.791 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243203 | 1 | 15.1179 | 7.1832 | -114.4343 | 11.7405 | 172.0787 | 0.1572 | 0.0182 |
| 2024_09_20 22:00 | 3275932 | 2 | 17.9717 | 16.4538 | -117.0234 | 14.2963 | 180.6406 | 0.0104 | 0.0120 |
| 2024_09_20 22:00 | 3263353 | 3 | 7.6977 | 8.9327 | -115.0595 | 6.7762 | 173.0523 | 0.0040 | 0.0127 |
| 2024_09_20 22:00 | 3244308 | 4 | 14.1278 | 8.1512 | -114.6722 | 17.7732 | 172.7400 | 0.0028 | 0.0189 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415153_DF06CE31 | 504990 | 648 | -108.7 | 504990 | 101 | -110.0 | 504990 | 103 | -116.9 | 504990 | 849 |
| MR_1774415153_B063E11E | 504990 | 648 | -105.5 | 504990 | 101 | -108.8 | 504990 | 103 | -118.2 | 504990 | 849 |
| MR_1774415153_A2B96AA2 | 504990 | 648 | -107.5 | 504990 | 101 | -108.8 | 504990 | 103 | -116.6 | 504990 | 849 |
| MR_1774415153_CC458E52 | 504990 | 648 | -106.1 | 504990 | 101 | -111.2 | 504990 | 103 | -115.2 | 504990 | 849 |
| MR_1774415153_0813006A | 504990 | 648 | -108.7 | 504990 | 101 | -111.8 | 504990 | 103 | -115.1 | 504990 | 849 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1564: `62697688-e8b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `62697688-e8b5-4d60-b41a-6279bd73fce8` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Lift the tilt angle  of 3279227_4 by 9 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1564] topology](images/train_1564.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3261278_1
- `C2`: Decrease A3 Offset threshold for 3261278_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261278_1
- `C4`: Press down the tilt angle of 3261278_1 by 3 degrees
- `C5`: Increase A3 Offset threshold for 3261278_1
- `C6`: Add neighbor relationship between 3279227_4 and 3268354_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268354_2
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase transmission power for 3268354_2
- `C10`: Adjust the azimuth of 3279227_4 by 50 degrees
- `C11`: Add neighbor relationship between 3261278_1 and 3268354_2
- `C12`: Increase transmission power for 3261278_1
- `C13`: Decrease A3 Offset threshold for 3268354_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261278_1
- `C15`: Check test server and transmission issues
- `C16`: Adjust the azimuth of 3261278_1 by 37 degrees
- `C17`: Lift the tilt angle  of 3279227_4 by 9 degrees **← 정답**
- `C18`: Increase A3 Offset threshold for 3268354_2
- `C19`: Press down the tilt angle  of 3279227_4 by 9 degrees
- `C20`: Lift the tilt angle of 3261278_1 by 3 degrees
- `C21`: Decrease transmission power for 3268354_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268354_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.733 | MS1 | 121.4656770915 | 31.1446341426 | 401 | 504990 | -91.91 | 12.56 | 497.90 | 0.14 | 2.42 | 1569 |
| 2024-09-20 22:21:32.388 | MS1 | 121.4656722871 | 31.1446362137 | 401 | 504990 | -87.63 | 13.83 | 566.32 | 0.12 | 2.46 | 1572 |
| 2024-09-20 22:21:33.392 | MS1 | 121.4656624102 | 31.1446280450 | 401 | 504990 | -86.28 | 12.95 | 463.46 | 0.12 | 2.69 | 1593 |
| 2024-09-20 22:21:34.832 | MS1 | 121.4656701194 | 31.1446252429 | 401 | 504990 | -91.37 | 15.99 | 49.27 | 0.15 | 2.55 | 1572 |
| 2024-09-20 22:21:35.993 | MS1 | 121.4656728117 | 31.1446367240 | 401 | 504990 | -91.79 | 12.06 | 101.46 | 0.18 | 2.57 | 1591 |
| 2024-09-20 22:21:36.334 | MS1 | 121.4656700051 | 31.1446218308 | 401 | 504990 | -89.25 | 16.98 | 79.67 | 0.09 | 2.24 | 1593 |
| 2024-09-20 22:21:37.213 | MS1 | 121.4656666062 | 31.1446337332 | 401 | 504990 | -93.55 | 11.66 | 70.94 | 0.07 | 2.47 | 1584 |
| 2024-09-20 22:21:38.427 | MS1 | 121.4656723354 | 31.1446279137 | 401 | 504990 | -91.25 | 8.58 | 75.52 | 0.05 | 2.14 | 1567 |
| 2024-09-20 22:21:39.157 | MS1 | 121.4656774958 | 31.1446372867 | 401 | 504990 | -93.34 | 7.92 | 56.15 | 0.11 | 2.51 | 1577 |
| 2024-09-20 22:21:40.331 | MS1 | 121.4656624508 | 31.1446300892 | 401 | 504990 | -90.55 | 8.82 | 518.44 | 0.07 | 2.10 | 1571 |
| 2024-09-20 22:21:41.788 | MS1 | 121.4656629679 | 31.1446321056 | 401 | 504990 | -92.18 | 8.14 | 363.36 | 0.19 | 2.70 | 1588 |
| 2024-09-20 22:21:42.210 | MS1 | 121.4656766010 | 31.1446252019 | 401 | 504990 | -93.01 | 8.72 | 350.96 | 0.20 | 2.63 | 1570 |

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
| 3245946 | 3 | 121.4694616168 | 31.1447964609 | 331 | 8 | 0 | 36.2 | TDD | 614 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3261278 | 1 | 121.4664229599 | 31.1550165492 | 147 | 1 | 2 | 42.0 | TDD | 401 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3268354 | 2 | 121.4703834300 | 31.1451504356 | 354 | 3 | 11 | 47.8 | TDD | 531 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3279227 | 4 | 121.4658928746 | 31.1470784383 | 263 | 0 | 11 | 32.6 | TDD | 297 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.968 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.107 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.107 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.809 | NREventA3 | measId:2;ServCellPCI:477;Se... |
| 2024-09-20 22:21:38.049 | NRHandoverAttempt | SourcePCI:477;SourceNR-ARFC... |
| 2024-09-20 22:21:38.088 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.099 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.201 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.201 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261278 | 1 | 86.3881 | 87.6026 | -116.0162 | 10.8522 | 182.7898 | 0.0166 | 0.0044 |
| 2024_09_20 22:00 | 3268354 | 2 | 10.1966 | 19.3252 | -116.8755 | 5.2004 | 91.8823 | 0.0155 | 0.0114 |
| 2024_09_20 22:00 | 3245946 | 3 | 5.1352 | 14.3967 | -115.1626 | 15.9810 | 98.5268 | 0.0105 | 0.0117 |
| 2024_09_20 22:00 | 3279227 | 4 | 11.4902 | 8.7429 | -117.4195 | 8.1747 | 173.9472 | 0.0059 | 0.0103 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417068_900D08B0 | 504990 | 401 | -92.5 | 504990 | 531 | -97.7 | 504990 | 297 | -101.4 | 504990 | 614 |
| MR_1774417068_3D3E6392 | 504990 | 401 | -92.0 | 504990 | 531 | -98.5 | 504990 | 297 | -101.8 | 504990 | 614 |
| MR_1774417068_4A3424FE | 504990 | 401 | -91.3 | 504990 | 531 | -99.5 | 504990 | 297 | -100.4 | 504990 | 614 |
| MR_1774417068_9CCA77DF | 504990 | 401 | -91.3 | 504990 | 531 | -96.8 | 504990 | 297 | -99.2 | 504990 | 614 |
| MR_1774417068_510B99FD | 504990 | 401 | -89.9 | 504990 | 531 | -98.1 | 504990 | 297 | -99.5 | 504990 | 614 |
| MR_1774417068_DDDEE7C0 | 504990 | 401 | -90.2 | 504990 | 531 | -97.6 | 504990 | 297 | -98.4 | 504990 | 614 |
| MR_1774417068_55140F71 | 504990 | 401 | -92.8 | 504990 | 531 | -98.3 | 504990 | 297 | -98.7 | 504990 | 614 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1565: `2c82ebe4-df9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2c82ebe4-df95-490a-9ef7-5490c6972bcf` |
| Tag | **multiple-answer** |
| 정답 | **C2|C10** |
| C2 의미 | Press down the tilt angle  of 3228869_3 by 3 degrees |
| C10 의미 | Decrease transmission power for 3228869_3 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1565] topology](images/train_1565.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3240183_2
- `C2`: Press down the tilt angle  of 3228869_3 by 3 degrees **← 정답**
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240183_2
- `C4`: Increase A3 Offset threshold for 3228869_3
- `C5`: Press down the tilt angle of 3240183_2 by 5 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease A3 Offset threshold for 3240183_2
- `C8`: Lift the tilt angle of 3240183_2 by 5 degrees
- `C9`: Increase transmission power for 3228869_3
- `C10`: Decrease transmission power for 3228869_3 **← 정답**
- `C11`: Adjust the azimuth of 3228869_3 by 14 degrees
- `C12`: Add neighbor relationship between 3240183_2 and 3228869_3
- `C13`: Decrease transmission power for 3240183_2
- `C14`: Decrease A3 Offset threshold for 3228869_3
- `C15`: Add neighbor relationship between 3271562_1 and 3228869_3
- `C16`: Adjust the azimuth of 3240183_2 by 1 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228869_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228869_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240183_2
- `C20`: Check test server and transmission issues
- `C21`: Increase A3 Offset threshold for 3240183_2
- `C22`: Lift the tilt angle  of 3228869_3 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.782 | MS1 | 121.4656687525 | 31.1446218973 | 828 | 504990 | -83.51 | 17.54 | 404.84 | 0.02 | 2.71 | 1577 |
| 2024-09-20 22:21:32.840 | MS1 | 121.4656610458 | 31.1446281256 | 828 | 504990 | -79.28 | 13.28 | 348.51 | 0.07 | 2.34 | 1578 |
| 2024-09-20 22:21:33.940 | MS1 | 121.4656637040 | 31.1446264986 | 828 | 504990 | -81.68 | 17.05 | 490.13 | 0.02 | 2.99 | 1577 |
| 2024-09-20 22:21:34.205 | MS1 | 121.4656745437 | 31.1446286310 | 828 | 504990 | -86.93 | 1.75 | 44.56 | 0.04 | 1.12 | 1572 |
| 2024-09-20 22:21:35.806 | MS1 | 121.4656619760 | 31.1446296415 | 828 | 504990 | -91.89 | 0.52 | 57.13 | 0.03 | 1.03 | 1582 |
| 2024-09-20 22:21:36.111 | MS1 | 121.4656606766 | 31.1446232607 | 828 | 504990 | -92.52 | 0.43 | 48.99 | 0.07 | 1.08 | 1562 |
| 2024-09-20 22:21:37.900 | MS1 | 121.4656683267 | 31.1446286475 | 828 | 504990 | -87.11 | 0.33 | 37.29 | 0.15 | 1.32 | 1562 |
| 2024-09-20 22:21:38.999 | MS1 | 121.4656670716 | 31.1446197544 | 828 | 504990 | -91.65 | 0.01 | 73.29 | 0.11 | 1.19 | 1593 |
| 2024-09-20 22:21:39.468 | MS1 | 121.4656608287 | 31.1446286201 | 828 | 504990 | -91.07 | 1.56 | 67.25 | 0.02 | 1.37 | 1575 |
| 2024-09-20 22:21:40.931 | MS1 | 121.4656683646 | 31.1446271853 | 828 | 504990 | -80.24 | 14.80 | 429.39 | 0.11 | 2.28 | 1565 |
| 2024-09-20 22:21:41.720 | MS1 | 121.4656621981 | 31.1446306974 | 828 | 504990 | -76.60 | 12.79 | 456.96 | 0.08 | 2.83 | 1589 |
| 2024-09-20 22:21:42.833 | MS1 | 121.4656612812 | 31.1446242141 | 828 | 504990 | -79.65 | 17.90 | 410.98 | 0.05 | 2.13 | 1585 |

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
| 3228869 | 3 | 121.4753849099 | 31.1440853580 | 288 | 1 | 4 | 29.0 | TDD | 127 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3240183 | 2 | 121.4758488119 | 31.1551890964 | 221 | 4 | 7 | 23.3 | TDD | 828 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3254393 | 4 | 121.4751981552 | 31.1489154067 | 77 | 11 | 12 | 36.5 | TDD | 960 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3271562 | 1 | 121.4743035409 | 31.1474237015 | 160 | 0 | 5 | 26.1 | TDD | 368 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.449 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.467 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.588 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.588 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271562 | 1 | 14.2110 | 15.2255 | -115.8705 | 13.7486 | 113.6747 | 0.0168 | 0.0051 |
| 2024_09_20 22:00 | 3240183 | 2 | 19.4005 | 15.1996 | -109.5512 | 19.7773 | 91.2366 | 0.0080 | 0.0026 |
| 2024_09_20 22:00 | 3228869 | 3 | 7.9987 | 14.1531 | -114.8650 | 5.4985 | 130.0505 | 0.0148 | 0.0146 |
| 2024_09_20 22:00 | 3254393 | 4 | 10.0819 | 13.8923 | -114.9072 | 14.2830 | 164.7724 | 0.0076 | 0.0088 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412850_2C92616E | 504990 | 828 | -85.7 | 504990 | 127 | -85.0 | 504990 | 368 | -87.1 | 504990 | 960 |
| MR_1774412850_2267238C | 504990 | 127 | -88.2 | 504990 | 828 | -88.0 | 504990 | 368 | -87.0 | 504990 | 960 |
| MR_1774412850_DDA6AEA9 | 504990 | 127 | -87.7 | 504990 | 828 | -88.7 | 504990 | 368 | -87.1 | 504990 | 960 |
| MR_1774412850_07DD21BC | 504990 | 127 | -88.1 | 504990 | 828 | -88.8 | 504990 | 368 | -90.3 | 504990 | 960 |
| MR_1774412850_2776969D | 504990 | 828 | -88.3 | 504990 | 127 | -85.9 | 504990 | 368 | -89.8 | 504990 | 960 |
| MR_1774412850_64DBA1DA | 504990 | 127 | -85.5 | 504990 | 828 | -88.3 | 504990 | 368 | -86.8 | 504990 | 960 |
| MR_1774412850_B871075C | 504990 | 828 | -86.8 | 504990 | 127 | -88.4 | 504990 | 368 | -89.4 | 504990 | 960 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1566: `e7bbe20d-aa7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e7bbe20d-aa75-48fa-baf1-8d9e160d6fd9` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Lift the tilt angle  of 3258689_3 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1566] topology](images/train_1566.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3263011_4
- `C2`: Decrease transmission power for 3263011_4
- `C3`: Increase transmission power for 3278848_1
- `C4`: Add neighbor relationship between 3258689_3 and 3263011_4
- `C5`: Increase A3 Offset threshold for 3278848_1
- `C6`: Press down the tilt angle  of 3258689_3 by 7 degrees
- `C7`: Decrease transmission power for 3278848_1
- `C8`: Adjust the azimuth of 3278848_1 by 46 degrees
- `C9`: Adjust the azimuth of 3258689_3 by 44 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263011_4
- `C11`: Add neighbor relationship between 3278848_1 and 3263011_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263011_4
- `C13`: Lift the tilt angle of 3278848_1 by 5 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278848_1
- `C15`: Press down the tilt angle of 3278848_1 by 5 degrees
- `C16`: Lift the tilt angle  of 3258689_3 by 7 degrees **← 정답**
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278848_1
- `C19`: Check test server and transmission issues
- `C20`: Increase A3 Offset threshold for 3263011_4
- `C21`: Decrease A3 Offset threshold for 3278848_1
- `C22`: Increase transmission power for 3263011_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.426 | MS1 | 121.4656672589 | 31.1446223989 | 940 | 504990 | -87.32 | 13.59 | 449.83 | 0.09 | 2.26 | 1578 |
| 2024-09-20 22:21:32.276 | MS1 | 121.4656643880 | 31.1446357801 | 940 | 504990 | -87.81 | 13.89 | 437.68 | 0.08 | 2.33 | 1595 |
| 2024-09-20 22:21:33.818 | MS1 | 121.4656732225 | 31.1446244933 | 940 | 504990 | -89.64 | 12.86 | 582.36 | 0.18 | 2.06 | 1597 |
| 2024-09-20 22:21:34.474 | MS1 | 121.4656744258 | 31.1446273300 | 940 | 504990 | -85.01 | 12.61 | 85.54 | 0.15 | 2.50 | 1580 |
| 2024-09-20 22:21:35.386 | MS1 | 121.4656722144 | 31.1446202763 | 940 | 504990 | -91.26 | 16.51 | 101.80 | 0.00 | 2.68 | 1597 |
| 2024-09-20 22:21:36.748 | MS1 | 121.4656585433 | 31.1446256823 | 940 | 504990 | -90.63 | 16.71 | 70.97 | 0.06 | 2.39 | 1572 |
| 2024-09-20 22:21:37.706 | MS1 | 121.4656688940 | 31.1446207741 | 940 | 504990 | -93.63 | 7.67 | 78.48 | 0.07 | 2.57 | 1589 |
| 2024-09-20 22:21:38.994 | MS1 | 121.4656761318 | 31.1446298420 | 940 | 504990 | -91.22 | 11.55 | 92.07 | 0.05 | 2.36 | 1568 |
| 2024-09-20 22:21:39.910 | MS1 | 121.4656772342 | 31.1446311851 | 940 | 504990 | -93.30 | 12.55 | 56.01 | 0.06 | 2.83 | 1563 |
| 2024-09-20 22:21:40.872 | MS1 | 121.4656664817 | 31.1446213000 | 940 | 504990 | -89.29 | 12.85 | 479.38 | 0.07 | 2.02 | 1563 |
| 2024-09-20 22:21:41.449 | MS1 | 121.4656698767 | 31.1446297185 | 940 | 504990 | -89.37 | 8.13 | 401.05 | 0.11 | 2.77 | 1573 |
| 2024-09-20 22:21:42.581 | MS1 | 121.4656592994 | 31.1446245015 | 940 | 504990 | -89.54 | 7.84 | 540.06 | 0.02 | 2.02 | 1582 |

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
| 3258689 | 3 | 121.4754417296 | 31.1516690452 | 284 | 4 | 5 | 49.2 | TDD | 622 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3263011 | 4 | 121.4643898634 | 31.1541413060 | 129 | 4 | 4 | 49.8 | TDD | 820 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3266182 | 2 | 121.4658848423 | 31.1468657099 | 220 | 8 | 11 | 30.4 | TDD | 965 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3278848 | 1 | 121.4661349606 | 31.1498968663 | 138 | 3 | 4 | 22.0 | TDD | 940 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.186 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.209 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.356 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.356 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.009 | NREventA3 | measId:2;ServCellPCI:293;Se... |
| 2024-09-20 22:21:38.249 | NRHandoverAttempt | SourcePCI:293;SourceNR-ARFC... |
| 2024-09-20 22:21:38.280 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.295 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.431 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.431 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278848 | 1 | 92.3539 | 91.4013 | -114.5174 | 10.3992 | 169.6453 | 0.0023 | 0.0173 |
| 2024_09_20 22:00 | 3266182 | 2 | 8.9221 | 16.1624 | -114.1966 | 12.9592 | 161.9435 | 0.0137 | 0.0197 |
| 2024_09_20 22:00 | 3258689 | 3 | 6.4880 | 6.7917 | -114.7214 | 16.7741 | 146.4860 | 0.0148 | 0.0041 |
| 2024_09_20 22:00 | 3263011 | 4 | 8.0981 | 18.6164 | -116.4883 | 19.5669 | 160.8216 | 0.0123 | 0.0178 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414146_AC74C216 | 504990 | 940 | -85.2 | 504990 | 820 | -92.7 | 504990 | 622 | -95.7 | 504990 | 965 |
| MR_1774414146_D200D9AA | 504990 | 940 | -86.7 | 504990 | 820 | -93.1 | 504990 | 622 | -92.4 | 504990 | 965 |
| MR_1774414146_7DBC4963 | 504990 | 940 | -84.4 | 504990 | 820 | -92.3 | 504990 | 622 | -93.8 | 504990 | 965 |
| MR_1774414146_E91E22BD | 504990 | 940 | -86.8 | 504990 | 820 | -95.3 | 504990 | 622 | -94.8 | 504990 | 965 |
| MR_1774414146_A86950EF | 504990 | 940 | -86.2 | 504990 | 820 | -92.1 | 504990 | 622 | -93.6 | 504990 | 965 |
| MR_1774414146_FF82736F | 504990 | 940 | -83.3 | 504990 | 820 | -95.3 | 504990 | 622 | -93.0 | 504990 | 965 |
| MR_1774414146_B79C6416 | 504990 | 940 | -84.8 | 504990 | 820 | -94.8 | 504990 | 622 | -94.8 | 504990 | 965 |
| MR_1774414146_3148B6D2 | 504990 | 940 | -83.7 | 504990 | 820 | -92.7 | 504990 | 622 | -95.5 | 504990 | 965 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1567: `eb0c5c4f-b0a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `eb0c5c4f-b0a0-41e0-b7e2-c7b14b69843f` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1567] topology](images/train_1567.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3267848_3 by 10 degrees
- `C2`: Decrease transmission power for 3225400_4
- `C3`: Increase A3 Offset threshold for 3267848_3
- `C4`: Adjust the azimuth of 3267848_3 by 5 degrees
- `C5`: Lift the tilt angle  of 3225400_4 by 10 degrees
- `C6`: Adjust the azimuth of 3225400_4 by 50 degrees
- `C7`: Increase transmission power for 3225400_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225400_4
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease A3 Offset threshold for 3225400_4
- `C11`: Increase transmission power for 3267848_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267848_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225400_4
- `C14`: Add neighbor relationship between 3226389_2 and 3225400_4
- `C15`: Check test server and transmission issues **← 정답**
- `C16`: Decrease A3 Offset threshold for 3267848_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267848_3
- `C18`: Press down the tilt angle of 3267848_3 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3225400_4
- `C20`: Press down the tilt angle  of 3225400_4 by 10 degrees
- `C21`: Add neighbor relationship between 3267848_3 and 3225400_4
- `C22`: Decrease transmission power for 3267848_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.768 | MS1 | 121.4656767413 | 31.1446314110 | 129 | 504990 | -87.82 | 12.88 | 361.44 | 0.08 | 2.96 | 1595 |
| 2024-09-20 22:21:32.911 | MS1 | 121.4656625236 | 31.1446277887 | 129 | 504990 | -87.30 | 14.30 | 452.65 | 0.03 | 2.31 | 1576 |
| 2024-09-20 22:21:33.657 | MS1 | 121.4656666503 | 31.1446303485 | 129 | 504990 | -90.17 | 15.51 | 311.88 | 0.19 | 2.29 | 1597 |
| 2024-09-20 22:21:34.320 | MS1 | 121.4656670270 | 31.1446180001 | 129 | 504990 | -88.83 | 14.56 | 74.17 | 0.02 | 2.37 | 466 |
| 2024-09-20 22:21:35.940 | MS1 | 121.4656678665 | 31.1446202800 | 129 | 504990 | -88.03 | 13.47 | 90.97 | 0.17 | 2.56 | 386 |
| 2024-09-20 22:21:36.252 | MS1 | 121.4656753872 | 31.1446236194 | 129 | 504990 | -87.01 | 15.75 | 81.99 | 0.01 | 2.98 | 484 |
| 2024-09-20 22:21:37.421 | MS1 | 121.4656759190 | 31.1446231652 | 129 | 504990 | -91.08 | 8.17 | 74.16 | 0.09 | 2.80 | 458 |
| 2024-09-20 22:21:38.765 | MS1 | 121.4656722305 | 31.1446269218 | 129 | 504990 | -89.44 | 9.84 | 55.95 | 0.18 | 2.57 | 397 |
| 2024-09-20 22:21:39.921 | MS1 | 121.4656587895 | 31.1446273669 | 129 | 504990 | -90.25 | 12.09 | 53.19 | 0.09 | 2.16 | 467 |
| 2024-09-20 22:21:40.824 | MS1 | 121.4656757044 | 31.1446321173 | 129 | 504990 | -93.65 | 7.36 | 561.67 | 0.09 | 2.73 | 1579 |
| 2024-09-20 22:21:41.742 | MS1 | 121.4656737070 | 31.1446268400 | 129 | 504990 | -91.16 | 9.17 | 303.50 | 0.05 | 2.55 | 1560 |
| 2024-09-20 22:21:42.302 | MS1 | 121.4656608610 | 31.1446353778 | 129 | 504990 | -92.84 | 12.04 | 419.29 | 0.16 | 2.39 | 1571 |

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
| 3225400 | 4 | 121.4713235089 | 31.1525722020 | 339 | 11 | 5 | 38.5 | TDD | 579 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3226389 | 2 | 121.4671285466 | 31.1557409622 | 54 | 11 | 12 | 29.2 | TDD | 953 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3228330 | 1 | 121.4741063718 | 31.1512649207 | 219 | 7 | 3 | 23.5 | TDD | 592 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3267848 | 3 | 121.4658235979 | 31.1477668351 | 178 | 13 | 11 | 36.5 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.312 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.328 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.442 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.442 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.162 | NREventA3 | measId:2;ServCellPCI:316;Se... |
| 2024-09-20 22:21:38.402 | NRHandoverAttempt | SourcePCI:316;SourceNR-ARFC... |
| 2024-09-20 22:21:38.450 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.460 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.594 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.594 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228330 | 1 | 9.2295 | 18.6304 | -116.9208 | 8.2000 | 156.6835 | 0.0196 | 0.0176 |
| 2024_09_20 22:00 | 3226389 | 2 | 12.0362 | 11.4687 | -116.6128 | 15.9558 | 110.5125 | 0.0072 | 0.0190 |
| 2024_09_20 22:00 | 3267848 | 3 | 15.7844 | 17.7878 | -115.0948 | 7.4814 | 152.7938 | 0.0193 | 0.0137 |
| 2024_09_20 22:00 | 3225400 | 4 | 19.4382 | 8.2598 | -114.0812 | 17.2027 | 174.8555 | 0.0186 | 0.0152 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417124_70E70229 | 504990 | 129 | -88.7 | 504990 | 579 | -88.2 | 504990 | 953 | -103.1 | 504990 | 592 |
| MR_1774417124_FDF2A490 | 504990 | 129 | -89.0 | 504990 | 579 | -87.9 | 504990 | 953 | -102.4 | 504990 | 592 |
| MR_1774417124_DD160317 | 504990 | 129 | -88.6 | 504990 | 579 | -89.0 | 504990 | 953 | -102.5 | 504990 | 592 |
| MR_1774417124_54B2FE65 | 504990 | 129 | -88.0 | 504990 | 579 | -88.3 | 504990 | 953 | -105.0 | 504990 | 592 |
| MR_1774417124_EE66C116 | 504990 | 129 | -87.2 | 504990 | 579 | -91.3 | 504990 | 953 | -104.5 | 504990 | 592 |
| MR_1774417124_2F6D1608 | 504990 | 129 | -88.9 | 504990 | 579 | -90.4 | 504990 | 953 | -105.0 | 504990 | 592 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1568: `bc400845-55d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bc400845-55d0-4eaf-84e6-13027bfe672a` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249842_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1568] topology](images/train_1568.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3249842_6 and 3222115_5
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222115_5
- `C3`: Increase transmission power for 3222115_5
- `C4`: Check test server and transmission issues
- `C5`: Decrease transmission power for 3222115_5
- `C6`: Add neighbor relationship between 3229202_13 and 3222115_5
- `C7`: Decrease A3 Offset threshold for 3249842_6
- `C8`: Adjust the azimuth of 3222115_5 by 25 degrees
- `C9`: Increase A3 Offset threshold for 3222115_5
- `C10`: Increase A3 Offset threshold for 3249842_6
- `C11`: Decrease transmission power for 3249842_6
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222115_5
- `C13`: Press down the tilt angle of 3249842_6 by 5 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249842_6
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Lift the tilt angle  of 3222115_5 by 4 degrees
- `C17`: Lift the tilt angle of 3249842_6 by 5 degrees
- `C18`: Decrease A3 Offset threshold for 3222115_5
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249842_6 **← 정답**
- `C20`: Increase transmission power for 3249842_6
- `C21`: Adjust the azimuth of 3249842_6 by 19 degrees
- `C22`: Press down the tilt angle  of 3222115_5 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.194 | MS1 | 121.4656655997 | 31.1446267960 | 114 | 504990 | -94.09 | 12.48 | 575.99 | 0.18 | 2.91 | 1587 |
| 2024-09-20 22:21:32.309 | MS1 | 121.4656680938 | 31.1446330122 | 642 | 504990 | -95.03 | 9.24 | 484.89 | 0.15 | 2.28 | 1575 |
| 2024-09-20 22:21:33.748 | MS1 | 121.4656590620 | 31.1446185638 | 455 | 504990 | -95.11 | 11.05 | 500.66 | 0.18 | 2.14 | 1593 |
| 2024-09-20 22:21:34.714 | MS1 | 121.4656691073 | 31.1446185347 | 171 | 152650 | -91.84 | 6.45 | 71.85 | 0.00 | 1.66 | 987 |
| 2024-09-20 22:21:35.466 | MS1 | 121.4656676563 | 31.1446245380 | 160 | 152650 | -95.81 | 7.73 | 80.89 | 0.05 | 1.81 | 940 |
| 2024-09-20 22:21:36.168 | MS1 | 121.4656594469 | 31.1446319344 | 318 | 152650 | -90.49 | 2.68 | 98.83 | 0.17 | 1.86 | 952 |
| 2024-09-20 22:21:37.379 | MS1 | 121.4656588365 | 31.1446261597 | 342 | 152650 | -90.68 | 5.97 | 86.32 | 0.20 | 1.58 | 978 |
| 2024-09-20 22:21:38.596 | MS1 | 121.4656779355 | 31.1446325508 | 171 | 152650 | -93.61 | 5.74 | 80.92 | 0.11 | 1.57 | 991 |
| 2024-09-20 22:21:39.766 | MS1 | 121.4656768939 | 31.1446226102 | 160 | 152650 | -91.18 | 5.53 | 71.02 | 0.20 | 1.67 | 992 |
| 2024-09-20 22:21:40.542 | MS1 | 121.4656714578 | 31.1446322516 | 318 | 152650 | -95.94 | 7.87 | 92.51 | 0.19 | 2.04 | 1563 |
| 2024-09-20 22:21:41.257 | MS1 | 121.4656713849 | 31.1446302808 | 342 | 152650 | -94.47 | 2.89 | 87.83 | 0.08 | 2.14 | 1578 |
| 2024-09-20 22:21:42.873 | MS1 | 121.4656682412 | 31.1446349596 | 171 | 152650 | -92.00 | 3.02 | 61.52 | 0.16 | 2.62 | 1576 |

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
| 3220195 | 3 | 121.4752238811 | 31.1444613347 | 306 | 10 | 7 | 6.8 | TDD | 455 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3222115 | 5 | 121.4744755407 | 31.1441282891 | 299 | 4 | 3 | 5.9 | TDD | 112 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3228671 | 11 | 121.4656035039 | 31.1546278130 | 284 | 8 | 1 | 8.2 | FDD | 51 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3229202 | 13 | 121.4657046343 | 31.1515384133 | 343 | 0 | 1 | 27.0 | FDD | 318 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3238048 | 12 | 121.4730073577 | 31.1550234177 | 180 | 6 | 3 | 0.2 | FDD | 342 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3240066 | 4 | 121.4697217729 | 31.1543135854 | 249 | 14 | 11 | 21.5 | TDD | 106 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3248686 | 10 | 121.4729988088 | 31.1504783463 | 114 | 9 | 11 | 12.7 | FDD | 12 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3249842 | 6 | 121.4716065891 | 31.1505302979 | 202 | 5 | 0 | 3.9 | TDD | 114 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3250539 | 9 | 121.4747020406 | 31.1451376017 | 348 | 15 | 0 | 16.0 | FDD | 171 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3251361 | 8 | 121.4735988250 | 31.1524220904 | 176 | 12 | 4 | 19.0 | FDD | 608 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3267199 | 7 | 121.4663426996 | 31.1513180042 | 96 | 0 | 3 | 10.6 | FDD | 160 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3267659 | 1 | 121.4655889003 | 31.1471457801 | 121 | 11 | 11 | 4.0 | TDD | 642 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3278950 | 2 | 121.4679428447 | 31.1535149480 | 231 | 7 | 4 | 3.8 | TDD | 229 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.091 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.110 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.257 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.257 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.980 | NREventA2 | measId:1;ServCellPCI:659;Se... |
| 2024-09-20 22:21:35.110 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.397 | NREventA5 | measId:3;ServCellPCI:659;Se... |
| 2024-09-20 22:21:35.473 | NRHandoverAttempt | SourcePCI:659;SourceNR-ARFC... |
| 2024-09-20 22:21:35.494 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.506 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.636 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.636 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267659 | 1 | 10.5371 | 8.1721 | -115.5420 | 7.5505 | 174.7918 | 0.0178 | 0.0060 |
| 2024_09_20 22:00 | 3278950 | 2 | 11.7080 | 9.9589 | -114.2244 | 14.4122 | 97.9568 | 0.0121 | 0.0113 |
| 2024_09_20 22:00 | 3220195 | 3 | 14.6185 | 7.6603 | -116.2190 | 13.7805 | 185.5700 | 0.0128 | 0.0131 |
| 2024_09_20 22:00 | 3240066 | 4 | 18.5104 | 7.4940 | -116.1711 | 14.8906 | 93.7958 | 0.0005 | 0.0192 |
| 2024_09_20 22:00 | 3222115 | 5 | 15.9607 | 17.6047 | -114.5762 | 14.0155 | 186.7527 | 0.0163 | 0.0075 |
| 2024_09_20 22:00 | 3249842 | 6 | 12.1057 | 10.0504 | -117.8060 | 6.0288 | 90.7280 | 0.0132 | 0.0068 |
| 2024_09_20 22:00 | 3267199 | 7 | 16.7783 | 16.4633 | -114.3883 | 3.3642 | 21.2880 | 0.0078 | 0.0124 |
| 2024_09_20 22:00 | 3251361 | 8 | 8.1272 | 7.3810 | -116.6421 | 3.0932 | 34.8773 | 0.0199 | 0.0092 |
| 2024_09_20 22:00 | 3250539 | 9 | 17.3856 | 19.9612 | -116.6785 | 3.4685 | 24.4111 | 0.0062 | 0.0171 |
| 2024_09_20 22:00 | 3248686 | 10 | 17.5261 | 17.5415 | -114.7904 | 4.8797 | 30.6433 | 0.0103 | 0.0115 |
| 2024_09_20 22:00 | 3228671 | 11 | 9.1675 | 15.3462 | -116.8696 | 4.4381 | 38.1293 | 0.0139 | 0.0017 |
| 2024_09_20 22:00 | 3238048 | 12 | 11.9606 | 9.5249 | -115.5881 | 4.4014 | 41.0142 | 0.0174 | 0.0095 |
| 2024_09_20 22:00 | 3229202 | 13 | 5.6468 | 5.5267 | -115.2433 | 4.3311 | 28.7946 | 0.0071 | 0.0014 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416715_08C7BB55 | 504990 | 455 | -95.3 | 504990 | 112 | -95.5 | 504990 | 106 | -94.4 | 504990 | 229 |
| MR_1774416715_A04F2D43 | 504990 | 455 | -95.0 | 504990 | 112 | -94.0 | 504990 | 106 | -94.8 | 504990 | 229 |
| MR_1774416715_F6B15362 | 504990 | 455 | -95.5 | 504990 | 112 | -93.2 | 504990 | 106 | -93.8 | 504990 | 229 |
| MR_1774416715_2C2BEC48 | 504990 | 455 | -95.6 | 504990 | 112 | -94.4 | 504990 | 106 | -95.5 | 504990 | 229 |
| MR_1774416715_1F5D1A9D | 504990 | 455 | -93.3 | 504990 | 112 | -93.3 | 504990 | 106 | -94.2 | 504990 | 229 |
| MR_1774416715_AB5EE7D8 | 504990 | 455 | -96.3 | 504990 | 112 | -95.1 | 504990 | 106 | -95.8 | 504990 | 229 |
| MR_1774416715_A1496529 | 152650 | 171 | -93.3 | 152650 | 12 | -94.9 | 152650 | 608 | -99.4 | 152650 | 51 |
| MR_1774416715_8DC3E031 | 504990 | 455 | -96.4 | 504990 | 112 | -93.5 | 504990 | 106 | -95.6 | 504990 | 229 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1569: `0af440cf-72f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0af440cf-72f7-47e0-b1c7-29f6a1f7bd45` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1569] topology](images/train_1569.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3260008_3
- `C2`: Add neighbor relationship between 3268785_2 and 3260008_3
- `C3`: Decrease A3 Offset threshold for 3268785_2
- `C4`: Decrease transmission power for 3268785_2
- `C5`: Increase transmission power for 3268785_2
- `C6`: Add neighbor relationship between 3266032_4 and 3260008_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268785_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260008_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260008_3
- `C10`: Adjust the azimuth of 3260008_3 by 29 degrees
- `C11`: Decrease A3 Offset threshold for 3260008_3
- `C12`: Check test server and transmission issues
- `C13`: Increase transmission power for 3260008_3
- `C14`: Lift the tilt angle of 3268785_2 by 9 degrees
- `C15`: Press down the tilt angle  of 3260008_3 by 10 degrees
- `C16`: Increase A3 Offset threshold for 3260008_3
- `C17`: Increase A3 Offset threshold for 3268785_2
- `C18`: Lift the tilt angle  of 3260008_3 by 10 degrees
- `C19`: Insufficient data; more data is needed for judgment. **← 정답**
- `C20`: Press down the tilt angle of 3268785_2 by 9 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268785_2
- `C22`: Adjust the azimuth of 3268785_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.764 | MS1 | 121.4656708697 | 31.1446279216 | 506 | 504990 | -86.96 | 12.03 | 334.25 | 0.08 | 2.39 | 1591 |
| 2024-09-20 22:21:32.893 | MS1 | 121.4656722948 | 31.1446245412 | 506 | 504990 | -87.61 | 16.04 | 554.89 | 0.00 | 2.45 | 1599 |
| 2024-09-20 22:21:33.173 | MS1 | 121.4656738788 | 31.1446273220 | 506 | 504990 | -86.92 | 14.04 | 409.62 | 0.16 | 2.04 | 1566 |
| 2024-09-20 22:21:34.438 | MS1 | 121.4656665411 | 31.1446347300 | 506 | 504990 | -89.97 | 13.13 | 73.06 | 0.20 | 2.67 | 1592 |
| 2024-09-20 22:21:35.782 | MS1 | 121.4656711938 | 31.1446361611 | 506 | 504990 | -87.17 | 13.79 | 92.87 | 0.09 | 2.39 | 1591 |
| 2024-09-20 22:21:36.515 | MS1 | 121.4656755647 | 31.1446285966 | 506 | 504990 | -88.87 | 13.11 | 58.82 | 0.01 | 2.05 | 1579 |
| 2024-09-20 22:21:37.236 | MS1 | 121.4656650076 | 31.1446322511 | 506 | 504990 | -90.95 | 9.18 | 92.25 | 0.12 | 2.07 | 1574 |
| 2024-09-20 22:21:38.624 | MS1 | 121.4656762482 | 31.1446262263 | 506 | 504990 | -89.20 | 12.43 | 99.95 | 0.05 | 2.39 | 1593 |
| 2024-09-20 22:21:39.797 | MS1 | 121.4656759656 | 31.1446226957 | 506 | 504990 | -93.79 | 7.44 | 60.02 | 0.03 | 2.95 | 1562 |
| 2024-09-20 22:21:40.200 | MS1 | 121.4656746834 | 31.1446305353 | 506 | 504990 | -90.29 | 12.89 | 342.54 | 0.13 | 2.93 | 1563 |
| 2024-09-20 22:21:41.204 | MS1 | 121.4656615573 | 31.1446209910 | 506 | 504990 | -90.40 | 12.41 | 511.27 | 0.11 | 2.14 | 1595 |
| 2024-09-20 22:21:42.472 | MS1 | 121.4656669270 | 31.1446341582 | 506 | 504990 | -93.59 | 10.57 | 383.00 | 0.18 | 2.95 | 1564 |

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
| 3260008 | 3 | 121.4659365500 | 31.1488541719 | 212 | 11 | 3 | 45.3 | TDD | 805 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3266032 | 4 | 121.4679502976 | 31.1487487197 | 132 | 0 | 2 | 26.4 | TDD | 349 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3268785 | 2 | 121.4685535280 | 31.1441735450 | 352 | 3 | 0 | 28.4 | TDD | 506 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3271272 | 1 | 121.4727963335 | 31.1526282389 | 307 | 13 | 5 | 35.4 | TDD | 737 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.170 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.193 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.324 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.324 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.045 | NREventA3 | measId:2;ServCellPCI:382;Se... |
| 2024-09-20 22:21:38.285 | NRHandoverAttempt | SourcePCI:382;SourceNR-ARFC... |
| 2024-09-20 22:21:38.327 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.337 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.467 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.467 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3271272 | 1 | 88.7583 | 92.5491 | -116.2418 | 19.4262 | 162.9972 | 0.0025 | 0.0118 |
| 2024_09_19 22:00 | 3268785 | 2 | 90.9667 | 90.3997 | -116.6804 | 16.6296 | 166.8140 | 0.0146 | 0.0174 |
| 2024_09_19 22:00 | 3260008 | 3 | 86.1863 | 89.8889 | -117.2326 | 17.9079 | 157.1105 | 0.0183 | 0.0069 |
| 2024_09_19 22:00 | 3266032 | 4 | 85.8950 | 89.3742 | -116.6538 | 9.7073 | 129.4422 | 0.0094 | 0.0063 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417125_1B00C850 | 504990 | 506 | -89.4 | 504990 | 805 | -98.5 | 504990 | 349 | -104.1 | 504990 | 737 |
| MR_1774417125_79BF9FA7 | 504990 | 506 | -90.3 | 504990 | 805 | -100.8 | 504990 | 349 | -101.8 | 504990 | 737 |
| MR_1774417125_36DB9135 | 504990 | 506 | -88.3 | 504990 | 805 | -98.4 | 504990 | 349 | -102.1 | 504990 | 737 |
| MR_1774417125_AF1D0FDB | 504990 | 506 | -91.8 | 504990 | 805 | -100.4 | 504990 | 349 | -103.9 | 504990 | 737 |
| MR_1774417125_9A589EE6 | 504990 | 506 | -90.1 | 504990 | 805 | -100.2 | 504990 | 349 | -101.8 | 504990 | 737 |

> *... 2개 열 생략 (전체 14열)*

---
