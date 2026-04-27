# Track A 문제 분석 — train[1760]~train[1769]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1760] ~ train[1769] (10개)

## 목차

1. [문제 1760: `12f6a0b4-c8d...`](#1760) — single-answer, 정답: C20
2. [문제 1761: `c6505d95-704...`](#1761) — single-answer, 정답: C20
3. [문제 1762: `b5ec8b95-218...`](#1762) — single-answer, 정답: C4
4. [문제 1763: `0d4867f2-315...`](#1763) — single-answer, 정답: C16
5. [문제 1764: `03fceab8-1c5...`](#1764) — single-answer, 정답: C15
6. [문제 1765: `e3447584-b8a...`](#1765) — multiple-answer, 정답: C9|C17|C18|C20
7. [문제 1766: `bdbccf38-50a...`](#1766) — single-answer, 정답: C6
8. [문제 1767: `55bc7b0b-a0c...`](#1767) — single-answer, 정답: C20
9. [문제 1768: `98e3f7ea-400...`](#1768) — single-answer, 정답: C22
10. [문제 1769: `f0044604-913...`](#1769) — single-answer, 정답: C10

---

### 문제 1760: `12f6a0b4-c8d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `12f6a0b4-c8d6-49a0-9e01-55d44bbcf384` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1760] topology](images/train_1760.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3256354_4
- `C2`: Increase A3 Offset threshold for 3234077_3
- `C3`: Add neighbor relationship between 3234077_3 and 3256354_4
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Adjust the azimuth of 3234077_3 by 15 degrees
- `C6`: Press down the tilt angle  of 3256354_4 by 2 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256354_4
- `C8`: Increase A3 Offset threshold for 3256354_4
- `C9`: Lift the tilt angle of 3234077_3 by 10 degrees
- `C10`: Decrease transmission power for 3234077_3
- `C11`: Lift the tilt angle  of 3256354_4 by 2 degrees
- `C12`: Adjust the azimuth of 3256354_4 by 18 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234077_3
- `C14`: Decrease A3 Offset threshold for 3234077_3
- `C15`: Add neighbor relationship between 3226537_1 and 3256354_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256354_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234077_3
- `C18`: Decrease A3 Offset threshold for 3256354_4
- `C19`: Increase transmission power for 3234077_3
- `C20`: Check test server and transmission issues **← 정답**
- `C21`: Increase transmission power for 3256354_4
- `C22`: Press down the tilt angle of 3234077_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.393 | MS1 | 121.4656719506 | 31.1446303190 | 92 | 504990 | -87.97 | 14.26 | 552.76 | 0.03 | 2.26 | 1579 |
| 2024-09-20 22:21:32.566 | MS1 | 121.4656624812 | 31.1446344952 | 92 | 504990 | -88.66 | 17.12 | 396.93 | 0.02 | 2.86 | 1568 |
| 2024-09-20 22:21:33.973 | MS1 | 121.4656595181 | 31.1446304232 | 92 | 504990 | -91.87 | 14.24 | 535.62 | 0.05 | 2.40 | 1587 |
| 2024-09-20 22:21:34.319 | MS1 | 121.4656672599 | 31.1446332100 | 92 | 504990 | -89.01 | 14.60 | 96.07 | 0.01 | 2.45 | 391 |
| 2024-09-20 22:21:35.354 | MS1 | 121.4656638411 | 31.1446363592 | 92 | 504990 | -87.11 | 14.04 | 59.92 | 0.02 | 2.30 | 371 |
| 2024-09-20 22:21:36.285 | MS1 | 121.4656644605 | 31.1446342120 | 92 | 504990 | -87.19 | 14.25 | 55.74 | 0.07 | 2.80 | 355 |
| 2024-09-20 22:21:37.660 | MS1 | 121.4656712865 | 31.1446346772 | 92 | 504990 | -91.46 | 9.60 | 73.96 | 0.19 | 2.60 | 317 |
| 2024-09-20 22:21:38.778 | MS1 | 121.4656720600 | 31.1446270286 | 92 | 504990 | -90.99 | 8.41 | 59.92 | 0.15 | 2.49 | 346 |
| 2024-09-20 22:21:39.199 | MS1 | 121.4656586173 | 31.1446260286 | 92 | 504990 | -89.59 | 12.24 | 64.38 | 0.15 | 2.62 | 433 |
| 2024-09-20 22:21:40.365 | MS1 | 121.4656664385 | 31.1446228562 | 92 | 504990 | -89.90 | 12.67 | 331.88 | 0.13 | 2.94 | 1600 |
| 2024-09-20 22:21:41.279 | MS1 | 121.4656756385 | 31.1446213206 | 92 | 504990 | -89.50 | 11.12 | 340.38 | 0.03 | 2.88 | 1563 |
| 2024-09-20 22:21:42.929 | MS1 | 121.4656750349 | 31.1446348219 | 92 | 504990 | -93.81 | 12.76 | 444.46 | 0.07 | 2.54 | 1570 |

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
| 3214055 | 2 | 121.4658742832 | 31.1483128499 | 347 | 2 | 9 | 16.6 | TDD | 979 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3226537 | 1 | 121.4682350788 | 31.1475449999 | 8 | 4 | 8 | 34.1 | TDD | 281 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3234077 | 3 | 121.4756770102 | 31.1504528040 | 251 | 10 | 9 | 20.0 | TDD | 92 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3256354 | 4 | 121.4749000308 | 31.1462270139 | 241 | 0 | 0 | 24.6 | TDD | 375 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.816 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.837 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.974 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.974 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.618 | NREventA3 | measId:2;ServCellPCI:548;Se... |
| 2024-09-20 22:21:37.858 | NRHandoverAttempt | SourcePCI:548;SourceNR-ARFC... |
| 2024-09-20 22:21:37.902 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.915 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.042 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.042 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226537 | 1 | 7.4299 | 8.2172 | -116.0805 | 11.1535 | 163.0578 | 0.0058 | 0.0149 |
| 2024_09_20 22:00 | 3214055 | 2 | 13.9383 | 6.1817 | -117.6026 | 19.4939 | 150.6279 | 0.0153 | 0.0091 |
| 2024_09_20 22:00 | 3234077 | 3 | 9.4069 | 7.9853 | -114.2645 | 11.4563 | 106.3240 | 0.0001 | 0.0189 |
| 2024_09_20 22:00 | 3256354 | 4 | 7.5154 | 7.8467 | -116.2098 | 14.4677 | 123.9468 | 0.0172 | 0.0155 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415784_CA55BAB4 | 504990 | 92 | -87.5 | 504990 | 375 | -90.3 | 504990 | 281 | -97.7 | 504990 | 979 |
| MR_1774415784_45D7021A | 504990 | 92 | -89.8 | 504990 | 375 | -91.3 | 504990 | 281 | -98.6 | 504990 | 979 |
| MR_1774415784_4C24C9C1 | 504990 | 92 | -87.2 | 504990 | 375 | -91.3 | 504990 | 281 | -95.2 | 504990 | 979 |
| MR_1774415784_BF65CC9D | 504990 | 92 | -90.6 | 504990 | 375 | -88.7 | 504990 | 281 | -96.8 | 504990 | 979 |
| MR_1774415784_7D825A3B | 504990 | 92 | -88.8 | 504990 | 375 | -88.7 | 504990 | 281 | -97.1 | 504990 | 979 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1761: `c6505d95-704...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c6505d95-704c-4ad1-94c6-955f830fb0e5` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Add neighbor relationship between 3233794_1 and 3235202_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1761] topology](images/train_1761.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3235202_3
- `C2`: Check test server and transmission issues
- `C3`: Decrease transmission power for 3233794_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233794_1
- `C5`: Decrease A3 Offset threshold for 3233794_1
- `C6`: Decrease transmission power for 3235202_3
- `C7`: Press down the tilt angle of 3233794_1 by 10 degrees
- `C8`: Press down the tilt angle  of 3235202_3 by 4 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235202_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233794_1
- `C11`: Adjust the azimuth of 3235202_3 by 36 degrees
- `C12`: Increase A3 Offset threshold for 3233794_1
- `C13`: Increase transmission power for 3233794_1
- `C14`: Adjust the azimuth of 3233794_1 by 50 degrees
- `C15`: Add neighbor relationship between 3261794_2 and 3235202_3
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235202_3
- `C18`: Lift the tilt angle  of 3235202_3 by 4 degrees
- `C19`: Increase transmission power for 3235202_3
- `C20`: Add neighbor relationship between 3233794_1 and 3235202_3 **← 정답**
- `C21`: Lift the tilt angle of 3233794_1 by 10 degrees
- `C22`: Increase A3 Offset threshold for 3235202_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.468 | MS1 | 121.4656602659 | 31.1446363094 | 232 | 504990 | -81.32 | 17.26 | 596.25 | 0.02 | 2.49 | 1585 |
| 2024-09-20 22:21:32.122 | MS1 | 121.4656660654 | 31.1446362077 | 232 | 504990 | -83.11 | 12.33 | 444.03 | 0.15 | 2.97 | 1600 |
| 2024-09-20 22:21:33.219 | MS1 | 121.4656628160 | 31.1446250498 | 232 | 504990 | -80.94 | 14.72 | 395.37 | 0.17 | 2.37 | 1569 |
| 2024-09-20 22:21:34.937 | MS1 | 121.4656607974 | 31.1446328048 | 232 | 504990 | -94.43 | -2.90 | 45.23 | 0.04 | 1.48 | 1581 |
| 2024-09-20 22:21:35.142 | MS1 | 121.4656732707 | 31.1446239140 | 232 | 504990 | -89.13 | -3.85 | 67.69 | 0.06 | 1.34 | 1575 |
| 2024-09-20 22:21:36.814 | MS1 | 121.4656773685 | 31.1446268658 | 232 | 504990 | -88.55 | -0.97 | 62.79 | 0.18 | 1.35 | 1584 |
| 2024-09-20 22:21:37.753 | MS1 | 121.4656633511 | 31.1446369818 | 232 | 504990 | -89.25 | -3.03 | 53.26 | 0.09 | 1.18 | 1578 |
| 2024-09-20 22:21:38.106 | MS1 | 121.4656746184 | 31.1446214338 | 232 | 504990 | -84.74 | 16.55 | 390.44 | 0.19 | 1.32 | 1572 |
| 2024-09-20 22:21:39.472 | MS1 | 121.4656650626 | 31.1446254625 | 232 | 504990 | -79.49 | 16.68 | 469.28 | 0.08 | 1.22 | 1568 |
| 2024-09-20 22:21:40.902 | MS1 | 121.4656644661 | 31.1446181848 | 232 | 504990 | -82.53 | 13.44 | 323.71 | 0.05 | 2.72 | 1597 |
| 2024-09-20 22:21:41.738 | MS1 | 121.4656722422 | 31.1446180419 | 232 | 504990 | -79.01 | 14.06 | 468.23 | 0.08 | 2.85 | 1580 |
| 2024-09-20 22:21:42.679 | MS1 | 121.4656679373 | 31.1446259317 | 232 | 504990 | -82.63 | 17.76 | 402.96 | 0.06 | 2.66 | 1565 |

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
| 3214480 | 4 | 121.4719293388 | 31.1473040362 | 345 | 11 | 7 | 37.1 | TDD | 919 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3233794 | 1 | 121.4654259661 | 31.1523695549 | 59 | 12 | 3 | 24.7 | TDD | 232 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3235202 | 3 | 121.4643277347 | 31.1541834035 | 137 | 2 | 6 | 46.1 | TDD | 125 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3261794 | 2 | 121.4703548884 | 31.1553406921 | 178 | 12 | 12 | 41.1 | TDD | 561 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.351 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.376 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.481 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.481 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.183 | NREventA3 | measId:2;ServCellPCI:3;Serv... |
| 2024-09-20 22:21:36.183 | NREventA3 | measId:2;ServCellPCI:3;Serv... |
| 2024-09-20 22:21:37.183 | NREventA3 | measId:2;ServCellPCI:3;Serv... |
| 2024-09-20 22:21:39.683 | NRRRCReestablishAttempt | PCI:3 |
| 2024-09-20 22:21:39.699 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.711 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.836 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.836 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233794 | 1 | 13.2858 | 11.4066 | -114.1978 | 6.7991 | 150.4963 | 0.0075 | 0.1697 |
| 2024_09_20 22:00 | 3261794 | 2 | 5.7291 | 10.3639 | -115.5154 | 13.6999 | 183.1911 | 0.0007 | 0.0044 |
| 2024_09_20 22:00 | 3235202 | 3 | 6.2425 | 10.2623 | -116.0046 | 18.5667 | 151.7320 | 0.0164 | 0.0112 |
| 2024_09_20 22:00 | 3214480 | 4 | 5.4647 | 8.1644 | -117.5880 | 7.0121 | 174.0161 | 0.0011 | 0.0137 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416742_210BD2A5 | 504990 | 125 | -88.7 | 504990 | 232 | -94.3 | 504990 | 561 | -90.1 | 504990 | 919 |
| MR_1774416742_B30B75EC | 504990 | 232 | -93.4 | 504990 | 125 | -90.0 | 504990 | 561 | -89.4 | 504990 | 919 |
| MR_1774416742_724D5332 | 504990 | 232 | -93.2 | 504990 | 125 | -90.4 | 504990 | 561 | -89.0 | 504990 | 919 |
| MR_1774416742_F6543B2C | 504990 | 232 | -94.4 | 504990 | 125 | -90.2 | 504990 | 561 | -89.8 | 504990 | 919 |
| MR_1774416742_A9603639 | 504990 | 232 | -95.4 | 504990 | 125 | -86.9 | 504990 | 561 | -89.1 | 504990 | 919 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1762: `b5ec8b95-218...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b5ec8b95-218f-48f1-8021-60518742ccd2` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238650_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1762] topology](images/train_1762.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247160_3
- `C3`: Check test server and transmission issues
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238650_1 **← 정답**
- `C5`: Decrease A3 Offset threshold for 3238650_1
- `C6`: Decrease transmission power for 3238650_1
- `C7`: Adjust the azimuth of 3247160_3 by 41 degrees
- `C8`: Press down the tilt angle  of 3247160_3 by 4 degrees
- `C9`: Decrease transmission power for 3247160_3
- `C10`: Increase A3 Offset threshold for 3238650_1
- `C11`: Add neighbor relationship between 3238650_1 and 3247160_3
- `C12`: Adjust the azimuth of 3238650_1 by 14 degrees
- `C13`: Add neighbor relationship between 3214189_10 and 3247160_3
- `C14`: Increase transmission power for 3238650_1
- `C15`: Decrease A3 Offset threshold for 3247160_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247160_3
- `C17`: Increase transmission power for 3247160_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238650_1
- `C19`: Lift the tilt angle of 3238650_1 by 4 degrees
- `C20`: Lift the tilt angle  of 3247160_3 by 4 degrees
- `C21`: Press down the tilt angle of 3238650_1 by 4 degrees
- `C22`: Increase A3 Offset threshold for 3247160_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.288 | MS1 | 121.4656773717 | 31.1446318843 | 577 | 504990 | -93.69 | 9.26 | 422.04 | 0.09 | 2.29 | 1599 |
| 2024-09-20 22:21:32.989 | MS1 | 121.4656690896 | 31.1446279591 | 575 | 504990 | -94.60 | 13.18 | 316.11 | 0.01 | 2.71 | 1600 |
| 2024-09-20 22:21:33.928 | MS1 | 121.4656763128 | 31.1446207964 | 861 | 504990 | -95.03 | 9.54 | 327.94 | 0.11 | 2.31 | 1578 |
| 2024-09-20 22:21:34.747 | MS1 | 121.4656709760 | 31.1446347322 | 923 | 152650 | -94.14 | 4.79 | 53.14 | 0.05 | 1.81 | 957 |
| 2024-09-20 22:21:35.769 | MS1 | 121.4656772841 | 31.1446357804 | 193 | 152650 | -89.26 | 3.12 | 70.92 | 0.02 | 1.76 | 984 |
| 2024-09-20 22:21:36.431 | MS1 | 121.4656620087 | 31.1446368981 | 523 | 152650 | -95.57 | 2.74 | 54.50 | 0.01 | 1.67 | 935 |
| 2024-09-20 22:21:37.634 | MS1 | 121.4656665645 | 31.1446215282 | 951 | 152650 | -94.16 | 5.33 | 73.82 | 0.18 | 1.83 | 921 |
| 2024-09-20 22:21:38.243 | MS1 | 121.4656606109 | 31.1446361953 | 923 | 152650 | -96.91 | 6.70 | 80.97 | 0.06 | 1.72 | 912 |
| 2024-09-20 22:21:39.432 | MS1 | 121.4656581875 | 31.1446334338 | 193 | 152650 | -88.16 | 6.37 | 93.22 | 0.11 | 1.77 | 937 |
| 2024-09-20 22:21:40.561 | MS1 | 121.4656741462 | 31.1446186678 | 523 | 152650 | -91.99 | 4.66 | 70.19 | 0.09 | 2.74 | 1569 |
| 2024-09-20 22:21:41.384 | MS1 | 121.4656691263 | 31.1446241176 | 951 | 152650 | -94.79 | 7.26 | 52.46 | 0.01 | 2.76 | 1585 |
| 2024-09-20 22:21:42.377 | MS1 | 121.4656726887 | 31.1446196812 | 923 | 152650 | -95.08 | 5.41 | 90.37 | 0.04 | 2.58 | 1594 |

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
| 3214189 | 10 | 121.4727838114 | 31.1514598365 | 171 | 12 | 10 | 9.2 | FDD | 523 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3217247 | 5 | 121.4744220649 | 31.1471910616 | 315 | 14 | 10 | 1.0 | TDD | 861 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3229733 | 12 | 121.4751933272 | 31.1507323447 | 263 | 9 | 8 | 17.1 | FDD | 951 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3238650 | 1 | 121.4699788695 | 31.1449443908 | 279 | 3 | 5 | 10.5 | TDD | 577 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3244050 | 8 | 121.4696579139 | 31.1460308812 | 9 | 7 | 8 | 26.2 | FDD | 449 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3245152 | 6 | 121.4751991977 | 31.1504599793 | 196 | 15 | 4 | 29.2 | TDD | 575 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3247160 | 3 | 121.4640330080 | 31.1492111069 | 204 | 3 | 6 | 12.4 | TDD | 453 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3260814 | 11 | 121.4738441126 | 31.1481143550 | 89 | 2 | 9 | 15.4 | FDD | 848 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3262183 | 9 | 121.4664116783 | 31.1522847442 | 93 | 2 | 3 | 20.6 | FDD | 261 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3273023 | 7 | 121.4701600959 | 31.1472529260 | 250 | 12 | 10 | 7.8 | FDD | 193 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3274536 | 13 | 121.4681158322 | 31.1496225287 | 330 | 15 | 5 | 28.0 | FDD | 923 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3277837 | 4 | 121.4684066730 | 31.1522702563 | 253 | 12 | 4 | 7.9 | TDD | 314 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3278940 | 2 | 121.4646231914 | 31.1456771117 | 299 | 5 | 3 | 28.9 | TDD | 163 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.889 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.910 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.016 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.016 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.761 | NREventA2 | measId:1;ServCellPCI:365;Se... |
| 2024-09-20 22:21:34.881 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.120 | NREventA5 | measId:3;ServCellPCI:365;Se... |
| 2024-09-20 22:21:35.177 | NRHandoverAttempt | SourcePCI:365;SourceNR-ARFC... |
| 2024-09-20 22:21:35.209 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.224 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.368 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.368 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238650 | 1 | 15.2507 | 16.2515 | -114.5428 | 9.7600 | 110.4534 | 0.0108 | 0.0007 |
| 2024_09_20 22:00 | 3278940 | 2 | 17.7757 | 17.3317 | -114.8237 | 16.3924 | 158.4255 | 0.0017 | 0.0199 |
| 2024_09_20 22:00 | 3247160 | 3 | 17.8928 | 15.2527 | -114.2966 | 19.4358 | 92.6908 | 0.0097 | 0.0105 |
| 2024_09_20 22:00 | 3277837 | 4 | 17.0243 | 18.0860 | -115.0858 | 7.9626 | 109.0327 | 0.0030 | 0.0160 |
| 2024_09_20 22:00 | 3217247 | 5 | 19.9528 | 18.2739 | -117.4821 | 10.1979 | 117.2477 | 0.0159 | 0.0171 |
| 2024_09_20 22:00 | 3245152 | 6 | 8.0044 | 11.0457 | -114.2723 | 12.7538 | 197.0587 | 0.0139 | 0.0106 |
| 2024_09_20 22:00 | 3273023 | 7 | 12.6113 | 13.6131 | -114.4595 | 3.8264 | 24.8504 | 0.0067 | 0.0200 |
| 2024_09_20 22:00 | 3244050 | 8 | 17.5790 | 7.7841 | -117.3002 | 4.1116 | 42.4544 | 0.0188 | 0.0126 |
| 2024_09_20 22:00 | 3262183 | 9 | 13.5247 | 19.6853 | -117.4148 | 4.2562 | 51.4639 | 0.0036 | 0.0038 |
| 2024_09_20 22:00 | 3214189 | 10 | 7.0174 | 5.1673 | -116.2068 | 4.4819 | 20.7710 | 0.0162 | 0.0171 |
| 2024_09_20 22:00 | 3260814 | 11 | 11.0227 | 15.8547 | -116.5475 | 4.9527 | 54.3310 | 0.0180 | 0.0104 |
| 2024_09_20 22:00 | 3229733 | 12 | 14.5162 | 17.8952 | -117.2201 | 3.7133 | 42.6528 | 0.0033 | 0.0119 |
| 2024_09_20 22:00 | 3274536 | 13 | 16.2415 | 9.5059 | -114.2982 | 4.7918 | 28.8400 | 0.0063 | 0.0157 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416956_55D1AAD7 | 152650 | 923 | -94.1 | 152650 | 848 | -99.7 | 152650 | 261 | -103.6 | 152650 | 449 |
| MR_1774416956_4B3BDD45 | 504990 | 861 | -96.1 | 504990 | 453 | -89.2 | 504990 | 314 | -96.3 | 504990 | 163 |
| MR_1774416956_91A02A5F | 504990 | 861 | -93.7 | 504990 | 453 | -88.5 | 504990 | 314 | -98.2 | 504990 | 163 |
| MR_1774416956_E5E695E3 | 504990 | 861 | -94.0 | 504990 | 453 | -91.7 | 504990 | 314 | -97.5 | 504990 | 163 |
| MR_1774416956_B1FCDC3D | 152650 | 923 | -92.4 | 152650 | 848 | -101.7 | 152650 | 261 | -100.6 | 152650 | 449 |
| MR_1774416956_77F7D6C4 | 504990 | 861 | -96.3 | 504990 | 453 | -90.9 | 504990 | 314 | -96.9 | 504990 | 163 |
| MR_1774416956_03129D3E | 504990 | 861 | -94.7 | 504990 | 453 | -91.4 | 504990 | 314 | -94.8 | 504990 | 163 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1763: `0d4867f2-315...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0d4867f2-3157-4b75-a364-33842bd15160` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease A3 Offset threshold for 3243390_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1763] topology](images/train_1763.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3243390_3
- `C2`: Increase transmission power for 3243390_3
- `C3`: Adjust the azimuth of 3239613_2 by 10 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239613_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243390_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243390_3
- `C7`: Lift the tilt angle  of 3239613_2 by 10 degrees
- `C8`: Increase transmission power for 3239613_2
- `C9`: Lift the tilt angle of 3243390_3 by 9 degrees
- `C10`: Decrease transmission power for 3239613_2
- `C11`: Decrease A3 Offset threshold for 3239613_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Press down the tilt angle of 3243390_3 by 9 degrees
- `C14`: Check test server and transmission issues
- `C15`: Increase A3 Offset threshold for 3239613_2
- `C16`: Decrease A3 Offset threshold for 3243390_3 **← 정답**
- `C17`: Add neighbor relationship between 3274956_1 and 3239613_2
- `C18`: Press down the tilt angle  of 3239613_2 by 10 degrees
- `C19`: Adjust the azimuth of 3243390_3 by 33 degrees
- `C20`: Decrease transmission power for 3243390_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239613_2
- `C22`: Add neighbor relationship between 3243390_3 and 3239613_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.823 | MS1 | 121.4656705985 | 31.1446287451 | 933 | 504990 | -77.84 | 15.47 | 602.43 | 0.07 | 2.57 | 1568 |
| 2024-09-20 22:21:32.645 | MS1 | 121.4656698819 | 31.1446265189 | 933 | 504990 | -83.67 | 14.54 | 451.05 | 0.08 | 2.98 | 1597 |
| 2024-09-20 22:21:33.593 | MS1 | 121.4656711125 | 31.1446244177 | 933 | 504990 | -77.07 | 16.66 | 417.61 | 0.14 | 2.54 | 1570 |
| 2024-09-20 22:21:34.232 | MS1 | 121.4656598460 | 31.1446210728 | 933 | 504990 | -92.18 | -0.82 | 54.29 | 0.02 | 1.27 | 1593 |
| 2024-09-20 22:21:35.957 | MS1 | 121.4656612726 | 31.1446281533 | 933 | 504990 | -88.16 | -2.28 | 39.26 | 0.13 | 1.09 | 1585 |
| 2024-09-20 22:21:36.213 | MS1 | 121.4656634404 | 31.1446243102 | 933 | 504990 | -90.64 | -3.17 | 67.62 | 0.17 | 1.32 | 1591 |
| 2024-09-20 22:21:37.257 | MS1 | 121.4656778265 | 31.1446228811 | 933 | 504990 | -85.65 | -0.89 | 24.62 | 0.02 | 1.15 | 1582 |
| 2024-09-20 22:21:38.788 | MS1 | 121.4656695153 | 31.1446269688 | 933 | 504990 | -92.31 | -1.19 | 56.52 | 0.11 | 1.00 | 1587 |
| 2024-09-20 22:21:39.653 | MS1 | 121.4656610661 | 31.1446297135 | 228 | 504990 | -82.71 | 14.92 | 181.53 | 0.00 | 1.36 | 1570 |
| 2024-09-20 22:21:40.825 | MS1 | 121.4656675553 | 31.1446376452 | 228 | 504990 | -77.96 | 14.41 | 509.86 | 0.15 | 2.99 | 1561 |
| 2024-09-20 22:21:41.167 | MS1 | 121.4656701198 | 31.1446192584 | 228 | 504990 | -82.98 | 13.57 | 542.45 | 0.19 | 2.90 | 1575 |
| 2024-09-20 22:21:42.867 | MS1 | 121.4656615742 | 31.1446339862 | 228 | 504990 | -80.84 | 16.26 | 570.26 | 0.18 | 2.54 | 1584 |

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
| 3223323 | 4 | 121.4657218537 | 31.1490588107 | 130 | 14 | 0 | 40.0 | TDD | 463 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3239613 | 2 | 121.4669234445 | 31.1463635977 | 201 | 11 | 5 | 38.9 | TDD | 228 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3243390 | 3 | 121.4731892894 | 31.1469754837 | 217 | 7 | 11 | 23.5 | TDD | 933 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3274956 | 1 | 121.4702295193 | 31.1496247591 | 53 | 13 | 3 | 42.6 | TDD | 507 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.807 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.826 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.930 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.930 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.615 | NREventA3 | measId:2;ServCellPCI:35;Ser... |
| 2024-09-20 22:21:37.855 | NRHandoverAttempt | SourcePCI:35;SourceNR-ARFCN... |
| 2024-09-20 22:21:37.902 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.913 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.017 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.017 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274956 | 1 | 11.1433 | 18.6974 | -114.2969 | 16.6621 | 110.2869 | 0.0087 | 0.0056 |
| 2024_09_20 22:00 | 3239613 | 2 | 17.1355 | 5.1737 | -116.3481 | 9.4177 | 172.8052 | 0.0063 | 0.0132 |
| 2024_09_20 22:00 | 3243390 | 3 | 7.7311 | 16.5896 | -115.0914 | 18.0867 | 172.1409 | 0.0007 | 0.1985 |
| 2024_09_20 22:00 | 3223323 | 4 | 15.3141 | 5.4695 | -114.9662 | 18.3026 | 182.3299 | 0.0106 | 0.0075 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415292_8B10FCC0 | 504990 | 933 | -93.0 | 504990 | 228 | -87.1 | 504990 | 507 | -88.5 | 504990 | 463 |
| MR_1774415292_8219DFA4 | 504990 | 933 | -91.2 | 504990 | 228 | -89.0 | 504990 | 507 | -90.8 | 504990 | 463 |
| MR_1774415292_CB7CF6C4 | 504990 | 228 | -88.3 | 504990 | 933 | -90.7 | 504990 | 507 | -88.1 | 504990 | 463 |
| MR_1774415292_618F2EFC | 504990 | 228 | -87.4 | 504990 | 933 | -90.2 | 504990 | 507 | -91.2 | 504990 | 463 |
| MR_1774415292_5A2C4BA0 | 504990 | 933 | -92.5 | 504990 | 228 | -86.8 | 504990 | 507 | -88.8 | 504990 | 463 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1764: `03fceab8-1c5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `03fceab8-1c50-4eb5-9eb9-2643204f5380` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Lift the tilt angle  of 3227671_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1764] topology](images/train_1764.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3257163_4 and 3273909_1
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease transmission power for 3273909_1
- `C4`: Decrease A3 Offset threshold for 3257163_4
- `C5`: Adjust the azimuth of 3227671_3 by 50 degrees
- `C6`: Press down the tilt angle of 3257163_4 by 2 degrees
- `C7`: Lift the tilt angle of 3257163_4 by 2 degrees
- `C8`: Decrease A3 Offset threshold for 3273909_1
- `C9`: Increase A3 Offset threshold for 3257163_4
- `C10`: Decrease transmission power for 3257163_4
- `C11`: Add neighbor relationship between 3227671_3 and 3273909_1
- `C12`: Press down the tilt angle  of 3227671_3 by 10 degrees
- `C13`: Adjust the azimuth of 3257163_4 by 47 degrees
- `C14`: Increase transmission power for 3257163_4
- `C15`: Lift the tilt angle  of 3227671_3 by 10 degrees **← 정답**
- `C16`: Increase A3 Offset threshold for 3273909_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273909_1
- `C18`: Check test server and transmission issues
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273909_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257163_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257163_4
- `C22`: Increase transmission power for 3273909_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.585 | MS1 | 121.4656762962 | 31.1446210222 | 31 | 504990 | -89.23 | 12.58 | 338.52 | 0.18 | 2.13 | 1573 |
| 2024-09-20 22:21:32.334 | MS1 | 121.4656755209 | 31.1446339936 | 31 | 504990 | -86.66 | 13.92 | 468.28 | 0.10 | 2.46 | 1599 |
| 2024-09-20 22:21:33.855 | MS1 | 121.4656707710 | 31.1446300414 | 31 | 504990 | -86.79 | 15.37 | 576.52 | 0.18 | 2.44 | 1569 |
| 2024-09-20 22:21:34.111 | MS1 | 121.4656721871 | 31.1446188737 | 31 | 504990 | -85.72 | 13.24 | 63.60 | 0.11 | 2.98 | 1595 |
| 2024-09-20 22:21:35.530 | MS1 | 121.4656594558 | 31.1446310137 | 31 | 504990 | -87.10 | 14.84 | 80.58 | 0.10 | 2.73 | 1578 |
| 2024-09-20 22:21:36.624 | MS1 | 121.4656737542 | 31.1446341274 | 31 | 504990 | -89.74 | 17.79 | 53.35 | 0.20 | 2.12 | 1599 |
| 2024-09-20 22:21:37.298 | MS1 | 121.4656644768 | 31.1446342375 | 31 | 504990 | -93.42 | 9.16 | 54.59 | 0.12 | 2.76 | 1584 |
| 2024-09-20 22:21:38.654 | MS1 | 121.4656673980 | 31.1446197991 | 31 | 504990 | -90.35 | 8.54 | 95.93 | 0.00 | 2.73 | 1567 |
| 2024-09-20 22:21:39.998 | MS1 | 121.4656676249 | 31.1446369763 | 31 | 504990 | -90.25 | 7.05 | 86.08 | 0.13 | 2.86 | 1598 |
| 2024-09-20 22:21:40.732 | MS1 | 121.4656747304 | 31.1446307986 | 31 | 504990 | -90.62 | 9.92 | 556.29 | 0.02 | 2.62 | 1584 |
| 2024-09-20 22:21:41.244 | MS1 | 121.4656594275 | 31.1446235263 | 31 | 504990 | -89.94 | 10.45 | 473.73 | 0.19 | 2.43 | 1561 |
| 2024-09-20 22:21:42.381 | MS1 | 121.4656715088 | 31.1446198525 | 31 | 504990 | -89.78 | 7.44 | 293.39 | 0.08 | 2.80 | 1597 |

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
| 3227671 | 3 | 121.4664298286 | 31.1512923810 | 66 | 14 | 12 | 23.0 | TDD | 333 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3252440 | 2 | 121.4741298521 | 31.1539453886 | 188 | 15 | 3 | 43.9 | TDD | 554 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3257163 | 4 | 121.4699392618 | 31.1502700126 | 260 | 0 | 9 | 21.3 | TDD | 31 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3273909 | 1 | 121.4660160239 | 31.1470372243 | 265 | 15 | 10 | 43.6 | TDD | 474 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.124 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.139 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.259 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.259 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.957 | NREventA3 | measId:2;ServCellPCI:168;Se... |
| 2024-09-20 22:21:38.197 | NRHandoverAttempt | SourcePCI:168;SourceNR-ARFC... |
| 2024-09-20 22:21:38.240 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.251 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.376 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.376 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273909 | 1 | 5.2453 | 5.4408 | -114.2595 | 6.7123 | 145.1680 | 0.0049 | 0.0085 |
| 2024_09_20 22:00 | 3252440 | 2 | 13.2696 | 15.6298 | -115.4463 | 11.4850 | 198.7225 | 0.0123 | 0.0093 |
| 2024_09_20 22:00 | 3227671 | 3 | 11.0600 | 14.1489 | -115.1181 | 11.6460 | 172.2567 | 0.0141 | 0.0076 |
| 2024_09_20 22:00 | 3257163 | 4 | 93.7632 | 75.0970 | -114.6082 | 7.5433 | 154.0350 | 0.0068 | 0.0022 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413682_60DAFBD3 | 504990 | 31 | -86.4 | 504990 | 474 | -85.9 | 504990 | 333 | -99.2 | 504990 | 554 |
| MR_1774413682_1EFD6B2C | 504990 | 31 | -83.7 | 504990 | 474 | -84.7 | 504990 | 333 | -97.7 | 504990 | 554 |
| MR_1774413682_71A28E18 | 504990 | 31 | -86.9 | 504990 | 474 | -84.6 | 504990 | 333 | -97.7 | 504990 | 554 |
| MR_1774413682_00E95A54 | 504990 | 31 | -84.7 | 504990 | 474 | -84.2 | 504990 | 333 | -99.4 | 504990 | 554 |
| MR_1774413682_85CB5FCB | 504990 | 31 | -87.3 | 504990 | 474 | -84.5 | 504990 | 333 | -98.3 | 504990 | 554 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1765: `e3447584-b8a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e3447584-b8a9-4b2f-9a06-08453d21996d` |
| Tag | **multiple-answer** |
| 정답 | **C9|C17|C18|C20** |
| C9 의미 | Decrease transmission power for 3231447_5 |
| C17 의미 | Press down the tilt angle  of 3231447_5 by 5 degrees |
| C18 의미 | Increase A3 Offset threshold for 3231447_5 |
| C20 의미 | Increase A3 Offset threshold for 3269372_2 |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1765] topology](images/train_1765.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269372_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269372_2
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Lift the tilt angle  of 3231447_5 by 5 degrees
- `C5`: Adjust the azimuth of 3231447_5 by 14 degrees
- `C6`: Lift the tilt angle of 3269372_2 by 3 degrees
- `C7`: Adjust the azimuth of 3269372_2 by 26 degrees
- `C8`: Add neighbor relationship between 3269372_2 and 3231447_5
- `C9`: Decrease transmission power for 3231447_5 **← 정답**
- `C10`: Add neighbor relationship between 3217632_1 and 3231447_5
- `C11`: Decrease A3 Offset threshold for 3231447_5
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231447_5
- `C13`: Increase transmission power for 3269372_2
- `C14`: Increase transmission power for 3231447_5
- `C15`: Decrease A3 Offset threshold for 3269372_2
- `C16`: Check test server and transmission issues
- `C17`: Press down the tilt angle  of 3231447_5 by 5 degrees **← 정답**
- `C18`: Increase A3 Offset threshold for 3231447_5 **← 정답**
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231447_5
- `C20`: Increase A3 Offset threshold for 3269372_2 **← 정답**
- `C21`: Press down the tilt angle of 3269372_2 by 3 degrees
- `C22`: Decrease transmission power for 3269372_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.788 | MS1 | 121.4656659999 | 31.1446378952 | 868 | 504990 | -75.87 | 13.31 | 375.75 | 0.05 | 2.78 | 1561 |
| 2024-09-20 22:21:32.829 | MS1 | 121.4656725117 | 31.1446319476 | 868 | 504990 | -80.49 | 14.84 | 460.59 | 0.13 | 2.53 | 1571 |
| 2024-09-20 22:21:33.734 | MS1 | 121.4656668970 | 31.1446249546 | 868 | 504990 | -78.79 | 12.70 | 492.91 | 0.19 | 2.46 | 1593 |
| 2024-09-20 22:21:34.288 | MS1 | 121.4656763832 | 31.1446207068 | 917 | 504990 | -85.96 | 2.34 | 34.03 | 0.05 | 1.40 | 1599 |
| 2024-09-20 22:21:35.403 | MS1 | 121.4656740812 | 31.1446191821 | 917 | 504990 | -86.82 | 3.47 | 43.67 | 0.06 | 1.36 | 1577 |
| 2024-09-20 22:21:36.110 | MS1 | 121.4656639036 | 31.1446256576 | 868 | 504990 | -81.62 | 3.92 | 57.54 | 0.11 | 1.44 | 1595 |
| 2024-09-20 22:21:37.975 | MS1 | 121.4656760628 | 31.1446265194 | 868 | 504990 | -84.41 | 4.75 | 82.92 | 0.05 | 1.01 | 1568 |
| 2024-09-20 22:21:38.648 | MS1 | 121.4656611367 | 31.1446244812 | 917 | 504990 | -81.81 | 4.93 | 76.50 | 0.16 | 1.34 | 1600 |
| 2024-09-20 22:21:39.917 | MS1 | 121.4656643647 | 31.1446287032 | 917 | 504990 | -86.81 | 1.75 | 53.43 | 0.05 | 1.24 | 1582 |
| 2024-09-20 22:21:40.391 | MS1 | 121.4656697829 | 31.1446351641 | 917 | 504990 | -82.57 | 13.43 | 349.40 | 0.01 | 2.04 | 1596 |
| 2024-09-20 22:21:41.436 | MS1 | 121.4656703309 | 31.1446314802 | 917 | 504990 | -75.54 | 17.59 | 336.88 | 0.08 | 2.86 | 1599 |
| 2024-09-20 22:21:42.951 | MS1 | 121.4656762171 | 31.1446273995 | 917 | 504990 | -82.33 | 17.43 | 585.41 | 0.14 | 2.67 | 1582 |

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
| 3217065 | 4 | 121.4686946246 | 31.1466761545 | 223 | 4 | 5 | 33.9 | TDD | 917 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3217632 | 1 | 121.4703125654 | 31.1461367657 | 60 | 9 | 12 | 28.7 | TDD | 291 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3231447 | 5 | 121.4643813628 | 31.1536263988 | 159 | 3 | 8 | 40.8 | TDD | 924 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3269372 | 2 | 121.4739959250 | 31.1524380593 | 196 | 2 | 7 | 16.3 | TDD | 868 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3273801 | 3 | 121.4752203095 | 31.1452769370 | 315 | 0 | 11 | 47.2 | TDD | 499 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.536 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.552 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.680 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.680 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.347 | NREventA3 | measId:2;ServCellPCI:344;Se... |
| 2024-09-20 22:21:34.587 | NRHandoverAttempt | SourcePCI:344;SourceNR-ARFC... |
| 2024-09-20 22:21:34.625 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.635 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:34.741 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.741 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.347 | NREventA3 | measId:2;ServCellPCI:101;Se... |
| 2024-09-20 22:21:36.587 | NRHandoverAttempt | SourcePCI:101;SourceNR-ARFC... |
| 2024-09-20 22:21:36.617 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.632 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.733 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.733 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.347 | NREventA3 | measId:2;ServCellPCI:344;Se... |
| 2024-09-20 22:21:38.587 | NRHandoverAttempt | SourcePCI:344;SourceNR-ARFC... |
| 2024-09-20 22:21:38.634 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.645 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.781 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.781 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217632 | 1 | 18.0980 | 9.2814 | -115.8457 | 13.3858 | 142.1827 | 0.0192 | 0.0039 |
| 2024_09_20 22:00 | 3269372 | 2 | 14.4468 | 11.2875 | -117.6578 | 7.0901 | 176.7286 | 0.0148 | 0.0157 |
| 2024_09_20 22:00 | 3273801 | 3 | 11.2524 | 7.0807 | -116.8980 | 15.7966 | 197.4684 | 0.0185 | 0.0053 |
| 2024_09_20 22:00 | 3217065 | 4 | 13.9164 | 15.0930 | -115.9116 | 9.8181 | 178.2762 | 0.0178 | 0.0100 |
| 2024_09_20 22:00 | 3231447 | 5 | 8.4444 | 13.1863 | -116.3070 | 10.9053 | 118.8712 | 0.0148 | 0.0135 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413847_6EFD4B96 | 504990 | 868 | -87.3 | 504990 | 917 | -83.1 | 504990 | 924 | -84.6 | 504990 | 291 |
| MR_1774413847_2A8F4BCB | 504990 | 917 | -85.4 | 504990 | 868 | -83.5 | 504990 | 924 | -85.0 | 504990 | 291 |
| MR_1774413847_E50B06C2 | 504990 | 868 | -85.2 | 504990 | 917 | -86.1 | 504990 | 924 | -87.1 | 504990 | 291 |
| MR_1774413847_1D957051 | 504990 | 917 | -86.1 | 504990 | 868 | -83.4 | 504990 | 924 | -85.0 | 504990 | 291 |
| MR_1774413847_674EC513 | 504990 | 868 | -85.8 | 504990 | 917 | -82.5 | 504990 | 924 | -87.5 | 504990 | 291 |
| MR_1774413847_35F1F584 | 504990 | 868 | -85.7 | 504990 | 917 | -83.5 | 504990 | 924 | -87.7 | 504990 | 291 |
| MR_1774413847_585D9901 | 504990 | 868 | -84.4 | 504990 | 917 | -85.1 | 504990 | 924 | -86.5 | 504990 | 291 |
| MR_1774413847_F1B89769 | 504990 | 917 | -86.2 | 504990 | 868 | -84.0 | 504990 | 924 | -86.5 | 504990 | 291 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1766: `bdbccf38-50a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bdbccf38-50a9-4f8d-bbe8-663d0d9d8821` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1766] topology](images/train_1766.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3221942_3
- `C2`: Adjust the azimuth of 3250669_4 by 50 degrees
- `C3`: Lift the tilt angle of 3250669_4 by 10 degrees
- `C4`: Add neighbor relationship between 3248860_2 and 3221942_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221942_3
- `C6`: Check test server and transmission issues **← 정답**
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250669_4
- `C8`: Decrease A3 Offset threshold for 3221942_3
- `C9`: Increase A3 Offset threshold for 3250669_4
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase transmission power for 3250669_4
- `C12`: Lift the tilt angle  of 3221942_3 by 6 degrees
- `C13`: Adjust the azimuth of 3221942_3 by 50 degrees
- `C14`: Decrease A3 Offset threshold for 3250669_4
- `C15`: Press down the tilt angle of 3250669_4 by 10 degrees
- `C16`: Increase A3 Offset threshold for 3221942_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221942_3
- `C18`: Add neighbor relationship between 3250669_4 and 3221942_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250669_4
- `C20`: Increase transmission power for 3221942_3
- `C21`: Press down the tilt angle  of 3221942_3 by 6 degrees
- `C22`: Decrease transmission power for 3250669_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.802 | MS1 | 121.4656732978 | 31.1446237730 | 287 | 504990 | -91.51 | 12.09 | 550.12 | 0.08 | 2.38 | 1561 |
| 2024-09-20 22:21:32.795 | MS1 | 121.4656721368 | 31.1446249013 | 287 | 504990 | -90.56 | 17.95 | 317.03 | 0.11 | 2.52 | 1596 |
| 2024-09-20 22:21:33.444 | MS1 | 121.4656590875 | 31.1446217798 | 287 | 504990 | -86.51 | 16.76 | 552.06 | 0.02 | 2.81 | 1584 |
| 2024-09-20 22:21:34.151 | MS1 | 121.4656582345 | 31.1446184990 | 287 | 504990 | -89.17 | 16.54 | 59.73 | 0.12 | 2.71 | 499 |
| 2024-09-20 22:21:35.102 | MS1 | 121.4656580741 | 31.1446277471 | 287 | 504990 | -87.51 | 13.36 | 83.32 | 0.07 | 2.87 | 426 |
| 2024-09-20 22:21:36.693 | MS1 | 121.4656670388 | 31.1446264696 | 287 | 504990 | -86.86 | 14.66 | 62.73 | 0.14 | 2.86 | 344 |
| 2024-09-20 22:21:37.726 | MS1 | 121.4656615663 | 31.1446261414 | 287 | 504990 | -89.37 | 11.57 | 97.68 | 0.12 | 2.93 | 488 |
| 2024-09-20 22:21:38.167 | MS1 | 121.4656758868 | 31.1446304902 | 287 | 504990 | -89.57 | 12.72 | 44.67 | 0.09 | 2.36 | 310 |
| 2024-09-20 22:21:39.399 | MS1 | 121.4656659481 | 31.1446282273 | 287 | 504990 | -92.80 | 8.73 | 72.82 | 0.13 | 2.28 | 327 |
| 2024-09-20 22:21:40.971 | MS1 | 121.4656599774 | 31.1446281814 | 287 | 504990 | -89.73 | 10.40 | 466.86 | 0.05 | 2.17 | 1571 |
| 2024-09-20 22:21:41.326 | MS1 | 121.4656604848 | 31.1446238762 | 287 | 504990 | -93.41 | 8.24 | 498.84 | 0.06 | 2.17 | 1560 |
| 2024-09-20 22:21:42.517 | MS1 | 121.4656681256 | 31.1446368410 | 287 | 504990 | -92.10 | 11.85 | 589.39 | 0.05 | 2.02 | 1580 |

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
| 3221285 | 1 | 121.4644891901 | 31.1497767177 | 271 | 0 | 4 | 21.9 | TDD | 897 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3221942 | 3 | 121.4757381590 | 31.1504754139 | 343 | 5 | 7 | 22.4 | TDD | 44 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3248860 | 2 | 121.4730183248 | 31.1490363016 | 68 | 14 | 1 | 47.0 | TDD | 603 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3250669 | 4 | 121.4705318626 | 31.1491849754 | 275 | 9 | 1 | 20.0 | TDD | 287 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.289 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.308 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.443 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.443 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.140 | NREventA3 | measId:2;ServCellPCI:964;Se... |
| 2024-09-20 22:21:38.380 | NRHandoverAttempt | SourcePCI:964;SourceNR-ARFC... |
| 2024-09-20 22:21:38.411 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.424 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.531 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.531 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221285 | 1 | 9.9319 | 19.7325 | -114.2229 | 14.5939 | 138.7368 | 0.0167 | 0.0109 |
| 2024_09_20 22:00 | 3248860 | 2 | 8.0896 | 12.7547 | -117.8087 | 10.6893 | 101.3033 | 0.0189 | 0.0119 |
| 2024_09_20 22:00 | 3221942 | 3 | 17.2921 | 6.0158 | -116.5881 | 10.6815 | 160.6893 | 0.0072 | 0.0185 |
| 2024_09_20 22:00 | 3250669 | 4 | 8.1292 | 6.9826 | -117.1965 | 10.3070 | 179.0398 | 0.0057 | 0.0071 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417199_B4655FE9 | 504990 | 287 | -87.5 | 504990 | 44 | -97.0 | 504990 | 603 | -96.0 | 504990 | 897 |
| MR_1774417199_97D7070A | 504990 | 287 | -88.0 | 504990 | 44 | -96.2 | 504990 | 603 | -99.3 | 504990 | 897 |
| MR_1774417199_83ECB5A9 | 504990 | 287 | -90.2 | 504990 | 44 | -98.3 | 504990 | 603 | -96.4 | 504990 | 897 |
| MR_1774417199_4362447C | 504990 | 287 | -89.8 | 504990 | 44 | -98.7 | 504990 | 603 | -98.1 | 504990 | 897 |
| MR_1774417199_61D245DE | 504990 | 287 | -88.9 | 504990 | 44 | -97.7 | 504990 | 603 | -96.6 | 504990 | 897 |
| MR_1774417199_455814C8 | 504990 | 287 | -87.8 | 504990 | 44 | -95.8 | 504990 | 603 | -99.4 | 504990 | 897 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1767: `55bc7b0b-a0c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `55bc7b0b-a0ce-4487-94e9-25f538cf2358` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1767] topology](images/train_1767.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3224129_1 by 7 degrees
- `C2`: Decrease transmission power for 3216262_3
- `C3`: Increase A3 Offset threshold for 3224129_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216262_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216262_3
- `C6`: Add neighbor relationship between 3216262_3 and 3224129_1
- `C7`: Decrease A3 Offset threshold for 3224129_1
- `C8`: Decrease transmission power for 3224129_1
- `C9`: Adjust the azimuth of 3216262_3 by 21 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224129_1
- `C11`: Add neighbor relationship between 3256300_2 and 3224129_1
- `C12`: Press down the tilt angle of 3216262_3 by 10 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224129_1
- `C14`: Increase transmission power for 3216262_3
- `C15`: Lift the tilt angle  of 3224129_1 by 7 degrees
- `C16`: Decrease A3 Offset threshold for 3216262_3
- `C17`: Adjust the azimuth of 3224129_1 by 33 degrees
- `C18`: Increase A3 Offset threshold for 3216262_3
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Check test server and transmission issues **← 정답**
- `C21`: Lift the tilt angle of 3216262_3 by 10 degrees
- `C22`: Increase transmission power for 3224129_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.311 | MS1 | 121.4656779089 | 31.1446266386 | 390 | 504990 | -91.97 | 13.93 | 531.96 | 0.02 | 2.93 | 1565 |
| 2024-09-20 22:21:32.678 | MS1 | 121.4656590035 | 31.1446292046 | 390 | 504990 | -89.06 | 13.59 | 358.38 | 0.14 | 2.00 | 1560 |
| 2024-09-20 22:21:33.232 | MS1 | 121.4656681884 | 31.1446267300 | 390 | 504990 | -88.84 | 13.95 | 343.05 | 0.09 | 2.80 | 1588 |
| 2024-09-20 22:21:34.444 | MS1 | 121.4656766879 | 31.1446229659 | 390 | 504990 | -88.55 | 16.62 | 79.43 | 0.12 | 2.01 | 308 |
| 2024-09-20 22:21:35.356 | MS1 | 121.4656670553 | 31.1446317323 | 390 | 504990 | -88.12 | 14.74 | 53.88 | 0.03 | 2.34 | 306 |
| 2024-09-20 22:21:36.811 | MS1 | 121.4656605619 | 31.1446346252 | 390 | 504990 | -89.36 | 12.02 | 91.58 | 0.19 | 2.11 | 345 |
| 2024-09-20 22:21:37.549 | MS1 | 121.4656604254 | 31.1446304544 | 390 | 504990 | -92.17 | 9.45 | 67.28 | 0.17 | 2.19 | 497 |
| 2024-09-20 22:21:38.542 | MS1 | 121.4656696169 | 31.1446327790 | 390 | 504990 | -90.89 | 12.09 | 56.32 | 0.04 | 2.58 | 461 |
| 2024-09-20 22:21:39.569 | MS1 | 121.4656643936 | 31.1446362954 | 390 | 504990 | -89.48 | 9.94 | 88.03 | 0.08 | 2.90 | 467 |
| 2024-09-20 22:21:40.573 | MS1 | 121.4656634730 | 31.1446322360 | 390 | 504990 | -93.97 | 11.18 | 478.81 | 0.07 | 2.13 | 1573 |
| 2024-09-20 22:21:41.976 | MS1 | 121.4656754717 | 31.1446316078 | 390 | 504990 | -92.35 | 11.89 | 334.28 | 0.16 | 2.57 | 1591 |
| 2024-09-20 22:21:42.923 | MS1 | 121.4656692484 | 31.1446230146 | 390 | 504990 | -93.29 | 8.16 | 541.22 | 0.18 | 2.07 | 1566 |

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
| 3216262 | 3 | 121.4672276235 | 31.1534741507 | 168 | 8 | 12 | 27.3 | TDD | 390 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3224129 | 1 | 121.4721756032 | 31.1443083985 | 240 | 3 | 9 | 39.4 | TDD | 416 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3254451 | 4 | 121.4700596239 | 31.1514502167 | 66 | 1 | 12 | 26.0 | TDD | 23 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3256300 | 2 | 121.4742189241 | 31.1458066236 | 41 | 13 | 12 | 36.5 | TDD | 998 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.459 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.480 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.582 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.582 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.285 | NREventA3 | measId:2;ServCellPCI:1002;S... |
| 2024-09-20 22:21:38.525 | NRHandoverAttempt | SourcePCI:1002;SourceNR-ARF... |
| 2024-09-20 22:21:38.569 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.582 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.708 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.708 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224129 | 1 | 6.9897 | 15.0863 | -117.1095 | 6.3660 | 198.7838 | 0.0009 | 0.0055 |
| 2024_09_20 22:00 | 3256300 | 2 | 12.5338 | 13.7678 | -116.7538 | 16.1916 | 176.4424 | 0.0040 | 0.0040 |
| 2024_09_20 22:00 | 3216262 | 3 | 10.8564 | 5.3933 | -115.5629 | 8.8100 | 157.9554 | 0.0180 | 0.0176 |
| 2024_09_20 22:00 | 3254451 | 4 | 14.3594 | 9.6268 | -117.7386 | 12.5141 | 159.9882 | 0.0043 | 0.0115 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414293_AF714CCA | 504990 | 390 | -88.9 | 504990 | 416 | -93.2 | 504990 | 998 | -102.9 | 504990 | 23 |
| MR_1774414293_4B50E6E0 | 504990 | 390 | -89.3 | 504990 | 416 | -94.3 | 504990 | 998 | -103.0 | 504990 | 23 |
| MR_1774414293_E2C2FC42 | 504990 | 390 | -87.1 | 504990 | 416 | -94.9 | 504990 | 998 | -101.3 | 504990 | 23 |
| MR_1774414293_814E9A3E | 504990 | 390 | -87.4 | 504990 | 416 | -93.4 | 504990 | 998 | -99.5 | 504990 | 23 |
| MR_1774414293_6A278EE2 | 504990 | 390 | -88.0 | 504990 | 416 | -92.8 | 504990 | 998 | -102.5 | 504990 | 23 |
| MR_1774414293_C3A9CAB8 | 504990 | 390 | -88.3 | 504990 | 416 | -93.9 | 504990 | 998 | -103.3 | 504990 | 23 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1768: `98e3f7ea-400...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `98e3f7ea-400f-4a41-a8b3-6106c6df5fec` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease A3 Offset threshold for 3222703_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1768] topology](images/train_1768.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3226013_4 by 50 degrees
- `C2`: Decrease transmission power for 3226013_4
- `C3`: Lift the tilt angle of 3222703_2 by 6 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226013_4
- `C5`: Add neighbor relationship between 3222703_2 and 3226013_4
- `C6`: Increase transmission power for 3222703_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222703_2
- `C8`: Decrease A3 Offset threshold for 3226013_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226013_4
- `C10`: Check test server and transmission issues
- `C11`: Lift the tilt angle  of 3226013_4 by 2 degrees
- `C12`: Increase transmission power for 3226013_4
- `C13`: Press down the tilt angle  of 3226013_4 by 2 degrees
- `C14`: Increase A3 Offset threshold for 3226013_4
- `C15`: Increase A3 Offset threshold for 3222703_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease transmission power for 3222703_2
- `C18`: Add neighbor relationship between 3270321_1 and 3226013_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222703_2
- `C20`: Adjust the azimuth of 3222703_2 by 44 degrees
- `C21`: Press down the tilt angle of 3222703_2 by 6 degrees
- `C22`: Decrease A3 Offset threshold for 3222703_2 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.928 | MS1 | 121.4656762305 | 31.1446202172 | 587 | 504990 | -78.58 | 16.91 | 478.46 | 0.16 | 2.61 | 1592 |
| 2024-09-20 22:21:32.353 | MS1 | 121.4656744117 | 31.1446325768 | 587 | 504990 | -82.05 | 17.46 | 355.91 | 0.02 | 2.58 | 1586 |
| 2024-09-20 22:21:33.975 | MS1 | 121.4656609252 | 31.1446296556 | 587 | 504990 | -79.21 | 16.39 | 502.15 | 0.06 | 2.69 | 1561 |
| 2024-09-20 22:21:34.865 | MS1 | 121.4656633413 | 31.1446235009 | 587 | 504990 | -84.23 | -0.92 | 66.61 | 0.06 | 1.30 | 1566 |
| 2024-09-20 22:21:35.731 | MS1 | 121.4656600683 | 31.1446355373 | 587 | 504990 | -87.66 | -2.81 | 53.72 | 0.18 | 1.23 | 1582 |
| 2024-09-20 22:21:36.334 | MS1 | 121.4656584707 | 31.1446208409 | 587 | 504990 | -91.83 | -2.07 | 60.85 | 0.17 | 1.20 | 1564 |
| 2024-09-20 22:21:37.996 | MS1 | 121.4656764268 | 31.1446340724 | 587 | 504990 | -86.71 | -3.67 | 73.07 | 0.02 | 1.23 | 1572 |
| 2024-09-20 22:21:38.157 | MS1 | 121.4656718126 | 31.1446188753 | 587 | 504990 | -86.16 | -0.73 | 33.72 | 0.01 | 1.06 | 1585 |
| 2024-09-20 22:21:39.401 | MS1 | 121.4656666931 | 31.1446263562 | 78 | 504990 | -75.22 | 15.17 | 266.03 | 0.17 | 1.29 | 1589 |
| 2024-09-20 22:21:40.786 | MS1 | 121.4656713359 | 31.1446328171 | 78 | 504990 | -81.85 | 12.81 | 300.88 | 0.14 | 2.24 | 1596 |
| 2024-09-20 22:21:41.373 | MS1 | 121.4656601362 | 31.1446329222 | 78 | 504990 | -77.11 | 15.18 | 318.32 | 0.01 | 2.21 | 1583 |
| 2024-09-20 22:21:42.521 | MS1 | 121.4656718757 | 31.1446269295 | 78 | 504990 | -79.59 | 12.86 | 395.04 | 0.17 | 2.45 | 1578 |

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
| 3220697 | 3 | 121.4718125406 | 31.1519453037 | 263 | 5 | 5 | 33.1 | TDD | 844 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3222703 | 2 | 121.4705519738 | 31.1457707615 | 211 | 2 | 9 | 36.8 | TDD | 587 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3226013 | 4 | 121.4739070159 | 31.1537433512 | 330 | 1 | 6 | 32.2 | TDD | 78 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3270321 | 1 | 121.4758944393 | 31.1527923548 | 239 | 5 | 2 | 38.2 | TDD | 649 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.190 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.213 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.362 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.362 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.045 | NREventA3 | measId:2;ServCellPCI:963;Se... |
| 2024-09-20 22:21:38.285 | NRHandoverAttempt | SourcePCI:963;SourceNR-ARFC... |
| 2024-09-20 22:21:38.325 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.339 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.449 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.449 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270321 | 1 | 8.6678 | 9.5848 | -114.0032 | 19.3079 | 119.9678 | 0.0104 | 0.0027 |
| 2024_09_20 22:00 | 3222703 | 2 | 17.2403 | 12.6623 | -115.5653 | 19.4751 | 116.5965 | 0.0020 | 0.1844 |
| 2024_09_20 22:00 | 3220697 | 3 | 13.6046 | 10.0305 | -114.8539 | 19.9488 | 188.2396 | 0.0060 | 0.0182 |
| 2024_09_20 22:00 | 3226013 | 4 | 15.0242 | 18.0317 | -116.9092 | 9.4842 | 168.3086 | 0.0128 | 0.0088 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415783_9C16A928 | 504990 | 587 | -82.4 | 504990 | 78 | -78.7 | 504990 | 649 | -90.5 | 504990 | 844 |
| MR_1774415783_05C16128 | 504990 | 587 | -82.7 | 504990 | 78 | -80.3 | 504990 | 649 | -90.1 | 504990 | 844 |
| MR_1774415783_085C4FA4 | 504990 | 587 | -82.6 | 504990 | 78 | -78.3 | 504990 | 649 | -91.2 | 504990 | 844 |
| MR_1774415783_D7054763 | 504990 | 78 | -81.4 | 504990 | 587 | -86.1 | 504990 | 649 | -90.4 | 504990 | 844 |
| MR_1774415783_5D2E3918 | 504990 | 587 | -83.6 | 504990 | 78 | -79.9 | 504990 | 649 | -91.1 | 504990 | 844 |
| MR_1774415783_ACD6125E | 504990 | 587 | -85.6 | 504990 | 78 | -78.1 | 504990 | 649 | -89.4 | 504990 | 844 |
| MR_1774415783_AAEBF33F | 504990 | 587 | -84.0 | 504990 | 78 | -79.5 | 504990 | 649 | -87.3 | 504990 | 844 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1769: `f0044604-913...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f0044604-9135-4bde-9f9d-8f1f148f1b4b` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease A3 Offset threshold for 3213351_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1769] topology](images/train_1769.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214772_1
- `C2`: Check test server and transmission issues
- `C3`: Add neighbor relationship between 3254102_4 and 3214772_1
- `C4`: Lift the tilt angle  of 3214772_1 by 10 degrees
- `C5`: Lift the tilt angle of 3213351_2 by 5 degrees
- `C6`: Decrease A3 Offset threshold for 3214772_1
- `C7`: Adjust the azimuth of 3213351_2 by 50 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213351_2
- `C9`: Decrease transmission power for 3214772_1
- `C10`: Decrease A3 Offset threshold for 3213351_2 **← 정답**
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213351_2
- `C12`: Increase transmission power for 3214772_1
- `C13`: Add neighbor relationship between 3213351_2 and 3214772_1
- `C14`: Adjust the azimuth of 3214772_1 by 36 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214772_1
- `C16`: Increase A3 Offset threshold for 3213351_2
- `C17`: Decrease transmission power for 3213351_2
- `C18`: Press down the tilt angle of 3213351_2 by 5 degrees
- `C19`: Increase transmission power for 3213351_2
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase A3 Offset threshold for 3214772_1
- `C22`: Press down the tilt angle  of 3214772_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.172 | MS1 | 121.4656749772 | 31.1446201587 | 654 | 504990 | -81.14 | 14.92 | 431.10 | 0.11 | 2.95 | 1589 |
| 2024-09-20 22:21:32.826 | MS1 | 121.4656699687 | 31.1446307871 | 654 | 504990 | -79.20 | 17.93 | 520.43 | 0.11 | 2.17 | 1581 |
| 2024-09-20 22:21:33.145 | MS1 | 121.4656739394 | 31.1446376413 | 654 | 504990 | -78.59 | 17.65 | 339.54 | 0.07 | 2.25 | 1580 |
| 2024-09-20 22:21:34.345 | MS1 | 121.4656708841 | 31.1446213517 | 654 | 504990 | -91.21 | -3.91 | 23.76 | 0.12 | 1.22 | 1599 |
| 2024-09-20 22:21:35.440 | MS1 | 121.4656702766 | 31.1446269522 | 654 | 504990 | -90.15 | -3.96 | 56.78 | 0.17 | 1.49 | 1589 |
| 2024-09-20 22:21:36.232 | MS1 | 121.4656685176 | 31.1446375309 | 654 | 504990 | -86.85 | -2.56 | 45.66 | 0.12 | 1.21 | 1567 |
| 2024-09-20 22:21:37.229 | MS1 | 121.4656673218 | 31.1446303525 | 654 | 504990 | -86.30 | -0.32 | 24.97 | 0.18 | 1.03 | 1590 |
| 2024-09-20 22:21:38.823 | MS1 | 121.4656664327 | 31.1446231240 | 654 | 504990 | -88.12 | -2.62 | 42.79 | 0.09 | 1.08 | 1571 |
| 2024-09-20 22:21:39.348 | MS1 | 121.4656655749 | 31.1446182143 | 730 | 504990 | -75.52 | 14.24 | 151.85 | 0.11 | 1.18 | 1562 |
| 2024-09-20 22:21:40.661 | MS1 | 121.4656610316 | 31.1446355568 | 730 | 504990 | -81.50 | 17.86 | 496.40 | 0.03 | 2.41 | 1576 |
| 2024-09-20 22:21:41.214 | MS1 | 121.4656742057 | 31.1446236792 | 730 | 504990 | -82.78 | 14.77 | 332.39 | 0.19 | 2.47 | 1583 |
| 2024-09-20 22:21:42.806 | MS1 | 121.4656753044 | 31.1446275047 | 730 | 504990 | -84.56 | 15.03 | 528.73 | 0.03 | 2.30 | 1564 |

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
| 3213351 | 2 | 121.4704494065 | 31.1506286616 | 133 | 1 | 1 | 49.6 | TDD | 654 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3214772 | 1 | 121.4653749331 | 31.1556201871 | 215 | 15 | 6 | 24.0 | TDD | 730 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3254102 | 4 | 121.4741296029 | 31.1486731918 | 237 | 13 | 9 | 15.1 | TDD | 62 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3275087 | 3 | 121.4755833370 | 31.1534091026 | 137 | 11 | 6 | 16.7 | TDD | 764 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.396 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.412 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.525 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.525 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.251 | NREventA3 | measId:2;ServCellPCI:472;Se... |
| 2024-09-20 22:21:38.491 | NRHandoverAttempt | SourcePCI:472;SourceNR-ARFC... |
| 2024-09-20 22:21:38.529 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.540 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.673 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.673 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214772 | 1 | 12.1122 | 8.7884 | -114.2581 | 9.8764 | 98.6066 | 0.0149 | 0.0131 |
| 2024_09_20 22:00 | 3213351 | 2 | 10.7370 | 8.0059 | -117.7766 | 10.8575 | 169.1622 | 0.0040 | 0.1482 |
| 2024_09_20 22:00 | 3275087 | 3 | 7.9537 | 10.9119 | -114.0563 | 18.7923 | 140.0860 | 0.0026 | 0.0181 |
| 2024_09_20 22:00 | 3254102 | 4 | 6.0403 | 15.2887 | -117.8510 | 10.6548 | 188.9577 | 0.0104 | 0.0106 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412401_941C0AC5 | 504990 | 654 | -91.8 | 504990 | 730 | -86.7 | 504990 | 62 | -94.6 | 504990 | 764 |
| MR_1774412401_57449DA5 | 504990 | 730 | -87.7 | 504990 | 654 | -90.5 | 504990 | 62 | -94.9 | 504990 | 764 |
| MR_1774412401_0FA286CD | 504990 | 654 | -92.4 | 504990 | 730 | -87.9 | 504990 | 62 | -92.8 | 504990 | 764 |
| MR_1774412401_B9DC8120 | 504990 | 654 | -93.2 | 504990 | 730 | -84.9 | 504990 | 62 | -94.5 | 504990 | 764 |
| MR_1774412401_E4B33EDB | 504990 | 730 | -85.3 | 504990 | 654 | -92.2 | 504990 | 62 | -93.4 | 504990 | 764 |

> *... 2개 열 생략 (전체 14열)*

---
