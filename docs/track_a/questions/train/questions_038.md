# Track A 문제 분석 — train[370]~train[379]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[370] ~ train[379] (10개)

## 목차

1. [문제 370: `e7370bdc-c91...`](#370) — single-answer, 정답: C12
2. [문제 371: `190f63fa-d8b...`](#371) — single-answer, 정답: C2
3. [문제 372: `39f289c2-2d7...`](#372) — single-answer, 정답: C16
4. [문제 373: `282739f9-8fb...`](#373) — single-answer, 정답: C4
5. [문제 374: `40853732-340...`](#374) — single-answer, 정답: C15
6. [문제 375: `ec76b540-cc3...`](#375) — multiple-answer, 정답: C1|C6|C8|C21
7. [문제 376: `17ed83a9-3ae...`](#376) — multiple-answer, 정답: C4|C14
8. [문제 377: `4c369ece-197...`](#377) — multiple-answer, 정답: C1|C16
9. [문제 378: `3ecb919e-2cc...`](#378) — single-answer, 정답: C16
10. [문제 379: `efe35e97-980...`](#379) — single-answer, 정답: C4

---

### 문제 370: `e7370bdc-c91...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e7370bdc-c917-472b-a4fc-c7b6a9dfe24f` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Add neighbor relationship between 3272669_4 and 3211813_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[370] topology](images/train_0370.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3211813_3
- `C2`: Decrease transmission power for 3272669_4
- `C3`: Increase transmission power for 3272669_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272669_4
- `C5`: Press down the tilt angle  of 3211813_3 by 3 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211813_3
- `C7`: Add neighbor relationship between 3242517_2 and 3211813_3
- `C8`: Press down the tilt angle of 3272669_4 by 10 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211813_3
- `C10`: Increase A3 Offset threshold for 3211813_3
- `C11`: Lift the tilt angle of 3272669_4 by 10 degrees
- `C12`: Add neighbor relationship between 3272669_4 and 3211813_3 **← 정답**
- `C13`: Increase A3 Offset threshold for 3272669_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272669_4
- `C15`: Check test server and transmission issues
- `C16`: Decrease A3 Offset threshold for 3272669_4
- `C17`: Adjust the azimuth of 3272669_4 by 30 degrees
- `C18`: Decrease A3 Offset threshold for 3211813_3
- `C19`: Increase transmission power for 3211813_3
- `C20`: Lift the tilt angle  of 3211813_3 by 3 degrees
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Adjust the azimuth of 3211813_3 by 13 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.395 | MS1 | 121.4656608843 | 31.1446223081 | 485 | 504990 | -78.68 | 12.97 | 508.63 | 0.09 | 2.52 | 1574 |
| 2024-09-20 22:21:32.475 | MS1 | 121.4656610122 | 31.1446196230 | 485 | 504990 | -81.84 | 17.83 | 373.65 | 0.00 | 2.85 | 1577 |
| 2024-09-20 22:21:33.167 | MS1 | 121.4656644207 | 31.1446328092 | 485 | 504990 | -77.12 | 12.07 | 433.73 | 0.14 | 2.51 | 1597 |
| 2024-09-20 22:21:34.750 | MS1 | 121.4656587256 | 31.1446246405 | 485 | 504990 | -92.61 | -2.77 | 40.04 | 0.19 | 1.36 | 1594 |
| 2024-09-20 22:21:35.591 | MS1 | 121.4656643980 | 31.1446248830 | 485 | 504990 | -91.97 | -1.71 | 67.55 | 0.11 | 1.36 | 1567 |
| 2024-09-20 22:21:36.870 | MS1 | 121.4656761088 | 31.1446183902 | 485 | 504990 | -87.75 | -0.50 | 49.34 | 0.01 | 1.38 | 1587 |
| 2024-09-20 22:21:37.449 | MS1 | 121.4656682045 | 31.1446366633 | 485 | 504990 | -91.59 | -1.36 | 48.69 | 0.19 | 1.05 | 1578 |
| 2024-09-20 22:21:38.908 | MS1 | 121.4656585388 | 31.1446294355 | 485 | 504990 | -76.07 | 13.31 | 574.90 | 0.08 | 1.02 | 1576 |
| 2024-09-20 22:21:39.907 | MS1 | 121.4656774170 | 31.1446332124 | 485 | 504990 | -80.30 | 16.38 | 356.03 | 0.01 | 1.24 | 1592 |
| 2024-09-20 22:21:40.592 | MS1 | 121.4656709224 | 31.1446258453 | 485 | 504990 | -77.31 | 12.75 | 499.16 | 0.12 | 2.13 | 1579 |
| 2024-09-20 22:21:41.902 | MS1 | 121.4656684131 | 31.1446344498 | 485 | 504990 | -76.22 | 12.05 | 473.23 | 0.13 | 2.63 | 1576 |
| 2024-09-20 22:21:42.865 | MS1 | 121.4656708727 | 31.1446184350 | 485 | 504990 | -78.25 | 12.72 | 391.60 | 0.05 | 2.95 | 1568 |

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
| 3211813 | 3 | 121.4648729883 | 31.1515989626 | 187 | 2 | 5 | 20.0 | TDD | 59 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3219477 | 1 | 121.4736893145 | 31.1549686957 | 305 | 15 | 5 | 41.9 | TDD | 681 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3242517 | 2 | 121.4674377913 | 31.1533313178 | 214 | 4 | 1 | 35.2 | TDD | 82 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3272669 | 4 | 121.4655697852 | 31.1472726924 | 208 | 11 | 1 | 46.9 | TDD | 485 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.401 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.422 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.570 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.570 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.273 | NREventA3 | measId:2;ServCellPCI:1006;S... |
| 2024-09-20 22:21:36.273 | NREventA3 | measId:2;ServCellPCI:1006;S... |
| 2024-09-20 22:21:37.273 | NREventA3 | measId:2;ServCellPCI:1006;S... |
| 2024-09-20 22:21:39.773 | NRRRCReestablishAttempt | PCI:1006 |
| 2024-09-20 22:21:39.783 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.798 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.934 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.934 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219477 | 1 | 17.7957 | 15.9921 | -117.3062 | 5.3397 | 90.0406 | 0.0139 | 0.0038 |
| 2024_09_20 22:00 | 3242517 | 2 | 11.1544 | 13.1511 | -114.2462 | 9.7046 | 130.4504 | 0.0054 | 0.0044 |
| 2024_09_20 22:00 | 3211813 | 3 | 7.5849 | 10.5004 | -115.0489 | 11.8492 | 160.7351 | 0.0196 | 0.0044 |
| 2024_09_20 22:00 | 3272669 | 4 | 13.4566 | 7.4533 | -114.4785 | 5.5891 | 177.9264 | 0.0039 | 0.1223 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414026_99481A52 | 504990 | 59 | -88.5 | 504990 | 485 | -94.0 | 504990 | 82 | -91.2 | 504990 | 681 |
| MR_1774414026_F7F70FB7 | 504990 | 59 | -89.7 | 504990 | 485 | -91.6 | 504990 | 82 | -89.6 | 504990 | 681 |
| MR_1774414026_A6B35F81 | 504990 | 485 | -91.3 | 504990 | 59 | -88.3 | 504990 | 82 | -90.5 | 504990 | 681 |
| MR_1774414026_CAE08072 | 504990 | 59 | -87.0 | 504990 | 485 | -91.3 | 504990 | 82 | -88.7 | 504990 | 681 |
| MR_1774414026_6661CC9D | 504990 | 485 | -94.1 | 504990 | 59 | -88.3 | 504990 | 82 | -88.4 | 504990 | 681 |
| MR_1774414026_832A9C9D | 504990 | 485 | -92.2 | 504990 | 59 | -89.8 | 504990 | 82 | -89.0 | 504990 | 681 |
| MR_1774414026_EEEBA204 | 504990 | 59 | -90.1 | 504990 | 485 | -93.6 | 504990 | 82 | -91.5 | 504990 | 681 |
| MR_1774414026_81E8129D | 504990 | 59 | -89.8 | 504990 | 485 | -94.5 | 504990 | 82 | -90.8 | 504990 | 681 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 371: `190f63fa-d8b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `190f63fa-d8bf-4b8d-91ee-4cb54520e79d` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Add neighbor relationship between 3257089_4 and 3246948_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[371] topology](images/train_0371.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3257089_4
- `C2`: Add neighbor relationship between 3257089_4 and 3246948_3 **← 정답**
- `C3`: Lift the tilt angle of 3257089_4 by 4 degrees
- `C4`: Increase transmission power for 3246948_3
- `C5`: Increase A3 Offset threshold for 3257089_4
- `C6`: Decrease A3 Offset threshold for 3257089_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257089_4
- `C8`: Check test server and transmission issues
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease transmission power for 3246948_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246948_3
- `C12`: Press down the tilt angle  of 3246948_3 by 3 degrees
- `C13`: Add neighbor relationship between 3242358_2 and 3246948_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257089_4
- `C15`: Press down the tilt angle of 3257089_4 by 4 degrees
- `C16`: Adjust the azimuth of 3246948_3 by 50 degrees
- `C17`: Decrease A3 Offset threshold for 3246948_3
- `C18`: Lift the tilt angle  of 3246948_3 by 3 degrees
- `C19`: Adjust the azimuth of 3257089_4 by 50 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246948_3
- `C21`: Increase A3 Offset threshold for 3246948_3
- `C22`: Increase transmission power for 3257089_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.601 | MS1 | 121.4656600644 | 31.1446299701 | 807 | 504990 | -83.02 | 14.03 | 410.22 | 0.18 | 2.38 | 1560 |
| 2024-09-20 22:21:32.518 | MS1 | 121.4656718406 | 31.1446276457 | 807 | 504990 | -76.83 | 16.08 | 439.09 | 0.13 | 2.89 | 1574 |
| 2024-09-20 22:21:33.737 | MS1 | 121.4656623955 | 31.1446275295 | 807 | 504990 | -80.63 | 12.50 | 589.52 | 0.02 | 2.54 | 1561 |
| 2024-09-20 22:21:34.102 | MS1 | 121.4656666712 | 31.1446355233 | 807 | 504990 | -94.74 | -2.35 | 75.00 | 0.17 | 1.09 | 1592 |
| 2024-09-20 22:21:35.418 | MS1 | 121.4656663552 | 31.1446287920 | 807 | 504990 | -92.04 | -1.84 | 64.55 | 0.09 | 1.04 | 1595 |
| 2024-09-20 22:21:36.787 | MS1 | 121.4656662126 | 31.1446330977 | 807 | 504990 | -93.72 | -2.15 | 59.66 | 0.06 | 1.34 | 1592 |
| 2024-09-20 22:21:37.840 | MS1 | 121.4656661458 | 31.1446363670 | 807 | 504990 | -91.10 | -1.20 | 74.11 | 0.00 | 1.00 | 1561 |
| 2024-09-20 22:21:38.273 | MS1 | 121.4656623932 | 31.1446274032 | 807 | 504990 | -78.91 | 13.61 | 443.63 | 0.13 | 1.28 | 1567 |
| 2024-09-20 22:21:39.686 | MS1 | 121.4656643074 | 31.1446288566 | 807 | 504990 | -84.42 | 15.65 | 428.47 | 0.19 | 1.06 | 1577 |
| 2024-09-20 22:21:40.184 | MS1 | 121.4656611862 | 31.1446255518 | 807 | 504990 | -76.98 | 13.31 | 386.35 | 0.01 | 2.48 | 1567 |
| 2024-09-20 22:21:41.603 | MS1 | 121.4656738449 | 31.1446215129 | 807 | 504990 | -79.83 | 12.29 | 343.17 | 0.20 | 2.09 | 1576 |
| 2024-09-20 22:21:42.173 | MS1 | 121.4656673942 | 31.1446208060 | 807 | 504990 | -78.29 | 15.13 | 475.00 | 0.14 | 2.73 | 1572 |

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
| 3233072 | 1 | 121.4653782425 | 31.1462504956 | 27 | 0 | 4 | 42.3 | TDD | 897 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3242358 | 2 | 121.4759040885 | 31.1448500916 | 253 | 7 | 6 | 23.3 | TDD | 722 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3246948 | 3 | 121.4699991386 | 31.1517577977 | 257 | 2 | 0 | 17.3 | TDD | 958 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3257089 | 4 | 121.4672312461 | 31.1525727270 | 352 | 2 | 0 | 36.2 | TDD | 807 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.483 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.595 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.595 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.291 | NREventA3 | measId:2;ServCellPCI:891;Se... |
| 2024-09-20 22:21:36.291 | NREventA3 | measId:2;ServCellPCI:891;Se... |
| 2024-09-20 22:21:37.291 | NREventA3 | measId:2;ServCellPCI:891;Se... |
| 2024-09-20 22:21:39.791 | NRRRCReestablishAttempt | PCI:891 |
| 2024-09-20 22:21:39.807 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.817 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.963 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.963 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233072 | 1 | 10.4619 | 14.3908 | -117.7882 | 17.2151 | 97.6432 | 0.0187 | 0.0068 |
| 2024_09_20 22:00 | 3242358 | 2 | 17.5747 | 19.3045 | -116.6335 | 8.1095 | 88.2445 | 0.0041 | 0.0184 |
| 2024_09_20 22:00 | 3246948 | 3 | 17.8509 | 14.1261 | -114.7814 | 13.7457 | 148.4308 | 0.0186 | 0.0040 |
| 2024_09_20 22:00 | 3257089 | 4 | 13.4480 | 17.2058 | -116.8580 | 9.1316 | 80.1393 | 0.0043 | 0.1795 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412328_53CAEFB7 | 504990 | 807 | -92.8 | 504990 | 958 | -89.4 | 504990 | 722 | -95.9 | 504990 | 897 |
| MR_1774412328_C6521D7A | 504990 | 807 | -94.7 | 504990 | 958 | -91.3 | 504990 | 722 | -97.9 | 504990 | 897 |
| MR_1774412328_4A178AC9 | 504990 | 958 | -91.2 | 504990 | 807 | -93.0 | 504990 | 722 | -96.9 | 504990 | 897 |
| MR_1774412328_011D8425 | 504990 | 807 | -94.8 | 504990 | 958 | -92.1 | 504990 | 722 | -95.5 | 504990 | 897 |
| MR_1774412328_525EFA3A | 504990 | 958 | -88.4 | 504990 | 807 | -96.0 | 504990 | 722 | -97.9 | 504990 | 897 |
| MR_1774412328_9046FB3E | 504990 | 958 | -91.9 | 504990 | 807 | -93.4 | 504990 | 722 | -95.9 | 504990 | 897 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 372: `39f289c2-2d7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `39f289c2-2d78-423c-acf6-a19066e3ae9f` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease A3 Offset threshold for 3251717_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[372] topology](images/train_0372.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3251717_4 by 5 degrees
- `C2`: Lift the tilt angle of 3251717_4 by 5 degrees
- `C3`: Adjust the azimuth of 3251717_4 by 37 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251717_4
- `C5`: Add neighbor relationship between 3251717_4 and 3255662_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251717_4
- `C7`: Decrease transmission power for 3255662_1
- `C8`: Add neighbor relationship between 3217852_3 and 3255662_1
- `C9`: Increase A3 Offset threshold for 3255662_1
- `C10`: Increase transmission power for 3255662_1
- `C11`: Increase A3 Offset threshold for 3251717_4
- `C12`: Lift the tilt angle  of 3255662_1 by 10 degrees
- `C13`: Check test server and transmission issues
- `C14`: Increase transmission power for 3251717_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255662_1
- `C16`: Decrease A3 Offset threshold for 3251717_4 **← 정답**
- `C17`: Press down the tilt angle  of 3255662_1 by 10 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Adjust the azimuth of 3255662_1 by 15 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255662_1
- `C21`: Decrease A3 Offset threshold for 3255662_1
- `C22`: Decrease transmission power for 3251717_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.256 | MS1 | 121.4656635605 | 31.1446317171 | 165 | 504990 | -77.56 | 12.54 | 340.97 | 0.12 | 2.02 | 1563 |
| 2024-09-20 22:21:32.222 | MS1 | 121.4656729573 | 31.1446240406 | 165 | 504990 | -82.22 | 16.07 | 569.32 | 0.04 | 2.88 | 1595 |
| 2024-09-20 22:21:33.464 | MS1 | 121.4656685805 | 31.1446296591 | 165 | 504990 | -79.08 | 13.82 | 430.51 | 0.08 | 2.58 | 1567 |
| 2024-09-20 22:21:34.666 | MS1 | 121.4656737079 | 31.1446325641 | 165 | 504990 | -83.09 | -1.89 | 38.70 | 0.00 | 1.21 | 1588 |
| 2024-09-20 22:21:35.540 | MS1 | 121.4656751167 | 31.1446202287 | 165 | 504990 | -85.13 | -0.56 | 44.84 | 0.02 | 1.05 | 1563 |
| 2024-09-20 22:21:36.159 | MS1 | 121.4656638401 | 31.1446336065 | 165 | 504990 | -88.98 | -2.61 | 33.26 | 0.01 | 1.30 | 1582 |
| 2024-09-20 22:21:37.827 | MS1 | 121.4656641806 | 31.1446247471 | 165 | 504990 | -83.21 | -0.28 | 32.30 | 0.16 | 1.16 | 1564 |
| 2024-09-20 22:21:38.999 | MS1 | 121.4656591434 | 31.1446181149 | 165 | 504990 | -90.25 | -3.46 | 68.47 | 0.19 | 1.01 | 1579 |
| 2024-09-20 22:21:39.959 | MS1 | 121.4656752472 | 31.1446183557 | 337 | 504990 | -79.39 | 16.56 | 279.38 | 0.19 | 1.35 | 1575 |
| 2024-09-20 22:21:40.161 | MS1 | 121.4656673532 | 31.1446283541 | 337 | 504990 | -84.60 | 17.75 | 470.87 | 0.10 | 2.16 | 1586 |
| 2024-09-20 22:21:41.771 | MS1 | 121.4656719936 | 31.1446256098 | 337 | 504990 | -75.11 | 17.68 | 392.96 | 0.06 | 2.60 | 1568 |
| 2024-09-20 22:21:42.625 | MS1 | 121.4656697111 | 31.1446326687 | 337 | 504990 | -78.73 | 15.85 | 404.56 | 0.07 | 2.78 | 1576 |

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
| 3217852 | 3 | 121.4734260106 | 31.1537795381 | 128 | 9 | 1 | 36.0 | TDD | 876 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3251717 | 4 | 121.4718272211 | 31.1495451785 | 264 | 3 | 1 | 28.9 | TDD | 165 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3255662 | 1 | 121.4747432806 | 31.1442152740 | 288 | 13 | 10 | 20.6 | TDD | 337 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3265566 | 2 | 121.4645842377 | 31.1443032331 | 331 | 14 | 1 | 32.6 | TDD | 35 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.175 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.199 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.331 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.331 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.019 | NREventA3 | measId:2;ServCellPCI:175;Se... |
| 2024-09-20 22:21:38.259 | NRHandoverAttempt | SourcePCI:175;SourceNR-ARFC... |
| 2024-09-20 22:21:38.289 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.300 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.409 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.409 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255662 | 1 | 8.6425 | 17.5644 | -115.9489 | 15.2540 | 106.5212 | 0.0066 | 0.0155 |
| 2024_09_20 22:00 | 3265566 | 2 | 9.8135 | 9.2440 | -114.0838 | 13.7202 | 146.1788 | 0.0004 | 0.0157 |
| 2024_09_20 22:00 | 3217852 | 3 | 17.1640 | 14.9344 | -117.7193 | 6.7785 | 135.0607 | 0.0115 | 0.0002 |
| 2024_09_20 22:00 | 3251717 | 4 | 16.2635 | 6.4582 | -114.6187 | 11.8366 | 163.2429 | 0.0089 | 0.1056 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412399_86BE0585 | 504990 | 337 | -78.0 | 504990 | 165 | -83.8 | 504990 | 876 | -81.9 | 504990 | 35 |
| MR_1774412399_C3A95784 | 504990 | 165 | -82.9 | 504990 | 337 | -78.2 | 504990 | 876 | -81.4 | 504990 | 35 |
| MR_1774412399_952483BD | 504990 | 165 | -81.4 | 504990 | 337 | -75.9 | 504990 | 876 | -79.6 | 504990 | 35 |
| MR_1774412399_1CA4E80B | 504990 | 165 | -82.8 | 504990 | 337 | -76.3 | 504990 | 876 | -80.7 | 504990 | 35 |
| MR_1774412399_2C5D21F6 | 504990 | 165 | -82.8 | 504990 | 337 | -76.5 | 504990 | 876 | -81.5 | 504990 | 35 |
| MR_1774412399_FF5B2B4C | 504990 | 165 | -82.1 | 504990 | 337 | -76.3 | 504990 | 876 | -81.7 | 504990 | 35 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 373: `282739f9-8fb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `282739f9-8fb0-41b8-96fc-f7d459f5c573` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Decrease A3 Offset threshold for 3258012_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[373] topology](images/train_0373.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease A3 Offset threshold for 3272981_3
- `C4`: Decrease A3 Offset threshold for 3258012_1 **← 정답**
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258012_1
- `C6`: Increase transmission power for 3258012_1
- `C7`: Decrease transmission power for 3272981_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258012_1
- `C9`: Adjust the azimuth of 3258012_1 by 50 degrees
- `C10`: Adjust the azimuth of 3272981_3 by 50 degrees
- `C11`: Press down the tilt angle of 3258012_1 by 10 degrees
- `C12`: Add neighbor relationship between 3215164_2 and 3272981_3
- `C13`: Lift the tilt angle  of 3272981_3 by 2 degrees
- `C14`: Press down the tilt angle  of 3272981_3 by 2 degrees
- `C15`: Increase A3 Offset threshold for 3272981_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272981_3
- `C17`: Add neighbor relationship between 3258012_1 and 3272981_3
- `C18`: Increase A3 Offset threshold for 3258012_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272981_3
- `C20`: Decrease transmission power for 3258012_1
- `C21`: Increase transmission power for 3272981_3
- `C22`: Lift the tilt angle of 3258012_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.459 | MS1 | 121.4656675395 | 31.1446223609 | 585 | 504990 | -83.50 | 16.46 | 358.37 | 0.02 | 2.49 | 1579 |
| 2024-09-20 22:21:32.558 | MS1 | 121.4656630579 | 31.1446357840 | 585 | 504990 | -80.82 | 13.84 | 482.60 | 0.17 | 2.19 | 1568 |
| 2024-09-20 22:21:33.391 | MS1 | 121.4656657688 | 31.1446310769 | 585 | 504990 | -75.69 | 14.88 | 457.64 | 0.18 | 2.03 | 1574 |
| 2024-09-20 22:21:34.767 | MS1 | 121.4656737099 | 31.1446223987 | 585 | 504990 | -87.08 | -0.20 | 32.44 | 0.11 | 1.43 | 1591 |
| 2024-09-20 22:21:35.195 | MS1 | 121.4656751935 | 31.1446189841 | 585 | 504990 | -83.31 | -1.98 | 60.57 | 0.15 | 1.02 | 1560 |
| 2024-09-20 22:21:36.405 | MS1 | 121.4656690557 | 31.1446367451 | 585 | 504990 | -83.64 | -2.04 | 58.67 | 0.14 | 1.02 | 1590 |
| 2024-09-20 22:21:37.129 | MS1 | 121.4656659999 | 31.1446233381 | 585 | 504990 | -86.54 | -3.05 | 54.38 | 0.04 | 1.03 | 1586 |
| 2024-09-20 22:21:38.595 | MS1 | 121.4656635454 | 31.1446209120 | 585 | 504990 | -84.81 | -1.60 | 66.23 | 0.08 | 1.49 | 1589 |
| 2024-09-20 22:21:39.253 | MS1 | 121.4656779190 | 31.1446311418 | 950 | 504990 | -80.69 | 15.23 | 269.59 | 0.17 | 1.49 | 1581 |
| 2024-09-20 22:21:40.352 | MS1 | 121.4656616472 | 31.1446197376 | 950 | 504990 | -82.83 | 17.74 | 590.67 | 0.07 | 2.01 | 1586 |
| 2024-09-20 22:21:41.707 | MS1 | 121.4656666485 | 31.1446275117 | 950 | 504990 | -77.09 | 16.58 | 421.55 | 0.17 | 2.96 | 1571 |
| 2024-09-20 22:21:42.991 | MS1 | 121.4656779997 | 31.1446182641 | 950 | 504990 | -77.58 | 14.15 | 339.29 | 0.09 | 2.48 | 1587 |

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
| 3215164 | 2 | 121.4705176290 | 31.1498351513 | 126 | 3 | 5 | 46.8 | TDD | 498 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3245376 | 4 | 121.4742384014 | 31.1471005111 | 230 | 14 | 2 | 36.0 | TDD | 471 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3258012 | 1 | 121.4689730775 | 31.1453653080 | 64 | 3 | 10 | 47.2 | TDD | 585 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3272981 | 3 | 121.4649364450 | 31.1503334458 | 332 | 0 | 9 | 17.2 | TDD | 950 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.362 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.383 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.531 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.531 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.168 | NREventA3 | measId:2;ServCellPCI:484;Se... |
| 2024-09-20 22:21:38.408 | NRHandoverAttempt | SourcePCI:484;SourceNR-ARFC... |
| 2024-09-20 22:21:38.449 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.459 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.593 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.593 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258012 | 1 | 11.4062 | 11.3535 | -114.6615 | 15.7643 | 103.7339 | 0.0007 | 0.1127 |
| 2024_09_20 22:00 | 3215164 | 2 | 8.9407 | 13.8521 | -115.3753 | 19.5476 | 184.9664 | 0.0016 | 0.0156 |
| 2024_09_20 22:00 | 3272981 | 3 | 16.1733 | 6.9179 | -115.5400 | 9.3947 | 114.7329 | 0.0144 | 0.0138 |
| 2024_09_20 22:00 | 3245376 | 4 | 14.4018 | 13.3950 | -117.3501 | 12.6806 | 157.0839 | 0.0174 | 0.0118 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417220_A9E1F121 | 504990 | 585 | -85.6 | 504990 | 950 | -81.5 | 504990 | 498 | -86.8 | 504990 | 471 |
| MR_1774417220_DC412637 | 504990 | 950 | -82.9 | 504990 | 585 | -88.3 | 504990 | 498 | -84.8 | 504990 | 471 |
| MR_1774417220_3FE7F4DD | 504990 | 950 | -82.0 | 504990 | 585 | -86.2 | 504990 | 498 | -88.0 | 504990 | 471 |
| MR_1774417220_11481978 | 504990 | 585 | -86.0 | 504990 | 950 | -83.0 | 504990 | 498 | -86.9 | 504990 | 471 |
| MR_1774417220_27735FB9 | 504990 | 950 | -81.3 | 504990 | 585 | -86.0 | 504990 | 498 | -85.4 | 504990 | 471 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 374: `40853732-340...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `40853732-340c-4445-bc46-d510dc905b4e` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Lift the tilt angle  of 3276446_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[374] topology](images/train_0374.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3223837_2 by 5 degrees
- `C2`: Lift the tilt angle of 3223837_2 by 5 degrees
- `C3`: Adjust the azimuth of 3276446_3 by 6 degrees
- `C4`: Decrease transmission power for 3223837_2
- `C5`: Increase A3 Offset threshold for 3233558_1
- `C6`: Add neighbor relationship between 3276446_3 and 3233558_1
- `C7`: Check test server and transmission issues
- `C8`: Increase transmission power for 3223837_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233558_1
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease A3 Offset threshold for 3233558_1
- `C12`: Press down the tilt angle  of 3276446_3 by 10 degrees
- `C13`: Adjust the azimuth of 3223837_2 by 12 degrees
- `C14`: Decrease A3 Offset threshold for 3223837_2
- `C15`: Lift the tilt angle  of 3276446_3 by 10 degrees **← 정답**
- `C16`: Increase A3 Offset threshold for 3223837_2
- `C17`: Increase transmission power for 3233558_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223837_2
- `C19`: Add neighbor relationship between 3223837_2 and 3233558_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223837_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233558_1
- `C22`: Decrease transmission power for 3233558_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.263 | MS1 | 121.4656761154 | 31.1446209144 | 931 | 504990 | -87.12 | 16.40 | 380.85 | 0.03 | 2.67 | 1583 |
| 2024-09-20 22:21:32.728 | MS1 | 121.4656617560 | 31.1446257261 | 931 | 504990 | -91.92 | 16.09 | 474.89 | 0.06 | 2.53 | 1585 |
| 2024-09-20 22:21:33.221 | MS1 | 121.4656704955 | 31.1446218879 | 931 | 504990 | -89.45 | 16.39 | 558.49 | 0.14 | 2.72 | 1599 |
| 2024-09-20 22:21:34.981 | MS1 | 121.4656616745 | 31.1446310194 | 931 | 504990 | -87.52 | 12.86 | 72.45 | 0.02 | 2.31 | 1575 |
| 2024-09-20 22:21:35.583 | MS1 | 121.4656759790 | 31.1446263682 | 931 | 504990 | -90.92 | 15.56 | 69.97 | 0.15 | 2.95 | 1594 |
| 2024-09-20 22:21:36.905 | MS1 | 121.4656730909 | 31.1446212906 | 931 | 504990 | -87.00 | 17.29 | 56.90 | 0.05 | 2.64 | 1588 |
| 2024-09-20 22:21:37.213 | MS1 | 121.4656600714 | 31.1446348211 | 931 | 504990 | -89.65 | 7.84 | 93.49 | 0.08 | 2.10 | 1562 |
| 2024-09-20 22:21:38.947 | MS1 | 121.4656651643 | 31.1446209212 | 931 | 504990 | -93.28 | 8.52 | 64.79 | 0.17 | 2.05 | 1564 |
| 2024-09-20 22:21:39.301 | MS1 | 121.4656670245 | 31.1446373652 | 931 | 504990 | -92.52 | 11.05 | 66.06 | 0.06 | 2.54 | 1573 |
| 2024-09-20 22:21:40.937 | MS1 | 121.4656755662 | 31.1446267862 | 931 | 504990 | -89.13 | 11.55 | 456.47 | 0.02 | 2.58 | 1572 |
| 2024-09-20 22:21:41.885 | MS1 | 121.4656689992 | 31.1446352141 | 931 | 504990 | -90.60 | 11.88 | 438.83 | 0.03 | 2.65 | 1597 |
| 2024-09-20 22:21:42.351 | MS1 | 121.4656585557 | 31.1446368172 | 931 | 504990 | -90.66 | 9.75 | 399.56 | 0.15 | 2.40 | 1591 |

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
| 3223837 | 2 | 121.4658345965 | 31.1549417574 | 193 | 4 | 7 | 26.6 | TDD | 931 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3233558 | 1 | 121.4668142014 | 31.1466828025 | 199 | 3 | 11 | 46.6 | TDD | 566 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3276446 | 3 | 121.4746234182 | 31.1515862813 | 346 | 2 | 6 | 34.5 | TDD | 468 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3278574 | 4 | 121.4684483349 | 31.1540843320 | 322 | 4 | 7 | 48.0 | TDD | 214 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.329 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.345 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.456 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.456 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.144 | NREventA3 | measId:2;ServCellPCI:129;Se... |
| 2024-09-20 22:21:38.384 | NRHandoverAttempt | SourcePCI:129;SourceNR-ARFC... |
| 2024-09-20 22:21:38.433 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.444 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.558 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.558 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233558 | 1 | 16.2963 | 15.3662 | -115.0831 | 18.5435 | 169.9651 | 0.0040 | 0.0046 |
| 2024_09_20 22:00 | 3223837 | 2 | 79.6427 | 75.0761 | -115.5655 | 16.2703 | 196.6185 | 0.0048 | 0.0137 |
| 2024_09_20 22:00 | 3276446 | 3 | 8.0320 | 13.1349 | -115.7452 | 10.2517 | 98.5860 | 0.0151 | 0.0014 |
| 2024_09_20 22:00 | 3278574 | 4 | 12.7234 | 12.4733 | -116.4306 | 8.7703 | 120.4431 | 0.0068 | 0.0182 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413733_E1408274 | 504990 | 931 | -88.8 | 504990 | 566 | -93.5 | 504990 | 468 | -94.3 | 504990 | 214 |
| MR_1774413733_99870A39 | 504990 | 931 | -86.1 | 504990 | 566 | -92.6 | 504990 | 468 | -95.5 | 504990 | 214 |
| MR_1774413733_5ABE8703 | 504990 | 931 | -86.5 | 504990 | 566 | -94.1 | 504990 | 468 | -93.8 | 504990 | 214 |
| MR_1774413733_57AC2B83 | 504990 | 931 | -89.4 | 504990 | 566 | -92.2 | 504990 | 468 | -94.3 | 504990 | 214 |
| MR_1774413733_945BD6B7 | 504990 | 931 | -88.5 | 504990 | 566 | -93.3 | 504990 | 468 | -96.0 | 504990 | 214 |
| MR_1774413733_84A0C568 | 504990 | 931 | -86.8 | 504990 | 566 | -92.6 | 504990 | 468 | -95.7 | 504990 | 214 |
| MR_1774413733_93FAD8D7 | 504990 | 931 | -87.6 | 504990 | 566 | -91.1 | 504990 | 468 | -95.8 | 504990 | 214 |
| MR_1774413733_FC6D64B0 | 504990 | 931 | -86.6 | 504990 | 566 | -91.4 | 504990 | 468 | -95.2 | 504990 | 214 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 375: `ec76b540-cc3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ec76b540-cc3b-45f1-9336-0571d8ee35cb` |
| Tag | **multiple-answer** |
| 정답 | **C1|C6|C8|C21** |
| C1 의미 | Increase A3 Offset threshold for 3254875_2 |
| C6 의미 | Press down the tilt angle  of 3233271_1 by 4 degrees |
| C8 의미 | Increase A3 Offset threshold for 3233271_1 |
| C21 의미 | Decrease transmission power for 3233271_1 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[375] topology](images/train_0375.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3254875_2 **← 정답**
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254875_2
- `C3`: Adjust the azimuth of 3254875_2 by 5 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254875_2
- `C5`: Add neighbor relationship between 3254875_2 and 3233271_1
- `C6`: Press down the tilt angle  of 3233271_1 by 4 degrees **← 정답**
- `C7`: Lift the tilt angle  of 3233271_1 by 4 degrees
- `C8`: Increase A3 Offset threshold for 3233271_1 **← 정답**
- `C9`: Lift the tilt angle of 3254875_2 by 5 degrees
- `C10`: Increase transmission power for 3233271_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233271_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233271_1
- `C13`: Decrease A3 Offset threshold for 3233271_1
- `C14`: Decrease transmission power for 3254875_2
- `C15`: Increase transmission power for 3254875_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease A3 Offset threshold for 3254875_2
- `C18`: Press down the tilt angle of 3254875_2 by 5 degrees
- `C19`: Adjust the azimuth of 3233271_1 by 32 degrees
- `C20`: Add neighbor relationship between 3247876_4 and 3233271_1
- `C21`: Decrease transmission power for 3233271_1 **← 정답**
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.253 | MS1 | 121.4656600544 | 31.1446181634 | 678 | 504990 | -83.74 | 15.29 | 549.99 | 0.16 | 2.37 | 1561 |
| 2024-09-20 22:21:32.374 | MS1 | 121.4656652333 | 31.1446186223 | 678 | 504990 | -77.76 | 12.96 | 570.82 | 0.10 | 2.16 | 1564 |
| 2024-09-20 22:21:33.816 | MS1 | 121.4656764033 | 31.1446248648 | 678 | 504990 | -78.42 | 17.25 | 437.05 | 0.04 | 2.43 | 1581 |
| 2024-09-20 22:21:34.149 | MS1 | 121.4656701262 | 31.1446246876 | 600 | 504990 | -89.80 | 4.58 | 68.46 | 0.03 | 1.19 | 1566 |
| 2024-09-20 22:21:35.851 | MS1 | 121.4656638698 | 31.1446330629 | 600 | 504990 | -89.71 | 3.07 | 75.49 | 0.02 | 1.48 | 1571 |
| 2024-09-20 22:21:36.590 | MS1 | 121.4656613718 | 31.1446327369 | 678 | 504990 | -84.53 | 2.86 | 67.22 | 0.13 | 1.01 | 1599 |
| 2024-09-20 22:21:37.615 | MS1 | 121.4656737308 | 31.1446283604 | 678 | 504990 | -82.10 | 2.55 | 68.91 | 0.07 | 1.36 | 1586 |
| 2024-09-20 22:21:38.614 | MS1 | 121.4656776521 | 31.1446375038 | 600 | 504990 | -89.36 | 1.19 | 47.82 | 0.06 | 1.10 | 1595 |
| 2024-09-20 22:21:39.780 | MS1 | 121.4656770215 | 31.1446224625 | 600 | 504990 | -88.88 | 3.58 | 59.15 | 0.09 | 1.26 | 1574 |
| 2024-09-20 22:21:40.268 | MS1 | 121.4656647083 | 31.1446246262 | 600 | 504990 | -82.97 | 16.92 | 342.88 | 0.06 | 2.38 | 1565 |
| 2024-09-20 22:21:41.676 | MS1 | 121.4656632417 | 31.1446242880 | 600 | 504990 | -76.92 | 13.61 | 564.52 | 0.14 | 2.20 | 1561 |
| 2024-09-20 22:21:42.772 | MS1 | 121.4656678805 | 31.1446328778 | 600 | 504990 | -84.81 | 12.20 | 340.15 | 0.17 | 2.07 | 1586 |

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
| 3221857 | 5 | 121.4688423053 | 31.1520905138 | 201 | 15 | 2 | 37.3 | TDD | 600 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3233271 | 1 | 121.4707513356 | 31.1494834456 | 254 | 2 | 3 | 22.2 | TDD | 128 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3238393 | 3 | 121.4648061183 | 31.1446217918 | 332 | 6 | 7 | 34.4 | TDD | 12 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3247876 | 4 | 121.4748285984 | 31.1477246707 | 147 | 2 | 4 | 49.0 | TDD | 720 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3254875 | 2 | 121.4686915180 | 31.1469151399 | 234 | 2 | 3 | 21.1 | TDD | 678 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.212 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.229 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.341 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.341 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.088 | NREventA3 | measId:2;ServCellPCI:38;Ser... |
| 2024-09-20 22:21:34.328 | NRHandoverAttempt | SourcePCI:38;SourceNR-ARFCN... |
| 2024-09-20 22:21:34.373 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.384 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:34.493 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.493 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.088 | NREventA3 | measId:2;ServCellPCI:332;Se... |
| 2024-09-20 22:21:36.328 | NRHandoverAttempt | SourcePCI:332;SourceNR-ARFC... |
| 2024-09-20 22:21:36.360 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.374 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.509 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.509 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.088 | NREventA3 | measId:2;ServCellPCI:38;Ser... |
| 2024-09-20 22:21:38.328 | NRHandoverAttempt | SourcePCI:38;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.359 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.369 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.510 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.510 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233271 | 1 | 8.8588 | 16.3461 | -115.3339 | 11.7364 | 174.0782 | 0.0080 | 0.0196 |
| 2024_09_20 22:00 | 3254875 | 2 | 19.8963 | 12.7695 | -114.0856 | 17.3753 | 90.8337 | 0.0111 | 0.0076 |
| 2024_09_20 22:00 | 3238393 | 3 | 7.9441 | 19.9993 | -115.3450 | 5.6795 | 176.5628 | 0.0115 | 0.0181 |
| 2024_09_20 22:00 | 3247876 | 4 | 18.6239 | 9.3340 | -115.0155 | 10.7009 | 170.4891 | 0.0175 | 0.0150 |
| 2024_09_20 22:00 | 3221857 | 5 | 9.7192 | 13.8038 | -114.9637 | 8.0019 | 193.6826 | 0.0066 | 0.0179 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413219_0F8DD5FA | 504990 | 678 | -90.0 | 504990 | 600 | -89.6 | 504990 | 128 | -94.1 | 504990 | 720 |
| MR_1774413219_9DFE3D0C | 504990 | 678 | -89.4 | 504990 | 600 | -92.0 | 504990 | 128 | -95.1 | 504990 | 720 |
| MR_1774413219_C457C1F9 | 504990 | 600 | -88.4 | 504990 | 678 | -92.7 | 504990 | 128 | -93.2 | 504990 | 720 |
| MR_1774413219_A7501D7C | 504990 | 678 | -90.3 | 504990 | 600 | -89.7 | 504990 | 128 | -94.0 | 504990 | 720 |
| MR_1774413219_8B53ECF5 | 504990 | 678 | -89.8 | 504990 | 600 | -89.2 | 504990 | 128 | -92.1 | 504990 | 720 |
| MR_1774413219_9D752BDD | 504990 | 600 | -91.3 | 504990 | 678 | -91.1 | 504990 | 128 | -95.0 | 504990 | 720 |
| MR_1774413219_42008EBA | 504990 | 678 | -91.1 | 504990 | 600 | -89.9 | 504990 | 128 | -92.2 | 504990 | 720 |
| MR_1774413219_9B7A00E6 | 504990 | 678 | -89.6 | 504990 | 600 | -90.0 | 504990 | 128 | -93.7 | 504990 | 720 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 376: `17ed83a9-3ae...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `17ed83a9-3aee-4e5a-92e5-92ad0651d055` |
| Tag | **multiple-answer** |
| 정답 | **C4|C14** |
| C4 의미 | Adjust the azimuth of 3252481_4 by 50 degrees |
| C14 의미 | Increase transmission power for 3252481_4 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[376] topology](images/train_0376.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3252481_4 and 3248738_3
- `C2`: Increase A3 Offset threshold for 3248738_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248738_3
- `C4`: Adjust the azimuth of 3252481_4 by 50 degrees **← 정답**
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease A3 Offset threshold for 3248738_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248738_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252481_4
- `C9`: Press down the tilt angle of 3252481_4 by 6 degrees
- `C10`: Lift the tilt angle of 3252481_4 by 6 degrees
- `C11`: Adjust the azimuth of 3248738_3 by 14 degrees
- `C12`: Decrease transmission power for 3248738_3
- `C13`: Decrease transmission power for 3252481_4
- `C14`: Increase transmission power for 3252481_4 **← 정답**
- `C15`: Lift the tilt angle  of 3248738_3 by 3 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252481_4
- `C17`: Press down the tilt angle  of 3248738_3 by 3 degrees
- `C18`: Increase transmission power for 3248738_3
- `C19`: Add neighbor relationship between 3226988_1 and 3248738_3
- `C20`: Decrease A3 Offset threshold for 3252481_4
- `C21`: Increase A3 Offset threshold for 3252481_4
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.636 | MS1 | 121.4656642159 | 31.1446231558 | 127 | 504990 | -88.18 | 12.06 | 506.71 | 0.08 | 2.70 | 1593 |
| 2024-09-20 22:21:32.531 | MS1 | 121.4656736180 | 31.1446295268 | 127 | 504990 | -90.07 | 15.05 | 359.55 | 0.17 | 2.03 | 1569 |
| 2024-09-20 22:21:33.178 | MS1 | 121.4656661550 | 31.1446275889 | 127 | 504990 | -85.67 | 12.17 | 559.27 | 0.12 | 2.64 | 1562 |
| 2024-09-20 22:21:34.601 | MS1 | 121.4656657695 | 31.1446199965 | 127 | 504990 | -106.42 | -0.83 | 37.33 | 0.03 | 1.25 | 1565 |
| 2024-09-20 22:21:35.401 | MS1 | 121.4656613464 | 31.1446208827 | 127 | 504990 | -102.18 | -0.33 | 57.28 | 0.16 | 1.00 | 1575 |
| 2024-09-20 22:21:36.936 | MS1 | 121.4656624605 | 31.1446196507 | 127 | 504990 | -108.85 | 1.73 | 26.02 | 0.05 | 1.43 | 1597 |
| 2024-09-20 22:21:37.302 | MS1 | 121.4656676830 | 31.1446343921 | 127 | 504990 | -104.38 | -0.10 | 29.65 | 0.13 | 1.30 | 1577 |
| 2024-09-20 22:21:38.812 | MS1 | 121.4656659042 | 31.1446329886 | 127 | 504990 | -102.06 | 0.66 | 29.61 | 0.13 | 1.48 | 1569 |
| 2024-09-20 22:21:39.245 | MS1 | 121.4656680577 | 31.1446343308 | 127 | 504990 | -109.32 | -0.21 | 30.77 | 0.13 | 1.34 | 1561 |
| 2024-09-20 22:21:40.859 | MS1 | 121.4656674357 | 31.1446294347 | 127 | 504990 | -86.08 | 14.64 | 518.91 | 0.13 | 2.78 | 1562 |
| 2024-09-20 22:21:41.420 | MS1 | 121.4656672952 | 31.1446273079 | 127 | 504990 | -92.95 | 14.25 | 512.91 | 0.03 | 2.66 | 1570 |
| 2024-09-20 22:21:42.505 | MS1 | 121.4656765888 | 31.1446280551 | 127 | 504990 | -88.52 | 16.09 | 509.75 | 0.09 | 2.99 | 1571 |

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
| 3212905 | 2 | 121.4745708695 | 31.1556667477 | 355 | 11 | 3 | 29.9 | TDD | 733 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3226988 | 1 | 121.4681834085 | 31.1479307918 | 27 | 12 | 0 | 40.3 | TDD | 109 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3248738 | 3 | 121.4646950809 | 31.1549092761 | 189 | 1 | 12 | 37.2 | TDD | 62 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3252481 | 4 | 121.4722232507 | 31.1468054361 | 306 | 3 | 1 | 34.2 | TDD | 127 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.285 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.302 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.450 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.450 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.650 | NREventA2 | measId:1;ServCellPCI:480;Se... |
| 2024-09-20 22:21:34.778 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226988 | 1 | 6.9488 | 11.5284 | -115.3253 | 18.3214 | 128.2159 | 0.0151 | 0.0194 |
| 2024_09_20 22:00 | 3212905 | 2 | 9.7133 | 10.6887 | -114.1038 | 11.2944 | 94.2195 | 0.0104 | 0.0162 |
| 2024_09_20 22:00 | 3248738 | 3 | 10.4743 | 13.2954 | -117.3674 | 13.7847 | 100.5500 | 0.0060 | 0.0100 |
| 2024_09_20 22:00 | 3252481 | 4 | 15.2381 | 16.8731 | -116.3724 | 7.9932 | 145.5365 | 0.1167 | 0.0140 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415767_E8C46E93 | 504990 | 127 | -106.1 | 504990 | 62 | -111.6 | 504990 | 109 | -113.8 | 504990 | 733 |
| MR_1774415767_D3F202DE | 504990 | 127 | -107.7 | 504990 | 62 | -112.1 | 504990 | 109 | -116.0 | 504990 | 733 |
| MR_1774415767_AFE7ADCC | 504990 | 127 | -105.1 | 504990 | 62 | -111.0 | 504990 | 109 | -116.0 | 504990 | 733 |
| MR_1774415767_41AF9C6B | 504990 | 127 | -105.7 | 504990 | 62 | -110.1 | 504990 | 109 | -116.7 | 504990 | 733 |
| MR_1774415767_4B6B36F7 | 504990 | 127 | -106.0 | 504990 | 62 | -111.9 | 504990 | 109 | -113.8 | 504990 | 733 |
| MR_1774415767_CE932FF0 | 504990 | 127 | -105.4 | 504990 | 62 | -111.6 | 504990 | 109 | -114.6 | 504990 | 733 |
| MR_1774415767_50BB9063 | 504990 | 127 | -106.4 | 504990 | 62 | -110.5 | 504990 | 109 | -114.1 | 504990 | 733 |
| MR_1774415767_01B82FDD | 504990 | 127 | -104.6 | 504990 | 62 | -109.3 | 504990 | 109 | -113.3 | 504990 | 733 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 377: `4c369ece-197...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4c369ece-197b-496c-9532-36ff13bfec2a` |
| Tag | **multiple-answer** |
| 정답 | **C1|C16** |
| C1 의미 | Adjust the azimuth of 3260647_1 by 50 degrees |
| C16 의미 | Increase transmission power for 3260647_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[377] topology](images/train_0377.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3260647_1 by 50 degrees **← 정답**
- `C2`: Lift the tilt angle of 3260647_1 by 10 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase transmission power for 3278932_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278932_3
- `C6`: Increase A3 Offset threshold for 3260647_1
- `C7`: Decrease A3 Offset threshold for 3278932_3
- `C8`: Lift the tilt angle  of 3278932_3 by 4 degrees
- `C9`: Add neighbor relationship between 3251030_2 and 3278932_3
- `C10`: Press down the tilt angle  of 3278932_3 by 4 degrees
- `C11`: Check test server and transmission issues
- `C12`: Decrease A3 Offset threshold for 3260647_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278932_3
- `C14`: Increase A3 Offset threshold for 3278932_3
- `C15`: Decrease transmission power for 3260647_1
- `C16`: Increase transmission power for 3260647_1 **← 정답**
- `C17`: Add neighbor relationship between 3260647_1 and 3278932_3
- `C18`: Adjust the azimuth of 3278932_3 by 10 degrees
- `C19`: Decrease transmission power for 3278932_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260647_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260647_1
- `C22`: Press down the tilt angle of 3260647_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.231 | MS1 | 121.4656628511 | 31.1446310723 | 959 | 504990 | -91.37 | 13.37 | 314.27 | 0.02 | 2.87 | 1594 |
| 2024-09-20 22:21:32.964 | MS1 | 121.4656627325 | 31.1446287017 | 959 | 504990 | -85.80 | 13.34 | 395.83 | 0.10 | 2.89 | 1568 |
| 2024-09-20 22:21:33.622 | MS1 | 121.4656632869 | 31.1446246085 | 959 | 504990 | -86.65 | 13.66 | 346.40 | 0.09 | 2.00 | 1593 |
| 2024-09-20 22:21:34.779 | MS1 | 121.4656713500 | 31.1446281849 | 959 | 504990 | -106.86 | 0.48 | 27.39 | 0.05 | 1.49 | 1571 |
| 2024-09-20 22:21:35.335 | MS1 | 121.4656766608 | 31.1446372602 | 959 | 504990 | -109.63 | 1.51 | 12.47 | 0.07 | 1.36 | 1592 |
| 2024-09-20 22:21:36.719 | MS1 | 121.4656691511 | 31.1446350317 | 959 | 504990 | -100.31 | -1.37 | 37.09 | 0.08 | 1.33 | 1575 |
| 2024-09-20 22:21:37.538 | MS1 | 121.4656691524 | 31.1446344589 | 959 | 504990 | -105.90 | 0.12 | 49.87 | 0.00 | 1.16 | 1575 |
| 2024-09-20 22:21:38.374 | MS1 | 121.4656693223 | 31.1446333463 | 959 | 504990 | -100.41 | 1.05 | 34.16 | 0.10 | 1.05 | 1563 |
| 2024-09-20 22:21:39.422 | MS1 | 121.4656650987 | 31.1446318345 | 959 | 504990 | -101.88 | 0.87 | 45.24 | 0.01 | 1.17 | 1582 |
| 2024-09-20 22:21:40.148 | MS1 | 121.4656664953 | 31.1446213830 | 959 | 504990 | -94.01 | 13.95 | 405.26 | 0.16 | 2.25 | 1570 |
| 2024-09-20 22:21:41.954 | MS1 | 121.4656586544 | 31.1446326251 | 959 | 504990 | -94.96 | 16.20 | 447.41 | 0.16 | 2.52 | 1584 |
| 2024-09-20 22:21:42.234 | MS1 | 121.4656684359 | 31.1446359461 | 959 | 504990 | -88.95 | 14.81 | 586.78 | 0.16 | 2.75 | 1577 |

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
| 3251030 | 2 | 121.4647224775 | 31.1542210912 | 354 | 13 | 11 | 34.3 | TDD | 635 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3260647 | 1 | 121.4755375075 | 31.1466360640 | 312 | 8 | 7 | 41.6 | TDD | 959 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3273862 | 4 | 121.4651998406 | 31.1475153554 | 292 | 5 | 8 | 41.4 | TDD | 263 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3278932 | 3 | 121.4703750785 | 31.1519565358 | 199 | 3 | 5 | 15.7 | TDD | 926 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.829 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.849 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.973 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.973 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.132 | NREventA2 | measId:1;ServCellPCI:254;Se... |
| 2024-09-20 22:21:34.280 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260647 | 1 | 17.4579 | 12.4469 | -115.5229 | 6.1325 | 84.9099 | 0.1692 | 0.0193 |
| 2024_09_20 22:00 | 3251030 | 2 | 17.6207 | 14.3609 | -114.5040 | 5.0918 | 131.0918 | 0.0073 | 0.0013 |
| 2024_09_20 22:00 | 3278932 | 3 | 12.1762 | 19.7393 | -115.8066 | 14.6212 | 145.9848 | 0.0158 | 0.0168 |
| 2024_09_20 22:00 | 3273862 | 4 | 19.2584 | 18.0643 | -114.0692 | 15.7621 | 90.9203 | 0.0176 | 0.0192 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413559_517AF355 | 504990 | 959 | -106.4 | 504990 | 926 | -111.6 | 504990 | 635 | -117.1 | 504990 | 263 |
| MR_1774413559_D5592C57 | 504990 | 959 | -106.9 | 504990 | 926 | -112.3 | 504990 | 635 | -117.7 | 504990 | 263 |
| MR_1774413559_DCDAB4A0 | 504990 | 959 | -106.8 | 504990 | 926 | -112.5 | 504990 | 635 | -118.5 | 504990 | 263 |
| MR_1774413559_B97562B9 | 504990 | 959 | -107.7 | 504990 | 926 | -112.7 | 504990 | 635 | -120.3 | 504990 | 263 |
| MR_1774413559_106A8B5C | 504990 | 959 | -107.5 | 504990 | 926 | -110.4 | 504990 | 635 | -118.2 | 504990 | 263 |
| MR_1774413559_87749B7F | 504990 | 959 | -108.2 | 504990 | 926 | -111.9 | 504990 | 635 | -118.6 | 504990 | 263 |
| MR_1774413559_99D85A87 | 504990 | 959 | -107.8 | 504990 | 926 | -110.9 | 504990 | 635 | -119.5 | 504990 | 263 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 378: `3ecb919e-2cc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3ecb919e-2cce-41f5-83dd-cd7f175d0687` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[378] topology](images/train_0378.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3276279_4
- `C2`: Lift the tilt angle of 3276279_4 by 7 degrees
- `C3`: Add neighbor relationship between 3273130_2 and 3266316_3
- `C4`: Increase A3 Offset threshold for 3276279_4
- `C5`: Increase transmission power for 3266316_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266316_3
- `C7`: Press down the tilt angle  of 3266316_3 by 7 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276279_4
- `C9`: Lift the tilt angle  of 3266316_3 by 7 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266316_3
- `C11`: Adjust the azimuth of 3276279_4 by 36 degrees
- `C12`: Decrease A3 Offset threshold for 3276279_4
- `C13`: Press down the tilt angle of 3276279_4 by 7 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276279_4
- `C15`: Increase transmission power for 3276279_4
- `C16`: Insufficient data; more data is needed for judgment. **← 정답**
- `C17`: Check test server and transmission issues
- `C18`: Increase A3 Offset threshold for 3266316_3
- `C19`: Decrease transmission power for 3266316_3
- `C20`: Add neighbor relationship between 3276279_4 and 3266316_3
- `C21`: Decrease A3 Offset threshold for 3266316_3
- `C22`: Adjust the azimuth of 3266316_3 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.620 | MS1 | 121.4656652446 | 31.1446235695 | 663 | 504990 | -86.52 | 17.48 | 376.61 | 0.18 | 2.48 | 1560 |
| 2024-09-20 22:21:32.250 | MS1 | 121.4656719426 | 31.1446345360 | 663 | 504990 | -88.72 | 12.27 | 484.45 | 0.05 | 2.88 | 1560 |
| 2024-09-20 22:21:33.234 | MS1 | 121.4656622818 | 31.1446201415 | 663 | 504990 | -87.05 | 13.62 | 305.11 | 0.15 | 2.34 | 1587 |
| 2024-09-20 22:21:34.852 | MS1 | 121.4656734676 | 31.1446338984 | 663 | 504990 | -90.28 | 12.15 | 44.38 | 0.07 | 2.96 | 1561 |
| 2024-09-20 22:21:35.440 | MS1 | 121.4656709994 | 31.1446183776 | 663 | 504990 | -86.13 | 12.50 | 66.63 | 0.04 | 2.70 | 1597 |
| 2024-09-20 22:21:36.743 | MS1 | 121.4656623386 | 31.1446352978 | 663 | 504990 | -88.44 | 12.98 | 96.00 | 0.00 | 2.97 | 1586 |
| 2024-09-20 22:21:37.727 | MS1 | 121.4656696233 | 31.1446336565 | 663 | 504990 | -93.28 | 7.56 | 87.76 | 0.03 | 2.34 | 1560 |
| 2024-09-20 22:21:38.293 | MS1 | 121.4656626511 | 31.1446218394 | 663 | 504990 | -91.45 | 9.12 | 45.53 | 0.16 | 2.94 | 1571 |
| 2024-09-20 22:21:39.442 | MS1 | 121.4656714348 | 31.1446315902 | 663 | 504990 | -93.27 | 8.36 | 76.80 | 0.12 | 2.01 | 1591 |
| 2024-09-20 22:21:40.987 | MS1 | 121.4656679948 | 31.1446246274 | 663 | 504990 | -93.50 | 12.67 | 558.84 | 0.10 | 2.17 | 1576 |
| 2024-09-20 22:21:41.110 | MS1 | 121.4656619872 | 31.1446243837 | 663 | 504990 | -92.98 | 9.84 | 407.42 | 0.14 | 2.42 | 1593 |
| 2024-09-20 22:21:42.893 | MS1 | 121.4656736117 | 31.1446281547 | 663 | 504990 | -93.33 | 11.47 | 496.89 | 0.20 | 2.35 | 1586 |

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
| 3212710 | 1 | 121.4726660791 | 31.1551736772 | 306 | 15 | 5 | 48.7 | TDD | 643 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3266316 | 3 | 121.4683958570 | 31.1502029531 | 299 | 4 | 5 | 40.5 | TDD | 638 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3273130 | 2 | 121.4692219408 | 31.1497133475 | 96 | 12 | 5 | 26.9 | TDD | 932 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3276279 | 4 | 121.4649726126 | 31.1530906376 | 140 | 4 | 8 | 45.4 | TDD | 663 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.855 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.873 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.982 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.982 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.748 | NREventA3 | measId:2;ServCellPCI:608;Se... |
| 2024-09-20 22:21:37.988 | NRHandoverAttempt | SourcePCI:608;SourceNR-ARFC... |
| 2024-09-20 22:21:38.029 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.040 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.152 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.152 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3212710 | 1 | 87.1573 | 94.7378 | -117.1335 | 9.9269 | 164.8752 | 0.0187 | 0.0064 |
| 2024_09_19 22:00 | 3273130 | 2 | 85.8072 | 86.6987 | -116.0064 | 8.2405 | 152.5821 | 0.0009 | 0.0189 |
| 2024_09_19 22:00 | 3266316 | 3 | 85.9780 | 93.5943 | -115.9986 | 10.7925 | 124.9759 | 0.0131 | 0.0151 |
| 2024_09_19 22:00 | 3276279 | 4 | 84.5629 | 88.4637 | -116.2306 | 9.6837 | 117.2523 | 0.0136 | 0.0111 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414510_1CAB0949 | 504990 | 663 | -89.9 | 504990 | 638 | -99.9 | 504990 | 932 | -106.5 | 504990 | 643 |
| MR_1774414510_C76E6CB7 | 504990 | 663 | -90.7 | 504990 | 638 | -100.0 | 504990 | 932 | -103.1 | 504990 | 643 |
| MR_1774414510_675927C3 | 504990 | 663 | -88.8 | 504990 | 638 | -98.0 | 504990 | 932 | -105.7 | 504990 | 643 |
| MR_1774414510_5458799F | 504990 | 663 | -90.6 | 504990 | 638 | -99.4 | 504990 | 932 | -104.4 | 504990 | 643 |
| MR_1774414510_A41CA00C | 504990 | 663 | -91.4 | 504990 | 638 | -98.1 | 504990 | 932 | -106.4 | 504990 | 643 |
| MR_1774414510_35965859 | 504990 | 663 | -90.7 | 504990 | 638 | -99.0 | 504990 | 932 | -103.0 | 504990 | 643 |
| MR_1774414510_88577A7F | 504990 | 663 | -89.4 | 504990 | 638 | -96.5 | 504990 | 932 | -104.2 | 504990 | 643 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 379: `efe35e97-980...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `efe35e97-9806-4aa4-8708-508816e22973` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[379] topology](images/train_0379.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3219711_2
- `C2`: Add neighbor relationship between 3219711_2 and 3256148_1
- `C3`: Adjust the azimuth of 3256148_1 by 50 degrees
- `C4`: Insufficient data; more data is needed for judgment. **← 정답**
- `C5`: Adjust the azimuth of 3219711_2 by 50 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256148_1
- `C7`: Press down the tilt angle of 3219711_2 by 10 degrees
- `C8`: Decrease transmission power for 3219711_2
- `C9`: Add neighbor relationship between 3220551_4 and 3256148_1
- `C10`: Decrease A3 Offset threshold for 3219711_2
- `C11`: Lift the tilt angle of 3219711_2 by 10 degrees
- `C12`: Increase transmission power for 3256148_1
- `C13`: Decrease transmission power for 3256148_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256148_1
- `C15`: Check test server and transmission issues
- `C16`: Lift the tilt angle  of 3256148_1 by 5 degrees
- `C17`: Increase A3 Offset threshold for 3256148_1
- `C18`: Increase A3 Offset threshold for 3219711_2
- `C19`: Decrease A3 Offset threshold for 3256148_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219711_2
- `C21`: Press down the tilt angle  of 3256148_1 by 5 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219711_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.306 | MS1 | 121.4656629224 | 31.1446347852 | 363 | 504990 | -86.98 | 13.68 | 557.44 | 0.17 | 2.09 | 1566 |
| 2024-09-20 22:21:32.584 | MS1 | 121.4656777298 | 31.1446279644 | 363 | 504990 | -91.26 | 15.40 | 570.33 | 0.08 | 2.19 | 1600 |
| 2024-09-20 22:21:33.262 | MS1 | 121.4656600936 | 31.1446254676 | 363 | 504990 | -90.69 | 17.84 | 343.23 | 0.12 | 2.07 | 1583 |
| 2024-09-20 22:21:34.725 | MS1 | 121.4656738630 | 31.1446347370 | 363 | 504990 | -86.86 | 17.56 | 47.16 | 0.02 | 2.97 | 1569 |
| 2024-09-20 22:21:35.982 | MS1 | 121.4656718405 | 31.1446351733 | 363 | 504990 | -86.51 | 17.96 | 89.53 | 0.11 | 2.85 | 1567 |
| 2024-09-20 22:21:36.707 | MS1 | 121.4656635686 | 31.1446321554 | 363 | 504990 | -90.05 | 16.43 | 72.48 | 0.06 | 2.70 | 1600 |
| 2024-09-20 22:21:37.592 | MS1 | 121.4656685897 | 31.1446232915 | 363 | 504990 | -93.17 | 10.68 | 52.20 | 0.03 | 2.92 | 1588 |
| 2024-09-20 22:21:38.660 | MS1 | 121.4656725079 | 31.1446367448 | 363 | 504990 | -92.17 | 7.74 | 64.77 | 0.04 | 2.98 | 1600 |
| 2024-09-20 22:21:39.463 | MS1 | 121.4656586651 | 31.1446279053 | 363 | 504990 | -90.47 | 8.45 | 56.85 | 0.19 | 2.00 | 1560 |
| 2024-09-20 22:21:40.144 | MS1 | 121.4656594116 | 31.1446275265 | 363 | 504990 | -93.27 | 7.01 | 536.27 | 0.19 | 2.32 | 1568 |
| 2024-09-20 22:21:41.769 | MS1 | 121.4656620757 | 31.1446295275 | 363 | 504990 | -89.65 | 7.23 | 544.51 | 0.17 | 2.32 | 1583 |
| 2024-09-20 22:21:42.462 | MS1 | 121.4656624295 | 31.1446344160 | 363 | 504990 | -91.55 | 7.45 | 399.03 | 0.06 | 2.09 | 1566 |

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
| 3219711 | 2 | 121.4680086004 | 31.1515472074 | 298 | 9 | 6 | 15.5 | TDD | 363 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3220551 | 4 | 121.4706880755 | 31.1447959086 | 46 | 3 | 11 | 49.1 | TDD | 230 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3250937 | 3 | 121.4748005694 | 31.1553467808 | 62 | 3 | 9 | 35.6 | TDD | 654 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3256148 | 1 | 121.4701980580 | 31.1535627104 | 280 | 3 | 6 | 39.9 | TDD | 401 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.871 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.895 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.044 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.044 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.715 | NREventA3 | measId:2;ServCellPCI:49;Ser... |
| 2024-09-20 22:21:37.955 | NRHandoverAttempt | SourcePCI:49;SourceNR-ARFCN... |
| 2024-09-20 22:21:37.990 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.001 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.146 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.146 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3256148 | 1 | 88.0868 | 83.0448 | -117.3237 | 9.8883 | 115.1244 | 0.0048 | 0.0114 |
| 2024_09_19 22:00 | 3219711 | 2 | 91.3105 | 76.1418 | -114.1079 | 17.5815 | 169.7212 | 0.0149 | 0.0048 |
| 2024_09_19 22:00 | 3250937 | 3 | 76.0998 | 78.4396 | -115.9914 | 14.3169 | 192.6310 | 0.0005 | 0.0026 |
| 2024_09_19 22:00 | 3220551 | 4 | 78.7521 | 79.3473 | -116.3279 | 17.0627 | 140.3634 | 0.0155 | 0.0008 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413668_048967F8 | 504990 | 363 | -86.7 | 504990 | 401 | -91.7 | 504990 | 230 | -95.3 | 504990 | 654 |
| MR_1774413668_522965B4 | 504990 | 363 | -87.5 | 504990 | 401 | -92.1 | 504990 | 230 | -94.1 | 504990 | 654 |
| MR_1774413668_85C51957 | 504990 | 363 | -88.7 | 504990 | 401 | -94.3 | 504990 | 230 | -96.1 | 504990 | 654 |
| MR_1774413668_805DF596 | 504990 | 363 | -87.5 | 504990 | 401 | -94.2 | 504990 | 230 | -95.4 | 504990 | 654 |
| MR_1774413668_C55E8BA0 | 504990 | 363 | -87.5 | 504990 | 401 | -91.6 | 504990 | 230 | -94.1 | 504990 | 654 |
| MR_1774413668_2D160BDC | 504990 | 363 | -88.1 | 504990 | 401 | -92.6 | 504990 | 230 | -96.6 | 504990 | 654 |
| MR_1774413668_6C97872F | 504990 | 363 | -86.3 | 504990 | 401 | -93.5 | 504990 | 230 | -96.8 | 504990 | 654 |
| MR_1774413668_170F67F4 | 504990 | 363 | -85.7 | 504990 | 401 | -92.0 | 504990 | 230 | -96.4 | 504990 | 654 |

> *... 2개 열 생략 (전체 14열)*

---
