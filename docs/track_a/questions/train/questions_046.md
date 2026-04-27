# Track A 문제 분석 — train[450]~train[459]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[450] ~ train[459] (10개)

## 목차

1. [문제 450: `b967f512-758...`](#450) — single-answer, 정답: C6
2. [문제 451: `c5569656-2a7...`](#451) — single-answer, 정답: C22
3. [문제 452: `df55b209-5fb...`](#452) — multiple-answer, 정답: C1|C22
4. [문제 453: `1c74d960-256...`](#453) — single-answer, 정답: C3
5. [문제 454: `6d52fdce-823...`](#454) — single-answer, 정답: C12
6. [문제 455: `7d17a240-153...`](#455) — single-answer, 정답: C22
7. [문제 456: `d7537c71-27b...`](#456) — single-answer, 정답: C15
8. [문제 457: `496f7980-c90...`](#457) — single-answer, 정답: C9
9. [문제 458: `38af0020-779...`](#458) — single-answer, 정답: C17
10. [문제 459: `dc7fab49-aa3...`](#459) — single-answer, 정답: C20

---

### 문제 450: `b967f512-758...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b967f512-7582-436a-a754-e207f951caa6` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Lift the tilt angle  of 3275549_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[450] topology](images/train_0450.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247659_2
- `C2`: Decrease transmission power for 3247659_2
- `C3`: Press down the tilt angle of 3247659_2 by 6 degrees
- `C4`: Lift the tilt angle of 3247659_2 by 6 degrees
- `C5`: Increase A3 Offset threshold for 3247659_2
- `C6`: Lift the tilt angle  of 3275549_4 by 10 degrees **← 정답**
- `C7`: Decrease transmission power for 3264100_3
- `C8`: Increase A3 Offset threshold for 3264100_3
- `C9`: Increase transmission power for 3264100_3
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Add neighbor relationship between 3247659_2 and 3264100_3
- `C12`: Decrease A3 Offset threshold for 3247659_2
- `C13`: Check test server and transmission issues
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264100_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247659_2
- `C16`: Increase transmission power for 3247659_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264100_3
- `C18`: Decrease A3 Offset threshold for 3264100_3
- `C19`: Press down the tilt angle  of 3275549_4 by 10 degrees
- `C20`: Adjust the azimuth of 3275549_4 by 49 degrees
- `C21`: Adjust the azimuth of 3247659_2 by 18 degrees
- `C22`: Add neighbor relationship between 3275549_4 and 3264100_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.197 | MS1 | 121.4656623640 | 31.1446254545 | 587 | 504990 | -88.76 | 13.76 | 580.05 | 0.14 | 2.81 | 1577 |
| 2024-09-20 22:21:32.519 | MS1 | 121.4656682874 | 31.1446252423 | 587 | 504990 | -91.15 | 13.60 | 484.31 | 0.08 | 2.76 | 1560 |
| 2024-09-20 22:21:33.693 | MS1 | 121.4656735207 | 31.1446195742 | 587 | 504990 | -85.51 | 15.33 | 478.47 | 0.05 | 2.18 | 1595 |
| 2024-09-20 22:21:34.215 | MS1 | 121.4656708453 | 31.1446281822 | 587 | 504990 | -91.60 | 17.87 | 85.22 | 0.16 | 2.25 | 1581 |
| 2024-09-20 22:21:35.159 | MS1 | 121.4656641869 | 31.1446335130 | 587 | 504990 | -85.21 | 14.41 | 97.84 | 0.10 | 2.26 | 1570 |
| 2024-09-20 22:21:36.480 | MS1 | 121.4656622357 | 31.1446203867 | 587 | 504990 | -85.29 | 16.09 | 71.72 | 0.14 | 2.65 | 1571 |
| 2024-09-20 22:21:37.610 | MS1 | 121.4656614505 | 31.1446294987 | 587 | 504990 | -92.83 | 8.05 | 88.38 | 0.19 | 2.57 | 1581 |
| 2024-09-20 22:21:38.421 | MS1 | 121.4656675584 | 31.1446314132 | 587 | 504990 | -91.12 | 8.75 | 63.81 | 0.14 | 2.14 | 1592 |
| 2024-09-20 22:21:39.307 | MS1 | 121.4656719728 | 31.1446237350 | 587 | 504990 | -89.98 | 7.56 | 90.40 | 0.20 | 2.97 | 1567 |
| 2024-09-20 22:21:40.612 | MS1 | 121.4656733025 | 31.1446182415 | 587 | 504990 | -93.12 | 11.62 | 535.55 | 0.10 | 2.21 | 1570 |
| 2024-09-20 22:21:41.425 | MS1 | 121.4656644912 | 31.1446265752 | 587 | 504990 | -91.47 | 12.15 | 471.71 | 0.18 | 2.77 | 1577 |
| 2024-09-20 22:21:42.765 | MS1 | 121.4656636513 | 31.1446227446 | 587 | 504990 | -91.36 | 11.88 | 535.21 | 0.01 | 2.57 | 1600 |

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
| 3215574 | 1 | 121.4663860818 | 31.1528798185 | 357 | 13 | 1 | 43.8 | TDD | 992 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3247659 | 2 | 121.4739955070 | 31.1446973752 | 287 | 4 | 9 | 27.1 | TDD | 587 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3264100 | 3 | 121.4744365667 | 31.1482247324 | 293 | 15 | 8 | 22.6 | TDD | 271 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3275549 | 4 | 121.4734939195 | 31.1550807768 | 14 | 0 | 9 | 28.6 | TDD | 327 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.997 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.017 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.161 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.161 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.862 | NREventA3 | measId:2;ServCellPCI:321;Se... |
| 2024-09-20 22:21:38.102 | NRHandoverAttempt | SourcePCI:321;SourceNR-ARFC... |
| 2024-09-20 22:21:38.137 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.149 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.269 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.269 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215574 | 1 | 5.3094 | 16.9826 | -117.4140 | 19.3325 | 153.6707 | 0.0047 | 0.0069 |
| 2024_09_20 22:00 | 3247659 | 2 | 76.7975 | 90.9641 | -115.4465 | 13.3999 | 197.2008 | 0.0061 | 0.0044 |
| 2024_09_20 22:00 | 3264100 | 3 | 5.9334 | 18.2386 | -114.6154 | 10.2906 | 133.1030 | 0.0140 | 0.0069 |
| 2024_09_20 22:00 | 3275549 | 4 | 5.6942 | 9.6725 | -114.9915 | 13.1191 | 159.0571 | 0.0029 | 0.0019 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415071_1E5A69D4 | 504990 | 587 | -92.9 | 504990 | 271 | -98.6 | 504990 | 327 | -102.6 | 504990 | 992 |
| MR_1774415071_A7BFF1D7 | 504990 | 587 | -89.6 | 504990 | 271 | -96.8 | 504990 | 327 | -104.6 | 504990 | 992 |
| MR_1774415071_0556D828 | 504990 | 587 | -92.2 | 504990 | 271 | -96.3 | 504990 | 327 | -101.3 | 504990 | 992 |
| MR_1774415071_7E479E63 | 504990 | 587 | -92.2 | 504990 | 271 | -97.2 | 504990 | 327 | -104.6 | 504990 | 992 |
| MR_1774415071_870C310E | 504990 | 587 | -90.3 | 504990 | 271 | -97.6 | 504990 | 327 | -102.6 | 504990 | 992 |
| MR_1774415071_9233971E | 504990 | 587 | -93.1 | 504990 | 271 | -98.5 | 504990 | 327 | -103.5 | 504990 | 992 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 451: `c5569656-2a7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c5569656-2a7f-4eec-82d3-2c476f34b973` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256911_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[451] topology](images/train_0451.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease A3 Offset threshold for 3256911_6
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase transmission power for 3230121_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230121_4
- `C6`: Add neighbor relationship between 3256911_6 and 3230121_4
- `C7`: Lift the tilt angle  of 3230121_4 by 3 degrees
- `C8`: Decrease A3 Offset threshold for 3230121_4
- `C9`: Increase transmission power for 3256911_6
- `C10`: Lift the tilt angle of 3256911_6 by 1 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230121_4
- `C12`: Add neighbor relationship between 3251352_11 and 3230121_4
- `C13`: Press down the tilt angle of 3256911_6 by 1 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256911_6
- `C15`: Increase A3 Offset threshold for 3230121_4
- `C16`: Decrease transmission power for 3230121_4
- `C17`: Decrease transmission power for 3256911_6
- `C18`: Press down the tilt angle  of 3230121_4 by 3 degrees
- `C19`: Adjust the azimuth of 3230121_4 by 18 degrees
- `C20`: Adjust the azimuth of 3256911_6 by 39 degrees
- `C21`: Increase A3 Offset threshold for 3256911_6
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256911_6 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.405 | MS1 | 121.4656592284 | 31.1446274623 | 441 | 504990 | -93.36 | 10.57 | 361.35 | 0.19 | 2.74 | 1562 |
| 2024-09-20 22:21:32.626 | MS1 | 121.4656601577 | 31.1446198035 | 967 | 504990 | -93.46 | 11.32 | 295.36 | 0.20 | 2.53 | 1591 |
| 2024-09-20 22:21:33.307 | MS1 | 121.4656613050 | 31.1446332242 | 197 | 504990 | -94.99 | 12.52 | 564.35 | 0.16 | 2.52 | 1570 |
| 2024-09-20 22:21:34.267 | MS1 | 121.4656751834 | 31.1446227307 | 737 | 152650 | -87.71 | 3.02 | 42.26 | 0.01 | 1.79 | 921 |
| 2024-09-20 22:21:35.380 | MS1 | 121.4656677328 | 31.1446193282 | 378 | 152650 | -95.41 | 5.10 | 91.15 | 0.12 | 1.75 | 962 |
| 2024-09-20 22:21:36.347 | MS1 | 121.4656692157 | 31.1446259234 | 148 | 152650 | -96.91 | 4.45 | 96.18 | 0.15 | 1.61 | 936 |
| 2024-09-20 22:21:37.281 | MS1 | 121.4656625294 | 31.1446264519 | 481 | 152650 | -96.35 | 6.80 | 76.20 | 0.11 | 1.73 | 950 |
| 2024-09-20 22:21:38.365 | MS1 | 121.4656719323 | 31.1446262733 | 737 | 152650 | -87.34 | 4.64 | 78.08 | 0.01 | 1.70 | 912 |
| 2024-09-20 22:21:39.387 | MS1 | 121.4656604423 | 31.1446193898 | 378 | 152650 | -87.36 | 2.93 | 101.16 | 0.15 | 1.80 | 980 |
| 2024-09-20 22:21:40.175 | MS1 | 121.4656690659 | 31.1446256073 | 148 | 152650 | -88.78 | 2.73 | 89.03 | 0.14 | 2.86 | 1595 |
| 2024-09-20 22:21:41.503 | MS1 | 121.4656700919 | 31.1446370760 | 481 | 152650 | -96.29 | 7.65 | 56.51 | 0.12 | 2.22 | 1573 |
| 2024-09-20 22:21:42.122 | MS1 | 121.4656747373 | 31.1446186541 | 737 | 152650 | -95.61 | 2.41 | 61.50 | 0.08 | 2.45 | 1592 |

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
| 3212742 | 10 | 121.4710881443 | 31.1445315106 | 215 | 6 | 1 | 6.5 | FDD | 717 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3214598 | 5 | 121.4646051006 | 31.1533591340 | 289 | 1 | 10 | 2.7 | TDD | 245 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3219678 | 2 | 121.4648682891 | 31.1522165855 | 108 | 14 | 10 | 28.2 | TDD | 967 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3222187 | 3 | 121.4685269325 | 31.1547465980 | 163 | 15 | 8 | 21.0 | TDD | 752 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3230121 | 4 | 121.4706463832 | 31.1521101986 | 192 | 2 | 7 | 24.3 | TDD | 657 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3237974 | 8 | 121.4698814773 | 31.1446272362 | 228 | 14 | 6 | 27.4 | FDD | 481 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3241552 | 9 | 121.4665370110 | 31.1521221318 | 322 | 1 | 7 | 23.2 | FDD | 230 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3251004 | 7 | 121.4694303041 | 31.1499551185 | 188 | 13 | 2 | 28.2 | FDD | 737 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3251352 | 11 | 121.4691907682 | 31.1518003651 | 9 | 13 | 10 | 7.2 | FDD | 148 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3252242 | 12 | 121.4660866192 | 31.1470297691 | 280 | 7 | 1 | 19.3 | FDD | 378 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3256383 | 1 | 121.4711751953 | 31.1534672295 | 4 | 5 | 8 | 23.5 | TDD | 197 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3256911 | 6 | 121.4747595782 | 31.1551809151 | 255 | 0 | 12 | 25.5 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3263220 | 13 | 121.4696588534 | 31.1538752057 | 209 | 4 | 7 | 11.1 | FDD | 319 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |

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
| 2024-09-20 22:21:30.893 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.910 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.034 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.034 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.697 | NREventA2 | measId:1;ServCellPCI:59;Ser... |
| 2024-09-20 22:21:34.816 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.055 | NREventA5 | measId:3;ServCellPCI:59;Ser... |
| 2024-09-20 22:21:35.103 | NRHandoverAttempt | SourcePCI:59;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.140 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.152 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.257 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.257 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256383 | 1 | 18.7211 | 11.6635 | -117.8069 | 17.0819 | 141.7122 | 0.0080 | 0.0114 |
| 2024_09_20 22:00 | 3219678 | 2 | 11.0139 | 15.7060 | -117.7649 | 11.7572 | 160.8749 | 0.0109 | 0.0023 |
| 2024_09_20 22:00 | 3222187 | 3 | 17.0650 | 7.5164 | -116.6587 | 14.5675 | 193.8127 | 0.0117 | 0.0183 |
| 2024_09_20 22:00 | 3230121 | 4 | 13.2208 | 5.1270 | -117.5540 | 13.1474 | 182.2281 | 0.0127 | 0.0059 |
| 2024_09_20 22:00 | 3214598 | 5 | 8.1083 | 16.2401 | -114.8866 | 14.1184 | 146.3919 | 0.0103 | 0.0141 |
| 2024_09_20 22:00 | 3256911 | 6 | 17.7070 | 16.4002 | -114.4235 | 11.2852 | 85.9811 | 0.0093 | 0.0107 |
| 2024_09_20 22:00 | 3251004 | 7 | 7.4062 | 16.0086 | -117.5170 | 4.4889 | 49.7665 | 0.0016 | 0.0174 |
| 2024_09_20 22:00 | 3237974 | 8 | 14.4874 | 5.8416 | -116.3251 | 4.9861 | 55.9092 | 0.0057 | 0.0048 |
| 2024_09_20 22:00 | 3241552 | 9 | 11.8994 | 18.7435 | -115.4988 | 3.1446 | 30.4867 | 0.0072 | 0.0172 |
| 2024_09_20 22:00 | 3212742 | 10 | 11.0189 | 13.6236 | -115.2853 | 4.4594 | 20.6589 | 0.0173 | 0.0056 |
| 2024_09_20 22:00 | 3251352 | 11 | 14.9795 | 16.2428 | -114.3103 | 3.7206 | 59.6432 | 0.0003 | 0.0062 |
| 2024_09_20 22:00 | 3252242 | 12 | 7.3377 | 10.1803 | -115.2643 | 4.5180 | 29.9522 | 0.0034 | 0.0175 |
| 2024_09_20 22:00 | 3263220 | 13 | 8.7010 | 15.3967 | -117.5679 | 3.5970 | 25.5549 | 0.0197 | 0.0114 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413345_D2346F51 | 504990 | 197 | -95.3 | 504990 | 657 | -97.1 | 504990 | 752 | -99.9 | 504990 | 245 |
| MR_1774413345_0BE7146D | 504990 | 197 | -96.9 | 504990 | 657 | -98.2 | 504990 | 752 | -99.4 | 504990 | 245 |
| MR_1774413345_24F23769 | 504990 | 197 | -95.3 | 504990 | 657 | -98.5 | 504990 | 752 | -101.9 | 504990 | 245 |
| MR_1774413345_FB557588 | 504990 | 197 | -95.5 | 504990 | 657 | -99.6 | 504990 | 752 | -101.6 | 504990 | 245 |
| MR_1774413345_F04BCED4 | 152650 | 737 | -87.8 | 152650 | 717 | -92.8 | 152650 | 319 | -97.4 | 152650 | 230 |
| MR_1774413345_779B657F | 152650 | 737 | -85.8 | 152650 | 717 | -89.5 | 152650 | 319 | -96.8 | 152650 | 230 |
| MR_1774413345_DAC5F7EA | 152650 | 737 | -88.8 | 152650 | 717 | -90.1 | 152650 | 319 | -96.3 | 152650 | 230 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 452: `df55b209-5fb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `df55b209-5fbe-47c6-a410-ea5873be41e3` |
| Tag | **multiple-answer** |
| 정답 | **C1|C22** |
| C1 의미 | Increase transmission power for 3244161_1 |
| C22 의미 | Adjust the azimuth of 3244161_1 by 40 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[452] topology](images/train_0452.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3244161_1 **← 정답**
- `C2`: Lift the tilt angle of 3244161_1 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244161_1
- `C4`: Decrease transmission power for 3244161_1
- `C5`: Decrease transmission power for 3248341_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248341_2
- `C7`: Add neighbor relationship between 3265669_3 and 3248341_2
- `C8`: Lift the tilt angle  of 3248341_2 by 4 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244161_1
- `C10`: Decrease A3 Offset threshold for 3248341_2
- `C11`: Press down the tilt angle of 3244161_1 by 10 degrees
- `C12`: Increase A3 Offset threshold for 3248341_2
- `C13`: Increase transmission power for 3248341_2
- `C14`: Check test server and transmission issues
- `C15`: Increase A3 Offset threshold for 3244161_1
- `C16`: Adjust the azimuth of 3248341_2 by 46 degrees
- `C17`: Press down the tilt angle  of 3248341_2 by 4 degrees
- `C18`: Decrease A3 Offset threshold for 3244161_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248341_2
- `C20`: Add neighbor relationship between 3244161_1 and 3248341_2
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Adjust the azimuth of 3244161_1 by 40 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.588 | MS1 | 121.4656589515 | 31.1446376223 | 265 | 504990 | -93.49 | 13.37 | 498.74 | 0.18 | 2.08 | 1575 |
| 2024-09-20 22:21:32.858 | MS1 | 121.4656580232 | 31.1446239741 | 265 | 504990 | -93.49 | 13.06 | 589.44 | 0.12 | 2.93 | 1571 |
| 2024-09-20 22:21:33.948 | MS1 | 121.4656738899 | 31.1446251991 | 265 | 504990 | -94.62 | 16.30 | 485.48 | 0.18 | 2.49 | 1567 |
| 2024-09-20 22:21:34.661 | MS1 | 121.4656690117 | 31.1446252367 | 265 | 504990 | -106.70 | -1.87 | 50.41 | 0.17 | 1.42 | 1561 |
| 2024-09-20 22:21:35.767 | MS1 | 121.4656648099 | 31.1446285550 | 265 | 504990 | -109.65 | 0.80 | 48.25 | 0.02 | 1.05 | 1594 |
| 2024-09-20 22:21:36.827 | MS1 | 121.4656684216 | 31.1446247138 | 265 | 504990 | -100.73 | -1.70 | 60.24 | 0.12 | 1.49 | 1598 |
| 2024-09-20 22:21:37.898 | MS1 | 121.4656774825 | 31.1446288825 | 265 | 504990 | -109.77 | -1.92 | 35.65 | 0.10 | 1.03 | 1594 |
| 2024-09-20 22:21:38.140 | MS1 | 121.4656774692 | 31.1446375183 | 265 | 504990 | -105.48 | 0.76 | 68.28 | 0.11 | 1.46 | 1592 |
| 2024-09-20 22:21:39.336 | MS1 | 121.4656647450 | 31.1446299083 | 265 | 504990 | -103.93 | 0.27 | 54.37 | 0.12 | 1.20 | 1588 |
| 2024-09-20 22:21:40.527 | MS1 | 121.4656757633 | 31.1446360008 | 265 | 504990 | -87.74 | 13.39 | 368.13 | 0.07 | 2.02 | 1566 |
| 2024-09-20 22:21:41.188 | MS1 | 121.4656709453 | 31.1446366548 | 265 | 504990 | -91.07 | 17.90 | 400.11 | 0.16 | 2.50 | 1562 |
| 2024-09-20 22:21:42.263 | MS1 | 121.4656628205 | 31.1446228534 | 265 | 504990 | -92.88 | 17.56 | 525.06 | 0.20 | 2.82 | 1578 |

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
| 3244161 | 1 | 121.4669269502 | 31.1453311235 | 197 | 3 | 1 | 34.1 | TDD | 265 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3248341 | 2 | 121.4692339288 | 31.1552449017 | 150 | 2 | 5 | 39.6 | TDD | 490 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3265669 | 3 | 121.4653960618 | 31.1491720024 | 128 | 6 | 11 | 38.4 | TDD | 156 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3271022 | 4 | 121.4709099566 | 31.1444866867 | 94 | 0 | 12 | 18.5 | TDD | 25 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.251 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.267 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.383 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.383 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.570 | NREventA2 | measId:1;ServCellPCI:761;Se... |
| 2024-09-20 22:21:34.701 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244161 | 1 | 17.6587 | 8.0045 | -114.6837 | 17.4593 | 199.8717 | 0.1013 | 0.0012 |
| 2024_09_20 22:00 | 3248341 | 2 | 18.7850 | 18.7280 | -115.3031 | 17.0508 | 127.8328 | 0.0101 | 0.0059 |
| 2024_09_20 22:00 | 3265669 | 3 | 14.3975 | 12.5631 | -117.0745 | 7.5918 | 181.0085 | 0.0173 | 0.0146 |
| 2024_09_20 22:00 | 3271022 | 4 | 14.7123 | 19.7464 | -116.5831 | 11.0101 | 111.1536 | 0.0034 | 0.0075 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413360_69D50D42 | 504990 | 265 | -105.9 | 504990 | 490 | -113.2 | 504990 | 156 | -118.3 | 504990 | 25 |
| MR_1774413360_15B74457 | 504990 | 265 | -106.7 | 504990 | 490 | -112.8 | 504990 | 156 | -120.5 | 504990 | 25 |
| MR_1774413360_EEEFBF6B | 504990 | 265 | -105.0 | 504990 | 490 | -112.5 | 504990 | 156 | -120.0 | 504990 | 25 |
| MR_1774413360_E8246AE5 | 504990 | 265 | -106.9 | 504990 | 490 | -114.6 | 504990 | 156 | -119.1 | 504990 | 25 |
| MR_1774413360_B435954C | 504990 | 265 | -106.6 | 504990 | 490 | -113.7 | 504990 | 156 | -117.9 | 504990 | 25 |
| MR_1774413360_3DD8792E | 504990 | 265 | -105.8 | 504990 | 490 | -112.1 | 504990 | 156 | -118.1 | 504990 | 25 |
| MR_1774413360_15931B43 | 504990 | 265 | -106.8 | 504990 | 490 | -114.1 | 504990 | 156 | -118.9 | 504990 | 25 |
| MR_1774413360_8A4E03D5 | 504990 | 265 | -108.0 | 504990 | 490 | -112.8 | 504990 | 156 | -117.1 | 504990 | 25 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 453: `1c74d960-256...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1c74d960-2569-4c38-8543-d371eeb1fc44` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease A3 Offset threshold for 3261120_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[453] topology](images/train_0453.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3261120_4
- `C2`: Add neighbor relationship between 3220988_3 and 3275687_2
- `C3`: Decrease A3 Offset threshold for 3261120_4 **← 정답**
- `C4`: Decrease A3 Offset threshold for 3275687_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275687_2
- `C6`: Increase transmission power for 3275687_2
- `C7`: Lift the tilt angle  of 3275687_2 by 10 degrees
- `C8`: Press down the tilt angle  of 3275687_2 by 10 degrees
- `C9`: Lift the tilt angle of 3261120_4 by 10 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275687_2
- `C11`: Check test server and transmission issues
- `C12`: Adjust the azimuth of 3261120_4 by 50 degrees
- `C13`: Increase transmission power for 3261120_4
- `C14`: Decrease transmission power for 3261120_4
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261120_4
- `C17`: Decrease transmission power for 3275687_2
- `C18`: Add neighbor relationship between 3261120_4 and 3275687_2
- `C19`: Press down the tilt angle of 3261120_4 by 10 degrees
- `C20`: Adjust the azimuth of 3275687_2 by 12 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261120_4
- `C22`: Increase A3 Offset threshold for 3275687_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.736 | MS1 | 121.4656603604 | 31.1446216662 | 181 | 504990 | -75.76 | 14.55 | 529.94 | 0.04 | 2.71 | 1595 |
| 2024-09-20 22:21:32.262 | MS1 | 121.4656597671 | 31.1446297933 | 181 | 504990 | -77.14 | 13.83 | 423.50 | 0.13 | 2.45 | 1571 |
| 2024-09-20 22:21:33.964 | MS1 | 121.4656709685 | 31.1446363699 | 181 | 504990 | -79.15 | 17.00 | 474.65 | 0.17 | 2.40 | 1562 |
| 2024-09-20 22:21:34.194 | MS1 | 121.4656765039 | 31.1446258070 | 181 | 504990 | -92.25 | -0.19 | 66.92 | 0.09 | 1.02 | 1583 |
| 2024-09-20 22:21:35.991 | MS1 | 121.4656742252 | 31.1446251721 | 181 | 504990 | -85.85 | -2.67 | 56.14 | 0.19 | 1.23 | 1575 |
| 2024-09-20 22:21:36.968 | MS1 | 121.4656580240 | 31.1446352215 | 181 | 504990 | -87.88 | -2.94 | 45.14 | 0.02 | 1.27 | 1576 |
| 2024-09-20 22:21:37.328 | MS1 | 121.4656654088 | 31.1446296029 | 181 | 504990 | -90.20 | -3.88 | 60.79 | 0.08 | 1.38 | 1592 |
| 2024-09-20 22:21:38.368 | MS1 | 121.4656648892 | 31.1446234594 | 181 | 504990 | -87.11 | -3.88 | 56.11 | 0.17 | 1.09 | 1595 |
| 2024-09-20 22:21:39.987 | MS1 | 121.4656583898 | 31.1446246104 | 348 | 504990 | -84.67 | 12.82 | 156.05 | 0.14 | 1.39 | 1562 |
| 2024-09-20 22:21:40.920 | MS1 | 121.4656638332 | 31.1446261643 | 348 | 504990 | -81.63 | 16.75 | 437.68 | 0.19 | 2.71 | 1586 |
| 2024-09-20 22:21:41.441 | MS1 | 121.4656705631 | 31.1446237564 | 348 | 504990 | -81.91 | 14.51 | 467.69 | 0.19 | 2.78 | 1597 |
| 2024-09-20 22:21:42.342 | MS1 | 121.4656669300 | 31.1446280503 | 348 | 504990 | -79.28 | 14.30 | 557.25 | 0.00 | 2.97 | 1598 |

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
| 3220988 | 3 | 121.4704788310 | 31.1521424762 | 358 | 15 | 10 | 39.8 | TDD | 501 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3258611 | 1 | 121.4685689662 | 31.1514921547 | 154 | 10 | 0 | 43.0 | TDD | 210 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3261120 | 4 | 121.4729180426 | 31.1445349273 | 151 | 10 | 0 | 21.5 | TDD | 181 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3275687 | 2 | 121.4754363885 | 31.1522477708 | 216 | 12 | 11 | 40.0 | TDD | 348 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.167 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.315 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.315 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.037 | NREventA3 | measId:2;ServCellPCI:375;Se... |
| 2024-09-20 22:21:38.277 | NRHandoverAttempt | SourcePCI:375;SourceNR-ARFC... |
| 2024-09-20 22:21:38.317 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.327 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.458 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.458 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258611 | 1 | 13.2286 | 11.7466 | -114.3828 | 15.6333 | 127.3730 | 0.0002 | 0.0070 |
| 2024_09_20 22:00 | 3275687 | 2 | 12.0829 | 6.9956 | -115.3169 | 7.8786 | 117.3490 | 0.0019 | 0.0120 |
| 2024_09_20 22:00 | 3220988 | 3 | 11.8949 | 10.5499 | -117.1481 | 15.0989 | 173.5931 | 0.0129 | 0.0006 |
| 2024_09_20 22:00 | 3261120 | 4 | 11.7535 | 14.6869 | -116.4420 | 19.3759 | 160.0478 | 0.0169 | 0.1132 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413583_F5431402 | 504990 | 181 | -92.2 | 504990 | 348 | -87.8 | 504990 | 501 | -95.4 | 504990 | 210 |
| MR_1774413583_B307F5A2 | 504990 | 181 | -93.4 | 504990 | 348 | -86.8 | 504990 | 501 | -92.7 | 504990 | 210 |
| MR_1774413583_704A0B41 | 504990 | 348 | -85.0 | 504990 | 181 | -93.1 | 504990 | 501 | -93.2 | 504990 | 210 |
| MR_1774413583_EBDD0B27 | 504990 | 348 | -88.3 | 504990 | 181 | -94.1 | 504990 | 501 | -95.8 | 504990 | 210 |
| MR_1774413583_C9A7AF55 | 504990 | 181 | -93.1 | 504990 | 348 | -88.3 | 504990 | 501 | -95.7 | 504990 | 210 |
| MR_1774413583_636847F3 | 504990 | 348 | -86.0 | 504990 | 181 | -92.9 | 504990 | 501 | -95.9 | 504990 | 210 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 454: `6d52fdce-823...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6d52fdce-8237-433f-a499-69eef371be48` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Add neighbor relationship between 3248861_3 and 3233401_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[454] topology](images/train_0454.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3248861_3 by 10 degrees
- `C2`: Decrease A3 Offset threshold for 3248861_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233401_1
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease transmission power for 3248861_3
- `C6`: Decrease transmission power for 3233401_1
- `C7`: Press down the tilt angle  of 3233401_1 by 5 degrees
- `C8`: Adjust the azimuth of 3233401_1 by 7 degrees
- `C9`: Increase transmission power for 3233401_1
- `C10`: Check test server and transmission issues
- `C11`: Lift the tilt angle of 3248861_3 by 10 degrees
- `C12`: Add neighbor relationship between 3248861_3 and 3233401_1 **← 정답**
- `C13`: Adjust the azimuth of 3248861_3 by 13 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233401_1
- `C15`: Increase A3 Offset threshold for 3233401_1
- `C16`: Lift the tilt angle  of 3233401_1 by 5 degrees
- `C17`: Add neighbor relationship between 3214704_2 and 3233401_1
- `C18`: Increase transmission power for 3248861_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248861_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248861_3
- `C21`: Decrease A3 Offset threshold for 3233401_1
- `C22`: Increase A3 Offset threshold for 3248861_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.423 | MS1 | 121.4656662419 | 31.1446304426 | 860 | 504990 | -82.03 | 13.92 | 315.91 | 0.03 | 2.95 | 1586 |
| 2024-09-20 22:21:32.478 | MS1 | 121.4656677978 | 31.1446349512 | 860 | 504990 | -78.69 | 13.54 | 474.04 | 0.02 | 2.35 | 1594 |
| 2024-09-20 22:21:33.873 | MS1 | 121.4656628837 | 31.1446186744 | 860 | 504990 | -79.80 | 17.73 | 466.21 | 0.07 | 2.38 | 1591 |
| 2024-09-20 22:21:34.503 | MS1 | 121.4656618599 | 31.1446264253 | 860 | 504990 | -94.15 | -1.35 | 59.59 | 0.05 | 1.29 | 1585 |
| 2024-09-20 22:21:35.946 | MS1 | 121.4656644783 | 31.1446342968 | 860 | 504990 | -88.14 | -2.88 | 74.69 | 0.01 | 1.07 | 1568 |
| 2024-09-20 22:21:36.715 | MS1 | 121.4656611855 | 31.1446212476 | 860 | 504990 | -87.79 | -1.68 | 69.63 | 0.00 | 1.04 | 1587 |
| 2024-09-20 22:21:37.735 | MS1 | 121.4656599801 | 31.1446341482 | 860 | 504990 | -88.11 | -3.68 | 47.33 | 0.18 | 1.34 | 1570 |
| 2024-09-20 22:21:38.388 | MS1 | 121.4656714619 | 31.1446312253 | 860 | 504990 | -84.72 | 14.89 | 486.36 | 0.11 | 1.32 | 1565 |
| 2024-09-20 22:21:39.806 | MS1 | 121.4656758403 | 31.1446272454 | 860 | 504990 | -79.47 | 14.23 | 347.04 | 0.18 | 1.27 | 1576 |
| 2024-09-20 22:21:40.125 | MS1 | 121.4656683571 | 31.1446218285 | 860 | 504990 | -80.60 | 13.47 | 579.28 | 0.08 | 2.09 | 1567 |
| 2024-09-20 22:21:41.430 | MS1 | 121.4656705446 | 31.1446325677 | 860 | 504990 | -77.15 | 13.29 | 524.60 | 0.04 | 2.54 | 1575 |
| 2024-09-20 22:21:42.335 | MS1 | 121.4656603074 | 31.1446354880 | 860 | 504990 | -82.47 | 13.17 | 486.71 | 0.15 | 2.16 | 1573 |

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
| 3214704 | 2 | 121.4684597567 | 31.1463534629 | 319 | 15 | 2 | 19.8 | TDD | 35 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3233401 | 1 | 121.4687131211 | 31.1474127113 | 230 | 0 | 12 | 38.7 | TDD | 370 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3244909 | 4 | 121.4748138022 | 31.1456762147 | 315 | 10 | 9 | 43.5 | TDD | 570 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3248861 | 3 | 121.4692128258 | 31.1539044627 | 211 | 9 | 3 | 36.7 | TDD | 860 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.987 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.004 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.115 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.115 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.789 | NREventA3 | measId:2;ServCellPCI:212;Se... |
| 2024-09-20 22:21:35.789 | NREventA3 | measId:2;ServCellPCI:212;Se... |
| 2024-09-20 22:21:36.789 | NREventA3 | measId:2;ServCellPCI:212;Se... |
| 2024-09-20 22:21:39.289 | NRRRCReestablishAttempt | PCI:212 |
| 2024-09-20 22:21:39.302 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.314 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.461 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.461 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233401 | 1 | 6.2701 | 12.5865 | -114.0355 | 16.6760 | 155.8833 | 0.0142 | 0.0122 |
| 2024_09_20 22:00 | 3214704 | 2 | 5.5265 | 6.3046 | -115.0365 | 10.8061 | 178.8583 | 0.0113 | 0.0077 |
| 2024_09_20 22:00 | 3248861 | 3 | 18.0919 | 11.5922 | -116.5741 | 9.2964 | 198.7524 | 0.0083 | 0.1858 |
| 2024_09_20 22:00 | 3244909 | 4 | 17.7585 | 14.2119 | -116.5304 | 19.4587 | 144.2152 | 0.0189 | 0.0013 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416973_8EAA5AA3 | 504990 | 860 | -94.0 | 504990 | 370 | -88.3 | 504990 | 35 | -99.3 | 504990 | 570 |
| MR_1774416973_E3A47FC1 | 504990 | 370 | -89.6 | 504990 | 860 | -93.5 | 504990 | 35 | -100.1 | 504990 | 570 |
| MR_1774416973_D24A4AC0 | 504990 | 860 | -92.4 | 504990 | 370 | -90.2 | 504990 | 35 | -97.4 | 504990 | 570 |
| MR_1774416973_23169B3B | 504990 | 370 | -90.7 | 504990 | 860 | -93.7 | 504990 | 35 | -96.8 | 504990 | 570 |
| MR_1774416973_BA4FF15E | 504990 | 370 | -88.7 | 504990 | 860 | -92.2 | 504990 | 35 | -97.2 | 504990 | 570 |
| MR_1774416973_875739C0 | 504990 | 370 | -90.8 | 504990 | 860 | -94.4 | 504990 | 35 | -99.3 | 504990 | 570 |
| MR_1774416973_42DF293D | 504990 | 860 | -95.0 | 504990 | 370 | -90.4 | 504990 | 35 | -97.5 | 504990 | 570 |
| MR_1774416973_FE00F058 | 504990 | 370 | -88.0 | 504990 | 860 | -92.2 | 504990 | 35 | -98.8 | 504990 | 570 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 455: `7d17a240-153...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7d17a240-153f-40c4-83ed-4262dd415ceb` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[455] topology](images/train_0455.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3268427_4 and 3244325_3
- `C2`: Increase transmission power for 3236412_1
- `C3`: Press down the tilt angle of 3236412_1 by 10 degrees
- `C4`: Lift the tilt angle  of 3244325_3 by 6 degrees
- `C5`: Lift the tilt angle of 3236412_1 by 10 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244325_3
- `C7`: Adjust the azimuth of 3244325_3 by 39 degrees
- `C8`: Decrease transmission power for 3244325_3
- `C9`: Adjust the azimuth of 3236412_1 by 8 degrees
- `C10`: Add neighbor relationship between 3236412_1 and 3244325_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244325_3
- `C12`: Decrease A3 Offset threshold for 3244325_3
- `C13`: Check test server and transmission issues
- `C14`: Increase transmission power for 3244325_3
- `C15`: Press down the tilt angle  of 3244325_3 by 6 degrees
- `C16`: Increase A3 Offset threshold for 3244325_3
- `C17`: Decrease transmission power for 3236412_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236412_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236412_1
- `C20`: Increase A3 Offset threshold for 3236412_1
- `C21`: Decrease A3 Offset threshold for 3236412_1
- `C22`: Insufficient data; more data is needed for judgment. **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.212 | MS1 | 121.4656756105 | 31.1446300086 | 11 | 504990 | -90.09 | 15.18 | 403.00 | 0.01 | 2.76 | 1570 |
| 2024-09-20 22:21:32.738 | MS1 | 121.4656597700 | 31.1446285846 | 11 | 504990 | -88.87 | 13.84 | 345.90 | 0.02 | 2.73 | 1560 |
| 2024-09-20 22:21:33.781 | MS1 | 121.4656639265 | 31.1446334507 | 11 | 504990 | -91.29 | 17.74 | 388.06 | 0.02 | 2.15 | 1583 |
| 2024-09-20 22:21:34.621 | MS1 | 121.4656738120 | 31.1446247403 | 11 | 504990 | -91.29 | 14.49 | 87.45 | 0.02 | 2.25 | 1561 |
| 2024-09-20 22:21:35.746 | MS1 | 121.4656645934 | 31.1446212045 | 11 | 504990 | -85.02 | 16.09 | 51.76 | 0.05 | 2.12 | 1579 |
| 2024-09-20 22:21:36.776 | MS1 | 121.4656628607 | 31.1446252906 | 11 | 504990 | -91.26 | 13.27 | 52.41 | 0.14 | 2.35 | 1583 |
| 2024-09-20 22:21:37.180 | MS1 | 121.4656717442 | 31.1446211696 | 11 | 504990 | -89.62 | 12.01 | 86.97 | 0.08 | 2.17 | 1594 |
| 2024-09-20 22:21:38.400 | MS1 | 121.4656757856 | 31.1446377805 | 11 | 504990 | -90.50 | 12.24 | 81.09 | 0.00 | 2.63 | 1585 |
| 2024-09-20 22:21:39.935 | MS1 | 121.4656626144 | 31.1446334285 | 11 | 504990 | -91.03 | 7.11 | 98.83 | 0.03 | 2.30 | 1566 |
| 2024-09-20 22:21:40.685 | MS1 | 121.4656591466 | 31.1446276977 | 11 | 504990 | -89.19 | 8.75 | 538.78 | 0.12 | 2.27 | 1576 |
| 2024-09-20 22:21:41.946 | MS1 | 121.4656615075 | 31.1446236539 | 11 | 504990 | -89.33 | 7.27 | 412.02 | 0.06 | 2.40 | 1575 |
| 2024-09-20 22:21:42.635 | MS1 | 121.4656762970 | 31.1446191565 | 11 | 504990 | -92.85 | 12.25 | 347.45 | 0.13 | 2.67 | 1590 |

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
| 3236412 | 1 | 121.4670602540 | 31.1549905136 | 195 | 9 | 12 | 24.6 | TDD | 11 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3244325 | 3 | 121.4731995567 | 31.1513991705 | 263 | 5 | 11 | 20.2 | TDD | 670 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3261546 | 2 | 121.4695175140 | 31.1521215304 | 83 | 6 | 0 | 45.1 | TDD | 877 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3268427 | 4 | 121.4655721070 | 31.1456015355 | 136 | 0 | 9 | 43.2 | TDD | 831 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.525 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.646 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.646 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.336 | NREventA3 | measId:2;ServCellPCI:15;Ser... |
| 2024-09-20 22:21:38.576 | NRHandoverAttempt | SourcePCI:15;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.620 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.631 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.745 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.745 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3236412 | 1 | 92.2789 | 94.9662 | -116.2376 | 18.5016 | 170.5749 | 0.0200 | 0.0111 |
| 2024_09_19 22:00 | 3261546 | 2 | 93.6934 | 88.1533 | -116.8250 | 17.6770 | 147.6137 | 0.0175 | 0.0090 |
| 2024_09_19 22:00 | 3244325 | 3 | 84.8521 | 82.5405 | -117.0267 | 10.8645 | 167.9992 | 0.0115 | 0.0069 |
| 2024_09_19 22:00 | 3268427 | 4 | 78.6101 | 88.1778 | -115.4969 | 17.4191 | 132.0963 | 0.0152 | 0.0077 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412107_129B06F1 | 504990 | 11 | -90.7 | 504990 | 670 | -93.7 | 504990 | 831 | -98.2 | 504990 | 877 |
| MR_1774412107_C2A21A74 | 504990 | 11 | -91.1 | 504990 | 670 | -94.8 | 504990 | 831 | -98.6 | 504990 | 877 |
| MR_1774412107_D7D21EC9 | 504990 | 11 | -93.0 | 504990 | 670 | -95.4 | 504990 | 831 | -99.1 | 504990 | 877 |
| MR_1774412107_B3B6B055 | 504990 | 11 | -92.7 | 504990 | 670 | -93.6 | 504990 | 831 | -95.6 | 504990 | 877 |
| MR_1774412107_32C3BDBE | 504990 | 11 | -91.6 | 504990 | 670 | -95.1 | 504990 | 831 | -98.6 | 504990 | 877 |
| MR_1774412107_04FF8249 | 504990 | 11 | -89.8 | 504990 | 670 | -93.6 | 504990 | 831 | -98.8 | 504990 | 877 |
| MR_1774412107_7CDABDB8 | 504990 | 11 | -90.5 | 504990 | 670 | -95.4 | 504990 | 831 | -95.9 | 504990 | 877 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 456: `d7537c71-27b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d7537c71-27b5-4b73-a116-7310d39c28ef` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[456] topology](images/train_0456.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218592_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218592_4
- `C4`: Increase A3 Offset threshold for 3253284_1
- `C5`: Decrease A3 Offset threshold for 3218592_4
- `C6`: Add neighbor relationship between 3253284_1 and 3218592_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253284_1
- `C8`: Lift the tilt angle of 3253284_1 by 5 degrees
- `C9`: Adjust the azimuth of 3253284_1 by 50 degrees
- `C10`: Add neighbor relationship between 3241482_2 and 3218592_4
- `C11`: Decrease A3 Offset threshold for 3253284_1
- `C12`: Increase A3 Offset threshold for 3218592_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253284_1
- `C14`: Adjust the azimuth of 3218592_4 by 4 degrees
- `C15`: Insufficient data; more data is needed for judgment. **← 정답**
- `C16`: Press down the tilt angle  of 3218592_4 by 10 degrees
- `C17`: Decrease transmission power for 3253284_1
- `C18`: Press down the tilt angle of 3253284_1 by 5 degrees
- `C19`: Increase transmission power for 3253284_1
- `C20`: Increase transmission power for 3218592_4
- `C21`: Lift the tilt angle  of 3218592_4 by 10 degrees
- `C22`: Decrease transmission power for 3218592_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.674 | MS1 | 121.4656705801 | 31.1446211293 | 857 | 504990 | -87.35 | 17.14 | 403.45 | 0.01 | 2.13 | 1582 |
| 2024-09-20 22:21:32.648 | MS1 | 121.4656754170 | 31.1446223463 | 857 | 504990 | -85.50 | 14.03 | 293.03 | 0.05 | 2.15 | 1588 |
| 2024-09-20 22:21:33.835 | MS1 | 121.4656611401 | 31.1446347129 | 857 | 504990 | -87.29 | 15.60 | 553.33 | 0.13 | 2.84 | 1598 |
| 2024-09-20 22:21:34.490 | MS1 | 121.4656632646 | 31.1446222402 | 857 | 504990 | -91.08 | 14.10 | 88.11 | 0.09 | 2.32 | 1565 |
| 2024-09-20 22:21:35.330 | MS1 | 121.4656604599 | 31.1446240394 | 857 | 504990 | -91.92 | 13.08 | 105.05 | 0.17 | 2.46 | 1595 |
| 2024-09-20 22:21:36.335 | MS1 | 121.4656674285 | 31.1446191941 | 857 | 504990 | -88.44 | 17.73 | 83.65 | 0.19 | 2.97 | 1589 |
| 2024-09-20 22:21:37.632 | MS1 | 121.4656752937 | 31.1446223411 | 857 | 504990 | -93.94 | 7.64 | 71.25 | 0.02 | 2.20 | 1570 |
| 2024-09-20 22:21:38.671 | MS1 | 121.4656735138 | 31.1446251826 | 857 | 504990 | -93.93 | 12.07 | 103.88 | 0.03 | 2.07 | 1576 |
| 2024-09-20 22:21:39.977 | MS1 | 121.4656648555 | 31.1446276960 | 857 | 504990 | -93.34 | 9.26 | 86.05 | 0.12 | 2.71 | 1572 |
| 2024-09-20 22:21:40.320 | MS1 | 121.4656580044 | 31.1446275090 | 857 | 504990 | -91.29 | 9.03 | 566.03 | 0.04 | 2.80 | 1591 |
| 2024-09-20 22:21:41.681 | MS1 | 121.4656717231 | 31.1446183410 | 857 | 504990 | -90.43 | 9.69 | 558.10 | 0.06 | 2.34 | 1561 |
| 2024-09-20 22:21:42.528 | MS1 | 121.4656766921 | 31.1446366497 | 857 | 504990 | -92.32 | 10.18 | 294.16 | 0.02 | 2.38 | 1567 |

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
| 3218592 | 4 | 121.4671701712 | 31.1445905691 | 267 | 4 | 1 | 29.6 | TDD | 823 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3241482 | 2 | 121.4756906288 | 31.1517234247 | 2 | 2 | 4 | 23.0 | TDD | 75 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3243358 | 3 | 121.4714556040 | 31.1528134672 | 353 | 5 | 2 | 20.4 | TDD | 726 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3253284 | 1 | 121.4710235774 | 31.1558859081 | 282 | 4 | 2 | 19.2 | TDD | 857 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.208 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.224 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.328 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.328 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.066 | NREventA3 | measId:2;ServCellPCI:792;Se... |
| 2024-09-20 22:21:38.306 | NRHandoverAttempt | SourcePCI:792;SourceNR-ARFC... |
| 2024-09-20 22:21:38.337 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.349 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.452 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.452 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3253284 | 1 | 88.7974 | 89.0878 | -115.0476 | 16.3183 | 185.2230 | 0.0131 | 0.0093 |
| 2024_09_19 22:00 | 3241482 | 2 | 85.6262 | 81.1003 | -114.2556 | 19.4646 | 120.2364 | 0.0122 | 0.0067 |
| 2024_09_19 22:00 | 3243358 | 3 | 92.7877 | 93.8144 | -117.3328 | 7.4325 | 148.2385 | 0.0026 | 0.0193 |
| 2024_09_19 22:00 | 3218592 | 4 | 89.0178 | 85.2296 | -116.6347 | 7.4906 | 120.2221 | 0.0102 | 0.0097 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416004_0D3609AF | 504990 | 857 | -92.6 | 504990 | 823 | -97.3 | 504990 | 75 | -101.3 | 504990 | 726 |
| MR_1774416004_FAA53E69 | 504990 | 857 | -91.9 | 504990 | 823 | -98.0 | 504990 | 75 | -99.4 | 504990 | 726 |
| MR_1774416004_ED3B85DE | 504990 | 857 | -89.5 | 504990 | 823 | -98.9 | 504990 | 75 | -100.8 | 504990 | 726 |
| MR_1774416004_B9159AC6 | 504990 | 857 | -90.1 | 504990 | 823 | -95.9 | 504990 | 75 | -101.4 | 504990 | 726 |
| MR_1774416004_8080DEB9 | 504990 | 857 | -91.4 | 504990 | 823 | -95.6 | 504990 | 75 | -101.3 | 504990 | 726 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 457: `496f7980-c90...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `496f7980-c907-4477-b08d-50688283621a` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252361_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[457] topology](images/train_0457.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3260500_5 by 1 degrees
- `C2`: Lift the tilt angle  of 3260500_5 by 1 degrees
- `C3`: Decrease A3 Offset threshold for 3260500_5
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260500_5
- `C5`: Increase transmission power for 3252361_1
- `C6`: Decrease A3 Offset threshold for 3252361_1
- `C7`: Decrease transmission power for 3260500_5
- `C8`: Increase A3 Offset threshold for 3260500_5
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252361_1 **← 정답**
- `C10`: Adjust the azimuth of 3252361_1 by 40 degrees
- `C11`: Press down the tilt angle of 3252361_1 by 3 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260500_5
- `C13`: Increase transmission power for 3260500_5
- `C14`: Adjust the azimuth of 3260500_5 by 13 degrees
- `C15`: Lift the tilt angle of 3252361_1 by 3 degrees
- `C16`: Add neighbor relationship between 3243767_11 and 3260500_5
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252361_1
- `C18`: Decrease transmission power for 3252361_1
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase A3 Offset threshold for 3252361_1
- `C21`: Add neighbor relationship between 3252361_1 and 3260500_5
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.880 | MS1 | 121.4656594562 | 31.1446294869 | 354 | 504990 | -93.03 | 13.68 | 385.27 | 0.01 | 2.94 | 1561 |
| 2024-09-20 22:21:32.312 | MS1 | 121.4656758041 | 31.1446250168 | 878 | 504990 | -93.57 | 10.04 | 366.90 | 0.07 | 2.90 | 1585 |
| 2024-09-20 22:21:33.182 | MS1 | 121.4656752321 | 31.1446349511 | 146 | 504990 | -94.46 | 9.03 | 556.18 | 0.17 | 2.31 | 1594 |
| 2024-09-20 22:21:34.798 | MS1 | 121.4656711745 | 31.1446251101 | 388 | 152650 | -93.52 | 6.54 | 70.05 | 0.16 | 1.99 | 928 |
| 2024-09-20 22:21:35.767 | MS1 | 121.4656619592 | 31.1446323716 | 480 | 152650 | -87.47 | 6.57 | 57.96 | 0.16 | 1.65 | 910 |
| 2024-09-20 22:21:36.339 | MS1 | 121.4656699804 | 31.1446373401 | 265 | 152650 | -87.52 | 7.04 | 65.86 | 0.18 | 1.51 | 976 |
| 2024-09-20 22:21:37.136 | MS1 | 121.4656615357 | 31.1446184747 | 207 | 152650 | -90.02 | 6.70 | 92.91 | 0.15 | 1.98 | 903 |
| 2024-09-20 22:21:38.515 | MS1 | 121.4656683628 | 31.1446319281 | 388 | 152650 | -91.76 | 5.40 | 45.50 | 0.13 | 1.97 | 950 |
| 2024-09-20 22:21:39.963 | MS1 | 121.4656728556 | 31.1446243168 | 480 | 152650 | -96.47 | 6.06 | 70.83 | 0.17 | 1.73 | 911 |
| 2024-09-20 22:21:40.754 | MS1 | 121.4656767039 | 31.1446262520 | 265 | 152650 | -90.62 | 7.41 | 56.61 | 0.08 | 2.61 | 1576 |
| 2024-09-20 22:21:41.372 | MS1 | 121.4656704889 | 31.1446324250 | 207 | 152650 | -89.88 | 5.64 | 85.80 | 0.15 | 2.82 | 1561 |
| 2024-09-20 22:21:42.969 | MS1 | 121.4656669725 | 31.1446368486 | 388 | 152650 | -93.95 | 2.81 | 85.38 | 0.15 | 2.17 | 1562 |

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
| 3216616 | 3 | 121.4745786348 | 31.1549366565 | 77 | 3 | 10 | 11.2 | TDD | 67 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3228176 | 6 | 121.4664442273 | 31.1546999908 | 126 | 5 | 9 | 3.7 | TDD | 146 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3232894 | 4 | 121.4695835857 | 31.1475994392 | 114 | 14 | 8 | 26.7 | TDD | 878 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3233351 | 10 | 121.4652035148 | 31.1512779298 | 104 | 8 | 0 | 10.5 | FDD | 388 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3242768 | 13 | 121.4698958336 | 31.1476262888 | 54 | 9 | 11 | 20.0 | FDD | 786 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3243767 | 11 | 121.4655686585 | 31.1528884376 | 155 | 9 | 3 | 23.1 | FDD | 265 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3250752 | 9 | 121.4719190986 | 31.1480736068 | 322 | 11 | 10 | 8.1 | FDD | 195 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3250870 | 2 | 121.4708634852 | 31.1471082654 | 28 | 7 | 11 | 2.6 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3251841 | 7 | 121.4732061694 | 31.1527873285 | 33 | 3 | 2 | 1.9 | FDD | 480 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3252361 | 1 | 121.4732201825 | 31.1499089390 | 191 | 2 | 3 | 17.9 | TDD | 354 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3253806 | 12 | 121.4726532715 | 31.1503681609 | 312 | 2 | 1 | 28.6 | FDD | 207 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3260500 | 5 | 121.4701858488 | 31.1533493612 | 217 | 0 | 1 | 12.4 | TDD | 943 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3263350 | 8 | 121.4677838584 | 31.1540065112 | 210 | 9 | 8 | 20.9 | FDD | 225 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |

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
| 2024-09-20 22:21:31.439 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.454 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.588 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.588 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.338 | NREventA2 | measId:1;ServCellPCI:261;Se... |
| 2024-09-20 22:21:35.439 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.689 | NREventA5 | measId:3;ServCellPCI:261;Se... |
| 2024-09-20 22:21:35.739 | NRHandoverAttempt | SourcePCI:261;SourceNR-ARFC... |
| 2024-09-20 22:21:35.780 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.794 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.903 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.903 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252361 | 1 | 7.7903 | 13.0216 | -115.1393 | 18.6554 | 110.4585 | 0.0087 | 0.0082 |
| 2024_09_20 22:00 | 3250870 | 2 | 9.1944 | 16.0001 | -114.6251 | 18.9229 | 161.1219 | 0.0046 | 0.0065 |
| 2024_09_20 22:00 | 3216616 | 3 | 19.6952 | 12.9545 | -116.9184 | 19.4987 | 81.3543 | 0.0015 | 0.0134 |
| 2024_09_20 22:00 | 3232894 | 4 | 19.5857 | 16.3837 | -116.8415 | 12.9069 | 176.3133 | 0.0056 | 0.0177 |
| 2024_09_20 22:00 | 3260500 | 5 | 6.1210 | 17.9935 | -114.7824 | 10.5950 | 181.8053 | 0.0078 | 0.0145 |
| 2024_09_20 22:00 | 3228176 | 6 | 6.1104 | 14.6544 | -116.3562 | 12.5952 | 172.1643 | 0.0065 | 0.0043 |
| 2024_09_20 22:00 | 3251841 | 7 | 8.4068 | 6.7371 | -114.6819 | 3.8395 | 25.3538 | 0.0092 | 0.0159 |
| 2024_09_20 22:00 | 3263350 | 8 | 15.9042 | 11.6984 | -114.0864 | 4.2147 | 43.0730 | 0.0198 | 0.0012 |
| 2024_09_20 22:00 | 3250752 | 9 | 6.4173 | 14.6191 | -114.8295 | 4.8183 | 45.2167 | 0.0190 | 0.0021 |
| 2024_09_20 22:00 | 3233351 | 10 | 17.8394 | 18.7354 | -116.1587 | 3.3650 | 37.4524 | 0.0086 | 0.0120 |
| 2024_09_20 22:00 | 3243767 | 11 | 18.6391 | 7.1626 | -116.3244 | 3.2174 | 43.7078 | 0.0088 | 0.0003 |
| 2024_09_20 22:00 | 3253806 | 12 | 8.8319 | 5.1642 | -114.5288 | 4.0564 | 57.3761 | 0.0128 | 0.0072 |
| 2024_09_20 22:00 | 3242768 | 13 | 6.6216 | 13.9356 | -115.9336 | 3.6720 | 39.7059 | 0.0135 | 0.0123 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412290_99331A15 | 504990 | 146 | -94.3 | 504990 | 943 | -94.5 | 504990 | 258 | -100.3 | 504990 | 67 |
| MR_1774412290_FA9B61BE | 504990 | 146 | -95.4 | 504990 | 943 | -93.8 | 504990 | 258 | -100.1 | 504990 | 67 |
| MR_1774412290_721587AB | 152650 | 388 | -94.3 | 152650 | 786 | -96.3 | 152650 | 195 | -103.3 | 152650 | 225 |
| MR_1774412290_F4854ADA | 152650 | 388 | -94.0 | 152650 | 786 | -96.4 | 152650 | 195 | -103.8 | 152650 | 225 |
| MR_1774412290_17399C3A | 504990 | 146 | -94.8 | 504990 | 943 | -93.7 | 504990 | 258 | -99.2 | 504990 | 67 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 458: `38af0020-779...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `38af0020-7790-412f-b655-ec649c652657` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3255392_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[458] topology](images/train_0458.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3255392_4 by 18 degrees
- `C2`: Lift the tilt angle of 3255392_4 by 3 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229187_1
- `C4`: Decrease transmission power for 3255392_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229187_1
- `C6`: Increase A3 Offset threshold for 3229187_1
- `C7`: Increase A3 Offset threshold for 3255392_4
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease A3 Offset threshold for 3255392_4
- `C10`: Add neighbor relationship between 3255392_4 and 3229187_1
- `C11`: Press down the tilt angle  of 3229187_1 by 10 degrees
- `C12`: Adjust the azimuth of 3229187_1 by 50 degrees
- `C13`: Press down the tilt angle of 3255392_4 by 3 degrees
- `C14`: Add neighbor relationship between 3212726_2 and 3229187_1
- `C15`: Lift the tilt angle  of 3229187_1 by 10 degrees
- `C16`: Decrease transmission power for 3229187_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255392_4 **← 정답**
- `C18`: Check test server and transmission issues
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255392_4
- `C20`: Increase transmission power for 3255392_4
- `C21`: Increase transmission power for 3229187_1
- `C22`: Decrease A3 Offset threshold for 3229187_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.764 | MS1 | 121.4656593168 | 31.1446266288 | 926 | 504990 | -86.22 | 15.01 | 471.66 | 0.09 | 2.20 | 1579 |
| 2024-09-20 22:21:32.505 | MS1 | 121.4656698629 | 31.1446335389 | 926 | 504990 | -88.50 | 17.09 | 594.33 | 0.02 | 2.09 | 1584 |
| 2024-09-20 22:21:33.674 | MS1 | 121.4656736851 | 31.1446264238 | 926 | 504990 | -88.19 | 13.65 | 548.51 | 0.19 | 2.59 | 1595 |
| 2024-09-20 22:21:34.981 | MS1 | 121.4656633776 | 31.1446362812 | 926 | 504990 | -91.47 | 12.62 | 98.20 | 0.58 | 2.17 | 577 |
| 2024-09-20 22:21:35.963 | MS1 | 121.4656615660 | 31.1446203717 | 926 | 504990 | -89.51 | 17.81 | 83.84 | 0.53 | 2.38 | 650 |
| 2024-09-20 22:21:36.732 | MS1 | 121.4656610298 | 31.1446312581 | 926 | 504990 | -87.70 | 12.13 | 101.86 | 0.64 | 2.92 | 536 |
| 2024-09-20 22:21:37.108 | MS1 | 121.4656623286 | 31.1446258288 | 926 | 504990 | -92.79 | 13.00 | 67.43 | 0.50 | 2.43 | 568 |
| 2024-09-20 22:21:38.708 | MS1 | 121.4656702974 | 31.1446332697 | 926 | 504990 | -90.06 | 9.73 | 62.59 | 0.54 | 2.11 | 605 |
| 2024-09-20 22:21:39.242 | MS1 | 121.4656749697 | 31.1446325403 | 926 | 504990 | -91.44 | 7.15 | 93.81 | 0.51 | 2.05 | 615 |
| 2024-09-20 22:21:40.256 | MS1 | 121.4656648640 | 31.1446336313 | 926 | 504990 | -90.76 | 11.19 | 514.56 | 0.18 | 2.51 | 1570 |
| 2024-09-20 22:21:41.243 | MS1 | 121.4656772679 | 31.1446371351 | 926 | 504990 | -92.44 | 8.97 | 478.42 | 0.19 | 2.23 | 1589 |
| 2024-09-20 22:21:42.699 | MS1 | 121.4656702102 | 31.1446375943 | 926 | 504990 | -93.73 | 8.72 | 399.23 | 0.05 | 2.62 | 1586 |

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
| 3212726 | 2 | 121.4690771943 | 31.1540451336 | 39 | 3 | 3 | 43.5 | TDD | 795 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3229187 | 1 | 121.4721947352 | 31.1475665173 | 359 | 11 | 3 | 26.8 | TDD | 736 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3246320 | 3 | 121.4700508002 | 31.1506780859 | 197 | 13 | 11 | 19.3 | TDD | 563 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3255392 | 4 | 121.4712895934 | 31.1532481031 | 227 | 2 | 6 | 15.9 | TDD | 926 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.339 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.354 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.472 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.472 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.231 | NREventA3 | measId:2;ServCellPCI:298;Se... |
| 2024-09-20 22:21:38.471 | NRHandoverAttempt | SourcePCI:298;SourceNR-ARFC... |
| 2024-09-20 22:21:38.504 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.517 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.638 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.638 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229187 | 1 | 19.1605 | 12.1131 | -115.4080 | 11.3624 | 157.2456 | 0.0022 | 0.0168 |
| 2024_09_20 22:00 | 3212726 | 2 | 10.3723 | 15.4880 | -115.9584 | 9.4966 | 199.5014 | 0.0104 | 0.0027 |
| 2024_09_20 22:00 | 3246320 | 3 | 9.5279 | 6.3996 | -115.4320 | 9.8750 | 93.2881 | 0.0182 | 0.0060 |
| 2024_09_20 22:00 | 3255392 | 4 | 17.4970 | 11.2646 | -115.3429 | 12.7861 | 91.3172 | 0.0079 | 0.0059 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413495_BA0D2EF3 | 504990 | 926 | -93.2 | 504990 | 736 | -91.0 | 504990 | 795 | -97.8 | 504990 | 563 |
| MR_1774413495_CACED5E9 | 504990 | 926 | -90.0 | 504990 | 736 | -91.5 | 504990 | 795 | -101.1 | 504990 | 563 |
| MR_1774413495_6839291A | 504990 | 926 | -91.8 | 504990 | 736 | -89.7 | 504990 | 795 | -99.1 | 504990 | 563 |
| MR_1774413495_9EECF354 | 504990 | 926 | -89.5 | 504990 | 736 | -92.0 | 504990 | 795 | -98.8 | 504990 | 563 |
| MR_1774413495_82FD9BC9 | 504990 | 926 | -90.4 | 504990 | 736 | -90.3 | 504990 | 795 | -99.3 | 504990 | 563 |
| MR_1774413495_E0D8ADD7 | 504990 | 926 | -91.6 | 504990 | 736 | -91.4 | 504990 | 795 | -98.6 | 504990 | 563 |
| MR_1774413495_AD1B4C8C | 504990 | 926 | -91.2 | 504990 | 736 | -90.2 | 504990 | 795 | -99.7 | 504990 | 563 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 459: `dc7fab49-aa3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dc7fab49-aa33-408a-92be-f181986238b6` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227167_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[459] topology](images/train_0459.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3274983_6 by 4 degrees
- `C2`: Increase A3 Offset threshold for 3227167_5
- `C3`: Increase transmission power for 3227167_5
- `C4`: Lift the tilt angle of 3227167_5 by 1 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Add neighbor relationship between 3211355_9 and 3274983_6
- `C7`: Decrease transmission power for 3274983_6
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274983_6
- `C9`: Increase transmission power for 3274983_6
- `C10`: Decrease A3 Offset threshold for 3227167_5
- `C11`: Increase A3 Offset threshold for 3274983_6
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274983_6
- `C13`: Press down the tilt angle of 3227167_5 by 1 degrees
- `C14`: Decrease transmission power for 3227167_5
- `C15`: Adjust the azimuth of 3274983_6 by 4 degrees
- `C16`: Add neighbor relationship between 3227167_5 and 3274983_6
- `C17`: Check test server and transmission issues
- `C18`: Decrease A3 Offset threshold for 3274983_6
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227167_5
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227167_5 **← 정답**
- `C21`: Adjust the azimuth of 3227167_5 by 21 degrees
- `C22`: Lift the tilt angle  of 3274983_6 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.791 | MS1 | 121.4656749634 | 31.1446266596 | 667 | 504990 | -95.42 | 13.50 | 336.76 | 0.06 | 2.39 | 1573 |
| 2024-09-20 22:21:32.471 | MS1 | 121.4656713547 | 31.1446198421 | 782 | 504990 | -95.37 | 9.90 | 421.79 | 0.17 | 2.95 | 1571 |
| 2024-09-20 22:21:33.109 | MS1 | 121.4656618187 | 31.1446219272 | 486 | 504990 | -94.67 | 13.39 | 416.29 | 0.03 | 2.93 | 1567 |
| 2024-09-20 22:21:34.854 | MS1 | 121.4656720724 | 31.1446200612 | 39 | 152650 | -93.23 | 2.72 | 84.71 | 0.02 | 1.70 | 909 |
| 2024-09-20 22:21:35.401 | MS1 | 121.4656657876 | 31.1446358490 | 743 | 152650 | -89.03 | 5.59 | 59.52 | 0.04 | 1.66 | 939 |
| 2024-09-20 22:21:36.887 | MS1 | 121.4656690470 | 31.1446296016 | 617 | 152650 | -95.35 | 4.22 | 68.54 | 0.03 | 1.61 | 905 |
| 2024-09-20 22:21:37.356 | MS1 | 121.4656759735 | 31.1446298051 | 431 | 152650 | -89.76 | 4.25 | 77.09 | 0.12 | 1.72 | 912 |
| 2024-09-20 22:21:38.286 | MS1 | 121.4656722408 | 31.1446363205 | 39 | 152650 | -88.95 | 4.91 | 53.02 | 0.17 | 1.73 | 916 |
| 2024-09-20 22:21:39.989 | MS1 | 121.4656746091 | 31.1446224661 | 743 | 152650 | -90.81 | 3.10 | 59.50 | 0.04 | 1.77 | 992 |
| 2024-09-20 22:21:40.786 | MS1 | 121.4656695673 | 31.1446279820 | 617 | 152650 | -87.10 | 5.63 | 66.59 | 0.13 | 2.61 | 1570 |
| 2024-09-20 22:21:41.468 | MS1 | 121.4656760265 | 31.1446247729 | 431 | 152650 | -93.30 | 3.16 | 87.18 | 0.00 | 2.03 | 1593 |
| 2024-09-20 22:21:42.840 | MS1 | 121.4656762922 | 31.1446254779 | 39 | 152650 | -93.43 | 4.73 | 76.75 | 0.14 | 2.97 | 1589 |

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
| 3211355 | 9 | 121.4748461211 | 31.1473879151 | 333 | 5 | 11 | 12.6 | FDD | 617 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3211501 | 10 | 121.4692982252 | 31.1558422317 | 270 | 6 | 7 | 4.1 | FDD | 554 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3215740 | 13 | 121.4697283849 | 31.1542154145 | 358 | 1 | 7 | 7.1 | FDD | 407 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3221851 | 2 | 121.4691503965 | 31.1493641470 | 65 | 10 | 10 | 3.6 | TDD | 486 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3227167 | 5 | 121.4720886227 | 31.1511314011 | 241 | 0 | 3 | 14.0 | TDD | 667 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3228210 | 12 | 121.4754335995 | 31.1519594258 | 202 | 5 | 5 | 6.3 | FDD | 341 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3240989 | 7 | 121.4746423633 | 31.1473374956 | 317 | 2 | 11 | 0.4 | FDD | 743 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3243531 | 8 | 121.4653859092 | 31.1480101501 | 258 | 7 | 9 | 15.9 | FDD | 39 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3253149 | 4 | 121.4736971926 | 31.1490635289 | 358 | 4 | 7 | 4.4 | TDD | 306 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3260309 | 3 | 121.4652313383 | 31.1446753426 | 49 | 10 | 8 | 27.5 | TDD | 782 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3274983 | 6 | 121.4744091547 | 31.1506812028 | 227 | 4 | 4 | 2.6 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3277040 | 1 | 121.4692071096 | 31.1533958960 | 320 | 6 | 9 | 12.1 | TDD | 869 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3278679 | 11 | 121.4690976808 | 31.1536294483 | 248 | 1 | 2 | 26.6 | FDD | 431 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |

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
| 2024-09-20 22:21:31.310 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.328 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.478 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.478 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.179 | NREventA2 | measId:1;ServCellPCI:800;Se... |
| 2024-09-20 22:21:35.302 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.579 | NREventA5 | measId:3;ServCellPCI:800;Se... |
| 2024-09-20 22:21:35.625 | NRHandoverAttempt | SourcePCI:800;SourceNR-ARFC... |
| 2024-09-20 22:21:35.674 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.688 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.795 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.795 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277040 | 1 | 15.6972 | 18.9036 | -114.3234 | 10.8408 | 177.9874 | 0.0056 | 0.0077 |
| 2024_09_20 22:00 | 3221851 | 2 | 5.4251 | 6.8362 | -115.8716 | 12.8067 | 137.2457 | 0.0126 | 0.0118 |
| 2024_09_20 22:00 | 3260309 | 3 | 17.1464 | 18.9848 | -117.3478 | 6.9822 | 164.9018 | 0.0052 | 0.0015 |
| 2024_09_20 22:00 | 3253149 | 4 | 16.6357 | 11.6906 | -116.7004 | 5.3925 | 81.8181 | 0.0137 | 0.0044 |
| 2024_09_20 22:00 | 3227167 | 5 | 19.4517 | 11.7599 | -116.9524 | 16.9937 | 194.9769 | 0.0127 | 0.0080 |
| 2024_09_20 22:00 | 3274983 | 6 | 8.8080 | 17.3461 | -116.2574 | 12.8107 | 180.8645 | 0.0017 | 0.0135 |
| 2024_09_20 22:00 | 3240989 | 7 | 11.9685 | 11.7916 | -116.9611 | 4.8251 | 20.0925 | 0.0131 | 0.0196 |
| 2024_09_20 22:00 | 3243531 | 8 | 11.2216 | 6.7750 | -114.4314 | 4.4831 | 32.6672 | 0.0044 | 0.0091 |
| 2024_09_20 22:00 | 3211355 | 9 | 17.0028 | 11.1369 | -116.8957 | 3.7359 | 36.9983 | 0.0164 | 0.0046 |
| 2024_09_20 22:00 | 3211501 | 10 | 7.1602 | 17.0805 | -114.5154 | 4.8864 | 24.2809 | 0.0058 | 0.0019 |
| 2024_09_20 22:00 | 3278679 | 11 | 11.6615 | 11.9785 | -115.3258 | 4.2572 | 44.5446 | 0.0155 | 0.0110 |
| 2024_09_20 22:00 | 3228210 | 12 | 7.8231 | 17.7256 | -115.7383 | 3.2274 | 42.4395 | 0.0121 | 0.0051 |
| 2024_09_20 22:00 | 3215740 | 13 | 19.1334 | 15.9776 | -114.3712 | 3.0682 | 25.0917 | 0.0070 | 0.0074 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415319_A9EF7067 | 504990 | 486 | -95.4 | 504990 | 382 | -91.0 | 504990 | 306 | -100.7 | 504990 | 869 |
| MR_1774415319_F3A9C6D8 | 504990 | 486 | -96.1 | 504990 | 382 | -91.4 | 504990 | 306 | -102.4 | 504990 | 869 |
| MR_1774415319_DC93D07C | 504990 | 486 | -93.4 | 504990 | 382 | -93.2 | 504990 | 306 | -100.7 | 504990 | 869 |
| MR_1774415319_83E1EAE7 | 504990 | 486 | -96.3 | 504990 | 382 | -89.8 | 504990 | 306 | -101.9 | 504990 | 869 |
| MR_1774415319_15413663 | 152650 | 39 | -91.3 | 152650 | 554 | -99.2 | 152650 | 407 | -100.6 | 152650 | 341 |
| MR_1774415319_117F34F3 | 504990 | 486 | -94.4 | 504990 | 382 | -91.6 | 504990 | 306 | -102.4 | 504990 | 869 |
| MR_1774415319_BE8087A8 | 504990 | 486 | -93.4 | 504990 | 382 | -89.8 | 504990 | 306 | -102.4 | 504990 | 869 |

> *... 2개 열 생략 (전체 14열)*

---
