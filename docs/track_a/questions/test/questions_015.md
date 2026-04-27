# Track A 문제 분석 — test[140]~test[149]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[140] ~ test[149] (10개)

## 목차

1. [문제 140: `f6b40ef4-7e2...`](#140) — single-answer
2. [문제 141: `805c01e9-c1c...`](#141) — single-answer
3. [문제 142: `2d45b5cf-c10...`](#142) — single-answer
4. [문제 143: `1d8947b0-713...`](#143) — single-answer
5. [문제 144: `aafaf462-2e1...`](#144) — single-answer
6. [문제 145: `060a207b-591...`](#145) — single-answer
7. [문제 146: `9158917d-348...`](#146) — single-answer
8. [문제 147: `8be2f8b9-6be...`](#147) — single-answer
9. [문제 148: `2693d888-edf...`](#148) — single-answer
10. [문제 149: `49f218ff-162...`](#149) — single-answer

---

### 문제 140: `f6b40ef4-7e2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f6b40ef4-7e29-46df-bc31-74e4d0109ef3` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[140] topology](images/test_0140.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3232715_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232715_3
- `C3`: Add neighbor relationship between 3211666_4 and 3266745_1
- `C4`: Decrease A3 Offset threshold for 3232715_3
- `C5`: Press down the tilt angle  of 3266745_1 by 5 degrees
- `C6`: Lift the tilt angle of 3232715_3 by 10 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266745_1
- `C8`: Decrease transmission power for 3266745_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232715_3
- `C10`: Increase A3 Offset threshold for 3266745_1
- `C11`: Decrease transmission power for 3232715_3
- `C12`: Adjust the azimuth of 3266745_1 by 21 degrees
- `C13`: Add neighbor relationship between 3232715_3 and 3266745_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266745_1
- `C15`: Press down the tilt angle of 3232715_3 by 10 degrees
- `C16`: Increase transmission power for 3266745_1
- `C17`: Check test server and transmission issues
- `C18`: Increase transmission power for 3232715_3
- `C19`: Lift the tilt angle  of 3266745_1 by 5 degrees
- `C20`: Decrease A3 Offset threshold for 3266745_1
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Adjust the azimuth of 3232715_3 by 19 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.974 | MS1 | 121.4656603480 | 31.1446274052 | 223 | 504990 | -84.64 | 13.72 | 534.21 | 0.10 | 2.83 | 1600 |
| 2024-09-20 22:21:32.338 | MS1 | 121.4656756303 | 31.1446350197 | 223 | 504990 | -84.25 | 15.70 | 568.97 | 0.01 | 2.70 | 1572 |
| 2024-09-20 22:21:33.495 | MS1 | 121.4656756267 | 31.1446284367 | 223 | 504990 | -78.55 | 17.31 | 598.57 | 0.11 | 2.72 | 1575 |
| 2024-09-20 22:21:34.880 | MS1 | 121.4656763398 | 31.1446300040 | 223 | 504990 | -89.38 | -3.31 | 45.77 | 0.11 | 1.12 | 1593 |
| 2024-09-20 22:21:35.475 | MS1 | 121.4656614394 | 31.1446198380 | 223 | 504990 | -90.33 | -3.64 | 38.98 | 0.18 | 1.23 | 1572 |
| 2024-09-20 22:21:36.548 | MS1 | 121.4656695946 | 31.1446335135 | 223 | 504990 | -86.74 | -2.02 | 36.67 | 0.12 | 1.46 | 1576 |
| 2024-09-20 22:21:37.945 | MS1 | 121.4656683170 | 31.1446304626 | 223 | 504990 | -86.39 | -3.45 | 61.30 | 0.06 | 1.15 | 1562 |
| 2024-09-20 22:21:38.581 | MS1 | 121.4656779301 | 31.1446323046 | 223 | 504990 | -76.90 | 12.66 | 330.68 | 0.09 | 1.17 | 1567 |
| 2024-09-20 22:21:39.310 | MS1 | 121.4656649317 | 31.1446245366 | 223 | 504990 | -79.45 | 14.97 | 557.03 | 0.08 | 1.04 | 1561 |
| 2024-09-20 22:21:40.536 | MS1 | 121.4656705676 | 31.1446348176 | 223 | 504990 | -75.51 | 16.36 | 508.94 | 0.06 | 2.66 | 1585 |
| 2024-09-20 22:21:41.496 | MS1 | 121.4656630329 | 31.1446199563 | 223 | 504990 | -77.56 | 13.58 | 291.86 | 0.15 | 2.19 | 1572 |
| 2024-09-20 22:21:42.762 | MS1 | 121.4656581495 | 31.1446365072 | 223 | 504990 | -75.34 | 12.57 | 540.57 | 0.09 | 2.73 | 1574 |

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
| 3211666 | 4 | 121.4676888197 | 31.1446183448 | 88 | 14 | 10 | 36.0 | TDD | 767 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3232715 | 3 | 121.4694052552 | 31.1547691189 | 179 | 12 | 8 | 43.9 | TDD | 223 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3253114 | 2 | 121.4663431240 | 31.1501076911 | 124 | 9 | 10 | 30.2 | TDD | 826 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3266745 | 1 | 121.4700004722 | 31.1467565121 | 219 | 2 | 3 | 21.1 | TDD | 137 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.897 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.918 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.028 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.028 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.786 | NREventA3 | measId:2;ServCellPCI:426;Se... |
| 2024-09-20 22:21:35.786 | NREventA3 | measId:2;ServCellPCI:426;Se... |
| 2024-09-20 22:21:36.786 | NREventA3 | measId:2;ServCellPCI:426;Se... |
| 2024-09-20 22:21:39.286 | NRRRCReestablishAttempt | PCI:426 |
| 2024-09-20 22:21:39.303 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.314 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.461 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.461 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266745 | 1 | 5.3584 | 16.5370 | -114.9717 | 15.4848 | 168.6376 | 0.0172 | 0.0155 |
| 2024_09_20 22:00 | 3253114 | 2 | 8.2238 | 17.7668 | -117.6680 | 10.7112 | 187.8744 | 0.0140 | 0.0147 |
| 2024_09_20 22:00 | 3232715 | 3 | 8.4064 | 11.6832 | -115.2044 | 8.9153 | 90.1612 | 0.0070 | 0.1517 |
| 2024_09_20 22:00 | 3211666 | 4 | 13.3278 | 14.2237 | -117.3216 | 8.9832 | 134.0711 | 0.0121 | 0.0011 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413569_F592C286 | 504990 | 223 | -88.6 | 504990 | 137 | -83.5 | 504990 | 767 | -88.9 | 504990 | 826 |
| MR_1774413569_274AE40C | 504990 | 137 | -85.6 | 504990 | 223 | -89.3 | 504990 | 767 | -89.9 | 504990 | 826 |
| MR_1774413569_C75837FE | 504990 | 137 | -85.5 | 504990 | 223 | -91.3 | 504990 | 767 | -91.6 | 504990 | 826 |
| MR_1774413569_85BA5928 | 504990 | 137 | -85.4 | 504990 | 223 | -88.7 | 504990 | 767 | -90.7 | 504990 | 826 |
| MR_1774413569_DFFD8F9F | 504990 | 137 | -84.6 | 504990 | 223 | -90.2 | 504990 | 767 | -90.4 | 504990 | 826 |
| MR_1774413569_E20E05F3 | 504990 | 223 | -87.6 | 504990 | 137 | -86.0 | 504990 | 767 | -91.9 | 504990 | 826 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 141: `805c01e9-c1c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `805c01e9-c1cf-48d8-b0c3-7a6d13b00695` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[141] topology](images/test_0141.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3238942_2
- `C2`: Adjust the azimuth of 3238942_2 by 3 degrees
- `C3`: Add neighbor relationship between 3257142_3 and 3238942_2
- `C4`: Increase A3 Offset threshold for 3238942_2
- `C5`: Decrease transmission power for 3238942_2
- `C6`: Lift the tilt angle of 3257142_3 by 6 degrees
- `C7`: Press down the tilt angle of 3257142_3 by 6 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238942_2
- `C9`: Decrease A3 Offset threshold for 3238942_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase A3 Offset threshold for 3257142_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257142_3
- `C13`: Decrease transmission power for 3257142_3
- `C14`: Increase transmission power for 3257142_3
- `C15`: Adjust the azimuth of 3257142_3 by 50 degrees
- `C16`: Add neighbor relationship between 3218881_1 and 3238942_2
- `C17`: Decrease A3 Offset threshold for 3257142_3
- `C18`: Lift the tilt angle  of 3238942_2 by 10 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238942_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257142_3
- `C21`: Check test server and transmission issues
- `C22`: Press down the tilt angle  of 3238942_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.188 | MS1 | 121.4656697407 | 31.1446266894 | 6 | 504990 | -81.47 | 17.10 | 525.82 | 0.19 | 2.80 | 1572 |
| 2024-09-20 22:21:32.647 | MS1 | 121.4656631871 | 31.1446214882 | 6 | 504990 | -81.72 | 17.15 | 511.03 | 0.14 | 2.37 | 1580 |
| 2024-09-20 22:21:33.224 | MS1 | 121.4656639753 | 31.1446263533 | 6 | 504990 | -82.76 | 15.78 | 558.26 | 0.18 | 2.48 | 1575 |
| 2024-09-20 22:21:34.596 | MS1 | 121.4656680490 | 31.1446195989 | 6 | 504990 | -90.15 | -1.17 | 62.73 | 0.15 | 1.05 | 1569 |
| 2024-09-20 22:21:35.335 | MS1 | 121.4656654125 | 31.1446277764 | 6 | 504990 | -91.17 | -1.53 | 60.56 | 0.20 | 1.34 | 1568 |
| 2024-09-20 22:21:36.240 | MS1 | 121.4656778047 | 31.1446250160 | 6 | 504990 | -83.03 | -0.52 | 41.97 | 0.19 | 1.01 | 1595 |
| 2024-09-20 22:21:37.516 | MS1 | 121.4656728763 | 31.1446293296 | 6 | 504990 | -90.74 | -1.31 | 47.37 | 0.14 | 1.11 | 1597 |
| 2024-09-20 22:21:38.372 | MS1 | 121.4656702168 | 31.1446243807 | 6 | 504990 | -87.50 | -1.09 | 68.55 | 0.18 | 1.28 | 1564 |
| 2024-09-20 22:21:39.148 | MS1 | 121.4656593161 | 31.1446214495 | 461 | 504990 | -75.38 | 17.30 | 177.57 | 0.12 | 1.29 | 1570 |
| 2024-09-20 22:21:40.745 | MS1 | 121.4656615577 | 31.1446274658 | 461 | 504990 | -81.02 | 13.24 | 368.57 | 0.15 | 2.02 | 1599 |
| 2024-09-20 22:21:41.790 | MS1 | 121.4656652204 | 31.1446311068 | 461 | 504990 | -82.30 | 12.22 | 513.99 | 0.13 | 2.11 | 1599 |
| 2024-09-20 22:21:42.842 | MS1 | 121.4656636730 | 31.1446238261 | 461 | 504990 | -77.50 | 14.47 | 423.82 | 0.07 | 2.81 | 1592 |

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
| 3218881 | 1 | 121.4666573088 | 31.1530879999 | 187 | 7 | 8 | 43.6 | TDD | 267 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3238942 | 2 | 121.4664608473 | 31.1471898195 | 192 | 8 | 2 | 19.2 | TDD | 461 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3257142 | 3 | 121.4690632327 | 31.1504939310 | 33 | 5 | 0 | 18.2 | TDD | 6 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3271726 | 4 | 121.4670493620 | 31.1511912051 | 71 | 12 | 7 | 46.5 | TDD | 445 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.317 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.342 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.470 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.470 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.172 | NREventA3 | measId:2;ServCellPCI:606;Se... |
| 2024-09-20 22:21:38.412 | NRHandoverAttempt | SourcePCI:606;SourceNR-ARFC... |
| 2024-09-20 22:21:38.454 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.468 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.580 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.580 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218881 | 1 | 8.6732 | 8.0086 | -115.5718 | 18.2123 | 100.6631 | 0.0074 | 0.0169 |
| 2024_09_20 22:00 | 3238942 | 2 | 17.9999 | 19.7030 | -116.9670 | 13.7007 | 91.0470 | 0.0043 | 0.0125 |
| 2024_09_20 22:00 | 3257142 | 3 | 13.1392 | 15.2312 | -115.6549 | 18.9735 | 177.5028 | 0.0179 | 0.1369 |
| 2024_09_20 22:00 | 3271726 | 4 | 19.4342 | 19.8380 | -116.2101 | 14.2094 | 105.6968 | 0.0116 | 0.0030 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412785_65B0758B | 504990 | 6 | -89.6 | 504990 | 461 | -84.1 | 504990 | 267 | -85.7 | 504990 | 445 |
| MR_1774412785_B0392DDC | 504990 | 461 | -86.0 | 504990 | 6 | -90.4 | 504990 | 267 | -87.6 | 504990 | 445 |
| MR_1774412785_64002558 | 504990 | 461 | -84.5 | 504990 | 6 | -90.3 | 504990 | 267 | -88.5 | 504990 | 445 |
| MR_1774412785_FCA86962 | 504990 | 461 | -85.8 | 504990 | 6 | -89.1 | 504990 | 267 | -84.6 | 504990 | 445 |
| MR_1774412785_E9FB2E31 | 504990 | 6 | -89.2 | 504990 | 461 | -84.0 | 504990 | 267 | -85.9 | 504990 | 445 |
| MR_1774412785_CEA79423 | 504990 | 6 | -90.9 | 504990 | 461 | -86.6 | 504990 | 267 | -85.8 | 504990 | 445 |
| MR_1774412785_507B69D5 | 504990 | 6 | -89.1 | 504990 | 461 | -84.5 | 504990 | 267 | -86.9 | 504990 | 445 |
| MR_1774412785_F5AF4CF8 | 504990 | 461 | -83.9 | 504990 | 6 | -89.1 | 504990 | 267 | -85.3 | 504990 | 445 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 142: `2d45b5cf-c10...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2d45b5cf-c107-42d0-b5aa-9e86e4334c2a` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[142] topology](images/test_0142.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3210518_2 and 3276137_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276137_4
- `C3`: Increase transmission power for 3275603_1
- `C4`: Adjust the azimuth of 3276137_4 by 50 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276137_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275603_1
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Increase A3 Offset threshold for 3275603_1
- `C9`: Press down the tilt angle  of 3276137_4 by 10 degrees
- `C10`: Decrease transmission power for 3275603_1
- `C11`: Press down the tilt angle of 3275603_1 by 5 degrees
- `C12`: Decrease A3 Offset threshold for 3276137_4
- `C13`: Lift the tilt angle  of 3276137_4 by 10 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275603_1
- `C15`: Decrease A3 Offset threshold for 3275603_1
- `C16`: Increase transmission power for 3276137_4
- `C17`: Decrease transmission power for 3276137_4
- `C18`: Lift the tilt angle of 3275603_1 by 5 degrees
- `C19`: Adjust the azimuth of 3275603_1 by 7 degrees
- `C20`: Check test server and transmission issues
- `C21`: Increase A3 Offset threshold for 3276137_4
- `C22`: Add neighbor relationship between 3275603_1 and 3276137_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.689 | MS1 | 121.4656769273 | 31.1446295042 | 298 | 504990 | -88.67 | 15.32 | 478.00 | 0.04 | 2.22 | 1595 |
| 2024-09-20 22:21:32.397 | MS1 | 121.4656702519 | 31.1446341728 | 298 | 504990 | -85.36 | 16.51 | 415.62 | 0.17 | 2.21 | 1565 |
| 2024-09-20 22:21:33.224 | MS1 | 121.4656580777 | 31.1446360700 | 298 | 504990 | -91.89 | 14.20 | 518.06 | 0.02 | 2.65 | 1593 |
| 2024-09-20 22:21:34.713 | MS1 | 121.4656720457 | 31.1446340499 | 298 | 504990 | -87.04 | 14.47 | 62.45 | 0.67 | 2.92 | 577 |
| 2024-09-20 22:21:35.434 | MS1 | 121.4656672984 | 31.1446276889 | 298 | 504990 | -91.66 | 17.74 | 70.63 | 0.54 | 2.93 | 565 |
| 2024-09-20 22:21:36.624 | MS1 | 121.4656596206 | 31.1446289727 | 298 | 504990 | -87.27 | 12.14 | 91.76 | 0.67 | 2.66 | 538 |
| 2024-09-20 22:21:37.846 | MS1 | 121.4656653703 | 31.1446342970 | 298 | 504990 | -89.75 | 7.75 | 88.03 | 0.67 | 2.34 | 637 |
| 2024-09-20 22:21:38.164 | MS1 | 121.4656659319 | 31.1446269371 | 298 | 504990 | -93.91 | 9.26 | 61.69 | 0.59 | 2.42 | 649 |
| 2024-09-20 22:21:39.264 | MS1 | 121.4656613562 | 31.1446292855 | 298 | 504990 | -90.96 | 11.27 | 88.41 | 0.54 | 2.11 | 549 |
| 2024-09-20 22:21:40.834 | MS1 | 121.4656775671 | 31.1446359053 | 298 | 504990 | -91.35 | 9.53 | 562.86 | 0.11 | 2.12 | 1583 |
| 2024-09-20 22:21:41.588 | MS1 | 121.4656701526 | 31.1446354229 | 298 | 504990 | -91.20 | 9.85 | 493.19 | 0.04 | 2.74 | 1575 |
| 2024-09-20 22:21:42.620 | MS1 | 121.4656697573 | 31.1446276645 | 298 | 504990 | -93.53 | 9.79 | 546.51 | 0.12 | 2.73 | 1589 |

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
| 3210518 | 2 | 121.4659906434 | 31.1469907525 | 350 | 8 | 11 | 48.2 | TDD | 643 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3225231 | 3 | 121.4651230018 | 31.1447199442 | 345 | 6 | 10 | 22.8 | TDD | 598 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3275603 | 1 | 121.4640357323 | 31.1534172569 | 164 | 3 | 10 | 40.3 | TDD | 298 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3276137 | 4 | 121.4644091327 | 31.1446592490 | 301 | 4 | 6 | 15.1 | TDD | 567 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.214 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.231 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.362 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.362 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.087 | NREventA3 | measId:2;ServCellPCI:531;Se... |
| 2024-09-20 22:21:38.327 | NRHandoverAttempt | SourcePCI:531;SourceNR-ARFC... |
| 2024-09-20 22:21:38.359 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.369 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.512 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.512 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275603 | 1 | 19.2280 | 12.3775 | -116.9481 | 18.8504 | 151.7435 | 0.0050 | 0.0053 |
| 2024_09_20 22:00 | 3210518 | 2 | 10.1072 | 7.7325 | -117.1646 | 15.6879 | 113.0522 | 0.0162 | 0.0024 |
| 2024_09_20 22:00 | 3225231 | 3 | 12.9556 | 16.1280 | -115.2134 | 14.7719 | 126.3220 | 0.0010 | 0.0089 |
| 2024_09_20 22:00 | 3276137 | 4 | 6.9942 | 19.2637 | -114.0559 | 7.8652 | 86.0507 | 0.0043 | 0.0058 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413450_A8B020C5 | 504990 | 298 | -85.9 | 504990 | 567 | -93.4 | 504990 | 643 | -95.3 | 504990 | 598 |
| MR_1774413450_F885DB16 | 504990 | 298 | -87.7 | 504990 | 567 | -94.7 | 504990 | 643 | -97.0 | 504990 | 598 |
| MR_1774413450_DE2FF640 | 504990 | 298 | -86.3 | 504990 | 567 | -92.8 | 504990 | 643 | -95.1 | 504990 | 598 |
| MR_1774413450_4CAB9F83 | 504990 | 298 | -86.2 | 504990 | 567 | -95.3 | 504990 | 643 | -98.6 | 504990 | 598 |
| MR_1774413450_7E9EC4D9 | 504990 | 298 | -86.3 | 504990 | 567 | -95.1 | 504990 | 643 | -98.5 | 504990 | 598 |
| MR_1774413450_C8DAEE0C | 504990 | 298 | -88.8 | 504990 | 567 | -94.6 | 504990 | 643 | -98.1 | 504990 | 598 |
| MR_1774413450_8470CBF1 | 504990 | 298 | -85.1 | 504990 | 567 | -95.9 | 504990 | 643 | -95.2 | 504990 | 598 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 143: `1d8947b0-713...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1d8947b0-7135-45ea-b7f8-3b3e8d6512d9` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[143] topology](images/test_0143.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3253133_3
- `C2`: Increase A3 Offset threshold for 3253133_3
- `C3`: Press down the tilt angle of 3265987_1 by 5 degrees
- `C4`: Add neighbor relationship between 3214186_2 and 3253133_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265987_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253133_3
- `C7`: Decrease transmission power for 3265987_1
- `C8`: Decrease A3 Offset threshold for 3253133_3
- `C9`: Increase A3 Offset threshold for 3265987_1
- `C10`: Decrease A3 Offset threshold for 3265987_1
- `C11`: Lift the tilt angle  of 3253133_3 by 6 degrees
- `C12`: Adjust the azimuth of 3265987_1 by 47 degrees
- `C13`: Lift the tilt angle of 3265987_1 by 5 degrees
- `C14`: Press down the tilt angle  of 3253133_3 by 6 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Add neighbor relationship between 3265987_1 and 3253133_3
- `C17`: Adjust the azimuth of 3253133_3 by 7 degrees
- `C18`: Check test server and transmission issues
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253133_3
- `C20`: Increase transmission power for 3265987_1
- `C21`: Decrease transmission power for 3253133_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265987_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.806 | MS1 | 121.4656597582 | 31.1446352645 | 8 | 504990 | -80.80 | 16.37 | 450.63 | 0.17 | 2.99 | 1590 |
| 2024-09-20 22:21:32.652 | MS1 | 121.4656635771 | 31.1446343121 | 8 | 504990 | -83.68 | 15.51 | 433.00 | 0.18 | 2.36 | 1582 |
| 2024-09-20 22:21:33.579 | MS1 | 121.4656758585 | 31.1446377148 | 8 | 504990 | -76.75 | 14.50 | 561.34 | 0.09 | 2.44 | 1577 |
| 2024-09-20 22:21:34.252 | MS1 | 121.4656737701 | 31.1446342266 | 8 | 504990 | -92.69 | -1.33 | 76.13 | 0.09 | 1.28 | 1581 |
| 2024-09-20 22:21:35.208 | MS1 | 121.4656659500 | 31.1446375760 | 8 | 504990 | -91.79 | -2.89 | 45.22 | 0.09 | 1.10 | 1577 |
| 2024-09-20 22:21:36.502 | MS1 | 121.4656635254 | 31.1446308661 | 8 | 504990 | -83.77 | -0.70 | 72.17 | 0.15 | 1.02 | 1581 |
| 2024-09-20 22:21:37.856 | MS1 | 121.4656598812 | 31.1446277420 | 8 | 504990 | -87.09 | -1.13 | 30.92 | 0.04 | 1.44 | 1587 |
| 2024-09-20 22:21:38.987 | MS1 | 121.4656764763 | 31.1446267616 | 8 | 504990 | -85.22 | -0.84 | 76.33 | 0.14 | 1.17 | 1577 |
| 2024-09-20 22:21:39.412 | MS1 | 121.4656754851 | 31.1446351899 | 292 | 504990 | -75.31 | 12.65 | 279.69 | 0.06 | 1.27 | 1560 |
| 2024-09-20 22:21:40.694 | MS1 | 121.4656650453 | 31.1446317102 | 292 | 504990 | -82.40 | 16.90 | 554.29 | 0.08 | 2.38 | 1599 |
| 2024-09-20 22:21:41.381 | MS1 | 121.4656745833 | 31.1446280213 | 292 | 504990 | -83.00 | 13.58 | 389.66 | 0.15 | 2.93 | 1581 |
| 2024-09-20 22:21:42.117 | MS1 | 121.4656663129 | 31.1446264620 | 292 | 504990 | -75.73 | 17.27 | 387.92 | 0.04 | 2.24 | 1573 |

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
| 3214186 | 2 | 121.4647502202 | 31.1477637749 | 122 | 4 | 8 | 15.9 | TDD | 737 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3253133 | 3 | 121.4696048677 | 31.1486701315 | 213 | 4 | 9 | 23.9 | TDD | 292 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3265987 | 1 | 121.4738083650 | 31.1525526268 | 268 | 3 | 4 | 40.8 | TDD | 8 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3272958 | 4 | 121.4712647036 | 31.1486197038 | 264 | 1 | 9 | 19.9 | TDD | 726 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.625 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.763 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.763 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.427 | NREventA3 | measId:2;ServCellPCI:834;Se... |
| 2024-09-20 22:21:38.667 | NRHandoverAttempt | SourcePCI:834;SourceNR-ARFC... |
| 2024-09-20 22:21:38.706 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.719 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.854 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.854 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265987 | 1 | 7.3363 | 5.1338 | -117.4376 | 9.9594 | 181.5823 | 0.0099 | 0.1582 |
| 2024_09_20 22:00 | 3214186 | 2 | 17.1636 | 6.0041 | -116.4003 | 19.8749 | 153.1985 | 0.0008 | 0.0082 |
| 2024_09_20 22:00 | 3253133 | 3 | 14.6504 | 12.4387 | -115.1988 | 15.6918 | 107.6554 | 0.0038 | 0.0182 |
| 2024_09_20 22:00 | 3272958 | 4 | 10.5494 | 19.6358 | -115.4786 | 11.9221 | 91.4492 | 0.0048 | 0.0155 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415541_4EF4CB8D | 504990 | 8 | -91.9 | 504990 | 292 | -89.2 | 504990 | 737 | -89.9 | 504990 | 726 |
| MR_1774415541_A070D679 | 504990 | 8 | -94.2 | 504990 | 292 | -86.8 | 504990 | 737 | -92.6 | 504990 | 726 |
| MR_1774415541_EBE3A952 | 504990 | 8 | -91.7 | 504990 | 292 | -88.8 | 504990 | 737 | -89.9 | 504990 | 726 |
| MR_1774415541_BF78E683 | 504990 | 292 | -89.4 | 504990 | 8 | -91.7 | 504990 | 737 | -93.2 | 504990 | 726 |
| MR_1774415541_8C9D8C23 | 504990 | 8 | -93.5 | 504990 | 292 | -88.3 | 504990 | 737 | -92.6 | 504990 | 726 |
| MR_1774415541_C10F0EBF | 504990 | 292 | -86.2 | 504990 | 8 | -94.3 | 504990 | 737 | -90.7 | 504990 | 726 |
| MR_1774415541_7F81C3A9 | 504990 | 292 | -88.4 | 504990 | 8 | -91.7 | 504990 | 737 | -91.0 | 504990 | 726 |
| MR_1774415541_A4849B28 | 504990 | 292 | -88.9 | 504990 | 8 | -91.4 | 504990 | 737 | -92.4 | 504990 | 726 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 144: `aafaf462-2e1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `aafaf462-2e10-4a5a-8b9c-c8c65b656483` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[144] topology](images/test_0144.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247718_3
- `C2`: Adjust the azimuth of 3247718_3 by 19 degrees
- `C3`: Check test server and transmission issues
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279926_2
- `C5`: Adjust the azimuth of 3279926_2 by 50 degrees
- `C6`: Press down the tilt angle  of 3247718_3 by 10 degrees
- `C7`: Increase transmission power for 3247718_3
- `C8`: Decrease transmission power for 3279926_2
- `C9`: Decrease A3 Offset threshold for 3279926_2
- `C10`: Add neighbor relationship between 3250803_4 and 3247718_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247718_3
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Lift the tilt angle  of 3247718_3 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279926_2
- `C15`: Increase transmission power for 3279926_2
- `C16`: Press down the tilt angle of 3279926_2 by 10 degrees
- `C17`: Lift the tilt angle of 3279926_2 by 10 degrees
- `C18`: Increase A3 Offset threshold for 3279926_2
- `C19`: Decrease transmission power for 3247718_3
- `C20`: Decrease A3 Offset threshold for 3247718_3
- `C21`: Increase A3 Offset threshold for 3247718_3
- `C22`: Add neighbor relationship between 3279926_2 and 3247718_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.615 | MS1 | 121.4656677899 | 31.1446263257 | 921 | 504990 | -85.41 | 15.86 | 520.54 | 0.13 | 2.73 | 1585 |
| 2024-09-20 22:21:32.985 | MS1 | 121.4656756457 | 31.1446321022 | 921 | 504990 | -89.62 | 14.06 | 490.69 | 0.03 | 2.57 | 1596 |
| 2024-09-20 22:21:33.709 | MS1 | 121.4656714702 | 31.1446290518 | 921 | 504990 | -86.61 | 16.02 | 486.78 | 0.06 | 2.93 | 1587 |
| 2024-09-20 22:21:34.791 | MS1 | 121.4656625099 | 31.1446317121 | 921 | 504990 | -90.10 | 15.12 | 83.60 | 0.05 | 2.46 | 1576 |
| 2024-09-20 22:21:35.636 | MS1 | 121.4656647498 | 31.1446199696 | 921 | 504990 | -85.22 | 17.35 | 60.56 | 0.10 | 2.79 | 1576 |
| 2024-09-20 22:21:36.182 | MS1 | 121.4656779900 | 31.1446335844 | 921 | 504990 | -90.72 | 14.56 | 72.52 | 0.18 | 2.70 | 1577 |
| 2024-09-20 22:21:37.951 | MS1 | 121.4656711894 | 31.1446276453 | 921 | 504990 | -93.63 | 10.16 | 55.21 | 0.04 | 2.01 | 1590 |
| 2024-09-20 22:21:38.692 | MS1 | 121.4656644544 | 31.1446263057 | 921 | 504990 | -92.80 | 12.53 | 92.27 | 0.16 | 2.17 | 1589 |
| 2024-09-20 22:21:39.500 | MS1 | 121.4656585020 | 31.1446376386 | 921 | 504990 | -92.80 | 9.51 | 75.72 | 0.04 | 2.62 | 1573 |
| 2024-09-20 22:21:40.669 | MS1 | 121.4656752682 | 31.1446298910 | 921 | 504990 | -93.83 | 11.56 | 305.22 | 0.00 | 2.17 | 1581 |
| 2024-09-20 22:21:41.867 | MS1 | 121.4656696840 | 31.1446348681 | 921 | 504990 | -89.22 | 12.07 | 589.83 | 0.07 | 2.33 | 1592 |
| 2024-09-20 22:21:42.180 | MS1 | 121.4656590000 | 31.1446331132 | 921 | 504990 | -91.73 | 10.26 | 555.72 | 0.09 | 2.20 | 1597 |

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
| 3247718 | 3 | 121.4732269672 | 31.1493763797 | 215 | 14 | 1 | 46.3 | TDD | 180 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3250803 | 4 | 121.4726199466 | 31.1445274158 | 131 | 2 | 2 | 43.1 | TDD | 487 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3276062 | 1 | 121.4657593960 | 31.1523234291 | 316 | 12 | 4 | 36.6 | TDD | 472 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3279926 | 2 | 121.4657606402 | 31.1459757220 | 64 | 6 | 12 | 21.9 | TDD | 921 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.437 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.461 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.603 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.603 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.281 | NREventA3 | measId:2;ServCellPCI:916;Se... |
| 2024-09-20 22:21:38.521 | NRHandoverAttempt | SourcePCI:916;SourceNR-ARFC... |
| 2024-09-20 22:21:38.551 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.566 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.715 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.715 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3276062 | 1 | 80.5628 | 77.3991 | -117.7203 | 15.3040 | 137.9010 | 0.0053 | 0.0008 |
| 2024_09_19 22:00 | 3279926 | 2 | 93.7213 | 77.9193 | -116.6561 | 19.9780 | 136.6660 | 0.0128 | 0.0026 |
| 2024_09_19 22:00 | 3247718 | 3 | 86.9854 | 77.2482 | -116.0577 | 6.6394 | 96.1544 | 0.0157 | 0.0150 |
| 2024_09_19 22:00 | 3250803 | 4 | 85.9102 | 83.3720 | -117.1468 | 17.6357 | 101.5931 | 0.0152 | 0.0063 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416599_FF73240D | 504990 | 921 | -88.9 | 504990 | 180 | -92.8 | 504990 | 487 | -101.6 | 504990 | 472 |
| MR_1774416599_523218CE | 504990 | 921 | -88.3 | 504990 | 180 | -94.7 | 504990 | 487 | -103.5 | 504990 | 472 |
| MR_1774416599_B6DA9923 | 504990 | 921 | -91.0 | 504990 | 180 | -94.4 | 504990 | 487 | -103.4 | 504990 | 472 |
| MR_1774416599_73AF5559 | 504990 | 921 | -88.6 | 504990 | 180 | -94.1 | 504990 | 487 | -101.7 | 504990 | 472 |
| MR_1774416599_103159AE | 504990 | 921 | -88.9 | 504990 | 180 | -92.1 | 504990 | 487 | -103.7 | 504990 | 472 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 145: `060a207b-591...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `060a207b-5918-43e4-8b56-d1687190b4ee` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[145] topology](images/test_0145.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3269653_1
- `C2`: Adjust the azimuth of 3255566_4 by 50 degrees
- `C3`: Decrease transmission power for 3255566_4
- `C4`: Decrease A3 Offset threshold for 3269653_1
- `C5`: Add neighbor relationship between 3240147_3 and 3269653_1
- `C6`: Adjust the azimuth of 3269653_1 by 34 degrees
- `C7`: Decrease A3 Offset threshold for 3255566_4
- `C8`: Increase A3 Offset threshold for 3255566_4
- `C9`: Lift the tilt angle of 3255566_4 by 10 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255566_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269653_1
- `C12`: Increase transmission power for 3255566_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255566_4
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease transmission power for 3269653_1
- `C16`: Increase A3 Offset threshold for 3269653_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269653_1
- `C18`: Press down the tilt angle  of 3269653_1 by 3 degrees
- `C19`: Press down the tilt angle of 3255566_4 by 10 degrees
- `C20`: Add neighbor relationship between 3255566_4 and 3269653_1
- `C21`: Lift the tilt angle  of 3269653_1 by 3 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.670 | MS1 | 121.4656758433 | 31.1446282381 | 943 | 504990 | -76.49 | 16.08 | 515.41 | 0.20 | 2.03 | 1561 |
| 2024-09-20 22:21:32.445 | MS1 | 121.4656631725 | 31.1446333366 | 943 | 504990 | -80.87 | 13.24 | 377.11 | 0.05 | 2.96 | 1561 |
| 2024-09-20 22:21:33.455 | MS1 | 121.4656747196 | 31.1446361875 | 943 | 504990 | -78.73 | 13.30 | 447.69 | 0.05 | 2.11 | 1566 |
| 2024-09-20 22:21:34.932 | MS1 | 121.4656709121 | 31.1446298439 | 943 | 504990 | -91.52 | -3.74 | 54.72 | 0.06 | 1.39 | 1570 |
| 2024-09-20 22:21:35.659 | MS1 | 121.4656695309 | 31.1446348199 | 943 | 504990 | -94.26 | -2.83 | 53.93 | 0.17 | 1.29 | 1561 |
| 2024-09-20 22:21:36.283 | MS1 | 121.4656636321 | 31.1446264010 | 943 | 504990 | -87.71 | -1.70 | 52.08 | 0.06 | 1.15 | 1600 |
| 2024-09-20 22:21:37.866 | MS1 | 121.4656718336 | 31.1446224593 | 943 | 504990 | -93.60 | -0.77 | 46.85 | 0.02 | 1.24 | 1563 |
| 2024-09-20 22:21:38.934 | MS1 | 121.4656766741 | 31.1446233131 | 943 | 504990 | -82.58 | 12.63 | 557.30 | 0.03 | 1.39 | 1561 |
| 2024-09-20 22:21:39.327 | MS1 | 121.4656714681 | 31.1446362701 | 943 | 504990 | -75.74 | 14.51 | 516.79 | 0.08 | 1.29 | 1581 |
| 2024-09-20 22:21:40.578 | MS1 | 121.4656757523 | 31.1446248975 | 943 | 504990 | -78.18 | 13.51 | 495.71 | 0.05 | 2.11 | 1600 |
| 2024-09-20 22:21:41.340 | MS1 | 121.4656627600 | 31.1446316204 | 943 | 504990 | -81.01 | 13.05 | 506.06 | 0.18 | 2.99 | 1563 |
| 2024-09-20 22:21:42.473 | MS1 | 121.4656754606 | 31.1446288263 | 943 | 504990 | -81.10 | 15.55 | 603.75 | 0.12 | 2.67 | 1576 |

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
| 3214471 | 2 | 121.4670895998 | 31.1488406114 | 306 | 0 | 3 | 36.3 | TDD | 131 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3240147 | 3 | 121.4652010537 | 31.1511252285 | 331 | 12 | 11 | 26.1 | TDD | 971 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3255566 | 4 | 121.4735282599 | 31.1559135149 | 302 | 12 | 10 | 31.1 | TDD | 943 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3269653 | 1 | 121.4731201986 | 31.1511711206 | 258 | 1 | 7 | 30.5 | TDD | 323 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.388 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.407 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.519 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.519 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.240 | NREventA3 | measId:2;ServCellPCI:208;Se... |
| 2024-09-20 22:21:36.240 | NREventA3 | measId:2;ServCellPCI:208;Se... |
| 2024-09-20 22:21:37.240 | NREventA3 | measId:2;ServCellPCI:208;Se... |
| 2024-09-20 22:21:39.740 | NRRRCReestablishAttempt | PCI:208 |
| 2024-09-20 22:21:39.758 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.769 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.919 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.919 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269653 | 1 | 15.2129 | 11.6556 | -116.0936 | 18.2746 | 81.7916 | 0.0119 | 0.0159 |
| 2024_09_20 22:00 | 3214471 | 2 | 18.9515 | 18.9607 | -117.7301 | 14.1195 | 183.5094 | 0.0010 | 0.0126 |
| 2024_09_20 22:00 | 3240147 | 3 | 6.3540 | 7.4897 | -114.2550 | 14.1571 | 160.5315 | 0.0029 | 0.0090 |
| 2024_09_20 22:00 | 3255566 | 4 | 5.2247 | 8.3482 | -116.0263 | 10.7851 | 139.5309 | 0.0138 | 0.1075 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414846_23B4A434 | 504990 | 943 | -93.5 | 504990 | 323 | -85.7 | 504990 | 971 | -90.7 | 504990 | 131 |
| MR_1774414846_7DE8EAF9 | 504990 | 943 | -91.8 | 504990 | 323 | -87.5 | 504990 | 971 | -92.1 | 504990 | 131 |
| MR_1774414846_2D58B728 | 504990 | 943 | -90.8 | 504990 | 323 | -86.1 | 504990 | 971 | -91.5 | 504990 | 131 |
| MR_1774414846_E4D415C8 | 504990 | 323 | -85.8 | 504990 | 943 | -92.9 | 504990 | 971 | -91.4 | 504990 | 131 |
| MR_1774414846_0D110AD6 | 504990 | 943 | -91.7 | 504990 | 323 | -89.2 | 504990 | 971 | -90.4 | 504990 | 131 |
| MR_1774414846_DE7985DA | 504990 | 943 | -90.8 | 504990 | 323 | -89.2 | 504990 | 971 | -89.3 | 504990 | 131 |
| MR_1774414846_14D82ACA | 504990 | 943 | -89.5 | 504990 | 323 | -87.8 | 504990 | 971 | -89.3 | 504990 | 131 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 146: `9158917d-348...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9158917d-3486-4916-8121-1b5a7fc48217` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[146] topology](images/test_0146.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase transmission power for 3242961_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242961_1
- `C4`: Decrease A3 Offset threshold for 3242961_1
- `C5`: Increase transmission power for 3252404_2
- `C6`: Decrease A3 Offset threshold for 3252404_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252404_2
- `C8`: Decrease transmission power for 3242961_1
- `C9`: Increase A3 Offset threshold for 3242961_1
- `C10`: Press down the tilt angle  of 3242961_1 by 6 degrees
- `C11`: Lift the tilt angle of 3252404_2 by 10 degrees
- `C12`: Adjust the azimuth of 3242961_1 by 22 degrees
- `C13`: Lift the tilt angle  of 3242961_1 by 6 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242961_1
- `C15`: Add neighbor relationship between 3252404_2 and 3242961_1
- `C16`: Decrease transmission power for 3252404_2
- `C17`: Adjust the azimuth of 3252404_2 by 50 degrees
- `C18`: Check test server and transmission issues
- `C19`: Increase A3 Offset threshold for 3252404_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252404_2
- `C21`: Press down the tilt angle of 3252404_2 by 10 degrees
- `C22`: Add neighbor relationship between 3235648_3 and 3242961_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.507 | MS1 | 121.4656736974 | 31.1446364838 | 681 | 504990 | -80.75 | 17.50 | 583.56 | 0.19 | 2.48 | 1572 |
| 2024-09-20 22:21:32.661 | MS1 | 121.4656667097 | 31.1446352278 | 681 | 504990 | -82.23 | 16.79 | 420.45 | 0.03 | 2.70 | 1569 |
| 2024-09-20 22:21:33.613 | MS1 | 121.4656776778 | 31.1446239703 | 681 | 504990 | -76.17 | 15.33 | 579.17 | 0.03 | 2.83 | 1583 |
| 2024-09-20 22:21:34.313 | MS1 | 121.4656594429 | 31.1446249374 | 681 | 504990 | -89.48 | -3.19 | 67.97 | 0.15 | 1.33 | 1575 |
| 2024-09-20 22:21:35.822 | MS1 | 121.4656595388 | 31.1446279393 | 681 | 504990 | -92.28 | -2.12 | 73.69 | 0.06 | 1.15 | 1569 |
| 2024-09-20 22:21:36.198 | MS1 | 121.4656609862 | 31.1446344459 | 681 | 504990 | -88.97 | -1.07 | 34.85 | 0.14 | 1.16 | 1565 |
| 2024-09-20 22:21:37.741 | MS1 | 121.4656706574 | 31.1446204397 | 681 | 504990 | -85.15 | -1.80 | 26.68 | 0.12 | 1.17 | 1599 |
| 2024-09-20 22:21:38.831 | MS1 | 121.4656745259 | 31.1446259437 | 681 | 504990 | -77.22 | 13.21 | 479.76 | 0.11 | 1.09 | 1572 |
| 2024-09-20 22:21:39.974 | MS1 | 121.4656623788 | 31.1446287112 | 681 | 504990 | -79.80 | 14.19 | 461.10 | 0.11 | 1.27 | 1563 |
| 2024-09-20 22:21:40.694 | MS1 | 121.4656758029 | 31.1446307690 | 681 | 504990 | -79.88 | 17.58 | 545.52 | 0.00 | 2.01 | 1566 |
| 2024-09-20 22:21:41.940 | MS1 | 121.4656627421 | 31.1446259428 | 681 | 504990 | -81.82 | 12.69 | 497.80 | 0.01 | 2.21 | 1597 |
| 2024-09-20 22:21:42.202 | MS1 | 121.4656666005 | 31.1446189223 | 681 | 504990 | -77.17 | 13.26 | 521.34 | 0.11 | 2.92 | 1565 |

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
| 3220759 | 4 | 121.4742293854 | 31.1546049796 | 96 | 8 | 8 | 26.4 | TDD | 715 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3235648 | 3 | 121.4640665729 | 31.1523923605 | 217 | 10 | 3 | 28.9 | TDD | 11 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3242961 | 1 | 121.4667557468 | 31.1503217995 | 211 | 2 | 9 | 39.3 | TDD | 584 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3252404 | 2 | 121.4657675889 | 31.1483233445 | 328 | 10 | 3 | 47.0 | TDD | 681 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.482 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.507 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.619 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.619 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.364 | NREventA3 | measId:2;ServCellPCI:339;Se... |
| 2024-09-20 22:21:36.364 | NREventA3 | measId:2;ServCellPCI:339;Se... |
| 2024-09-20 22:21:37.364 | NREventA3 | measId:2;ServCellPCI:339;Se... |
| 2024-09-20 22:21:39.864 | NRRRCReestablishAttempt | PCI:339 |
| 2024-09-20 22:21:39.884 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.898 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:40.022 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.022 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242961 | 1 | 18.9840 | 13.7235 | -114.4273 | 11.6146 | 123.1189 | 0.0086 | 0.0008 |
| 2024_09_20 22:00 | 3252404 | 2 | 7.2623 | 15.5813 | -115.5614 | 15.7949 | 144.8526 | 0.0173 | 0.1655 |
| 2024_09_20 22:00 | 3235648 | 3 | 9.2118 | 8.3347 | -117.5482 | 5.0363 | 83.9110 | 0.0094 | 0.0125 |
| 2024_09_20 22:00 | 3220759 | 4 | 19.0912 | 5.5234 | -114.3447 | 8.2850 | 117.5226 | 0.0084 | 0.0093 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415698_3F6F5A18 | 504990 | 584 | -85.5 | 504990 | 681 | -88.7 | 504990 | 11 | -93.1 | 504990 | 715 |
| MR_1774415698_21E7065B | 504990 | 584 | -83.8 | 504990 | 681 | -88.7 | 504990 | 11 | -90.6 | 504990 | 715 |
| MR_1774415698_38B3990D | 504990 | 584 | -85.9 | 504990 | 681 | -89.1 | 504990 | 11 | -93.0 | 504990 | 715 |
| MR_1774415698_DDAD4D6B | 504990 | 681 | -90.1 | 504990 | 584 | -84.6 | 504990 | 11 | -90.9 | 504990 | 715 |
| MR_1774415698_30DBB34A | 504990 | 681 | -87.7 | 504990 | 584 | -85.4 | 504990 | 11 | -93.8 | 504990 | 715 |
| MR_1774415698_A94C7C7A | 504990 | 584 | -85.6 | 504990 | 681 | -89.5 | 504990 | 11 | -93.5 | 504990 | 715 |
| MR_1774415698_506F1C96 | 504990 | 584 | -86.9 | 504990 | 681 | -90.5 | 504990 | 11 | -91.3 | 504990 | 715 |
| MR_1774415698_504B477A | 504990 | 584 | -86.2 | 504990 | 681 | -88.6 | 504990 | 11 | -92.4 | 504990 | 715 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 147: `8be2f8b9-6be...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8be2f8b9-6be2-41de-9844-205deef92705` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[147] topology](images/test_0147.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3216433_4 by 10 degrees
- `C2`: Increase transmission power for 3216300_1
- `C3`: Lift the tilt angle  of 3216433_4 by 10 degrees
- `C4`: Check test server and transmission issues
- `C5`: Adjust the azimuth of 3216433_4 by 8 degrees
- `C6`: Add neighbor relationship between 3216300_1 and 3262041_3
- `C7`: Press down the tilt angle of 3216300_1 by 5 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase transmission power for 3262041_3
- `C10`: Decrease transmission power for 3262041_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216300_1
- `C12`: Adjust the azimuth of 3216300_1 by 41 degrees
- `C13`: Increase A3 Offset threshold for 3216300_1
- `C14`: Decrease transmission power for 3216300_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262041_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216300_1
- `C17`: Add neighbor relationship between 3216433_4 and 3262041_3
- `C18`: Decrease A3 Offset threshold for 3216300_1
- `C19`: Decrease A3 Offset threshold for 3262041_3
- `C20`: Lift the tilt angle of 3216300_1 by 5 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262041_3
- `C22`: Increase A3 Offset threshold for 3262041_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.582 | MS1 | 121.4656731355 | 31.1446299448 | 250 | 504990 | -89.24 | 17.92 | 463.91 | 0.12 | 2.50 | 1599 |
| 2024-09-20 22:21:32.486 | MS1 | 121.4656722061 | 31.1446368078 | 250 | 504990 | -87.05 | 15.89 | 481.01 | 0.05 | 2.94 | 1579 |
| 2024-09-20 22:21:33.179 | MS1 | 121.4656647161 | 31.1446214527 | 250 | 504990 | -88.31 | 14.51 | 309.28 | 0.03 | 2.51 | 1562 |
| 2024-09-20 22:21:34.998 | MS1 | 121.4656679103 | 31.1446208775 | 250 | 504990 | -85.79 | 17.27 | 68.39 | 0.00 | 2.90 | 1578 |
| 2024-09-20 22:21:35.581 | MS1 | 121.4656742635 | 31.1446355688 | 250 | 504990 | -89.16 | 16.87 | 67.63 | 0.02 | 2.72 | 1592 |
| 2024-09-20 22:21:36.854 | MS1 | 121.4656712379 | 31.1446244602 | 250 | 504990 | -90.37 | 17.26 | 91.02 | 0.01 | 2.32 | 1595 |
| 2024-09-20 22:21:37.979 | MS1 | 121.4656682647 | 31.1446308551 | 250 | 504990 | -89.96 | 8.23 | 58.12 | 0.16 | 2.67 | 1581 |
| 2024-09-20 22:21:38.511 | MS1 | 121.4656615872 | 31.1446278798 | 250 | 504990 | -92.48 | 11.15 | 63.35 | 0.02 | 2.72 | 1597 |
| 2024-09-20 22:21:39.984 | MS1 | 121.4656699111 | 31.1446306330 | 250 | 504990 | -93.81 | 8.76 | 74.69 | 0.00 | 2.60 | 1572 |
| 2024-09-20 22:21:40.383 | MS1 | 121.4656710046 | 31.1446233877 | 250 | 504990 | -93.19 | 11.29 | 422.85 | 0.10 | 2.45 | 1579 |
| 2024-09-20 22:21:41.639 | MS1 | 121.4656670556 | 31.1446363689 | 250 | 504990 | -93.39 | 9.63 | 333.53 | 0.02 | 2.30 | 1578 |
| 2024-09-20 22:21:42.357 | MS1 | 121.4656663585 | 31.1446211893 | 250 | 504990 | -90.70 | 8.98 | 383.80 | 0.20 | 2.71 | 1583 |

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
| 3216300 | 1 | 121.4747450484 | 31.1468696676 | 213 | 4 | 12 | 19.5 | TDD | 250 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3216433 | 4 | 121.4656220513 | 31.1536808468 | 22 | 15 | 12 | 16.5 | TDD | 882 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3238353 | 2 | 121.4757009797 | 31.1492713529 | 187 | 3 | 0 | 48.1 | TDD | 419 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3262041 | 3 | 121.4710799411 | 31.1468209270 | 237 | 7 | 5 | 48.5 | TDD | 114 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.488 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.513 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.614 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.614 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.319 | NREventA3 | measId:2;ServCellPCI:354;Se... |
| 2024-09-20 22:21:38.559 | NRHandoverAttempt | SourcePCI:354;SourceNR-ARFC... |
| 2024-09-20 22:21:38.592 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.603 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.729 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.729 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216300 | 1 | 87.8434 | 92.8282 | -116.2556 | 17.0608 | 97.9611 | 0.0065 | 0.0014 |
| 2024_09_20 22:00 | 3238353 | 2 | 17.9569 | 12.3381 | -114.2206 | 5.1911 | 138.4285 | 0.0098 | 0.0172 |
| 2024_09_20 22:00 | 3262041 | 3 | 18.3522 | 11.2903 | -117.1728 | 12.9099 | 184.7691 | 0.0024 | 0.0122 |
| 2024_09_20 22:00 | 3216433 | 4 | 7.6195 | 12.7532 | -117.7026 | 11.6519 | 93.6982 | 0.0149 | 0.0123 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415996_D555BDC9 | 504990 | 250 | -87.7 | 504990 | 114 | -88.4 | 504990 | 882 | -93.3 | 504990 | 419 |
| MR_1774415996_00E64A00 | 504990 | 250 | -83.9 | 504990 | 114 | -87.4 | 504990 | 882 | -94.6 | 504990 | 419 |
| MR_1774415996_85299838 | 504990 | 250 | -85.9 | 504990 | 114 | -87.4 | 504990 | 882 | -94.0 | 504990 | 419 |
| MR_1774415996_AF7767F6 | 504990 | 250 | -85.8 | 504990 | 114 | -87.1 | 504990 | 882 | -96.7 | 504990 | 419 |
| MR_1774415996_947AB921 | 504990 | 250 | -86.5 | 504990 | 114 | -86.3 | 504990 | 882 | -93.7 | 504990 | 419 |
| MR_1774415996_17557776 | 504990 | 250 | -84.2 | 504990 | 114 | -87.5 | 504990 | 882 | -96.3 | 504990 | 419 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 148: `2693d888-edf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2693d888-edf7-4070-976d-68a1b5191e37` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[148] topology](images/test_0148.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3275612_1 by 8 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269907_2
- `C3`: Press down the tilt angle  of 3275612_1 by 8 degrees
- `C4`: Adjust the azimuth of 3269907_2 by 50 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Check test server and transmission issues
- `C7`: Decrease transmission power for 3269907_2
- `C8`: Press down the tilt angle of 3269907_2 by 10 degrees
- `C9`: Adjust the azimuth of 3275612_1 by 14 degrees
- `C10`: Increase transmission power for 3275612_1
- `C11`: Decrease A3 Offset threshold for 3275612_1
- `C12`: Decrease transmission power for 3275612_1
- `C13`: Lift the tilt angle of 3269907_2 by 10 degrees
- `C14`: Add neighbor relationship between 3269907_2 and 3275612_1
- `C15`: Increase A3 Offset threshold for 3275612_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275612_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275612_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269907_2
- `C19`: Add neighbor relationship between 3215274_3 and 3275612_1
- `C20`: Decrease A3 Offset threshold for 3269907_2
- `C21`: Increase transmission power for 3269907_2
- `C22`: Increase A3 Offset threshold for 3269907_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.266 | MS1 | 121.4656673315 | 31.1446367198 | 723 | 504990 | -85.69 | 16.29 | 439.71 | 0.17 | 2.28 | 1579 |
| 2024-09-20 22:21:32.888 | MS1 | 121.4656624477 | 31.1446244889 | 723 | 504990 | -89.04 | 13.81 | 457.71 | 0.16 | 2.80 | 1585 |
| 2024-09-20 22:21:33.367 | MS1 | 121.4656671288 | 31.1446335434 | 723 | 504990 | -89.50 | 12.69 | 324.71 | 0.14 | 2.24 | 1588 |
| 2024-09-20 22:21:34.681 | MS1 | 121.4656686996 | 31.1446280336 | 723 | 504990 | -89.26 | 16.70 | 103.75 | 0.05 | 2.59 | 1591 |
| 2024-09-20 22:21:35.985 | MS1 | 121.4656720447 | 31.1446341898 | 723 | 504990 | -88.41 | 14.26 | 92.80 | 0.00 | 2.21 | 1591 |
| 2024-09-20 22:21:36.741 | MS1 | 121.4656704068 | 31.1446201979 | 723 | 504990 | -86.24 | 17.76 | 74.54 | 0.19 | 2.83 | 1583 |
| 2024-09-20 22:21:37.899 | MS1 | 121.4656662279 | 31.1446329988 | 723 | 504990 | -91.25 | 8.31 | 62.37 | 0.20 | 2.27 | 1565 |
| 2024-09-20 22:21:38.239 | MS1 | 121.4656725230 | 31.1446276963 | 723 | 504990 | -89.57 | 11.63 | 58.91 | 0.01 | 2.00 | 1592 |
| 2024-09-20 22:21:39.893 | MS1 | 121.4656692787 | 31.1446228401 | 723 | 504990 | -91.55 | 12.31 | 60.83 | 0.03 | 2.33 | 1577 |
| 2024-09-20 22:21:40.204 | MS1 | 121.4656726617 | 31.1446343925 | 723 | 504990 | -89.81 | 8.11 | 417.11 | 0.19 | 2.58 | 1597 |
| 2024-09-20 22:21:41.569 | MS1 | 121.4656736128 | 31.1446322898 | 723 | 504990 | -92.84 | 9.58 | 358.27 | 0.20 | 2.55 | 1580 |
| 2024-09-20 22:21:42.295 | MS1 | 121.4656717803 | 31.1446352619 | 723 | 504990 | -91.75 | 9.51 | 431.99 | 0.05 | 2.30 | 1595 |

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
| 3215274 | 3 | 121.4752955581 | 31.1499943275 | 330 | 6 | 8 | 27.8 | TDD | 279 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3238460 | 4 | 121.4699695609 | 31.1537103422 | 159 | 7 | 5 | 18.7 | TDD | 747 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3269907 | 2 | 121.4677197349 | 31.1480664933 | 25 | 11 | 7 | 27.5 | TDD | 723 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3275612 | 1 | 121.4655618216 | 31.1542871930 | 193 | 7 | 7 | 20.7 | TDD | 408 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.389 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.406 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.532 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.532 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.202 | NREventA3 | measId:2;ServCellPCI:314;Se... |
| 2024-09-20 22:21:38.442 | NRHandoverAttempt | SourcePCI:314;SourceNR-ARFC... |
| 2024-09-20 22:21:38.472 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.482 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.588 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.588 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3275612 | 1 | 75.2572 | 86.0870 | -115.4621 | 12.0890 | 115.9916 | 0.0043 | 0.0190 |
| 2024_09_19 22:00 | 3269907 | 2 | 88.6332 | 82.9038 | -117.9675 | 8.4120 | 123.8040 | 0.0048 | 0.0158 |
| 2024_09_19 22:00 | 3215274 | 3 | 80.2709 | 88.6979 | -116.1590 | 8.6422 | 199.0369 | 0.0154 | 0.0188 |
| 2024_09_19 22:00 | 3238460 | 4 | 81.8018 | 89.7752 | -114.7842 | 10.3713 | 119.9782 | 0.0109 | 0.0169 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413437_2ABE99C9 | 504990 | 723 | -87.2 | 504990 | 408 | -91.0 | 504990 | 279 | -101.6 | 504990 | 747 |
| MR_1774413437_DCBF700B | 504990 | 723 | -86.6 | 504990 | 408 | -90.5 | 504990 | 279 | -99.6 | 504990 | 747 |
| MR_1774413437_1959B243 | 504990 | 723 | -87.4 | 504990 | 408 | -91.4 | 504990 | 279 | -98.4 | 504990 | 747 |
| MR_1774413437_F267052A | 504990 | 723 | -86.7 | 504990 | 408 | -88.4 | 504990 | 279 | -101.9 | 504990 | 747 |
| MR_1774413437_36BE3B9A | 504990 | 723 | -90.2 | 504990 | 408 | -90.8 | 504990 | 279 | -99.5 | 504990 | 747 |
| MR_1774413437_C045D2D2 | 504990 | 723 | -89.7 | 504990 | 408 | -87.6 | 504990 | 279 | -98.8 | 504990 | 747 |
| MR_1774413437_D6ADEFB7 | 504990 | 723 | -89.9 | 504990 | 408 | -87.8 | 504990 | 279 | -99.7 | 504990 | 747 |
| MR_1774413437_D17A3406 | 504990 | 723 | -90.2 | 504990 | 408 | -90.1 | 504990 | 279 | -99.6 | 504990 | 747 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 149: `49f218ff-162...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `49f218ff-162a-4f60-94ed-e2eb28f4d6e6` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[149] topology](images/test_0149.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3252897_3
- `C2`: Adjust the azimuth of 3278760_4 by 50 degrees
- `C3`: Decrease transmission power for 3252897_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252897_3
- `C5`: Decrease A3 Offset threshold for 3230089_1
- `C6`: Adjust the azimuth of 3230089_1 by 25 degrees
- `C7`: Lift the tilt angle of 3230089_1 by 6 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252897_3
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Check test server and transmission issues
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230089_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230089_1
- `C13`: Decrease A3 Offset threshold for 3252897_3
- `C14`: Add neighbor relationship between 3278760_4 and 3252897_3
- `C15`: Press down the tilt angle of 3230089_1 by 6 degrees
- `C16`: Press down the tilt angle  of 3278760_4 by 10 degrees
- `C17`: Lift the tilt angle  of 3278760_4 by 10 degrees
- `C18`: Decrease transmission power for 3230089_1
- `C19`: Add neighbor relationship between 3230089_1 and 3252897_3
- `C20`: Increase A3 Offset threshold for 3230089_1
- `C21`: Increase A3 Offset threshold for 3252897_3
- `C22`: Increase transmission power for 3230089_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.317 | MS1 | 121.4656750679 | 31.1446234830 | 273 | 504990 | -86.40 | 14.76 | 504.31 | 0.12 | 2.32 | 1595 |
| 2024-09-20 22:21:32.985 | MS1 | 121.4656714790 | 31.1446298590 | 273 | 504990 | -87.79 | 13.76 | 525.82 | 0.01 | 2.76 | 1574 |
| 2024-09-20 22:21:33.219 | MS1 | 121.4656714070 | 31.1446275969 | 273 | 504990 | -87.61 | 16.28 | 468.62 | 0.09 | 2.34 | 1594 |
| 2024-09-20 22:21:34.241 | MS1 | 121.4656731129 | 31.1446287143 | 273 | 504990 | -86.48 | 16.41 | 67.44 | 0.13 | 2.45 | 1564 |
| 2024-09-20 22:21:35.923 | MS1 | 121.4656693298 | 31.1446335317 | 273 | 504990 | -91.18 | 16.19 | 51.75 | 0.06 | 2.23 | 1596 |
| 2024-09-20 22:21:36.111 | MS1 | 121.4656729172 | 31.1446290321 | 273 | 504990 | -91.38 | 16.09 | 79.33 | 0.02 | 2.62 | 1567 |
| 2024-09-20 22:21:37.988 | MS1 | 121.4656734662 | 31.1446265362 | 273 | 504990 | -90.86 | 10.64 | 87.31 | 0.10 | 2.85 | 1580 |
| 2024-09-20 22:21:38.740 | MS1 | 121.4656682913 | 31.1446192378 | 273 | 504990 | -93.66 | 7.25 | 54.13 | 0.13 | 2.60 | 1588 |
| 2024-09-20 22:21:39.910 | MS1 | 121.4656665387 | 31.1446287753 | 273 | 504990 | -92.00 | 11.35 | 79.83 | 0.13 | 2.11 | 1571 |
| 2024-09-20 22:21:40.471 | MS1 | 121.4656584538 | 31.1446185828 | 273 | 504990 | -89.01 | 10.05 | 351.79 | 0.08 | 2.34 | 1599 |
| 2024-09-20 22:21:41.821 | MS1 | 121.4656732362 | 31.1446281474 | 273 | 504990 | -93.76 | 11.71 | 385.80 | 0.04 | 2.55 | 1583 |
| 2024-09-20 22:21:42.171 | MS1 | 121.4656678856 | 31.1446356889 | 273 | 504990 | -90.88 | 8.55 | 541.44 | 0.07 | 2.89 | 1569 |

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
| 3230089 | 1 | 121.4712201526 | 31.1557896560 | 178 | 4 | 2 | 46.2 | TDD | 273 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3233100 | 2 | 121.4758058381 | 31.1448512465 | 22 | 14 | 1 | 43.0 | TDD | 523 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3252897 | 3 | 121.4642491355 | 31.1464179078 | 253 | 13 | 1 | 42.3 | TDD | 9 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3278760 | 4 | 121.4738940868 | 31.1468038775 | 348 | 10 | 12 | 30.4 | TDD | 238 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.892 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.912 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.019 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.019 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.714 | NREventA3 | measId:2;ServCellPCI:908;Se... |
| 2024-09-20 22:21:37.954 | NRHandoverAttempt | SourcePCI:908;SourceNR-ARFC... |
| 2024-09-20 22:21:37.997 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.008 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.118 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.118 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230089 | 1 | 80.6783 | 76.5196 | -117.0366 | 16.8739 | 182.2108 | 0.0132 | 0.0023 |
| 2024_09_20 22:00 | 3233100 | 2 | 14.0822 | 5.3260 | -116.8494 | 5.1933 | 108.3153 | 0.0012 | 0.0132 |
| 2024_09_20 22:00 | 3252897 | 3 | 11.7879 | 15.8372 | -114.4220 | 9.7391 | 124.0714 | 0.0104 | 0.0116 |
| 2024_09_20 22:00 | 3278760 | 4 | 12.0955 | 7.7770 | -115.5786 | 5.6752 | 109.1504 | 0.0182 | 0.0101 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412373_5CADABD1 | 504990 | 273 | -84.7 | 504990 | 9 | -88.6 | 504990 | 238 | -98.6 | 504990 | 523 |
| MR_1774412373_2C998DDE | 504990 | 273 | -85.2 | 504990 | 9 | -89.0 | 504990 | 238 | -100.2 | 504990 | 523 |
| MR_1774412373_3980C25E | 504990 | 273 | -86.9 | 504990 | 9 | -88.2 | 504990 | 238 | -98.1 | 504990 | 523 |
| MR_1774412373_23B808EB | 504990 | 273 | -87.8 | 504990 | 9 | -88.9 | 504990 | 238 | -97.5 | 504990 | 523 |
| MR_1774412373_2BA435F0 | 504990 | 273 | -85.1 | 504990 | 9 | -87.7 | 504990 | 238 | -97.9 | 504990 | 523 |
| MR_1774412373_497B4E3F | 504990 | 273 | -85.6 | 504990 | 9 | -88.7 | 504990 | 238 | -99.1 | 504990 | 523 |
| MR_1774412373_E02C765F | 504990 | 273 | -86.4 | 504990 | 9 | -85.7 | 504990 | 238 | -101.2 | 504990 | 523 |
| MR_1774412373_AE1E9C1C | 504990 | 273 | -87.3 | 504990 | 9 | -87.1 | 504990 | 238 | -99.0 | 504990 | 523 |

> *... 2개 열 생략 (전체 14열)*

---
