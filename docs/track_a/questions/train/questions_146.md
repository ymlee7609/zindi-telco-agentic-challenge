# Track A 문제 분석 — train[1450]~train[1459]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1450] ~ train[1459] (10개)

## 목차

1. [문제 1450: `0047be8e-a4f...`](#1450) — single-answer, 정답: C22
2. [문제 1451: `2b9464bb-cc7...`](#1451) — single-answer, 정답: C6
3. [문제 1452: `ae308d79-212...`](#1452) — single-answer, 정답: C20
4. [문제 1453: `b15d305f-1d6...`](#1453) — single-answer, 정답: C12
5. [문제 1454: `cdddeb05-4d2...`](#1454) — single-answer, 정답: C20
6. [문제 1455: `cadf587f-71e...`](#1455) — single-answer, 정답: C11
7. [문제 1456: `0432698f-72f...`](#1456) — single-answer, 정답: C3
8. [문제 1457: `232801e5-f03...`](#1457) — single-answer, 정답: C6
9. [문제 1458: `472c772e-28e...`](#1458) — single-answer, 정답: C1
10. [문제 1459: `e879367f-ffd...`](#1459) — single-answer, 정답: C2

---

### 문제 1450: `0047be8e-a4f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0047be8e-a4f9-4872-9f34-364b5967a692` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Add neighbor relationship between 3237345_3 and 3251195_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1450] topology](images/train_1450.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3251195_4
- `C2`: Adjust the azimuth of 3237345_3 by 8 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237345_3
- `C4`: Decrease A3 Offset threshold for 3251195_4
- `C5`: Decrease A3 Offset threshold for 3237345_3
- `C6`: Adjust the azimuth of 3251195_4 by 11 degrees
- `C7`: Decrease transmission power for 3251195_4
- `C8`: Press down the tilt angle of 3237345_3 by 10 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251195_4
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase A3 Offset threshold for 3237345_3
- `C12`: Increase A3 Offset threshold for 3251195_4
- `C13`: Add neighbor relationship between 3231759_1 and 3251195_4
- `C14`: Decrease transmission power for 3237345_3
- `C15`: Press down the tilt angle  of 3251195_4 by 5 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251195_4
- `C17`: Lift the tilt angle  of 3251195_4 by 5 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237345_3
- `C19`: Lift the tilt angle of 3237345_3 by 10 degrees
- `C20`: Increase transmission power for 3237345_3
- `C21`: Check test server and transmission issues
- `C22`: Add neighbor relationship between 3237345_3 and 3251195_4 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.734 | MS1 | 121.4656726522 | 31.1446277784 | 541 | 504990 | -81.57 | 16.91 | 401.37 | 0.12 | 2.04 | 1584 |
| 2024-09-20 22:21:32.673 | MS1 | 121.4656769570 | 31.1446344133 | 541 | 504990 | -76.76 | 12.49 | 585.56 | 0.04 | 2.56 | 1598 |
| 2024-09-20 22:21:33.974 | MS1 | 121.4656583181 | 31.1446363879 | 541 | 504990 | -81.79 | 17.11 | 361.71 | 0.05 | 2.83 | 1599 |
| 2024-09-20 22:21:34.354 | MS1 | 121.4656773015 | 31.1446232769 | 541 | 504990 | -94.12 | -2.37 | 35.94 | 0.20 | 1.24 | 1568 |
| 2024-09-20 22:21:35.971 | MS1 | 121.4656727404 | 31.1446197777 | 541 | 504990 | -86.15 | -3.39 | 37.58 | 0.07 | 1.15 | 1582 |
| 2024-09-20 22:21:36.244 | MS1 | 121.4656755670 | 31.1446209069 | 541 | 504990 | -87.87 | -2.01 | 59.14 | 0.20 | 1.07 | 1576 |
| 2024-09-20 22:21:37.633 | MS1 | 121.4656588130 | 31.1446295536 | 541 | 504990 | -94.87 | -2.98 | 52.85 | 0.06 | 1.36 | 1562 |
| 2024-09-20 22:21:38.837 | MS1 | 121.4656749513 | 31.1446315777 | 541 | 504990 | -84.83 | 16.15 | 505.99 | 0.05 | 1.14 | 1597 |
| 2024-09-20 22:21:39.230 | MS1 | 121.4656715964 | 31.1446319802 | 541 | 504990 | -75.27 | 12.35 | 529.22 | 0.03 | 1.19 | 1570 |
| 2024-09-20 22:21:40.979 | MS1 | 121.4656755487 | 31.1446377242 | 541 | 504990 | -76.51 | 17.80 | 573.99 | 0.01 | 2.63 | 1575 |
| 2024-09-20 22:21:41.640 | MS1 | 121.4656724518 | 31.1446284899 | 541 | 504990 | -80.55 | 16.37 | 463.16 | 0.02 | 2.54 | 1564 |
| 2024-09-20 22:21:42.440 | MS1 | 121.4656777213 | 31.1446290973 | 541 | 504990 | -84.29 | 13.87 | 345.18 | 0.08 | 2.37 | 1573 |

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
| 3231759 | 1 | 121.4675550880 | 31.1541967934 | 128 | 5 | 10 | 20.1 | TDD | 442 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3237345 | 3 | 121.4747396186 | 31.1514592139 | 221 | 12 | 2 | 16.1 | TDD | 541 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3251195 | 4 | 121.4749267527 | 31.1518468625 | 239 | 3 | 10 | 32.2 | TDD | 374 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3274560 | 2 | 121.4740648198 | 31.1482901957 | 320 | 4 | 8 | 27.4 | TDD | 908 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.456 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.597 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.597 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.313 | NREventA3 | measId:2;ServCellPCI:572;Se... |
| 2024-09-20 22:21:36.313 | NREventA3 | measId:2;ServCellPCI:572;Se... |
| 2024-09-20 22:21:37.313 | NREventA3 | measId:2;ServCellPCI:572;Se... |
| 2024-09-20 22:21:39.813 | NRRRCReestablishAttempt | PCI:572 |
| 2024-09-20 22:21:39.832 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.846 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.980 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.980 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231759 | 1 | 10.3586 | 16.6676 | -116.3195 | 13.6737 | 161.7541 | 0.0021 | 0.0068 |
| 2024_09_20 22:00 | 3274560 | 2 | 17.0538 | 15.6642 | -115.4730 | 15.3454 | 90.6586 | 0.0097 | 0.0121 |
| 2024_09_20 22:00 | 3237345 | 3 | 9.0281 | 11.5372 | -114.8588 | 12.3070 | 104.7159 | 0.0042 | 0.1518 |
| 2024_09_20 22:00 | 3251195 | 4 | 11.9357 | 7.5264 | -114.1794 | 5.5724 | 92.1183 | 0.0117 | 0.0098 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415973_6462C261 | 504990 | 374 | -87.5 | 504990 | 541 | -92.6 | 504990 | 442 | -90.5 | 504990 | 908 |
| MR_1774415973_9C49C5AD | 504990 | 374 | -88.4 | 504990 | 541 | -92.8 | 504990 | 442 | -88.4 | 504990 | 908 |
| MR_1774415973_EE23F215 | 504990 | 374 | -89.4 | 504990 | 541 | -95.8 | 504990 | 442 | -89.3 | 504990 | 908 |
| MR_1774415973_7DBEDD52 | 504990 | 541 | -95.5 | 504990 | 374 | -89.7 | 504990 | 442 | -90.3 | 504990 | 908 |
| MR_1774415973_A1C722BE | 504990 | 541 | -96.0 | 504990 | 374 | -88.6 | 504990 | 442 | -90.8 | 504990 | 908 |
| MR_1774415973_6B3F0340 | 504990 | 541 | -94.9 | 504990 | 374 | -90.7 | 504990 | 442 | -91.1 | 504990 | 908 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1451: `2b9464bb-cc7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2b9464bb-cc70-4147-a7b8-a18d12145dc7` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Add neighbor relationship between 3257714_2 and 3243351_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1451] topology](images/train_1451.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3243351_4
- `C2`: Decrease transmission power for 3257714_2
- `C3`: Lift the tilt angle  of 3243351_4 by 5 degrees
- `C4`: Press down the tilt angle  of 3243351_4 by 5 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Add neighbor relationship between 3257714_2 and 3243351_4 **← 정답**
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257714_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243351_4
- `C9`: Increase transmission power for 3243351_4
- `C10`: Increase transmission power for 3257714_2
- `C11`: Press down the tilt angle of 3257714_2 by 9 degrees
- `C12`: Adjust the azimuth of 3243351_4 by 30 degrees
- `C13`: Lift the tilt angle of 3257714_2 by 9 degrees
- `C14`: Increase A3 Offset threshold for 3257714_2
- `C15`: Decrease A3 Offset threshold for 3243351_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257714_2
- `C17`: Decrease transmission power for 3243351_4
- `C18`: Check test server and transmission issues
- `C19`: Adjust the azimuth of 3257714_2 by 24 degrees
- `C20`: Decrease A3 Offset threshold for 3257714_2
- `C21`: Add neighbor relationship between 3235036_1 and 3243351_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243351_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.326 | MS1 | 121.4656731836 | 31.1446241055 | 833 | 504990 | -83.03 | 17.26 | 486.69 | 0.07 | 2.82 | 1600 |
| 2024-09-20 22:21:32.871 | MS1 | 121.4656723407 | 31.1446316060 | 833 | 504990 | -77.03 | 14.33 | 569.79 | 0.11 | 2.59 | 1592 |
| 2024-09-20 22:21:33.706 | MS1 | 121.4656613793 | 31.1446241094 | 833 | 504990 | -83.15 | 12.34 | 371.73 | 0.03 | 2.93 | 1594 |
| 2024-09-20 22:21:34.913 | MS1 | 121.4656637028 | 31.1446190244 | 833 | 504990 | -93.09 | -0.36 | 75.88 | 0.12 | 1.45 | 1578 |
| 2024-09-20 22:21:35.425 | MS1 | 121.4656778002 | 31.1446183452 | 833 | 504990 | -93.78 | -1.52 | 56.25 | 0.03 | 1.27 | 1568 |
| 2024-09-20 22:21:36.731 | MS1 | 121.4656744163 | 31.1446370436 | 833 | 504990 | -85.64 | -1.81 | 30.79 | 0.17 | 1.20 | 1589 |
| 2024-09-20 22:21:37.579 | MS1 | 121.4656681076 | 31.1446344967 | 833 | 504990 | -90.17 | -0.62 | 59.55 | 0.11 | 1.48 | 1564 |
| 2024-09-20 22:21:38.712 | MS1 | 121.4656622634 | 31.1446269133 | 833 | 504990 | -81.80 | 17.98 | 557.15 | 0.07 | 1.00 | 1568 |
| 2024-09-20 22:21:39.194 | MS1 | 121.4656722717 | 31.1446234337 | 833 | 504990 | -80.03 | 12.83 | 549.82 | 0.18 | 1.09 | 1576 |
| 2024-09-20 22:21:40.157 | MS1 | 121.4656676747 | 31.1446230727 | 833 | 504990 | -75.25 | 16.92 | 306.07 | 0.03 | 2.73 | 1587 |
| 2024-09-20 22:21:41.341 | MS1 | 121.4656761663 | 31.1446284319 | 833 | 504990 | -83.60 | 13.04 | 324.37 | 0.03 | 2.43 | 1570 |
| 2024-09-20 22:21:42.163 | MS1 | 121.4656593654 | 31.1446205514 | 833 | 504990 | -75.14 | 15.87 | 480.72 | 0.16 | 2.32 | 1568 |

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
| 3235036 | 1 | 121.4736472966 | 31.1476849096 | 266 | 8 | 3 | 24.7 | TDD | 752 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3243351 | 4 | 121.4703944025 | 31.1496304731 | 189 | 2 | 1 | 35.2 | TDD | 703 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3257714 | 2 | 121.4665504250 | 31.1530097746 | 209 | 6 | 5 | 42.6 | TDD | 833 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3272033 | 3 | 121.4676050859 | 31.1551371072 | 17 | 4 | 1 | 21.8 | TDD | 509 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.440 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.463 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.589 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.589 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.334 | NREventA3 | measId:2;ServCellPCI:899;Se... |
| 2024-09-20 22:21:36.334 | NREventA3 | measId:2;ServCellPCI:899;Se... |
| 2024-09-20 22:21:37.334 | NREventA3 | measId:2;ServCellPCI:899;Se... |
| 2024-09-20 22:21:39.834 | NRRRCReestablishAttempt | PCI:899 |
| 2024-09-20 22:21:39.846 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.860 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.984 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.984 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235036 | 1 | 14.4168 | 12.4107 | -114.3912 | 8.5313 | 81.5370 | 0.0182 | 0.0074 |
| 2024_09_20 22:00 | 3257714 | 2 | 15.4648 | 9.9371 | -115.6313 | 10.1450 | 199.6667 | 0.0152 | 0.1819 |
| 2024_09_20 22:00 | 3272033 | 3 | 7.3385 | 18.3928 | -115.2305 | 6.3207 | 91.0154 | 0.0169 | 0.0102 |
| 2024_09_20 22:00 | 3243351 | 4 | 15.9945 | 16.6522 | -117.5139 | 18.7178 | 176.8849 | 0.0094 | 0.0081 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413719_C31459D7 | 504990 | 833 | -94.2 | 504990 | 703 | -87.4 | 504990 | 752 | -92.6 | 504990 | 509 |
| MR_1774413719_76470CCA | 504990 | 833 | -91.7 | 504990 | 703 | -90.0 | 504990 | 752 | -89.6 | 504990 | 509 |
| MR_1774413719_1FFAB800 | 504990 | 703 | -89.1 | 504990 | 833 | -94.2 | 504990 | 752 | -91.4 | 504990 | 509 |
| MR_1774413719_7736C3D9 | 504990 | 703 | -90.5 | 504990 | 833 | -94.8 | 504990 | 752 | -92.8 | 504990 | 509 |
| MR_1774413719_FA5DFD27 | 504990 | 703 | -90.4 | 504990 | 833 | -91.4 | 504990 | 752 | -90.4 | 504990 | 509 |
| MR_1774413719_86BE67E9 | 504990 | 703 | -89.2 | 504990 | 833 | -93.7 | 504990 | 752 | -89.5 | 504990 | 509 |
| MR_1774413719_89CE8DB6 | 504990 | 833 | -94.3 | 504990 | 703 | -88.9 | 504990 | 752 | -92.0 | 504990 | 509 |
| MR_1774413719_1EA7237A | 504990 | 833 | -93.9 | 504990 | 703 | -88.2 | 504990 | 752 | -92.7 | 504990 | 509 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1452: `ae308d79-212...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ae308d79-212f-42a0-9c4b-66f3f12c2aa9` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1452] topology](images/train_1452.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3271641_2 by 10 degrees
- `C2`: Decrease A3 Offset threshold for 3271641_2
- `C3`: Lift the tilt angle  of 3244052_3 by 10 degrees
- `C4`: Add neighbor relationship between 3237269_4 and 3244052_3
- `C5`: Press down the tilt angle  of 3244052_3 by 10 degrees
- `C6`: Increase transmission power for 3244052_3
- `C7`: Decrease A3 Offset threshold for 3244052_3
- `C8`: Adjust the azimuth of 3244052_3 by 27 degrees
- `C9`: Press down the tilt angle of 3271641_2 by 10 degrees
- `C10`: Increase A3 Offset threshold for 3271641_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271641_2
- `C12`: Add neighbor relationship between 3271641_2 and 3244052_3
- `C13`: Check test server and transmission issues
- `C14`: Decrease transmission power for 3244052_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244052_3
- `C16`: Adjust the azimuth of 3271641_2 by 37 degrees
- `C17`: Increase A3 Offset threshold for 3244052_3
- `C18`: Decrease transmission power for 3271641_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244052_3
- `C20`: Insufficient data; more data is needed for judgment. **← 정답**
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271641_2
- `C22`: Increase transmission power for 3271641_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.305 | MS1 | 121.4656591022 | 31.1446282432 | 900 | 504990 | -88.83 | 13.61 | 378.73 | 0.02 | 2.61 | 1564 |
| 2024-09-20 22:21:32.553 | MS1 | 121.4656703954 | 31.1446318059 | 900 | 504990 | -91.58 | 17.95 | 418.12 | 0.18 | 2.58 | 1568 |
| 2024-09-20 22:21:33.210 | MS1 | 121.4656678893 | 31.1446185600 | 900 | 504990 | -88.45 | 17.61 | 385.99 | 0.13 | 2.39 | 1597 |
| 2024-09-20 22:21:34.687 | MS1 | 121.4656769797 | 31.1446356877 | 900 | 504990 | -90.89 | 14.11 | 62.81 | 0.03 | 2.41 | 1596 |
| 2024-09-20 22:21:35.944 | MS1 | 121.4656687547 | 31.1446376703 | 900 | 504990 | -91.11 | 14.36 | 91.42 | 0.03 | 2.23 | 1565 |
| 2024-09-20 22:21:36.136 | MS1 | 121.4656697227 | 31.1446185514 | 900 | 504990 | -90.98 | 15.60 | 72.90 | 0.18 | 2.30 | 1597 |
| 2024-09-20 22:21:37.813 | MS1 | 121.4656587789 | 31.1446357419 | 900 | 504990 | -93.10 | 9.95 | 44.35 | 0.13 | 2.53 | 1582 |
| 2024-09-20 22:21:38.682 | MS1 | 121.4656748079 | 31.1446183913 | 900 | 504990 | -89.03 | 7.78 | 98.64 | 0.11 | 2.32 | 1562 |
| 2024-09-20 22:21:39.819 | MS1 | 121.4656723223 | 31.1446277568 | 900 | 504990 | -92.37 | 9.82 | 54.18 | 0.19 | 2.13 | 1593 |
| 2024-09-20 22:21:40.603 | MS1 | 121.4656660426 | 31.1446352953 | 900 | 504990 | -91.71 | 9.50 | 378.86 | 0.17 | 2.86 | 1560 |
| 2024-09-20 22:21:41.832 | MS1 | 121.4656681801 | 31.1446196541 | 900 | 504990 | -92.55 | 9.38 | 491.23 | 0.16 | 2.01 | 1595 |
| 2024-09-20 22:21:42.246 | MS1 | 121.4656631366 | 31.1446188517 | 900 | 504990 | -93.18 | 12.14 | 560.10 | 0.16 | 2.29 | 1566 |

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
| 3237269 | 4 | 121.4757997825 | 31.1521253862 | 140 | 5 | 1 | 24.7 | TDD | 972 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3244052 | 3 | 121.4737764138 | 31.1558756899 | 239 | 9 | 4 | 45.5 | TDD | 563 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3271466 | 1 | 121.4679374721 | 31.1491204004 | 159 | 13 | 0 | 25.4 | TDD | 728 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3271641 | 2 | 121.4731257021 | 31.1471281530 | 286 | 14 | 10 | 19.4 | TDD | 900 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.929 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.944 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.076 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.076 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.785 | NREventA3 | measId:2;ServCellPCI:32;Ser... |
| 2024-09-20 22:21:38.025 | NRHandoverAttempt | SourcePCI:32;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.060 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.072 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.172 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.172 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3271466 | 1 | 85.7403 | 80.6199 | -117.8744 | 13.5229 | 167.5943 | 0.0108 | 0.0170 |
| 2024_09_19 22:00 | 3271641 | 2 | 93.3514 | 80.6980 | -114.6968 | 16.8323 | 87.2556 | 0.0014 | 0.0171 |
| 2024_09_19 22:00 | 3244052 | 3 | 91.7899 | 83.9428 | -115.0222 | 17.1921 | 158.4605 | 0.0068 | 0.0080 |
| 2024_09_19 22:00 | 3237269 | 4 | 86.8390 | 87.5911 | -116.6842 | 19.0935 | 121.9875 | 0.0049 | 0.0139 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414639_95157D3F | 504990 | 900 | -90.8 | 504990 | 563 | -96.8 | 504990 | 972 | -100.5 | 504990 | 728 |
| MR_1774414639_E9807B49 | 504990 | 900 | -92.2 | 504990 | 563 | -96.3 | 504990 | 972 | -102.8 | 504990 | 728 |
| MR_1774414639_E1721380 | 504990 | 900 | -90.3 | 504990 | 563 | -96.8 | 504990 | 972 | -101.6 | 504990 | 728 |
| MR_1774414639_31FCCCB6 | 504990 | 900 | -91.8 | 504990 | 563 | -96.9 | 504990 | 972 | -100.6 | 504990 | 728 |
| MR_1774414639_84177129 | 504990 | 900 | -92.3 | 504990 | 563 | -96.7 | 504990 | 972 | -99.9 | 504990 | 728 |
| MR_1774414639_FE798CE9 | 504990 | 900 | -91.2 | 504990 | 563 | -96.3 | 504990 | 972 | -103.2 | 504990 | 728 |
| MR_1774414639_9CA97362 | 504990 | 900 | -91.0 | 504990 | 563 | -98.3 | 504990 | 972 | -99.9 | 504990 | 728 |
| MR_1774414639_4087835D | 504990 | 900 | -91.0 | 504990 | 563 | -97.4 | 504990 | 972 | -100.0 | 504990 | 728 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1453: `b15d305f-1d6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b15d305f-1d60-4e6b-bd40-fd4ae812bbc3` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3263860_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1453] topology](images/train_1453.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3263860_1
- `C2`: Press down the tilt angle  of 3245963_4 by 10 degrees
- `C3`: Decrease transmission power for 3245963_4
- `C4`: Increase A3 Offset threshold for 3263860_1
- `C5`: Lift the tilt angle of 3263860_1 by 4 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Adjust the azimuth of 3245963_4 by 50 degrees
- `C8`: Adjust the azimuth of 3263860_1 by 21 degrees
- `C9`: Decrease A3 Offset threshold for 3263860_1
- `C10`: Increase A3 Offset threshold for 3245963_4
- `C11`: Decrease A3 Offset threshold for 3245963_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263860_1 **← 정답**
- `C13`: Increase transmission power for 3263860_1
- `C14`: Check test server and transmission issues
- `C15`: Add neighbor relationship between 3263860_1 and 3245963_4
- `C16`: Increase transmission power for 3245963_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263860_1
- `C18`: Lift the tilt angle  of 3245963_4 by 10 degrees
- `C19`: Press down the tilt angle of 3263860_1 by 4 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245963_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245963_4
- `C22`: Add neighbor relationship between 3250873_2 and 3245963_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.872 | MS1 | 121.4656718285 | 31.1446215265 | 337 | 504990 | -86.36 | 14.61 | 472.49 | 0.04 | 2.36 | 1586 |
| 2024-09-20 22:21:32.429 | MS1 | 121.4656626505 | 31.1446246226 | 337 | 504990 | -88.93 | 16.21 | 509.62 | 0.09 | 2.44 | 1598 |
| 2024-09-20 22:21:33.830 | MS1 | 121.4656717466 | 31.1446240796 | 337 | 504990 | -91.72 | 16.51 | 451.91 | 0.05 | 2.05 | 1577 |
| 2024-09-20 22:21:34.900 | MS1 | 121.4656682234 | 31.1446377338 | 337 | 504990 | -87.30 | 15.19 | 56.69 | 0.54 | 2.17 | 694 |
| 2024-09-20 22:21:35.492 | MS1 | 121.4656681830 | 31.1446301824 | 337 | 504990 | -85.42 | 17.06 | 91.56 | 0.68 | 2.85 | 565 |
| 2024-09-20 22:21:36.737 | MS1 | 121.4656666879 | 31.1446199108 | 337 | 504990 | -89.17 | 13.07 | 71.91 | 0.70 | 2.83 | 537 |
| 2024-09-20 22:21:37.658 | MS1 | 121.4656722716 | 31.1446359344 | 337 | 504990 | -92.60 | 10.40 | 46.49 | 0.68 | 2.76 | 646 |
| 2024-09-20 22:21:38.135 | MS1 | 121.4656727523 | 31.1446245989 | 337 | 504990 | -91.19 | 9.86 | 68.55 | 0.56 | 2.99 | 638 |
| 2024-09-20 22:21:39.169 | MS1 | 121.4656593677 | 31.1446285822 | 337 | 504990 | -89.46 | 11.69 | 61.10 | 0.61 | 2.85 | 699 |
| 2024-09-20 22:21:40.741 | MS1 | 121.4656581047 | 31.1446319240 | 337 | 504990 | -92.01 | 7.95 | 392.34 | 0.04 | 2.08 | 1568 |
| 2024-09-20 22:21:41.402 | MS1 | 121.4656711860 | 31.1446210010 | 337 | 504990 | -92.29 | 11.06 | 451.89 | 0.04 | 2.03 | 1567 |
| 2024-09-20 22:21:42.975 | MS1 | 121.4656607909 | 31.1446185974 | 337 | 504990 | -92.81 | 8.76 | 347.34 | 0.12 | 2.77 | 1597 |

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
| 3238509 | 3 | 121.4740142372 | 31.1526927877 | 240 | 5 | 8 | 31.8 | TDD | 699 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3245963 | 4 | 121.4655282715 | 31.1538907593 | 68 | 9 | 0 | 37.5 | TDD | 430 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3250873 | 2 | 121.4675728287 | 31.1448369502 | 236 | 3 | 1 | 26.3 | TDD | 987 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3263860 | 1 | 121.4712558798 | 31.1548540204 | 226 | 3 | 3 | 23.3 | TDD | 337 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.367 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.387 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.499 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.499 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.196 | NREventA3 | measId:2;ServCellPCI:433;Se... |
| 2024-09-20 22:21:38.436 | NRHandoverAttempt | SourcePCI:433;SourceNR-ARFC... |
| 2024-09-20 22:21:38.477 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.491 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.637 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.637 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263860 | 1 | 17.6309 | 16.1276 | -117.0891 | 5.7930 | 137.7768 | 0.0103 | 0.0055 |
| 2024_09_20 22:00 | 3250873 | 2 | 11.3698 | 10.7331 | -116.4372 | 11.3522 | 177.0572 | 0.0130 | 0.0157 |
| 2024_09_20 22:00 | 3238509 | 3 | 19.2151 | 8.0760 | -117.2651 | 12.4980 | 102.7426 | 0.0040 | 0.0067 |
| 2024_09_20 22:00 | 3245963 | 4 | 18.3541 | 5.6623 | -116.7896 | 5.8191 | 91.0108 | 0.0011 | 0.0011 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413148_FF85158D | 504990 | 337 | -87.8 | 504990 | 430 | -90.2 | 504990 | 987 | -94.7 | 504990 | 699 |
| MR_1774413148_73CA4BD2 | 504990 | 337 | -88.8 | 504990 | 430 | -90.5 | 504990 | 987 | -93.6 | 504990 | 699 |
| MR_1774413148_2ECB0BFC | 504990 | 337 | -85.3 | 504990 | 430 | -91.1 | 504990 | 987 | -96.4 | 504990 | 699 |
| MR_1774413148_32DB5F27 | 504990 | 337 | -86.0 | 504990 | 430 | -92.6 | 504990 | 987 | -93.8 | 504990 | 699 |
| MR_1774413148_0D4995BF | 504990 | 337 | -85.5 | 504990 | 430 | -89.5 | 504990 | 987 | -96.2 | 504990 | 699 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1454: `cdddeb05-4d2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cdddeb05-4d2c-4bc8-a091-7ec948bd8c08` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Lift the tilt angle  of 3275503_1 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1454] topology](images/train_1454.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3247281_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247281_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257214_4
- `C4`: Increase transmission power for 3257214_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257214_4
- `C6`: Press down the tilt angle of 3257214_4 by 1 degrees
- `C7`: Add neighbor relationship between 3257214_4 and 3247281_3
- `C8`: Check test server and transmission issues
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247281_3
- `C10`: Increase transmission power for 3247281_3
- `C11`: Add neighbor relationship between 3275503_1 and 3247281_3
- `C12`: Decrease A3 Offset threshold for 3257214_4
- `C13`: Decrease transmission power for 3247281_3
- `C14`: Decrease transmission power for 3257214_4
- `C15`: Adjust the azimuth of 3257214_4 by 42 degrees
- `C16`: Adjust the azimuth of 3275503_1 by 50 degrees
- `C17`: Press down the tilt angle  of 3275503_1 by 7 degrees
- `C18`: Lift the tilt angle of 3257214_4 by 1 degrees
- `C19`: Increase A3 Offset threshold for 3247281_3
- `C20`: Lift the tilt angle  of 3275503_1 by 7 degrees **← 정답**
- `C21`: Increase A3 Offset threshold for 3257214_4
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.647 | MS1 | 121.4656626648 | 31.1446211367 | 917 | 504990 | -86.98 | 15.59 | 372.92 | 0.04 | 2.23 | 1571 |
| 2024-09-20 22:21:32.674 | MS1 | 121.4656704127 | 31.1446315883 | 917 | 504990 | -88.06 | 15.48 | 369.76 | 0.03 | 2.23 | 1570 |
| 2024-09-20 22:21:33.899 | MS1 | 121.4656595498 | 31.1446276140 | 917 | 504990 | -91.75 | 17.72 | 455.95 | 0.06 | 2.07 | 1586 |
| 2024-09-20 22:21:34.879 | MS1 | 121.4656686267 | 31.1446206976 | 917 | 504990 | -86.63 | 14.72 | 74.52 | 0.16 | 2.98 | 1575 |
| 2024-09-20 22:21:35.852 | MS1 | 121.4656746371 | 31.1446206305 | 917 | 504990 | -88.02 | 13.45 | 83.38 | 0.18 | 2.56 | 1564 |
| 2024-09-20 22:21:36.159 | MS1 | 121.4656721120 | 31.1446351695 | 917 | 504990 | -86.15 | 12.00 | 74.60 | 0.14 | 2.07 | 1569 |
| 2024-09-20 22:21:37.983 | MS1 | 121.4656711294 | 31.1446319777 | 917 | 504990 | -90.32 | 9.27 | 85.11 | 0.09 | 2.96 | 1563 |
| 2024-09-20 22:21:38.816 | MS1 | 121.4656620380 | 31.1446281459 | 917 | 504990 | -93.99 | 9.53 | 75.67 | 0.03 | 2.37 | 1581 |
| 2024-09-20 22:21:39.114 | MS1 | 121.4656659833 | 31.1446223929 | 917 | 504990 | -92.64 | 12.15 | 64.05 | 0.08 | 2.78 | 1566 |
| 2024-09-20 22:21:40.124 | MS1 | 121.4656684985 | 31.1446234205 | 917 | 504990 | -91.10 | 9.02 | 476.64 | 0.09 | 2.19 | 1573 |
| 2024-09-20 22:21:41.377 | MS1 | 121.4656588718 | 31.1446314180 | 917 | 504990 | -92.31 | 8.08 | 563.79 | 0.09 | 2.43 | 1589 |
| 2024-09-20 22:21:42.116 | MS1 | 121.4656763780 | 31.1446253028 | 917 | 504990 | -92.75 | 8.58 | 567.20 | 0.06 | 2.26 | 1582 |

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
| 3247281 | 3 | 121.4708237411 | 31.1497082769 | 282 | 3 | 1 | 47.8 | TDD | 197 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3250100 | 2 | 121.4678189648 | 31.1527876151 | 113 | 1 | 0 | 43.1 | TDD | 939 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3257214 | 4 | 121.4756580911 | 31.1464802233 | 216 | 0 | 11 | 16.7 | TDD | 917 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3275503 | 1 | 121.4667764245 | 31.1477608440 | 62 | 13 | 10 | 25.2 | TDD | 490 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.823 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.838 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.982 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.982 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.664 | NREventA3 | measId:2;ServCellPCI:316;Se... |
| 2024-09-20 22:21:37.904 | NRHandoverAttempt | SourcePCI:316;SourceNR-ARFC... |
| 2024-09-20 22:21:37.951 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.966 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.101 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.101 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275503 | 1 | 14.9311 | 18.0082 | -116.1832 | 8.8880 | 88.3789 | 0.0024 | 0.0082 |
| 2024_09_20 22:00 | 3250100 | 2 | 6.5853 | 17.2071 | -115.5302 | 11.5765 | 183.9178 | 0.0173 | 0.0051 |
| 2024_09_20 22:00 | 3247281 | 3 | 14.1599 | 9.4406 | -114.5058 | 17.3313 | 87.5802 | 0.0004 | 0.0133 |
| 2024_09_20 22:00 | 3257214 | 4 | 87.5817 | 92.2221 | -115.6443 | 17.7173 | 191.7937 | 0.0034 | 0.0154 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414659_27498BDF | 504990 | 917 | -85.0 | 504990 | 197 | -93.5 | 504990 | 490 | -93.4 | 504990 | 939 |
| MR_1774414659_B803986C | 504990 | 917 | -84.8 | 504990 | 197 | -92.5 | 504990 | 490 | -94.0 | 504990 | 939 |
| MR_1774414659_46576021 | 504990 | 917 | -86.7 | 504990 | 197 | -94.3 | 504990 | 490 | -93.5 | 504990 | 939 |
| MR_1774414659_C9358BA7 | 504990 | 917 | -86.3 | 504990 | 197 | -92.3 | 504990 | 490 | -95.0 | 504990 | 939 |
| MR_1774414659_97C98097 | 504990 | 917 | -88.5 | 504990 | 197 | -96.2 | 504990 | 490 | -94.2 | 504990 | 939 |
| MR_1774414659_0A00C71D | 504990 | 917 | -85.7 | 504990 | 197 | -93.1 | 504990 | 490 | -95.3 | 504990 | 939 |
| MR_1774414659_1383C01B | 504990 | 917 | -85.5 | 504990 | 197 | -95.7 | 504990 | 490 | -93.4 | 504990 | 939 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1455: `cadf587f-71e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cadf587f-71e4-4cc6-82ea-bcf083510cb5` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease A3 Offset threshold for 3244276_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1455] topology](images/train_1455.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3279794_2
- `C2`: Increase A3 Offset threshold for 3244276_4
- `C3`: Decrease transmission power for 3244276_4
- `C4`: Check test server and transmission issues
- `C5`: Add neighbor relationship between 3244276_4 and 3279794_2
- `C6`: Increase transmission power for 3244276_4
- `C7`: Press down the tilt angle  of 3279794_2 by 10 degrees
- `C8`: Adjust the azimuth of 3279794_2 by 50 degrees
- `C9`: Adjust the azimuth of 3244276_4 by 15 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279794_2
- `C11`: Decrease A3 Offset threshold for 3244276_4 **← 정답**
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Lift the tilt angle  of 3279794_2 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279794_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244276_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244276_4
- `C17`: Decrease A3 Offset threshold for 3279794_2
- `C18`: Press down the tilt angle of 3244276_4 by 8 degrees
- `C19`: Add neighbor relationship between 3230235_1 and 3279794_2
- `C20`: Decrease transmission power for 3279794_2
- `C21`: Lift the tilt angle of 3244276_4 by 8 degrees
- `C22`: Increase transmission power for 3279794_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.698 | MS1 | 121.4656734066 | 31.1446344602 | 534 | 504990 | -83.24 | 17.23 | 580.08 | 0.05 | 2.40 | 1581 |
| 2024-09-20 22:21:32.616 | MS1 | 121.4656604536 | 31.1446182605 | 534 | 504990 | -84.89 | 17.29 | 546.46 | 0.16 | 2.61 | 1588 |
| 2024-09-20 22:21:33.521 | MS1 | 121.4656624359 | 31.1446259098 | 534 | 504990 | -84.57 | 15.05 | 391.33 | 0.01 | 2.73 | 1560 |
| 2024-09-20 22:21:34.958 | MS1 | 121.4656602585 | 31.1446323792 | 534 | 504990 | -85.98 | -1.57 | 47.42 | 0.07 | 1.06 | 1561 |
| 2024-09-20 22:21:35.290 | MS1 | 121.4656743266 | 31.1446298625 | 534 | 504990 | -86.55 | -3.18 | 72.86 | 0.11 | 1.33 | 1578 |
| 2024-09-20 22:21:36.141 | MS1 | 121.4656616985 | 31.1446242682 | 534 | 504990 | -92.89 | -1.20 | 59.36 | 0.02 | 1.17 | 1599 |
| 2024-09-20 22:21:37.510 | MS1 | 121.4656659547 | 31.1446322237 | 534 | 504990 | -86.00 | -1.72 | 68.58 | 0.19 | 1.16 | 1562 |
| 2024-09-20 22:21:38.427 | MS1 | 121.4656763951 | 31.1446189621 | 534 | 504990 | -89.42 | -3.69 | 76.91 | 0.13 | 1.06 | 1592 |
| 2024-09-20 22:21:39.438 | MS1 | 121.4656612390 | 31.1446187524 | 6 | 504990 | -80.78 | 12.04 | 295.53 | 0.20 | 1.43 | 1575 |
| 2024-09-20 22:21:40.807 | MS1 | 121.4656627854 | 31.1446236414 | 6 | 504990 | -83.92 | 13.59 | 530.21 | 0.06 | 2.05 | 1571 |
| 2024-09-20 22:21:41.532 | MS1 | 121.4656769247 | 31.1446357682 | 6 | 504990 | -75.89 | 17.06 | 397.28 | 0.05 | 2.97 | 1572 |
| 2024-09-20 22:21:42.710 | MS1 | 121.4656689223 | 31.1446359901 | 6 | 504990 | -77.55 | 15.81 | 594.49 | 0.06 | 2.81 | 1597 |

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
| 3230235 | 1 | 121.4695622102 | 31.1445684219 | 321 | 3 | 10 | 38.9 | TDD | 297 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3244276 | 4 | 121.4757923111 | 31.1516397890 | 216 | 7 | 3 | 15.7 | TDD | 534 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3250920 | 3 | 121.4727324888 | 31.1518925720 | 163 | 1 | 1 | 46.1 | TDD | 486 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3279794 | 2 | 121.4742115736 | 31.1553646822 | 346 | 12 | 12 | 33.7 | TDD | 6 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.405 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.425 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.573 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.573 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.233 | NREventA3 | measId:2;ServCellPCI:857;Se... |
| 2024-09-20 22:21:38.473 | NRHandoverAttempt | SourcePCI:857;SourceNR-ARFC... |
| 2024-09-20 22:21:38.513 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.526 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.658 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.658 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230235 | 1 | 12.5067 | 13.5864 | -116.3137 | 15.8696 | 154.9446 | 0.0063 | 0.0085 |
| 2024_09_20 22:00 | 3279794 | 2 | 6.9097 | 7.8310 | -117.1057 | 16.3759 | 155.5415 | 0.0039 | 0.0098 |
| 2024_09_20 22:00 | 3250920 | 3 | 7.8406 | 12.3295 | -115.9375 | 13.3081 | 149.8022 | 0.0176 | 0.0056 |
| 2024_09_20 22:00 | 3244276 | 4 | 17.0446 | 6.5987 | -115.7367 | 17.6710 | 192.1467 | 0.0157 | 0.1768 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414890_9F1E854B | 504990 | 534 | -87.9 | 504990 | 6 | -83.6 | 504990 | 297 | -84.9 | 504990 | 486 |
| MR_1774414890_DAAFE98D | 504990 | 534 | -86.8 | 504990 | 6 | -81.3 | 504990 | 297 | -83.6 | 504990 | 486 |
| MR_1774414890_0EF3043B | 504990 | 6 | -82.3 | 504990 | 534 | -86.8 | 504990 | 297 | -86.1 | 504990 | 486 |
| MR_1774414890_2057316E | 504990 | 534 | -84.8 | 504990 | 6 | -82.1 | 504990 | 297 | -85.5 | 504990 | 486 |
| MR_1774414890_08FC35C9 | 504990 | 534 | -84.5 | 504990 | 6 | -83.3 | 504990 | 297 | -86.2 | 504990 | 486 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1456: `0432698f-72f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0432698f-72f9-49cb-b861-d27f4aec5049` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1456] topology](images/train_1456.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3242712_2 and 3228367_1
- `C2`: Decrease A3 Offset threshold for 3265483_4
- `C3`: Check test server and transmission issues **← 정답**
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228367_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265483_4
- `C6`: Increase A3 Offset threshold for 3228367_1
- `C7`: Press down the tilt angle of 3265483_4 by 1 degrees
- `C8`: Adjust the azimuth of 3265483_4 by 50 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Add neighbor relationship between 3265483_4 and 3228367_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228367_1
- `C12`: Increase transmission power for 3265483_4
- `C13`: Lift the tilt angle of 3265483_4 by 1 degrees
- `C14`: Increase A3 Offset threshold for 3265483_4
- `C15`: Press down the tilt angle  of 3228367_1 by 10 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265483_4
- `C17`: Adjust the azimuth of 3228367_1 by 50 degrees
- `C18`: Lift the tilt angle  of 3228367_1 by 10 degrees
- `C19`: Decrease transmission power for 3228367_1
- `C20`: Decrease A3 Offset threshold for 3228367_1
- `C21`: Decrease transmission power for 3265483_4
- `C22`: Increase transmission power for 3228367_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.111 | MS1 | 121.4656666951 | 31.1446187043 | 471 | 504990 | -85.23 | 13.85 | 521.57 | 0.01 | 2.62 | 1590 |
| 2024-09-20 22:21:32.252 | MS1 | 121.4656685527 | 31.1446330523 | 471 | 504990 | -86.92 | 14.21 | 551.34 | 0.03 | 2.88 | 1593 |
| 2024-09-20 22:21:33.547 | MS1 | 121.4656685116 | 31.1446223963 | 471 | 504990 | -87.40 | 13.67 | 564.12 | 0.09 | 2.71 | 1581 |
| 2024-09-20 22:21:34.370 | MS1 | 121.4656595963 | 31.1446230136 | 471 | 504990 | -85.38 | 12.61 | 78.37 | 0.08 | 2.66 | 451 |
| 2024-09-20 22:21:35.410 | MS1 | 121.4656667251 | 31.1446275521 | 471 | 504990 | -87.39 | 17.63 | 88.52 | 0.04 | 2.00 | 409 |
| 2024-09-20 22:21:36.939 | MS1 | 121.4656714287 | 31.1446264613 | 471 | 504990 | -87.05 | 14.47 | 73.88 | 0.18 | 2.62 | 384 |
| 2024-09-20 22:21:37.826 | MS1 | 121.4656650276 | 31.1446346432 | 471 | 504990 | -90.52 | 8.93 | 51.34 | 0.00 | 2.98 | 371 |
| 2024-09-20 22:21:38.833 | MS1 | 121.4656720670 | 31.1446270580 | 471 | 504990 | -92.07 | 11.27 | 69.02 | 0.00 | 2.02 | 428 |
| 2024-09-20 22:21:39.358 | MS1 | 121.4656714120 | 31.1446226940 | 471 | 504990 | -91.06 | 12.53 | 61.38 | 0.20 | 2.68 | 492 |
| 2024-09-20 22:21:40.929 | MS1 | 121.4656631377 | 31.1446226164 | 471 | 504990 | -92.27 | 9.53 | 367.67 | 0.02 | 2.09 | 1588 |
| 2024-09-20 22:21:41.529 | MS1 | 121.4656715832 | 31.1446298349 | 471 | 504990 | -93.13 | 12.68 | 332.50 | 0.09 | 2.88 | 1585 |
| 2024-09-20 22:21:42.388 | MS1 | 121.4656659330 | 31.1446378096 | 471 | 504990 | -92.88 | 9.21 | 376.07 | 0.12 | 2.42 | 1598 |

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
| 3213205 | 3 | 121.4658346249 | 31.1482106593 | 165 | 6 | 2 | 29.7 | TDD | 54 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3228367 | 1 | 121.4718393532 | 31.1498066115 | 13 | 15 | 9 | 16.6 | TDD | 256 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3242712 | 2 | 121.4678828310 | 31.1483008559 | 178 | 11 | 5 | 21.9 | TDD | 902 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3265483 | 4 | 121.4698570759 | 31.1548532283 | 66 | 0 | 11 | 24.2 | TDD | 471 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.241 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.258 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.388 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.388 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.114 | NREventA3 | measId:2;ServCellPCI:150;Se... |
| 2024-09-20 22:21:38.354 | NRHandoverAttempt | SourcePCI:150;SourceNR-ARFC... |
| 2024-09-20 22:21:38.389 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.399 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.519 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.519 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228367 | 1 | 16.2937 | 6.2893 | -116.6908 | 18.8741 | 101.2591 | 0.0192 | 0.0039 |
| 2024_09_20 22:00 | 3242712 | 2 | 16.9969 | 17.1028 | -114.6165 | 10.8921 | 177.5498 | 0.0152 | 0.0076 |
| 2024_09_20 22:00 | 3213205 | 3 | 7.0496 | 7.1457 | -115.0765 | 8.6078 | 184.1714 | 0.0056 | 0.0106 |
| 2024_09_20 22:00 | 3265483 | 4 | 11.6317 | 5.8473 | -115.7682 | 16.2286 | 100.6051 | 0.0037 | 0.0116 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415618_3C86B2AF | 504990 | 471 | -84.6 | 504990 | 256 | -94.2 | 504990 | 902 | -93.2 | 504990 | 54 |
| MR_1774415618_A05B8E21 | 504990 | 471 | -86.0 | 504990 | 256 | -90.8 | 504990 | 902 | -93.1 | 504990 | 54 |
| MR_1774415618_DB6B90E4 | 504990 | 471 | -83.7 | 504990 | 256 | -93.1 | 504990 | 902 | -93.7 | 504990 | 54 |
| MR_1774415618_9B35F1CC | 504990 | 471 | -84.8 | 504990 | 256 | -91.8 | 504990 | 902 | -93.0 | 504990 | 54 |
| MR_1774415618_55011158 | 504990 | 471 | -84.9 | 504990 | 256 | -93.5 | 504990 | 902 | -91.1 | 504990 | 54 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1457: `232801e5-f03...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `232801e5-f031-428d-9dfb-7e0c84d944e8` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Add neighbor relationship between 3249374_3 and 3224149_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1457] topology](images/train_1457.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3249374_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224149_1
- `C3`: Lift the tilt angle  of 3224149_1 by 6 degrees
- `C4`: Check test server and transmission issues
- `C5`: Decrease A3 Offset threshold for 3249374_3
- `C6`: Add neighbor relationship between 3249374_3 and 3224149_1 **← 정답**
- `C7`: Increase A3 Offset threshold for 3224149_1
- `C8`: Lift the tilt angle of 3249374_3 by 5 degrees
- `C9`: Increase A3 Offset threshold for 3249374_3
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase transmission power for 3249374_3
- `C12`: Adjust the azimuth of 3249374_3 by 50 degrees
- `C13`: Decrease A3 Offset threshold for 3224149_1
- `C14`: Increase transmission power for 3224149_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249374_3
- `C16`: Press down the tilt angle  of 3224149_1 by 6 degrees
- `C17`: Decrease transmission power for 3224149_1
- `C18`: Adjust the azimuth of 3224149_1 by 32 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249374_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224149_1
- `C21`: Press down the tilt angle of 3249374_3 by 5 degrees
- `C22`: Add neighbor relationship between 3279183_2 and 3224149_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.553 | MS1 | 121.4656588930 | 31.1446372636 | 382 | 504990 | -81.39 | 14.89 | 334.79 | 0.14 | 2.70 | 1574 |
| 2024-09-20 22:21:32.138 | MS1 | 121.4656735938 | 31.1446192145 | 382 | 504990 | -79.95 | 16.92 | 421.79 | 0.07 | 2.73 | 1561 |
| 2024-09-20 22:21:33.406 | MS1 | 121.4656624697 | 31.1446207238 | 382 | 504990 | -83.81 | 14.81 | 368.53 | 0.19 | 2.48 | 1593 |
| 2024-09-20 22:21:34.744 | MS1 | 121.4656674041 | 31.1446305266 | 382 | 504990 | -86.73 | -1.95 | 33.93 | 0.11 | 1.19 | 1576 |
| 2024-09-20 22:21:35.513 | MS1 | 121.4656681293 | 31.1446191696 | 382 | 504990 | -94.44 | -0.89 | 42.60 | 0.15 | 1.25 | 1560 |
| 2024-09-20 22:21:36.139 | MS1 | 121.4656695573 | 31.1446206306 | 382 | 504990 | -93.64 | -3.99 | 55.40 | 0.11 | 1.27 | 1585 |
| 2024-09-20 22:21:37.275 | MS1 | 121.4656744005 | 31.1446184050 | 382 | 504990 | -87.34 | -0.77 | 44.23 | 0.10 | 1.15 | 1598 |
| 2024-09-20 22:21:38.311 | MS1 | 121.4656653321 | 31.1446375180 | 382 | 504990 | -80.86 | 17.48 | 358.96 | 0.15 | 1.19 | 1560 |
| 2024-09-20 22:21:39.147 | MS1 | 121.4656778782 | 31.1446364862 | 382 | 504990 | -82.27 | 13.34 | 583.41 | 0.10 | 1.37 | 1574 |
| 2024-09-20 22:21:40.263 | MS1 | 121.4656596758 | 31.1446254536 | 382 | 504990 | -79.91 | 16.93 | 560.03 | 0.17 | 2.49 | 1596 |
| 2024-09-20 22:21:41.575 | MS1 | 121.4656595130 | 31.1446234150 | 382 | 504990 | -84.93 | 17.85 | 346.38 | 0.02 | 2.78 | 1585 |
| 2024-09-20 22:21:42.789 | MS1 | 121.4656754940 | 31.1446346108 | 382 | 504990 | -79.03 | 17.12 | 566.70 | 0.14 | 2.11 | 1560 |

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
| 3224149 | 1 | 121.4679078644 | 31.1524820695 | 162 | 3 | 4 | 46.3 | TDD | 740 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3249374 | 3 | 121.4673088902 | 31.1557860841 | 271 | 4 | 1 | 15.3 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3278017 | 4 | 121.4685114054 | 31.1556327854 | 44 | 13 | 5 | 30.3 | TDD | 623 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3279183 | 2 | 121.4656573848 | 31.1453840011 | 95 | 5 | 2 | 29.0 | TDD | 757 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.492 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.513 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.628 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.628 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.322 | NREventA3 | measId:2;ServCellPCI:181;Se... |
| 2024-09-20 22:21:36.322 | NREventA3 | measId:2;ServCellPCI:181;Se... |
| 2024-09-20 22:21:37.322 | NREventA3 | measId:2;ServCellPCI:181;Se... |
| 2024-09-20 22:21:39.822 | NRRRCReestablishAttempt | PCI:181 |
| 2024-09-20 22:21:39.836 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.849 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.974 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.974 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224149 | 1 | 16.0081 | 5.3416 | -116.0036 | 7.4367 | 127.6866 | 0.0149 | 0.0163 |
| 2024_09_20 22:00 | 3279183 | 2 | 17.2503 | 16.7163 | -116.4804 | 9.7640 | 176.4986 | 0.0071 | 0.0151 |
| 2024_09_20 22:00 | 3249374 | 3 | 9.7610 | 15.4810 | -117.9317 | 18.2737 | 194.0282 | 0.0097 | 0.1964 |
| 2024_09_20 22:00 | 3278017 | 4 | 19.8066 | 12.4843 | -117.8463 | 12.6223 | 173.9374 | 0.0184 | 0.0006 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416382_C3FCEB4C | 504990 | 382 | -88.1 | 504990 | 740 | -82.2 | 504990 | 757 | -81.9 | 504990 | 623 |
| MR_1774416382_9AB56058 | 504990 | 382 | -86.0 | 504990 | 740 | -82.3 | 504990 | 757 | -84.1 | 504990 | 623 |
| MR_1774416382_D02B6D4B | 504990 | 740 | -82.7 | 504990 | 382 | -86.9 | 504990 | 757 | -82.2 | 504990 | 623 |
| MR_1774416382_E0B4F8FD | 504990 | 382 | -84.8 | 504990 | 740 | -82.2 | 504990 | 757 | -84.0 | 504990 | 623 |
| MR_1774416382_6F96BDA4 | 504990 | 740 | -79.6 | 504990 | 382 | -87.8 | 504990 | 757 | -82.6 | 504990 | 623 |
| MR_1774416382_912AA94D | 504990 | 382 | -87.7 | 504990 | 740 | -79.7 | 504990 | 757 | -84.7 | 504990 | 623 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1458: `472c772e-28e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `472c772e-28eb-44d2-bbe7-08ec743728ca` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Lift the tilt angle  of 3238843_1 by 5 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1458] topology](images/train_1458.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3238843_1 by 5 degrees **← 정답**
- `C2`: Press down the tilt angle of 3217505_3 by 5 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase A3 Offset threshold for 3224516_2
- `C5`: Decrease transmission power for 3224516_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217505_3
- `C7`: Lift the tilt angle of 3217505_3 by 5 degrees
- `C8`: Increase transmission power for 3224516_2
- `C9`: Adjust the azimuth of 3217505_3 by 38 degrees
- `C10`: Check test server and transmission issues
- `C11`: Press down the tilt angle  of 3238843_1 by 5 degrees
- `C12`: Add neighbor relationship between 3238843_1 and 3224516_2
- `C13`: Decrease transmission power for 3217505_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217505_3
- `C15`: Add neighbor relationship between 3217505_3 and 3224516_2
- `C16`: Adjust the azimuth of 3238843_1 by 50 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224516_2
- `C18`: Increase transmission power for 3217505_3
- `C19`: Decrease A3 Offset threshold for 3224516_2
- `C20`: Increase A3 Offset threshold for 3217505_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224516_2
- `C22`: Decrease A3 Offset threshold for 3217505_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.417 | MS1 | 121.4656638898 | 31.1446291225 | 146 | 504990 | -88.05 | 15.65 | 366.58 | 0.18 | 2.11 | 1597 |
| 2024-09-20 22:21:32.201 | MS1 | 121.4656746510 | 31.1446330024 | 146 | 504990 | -91.33 | 16.28 | 512.93 | 0.19 | 2.88 | 1571 |
| 2024-09-20 22:21:33.884 | MS1 | 121.4656728019 | 31.1446364889 | 146 | 504990 | -90.15 | 14.64 | 535.74 | 0.08 | 2.84 | 1572 |
| 2024-09-20 22:21:34.124 | MS1 | 121.4656773262 | 31.1446237997 | 146 | 504990 | -89.23 | 16.22 | 90.40 | 0.03 | 2.61 | 1574 |
| 2024-09-20 22:21:35.305 | MS1 | 121.4656744842 | 31.1446268725 | 146 | 504990 | -86.26 | 17.14 | 43.99 | 0.16 | 2.72 | 1578 |
| 2024-09-20 22:21:36.644 | MS1 | 121.4656718486 | 31.1446344442 | 146 | 504990 | -91.12 | 13.97 | 92.88 | 0.04 | 2.37 | 1585 |
| 2024-09-20 22:21:37.309 | MS1 | 121.4656727461 | 31.1446227128 | 146 | 504990 | -90.21 | 11.30 | 66.51 | 0.12 | 2.97 | 1573 |
| 2024-09-20 22:21:38.783 | MS1 | 121.4656636410 | 31.1446208161 | 146 | 504990 | -92.59 | 8.53 | 93.94 | 0.00 | 2.78 | 1577 |
| 2024-09-20 22:21:39.248 | MS1 | 121.4656600079 | 31.1446305675 | 146 | 504990 | -93.56 | 11.09 | 102.54 | 0.14 | 2.58 | 1575 |
| 2024-09-20 22:21:40.449 | MS1 | 121.4656605621 | 31.1446274839 | 146 | 504990 | -91.17 | 9.67 | 527.78 | 0.05 | 2.97 | 1593 |
| 2024-09-20 22:21:41.226 | MS1 | 121.4656596179 | 31.1446333501 | 146 | 504990 | -92.46 | 9.16 | 387.65 | 0.14 | 2.53 | 1591 |
| 2024-09-20 22:21:42.176 | MS1 | 121.4656683484 | 31.1446371764 | 146 | 504990 | -90.05 | 8.20 | 338.36 | 0.16 | 2.72 | 1598 |

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
| 3215545 | 4 | 121.4759151620 | 31.1522871753 | 50 | 2 | 11 | 39.7 | TDD | 308 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3217505 | 3 | 121.4715556876 | 31.1534027512 | 248 | 4 | 5 | 25.7 | TDD | 146 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3224516 | 2 | 121.4714041392 | 31.1458864782 | 70 | 2 | 8 | 29.4 | TDD | 41 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3238843 | 1 | 121.4683984599 | 31.1494000068 | 47 | 4 | 12 | 35.6 | TDD | 152 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.080 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.098 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.237 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.237 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.974 | NREventA3 | measId:2;ServCellPCI:506;Se... |
| 2024-09-20 22:21:38.214 | NRHandoverAttempt | SourcePCI:506;SourceNR-ARFC... |
| 2024-09-20 22:21:38.258 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.273 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.377 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.377 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238843 | 1 | 16.0624 | 7.4251 | -114.5707 | 8.7419 | 98.3594 | 0.0193 | 0.0132 |
| 2024_09_20 22:00 | 3224516 | 2 | 19.5091 | 17.7149 | -115.0243 | 7.1162 | 155.5483 | 0.0036 | 0.0078 |
| 2024_09_20 22:00 | 3217505 | 3 | 89.2937 | 84.2048 | -116.7359 | 13.9703 | 164.5214 | 0.0065 | 0.0088 |
| 2024_09_20 22:00 | 3215545 | 4 | 17.1842 | 17.0942 | -115.1600 | 9.2885 | 173.2562 | 0.0110 | 0.0145 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412082_3318A7B8 | 504990 | 146 | -87.9 | 504990 | 41 | -94.6 | 504990 | 152 | -95.8 | 504990 | 308 |
| MR_1774412082_4D0320A9 | 504990 | 146 | -89.5 | 504990 | 41 | -97.4 | 504990 | 152 | -98.3 | 504990 | 308 |
| MR_1774412082_52BB9242 | 504990 | 146 | -89.0 | 504990 | 41 | -95.0 | 504990 | 152 | -96.9 | 504990 | 308 |
| MR_1774412082_96D50F2C | 504990 | 146 | -89.0 | 504990 | 41 | -96.4 | 504990 | 152 | -95.6 | 504990 | 308 |
| MR_1774412082_BCBE25A6 | 504990 | 146 | -89.0 | 504990 | 41 | -97.9 | 504990 | 152 | -98.7 | 504990 | 308 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1459: `e879367f-ffd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e879367f-ffda-4d5f-9ab4-5ce7ddeb5560` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1459] topology](images/train_1459.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3250577_2
- `C2`: Check test server and transmission issues **← 정답**
- `C3`: Add neighbor relationship between 3240953_1 and 3250577_2
- `C4`: Increase A3 Offset threshold for 3250577_2
- `C5`: Adjust the azimuth of 3250577_2 by 50 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250577_2
- `C7`: Adjust the azimuth of 3216023_4 by 50 degrees
- `C8`: Lift the tilt angle of 3216023_4 by 3 degrees
- `C9`: Decrease A3 Offset threshold for 3216023_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216023_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216023_4
- `C12`: Increase A3 Offset threshold for 3216023_4
- `C13`: Add neighbor relationship between 3216023_4 and 3250577_2
- `C14`: Increase transmission power for 3250577_2
- `C15`: Decrease transmission power for 3216023_4
- `C16`: Press down the tilt angle  of 3250577_2 by 5 degrees
- `C17`: Press down the tilt angle of 3216023_4 by 3 degrees
- `C18`: Lift the tilt angle  of 3250577_2 by 5 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase transmission power for 3216023_4
- `C21`: Decrease transmission power for 3250577_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250577_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.827 | MS1 | 121.4656668904 | 31.1446369562 | 270 | 504990 | -90.10 | 15.75 | 342.60 | 0.17 | 2.76 | 1584 |
| 2024-09-20 22:21:32.248 | MS1 | 121.4656589149 | 31.1446331878 | 270 | 504990 | -86.78 | 17.19 | 361.68 | 0.04 | 2.74 | 1572 |
| 2024-09-20 22:21:33.246 | MS1 | 121.4656659074 | 31.1446305010 | 270 | 504990 | -85.06 | 17.02 | 416.09 | 0.13 | 2.16 | 1586 |
| 2024-09-20 22:21:34.171 | MS1 | 121.4656693786 | 31.1446335670 | 270 | 504990 | -91.07 | 17.70 | 90.69 | 0.16 | 2.18 | 488 |
| 2024-09-20 22:21:35.964 | MS1 | 121.4656606278 | 31.1446356785 | 270 | 504990 | -86.52 | 12.96 | 94.94 | 0.02 | 2.24 | 396 |
| 2024-09-20 22:21:36.896 | MS1 | 121.4656622455 | 31.1446263478 | 270 | 504990 | -90.05 | 14.24 | 83.87 | 0.06 | 2.87 | 447 |
| 2024-09-20 22:21:37.571 | MS1 | 121.4656669788 | 31.1446285864 | 270 | 504990 | -93.40 | 7.29 | 59.98 | 0.11 | 2.54 | 482 |
| 2024-09-20 22:21:38.164 | MS1 | 121.4656659582 | 31.1446181888 | 270 | 504990 | -91.44 | 10.60 | 97.86 | 0.13 | 2.10 | 450 |
| 2024-09-20 22:21:39.139 | MS1 | 121.4656767512 | 31.1446265827 | 270 | 504990 | -90.87 | 8.06 | 49.08 | 0.13 | 2.38 | 409 |
| 2024-09-20 22:21:40.796 | MS1 | 121.4656665786 | 31.1446365234 | 270 | 504990 | -91.94 | 11.58 | 557.30 | 0.06 | 2.94 | 1577 |
| 2024-09-20 22:21:41.735 | MS1 | 121.4656696651 | 31.1446221058 | 270 | 504990 | -89.13 | 12.74 | 440.66 | 0.08 | 2.86 | 1575 |
| 2024-09-20 22:21:42.310 | MS1 | 121.4656690834 | 31.1446272893 | 270 | 504990 | -93.04 | 9.10 | 469.57 | 0.09 | 2.88 | 1572 |

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
| 3216023 | 4 | 121.4702791884 | 31.1538390155 | 325 | 0 | 0 | 49.3 | TDD | 270 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3240953 | 1 | 121.4652106364 | 31.1443277423 | 43 | 1 | 6 | 33.1 | TDD | 431 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3250577 | 2 | 121.4749752328 | 31.1515333142 | 329 | 3 | 4 | 42.3 | TDD | 451 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3256083 | 3 | 121.4708964089 | 31.1480391156 | 234 | 3 | 12 | 46.7 | TDD | 222 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.611 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.627 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.768 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.768 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.415 | NREventA3 | measId:2;ServCellPCI:260;Se... |
| 2024-09-20 22:21:38.655 | NRHandoverAttempt | SourcePCI:260;SourceNR-ARFC... |
| 2024-09-20 22:21:38.696 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.708 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.829 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.829 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240953 | 1 | 13.9686 | 15.5370 | -117.7705 | 8.8430 | 199.3474 | 0.0119 | 0.0092 |
| 2024_09_20 22:00 | 3250577 | 2 | 15.2965 | 6.8145 | -116.7428 | 15.0605 | 195.9218 | 0.0171 | 0.0135 |
| 2024_09_20 22:00 | 3256083 | 3 | 8.0571 | 12.2272 | -115.7780 | 19.7411 | 125.1495 | 0.0022 | 0.0060 |
| 2024_09_20 22:00 | 3216023 | 4 | 17.7847 | 5.1117 | -117.7236 | 17.1621 | 87.9597 | 0.0002 | 0.0163 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413239_44086B30 | 504990 | 270 | -91.4 | 504990 | 451 | -94.8 | 504990 | 431 | -98.9 | 504990 | 222 |
| MR_1774413239_064E4167 | 504990 | 270 | -93.1 | 504990 | 451 | -97.8 | 504990 | 431 | -98.9 | 504990 | 222 |
| MR_1774413239_0E89F07A | 504990 | 270 | -89.5 | 504990 | 451 | -96.9 | 504990 | 431 | -101.4 | 504990 | 222 |
| MR_1774413239_364E6B66 | 504990 | 270 | -92.0 | 504990 | 451 | -97.7 | 504990 | 431 | -98.3 | 504990 | 222 |
| MR_1774413239_6B1CD3FC | 504990 | 270 | -89.9 | 504990 | 451 | -97.0 | 504990 | 431 | -98.3 | 504990 | 222 |
| MR_1774413239_AF9EAAD9 | 504990 | 270 | -92.0 | 504990 | 451 | -98.1 | 504990 | 431 | -101.9 | 504990 | 222 |

> *... 2개 열 생략 (전체 14열)*

---
