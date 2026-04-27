# Track A 문제 분석 — train[1840]~train[1849]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1840] ~ train[1849] (10개)

## 목차

1. [문제 1840: `d97c9bd8-5a9...`](#1840) — single-answer, 정답: C17
2. [문제 1841: `550a6bd0-871...`](#1841) — multiple-answer, 정답: C2|C6
3. [문제 1842: `44e4051f-9bc...`](#1842) — single-answer, 정답: C15
4. [문제 1843: `dd612ece-57d...`](#1843) — multiple-answer, 정답: C3|C7|C10|C11
5. [문제 1844: `e593f712-465...`](#1844) — single-answer, 정답: C22
6. [문제 1845: `d0ee46a6-dee...`](#1845) — multiple-answer, 정답: C3|C6|C15|C17
7. [문제 1846: `fa529e46-85f...`](#1846) — single-answer, 정답: C15
8. [문제 1847: `d9b0ca11-c68...`](#1847) — single-answer, 정답: C21
9. [문제 1848: `a84366be-3c0...`](#1848) — single-answer, 정답: C1
10. [문제 1849: `0b9dc5f8-67e...`](#1849) — single-answer, 정답: C10

---

### 문제 1840: `d97c9bd8-5a9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d97c9bd8-5a90-40af-b424-494b8a92d64f` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Decrease A3 Offset threshold for 3215440_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1840] topology](images/train_1840.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3278249_2 by 32 degrees
- `C2`: Adjust the azimuth of 3215440_3 by 50 degrees
- `C3`: Increase A3 Offset threshold for 3278249_2
- `C4`: Increase transmission power for 3215440_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215440_3
- `C6`: Increase transmission power for 3278249_2
- `C7`: Increase A3 Offset threshold for 3215440_3
- `C8`: Check test server and transmission issues
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278249_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Lift the tilt angle  of 3278249_2 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278249_2
- `C13`: Decrease A3 Offset threshold for 3278249_2
- `C14`: Add neighbor relationship between 3215440_3 and 3278249_2
- `C15`: Add neighbor relationship between 3254472_1 and 3278249_2
- `C16`: Lift the tilt angle of 3215440_3 by 10 degrees
- `C17`: Decrease A3 Offset threshold for 3215440_3 **← 정답**
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215440_3
- `C19`: Press down the tilt angle  of 3278249_2 by 10 degrees
- `C20`: Decrease transmission power for 3278249_2
- `C21`: Decrease transmission power for 3215440_3
- `C22`: Press down the tilt angle of 3215440_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.209 | MS1 | 121.4656661795 | 31.1446248273 | 941 | 504990 | -84.25 | 14.64 | 570.88 | 0.13 | 2.85 | 1571 |
| 2024-09-20 22:21:32.654 | MS1 | 121.4656664134 | 31.1446200119 | 941 | 504990 | -77.52 | 12.06 | 468.11 | 0.19 | 2.19 | 1599 |
| 2024-09-20 22:21:33.368 | MS1 | 121.4656760160 | 31.1446367700 | 941 | 504990 | -82.40 | 16.51 | 598.14 | 0.08 | 2.18 | 1596 |
| 2024-09-20 22:21:34.905 | MS1 | 121.4656667281 | 31.1446273340 | 941 | 504990 | -87.82 | -2.50 | 46.08 | 0.15 | 1.45 | 1587 |
| 2024-09-20 22:21:35.791 | MS1 | 121.4656616618 | 31.1446237204 | 941 | 504990 | -85.82 | -1.45 | 49.17 | 0.01 | 1.21 | 1563 |
| 2024-09-20 22:21:36.633 | MS1 | 121.4656745367 | 31.1446235264 | 941 | 504990 | -83.15 | -1.84 | 75.77 | 0.02 | 1.01 | 1584 |
| 2024-09-20 22:21:37.659 | MS1 | 121.4656772460 | 31.1446330758 | 941 | 504990 | -92.25 | -1.78 | 54.76 | 0.07 | 1.44 | 1591 |
| 2024-09-20 22:21:38.683 | MS1 | 121.4656631167 | 31.1446292834 | 941 | 504990 | -91.25 | -1.48 | 51.85 | 0.14 | 1.34 | 1590 |
| 2024-09-20 22:21:39.598 | MS1 | 121.4656736528 | 31.1446240160 | 452 | 504990 | -75.45 | 14.42 | 181.50 | 0.11 | 1.44 | 1568 |
| 2024-09-20 22:21:40.491 | MS1 | 121.4656685404 | 31.1446279319 | 452 | 504990 | -81.97 | 17.02 | 379.13 | 0.12 | 2.31 | 1568 |
| 2024-09-20 22:21:41.781 | MS1 | 121.4656644811 | 31.1446182768 | 452 | 504990 | -82.72 | 17.83 | 326.49 | 0.18 | 2.01 | 1580 |
| 2024-09-20 22:21:42.239 | MS1 | 121.4656767681 | 31.1446224819 | 452 | 504990 | -79.09 | 15.52 | 554.37 | 0.07 | 3.00 | 1571 |

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
| 3215440 | 3 | 121.4656206561 | 31.1455556775 | 312 | 1 | 8 | 26.6 | TDD | 941 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3233126 | 4 | 121.4720874266 | 31.1522164019 | 347 | 6 | 3 | 33.1 | TDD | 295 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3254472 | 1 | 121.4713251078 | 31.1544031048 | 136 | 8 | 7 | 45.2 | TDD | 467 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3278249 | 2 | 121.4649642415 | 31.1444206038 | 39 | 5 | 12 | 25.2 | TDD | 452 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.500 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.524 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.654 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.654 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.369 | NREventA3 | measId:2;ServCellPCI:47;Ser... |
| 2024-09-20 22:21:38.609 | NRHandoverAttempt | SourcePCI:47;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.659 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.671 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.789 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.789 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254472 | 1 | 5.2281 | 9.8421 | -114.2918 | 11.5382 | 138.7134 | 0.0120 | 0.0195 |
| 2024_09_20 22:00 | 3278249 | 2 | 12.4791 | 13.3984 | -117.4838 | 14.1187 | 189.9102 | 0.0134 | 0.0156 |
| 2024_09_20 22:00 | 3215440 | 3 | 12.4850 | 6.0208 | -115.6099 | 19.8487 | 163.8389 | 0.0143 | 0.1283 |
| 2024_09_20 22:00 | 3233126 | 4 | 16.8349 | 5.5393 | -115.1026 | 19.0101 | 101.6318 | 0.0058 | 0.0107 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412796_A9787343 | 504990 | 941 | -87.8 | 504990 | 452 | -82.4 | 504990 | 467 | -89.0 | 504990 | 295 |
| MR_1774412796_9FB42D1E | 504990 | 452 | -81.8 | 504990 | 941 | -87.2 | 504990 | 467 | -89.1 | 504990 | 295 |
| MR_1774412796_534C3CD7 | 504990 | 941 | -87.2 | 504990 | 452 | -82.6 | 504990 | 467 | -89.0 | 504990 | 295 |
| MR_1774412796_B3F99335 | 504990 | 452 | -83.6 | 504990 | 941 | -87.3 | 504990 | 467 | -90.3 | 504990 | 295 |
| MR_1774412796_480BE104 | 504990 | 452 | -82.6 | 504990 | 941 | -86.9 | 504990 | 467 | -88.7 | 504990 | 295 |
| MR_1774412796_F4063DA2 | 504990 | 941 | -87.0 | 504990 | 452 | -82.1 | 504990 | 467 | -90.8 | 504990 | 295 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1841: `550a6bd0-871...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `550a6bd0-8711-4b04-b093-ef4ad8d1f254` |
| Tag | **multiple-answer** |
| 정답 | **C2|C6** |
| C2 의미 | Press down the tilt angle  of 3218325_4 by 4 degrees |
| C6 의미 | Decrease transmission power for 3218325_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1841] topology](images/train_1841.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Press down the tilt angle  of 3218325_4 by 4 degrees **← 정답**
- `C3`: Adjust the azimuth of 3218325_4 by 17 degrees
- `C4`: Lift the tilt angle  of 3218325_4 by 4 degrees
- `C5`: Decrease A3 Offset threshold for 3218325_4
- `C6`: Decrease transmission power for 3218325_4 **← 정답**
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270515_2
- `C8`: Press down the tilt angle of 3270515_2 by 3 degrees
- `C9`: Increase A3 Offset threshold for 3270515_2
- `C10`: Increase A3 Offset threshold for 3218325_4
- `C11`: Decrease A3 Offset threshold for 3270515_2
- `C12`: Lift the tilt angle of 3270515_2 by 3 degrees
- `C13`: Increase transmission power for 3270515_2
- `C14`: Add neighbor relationship between 3215589_3 and 3218325_4
- `C15`: Add neighbor relationship between 3270515_2 and 3218325_4
- `C16`: Check test server and transmission issues
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270515_2
- `C18`: Decrease transmission power for 3270515_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218325_4
- `C20`: Adjust the azimuth of 3270515_2 by 6 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218325_4
- `C22`: Increase transmission power for 3218325_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.336 | MS1 | 121.4656673090 | 31.1446208857 | 683 | 504990 | -77.25 | 17.43 | 592.52 | 0.12 | 2.49 | 1593 |
| 2024-09-20 22:21:32.377 | MS1 | 121.4656718208 | 31.1446373776 | 683 | 504990 | -78.89 | 17.96 | 384.75 | 0.17 | 2.94 | 1585 |
| 2024-09-20 22:21:33.241 | MS1 | 121.4656638272 | 31.1446239600 | 683 | 504990 | -80.67 | 16.97 | 488.40 | 0.08 | 2.97 | 1570 |
| 2024-09-20 22:21:34.372 | MS1 | 121.4656621883 | 31.1446263673 | 683 | 504990 | -87.47 | 3.64 | 96.08 | 0.03 | 1.11 | 1593 |
| 2024-09-20 22:21:35.650 | MS1 | 121.4656750544 | 31.1446255018 | 683 | 504990 | -86.83 | 0.02 | 69.98 | 0.03 | 1.12 | 1588 |
| 2024-09-20 22:21:36.555 | MS1 | 121.4656604303 | 31.1446338615 | 683 | 504990 | -92.15 | 3.45 | 83.93 | 0.02 | 1.13 | 1566 |
| 2024-09-20 22:21:37.868 | MS1 | 121.4656598865 | 31.1446336199 | 683 | 504990 | -86.82 | 0.68 | 54.51 | 0.16 | 1.43 | 1574 |
| 2024-09-20 22:21:38.190 | MS1 | 121.4656756091 | 31.1446196829 | 683 | 504990 | -92.82 | 3.57 | 56.07 | 0.13 | 1.35 | 1562 |
| 2024-09-20 22:21:39.409 | MS1 | 121.4656765060 | 31.1446218543 | 683 | 504990 | -85.03 | 1.63 | 57.28 | 0.09 | 1.14 | 1578 |
| 2024-09-20 22:21:40.874 | MS1 | 121.4656707782 | 31.1446301575 | 683 | 504990 | -82.71 | 13.27 | 517.59 | 0.08 | 2.54 | 1590 |
| 2024-09-20 22:21:41.620 | MS1 | 121.4656581282 | 31.1446212307 | 683 | 504990 | -80.05 | 14.52 | 317.45 | 0.03 | 2.58 | 1567 |
| 2024-09-20 22:21:42.456 | MS1 | 121.4656654086 | 31.1446196708 | 683 | 504990 | -75.70 | 14.09 | 577.83 | 0.18 | 2.52 | 1573 |

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
| 3215589 | 3 | 121.4739828632 | 31.1510125542 | 41 | 15 | 8 | 43.7 | TDD | 300 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3218325 | 4 | 121.4736473031 | 31.1539969471 | 233 | 3 | 12 | 33.5 | TDD | 271 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3236502 | 1 | 121.4655711960 | 31.1537807077 | 97 | 8 | 3 | 43.8 | TDD | 18 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3270515 | 2 | 121.4750055357 | 31.1507553705 | 239 | 1 | 8 | 39.4 | TDD | 683 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.964 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.985 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.125 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.125 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236502 | 1 | 7.9286 | 19.0525 | -114.6115 | 17.8085 | 113.7719 | 0.0007 | 0.0073 |
| 2024_09_20 22:00 | 3270515 | 2 | 14.5112 | 19.3654 | -109.1111 | 18.1538 | 183.1329 | 0.0041 | 0.0031 |
| 2024_09_20 22:00 | 3215589 | 3 | 15.2575 | 7.4303 | -114.6785 | 9.8973 | 173.3239 | 0.0121 | 0.0083 |
| 2024_09_20 22:00 | 3218325 | 4 | 8.1964 | 19.7337 | -114.9458 | 16.0568 | 86.8615 | 0.0030 | 0.0040 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417061_16300653 | 504990 | 683 | -87.9 | 504990 | 271 | -85.3 | 504990 | 300 | -88.9 | 504990 | 18 |
| MR_1774417061_B4AF2166 | 504990 | 271 | -86.6 | 504990 | 683 | -86.8 | 504990 | 300 | -88.2 | 504990 | 18 |
| MR_1774417061_3BA8A206 | 504990 | 271 | -87.7 | 504990 | 683 | -83.9 | 504990 | 300 | -86.7 | 504990 | 18 |
| MR_1774417061_29CADBCB | 504990 | 271 | -88.4 | 504990 | 683 | -84.8 | 504990 | 300 | -89.0 | 504990 | 18 |
| MR_1774417061_42B64A13 | 504990 | 683 | -87.6 | 504990 | 271 | -86.7 | 504990 | 300 | -89.7 | 504990 | 18 |
| MR_1774417061_00D2A3BF | 504990 | 683 | -87.7 | 504990 | 271 | -87.0 | 504990 | 300 | -87.0 | 504990 | 18 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1842: `44e4051f-9bc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `44e4051f-9bca-4e80-ad97-c17e5415a9ef` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Lift the tilt angle  of 3265911_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1842] topology](images/train_1842.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3267078_3
- `C2`: Decrease transmission power for 3267078_3
- `C3`: Add neighbor relationship between 3265911_1 and 3239961_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267078_3
- `C5`: Increase A3 Offset threshold for 3239961_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239961_2
- `C7`: Press down the tilt angle of 3267078_3 by 4 degrees
- `C8`: Add neighbor relationship between 3267078_3 and 3239961_2
- `C9`: Increase transmission power for 3239961_2
- `C10`: Decrease A3 Offset threshold for 3267078_3
- `C11`: Press down the tilt angle  of 3265911_1 by 10 degrees
- `C12`: Adjust the azimuth of 3265911_1 by 50 degrees
- `C13`: Adjust the azimuth of 3267078_3 by 26 degrees
- `C14`: Check test server and transmission issues
- `C15`: Lift the tilt angle  of 3265911_1 by 10 degrees **← 정답**
- `C16`: Lift the tilt angle of 3267078_3 by 4 degrees
- `C17`: Decrease transmission power for 3239961_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267078_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239961_2
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase transmission power for 3267078_3
- `C22`: Decrease A3 Offset threshold for 3239961_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.544 | MS1 | 121.4656689833 | 31.1446188792 | 509 | 504990 | -91.32 | 12.09 | 362.12 | 0.00 | 2.29 | 1596 |
| 2024-09-20 22:21:32.314 | MS1 | 121.4656716289 | 31.1446286982 | 509 | 504990 | -89.94 | 17.37 | 490.86 | 0.17 | 2.12 | 1570 |
| 2024-09-20 22:21:33.612 | MS1 | 121.4656605679 | 31.1446321930 | 509 | 504990 | -86.74 | 17.87 | 524.01 | 0.13 | 2.44 | 1578 |
| 2024-09-20 22:21:34.296 | MS1 | 121.4656621451 | 31.1446219693 | 509 | 504990 | -86.98 | 17.31 | 65.14 | 0.20 | 2.53 | 1567 |
| 2024-09-20 22:21:35.384 | MS1 | 121.4656724476 | 31.1446324263 | 509 | 504990 | -88.31 | 16.84 | 55.97 | 0.07 | 2.54 | 1567 |
| 2024-09-20 22:21:36.355 | MS1 | 121.4656737227 | 31.1446204310 | 509 | 504990 | -90.21 | 17.87 | 55.24 | 0.17 | 2.19 | 1590 |
| 2024-09-20 22:21:37.656 | MS1 | 121.4656609760 | 31.1446370699 | 509 | 504990 | -90.70 | 8.88 | 69.87 | 0.11 | 2.43 | 1563 |
| 2024-09-20 22:21:38.871 | MS1 | 121.4656645667 | 31.1446303376 | 509 | 504990 | -89.82 | 12.68 | 88.09 | 0.16 | 2.75 | 1581 |
| 2024-09-20 22:21:39.546 | MS1 | 121.4656677735 | 31.1446313777 | 509 | 504990 | -93.20 | 12.22 | 70.53 | 0.20 | 2.88 | 1578 |
| 2024-09-20 22:21:40.645 | MS1 | 121.4656656954 | 31.1446258254 | 509 | 504990 | -93.15 | 11.86 | 356.84 | 0.07 | 2.71 | 1569 |
| 2024-09-20 22:21:41.496 | MS1 | 121.4656591529 | 31.1446350436 | 509 | 504990 | -93.87 | 10.92 | 363.96 | 0.15 | 2.93 | 1560 |
| 2024-09-20 22:21:42.152 | MS1 | 121.4656724470 | 31.1446183200 | 509 | 504990 | -93.80 | 12.64 | 396.87 | 0.06 | 2.99 | 1566 |

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
| 3239961 | 2 | 121.4758209501 | 31.1442739671 | 86 | 11 | 6 | 33.8 | TDD | 516 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3265911 | 1 | 121.4663725385 | 31.1516289092 | 63 | 2 | 10 | 45.9 | TDD | 58 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3267078 | 3 | 121.4689955100 | 31.1488280147 | 240 | 1 | 10 | 27.4 | TDD | 509 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3267278 | 4 | 121.4732202838 | 31.1536150352 | 72 | 2 | 2 | 23.9 | TDD | 292 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.047 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.071 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.173 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.173 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.854 | NREventA3 | measId:2;ServCellPCI:172;Se... |
| 2024-09-20 22:21:38.094 | NRHandoverAttempt | SourcePCI:172;SourceNR-ARFC... |
| 2024-09-20 22:21:38.127 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.138 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.241 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.241 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265911 | 1 | 10.2082 | 14.1623 | -115.5190 | 5.6847 | 162.7841 | 0.0061 | 0.0083 |
| 2024_09_20 22:00 | 3239961 | 2 | 13.6927 | 19.6493 | -115.7767 | 11.4823 | 145.6332 | 0.0153 | 0.0105 |
| 2024_09_20 22:00 | 3267078 | 3 | 85.1477 | 93.5754 | -115.8433 | 19.0923 | 149.0503 | 0.0121 | 0.0112 |
| 2024_09_20 22:00 | 3267278 | 4 | 11.5572 | 8.9077 | -117.3251 | 15.1801 | 96.7576 | 0.0118 | 0.0107 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413505_6BC9212B | 504990 | 509 | -85.0 | 504990 | 516 | -90.4 | 504990 | 58 | -100.6 | 504990 | 292 |
| MR_1774413505_5B1C2EC3 | 504990 | 509 | -86.6 | 504990 | 516 | -87.1 | 504990 | 58 | -100.5 | 504990 | 292 |
| MR_1774413505_DF1D1A9A | 504990 | 509 | -86.7 | 504990 | 516 | -87.4 | 504990 | 58 | -99.3 | 504990 | 292 |
| MR_1774413505_7E4240A6 | 504990 | 509 | -88.1 | 504990 | 516 | -87.9 | 504990 | 58 | -98.1 | 504990 | 292 |
| MR_1774413505_BC099259 | 504990 | 509 | -87.2 | 504990 | 516 | -90.4 | 504990 | 58 | -99.2 | 504990 | 292 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1843: `dd612ece-57d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dd612ece-57dc-4841-937b-040c8f7729a1` |
| Tag | **multiple-answer** |
| 정답 | **C3|C7|C10|C11** |
| C3 의미 | Increase A3 Offset threshold for 3257591_4 |
| C7 의미 | Increase A3 Offset threshold for 3214765_3 |
| C10 의미 | Decrease transmission power for 3214765_3 |
| C11 의미 | Press down the tilt angle  of 3214765_3 by 3 degrees |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1843] topology](images/train_1843.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3257591_4 by 2 degrees
- `C2`: Check test server and transmission issues
- `C3`: Increase A3 Offset threshold for 3257591_4 **← 정답**
- `C4`: Add neighbor relationship between 3257591_4 and 3214765_3
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Adjust the azimuth of 3214765_3 by 17 degrees
- `C7`: Increase A3 Offset threshold for 3214765_3 **← 정답**
- `C8`: Decrease A3 Offset threshold for 3214765_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214765_3
- `C10`: Decrease transmission power for 3214765_3 **← 정답**
- `C11`: Press down the tilt angle  of 3214765_3 by 3 degrees **← 정답**
- `C12`: Increase transmission power for 3214765_3
- `C13`: Press down the tilt angle of 3257591_4 by 2 degrees
- `C14`: Lift the tilt angle  of 3214765_3 by 3 degrees
- `C15`: Increase transmission power for 3257591_4
- `C16`: Add neighbor relationship between 3249755_2 and 3214765_3
- `C17`: Decrease A3 Offset threshold for 3257591_4
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214765_3
- `C19`: Adjust the azimuth of 3257591_4 by 44 degrees
- `C20`: Decrease transmission power for 3257591_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257591_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257591_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.174 | MS1 | 121.4656723063 | 31.1446249791 | 441 | 504990 | -77.77 | 16.59 | 366.17 | 0.03 | 2.15 | 1566 |
| 2024-09-20 22:21:32.336 | MS1 | 121.4656758069 | 31.1446242617 | 441 | 504990 | -75.39 | 13.30 | 453.94 | 0.19 | 2.77 | 1563 |
| 2024-09-20 22:21:33.326 | MS1 | 121.4656692986 | 31.1446373579 | 441 | 504990 | -77.88 | 13.00 | 542.13 | 0.09 | 2.02 | 1598 |
| 2024-09-20 22:21:34.898 | MS1 | 121.4656669547 | 31.1446338858 | 413 | 504990 | -86.77 | 2.65 | 78.84 | 0.20 | 1.40 | 1595 |
| 2024-09-20 22:21:35.937 | MS1 | 121.4656775872 | 31.1446244708 | 413 | 504990 | -88.88 | 1.66 | 48.05 | 0.14 | 1.19 | 1566 |
| 2024-09-20 22:21:36.923 | MS1 | 121.4656586210 | 31.1446360167 | 441 | 504990 | -88.81 | 3.89 | 24.63 | 0.03 | 1.02 | 1599 |
| 2024-09-20 22:21:37.704 | MS1 | 121.4656627095 | 31.1446228262 | 441 | 504990 | -86.73 | 4.98 | 51.34 | 0.12 | 1.31 | 1575 |
| 2024-09-20 22:21:38.821 | MS1 | 121.4656774573 | 31.1446367658 | 413 | 504990 | -84.54 | 1.52 | 77.41 | 0.18 | 1.24 | 1591 |
| 2024-09-20 22:21:39.261 | MS1 | 121.4656707595 | 31.1446313801 | 413 | 504990 | -87.92 | 5.00 | 66.29 | 0.06 | 1.31 | 1574 |
| 2024-09-20 22:21:40.739 | MS1 | 121.4656666619 | 31.1446365841 | 413 | 504990 | -76.84 | 14.77 | 540.91 | 0.09 | 2.26 | 1598 |
| 2024-09-20 22:21:41.376 | MS1 | 121.4656731375 | 31.1446323951 | 413 | 504990 | -84.32 | 15.68 | 328.40 | 0.16 | 2.36 | 1587 |
| 2024-09-20 22:21:42.379 | MS1 | 121.4656750663 | 31.1446285984 | 413 | 504990 | -81.11 | 13.90 | 344.94 | 0.03 | 2.49 | 1574 |

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
| 3214765 | 3 | 121.4681773261 | 31.1544715136 | 175 | 1 | 2 | 46.3 | TDD | 788 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3245361 | 1 | 121.4692076671 | 31.1474290069 | 27 | 13 | 4 | 19.9 | TDD | 992 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3249755 | 2 | 121.4688476101 | 31.1516943982 | 295 | 5 | 11 | 33.9 | TDD | 691 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3257591 | 4 | 121.4731460828 | 31.1517839038 | 178 | 0 | 3 | 37.6 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3273183 | 5 | 121.4671237820 | 31.1460495690 | 162 | 6 | 3 | 18.9 | TDD | 413 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.138 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.158 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.269 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.269 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.988 | NREventA3 | measId:2;ServCellPCI:32;Ser... |
| 2024-09-20 22:21:34.228 | NRHandoverAttempt | SourcePCI:32;SourceNR-ARFCN... |
| 2024-09-20 22:21:34.278 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.291 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:34.404 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.404 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.988 | NREventA3 | measId:2;ServCellPCI:275;Se... |
| 2024-09-20 22:21:36.228 | NRHandoverAttempt | SourcePCI:275;SourceNR-ARFC... |
| 2024-09-20 22:21:36.268 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.281 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.383 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.383 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.988 | NREventA3 | measId:2;ServCellPCI:32;Ser... |
| 2024-09-20 22:21:38.228 | NRHandoverAttempt | SourcePCI:32;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.272 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.283 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.430 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.430 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245361 | 1 | 5.6201 | 19.2952 | -114.6240 | 19.4512 | 92.2551 | 0.0171 | 0.0108 |
| 2024_09_20 22:00 | 3249755 | 2 | 7.3140 | 19.3715 | -117.0144 | 10.1582 | 138.8846 | 0.0048 | 0.0197 |
| 2024_09_20 22:00 | 3214765 | 3 | 15.1968 | 5.1302 | -117.4886 | 8.1977 | 157.1880 | 0.0172 | 0.0010 |
| 2024_09_20 22:00 | 3257591 | 4 | 10.0060 | 6.9376 | -115.5562 | 10.2583 | 153.4192 | 0.0104 | 0.0190 |
| 2024_09_20 22:00 | 3273183 | 5 | 19.6002 | 12.0500 | -114.2825 | 8.1851 | 148.9394 | 0.0129 | 0.0008 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413617_03637338 | 504990 | 413 | -85.5 | 504990 | 441 | -83.3 | 504990 | 788 | -83.8 | 504990 | 691 |
| MR_1774413617_05FC4529 | 504990 | 413 | -86.5 | 504990 | 441 | -82.7 | 504990 | 788 | -86.2 | 504990 | 691 |
| MR_1774413617_F603262B | 504990 | 413 | -86.9 | 504990 | 441 | -82.8 | 504990 | 788 | -85.1 | 504990 | 691 |
| MR_1774413617_2CC9E276 | 504990 | 441 | -86.2 | 504990 | 413 | -83.3 | 504990 | 788 | -85.4 | 504990 | 691 |
| MR_1774413617_7AD7BA17 | 504990 | 441 | -88.6 | 504990 | 413 | -81.8 | 504990 | 788 | -86.4 | 504990 | 691 |
| MR_1774413617_28DC2EC6 | 504990 | 413 | -85.9 | 504990 | 441 | -80.7 | 504990 | 788 | -86.2 | 504990 | 691 |
| MR_1774413617_BD22302F | 504990 | 441 | -87.4 | 504990 | 413 | -82.5 | 504990 | 788 | -85.2 | 504990 | 691 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1844: `e593f712-465...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e593f712-465f-4ae7-82e9-05ee537ec039` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1844] topology](images/train_1844.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3233748_4
- `C2`: Decrease transmission power for 3247185_3
- `C3`: Adjust the azimuth of 3233748_4 by 7 degrees
- `C4`: Lift the tilt angle of 3247185_3 by 10 degrees
- `C5`: Lift the tilt angle  of 3233748_4 by 10 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247185_3
- `C7`: Decrease A3 Offset threshold for 3233748_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233748_4
- `C9`: Press down the tilt angle  of 3233748_4 by 10 degrees
- `C10`: Increase transmission power for 3247185_3
- `C11`: Adjust the azimuth of 3247185_3 by 50 degrees
- `C12`: Decrease A3 Offset threshold for 3247185_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233748_4
- `C14`: Add neighbor relationship between 3262814_2 and 3233748_4
- `C15`: Check test server and transmission issues
- `C16`: Add neighbor relationship between 3247185_3 and 3233748_4
- `C17`: Increase A3 Offset threshold for 3247185_3
- `C18`: Increase A3 Offset threshold for 3233748_4
- `C19`: Press down the tilt angle of 3247185_3 by 10 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247185_3
- `C21`: Increase transmission power for 3233748_4
- `C22`: Insufficient data; more data is needed for judgment. **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.668 | MS1 | 121.4656745222 | 31.1446314633 | 741 | 504990 | -85.25 | 12.89 | 551.22 | 0.11 | 2.46 | 1579 |
| 2024-09-20 22:21:32.103 | MS1 | 121.4656591625 | 31.1446242509 | 741 | 504990 | -88.50 | 12.73 | 339.35 | 0.14 | 2.99 | 1577 |
| 2024-09-20 22:21:33.825 | MS1 | 121.4656769530 | 31.1446210136 | 741 | 504990 | -91.92 | 15.38 | 486.58 | 0.12 | 2.54 | 1585 |
| 2024-09-20 22:21:34.355 | MS1 | 121.4656764509 | 31.1446195367 | 741 | 504990 | -87.46 | 17.27 | 73.99 | 0.17 | 2.37 | 1560 |
| 2024-09-20 22:21:35.549 | MS1 | 121.4656693869 | 31.1446250857 | 741 | 504990 | -87.47 | 14.54 | 87.41 | 0.05 | 2.43 | 1568 |
| 2024-09-20 22:21:36.346 | MS1 | 121.4656606495 | 31.1446305156 | 741 | 504990 | -86.57 | 16.20 | 86.59 | 0.01 | 2.33 | 1588 |
| 2024-09-20 22:21:37.761 | MS1 | 121.4656756483 | 31.1446203609 | 741 | 504990 | -93.78 | 7.97 | 81.22 | 0.16 | 2.94 | 1585 |
| 2024-09-20 22:21:38.980 | MS1 | 121.4656680278 | 31.1446197555 | 741 | 504990 | -89.29 | 8.15 | 85.24 | 0.14 | 2.05 | 1575 |
| 2024-09-20 22:21:39.708 | MS1 | 121.4656636903 | 31.1446228455 | 741 | 504990 | -90.94 | 10.66 | 82.65 | 0.02 | 2.10 | 1600 |
| 2024-09-20 22:21:40.941 | MS1 | 121.4656707835 | 31.1446228142 | 741 | 504990 | -92.19 | 8.61 | 421.00 | 0.11 | 2.09 | 1583 |
| 2024-09-20 22:21:41.738 | MS1 | 121.4656589424 | 31.1446357146 | 741 | 504990 | -91.47 | 11.33 | 454.86 | 0.03 | 2.76 | 1578 |
| 2024-09-20 22:21:42.805 | MS1 | 121.4656769797 | 31.1446345994 | 741 | 504990 | -89.96 | 7.51 | 335.80 | 0.16 | 2.47 | 1564 |

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
| 3233748 | 4 | 121.4658897910 | 31.1482622520 | 176 | 10 | 7 | 37.0 | TDD | 558 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3247185 | 3 | 121.4700605572 | 31.1472991337 | 300 | 12 | 0 | 35.5 | TDD | 741 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3262814 | 2 | 121.4649981710 | 31.1469913680 | 82 | 2 | 3 | 19.7 | TDD | 954 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3269481 | 1 | 121.4695087140 | 31.1535505915 | 43 | 0 | 6 | 24.7 | TDD | 617 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.229 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.250 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.383 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.383 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.123 | NREventA3 | measId:2;ServCellPCI:517;Se... |
| 2024-09-20 22:21:38.363 | NRHandoverAttempt | SourcePCI:517;SourceNR-ARFC... |
| 2024-09-20 22:21:38.400 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.412 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.518 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.518 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3269481 | 1 | 79.2435 | 91.0279 | -115.6036 | 14.1172 | 88.7197 | 0.0071 | 0.0108 |
| 2024_09_19 22:00 | 3262814 | 2 | 89.0846 | 76.1354 | -115.8573 | 10.6455 | 162.1636 | 0.0028 | 0.0019 |
| 2024_09_19 22:00 | 3247185 | 3 | 93.2134 | 78.3111 | -115.3375 | 17.0574 | 142.4765 | 0.0092 | 0.0193 |
| 2024_09_19 22:00 | 3233748 | 4 | 80.2951 | 79.9979 | -117.4578 | 6.8995 | 180.2144 | 0.0022 | 0.0194 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416393_96E31590 | 504990 | 741 | -85.9 | 504990 | 558 | -96.2 | 504990 | 954 | -95.9 | 504990 | 617 |
| MR_1774416393_5A76B82E | 504990 | 741 | -87.7 | 504990 | 558 | -95.6 | 504990 | 954 | -97.3 | 504990 | 617 |
| MR_1774416393_9A279241 | 504990 | 741 | -87.6 | 504990 | 558 | -97.3 | 504990 | 954 | -95.8 | 504990 | 617 |
| MR_1774416393_0272C224 | 504990 | 741 | -89.4 | 504990 | 558 | -97.9 | 504990 | 954 | -94.7 | 504990 | 617 |
| MR_1774416393_148C0969 | 504990 | 741 | -86.4 | 504990 | 558 | -95.1 | 504990 | 954 | -97.2 | 504990 | 617 |
| MR_1774416393_EA4411B3 | 504990 | 741 | -88.9 | 504990 | 558 | -96.1 | 504990 | 954 | -96.1 | 504990 | 617 |
| MR_1774416393_B6F7DB54 | 504990 | 741 | -89.1 | 504990 | 558 | -96.1 | 504990 | 954 | -97.0 | 504990 | 617 |
| MR_1774416393_50D72AFD | 504990 | 741 | -87.9 | 504990 | 558 | -98.1 | 504990 | 954 | -96.7 | 504990 | 617 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1845: `d0ee46a6-dee...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d0ee46a6-dee1-427b-8eef-e4e40fd26839` |
| Tag | **multiple-answer** |
| 정답 | **C3|C6|C15|C17** |
| C3 의미 | Increase A3 Offset threshold for 3218256_1 |
| C6 의미 | Decrease transmission power for 3218256_1 |
| C15 의미 | Press down the tilt angle  of 3218256_1 by 4 degrees |
| C17 의미 | Increase A3 Offset threshold for 3260786_5 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1845] topology](images/train_1845.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218256_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260786_5
- `C3`: Increase A3 Offset threshold for 3218256_1 **← 정답**
- `C4`: Decrease A3 Offset threshold for 3218256_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260786_5
- `C6`: Decrease transmission power for 3218256_1 **← 정답**
- `C7`: Press down the tilt angle of 3260786_5 by 6 degrees
- `C8`: Check test server and transmission issues
- `C9`: Decrease transmission power for 3260786_5
- `C10`: Add neighbor relationship between 3260786_5 and 3218256_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218256_1
- `C12`: Increase transmission power for 3218256_1
- `C13`: Adjust the azimuth of 3260786_5 by 31 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Press down the tilt angle  of 3218256_1 by 4 degrees **← 정답**
- `C16`: Add neighbor relationship between 3218519_4 and 3218256_1
- `C17`: Increase A3 Offset threshold for 3260786_5 **← 정답**
- `C18`: Lift the tilt angle of 3260786_5 by 6 degrees
- `C19`: Increase transmission power for 3260786_5
- `C20`: Decrease A3 Offset threshold for 3260786_5
- `C21`: Adjust the azimuth of 3218256_1 by 5 degrees
- `C22`: Lift the tilt angle  of 3218256_1 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.457 | MS1 | 121.4656707478 | 31.1446357470 | 927 | 504990 | -78.64 | 15.77 | 485.63 | 0.07 | 2.85 | 1570 |
| 2024-09-20 22:21:32.164 | MS1 | 121.4656690866 | 31.1446180825 | 927 | 504990 | -81.55 | 14.41 | 479.64 | 0.14 | 2.35 | 1584 |
| 2024-09-20 22:21:33.355 | MS1 | 121.4656620563 | 31.1446320794 | 927 | 504990 | -83.45 | 17.66 | 517.47 | 0.09 | 2.66 | 1593 |
| 2024-09-20 22:21:34.706 | MS1 | 121.4656689461 | 31.1446217579 | 804 | 504990 | -89.13 | 4.78 | 49.32 | 0.18 | 1.33 | 1584 |
| 2024-09-20 22:21:35.924 | MS1 | 121.4656714443 | 31.1446293836 | 804 | 504990 | -85.04 | 1.32 | 35.38 | 0.13 | 1.38 | 1598 |
| 2024-09-20 22:21:36.370 | MS1 | 121.4656637601 | 31.1446320203 | 927 | 504990 | -87.51 | 3.65 | 86.10 | 0.10 | 1.14 | 1593 |
| 2024-09-20 22:21:37.502 | MS1 | 121.4656627916 | 31.1446292992 | 927 | 504990 | -85.62 | 2.15 | 74.42 | 0.00 | 1.41 | 1576 |
| 2024-09-20 22:21:38.615 | MS1 | 121.4656682245 | 31.1446231145 | 804 | 504990 | -88.40 | 4.50 | 88.34 | 0.13 | 1.39 | 1584 |
| 2024-09-20 22:21:39.717 | MS1 | 121.4656688362 | 31.1446246790 | 804 | 504990 | -89.43 | 2.96 | 53.16 | 0.00 | 1.46 | 1562 |
| 2024-09-20 22:21:40.840 | MS1 | 121.4656738448 | 31.1446328837 | 804 | 504990 | -83.84 | 12.54 | 422.26 | 0.17 | 2.11 | 1590 |
| 2024-09-20 22:21:41.849 | MS1 | 121.4656743330 | 31.1446199924 | 804 | 504990 | -77.59 | 15.94 | 533.44 | 0.05 | 2.78 | 1599 |
| 2024-09-20 22:21:42.475 | MS1 | 121.4656730131 | 31.1446317688 | 804 | 504990 | -80.62 | 13.67 | 324.01 | 0.06 | 2.08 | 1572 |

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
| 3211735 | 3 | 121.4757681758 | 31.1496980562 | 227 | 12 | 9 | 40.9 | TDD | 941 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3218256 | 1 | 121.4754119389 | 31.1486338536 | 249 | 2 | 3 | 32.3 | TDD | 481 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3218519 | 4 | 121.4682420938 | 31.1523517765 | 146 | 1 | 7 | 21.9 | TDD | 54 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3248996 | 2 | 121.4716058270 | 31.1502908616 | 244 | 13 | 4 | 39.9 | TDD | 804 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3260786 | 5 | 121.4665128845 | 31.1493945620 | 220 | 3 | 1 | 24.7 | TDD | 927 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.319 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.334 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.474 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.474 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.218 | NREventA3 | measId:2;ServCellPCI:860;Se... |
| 2024-09-20 22:21:34.458 | NRHandoverAttempt | SourcePCI:860;SourceNR-ARFC... |
| 2024-09-20 22:21:34.498 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.511 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:34.649 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.649 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.218 | NREventA3 | measId:2;ServCellPCI:915;Se... |
| 2024-09-20 22:21:36.458 | NRHandoverAttempt | SourcePCI:915;SourceNR-ARFC... |
| 2024-09-20 22:21:36.498 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.513 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.657 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.657 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.218 | NREventA3 | measId:2;ServCellPCI:860;Se... |
| 2024-09-20 22:21:38.458 | NRHandoverAttempt | SourcePCI:860;SourceNR-ARFC... |
| 2024-09-20 22:21:38.493 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.508 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.628 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.628 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218256 | 1 | 11.5833 | 10.0864 | -116.0757 | 5.5910 | 107.3580 | 0.0164 | 0.0073 |
| 2024_09_20 22:00 | 3248996 | 2 | 18.6147 | 11.7018 | -115.3855 | 5.5578 | 158.6918 | 0.0074 | 0.0189 |
| 2024_09_20 22:00 | 3211735 | 3 | 8.0649 | 10.2277 | -116.2202 | 16.1143 | 127.0866 | 0.0029 | 0.0077 |
| 2024_09_20 22:00 | 3218519 | 4 | 13.4658 | 16.4838 | -115.9841 | 16.4541 | 164.9835 | 0.0151 | 0.0003 |
| 2024_09_20 22:00 | 3260786 | 5 | 16.3228 | 19.1568 | -114.8452 | 13.7059 | 192.5764 | 0.0008 | 0.0028 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416177_825ECAC8 | 504990 | 804 | -88.5 | 504990 | 927 | -86.4 | 504990 | 481 | -89.1 | 504990 | 54 |
| MR_1774416177_7BC005F6 | 504990 | 804 | -87.9 | 504990 | 927 | -85.7 | 504990 | 481 | -87.8 | 504990 | 54 |
| MR_1774416177_7823CE61 | 504990 | 804 | -88.8 | 504990 | 927 | -87.5 | 504990 | 481 | -91.0 | 504990 | 54 |
| MR_1774416177_57125575 | 504990 | 927 | -88.0 | 504990 | 804 | -87.4 | 504990 | 481 | -88.9 | 504990 | 54 |
| MR_1774416177_B4B39492 | 504990 | 804 | -90.2 | 504990 | 927 | -86.3 | 504990 | 481 | -90.3 | 504990 | 54 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1846: `fa529e46-85f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fa529e46-85fc-488f-afa1-e47186e20b35` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1846] topology](images/train_1846.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3265476_1
- `C2`: Press down the tilt angle  of 3212423_3 by 10 degrees
- `C3`: Lift the tilt angle  of 3212423_3 by 10 degrees
- `C4`: Press down the tilt angle of 3265476_1 by 9 degrees
- `C5`: Increase A3 Offset threshold for 3212423_3
- `C6`: Adjust the azimuth of 3265476_1 by 50 degrees
- `C7`: Adjust the azimuth of 3212423_3 by 8 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212423_3
- `C9`: Decrease transmission power for 3212423_3
- `C10`: Lift the tilt angle of 3265476_1 by 9 degrees
- `C11`: Decrease A3 Offset threshold for 3212423_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265476_1
- `C13`: Add neighbor relationship between 3263594_4 and 3212423_3
- `C14`: Check test server and transmission issues
- `C15`: Insufficient data; more data is needed for judgment. **← 정답**
- `C16`: Decrease A3 Offset threshold for 3265476_1
- `C17`: Add neighbor relationship between 3265476_1 and 3212423_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212423_3
- `C19`: Increase transmission power for 3212423_3
- `C20`: Decrease transmission power for 3265476_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265476_1
- `C22`: Increase A3 Offset threshold for 3265476_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.335 | MS1 | 121.4656648629 | 31.1446200777 | 38 | 504990 | -91.88 | 12.16 | 460.09 | 0.16 | 2.16 | 1578 |
| 2024-09-20 22:21:32.470 | MS1 | 121.4656754278 | 31.1446304124 | 38 | 504990 | -90.22 | 13.13 | 574.83 | 0.03 | 2.01 | 1584 |
| 2024-09-20 22:21:33.556 | MS1 | 121.4656603775 | 31.1446343240 | 38 | 504990 | -87.90 | 16.56 | 574.85 | 0.04 | 2.14 | 1592 |
| 2024-09-20 22:21:34.966 | MS1 | 121.4656629086 | 31.1446322870 | 38 | 504990 | -88.92 | 14.04 | 67.83 | 0.16 | 2.01 | 1579 |
| 2024-09-20 22:21:35.709 | MS1 | 121.4656691020 | 31.1446309594 | 38 | 504990 | -90.55 | 12.77 | 58.70 | 0.14 | 2.21 | 1564 |
| 2024-09-20 22:21:36.866 | MS1 | 121.4656685468 | 31.1446335294 | 38 | 504990 | -90.10 | 15.29 | 48.67 | 0.12 | 2.48 | 1563 |
| 2024-09-20 22:21:37.210 | MS1 | 121.4656646531 | 31.1446291623 | 38 | 504990 | -91.96 | 12.89 | 56.46 | 0.08 | 2.06 | 1581 |
| 2024-09-20 22:21:38.228 | MS1 | 121.4656686432 | 31.1446281341 | 38 | 504990 | -91.86 | 12.90 | 72.76 | 0.05 | 2.18 | 1583 |
| 2024-09-20 22:21:39.343 | MS1 | 121.4656707482 | 31.1446277998 | 38 | 504990 | -90.38 | 8.00 | 53.87 | 0.09 | 2.41 | 1584 |
| 2024-09-20 22:21:40.965 | MS1 | 121.4656620623 | 31.1446304987 | 38 | 504990 | -92.66 | 9.77 | 371.12 | 0.04 | 2.16 | 1582 |
| 2024-09-20 22:21:41.798 | MS1 | 121.4656605531 | 31.1446323863 | 38 | 504990 | -92.67 | 9.92 | 451.89 | 0.02 | 2.01 | 1571 |
| 2024-09-20 22:21:42.580 | MS1 | 121.4656660838 | 31.1446353178 | 38 | 504990 | -89.28 | 11.98 | 373.00 | 0.07 | 2.59 | 1564 |

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
| 3212423 | 3 | 121.4672748804 | 31.1457136014 | 240 | 10 | 8 | 29.7 | TDD | 830 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3263594 | 4 | 121.4738890254 | 31.1489101897 | 120 | 8 | 11 | 39.4 | TDD | 815 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3265476 | 1 | 121.4727285560 | 31.1470540009 | 357 | 8 | 4 | 15.6 | TDD | 38 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3269459 | 2 | 121.4644153491 | 31.1485650319 | 293 | 10 | 2 | 19.4 | TDD | 266 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.643 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.663 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.807 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.807 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.461 | NREventA3 | measId:2;ServCellPCI:352;Se... |
| 2024-09-20 22:21:38.701 | NRHandoverAttempt | SourcePCI:352;SourceNR-ARFC... |
| 2024-09-20 22:21:38.748 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.762 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.901 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.901 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3265476 | 1 | 89.1516 | 79.0243 | -114.0377 | 9.1418 | 149.4873 | 0.0081 | 0.0057 |
| 2024_09_19 22:00 | 3269459 | 2 | 92.1836 | 93.0444 | -117.9215 | 9.0707 | 189.0207 | 0.0022 | 0.0090 |
| 2024_09_19 22:00 | 3212423 | 3 | 92.6692 | 76.5441 | -117.6512 | 11.6045 | 112.7344 | 0.0047 | 0.0189 |
| 2024_09_19 22:00 | 3263594 | 4 | 83.5436 | 94.1175 | -117.5074 | 5.6851 | 129.3457 | 0.0018 | 0.0184 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411983_D65E4527 | 504990 | 38 | -88.1 | 504990 | 830 | -90.0 | 504990 | 815 | -100.1 | 504990 | 266 |
| MR_1774411983_F078FB22 | 504990 | 38 | -90.1 | 504990 | 830 | -91.6 | 504990 | 815 | -101.4 | 504990 | 266 |
| MR_1774411983_4ED2475A | 504990 | 38 | -90.9 | 504990 | 830 | -90.6 | 504990 | 815 | -99.0 | 504990 | 266 |
| MR_1774411983_3C5DA8C8 | 504990 | 38 | -87.2 | 504990 | 830 | -91.1 | 504990 | 815 | -98.7 | 504990 | 266 |
| MR_1774411983_DC83F9BB | 504990 | 38 | -89.3 | 504990 | 830 | -93.5 | 504990 | 815 | -101.2 | 504990 | 266 |
| MR_1774411983_51EC0961 | 504990 | 38 | -90.4 | 504990 | 830 | -91.7 | 504990 | 815 | -99.1 | 504990 | 266 |
| MR_1774411983_DD8920E6 | 504990 | 38 | -88.9 | 504990 | 830 | -92.2 | 504990 | 815 | -98.0 | 504990 | 266 |
| MR_1774411983_2F823225 | 504990 | 38 | -90.9 | 504990 | 830 | -91.1 | 504990 | 815 | -100.8 | 504990 | 266 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1847: `d9b0ca11-c68...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d9b0ca11-c68f-4ebf-b4da-b145efd2d2d3` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1847] topology](images/train_1847.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3246027_2 by 10 degrees
- `C2`: Increase A3 Offset threshold for 3253953_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253953_1
- `C4`: Lift the tilt angle  of 3253953_1 by 10 degrees
- `C5`: Add neighbor relationship between 3246027_2 and 3253953_1
- `C6`: Press down the tilt angle  of 3253953_1 by 10 degrees
- `C7`: Add neighbor relationship between 3239669_3 and 3253953_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246027_2
- `C9`: Increase transmission power for 3246027_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253953_1
- `C11`: Increase A3 Offset threshold for 3246027_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Press down the tilt angle of 3246027_2 by 10 degrees
- `C14`: Decrease transmission power for 3246027_2
- `C15`: Decrease A3 Offset threshold for 3253953_1
- `C16`: Increase transmission power for 3253953_1
- `C17`: Decrease transmission power for 3253953_1
- `C18`: Adjust the azimuth of 3246027_2 by 50 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246027_2
- `C20`: Decrease A3 Offset threshold for 3246027_2
- `C21`: Check test server and transmission issues **← 정답**
- `C22`: Adjust the azimuth of 3253953_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.262 | MS1 | 121.4656672787 | 31.1446377796 | 315 | 504990 | -85.35 | 17.04 | 337.34 | 0.03 | 2.75 | 1587 |
| 2024-09-20 22:21:32.923 | MS1 | 121.4656636276 | 31.1446329537 | 315 | 504990 | -89.14 | 13.85 | 510.71 | 0.01 | 2.47 | 1564 |
| 2024-09-20 22:21:33.223 | MS1 | 121.4656771959 | 31.1446224217 | 315 | 504990 | -86.28 | 13.44 | 395.90 | 0.18 | 2.79 | 1577 |
| 2024-09-20 22:21:34.121 | MS1 | 121.4656734739 | 31.1446263404 | 315 | 504990 | -87.16 | 14.80 | 81.96 | 0.08 | 2.93 | 377 |
| 2024-09-20 22:21:35.473 | MS1 | 121.4656684351 | 31.1446344827 | 315 | 504990 | -87.11 | 13.64 | 82.87 | 0.05 | 2.85 | 348 |
| 2024-09-20 22:21:36.753 | MS1 | 121.4656743364 | 31.1446192966 | 315 | 504990 | -88.13 | 17.11 | 73.54 | 0.18 | 2.99 | 317 |
| 2024-09-20 22:21:37.488 | MS1 | 121.4656604788 | 31.1446378429 | 315 | 504990 | -90.29 | 11.98 | 105.12 | 0.10 | 2.46 | 377 |
| 2024-09-20 22:21:38.921 | MS1 | 121.4656707208 | 31.1446182018 | 315 | 504990 | -92.71 | 9.99 | 96.91 | 0.00 | 2.80 | 348 |
| 2024-09-20 22:21:39.523 | MS1 | 121.4656710513 | 31.1446274326 | 315 | 504990 | -89.15 | 12.30 | 82.57 | 0.14 | 2.56 | 415 |
| 2024-09-20 22:21:40.751 | MS1 | 121.4656759984 | 31.1446252099 | 315 | 504990 | -92.22 | 9.35 | 553.50 | 0.14 | 2.23 | 1575 |
| 2024-09-20 22:21:41.921 | MS1 | 121.4656758131 | 31.1446224792 | 315 | 504990 | -93.14 | 11.24 | 406.51 | 0.11 | 2.13 | 1564 |
| 2024-09-20 22:21:42.482 | MS1 | 121.4656583953 | 31.1446353245 | 315 | 504990 | -92.87 | 9.89 | 491.10 | 0.04 | 2.04 | 1571 |

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
| 3239669 | 3 | 121.4723691928 | 31.1539709148 | 64 | 3 | 8 | 26.8 | TDD | 294 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3246027 | 2 | 121.4643569301 | 31.1554915310 | 35 | 12 | 8 | 15.3 | TDD | 315 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3253953 | 1 | 121.4667292015 | 31.1490287795 | 20 | 9 | 7 | 37.9 | TDD | 320 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3276390 | 4 | 121.4649529023 | 31.1475616388 | 116 | 1 | 11 | 23.2 | TDD | 720 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.093 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.114 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.261 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.261 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.894 | NREventA3 | measId:2;ServCellPCI:809;Se... |
| 2024-09-20 22:21:38.134 | NRHandoverAttempt | SourcePCI:809;SourceNR-ARFC... |
| 2024-09-20 22:21:38.170 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.185 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.332 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.332 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253953 | 1 | 14.4825 | 10.8434 | -117.0632 | 13.5485 | 107.4927 | 0.0178 | 0.0026 |
| 2024_09_20 22:00 | 3246027 | 2 | 10.1832 | 13.0356 | -117.7552 | 18.7554 | 159.5002 | 0.0003 | 0.0015 |
| 2024_09_20 22:00 | 3239669 | 3 | 5.6989 | 8.8215 | -114.1823 | 11.7585 | 141.4457 | 0.0113 | 0.0125 |
| 2024_09_20 22:00 | 3276390 | 4 | 8.3149 | 14.2746 | -115.4679 | 19.7967 | 175.1516 | 0.0168 | 0.0133 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412974_C596D04E | 504990 | 315 | -85.8 | 504990 | 320 | -92.6 | 504990 | 294 | -95.2 | 504990 | 720 |
| MR_1774412974_E8816884 | 504990 | 315 | -87.2 | 504990 | 320 | -91.4 | 504990 | 294 | -93.7 | 504990 | 720 |
| MR_1774412974_7E0520A4 | 504990 | 315 | -86.4 | 504990 | 320 | -90.4 | 504990 | 294 | -95.5 | 504990 | 720 |
| MR_1774412974_43AE2623 | 504990 | 315 | -89.0 | 504990 | 320 | -89.2 | 504990 | 294 | -93.3 | 504990 | 720 |
| MR_1774412974_86C09B62 | 504990 | 315 | -87.9 | 504990 | 320 | -91.6 | 504990 | 294 | -94.1 | 504990 | 720 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1848: `a84366be-3c0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a84366be-3c09-4a35-82ae-3c7373a75700` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3256167_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1848] topology](images/train_1848.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256167_3 **← 정답**
- `C2`: Adjust the azimuth of 3256167_3 by 38 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225165_2
- `C4`: Decrease transmission power for 3256167_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225165_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256167_3
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Increase transmission power for 3225165_2
- `C9`: Press down the tilt angle of 3256167_3 by 5 degrees
- `C10`: Increase A3 Offset threshold for 3225165_2
- `C11`: Check test server and transmission issues
- `C12`: Adjust the azimuth of 3225165_2 by 50 degrees
- `C13`: Decrease A3 Offset threshold for 3225165_2
- `C14`: Lift the tilt angle  of 3225165_2 by 4 degrees
- `C15`: Lift the tilt angle of 3256167_3 by 5 degrees
- `C16`: Decrease transmission power for 3225165_2
- `C17`: Add neighbor relationship between 3258851_4 and 3225165_2
- `C18`: Increase A3 Offset threshold for 3256167_3
- `C19`: Add neighbor relationship between 3256167_3 and 3225165_2
- `C20`: Increase transmission power for 3256167_3
- `C21`: Press down the tilt angle  of 3225165_2 by 4 degrees
- `C22`: Decrease A3 Offset threshold for 3256167_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.183 | MS1 | 121.4656618780 | 31.1446352996 | 403 | 504990 | -89.45 | 15.64 | 542.61 | 0.19 | 2.44 | 1593 |
| 2024-09-20 22:21:32.601 | MS1 | 121.4656776294 | 31.1446190152 | 403 | 504990 | -87.90 | 15.55 | 358.93 | 0.13 | 2.31 | 1590 |
| 2024-09-20 22:21:33.857 | MS1 | 121.4656704367 | 31.1446358408 | 403 | 504990 | -89.10 | 17.35 | 527.70 | 0.02 | 2.58 | 1579 |
| 2024-09-20 22:21:34.586 | MS1 | 121.4656779324 | 31.1446259324 | 403 | 504990 | -88.10 | 13.06 | 83.86 | 0.58 | 2.15 | 506 |
| 2024-09-20 22:21:35.620 | MS1 | 121.4656594507 | 31.1446212617 | 403 | 504990 | -90.47 | 13.91 | 56.43 | 0.61 | 2.37 | 543 |
| 2024-09-20 22:21:36.583 | MS1 | 121.4656625991 | 31.1446281579 | 403 | 504990 | -86.20 | 12.67 | 63.95 | 0.67 | 2.99 | 542 |
| 2024-09-20 22:21:37.755 | MS1 | 121.4656647031 | 31.1446254064 | 403 | 504990 | -92.94 | 9.68 | 72.35 | 0.64 | 2.81 | 541 |
| 2024-09-20 22:21:38.553 | MS1 | 121.4656698862 | 31.1446302780 | 403 | 504990 | -90.58 | 11.74 | 101.68 | 0.54 | 2.13 | 585 |
| 2024-09-20 22:21:39.817 | MS1 | 121.4656710567 | 31.1446200673 | 403 | 504990 | -90.92 | 10.00 | 53.24 | 0.54 | 2.95 | 557 |
| 2024-09-20 22:21:40.772 | MS1 | 121.4656690121 | 31.1446329586 | 403 | 504990 | -89.26 | 8.22 | 420.36 | 0.15 | 2.62 | 1569 |
| 2024-09-20 22:21:41.177 | MS1 | 121.4656758817 | 31.1446189653 | 403 | 504990 | -91.09 | 12.10 | 546.20 | 0.01 | 2.83 | 1569 |
| 2024-09-20 22:21:42.921 | MS1 | 121.4656760796 | 31.1446185320 | 403 | 504990 | -90.89 | 10.37 | 421.83 | 0.10 | 2.66 | 1591 |

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
| 3225165 | 2 | 121.4709214360 | 31.1545933224 | 317 | 3 | 12 | 29.8 | TDD | 611 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3256167 | 3 | 121.4715340107 | 31.1493555152 | 189 | 4 | 7 | 17.0 | TDD | 403 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3258851 | 4 | 121.4746559571 | 31.1448138066 | 203 | 13 | 8 | 42.7 | TDD | 365 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3278182 | 1 | 121.4713656101 | 31.1495396877 | 61 | 13 | 11 | 41.3 | TDD | 563 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.149 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.165 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.279 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.279 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.032 | NREventA3 | measId:2;ServCellPCI:278;Se... |
| 2024-09-20 22:21:38.272 | NRHandoverAttempt | SourcePCI:278;SourceNR-ARFC... |
| 2024-09-20 22:21:38.319 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.332 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.476 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.476 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278182 | 1 | 6.3470 | 8.7900 | -114.6850 | 16.1377 | 197.2534 | 0.0010 | 0.0167 |
| 2024_09_20 22:00 | 3225165 | 2 | 6.6201 | 8.2782 | -115.2973 | 8.7952 | 128.6862 | 0.0122 | 0.0047 |
| 2024_09_20 22:00 | 3256167 | 3 | 10.6520 | 10.5729 | -117.4110 | 9.1015 | 177.2363 | 0.0122 | 0.0135 |
| 2024_09_20 22:00 | 3258851 | 4 | 5.4559 | 8.8148 | -117.2948 | 17.6964 | 123.4190 | 0.0074 | 0.0162 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414620_A59CC413 | 504990 | 403 | -90.0 | 504990 | 611 | -96.9 | 504990 | 365 | -96.3 | 504990 | 563 |
| MR_1774414620_80066F2F | 504990 | 403 | -88.7 | 504990 | 611 | -96.5 | 504990 | 365 | -98.3 | 504990 | 563 |
| MR_1774414620_537FC313 | 504990 | 403 | -87.8 | 504990 | 611 | -96.1 | 504990 | 365 | -99.1 | 504990 | 563 |
| MR_1774414620_3EFCE082 | 504990 | 403 | -89.2 | 504990 | 611 | -97.3 | 504990 | 365 | -95.4 | 504990 | 563 |
| MR_1774414620_AE660483 | 504990 | 403 | -86.4 | 504990 | 611 | -96.1 | 504990 | 365 | -97.5 | 504990 | 563 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1849: `0b9dc5f8-67e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0b9dc5f8-67ea-4c46-9655-015cd915d189` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Add neighbor relationship between 3271102_1 and 3279703_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1849] topology](images/train_1849.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Lift the tilt angle of 3271102_1 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279703_4
- `C4`: Add neighbor relationship between 3251379_3 and 3279703_4
- `C5`: Decrease A3 Offset threshold for 3279703_4
- `C6`: Increase transmission power for 3279703_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271102_1
- `C8`: Decrease A3 Offset threshold for 3271102_1
- `C9`: Adjust the azimuth of 3279703_4 by 8 degrees
- `C10`: Add neighbor relationship between 3271102_1 and 3279703_4 **← 정답**
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271102_1
- `C12`: Lift the tilt angle  of 3279703_4 by 4 degrees
- `C13`: Decrease transmission power for 3271102_1
- `C14`: Increase A3 Offset threshold for 3271102_1
- `C15`: Press down the tilt angle of 3271102_1 by 10 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Adjust the azimuth of 3271102_1 by 50 degrees
- `C18`: Increase transmission power for 3271102_1
- `C19`: Press down the tilt angle  of 3279703_4 by 4 degrees
- `C20`: Decrease transmission power for 3279703_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279703_4
- `C22`: Increase A3 Offset threshold for 3279703_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.873 | MS1 | 121.4656773118 | 31.1446330581 | 514 | 504990 | -80.53 | 14.01 | 526.52 | 0.12 | 2.94 | 1583 |
| 2024-09-20 22:21:32.821 | MS1 | 121.4656764353 | 31.1446334098 | 514 | 504990 | -77.83 | 15.55 | 521.02 | 0.03 | 2.35 | 1573 |
| 2024-09-20 22:21:33.196 | MS1 | 121.4656635599 | 31.1446204266 | 514 | 504990 | -78.22 | 15.53 | 376.18 | 0.13 | 2.02 | 1582 |
| 2024-09-20 22:21:34.572 | MS1 | 121.4656611653 | 31.1446180902 | 514 | 504990 | -92.77 | -2.81 | 66.41 | 0.05 | 1.45 | 1579 |
| 2024-09-20 22:21:35.775 | MS1 | 121.4656739333 | 31.1446284030 | 514 | 504990 | -94.12 | -1.37 | 53.88 | 0.01 | 1.23 | 1590 |
| 2024-09-20 22:21:36.517 | MS1 | 121.4656723819 | 31.1446328200 | 514 | 504990 | -91.05 | -3.33 | 54.45 | 0.16 | 1.44 | 1570 |
| 2024-09-20 22:21:37.726 | MS1 | 121.4656773684 | 31.1446236471 | 514 | 504990 | -88.51 | -3.34 | 56.17 | 0.10 | 1.45 | 1564 |
| 2024-09-20 22:21:38.909 | MS1 | 121.4656731270 | 31.1446287221 | 514 | 504990 | -84.02 | 17.53 | 466.30 | 0.12 | 1.20 | 1581 |
| 2024-09-20 22:21:39.692 | MS1 | 121.4656623262 | 31.1446236872 | 514 | 504990 | -83.27 | 12.14 | 557.46 | 0.13 | 1.41 | 1571 |
| 2024-09-20 22:21:40.470 | MS1 | 121.4656738915 | 31.1446361091 | 514 | 504990 | -80.23 | 12.41 | 570.62 | 0.15 | 2.50 | 1594 |
| 2024-09-20 22:21:41.528 | MS1 | 121.4656651821 | 31.1446312551 | 514 | 504990 | -78.94 | 13.01 | 485.62 | 0.11 | 2.47 | 1567 |
| 2024-09-20 22:21:42.615 | MS1 | 121.4656716246 | 31.1446340923 | 514 | 504990 | -76.93 | 14.27 | 328.01 | 0.09 | 2.10 | 1583 |

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
| 3245635 | 2 | 121.4710069027 | 31.1463775514 | 242 | 8 | 11 | 29.8 | TDD | 795 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3251379 | 3 | 121.4697880628 | 31.1539331271 | 140 | 11 | 8 | 42.8 | TDD | 932 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3271102 | 1 | 121.4686234665 | 31.1486355675 | 348 | 11 | 0 | 17.7 | TDD | 514 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3279703 | 4 | 121.4758050391 | 31.1528326113 | 235 | 2 | 10 | 48.9 | TDD | 796 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.361 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.383 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.521 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.521 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.231 | NREventA3 | measId:2;ServCellPCI:433;Se... |
| 2024-09-20 22:21:36.231 | NREventA3 | measId:2;ServCellPCI:433;Se... |
| 2024-09-20 22:21:37.231 | NREventA3 | measId:2;ServCellPCI:433;Se... |
| 2024-09-20 22:21:39.731 | NRRRCReestablishAttempt | PCI:433 |
| 2024-09-20 22:21:39.741 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.756 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.887 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.887 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271102 | 1 | 9.0904 | 18.5846 | -114.2463 | 10.5817 | 135.5941 | 0.0178 | 0.1034 |
| 2024_09_20 22:00 | 3245635 | 2 | 19.4624 | 7.3088 | -114.6991 | 18.8179 | 80.3255 | 0.0001 | 0.0129 |
| 2024_09_20 22:00 | 3251379 | 3 | 6.1794 | 8.1382 | -116.9680 | 16.0714 | 89.4332 | 0.0111 | 0.0041 |
| 2024_09_20 22:00 | 3279703 | 4 | 7.0615 | 19.8876 | -116.8834 | 13.9658 | 151.6849 | 0.0123 | 0.0038 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412808_9267B0D4 | 504990 | 514 | -92.9 | 504990 | 796 | -89.4 | 504990 | 932 | -91.9 | 504990 | 795 |
| MR_1774412808_9AA8E5BB | 504990 | 796 | -88.2 | 504990 | 514 | -92.0 | 504990 | 932 | -91.9 | 504990 | 795 |
| MR_1774412808_3EC08F2B | 504990 | 514 | -94.4 | 504990 | 796 | -86.7 | 504990 | 932 | -90.5 | 504990 | 795 |
| MR_1774412808_7AF029B7 | 504990 | 796 | -86.1 | 504990 | 514 | -92.4 | 504990 | 932 | -90.1 | 504990 | 795 |
| MR_1774412808_B983A5EE | 504990 | 514 | -91.1 | 504990 | 796 | -86.0 | 504990 | 932 | -91.4 | 504990 | 795 |

> *... 2개 열 생략 (전체 14열)*

---
