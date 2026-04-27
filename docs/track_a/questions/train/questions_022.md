# Track A 문제 분석 — train[210]~train[219]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[210] ~ train[219] (10개)

## 목차

1. [문제 210: `cc59771a-77b...`](#210) — single-answer, 정답: C22
2. [문제 211: `fc40e74f-b07...`](#211) — single-answer, 정답: C20
3. [문제 212: `6e87e84a-86e...`](#212) — multiple-answer, 정답: C11|C18
4. [문제 213: `61599f7f-542...`](#213) — single-answer, 정답: C3
5. [문제 214: `a926ffde-cf3...`](#214) — single-answer, 정답: C15
6. [문제 215: `e66dbb45-38e...`](#215) — single-answer, 정답: C18
7. [문제 216: `fabb6c1d-4ed...`](#216) — single-answer, 정답: C12
8. [문제 217: `068ed787-42c...`](#217) — single-answer, 정답: C3
9. [문제 218: `04d39e85-989...`](#218) — single-answer, 정답: C6
10. [문제 219: `174da1d3-415...`](#219) — multiple-answer, 정답: C4|C17

---

### 문제 210: `cc59771a-77b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cc59771a-77bd-49c0-86b7-ea7f88346f8e` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Add neighbor relationship between 3234864_2 and 3272429_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[210] topology](images/train_0210.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3272429_1
- `C2`: Increase transmission power for 3234864_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234864_2
- `C4`: Lift the tilt angle  of 3272429_1 by 5 degrees
- `C5`: Increase A3 Offset threshold for 3234864_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272429_1
- `C7`: Decrease transmission power for 3272429_1
- `C8`: Press down the tilt angle of 3234864_2 by 9 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272429_1
- `C10`: Decrease A3 Offset threshold for 3272429_1
- `C11`: Increase A3 Offset threshold for 3272429_1
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234864_2
- `C14`: Add neighbor relationship between 3264400_4 and 3272429_1
- `C15`: Decrease transmission power for 3234864_2
- `C16`: Check test server and transmission issues
- `C17`: Lift the tilt angle of 3234864_2 by 9 degrees
- `C18`: Adjust the azimuth of 3234864_2 by 50 degrees
- `C19`: Press down the tilt angle  of 3272429_1 by 5 degrees
- `C20`: Decrease A3 Offset threshold for 3234864_2
- `C21`: Adjust the azimuth of 3272429_1 by 46 degrees
- `C22`: Add neighbor relationship between 3234864_2 and 3272429_1 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.419 | MS1 | 121.4656589500 | 31.1446297538 | 670 | 504990 | -79.91 | 14.61 | 451.62 | 0.11 | 2.14 | 1590 |
| 2024-09-20 22:21:32.100 | MS1 | 121.4656592478 | 31.1446313479 | 670 | 504990 | -81.05 | 17.55 | 523.00 | 0.02 | 2.81 | 1577 |
| 2024-09-20 22:21:33.211 | MS1 | 121.4656656888 | 31.1446208349 | 670 | 504990 | -79.26 | 17.08 | 422.03 | 0.15 | 2.87 | 1598 |
| 2024-09-20 22:21:34.670 | MS1 | 121.4656613716 | 31.1446298273 | 670 | 504990 | -93.25 | -3.72 | 48.69 | 0.12 | 1.38 | 1600 |
| 2024-09-20 22:21:35.475 | MS1 | 121.4656765450 | 31.1446194698 | 670 | 504990 | -91.45 | -3.58 | 53.62 | 0.01 | 1.17 | 1567 |
| 2024-09-20 22:21:36.884 | MS1 | 121.4656738871 | 31.1446378915 | 670 | 504990 | -94.44 | -2.22 | 50.21 | 0.06 | 1.13 | 1574 |
| 2024-09-20 22:21:37.108 | MS1 | 121.4656684282 | 31.1446298111 | 670 | 504990 | -93.57 | -0.09 | 35.00 | 0.05 | 1.10 | 1585 |
| 2024-09-20 22:21:38.701 | MS1 | 121.4656626469 | 31.1446351235 | 670 | 504990 | -77.66 | 14.50 | 303.17 | 0.09 | 1.49 | 1589 |
| 2024-09-20 22:21:39.779 | MS1 | 121.4656596635 | 31.1446347383 | 670 | 504990 | -81.54 | 12.43 | 356.44 | 0.06 | 1.44 | 1565 |
| 2024-09-20 22:21:40.335 | MS1 | 121.4656756791 | 31.1446214383 | 670 | 504990 | -76.60 | 12.17 | 581.20 | 0.06 | 2.62 | 1589 |
| 2024-09-20 22:21:41.635 | MS1 | 121.4656588338 | 31.1446265790 | 670 | 504990 | -79.07 | 15.56 | 302.90 | 0.10 | 2.37 | 1598 |
| 2024-09-20 22:21:42.541 | MS1 | 121.4656749991 | 31.1446324458 | 670 | 504990 | -76.14 | 15.07 | 475.61 | 0.05 | 2.08 | 1565 |

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
| 3218126 | 3 | 121.4703563915 | 31.1487398165 | 331 | 1 | 0 | 39.1 | TDD | 461 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3234864 | 2 | 121.4683946382 | 31.1540657491 | 337 | 7 | 3 | 42.4 | TDD | 670 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3264400 | 4 | 121.4660581000 | 31.1511104858 | 3 | 11 | 12 | 29.7 | TDD | 509 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3272429 | 1 | 121.4646451894 | 31.1518762106 | 127 | 4 | 5 | 21.0 | TDD | 937 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.071 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.093 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.205 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.205 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.911 | NREventA3 | measId:2;ServCellPCI:492;Se... |
| 2024-09-20 22:21:35.911 | NREventA3 | measId:2;ServCellPCI:492;Se... |
| 2024-09-20 22:21:36.911 | NREventA3 | measId:2;ServCellPCI:492;Se... |
| 2024-09-20 22:21:39.411 | NRRRCReestablishAttempt | PCI:492 |
| 2024-09-20 22:21:39.425 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.438 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.577 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.577 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272429 | 1 | 10.9755 | 18.4971 | -116.8371 | 11.7787 | 141.1444 | 0.0126 | 0.0030 |
| 2024_09_20 22:00 | 3234864 | 2 | 16.8458 | 18.1120 | -114.9012 | 13.4059 | 135.3444 | 0.0018 | 0.1853 |
| 2024_09_20 22:00 | 3218126 | 3 | 6.6505 | 15.5025 | -116.4729 | 6.6312 | 196.3056 | 0.0079 | 0.0039 |
| 2024_09_20 22:00 | 3264400 | 4 | 8.6751 | 5.0651 | -116.6405 | 18.8501 | 147.4874 | 0.0142 | 0.0147 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415168_FBC9D133 | 504990 | 937 | -89.5 | 504990 | 670 | -91.8 | 504990 | 509 | -93.2 | 504990 | 461 |
| MR_1774415168_E6A76929 | 504990 | 937 | -88.3 | 504990 | 670 | -94.7 | 504990 | 509 | -92.8 | 504990 | 461 |
| MR_1774415168_9227A03E | 504990 | 937 | -89.9 | 504990 | 670 | -93.1 | 504990 | 509 | -95.7 | 504990 | 461 |
| MR_1774415168_7E51A2E2 | 504990 | 937 | -90.6 | 504990 | 670 | -93.6 | 504990 | 509 | -95.4 | 504990 | 461 |
| MR_1774415168_7AEA31AC | 504990 | 670 | -92.7 | 504990 | 937 | -87.7 | 504990 | 509 | -94.7 | 504990 | 461 |
| MR_1774415168_299856C2 | 504990 | 937 | -87.8 | 504990 | 670 | -92.3 | 504990 | 509 | -94.7 | 504990 | 461 |
| MR_1774415168_E58F2E52 | 504990 | 670 | -94.7 | 504990 | 937 | -88.9 | 504990 | 509 | -94.6 | 504990 | 461 |
| MR_1774415168_F7D7E51F | 504990 | 937 | -89.8 | 504990 | 670 | -93.8 | 504990 | 509 | -93.6 | 504990 | 461 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 211: `fc40e74f-b07...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fc40e74f-b072-4f35-ba2a-a50b397bd263` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[211] topology](images/train_0211.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3211112_3 and 3239318_1
- `C2`: Increase transmission power for 3211112_3
- `C3`: Press down the tilt angle  of 3239318_1 by 10 degrees
- `C4`: Decrease A3 Offset threshold for 3239318_1
- `C5`: Adjust the azimuth of 3239318_1 by 50 degrees
- `C6`: Press down the tilt angle of 3211112_3 by 10 degrees
- `C7`: Decrease transmission power for 3211112_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239318_1
- `C9`: Lift the tilt angle of 3211112_3 by 10 degrees
- `C10`: Decrease A3 Offset threshold for 3211112_3
- `C11`: Increase A3 Offset threshold for 3211112_3
- `C12`: Increase A3 Offset threshold for 3239318_1
- `C13`: Increase transmission power for 3239318_1
- `C14`: Add neighbor relationship between 3255346_4 and 3239318_1
- `C15`: Lift the tilt angle  of 3239318_1 by 10 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239318_1
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Adjust the azimuth of 3211112_3 by 50 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211112_3
- `C20`: Check test server and transmission issues **← 정답**
- `C21`: Decrease transmission power for 3239318_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211112_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.577 | MS1 | 121.4656765130 | 31.1446307193 | 579 | 504990 | -85.53 | 16.85 | 425.63 | 0.06 | 2.58 | 1578 |
| 2024-09-20 22:21:32.757 | MS1 | 121.4656767946 | 31.1446282784 | 579 | 504990 | -90.46 | 14.28 | 505.69 | 0.08 | 2.47 | 1563 |
| 2024-09-20 22:21:33.171 | MS1 | 121.4656713733 | 31.1446240033 | 579 | 504990 | -87.32 | 17.02 | 561.95 | 0.18 | 2.10 | 1573 |
| 2024-09-20 22:21:34.937 | MS1 | 121.4656682922 | 31.1446207472 | 579 | 504990 | -89.74 | 15.66 | 90.64 | 0.00 | 2.14 | 490 |
| 2024-09-20 22:21:35.920 | MS1 | 121.4656761837 | 31.1446201748 | 579 | 504990 | -87.62 | 15.99 | 103.21 | 0.16 | 2.09 | 332 |
| 2024-09-20 22:21:36.105 | MS1 | 121.4656755405 | 31.1446295473 | 579 | 504990 | -89.43 | 17.11 | 83.41 | 0.13 | 2.49 | 443 |
| 2024-09-20 22:21:37.514 | MS1 | 121.4656653994 | 31.1446357543 | 579 | 504990 | -92.87 | 10.56 | 69.76 | 0.10 | 2.20 | 431 |
| 2024-09-20 22:21:38.158 | MS1 | 121.4656740990 | 31.1446313259 | 579 | 504990 | -92.34 | 11.61 | 49.25 | 0.10 | 2.02 | 331 |
| 2024-09-20 22:21:39.148 | MS1 | 121.4656700692 | 31.1446292132 | 579 | 504990 | -90.72 | 7.63 | 75.03 | 0.16 | 2.91 | 321 |
| 2024-09-20 22:21:40.442 | MS1 | 121.4656652355 | 31.1446320481 | 579 | 504990 | -92.53 | 8.50 | 578.33 | 0.18 | 2.14 | 1592 |
| 2024-09-20 22:21:41.343 | MS1 | 121.4656702160 | 31.1446364431 | 579 | 504990 | -91.42 | 9.54 | 382.02 | 0.09 | 2.96 | 1582 |
| 2024-09-20 22:21:42.976 | MS1 | 121.4656723347 | 31.1446241583 | 579 | 504990 | -92.76 | 9.26 | 499.99 | 0.06 | 2.90 | 1579 |

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
| 3211112 | 3 | 121.4715962082 | 31.1446666933 | 7 | 9 | 2 | 39.5 | TDD | 579 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3225849 | 2 | 121.4692465620 | 31.1459999677 | 138 | 11 | 7 | 24.3 | TDD | 713 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3239318 | 1 | 121.4734818658 | 31.1506179861 | 47 | 15 | 5 | 22.8 | TDD | 976 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3255346 | 4 | 121.4653479494 | 31.1532533984 | 85 | 11 | 6 | 36.6 | TDD | 523 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.765 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.780 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.884 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.884 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.606 | NREventA3 | measId:2;ServCellPCI:752;Se... |
| 2024-09-20 22:21:37.846 | NRHandoverAttempt | SourcePCI:752;SourceNR-ARFC... |
| 2024-09-20 22:21:37.887 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.902 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.041 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.041 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239318 | 1 | 19.6963 | 12.2974 | -115.9277 | 13.3497 | 199.2673 | 0.0169 | 0.0173 |
| 2024_09_20 22:00 | 3225849 | 2 | 9.3239 | 13.6549 | -115.3908 | 9.5340 | 166.0336 | 0.0180 | 0.0039 |
| 2024_09_20 22:00 | 3211112 | 3 | 5.5799 | 8.4707 | -114.5982 | 17.9529 | 179.5480 | 0.0187 | 0.0073 |
| 2024_09_20 22:00 | 3255346 | 4 | 18.9760 | 19.6019 | -115.8474 | 19.1918 | 82.5209 | 0.0016 | 0.0029 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413604_51977CFD | 504990 | 579 | -87.8 | 504990 | 976 | -91.0 | 504990 | 523 | -96.0 | 504990 | 713 |
| MR_1774413604_456EB6EA | 504990 | 579 | -88.3 | 504990 | 976 | -94.3 | 504990 | 523 | -99.1 | 504990 | 713 |
| MR_1774413604_556F6936 | 504990 | 579 | -89.5 | 504990 | 976 | -92.1 | 504990 | 523 | -98.6 | 504990 | 713 |
| MR_1774413604_40D971C3 | 504990 | 579 | -90.7 | 504990 | 976 | -91.9 | 504990 | 523 | -96.6 | 504990 | 713 |
| MR_1774413604_7FE1485B | 504990 | 579 | -88.8 | 504990 | 976 | -91.7 | 504990 | 523 | -96.1 | 504990 | 713 |
| MR_1774413604_F0657EEC | 504990 | 579 | -88.6 | 504990 | 976 | -93.8 | 504990 | 523 | -96.2 | 504990 | 713 |
| MR_1774413604_51193340 | 504990 | 579 | -90.1 | 504990 | 976 | -91.0 | 504990 | 523 | -96.4 | 504990 | 713 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 212: `6e87e84a-86e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6e87e84a-86ec-4321-b08b-3406d8197d60` |
| Tag | **multiple-answer** |
| 정답 | **C11|C18** |
| C11 의미 | Adjust the azimuth of 3240672_1 by 50 degrees |
| C18 의미 | Increase transmission power for 3240672_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[212] topology](images/train_0212.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3276431_2 by 5 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276431_2
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276431_2
- `C5`: Add neighbor relationship between 3215570_3 and 3276431_2
- `C6`: Check test server and transmission issues
- `C7`: Increase A3 Offset threshold for 3276431_2
- `C8`: Adjust the azimuth of 3276431_2 by 16 degrees
- `C9`: Add neighbor relationship between 3240672_1 and 3276431_2
- `C10`: Lift the tilt angle  of 3276431_2 by 5 degrees
- `C11`: Adjust the azimuth of 3240672_1 by 50 degrees **← 정답**
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240672_1
- `C13`: Decrease transmission power for 3276431_2
- `C14`: Increase A3 Offset threshold for 3240672_1
- `C15`: Decrease A3 Offset threshold for 3240672_1
- `C16`: Increase transmission power for 3276431_2
- `C17`: Lift the tilt angle of 3240672_1 by 7 degrees
- `C18`: Increase transmission power for 3240672_1 **← 정답**
- `C19`: Decrease A3 Offset threshold for 3276431_2
- `C20`: Decrease transmission power for 3240672_1
- `C21`: Press down the tilt angle of 3240672_1 by 7 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240672_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.914 | MS1 | 121.4656666864 | 31.1446212102 | 801 | 504990 | -90.55 | 16.26 | 478.26 | 0.09 | 2.79 | 1570 |
| 2024-09-20 22:21:32.721 | MS1 | 121.4656690986 | 31.1446201517 | 801 | 504990 | -90.47 | 14.03 | 375.33 | 0.12 | 2.48 | 1583 |
| 2024-09-20 22:21:33.363 | MS1 | 121.4656744430 | 31.1446198449 | 801 | 504990 | -90.69 | 17.62 | 317.00 | 0.02 | 2.96 | 1571 |
| 2024-09-20 22:21:34.891 | MS1 | 121.4656618662 | 31.1446250783 | 801 | 504990 | -105.30 | 0.35 | 76.33 | 0.19 | 1.23 | 1565 |
| 2024-09-20 22:21:35.740 | MS1 | 121.4656666516 | 31.1446306253 | 801 | 504990 | -101.50 | -1.26 | 55.97 | 0.01 | 1.07 | 1585 |
| 2024-09-20 22:21:36.693 | MS1 | 121.4656701783 | 31.1446205782 | 801 | 504990 | -102.68 | -1.19 | 41.72 | 0.11 | 1.13 | 1561 |
| 2024-09-20 22:21:37.482 | MS1 | 121.4656631565 | 31.1446277967 | 801 | 504990 | -106.95 | 1.65 | 30.45 | 0.05 | 1.30 | 1566 |
| 2024-09-20 22:21:38.215 | MS1 | 121.4656626383 | 31.1446204819 | 801 | 504990 | -109.77 | 1.08 | 59.02 | 0.03 | 1.09 | 1573 |
| 2024-09-20 22:21:39.418 | MS1 | 121.4656676636 | 31.1446239599 | 801 | 504990 | -107.92 | -0.35 | 53.19 | 0.05 | 1.13 | 1598 |
| 2024-09-20 22:21:40.681 | MS1 | 121.4656639730 | 31.1446340235 | 801 | 504990 | -93.43 | 17.89 | 419.77 | 0.05 | 2.23 | 1579 |
| 2024-09-20 22:21:41.738 | MS1 | 121.4656628723 | 31.1446266674 | 801 | 504990 | -94.41 | 12.06 | 448.41 | 0.03 | 2.26 | 1575 |
| 2024-09-20 22:21:42.732 | MS1 | 121.4656666002 | 31.1446288445 | 801 | 504990 | -92.37 | 17.62 | 370.69 | 0.16 | 2.19 | 1577 |

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
| 3215570 | 3 | 121.4691497983 | 31.1458834405 | 46 | 11 | 2 | 37.2 | TDD | 534 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3240672 | 1 | 121.4739207511 | 31.1492746496 | 294 | 5 | 8 | 25.2 | TDD | 801 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3241709 | 4 | 121.4698329214 | 31.1469618943 | 180 | 12 | 3 | 26.1 | TDD | 135 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3276431 | 2 | 121.4653300001 | 31.1521425207 | 162 | 2 | 4 | 39.4 | TDD | 850 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.718 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.735 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.856 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.856 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.101 | NREventA2 | measId:1;ServCellPCI:721;Se... |
| 2024-09-20 22:21:34.203 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240672 | 1 | 5.8921 | 11.0191 | -117.5265 | 19.8077 | 162.9099 | 0.1925 | 0.0186 |
| 2024_09_20 22:00 | 3276431 | 2 | 8.7911 | 11.0982 | -117.8633 | 9.4219 | 123.7314 | 0.0121 | 0.0014 |
| 2024_09_20 22:00 | 3215570 | 3 | 13.1768 | 13.6260 | -114.5924 | 10.6537 | 198.9064 | 0.0025 | 0.0011 |
| 2024_09_20 22:00 | 3241709 | 4 | 5.3534 | 11.4838 | -114.4156 | 13.0514 | 105.7023 | 0.0137 | 0.0163 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414247_3655404A | 504990 | 801 | -106.4 | 504990 | 850 | -111.0 | 504990 | 534 | -115.5 | 504990 | 135 |
| MR_1774414247_A888EEDD | 504990 | 801 | -103.9 | 504990 | 850 | -109.9 | 504990 | 534 | -117.9 | 504990 | 135 |
| MR_1774414247_491D9F6D | 504990 | 801 | -104.2 | 504990 | 850 | -111.0 | 504990 | 534 | -118.7 | 504990 | 135 |
| MR_1774414247_D7A92179 | 504990 | 801 | -103.5 | 504990 | 850 | -113.3 | 504990 | 534 | -116.8 | 504990 | 135 |
| MR_1774414247_E89417EF | 504990 | 801 | -105.8 | 504990 | 850 | -113.2 | 504990 | 534 | -118.9 | 504990 | 135 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 213: `61599f7f-542...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `61599f7f-5421-4c00-81b7-f3e7bf58c28e` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234663_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[213] topology](images/train_0213.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3234663_5
- `C2`: Increase transmission power for 3234663_5
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234663_5 **← 정답**
- `C4`: Lift the tilt angle  of 3223632_1 by 6 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase transmission power for 3223632_1
- `C7`: Adjust the azimuth of 3223632_1 by 33 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223632_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223632_1
- `C10`: Adjust the azimuth of 3234663_5 by 32 degrees
- `C11`: Lift the tilt angle of 3234663_5 by 5 degrees
- `C12`: Press down the tilt angle of 3234663_5 by 5 degrees
- `C13`: Decrease A3 Offset threshold for 3223632_1
- `C14`: Decrease transmission power for 3234663_5
- `C15`: Increase A3 Offset threshold for 3223632_1
- `C16`: Add neighbor relationship between 3252876_11 and 3223632_1
- `C17`: Press down the tilt angle  of 3223632_1 by 6 degrees
- `C18`: Add neighbor relationship between 3234663_5 and 3223632_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234663_5
- `C20`: Decrease transmission power for 3223632_1
- `C21`: Increase A3 Offset threshold for 3234663_5
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.818 | MS1 | 121.4656776080 | 31.1446282471 | 187 | 504990 | -95.75 | 14.72 | 589.10 | 0.09 | 2.50 | 1566 |
| 2024-09-20 22:21:32.805 | MS1 | 121.4656698319 | 31.1446227347 | 447 | 504990 | -94.77 | 11.55 | 364.56 | 0.19 | 2.27 | 1565 |
| 2024-09-20 22:21:33.246 | MS1 | 121.4656664846 | 31.1446246845 | 629 | 504990 | -95.39 | 12.17 | 394.39 | 0.19 | 2.62 | 1581 |
| 2024-09-20 22:21:34.224 | MS1 | 121.4656612963 | 31.1446357205 | 133 | 152650 | -92.21 | 2.16 | 69.44 | 0.03 | 1.83 | 927 |
| 2024-09-20 22:21:35.172 | MS1 | 121.4656646241 | 31.1446213027 | 728 | 152650 | -92.64 | 7.76 | 97.56 | 0.18 | 1.62 | 938 |
| 2024-09-20 22:21:36.714 | MS1 | 121.4656650804 | 31.1446326730 | 380 | 152650 | -91.33 | 2.98 | 58.10 | 0.11 | 1.62 | 946 |
| 2024-09-20 22:21:37.614 | MS1 | 121.4656735694 | 31.1446285348 | 125 | 152650 | -94.23 | 4.72 | 68.12 | 0.18 | 1.99 | 997 |
| 2024-09-20 22:21:38.683 | MS1 | 121.4656590817 | 31.1446279260 | 133 | 152650 | -89.76 | 3.37 | 67.38 | 0.17 | 1.83 | 986 |
| 2024-09-20 22:21:39.936 | MS1 | 121.4656744515 | 31.1446375597 | 728 | 152650 | -95.81 | 3.03 | 46.12 | 0.04 | 1.65 | 903 |
| 2024-09-20 22:21:40.828 | MS1 | 121.4656738194 | 31.1446241291 | 380 | 152650 | -89.18 | 6.21 | 90.52 | 0.17 | 2.07 | 1581 |
| 2024-09-20 22:21:41.548 | MS1 | 121.4656593886 | 31.1446181295 | 125 | 152650 | -88.55 | 2.09 | 96.41 | 0.20 | 2.49 | 1573 |
| 2024-09-20 22:21:42.844 | MS1 | 121.4656622703 | 31.1446192534 | 133 | 152650 | -94.69 | 7.42 | 58.55 | 0.12 | 2.68 | 1584 |

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
| 3214658 | 13 | 121.4732530082 | 31.1443244832 | 104 | 13 | 9 | 21.7 | FDD | 31 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3223632 | 1 | 121.4744732469 | 31.1465342322 | 223 | 5 | 9 | 14.8 | TDD | 675 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3227137 | 12 | 121.4711702246 | 31.1552476432 | 220 | 14 | 10 | 28.2 | FDD | 125 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3228846 | 9 | 121.4710120261 | 31.1448611778 | 136 | 9 | 5 | 2.7 | FDD | 21 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3234477 | 4 | 121.4689222053 | 31.1471432442 | 217 | 4 | 4 | 19.7 | TDD | 629 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3234663 | 5 | 121.4689920076 | 31.1482079534 | 186 | 5 | 3 | 1.4 | TDD | 187 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3241644 | 2 | 121.4677302635 | 31.1500072962 | 15 | 10 | 5 | 13.0 | TDD | 998 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3242821 | 10 | 121.4751521643 | 31.1447906396 | 319 | 4 | 11 | 15.5 | FDD | 728 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3244867 | 6 | 121.4709453547 | 31.1491630471 | 34 | 2 | 9 | 13.2 | TDD | 447 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3246107 | 3 | 121.4665168177 | 31.1483011475 | 296 | 15 | 7 | 2.4 | TDD | 469 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3252876 | 11 | 121.4716071185 | 31.1556918088 | 295 | 10 | 8 | 12.9 | FDD | 380 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3259365 | 7 | 121.4746081508 | 31.1462713238 | 37 | 1 | 12 | 28.3 | FDD | 133 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3273979 | 8 | 121.4675737917 | 31.1492035861 | 337 | 8 | 12 | 5.5 | FDD | 669 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |

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
| 2024-09-20 22:21:31.215 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.237 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.358 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.358 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.089 | NREventA2 | measId:1;ServCellPCI:548;Se... |
| 2024-09-20 22:21:35.204 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.414 | NREventA5 | measId:3;ServCellPCI:548;Se... |
| 2024-09-20 22:21:35.470 | NRHandoverAttempt | SourcePCI:548;SourceNR-ARFC... |
| 2024-09-20 22:21:35.504 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.519 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.666 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.666 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223632 | 1 | 7.2814 | 8.3224 | -116.0210 | 19.0223 | 197.4036 | 0.0022 | 0.0036 |
| 2024_09_20 22:00 | 3241644 | 2 | 13.7695 | 18.9110 | -115.5052 | 13.9162 | 124.7743 | 0.0047 | 0.0083 |
| 2024_09_20 22:00 | 3246107 | 3 | 9.0201 | 6.4787 | -115.6232 | 13.0601 | 193.1631 | 0.0167 | 0.0106 |
| 2024_09_20 22:00 | 3234477 | 4 | 12.0895 | 10.6907 | -117.6302 | 8.7433 | 179.2261 | 0.0026 | 0.0014 |
| 2024_09_20 22:00 | 3234663 | 5 | 11.4496 | 18.0954 | -116.0451 | 16.8923 | 171.4305 | 0.0122 | 0.0109 |
| 2024_09_20 22:00 | 3244867 | 6 | 12.9102 | 10.1223 | -114.5562 | 6.4085 | 163.5023 | 0.0092 | 0.0144 |
| 2024_09_20 22:00 | 3259365 | 7 | 15.8505 | 13.3983 | -116.1821 | 4.4980 | 52.3169 | 0.0010 | 0.0121 |
| 2024_09_20 22:00 | 3273979 | 8 | 18.5481 | 5.9948 | -115.0161 | 3.0912 | 36.4826 | 0.0187 | 0.0179 |
| 2024_09_20 22:00 | 3228846 | 9 | 18.9257 | 7.0264 | -117.8095 | 3.6080 | 33.5994 | 0.0156 | 0.0026 |
| 2024_09_20 22:00 | 3242821 | 10 | 17.0160 | 8.3603 | -116.2150 | 3.8921 | 47.1913 | 0.0108 | 0.0096 |
| 2024_09_20 22:00 | 3252876 | 11 | 11.6297 | 9.4766 | -116.4700 | 4.2351 | 37.6481 | 0.0043 | 0.0015 |
| 2024_09_20 22:00 | 3227137 | 12 | 15.5948 | 13.2601 | -116.8400 | 3.3315 | 24.2730 | 0.0114 | 0.0167 |
| 2024_09_20 22:00 | 3214658 | 13 | 7.5509 | 15.6178 | -117.1793 | 4.5043 | 34.8499 | 0.0014 | 0.0134 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414341_989D3F92 | 152650 | 133 | -90.6 | 152650 | 31 | -98.3 | 152650 | 669 | -103.0 | 152650 | 21 |
| MR_1774414341_96E3EAF5 | 504990 | 629 | -96.1 | 504990 | 675 | -92.3 | 504990 | 469 | -100.5 | 504990 | 998 |
| MR_1774414341_E1D0E28E | 504990 | 629 | -96.7 | 504990 | 675 | -93.9 | 504990 | 469 | -101.2 | 504990 | 998 |
| MR_1774414341_14352559 | 504990 | 629 | -95.8 | 504990 | 675 | -90.5 | 504990 | 469 | -102.5 | 504990 | 998 |
| MR_1774414341_8F6B85D2 | 504990 | 629 | -97.3 | 504990 | 675 | -90.3 | 504990 | 469 | -100.9 | 504990 | 998 |
| MR_1774414341_38C614BB | 152650 | 133 | -90.9 | 152650 | 31 | -98.1 | 152650 | 669 | -104.4 | 152650 | 21 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 214: `a926ffde-cf3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a926ffde-cf3d-4216-be98-65e19fe48b99` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3226858_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[214] topology](images/train_0214.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3214148_2 and 3252804_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252804_4
- `C3`: Decrease A3 Offset threshold for 3226858_1
- `C4`: Increase transmission power for 3252804_4
- `C5`: Lift the tilt angle of 3226858_1 by 4 degrees
- `C6`: Increase A3 Offset threshold for 3226858_1
- `C7`: Lift the tilt angle  of 3252804_4 by 7 degrees
- `C8`: Check test server and transmission issues
- `C9`: Decrease transmission power for 3252804_4
- `C10`: Press down the tilt angle of 3226858_1 by 4 degrees
- `C11`: Press down the tilt angle  of 3252804_4 by 7 degrees
- `C12`: Increase A3 Offset threshold for 3252804_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226858_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226858_1 **← 정답**
- `C16`: Increase transmission power for 3226858_1
- `C17`: Adjust the azimuth of 3226858_1 by 9 degrees
- `C18`: Decrease transmission power for 3226858_1
- `C19`: Decrease A3 Offset threshold for 3252804_4
- `C20`: Adjust the azimuth of 3252804_4 by 50 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252804_4
- `C22`: Add neighbor relationship between 3226858_1 and 3252804_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.758 | MS1 | 121.4656717987 | 31.1446200162 | 176 | 504990 | -85.69 | 14.77 | 340.51 | 0.13 | 2.79 | 1589 |
| 2024-09-20 22:21:32.505 | MS1 | 121.4656758941 | 31.1446257965 | 176 | 504990 | -90.47 | 17.99 | 393.59 | 0.14 | 2.67 | 1580 |
| 2024-09-20 22:21:33.569 | MS1 | 121.4656595129 | 31.1446213355 | 176 | 504990 | -86.83 | 13.76 | 544.68 | 0.18 | 2.21 | 1587 |
| 2024-09-20 22:21:34.519 | MS1 | 121.4656759184 | 31.1446261202 | 176 | 504990 | -91.59 | 17.03 | 94.49 | 0.60 | 2.43 | 559 |
| 2024-09-20 22:21:35.276 | MS1 | 121.4656722548 | 31.1446345108 | 176 | 504990 | -87.25 | 15.26 | 58.87 | 0.55 | 2.35 | 683 |
| 2024-09-20 22:21:36.338 | MS1 | 121.4656716651 | 31.1446257683 | 176 | 504990 | -87.89 | 14.68 | 81.99 | 0.59 | 2.27 | 684 |
| 2024-09-20 22:21:37.642 | MS1 | 121.4656582264 | 31.1446241070 | 176 | 504990 | -91.88 | 9.38 | 59.77 | 0.58 | 2.08 | 527 |
| 2024-09-20 22:21:38.973 | MS1 | 121.4656702697 | 31.1446292801 | 176 | 504990 | -90.77 | 10.83 | 45.89 | 0.52 | 2.80 | 597 |
| 2024-09-20 22:21:39.208 | MS1 | 121.4656670373 | 31.1446367274 | 176 | 504990 | -90.87 | 7.98 | 93.54 | 0.62 | 2.05 | 575 |
| 2024-09-20 22:21:40.561 | MS1 | 121.4656675666 | 31.1446343321 | 176 | 504990 | -92.59 | 7.11 | 553.02 | 0.01 | 2.92 | 1584 |
| 2024-09-20 22:21:41.335 | MS1 | 121.4656777897 | 31.1446188708 | 176 | 504990 | -92.30 | 12.35 | 390.34 | 0.15 | 2.90 | 1563 |
| 2024-09-20 22:21:42.690 | MS1 | 121.4656692204 | 31.1446210693 | 176 | 504990 | -93.67 | 9.13 | 562.74 | 0.20 | 2.61 | 1563 |

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
| 3214148 | 2 | 121.4754367987 | 31.1543741010 | 153 | 5 | 2 | 33.3 | TDD | 784 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3226858 | 1 | 121.4740325126 | 31.1531214466 | 229 | 3 | 12 | 25.7 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3252804 | 4 | 121.4682919029 | 31.1446915776 | 64 | 2 | 6 | 21.7 | TDD | 855 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3279610 | 3 | 121.4640375286 | 31.1542194323 | 70 | 11 | 3 | 20.6 | TDD | 182 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.387 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.403 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.511 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.511 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.210 | NREventA3 | measId:2;ServCellPCI:676;Se... |
| 2024-09-20 22:21:38.450 | NRHandoverAttempt | SourcePCI:676;SourceNR-ARFC... |
| 2024-09-20 22:21:38.496 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.509 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.652 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.652 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226858 | 1 | 14.1532 | 14.9455 | -117.8700 | 11.4803 | 155.8238 | 0.0040 | 0.0101 |
| 2024_09_20 22:00 | 3214148 | 2 | 18.5482 | 11.8039 | -116.1910 | 5.7687 | 121.7997 | 0.0076 | 0.0189 |
| 2024_09_20 22:00 | 3279610 | 3 | 17.5067 | 9.6449 | -116.8253 | 13.3642 | 111.6707 | 0.0025 | 0.0094 |
| 2024_09_20 22:00 | 3252804 | 4 | 17.8667 | 9.5250 | -117.7303 | 11.4388 | 168.5778 | 0.0153 | 0.0031 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416828_DC591B54 | 504990 | 176 | -91.1 | 504990 | 855 | -92.6 | 504990 | 784 | -103.5 | 504990 | 182 |
| MR_1774416828_3FB64E6F | 504990 | 176 | -92.7 | 504990 | 855 | -96.5 | 504990 | 784 | -101.9 | 504990 | 182 |
| MR_1774416828_4041B1EB | 504990 | 176 | -92.8 | 504990 | 855 | -96.1 | 504990 | 784 | -102.6 | 504990 | 182 |
| MR_1774416828_1572B4A9 | 504990 | 176 | -93.1 | 504990 | 855 | -95.0 | 504990 | 784 | -103.4 | 504990 | 182 |
| MR_1774416828_AFD6CD61 | 504990 | 176 | -93.4 | 504990 | 855 | -94.7 | 504990 | 784 | -103.8 | 504990 | 182 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 215: `e66dbb45-38e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e66dbb45-38e7-440a-b173-124319e05954` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Lift the tilt angle  of 3221103_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[215] topology](images/train_0215.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3253947_1 by 5 degrees
- `C2`: Adjust the azimuth of 3221103_3 by 22 degrees
- `C3`: Adjust the azimuth of 3253947_1 by 5 degrees
- `C4`: Increase A3 Offset threshold for 3268200_2
- `C5`: Increase transmission power for 3268200_2
- `C6`: Add neighbor relationship between 3221103_3 and 3268200_2
- `C7`: Decrease A3 Offset threshold for 3268200_2
- `C8`: Check test server and transmission issues
- `C9`: Increase A3 Offset threshold for 3253947_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268200_2
- `C11`: Increase transmission power for 3253947_1
- `C12`: Lift the tilt angle of 3253947_1 by 5 degrees
- `C13`: Decrease transmission power for 3253947_1
- `C14`: Decrease A3 Offset threshold for 3253947_1
- `C15`: Press down the tilt angle  of 3221103_3 by 10 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253947_1
- `C17`: Decrease transmission power for 3268200_2
- `C18`: Lift the tilt angle  of 3221103_3 by 10 degrees **← 정답**
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Add neighbor relationship between 3253947_1 and 3268200_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268200_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253947_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.233 | MS1 | 121.4656765060 | 31.1446256657 | 800 | 504990 | -85.96 | 17.59 | 424.51 | 0.12 | 2.51 | 1577 |
| 2024-09-20 22:21:32.799 | MS1 | 121.4656605519 | 31.1446261557 | 800 | 504990 | -85.15 | 16.74 | 425.01 | 0.10 | 2.89 | 1572 |
| 2024-09-20 22:21:33.165 | MS1 | 121.4656724958 | 31.1446190366 | 800 | 504990 | -89.14 | 17.55 | 505.10 | 0.13 | 2.02 | 1571 |
| 2024-09-20 22:21:34.839 | MS1 | 121.4656640855 | 31.1446346957 | 800 | 504990 | -89.68 | 14.71 | 61.77 | 0.04 | 2.26 | 1586 |
| 2024-09-20 22:21:35.715 | MS1 | 121.4656583455 | 31.1446194851 | 800 | 504990 | -87.83 | 14.75 | 62.01 | 0.15 | 2.32 | 1573 |
| 2024-09-20 22:21:36.803 | MS1 | 121.4656655522 | 31.1446250964 | 800 | 504990 | -85.37 | 12.63 | 81.12 | 0.05 | 2.56 | 1590 |
| 2024-09-20 22:21:37.173 | MS1 | 121.4656591989 | 31.1446227242 | 800 | 504990 | -93.80 | 7.33 | 66.90 | 0.06 | 2.58 | 1568 |
| 2024-09-20 22:21:38.864 | MS1 | 121.4656612697 | 31.1446359701 | 800 | 504990 | -92.73 | 7.95 | 69.41 | 0.08 | 2.01 | 1579 |
| 2024-09-20 22:21:39.342 | MS1 | 121.4656761995 | 31.1446311339 | 800 | 504990 | -92.35 | 7.82 | 61.08 | 0.14 | 2.71 | 1574 |
| 2024-09-20 22:21:40.215 | MS1 | 121.4656696826 | 31.1446197538 | 800 | 504990 | -91.80 | 9.23 | 365.92 | 0.04 | 2.96 | 1586 |
| 2024-09-20 22:21:41.843 | MS1 | 121.4656650788 | 31.1446226433 | 800 | 504990 | -89.39 | 10.84 | 433.36 | 0.15 | 2.85 | 1589 |
| 2024-09-20 22:21:42.184 | MS1 | 121.4656700489 | 31.1446199145 | 800 | 504990 | -93.66 | 10.65 | 356.18 | 0.02 | 2.51 | 1571 |

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
| 3221103 | 3 | 121.4646227164 | 31.1549685979 | 228 | 8 | 3 | 23.4 | TDD | 940 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3253947 | 1 | 121.4759313447 | 31.1442870852 | 267 | 2 | 1 | 44.7 | TDD | 800 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3257774 | 4 | 121.4697181544 | 31.1485622460 | 243 | 9 | 9 | 37.9 | TDD | 492 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3268200 | 2 | 121.4736814856 | 31.1551532853 | 191 | 11 | 6 | 30.4 | TDD | 122 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.280 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.296 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.397 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.397 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.098 | NREventA3 | measId:2;ServCellPCI:63;Ser... |
| 2024-09-20 22:21:38.338 | NRHandoverAttempt | SourcePCI:63;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.373 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.386 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.500 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.500 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253947 | 1 | 89.8706 | 93.7644 | -115.6590 | 17.3964 | 161.2147 | 0.0070 | 0.0124 |
| 2024_09_20 22:00 | 3268200 | 2 | 18.4789 | 12.7981 | -117.5977 | 6.6589 | 104.2845 | 0.0137 | 0.0131 |
| 2024_09_20 22:00 | 3221103 | 3 | 19.8214 | 10.3124 | -116.7514 | 12.0266 | 190.4681 | 0.0080 | 0.0130 |
| 2024_09_20 22:00 | 3257774 | 4 | 19.5779 | 10.9991 | -116.8849 | 13.9360 | 102.1461 | 0.0181 | 0.0117 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414626_2A526DEC | 504990 | 800 | -89.0 | 504990 | 122 | -93.5 | 504990 | 940 | -102.2 | 504990 | 492 |
| MR_1774414626_7410F0EA | 504990 | 800 | -90.4 | 504990 | 122 | -89.8 | 504990 | 940 | -99.7 | 504990 | 492 |
| MR_1774414626_931A1BBE | 504990 | 800 | -89.3 | 504990 | 122 | -90.6 | 504990 | 940 | -100.2 | 504990 | 492 |
| MR_1774414626_334C6F12 | 504990 | 800 | -91.4 | 504990 | 122 | -91.7 | 504990 | 940 | -100.5 | 504990 | 492 |
| MR_1774414626_08D8C299 | 504990 | 800 | -87.8 | 504990 | 122 | -91.6 | 504990 | 940 | -101.0 | 504990 | 492 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 216: `fabb6c1d-4ed...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fabb6c1d-4ed4-4e30-bacd-d9b3f367388d` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3228443_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[216] topology](images/train_0216.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase A3 Offset threshold for 3274318_2
- `C3`: Press down the tilt angle of 3228443_4 by 4 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274318_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274318_2
- `C6`: Increase transmission power for 3228443_4
- `C7`: Add neighbor relationship between 3228443_4 and 3274318_2
- `C8`: Press down the tilt angle  of 3274318_2 by 5 degrees
- `C9`: Decrease transmission power for 3274318_2
- `C10`: Decrease transmission power for 3228443_4
- `C11`: Add neighbor relationship between 3249287_1 and 3274318_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228443_4 **← 정답**
- `C13`: Check test server and transmission issues
- `C14`: Adjust the azimuth of 3228443_4 by 7 degrees
- `C15`: Increase transmission power for 3274318_2
- `C16`: Adjust the azimuth of 3274318_2 by 50 degrees
- `C17`: Lift the tilt angle  of 3274318_2 by 5 degrees
- `C18`: Decrease A3 Offset threshold for 3274318_2
- `C19`: Decrease A3 Offset threshold for 3228443_4
- `C20`: Increase A3 Offset threshold for 3228443_4
- `C21`: Lift the tilt angle of 3228443_4 by 4 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228443_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.903 | MS1 | 121.4656644198 | 31.1446240865 | 949 | 504990 | -87.31 | 16.70 | 588.93 | 0.15 | 2.84 | 1600 |
| 2024-09-20 22:21:32.778 | MS1 | 121.4656684571 | 31.1446350847 | 949 | 504990 | -88.94 | 16.72 | 414.71 | 0.11 | 2.04 | 1565 |
| 2024-09-20 22:21:33.903 | MS1 | 121.4656644250 | 31.1446295147 | 949 | 504990 | -90.51 | 13.00 | 342.11 | 0.13 | 2.43 | 1579 |
| 2024-09-20 22:21:34.898 | MS1 | 121.4656654590 | 31.1446280517 | 949 | 504990 | -91.99 | 16.43 | 53.55 | 0.62 | 2.86 | 554 |
| 2024-09-20 22:21:35.707 | MS1 | 121.4656618023 | 31.1446345001 | 949 | 504990 | -89.82 | 13.75 | 66.07 | 0.67 | 2.62 | 513 |
| 2024-09-20 22:21:36.186 | MS1 | 121.4656756568 | 31.1446323830 | 949 | 504990 | -91.36 | 16.52 | 97.23 | 0.61 | 2.72 | 586 |
| 2024-09-20 22:21:37.641 | MS1 | 121.4656681542 | 31.1446352245 | 949 | 504990 | -91.04 | 10.51 | 84.51 | 0.65 | 2.71 | 500 |
| 2024-09-20 22:21:38.585 | MS1 | 121.4656713398 | 31.1446200608 | 949 | 504990 | -89.60 | 11.90 | 93.25 | 0.59 | 2.77 | 629 |
| 2024-09-20 22:21:39.740 | MS1 | 121.4656748359 | 31.1446230813 | 949 | 504990 | -89.87 | 10.21 | 60.51 | 0.67 | 2.29 | 515 |
| 2024-09-20 22:21:40.879 | MS1 | 121.4656602343 | 31.1446316050 | 949 | 504990 | -90.98 | 11.14 | 511.18 | 0.20 | 2.39 | 1569 |
| 2024-09-20 22:21:41.513 | MS1 | 121.4656711431 | 31.1446182879 | 949 | 504990 | -89.05 | 12.65 | 312.24 | 0.08 | 2.24 | 1590 |
| 2024-09-20 22:21:42.688 | MS1 | 121.4656696803 | 31.1446232329 | 949 | 504990 | -90.10 | 11.79 | 441.36 | 0.03 | 2.71 | 1577 |

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
| 3221826 | 3 | 121.4748679178 | 31.1467862031 | 97 | 5 | 11 | 49.0 | TDD | 875 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3228443 | 4 | 121.4747458217 | 31.1476114820 | 256 | 1 | 6 | 42.4 | TDD | 949 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3249287 | 1 | 121.4713360346 | 31.1480421945 | 306 | 15 | 5 | 16.7 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3274318 | 2 | 121.4661268733 | 31.1555225370 | 87 | 3 | 1 | 44.1 | TDD | 819 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.768 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.792 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.929 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.929 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.649 | NREventA3 | measId:2;ServCellPCI:706;Se... |
| 2024-09-20 22:21:37.889 | NRHandoverAttempt | SourcePCI:706;SourceNR-ARFC... |
| 2024-09-20 22:21:37.922 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.936 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.078 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.078 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249287 | 1 | 5.1053 | 9.7216 | -115.0204 | 11.6008 | 199.6066 | 0.0124 | 0.0142 |
| 2024_09_20 22:00 | 3274318 | 2 | 13.1240 | 5.3200 | -117.0458 | 14.7695 | 177.7297 | 0.0179 | 0.0013 |
| 2024_09_20 22:00 | 3221826 | 3 | 10.2476 | 12.0492 | -117.6056 | 9.7741 | 179.8409 | 0.0169 | 0.0137 |
| 2024_09_20 22:00 | 3228443 | 4 | 13.9422 | 10.6196 | -114.9219 | 19.2599 | 105.5730 | 0.0134 | 0.0145 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412293_2D572D12 | 504990 | 949 | -90.6 | 504990 | 819 | -97.8 | 504990 | 248 | -101.3 | 504990 | 875 |
| MR_1774412293_2DBD5F1A | 504990 | 949 | -93.3 | 504990 | 819 | -100.9 | 504990 | 248 | -99.7 | 504990 | 875 |
| MR_1774412293_0759BEC3 | 504990 | 949 | -91.0 | 504990 | 819 | -99.9 | 504990 | 248 | -99.8 | 504990 | 875 |
| MR_1774412293_6312A8BE | 504990 | 949 | -92.2 | 504990 | 819 | -98.0 | 504990 | 248 | -99.4 | 504990 | 875 |
| MR_1774412293_0E0C3CFD | 504990 | 949 | -91.5 | 504990 | 819 | -101.3 | 504990 | 248 | -101.5 | 504990 | 875 |
| MR_1774412293_C8AE568A | 504990 | 949 | -91.0 | 504990 | 819 | -98.4 | 504990 | 248 | -102.1 | 504990 | 875 |
| MR_1774412293_3E121D83 | 504990 | 949 | -92.9 | 504990 | 819 | -99.3 | 504990 | 248 | -100.9 | 504990 | 875 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 217: `068ed787-42c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `068ed787-42cb-4c03-8930-b89b25f649d0` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[217] topology](images/train_0217.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277617_1
- `C2`: Press down the tilt angle of 3277617_1 by 10 degrees
- `C3`: Insufficient data; more data is needed for judgment. **← 정답**
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245944_3
- `C5`: Decrease transmission power for 3245944_3
- `C6`: Increase transmission power for 3245944_3
- `C7`: Decrease A3 Offset threshold for 3245944_3
- `C8`: Decrease A3 Offset threshold for 3277617_1
- `C9`: Increase A3 Offset threshold for 3245944_3
- `C10`: Decrease transmission power for 3277617_1
- `C11`: Add neighbor relationship between 3230690_2 and 3245944_3
- `C12`: Press down the tilt angle  of 3245944_3 by 10 degrees
- `C13`: Check test server and transmission issues
- `C14`: Lift the tilt angle  of 3245944_3 by 10 degrees
- `C15`: Increase transmission power for 3277617_1
- `C16`: Adjust the azimuth of 3245944_3 by 50 degrees
- `C17`: Increase A3 Offset threshold for 3277617_1
- `C18`: Adjust the azimuth of 3277617_1 by 50 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245944_3
- `C20`: Add neighbor relationship between 3277617_1 and 3245944_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277617_1
- `C22`: Lift the tilt angle of 3277617_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.351 | MS1 | 121.4656616432 | 31.1446312130 | 240 | 504990 | -89.07 | 13.27 | 495.15 | 0.11 | 2.94 | 1585 |
| 2024-09-20 22:21:32.752 | MS1 | 121.4656668040 | 31.1446292754 | 240 | 504990 | -91.88 | 17.28 | 311.90 | 0.02 | 2.91 | 1587 |
| 2024-09-20 22:21:33.466 | MS1 | 121.4656649868 | 31.1446313899 | 240 | 504990 | -90.62 | 17.70 | 555.79 | 0.12 | 2.72 | 1566 |
| 2024-09-20 22:21:34.892 | MS1 | 121.4656588142 | 31.1446379004 | 240 | 504990 | -87.09 | 15.49 | 90.60 | 0.11 | 2.38 | 1583 |
| 2024-09-20 22:21:35.549 | MS1 | 121.4656727788 | 31.1446250863 | 240 | 504990 | -88.48 | 15.88 | 81.05 | 0.01 | 2.14 | 1562 |
| 2024-09-20 22:21:36.144 | MS1 | 121.4656622016 | 31.1446368094 | 240 | 504990 | -85.54 | 15.87 | 84.70 | 0.17 | 2.73 | 1565 |
| 2024-09-20 22:21:37.836 | MS1 | 121.4656686609 | 31.1446299656 | 240 | 504990 | -89.93 | 12.41 | 55.34 | 0.02 | 2.77 | 1592 |
| 2024-09-20 22:21:38.634 | MS1 | 121.4656581973 | 31.1446304346 | 240 | 504990 | -89.91 | 10.38 | 85.76 | 0.05 | 2.72 | 1583 |
| 2024-09-20 22:21:39.227 | MS1 | 121.4656688779 | 31.1446360393 | 240 | 504990 | -92.28 | 11.35 | 68.09 | 0.09 | 2.29 | 1599 |
| 2024-09-20 22:21:40.877 | MS1 | 121.4656629435 | 31.1446273558 | 240 | 504990 | -90.25 | 12.52 | 582.65 | 0.01 | 2.42 | 1598 |
| 2024-09-20 22:21:41.757 | MS1 | 121.4656589818 | 31.1446208190 | 240 | 504990 | -91.17 | 7.45 | 471.69 | 0.09 | 2.11 | 1590 |
| 2024-09-20 22:21:42.389 | MS1 | 121.4656587403 | 31.1446357218 | 240 | 504990 | -92.39 | 7.45 | 481.36 | 0.04 | 2.85 | 1578 |

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
| 3230690 | 2 | 121.4748198333 | 31.1505802815 | 270 | 10 | 11 | 44.1 | TDD | 370 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3245944 | 3 | 121.4643837395 | 31.1536964337 | 2 | 15 | 8 | 29.2 | TDD | 627 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3257571 | 4 | 121.4684861112 | 31.1502531483 | 134 | 10 | 7 | 46.2 | TDD | 655 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3277617 | 1 | 121.4645482150 | 31.1441290506 | 186 | 0 | 7 | 48.5 | TDD | 240 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.509 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.529 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.634 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.634 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.351 | NREventA3 | measId:2;ServCellPCI:148;Se... |
| 2024-09-20 22:21:38.591 | NRHandoverAttempt | SourcePCI:148;SourceNR-ARFC... |
| 2024-09-20 22:21:38.623 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.635 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.768 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.768 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3277617 | 1 | 81.4138 | 84.0876 | -115.6029 | 7.0419 | 170.4202 | 0.0186 | 0.0150 |
| 2024_09_19 22:00 | 3230690 | 2 | 76.3647 | 88.2714 | -116.9655 | 6.9353 | 196.0179 | 0.0083 | 0.0006 |
| 2024_09_19 22:00 | 3245944 | 3 | 88.0525 | 91.8054 | -116.5814 | 10.2051 | 167.4806 | 0.0102 | 0.0023 |
| 2024_09_19 22:00 | 3257571 | 4 | 82.5726 | 92.6117 | -115.2079 | 8.5256 | 154.7340 | 0.0158 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412483_967E4AAB | 504990 | 240 | -88.4 | 504990 | 627 | -95.2 | 504990 | 370 | -97.7 | 504990 | 655 |
| MR_1774412483_CC0A9079 | 504990 | 240 | -86.3 | 504990 | 627 | -93.3 | 504990 | 370 | -96.9 | 504990 | 655 |
| MR_1774412483_0389CA6F | 504990 | 240 | -87.2 | 504990 | 627 | -95.2 | 504990 | 370 | -98.5 | 504990 | 655 |
| MR_1774412483_796EA27E | 504990 | 240 | -88.2 | 504990 | 627 | -95.3 | 504990 | 370 | -98.8 | 504990 | 655 |
| MR_1774412483_FAAFAEA8 | 504990 | 240 | -88.0 | 504990 | 627 | -96.5 | 504990 | 370 | -96.5 | 504990 | 655 |
| MR_1774412483_ABA870DC | 504990 | 240 | -88.1 | 504990 | 627 | -93.8 | 504990 | 370 | -96.8 | 504990 | 655 |
| MR_1774412483_FDEA13F9 | 504990 | 240 | -86.4 | 504990 | 627 | -94.4 | 504990 | 370 | -96.3 | 504990 | 655 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 218: `04d39e85-989...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `04d39e85-989e-4777-80d1-0c8fb6982f50` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262413_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[218] topology](images/train_0218.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3262648_5
- `C2`: Increase A3 Offset threshold for 3262413_4
- `C3`: Add neighbor relationship between 3262413_4 and 3262648_5
- `C4`: Increase A3 Offset threshold for 3262648_5
- `C5`: Press down the tilt angle  of 3262648_5 by 5 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262413_4 **← 정답**
- `C7`: Decrease A3 Offset threshold for 3262413_4
- `C8`: Decrease A3 Offset threshold for 3262648_5
- `C9`: Adjust the azimuth of 3262648_5 by 8 degrees
- `C10`: Add neighbor relationship between 3272419_12 and 3262648_5
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262648_5
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262648_5
- `C13`: Lift the tilt angle of 3262413_4 by 2 degrees
- `C14`: Adjust the azimuth of 3262413_4 by 10 degrees
- `C15`: Decrease transmission power for 3262413_4
- `C16`: Decrease transmission power for 3262648_5
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262413_4
- `C18`: Press down the tilt angle of 3262413_4 by 2 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Lift the tilt angle  of 3262648_5 by 5 degrees
- `C21`: Check test server and transmission issues
- `C22`: Increase transmission power for 3262413_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.375 | MS1 | 121.4656588526 | 31.1446361419 | 684 | 504990 | -95.95 | 12.33 | 490.49 | 0.03 | 2.86 | 1570 |
| 2024-09-20 22:21:32.206 | MS1 | 121.4656629956 | 31.1446193403 | 200 | 504990 | -94.11 | 13.28 | 380.58 | 0.07 | 2.48 | 1590 |
| 2024-09-20 22:21:33.430 | MS1 | 121.4656620695 | 31.1446271931 | 393 | 504990 | -95.87 | 12.54 | 574.07 | 0.14 | 2.47 | 1595 |
| 2024-09-20 22:21:34.993 | MS1 | 121.4656709064 | 31.1446303430 | 935 | 152650 | -91.07 | 5.16 | 73.73 | 0.07 | 1.69 | 946 |
| 2024-09-20 22:21:35.947 | MS1 | 121.4656765345 | 31.1446343708 | 998 | 152650 | -92.20 | 7.18 | 100.48 | 0.07 | 1.65 | 931 |
| 2024-09-20 22:21:36.258 | MS1 | 121.4656745095 | 31.1446332809 | 790 | 152650 | -92.20 | 7.14 | 86.23 | 0.19 | 1.89 | 999 |
| 2024-09-20 22:21:37.228 | MS1 | 121.4656609297 | 31.1446317871 | 93 | 152650 | -87.81 | 3.41 | 101.29 | 0.12 | 1.68 | 924 |
| 2024-09-20 22:21:38.628 | MS1 | 121.4656670679 | 31.1446360883 | 935 | 152650 | -87.51 | 4.69 | 106.96 | 0.17 | 1.55 | 940 |
| 2024-09-20 22:21:39.864 | MS1 | 121.4656769262 | 31.1446329260 | 998 | 152650 | -90.56 | 5.54 | 60.69 | 0.11 | 1.73 | 910 |
| 2024-09-20 22:21:40.313 | MS1 | 121.4656678017 | 31.1446295591 | 790 | 152650 | -90.69 | 5.89 | 57.96 | 0.06 | 2.73 | 1577 |
| 2024-09-20 22:21:41.375 | MS1 | 121.4656697070 | 31.1446360819 | 93 | 152650 | -91.21 | 2.46 | 83.01 | 0.03 | 2.11 | 1564 |
| 2024-09-20 22:21:42.525 | MS1 | 121.4656603864 | 31.1446326732 | 935 | 152650 | -87.02 | 5.22 | 91.21 | 0.03 | 2.04 | 1560 |

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
| 3211782 | 9 | 121.4757352238 | 31.1444276526 | 136 | 6 | 3 | 1.3 | FDD | 935 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3220723 | 8 | 121.4647487655 | 31.1538874703 | 255 | 5 | 7 | 8.7 | FDD | 998 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3224477 | 3 | 121.4728463766 | 31.1478894050 | 4 | 3 | 1 | 4.9 | TDD | 393 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3235395 | 10 | 121.4676850650 | 31.1531993841 | 293 | 1 | 1 | 0.6 | FDD | 815 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3240789 | 11 | 121.4757951347 | 31.1464756840 | 119 | 15 | 8 | 5.0 | FDD | 369 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3250707 | 6 | 121.4670338431 | 31.1528185255 | 317 | 7 | 2 | 20.1 | TDD | 154 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3262413 | 4 | 121.4712570394 | 31.1453851046 | 251 | 1 | 10 | 11.9 | TDD | 684 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3262648 | 5 | 121.4678088327 | 31.1451668268 | 262 | 0 | 7 | 17.3 | TDD | 77 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3268523 | 7 | 121.4747273953 | 31.1450290298 | 146 | 14 | 8 | 13.0 | FDD | 132 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3269059 | 1 | 121.4689827160 | 31.1558635485 | 203 | 15 | 8 | 7.0 | TDD | 930 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3271549 | 13 | 121.4723530511 | 31.1539001665 | 32 | 3 | 3 | 28.7 | FDD | 93 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3272419 | 12 | 121.4697589117 | 31.1483240860 | 270 | 12 | 7 | 29.7 | FDD | 790 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3275734 | 2 | 121.4656882652 | 31.1554247243 | 102 | 4 | 1 | 28.1 | TDD | 200 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.561 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.582 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.710 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.710 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.412 | NREventA2 | measId:1;ServCellPCI:52;Ser... |
| 2024-09-20 22:21:35.539 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.764 | NREventA5 | measId:3;ServCellPCI:52;Ser... |
| 2024-09-20 22:21:35.820 | NRHandoverAttempt | SourcePCI:52;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.862 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.876 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.019 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.019 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269059 | 1 | 13.9224 | 17.4288 | -116.8704 | 19.0294 | 154.0043 | 0.0133 | 0.0130 |
| 2024_09_20 22:00 | 3275734 | 2 | 9.8796 | 19.5852 | -114.4577 | 7.8861 | 121.4570 | 0.0180 | 0.0097 |
| 2024_09_20 22:00 | 3224477 | 3 | 9.8466 | 19.8232 | -116.6438 | 9.0470 | 88.8896 | 0.0133 | 0.0107 |
| 2024_09_20 22:00 | 3262413 | 4 | 10.3508 | 8.2064 | -115.4717 | 9.9832 | 138.5805 | 0.0091 | 0.0026 |
| 2024_09_20 22:00 | 3262648 | 5 | 14.9926 | 16.3160 | -117.2398 | 16.3471 | 179.4833 | 0.0042 | 0.0067 |
| 2024_09_20 22:00 | 3250707 | 6 | 14.0050 | 16.1516 | -115.1789 | 14.2168 | 164.0622 | 0.0073 | 0.0039 |
| 2024_09_20 22:00 | 3268523 | 7 | 5.0594 | 10.2160 | -114.5261 | 4.9568 | 54.1793 | 0.0015 | 0.0191 |
| 2024_09_20 22:00 | 3220723 | 8 | 10.3384 | 19.1427 | -115.8650 | 3.6442 | 51.7379 | 0.0170 | 0.0196 |
| 2024_09_20 22:00 | 3211782 | 9 | 15.8577 | 13.9622 | -115.4991 | 3.1823 | 30.5799 | 0.0068 | 0.0047 |
| 2024_09_20 22:00 | 3235395 | 10 | 17.7124 | 7.3092 | -115.7571 | 4.3143 | 46.3338 | 0.0090 | 0.0097 |
| 2024_09_20 22:00 | 3240789 | 11 | 19.7662 | 5.1664 | -114.5339 | 4.3452 | 29.0846 | 0.0178 | 0.0045 |
| 2024_09_20 22:00 | 3272419 | 12 | 18.0026 | 19.9866 | -115.5386 | 3.1901 | 30.4101 | 0.0109 | 0.0100 |
| 2024_09_20 22:00 | 3271549 | 13 | 15.7740 | 12.8938 | -115.7676 | 4.7540 | 32.8146 | 0.0113 | 0.0192 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414742_8D9F763C | 504990 | 393 | -94.1 | 504990 | 77 | -90.2 | 504990 | 154 | -101.1 | 504990 | 930 |
| MR_1774414742_DC1A88DB | 504990 | 393 | -95.5 | 504990 | 77 | -91.2 | 504990 | 154 | -101.0 | 504990 | 930 |
| MR_1774414742_6DAD8FF2 | 152650 | 935 | -90.2 | 152650 | 369 | -98.8 | 152650 | 815 | -97.9 | 152650 | 132 |
| MR_1774414742_5443D049 | 152650 | 935 | -91.7 | 152650 | 369 | -97.2 | 152650 | 815 | -99.2 | 152650 | 132 |
| MR_1774414742_12400DE9 | 504990 | 393 | -97.1 | 504990 | 77 | -90.5 | 504990 | 154 | -102.6 | 504990 | 930 |
| MR_1774414742_5FB3AEDE | 152650 | 935 | -91.0 | 152650 | 369 | -99.9 | 152650 | 815 | -97.7 | 152650 | 132 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 219: `174da1d3-415...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `174da1d3-415b-4a99-b987-157e1d0d361d` |
| Tag | **multiple-answer** |
| 정답 | **C4|C17** |
| C4 의미 | Increase transmission power for 3254475_2 |
| C17 의미 | Adjust the azimuth of 3254475_2 by 17 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[219] topology](images/train_0219.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3254475_2
- `C2`: Add neighbor relationship between 3258897_4 and 3265422_1
- `C3`: Increase A3 Offset threshold for 3254475_2
- `C4`: Increase transmission power for 3254475_2 **← 정답**
- `C5`: Decrease A3 Offset threshold for 3265422_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254475_2
- `C7`: Lift the tilt angle  of 3265422_1 by 4 degrees
- `C8`: Adjust the azimuth of 3265422_1 by 36 degrees
- `C9`: Decrease transmission power for 3265422_1
- `C10`: Check test server and transmission issues
- `C11`: Add neighbor relationship between 3254475_2 and 3265422_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265422_1
- `C13`: Increase transmission power for 3265422_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase A3 Offset threshold for 3265422_1
- `C16`: Decrease A3 Offset threshold for 3254475_2
- `C17`: Adjust the azimuth of 3254475_2 by 17 degrees **← 정답**
- `C18`: Press down the tilt angle  of 3265422_1 by 4 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254475_2
- `C20`: Press down the tilt angle of 3254475_2 by 10 degrees
- `C21`: Lift the tilt angle of 3254475_2 by 10 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265422_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.754 | MS1 | 121.4656600978 | 31.1446365822 | 18 | 504990 | -86.67 | 17.44 | 297.54 | 0.16 | 2.14 | 1564 |
| 2024-09-20 22:21:32.172 | MS1 | 121.4656720638 | 31.1446278197 | 18 | 504990 | -93.99 | 14.15 | 318.72 | 0.13 | 2.55 | 1589 |
| 2024-09-20 22:21:33.389 | MS1 | 121.4656595548 | 31.1446201385 | 18 | 504990 | -94.12 | 17.57 | 350.74 | 0.13 | 2.65 | 1564 |
| 2024-09-20 22:21:34.457 | MS1 | 121.4656682867 | 31.1446201592 | 18 | 504990 | -106.74 | -0.73 | 40.53 | 0.05 | 1.48 | 1572 |
| 2024-09-20 22:21:35.165 | MS1 | 121.4656613857 | 31.1446358884 | 18 | 504990 | -100.56 | 1.57 | 76.66 | 0.09 | 1.15 | 1582 |
| 2024-09-20 22:21:36.824 | MS1 | 121.4656667904 | 31.1446312557 | 18 | 504990 | -101.53 | -0.24 | 26.97 | 0.10 | 1.35 | 1598 |
| 2024-09-20 22:21:37.591 | MS1 | 121.4656598929 | 31.1446257741 | 18 | 504990 | -109.40 | 1.04 | 55.03 | 0.05 | 1.40 | 1563 |
| 2024-09-20 22:21:38.840 | MS1 | 121.4656621509 | 31.1446354450 | 18 | 504990 | -102.24 | -0.93 | 86.64 | 0.12 | 1.12 | 1563 |
| 2024-09-20 22:21:39.745 | MS1 | 121.4656655032 | 31.1446290480 | 18 | 504990 | -102.74 | 0.26 | 47.11 | 0.09 | 1.01 | 1562 |
| 2024-09-20 22:21:40.493 | MS1 | 121.4656582928 | 31.1446198191 | 18 | 504990 | -88.70 | 14.99 | 351.78 | 0.12 | 2.67 | 1560 |
| 2024-09-20 22:21:41.925 | MS1 | 121.4656582037 | 31.1446308631 | 18 | 504990 | -85.52 | 13.10 | 558.86 | 0.20 | 2.74 | 1571 |
| 2024-09-20 22:21:42.202 | MS1 | 121.4656751107 | 31.1446282892 | 18 | 504990 | -90.14 | 17.36 | 321.55 | 0.02 | 2.91 | 1572 |

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
| 3254475 | 2 | 121.4747002260 | 31.1496715699 | 220 | 14 | 2 | 38.0 | TDD | 18 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3258897 | 4 | 121.4671114384 | 31.1449962169 | 153 | 12 | 2 | 44.9 | TDD | 133 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3265422 | 1 | 121.4650831684 | 31.1476960520 | 135 | 1 | 8 | 16.1 | TDD | 771 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3270597 | 3 | 121.4750386407 | 31.1530675992 | 309 | 14 | 6 | 38.4 | TDD | 547 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.870 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.889 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.996 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.996 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.266 | NREventA2 | measId:1;ServCellPCI:747;Se... |
| 2024-09-20 22:21:34.377 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265422 | 1 | 8.2210 | 6.6571 | -115.0436 | 11.8184 | 113.2561 | 0.0033 | 0.0132 |
| 2024_09_20 22:00 | 3254475 | 2 | 8.3743 | 18.5198 | -114.1479 | 6.7167 | 108.6140 | 0.1618 | 0.0019 |
| 2024_09_20 22:00 | 3270597 | 3 | 5.6839 | 12.0731 | -116.8515 | 6.6564 | 197.3845 | 0.0089 | 0.0128 |
| 2024_09_20 22:00 | 3258897 | 4 | 18.6661 | 10.7788 | -115.9371 | 8.9633 | 183.0096 | 0.0114 | 0.0118 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414092_11EC16B1 | 504990 | 18 | -107.8 | 504990 | 771 | -109.0 | 504990 | 133 | -119.2 | 504990 | 547 |
| MR_1774414092_13F7F00B | 504990 | 18 | -105.9 | 504990 | 771 | -111.6 | 504990 | 133 | -119.6 | 504990 | 547 |
| MR_1774414092_5461726E | 504990 | 18 | -106.7 | 504990 | 771 | -112.2 | 504990 | 133 | -118.3 | 504990 | 547 |
| MR_1774414092_F89F8D00 | 504990 | 18 | -106.9 | 504990 | 771 | -110.4 | 504990 | 133 | -117.3 | 504990 | 547 |
| MR_1774414092_DDBCEE3B | 504990 | 18 | -108.5 | 504990 | 771 | -109.0 | 504990 | 133 | -116.5 | 504990 | 547 |
| MR_1774414092_5FE3E8E3 | 504990 | 18 | -107.9 | 504990 | 771 | -110.1 | 504990 | 133 | -119.2 | 504990 | 547 |
| MR_1774414092_F63DD1B7 | 504990 | 18 | -107.3 | 504990 | 771 | -110.2 | 504990 | 133 | -117.9 | 504990 | 547 |

> *... 2개 열 생략 (전체 14열)*

---
