# Track A 문제 분석 — train[1720]~train[1729]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1720] ~ train[1729] (10개)

## 목차

1. [문제 1720: `edb1e9c0-36a...`](#1720) — single-answer, 정답: C15
2. [문제 1721: `83b3b795-8f4...`](#1721) — single-answer, 정답: C22
3. [문제 1722: `05e1ca9c-f52...`](#1722) — single-answer, 정답: C8
4. [문제 1723: `d92b5f5d-6ee...`](#1723) — single-answer, 정답: C16
5. [문제 1724: `4d362eb6-837...`](#1724) — single-answer, 정답: C4
6. [문제 1725: `236316c6-2c2...`](#1725) — single-answer, 정답: C13
7. [문제 1726: `088415b4-ed2...`](#1726) — multiple-answer, 정답: C1|C22
8. [문제 1727: `99dabe7c-f6d...`](#1727) — single-answer, 정답: C7
9. [문제 1728: `d6e59c80-fc3...`](#1728) — single-answer, 정답: C5
10. [문제 1729: `6b82f286-e6f...`](#1729) — single-answer, 정답: C9

---

### 문제 1720: `edb1e9c0-36a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `edb1e9c0-36a4-469e-86f4-6311f6bfa665` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Add neighbor relationship between 3267466_3 and 3224153_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1720] topology](images/train_1720.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224153_4
- `C3`: Decrease transmission power for 3224153_4
- `C4`: Increase A3 Offset threshold for 3267466_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224153_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267466_3
- `C7`: Increase transmission power for 3224153_4
- `C8`: Decrease A3 Offset threshold for 3224153_4
- `C9`: Lift the tilt angle  of 3224153_4 by 6 degrees
- `C10`: Increase A3 Offset threshold for 3224153_4
- `C11`: Adjust the azimuth of 3267466_3 by 50 degrees
- `C12`: Decrease A3 Offset threshold for 3267466_3
- `C13`: Adjust the azimuth of 3224153_4 by 19 degrees
- `C14`: Press down the tilt angle of 3267466_3 by 10 degrees
- `C15`: Add neighbor relationship between 3267466_3 and 3224153_4 **← 정답**
- `C16`: Decrease transmission power for 3267466_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267466_3
- `C18`: Lift the tilt angle of 3267466_3 by 10 degrees
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle  of 3224153_4 by 6 degrees
- `C21`: Increase transmission power for 3267466_3
- `C22`: Add neighbor relationship between 3247249_1 and 3224153_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.374 | MS1 | 121.4656724992 | 31.1446304330 | 286 | 504990 | -75.24 | 17.18 | 412.58 | 0.15 | 2.25 | 1568 |
| 2024-09-20 22:21:32.848 | MS1 | 121.4656676261 | 31.1446284943 | 286 | 504990 | -79.23 | 16.86 | 445.36 | 0.03 | 2.63 | 1573 |
| 2024-09-20 22:21:33.556 | MS1 | 121.4656589741 | 31.1446269470 | 286 | 504990 | -82.95 | 14.72 | 302.77 | 0.14 | 2.56 | 1573 |
| 2024-09-20 22:21:34.149 | MS1 | 121.4656640283 | 31.1446301476 | 286 | 504990 | -87.80 | -0.77 | 42.17 | 0.11 | 1.22 | 1585 |
| 2024-09-20 22:21:35.648 | MS1 | 121.4656589063 | 31.1446378314 | 286 | 504990 | -91.88 | -3.34 | 46.56 | 0.19 | 1.18 | 1572 |
| 2024-09-20 22:21:36.761 | MS1 | 121.4656661410 | 31.1446208110 | 286 | 504990 | -88.37 | -0.94 | 56.94 | 0.14 | 1.43 | 1578 |
| 2024-09-20 22:21:37.832 | MS1 | 121.4656742815 | 31.1446274390 | 286 | 504990 | -86.51 | -3.26 | 55.10 | 0.19 | 1.04 | 1596 |
| 2024-09-20 22:21:38.670 | MS1 | 121.4656698180 | 31.1446328078 | 286 | 504990 | -77.54 | 17.23 | 594.88 | 0.03 | 1.18 | 1570 |
| 2024-09-20 22:21:39.555 | MS1 | 121.4656713396 | 31.1446321649 | 286 | 504990 | -82.79 | 13.09 | 435.42 | 0.00 | 1.04 | 1567 |
| 2024-09-20 22:21:40.580 | MS1 | 121.4656759240 | 31.1446282891 | 286 | 504990 | -84.34 | 15.48 | 566.82 | 0.17 | 2.42 | 1570 |
| 2024-09-20 22:21:41.214 | MS1 | 121.4656728509 | 31.1446351114 | 286 | 504990 | -82.57 | 12.79 | 301.36 | 0.13 | 2.65 | 1597 |
| 2024-09-20 22:21:42.470 | MS1 | 121.4656589786 | 31.1446325072 | 286 | 504990 | -83.79 | 12.75 | 405.57 | 0.02 | 2.36 | 1560 |

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
| 3224153 | 4 | 121.4756879221 | 31.1522560609 | 209 | 5 | 11 | 17.0 | TDD | 623 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3224979 | 2 | 121.4659536043 | 31.1475457200 | 257 | 14 | 8 | 24.1 | TDD | 947 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3247249 | 1 | 121.4642093344 | 31.1460917907 | 108 | 7 | 4 | 15.2 | TDD | 90 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3267466 | 3 | 121.4660852757 | 31.1530901348 | 346 | 14 | 9 | 46.6 | TDD | 286 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.025 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.040 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.151 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.151 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.850 | NREventA3 | measId:2;ServCellPCI:253;Se... |
| 2024-09-20 22:21:35.850 | NREventA3 | measId:2;ServCellPCI:253;Se... |
| 2024-09-20 22:21:36.850 | NREventA3 | measId:2;ServCellPCI:253;Se... |
| 2024-09-20 22:21:39.350 | NRRRCReestablishAttempt | PCI:253 |
| 2024-09-20 22:21:39.363 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.376 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.511 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.511 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247249 | 1 | 16.3806 | 6.5142 | -114.3095 | 15.1958 | 80.7144 | 0.0038 | 0.0190 |
| 2024_09_20 22:00 | 3224979 | 2 | 17.5056 | 13.2074 | -117.2696 | 15.8503 | 191.9119 | 0.0059 | 0.0135 |
| 2024_09_20 22:00 | 3267466 | 3 | 17.5556 | 15.6228 | -114.0618 | 19.5172 | 117.6242 | 0.0124 | 0.1193 |
| 2024_09_20 22:00 | 3224153 | 4 | 17.9724 | 14.1677 | -116.7148 | 18.6745 | 178.8720 | 0.0061 | 0.0144 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413908_464025F0 | 504990 | 623 | -83.2 | 504990 | 286 | -86.0 | 504990 | 90 | -90.7 | 504990 | 947 |
| MR_1774413908_9B1B9D34 | 504990 | 286 | -86.2 | 504990 | 623 | -83.4 | 504990 | 90 | -90.5 | 504990 | 947 |
| MR_1774413908_DA112EC2 | 504990 | 623 | -83.9 | 504990 | 286 | -86.0 | 504990 | 90 | -90.9 | 504990 | 947 |
| MR_1774413908_33B52B0A | 504990 | 623 | -83.0 | 504990 | 286 | -86.8 | 504990 | 90 | -92.4 | 504990 | 947 |
| MR_1774413908_E03DF479 | 504990 | 623 | -83.1 | 504990 | 286 | -86.2 | 504990 | 90 | -89.2 | 504990 | 947 |
| MR_1774413908_943F2162 | 504990 | 623 | -82.1 | 504990 | 286 | -87.3 | 504990 | 90 | -89.9 | 504990 | 947 |
| MR_1774413908_E682F50F | 504990 | 286 | -88.7 | 504990 | 623 | -84.7 | 504990 | 90 | -90.1 | 504990 | 947 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1721: `83b3b795-8f4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `83b3b795-8f4c-4112-876f-efba3c38200c` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Lift the tilt angle  of 3271497_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1721] topology](images/train_1721.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3245715_2
- `C2`: Increase transmission power for 3245715_2
- `C3`: Check test server and transmission issues
- `C4`: Adjust the azimuth of 3244128_1 by 34 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245715_2
- `C6`: Decrease A3 Offset threshold for 3244128_1
- `C7`: Adjust the azimuth of 3271497_3 by 48 degrees
- `C8`: Add neighbor relationship between 3271497_3 and 3245715_2
- `C9`: Press down the tilt angle  of 3271497_3 by 10 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244128_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245715_2
- `C12`: Lift the tilt angle of 3244128_1 by 1 degrees
- `C13`: Increase transmission power for 3244128_1
- `C14`: Add neighbor relationship between 3244128_1 and 3245715_2
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Press down the tilt angle of 3244128_1 by 1 degrees
- `C17`: Increase A3 Offset threshold for 3244128_1
- `C18`: Increase A3 Offset threshold for 3245715_2
- `C19`: Decrease transmission power for 3244128_1
- `C20`: Decrease A3 Offset threshold for 3245715_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244128_1
- `C22`: Lift the tilt angle  of 3271497_3 by 10 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.563 | MS1 | 121.4656727856 | 31.1446191269 | 609 | 504990 | -91.42 | 16.42 | 486.95 | 0.16 | 2.70 | 1563 |
| 2024-09-20 22:21:32.107 | MS1 | 121.4656645949 | 31.1446214563 | 609 | 504990 | -91.32 | 14.51 | 424.60 | 0.05 | 2.19 | 1584 |
| 2024-09-20 22:21:33.834 | MS1 | 121.4656741860 | 31.1446187975 | 609 | 504990 | -89.83 | 13.25 | 307.04 | 0.10 | 2.68 | 1587 |
| 2024-09-20 22:21:34.607 | MS1 | 121.4656708432 | 31.1446255589 | 609 | 504990 | -88.78 | 16.52 | 79.47 | 0.14 | 2.80 | 1584 |
| 2024-09-20 22:21:35.398 | MS1 | 121.4656723530 | 31.1446246438 | 609 | 504990 | -91.09 | 12.61 | 76.11 | 0.16 | 2.19 | 1566 |
| 2024-09-20 22:21:36.285 | MS1 | 121.4656631897 | 31.1446360930 | 609 | 504990 | -86.14 | 17.20 | 57.74 | 0.17 | 2.57 | 1584 |
| 2024-09-20 22:21:37.932 | MS1 | 121.4656746819 | 31.1446196452 | 609 | 504990 | -90.11 | 12.93 | 56.11 | 0.01 | 2.11 | 1582 |
| 2024-09-20 22:21:38.816 | MS1 | 121.4656588111 | 31.1446264516 | 609 | 504990 | -91.51 | 12.71 | 84.13 | 0.08 | 2.92 | 1571 |
| 2024-09-20 22:21:39.426 | MS1 | 121.4656628433 | 31.1446251921 | 609 | 504990 | -90.99 | 11.91 | 90.24 | 0.12 | 2.49 | 1597 |
| 2024-09-20 22:21:40.112 | MS1 | 121.4656603108 | 31.1446344559 | 609 | 504990 | -92.03 | 12.51 | 527.05 | 0.07 | 2.21 | 1575 |
| 2024-09-20 22:21:41.732 | MS1 | 121.4656632410 | 31.1446278567 | 609 | 504990 | -91.95 | 12.96 | 469.32 | 0.19 | 2.01 | 1600 |
| 2024-09-20 22:21:42.716 | MS1 | 121.4656670880 | 31.1446258631 | 609 | 504990 | -89.10 | 7.64 | 450.65 | 0.16 | 2.13 | 1592 |

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
| 3244128 | 1 | 121.4734184819 | 31.1553263837 | 178 | 0 | 8 | 20.5 | TDD | 609 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3245715 | 2 | 121.4655303880 | 31.1550968700 | 131 | 8 | 5 | 42.4 | TDD | 28 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3271497 | 3 | 121.4730267777 | 31.1528888138 | 18 | 9 | 2 | 19.7 | TDD | 813 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3276732 | 4 | 121.4659186235 | 31.1534638914 | 78 | 4 | 0 | 33.7 | TDD | 949 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.063 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.079 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.189 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.189 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.932 | NREventA3 | measId:2;ServCellPCI:576;Se... |
| 2024-09-20 22:21:38.172 | NRHandoverAttempt | SourcePCI:576;SourceNR-ARFC... |
| 2024-09-20 22:21:38.222 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.232 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.340 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.340 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244128 | 1 | 91.4633 | 94.2055 | -115.1960 | 6.2586 | 196.6188 | 0.0131 | 0.0012 |
| 2024_09_20 22:00 | 3245715 | 2 | 19.7457 | 15.6957 | -114.0344 | 9.6988 | 149.2675 | 0.0020 | 0.0013 |
| 2024_09_20 22:00 | 3271497 | 3 | 13.3975 | 11.0687 | -117.4159 | 6.6446 | 164.3488 | 0.0096 | 0.0089 |
| 2024_09_20 22:00 | 3276732 | 4 | 8.7566 | 8.2005 | -116.7257 | 17.8201 | 131.4313 | 0.0076 | 0.0140 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413174_197D6937 | 504990 | 609 | -90.0 | 504990 | 28 | -95.1 | 504990 | 813 | -98.1 | 504990 | 949 |
| MR_1774413174_95C20CBC | 504990 | 609 | -87.7 | 504990 | 28 | -94.8 | 504990 | 813 | -97.5 | 504990 | 949 |
| MR_1774413174_C8A7D7A7 | 504990 | 609 | -87.2 | 504990 | 28 | -96.0 | 504990 | 813 | -98.2 | 504990 | 949 |
| MR_1774413174_6DE57523 | 504990 | 609 | -88.8 | 504990 | 28 | -94.8 | 504990 | 813 | -96.5 | 504990 | 949 |
| MR_1774413174_0D08D7D0 | 504990 | 609 | -87.5 | 504990 | 28 | -97.3 | 504990 | 813 | -98.4 | 504990 | 949 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1722: `05e1ca9c-f52...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `05e1ca9c-f52c-418b-9790-7b6f3a674638` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease A3 Offset threshold for 3224971_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1722] topology](images/train_1722.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3224971_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254612_4
- `C3`: Increase A3 Offset threshold for 3254612_4
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Press down the tilt angle of 3224971_3 by 10 degrees
- `C6`: Increase transmission power for 3254612_4
- `C7`: Press down the tilt angle  of 3254612_4 by 2 degrees
- `C8`: Decrease A3 Offset threshold for 3224971_3 **← 정답**
- `C9`: Decrease A3 Offset threshold for 3254612_4
- `C10`: Adjust the azimuth of 3224971_3 by 50 degrees
- `C11`: Lift the tilt angle of 3224971_3 by 10 degrees
- `C12`: Adjust the azimuth of 3254612_4 by 43 degrees
- `C13`: Check test server and transmission issues
- `C14`: Decrease transmission power for 3254612_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224971_3
- `C16`: Increase transmission power for 3224971_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254612_4
- `C18`: Lift the tilt angle  of 3254612_4 by 2 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224971_3
- `C20`: Decrease transmission power for 3224971_3
- `C21`: Add neighbor relationship between 3277571_1 and 3254612_4
- `C22`: Add neighbor relationship between 3224971_3 and 3254612_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.402 | MS1 | 121.4656616493 | 31.1446244266 | 419 | 504990 | -77.77 | 14.33 | 541.54 | 0.14 | 2.55 | 1576 |
| 2024-09-20 22:21:32.586 | MS1 | 121.4656704928 | 31.1446351041 | 419 | 504990 | -78.03 | 14.01 | 336.64 | 0.18 | 2.90 | 1569 |
| 2024-09-20 22:21:33.924 | MS1 | 121.4656693626 | 31.1446276390 | 419 | 504990 | -77.46 | 12.80 | 501.44 | 0.16 | 2.60 | 1592 |
| 2024-09-20 22:21:34.749 | MS1 | 121.4656768490 | 31.1446254207 | 419 | 504990 | -90.00 | -0.77 | 69.41 | 0.12 | 1.09 | 1591 |
| 2024-09-20 22:21:35.756 | MS1 | 121.4656688491 | 31.1446234588 | 419 | 504990 | -85.40 | -1.73 | 48.79 | 0.19 | 1.11 | 1567 |
| 2024-09-20 22:21:36.378 | MS1 | 121.4656669535 | 31.1446224863 | 419 | 504990 | -90.27 | -2.11 | 59.43 | 0.00 | 1.30 | 1569 |
| 2024-09-20 22:21:37.766 | MS1 | 121.4656608884 | 31.1446261739 | 419 | 504990 | -89.08 | -3.82 | 43.33 | 0.05 | 1.34 | 1573 |
| 2024-09-20 22:21:38.650 | MS1 | 121.4656761351 | 31.1446377061 | 419 | 504990 | -89.53 | -0.52 | 57.34 | 0.16 | 1.33 | 1567 |
| 2024-09-20 22:21:39.944 | MS1 | 121.4656728557 | 31.1446244353 | 588 | 504990 | -76.66 | 15.96 | 216.45 | 0.13 | 1.43 | 1572 |
| 2024-09-20 22:21:40.765 | MS1 | 121.4656690240 | 31.1446258901 | 588 | 504990 | -80.17 | 14.93 | 561.96 | 0.01 | 2.48 | 1580 |
| 2024-09-20 22:21:41.360 | MS1 | 121.4656686419 | 31.1446297428 | 588 | 504990 | -75.22 | 12.28 | 597.32 | 0.12 | 2.36 | 1570 |
| 2024-09-20 22:21:42.818 | MS1 | 121.4656777573 | 31.1446235038 | 588 | 504990 | -81.08 | 12.29 | 364.02 | 0.12 | 2.45 | 1579 |

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
| 3224505 | 2 | 121.4698933959 | 31.1473000286 | 187 | 14 | 7 | 25.2 | TDD | 618 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3224971 | 3 | 121.4667830614 | 31.1537054471 | 256 | 9 | 6 | 25.7 | TDD | 419 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3254612 | 4 | 121.4701704369 | 31.1534167481 | 247 | 0 | 1 | 37.6 | TDD | 588 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3277571 | 1 | 121.4757041056 | 31.1442448053 | 123 | 5 | 3 | 48.7 | TDD | 624 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.471 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.494 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.603 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.603 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.329 | NREventA3 | measId:2;ServCellPCI:993;Se... |
| 2024-09-20 22:21:38.569 | NRHandoverAttempt | SourcePCI:993;SourceNR-ARFC... |
| 2024-09-20 22:21:38.607 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.622 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.766 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.766 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277571 | 1 | 8.9232 | 19.4671 | -117.7924 | 18.0171 | 152.1809 | 0.0028 | 0.0113 |
| 2024_09_20 22:00 | 3224505 | 2 | 17.6764 | 19.9859 | -116.8136 | 16.5266 | 87.0092 | 0.0067 | 0.0002 |
| 2024_09_20 22:00 | 3224971 | 3 | 18.7812 | 16.6168 | -117.6390 | 5.7788 | 168.6301 | 0.0052 | 0.1774 |
| 2024_09_20 22:00 | 3254612 | 4 | 5.0496 | 8.2283 | -114.3003 | 19.5157 | 175.5880 | 0.0016 | 0.0138 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414899_7A54D280 | 504990 | 588 | -85.8 | 504990 | 419 | -88.3 | 504990 | 624 | -88.0 | 504990 | 618 |
| MR_1774414899_7DACCADF | 504990 | 588 | -83.2 | 504990 | 419 | -90.4 | 504990 | 624 | -91.0 | 504990 | 618 |
| MR_1774414899_10489352 | 504990 | 588 | -86.7 | 504990 | 419 | -91.0 | 504990 | 624 | -89.5 | 504990 | 618 |
| MR_1774414899_E1B216BC | 504990 | 419 | -91.3 | 504990 | 588 | -83.9 | 504990 | 624 | -91.1 | 504990 | 618 |
| MR_1774414899_05BD3432 | 504990 | 419 | -90.6 | 504990 | 588 | -85.9 | 504990 | 624 | -88.5 | 504990 | 618 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1723: `d92b5f5d-6ee...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d92b5f5d-6ee4-4f68-955c-15e37cf55f11` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease A3 Offset threshold for 3240885_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1723] topology](images/train_1723.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3266786_3 by 50 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease A3 Offset threshold for 3266786_3
- `C4`: Add neighbor relationship between 3213230_2 and 3266786_3
- `C5`: Increase transmission power for 3266786_3
- `C6`: Lift the tilt angle  of 3266786_3 by 10 degrees
- `C7`: Decrease transmission power for 3266786_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266786_3
- `C9`: Add neighbor relationship between 3240885_4 and 3266786_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240885_4
- `C11`: Increase A3 Offset threshold for 3266786_3
- `C12`: Decrease transmission power for 3240885_4
- `C13`: Press down the tilt angle of 3240885_4 by 5 degrees
- `C14`: Lift the tilt angle of 3240885_4 by 5 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266786_3
- `C16`: Decrease A3 Offset threshold for 3240885_4 **← 정답**
- `C17`: Increase A3 Offset threshold for 3240885_4
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240885_4
- `C19`: Increase transmission power for 3240885_4
- `C20`: Adjust the azimuth of 3240885_4 by 50 degrees
- `C21`: Check test server and transmission issues
- `C22`: Press down the tilt angle  of 3266786_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.879 | MS1 | 121.4656700195 | 31.1446339218 | 719 | 504990 | -81.38 | 16.10 | 401.44 | 0.07 | 2.22 | 1588 |
| 2024-09-20 22:21:32.471 | MS1 | 121.4656582804 | 31.1446230753 | 719 | 504990 | -83.40 | 17.77 | 336.49 | 0.03 | 2.36 | 1563 |
| 2024-09-20 22:21:33.540 | MS1 | 121.4656719427 | 31.1446262783 | 719 | 504990 | -75.20 | 12.20 | 515.48 | 0.11 | 2.05 | 1589 |
| 2024-09-20 22:21:34.695 | MS1 | 121.4656641471 | 31.1446345462 | 719 | 504990 | -87.15 | -0.14 | 30.11 | 0.14 | 1.32 | 1593 |
| 2024-09-20 22:21:35.564 | MS1 | 121.4656742591 | 31.1446277623 | 719 | 504990 | -92.12 | -1.26 | 61.34 | 0.09 | 1.49 | 1590 |
| 2024-09-20 22:21:36.526 | MS1 | 121.4656635400 | 31.1446371183 | 719 | 504990 | -89.74 | -0.02 | 53.17 | 0.09 | 1.29 | 1564 |
| 2024-09-20 22:21:37.658 | MS1 | 121.4656728488 | 31.1446336397 | 719 | 504990 | -88.06 | -1.53 | 27.65 | 0.02 | 1.39 | 1564 |
| 2024-09-20 22:21:38.142 | MS1 | 121.4656694575 | 31.1446189957 | 719 | 504990 | -83.47 | -3.95 | 44.24 | 0.18 | 1.31 | 1594 |
| 2024-09-20 22:21:39.202 | MS1 | 121.4656691888 | 31.1446289334 | 174 | 504990 | -84.27 | 13.11 | 169.07 | 0.02 | 1.21 | 1573 |
| 2024-09-20 22:21:40.437 | MS1 | 121.4656616272 | 31.1446379179 | 174 | 504990 | -84.36 | 17.02 | 514.91 | 0.14 | 2.69 | 1593 |
| 2024-09-20 22:21:41.912 | MS1 | 121.4656649281 | 31.1446217427 | 174 | 504990 | -82.47 | 15.87 | 346.11 | 0.01 | 2.50 | 1596 |
| 2024-09-20 22:21:42.369 | MS1 | 121.4656583995 | 31.1446308592 | 174 | 504990 | -83.85 | 15.21 | 375.13 | 0.14 | 2.02 | 1586 |

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
| 3213230 | 2 | 121.4758544791 | 31.1492629679 | 284 | 8 | 6 | 25.6 | TDD | 45 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3240885 | 4 | 121.4673878767 | 31.1492959601 | 5 | 3 | 0 | 20.8 | TDD | 719 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3249117 | 1 | 121.4716870764 | 31.1481619972 | 89 | 12 | 6 | 29.8 | TDD | 130 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3266786 | 3 | 121.4716080802 | 31.1447024653 | 183 | 8 | 1 | 49.5 | TDD | 174 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.150 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.172 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.291 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.291 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.965 | NREventA3 | measId:2;ServCellPCI:79;Ser... |
| 2024-09-20 22:21:38.205 | NRHandoverAttempt | SourcePCI:79;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.240 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.254 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.365 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.365 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249117 | 1 | 14.6733 | 15.6033 | -114.1864 | 8.9616 | 127.4614 | 0.0094 | 0.0131 |
| 2024_09_20 22:00 | 3213230 | 2 | 17.7538 | 7.2076 | -117.7145 | 14.8560 | 144.1754 | 0.0088 | 0.0159 |
| 2024_09_20 22:00 | 3266786 | 3 | 18.4165 | 14.9292 | -114.8870 | 8.5682 | 124.4641 | 0.0048 | 0.0196 |
| 2024_09_20 22:00 | 3240885 | 4 | 18.1312 | 17.0047 | -114.5879 | 12.2236 | 169.3479 | 0.0027 | 0.1856 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417157_62D85585 | 504990 | 719 | -85.4 | 504990 | 174 | -83.1 | 504990 | 45 | -88.6 | 504990 | 130 |
| MR_1774417157_2D2F1423 | 504990 | 719 | -87.5 | 504990 | 174 | -83.2 | 504990 | 45 | -91.2 | 504990 | 130 |
| MR_1774417157_336F816E | 504990 | 174 | -79.8 | 504990 | 719 | -88.6 | 504990 | 45 | -90.0 | 504990 | 130 |
| MR_1774417157_C10DBE12 | 504990 | 719 | -87.4 | 504990 | 174 | -81.6 | 504990 | 45 | -88.5 | 504990 | 130 |
| MR_1774417157_F81078D1 | 504990 | 719 | -86.0 | 504990 | 174 | -79.8 | 504990 | 45 | -90.7 | 504990 | 130 |
| MR_1774417157_006FC698 | 504990 | 719 | -87.3 | 504990 | 174 | -82.5 | 504990 | 45 | -90.3 | 504990 | 130 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1724: `4d362eb6-837...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4d362eb6-837e-4dde-8c39-8414a21ef0a7` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Decrease A3 Offset threshold for 3240390_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1724] topology](images/train_1724.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3224368_2 by 27 degrees
- `C2`: Increase A3 Offset threshold for 3240390_1
- `C3`: Add neighbor relationship between 3240390_1 and 3224368_2
- `C4`: Decrease A3 Offset threshold for 3240390_1 **← 정답**
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240390_1
- `C6`: Add neighbor relationship between 3273611_4 and 3224368_2
- `C7`: Check test server and transmission issues
- `C8`: Increase transmission power for 3224368_2
- `C9`: Lift the tilt angle  of 3224368_2 by 10 degrees
- `C10`: Press down the tilt angle  of 3224368_2 by 10 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224368_2
- `C12`: Adjust the azimuth of 3240390_1 by 4 degrees
- `C13`: Increase A3 Offset threshold for 3224368_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240390_1
- `C15`: Press down the tilt angle of 3240390_1 by 10 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224368_2
- `C17`: Decrease A3 Offset threshold for 3224368_2
- `C18`: Decrease transmission power for 3224368_2
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase transmission power for 3240390_1
- `C21`: Decrease transmission power for 3240390_1
- `C22`: Lift the tilt angle of 3240390_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.623 | MS1 | 121.4656775959 | 31.1446290180 | 256 | 504990 | -81.30 | 15.51 | 472.33 | 0.15 | 2.73 | 1562 |
| 2024-09-20 22:21:32.708 | MS1 | 121.4656745986 | 31.1446376059 | 256 | 504990 | -78.58 | 14.99 | 414.78 | 0.05 | 2.29 | 1587 |
| 2024-09-20 22:21:33.475 | MS1 | 121.4656685473 | 31.1446180550 | 256 | 504990 | -81.10 | 14.16 | 453.40 | 0.13 | 2.80 | 1565 |
| 2024-09-20 22:21:34.212 | MS1 | 121.4656720996 | 31.1446346519 | 256 | 504990 | -85.20 | -1.54 | 57.13 | 0.02 | 1.15 | 1566 |
| 2024-09-20 22:21:35.786 | MS1 | 121.4656594661 | 31.1446327976 | 256 | 504990 | -86.34 | -3.21 | 58.16 | 0.16 | 1.27 | 1600 |
| 2024-09-20 22:21:36.945 | MS1 | 121.4656673200 | 31.1446281020 | 256 | 504990 | -83.28 | -3.57 | 65.68 | 0.20 | 1.07 | 1581 |
| 2024-09-20 22:21:37.237 | MS1 | 121.4656628531 | 31.1446369142 | 256 | 504990 | -86.19 | -0.39 | 71.62 | 0.11 | 1.15 | 1596 |
| 2024-09-20 22:21:38.116 | MS1 | 121.4656765661 | 31.1446369354 | 256 | 504990 | -91.58 | -1.53 | 68.64 | 0.16 | 1.12 | 1577 |
| 2024-09-20 22:21:39.341 | MS1 | 121.4656707412 | 31.1446246975 | 707 | 504990 | -83.65 | 16.61 | 284.69 | 0.15 | 1.01 | 1594 |
| 2024-09-20 22:21:40.589 | MS1 | 121.4656611802 | 31.1446334053 | 707 | 504990 | -84.94 | 13.95 | 556.40 | 0.05 | 2.63 | 1584 |
| 2024-09-20 22:21:41.492 | MS1 | 121.4656724701 | 31.1446202533 | 707 | 504990 | -75.50 | 14.73 | 531.29 | 0.06 | 2.08 | 1587 |
| 2024-09-20 22:21:42.705 | MS1 | 121.4656708586 | 31.1446318525 | 707 | 504990 | -84.12 | 14.27 | 462.00 | 0.15 | 2.02 | 1584 |

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
| 3219894 | 3 | 121.4681317227 | 31.1542691475 | 162 | 3 | 8 | 36.1 | TDD | 413 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3224368 | 2 | 121.4644667363 | 31.1444589267 | 107 | 15 | 3 | 40.1 | TDD | 707 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3240390 | 1 | 121.4718404528 | 31.1493334692 | 232 | 8 | 10 | 37.6 | TDD | 256 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3273611 | 4 | 121.4692954048 | 31.1508509050 | 347 | 10 | 8 | 27.1 | TDD | 243 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.152 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.173 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.288 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.288 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.984 | NREventA3 | measId:2;ServCellPCI:421;Se... |
| 2024-09-20 22:21:38.224 | NRHandoverAttempt | SourcePCI:421;SourceNR-ARFC... |
| 2024-09-20 22:21:38.261 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.276 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.413 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.413 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240390 | 1 | 17.3889 | 5.1123 | -117.6369 | 13.7031 | 120.8639 | 0.0119 | 0.1947 |
| 2024_09_20 22:00 | 3224368 | 2 | 8.5310 | 12.8173 | -116.7170 | 15.2280 | 98.0555 | 0.0109 | 0.0050 |
| 2024_09_20 22:00 | 3219894 | 3 | 7.3205 | 13.6939 | -114.3325 | 5.1287 | 93.5505 | 0.0038 | 0.0167 |
| 2024_09_20 22:00 | 3273611 | 4 | 5.5974 | 5.6317 | -114.6724 | 13.2726 | 86.5135 | 0.0017 | 0.0159 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416987_C0A78899 | 504990 | 256 | -84.4 | 504990 | 707 | -80.2 | 504990 | 243 | -80.7 | 504990 | 413 |
| MR_1774416987_C5E61DF7 | 504990 | 256 | -86.2 | 504990 | 707 | -77.2 | 504990 | 243 | -81.2 | 504990 | 413 |
| MR_1774416987_ADDD5D49 | 504990 | 256 | -85.0 | 504990 | 707 | -80.0 | 504990 | 243 | -80.4 | 504990 | 413 |
| MR_1774416987_68BE9DC3 | 504990 | 707 | -79.7 | 504990 | 256 | -84.6 | 504990 | 243 | -82.5 | 504990 | 413 |
| MR_1774416987_E0F8413F | 504990 | 256 | -85.7 | 504990 | 707 | -78.4 | 504990 | 243 | -81.2 | 504990 | 413 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1725: `236316c6-2c2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `236316c6-2c2b-470f-b33f-e7051ce022c0` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3250739_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1725] topology](images/train_1725.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3219736_4 and 3270365_2
- `C2`: Lift the tilt angle of 3250739_1 by 2 degrees
- `C3`: Increase A3 Offset threshold for 3250739_1
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease transmission power for 3250739_1
- `C6`: Press down the tilt angle  of 3270365_2 by 10 degrees
- `C7`: Decrease transmission power for 3270365_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270365_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270365_2
- `C10`: Decrease A3 Offset threshold for 3250739_1
- `C11`: Press down the tilt angle of 3250739_1 by 2 degrees
- `C12`: Check test server and transmission issues
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250739_1 **← 정답**
- `C14`: Add neighbor relationship between 3250739_1 and 3270365_2
- `C15`: Decrease A3 Offset threshold for 3270365_2
- `C16`: Increase A3 Offset threshold for 3270365_2
- `C17`: Lift the tilt angle  of 3270365_2 by 10 degrees
- `C18`: Increase transmission power for 3270365_2
- `C19`: Adjust the azimuth of 3270365_2 by 50 degrees
- `C20`: Adjust the azimuth of 3250739_1 by 17 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250739_1
- `C22`: Increase transmission power for 3250739_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.698 | MS1 | 121.4656755769 | 31.1446308824 | 153 | 504990 | -91.81 | 15.82 | 330.60 | 0.04 | 2.43 | 1571 |
| 2024-09-20 22:21:32.348 | MS1 | 121.4656715355 | 31.1446299262 | 153 | 504990 | -87.26 | 17.85 | 511.80 | 0.13 | 2.37 | 1594 |
| 2024-09-20 22:21:33.422 | MS1 | 121.4656736784 | 31.1446263726 | 153 | 504990 | -85.37 | 12.69 | 369.17 | 0.08 | 2.64 | 1581 |
| 2024-09-20 22:21:34.118 | MS1 | 121.4656637802 | 31.1446354679 | 153 | 504990 | -91.59 | 17.37 | 97.42 | 0.57 | 2.92 | 697 |
| 2024-09-20 22:21:35.515 | MS1 | 121.4656636920 | 31.1446301689 | 153 | 504990 | -89.35 | 13.96 | 100.87 | 0.55 | 2.56 | 539 |
| 2024-09-20 22:21:36.576 | MS1 | 121.4656666619 | 31.1446318743 | 153 | 504990 | -85.39 | 13.45 | 59.47 | 0.54 | 2.02 | 630 |
| 2024-09-20 22:21:37.270 | MS1 | 121.4656626826 | 31.1446234280 | 153 | 504990 | -92.89 | 10.55 | 54.46 | 0.68 | 2.09 | 650 |
| 2024-09-20 22:21:38.904 | MS1 | 121.4656650695 | 31.1446266561 | 153 | 504990 | -89.74 | 11.34 | 84.66 | 0.59 | 2.23 | 543 |
| 2024-09-20 22:21:39.134 | MS1 | 121.4656762961 | 31.1446351627 | 153 | 504990 | -93.39 | 10.81 | 76.00 | 0.52 | 2.60 | 681 |
| 2024-09-20 22:21:40.619 | MS1 | 121.4656645343 | 31.1446232699 | 153 | 504990 | -91.69 | 10.65 | 456.11 | 0.06 | 2.99 | 1595 |
| 2024-09-20 22:21:41.882 | MS1 | 121.4656603487 | 31.1446282290 | 153 | 504990 | -90.73 | 7.93 | 383.35 | 0.07 | 2.15 | 1597 |
| 2024-09-20 22:21:42.358 | MS1 | 121.4656734365 | 31.1446233951 | 153 | 504990 | -90.08 | 7.95 | 579.61 | 0.10 | 2.40 | 1595 |

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
| 3219736 | 4 | 121.4750016996 | 31.1444773748 | 192 | 4 | 2 | 33.4 | TDD | 722 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3250739 | 1 | 121.4683778885 | 31.1557792501 | 175 | 1 | 5 | 22.0 | TDD | 153 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3252505 | 3 | 121.4759552210 | 31.1470872816 | 183 | 4 | 6 | 20.0 | TDD | 460 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3270365 | 2 | 121.4745247507 | 31.1448358190 | 65 | 8 | 11 | 24.2 | TDD | 10 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.167 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.191 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.330 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.330 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.021 | NREventA3 | measId:2;ServCellPCI:461;Se... |
| 2024-09-20 22:21:38.261 | NRHandoverAttempt | SourcePCI:461;SourceNR-ARFC... |
| 2024-09-20 22:21:38.299 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.314 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.428 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.428 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250739 | 1 | 12.7971 | 8.3618 | -114.1383 | 7.3464 | 96.8875 | 0.0135 | 0.0187 |
| 2024_09_20 22:00 | 3270365 | 2 | 9.9997 | 5.6596 | -116.4545 | 11.3885 | 102.5465 | 0.0164 | 0.0041 |
| 2024_09_20 22:00 | 3252505 | 3 | 10.0051 | 6.9529 | -116.9908 | 18.8313 | 120.9848 | 0.0074 | 0.0043 |
| 2024_09_20 22:00 | 3219736 | 4 | 17.0924 | 5.9300 | -115.0450 | 11.3884 | 149.5131 | 0.0066 | 0.0054 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415698_3B458FA8 | 504990 | 153 | -90.5 | 504990 | 10 | -99.3 | 504990 | 722 | -102.3 | 504990 | 460 |
| MR_1774415698_A8B027E8 | 504990 | 153 | -91.7 | 504990 | 10 | -98.9 | 504990 | 722 | -99.5 | 504990 | 460 |
| MR_1774415698_3DCF8AFD | 504990 | 153 | -92.2 | 504990 | 10 | -97.8 | 504990 | 722 | -102.3 | 504990 | 460 |
| MR_1774415698_6E263371 | 504990 | 153 | -89.6 | 504990 | 10 | -97.8 | 504990 | 722 | -100.1 | 504990 | 460 |
| MR_1774415698_97B21569 | 504990 | 153 | -91.4 | 504990 | 10 | -96.7 | 504990 | 722 | -102.3 | 504990 | 460 |
| MR_1774415698_2CD52842 | 504990 | 153 | -92.3 | 504990 | 10 | -98.5 | 504990 | 722 | -100.1 | 504990 | 460 |
| MR_1774415698_BA531DDE | 504990 | 153 | -90.7 | 504990 | 10 | -98.1 | 504990 | 722 | -99.4 | 504990 | 460 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1726: `088415b4-ed2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `088415b4-ed21-4e4e-a249-35e90cfd9783` |
| Tag | **multiple-answer** |
| 정답 | **C1|C22** |
| C1 의미 | Increase transmission power for 3250275_1 |
| C22 의미 | Adjust the azimuth of 3250275_1 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1726] topology](images/train_1726.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3250275_1 **← 정답**
- `C2`: Lift the tilt angle  of 3264106_2 by 4 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250275_1
- `C4`: Add neighbor relationship between 3240989_4 and 3264106_2
- `C5`: Decrease transmission power for 3264106_2
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Press down the tilt angle of 3250275_1 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264106_2
- `C9`: Press down the tilt angle  of 3264106_2 by 4 degrees
- `C10`: Increase A3 Offset threshold for 3264106_2
- `C11`: Adjust the azimuth of 3264106_2 by 35 degrees
- `C12`: Decrease A3 Offset threshold for 3250275_1
- `C13`: Decrease A3 Offset threshold for 3264106_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264106_2
- `C15`: Add neighbor relationship between 3250275_1 and 3264106_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250275_1
- `C17`: Increase A3 Offset threshold for 3250275_1
- `C18`: Lift the tilt angle of 3250275_1 by 10 degrees
- `C19`: Increase transmission power for 3264106_2
- `C20`: Decrease transmission power for 3250275_1
- `C21`: Check test server and transmission issues
- `C22`: Adjust the azimuth of 3250275_1 by 50 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.322 | MS1 | 121.4656684766 | 31.1446369478 | 592 | 504990 | -87.81 | 16.00 | 374.01 | 0.16 | 2.20 | 1567 |
| 2024-09-20 22:21:32.390 | MS1 | 121.4656722141 | 31.1446275847 | 592 | 504990 | -87.90 | 13.44 | 528.37 | 0.11 | 2.19 | 1585 |
| 2024-09-20 22:21:33.501 | MS1 | 121.4656624304 | 31.1446238231 | 592 | 504990 | -90.29 | 17.22 | 553.38 | 0.20 | 2.67 | 1576 |
| 2024-09-20 22:21:34.415 | MS1 | 121.4656689564 | 31.1446357351 | 592 | 504990 | -109.95 | -0.52 | 60.07 | 0.09 | 1.39 | 1583 |
| 2024-09-20 22:21:35.747 | MS1 | 121.4656637740 | 31.1446374464 | 592 | 504990 | -100.09 | -0.01 | 70.27 | 0.12 | 1.00 | 1567 |
| 2024-09-20 22:21:36.987 | MS1 | 121.4656763924 | 31.1446219374 | 592 | 504990 | -105.95 | 1.60 | 27.52 | 0.05 | 1.31 | 1597 |
| 2024-09-20 22:21:37.555 | MS1 | 121.4656651669 | 31.1446190994 | 592 | 504990 | -107.92 | -0.33 | 76.33 | 0.19 | 1.38 | 1595 |
| 2024-09-20 22:21:38.674 | MS1 | 121.4656757298 | 31.1446324765 | 592 | 504990 | -106.22 | -1.79 | 34.99 | 0.05 | 1.43 | 1573 |
| 2024-09-20 22:21:39.605 | MS1 | 121.4656586556 | 31.1446262988 | 592 | 504990 | -107.30 | 0.83 | 24.81 | 0.18 | 1.27 | 1572 |
| 2024-09-20 22:21:40.413 | MS1 | 121.4656623465 | 31.1446225233 | 592 | 504990 | -91.01 | 15.12 | 453.65 | 0.15 | 2.89 | 1579 |
| 2024-09-20 22:21:41.149 | MS1 | 121.4656676878 | 31.1446230818 | 592 | 504990 | -88.52 | 12.18 | 468.14 | 0.09 | 2.17 | 1590 |
| 2024-09-20 22:21:42.358 | MS1 | 121.4656606183 | 31.1446308969 | 592 | 504990 | -90.36 | 15.51 | 451.80 | 0.09 | 2.90 | 1563 |

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
| 3232326 | 3 | 121.4673891211 | 31.1491019014 | 159 | 4 | 12 | 26.3 | TDD | 422 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3240989 | 4 | 121.4669688291 | 31.1462192029 | 135 | 3 | 0 | 27.3 | TDD | 711 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3250275 | 1 | 121.4645584547 | 31.1459661839 | 73 | 9 | 2 | 33.5 | TDD | 592 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3264106 | 2 | 121.4708585774 | 31.1462496517 | 215 | 1 | 12 | 30.7 | TDD | 842 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.746 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.766 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.885 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.885 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.120 | NREventA2 | measId:1;ServCellPCI:208;Se... |
| 2024-09-20 22:21:34.254 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250275 | 1 | 13.1919 | 12.3011 | -115.3459 | 7.7237 | 98.8268 | 0.1849 | 0.0193 |
| 2024_09_20 22:00 | 3264106 | 2 | 6.4080 | 10.4211 | -115.5706 | 10.6555 | 161.3251 | 0.0189 | 0.0148 |
| 2024_09_20 22:00 | 3232326 | 3 | 6.2345 | 9.2550 | -115.8513 | 11.9808 | 128.1792 | 0.0055 | 0.0169 |
| 2024_09_20 22:00 | 3240989 | 4 | 10.5049 | 18.9605 | -116.7931 | 15.1728 | 167.0749 | 0.0052 | 0.0142 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412576_779F614A | 504990 | 592 | -108.2 | 504990 | 842 | -113.9 | 504990 | 711 | -116.1 | 504990 | 422 |
| MR_1774412576_0B76982F | 504990 | 592 | -109.9 | 504990 | 842 | -113.3 | 504990 | 711 | -115.9 | 504990 | 422 |
| MR_1774412576_B3DD81C4 | 504990 | 592 | -108.4 | 504990 | 842 | -114.7 | 504990 | 711 | -119.0 | 504990 | 422 |
| MR_1774412576_317BD221 | 504990 | 592 | -110.5 | 504990 | 842 | -111.3 | 504990 | 711 | -116.0 | 504990 | 422 |
| MR_1774412576_DA989E49 | 504990 | 592 | -110.6 | 504990 | 842 | -112.2 | 504990 | 711 | -117.4 | 504990 | 422 |
| MR_1774412576_D108A972 | 504990 | 592 | -111.0 | 504990 | 842 | -114.3 | 504990 | 711 | -116.4 | 504990 | 422 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1727: `99dabe7c-f6d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `99dabe7c-f6d3-44f3-a9e9-874033a6512f` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3215157_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1727] topology](images/train_1727.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3259344_4 by 10 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215157_1
- `C3`: Decrease A3 Offset threshold for 3215157_1
- `C4`: Lift the tilt angle of 3215157_1 by 5 degrees
- `C5`: Adjust the azimuth of 3259344_4 by 50 degrees
- `C6`: Increase transmission power for 3215157_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215157_1 **← 정답**
- `C8`: Press down the tilt angle of 3215157_1 by 5 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Press down the tilt angle  of 3259344_4 by 10 degrees
- `C11`: Decrease transmission power for 3215157_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259344_4
- `C13`: Check test server and transmission issues
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259344_4
- `C15`: Increase A3 Offset threshold for 3215157_1
- `C16`: Add neighbor relationship between 3231854_3 and 3259344_4
- `C17`: Add neighbor relationship between 3215157_1 and 3259344_4
- `C18`: Decrease transmission power for 3259344_4
- `C19`: Adjust the azimuth of 3215157_1 by 20 degrees
- `C20`: Increase A3 Offset threshold for 3259344_4
- `C21`: Increase transmission power for 3259344_4
- `C22`: Decrease A3 Offset threshold for 3259344_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.699 | MS1 | 121.4656590573 | 31.1446199957 | 336 | 504990 | -89.05 | 13.48 | 528.42 | 0.03 | 2.55 | 1562 |
| 2024-09-20 22:21:32.402 | MS1 | 121.4656738555 | 31.1446187640 | 336 | 504990 | -91.38 | 14.15 | 375.15 | 0.18 | 2.07 | 1587 |
| 2024-09-20 22:21:33.766 | MS1 | 121.4656647040 | 31.1446195426 | 336 | 504990 | -86.47 | 14.45 | 519.96 | 0.09 | 2.48 | 1571 |
| 2024-09-20 22:21:34.620 | MS1 | 121.4656672406 | 31.1446371630 | 336 | 504990 | -89.66 | 16.83 | 94.84 | 0.67 | 2.12 | 617 |
| 2024-09-20 22:21:35.842 | MS1 | 121.4656643828 | 31.1446287191 | 336 | 504990 | -88.60 | 12.17 | 69.33 | 0.58 | 2.89 | 559 |
| 2024-09-20 22:21:36.604 | MS1 | 121.4656728350 | 31.1446357866 | 336 | 504990 | -87.88 | 14.08 | 73.40 | 0.54 | 2.59 | 600 |
| 2024-09-20 22:21:37.722 | MS1 | 121.4656593247 | 31.1446209165 | 336 | 504990 | -91.62 | 10.70 | 91.89 | 0.53 | 2.06 | 699 |
| 2024-09-20 22:21:38.934 | MS1 | 121.4656642054 | 31.1446263598 | 336 | 504990 | -91.07 | 8.18 | 74.46 | 0.55 | 2.05 | 525 |
| 2024-09-20 22:21:39.907 | MS1 | 121.4656644875 | 31.1446228029 | 336 | 504990 | -92.52 | 12.74 | 58.83 | 0.59 | 2.38 | 695 |
| 2024-09-20 22:21:40.885 | MS1 | 121.4656753954 | 31.1446292414 | 336 | 504990 | -92.92 | 12.49 | 445.55 | 0.13 | 2.70 | 1577 |
| 2024-09-20 22:21:41.743 | MS1 | 121.4656742645 | 31.1446353373 | 336 | 504990 | -89.72 | 10.47 | 335.23 | 0.08 | 2.23 | 1586 |
| 2024-09-20 22:21:42.690 | MS1 | 121.4656775667 | 31.1446253122 | 336 | 504990 | -89.49 | 10.54 | 503.54 | 0.13 | 2.16 | 1563 |

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
| 3211740 | 2 | 121.4678753861 | 31.1447849470 | 292 | 4 | 7 | 15.5 | TDD | 993 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3215157 | 1 | 121.4736656300 | 31.1534225674 | 238 | 4 | 1 | 32.1 | TDD | 336 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3231854 | 3 | 121.4737238500 | 31.1491546861 | 93 | 10 | 2 | 17.9 | TDD | 907 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3259344 | 4 | 121.4684622326 | 31.1512087986 | 11 | 14 | 11 | 17.5 | TDD | 864 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.158 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.308 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.308 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.989 | NREventA3 | measId:2;ServCellPCI:319;Se... |
| 2024-09-20 22:21:38.229 | NRHandoverAttempt | SourcePCI:319;SourceNR-ARFC... |
| 2024-09-20 22:21:38.275 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.286 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.401 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.401 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215157 | 1 | 10.9538 | 8.9943 | -115.2362 | 9.3512 | 146.3769 | 0.0084 | 0.0055 |
| 2024_09_20 22:00 | 3211740 | 2 | 11.1044 | 10.3943 | -117.8307 | 14.8435 | 181.4878 | 0.0073 | 0.0096 |
| 2024_09_20 22:00 | 3231854 | 3 | 19.5052 | 10.8792 | -114.2792 | 9.0289 | 163.3322 | 0.0006 | 0.0115 |
| 2024_09_20 22:00 | 3259344 | 4 | 17.7225 | 5.3736 | -117.0379 | 19.3184 | 171.7356 | 0.0007 | 0.0115 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414710_D79F0506 | 504990 | 336 | -89.8 | 504990 | 864 | -93.2 | 504990 | 907 | -104.2 | 504990 | 993 |
| MR_1774414710_0E3542C6 | 504990 | 336 | -87.8 | 504990 | 864 | -94.3 | 504990 | 907 | -101.8 | 504990 | 993 |
| MR_1774414710_37F4167D | 504990 | 336 | -88.0 | 504990 | 864 | -93.2 | 504990 | 907 | -104.0 | 504990 | 993 |
| MR_1774414710_4CE88ABF | 504990 | 336 | -89.6 | 504990 | 864 | -92.4 | 504990 | 907 | -100.3 | 504990 | 993 |
| MR_1774414710_D93A8758 | 504990 | 336 | -88.1 | 504990 | 864 | -93.4 | 504990 | 907 | -101.8 | 504990 | 993 |
| MR_1774414710_C27AB1DF | 504990 | 336 | -91.1 | 504990 | 864 | -95.3 | 504990 | 907 | -103.7 | 504990 | 993 |
| MR_1774414710_63EEE8F0 | 504990 | 336 | -91.2 | 504990 | 864 | -94.7 | 504990 | 907 | -104.3 | 504990 | 993 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1728: `d6e59c80-fc3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d6e59c80-fc32-4b33-a37c-4fafadb0c66e` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1728] topology](images/train_1728.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3231630_4 by 5 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237600_2
- `C3`: Increase transmission power for 3237600_2
- `C4`: Press down the tilt angle of 3237600_2 by 10 degrees
- `C5`: Insufficient data; more data is needed for judgment. **← 정답**
- `C6`: Lift the tilt angle of 3237600_2 by 10 degrees
- `C7`: Decrease A3 Offset threshold for 3231630_4
- `C8`: Decrease A3 Offset threshold for 3237600_2
- `C9`: Decrease transmission power for 3231630_4
- `C10`: Add neighbor relationship between 3257037_3 and 3231630_4
- `C11`: Increase A3 Offset threshold for 3237600_2
- `C12`: Lift the tilt angle  of 3231630_4 by 5 degrees
- `C13`: Decrease transmission power for 3237600_2
- `C14`: Adjust the azimuth of 3237600_2 by 19 degrees
- `C15`: Increase transmission power for 3231630_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237600_2
- `C17`: Check test server and transmission issues
- `C18`: Increase A3 Offset threshold for 3231630_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231630_4
- `C20`: Add neighbor relationship between 3237600_2 and 3231630_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231630_4
- `C22`: Adjust the azimuth of 3231630_4 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.940 | MS1 | 121.4656723680 | 31.1446294153 | 34 | 504990 | -85.50 | 14.62 | 597.96 | 0.17 | 2.10 | 1580 |
| 2024-09-20 22:21:32.178 | MS1 | 121.4656690404 | 31.1446296463 | 34 | 504990 | -89.11 | 17.48 | 402.10 | 0.09 | 2.95 | 1566 |
| 2024-09-20 22:21:33.534 | MS1 | 121.4656753555 | 31.1446228912 | 34 | 504990 | -85.25 | 16.89 | 448.23 | 0.11 | 2.57 | 1591 |
| 2024-09-20 22:21:34.747 | MS1 | 121.4656713690 | 31.1446341033 | 34 | 504990 | -91.97 | 14.35 | 86.91 | 0.12 | 2.93 | 1571 |
| 2024-09-20 22:21:35.156 | MS1 | 121.4656698931 | 31.1446313751 | 34 | 504990 | -89.14 | 15.82 | 64.71 | 0.20 | 2.99 | 1581 |
| 2024-09-20 22:21:36.291 | MS1 | 121.4656671090 | 31.1446268944 | 34 | 504990 | -90.89 | 13.24 | 48.43 | 0.14 | 2.18 | 1579 |
| 2024-09-20 22:21:37.765 | MS1 | 121.4656699362 | 31.1446349171 | 34 | 504990 | -89.94 | 8.64 | 80.77 | 0.12 | 2.33 | 1577 |
| 2024-09-20 22:21:38.455 | MS1 | 121.4656718577 | 31.1446183307 | 34 | 504990 | -90.17 | 9.59 | 62.59 | 0.07 | 2.56 | 1596 |
| 2024-09-20 22:21:39.935 | MS1 | 121.4656636869 | 31.1446212885 | 34 | 504990 | -90.52 | 8.84 | 97.12 | 0.10 | 2.21 | 1578 |
| 2024-09-20 22:21:40.372 | MS1 | 121.4656772585 | 31.1446192528 | 34 | 504990 | -90.52 | 12.83 | 565.90 | 0.05 | 2.59 | 1595 |
| 2024-09-20 22:21:41.324 | MS1 | 121.4656697978 | 31.1446350905 | 34 | 504990 | -92.45 | 8.62 | 572.90 | 0.16 | 2.53 | 1570 |
| 2024-09-20 22:21:42.926 | MS1 | 121.4656767659 | 31.1446356684 | 34 | 504990 | -89.17 | 11.95 | 517.40 | 0.12 | 2.23 | 1593 |

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
| 3231630 | 4 | 121.4714724614 | 31.1458987442 | 151 | 3 | 12 | 19.5 | TDD | 658 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3237600 | 2 | 121.4660216062 | 31.1443414291 | 332 | 3 | 12 | 49.2 | TDD | 34 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3257037 | 3 | 121.4705590786 | 31.1553712792 | 302 | 1 | 8 | 38.6 | TDD | 812 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3266792 | 1 | 121.4659681877 | 31.1514558529 | 261 | 7 | 4 | 33.5 | TDD | 401 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.626 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.644 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.759 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.759 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.452 | NREventA3 | measId:2;ServCellPCI:972;Se... |
| 2024-09-20 22:21:38.692 | NRHandoverAttempt | SourcePCI:972;SourceNR-ARFC... |
| 2024-09-20 22:21:38.727 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.737 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.841 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.841 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3266792 | 1 | 93.2097 | 91.6504 | -115.1502 | 9.0790 | 196.4354 | 0.0082 | 0.0172 |
| 2024_09_19 22:00 | 3237600 | 2 | 79.0810 | 83.1138 | -116.8214 | 12.5785 | 183.8041 | 0.0072 | 0.0183 |
| 2024_09_19 22:00 | 3257037 | 3 | 76.7134 | 81.6455 | -115.1895 | 19.6153 | 140.8147 | 0.0181 | 0.0038 |
| 2024_09_19 22:00 | 3231630 | 4 | 78.5407 | 81.1020 | -116.2126 | 17.6365 | 174.9743 | 0.0129 | 0.0144 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414313_6057A976 | 504990 | 34 | -93.5 | 504990 | 658 | -101.4 | 504990 | 812 | -101.4 | 504990 | 401 |
| MR_1774414313_8E8BD6D5 | 504990 | 34 | -91.7 | 504990 | 658 | -100.0 | 504990 | 812 | -99.3 | 504990 | 401 |
| MR_1774414313_AB0EFA58 | 504990 | 34 | -90.6 | 504990 | 658 | -101.4 | 504990 | 812 | -102.8 | 504990 | 401 |
| MR_1774414313_CA6C8CCF | 504990 | 34 | -90.7 | 504990 | 658 | -98.6 | 504990 | 812 | -101.8 | 504990 | 401 |
| MR_1774414313_C5589539 | 504990 | 34 | -93.1 | 504990 | 658 | -98.5 | 504990 | 812 | -99.2 | 504990 | 401 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1729: `6b82f286-e6f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6b82f286-e6f0-4681-8857-b0f616b8172c` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1729] topology](images/train_1729.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3264852_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264852_2
- `C3`: Decrease transmission power for 3217512_1
- `C4`: Adjust the azimuth of 3264852_2 by 50 degrees
- `C5`: Increase A3 Offset threshold for 3217512_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217512_1
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217512_1
- `C9`: Check test server and transmission issues **← 정답**
- `C10`: Add neighbor relationship between 3217512_1 and 3264852_2
- `C11`: Decrease A3 Offset threshold for 3217512_1
- `C12`: Increase A3 Offset threshold for 3264852_2
- `C13`: Press down the tilt angle of 3217512_1 by 10 degrees
- `C14`: Adjust the azimuth of 3217512_1 by 50 degrees
- `C15`: Lift the tilt angle of 3217512_1 by 10 degrees
- `C16`: Lift the tilt angle  of 3264852_2 by 6 degrees
- `C17`: Decrease A3 Offset threshold for 3264852_2
- `C18`: Press down the tilt angle  of 3264852_2 by 6 degrees
- `C19`: Add neighbor relationship between 3210729_4 and 3264852_2
- `C20`: Increase transmission power for 3217512_1
- `C21`: Decrease transmission power for 3264852_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264852_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.464 | MS1 | 121.4656739189 | 31.1446311124 | 248 | 504990 | -87.40 | 17.68 | 405.57 | 0.18 | 2.82 | 1567 |
| 2024-09-20 22:21:32.189 | MS1 | 121.4656604258 | 31.1446369414 | 248 | 504990 | -91.96 | 16.60 | 317.94 | 0.16 | 2.45 | 1590 |
| 2024-09-20 22:21:33.835 | MS1 | 121.4656641081 | 31.1446346069 | 248 | 504990 | -90.98 | 15.67 | 538.30 | 0.06 | 2.63 | 1599 |
| 2024-09-20 22:21:34.169 | MS1 | 121.4656655655 | 31.1446188773 | 248 | 504990 | -85.28 | 13.14 | 99.31 | 0.09 | 2.65 | 471 |
| 2024-09-20 22:21:35.125 | MS1 | 121.4656665712 | 31.1446325144 | 248 | 504990 | -89.33 | 15.16 | 72.48 | 0.02 | 2.19 | 377 |
| 2024-09-20 22:21:36.875 | MS1 | 121.4656694930 | 31.1446227111 | 248 | 504990 | -90.22 | 17.34 | 65.18 | 0.05 | 2.45 | 312 |
| 2024-09-20 22:21:37.271 | MS1 | 121.4656679711 | 31.1446308774 | 248 | 504990 | -90.33 | 11.77 | 66.92 | 0.03 | 2.79 | 410 |
| 2024-09-20 22:21:38.783 | MS1 | 121.4656648586 | 31.1446191071 | 248 | 504990 | -92.76 | 9.23 | 77.49 | 0.19 | 2.48 | 498 |
| 2024-09-20 22:21:39.757 | MS1 | 121.4656756423 | 31.1446341751 | 248 | 504990 | -89.27 | 11.96 | 95.59 | 0.20 | 2.69 | 481 |
| 2024-09-20 22:21:40.482 | MS1 | 121.4656697973 | 31.1446271826 | 248 | 504990 | -91.57 | 10.88 | 341.45 | 0.16 | 2.88 | 1585 |
| 2024-09-20 22:21:41.877 | MS1 | 121.4656693693 | 31.1446289708 | 248 | 504990 | -93.24 | 12.39 | 372.90 | 0.17 | 2.75 | 1591 |
| 2024-09-20 22:21:42.602 | MS1 | 121.4656733940 | 31.1446196654 | 248 | 504990 | -90.29 | 12.96 | 530.82 | 0.15 | 2.97 | 1575 |

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
| 3210729 | 4 | 121.4676378941 | 31.1545336710 | 106 | 6 | 12 | 41.2 | TDD | 360 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3217512 | 1 | 121.4674172802 | 31.1467160072 | 293 | 15 | 11 | 19.6 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3240156 | 3 | 121.4718245250 | 31.1482319545 | 135 | 9 | 8 | 43.4 | TDD | 99 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3264852 | 2 | 121.4676903043 | 31.1482156667 | 119 | 3 | 3 | 26.5 | TDD | 457 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.565 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.697 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.697 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.438 | NREventA3 | measId:2;ServCellPCI:246;Se... |
| 2024-09-20 22:21:38.678 | NRHandoverAttempt | SourcePCI:246;SourceNR-ARFC... |
| 2024-09-20 22:21:38.726 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.740 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.864 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.864 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217512 | 1 | 7.1513 | 17.9828 | -114.4605 | 14.7102 | 139.6207 | 0.0160 | 0.0123 |
| 2024_09_20 22:00 | 3264852 | 2 | 10.4520 | 15.4869 | -116.9814 | 16.0101 | 162.5335 | 0.0089 | 0.0008 |
| 2024_09_20 22:00 | 3240156 | 3 | 13.2721 | 17.3952 | -117.4685 | 10.0877 | 81.3403 | 0.0145 | 0.0037 |
| 2024_09_20 22:00 | 3210729 | 4 | 16.4499 | 9.9132 | -115.5263 | 7.9294 | 88.0405 | 0.0097 | 0.0028 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414659_AA1F3A78 | 504990 | 248 | -84.2 | 504990 | 457 | -86.3 | 504990 | 360 | -95.1 | 504990 | 99 |
| MR_1774414659_B1007753 | 504990 | 248 | -84.9 | 504990 | 457 | -84.6 | 504990 | 360 | -95.3 | 504990 | 99 |
| MR_1774414659_C986638F | 504990 | 248 | -84.8 | 504990 | 457 | -85.0 | 504990 | 360 | -94.8 | 504990 | 99 |
| MR_1774414659_9EC87DCF | 504990 | 248 | -84.6 | 504990 | 457 | -84.5 | 504990 | 360 | -95.7 | 504990 | 99 |
| MR_1774414659_2396F9E1 | 504990 | 248 | -85.4 | 504990 | 457 | -86.8 | 504990 | 360 | -97.5 | 504990 | 99 |

> *... 2개 열 생략 (전체 14열)*

---
