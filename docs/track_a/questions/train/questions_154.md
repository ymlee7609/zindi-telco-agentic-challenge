# Track A 문제 분석 — train[1530]~train[1539]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1530] ~ train[1539] (10개)

## 목차

1. [문제 1530: `c3019a1d-75e...`](#1530) — single-answer, 정답: C10
2. [문제 1531: `8fb6be05-f93...`](#1531) — single-answer, 정답: C1
3. [문제 1532: `2f92e38b-939...`](#1532) — single-answer, 정답: C2
4. [문제 1533: `efee3314-637...`](#1533) — single-answer, 정답: C5
5. [문제 1534: `dad544de-018...`](#1534) — single-answer, 정답: C16
6. [문제 1535: `ae2c8d0a-a3f...`](#1535) — single-answer, 정답: C18
7. [문제 1536: `64195173-b95...`](#1536) — single-answer, 정답: C19
8. [문제 1537: `3684dd34-38b...`](#1537) — single-answer, 정답: C21
9. [문제 1538: `113294c7-9af...`](#1538) — single-answer, 정답: C14
10. [문제 1539: `ea9a5cbe-b24...`](#1539) — single-answer, 정답: C19

---

### 문제 1530: `c3019a1d-75e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c3019a1d-75eb-443c-9b9c-05bc732eed35` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Add neighbor relationship between 3252371_2 and 3275153_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1530] topology](images/train_1530.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3252371_2 by 10 degrees
- `C2`: Increase transmission power for 3252371_2
- `C3`: Press down the tilt angle  of 3275153_3 by 4 degrees
- `C4`: Lift the tilt angle  of 3275153_3 by 4 degrees
- `C5`: Decrease A3 Offset threshold for 3275153_3
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Add neighbor relationship between 3221736_1 and 3275153_3
- `C8`: Adjust the azimuth of 3252371_2 by 50 degrees
- `C9`: Decrease transmission power for 3275153_3
- `C10`: Add neighbor relationship between 3252371_2 and 3275153_3 **← 정답**
- `C11`: Increase A3 Offset threshold for 3252371_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252371_2
- `C13`: Increase transmission power for 3275153_3
- `C14`: Press down the tilt angle of 3252371_2 by 10 degrees
- `C15`: Check test server and transmission issues
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252371_2
- `C17`: Decrease A3 Offset threshold for 3252371_2
- `C18`: Increase A3 Offset threshold for 3275153_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275153_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275153_3
- `C21`: Adjust the azimuth of 3275153_3 by 4 degrees
- `C22`: Decrease transmission power for 3252371_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.428 | MS1 | 121.4656703904 | 31.1446193283 | 196 | 504990 | -78.78 | 16.00 | 544.48 | 0.20 | 2.27 | 1568 |
| 2024-09-20 22:21:32.670 | MS1 | 121.4656728980 | 31.1446374957 | 196 | 504990 | -79.92 | 15.99 | 324.14 | 0.06 | 2.24 | 1598 |
| 2024-09-20 22:21:33.287 | MS1 | 121.4656660612 | 31.1446293416 | 196 | 504990 | -79.09 | 14.79 | 319.55 | 0.17 | 2.90 | 1592 |
| 2024-09-20 22:21:34.205 | MS1 | 121.4656679284 | 31.1446226806 | 196 | 504990 | -92.35 | -2.44 | 59.72 | 0.04 | 1.39 | 1580 |
| 2024-09-20 22:21:35.924 | MS1 | 121.4656591007 | 31.1446331093 | 196 | 504990 | -89.51 | -2.29 | 28.41 | 0.02 | 1.38 | 1600 |
| 2024-09-20 22:21:36.867 | MS1 | 121.4656748091 | 31.1446220412 | 196 | 504990 | -90.17 | -0.31 | 42.90 | 0.12 | 1.12 | 1585 |
| 2024-09-20 22:21:37.344 | MS1 | 121.4656643879 | 31.1446241767 | 196 | 504990 | -88.37 | -3.58 | 47.95 | 0.18 | 1.11 | 1582 |
| 2024-09-20 22:21:38.258 | MS1 | 121.4656615653 | 31.1446195757 | 196 | 504990 | -78.96 | 16.74 | 511.30 | 0.10 | 1.33 | 1595 |
| 2024-09-20 22:21:39.943 | MS1 | 121.4656585961 | 31.1446271471 | 196 | 504990 | -77.35 | 16.12 | 357.25 | 0.18 | 1.30 | 1595 |
| 2024-09-20 22:21:40.200 | MS1 | 121.4656594480 | 31.1446180197 | 196 | 504990 | -77.14 | 16.59 | 518.87 | 0.04 | 2.63 | 1580 |
| 2024-09-20 22:21:41.219 | MS1 | 121.4656741946 | 31.1446313884 | 196 | 504990 | -79.91 | 15.83 | 352.98 | 0.01 | 2.30 | 1563 |
| 2024-09-20 22:21:42.227 | MS1 | 121.4656654349 | 31.1446271302 | 196 | 504990 | -79.11 | 17.92 | 410.73 | 0.08 | 2.08 | 1573 |

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
| 3221736 | 1 | 121.4656428696 | 31.1465812564 | 28 | 1 | 3 | 28.3 | TDD | 240 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3252371 | 2 | 121.4726768601 | 31.1507133756 | 359 | 8 | 7 | 47.2 | TDD | 196 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3264077 | 4 | 121.4664373845 | 31.1531108557 | 110 | 2 | 5 | 49.2 | TDD | 863 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3275153 | 3 | 121.4753448036 | 31.1555384352 | 213 | 3 | 5 | 32.1 | TDD | 822 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.975 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.000 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.102 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.102 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.847 | NREventA3 | measId:2;ServCellPCI:970;Se... |
| 2024-09-20 22:21:35.847 | NREventA3 | measId:2;ServCellPCI:970;Se... |
| 2024-09-20 22:21:36.847 | NREventA3 | measId:2;ServCellPCI:970;Se... |
| 2024-09-20 22:21:39.347 | NRRRCReestablishAttempt | PCI:970 |
| 2024-09-20 22:21:39.366 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.377 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.509 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.509 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221736 | 1 | 5.8158 | 17.1018 | -115.7107 | 8.2538 | 139.2945 | 0.0014 | 0.0142 |
| 2024_09_20 22:00 | 3252371 | 2 | 13.5840 | 13.4321 | -115.0117 | 18.2291 | 124.8378 | 0.0055 | 0.1586 |
| 2024_09_20 22:00 | 3275153 | 3 | 5.1595 | 8.1266 | -117.7018 | 18.6617 | 118.8219 | 0.0108 | 0.0114 |
| 2024_09_20 22:00 | 3264077 | 4 | 12.9447 | 18.2101 | -117.6307 | 7.3046 | 113.1813 | 0.0040 | 0.0171 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413827_271696AD | 504990 | 822 | -86.4 | 504990 | 196 | -92.1 | 504990 | 240 | -94.4 | 504990 | 863 |
| MR_1774413827_C597E924 | 504990 | 196 | -91.4 | 504990 | 822 | -84.8 | 504990 | 240 | -97.1 | 504990 | 863 |
| MR_1774413827_AF2B7DA6 | 504990 | 822 | -87.3 | 504990 | 196 | -91.7 | 504990 | 240 | -95.9 | 504990 | 863 |
| MR_1774413827_22E9CCD7 | 504990 | 822 | -85.8 | 504990 | 196 | -92.2 | 504990 | 240 | -95.5 | 504990 | 863 |
| MR_1774413827_B7F43156 | 504990 | 196 | -91.1 | 504990 | 822 | -86.8 | 504990 | 240 | -95.8 | 504990 | 863 |
| MR_1774413827_2F043302 | 504990 | 196 | -92.6 | 504990 | 822 | -87.5 | 504990 | 240 | -93.8 | 504990 | 863 |
| MR_1774413827_E61BA273 | 504990 | 196 | -93.3 | 504990 | 822 | -86.1 | 504990 | 240 | -94.5 | 504990 | 863 |
| MR_1774413827_1B54F903 | 504990 | 822 | -85.4 | 504990 | 196 | -92.2 | 504990 | 240 | -94.8 | 504990 | 863 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1531: `8fb6be05-f93...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8fb6be05-f93e-4df8-9a9a-704c440f1f99` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1531] topology](images/train_1531.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment. **← 정답**
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225858_3
- `C3`: Add neighbor relationship between 3257043_1 and 3218611_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225858_3
- `C5`: Press down the tilt angle  of 3218611_2 by 9 degrees
- `C6`: Decrease A3 Offset threshold for 3225858_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218611_2
- `C8`: Lift the tilt angle  of 3218611_2 by 9 degrees
- `C9`: Check test server and transmission issues
- `C10`: Increase A3 Offset threshold for 3218611_2
- `C11`: Lift the tilt angle of 3225858_3 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218611_2
- `C13`: Increase A3 Offset threshold for 3225858_3
- `C14`: Increase transmission power for 3225858_3
- `C15`: Add neighbor relationship between 3225858_3 and 3218611_2
- `C16`: Adjust the azimuth of 3225858_3 by 14 degrees
- `C17`: Decrease transmission power for 3225858_3
- `C18`: Decrease transmission power for 3218611_2
- `C19`: Increase transmission power for 3218611_2
- `C20`: Decrease A3 Offset threshold for 3218611_2
- `C21`: Press down the tilt angle of 3225858_3 by 10 degrees
- `C22`: Adjust the azimuth of 3218611_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.509 | MS1 | 121.4656704657 | 31.1446360572 | 915 | 504990 | -89.42 | 17.46 | 565.75 | 0.16 | 2.38 | 1588 |
| 2024-09-20 22:21:32.553 | MS1 | 121.4656598063 | 31.1446356813 | 915 | 504990 | -90.55 | 16.92 | 604.15 | 0.16 | 2.06 | 1600 |
| 2024-09-20 22:21:33.717 | MS1 | 121.4656661089 | 31.1446290800 | 915 | 504990 | -85.93 | 16.52 | 531.04 | 0.04 | 2.04 | 1584 |
| 2024-09-20 22:21:34.437 | MS1 | 121.4656671273 | 31.1446288699 | 915 | 504990 | -85.17 | 16.66 | 88.27 | 0.20 | 2.33 | 1584 |
| 2024-09-20 22:21:35.304 | MS1 | 121.4656680934 | 31.1446366530 | 915 | 504990 | -87.61 | 17.98 | 64.33 | 0.07 | 2.47 | 1598 |
| 2024-09-20 22:21:36.137 | MS1 | 121.4656588835 | 31.1446246432 | 915 | 504990 | -86.02 | 17.93 | 72.36 | 0.15 | 2.25 | 1583 |
| 2024-09-20 22:21:37.395 | MS1 | 121.4656671689 | 31.1446183965 | 915 | 504990 | -89.73 | 11.20 | 63.97 | 0.04 | 2.55 | 1584 |
| 2024-09-20 22:21:38.148 | MS1 | 121.4656646580 | 31.1446193027 | 915 | 504990 | -92.23 | 9.27 | 74.89 | 0.10 | 2.56 | 1586 |
| 2024-09-20 22:21:39.349 | MS1 | 121.4656737721 | 31.1446321620 | 915 | 504990 | -90.81 | 12.07 | 77.12 | 0.02 | 2.23 | 1568 |
| 2024-09-20 22:21:40.386 | MS1 | 121.4656589822 | 31.1446318628 | 915 | 504990 | -93.71 | 12.82 | 393.21 | 0.18 | 2.97 | 1591 |
| 2024-09-20 22:21:41.483 | MS1 | 121.4656746076 | 31.1446359227 | 915 | 504990 | -89.50 | 8.09 | 553.37 | 0.14 | 2.93 | 1581 |
| 2024-09-20 22:21:42.929 | MS1 | 121.4656727470 | 31.1446222589 | 915 | 504990 | -89.30 | 11.99 | 569.98 | 0.06 | 2.01 | 1587 |

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
| 3218611 | 2 | 121.4757832628 | 31.1524819692 | 6 | 8 | 6 | 30.7 | TDD | 99 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3225858 | 3 | 121.4640072022 | 31.1442555988 | 90 | 9 | 2 | 41.4 | TDD | 915 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3257043 | 1 | 121.4745487024 | 31.1512371680 | 173 | 10 | 9 | 44.2 | TDD | 98 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3279577 | 4 | 121.4747306727 | 31.1457789503 | 280 | 1 | 1 | 43.6 | TDD | 149 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.003 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.025 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.143 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.143 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.863 | NREventA3 | measId:2;ServCellPCI:283;Se... |
| 2024-09-20 22:21:38.103 | NRHandoverAttempt | SourcePCI:283;SourceNR-ARFC... |
| 2024-09-20 22:21:38.133 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.143 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.279 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.279 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3257043 | 1 | 91.3626 | 88.0653 | -116.4375 | 16.5054 | 113.2420 | 0.0029 | 0.0172 |
| 2024_09_19 22:00 | 3218611 | 2 | 75.9857 | 80.3675 | -116.2639 | 16.0328 | 171.6875 | 0.0110 | 0.0197 |
| 2024_09_19 22:00 | 3225858 | 3 | 82.5482 | 94.4109 | -117.6983 | 17.1205 | 98.2257 | 0.0169 | 0.0122 |
| 2024_09_19 22:00 | 3279577 | 4 | 88.6196 | 87.6068 | -117.0329 | 16.5553 | 181.2400 | 0.0083 | 0.0069 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415819_69DF9BC5 | 504990 | 915 | -86.6 | 504990 | 99 | -96.4 | 504990 | 98 | -96.3 | 504990 | 149 |
| MR_1774415819_54CC2E33 | 504990 | 915 | -84.0 | 504990 | 99 | -94.7 | 504990 | 98 | -95.0 | 504990 | 149 |
| MR_1774415819_7D8A4E05 | 504990 | 915 | -86.3 | 504990 | 99 | -92.5 | 504990 | 98 | -95.3 | 504990 | 149 |
| MR_1774415819_70ACABBA | 504990 | 915 | -86.8 | 504990 | 99 | -94.3 | 504990 | 98 | -96.4 | 504990 | 149 |
| MR_1774415819_B3535446 | 504990 | 915 | -85.8 | 504990 | 99 | -95.9 | 504990 | 98 | -96.2 | 504990 | 149 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1532: `2f92e38b-939...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2f92e38b-9394-4783-b2c6-aa544da657d4` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Add neighbor relationship between 3225515_1 and 3214285_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1532] topology](images/train_1532.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214285_3
- `C2`: Add neighbor relationship between 3225515_1 and 3214285_3 **← 정답**
- `C3`: Decrease transmission power for 3225515_1
- `C4`: Increase transmission power for 3225515_1
- `C5`: Press down the tilt angle of 3225515_1 by 5 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214285_3
- `C7`: Decrease transmission power for 3214285_3
- `C8`: Lift the tilt angle of 3225515_1 by 5 degrees
- `C9`: Add neighbor relationship between 3277313_4 and 3214285_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225515_1
- `C11`: Increase A3 Offset threshold for 3225515_1
- `C12`: Increase A3 Offset threshold for 3214285_3
- `C13`: Decrease A3 Offset threshold for 3225515_1
- `C14`: Increase transmission power for 3214285_3
- `C15`: Decrease A3 Offset threshold for 3214285_3
- `C16`: Check test server and transmission issues
- `C17`: Press down the tilt angle  of 3214285_3 by 3 degrees
- `C18`: Lift the tilt angle  of 3214285_3 by 3 degrees
- `C19`: Adjust the azimuth of 3225515_1 by 50 degrees
- `C20`: Adjust the azimuth of 3214285_3 by 26 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225515_1
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.276 | MS1 | 121.4656735867 | 31.1446357927 | 760 | 504990 | -79.46 | 12.44 | 577.80 | 0.04 | 2.82 | 1562 |
| 2024-09-20 22:21:32.279 | MS1 | 121.4656679480 | 31.1446239960 | 760 | 504990 | -81.23 | 12.08 | 391.94 | 0.17 | 2.32 | 1568 |
| 2024-09-20 22:21:33.637 | MS1 | 121.4656775181 | 31.1446337413 | 760 | 504990 | -76.99 | 14.41 | 509.68 | 0.07 | 2.37 | 1576 |
| 2024-09-20 22:21:34.160 | MS1 | 121.4656701020 | 31.1446186136 | 760 | 504990 | -91.02 | -1.28 | 44.92 | 0.03 | 1.31 | 1574 |
| 2024-09-20 22:21:35.849 | MS1 | 121.4656647125 | 31.1446198349 | 760 | 504990 | -92.21 | -0.87 | 32.52 | 0.02 | 1.08 | 1566 |
| 2024-09-20 22:21:36.106 | MS1 | 121.4656672438 | 31.1446327631 | 760 | 504990 | -86.02 | -0.04 | 27.80 | 0.03 | 1.03 | 1563 |
| 2024-09-20 22:21:37.840 | MS1 | 121.4656582882 | 31.1446358179 | 760 | 504990 | -94.18 | -0.83 | 44.17 | 0.01 | 1.06 | 1562 |
| 2024-09-20 22:21:38.716 | MS1 | 121.4656773729 | 31.1446184010 | 760 | 504990 | -82.04 | 12.91 | 420.93 | 0.02 | 1.16 | 1596 |
| 2024-09-20 22:21:39.425 | MS1 | 121.4656757094 | 31.1446243722 | 760 | 504990 | -78.23 | 12.99 | 350.14 | 0.04 | 1.02 | 1571 |
| 2024-09-20 22:21:40.138 | MS1 | 121.4656701489 | 31.1446269027 | 760 | 504990 | -79.46 | 17.42 | 321.29 | 0.16 | 2.31 | 1567 |
| 2024-09-20 22:21:41.165 | MS1 | 121.4656670875 | 31.1446312413 | 760 | 504990 | -81.45 | 17.29 | 357.85 | 0.03 | 2.31 | 1595 |
| 2024-09-20 22:21:42.144 | MS1 | 121.4656649690 | 31.1446373124 | 760 | 504990 | -79.22 | 14.21 | 434.13 | 0.07 | 2.23 | 1595 |

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
| 3213588 | 2 | 121.4729021465 | 31.1462922608 | 103 | 2 | 6 | 38.6 | TDD | 825 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3214285 | 3 | 121.4721114253 | 31.1518804084 | 191 | 1 | 4 | 41.5 | TDD | 66 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3225515 | 1 | 121.4685533297 | 31.1550220928 | 80 | 3 | 11 | 48.2 | TDD | 760 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3277313 | 4 | 121.4683789646 | 31.1527490576 | 282 | 6 | 3 | 31.5 | TDD | 596 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.269 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.284 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.425 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.425 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.121 | NREventA3 | measId:2;ServCellPCI:970;Se... |
| 2024-09-20 22:21:36.121 | NREventA3 | measId:2;ServCellPCI:970;Se... |
| 2024-09-20 22:21:37.121 | NREventA3 | measId:2;ServCellPCI:970;Se... |
| 2024-09-20 22:21:39.621 | NRRRCReestablishAttempt | PCI:970 |
| 2024-09-20 22:21:39.639 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.653 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.802 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.802 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225515 | 1 | 9.4165 | 8.3843 | -115.4543 | 6.7309 | 151.8831 | 0.0133 | 0.1112 |
| 2024_09_20 22:00 | 3213588 | 2 | 8.7738 | 12.6887 | -116.7987 | 13.0426 | 169.3474 | 0.0160 | 0.0022 |
| 2024_09_20 22:00 | 3214285 | 3 | 6.7201 | 6.0780 | -116.5772 | 15.5081 | 184.6285 | 0.0092 | 0.0179 |
| 2024_09_20 22:00 | 3277313 | 4 | 19.7670 | 19.2612 | -117.0208 | 5.7069 | 131.0081 | 0.0034 | 0.0026 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415981_3ED33896 | 504990 | 760 | -90.0 | 504990 | 66 | -86.8 | 504990 | 596 | -90.3 | 504990 | 825 |
| MR_1774415981_4580FA3E | 504990 | 66 | -86.0 | 504990 | 760 | -91.3 | 504990 | 596 | -87.9 | 504990 | 825 |
| MR_1774415981_AAF8CD34 | 504990 | 760 | -92.9 | 504990 | 66 | -86.2 | 504990 | 596 | -89.0 | 504990 | 825 |
| MR_1774415981_9DC004ED | 504990 | 760 | -90.0 | 504990 | 66 | -87.2 | 504990 | 596 | -89.9 | 504990 | 825 |
| MR_1774415981_18F88866 | 504990 | 760 | -90.3 | 504990 | 66 | -84.6 | 504990 | 596 | -90.4 | 504990 | 825 |
| MR_1774415981_8474852C | 504990 | 66 | -86.7 | 504990 | 760 | -92.1 | 504990 | 596 | -88.0 | 504990 | 825 |
| MR_1774415981_56CAD13D | 504990 | 760 | -89.7 | 504990 | 66 | -84.8 | 504990 | 596 | -90.6 | 504990 | 825 |
| MR_1774415981_6DBF45B2 | 504990 | 760 | -91.2 | 504990 | 66 | -86.8 | 504990 | 596 | -89.2 | 504990 | 825 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1533: `efee3314-637...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `efee3314-6375-42d3-b958-a19daf5d618f` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Decrease A3 Offset threshold for 3244307_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1533] topology](images/train_1533.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3236530_3 and 3274789_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase transmission power for 3274789_2
- `C4`: Decrease transmission power for 3244307_4
- `C5`: Decrease A3 Offset threshold for 3244307_4 **← 정답**
- `C6`: Lift the tilt angle  of 3274789_2 by 8 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244307_4
- `C8`: Press down the tilt angle  of 3274789_2 by 8 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274789_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244307_4
- `C11`: Decrease transmission power for 3274789_2
- `C12`: Increase A3 Offset threshold for 3244307_4
- `C13`: Add neighbor relationship between 3244307_4 and 3274789_2
- `C14`: Decrease A3 Offset threshold for 3274789_2
- `C15`: Adjust the azimuth of 3274789_2 by 50 degrees
- `C16`: Adjust the azimuth of 3244307_4 by 50 degrees
- `C17`: Increase A3 Offset threshold for 3274789_2
- `C18`: Press down the tilt angle of 3244307_4 by 10 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274789_2
- `C20`: Increase transmission power for 3244307_4
- `C21`: Lift the tilt angle of 3244307_4 by 10 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.458 | MS1 | 121.4656613484 | 31.1446300746 | 669 | 504990 | -76.65 | 15.66 | 560.51 | 0.16 | 2.00 | 1576 |
| 2024-09-20 22:21:32.749 | MS1 | 121.4656581509 | 31.1446206696 | 669 | 504990 | -76.10 | 15.12 | 551.11 | 0.07 | 2.08 | 1581 |
| 2024-09-20 22:21:33.197 | MS1 | 121.4656583800 | 31.1446340460 | 669 | 504990 | -76.91 | 17.20 | 404.21 | 0.11 | 2.65 | 1560 |
| 2024-09-20 22:21:34.459 | MS1 | 121.4656668021 | 31.1446366154 | 669 | 504990 | -84.24 | -1.79 | 30.59 | 0.08 | 1.37 | 1582 |
| 2024-09-20 22:21:35.117 | MS1 | 121.4656769316 | 31.1446355674 | 669 | 504990 | -83.02 | -2.16 | 63.86 | 0.06 | 1.04 | 1581 |
| 2024-09-20 22:21:36.376 | MS1 | 121.4656601164 | 31.1446199850 | 669 | 504990 | -88.12 | -3.59 | 47.33 | 0.02 | 1.48 | 1575 |
| 2024-09-20 22:21:37.241 | MS1 | 121.4656596422 | 31.1446361511 | 669 | 504990 | -92.05 | -0.33 | 60.49 | 0.13 | 1.49 | 1562 |
| 2024-09-20 22:21:38.765 | MS1 | 121.4656720392 | 31.1446223271 | 669 | 504990 | -84.05 | -1.67 | 73.16 | 0.05 | 1.39 | 1565 |
| 2024-09-20 22:21:39.872 | MS1 | 121.4656761299 | 31.1446273127 | 650 | 504990 | -81.88 | 13.95 | 247.49 | 0.02 | 1.04 | 1565 |
| 2024-09-20 22:21:40.303 | MS1 | 121.4656637671 | 31.1446264036 | 650 | 504990 | -76.85 | 16.41 | 428.13 | 0.17 | 2.86 | 1589 |
| 2024-09-20 22:21:41.887 | MS1 | 121.4656671772 | 31.1446340665 | 650 | 504990 | -84.60 | 16.65 | 378.26 | 0.14 | 2.77 | 1583 |
| 2024-09-20 22:21:42.546 | MS1 | 121.4656646639 | 31.1446317322 | 650 | 504990 | -80.64 | 13.68 | 325.45 | 0.15 | 2.89 | 1591 |

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
| 3236530 | 3 | 121.4642569374 | 31.1488316936 | 222 | 5 | 7 | 44.7 | TDD | 444 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3244307 | 4 | 121.4744992305 | 31.1448859611 | 109 | 14 | 8 | 15.9 | TDD | 669 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3253644 | 1 | 121.4726648246 | 31.1559141134 | 25 | 0 | 10 | 46.8 | TDD | 728 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3274789 | 2 | 121.4648383857 | 31.1504369941 | 20 | 6 | 8 | 22.3 | TDD | 650 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.252 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.271 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.415 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.415 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.146 | NREventA3 | measId:2;ServCellPCI:444;Se... |
| 2024-09-20 22:21:38.386 | NRHandoverAttempt | SourcePCI:444;SourceNR-ARFC... |
| 2024-09-20 22:21:38.425 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.439 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.556 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.556 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253644 | 1 | 12.8261 | 9.3647 | -116.9828 | 19.5462 | 111.9610 | 0.0161 | 0.0029 |
| 2024_09_20 22:00 | 3274789 | 2 | 12.9486 | 9.1460 | -114.8775 | 11.4953 | 188.3844 | 0.0018 | 0.0167 |
| 2024_09_20 22:00 | 3236530 | 3 | 16.3304 | 10.6675 | -116.7423 | 15.7277 | 159.1136 | 0.0002 | 0.0112 |
| 2024_09_20 22:00 | 3244307 | 4 | 15.3866 | 14.0782 | -114.0163 | 18.1427 | 180.0708 | 0.0030 | 0.1204 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415717_1028A329 | 504990 | 650 | -77.2 | 504990 | 669 | -84.5 | 504990 | 444 | -79.0 | 504990 | 728 |
| MR_1774415717_354F16AD | 504990 | 669 | -83.6 | 504990 | 650 | -78.2 | 504990 | 444 | -80.8 | 504990 | 728 |
| MR_1774415717_21D73BC5 | 504990 | 650 | -77.5 | 504990 | 669 | -84.1 | 504990 | 444 | -80.2 | 504990 | 728 |
| MR_1774415717_8D55D4D1 | 504990 | 650 | -81.2 | 504990 | 669 | -83.2 | 504990 | 444 | -77.7 | 504990 | 728 |
| MR_1774415717_BAE1DC74 | 504990 | 650 | -80.0 | 504990 | 669 | -83.4 | 504990 | 444 | -80.1 | 504990 | 728 |
| MR_1774415717_4B137352 | 504990 | 669 | -84.5 | 504990 | 650 | -77.2 | 504990 | 444 | -77.5 | 504990 | 728 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1534: `dad544de-018...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dad544de-0187-495e-b983-a96de0020477` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1534] topology](images/train_1534.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease A3 Offset threshold for 3277614_3
- `C3`: Lift the tilt angle  of 3277614_3 by 9 degrees
- `C4`: Add neighbor relationship between 3214347_2 and 3277614_3
- `C5`: Adjust the azimuth of 3222905_4 by 50 degrees
- `C6`: Increase A3 Offset threshold for 3222905_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222905_4
- `C8`: Increase A3 Offset threshold for 3277614_3
- `C9`: Add neighbor relationship between 3222905_4 and 3277614_3
- `C10`: Adjust the azimuth of 3277614_3 by 50 degrees
- `C11`: Decrease A3 Offset threshold for 3222905_4
- `C12`: Decrease transmission power for 3222905_4
- `C13`: Lift the tilt angle of 3222905_4 by 8 degrees
- `C14`: Increase transmission power for 3222905_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222905_4
- `C16`: Check test server and transmission issues **← 정답**
- `C17`: Press down the tilt angle  of 3277614_3 by 9 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277614_3
- `C19`: Decrease transmission power for 3277614_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277614_3
- `C21`: Increase transmission power for 3277614_3
- `C22`: Press down the tilt angle of 3222905_4 by 8 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.883 | MS1 | 121.4656696113 | 31.1446269217 | 742 | 504990 | -92.00 | 13.73 | 362.00 | 0.11 | 2.73 | 1578 |
| 2024-09-20 22:21:32.370 | MS1 | 121.4656600936 | 31.1446234521 | 742 | 504990 | -87.73 | 14.95 | 549.27 | 0.16 | 2.40 | 1576 |
| 2024-09-20 22:21:33.235 | MS1 | 121.4656734239 | 31.1446323619 | 742 | 504990 | -85.81 | 13.59 | 353.65 | 0.18 | 2.13 | 1573 |
| 2024-09-20 22:21:34.567 | MS1 | 121.4656702397 | 31.1446207546 | 742 | 504990 | -86.06 | 16.51 | 59.77 | 0.16 | 2.87 | 314 |
| 2024-09-20 22:21:35.675 | MS1 | 121.4656623030 | 31.1446302282 | 742 | 504990 | -87.74 | 12.14 | 62.85 | 0.01 | 2.05 | 339 |
| 2024-09-20 22:21:36.955 | MS1 | 121.4656686758 | 31.1446262490 | 742 | 504990 | -88.15 | 12.36 | 71.92 | 0.17 | 2.19 | 358 |
| 2024-09-20 22:21:37.495 | MS1 | 121.4656763957 | 31.1446243524 | 742 | 504990 | -93.92 | 12.15 | 79.91 | 0.10 | 2.28 | 456 |
| 2024-09-20 22:21:38.101 | MS1 | 121.4656721049 | 31.1446323611 | 742 | 504990 | -92.52 | 12.08 | 98.79 | 0.04 | 2.10 | 468 |
| 2024-09-20 22:21:39.772 | MS1 | 121.4656581458 | 31.1446341180 | 742 | 504990 | -90.97 | 10.60 | 64.50 | 0.06 | 2.23 | 445 |
| 2024-09-20 22:21:40.596 | MS1 | 121.4656606965 | 31.1446196671 | 742 | 504990 | -90.24 | 8.09 | 412.32 | 0.19 | 2.84 | 1582 |
| 2024-09-20 22:21:41.530 | MS1 | 121.4656766514 | 31.1446292646 | 742 | 504990 | -93.83 | 7.75 | 593.75 | 0.12 | 2.76 | 1596 |
| 2024-09-20 22:21:42.187 | MS1 | 121.4656617574 | 31.1446360381 | 742 | 504990 | -90.92 | 11.65 | 417.30 | 0.11 | 2.63 | 1563 |

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
| 3214347 | 2 | 121.4747909797 | 31.1506148912 | 216 | 3 | 11 | 23.0 | TDD | 636 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3222905 | 4 | 121.4753234474 | 31.1517400901 | 327 | 7 | 0 | 16.6 | TDD | 742 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3275805 | 1 | 121.4658326580 | 31.1554473889 | 327 | 5 | 9 | 49.5 | TDD | 498 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3277614 | 3 | 121.4654860433 | 31.1472278613 | 261 | 4 | 5 | 24.1 | TDD | 357 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.801 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.825 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.939 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.939 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.674 | NREventA3 | measId:2;ServCellPCI:783;Se... |
| 2024-09-20 22:21:37.914 | NRHandoverAttempt | SourcePCI:783;SourceNR-ARFC... |
| 2024-09-20 22:21:37.947 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.957 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.071 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.071 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275805 | 1 | 15.5058 | 5.3689 | -117.3799 | 10.0169 | 87.0335 | 0.0077 | 0.0075 |
| 2024_09_20 22:00 | 3214347 | 2 | 14.6311 | 5.0214 | -114.2139 | 10.1274 | 87.0252 | 0.0071 | 0.0009 |
| 2024_09_20 22:00 | 3277614 | 3 | 14.1935 | 15.9229 | -115.0892 | 13.9372 | 100.3238 | 0.0079 | 0.0017 |
| 2024_09_20 22:00 | 3222905 | 4 | 5.8471 | 6.3890 | -114.5882 | 16.7732 | 84.2932 | 0.0157 | 0.0021 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414329_A614AADE | 504990 | 742 | -87.8 | 504990 | 357 | -89.2 | 504990 | 636 | -101.8 | 504990 | 498 |
| MR_1774414329_2336FB97 | 504990 | 742 | -87.2 | 504990 | 357 | -91.3 | 504990 | 636 | -99.8 | 504990 | 498 |
| MR_1774414329_91926615 | 504990 | 742 | -88.0 | 504990 | 357 | -88.7 | 504990 | 636 | -99.0 | 504990 | 498 |
| MR_1774414329_DBDCDB0D | 504990 | 742 | -87.7 | 504990 | 357 | -91.2 | 504990 | 636 | -101.1 | 504990 | 498 |
| MR_1774414329_86735E97 | 504990 | 742 | -86.6 | 504990 | 357 | -89.6 | 504990 | 636 | -101.1 | 504990 | 498 |
| MR_1774414329_F51F4EB2 | 504990 | 742 | -87.3 | 504990 | 357 | -91.3 | 504990 | 636 | -102.2 | 504990 | 498 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1535: `ae2c8d0a-a3f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ae2c8d0a-a3fb-4d0c-96dc-870726efcac0` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Lift the tilt angle  of 3235525_3 by 8 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1535] topology](images/train_1535.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3273186_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233122_1
- `C3`: Decrease A3 Offset threshold for 3233122_1
- `C4`: Add neighbor relationship between 3235525_3 and 3273186_2
- `C5`: Lift the tilt angle of 3233122_1 by 4 degrees
- `C6`: Press down the tilt angle of 3233122_1 by 4 degrees
- `C7`: Increase transmission power for 3233122_1
- `C8`: Adjust the azimuth of 3235525_3 by 18 degrees
- `C9`: Press down the tilt angle  of 3235525_3 by 8 degrees
- `C10`: Check test server and transmission issues
- `C11`: Increase transmission power for 3273186_2
- `C12`: Increase A3 Offset threshold for 3273186_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273186_2
- `C14`: Add neighbor relationship between 3233122_1 and 3273186_2
- `C15`: Adjust the azimuth of 3233122_1 by 17 degrees
- `C16`: Decrease A3 Offset threshold for 3273186_2
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Lift the tilt angle  of 3235525_3 by 8 degrees **← 정답**
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233122_1
- `C20`: Increase A3 Offset threshold for 3233122_1
- `C21`: Decrease transmission power for 3233122_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273186_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.349 | MS1 | 121.4656651709 | 31.1446240573 | 856 | 504990 | -85.27 | 17.43 | 380.08 | 0.18 | 2.44 | 1593 |
| 2024-09-20 22:21:32.960 | MS1 | 121.4656647185 | 31.1446277746 | 856 | 504990 | -88.52 | 17.54 | 301.60 | 0.04 | 2.35 | 1587 |
| 2024-09-20 22:21:33.482 | MS1 | 121.4656695567 | 31.1446337088 | 856 | 504990 | -88.96 | 17.23 | 501.28 | 0.05 | 2.69 | 1588 |
| 2024-09-20 22:21:34.638 | MS1 | 121.4656664133 | 31.1446218736 | 856 | 504990 | -91.26 | 15.08 | 72.37 | 0.04 | 2.17 | 1589 |
| 2024-09-20 22:21:35.694 | MS1 | 121.4656657701 | 31.1446256046 | 856 | 504990 | -90.12 | 14.30 | 59.50 | 0.08 | 2.79 | 1588 |
| 2024-09-20 22:21:36.432 | MS1 | 121.4656765104 | 31.1446285810 | 856 | 504990 | -85.92 | 12.12 | 56.31 | 0.12 | 2.83 | 1592 |
| 2024-09-20 22:21:37.426 | MS1 | 121.4656610188 | 31.1446251040 | 856 | 504990 | -89.46 | 11.57 | 76.32 | 0.00 | 2.31 | 1561 |
| 2024-09-20 22:21:38.363 | MS1 | 121.4656589028 | 31.1446349694 | 856 | 504990 | -90.46 | 12.47 | 57.97 | 0.17 | 2.13 | 1600 |
| 2024-09-20 22:21:39.646 | MS1 | 121.4656597313 | 31.1446334631 | 856 | 504990 | -92.69 | 11.43 | 94.54 | 0.11 | 2.22 | 1564 |
| 2024-09-20 22:21:40.973 | MS1 | 121.4656606600 | 31.1446228633 | 856 | 504990 | -89.81 | 11.56 | 494.95 | 0.03 | 2.59 | 1569 |
| 2024-09-20 22:21:41.521 | MS1 | 121.4656583770 | 31.1446188664 | 856 | 504990 | -92.31 | 9.48 | 421.90 | 0.02 | 2.67 | 1592 |
| 2024-09-20 22:21:42.833 | MS1 | 121.4656688512 | 31.1446268870 | 856 | 504990 | -92.70 | 10.37 | 516.58 | 0.14 | 2.69 | 1566 |

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
| 3233122 | 1 | 121.4756098279 | 31.1520301009 | 212 | 3 | 11 | 15.5 | TDD | 856 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3235525 | 3 | 121.4672438246 | 31.1521880593 | 343 | 4 | 0 | 44.4 | TDD | 85 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3243262 | 4 | 121.4650841563 | 31.1458161453 | 253 | 14 | 1 | 24.7 | TDD | 941 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3273186 | 2 | 121.4690573303 | 31.1440402402 | 263 | 4 | 7 | 22.3 | TDD | 738 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.523 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.542 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.647 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.647 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.412 | NREventA3 | measId:2;ServCellPCI:419;Se... |
| 2024-09-20 22:21:38.652 | NRHandoverAttempt | SourcePCI:419;SourceNR-ARFC... |
| 2024-09-20 22:21:38.693 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.707 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.836 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.836 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233122 | 1 | 75.5817 | 75.2195 | -114.4340 | 10.4095 | 142.0180 | 0.0157 | 0.0165 |
| 2024_09_20 22:00 | 3273186 | 2 | 14.4576 | 9.3899 | -114.1774 | 7.1084 | 83.3335 | 0.0133 | 0.0164 |
| 2024_09_20 22:00 | 3235525 | 3 | 6.3058 | 7.2887 | -115.7659 | 11.7211 | 95.7520 | 0.0050 | 0.0120 |
| 2024_09_20 22:00 | 3243262 | 4 | 10.5585 | 12.8186 | -117.3699 | 18.5138 | 139.2808 | 0.0194 | 0.0189 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413478_743C583D | 504990 | 856 | -93.1 | 504990 | 738 | -91.5 | 504990 | 85 | -105.5 | 504990 | 941 |
| MR_1774413478_EEFCC0C6 | 504990 | 856 | -92.3 | 504990 | 738 | -91.0 | 504990 | 85 | -105.4 | 504990 | 941 |
| MR_1774413478_50D90E86 | 504990 | 856 | -92.4 | 504990 | 738 | -93.3 | 504990 | 85 | -104.6 | 504990 | 941 |
| MR_1774413478_D57A7244 | 504990 | 856 | -90.1 | 504990 | 738 | -94.6 | 504990 | 85 | -103.8 | 504990 | 941 |
| MR_1774413478_DFACD383 | 504990 | 856 | -91.6 | 504990 | 738 | -91.8 | 504990 | 85 | -106.1 | 504990 | 941 |
| MR_1774413478_E49B24B9 | 504990 | 856 | -91.5 | 504990 | 738 | -92.3 | 504990 | 85 | -104.0 | 504990 | 941 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1536: `64195173-b95...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `64195173-b954-4330-a3b9-d5eb354a596c` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Add neighbor relationship between 3253534_2 and 3243123_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1536] topology](images/train_1536.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Lift the tilt angle of 3253534_2 by 10 degrees
- `C3`: Increase A3 Offset threshold for 3243123_4
- `C4`: Check test server and transmission issues
- `C5`: Increase A3 Offset threshold for 3253534_2
- `C6`: Decrease transmission power for 3253534_2
- `C7`: Increase transmission power for 3243123_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243123_4
- `C9`: Press down the tilt angle  of 3243123_4 by 1 degrees
- `C10`: Lift the tilt angle  of 3243123_4 by 1 degrees
- `C11`: Decrease transmission power for 3243123_4
- `C12`: Decrease A3 Offset threshold for 3253534_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253534_2
- `C14`: Adjust the azimuth of 3243123_4 by 33 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243123_4
- `C16`: Adjust the azimuth of 3253534_2 by 50 degrees
- `C17`: Add neighbor relationship between 3257147_1 and 3243123_4
- `C18`: Increase transmission power for 3253534_2
- `C19`: Add neighbor relationship between 3253534_2 and 3243123_4 **← 정답**
- `C20`: Press down the tilt angle of 3253534_2 by 10 degrees
- `C21`: Decrease A3 Offset threshold for 3243123_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253534_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.873 | MS1 | 121.4656599033 | 31.1446309979 | 428 | 504990 | -76.05 | 12.06 | 561.54 | 0.14 | 2.16 | 1574 |
| 2024-09-20 22:21:32.977 | MS1 | 121.4656699167 | 31.1446210141 | 428 | 504990 | -84.39 | 13.03 | 436.87 | 0.00 | 2.35 | 1594 |
| 2024-09-20 22:21:33.161 | MS1 | 121.4656644145 | 31.1446243390 | 428 | 504990 | -83.03 | 12.07 | 497.11 | 0.18 | 2.52 | 1561 |
| 2024-09-20 22:21:34.782 | MS1 | 121.4656693170 | 31.1446218752 | 428 | 504990 | -85.42 | -2.14 | 44.97 | 0.16 | 1.33 | 1568 |
| 2024-09-20 22:21:35.111 | MS1 | 121.4656653946 | 31.1446206042 | 428 | 504990 | -86.72 | -0.40 | 53.47 | 0.05 | 1.22 | 1575 |
| 2024-09-20 22:21:36.498 | MS1 | 121.4656708895 | 31.1446306899 | 428 | 504990 | -85.78 | -1.61 | 45.68 | 0.08 | 1.42 | 1560 |
| 2024-09-20 22:21:37.450 | MS1 | 121.4656690395 | 31.1446215952 | 428 | 504990 | -89.44 | -1.43 | 32.75 | 0.17 | 1.07 | 1579 |
| 2024-09-20 22:21:38.540 | MS1 | 121.4656727493 | 31.1446204221 | 428 | 504990 | -83.60 | 14.42 | 502.22 | 0.04 | 1.01 | 1576 |
| 2024-09-20 22:21:39.160 | MS1 | 121.4656602108 | 31.1446323810 | 428 | 504990 | -84.32 | 13.40 | 503.35 | 0.12 | 1.15 | 1567 |
| 2024-09-20 22:21:40.631 | MS1 | 121.4656632565 | 31.1446206567 | 428 | 504990 | -82.35 | 16.84 | 451.62 | 0.06 | 2.25 | 1588 |
| 2024-09-20 22:21:41.500 | MS1 | 121.4656681890 | 31.1446187035 | 428 | 504990 | -78.31 | 14.68 | 498.19 | 0.18 | 2.05 | 1571 |
| 2024-09-20 22:21:42.519 | MS1 | 121.4656605404 | 31.1446276207 | 428 | 504990 | -81.09 | 13.09 | 361.67 | 0.03 | 2.73 | 1600 |

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
| 3243123 | 4 | 121.4677039975 | 31.1547372861 | 223 | 0 | 2 | 16.9 | TDD | 774 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3253534 | 2 | 121.4731576613 | 31.1533679380 | 283 | 14 | 9 | 33.8 | TDD | 428 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3257147 | 1 | 121.4736930752 | 31.1541223463 | 257 | 10 | 5 | 46.8 | TDD | 752 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3276723 | 3 | 121.4657281130 | 31.1558848068 | 301 | 10 | 8 | 40.6 | TDD | 853 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.262 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.282 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.430 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.430 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.132 | NREventA3 | measId:2;ServCellPCI:721;Se... |
| 2024-09-20 22:21:36.132 | NREventA3 | measId:2;ServCellPCI:721;Se... |
| 2024-09-20 22:21:37.132 | NREventA3 | measId:2;ServCellPCI:721;Se... |
| 2024-09-20 22:21:39.632 | NRRRCReestablishAttempt | PCI:721 |
| 2024-09-20 22:21:39.652 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.665 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.807 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.807 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257147 | 1 | 14.6441 | 19.1316 | -116.8362 | 10.8410 | 120.1828 | 0.0116 | 0.0095 |
| 2024_09_20 22:00 | 3253534 | 2 | 11.2925 | 16.0428 | -116.3119 | 6.6912 | 150.6014 | 0.0062 | 0.1814 |
| 2024_09_20 22:00 | 3276723 | 3 | 10.7182 | 6.4473 | -117.1886 | 15.1367 | 119.0810 | 0.0070 | 0.0106 |
| 2024_09_20 22:00 | 3243123 | 4 | 6.5778 | 16.6079 | -114.8529 | 15.9905 | 161.8393 | 0.0083 | 0.0062 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416769_BAD4D2B8 | 504990 | 774 | -80.9 | 504990 | 428 | -83.8 | 504990 | 752 | -88.2 | 504990 | 853 |
| MR_1774416769_63DE8E36 | 504990 | 428 | -85.9 | 504990 | 774 | -81.1 | 504990 | 752 | -88.9 | 504990 | 853 |
| MR_1774416769_A0D17514 | 504990 | 774 | -78.2 | 504990 | 428 | -84.5 | 504990 | 752 | -89.5 | 504990 | 853 |
| MR_1774416769_3F310EFE | 504990 | 428 | -85.2 | 504990 | 774 | -77.6 | 504990 | 752 | -89.7 | 504990 | 853 |
| MR_1774416769_B0D78614 | 504990 | 428 | -86.7 | 504990 | 774 | -78.2 | 504990 | 752 | -89.1 | 504990 | 853 |
| MR_1774416769_3161BBC6 | 504990 | 428 | -84.7 | 504990 | 774 | -79.9 | 504990 | 752 | -89.3 | 504990 | 853 |
| MR_1774416769_1F761EB2 | 504990 | 774 | -79.9 | 504990 | 428 | -85.6 | 504990 | 752 | -89.5 | 504990 | 853 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1537: `3684dd34-38b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3684dd34-38ba-48d5-9965-f35e43b0f7f7` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3276384_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1537] topology](images/train_1537.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3251144_3 and 3229468_4
- `C2`: Decrease A3 Offset threshold for 3276384_1
- `C3`: Press down the tilt angle  of 3229468_4 by 3 degrees
- `C4`: Add neighbor relationship between 3276384_1 and 3229468_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229468_4
- `C6`: Increase transmission power for 3276384_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229468_4
- `C8`: Lift the tilt angle of 3276384_1 by 5 degrees
- `C9`: Increase A3 Offset threshold for 3229468_4
- `C10`: Increase A3 Offset threshold for 3276384_1
- `C11`: Decrease transmission power for 3276384_1
- `C12`: Increase transmission power for 3229468_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276384_1
- `C14`: Check test server and transmission issues
- `C15`: Lift the tilt angle  of 3229468_4 by 3 degrees
- `C16`: Press down the tilt angle of 3276384_1 by 5 degrees
- `C17`: Adjust the azimuth of 3229468_4 by 50 degrees
- `C18`: Decrease A3 Offset threshold for 3229468_4
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease transmission power for 3229468_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276384_1 **← 정답**
- `C22`: Adjust the azimuth of 3276384_1 by 19 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.792 | MS1 | 121.4656620911 | 31.1446255978 | 857 | 504990 | -86.37 | 15.38 | 351.37 | 0.01 | 2.96 | 1573 |
| 2024-09-20 22:21:32.651 | MS1 | 121.4656743779 | 31.1446293637 | 857 | 504990 | -90.86 | 15.60 | 293.17 | 0.17 | 2.30 | 1589 |
| 2024-09-20 22:21:33.575 | MS1 | 121.4656632912 | 31.1446247504 | 857 | 504990 | -87.77 | 12.20 | 425.48 | 0.02 | 2.57 | 1579 |
| 2024-09-20 22:21:34.858 | MS1 | 121.4656599597 | 31.1446332150 | 857 | 504990 | -85.41 | 12.08 | 70.49 | 0.61 | 2.32 | 525 |
| 2024-09-20 22:21:35.127 | MS1 | 121.4656618653 | 31.1446294634 | 857 | 504990 | -91.52 | 13.18 | 77.21 | 0.67 | 2.77 | 512 |
| 2024-09-20 22:21:36.939 | MS1 | 121.4656731031 | 31.1446219639 | 857 | 504990 | -91.62 | 13.25 | 88.91 | 0.57 | 2.50 | 660 |
| 2024-09-20 22:21:37.177 | MS1 | 121.4656602968 | 31.1446331377 | 857 | 504990 | -91.94 | 7.25 | 64.08 | 0.58 | 2.52 | 558 |
| 2024-09-20 22:21:38.990 | MS1 | 121.4656629553 | 31.1446356485 | 857 | 504990 | -89.99 | 7.77 | 78.20 | 0.64 | 2.77 | 606 |
| 2024-09-20 22:21:39.319 | MS1 | 121.4656605244 | 31.1446366102 | 857 | 504990 | -92.83 | 7.56 | 91.62 | 0.58 | 2.77 | 633 |
| 2024-09-20 22:21:40.522 | MS1 | 121.4656701471 | 31.1446357556 | 857 | 504990 | -91.01 | 7.93 | 311.64 | 0.16 | 2.39 | 1564 |
| 2024-09-20 22:21:41.393 | MS1 | 121.4656743516 | 31.1446243780 | 857 | 504990 | -93.71 | 10.59 | 321.50 | 0.09 | 2.84 | 1590 |
| 2024-09-20 22:21:42.981 | MS1 | 121.4656611822 | 31.1446189873 | 857 | 504990 | -91.35 | 12.26 | 481.12 | 0.14 | 2.80 | 1588 |

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
| 3229468 | 4 | 121.4696728293 | 31.1486736252 | 18 | 0 | 6 | 34.0 | TDD | 157 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3245073 | 2 | 121.4704286247 | 31.1449860590 | 93 | 7 | 12 | 25.0 | TDD | 394 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3251144 | 3 | 121.4738607806 | 31.1457862603 | 334 | 0 | 9 | 15.3 | TDD | 201 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3276384 | 1 | 121.4705712692 | 31.1460780456 | 232 | 0 | 4 | 42.7 | TDD | 857 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.567 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.671 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.671 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.368 | NREventA3 | measId:2;ServCellPCI:303;Se... |
| 2024-09-20 22:21:38.608 | NRHandoverAttempt | SourcePCI:303;SourceNR-ARFC... |
| 2024-09-20 22:21:38.646 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.656 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.769 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.769 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276384 | 1 | 11.9389 | 11.9139 | -117.1385 | 19.5784 | 124.3206 | 0.0039 | 0.0069 |
| 2024_09_20 22:00 | 3245073 | 2 | 6.8550 | 7.9690 | -117.3125 | 10.3315 | 196.2067 | 0.0188 | 0.0160 |
| 2024_09_20 22:00 | 3251144 | 3 | 13.4607 | 8.0922 | -114.6997 | 7.5487 | 173.1213 | 0.0098 | 0.0112 |
| 2024_09_20 22:00 | 3229468 | 4 | 19.0846 | 14.3754 | -117.0677 | 8.4454 | 143.5625 | 0.0052 | 0.0143 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414067_B4C510EC | 504990 | 857 | -86.4 | 504990 | 157 | -91.7 | 504990 | 201 | -98.0 | 504990 | 394 |
| MR_1774414067_85B23BFD | 504990 | 857 | -87.1 | 504990 | 157 | -90.6 | 504990 | 201 | -97.6 | 504990 | 394 |
| MR_1774414067_AB91BDAD | 504990 | 857 | -86.1 | 504990 | 157 | -88.6 | 504990 | 201 | -94.6 | 504990 | 394 |
| MR_1774414067_CCFE8569 | 504990 | 857 | -84.8 | 504990 | 157 | -89.9 | 504990 | 201 | -97.1 | 504990 | 394 |
| MR_1774414067_977DD337 | 504990 | 857 | -85.2 | 504990 | 157 | -89.3 | 504990 | 201 | -95.9 | 504990 | 394 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1538: `113294c7-9af...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `113294c7-9afe-4062-8dd1-de00407b1721` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1538] topology](images/train_1538.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3228473_2
- `C2`: Press down the tilt angle  of 3228473_2 by 6 degrees
- `C3`: Press down the tilt angle of 3275158_3 by 10 degrees
- `C4`: Increase A3 Offset threshold for 3228473_2
- `C5`: Add neighbor relationship between 3275158_3 and 3228473_2
- `C6`: Lift the tilt angle  of 3228473_2 by 6 degrees
- `C7`: Decrease transmission power for 3275158_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275158_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275158_3
- `C10`: Increase transmission power for 3228473_2
- `C11`: Adjust the azimuth of 3275158_3 by 50 degrees
- `C12`: Lift the tilt angle of 3275158_3 by 10 degrees
- `C13`: Add neighbor relationship between 3210714_1 and 3228473_2
- `C14`: Check test server and transmission issues **← 정답**
- `C15`: Decrease A3 Offset threshold for 3275158_3
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228473_2
- `C18`: Decrease A3 Offset threshold for 3228473_2
- `C19`: Increase A3 Offset threshold for 3275158_3
- `C20`: Increase transmission power for 3275158_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228473_2
- `C22`: Adjust the azimuth of 3228473_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.539 | MS1 | 121.4656770459 | 31.1446341790 | 791 | 504990 | -88.26 | 12.43 | 477.85 | 0.07 | 2.55 | 1561 |
| 2024-09-20 22:21:32.961 | MS1 | 121.4656585707 | 31.1446343039 | 791 | 504990 | -90.23 | 12.95 | 449.86 | 0.11 | 2.26 | 1585 |
| 2024-09-20 22:21:33.722 | MS1 | 121.4656764374 | 31.1446229437 | 791 | 504990 | -89.30 | 16.78 | 383.69 | 0.07 | 2.53 | 1584 |
| 2024-09-20 22:21:34.931 | MS1 | 121.4656629432 | 31.1446298102 | 791 | 504990 | -90.74 | 17.67 | 92.35 | 0.05 | 2.12 | 300 |
| 2024-09-20 22:21:35.664 | MS1 | 121.4656650380 | 31.1446266229 | 791 | 504990 | -90.11 | 15.82 | 67.28 | 0.17 | 2.89 | 366 |
| 2024-09-20 22:21:36.544 | MS1 | 121.4656663640 | 31.1446222206 | 791 | 504990 | -91.94 | 15.26 | 71.44 | 0.19 | 2.15 | 344 |
| 2024-09-20 22:21:37.344 | MS1 | 121.4656594822 | 31.1446240427 | 791 | 504990 | -92.78 | 9.65 | 72.48 | 0.16 | 2.89 | 491 |
| 2024-09-20 22:21:38.383 | MS1 | 121.4656611384 | 31.1446299635 | 791 | 504990 | -90.08 | 8.41 | 71.98 | 0.17 | 2.64 | 366 |
| 2024-09-20 22:21:39.850 | MS1 | 121.4656757444 | 31.1446255664 | 791 | 504990 | -90.94 | 11.84 | 57.30 | 0.15 | 2.73 | 448 |
| 2024-09-20 22:21:40.862 | MS1 | 121.4656729434 | 31.1446294267 | 791 | 504990 | -90.17 | 9.70 | 438.16 | 0.16 | 2.71 | 1560 |
| 2024-09-20 22:21:41.713 | MS1 | 121.4656714966 | 31.1446230287 | 791 | 504990 | -93.28 | 7.58 | 569.66 | 0.12 | 2.86 | 1595 |
| 2024-09-20 22:21:42.768 | MS1 | 121.4656627675 | 31.1446255673 | 791 | 504990 | -93.91 | 7.15 | 316.22 | 0.05 | 2.38 | 1586 |

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
| 3210714 | 1 | 121.4708354596 | 31.1461341432 | 288 | 9 | 5 | 44.7 | TDD | 808 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3228473 | 2 | 121.4678437038 | 31.1464777994 | 95 | 2 | 0 | 19.0 | TDD | 755 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3240075 | 4 | 121.4726565547 | 31.1463568638 | 281 | 15 | 7 | 40.6 | TDD | 479 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3275158 | 3 | 121.4641905606 | 31.1505161410 | 244 | 13 | 5 | 16.1 | TDD | 791 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.865 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.883 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.017 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.017 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.744 | NREventA3 | measId:2;ServCellPCI:420;Se... |
| 2024-09-20 22:21:37.984 | NRHandoverAttempt | SourcePCI:420;SourceNR-ARFC... |
| 2024-09-20 22:21:38.034 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.044 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.191 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.191 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210714 | 1 | 17.8142 | 11.5775 | -116.8924 | 8.3049 | 112.7624 | 0.0134 | 0.0168 |
| 2024_09_20 22:00 | 3228473 | 2 | 9.4948 | 14.6247 | -117.6069 | 15.8281 | 199.0574 | 0.0036 | 0.0111 |
| 2024_09_20 22:00 | 3275158 | 3 | 11.2646 | 11.7400 | -117.0638 | 18.4372 | 175.4192 | 0.0175 | 0.0073 |
| 2024_09_20 22:00 | 3240075 | 4 | 7.8744 | 8.8432 | -116.9918 | 12.7401 | 113.3428 | 0.0058 | 0.0196 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417134_822ACC7E | 504990 | 791 | -91.2 | 504990 | 755 | -99.3 | 504990 | 808 | -100.4 | 504990 | 479 |
| MR_1774417134_511CE7F3 | 504990 | 791 | -92.0 | 504990 | 755 | -101.3 | 504990 | 808 | -99.4 | 504990 | 479 |
| MR_1774417134_A0E5B02C | 504990 | 791 | -90.3 | 504990 | 755 | -99.9 | 504990 | 808 | -101.0 | 504990 | 479 |
| MR_1774417134_A1A0CC2A | 504990 | 791 | -91.0 | 504990 | 755 | -100.7 | 504990 | 808 | -99.7 | 504990 | 479 |
| MR_1774417134_0F7FE07D | 504990 | 791 | -91.2 | 504990 | 755 | -101.2 | 504990 | 808 | -98.4 | 504990 | 479 |
| MR_1774417134_7730C5AD | 504990 | 791 | -91.8 | 504990 | 755 | -99.5 | 504990 | 808 | -98.4 | 504990 | 479 |
| MR_1774417134_18A33838 | 504990 | 791 | -91.9 | 504990 | 755 | -100.4 | 504990 | 808 | -97.9 | 504990 | 479 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1539: `ea9a5cbe-b24...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ea9a5cbe-b24a-4be4-a8da-3dc2abaa51f1` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Add neighbor relationship between 3276921_1 and 3268922_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1539] topology](images/train_1539.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3268922_2 by 1 degrees
- `C2`: Increase A3 Offset threshold for 3268922_2
- `C3`: Add neighbor relationship between 3218331_4 and 3268922_2
- `C4`: Adjust the azimuth of 3276921_1 by 50 degrees
- `C5`: Increase transmission power for 3268922_2
- `C6`: Lift the tilt angle of 3276921_1 by 10 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268922_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276921_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276921_1
- `C10`: Decrease A3 Offset threshold for 3276921_1
- `C11`: Increase A3 Offset threshold for 3276921_1
- `C12`: Decrease transmission power for 3276921_1
- `C13`: Check test server and transmission issues
- `C14`: Decrease transmission power for 3268922_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268922_2
- `C16`: Adjust the azimuth of 3268922_2 by 6 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease A3 Offset threshold for 3268922_2
- `C19`: Add neighbor relationship between 3276921_1 and 3268922_2 **← 정답**
- `C20`: Press down the tilt angle of 3276921_1 by 10 degrees
- `C21`: Press down the tilt angle  of 3268922_2 by 1 degrees
- `C22`: Increase transmission power for 3276921_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.421 | MS1 | 121.4656623239 | 31.1446204456 | 793 | 504990 | -82.91 | 14.53 | 386.12 | 0.16 | 2.03 | 1589 |
| 2024-09-20 22:21:32.649 | MS1 | 121.4656730724 | 31.1446233082 | 793 | 504990 | -76.65 | 16.33 | 395.83 | 0.06 | 2.96 | 1576 |
| 2024-09-20 22:21:33.796 | MS1 | 121.4656650681 | 31.1446218655 | 793 | 504990 | -83.91 | 12.23 | 521.07 | 0.04 | 2.08 | 1592 |
| 2024-09-20 22:21:34.450 | MS1 | 121.4656688838 | 31.1446300996 | 793 | 504990 | -88.63 | -1.02 | 31.05 | 0.12 | 1.13 | 1570 |
| 2024-09-20 22:21:35.794 | MS1 | 121.4656613830 | 31.1446229470 | 793 | 504990 | -94.56 | -3.57 | 23.95 | 0.13 | 1.30 | 1563 |
| 2024-09-20 22:21:36.912 | MS1 | 121.4656745718 | 31.1446260870 | 793 | 504990 | -88.98 | -1.61 | 68.76 | 0.18 | 1.17 | 1566 |
| 2024-09-20 22:21:37.386 | MS1 | 121.4656672237 | 31.1446277561 | 793 | 504990 | -85.51 | -3.13 | 38.12 | 0.11 | 1.10 | 1575 |
| 2024-09-20 22:21:38.339 | MS1 | 121.4656689719 | 31.1446371233 | 793 | 504990 | -84.43 | 16.54 | 469.83 | 0.17 | 1.04 | 1582 |
| 2024-09-20 22:21:39.546 | MS1 | 121.4656604564 | 31.1446275681 | 793 | 504990 | -78.31 | 14.99 | 320.33 | 0.09 | 1.29 | 1565 |
| 2024-09-20 22:21:40.496 | MS1 | 121.4656677056 | 31.1446212534 | 793 | 504990 | -80.64 | 17.39 | 368.29 | 0.16 | 2.71 | 1571 |
| 2024-09-20 22:21:41.588 | MS1 | 121.4656718323 | 31.1446317797 | 793 | 504990 | -77.75 | 13.13 | 513.16 | 0.13 | 2.47 | 1566 |
| 2024-09-20 22:21:42.996 | MS1 | 121.4656669368 | 31.1446205218 | 793 | 504990 | -80.00 | 12.68 | 461.55 | 0.11 | 2.18 | 1570 |

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
| 3216257 | 3 | 121.4701808454 | 31.1544487714 | 211 | 2 | 3 | 25.2 | TDD | 62 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3218331 | 4 | 121.4693907527 | 31.1544827140 | 325 | 6 | 3 | 45.4 | TDD | 607 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3268922 | 2 | 121.4683960051 | 31.1530676225 | 201 | 0 | 5 | 19.0 | TDD | 465 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3276921 | 1 | 121.4714929827 | 31.1490385742 | 127 | 6 | 4 | 49.9 | TDD | 793 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.571 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.589 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.700 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.700 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.378 | NREventA3 | measId:2;ServCellPCI:874;Se... |
| 2024-09-20 22:21:36.378 | NREventA3 | measId:2;ServCellPCI:874;Se... |
| 2024-09-20 22:21:37.378 | NREventA3 | measId:2;ServCellPCI:874;Se... |
| 2024-09-20 22:21:39.878 | NRRRCReestablishAttempt | PCI:874 |
| 2024-09-20 22:21:39.896 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.907 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:40.047 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.047 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276921 | 1 | 6.7876 | 17.2716 | -116.9442 | 5.1366 | 172.4898 | 0.0154 | 0.1794 |
| 2024_09_20 22:00 | 3268922 | 2 | 11.7233 | 18.5089 | -117.1672 | 9.0999 | 91.3953 | 0.0169 | 0.0132 |
| 2024_09_20 22:00 | 3216257 | 3 | 14.8327 | 5.5237 | -114.6827 | 5.8637 | 100.5115 | 0.0064 | 0.0102 |
| 2024_09_20 22:00 | 3218331 | 4 | 14.7643 | 15.2055 | -115.2272 | 13.8678 | 97.5056 | 0.0070 | 0.0009 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414684_08CD5B04 | 504990 | 793 | -89.1 | 504990 | 465 | -83.4 | 504990 | 607 | -86.2 | 504990 | 62 |
| MR_1774414684_4ABD1E02 | 504990 | 793 | -89.1 | 504990 | 465 | -82.2 | 504990 | 607 | -87.4 | 504990 | 62 |
| MR_1774414684_29F27B22 | 504990 | 793 | -88.7 | 504990 | 465 | -83.8 | 504990 | 607 | -85.9 | 504990 | 62 |
| MR_1774414684_7F38249B | 504990 | 465 | -85.2 | 504990 | 793 | -87.5 | 504990 | 607 | -87.4 | 504990 | 62 |
| MR_1774414684_AFF4715C | 504990 | 793 | -87.5 | 504990 | 465 | -82.6 | 504990 | 607 | -85.1 | 504990 | 62 |

> *... 2개 열 생략 (전체 14열)*

---
