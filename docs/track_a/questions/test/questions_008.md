# Track A 문제 분석 — test[70]~test[79]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[70] ~ test[79] (10개)

## 목차

1. [문제 70: `228d7c46-245...`](#70) — single-answer
2. [문제 71: `127185e7-f19...`](#71) — single-answer
3. [문제 72: `be9afd70-1eb...`](#72) — single-answer
4. [문제 73: `01dc52be-979...`](#73) — single-answer
5. [문제 74: `e66c48ff-39d...`](#74) — single-answer
6. [문제 75: `2cb1a364-0be...`](#75) — single-answer
7. [문제 76: `1dbd6c19-939...`](#76) — single-answer
8. [문제 77: `399e0ae7-028...`](#77) — single-answer
9. [문제 78: `3d419e73-67a...`](#78) — single-answer
10. [문제 79: `4afc7315-302...`](#79) — multiple-answer

---

### 문제 70: `228d7c46-245...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `228d7c46-245d-459d-961c-035f58d77e99` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[70] topology](images/test_0070.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3221561_4 by 38 degrees
- `C2`: Add neighbor relationship between 3270414_3 and 3243864_1
- `C3`: Add neighbor relationship between 3221561_4 and 3243864_1
- `C4`: Decrease A3 Offset threshold for 3221561_4
- `C5`: Lift the tilt angle  of 3243864_1 by 5 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221561_4
- `C7`: Check test server and transmission issues
- `C8`: Adjust the azimuth of 3243864_1 by 50 degrees
- `C9`: Increase A3 Offset threshold for 3221561_4
- `C10`: Press down the tilt angle of 3221561_4 by 4 degrees
- `C11`: Decrease A3 Offset threshold for 3243864_1
- `C12`: Decrease transmission power for 3221561_4
- `C13`: Increase A3 Offset threshold for 3243864_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221561_4
- `C15`: Decrease transmission power for 3243864_1
- `C16`: Lift the tilt angle of 3221561_4 by 4 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243864_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243864_1
- `C20`: Press down the tilt angle  of 3243864_1 by 5 degrees
- `C21`: Increase transmission power for 3221561_4
- `C22`: Increase transmission power for 3243864_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.569 | MS1 | 121.4656593375 | 31.1446289108 | 521 | 504990 | -91.19 | 13.76 | 567.99 | 0.03 | 2.03 | 1599 |
| 2024-09-20 22:21:32.386 | MS1 | 121.4656729347 | 31.1446378223 | 521 | 504990 | -87.23 | 16.08 | 438.39 | 0.05 | 2.18 | 1562 |
| 2024-09-20 22:21:33.188 | MS1 | 121.4656749877 | 31.1446360120 | 521 | 504990 | -88.34 | 15.62 | 335.28 | 0.15 | 2.91 | 1589 |
| 2024-09-20 22:21:34.401 | MS1 | 121.4656773685 | 31.1446342548 | 521 | 504990 | -89.52 | 17.68 | 70.18 | 0.60 | 2.35 | 555 |
| 2024-09-20 22:21:35.464 | MS1 | 121.4656759517 | 31.1446253806 | 521 | 504990 | -91.32 | 16.33 | 90.03 | 0.60 | 2.55 | 503 |
| 2024-09-20 22:21:36.558 | MS1 | 121.4656669144 | 31.1446322418 | 521 | 504990 | -90.65 | 15.38 | 52.37 | 0.69 | 2.56 | 662 |
| 2024-09-20 22:21:37.908 | MS1 | 121.4656662931 | 31.1446213162 | 521 | 504990 | -90.16 | 8.23 | 91.92 | 0.51 | 2.13 | 505 |
| 2024-09-20 22:21:38.664 | MS1 | 121.4656779033 | 31.1446358995 | 521 | 504990 | -93.68 | 11.63 | 47.62 | 0.68 | 2.97 | 663 |
| 2024-09-20 22:21:39.408 | MS1 | 121.4656600432 | 31.1446379052 | 521 | 504990 | -93.32 | 10.95 | 61.47 | 0.60 | 2.16 | 548 |
| 2024-09-20 22:21:40.200 | MS1 | 121.4656607616 | 31.1446260781 | 521 | 504990 | -92.85 | 12.14 | 490.31 | 0.01 | 2.90 | 1565 |
| 2024-09-20 22:21:41.678 | MS1 | 121.4656615971 | 31.1446296953 | 521 | 504990 | -93.56 | 12.70 | 444.43 | 0.05 | 2.72 | 1578 |
| 2024-09-20 22:21:42.750 | MS1 | 121.4656636125 | 31.1446348909 | 521 | 504990 | -89.97 | 9.59 | 333.93 | 0.00 | 3.00 | 1572 |

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
| 3221561 | 4 | 121.4705274017 | 31.1533229295 | 168 | 1 | 8 | 47.7 | TDD | 521 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3238845 | 2 | 121.4732749842 | 31.1472409834 | 55 | 10 | 9 | 46.1 | TDD | 490 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3243864 | 1 | 121.4692256020 | 31.1484560774 | 43 | 0 | 12 | 44.0 | TDD | 345 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3270414 | 3 | 121.4674324795 | 31.1481543069 | 306 | 7 | 9 | 29.8 | TDD | 965 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.548 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.571 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.710 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.710 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.372 | NREventA3 | measId:2;ServCellPCI:864;Se... |
| 2024-09-20 22:21:38.612 | NRHandoverAttempt | SourcePCI:864;SourceNR-ARFC... |
| 2024-09-20 22:21:38.654 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.664 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.805 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.805 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243864 | 1 | 5.8030 | 7.1202 | -114.3027 | 13.8124 | 86.6718 | 0.0113 | 0.0113 |
| 2024_09_20 22:00 | 3238845 | 2 | 9.3929 | 9.9532 | -116.9987 | 11.1602 | 186.1574 | 0.0003 | 0.0024 |
| 2024_09_20 22:00 | 3270414 | 3 | 18.4662 | 14.9930 | -115.0872 | 7.6484 | 183.7853 | 0.0039 | 0.0128 |
| 2024_09_20 22:00 | 3221561 | 4 | 13.8676 | 12.6546 | -114.9777 | 10.9958 | 145.5507 | 0.0177 | 0.0111 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417199_C0B34DE7 | 504990 | 521 | -90.8 | 504990 | 345 | -88.9 | 504990 | 965 | -97.8 | 504990 | 490 |
| MR_1774417199_1859B4A7 | 504990 | 521 | -89.2 | 504990 | 345 | -89.6 | 504990 | 965 | -97.3 | 504990 | 490 |
| MR_1774417199_6A3B1214 | 504990 | 521 | -90.4 | 504990 | 345 | -89.1 | 504990 | 965 | -95.5 | 504990 | 490 |
| MR_1774417199_26D27ED2 | 504990 | 521 | -89.7 | 504990 | 345 | -89.3 | 504990 | 965 | -98.8 | 504990 | 490 |
| MR_1774417199_11A7ECD1 | 504990 | 521 | -89.0 | 504990 | 345 | -89.3 | 504990 | 965 | -95.5 | 504990 | 490 |
| MR_1774417199_E424E325 | 504990 | 521 | -88.6 | 504990 | 345 | -91.2 | 504990 | 965 | -96.2 | 504990 | 490 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 71: `127185e7-f19...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `127185e7-f195-48f3-8c5d-11b786a57bde` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[71] topology](images/test_0071.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3263451_4
- `C2`: Increase transmission power for 3263451_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248652_1
- `C4`: Decrease A3 Offset threshold for 3263451_4
- `C5`: Adjust the azimuth of 3248652_1 by 25 degrees
- `C6`: Increase A3 Offset threshold for 3263451_4
- `C7`: Increase transmission power for 3248652_1
- `C8`: Press down the tilt angle of 3248652_1 by 6 degrees
- `C9`: Adjust the azimuth of 3263451_4 by 48 degrees
- `C10`: Decrease A3 Offset threshold for 3248652_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248652_1
- `C12`: Press down the tilt angle  of 3263451_4 by 1 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263451_4
- `C14`: Add neighbor relationship between 3271334_12 and 3263451_4
- `C15`: Decrease transmission power for 3248652_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263451_4
- `C17`: Lift the tilt angle  of 3263451_4 by 1 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Increase A3 Offset threshold for 3248652_1
- `C20`: Add neighbor relationship between 3248652_1 and 3263451_4
- `C21`: Lift the tilt angle of 3248652_1 by 6 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.818 | MS1 | 121.4656627457 | 31.1446201378 | 795 | 504990 | -95.38 | 14.12 | 419.06 | 0.20 | 2.55 | 1579 |
| 2024-09-20 22:21:32.553 | MS1 | 121.4656733900 | 31.1446198277 | 490 | 504990 | -93.96 | 10.22 | 526.76 | 0.09 | 2.99 | 1561 |
| 2024-09-20 22:21:33.559 | MS1 | 121.4656602391 | 31.1446319070 | 621 | 504990 | -93.11 | 9.19 | 419.44 | 0.13 | 2.98 | 1571 |
| 2024-09-20 22:21:34.915 | MS1 | 121.4656723092 | 31.1446319167 | 473 | 152650 | -92.71 | 7.01 | 66.00 | 0.02 | 1.50 | 958 |
| 2024-09-20 22:21:35.797 | MS1 | 121.4656701944 | 31.1446331928 | 16 | 152650 | -88.36 | 2.90 | 102.25 | 0.02 | 1.61 | 959 |
| 2024-09-20 22:21:36.317 | MS1 | 121.4656633096 | 31.1446247382 | 636 | 152650 | -88.39 | 4.32 | 95.66 | 0.10 | 1.93 | 981 |
| 2024-09-20 22:21:37.842 | MS1 | 121.4656745261 | 31.1446297282 | 335 | 152650 | -88.31 | 2.15 | 82.32 | 0.09 | 1.78 | 987 |
| 2024-09-20 22:21:38.462 | MS1 | 121.4656662425 | 31.1446363979 | 473 | 152650 | -94.70 | 7.66 | 55.21 | 0.13 | 1.99 | 930 |
| 2024-09-20 22:21:39.400 | MS1 | 121.4656591051 | 31.1446343798 | 16 | 152650 | -87.02 | 6.32 | 72.30 | 0.19 | 1.63 | 990 |
| 2024-09-20 22:21:40.966 | MS1 | 121.4656661195 | 31.1446254326 | 636 | 152650 | -87.60 | 6.62 | 86.96 | 0.07 | 2.32 | 1583 |
| 2024-09-20 22:21:41.376 | MS1 | 121.4656648908 | 31.1446367643 | 335 | 152650 | -92.49 | 7.02 | 49.49 | 0.06 | 2.66 | 1565 |
| 2024-09-20 22:21:42.725 | MS1 | 121.4656746843 | 31.1446297052 | 473 | 152650 | -90.68 | 6.27 | 81.65 | 0.06 | 2.30 | 1587 |

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
| 3214834 | 3 | 121.4692720786 | 31.1441329523 | 288 | 12 | 4 | 18.7 | TDD | 621 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3215148 | 10 | 121.4641581686 | 31.1558712893 | 13 | 14 | 5 | 20.3 | FDD | 757 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3219002 | 9 | 121.4733729189 | 31.1470402985 | 172 | 8 | 6 | 13.6 | FDD | 465 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3219857 | 8 | 121.4698204249 | 31.1465818665 | 204 | 4 | 0 | 14.5 | FDD | 16 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3227318 | 6 | 121.4651229475 | 31.1458468333 | 339 | 12 | 4 | 14.6 | TDD | 59 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3248652 | 1 | 121.4757468877 | 31.1450624552 | 242 | 5 | 6 | 11.9 | TDD | 795 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3254684 | 7 | 121.4676414310 | 31.1490386456 | 210 | 14 | 9 | 21.1 | FDD | 335 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3257739 | 13 | 121.4659911352 | 31.1552652819 | 198 | 13 | 12 | 13.2 | FDD | 701 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3263451 | 4 | 121.4663508260 | 31.1476984834 | 239 | 0 | 1 | 8.9 | TDD | 526 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3264716 | 5 | 121.4662339495 | 31.1509959551 | 275 | 8 | 9 | 3.2 | TDD | 22 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3271334 | 12 | 121.4731579213 | 31.1518200401 | 88 | 14 | 9 | 15.4 | FDD | 636 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3274472 | 11 | 121.4659439523 | 31.1513796166 | 223 | 12 | 10 | 9.7 | FDD | 473 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3277854 | 2 | 121.4747118959 | 31.1498640765 | 274 | 3 | 9 | 27.5 | TDD | 490 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.550 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.572 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.673 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.673 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.369 | NREventA2 | measId:1;ServCellPCI:721;Se... |
| 2024-09-20 22:21:35.479 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.681 | NREventA5 | measId:3;ServCellPCI:721;Se... |
| 2024-09-20 22:21:35.730 | NRHandoverAttempt | SourcePCI:721;SourceNR-ARFC... |
| 2024-09-20 22:21:35.764 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.779 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.881 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.881 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248652 | 1 | 9.5758 | 19.2347 | -114.7954 | 18.1830 | 89.6734 | 0.0195 | 0.0062 |
| 2024_09_20 22:00 | 3277854 | 2 | 11.7411 | 6.6448 | -117.1673 | 17.9775 | 88.9281 | 0.0087 | 0.0038 |
| 2024_09_20 22:00 | 3214834 | 3 | 14.3721 | 7.1005 | -115.7803 | 19.5662 | 193.8742 | 0.0150 | 0.0042 |
| 2024_09_20 22:00 | 3263451 | 4 | 10.8186 | 8.6529 | -115.3561 | 19.5725 | 105.6007 | 0.0146 | 0.0137 |
| 2024_09_20 22:00 | 3264716 | 5 | 14.2376 | 19.8915 | -114.7728 | 13.5342 | 167.6970 | 0.0000 | 0.0130 |
| 2024_09_20 22:00 | 3227318 | 6 | 12.4128 | 15.7178 | -117.5885 | 13.0987 | 178.9974 | 0.0151 | 0.0101 |
| 2024_09_20 22:00 | 3254684 | 7 | 8.8056 | 10.8129 | -117.9241 | 4.8806 | 47.5851 | 0.0091 | 0.0026 |
| 2024_09_20 22:00 | 3219857 | 8 | 5.0506 | 17.5901 | -116.8050 | 3.8810 | 55.1729 | 0.0071 | 0.0159 |
| 2024_09_20 22:00 | 3219002 | 9 | 12.6698 | 10.1988 | -117.3850 | 4.7284 | 29.2824 | 0.0176 | 0.0009 |
| 2024_09_20 22:00 | 3215148 | 10 | 13.7619 | 9.4269 | -117.9701 | 4.5712 | 27.0329 | 0.0108 | 0.0161 |
| 2024_09_20 22:00 | 3274472 | 11 | 6.8005 | 5.8564 | -116.9413 | 4.3979 | 56.1049 | 0.0039 | 0.0189 |
| 2024_09_20 22:00 | 3271334 | 12 | 18.7911 | 11.6392 | -116.5647 | 3.1846 | 46.2557 | 0.0167 | 0.0164 |
| 2024_09_20 22:00 | 3257739 | 13 | 5.4038 | 10.2387 | -116.6579 | 3.3556 | 28.4902 | 0.0097 | 0.0004 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416281_16C5A6CC | 152650 | 473 | -93.8 | 152650 | 465 | -96.9 | 152650 | 757 | -99.7 | 152650 | 701 |
| MR_1774416281_90A58F50 | 504990 | 621 | -94.1 | 504990 | 526 | -91.0 | 504990 | 59 | -94.4 | 504990 | 22 |
| MR_1774416281_2AB8733C | 504990 | 621 | -91.7 | 504990 | 526 | -91.7 | 504990 | 59 | -94.1 | 504990 | 22 |
| MR_1774416281_9A8E22DA | 152650 | 473 | -92.6 | 152650 | 465 | -100.1 | 152650 | 757 | -98.6 | 152650 | 701 |
| MR_1774416281_655CFF48 | 504990 | 621 | -92.6 | 504990 | 526 | -91.2 | 504990 | 59 | -91.8 | 504990 | 22 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 72: `be9afd70-1eb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `be9afd70-1eb5-409e-b5de-bde1ec49b3c4` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[72] topology](images/test_0072.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255199_6
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222792_5
- `C3`: Check test server and transmission issues
- `C4`: Increase transmission power for 3222792_5
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255199_6
- `C6`: Increase A3 Offset threshold for 3255199_6
- `C7`: Lift the tilt angle  of 3222792_5 by 3 degrees
- `C8`: Adjust the azimuth of 3222792_5 by 25 degrees
- `C9`: Press down the tilt angle of 3255199_6 by 3 degrees
- `C10`: Decrease transmission power for 3255199_6
- `C11`: Add neighbor relationship between 3264291_10 and 3222792_5
- `C12`: Add neighbor relationship between 3255199_6 and 3222792_5
- `C13`: Decrease transmission power for 3222792_5
- `C14`: Adjust the azimuth of 3255199_6 by 9 degrees
- `C15`: Decrease A3 Offset threshold for 3222792_5
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Lift the tilt angle of 3255199_6 by 3 degrees
- `C18`: Increase transmission power for 3255199_6
- `C19`: Decrease A3 Offset threshold for 3255199_6
- `C20`: Increase A3 Offset threshold for 3222792_5
- `C21`: Press down the tilt angle  of 3222792_5 by 3 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222792_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.270 | MS1 | 121.4656727212 | 31.1446304235 | 605 | 504990 | -94.60 | 13.67 | 420.07 | 0.01 | 2.80 | 1585 |
| 2024-09-20 22:21:32.640 | MS1 | 121.4656762677 | 31.1446317358 | 848 | 504990 | -94.15 | 9.57 | 559.69 | 0.11 | 2.38 | 1589 |
| 2024-09-20 22:21:33.403 | MS1 | 121.4656663330 | 31.1446298961 | 857 | 504990 | -93.26 | 14.45 | 469.11 | 0.04 | 2.05 | 1576 |
| 2024-09-20 22:21:34.207 | MS1 | 121.4656637421 | 31.1446217719 | 193 | 152650 | -94.83 | 7.08 | 82.10 | 0.10 | 1.65 | 991 |
| 2024-09-20 22:21:35.564 | MS1 | 121.4656599391 | 31.1446210421 | 186 | 152650 | -89.58 | 6.80 | 65.12 | 0.19 | 1.96 | 963 |
| 2024-09-20 22:21:36.978 | MS1 | 121.4656668700 | 31.1446363991 | 239 | 152650 | -88.16 | 7.05 | 60.11 | 0.10 | 1.68 | 932 |
| 2024-09-20 22:21:37.823 | MS1 | 121.4656718446 | 31.1446191233 | 350 | 152650 | -95.17 | 4.89 | 44.00 | 0.05 | 1.87 | 990 |
| 2024-09-20 22:21:38.768 | MS1 | 121.4656618895 | 31.1446242000 | 193 | 152650 | -87.29 | 6.15 | 74.67 | 0.17 | 1.72 | 965 |
| 2024-09-20 22:21:39.675 | MS1 | 121.4656738356 | 31.1446254922 | 186 | 152650 | -89.70 | 4.76 | 93.25 | 0.20 | 1.77 | 941 |
| 2024-09-20 22:21:40.533 | MS1 | 121.4656759599 | 31.1446319412 | 239 | 152650 | -89.61 | 2.82 | 49.73 | 0.10 | 2.39 | 1575 |
| 2024-09-20 22:21:41.912 | MS1 | 121.4656752117 | 31.1446218614 | 350 | 152650 | -93.90 | 2.81 | 79.68 | 0.13 | 2.97 | 1598 |
| 2024-09-20 22:21:42.953 | MS1 | 121.4656720350 | 31.1446247188 | 193 | 152650 | -87.01 | 7.48 | 72.32 | 0.09 | 2.33 | 1598 |

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
| 3210026 | 4 | 121.4712358153 | 31.1443171181 | 144 | 2 | 6 | 11.5 | TDD | 857 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3219776 | 11 | 121.4731311333 | 31.1532694394 | 255 | 10 | 3 | 21.5 | FDD | 186 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3222792 | 5 | 121.4663597301 | 31.1503533888 | 161 | 1 | 7 | 17.4 | TDD | 154 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3237403 | 13 | 121.4742122770 | 31.1520920677 | 324 | 11 | 1 | 20.6 | FDD | 63 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3243765 | 2 | 121.4724525163 | 31.1520035431 | 49 | 2 | 4 | 19.0 | TDD | 848 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3245449 | 7 | 121.4671274603 | 31.1495621204 | 76 | 10 | 4 | 10.0 | FDD | 193 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3251103 | 9 | 121.4673311690 | 31.1483327041 | 286 | 0 | 2 | 27.4 | FDD | 237 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3255199 | 6 | 121.4689148294 | 31.1469738303 | 221 | 2 | 9 | 5.0 | TDD | 605 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3258089 | 12 | 121.4660569315 | 31.1545962096 | 14 | 8 | 12 | 22.8 | FDD | 350 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3261314 | 3 | 121.4690080428 | 31.1485887919 | 116 | 12 | 11 | 4.9 | TDD | 657 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3264291 | 10 | 121.4657859478 | 31.1484252169 | 349 | 3 | 1 | 14.7 | FDD | 239 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3270738 | 1 | 121.4679835864 | 31.1486870410 | 115 | 12 | 12 | 21.7 | TDD | 974 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3272693 | 8 | 121.4712875072 | 31.1468277703 | 317 | 4 | 8 | 4.3 | FDD | 461 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |

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
| 2024-09-20 22:21:30.908 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.923 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.068 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.068 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.796 | NREventA2 | measId:1;ServCellPCI:545;Se... |
| 2024-09-20 22:21:34.915 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.140 | NREventA5 | measId:3;ServCellPCI:545;Se... |
| 2024-09-20 22:21:35.189 | NRHandoverAttempt | SourcePCI:545;SourceNR-ARFC... |
| 2024-09-20 22:21:35.238 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.248 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.367 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.367 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270738 | 1 | 12.1724 | 16.0823 | -115.0826 | 7.1105 | 128.9168 | 0.0006 | 0.0170 |
| 2024_09_20 22:00 | 3243765 | 2 | 14.5870 | 7.9090 | -115.6489 | 11.2555 | 113.1318 | 0.0084 | 0.0013 |
| 2024_09_20 22:00 | 3261314 | 3 | 7.9404 | 13.0849 | -117.4947 | 18.6286 | 180.3423 | 0.0163 | 0.0139 |
| 2024_09_20 22:00 | 3210026 | 4 | 19.2936 | 14.2589 | -114.8319 | 15.4797 | 164.1596 | 0.0115 | 0.0185 |
| 2024_09_20 22:00 | 3222792 | 5 | 13.8438 | 5.3400 | -117.2670 | 8.2996 | 163.7001 | 0.0021 | 0.0089 |
| 2024_09_20 22:00 | 3255199 | 6 | 12.6401 | 6.1680 | -114.2318 | 12.6802 | 110.1566 | 0.0190 | 0.0008 |
| 2024_09_20 22:00 | 3245449 | 7 | 8.8634 | 9.5543 | -116.5773 | 4.8186 | 55.7584 | 0.0109 | 0.0020 |
| 2024_09_20 22:00 | 3272693 | 8 | 12.1129 | 6.7332 | -116.5189 | 3.9971 | 22.0617 | 0.0019 | 0.0095 |
| 2024_09_20 22:00 | 3251103 | 9 | 16.9438 | 9.0834 | -115.9587 | 3.7258 | 55.4441 | 0.0187 | 0.0077 |
| 2024_09_20 22:00 | 3264291 | 10 | 13.4794 | 5.4938 | -116.5303 | 3.1906 | 53.4565 | 0.0158 | 0.0192 |
| 2024_09_20 22:00 | 3219776 | 11 | 8.7789 | 15.1453 | -115.3691 | 4.0182 | 28.3949 | 0.0142 | 0.0150 |
| 2024_09_20 22:00 | 3258089 | 12 | 12.6198 | 19.0555 | -114.7763 | 3.3738 | 55.1033 | 0.0081 | 0.0120 |
| 2024_09_20 22:00 | 3237403 | 13 | 7.2138 | 10.4591 | -116.7355 | 4.5950 | 55.3351 | 0.0095 | 0.0109 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414604_DF1911DC | 504990 | 857 | -93.3 | 504990 | 154 | -91.3 | 504990 | 974 | -100.1 | 504990 | 657 |
| MR_1774414604_CAE53031 | 152650 | 193 | -94.7 | 152650 | 63 | -98.8 | 152650 | 461 | -102.1 | 152650 | 237 |
| MR_1774414604_D6FAC6BF | 504990 | 857 | -92.4 | 504990 | 154 | -87.9 | 504990 | 974 | -102.4 | 504990 | 657 |
| MR_1774414604_B1DF9EE0 | 152650 | 193 | -93.4 | 152650 | 63 | -101.1 | 152650 | 461 | -101.6 | 152650 | 237 |
| MR_1774414604_CC60B357 | 504990 | 857 | -93.5 | 504990 | 154 | -90.9 | 504990 | 974 | -99.4 | 504990 | 657 |
| MR_1774414604_D37081B6 | 504990 | 857 | -93.9 | 504990 | 154 | -88.1 | 504990 | 974 | -102.0 | 504990 | 657 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 73: `01dc52be-979...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `01dc52be-9796-40de-815b-e65a6c644f4d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[73] topology](images/test_0073.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219188_4
- `C2`: Check test server and transmission issues
- `C3`: Decrease A3 Offset threshold for 3219188_4
- `C4`: Decrease A3 Offset threshold for 3215585_1
- `C5`: Adjust the azimuth of 3215585_1 by 27 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase transmission power for 3219188_4
- `C8`: Add neighbor relationship between 3214644_8 and 3215585_1
- `C9`: Lift the tilt angle  of 3215585_1 by 5 degrees
- `C10`: Press down the tilt angle of 3219188_4 by 5 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215585_1
- `C12`: Decrease transmission power for 3219188_4
- `C13`: Lift the tilt angle of 3219188_4 by 5 degrees
- `C14`: Increase transmission power for 3215585_1
- `C15`: Adjust the azimuth of 3219188_4 by 15 degrees
- `C16`: Press down the tilt angle  of 3215585_1 by 5 degrees
- `C17`: Increase A3 Offset threshold for 3215585_1
- `C18`: Decrease transmission power for 3215585_1
- `C19`: Increase A3 Offset threshold for 3219188_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215585_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219188_4
- `C22`: Add neighbor relationship between 3219188_4 and 3215585_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.416 | MS1 | 121.4656646774 | 31.1446186294 | 690 | 504990 | -94.97 | 14.96 | 352.91 | 0.08 | 2.17 | 1585 |
| 2024-09-20 22:21:32.131 | MS1 | 121.4656668740 | 31.1446235943 | 414 | 504990 | -94.86 | 9.77 | 546.16 | 0.18 | 2.09 | 1566 |
| 2024-09-20 22:21:33.168 | MS1 | 121.4656746838 | 31.1446201818 | 355 | 504990 | -94.48 | 9.41 | 327.69 | 0.01 | 2.57 | 1582 |
| 2024-09-20 22:21:34.979 | MS1 | 121.4656652990 | 31.1446257668 | 596 | 152650 | -96.76 | 4.85 | 88.67 | 0.12 | 1.60 | 995 |
| 2024-09-20 22:21:35.387 | MS1 | 121.4656645161 | 31.1446186651 | 733 | 152650 | -87.49 | 6.23 | 91.02 | 0.15 | 1.71 | 972 |
| 2024-09-20 22:21:36.658 | MS1 | 121.4656751617 | 31.1446242348 | 998 | 152650 | -94.26 | 5.97 | 84.55 | 0.14 | 1.57 | 938 |
| 2024-09-20 22:21:37.938 | MS1 | 121.4656732546 | 31.1446183640 | 621 | 152650 | -91.36 | 6.42 | 108.46 | 0.17 | 1.66 | 905 |
| 2024-09-20 22:21:38.374 | MS1 | 121.4656758192 | 31.1446213216 | 596 | 152650 | -92.97 | 3.46 | 89.07 | 0.06 | 1.62 | 922 |
| 2024-09-20 22:21:39.679 | MS1 | 121.4656595784 | 31.1446274365 | 733 | 152650 | -89.49 | 3.69 | 88.41 | 0.15 | 1.69 | 973 |
| 2024-09-20 22:21:40.949 | MS1 | 121.4656589811 | 31.1446249148 | 998 | 152650 | -95.86 | 4.16 | 70.42 | 0.20 | 2.36 | 1591 |
| 2024-09-20 22:21:41.135 | MS1 | 121.4656732699 | 31.1446310614 | 621 | 152650 | -94.98 | 4.96 | 69.48 | 0.08 | 2.13 | 1570 |
| 2024-09-20 22:21:42.572 | MS1 | 121.4656620835 | 31.1446317739 | 596 | 152650 | -87.02 | 4.22 | 100.93 | 0.06 | 2.67 | 1573 |

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
| 3214644 | 8 | 121.4687539864 | 31.1497089521 | 273 | 3 | 12 | 28.0 | FDD | 998 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3215585 | 1 | 121.4672319402 | 31.1527084433 | 216 | 5 | 7 | 5.2 | TDD | 32 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3219188 | 4 | 121.4689370372 | 31.1547937419 | 180 | 4 | 9 | 28.0 | TDD | 690 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3219360 | 11 | 121.4659798785 | 31.1455819909 | 161 | 14 | 6 | 28.0 | FDD | 951 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3224138 | 13 | 121.4699875282 | 31.1506747124 | 301 | 5 | 0 | 28.5 | FDD | 733 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3230895 | 10 | 121.4724053862 | 31.1507627072 | 53 | 8 | 10 | 22.9 | FDD | 596 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3233427 | 7 | 121.4744348652 | 31.1524518500 | 220 | 15 | 2 | 2.9 | FDD | 101 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3239901 | 2 | 121.4642800918 | 31.1446188965 | 156 | 4 | 4 | 2.5 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3244859 | 5 | 121.4671519533 | 31.1465266315 | 44 | 7 | 3 | 12.2 | TDD | 349 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3252409 | 3 | 121.4710343181 | 31.1483319020 | 78 | 3 | 11 | 12.8 | TDD | 236 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3257993 | 6 | 121.4743038833 | 31.1535188731 | 358 | 7 | 7 | 11.8 | TDD | 414 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3270950 | 9 | 121.4670147183 | 31.1542288539 | 287 | 4 | 4 | 19.2 | FDD | 621 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3274494 | 12 | 121.4756777923 | 31.1469987734 | 14 | 15 | 12 | 0.3 | FDD | 600 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |

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
| 2024-09-20 22:21:31.099 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.122 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.244 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.244 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.923 | NREventA2 | measId:1;ServCellPCI:739;Se... |
| 2024-09-20 22:21:35.069 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.315 | NREventA5 | measId:3;ServCellPCI:739;Se... |
| 2024-09-20 22:21:35.377 | NRHandoverAttempt | SourcePCI:739;SourceNR-ARFC... |
| 2024-09-20 22:21:35.403 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.413 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.556 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.556 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215585 | 1 | 19.6321 | 19.9120 | -116.0100 | 19.5795 | 125.6599 | 0.0104 | 0.0080 |
| 2024_09_20 22:00 | 3239901 | 2 | 6.5212 | 7.8183 | -115.6710 | 9.5809 | 181.7001 | 0.0059 | 0.0067 |
| 2024_09_20 22:00 | 3252409 | 3 | 16.6890 | 12.0327 | -116.2326 | 17.8668 | 110.0799 | 0.0063 | 0.0111 |
| 2024_09_20 22:00 | 3219188 | 4 | 15.2601 | 16.9923 | -116.8609 | 8.0303 | 152.6497 | 0.0148 | 0.0013 |
| 2024_09_20 22:00 | 3244859 | 5 | 12.6085 | 15.2498 | -116.5178 | 12.3886 | 174.9007 | 0.0107 | 0.0152 |
| 2024_09_20 22:00 | 3257993 | 6 | 16.5727 | 7.4761 | -114.5875 | 12.3671 | 134.4598 | 0.0082 | 0.0042 |
| 2024_09_20 22:00 | 3233427 | 7 | 9.3287 | 6.5972 | -114.0669 | 4.8598 | 43.2047 | 0.0148 | 0.0098 |
| 2024_09_20 22:00 | 3214644 | 8 | 16.2921 | 10.9692 | -115.5792 | 4.1507 | 57.1108 | 0.0136 | 0.0185 |
| 2024_09_20 22:00 | 3270950 | 9 | 17.8004 | 9.0483 | -117.4198 | 4.6361 | 23.8711 | 0.0014 | 0.0163 |
| 2024_09_20 22:00 | 3230895 | 10 | 7.8793 | 8.2697 | -117.0907 | 3.7052 | 30.5581 | 0.0160 | 0.0131 |
| 2024_09_20 22:00 | 3219360 | 11 | 5.2398 | 7.1012 | -116.1651 | 3.5935 | 37.4511 | 0.0077 | 0.0010 |
| 2024_09_20 22:00 | 3274494 | 12 | 8.2801 | 18.9011 | -116.4808 | 4.8205 | 20.4842 | 0.0036 | 0.0019 |
| 2024_09_20 22:00 | 3224138 | 13 | 11.3301 | 10.6970 | -117.4921 | 3.7420 | 48.0375 | 0.0100 | 0.0156 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414252_E218E2F7 | 152650 | 596 | -97.8 | 152650 | 951 | -103.7 | 152650 | 101 | -103.8 | 152650 | 600 |
| MR_1774414252_EB708BEF | 504990 | 355 | -93.2 | 504990 | 32 | -95.9 | 504990 | 349 | -100.4 | 504990 | 236 |
| MR_1774414252_2D10179B | 504990 | 355 | -93.0 | 504990 | 32 | -97.9 | 504990 | 349 | -101.2 | 504990 | 236 |
| MR_1774414252_FFADC210 | 152650 | 596 | -97.1 | 152650 | 951 | -103.3 | 152650 | 101 | -105.0 | 152650 | 600 |
| MR_1774414252_1C99FB03 | 152650 | 596 | -96.9 | 152650 | 951 | -103.5 | 152650 | 101 | -105.3 | 152650 | 600 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 74: `e66c48ff-39d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e66c48ff-39d1-421a-9234-9548c20bb075` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[74] topology](images/test_0074.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3216162_4 and 3229733_3
- `C2`: Decrease transmission power for 3216162_4
- `C3`: Lift the tilt angle of 3216162_4 by 10 degrees
- `C4`: Press down the tilt angle  of 3229733_3 by 10 degrees
- `C5`: Increase A3 Offset threshold for 3229733_3
- `C6`: Increase transmission power for 3216162_4
- `C7`: Decrease A3 Offset threshold for 3216162_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229733_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229733_3
- `C10`: Decrease transmission power for 3229733_3
- `C11`: Lift the tilt angle  of 3229733_3 by 10 degrees
- `C12`: Adjust the azimuth of 3229733_3 by 19 degrees
- `C13`: Increase transmission power for 3229733_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216162_4
- `C15`: Press down the tilt angle of 3216162_4 by 10 degrees
- `C16`: Adjust the azimuth of 3216162_4 by 50 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase A3 Offset threshold for 3216162_4
- `C19`: Add neighbor relationship between 3275565_1 and 3229733_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216162_4
- `C21`: Decrease A3 Offset threshold for 3229733_3
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.172 | MS1 | 121.4656608621 | 31.1446191853 | 462 | 504990 | -88.13 | 12.80 | 538.91 | 0.14 | 2.96 | 1590 |
| 2024-09-20 22:21:32.414 | MS1 | 121.4656613619 | 31.1446328952 | 462 | 504990 | -91.61 | 17.59 | 389.29 | 0.14 | 2.54 | 1597 |
| 2024-09-20 22:21:33.839 | MS1 | 121.4656661287 | 31.1446279358 | 462 | 504990 | -90.04 | 14.28 | 580.54 | 0.18 | 2.72 | 1575 |
| 2024-09-20 22:21:34.911 | MS1 | 121.4656635929 | 31.1446193318 | 462 | 504990 | -87.95 | 14.56 | 97.98 | 0.11 | 2.94 | 353 |
| 2024-09-20 22:21:35.186 | MS1 | 121.4656587825 | 31.1446279348 | 462 | 504990 | -89.64 | 12.69 | 58.85 | 0.01 | 2.51 | 454 |
| 2024-09-20 22:21:36.596 | MS1 | 121.4656604520 | 31.1446267939 | 462 | 504990 | -88.38 | 14.54 | 67.53 | 0.20 | 2.73 | 494 |
| 2024-09-20 22:21:37.967 | MS1 | 121.4656770497 | 31.1446253448 | 462 | 504990 | -91.38 | 11.05 | 89.17 | 0.11 | 2.95 | 417 |
| 2024-09-20 22:21:38.438 | MS1 | 121.4656684711 | 31.1446244283 | 462 | 504990 | -90.96 | 12.36 | 91.36 | 0.18 | 2.85 | 358 |
| 2024-09-20 22:21:39.956 | MS1 | 121.4656653418 | 31.1446289093 | 462 | 504990 | -93.72 | 10.37 | 101.34 | 0.11 | 2.18 | 446 |
| 2024-09-20 22:21:40.947 | MS1 | 121.4656688698 | 31.1446206292 | 462 | 504990 | -93.33 | 10.26 | 567.26 | 0.04 | 2.16 | 1586 |
| 2024-09-20 22:21:41.882 | MS1 | 121.4656665337 | 31.1446353066 | 462 | 504990 | -93.70 | 9.90 | 368.07 | 0.16 | 2.11 | 1572 |
| 2024-09-20 22:21:42.286 | MS1 | 121.4656670584 | 31.1446269758 | 462 | 504990 | -90.14 | 10.69 | 367.18 | 0.02 | 2.49 | 1585 |

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
| 3216162 | 4 | 121.4734685090 | 31.1538641529 | 146 | 10 | 3 | 48.3 | TDD | 462 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3229733 | 3 | 121.4743587598 | 31.1477333754 | 266 | 15 | 1 | 24.1 | TDD | 955 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3239347 | 2 | 121.4746989827 | 31.1442564203 | 308 | 14 | 0 | 26.1 | TDD | 497 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3275565 | 1 | 121.4668503723 | 31.1458271708 | 295 | 5 | 8 | 34.0 | TDD | 584 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.953 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.976 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.110 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.110 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.849 | NREventA3 | measId:2;ServCellPCI:991;Se... |
| 2024-09-20 22:21:38.089 | NRHandoverAttempt | SourcePCI:991;SourceNR-ARFC... |
| 2024-09-20 22:21:38.123 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.138 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.238 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.238 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275565 | 1 | 5.0210 | 5.3133 | -115.3014 | 9.1373 | 179.3246 | 0.0086 | 0.0175 |
| 2024_09_20 22:00 | 3239347 | 2 | 12.2073 | 5.8881 | -116.4607 | 13.6651 | 199.9390 | 0.0174 | 0.0158 |
| 2024_09_20 22:00 | 3229733 | 3 | 5.6736 | 8.2589 | -115.2706 | 13.9280 | 91.6524 | 0.0122 | 0.0104 |
| 2024_09_20 22:00 | 3216162 | 4 | 17.8566 | 13.8544 | -114.6020 | 8.3703 | 104.2127 | 0.0066 | 0.0066 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413341_20171A5B | 504990 | 462 | -86.4 | 504990 | 955 | -87.7 | 504990 | 584 | -95.9 | 504990 | 497 |
| MR_1774413341_0C84EB5E | 504990 | 462 | -87.4 | 504990 | 955 | -88.0 | 504990 | 584 | -94.3 | 504990 | 497 |
| MR_1774413341_30DED2E8 | 504990 | 462 | -87.1 | 504990 | 955 | -89.4 | 504990 | 584 | -93.3 | 504990 | 497 |
| MR_1774413341_BF35A28D | 504990 | 462 | -88.6 | 504990 | 955 | -87.2 | 504990 | 584 | -95.5 | 504990 | 497 |
| MR_1774413341_06225EE9 | 504990 | 462 | -87.9 | 504990 | 955 | -90.2 | 504990 | 584 | -95.2 | 504990 | 497 |
| MR_1774413341_B633B3D2 | 504990 | 462 | -89.4 | 504990 | 955 | -86.9 | 504990 | 584 | -92.8 | 504990 | 497 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 75: `2cb1a364-0be...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2cb1a364-0be3-4fde-800b-076b80ec8140` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[75] topology](images/test_0075.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3214532_1
- `C2`: Increase transmission power for 3214532_1
- `C3`: Lift the tilt angle of 3214532_1 by 6 degrees
- `C4`: Add neighbor relationship between 3214532_1 and 3256276_3
- `C5`: Decrease transmission power for 3256276_3
- `C6`: Decrease A3 Offset threshold for 3214532_1
- `C7`: Lift the tilt angle  of 3279070_4 by 10 degrees
- `C8`: Decrease transmission power for 3214532_1
- `C9`: Decrease A3 Offset threshold for 3256276_3
- `C10`: Check test server and transmission issues
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214532_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214532_1
- `C13`: Press down the tilt angle of 3214532_1 by 6 degrees
- `C14`: Adjust the azimuth of 3279070_4 by 50 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256276_3
- `C16`: Add neighbor relationship between 3279070_4 and 3256276_3
- `C17`: Press down the tilt angle  of 3279070_4 by 10 degrees
- `C18`: Increase A3 Offset threshold for 3256276_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256276_3
- `C20`: Increase transmission power for 3256276_3
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Adjust the azimuth of 3214532_1 by 30 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.945 | MS1 | 121.4656732165 | 31.1446261588 | 424 | 504990 | -89.19 | 15.83 | 348.94 | 0.07 | 2.19 | 1565 |
| 2024-09-20 22:21:32.100 | MS1 | 121.4656618870 | 31.1446298013 | 424 | 504990 | -91.66 | 12.60 | 513.94 | 0.13 | 2.46 | 1593 |
| 2024-09-20 22:21:33.912 | MS1 | 121.4656607364 | 31.1446214419 | 424 | 504990 | -86.42 | 15.34 | 496.57 | 0.00 | 2.35 | 1566 |
| 2024-09-20 22:21:34.709 | MS1 | 121.4656634607 | 31.1446203830 | 424 | 504990 | -87.04 | 17.51 | 78.04 | 0.17 | 2.49 | 1589 |
| 2024-09-20 22:21:35.506 | MS1 | 121.4656685457 | 31.1446304597 | 424 | 504990 | -86.41 | 12.45 | 51.00 | 0.20 | 2.34 | 1587 |
| 2024-09-20 22:21:36.538 | MS1 | 121.4656622873 | 31.1446348115 | 424 | 504990 | -86.87 | 12.91 | 76.69 | 0.04 | 2.75 | 1579 |
| 2024-09-20 22:21:37.376 | MS1 | 121.4656623696 | 31.1446276854 | 424 | 504990 | -90.02 | 12.60 | 76.43 | 0.04 | 2.48 | 1599 |
| 2024-09-20 22:21:38.910 | MS1 | 121.4656701225 | 31.1446286900 | 424 | 504990 | -90.14 | 12.46 | 99.90 | 0.15 | 2.30 | 1589 |
| 2024-09-20 22:21:39.630 | MS1 | 121.4656611292 | 31.1446357895 | 424 | 504990 | -93.39 | 12.01 | 86.41 | 0.16 | 2.94 | 1579 |
| 2024-09-20 22:21:40.647 | MS1 | 121.4656734605 | 31.1446207478 | 424 | 504990 | -89.70 | 7.33 | 459.41 | 0.16 | 2.95 | 1570 |
| 2024-09-20 22:21:41.317 | MS1 | 121.4656655008 | 31.1446190817 | 424 | 504990 | -93.39 | 10.47 | 375.14 | 0.04 | 2.56 | 1597 |
| 2024-09-20 22:21:42.754 | MS1 | 121.4656644535 | 31.1446199797 | 424 | 504990 | -93.34 | 9.98 | 398.89 | 0.18 | 2.05 | 1590 |

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
| 3214532 | 1 | 121.4644830537 | 31.1509367399 | 201 | 3 | 5 | 33.1 | TDD | 424 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3234653 | 2 | 121.4649403912 | 31.1471736488 | 312 | 4 | 2 | 47.3 | TDD | 1001 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3256276 | 3 | 121.4701961385 | 31.1531006489 | 39 | 15 | 8 | 25.7 | TDD | 68 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3279070 | 4 | 121.4680551472 | 31.1519632499 | 52 | 2 | 7 | 18.1 | TDD | 71 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.140 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.160 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.267 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.267 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.947 | NREventA3 | measId:2;ServCellPCI:287;Se... |
| 2024-09-20 22:21:38.187 | NRHandoverAttempt | SourcePCI:287;SourceNR-ARFC... |
| 2024-09-20 22:21:38.233 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.247 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.386 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.386 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214532 | 1 | 76.1099 | 75.0950 | -114.4872 | 14.2986 | 131.5444 | 0.0180 | 0.0107 |
| 2024_09_20 22:00 | 3234653 | 2 | 11.1419 | 15.8725 | -115.5699 | 10.8987 | 83.1637 | 0.0120 | 0.0125 |
| 2024_09_20 22:00 | 3256276 | 3 | 11.3971 | 18.3022 | -116.0248 | 10.5813 | 88.5530 | 0.0080 | 0.0019 |
| 2024_09_20 22:00 | 3279070 | 4 | 14.0189 | 6.9174 | -116.3963 | 9.1195 | 169.6342 | 0.0031 | 0.0175 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413980_C5680733 | 504990 | 424 | -88.0 | 504990 | 68 | -88.7 | 504990 | 71 | -94.8 | 504990 | 1001 |
| MR_1774413980_22435669 | 504990 | 424 | -85.9 | 504990 | 68 | -90.0 | 504990 | 71 | -96.2 | 504990 | 1001 |
| MR_1774413980_FD99B5D3 | 504990 | 424 | -87.1 | 504990 | 68 | -88.2 | 504990 | 71 | -93.2 | 504990 | 1001 |
| MR_1774413980_AC356BA7 | 504990 | 424 | -88.2 | 504990 | 68 | -88.8 | 504990 | 71 | -95.4 | 504990 | 1001 |
| MR_1774413980_A4C3A955 | 504990 | 424 | -89.0 | 504990 | 68 | -88.1 | 504990 | 71 | -96.0 | 504990 | 1001 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 76: `1dbd6c19-939...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1dbd6c19-9395-4f11-872b-0a95dca72228` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[76] topology](images/test_0076.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3262616_2 and 3228523_3
- `C2`: Check test server and transmission issues
- `C3`: Decrease transmission power for 3228523_3
- `C4`: Adjust the azimuth of 3228523_3 by 8 degrees
- `C5`: Decrease A3 Offset threshold for 3228523_3
- `C6`: Increase transmission power for 3228523_3
- `C7`: Press down the tilt angle of 3262616_2 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3262616_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228523_3
- `C10`: Increase A3 Offset threshold for 3228523_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262616_2
- `C12`: Lift the tilt angle  of 3228523_3 by 10 degrees
- `C13`: Increase A3 Offset threshold for 3262616_2
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Adjust the azimuth of 3262616_2 by 50 degrees
- `C16`: Decrease transmission power for 3262616_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228523_3
- `C18`: Add neighbor relationship between 3253549_4 and 3228523_3
- `C19`: Lift the tilt angle of 3262616_2 by 10 degrees
- `C20`: Press down the tilt angle  of 3228523_3 by 10 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262616_2
- `C22`: Increase transmission power for 3262616_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.787 | MS1 | 121.4656670470 | 31.1446297545 | 875 | 504990 | -78.07 | 12.21 | 536.05 | 0.13 | 2.73 | 1592 |
| 2024-09-20 22:21:32.626 | MS1 | 121.4656745473 | 31.1446249370 | 875 | 504990 | -82.68 | 17.10 | 544.67 | 0.15 | 2.57 | 1597 |
| 2024-09-20 22:21:33.605 | MS1 | 121.4656694296 | 31.1446285161 | 875 | 504990 | -75.23 | 14.44 | 496.83 | 0.07 | 2.02 | 1591 |
| 2024-09-20 22:21:34.385 | MS1 | 121.4656737405 | 31.1446345402 | 875 | 504990 | -83.36 | -0.27 | 50.80 | 0.12 | 1.42 | 1588 |
| 2024-09-20 22:21:35.698 | MS1 | 121.4656589426 | 31.1446209034 | 875 | 504990 | -91.30 | -1.83 | 56.80 | 0.08 | 1.06 | 1574 |
| 2024-09-20 22:21:36.284 | MS1 | 121.4656631760 | 31.1446348679 | 875 | 504990 | -89.11 | -3.90 | 70.65 | 0.01 | 1.41 | 1566 |
| 2024-09-20 22:21:37.198 | MS1 | 121.4656605050 | 31.1446184206 | 875 | 504990 | -89.34 | -1.64 | 61.38 | 0.05 | 1.05 | 1566 |
| 2024-09-20 22:21:38.967 | MS1 | 121.4656734624 | 31.1446364307 | 875 | 504990 | -87.43 | -0.39 | 32.90 | 0.05 | 1.06 | 1585 |
| 2024-09-20 22:21:39.674 | MS1 | 121.4656659115 | 31.1446350418 | 844 | 504990 | -81.68 | 13.77 | 187.34 | 0.14 | 1.01 | 1574 |
| 2024-09-20 22:21:40.978 | MS1 | 121.4656746169 | 31.1446303650 | 844 | 504990 | -84.39 | 12.07 | 454.09 | 0.16 | 2.65 | 1577 |
| 2024-09-20 22:21:41.254 | MS1 | 121.4656697625 | 31.1446197516 | 844 | 504990 | -83.84 | 14.15 | 301.47 | 0.02 | 2.17 | 1579 |
| 2024-09-20 22:21:42.486 | MS1 | 121.4656747717 | 31.1446362945 | 844 | 504990 | -79.00 | 15.51 | 387.21 | 0.09 | 2.34 | 1572 |

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
| 3212508 | 1 | 121.4669536901 | 31.1464479187 | 106 | 13 | 2 | 46.6 | TDD | 785 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3228523 | 3 | 121.4661048748 | 31.1449248258 | 240 | 12 | 10 | 36.9 | TDD | 844 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3253549 | 4 | 121.4745497619 | 31.1544837962 | 130 | 15 | 7 | 22.8 | TDD | 723 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3262616 | 2 | 121.4665471225 | 31.1551484143 | 298 | 9 | 8 | 47.0 | TDD | 875 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.433 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.450 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.551 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.551 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.304 | NREventA3 | measId:2;ServCellPCI:853;Se... |
| 2024-09-20 22:21:38.544 | NRHandoverAttempt | SourcePCI:853;SourceNR-ARFC... |
| 2024-09-20 22:21:38.580 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.590 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.725 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.725 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212508 | 1 | 10.8588 | 14.6061 | -117.3554 | 12.0151 | 147.3011 | 0.0119 | 0.0086 |
| 2024_09_20 22:00 | 3262616 | 2 | 13.1927 | 14.9867 | -115.4974 | 10.4260 | 87.7265 | 0.0053 | 0.1501 |
| 2024_09_20 22:00 | 3228523 | 3 | 17.9103 | 13.3239 | -116.4487 | 16.5906 | 83.3021 | 0.0153 | 0.0085 |
| 2024_09_20 22:00 | 3253549 | 4 | 13.7532 | 9.7878 | -116.9559 | 14.7050 | 114.7408 | 0.0190 | 0.0099 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417071_8BFFF650 | 504990 | 844 | -79.4 | 504990 | 875 | -82.8 | 504990 | 723 | -90.1 | 504990 | 785 |
| MR_1774417071_DD91449D | 504990 | 875 | -83.1 | 504990 | 844 | -80.1 | 504990 | 723 | -89.0 | 504990 | 785 |
| MR_1774417071_DFE97EFE | 504990 | 844 | -77.5 | 504990 | 875 | -83.2 | 504990 | 723 | -88.3 | 504990 | 785 |
| MR_1774417071_DF382480 | 504990 | 844 | -80.5 | 504990 | 875 | -82.3 | 504990 | 723 | -87.1 | 504990 | 785 |
| MR_1774417071_AB5B90EE | 504990 | 844 | -81.0 | 504990 | 875 | -84.3 | 504990 | 723 | -88.3 | 504990 | 785 |
| MR_1774417071_6373ACC8 | 504990 | 875 | -81.4 | 504990 | 844 | -81.0 | 504990 | 723 | -87.6 | 504990 | 785 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 77: `399e0ae7-028...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `399e0ae7-0286-4c48-bd6e-099b9bc15922` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[77] topology](images/test_0077.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242478_1
- `C2`: Increase A3 Offset threshold for 3243051_3
- `C3`: Increase transmission power for 3242478_1
- `C4`: Increase A3 Offset threshold for 3242478_1
- `C5`: Increase transmission power for 3243051_3
- `C6`: Adjust the azimuth of 3242478_1 by 46 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242478_1
- `C8`: Check test server and transmission issues
- `C9`: Press down the tilt angle  of 3242478_1 by 3 degrees
- `C10`: Adjust the azimuth of 3243051_3 by 6 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Lift the tilt angle  of 3242478_1 by 3 degrees
- `C13`: Add neighbor relationship between 3269948_2 and 3242478_1
- `C14`: Decrease A3 Offset threshold for 3243051_3
- `C15`: Decrease transmission power for 3243051_3
- `C16`: Decrease A3 Offset threshold for 3242478_1
- `C17`: Lift the tilt angle of 3243051_3 by 10 degrees
- `C18`: Decrease transmission power for 3242478_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243051_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243051_3
- `C21`: Add neighbor relationship between 3243051_3 and 3242478_1
- `C22`: Press down the tilt angle of 3243051_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.189 | MS1 | 121.4656773106 | 31.1446363048 | 285 | 504990 | -80.09 | 13.18 | 342.13 | 0.08 | 2.73 | 1587 |
| 2024-09-20 22:21:32.500 | MS1 | 121.4656705093 | 31.1446351020 | 285 | 504990 | -84.66 | 12.37 | 419.18 | 0.00 | 2.53 | 1566 |
| 2024-09-20 22:21:33.700 | MS1 | 121.4656603933 | 31.1446361234 | 285 | 504990 | -84.94 | 17.59 | 536.95 | 0.07 | 2.34 | 1593 |
| 2024-09-20 22:21:34.561 | MS1 | 121.4656657572 | 31.1446249986 | 285 | 504990 | -86.25 | -1.80 | 55.58 | 0.08 | 1.34 | 1566 |
| 2024-09-20 22:21:35.600 | MS1 | 121.4656645284 | 31.1446338189 | 285 | 504990 | -90.48 | -2.47 | 59.31 | 0.18 | 1.28 | 1564 |
| 2024-09-20 22:21:36.539 | MS1 | 121.4656594697 | 31.1446236213 | 285 | 504990 | -88.44 | -0.74 | 44.56 | 0.17 | 1.40 | 1564 |
| 2024-09-20 22:21:37.838 | MS1 | 121.4656664306 | 31.1446210115 | 285 | 504990 | -88.31 | -1.36 | 68.07 | 0.20 | 1.07 | 1571 |
| 2024-09-20 22:21:38.157 | MS1 | 121.4656714345 | 31.1446185916 | 285 | 504990 | -79.40 | 12.00 | 544.41 | 0.04 | 1.27 | 1591 |
| 2024-09-20 22:21:39.394 | MS1 | 121.4656767462 | 31.1446349056 | 285 | 504990 | -75.07 | 15.04 | 337.53 | 0.17 | 1.24 | 1590 |
| 2024-09-20 22:21:40.504 | MS1 | 121.4656639626 | 31.1446332845 | 285 | 504990 | -79.31 | 17.44 | 508.34 | 0.02 | 2.95 | 1571 |
| 2024-09-20 22:21:41.385 | MS1 | 121.4656635582 | 31.1446297012 | 285 | 504990 | -76.40 | 13.96 | 506.49 | 0.19 | 2.25 | 1561 |
| 2024-09-20 22:21:42.280 | MS1 | 121.4656642480 | 31.1446258822 | 285 | 504990 | -76.46 | 13.98 | 553.72 | 0.19 | 2.87 | 1566 |

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
| 3237776 | 4 | 121.4695699988 | 31.1517173233 | 250 | 9 | 0 | 20.2 | TDD | 287 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3242478 | 1 | 121.4758647720 | 31.1486470553 | 199 | 1 | 11 | 40.3 | TDD | 560 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3243051 | 3 | 121.4672102618 | 31.1466435832 | 207 | 6 | 12 | 30.9 | TDD | 285 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3269948 | 2 | 121.4713411397 | 31.1507385524 | 346 | 5 | 11 | 28.4 | TDD | 145 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.552 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.575 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.722 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.722 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.366 | NREventA3 | measId:2;ServCellPCI:457;Se... |
| 2024-09-20 22:21:36.366 | NREventA3 | measId:2;ServCellPCI:457;Se... |
| 2024-09-20 22:21:37.366 | NREventA3 | measId:2;ServCellPCI:457;Se... |
| 2024-09-20 22:21:39.866 | NRRRCReestablishAttempt | PCI:457 |
| 2024-09-20 22:21:39.883 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.895 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:40.015 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.015 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242478 | 1 | 14.8612 | 18.0757 | -114.6733 | 13.3714 | 134.2798 | 0.0092 | 0.0143 |
| 2024_09_20 22:00 | 3269948 | 2 | 16.6444 | 19.1066 | -116.3543 | 13.1461 | 130.1229 | 0.0167 | 0.0148 |
| 2024_09_20 22:00 | 3243051 | 3 | 5.0135 | 17.4660 | -115.3435 | 8.1749 | 102.2109 | 0.0182 | 0.1854 |
| 2024_09_20 22:00 | 3237776 | 4 | 10.5325 | 19.0875 | -115.4217 | 19.4175 | 188.1556 | 0.0084 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412685_4E9E212A | 504990 | 285 | -85.8 | 504990 | 560 | -80.6 | 504990 | 145 | -91.3 | 504990 | 287 |
| MR_1774412685_674AC9AC | 504990 | 285 | -85.1 | 504990 | 560 | -79.3 | 504990 | 145 | -90.3 | 504990 | 287 |
| MR_1774412685_8C1E659B | 504990 | 285 | -85.0 | 504990 | 560 | -82.1 | 504990 | 145 | -89.8 | 504990 | 287 |
| MR_1774412685_F0237B64 | 504990 | 560 | -79.0 | 504990 | 285 | -84.4 | 504990 | 145 | -88.9 | 504990 | 287 |
| MR_1774412685_2A0B4A66 | 504990 | 285 | -87.8 | 504990 | 560 | -82.1 | 504990 | 145 | -90.3 | 504990 | 287 |
| MR_1774412685_637C200C | 504990 | 285 | -84.7 | 504990 | 560 | -82.7 | 504990 | 145 | -89.1 | 504990 | 287 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 78: `3d419e73-67a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3d419e73-67a1-4ac3-841e-f67088ddb14e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[78] topology](images/test_0078.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3266550_1
- `C2`: Check test server and transmission issues
- `C3`: Decrease transmission power for 3266550_1
- `C4`: Decrease transmission power for 3268437_2
- `C5`: Decrease A3 Offset threshold for 3268437_2
- `C6`: Add neighbor relationship between 3266550_1 and 3268437_2
- `C7`: Increase A3 Offset threshold for 3266550_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268437_2
- `C10`: Increase transmission power for 3268437_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266550_1
- `C12`: Adjust the azimuth of 3268437_2 by 26 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266550_1
- `C14`: Lift the tilt angle  of 3268437_2 by 10 degrees
- `C15`: Add neighbor relationship between 3216987_3 and 3268437_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268437_2
- `C17`: Press down the tilt angle of 3266550_1 by 7 degrees
- `C18`: Increase transmission power for 3266550_1
- `C19`: Lift the tilt angle of 3266550_1 by 7 degrees
- `C20`: Adjust the azimuth of 3266550_1 by 50 degrees
- `C21`: Press down the tilt angle  of 3268437_2 by 10 degrees
- `C22`: Increase A3 Offset threshold for 3268437_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.755 | MS1 | 121.4656653832 | 31.1446346369 | 439 | 504990 | -82.07 | 12.22 | 556.61 | 0.19 | 2.82 | 1585 |
| 2024-09-20 22:21:32.848 | MS1 | 121.4656701178 | 31.1446352784 | 439 | 504990 | -84.31 | 16.43 | 512.85 | 0.01 | 2.83 | 1581 |
| 2024-09-20 22:21:33.272 | MS1 | 121.4656770185 | 31.1446338574 | 439 | 504990 | -76.65 | 14.88 | 542.01 | 0.19 | 2.90 | 1597 |
| 2024-09-20 22:21:34.571 | MS1 | 121.4656701792 | 31.1446257910 | 439 | 504990 | -86.82 | -2.24 | 64.23 | 0.12 | 1.46 | 1565 |
| 2024-09-20 22:21:35.239 | MS1 | 121.4656751595 | 31.1446196380 | 439 | 504990 | -90.16 | -1.56 | 54.68 | 0.19 | 1.40 | 1565 |
| 2024-09-20 22:21:36.437 | MS1 | 121.4656650528 | 31.1446285346 | 439 | 504990 | -91.55 | -1.16 | 72.31 | 0.11 | 1.07 | 1593 |
| 2024-09-20 22:21:37.184 | MS1 | 121.4656643876 | 31.1446221542 | 439 | 504990 | -90.08 | -1.58 | 52.07 | 0.13 | 1.05 | 1597 |
| 2024-09-20 22:21:38.832 | MS1 | 121.4656694936 | 31.1446344234 | 439 | 504990 | -90.85 | -0.18 | 45.72 | 0.20 | 1.32 | 1577 |
| 2024-09-20 22:21:39.168 | MS1 | 121.4656632960 | 31.1446296590 | 787 | 504990 | -75.87 | 16.28 | 209.55 | 0.14 | 1.25 | 1566 |
| 2024-09-20 22:21:40.281 | MS1 | 121.4656616836 | 31.1446260395 | 787 | 504990 | -77.22 | 17.72 | 413.28 | 0.02 | 2.39 | 1569 |
| 2024-09-20 22:21:41.260 | MS1 | 121.4656598214 | 31.1446193132 | 787 | 504990 | -80.79 | 15.59 | 513.75 | 0.05 | 2.13 | 1569 |
| 2024-09-20 22:21:42.831 | MS1 | 121.4656734008 | 31.1446365790 | 787 | 504990 | -84.35 | 14.71 | 485.44 | 0.01 | 2.43 | 1584 |

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
| 3216987 | 3 | 121.4732285858 | 31.1539388785 | 41 | 10 | 5 | 39.8 | TDD | 295 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3239294 | 4 | 121.4662166521 | 31.1553165313 | 3 | 8 | 1 | 22.5 | TDD | 487 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3266550 | 1 | 121.4711513448 | 31.1464187527 | 158 | 3 | 8 | 37.3 | TDD | 439 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3268437 | 2 | 121.4643232380 | 31.1477585589 | 134 | 10 | 8 | 48.2 | TDD | 787 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.299 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.319 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.454 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.454 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.140 | NREventA3 | measId:2;ServCellPCI:76;Ser... |
| 2024-09-20 22:21:38.380 | NRHandoverAttempt | SourcePCI:76;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.430 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.442 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.560 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.560 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266550 | 1 | 6.3274 | 11.9065 | -114.2060 | 5.5502 | 141.4211 | 0.0056 | 0.1820 |
| 2024_09_20 22:00 | 3268437 | 2 | 19.0273 | 15.5833 | -116.2903 | 12.7453 | 173.4253 | 0.0031 | 0.0198 |
| 2024_09_20 22:00 | 3216987 | 3 | 7.5827 | 9.6386 | -116.6473 | 11.0067 | 186.8927 | 0.0093 | 0.0021 |
| 2024_09_20 22:00 | 3239294 | 4 | 16.6694 | 19.4138 | -115.2984 | 17.9852 | 189.3938 | 0.0099 | 0.0103 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411978_8E82B196 | 504990 | 439 | -86.4 | 504990 | 787 | -81.5 | 504990 | 295 | -82.1 | 504990 | 487 |
| MR_1774411978_0D01A6EA | 504990 | 439 | -85.9 | 504990 | 787 | -81.7 | 504990 | 295 | -82.6 | 504990 | 487 |
| MR_1774411978_AAA3BD42 | 504990 | 787 | -80.5 | 504990 | 439 | -88.5 | 504990 | 295 | -84.5 | 504990 | 487 |
| MR_1774411978_BB4C1C36 | 504990 | 787 | -82.4 | 504990 | 439 | -88.8 | 504990 | 295 | -84.0 | 504990 | 487 |
| MR_1774411978_B3AF281E | 504990 | 787 | -82.9 | 504990 | 439 | -88.3 | 504990 | 295 | -82.6 | 504990 | 487 |
| MR_1774411978_9D976A6D | 504990 | 787 | -80.5 | 504990 | 439 | -85.3 | 504990 | 295 | -81.8 | 504990 | 487 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 79: `4afc7315-302...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4afc7315-3021-4193-add7-5e93b94b4e15` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[79] topology](images/test_0079.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3250951_2 by 36 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase A3 Offset threshold for 3214797_1
- `C4`: Adjust the azimuth of 3214797_1 by 41 degrees
- `C5`: Add neighbor relationship between 3214797_1 and 3250951_2
- `C6`: Decrease transmission power for 3214797_1
- `C7`: Add neighbor relationship between 3229045_4 and 3250951_2
- `C8`: Check test server and transmission issues
- `C9`: Decrease A3 Offset threshold for 3214797_1
- `C10`: Increase transmission power for 3250951_2
- `C11`: Press down the tilt angle  of 3250951_2 by 3 degrees
- `C12`: Decrease A3 Offset threshold for 3250951_2
- `C13`: Lift the tilt angle  of 3250951_2 by 3 degrees
- `C14`: Decrease transmission power for 3250951_2
- `C15`: Press down the tilt angle of 3214797_1 by 10 degrees
- `C16`: Increase A3 Offset threshold for 3250951_2
- `C17`: Lift the tilt angle of 3214797_1 by 10 degrees
- `C18`: Increase transmission power for 3214797_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214797_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250951_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250951_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214797_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.223 | MS1 | 121.4656635741 | 31.1446377631 | 978 | 504990 | -86.37 | 12.64 | 339.87 | 0.01 | 2.28 | 1582 |
| 2024-09-20 22:21:32.741 | MS1 | 121.4656746217 | 31.1446242153 | 978 | 504990 | -87.57 | 12.44 | 430.74 | 0.04 | 2.85 | 1563 |
| 2024-09-20 22:21:33.565 | MS1 | 121.4656771449 | 31.1446333761 | 978 | 504990 | -87.56 | 12.32 | 553.31 | 0.10 | 2.35 | 1588 |
| 2024-09-20 22:21:34.185 | MS1 | 121.4656694908 | 31.1446231434 | 978 | 504990 | -101.85 | -0.53 | 30.95 | 0.05 | 1.32 | 1568 |
| 2024-09-20 22:21:35.885 | MS1 | 121.4656629554 | 31.1446371684 | 978 | 504990 | -109.37 | -1.51 | 67.89 | 0.04 | 1.04 | 1586 |
| 2024-09-20 22:21:36.878 | MS1 | 121.4656658879 | 31.1446222629 | 978 | 504990 | -108.91 | -0.74 | 34.50 | 0.16 | 1.48 | 1585 |
| 2024-09-20 22:21:37.654 | MS1 | 121.4656629286 | 31.1446300549 | 978 | 504990 | -103.94 | 1.68 | 74.68 | 0.00 | 1.14 | 1586 |
| 2024-09-20 22:21:38.861 | MS1 | 121.4656753580 | 31.1446379462 | 978 | 504990 | -108.02 | -0.43 | 42.82 | 0.13 | 1.13 | 1578 |
| 2024-09-20 22:21:39.567 | MS1 | 121.4656598070 | 31.1446183645 | 978 | 504990 | -107.01 | 0.41 | 79.38 | 0.01 | 1.40 | 1579 |
| 2024-09-20 22:21:40.815 | MS1 | 121.4656593211 | 31.1446283689 | 978 | 504990 | -88.87 | 12.41 | 311.16 | 0.15 | 2.81 | 1590 |
| 2024-09-20 22:21:41.686 | MS1 | 121.4656636977 | 31.1446295199 | 978 | 504990 | -91.84 | 13.20 | 391.26 | 0.18 | 2.52 | 1560 |
| 2024-09-20 22:21:42.637 | MS1 | 121.4656690204 | 31.1446268262 | 978 | 504990 | -91.19 | 17.03 | 296.71 | 0.19 | 2.03 | 1587 |

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
| 3214797 | 1 | 121.4667540615 | 31.1446852258 | 307 | 2 | 4 | 17.3 | TDD | 978 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3229045 | 4 | 121.4748523542 | 31.1446503514 | 247 | 13 | 7 | 47.3 | TDD | 766 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3250951 | 2 | 121.4733876965 | 31.1540695090 | 179 | 1 | 8 | 46.8 | TDD | 858 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3257023 | 3 | 121.4652717217 | 31.1464778616 | 327 | 2 | 11 | 35.9 | TDD | 134 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.610 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.631 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.764 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.764 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.919 | NREventA2 | measId:1;ServCellPCI:107;Se... |
| 2024-09-20 22:21:35.047 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214797 | 1 | 10.3317 | 12.7533 | -114.1520 | 7.1208 | 131.5107 | 0.1406 | 0.0118 |
| 2024_09_20 22:00 | 3250951 | 2 | 16.1605 | 16.0781 | -116.0282 | 18.1296 | 126.0946 | 0.0020 | 0.0108 |
| 2024_09_20 22:00 | 3257023 | 3 | 6.0270 | 13.9928 | -117.6327 | 6.6855 | 149.5539 | 0.0195 | 0.0072 |
| 2024_09_20 22:00 | 3229045 | 4 | 7.3226 | 16.8030 | -116.9866 | 18.7220 | 165.0756 | 0.0080 | 0.0104 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416420_4AD05922 | 504990 | 978 | -103.1 | 504990 | 858 | -107.4 | 504990 | 766 | -114.2 | 504990 | 134 |
| MR_1774416420_3F0B5414 | 504990 | 978 | -101.1 | 504990 | 858 | -104.3 | 504990 | 766 | -112.5 | 504990 | 134 |
| MR_1774416420_BFDC66E0 | 504990 | 978 | -100.2 | 504990 | 858 | -105.7 | 504990 | 766 | -113.9 | 504990 | 134 |
| MR_1774416420_58BF33FD | 504990 | 978 | -100.9 | 504990 | 858 | -108.1 | 504990 | 766 | -112.4 | 504990 | 134 |
| MR_1774416420_7328D2EB | 504990 | 978 | -102.3 | 504990 | 858 | -106.7 | 504990 | 766 | -113.8 | 504990 | 134 |
| MR_1774416420_4FABAADD | 504990 | 978 | -100.2 | 504990 | 858 | -106.4 | 504990 | 766 | -111.7 | 504990 | 134 |

> *... 2개 열 생략 (전체 14열)*

---
