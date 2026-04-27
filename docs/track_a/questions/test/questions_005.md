# Track A 문제 분석 — test[40]~test[49]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[40] ~ test[49] (10개)

## 목차

1. [문제 40: `4760488a-0f6...`](#40) — single-answer
2. [문제 41: `047973ff-6f7...`](#41) — single-answer
3. [문제 42: `9eb599d5-bbf...`](#42) — single-answer
4. [문제 43: `4d39f7f8-646...`](#43) — multiple-answer
5. [문제 44: `074d8dcd-dca...`](#44) — single-answer
6. [문제 45: `51d20b8e-e22...`](#45) — multiple-answer
7. [문제 46: `f902d75d-dba...`](#46) — multiple-answer
8. [문제 47: `3720ba2c-7aa...`](#47) — single-answer
9. [문제 48: `f45d84d2-ae7...`](#48) — single-answer
10. [문제 49: `66c959ea-332...`](#49) — single-answer

---

### 문제 40: `4760488a-0f6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4760488a-0f65-447c-82c5-9523ba4afda9` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[40] topology](images/test_0040.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213565_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213565_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Press down the tilt angle  of 3272533_4 by 10 degrees
- `C5`: Lift the tilt angle  of 3272533_4 by 10 degrees
- `C6`: Decrease transmission power for 3210426_2
- `C7`: Decrease A3 Offset threshold for 3210426_2
- `C8`: Press down the tilt angle of 3210426_2 by 2 degrees
- `C9`: Decrease transmission power for 3213565_1
- `C10`: Adjust the azimuth of 3210426_2 by 25 degrees
- `C11`: Increase transmission power for 3210426_2
- `C12`: Increase transmission power for 3213565_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210426_2
- `C14`: Increase A3 Offset threshold for 3210426_2
- `C15`: Adjust the azimuth of 3272533_4 by 50 degrees
- `C16`: Lift the tilt angle of 3210426_2 by 2 degrees
- `C17`: Check test server and transmission issues
- `C18`: Decrease A3 Offset threshold for 3213565_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210426_2
- `C20`: Add neighbor relationship between 3210426_2 and 3213565_1
- `C21`: Add neighbor relationship between 3272533_4 and 3213565_1
- `C22`: Increase A3 Offset threshold for 3213565_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.811 | MS1 | 121.4656605202 | 31.1446256829 | 412 | 504990 | -90.62 | 13.89 | 338.07 | 0.16 | 2.54 | 1595 |
| 2024-09-20 22:21:32.650 | MS1 | 121.4656684841 | 31.1446339987 | 412 | 504990 | -91.48 | 14.39 | 322.39 | 0.14 | 2.45 | 1574 |
| 2024-09-20 22:21:33.131 | MS1 | 121.4656682823 | 31.1446225413 | 412 | 504990 | -91.89 | 17.07 | 342.79 | 0.07 | 2.03 | 1582 |
| 2024-09-20 22:21:34.754 | MS1 | 121.4656711674 | 31.1446274263 | 412 | 504990 | -87.53 | 14.04 | 90.52 | 0.17 | 2.64 | 1573 |
| 2024-09-20 22:21:35.189 | MS1 | 121.4656639331 | 31.1446280690 | 412 | 504990 | -87.65 | 14.88 | 63.39 | 0.09 | 2.57 | 1564 |
| 2024-09-20 22:21:36.602 | MS1 | 121.4656627793 | 31.1446227533 | 412 | 504990 | -85.45 | 15.03 | 76.94 | 0.03 | 2.58 | 1581 |
| 2024-09-20 22:21:37.570 | MS1 | 121.4656596517 | 31.1446266505 | 412 | 504990 | -92.09 | 7.17 | 84.62 | 0.13 | 2.24 | 1581 |
| 2024-09-20 22:21:38.233 | MS1 | 121.4656778960 | 31.1446321204 | 412 | 504990 | -90.92 | 9.58 | 98.31 | 0.03 | 2.48 | 1579 |
| 2024-09-20 22:21:39.313 | MS1 | 121.4656748380 | 31.1446221412 | 412 | 504990 | -91.69 | 12.54 | 89.01 | 0.08 | 2.64 | 1596 |
| 2024-09-20 22:21:40.713 | MS1 | 121.4656724960 | 31.1446188307 | 412 | 504990 | -90.36 | 7.90 | 495.80 | 0.03 | 2.21 | 1599 |
| 2024-09-20 22:21:41.588 | MS1 | 121.4656679819 | 31.1446344525 | 412 | 504990 | -90.05 | 9.75 | 330.57 | 0.05 | 2.52 | 1594 |
| 2024-09-20 22:21:42.824 | MS1 | 121.4656771730 | 31.1446313981 | 412 | 504990 | -93.35 | 7.38 | 461.59 | 0.11 | 2.05 | 1571 |

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
| 3210426 | 2 | 121.4714760901 | 31.1514819717 | 241 | 0 | 9 | 28.8 | TDD | 412 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3213565 | 1 | 121.4717297049 | 31.1475591102 | 68 | 14 | 6 | 19.4 | TDD | 98 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3267746 | 3 | 121.4694190941 | 31.1548507836 | 220 | 9 | 6 | 38.2 | TDD | 101 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3272533 | 4 | 121.4742942088 | 31.1528270646 | 89 | 6 | 12 | 33.3 | TDD | 903 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.242 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.382 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.382 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.084 | NREventA3 | measId:2;ServCellPCI:708;Se... |
| 2024-09-20 22:21:38.324 | NRHandoverAttempt | SourcePCI:708;SourceNR-ARFC... |
| 2024-09-20 22:21:38.356 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.367 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.472 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.472 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213565 | 1 | 15.8432 | 12.5086 | -117.8944 | 5.6161 | 173.1306 | 0.0064 | 0.0077 |
| 2024_09_20 22:00 | 3210426 | 2 | 77.6114 | 79.6022 | -116.7116 | 9.3136 | 87.7771 | 0.0067 | 0.0059 |
| 2024_09_20 22:00 | 3267746 | 3 | 13.5995 | 15.5171 | -114.4528 | 5.8111 | 192.1925 | 0.0158 | 0.0041 |
| 2024_09_20 22:00 | 3272533 | 4 | 11.7886 | 10.3509 | -115.5568 | 10.5540 | 190.8643 | 0.0135 | 0.0050 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412051_707B9218 | 504990 | 412 | -88.6 | 504990 | 98 | -89.5 | 504990 | 903 | -101.7 | 504990 | 101 |
| MR_1774412051_AD0371BC | 504990 | 412 | -86.6 | 504990 | 98 | -90.2 | 504990 | 903 | -102.9 | 504990 | 101 |
| MR_1774412051_0CCA7F30 | 504990 | 412 | -88.3 | 504990 | 98 | -89.4 | 504990 | 903 | -102.4 | 504990 | 101 |
| MR_1774412051_C8CE8306 | 504990 | 412 | -88.0 | 504990 | 98 | -87.6 | 504990 | 903 | -102.3 | 504990 | 101 |
| MR_1774412051_31C733C0 | 504990 | 412 | -87.3 | 504990 | 98 | -88.2 | 504990 | 903 | -101.2 | 504990 | 101 |
| MR_1774412051_92DA526D | 504990 | 412 | -89.2 | 504990 | 98 | -87.2 | 504990 | 903 | -103.0 | 504990 | 101 |
| MR_1774412051_9172689C | 504990 | 412 | -88.5 | 504990 | 98 | -90.5 | 504990 | 903 | -101.0 | 504990 | 101 |
| MR_1774412051_C1922BCD | 504990 | 412 | -87.4 | 504990 | 98 | -90.0 | 504990 | 903 | -101.3 | 504990 | 101 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 41: `047973ff-6f7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `047973ff-6f7b-4760-88a6-acd32a89fc00` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[41] topology](images/test_0041.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3243855_3
- `C2`: Increase A3 Offset threshold for 3248898_2
- `C3`: Increase transmission power for 3248898_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248898_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243855_3
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243855_3
- `C8`: Add neighbor relationship between 3243855_3 and 3248898_2
- `C9`: Add neighbor relationship between 3211703_1 and 3248898_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248898_2
- `C11`: Press down the tilt angle  of 3248898_2 by 8 degrees
- `C12`: Decrease A3 Offset threshold for 3248898_2
- `C13`: Check test server and transmission issues
- `C14`: Lift the tilt angle of 3243855_3 by 3 degrees
- `C15`: Decrease transmission power for 3243855_3
- `C16`: Adjust the azimuth of 3243855_3 by 50 degrees
- `C17`: Press down the tilt angle of 3243855_3 by 3 degrees
- `C18`: Increase transmission power for 3243855_3
- `C19`: Decrease A3 Offset threshold for 3243855_3
- `C20`: Adjust the azimuth of 3248898_2 by 50 degrees
- `C21`: Lift the tilt angle  of 3248898_2 by 8 degrees
- `C22`: Decrease transmission power for 3248898_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.452 | MS1 | 121.4656704716 | 31.1446286380 | 646 | 504990 | -81.77 | 15.76 | 471.62 | 0.18 | 2.65 | 1575 |
| 2024-09-20 22:21:32.640 | MS1 | 121.4656659253 | 31.1446323264 | 646 | 504990 | -78.43 | 12.37 | 571.27 | 0.01 | 2.16 | 1579 |
| 2024-09-20 22:21:33.816 | MS1 | 121.4656636744 | 31.1446293811 | 646 | 504990 | -81.39 | 14.90 | 535.97 | 0.17 | 2.58 | 1583 |
| 2024-09-20 22:21:34.304 | MS1 | 121.4656776801 | 31.1446367835 | 646 | 504990 | -84.89 | -1.23 | 38.46 | 0.09 | 1.33 | 1562 |
| 2024-09-20 22:21:35.273 | MS1 | 121.4656620209 | 31.1446285612 | 646 | 504990 | -92.08 | -1.09 | 63.34 | 0.03 | 1.41 | 1572 |
| 2024-09-20 22:21:36.688 | MS1 | 121.4656689180 | 31.1446344790 | 646 | 504990 | -89.47 | -2.15 | 60.63 | 0.12 | 1.37 | 1590 |
| 2024-09-20 22:21:37.411 | MS1 | 121.4656692405 | 31.1446187184 | 646 | 504990 | -86.86 | -1.97 | 65.27 | 0.18 | 1.47 | 1590 |
| 2024-09-20 22:21:38.121 | MS1 | 121.4656624138 | 31.1446247352 | 646 | 504990 | -89.69 | -2.12 | 67.55 | 0.13 | 1.07 | 1596 |
| 2024-09-20 22:21:39.551 | MS1 | 121.4656605704 | 31.1446239919 | 331 | 504990 | -83.50 | 16.85 | 187.86 | 0.02 | 1.34 | 1585 |
| 2024-09-20 22:21:40.402 | MS1 | 121.4656622701 | 31.1446182780 | 331 | 504990 | -80.47 | 17.59 | 338.50 | 0.06 | 2.18 | 1600 |
| 2024-09-20 22:21:41.365 | MS1 | 121.4656704201 | 31.1446192968 | 331 | 504990 | -76.23 | 17.70 | 351.43 | 0.03 | 2.22 | 1575 |
| 2024-09-20 22:21:42.508 | MS1 | 121.4656628747 | 31.1446259294 | 331 | 504990 | -75.21 | 14.41 | 503.88 | 0.03 | 2.14 | 1588 |

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
| 3211703 | 1 | 121.4661629801 | 31.1478972311 | 192 | 7 | 3 | 16.6 | TDD | 305 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3243855 | 3 | 121.4644890734 | 31.1527596098 | 289 | 1 | 3 | 35.4 | TDD | 646 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3248898 | 2 | 121.4717826938 | 31.1553502270 | 37 | 6 | 11 | 40.0 | TDD | 331 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3267326 | 4 | 121.4739576370 | 31.1538072514 | 120 | 7 | 2 | 18.5 | TDD | 491 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.510 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.526 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.664 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.664 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.311 | NREventA3 | measId:2;ServCellPCI:461;Se... |
| 2024-09-20 22:21:38.551 | NRHandoverAttempt | SourcePCI:461;SourceNR-ARFC... |
| 2024-09-20 22:21:38.601 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.613 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.719 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.719 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211703 | 1 | 13.9386 | 13.8256 | -115.7391 | 9.0145 | 189.3524 | 0.0145 | 0.0101 |
| 2024_09_20 22:00 | 3248898 | 2 | 19.8163 | 17.6822 | -115.0719 | 8.9668 | 138.0733 | 0.0137 | 0.0191 |
| 2024_09_20 22:00 | 3243855 | 3 | 12.9402 | 7.6001 | -117.7274 | 16.2949 | 152.0719 | 0.0026 | 0.1675 |
| 2024_09_20 22:00 | 3267326 | 4 | 5.8737 | 17.3506 | -115.1390 | 15.5509 | 168.5803 | 0.0168 | 0.0093 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414446_B80F4980 | 504990 | 331 | -79.8 | 504990 | 646 | -83.7 | 504990 | 305 | -81.7 | 504990 | 491 |
| MR_1774414446_A9DBF153 | 504990 | 646 | -85.9 | 504990 | 331 | -82.4 | 504990 | 305 | -82.9 | 504990 | 491 |
| MR_1774414446_332B418C | 504990 | 331 | -79.5 | 504990 | 646 | -85.7 | 504990 | 305 | -83.1 | 504990 | 491 |
| MR_1774414446_D630B94E | 504990 | 646 | -83.7 | 504990 | 331 | -80.5 | 504990 | 305 | -81.5 | 504990 | 491 |
| MR_1774414446_2D490F9D | 504990 | 646 | -84.8 | 504990 | 331 | -79.3 | 504990 | 305 | -82.5 | 504990 | 491 |
| MR_1774414446_2A71F526 | 504990 | 646 | -84.3 | 504990 | 331 | -80.9 | 504990 | 305 | -82.0 | 504990 | 491 |
| MR_1774414446_8187D06F | 504990 | 646 | -86.5 | 504990 | 331 | -79.6 | 504990 | 305 | -84.9 | 504990 | 491 |
| MR_1774414446_D1949348 | 504990 | 646 | -85.1 | 504990 | 331 | -78.6 | 504990 | 305 | -84.3 | 504990 | 491 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 42: `9eb599d5-bbf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9eb599d5-bbfb-4d59-81e2-c435b4486894` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[42] topology](images/test_0042.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3237944_3
- `C2`: Decrease A3 Offset threshold for 3212003_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237944_3
- `C4`: Decrease transmission power for 3237944_3
- `C5`: Decrease A3 Offset threshold for 3237944_3
- `C6`: Check test server and transmission issues
- `C7`: Increase transmission power for 3237944_3
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Press down the tilt angle  of 3237944_3 by 8 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237944_3
- `C11`: Adjust the azimuth of 3212003_4 by 38 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212003_4
- `C13`: Decrease transmission power for 3212003_4
- `C14`: Add neighbor relationship between 3212003_4 and 3237944_3
- `C15`: Add neighbor relationship between 3265746_2 and 3237944_3
- `C16`: Press down the tilt angle of 3212003_4 by 5 degrees
- `C17`: Lift the tilt angle of 3212003_4 by 5 degrees
- `C18`: Lift the tilt angle  of 3237944_3 by 8 degrees
- `C19`: Increase transmission power for 3212003_4
- `C20`: Adjust the azimuth of 3237944_3 by 50 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212003_4
- `C22`: Increase A3 Offset threshold for 3212003_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.601 | MS1 | 121.4656710248 | 31.1446235306 | 94 | 504990 | -90.74 | 14.30 | 443.85 | 0.03 | 2.95 | 1598 |
| 2024-09-20 22:21:32.466 | MS1 | 121.4656683294 | 31.1446270526 | 94 | 504990 | -90.39 | 13.39 | 482.88 | 0.02 | 2.54 | 1597 |
| 2024-09-20 22:21:33.676 | MS1 | 121.4656667159 | 31.1446312981 | 94 | 504990 | -86.48 | 13.56 | 515.75 | 0.11 | 2.80 | 1560 |
| 2024-09-20 22:21:34.987 | MS1 | 121.4656769304 | 31.1446269630 | 94 | 504990 | -90.35 | 15.24 | 86.17 | 0.60 | 2.89 | 683 |
| 2024-09-20 22:21:35.409 | MS1 | 121.4656666229 | 31.1446185340 | 94 | 504990 | -86.54 | 13.33 | 86.82 | 0.69 | 2.23 | 607 |
| 2024-09-20 22:21:36.494 | MS1 | 121.4656604229 | 31.1446246719 | 94 | 504990 | -91.64 | 17.78 | 102.13 | 0.54 | 2.34 | 524 |
| 2024-09-20 22:21:37.646 | MS1 | 121.4656628785 | 31.1446220548 | 94 | 504990 | -92.71 | 9.80 | 65.15 | 0.54 | 2.12 | 652 |
| 2024-09-20 22:21:38.873 | MS1 | 121.4656620505 | 31.1446195380 | 94 | 504990 | -93.99 | 11.21 | 64.01 | 0.52 | 2.73 | 689 |
| 2024-09-20 22:21:39.966 | MS1 | 121.4656600706 | 31.1446245486 | 94 | 504990 | -93.25 | 11.05 | 76.67 | 0.67 | 2.23 | 531 |
| 2024-09-20 22:21:40.997 | MS1 | 121.4656755084 | 31.1446195935 | 94 | 504990 | -89.11 | 12.69 | 297.29 | 0.15 | 2.43 | 1573 |
| 2024-09-20 22:21:41.946 | MS1 | 121.4656600410 | 31.1446249273 | 94 | 504990 | -92.64 | 8.95 | 440.64 | 0.07 | 2.37 | 1592 |
| 2024-09-20 22:21:42.519 | MS1 | 121.4656601033 | 31.1446311213 | 94 | 504990 | -91.97 | 9.79 | 337.46 | 0.15 | 2.59 | 1565 |

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
| 3212003 | 4 | 121.4758861843 | 31.1482884308 | 209 | 3 | 4 | 31.5 | TDD | 94 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3237944 | 3 | 121.4674030815 | 31.1525524059 | 18 | 7 | 1 | 15.2 | TDD | 411 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3240684 | 1 | 121.4670058694 | 31.1452707250 | 176 | 15 | 1 | 49.5 | TDD | 728 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3265746 | 2 | 121.4724446386 | 31.1545889362 | 318 | 13 | 2 | 24.5 | TDD | 842 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.262 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.286 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.422 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.422 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.086 | NREventA3 | measId:2;ServCellPCI:892;Se... |
| 2024-09-20 22:21:38.326 | NRHandoverAttempt | SourcePCI:892;SourceNR-ARFC... |
| 2024-09-20 22:21:38.363 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.378 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.485 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.485 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240684 | 1 | 14.5749 | 11.1287 | -115.2478 | 5.9494 | 126.4765 | 0.0063 | 0.0062 |
| 2024_09_20 22:00 | 3265746 | 2 | 13.9257 | 6.5427 | -116.6346 | 13.8195 | 161.2251 | 0.0057 | 0.0190 |
| 2024_09_20 22:00 | 3237944 | 3 | 11.6187 | 19.3172 | -114.0404 | 19.6636 | 88.8692 | 0.0105 | 0.0141 |
| 2024_09_20 22:00 | 3212003 | 4 | 11.7472 | 12.4098 | -115.9339 | 10.5662 | 143.9286 | 0.0094 | 0.0034 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413630_2A148B8D | 504990 | 94 | -89.0 | 504990 | 411 | -96.7 | 504990 | 842 | -101.0 | 504990 | 728 |
| MR_1774413630_D0587B17 | 504990 | 94 | -92.1 | 504990 | 411 | -99.1 | 504990 | 842 | -100.3 | 504990 | 728 |
| MR_1774413630_A406AF4D | 504990 | 94 | -89.2 | 504990 | 411 | -97.2 | 504990 | 842 | -99.1 | 504990 | 728 |
| MR_1774413630_3442A0A6 | 504990 | 94 | -89.8 | 504990 | 411 | -99.5 | 504990 | 842 | -98.2 | 504990 | 728 |
| MR_1774413630_AF732BA4 | 504990 | 94 | -88.5 | 504990 | 411 | -98.0 | 504990 | 842 | -100.6 | 504990 | 728 |
| MR_1774413630_D5A942FF | 504990 | 94 | -89.1 | 504990 | 411 | -97.4 | 504990 | 842 | -101.9 | 504990 | 728 |
| MR_1774413630_3C8EC7CD | 504990 | 94 | -89.9 | 504990 | 411 | -97.0 | 504990 | 842 | -98.7 | 504990 | 728 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 43: `4d39f7f8-646...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4d39f7f8-6467-4dce-bc31-c2292e7407a6` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[43] topology](images/test_0043.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3247816_1
- `C2`: Increase A3 Offset threshold for 3247816_1
- `C3`: Lift the tilt angle  of 3247816_1 by 6 degrees
- `C4`: Check test server and transmission issues
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247816_1
- `C6`: Lift the tilt angle of 3278949_4 by 5 degrees
- `C7`: Adjust the azimuth of 3247816_1 by 23 degrees
- `C8`: Adjust the azimuth of 3278949_4 by 29 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278949_4
- `C10`: Increase transmission power for 3278949_4
- `C11`: Decrease transmission power for 3278949_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278949_4
- `C13`: Increase A3 Offset threshold for 3278949_4
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease transmission power for 3247816_1
- `C16`: Press down the tilt angle of 3278949_4 by 5 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247816_1
- `C18`: Add neighbor relationship between 3278949_4 and 3247816_1
- `C19`: Decrease A3 Offset threshold for 3278949_4
- `C20`: Add neighbor relationship between 3258775_2 and 3247816_1
- `C21`: Press down the tilt angle  of 3247816_1 by 6 degrees
- `C22`: Increase transmission power for 3247816_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.170 | MS1 | 121.4656751665 | 31.1446210592 | 686 | 504990 | -80.72 | 17.08 | 318.06 | 0.18 | 2.84 | 1574 |
| 2024-09-20 22:21:32.740 | MS1 | 121.4656669757 | 31.1446207492 | 686 | 504990 | -80.98 | 12.00 | 574.84 | 0.11 | 2.84 | 1586 |
| 2024-09-20 22:21:33.374 | MS1 | 121.4656742893 | 31.1446216093 | 686 | 504990 | -76.51 | 15.39 | 337.63 | 0.05 | 2.12 | 1597 |
| 2024-09-20 22:21:34.346 | MS1 | 121.4656616434 | 31.1446211511 | 686 | 504990 | -92.47 | 1.01 | 57.23 | 0.03 | 1.47 | 1560 |
| 2024-09-20 22:21:35.243 | MS1 | 121.4656648031 | 31.1446318887 | 686 | 504990 | -91.50 | 0.34 | 38.21 | 0.18 | 1.25 | 1579 |
| 2024-09-20 22:21:36.909 | MS1 | 121.4656671534 | 31.1446197628 | 686 | 504990 | -91.28 | 1.74 | 46.76 | 0.12 | 1.28 | 1582 |
| 2024-09-20 22:21:37.697 | MS1 | 121.4656583436 | 31.1446201335 | 686 | 504990 | -85.55 | 2.03 | 71.88 | 0.03 | 1.18 | 1573 |
| 2024-09-20 22:21:38.768 | MS1 | 121.4656744404 | 31.1446274478 | 686 | 504990 | -91.83 | 0.16 | 78.55 | 0.09 | 1.17 | 1564 |
| 2024-09-20 22:21:39.513 | MS1 | 121.4656635917 | 31.1446262458 | 686 | 504990 | -92.66 | 0.32 | 79.74 | 0.09 | 1.47 | 1580 |
| 2024-09-20 22:21:40.192 | MS1 | 121.4656658092 | 31.1446266047 | 686 | 504990 | -81.67 | 17.33 | 508.43 | 0.16 | 2.13 | 1563 |
| 2024-09-20 22:21:41.505 | MS1 | 121.4656754684 | 31.1446355084 | 686 | 504990 | -80.73 | 13.38 | 401.60 | 0.17 | 2.59 | 1572 |
| 2024-09-20 22:21:42.436 | MS1 | 121.4656594451 | 31.1446189135 | 686 | 504990 | -77.33 | 12.64 | 385.56 | 0.17 | 2.41 | 1569 |

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
| 3212265 | 3 | 121.4669869676 | 31.1481428182 | 131 | 10 | 5 | 19.0 | TDD | 716 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3247816 | 1 | 121.4750689081 | 31.1527178423 | 202 | 4 | 6 | 42.5 | TDD | 112 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3258775 | 2 | 121.4718269454 | 31.1512217733 | 147 | 4 | 1 | 26.5 | TDD | 155 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3278949 | 4 | 121.4758504076 | 31.1513494930 | 203 | 4 | 0 | 24.2 | TDD | 686 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.347 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.368 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.495 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.495 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247816 | 1 | 6.8601 | 16.0920 | -115.0141 | 5.7788 | 93.6044 | 0.0183 | 0.0039 |
| 2024_09_20 22:00 | 3258775 | 2 | 17.4630 | 15.8686 | -116.9732 | 19.0089 | 82.2184 | 0.0036 | 0.0180 |
| 2024_09_20 22:00 | 3212265 | 3 | 9.5713 | 12.0358 | -115.4575 | 7.7005 | 152.9650 | 0.0077 | 0.0157 |
| 2024_09_20 22:00 | 3278949 | 4 | 13.3464 | 14.2905 | -109.5213 | 15.9226 | 119.0160 | 0.0187 | 0.0067 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414912_542420DE | 504990 | 686 | -91.5 | 504990 | 112 | -90.3 | 504990 | 155 | -97.4 | 504990 | 716 |
| MR_1774414912_38035863 | 504990 | 112 | -93.1 | 504990 | 686 | -91.9 | 504990 | 155 | -94.3 | 504990 | 716 |
| MR_1774414912_296FF582 | 504990 | 112 | -90.6 | 504990 | 686 | -93.1 | 504990 | 155 | -96.7 | 504990 | 716 |
| MR_1774414912_A4A3835E | 504990 | 686 | -93.7 | 504990 | 112 | -91.4 | 504990 | 155 | -95.8 | 504990 | 716 |
| MR_1774414912_E5CFF27C | 504990 | 686 | -92.9 | 504990 | 112 | -93.7 | 504990 | 155 | -96.9 | 504990 | 716 |
| MR_1774414912_616CEA0E | 504990 | 112 | -91.0 | 504990 | 686 | -93.4 | 504990 | 155 | -94.9 | 504990 | 716 |
| MR_1774414912_CF064A25 | 504990 | 686 | -90.5 | 504990 | 112 | -91.5 | 504990 | 155 | -95.0 | 504990 | 716 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 44: `074d8dcd-dca...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `074d8dcd-dca7-4102-babd-4b0ba4c5813d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[44] topology](images/test_0044.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3231124_1
- `C2`: Lift the tilt angle  of 3237075_2 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231124_1
- `C4`: Add neighbor relationship between 3231124_1 and 3237075_2
- `C5`: Decrease A3 Offset threshold for 3237075_2
- `C6`: Press down the tilt angle  of 3237075_2 by 10 degrees
- `C7`: Decrease transmission power for 3237075_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237075_2
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Increase A3 Offset threshold for 3231124_1
- `C11`: Adjust the azimuth of 3237075_2 by 50 degrees
- `C12`: Lift the tilt angle of 3231124_1 by 5 degrees
- `C13`: Decrease A3 Offset threshold for 3231124_1
- `C14`: Add neighbor relationship between 3234053_4 and 3237075_2
- `C15`: Check test server and transmission issues
- `C16`: Decrease transmission power for 3231124_1
- `C17`: Increase transmission power for 3237075_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231124_1
- `C19`: Adjust the azimuth of 3231124_1 by 24 degrees
- `C20`: Press down the tilt angle of 3231124_1 by 5 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237075_2
- `C22`: Increase A3 Offset threshold for 3237075_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.427 | MS1 | 121.4656613395 | 31.1446273079 | 94 | 504990 | -90.57 | 16.76 | 517.45 | 0.12 | 2.03 | 1573 |
| 2024-09-20 22:21:32.330 | MS1 | 121.4656730094 | 31.1446358361 | 94 | 504990 | -90.31 | 16.76 | 454.48 | 0.06 | 2.18 | 1596 |
| 2024-09-20 22:21:33.174 | MS1 | 121.4656778479 | 31.1446307757 | 94 | 504990 | -88.19 | 16.21 | 465.25 | 0.19 | 2.53 | 1581 |
| 2024-09-20 22:21:34.456 | MS1 | 121.4656766523 | 31.1446375657 | 94 | 504990 | -86.80 | 16.93 | 77.13 | 0.68 | 2.71 | 510 |
| 2024-09-20 22:21:35.725 | MS1 | 121.4656686455 | 31.1446291734 | 94 | 504990 | -90.96 | 16.41 | 65.55 | 0.52 | 2.97 | 542 |
| 2024-09-20 22:21:36.180 | MS1 | 121.4656589411 | 31.1446237206 | 94 | 504990 | -90.32 | 15.38 | 60.29 | 0.64 | 2.53 | 579 |
| 2024-09-20 22:21:37.404 | MS1 | 121.4656619381 | 31.1446291525 | 94 | 504990 | -92.66 | 10.74 | 76.25 | 0.69 | 2.99 | 643 |
| 2024-09-20 22:21:38.238 | MS1 | 121.4656721356 | 31.1446320172 | 94 | 504990 | -91.69 | 11.62 | 53.98 | 0.65 | 2.31 | 526 |
| 2024-09-20 22:21:39.423 | MS1 | 121.4656625356 | 31.1446352640 | 94 | 504990 | -89.05 | 12.86 | 55.50 | 0.69 | 2.64 | 630 |
| 2024-09-20 22:21:40.701 | MS1 | 121.4656773841 | 31.1446293954 | 94 | 504990 | -92.44 | 11.56 | 433.05 | 0.16 | 2.52 | 1589 |
| 2024-09-20 22:21:41.955 | MS1 | 121.4656734490 | 31.1446196507 | 94 | 504990 | -92.85 | 11.15 | 501.02 | 0.02 | 2.26 | 1579 |
| 2024-09-20 22:21:42.482 | MS1 | 121.4656736804 | 31.1446292089 | 94 | 504990 | -93.19 | 10.70 | 490.52 | 0.16 | 2.71 | 1573 |

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
| 3231124 | 1 | 121.4750926330 | 31.1457898588 | 286 | 3 | 9 | 29.3 | TDD | 94 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3234053 | 4 | 121.4662029868 | 31.1469613810 | 64 | 1 | 12 | 24.7 | TDD | 462 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3237075 | 2 | 121.4720224365 | 31.1531558960 | 154 | 12 | 12 | 19.8 | TDD | 410 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3261580 | 3 | 121.4741600047 | 31.1513393292 | 280 | 2 | 12 | 31.8 | TDD | 820 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.834 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.858 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.998 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.998 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.664 | NREventA3 | measId:2;ServCellPCI:484;Se... |
| 2024-09-20 22:21:37.904 | NRHandoverAttempt | SourcePCI:484;SourceNR-ARFC... |
| 2024-09-20 22:21:37.949 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.961 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.073 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.073 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231124 | 1 | 8.5174 | 12.7123 | -116.8715 | 6.1367 | 110.4477 | 0.0139 | 0.0196 |
| 2024_09_20 22:00 | 3237075 | 2 | 13.7212 | 12.0228 | -117.4395 | 17.6833 | 113.6384 | 0.0179 | 0.0135 |
| 2024_09_20 22:00 | 3261580 | 3 | 9.3319 | 16.3404 | -116.2561 | 10.4477 | 89.9559 | 0.0013 | 0.0174 |
| 2024_09_20 22:00 | 3234053 | 4 | 5.3046 | 16.4287 | -116.3248 | 13.4323 | 196.0312 | 0.0135 | 0.0178 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416055_A05BED09 | 504990 | 94 | -88.2 | 504990 | 410 | -88.3 | 504990 | 462 | -97.9 | 504990 | 820 |
| MR_1774416055_DBF0764D | 504990 | 94 | -87.5 | 504990 | 410 | -90.8 | 504990 | 462 | -100.6 | 504990 | 820 |
| MR_1774416055_2E1EF06D | 504990 | 94 | -86.7 | 504990 | 410 | -90.8 | 504990 | 462 | -101.3 | 504990 | 820 |
| MR_1774416055_D48E1309 | 504990 | 94 | -88.6 | 504990 | 410 | -89.4 | 504990 | 462 | -99.7 | 504990 | 820 |
| MR_1774416055_F7988A7E | 504990 | 94 | -85.9 | 504990 | 410 | -90.2 | 504990 | 462 | -98.7 | 504990 | 820 |
| MR_1774416055_A784A267 | 504990 | 94 | -86.4 | 504990 | 410 | -88.2 | 504990 | 462 | -101.3 | 504990 | 820 |
| MR_1774416055_35C73D61 | 504990 | 94 | -87.4 | 504990 | 410 | -91.0 | 504990 | 462 | -98.2 | 504990 | 820 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 45: `51d20b8e-e22...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `51d20b8e-e226-4601-b2a5-7269a68e8285` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[45] topology](images/test_0045.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3222568_5 by 47 degrees
- `C2`: Increase transmission power for 3235777_3
- `C3`: Adjust the azimuth of 3235777_3 by 14 degrees
- `C4`: Check test server and transmission issues
- `C5`: Increase transmission power for 3222568_5
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222568_5
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Add neighbor relationship between 3239330_2 and 3222568_5
- `C9`: Increase A3 Offset threshold for 3235777_3
- `C10`: Lift the tilt angle of 3235777_3 by 2 degrees
- `C11`: Lift the tilt angle  of 3222568_5 by 6 degrees
- `C12`: Decrease transmission power for 3235777_3
- `C13`: Press down the tilt angle  of 3222568_5 by 6 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235777_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222568_5
- `C16`: Add neighbor relationship between 3235777_3 and 3222568_5
- `C17`: Increase A3 Offset threshold for 3222568_5
- `C18`: Decrease A3 Offset threshold for 3222568_5
- `C19`: Press down the tilt angle of 3235777_3 by 2 degrees
- `C20`: Decrease A3 Offset threshold for 3235777_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235777_3
- `C22`: Decrease transmission power for 3222568_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.725 | MS1 | 121.4656618845 | 31.1446373756 | 465 | 504990 | -75.84 | 14.19 | 354.50 | 0.18 | 2.66 | 1577 |
| 2024-09-20 22:21:32.944 | MS1 | 121.4656711483 | 31.1446229693 | 465 | 504990 | -79.39 | 17.33 | 420.46 | 0.17 | 2.04 | 1571 |
| 2024-09-20 22:21:33.506 | MS1 | 121.4656721719 | 31.1446244122 | 465 | 504990 | -80.09 | 16.45 | 572.29 | 0.12 | 2.78 | 1576 |
| 2024-09-20 22:21:34.822 | MS1 | 121.4656713393 | 31.1446194480 | 178 | 504990 | -85.45 | 1.73 | 88.59 | 0.01 | 1.46 | 1562 |
| 2024-09-20 22:21:35.275 | MS1 | 121.4656718089 | 31.1446268756 | 178 | 504990 | -86.21 | 1.77 | 67.20 | 0.08 | 1.21 | 1581 |
| 2024-09-20 22:21:36.807 | MS1 | 121.4656615798 | 31.1446229082 | 465 | 504990 | -82.47 | 2.66 | 78.29 | 0.17 | 1.43 | 1599 |
| 2024-09-20 22:21:37.535 | MS1 | 121.4656712570 | 31.1446284890 | 465 | 504990 | -81.63 | 2.36 | 75.04 | 0.17 | 1.42 | 1591 |
| 2024-09-20 22:21:38.628 | MS1 | 121.4656737496 | 31.1446250688 | 178 | 504990 | -88.14 | 2.30 | 47.12 | 0.14 | 1.02 | 1560 |
| 2024-09-20 22:21:39.257 | MS1 | 121.4656734541 | 31.1446242505 | 178 | 504990 | -82.76 | 3.01 | 60.99 | 0.14 | 1.50 | 1570 |
| 2024-09-20 22:21:40.490 | MS1 | 121.4656773900 | 31.1446358902 | 178 | 504990 | -82.30 | 14.52 | 344.45 | 0.12 | 2.31 | 1561 |
| 2024-09-20 22:21:41.152 | MS1 | 121.4656746947 | 31.1446204731 | 178 | 504990 | -84.06 | 15.29 | 558.52 | 0.04 | 2.26 | 1587 |
| 2024-09-20 22:21:42.466 | MS1 | 121.4656685105 | 31.1446257589 | 178 | 504990 | -79.32 | 13.25 | 451.17 | 0.07 | 2.69 | 1567 |

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
| 3222568 | 5 | 121.4700692708 | 31.1444552870 | 226 | 3 | 0 | 19.0 | TDD | 153 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3235777 | 3 | 121.4754474941 | 31.1535875902 | 209 | 1 | 8 | 34.1 | TDD | 465 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3239330 | 2 | 121.4734050812 | 31.1473669397 | 68 | 12 | 5 | 48.7 | TDD | 621 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3263527 | 1 | 121.4696440057 | 31.1487739511 | 137 | 9 | 11 | 26.8 | TDD | 800 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3275700 | 4 | 121.4710179790 | 31.1500729415 | 348 | 3 | 1 | 42.0 | TDD | 178 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.376 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.486 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.486 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.203 | NREventA3 | measId:2;ServCellPCI:464;Se... |
| 2024-09-20 22:21:34.443 | NRHandoverAttempt | SourcePCI:464;SourceNR-ARFC... |
| 2024-09-20 22:21:34.473 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.488 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.632 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.632 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.203 | NREventA3 | measId:2;ServCellPCI:428;Se... |
| 2024-09-20 22:21:36.443 | NRHandoverAttempt | SourcePCI:428;SourceNR-ARFC... |
| 2024-09-20 22:21:36.493 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.504 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.622 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.622 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.203 | NREventA3 | measId:2;ServCellPCI:464;Se... |
| 2024-09-20 22:21:38.443 | NRHandoverAttempt | SourcePCI:464;SourceNR-ARFC... |
| 2024-09-20 22:21:38.485 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.496 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.614 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.614 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263527 | 1 | 7.7434 | 18.1229 | -114.2695 | 15.1891 | 96.5310 | 0.0050 | 0.0045 |
| 2024_09_20 22:00 | 3239330 | 2 | 14.1885 | 19.8789 | -117.2102 | 10.1937 | 181.2490 | 0.0101 | 0.0170 |
| 2024_09_20 22:00 | 3235777 | 3 | 8.9631 | 5.3572 | -117.8248 | 13.4633 | 130.5193 | 0.0101 | 0.0118 |
| 2024_09_20 22:00 | 3275700 | 4 | 14.6450 | 15.3931 | -117.3856 | 17.4843 | 152.9935 | 0.0038 | 0.0110 |
| 2024_09_20 22:00 | 3222568 | 5 | 11.5050 | 10.4773 | -117.5205 | 6.3101 | 83.7702 | 0.0107 | 0.0052 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415657_4BB9D42A | 504990 | 178 | -86.4 | 504990 | 465 | -85.8 | 504990 | 153 | -87.4 | 504990 | 621 |
| MR_1774415657_A6656A9A | 504990 | 178 | -84.8 | 504990 | 465 | -83.3 | 504990 | 153 | -86.3 | 504990 | 621 |
| MR_1774415657_4B4BA5ED | 504990 | 178 | -85.5 | 504990 | 465 | -85.0 | 504990 | 153 | -84.7 | 504990 | 621 |
| MR_1774415657_0FB1337D | 504990 | 178 | -86.1 | 504990 | 465 | -85.0 | 504990 | 153 | -86.8 | 504990 | 621 |
| MR_1774415657_76A7EC3A | 504990 | 178 | -84.4 | 504990 | 465 | -83.6 | 504990 | 153 | -87.5 | 504990 | 621 |
| MR_1774415657_05A6761E | 504990 | 178 | -87.0 | 504990 | 465 | -84.2 | 504990 | 153 | -88.2 | 504990 | 621 |
| MR_1774415657_EED344C7 | 504990 | 178 | -84.3 | 504990 | 465 | -83.1 | 504990 | 153 | -84.4 | 504990 | 621 |
| MR_1774415657_7776F619 | 504990 | 465 | -86.7 | 504990 | 178 | -82.2 | 504990 | 153 | -86.9 | 504990 | 621 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 46: `f902d75d-dba...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f902d75d-dbac-46ed-8cea-e81c1d1e213f` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[46] topology](images/test_0046.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3218159_2 by 3 degrees
- `C2`: Adjust the azimuth of 3259317_4 by 35 degrees
- `C3`: Check test server and transmission issues
- `C4`: Lift the tilt angle of 3259317_4 by 5 degrees
- `C5`: Increase A3 Offset threshold for 3259317_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218159_2
- `C8`: Increase A3 Offset threshold for 3218159_2
- `C9`: Increase transmission power for 3218159_2
- `C10`: Decrease A3 Offset threshold for 3259317_4
- `C11`: Decrease transmission power for 3259317_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259317_4
- `C13`: Add neighbor relationship between 3213518_3 and 3218159_2
- `C14`: Adjust the azimuth of 3218159_2 by 8 degrees
- `C15`: Decrease A3 Offset threshold for 3218159_2
- `C16`: Add neighbor relationship between 3259317_4 and 3218159_2
- `C17`: Increase transmission power for 3259317_4
- `C18`: Lift the tilt angle  of 3218159_2 by 3 degrees
- `C19`: Press down the tilt angle of 3259317_4 by 5 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218159_2
- `C21`: Decrease transmission power for 3218159_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259317_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.613 | MS1 | 121.4656631740 | 31.1446361014 | 391 | 504990 | -75.12 | 13.02 | 414.45 | 0.16 | 2.63 | 1573 |
| 2024-09-20 22:21:32.794 | MS1 | 121.4656759896 | 31.1446253230 | 391 | 504990 | -83.70 | 17.04 | 515.69 | 0.07 | 2.79 | 1591 |
| 2024-09-20 22:21:33.234 | MS1 | 121.4656721932 | 31.1446351752 | 391 | 504990 | -77.56 | 17.71 | 478.10 | 0.02 | 2.88 | 1578 |
| 2024-09-20 22:21:34.117 | MS1 | 121.4656655499 | 31.1446238887 | 391 | 504990 | -89.80 | 0.71 | 46.25 | 0.00 | 1.10 | 1594 |
| 2024-09-20 22:21:35.249 | MS1 | 121.4656705861 | 31.1446290818 | 391 | 504990 | -90.33 | 1.14 | 73.89 | 0.19 | 1.28 | 1587 |
| 2024-09-20 22:21:36.160 | MS1 | 121.4656769463 | 31.1446269117 | 391 | 504990 | -94.32 | 2.18 | 38.48 | 0.08 | 1.25 | 1563 |
| 2024-09-20 22:21:37.426 | MS1 | 121.4656640383 | 31.1446231268 | 391 | 504990 | -90.96 | 0.11 | 49.11 | 0.09 | 1.07 | 1571 |
| 2024-09-20 22:21:38.388 | MS1 | 121.4656694235 | 31.1446215138 | 391 | 504990 | -89.86 | 0.55 | 34.47 | 0.04 | 1.35 | 1581 |
| 2024-09-20 22:21:39.116 | MS1 | 121.4656768378 | 31.1446361180 | 391 | 504990 | -88.61 | 0.25 | 77.31 | 0.00 | 1.15 | 1585 |
| 2024-09-20 22:21:40.698 | MS1 | 121.4656616718 | 31.1446351852 | 391 | 504990 | -83.15 | 14.63 | 429.17 | 0.14 | 2.68 | 1596 |
| 2024-09-20 22:21:41.151 | MS1 | 121.4656600211 | 31.1446223334 | 391 | 504990 | -81.81 | 13.01 | 405.42 | 0.03 | 2.23 | 1573 |
| 2024-09-20 22:21:42.117 | MS1 | 121.4656624705 | 31.1446318288 | 391 | 504990 | -81.09 | 12.07 | 345.70 | 0.06 | 2.41 | 1576 |

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
| 3213518 | 3 | 121.4652399708 | 31.1544347554 | 261 | 0 | 1 | 29.3 | TDD | 844 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3218159 | 2 | 121.4751697311 | 31.1448183402 | 261 | 0 | 2 | 42.0 | TDD | 147 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3240179 | 1 | 121.4733949900 | 31.1465952521 | 327 | 14 | 5 | 40.0 | TDD | 313 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3259317 | 4 | 121.4753677961 | 31.1504634869 | 270 | 3 | 0 | 45.3 | TDD | 391 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.450 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.467 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.595 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.595 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240179 | 1 | 5.6914 | 7.4646 | -114.5553 | 11.9287 | 125.8967 | 0.0004 | 0.0151 |
| 2024_09_20 22:00 | 3218159 | 2 | 17.4217 | 6.6583 | -117.5095 | 19.7062 | 118.1743 | 0.0179 | 0.0068 |
| 2024_09_20 22:00 | 3213518 | 3 | 15.4849 | 19.2959 | -117.4464 | 16.5495 | 170.0200 | 0.0148 | 0.0082 |
| 2024_09_20 22:00 | 3259317 | 4 | 10.8271 | 12.1352 | -108.2739 | 14.7473 | 90.3247 | 0.0033 | 0.0062 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414735_745187BC | 504990 | 391 | -89.9 | 504990 | 147 | -89.7 | 504990 | 844 | -90.9 | 504990 | 313 |
| MR_1774414735_66E79E0D | 504990 | 391 | -88.0 | 504990 | 147 | -89.8 | 504990 | 844 | -92.2 | 504990 | 313 |
| MR_1774414735_B9222424 | 504990 | 391 | -88.2 | 504990 | 147 | -88.0 | 504990 | 844 | -94.2 | 504990 | 313 |
| MR_1774414735_4DF6FA46 | 504990 | 391 | -89.8 | 504990 | 147 | -87.6 | 504990 | 844 | -92.1 | 504990 | 313 |
| MR_1774414735_FEFD0C29 | 504990 | 147 | -90.2 | 504990 | 391 | -86.9 | 504990 | 844 | -91.2 | 504990 | 313 |
| MR_1774414735_DFCB91D6 | 504990 | 391 | -87.8 | 504990 | 147 | -86.9 | 504990 | 844 | -91.8 | 504990 | 313 |
| MR_1774414735_12025E4B | 504990 | 391 | -90.3 | 504990 | 147 | -87.4 | 504990 | 844 | -93.4 | 504990 | 313 |
| MR_1774414735_3CDB7D80 | 504990 | 391 | -91.1 | 504990 | 147 | -88.3 | 504990 | 844 | -90.8 | 504990 | 313 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 47: `3720ba2c-7aa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3720ba2c-7aac-41f5-a408-b37379a33b6e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[47] topology](images/test_0047.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3253955_2
- `C2`: Decrease transmission power for 3253955_2
- `C3`: Add neighbor relationship between 3243821_3 and 3253955_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224187_1
- `C5`: Decrease transmission power for 3224187_1
- `C6`: Check test server and transmission issues
- `C7`: Decrease A3 Offset threshold for 3253955_2
- `C8`: Increase transmission power for 3224187_1
- `C9`: Press down the tilt angle of 3224187_1 by 7 degrees
- `C10`: Lift the tilt angle of 3224187_1 by 7 degrees
- `C11`: Lift the tilt angle  of 3253955_2 by 10 degrees
- `C12`: Adjust the azimuth of 3224187_1 by 18 degrees
- `C13`: Increase A3 Offset threshold for 3224187_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253955_2
- `C15`: Increase transmission power for 3253955_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224187_1
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Add neighbor relationship between 3224187_1 and 3253955_2
- `C19`: Decrease A3 Offset threshold for 3224187_1
- `C20`: Press down the tilt angle  of 3253955_2 by 10 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253955_2
- `C22`: Adjust the azimuth of 3253955_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.556 | MS1 | 121.4656758242 | 31.1446219460 | 921 | 504990 | -82.33 | 12.83 | 480.29 | 0.19 | 2.64 | 1589 |
| 2024-09-20 22:21:32.865 | MS1 | 121.4656709286 | 31.1446259616 | 921 | 504990 | -84.15 | 14.34 | 469.95 | 0.05 | 2.97 | 1583 |
| 2024-09-20 22:21:33.248 | MS1 | 121.4656592453 | 31.1446350113 | 921 | 504990 | -82.49 | 16.47 | 415.31 | 0.02 | 2.79 | 1577 |
| 2024-09-20 22:21:34.133 | MS1 | 121.4656727539 | 31.1446199971 | 921 | 504990 | -92.18 | -1.90 | 41.52 | 0.01 | 1.25 | 1576 |
| 2024-09-20 22:21:35.383 | MS1 | 121.4656699344 | 31.1446241012 | 921 | 504990 | -90.29 | -1.82 | 46.95 | 0.12 | 1.49 | 1595 |
| 2024-09-20 22:21:36.302 | MS1 | 121.4656734108 | 31.1446222163 | 921 | 504990 | -88.16 | -3.23 | 79.65 | 0.09 | 1.39 | 1576 |
| 2024-09-20 22:21:37.954 | MS1 | 121.4656747189 | 31.1446345527 | 921 | 504990 | -89.79 | -1.60 | 39.58 | 0.12 | 1.21 | 1568 |
| 2024-09-20 22:21:38.762 | MS1 | 121.4656743949 | 31.1446282435 | 921 | 504990 | -88.69 | -0.69 | 60.23 | 0.08 | 1.40 | 1588 |
| 2024-09-20 22:21:39.101 | MS1 | 121.4656705625 | 31.1446204801 | 471 | 504990 | -78.59 | 17.76 | 274.32 | 0.18 | 1.18 | 1570 |
| 2024-09-20 22:21:40.488 | MS1 | 121.4656588525 | 31.1446279873 | 471 | 504990 | -84.64 | 16.11 | 462.89 | 0.09 | 2.50 | 1598 |
| 2024-09-20 22:21:41.721 | MS1 | 121.4656691359 | 31.1446363342 | 471 | 504990 | -82.41 | 12.37 | 394.37 | 0.11 | 2.16 | 1564 |
| 2024-09-20 22:21:42.602 | MS1 | 121.4656755425 | 31.1446181547 | 471 | 504990 | -78.48 | 14.14 | 523.87 | 0.02 | 2.57 | 1566 |

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
| 3220149 | 4 | 121.4748956418 | 31.1472955298 | 224 | 1 | 4 | 46.7 | TDD | 791 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3224187 | 1 | 121.4741503319 | 31.1482883183 | 261 | 5 | 10 | 33.8 | TDD | 921 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3243821 | 3 | 121.4721040217 | 31.1465702240 | 196 | 5 | 4 | 19.8 | TDD | 741 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3253955 | 2 | 121.4675399371 | 31.1468478003 | 70 | 5 | 5 | 31.7 | TDD | 471 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.103 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.128 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.239 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.239 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.975 | NREventA3 | measId:2;ServCellPCI:795;Se... |
| 2024-09-20 22:21:38.215 | NRHandoverAttempt | SourcePCI:795;SourceNR-ARFC... |
| 2024-09-20 22:21:38.251 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.263 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.402 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.402 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224187 | 1 | 8.1443 | 16.0642 | -115.9993 | 14.8783 | 151.5247 | 0.0000 | 0.1832 |
| 2024_09_20 22:00 | 3253955 | 2 | 5.0077 | 8.7661 | -115.0135 | 13.1629 | 142.1816 | 0.0175 | 0.0073 |
| 2024_09_20 22:00 | 3243821 | 3 | 6.2003 | 5.3349 | -117.0588 | 8.9476 | 155.4324 | 0.0018 | 0.0001 |
| 2024_09_20 22:00 | 3220149 | 4 | 17.6762 | 13.5359 | -117.3879 | 8.9715 | 86.5518 | 0.0040 | 0.0154 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414127_DA6750E5 | 504990 | 921 | -91.1 | 504990 | 471 | -88.3 | 504990 | 741 | -89.0 | 504990 | 791 |
| MR_1774414127_F6CEBC92 | 504990 | 471 | -85.6 | 504990 | 921 | -92.3 | 504990 | 741 | -89.1 | 504990 | 791 |
| MR_1774414127_66EE3EC9 | 504990 | 921 | -90.9 | 504990 | 471 | -84.7 | 504990 | 741 | -85.7 | 504990 | 791 |
| MR_1774414127_0710F67B | 504990 | 921 | -94.1 | 504990 | 471 | -86.6 | 504990 | 741 | -86.3 | 504990 | 791 |
| MR_1774414127_8583359B | 504990 | 471 | -86.5 | 504990 | 921 | -92.8 | 504990 | 741 | -86.2 | 504990 | 791 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 48: `f45d84d2-ae7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f45d84d2-ae71-42ef-b814-4d4d9fbddf46` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[48] topology](images/test_0048.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261512_4
- `C2`: Check test server and transmission issues
- `C3`: Decrease transmission power for 3261512_4
- `C4`: Increase A3 Offset threshold for 3251835_1
- `C5`: Lift the tilt angle  of 3261512_4 by 2 degrees
- `C6`: Add neighbor relationship between 3236607_12 and 3261512_4
- `C7`: Increase A3 Offset threshold for 3261512_4
- `C8`: Increase transmission power for 3251835_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261512_4
- `C10`: Decrease transmission power for 3251835_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Lift the tilt angle of 3251835_1 by 3 degrees
- `C13`: Decrease A3 Offset threshold for 3251835_1
- `C14`: Press down the tilt angle  of 3261512_4 by 2 degrees
- `C15`: Add neighbor relationship between 3251835_1 and 3261512_4
- `C16`: Press down the tilt angle of 3251835_1 by 3 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251835_1
- `C18`: Increase transmission power for 3261512_4
- `C19`: Decrease A3 Offset threshold for 3261512_4
- `C20`: Adjust the azimuth of 3251835_1 by 41 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251835_1
- `C22`: Adjust the azimuth of 3261512_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.340 | MS1 | 121.4656663778 | 31.1446189785 | 100 | 504990 | -94.29 | 12.87 | 396.70 | 0.12 | 2.72 | 1592 |
| 2024-09-20 22:21:32.477 | MS1 | 121.4656585686 | 31.1446364553 | 286 | 504990 | -94.33 | 12.96 | 442.66 | 0.11 | 2.39 | 1570 |
| 2024-09-20 22:21:33.249 | MS1 | 121.4656776833 | 31.1446334921 | 269 | 504990 | -95.84 | 11.52 | 416.67 | 0.11 | 2.49 | 1595 |
| 2024-09-20 22:21:34.825 | MS1 | 121.4656626309 | 31.1446182157 | 172 | 152650 | -93.59 | 7.21 | 77.93 | 0.04 | 1.93 | 966 |
| 2024-09-20 22:21:35.363 | MS1 | 121.4656670940 | 31.1446375220 | 541 | 152650 | -91.56 | 7.57 | 74.44 | 0.07 | 1.56 | 916 |
| 2024-09-20 22:21:36.189 | MS1 | 121.4656763282 | 31.1446322148 | 280 | 152650 | -87.90 | 6.89 | 84.56 | 0.19 | 1.57 | 909 |
| 2024-09-20 22:21:37.955 | MS1 | 121.4656687640 | 31.1446185327 | 230 | 152650 | -90.61 | 6.18 | 101.19 | 0.08 | 1.67 | 932 |
| 2024-09-20 22:21:38.553 | MS1 | 121.4656666704 | 31.1446264453 | 172 | 152650 | -91.39 | 6.68 | 67.10 | 0.10 | 1.78 | 932 |
| 2024-09-20 22:21:39.879 | MS1 | 121.4656769821 | 31.1446187443 | 541 | 152650 | -87.77 | 2.70 | 43.85 | 0.06 | 1.90 | 958 |
| 2024-09-20 22:21:40.406 | MS1 | 121.4656718927 | 31.1446358170 | 280 | 152650 | -96.35 | 2.62 | 81.21 | 0.19 | 2.15 | 1569 |
| 2024-09-20 22:21:41.466 | MS1 | 121.4656777894 | 31.1446208048 | 230 | 152650 | -90.00 | 2.06 | 59.87 | 0.18 | 2.74 | 1591 |
| 2024-09-20 22:21:42.775 | MS1 | 121.4656596056 | 31.1446189347 | 172 | 152650 | -90.32 | 7.56 | 69.30 | 0.16 | 2.03 | 1585 |

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
| 3219687 | 8 | 121.4731733877 | 31.1517030234 | 194 | 6 | 8 | 14.8 | FDD | 961 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3228226 | 11 | 121.4757701567 | 31.1516933737 | 166 | 6 | 9 | 19.0 | FDD | 189 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3236607 | 12 | 121.4706448203 | 31.1462710245 | 100 | 6 | 6 | 20.0 | FDD | 280 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3239146 | 13 | 121.4656271275 | 31.1479202859 | 145 | 3 | 1 | 2.6 | FDD | 541 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3244860 | 6 | 121.4664673912 | 31.1547617570 | 327 | 15 | 3 | 23.8 | TDD | 286 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3246720 | 5 | 121.4690218169 | 31.1498710625 | 170 | 1 | 4 | 17.3 | TDD | 154 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3250625 | 3 | 121.4704372547 | 31.1514685730 | 38 | 5 | 8 | 15.2 | TDD | 312 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3251353 | 10 | 121.4726670462 | 31.1485967455 | 131 | 4 | 3 | 25.5 | FDD | 172 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3251835 | 1 | 121.4654447083 | 31.1493485127 | 219 | 0 | 11 | 27.8 | TDD | 100 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3254391 | 7 | 121.4694015635 | 31.1442022248 | 3 | 7 | 1 | 13.6 | FDD | 800 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3261512 | 4 | 121.4747150855 | 31.1533146671 | 212 | 1 | 11 | 27.7 | TDD | 345 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3272112 | 2 | 121.4652490318 | 31.1505325009 | 162 | 11 | 10 | 28.0 | TDD | 269 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3274925 | 9 | 121.4747850487 | 31.1470889843 | 146 | 13 | 7 | 15.9 | FDD | 230 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |

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
| 2024-09-20 22:21:31.139 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.163 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.271 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.271 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.997 | NREventA2 | measId:1;ServCellPCI:784;Se... |
| 2024-09-20 22:21:35.137 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.365 | NREventA5 | measId:3;ServCellPCI:784;Se... |
| 2024-09-20 22:21:35.396 | NRHandoverAttempt | SourcePCI:784;SourceNR-ARFC... |
| 2024-09-20 22:21:35.424 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.438 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.573 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.573 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251835 | 1 | 19.0255 | 15.0243 | -115.8537 | 12.2180 | 111.4218 | 0.0153 | 0.0191 |
| 2024_09_20 22:00 | 3272112 | 2 | 13.6761 | 10.6562 | -115.4930 | 15.0951 | 120.5442 | 0.0197 | 0.0061 |
| 2024_09_20 22:00 | 3250625 | 3 | 16.6766 | 17.7728 | -117.7085 | 12.8399 | 111.3353 | 0.0184 | 0.0059 |
| 2024_09_20 22:00 | 3261512 | 4 | 12.8164 | 6.9712 | -116.9013 | 16.2842 | 127.8040 | 0.0034 | 0.0194 |
| 2024_09_20 22:00 | 3246720 | 5 | 6.5639 | 5.8617 | -114.2416 | 15.0044 | 143.1380 | 0.0149 | 0.0139 |
| 2024_09_20 22:00 | 3244860 | 6 | 8.0449 | 5.8610 | -114.1275 | 10.2754 | 96.4373 | 0.0158 | 0.0017 |
| 2024_09_20 22:00 | 3254391 | 7 | 18.7094 | 15.0586 | -115.8540 | 3.8361 | 34.6959 | 0.0059 | 0.0026 |
| 2024_09_20 22:00 | 3219687 | 8 | 9.0554 | 8.6881 | -115.5339 | 4.2255 | 40.6787 | 0.0051 | 0.0019 |
| 2024_09_20 22:00 | 3274925 | 9 | 13.5590 | 19.2147 | -114.7433 | 3.2410 | 50.4755 | 0.0173 | 0.0147 |
| 2024_09_20 22:00 | 3251353 | 10 | 12.7440 | 10.8881 | -115.6303 | 4.8746 | 56.8827 | 0.0164 | 0.0191 |
| 2024_09_20 22:00 | 3228226 | 11 | 11.1281 | 18.6879 | -116.0291 | 3.6697 | 35.3531 | 0.0157 | 0.0065 |
| 2024_09_20 22:00 | 3236607 | 12 | 5.5782 | 6.3674 | -114.5021 | 4.8138 | 38.9583 | 0.0002 | 0.0111 |
| 2024_09_20 22:00 | 3239146 | 13 | 18.6448 | 5.6052 | -117.4029 | 4.9596 | 32.0337 | 0.0036 | 0.0034 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413514_4FCE1AF4 | 152650 | 172 | -94.6 | 152650 | 961 | -101.1 | 152650 | 800 | -102.2 | 152650 | 189 |
| MR_1774413514_26CAEEDD | 504990 | 269 | -96.7 | 504990 | 345 | -95.5 | 504990 | 154 | -98.8 | 504990 | 312 |
| MR_1774413514_C874735B | 152650 | 172 | -93.2 | 152650 | 961 | -103.4 | 152650 | 800 | -101.9 | 152650 | 189 |
| MR_1774413514_1B726AC9 | 504990 | 269 | -94.8 | 504990 | 345 | -96.6 | 504990 | 154 | -101.4 | 504990 | 312 |
| MR_1774413514_CF431463 | 152650 | 172 | -95.4 | 152650 | 961 | -100.3 | 152650 | 800 | -105.2 | 152650 | 189 |
| MR_1774413514_9A1749AE | 504990 | 269 | -94.4 | 504990 | 345 | -95.1 | 504990 | 154 | -101.6 | 504990 | 312 |
| MR_1774413514_F55C887A | 152650 | 172 | -94.9 | 152650 | 961 | -102.8 | 152650 | 800 | -102.7 | 152650 | 189 |
| MR_1774413514_6C4DF93E | 152650 | 172 | -92.8 | 152650 | 961 | -102.9 | 152650 | 800 | -104.6 | 152650 | 189 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 49: `66c959ea-332...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `66c959ea-332d-4802-a7ff-af79dc2bf566` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[49] topology](images/test_0049.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3238245_1
- `C2`: Increase A3 Offset threshold for 3238245_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Add neighbor relationship between 3237113_4 and 3255363_3
- `C5`: Press down the tilt angle of 3238245_1 by 10 degrees
- `C6`: Adjust the azimuth of 3238245_1 by 50 degrees
- `C7`: Decrease transmission power for 3255363_3
- `C8`: Add neighbor relationship between 3238245_1 and 3255363_3
- `C9`: Lift the tilt angle  of 3255363_3 by 3 degrees
- `C10`: Lift the tilt angle of 3238245_1 by 10 degrees
- `C11`: Decrease A3 Offset threshold for 3255363_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238245_1
- `C13`: Decrease transmission power for 3238245_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255363_3
- `C15`: Increase transmission power for 3255363_3
- `C16`: Check test server and transmission issues
- `C17`: Increase transmission power for 3238245_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238245_1
- `C19`: Increase A3 Offset threshold for 3255363_3
- `C20`: Press down the tilt angle  of 3255363_3 by 3 degrees
- `C21`: Adjust the azimuth of 3255363_3 by 19 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255363_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.469 | MS1 | 121.4656726609 | 31.1446356221 | 528 | 504990 | -82.67 | 12.45 | 410.28 | 0.07 | 2.42 | 1571 |
| 2024-09-20 22:21:32.101 | MS1 | 121.4656625224 | 31.1446352020 | 528 | 504990 | -83.76 | 17.21 | 361.98 | 0.15 | 2.55 | 1591 |
| 2024-09-20 22:21:33.909 | MS1 | 121.4656659092 | 31.1446231877 | 528 | 504990 | -77.08 | 17.77 | 538.49 | 0.12 | 2.04 | 1597 |
| 2024-09-20 22:21:34.670 | MS1 | 121.4656727360 | 31.1446261597 | 528 | 504990 | -88.87 | -2.30 | 71.08 | 0.17 | 1.06 | 1569 |
| 2024-09-20 22:21:35.960 | MS1 | 121.4656749549 | 31.1446330172 | 528 | 504990 | -87.12 | -3.31 | 69.15 | 0.06 | 1.07 | 1571 |
| 2024-09-20 22:21:36.748 | MS1 | 121.4656688429 | 31.1446257916 | 528 | 504990 | -88.22 | -1.93 | 39.67 | 0.06 | 1.09 | 1572 |
| 2024-09-20 22:21:37.609 | MS1 | 121.4656720981 | 31.1446245856 | 528 | 504990 | -86.62 | -3.73 | 43.33 | 0.19 | 1.44 | 1597 |
| 2024-09-20 22:21:38.102 | MS1 | 121.4656755597 | 31.1446236398 | 528 | 504990 | -80.47 | 17.52 | 511.11 | 0.03 | 1.47 | 1586 |
| 2024-09-20 22:21:39.484 | MS1 | 121.4656706765 | 31.1446257856 | 528 | 504990 | -78.46 | 13.82 | 495.99 | 0.12 | 1.33 | 1569 |
| 2024-09-20 22:21:40.430 | MS1 | 121.4656760640 | 31.1446300195 | 528 | 504990 | -77.28 | 14.64 | 558.57 | 0.08 | 2.92 | 1566 |
| 2024-09-20 22:21:41.366 | MS1 | 121.4656591163 | 31.1446227750 | 528 | 504990 | -77.51 | 16.14 | 550.49 | 0.11 | 2.80 | 1566 |
| 2024-09-20 22:21:42.641 | MS1 | 121.4656604689 | 31.1446356956 | 528 | 504990 | -77.41 | 17.38 | 519.83 | 0.07 | 2.42 | 1596 |

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
| 3226923 | 2 | 121.4641084580 | 31.1444126192 | 69 | 12 | 8 | 46.9 | TDD | 96 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3237113 | 4 | 121.4740019959 | 31.1493978096 | 343 | 8 | 6 | 41.2 | TDD | 119 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3238245 | 1 | 121.4659806279 | 31.1545530835 | 5 | 14 | 8 | 34.6 | TDD | 528 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3255363 | 3 | 121.4714851648 | 31.1532764420 | 229 | 2 | 7 | 23.8 | TDD | 678 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.980 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.996 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.097 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.097 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.852 | NREventA3 | measId:2;ServCellPCI:87;Ser... |
| 2024-09-20 22:21:35.852 | NREventA3 | measId:2;ServCellPCI:87;Ser... |
| 2024-09-20 22:21:36.852 | NREventA3 | measId:2;ServCellPCI:87;Ser... |
| 2024-09-20 22:21:39.352 | NRRRCReestablishAttempt | PCI:87 |
| 2024-09-20 22:21:39.367 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.378 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.521 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.521 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238245 | 1 | 15.3005 | 12.3471 | -114.3859 | 10.5551 | 146.7563 | 0.0089 | 0.1959 |
| 2024_09_20 22:00 | 3226923 | 2 | 12.7278 | 11.7558 | -115.8327 | 10.3571 | 177.5709 | 0.0081 | 0.0055 |
| 2024_09_20 22:00 | 3255363 | 3 | 8.7007 | 5.5501 | -115.0630 | 16.3512 | 120.9221 | 0.0043 | 0.0177 |
| 2024_09_20 22:00 | 3237113 | 4 | 17.8757 | 16.7115 | -116.1921 | 13.3720 | 135.6879 | 0.0004 | 0.0009 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415368_BB57D355 | 504990 | 678 | -81.9 | 504990 | 528 | -89.8 | 504990 | 119 | -84.6 | 504990 | 96 |
| MR_1774415368_1A40F978 | 504990 | 678 | -84.1 | 504990 | 528 | -89.0 | 504990 | 119 | -84.6 | 504990 | 96 |
| MR_1774415368_81F39855 | 504990 | 678 | -85.3 | 504990 | 528 | -90.4 | 504990 | 119 | -84.9 | 504990 | 96 |
| MR_1774415368_78E3AD04 | 504990 | 678 | -82.0 | 504990 | 528 | -88.6 | 504990 | 119 | -87.9 | 504990 | 96 |
| MR_1774415368_26F99DEB | 504990 | 678 | -84.8 | 504990 | 528 | -89.5 | 504990 | 119 | -84.1 | 504990 | 96 |
| MR_1774415368_4075DFD2 | 504990 | 528 | -88.4 | 504990 | 678 | -81.9 | 504990 | 119 | -86.3 | 504990 | 96 |
| MR_1774415368_0BFE2BBA | 504990 | 528 | -89.0 | 504990 | 678 | -82.0 | 504990 | 119 | -86.5 | 504990 | 96 |
| MR_1774415368_FBF15D71 | 504990 | 678 | -85.7 | 504990 | 528 | -88.6 | 504990 | 119 | -86.3 | 504990 | 96 |

> *... 2개 열 생략 (전체 14열)*

---
