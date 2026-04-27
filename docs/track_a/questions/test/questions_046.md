# Track A 문제 분석 — test[450]~test[459]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[450] ~ test[459] (10개)

## 목차

1. [문제 450: `cea6a945-03a...`](#450) — single-answer
2. [문제 451: `4cfe0816-ced...`](#451) — single-answer
3. [문제 452: `bd45cfcc-078...`](#452) — single-answer
4. [문제 453: `97c0218f-91c...`](#453) — single-answer
5. [문제 454: `b25a3f95-073...`](#454) — single-answer
6. [문제 455: `d1cf0274-e71...`](#455) — single-answer
7. [문제 456: `5b81cf32-74f...`](#456) — single-answer
8. [문제 457: `b8b8ac25-094...`](#457) — single-answer
9. [문제 458: `2e8837d5-777...`](#458) — multiple-answer
10. [문제 459: `f2e50ae6-693...`](#459) — single-answer

---

### 문제 450: `cea6a945-03a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cea6a945-03a2-42f1-b6f4-4a024bff4c6d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[450] topology](images/test_0450.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3227481_6 by 48 degrees
- `C2`: Decrease A3 Offset threshold for 3251590_1
- `C3`: Decrease transmission power for 3251590_1
- `C4`: Add neighbor relationship between 3219390_10 and 3227481_6
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227481_6
- `C6`: Increase A3 Offset threshold for 3251590_1
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease A3 Offset threshold for 3227481_6
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251590_1
- `C10`: Lift the tilt angle of 3251590_1 by 2 degrees
- `C11`: Increase transmission power for 3251590_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227481_6
- `C13`: Lift the tilt angle  of 3227481_6 by 4 degrees
- `C14`: Press down the tilt angle  of 3227481_6 by 4 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251590_1
- `C16`: Decrease transmission power for 3227481_6
- `C17`: Check test server and transmission issues
- `C18`: Add neighbor relationship between 3251590_1 and 3227481_6
- `C19`: Increase A3 Offset threshold for 3227481_6
- `C20`: Press down the tilt angle of 3251590_1 by 2 degrees
- `C21`: Increase transmission power for 3227481_6
- `C22`: Adjust the azimuth of 3251590_1 by 33 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.608 | MS1 | 121.4656708872 | 31.1446291075 | 64 | 504990 | -95.41 | 9.96 | 384.88 | 0.13 | 2.92 | 1564 |
| 2024-09-20 22:21:32.294 | MS1 | 121.4656638750 | 31.1446333438 | 896 | 504990 | -95.79 | 14.98 | 571.47 | 0.15 | 2.29 | 1568 |
| 2024-09-20 22:21:33.296 | MS1 | 121.4656694478 | 31.1446241606 | 784 | 504990 | -93.32 | 11.15 | 389.51 | 0.05 | 2.88 | 1574 |
| 2024-09-20 22:21:34.999 | MS1 | 121.4656707494 | 31.1446191977 | 810 | 152650 | -95.00 | 7.44 | 86.55 | 0.08 | 1.58 | 993 |
| 2024-09-20 22:21:35.702 | MS1 | 121.4656703892 | 31.1446286430 | 580 | 152650 | -93.51 | 5.65 | 60.87 | 0.10 | 1.63 | 904 |
| 2024-09-20 22:21:36.662 | MS1 | 121.4656682846 | 31.1446261117 | 856 | 152650 | -87.08 | 2.99 | 56.30 | 0.11 | 1.81 | 952 |
| 2024-09-20 22:21:37.742 | MS1 | 121.4656696425 | 31.1446353262 | 733 | 152650 | -92.34 | 5.61 | 100.80 | 0.03 | 1.78 | 924 |
| 2024-09-20 22:21:38.844 | MS1 | 121.4656701388 | 31.1446222012 | 810 | 152650 | -88.24 | 5.22 | 70.17 | 0.08 | 1.93 | 908 |
| 2024-09-20 22:21:39.507 | MS1 | 121.4656635218 | 31.1446200808 | 580 | 152650 | -96.18 | 3.99 | 79.51 | 0.05 | 1.74 | 921 |
| 2024-09-20 22:21:40.833 | MS1 | 121.4656733317 | 31.1446277220 | 856 | 152650 | -90.08 | 2.34 | 85.26 | 0.08 | 2.09 | 1571 |
| 2024-09-20 22:21:41.325 | MS1 | 121.4656610007 | 31.1446355491 | 733 | 152650 | -91.16 | 3.41 | 64.90 | 0.07 | 2.23 | 1568 |
| 2024-09-20 22:21:42.203 | MS1 | 121.4656608921 | 31.1446244137 | 810 | 152650 | -89.01 | 6.16 | 79.35 | 0.14 | 2.29 | 1590 |

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
| 3210839 | 9 | 121.4722900566 | 31.1468875354 | 120 | 15 | 4 | 4.3 | FDD | 460 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3212508 | 5 | 121.4758656632 | 31.1461821876 | 103 | 14 | 11 | 4.3 | TDD | 469 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3219390 | 10 | 121.4697594638 | 31.1458524413 | 81 | 3 | 10 | 8.6 | FDD | 856 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3227481 | 6 | 121.4694983404 | 31.1447738240 | 315 | 2 | 1 | 14.9 | TDD | 408 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3235737 | 2 | 121.4650879402 | 31.1444696227 | 320 | 0 | 10 | 0.4 | TDD | 896 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3242334 | 7 | 121.4658890338 | 31.1547815621 | 33 | 14 | 11 | 8.7 | FDD | 580 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3243591 | 11 | 121.4694099212 | 31.1448096117 | 94 | 13 | 4 | 2.7 | FDD | 345 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3244687 | 12 | 121.4752661473 | 31.1474163828 | 347 | 4 | 2 | 20.2 | FDD | 733 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3248509 | 8 | 121.4737432539 | 31.1529084889 | 27 | 7 | 7 | 14.9 | FDD | 810 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3251590 | 1 | 121.4726652704 | 31.1542053861 | 245 | 1 | 9 | 29.0 | TDD | 64 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3259833 | 4 | 121.4641358003 | 31.1502579427 | 125 | 8 | 10 | 7.9 | TDD | 784 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3260339 | 3 | 121.4647219904 | 31.1467796473 | 296 | 5 | 9 | 10.2 | TDD | 643 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3276096 | 13 | 121.4714950532 | 31.1445971867 | 156 | 14 | 6 | 1.6 | FDD | 927 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |

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
| 2024-09-20 22:21:30.760 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.783 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.907 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.907 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.644 | NREventA2 | measId:1;ServCellPCI:472;Se... |
| 2024-09-20 22:21:34.777 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.045 | NREventA5 | measId:3;ServCellPCI:472;Se... |
| 2024-09-20 22:21:35.119 | NRHandoverAttempt | SourcePCI:472;SourceNR-ARFC... |
| 2024-09-20 22:21:35.166 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.177 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.316 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.316 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251590 | 1 | 5.9390 | 16.1684 | -115.7471 | 9.7678 | 140.6260 | 0.0040 | 0.0148 |
| 2024_09_20 22:00 | 3235737 | 2 | 8.3304 | 5.8638 | -116.7890 | 17.8632 | 96.5654 | 0.0073 | 0.0099 |
| 2024_09_20 22:00 | 3260339 | 3 | 16.3660 | 12.3915 | -116.9514 | 19.7800 | 157.8558 | 0.0017 | 0.0086 |
| 2024_09_20 22:00 | 3259833 | 4 | 5.4589 | 14.5123 | -114.6295 | 14.3199 | 141.8146 | 0.0064 | 0.0154 |
| 2024_09_20 22:00 | 3212508 | 5 | 11.9187 | 12.1138 | -116.0337 | 6.5413 | 88.8872 | 0.0164 | 0.0180 |
| 2024_09_20 22:00 | 3227481 | 6 | 9.0767 | 16.8695 | -114.7892 | 13.9449 | 107.4168 | 0.0008 | 0.0131 |
| 2024_09_20 22:00 | 3242334 | 7 | 16.3610 | 11.0987 | -117.0728 | 4.2299 | 31.8135 | 0.0115 | 0.0146 |
| 2024_09_20 22:00 | 3248509 | 8 | 6.7362 | 6.9072 | -117.9539 | 4.2594 | 28.3960 | 0.0001 | 0.0056 |
| 2024_09_20 22:00 | 3210839 | 9 | 6.2972 | 12.9368 | -114.3794 | 4.6009 | 28.1138 | 0.0114 | 0.0079 |
| 2024_09_20 22:00 | 3219390 | 10 | 12.4813 | 7.0069 | -116.9292 | 3.5353 | 33.2104 | 0.0092 | 0.0177 |
| 2024_09_20 22:00 | 3243591 | 11 | 15.9414 | 12.2597 | -116.8795 | 4.9394 | 52.1868 | 0.0174 | 0.0163 |
| 2024_09_20 22:00 | 3244687 | 12 | 7.1776 | 14.5996 | -115.3568 | 4.1090 | 38.0908 | 0.0078 | 0.0171 |
| 2024_09_20 22:00 | 3276096 | 13 | 16.8879 | 19.1267 | -116.9449 | 4.6987 | 54.3666 | 0.0115 | 0.0081 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414038_EF6D2CD6 | 152650 | 810 | -93.6 | 152650 | 927 | -96.8 | 152650 | 460 | -104.0 | 152650 | 345 |
| MR_1774414038_58C99E4C | 152650 | 810 | -96.3 | 152650 | 927 | -96.0 | 152650 | 460 | -103.0 | 152650 | 345 |
| MR_1774414038_41B1BB58 | 504990 | 784 | -91.4 | 504990 | 408 | -96.3 | 504990 | 643 | -95.2 | 504990 | 469 |
| MR_1774414038_F9994B4E | 152650 | 810 | -96.6 | 152650 | 927 | -97.0 | 152650 | 460 | -103.3 | 152650 | 345 |
| MR_1774414038_11F7202B | 152650 | 810 | -96.1 | 152650 | 927 | -98.4 | 152650 | 460 | -101.6 | 152650 | 345 |
| MR_1774414038_C5DF87F6 | 152650 | 810 | -95.5 | 152650 | 927 | -95.9 | 152650 | 460 | -102.1 | 152650 | 345 |
| MR_1774414038_3C834771 | 152650 | 810 | -93.3 | 152650 | 927 | -99.1 | 152650 | 460 | -102.8 | 152650 | 345 |
| MR_1774414038_834EB549 | 504990 | 784 | -92.1 | 504990 | 408 | -96.1 | 504990 | 643 | -95.5 | 504990 | 469 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 451: `4cfe0816-ced...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4cfe0816-ced9-4d7b-ade7-cb27a46c97b0` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[451] topology](images/test_0451.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3247170_2 by 10 degrees
- `C2`: Increase transmission power for 3259519_1
- `C3`: Adjust the azimuth of 3247170_2 by 50 degrees
- `C4`: Lift the tilt angle  of 3259519_1 by 10 degrees
- `C5`: Add neighbor relationship between 3221465_4 and 3259519_1
- `C6`: Increase transmission power for 3247170_2
- `C7`: Decrease transmission power for 3259519_1
- `C8`: Decrease A3 Offset threshold for 3259519_1
- `C9`: Decrease transmission power for 3247170_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Check test server and transmission issues
- `C12`: Adjust the azimuth of 3259519_1 by 50 degrees
- `C13`: Increase A3 Offset threshold for 3247170_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247170_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259519_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259519_1
- `C17`: Increase A3 Offset threshold for 3259519_1
- `C18`: Add neighbor relationship between 3247170_2 and 3259519_1
- `C19`: Decrease A3 Offset threshold for 3247170_2
- `C20`: Press down the tilt angle  of 3259519_1 by 10 degrees
- `C21`: Lift the tilt angle of 3247170_2 by 10 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247170_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.754 | MS1 | 121.4656761157 | 31.1446238600 | 138 | 504990 | -88.67 | 16.36 | 602.88 | 0.20 | 2.84 | 1591 |
| 2024-09-20 22:21:32.959 | MS1 | 121.4656620679 | 31.1446291753 | 138 | 504990 | -87.65 | 16.53 | 419.90 | 0.09 | 2.37 | 1596 |
| 2024-09-20 22:21:33.869 | MS1 | 121.4656753510 | 31.1446271422 | 138 | 504990 | -89.47 | 17.61 | 426.62 | 0.16 | 2.67 | 1597 |
| 2024-09-20 22:21:34.166 | MS1 | 121.4656693300 | 31.1446251668 | 138 | 504990 | -90.53 | 16.71 | 51.01 | 0.06 | 2.34 | 412 |
| 2024-09-20 22:21:35.582 | MS1 | 121.4656745159 | 31.1446313982 | 138 | 504990 | -85.57 | 14.69 | 84.51 | 0.11 | 2.85 | 327 |
| 2024-09-20 22:21:36.290 | MS1 | 121.4656708849 | 31.1446338342 | 138 | 504990 | -86.75 | 15.76 | 78.75 | 0.02 | 2.06 | 476 |
| 2024-09-20 22:21:37.669 | MS1 | 121.4656688823 | 31.1446350227 | 138 | 504990 | -93.33 | 10.96 | 68.87 | 0.15 | 2.66 | 472 |
| 2024-09-20 22:21:38.515 | MS1 | 121.4656663510 | 31.1446250395 | 138 | 504990 | -92.77 | 9.03 | 77.22 | 0.15 | 2.93 | 343 |
| 2024-09-20 22:21:39.348 | MS1 | 121.4656591117 | 31.1446199607 | 138 | 504990 | -93.73 | 8.61 | 72.33 | 0.12 | 2.88 | 435 |
| 2024-09-20 22:21:40.159 | MS1 | 121.4656596432 | 31.1446297858 | 138 | 504990 | -93.25 | 12.86 | 389.11 | 0.04 | 2.73 | 1567 |
| 2024-09-20 22:21:41.113 | MS1 | 121.4656620530 | 31.1446318113 | 138 | 504990 | -89.34 | 8.93 | 369.69 | 0.12 | 2.62 | 1572 |
| 2024-09-20 22:21:42.724 | MS1 | 121.4656653137 | 31.1446204776 | 138 | 504990 | -92.97 | 12.29 | 463.28 | 0.08 | 2.07 | 1575 |

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
| 3221465 | 4 | 121.4653033873 | 31.1540269611 | 276 | 4 | 4 | 31.6 | TDD | 215 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3247170 | 2 | 121.4647913095 | 31.1506757654 | 341 | 12 | 0 | 27.1 | TDD | 138 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3253850 | 3 | 121.4731456586 | 31.1474268337 | 279 | 9 | 8 | 27.0 | TDD | 142 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3259519 | 1 | 121.4688825955 | 31.1518494705 | 53 | 13 | 5 | 24.5 | TDD | 128 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.218 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.241 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.370 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.370 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.042 | NREventA3 | measId:2;ServCellPCI:719;Se... |
| 2024-09-20 22:21:38.282 | NRHandoverAttempt | SourcePCI:719;SourceNR-ARFC... |
| 2024-09-20 22:21:38.323 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.333 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.433 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.433 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259519 | 1 | 9.6223 | 17.8022 | -114.5056 | 10.5778 | 128.4598 | 0.0089 | 0.0049 |
| 2024_09_20 22:00 | 3247170 | 2 | 11.8054 | 19.9367 | -115.7442 | 7.0336 | 181.3754 | 0.0138 | 0.0002 |
| 2024_09_20 22:00 | 3253850 | 3 | 8.6032 | 17.2106 | -117.1958 | 13.4895 | 84.5995 | 0.0179 | 0.0092 |
| 2024_09_20 22:00 | 3221465 | 4 | 5.8541 | 7.4506 | -115.2285 | 8.1162 | 141.6710 | 0.0074 | 0.0200 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414805_81488E02 | 504990 | 138 | -92.1 | 504990 | 128 | -92.1 | 504990 | 215 | -99.8 | 504990 | 142 |
| MR_1774414805_F0EFFD6E | 504990 | 138 | -91.5 | 504990 | 128 | -92.0 | 504990 | 215 | -99.9 | 504990 | 142 |
| MR_1774414805_CE3E997D | 504990 | 138 | -91.2 | 504990 | 128 | -93.3 | 504990 | 215 | -98.5 | 504990 | 142 |
| MR_1774414805_8B13117B | 504990 | 138 | -88.9 | 504990 | 128 | -93.5 | 504990 | 215 | -97.4 | 504990 | 142 |
| MR_1774414805_5A57B77D | 504990 | 138 | -91.7 | 504990 | 128 | -94.2 | 504990 | 215 | -100.4 | 504990 | 142 |
| MR_1774414805_D7694BFB | 504990 | 138 | -91.2 | 504990 | 128 | -92.6 | 504990 | 215 | -97.6 | 504990 | 142 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 452: `bd45cfcc-078...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bd45cfcc-0780-42f3-b110-28d7e43d8b2b` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[452] topology](images/test_0452.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3255577_1
- `C2`: Lift the tilt angle of 3219576_4 by 3 degrees
- `C3`: Decrease A3 Offset threshold for 3255577_1
- `C4`: Decrease transmission power for 3219576_4
- `C5`: Lift the tilt angle  of 3232587_2 by 10 degrees
- `C6`: Decrease A3 Offset threshold for 3219576_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255577_1
- `C8`: Check test server and transmission issues
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255577_1
- `C10`: Add neighbor relationship between 3232587_2 and 3255577_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219576_4
- `C12`: Increase A3 Offset threshold for 3219576_4
- `C13`: Increase transmission power for 3219576_4
- `C14`: Add neighbor relationship between 3219576_4 and 3255577_1
- `C15`: Press down the tilt angle of 3219576_4 by 3 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Adjust the azimuth of 3232587_2 by 50 degrees
- `C18`: Adjust the azimuth of 3219576_4 by 29 degrees
- `C19`: Press down the tilt angle  of 3232587_2 by 10 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219576_4
- `C21`: Increase transmission power for 3255577_1
- `C22`: Increase A3 Offset threshold for 3255577_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.985 | MS1 | 121.4656680196 | 31.1446233751 | 213 | 504990 | -90.62 | 13.16 | 352.79 | 0.07 | 2.74 | 1572 |
| 2024-09-20 22:21:32.402 | MS1 | 121.4656696772 | 31.1446309666 | 213 | 504990 | -89.88 | 14.41 | 602.67 | 0.12 | 2.67 | 1587 |
| 2024-09-20 22:21:33.929 | MS1 | 121.4656620735 | 31.1446271551 | 213 | 504990 | -86.00 | 13.25 | 541.73 | 0.08 | 2.34 | 1574 |
| 2024-09-20 22:21:34.230 | MS1 | 121.4656772104 | 31.1446348640 | 213 | 504990 | -90.60 | 15.79 | 68.61 | 0.16 | 2.25 | 1582 |
| 2024-09-20 22:21:35.483 | MS1 | 121.4656711856 | 31.1446194534 | 213 | 504990 | -86.46 | 17.44 | 74.81 | 0.03 | 2.55 | 1563 |
| 2024-09-20 22:21:36.995 | MS1 | 121.4656740826 | 31.1446270034 | 213 | 504990 | -88.00 | 15.03 | 65.76 | 0.16 | 2.59 | 1578 |
| 2024-09-20 22:21:37.644 | MS1 | 121.4656741954 | 31.1446199322 | 213 | 504990 | -90.07 | 7.33 | 99.64 | 0.11 | 2.72 | 1582 |
| 2024-09-20 22:21:38.213 | MS1 | 121.4656677905 | 31.1446376083 | 213 | 504990 | -94.00 | 10.96 | 99.22 | 0.03 | 2.04 | 1575 |
| 2024-09-20 22:21:39.215 | MS1 | 121.4656606937 | 31.1446310770 | 213 | 504990 | -90.49 | 8.80 | 102.22 | 0.16 | 2.99 | 1593 |
| 2024-09-20 22:21:40.614 | MS1 | 121.4656745583 | 31.1446317122 | 213 | 504990 | -90.57 | 9.54 | 552.82 | 0.14 | 2.31 | 1584 |
| 2024-09-20 22:21:41.413 | MS1 | 121.4656647364 | 31.1446211943 | 213 | 504990 | -90.16 | 10.70 | 332.05 | 0.20 | 2.56 | 1598 |
| 2024-09-20 22:21:42.170 | MS1 | 121.4656657551 | 31.1446234936 | 213 | 504990 | -92.31 | 12.77 | 364.30 | 0.12 | 2.72 | 1583 |

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
| 3219576 | 4 | 121.4645683284 | 31.1513460475 | 143 | 1 | 10 | 27.7 | TDD | 213 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3232587 | 2 | 121.4699988790 | 31.1505692642 | 341 | 0 | 5 | 36.2 | TDD | 706 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3255577 | 1 | 121.4755303832 | 31.1513174317 | 141 | 9 | 3 | 24.8 | TDD | 496 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3260387 | 3 | 121.4745924876 | 31.1474962125 | 19 | 3 | 8 | 36.8 | TDD | 67 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.576 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.595 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.721 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.721 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.378 | NREventA3 | measId:2;ServCellPCI:522;Se... |
| 2024-09-20 22:21:38.618 | NRHandoverAttempt | SourcePCI:522;SourceNR-ARFC... |
| 2024-09-20 22:21:38.666 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.681 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.815 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.815 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255577 | 1 | 13.0773 | 9.1793 | -114.7027 | 12.3980 | 149.7342 | 0.0069 | 0.0009 |
| 2024_09_20 22:00 | 3232587 | 2 | 7.2616 | 19.9965 | -117.7286 | 9.3077 | 163.6362 | 0.0110 | 0.0042 |
| 2024_09_20 22:00 | 3260387 | 3 | 16.4274 | 10.5429 | -115.3470 | 10.9469 | 190.8720 | 0.0192 | 0.0067 |
| 2024_09_20 22:00 | 3219576 | 4 | 85.2738 | 76.5019 | -116.2036 | 10.1117 | 150.2157 | 0.0013 | 0.0104 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414044_7DDB99B6 | 504990 | 213 | -89.6 | 504990 | 496 | -93.5 | 504990 | 706 | -102.2 | 504990 | 67 |
| MR_1774414044_0A57CC08 | 504990 | 213 | -91.6 | 504990 | 496 | -90.4 | 504990 | 706 | -104.1 | 504990 | 67 |
| MR_1774414044_23F885A7 | 504990 | 213 | -92.4 | 504990 | 496 | -92.2 | 504990 | 706 | -103.1 | 504990 | 67 |
| MR_1774414044_71081150 | 504990 | 213 | -89.7 | 504990 | 496 | -93.0 | 504990 | 706 | -104.7 | 504990 | 67 |
| MR_1774414044_FB17759E | 504990 | 213 | -91.4 | 504990 | 496 | -94.2 | 504990 | 706 | -104.1 | 504990 | 67 |
| MR_1774414044_30DE73A1 | 504990 | 213 | -92.2 | 504990 | 496 | -93.4 | 504990 | 706 | -105.1 | 504990 | 67 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 453: `97c0218f-91c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `97c0218f-91c5-4382-b371-59dd9eb8138d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[453] topology](images/test_0453.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Lift the tilt angle  of 3262151_2 by 9 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase A3 Offset threshold for 3235381_1
- `C5`: Decrease transmission power for 3235381_1
- `C6`: Press down the tilt angle of 3235381_1 by 6 degrees
- `C7`: Adjust the azimuth of 3235381_1 by 50 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262151_2
- `C9`: Lift the tilt angle of 3235381_1 by 6 degrees
- `C10`: Decrease transmission power for 3262151_2
- `C11`: Add neighbor relationship between 3235381_1 and 3262151_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235381_1
- `C13`: Increase A3 Offset threshold for 3262151_2
- `C14`: Decrease A3 Offset threshold for 3235381_1
- `C15`: Add neighbor relationship between 3252885_4 and 3262151_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262151_2
- `C17`: Decrease A3 Offset threshold for 3262151_2
- `C18`: Adjust the azimuth of 3262151_2 by 50 degrees
- `C19`: Increase transmission power for 3262151_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235381_1
- `C21`: Press down the tilt angle  of 3262151_2 by 9 degrees
- `C22`: Increase transmission power for 3235381_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.228 | MS1 | 121.4656641522 | 31.1446310742 | 553 | 504990 | -91.22 | 12.34 | 374.37 | 0.04 | 2.37 | 1590 |
| 2024-09-20 22:21:32.895 | MS1 | 121.4656772902 | 31.1446265049 | 553 | 504990 | -88.31 | 13.35 | 447.34 | 0.17 | 2.78 | 1587 |
| 2024-09-20 22:21:33.534 | MS1 | 121.4656600456 | 31.1446281204 | 553 | 504990 | -85.79 | 17.68 | 341.90 | 0.01 | 2.96 | 1589 |
| 2024-09-20 22:21:34.695 | MS1 | 121.4656648544 | 31.1446348673 | 553 | 504990 | -88.48 | 12.39 | 59.69 | 0.11 | 2.78 | 1596 |
| 2024-09-20 22:21:35.307 | MS1 | 121.4656675611 | 31.1446204957 | 553 | 504990 | -90.52 | 13.24 | 91.60 | 0.02 | 2.29 | 1586 |
| 2024-09-20 22:21:36.125 | MS1 | 121.4656677365 | 31.1446197470 | 553 | 504990 | -89.92 | 15.82 | 93.47 | 0.02 | 2.52 | 1599 |
| 2024-09-20 22:21:37.108 | MS1 | 121.4656765346 | 31.1446368277 | 553 | 504990 | -92.08 | 11.34 | 88.40 | 0.18 | 2.24 | 1598 |
| 2024-09-20 22:21:38.216 | MS1 | 121.4656643433 | 31.1446281341 | 553 | 504990 | -91.03 | 8.98 | 71.44 | 0.10 | 2.32 | 1598 |
| 2024-09-20 22:21:39.456 | MS1 | 121.4656702759 | 31.1446293987 | 553 | 504990 | -93.12 | 10.75 | 73.96 | 0.11 | 2.50 | 1569 |
| 2024-09-20 22:21:40.847 | MS1 | 121.4656657903 | 31.1446307959 | 553 | 504990 | -93.40 | 12.33 | 339.25 | 0.15 | 2.98 | 1590 |
| 2024-09-20 22:21:41.570 | MS1 | 121.4656689341 | 31.1446186029 | 553 | 504990 | -92.92 | 12.73 | 568.01 | 0.02 | 2.83 | 1588 |
| 2024-09-20 22:21:42.316 | MS1 | 121.4656615976 | 31.1446356537 | 553 | 504990 | -89.58 | 12.04 | 375.15 | 0.19 | 2.76 | 1568 |

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
| 3235381 | 1 | 121.4690581186 | 31.1555174502 | 281 | 5 | 5 | 30.1 | TDD | 553 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3252885 | 4 | 121.4729946152 | 31.1477614697 | 92 | 5 | 11 | 33.7 | TDD | 316 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3262151 | 2 | 121.4725918273 | 31.1541633621 | 307 | 8 | 12 | 20.2 | TDD | 556 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3263444 | 3 | 121.4680379591 | 31.1481524078 | 156 | 11 | 4 | 22.8 | TDD | 653 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.905 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.923 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.024 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.024 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.705 | NREventA3 | measId:2;ServCellPCI:357;Se... |
| 2024-09-20 22:21:37.945 | NRHandoverAttempt | SourcePCI:357;SourceNR-ARFC... |
| 2024-09-20 22:21:37.975 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.990 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.107 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.107 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3235381 | 1 | 80.0973 | 93.2718 | -117.2310 | 14.3903 | 89.7070 | 0.0169 | 0.0099 |
| 2024_09_19 22:00 | 3262151 | 2 | 89.2839 | 90.8310 | -115.8935 | 8.2833 | 143.4221 | 0.0107 | 0.0156 |
| 2024_09_19 22:00 | 3263444 | 3 | 88.0642 | 92.3249 | -115.2696 | 12.4429 | 121.6359 | 0.0138 | 0.0083 |
| 2024_09_19 22:00 | 3252885 | 4 | 92.1103 | 89.8611 | -117.3172 | 10.8168 | 84.3256 | 0.0071 | 0.0118 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415210_BD8314D8 | 504990 | 553 | -86.8 | 504990 | 556 | -90.3 | 504990 | 316 | -94.6 | 504990 | 653 |
| MR_1774415210_0A192310 | 504990 | 553 | -88.5 | 504990 | 556 | -89.3 | 504990 | 316 | -94.3 | 504990 | 653 |
| MR_1774415210_FD3547D8 | 504990 | 553 | -89.0 | 504990 | 556 | -88.5 | 504990 | 316 | -93.1 | 504990 | 653 |
| MR_1774415210_15573813 | 504990 | 553 | -89.0 | 504990 | 556 | -88.6 | 504990 | 316 | -94.8 | 504990 | 653 |
| MR_1774415210_DB5D7867 | 504990 | 553 | -90.2 | 504990 | 556 | -90.2 | 504990 | 316 | -96.4 | 504990 | 653 |
| MR_1774415210_AAC3941D | 504990 | 553 | -89.8 | 504990 | 556 | -91.4 | 504990 | 316 | -93.7 | 504990 | 653 |
| MR_1774415210_82F603A9 | 504990 | 553 | -88.3 | 504990 | 556 | -90.7 | 504990 | 316 | -93.6 | 504990 | 653 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 454: `b25a3f95-073...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b25a3f95-073f-43a0-8322-87a13871a6de` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[454] topology](images/test_0454.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256087_2
- `C2`: Decrease A3 Offset threshold for 3228478_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256087_2
- `C4`: Add neighbor relationship between 3256087_2 and 3228478_1
- `C5`: Check test server and transmission issues
- `C6`: Decrease transmission power for 3228478_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228478_1
- `C8`: Adjust the azimuth of 3256087_2 by 50 degrees
- `C9`: Adjust the azimuth of 3228478_1 by 37 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228478_1
- `C12`: Press down the tilt angle of 3256087_2 by 10 degrees
- `C13`: Increase transmission power for 3256087_2
- `C14`: Lift the tilt angle  of 3228478_1 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3256087_2
- `C16`: Decrease transmission power for 3256087_2
- `C17`: Increase transmission power for 3228478_1
- `C18`: Lift the tilt angle of 3256087_2 by 10 degrees
- `C19`: Press down the tilt angle  of 3228478_1 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3256087_2
- `C21`: Add neighbor relationship between 3240088_4 and 3228478_1
- `C22`: Increase A3 Offset threshold for 3228478_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.353 | MS1 | 121.4656779922 | 31.1446188316 | 707 | 504990 | -84.60 | 15.17 | 430.98 | 0.12 | 2.99 | 1597 |
| 2024-09-20 22:21:32.278 | MS1 | 121.4656665119 | 31.1446288058 | 707 | 504990 | -76.82 | 15.91 | 530.20 | 0.18 | 2.88 | 1576 |
| 2024-09-20 22:21:33.375 | MS1 | 121.4656658485 | 31.1446350359 | 707 | 504990 | -76.45 | 13.37 | 395.46 | 0.14 | 2.21 | 1575 |
| 2024-09-20 22:21:34.663 | MS1 | 121.4656694761 | 31.1446355811 | 707 | 504990 | -83.26 | -0.50 | 39.76 | 0.03 | 1.36 | 1587 |
| 2024-09-20 22:21:35.387 | MS1 | 121.4656590443 | 31.1446364170 | 707 | 504990 | -88.72 | -2.22 | 51.52 | 0.11 | 1.42 | 1571 |
| 2024-09-20 22:21:36.223 | MS1 | 121.4656582381 | 31.1446192519 | 707 | 504990 | -85.96 | -1.88 | 39.11 | 0.00 | 1.22 | 1566 |
| 2024-09-20 22:21:37.659 | MS1 | 121.4656697564 | 31.1446325525 | 707 | 504990 | -86.20 | -1.11 | 51.07 | 0.06 | 1.01 | 1581 |
| 2024-09-20 22:21:38.416 | MS1 | 121.4656687634 | 31.1446369320 | 707 | 504990 | -84.14 | -0.41 | 55.98 | 0.10 | 1.27 | 1561 |
| 2024-09-20 22:21:39.917 | MS1 | 121.4656631395 | 31.1446320911 | 592 | 504990 | -83.79 | 13.24 | 155.37 | 0.01 | 1.18 | 1597 |
| 2024-09-20 22:21:40.256 | MS1 | 121.4656614681 | 31.1446300818 | 592 | 504990 | -82.70 | 14.48 | 493.27 | 0.15 | 2.18 | 1573 |
| 2024-09-20 22:21:41.245 | MS1 | 121.4656619322 | 31.1446188349 | 592 | 504990 | -84.15 | 15.18 | 564.26 | 0.02 | 2.99 | 1588 |
| 2024-09-20 22:21:42.592 | MS1 | 121.4656704456 | 31.1446341209 | 592 | 504990 | -75.06 | 12.22 | 373.86 | 0.07 | 2.08 | 1584 |

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
| 3228478 | 1 | 121.4656196069 | 31.1467679907 | 142 | 7 | 7 | 17.0 | TDD | 592 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3240088 | 4 | 121.4645711709 | 31.1526142816 | 154 | 15 | 11 | 18.6 | TDD | 231 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3256087 | 2 | 121.4688216245 | 31.1454197025 | 19 | 4 | 8 | 42.5 | TDD | 707 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3262038 | 3 | 121.4645551337 | 31.1467080517 | 324 | 12 | 8 | 25.6 | TDD | 532 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.212 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.212 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.970 | NREventA3 | measId:2;ServCellPCI:240;Se... |
| 2024-09-20 22:21:38.210 | NRHandoverAttempt | SourcePCI:240;SourceNR-ARFC... |
| 2024-09-20 22:21:38.244 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.254 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.372 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.372 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228478 | 1 | 8.4329 | 13.6459 | -114.7421 | 11.5915 | 98.7475 | 0.0140 | 0.0026 |
| 2024_09_20 22:00 | 3256087 | 2 | 5.6566 | 16.9123 | -116.0740 | 9.5241 | 145.0527 | 0.0157 | 0.1026 |
| 2024_09_20 22:00 | 3262038 | 3 | 18.0544 | 12.3604 | -116.9894 | 9.1349 | 124.7953 | 0.0146 | 0.0139 |
| 2024_09_20 22:00 | 3240088 | 4 | 10.8982 | 19.8649 | -114.1276 | 19.7483 | 152.8674 | 0.0154 | 0.0166 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414091_E12FB933 | 504990 | 707 | -81.7 | 504990 | 592 | -74.9 | 504990 | 231 | -77.7 | 504990 | 532 |
| MR_1774414091_A3E04457 | 504990 | 592 | -77.8 | 504990 | 707 | -83.9 | 504990 | 231 | -79.2 | 504990 | 532 |
| MR_1774414091_9410FD12 | 504990 | 707 | -82.3 | 504990 | 592 | -77.0 | 504990 | 231 | -80.5 | 504990 | 532 |
| MR_1774414091_6DD67159 | 504990 | 707 | -82.6 | 504990 | 592 | -76.0 | 504990 | 231 | -77.2 | 504990 | 532 |
| MR_1774414091_357C1CD7 | 504990 | 707 | -83.1 | 504990 | 592 | -75.8 | 504990 | 231 | -80.1 | 504990 | 532 |
| MR_1774414091_4B457303 | 504990 | 707 | -84.0 | 504990 | 592 | -77.1 | 504990 | 231 | -78.6 | 504990 | 532 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 455: `d1cf0274-e71...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d1cf0274-e713-4252-97b6-dd6ff0e20e1a` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[455] topology](images/test_0455.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3237055_1 and 3221389_3
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase transmission power for 3237055_1
- `C4`: Press down the tilt angle of 3237055_1 by 10 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237055_1
- `C6`: Decrease A3 Offset threshold for 3221389_3
- `C7`: Press down the tilt angle  of 3221389_3 by 10 degrees
- `C8`: Increase A3 Offset threshold for 3221389_3
- `C9`: Increase transmission power for 3221389_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237055_1
- `C11`: Lift the tilt angle of 3237055_1 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221389_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221389_3
- `C14`: Lift the tilt angle  of 3221389_3 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3237055_1
- `C16`: Check test server and transmission issues
- `C17`: Decrease transmission power for 3221389_3
- `C18`: Adjust the azimuth of 3221389_3 by 50 degrees
- `C19`: Increase A3 Offset threshold for 3237055_1
- `C20`: Adjust the azimuth of 3237055_1 by 25 degrees
- `C21`: Decrease transmission power for 3237055_1
- `C22`: Add neighbor relationship between 3253760_4 and 3221389_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.619 | MS1 | 121.4656633462 | 31.1446238077 | 237 | 504990 | -88.74 | 13.13 | 452.41 | 0.05 | 2.52 | 1595 |
| 2024-09-20 22:21:32.133 | MS1 | 121.4656660116 | 31.1446341668 | 237 | 504990 | -85.87 | 12.87 | 440.32 | 0.17 | 2.67 | 1572 |
| 2024-09-20 22:21:33.360 | MS1 | 121.4656637649 | 31.1446334164 | 237 | 504990 | -88.48 | 15.33 | 587.28 | 0.09 | 2.10 | 1571 |
| 2024-09-20 22:21:34.714 | MS1 | 121.4656598265 | 31.1446235955 | 237 | 504990 | -89.55 | 17.95 | 65.88 | 0.14 | 2.02 | 338 |
| 2024-09-20 22:21:35.582 | MS1 | 121.4656691105 | 31.1446242006 | 237 | 504990 | -85.59 | 12.71 | 56.68 | 0.07 | 2.56 | 389 |
| 2024-09-20 22:21:36.619 | MS1 | 121.4656597487 | 31.1446297825 | 237 | 504990 | -91.62 | 14.54 | 102.48 | 0.11 | 2.09 | 472 |
| 2024-09-20 22:21:37.496 | MS1 | 121.4656704613 | 31.1446206032 | 237 | 504990 | -93.57 | 9.42 | 61.89 | 0.18 | 2.24 | 395 |
| 2024-09-20 22:21:38.426 | MS1 | 121.4656665088 | 31.1446193393 | 237 | 504990 | -89.41 | 10.44 | 81.89 | 0.14 | 2.22 | 493 |
| 2024-09-20 22:21:39.528 | MS1 | 121.4656723435 | 31.1446194172 | 237 | 504990 | -89.82 | 8.27 | 72.31 | 0.18 | 2.35 | 455 |
| 2024-09-20 22:21:40.639 | MS1 | 121.4656711133 | 31.1446228710 | 237 | 504990 | -91.66 | 12.49 | 590.97 | 0.06 | 2.24 | 1581 |
| 2024-09-20 22:21:41.891 | MS1 | 121.4656599083 | 31.1446265433 | 237 | 504990 | -89.51 | 11.75 | 352.97 | 0.01 | 2.98 | 1585 |
| 2024-09-20 22:21:42.853 | MS1 | 121.4656668692 | 31.1446280517 | 237 | 504990 | -90.34 | 7.33 | 419.84 | 0.02 | 2.02 | 1567 |

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
| 3221389 | 3 | 121.4663869274 | 31.1485347448 | 20 | 14 | 11 | 44.8 | TDD | 60 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3221710 | 2 | 121.4648589564 | 31.1526276643 | 307 | 8 | 7 | 36.5 | TDD | 675 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3237055 | 1 | 121.4737714677 | 31.1529560950 | 245 | 11 | 9 | 22.9 | TDD | 237 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3253760 | 4 | 121.4705903124 | 31.1476897192 | 99 | 9 | 7 | 46.6 | TDD | 597 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.414 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.430 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.574 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.574 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.225 | NREventA3 | measId:2;ServCellPCI:262;Se... |
| 2024-09-20 22:21:38.465 | NRHandoverAttempt | SourcePCI:262;SourceNR-ARFC... |
| 2024-09-20 22:21:38.503 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.517 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.658 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.658 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237055 | 1 | 16.2677 | 13.4344 | -116.3023 | 7.0092 | 154.1286 | 0.0180 | 0.0189 |
| 2024_09_20 22:00 | 3221710 | 2 | 13.9422 | 17.4284 | -117.5111 | 9.5922 | 88.4656 | 0.0145 | 0.0044 |
| 2024_09_20 22:00 | 3221389 | 3 | 7.1608 | 11.4352 | -116.3932 | 11.4195 | 105.2765 | 0.0080 | 0.0178 |
| 2024_09_20 22:00 | 3253760 | 4 | 18.2915 | 15.2960 | -115.5418 | 17.8457 | 152.4686 | 0.0046 | 0.0097 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416981_5DCCF916 | 504990 | 237 | -88.5 | 504990 | 60 | -98.8 | 504990 | 597 | -97.1 | 504990 | 675 |
| MR_1774416981_423D819F | 504990 | 237 | -91.0 | 504990 | 60 | -95.9 | 504990 | 597 | -99.8 | 504990 | 675 |
| MR_1774416981_078427C5 | 504990 | 237 | -91.0 | 504990 | 60 | -96.4 | 504990 | 597 | -100.2 | 504990 | 675 |
| MR_1774416981_8298D1A7 | 504990 | 237 | -87.7 | 504990 | 60 | -95.5 | 504990 | 597 | -99.5 | 504990 | 675 |
| MR_1774416981_69F3D7F3 | 504990 | 237 | -90.9 | 504990 | 60 | -95.0 | 504990 | 597 | -98.0 | 504990 | 675 |
| MR_1774416981_EA9C3EC5 | 504990 | 237 | -89.7 | 504990 | 60 | -98.1 | 504990 | 597 | -98.5 | 504990 | 675 |
| MR_1774416981_BB503122 | 504990 | 237 | -90.5 | 504990 | 60 | -97.2 | 504990 | 597 | -99.8 | 504990 | 675 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 456: `5b81cf32-74f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5b81cf32-74f6-409f-8ce5-28bcc1cf1952` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[456] topology](images/test_0456.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3273469_1 by 1 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273469_1
- `C3`: Increase transmission power for 3275842_4
- `C4`: Decrease transmission power for 3275842_4
- `C5`: Decrease transmission power for 3273469_1
- `C6`: Check test server and transmission issues
- `C7`: Press down the tilt angle of 3273469_1 by 1 degrees
- `C8`: Decrease A3 Offset threshold for 3273469_1
- `C9`: Add neighbor relationship between 3273469_1 and 3275842_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273469_1
- `C11`: Increase A3 Offset threshold for 3275842_4
- `C12`: Press down the tilt angle  of 3275842_4 by 6 degrees
- `C13`: Adjust the azimuth of 3273469_1 by 6 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Adjust the azimuth of 3275842_4 by 50 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275842_4
- `C17`: Increase A3 Offset threshold for 3273469_1
- `C18`: Increase transmission power for 3273469_1
- `C19`: Add neighbor relationship between 3224839_2 and 3275842_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275842_4
- `C21`: Lift the tilt angle  of 3275842_4 by 6 degrees
- `C22`: Decrease A3 Offset threshold for 3275842_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.130 | MS1 | 121.4656709641 | 31.1446316907 | 995 | 504990 | -86.42 | 17.36 | 338.77 | 0.15 | 2.37 | 1573 |
| 2024-09-20 22:21:32.567 | MS1 | 121.4656638566 | 31.1446312891 | 995 | 504990 | -86.87 | 16.89 | 501.75 | 0.17 | 2.22 | 1594 |
| 2024-09-20 22:21:33.859 | MS1 | 121.4656751153 | 31.1446328310 | 995 | 504990 | -88.89 | 16.65 | 438.93 | 0.02 | 2.69 | 1564 |
| 2024-09-20 22:21:34.290 | MS1 | 121.4656763355 | 31.1446296364 | 995 | 504990 | -89.60 | 12.66 | 74.65 | 0.58 | 2.89 | 564 |
| 2024-09-20 22:21:35.191 | MS1 | 121.4656743502 | 31.1446240792 | 995 | 504990 | -89.15 | 12.07 | 79.04 | 0.51 | 2.11 | 590 |
| 2024-09-20 22:21:36.768 | MS1 | 121.4656647592 | 31.1446310705 | 995 | 504990 | -89.36 | 13.45 | 82.14 | 0.68 | 2.64 | 687 |
| 2024-09-20 22:21:37.333 | MS1 | 121.4656750043 | 31.1446224709 | 995 | 504990 | -93.26 | 7.94 | 89.41 | 0.55 | 2.91 | 636 |
| 2024-09-20 22:21:38.214 | MS1 | 121.4656609420 | 31.1446339965 | 995 | 504990 | -93.48 | 12.49 | 58.71 | 0.58 | 2.37 | 593 |
| 2024-09-20 22:21:39.485 | MS1 | 121.4656612150 | 31.1446304935 | 995 | 504990 | -89.22 | 8.83 | 75.36 | 0.69 | 2.03 | 522 |
| 2024-09-20 22:21:40.939 | MS1 | 121.4656727068 | 31.1446318178 | 995 | 504990 | -91.99 | 9.59 | 518.14 | 0.00 | 2.99 | 1568 |
| 2024-09-20 22:21:41.182 | MS1 | 121.4656603392 | 31.1446298775 | 995 | 504990 | -93.93 | 8.23 | 512.26 | 0.11 | 2.58 | 1564 |
| 2024-09-20 22:21:42.267 | MS1 | 121.4656726241 | 31.1446184953 | 995 | 504990 | -93.81 | 11.42 | 517.79 | 0.16 | 2.06 | 1600 |

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
| 3224418 | 3 | 121.4720201021 | 31.1512192975 | 234 | 2 | 9 | 47.5 | TDD | 422 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3224839 | 2 | 121.4652198542 | 31.1553129920 | 308 | 0 | 10 | 44.2 | TDD | 4 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3273469 | 1 | 121.4686416525 | 31.1535385410 | 190 | 0 | 3 | 20.3 | TDD | 995 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3275842 | 4 | 121.4690647899 | 31.1547639060 | 345 | 5 | 1 | 23.9 | TDD | 951 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.784 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.806 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.907 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.907 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.607 | NREventA3 | measId:2;ServCellPCI:125;Se... |
| 2024-09-20 22:21:37.847 | NRHandoverAttempt | SourcePCI:125;SourceNR-ARFC... |
| 2024-09-20 22:21:37.885 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.896 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.040 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.040 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273469 | 1 | 7.3717 | 12.1813 | -117.9531 | 11.4817 | 159.4178 | 0.0169 | 0.0125 |
| 2024_09_20 22:00 | 3224839 | 2 | 15.6450 | 12.3643 | -116.9402 | 6.9880 | 89.8535 | 0.0033 | 0.0119 |
| 2024_09_20 22:00 | 3224418 | 3 | 13.0241 | 6.8726 | -116.4165 | 8.6523 | 152.3546 | 0.0186 | 0.0182 |
| 2024_09_20 22:00 | 3275842 | 4 | 11.9492 | 10.4391 | -115.7482 | 6.4194 | 161.0022 | 0.0190 | 0.0077 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412627_2EA21AF5 | 504990 | 995 | -87.8 | 504990 | 951 | -97.5 | 504990 | 4 | -100.8 | 504990 | 422 |
| MR_1774412627_71687540 | 504990 | 995 | -90.2 | 504990 | 951 | -96.8 | 504990 | 4 | -101.9 | 504990 | 422 |
| MR_1774412627_5B0D3229 | 504990 | 995 | -90.3 | 504990 | 951 | -96.5 | 504990 | 4 | -102.6 | 504990 | 422 |
| MR_1774412627_B6E05F42 | 504990 | 995 | -91.3 | 504990 | 951 | -100.2 | 504990 | 4 | -102.7 | 504990 | 422 |
| MR_1774412627_B65332E3 | 504990 | 995 | -90.4 | 504990 | 951 | -97.6 | 504990 | 4 | -101.0 | 504990 | 422 |
| MR_1774412627_E6D0F903 | 504990 | 995 | -88.9 | 504990 | 951 | -99.7 | 504990 | 4 | -100.1 | 504990 | 422 |
| MR_1774412627_2212006D | 504990 | 995 | -90.4 | 504990 | 951 | -100.2 | 504990 | 4 | -102.3 | 504990 | 422 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 457: `b8b8ac25-094...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b8b8ac25-0944-41ec-a668-c9b1e861f9cc` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[457] topology](images/test_0457.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3276599_4
- `C2`: Adjust the azimuth of 3213298_3 by 50 degrees
- `C3`: Decrease A3 Offset threshold for 3213298_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276599_4
- `C5`: Increase transmission power for 3213298_3
- `C6`: Check test server and transmission issues
- `C7`: Adjust the azimuth of 3276599_4 by 50 degrees
- `C8`: Decrease A3 Offset threshold for 3276599_4
- `C9`: Add neighbor relationship between 3276599_4 and 3213298_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276599_4
- `C11`: Lift the tilt angle  of 3213298_3 by 4 degrees
- `C12`: Increase A3 Offset threshold for 3213298_3
- `C13`: Add neighbor relationship between 3222599_1 and 3213298_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213298_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213298_3
- `C16`: Press down the tilt angle  of 3213298_3 by 4 degrees
- `C17`: Lift the tilt angle of 3276599_4 by 5 degrees
- `C18`: Decrease transmission power for 3276599_4
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Press down the tilt angle of 3276599_4 by 5 degrees
- `C21`: Increase transmission power for 3276599_4
- `C22`: Decrease transmission power for 3213298_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.443 | MS1 | 121.4656676907 | 31.1446329976 | 167 | 504990 | -75.79 | 16.49 | 468.58 | 0.04 | 2.93 | 1562 |
| 2024-09-20 22:21:32.112 | MS1 | 121.4656738873 | 31.1446183491 | 167 | 504990 | -78.02 | 13.62 | 580.72 | 0.04 | 2.30 | 1588 |
| 2024-09-20 22:21:33.824 | MS1 | 121.4656585037 | 31.1446278107 | 167 | 504990 | -81.08 | 15.61 | 451.09 | 0.09 | 2.84 | 1575 |
| 2024-09-20 22:21:34.738 | MS1 | 121.4656700456 | 31.1446222239 | 167 | 504990 | -86.53 | -1.80 | 81.30 | 0.12 | 1.23 | 1564 |
| 2024-09-20 22:21:35.140 | MS1 | 121.4656656397 | 31.1446230509 | 167 | 504990 | -86.19 | -0.83 | 31.37 | 0.03 | 1.18 | 1564 |
| 2024-09-20 22:21:36.343 | MS1 | 121.4656677272 | 31.1446302249 | 167 | 504990 | -89.41 | -0.65 | 59.76 | 0.18 | 1.38 | 1592 |
| 2024-09-20 22:21:37.513 | MS1 | 121.4656602577 | 31.1446234576 | 167 | 504990 | -89.68 | -2.65 | 48.90 | 0.19 | 1.02 | 1579 |
| 2024-09-20 22:21:38.318 | MS1 | 121.4656743084 | 31.1446280201 | 167 | 504990 | -92.64 | -1.48 | 51.20 | 0.06 | 1.21 | 1569 |
| 2024-09-20 22:21:39.294 | MS1 | 121.4656710844 | 31.1446215589 | 150 | 504990 | -76.87 | 13.50 | 277.19 | 0.19 | 1.23 | 1564 |
| 2024-09-20 22:21:40.274 | MS1 | 121.4656688599 | 31.1446213658 | 150 | 504990 | -77.58 | 15.72 | 471.23 | 0.05 | 2.74 | 1585 |
| 2024-09-20 22:21:41.893 | MS1 | 121.4656593711 | 31.1446204722 | 150 | 504990 | -84.96 | 15.65 | 487.30 | 0.19 | 2.41 | 1581 |
| 2024-09-20 22:21:42.332 | MS1 | 121.4656643798 | 31.1446317483 | 150 | 504990 | -75.50 | 14.59 | 325.43 | 0.14 | 2.31 | 1593 |

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
| 3213298 | 3 | 121.4736180190 | 31.1547247537 | 98 | 3 | 10 | 25.7 | TDD | 150 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3222599 | 1 | 121.4702152856 | 31.1466105313 | 76 | 1 | 8 | 31.5 | TDD | 872 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3225722 | 2 | 121.4646136963 | 31.1531262673 | 337 | 5 | 11 | 28.3 | TDD | 348 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3276599 | 4 | 121.4710473464 | 31.1499428926 | 22 | 2 | 3 | 44.0 | TDD | 167 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.384 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.400 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.540 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.540 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.195 | NREventA3 | measId:2;ServCellPCI:981;Se... |
| 2024-09-20 22:21:38.435 | NRHandoverAttempt | SourcePCI:981;SourceNR-ARFC... |
| 2024-09-20 22:21:38.474 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.489 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.593 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.593 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222599 | 1 | 12.4749 | 15.5094 | -116.7727 | 5.4608 | 146.9077 | 0.0083 | 0.0174 |
| 2024_09_20 22:00 | 3225722 | 2 | 7.2334 | 6.4607 | -117.9415 | 10.5425 | 196.8523 | 0.0032 | 0.0059 |
| 2024_09_20 22:00 | 3213298 | 3 | 18.2709 | 16.6478 | -114.6432 | 10.1256 | 175.6475 | 0.0031 | 0.0140 |
| 2024_09_20 22:00 | 3276599 | 4 | 13.4487 | 12.5891 | -114.9977 | 19.2695 | 142.3789 | 0.0100 | 0.1568 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412773_DA086B38 | 504990 | 150 | -78.7 | 504990 | 167 | -87.5 | 504990 | 872 | -89.7 | 504990 | 348 |
| MR_1774412773_68B63800 | 504990 | 150 | -82.1 | 504990 | 167 | -87.8 | 504990 | 872 | -88.0 | 504990 | 348 |
| MR_1774412773_C1F111FC | 504990 | 167 | -87.0 | 504990 | 150 | -80.9 | 504990 | 872 | -88.5 | 504990 | 348 |
| MR_1774412773_C70B6123 | 504990 | 150 | -78.6 | 504990 | 167 | -86.0 | 504990 | 872 | -86.7 | 504990 | 348 |
| MR_1774412773_126EB823 | 504990 | 150 | -79.6 | 504990 | 167 | -84.8 | 504990 | 872 | -89.9 | 504990 | 348 |
| MR_1774412773_EAEB22A7 | 504990 | 167 | -85.9 | 504990 | 150 | -81.7 | 504990 | 872 | -87.2 | 504990 | 348 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 458: `2e8837d5-777...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2e8837d5-7779-4925-8e66-b75b185757ab` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[458] topology](images/test_0458.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3274006_4
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274006_4
- `C4`: Decrease A3 Offset threshold for 3267157_5
- `C5`: Increase A3 Offset threshold for 3274006_4
- `C6`: Lift the tilt angle of 3267157_5 by 5 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267157_5
- `C8`: Decrease transmission power for 3267157_5
- `C9`: Check test server and transmission issues
- `C10`: Lift the tilt angle  of 3274006_4 by 3 degrees
- `C11`: Adjust the azimuth of 3267157_5 by 33 degrees
- `C12`: Increase A3 Offset threshold for 3267157_5
- `C13`: Decrease transmission power for 3274006_4
- `C14`: Decrease A3 Offset threshold for 3274006_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267157_5
- `C16`: Add neighbor relationship between 3267157_5 and 3274006_4
- `C17`: Press down the tilt angle  of 3274006_4 by 3 degrees
- `C18`: Press down the tilt angle of 3267157_5 by 5 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274006_4
- `C20`: Adjust the azimuth of 3274006_4 by 21 degrees
- `C21`: Increase transmission power for 3267157_5
- `C22`: Add neighbor relationship between 3225738_1 and 3274006_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.990 | MS1 | 121.4656599172 | 31.1446317739 | 23 | 504990 | -83.85 | 17.04 | 605.32 | 0.18 | 2.58 | 1575 |
| 2024-09-20 22:21:32.518 | MS1 | 121.4656593875 | 31.1446359929 | 23 | 504990 | -84.09 | 16.74 | 378.86 | 0.02 | 2.21 | 1594 |
| 2024-09-20 22:21:33.492 | MS1 | 121.4656589726 | 31.1446285946 | 23 | 504990 | -78.82 | 13.10 | 511.96 | 0.18 | 2.09 | 1588 |
| 2024-09-20 22:21:34.446 | MS1 | 121.4656739725 | 31.1446316936 | 716 | 504990 | -85.82 | 1.41 | 33.42 | 0.17 | 1.43 | 1584 |
| 2024-09-20 22:21:35.674 | MS1 | 121.4656763398 | 31.1446305418 | 716 | 504990 | -82.76 | 3.84 | 54.26 | 0.04 | 1.50 | 1575 |
| 2024-09-20 22:21:36.887 | MS1 | 121.4656745727 | 31.1446288787 | 23 | 504990 | -84.38 | 4.43 | 32.87 | 0.13 | 1.48 | 1568 |
| 2024-09-20 22:21:37.978 | MS1 | 121.4656707627 | 31.1446217460 | 23 | 504990 | -87.75 | 2.89 | 36.46 | 0.10 | 1.23 | 1572 |
| 2024-09-20 22:21:38.574 | MS1 | 121.4656595353 | 31.1446243960 | 716 | 504990 | -87.96 | 3.36 | 34.64 | 0.10 | 1.04 | 1564 |
| 2024-09-20 22:21:39.600 | MS1 | 121.4656755032 | 31.1446322258 | 716 | 504990 | -82.09 | 4.95 | 34.78 | 0.19 | 1.10 | 1597 |
| 2024-09-20 22:21:40.150 | MS1 | 121.4656655340 | 31.1446263389 | 716 | 504990 | -79.38 | 17.45 | 317.32 | 0.06 | 2.83 | 1562 |
| 2024-09-20 22:21:41.163 | MS1 | 121.4656713037 | 31.1446239720 | 716 | 504990 | -78.27 | 12.33 | 495.64 | 0.15 | 2.56 | 1575 |
| 2024-09-20 22:21:42.768 | MS1 | 121.4656675854 | 31.1446221211 | 716 | 504990 | -82.39 | 12.64 | 357.09 | 0.15 | 2.57 | 1567 |

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
| 3225738 | 1 | 121.4675194169 | 31.1458234138 | 184 | 1 | 12 | 49.3 | TDD | 327 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3244029 | 3 | 121.4645055593 | 31.1500730319 | 50 | 15 | 5 | 30.2 | TDD | 756 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3256239 | 2 | 121.4685079823 | 31.1532434137 | 326 | 4 | 12 | 38.7 | TDD | 716 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3267157 | 5 | 121.4737312265 | 31.1515168567 | 258 | 4 | 6 | 17.9 | TDD | 23 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3274006 | 4 | 121.4645154427 | 31.1518153858 | 151 | 1 | 0 | 24.2 | TDD | 22 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.589 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.604 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.708 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.708 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.428 | NREventA3 | measId:2;ServCellPCI:317;Se... |
| 2024-09-20 22:21:34.668 | NRHandoverAttempt | SourcePCI:317;SourceNR-ARFC... |
| 2024-09-20 22:21:34.718 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.728 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:34.830 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.830 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.428 | NREventA3 | measId:2;ServCellPCI:260;Se... |
| 2024-09-20 22:21:36.668 | NRHandoverAttempt | SourcePCI:260;SourceNR-ARFC... |
| 2024-09-20 22:21:36.718 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.731 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.845 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.845 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.428 | NREventA3 | measId:2;ServCellPCI:317;Se... |
| 2024-09-20 22:21:38.668 | NRHandoverAttempt | SourcePCI:317;SourceNR-ARFC... |
| 2024-09-20 22:21:38.707 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.719 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.855 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.855 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225738 | 1 | 7.2583 | 10.0584 | -114.8401 | 10.3553 | 83.5106 | 0.0107 | 0.0138 |
| 2024_09_20 22:00 | 3256239 | 2 | 16.7769 | 16.3682 | -114.1676 | 12.3956 | 98.2224 | 0.0032 | 0.0046 |
| 2024_09_20 22:00 | 3244029 | 3 | 17.0089 | 17.8654 | -116.2700 | 19.2708 | 125.8760 | 0.0044 | 0.0054 |
| 2024_09_20 22:00 | 3274006 | 4 | 19.4691 | 19.7939 | -117.2947 | 18.7403 | 88.7938 | 0.0015 | 0.0128 |
| 2024_09_20 22:00 | 3267157 | 5 | 10.3207 | 12.2064 | -115.7718 | 12.4894 | 192.7030 | 0.0098 | 0.0101 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412276_9F2E9357 | 504990 | 716 | -84.2 | 504990 | 23 | -83.1 | 504990 | 22 | -85.9 | 504990 | 327 |
| MR_1774412276_8556AABE | 504990 | 23 | -87.1 | 504990 | 716 | -83.8 | 504990 | 22 | -85.3 | 504990 | 327 |
| MR_1774412276_8B58CCBB | 504990 | 23 | -83.9 | 504990 | 716 | -85.0 | 504990 | 22 | -86.2 | 504990 | 327 |
| MR_1774412276_EFD75528 | 504990 | 23 | -86.3 | 504990 | 716 | -82.6 | 504990 | 22 | -85.5 | 504990 | 327 |
| MR_1774412276_A232B90E | 504990 | 23 | -86.6 | 504990 | 716 | -83.7 | 504990 | 22 | -88.1 | 504990 | 327 |
| MR_1774412276_39237B14 | 504990 | 23 | -85.9 | 504990 | 716 | -82.1 | 504990 | 22 | -87.6 | 504990 | 327 |
| MR_1774412276_4BEB8C39 | 504990 | 23 | -85.9 | 504990 | 716 | -82.9 | 504990 | 22 | -86.0 | 504990 | 327 |
| MR_1774412276_8EB90E82 | 504990 | 716 | -86.1 | 504990 | 23 | -83.5 | 504990 | 22 | -88.7 | 504990 | 327 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 459: `f2e50ae6-693...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f2e50ae6-693f-4c61-ae43-787bf580ebd1` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[459] topology](images/test_0459.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3221588_4 by 9 degrees
- `C2`: Increase A3 Offset threshold for 3267147_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221588_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267147_2
- `C5`: Increase A3 Offset threshold for 3221588_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221588_4
- `C7`: Add neighbor relationship between 3229544_3 and 3221588_4
- `C8`: Adjust the azimuth of 3267147_2 by 50 degrees
- `C9`: Decrease transmission power for 3267147_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease transmission power for 3221588_4
- `C12`: Increase transmission power for 3221588_4
- `C13`: Press down the tilt angle of 3267147_2 by 2 degrees
- `C14`: Increase transmission power for 3267147_2
- `C15`: Check test server and transmission issues
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267147_2
- `C17`: Lift the tilt angle  of 3221588_4 by 10 degrees
- `C18`: Press down the tilt angle  of 3221588_4 by 10 degrees
- `C19`: Decrease A3 Offset threshold for 3267147_2
- `C20`: Lift the tilt angle of 3267147_2 by 2 degrees
- `C21`: Add neighbor relationship between 3267147_2 and 3221588_4
- `C22`: Decrease A3 Offset threshold for 3221588_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.710 | MS1 | 121.4656768523 | 31.1446258059 | 1007 | 504990 | -82.01 | 14.68 | 517.28 | 0.05 | 2.23 | 1595 |
| 2024-09-20 22:21:32.643 | MS1 | 121.4656633668 | 31.1446372395 | 1007 | 504990 | -84.62 | 14.91 | 593.56 | 0.13 | 3.00 | 1566 |
| 2024-09-20 22:21:33.602 | MS1 | 121.4656682057 | 31.1446330311 | 1007 | 504990 | -77.73 | 14.85 | 526.91 | 0.14 | 2.48 | 1596 |
| 2024-09-20 22:21:34.677 | MS1 | 121.4656664980 | 31.1446201119 | 1007 | 504990 | -90.12 | -3.28 | 83.64 | 0.19 | 1.21 | 1592 |
| 2024-09-20 22:21:35.443 | MS1 | 121.4656636682 | 31.1446282072 | 1007 | 504990 | -90.20 | -3.50 | 77.11 | 0.10 | 1.01 | 1568 |
| 2024-09-20 22:21:36.535 | MS1 | 121.4656670298 | 31.1446371074 | 1007 | 504990 | -91.20 | -0.54 | 29.01 | 0.01 | 1.28 | 1564 |
| 2024-09-20 22:21:37.241 | MS1 | 121.4656723277 | 31.1446265776 | 1007 | 504990 | -89.93 | -0.18 | 51.89 | 0.15 | 1.10 | 1591 |
| 2024-09-20 22:21:38.835 | MS1 | 121.4656667189 | 31.1446218241 | 1007 | 504990 | -90.40 | -0.04 | 56.11 | 0.11 | 1.49 | 1570 |
| 2024-09-20 22:21:39.522 | MS1 | 121.4656709236 | 31.1446228479 | 991 | 504990 | -81.74 | 15.46 | 294.62 | 0.01 | 1.16 | 1563 |
| 2024-09-20 22:21:40.769 | MS1 | 121.4656692560 | 31.1446210452 | 991 | 504990 | -80.51 | 16.97 | 341.68 | 0.12 | 2.48 | 1600 |
| 2024-09-20 22:21:41.294 | MS1 | 121.4656619043 | 31.1446304627 | 991 | 504990 | -81.49 | 15.35 | 367.88 | 0.10 | 2.45 | 1590 |
| 2024-09-20 22:21:42.292 | MS1 | 121.4656679036 | 31.1446235699 | 991 | 504990 | -83.14 | 12.72 | 508.15 | 0.08 | 2.79 | 1580 |

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
| 3221588 | 4 | 121.4694921953 | 31.1494449445 | 223 | 13 | 5 | 47.6 | TDD | 991 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3229544 | 3 | 121.4714035441 | 31.1517228109 | 56 | 5 | 4 | 28.0 | TDD | 111 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3255928 | 1 | 121.4669503128 | 31.1558151505 | 315 | 1 | 4 | 34.3 | TDD | 304 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3267147 | 2 | 121.4642303701 | 31.1529587526 | 277 | 1 | 3 | 22.7 | TDD | 1007 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.998 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.019 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.148 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.148 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.895 | NREventA3 | measId:2;ServCellPCI:293;Se... |
| 2024-09-20 22:21:38.135 | NRHandoverAttempt | SourcePCI:293;SourceNR-ARFC... |
| 2024-09-20 22:21:38.184 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.197 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.344 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.344 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255928 | 1 | 15.5346 | 6.3904 | -114.3208 | 10.8766 | 95.1944 | 0.0027 | 0.0037 |
| 2024_09_20 22:00 | 3267147 | 2 | 12.9181 | 17.1388 | -115.2199 | 11.6859 | 145.3358 | 0.0157 | 0.1954 |
| 2024_09_20 22:00 | 3229544 | 3 | 16.3735 | 19.8028 | -116.3592 | 18.1103 | 185.6239 | 0.0157 | 0.0028 |
| 2024_09_20 22:00 | 3221588 | 4 | 19.7368 | 19.7217 | -116.4473 | 14.3781 | 95.3780 | 0.0059 | 0.0135 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415612_C743A72E | 504990 | 1007 | -90.0 | 504990 | 991 | -84.7 | 504990 | 111 | -86.1 | 504990 | 304 |
| MR_1774415612_F1875621 | 504990 | 991 | -87.3 | 504990 | 1007 | -92.0 | 504990 | 111 | -87.8 | 504990 | 304 |
| MR_1774415612_51E673B5 | 504990 | 1007 | -88.2 | 504990 | 991 | -83.9 | 504990 | 111 | -85.9 | 504990 | 304 |
| MR_1774415612_0BB66F33 | 504990 | 991 | -86.8 | 504990 | 1007 | -90.9 | 504990 | 111 | -86.9 | 504990 | 304 |
| MR_1774415612_57E8423F | 504990 | 1007 | -88.4 | 504990 | 991 | -84.0 | 504990 | 111 | -85.9 | 504990 | 304 |
| MR_1774415612_EC45B209 | 504990 | 991 | -87.1 | 504990 | 1007 | -88.4 | 504990 | 111 | -87.9 | 504990 | 304 |
| MR_1774415612_7628B847 | 504990 | 1007 | -91.6 | 504990 | 991 | -86.7 | 504990 | 111 | -86.8 | 504990 | 304 |
| MR_1774415612_0393CE37 | 504990 | 991 | -86.6 | 504990 | 1007 | -90.3 | 504990 | 111 | -84.7 | 504990 | 304 |

> *... 2개 열 생략 (전체 14열)*

---
