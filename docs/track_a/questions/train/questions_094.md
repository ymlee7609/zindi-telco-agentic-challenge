# Track A 문제 분석 — train[930]~train[939]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[930] ~ train[939] (10개)

## 목차

1. [문제 930: `6c655b85-5a3...`](#930) — single-answer, 정답: C21
2. [문제 931: `5101ef0b-c4d...`](#931) — single-answer, 정답: C22
3. [문제 932: `ec469e7d-399...`](#932) — single-answer, 정답: C1
4. [문제 933: `f2162684-946...`](#933) — single-answer, 정답: C14
5. [문제 934: `dcb2aa41-07d...`](#934) — single-answer, 정답: C18
6. [문제 935: `86565522-722...`](#935) — single-answer, 정답: C21
7. [문제 936: `c5d69ae1-5ef...`](#936) — single-answer, 정답: C7
8. [문제 937: `1e46dba1-b49...`](#937) — single-answer, 정답: C14
9. [문제 938: `c96e6867-b4e...`](#938) — single-answer, 정답: C16
10. [문제 939: `0191f687-27d...`](#939) — single-answer, 정답: C13

---

### 문제 930: `6c655b85-5a3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6c655b85-5a36-4479-89d0-5bd8c74df5db` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease A3 Offset threshold for 3223009_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[930] topology](images/train_0930.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3231933_3 by 50 degrees
- `C2`: Lift the tilt angle of 3223009_1 by 10 degrees
- `C3`: Adjust the azimuth of 3223009_1 by 50 degrees
- `C4`: Add neighbor relationship between 3210437_2 and 3231933_3
- `C5`: Add neighbor relationship between 3223009_1 and 3231933_3
- `C6`: Increase A3 Offset threshold for 3231933_3
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Press down the tilt angle of 3223009_1 by 10 degrees
- `C9`: Increase transmission power for 3223009_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231933_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223009_1
- `C12`: Press down the tilt angle  of 3231933_3 by 2 degrees
- `C13`: Decrease transmission power for 3231933_3
- `C14`: Increase transmission power for 3231933_3
- `C15`: Decrease transmission power for 3223009_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231933_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223009_1
- `C18`: Check test server and transmission issues
- `C19`: Decrease A3 Offset threshold for 3231933_3
- `C20`: Increase A3 Offset threshold for 3223009_1
- `C21`: Decrease A3 Offset threshold for 3223009_1 **← 정답**
- `C22`: Lift the tilt angle  of 3231933_3 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.645 | MS1 | 121.4656702150 | 31.1446309166 | 571 | 504990 | -81.85 | 16.32 | 476.03 | 0.18 | 2.97 | 1596 |
| 2024-09-20 22:21:32.111 | MS1 | 121.4656744292 | 31.1446320175 | 571 | 504990 | -76.51 | 16.97 | 487.67 | 0.16 | 2.79 | 1598 |
| 2024-09-20 22:21:33.647 | MS1 | 121.4656591395 | 31.1446345774 | 571 | 504990 | -80.08 | 14.40 | 430.19 | 0.06 | 2.93 | 1577 |
| 2024-09-20 22:21:34.915 | MS1 | 121.4656756271 | 31.1446273686 | 571 | 504990 | -84.62 | -0.02 | 45.00 | 0.05 | 1.43 | 1591 |
| 2024-09-20 22:21:35.654 | MS1 | 121.4656594712 | 31.1446180092 | 571 | 504990 | -92.12 | -3.64 | 61.16 | 0.02 | 1.47 | 1581 |
| 2024-09-20 22:21:36.516 | MS1 | 121.4656673060 | 31.1446285467 | 571 | 504990 | -91.99 | -3.30 | 72.03 | 0.06 | 1.30 | 1570 |
| 2024-09-20 22:21:37.825 | MS1 | 121.4656631978 | 31.1446310298 | 571 | 504990 | -92.87 | -2.68 | 40.81 | 0.14 | 1.05 | 1599 |
| 2024-09-20 22:21:38.553 | MS1 | 121.4656600387 | 31.1446351493 | 571 | 504990 | -92.48 | -0.23 | 44.49 | 0.08 | 1.45 | 1566 |
| 2024-09-20 22:21:39.854 | MS1 | 121.4656593635 | 31.1446354612 | 893 | 504990 | -81.61 | 17.54 | 277.72 | 0.04 | 1.15 | 1567 |
| 2024-09-20 22:21:40.116 | MS1 | 121.4656755187 | 31.1446363544 | 893 | 504990 | -81.08 | 15.38 | 574.16 | 0.02 | 2.54 | 1562 |
| 2024-09-20 22:21:41.438 | MS1 | 121.4656693906 | 31.1446298790 | 893 | 504990 | -78.89 | 14.52 | 380.82 | 0.03 | 2.86 | 1600 |
| 2024-09-20 22:21:42.877 | MS1 | 121.4656709640 | 31.1446209929 | 893 | 504990 | -76.11 | 14.50 | 401.56 | 0.09 | 2.67 | 1580 |

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
| 3210437 | 2 | 121.4697244170 | 31.1555450330 | 300 | 15 | 7 | 19.4 | TDD | 127 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3223009 | 1 | 121.4687696217 | 31.1539943331 | 300 | 12 | 10 | 46.9 | TDD | 571 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3231933 | 3 | 121.4694104891 | 31.1487118893 | 290 | 0 | 3 | 23.7 | TDD | 893 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3239869 | 4 | 121.4675137166 | 31.1507650997 | 73 | 9 | 2 | 21.5 | TDD | 895 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.430 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.454 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.570 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.570 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.283 | NREventA3 | measId:2;ServCellPCI:23;Ser... |
| 2024-09-20 22:21:38.523 | NRHandoverAttempt | SourcePCI:23;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.554 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.565 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.695 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.695 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223009 | 1 | 18.8078 | 11.7324 | -114.6949 | 8.8230 | 99.6990 | 0.0015 | 0.1010 |
| 2024_09_20 22:00 | 3210437 | 2 | 6.9559 | 19.7243 | -115.6509 | 12.5832 | 95.0918 | 0.0199 | 0.0054 |
| 2024_09_20 22:00 | 3231933 | 3 | 16.2908 | 19.5071 | -116.0791 | 17.0832 | 154.6724 | 0.0169 | 0.0075 |
| 2024_09_20 22:00 | 3239869 | 4 | 13.5528 | 15.0711 | -114.4620 | 8.6067 | 93.0118 | 0.0195 | 0.0155 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412578_C16C57E6 | 504990 | 571 | -83.1 | 504990 | 893 | -77.6 | 504990 | 127 | -82.3 | 504990 | 895 |
| MR_1774412578_D78B4779 | 504990 | 893 | -79.6 | 504990 | 571 | -85.5 | 504990 | 127 | -78.7 | 504990 | 895 |
| MR_1774412578_E11640F2 | 504990 | 571 | -84.4 | 504990 | 893 | -81.3 | 504990 | 127 | -81.1 | 504990 | 895 |
| MR_1774412578_E0EABEF9 | 504990 | 571 | -84.6 | 504990 | 893 | -80.4 | 504990 | 127 | -80.9 | 504990 | 895 |
| MR_1774412578_08B1A59B | 504990 | 571 | -83.5 | 504990 | 893 | -81.0 | 504990 | 127 | -81.9 | 504990 | 895 |
| MR_1774412578_C18E5288 | 504990 | 571 | -83.2 | 504990 | 893 | -77.8 | 504990 | 127 | -81.2 | 504990 | 895 |
| MR_1774412578_C48D5FBB | 504990 | 571 | -83.5 | 504990 | 893 | -80.4 | 504990 | 127 | -82.1 | 504990 | 895 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 931: `5101ef0b-c4d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5101ef0b-c4dd-4ce8-9815-4af3c720e965` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Add neighbor relationship between 3272311_1 and 3267891_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[931] topology](images/train_0931.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3256109_3 and 3267891_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272311_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Press down the tilt angle of 3272311_1 by 3 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267891_2
- `C6`: Adjust the azimuth of 3272311_1 by 50 degrees
- `C7`: Increase transmission power for 3267891_2
- `C8`: Increase A3 Offset threshold for 3267891_2
- `C9`: Lift the tilt angle  of 3267891_2 by 4 degrees
- `C10`: Decrease transmission power for 3272311_1
- `C11`: Decrease A3 Offset threshold for 3272311_1
- `C12`: Decrease transmission power for 3267891_2
- `C13`: Decrease A3 Offset threshold for 3267891_2
- `C14`: Adjust the azimuth of 3267891_2 by 46 degrees
- `C15`: Lift the tilt angle of 3272311_1 by 3 degrees
- `C16`: Press down the tilt angle  of 3267891_2 by 4 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272311_1
- `C18`: Increase transmission power for 3272311_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267891_2
- `C20`: Check test server and transmission issues
- `C21`: Increase A3 Offset threshold for 3272311_1
- `C22`: Add neighbor relationship between 3272311_1 and 3267891_2 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.791 | MS1 | 121.4656728593 | 31.1446198635 | 632 | 504990 | -77.02 | 16.47 | 421.75 | 0.02 | 2.62 | 1576 |
| 2024-09-20 22:21:32.929 | MS1 | 121.4656767362 | 31.1446192152 | 632 | 504990 | -79.29 | 12.10 | 480.97 | 0.09 | 2.88 | 1570 |
| 2024-09-20 22:21:33.585 | MS1 | 121.4656691674 | 31.1446364411 | 632 | 504990 | -83.93 | 15.45 | 581.81 | 0.12 | 2.72 | 1573 |
| 2024-09-20 22:21:34.948 | MS1 | 121.4656621345 | 31.1446269109 | 632 | 504990 | -86.99 | -0.92 | 71.30 | 0.16 | 1.29 | 1573 |
| 2024-09-20 22:21:35.611 | MS1 | 121.4656685218 | 31.1446280065 | 632 | 504990 | -90.62 | -1.34 | 60.88 | 0.08 | 1.17 | 1596 |
| 2024-09-20 22:21:36.384 | MS1 | 121.4656643409 | 31.1446334062 | 632 | 504990 | -86.68 | -3.64 | 57.50 | 0.02 | 1.45 | 1598 |
| 2024-09-20 22:21:37.969 | MS1 | 121.4656665633 | 31.1446214091 | 632 | 504990 | -92.71 | -0.52 | 60.20 | 0.10 | 1.26 | 1596 |
| 2024-09-20 22:21:38.923 | MS1 | 121.4656760402 | 31.1446374111 | 632 | 504990 | -79.82 | 17.26 | 524.37 | 0.08 | 1.07 | 1580 |
| 2024-09-20 22:21:39.234 | MS1 | 121.4656588815 | 31.1446247346 | 632 | 504990 | -79.49 | 16.90 | 375.28 | 0.05 | 1.47 | 1563 |
| 2024-09-20 22:21:40.846 | MS1 | 121.4656589484 | 31.1446196777 | 632 | 504990 | -82.52 | 17.69 | 332.42 | 0.14 | 2.54 | 1585 |
| 2024-09-20 22:21:41.585 | MS1 | 121.4656658017 | 31.1446283569 | 632 | 504990 | -84.04 | 13.53 | 516.77 | 0.03 | 2.65 | 1596 |
| 2024-09-20 22:21:42.318 | MS1 | 121.4656706051 | 31.1446185960 | 632 | 504990 | -83.37 | 15.94 | 510.92 | 0.12 | 2.16 | 1592 |

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
| 3245637 | 4 | 121.4670208582 | 31.1536254470 | 74 | 10 | 0 | 31.0 | TDD | 927 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3256109 | 3 | 121.4717325033 | 31.1545573727 | 16 | 5 | 9 | 49.4 | TDD | 149 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3267891 | 2 | 121.4741658984 | 31.1503515801 | 278 | 2 | 4 | 39.9 | TDD | 212 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3272311 | 1 | 121.4704625764 | 31.1479494378 | 298 | 1 | 1 | 15.4 | TDD | 632 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.591 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.613 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.726 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.726 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.457 | NREventA3 | measId:2;ServCellPCI:268;Se... |
| 2024-09-20 22:21:36.457 | NREventA3 | measId:2;ServCellPCI:268;Se... |
| 2024-09-20 22:21:37.457 | NREventA3 | measId:2;ServCellPCI:268;Se... |
| 2024-09-20 22:21:39.957 | NRRRCReestablishAttempt | PCI:268 |
| 2024-09-20 22:21:39.967 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.980 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:40.125 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.125 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272311 | 1 | 9.5081 | 18.4375 | -114.3463 | 6.4731 | 137.5773 | 0.0031 | 0.1071 |
| 2024_09_20 22:00 | 3267891 | 2 | 10.9761 | 11.8013 | -115.7805 | 16.9757 | 127.5836 | 0.0056 | 0.0012 |
| 2024_09_20 22:00 | 3256109 | 3 | 11.7894 | 15.5281 | -117.1269 | 5.5896 | 133.2333 | 0.0069 | 0.0047 |
| 2024_09_20 22:00 | 3245637 | 4 | 8.9236 | 12.6784 | -117.4255 | 17.8442 | 196.6783 | 0.0005 | 0.0019 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415298_12D134ED | 504990 | 632 | -88.4 | 504990 | 212 | -84.2 | 504990 | 149 | -88.4 | 504990 | 927 |
| MR_1774415298_1AE4A420 | 504990 | 212 | -82.5 | 504990 | 632 | -85.3 | 504990 | 149 | -88.0 | 504990 | 927 |
| MR_1774415298_E216F002 | 504990 | 632 | -87.8 | 504990 | 212 | -81.3 | 504990 | 149 | -85.7 | 504990 | 927 |
| MR_1774415298_C11ADCBF | 504990 | 632 | -86.0 | 504990 | 212 | -84.0 | 504990 | 149 | -86.5 | 504990 | 927 |
| MR_1774415298_F4A50F80 | 504990 | 632 | -87.3 | 504990 | 212 | -82.6 | 504990 | 149 | -85.0 | 504990 | 927 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 932: `ec469e7d-399...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ec469e7d-399b-4ebf-a4f8-a387cb57ee47` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3218451_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[932] topology](images/train_0932.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218451_4 **← 정답**
- `C2`: Decrease transmission power for 3218451_4
- `C3`: Decrease transmission power for 3235194_1
- `C4`: Increase A3 Offset threshold for 3235194_1
- `C5`: Lift the tilt angle of 3218451_4 by 3 degrees
- `C6`: Decrease A3 Offset threshold for 3218451_4
- `C7`: Add neighbor relationship between 3218451_4 and 3235194_1
- `C8`: Increase A3 Offset threshold for 3218451_4
- `C9`: Check test server and transmission issues
- `C10`: Adjust the azimuth of 3218451_4 by 46 degrees
- `C11`: Add neighbor relationship between 3219675_3 and 3235194_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218451_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235194_1
- `C14`: Press down the tilt angle  of 3235194_1 by 7 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235194_1
- `C16`: Increase transmission power for 3235194_1
- `C17`: Increase transmission power for 3218451_4
- `C18`: Press down the tilt angle of 3218451_4 by 3 degrees
- `C19`: Lift the tilt angle  of 3235194_1 by 7 degrees
- `C20`: Decrease A3 Offset threshold for 3235194_1
- `C21`: Adjust the azimuth of 3235194_1 by 50 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.791 | MS1 | 121.4656655444 | 31.1446353312 | 95 | 504990 | -87.78 | 15.91 | 503.78 | 0.00 | 2.50 | 1581 |
| 2024-09-20 22:21:32.364 | MS1 | 121.4656673071 | 31.1446247410 | 95 | 504990 | -85.33 | 15.12 | 455.07 | 0.02 | 2.48 | 1571 |
| 2024-09-20 22:21:33.336 | MS1 | 121.4656709585 | 31.1446273081 | 95 | 504990 | -88.12 | 15.39 | 485.81 | 0.20 | 2.70 | 1560 |
| 2024-09-20 22:21:34.648 | MS1 | 121.4656619681 | 31.1446358755 | 95 | 504990 | -87.18 | 15.93 | 55.02 | 0.59 | 2.39 | 591 |
| 2024-09-20 22:21:35.943 | MS1 | 121.4656597636 | 31.1446226775 | 95 | 504990 | -89.03 | 14.35 | 81.91 | 0.59 | 2.45 | 557 |
| 2024-09-20 22:21:36.279 | MS1 | 121.4656661095 | 31.1446363474 | 95 | 504990 | -88.03 | 12.84 | 104.34 | 0.64 | 2.18 | 621 |
| 2024-09-20 22:21:37.206 | MS1 | 121.4656699409 | 31.1446378572 | 95 | 504990 | -89.99 | 12.56 | 45.02 | 0.55 | 2.96 | 557 |
| 2024-09-20 22:21:38.644 | MS1 | 121.4656693079 | 31.1446231991 | 95 | 504990 | -90.83 | 12.70 | 84.58 | 0.57 | 2.61 | 587 |
| 2024-09-20 22:21:39.259 | MS1 | 121.4656779026 | 31.1446180158 | 95 | 504990 | -89.47 | 10.97 | 76.42 | 0.67 | 2.09 | 661 |
| 2024-09-20 22:21:40.276 | MS1 | 121.4656613754 | 31.1446302078 | 95 | 504990 | -90.60 | 8.06 | 480.92 | 0.17 | 2.23 | 1581 |
| 2024-09-20 22:21:41.484 | MS1 | 121.4656739060 | 31.1446337560 | 95 | 504990 | -89.74 | 12.27 | 571.18 | 0.07 | 3.00 | 1573 |
| 2024-09-20 22:21:42.483 | MS1 | 121.4656652037 | 31.1446274628 | 95 | 504990 | -92.55 | 12.46 | 542.62 | 0.01 | 2.75 | 1597 |

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
| 3218451 | 4 | 121.4758128734 | 31.1557696595 | 264 | 2 | 6 | 39.7 | TDD | 95 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3219675 | 3 | 121.4699124463 | 31.1539225852 | 197 | 0 | 7 | 25.7 | TDD | 945 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3235194 | 1 | 121.4666735939 | 31.1543017111 | 53 | 5 | 6 | 32.2 | TDD | 169 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3273732 | 2 | 121.4659334963 | 31.1464770088 | 45 | 1 | 8 | 44.2 | TDD | 330 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.341 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.363 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.470 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.470 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.189 | NREventA3 | measId:2;ServCellPCI:554;Se... |
| 2024-09-20 22:21:38.429 | NRHandoverAttempt | SourcePCI:554;SourceNR-ARFC... |
| 2024-09-20 22:21:38.477 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.490 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.616 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.616 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235194 | 1 | 18.3103 | 18.8448 | -116.8626 | 12.1057 | 177.6633 | 0.0060 | 0.0116 |
| 2024_09_20 22:00 | 3273732 | 2 | 16.4976 | 6.4107 | -116.7480 | 14.2690 | 178.9741 | 0.0039 | 0.0163 |
| 2024_09_20 22:00 | 3219675 | 3 | 16.2582 | 16.6173 | -114.5814 | 11.7576 | 145.8369 | 0.0031 | 0.0114 |
| 2024_09_20 22:00 | 3218451 | 4 | 16.4020 | 18.6363 | -116.6549 | 5.4042 | 131.1320 | 0.0153 | 0.0142 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416854_FD7435AB | 504990 | 95 | -86.2 | 504990 | 169 | -93.2 | 504990 | 945 | -96.9 | 504990 | 330 |
| MR_1774416854_B7FBA367 | 504990 | 95 | -88.8 | 504990 | 169 | -90.5 | 504990 | 945 | -97.3 | 504990 | 330 |
| MR_1774416854_091D3A98 | 504990 | 95 | -86.6 | 504990 | 169 | -92.5 | 504990 | 945 | -97.0 | 504990 | 330 |
| MR_1774416854_F4DEBDE7 | 504990 | 95 | -87.4 | 504990 | 169 | -92.0 | 504990 | 945 | -97.1 | 504990 | 330 |
| MR_1774416854_337C0755 | 504990 | 95 | -87.5 | 504990 | 169 | -92.1 | 504990 | 945 | -98.4 | 504990 | 330 |
| MR_1774416854_E174B31B | 504990 | 95 | -89.1 | 504990 | 169 | -93.9 | 504990 | 945 | -97.0 | 504990 | 330 |
| MR_1774416854_C6430518 | 504990 | 95 | -87.8 | 504990 | 169 | -91.2 | 504990 | 945 | -97.8 | 504990 | 330 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 933: `f2162684-946...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f2162684-9464-49c4-a191-44ec6d0bc8ab` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Add neighbor relationship between 3237551_1 and 3256985_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[933] topology](images/train_0933.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Check test server and transmission issues
- `C3`: Increase A3 Offset threshold for 3237551_1
- `C4`: Adjust the azimuth of 3256985_3 by 14 degrees
- `C5`: Decrease A3 Offset threshold for 3237551_1
- `C6`: Lift the tilt angle of 3237551_1 by 2 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256985_3
- `C8`: Decrease A3 Offset threshold for 3256985_3
- `C9`: Press down the tilt angle  of 3256985_3 by 5 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237551_1
- `C11`: Increase transmission power for 3256985_3
- `C12`: Increase transmission power for 3237551_1
- `C13`: Press down the tilt angle of 3237551_1 by 2 degrees
- `C14`: Add neighbor relationship between 3237551_1 and 3256985_3 **← 정답**
- `C15`: Decrease transmission power for 3237551_1
- `C16`: Lift the tilt angle  of 3256985_3 by 5 degrees
- `C17`: Adjust the azimuth of 3237551_1 by 50 degrees
- `C18`: Decrease transmission power for 3256985_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256985_3
- `C20`: Increase A3 Offset threshold for 3256985_3
- `C21`: Add neighbor relationship between 3210696_4 and 3256985_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237551_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.179 | MS1 | 121.4656718310 | 31.1446189707 | 977 | 504990 | -77.81 | 15.49 | 588.72 | 0.03 | 2.07 | 1568 |
| 2024-09-20 22:21:32.115 | MS1 | 121.4656640069 | 31.1446323348 | 977 | 504990 | -84.84 | 12.20 | 505.06 | 0.10 | 2.12 | 1561 |
| 2024-09-20 22:21:33.489 | MS1 | 121.4656774789 | 31.1446356343 | 977 | 504990 | -84.39 | 15.20 | 533.80 | 0.00 | 2.26 | 1592 |
| 2024-09-20 22:21:34.120 | MS1 | 121.4656743562 | 31.1446299248 | 977 | 504990 | -90.52 | -3.13 | 57.16 | 0.03 | 1.03 | 1585 |
| 2024-09-20 22:21:35.329 | MS1 | 121.4656587415 | 31.1446210886 | 977 | 504990 | -91.12 | -2.53 | 65.64 | 0.10 | 1.07 | 1600 |
| 2024-09-20 22:21:36.653 | MS1 | 121.4656722723 | 31.1446267891 | 977 | 504990 | -91.35 | -0.67 | 55.38 | 0.07 | 1.07 | 1586 |
| 2024-09-20 22:21:37.241 | MS1 | 121.4656754334 | 31.1446286966 | 977 | 504990 | -87.12 | -1.52 | 42.78 | 0.12 | 1.02 | 1573 |
| 2024-09-20 22:21:38.791 | MS1 | 121.4656600878 | 31.1446191728 | 977 | 504990 | -83.45 | 15.45 | 346.99 | 0.14 | 1.26 | 1581 |
| 2024-09-20 22:21:39.751 | MS1 | 121.4656592907 | 31.1446243703 | 977 | 504990 | -84.67 | 12.86 | 522.38 | 0.11 | 1.34 | 1580 |
| 2024-09-20 22:21:40.250 | MS1 | 121.4656775191 | 31.1446301497 | 977 | 504990 | -80.24 | 14.07 | 552.63 | 0.13 | 2.05 | 1566 |
| 2024-09-20 22:21:41.777 | MS1 | 121.4656701538 | 31.1446371444 | 977 | 504990 | -76.18 | 14.43 | 572.64 | 0.09 | 2.87 | 1582 |
| 2024-09-20 22:21:42.219 | MS1 | 121.4656772105 | 31.1446232000 | 977 | 504990 | -75.79 | 15.72 | 402.91 | 0.12 | 2.63 | 1578 |

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
| 3210696 | 4 | 121.4662221154 | 31.1556762812 | 224 | 15 | 1 | 31.1 | TDD | 286 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3237551 | 1 | 121.4725072123 | 31.1492292632 | 181 | 0 | 11 | 28.0 | TDD | 977 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3250782 | 2 | 121.4734977032 | 31.1473372644 | 351 | 4 | 2 | 23.9 | TDD | 690 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3256985 | 3 | 121.4712591360 | 31.1552692194 | 190 | 4 | 1 | 23.5 | TDD | 893 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.544 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.569 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.719 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.719 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.399 | NREventA3 | measId:2;ServCellPCI:394;Se... |
| 2024-09-20 22:21:36.399 | NREventA3 | measId:2;ServCellPCI:394;Se... |
| 2024-09-20 22:21:37.399 | NREventA3 | measId:2;ServCellPCI:394;Se... |
| 2024-09-20 22:21:39.899 | NRRRCReestablishAttempt | PCI:394 |
| 2024-09-20 22:21:39.919 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.934 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:40.065 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.065 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237551 | 1 | 5.7784 | 10.4455 | -116.0151 | 10.5028 | 180.7962 | 0.0071 | 0.1358 |
| 2024_09_20 22:00 | 3250782 | 2 | 7.8124 | 18.9391 | -117.1623 | 12.9916 | 80.2500 | 0.0064 | 0.0091 |
| 2024_09_20 22:00 | 3256985 | 3 | 15.4179 | 9.0672 | -116.2441 | 15.1881 | 91.5565 | 0.0100 | 0.0006 |
| 2024_09_20 22:00 | 3210696 | 4 | 9.7611 | 12.9208 | -117.3455 | 9.3964 | 177.4753 | 0.0161 | 0.0131 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416409_ADEC53AA | 504990 | 893 | -84.3 | 504990 | 977 | -89.3 | 504990 | 286 | -93.6 | 504990 | 690 |
| MR_1774416409_0FE1E78B | 504990 | 893 | -84.6 | 504990 | 977 | -89.6 | 504990 | 286 | -91.7 | 504990 | 690 |
| MR_1774416409_89EEB83D | 504990 | 977 | -90.6 | 504990 | 893 | -86.9 | 504990 | 286 | -94.4 | 504990 | 690 |
| MR_1774416409_AF074459 | 504990 | 977 | -92.5 | 504990 | 893 | -84.2 | 504990 | 286 | -94.9 | 504990 | 690 |
| MR_1774416409_DB180F73 | 504990 | 893 | -86.9 | 504990 | 977 | -89.9 | 504990 | 286 | -93.1 | 504990 | 690 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 934: `dcb2aa41-07d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dcb2aa41-07de-4338-8c98-e64452badab1` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Add neighbor relationship between 3249916_4 and 3215558_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[934] topology](images/train_0934.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3215558_2
- `C2`: Increase A3 Offset threshold for 3249916_4
- `C3`: Adjust the azimuth of 3215558_2 by 32 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease transmission power for 3215558_2
- `C6`: Increase transmission power for 3249916_4
- `C7`: Press down the tilt angle of 3249916_4 by 6 degrees
- `C8`: Lift the tilt angle  of 3215558_2 by 4 degrees
- `C9`: Decrease A3 Offset threshold for 3249916_4
- `C10`: Add neighbor relationship between 3264204_1 and 3215558_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249916_4
- `C12`: Increase A3 Offset threshold for 3215558_2
- `C13`: Decrease A3 Offset threshold for 3215558_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215558_2
- `C15`: Check test server and transmission issues
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215558_2
- `C17`: Decrease transmission power for 3249916_4
- `C18`: Add neighbor relationship between 3249916_4 and 3215558_2 **← 정답**
- `C19`: Lift the tilt angle of 3249916_4 by 6 degrees
- `C20`: Adjust the azimuth of 3249916_4 by 50 degrees
- `C21`: Press down the tilt angle  of 3215558_2 by 4 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249916_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.764 | MS1 | 121.4656612314 | 31.1446353421 | 615 | 504990 | -78.07 | 12.03 | 332.91 | 0.13 | 2.40 | 1562 |
| 2024-09-20 22:21:32.166 | MS1 | 121.4656722476 | 31.1446340809 | 615 | 504990 | -78.42 | 14.55 | 484.65 | 0.03 | 2.02 | 1563 |
| 2024-09-20 22:21:33.877 | MS1 | 121.4656739246 | 31.1446332155 | 615 | 504990 | -75.25 | 12.54 | 554.78 | 0.18 | 2.21 | 1567 |
| 2024-09-20 22:21:34.527 | MS1 | 121.4656625843 | 31.1446239764 | 615 | 504990 | -85.87 | -3.73 | 37.14 | 0.11 | 1.20 | 1594 |
| 2024-09-20 22:21:35.953 | MS1 | 121.4656594164 | 31.1446251329 | 615 | 504990 | -93.01 | -0.22 | 45.23 | 0.14 | 1.25 | 1579 |
| 2024-09-20 22:21:36.277 | MS1 | 121.4656777197 | 31.1446294415 | 615 | 504990 | -92.94 | -2.41 | 46.83 | 0.06 | 1.27 | 1569 |
| 2024-09-20 22:21:37.665 | MS1 | 121.4656718333 | 31.1446259391 | 615 | 504990 | -90.20 | -1.66 | 44.13 | 0.08 | 1.29 | 1597 |
| 2024-09-20 22:21:38.950 | MS1 | 121.4656739147 | 31.1446324924 | 615 | 504990 | -80.76 | 17.67 | 368.61 | 0.17 | 1.13 | 1583 |
| 2024-09-20 22:21:39.712 | MS1 | 121.4656659697 | 31.1446301536 | 615 | 504990 | -76.92 | 14.41 | 317.87 | 0.14 | 1.31 | 1576 |
| 2024-09-20 22:21:40.597 | MS1 | 121.4656746196 | 31.1446357041 | 615 | 504990 | -77.31 | 14.83 | 326.82 | 0.06 | 2.13 | 1590 |
| 2024-09-20 22:21:41.772 | MS1 | 121.4656692423 | 31.1446306010 | 615 | 504990 | -84.79 | 14.01 | 431.70 | 0.09 | 2.15 | 1567 |
| 2024-09-20 22:21:42.174 | MS1 | 121.4656584124 | 31.1446206843 | 615 | 504990 | -82.70 | 14.88 | 558.58 | 0.07 | 2.17 | 1583 |

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
| 3215558 | 2 | 121.4723564448 | 31.1519657305 | 250 | 2 | 10 | 32.3 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3232348 | 3 | 121.4745209666 | 31.1559054630 | 346 | 6 | 2 | 21.7 | TDD | 491 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3249916 | 4 | 121.4665753054 | 31.1485109679 | 115 | 1 | 4 | 39.3 | TDD | 615 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3264204 | 1 | 121.4650151378 | 31.1441582862 | 38 | 13 | 11 | 29.2 | TDD | 608 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.850 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.998 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.998 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.653 | NREventA3 | measId:2;ServCellPCI:719;Se... |
| 2024-09-20 22:21:35.653 | NREventA3 | measId:2;ServCellPCI:719;Se... |
| 2024-09-20 22:21:36.653 | NREventA3 | measId:2;ServCellPCI:719;Se... |
| 2024-09-20 22:21:39.153 | NRRRCReestablishAttempt | PCI:719 |
| 2024-09-20 22:21:39.166 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.176 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.326 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.326 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264204 | 1 | 16.1248 | 10.2556 | -114.9713 | 5.6195 | 179.0821 | 0.0042 | 0.0127 |
| 2024_09_20 22:00 | 3215558 | 2 | 14.0612 | 18.5514 | -116.8084 | 15.5343 | 195.8194 | 0.0192 | 0.0004 |
| 2024_09_20 22:00 | 3232348 | 3 | 18.4171 | 10.4869 | -114.1696 | 16.2156 | 136.9156 | 0.0060 | 0.0020 |
| 2024_09_20 22:00 | 3249916 | 4 | 19.3770 | 8.8749 | -117.9654 | 18.4831 | 185.9111 | 0.0078 | 0.1838 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413329_8E36AEA7 | 504990 | 615 | -87.0 | 504990 | 258 | -80.6 | 504990 | 608 | -87.2 | 504990 | 491 |
| MR_1774413329_6E94C3CA | 504990 | 615 | -85.8 | 504990 | 258 | -81.5 | 504990 | 608 | -86.1 | 504990 | 491 |
| MR_1774413329_EC844711 | 504990 | 615 | -86.3 | 504990 | 258 | -79.6 | 504990 | 608 | -87.4 | 504990 | 491 |
| MR_1774413329_7B91B678 | 504990 | 615 | -86.4 | 504990 | 258 | -81.3 | 504990 | 608 | -87.1 | 504990 | 491 |
| MR_1774413329_1C13630D | 504990 | 258 | -79.9 | 504990 | 615 | -85.3 | 504990 | 608 | -88.9 | 504990 | 491 |
| MR_1774413329_B2B95E4C | 504990 | 258 | -82.2 | 504990 | 615 | -84.6 | 504990 | 608 | -87.3 | 504990 | 491 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 935: `86565522-722...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `86565522-7224-44ab-aa5e-d9c22b7e8ffc` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease A3 Offset threshold for 3229841_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[935] topology](images/train_0935.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3227347_2
- `C2`: Increase A3 Offset threshold for 3229841_1
- `C3`: Adjust the azimuth of 3229841_1 by 24 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227347_2
- `C5`: Adjust the azimuth of 3227347_2 by 35 degrees
- `C6`: Increase transmission power for 3227347_2
- `C7`: Check test server and transmission issues
- `C8`: Add neighbor relationship between 3229841_1 and 3227347_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227347_2
- `C10`: Increase A3 Offset threshold for 3227347_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229841_1
- `C12`: Decrease A3 Offset threshold for 3227347_2
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Lift the tilt angle  of 3227347_2 by 10 degrees
- `C15`: Lift the tilt angle of 3229841_1 by 10 degrees
- `C16`: Press down the tilt angle  of 3227347_2 by 10 degrees
- `C17`: Press down the tilt angle of 3229841_1 by 10 degrees
- `C18`: Decrease transmission power for 3229841_1
- `C19`: Increase transmission power for 3229841_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229841_1
- `C21`: Decrease A3 Offset threshold for 3229841_1 **← 정답**
- `C22`: Add neighbor relationship between 3261097_4 and 3227347_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.336 | MS1 | 121.4656606602 | 31.1446348227 | 846 | 504990 | -83.26 | 13.12 | 407.43 | 0.05 | 2.25 | 1560 |
| 2024-09-20 22:21:32.622 | MS1 | 121.4656663342 | 31.1446285635 | 846 | 504990 | -83.93 | 12.52 | 390.73 | 0.11 | 2.91 | 1592 |
| 2024-09-20 22:21:33.248 | MS1 | 121.4656675324 | 31.1446245412 | 846 | 504990 | -83.00 | 12.59 | 379.19 | 0.01 | 2.08 | 1568 |
| 2024-09-20 22:21:34.766 | MS1 | 121.4656612606 | 31.1446355877 | 846 | 504990 | -86.19 | -1.65 | 55.78 | 0.08 | 1.04 | 1568 |
| 2024-09-20 22:21:35.615 | MS1 | 121.4656747395 | 31.1446191526 | 846 | 504990 | -89.10 | -0.43 | 58.02 | 0.05 | 1.26 | 1573 |
| 2024-09-20 22:21:36.235 | MS1 | 121.4656708025 | 31.1446232019 | 846 | 504990 | -85.42 | -2.08 | 37.29 | 0.14 | 1.41 | 1600 |
| 2024-09-20 22:21:37.960 | MS1 | 121.4656703053 | 31.1446277758 | 846 | 504990 | -83.05 | -1.71 | 57.07 | 0.19 | 1.09 | 1567 |
| 2024-09-20 22:21:38.613 | MS1 | 121.4656708599 | 31.1446286538 | 846 | 504990 | -84.54 | -0.65 | 43.44 | 0.07 | 1.25 | 1571 |
| 2024-09-20 22:21:39.837 | MS1 | 121.4656640323 | 31.1446268525 | 229 | 504990 | -83.32 | 14.97 | 275.05 | 0.17 | 1.01 | 1563 |
| 2024-09-20 22:21:40.203 | MS1 | 121.4656730349 | 31.1446338110 | 229 | 504990 | -75.88 | 13.84 | 372.87 | 0.14 | 2.50 | 1568 |
| 2024-09-20 22:21:41.320 | MS1 | 121.4656582894 | 31.1446181861 | 229 | 504990 | -79.93 | 17.83 | 298.71 | 0.08 | 2.20 | 1575 |
| 2024-09-20 22:21:42.864 | MS1 | 121.4656755542 | 31.1446310710 | 229 | 504990 | -79.08 | 16.04 | 373.39 | 0.17 | 2.51 | 1573 |

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
| 3227347 | 2 | 121.4665470068 | 31.1507166886 | 152 | 7 | 6 | 39.3 | TDD | 229 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3229841 | 1 | 121.4723854838 | 31.1477676675 | 265 | 10 | 3 | 17.5 | TDD | 846 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3251350 | 3 | 121.4703097837 | 31.1539700349 | 182 | 0 | 6 | 27.3 | TDD | 326 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3261097 | 4 | 121.4729847776 | 31.1468106044 | 133 | 9 | 10 | 32.4 | TDD | 143 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.371 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.391 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.541 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.541 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.176 | NREventA3 | measId:2;ServCellPCI:986;Se... |
| 2024-09-20 22:21:38.416 | NRHandoverAttempt | SourcePCI:986;SourceNR-ARFC... |
| 2024-09-20 22:21:38.466 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.478 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.615 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.615 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229841 | 1 | 19.6253 | 14.6562 | -117.0785 | 19.0777 | 182.3766 | 0.0036 | 0.1921 |
| 2024_09_20 22:00 | 3227347 | 2 | 13.0496 | 19.5077 | -116.3360 | 10.8636 | 178.4131 | 0.0039 | 0.0137 |
| 2024_09_20 22:00 | 3251350 | 3 | 8.2827 | 11.2869 | -117.5662 | 8.5614 | 149.1873 | 0.0171 | 0.0071 |
| 2024_09_20 22:00 | 3261097 | 4 | 12.0138 | 18.6421 | -114.5238 | 15.3476 | 187.5461 | 0.0190 | 0.0137 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412196_21F45E51 | 504990 | 229 | -81.0 | 504990 | 846 | -85.9 | 504990 | 143 | -80.9 | 504990 | 326 |
| MR_1774412196_3EF76976 | 504990 | 229 | -80.1 | 504990 | 846 | -86.5 | 504990 | 143 | -81.1 | 504990 | 326 |
| MR_1774412196_12668E88 | 504990 | 846 | -87.8 | 504990 | 229 | -79.7 | 504990 | 143 | -81.5 | 504990 | 326 |
| MR_1774412196_0E028FFA | 504990 | 846 | -87.4 | 504990 | 229 | -82.0 | 504990 | 143 | -83.9 | 504990 | 326 |
| MR_1774412196_0F25B0AC | 504990 | 846 | -84.2 | 504990 | 229 | -80.9 | 504990 | 143 | -83.5 | 504990 | 326 |
| MR_1774412196_3ECD8796 | 504990 | 846 | -87.7 | 504990 | 229 | -81.1 | 504990 | 143 | -83.8 | 504990 | 326 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 936: `c5d69ae1-5ef...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c5d69ae1-5efb-4dc9-83ca-d3948d4f3681` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Lift the tilt angle  of 3269399_4 by 4 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[936] topology](images/train_0936.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216569_1
- `C2`: Add neighbor relationship between 3269399_4 and 3267874_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267874_3
- `C4`: Increase transmission power for 3216569_1
- `C5`: Decrease transmission power for 3267874_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216569_1
- `C7`: Lift the tilt angle  of 3269399_4 by 4 degrees **← 정답**
- `C8`: Lift the tilt angle of 3216569_1 by 5 degrees
- `C9`: Decrease A3 Offset threshold for 3216569_1
- `C10`: Decrease transmission power for 3216569_1
- `C11`: Check test server and transmission issues
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Adjust the azimuth of 3216569_1 by 24 degrees
- `C14`: Increase transmission power for 3267874_3
- `C15`: Decrease A3 Offset threshold for 3267874_3
- `C16`: Increase A3 Offset threshold for 3216569_1
- `C17`: Adjust the azimuth of 3269399_4 by 10 degrees
- `C18`: Increase A3 Offset threshold for 3267874_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267874_3
- `C20`: Press down the tilt angle of 3216569_1 by 5 degrees
- `C21`: Add neighbor relationship between 3216569_1 and 3267874_3
- `C22`: Press down the tilt angle  of 3269399_4 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.900 | MS1 | 121.4656595953 | 31.1446285685 | 344 | 504990 | -86.35 | 16.75 | 580.56 | 0.06 | 2.97 | 1560 |
| 2024-09-20 22:21:32.545 | MS1 | 121.4656768272 | 31.1446290790 | 344 | 504990 | -86.81 | 15.38 | 488.93 | 0.04 | 2.00 | 1586 |
| 2024-09-20 22:21:33.199 | MS1 | 121.4656724497 | 31.1446238989 | 344 | 504990 | -88.55 | 17.84 | 417.85 | 0.13 | 2.84 | 1575 |
| 2024-09-20 22:21:34.642 | MS1 | 121.4656723807 | 31.1446322049 | 344 | 504990 | -90.46 | 14.75 | 69.68 | 0.03 | 2.16 | 1573 |
| 2024-09-20 22:21:35.435 | MS1 | 121.4656649758 | 31.1446334693 | 344 | 504990 | -87.29 | 13.66 | 86.71 | 0.19 | 2.20 | 1585 |
| 2024-09-20 22:21:36.947 | MS1 | 121.4656735515 | 31.1446180703 | 344 | 504990 | -87.41 | 14.85 | 72.29 | 0.14 | 2.88 | 1572 |
| 2024-09-20 22:21:37.488 | MS1 | 121.4656596383 | 31.1446339089 | 344 | 504990 | -89.06 | 10.15 | 81.34 | 0.07 | 2.38 | 1589 |
| 2024-09-20 22:21:38.691 | MS1 | 121.4656591973 | 31.1446362901 | 344 | 504990 | -90.45 | 9.12 | 68.76 | 0.00 | 2.91 | 1578 |
| 2024-09-20 22:21:39.121 | MS1 | 121.4656673399 | 31.1446263386 | 344 | 504990 | -92.69 | 12.64 | 93.10 | 0.12 | 2.61 | 1568 |
| 2024-09-20 22:21:40.346 | MS1 | 121.4656635275 | 31.1446297421 | 344 | 504990 | -89.82 | 9.79 | 350.98 | 0.03 | 2.44 | 1600 |
| 2024-09-20 22:21:41.760 | MS1 | 121.4656669102 | 31.1446354771 | 344 | 504990 | -93.52 | 8.39 | 436.92 | 0.05 | 2.26 | 1580 |
| 2024-09-20 22:21:42.110 | MS1 | 121.4656587116 | 31.1446260666 | 344 | 504990 | -89.12 | 11.91 | 466.00 | 0.13 | 2.66 | 1593 |

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
| 3216569 | 1 | 121.4695259154 | 31.1497643634 | 189 | 3 | 9 | 29.1 | TDD | 344 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3267874 | 3 | 121.4705777132 | 31.1473465434 | 227 | 0 | 10 | 38.4 | TDD | 350 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3269399 | 4 | 121.4727739652 | 31.1552094510 | 326 | 2 | 6 | 31.8 | TDD | 999 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3274840 | 2 | 121.4694846771 | 31.1514942105 | 231 | 14 | 0 | 36.2 | TDD | 281 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.385 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.409 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.536 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.536 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.204 | NREventA3 | measId:2;ServCellPCI:650;Se... |
| 2024-09-20 22:21:38.444 | NRHandoverAttempt | SourcePCI:650;SourceNR-ARFC... |
| 2024-09-20 22:21:38.488 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.499 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.625 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.625 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216569 | 1 | 76.8232 | 87.8680 | -116.7374 | 6.6225 | 176.0452 | 0.0142 | 0.0189 |
| 2024_09_20 22:00 | 3274840 | 2 | 17.2805 | 6.1158 | -115.9125 | 7.0896 | 127.0794 | 0.0009 | 0.0105 |
| 2024_09_20 22:00 | 3267874 | 3 | 15.8385 | 14.0236 | -115.8120 | 12.0561 | 179.3770 | 0.0108 | 0.0124 |
| 2024_09_20 22:00 | 3269399 | 4 | 18.4880 | 9.8249 | -117.5791 | 19.4995 | 106.2201 | 0.0081 | 0.0088 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416359_8D97BC3A | 504990 | 344 | -89.8 | 504990 | 350 | -97.6 | 504990 | 999 | -99.8 | 504990 | 281 |
| MR_1774416359_7117676C | 504990 | 344 | -90.8 | 504990 | 350 | -99.3 | 504990 | 999 | -97.5 | 504990 | 281 |
| MR_1774416359_3895D709 | 504990 | 344 | -92.2 | 504990 | 350 | -98.5 | 504990 | 999 | -96.7 | 504990 | 281 |
| MR_1774416359_CC77546C | 504990 | 344 | -89.9 | 504990 | 350 | -96.8 | 504990 | 999 | -96.8 | 504990 | 281 |
| MR_1774416359_E1997F96 | 504990 | 344 | -91.6 | 504990 | 350 | -99.4 | 504990 | 999 | -97.7 | 504990 | 281 |
| MR_1774416359_12E4CD14 | 504990 | 344 | -91.8 | 504990 | 350 | -97.3 | 504990 | 999 | -99.0 | 504990 | 281 |
| MR_1774416359_2E529342 | 504990 | 344 | -91.3 | 504990 | 350 | -97.0 | 504990 | 999 | -96.5 | 504990 | 281 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 937: `1e46dba1-b49...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1e46dba1-b493-4c8f-87ec-3f389d28b8ce` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[937] topology](images/train_0937.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236303_4
- `C2`: Adjust the azimuth of 3236303_4 by 11 degrees
- `C3`: Increase A3 Offset threshold for 3236303_4
- `C4`: Decrease A3 Offset threshold for 3225861_2
- `C5`: Check test server and transmission issues
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225861_2
- `C7`: Increase transmission power for 3225861_2
- `C8`: Lift the tilt angle  of 3236303_4 by 10 degrees
- `C9`: Increase transmission power for 3236303_4
- `C10`: Decrease A3 Offset threshold for 3236303_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236303_4
- `C12`: Press down the tilt angle of 3225861_2 by 1 degrees
- `C13`: Decrease transmission power for 3225861_2
- `C14`: Insufficient data; more data is needed for judgment. **← 정답**
- `C15`: Adjust the azimuth of 3225861_2 by 50 degrees
- `C16`: Lift the tilt angle of 3225861_2 by 1 degrees
- `C17`: Increase A3 Offset threshold for 3225861_2
- `C18`: Add neighbor relationship between 3250343_1 and 3236303_4
- `C19`: Decrease transmission power for 3236303_4
- `C20`: Press down the tilt angle  of 3236303_4 by 10 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225861_2
- `C22`: Add neighbor relationship between 3225861_2 and 3236303_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.805 | MS1 | 121.4656681275 | 31.1446281009 | 620 | 504990 | -85.75 | 16.42 | 524.32 | 0.11 | 2.11 | 1566 |
| 2024-09-20 22:21:32.143 | MS1 | 121.4656722305 | 31.1446195243 | 620 | 504990 | -86.72 | 16.70 | 378.57 | 0.11 | 2.02 | 1567 |
| 2024-09-20 22:21:33.879 | MS1 | 121.4656602015 | 31.1446358094 | 620 | 504990 | -88.42 | 15.67 | 379.19 | 0.20 | 2.63 | 1590 |
| 2024-09-20 22:21:34.457 | MS1 | 121.4656623194 | 31.1446233678 | 620 | 504990 | -91.93 | 12.57 | 60.13 | 0.10 | 2.39 | 1572 |
| 2024-09-20 22:21:35.730 | MS1 | 121.4656653459 | 31.1446317028 | 620 | 504990 | -89.79 | 15.56 | 75.98 | 0.04 | 2.84 | 1578 |
| 2024-09-20 22:21:36.897 | MS1 | 121.4656626435 | 31.1446360772 | 620 | 504990 | -85.80 | 15.93 | 63.53 | 0.16 | 2.66 | 1590 |
| 2024-09-20 22:21:37.620 | MS1 | 121.4656745699 | 31.1446367597 | 620 | 504990 | -92.17 | 11.36 | 99.86 | 0.17 | 2.57 | 1565 |
| 2024-09-20 22:21:38.160 | MS1 | 121.4656618208 | 31.1446371760 | 620 | 504990 | -89.83 | 8.27 | 83.46 | 0.19 | 2.01 | 1592 |
| 2024-09-20 22:21:39.427 | MS1 | 121.4656675463 | 31.1446205309 | 620 | 504990 | -92.25 | 10.57 | 62.51 | 0.11 | 2.67 | 1572 |
| 2024-09-20 22:21:40.855 | MS1 | 121.4656700139 | 31.1446195360 | 620 | 504990 | -89.59 | 10.23 | 528.38 | 0.19 | 2.58 | 1592 |
| 2024-09-20 22:21:41.686 | MS1 | 121.4656652660 | 31.1446254186 | 620 | 504990 | -92.84 | 8.33 | 481.44 | 0.11 | 2.56 | 1576 |
| 2024-09-20 22:21:42.430 | MS1 | 121.4656692947 | 31.1446343594 | 620 | 504990 | -91.06 | 11.86 | 312.13 | 0.02 | 2.18 | 1565 |

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
| 3225861 | 2 | 121.4749350653 | 31.1555775594 | 107 | 0 | 3 | 24.5 | TDD | 620 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3236303 | 4 | 121.4738676718 | 31.1548601128 | 203 | 11 | 6 | 20.4 | TDD | 294 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3250343 | 1 | 121.4689339062 | 31.1529567425 | 42 | 14 | 1 | 15.9 | TDD | 713 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3263522 | 3 | 121.4690434270 | 31.1491241448 | 31 | 5 | 3 | 29.8 | TDD | 268 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.977 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.992 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.137 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.137 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.863 | NREventA3 | measId:2;ServCellPCI:318;Se... |
| 2024-09-20 22:21:38.103 | NRHandoverAttempt | SourcePCI:318;SourceNR-ARFC... |
| 2024-09-20 22:21:38.143 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.158 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.286 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.286 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3250343 | 1 | 85.9126 | 84.7815 | -115.6380 | 13.9816 | 91.0313 | 0.0088 | 0.0061 |
| 2024_09_19 22:00 | 3225861 | 2 | 89.8479 | 83.8061 | -117.0669 | 6.6357 | 193.1403 | 0.0143 | 0.0069 |
| 2024_09_19 22:00 | 3263522 | 3 | 80.9503 | 93.9711 | -114.0894 | 7.4457 | 97.4987 | 0.0148 | 0.0198 |
| 2024_09_19 22:00 | 3236303 | 4 | 92.6247 | 91.5218 | -115.4238 | 19.1873 | 195.7553 | 0.0170 | 0.0029 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412259_AF204C9F | 504990 | 620 | -90.3 | 504990 | 294 | -91.0 | 504990 | 713 | -103.2 | 504990 | 268 |
| MR_1774412259_6389FC64 | 504990 | 620 | -93.8 | 504990 | 294 | -93.2 | 504990 | 713 | -104.0 | 504990 | 268 |
| MR_1774412259_771C6435 | 504990 | 620 | -91.6 | 504990 | 294 | -91.5 | 504990 | 713 | -101.1 | 504990 | 268 |
| MR_1774412259_FFF38611 | 504990 | 620 | -92.6 | 504990 | 294 | -93.0 | 504990 | 713 | -103.5 | 504990 | 268 |
| MR_1774412259_345A684C | 504990 | 620 | -90.6 | 504990 | 294 | -93.1 | 504990 | 713 | -103.7 | 504990 | 268 |
| MR_1774412259_FCA79E12 | 504990 | 620 | -92.2 | 504990 | 294 | -90.9 | 504990 | 713 | -104.3 | 504990 | 268 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 938: `c96e6867-b4e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c96e6867-b4e2-426f-931f-bac1e2f3b9ce` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease A3 Offset threshold for 3269780_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[938] topology](images/train_0938.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3269780_2 by 9 degrees
- `C2`: Decrease transmission power for 3269780_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269780_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease A3 Offset threshold for 3236272_3
- `C6`: Add neighbor relationship between 3269780_2 and 3236272_3
- `C7`: Check test server and transmission issues
- `C8`: Increase transmission power for 3269780_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236272_3
- `C10`: Adjust the azimuth of 3269780_2 by 16 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236272_3
- `C12`: Lift the tilt angle  of 3236272_3 by 10 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269780_2
- `C14`: Add neighbor relationship between 3239326_1 and 3236272_3
- `C15`: Increase A3 Offset threshold for 3236272_3
- `C16`: Decrease A3 Offset threshold for 3269780_2 **← 정답**
- `C17`: Press down the tilt angle of 3269780_2 by 9 degrees
- `C18`: Decrease transmission power for 3236272_3
- `C19`: Adjust the azimuth of 3236272_3 by 50 degrees
- `C20`: Increase transmission power for 3236272_3
- `C21`: Press down the tilt angle  of 3236272_3 by 10 degrees
- `C22`: Increase A3 Offset threshold for 3269780_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.290 | MS1 | 121.4656749721 | 31.1446208011 | 147 | 504990 | -81.75 | 17.92 | 312.83 | 0.16 | 2.09 | 1589 |
| 2024-09-20 22:21:32.418 | MS1 | 121.4656779022 | 31.1446195981 | 147 | 504990 | -79.70 | 15.07 | 474.76 | 0.06 | 2.08 | 1566 |
| 2024-09-20 22:21:33.310 | MS1 | 121.4656707395 | 31.1446283012 | 147 | 504990 | -78.53 | 13.99 | 396.46 | 0.02 | 2.97 | 1596 |
| 2024-09-20 22:21:34.952 | MS1 | 121.4656648707 | 31.1446371946 | 147 | 504990 | -87.27 | -3.26 | 40.32 | 0.12 | 1.24 | 1564 |
| 2024-09-20 22:21:35.310 | MS1 | 121.4656690615 | 31.1446238170 | 147 | 504990 | -92.58 | -0.23 | 63.69 | 0.03 | 1.18 | 1580 |
| 2024-09-20 22:21:36.883 | MS1 | 121.4656688186 | 31.1446242662 | 147 | 504990 | -92.52 | -2.53 | 30.24 | 0.03 | 1.31 | 1563 |
| 2024-09-20 22:21:37.937 | MS1 | 121.4656630626 | 31.1446234212 | 147 | 504990 | -88.24 | -0.44 | 43.19 | 0.18 | 1.17 | 1587 |
| 2024-09-20 22:21:38.255 | MS1 | 121.4656626787 | 31.1446368211 | 147 | 504990 | -83.88 | -3.55 | 41.87 | 0.18 | 1.23 | 1595 |
| 2024-09-20 22:21:39.437 | MS1 | 121.4656691083 | 31.1446192505 | 860 | 504990 | -80.37 | 17.87 | 245.65 | 0.02 | 1.32 | 1565 |
| 2024-09-20 22:21:40.533 | MS1 | 121.4656613891 | 31.1446206488 | 860 | 504990 | -75.32 | 14.36 | 375.70 | 0.07 | 2.40 | 1588 |
| 2024-09-20 22:21:41.927 | MS1 | 121.4656642291 | 31.1446287803 | 860 | 504990 | -78.14 | 12.27 | 551.47 | 0.15 | 2.56 | 1573 |
| 2024-09-20 22:21:42.220 | MS1 | 121.4656729122 | 31.1446299438 | 860 | 504990 | -83.73 | 14.18 | 485.85 | 0.14 | 2.52 | 1581 |

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
| 3213144 | 4 | 121.4732944853 | 31.1481833078 | 32 | 6 | 1 | 41.2 | TDD | 7 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3236272 | 3 | 121.4641937173 | 31.1534881157 | 94 | 12 | 9 | 39.9 | TDD | 860 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3239326 | 1 | 121.4681701767 | 31.1534152085 | 186 | 1 | 1 | 43.4 | TDD | 145 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3269780 | 2 | 121.4701716360 | 31.1471181368 | 221 | 5 | 4 | 33.7 | TDD | 147 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.758 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.773 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.923 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.923 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.618 | NREventA3 | measId:2;ServCellPCI:984;Se... |
| 2024-09-20 22:21:37.858 | NRHandoverAttempt | SourcePCI:984;SourceNR-ARFC... |
| 2024-09-20 22:21:37.907 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.920 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.056 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.056 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239326 | 1 | 6.6293 | 8.4024 | -116.7458 | 19.0728 | 110.5782 | 0.0099 | 0.0184 |
| 2024_09_20 22:00 | 3269780 | 2 | 15.5580 | 11.0387 | -115.0086 | 11.5462 | 173.8339 | 0.0057 | 0.1652 |
| 2024_09_20 22:00 | 3236272 | 3 | 14.4990 | 14.6339 | -114.7378 | 15.2993 | 136.0953 | 0.0047 | 0.0111 |
| 2024_09_20 22:00 | 3213144 | 4 | 17.4298 | 15.0285 | -115.9289 | 14.2681 | 106.4381 | 0.0147 | 0.0111 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412361_D5FA1B2C | 504990 | 860 | -83.3 | 504990 | 147 | -88.5 | 504990 | 145 | -83.3 | 504990 | 7 |
| MR_1774412361_8394FF26 | 504990 | 147 | -88.4 | 504990 | 860 | -80.0 | 504990 | 145 | -84.2 | 504990 | 7 |
| MR_1774412361_2F897F11 | 504990 | 147 | -87.4 | 504990 | 860 | -83.5 | 504990 | 145 | -83.8 | 504990 | 7 |
| MR_1774412361_E969C642 | 504990 | 147 | -86.7 | 504990 | 860 | -83.5 | 504990 | 145 | -83.9 | 504990 | 7 |
| MR_1774412361_862C2A22 | 504990 | 860 | -81.4 | 504990 | 147 | -87.4 | 504990 | 145 | -83.5 | 504990 | 7 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 939: `0191f687-27d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0191f687-27d3-40f8-8e8e-518ca3f64ce6` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[939] topology](images/train_0939.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3231916_1 by 9 degrees
- `C2`: Decrease A3 Offset threshold for 3275563_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275563_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231916_1
- `C5`: Lift the tilt angle  of 3231916_1 by 9 degrees
- `C6`: Adjust the azimuth of 3231916_1 by 49 degrees
- `C7`: Add neighbor relationship between 3222345_4 and 3231916_1
- `C8`: Decrease transmission power for 3231916_1
- `C9`: Adjust the azimuth of 3275563_2 by 50 degrees
- `C10`: Decrease A3 Offset threshold for 3231916_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231916_1
- `C12`: Decrease transmission power for 3275563_2
- `C13`: Insufficient data; more data is needed for judgment. **← 정답**
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275563_2
- `C15`: Check test server and transmission issues
- `C16`: Add neighbor relationship between 3275563_2 and 3231916_1
- `C17`: Lift the tilt angle of 3275563_2 by 2 degrees
- `C18`: Increase transmission power for 3275563_2
- `C19`: Increase A3 Offset threshold for 3275563_2
- `C20`: Press down the tilt angle of 3275563_2 by 2 degrees
- `C21`: Increase A3 Offset threshold for 3231916_1
- `C22`: Increase transmission power for 3231916_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.890 | MS1 | 121.4656765913 | 31.1446345734 | 249 | 504990 | -91.14 | 17.81 | 573.17 | 0.08 | 2.16 | 1596 |
| 2024-09-20 22:21:32.708 | MS1 | 121.4656743040 | 31.1446252419 | 249 | 504990 | -85.01 | 13.50 | 574.48 | 0.08 | 2.65 | 1570 |
| 2024-09-20 22:21:33.727 | MS1 | 121.4656750513 | 31.1446350195 | 249 | 504990 | -90.76 | 16.67 | 436.81 | 0.19 | 2.80 | 1582 |
| 2024-09-20 22:21:34.377 | MS1 | 121.4656681395 | 31.1446364638 | 249 | 504990 | -91.14 | 17.02 | 48.31 | 0.14 | 2.18 | 1583 |
| 2024-09-20 22:21:35.286 | MS1 | 121.4656599598 | 31.1446334333 | 249 | 504990 | -89.95 | 13.49 | 89.21 | 0.20 | 2.67 | 1579 |
| 2024-09-20 22:21:36.465 | MS1 | 121.4656624126 | 31.1446220904 | 249 | 504990 | -89.58 | 13.16 | 84.90 | 0.09 | 2.18 | 1582 |
| 2024-09-20 22:21:37.313 | MS1 | 121.4656593548 | 31.1446280243 | 249 | 504990 | -92.51 | 7.84 | 96.57 | 0.03 | 2.28 | 1597 |
| 2024-09-20 22:21:38.225 | MS1 | 121.4656661189 | 31.1446306066 | 249 | 504990 | -90.26 | 11.63 | 98.88 | 0.16 | 2.17 | 1589 |
| 2024-09-20 22:21:39.486 | MS1 | 121.4656755521 | 31.1446299654 | 249 | 504990 | -89.49 | 8.48 | 68.34 | 0.14 | 2.11 | 1592 |
| 2024-09-20 22:21:40.332 | MS1 | 121.4656686215 | 31.1446239278 | 249 | 504990 | -91.58 | 11.40 | 368.22 | 0.05 | 2.37 | 1599 |
| 2024-09-20 22:21:41.504 | MS1 | 121.4656754864 | 31.1446376642 | 249 | 504990 | -90.10 | 9.22 | 528.41 | 0.03 | 2.18 | 1591 |
| 2024-09-20 22:21:42.995 | MS1 | 121.4656612063 | 31.1446303138 | 249 | 504990 | -90.60 | 9.92 | 543.98 | 0.07 | 2.93 | 1573 |

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
| 3222345 | 4 | 121.4657929505 | 31.1522732025 | 126 | 8 | 10 | 28.4 | TDD | 208 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3231916 | 1 | 121.4690029186 | 31.1447617266 | 316 | 6 | 6 | 15.9 | TDD | 456 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3267156 | 3 | 121.4749092307 | 31.1460114701 | 14 | 2 | 9 | 29.0 | TDD | 274 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3275563 | 2 | 121.4711162273 | 31.1515381273 | 333 | 1 | 11 | 22.5 | TDD | 249 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.343 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.358 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.474 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.474 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.209 | NREventA3 | measId:2;ServCellPCI:909;Se... |
| 2024-09-20 22:21:38.449 | NRHandoverAttempt | SourcePCI:909;SourceNR-ARFC... |
| 2024-09-20 22:21:38.490 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.505 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.607 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.607 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3231916 | 1 | 81.3732 | 94.4142 | -114.0596 | 14.7569 | 99.8712 | 0.0139 | 0.0185 |
| 2024_09_19 22:00 | 3275563 | 2 | 78.3248 | 75.0716 | -116.2733 | 9.9864 | 108.5304 | 0.0082 | 0.0147 |
| 2024_09_19 22:00 | 3267156 | 3 | 80.4746 | 80.8154 | -116.7574 | 13.8529 | 137.7035 | 0.0192 | 0.0023 |
| 2024_09_19 22:00 | 3222345 | 4 | 80.7804 | 92.9200 | -115.5654 | 9.4508 | 184.0453 | 0.0129 | 0.0183 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417038_4704155B | 504990 | 249 | -92.6 | 504990 | 456 | -91.0 | 504990 | 208 | -104.7 | 504990 | 274 |
| MR_1774417038_EF4478CE | 504990 | 249 | -93.0 | 504990 | 456 | -90.4 | 504990 | 208 | -103.8 | 504990 | 274 |
| MR_1774417038_12CDBD73 | 504990 | 249 | -90.9 | 504990 | 456 | -93.8 | 504990 | 208 | -102.2 | 504990 | 274 |
| MR_1774417038_0879341A | 504990 | 249 | -91.4 | 504990 | 456 | -93.8 | 504990 | 208 | -103.4 | 504990 | 274 |
| MR_1774417038_EF4920D7 | 504990 | 249 | -89.9 | 504990 | 456 | -92.0 | 504990 | 208 | -105.5 | 504990 | 274 |

> *... 2개 열 생략 (전체 14열)*

---
