# Track A 문제 분석 — test[100]~test[109]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[100] ~ test[109] (10개)

## 목차

1. [문제 100: `76a27827-bbd...`](#100) — single-answer
2. [문제 101: `cecbb680-5a9...`](#101) — single-answer
3. [문제 102: `40e31b37-608...`](#102) — single-answer
4. [문제 103: `887b70e0-ae2...`](#103) — single-answer
5. [문제 104: `be04ca82-4b5...`](#104) — single-answer
6. [문제 105: `664d75d3-5ee...`](#105) — single-answer
7. [문제 106: `9f4f1d2d-f72...`](#106) — single-answer
8. [문제 107: `42ef2542-0fb...`](#107) — single-answer
9. [문제 108: `2b3c1dbb-1a2...`](#108) — single-answer
10. [문제 109: `2a03e00b-275...`](#109) — single-answer

---

### 문제 100: `76a27827-bbd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `76a27827-bbd4-4edf-a68b-32b71883b866` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[100] topology](images/test_0100.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3262571_4 by 8 degrees
- `C2`: Decrease transmission power for 3268431_3
- `C3`: Increase transmission power for 3268431_3
- `C4`: Increase transmission power for 3262571_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262571_4
- `C6`: Adjust the azimuth of 3268431_3 by 37 degrees
- `C7`: Decrease transmission power for 3262571_4
- `C8`: Decrease A3 Offset threshold for 3262571_4
- `C9`: Add neighbor relationship between 3214127_1 and 3262571_4
- `C10`: Increase A3 Offset threshold for 3268431_3
- `C11`: Adjust the azimuth of 3262571_4 by 50 degrees
- `C12`: Add neighbor relationship between 3268431_3 and 3262571_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262571_4
- `C14`: Press down the tilt angle  of 3262571_4 by 8 degrees
- `C15`: Decrease A3 Offset threshold for 3268431_3
- `C16`: Lift the tilt angle of 3268431_3 by 6 degrees
- `C17`: Press down the tilt angle of 3268431_3 by 6 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268431_3
- `C20`: Increase A3 Offset threshold for 3262571_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268431_3
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.382 | MS1 | 121.4656637397 | 31.1446231752 | 474 | 504990 | -88.82 | 17.67 | 367.41 | 0.05 | 2.82 | 1597 |
| 2024-09-20 22:21:32.551 | MS1 | 121.4656720617 | 31.1446184448 | 474 | 504990 | -86.09 | 16.60 | 354.74 | 0.09 | 2.17 | 1578 |
| 2024-09-20 22:21:33.253 | MS1 | 121.4656775502 | 31.1446370429 | 474 | 504990 | -90.84 | 17.26 | 464.84 | 0.16 | 2.61 | 1577 |
| 2024-09-20 22:21:34.311 | MS1 | 121.4656779678 | 31.1446271085 | 474 | 504990 | -88.00 | 16.93 | 65.34 | 0.67 | 2.61 | 528 |
| 2024-09-20 22:21:35.509 | MS1 | 121.4656592079 | 31.1446255008 | 474 | 504990 | -88.89 | 12.03 | 62.51 | 0.65 | 2.92 | 603 |
| 2024-09-20 22:21:36.680 | MS1 | 121.4656723713 | 31.1446364797 | 474 | 504990 | -85.41 | 12.30 | 95.53 | 0.56 | 2.22 | 648 |
| 2024-09-20 22:21:37.154 | MS1 | 121.4656731921 | 31.1446341766 | 474 | 504990 | -90.24 | 8.66 | 75.25 | 0.65 | 2.91 | 691 |
| 2024-09-20 22:21:38.642 | MS1 | 121.4656609149 | 31.1446304010 | 474 | 504990 | -91.91 | 10.81 | 48.01 | 0.53 | 2.52 | 587 |
| 2024-09-20 22:21:39.527 | MS1 | 121.4656764689 | 31.1446184232 | 474 | 504990 | -91.27 | 9.08 | 51.30 | 0.64 | 2.22 | 634 |
| 2024-09-20 22:21:40.281 | MS1 | 121.4656632241 | 31.1446236714 | 474 | 504990 | -91.57 | 12.71 | 314.91 | 0.05 | 2.49 | 1564 |
| 2024-09-20 22:21:41.610 | MS1 | 121.4656737379 | 31.1446235098 | 474 | 504990 | -93.55 | 12.25 | 340.57 | 0.17 | 2.38 | 1584 |
| 2024-09-20 22:21:42.288 | MS1 | 121.4656639168 | 31.1446294033 | 474 | 504990 | -93.25 | 9.54 | 322.26 | 0.07 | 2.24 | 1594 |

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
| 3214127 | 1 | 121.4732421991 | 31.1442384545 | 15 | 13 | 4 | 43.9 | TDD | 224 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3228554 | 2 | 121.4734447968 | 31.1440996902 | 270 | 9 | 3 | 43.6 | TDD | 752 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3262571 | 4 | 121.4658709158 | 31.1475938016 | 341 | 1 | 9 | 40.4 | TDD | 586 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3268431 | 3 | 121.4742512940 | 31.1491537074 | 201 | 4 | 6 | 27.6 | TDD | 474 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.149 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.280 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.280 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.928 | NREventA3 | measId:2;ServCellPCI:736;Se... |
| 2024-09-20 22:21:38.168 | NRHandoverAttempt | SourcePCI:736;SourceNR-ARFC... |
| 2024-09-20 22:21:38.204 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.215 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.348 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.348 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214127 | 1 | 15.7589 | 13.9257 | -117.2677 | 16.9266 | 160.6597 | 0.0046 | 0.0081 |
| 2024_09_20 22:00 | 3228554 | 2 | 9.4807 | 15.8446 | -117.0300 | 14.1164 | 96.7350 | 0.0092 | 0.0192 |
| 2024_09_20 22:00 | 3268431 | 3 | 7.9654 | 6.8840 | -117.1692 | 10.8861 | 92.6311 | 0.0194 | 0.0143 |
| 2024_09_20 22:00 | 3262571 | 4 | 9.5892 | 15.2999 | -114.9818 | 14.6074 | 107.8241 | 0.0191 | 0.0138 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415954_6FE2D502 | 504990 | 474 | -89.5 | 504990 | 586 | -94.2 | 504990 | 224 | -100.3 | 504990 | 752 |
| MR_1774415954_CC62483D | 504990 | 474 | -89.4 | 504990 | 586 | -97.4 | 504990 | 224 | -98.6 | 504990 | 752 |
| MR_1774415954_08A188A4 | 504990 | 474 | -88.7 | 504990 | 586 | -96.9 | 504990 | 224 | -100.5 | 504990 | 752 |
| MR_1774415954_6039B6EA | 504990 | 474 | -88.3 | 504990 | 586 | -96.6 | 504990 | 224 | -101.1 | 504990 | 752 |
| MR_1774415954_36C704B4 | 504990 | 474 | -87.9 | 504990 | 586 | -95.6 | 504990 | 224 | -98.5 | 504990 | 752 |
| MR_1774415954_B3B528F5 | 504990 | 474 | -87.7 | 504990 | 586 | -97.4 | 504990 | 224 | -98.1 | 504990 | 752 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 101: `cecbb680-5a9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cecbb680-5a90-4847-acea-5b5b87ac2484` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[101] topology](images/test_0101.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262519_3
- `C2`: Decrease transmission power for 3262519_3
- `C3`: Decrease A3 Offset threshold for 3262519_3
- `C4`: Add neighbor relationship between 3247393_4 and 3262519_3
- `C5`: Increase transmission power for 3262519_3
- `C6`: Adjust the azimuth of 3261990_2 by 50 degrees
- `C7`: Increase transmission power for 3261990_2
- `C8`: Increase A3 Offset threshold for 3262519_3
- `C9`: Add neighbor relationship between 3261990_2 and 3262519_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262519_3
- `C11`: Lift the tilt angle  of 3262519_3 by 8 degrees
- `C12`: Lift the tilt angle of 3261990_2 by 4 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Press down the tilt angle of 3261990_2 by 4 degrees
- `C15`: Check test server and transmission issues
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261990_2
- `C17`: Adjust the azimuth of 3262519_3 by 50 degrees
- `C18`: Increase A3 Offset threshold for 3261990_2
- `C19`: Decrease A3 Offset threshold for 3261990_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261990_2
- `C21`: Decrease transmission power for 3261990_2
- `C22`: Press down the tilt angle  of 3262519_3 by 8 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.801 | MS1 | 121.4656590465 | 31.1446289540 | 410 | 504990 | -88.36 | 15.62 | 389.43 | 0.11 | 2.43 | 1563 |
| 2024-09-20 22:21:32.961 | MS1 | 121.4656598004 | 31.1446220600 | 410 | 504990 | -87.01 | 16.00 | 495.47 | 0.01 | 2.93 | 1565 |
| 2024-09-20 22:21:33.736 | MS1 | 121.4656714847 | 31.1446260276 | 410 | 504990 | -86.74 | 13.98 | 465.96 | 0.08 | 2.40 | 1598 |
| 2024-09-20 22:21:34.845 | MS1 | 121.4656626078 | 31.1446290307 | 410 | 504990 | -90.75 | 14.24 | 52.62 | 0.14 | 2.48 | 366 |
| 2024-09-20 22:21:35.427 | MS1 | 121.4656606713 | 31.1446243436 | 410 | 504990 | -91.25 | 14.66 | 56.87 | 0.10 | 2.96 | 444 |
| 2024-09-20 22:21:36.688 | MS1 | 121.4656603439 | 31.1446193838 | 410 | 504990 | -89.45 | 16.01 | 77.42 | 0.08 | 2.48 | 368 |
| 2024-09-20 22:21:37.151 | MS1 | 121.4656667632 | 31.1446363101 | 410 | 504990 | -89.37 | 12.17 | 76.30 | 0.14 | 2.67 | 476 |
| 2024-09-20 22:21:38.113 | MS1 | 121.4656774217 | 31.1446325214 | 410 | 504990 | -89.19 | 8.28 | 80.58 | 0.16 | 2.43 | 420 |
| 2024-09-20 22:21:39.524 | MS1 | 121.4656584631 | 31.1446360112 | 410 | 504990 | -91.32 | 7.24 | 74.09 | 0.08 | 2.16 | 426 |
| 2024-09-20 22:21:40.113 | MS1 | 121.4656741406 | 31.1446295221 | 410 | 504990 | -91.41 | 8.17 | 308.62 | 0.12 | 2.31 | 1563 |
| 2024-09-20 22:21:41.867 | MS1 | 121.4656760991 | 31.1446324364 | 410 | 504990 | -91.87 | 11.41 | 599.85 | 0.03 | 2.48 | 1587 |
| 2024-09-20 22:21:42.302 | MS1 | 121.4656779444 | 31.1446319600 | 410 | 504990 | -91.36 | 11.72 | 533.48 | 0.19 | 2.40 | 1595 |

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
| 3247393 | 4 | 121.4651715019 | 31.1472468591 | 249 | 0 | 11 | 38.2 | TDD | 350 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3261990 | 2 | 121.4751828720 | 31.1539678502 | 6 | 2 | 10 | 46.6 | TDD | 410 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3262519 | 3 | 121.4734013387 | 31.1482989755 | 359 | 5 | 3 | 37.3 | TDD | 741 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3268426 | 1 | 121.4654370640 | 31.1501074119 | 67 | 8 | 12 | 42.4 | TDD | 641 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.588 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.612 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.715 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.715 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.445 | NREventA3 | measId:2;ServCellPCI:138;Se... |
| 2024-09-20 22:21:38.685 | NRHandoverAttempt | SourcePCI:138;SourceNR-ARFC... |
| 2024-09-20 22:21:38.720 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.732 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.864 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.864 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268426 | 1 | 7.8113 | 12.0196 | -116.1737 | 12.6497 | 128.9395 | 0.0151 | 0.0061 |
| 2024_09_20 22:00 | 3261990 | 2 | 14.8705 | 5.3831 | -117.7099 | 17.2996 | 136.7790 | 0.0150 | 0.0125 |
| 2024_09_20 22:00 | 3262519 | 3 | 15.0534 | 9.3065 | -114.4797 | 6.7565 | 82.1003 | 0.0179 | 0.0063 |
| 2024_09_20 22:00 | 3247393 | 4 | 6.4049 | 16.4200 | -116.2079 | 17.7691 | 179.0611 | 0.0028 | 0.0024 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416840_A608DCB0 | 504990 | 410 | -92.2 | 504990 | 741 | -98.3 | 504990 | 350 | -98.8 | 504990 | 641 |
| MR_1774416840_0EB3F550 | 504990 | 410 | -91.9 | 504990 | 741 | -98.8 | 504990 | 350 | -97.4 | 504990 | 641 |
| MR_1774416840_D01B836A | 504990 | 410 | -92.5 | 504990 | 741 | -95.2 | 504990 | 350 | -99.6 | 504990 | 641 |
| MR_1774416840_38F9240B | 504990 | 410 | -89.8 | 504990 | 741 | -97.3 | 504990 | 350 | -96.7 | 504990 | 641 |
| MR_1774416840_09D067EE | 504990 | 410 | -88.8 | 504990 | 741 | -98.9 | 504990 | 350 | -96.7 | 504990 | 641 |
| MR_1774416840_02014A04 | 504990 | 410 | -89.6 | 504990 | 741 | -95.6 | 504990 | 350 | -98.7 | 504990 | 641 |
| MR_1774416840_7DEDE5B3 | 504990 | 410 | -90.9 | 504990 | 741 | -98.0 | 504990 | 350 | -100.0 | 504990 | 641 |
| MR_1774416840_702234AA | 504990 | 410 | -92.4 | 504990 | 741 | -97.4 | 504990 | 350 | -98.3 | 504990 | 641 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 102: `40e31b37-608...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `40e31b37-608c-4e96-8f70-003bf488b99c` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[102] topology](images/test_0102.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3253640_1 and 3271716_3
- `C2`: Decrease transmission power for 3271716_3
- `C3`: Adjust the azimuth of 3253640_1 by 50 degrees
- `C4`: Increase A3 Offset threshold for 3271716_3
- `C5`: Add neighbor relationship between 3254045_2 and 3271716_3
- `C6`: Adjust the azimuth of 3271716_3 by 50 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Check test server and transmission issues
- `C9`: Increase A3 Offset threshold for 3253640_1
- `C10`: Decrease A3 Offset threshold for 3271716_3
- `C11`: Increase transmission power for 3271716_3
- `C12`: Decrease transmission power for 3253640_1
- `C13`: Decrease A3 Offset threshold for 3253640_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271716_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253640_1
- `C16`: Lift the tilt angle  of 3271716_3 by 9 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271716_3
- `C18`: Increase transmission power for 3253640_1
- `C19`: Lift the tilt angle of 3253640_1 by 10 degrees
- `C20`: Press down the tilt angle of 3253640_1 by 10 degrees
- `C21`: Press down the tilt angle  of 3271716_3 by 9 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253640_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.750 | MS1 | 121.4656636345 | 31.1446227318 | 704 | 504990 | -91.85 | 16.26 | 314.56 | 0.20 | 2.07 | 1592 |
| 2024-09-20 22:21:32.828 | MS1 | 121.4656596456 | 31.1446265605 | 704 | 504990 | -89.32 | 13.94 | 528.91 | 0.05 | 2.75 | 1576 |
| 2024-09-20 22:21:33.685 | MS1 | 121.4656677957 | 31.1446181955 | 704 | 504990 | -89.46 | 17.26 | 370.21 | 0.13 | 2.97 | 1597 |
| 2024-09-20 22:21:34.787 | MS1 | 121.4656727294 | 31.1446181906 | 704 | 504990 | -88.13 | 17.08 | 47.94 | 0.12 | 2.33 | 1593 |
| 2024-09-20 22:21:35.867 | MS1 | 121.4656766039 | 31.1446253095 | 704 | 504990 | -86.53 | 14.20 | 89.02 | 0.01 | 2.36 | 1585 |
| 2024-09-20 22:21:36.299 | MS1 | 121.4656663055 | 31.1446201374 | 704 | 504990 | -86.33 | 15.92 | 60.95 | 0.01 | 2.23 | 1567 |
| 2024-09-20 22:21:37.552 | MS1 | 121.4656638957 | 31.1446194662 | 704 | 504990 | -89.22 | 12.84 | 86.05 | 0.07 | 2.93 | 1582 |
| 2024-09-20 22:21:38.686 | MS1 | 121.4656620101 | 31.1446310457 | 704 | 504990 | -92.04 | 12.85 | 57.56 | 0.03 | 2.38 | 1595 |
| 2024-09-20 22:21:39.165 | MS1 | 121.4656652826 | 31.1446297552 | 704 | 504990 | -92.97 | 8.40 | 55.60 | 0.00 | 2.10 | 1582 |
| 2024-09-20 22:21:40.776 | MS1 | 121.4656657442 | 31.1446195090 | 704 | 504990 | -92.44 | 7.61 | 388.22 | 0.15 | 2.07 | 1565 |
| 2024-09-20 22:21:41.581 | MS1 | 121.4656713045 | 31.1446218125 | 704 | 504990 | -92.94 | 9.61 | 338.02 | 0.02 | 2.38 | 1587 |
| 2024-09-20 22:21:42.315 | MS1 | 121.4656632823 | 31.1446181465 | 704 | 504990 | -91.85 | 9.21 | 308.57 | 0.14 | 2.66 | 1588 |

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
| 3253640 | 1 | 121.4743691960 | 31.1449185727 | 92 | 13 | 12 | 48.5 | TDD | 704 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3254045 | 2 | 121.4662691469 | 31.1539508518 | 162 | 3 | 6 | 29.5 | TDD | 577 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3271716 | 3 | 121.4661662061 | 31.1552882116 | 14 | 8 | 1 | 25.0 | TDD | 98 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3276125 | 4 | 121.4724686617 | 31.1478605000 | 286 | 13 | 8 | 45.4 | TDD | 351 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.892 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.892 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.658 | NREventA3 | measId:2;ServCellPCI:607;Se... |
| 2024-09-20 22:21:37.898 | NRHandoverAttempt | SourcePCI:607;SourceNR-ARFC... |
| 2024-09-20 22:21:37.946 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.961 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.104 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.104 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3253640 | 1 | 77.5468 | 91.3540 | -114.1700 | 14.2021 | 155.0504 | 0.0030 | 0.0068 |
| 2024_09_19 22:00 | 3254045 | 2 | 88.9001 | 94.6958 | -115.1806 | 10.0392 | 109.6238 | 0.0076 | 0.0056 |
| 2024_09_19 22:00 | 3271716 | 3 | 90.3795 | 75.1843 | -114.7110 | 11.6300 | 107.7084 | 0.0110 | 0.0074 |
| 2024_09_19 22:00 | 3276125 | 4 | 91.4566 | 90.2950 | -114.5992 | 19.1748 | 157.7333 | 0.0060 | 0.0125 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413600_E56D768A | 504990 | 704 | -87.5 | 504990 | 98 | -94.5 | 504990 | 577 | -98.8 | 504990 | 351 |
| MR_1774413600_860AA276 | 504990 | 704 | -89.4 | 504990 | 98 | -93.5 | 504990 | 577 | -96.2 | 504990 | 351 |
| MR_1774413600_C71F009D | 504990 | 704 | -89.2 | 504990 | 98 | -94.5 | 504990 | 577 | -96.4 | 504990 | 351 |
| MR_1774413600_D2E5FF61 | 504990 | 704 | -89.2 | 504990 | 98 | -92.7 | 504990 | 577 | -99.6 | 504990 | 351 |
| MR_1774413600_7A71CA7F | 504990 | 704 | -86.4 | 504990 | 98 | -93.3 | 504990 | 577 | -99.4 | 504990 | 351 |
| MR_1774413600_74D9C45D | 504990 | 704 | -89.9 | 504990 | 98 | -92.6 | 504990 | 577 | -98.9 | 504990 | 351 |
| MR_1774413600_DABBB3CC | 504990 | 704 | -89.7 | 504990 | 98 | -92.3 | 504990 | 577 | -96.0 | 504990 | 351 |
| MR_1774413600_80A08E35 | 504990 | 704 | -88.9 | 504990 | 98 | -92.9 | 504990 | 577 | -99.6 | 504990 | 351 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 103: `887b70e0-ae2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `887b70e0-ae2c-4d5b-a748-0ab57809c9aa` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[103] topology](images/test_0103.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3245464_1 by 6 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237820_2
- `C3`: Lift the tilt angle  of 3245464_1 by 6 degrees
- `C4`: Adjust the azimuth of 3237820_2 by 15 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245464_1
- `C6`: Check test server and transmission issues
- `C7`: Adjust the azimuth of 3245464_1 by 48 degrees
- `C8`: Decrease transmission power for 3245464_1
- `C9`: Add neighbor relationship between 3256834_3 and 3245464_1
- `C10`: Increase transmission power for 3237820_2
- `C11`: Lift the tilt angle of 3237820_2 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245464_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237820_2
- `C14`: Decrease A3 Offset threshold for 3245464_1
- `C15`: Increase A3 Offset threshold for 3245464_1
- `C16`: Add neighbor relationship between 3237820_2 and 3245464_1
- `C17`: Increase A3 Offset threshold for 3237820_2
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Increase transmission power for 3245464_1
- `C20`: Press down the tilt angle of 3237820_2 by 10 degrees
- `C21`: Decrease transmission power for 3237820_2
- `C22`: Decrease A3 Offset threshold for 3237820_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.247 | MS1 | 121.4656743531 | 31.1446240577 | 111 | 504990 | -84.59 | 16.22 | 510.11 | 0.03 | 2.66 | 1590 |
| 2024-09-20 22:21:32.960 | MS1 | 121.4656581937 | 31.1446327723 | 111 | 504990 | -79.43 | 15.10 | 471.56 | 0.19 | 2.48 | 1592 |
| 2024-09-20 22:21:33.429 | MS1 | 121.4656723333 | 31.1446306019 | 111 | 504990 | -79.24 | 16.69 | 396.15 | 0.11 | 2.02 | 1560 |
| 2024-09-20 22:21:34.138 | MS1 | 121.4656599522 | 31.1446286111 | 111 | 504990 | -85.74 | -2.76 | 64.37 | 0.12 | 1.30 | 1573 |
| 2024-09-20 22:21:35.113 | MS1 | 121.4656699074 | 31.1446205176 | 111 | 504990 | -92.35 | -0.82 | 55.82 | 0.08 | 1.20 | 1584 |
| 2024-09-20 22:21:36.610 | MS1 | 121.4656708962 | 31.1446235472 | 111 | 504990 | -89.59 | -2.84 | 55.24 | 0.03 | 1.31 | 1584 |
| 2024-09-20 22:21:37.521 | MS1 | 121.4656589735 | 31.1446357692 | 111 | 504990 | -85.21 | -1.33 | 59.04 | 0.10 | 1.30 | 1587 |
| 2024-09-20 22:21:38.191 | MS1 | 121.4656698086 | 31.1446305281 | 111 | 504990 | -76.59 | 12.03 | 569.93 | 0.02 | 1.47 | 1564 |
| 2024-09-20 22:21:39.945 | MS1 | 121.4656751696 | 31.1446277589 | 111 | 504990 | -82.86 | 13.52 | 520.09 | 0.08 | 1.22 | 1584 |
| 2024-09-20 22:21:40.558 | MS1 | 121.4656713586 | 31.1446291765 | 111 | 504990 | -81.33 | 15.65 | 500.10 | 0.11 | 2.67 | 1573 |
| 2024-09-20 22:21:41.273 | MS1 | 121.4656673768 | 31.1446304911 | 111 | 504990 | -80.74 | 12.90 | 402.22 | 0.11 | 2.92 | 1564 |
| 2024-09-20 22:21:42.660 | MS1 | 121.4656590053 | 31.1446275604 | 111 | 504990 | -82.01 | 17.66 | 487.87 | 0.01 | 2.96 | 1563 |

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
| 3237820 | 2 | 121.4654971726 | 31.1529594618 | 194 | 10 | 10 | 27.3 | TDD | 111 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3240209 | 4 | 121.4738641314 | 31.1481779661 | 119 | 0 | 10 | 37.5 | TDD | 535 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3245464 | 1 | 121.4679052391 | 31.1524663142 | 242 | 3 | 0 | 40.8 | TDD | 602 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3256834 | 3 | 121.4708502683 | 31.1451121708 | 73 | 14 | 11 | 28.0 | TDD | 349 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.322 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.345 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.484 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.484 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.123 | NREventA3 | measId:2;ServCellPCI:822;Se... |
| 2024-09-20 22:21:36.123 | NREventA3 | measId:2;ServCellPCI:822;Se... |
| 2024-09-20 22:21:37.123 | NREventA3 | measId:2;ServCellPCI:822;Se... |
| 2024-09-20 22:21:39.623 | NRRRCReestablishAttempt | PCI:822 |
| 2024-09-20 22:21:39.637 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.648 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.792 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.792 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245464 | 1 | 12.6311 | 17.0161 | -115.0880 | 11.7692 | 191.1780 | 0.0172 | 0.0191 |
| 2024_09_20 22:00 | 3237820 | 2 | 15.9721 | 5.6508 | -114.6960 | 19.2569 | 159.7902 | 0.0051 | 0.1111 |
| 2024_09_20 22:00 | 3256834 | 3 | 15.1553 | 9.7794 | -114.8981 | 13.5266 | 135.9691 | 0.0000 | 0.0179 |
| 2024_09_20 22:00 | 3240209 | 4 | 17.4088 | 15.5982 | -117.1313 | 18.8413 | 153.1917 | 0.0068 | 0.0127 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413173_C26E2558 | 504990 | 602 | -81.1 | 504990 | 111 | -85.9 | 504990 | 349 | -91.8 | 504990 | 535 |
| MR_1774413173_88612606 | 504990 | 111 | -87.5 | 504990 | 602 | -81.4 | 504990 | 349 | -91.2 | 504990 | 535 |
| MR_1774413173_678CAD04 | 504990 | 602 | -79.8 | 504990 | 111 | -84.1 | 504990 | 349 | -88.2 | 504990 | 535 |
| MR_1774413173_6562B4E0 | 504990 | 602 | -80.2 | 504990 | 111 | -85.0 | 504990 | 349 | -87.9 | 504990 | 535 |
| MR_1774413173_FE05DE7B | 504990 | 111 | -85.3 | 504990 | 602 | -79.7 | 504990 | 349 | -91.6 | 504990 | 535 |
| MR_1774413173_BFF8F0BE | 504990 | 602 | -81.5 | 504990 | 111 | -84.8 | 504990 | 349 | -91.6 | 504990 | 535 |
| MR_1774413173_DC17EB02 | 504990 | 602 | -81.5 | 504990 | 111 | -84.8 | 504990 | 349 | -89.2 | 504990 | 535 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 104: `be04ca82-4b5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `be04ca82-4b52-4b2d-b464-d9f36a5e5167` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[104] topology](images/test_0104.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3253386_4 by 4 degrees
- `C2`: Press down the tilt angle of 3253386_4 by 4 degrees
- `C3`: Lift the tilt angle  of 3222765_3 by 10 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253386_4
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222765_3
- `C7`: Add neighbor relationship between 3247950_2 and 3222765_3
- `C8`: Adjust the azimuth of 3253386_4 by 50 degrees
- `C9`: Increase A3 Offset threshold for 3253386_4
- `C10`: Press down the tilt angle  of 3222765_3 by 10 degrees
- `C11`: Decrease A3 Offset threshold for 3253386_4
- `C12`: Increase A3 Offset threshold for 3222765_3
- `C13`: Adjust the azimuth of 3222765_3 by 3 degrees
- `C14`: Add neighbor relationship between 3253386_4 and 3222765_3
- `C15`: Decrease transmission power for 3222765_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253386_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222765_3
- `C18`: Increase transmission power for 3222765_3
- `C19`: Decrease transmission power for 3253386_4
- `C20`: Increase transmission power for 3253386_4
- `C21`: Decrease A3 Offset threshold for 3222765_3
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.590 | MS1 | 121.4656674158 | 31.1446271267 | 909 | 504990 | -84.01 | 15.48 | 508.41 | 0.03 | 2.17 | 1583 |
| 2024-09-20 22:21:32.984 | MS1 | 121.4656580682 | 31.1446371572 | 909 | 504990 | -82.82 | 14.86 | 525.50 | 0.02 | 2.63 | 1576 |
| 2024-09-20 22:21:33.362 | MS1 | 121.4656637723 | 31.1446315598 | 909 | 504990 | -75.52 | 14.33 | 427.90 | 0.20 | 2.49 | 1592 |
| 2024-09-20 22:21:34.126 | MS1 | 121.4656765954 | 31.1446243836 | 909 | 504990 | -90.77 | -2.94 | 37.75 | 0.19 | 1.25 | 1577 |
| 2024-09-20 22:21:35.383 | MS1 | 121.4656752499 | 31.1446217029 | 909 | 504990 | -88.31 | -0.60 | 71.35 | 0.19 | 1.45 | 1582 |
| 2024-09-20 22:21:36.989 | MS1 | 121.4656603969 | 31.1446218942 | 909 | 504990 | -92.98 | -0.39 | 47.17 | 0.11 | 1.48 | 1566 |
| 2024-09-20 22:21:37.194 | MS1 | 121.4656658677 | 31.1446290262 | 909 | 504990 | -83.75 | -0.56 | 53.26 | 0.04 | 1.37 | 1563 |
| 2024-09-20 22:21:38.341 | MS1 | 121.4656621698 | 31.1446334357 | 909 | 504990 | -92.47 | -1.50 | 56.26 | 0.08 | 1.35 | 1564 |
| 2024-09-20 22:21:39.437 | MS1 | 121.4656594881 | 31.1446253328 | 435 | 504990 | -80.12 | 16.13 | 229.35 | 0.12 | 1.22 | 1572 |
| 2024-09-20 22:21:40.333 | MS1 | 121.4656637579 | 31.1446344691 | 435 | 504990 | -80.59 | 12.91 | 443.50 | 0.08 | 2.49 | 1589 |
| 2024-09-20 22:21:41.108 | MS1 | 121.4656605889 | 31.1446345034 | 435 | 504990 | -75.25 | 13.34 | 541.98 | 0.15 | 2.25 | 1592 |
| 2024-09-20 22:21:42.835 | MS1 | 121.4656729753 | 31.1446256726 | 435 | 504990 | -76.97 | 16.59 | 366.31 | 0.07 | 2.02 | 1571 |

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
| 3222765 | 3 | 121.4725378509 | 31.1453941034 | 260 | 10 | 9 | 31.6 | TDD | 435 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3247950 | 2 | 121.4683317946 | 31.1492119020 | 148 | 13 | 12 | 35.6 | TDD | 689 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3248571 | 1 | 121.4698341225 | 31.1515936905 | 18 | 5 | 0 | 38.9 | TDD | 464 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3253386 | 4 | 121.4728185549 | 31.1505863865 | 287 | 2 | 4 | 29.6 | TDD | 909 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.881 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.902 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.008 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.008 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.734 | NREventA3 | measId:2;ServCellPCI:979;Se... |
| 2024-09-20 22:21:37.974 | NRHandoverAttempt | SourcePCI:979;SourceNR-ARFC... |
| 2024-09-20 22:21:38.019 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.031 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.151 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.151 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248571 | 1 | 15.5943 | 6.1880 | -116.9470 | 7.2697 | 156.4474 | 0.0087 | 0.0084 |
| 2024_09_20 22:00 | 3247950 | 2 | 18.2223 | 11.1797 | -117.6181 | 12.5007 | 185.6006 | 0.0089 | 0.0071 |
| 2024_09_20 22:00 | 3222765 | 3 | 16.8322 | 8.6658 | -117.2206 | 6.7564 | 112.4506 | 0.0069 | 0.0138 |
| 2024_09_20 22:00 | 3253386 | 4 | 16.5937 | 5.4737 | -115.0229 | 15.6738 | 163.3323 | 0.0178 | 0.1486 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414758_486FD49B | 504990 | 909 | -90.9 | 504990 | 435 | -85.5 | 504990 | 689 | -94.8 | 504990 | 464 |
| MR_1774414758_8BC6CD90 | 504990 | 909 | -89.3 | 504990 | 435 | -86.1 | 504990 | 689 | -94.1 | 504990 | 464 |
| MR_1774414758_C849551B | 504990 | 435 | -85.1 | 504990 | 909 | -91.3 | 504990 | 689 | -94.7 | 504990 | 464 |
| MR_1774414758_5C5342B9 | 504990 | 909 | -90.2 | 504990 | 435 | -86.2 | 504990 | 689 | -96.3 | 504990 | 464 |
| MR_1774414758_CBD9D41B | 504990 | 435 | -85.3 | 504990 | 909 | -90.6 | 504990 | 689 | -93.6 | 504990 | 464 |
| MR_1774414758_7C204A88 | 504990 | 909 | -89.0 | 504990 | 435 | -87.3 | 504990 | 689 | -94.3 | 504990 | 464 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 105: `664d75d3-5ee...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `664d75d3-5ee0-4c4c-90c7-5eebbbcbb7bc` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[105] topology](images/test_0105.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Lift the tilt angle of 3272451_1 by 8 degrees
- `C3`: Increase A3 Offset threshold for 3274024_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272451_1
- `C5`: Lift the tilt angle  of 3274024_2 by 4 degrees
- `C6`: Increase transmission power for 3274024_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274024_2
- `C8`: Check test server and transmission issues
- `C9`: Add neighbor relationship between 3272451_1 and 3274024_2
- `C10`: Adjust the azimuth of 3274024_2 by 50 degrees
- `C11`: Press down the tilt angle  of 3274024_2 by 4 degrees
- `C12`: Increase A3 Offset threshold for 3272451_1
- `C13`: Decrease transmission power for 3272451_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274024_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272451_1
- `C16`: Increase transmission power for 3272451_1
- `C17`: Decrease A3 Offset threshold for 3274024_2
- `C18`: Adjust the azimuth of 3272451_1 by 50 degrees
- `C19`: Decrease A3 Offset threshold for 3272451_1
- `C20`: Press down the tilt angle of 3272451_1 by 8 degrees
- `C21`: Decrease transmission power for 3274024_2
- `C22`: Add neighbor relationship between 3263225_3 and 3274024_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.495 | MS1 | 121.4656606637 | 31.1446320220 | 80 | 504990 | -90.36 | 13.76 | 376.63 | 0.10 | 2.88 | 1577 |
| 2024-09-20 22:21:32.849 | MS1 | 121.4656757143 | 31.1446188985 | 80 | 504990 | -86.62 | 16.89 | 593.32 | 0.05 | 2.71 | 1590 |
| 2024-09-20 22:21:33.808 | MS1 | 121.4656705690 | 31.1446224103 | 80 | 504990 | -87.62 | 16.34 | 422.00 | 0.15 | 2.86 | 1577 |
| 2024-09-20 22:21:34.756 | MS1 | 121.4656654791 | 31.1446222416 | 80 | 504990 | -88.65 | 15.75 | 73.01 | 0.16 | 2.09 | 465 |
| 2024-09-20 22:21:35.148 | MS1 | 121.4656581654 | 31.1446343651 | 80 | 504990 | -90.56 | 16.22 | 75.03 | 0.02 | 2.18 | 317 |
| 2024-09-20 22:21:36.625 | MS1 | 121.4656613524 | 31.1446238959 | 80 | 504990 | -85.20 | 12.84 | 57.54 | 0.14 | 2.81 | 486 |
| 2024-09-20 22:21:37.130 | MS1 | 121.4656639314 | 31.1446274819 | 80 | 504990 | -91.96 | 11.16 | 55.62 | 0.01 | 2.88 | 447 |
| 2024-09-20 22:21:38.215 | MS1 | 121.4656644488 | 31.1446308420 | 80 | 504990 | -92.97 | 9.56 | 86.36 | 0.18 | 2.48 | 471 |
| 2024-09-20 22:21:39.807 | MS1 | 121.4656695776 | 31.1446210209 | 80 | 504990 | -89.63 | 9.34 | 52.85 | 0.09 | 2.52 | 490 |
| 2024-09-20 22:21:40.857 | MS1 | 121.4656685705 | 31.1446294392 | 80 | 504990 | -89.72 | 9.80 | 498.74 | 0.00 | 2.51 | 1590 |
| 2024-09-20 22:21:41.356 | MS1 | 121.4656715630 | 31.1446346468 | 80 | 504990 | -92.26 | 7.76 | 531.09 | 0.17 | 2.36 | 1589 |
| 2024-09-20 22:21:42.183 | MS1 | 121.4656767571 | 31.1446245185 | 80 | 504990 | -90.79 | 7.20 | 417.82 | 0.14 | 2.35 | 1589 |

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
| 3252096 | 4 | 121.4706336002 | 31.1459512771 | 117 | 8 | 1 | 26.3 | TDD | 6 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3263225 | 3 | 121.4700640866 | 31.1544861067 | 92 | 13 | 4 | 17.1 | TDD | 160 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3272451 | 1 | 121.4753534376 | 31.1463333312 | 23 | 6 | 11 | 37.5 | TDD | 80 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3274024 | 2 | 121.4740544754 | 31.1483178243 | 301 | 2 | 10 | 26.4 | TDD | 1002 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.817 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.840 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.975 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.975 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.697 | NREventA3 | measId:2;ServCellPCI:990;Se... |
| 2024-09-20 22:21:37.937 | NRHandoverAttempt | SourcePCI:990;SourceNR-ARFC... |
| 2024-09-20 22:21:37.977 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.988 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.115 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.115 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272451 | 1 | 16.9365 | 10.5861 | -117.5455 | 14.2704 | 142.4264 | 0.0017 | 0.0146 |
| 2024_09_20 22:00 | 3274024 | 2 | 5.3667 | 13.2536 | -115.4168 | 18.2053 | 135.2736 | 0.0061 | 0.0030 |
| 2024_09_20 22:00 | 3263225 | 3 | 18.1600 | 5.5281 | -115.5213 | 17.8519 | 114.1366 | 0.0108 | 0.0181 |
| 2024_09_20 22:00 | 3252096 | 4 | 10.3574 | 13.6886 | -117.6423 | 18.3178 | 129.9984 | 0.0146 | 0.0049 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416684_DF2C1DCE | 504990 | 80 | -89.3 | 504990 | 1002 | -91.9 | 504990 | 160 | -99.4 | 504990 | 6 |
| MR_1774416684_D293173F | 504990 | 80 | -90.4 | 504990 | 1002 | -95.1 | 504990 | 160 | -102.0 | 504990 | 6 |
| MR_1774416684_2BD00C4F | 504990 | 80 | -89.8 | 504990 | 1002 | -91.8 | 504990 | 160 | -100.2 | 504990 | 6 |
| MR_1774416684_69BE3E00 | 504990 | 80 | -86.7 | 504990 | 1002 | -91.7 | 504990 | 160 | -98.9 | 504990 | 6 |
| MR_1774416684_E4552275 | 504990 | 80 | -90.1 | 504990 | 1002 | -92.9 | 504990 | 160 | -101.3 | 504990 | 6 |
| MR_1774416684_3DDCE5E1 | 504990 | 80 | -89.5 | 504990 | 1002 | -94.0 | 504990 | 160 | -99.7 | 504990 | 6 |
| MR_1774416684_94D317C2 | 504990 | 80 | -88.2 | 504990 | 1002 | -91.7 | 504990 | 160 | -98.7 | 504990 | 6 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 106: `9f4f1d2d-f72...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9f4f1d2d-f722-4ee7-8802-3d299e805acc` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[106] topology](images/test_0106.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250697_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263741_1
- `C3`: Increase transmission power for 3263741_1
- `C4`: Lift the tilt angle  of 3250697_2 by 9 degrees
- `C5`: Lift the tilt angle of 3263741_1 by 5 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263741_1
- `C7`: Press down the tilt angle of 3263741_1 by 5 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250697_2
- `C9`: Check test server and transmission issues
- `C10`: Decrease transmission power for 3263741_1
- `C11`: Decrease A3 Offset threshold for 3250697_2
- `C12`: Increase A3 Offset threshold for 3263741_1
- `C13`: Decrease A3 Offset threshold for 3263741_1
- `C14`: Add neighbor relationship between 3239744_3 and 3250697_2
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease transmission power for 3250697_2
- `C17`: Increase transmission power for 3250697_2
- `C18`: Adjust the azimuth of 3263741_1 by 17 degrees
- `C19`: Add neighbor relationship between 3263741_1 and 3250697_2
- `C20`: Press down the tilt angle  of 3250697_2 by 9 degrees
- `C21`: Increase A3 Offset threshold for 3250697_2
- `C22`: Adjust the azimuth of 3250697_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.182 | MS1 | 121.4656660908 | 31.1446259972 | 394 | 504990 | -86.61 | 17.35 | 500.00 | 0.03 | 2.19 | 1571 |
| 2024-09-20 22:21:32.131 | MS1 | 121.4656631528 | 31.1446288246 | 394 | 504990 | -88.18 | 14.39 | 359.41 | 0.10 | 2.82 | 1590 |
| 2024-09-20 22:21:33.331 | MS1 | 121.4656717756 | 31.1446258767 | 394 | 504990 | -90.42 | 15.86 | 310.43 | 0.09 | 2.06 | 1593 |
| 2024-09-20 22:21:34.461 | MS1 | 121.4656665680 | 31.1446333834 | 394 | 504990 | -85.38 | 17.85 | 91.74 | 0.67 | 2.66 | 659 |
| 2024-09-20 22:21:35.442 | MS1 | 121.4656664872 | 31.1446334883 | 394 | 504990 | -90.20 | 14.82 | 57.77 | 0.64 | 2.41 | 664 |
| 2024-09-20 22:21:36.518 | MS1 | 121.4656627836 | 31.1446320374 | 394 | 504990 | -85.32 | 14.99 | 82.71 | 0.52 | 2.93 | 562 |
| 2024-09-20 22:21:37.236 | MS1 | 121.4656601930 | 31.1446241874 | 394 | 504990 | -89.88 | 8.31 | 97.37 | 0.64 | 2.62 | 674 |
| 2024-09-20 22:21:38.708 | MS1 | 121.4656668867 | 31.1446291251 | 394 | 504990 | -92.82 | 11.89 | 57.00 | 0.56 | 2.85 | 659 |
| 2024-09-20 22:21:39.804 | MS1 | 121.4656776696 | 31.1446237213 | 394 | 504990 | -91.12 | 9.91 | 79.40 | 0.68 | 2.25 | 507 |
| 2024-09-20 22:21:40.640 | MS1 | 121.4656773331 | 31.1446342414 | 394 | 504990 | -91.80 | 7.88 | 520.78 | 0.13 | 2.08 | 1565 |
| 2024-09-20 22:21:41.471 | MS1 | 121.4656733913 | 31.1446324050 | 394 | 504990 | -93.84 | 9.79 | 376.48 | 0.04 | 2.26 | 1576 |
| 2024-09-20 22:21:42.485 | MS1 | 121.4656678197 | 31.1446184194 | 394 | 504990 | -91.22 | 7.41 | 438.13 | 0.08 | 2.88 | 1584 |

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
| 3239744 | 3 | 121.4741431148 | 31.1493659875 | 19 | 0 | 10 | 34.5 | TDD | 15 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3243483 | 4 | 121.4727860246 | 31.1532549522 | 178 | 15 | 6 | 48.6 | TDD | 783 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3250697 | 2 | 121.4754202272 | 31.1502111011 | 320 | 8 | 10 | 29.1 | TDD | 699 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3263741 | 1 | 121.4673221310 | 31.1541397273 | 205 | 3 | 10 | 40.7 | TDD | 394 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.085 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.105 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.235 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.235 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.941 | NREventA3 | measId:2;ServCellPCI:892;Se... |
| 2024-09-20 22:21:38.181 | NRHandoverAttempt | SourcePCI:892;SourceNR-ARFC... |
| 2024-09-20 22:21:38.231 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.242 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.363 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.363 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263741 | 1 | 17.7741 | 19.6337 | -116.8397 | 15.4380 | 104.8463 | 0.0155 | 0.0089 |
| 2024_09_20 22:00 | 3250697 | 2 | 11.8229 | 14.4204 | -117.5571 | 7.5565 | 146.9026 | 0.0057 | 0.0082 |
| 2024_09_20 22:00 | 3239744 | 3 | 18.1405 | 12.6017 | -117.6246 | 11.9824 | 146.5187 | 0.0012 | 0.0007 |
| 2024_09_20 22:00 | 3243483 | 4 | 16.0218 | 8.1025 | -114.6465 | 6.5508 | 184.3228 | 0.0170 | 0.0028 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415417_B3F6A92D | 504990 | 394 | -84.8 | 504990 | 699 | -90.8 | 504990 | 15 | -100.0 | 504990 | 783 |
| MR_1774415417_0C9B6F9F | 504990 | 394 | -86.0 | 504990 | 699 | -91.9 | 504990 | 15 | -97.9 | 504990 | 783 |
| MR_1774415417_99DE48A9 | 504990 | 394 | -86.8 | 504990 | 699 | -91.0 | 504990 | 15 | -99.9 | 504990 | 783 |
| MR_1774415417_9EF53FC1 | 504990 | 394 | -83.6 | 504990 | 699 | -92.3 | 504990 | 15 | -99.5 | 504990 | 783 |
| MR_1774415417_C10BD51D | 504990 | 394 | -84.2 | 504990 | 699 | -91.1 | 504990 | 15 | -100.6 | 504990 | 783 |
| MR_1774415417_9921B01B | 504990 | 394 | -84.1 | 504990 | 699 | -90.9 | 504990 | 15 | -98.3 | 504990 | 783 |
| MR_1774415417_671A820C | 504990 | 394 | -87.2 | 504990 | 699 | -91.5 | 504990 | 15 | -99.8 | 504990 | 783 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 107: `42ef2542-0fb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `42ef2542-0fb3-45ed-953c-e4fb5541390f` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[107] topology](images/test_0107.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3253443_1
- `C2`: Check test server and transmission issues
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220569_2
- `C4`: Add neighbor relationship between 3220569_2 and 3253443_1
- `C5`: Decrease transmission power for 3220569_2
- `C6`: Press down the tilt angle of 3220569_2 by 10 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253443_1
- `C8`: Adjust the azimuth of 3253443_1 by 50 degrees
- `C9`: Increase A3 Offset threshold for 3220569_2
- `C10`: Press down the tilt angle  of 3253443_1 by 10 degrees
- `C11`: Add neighbor relationship between 3273339_4 and 3253443_1
- `C12`: Lift the tilt angle of 3220569_2 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3253443_1
- `C14`: Adjust the azimuth of 3220569_2 by 50 degrees
- `C15`: Lift the tilt angle  of 3253443_1 by 10 degrees
- `C16`: Increase transmission power for 3220569_2
- `C17`: Increase A3 Offset threshold for 3253443_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220569_2
- `C19`: Increase transmission power for 3253443_1
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253443_1
- `C22`: Decrease A3 Offset threshold for 3220569_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.418 | MS1 | 121.4656775543 | 31.1446267564 | 482 | 504990 | -91.36 | 14.15 | 426.43 | 0.08 | 2.36 | 1591 |
| 2024-09-20 22:21:32.175 | MS1 | 121.4656743521 | 31.1446247127 | 482 | 504990 | -88.65 | 17.38 | 458.39 | 0.15 | 2.85 | 1564 |
| 2024-09-20 22:21:33.105 | MS1 | 121.4656638868 | 31.1446260267 | 482 | 504990 | -89.79 | 13.20 | 373.15 | 0.07 | 2.76 | 1571 |
| 2024-09-20 22:21:34.683 | MS1 | 121.4656768865 | 31.1446351813 | 482 | 504990 | -90.86 | 17.98 | 82.11 | 0.20 | 2.86 | 1564 |
| 2024-09-20 22:21:35.741 | MS1 | 121.4656662160 | 31.1446305863 | 482 | 504990 | -88.41 | 15.06 | 61.58 | 0.14 | 2.89 | 1560 |
| 2024-09-20 22:21:36.970 | MS1 | 121.4656584786 | 31.1446271011 | 482 | 504990 | -89.56 | 15.52 | 68.35 | 0.04 | 2.02 | 1585 |
| 2024-09-20 22:21:37.812 | MS1 | 121.4656698315 | 31.1446193869 | 482 | 504990 | -91.06 | 7.38 | 79.28 | 0.17 | 2.40 | 1581 |
| 2024-09-20 22:21:38.567 | MS1 | 121.4656754728 | 31.1446344291 | 482 | 504990 | -91.76 | 12.32 | 59.36 | 0.09 | 2.89 | 1585 |
| 2024-09-20 22:21:39.133 | MS1 | 121.4656685491 | 31.1446326384 | 482 | 504990 | -92.09 | 12.04 | 89.92 | 0.05 | 2.42 | 1599 |
| 2024-09-20 22:21:40.709 | MS1 | 121.4656643505 | 31.1446376057 | 482 | 504990 | -90.67 | 8.02 | 576.69 | 0.16 | 2.10 | 1584 |
| 2024-09-20 22:21:41.325 | MS1 | 121.4656715206 | 31.1446366090 | 482 | 504990 | -92.57 | 12.57 | 461.11 | 0.05 | 2.77 | 1564 |
| 2024-09-20 22:21:42.159 | MS1 | 121.4656763717 | 31.1446222820 | 482 | 504990 | -91.09 | 11.41 | 381.22 | 0.18 | 2.79 | 1593 |

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
| 3220569 | 2 | 121.4758664068 | 31.1459296526 | 346 | 13 | 6 | 16.4 | TDD | 482 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3253443 | 1 | 121.4681570123 | 31.1508070195 | 262 | 8 | 6 | 39.5 | TDD | 160 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3273339 | 4 | 121.4752255364 | 31.1525091152 | 60 | 7 | 2 | 43.2 | TDD | 648 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3276832 | 3 | 121.4730207513 | 31.1542478148 | 231 | 2 | 5 | 15.9 | TDD | 20 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.946 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.964 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.101 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.101 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.792 | NREventA3 | measId:2;ServCellPCI:935;Se... |
| 2024-09-20 22:21:38.032 | NRHandoverAttempt | SourcePCI:935;SourceNR-ARFC... |
| 2024-09-20 22:21:38.074 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.088 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.206 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.206 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3253443 | 1 | 78.2976 | 86.5484 | -114.4200 | 8.7940 | 149.6173 | 0.0035 | 0.0064 |
| 2024_09_19 22:00 | 3220569 | 2 | 93.1078 | 79.0258 | -115.3645 | 15.2042 | 156.4948 | 0.0197 | 0.0073 |
| 2024_09_19 22:00 | 3276832 | 3 | 76.7778 | 90.5315 | -116.6530 | 12.7246 | 155.9126 | 0.0001 | 0.0061 |
| 2024_09_19 22:00 | 3273339 | 4 | 80.5043 | 85.7393 | -114.2787 | 7.3742 | 157.0072 | 0.0144 | 0.0124 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412584_1B849686 | 504990 | 482 | -92.0 | 504990 | 160 | -99.4 | 504990 | 648 | -99.5 | 504990 | 20 |
| MR_1774412584_E073CF12 | 504990 | 482 | -92.5 | 504990 | 160 | -98.1 | 504990 | 648 | -99.4 | 504990 | 20 |
| MR_1774412584_0204E6A6 | 504990 | 482 | -90.5 | 504990 | 160 | -95.9 | 504990 | 648 | -102.2 | 504990 | 20 |
| MR_1774412584_7435E0B4 | 504990 | 482 | -91.3 | 504990 | 160 | -98.7 | 504990 | 648 | -100.9 | 504990 | 20 |
| MR_1774412584_A12F5C93 | 504990 | 482 | -90.1 | 504990 | 160 | -99.0 | 504990 | 648 | -102.3 | 504990 | 20 |
| MR_1774412584_7E865FEA | 504990 | 482 | -92.2 | 504990 | 160 | -98.7 | 504990 | 648 | -102.0 | 504990 | 20 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 108: `2b3c1dbb-1a2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2b3c1dbb-1a24-4d88-8ad5-97d23e49aa0b` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[108] topology](images/test_0108.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Press down the tilt angle of 3270307_2 by 10 degrees
- `C3`: Decrease transmission power for 3255971_1
- `C4`: Lift the tilt angle  of 3255971_1 by 10 degrees
- `C5`: Decrease A3 Offset threshold for 3255971_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255971_1
- `C7`: Increase A3 Offset threshold for 3255971_1
- `C8`: Lift the tilt angle of 3270307_2 by 10 degrees
- `C9`: Press down the tilt angle  of 3255971_1 by 10 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270307_2
- `C11`: Decrease transmission power for 3270307_2
- `C12`: Increase A3 Offset threshold for 3270307_2
- `C13`: Adjust the azimuth of 3255971_1 by 50 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255971_1
- `C15`: Decrease A3 Offset threshold for 3270307_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase transmission power for 3255971_1
- `C18`: Add neighbor relationship between 3240914_4 and 3255971_1
- `C19`: Increase transmission power for 3270307_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270307_2
- `C21`: Add neighbor relationship between 3270307_2 and 3255971_1
- `C22`: Adjust the azimuth of 3270307_2 by 20 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.148 | MS1 | 121.4656622681 | 31.1446289569 | 338 | 504990 | -76.01 | 12.25 | 552.27 | 0.08 | 2.57 | 1587 |
| 2024-09-20 22:21:32.981 | MS1 | 121.4656716548 | 31.1446339271 | 338 | 504990 | -77.11 | 17.53 | 588.55 | 0.04 | 2.14 | 1580 |
| 2024-09-20 22:21:33.508 | MS1 | 121.4656615012 | 31.1446182921 | 338 | 504990 | -78.70 | 12.22 | 552.77 | 0.13 | 2.34 | 1599 |
| 2024-09-20 22:21:34.113 | MS1 | 121.4656588649 | 31.1446254887 | 338 | 504990 | -86.56 | -3.69 | 67.57 | 0.10 | 1.07 | 1593 |
| 2024-09-20 22:21:35.932 | MS1 | 121.4656653931 | 31.1446329667 | 338 | 504990 | -87.58 | -0.86 | 61.22 | 0.18 | 1.39 | 1589 |
| 2024-09-20 22:21:36.314 | MS1 | 121.4656702879 | 31.1446286338 | 338 | 504990 | -83.16 | -0.99 | 50.44 | 0.17 | 1.33 | 1588 |
| 2024-09-20 22:21:37.906 | MS1 | 121.4656644715 | 31.1446312276 | 338 | 504990 | -91.17 | -2.27 | 81.28 | 0.20 | 1.29 | 1596 |
| 2024-09-20 22:21:38.667 | MS1 | 121.4656659117 | 31.1446340931 | 338 | 504990 | -89.54 | -2.90 | 40.48 | 0.03 | 1.27 | 1593 |
| 2024-09-20 22:21:39.518 | MS1 | 121.4656680647 | 31.1446216905 | 752 | 504990 | -83.70 | 15.36 | 191.90 | 0.13 | 1.30 | 1563 |
| 2024-09-20 22:21:40.304 | MS1 | 121.4656740308 | 31.1446323480 | 752 | 504990 | -80.07 | 15.86 | 419.88 | 0.06 | 2.57 | 1581 |
| 2024-09-20 22:21:41.486 | MS1 | 121.4656602565 | 31.1446265086 | 752 | 504990 | -78.39 | 15.32 | 409.22 | 0.16 | 2.98 | 1592 |
| 2024-09-20 22:21:42.115 | MS1 | 121.4656667070 | 31.1446251256 | 752 | 504990 | -82.69 | 16.39 | 396.90 | 0.18 | 2.90 | 1578 |

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
| 3240914 | 4 | 121.4706909657 | 31.1489073571 | 278 | 11 | 0 | 25.8 | TDD | 554 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3255971 | 1 | 121.4676133629 | 31.1516278531 | 311 | 10 | 8 | 46.2 | TDD | 752 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3270307 | 2 | 121.4673016424 | 31.1543314588 | 208 | 9 | 12 | 26.8 | TDD | 338 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3278883 | 3 | 121.4740510699 | 31.1523522589 | 135 | 8 | 6 | 36.9 | TDD | 708 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.198 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.217 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.324 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.324 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.094 | NREventA3 | measId:2;ServCellPCI:516;Se... |
| 2024-09-20 22:21:38.334 | NRHandoverAttempt | SourcePCI:516;SourceNR-ARFC... |
| 2024-09-20 22:21:38.381 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.392 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.495 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.495 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255971 | 1 | 14.4227 | 14.6521 | -115.6631 | 13.0839 | 118.9483 | 0.0187 | 0.0032 |
| 2024_09_20 22:00 | 3270307 | 2 | 8.9935 | 8.1603 | -116.2720 | 12.7712 | 198.9805 | 0.0098 | 0.1687 |
| 2024_09_20 22:00 | 3278883 | 3 | 11.7671 | 7.1986 | -114.0228 | 7.2856 | 91.9169 | 0.0169 | 0.0016 |
| 2024_09_20 22:00 | 3240914 | 4 | 8.8522 | 14.2611 | -114.0192 | 18.9832 | 193.4293 | 0.0111 | 0.0120 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414669_D202A34B | 504990 | 338 | -86.1 | 504990 | 752 | -83.7 | 504990 | 554 | -84.0 | 504990 | 708 |
| MR_1774414669_91CC26FD | 504990 | 752 | -82.4 | 504990 | 338 | -87.5 | 504990 | 554 | -81.1 | 504990 | 708 |
| MR_1774414669_92716D2A | 504990 | 338 | -87.2 | 504990 | 752 | -83.2 | 504990 | 554 | -83.8 | 504990 | 708 |
| MR_1774414669_2453E20C | 504990 | 752 | -81.1 | 504990 | 338 | -87.2 | 504990 | 554 | -82.4 | 504990 | 708 |
| MR_1774414669_AB22D6E9 | 504990 | 752 | -81.1 | 504990 | 338 | -88.4 | 504990 | 554 | -83.6 | 504990 | 708 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 109: `2a03e00b-275...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2a03e00b-2752-495b-b254-33e58f913d7a` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[109] topology](images/test_0109.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255230_5
- `C2`: Decrease A3 Offset threshold for 3224149_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255230_5
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease transmission power for 3255230_5
- `C6`: Add neighbor relationship between 3277147_13 and 3255230_5
- `C7`: Check test server and transmission issues
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224149_2
- `C9`: Add neighbor relationship between 3224149_2 and 3255230_5
- `C10`: Increase A3 Offset threshold for 3255230_5
- `C11`: Increase transmission power for 3255230_5
- `C12`: Decrease A3 Offset threshold for 3255230_5
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224149_2
- `C14`: Press down the tilt angle  of 3255230_5 by 5 degrees
- `C15`: Adjust the azimuth of 3224149_2 by 2 degrees
- `C16`: Press down the tilt angle of 3224149_2 by 4 degrees
- `C17`: Decrease transmission power for 3224149_2
- `C18`: Adjust the azimuth of 3255230_5 by 43 degrees
- `C19`: Lift the tilt angle of 3224149_2 by 4 degrees
- `C20`: Increase transmission power for 3224149_2
- `C21`: Increase A3 Offset threshold for 3224149_2
- `C22`: Lift the tilt angle  of 3255230_5 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.855 | MS1 | 121.4656593762 | 31.1446194071 | 236 | 504990 | -95.09 | 11.40 | 401.54 | 0.00 | 2.40 | 1597 |
| 2024-09-20 22:21:32.125 | MS1 | 121.4656700324 | 31.1446344604 | 336 | 504990 | -95.00 | 13.42 | 553.74 | 0.19 | 2.90 | 1590 |
| 2024-09-20 22:21:33.252 | MS1 | 121.4656625252 | 31.1446282899 | 593 | 504990 | -94.86 | 9.39 | 401.26 | 0.17 | 2.24 | 1586 |
| 2024-09-20 22:21:34.303 | MS1 | 121.4656712755 | 31.1446348577 | 399 | 152650 | -94.73 | 4.47 | 72.59 | 0.20 | 1.76 | 956 |
| 2024-09-20 22:21:35.145 | MS1 | 121.4656640014 | 31.1446266668 | 227 | 152650 | -94.45 | 6.55 | 88.96 | 0.13 | 1.75 | 912 |
| 2024-09-20 22:21:36.946 | MS1 | 121.4656623842 | 31.1446299509 | 959 | 152650 | -92.89 | 5.41 | 85.58 | 0.06 | 1.63 | 948 |
| 2024-09-20 22:21:37.425 | MS1 | 121.4656691418 | 31.1446277897 | 351 | 152650 | -91.41 | 3.27 | 88.86 | 0.16 | 1.86 | 972 |
| 2024-09-20 22:21:38.573 | MS1 | 121.4656746170 | 31.1446225705 | 399 | 152650 | -87.00 | 5.09 | 74.47 | 0.11 | 1.59 | 914 |
| 2024-09-20 22:21:39.795 | MS1 | 121.4656616474 | 31.1446237668 | 227 | 152650 | -96.41 | 3.81 | 72.57 | 0.17 | 1.67 | 982 |
| 2024-09-20 22:21:40.211 | MS1 | 121.4656636725 | 31.1446373424 | 959 | 152650 | -89.13 | 7.66 | 77.05 | 0.12 | 2.30 | 1596 |
| 2024-09-20 22:21:41.528 | MS1 | 121.4656702315 | 31.1446208943 | 351 | 152650 | -93.08 | 7.58 | 79.09 | 0.15 | 2.14 | 1574 |
| 2024-09-20 22:21:42.906 | MS1 | 121.4656715270 | 31.1446313618 | 399 | 152650 | -88.68 | 2.87 | 55.55 | 0.17 | 2.86 | 1588 |

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
| 3215589 | 4 | 121.4646863410 | 31.1488646185 | 139 | 15 | 8 | 14.1 | TDD | 593 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3223982 | 12 | 121.4754023737 | 31.1527270144 | 158 | 12 | 8 | 23.1 | FDD | 569 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3224149 | 2 | 121.4718531084 | 31.1442589250 | 276 | 4 | 9 | 0.3 | TDD | 236 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3228651 | 3 | 121.4692549789 | 31.1481132199 | 329 | 0 | 3 | 7.7 | TDD | 336 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3232257 | 1 | 121.4746441404 | 31.1540864054 | 67 | 2 | 5 | 9.7 | TDD | 320 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3242259 | 7 | 121.4745414195 | 31.1531873827 | 159 | 8 | 1 | 24.8 | FDD | 227 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3242902 | 10 | 121.4700965143 | 31.1487958787 | 207 | 6 | 9 | 23.9 | FDD | 235 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3255230 | 5 | 121.4716308313 | 31.1533138126 | 253 | 4 | 8 | 14.6 | TDD | 596 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3258976 | 11 | 121.4688502018 | 31.1444828636 | 255 | 3 | 10 | 16.7 | FDD | 399 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3259298 | 8 | 121.4732410987 | 31.1444818632 | 134 | 12 | 4 | 8.8 | FDD | 228 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3273920 | 6 | 121.4751583658 | 31.1484004481 | 72 | 12 | 11 | 7.5 | TDD | 665 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3277147 | 13 | 121.4680927690 | 31.1506759779 | 277 | 8 | 8 | 5.5 | FDD | 959 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3278644 | 9 | 121.4720197462 | 31.1450909914 | 342 | 2 | 12 | 25.5 | FDD | 351 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |

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
| 2024-09-20 22:21:30.999 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.014 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.138 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.138 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.801 | NREventA2 | measId:1;ServCellPCI:420;Se... |
| 2024-09-20 22:21:34.943 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.220 | NREventA5 | measId:3;ServCellPCI:420;Se... |
| 2024-09-20 22:21:35.296 | NRHandoverAttempt | SourcePCI:420;SourceNR-ARFC... |
| 2024-09-20 22:21:35.335 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.346 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.467 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.467 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232257 | 1 | 5.4260 | 19.2820 | -115.5817 | 8.0667 | 116.8961 | 0.0138 | 0.0169 |
| 2024_09_20 22:00 | 3224149 | 2 | 13.0889 | 7.2005 | -114.4696 | 19.8871 | 83.2012 | 0.0073 | 0.0139 |
| 2024_09_20 22:00 | 3228651 | 3 | 18.6554 | 8.6057 | -115.5783 | 13.4923 | 188.2579 | 0.0062 | 0.0152 |
| 2024_09_20 22:00 | 3215589 | 4 | 13.8547 | 8.9909 | -116.9023 | 13.4898 | 149.3203 | 0.0004 | 0.0163 |
| 2024_09_20 22:00 | 3255230 | 5 | 6.4502 | 10.4060 | -116.3851 | 12.6395 | 111.9128 | 0.0020 | 0.0003 |
| 2024_09_20 22:00 | 3273920 | 6 | 13.8499 | 16.7794 | -114.6508 | 19.8496 | 136.8066 | 0.0193 | 0.0189 |
| 2024_09_20 22:00 | 3242259 | 7 | 7.2020 | 18.3547 | -114.5559 | 3.7599 | 22.0719 | 0.0199 | 0.0180 |
| 2024_09_20 22:00 | 3259298 | 8 | 7.5668 | 15.6113 | -117.1110 | 4.6061 | 53.2603 | 0.0134 | 0.0042 |
| 2024_09_20 22:00 | 3278644 | 9 | 6.5526 | 14.0814 | -116.4017 | 4.3546 | 28.7125 | 0.0114 | 0.0142 |
| 2024_09_20 22:00 | 3242902 | 10 | 18.8232 | 9.7233 | -116.6048 | 3.2369 | 27.1784 | 0.0065 | 0.0164 |
| 2024_09_20 22:00 | 3258976 | 11 | 14.1949 | 17.4276 | -116.4777 | 4.2552 | 54.1000 | 0.0124 | 0.0173 |
| 2024_09_20 22:00 | 3223982 | 12 | 10.7959 | 11.1105 | -115.7270 | 3.7932 | 39.5440 | 0.0004 | 0.0140 |
| 2024_09_20 22:00 | 3277147 | 13 | 7.7955 | 5.8269 | -115.1724 | 4.9847 | 40.7870 | 0.0185 | 0.0185 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416974_E8DC656E | 504990 | 593 | -95.0 | 504990 | 596 | -88.3 | 504990 | 665 | -97.9 | 504990 | 320 |
| MR_1774416974_AC46A105 | 152650 | 399 | -93.1 | 152650 | 235 | -100.7 | 152650 | 569 | -105.8 | 152650 | 228 |
| MR_1774416974_712AF462 | 152650 | 399 | -94.5 | 152650 | 235 | -103.2 | 152650 | 569 | -106.4 | 152650 | 228 |
| MR_1774416974_6C2D7C2C | 504990 | 593 | -96.4 | 504990 | 596 | -91.1 | 504990 | 665 | -98.8 | 504990 | 320 |
| MR_1774416974_72AE42A3 | 152650 | 399 | -95.4 | 152650 | 235 | -100.4 | 152650 | 569 | -106.8 | 152650 | 228 |
| MR_1774416974_7BCC756A | 504990 | 593 | -95.0 | 504990 | 596 | -89.2 | 504990 | 665 | -96.2 | 504990 | 320 |
| MR_1774416974_A4D6C7BB | 152650 | 399 | -92.7 | 152650 | 235 | -101.8 | 152650 | 569 | -104.7 | 152650 | 228 |

> *... 2개 열 생략 (전체 14열)*

---
