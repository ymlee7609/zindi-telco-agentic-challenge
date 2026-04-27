# Track A 문제 분석 — train[110]~train[119]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[110] ~ train[119] (10개)

## 목차

1. [문제 110: `1a5e983c-72f...`](#110) — single-answer, 정답: C13
2. [문제 111: `b9da73f6-a95...`](#111) — single-answer, 정답: C11
3. [문제 112: `cfc39757-52c...`](#112) — single-answer, 정답: C20
4. [문제 113: `8e5e506b-3d5...`](#113) — single-answer, 정답: C2
5. [문제 114: `46a37242-f8a...`](#114) — single-answer, 정답: C2
6. [문제 115: `77ffffa9-6f2...`](#115) — single-answer, 정답: C10
7. [문제 116: `f9cd0ca5-0f8...`](#116) — single-answer, 정답: C20
8. [문제 117: `bea2aee2-10e...`](#117) — single-answer, 정답: C13
9. [문제 118: `0938209f-a67...`](#118) — single-answer, 정답: C22
10. [문제 119: `43e8ab0c-50a...`](#119) — single-answer, 정답: C15

---

### 문제 110: `1a5e983c-72f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1a5e983c-72fd-4ed6-9db6-d2d6f59c2367` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease A3 Offset threshold for 3237273_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[110] topology](images/train_0110.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Add neighbor relationship between 3247971_4 and 3222299_2
- `C3`: Decrease transmission power for 3222299_2
- `C4`: Adjust the azimuth of 3222299_2 by 50 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237273_1
- `C6`: Decrease A3 Offset threshold for 3222299_2
- `C7`: Lift the tilt angle  of 3222299_2 by 8 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237273_1
- `C9`: Increase A3 Offset threshold for 3237273_1
- `C10`: Increase A3 Offset threshold for 3222299_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222299_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease A3 Offset threshold for 3237273_1 **← 정답**
- `C14`: Press down the tilt angle of 3237273_1 by 4 degrees
- `C15`: Adjust the azimuth of 3237273_1 by 26 degrees
- `C16`: Press down the tilt angle  of 3222299_2 by 8 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222299_2
- `C18`: Increase transmission power for 3222299_2
- `C19`: Decrease transmission power for 3237273_1
- `C20`: Add neighbor relationship between 3237273_1 and 3222299_2
- `C21`: Lift the tilt angle of 3237273_1 by 4 degrees
- `C22`: Increase transmission power for 3237273_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.210 | MS1 | 121.4656645864 | 31.1446237958 | 576 | 504990 | -83.42 | 17.49 | 547.47 | 0.15 | 2.30 | 1584 |
| 2024-09-20 22:21:32.260 | MS1 | 121.4656767694 | 31.1446260018 | 576 | 504990 | -83.85 | 12.28 | 428.20 | 0.19 | 2.71 | 1566 |
| 2024-09-20 22:21:33.340 | MS1 | 121.4656699816 | 31.1446357532 | 576 | 504990 | -82.34 | 13.08 | 312.90 | 0.08 | 2.60 | 1585 |
| 2024-09-20 22:21:34.531 | MS1 | 121.4656745077 | 31.1446240616 | 576 | 504990 | -87.38 | -3.43 | 68.75 | 0.16 | 1.44 | 1570 |
| 2024-09-20 22:21:35.129 | MS1 | 121.4656745361 | 31.1446188708 | 576 | 504990 | -87.86 | -3.36 | 50.33 | 0.16 | 1.05 | 1599 |
| 2024-09-20 22:21:36.508 | MS1 | 121.4656582889 | 31.1446368187 | 576 | 504990 | -88.28 | -0.38 | 54.88 | 0.06 | 1.29 | 1592 |
| 2024-09-20 22:21:37.303 | MS1 | 121.4656588486 | 31.1446293197 | 576 | 504990 | -83.36 | -0.78 | 53.90 | 0.06 | 1.36 | 1562 |
| 2024-09-20 22:21:38.465 | MS1 | 121.4656715730 | 31.1446266793 | 576 | 504990 | -91.30 | -1.82 | 38.09 | 0.01 | 1.08 | 1561 |
| 2024-09-20 22:21:39.279 | MS1 | 121.4656677966 | 31.1446349925 | 826 | 504990 | -76.95 | 12.88 | 282.92 | 0.15 | 1.34 | 1566 |
| 2024-09-20 22:21:40.168 | MS1 | 121.4656758577 | 31.1446293751 | 826 | 504990 | -79.95 | 17.65 | 505.22 | 0.16 | 2.11 | 1594 |
| 2024-09-20 22:21:41.554 | MS1 | 121.4656649541 | 31.1446225835 | 826 | 504990 | -82.13 | 14.19 | 398.20 | 0.17 | 2.53 | 1582 |
| 2024-09-20 22:21:42.134 | MS1 | 121.4656703002 | 31.1446371549 | 826 | 504990 | -76.14 | 14.04 | 512.04 | 0.09 | 2.52 | 1574 |

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
| 3222299 | 2 | 121.4758073896 | 31.1559335536 | 13 | 6 | 2 | 44.3 | TDD | 826 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3237273 | 1 | 121.4680265614 | 31.1551716194 | 217 | 3 | 4 | 25.9 | TDD | 576 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3242239 | 3 | 121.4640127042 | 31.1444463922 | 356 | 8 | 10 | 26.0 | TDD | 482 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3247971 | 4 | 121.4643584700 | 31.1480339729 | 2 | 9 | 4 | 25.1 | TDD | 686 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.543 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.567 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.682 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.682 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.396 | NREventA3 | measId:2;ServCellPCI:391;Se... |
| 2024-09-20 22:21:38.636 | NRHandoverAttempt | SourcePCI:391;SourceNR-ARFC... |
| 2024-09-20 22:21:38.680 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.692 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.835 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.835 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237273 | 1 | 8.1627 | 7.3574 | -115.0791 | 15.4591 | 183.7230 | 0.0181 | 0.1715 |
| 2024_09_20 22:00 | 3222299 | 2 | 11.0716 | 17.4294 | -115.4158 | 16.7847 | 99.4448 | 0.0196 | 0.0063 |
| 2024_09_20 22:00 | 3242239 | 3 | 7.5406 | 9.1766 | -117.9059 | 6.4537 | 87.7854 | 0.0135 | 0.0008 |
| 2024_09_20 22:00 | 3247971 | 4 | 9.9745 | 9.9989 | -117.3574 | 6.3361 | 84.5508 | 0.0058 | 0.0084 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415542_4860FC45 | 504990 | 576 | -86.1 | 504990 | 826 | -83.4 | 504990 | 686 | -90.6 | 504990 | 482 |
| MR_1774415542_B3873617 | 504990 | 576 | -88.6 | 504990 | 826 | -81.4 | 504990 | 686 | -89.6 | 504990 | 482 |
| MR_1774415542_A0F4189F | 504990 | 826 | -81.8 | 504990 | 576 | -87.1 | 504990 | 686 | -88.8 | 504990 | 482 |
| MR_1774415542_28751801 | 504990 | 576 | -88.7 | 504990 | 826 | -81.1 | 504990 | 686 | -88.3 | 504990 | 482 |
| MR_1774415542_9B452267 | 504990 | 826 | -83.7 | 504990 | 576 | -86.8 | 504990 | 686 | -89.0 | 504990 | 482 |
| MR_1774415542_79C39178 | 504990 | 576 | -85.4 | 504990 | 826 | -80.2 | 504990 | 686 | -90.2 | 504990 | 482 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 111: `b9da73f6-a95...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b9da73f6-a957-4df9-9956-3cc53ccbf419` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211667_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[111] topology](images/train_0111.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3232082_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase A3 Offset threshold for 3232082_2
- `C4`: Add neighbor relationship between 3216334_11 and 3232082_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211667_4
- `C6`: Press down the tilt angle  of 3232082_2 by 2 degrees
- `C7`: Increase transmission power for 3211667_4
- `C8`: Decrease A3 Offset threshold for 3211667_4
- `C9`: Lift the tilt angle of 3211667_4 by 5 degrees
- `C10`: Add neighbor relationship between 3211667_4 and 3232082_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211667_4 **← 정답**
- `C12`: Adjust the azimuth of 3232082_2 by 16 degrees
- `C13`: Increase transmission power for 3232082_2
- `C14`: Press down the tilt angle of 3211667_4 by 5 degrees
- `C15`: Decrease transmission power for 3211667_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232082_2
- `C17`: Check test server and transmission issues
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232082_2
- `C19`: Increase A3 Offset threshold for 3211667_4
- `C20`: Decrease transmission power for 3232082_2
- `C21`: Adjust the azimuth of 3211667_4 by 19 degrees
- `C22`: Lift the tilt angle  of 3232082_2 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.554 | MS1 | 121.4656767483 | 31.1446229644 | 936 | 504990 | -94.87 | 11.80 | 409.74 | 0.19 | 2.19 | 1571 |
| 2024-09-20 22:21:32.758 | MS1 | 121.4656742437 | 31.1446205114 | 417 | 504990 | -94.82 | 14.03 | 524.20 | 0.14 | 2.76 | 1596 |
| 2024-09-20 22:21:33.838 | MS1 | 121.4656656064 | 31.1446241728 | 411 | 504990 | -93.78 | 13.13 | 368.93 | 0.02 | 2.16 | 1589 |
| 2024-09-20 22:21:34.992 | MS1 | 121.4656713265 | 31.1446214432 | 643 | 152650 | -96.71 | 3.11 | 72.89 | 0.00 | 1.68 | 925 |
| 2024-09-20 22:21:35.578 | MS1 | 121.4656763409 | 31.1446192258 | 107 | 152650 | -92.42 | 7.61 | 67.02 | 0.08 | 1.55 | 912 |
| 2024-09-20 22:21:36.669 | MS1 | 121.4656647273 | 31.1446297819 | 51 | 152650 | -94.28 | 3.22 | 66.67 | 0.06 | 1.81 | 984 |
| 2024-09-20 22:21:37.710 | MS1 | 121.4656744819 | 31.1446325659 | 481 | 152650 | -94.39 | 5.39 | 91.29 | 0.03 | 1.53 | 949 |
| 2024-09-20 22:21:38.625 | MS1 | 121.4656715254 | 31.1446361176 | 643 | 152650 | -92.77 | 3.20 | 91.07 | 0.09 | 1.77 | 962 |
| 2024-09-20 22:21:39.999 | MS1 | 121.4656757324 | 31.1446224410 | 107 | 152650 | -93.74 | 2.20 | 84.24 | 0.17 | 1.57 | 959 |
| 2024-09-20 22:21:40.257 | MS1 | 121.4656762899 | 31.1446328983 | 51 | 152650 | -92.19 | 4.34 | 88.41 | 0.15 | 2.69 | 1596 |
| 2024-09-20 22:21:41.442 | MS1 | 121.4656615639 | 31.1446350377 | 481 | 152650 | -89.81 | 5.69 | 59.42 | 0.02 | 2.58 | 1592 |
| 2024-09-20 22:21:42.709 | MS1 | 121.4656760469 | 31.1446283207 | 643 | 152650 | -94.41 | 3.06 | 48.30 | 0.17 | 2.23 | 1572 |

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
| 3211667 | 4 | 121.4696526697 | 31.1488168172 | 238 | 5 | 3 | 3.6 | TDD | 936 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3216334 | 11 | 121.4675305103 | 31.1529683453 | 251 | 7 | 2 | 8.9 | FDD | 51 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3232082 | 2 | 121.4712358941 | 31.1470806675 | 259 | 0 | 12 | 22.5 | TDD | 195 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3233689 | 10 | 121.4754408439 | 31.1527006874 | 25 | 13 | 10 | 11.3 | FDD | 107 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3234320 | 6 | 121.4688477291 | 31.1453853923 | 94 | 1 | 4 | 17.2 | TDD | 411 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3237035 | 9 | 121.4675174616 | 31.1542429452 | 150 | 12 | 8 | 2.1 | FDD | 490 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3244868 | 5 | 121.4703379685 | 31.1474338427 | 22 | 3 | 10 | 9.3 | TDD | 180 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3245426 | 8 | 121.4645064701 | 31.1493817271 | 76 | 2 | 9 | 20.2 | FDD | 643 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3248366 | 13 | 121.4699339984 | 31.1441239825 | 315 | 11 | 4 | 10.5 | FDD | 639 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3249094 | 1 | 121.4663075989 | 31.1548268177 | 102 | 8 | 8 | 13.7 | TDD | 417 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3249127 | 7 | 121.4744732179 | 31.1529526562 | 28 | 1 | 12 | 20.3 | FDD | 481 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3268981 | 3 | 121.4752467643 | 31.1476601125 | 283 | 7 | 2 | 28.1 | TDD | 37 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3273380 | 12 | 121.4722572003 | 31.1491130398 | 88 | 14 | 8 | 29.7 | FDD | 950 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |

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
| 2024-09-20 22:21:31.166 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.302 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.302 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.007 | NREventA2 | measId:1;ServCellPCI:707;Se... |
| 2024-09-20 22:21:35.135 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.410 | NREventA5 | measId:3;ServCellPCI:707;Se... |
| 2024-09-20 22:21:35.488 | NRHandoverAttempt | SourcePCI:707;SourceNR-ARFC... |
| 2024-09-20 22:21:35.535 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.549 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.682 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.682 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249094 | 1 | 13.6203 | 14.4728 | -114.9565 | 14.8930 | 94.2960 | 0.0174 | 0.0080 |
| 2024_09_20 22:00 | 3232082 | 2 | 18.8535 | 19.6680 | -116.4373 | 8.8371 | 121.5586 | 0.0141 | 0.0080 |
| 2024_09_20 22:00 | 3268981 | 3 | 16.4823 | 10.0559 | -114.2818 | 12.3755 | 87.7890 | 0.0045 | 0.0006 |
| 2024_09_20 22:00 | 3211667 | 4 | 6.0752 | 8.2982 | -115.3955 | 9.7292 | 111.6521 | 0.0013 | 0.0181 |
| 2024_09_20 22:00 | 3244868 | 5 | 18.0264 | 19.8740 | -114.6584 | 13.7507 | 109.6081 | 0.0103 | 0.0173 |
| 2024_09_20 22:00 | 3234320 | 6 | 17.7692 | 17.7891 | -116.3361 | 12.9032 | 192.2573 | 0.0004 | 0.0162 |
| 2024_09_20 22:00 | 3249127 | 7 | 6.4347 | 11.9276 | -115.6101 | 4.3511 | 40.9164 | 0.0028 | 0.0174 |
| 2024_09_20 22:00 | 3245426 | 8 | 12.8640 | 12.9023 | -116.9800 | 3.4844 | 50.1828 | 0.0123 | 0.0113 |
| 2024_09_20 22:00 | 3237035 | 9 | 14.3592 | 7.9180 | -114.7130 | 4.1276 | 37.6428 | 0.0101 | 0.0143 |
| 2024_09_20 22:00 | 3233689 | 10 | 7.0266 | 19.4619 | -117.9006 | 4.2113 | 37.7969 | 0.0109 | 0.0063 |
| 2024_09_20 22:00 | 3216334 | 11 | 17.2700 | 8.0737 | -117.3290 | 4.3326 | 21.4022 | 0.0151 | 0.0199 |
| 2024_09_20 22:00 | 3273380 | 12 | 19.9477 | 12.8197 | -114.4488 | 4.0353 | 23.8212 | 0.0133 | 0.0043 |
| 2024_09_20 22:00 | 3248366 | 13 | 14.4887 | 10.9884 | -114.7102 | 4.6223 | 28.4714 | 0.0006 | 0.0108 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414654_42C44735 | 504990 | 411 | -93.9 | 504990 | 195 | -95.4 | 504990 | 180 | -98.8 | 504990 | 37 |
| MR_1774414654_AB5BA8BD | 152650 | 643 | -95.0 | 152650 | 950 | -102.9 | 152650 | 639 | -101.1 | 152650 | 490 |
| MR_1774414654_2080B3C2 | 152650 | 643 | -96.7 | 152650 | 950 | -104.0 | 152650 | 639 | -104.5 | 152650 | 490 |
| MR_1774414654_AC0A937F | 504990 | 411 | -91.9 | 504990 | 195 | -96.0 | 504990 | 180 | -99.9 | 504990 | 37 |
| MR_1774414654_CB6FCB37 | 504990 | 411 | -92.3 | 504990 | 195 | -95.6 | 504990 | 180 | -101.7 | 504990 | 37 |
| MR_1774414654_DF8EADCC | 504990 | 411 | -93.9 | 504990 | 195 | -97.5 | 504990 | 180 | -100.8 | 504990 | 37 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 112: `cfc39757-52c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cfc39757-52c5-4906-bccf-6abd153ca405` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease A3 Offset threshold for 3237485_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[112] topology](images/train_0112.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3243995_4 by 7 degrees
- `C2`: Increase transmission power for 3237485_3
- `C3`: Check test server and transmission issues
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Add neighbor relationship between 3271307_2 and 3243995_4
- `C6`: Increase transmission power for 3243995_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237485_3
- `C8`: Adjust the azimuth of 3237485_3 by 50 degrees
- `C9`: Increase A3 Offset threshold for 3237485_3
- `C10`: Increase A3 Offset threshold for 3243995_4
- `C11`: Press down the tilt angle of 3237485_3 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243995_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243995_4
- `C14`: Decrease transmission power for 3243995_4
- `C15`: Decrease A3 Offset threshold for 3243995_4
- `C16`: Decrease transmission power for 3237485_3
- `C17`: Lift the tilt angle  of 3243995_4 by 7 degrees
- `C18`: Add neighbor relationship between 3237485_3 and 3243995_4
- `C19`: Adjust the azimuth of 3243995_4 by 50 degrees
- `C20`: Decrease A3 Offset threshold for 3237485_3 **← 정답**
- `C21`: Lift the tilt angle of 3237485_3 by 10 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237485_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.936 | MS1 | 121.4656745970 | 31.1446180976 | 190 | 504990 | -78.79 | 12.18 | 513.67 | 0.07 | 2.54 | 1591 |
| 2024-09-20 22:21:32.738 | MS1 | 121.4656644971 | 31.1446235684 | 190 | 504990 | -76.55 | 14.53 | 313.72 | 0.08 | 2.48 | 1594 |
| 2024-09-20 22:21:33.844 | MS1 | 121.4656624617 | 31.1446320291 | 190 | 504990 | -76.73 | 14.79 | 369.55 | 0.09 | 2.31 | 1578 |
| 2024-09-20 22:21:34.479 | MS1 | 121.4656583039 | 31.1446180739 | 190 | 504990 | -85.74 | -0.51 | 63.22 | 0.01 | 1.22 | 1574 |
| 2024-09-20 22:21:35.914 | MS1 | 121.4656676490 | 31.1446281345 | 190 | 504990 | -87.55 | -2.59 | 45.63 | 0.14 | 1.01 | 1581 |
| 2024-09-20 22:21:36.794 | MS1 | 121.4656620342 | 31.1446221758 | 190 | 504990 | -84.04 | -3.98 | 63.69 | 0.11 | 1.47 | 1592 |
| 2024-09-20 22:21:37.773 | MS1 | 121.4656668701 | 31.1446256622 | 190 | 504990 | -89.63 | -0.05 | 73.89 | 0.04 | 1.26 | 1590 |
| 2024-09-20 22:21:38.571 | MS1 | 121.4656767192 | 31.1446358030 | 190 | 504990 | -87.06 | -0.81 | 32.28 | 0.16 | 1.16 | 1575 |
| 2024-09-20 22:21:39.196 | MS1 | 121.4656601874 | 31.1446227954 | 1003 | 504990 | -84.24 | 16.55 | 184.01 | 0.17 | 1.20 | 1563 |
| 2024-09-20 22:21:40.901 | MS1 | 121.4656711586 | 31.1446347221 | 1003 | 504990 | -82.26 | 15.91 | 415.39 | 0.07 | 2.64 | 1568 |
| 2024-09-20 22:21:41.920 | MS1 | 121.4656633725 | 31.1446313568 | 1003 | 504990 | -77.81 | 13.54 | 501.38 | 0.06 | 2.65 | 1571 |
| 2024-09-20 22:21:42.495 | MS1 | 121.4656709847 | 31.1446343710 | 1003 | 504990 | -80.85 | 12.35 | 410.07 | 0.06 | 2.54 | 1599 |

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
| 3237485 | 3 | 121.4704576945 | 31.1453360373 | 79 | 13 | 2 | 40.5 | TDD | 190 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3243995 | 4 | 121.4678968215 | 31.1532980311 | 54 | 6 | 4 | 23.0 | TDD | 1003 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3247160 | 1 | 121.4741137471 | 31.1514047883 | 261 | 3 | 5 | 42.4 | TDD | 18 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3271307 | 2 | 121.4713164627 | 31.1509972933 | 275 | 7 | 0 | 26.6 | TDD | 242 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.331 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.346 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.478 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.478 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.228 | NREventA3 | measId:2;ServCellPCI:26;Ser... |
| 2024-09-20 22:21:38.468 | NRHandoverAttempt | SourcePCI:26;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.501 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.515 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.659 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.659 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247160 | 1 | 7.8380 | 14.8531 | -117.4053 | 10.0027 | 156.4425 | 0.0115 | 0.0075 |
| 2024_09_20 22:00 | 3271307 | 2 | 11.2429 | 17.4139 | -115.7119 | 14.4859 | 89.5861 | 0.0145 | 0.0111 |
| 2024_09_20 22:00 | 3237485 | 3 | 9.8958 | 19.9269 | -114.0626 | 19.9324 | 187.1157 | 0.0066 | 0.1885 |
| 2024_09_20 22:00 | 3243995 | 4 | 16.7043 | 17.1441 | -116.9731 | 8.2799 | 100.1558 | 0.0182 | 0.0107 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413318_FF252DD1 | 504990 | 190 | -84.6 | 504990 | 1003 | -79.7 | 504990 | 242 | -83.3 | 504990 | 18 |
| MR_1774413318_A2A2DE56 | 504990 | 190 | -83.8 | 504990 | 1003 | -81.4 | 504990 | 242 | -83.9 | 504990 | 18 |
| MR_1774413318_12F538D8 | 504990 | 1003 | -80.3 | 504990 | 190 | -84.2 | 504990 | 242 | -83.3 | 504990 | 18 |
| MR_1774413318_6C6D034B | 504990 | 1003 | -80.6 | 504990 | 190 | -83.8 | 504990 | 242 | -83.0 | 504990 | 18 |
| MR_1774413318_A6F81CA5 | 504990 | 1003 | -81.5 | 504990 | 190 | -86.9 | 504990 | 242 | -85.0 | 504990 | 18 |
| MR_1774413318_89D106CA | 504990 | 190 | -87.4 | 504990 | 1003 | -78.8 | 504990 | 242 | -85.6 | 504990 | 18 |
| MR_1774413318_58A2EF16 | 504990 | 190 | -86.2 | 504990 | 1003 | -81.2 | 504990 | 242 | -83.4 | 504990 | 18 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 113: `8e5e506b-3d5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8e5e506b-3d57-4ac2-ac54-899967c3ea74` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Lift the tilt angle  of 3225563_4 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[113] topology](images/train_0113.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3260846_1
- `C2`: Lift the tilt angle  of 3225563_4 by 7 degrees **← 정답**
- `C3`: Decrease A3 Offset threshold for 3260846_1
- `C4`: Press down the tilt angle  of 3225563_4 by 7 degrees
- `C5`: Increase A3 Offset threshold for 3260846_1
- `C6`: Decrease A3 Offset threshold for 3228100_3
- `C7`: Add neighbor relationship between 3225563_4 and 3260846_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Adjust the azimuth of 3225563_4 by 50 degrees
- `C10`: Decrease transmission power for 3228100_3
- `C11`: Increase transmission power for 3228100_3
- `C12`: Press down the tilt angle of 3228100_3 by 1 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260846_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228100_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228100_3
- `C16`: Add neighbor relationship between 3228100_3 and 3260846_1
- `C17`: Lift the tilt angle of 3228100_3 by 1 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260846_1
- `C19`: Increase A3 Offset threshold for 3228100_3
- `C20`: Adjust the azimuth of 3228100_3 by 9 degrees
- `C21`: Decrease transmission power for 3260846_1
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.881 | MS1 | 121.4656661952 | 31.1446227075 | 989 | 504990 | -88.24 | 12.95 | 564.95 | 0.03 | 2.85 | 1578 |
| 2024-09-20 22:21:32.453 | MS1 | 121.4656684285 | 31.1446358806 | 989 | 504990 | -87.50 | 13.10 | 515.19 | 0.05 | 2.42 | 1588 |
| 2024-09-20 22:21:33.714 | MS1 | 121.4656605064 | 31.1446216276 | 989 | 504990 | -88.56 | 12.19 | 507.05 | 0.15 | 2.55 | 1586 |
| 2024-09-20 22:21:34.793 | MS1 | 121.4656771454 | 31.1446258114 | 989 | 504990 | -87.91 | 13.42 | 94.53 | 0.11 | 2.04 | 1582 |
| 2024-09-20 22:21:35.180 | MS1 | 121.4656732341 | 31.1446182812 | 989 | 504990 | -91.07 | 13.44 | 91.34 | 0.19 | 2.82 | 1570 |
| 2024-09-20 22:21:36.717 | MS1 | 121.4656625704 | 31.1446273542 | 989 | 504990 | -90.44 | 14.52 | 66.30 | 0.07 | 2.29 | 1593 |
| 2024-09-20 22:21:37.544 | MS1 | 121.4656592692 | 31.1446338631 | 989 | 504990 | -92.53 | 7.29 | 70.59 | 0.18 | 2.64 | 1600 |
| 2024-09-20 22:21:38.614 | MS1 | 121.4656681443 | 31.1446231151 | 989 | 504990 | -89.43 | 7.78 | 85.02 | 0.10 | 2.94 | 1568 |
| 2024-09-20 22:21:39.133 | MS1 | 121.4656686876 | 31.1446299032 | 989 | 504990 | -90.20 | 10.75 | 64.56 | 0.00 | 2.43 | 1594 |
| 2024-09-20 22:21:40.210 | MS1 | 121.4656761368 | 31.1446255429 | 989 | 504990 | -93.76 | 10.92 | 524.69 | 0.12 | 2.77 | 1584 |
| 2024-09-20 22:21:41.524 | MS1 | 121.4656584919 | 31.1446279816 | 989 | 504990 | -89.66 | 8.30 | 530.45 | 0.09 | 2.75 | 1575 |
| 2024-09-20 22:21:42.679 | MS1 | 121.4656731586 | 31.1446340464 | 989 | 504990 | -91.19 | 7.03 | 525.08 | 0.07 | 2.74 | 1593 |

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
| 3225563 | 4 | 121.4734144661 | 31.1482301709 | 33 | 11 | 9 | 24.0 | TDD | 670 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3228100 | 3 | 121.4730384458 | 31.1501535713 | 220 | 0 | 8 | 17.6 | TDD | 989 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3260846 | 1 | 121.4730206201 | 31.1526042219 | 51 | 5 | 3 | 37.3 | TDD | 280 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3267177 | 2 | 121.4663770335 | 31.1534221950 | 66 | 6 | 11 | 29.1 | TDD | 169 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.524 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.549 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.689 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.689 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.369 | NREventA3 | measId:2;ServCellPCI:312;Se... |
| 2024-09-20 22:21:38.609 | NRHandoverAttempt | SourcePCI:312;SourceNR-ARFC... |
| 2024-09-20 22:21:38.655 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.669 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.796 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.796 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260846 | 1 | 8.4137 | 6.6055 | -114.2010 | 11.8667 | 122.7180 | 0.0177 | 0.0075 |
| 2024_09_20 22:00 | 3267177 | 2 | 6.3022 | 17.1906 | -114.7480 | 5.0667 | 190.3770 | 0.0068 | 0.0194 |
| 2024_09_20 22:00 | 3228100 | 3 | 92.4610 | 84.1084 | -114.3673 | 6.8292 | 138.9059 | 0.0054 | 0.0158 |
| 2024_09_20 22:00 | 3225563 | 4 | 17.0634 | 7.4131 | -116.2375 | 12.7524 | 125.4530 | 0.0001 | 0.0128 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416232_7F16C848 | 504990 | 989 | -89.0 | 504990 | 280 | -96.3 | 504990 | 670 | -99.5 | 504990 | 169 |
| MR_1774416232_022F706F | 504990 | 989 | -89.5 | 504990 | 280 | -97.0 | 504990 | 670 | -99.2 | 504990 | 169 |
| MR_1774416232_6C4258AD | 504990 | 989 | -87.2 | 504990 | 280 | -95.0 | 504990 | 670 | -99.3 | 504990 | 169 |
| MR_1774416232_C8A9ABBC | 504990 | 989 | -86.7 | 504990 | 280 | -96.2 | 504990 | 670 | -97.7 | 504990 | 169 |
| MR_1774416232_0D77CBED | 504990 | 989 | -87.6 | 504990 | 280 | -94.5 | 504990 | 670 | -99.3 | 504990 | 169 |
| MR_1774416232_21B0AE9E | 504990 | 989 | -89.7 | 504990 | 280 | -94.9 | 504990 | 670 | -99.9 | 504990 | 169 |
| MR_1774416232_2983CE62 | 504990 | 989 | -88.1 | 504990 | 280 | -94.3 | 504990 | 670 | -99.8 | 504990 | 169 |
| MR_1774416232_69C50A6C | 504990 | 989 | -89.5 | 504990 | 280 | -96.7 | 504990 | 670 | -98.2 | 504990 | 169 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 114: `46a37242-f8a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `46a37242-f8ab-4358-acbb-a89876906475` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[114] topology](images/train_0114.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3264035_2
- `C2`: Insufficient data; more data is needed for judgment. **← 정답**
- `C3`: Press down the tilt angle of 3264035_2 by 10 degrees
- `C4`: Increase transmission power for 3274881_3
- `C5`: Add neighbor relationship between 3238480_1 and 3274881_3
- `C6`: Adjust the azimuth of 3264035_2 by 50 degrees
- `C7`: Decrease A3 Offset threshold for 3264035_2
- `C8`: Increase A3 Offset threshold for 3264035_2
- `C9`: Check test server and transmission issues
- `C10`: Lift the tilt angle of 3264035_2 by 10 degrees
- `C11`: Press down the tilt angle  of 3274881_3 by 10 degrees
- `C12`: Decrease transmission power for 3274881_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264035_2
- `C14`: Adjust the azimuth of 3274881_3 by 50 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274881_3
- `C16`: Decrease A3 Offset threshold for 3274881_3
- `C17`: Decrease transmission power for 3264035_2
- `C18`: Increase A3 Offset threshold for 3274881_3
- `C19`: Add neighbor relationship between 3264035_2 and 3274881_3
- `C20`: Lift the tilt angle  of 3274881_3 by 10 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264035_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274881_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.265 | MS1 | 121.4656695608 | 31.1446378839 | 28 | 504990 | -87.18 | 16.77 | 392.55 | 0.19 | 2.97 | 1579 |
| 2024-09-20 22:21:32.664 | MS1 | 121.4656746657 | 31.1446371301 | 28 | 504990 | -85.52 | 15.61 | 317.81 | 0.16 | 2.48 | 1591 |
| 2024-09-20 22:21:33.467 | MS1 | 121.4656710051 | 31.1446183352 | 28 | 504990 | -89.66 | 15.02 | 432.40 | 0.18 | 2.79 | 1592 |
| 2024-09-20 22:21:34.546 | MS1 | 121.4656674073 | 31.1446228173 | 28 | 504990 | -90.02 | 14.22 | 55.76 | 0.17 | 2.22 | 1582 |
| 2024-09-20 22:21:35.805 | MS1 | 121.4656728075 | 31.1446272164 | 28 | 504990 | -85.36 | 14.20 | 107.58 | 0.10 | 2.62 | 1593 |
| 2024-09-20 22:21:36.625 | MS1 | 121.4656775623 | 31.1446378026 | 28 | 504990 | -91.33 | 12.45 | 42.85 | 0.12 | 2.82 | 1567 |
| 2024-09-20 22:21:37.910 | MS1 | 121.4656761069 | 31.1446248013 | 28 | 504990 | -92.81 | 10.26 | 67.04 | 0.16 | 2.51 | 1563 |
| 2024-09-20 22:21:38.271 | MS1 | 121.4656744330 | 31.1446330181 | 28 | 504990 | -93.59 | 11.29 | 62.84 | 0.14 | 2.69 | 1570 |
| 2024-09-20 22:21:39.157 | MS1 | 121.4656663451 | 31.1446301895 | 28 | 504990 | -93.37 | 9.03 | 91.01 | 0.08 | 2.57 | 1574 |
| 2024-09-20 22:21:40.822 | MS1 | 121.4656589242 | 31.1446312634 | 28 | 504990 | -89.94 | 11.15 | 431.85 | 0.16 | 2.93 | 1576 |
| 2024-09-20 22:21:41.311 | MS1 | 121.4656589907 | 31.1446270401 | 28 | 504990 | -90.47 | 12.11 | 496.42 | 0.05 | 2.06 | 1576 |
| 2024-09-20 22:21:42.141 | MS1 | 121.4656602300 | 31.1446357612 | 28 | 504990 | -91.23 | 8.52 | 453.24 | 0.16 | 2.56 | 1595 |

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
| 3216425 | 4 | 121.4719106405 | 31.1459954211 | 320 | 0 | 0 | 19.8 | TDD | 638 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3238480 | 1 | 121.4700882144 | 31.1482215952 | 17 | 10 | 3 | 32.0 | TDD | 760 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3264035 | 2 | 121.4667608414 | 31.1443186114 | 230 | 12 | 7 | 42.6 | TDD | 28 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3274881 | 3 | 121.4735946551 | 31.1503970621 | 331 | 9 | 12 | 45.8 | TDD | 365 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.833 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.858 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.958 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.958 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.706 | NREventA3 | measId:2;ServCellPCI:697;Se... |
| 2024-09-20 22:21:37.946 | NRHandoverAttempt | SourcePCI:697;SourceNR-ARFC... |
| 2024-09-20 22:21:37.995 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.010 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.119 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.119 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3238480 | 1 | 93.3875 | 94.5010 | -114.2713 | 13.9757 | 188.5989 | 0.0036 | 0.0015 |
| 2024_09_19 22:00 | 3264035 | 2 | 94.1751 | 77.3381 | -117.3849 | 18.6862 | 128.1768 | 0.0051 | 0.0120 |
| 2024_09_19 22:00 | 3274881 | 3 | 82.3726 | 75.2480 | -114.0572 | 13.5851 | 89.0711 | 0.0159 | 0.0107 |
| 2024_09_19 22:00 | 3216425 | 4 | 75.0488 | 93.3444 | -114.1180 | 8.9050 | 136.9159 | 0.0121 | 0.0044 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411995_A006F387 | 504990 | 28 | -89.7 | 504990 | 365 | -96.4 | 504990 | 760 | -104.7 | 504990 | 638 |
| MR_1774411995_205632AA | 504990 | 28 | -88.9 | 504990 | 365 | -94.9 | 504990 | 760 | -104.5 | 504990 | 638 |
| MR_1774411995_674DB4D6 | 504990 | 28 | -91.2 | 504990 | 365 | -93.5 | 504990 | 760 | -102.3 | 504990 | 638 |
| MR_1774411995_4BE288D7 | 504990 | 28 | -89.4 | 504990 | 365 | -96.5 | 504990 | 760 | -102.8 | 504990 | 638 |
| MR_1774411995_F36874AE | 504990 | 28 | -88.6 | 504990 | 365 | -96.1 | 504990 | 760 | -104.1 | 504990 | 638 |
| MR_1774411995_73F1CFA0 | 504990 | 28 | -88.1 | 504990 | 365 | -97.3 | 504990 | 760 | -101.5 | 504990 | 638 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 115: `77ffffa9-6f2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `77ffffa9-6f2d-4e94-849c-f5607f79210c` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[115] topology](images/train_0115.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259938_4
- `C2`: Add neighbor relationship between 3273589_3 and 3259938_4
- `C3`: Adjust the azimuth of 3259938_4 by 50 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259938_4
- `C5`: Adjust the azimuth of 3273589_3 by 50 degrees
- `C6`: Decrease A3 Offset threshold for 3273589_3
- `C7`: Press down the tilt angle of 3273589_3 by 7 degrees
- `C8`: Press down the tilt angle  of 3259938_4 by 10 degrees
- `C9`: Decrease transmission power for 3259938_4
- `C10`: Check test server and transmission issues **← 정답**
- `C11`: Increase transmission power for 3273589_3
- `C12`: Lift the tilt angle of 3273589_3 by 7 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Lift the tilt angle  of 3259938_4 by 10 degrees
- `C15`: Increase transmission power for 3259938_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273589_3
- `C17`: Increase A3 Offset threshold for 3259938_4
- `C18`: Increase A3 Offset threshold for 3273589_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273589_3
- `C20`: Decrease A3 Offset threshold for 3259938_4
- `C21`: Add neighbor relationship between 3217959_1 and 3259938_4
- `C22`: Decrease transmission power for 3273589_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.513 | MS1 | 121.4656683397 | 31.1446378396 | 765 | 504990 | -88.64 | 14.72 | 601.64 | 0.16 | 2.34 | 1600 |
| 2024-09-20 22:21:32.886 | MS1 | 121.4656664467 | 31.1446231826 | 765 | 504990 | -88.42 | 16.00 | 452.36 | 0.18 | 2.04 | 1572 |
| 2024-09-20 22:21:33.558 | MS1 | 121.4656714489 | 31.1446249226 | 765 | 504990 | -86.66 | 15.91 | 523.76 | 0.07 | 2.84 | 1580 |
| 2024-09-20 22:21:34.763 | MS1 | 121.4656622041 | 31.1446309401 | 765 | 504990 | -85.43 | 14.52 | 64.08 | 0.07 | 2.12 | 464 |
| 2024-09-20 22:21:35.138 | MS1 | 121.4656609674 | 31.1446193020 | 765 | 504990 | -86.94 | 17.39 | 99.00 | 0.11 | 2.76 | 444 |
| 2024-09-20 22:21:36.694 | MS1 | 121.4656638931 | 31.1446286682 | 765 | 504990 | -85.67 | 13.94 | 56.21 | 0.10 | 2.54 | 457 |
| 2024-09-20 22:21:37.332 | MS1 | 121.4656710966 | 31.1446335278 | 765 | 504990 | -89.34 | 10.89 | 78.71 | 0.03 | 2.07 | 472 |
| 2024-09-20 22:21:38.320 | MS1 | 121.4656759845 | 31.1446374759 | 765 | 504990 | -92.99 | 9.53 | 66.22 | 0.08 | 2.38 | 414 |
| 2024-09-20 22:21:39.984 | MS1 | 121.4656779014 | 31.1446182840 | 765 | 504990 | -93.37 | 9.55 | 84.38 | 0.08 | 2.39 | 467 |
| 2024-09-20 22:21:40.541 | MS1 | 121.4656648380 | 31.1446222998 | 765 | 504990 | -91.06 | 9.30 | 550.16 | 0.10 | 2.83 | 1595 |
| 2024-09-20 22:21:41.369 | MS1 | 121.4656603825 | 31.1446275197 | 765 | 504990 | -91.24 | 10.66 | 339.06 | 0.17 | 2.52 | 1565 |
| 2024-09-20 22:21:42.121 | MS1 | 121.4656759755 | 31.1446311564 | 765 | 504990 | -91.85 | 10.45 | 472.59 | 0.05 | 2.26 | 1571 |

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
| 3217959 | 1 | 121.4751983934 | 31.1502488466 | 5 | 6 | 5 | 45.3 | TDD | 768 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3223377 | 2 | 121.4654916748 | 31.1479933421 | 13 | 11 | 6 | 38.0 | TDD | 946 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3259938 | 4 | 121.4673838894 | 31.1445907113 | 92 | 9 | 6 | 44.6 | TDD | 262 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3273589 | 3 | 121.4733280185 | 31.1534193915 | 141 | 5 | 12 | 44.6 | TDD | 765 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.107 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.130 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.279 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.279 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.973 | NREventA3 | measId:2;ServCellPCI:205;Se... |
| 2024-09-20 22:21:38.213 | NRHandoverAttempt | SourcePCI:205;SourceNR-ARFC... |
| 2024-09-20 22:21:38.243 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.255 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.397 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.397 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217959 | 1 | 8.8004 | 15.0872 | -116.9342 | 19.4703 | 191.1502 | 0.0105 | 0.0190 |
| 2024_09_20 22:00 | 3223377 | 2 | 17.2991 | 6.1844 | -117.1642 | 14.5229 | 145.8035 | 0.0040 | 0.0182 |
| 2024_09_20 22:00 | 3273589 | 3 | 11.3588 | 18.8492 | -115.3063 | 19.1785 | 159.9557 | 0.0026 | 0.0149 |
| 2024_09_20 22:00 | 3259938 | 4 | 16.9558 | 12.1107 | -114.8518 | 7.6517 | 91.1166 | 0.0120 | 0.0046 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412061_4B924088 | 504990 | 765 | -84.2 | 504990 | 262 | -94.0 | 504990 | 768 | -94.2 | 504990 | 946 |
| MR_1774412061_3DA91C0F | 504990 | 765 | -86.0 | 504990 | 262 | -90.9 | 504990 | 768 | -93.2 | 504990 | 946 |
| MR_1774412061_3837B318 | 504990 | 765 | -84.8 | 504990 | 262 | -91.7 | 504990 | 768 | -95.6 | 504990 | 946 |
| MR_1774412061_9CAD4F11 | 504990 | 765 | -86.5 | 504990 | 262 | -92.2 | 504990 | 768 | -92.6 | 504990 | 946 |
| MR_1774412061_5BCBA184 | 504990 | 765 | -83.8 | 504990 | 262 | -94.0 | 504990 | 768 | -94.0 | 504990 | 946 |
| MR_1774412061_072C7E07 | 504990 | 765 | -86.0 | 504990 | 262 | -92.8 | 504990 | 768 | -92.6 | 504990 | 946 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 116: `f9cd0ca5-0f8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f9cd0ca5-0f8c-4db6-bf58-1e9cec5f4e9e` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266154_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[116] topology](images/train_0116.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3236746_6 by 1 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase transmission power for 3236746_6
- `C4`: Lift the tilt angle  of 3236746_6 by 2 degrees
- `C5`: Increase transmission power for 3266154_2
- `C6`: Adjust the azimuth of 3266154_2 by 2 degrees
- `C7`: Check test server and transmission issues
- `C8`: Add neighbor relationship between 3268338_12 and 3236746_6
- `C9`: Press down the tilt angle of 3266154_2 by 1 degrees
- `C10`: Press down the tilt angle  of 3236746_6 by 2 degrees
- `C11`: Decrease A3 Offset threshold for 3266154_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236746_6
- `C13`: Increase A3 Offset threshold for 3236746_6
- `C14`: Decrease A3 Offset threshold for 3236746_6
- `C15`: Decrease transmission power for 3236746_6
- `C16`: Lift the tilt angle of 3266154_2 by 1 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266154_2
- `C18`: Decrease transmission power for 3266154_2
- `C19`: Add neighbor relationship between 3266154_2 and 3236746_6
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266154_2 **← 정답**
- `C21`: Increase A3 Offset threshold for 3266154_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236746_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.812 | MS1 | 121.4656616783 | 31.1446289223 | 866 | 504990 | -95.86 | 11.52 | 541.90 | 0.00 | 2.30 | 1560 |
| 2024-09-20 22:21:32.789 | MS1 | 121.4656682347 | 31.1446319706 | 281 | 504990 | -94.03 | 12.69 | 589.78 | 0.18 | 2.49 | 1589 |
| 2024-09-20 22:21:33.375 | MS1 | 121.4656594952 | 31.1446214048 | 934 | 504990 | -95.98 | 13.71 | 579.18 | 0.06 | 2.53 | 1581 |
| 2024-09-20 22:21:34.475 | MS1 | 121.4656644633 | 31.1446288393 | 90 | 152650 | -92.62 | 2.90 | 52.87 | 0.17 | 1.87 | 934 |
| 2024-09-20 22:21:35.242 | MS1 | 121.4656761245 | 31.1446319481 | 755 | 152650 | -94.54 | 2.86 | 100.57 | 0.12 | 1.52 | 974 |
| 2024-09-20 22:21:36.823 | MS1 | 121.4656600031 | 31.1446352026 | 445 | 152650 | -89.15 | 6.21 | 98.35 | 0.19 | 1.89 | 932 |
| 2024-09-20 22:21:37.346 | MS1 | 121.4656705362 | 31.1446234590 | 255 | 152650 | -91.09 | 7.23 | 72.92 | 0.01 | 1.83 | 902 |
| 2024-09-20 22:21:38.266 | MS1 | 121.4656765792 | 31.1446199569 | 90 | 152650 | -88.72 | 6.24 | 62.29 | 0.07 | 1.65 | 987 |
| 2024-09-20 22:21:39.706 | MS1 | 121.4656641411 | 31.1446327807 | 755 | 152650 | -88.36 | 5.90 | 79.28 | 0.16 | 1.52 | 954 |
| 2024-09-20 22:21:40.908 | MS1 | 121.4656746761 | 31.1446318362 | 445 | 152650 | -88.46 | 2.91 | 54.10 | 0.12 | 2.97 | 1578 |
| 2024-09-20 22:21:41.838 | MS1 | 121.4656753799 | 31.1446307438 | 255 | 152650 | -87.30 | 7.48 | 84.87 | 0.04 | 2.57 | 1560 |
| 2024-09-20 22:21:42.961 | MS1 | 121.4656670672 | 31.1446185888 | 90 | 152650 | -87.10 | 4.12 | 53.94 | 0.07 | 2.06 | 1589 |

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
| 3210822 | 3 | 121.4733159753 | 31.1506535727 | 5 | 9 | 9 | 29.8 | TDD | 934 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3214689 | 7 | 121.4754645090 | 31.1444210627 | 63 | 9 | 7 | 11.7 | FDD | 197 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3226624 | 5 | 121.4727906391 | 31.1440608188 | 191 | 9 | 2 | 13.6 | TDD | 281 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3226884 | 10 | 121.4754896441 | 31.1555547293 | 116 | 7 | 6 | 28.0 | FDD | 696 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3236746 | 6 | 121.4660847970 | 31.1555039316 | 181 | 2 | 2 | 6.5 | TDD | 187 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3238960 | 1 | 121.4666158990 | 31.1474268188 | 60 | 13 | 6 | 4.0 | TDD | 929 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3241057 | 9 | 121.4678234620 | 31.1546346715 | 68 | 10 | 1 | 10.4 | FDD | 755 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3241612 | 8 | 121.4690195219 | 31.1452633407 | 35 | 5 | 2 | 9.6 | FDD | 553 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3264405 | 13 | 121.4650922040 | 31.1440342034 | 3 | 10 | 3 | 26.5 | FDD | 255 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3266154 | 2 | 121.4710100216 | 31.1517431326 | 211 | 0 | 8 | 19.5 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3268338 | 12 | 121.4704153352 | 31.1550527350 | 283 | 5 | 7 | 13.5 | FDD | 445 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3269285 | 4 | 121.4738710355 | 31.1495963915 | 304 | 10 | 6 | 1.7 | TDD | 52 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3275910 | 11 | 121.4715559910 | 31.1535975516 | 57 | 3 | 11 | 21.4 | FDD | 90 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |

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
| 2024-09-20 22:21:31.342 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.469 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.469 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.176 | NREventA2 | measId:1;ServCellPCI:806;Se... |
| 2024-09-20 22:21:35.324 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.530 | NREventA5 | measId:3;ServCellPCI:806;Se... |
| 2024-09-20 22:21:35.585 | NRHandoverAttempt | SourcePCI:806;SourceNR-ARFC... |
| 2024-09-20 22:21:35.619 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.631 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.755 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.755 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238960 | 1 | 11.8769 | 11.8420 | -115.2759 | 5.9193 | 184.6137 | 0.0032 | 0.0144 |
| 2024_09_20 22:00 | 3266154 | 2 | 11.6734 | 7.6503 | -116.2710 | 15.9077 | 123.4532 | 0.0046 | 0.0002 |
| 2024_09_20 22:00 | 3210822 | 3 | 8.8614 | 10.4692 | -115.8871 | 5.6003 | 176.8758 | 0.0017 | 0.0171 |
| 2024_09_20 22:00 | 3269285 | 4 | 18.6237 | 18.8055 | -115.6200 | 15.7698 | 139.5143 | 0.0013 | 0.0153 |
| 2024_09_20 22:00 | 3226624 | 5 | 9.6357 | 9.4122 | -117.2376 | 12.9006 | 175.6523 | 0.0080 | 0.0049 |
| 2024_09_20 22:00 | 3236746 | 6 | 17.5434 | 12.0349 | -115.5951 | 7.7562 | 183.6179 | 0.0009 | 0.0136 |
| 2024_09_20 22:00 | 3214689 | 7 | 15.2538 | 15.4527 | -116.3491 | 3.4865 | 45.0159 | 0.0102 | 0.0075 |
| 2024_09_20 22:00 | 3241612 | 8 | 10.5152 | 17.3019 | -117.7280 | 3.7153 | 25.2860 | 0.0077 | 0.0169 |
| 2024_09_20 22:00 | 3241057 | 9 | 10.8236 | 13.0028 | -114.6441 | 4.5067 | 29.3678 | 0.0166 | 0.0137 |
| 2024_09_20 22:00 | 3226884 | 10 | 5.1293 | 7.7831 | -117.1798 | 4.4820 | 51.5521 | 0.0164 | 0.0136 |
| 2024_09_20 22:00 | 3275910 | 11 | 11.6580 | 10.9046 | -116.2047 | 3.2707 | 22.7546 | 0.0091 | 0.0107 |
| 2024_09_20 22:00 | 3268338 | 12 | 8.0011 | 6.7463 | -117.1052 | 3.0233 | 45.2857 | 0.0127 | 0.0035 |
| 2024_09_20 22:00 | 3264405 | 13 | 19.7720 | 13.4642 | -115.0791 | 4.2470 | 36.8596 | 0.0015 | 0.0199 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412954_6744370F | 504990 | 934 | -97.3 | 504990 | 187 | -97.1 | 504990 | 929 | -96.1 | 504990 | 52 |
| MR_1774412954_D051E6F5 | 152650 | 90 | -90.9 | 152650 | 197 | -100.3 | 152650 | 696 | -100.2 | 152650 | 553 |
| MR_1774412954_7D6EF196 | 152650 | 90 | -91.2 | 152650 | 197 | -98.5 | 152650 | 696 | -102.7 | 152650 | 553 |
| MR_1774412954_80491149 | 504990 | 934 | -97.2 | 504990 | 187 | -97.2 | 504990 | 929 | -99.4 | 504990 | 52 |
| MR_1774412954_15732A2A | 504990 | 934 | -96.2 | 504990 | 187 | -97.2 | 504990 | 929 | -98.6 | 504990 | 52 |
| MR_1774412954_4BFB0DF6 | 504990 | 934 | -96.7 | 504990 | 187 | -98.1 | 504990 | 929 | -96.7 | 504990 | 52 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 117: `bea2aee2-10e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bea2aee2-10e0-4ac4-9b78-e710c2bb221b` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Lift the tilt angle  of 3246842_2 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[117] topology](images/train_0117.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3253564_3
- `C2`: Press down the tilt angle of 3222478_1 by 6 degrees
- `C3`: Press down the tilt angle  of 3246842_2 by 7 degrees
- `C4`: Increase A3 Offset threshold for 3222478_1
- `C5`: Decrease transmission power for 3222478_1
- `C6`: Decrease A3 Offset threshold for 3222478_1
- `C7`: Check test server and transmission issues
- `C8`: Decrease A3 Offset threshold for 3253564_3
- `C9`: Decrease transmission power for 3253564_3
- `C10`: Increase transmission power for 3222478_1
- `C11`: Adjust the azimuth of 3222478_1 by 32 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222478_1
- `C13`: Lift the tilt angle  of 3246842_2 by 7 degrees **← 정답**
- `C14`: Increase transmission power for 3253564_3
- `C15`: Add neighbor relationship between 3222478_1 and 3253564_3
- `C16`: Lift the tilt angle of 3222478_1 by 6 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222478_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253564_3
- `C19`: Add neighbor relationship between 3246842_2 and 3253564_3
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Adjust the azimuth of 3246842_2 by 11 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253564_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.103 | MS1 | 121.4656702825 | 31.1446226701 | 248 | 504990 | -90.45 | 12.08 | 332.96 | 0.16 | 2.57 | 1596 |
| 2024-09-20 22:21:32.356 | MS1 | 121.4656654847 | 31.1446305085 | 248 | 504990 | -87.96 | 12.24 | 473.08 | 0.03 | 2.86 | 1573 |
| 2024-09-20 22:21:33.533 | MS1 | 121.4656671193 | 31.1446325403 | 248 | 504990 | -89.77 | 15.42 | 413.49 | 0.08 | 2.86 | 1577 |
| 2024-09-20 22:21:34.368 | MS1 | 121.4656724185 | 31.1446346098 | 248 | 504990 | -88.30 | 16.99 | 53.73 | 0.18 | 2.45 | 1560 |
| 2024-09-20 22:21:35.407 | MS1 | 121.4656716407 | 31.1446276166 | 248 | 504990 | -86.89 | 13.71 | 100.34 | 0.06 | 2.63 | 1593 |
| 2024-09-20 22:21:36.818 | MS1 | 121.4656690720 | 31.1446181259 | 248 | 504990 | -85.49 | 13.02 | 65.32 | 0.12 | 2.04 | 1571 |
| 2024-09-20 22:21:37.262 | MS1 | 121.4656647894 | 31.1446366663 | 248 | 504990 | -90.63 | 9.81 | 66.97 | 0.09 | 2.67 | 1564 |
| 2024-09-20 22:21:38.777 | MS1 | 121.4656660951 | 31.1446361640 | 248 | 504990 | -89.25 | 12.54 | 61.91 | 0.07 | 2.54 | 1580 |
| 2024-09-20 22:21:39.485 | MS1 | 121.4656619226 | 31.1446259221 | 248 | 504990 | -92.76 | 7.70 | 71.51 | 0.14 | 2.12 | 1563 |
| 2024-09-20 22:21:40.300 | MS1 | 121.4656668570 | 31.1446192554 | 248 | 504990 | -93.74 | 8.05 | 540.29 | 0.03 | 2.85 | 1588 |
| 2024-09-20 22:21:41.200 | MS1 | 121.4656687457 | 31.1446355581 | 248 | 504990 | -92.19 | 7.61 | 601.66 | 0.19 | 2.07 | 1587 |
| 2024-09-20 22:21:42.722 | MS1 | 121.4656722968 | 31.1446356707 | 248 | 504990 | -91.55 | 9.37 | 491.22 | 0.12 | 2.45 | 1575 |

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
| 3222478 | 1 | 121.4694423805 | 31.1487548878 | 250 | 2 | 8 | 36.2 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3225260 | 4 | 121.4756587477 | 31.1467764946 | 103 | 0 | 0 | 19.4 | TDD | 208 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3246842 | 2 | 121.4652472717 | 31.1550984390 | 79 | 9 | 12 | 43.7 | TDD | 288 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3253564 | 3 | 121.4650454948 | 31.1479465285 | 160 | 0 | 3 | 46.3 | TDD | 719 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.247 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.262 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.371 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.371 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.135 | NREventA3 | measId:2;ServCellPCI:753;Se... |
| 2024-09-20 22:21:38.375 | NRHandoverAttempt | SourcePCI:753;SourceNR-ARFC... |
| 2024-09-20 22:21:38.413 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.427 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.536 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.536 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222478 | 1 | 84.6704 | 91.2653 | -117.9506 | 5.4126 | 156.4766 | 0.0028 | 0.0152 |
| 2024_09_20 22:00 | 3246842 | 2 | 9.2099 | 19.3488 | -114.0060 | 17.8414 | 140.5652 | 0.0021 | 0.0116 |
| 2024_09_20 22:00 | 3253564 | 3 | 15.9564 | 11.3360 | -115.0142 | 13.2274 | 98.4532 | 0.0065 | 0.0079 |
| 2024_09_20 22:00 | 3225260 | 4 | 16.3529 | 18.4903 | -114.9105 | 7.8647 | 190.0731 | 0.0099 | 0.0193 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417062_2F5699EF | 504990 | 248 | -88.0 | 504990 | 719 | -91.9 | 504990 | 288 | -98.8 | 504990 | 208 |
| MR_1774417062_DD785616 | 504990 | 248 | -88.2 | 504990 | 719 | -90.9 | 504990 | 288 | -100.9 | 504990 | 208 |
| MR_1774417062_488676E2 | 504990 | 248 | -90.2 | 504990 | 719 | -89.9 | 504990 | 288 | -98.3 | 504990 | 208 |
| MR_1774417062_81DE44E0 | 504990 | 248 | -89.6 | 504990 | 719 | -91.2 | 504990 | 288 | -98.0 | 504990 | 208 |
| MR_1774417062_258D0819 | 504990 | 248 | -87.1 | 504990 | 719 | -90.7 | 504990 | 288 | -100.6 | 504990 | 208 |
| MR_1774417062_24632562 | 504990 | 248 | -88.0 | 504990 | 719 | -90.0 | 504990 | 288 | -101.4 | 504990 | 208 |
| MR_1774417062_F1AF2081 | 504990 | 248 | -89.1 | 504990 | 719 | -90.5 | 504990 | 288 | -98.8 | 504990 | 208 |
| MR_1774417062_E5613DAA | 504990 | 248 | -86.7 | 504990 | 719 | -90.4 | 504990 | 288 | -100.4 | 504990 | 208 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 118: `0938209f-a67...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0938209f-a67c-4d4a-a6ff-39dc416ff112` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[118] topology](images/train_0118.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265963_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265963_2
- `C3`: Check test server and transmission issues
- `C4`: Decrease transmission power for 3217915_1
- `C5`: Decrease transmission power for 3265963_2
- `C6`: Increase transmission power for 3217915_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217915_1
- `C8`: Lift the tilt angle of 3265963_2 by 10 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217915_1
- `C10`: Lift the tilt angle  of 3217915_1 by 10 degrees
- `C11`: Decrease A3 Offset threshold for 3217915_1
- `C12`: Increase transmission power for 3265963_2
- `C13`: Press down the tilt angle of 3265963_2 by 10 degrees
- `C14`: Increase A3 Offset threshold for 3217915_1
- `C15`: Decrease A3 Offset threshold for 3265963_2
- `C16`: Adjust the azimuth of 3265963_2 by 50 degrees
- `C17`: Adjust the azimuth of 3217915_1 by 15 degrees
- `C18`: Increase A3 Offset threshold for 3265963_2
- `C19`: Press down the tilt angle  of 3217915_1 by 10 degrees
- `C20`: Add neighbor relationship between 3227794_4 and 3217915_1
- `C21`: Add neighbor relationship between 3265963_2 and 3217915_1
- `C22`: Insufficient data; more data is needed for judgment. **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.215 | MS1 | 121.4656719031 | 31.1446278578 | 83 | 504990 | -86.87 | 13.59 | 493.25 | 0.09 | 2.58 | 1579 |
| 2024-09-20 22:21:32.308 | MS1 | 121.4656738931 | 31.1446316651 | 83 | 504990 | -85.97 | 12.62 | 354.72 | 0.04 | 2.77 | 1577 |
| 2024-09-20 22:21:33.616 | MS1 | 121.4656633276 | 31.1446344525 | 83 | 504990 | -89.79 | 14.45 | 582.26 | 0.02 | 2.09 | 1588 |
| 2024-09-20 22:21:34.544 | MS1 | 121.4656668382 | 31.1446365563 | 83 | 504990 | -88.00 | 15.52 | 91.45 | 0.19 | 2.72 | 1579 |
| 2024-09-20 22:21:35.321 | MS1 | 121.4656631651 | 31.1446227686 | 83 | 504990 | -85.76 | 17.54 | 76.08 | 0.17 | 2.85 | 1577 |
| 2024-09-20 22:21:36.435 | MS1 | 121.4656701251 | 31.1446314719 | 83 | 504990 | -89.02 | 16.08 | 76.96 | 0.03 | 2.98 | 1584 |
| 2024-09-20 22:21:37.604 | MS1 | 121.4656591476 | 31.1446241430 | 83 | 504990 | -90.66 | 9.40 | 63.08 | 0.03 | 2.50 | 1566 |
| 2024-09-20 22:21:38.657 | MS1 | 121.4656660307 | 31.1446237638 | 83 | 504990 | -89.13 | 11.61 | 67.00 | 0.17 | 2.56 | 1580 |
| 2024-09-20 22:21:39.579 | MS1 | 121.4656752276 | 31.1446297247 | 83 | 504990 | -93.89 | 10.95 | 62.04 | 0.17 | 2.83 | 1591 |
| 2024-09-20 22:21:40.741 | MS1 | 121.4656599538 | 31.1446200762 | 83 | 504990 | -92.02 | 7.00 | 468.07 | 0.11 | 2.12 | 1600 |
| 2024-09-20 22:21:41.284 | MS1 | 121.4656678975 | 31.1446298634 | 83 | 504990 | -93.28 | 7.89 | 520.45 | 0.02 | 2.77 | 1597 |
| 2024-09-20 22:21:42.419 | MS1 | 121.4656711697 | 31.1446326244 | 83 | 504990 | -92.84 | 8.94 | 321.74 | 0.00 | 2.36 | 1599 |

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
| 3217915 | 1 | 121.4758500565 | 31.1499653255 | 224 | 11 | 3 | 46.8 | TDD | 472 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3227794 | 4 | 121.4713620532 | 31.1503740783 | 50 | 1 | 6 | 46.0 | TDD | 749 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3265963 | 2 | 121.4711958023 | 31.1498451657 | 149 | 6 | 6 | 49.5 | TDD | 83 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3276455 | 3 | 121.4677417364 | 31.1458057735 | 243 | 13 | 5 | 33.1 | TDD | 876 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.541 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.566 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.703 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.703 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.361 | NREventA3 | measId:2;ServCellPCI:682;Se... |
| 2024-09-20 22:21:38.601 | NRHandoverAttempt | SourcePCI:682;SourceNR-ARFC... |
| 2024-09-20 22:21:38.640 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.655 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.778 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.778 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3217915 | 1 | 88.5082 | 81.6071 | -116.4542 | 7.9997 | 104.6563 | 0.0019 | 0.0049 |
| 2024_09_19 22:00 | 3265963 | 2 | 77.4168 | 80.5892 | -115.1044 | 16.1333 | 142.4988 | 0.0017 | 0.0145 |
| 2024_09_19 22:00 | 3276455 | 3 | 87.4866 | 81.4732 | -115.3432 | 6.0269 | 101.9946 | 0.0147 | 0.0165 |
| 2024_09_19 22:00 | 3227794 | 4 | 82.0249 | 84.1869 | -115.8178 | 13.2854 | 188.2885 | 0.0023 | 0.0162 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412659_4009E548 | 504990 | 83 | -87.7 | 504990 | 472 | -89.6 | 504990 | 749 | -101.5 | 504990 | 876 |
| MR_1774412659_3CD31B62 | 504990 | 83 | -88.8 | 504990 | 472 | -90.2 | 504990 | 749 | -102.7 | 504990 | 876 |
| MR_1774412659_5917D6C7 | 504990 | 83 | -89.3 | 504990 | 472 | -90.0 | 504990 | 749 | -104.9 | 504990 | 876 |
| MR_1774412659_5A3C378F | 504990 | 83 | -86.4 | 504990 | 472 | -90.3 | 504990 | 749 | -101.5 | 504990 | 876 |
| MR_1774412659_B39F0973 | 504990 | 83 | -88.1 | 504990 | 472 | -90.0 | 504990 | 749 | -102.3 | 504990 | 876 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 119: `43e8ab0c-50a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `43e8ab0c-50ac-477b-9098-8ba1cbd0f0f0` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270844_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[119] topology](images/train_0119.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Increase transmission power for 3270844_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214354_2
- `C4`: Increase A3 Offset threshold for 3214354_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214354_2
- `C6`: Add neighbor relationship between 3263308_11 and 3214354_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Increase transmission power for 3214354_2
- `C9`: Decrease transmission power for 3270844_1
- `C10`: Lift the tilt angle of 3270844_1 by 5 degrees
- `C11`: Press down the tilt angle of 3270844_1 by 5 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270844_1
- `C13`: Adjust the azimuth of 3214354_2 by 31 degrees
- `C14`: Adjust the azimuth of 3270844_1 by 0 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270844_1 **← 정답**
- `C16`: Decrease A3 Offset threshold for 3270844_1
- `C17`: Decrease transmission power for 3214354_2
- `C18`: Add neighbor relationship between 3270844_1 and 3214354_2
- `C19`: Increase A3 Offset threshold for 3270844_1
- `C20`: Decrease A3 Offset threshold for 3214354_2
- `C21`: Press down the tilt angle  of 3214354_2 by 4 degrees
- `C22`: Lift the tilt angle  of 3214354_2 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.544 | MS1 | 121.4656765186 | 31.1446187800 | 805 | 504990 | -93.28 | 12.79 | 413.91 | 0.01 | 2.30 | 1586 |
| 2024-09-20 22:21:32.868 | MS1 | 121.4656772105 | 31.1446294258 | 119 | 504990 | -94.88 | 13.73 | 350.16 | 0.20 | 2.20 | 1564 |
| 2024-09-20 22:21:33.889 | MS1 | 121.4656706185 | 31.1446259917 | 149 | 504990 | -93.49 | 13.58 | 535.60 | 0.07 | 2.66 | 1584 |
| 2024-09-20 22:21:34.567 | MS1 | 121.4656683835 | 31.1446317923 | 257 | 152650 | -91.88 | 6.06 | 64.78 | 0.07 | 1.90 | 997 |
| 2024-09-20 22:21:35.268 | MS1 | 121.4656674189 | 31.1446258415 | 571 | 152650 | -89.39 | 7.82 | 43.96 | 0.19 | 1.99 | 994 |
| 2024-09-20 22:21:36.508 | MS1 | 121.4656629710 | 31.1446242906 | 87 | 152650 | -96.28 | 2.27 | 72.52 | 0.07 | 1.65 | 936 |
| 2024-09-20 22:21:37.183 | MS1 | 121.4656641444 | 31.1446355669 | 175 | 152650 | -88.05 | 4.58 | 56.58 | 0.16 | 1.61 | 915 |
| 2024-09-20 22:21:38.946 | MS1 | 121.4656710147 | 31.1446206448 | 257 | 152650 | -96.41 | 2.31 | 42.67 | 0.14 | 1.61 | 931 |
| 2024-09-20 22:21:39.613 | MS1 | 121.4656670963 | 31.1446307499 | 571 | 152650 | -87.18 | 5.83 | 88.70 | 0.12 | 1.88 | 938 |
| 2024-09-20 22:21:40.309 | MS1 | 121.4656730864 | 31.1446278355 | 87 | 152650 | -96.98 | 2.62 | 73.08 | 0.01 | 2.41 | 1578 |
| 2024-09-20 22:21:41.800 | MS1 | 121.4656729594 | 31.1446325033 | 175 | 152650 | -93.92 | 7.14 | 46.95 | 0.14 | 2.35 | 1590 |
| 2024-09-20 22:21:42.807 | MS1 | 121.4656719940 | 31.1446304221 | 257 | 152650 | -88.57 | 2.37 | 79.97 | 0.08 | 2.31 | 1592 |

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
| 3214090 | 3 | 121.4732086209 | 31.1497843545 | 184 | 6 | 3 | 24.7 | TDD | 693 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3214354 | 2 | 121.4674227997 | 31.1481822465 | 172 | 2 | 0 | 14.4 | TDD | 273 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3223425 | 6 | 121.4654594736 | 31.1527264213 | 156 | 15 | 11 | 10.9 | TDD | 185 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3232474 | 7 | 121.4681243995 | 31.1528502963 | 340 | 12 | 2 | 6.7 | FDD | 257 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3236837 | 10 | 121.4734706681 | 31.1525140740 | 130 | 15 | 12 | 16.5 | FDD | 753 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3246122 | 13 | 121.4710599242 | 31.1522144913 | 242 | 10 | 2 | 17.7 | FDD | 571 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3247810 | 8 | 121.4670383439 | 31.1467937388 | 38 | 2 | 7 | 0.8 | FDD | 846 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3253418 | 9 | 121.4741858560 | 31.1461833461 | 185 | 15 | 3 | 0.8 | FDD | 175 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3255266 | 4 | 121.4719196207 | 31.1449922471 | 194 | 8 | 0 | 16.0 | TDD | 149 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3258091 | 12 | 121.4653442349 | 31.1509519534 | 320 | 8 | 11 | 23.3 | FDD | 697 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3263308 | 11 | 121.4670535345 | 31.1532851036 | 194 | 0 | 11 | 5.8 | FDD | 87 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3270844 | 1 | 121.4729668326 | 31.1559714093 | 209 | 5 | 8 | 11.0 | TDD | 805 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3279139 | 5 | 121.4754805854 | 31.1527869761 | 195 | 14 | 4 | 12.5 | TDD | 119 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.604 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.620 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.724 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.724 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.482 | NREventA2 | measId:1;ServCellPCI:249;Se... |
| 2024-09-20 22:21:35.619 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.872 | NREventA5 | measId:3;ServCellPCI:249;Se... |
| 2024-09-20 22:21:35.911 | NRHandoverAttempt | SourcePCI:249;SourceNR-ARFC... |
| 2024-09-20 22:21:35.939 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.952 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.091 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.091 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270844 | 1 | 14.2309 | 12.1441 | -116.6033 | 11.0896 | 167.7509 | 0.0187 | 0.0049 |
| 2024_09_20 22:00 | 3214354 | 2 | 19.8266 | 7.7993 | -116.9843 | 13.0472 | 167.8573 | 0.0022 | 0.0089 |
| 2024_09_20 22:00 | 3214090 | 3 | 14.7033 | 16.8597 | -114.0494 | 12.1787 | 133.5245 | 0.0099 | 0.0190 |
| 2024_09_20 22:00 | 3255266 | 4 | 12.4636 | 9.0594 | -116.1242 | 5.1007 | 94.0285 | 0.0116 | 0.0072 |
| 2024_09_20 22:00 | 3279139 | 5 | 12.1193 | 5.3877 | -117.3658 | 7.1678 | 94.7415 | 0.0106 | 0.0179 |
| 2024_09_20 22:00 | 3223425 | 6 | 9.6972 | 9.5628 | -117.1004 | 5.2143 | 84.4864 | 0.0094 | 0.0020 |
| 2024_09_20 22:00 | 3232474 | 7 | 18.4039 | 6.2893 | -114.5528 | 4.0578 | 35.3048 | 0.0024 | 0.0084 |
| 2024_09_20 22:00 | 3247810 | 8 | 17.4722 | 8.7921 | -117.8973 | 3.4049 | 57.3546 | 0.0078 | 0.0028 |
| 2024_09_20 22:00 | 3253418 | 9 | 8.9816 | 7.6299 | -115.6739 | 3.0090 | 56.9490 | 0.0167 | 0.0101 |
| 2024_09_20 22:00 | 3236837 | 10 | 7.8747 | 6.6340 | -117.9804 | 4.6321 | 29.1841 | 0.0052 | 0.0034 |
| 2024_09_20 22:00 | 3263308 | 11 | 8.3233 | 12.3098 | -116.7406 | 4.6710 | 44.6965 | 0.0030 | 0.0182 |
| 2024_09_20 22:00 | 3258091 | 12 | 12.8734 | 13.7476 | -117.6865 | 3.2554 | 37.8385 | 0.0145 | 0.0054 |
| 2024_09_20 22:00 | 3246122 | 13 | 12.1255 | 12.6853 | -114.6803 | 3.7411 | 55.1677 | 0.0056 | 0.0164 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413796_91858130 | 504990 | 149 | -94.9 | 504990 | 273 | -92.6 | 504990 | 693 | -96.4 | 504990 | 185 |
| MR_1774413796_94D6BA4E | 152650 | 257 | -91.0 | 152650 | 753 | -97.3 | 152650 | 846 | -103.4 | 152650 | 697 |
| MR_1774413796_090FDA76 | 152650 | 257 | -90.7 | 152650 | 753 | -97.7 | 152650 | 846 | -104.2 | 152650 | 697 |
| MR_1774413796_1D1A9815 | 152650 | 257 | -91.7 | 152650 | 753 | -97.2 | 152650 | 846 | -102.2 | 152650 | 697 |
| MR_1774413796_7DFC8683 | 504990 | 149 | -94.4 | 504990 | 273 | -93.1 | 504990 | 693 | -95.6 | 504990 | 185 |
| MR_1774413796_94BE35E4 | 504990 | 149 | -93.5 | 504990 | 273 | -92.8 | 504990 | 693 | -94.4 | 504990 | 185 |
| MR_1774413796_B2278FC1 | 152650 | 257 | -91.1 | 152650 | 753 | -97.9 | 152650 | 846 | -102.7 | 152650 | 697 |
| MR_1774413796_52E7613A | 504990 | 149 | -95.4 | 504990 | 273 | -89.7 | 504990 | 693 | -93.2 | 504990 | 185 |

> *... 2개 열 생략 (전체 14열)*

---
