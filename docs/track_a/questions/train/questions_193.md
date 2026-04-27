# Track A 문제 분석 — train[1920]~train[1929]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1920] ~ train[1929] (10개)

## 목차

1. [문제 1920: `e651c677-03f...`](#1920) — single-answer, 정답: C6
2. [문제 1921: `d72babc0-6ca...`](#1921) — single-answer, 정답: C8
3. [문제 1922: `0794c208-bb5...`](#1922) — multiple-answer, 정답: C15|C20
4. [문제 1923: `e94e5196-eb7...`](#1923) — single-answer, 정답: C18
5. [문제 1924: `3a49306d-8df...`](#1924) — single-answer, 정답: C9
6. [문제 1925: `7f6b39ff-589...`](#1925) — multiple-answer, 정답: C15|C20
7. [문제 1926: `c741dabb-7ba...`](#1926) — single-answer, 정답: C7
8. [문제 1927: `b57a5908-6f7...`](#1927) — multiple-answer, 정답: C12|C18
9. [문제 1928: `c59fb0e7-8ff...`](#1928) — single-answer, 정답: C16
10. [문제 1929: `c2941e9a-80a...`](#1929) — single-answer, 정답: C3

---

### 문제 1920: `e651c677-03f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e651c677-03f6-4dc8-969a-b56e7f9df68c` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1920] topology](images/train_1920.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3219669_3 by 6 degrees
- `C2`: Decrease A3 Offset threshold for 3219669_3
- `C3`: Press down the tilt angle  of 3219669_3 by 6 degrees
- `C4`: Increase A3 Offset threshold for 3219669_3
- `C5`: Check test server and transmission issues
- `C6`: Insufficient data; more data is needed for judgment. **← 정답**
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237651_4
- `C8`: Decrease transmission power for 3237651_4
- `C9`: Adjust the azimuth of 3219669_3 by 50 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219669_3
- `C11`: Add neighbor relationship between 3271976_2 and 3219669_3
- `C12`: Increase transmission power for 3237651_4
- `C13`: Add neighbor relationship between 3237651_4 and 3219669_3
- `C14`: Increase transmission power for 3219669_3
- `C15`: Decrease transmission power for 3219669_3
- `C16`: Decrease A3 Offset threshold for 3237651_4
- `C17`: Press down the tilt angle of 3237651_4 by 10 degrees
- `C18`: Increase A3 Offset threshold for 3237651_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237651_4
- `C20`: Adjust the azimuth of 3237651_4 by 50 degrees
- `C21`: Lift the tilt angle of 3237651_4 by 10 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219669_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.685 | MS1 | 121.4656755358 | 31.1446296059 | 151 | 504990 | -91.17 | 14.05 | 342.72 | 0.15 | 2.36 | 1566 |
| 2024-09-20 22:21:32.258 | MS1 | 121.4656610078 | 31.1446278721 | 151 | 504990 | -89.63 | 17.22 | 420.83 | 0.05 | 2.40 | 1582 |
| 2024-09-20 22:21:33.740 | MS1 | 121.4656661207 | 31.1446279077 | 151 | 504990 | -89.91 | 15.59 | 439.60 | 0.20 | 2.82 | 1568 |
| 2024-09-20 22:21:34.330 | MS1 | 121.4656670719 | 31.1446312121 | 151 | 504990 | -87.18 | 16.66 | 66.61 | 0.06 | 2.53 | 1592 |
| 2024-09-20 22:21:35.921 | MS1 | 121.4656704754 | 31.1446278807 | 151 | 504990 | -90.51 | 14.65 | 90.78 | 0.08 | 2.58 | 1571 |
| 2024-09-20 22:21:36.808 | MS1 | 121.4656761306 | 31.1446316626 | 151 | 504990 | -88.07 | 17.86 | 74.39 | 0.12 | 2.92 | 1566 |
| 2024-09-20 22:21:37.998 | MS1 | 121.4656648613 | 31.1446366654 | 151 | 504990 | -90.45 | 11.03 | 97.10 | 0.15 | 2.51 | 1592 |
| 2024-09-20 22:21:38.420 | MS1 | 121.4656754865 | 31.1446375587 | 151 | 504990 | -90.44 | 7.74 | 79.49 | 0.18 | 2.82 | 1598 |
| 2024-09-20 22:21:39.712 | MS1 | 121.4656738655 | 31.1446373903 | 151 | 504990 | -90.67 | 10.29 | 67.10 | 0.09 | 2.42 | 1573 |
| 2024-09-20 22:21:40.541 | MS1 | 121.4656619698 | 31.1446247811 | 151 | 504990 | -90.48 | 8.47 | 570.53 | 0.02 | 2.93 | 1565 |
| 2024-09-20 22:21:41.240 | MS1 | 121.4656640455 | 31.1446196924 | 151 | 504990 | -89.60 | 11.52 | 370.13 | 0.15 | 2.86 | 1585 |
| 2024-09-20 22:21:42.564 | MS1 | 121.4656764162 | 31.1446187328 | 151 | 504990 | -93.60 | 7.97 | 597.54 | 0.20 | 2.08 | 1586 |

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
| 3219669 | 3 | 121.4707591486 | 31.1450785794 | 117 | 1 | 3 | 41.8 | TDD | 46 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3237651 | 4 | 121.4647086844 | 31.1507463517 | 357 | 6 | 0 | 43.1 | TDD | 151 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3258672 | 1 | 121.4706503073 | 31.1495703782 | 11 | 6 | 6 | 43.6 | TDD | 929 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3271976 | 2 | 121.4672097124 | 31.1454089631 | 238 | 4 | 10 | 27.0 | TDD | 74 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.572 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.594 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.705 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.705 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.428 | NREventA3 | measId:2;ServCellPCI:503;Se... |
| 2024-09-20 22:21:38.668 | NRHandoverAttempt | SourcePCI:503;SourceNR-ARFC... |
| 2024-09-20 22:21:38.698 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.711 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.833 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.833 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3258672 | 1 | 83.9784 | 79.1918 | -115.4815 | 18.4627 | 137.3182 | 0.0057 | 0.0055 |
| 2024_09_19 22:00 | 3271976 | 2 | 79.7924 | 86.2718 | -117.7442 | 11.4951 | 175.6980 | 0.0165 | 0.0191 |
| 2024_09_19 22:00 | 3219669 | 3 | 88.4154 | 89.7469 | -114.4893 | 17.6426 | 102.1003 | 0.0157 | 0.0189 |
| 2024_09_19 22:00 | 3237651 | 4 | 78.0047 | 84.9732 | -116.0618 | 14.7401 | 102.5865 | 0.0050 | 0.0092 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414563_0BEDEF6B | 504990 | 151 | -86.1 | 504990 | 46 | -87.8 | 504990 | 74 | -99.7 | 504990 | 929 |
| MR_1774414563_6444FCB6 | 504990 | 151 | -85.9 | 504990 | 46 | -88.0 | 504990 | 74 | -97.0 | 504990 | 929 |
| MR_1774414563_D1597EBE | 504990 | 151 | -88.0 | 504990 | 46 | -88.9 | 504990 | 74 | -98.7 | 504990 | 929 |
| MR_1774414563_E44FFA9E | 504990 | 151 | -86.7 | 504990 | 46 | -89.5 | 504990 | 74 | -99.2 | 504990 | 929 |
| MR_1774414563_536231ED | 504990 | 151 | -86.8 | 504990 | 46 | -90.9 | 504990 | 74 | -97.7 | 504990 | 929 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1921: `d72babc0-6ca...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d72babc0-6ca2-4680-9eda-7a43c8aa3540` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1921] topology](images/train_1921.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220714_4
- `C2`: Press down the tilt angle  of 3220714_4 by 5 degrees
- `C3`: Adjust the azimuth of 3220714_4 by 50 degrees
- `C4`: Decrease transmission power for 3261099_2
- `C5`: Lift the tilt angle  of 3220714_4 by 5 degrees
- `C6`: Decrease A3 Offset threshold for 3261099_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261099_2
- `C8`: Insufficient data; more data is needed for judgment. **← 정답**
- `C9`: Increase A3 Offset threshold for 3220714_4
- `C10`: Decrease A3 Offset threshold for 3220714_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261099_2
- `C12`: Lift the tilt angle of 3261099_2 by 10 degrees
- `C13`: Increase transmission power for 3261099_2
- `C14`: Check test server and transmission issues
- `C15`: Press down the tilt angle of 3261099_2 by 10 degrees
- `C16`: Decrease transmission power for 3220714_4
- `C17`: Add neighbor relationship between 3261099_2 and 3220714_4
- `C18`: Increase A3 Offset threshold for 3261099_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220714_4
- `C20`: Increase transmission power for 3220714_4
- `C21`: Add neighbor relationship between 3231178_1 and 3220714_4
- `C22`: Adjust the azimuth of 3261099_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.980 | MS1 | 121.4656733298 | 31.1446305122 | 492 | 504990 | -85.60 | 16.54 | 532.26 | 0.10 | 2.21 | 1570 |
| 2024-09-20 22:21:32.795 | MS1 | 121.4656713078 | 31.1446344220 | 492 | 504990 | -87.43 | 14.68 | 465.98 | 0.16 | 2.47 | 1572 |
| 2024-09-20 22:21:33.265 | MS1 | 121.4656738492 | 31.1446373735 | 492 | 504990 | -86.58 | 12.42 | 534.38 | 0.17 | 2.53 | 1595 |
| 2024-09-20 22:21:34.610 | MS1 | 121.4656779555 | 31.1446236121 | 492 | 504990 | -91.16 | 12.75 | 80.23 | 0.03 | 2.53 | 1576 |
| 2024-09-20 22:21:35.489 | MS1 | 121.4656588750 | 31.1446240090 | 492 | 504990 | -85.76 | 14.12 | 45.61 | 0.15 | 2.82 | 1578 |
| 2024-09-20 22:21:36.284 | MS1 | 121.4656757329 | 31.1446246134 | 492 | 504990 | -91.94 | 17.29 | 50.40 | 0.15 | 2.66 | 1568 |
| 2024-09-20 22:21:37.842 | MS1 | 121.4656641138 | 31.1446342858 | 492 | 504990 | -91.09 | 10.29 | 87.34 | 0.09 | 2.97 | 1560 |
| 2024-09-20 22:21:38.114 | MS1 | 121.4656727692 | 31.1446187431 | 492 | 504990 | -93.17 | 11.97 | 44.51 | 0.14 | 2.69 | 1596 |
| 2024-09-20 22:21:39.767 | MS1 | 121.4656750308 | 31.1446185895 | 492 | 504990 | -92.56 | 10.61 | 67.95 | 0.14 | 2.60 | 1589 |
| 2024-09-20 22:21:40.447 | MS1 | 121.4656613258 | 31.1446232678 | 492 | 504990 | -90.43 | 9.53 | 324.38 | 0.04 | 2.08 | 1588 |
| 2024-09-20 22:21:41.765 | MS1 | 121.4656739009 | 31.1446311763 | 492 | 504990 | -92.04 | 9.45 | 388.12 | 0.13 | 2.80 | 1581 |
| 2024-09-20 22:21:42.663 | MS1 | 121.4656605841 | 31.1446351492 | 492 | 504990 | -92.39 | 7.07 | 412.98 | 0.15 | 2.48 | 1594 |

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
| 3220714 | 4 | 121.4656276408 | 31.1496796749 | 341 | 0 | 11 | 47.0 | TDD | 911 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3231178 | 1 | 121.4674067477 | 31.1519457588 | 287 | 7 | 8 | 22.9 | TDD | 442 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3244246 | 3 | 121.4758431105 | 31.1490307831 | 119 | 10 | 9 | 49.4 | TDD | 4 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3261099 | 2 | 121.4725583911 | 31.1557810160 | 53 | 14 | 4 | 45.3 | TDD | 492 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.323 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.340 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.458 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.458 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.198 | NREventA3 | measId:2;ServCellPCI:787;Se... |
| 2024-09-20 22:21:38.438 | NRHandoverAttempt | SourcePCI:787;SourceNR-ARFC... |
| 2024-09-20 22:21:38.473 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.485 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.633 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.633 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3231178 | 1 | 81.0036 | 90.7685 | -117.9667 | 13.3496 | 87.4115 | 0.0095 | 0.0061 |
| 2024_09_19 22:00 | 3261099 | 2 | 77.5647 | 80.7745 | -115.2117 | 19.7804 | 187.8600 | 0.0023 | 0.0062 |
| 2024_09_19 22:00 | 3244246 | 3 | 78.1794 | 87.8144 | -116.0188 | 5.9382 | 81.8899 | 0.0048 | 0.0044 |
| 2024_09_19 22:00 | 3220714 | 4 | 90.8387 | 78.7985 | -114.7369 | 13.8950 | 157.0811 | 0.0030 | 0.0159 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415768_58092736 | 504990 | 492 | -93.0 | 504990 | 911 | -97.4 | 504990 | 442 | -99.8 | 504990 | 4 |
| MR_1774415768_AC424082 | 504990 | 492 | -91.9 | 504990 | 911 | -94.7 | 504990 | 442 | -98.4 | 504990 | 4 |
| MR_1774415768_AFD9F3B8 | 504990 | 492 | -89.6 | 504990 | 911 | -94.1 | 504990 | 442 | -96.6 | 504990 | 4 |
| MR_1774415768_5DA1F588 | 504990 | 492 | -89.9 | 504990 | 911 | -96.8 | 504990 | 442 | -98.0 | 504990 | 4 |
| MR_1774415768_FF5B9202 | 504990 | 492 | -90.8 | 504990 | 911 | -96.5 | 504990 | 442 | -98.9 | 504990 | 4 |
| MR_1774415768_1F382DD5 | 504990 | 492 | -89.3 | 504990 | 911 | -94.2 | 504990 | 442 | -97.9 | 504990 | 4 |
| MR_1774415768_F14DD373 | 504990 | 492 | -89.7 | 504990 | 911 | -97.0 | 504990 | 442 | -97.0 | 504990 | 4 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1922: `0794c208-bb5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0794c208-bb55-4dd6-bc55-d1c7c8a81bbc` |
| Tag | **multiple-answer** |
| 정답 | **C15|C20** |
| C15 의미 | Increase transmission power for 3248211_2 |
| C20 의미 | Adjust the azimuth of 3248211_2 by 37 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1922] topology](images/train_1922.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270346_1
- `C2`: Lift the tilt angle  of 3270346_1 by 5 degrees
- `C3`: Increase transmission power for 3270346_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270346_1
- `C5`: Decrease A3 Offset threshold for 3248211_2
- `C6`: Add neighbor relationship between 3257167_3 and 3270346_1
- `C7`: Increase A3 Offset threshold for 3248211_2
- `C8`: Lift the tilt angle of 3248211_2 by 10 degrees
- `C9`: Add neighbor relationship between 3248211_2 and 3270346_1
- `C10`: Decrease transmission power for 3248211_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248211_2
- `C12`: Decrease transmission power for 3270346_1
- `C13`: Check test server and transmission issues
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase transmission power for 3248211_2 **← 정답**
- `C16`: Increase A3 Offset threshold for 3270346_1
- `C17`: Press down the tilt angle of 3248211_2 by 10 degrees
- `C18`: Press down the tilt angle  of 3270346_1 by 5 degrees
- `C19`: Decrease A3 Offset threshold for 3270346_1
- `C20`: Adjust the azimuth of 3248211_2 by 37 degrees **← 정답**
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248211_2
- `C22`: Adjust the azimuth of 3270346_1 by 40 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.733 | MS1 | 121.4656620065 | 31.1446317517 | 802 | 504990 | -92.03 | 16.70 | 490.26 | 0.13 | 2.92 | 1594 |
| 2024-09-20 22:21:32.960 | MS1 | 121.4656726854 | 31.1446231689 | 802 | 504990 | -86.26 | 17.18 | 490.68 | 0.18 | 2.43 | 1593 |
| 2024-09-20 22:21:33.548 | MS1 | 121.4656688865 | 31.1446238582 | 802 | 504990 | -85.96 | 13.85 | 469.80 | 0.14 | 2.47 | 1572 |
| 2024-09-20 22:21:34.526 | MS1 | 121.4656681523 | 31.1446189187 | 802 | 504990 | -105.77 | 1.82 | 47.43 | 0.01 | 1.39 | 1583 |
| 2024-09-20 22:21:35.582 | MS1 | 121.4656636142 | 31.1446249273 | 802 | 504990 | -105.83 | -0.91 | 41.48 | 0.15 | 1.15 | 1569 |
| 2024-09-20 22:21:36.212 | MS1 | 121.4656676429 | 31.1446186464 | 802 | 504990 | -102.68 | 0.20 | 44.83 | 0.13 | 1.14 | 1571 |
| 2024-09-20 22:21:37.699 | MS1 | 121.4656729683 | 31.1446289351 | 802 | 504990 | -103.29 | 0.09 | 26.45 | 0.17 | 1.25 | 1599 |
| 2024-09-20 22:21:38.393 | MS1 | 121.4656665515 | 31.1446316429 | 802 | 504990 | -102.74 | -1.22 | 51.15 | 0.17 | 1.27 | 1561 |
| 2024-09-20 22:21:39.458 | MS1 | 121.4656628671 | 31.1446349794 | 802 | 504990 | -105.66 | 1.26 | 67.79 | 0.11 | 1.25 | 1565 |
| 2024-09-20 22:21:40.446 | MS1 | 121.4656732214 | 31.1446202137 | 802 | 504990 | -87.58 | 16.70 | 425.23 | 0.19 | 2.30 | 1566 |
| 2024-09-20 22:21:41.558 | MS1 | 121.4656617181 | 31.1446276029 | 802 | 504990 | -87.71 | 12.20 | 354.46 | 0.20 | 2.51 | 1595 |
| 2024-09-20 22:21:42.718 | MS1 | 121.4656636391 | 31.1446282704 | 802 | 504990 | -91.38 | 12.25 | 455.44 | 0.16 | 2.85 | 1569 |

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
| 3223214 | 4 | 121.4710442340 | 31.1482224599 | 265 | 14 | 5 | 23.1 | TDD | 578 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3248211 | 2 | 121.4678341472 | 31.1448224406 | 301 | 5 | 0 | 35.1 | TDD | 802 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3257167 | 3 | 121.4685587408 | 31.1485802559 | 57 | 15 | 0 | 35.4 | TDD | 116 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3270346 | 1 | 121.4643816257 | 31.1528013448 | 212 | 3 | 10 | 27.4 | TDD | 137 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.368 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.391 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.521 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.521 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.675 | NREventA2 | measId:1;ServCellPCI:721;Se... |
| 2024-09-20 22:21:34.798 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270346 | 1 | 16.0574 | 14.8990 | -114.0008 | 10.2144 | 127.0674 | 0.0055 | 0.0050 |
| 2024_09_20 22:00 | 3248211 | 2 | 11.7706 | 7.9492 | -117.9918 | 10.0828 | 85.2482 | 0.1555 | 0.0135 |
| 2024_09_20 22:00 | 3257167 | 3 | 6.2032 | 17.5230 | -116.8318 | 9.2832 | 148.0901 | 0.0057 | 0.0029 |
| 2024_09_20 22:00 | 3223214 | 4 | 15.4584 | 6.3883 | -116.4243 | 19.0049 | 141.8928 | 0.0086 | 0.0102 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415683_E4963E9B | 504990 | 802 | -107.2 | 504990 | 137 | -109.8 | 504990 | 116 | -115.1 | 504990 | 578 |
| MR_1774415683_7AE2734D | 504990 | 802 | -107.4 | 504990 | 137 | -109.4 | 504990 | 116 | -115.9 | 504990 | 578 |
| MR_1774415683_FF984465 | 504990 | 802 | -106.7 | 504990 | 137 | -109.4 | 504990 | 116 | -114.2 | 504990 | 578 |
| MR_1774415683_70B667DD | 504990 | 802 | -106.4 | 504990 | 137 | -108.9 | 504990 | 116 | -117.1 | 504990 | 578 |
| MR_1774415683_FD89D474 | 504990 | 802 | -103.8 | 504990 | 137 | -110.1 | 504990 | 116 | -117.0 | 504990 | 578 |
| MR_1774415683_E9A53B31 | 504990 | 802 | -107.4 | 504990 | 137 | -109.9 | 504990 | 116 | -113.2 | 504990 | 578 |
| MR_1774415683_F9095E18 | 504990 | 802 | -106.8 | 504990 | 137 | -109.0 | 504990 | 116 | -116.8 | 504990 | 578 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1923: `e94e5196-eb7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e94e5196-eb73-4ddf-b719-6bf6c1bb9f22` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1923] topology](images/train_1923.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3213522_1 by 10 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236984_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236984_3
- `C4`: Adjust the azimuth of 3236984_3 by 50 degrees
- `C5`: Check test server and transmission issues
- `C6`: Lift the tilt angle  of 3236984_3 by 7 degrees
- `C7`: Increase transmission power for 3236984_3
- `C8`: Add neighbor relationship between 3213522_1 and 3236984_3
- `C9`: Decrease transmission power for 3236984_3
- `C10`: Decrease A3 Offset threshold for 3213522_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213522_1
- `C12`: Increase transmission power for 3213522_1
- `C13`: Lift the tilt angle of 3213522_1 by 10 degrees
- `C14`: Adjust the azimuth of 3213522_1 by 50 degrees
- `C15`: Decrease transmission power for 3213522_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213522_1
- `C17`: Press down the tilt angle  of 3236984_3 by 7 degrees
- `C18`: Insufficient data; more data is needed for judgment. **← 정답**
- `C19`: Add neighbor relationship between 3270779_2 and 3236984_3
- `C20`: Decrease A3 Offset threshold for 3236984_3
- `C21`: Increase A3 Offset threshold for 3236984_3
- `C22`: Increase A3 Offset threshold for 3213522_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.277 | MS1 | 121.4656665649 | 31.1446306297 | 40 | 504990 | -85.62 | 14.30 | 512.29 | 0.05 | 2.22 | 1597 |
| 2024-09-20 22:21:32.414 | MS1 | 121.4656703255 | 31.1446366280 | 40 | 504990 | -89.05 | 17.76 | 479.84 | 0.06 | 2.35 | 1596 |
| 2024-09-20 22:21:33.795 | MS1 | 121.4656713401 | 31.1446281549 | 40 | 504990 | -87.94 | 17.43 | 314.45 | 0.01 | 2.87 | 1566 |
| 2024-09-20 22:21:34.368 | MS1 | 121.4656662864 | 31.1446237703 | 40 | 504990 | -88.68 | 15.07 | 70.89 | 0.14 | 2.54 | 1592 |
| 2024-09-20 22:21:35.624 | MS1 | 121.4656666943 | 31.1446200717 | 40 | 504990 | -90.59 | 17.92 | 98.53 | 0.16 | 2.21 | 1595 |
| 2024-09-20 22:21:36.195 | MS1 | 121.4656660327 | 31.1446366730 | 40 | 504990 | -91.25 | 16.67 | 88.05 | 0.15 | 3.00 | 1579 |
| 2024-09-20 22:21:37.507 | MS1 | 121.4656649505 | 31.1446200637 | 40 | 504990 | -90.71 | 9.18 | 55.68 | 0.20 | 2.00 | 1565 |
| 2024-09-20 22:21:38.841 | MS1 | 121.4656621163 | 31.1446267618 | 40 | 504990 | -93.80 | 8.23 | 81.38 | 0.20 | 2.22 | 1589 |
| 2024-09-20 22:21:39.181 | MS1 | 121.4656750591 | 31.1446253084 | 40 | 504990 | -89.07 | 7.23 | 96.38 | 0.11 | 2.60 | 1575 |
| 2024-09-20 22:21:40.722 | MS1 | 121.4656743457 | 31.1446266555 | 40 | 504990 | -92.71 | 10.64 | 575.47 | 0.00 | 2.10 | 1600 |
| 2024-09-20 22:21:41.315 | MS1 | 121.4656765500 | 31.1446266715 | 40 | 504990 | -93.98 | 12.90 | 535.07 | 0.16 | 2.37 | 1588 |
| 2024-09-20 22:21:42.933 | MS1 | 121.4656664608 | 31.1446322054 | 40 | 504990 | -90.18 | 10.49 | 433.23 | 0.16 | 2.88 | 1569 |

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
| 3213522 | 1 | 121.4747380763 | 31.1552971462 | 155 | 14 | 2 | 43.4 | TDD | 40 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3236984 | 3 | 121.4745755703 | 31.1521737085 | 36 | 6 | 1 | 23.1 | TDD | 707 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3261264 | 4 | 121.4717780885 | 31.1455273964 | 263 | 13 | 12 | 27.1 | TDD | 125 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3270779 | 2 | 121.4641248409 | 31.1541953210 | 62 | 10 | 0 | 48.6 | TDD | 232 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.244 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.259 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.402 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.402 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.135 | NREventA3 | measId:2;ServCellPCI:272;Se... |
| 2024-09-20 22:21:38.375 | NRHandoverAttempt | SourcePCI:272;SourceNR-ARFC... |
| 2024-09-20 22:21:38.419 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.433 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.539 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.539 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3213522 | 1 | 88.5386 | 80.3259 | -115.5335 | 17.1420 | 87.7330 | 0.0006 | 0.0088 |
| 2024_09_19 22:00 | 3270779 | 2 | 76.4258 | 79.8415 | -117.7184 | 10.3437 | 129.8775 | 0.0016 | 0.0051 |
| 2024_09_19 22:00 | 3236984 | 3 | 87.7330 | 90.2731 | -117.3046 | 15.8624 | 108.7605 | 0.0090 | 0.0177 |
| 2024_09_19 22:00 | 3261264 | 4 | 89.7298 | 88.6004 | -115.4237 | 18.2375 | 126.4819 | 0.0093 | 0.0020 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416014_C7AD6545 | 504990 | 40 | -90.2 | 504990 | 707 | -94.1 | 504990 | 232 | -97.5 | 504990 | 125 |
| MR_1774416014_294D9FCA | 504990 | 40 | -87.6 | 504990 | 707 | -93.6 | 504990 | 232 | -99.9 | 504990 | 125 |
| MR_1774416014_F04621CB | 504990 | 40 | -89.1 | 504990 | 707 | -92.6 | 504990 | 232 | -100.4 | 504990 | 125 |
| MR_1774416014_9A777370 | 504990 | 40 | -88.3 | 504990 | 707 | -92.1 | 504990 | 232 | -100.0 | 504990 | 125 |
| MR_1774416014_95AC02FB | 504990 | 40 | -89.4 | 504990 | 707 | -92.3 | 504990 | 232 | -98.2 | 504990 | 125 |
| MR_1774416014_59D3D7E1 | 504990 | 40 | -86.7 | 504990 | 707 | -93.4 | 504990 | 232 | -99.4 | 504990 | 125 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1924: `3a49306d-8df...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3a49306d-8df2-41ad-bbaf-36c7d6e375b1` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease A3 Offset threshold for 3268828_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1924] topology](images/train_1924.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213532_1
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Press down the tilt angle  of 3213532_1 by 3 degrees
- `C4`: Decrease transmission power for 3213532_1
- `C5`: Decrease transmission power for 3268828_2
- `C6`: Lift the tilt angle of 3268828_2 by 5 degrees
- `C7`: Press down the tilt angle of 3268828_2 by 5 degrees
- `C8`: Check test server and transmission issues
- `C9`: Decrease A3 Offset threshold for 3268828_2 **← 정답**
- `C10`: Decrease A3 Offset threshold for 3213532_1
- `C11`: Adjust the azimuth of 3268828_2 by 50 degrees
- `C12`: Adjust the azimuth of 3213532_1 by 6 degrees
- `C13`: Add neighbor relationship between 3268828_2 and 3213532_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268828_2
- `C15`: Add neighbor relationship between 3238942_3 and 3213532_1
- `C16`: Increase transmission power for 3213532_1
- `C17`: Lift the tilt angle  of 3213532_1 by 3 degrees
- `C18`: Increase A3 Offset threshold for 3213532_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268828_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213532_1
- `C21`: Increase transmission power for 3268828_2
- `C22`: Increase A3 Offset threshold for 3268828_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.194 | MS1 | 121.4656772729 | 31.1446205607 | 621 | 504990 | -79.39 | 13.88 | 434.66 | 0.04 | 2.92 | 1589 |
| 2024-09-20 22:21:32.878 | MS1 | 121.4656769671 | 31.1446205634 | 621 | 504990 | -84.27 | 17.51 | 360.39 | 0.03 | 3.00 | 1586 |
| 2024-09-20 22:21:33.527 | MS1 | 121.4656594827 | 31.1446325420 | 621 | 504990 | -80.37 | 17.48 | 528.96 | 0.04 | 2.23 | 1581 |
| 2024-09-20 22:21:34.257 | MS1 | 121.4656742321 | 31.1446372470 | 621 | 504990 | -84.56 | -3.19 | 60.06 | 0.14 | 1.10 | 1588 |
| 2024-09-20 22:21:35.296 | MS1 | 121.4656773006 | 31.1446345770 | 621 | 504990 | -92.00 | -1.75 | 26.15 | 0.14 | 1.01 | 1575 |
| 2024-09-20 22:21:36.924 | MS1 | 121.4656640824 | 31.1446335482 | 621 | 504990 | -88.01 | -3.46 | 21.00 | 0.09 | 1.39 | 1581 |
| 2024-09-20 22:21:37.777 | MS1 | 121.4656773567 | 31.1446287210 | 621 | 504990 | -85.53 | -2.27 | 28.02 | 0.10 | 1.21 | 1595 |
| 2024-09-20 22:21:38.147 | MS1 | 121.4656606178 | 31.1446216056 | 621 | 504990 | -84.52 | -3.00 | 37.64 | 0.09 | 1.21 | 1583 |
| 2024-09-20 22:21:39.785 | MS1 | 121.4656627862 | 31.1446337653 | 914 | 504990 | -76.72 | 12.00 | 190.38 | 0.19 | 1.36 | 1598 |
| 2024-09-20 22:21:40.295 | MS1 | 121.4656708686 | 31.1446348393 | 914 | 504990 | -79.56 | 16.91 | 371.79 | 0.11 | 2.90 | 1591 |
| 2024-09-20 22:21:41.237 | MS1 | 121.4656691396 | 31.1446231881 | 914 | 504990 | -83.07 | 17.16 | 420.15 | 0.20 | 2.90 | 1568 |
| 2024-09-20 22:21:42.858 | MS1 | 121.4656612095 | 31.1446300402 | 914 | 504990 | -83.20 | 17.78 | 392.84 | 0.04 | 2.33 | 1561 |

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
| 3213532 | 1 | 121.4736633494 | 31.1459831749 | 265 | 1 | 1 | 31.2 | TDD | 914 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3236672 | 4 | 121.4723875043 | 31.1526875719 | 118 | 13 | 3 | 38.9 | TDD | 351 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3238942 | 3 | 121.4730114938 | 31.1536797781 | 78 | 12 | 4 | 46.4 | TDD | 702 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3268828 | 2 | 121.4744693296 | 31.1475766504 | 41 | 3 | 5 | 28.4 | TDD | 621 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.119 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.236 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.236 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.970 | NREventA3 | measId:2;ServCellPCI:885;Se... |
| 2024-09-20 22:21:38.210 | NRHandoverAttempt | SourcePCI:885;SourceNR-ARFC... |
| 2024-09-20 22:21:38.255 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.267 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.411 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.411 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213532 | 1 | 18.8209 | 9.2373 | -114.2378 | 16.8330 | 147.0297 | 0.0159 | 0.0193 |
| 2024_09_20 22:00 | 3268828 | 2 | 6.9397 | 11.2056 | -115.2103 | 10.9395 | 166.9392 | 0.0114 | 0.1852 |
| 2024_09_20 22:00 | 3238942 | 3 | 16.7622 | 7.3495 | -116.3618 | 19.2344 | 99.5202 | 0.0065 | 0.0024 |
| 2024_09_20 22:00 | 3236672 | 4 | 18.3035 | 12.3900 | -114.1453 | 18.5599 | 86.2165 | 0.0184 | 0.0192 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415155_8E3AC35E | 504990 | 621 | -86.2 | 504990 | 914 | -79.3 | 504990 | 702 | -83.3 | 504990 | 351 |
| MR_1774415155_242C76BD | 504990 | 621 | -85.4 | 504990 | 914 | -77.7 | 504990 | 702 | -83.7 | 504990 | 351 |
| MR_1774415155_A655695C | 504990 | 914 | -79.4 | 504990 | 621 | -86.2 | 504990 | 702 | -83.4 | 504990 | 351 |
| MR_1774415155_AF43DAC9 | 504990 | 914 | -79.7 | 504990 | 621 | -83.7 | 504990 | 702 | -83.5 | 504990 | 351 |
| MR_1774415155_0317AD1C | 504990 | 621 | -84.4 | 504990 | 914 | -80.7 | 504990 | 702 | -84.5 | 504990 | 351 |
| MR_1774415155_7E4B5F69 | 504990 | 621 | -86.4 | 504990 | 914 | -77.5 | 504990 | 702 | -83.3 | 504990 | 351 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1925: `7f6b39ff-589...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7f6b39ff-589c-424d-9404-3a8d7a8d9a59` |
| Tag | **multiple-answer** |
| 정답 | **C15|C20** |
| C15 의미 | Increase transmission power for 3259744_1 |
| C20 의미 | Adjust the azimuth of 3259744_1 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1925] topology](images/train_1925.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251975_4
- `C2`: Increase A3 Offset threshold for 3259744_1
- `C3`: Lift the tilt angle  of 3251975_4 by 4 degrees
- `C4`: Adjust the azimuth of 3251975_4 by 8 degrees
- `C5`: Lift the tilt angle of 3259744_1 by 10 degrees
- `C6`: Decrease A3 Offset threshold for 3251975_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259744_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease transmission power for 3251975_4
- `C10`: Increase A3 Offset threshold for 3251975_4
- `C11`: Increase transmission power for 3251975_4
- `C12`: Decrease A3 Offset threshold for 3259744_1
- `C13`: Add neighbor relationship between 3259744_1 and 3251975_4
- `C14`: Press down the tilt angle  of 3251975_4 by 4 degrees
- `C15`: Increase transmission power for 3259744_1 **← 정답**
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251975_4
- `C17`: Check test server and transmission issues
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259744_1
- `C19`: Add neighbor relationship between 3213892_2 and 3251975_4
- `C20`: Adjust the azimuth of 3259744_1 by 50 degrees **← 정답**
- `C21`: Decrease transmission power for 3259744_1
- `C22`: Press down the tilt angle of 3259744_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.747 | MS1 | 121.4656640078 | 31.1446193567 | 346 | 504990 | -87.05 | 16.22 | 391.28 | 0.19 | 2.48 | 1580 |
| 2024-09-20 22:21:32.288 | MS1 | 121.4656766810 | 31.1446371627 | 346 | 504990 | -85.63 | 12.40 | 494.60 | 0.06 | 2.76 | 1576 |
| 2024-09-20 22:21:33.890 | MS1 | 121.4656773240 | 31.1446323100 | 346 | 504990 | -94.16 | 13.84 | 562.85 | 0.03 | 2.29 | 1573 |
| 2024-09-20 22:21:34.321 | MS1 | 121.4656638920 | 31.1446351121 | 346 | 504990 | -105.21 | -0.08 | 62.78 | 0.02 | 1.01 | 1574 |
| 2024-09-20 22:21:35.983 | MS1 | 121.4656611550 | 31.1446228871 | 346 | 504990 | -101.28 | 1.61 | 38.67 | 0.12 | 1.11 | 1599 |
| 2024-09-20 22:21:36.468 | MS1 | 121.4656732355 | 31.1446256539 | 346 | 504990 | -103.56 | 0.38 | 19.68 | 0.03 | 1.11 | 1563 |
| 2024-09-20 22:21:37.788 | MS1 | 121.4656696618 | 31.1446278320 | 346 | 504990 | -102.87 | -0.40 | 24.19 | 0.09 | 1.45 | 1576 |
| 2024-09-20 22:21:38.997 | MS1 | 121.4656686256 | 31.1446377755 | 346 | 504990 | -103.60 | -0.28 | 68.37 | 0.06 | 1.40 | 1579 |
| 2024-09-20 22:21:39.119 | MS1 | 121.4656603610 | 31.1446277502 | 346 | 504990 | -106.39 | -1.07 | 55.59 | 0.03 | 1.08 | 1570 |
| 2024-09-20 22:21:40.661 | MS1 | 121.4656599718 | 31.1446246682 | 346 | 504990 | -94.64 | 16.83 | 400.38 | 0.18 | 2.91 | 1593 |
| 2024-09-20 22:21:41.172 | MS1 | 121.4656655179 | 31.1446357261 | 346 | 504990 | -88.18 | 14.23 | 515.10 | 0.03 | 2.45 | 1572 |
| 2024-09-20 22:21:42.439 | MS1 | 121.4656756367 | 31.1446294497 | 346 | 504990 | -93.89 | 17.53 | 369.32 | 0.02 | 2.40 | 1585 |

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
| 3213892 | 2 | 121.4675714643 | 31.1504183158 | 37 | 2 | 2 | 27.0 | TDD | 747 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3249555 | 3 | 121.4666238519 | 31.1489165213 | 90 | 3 | 5 | 37.5 | TDD | 820 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3251975 | 4 | 121.4748973477 | 31.1445167784 | 263 | 1 | 7 | 46.1 | TDD | 718 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3259744 | 1 | 121.4701032476 | 31.1491506362 | 148 | 14 | 5 | 35.1 | TDD | 346 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.969 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.986 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.124 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.124 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.348 | NREventA2 | measId:1;ServCellPCI:14;Ser... |
| 2024-09-20 22:21:34.450 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259744 | 1 | 19.6374 | 14.7720 | -116.7622 | 12.7414 | 164.2334 | 0.1474 | 0.0055 |
| 2024_09_20 22:00 | 3213892 | 2 | 13.0054 | 5.2435 | -117.0165 | 7.7025 | 146.4128 | 0.0034 | 0.0121 |
| 2024_09_20 22:00 | 3249555 | 3 | 13.9749 | 18.4844 | -117.3118 | 6.6249 | 137.2492 | 0.0077 | 0.0105 |
| 2024_09_20 22:00 | 3251975 | 4 | 16.6773 | 13.6506 | -117.9170 | 17.6235 | 137.6707 | 0.0052 | 0.0054 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415254_E9777E3C | 504990 | 346 | -106.5 | 504990 | 718 | -106.9 | 504990 | 747 | -114.1 | 504990 | 820 |
| MR_1774415254_DB5372BB | 504990 | 346 | -105.1 | 504990 | 718 | -109.3 | 504990 | 747 | -113.9 | 504990 | 820 |
| MR_1774415254_06F441BD | 504990 | 346 | -103.3 | 504990 | 718 | -107.8 | 504990 | 747 | -114.0 | 504990 | 820 |
| MR_1774415254_5EA03342 | 504990 | 346 | -104.5 | 504990 | 718 | -109.2 | 504990 | 747 | -115.6 | 504990 | 820 |
| MR_1774415254_1CF3A17F | 504990 | 346 | -106.9 | 504990 | 718 | -108.9 | 504990 | 747 | -115.6 | 504990 | 820 |
| MR_1774415254_32C62BC5 | 504990 | 346 | -104.8 | 504990 | 718 | -110.1 | 504990 | 747 | -113.4 | 504990 | 820 |
| MR_1774415254_DD53E0B6 | 504990 | 346 | -104.9 | 504990 | 718 | -107.4 | 504990 | 747 | -116.6 | 504990 | 820 |
| MR_1774415254_811F7BF5 | 504990 | 346 | -105.5 | 504990 | 718 | -106.4 | 504990 | 747 | -114.2 | 504990 | 820 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1926: `c741dabb-7ba...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c741dabb-7ba4-48ff-8f43-3eef717796fb` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1926] topology](images/train_1926.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3213583_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213583_3
- `C3`: Adjust the azimuth of 3213583_3 by 50 degrees
- `C4`: Adjust the azimuth of 3233393_2 by 50 degrees
- `C5`: Press down the tilt angle  of 3233393_2 by 4 degrees
- `C6`: Check test server and transmission issues
- `C7`: Insufficient data; more data is needed for judgment. **← 정답**
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233393_2
- `C9`: Add neighbor relationship between 3238284_4 and 3233393_2
- `C10`: Decrease transmission power for 3213583_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233393_2
- `C12`: Press down the tilt angle of 3213583_3 by 7 degrees
- `C13`: Lift the tilt angle  of 3233393_2 by 4 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213583_3
- `C15`: Lift the tilt angle of 3213583_3 by 7 degrees
- `C16`: Decrease A3 Offset threshold for 3213583_3
- `C17`: Decrease transmission power for 3233393_2
- `C18`: Decrease A3 Offset threshold for 3233393_2
- `C19`: Add neighbor relationship between 3213583_3 and 3233393_2
- `C20`: Increase transmission power for 3233393_2
- `C21`: Increase A3 Offset threshold for 3233393_2
- `C22`: Increase transmission power for 3213583_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.404 | MS1 | 121.4656587314 | 31.1446238121 | 620 | 504990 | -90.92 | 16.78 | 576.32 | 0.04 | 2.52 | 1568 |
| 2024-09-20 22:21:32.742 | MS1 | 121.4656735166 | 31.1446195588 | 620 | 504990 | -88.02 | 14.76 | 561.18 | 0.20 | 2.36 | 1575 |
| 2024-09-20 22:21:33.513 | MS1 | 121.4656753250 | 31.1446258182 | 620 | 504990 | -88.70 | 15.75 | 361.02 | 0.14 | 2.44 | 1561 |
| 2024-09-20 22:21:34.681 | MS1 | 121.4656778763 | 31.1446264956 | 620 | 504990 | -90.85 | 17.86 | 54.88 | 0.11 | 2.57 | 1600 |
| 2024-09-20 22:21:35.332 | MS1 | 121.4656659321 | 31.1446339761 | 620 | 504990 | -89.46 | 15.31 | 69.39 | 0.01 | 2.27 | 1583 |
| 2024-09-20 22:21:36.296 | MS1 | 121.4656746489 | 31.1446316686 | 620 | 504990 | -89.66 | 12.17 | 68.59 | 0.08 | 2.09 | 1579 |
| 2024-09-20 22:21:37.872 | MS1 | 121.4656673370 | 31.1446184302 | 620 | 504990 | -91.76 | 7.44 | 60.42 | 0.12 | 2.28 | 1597 |
| 2024-09-20 22:21:38.661 | MS1 | 121.4656692268 | 31.1446324133 | 620 | 504990 | -93.69 | 12.71 | 83.91 | 0.14 | 2.58 | 1562 |
| 2024-09-20 22:21:39.421 | MS1 | 121.4656720575 | 31.1446182234 | 620 | 504990 | -93.30 | 10.37 | 64.92 | 0.18 | 2.81 | 1566 |
| 2024-09-20 22:21:40.611 | MS1 | 121.4656725036 | 31.1446235682 | 620 | 504990 | -90.32 | 11.06 | 350.99 | 0.08 | 2.11 | 1578 |
| 2024-09-20 22:21:41.785 | MS1 | 121.4656580425 | 31.1446225709 | 620 | 504990 | -91.07 | 10.29 | 346.82 | 0.02 | 2.85 | 1561 |
| 2024-09-20 22:21:42.289 | MS1 | 121.4656584470 | 31.1446363912 | 620 | 504990 | -93.46 | 10.24 | 511.85 | 0.19 | 2.81 | 1570 |

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
| 3213583 | 3 | 121.4751491767 | 31.1442023480 | 95 | 5 | 8 | 30.0 | TDD | 620 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3214144 | 1 | 121.4703461161 | 31.1525050569 | 261 | 0 | 11 | 46.3 | TDD | 729 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3233393 | 2 | 121.4697224397 | 31.1481552476 | 37 | 0 | 0 | 38.1 | TDD | 659 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3238284 | 4 | 121.4694482086 | 31.1478432559 | 176 | 14 | 9 | 17.5 | TDD | 821 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.374 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.398 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.504 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.504 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.187 | NREventA3 | measId:2;ServCellPCI:997;Se... |
| 2024-09-20 22:21:38.427 | NRHandoverAttempt | SourcePCI:997;SourceNR-ARFC... |
| 2024-09-20 22:21:38.470 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.484 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.598 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.598 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3214144 | 1 | 92.5766 | 90.6589 | -114.9926 | 15.2744 | 148.3822 | 0.0003 | 0.0112 |
| 2024_09_19 22:00 | 3233393 | 2 | 80.3699 | 90.3351 | -116.3729 | 18.7528 | 183.8596 | 0.0035 | 0.0076 |
| 2024_09_19 22:00 | 3213583 | 3 | 81.6424 | 94.9052 | -117.7697 | 5.1304 | 197.5965 | 0.0156 | 0.0144 |
| 2024_09_19 22:00 | 3238284 | 4 | 78.3953 | 93.0353 | -117.2028 | 8.3475 | 80.5555 | 0.0036 | 0.0025 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412564_4AA52F75 | 504990 | 620 | -90.4 | 504990 | 659 | -95.9 | 504990 | 821 | -100.9 | 504990 | 729 |
| MR_1774412564_9EA0DCDC | 504990 | 620 | -91.0 | 504990 | 659 | -97.5 | 504990 | 821 | -99.8 | 504990 | 729 |
| MR_1774412564_55D69D1C | 504990 | 620 | -90.7 | 504990 | 659 | -94.4 | 504990 | 821 | -101.1 | 504990 | 729 |
| MR_1774412564_5956C686 | 504990 | 620 | -90.6 | 504990 | 659 | -97.2 | 504990 | 821 | -100.0 | 504990 | 729 |
| MR_1774412564_8CD3D52E | 504990 | 620 | -92.2 | 504990 | 659 | -94.5 | 504990 | 821 | -97.7 | 504990 | 729 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1927: `b57a5908-6f7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b57a5908-6f76-4e40-ab5e-01f1ef75189d` |
| Tag | **multiple-answer** |
| 정답 | **C12|C18** |
| C12 의미 | Adjust the azimuth of 3212124_1 by 39 degrees |
| C18 의미 | Increase transmission power for 3212124_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1927] topology](images/train_1927.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease transmission power for 3214338_4
- `C3`: Increase A3 Offset threshold for 3212124_1
- `C4`: Decrease A3 Offset threshold for 3214338_4
- `C5`: Increase transmission power for 3214338_4
- `C6`: Increase A3 Offset threshold for 3214338_4
- `C7`: Check test server and transmission issues
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212124_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214338_4
- `C10`: Press down the tilt angle  of 3214338_4 by 6 degrees
- `C11`: Press down the tilt angle of 3212124_1 by 8 degrees
- `C12`: Adjust the azimuth of 3212124_1 by 39 degrees **← 정답**
- `C13`: Decrease transmission power for 3212124_1
- `C14`: Add neighbor relationship between 3279046_2 and 3214338_4
- `C15`: Decrease A3 Offset threshold for 3212124_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214338_4
- `C17`: Add neighbor relationship between 3212124_1 and 3214338_4
- `C18`: Increase transmission power for 3212124_1 **← 정답**
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212124_1
- `C20`: Lift the tilt angle  of 3214338_4 by 6 degrees
- `C21`: Lift the tilt angle of 3212124_1 by 8 degrees
- `C22`: Adjust the azimuth of 3214338_4 by 13 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.815 | MS1 | 121.4656630063 | 31.1446234919 | 96 | 504990 | -89.58 | 13.19 | 566.11 | 0.02 | 2.58 | 1582 |
| 2024-09-20 22:21:32.354 | MS1 | 121.4656653660 | 31.1446205581 | 96 | 504990 | -93.00 | 14.30 | 537.06 | 0.02 | 2.94 | 1580 |
| 2024-09-20 22:21:33.151 | MS1 | 121.4656638976 | 31.1446266402 | 96 | 504990 | -86.91 | 17.86 | 311.00 | 0.02 | 2.91 | 1571 |
| 2024-09-20 22:21:34.266 | MS1 | 121.4656751815 | 31.1446215606 | 96 | 504990 | -105.32 | -0.70 | 53.32 | 0.14 | 1.30 | 1580 |
| 2024-09-20 22:21:35.312 | MS1 | 121.4656650889 | 31.1446328459 | 96 | 504990 | -107.28 | -0.03 | 69.20 | 0.03 | 1.41 | 1565 |
| 2024-09-20 22:21:36.833 | MS1 | 121.4656663176 | 31.1446363065 | 96 | 504990 | -105.17 | -1.75 | 60.10 | 0.16 | 1.46 | 1577 |
| 2024-09-20 22:21:37.770 | MS1 | 121.4656702016 | 31.1446229884 | 96 | 504990 | -107.39 | 1.81 | 70.84 | 0.01 | 1.43 | 1599 |
| 2024-09-20 22:21:38.516 | MS1 | 121.4656590565 | 31.1446308894 | 96 | 504990 | -106.67 | 1.26 | 42.76 | 0.00 | 1.45 | 1585 |
| 2024-09-20 22:21:39.612 | MS1 | 121.4656736611 | 31.1446192924 | 96 | 504990 | -108.26 | 0.84 | 46.15 | 0.17 | 1.42 | 1583 |
| 2024-09-20 22:21:40.458 | MS1 | 121.4656650770 | 31.1446367640 | 96 | 504990 | -87.35 | 12.18 | 474.90 | 0.01 | 2.56 | 1593 |
| 2024-09-20 22:21:41.197 | MS1 | 121.4656679321 | 31.1446250218 | 96 | 504990 | -88.28 | 13.14 | 359.52 | 0.19 | 2.52 | 1560 |
| 2024-09-20 22:21:42.481 | MS1 | 121.4656741096 | 31.1446293782 | 96 | 504990 | -93.46 | 12.39 | 393.62 | 0.07 | 2.45 | 1586 |

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
| 3212124 | 1 | 121.4740664881 | 31.1477501599 | 286 | 5 | 7 | 40.9 | TDD | 96 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3214338 | 4 | 121.4707914306 | 31.1555182993 | 189 | 4 | 1 | 42.3 | TDD | 894 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3237960 | 3 | 121.4688150014 | 31.1521740263 | 32 | 3 | 7 | 30.3 | TDD | 400 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3279046 | 2 | 121.4744411935 | 31.1554320458 | 211 | 11 | 12 | 43.1 | TDD | 393 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.572 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.596 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.744 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.744 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.908 | NREventA2 | measId:1;ServCellPCI:862;Se... |
| 2024-09-20 22:21:35.044 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212124 | 1 | 12.7626 | 5.1888 | -114.2874 | 14.2178 | 136.3759 | 0.1538 | 0.0005 |
| 2024_09_20 22:00 | 3279046 | 2 | 9.9164 | 17.8142 | -117.1213 | 6.5527 | 191.3835 | 0.0118 | 0.0011 |
| 2024_09_20 22:00 | 3237960 | 3 | 17.5863 | 6.7116 | -116.1017 | 13.8651 | 117.6459 | 0.0085 | 0.0151 |
| 2024_09_20 22:00 | 3214338 | 4 | 6.1069 | 7.1752 | -115.4262 | 17.9576 | 154.7016 | 0.0128 | 0.0139 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415000_02C16639 | 504990 | 96 | -107.2 | 504990 | 894 | -110.3 | 504990 | 393 | -115.5 | 504990 | 400 |
| MR_1774415000_AFA0CCE6 | 504990 | 96 | -106.0 | 504990 | 894 | -108.5 | 504990 | 393 | -112.9 | 504990 | 400 |
| MR_1774415000_62AA4385 | 504990 | 96 | -107.0 | 504990 | 894 | -107.2 | 504990 | 393 | -113.0 | 504990 | 400 |
| MR_1774415000_E6119684 | 504990 | 96 | -104.5 | 504990 | 894 | -108.7 | 504990 | 393 | -111.5 | 504990 | 400 |
| MR_1774415000_843A099A | 504990 | 96 | -104.3 | 504990 | 894 | -109.2 | 504990 | 393 | -114.5 | 504990 | 400 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1928: `c59fb0e7-8ff...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c59fb0e7-8ff1-4752-8e93-0c5a5717f1b1` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1928] topology](images/train_1928.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3221289_1 by 50 degrees
- `C2`: Adjust the azimuth of 3242472_2 by 50 degrees
- `C3`: Increase transmission power for 3242472_2
- `C4`: Add neighbor relationship between 3242472_2 and 3221289_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242472_2
- `C6`: Add neighbor relationship between 3253065_4 and 3221289_1
- `C7`: Increase A3 Offset threshold for 3242472_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221289_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221289_1
- `C10`: Press down the tilt angle of 3242472_2 by 10 degrees
- `C11`: Lift the tilt angle  of 3221289_1 by 10 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242472_2
- `C13`: Increase transmission power for 3221289_1
- `C14`: Press down the tilt angle  of 3221289_1 by 10 degrees
- `C15`: Lift the tilt angle of 3242472_2 by 10 degrees
- `C16`: Check test server and transmission issues **← 정답**
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase A3 Offset threshold for 3221289_1
- `C19`: Decrease A3 Offset threshold for 3221289_1
- `C20`: Decrease transmission power for 3242472_2
- `C21`: Decrease transmission power for 3221289_1
- `C22`: Decrease A3 Offset threshold for 3242472_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.349 | MS1 | 121.4656615080 | 31.1446267415 | 771 | 504990 | -88.34 | 13.78 | 378.65 | 0.04 | 2.02 | 1589 |
| 2024-09-20 22:21:32.793 | MS1 | 121.4656605666 | 31.1446301498 | 771 | 504990 | -91.69 | 14.74 | 502.79 | 0.05 | 2.14 | 1574 |
| 2024-09-20 22:21:33.281 | MS1 | 121.4656744852 | 31.1446324272 | 771 | 504990 | -87.87 | 13.14 | 356.31 | 0.13 | 2.01 | 1588 |
| 2024-09-20 22:21:34.160 | MS1 | 121.4656662963 | 31.1446257469 | 771 | 504990 | -86.92 | 17.20 | 67.42 | 0.05 | 2.30 | 301 |
| 2024-09-20 22:21:35.976 | MS1 | 121.4656742094 | 31.1446290697 | 771 | 504990 | -86.67 | 17.97 | 83.42 | 0.06 | 2.46 | 389 |
| 2024-09-20 22:21:36.505 | MS1 | 121.4656596083 | 31.1446265962 | 771 | 504990 | -89.22 | 14.94 | 68.09 | 0.04 | 2.08 | 307 |
| 2024-09-20 22:21:37.750 | MS1 | 121.4656773935 | 31.1446194661 | 771 | 504990 | -90.56 | 10.48 | 86.53 | 0.10 | 2.03 | 346 |
| 2024-09-20 22:21:38.437 | MS1 | 121.4656585144 | 31.1446220495 | 771 | 504990 | -93.58 | 11.61 | 97.09 | 0.01 | 2.85 | 366 |
| 2024-09-20 22:21:39.827 | MS1 | 121.4656670225 | 31.1446208995 | 771 | 504990 | -93.66 | 8.46 | 60.21 | 0.08 | 2.87 | 494 |
| 2024-09-20 22:21:40.760 | MS1 | 121.4656632971 | 31.1446208369 | 771 | 504990 | -92.44 | 12.76 | 439.73 | 0.15 | 2.52 | 1563 |
| 2024-09-20 22:21:41.534 | MS1 | 121.4656653128 | 31.1446240069 | 771 | 504990 | -93.82 | 7.90 | 556.23 | 0.17 | 2.86 | 1593 |
| 2024-09-20 22:21:42.409 | MS1 | 121.4656671346 | 31.1446280014 | 771 | 504990 | -91.04 | 10.18 | 568.48 | 0.14 | 2.83 | 1563 |

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
| 3221289 | 1 | 121.4729988683 | 31.1464175420 | 67 | 12 | 2 | 36.1 | TDD | 465 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3242472 | 2 | 121.4655157886 | 31.1506922574 | 34 | 14 | 0 | 17.7 | TDD | 771 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3253065 | 4 | 121.4688102561 | 31.1491530140 | 52 | 9 | 6 | 40.2 | TDD | 113 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3279325 | 3 | 121.4739969475 | 31.1537066110 | 307 | 3 | 12 | 28.2 | TDD | 821 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.296 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.321 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.442 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.442 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.192 | NREventA3 | measId:2;ServCellPCI:96;Ser... |
| 2024-09-20 22:21:38.432 | NRHandoverAttempt | SourcePCI:96;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.466 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.480 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.600 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.600 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221289 | 1 | 8.5244 | 12.7995 | -115.6388 | 11.7689 | 169.1788 | 0.0105 | 0.0131 |
| 2024_09_20 22:00 | 3242472 | 2 | 11.3591 | 15.1606 | -114.0576 | 11.3063 | 99.0144 | 0.0105 | 0.0104 |
| 2024_09_20 22:00 | 3279325 | 3 | 6.7092 | 18.4134 | -114.2454 | 11.9271 | 176.3903 | 0.0140 | 0.0179 |
| 2024_09_20 22:00 | 3253065 | 4 | 7.6100 | 13.4004 | -117.6708 | 12.2808 | 100.1155 | 0.0089 | 0.0064 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411976_7E1F40DB | 504990 | 771 | -85.6 | 504990 | 465 | -97.9 | 504990 | 113 | -100.7 | 504990 | 821 |
| MR_1774411976_F7919FCB | 504990 | 771 | -85.2 | 504990 | 465 | -94.5 | 504990 | 113 | -101.5 | 504990 | 821 |
| MR_1774411976_C33C2738 | 504990 | 771 | -86.7 | 504990 | 465 | -96.9 | 504990 | 113 | -100.2 | 504990 | 821 |
| MR_1774411976_9AF201CD | 504990 | 771 | -88.3 | 504990 | 465 | -94.5 | 504990 | 113 | -100.1 | 504990 | 821 |
| MR_1774411976_CB837DAB | 504990 | 771 | -86.9 | 504990 | 465 | -97.0 | 504990 | 113 | -101.5 | 504990 | 821 |
| MR_1774411976_B3F004D7 | 504990 | 771 | -86.7 | 504990 | 465 | -95.9 | 504990 | 113 | -102.9 | 504990 | 821 |
| MR_1774411976_00BC6B91 | 504990 | 771 | -87.4 | 504990 | 465 | -95.6 | 504990 | 113 | -102.1 | 504990 | 821 |
| MR_1774411976_A401FC9D | 504990 | 771 | -86.1 | 504990 | 465 | -97.8 | 504990 | 113 | -101.2 | 504990 | 821 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1929: `c2941e9a-80a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c2941e9a-80a2-498c-bf4c-d752e3ad1c18` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1929] topology](images/train_1929.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3250400_1
- `C2`: Adjust the azimuth of 3250400_1 by 50 degrees
- `C3`: Check test server and transmission issues **← 정답**
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247917_2
- `C5`: Decrease A3 Offset threshold for 3247917_2
- `C6`: Decrease transmission power for 3250400_1
- `C7`: Increase A3 Offset threshold for 3247917_2
- `C8`: Increase transmission power for 3247917_2
- `C9`: Lift the tilt angle of 3250400_1 by 10 degrees
- `C10`: Add neighbor relationship between 3250400_1 and 3247917_2
- `C11`: Add neighbor relationship between 3242511_4 and 3247917_2
- `C12`: Lift the tilt angle  of 3247917_2 by 9 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247917_2
- `C14`: Press down the tilt angle  of 3247917_2 by 9 degrees
- `C15`: Press down the tilt angle of 3250400_1 by 10 degrees
- `C16`: Decrease transmission power for 3247917_2
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250400_1
- `C19`: Increase A3 Offset threshold for 3250400_1
- `C20`: Adjust the azimuth of 3247917_2 by 50 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250400_1
- `C22`: Decrease A3 Offset threshold for 3250400_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.296 | MS1 | 121.4656772071 | 31.1446319717 | 927 | 504990 | -86.21 | 12.86 | 420.46 | 0.16 | 2.22 | 1595 |
| 2024-09-20 22:21:32.262 | MS1 | 121.4656643285 | 31.1446234228 | 927 | 504990 | -90.69 | 16.14 | 297.75 | 0.14 | 2.24 | 1581 |
| 2024-09-20 22:21:33.573 | MS1 | 121.4656586841 | 31.1446362221 | 927 | 504990 | -91.72 | 14.02 | 347.52 | 0.14 | 2.90 | 1589 |
| 2024-09-20 22:21:34.656 | MS1 | 121.4656720390 | 31.1446351103 | 927 | 504990 | -86.62 | 13.93 | 93.24 | 0.13 | 2.62 | 335 |
| 2024-09-20 22:21:35.459 | MS1 | 121.4656721547 | 31.1446230043 | 927 | 504990 | -90.24 | 13.26 | 86.38 | 0.03 | 2.85 | 320 |
| 2024-09-20 22:21:36.717 | MS1 | 121.4656767596 | 31.1446344127 | 927 | 504990 | -85.58 | 13.12 | 70.02 | 0.05 | 2.17 | 490 |
| 2024-09-20 22:21:37.718 | MS1 | 121.4656586642 | 31.1446343188 | 927 | 504990 | -89.80 | 8.56 | 74.75 | 0.08 | 2.80 | 354 |
| 2024-09-20 22:21:38.581 | MS1 | 121.4656709327 | 31.1446229173 | 927 | 504990 | -89.06 | 12.05 | 62.47 | 0.13 | 2.13 | 443 |
| 2024-09-20 22:21:39.703 | MS1 | 121.4656642771 | 31.1446279799 | 927 | 504990 | -92.78 | 9.92 | 86.17 | 0.19 | 2.07 | 480 |
| 2024-09-20 22:21:40.874 | MS1 | 121.4656624555 | 31.1446253409 | 927 | 504990 | -93.82 | 11.52 | 297.87 | 0.17 | 2.50 | 1575 |
| 2024-09-20 22:21:41.230 | MS1 | 121.4656581735 | 31.1446221472 | 927 | 504990 | -93.10 | 9.87 | 429.41 | 0.10 | 2.56 | 1584 |
| 2024-09-20 22:21:42.886 | MS1 | 121.4656752605 | 31.1446294619 | 927 | 504990 | -90.37 | 10.03 | 579.63 | 0.18 | 2.81 | 1589 |

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
| 3242511 | 4 | 121.4757343072 | 31.1474102683 | 23 | 2 | 6 | 34.5 | TDD | 31 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3247459 | 3 | 121.4752152287 | 31.1539951951 | 326 | 4 | 8 | 48.2 | TDD | 658 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3247917 | 2 | 121.4718443800 | 31.1458040349 | 137 | 6 | 0 | 32.7 | TDD | 89 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3250400 | 1 | 121.4665929690 | 31.1452663362 | 165 | 7 | 0 | 29.9 | TDD | 927 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.958 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.982 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.123 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.123 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.804 | NREventA3 | measId:2;ServCellPCI:758;Se... |
| 2024-09-20 22:21:38.044 | NRHandoverAttempt | SourcePCI:758;SourceNR-ARFC... |
| 2024-09-20 22:21:38.079 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.089 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.233 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.233 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250400 | 1 | 12.1258 | 14.1888 | -117.5265 | 16.9410 | 109.1848 | 0.0193 | 0.0121 |
| 2024_09_20 22:00 | 3247917 | 2 | 17.5252 | 12.9900 | -116.5464 | 18.1707 | 192.4798 | 0.0199 | 0.0038 |
| 2024_09_20 22:00 | 3247459 | 3 | 8.5086 | 5.3448 | -115.4082 | 5.9234 | 142.5796 | 0.0070 | 0.0097 |
| 2024_09_20 22:00 | 3242511 | 4 | 6.3788 | 6.0758 | -116.2519 | 13.2577 | 116.0477 | 0.0033 | 0.0027 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414500_93538640 | 504990 | 927 | -85.9 | 504990 | 89 | -95.3 | 504990 | 31 | -100.7 | 504990 | 658 |
| MR_1774414500_B2DFBBD1 | 504990 | 927 | -88.5 | 504990 | 89 | -92.5 | 504990 | 31 | -99.5 | 504990 | 658 |
| MR_1774414500_D1BC7F9B | 504990 | 927 | -86.3 | 504990 | 89 | -91.7 | 504990 | 31 | -99.1 | 504990 | 658 |
| MR_1774414500_0B9BBD83 | 504990 | 927 | -88.4 | 504990 | 89 | -93.7 | 504990 | 31 | -100.4 | 504990 | 658 |
| MR_1774414500_05C3E986 | 504990 | 927 | -85.6 | 504990 | 89 | -93.3 | 504990 | 31 | -101.1 | 504990 | 658 |
| MR_1774414500_0FEA820A | 504990 | 927 | -88.5 | 504990 | 89 | -93.4 | 504990 | 31 | -98.4 | 504990 | 658 |

> *... 2개 열 생략 (전체 14열)*

---
