# Track A 문제 분석 — test[240]~test[249]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[240] ~ test[249] (10개)

## 목차

1. [문제 240: `f61eea97-9c4...`](#240) — single-answer
2. [문제 241: `1d6d05bc-dfd...`](#241) — single-answer
3. [문제 242: `5164011d-5df...`](#242) — single-answer
4. [문제 243: `53b0e0b6-b3b...`](#243) — multiple-answer
5. [문제 244: `ab98861f-fa2...`](#244) — single-answer
6. [문제 245: `08982883-e4e...`](#245) — single-answer
7. [문제 246: `0d99d2b4-834...`](#246) — single-answer
8. [문제 247: `46a737d2-c00...`](#247) — single-answer
9. [문제 248: `71375ac3-717...`](#248) — single-answer
10. [문제 249: `e0d6eae2-499...`](#249) — multiple-answer

---

### 문제 240: `f61eea97-9c4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f61eea97-9c40-418d-8556-673cd9e59d2c` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[240] topology](images/test_0240.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3236322_1
- `C2`: Add neighbor relationship between 3236322_1 and 3265604_3
- `C3`: Increase A3 Offset threshold for 3265604_3
- `C4`: Press down the tilt angle  of 3265604_3 by 7 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265604_3
- `C6`: Increase transmission power for 3265604_3
- `C7`: Lift the tilt angle  of 3265604_3 by 7 degrees
- `C8`: Increase A3 Offset threshold for 3236322_1
- `C9`: Adjust the azimuth of 3265604_3 by 50 degrees
- `C10`: Decrease A3 Offset threshold for 3236322_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236322_1
- `C12`: Decrease transmission power for 3236322_1
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Lift the tilt angle of 3236322_1 by 5 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265604_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236322_1
- `C17`: Adjust the azimuth of 3236322_1 by 32 degrees
- `C18`: Press down the tilt angle of 3236322_1 by 5 degrees
- `C19`: Decrease transmission power for 3265604_3
- `C20`: Check test server and transmission issues
- `C21`: Decrease A3 Offset threshold for 3265604_3
- `C22`: Add neighbor relationship between 3247474_4 and 3265604_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.858 | MS1 | 121.4656668960 | 31.1446253535 | 704 | 504990 | -87.98 | 13.57 | 477.81 | 0.11 | 2.25 | 1573 |
| 2024-09-20 22:21:32.449 | MS1 | 121.4656749531 | 31.1446206591 | 704 | 504990 | -89.31 | 12.11 | 553.05 | 0.17 | 2.40 | 1582 |
| 2024-09-20 22:21:33.590 | MS1 | 121.4656747573 | 31.1446224069 | 704 | 504990 | -88.23 | 15.89 | 556.36 | 0.02 | 2.32 | 1564 |
| 2024-09-20 22:21:34.748 | MS1 | 121.4656658843 | 31.1446358399 | 704 | 504990 | -85.37 | 13.75 | 91.29 | 0.50 | 2.28 | 664 |
| 2024-09-20 22:21:35.681 | MS1 | 121.4656658509 | 31.1446272385 | 704 | 504990 | -91.91 | 12.66 | 77.93 | 0.67 | 2.13 | 646 |
| 2024-09-20 22:21:36.830 | MS1 | 121.4656626840 | 31.1446233165 | 704 | 504990 | -91.00 | 16.63 | 79.00 | 0.51 | 2.25 | 604 |
| 2024-09-20 22:21:37.874 | MS1 | 121.4656703892 | 31.1446195305 | 704 | 504990 | -92.08 | 10.12 | 87.80 | 0.60 | 2.93 | 572 |
| 2024-09-20 22:21:38.253 | MS1 | 121.4656603754 | 31.1446350199 | 704 | 504990 | -91.44 | 11.37 | 62.07 | 0.68 | 2.26 | 658 |
| 2024-09-20 22:21:39.608 | MS1 | 121.4656607728 | 31.1446202232 | 704 | 504990 | -90.75 | 11.29 | 88.90 | 0.67 | 2.61 | 547 |
| 2024-09-20 22:21:40.920 | MS1 | 121.4656702156 | 31.1446318393 | 704 | 504990 | -92.31 | 9.28 | 505.02 | 0.17 | 2.37 | 1591 |
| 2024-09-20 22:21:41.521 | MS1 | 121.4656597532 | 31.1446377838 | 704 | 504990 | -90.52 | 7.11 | 521.25 | 0.06 | 2.63 | 1574 |
| 2024-09-20 22:21:42.828 | MS1 | 121.4656696036 | 31.1446329226 | 704 | 504990 | -90.81 | 10.69 | 357.98 | 0.08 | 2.61 | 1577 |

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
| 3236322 | 1 | 121.4699605628 | 31.1470200301 | 269 | 0 | 7 | 38.5 | TDD | 704 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3247474 | 4 | 121.4683300036 | 31.1447155675 | 88 | 0 | 0 | 30.4 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3263392 | 2 | 121.4670904680 | 31.1465161242 | 139 | 4 | 10 | 41.1 | TDD | 504 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3265604 | 3 | 121.4697381502 | 31.1475996464 | 85 | 3 | 8 | 36.5 | TDD | 772 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.522 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.546 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.680 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.680 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.387 | NREventA3 | measId:2;ServCellPCI:605;Se... |
| 2024-09-20 22:21:38.627 | NRHandoverAttempt | SourcePCI:605;SourceNR-ARFC... |
| 2024-09-20 22:21:38.668 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.679 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.816 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.816 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236322 | 1 | 12.8882 | 11.8651 | -115.1962 | 7.8413 | 124.0177 | 0.0128 | 0.0189 |
| 2024_09_20 22:00 | 3263392 | 2 | 17.2267 | 13.0084 | -114.7230 | 15.0764 | 185.2583 | 0.0191 | 0.0055 |
| 2024_09_20 22:00 | 3265604 | 3 | 6.9385 | 14.5998 | -116.6612 | 7.8376 | 162.4240 | 0.0120 | 0.0073 |
| 2024_09_20 22:00 | 3247474 | 4 | 7.6976 | 7.9976 | -115.5742 | 9.3690 | 193.4900 | 0.0143 | 0.0062 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415895_9A05877B | 504990 | 704 | -84.3 | 504990 | 772 | -92.5 | 504990 | 309 | -92.1 | 504990 | 504 |
| MR_1774415895_C9068AD4 | 504990 | 704 | -85.8 | 504990 | 772 | -93.3 | 504990 | 309 | -95.5 | 504990 | 504 |
| MR_1774415895_8BC5D8EE | 504990 | 704 | -86.5 | 504990 | 772 | -93.6 | 504990 | 309 | -94.3 | 504990 | 504 |
| MR_1774415895_5C8A6BF5 | 504990 | 704 | -85.9 | 504990 | 772 | -92.5 | 504990 | 309 | -94.3 | 504990 | 504 |
| MR_1774415895_7CD85AEB | 504990 | 704 | -86.2 | 504990 | 772 | -94.3 | 504990 | 309 | -94.1 | 504990 | 504 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 241: `1d6d05bc-dfd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1d6d05bc-dfd4-4aa3-9237-37f48916d354` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[241] topology](images/test_0241.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254716_2
- `C2`: Decrease transmission power for 3254716_2
- `C3`: Check test server and transmission issues
- `C4`: Lift the tilt angle of 3276295_6 by 4 degrees
- `C5`: Press down the tilt angle of 3276295_6 by 4 degrees
- `C6`: Adjust the azimuth of 3254716_2 by 25 degrees
- `C7`: Press down the tilt angle  of 3254716_2 by 4 degrees
- `C8`: Lift the tilt angle  of 3254716_2 by 4 degrees
- `C9`: Increase transmission power for 3276295_6
- `C10`: Add neighbor relationship between 3268575_12 and 3254716_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276295_6
- `C12`: Increase A3 Offset threshold for 3276295_6
- `C13`: Increase A3 Offset threshold for 3254716_2
- `C14`: Decrease transmission power for 3276295_6
- `C15`: Adjust the azimuth of 3276295_6 by 42 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase transmission power for 3254716_2
- `C18`: Decrease A3 Offset threshold for 3276295_6
- `C19`: Add neighbor relationship between 3276295_6 and 3254716_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254716_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276295_6
- `C22`: Decrease A3 Offset threshold for 3254716_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.752 | MS1 | 121.4656654247 | 31.1446300336 | 701 | 504990 | -95.49 | 14.62 | 321.87 | 0.05 | 2.33 | 1567 |
| 2024-09-20 22:21:32.346 | MS1 | 121.4656632070 | 31.1446371983 | 111 | 504990 | -94.75 | 12.09 | 579.14 | 0.05 | 2.06 | 1570 |
| 2024-09-20 22:21:33.649 | MS1 | 121.4656778615 | 31.1446349356 | 26 | 504990 | -93.83 | 14.29 | 461.21 | 0.16 | 2.40 | 1577 |
| 2024-09-20 22:21:34.634 | MS1 | 121.4656709520 | 31.1446211143 | 291 | 152650 | -88.62 | 3.00 | 67.11 | 0.12 | 1.74 | 948 |
| 2024-09-20 22:21:35.310 | MS1 | 121.4656736929 | 31.1446367133 | 727 | 152650 | -95.91 | 2.03 | 47.04 | 0.19 | 1.81 | 947 |
| 2024-09-20 22:21:36.308 | MS1 | 121.4656699396 | 31.1446211412 | 338 | 152650 | -93.76 | 3.88 | 65.53 | 0.13 | 1.91 | 907 |
| 2024-09-20 22:21:37.353 | MS1 | 121.4656660954 | 31.1446331999 | 620 | 152650 | -90.59 | 7.34 | 57.86 | 0.14 | 1.97 | 904 |
| 2024-09-20 22:21:38.749 | MS1 | 121.4656663803 | 31.1446302411 | 291 | 152650 | -96.13 | 6.75 | 71.17 | 0.01 | 1.99 | 981 |
| 2024-09-20 22:21:39.761 | MS1 | 121.4656624081 | 31.1446181177 | 727 | 152650 | -94.37 | 5.54 | 65.60 | 0.16 | 1.53 | 960 |
| 2024-09-20 22:21:40.604 | MS1 | 121.4656650276 | 31.1446228938 | 338 | 152650 | -90.83 | 6.36 | 80.13 | 0.06 | 2.51 | 1571 |
| 2024-09-20 22:21:41.121 | MS1 | 121.4656776595 | 31.1446277374 | 620 | 152650 | -96.57 | 5.12 | 67.16 | 0.15 | 2.87 | 1572 |
| 2024-09-20 22:21:42.175 | MS1 | 121.4656742522 | 31.1446180260 | 291 | 152650 | -92.85 | 2.32 | 60.59 | 0.00 | 2.86 | 1591 |

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
| 3218289 | 10 | 121.4743198348 | 31.1447366436 | 106 | 0 | 1 | 9.4 | FDD | 40 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3224741 | 4 | 121.4643088560 | 31.1506062853 | 20 | 8 | 5 | 10.7 | TDD | 565 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3229633 | 9 | 121.4709132677 | 31.1538144054 | 1 | 5 | 2 | 12.9 | FDD | 391 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3231097 | 5 | 121.4731951412 | 31.1559377872 | 302 | 15 | 10 | 27.0 | TDD | 26 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3242074 | 11 | 121.4732430915 | 31.1551067092 | 132 | 15 | 4 | 7.1 | FDD | 620 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3246672 | 13 | 121.4715891213 | 31.1536399496 | 136 | 7 | 11 | 23.4 | FDD | 727 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3254716 | 2 | 121.4670513861 | 31.1530729764 | 163 | 3 | 1 | 12.8 | TDD | 490 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3258173 | 7 | 121.4706734341 | 31.1441600741 | 232 | 15 | 10 | 22.2 | FDD | 291 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3265360 | 3 | 121.4651591819 | 31.1546492600 | 211 | 14 | 8 | 3.6 | TDD | 111 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3268575 | 12 | 121.4747962363 | 31.1529757624 | 302 | 15 | 11 | 15.0 | FDD | 338 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3269154 | 1 | 121.4719421737 | 31.1503666585 | 97 | 9 | 12 | 23.8 | TDD | 169 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3276295 | 6 | 121.4708610651 | 31.1550144542 | 245 | 3 | 11 | 28.3 | TDD | 701 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3276702 | 8 | 121.4706356094 | 31.1495097823 | 149 | 3 | 9 | 2.2 | FDD | 485 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |

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
| 2024-09-20 22:21:30.983 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.002 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.129 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.129 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.795 | NREventA2 | measId:1;ServCellPCI:435;Se... |
| 2024-09-20 22:21:34.935 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.192 | NREventA5 | measId:3;ServCellPCI:435;Se... |
| 2024-09-20 22:21:35.224 | NRHandoverAttempt | SourcePCI:435;SourceNR-ARFC... |
| 2024-09-20 22:21:35.250 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.264 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.401 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.401 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269154 | 1 | 5.5591 | 11.4391 | -116.7593 | 5.1639 | 126.3448 | 0.0075 | 0.0062 |
| 2024_09_20 22:00 | 3254716 | 2 | 5.4183 | 10.1202 | -115.7696 | 16.0000 | 144.3910 | 0.0113 | 0.0098 |
| 2024_09_20 22:00 | 3265360 | 3 | 10.3039 | 13.6632 | -115.4836 | 6.0926 | 101.0658 | 0.0126 | 0.0076 |
| 2024_09_20 22:00 | 3224741 | 4 | 14.4012 | 14.4053 | -114.2714 | 12.6755 | 173.1333 | 0.0063 | 0.0157 |
| 2024_09_20 22:00 | 3231097 | 5 | 18.8298 | 11.9956 | -115.8124 | 11.9471 | 142.3835 | 0.0181 | 0.0133 |
| 2024_09_20 22:00 | 3276295 | 6 | 10.3731 | 6.7146 | -114.7039 | 16.8821 | 187.1804 | 0.0026 | 0.0068 |
| 2024_09_20 22:00 | 3258173 | 7 | 18.5124 | 14.1239 | -115.9381 | 3.3902 | 33.7125 | 0.0175 | 0.0041 |
| 2024_09_20 22:00 | 3276702 | 8 | 9.8986 | 13.4795 | -116.6018 | 3.6480 | 35.8001 | 0.0025 | 0.0151 |
| 2024_09_20 22:00 | 3229633 | 9 | 17.6970 | 8.3561 | -116.0617 | 3.0446 | 49.3777 | 0.0071 | 0.0060 |
| 2024_09_20 22:00 | 3218289 | 10 | 14.9202 | 15.7390 | -116.4666 | 4.2719 | 20.5729 | 0.0007 | 0.0045 |
| 2024_09_20 22:00 | 3242074 | 11 | 12.9537 | 16.9502 | -116.6021 | 3.0472 | 33.0281 | 0.0189 | 0.0153 |
| 2024_09_20 22:00 | 3268575 | 12 | 19.6689 | 5.7259 | -116.0503 | 4.4627 | 57.4496 | 0.0136 | 0.0062 |
| 2024_09_20 22:00 | 3246672 | 13 | 16.7318 | 8.8258 | -117.9031 | 4.4142 | 23.4183 | 0.0118 | 0.0099 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413801_A76ED3E9 | 504990 | 26 | -94.0 | 504990 | 490 | -92.4 | 504990 | 565 | -99.3 | 504990 | 169 |
| MR_1774413801_048FC312 | 152650 | 291 | -90.4 | 152650 | 391 | -96.4 | 152650 | 40 | -97.5 | 152650 | 485 |
| MR_1774413801_821ACD09 | 152650 | 291 | -89.9 | 152650 | 391 | -95.9 | 152650 | 40 | -99.7 | 152650 | 485 |
| MR_1774413801_616D26C7 | 504990 | 26 | -92.5 | 504990 | 490 | -91.1 | 504990 | 565 | -99.4 | 504990 | 169 |
| MR_1774413801_673874B9 | 504990 | 26 | -91.8 | 504990 | 490 | -92.1 | 504990 | 565 | -98.7 | 504990 | 169 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 242: `5164011d-5df...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5164011d-5df3-42c4-869b-d611dcbfabe2` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[242] topology](images/test_0242.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3274629_4
- `C2`: Lift the tilt angle of 3255894_1 by 6 degrees
- `C3`: Add neighbor relationship between 3255894_1 and 3274629_4
- `C4`: Lift the tilt angle  of 3274629_4 by 10 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255894_1
- `C6`: Increase A3 Offset threshold for 3255894_1
- `C7`: Increase transmission power for 3274629_4
- `C8`: Check test server and transmission issues
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Increase A3 Offset threshold for 3274629_4
- `C11`: Press down the tilt angle  of 3274629_4 by 10 degrees
- `C12`: Decrease transmission power for 3255894_1
- `C13`: Press down the tilt angle of 3255894_1 by 6 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274629_4
- `C15`: Adjust the azimuth of 3274629_4 by 50 degrees
- `C16`: Add neighbor relationship between 3258131_2 and 3274629_4
- `C17`: Decrease A3 Offset threshold for 3255894_1
- `C18`: Adjust the azimuth of 3255894_1 by 35 degrees
- `C19`: Decrease A3 Offset threshold for 3274629_4
- `C20`: Increase transmission power for 3255894_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255894_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274629_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.199 | MS1 | 121.4656680488 | 31.1446285558 | 441 | 504990 | -89.89 | 12.80 | 468.49 | 0.04 | 2.05 | 1599 |
| 2024-09-20 22:21:32.619 | MS1 | 121.4656610986 | 31.1446241819 | 441 | 504990 | -87.00 | 16.05 | 337.12 | 0.08 | 2.57 | 1579 |
| 2024-09-20 22:21:33.130 | MS1 | 121.4656726524 | 31.1446250026 | 441 | 504990 | -91.54 | 17.14 | 464.38 | 0.14 | 2.36 | 1589 |
| 2024-09-20 22:21:34.668 | MS1 | 121.4656711134 | 31.1446264896 | 441 | 504990 | -91.29 | 17.05 | 61.39 | 0.56 | 2.04 | 635 |
| 2024-09-20 22:21:35.899 | MS1 | 121.4656664218 | 31.1446294031 | 441 | 504990 | -85.15 | 14.56 | 96.08 | 0.69 | 2.56 | 612 |
| 2024-09-20 22:21:36.552 | MS1 | 121.4656767003 | 31.1446277116 | 441 | 504990 | -85.11 | 13.70 | 64.56 | 0.61 | 2.13 | 631 |
| 2024-09-20 22:21:37.699 | MS1 | 121.4656700092 | 31.1446322538 | 441 | 504990 | -93.33 | 10.09 | 66.76 | 0.54 | 2.16 | 689 |
| 2024-09-20 22:21:38.355 | MS1 | 121.4656681065 | 31.1446180509 | 441 | 504990 | -92.98 | 8.45 | 93.98 | 0.66 | 2.70 | 540 |
| 2024-09-20 22:21:39.425 | MS1 | 121.4656772589 | 31.1446284329 | 441 | 504990 | -91.65 | 7.19 | 68.09 | 0.51 | 2.09 | 500 |
| 2024-09-20 22:21:40.883 | MS1 | 121.4656605479 | 31.1446251906 | 441 | 504990 | -92.25 | 11.14 | 318.35 | 0.11 | 2.24 | 1577 |
| 2024-09-20 22:21:41.342 | MS1 | 121.4656694892 | 31.1446293094 | 441 | 504990 | -90.04 | 12.43 | 387.67 | 0.09 | 2.36 | 1595 |
| 2024-09-20 22:21:42.871 | MS1 | 121.4656701080 | 31.1446183358 | 441 | 504990 | -90.75 | 8.09 | 392.77 | 0.01 | 2.02 | 1590 |

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
| 3218858 | 3 | 121.4705687623 | 31.1517502613 | 154 | 2 | 12 | 37.2 | TDD | 106 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3255894 | 1 | 121.4646937253 | 31.1520167828 | 209 | 4 | 2 | 28.6 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3258131 | 2 | 121.4705542594 | 31.1516482251 | 351 | 2 | 12 | 45.4 | TDD | 138 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3274629 | 4 | 121.4725264182 | 31.1471215201 | 86 | 8 | 10 | 36.1 | TDD | 487 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.890 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.910 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.056 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.056 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.745 | NREventA3 | measId:2;ServCellPCI:157;Se... |
| 2024-09-20 22:21:37.985 | NRHandoverAttempt | SourcePCI:157;SourceNR-ARFC... |
| 2024-09-20 22:21:38.025 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.037 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.187 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.187 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255894 | 1 | 11.7812 | 10.3562 | -116.8666 | 7.6831 | 146.1157 | 0.0104 | 0.0074 |
| 2024_09_20 22:00 | 3258131 | 2 | 13.7746 | 18.7923 | -116.2505 | 11.6065 | 102.0060 | 0.0044 | 0.0096 |
| 2024_09_20 22:00 | 3218858 | 3 | 11.2198 | 17.8392 | -117.2016 | 13.9134 | 188.5459 | 0.0054 | 0.0156 |
| 2024_09_20 22:00 | 3274629 | 4 | 5.3969 | 14.1320 | -117.4597 | 13.8875 | 97.8741 | 0.0043 | 0.0128 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416860_1428084D | 504990 | 441 | -90.5 | 504990 | 487 | -98.2 | 504990 | 138 | -104.1 | 504990 | 106 |
| MR_1774416860_7B3A25B1 | 504990 | 441 | -89.4 | 504990 | 487 | -95.9 | 504990 | 138 | -107.6 | 504990 | 106 |
| MR_1774416860_01AF3993 | 504990 | 441 | -89.3 | 504990 | 487 | -96.0 | 504990 | 138 | -107.9 | 504990 | 106 |
| MR_1774416860_2C144921 | 504990 | 441 | -90.9 | 504990 | 487 | -99.6 | 504990 | 138 | -106.9 | 504990 | 106 |
| MR_1774416860_E08F01F8 | 504990 | 441 | -92.0 | 504990 | 487 | -97.0 | 504990 | 138 | -107.7 | 504990 | 106 |
| MR_1774416860_CD441435 | 504990 | 441 | -90.0 | 504990 | 487 | -96.6 | 504990 | 138 | -105.6 | 504990 | 106 |
| MR_1774416860_F446E98D | 504990 | 441 | -91.3 | 504990 | 487 | -97.0 | 504990 | 138 | -105.8 | 504990 | 106 |
| MR_1774416860_70F993B0 | 504990 | 441 | -89.6 | 504990 | 487 | -99.6 | 504990 | 138 | -105.1 | 504990 | 106 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 243: `53b0e0b6-b3b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `53b0e0b6-b3bd-4b84-afc2-18365086fb1c` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[243] topology](images/test_0243.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3211680_1 by 3 degrees
- `C2`: Check test server and transmission issues
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233357_3
- `C4`: Adjust the azimuth of 3233357_3 by 15 degrees
- `C5`: Lift the tilt angle of 3233357_3 by 3 degrees
- `C6`: Increase transmission power for 3211680_1
- `C7`: Lift the tilt angle  of 3211680_1 by 3 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211680_1
- `C9`: Add neighbor relationship between 3263739_2 and 3211680_1
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase transmission power for 3233357_3
- `C12`: Adjust the azimuth of 3211680_1 by 13 degrees
- `C13`: Decrease transmission power for 3233357_3
- `C14`: Add neighbor relationship between 3233357_3 and 3211680_1
- `C15`: Press down the tilt angle of 3233357_3 by 3 degrees
- `C16`: Increase A3 Offset threshold for 3211680_1
- `C17`: Decrease transmission power for 3211680_1
- `C18`: Increase A3 Offset threshold for 3233357_3
- `C19`: Decrease A3 Offset threshold for 3211680_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211680_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233357_3
- `C22`: Decrease A3 Offset threshold for 3233357_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.930 | MS1 | 121.4656630433 | 31.1446294212 | 536 | 504990 | -83.76 | 14.46 | 571.03 | 0.13 | 2.43 | 1594 |
| 2024-09-20 22:21:32.755 | MS1 | 121.4656600854 | 31.1446337484 | 536 | 504990 | -82.32 | 13.96 | 437.43 | 0.07 | 2.27 | 1594 |
| 2024-09-20 22:21:33.983 | MS1 | 121.4656671850 | 31.1446240464 | 536 | 504990 | -75.65 | 17.87 | 593.13 | 0.18 | 2.25 | 1589 |
| 2024-09-20 22:21:34.736 | MS1 | 121.4656779026 | 31.1446300838 | 316 | 504990 | -85.98 | 4.82 | 40.77 | 0.13 | 1.20 | 1597 |
| 2024-09-20 22:21:35.988 | MS1 | 121.4656743057 | 31.1446279865 | 316 | 504990 | -81.06 | 3.96 | 60.38 | 0.02 | 1.07 | 1584 |
| 2024-09-20 22:21:36.362 | MS1 | 121.4656591917 | 31.1446185534 | 536 | 504990 | -80.35 | 1.65 | 48.29 | 0.03 | 1.37 | 1580 |
| 2024-09-20 22:21:37.464 | MS1 | 121.4656744795 | 31.1446304249 | 536 | 504990 | -86.32 | 3.78 | 58.56 | 0.14 | 1.18 | 1579 |
| 2024-09-20 22:21:38.645 | MS1 | 121.4656696576 | 31.1446313203 | 316 | 504990 | -88.04 | 2.58 | 60.48 | 0.00 | 1.46 | 1596 |
| 2024-09-20 22:21:39.974 | MS1 | 121.4656593732 | 31.1446297651 | 316 | 504990 | -84.74 | 1.69 | 64.67 | 0.13 | 1.29 | 1566 |
| 2024-09-20 22:21:40.777 | MS1 | 121.4656610539 | 31.1446351452 | 316 | 504990 | -80.61 | 16.74 | 483.38 | 0.02 | 2.14 | 1592 |
| 2024-09-20 22:21:41.654 | MS1 | 121.4656589164 | 31.1446370961 | 316 | 504990 | -75.89 | 13.77 | 448.61 | 0.06 | 2.94 | 1596 |
| 2024-09-20 22:21:42.730 | MS1 | 121.4656673041 | 31.1446307643 | 316 | 504990 | -82.40 | 17.78 | 381.96 | 0.10 | 2.15 | 1582 |

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
| 3211680 | 1 | 121.4711361816 | 31.1470512504 | 230 | 0 | 7 | 29.5 | TDD | 673 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3232314 | 5 | 121.4715282592 | 31.1510977835 | 108 | 0 | 4 | 39.3 | TDD | 316 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3233357 | 3 | 121.4668735328 | 31.1496268956 | 177 | 1 | 9 | 19.1 | TDD | 536 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3263739 | 2 | 121.4720005507 | 31.1506753687 | 328 | 8 | 3 | 49.9 | TDD | 265 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3278504 | 4 | 121.4654567850 | 31.1487902921 | 259 | 6 | 1 | 26.9 | TDD | 280 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.839 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.858 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.005 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.005 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.654 | NREventA3 | measId:2;ServCellPCI:752;Se... |
| 2024-09-20 22:21:33.894 | NRHandoverAttempt | SourcePCI:752;SourceNR-ARFC... |
| 2024-09-20 22:21:33.924 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:33.939 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.086 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.086 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.654 | NREventA3 | measId:2;ServCellPCI:834;Se... |
| 2024-09-20 22:21:35.894 | NRHandoverAttempt | SourcePCI:834;SourceNR-ARFC... |
| 2024-09-20 22:21:35.931 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.941 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:36.086 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.086 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.654 | NREventA3 | measId:2;ServCellPCI:752;Se... |
| 2024-09-20 22:21:37.894 | NRHandoverAttempt | SourcePCI:752;SourceNR-ARFC... |
| 2024-09-20 22:21:37.930 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.941 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.073 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.073 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211680 | 1 | 18.3767 | 6.6670 | -115.8634 | 14.3507 | 117.8804 | 0.0146 | 0.0157 |
| 2024_09_20 22:00 | 3263739 | 2 | 8.6952 | 12.3324 | -116.9636 | 11.6980 | 193.7979 | 0.0134 | 0.0031 |
| 2024_09_20 22:00 | 3233357 | 3 | 19.1640 | 19.4899 | -115.3910 | 18.1121 | 134.5894 | 0.0004 | 0.0139 |
| 2024_09_20 22:00 | 3278504 | 4 | 11.9867 | 10.1630 | -114.8655 | 10.4027 | 151.5211 | 0.0166 | 0.0024 |
| 2024_09_20 22:00 | 3232314 | 5 | 11.0112 | 16.0973 | -116.0379 | 5.5024 | 157.9860 | 0.0122 | 0.0175 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415819_8E2B60DA | 504990 | 316 | -87.4 | 504990 | 536 | -86.2 | 504990 | 673 | -89.1 | 504990 | 265 |
| MR_1774415819_CCAA2B77 | 504990 | 316 | -84.5 | 504990 | 536 | -85.9 | 504990 | 673 | -90.7 | 504990 | 265 |
| MR_1774415819_D099CD72 | 504990 | 536 | -85.3 | 504990 | 316 | -84.7 | 504990 | 673 | -90.1 | 504990 | 265 |
| MR_1774415819_95878B2A | 504990 | 316 | -84.4 | 504990 | 536 | -83.7 | 504990 | 673 | -91.0 | 504990 | 265 |
| MR_1774415819_44C4BF54 | 504990 | 536 | -84.3 | 504990 | 316 | -84.6 | 504990 | 673 | -88.6 | 504990 | 265 |
| MR_1774415819_26CFE542 | 504990 | 316 | -84.1 | 504990 | 536 | -84.5 | 504990 | 673 | -88.9 | 504990 | 265 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 244: `ab98861f-fa2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ab98861f-fa2c-461c-bdf2-f1184aa79bc9` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[244] topology](images/test_0244.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3266105_1 and 3250435_4
- `C2`: Increase A3 Offset threshold for 3266105_1
- `C3`: Decrease A3 Offset threshold for 3250435_4
- `C4`: Lift the tilt angle of 3266105_1 by 4 degrees
- `C5`: Adjust the azimuth of 3250435_4 by 8 degrees
- `C6`: Press down the tilt angle of 3266105_1 by 4 degrees
- `C7`: Decrease transmission power for 3250435_4
- `C8`: Decrease transmission power for 3266105_1
- `C9`: Add neighbor relationship between 3210892_11 and 3250435_4
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase A3 Offset threshold for 3250435_4
- `C12`: Increase transmission power for 3250435_4
- `C13`: Increase transmission power for 3266105_1
- `C14`: Check test server and transmission issues
- `C15`: Decrease A3 Offset threshold for 3266105_1
- `C16`: Adjust the azimuth of 3266105_1 by 26 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266105_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250435_4
- `C19`: Lift the tilt angle  of 3250435_4 by 4 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266105_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250435_4
- `C22`: Press down the tilt angle  of 3250435_4 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.235 | MS1 | 121.4656618082 | 31.1446283028 | 994 | 504990 | -93.35 | 9.29 | 555.98 | 0.06 | 2.21 | 1561 |
| 2024-09-20 22:21:32.576 | MS1 | 121.4656725657 | 31.1446351720 | 651 | 504990 | -93.15 | 10.47 | 513.16 | 0.01 | 2.29 | 1580 |
| 2024-09-20 22:21:33.647 | MS1 | 121.4656586176 | 31.1446260869 | 563 | 504990 | -95.64 | 11.73 | 532.14 | 0.17 | 2.57 | 1586 |
| 2024-09-20 22:21:34.814 | MS1 | 121.4656687314 | 31.1446273601 | 603 | 152650 | -87.12 | 6.07 | 95.30 | 0.16 | 1.70 | 925 |
| 2024-09-20 22:21:35.547 | MS1 | 121.4656771259 | 31.1446317959 | 385 | 152650 | -90.18 | 6.60 | 79.53 | 0.02 | 1.90 | 998 |
| 2024-09-20 22:21:36.420 | MS1 | 121.4656657630 | 31.1446250685 | 241 | 152650 | -91.79 | 5.69 | 80.74 | 0.15 | 1.79 | 961 |
| 2024-09-20 22:21:37.454 | MS1 | 121.4656723013 | 31.1446292730 | 394 | 152650 | -91.76 | 2.01 | 60.78 | 0.14 | 1.69 | 944 |
| 2024-09-20 22:21:38.815 | MS1 | 121.4656752868 | 31.1446242755 | 603 | 152650 | -87.09 | 2.75 | 83.09 | 0.03 | 1.64 | 955 |
| 2024-09-20 22:21:39.310 | MS1 | 121.4656715543 | 31.1446356441 | 385 | 152650 | -90.89 | 4.56 | 56.90 | 0.19 | 1.94 | 977 |
| 2024-09-20 22:21:40.966 | MS1 | 121.4656637785 | 31.1446379857 | 241 | 152650 | -94.45 | 4.07 | 74.84 | 0.12 | 2.98 | 1591 |
| 2024-09-20 22:21:41.681 | MS1 | 121.4656728044 | 31.1446293245 | 394 | 152650 | -94.03 | 7.11 | 70.26 | 0.20 | 2.31 | 1568 |
| 2024-09-20 22:21:42.611 | MS1 | 121.4656722393 | 31.1446321276 | 603 | 152650 | -96.18 | 4.52 | 80.18 | 0.11 | 2.25 | 1566 |

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
| 3210892 | 11 | 121.4669829191 | 31.1456288093 | 191 | 3 | 2 | 3.7 | FDD | 241 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3216025 | 8 | 121.4657720858 | 31.1548218041 | 247 | 4 | 12 | 19.8 | FDD | 293 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3218208 | 2 | 121.4652216550 | 31.1481869052 | 326 | 4 | 11 | 8.7 | TDD | 904 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3233582 | 7 | 121.4713676091 | 31.1543974450 | 265 | 3 | 9 | 8.0 | FDD | 385 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3234172 | 10 | 121.4667770117 | 31.1494189611 | 203 | 0 | 4 | 23.2 | FDD | 878 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3241714 | 9 | 121.4716130787 | 31.1449083341 | 207 | 2 | 1 | 19.7 | FDD | 394 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3249081 | 6 | 121.4688766894 | 31.1556169701 | 97 | 9 | 6 | 3.6 | TDD | 563 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3250435 | 4 | 121.4735177360 | 31.1544442862 | 206 | 4 | 12 | 1.0 | TDD | 684 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3256927 | 13 | 121.4660457321 | 31.1507883066 | 29 | 2 | 7 | 23.7 | FDD | 189 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3264623 | 5 | 121.4695403344 | 31.1440999726 | 236 | 7 | 10 | 27.8 | TDD | 850 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3265728 | 3 | 121.4700158975 | 31.1440742865 | 184 | 9 | 8 | 26.7 | TDD | 651 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3266105 | 1 | 121.4723278112 | 31.1505136930 | 250 | 4 | 7 | 1.9 | TDD | 994 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3271571 | 12 | 121.4716659497 | 31.1462666609 | 102 | 4 | 10 | 9.0 | FDD | 603 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |

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
| 2024-09-20 22:21:31.301 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.320 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.448 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.448 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.161 | NREventA2 | measId:1;ServCellPCI:55;Ser... |
| 2024-09-20 22:21:35.304 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.522 | NREventA5 | measId:3;ServCellPCI:55;Ser... |
| 2024-09-20 22:21:35.562 | NRHandoverAttempt | SourcePCI:55;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.591 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.604 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.715 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.715 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266105 | 1 | 15.7667 | 8.9726 | -117.5446 | 5.7490 | 171.7593 | 0.0021 | 0.0143 |
| 2024_09_20 22:00 | 3218208 | 2 | 6.1194 | 8.3236 | -114.0069 | 15.0374 | 123.2670 | 0.0131 | 0.0136 |
| 2024_09_20 22:00 | 3265728 | 3 | 14.5323 | 10.1377 | -115.3639 | 5.1180 | 94.6818 | 0.0010 | 0.0072 |
| 2024_09_20 22:00 | 3250435 | 4 | 10.0119 | 14.1071 | -116.5130 | 9.3716 | 134.1394 | 0.0148 | 0.0036 |
| 2024_09_20 22:00 | 3264623 | 5 | 18.4779 | 14.4936 | -117.3145 | 6.0631 | 185.7272 | 0.0059 | 0.0086 |
| 2024_09_20 22:00 | 3249081 | 6 | 17.1985 | 12.9204 | -116.8158 | 10.8144 | 192.5967 | 0.0175 | 0.0029 |
| 2024_09_20 22:00 | 3233582 | 7 | 7.4506 | 15.3565 | -116.0626 | 3.5502 | 40.7871 | 0.0088 | 0.0007 |
| 2024_09_20 22:00 | 3216025 | 8 | 8.6843 | 19.3647 | -117.8899 | 4.9912 | 27.5983 | 0.0039 | 0.0118 |
| 2024_09_20 22:00 | 3241714 | 9 | 10.4807 | 7.5920 | -114.3375 | 3.6295 | 21.5876 | 0.0118 | 0.0140 |
| 2024_09_20 22:00 | 3234172 | 10 | 13.6724 | 16.0882 | -117.9109 | 3.4720 | 20.7439 | 0.0022 | 0.0192 |
| 2024_09_20 22:00 | 3210892 | 11 | 16.5410 | 14.8543 | -114.9862 | 4.6213 | 22.5965 | 0.0029 | 0.0171 |
| 2024_09_20 22:00 | 3271571 | 12 | 16.4819 | 12.3101 | -115.8538 | 3.1368 | 44.0143 | 0.0054 | 0.0013 |
| 2024_09_20 22:00 | 3256927 | 13 | 17.6845 | 5.9737 | -116.0567 | 3.2107 | 46.3532 | 0.0028 | 0.0041 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416626_95613AC3 | 504990 | 563 | -93.8 | 504990 | 684 | -91.0 | 504990 | 850 | -96.5 | 504990 | 904 |
| MR_1774416626_2AB128A5 | 152650 | 603 | -87.4 | 152650 | 878 | -89.3 | 152650 | 189 | -95.7 | 152650 | 293 |
| MR_1774416626_62FA0F8A | 152650 | 603 | -85.8 | 152650 | 878 | -91.9 | 152650 | 189 | -93.2 | 152650 | 293 |
| MR_1774416626_4DFD257D | 152650 | 603 | -87.5 | 152650 | 878 | -90.3 | 152650 | 189 | -96.0 | 152650 | 293 |
| MR_1774416626_627C1AB3 | 152650 | 603 | -88.7 | 152650 | 878 | -91.6 | 152650 | 189 | -95.8 | 152650 | 293 |
| MR_1774416626_F7A7F200 | 152650 | 603 | -87.3 | 152650 | 878 | -91.2 | 152650 | 189 | -95.0 | 152650 | 293 |
| MR_1774416626_25FA289F | 152650 | 603 | -85.6 | 152650 | 878 | -89.5 | 152650 | 189 | -94.1 | 152650 | 293 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 245: `08982883-e4e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `08982883-e4e6-427c-8e83-5239ce67a804` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[245] topology](images/test_0245.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3273814_12 and 3215935_4
- `C2`: Decrease A3 Offset threshold for 3215935_4
- `C3`: Decrease transmission power for 3215935_4
- `C4`: Increase A3 Offset threshold for 3267839_6
- `C5`: Increase transmission power for 3267839_6
- `C6`: Decrease transmission power for 3267839_6
- `C7`: Add neighbor relationship between 3267839_6 and 3215935_4
- `C8`: Press down the tilt angle of 3267839_6 by 5 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215935_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267839_6
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase transmission power for 3215935_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215935_4
- `C14`: Increase A3 Offset threshold for 3215935_4
- `C15`: Press down the tilt angle  of 3215935_4 by 3 degrees
- `C16`: Decrease A3 Offset threshold for 3267839_6
- `C17`: Adjust the azimuth of 3267839_6 by 38 degrees
- `C18`: Adjust the azimuth of 3215935_4 by 1 degrees
- `C19`: Lift the tilt angle  of 3215935_4 by 3 degrees
- `C20`: Check test server and transmission issues
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267839_6
- `C22`: Lift the tilt angle of 3267839_6 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.576 | MS1 | 121.4656706596 | 31.1446350654 | 216 | 504990 | -93.76 | 10.10 | 506.84 | 0.04 | 2.38 | 1566 |
| 2024-09-20 22:21:32.200 | MS1 | 121.4656666648 | 31.1446331941 | 678 | 504990 | -94.75 | 13.17 | 342.74 | 0.03 | 2.12 | 1597 |
| 2024-09-20 22:21:33.401 | MS1 | 121.4656611526 | 31.1446180143 | 608 | 504990 | -93.50 | 12.09 | 530.14 | 0.16 | 2.22 | 1587 |
| 2024-09-20 22:21:34.680 | MS1 | 121.4656733149 | 31.1446205662 | 716 | 152650 | -89.68 | 2.88 | 69.38 | 0.04 | 1.82 | 924 |
| 2024-09-20 22:21:35.862 | MS1 | 121.4656669778 | 31.1446229613 | 897 | 152650 | -91.31 | 5.01 | 88.51 | 0.02 | 1.86 | 977 |
| 2024-09-20 22:21:36.916 | MS1 | 121.4656721931 | 31.1446229756 | 860 | 152650 | -91.19 | 4.04 | 81.24 | 0.03 | 1.52 | 962 |
| 2024-09-20 22:21:37.459 | MS1 | 121.4656703753 | 31.1446285941 | 303 | 152650 | -91.94 | 4.93 | 83.28 | 0.15 | 1.53 | 993 |
| 2024-09-20 22:21:38.800 | MS1 | 121.4656640040 | 31.1446193704 | 716 | 152650 | -94.35 | 2.88 | 92.96 | 0.06 | 1.96 | 916 |
| 2024-09-20 22:21:39.378 | MS1 | 121.4656583262 | 31.1446257073 | 897 | 152650 | -88.94 | 4.09 | 85.50 | 0.16 | 1.91 | 981 |
| 2024-09-20 22:21:40.302 | MS1 | 121.4656774499 | 31.1446205652 | 860 | 152650 | -95.96 | 4.24 | 84.97 | 0.12 | 2.74 | 1595 |
| 2024-09-20 22:21:41.959 | MS1 | 121.4656599075 | 31.1446236512 | 303 | 152650 | -88.29 | 3.62 | 74.04 | 0.12 | 2.85 | 1589 |
| 2024-09-20 22:21:42.695 | MS1 | 121.4656757840 | 31.1446188830 | 716 | 152650 | -90.80 | 3.94 | 53.82 | 0.15 | 2.44 | 1588 |

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
| 3215935 | 4 | 121.4724126028 | 31.1503256960 | 224 | 2 | 11 | 22.7 | TDD | 331 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3217312 | 5 | 121.4689404144 | 31.1469937750 | 210 | 0 | 7 | 25.2 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3218806 | 1 | 121.4729550008 | 31.1476382306 | 27 | 10 | 4 | 21.1 | TDD | 608 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3219155 | 11 | 121.4696699172 | 31.1559813864 | 331 | 13 | 2 | 29.6 | FDD | 817 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3220914 | 8 | 121.4689278189 | 31.1503336461 | 357 | 1 | 8 | 16.3 | FDD | 897 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3229649 | 3 | 121.4759169501 | 31.1440513510 | 202 | 8 | 10 | 17.4 | TDD | 9 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3245304 | 10 | 121.4680295618 | 31.1551449687 | 25 | 12 | 10 | 4.6 | FDD | 303 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3245759 | 2 | 121.4685828991 | 31.1478620741 | 236 | 13 | 10 | 10.6 | TDD | 678 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3261923 | 7 | 121.4680740662 | 31.1467754705 | 288 | 2 | 12 | 14.8 | FDD | 736 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3267839 | 6 | 121.4750069798 | 31.1469698991 | 292 | 5 | 6 | 5.0 | TDD | 216 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3273814 | 12 | 121.4721008822 | 31.1552428170 | 79 | 8 | 8 | 5.8 | FDD | 860 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3274423 | 13 | 121.4673899262 | 31.1521568731 | 359 | 12 | 8 | 4.3 | FDD | 255 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3277381 | 9 | 121.4659661947 | 31.1510515624 | 223 | 1 | 3 | 6.9 | FDD | 716 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |

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
| 2024-09-20 22:21:31.448 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.464 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.591 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.591 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.334 | NREventA2 | measId:1;ServCellPCI:46;Ser... |
| 2024-09-20 22:21:35.437 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.711 | NREventA5 | measId:3;ServCellPCI:46;Ser... |
| 2024-09-20 22:21:35.757 | NRHandoverAttempt | SourcePCI:46;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.802 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.816 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.947 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.947 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218806 | 1 | 14.7473 | 13.2861 | -116.4259 | 6.8132 | 108.9695 | 0.0147 | 0.0092 |
| 2024_09_20 22:00 | 3245759 | 2 | 15.4842 | 5.6052 | -114.4514 | 5.5978 | 147.5609 | 0.0141 | 0.0103 |
| 2024_09_20 22:00 | 3229649 | 3 | 5.4775 | 19.7626 | -115.0763 | 19.1432 | 197.6643 | 0.0094 | 0.0149 |
| 2024_09_20 22:00 | 3215935 | 4 | 7.7003 | 15.4930 | -115.7519 | 16.7955 | 115.3049 | 0.0155 | 0.0024 |
| 2024_09_20 22:00 | 3217312 | 5 | 7.3652 | 16.7156 | -117.8064 | 18.4002 | 118.0579 | 0.0017 | 0.0171 |
| 2024_09_20 22:00 | 3267839 | 6 | 14.5286 | 18.3413 | -116.8077 | 18.4153 | 91.3593 | 0.0026 | 0.0023 |
| 2024_09_20 22:00 | 3261923 | 7 | 11.9265 | 13.8949 | -115.9209 | 3.4677 | 43.5481 | 0.0078 | 0.0121 |
| 2024_09_20 22:00 | 3220914 | 8 | 11.1639 | 10.6672 | -115.8739 | 4.3339 | 24.1856 | 0.0198 | 0.0166 |
| 2024_09_20 22:00 | 3277381 | 9 | 9.9733 | 14.3429 | -116.9607 | 4.2746 | 52.6589 | 0.0054 | 0.0027 |
| 2024_09_20 22:00 | 3245304 | 10 | 8.9604 | 5.4893 | -116.3084 | 3.7223 | 34.3845 | 0.0131 | 0.0135 |
| 2024_09_20 22:00 | 3219155 | 11 | 17.7383 | 14.8893 | -116.4612 | 3.2692 | 28.6901 | 0.0130 | 0.0101 |
| 2024_09_20 22:00 | 3273814 | 12 | 10.8746 | 9.9087 | -116.1760 | 4.0601 | 37.3059 | 0.0160 | 0.0188 |
| 2024_09_20 22:00 | 3274423 | 13 | 6.2226 | 16.9404 | -114.7514 | 4.8162 | 23.6666 | 0.0155 | 0.0080 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416823_3CDF9C05 | 504990 | 608 | -91.7 | 504990 | 331 | -96.5 | 504990 | 309 | -97.6 | 504990 | 9 |
| MR_1774416823_8FBBC829 | 152650 | 716 | -89.4 | 152650 | 817 | -95.8 | 152650 | 255 | -98.6 | 152650 | 736 |
| MR_1774416823_8D17A1AC | 504990 | 608 | -91.8 | 504990 | 331 | -93.7 | 504990 | 309 | -97.2 | 504990 | 9 |
| MR_1774416823_48587D44 | 152650 | 716 | -88.8 | 152650 | 817 | -95.1 | 152650 | 255 | -101.3 | 152650 | 736 |
| MR_1774416823_63BAA349 | 152650 | 716 | -88.3 | 152650 | 817 | -95.2 | 152650 | 255 | -100.9 | 152650 | 736 |
| MR_1774416823_B1B2A026 | 152650 | 716 | -89.7 | 152650 | 817 | -96.0 | 152650 | 255 | -99.3 | 152650 | 736 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 246: `0d99d2b4-834...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0d99d2b4-8344-491a-8ffc-5cf63b7d9c9e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[246] topology](images/test_0246.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3258582_3 by 26 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258582_3
- `C3`: Lift the tilt angle  of 3236676_2 by 4 degrees
- `C4`: Increase A3 Offset threshold for 3258582_3
- `C5`: Add neighbor relationship between 3258401_4 and 3236676_2
- `C6`: Check test server and transmission issues
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease transmission power for 3258582_3
- `C9`: Lift the tilt angle of 3258582_3 by 10 degrees
- `C10`: Decrease transmission power for 3236676_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236676_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258582_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236676_2
- `C14`: Increase A3 Offset threshold for 3236676_2
- `C15`: Decrease A3 Offset threshold for 3236676_2
- `C16`: Increase transmission power for 3258582_3
- `C17`: Press down the tilt angle  of 3236676_2 by 4 degrees
- `C18`: Decrease A3 Offset threshold for 3258582_3
- `C19`: Press down the tilt angle of 3258582_3 by 10 degrees
- `C20`: Increase transmission power for 3236676_2
- `C21`: Adjust the azimuth of 3236676_2 by 4 degrees
- `C22`: Add neighbor relationship between 3258582_3 and 3236676_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.451 | MS1 | 121.4656688917 | 31.1446355263 | 638 | 504990 | -77.31 | 12.06 | 361.29 | 0.17 | 2.28 | 1581 |
| 2024-09-20 22:21:32.379 | MS1 | 121.4656605457 | 31.1446268197 | 638 | 504990 | -82.56 | 12.40 | 516.97 | 0.01 | 2.62 | 1584 |
| 2024-09-20 22:21:33.176 | MS1 | 121.4656695474 | 31.1446373073 | 638 | 504990 | -78.73 | 16.02 | 585.74 | 0.17 | 2.33 | 1571 |
| 2024-09-20 22:21:34.511 | MS1 | 121.4656771559 | 31.1446182040 | 638 | 504990 | -92.17 | -3.76 | 51.66 | 0.13 | 1.09 | 1567 |
| 2024-09-20 22:21:35.785 | MS1 | 121.4656587566 | 31.1446309187 | 638 | 504990 | -85.95 | -0.96 | 51.75 | 0.20 | 1.12 | 1562 |
| 2024-09-20 22:21:36.502 | MS1 | 121.4656616807 | 31.1446338508 | 638 | 504990 | -88.22 | -1.87 | 47.06 | 0.10 | 1.18 | 1581 |
| 2024-09-20 22:21:37.413 | MS1 | 121.4656745548 | 31.1446207100 | 638 | 504990 | -86.37 | -3.16 | 44.31 | 0.00 | 1.41 | 1571 |
| 2024-09-20 22:21:38.964 | MS1 | 121.4656653502 | 31.1446214181 | 638 | 504990 | -78.29 | 13.35 | 385.75 | 0.04 | 1.41 | 1582 |
| 2024-09-20 22:21:39.203 | MS1 | 121.4656587437 | 31.1446241292 | 638 | 504990 | -84.38 | 16.20 | 374.80 | 0.12 | 1.43 | 1586 |
| 2024-09-20 22:21:40.336 | MS1 | 121.4656777395 | 31.1446196466 | 638 | 504990 | -80.33 | 17.40 | 535.49 | 0.07 | 2.80 | 1583 |
| 2024-09-20 22:21:41.998 | MS1 | 121.4656665405 | 31.1446309794 | 638 | 504990 | -78.90 | 14.97 | 434.42 | 0.14 | 2.79 | 1571 |
| 2024-09-20 22:21:42.458 | MS1 | 121.4656751569 | 31.1446315136 | 638 | 504990 | -81.11 | 15.55 | 350.58 | 0.06 | 2.94 | 1569 |

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
| 3236676 | 2 | 121.4724130962 | 31.1507280451 | 227 | 2 | 12 | 33.9 | TDD | 213 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3250010 | 1 | 121.4675113310 | 31.1459316969 | 313 | 3 | 12 | 20.5 | TDD | 266 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3258401 | 4 | 121.4698902880 | 31.1510903447 | 351 | 3 | 3 | 44.4 | TDD | 543 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3258582 | 3 | 121.4693456779 | 31.1477455210 | 251 | 13 | 4 | 18.0 | TDD | 638 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.084 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.104 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.240 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.240 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.958 | NREventA3 | measId:2;ServCellPCI:918;Se... |
| 2024-09-20 22:21:35.958 | NREventA3 | measId:2;ServCellPCI:918;Se... |
| 2024-09-20 22:21:36.958 | NREventA3 | measId:2;ServCellPCI:918;Se... |
| 2024-09-20 22:21:39.458 | NRRRCReestablishAttempt | PCI:918 |
| 2024-09-20 22:21:39.468 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.478 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.622 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.622 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250010 | 1 | 13.8259 | 8.0650 | -116.7437 | 15.0497 | 135.7753 | 0.0071 | 0.0153 |
| 2024_09_20 22:00 | 3236676 | 2 | 6.7794 | 18.3793 | -115.6588 | 11.1456 | 199.9458 | 0.0062 | 0.0157 |
| 2024_09_20 22:00 | 3258582 | 3 | 19.2426 | 8.7888 | -116.9480 | 18.6994 | 111.4887 | 0.0134 | 0.1537 |
| 2024_09_20 22:00 | 3258401 | 4 | 7.6515 | 18.7897 | -116.8085 | 9.5941 | 196.1346 | 0.0175 | 0.0056 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412194_1B5A7B16 | 504990 | 213 | -87.4 | 504990 | 638 | -92.4 | 504990 | 543 | -95.6 | 504990 | 266 |
| MR_1774412194_DBAFE49B | 504990 | 213 | -88.3 | 504990 | 638 | -92.3 | 504990 | 543 | -94.8 | 504990 | 266 |
| MR_1774412194_0AA698AF | 504990 | 638 | -92.4 | 504990 | 213 | -87.4 | 504990 | 543 | -95.7 | 504990 | 266 |
| MR_1774412194_B6284C9E | 504990 | 213 | -86.9 | 504990 | 638 | -92.5 | 504990 | 543 | -95.4 | 504990 | 266 |
| MR_1774412194_3A128EC9 | 504990 | 638 | -90.7 | 504990 | 213 | -86.1 | 504990 | 543 | -97.8 | 504990 | 266 |
| MR_1774412194_58FF4E09 | 504990 | 638 | -93.0 | 504990 | 213 | -87.0 | 504990 | 543 | -96.8 | 504990 | 266 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 247: `46a737d2-c00...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `46a737d2-c00a-4a0b-ab40-90ede90e60fb` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[247] topology](images/test_0247.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3262660_1
- `C2`: Press down the tilt angle of 3266313_3 by 10 degrees
- `C3`: Decrease transmission power for 3266313_3
- `C4`: Lift the tilt angle of 3266313_3 by 10 degrees
- `C5`: Increase transmission power for 3266313_3
- `C6`: Decrease A3 Offset threshold for 3266313_3
- `C7`: Add neighbor relationship between 3258817_4 and 3262660_1
- `C8`: Adjust the azimuth of 3262660_1 by 22 degrees
- `C9`: Increase transmission power for 3262660_1
- `C10`: Decrease A3 Offset threshold for 3262660_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262660_1
- `C12`: Press down the tilt angle  of 3262660_1 by 5 degrees
- `C13`: Increase A3 Offset threshold for 3266313_3
- `C14`: Decrease transmission power for 3262660_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Adjust the azimuth of 3266313_3 by 50 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266313_3
- `C18`: Check test server and transmission issues
- `C19`: Add neighbor relationship between 3266313_3 and 3262660_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266313_3
- `C21`: Lift the tilt angle  of 3262660_1 by 5 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262660_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.412 | MS1 | 121.4656674088 | 31.1446271587 | 283 | 504990 | -83.41 | 15.36 | 310.07 | 0.17 | 2.85 | 1575 |
| 2024-09-20 22:21:32.240 | MS1 | 121.4656592205 | 31.1446365318 | 283 | 504990 | -83.06 | 17.63 | 541.18 | 0.06 | 2.18 | 1582 |
| 2024-09-20 22:21:33.469 | MS1 | 121.4656591208 | 31.1446201146 | 283 | 504990 | -83.72 | 15.45 | 412.43 | 0.10 | 2.42 | 1567 |
| 2024-09-20 22:21:34.853 | MS1 | 121.4656662882 | 31.1446231600 | 283 | 504990 | -89.32 | -3.21 | 55.33 | 0.13 | 1.26 | 1590 |
| 2024-09-20 22:21:35.996 | MS1 | 121.4656654468 | 31.1446218779 | 283 | 504990 | -90.79 | -2.34 | 23.80 | 0.10 | 1.42 | 1597 |
| 2024-09-20 22:21:36.739 | MS1 | 121.4656644774 | 31.1446315220 | 283 | 504990 | -93.37 | -1.28 | 31.98 | 0.08 | 1.22 | 1580 |
| 2024-09-20 22:21:37.696 | MS1 | 121.4656588824 | 31.1446286297 | 283 | 504990 | -85.05 | -2.34 | 39.78 | 0.19 | 1.42 | 1597 |
| 2024-09-20 22:21:38.196 | MS1 | 121.4656635891 | 31.1446268657 | 283 | 504990 | -80.27 | 14.28 | 468.40 | 0.09 | 1.44 | 1597 |
| 2024-09-20 22:21:39.725 | MS1 | 121.4656626174 | 31.1446273380 | 283 | 504990 | -85.00 | 13.54 | 483.09 | 0.02 | 1.08 | 1596 |
| 2024-09-20 22:21:40.836 | MS1 | 121.4656725091 | 31.1446259101 | 283 | 504990 | -78.93 | 17.88 | 483.29 | 0.05 | 2.14 | 1583 |
| 2024-09-20 22:21:41.183 | MS1 | 121.4656765137 | 31.1446360749 | 283 | 504990 | -82.49 | 15.69 | 553.89 | 0.09 | 2.12 | 1566 |
| 2024-09-20 22:21:42.715 | MS1 | 121.4656760473 | 31.1446341911 | 283 | 504990 | -78.33 | 13.40 | 550.11 | 0.15 | 2.95 | 1595 |

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
| 3254619 | 2 | 121.4651438705 | 31.1477634948 | 79 | 5 | 7 | 25.0 | TDD | 418 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3258817 | 4 | 121.4664492112 | 31.1483328972 | 178 | 1 | 11 | 45.2 | TDD | 13 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3262660 | 1 | 121.4757315020 | 31.1473401484 | 274 | 3 | 5 | 37.1 | TDD | 537 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3266313 | 3 | 121.4683121641 | 31.1467179110 | 41 | 13 | 11 | 45.9 | TDD | 283 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.271 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.296 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.422 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.422 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.088 | NREventA3 | measId:2;ServCellPCI:302;Se... |
| 2024-09-20 22:21:36.088 | NREventA3 | measId:2;ServCellPCI:302;Se... |
| 2024-09-20 22:21:37.088 | NREventA3 | measId:2;ServCellPCI:302;Se... |
| 2024-09-20 22:21:39.588 | NRRRCReestablishAttempt | PCI:302 |
| 2024-09-20 22:21:39.607 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.621 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.760 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.760 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262660 | 1 | 9.2786 | 10.9053 | -117.9797 | 19.5456 | 169.8957 | 0.0051 | 0.0098 |
| 2024_09_20 22:00 | 3254619 | 2 | 10.8408 | 7.5740 | -116.0256 | 15.5193 | 193.2170 | 0.0177 | 0.0060 |
| 2024_09_20 22:00 | 3266313 | 3 | 5.0179 | 7.2192 | -116.9335 | 14.5942 | 111.9676 | 0.0194 | 0.1960 |
| 2024_09_20 22:00 | 3258817 | 4 | 16.1267 | 19.0886 | -115.0994 | 9.9299 | 132.5383 | 0.0163 | 0.0151 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415428_9AEE40BE | 504990 | 283 | -87.6 | 504990 | 537 | -83.4 | 504990 | 13 | -90.3 | 504990 | 418 |
| MR_1774415428_B74568F3 | 504990 | 537 | -86.2 | 504990 | 283 | -90.9 | 504990 | 13 | -90.1 | 504990 | 418 |
| MR_1774415428_A498DE67 | 504990 | 283 | -90.1 | 504990 | 537 | -83.4 | 504990 | 13 | -89.5 | 504990 | 418 |
| MR_1774415428_821F868A | 504990 | 283 | -87.4 | 504990 | 537 | -83.8 | 504990 | 13 | -90.7 | 504990 | 418 |
| MR_1774415428_B9115AC5 | 504990 | 283 | -88.2 | 504990 | 537 | -84.8 | 504990 | 13 | -89.1 | 504990 | 418 |
| MR_1774415428_2E17B61E | 504990 | 537 | -86.4 | 504990 | 283 | -89.8 | 504990 | 13 | -88.2 | 504990 | 418 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 248: `71375ac3-717...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `71375ac3-7176-49ee-adf1-ec42415219b7` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[248] topology](images/test_0248.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3224308_4
- `C2`: Increase A3 Offset threshold for 3245032_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224308_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245032_3
- `C5`: Press down the tilt angle  of 3245032_3 by 10 degrees
- `C6`: Increase transmission power for 3224308_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245032_3
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease transmission power for 3245032_3
- `C10`: Lift the tilt angle  of 3245032_3 by 10 degrees
- `C11`: Decrease A3 Offset threshold for 3224308_4
- `C12`: Press down the tilt angle of 3224308_4 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3245032_3
- `C14`: Adjust the azimuth of 3224308_4 by 50 degrees
- `C15`: Add neighbor relationship between 3224308_4 and 3245032_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224308_4
- `C17`: Check test server and transmission issues
- `C18`: Adjust the azimuth of 3245032_3 by 23 degrees
- `C19`: Increase transmission power for 3245032_3
- `C20`: Lift the tilt angle of 3224308_4 by 10 degrees
- `C21`: Add neighbor relationship between 3216137_1 and 3245032_3
- `C22`: Decrease transmission power for 3224308_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.422 | MS1 | 121.4656639619 | 31.1446269653 | 405 | 504990 | -79.36 | 16.41 | 518.90 | 0.03 | 2.30 | 1593 |
| 2024-09-20 22:21:32.704 | MS1 | 121.4656612931 | 31.1446320614 | 405 | 504990 | -79.40 | 16.14 | 527.12 | 0.02 | 2.89 | 1565 |
| 2024-09-20 22:21:33.937 | MS1 | 121.4656616138 | 31.1446283045 | 405 | 504990 | -84.31 | 13.61 | 457.00 | 0.16 | 2.10 | 1583 |
| 2024-09-20 22:21:34.751 | MS1 | 121.4656587564 | 31.1446306603 | 405 | 504990 | -89.91 | -2.87 | 77.93 | 0.06 | 1.49 | 1571 |
| 2024-09-20 22:21:35.133 | MS1 | 121.4656652513 | 31.1446230818 | 405 | 504990 | -90.36 | -2.62 | 33.24 | 0.13 | 1.28 | 1562 |
| 2024-09-20 22:21:36.220 | MS1 | 121.4656583641 | 31.1446316196 | 405 | 504990 | -92.26 | -3.57 | 48.37 | 0.01 | 1.37 | 1584 |
| 2024-09-20 22:21:37.591 | MS1 | 121.4656728576 | 31.1446259763 | 405 | 504990 | -83.28 | -3.70 | 26.97 | 0.04 | 1.29 | 1581 |
| 2024-09-20 22:21:38.167 | MS1 | 121.4656581343 | 31.1446267042 | 405 | 504990 | -89.13 | -0.24 | 22.58 | 0.09 | 1.07 | 1583 |
| 2024-09-20 22:21:39.540 | MS1 | 121.4656663148 | 31.1446315544 | 761 | 504990 | -75.04 | 15.06 | 219.65 | 0.08 | 1.30 | 1581 |
| 2024-09-20 22:21:40.157 | MS1 | 121.4656764841 | 31.1446343143 | 761 | 504990 | -83.28 | 14.55 | 554.10 | 0.14 | 2.30 | 1580 |
| 2024-09-20 22:21:41.138 | MS1 | 121.4656617589 | 31.1446316231 | 761 | 504990 | -82.33 | 14.87 | 420.94 | 0.08 | 2.61 | 1585 |
| 2024-09-20 22:21:42.151 | MS1 | 121.4656638020 | 31.1446285606 | 761 | 504990 | -77.18 | 15.64 | 303.72 | 0.02 | 2.92 | 1594 |

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
| 3216137 | 1 | 121.4654547878 | 31.1510303004 | 104 | 6 | 4 | 27.9 | TDD | 841 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3224308 | 4 | 121.4649734987 | 31.1505007321 | 281 | 15 | 7 | 25.6 | TDD | 405 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3239581 | 2 | 121.4657249158 | 31.1484251331 | 235 | 14 | 2 | 37.8 | TDD | 430 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3245032 | 3 | 121.4684363251 | 31.1525717306 | 220 | 11 | 7 | 25.1 | TDD | 761 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.361 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.493 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.493 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.162 | NREventA3 | measId:2;ServCellPCI:358;Se... |
| 2024-09-20 22:21:38.402 | NRHandoverAttempt | SourcePCI:358;SourceNR-ARFC... |
| 2024-09-20 22:21:38.449 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.460 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.593 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.593 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216137 | 1 | 13.5815 | 9.7170 | -115.0675 | 6.6686 | 178.2238 | 0.0174 | 0.0103 |
| 2024_09_20 22:00 | 3239581 | 2 | 14.7483 | 10.1521 | -115.1712 | 10.1215 | 123.7508 | 0.0176 | 0.0074 |
| 2024_09_20 22:00 | 3245032 | 3 | 15.6835 | 15.3812 | -114.4861 | 8.6023 | 94.7430 | 0.0093 | 0.0008 |
| 2024_09_20 22:00 | 3224308 | 4 | 8.7751 | 7.6636 | -115.2628 | 6.7392 | 116.8322 | 0.0012 | 0.1904 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413629_DE4D3D23 | 504990 | 405 | -88.1 | 504990 | 761 | -85.7 | 504990 | 841 | -85.0 | 504990 | 430 |
| MR_1774413629_FC0332D4 | 504990 | 761 | -84.2 | 504990 | 405 | -88.6 | 504990 | 841 | -85.1 | 504990 | 430 |
| MR_1774413629_AD6B29B8 | 504990 | 761 | -83.3 | 504990 | 405 | -91.1 | 504990 | 841 | -85.0 | 504990 | 430 |
| MR_1774413629_39AAAAF3 | 504990 | 405 | -91.9 | 504990 | 761 | -84.4 | 504990 | 841 | -82.0 | 504990 | 430 |
| MR_1774413629_53264159 | 504990 | 405 | -89.2 | 504990 | 761 | -85.6 | 504990 | 841 | -83.6 | 504990 | 430 |
| MR_1774413629_DB43E2BD | 504990 | 405 | -90.1 | 504990 | 761 | -83.9 | 504990 | 841 | -83.4 | 504990 | 430 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 249: `e0d6eae2-499...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e0d6eae2-4992-4bdb-ab99-00abd365445b` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[249] topology](images/test_0249.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264009_1
- `C2`: Press down the tilt angle of 3264009_1 by 3 degrees
- `C3`: Press down the tilt angle  of 3254834_2 by 3 degrees
- `C4`: Check test server and transmission issues
- `C5`: Increase A3 Offset threshold for 3254834_2
- `C6`: Decrease transmission power for 3264009_1
- `C7`: Increase A3 Offset threshold for 3264009_1
- `C8`: Decrease A3 Offset threshold for 3254834_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254834_2
- `C10`: Lift the tilt angle  of 3254834_2 by 3 degrees
- `C11`: Decrease transmission power for 3254834_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Lift the tilt angle of 3264009_1 by 3 degrees
- `C14`: Adjust the azimuth of 3254834_2 by 8 degrees
- `C15`: Adjust the azimuth of 3264009_1 by 18 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264009_1
- `C17`: Decrease A3 Offset threshold for 3264009_1
- `C18`: Add neighbor relationship between 3267900_4 and 3254834_2
- `C19`: Add neighbor relationship between 3264009_1 and 3254834_2
- `C20`: Increase transmission power for 3264009_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254834_2
- `C22`: Increase transmission power for 3254834_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.828 | MS1 | 121.4656760587 | 31.1446315020 | 368 | 504990 | -84.68 | 15.59 | 334.48 | 0.11 | 2.46 | 1585 |
| 2024-09-20 22:21:32.668 | MS1 | 121.4656693805 | 31.1446341313 | 368 | 504990 | -75.50 | 15.05 | 310.82 | 0.12 | 2.97 | 1580 |
| 2024-09-20 22:21:33.801 | MS1 | 121.4656757877 | 31.1446311826 | 368 | 504990 | -81.38 | 15.28 | 314.58 | 0.20 | 2.95 | 1588 |
| 2024-09-20 22:21:34.950 | MS1 | 121.4656760082 | 31.1446363059 | 368 | 504990 | -89.26 | 2.41 | 55.50 | 0.04 | 1.06 | 1582 |
| 2024-09-20 22:21:35.690 | MS1 | 121.4656594345 | 31.1446288593 | 368 | 504990 | -93.63 | 1.53 | 81.86 | 0.18 | 1.12 | 1575 |
| 2024-09-20 22:21:36.795 | MS1 | 121.4656699081 | 31.1446269089 | 368 | 504990 | -92.46 | 3.33 | 38.39 | 0.13 | 1.01 | 1561 |
| 2024-09-20 22:21:37.278 | MS1 | 121.4656656535 | 31.1446185951 | 368 | 504990 | -87.38 | 1.60 | 40.99 | 0.15 | 1.08 | 1580 |
| 2024-09-20 22:21:38.921 | MS1 | 121.4656693658 | 31.1446240472 | 368 | 504990 | -88.95 | 3.76 | 52.22 | 0.10 | 1.45 | 1585 |
| 2024-09-20 22:21:39.543 | MS1 | 121.4656710724 | 31.1446256295 | 368 | 504990 | -87.06 | 2.87 | 64.93 | 0.13 | 1.26 | 1600 |
| 2024-09-20 22:21:40.167 | MS1 | 121.4656619682 | 31.1446282387 | 368 | 504990 | -84.03 | 14.89 | 565.48 | 0.07 | 2.71 | 1580 |
| 2024-09-20 22:21:41.880 | MS1 | 121.4656732710 | 31.1446236054 | 368 | 504990 | -78.89 | 17.88 | 301.15 | 0.17 | 2.92 | 1583 |
| 2024-09-20 22:21:42.653 | MS1 | 121.4656696534 | 31.1446279521 | 368 | 504990 | -84.89 | 15.81 | 387.01 | 0.11 | 2.51 | 1560 |

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
| 3254834 | 2 | 121.4742305086 | 31.1544950785 | 209 | 2 | 0 | 25.3 | TDD | 961 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3264009 | 1 | 121.4678087955 | 31.1506968119 | 215 | 1 | 9 | 25.9 | TDD | 368 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3267900 | 4 | 121.4721694729 | 31.1520036171 | 256 | 14 | 4 | 49.6 | TDD | 445 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3274467 | 3 | 121.4719285124 | 31.1517603970 | 39 | 14 | 0 | 19.1 | TDD | 852 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.562 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.578 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.681 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.681 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264009 | 1 | 11.7026 | 7.1171 | -108.7125 | 10.7941 | 197.1862 | 0.0053 | 0.0166 |
| 2024_09_20 22:00 | 3254834 | 2 | 11.7950 | 18.3772 | -115.0345 | 19.9473 | 127.3438 | 0.0179 | 0.0151 |
| 2024_09_20 22:00 | 3274467 | 3 | 5.9664 | 7.1395 | -116.2686 | 17.5503 | 184.8331 | 0.0176 | 0.0008 |
| 2024_09_20 22:00 | 3267900 | 4 | 7.4430 | 8.7096 | -114.2407 | 5.6375 | 112.8243 | 0.0188 | 0.0064 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412519_4299C2FB | 504990 | 961 | -89.0 | 504990 | 368 | -87.0 | 504990 | 445 | -88.0 | 504990 | 852 |
| MR_1774412519_13F9110F | 504990 | 368 | -88.8 | 504990 | 961 | -86.9 | 504990 | 445 | -90.4 | 504990 | 852 |
| MR_1774412519_C117A2A1 | 504990 | 961 | -87.8 | 504990 | 368 | -84.9 | 504990 | 445 | -88.4 | 504990 | 852 |
| MR_1774412519_30255B39 | 504990 | 368 | -89.7 | 504990 | 961 | -87.6 | 504990 | 445 | -88.3 | 504990 | 852 |
| MR_1774412519_8BDE488F | 504990 | 368 | -88.8 | 504990 | 961 | -85.3 | 504990 | 445 | -88.9 | 504990 | 852 |

> *... 2개 열 생략 (전체 14열)*

---
