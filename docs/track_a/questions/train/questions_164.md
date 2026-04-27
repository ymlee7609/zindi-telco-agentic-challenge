# Track A 문제 분석 — train[1630]~train[1639]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1630] ~ train[1639] (10개)

## 목차

1. [문제 1630: `7fdca64d-0c9...`](#1630) — single-answer, 정답: C17
2. [문제 1631: `f6da5f9f-87f...`](#1631) — single-answer, 정답: C19
3. [문제 1632: `671229e9-de8...`](#1632) — single-answer, 정답: C18
4. [문제 1633: `6e9508b9-4d9...`](#1633) — multiple-answer, 정답: C4|C6
5. [문제 1634: `adbb0d5b-18a...`](#1634) — single-answer, 정답: C14
6. [문제 1635: `0df47f28-481...`](#1635) — single-answer, 정답: C12
7. [문제 1636: `b65d9400-cd4...`](#1636) — single-answer, 정답: C20
8. [문제 1637: `e0bc9573-b99...`](#1637) — single-answer, 정답: C14
9. [문제 1638: `65477131-2be...`](#1638) — single-answer, 정답: C6
10. [문제 1639: `2ea33a0a-3aa...`](#1639) — single-answer, 정답: C18

---

### 문제 1630: `7fdca64d-0c9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7fdca64d-0c97-49d7-9041-e0aeb22a7b38` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Add neighbor relationship between 3239444_2 and 3241418_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1630] topology](images/train_1630.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3239444_2 by 50 degrees
- `C2`: Decrease transmission power for 3241418_3
- `C3`: Increase transmission power for 3239444_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Increase A3 Offset threshold for 3241418_3
- `C6`: Lift the tilt angle  of 3241418_3 by 3 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239444_2
- `C8`: Decrease A3 Offset threshold for 3239444_2
- `C9`: Press down the tilt angle  of 3241418_3 by 3 degrees
- `C10`: Press down the tilt angle of 3239444_2 by 10 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241418_3
- `C12`: Adjust the azimuth of 3241418_3 by 3 degrees
- `C13`: Check test server and transmission issues
- `C14`: Increase A3 Offset threshold for 3239444_2
- `C15`: Decrease A3 Offset threshold for 3241418_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239444_2
- `C17`: Add neighbor relationship between 3239444_2 and 3241418_3 **← 정답**
- `C18`: Increase transmission power for 3241418_3
- `C19`: Decrease transmission power for 3239444_2
- `C20`: Add neighbor relationship between 3241175_1 and 3241418_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241418_3
- `C22`: Lift the tilt angle of 3239444_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.842 | MS1 | 121.4656658468 | 31.1446273872 | 98 | 504990 | -77.10 | 12.73 | 403.04 | 0.12 | 2.13 | 1571 |
| 2024-09-20 22:21:32.460 | MS1 | 121.4656580967 | 31.1446264906 | 98 | 504990 | -77.58 | 14.95 | 542.04 | 0.19 | 2.05 | 1593 |
| 2024-09-20 22:21:33.545 | MS1 | 121.4656747057 | 31.1446207815 | 98 | 504990 | -82.18 | 16.38 | 323.45 | 0.10 | 2.64 | 1566 |
| 2024-09-20 22:21:34.682 | MS1 | 121.4656769044 | 31.1446210545 | 98 | 504990 | -90.14 | -2.56 | 71.91 | 0.07 | 1.26 | 1590 |
| 2024-09-20 22:21:35.535 | MS1 | 121.4656598404 | 31.1446320475 | 98 | 504990 | -86.39 | -2.63 | 72.37 | 0.15 | 1.27 | 1589 |
| 2024-09-20 22:21:36.238 | MS1 | 121.4656686377 | 31.1446216615 | 98 | 504990 | -87.95 | -0.76 | 43.48 | 0.10 | 1.46 | 1583 |
| 2024-09-20 22:21:37.832 | MS1 | 121.4656629843 | 31.1446213001 | 98 | 504990 | -86.84 | -0.13 | 46.22 | 0.20 | 1.16 | 1599 |
| 2024-09-20 22:21:38.825 | MS1 | 121.4656607739 | 31.1446228543 | 98 | 504990 | -78.45 | 14.99 | 573.19 | 0.15 | 1.27 | 1581 |
| 2024-09-20 22:21:39.603 | MS1 | 121.4656694860 | 31.1446318431 | 98 | 504990 | -81.03 | 16.40 | 413.00 | 0.06 | 1.09 | 1594 |
| 2024-09-20 22:21:40.948 | MS1 | 121.4656627358 | 31.1446270776 | 98 | 504990 | -76.82 | 13.39 | 589.65 | 0.18 | 2.49 | 1560 |
| 2024-09-20 22:21:41.915 | MS1 | 121.4656618066 | 31.1446298052 | 98 | 504990 | -81.90 | 14.32 | 344.00 | 0.10 | 2.88 | 1560 |
| 2024-09-20 22:21:42.928 | MS1 | 121.4656773622 | 31.1446314482 | 98 | 504990 | -75.75 | 15.54 | 349.35 | 0.15 | 2.29 | 1593 |

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
| 3210843 | 4 | 121.4644542830 | 31.1493452009 | 256 | 3 | 1 | 19.8 | TDD | 407 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3239444 | 2 | 121.4711024671 | 31.1496954656 | 7 | 8 | 2 | 46.4 | TDD | 98 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3241175 | 1 | 121.4657788833 | 31.1559889482 | 28 | 0 | 3 | 15.4 | TDD | 913 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3241418 | 3 | 121.4726716234 | 31.1457839395 | 256 | 0 | 0 | 38.0 | TDD | 243 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.586 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.606 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.754 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.754 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.431 | NREventA3 | measId:2;ServCellPCI:917;Se... |
| 2024-09-20 22:21:36.431 | NREventA3 | measId:2;ServCellPCI:917;Se... |
| 2024-09-20 22:21:37.431 | NREventA3 | measId:2;ServCellPCI:917;Se... |
| 2024-09-20 22:21:39.931 | NRRRCReestablishAttempt | PCI:917 |
| 2024-09-20 22:21:39.948 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.959 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:40.099 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.099 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241175 | 1 | 11.7752 | 10.7063 | -115.2472 | 7.6707 | 133.0462 | 0.0005 | 0.0168 |
| 2024_09_20 22:00 | 3239444 | 2 | 5.0526 | 5.6827 | -115.6209 | 5.0378 | 181.7465 | 0.0187 | 0.1581 |
| 2024_09_20 22:00 | 3241418 | 3 | 19.5530 | 11.4091 | -114.3197 | 18.4057 | 141.6295 | 0.0055 | 0.0097 |
| 2024_09_20 22:00 | 3210843 | 4 | 14.1235 | 19.7984 | -115.5582 | 6.6249 | 162.0343 | 0.0168 | 0.0195 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416907_4254C6C9 | 504990 | 98 | -91.0 | 504990 | 243 | -87.1 | 504990 | 913 | -88.8 | 504990 | 407 |
| MR_1774416907_8F4F983D | 504990 | 243 | -86.5 | 504990 | 98 | -89.4 | 504990 | 913 | -88.3 | 504990 | 407 |
| MR_1774416907_EAB85314 | 504990 | 98 | -91.3 | 504990 | 243 | -86.5 | 504990 | 913 | -87.8 | 504990 | 407 |
| MR_1774416907_5FE27DB2 | 504990 | 243 | -84.3 | 504990 | 98 | -89.8 | 504990 | 913 | -89.2 | 504990 | 407 |
| MR_1774416907_84F2B23F | 504990 | 98 | -88.3 | 504990 | 243 | -86.1 | 504990 | 913 | -90.8 | 504990 | 407 |
| MR_1774416907_0868E202 | 504990 | 98 | -91.5 | 504990 | 243 | -83.8 | 504990 | 913 | -91.1 | 504990 | 407 |
| MR_1774416907_92059DFC | 504990 | 98 | -88.9 | 504990 | 243 | -87.0 | 504990 | 913 | -91.4 | 504990 | 407 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1631: `f6da5f9f-87f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f6da5f9f-87f9-45d6-b29f-01edfe172493` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260491_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1631] topology](images/train_1631.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3219455_2
- `C2`: Increase A3 Offset threshold for 3260491_6
- `C3`: Decrease A3 Offset threshold for 3219455_2
- `C4`: Adjust the azimuth of 3219455_2 by 7 degrees
- `C5`: Lift the tilt angle of 3260491_6 by 1 degrees
- `C6`: Adjust the azimuth of 3260491_6 by 46 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219455_2
- `C8`: Decrease transmission power for 3219455_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219455_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Lift the tilt angle  of 3219455_2 by 5 degrees
- `C12`: Increase transmission power for 3219455_2
- `C13`: Decrease A3 Offset threshold for 3260491_6
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260491_6
- `C15`: Press down the tilt angle of 3260491_6 by 1 degrees
- `C16`: Add neighbor relationship between 3260491_6 and 3219455_2
- `C17`: Add neighbor relationship between 3229216_8 and 3219455_2
- `C18`: Check test server and transmission issues
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260491_6 **← 정답**
- `C20`: Press down the tilt angle  of 3219455_2 by 5 degrees
- `C21`: Increase transmission power for 3260491_6
- `C22`: Decrease transmission power for 3260491_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.649 | MS1 | 121.4656679091 | 31.1446376261 | 287 | 504990 | -93.36 | 14.81 | 360.02 | 0.05 | 2.99 | 1563 |
| 2024-09-20 22:21:32.673 | MS1 | 121.4656672161 | 31.1446332206 | 210 | 504990 | -95.07 | 11.79 | 453.76 | 0.01 | 2.87 | 1572 |
| 2024-09-20 22:21:33.198 | MS1 | 121.4656598021 | 31.1446286356 | 468 | 504990 | -93.98 | 12.52 | 528.63 | 0.01 | 2.15 | 1578 |
| 2024-09-20 22:21:34.803 | MS1 | 121.4656662412 | 31.1446204008 | 216 | 152650 | -90.35 | 4.60 | 93.57 | 0.13 | 1.51 | 931 |
| 2024-09-20 22:21:35.998 | MS1 | 121.4656768756 | 31.1446352718 | 242 | 152650 | -95.98 | 7.00 | 59.94 | 0.07 | 1.57 | 987 |
| 2024-09-20 22:21:36.715 | MS1 | 121.4656584368 | 31.1446253171 | 526 | 152650 | -87.84 | 5.34 | 68.25 | 0.04 | 1.81 | 999 |
| 2024-09-20 22:21:37.870 | MS1 | 121.4656625806 | 31.1446198246 | 269 | 152650 | -90.20 | 7.82 | 76.85 | 0.15 | 1.64 | 938 |
| 2024-09-20 22:21:38.653 | MS1 | 121.4656690825 | 31.1446354728 | 216 | 152650 | -91.24 | 3.64 | 61.73 | 0.14 | 1.76 | 968 |
| 2024-09-20 22:21:39.376 | MS1 | 121.4656649645 | 31.1446291050 | 242 | 152650 | -93.76 | 3.76 | 80.12 | 0.15 | 1.89 | 962 |
| 2024-09-20 22:21:40.533 | MS1 | 121.4656609004 | 31.1446234419 | 526 | 152650 | -89.68 | 7.23 | 76.99 | 0.07 | 2.93 | 1586 |
| 2024-09-20 22:21:41.812 | MS1 | 121.4656654060 | 31.1446303444 | 269 | 152650 | -95.16 | 5.10 | 54.13 | 0.10 | 3.00 | 1595 |
| 2024-09-20 22:21:42.605 | MS1 | 121.4656674675 | 31.1446303744 | 216 | 152650 | -87.10 | 2.64 | 60.35 | 0.01 | 2.50 | 1573 |

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
| 3219455 | 2 | 121.4732803729 | 31.1525935742 | 226 | 4 | 1 | 24.0 | TDD | 236 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3219612 | 11 | 121.4676264173 | 31.1510084201 | 76 | 13 | 7 | 26.3 | FDD | 372 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3229216 | 8 | 121.4681819242 | 31.1485372464 | 223 | 1 | 10 | 29.7 | FDD | 526 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3233328 | 7 | 121.4652446508 | 31.1478540988 | 139 | 11 | 7 | 26.9 | FDD | 269 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3237228 | 5 | 121.4689507132 | 31.1441100290 | 183 | 7 | 4 | 27.1 | TDD | 952 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3239817 | 13 | 121.4686156565 | 31.1526874913 | 142 | 6 | 4 | 24.9 | FDD | 767 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3244344 | 3 | 121.4684377400 | 31.1494425872 | 276 | 12 | 7 | 18.0 | TDD | 210 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3246336 | 10 | 121.4712377329 | 31.1545270648 | 74 | 10 | 4 | 4.4 | FDD | 242 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3249721 | 4 | 121.4661556040 | 31.1446552157 | 109 | 4 | 0 | 4.9 | TDD | 468 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3252478 | 12 | 121.4725239173 | 31.1540362615 | 174 | 5 | 9 | 4.0 | FDD | 216 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3260491 | 6 | 121.4659693247 | 31.1545556522 | 136 | 1 | 6 | 0.6 | TDD | 287 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3263782 | 9 | 121.4685067315 | 31.1460793020 | 110 | 12 | 9 | 24.0 | FDD | 624 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3276674 | 1 | 121.4662743318 | 31.1444042398 | 56 | 7 | 10 | 17.8 | TDD | 709 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.485 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.485 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.164 | NREventA2 | measId:1;ServCellPCI:116;Se... |
| 2024-09-20 22:21:35.300 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.589 | NREventA5 | measId:3;ServCellPCI:116;Se... |
| 2024-09-20 22:21:35.623 | NRHandoverAttempt | SourcePCI:116;SourceNR-ARFC... |
| 2024-09-20 22:21:35.648 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.663 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.778 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.778 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276674 | 1 | 16.8604 | 14.8091 | -116.4901 | 19.4807 | 112.3879 | 0.0054 | 0.0062 |
| 2024_09_20 22:00 | 3219455 | 2 | 16.4656 | 14.7704 | -117.7671 | 14.0673 | 166.6528 | 0.0135 | 0.0046 |
| 2024_09_20 22:00 | 3244344 | 3 | 5.4608 | 17.7291 | -117.3569 | 7.4132 | 181.6049 | 0.0054 | 0.0051 |
| 2024_09_20 22:00 | 3249721 | 4 | 13.1779 | 11.2814 | -116.7980 | 18.2653 | 116.9402 | 0.0064 | 0.0162 |
| 2024_09_20 22:00 | 3237228 | 5 | 15.0323 | 6.1496 | -114.0476 | 6.6725 | 102.1470 | 0.0035 | 0.0022 |
| 2024_09_20 22:00 | 3260491 | 6 | 13.8709 | 16.2777 | -116.3789 | 7.1811 | 97.7561 | 0.0081 | 0.0120 |
| 2024_09_20 22:00 | 3233328 | 7 | 6.6207 | 5.9419 | -116.8687 | 4.2958 | 46.0611 | 0.0047 | 0.0141 |
| 2024_09_20 22:00 | 3229216 | 8 | 8.7403 | 18.9153 | -114.5757 | 3.8668 | 32.8677 | 0.0133 | 0.0001 |
| 2024_09_20 22:00 | 3263782 | 9 | 9.8317 | 8.2339 | -117.9711 | 4.3868 | 43.3438 | 0.0052 | 0.0148 |
| 2024_09_20 22:00 | 3246336 | 10 | 14.1336 | 18.3864 | -114.6036 | 3.2629 | 36.9289 | 0.0156 | 0.0114 |
| 2024_09_20 22:00 | 3219612 | 11 | 6.0099 | 12.1632 | -116.1616 | 4.2644 | 37.8601 | 0.0033 | 0.0141 |
| 2024_09_20 22:00 | 3252478 | 12 | 11.0160 | 16.5132 | -117.5168 | 4.7929 | 52.6372 | 0.0069 | 0.0178 |
| 2024_09_20 22:00 | 3239817 | 13 | 12.8257 | 6.4642 | -116.2870 | 4.3261 | 30.3152 | 0.0112 | 0.0061 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414462_2356F6E0 | 504990 | 468 | -92.4 | 504990 | 236 | -94.5 | 504990 | 952 | -97.9 | 504990 | 709 |
| MR_1774414462_C5715EE9 | 152650 | 216 | -90.0 | 152650 | 624 | -96.7 | 152650 | 372 | -98.2 | 152650 | 767 |
| MR_1774414462_6C9E6568 | 504990 | 468 | -92.1 | 504990 | 236 | -92.5 | 504990 | 952 | -97.7 | 504990 | 709 |
| MR_1774414462_908D2829 | 504990 | 468 | -95.5 | 504990 | 236 | -95.2 | 504990 | 952 | -97.9 | 504990 | 709 |
| MR_1774414462_6EE82FBF | 504990 | 468 | -95.8 | 504990 | 236 | -95.9 | 504990 | 952 | -95.7 | 504990 | 709 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1632: `671229e9-de8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `671229e9-de8f-4fb6-8eb6-e858b8dcb205` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1632] topology](images/train_1632.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254215_3
- `C2`: Increase transmission power for 3254215_3
- `C3`: Decrease transmission power for 3275770_1
- `C4`: Add neighbor relationship between 3261114_2 and 3254215_3
- `C5`: Increase A3 Offset threshold for 3254215_3
- `C6`: Lift the tilt angle  of 3254215_3 by 9 degrees
- `C7`: Press down the tilt angle of 3275770_1 by 6 degrees
- `C8`: Add neighbor relationship between 3275770_1 and 3254215_3
- `C9`: Lift the tilt angle of 3275770_1 by 6 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275770_1
- `C11`: Adjust the azimuth of 3275770_1 by 50 degrees
- `C12`: Increase A3 Offset threshold for 3275770_1
- `C13`: Decrease A3 Offset threshold for 3254215_3
- `C14`: Adjust the azimuth of 3254215_3 by 16 degrees
- `C15`: Press down the tilt angle  of 3254215_3 by 9 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275770_1
- `C17`: Increase transmission power for 3275770_1
- `C18`: Insufficient data; more data is needed for judgment. **← 정답**
- `C19`: Decrease A3 Offset threshold for 3275770_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254215_3
- `C21`: Decrease transmission power for 3254215_3
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.602 | MS1 | 121.4656729141 | 31.1446226520 | 566 | 504990 | -88.77 | 15.88 | 455.88 | 0.17 | 2.69 | 1562 |
| 2024-09-20 22:21:32.553 | MS1 | 121.4656686949 | 31.1446244156 | 566 | 504990 | -87.86 | 14.48 | 398.09 | 0.18 | 2.39 | 1591 |
| 2024-09-20 22:21:33.842 | MS1 | 121.4656721181 | 31.1446219213 | 566 | 504990 | -90.60 | 16.40 | 390.78 | 0.17 | 2.84 | 1585 |
| 2024-09-20 22:21:34.612 | MS1 | 121.4656765180 | 31.1446278992 | 566 | 504990 | -90.42 | 16.29 | 85.15 | 0.19 | 2.73 | 1580 |
| 2024-09-20 22:21:35.619 | MS1 | 121.4656770055 | 31.1446248748 | 566 | 504990 | -88.17 | 16.99 | 78.93 | 0.07 | 2.05 | 1562 |
| 2024-09-20 22:21:36.737 | MS1 | 121.4656706169 | 31.1446284405 | 566 | 504990 | -87.30 | 16.97 | 83.85 | 0.16 | 2.63 | 1576 |
| 2024-09-20 22:21:37.536 | MS1 | 121.4656749547 | 31.1446244174 | 566 | 504990 | -90.25 | 10.48 | 64.90 | 0.09 | 2.21 | 1587 |
| 2024-09-20 22:21:38.889 | MS1 | 121.4656748193 | 31.1446336588 | 566 | 504990 | -89.77 | 10.37 | 91.17 | 0.07 | 2.53 | 1569 |
| 2024-09-20 22:21:39.707 | MS1 | 121.4656739429 | 31.1446195816 | 566 | 504990 | -89.92 | 12.52 | 56.34 | 0.07 | 2.16 | 1575 |
| 2024-09-20 22:21:40.821 | MS1 | 121.4656716743 | 31.1446206115 | 566 | 504990 | -90.71 | 8.15 | 588.65 | 0.06 | 2.51 | 1582 |
| 2024-09-20 22:21:41.962 | MS1 | 121.4656613832 | 31.1446344718 | 566 | 504990 | -90.31 | 10.35 | 423.29 | 0.13 | 2.85 | 1582 |
| 2024-09-20 22:21:42.759 | MS1 | 121.4656648481 | 31.1446241187 | 566 | 504990 | -92.75 | 7.14 | 341.05 | 0.13 | 2.89 | 1596 |

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
| 3215206 | 4 | 121.4686824959 | 31.1497421288 | 117 | 0 | 3 | 46.3 | TDD | 255 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3254215 | 3 | 121.4721600928 | 31.1499266229 | 242 | 6 | 2 | 40.7 | TDD | 694 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3261114 | 2 | 121.4679350593 | 31.1513599837 | 112 | 15 | 4 | 38.1 | TDD | 93 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3275770 | 1 | 121.4667415200 | 31.1553548739 | 318 | 4 | 4 | 32.9 | TDD | 566 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.233 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.248 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.374 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.374 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.110 | NREventA3 | measId:2;ServCellPCI:636;Se... |
| 2024-09-20 22:21:38.350 | NRHandoverAttempt | SourcePCI:636;SourceNR-ARFC... |
| 2024-09-20 22:21:38.384 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.396 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.525 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.525 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3275770 | 1 | 84.8813 | 77.4843 | -115.8060 | 16.2384 | 123.9382 | 0.0049 | 0.0183 |
| 2024_09_19 22:00 | 3261114 | 2 | 85.6723 | 76.4256 | -115.4481 | 17.0059 | 94.4122 | 0.0099 | 0.0108 |
| 2024_09_19 22:00 | 3254215 | 3 | 88.1334 | 85.0431 | -117.2618 | 18.9600 | 116.0785 | 0.0161 | 0.0018 |
| 2024_09_19 22:00 | 3215206 | 4 | 84.2889 | 84.8926 | -116.1453 | 8.1463 | 84.7893 | 0.0033 | 0.0090 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416011_857DFC43 | 504990 | 566 | -89.6 | 504990 | 694 | -89.3 | 504990 | 93 | -103.4 | 504990 | 255 |
| MR_1774416011_35A6D7C2 | 504990 | 566 | -92.2 | 504990 | 694 | -91.5 | 504990 | 93 | -103.2 | 504990 | 255 |
| MR_1774416011_C7DF35D9 | 504990 | 566 | -90.5 | 504990 | 694 | -91.9 | 504990 | 93 | -101.3 | 504990 | 255 |
| MR_1774416011_1820CE0F | 504990 | 566 | -89.4 | 504990 | 694 | -89.3 | 504990 | 93 | -99.6 | 504990 | 255 |
| MR_1774416011_C2628667 | 504990 | 566 | -90.7 | 504990 | 694 | -92.1 | 504990 | 93 | -102.8 | 504990 | 255 |
| MR_1774416011_8074991A | 504990 | 566 | -92.2 | 504990 | 694 | -90.3 | 504990 | 93 | -102.8 | 504990 | 255 |
| MR_1774416011_5B86A2FF | 504990 | 566 | -89.4 | 504990 | 694 | -91.3 | 504990 | 93 | -101.4 | 504990 | 255 |
| MR_1774416011_4B670DCF | 504990 | 566 | -89.4 | 504990 | 694 | -91.2 | 504990 | 93 | -101.2 | 504990 | 255 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1633: `6e9508b9-4d9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6e9508b9-4d9c-42bd-acf5-cdd6c8b26600` |
| Tag | **multiple-answer** |
| 정답 | **C4|C6** |
| C4 의미 | Decrease transmission power for 3260147_3 |
| C6 의미 | Press down the tilt angle  of 3260147_3 by 4 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1633] topology](images/train_1633.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3260147_3 by 4 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260147_3
- `C3`: Adjust the azimuth of 3260147_3 by 21 degrees
- `C4`: Decrease transmission power for 3260147_3 **← 정답**
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266605_2
- `C6`: Press down the tilt angle  of 3260147_3 by 4 degrees **← 정답**
- `C7`: Lift the tilt angle of 3266605_2 by 4 degrees
- `C8`: Increase transmission power for 3260147_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260147_3
- `C10`: Check test server and transmission issues
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266605_2
- `C12`: Decrease transmission power for 3266605_2
- `C13`: Increase A3 Offset threshold for 3266605_2
- `C14`: Add neighbor relationship between 3266605_2 and 3260147_3
- `C15`: Increase transmission power for 3266605_2
- `C16`: Increase A3 Offset threshold for 3260147_3
- `C17`: Press down the tilt angle of 3266605_2 by 4 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease A3 Offset threshold for 3260147_3
- `C20`: Decrease A3 Offset threshold for 3266605_2
- `C21`: Adjust the azimuth of 3266605_2 by 13 degrees
- `C22`: Add neighbor relationship between 3233508_4 and 3260147_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.556 | MS1 | 121.4656619845 | 31.1446254713 | 198 | 504990 | -80.28 | 14.66 | 374.89 | 0.06 | 2.92 | 1592 |
| 2024-09-20 22:21:32.611 | MS1 | 121.4656737239 | 31.1446216150 | 198 | 504990 | -83.25 | 12.07 | 433.81 | 0.12 | 2.50 | 1599 |
| 2024-09-20 22:21:33.194 | MS1 | 121.4656702994 | 31.1446290452 | 198 | 504990 | -83.10 | 14.57 | 416.94 | 0.14 | 2.14 | 1585 |
| 2024-09-20 22:21:34.549 | MS1 | 121.4656766047 | 31.1446223220 | 198 | 504990 | -86.72 | 2.28 | 55.51 | 0.02 | 1.25 | 1586 |
| 2024-09-20 22:21:35.364 | MS1 | 121.4656740927 | 31.1446240932 | 198 | 504990 | -91.13 | 0.27 | 79.74 | 0.07 | 1.24 | 1575 |
| 2024-09-20 22:21:36.329 | MS1 | 121.4656665740 | 31.1446229784 | 198 | 504990 | -91.35 | 2.19 | 82.10 | 0.12 | 1.16 | 1584 |
| 2024-09-20 22:21:37.159 | MS1 | 121.4656682712 | 31.1446259331 | 198 | 504990 | -87.08 | 0.78 | 63.54 | 0.11 | 1.00 | 1571 |
| 2024-09-20 22:21:38.714 | MS1 | 121.4656666308 | 31.1446261774 | 198 | 504990 | -94.48 | 3.24 | 80.12 | 0.17 | 1.22 | 1578 |
| 2024-09-20 22:21:39.396 | MS1 | 121.4656672736 | 31.1446268118 | 198 | 504990 | -89.04 | 0.38 | 68.33 | 0.07 | 1.23 | 1597 |
| 2024-09-20 22:21:40.519 | MS1 | 121.4656682991 | 31.1446360438 | 198 | 504990 | -75.59 | 17.43 | 308.05 | 0.06 | 2.04 | 1595 |
| 2024-09-20 22:21:41.260 | MS1 | 121.4656750399 | 31.1446295413 | 198 | 504990 | -84.94 | 16.72 | 563.42 | 0.17 | 2.41 | 1569 |
| 2024-09-20 22:21:42.545 | MS1 | 121.4656769857 | 31.1446258460 | 198 | 504990 | -83.68 | 14.80 | 557.95 | 0.17 | 2.58 | 1598 |

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
| 3231955 | 1 | 121.4727591833 | 31.1518096937 | 52 | 1 | 8 | 32.9 | TDD | 298 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3233508 | 4 | 121.4656280027 | 31.1482929511 | 324 | 11 | 1 | 32.6 | TDD | 847 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3260147 | 3 | 121.4731629660 | 31.1446916634 | 290 | 0 | 9 | 46.5 | TDD | 422 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3266605 | 2 | 121.4730229267 | 31.1546718121 | 225 | 2 | 11 | 40.6 | TDD | 198 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.157 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.175 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.300 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.300 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231955 | 1 | 9.7027 | 5.3778 | -114.1095 | 8.4696 | 159.0496 | 0.0118 | 0.0167 |
| 2024_09_20 22:00 | 3266605 | 2 | 8.8834 | 10.2246 | -108.2024 | 18.1089 | 92.8625 | 0.0095 | 0.0084 |
| 2024_09_20 22:00 | 3260147 | 3 | 7.3662 | 5.2298 | -116.5820 | 15.6465 | 81.3661 | 0.0149 | 0.0044 |
| 2024_09_20 22:00 | 3233508 | 4 | 13.9425 | 12.6859 | -115.2461 | 5.0841 | 126.2012 | 0.0018 | 0.0062 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413544_E2D97746 | 504990 | 422 | -86.3 | 504990 | 198 | -84.3 | 504990 | 847 | -87.1 | 504990 | 298 |
| MR_1774413544_5DFC6D05 | 504990 | 198 | -86.0 | 504990 | 422 | -85.6 | 504990 | 847 | -88.2 | 504990 | 298 |
| MR_1774413544_152A7FCB | 504990 | 198 | -88.6 | 504990 | 422 | -84.7 | 504990 | 847 | -87.7 | 504990 | 298 |
| MR_1774413544_0ECC51EB | 504990 | 422 | -88.0 | 504990 | 198 | -83.2 | 504990 | 847 | -90.2 | 504990 | 298 |
| MR_1774413544_8483C20C | 504990 | 422 | -85.4 | 504990 | 198 | -86.0 | 504990 | 847 | -86.4 | 504990 | 298 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1634: `adbb0d5b-18a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `adbb0d5b-18a2-4ff0-847e-453a14aeea76` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1634] topology](images/train_1634.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246077_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212253_2
- `C3`: Adjust the azimuth of 3246077_1 by 46 degrees
- `C4`: Decrease transmission power for 3246077_1
- `C5`: Press down the tilt angle of 3212253_2 by 10 degrees
- `C6`: Decrease A3 Offset threshold for 3246077_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246077_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Add neighbor relationship between 3212253_2 and 3246077_1
- `C10`: Decrease transmission power for 3212253_2
- `C11`: Press down the tilt angle  of 3246077_1 by 10 degrees
- `C12`: Increase transmission power for 3246077_1
- `C13`: Increase A3 Offset threshold for 3246077_1
- `C14`: Check test server and transmission issues **← 정답**
- `C15`: Lift the tilt angle of 3212253_2 by 10 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212253_2
- `C17`: Add neighbor relationship between 3275052_3 and 3246077_1
- `C18`: Adjust the azimuth of 3212253_2 by 50 degrees
- `C19`: Increase A3 Offset threshold for 3212253_2
- `C20`: Decrease A3 Offset threshold for 3212253_2
- `C21`: Lift the tilt angle  of 3246077_1 by 10 degrees
- `C22`: Increase transmission power for 3212253_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.933 | MS1 | 121.4656649473 | 31.1446216217 | 923 | 504990 | -90.17 | 16.24 | 326.80 | 0.05 | 2.38 | 1560 |
| 2024-09-20 22:21:32.220 | MS1 | 121.4656738442 | 31.1446219520 | 923 | 504990 | -90.80 | 16.28 | 565.82 | 0.01 | 2.52 | 1600 |
| 2024-09-20 22:21:33.291 | MS1 | 121.4656686246 | 31.1446269183 | 923 | 504990 | -88.10 | 15.12 | 453.76 | 0.06 | 2.42 | 1591 |
| 2024-09-20 22:21:34.785 | MS1 | 121.4656592035 | 31.1446181314 | 923 | 504990 | -86.96 | 17.84 | 53.26 | 0.09 | 2.01 | 349 |
| 2024-09-20 22:21:35.326 | MS1 | 121.4656779717 | 31.1446205821 | 923 | 504990 | -86.83 | 13.67 | 67.62 | 0.10 | 2.28 | 358 |
| 2024-09-20 22:21:36.166 | MS1 | 121.4656726296 | 31.1446300549 | 923 | 504990 | -88.97 | 16.82 | 57.98 | 0.02 | 2.78 | 420 |
| 2024-09-20 22:21:37.103 | MS1 | 121.4656664246 | 31.1446323614 | 923 | 504990 | -89.53 | 12.81 | 95.53 | 0.13 | 2.15 | 483 |
| 2024-09-20 22:21:38.560 | MS1 | 121.4656696479 | 31.1446318670 | 923 | 504990 | -93.33 | 11.14 | 63.85 | 0.16 | 2.09 | 416 |
| 2024-09-20 22:21:39.133 | MS1 | 121.4656716983 | 31.1446235836 | 923 | 504990 | -91.28 | 10.86 | 67.16 | 0.16 | 2.14 | 387 |
| 2024-09-20 22:21:40.350 | MS1 | 121.4656737168 | 31.1446316899 | 923 | 504990 | -93.85 | 8.97 | 512.73 | 0.18 | 2.80 | 1574 |
| 2024-09-20 22:21:41.839 | MS1 | 121.4656749952 | 31.1446239581 | 923 | 504990 | -89.22 | 7.67 | 595.87 | 0.09 | 2.50 | 1573 |
| 2024-09-20 22:21:42.104 | MS1 | 121.4656617782 | 31.1446322034 | 923 | 504990 | -92.35 | 11.95 | 359.76 | 0.00 | 2.01 | 1562 |

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
| 3212253 | 2 | 121.4672268165 | 31.1459749470 | 76 | 4 | 0 | 38.2 | TDD | 923 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3243185 | 4 | 121.4733893477 | 31.1445421988 | 355 | 13 | 1 | 21.8 | TDD | 55 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3246077 | 1 | 121.4698193931 | 31.1559728732 | 243 | 14 | 5 | 47.9 | TDD | 795 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3275052 | 3 | 121.4753967849 | 31.1475593160 | 298 | 10 | 12 | 46.6 | TDD | 933 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.753 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.768 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.906 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.906 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.653 | NREventA3 | measId:2;ServCellPCI:751;Se... |
| 2024-09-20 22:21:37.893 | NRHandoverAttempt | SourcePCI:751;SourceNR-ARFC... |
| 2024-09-20 22:21:37.939 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.953 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.098 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.098 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246077 | 1 | 6.2774 | 13.2373 | -117.0238 | 14.5789 | 160.9598 | 0.0157 | 0.0199 |
| 2024_09_20 22:00 | 3212253 | 2 | 11.1546 | 14.6413 | -117.5605 | 15.8956 | 195.5136 | 0.0022 | 0.0007 |
| 2024_09_20 22:00 | 3275052 | 3 | 7.3504 | 15.5170 | -115.3209 | 13.8274 | 89.4199 | 0.0144 | 0.0194 |
| 2024_09_20 22:00 | 3243185 | 4 | 6.7522 | 14.6191 | -114.0356 | 16.6491 | 163.7714 | 0.0045 | 0.0038 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412356_AF497E4F | 504990 | 923 | -88.0 | 504990 | 795 | -90.6 | 504990 | 933 | -92.3 | 504990 | 55 |
| MR_1774412356_A0A989E7 | 504990 | 923 | -85.9 | 504990 | 795 | -88.9 | 504990 | 933 | -94.8 | 504990 | 55 |
| MR_1774412356_1167B452 | 504990 | 923 | -86.2 | 504990 | 795 | -88.5 | 504990 | 933 | -94.8 | 504990 | 55 |
| MR_1774412356_82F8B419 | 504990 | 923 | -87.3 | 504990 | 795 | -90.0 | 504990 | 933 | -95.1 | 504990 | 55 |
| MR_1774412356_B3354AC5 | 504990 | 923 | -85.3 | 504990 | 795 | -88.0 | 504990 | 933 | -94.3 | 504990 | 55 |
| MR_1774412356_0CC156C0 | 504990 | 923 | -86.3 | 504990 | 795 | -91.3 | 504990 | 933 | -94.9 | 504990 | 55 |
| MR_1774412356_7CFC1418 | 504990 | 923 | -88.6 | 504990 | 795 | -87.6 | 504990 | 933 | -94.8 | 504990 | 55 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1635: `0df47f28-481...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0df47f28-4811-47dc-bba9-f38c607f16bb` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Add neighbor relationship between 3262312_2 and 3239553_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1635] topology](images/train_1635.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3262312_2 by 32 degrees
- `C2`: Press down the tilt angle of 3262312_2 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239553_1
- `C4`: Increase transmission power for 3262312_2
- `C5`: Decrease transmission power for 3239553_1
- `C6`: Increase A3 Offset threshold for 3262312_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239553_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262312_2
- `C10`: Decrease transmission power for 3262312_2
- `C11`: Add neighbor relationship between 3230971_3 and 3239553_1
- `C12`: Add neighbor relationship between 3262312_2 and 3239553_1 **← 정답**
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262312_2
- `C14`: Lift the tilt angle  of 3239553_1 by 6 degrees
- `C15`: Lift the tilt angle of 3262312_2 by 10 degrees
- `C16`: Adjust the azimuth of 3239553_1 by 7 degrees
- `C17`: Increase transmission power for 3239553_1
- `C18`: Press down the tilt angle  of 3239553_1 by 6 degrees
- `C19`: Increase A3 Offset threshold for 3239553_1
- `C20`: Decrease A3 Offset threshold for 3262312_2
- `C21`: Check test server and transmission issues
- `C22`: Decrease A3 Offset threshold for 3239553_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.382 | MS1 | 121.4656613109 | 31.1446374696 | 770 | 504990 | -75.19 | 15.96 | 580.12 | 0.03 | 2.74 | 1597 |
| 2024-09-20 22:21:32.100 | MS1 | 121.4656656722 | 31.1446273384 | 770 | 504990 | -78.17 | 16.77 | 535.56 | 0.05 | 2.06 | 1587 |
| 2024-09-20 22:21:33.784 | MS1 | 121.4656683165 | 31.1446346120 | 770 | 504990 | -81.58 | 12.93 | 366.63 | 0.03 | 2.12 | 1576 |
| 2024-09-20 22:21:34.694 | MS1 | 121.4656743900 | 31.1446328543 | 770 | 504990 | -88.05 | -2.48 | 58.27 | 0.19 | 1.27 | 1595 |
| 2024-09-20 22:21:35.736 | MS1 | 121.4656646117 | 31.1446262021 | 770 | 504990 | -91.31 | -0.24 | 61.52 | 0.04 | 1.00 | 1580 |
| 2024-09-20 22:21:36.624 | MS1 | 121.4656751324 | 31.1446289561 | 770 | 504990 | -88.29 | -1.23 | 62.83 | 0.12 | 1.08 | 1589 |
| 2024-09-20 22:21:37.205 | MS1 | 121.4656648324 | 31.1446290501 | 770 | 504990 | -92.00 | -2.36 | 41.77 | 0.03 | 1.12 | 1564 |
| 2024-09-20 22:21:38.152 | MS1 | 121.4656671657 | 31.1446309115 | 770 | 504990 | -82.96 | 13.99 | 591.67 | 0.18 | 1.11 | 1593 |
| 2024-09-20 22:21:39.384 | MS1 | 121.4656741505 | 31.1446212042 | 770 | 504990 | -77.29 | 12.91 | 363.08 | 0.13 | 1.39 | 1574 |
| 2024-09-20 22:21:40.309 | MS1 | 121.4656705363 | 31.1446184451 | 770 | 504990 | -79.83 | 13.61 | 434.91 | 0.13 | 2.13 | 1563 |
| 2024-09-20 22:21:41.666 | MS1 | 121.4656762256 | 31.1446315081 | 770 | 504990 | -76.72 | 14.58 | 445.36 | 0.18 | 2.46 | 1577 |
| 2024-09-20 22:21:42.294 | MS1 | 121.4656608742 | 31.1446375639 | 770 | 504990 | -81.45 | 12.27 | 463.84 | 0.13 | 2.83 | 1596 |

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
| 3230971 | 3 | 121.4757549205 | 31.1521906442 | 206 | 1 | 2 | 29.3 | TDD | 312 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3239553 | 1 | 121.4739453830 | 31.1482696935 | 236 | 3 | 6 | 45.1 | TDD | 336 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3262312 | 2 | 121.4665131261 | 31.1456539196 | 183 | 15 | 7 | 28.0 | TDD | 770 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3263401 | 4 | 121.4754741599 | 31.1543123633 | 104 | 9 | 0 | 39.6 | TDD | 261 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.923 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.943 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.048 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.048 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.747 | NREventA3 | measId:2;ServCellPCI:274;Se... |
| 2024-09-20 22:21:35.747 | NREventA3 | measId:2;ServCellPCI:274;Se... |
| 2024-09-20 22:21:36.747 | NREventA3 | measId:2;ServCellPCI:274;Se... |
| 2024-09-20 22:21:39.247 | NRRRCReestablishAttempt | PCI:274 |
| 2024-09-20 22:21:39.259 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.274 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.423 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.423 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239553 | 1 | 9.9925 | 8.4786 | -114.3822 | 9.0181 | 145.2866 | 0.0056 | 0.0176 |
| 2024_09_20 22:00 | 3262312 | 2 | 9.0236 | 14.6107 | -115.2158 | 10.0861 | 151.8076 | 0.0084 | 0.1286 |
| 2024_09_20 22:00 | 3230971 | 3 | 9.4486 | 13.4444 | -116.9648 | 19.4192 | 101.4253 | 0.0010 | 0.0182 |
| 2024_09_20 22:00 | 3263401 | 4 | 19.6263 | 14.2455 | -116.0295 | 13.7546 | 179.9692 | 0.0154 | 0.0190 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416642_63AD0D41 | 504990 | 770 | -89.6 | 504990 | 336 | -82.2 | 504990 | 312 | -86.1 | 504990 | 261 |
| MR_1774416642_DB4C0658 | 504990 | 336 | -81.9 | 504990 | 770 | -86.6 | 504990 | 312 | -88.0 | 504990 | 261 |
| MR_1774416642_47A292D3 | 504990 | 336 | -80.6 | 504990 | 770 | -86.9 | 504990 | 312 | -88.2 | 504990 | 261 |
| MR_1774416642_100DBF59 | 504990 | 336 | -81.5 | 504990 | 770 | -90.0 | 504990 | 312 | -88.5 | 504990 | 261 |
| MR_1774416642_87B577DE | 504990 | 336 | -83.4 | 504990 | 770 | -88.0 | 504990 | 312 | -88.5 | 504990 | 261 |
| MR_1774416642_247FEDB4 | 504990 | 770 | -89.6 | 504990 | 336 | -81.4 | 504990 | 312 | -87.6 | 504990 | 261 |
| MR_1774416642_DBE95A99 | 504990 | 336 | -81.2 | 504990 | 770 | -86.1 | 504990 | 312 | -85.6 | 504990 | 261 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1636: `b65d9400-cd4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b65d9400-cd4c-4921-a44e-8d751a3cfc9f` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275751_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1636] topology](images/train_1636.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275751_1
- `C2`: Increase A3 Offset threshold for 3213300_3
- `C3`: Lift the tilt angle of 3275751_1 by 4 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213300_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213300_3
- `C6`: Check test server and transmission issues
- `C7`: Increase transmission power for 3213300_3
- `C8`: Lift the tilt angle  of 3213300_3 by 0 degrees
- `C9`: Increase A3 Offset threshold for 3275751_1
- `C10`: Adjust the azimuth of 3275751_1 by 31 degrees
- `C11`: Press down the tilt angle of 3275751_1 by 4 degrees
- `C12`: Adjust the azimuth of 3213300_3 by 32 degrees
- `C13`: Add neighbor relationship between 3258985_12 and 3213300_3
- `C14`: Decrease transmission power for 3275751_1
- `C15`: Increase transmission power for 3275751_1
- `C16`: Press down the tilt angle  of 3213300_3 by 0 degrees
- `C17`: Decrease A3 Offset threshold for 3275751_1
- `C18`: Add neighbor relationship between 3275751_1 and 3213300_3
- `C19`: Decrease transmission power for 3213300_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275751_1 **← 정답**
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease A3 Offset threshold for 3213300_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.441 | MS1 | 121.4656703796 | 31.1446314854 | 902 | 504990 | -95.66 | 14.99 | 479.21 | 0.07 | 2.14 | 1597 |
| 2024-09-20 22:21:32.425 | MS1 | 121.4656660604 | 31.1446367610 | 534 | 504990 | -93.46 | 12.30 | 564.61 | 0.14 | 2.52 | 1597 |
| 2024-09-20 22:21:33.592 | MS1 | 121.4656605981 | 31.1446204400 | 208 | 504990 | -94.04 | 14.99 | 314.01 | 0.02 | 2.85 | 1567 |
| 2024-09-20 22:21:34.150 | MS1 | 121.4656580279 | 31.1446184274 | 769 | 152650 | -94.64 | 3.14 | 97.25 | 0.03 | 1.78 | 997 |
| 2024-09-20 22:21:35.657 | MS1 | 121.4656680650 | 31.1446262496 | 806 | 152650 | -88.10 | 4.39 | 84.48 | 0.16 | 1.85 | 913 |
| 2024-09-20 22:21:36.501 | MS1 | 121.4656615897 | 31.1446231094 | 916 | 152650 | -92.61 | 3.06 | 60.98 | 0.03 | 1.52 | 913 |
| 2024-09-20 22:21:37.216 | MS1 | 121.4656581819 | 31.1446191447 | 11 | 152650 | -87.57 | 2.79 | 46.63 | 0.04 | 1.53 | 987 |
| 2024-09-20 22:21:38.817 | MS1 | 121.4656615893 | 31.1446259043 | 769 | 152650 | -95.57 | 5.72 | 51.76 | 0.13 | 1.99 | 913 |
| 2024-09-20 22:21:39.140 | MS1 | 121.4656586617 | 31.1446227509 | 806 | 152650 | -92.67 | 5.99 | 84.90 | 0.07 | 1.76 | 989 |
| 2024-09-20 22:21:40.714 | MS1 | 121.4656642622 | 31.1446294569 | 916 | 152650 | -90.17 | 2.22 | 88.20 | 0.19 | 2.30 | 1575 |
| 2024-09-20 22:21:41.441 | MS1 | 121.4656764550 | 31.1446321240 | 11 | 152650 | -95.89 | 5.06 | 68.99 | 0.07 | 2.84 | 1576 |
| 2024-09-20 22:21:42.467 | MS1 | 121.4656591834 | 31.1446293002 | 769 | 152650 | -92.49 | 6.04 | 78.45 | 0.06 | 2.90 | 1575 |

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
| 3210028 | 8 | 121.4721983378 | 31.1514942260 | 86 | 1 | 6 | 21.7 | FDD | 769 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3211290 | 10 | 121.4684105623 | 31.1527962127 | 169 | 14 | 10 | 2.3 | FDD | 806 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3211537 | 4 | 121.4708048865 | 31.1529120568 | 348 | 12 | 5 | 27.3 | TDD | 208 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3213300 | 3 | 121.4710749032 | 31.1490588738 | 258 | 0 | 11 | 3.5 | TDD | 557 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3217558 | 2 | 121.4691506921 | 31.1472711500 | 169 | 8 | 9 | 12.7 | TDD | 616 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3224941 | 11 | 121.4641359869 | 31.1492591940 | 224 | 3 | 12 | 6.9 | FDD | 11 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3225364 | 7 | 121.4667507328 | 31.1523073433 | 160 | 12 | 0 | 4.6 | FDD | 576 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3230435 | 9 | 121.4654065532 | 31.1441960122 | 87 | 6 | 8 | 25.0 | FDD | 66 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3245970 | 13 | 121.4658418902 | 31.1542791984 | 19 | 3 | 9 | 27.6 | FDD | 955 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3256988 | 5 | 121.4660825310 | 31.1494666598 | 126 | 6 | 4 | 21.1 | TDD | 789 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3258985 | 12 | 121.4640144583 | 31.1448554307 | 191 | 10 | 11 | 0.7 | FDD | 916 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3259276 | 6 | 121.4654237060 | 31.1519406541 | 146 | 14 | 8 | 20.2 | TDD | 534 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3275751 | 1 | 121.4659129599 | 31.1543520658 | 150 | 3 | 12 | 19.9 | TDD | 902 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.088 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.105 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.239 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.239 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.940 | NREventA2 | measId:1;ServCellPCI:306;Se... |
| 2024-09-20 22:21:35.050 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.264 | NREventA5 | measId:3;ServCellPCI:306;Se... |
| 2024-09-20 22:21:35.299 | NRHandoverAttempt | SourcePCI:306;SourceNR-ARFC... |
| 2024-09-20 22:21:35.347 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.361 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.505 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.505 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275751 | 1 | 19.5111 | 12.6664 | -116.5456 | 12.2560 | 165.3935 | 0.0100 | 0.0029 |
| 2024_09_20 22:00 | 3217558 | 2 | 10.3354 | 7.2985 | -115.2128 | 19.7230 | 117.6361 | 0.0013 | 0.0172 |
| 2024_09_20 22:00 | 3213300 | 3 | 10.4102 | 6.2558 | -114.6622 | 15.3935 | 149.9573 | 0.0021 | 0.0038 |
| 2024_09_20 22:00 | 3211537 | 4 | 14.5041 | 13.1274 | -117.7910 | 17.2753 | 141.8793 | 0.0052 | 0.0003 |
| 2024_09_20 22:00 | 3256988 | 5 | 11.4680 | 6.9822 | -114.5443 | 17.3661 | 100.9415 | 0.0031 | 0.0125 |
| 2024_09_20 22:00 | 3259276 | 6 | 12.5985 | 10.8936 | -116.3214 | 7.9909 | 80.5271 | 0.0164 | 0.0082 |
| 2024_09_20 22:00 | 3225364 | 7 | 8.8462 | 13.1320 | -115.1091 | 4.4357 | 49.2564 | 0.0018 | 0.0172 |
| 2024_09_20 22:00 | 3210028 | 8 | 14.5207 | 19.9607 | -116.7044 | 3.5906 | 38.7951 | 0.0159 | 0.0062 |
| 2024_09_20 22:00 | 3230435 | 9 | 15.4559 | 19.9959 | -115.0846 | 4.0697 | 30.4306 | 0.0037 | 0.0101 |
| 2024_09_20 22:00 | 3211290 | 10 | 7.0193 | 17.7963 | -115.0201 | 4.5399 | 39.7693 | 0.0196 | 0.0039 |
| 2024_09_20 22:00 | 3224941 | 11 | 16.2722 | 13.7492 | -115.9580 | 3.6345 | 20.5447 | 0.0169 | 0.0150 |
| 2024_09_20 22:00 | 3258985 | 12 | 10.4470 | 17.3769 | -115.1079 | 3.9706 | 21.8098 | 0.0185 | 0.0058 |
| 2024_09_20 22:00 | 3245970 | 13 | 9.1550 | 17.7325 | -116.4585 | 4.3918 | 20.2461 | 0.0141 | 0.0076 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412307_1354B9B2 | 152650 | 769 | -94.1 | 152650 | 955 | -97.3 | 152650 | 576 | -104.4 | 152650 | 66 |
| MR_1774412307_868D338B | 504990 | 208 | -93.2 | 504990 | 557 | -96.2 | 504990 | 616 | -101.8 | 504990 | 789 |
| MR_1774412307_2FB8094F | 504990 | 208 | -94.1 | 504990 | 557 | -97.6 | 504990 | 616 | -101.7 | 504990 | 789 |
| MR_1774412307_3B637C6E | 152650 | 769 | -93.0 | 152650 | 955 | -96.9 | 152650 | 576 | -107.3 | 152650 | 66 |
| MR_1774412307_1D161DAB | 504990 | 208 | -94.4 | 504990 | 557 | -99.1 | 504990 | 616 | -99.1 | 504990 | 789 |
| MR_1774412307_C4370AEE | 152650 | 769 | -93.8 | 152650 | 955 | -99.0 | 152650 | 576 | -104.7 | 152650 | 66 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1637: `e0bc9573-b99...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e0bc9573-b99f-423a-b515-94d49c31281b` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1637] topology](images/train_1637.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3266994_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266994_1
- `C3`: Check test server and transmission issues
- `C4`: Add neighbor relationship between 3268182_3 and 3253634_2
- `C5`: Increase transmission power for 3253634_2
- `C6`: Add neighbor relationship between 3266994_1 and 3253634_2
- `C7`: Press down the tilt angle  of 3253634_2 by 4 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253634_2
- `C9`: Decrease transmission power for 3266994_1
- `C10`: Adjust the azimuth of 3253634_2 by 9 degrees
- `C11`: Increase A3 Offset threshold for 3266994_1
- `C12`: Decrease A3 Offset threshold for 3266994_1
- `C13`: Decrease A3 Offset threshold for 3253634_2
- `C14`: Insufficient data; more data is needed for judgment. **← 정답**
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253634_2
- `C16`: Lift the tilt angle of 3266994_1 by 2 degrees
- `C17`: Press down the tilt angle of 3266994_1 by 2 degrees
- `C18`: Decrease transmission power for 3253634_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266994_1
- `C20`: Increase A3 Offset threshold for 3253634_2
- `C21`: Lift the tilt angle  of 3253634_2 by 4 degrees
- `C22`: Adjust the azimuth of 3266994_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.793 | MS1 | 121.4656660961 | 31.1446243703 | 24 | 504990 | -87.05 | 13.29 | 329.39 | 0.08 | 2.57 | 1566 |
| 2024-09-20 22:21:32.513 | MS1 | 121.4656729972 | 31.1446214302 | 24 | 504990 | -88.41 | 13.19 | 452.39 | 0.20 | 2.54 | 1587 |
| 2024-09-20 22:21:33.562 | MS1 | 121.4656675132 | 31.1446206228 | 24 | 504990 | -88.56 | 12.92 | 339.17 | 0.18 | 2.01 | 1568 |
| 2024-09-20 22:21:34.367 | MS1 | 121.4656634777 | 31.1446214727 | 24 | 504990 | -85.81 | 12.58 | 68.56 | 0.08 | 2.61 | 1575 |
| 2024-09-20 22:21:35.984 | MS1 | 121.4656589403 | 31.1446377238 | 24 | 504990 | -87.31 | 12.84 | 62.55 | 0.02 | 2.70 | 1564 |
| 2024-09-20 22:21:36.636 | MS1 | 121.4656736917 | 31.1446355937 | 24 | 504990 | -85.50 | 14.26 | 54.36 | 0.12 | 2.38 | 1566 |
| 2024-09-20 22:21:37.658 | MS1 | 121.4656743261 | 31.1446303749 | 24 | 504990 | -93.91 | 9.54 | 64.75 | 0.04 | 2.41 | 1566 |
| 2024-09-20 22:21:38.816 | MS1 | 121.4656617355 | 31.1446197508 | 24 | 504990 | -92.95 | 8.99 | 68.98 | 0.01 | 2.23 | 1584 |
| 2024-09-20 22:21:39.372 | MS1 | 121.4656756753 | 31.1446240183 | 24 | 504990 | -93.11 | 8.61 | 66.31 | 0.15 | 2.38 | 1573 |
| 2024-09-20 22:21:40.457 | MS1 | 121.4656678613 | 31.1446318227 | 24 | 504990 | -89.66 | 7.69 | 553.46 | 0.05 | 2.52 | 1567 |
| 2024-09-20 22:21:41.796 | MS1 | 121.4656711927 | 31.1446307282 | 24 | 504990 | -92.52 | 11.50 | 560.41 | 0.06 | 2.44 | 1568 |
| 2024-09-20 22:21:42.374 | MS1 | 121.4656779308 | 31.1446307724 | 24 | 504990 | -89.31 | 11.08 | 476.14 | 0.10 | 2.57 | 1588 |

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
| 3252754 | 4 | 121.4744257532 | 31.1474405962 | 189 | 15 | 1 | 26.1 | TDD | 45 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3253634 | 2 | 121.4672171882 | 31.1511434217 | 182 | 2 | 10 | 25.4 | TDD | 482 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3266994 | 1 | 121.4700180590 | 31.1523914136 | 144 | 0 | 8 | 32.0 | TDD | 24 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3268182 | 3 | 121.4718833854 | 31.1500599859 | 90 | 14 | 7 | 36.4 | TDD | 754 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.990 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.008 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.144 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.144 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.840 | NREventA3 | measId:2;ServCellPCI:669;Se... |
| 2024-09-20 22:21:38.080 | NRHandoverAttempt | SourcePCI:669;SourceNR-ARFC... |
| 2024-09-20 22:21:38.126 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.138 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.288 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.288 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3266994 | 1 | 94.9776 | 76.3891 | -115.7575 | 7.2961 | 188.5122 | 0.0087 | 0.0009 |
| 2024_09_19 22:00 | 3253634 | 2 | 88.3747 | 88.6921 | -114.2636 | 5.1468 | 188.7952 | 0.0016 | 0.0027 |
| 2024_09_19 22:00 | 3268182 | 3 | 81.1159 | 82.5956 | -114.9334 | 11.5820 | 193.3665 | 0.0069 | 0.0129 |
| 2024_09_19 22:00 | 3252754 | 4 | 89.0803 | 89.0260 | -114.6036 | 15.0638 | 186.9894 | 0.0193 | 0.0076 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414995_F4AFDF6B | 504990 | 24 | -84.4 | 504990 | 482 | -92.5 | 504990 | 754 | -97.4 | 504990 | 45 |
| MR_1774414995_23A30F1A | 504990 | 24 | -87.0 | 504990 | 482 | -95.0 | 504990 | 754 | -98.8 | 504990 | 45 |
| MR_1774414995_9C3CC787 | 504990 | 24 | -87.0 | 504990 | 482 | -94.1 | 504990 | 754 | -98.5 | 504990 | 45 |
| MR_1774414995_6FEFB27F | 504990 | 24 | -85.5 | 504990 | 482 | -95.7 | 504990 | 754 | -98.1 | 504990 | 45 |
| MR_1774414995_E3B216AF | 504990 | 24 | -85.3 | 504990 | 482 | -93.3 | 504990 | 754 | -97.3 | 504990 | 45 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1638: `65477131-2be...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `65477131-2be5-4513-a566-2c1b3e0e1cdd` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1638] topology](images/train_1638.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3242780_4 by 7 degrees
- `C2`: Add neighbor relationship between 3213014_1 and 3242780_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242780_4
- `C4`: Increase transmission power for 3242780_4
- `C5`: Adjust the azimuth of 3242780_4 by 20 degrees
- `C6`: Insufficient data; more data is needed for judgment. **← 정답**
- `C7`: Check test server and transmission issues
- `C8`: Lift the tilt angle  of 3242780_4 by 7 degrees
- `C9`: Add neighbor relationship between 3218771_2 and 3242780_4
- `C10`: Decrease transmission power for 3213014_1
- `C11`: Adjust the azimuth of 3213014_1 by 50 degrees
- `C12`: Lift the tilt angle of 3213014_1 by 8 degrees
- `C13`: Decrease A3 Offset threshold for 3213014_1
- `C14`: Increase transmission power for 3213014_1
- `C15`: Decrease transmission power for 3242780_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213014_1
- `C17`: Decrease A3 Offset threshold for 3242780_4
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213014_1
- `C19`: Increase A3 Offset threshold for 3213014_1
- `C20`: Increase A3 Offset threshold for 3242780_4
- `C21`: Press down the tilt angle of 3213014_1 by 8 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242780_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.152 | MS1 | 121.4656640046 | 31.1446360648 | 705 | 504990 | -90.06 | 14.68 | 580.76 | 0.16 | 2.53 | 1562 |
| 2024-09-20 22:21:32.976 | MS1 | 121.4656629479 | 31.1446349145 | 705 | 504990 | -87.79 | 14.53 | 437.12 | 0.02 | 2.71 | 1590 |
| 2024-09-20 22:21:33.275 | MS1 | 121.4656661347 | 31.1446328140 | 705 | 504990 | -89.83 | 14.38 | 431.07 | 0.11 | 2.39 | 1591 |
| 2024-09-20 22:21:34.344 | MS1 | 121.4656651241 | 31.1446363494 | 705 | 504990 | -89.23 | 16.26 | 51.02 | 0.10 | 2.74 | 1591 |
| 2024-09-20 22:21:35.600 | MS1 | 121.4656774104 | 31.1446234248 | 705 | 504990 | -89.37 | 12.36 | 78.45 | 0.18 | 2.29 | 1579 |
| 2024-09-20 22:21:36.461 | MS1 | 121.4656652220 | 31.1446375066 | 705 | 504990 | -89.92 | 17.59 | 87.89 | 0.18 | 2.24 | 1594 |
| 2024-09-20 22:21:37.480 | MS1 | 121.4656748291 | 31.1446331743 | 705 | 504990 | -93.08 | 9.63 | 48.92 | 0.08 | 2.07 | 1565 |
| 2024-09-20 22:21:38.325 | MS1 | 121.4656643009 | 31.1446301559 | 705 | 504990 | -89.25 | 7.13 | 87.99 | 0.09 | 2.77 | 1568 |
| 2024-09-20 22:21:39.131 | MS1 | 121.4656765688 | 31.1446372467 | 705 | 504990 | -89.01 | 10.48 | 50.43 | 0.02 | 2.80 | 1567 |
| 2024-09-20 22:21:40.702 | MS1 | 121.4656702368 | 31.1446195187 | 705 | 504990 | -92.20 | 9.70 | 421.29 | 0.08 | 2.16 | 1589 |
| 2024-09-20 22:21:41.707 | MS1 | 121.4656623337 | 31.1446265639 | 705 | 504990 | -91.76 | 8.01 | 317.81 | 0.19 | 2.97 | 1560 |
| 2024-09-20 22:21:42.488 | MS1 | 121.4656604059 | 31.1446245629 | 705 | 504990 | -93.35 | 9.04 | 412.27 | 0.09 | 2.93 | 1568 |

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
| 3213014 | 1 | 121.4735984553 | 31.1547557920 | 117 | 7 | 5 | 24.8 | TDD | 705 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3218771 | 2 | 121.4652542362 | 31.1458331699 | 216 | 13 | 4 | 33.9 | TDD | 811 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3242780 | 4 | 121.4652449768 | 31.1531768652 | 158 | 5 | 6 | 38.7 | TDD | 493 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3255798 | 3 | 121.4742032732 | 31.1496653658 | 40 | 5 | 5 | 45.8 | TDD | 220 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.927 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.943 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.059 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.059 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.790 | NREventA3 | measId:2;ServCellPCI:918;Se... |
| 2024-09-20 22:21:38.030 | NRHandoverAttempt | SourcePCI:918;SourceNR-ARFC... |
| 2024-09-20 22:21:38.071 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.084 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.203 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.203 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3213014 | 1 | 75.3239 | 75.1321 | -116.8455 | 8.7402 | 148.8058 | 0.0095 | 0.0008 |
| 2024_09_19 22:00 | 3218771 | 2 | 89.9272 | 94.1414 | -117.9024 | 7.7672 | 125.9339 | 0.0130 | 0.0197 |
| 2024_09_19 22:00 | 3255798 | 3 | 89.8620 | 92.0684 | -117.0993 | 17.1919 | 99.0041 | 0.0075 | 0.0062 |
| 2024_09_19 22:00 | 3242780 | 4 | 79.9463 | 82.3417 | -116.7816 | 16.6738 | 192.7997 | 0.0126 | 0.0099 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413180_D67112B9 | 504990 | 705 | -89.1 | 504990 | 493 | -93.4 | 504990 | 811 | -97.6 | 504990 | 220 |
| MR_1774413180_6DC5343A | 504990 | 705 | -90.1 | 504990 | 493 | -93.3 | 504990 | 811 | -98.7 | 504990 | 220 |
| MR_1774413180_45459F48 | 504990 | 705 | -87.5 | 504990 | 493 | -90.6 | 504990 | 811 | -99.4 | 504990 | 220 |
| MR_1774413180_CF1DAF52 | 504990 | 705 | -88.9 | 504990 | 493 | -93.0 | 504990 | 811 | -99.6 | 504990 | 220 |
| MR_1774413180_15D486F8 | 504990 | 705 | -89.0 | 504990 | 493 | -90.0 | 504990 | 811 | -97.6 | 504990 | 220 |
| MR_1774413180_CB363CDC | 504990 | 705 | -88.8 | 504990 | 493 | -90.3 | 504990 | 811 | -99.7 | 504990 | 220 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1639: `2ea33a0a-3aa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2ea33a0a-3aa9-4c88-b1c7-ad8662cbe10c` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3223591_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1639] topology](images/train_1639.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3274335_2 by 4 degrees
- `C2`: Increase transmission power for 3274335_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223591_1
- `C4`: Decrease transmission power for 3223591_1
- `C5`: Decrease A3 Offset threshold for 3274335_2
- `C6`: Add neighbor relationship between 3223591_1 and 3274335_2
- `C7`: Adjust the azimuth of 3274335_2 by 50 degrees
- `C8`: Press down the tilt angle of 3223591_1 by 3 degrees
- `C9`: Check test server and transmission issues
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274335_2
- `C11`: Lift the tilt angle  of 3274335_2 by 4 degrees
- `C12`: Lift the tilt angle of 3223591_1 by 3 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Adjust the azimuth of 3223591_1 by 37 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274335_2
- `C16`: Add neighbor relationship between 3252946_4 and 3274335_2
- `C17`: Decrease transmission power for 3274335_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223591_1 **← 정답**
- `C19`: Increase A3 Offset threshold for 3274335_2
- `C20`: Increase A3 Offset threshold for 3223591_1
- `C21`: Decrease A3 Offset threshold for 3223591_1
- `C22`: Increase transmission power for 3223591_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.801 | MS1 | 121.4656767011 | 31.1446317690 | 737 | 504990 | -85.77 | 13.94 | 315.02 | 0.01 | 2.25 | 1565 |
| 2024-09-20 22:21:32.666 | MS1 | 121.4656612379 | 31.1446271481 | 737 | 504990 | -89.98 | 12.36 | 470.44 | 0.06 | 2.28 | 1583 |
| 2024-09-20 22:21:33.170 | MS1 | 121.4656719483 | 31.1446267091 | 737 | 504990 | -89.48 | 13.83 | 521.80 | 0.15 | 2.08 | 1577 |
| 2024-09-20 22:21:34.979 | MS1 | 121.4656603977 | 31.1446244442 | 737 | 504990 | -90.29 | 14.62 | 85.94 | 0.52 | 2.26 | 635 |
| 2024-09-20 22:21:35.220 | MS1 | 121.4656744302 | 31.1446286149 | 737 | 504990 | -88.83 | 14.92 | 57.13 | 0.61 | 2.33 | 619 |
| 2024-09-20 22:21:36.704 | MS1 | 121.4656759092 | 31.1446262074 | 737 | 504990 | -85.13 | 12.55 | 56.70 | 0.63 | 2.76 | 627 |
| 2024-09-20 22:21:37.801 | MS1 | 121.4656763040 | 31.1446291991 | 737 | 504990 | -91.85 | 11.05 | 96.50 | 0.62 | 2.43 | 573 |
| 2024-09-20 22:21:38.244 | MS1 | 121.4656600782 | 31.1446180308 | 737 | 504990 | -93.01 | 11.71 | 59.72 | 0.61 | 2.83 | 526 |
| 2024-09-20 22:21:39.912 | MS1 | 121.4656747211 | 31.1446318969 | 737 | 504990 | -93.97 | 10.02 | 48.73 | 0.62 | 2.42 | 501 |
| 2024-09-20 22:21:40.879 | MS1 | 121.4656744935 | 31.1446293041 | 737 | 504990 | -92.99 | 8.92 | 562.09 | 0.14 | 2.06 | 1584 |
| 2024-09-20 22:21:41.370 | MS1 | 121.4656759404 | 31.1446229561 | 737 | 504990 | -92.26 | 7.68 | 364.10 | 0.10 | 2.32 | 1573 |
| 2024-09-20 22:21:42.498 | MS1 | 121.4656683133 | 31.1446308604 | 737 | 504990 | -89.70 | 10.98 | 586.72 | 0.08 | 2.22 | 1575 |

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
| 3223591 | 1 | 121.4736974465 | 31.1442713983 | 310 | 0 | 9 | 33.4 | TDD | 737 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3243517 | 3 | 121.4755391403 | 31.1521207267 | 292 | 8 | 8 | 23.1 | TDD | 469 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3252946 | 4 | 121.4748067489 | 31.1496372495 | 195 | 15 | 3 | 47.0 | TDD | 71 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3274335 | 2 | 121.4686603364 | 31.1475061237 | 145 | 0 | 6 | 33.1 | TDD | 753 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.828 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.848 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.990 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.990 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.678 | NREventA3 | measId:2;ServCellPCI:53;Ser... |
| 2024-09-20 22:21:37.918 | NRHandoverAttempt | SourcePCI:53;SourceNR-ARFCN... |
| 2024-09-20 22:21:37.961 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.973 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.078 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.078 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223591 | 1 | 5.9365 | 19.0586 | -116.3310 | 14.6147 | 194.6658 | 0.0016 | 0.0027 |
| 2024_09_20 22:00 | 3274335 | 2 | 9.0658 | 18.2460 | -117.6833 | 8.6727 | 116.7871 | 0.0144 | 0.0187 |
| 2024_09_20 22:00 | 3243517 | 3 | 16.7329 | 11.7125 | -115.2241 | 5.3256 | 196.0808 | 0.0105 | 0.0155 |
| 2024_09_20 22:00 | 3252946 | 4 | 13.8965 | 19.0065 | -116.0324 | 17.0328 | 137.0057 | 0.0094 | 0.0063 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415559_EEA40900 | 504990 | 737 | -90.4 | 504990 | 753 | -95.6 | 504990 | 71 | -100.3 | 504990 | 469 |
| MR_1774415559_B8416177 | 504990 | 737 | -92.2 | 504990 | 753 | -94.8 | 504990 | 71 | -100.5 | 504990 | 469 |
| MR_1774415559_908F9372 | 504990 | 737 | -89.9 | 504990 | 753 | -94.0 | 504990 | 71 | -102.0 | 504990 | 469 |
| MR_1774415559_A699B2CA | 504990 | 737 | -88.9 | 504990 | 753 | -95.8 | 504990 | 71 | -102.3 | 504990 | 469 |
| MR_1774415559_4BC7ED2D | 504990 | 737 | -90.3 | 504990 | 753 | -95.2 | 504990 | 71 | -100.3 | 504990 | 469 |

> *... 2개 열 생략 (전체 14열)*

---
