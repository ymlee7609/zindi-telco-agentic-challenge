# Track A 문제 분석 — train[1250]~train[1259]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1250] ~ train[1259] (10개)

## 목차

1. [문제 1250: `7a73685b-8e6...`](#1250) — single-answer, 정답: C15
2. [문제 1251: `d2600d92-2f1...`](#1251) — single-answer, 정답: C12
3. [문제 1252: `4f7ff733-1d2...`](#1252) — multiple-answer, 정답: C5|C12
4. [문제 1253: `967a5bf5-279...`](#1253) — single-answer, 정답: C13
5. [문제 1254: `46bc535d-eeb...`](#1254) — multiple-answer, 정답: C3|C17
6. [문제 1255: `4b7d9b5b-f4c...`](#1255) — single-answer, 정답: C7
7. [문제 1256: `5b8896f2-7e3...`](#1256) — single-answer, 정답: C15
8. [문제 1257: `c6d14326-f55...`](#1257) — single-answer, 정답: C13
9. [문제 1258: `c5d7073e-22d...`](#1258) — single-answer, 정답: C14
10. [문제 1259: `36a2c1db-432...`](#1259) — single-answer, 정답: C12

---

### 문제 1250: `7a73685b-8e6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7a73685b-8e68-42a8-9c48-0a03eab066c2` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3270161_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1250] topology](images/train_1250.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3270161_1
- `C2`: Lift the tilt angle of 3270161_1 by 4 degrees
- `C3`: Decrease transmission power for 3273995_2
- `C4`: Increase transmission power for 3273995_2
- `C5`: Adjust the azimuth of 3270161_1 by 11 degrees
- `C6`: Increase A3 Offset threshold for 3270161_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273995_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273995_2
- `C9`: Adjust the azimuth of 3273995_2 by 50 degrees
- `C10`: Add neighbor relationship between 3244894_4 and 3273995_2
- `C11`: Check test server and transmission issues
- `C12`: Lift the tilt angle  of 3273995_2 by 10 degrees
- `C13`: Increase A3 Offset threshold for 3273995_2
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270161_1 **← 정답**
- `C16`: Add neighbor relationship between 3270161_1 and 3273995_2
- `C17`: Decrease transmission power for 3270161_1
- `C18`: Press down the tilt angle  of 3273995_2 by 10 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270161_1
- `C20`: Decrease A3 Offset threshold for 3273995_2
- `C21`: Press down the tilt angle of 3270161_1 by 4 degrees
- `C22`: Increase transmission power for 3270161_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.381 | MS1 | 121.4656619331 | 31.1446224381 | 833 | 504990 | -89.25 | 12.43 | 498.77 | 0.18 | 2.41 | 1562 |
| 2024-09-20 22:21:32.993 | MS1 | 121.4656629881 | 31.1446296959 | 833 | 504990 | -86.36 | 16.15 | 349.88 | 0.01 | 2.28 | 1575 |
| 2024-09-20 22:21:33.233 | MS1 | 121.4656713735 | 31.1446350636 | 833 | 504990 | -87.74 | 16.30 | 578.61 | 0.04 | 2.33 | 1571 |
| 2024-09-20 22:21:34.746 | MS1 | 121.4656714018 | 31.1446230178 | 833 | 504990 | -86.59 | 13.24 | 83.54 | 0.67 | 2.27 | 646 |
| 2024-09-20 22:21:35.450 | MS1 | 121.4656765545 | 31.1446379463 | 833 | 504990 | -85.18 | 13.15 | 101.84 | 0.52 | 2.14 | 513 |
| 2024-09-20 22:21:36.909 | MS1 | 121.4656768714 | 31.1446323144 | 833 | 504990 | -85.51 | 15.78 | 89.85 | 0.53 | 2.41 | 623 |
| 2024-09-20 22:21:37.336 | MS1 | 121.4656666767 | 31.1446190220 | 833 | 504990 | -89.50 | 9.16 | 68.79 | 0.64 | 2.27 | 554 |
| 2024-09-20 22:21:38.190 | MS1 | 121.4656762915 | 31.1446242554 | 833 | 504990 | -89.69 | 10.89 | 82.92 | 0.61 | 2.89 | 656 |
| 2024-09-20 22:21:39.507 | MS1 | 121.4656687909 | 31.1446230070 | 833 | 504990 | -92.81 | 9.97 | 77.98 | 0.69 | 2.92 | 638 |
| 2024-09-20 22:21:40.988 | MS1 | 121.4656718225 | 31.1446277332 | 833 | 504990 | -91.81 | 7.88 | 463.31 | 0.14 | 2.16 | 1567 |
| 2024-09-20 22:21:41.352 | MS1 | 121.4656688406 | 31.1446246085 | 833 | 504990 | -91.09 | 7.01 | 531.35 | 0.10 | 2.48 | 1585 |
| 2024-09-20 22:21:42.631 | MS1 | 121.4656743123 | 31.1446228838 | 833 | 504990 | -90.65 | 11.92 | 581.71 | 0.20 | 2.99 | 1597 |

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
| 3244894 | 4 | 121.4691189820 | 31.1451400080 | 290 | 13 | 2 | 38.1 | TDD | 324 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3251360 | 3 | 121.4661136054 | 31.1456811365 | 192 | 0 | 8 | 19.3 | TDD | 299 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3270161 | 1 | 121.4666101233 | 31.1514423305 | 176 | 1 | 5 | 38.5 | TDD | 833 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3273995 | 2 | 121.4657827758 | 31.1458210621 | 17 | 0 | 6 | 35.0 | TDD | 2 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.968 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.988 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.111 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.111 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.801 | NREventA3 | measId:2;ServCellPCI:562;Se... |
| 2024-09-20 22:21:38.041 | NRHandoverAttempt | SourcePCI:562;SourceNR-ARFC... |
| 2024-09-20 22:21:38.091 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.101 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.234 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.234 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270161 | 1 | 5.6279 | 6.0685 | -114.4757 | 14.8721 | 127.3576 | 0.0196 | 0.0041 |
| 2024_09_20 22:00 | 3273995 | 2 | 7.9396 | 14.8041 | -114.7192 | 17.1252 | 141.9170 | 0.0114 | 0.0043 |
| 2024_09_20 22:00 | 3251360 | 3 | 18.1444 | 5.3534 | -114.7115 | 6.5748 | 118.6557 | 0.0120 | 0.0165 |
| 2024_09_20 22:00 | 3244894 | 4 | 16.8278 | 11.4489 | -114.2857 | 8.3974 | 97.7248 | 0.0168 | 0.0099 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414296_E5B59BB9 | 504990 | 833 | -86.4 | 504990 | 2 | -92.9 | 504990 | 324 | -98.5 | 504990 | 299 |
| MR_1774414296_E9C17609 | 504990 | 833 | -84.9 | 504990 | 2 | -94.3 | 504990 | 324 | -98.0 | 504990 | 299 |
| MR_1774414296_C2991FFE | 504990 | 833 | -87.3 | 504990 | 2 | -96.3 | 504990 | 324 | -99.0 | 504990 | 299 |
| MR_1774414296_EE98C2E5 | 504990 | 833 | -87.7 | 504990 | 2 | -95.2 | 504990 | 324 | -96.2 | 504990 | 299 |
| MR_1774414296_D09A5C59 | 504990 | 833 | -86.5 | 504990 | 2 | -95.2 | 504990 | 324 | -97.0 | 504990 | 299 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1251: `d2600d92-2f1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d2600d92-2f1b-4b38-ab80-07dd7ce8f2f4` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214332_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1251] topology](images/train_1251.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3233814_4
- `C2`: Add neighbor relationship between 3214332_2 and 3233814_4
- `C3`: Decrease transmission power for 3233814_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233814_4
- `C5`: Adjust the azimuth of 3214332_2 by 6 degrees
- `C6`: Check test server and transmission issues
- `C7`: Increase A3 Offset threshold for 3233814_4
- `C8`: Decrease A3 Offset threshold for 3233814_4
- `C9`: Increase A3 Offset threshold for 3214332_2
- `C10`: Increase transmission power for 3214332_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214332_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214332_2 **← 정답**
- `C13`: Add neighbor relationship between 3262928_13 and 3233814_4
- `C14`: Lift the tilt angle of 3214332_2 by 4 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Press down the tilt angle of 3214332_2 by 4 degrees
- `C17`: Decrease A3 Offset threshold for 3214332_2
- `C18`: Adjust the azimuth of 3233814_4 by 20 degrees
- `C19`: Decrease transmission power for 3214332_2
- `C20`: Lift the tilt angle  of 3233814_4 by 0 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233814_4
- `C22`: Press down the tilt angle  of 3233814_4 by 0 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.918 | MS1 | 121.4656654119 | 31.1446327351 | 867 | 504990 | -95.37 | 11.10 | 578.15 | 0.12 | 2.90 | 1594 |
| 2024-09-20 22:21:32.354 | MS1 | 121.4656757940 | 31.1446348592 | 321 | 504990 | -94.38 | 12.24 | 555.91 | 0.07 | 2.46 | 1560 |
| 2024-09-20 22:21:33.875 | MS1 | 121.4656776034 | 31.1446274546 | 989 | 504990 | -93.03 | 11.80 | 402.47 | 0.16 | 2.32 | 1571 |
| 2024-09-20 22:21:34.178 | MS1 | 121.4656659159 | 31.1446209004 | 1007 | 152650 | -96.86 | 2.50 | 45.05 | 0.14 | 1.59 | 999 |
| 2024-09-20 22:21:35.962 | MS1 | 121.4656590882 | 31.1446356580 | 556 | 152650 | -93.52 | 3.78 | 96.00 | 0.18 | 1.71 | 952 |
| 2024-09-20 22:21:36.684 | MS1 | 121.4656690171 | 31.1446186418 | 951 | 152650 | -88.42 | 7.97 | 78.18 | 0.16 | 1.63 | 960 |
| 2024-09-20 22:21:37.732 | MS1 | 121.4656744912 | 31.1446279152 | 648 | 152650 | -91.09 | 4.11 | 73.65 | 0.16 | 1.91 | 914 |
| 2024-09-20 22:21:38.463 | MS1 | 121.4656614077 | 31.1446291400 | 1007 | 152650 | -88.56 | 5.46 | 75.69 | 0.09 | 1.94 | 937 |
| 2024-09-20 22:21:39.790 | MS1 | 121.4656585376 | 31.1446280252 | 556 | 152650 | -92.47 | 6.80 | 71.57 | 0.19 | 1.55 | 910 |
| 2024-09-20 22:21:40.119 | MS1 | 121.4656741604 | 31.1446206888 | 951 | 152650 | -95.06 | 4.27 | 53.79 | 0.11 | 2.48 | 1593 |
| 2024-09-20 22:21:41.726 | MS1 | 121.4656768159 | 31.1446184099 | 648 | 152650 | -92.38 | 7.88 | 69.42 | 0.02 | 2.92 | 1591 |
| 2024-09-20 22:21:42.222 | MS1 | 121.4656618907 | 31.1446323876 | 1007 | 152650 | -93.92 | 2.39 | 66.72 | 0.10 | 2.48 | 1571 |

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
| 3214332 | 2 | 121.4696499410 | 31.1492994525 | 222 | 2 | 10 | 22.4 | TDD | 867 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3216578 | 8 | 121.4756442045 | 31.1541280172 | 44 | 9 | 0 | 7.4 | FDD | 556 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3218780 | 5 | 121.4729580388 | 31.1538178962 | 60 | 2 | 9 | 29.1 | TDD | 755 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3219936 | 6 | 121.4752853148 | 31.1519161717 | 81 | 7 | 2 | 30.0 | TDD | 989 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3227059 | 7 | 121.4667043545 | 31.1459762042 | 350 | 2 | 4 | 4.3 | FDD | 648 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3233526 | 9 | 121.4688438654 | 31.1488492548 | 251 | 15 | 3 | 29.6 | FDD | 236 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3233814 | 4 | 121.4653151532 | 31.1524962130 | 198 | 0 | 8 | 0.1 | TDD | 656 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3235460 | 11 | 121.4642003905 | 31.1495442293 | 6 | 5 | 11 | 3.4 | FDD | 1007 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3255479 | 1 | 121.4707942668 | 31.1473153035 | 61 | 14 | 2 | 7.5 | TDD | 321 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3256217 | 10 | 121.4714224534 | 31.1480133525 | 60 | 1 | 0 | 26.5 | FDD | 492 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3257526 | 12 | 121.4726976495 | 31.1543194508 | 218 | 13 | 8 | 5.4 | FDD | 976 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3262928 | 13 | 121.4755887048 | 31.1468431944 | 332 | 14 | 10 | 20.5 | FDD | 951 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3269432 | 3 | 121.4746420894 | 31.1533575838 | 133 | 13 | 10 | 18.0 | TDD | 739 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.763 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.778 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.879 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.879 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.640 | NREventA2 | measId:1;ServCellPCI:443;Se... |
| 2024-09-20 22:21:34.744 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.018 | NREventA5 | measId:3;ServCellPCI:443;Se... |
| 2024-09-20 22:21:35.067 | NRHandoverAttempt | SourcePCI:443;SourceNR-ARFC... |
| 2024-09-20 22:21:35.089 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.103 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.244 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.244 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255479 | 1 | 15.1399 | 6.2920 | -116.7899 | 14.1766 | 161.1205 | 0.0047 | 0.0193 |
| 2024_09_20 22:00 | 3214332 | 2 | 13.9516 | 16.9731 | -115.1555 | 8.5722 | 178.6519 | 0.0024 | 0.0183 |
| 2024_09_20 22:00 | 3269432 | 3 | 13.7295 | 11.5543 | -115.0767 | 15.8780 | 159.8295 | 0.0125 | 0.0085 |
| 2024_09_20 22:00 | 3233814 | 4 | 10.1746 | 6.2221 | -116.9185 | 9.0249 | 130.3747 | 0.0052 | 0.0117 |
| 2024_09_20 22:00 | 3218780 | 5 | 11.7386 | 13.7496 | -115.2393 | 9.3558 | 95.5978 | 0.0125 | 0.0080 |
| 2024_09_20 22:00 | 3219936 | 6 | 5.5709 | 5.0613 | -114.8948 | 19.9248 | 130.9614 | 0.0185 | 0.0025 |
| 2024_09_20 22:00 | 3227059 | 7 | 17.0127 | 17.6919 | -116.8251 | 4.7362 | 50.9356 | 0.0100 | 0.0083 |
| 2024_09_20 22:00 | 3216578 | 8 | 8.2932 | 15.6673 | -114.3494 | 3.9181 | 44.3071 | 0.0183 | 0.0161 |
| 2024_09_20 22:00 | 3233526 | 9 | 18.0773 | 16.1457 | -115.3963 | 4.8073 | 20.6405 | 0.0024 | 0.0136 |
| 2024_09_20 22:00 | 3256217 | 10 | 18.8613 | 12.3158 | -115.9906 | 3.2274 | 42.6701 | 0.0071 | 0.0013 |
| 2024_09_20 22:00 | 3235460 | 11 | 19.5411 | 6.0548 | -114.7447 | 4.8748 | 31.2536 | 0.0106 | 0.0190 |
| 2024_09_20 22:00 | 3257526 | 12 | 18.8688 | 13.7559 | -117.6678 | 4.7810 | 31.9834 | 0.0107 | 0.0180 |
| 2024_09_20 22:00 | 3262928 | 13 | 14.4998 | 14.6309 | -114.8490 | 3.9900 | 37.0191 | 0.0156 | 0.0041 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413543_95BB26BD | 152650 | 1007 | -95.5 | 152650 | 236 | -98.9 | 152650 | 976 | -105.4 | 152650 | 492 |
| MR_1774413543_C83408B4 | 504990 | 989 | -92.3 | 504990 | 656 | -90.8 | 504990 | 739 | -93.5 | 504990 | 755 |
| MR_1774413543_28C380FC | 152650 | 1007 | -97.1 | 152650 | 236 | -101.8 | 152650 | 976 | -103.9 | 152650 | 492 |
| MR_1774413543_F487C61C | 152650 | 1007 | -96.5 | 152650 | 236 | -99.2 | 152650 | 976 | -104.2 | 152650 | 492 |
| MR_1774413543_F3BE73CF | 152650 | 1007 | -97.4 | 152650 | 236 | -98.7 | 152650 | 976 | -103.7 | 152650 | 492 |
| MR_1774413543_9C93B446 | 152650 | 1007 | -95.0 | 152650 | 236 | -102.6 | 152650 | 976 | -105.6 | 152650 | 492 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1252: `4f7ff733-1d2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4f7ff733-1d2e-40ed-8ca5-6c903ac63446` |
| Tag | **multiple-answer** |
| 정답 | **C5|C12** |
| C5 의미 | Increase transmission power for 3211745_2 |
| C12 의미 | Adjust the azimuth of 3211745_2 by 27 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1252] topology](images/train_1252.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3265233_3 and 3275197_1
- `C2`: Decrease transmission power for 3211745_2
- `C3`: Lift the tilt angle  of 3275197_1 by 2 degrees
- `C4`: Increase A3 Offset threshold for 3275197_1
- `C5`: Increase transmission power for 3211745_2 **← 정답**
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211745_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275197_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase transmission power for 3275197_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211745_2
- `C11`: Adjust the azimuth of 3275197_1 by 30 degrees
- `C12`: Adjust the azimuth of 3211745_2 by 27 degrees **← 정답**
- `C13`: Decrease transmission power for 3275197_1
- `C14`: Check test server and transmission issues
- `C15`: Add neighbor relationship between 3211745_2 and 3275197_1
- `C16`: Press down the tilt angle of 3211745_2 by 10 degrees
- `C17`: Press down the tilt angle  of 3275197_1 by 2 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275197_1
- `C19`: Decrease A3 Offset threshold for 3275197_1
- `C20`: Lift the tilt angle of 3211745_2 by 10 degrees
- `C21`: Increase A3 Offset threshold for 3211745_2
- `C22`: Decrease A3 Offset threshold for 3211745_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.232 | MS1 | 121.4656744926 | 31.1446378826 | 340 | 504990 | -94.77 | 14.70 | 327.21 | 0.03 | 2.08 | 1591 |
| 2024-09-20 22:21:32.990 | MS1 | 121.4656593348 | 31.1446254091 | 340 | 504990 | -86.15 | 12.72 | 319.97 | 0.07 | 2.41 | 1573 |
| 2024-09-20 22:21:33.195 | MS1 | 121.4656735094 | 31.1446191001 | 340 | 504990 | -91.00 | 16.04 | 342.56 | 0.18 | 2.04 | 1573 |
| 2024-09-20 22:21:34.446 | MS1 | 121.4656724103 | 31.1446264929 | 340 | 504990 | -108.17 | -0.01 | 46.73 | 0.12 | 1.23 | 1576 |
| 2024-09-20 22:21:35.877 | MS1 | 121.4656754789 | 31.1446325981 | 340 | 504990 | -104.92 | -1.49 | 35.11 | 0.19 | 1.30 | 1599 |
| 2024-09-20 22:21:36.960 | MS1 | 121.4656601988 | 31.1446196681 | 340 | 504990 | -104.81 | 1.35 | 72.38 | 0.00 | 1.28 | 1587 |
| 2024-09-20 22:21:37.959 | MS1 | 121.4656738752 | 31.1446189700 | 340 | 504990 | -103.92 | 0.59 | 84.51 | 0.12 | 1.13 | 1590 |
| 2024-09-20 22:21:38.428 | MS1 | 121.4656602960 | 31.1446289189 | 340 | 504990 | -108.75 | 1.68 | 33.54 | 0.02 | 1.34 | 1587 |
| 2024-09-20 22:21:39.317 | MS1 | 121.4656668238 | 31.1446220043 | 340 | 504990 | -105.87 | 0.10 | 49.01 | 0.16 | 1.03 | 1582 |
| 2024-09-20 22:21:40.716 | MS1 | 121.4656619414 | 31.1446317288 | 340 | 504990 | -85.07 | 13.14 | 430.42 | 0.06 | 2.65 | 1565 |
| 2024-09-20 22:21:41.935 | MS1 | 121.4656773008 | 31.1446299900 | 340 | 504990 | -85.39 | 15.88 | 424.06 | 0.19 | 2.18 | 1591 |
| 2024-09-20 22:21:42.376 | MS1 | 121.4656606522 | 31.1446324098 | 340 | 504990 | -87.23 | 12.09 | 561.37 | 0.04 | 2.79 | 1568 |

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
| 3211745 | 2 | 121.4667136424 | 31.1499761311 | 163 | 10 | 10 | 24.7 | TDD | 340 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3265233 | 3 | 121.4719518951 | 31.1496052387 | 115 | 6 | 3 | 43.4 | TDD | 98 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3272235 | 4 | 121.4729545343 | 31.1537266419 | 248 | 12 | 4 | 45.6 | TDD | 332 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3275197 | 1 | 121.4744211813 | 31.1459781698 | 290 | 0 | 5 | 36.9 | TDD | 1002 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.792 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.811 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.913 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.913 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.147 | NREventA2 | measId:1;ServCellPCI:749;Se... |
| 2024-09-20 22:21:34.284 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275197 | 1 | 10.1999 | 15.5252 | -117.3730 | 5.9417 | 150.6179 | 0.0188 | 0.0141 |
| 2024_09_20 22:00 | 3211745 | 2 | 13.6266 | 8.0897 | -117.7996 | 19.2201 | 139.3744 | 0.1344 | 0.0163 |
| 2024_09_20 22:00 | 3265233 | 3 | 6.6320 | 9.0295 | -114.8048 | 11.9737 | 116.3887 | 0.0100 | 0.0106 |
| 2024_09_20 22:00 | 3272235 | 4 | 18.9890 | 13.5894 | -116.7681 | 14.3113 | 190.1612 | 0.0130 | 0.0118 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416335_82793E44 | 504990 | 340 | -109.0 | 504990 | 1002 | -117.9 | 504990 | 98 | -123.7 | 504990 | 332 |
| MR_1774416335_2AA3CA2D | 504990 | 340 | -107.9 | 504990 | 1002 | -115.9 | 504990 | 98 | -120.9 | 504990 | 332 |
| MR_1774416335_22E3736E | 504990 | 340 | -107.4 | 504990 | 1002 | -117.7 | 504990 | 98 | -122.8 | 504990 | 332 |
| MR_1774416335_FB17A3CD | 504990 | 340 | -109.2 | 504990 | 1002 | -114.6 | 504990 | 98 | -122.3 | 504990 | 332 |
| MR_1774416335_57584C85 | 504990 | 340 | -106.8 | 504990 | 1002 | -115.8 | 504990 | 98 | -121.7 | 504990 | 332 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1253: `967a5bf5-279...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `967a5bf5-279f-40aa-bf8b-296aab1bbb24` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Lift the tilt angle  of 3263251_4 by 8 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1253] topology](images/train_1253.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234859_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210423_1
- `C3`: Add neighbor relationship between 3263251_4 and 3234859_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234859_2
- `C5`: Decrease transmission power for 3210423_1
- `C6`: Press down the tilt angle of 3210423_1 by 3 degrees
- `C7`: Lift the tilt angle of 3210423_1 by 3 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210423_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease A3 Offset threshold for 3234859_2
- `C11`: Press down the tilt angle  of 3263251_4 by 8 degrees
- `C12`: Increase transmission power for 3210423_1
- `C13`: Lift the tilt angle  of 3263251_4 by 8 degrees **← 정답**
- `C14`: Add neighbor relationship between 3210423_1 and 3234859_2
- `C15`: Decrease transmission power for 3234859_2
- `C16`: Increase transmission power for 3234859_2
- `C17`: Adjust the azimuth of 3263251_4 by 50 degrees
- `C18`: Increase A3 Offset threshold for 3210423_1
- `C19`: Increase A3 Offset threshold for 3234859_2
- `C20`: Adjust the azimuth of 3210423_1 by 40 degrees
- `C21`: Decrease A3 Offset threshold for 3210423_1
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.728 | MS1 | 121.4656685869 | 31.1446242031 | 139 | 504990 | -90.51 | 15.55 | 535.84 | 0.07 | 2.66 | 1576 |
| 2024-09-20 22:21:32.938 | MS1 | 121.4656603164 | 31.1446252327 | 139 | 504990 | -89.11 | 16.45 | 545.08 | 0.14 | 2.74 | 1598 |
| 2024-09-20 22:21:33.875 | MS1 | 121.4656697123 | 31.1446231416 | 139 | 504990 | -85.77 | 16.86 | 333.14 | 0.01 | 2.35 | 1568 |
| 2024-09-20 22:21:34.344 | MS1 | 121.4656750856 | 31.1446194973 | 139 | 504990 | -88.47 | 12.57 | 92.01 | 0.12 | 2.11 | 1560 |
| 2024-09-20 22:21:35.259 | MS1 | 121.4656585893 | 31.1446202163 | 139 | 504990 | -91.85 | 13.50 | 95.56 | 0.16 | 2.09 | 1573 |
| 2024-09-20 22:21:36.497 | MS1 | 121.4656685350 | 31.1446290295 | 139 | 504990 | -89.09 | 14.44 | 60.64 | 0.07 | 2.81 | 1563 |
| 2024-09-20 22:21:37.166 | MS1 | 121.4656631974 | 31.1446197499 | 139 | 504990 | -91.09 | 8.80 | 92.36 | 0.14 | 2.97 | 1594 |
| 2024-09-20 22:21:38.919 | MS1 | 121.4656660689 | 31.1446331935 | 139 | 504990 | -90.29 | 10.02 | 88.31 | 0.11 | 2.04 | 1592 |
| 2024-09-20 22:21:39.949 | MS1 | 121.4656658065 | 31.1446314355 | 139 | 504990 | -93.37 | 12.12 | 61.75 | 0.05 | 2.69 | 1593 |
| 2024-09-20 22:21:40.646 | MS1 | 121.4656759391 | 31.1446360780 | 139 | 504990 | -91.05 | 11.02 | 411.37 | 0.18 | 2.23 | 1569 |
| 2024-09-20 22:21:41.553 | MS1 | 121.4656684592 | 31.1446310175 | 139 | 504990 | -92.95 | 8.11 | 526.81 | 0.10 | 2.19 | 1588 |
| 2024-09-20 22:21:42.732 | MS1 | 121.4656777836 | 31.1446203940 | 139 | 504990 | -92.53 | 9.89 | 457.65 | 0.02 | 2.28 | 1593 |

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
| 3210423 | 1 | 121.4656122388 | 31.1526424092 | 140 | 0 | 4 | 42.1 | TDD | 139 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3234859 | 2 | 121.4737106578 | 31.1493056590 | 5 | 7 | 4 | 18.7 | TDD | 220 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3252061 | 3 | 121.4733903964 | 31.1505774805 | 301 | 0 | 8 | 22.0 | TDD | 973 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3263251 | 4 | 121.4727363391 | 31.1510388160 | 316 | 6 | 12 | 49.4 | TDD | 300 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.456 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.560 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.560 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.324 | NREventA3 | measId:2;ServCellPCI:843;Se... |
| 2024-09-20 22:21:38.564 | NRHandoverAttempt | SourcePCI:843;SourceNR-ARFC... |
| 2024-09-20 22:21:38.612 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.622 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.732 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.732 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210423 | 1 | 93.5003 | 92.6085 | -115.8291 | 19.0624 | 148.7812 | 0.0019 | 0.0087 |
| 2024_09_20 22:00 | 3234859 | 2 | 9.0759 | 15.8311 | -115.4165 | 14.4559 | 148.5329 | 0.0103 | 0.0177 |
| 2024_09_20 22:00 | 3252061 | 3 | 11.0961 | 5.4194 | -115.8281 | 18.6594 | 89.1497 | 0.0168 | 0.0050 |
| 2024_09_20 22:00 | 3263251 | 4 | 17.2999 | 18.6537 | -116.4961 | 11.2290 | 150.4007 | 0.0071 | 0.0076 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416351_90059835 | 504990 | 139 | -89.5 | 504990 | 220 | -93.4 | 504990 | 300 | -103.0 | 504990 | 973 |
| MR_1774416351_D14347E3 | 504990 | 139 | -88.1 | 504990 | 220 | -93.4 | 504990 | 300 | -101.4 | 504990 | 973 |
| MR_1774416351_6553FF27 | 504990 | 139 | -87.0 | 504990 | 220 | -90.1 | 504990 | 300 | -100.2 | 504990 | 973 |
| MR_1774416351_B19828F9 | 504990 | 139 | -88.9 | 504990 | 220 | -90.5 | 504990 | 300 | -100.7 | 504990 | 973 |
| MR_1774416351_17A98471 | 504990 | 139 | -89.6 | 504990 | 220 | -93.1 | 504990 | 300 | -101.5 | 504990 | 973 |
| MR_1774416351_54897C03 | 504990 | 139 | -87.0 | 504990 | 220 | -92.5 | 504990 | 300 | -100.0 | 504990 | 973 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1254: `46bc535d-eeb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `46bc535d-eebc-4d6e-9fa1-848e82b1fbd4` |
| Tag | **multiple-answer** |
| 정답 | **C3|C17** |
| C3 의미 | Decrease transmission power for 3233963_1 |
| C17 의미 | Press down the tilt angle  of 3233963_1 by 5 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1254] topology](images/train_1254.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233963_1
- `C2`: Decrease A3 Offset threshold for 3233963_1
- `C3`: Decrease transmission power for 3233963_1 **← 정답**
- `C4`: Increase A3 Offset threshold for 3225015_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225015_4
- `C6`: Lift the tilt angle  of 3233963_1 by 5 degrees
- `C7`: Decrease transmission power for 3225015_4
- `C8`: Increase transmission power for 3233963_1
- `C9`: Add neighbor relationship between 3225015_4 and 3233963_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233963_1
- `C11`: Add neighbor relationship between 3215538_3 and 3233963_1
- `C12`: Lift the tilt angle of 3225015_4 by 1 degrees
- `C13`: Decrease A3 Offset threshold for 3225015_4
- `C14`: Increase A3 Offset threshold for 3233963_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225015_4
- `C16`: Adjust the azimuth of 3233963_1 by 23 degrees
- `C17`: Press down the tilt angle  of 3233963_1 by 5 degrees **← 정답**
- `C18`: Increase transmission power for 3225015_4
- `C19`: Press down the tilt angle of 3225015_4 by 1 degrees
- `C20`: Adjust the azimuth of 3225015_4 by 7 degrees
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.648 | MS1 | 121.4656702731 | 31.1446207509 | 181 | 504990 | -82.84 | 12.18 | 346.26 | 0.17 | 2.29 | 1597 |
| 2024-09-20 22:21:32.346 | MS1 | 121.4656728075 | 31.1446374623 | 181 | 504990 | -83.48 | 16.29 | 380.65 | 0.09 | 2.06 | 1560 |
| 2024-09-20 22:21:33.757 | MS1 | 121.4656698649 | 31.1446229716 | 181 | 504990 | -75.56 | 15.44 | 432.90 | 0.01 | 2.75 | 1584 |
| 2024-09-20 22:21:34.565 | MS1 | 121.4656761274 | 31.1446209976 | 181 | 504990 | -88.83 | 3.73 | 49.09 | 0.10 | 1.30 | 1562 |
| 2024-09-20 22:21:35.971 | MS1 | 121.4656761522 | 31.1446361696 | 181 | 504990 | -88.92 | 1.44 | 55.87 | 0.16 | 1.26 | 1576 |
| 2024-09-20 22:21:36.650 | MS1 | 121.4656584686 | 31.1446198692 | 181 | 504990 | -86.08 | 3.97 | 82.24 | 0.16 | 1.39 | 1591 |
| 2024-09-20 22:21:37.479 | MS1 | 121.4656731873 | 31.1446378076 | 181 | 504990 | -92.71 | 1.27 | 62.34 | 0.09 | 1.16 | 1584 |
| 2024-09-20 22:21:38.285 | MS1 | 121.4656688953 | 31.1446190718 | 181 | 504990 | -87.73 | 2.45 | 77.62 | 0.08 | 1.49 | 1584 |
| 2024-09-20 22:21:39.769 | MS1 | 121.4656735637 | 31.1446343830 | 181 | 504990 | -91.13 | 3.96 | 41.12 | 0.19 | 1.23 | 1596 |
| 2024-09-20 22:21:40.958 | MS1 | 121.4656625166 | 31.1446195434 | 181 | 504990 | -77.00 | 17.83 | 366.31 | 0.02 | 2.27 | 1566 |
| 2024-09-20 22:21:41.767 | MS1 | 121.4656598429 | 31.1446219288 | 181 | 504990 | -84.27 | 13.15 | 579.98 | 0.01 | 2.74 | 1568 |
| 2024-09-20 22:21:42.271 | MS1 | 121.4656701971 | 31.1446358757 | 181 | 504990 | -77.55 | 17.49 | 571.29 | 0.09 | 2.48 | 1596 |

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
| 3215538 | 3 | 121.4691107449 | 31.1442645980 | 186 | 6 | 3 | 25.5 | TDD | 772 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3225015 | 4 | 121.4679219314 | 31.1558291195 | 183 | 0 | 1 | 29.7 | TDD | 181 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3233963 | 1 | 121.4713927335 | 31.1539690574 | 185 | 3 | 0 | 35.5 | TDD | 936 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3243445 | 2 | 121.4693873800 | 31.1453288952 | 98 | 1 | 0 | 16.3 | TDD | 1001 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.819 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.935 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.935 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233963 | 1 | 19.3892 | 14.6787 | -117.2181 | 14.6406 | 133.4835 | 0.0098 | 0.0037 |
| 2024_09_20 22:00 | 3243445 | 2 | 16.0945 | 17.6854 | -115.7542 | 14.7837 | 147.8398 | 0.0052 | 0.0019 |
| 2024_09_20 22:00 | 3215538 | 3 | 8.5729 | 8.8637 | -117.8227 | 11.1773 | 171.9571 | 0.0081 | 0.0074 |
| 2024_09_20 22:00 | 3225015 | 4 | 7.3865 | 15.7400 | -108.9063 | 5.6068 | 154.6903 | 0.0186 | 0.0185 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416649_8B63CD95 | 504990 | 936 | -87.6 | 504990 | 181 | -86.8 | 504990 | 772 | -90.6 | 504990 | 1001 |
| MR_1774416649_AD2A1AC1 | 504990 | 181 | -90.1 | 504990 | 936 | -87.9 | 504990 | 772 | -89.7 | 504990 | 1001 |
| MR_1774416649_36A06D40 | 504990 | 936 | -89.4 | 504990 | 181 | -86.5 | 504990 | 772 | -91.5 | 504990 | 1001 |
| MR_1774416649_820DEC38 | 504990 | 936 | -88.5 | 504990 | 181 | -90.1 | 504990 | 772 | -91.7 | 504990 | 1001 |
| MR_1774416649_FA1E152D | 504990 | 181 | -89.5 | 504990 | 936 | -89.6 | 504990 | 772 | -92.9 | 504990 | 1001 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1255: `4b7d9b5b-f4c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4b7d9b5b-f4cb-48d1-95ae-a29c0706c0f6` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Add neighbor relationship between 3264045_3 and 3277796_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1255] topology](images/train_1255.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3277796_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264045_3
- `C3`: Add neighbor relationship between 3236280_2 and 3277796_1
- `C4`: Decrease transmission power for 3264045_3
- `C5`: Decrease A3 Offset threshold for 3264045_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277796_1
- `C7`: Add neighbor relationship between 3264045_3 and 3277796_1 **← 정답**
- `C8`: Increase A3 Offset threshold for 3264045_3
- `C9`: Adjust the azimuth of 3264045_3 by 35 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Press down the tilt angle of 3264045_3 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264045_3
- `C13`: Increase A3 Offset threshold for 3277796_1
- `C14`: Increase transmission power for 3277796_1
- `C15`: Decrease transmission power for 3277796_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277796_1
- `C17`: Increase transmission power for 3264045_3
- `C18`: Press down the tilt angle  of 3277796_1 by 3 degrees
- `C19`: Adjust the azimuth of 3277796_1 by 24 degrees
- `C20`: Lift the tilt angle  of 3277796_1 by 3 degrees
- `C21`: Check test server and transmission issues
- `C22`: Lift the tilt angle of 3264045_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.281 | MS1 | 121.4656699814 | 31.1446237327 | 676 | 504990 | -81.20 | 15.24 | 469.33 | 0.13 | 2.91 | 1566 |
| 2024-09-20 22:21:32.500 | MS1 | 121.4656660623 | 31.1446311427 | 676 | 504990 | -76.94 | 15.15 | 549.45 | 0.18 | 2.49 | 1595 |
| 2024-09-20 22:21:33.988 | MS1 | 121.4656750744 | 31.1446316733 | 676 | 504990 | -76.63 | 13.50 | 597.41 | 0.19 | 2.19 | 1565 |
| 2024-09-20 22:21:34.826 | MS1 | 121.4656661362 | 31.1446365020 | 676 | 504990 | -86.90 | -2.84 | 46.56 | 0.08 | 1.39 | 1568 |
| 2024-09-20 22:21:35.883 | MS1 | 121.4656761881 | 31.1446206725 | 676 | 504990 | -92.05 | -2.06 | 45.78 | 0.08 | 1.21 | 1578 |
| 2024-09-20 22:21:36.646 | MS1 | 121.4656748747 | 31.1446378495 | 676 | 504990 | -94.04 | -3.66 | 36.85 | 0.19 | 1.47 | 1565 |
| 2024-09-20 22:21:37.987 | MS1 | 121.4656650863 | 31.1446183357 | 676 | 504990 | -85.39 | -0.04 | 46.04 | 0.18 | 1.47 | 1584 |
| 2024-09-20 22:21:38.674 | MS1 | 121.4656677613 | 31.1446281722 | 676 | 504990 | -81.82 | 13.01 | 422.54 | 0.18 | 1.36 | 1589 |
| 2024-09-20 22:21:39.974 | MS1 | 121.4656627879 | 31.1446352721 | 676 | 504990 | -83.93 | 16.87 | 599.29 | 0.06 | 1.48 | 1598 |
| 2024-09-20 22:21:40.319 | MS1 | 121.4656742378 | 31.1446248763 | 676 | 504990 | -79.43 | 14.30 | 446.11 | 0.08 | 2.45 | 1583 |
| 2024-09-20 22:21:41.467 | MS1 | 121.4656752990 | 31.1446341756 | 676 | 504990 | -76.10 | 16.76 | 514.18 | 0.06 | 2.54 | 1586 |
| 2024-09-20 22:21:42.777 | MS1 | 121.4656657342 | 31.1446218524 | 676 | 504990 | -81.58 | 13.18 | 595.04 | 0.17 | 2.69 | 1593 |

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
| 3236280 | 2 | 121.4643820300 | 31.1450369829 | 33 | 12 | 8 | 18.5 | TDD | 336 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3264045 | 3 | 121.4640102751 | 31.1499509159 | 200 | 8 | 1 | 31.2 | TDD | 676 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3276752 | 4 | 121.4709568715 | 31.1537639076 | 187 | 7 | 3 | 44.8 | TDD | 517 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3277796 | 1 | 121.4758048009 | 31.1535211717 | 248 | 2 | 7 | 29.7 | TDD | 224 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.006 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.031 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.138 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.138 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.807 | NREventA3 | measId:2;ServCellPCI:610;Se... |
| 2024-09-20 22:21:35.807 | NREventA3 | measId:2;ServCellPCI:610;Se... |
| 2024-09-20 22:21:36.807 | NREventA3 | measId:2;ServCellPCI:610;Se... |
| 2024-09-20 22:21:39.307 | NRRRCReestablishAttempt | PCI:610 |
| 2024-09-20 22:21:39.326 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.340 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.466 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.466 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277796 | 1 | 11.2371 | 8.6454 | -116.4996 | 16.8262 | 136.2562 | 0.0185 | 0.0098 |
| 2024_09_20 22:00 | 3236280 | 2 | 19.2705 | 12.6483 | -114.7922 | 9.3286 | 160.9291 | 0.0122 | 0.0065 |
| 2024_09_20 22:00 | 3264045 | 3 | 19.6154 | 18.6930 | -117.9810 | 13.0484 | 145.1161 | 0.0165 | 0.1875 |
| 2024_09_20 22:00 | 3276752 | 4 | 6.5277 | 10.5575 | -114.8344 | 16.3357 | 144.6796 | 0.0136 | 0.0199 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414279_851DBF2E | 504990 | 676 | -88.3 | 504990 | 224 | -82.8 | 504990 | 336 | -86.7 | 504990 | 517 |
| MR_1774414279_67BC05D6 | 504990 | 224 | -81.5 | 504990 | 676 | -86.9 | 504990 | 336 | -83.7 | 504990 | 517 |
| MR_1774414279_5EAAC8AB | 504990 | 676 | -86.5 | 504990 | 224 | -83.4 | 504990 | 336 | -84.8 | 504990 | 517 |
| MR_1774414279_CE9E353F | 504990 | 676 | -87.7 | 504990 | 224 | -83.0 | 504990 | 336 | -86.2 | 504990 | 517 |
| MR_1774414279_9B2CC675 | 504990 | 676 | -86.6 | 504990 | 224 | -81.4 | 504990 | 336 | -85.2 | 504990 | 517 |
| MR_1774414279_7BEA35C3 | 504990 | 676 | -87.2 | 504990 | 224 | -81.4 | 504990 | 336 | -84.6 | 504990 | 517 |
| MR_1774414279_74568FF8 | 504990 | 676 | -85.7 | 504990 | 224 | -83.2 | 504990 | 336 | -84.5 | 504990 | 517 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1256: `5b8896f2-7e3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5b8896f2-7e37-4658-bee5-665a6488f003` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3213773_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1256] topology](images/train_1256.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3213773_2 by 5 degrees
- `C2`: Adjust the azimuth of 3213773_2 by 29 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213773_2
- `C4`: Press down the tilt angle  of 3258283_4 by 10 degrees
- `C5`: Decrease transmission power for 3213773_2
- `C6`: Add neighbor relationship between 3213773_2 and 3258283_4
- `C7`: Add neighbor relationship between 3225112_1 and 3258283_4
- `C8`: Lift the tilt angle of 3213773_2 by 5 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Adjust the azimuth of 3258283_4 by 50 degrees
- `C11`: Check test server and transmission issues
- `C12`: Decrease A3 Offset threshold for 3258283_4
- `C13`: Increase transmission power for 3213773_2
- `C14`: Lift the tilt angle  of 3258283_4 by 10 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213773_2 **← 정답**
- `C16`: Increase A3 Offset threshold for 3213773_2
- `C17`: Increase transmission power for 3258283_4
- `C18`: Decrease A3 Offset threshold for 3213773_2
- `C19`: Increase A3 Offset threshold for 3258283_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258283_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258283_4
- `C22`: Decrease transmission power for 3258283_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.249 | MS1 | 121.4656659901 | 31.1446240976 | 306 | 504990 | -90.81 | 16.31 | 530.69 | 0.13 | 2.75 | 1592 |
| 2024-09-20 22:21:32.581 | MS1 | 121.4656673655 | 31.1446333941 | 306 | 504990 | -87.92 | 17.72 | 348.10 | 0.13 | 2.09 | 1572 |
| 2024-09-20 22:21:33.500 | MS1 | 121.4656621676 | 31.1446180534 | 306 | 504990 | -87.49 | 15.54 | 374.51 | 0.16 | 2.28 | 1575 |
| 2024-09-20 22:21:34.306 | MS1 | 121.4656779364 | 31.1446347834 | 306 | 504990 | -89.66 | 17.63 | 60.04 | 0.50 | 2.15 | 587 |
| 2024-09-20 22:21:35.330 | MS1 | 121.4656762514 | 31.1446375952 | 306 | 504990 | -85.48 | 12.27 | 65.68 | 0.64 | 2.67 | 616 |
| 2024-09-20 22:21:36.266 | MS1 | 121.4656715734 | 31.1446339289 | 306 | 504990 | -87.70 | 15.86 | 55.19 | 0.65 | 2.05 | 657 |
| 2024-09-20 22:21:37.213 | MS1 | 121.4656657327 | 31.1446280987 | 306 | 504990 | -92.76 | 7.21 | 73.17 | 0.66 | 2.95 | 603 |
| 2024-09-20 22:21:38.735 | MS1 | 121.4656626891 | 31.1446210800 | 306 | 504990 | -91.75 | 12.11 | 80.97 | 0.68 | 2.41 | 551 |
| 2024-09-20 22:21:39.363 | MS1 | 121.4656697679 | 31.1446322827 | 306 | 504990 | -90.49 | 12.35 | 63.33 | 0.66 | 2.25 | 629 |
| 2024-09-20 22:21:40.896 | MS1 | 121.4656731586 | 31.1446243776 | 306 | 504990 | -92.58 | 11.38 | 544.10 | 0.18 | 2.75 | 1578 |
| 2024-09-20 22:21:41.814 | MS1 | 121.4656688416 | 31.1446267744 | 306 | 504990 | -90.73 | 11.35 | 435.35 | 0.06 | 2.48 | 1584 |
| 2024-09-20 22:21:42.563 | MS1 | 121.4656661860 | 31.1446379164 | 306 | 504990 | -91.39 | 8.22 | 426.88 | 0.02 | 2.60 | 1576 |

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
| 3213773 | 2 | 121.4740464728 | 31.1448782424 | 297 | 2 | 1 | 42.3 | TDD | 306 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3225112 | 1 | 121.4669754657 | 31.1550338712 | 119 | 15 | 3 | 33.7 | TDD | 768 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3258283 | 4 | 121.4670588569 | 31.1513626993 | 75 | 9 | 5 | 43.4 | TDD | 500 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3272668 | 3 | 121.4731985317 | 31.1557743010 | 204 | 4 | 2 | 27.0 | TDD | 156 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.801 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.817 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:30.932 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.932 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.693 | NREventA3 | measId:2;ServCellPCI:332;Se... |
| 2024-09-20 22:21:37.933 | NRHandoverAttempt | SourcePCI:332;SourceNR-ARFC... |
| 2024-09-20 22:21:37.968 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.982 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.132 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.132 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225112 | 1 | 11.3000 | 9.4357 | -115.2635 | 9.5768 | 102.3308 | 0.0017 | 0.0144 |
| 2024_09_20 22:00 | 3213773 | 2 | 13.1800 | 7.3609 | -114.4106 | 11.9184 | 122.7263 | 0.0118 | 0.0084 |
| 2024_09_20 22:00 | 3272668 | 3 | 10.6733 | 13.4185 | -117.0401 | 11.7618 | 151.6799 | 0.0181 | 0.0026 |
| 2024_09_20 22:00 | 3258283 | 4 | 13.4306 | 18.4825 | -117.1118 | 10.6461 | 148.7451 | 0.0100 | 0.0055 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416135_1137852B | 504990 | 306 | -89.6 | 504990 | 500 | -94.4 | 504990 | 768 | -99.1 | 504990 | 156 |
| MR_1774416135_EA967609 | 504990 | 306 | -91.1 | 504990 | 500 | -95.8 | 504990 | 768 | -98.1 | 504990 | 156 |
| MR_1774416135_5B369176 | 504990 | 306 | -90.8 | 504990 | 500 | -96.9 | 504990 | 768 | -96.6 | 504990 | 156 |
| MR_1774416135_130E9FC4 | 504990 | 306 | -90.8 | 504990 | 500 | -94.9 | 504990 | 768 | -96.7 | 504990 | 156 |
| MR_1774416135_385F8EEC | 504990 | 306 | -91.4 | 504990 | 500 | -95.2 | 504990 | 768 | -96.6 | 504990 | 156 |
| MR_1774416135_557E4DE9 | 504990 | 306 | -91.0 | 504990 | 500 | -95.2 | 504990 | 768 | -100.5 | 504990 | 156 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1257: `c6d14326-f55...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c6d14326-f558-4620-86e1-734d9c242cf7` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253602_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1257] topology](images/train_1257.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3253602_1 by 5 degrees
- `C2`: Increase transmission power for 3259222_3
- `C3`: Decrease A3 Offset threshold for 3259222_3
- `C4`: Decrease A3 Offset threshold for 3253602_1
- `C5`: Check test server and transmission issues
- `C6`: Press down the tilt angle  of 3259222_3 by 2 degrees
- `C7`: Decrease transmission power for 3259222_3
- `C8`: Press down the tilt angle of 3253602_1 by 5 degrees
- `C9`: Add neighbor relationship between 3253602_1 and 3259222_3
- `C10`: Decrease transmission power for 3253602_1
- `C11`: Adjust the azimuth of 3253602_1 by 33 degrees
- `C12`: Adjust the azimuth of 3259222_3 by 48 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253602_1 **← 정답**
- `C14`: Increase A3 Offset threshold for 3259222_3
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259222_3
- `C17`: Lift the tilt angle  of 3259222_3 by 2 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253602_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259222_3
- `C20`: Add neighbor relationship between 3220006_10 and 3259222_3
- `C21`: Increase A3 Offset threshold for 3253602_1
- `C22`: Increase transmission power for 3253602_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.243 | MS1 | 121.4656642667 | 31.1446306843 | 482 | 504990 | -95.77 | 14.48 | 351.68 | 0.12 | 2.15 | 1571 |
| 2024-09-20 22:21:32.778 | MS1 | 121.4656716883 | 31.1446262776 | 697 | 504990 | -94.92 | 11.73 | 361.11 | 0.13 | 2.55 | 1584 |
| 2024-09-20 22:21:33.197 | MS1 | 121.4656754195 | 31.1446316732 | 255 | 504990 | -93.50 | 14.38 | 477.70 | 0.09 | 2.54 | 1576 |
| 2024-09-20 22:21:34.444 | MS1 | 121.4656751146 | 31.1446307413 | 738 | 152650 | -96.80 | 7.28 | 84.20 | 0.09 | 1.52 | 956 |
| 2024-09-20 22:21:35.376 | MS1 | 121.4656742131 | 31.1446246400 | 440 | 152650 | -92.93 | 7.63 | 83.22 | 0.15 | 1.53 | 903 |
| 2024-09-20 22:21:36.237 | MS1 | 121.4656663646 | 31.1446357346 | 820 | 152650 | -93.68 | 2.10 | 92.58 | 0.13 | 1.92 | 978 |
| 2024-09-20 22:21:37.945 | MS1 | 121.4656722665 | 31.1446352475 | 563 | 152650 | -90.63 | 4.96 | 56.84 | 0.12 | 1.91 | 945 |
| 2024-09-20 22:21:38.241 | MS1 | 121.4656754066 | 31.1446311278 | 738 | 152650 | -95.89 | 2.08 | 70.55 | 0.02 | 1.76 | 941 |
| 2024-09-20 22:21:39.558 | MS1 | 121.4656592904 | 31.1446337666 | 440 | 152650 | -96.97 | 4.15 | 67.73 | 0.13 | 1.98 | 986 |
| 2024-09-20 22:21:40.199 | MS1 | 121.4656661724 | 31.1446273666 | 820 | 152650 | -93.75 | 6.36 | 92.53 | 0.01 | 2.09 | 1595 |
| 2024-09-20 22:21:41.131 | MS1 | 121.4656590669 | 31.1446190315 | 563 | 152650 | -95.51 | 3.19 | 66.25 | 0.14 | 2.04 | 1590 |
| 2024-09-20 22:21:42.470 | MS1 | 121.4656710694 | 31.1446316037 | 738 | 152650 | -96.40 | 3.56 | 68.83 | 0.08 | 2.21 | 1560 |

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
| 3212358 | 11 | 121.4747712915 | 31.1448289158 | 192 | 11 | 5 | 26.0 | FDD | 434 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3212787 | 4 | 121.4745533175 | 31.1473119941 | 110 | 11 | 7 | 8.7 | TDD | 232 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3220006 | 10 | 121.4717336150 | 31.1513101276 | 246 | 5 | 6 | 13.8 | FDD | 820 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3227411 | 13 | 121.4724787867 | 31.1471300827 | 168 | 10 | 11 | 24.7 | FDD | 440 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3242115 | 12 | 121.4667718193 | 31.1550738368 | 219 | 1 | 7 | 22.2 | FDD | 406 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3243798 | 7 | 121.4700837023 | 31.1538172015 | 323 | 5 | 7 | 18.0 | FDD | 738 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3253297 | 8 | 121.4755990087 | 31.1498318923 | 20 | 2 | 5 | 20.2 | FDD | 466 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3253602 | 1 | 121.4718194009 | 31.1444134990 | 239 | 3 | 9 | 20.8 | TDD | 482 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3254130 | 9 | 121.4688198944 | 31.1511453834 | 256 | 1 | 0 | 24.5 | FDD | 563 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3259222 | 3 | 121.4685600317 | 31.1515151737 | 248 | 2 | 5 | 4.3 | TDD | 648 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3265302 | 6 | 121.4683682786 | 31.1508672687 | 99 | 13 | 2 | 9.5 | TDD | 831 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3271211 | 5 | 121.4671470430 | 31.1442759351 | 80 | 13 | 8 | 19.8 | TDD | 697 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3279789 | 2 | 121.4684816629 | 31.1455175114 | 266 | 14 | 10 | 8.6 | TDD | 255 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.531 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.549 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.681 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.681 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.373 | NREventA2 | measId:1;ServCellPCI:897;Se... |
| 2024-09-20 22:21:35.521 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.732 | NREventA5 | measId:3;ServCellPCI:897;Se... |
| 2024-09-20 22:21:35.762 | NRHandoverAttempt | SourcePCI:897;SourceNR-ARFC... |
| 2024-09-20 22:21:35.808 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.819 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.952 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.952 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253602 | 1 | 13.5644 | 12.7413 | -117.0525 | 18.1680 | 155.0502 | 0.0105 | 0.0002 |
| 2024_09_20 22:00 | 3279789 | 2 | 15.6265 | 9.7504 | -116.7677 | 5.7845 | 92.9889 | 0.0111 | 0.0047 |
| 2024_09_20 22:00 | 3259222 | 3 | 10.2149 | 18.6794 | -114.4363 | 17.0086 | 163.2466 | 0.0109 | 0.0128 |
| 2024_09_20 22:00 | 3212787 | 4 | 16.0128 | 15.1604 | -115.4418 | 16.8857 | 97.3780 | 0.0029 | 0.0169 |
| 2024_09_20 22:00 | 3271211 | 5 | 11.5765 | 17.5146 | -117.9549 | 8.5620 | 162.8182 | 0.0002 | 0.0163 |
| 2024_09_20 22:00 | 3265302 | 6 | 8.0713 | 16.1603 | -115.4244 | 8.1209 | 197.8242 | 0.0166 | 0.0128 |
| 2024_09_20 22:00 | 3243798 | 7 | 11.7499 | 10.3912 | -114.1319 | 4.1616 | 46.1655 | 0.0162 | 0.0132 |
| 2024_09_20 22:00 | 3253297 | 8 | 14.1268 | 15.0000 | -114.6827 | 4.3713 | 38.7045 | 0.0133 | 0.0074 |
| 2024_09_20 22:00 | 3254130 | 9 | 18.0525 | 9.1417 | -117.3801 | 4.6083 | 56.0484 | 0.0147 | 0.0177 |
| 2024_09_20 22:00 | 3220006 | 10 | 14.7968 | 18.0716 | -117.9868 | 4.6612 | 52.6782 | 0.0186 | 0.0018 |
| 2024_09_20 22:00 | 3212358 | 11 | 6.1249 | 10.2669 | -115.8430 | 3.5019 | 45.4889 | 0.0047 | 0.0126 |
| 2024_09_20 22:00 | 3242115 | 12 | 13.2722 | 17.6734 | -115.7860 | 4.1089 | 44.4707 | 0.0050 | 0.0100 |
| 2024_09_20 22:00 | 3227411 | 13 | 14.0951 | 11.5279 | -117.8423 | 3.8528 | 53.6733 | 0.0018 | 0.0199 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415059_04B32C4E | 152650 | 738 | -95.4 | 152650 | 406 | -103.1 | 152650 | 466 | -104.8 | 152650 | 434 |
| MR_1774415059_613B2603 | 504990 | 255 | -95.1 | 504990 | 648 | -89.0 | 504990 | 831 | -93.5 | 504990 | 232 |
| MR_1774415059_42B1F1C5 | 152650 | 738 | -95.9 | 152650 | 406 | -103.9 | 152650 | 466 | -104.6 | 152650 | 434 |
| MR_1774415059_D09C7BCC | 152650 | 738 | -97.3 | 152650 | 406 | -103.3 | 152650 | 466 | -105.2 | 152650 | 434 |
| MR_1774415059_5F0F71AA | 152650 | 738 | -98.1 | 152650 | 406 | -103.0 | 152650 | 466 | -104.4 | 152650 | 434 |
| MR_1774415059_63AFF965 | 504990 | 255 | -95.0 | 504990 | 648 | -87.9 | 504990 | 831 | -92.6 | 504990 | 232 |
| MR_1774415059_F9F69B3E | 152650 | 738 | -97.1 | 152650 | 406 | -102.3 | 152650 | 466 | -103.6 | 152650 | 434 |
| MR_1774415059_490CA947 | 152650 | 738 | -98.1 | 152650 | 406 | -103.6 | 152650 | 466 | -104.9 | 152650 | 434 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1258: `c5d7073e-22d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c5d7073e-22d4-4a9b-8647-c6c1f2ba3c12` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1258] topology](images/train_1258.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3230474_3 by 10 degrees
- `C2`: Increase transmission power for 3230474_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230474_3
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease A3 Offset threshold for 3230474_3
- `C6`: Increase transmission power for 3253060_4
- `C7`: Increase A3 Offset threshold for 3253060_4
- `C8`: Decrease transmission power for 3253060_4
- `C9`: Adjust the azimuth of 3230474_3 by 50 degrees
- `C10`: Press down the tilt angle of 3253060_4 by 8 degrees
- `C11`: Lift the tilt angle of 3253060_4 by 8 degrees
- `C12`: Lift the tilt angle  of 3230474_3 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3253060_4
- `C14`: Check test server and transmission issues **← 정답**
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253060_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230474_3
- `C17`: Add neighbor relationship between 3239654_1 and 3230474_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253060_4
- `C19`: Adjust the azimuth of 3253060_4 by 50 degrees
- `C20`: Increase A3 Offset threshold for 3230474_3
- `C21`: Decrease transmission power for 3230474_3
- `C22`: Add neighbor relationship between 3253060_4 and 3230474_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.574 | MS1 | 121.4656651578 | 31.1446203675 | 535 | 504990 | -89.24 | 17.54 | 556.33 | 0.03 | 2.08 | 1563 |
| 2024-09-20 22:21:32.495 | MS1 | 121.4656590642 | 31.1446215417 | 535 | 504990 | -88.53 | 17.82 | 469.38 | 0.06 | 2.46 | 1594 |
| 2024-09-20 22:21:33.657 | MS1 | 121.4656697034 | 31.1446377435 | 535 | 504990 | -86.67 | 14.66 | 417.11 | 0.10 | 2.71 | 1576 |
| 2024-09-20 22:21:34.430 | MS1 | 121.4656683820 | 31.1446245023 | 535 | 504990 | -91.24 | 13.49 | 49.34 | 0.01 | 2.51 | 351 |
| 2024-09-20 22:21:35.718 | MS1 | 121.4656767728 | 31.1446339332 | 535 | 504990 | -86.53 | 16.71 | 70.82 | 0.13 | 2.25 | 444 |
| 2024-09-20 22:21:36.456 | MS1 | 121.4656777626 | 31.1446188521 | 535 | 504990 | -88.46 | 15.65 | 93.55 | 0.12 | 2.98 | 307 |
| 2024-09-20 22:21:37.641 | MS1 | 121.4656743043 | 31.1446294584 | 535 | 504990 | -93.13 | 7.16 | 49.74 | 0.12 | 2.73 | 369 |
| 2024-09-20 22:21:38.477 | MS1 | 121.4656635704 | 31.1446272966 | 535 | 504990 | -90.62 | 7.53 | 91.07 | 0.15 | 2.95 | 490 |
| 2024-09-20 22:21:39.712 | MS1 | 121.4656610239 | 31.1446331038 | 535 | 504990 | -91.08 | 10.14 | 71.52 | 0.11 | 2.49 | 488 |
| 2024-09-20 22:21:40.547 | MS1 | 121.4656607625 | 31.1446192951 | 535 | 504990 | -89.69 | 8.38 | 359.79 | 0.04 | 2.77 | 1586 |
| 2024-09-20 22:21:41.472 | MS1 | 121.4656617225 | 31.1446300221 | 535 | 504990 | -91.69 | 12.40 | 310.35 | 0.08 | 2.91 | 1596 |
| 2024-09-20 22:21:42.550 | MS1 | 121.4656588118 | 31.1446287386 | 535 | 504990 | -93.15 | 12.53 | 416.55 | 0.18 | 2.22 | 1567 |

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
| 3230474 | 3 | 121.4641366031 | 31.1448041524 | 182 | 7 | 7 | 26.5 | TDD | 605 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3237178 | 2 | 121.4682593680 | 31.1494373570 | 75 | 5 | 9 | 26.0 | TDD | 780 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3239654 | 1 | 121.4678687171 | 31.1473956465 | 252 | 5 | 5 | 21.0 | TDD | 674 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3253060 | 4 | 121.4681001351 | 31.1502618856 | 310 | 4 | 6 | 44.7 | TDD | 535 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.079 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.101 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.219 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.219 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.920 | NREventA3 | measId:2;ServCellPCI:355;Se... |
| 2024-09-20 22:21:38.160 | NRHandoverAttempt | SourcePCI:355;SourceNR-ARFC... |
| 2024-09-20 22:21:38.201 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.216 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.323 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.323 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239654 | 1 | 19.0756 | 15.6566 | -114.9152 | 12.2906 | 150.1173 | 0.0005 | 0.0087 |
| 2024_09_20 22:00 | 3237178 | 2 | 14.3588 | 13.4426 | -115.5186 | 17.6196 | 131.0263 | 0.0138 | 0.0182 |
| 2024_09_20 22:00 | 3230474 | 3 | 10.7039 | 17.2229 | -116.7129 | 10.8866 | 195.6671 | 0.0194 | 0.0100 |
| 2024_09_20 22:00 | 3253060 | 4 | 9.0482 | 5.8286 | -114.4099 | 8.5789 | 173.0762 | 0.0147 | 0.0167 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417128_CE36F71A | 504990 | 535 | -91.0 | 504990 | 605 | -89.5 | 504990 | 674 | -104.8 | 504990 | 780 |
| MR_1774417128_D8F90607 | 504990 | 535 | -89.3 | 504990 | 605 | -90.6 | 504990 | 674 | -104.3 | 504990 | 780 |
| MR_1774417128_877BFB22 | 504990 | 535 | -89.9 | 504990 | 605 | -91.8 | 504990 | 674 | -104.5 | 504990 | 780 |
| MR_1774417128_2C034A9A | 504990 | 535 | -92.7 | 504990 | 605 | -89.6 | 504990 | 674 | -102.7 | 504990 | 780 |
| MR_1774417128_D45DDE6C | 504990 | 535 | -90.5 | 504990 | 605 | -89.7 | 504990 | 674 | -105.4 | 504990 | 780 |
| MR_1774417128_622F47EB | 504990 | 535 | -92.8 | 504990 | 605 | -89.3 | 504990 | 674 | -104.7 | 504990 | 780 |
| MR_1774417128_3EE54012 | 504990 | 535 | -89.9 | 504990 | 605 | -92.8 | 504990 | 674 | -103.3 | 504990 | 780 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1259: `36a2c1db-432...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `36a2c1db-4321-48c0-ab36-a00b1dbe7001` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease A3 Offset threshold for 3224128_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1259] topology](images/train_1259.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3224497_2
- `C2`: Lift the tilt angle of 3224128_1 by 10 degrees
- `C3`: Add neighbor relationship between 3224128_1 and 3224497_2
- `C4`: Adjust the azimuth of 3224497_2 by 50 degrees
- `C5`: Increase transmission power for 3224128_1
- `C6`: Add neighbor relationship between 3235207_3 and 3224497_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Press down the tilt angle of 3224128_1 by 10 degrees
- `C9`: Decrease transmission power for 3224497_2
- `C10`: Check test server and transmission issues
- `C11`: Lift the tilt angle  of 3224497_2 by 10 degrees
- `C12`: Decrease A3 Offset threshold for 3224128_1 **← 정답**
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224497_2
- `C14`: Decrease transmission power for 3224128_1
- `C15`: Adjust the azimuth of 3224128_1 by 50 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224128_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224128_1
- `C18`: Increase A3 Offset threshold for 3224128_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224497_2
- `C20`: Increase A3 Offset threshold for 3224497_2
- `C21`: Decrease A3 Offset threshold for 3224497_2
- `C22`: Press down the tilt angle  of 3224497_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.240 | MS1 | 121.4656719388 | 31.1446199339 | 728 | 504990 | -84.16 | 12.08 | 304.12 | 0.07 | 2.38 | 1574 |
| 2024-09-20 22:21:32.950 | MS1 | 121.4656701874 | 31.1446336327 | 728 | 504990 | -78.63 | 15.30 | 346.10 | 0.16 | 2.58 | 1576 |
| 2024-09-20 22:21:33.276 | MS1 | 121.4656711711 | 31.1446200090 | 728 | 504990 | -80.48 | 13.44 | 467.60 | 0.01 | 2.88 | 1595 |
| 2024-09-20 22:21:34.210 | MS1 | 121.4656764004 | 31.1446255825 | 728 | 504990 | -89.09 | -1.04 | 61.74 | 0.13 | 1.02 | 1582 |
| 2024-09-20 22:21:35.711 | MS1 | 121.4656703142 | 31.1446236732 | 728 | 504990 | -88.20 | -3.68 | 59.02 | 0.19 | 1.28 | 1581 |
| 2024-09-20 22:21:36.751 | MS1 | 121.4656641840 | 31.1446244096 | 728 | 504990 | -90.59 | -2.76 | 47.16 | 0.08 | 1.43 | 1595 |
| 2024-09-20 22:21:37.559 | MS1 | 121.4656663424 | 31.1446209447 | 728 | 504990 | -86.76 | -0.50 | 62.64 | 0.06 | 1.22 | 1569 |
| 2024-09-20 22:21:38.662 | MS1 | 121.4656622536 | 31.1446299387 | 728 | 504990 | -86.23 | -2.62 | 40.13 | 0.17 | 1.10 | 1588 |
| 2024-09-20 22:21:39.199 | MS1 | 121.4656758874 | 31.1446231281 | 145 | 504990 | -81.32 | 13.08 | 283.76 | 0.08 | 1.37 | 1586 |
| 2024-09-20 22:21:40.466 | MS1 | 121.4656774462 | 31.1446244045 | 145 | 504990 | -79.32 | 14.15 | 303.53 | 0.15 | 2.61 | 1572 |
| 2024-09-20 22:21:41.150 | MS1 | 121.4656635965 | 31.1446214168 | 145 | 504990 | -79.35 | 17.17 | 461.46 | 0.01 | 2.19 | 1575 |
| 2024-09-20 22:21:42.793 | MS1 | 121.4656662770 | 31.1446247604 | 145 | 504990 | -81.49 | 13.62 | 417.29 | 0.17 | 2.93 | 1590 |

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
| 3224128 | 1 | 121.4669025151 | 31.1530149672 | 293 | 10 | 2 | 35.2 | TDD | 728 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3224497 | 2 | 121.4712639272 | 31.1507152153 | 22 | 9 | 3 | 24.7 | TDD | 145 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3235207 | 3 | 121.4679037032 | 31.1523555869 | 311 | 10 | 5 | 22.5 | TDD | 136 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3270295 | 4 | 121.4746636253 | 31.1492562337 | 50 | 3 | 0 | 16.5 | TDD | 801 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.480 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.581 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.581 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.321 | NREventA3 | measId:2;ServCellPCI:797;Se... |
| 2024-09-20 22:21:38.561 | NRHandoverAttempt | SourcePCI:797;SourceNR-ARFC... |
| 2024-09-20 22:21:38.607 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.622 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.731 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.731 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224128 | 1 | 16.2319 | 15.9535 | -117.1396 | 5.6172 | 151.8783 | 0.0045 | 0.1944 |
| 2024_09_20 22:00 | 3224497 | 2 | 19.2676 | 19.8049 | -114.8625 | 12.9528 | 146.7277 | 0.0195 | 0.0121 |
| 2024_09_20 22:00 | 3235207 | 3 | 15.6503 | 5.8864 | -115.3610 | 19.2010 | 82.8504 | 0.0075 | 0.0033 |
| 2024_09_20 22:00 | 3270295 | 4 | 9.6626 | 15.8412 | -116.6750 | 10.2372 | 93.7128 | 0.0082 | 0.0076 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414500_CEEC42ED | 504990 | 145 | -85.0 | 504990 | 728 | -87.9 | 504990 | 136 | -89.2 | 504990 | 801 |
| MR_1774414500_79029355 | 504990 | 728 | -87.6 | 504990 | 145 | -86.7 | 504990 | 136 | -88.4 | 504990 | 801 |
| MR_1774414500_25E499E9 | 504990 | 145 | -83.5 | 504990 | 728 | -89.8 | 504990 | 136 | -87.4 | 504990 | 801 |
| MR_1774414500_EBC15FBE | 504990 | 145 | -83.7 | 504990 | 728 | -87.1 | 504990 | 136 | -88.8 | 504990 | 801 |
| MR_1774414500_3D9CA75D | 504990 | 145 | -86.3 | 504990 | 728 | -88.2 | 504990 | 136 | -89.5 | 504990 | 801 |
| MR_1774414500_72EF157A | 504990 | 728 | -87.9 | 504990 | 145 | -84.3 | 504990 | 136 | -88.5 | 504990 | 801 |

> *... 2개 열 생략 (전체 14열)*

---
