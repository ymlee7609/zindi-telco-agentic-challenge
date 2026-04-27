# Track A 문제 분석 — train[340]~train[349]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[340] ~ train[349] (10개)

## 목차

1. [문제 340: `e1f93ad4-279...`](#340) — single-answer, 정답: C2
2. [문제 341: `e856e40e-047...`](#341) — single-answer, 정답: C5
3. [문제 342: `b26f8458-b7b...`](#342) — single-answer, 정답: C20
4. [문제 343: `82527a90-142...`](#343) — single-answer, 정답: C11
5. [문제 344: `6ebba336-3a3...`](#344) — single-answer, 정답: C14
6. [문제 345: `bec47666-3e0...`](#345) — single-answer, 정답: C17
7. [문제 346: `030d78b6-def...`](#346) — multiple-answer, 정답: C12|C14
8. [문제 347: `6de715ec-0bc...`](#347) — single-answer, 정답: C17
9. [문제 348: `70063ca3-d21...`](#348) — single-answer, 정답: C12
10. [문제 349: `637a6ca6-8a5...`](#349) — single-answer, 정답: C14

---

### 문제 340: `e1f93ad4-279...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e1f93ad4-2791-4512-8f53-304883dce499` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Decrease A3 Offset threshold for 3216062_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[340] topology](images/train_0340.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278620_2
- `C2`: Decrease A3 Offset threshold for 3216062_1 **← 정답**
- `C3`: Decrease transmission power for 3216062_1
- `C4`: Press down the tilt angle of 3216062_1 by 10 degrees
- `C5`: Adjust the azimuth of 3278620_2 by 50 degrees
- `C6`: Adjust the azimuth of 3216062_1 by 21 degrees
- `C7`: Increase transmission power for 3278620_2
- `C8`: Increase A3 Offset threshold for 3216062_1
- `C9`: Decrease transmission power for 3278620_2
- `C10`: Add neighbor relationship between 3216062_1 and 3278620_2
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase A3 Offset threshold for 3278620_2
- `C13`: Lift the tilt angle  of 3278620_2 by 9 degrees
- `C14`: Lift the tilt angle of 3216062_1 by 10 degrees
- `C15`: Add neighbor relationship between 3271098_3 and 3278620_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216062_1
- `C17`: Press down the tilt angle  of 3278620_2 by 9 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278620_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216062_1
- `C20`: Decrease A3 Offset threshold for 3278620_2
- `C21`: Check test server and transmission issues
- `C22`: Increase transmission power for 3216062_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.438 | MS1 | 121.4656611473 | 31.1446302743 | 192 | 504990 | -78.55 | 14.26 | 310.51 | 0.17 | 2.36 | 1575 |
| 2024-09-20 22:21:32.948 | MS1 | 121.4656746006 | 31.1446251562 | 192 | 504990 | -75.86 | 12.49 | 348.12 | 0.02 | 2.47 | 1567 |
| 2024-09-20 22:21:33.939 | MS1 | 121.4656704198 | 31.1446182171 | 192 | 504990 | -81.67 | 15.27 | 448.53 | 0.09 | 2.61 | 1583 |
| 2024-09-20 22:21:34.220 | MS1 | 121.4656614253 | 31.1446325329 | 192 | 504990 | -83.47 | -1.11 | 42.66 | 0.07 | 1.27 | 1582 |
| 2024-09-20 22:21:35.234 | MS1 | 121.4656681616 | 31.1446231608 | 192 | 504990 | -90.61 | -0.37 | 53.04 | 0.01 | 1.12 | 1594 |
| 2024-09-20 22:21:36.762 | MS1 | 121.4656745155 | 31.1446234975 | 192 | 504990 | -88.12 | -2.59 | 61.73 | 0.01 | 1.49 | 1596 |
| 2024-09-20 22:21:37.571 | MS1 | 121.4656661820 | 31.1446337227 | 192 | 504990 | -86.53 | -2.39 | 41.25 | 0.02 | 1.49 | 1575 |
| 2024-09-20 22:21:38.483 | MS1 | 121.4656692909 | 31.1446253199 | 192 | 504990 | -88.10 | -3.47 | 66.19 | 0.19 | 1.04 | 1572 |
| 2024-09-20 22:21:39.565 | MS1 | 121.4656611309 | 31.1446323655 | 223 | 504990 | -82.37 | 12.96 | 209.03 | 0.10 | 1.28 | 1572 |
| 2024-09-20 22:21:40.246 | MS1 | 121.4656750690 | 31.1446227809 | 223 | 504990 | -77.02 | 17.06 | 500.48 | 0.02 | 2.59 | 1595 |
| 2024-09-20 22:21:41.249 | MS1 | 121.4656775048 | 31.1446220237 | 223 | 504990 | -80.76 | 16.70 | 389.31 | 0.09 | 2.59 | 1592 |
| 2024-09-20 22:21:42.535 | MS1 | 121.4656594687 | 31.1446248741 | 223 | 504990 | -76.49 | 16.39 | 369.14 | 0.19 | 2.46 | 1591 |

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
| 3216062 | 1 | 121.4642627821 | 31.1554954562 | 195 | 13 | 7 | 23.3 | TDD | 192 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3219069 | 4 | 121.4663167334 | 31.1558851329 | 123 | 13 | 0 | 33.9 | TDD | 503 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3271098 | 3 | 121.4702204335 | 31.1456057708 | 137 | 4 | 0 | 47.2 | TDD | 367 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3278620 | 2 | 121.4647081090 | 31.1544804704 | 113 | 7 | 1 | 37.9 | TDD | 223 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.496 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.515 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.617 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.617 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.337 | NREventA3 | measId:2;ServCellPCI:146;Se... |
| 2024-09-20 22:21:38.577 | NRHandoverAttempt | SourcePCI:146;SourceNR-ARFC... |
| 2024-09-20 22:21:38.615 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.625 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.736 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.736 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216062 | 1 | 19.4831 | 7.7285 | -116.2998 | 13.1044 | 159.0778 | 0.0118 | 0.1380 |
| 2024_09_20 22:00 | 3278620 | 2 | 17.5438 | 18.4562 | -117.7069 | 14.3110 | 125.2356 | 0.0155 | 0.0159 |
| 2024_09_20 22:00 | 3271098 | 3 | 6.2751 | 5.5415 | -117.4246 | 5.0792 | 138.2161 | 0.0098 | 0.0062 |
| 2024_09_20 22:00 | 3219069 | 4 | 9.1158 | 9.4797 | -115.4381 | 5.7151 | 131.2105 | 0.0128 | 0.0076 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412035_4CE686C7 | 504990 | 223 | -78.6 | 504990 | 192 | -83.3 | 504990 | 367 | -77.3 | 504990 | 503 |
| MR_1774412035_542401D2 | 504990 | 223 | -78.7 | 504990 | 192 | -81.6 | 504990 | 367 | -79.4 | 504990 | 503 |
| MR_1774412035_A54A7F53 | 504990 | 223 | -76.1 | 504990 | 192 | -84.0 | 504990 | 367 | -79.3 | 504990 | 503 |
| MR_1774412035_2571E365 | 504990 | 223 | -77.5 | 504990 | 192 | -83.8 | 504990 | 367 | -78.9 | 504990 | 503 |
| MR_1774412035_19DABD0E | 504990 | 192 | -85.1 | 504990 | 223 | -76.0 | 504990 | 367 | -77.8 | 504990 | 503 |
| MR_1774412035_782508B8 | 504990 | 223 | -78.4 | 504990 | 192 | -82.3 | 504990 | 367 | -77.2 | 504990 | 503 |
| MR_1774412035_B20F1D09 | 504990 | 192 | -84.4 | 504990 | 223 | -77.4 | 504990 | 367 | -78.9 | 504990 | 503 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 341: `e856e40e-047...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e856e40e-0477-48f1-bee3-d0bcf288d1d4` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3275905_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[341] topology](images/train_0341.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275905_1
- `C3`: Press down the tilt angle of 3275905_1 by 3 degrees
- `C4`: Adjust the azimuth of 3275905_1 by 26 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275905_1 **← 정답**
- `C6`: Increase A3 Offset threshold for 3219507_2
- `C7`: Decrease transmission power for 3275905_1
- `C8`: Check test server and transmission issues
- `C9`: Increase transmission power for 3275905_1
- `C10`: Lift the tilt angle of 3275905_1 by 3 degrees
- `C11`: Press down the tilt angle  of 3219507_2 by 3 degrees
- `C12`: Decrease A3 Offset threshold for 3275905_1
- `C13`: Increase A3 Offset threshold for 3275905_1
- `C14`: Decrease transmission power for 3219507_2
- `C15`: Increase transmission power for 3219507_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219507_2
- `C17`: Lift the tilt angle  of 3219507_2 by 3 degrees
- `C18`: Adjust the azimuth of 3219507_2 by 50 degrees
- `C19`: Add neighbor relationship between 3271207_4 and 3219507_2
- `C20`: Add neighbor relationship between 3275905_1 and 3219507_2
- `C21`: Decrease A3 Offset threshold for 3219507_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219507_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.872 | MS1 | 121.4656613042 | 31.1446370841 | 737 | 504990 | -86.44 | 14.54 | 418.12 | 0.16 | 2.63 | 1593 |
| 2024-09-20 22:21:32.279 | MS1 | 121.4656765146 | 31.1446349469 | 737 | 504990 | -88.00 | 15.25 | 340.99 | 0.16 | 2.18 | 1577 |
| 2024-09-20 22:21:33.954 | MS1 | 121.4656709757 | 31.1446339526 | 737 | 504990 | -88.69 | 16.95 | 521.76 | 0.11 | 2.92 | 1599 |
| 2024-09-20 22:21:34.183 | MS1 | 121.4656627792 | 31.1446310078 | 737 | 504990 | -91.42 | 14.31 | 103.03 | 0.55 | 2.35 | 595 |
| 2024-09-20 22:21:35.743 | MS1 | 121.4656735830 | 31.1446308526 | 737 | 504990 | -89.07 | 13.51 | 86.54 | 0.65 | 2.83 | 584 |
| 2024-09-20 22:21:36.929 | MS1 | 121.4656614961 | 31.1446361971 | 737 | 504990 | -87.36 | 13.43 | 102.71 | 0.55 | 2.99 | 511 |
| 2024-09-20 22:21:37.905 | MS1 | 121.4656660781 | 31.1446322520 | 737 | 504990 | -93.45 | 12.24 | 82.72 | 0.61 | 2.90 | 654 |
| 2024-09-20 22:21:38.433 | MS1 | 121.4656652778 | 31.1446228069 | 737 | 504990 | -90.04 | 7.93 | 90.55 | 0.59 | 2.74 | 502 |
| 2024-09-20 22:21:39.908 | MS1 | 121.4656752711 | 31.1446323562 | 737 | 504990 | -90.23 | 8.46 | 69.47 | 0.67 | 2.30 | 690 |
| 2024-09-20 22:21:40.779 | MS1 | 121.4656691932 | 31.1446362912 | 737 | 504990 | -92.29 | 10.11 | 367.59 | 0.19 | 2.19 | 1566 |
| 2024-09-20 22:21:41.243 | MS1 | 121.4656645856 | 31.1446343982 | 737 | 504990 | -90.57 | 9.74 | 481.14 | 0.07 | 2.93 | 1563 |
| 2024-09-20 22:21:42.867 | MS1 | 121.4656610894 | 31.1446217157 | 737 | 504990 | -93.88 | 10.50 | 467.20 | 0.12 | 2.49 | 1569 |

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
| 3215150 | 3 | 121.4659128361 | 31.1484328975 | 95 | 8 | 8 | 26.1 | TDD | 716 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3219507 | 2 | 121.4717456289 | 31.1506095123 | 332 | 1 | 6 | 35.8 | TDD | 978 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3271207 | 4 | 121.4696341463 | 31.1488170148 | 268 | 7 | 8 | 26.3 | TDD | 44 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3275905 | 1 | 121.4647390699 | 31.1515135820 | 199 | 2 | 5 | 16.6 | TDD | 737 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.995 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.012 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.161 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.161 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.836 | NREventA3 | measId:2;ServCellPCI:435;Se... |
| 2024-09-20 22:21:38.076 | NRHandoverAttempt | SourcePCI:435;SourceNR-ARFC... |
| 2024-09-20 22:21:38.115 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.126 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.235 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.235 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275905 | 1 | 11.3970 | 15.4673 | -114.1435 | 5.8909 | 151.8222 | 0.0017 | 0.0022 |
| 2024_09_20 22:00 | 3219507 | 2 | 14.7181 | 17.2969 | -117.8548 | 17.4849 | 193.8731 | 0.0073 | 0.0192 |
| 2024_09_20 22:00 | 3215150 | 3 | 5.8986 | 15.9336 | -115.2671 | 7.2227 | 113.5235 | 0.0132 | 0.0178 |
| 2024_09_20 22:00 | 3271207 | 4 | 12.6887 | 5.4134 | -115.5319 | 11.4222 | 150.9439 | 0.0188 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415520_B42C8FAC | 504990 | 737 | -87.3 | 504990 | 978 | -97.7 | 504990 | 44 | -96.4 | 504990 | 716 |
| MR_1774415520_CF73CC38 | 504990 | 737 | -87.9 | 504990 | 978 | -96.4 | 504990 | 44 | -98.1 | 504990 | 716 |
| MR_1774415520_EA574678 | 504990 | 737 | -89.4 | 504990 | 978 | -95.6 | 504990 | 44 | -96.7 | 504990 | 716 |
| MR_1774415520_E72CD2BB | 504990 | 737 | -88.5 | 504990 | 978 | -95.9 | 504990 | 44 | -96.5 | 504990 | 716 |
| MR_1774415520_0F50263A | 504990 | 737 | -89.5 | 504990 | 978 | -96.6 | 504990 | 44 | -97.7 | 504990 | 716 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 342: `b26f8458-b7b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b26f8458-b7b2-41cd-928e-ab04004a1527` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249873_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[342] topology](images/train_0342.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215534_6
- `C2`: Press down the tilt angle  of 3215534_6 by 5 degrees
- `C3`: Add neighbor relationship between 3249873_4 and 3215534_6
- `C4`: Adjust the azimuth of 3249873_4 by 37 degrees
- `C5`: Add neighbor relationship between 3229800_8 and 3215534_6
- `C6`: Increase A3 Offset threshold for 3215534_6
- `C7`: Increase transmission power for 3215534_6
- `C8`: Decrease transmission power for 3249873_4
- `C9`: Adjust the azimuth of 3215534_6 by 34 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase A3 Offset threshold for 3249873_4
- `C12`: Lift the tilt angle of 3249873_4 by 3 degrees
- `C13`: Lift the tilt angle  of 3215534_6 by 5 degrees
- `C14`: Increase transmission power for 3249873_4
- `C15`: Check test server and transmission issues
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215534_6
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249873_4
- `C18`: Decrease A3 Offset threshold for 3249873_4
- `C19`: Decrease A3 Offset threshold for 3215534_6
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249873_4 **← 정답**
- `C21`: Press down the tilt angle of 3249873_4 by 3 degrees
- `C22`: Decrease transmission power for 3215534_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.244 | MS1 | 121.4656604181 | 31.1446227254 | 783 | 504990 | -93.67 | 12.00 | 558.13 | 0.19 | 2.87 | 1577 |
| 2024-09-20 22:21:32.777 | MS1 | 121.4656591902 | 31.1446200111 | 279 | 504990 | -94.94 | 14.92 | 472.78 | 0.15 | 2.90 | 1567 |
| 2024-09-20 22:21:33.475 | MS1 | 121.4656586089 | 31.1446237967 | 161 | 504990 | -94.49 | 13.14 | 386.85 | 0.02 | 2.29 | 1572 |
| 2024-09-20 22:21:34.449 | MS1 | 121.4656666016 | 31.1446193507 | 142 | 152650 | -93.98 | 6.83 | 102.07 | 0.13 | 1.69 | 918 |
| 2024-09-20 22:21:35.301 | MS1 | 121.4656624750 | 31.1446185756 | 31 | 152650 | -90.34 | 5.47 | 83.76 | 0.04 | 1.95 | 956 |
| 2024-09-20 22:21:36.940 | MS1 | 121.4656709668 | 31.1446223108 | 613 | 152650 | -93.15 | 7.71 | 87.69 | 0.17 | 1.84 | 945 |
| 2024-09-20 22:21:37.922 | MS1 | 121.4656650535 | 31.1446328630 | 526 | 152650 | -94.49 | 6.25 | 49.92 | 0.13 | 1.68 | 927 |
| 2024-09-20 22:21:38.302 | MS1 | 121.4656715286 | 31.1446305561 | 142 | 152650 | -87.69 | 4.79 | 77.97 | 0.04 | 1.79 | 989 |
| 2024-09-20 22:21:39.449 | MS1 | 121.4656759914 | 31.1446274378 | 31 | 152650 | -87.84 | 7.71 | 56.94 | 0.00 | 1.84 | 921 |
| 2024-09-20 22:21:40.930 | MS1 | 121.4656765138 | 31.1446243047 | 613 | 152650 | -94.09 | 2.82 | 94.67 | 0.08 | 2.57 | 1582 |
| 2024-09-20 22:21:41.927 | MS1 | 121.4656726269 | 31.1446246366 | 526 | 152650 | -94.38 | 5.31 | 56.09 | 0.04 | 2.90 | 1593 |
| 2024-09-20 22:21:42.487 | MS1 | 121.4656749367 | 31.1446327014 | 142 | 152650 | -88.33 | 6.25 | 45.03 | 0.05 | 2.61 | 1578 |

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
| 3215534 | 6 | 121.4748497094 | 31.1533720341 | 256 | 4 | 2 | 16.4 | TDD | 217 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3217151 | 9 | 121.4685339571 | 31.1481258633 | 358 | 14 | 11 | 18.9 | FDD | 526 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3226483 | 11 | 121.4747182707 | 31.1459165018 | 331 | 7 | 0 | 3.6 | FDD | 797 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3229800 | 8 | 121.4756509129 | 31.1554162220 | 185 | 7 | 7 | 19.5 | FDD | 613 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3242947 | 12 | 121.4725223741 | 31.1538144993 | 210 | 5 | 4 | 4.8 | FDD | 894 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3249873 | 4 | 121.4693512300 | 31.1538963518 | 236 | 2 | 6 | 18.5 | TDD | 783 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3258552 | 10 | 121.4668008753 | 31.1465005231 | 90 | 2 | 4 | 10.3 | FDD | 142 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3261739 | 13 | 121.4679795640 | 31.1455473260 | 108 | 11 | 8 | 15.1 | FDD | 31 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3263645 | 7 | 121.4712568630 | 31.1509109568 | 141 | 10 | 10 | 19.2 | FDD | 896 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3265866 | 5 | 121.4696133566 | 31.1457581787 | 182 | 8 | 10 | 23.3 | TDD | 279 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3271785 | 3 | 121.4673326344 | 31.1534435968 | 15 | 14 | 9 | 2.0 | TDD | 587 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3275935 | 1 | 121.4702589545 | 31.1452639838 | 80 | 9 | 1 | 7.4 | TDD | 161 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3276949 | 2 | 121.4654809346 | 31.1547641672 | 108 | 8 | 7 | 20.5 | TDD | 614 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.349 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.371 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.512 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.512 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.150 | NREventA2 | measId:1;ServCellPCI:21;Ser... |
| 2024-09-20 22:21:35.295 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.531 | NREventA5 | measId:3;ServCellPCI:21;Ser... |
| 2024-09-20 22:21:35.588 | NRHandoverAttempt | SourcePCI:21;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.610 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.625 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.761 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.761 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275935 | 1 | 6.7086 | 9.8224 | -114.3850 | 15.8566 | 113.3270 | 0.0120 | 0.0027 |
| 2024_09_20 22:00 | 3276949 | 2 | 15.3352 | 18.4224 | -117.5936 | 9.3710 | 179.1559 | 0.0119 | 0.0087 |
| 2024_09_20 22:00 | 3271785 | 3 | 7.5340 | 8.7512 | -117.4171 | 13.2331 | 139.2124 | 0.0008 | 0.0012 |
| 2024_09_20 22:00 | 3249873 | 4 | 19.6224 | 8.5459 | -115.4259 | 13.0575 | 118.5508 | 0.0102 | 0.0182 |
| 2024_09_20 22:00 | 3265866 | 5 | 5.4661 | 15.0929 | -114.4149 | 5.9927 | 105.7352 | 0.0114 | 0.0047 |
| 2024_09_20 22:00 | 3215534 | 6 | 8.9539 | 6.9189 | -117.5537 | 14.0829 | 86.6828 | 0.0009 | 0.0147 |
| 2024_09_20 22:00 | 3263645 | 7 | 18.2989 | 16.1155 | -116.5426 | 4.5813 | 42.5223 | 0.0019 | 0.0145 |
| 2024_09_20 22:00 | 3229800 | 8 | 15.7063 | 11.4725 | -115.5699 | 4.0705 | 45.8078 | 0.0029 | 0.0146 |
| 2024_09_20 22:00 | 3217151 | 9 | 17.2856 | 9.0022 | -114.7011 | 3.9070 | 33.3640 | 0.0170 | 0.0118 |
| 2024_09_20 22:00 | 3258552 | 10 | 13.6301 | 17.8795 | -117.7882 | 3.4624 | 31.7894 | 0.0059 | 0.0038 |
| 2024_09_20 22:00 | 3226483 | 11 | 19.9938 | 8.3563 | -116.6474 | 4.0799 | 56.6205 | 0.0082 | 0.0153 |
| 2024_09_20 22:00 | 3242947 | 12 | 13.0109 | 19.0674 | -117.6649 | 4.6063 | 58.4180 | 0.0113 | 0.0161 |
| 2024_09_20 22:00 | 3261739 | 13 | 6.2516 | 8.7652 | -115.0259 | 4.6113 | 37.7288 | 0.0069 | 0.0159 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413893_A17B8C64 | 504990 | 161 | -95.6 | 504990 | 217 | -91.7 | 504990 | 614 | -96.7 | 504990 | 587 |
| MR_1774413893_281AB46F | 504990 | 161 | -93.8 | 504990 | 217 | -93.7 | 504990 | 614 | -94.0 | 504990 | 587 |
| MR_1774413893_57A32333 | 152650 | 31 | -88.7 | 152650 | 894 | -92.7 | 152650 | 797 | -100.9 | 152650 | 896 |
| MR_1774413893_3792E6AF | 504990 | 161 | -92.9 | 504990 | 217 | -93.8 | 504990 | 614 | -96.9 | 504990 | 587 |
| MR_1774413893_C9FB8018 | 152650 | 31 | -90.0 | 152650 | 894 | -94.9 | 152650 | 797 | -100.8 | 152650 | 896 |
| MR_1774413893_FC13A73D | 152650 | 31 | -91.0 | 152650 | 894 | -92.9 | 152650 | 797 | -102.7 | 152650 | 896 |
| MR_1774413893_BC8B1A08 | 504990 | 161 | -96.4 | 504990 | 217 | -93.7 | 504990 | 614 | -93.9 | 504990 | 587 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 343: `82527a90-142...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `82527a90-1426-4b6d-84b6-32f880dde461` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[343] topology](images/train_0343.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3256075_1
- `C2`: Increase transmission power for 3256075_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256075_1
- `C4`: Lift the tilt angle  of 3256075_1 by 3 degrees
- `C5`: Increase A3 Offset threshold for 3256075_1
- `C6`: Decrease transmission power for 3235006_3
- `C7`: Increase transmission power for 3235006_3
- `C8`: Decrease A3 Offset threshold for 3235006_3
- `C9`: Decrease transmission power for 3256075_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235006_3
- `C11`: Insufficient data; more data is needed for judgment. **← 정답**
- `C12`: Increase A3 Offset threshold for 3235006_3
- `C13`: Adjust the azimuth of 3256075_1 by 50 degrees
- `C14`: Add neighbor relationship between 3269154_4 and 3256075_1
- `C15`: Press down the tilt angle  of 3256075_1 by 3 degrees
- `C16`: Check test server and transmission issues
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256075_1
- `C18`: Lift the tilt angle of 3235006_3 by 3 degrees
- `C19`: Add neighbor relationship between 3235006_3 and 3256075_1
- `C20`: Press down the tilt angle of 3235006_3 by 3 degrees
- `C21`: Adjust the azimuth of 3235006_3 by 30 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235006_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.630 | MS1 | 121.4656589239 | 31.1446219001 | 483 | 504990 | -86.37 | 16.78 | 552.60 | 0.02 | 2.40 | 1583 |
| 2024-09-20 22:21:32.875 | MS1 | 121.4656660863 | 31.1446256310 | 483 | 504990 | -87.82 | 15.79 | 596.34 | 0.04 | 2.63 | 1572 |
| 2024-09-20 22:21:33.913 | MS1 | 121.4656753393 | 31.1446199172 | 483 | 504990 | -89.54 | 16.96 | 328.50 | 0.01 | 2.14 | 1577 |
| 2024-09-20 22:21:34.158 | MS1 | 121.4656696604 | 31.1446320072 | 483 | 504990 | -90.47 | 17.39 | 103.50 | 0.07 | 2.32 | 1570 |
| 2024-09-20 22:21:35.840 | MS1 | 121.4656592648 | 31.1446270923 | 483 | 504990 | -86.38 | 16.94 | 53.97 | 0.05 | 2.43 | 1584 |
| 2024-09-20 22:21:36.477 | MS1 | 121.4656646994 | 31.1446251000 | 483 | 504990 | -88.06 | 15.57 | 57.47 | 0.09 | 2.87 | 1596 |
| 2024-09-20 22:21:37.805 | MS1 | 121.4656594501 | 31.1446281478 | 483 | 504990 | -92.28 | 10.17 | 80.86 | 0.01 | 2.54 | 1563 |
| 2024-09-20 22:21:38.659 | MS1 | 121.4656683191 | 31.1446322469 | 483 | 504990 | -89.19 | 7.32 | 61.34 | 0.12 | 2.79 | 1581 |
| 2024-09-20 22:21:39.229 | MS1 | 121.4656652083 | 31.1446245189 | 483 | 504990 | -89.53 | 8.23 | 66.97 | 0.11 | 2.22 | 1588 |
| 2024-09-20 22:21:40.848 | MS1 | 121.4656683233 | 31.1446314818 | 483 | 504990 | -90.27 | 8.11 | 295.17 | 0.14 | 2.18 | 1563 |
| 2024-09-20 22:21:41.379 | MS1 | 121.4656606082 | 31.1446360761 | 483 | 504990 | -89.65 | 12.14 | 322.84 | 0.19 | 2.06 | 1579 |
| 2024-09-20 22:21:42.840 | MS1 | 121.4656639567 | 31.1446341316 | 483 | 504990 | -92.25 | 7.77 | 316.40 | 0.10 | 2.35 | 1566 |

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
| 3235006 | 3 | 121.4747117206 | 31.1457353521 | 292 | 0 | 12 | 47.2 | TDD | 483 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3256075 | 1 | 121.4741851549 | 31.1500268065 | 15 | 1 | 3 | 39.4 | TDD | 153 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3269154 | 4 | 121.4689367526 | 31.1465841863 | 39 | 8 | 6 | 34.1 | TDD | 813 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3276186 | 2 | 121.4650823328 | 31.1485446878 | 111 | 9 | 10 | 32.4 | TDD | 722 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.956 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.975 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.099 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.099 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.794 | NREventA3 | measId:2;ServCellPCI:758;Se... |
| 2024-09-20 22:21:38.034 | NRHandoverAttempt | SourcePCI:758;SourceNR-ARFC... |
| 2024-09-20 22:21:38.079 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.090 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.235 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.235 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3256075 | 1 | 94.6380 | 93.9871 | -115.7843 | 15.6745 | 92.0378 | 0.0141 | 0.0183 |
| 2024_09_19 22:00 | 3276186 | 2 | 87.7832 | 79.6878 | -115.2700 | 10.7336 | 101.8486 | 0.0147 | 0.0166 |
| 2024_09_19 22:00 | 3235006 | 3 | 75.3133 | 90.9643 | -114.6743 | 17.6410 | 135.0323 | 0.0122 | 0.0085 |
| 2024_09_19 22:00 | 3269154 | 4 | 77.4214 | 80.1962 | -116.0976 | 9.9891 | 187.8588 | 0.0129 | 0.0120 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415957_34CC407A | 504990 | 483 | -86.3 | 504990 | 153 | -88.2 | 504990 | 813 | -93.3 | 504990 | 722 |
| MR_1774415957_F5973560 | 504990 | 483 | -87.1 | 504990 | 153 | -87.6 | 504990 | 813 | -93.9 | 504990 | 722 |
| MR_1774415957_7DBC9F9E | 504990 | 483 | -87.6 | 504990 | 153 | -85.5 | 504990 | 813 | -93.7 | 504990 | 722 |
| MR_1774415957_D5A040D3 | 504990 | 483 | -86.2 | 504990 | 153 | -87.3 | 504990 | 813 | -92.2 | 504990 | 722 |
| MR_1774415957_A53DE445 | 504990 | 483 | -85.2 | 504990 | 153 | -86.6 | 504990 | 813 | -94.5 | 504990 | 722 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 344: `6ebba336-3a3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6ebba336-3a38-47a7-8fa4-fed71dff077c` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[344] topology](images/train_0344.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3277148_1 by 10 degrees
- `C2`: Increase A3 Offset threshold for 3245743_4
- `C3`: Adjust the azimuth of 3277148_1 by 15 degrees
- `C4`: Check test server and transmission issues
- `C5`: Increase A3 Offset threshold for 3277148_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277148_1
- `C7`: Lift the tilt angle of 3245743_4 by 3 degrees
- `C8`: Add neighbor relationship between 3245743_4 and 3277148_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277148_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245743_4
- `C11`: Lift the tilt angle  of 3277148_1 by 10 degrees
- `C12`: Decrease A3 Offset threshold for 3245743_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245743_4
- `C14`: Insufficient data; more data is needed for judgment. **← 정답**
- `C15`: Adjust the azimuth of 3245743_4 by 50 degrees
- `C16`: Decrease transmission power for 3277148_1
- `C17`: Increase transmission power for 3277148_1
- `C18`: Decrease A3 Offset threshold for 3277148_1
- `C19`: Add neighbor relationship between 3251312_2 and 3277148_1
- `C20`: Decrease transmission power for 3245743_4
- `C21`: Press down the tilt angle of 3245743_4 by 3 degrees
- `C22`: Increase transmission power for 3245743_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.722 | MS1 | 121.4656581833 | 31.1446272618 | 860 | 504990 | -85.84 | 13.44 | 468.00 | 0.03 | 2.36 | 1579 |
| 2024-09-20 22:21:32.668 | MS1 | 121.4656599835 | 31.1446240627 | 860 | 504990 | -87.61 | 12.89 | 473.87 | 0.10 | 2.66 | 1568 |
| 2024-09-20 22:21:33.690 | MS1 | 121.4656581069 | 31.1446283921 | 860 | 504990 | -88.43 | 12.07 | 335.63 | 0.17 | 2.08 | 1587 |
| 2024-09-20 22:21:34.467 | MS1 | 121.4656735371 | 31.1446233271 | 860 | 504990 | -90.89 | 16.54 | 78.51 | 0.13 | 2.31 | 1586 |
| 2024-09-20 22:21:35.454 | MS1 | 121.4656616432 | 31.1446265768 | 860 | 504990 | -91.29 | 14.74 | 86.46 | 0.03 | 2.78 | 1565 |
| 2024-09-20 22:21:36.730 | MS1 | 121.4656597522 | 31.1446357526 | 860 | 504990 | -90.80 | 14.85 | 88.93 | 0.02 | 2.92 | 1581 |
| 2024-09-20 22:21:37.850 | MS1 | 121.4656586897 | 31.1446198202 | 860 | 504990 | -91.22 | 11.69 | 92.27 | 0.05 | 2.59 | 1577 |
| 2024-09-20 22:21:38.223 | MS1 | 121.4656669749 | 31.1446251371 | 860 | 504990 | -89.68 | 7.78 | 78.87 | 0.04 | 2.88 | 1567 |
| 2024-09-20 22:21:39.178 | MS1 | 121.4656732769 | 31.1446260341 | 860 | 504990 | -92.93 | 7.13 | 76.81 | 0.16 | 2.01 | 1568 |
| 2024-09-20 22:21:40.729 | MS1 | 121.4656771899 | 31.1446202992 | 860 | 504990 | -90.92 | 11.64 | 478.64 | 0.08 | 2.35 | 1574 |
| 2024-09-20 22:21:41.471 | MS1 | 121.4656616508 | 31.1446301090 | 860 | 504990 | -91.51 | 12.98 | 588.24 | 0.08 | 2.10 | 1562 |
| 2024-09-20 22:21:42.841 | MS1 | 121.4656614393 | 31.1446270364 | 860 | 504990 | -90.45 | 11.19 | 451.94 | 0.13 | 2.10 | 1596 |

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
| 3233716 | 3 | 121.4744375155 | 31.1489897900 | 139 | 7 | 0 | 41.0 | TDD | 153 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3245743 | 4 | 121.4705115148 | 31.1516800129 | 323 | 1 | 2 | 31.3 | TDD | 860 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3251312 | 2 | 121.4706165497 | 31.1528755335 | 62 | 15 | 8 | 27.7 | TDD | 98 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3277148 | 1 | 121.4671377246 | 31.1461718837 | 234 | 13 | 7 | 49.7 | TDD | 17 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.417 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.435 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.540 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.540 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.254 | NREventA3 | measId:2;ServCellPCI:151;Se... |
| 2024-09-20 22:21:38.494 | NRHandoverAttempt | SourcePCI:151;SourceNR-ARFC... |
| 2024-09-20 22:21:38.532 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.547 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.682 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.682 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3277148 | 1 | 90.0264 | 76.0547 | -115.5885 | 10.7278 | 179.8472 | 0.0151 | 0.0177 |
| 2024_09_19 22:00 | 3251312 | 2 | 86.2409 | 92.5983 | -114.9532 | 17.5001 | 80.9165 | 0.0162 | 0.0086 |
| 2024_09_19 22:00 | 3233716 | 3 | 79.2712 | 75.4519 | -115.4155 | 16.7250 | 105.8987 | 0.0033 | 0.0023 |
| 2024_09_19 22:00 | 3245743 | 4 | 75.5168 | 75.5706 | -116.2431 | 11.2837 | 169.0838 | 0.0117 | 0.0035 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415809_C75894A2 | 504990 | 860 | -91.3 | 504990 | 17 | -95.3 | 504990 | 98 | -97.9 | 504990 | 153 |
| MR_1774415809_31F077CA | 504990 | 860 | -91.0 | 504990 | 17 | -93.0 | 504990 | 98 | -96.7 | 504990 | 153 |
| MR_1774415809_2CFC0C12 | 504990 | 860 | -92.0 | 504990 | 17 | -94.3 | 504990 | 98 | -96.9 | 504990 | 153 |
| MR_1774415809_D1DF05D1 | 504990 | 860 | -92.7 | 504990 | 17 | -93.5 | 504990 | 98 | -97.0 | 504990 | 153 |
| MR_1774415809_609E09B4 | 504990 | 860 | -91.2 | 504990 | 17 | -94.4 | 504990 | 98 | -98.5 | 504990 | 153 |
| MR_1774415809_DD74EE4B | 504990 | 860 | -91.3 | 504990 | 17 | -96.8 | 504990 | 98 | -99.2 | 504990 | 153 |
| MR_1774415809_B9AC45A8 | 504990 | 860 | -91.5 | 504990 | 17 | -95.0 | 504990 | 98 | -100.2 | 504990 | 153 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 345: `bec47666-3e0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bec47666-3e02-4b40-9a24-b916bf9e6576` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Add neighbor relationship between 3263403_4 and 3227894_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[345] topology](images/train_0345.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3227894_1 by 38 degrees
- `C2`: Decrease transmission power for 3263403_4
- `C3`: Press down the tilt angle of 3263403_4 by 10 degrees
- `C4`: Decrease transmission power for 3227894_1
- `C5`: Decrease A3 Offset threshold for 3263403_4
- `C6`: Lift the tilt angle of 3263403_4 by 10 degrees
- `C7`: Adjust the azimuth of 3263403_4 by 12 degrees
- `C8`: Check test server and transmission issues
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227894_1
- `C10`: Lift the tilt angle  of 3227894_1 by 4 degrees
- `C11`: Increase transmission power for 3227894_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227894_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263403_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263403_4
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Increase transmission power for 3263403_4
- `C17`: Add neighbor relationship between 3263403_4 and 3227894_1 **← 정답**
- `C18`: Increase A3 Offset threshold for 3263403_4
- `C19`: Add neighbor relationship between 3270106_3 and 3227894_1
- `C20`: Increase A3 Offset threshold for 3227894_1
- `C21`: Decrease A3 Offset threshold for 3227894_1
- `C22`: Press down the tilt angle  of 3227894_1 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.855 | MS1 | 121.4656668494 | 31.1446217583 | 734 | 504990 | -80.97 | 12.97 | 549.89 | 0.01 | 2.80 | 1597 |
| 2024-09-20 22:21:32.733 | MS1 | 121.4656648827 | 31.1446224745 | 734 | 504990 | -80.56 | 16.50 | 436.31 | 0.07 | 2.63 | 1561 |
| 2024-09-20 22:21:33.410 | MS1 | 121.4656772761 | 31.1446244849 | 734 | 504990 | -78.61 | 15.88 | 355.65 | 0.03 | 2.91 | 1582 |
| 2024-09-20 22:21:34.221 | MS1 | 121.4656611025 | 31.1446313193 | 734 | 504990 | -91.48 | -2.88 | 39.36 | 0.18 | 1.37 | 1583 |
| 2024-09-20 22:21:35.148 | MS1 | 121.4656731842 | 31.1446237270 | 734 | 504990 | -89.53 | -2.68 | 50.46 | 0.17 | 1.04 | 1591 |
| 2024-09-20 22:21:36.269 | MS1 | 121.4656623135 | 31.1446183744 | 734 | 504990 | -91.97 | -1.84 | 24.68 | 0.10 | 1.08 | 1587 |
| 2024-09-20 22:21:37.972 | MS1 | 121.4656682705 | 31.1446196281 | 734 | 504990 | -87.95 | -1.95 | 34.97 | 0.08 | 1.07 | 1571 |
| 2024-09-20 22:21:38.122 | MS1 | 121.4656694589 | 31.1446346742 | 734 | 504990 | -83.39 | 17.99 | 488.91 | 0.15 | 1.30 | 1587 |
| 2024-09-20 22:21:39.237 | MS1 | 121.4656684470 | 31.1446303298 | 734 | 504990 | -76.93 | 14.61 | 398.41 | 0.18 | 1.03 | 1597 |
| 2024-09-20 22:21:40.562 | MS1 | 121.4656762093 | 31.1446335393 | 734 | 504990 | -75.78 | 16.52 | 581.83 | 0.10 | 2.56 | 1595 |
| 2024-09-20 22:21:41.324 | MS1 | 121.4656772682 | 31.1446305668 | 734 | 504990 | -82.77 | 14.08 | 543.43 | 0.18 | 2.87 | 1572 |
| 2024-09-20 22:21:42.278 | MS1 | 121.4656742881 | 31.1446335244 | 734 | 504990 | -79.02 | 13.00 | 422.41 | 0.09 | 2.73 | 1564 |

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
| 3227894 | 1 | 121.4733305235 | 31.1442002290 | 312 | 2 | 2 | 29.0 | TDD | 872 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3243348 | 2 | 121.4755117553 | 31.1487144295 | 33 | 2 | 7 | 43.7 | TDD | 690 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3263403 | 4 | 121.4747211517 | 31.1460084961 | 248 | 12 | 4 | 39.4 | TDD | 734 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3270106 | 3 | 121.4725733455 | 31.1534846776 | 233 | 4 | 1 | 43.2 | TDD | 315 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.043 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.062 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.189 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.189 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.864 | NREventA3 | measId:2;ServCellPCI:757;Se... |
| 2024-09-20 22:21:35.864 | NREventA3 | measId:2;ServCellPCI:757;Se... |
| 2024-09-20 22:21:36.864 | NREventA3 | measId:2;ServCellPCI:757;Se... |
| 2024-09-20 22:21:39.364 | NRRRCReestablishAttempt | PCI:757 |
| 2024-09-20 22:21:39.381 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.395 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.540 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.540 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227894 | 1 | 17.9876 | 7.0074 | -114.7278 | 15.2361 | 94.8889 | 0.0009 | 0.0197 |
| 2024_09_20 22:00 | 3243348 | 2 | 18.0397 | 11.4776 | -116.8577 | 10.1249 | 132.2812 | 0.0107 | 0.0187 |
| 2024_09_20 22:00 | 3270106 | 3 | 18.8576 | 17.4529 | -114.4350 | 6.7740 | 146.8347 | 0.0050 | 0.0118 |
| 2024_09_20 22:00 | 3263403 | 4 | 13.9541 | 17.7057 | -114.6974 | 16.0787 | 148.2097 | 0.0172 | 0.1168 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414322_72E653CB | 504990 | 872 | -86.9 | 504990 | 734 | -92.4 | 504990 | 315 | -95.0 | 504990 | 690 |
| MR_1774414322_CEB119CC | 504990 | 734 | -89.6 | 504990 | 872 | -87.2 | 504990 | 315 | -95.9 | 504990 | 690 |
| MR_1774414322_65B751CF | 504990 | 872 | -87.9 | 504990 | 734 | -89.8 | 504990 | 315 | -96.1 | 504990 | 690 |
| MR_1774414322_E71755A7 | 504990 | 734 | -90.7 | 504990 | 872 | -84.8 | 504990 | 315 | -96.6 | 504990 | 690 |
| MR_1774414322_BB1FA395 | 504990 | 872 | -85.4 | 504990 | 734 | -93.3 | 504990 | 315 | -93.1 | 504990 | 690 |
| MR_1774414322_7A6D2623 | 504990 | 872 | -85.8 | 504990 | 734 | -93.1 | 504990 | 315 | -93.8 | 504990 | 690 |
| MR_1774414322_EF24D875 | 504990 | 872 | -85.9 | 504990 | 734 | -90.9 | 504990 | 315 | -93.8 | 504990 | 690 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 346: `030d78b6-def...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `030d78b6-defa-46a5-bde3-223038552019` |
| Tag | **multiple-answer** |
| 정답 | **C12|C14** |
| C12 의미 | Increase transmission power for 3220121_1 |
| C14 의미 | Adjust the azimuth of 3220121_1 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[346] topology](images/train_0346.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3265806_4
- `C2`: Add neighbor relationship between 3220121_1 and 3265806_4
- `C3`: Increase A3 Offset threshold for 3220121_1
- `C4`: Press down the tilt angle  of 3265806_4 by 4 degrees
- `C5`: Check test server and transmission issues
- `C6`: Increase A3 Offset threshold for 3265806_4
- `C7`: Decrease transmission power for 3265806_4
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Adjust the azimuth of 3265806_4 by 44 degrees
- `C10`: Add neighbor relationship between 3272659_2 and 3265806_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265806_4
- `C12`: Increase transmission power for 3220121_1 **← 정답**
- `C13`: Lift the tilt angle of 3220121_1 by 10 degrees
- `C14`: Adjust the azimuth of 3220121_1 by 50 degrees **← 정답**
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220121_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220121_1
- `C17`: Decrease A3 Offset threshold for 3220121_1
- `C18`: Increase transmission power for 3265806_4
- `C19`: Decrease transmission power for 3220121_1
- `C20`: Lift the tilt angle  of 3265806_4 by 4 degrees
- `C21`: Press down the tilt angle of 3220121_1 by 10 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265806_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.273 | MS1 | 121.4656645621 | 31.1446224558 | 1001 | 504990 | -91.99 | 15.92 | 344.10 | 0.08 | 2.06 | 1591 |
| 2024-09-20 22:21:32.969 | MS1 | 121.4656631653 | 31.1446260425 | 1001 | 504990 | -86.50 | 16.01 | 310.98 | 0.06 | 2.51 | 1585 |
| 2024-09-20 22:21:33.366 | MS1 | 121.4656586667 | 31.1446243162 | 1001 | 504990 | -85.55 | 14.51 | 534.93 | 0.14 | 2.53 | 1581 |
| 2024-09-20 22:21:34.425 | MS1 | 121.4656722466 | 31.1446208870 | 1001 | 504990 | -106.78 | -0.49 | 62.39 | 0.10 | 1.17 | 1569 |
| 2024-09-20 22:21:35.168 | MS1 | 121.4656769016 | 31.1446355679 | 1001 | 504990 | -105.36 | 1.59 | 68.11 | 0.06 | 1.06 | 1591 |
| 2024-09-20 22:21:36.835 | MS1 | 121.4656778263 | 31.1446284668 | 1001 | 504990 | -105.61 | -1.07 | 29.85 | 0.12 | 1.25 | 1579 |
| 2024-09-20 22:21:37.176 | MS1 | 121.4656581071 | 31.1446194298 | 1001 | 504990 | -108.31 | 1.13 | 78.67 | 0.06 | 1.35 | 1592 |
| 2024-09-20 22:21:38.578 | MS1 | 121.4656669531 | 31.1446278433 | 1001 | 504990 | -100.30 | -1.46 | 36.96 | 0.04 | 1.17 | 1580 |
| 2024-09-20 22:21:39.301 | MS1 | 121.4656685496 | 31.1446332935 | 1001 | 504990 | -100.02 | 1.34 | 58.06 | 0.19 | 1.43 | 1597 |
| 2024-09-20 22:21:40.814 | MS1 | 121.4656777804 | 31.1446272243 | 1001 | 504990 | -93.70 | 16.92 | 570.57 | 0.11 | 2.64 | 1563 |
| 2024-09-20 22:21:41.507 | MS1 | 121.4656620666 | 31.1446276855 | 1001 | 504990 | -90.47 | 17.90 | 392.31 | 0.12 | 2.19 | 1574 |
| 2024-09-20 22:21:42.901 | MS1 | 121.4656626759 | 31.1446194798 | 1001 | 504990 | -86.62 | 14.92 | 485.60 | 0.08 | 2.59 | 1568 |

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
| 3220121 | 1 | 121.4647681688 | 31.1468263106 | 100 | 6 | 11 | 30.5 | TDD | 1001 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3240143 | 3 | 121.4698795734 | 31.1543889094 | 343 | 14 | 1 | 18.3 | TDD | 174 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3265806 | 4 | 121.4728246912 | 31.1543940693 | 168 | 3 | 12 | 32.4 | TDD | 606 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3272659 | 2 | 121.4681884696 | 31.1464474809 | 201 | 0 | 8 | 47.0 | TDD | 842 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.507 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.526 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.666 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.666 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.823 | NREventA2 | measId:1;ServCellPCI:763;Se... |
| 2024-09-20 22:21:34.967 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220121 | 1 | 18.2489 | 19.2837 | -115.1291 | 19.1563 | 139.3338 | 0.1705 | 0.0114 |
| 2024_09_20 22:00 | 3272659 | 2 | 6.1009 | 6.4880 | -114.1559 | 16.1673 | 119.9552 | 0.0161 | 0.0077 |
| 2024_09_20 22:00 | 3240143 | 3 | 15.8039 | 15.0980 | -114.8607 | 13.6291 | 122.2420 | 0.0112 | 0.0072 |
| 2024_09_20 22:00 | 3265806 | 4 | 7.9839 | 14.9674 | -116.6887 | 19.2702 | 109.2072 | 0.0105 | 0.0020 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415920_50928E25 | 504990 | 1001 | -108.2 | 504990 | 606 | -110.8 | 504990 | 842 | -118.5 | 504990 | 174 |
| MR_1774415920_145F35FD | 504990 | 1001 | -105.3 | 504990 | 606 | -110.1 | 504990 | 842 | -117.0 | 504990 | 174 |
| MR_1774415920_FB389C01 | 504990 | 1001 | -105.9 | 504990 | 606 | -112.1 | 504990 | 842 | -119.0 | 504990 | 174 |
| MR_1774415920_E9D6417F | 504990 | 1001 | -107.9 | 504990 | 606 | -112.2 | 504990 | 842 | -119.4 | 504990 | 174 |
| MR_1774415920_0BBEEB5D | 504990 | 1001 | -104.8 | 504990 | 606 | -111.8 | 504990 | 842 | -117.5 | 504990 | 174 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 347: `6de715ec-0bc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6de715ec-0bcf-4be3-930d-3601e2d9e4b7` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Add neighbor relationship between 3215200_2 and 3234338_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[347] topology](images/train_0347.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3215200_2
- `C2`: Lift the tilt angle  of 3234338_1 by 6 degrees
- `C3`: Adjust the azimuth of 3215200_2 by 46 degrees
- `C4`: Decrease A3 Offset threshold for 3234338_1
- `C5`: Press down the tilt angle  of 3234338_1 by 6 degrees
- `C6`: Decrease transmission power for 3234338_1
- `C7`: Check test server and transmission issues
- `C8`: Press down the tilt angle of 3215200_2 by 10 degrees
- `C9`: Lift the tilt angle of 3215200_2 by 10 degrees
- `C10`: Add neighbor relationship between 3262164_3 and 3234338_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215200_2
- `C12`: Increase A3 Offset threshold for 3215200_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234338_1
- `C14`: Increase A3 Offset threshold for 3234338_1
- `C15`: Adjust the azimuth of 3234338_1 by 46 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Add neighbor relationship between 3215200_2 and 3234338_1 **← 정답**
- `C18`: Decrease A3 Offset threshold for 3215200_2
- `C19`: Increase transmission power for 3234338_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234338_1
- `C21`: Decrease transmission power for 3215200_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215200_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.414 | MS1 | 121.4656665251 | 31.1446199830 | 493 | 504990 | -82.28 | 16.94 | 428.78 | 0.09 | 2.78 | 1594 |
| 2024-09-20 22:21:32.445 | MS1 | 121.4656725596 | 31.1446372263 | 493 | 504990 | -76.06 | 16.83 | 465.25 | 0.06 | 2.08 | 1583 |
| 2024-09-20 22:21:33.137 | MS1 | 121.4656638799 | 31.1446318496 | 493 | 504990 | -76.26 | 17.50 | 589.58 | 0.16 | 2.55 | 1569 |
| 2024-09-20 22:21:34.785 | MS1 | 121.4656601021 | 31.1446339297 | 493 | 504990 | -87.21 | -3.48 | 48.29 | 0.03 | 1.48 | 1590 |
| 2024-09-20 22:21:35.265 | MS1 | 121.4656726090 | 31.1446244682 | 493 | 504990 | -85.54 | -2.26 | 65.22 | 0.03 | 1.25 | 1574 |
| 2024-09-20 22:21:36.842 | MS1 | 121.4656603911 | 31.1446251429 | 493 | 504990 | -85.17 | -0.91 | 41.04 | 0.11 | 1.17 | 1582 |
| 2024-09-20 22:21:37.793 | MS1 | 121.4656710944 | 31.1446336708 | 493 | 504990 | -92.03 | -1.99 | 47.70 | 0.11 | 1.16 | 1599 |
| 2024-09-20 22:21:38.243 | MS1 | 121.4656707161 | 31.1446222885 | 493 | 504990 | -79.25 | 14.90 | 326.93 | 0.18 | 1.46 | 1563 |
| 2024-09-20 22:21:39.548 | MS1 | 121.4656756514 | 31.1446243494 | 493 | 504990 | -81.40 | 17.81 | 418.05 | 0.01 | 1.15 | 1600 |
| 2024-09-20 22:21:40.777 | MS1 | 121.4656678994 | 31.1446251210 | 493 | 504990 | -80.99 | 14.80 | 443.92 | 0.03 | 2.17 | 1586 |
| 2024-09-20 22:21:41.874 | MS1 | 121.4656580207 | 31.1446318976 | 493 | 504990 | -84.38 | 16.29 | 486.11 | 0.03 | 2.53 | 1565 |
| 2024-09-20 22:21:42.789 | MS1 | 121.4656655935 | 31.1446374970 | 493 | 504990 | -79.20 | 13.58 | 478.44 | 0.19 | 2.19 | 1579 |

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
| 3215200 | 2 | 121.4746610942 | 31.1521871939 | 180 | 13 | 10 | 25.9 | TDD | 493 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3234338 | 1 | 121.4728191980 | 31.1446217562 | 316 | 2 | 10 | 42.5 | TDD | 976 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3236670 | 4 | 121.4657511763 | 31.1485327928 | 275 | 12 | 11 | 35.2 | TDD | 693 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3262164 | 3 | 121.4758809088 | 31.1534197397 | 166 | 0 | 8 | 30.7 | TDD | 254 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.557 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.577 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.700 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.700 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.436 | NREventA3 | measId:2;ServCellPCI:700;Se... |
| 2024-09-20 22:21:36.436 | NREventA3 | measId:2;ServCellPCI:700;Se... |
| 2024-09-20 22:21:37.436 | NREventA3 | measId:2;ServCellPCI:700;Se... |
| 2024-09-20 22:21:39.936 | NRRRCReestablishAttempt | PCI:700 |
| 2024-09-20 22:21:39.951 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.963 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:40.090 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.090 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234338 | 1 | 5.5942 | 6.2034 | -114.4055 | 8.7774 | 102.9115 | 0.0022 | 0.0157 |
| 2024_09_20 22:00 | 3215200 | 2 | 18.5172 | 7.1237 | -114.9764 | 12.9647 | 167.6060 | 0.0042 | 0.1291 |
| 2024_09_20 22:00 | 3262164 | 3 | 18.1863 | 11.4390 | -114.1259 | 11.6620 | 155.8186 | 0.0162 | 0.0194 |
| 2024_09_20 22:00 | 3236670 | 4 | 11.4055 | 9.8680 | -117.2339 | 9.4227 | 155.7860 | 0.0092 | 0.0109 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414442_0AD54B5F | 504990 | 493 | -89.0 | 504990 | 976 | -83.3 | 504990 | 254 | -91.2 | 504990 | 693 |
| MR_1774414442_06B520EE | 504990 | 493 | -87.6 | 504990 | 976 | -82.9 | 504990 | 254 | -88.6 | 504990 | 693 |
| MR_1774414442_D387F707 | 504990 | 976 | -82.6 | 504990 | 493 | -86.8 | 504990 | 254 | -90.0 | 504990 | 693 |
| MR_1774414442_FE736FBC | 504990 | 976 | -81.1 | 504990 | 493 | -88.9 | 504990 | 254 | -91.5 | 504990 | 693 |
| MR_1774414442_939B52DD | 504990 | 976 | -81.2 | 504990 | 493 | -86.2 | 504990 | 254 | -87.7 | 504990 | 693 |
| MR_1774414442_7764442F | 504990 | 976 | -84.3 | 504990 | 493 | -88.8 | 504990 | 254 | -91.0 | 504990 | 693 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 348: `70063ca3-d21...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `70063ca3-d21e-4749-a20b-e4bd0deab698` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263438_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[348] topology](images/train_0348.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Check test server and transmission issues
- `C3`: Add neighbor relationship between 3253141_13 and 3254628_3
- `C4`: Decrease transmission power for 3254628_3
- `C5`: Press down the tilt angle  of 3254628_3 by 6 degrees
- `C6`: Increase A3 Offset threshold for 3254628_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263438_2
- `C8`: Decrease A3 Offset threshold for 3263438_2
- `C9`: Add neighbor relationship between 3263438_2 and 3254628_3
- `C10`: Decrease transmission power for 3263438_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254628_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263438_2 **← 정답**
- `C13`: Increase transmission power for 3254628_3
- `C14`: Lift the tilt angle  of 3254628_3 by 6 degrees
- `C15`: Adjust the azimuth of 3254628_3 by 21 degrees
- `C16`: Lift the tilt angle of 3263438_2 by 0 degrees
- `C17`: Press down the tilt angle of 3263438_2 by 0 degrees
- `C18`: Increase transmission power for 3263438_2
- `C19`: Increase A3 Offset threshold for 3263438_2
- `C20`: Decrease A3 Offset threshold for 3254628_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254628_3
- `C22`: Adjust the azimuth of 3263438_2 by 49 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.695 | MS1 | 121.4656720508 | 31.1446316210 | 836 | 504990 | -95.22 | 12.08 | 575.94 | 0.01 | 2.37 | 1593 |
| 2024-09-20 22:21:32.171 | MS1 | 121.4656633955 | 31.1446199901 | 445 | 504990 | -94.52 | 13.94 | 370.25 | 0.15 | 2.86 | 1581 |
| 2024-09-20 22:21:33.224 | MS1 | 121.4656585982 | 31.1446320346 | 91 | 504990 | -93.68 | 13.25 | 331.05 | 0.17 | 2.84 | 1581 |
| 2024-09-20 22:21:34.329 | MS1 | 121.4656761161 | 31.1446189910 | 56 | 152650 | -93.82 | 6.95 | 78.10 | 0.09 | 1.51 | 966 |
| 2024-09-20 22:21:35.333 | MS1 | 121.4656602746 | 31.1446301476 | 962 | 152650 | -93.12 | 6.00 | 92.87 | 0.04 | 1.76 | 979 |
| 2024-09-20 22:21:36.167 | MS1 | 121.4656588537 | 31.1446187654 | 830 | 152650 | -91.56 | 6.02 | 81.44 | 0.09 | 1.88 | 900 |
| 2024-09-20 22:21:37.869 | MS1 | 121.4656695509 | 31.1446341804 | 365 | 152650 | -94.70 | 5.90 | 96.83 | 0.05 | 1.86 | 976 |
| 2024-09-20 22:21:38.503 | MS1 | 121.4656616787 | 31.1446376111 | 56 | 152650 | -87.49 | 3.79 | 63.18 | 0.14 | 1.56 | 913 |
| 2024-09-20 22:21:39.630 | MS1 | 121.4656685825 | 31.1446212939 | 962 | 152650 | -89.90 | 7.23 | 102.76 | 0.07 | 1.76 | 988 |
| 2024-09-20 22:21:40.903 | MS1 | 121.4656714072 | 31.1446258254 | 830 | 152650 | -91.48 | 6.77 | 67.34 | 0.19 | 2.37 | 1584 |
| 2024-09-20 22:21:41.171 | MS1 | 121.4656696280 | 31.1446378449 | 365 | 152650 | -88.95 | 4.82 | 95.66 | 0.05 | 2.98 | 1573 |
| 2024-09-20 22:21:42.446 | MS1 | 121.4656772809 | 31.1446200568 | 56 | 152650 | -96.73 | 3.70 | 75.72 | 0.09 | 2.82 | 1584 |

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
| 3214130 | 11 | 121.4702824881 | 31.1454570219 | 343 | 14 | 6 | 26.2 | FDD | 854 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3218792 | 7 | 121.4751534148 | 31.1513338163 | 0 | 6 | 2 | 13.6 | FDD | 962 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3225764 | 6 | 121.4737262804 | 31.1506840013 | 231 | 1 | 2 | 10.9 | TDD | 445 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3228241 | 4 | 121.4670158426 | 31.1521471232 | 233 | 12 | 10 | 9.8 | TDD | 391 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3237767 | 5 | 121.4745230437 | 31.1556891151 | 91 | 0 | 8 | 18.0 | TDD | 91 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3242212 | 9 | 121.4693672556 | 31.1446574149 | 25 | 7 | 4 | 18.7 | FDD | 52 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3246785 | 1 | 121.4674468456 | 31.1463458812 | 164 | 1 | 5 | 12.1 | TDD | 290 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3253141 | 13 | 121.4695131992 | 31.1495736752 | 310 | 6 | 2 | 18.8 | FDD | 830 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3254628 | 3 | 121.4683839010 | 31.1538100487 | 173 | 5 | 10 | 13.5 | TDD | 838 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3263438 | 2 | 121.4757128712 | 31.1549107747 | 171 | 0 | 12 | 9.2 | TDD | 836 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3271367 | 8 | 121.4676213308 | 31.1496784003 | 290 | 0 | 10 | 24.2 | FDD | 365 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3273678 | 10 | 121.4683134964 | 31.1495641173 | 144 | 8 | 7 | 13.0 | FDD | 533 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3277917 | 12 | 121.4704111564 | 31.1546334014 | 326 | 2 | 9 | 29.4 | FDD | 56 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |

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
| 2024-09-20 22:21:31.427 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.443 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.575 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.575 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.235 | NREventA2 | measId:1;ServCellPCI:336;Se... |
| 2024-09-20 22:21:35.336 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.614 | NREventA5 | measId:3;ServCellPCI:336;Se... |
| 2024-09-20 22:21:35.684 | NRHandoverAttempt | SourcePCI:336;SourceNR-ARFC... |
| 2024-09-20 22:21:35.707 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.722 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.831 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.831 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246785 | 1 | 12.7045 | 16.5908 | -115.8620 | 11.5633 | 154.3462 | 0.0168 | 0.0002 |
| 2024_09_20 22:00 | 3263438 | 2 | 10.4636 | 14.3286 | -117.2863 | 12.8485 | 159.5725 | 0.0075 | 0.0067 |
| 2024_09_20 22:00 | 3254628 | 3 | 9.9311 | 14.7053 | -117.6275 | 6.6586 | 106.8145 | 0.0080 | 0.0101 |
| 2024_09_20 22:00 | 3228241 | 4 | 19.5075 | 9.2968 | -116.8010 | 16.7196 | 107.3189 | 0.0161 | 0.0030 |
| 2024_09_20 22:00 | 3237767 | 5 | 14.0829 | 11.4734 | -115.7148 | 16.1782 | 190.8830 | 0.0010 | 0.0197 |
| 2024_09_20 22:00 | 3225764 | 6 | 17.5358 | 5.7307 | -117.7579 | 7.9642 | 102.2701 | 0.0083 | 0.0100 |
| 2024_09_20 22:00 | 3218792 | 7 | 15.2972 | 13.2150 | -114.0403 | 4.2102 | 53.4538 | 0.0074 | 0.0001 |
| 2024_09_20 22:00 | 3271367 | 8 | 11.9116 | 16.5030 | -114.2631 | 4.4787 | 47.0724 | 0.0148 | 0.0033 |
| 2024_09_20 22:00 | 3242212 | 9 | 5.0446 | 12.9609 | -117.6646 | 4.7758 | 49.3321 | 0.0083 | 0.0056 |
| 2024_09_20 22:00 | 3273678 | 10 | 10.9446 | 19.4946 | -117.8968 | 3.9945 | 51.4474 | 0.0009 | 0.0149 |
| 2024_09_20 22:00 | 3214130 | 11 | 5.9697 | 11.9909 | -115.8315 | 4.0454 | 24.5083 | 0.0031 | 0.0005 |
| 2024_09_20 22:00 | 3277917 | 12 | 6.8544 | 8.3145 | -117.1306 | 3.3467 | 45.2389 | 0.0175 | 0.0161 |
| 2024_09_20 22:00 | 3253141 | 13 | 6.5399 | 10.3852 | -117.1163 | 3.4731 | 59.9946 | 0.0077 | 0.0157 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415305_E3E608B6 | 504990 | 91 | -93.5 | 504990 | 838 | -96.9 | 504990 | 290 | -97.4 | 504990 | 391 |
| MR_1774415305_9B33720B | 504990 | 91 | -92.8 | 504990 | 838 | -96.0 | 504990 | 290 | -96.9 | 504990 | 391 |
| MR_1774415305_740FDCEC | 504990 | 91 | -92.1 | 504990 | 838 | -96.0 | 504990 | 290 | -95.3 | 504990 | 391 |
| MR_1774415305_E8463845 | 152650 | 56 | -92.7 | 152650 | 52 | -100.6 | 152650 | 854 | -102.9 | 152650 | 533 |
| MR_1774415305_E7589FF8 | 152650 | 56 | -94.5 | 152650 | 52 | -101.3 | 152650 | 854 | -100.8 | 152650 | 533 |
| MR_1774415305_3B9634F9 | 152650 | 56 | -94.7 | 152650 | 52 | -99.3 | 152650 | 854 | -102.3 | 152650 | 533 |
| MR_1774415305_FBBC2C10 | 504990 | 91 | -92.2 | 504990 | 838 | -94.2 | 504990 | 290 | -95.8 | 504990 | 391 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 349: `637a6ca6-8a5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `637a6ca6-8a5f-4248-80ef-d08cae85383c` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Add neighbor relationship between 3231274_1 and 3259876_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[349] topology](images/train_0349.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3251074_3 and 3259876_2
- `C2`: Decrease A3 Offset threshold for 3231274_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259876_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231274_1
- `C5`: Increase transmission power for 3259876_2
- `C6`: Decrease transmission power for 3231274_1
- `C7`: Check test server and transmission issues
- `C8`: Increase transmission power for 3231274_1
- `C9`: Decrease A3 Offset threshold for 3259876_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Lift the tilt angle  of 3259876_2 by 3 degrees
- `C12`: Increase A3 Offset threshold for 3259876_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259876_2
- `C14`: Add neighbor relationship between 3231274_1 and 3259876_2 **← 정답**
- `C15`: Adjust the azimuth of 3259876_2 by 3 degrees
- `C16`: Press down the tilt angle  of 3259876_2 by 3 degrees
- `C17`: Adjust the azimuth of 3231274_1 by 50 degrees
- `C18`: Lift the tilt angle of 3231274_1 by 9 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231274_1
- `C20`: Increase A3 Offset threshold for 3231274_1
- `C21`: Decrease transmission power for 3259876_2
- `C22`: Press down the tilt angle of 3231274_1 by 9 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.337 | MS1 | 121.4656604239 | 31.1446258365 | 328 | 504990 | -79.20 | 14.49 | 411.87 | 0.11 | 2.80 | 1594 |
| 2024-09-20 22:21:32.995 | MS1 | 121.4656715982 | 31.1446288515 | 328 | 504990 | -77.41 | 12.76 | 348.90 | 0.01 | 2.51 | 1589 |
| 2024-09-20 22:21:33.578 | MS1 | 121.4656697417 | 31.1446340672 | 328 | 504990 | -78.72 | 15.82 | 346.94 | 0.19 | 2.36 | 1581 |
| 2024-09-20 22:21:34.374 | MS1 | 121.4656774445 | 31.1446259241 | 328 | 504990 | -88.49 | -0.92 | 41.04 | 0.17 | 1.06 | 1569 |
| 2024-09-20 22:21:35.874 | MS1 | 121.4656683563 | 31.1446241749 | 328 | 504990 | -94.13 | -2.45 | 69.23 | 0.05 | 1.13 | 1570 |
| 2024-09-20 22:21:36.776 | MS1 | 121.4656714040 | 31.1446333837 | 328 | 504990 | -94.58 | -2.62 | 44.39 | 0.09 | 1.11 | 1568 |
| 2024-09-20 22:21:37.162 | MS1 | 121.4656683602 | 31.1446372749 | 328 | 504990 | -85.77 | -3.40 | 43.01 | 0.05 | 1.41 | 1572 |
| 2024-09-20 22:21:38.750 | MS1 | 121.4656586623 | 31.1446242233 | 328 | 504990 | -76.70 | 12.92 | 584.24 | 0.07 | 1.18 | 1588 |
| 2024-09-20 22:21:39.950 | MS1 | 121.4656592321 | 31.1446239131 | 328 | 504990 | -79.23 | 12.04 | 403.29 | 0.11 | 1.40 | 1561 |
| 2024-09-20 22:21:40.183 | MS1 | 121.4656601436 | 31.1446216952 | 328 | 504990 | -78.32 | 12.98 | 324.60 | 0.20 | 2.26 | 1568 |
| 2024-09-20 22:21:41.252 | MS1 | 121.4656718782 | 31.1446191638 | 328 | 504990 | -84.68 | 15.75 | 485.42 | 0.18 | 2.60 | 1590 |
| 2024-09-20 22:21:42.510 | MS1 | 121.4656705071 | 31.1446299683 | 328 | 504990 | -77.72 | 14.24 | 575.63 | 0.16 | 2.71 | 1570 |

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
| 3231274 | 1 | 121.4739178191 | 31.1508893124 | 298 | 7 | 7 | 38.8 | TDD | 328 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3251074 | 3 | 121.4704347894 | 31.1531823817 | 69 | 12 | 3 | 36.6 | TDD | 67 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3259876 | 2 | 121.4707466460 | 31.1512280335 | 216 | 2 | 5 | 19.1 | TDD | 73 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3277267 | 4 | 121.4724350549 | 31.1496632327 | 282 | 1 | 8 | 42.9 | TDD | 880 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.890 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.909 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.028 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.028 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.715 | NREventA3 | measId:2;ServCellPCI:744;Se... |
| 2024-09-20 22:21:35.715 | NREventA3 | measId:2;ServCellPCI:744;Se... |
| 2024-09-20 22:21:36.715 | NREventA3 | measId:2;ServCellPCI:744;Se... |
| 2024-09-20 22:21:39.215 | NRRRCReestablishAttempt | PCI:744 |
| 2024-09-20 22:21:39.231 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.241 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.376 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.376 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231274 | 1 | 11.2978 | 8.1053 | -117.2814 | 10.8820 | 176.9384 | 0.0187 | 0.1054 |
| 2024_09_20 22:00 | 3259876 | 2 | 6.1440 | 18.7457 | -116.8178 | 16.5639 | 108.9722 | 0.0109 | 0.0145 |
| 2024_09_20 22:00 | 3251074 | 3 | 8.7083 | 8.7593 | -115.2071 | 19.8590 | 180.9124 | 0.0078 | 0.0150 |
| 2024_09_20 22:00 | 3277267 | 4 | 10.6727 | 19.9666 | -114.3313 | 9.1155 | 193.8482 | 0.0039 | 0.0161 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415952_7CB88DAE | 504990 | 328 | -86.5 | 504990 | 73 | -82.5 | 504990 | 67 | -90.7 | 504990 | 880 |
| MR_1774415952_ADB7912D | 504990 | 328 | -87.3 | 504990 | 73 | -82.0 | 504990 | 67 | -90.6 | 504990 | 880 |
| MR_1774415952_25DF1445 | 504990 | 328 | -88.0 | 504990 | 73 | -84.2 | 504990 | 67 | -92.8 | 504990 | 880 |
| MR_1774415952_FB118678 | 504990 | 328 | -87.8 | 504990 | 73 | -84.1 | 504990 | 67 | -90.9 | 504990 | 880 |
| MR_1774415952_B545A295 | 504990 | 73 | -83.4 | 504990 | 328 | -87.1 | 504990 | 67 | -91.7 | 504990 | 880 |
| MR_1774415952_0A7ECB73 | 504990 | 73 | -82.9 | 504990 | 328 | -89.1 | 504990 | 67 | -92.3 | 504990 | 880 |

> *... 2개 열 생략 (전체 14열)*

---
