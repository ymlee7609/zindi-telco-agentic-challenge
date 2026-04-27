# Track A 문제 분석 — train[1890]~train[1899]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1890] ~ train[1899] (10개)

## 목차

1. [문제 1890: `898c6f88-51e...`](#1890) — multiple-answer, 정답: C1|C8|C13|C16
2. [문제 1891: `7a7fd799-3dc...`](#1891) — single-answer, 정답: C15
3. [문제 1892: `5a71b4cb-8a4...`](#1892) — single-answer, 정답: C16
4. [문제 1893: `6248ec03-bf9...`](#1893) — single-answer, 정답: C9
5. [문제 1894: `e179e18c-649...`](#1894) — multiple-answer, 정답: C17|C19
6. [문제 1895: `a979f52a-a52...`](#1895) — single-answer, 정답: C21
7. [문제 1896: `b67c5f9a-bb6...`](#1896) — single-answer, 정답: C6
8. [문제 1897: `c68d1486-ad4...`](#1897) — single-answer, 정답: C8
9. [문제 1898: `833825a6-ea9...`](#1898) — single-answer, 정답: C12
10. [문제 1899: `40d11965-818...`](#1899) — single-answer, 정답: C10

---

### 문제 1890: `898c6f88-51e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `898c6f88-51e5-424b-8b33-2fe06d60aa94` |
| Tag | **multiple-answer** |
| 정답 | **C1|C8|C13|C16** |
| C1 의미 | Increase A3 Offset threshold for 3218532_3 |
| C8 의미 | Press down the tilt angle  of 3225266_1 by 2 degrees |
| C13 의미 | Decrease transmission power for 3225266_1 |
| C16 의미 | Increase A3 Offset threshold for 3225266_1 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1890] topology](images/train_1890.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3218532_3 **← 정답**
- `C2`: Add neighbor relationship between 3218532_3 and 3225266_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225266_1
- `C4`: Add neighbor relationship between 3251741_5 and 3225266_1
- `C5`: Increase transmission power for 3218532_3
- `C6`: Lift the tilt angle  of 3225266_1 by 2 degrees
- `C7`: Adjust the azimuth of 3225266_1 by 14 degrees
- `C8`: Press down the tilt angle  of 3225266_1 by 2 degrees **← 정답**
- `C9`: Decrease A3 Offset threshold for 3218532_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225266_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218532_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218532_3
- `C13`: Decrease transmission power for 3225266_1 **← 정답**
- `C14`: Decrease transmission power for 3218532_3
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Increase A3 Offset threshold for 3225266_1 **← 정답**
- `C17`: Lift the tilt angle of 3218532_3 by 2 degrees
- `C18`: Check test server and transmission issues
- `C19`: Increase transmission power for 3225266_1
- `C20`: Adjust the azimuth of 3218532_3 by 9 degrees
- `C21`: Press down the tilt angle of 3218532_3 by 2 degrees
- `C22`: Decrease A3 Offset threshold for 3225266_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.273 | MS1 | 121.4656729292 | 31.1446343274 | 582 | 504990 | -77.44 | 12.95 | 445.83 | 0.11 | 2.78 | 1581 |
| 2024-09-20 22:21:32.435 | MS1 | 121.4656600452 | 31.1446343258 | 582 | 504990 | -78.54 | 16.51 | 500.84 | 0.14 | 2.80 | 1592 |
| 2024-09-20 22:21:33.883 | MS1 | 121.4656744843 | 31.1446299487 | 582 | 504990 | -76.50 | 14.78 | 478.92 | 0.05 | 2.62 | 1577 |
| 2024-09-20 22:21:34.893 | MS1 | 121.4656759814 | 31.1446285924 | 707 | 504990 | -87.88 | 1.45 | 86.12 | 0.04 | 1.43 | 1592 |
| 2024-09-20 22:21:35.923 | MS1 | 121.4656618681 | 31.1446244836 | 707 | 504990 | -85.81 | 3.39 | 69.31 | 0.10 | 1.35 | 1574 |
| 2024-09-20 22:21:36.130 | MS1 | 121.4656770218 | 31.1446249530 | 582 | 504990 | -84.86 | 3.84 | 31.87 | 0.15 | 1.42 | 1587 |
| 2024-09-20 22:21:37.212 | MS1 | 121.4656761094 | 31.1446358420 | 582 | 504990 | -85.02 | 3.81 | 34.81 | 0.17 | 1.45 | 1583 |
| 2024-09-20 22:21:38.647 | MS1 | 121.4656637802 | 31.1446199250 | 707 | 504990 | -80.79 | 4.73 | 60.84 | 0.11 | 1.14 | 1571 |
| 2024-09-20 22:21:39.819 | MS1 | 121.4656682320 | 31.1446290235 | 707 | 504990 | -85.99 | 2.62 | 78.92 | 0.05 | 1.46 | 1578 |
| 2024-09-20 22:21:40.824 | MS1 | 121.4656635968 | 31.1446295431 | 707 | 504990 | -83.64 | 16.44 | 435.39 | 0.00 | 2.88 | 1579 |
| 2024-09-20 22:21:41.187 | MS1 | 121.4656719732 | 31.1446359278 | 707 | 504990 | -77.07 | 15.38 | 330.42 | 0.12 | 2.88 | 1588 |
| 2024-09-20 22:21:42.526 | MS1 | 121.4656683318 | 31.1446223178 | 707 | 504990 | -79.35 | 16.72 | 486.45 | 0.01 | 2.05 | 1588 |

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
| 3218532 | 3 | 121.4670025742 | 31.1555781632 | 177 | 1 | 6 | 26.7 | TDD | 582 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3225266 | 1 | 121.4697659805 | 31.1548965721 | 213 | 1 | 9 | 31.5 | TDD | 641 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3242995 | 4 | 121.4748988640 | 31.1465982606 | 270 | 4 | 8 | 48.4 | TDD | 872 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3251741 | 5 | 121.4715348371 | 31.1536686720 | 49 | 3 | 9 | 21.1 | TDD | 735 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3259080 | 2 | 121.4675807930 | 31.1516636788 | 44 | 9 | 0 | 20.4 | TDD | 707 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.157 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.179 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.306 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.306 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.007 | NREventA3 | measId:2;ServCellPCI:113;Se... |
| 2024-09-20 22:21:34.247 | NRHandoverAttempt | SourcePCI:113;SourceNR-ARFC... |
| 2024-09-20 22:21:34.279 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.289 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:34.438 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.438 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.007 | NREventA3 | measId:2;ServCellPCI:28;Ser... |
| 2024-09-20 22:21:36.247 | NRHandoverAttempt | SourcePCI:28;SourceNR-ARFCN... |
| 2024-09-20 22:21:36.278 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.291 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.427 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.427 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.007 | NREventA3 | measId:2;ServCellPCI:113;Se... |
| 2024-09-20 22:21:38.247 | NRHandoverAttempt | SourcePCI:113;SourceNR-ARFC... |
| 2024-09-20 22:21:38.286 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.298 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.429 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.429 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225266 | 1 | 18.3557 | 16.5870 | -115.6177 | 15.6804 | 151.5336 | 0.0149 | 0.0173 |
| 2024_09_20 22:00 | 3259080 | 2 | 19.1214 | 5.5688 | -116.2262 | 9.0645 | 115.7860 | 0.0182 | 0.0200 |
| 2024_09_20 22:00 | 3218532 | 3 | 19.4168 | 9.0176 | -114.1254 | 12.4466 | 128.2516 | 0.0090 | 0.0123 |
| 2024_09_20 22:00 | 3242995 | 4 | 18.5318 | 10.4340 | -114.6439 | 14.4983 | 190.2675 | 0.0075 | 0.0071 |
| 2024_09_20 22:00 | 3251741 | 5 | 10.1195 | 16.2969 | -115.7072 | 18.0736 | 138.0747 | 0.0085 | 0.0017 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412962_6E0FB22A | 504990 | 707 | -89.7 | 504990 | 582 | -87.0 | 504990 | 641 | -87.9 | 504990 | 735 |
| MR_1774412962_CF24C621 | 504990 | 582 | -89.7 | 504990 | 707 | -87.1 | 504990 | 641 | -86.4 | 504990 | 735 |
| MR_1774412962_03F5F49A | 504990 | 707 | -89.1 | 504990 | 582 | -84.0 | 504990 | 641 | -88.5 | 504990 | 735 |
| MR_1774412962_6DDA0C06 | 504990 | 707 | -86.8 | 504990 | 582 | -86.1 | 504990 | 641 | -87.3 | 504990 | 735 |
| MR_1774412962_44FA44DA | 504990 | 707 | -88.2 | 504990 | 582 | -86.3 | 504990 | 641 | -87.8 | 504990 | 735 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1891: `7a7fd799-3dc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7a7fd799-3dcd-4368-9cf4-8c622d6339e2` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease A3 Offset threshold for 3244458_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1891] topology](images/train_1891.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244458_1
- `C2`: Press down the tilt angle  of 3216884_4 by 7 degrees
- `C3`: Increase transmission power for 3216884_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244458_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease A3 Offset threshold for 3216884_4
- `C7`: Increase transmission power for 3244458_1
- `C8`: Decrease transmission power for 3244458_1
- `C9`: Add neighbor relationship between 3244458_1 and 3216884_4
- `C10`: Increase A3 Offset threshold for 3216884_4
- `C11`: Press down the tilt angle of 3244458_1 by 5 degrees
- `C12`: Increase A3 Offset threshold for 3244458_1
- `C13`: Decrease transmission power for 3216884_4
- `C14`: Adjust the azimuth of 3216884_4 by 50 degrees
- `C15`: Decrease A3 Offset threshold for 3244458_1 **← 정답**
- `C16`: Lift the tilt angle of 3244458_1 by 5 degrees
- `C17`: Lift the tilt angle  of 3216884_4 by 7 degrees
- `C18`: Check test server and transmission issues
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216884_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216884_4
- `C21`: Add neighbor relationship between 3255954_2 and 3216884_4
- `C22`: Adjust the azimuth of 3244458_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.857 | MS1 | 121.4656625732 | 31.1446210694 | 418 | 504990 | -77.56 | 17.54 | 329.96 | 0.14 | 2.12 | 1590 |
| 2024-09-20 22:21:32.690 | MS1 | 121.4656733626 | 31.1446192523 | 418 | 504990 | -82.56 | 12.00 | 485.78 | 0.10 | 2.62 | 1586 |
| 2024-09-20 22:21:33.803 | MS1 | 121.4656625679 | 31.1446342283 | 418 | 504990 | -81.62 | 17.39 | 598.05 | 0.02 | 2.73 | 1576 |
| 2024-09-20 22:21:34.222 | MS1 | 121.4656745917 | 31.1446289252 | 418 | 504990 | -85.55 | -3.76 | 58.97 | 0.05 | 1.47 | 1568 |
| 2024-09-20 22:21:35.407 | MS1 | 121.4656590888 | 31.1446361460 | 418 | 504990 | -91.83 | -3.94 | 48.86 | 0.02 | 1.26 | 1586 |
| 2024-09-20 22:21:36.270 | MS1 | 121.4656631287 | 31.1446348933 | 418 | 504990 | -92.11 | -1.28 | 74.42 | 0.01 | 1.32 | 1577 |
| 2024-09-20 22:21:37.409 | MS1 | 121.4656725584 | 31.1446180078 | 418 | 504990 | -83.23 | -2.21 | 41.70 | 0.01 | 1.15 | 1568 |
| 2024-09-20 22:21:38.250 | MS1 | 121.4656648733 | 31.1446295980 | 418 | 504990 | -88.86 | -0.50 | 57.28 | 0.04 | 1.03 | 1591 |
| 2024-09-20 22:21:39.365 | MS1 | 121.4656778128 | 31.1446303554 | 619 | 504990 | -77.75 | 13.89 | 239.91 | 0.15 | 1.36 | 1598 |
| 2024-09-20 22:21:40.560 | MS1 | 121.4656623280 | 31.1446275790 | 619 | 504990 | -76.18 | 16.86 | 326.63 | 0.04 | 2.89 | 1576 |
| 2024-09-20 22:21:41.561 | MS1 | 121.4656763296 | 31.1446216079 | 619 | 504990 | -79.17 | 15.46 | 515.21 | 0.10 | 2.58 | 1593 |
| 2024-09-20 22:21:42.468 | MS1 | 121.4656685576 | 31.1446324686 | 619 | 504990 | -75.42 | 16.94 | 430.49 | 0.13 | 2.59 | 1597 |

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
| 3216884 | 4 | 121.4671304709 | 31.1480004379 | 74 | 0 | 9 | 46.9 | TDD | 619 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3242867 | 3 | 121.4742854412 | 31.1557863408 | 74 | 7 | 9 | 26.0 | TDD | 674 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3244458 | 1 | 121.4651571336 | 31.1479679240 | 286 | 0 | 1 | 30.8 | TDD | 418 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3255954 | 2 | 121.4708126728 | 31.1466019915 | 131 | 4 | 7 | 45.2 | TDD | 953 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.173 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.197 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.336 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.336 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.013 | NREventA3 | measId:2;ServCellPCI:837;Se... |
| 2024-09-20 22:21:38.253 | NRHandoverAttempt | SourcePCI:837;SourceNR-ARFC... |
| 2024-09-20 22:21:38.287 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.300 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.411 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.411 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244458 | 1 | 16.3133 | 15.1835 | -114.7568 | 16.4618 | 111.3142 | 0.0064 | 0.1853 |
| 2024_09_20 22:00 | 3255954 | 2 | 15.1802 | 7.9927 | -115.6744 | 13.6800 | 88.4564 | 0.0188 | 0.0141 |
| 2024_09_20 22:00 | 3242867 | 3 | 6.9141 | 14.8550 | -114.4101 | 15.9013 | 173.8592 | 0.0150 | 0.0105 |
| 2024_09_20 22:00 | 3216884 | 4 | 8.2260 | 9.1237 | -114.3472 | 15.8170 | 129.1576 | 0.0177 | 0.0031 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412046_16F11190 | 504990 | 418 | -84.0 | 504990 | 619 | -78.5 | 504990 | 953 | -81.3 | 504990 | 674 |
| MR_1774412046_E6121175 | 504990 | 418 | -86.4 | 504990 | 619 | -78.6 | 504990 | 953 | -81.0 | 504990 | 674 |
| MR_1774412046_21F0EFE4 | 504990 | 619 | -80.4 | 504990 | 418 | -87.4 | 504990 | 953 | -82.4 | 504990 | 674 |
| MR_1774412046_703CA23D | 504990 | 619 | -80.0 | 504990 | 418 | -85.7 | 504990 | 953 | -80.4 | 504990 | 674 |
| MR_1774412046_DC9F3293 | 504990 | 619 | -78.9 | 504990 | 418 | -87.2 | 504990 | 953 | -81.7 | 504990 | 674 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1892: `5a71b4cb-8a4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5a71b4cb-8a4d-49f5-84fa-927a587f589a` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Add neighbor relationship between 3250235_4 and 3259150_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1892] topology](images/train_1892.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3234078_3 and 3259150_1
- `C2`: Increase A3 Offset threshold for 3259150_1
- `C3`: Adjust the azimuth of 3259150_1 by 37 degrees
- `C4`: Decrease A3 Offset threshold for 3259150_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259150_1
- `C7`: Adjust the azimuth of 3250235_4 by 50 degrees
- `C8`: Increase transmission power for 3250235_4
- `C9`: Lift the tilt angle  of 3259150_1 by 3 degrees
- `C10`: Lift the tilt angle of 3250235_4 by 10 degrees
- `C11`: Increase transmission power for 3259150_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250235_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250235_4
- `C14`: Decrease transmission power for 3259150_1
- `C15`: Decrease transmission power for 3250235_4
- `C16`: Add neighbor relationship between 3250235_4 and 3259150_1 **← 정답**
- `C17`: Check test server and transmission issues
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259150_1
- `C19`: Increase A3 Offset threshold for 3250235_4
- `C20`: Press down the tilt angle of 3250235_4 by 10 degrees
- `C21`: Decrease A3 Offset threshold for 3250235_4
- `C22`: Press down the tilt angle  of 3259150_1 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.521 | MS1 | 121.4656699281 | 31.1446198086 | 655 | 504990 | -77.33 | 14.56 | 540.43 | 0.14 | 2.74 | 1564 |
| 2024-09-20 22:21:32.132 | MS1 | 121.4656694198 | 31.1446351543 | 655 | 504990 | -77.45 | 13.30 | 471.47 | 0.13 | 2.04 | 1568 |
| 2024-09-20 22:21:33.171 | MS1 | 121.4656741611 | 31.1446332018 | 655 | 504990 | -80.82 | 15.14 | 445.35 | 0.20 | 2.65 | 1564 |
| 2024-09-20 22:21:34.204 | MS1 | 121.4656702918 | 31.1446364261 | 655 | 504990 | -90.20 | -3.30 | 51.36 | 0.04 | 1.02 | 1577 |
| 2024-09-20 22:21:35.663 | MS1 | 121.4656722042 | 31.1446199791 | 655 | 504990 | -88.86 | -3.19 | 37.59 | 0.05 | 1.32 | 1563 |
| 2024-09-20 22:21:36.116 | MS1 | 121.4656778861 | 31.1446274229 | 655 | 504990 | -89.02 | -3.02 | 74.39 | 0.12 | 1.24 | 1563 |
| 2024-09-20 22:21:37.916 | MS1 | 121.4656648763 | 31.1446263529 | 655 | 504990 | -87.81 | -3.74 | 62.13 | 0.07 | 1.18 | 1560 |
| 2024-09-20 22:21:38.683 | MS1 | 121.4656588107 | 31.1446355088 | 655 | 504990 | -83.07 | 15.93 | 544.37 | 0.06 | 1.22 | 1566 |
| 2024-09-20 22:21:39.489 | MS1 | 121.4656580778 | 31.1446375009 | 655 | 504990 | -76.03 | 12.49 | 532.45 | 0.18 | 1.13 | 1590 |
| 2024-09-20 22:21:40.882 | MS1 | 121.4656769063 | 31.1446352141 | 655 | 504990 | -81.34 | 16.66 | 577.65 | 0.13 | 2.07 | 1581 |
| 2024-09-20 22:21:41.636 | MS1 | 121.4656584641 | 31.1446222460 | 655 | 504990 | -77.04 | 16.94 | 568.15 | 0.13 | 2.34 | 1562 |
| 2024-09-20 22:21:42.925 | MS1 | 121.4656714312 | 31.1446243928 | 655 | 504990 | -77.68 | 13.16 | 539.85 | 0.11 | 2.34 | 1580 |

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
| 3234078 | 3 | 121.4720478510 | 31.1456078384 | 91 | 12 | 10 | 28.4 | TDD | 261 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3240986 | 2 | 121.4643181075 | 31.1527707587 | 163 | 12 | 9 | 45.7 | TDD | 433 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3250235 | 4 | 121.4720543153 | 31.1508994510 | 279 | 14 | 0 | 22.2 | TDD | 655 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3259150 | 1 | 121.4709035409 | 31.1521606385 | 174 | 2 | 3 | 22.2 | TDD | 593 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.053 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.074 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.204 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.204 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.950 | NREventA3 | measId:2;ServCellPCI:747;Se... |
| 2024-09-20 22:21:35.950 | NREventA3 | measId:2;ServCellPCI:747;Se... |
| 2024-09-20 22:21:36.950 | NREventA3 | measId:2;ServCellPCI:747;Se... |
| 2024-09-20 22:21:39.450 | NRRRCReestablishAttempt | PCI:747 |
| 2024-09-20 22:21:39.464 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.478 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.598 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.598 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259150 | 1 | 5.4171 | 13.9165 | -115.4722 | 18.1306 | 85.1222 | 0.0028 | 0.0017 |
| 2024_09_20 22:00 | 3240986 | 2 | 15.7348 | 17.9217 | -117.4779 | 5.9304 | 117.0619 | 0.0040 | 0.0009 |
| 2024_09_20 22:00 | 3234078 | 3 | 12.1732 | 12.6283 | -115.3188 | 14.3788 | 197.9202 | 0.0187 | 0.0069 |
| 2024_09_20 22:00 | 3250235 | 4 | 7.3760 | 6.5375 | -117.9040 | 7.0588 | 196.2529 | 0.0181 | 0.1952 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416626_76393262 | 504990 | 655 | -91.7 | 504990 | 593 | -83.2 | 504990 | 261 | -85.7 | 504990 | 433 |
| MR_1774416626_64DD834E | 504990 | 655 | -90.1 | 504990 | 593 | -83.1 | 504990 | 261 | -86.7 | 504990 | 433 |
| MR_1774416626_596EBCC2 | 504990 | 655 | -88.7 | 504990 | 593 | -86.6 | 504990 | 261 | -87.8 | 504990 | 433 |
| MR_1774416626_7A3A8136 | 504990 | 593 | -84.2 | 504990 | 655 | -90.7 | 504990 | 261 | -87.1 | 504990 | 433 |
| MR_1774416626_4D821FC4 | 504990 | 655 | -89.8 | 504990 | 593 | -85.3 | 504990 | 261 | -87.9 | 504990 | 433 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1893: `6248ec03-bf9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6248ec03-bf97-4a0a-9995-22a93e471d7c` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Add neighbor relationship between 3222968_4 and 3216244_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1893] topology](images/train_1893.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3222968_4 by 5 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216244_1
- `C3`: Press down the tilt angle  of 3216244_1 by 2 degrees
- `C4`: Check test server and transmission issues
- `C5`: Decrease transmission power for 3216244_1
- `C6`: Adjust the azimuth of 3216244_1 by 13 degrees
- `C7`: Decrease transmission power for 3222968_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222968_4
- `C9`: Add neighbor relationship between 3222968_4 and 3216244_1 **← 정답**
- `C10`: Increase transmission power for 3222968_4
- `C11`: Increase A3 Offset threshold for 3222968_4
- `C12`: Adjust the azimuth of 3222968_4 by 50 degrees
- `C13`: Increase A3 Offset threshold for 3216244_1
- `C14`: Decrease A3 Offset threshold for 3216244_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216244_1
- `C17`: Add neighbor relationship between 3242388_2 and 3216244_1
- `C18`: Increase transmission power for 3216244_1
- `C19`: Lift the tilt angle  of 3216244_1 by 2 degrees
- `C20`: Press down the tilt angle of 3222968_4 by 5 degrees
- `C21`: Decrease A3 Offset threshold for 3222968_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222968_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.714 | MS1 | 121.4656606682 | 31.1446218168 | 279 | 504990 | -79.55 | 14.71 | 314.95 | 0.19 | 2.31 | 1586 |
| 2024-09-20 22:21:32.635 | MS1 | 121.4656647590 | 31.1446225796 | 279 | 504990 | -82.97 | 13.36 | 403.37 | 0.08 | 2.93 | 1587 |
| 2024-09-20 22:21:33.970 | MS1 | 121.4656586871 | 31.1446369610 | 279 | 504990 | -82.78 | 12.07 | 549.83 | 0.03 | 2.43 | 1600 |
| 2024-09-20 22:21:34.649 | MS1 | 121.4656726774 | 31.1446193168 | 279 | 504990 | -86.61 | -2.34 | 64.07 | 0.06 | 1.21 | 1595 |
| 2024-09-20 22:21:35.289 | MS1 | 121.4656604006 | 31.1446235664 | 279 | 504990 | -90.51 | -0.08 | 24.31 | 0.10 | 1.14 | 1560 |
| 2024-09-20 22:21:36.386 | MS1 | 121.4656734132 | 31.1446267954 | 279 | 504990 | -94.50 | -0.26 | 56.95 | 0.09 | 1.39 | 1589 |
| 2024-09-20 22:21:37.918 | MS1 | 121.4656666941 | 31.1446356261 | 279 | 504990 | -85.78 | -0.06 | 54.11 | 0.20 | 1.02 | 1561 |
| 2024-09-20 22:21:38.568 | MS1 | 121.4656758229 | 31.1446307394 | 279 | 504990 | -75.33 | 12.62 | 524.71 | 0.03 | 1.13 | 1570 |
| 2024-09-20 22:21:39.883 | MS1 | 121.4656583340 | 31.1446250532 | 279 | 504990 | -75.24 | 17.55 | 596.30 | 0.16 | 1.36 | 1587 |
| 2024-09-20 22:21:40.795 | MS1 | 121.4656732507 | 31.1446237424 | 279 | 504990 | -76.46 | 12.31 | 553.73 | 0.04 | 2.97 | 1577 |
| 2024-09-20 22:21:41.615 | MS1 | 121.4656648544 | 31.1446259658 | 279 | 504990 | -84.61 | 12.49 | 510.10 | 0.01 | 2.15 | 1570 |
| 2024-09-20 22:21:42.315 | MS1 | 121.4656725608 | 31.1446291695 | 279 | 504990 | -75.29 | 16.04 | 362.84 | 0.20 | 2.70 | 1591 |

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
| 3216244 | 1 | 121.4707017710 | 31.1496178878 | 234 | 0 | 1 | 21.2 | TDD | 202 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3220140 | 3 | 121.4748988999 | 31.1453480260 | 61 | 7 | 3 | 44.5 | TDD | 725 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3222968 | 4 | 121.4689584558 | 31.1525275865 | 85 | 2 | 11 | 42.5 | TDD | 279 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3242388 | 2 | 121.4721264224 | 31.1534926416 | 90 | 2 | 12 | 29.5 | TDD | 164 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.274 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.299 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.414 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.414 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.139 | NREventA3 | measId:2;ServCellPCI:314;Se... |
| 2024-09-20 22:21:36.139 | NREventA3 | measId:2;ServCellPCI:314;Se... |
| 2024-09-20 22:21:37.139 | NREventA3 | measId:2;ServCellPCI:314;Se... |
| 2024-09-20 22:21:39.639 | NRRRCReestablishAttempt | PCI:314 |
| 2024-09-20 22:21:39.653 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.666 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.793 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.793 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216244 | 1 | 10.8154 | 11.4794 | -115.2641 | 13.1812 | 182.0976 | 0.0055 | 0.0149 |
| 2024_09_20 22:00 | 3242388 | 2 | 17.0889 | 9.2092 | -115.1045 | 11.8560 | 149.3442 | 0.0085 | 0.0122 |
| 2024_09_20 22:00 | 3220140 | 3 | 9.4654 | 18.5580 | -115.3906 | 13.7578 | 124.8977 | 0.0045 | 0.0146 |
| 2024_09_20 22:00 | 3222968 | 4 | 10.3467 | 5.5817 | -117.7334 | 19.6970 | 91.9353 | 0.0174 | 0.1763 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414764_B31E9C47 | 504990 | 202 | -84.6 | 504990 | 279 | -87.6 | 504990 | 164 | -87.5 | 504990 | 725 |
| MR_1774414764_1CF54099 | 504990 | 202 | -83.8 | 504990 | 279 | -86.4 | 504990 | 164 | -83.8 | 504990 | 725 |
| MR_1774414764_6A389A80 | 504990 | 202 | -82.0 | 504990 | 279 | -86.8 | 504990 | 164 | -86.0 | 504990 | 725 |
| MR_1774414764_4CEAB897 | 504990 | 202 | -83.8 | 504990 | 279 | -85.2 | 504990 | 164 | -86.0 | 504990 | 725 |
| MR_1774414764_7A546496 | 504990 | 279 | -87.8 | 504990 | 202 | -81.1 | 504990 | 164 | -85.6 | 504990 | 725 |
| MR_1774414764_F422C79E | 504990 | 279 | -85.3 | 504990 | 202 | -81.8 | 504990 | 164 | -84.7 | 504990 | 725 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1894: `e179e18c-649...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e179e18c-6490-4b61-868f-960fdfbdd1eb` |
| Tag | **multiple-answer** |
| 정답 | **C17|C19** |
| C17 의미 | Decrease transmission power for 3228957_1 |
| C19 의미 | Press down the tilt angle  of 3228957_1 by 3 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1894] topology](images/train_1894.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3228957_1 by 21 degrees
- `C2`: Decrease A3 Offset threshold for 3222093_4
- `C3`: Lift the tilt angle  of 3228957_1 by 3 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228957_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228957_1
- `C7`: Increase A3 Offset threshold for 3228957_1
- `C8`: Decrease transmission power for 3222093_4
- `C9`: Increase A3 Offset threshold for 3222093_4
- `C10`: Decrease A3 Offset threshold for 3228957_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222093_4
- `C12`: Increase transmission power for 3228957_1
- `C13`: Lift the tilt angle of 3222093_4 by 5 degrees
- `C14`: Adjust the azimuth of 3222093_4 by 45 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222093_4
- `C16`: Add neighbor relationship between 3222093_4 and 3228957_1
- `C17`: Decrease transmission power for 3228957_1 **← 정답**
- `C18`: Check test server and transmission issues
- `C19`: Press down the tilt angle  of 3228957_1 by 3 degrees **← 정답**
- `C20`: Add neighbor relationship between 3255664_3 and 3228957_1
- `C21`: Increase transmission power for 3222093_4
- `C22`: Press down the tilt angle of 3222093_4 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.219 | MS1 | 121.4656606927 | 31.1446181133 | 398 | 504990 | -81.98 | 17.91 | 559.02 | 0.09 | 2.37 | 1586 |
| 2024-09-20 22:21:32.582 | MS1 | 121.4656657510 | 31.1446184855 | 398 | 504990 | -80.80 | 14.21 | 332.99 | 0.05 | 2.97 | 1569 |
| 2024-09-20 22:21:33.616 | MS1 | 121.4656608982 | 31.1446358870 | 398 | 504990 | -84.63 | 12.83 | 438.95 | 0.02 | 2.52 | 1594 |
| 2024-09-20 22:21:34.390 | MS1 | 121.4656746297 | 31.1446287443 | 398 | 504990 | -87.15 | 1.75 | 72.31 | 0.12 | 1.32 | 1595 |
| 2024-09-20 22:21:35.172 | MS1 | 121.4656669632 | 31.1446269538 | 398 | 504990 | -91.57 | 0.97 | 36.83 | 0.11 | 1.06 | 1575 |
| 2024-09-20 22:21:36.543 | MS1 | 121.4656752042 | 31.1446374860 | 398 | 504990 | -88.10 | 0.69 | 67.61 | 0.13 | 1.41 | 1566 |
| 2024-09-20 22:21:37.597 | MS1 | 121.4656605293 | 31.1446333690 | 398 | 504990 | -92.82 | 0.04 | 67.10 | 0.06 | 1.02 | 1596 |
| 2024-09-20 22:21:38.576 | MS1 | 121.4656580299 | 31.1446257226 | 398 | 504990 | -85.72 | 2.37 | 58.25 | 0.15 | 1.14 | 1580 |
| 2024-09-20 22:21:39.386 | MS1 | 121.4656633776 | 31.1446260057 | 398 | 504990 | -86.78 | 0.31 | 89.06 | 0.02 | 1.11 | 1562 |
| 2024-09-20 22:21:40.153 | MS1 | 121.4656647302 | 31.1446182019 | 398 | 504990 | -78.50 | 17.45 | 358.59 | 0.12 | 2.18 | 1577 |
| 2024-09-20 22:21:41.428 | MS1 | 121.4656748113 | 31.1446329774 | 398 | 504990 | -79.99 | 17.15 | 506.20 | 0.18 | 2.36 | 1596 |
| 2024-09-20 22:21:42.485 | MS1 | 121.4656624642 | 31.1446367677 | 398 | 504990 | -78.42 | 12.13 | 526.00 | 0.17 | 2.11 | 1571 |

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
| 3222093 | 4 | 121.4753476580 | 31.1483152808 | 201 | 4 | 4 | 26.1 | TDD | 398 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3228957 | 1 | 121.4750766523 | 31.1445749289 | 249 | 0 | 11 | 40.1 | TDD | 448 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3242698 | 2 | 121.4708938518 | 31.1452344793 | 356 | 5 | 6 | 35.2 | TDD | 921 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3255664 | 3 | 121.4696891014 | 31.1532202498 | 155 | 4 | 3 | 23.2 | TDD | 824 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.242 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.264 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.398 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.398 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228957 | 1 | 12.2210 | 12.1179 | -116.8752 | 15.2505 | 152.9046 | 0.0040 | 0.0187 |
| 2024_09_20 22:00 | 3242698 | 2 | 16.5485 | 6.0419 | -115.0530 | 5.7138 | 119.8766 | 0.0050 | 0.0099 |
| 2024_09_20 22:00 | 3255664 | 3 | 11.6794 | 13.9232 | -116.4416 | 6.0978 | 192.7848 | 0.0121 | 0.0034 |
| 2024_09_20 22:00 | 3222093 | 4 | 6.5605 | 11.5138 | -109.2246 | 5.5529 | 83.6365 | 0.0035 | 0.0101 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413933_2601D69B | 504990 | 448 | -87.7 | 504990 | 398 | -88.3 | 504990 | 824 | -88.1 | 504990 | 921 |
| MR_1774413933_1E8FB787 | 504990 | 398 | -86.0 | 504990 | 448 | -86.5 | 504990 | 824 | -88.5 | 504990 | 921 |
| MR_1774413933_5F1BB0D1 | 504990 | 448 | -87.3 | 504990 | 398 | -86.7 | 504990 | 824 | -87.8 | 504990 | 921 |
| MR_1774413933_7F20D777 | 504990 | 398 | -87.2 | 504990 | 448 | -87.5 | 504990 | 824 | -88.8 | 504990 | 921 |
| MR_1774413933_87E06D46 | 504990 | 398 | -89.0 | 504990 | 448 | -84.9 | 504990 | 824 | -88.6 | 504990 | 921 |
| MR_1774413933_295B5C57 | 504990 | 448 | -86.0 | 504990 | 398 | -86.9 | 504990 | 824 | -87.7 | 504990 | 921 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1895: `a979f52a-a52...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a979f52a-a52a-42d9-9be3-2358e4fafbcb` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1895] topology](images/train_1895.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244186_4
- `C2`: Adjust the azimuth of 3269988_2 by 50 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269988_2
- `C4`: Increase transmission power for 3244186_4
- `C5`: Press down the tilt angle of 3244186_4 by 10 degrees
- `C6`: Increase A3 Offset threshold for 3269988_2
- `C7`: Check test server and transmission issues
- `C8`: Add neighbor relationship between 3226359_3 and 3269988_2
- `C9`: Increase A3 Offset threshold for 3244186_4
- `C10`: Increase transmission power for 3269988_2
- `C11`: Decrease transmission power for 3269988_2
- `C12`: Decrease A3 Offset threshold for 3244186_4
- `C13`: Lift the tilt angle of 3244186_4 by 10 degrees
- `C14`: Adjust the azimuth of 3244186_4 by 50 degrees
- `C15`: Press down the tilt angle  of 3269988_2 by 3 degrees
- `C16`: Decrease A3 Offset threshold for 3269988_2
- `C17`: Add neighbor relationship between 3244186_4 and 3269988_2
- `C18`: Decrease transmission power for 3244186_4
- `C19`: Lift the tilt angle  of 3269988_2 by 3 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244186_4
- `C21`: Insufficient data; more data is needed for judgment. **← 정답**
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269988_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.984 | MS1 | 121.4656585852 | 31.1446237511 | 703 | 504990 | -86.30 | 16.00 | 582.58 | 0.14 | 2.36 | 1599 |
| 2024-09-20 22:21:32.378 | MS1 | 121.4656580525 | 31.1446328069 | 703 | 504990 | -91.61 | 16.23 | 550.80 | 0.09 | 2.99 | 1565 |
| 2024-09-20 22:21:33.367 | MS1 | 121.4656594756 | 31.1446232125 | 703 | 504990 | -88.95 | 16.26 | 325.57 | 0.18 | 2.49 | 1588 |
| 2024-09-20 22:21:34.429 | MS1 | 121.4656696307 | 31.1446321133 | 703 | 504990 | -90.67 | 13.98 | 67.80 | 0.07 | 2.14 | 1599 |
| 2024-09-20 22:21:35.555 | MS1 | 121.4656727574 | 31.1446286771 | 703 | 504990 | -85.27 | 13.07 | 74.36 | 0.19 | 2.47 | 1565 |
| 2024-09-20 22:21:36.614 | MS1 | 121.4656687650 | 31.1446288436 | 703 | 504990 | -87.51 | 17.40 | 95.80 | 0.02 | 2.79 | 1570 |
| 2024-09-20 22:21:37.579 | MS1 | 121.4656711547 | 31.1446199344 | 703 | 504990 | -91.85 | 7.95 | 91.91 | 0.04 | 2.29 | 1599 |
| 2024-09-20 22:21:38.397 | MS1 | 121.4656624492 | 31.1446344526 | 703 | 504990 | -92.31 | 10.09 | 61.32 | 0.15 | 2.77 | 1562 |
| 2024-09-20 22:21:39.838 | MS1 | 121.4656741616 | 31.1446201858 | 703 | 504990 | -90.81 | 8.42 | 86.79 | 0.15 | 2.27 | 1568 |
| 2024-09-20 22:21:40.898 | MS1 | 121.4656640754 | 31.1446373350 | 703 | 504990 | -91.46 | 11.82 | 586.21 | 0.16 | 2.86 | 1597 |
| 2024-09-20 22:21:41.179 | MS1 | 121.4656686905 | 31.1446331242 | 703 | 504990 | -89.10 | 10.18 | 589.21 | 0.20 | 2.32 | 1562 |
| 2024-09-20 22:21:42.537 | MS1 | 121.4656681840 | 31.1446219184 | 703 | 504990 | -89.76 | 9.51 | 317.58 | 0.08 | 2.69 | 1587 |

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
| 3226359 | 3 | 121.4671636340 | 31.1517139860 | 263 | 4 | 4 | 44.4 | TDD | 972 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3244186 | 4 | 121.4685247494 | 31.1488673347 | 314 | 9 | 5 | 37.1 | TDD | 703 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3244734 | 1 | 121.4704057185 | 31.1543767390 | 161 | 13 | 11 | 16.2 | TDD | 122 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3269988 | 2 | 121.4735155241 | 31.1523747926 | 68 | 1 | 11 | 47.7 | TDD | 299 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.185 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.204 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.328 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.328 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.060 | NREventA3 | measId:2;ServCellPCI:181;Se... |
| 2024-09-20 22:21:38.300 | NRHandoverAttempt | SourcePCI:181;SourceNR-ARFC... |
| 2024-09-20 22:21:38.347 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.359 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.487 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.487 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3244734 | 1 | 89.5149 | 89.4301 | -114.6565 | 9.2048 | 143.4203 | 0.0027 | 0.0192 |
| 2024_09_19 22:00 | 3269988 | 2 | 82.0841 | 92.7641 | -115.5249 | 16.6257 | 104.9152 | 0.0049 | 0.0182 |
| 2024_09_19 22:00 | 3226359 | 3 | 92.9099 | 90.2078 | -115.9395 | 17.6406 | 196.9664 | 0.0148 | 0.0082 |
| 2024_09_19 22:00 | 3244186 | 4 | 82.4450 | 84.5289 | -116.0032 | 10.2523 | 195.2253 | 0.0180 | 0.0076 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413805_F607467F | 504990 | 703 | -91.7 | 504990 | 299 | -95.6 | 504990 | 972 | -102.8 | 504990 | 122 |
| MR_1774413805_FBAAA68B | 504990 | 703 | -89.8 | 504990 | 299 | -93.5 | 504990 | 972 | -103.3 | 504990 | 122 |
| MR_1774413805_F4E7250F | 504990 | 703 | -88.9 | 504990 | 299 | -91.9 | 504990 | 972 | -105.2 | 504990 | 122 |
| MR_1774413805_CA3563DD | 504990 | 703 | -90.4 | 504990 | 299 | -92.6 | 504990 | 972 | -104.8 | 504990 | 122 |
| MR_1774413805_E5A9C4FF | 504990 | 703 | -90.2 | 504990 | 299 | -92.4 | 504990 | 972 | -102.2 | 504990 | 122 |
| MR_1774413805_33E78A29 | 504990 | 703 | -91.1 | 504990 | 299 | -92.1 | 504990 | 972 | -105.4 | 504990 | 122 |
| MR_1774413805_8D7CA8FB | 504990 | 703 | -91.5 | 504990 | 299 | -92.8 | 504990 | 972 | -103.7 | 504990 | 122 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1896: `b67c5f9a-bb6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b67c5f9a-bb6c-45e9-9273-ede7a8a697a8` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3272674_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1896] topology](images/train_1896.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3230197_3
- `C2`: Add neighbor relationship between 3221945_4 and 3230197_3
- `C3`: Adjust the azimuth of 3230197_3 by 50 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230197_3
- `C5`: Check test server and transmission issues
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272674_2 **← 정답**
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272674_2
- `C8`: Increase A3 Offset threshold for 3230197_3
- `C9`: Add neighbor relationship between 3272674_2 and 3230197_3
- `C10`: Press down the tilt angle of 3272674_2 by 5 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230197_3
- `C12`: Decrease transmission power for 3230197_3
- `C13`: Decrease transmission power for 3272674_2
- `C14`: Press down the tilt angle  of 3230197_3 by 6 degrees
- `C15`: Lift the tilt angle of 3272674_2 by 5 degrees
- `C16`: Increase A3 Offset threshold for 3272674_2
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease A3 Offset threshold for 3272674_2
- `C19`: Lift the tilt angle  of 3230197_3 by 6 degrees
- `C20`: Adjust the azimuth of 3272674_2 by 15 degrees
- `C21`: Decrease A3 Offset threshold for 3230197_3
- `C22`: Increase transmission power for 3272674_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.327 | MS1 | 121.4656737676 | 31.1446331454 | 282 | 504990 | -85.98 | 16.24 | 323.58 | 0.13 | 2.83 | 1581 |
| 2024-09-20 22:21:32.381 | MS1 | 121.4656757560 | 31.1446235797 | 282 | 504990 | -86.49 | 13.58 | 529.11 | 0.01 | 2.07 | 1600 |
| 2024-09-20 22:21:33.998 | MS1 | 121.4656740835 | 31.1446215075 | 282 | 504990 | -85.50 | 12.14 | 507.16 | 0.18 | 2.72 | 1587 |
| 2024-09-20 22:21:34.371 | MS1 | 121.4656699346 | 31.1446322822 | 282 | 504990 | -87.69 | 12.53 | 88.96 | 0.58 | 2.56 | 578 |
| 2024-09-20 22:21:35.535 | MS1 | 121.4656736401 | 31.1446349890 | 282 | 504990 | -85.65 | 16.99 | 50.26 | 0.67 | 2.60 | 523 |
| 2024-09-20 22:21:36.170 | MS1 | 121.4656640409 | 31.1446215990 | 282 | 504990 | -88.74 | 17.70 | 57.66 | 0.63 | 2.39 | 636 |
| 2024-09-20 22:21:37.603 | MS1 | 121.4656595108 | 31.1446298162 | 282 | 504990 | -89.80 | 7.06 | 88.94 | 0.57 | 2.58 | 603 |
| 2024-09-20 22:21:38.489 | MS1 | 121.4656733359 | 31.1446293863 | 282 | 504990 | -93.91 | 12.78 | 77.42 | 0.55 | 2.57 | 546 |
| 2024-09-20 22:21:39.783 | MS1 | 121.4656707262 | 31.1446315197 | 282 | 504990 | -93.43 | 12.08 | 52.01 | 0.61 | 2.17 | 505 |
| 2024-09-20 22:21:40.107 | MS1 | 121.4656663515 | 31.1446339904 | 282 | 504990 | -91.19 | 7.03 | 556.46 | 0.13 | 2.91 | 1568 |
| 2024-09-20 22:21:41.301 | MS1 | 121.4656679994 | 31.1446244149 | 282 | 504990 | -93.79 | 12.05 | 329.56 | 0.02 | 2.97 | 1600 |
| 2024-09-20 22:21:42.898 | MS1 | 121.4656712358 | 31.1446215164 | 282 | 504990 | -93.15 | 10.26 | 572.48 | 0.14 | 2.25 | 1590 |

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
| 3221945 | 4 | 121.4677365381 | 31.1501401691 | 116 | 3 | 3 | 17.2 | TDD | 469 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3230197 | 3 | 121.4652971443 | 31.1479078476 | 34 | 2 | 9 | 26.3 | TDD | 956 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3231461 | 1 | 121.4641645964 | 31.1463497489 | 345 | 13 | 1 | 17.4 | TDD | 1000 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3272674 | 2 | 121.4725446580 | 31.1496054090 | 215 | 3 | 2 | 23.1 | TDD | 282 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.948 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.969 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.109 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.109 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.795 | NREventA3 | measId:2;ServCellPCI:127;Se... |
| 2024-09-20 22:21:38.035 | NRHandoverAttempt | SourcePCI:127;SourceNR-ARFC... |
| 2024-09-20 22:21:38.070 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.081 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.206 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.206 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231461 | 1 | 15.6146 | 13.8365 | -116.4529 | 17.5381 | 197.9590 | 0.0062 | 0.0006 |
| 2024_09_20 22:00 | 3272674 | 2 | 6.4070 | 7.9056 | -114.3216 | 16.4032 | 139.7231 | 0.0037 | 0.0077 |
| 2024_09_20 22:00 | 3230197 | 3 | 5.4070 | 10.2306 | -115.0854 | 17.3921 | 197.3021 | 0.0100 | 0.0171 |
| 2024_09_20 22:00 | 3221945 | 4 | 10.2181 | 10.5026 | -115.3986 | 16.3254 | 195.6875 | 0.0082 | 0.0085 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413542_D0687B4E | 504990 | 282 | -87.7 | 504990 | 956 | -97.3 | 504990 | 469 | -95.3 | 504990 | 1000 |
| MR_1774413542_4B433BB3 | 504990 | 282 | -87.1 | 504990 | 956 | -95.9 | 504990 | 469 | -97.4 | 504990 | 1000 |
| MR_1774413542_8C3FEDEA | 504990 | 282 | -86.0 | 504990 | 956 | -97.0 | 504990 | 469 | -97.1 | 504990 | 1000 |
| MR_1774413542_A0866B17 | 504990 | 282 | -89.6 | 504990 | 956 | -96.3 | 504990 | 469 | -94.8 | 504990 | 1000 |
| MR_1774413542_5B735A64 | 504990 | 282 | -87.8 | 504990 | 956 | -95.0 | 504990 | 469 | -96.3 | 504990 | 1000 |
| MR_1774413542_21630111 | 504990 | 282 | -87.1 | 504990 | 956 | -95.9 | 504990 | 469 | -97.7 | 504990 | 1000 |
| MR_1774413542_7A38732A | 504990 | 282 | -87.7 | 504990 | 956 | -94.7 | 504990 | 469 | -98.6 | 504990 | 1000 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1897: `c68d1486-ad4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c68d1486-ad46-4642-a5ed-bbc2944802e5` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1897] topology](images/train_1897.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3239891_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273268_1
- `C3`: Increase A3 Offset threshold for 3239891_3
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Lift the tilt angle  of 3239891_3 by 2 degrees
- `C6`: Adjust the azimuth of 3239891_3 by 50 degrees
- `C7`: Add neighbor relationship between 3273268_1 and 3239891_3
- `C8`: Check test server and transmission issues **← 정답**
- `C9`: Lift the tilt angle of 3273268_1 by 7 degrees
- `C10`: Decrease A3 Offset threshold for 3273268_1
- `C11`: Add neighbor relationship between 3215674_2 and 3239891_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239891_3
- `C13`: Decrease A3 Offset threshold for 3239891_3
- `C14`: Decrease transmission power for 3273268_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239891_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273268_1
- `C17`: Adjust the azimuth of 3273268_1 by 50 degrees
- `C18`: Increase A3 Offset threshold for 3273268_1
- `C19`: Press down the tilt angle of 3273268_1 by 7 degrees
- `C20`: Increase transmission power for 3273268_1
- `C21`: Increase transmission power for 3239891_3
- `C22`: Press down the tilt angle  of 3239891_3 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.416 | MS1 | 121.4656596606 | 31.1446321645 | 840 | 504990 | -88.00 | 16.58 | 498.15 | 0.15 | 2.66 | 1573 |
| 2024-09-20 22:21:32.407 | MS1 | 121.4656600429 | 31.1446369374 | 840 | 504990 | -88.93 | 12.45 | 587.53 | 0.17 | 2.56 | 1589 |
| 2024-09-20 22:21:33.411 | MS1 | 121.4656633233 | 31.1446283968 | 840 | 504990 | -85.59 | 14.48 | 486.07 | 0.17 | 2.14 | 1574 |
| 2024-09-20 22:21:34.686 | MS1 | 121.4656767359 | 31.1446303780 | 840 | 504990 | -90.81 | 14.29 | 96.17 | 0.09 | 2.31 | 306 |
| 2024-09-20 22:21:35.190 | MS1 | 121.4656653831 | 31.1446252219 | 840 | 504990 | -86.42 | 12.90 | 57.95 | 0.16 | 2.85 | 369 |
| 2024-09-20 22:21:36.817 | MS1 | 121.4656645055 | 31.1446300698 | 840 | 504990 | -90.20 | 14.66 | 86.82 | 0.18 | 2.45 | 389 |
| 2024-09-20 22:21:37.880 | MS1 | 121.4656742748 | 31.1446312533 | 840 | 504990 | -89.85 | 7.59 | 105.84 | 0.19 | 2.78 | 458 |
| 2024-09-20 22:21:38.244 | MS1 | 121.4656582160 | 31.1446299215 | 840 | 504990 | -91.69 | 10.17 | 56.27 | 0.18 | 2.02 | 339 |
| 2024-09-20 22:21:39.243 | MS1 | 121.4656612680 | 31.1446328264 | 840 | 504990 | -92.74 | 9.96 | 50.97 | 0.01 | 2.39 | 304 |
| 2024-09-20 22:21:40.991 | MS1 | 121.4656603218 | 31.1446187530 | 840 | 504990 | -91.69 | 7.81 | 491.29 | 0.01 | 2.58 | 1574 |
| 2024-09-20 22:21:41.969 | MS1 | 121.4656681217 | 31.1446363015 | 840 | 504990 | -93.92 | 11.82 | 416.18 | 0.11 | 2.93 | 1600 |
| 2024-09-20 22:21:42.421 | MS1 | 121.4656641777 | 31.1446288362 | 840 | 504990 | -90.74 | 9.82 | 363.83 | 0.17 | 2.39 | 1589 |

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
| 3215674 | 2 | 121.4661044838 | 31.1503730308 | 330 | 3 | 7 | 32.3 | TDD | 267 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3239891 | 3 | 121.4734818705 | 31.1557979920 | 114 | 0 | 12 | 43.0 | TDD | 844 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3254685 | 4 | 121.4674010189 | 31.1495975110 | 143 | 8 | 11 | 33.8 | TDD | 861 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3273268 | 1 | 121.4689802855 | 31.1550465770 | 323 | 5 | 3 | 38.2 | TDD | 840 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.358 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.466 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.466 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.232 | NREventA3 | measId:2;ServCellPCI:719;Se... |
| 2024-09-20 22:21:38.472 | NRHandoverAttempt | SourcePCI:719;SourceNR-ARFC... |
| 2024-09-20 22:21:38.507 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.521 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.634 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.634 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273268 | 1 | 12.2906 | 19.0724 | -115.7568 | 10.1739 | 91.5926 | 0.0168 | 0.0056 |
| 2024_09_20 22:00 | 3215674 | 2 | 8.2626 | 18.5536 | -117.4987 | 12.6135 | 80.7252 | 0.0148 | 0.0174 |
| 2024_09_20 22:00 | 3239891 | 3 | 14.8823 | 8.2692 | -116.0655 | 6.6420 | 188.9119 | 0.0089 | 0.0183 |
| 2024_09_20 22:00 | 3254685 | 4 | 10.6753 | 18.3459 | -116.1279 | 12.5466 | 150.5485 | 0.0150 | 0.0058 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413658_7B9D3964 | 504990 | 840 | -90.4 | 504990 | 844 | -94.8 | 504990 | 267 | -105.6 | 504990 | 861 |
| MR_1774413658_10C05035 | 504990 | 840 | -91.8 | 504990 | 844 | -93.6 | 504990 | 267 | -106.8 | 504990 | 861 |
| MR_1774413658_44FDAC2C | 504990 | 840 | -91.0 | 504990 | 844 | -95.3 | 504990 | 267 | -104.0 | 504990 | 861 |
| MR_1774413658_32BC951F | 504990 | 840 | -88.9 | 504990 | 844 | -93.9 | 504990 | 267 | -107.0 | 504990 | 861 |
| MR_1774413658_32440437 | 504990 | 840 | -90.2 | 504990 | 844 | -96.3 | 504990 | 267 | -103.8 | 504990 | 861 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1898: `833825a6-ea9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `833825a6-ea95-4406-bb98-9f3994e274bc` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246364_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1898] topology](images/train_1898.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3246364_4 by 32 degrees
- `C2`: Check test server and transmission issues
- `C3`: Decrease A3 Offset threshold for 3234574_5
- `C4`: Decrease A3 Offset threshold for 3246364_4
- `C5`: Increase transmission power for 3246364_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246364_4
- `C7`: Add neighbor relationship between 3242997_12 and 3234574_5
- `C8`: Press down the tilt angle  of 3234574_5 by 6 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Lift the tilt angle  of 3234574_5 by 6 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234574_5
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246364_4 **← 정답**
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234574_5
- `C14`: Increase A3 Offset threshold for 3234574_5
- `C15`: Decrease transmission power for 3246364_4
- `C16`: Increase transmission power for 3234574_5
- `C17`: Lift the tilt angle of 3246364_4 by 5 degrees
- `C18`: Adjust the azimuth of 3234574_5 by 17 degrees
- `C19`: Decrease transmission power for 3234574_5
- `C20`: Add neighbor relationship between 3246364_4 and 3234574_5
- `C21`: Increase A3 Offset threshold for 3246364_4
- `C22`: Press down the tilt angle of 3246364_4 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.452 | MS1 | 121.4656628790 | 31.1446294682 | 759 | 504990 | -93.70 | 10.44 | 546.82 | 0.15 | 2.78 | 1581 |
| 2024-09-20 22:21:32.398 | MS1 | 121.4656676154 | 31.1446199171 | 800 | 504990 | -95.21 | 11.93 | 605.75 | 0.03 | 2.41 | 1593 |
| 2024-09-20 22:21:33.475 | MS1 | 121.4656713918 | 31.1446265475 | 783 | 504990 | -94.25 | 10.99 | 596.74 | 0.19 | 2.17 | 1567 |
| 2024-09-20 22:21:34.952 | MS1 | 121.4656728241 | 31.1446216279 | 706 | 152650 | -87.28 | 4.07 | 55.88 | 0.15 | 1.87 | 957 |
| 2024-09-20 22:21:35.875 | MS1 | 121.4656688236 | 31.1446335299 | 62 | 152650 | -94.28 | 7.52 | 51.18 | 0.01 | 1.97 | 922 |
| 2024-09-20 22:21:36.713 | MS1 | 121.4656776910 | 31.1446227680 | 182 | 152650 | -91.83 | 3.30 | 58.34 | 0.10 | 1.60 | 938 |
| 2024-09-20 22:21:37.368 | MS1 | 121.4656674256 | 31.1446199408 | 118 | 152650 | -90.98 | 5.73 | 74.52 | 0.10 | 1.90 | 969 |
| 2024-09-20 22:21:38.568 | MS1 | 121.4656675102 | 31.1446223319 | 706 | 152650 | -94.27 | 2.52 | 72.64 | 0.00 | 1.64 | 936 |
| 2024-09-20 22:21:39.523 | MS1 | 121.4656615502 | 31.1446272466 | 62 | 152650 | -95.95 | 2.74 | 50.36 | 0.15 | 1.93 | 970 |
| 2024-09-20 22:21:40.753 | MS1 | 121.4656644724 | 31.1446222257 | 182 | 152650 | -91.93 | 4.21 | 59.13 | 0.00 | 2.15 | 1566 |
| 2024-09-20 22:21:41.880 | MS1 | 121.4656646651 | 31.1446373602 | 118 | 152650 | -94.03 | 4.67 | 65.16 | 0.06 | 2.88 | 1578 |
| 2024-09-20 22:21:42.127 | MS1 | 121.4656670860 | 31.1446204530 | 706 | 152650 | -95.24 | 3.28 | 102.63 | 0.07 | 2.59 | 1584 |

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
| 3222699 | 8 | 121.4664559952 | 31.1455981122 | 218 | 11 | 9 | 17.7 | FDD | 196 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3227264 | 10 | 121.4683200223 | 31.1527271446 | 23 | 12 | 10 | 11.9 | FDD | 143 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3234574 | 5 | 121.4661997395 | 31.1520048644 | 167 | 4 | 1 | 24.9 | TDD | 185 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3235990 | 6 | 121.4651934689 | 31.1516051568 | 194 | 15 | 2 | 14.4 | TDD | 923 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3242997 | 12 | 121.4722147711 | 31.1484192387 | 182 | 0 | 12 | 25.7 | FDD | 182 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3243933 | 9 | 121.4745784763 | 31.1546710402 | 112 | 8 | 12 | 2.2 | FDD | 781 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3246364 | 4 | 121.4728764438 | 31.1452857567 | 232 | 3 | 10 | 22.6 | TDD | 759 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3247743 | 7 | 121.4755376761 | 31.1445038411 | 331 | 14 | 4 | 0.3 | FDD | 706 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3254827 | 13 | 121.4649293670 | 31.1453681601 | 20 | 1 | 2 | 9.3 | FDD | 62 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3259590 | 11 | 121.4745849375 | 31.1457686861 | 221 | 11 | 8 | 0.4 | FDD | 118 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3262862 | 1 | 121.4735511335 | 31.1483973817 | 262 | 0 | 12 | 0.6 | TDD | 800 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3267866 | 2 | 121.4713245557 | 31.1524121613 | 251 | 3 | 12 | 6.8 | TDD | 933 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3279189 | 3 | 121.4703876006 | 31.1537199969 | 136 | 3 | 8 | 23.5 | TDD | 783 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.098 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.120 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.251 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.251 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.916 | NREventA2 | measId:1;ServCellPCI:466;Se... |
| 2024-09-20 22:21:35.037 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.318 | NREventA5 | measId:3;ServCellPCI:466;Se... |
| 2024-09-20 22:21:35.377 | NRHandoverAttempt | SourcePCI:466;SourceNR-ARFC... |
| 2024-09-20 22:21:35.416 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.430 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.556 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.556 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262862 | 1 | 9.7378 | 10.8135 | -115.4970 | 17.9557 | 129.6036 | 0.0076 | 0.0130 |
| 2024_09_20 22:00 | 3267866 | 2 | 14.8102 | 19.9510 | -114.6345 | 13.8535 | 128.8263 | 0.0117 | 0.0109 |
| 2024_09_20 22:00 | 3279189 | 3 | 8.8032 | 13.6834 | -117.6936 | 17.5733 | 182.1449 | 0.0130 | 0.0155 |
| 2024_09_20 22:00 | 3246364 | 4 | 16.4445 | 10.6753 | -115.2477 | 6.8692 | 135.2257 | 0.0130 | 0.0187 |
| 2024_09_20 22:00 | 3234574 | 5 | 11.8744 | 8.2585 | -115.5073 | 19.1964 | 196.4862 | 0.0129 | 0.0019 |
| 2024_09_20 22:00 | 3235990 | 6 | 7.1418 | 13.9730 | -116.9087 | 15.6521 | 150.1455 | 0.0043 | 0.0146 |
| 2024_09_20 22:00 | 3247743 | 7 | 8.6612 | 17.4638 | -114.2736 | 3.8753 | 31.2624 | 0.0147 | 0.0154 |
| 2024_09_20 22:00 | 3222699 | 8 | 18.6545 | 18.4839 | -117.6522 | 4.2484 | 20.1093 | 0.0172 | 0.0200 |
| 2024_09_20 22:00 | 3243933 | 9 | 9.4797 | 15.9331 | -114.4746 | 4.9990 | 25.3004 | 0.0117 | 0.0064 |
| 2024_09_20 22:00 | 3227264 | 10 | 15.6300 | 17.6865 | -114.3174 | 4.8442 | 23.0892 | 0.0004 | 0.0095 |
| 2024_09_20 22:00 | 3259590 | 11 | 12.1848 | 6.5409 | -117.9671 | 4.7594 | 39.5179 | 0.0037 | 0.0195 |
| 2024_09_20 22:00 | 3242997 | 12 | 10.7730 | 13.1624 | -114.8551 | 3.0086 | 43.1256 | 0.0187 | 0.0026 |
| 2024_09_20 22:00 | 3254827 | 13 | 5.6280 | 11.0002 | -117.5649 | 3.9632 | 49.1923 | 0.0024 | 0.0067 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416236_C02B2AA6 | 504990 | 783 | -94.9 | 504990 | 185 | -96.6 | 504990 | 933 | -97.3 | 504990 | 923 |
| MR_1774416236_F921D9C1 | 504990 | 783 | -93.2 | 504990 | 185 | -96.6 | 504990 | 933 | -95.3 | 504990 | 923 |
| MR_1774416236_E92C4A4A | 504990 | 783 | -92.5 | 504990 | 185 | -95.5 | 504990 | 933 | -95.1 | 504990 | 923 |
| MR_1774416236_4E82CB0D | 152650 | 706 | -85.9 | 152650 | 143 | -91.6 | 152650 | 781 | -95.4 | 152650 | 196 |
| MR_1774416236_B1565366 | 152650 | 706 | -85.7 | 152650 | 143 | -94.1 | 152650 | 781 | -93.0 | 152650 | 196 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1899: `40d11965-818...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `40d11965-8186-4a10-af27-e970ca65e70d` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273471_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1899] topology](images/train_1899.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease A3 Offset threshold for 3264111_6
- `C4`: Decrease A3 Offset threshold for 3273471_4
- `C5`: Add neighbor relationship between 3261440_10 and 3264111_6
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273471_4
- `C7`: Adjust the azimuth of 3273471_4 by 38 degrees
- `C8`: Add neighbor relationship between 3273471_4 and 3264111_6
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264111_6
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273471_4 **← 정답**
- `C11`: Adjust the azimuth of 3264111_6 by 19 degrees
- `C12`: Increase A3 Offset threshold for 3273471_4
- `C13`: Press down the tilt angle  of 3264111_6 by 3 degrees
- `C14`: Lift the tilt angle  of 3264111_6 by 3 degrees
- `C15`: Decrease transmission power for 3264111_6
- `C16`: Increase transmission power for 3264111_6
- `C17`: Press down the tilt angle of 3273471_4 by 4 degrees
- `C18`: Increase A3 Offset threshold for 3264111_6
- `C19`: Lift the tilt angle of 3273471_4 by 4 degrees
- `C20`: Decrease transmission power for 3273471_4
- `C21`: Increase transmission power for 3273471_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264111_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.950 | MS1 | 121.4656694265 | 31.1446201308 | 659 | 504990 | -94.76 | 12.78 | 417.12 | 0.15 | 2.69 | 1568 |
| 2024-09-20 22:21:32.962 | MS1 | 121.4656641670 | 31.1446305982 | 372 | 504990 | -94.02 | 10.78 | 323.57 | 0.17 | 2.06 | 1591 |
| 2024-09-20 22:21:33.630 | MS1 | 121.4656748511 | 31.1446198366 | 750 | 504990 | -95.81 | 9.73 | 459.48 | 0.12 | 2.66 | 1581 |
| 2024-09-20 22:21:34.582 | MS1 | 121.4656777783 | 31.1446370401 | 680 | 152650 | -91.50 | 6.63 | 91.25 | 0.19 | 1.61 | 934 |
| 2024-09-20 22:21:35.641 | MS1 | 121.4656644754 | 31.1446289018 | 861 | 152650 | -92.32 | 7.83 | 61.83 | 0.12 | 1.67 | 962 |
| 2024-09-20 22:21:36.537 | MS1 | 121.4656627498 | 31.1446312748 | 785 | 152650 | -91.49 | 3.49 | 51.71 | 0.12 | 1.60 | 988 |
| 2024-09-20 22:21:37.217 | MS1 | 121.4656772958 | 31.1446242442 | 300 | 152650 | -94.38 | 3.97 | 85.05 | 0.16 | 1.82 | 979 |
| 2024-09-20 22:21:38.514 | MS1 | 121.4656624821 | 31.1446213702 | 680 | 152650 | -87.40 | 3.43 | 84.26 | 0.16 | 1.81 | 943 |
| 2024-09-20 22:21:39.268 | MS1 | 121.4656775369 | 31.1446342395 | 861 | 152650 | -92.33 | 6.03 | 46.43 | 0.03 | 1.96 | 990 |
| 2024-09-20 22:21:40.834 | MS1 | 121.4656773037 | 31.1446270492 | 785 | 152650 | -94.15 | 5.56 | 58.73 | 0.09 | 2.09 | 1582 |
| 2024-09-20 22:21:41.812 | MS1 | 121.4656662933 | 31.1446355829 | 300 | 152650 | -96.27 | 2.24 | 63.40 | 0.03 | 2.45 | 1570 |
| 2024-09-20 22:21:42.653 | MS1 | 121.4656698000 | 31.1446327511 | 680 | 152650 | -91.53 | 2.66 | 53.27 | 0.00 | 2.14 | 1560 |

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
| 3215861 | 8 | 121.4709853955 | 31.1500198565 | 161 | 15 | 11 | 22.6 | FDD | 168 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3216323 | 5 | 121.4688876508 | 31.1466298514 | 101 | 12 | 5 | 16.2 | TDD | 372 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3219751 | 13 | 121.4716002668 | 31.1448517680 | 174 | 8 | 5 | 1.9 | FDD | 861 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3244181 | 7 | 121.4750773590 | 31.1460930291 | 268 | 15 | 1 | 24.8 | FDD | 680 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3246953 | 2 | 121.4645875600 | 31.1537317914 | 219 | 8 | 3 | 18.3 | TDD | 301 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3247229 | 12 | 121.4739567664 | 31.1525649743 | 111 | 8 | 11 | 0.1 | FDD | 26 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3250502 | 9 | 121.4686810869 | 31.1526428053 | 232 | 5 | 10 | 5.4 | FDD | 300 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3251664 | 1 | 121.4754253547 | 31.1475775540 | 322 | 10 | 3 | 23.6 | TDD | 868 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3259492 | 3 | 121.4650498149 | 31.1472165066 | 239 | 7 | 9 | 18.3 | TDD | 750 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3261440 | 10 | 121.4717368461 | 31.1461332737 | 336 | 15 | 8 | 27.7 | FDD | 785 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3264111 | 6 | 121.4725877373 | 31.1477178503 | 261 | 2 | 11 | 11.8 | TDD | 568 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3273471 | 4 | 121.4675220174 | 31.1559971502 | 150 | 3 | 4 | 19.7 | TDD | 659 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3279861 | 11 | 121.4707305325 | 31.1542305871 | 246 | 2 | 1 | 15.3 | FDD | 505 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |

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
| 2024-09-20 22:21:31.366 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.388 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.510 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.510 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.251 | NREventA2 | measId:1;ServCellPCI:438;Se... |
| 2024-09-20 22:21:35.390 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.642 | NREventA5 | measId:3;ServCellPCI:438;Se... |
| 2024-09-20 22:21:35.677 | NRHandoverAttempt | SourcePCI:438;SourceNR-ARFC... |
| 2024-09-20 22:21:35.705 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.717 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.836 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.836 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251664 | 1 | 10.1098 | 16.9191 | -116.1342 | 10.4082 | 122.4457 | 0.0136 | 0.0093 |
| 2024_09_20 22:00 | 3246953 | 2 | 19.7128 | 8.1721 | -117.8721 | 13.8605 | 173.9988 | 0.0132 | 0.0162 |
| 2024_09_20 22:00 | 3259492 | 3 | 14.5240 | 18.4569 | -115.6720 | 5.2746 | 182.0672 | 0.0110 | 0.0159 |
| 2024_09_20 22:00 | 3273471 | 4 | 11.0569 | 14.6195 | -114.3869 | 16.4428 | 158.9464 | 0.0021 | 0.0030 |
| 2024_09_20 22:00 | 3216323 | 5 | 6.7274 | 12.7675 | -115.1549 | 16.1572 | 199.4585 | 0.0106 | 0.0094 |
| 2024_09_20 22:00 | 3264111 | 6 | 8.0965 | 14.5730 | -115.9648 | 6.5891 | 141.6952 | 0.0096 | 0.0081 |
| 2024_09_20 22:00 | 3244181 | 7 | 16.7204 | 12.9225 | -115.6769 | 3.6799 | 50.1996 | 0.0134 | 0.0079 |
| 2024_09_20 22:00 | 3215861 | 8 | 10.1434 | 15.6506 | -114.8095 | 4.3456 | 56.2448 | 0.0122 | 0.0014 |
| 2024_09_20 22:00 | 3250502 | 9 | 15.8798 | 12.0136 | -117.1564 | 3.5610 | 22.7792 | 0.0121 | 0.0042 |
| 2024_09_20 22:00 | 3261440 | 10 | 11.6008 | 18.9067 | -117.4432 | 4.8014 | 44.5326 | 0.0027 | 0.0120 |
| 2024_09_20 22:00 | 3279861 | 11 | 11.0176 | 16.8398 | -117.3669 | 4.3631 | 51.5439 | 0.0141 | 0.0028 |
| 2024_09_20 22:00 | 3247229 | 12 | 12.4410 | 19.0008 | -116.8088 | 3.5408 | 52.6999 | 0.0039 | 0.0022 |
| 2024_09_20 22:00 | 3219751 | 13 | 7.3068 | 13.2435 | -116.4635 | 3.1295 | 29.1723 | 0.0003 | 0.0163 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415416_1018F07E | 504990 | 750 | -95.4 | 504990 | 568 | -94.0 | 504990 | 301 | -100.2 | 504990 | 868 |
| MR_1774415416_B100F418 | 504990 | 750 | -95.7 | 504990 | 568 | -95.5 | 504990 | 301 | -102.8 | 504990 | 868 |
| MR_1774415416_C3ECC2D1 | 504990 | 750 | -94.4 | 504990 | 568 | -94.3 | 504990 | 301 | -102.3 | 504990 | 868 |
| MR_1774415416_2AB4F356 | 152650 | 680 | -91.8 | 152650 | 26 | -94.3 | 152650 | 168 | -102.8 | 152650 | 505 |
| MR_1774415416_EDF130A0 | 152650 | 680 | -93.2 | 152650 | 26 | -94.3 | 152650 | 168 | -100.0 | 152650 | 505 |
| MR_1774415416_B5EC4C9D | 504990 | 750 | -94.2 | 504990 | 568 | -96.5 | 504990 | 301 | -99.1 | 504990 | 868 |

> *... 2개 열 생략 (전체 14열)*

---
