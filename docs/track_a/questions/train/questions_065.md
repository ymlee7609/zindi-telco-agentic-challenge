# Track A 문제 분석 — train[640]~train[649]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[640] ~ train[649] (10개)

## 목차

1. [문제 640: `afb0ce7d-2cf...`](#640) — single-answer, 정답: C3
2. [문제 641: `af172816-b8f...`](#641) — single-answer, 정답: C6
3. [문제 642: `b4647e23-e81...`](#642) — single-answer, 정답: C3
4. [문제 643: `1d735987-1fa...`](#643) — single-answer, 정답: C4
5. [문제 644: `a9ab6d78-9e6...`](#644) — single-answer, 정답: C5
6. [문제 645: `6c392308-b1d...`](#645) — single-answer, 정답: C22
7. [문제 646: `d9b957d4-696...`](#646) — single-answer, 정답: C3
8. [문제 647: `81137def-c63...`](#647) — single-answer, 정답: C16
9. [문제 648: `7524fe86-3c5...`](#648) — multiple-answer, 정답: C7|C10
10. [문제 649: `4a884258-a48...`](#649) — single-answer, 정답: C19

---

### 문제 640: `afb0ce7d-2cf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `afb0ce7d-2cf3-4eb1-9de9-50d962c64af0` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3263837_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[640] topology](images/train_0640.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3236687_2 by 8 degrees
- `C2`: Press down the tilt angle of 3263837_4 by 5 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263837_4 **← 정답**
- `C4`: Add neighbor relationship between 3263837_4 and 3236687_2
- `C5`: Decrease A3 Offset threshold for 3263837_4
- `C6`: Decrease A3 Offset threshold for 3236687_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236687_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236687_2
- `C9`: Adjust the azimuth of 3236687_2 by 50 degrees
- `C10`: Add neighbor relationship between 3231331_1 and 3236687_2
- `C11`: Increase transmission power for 3236687_2
- `C12`: Check test server and transmission issues
- `C13`: Increase A3 Offset threshold for 3263837_4
- `C14`: Decrease transmission power for 3263837_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263837_4
- `C16`: Increase A3 Offset threshold for 3236687_2
- `C17`: Adjust the azimuth of 3263837_4 by 14 degrees
- `C18`: Lift the tilt angle  of 3236687_2 by 8 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Lift the tilt angle of 3263837_4 by 5 degrees
- `C21`: Increase transmission power for 3263837_4
- `C22`: Decrease transmission power for 3236687_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.537 | MS1 | 121.4656676313 | 31.1446292177 | 23 | 504990 | -87.61 | 13.29 | 321.71 | 0.01 | 2.52 | 1597 |
| 2024-09-20 22:21:32.573 | MS1 | 121.4656764117 | 31.1446341863 | 23 | 504990 | -89.59 | 17.23 | 444.28 | 0.04 | 2.40 | 1582 |
| 2024-09-20 22:21:33.580 | MS1 | 121.4656630980 | 31.1446307444 | 23 | 504990 | -91.93 | 15.14 | 491.92 | 0.08 | 2.67 | 1578 |
| 2024-09-20 22:21:34.724 | MS1 | 121.4656664720 | 31.1446266528 | 23 | 504990 | -88.61 | 16.69 | 90.99 | 0.62 | 2.98 | 650 |
| 2024-09-20 22:21:35.625 | MS1 | 121.4656641933 | 31.1446222579 | 23 | 504990 | -90.41 | 14.84 | 74.80 | 0.66 | 2.25 | 539 |
| 2024-09-20 22:21:36.607 | MS1 | 121.4656585963 | 31.1446207154 | 23 | 504990 | -90.33 | 15.59 | 46.41 | 0.54 | 2.13 | 686 |
| 2024-09-20 22:21:37.549 | MS1 | 121.4656768181 | 31.1446294520 | 23 | 504990 | -90.82 | 7.45 | 72.02 | 0.70 | 2.73 | 550 |
| 2024-09-20 22:21:38.357 | MS1 | 121.4656701717 | 31.1446267149 | 23 | 504990 | -92.01 | 9.84 | 73.11 | 0.65 | 2.62 | 671 |
| 2024-09-20 22:21:39.246 | MS1 | 121.4656676462 | 31.1446198920 | 23 | 504990 | -91.67 | 7.08 | 63.54 | 0.69 | 2.88 | 642 |
| 2024-09-20 22:21:40.114 | MS1 | 121.4656727280 | 31.1446244211 | 23 | 504990 | -91.62 | 7.73 | 341.17 | 0.19 | 2.29 | 1571 |
| 2024-09-20 22:21:41.746 | MS1 | 121.4656773741 | 31.1446222305 | 23 | 504990 | -89.90 | 10.20 | 424.25 | 0.07 | 2.07 | 1564 |
| 2024-09-20 22:21:42.973 | MS1 | 121.4656687737 | 31.1446375303 | 23 | 504990 | -91.80 | 9.17 | 372.62 | 0.15 | 2.26 | 1580 |

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
| 3231331 | 1 | 121.4717996848 | 31.1482925111 | 180 | 15 | 3 | 24.7 | TDD | 400 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3236687 | 2 | 121.4675867337 | 31.1478228425 | 357 | 3 | 5 | 37.0 | TDD | 154 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3238789 | 3 | 121.4728642407 | 31.1531212250 | 230 | 5 | 10 | 42.0 | TDD | 822 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3263837 | 4 | 121.4708819938 | 31.1493542888 | 209 | 3 | 3 | 28.9 | TDD | 23 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.274 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.294 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.421 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.421 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.152 | NREventA3 | measId:2;ServCellPCI:603;Se... |
| 2024-09-20 22:21:38.392 | NRHandoverAttempt | SourcePCI:603;SourceNR-ARFC... |
| 2024-09-20 22:21:38.438 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.452 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.576 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.576 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231331 | 1 | 12.0447 | 9.9030 | -117.4101 | 19.0141 | 192.4843 | 0.0187 | 0.0044 |
| 2024_09_20 22:00 | 3236687 | 2 | 17.3960 | 16.1071 | -117.6503 | 14.2137 | 126.2463 | 0.0091 | 0.0067 |
| 2024_09_20 22:00 | 3238789 | 3 | 8.9497 | 17.0985 | -116.4199 | 6.2522 | 112.7908 | 0.0130 | 0.0043 |
| 2024_09_20 22:00 | 3263837 | 4 | 11.7170 | 18.5062 | -115.6875 | 7.3767 | 155.3984 | 0.0146 | 0.0030 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412752_2135F314 | 504990 | 23 | -87.6 | 504990 | 154 | -90.9 | 504990 | 400 | -97.9 | 504990 | 822 |
| MR_1774412752_34B27249 | 504990 | 23 | -90.1 | 504990 | 154 | -90.0 | 504990 | 400 | -97.2 | 504990 | 822 |
| MR_1774412752_793F9BF9 | 504990 | 23 | -86.9 | 504990 | 154 | -93.0 | 504990 | 400 | -96.5 | 504990 | 822 |
| MR_1774412752_69AEBEC5 | 504990 | 23 | -86.6 | 504990 | 154 | -90.9 | 504990 | 400 | -97.0 | 504990 | 822 |
| MR_1774412752_E7CB83E2 | 504990 | 23 | -86.7 | 504990 | 154 | -93.4 | 504990 | 400 | -98.0 | 504990 | 822 |
| MR_1774412752_850CCEB7 | 504990 | 23 | -87.5 | 504990 | 154 | -91.6 | 504990 | 400 | -97.8 | 504990 | 822 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 641: `af172816-b8f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `af172816-b8f7-4589-bc87-5e1a11263a6b` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease A3 Offset threshold for 3217165_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[641] topology](images/train_0641.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3217165_4 by 10 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217165_4
- `C3`: Increase transmission power for 3217165_4
- `C4`: Increase A3 Offset threshold for 3235347_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217165_4
- `C6`: Decrease A3 Offset threshold for 3217165_4 **← 정답**
- `C7`: Decrease transmission power for 3217165_4
- `C8`: Decrease transmission power for 3235347_1
- `C9`: Increase transmission power for 3235347_1
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Lift the tilt angle  of 3235347_1 by 4 degrees
- `C12`: Add neighbor relationship between 3217165_4 and 3235347_1
- `C13`: Decrease A3 Offset threshold for 3235347_1
- `C14`: Press down the tilt angle of 3217165_4 by 10 degrees
- `C15`: Increase A3 Offset threshold for 3217165_4
- `C16`: Adjust the azimuth of 3217165_4 by 50 degrees
- `C17`: Add neighbor relationship between 3254461_3 and 3235347_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235347_1
- `C19`: Check test server and transmission issues
- `C20`: Adjust the azimuth of 3235347_1 by 50 degrees
- `C21`: Press down the tilt angle  of 3235347_1 by 4 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235347_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.206 | MS1 | 121.4656596031 | 31.1446308438 | 814 | 504990 | -82.14 | 15.60 | 554.20 | 0.19 | 2.92 | 1590 |
| 2024-09-20 22:21:32.536 | MS1 | 121.4656698384 | 31.1446374145 | 814 | 504990 | -81.04 | 16.37 | 440.71 | 0.10 | 2.32 | 1584 |
| 2024-09-20 22:21:33.907 | MS1 | 121.4656657314 | 31.1446187330 | 814 | 504990 | -75.99 | 14.17 | 366.18 | 0.08 | 2.48 | 1561 |
| 2024-09-20 22:21:34.414 | MS1 | 121.4656584637 | 31.1446255678 | 814 | 504990 | -84.57 | -2.32 | 71.59 | 0.18 | 1.36 | 1575 |
| 2024-09-20 22:21:35.649 | MS1 | 121.4656712568 | 31.1446215013 | 814 | 504990 | -85.48 | -0.15 | 72.96 | 0.14 | 1.48 | 1598 |
| 2024-09-20 22:21:36.341 | MS1 | 121.4656638342 | 31.1446262828 | 814 | 504990 | -84.06 | -2.24 | 84.03 | 0.17 | 1.08 | 1575 |
| 2024-09-20 22:21:37.380 | MS1 | 121.4656714528 | 31.1446296489 | 814 | 504990 | -89.63 | -1.78 | 65.29 | 0.05 | 1.45 | 1587 |
| 2024-09-20 22:21:38.554 | MS1 | 121.4656642410 | 31.1446344937 | 814 | 504990 | -83.69 | -0.31 | 66.84 | 0.02 | 1.11 | 1593 |
| 2024-09-20 22:21:39.822 | MS1 | 121.4656748041 | 31.1446239012 | 722 | 504990 | -80.26 | 15.61 | 195.80 | 0.10 | 1.36 | 1598 |
| 2024-09-20 22:21:40.621 | MS1 | 121.4656763831 | 31.1446369144 | 722 | 504990 | -80.71 | 15.53 | 473.08 | 0.12 | 2.61 | 1582 |
| 2024-09-20 22:21:41.391 | MS1 | 121.4656647440 | 31.1446261385 | 722 | 504990 | -84.93 | 12.37 | 376.14 | 0.20 | 2.84 | 1580 |
| 2024-09-20 22:21:42.480 | MS1 | 121.4656721105 | 31.1446185642 | 722 | 504990 | -77.96 | 14.84 | 578.56 | 0.12 | 2.66 | 1600 |

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
| 3217165 | 4 | 121.4746973516 | 31.1501293993 | 311 | 9 | 1 | 30.7 | TDD | 814 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3228733 | 2 | 121.4691362178 | 31.1501348399 | 198 | 12 | 9 | 41.5 | TDD | 651 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3235347 | 1 | 121.4716597490 | 31.1445068342 | 49 | 2 | 4 | 21.5 | TDD | 722 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3254461 | 3 | 121.4715286779 | 31.1453244471 | 194 | 0 | 11 | 38.9 | TDD | 508 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.781 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.801 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.917 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.917 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.606 | NREventA3 | measId:2;ServCellPCI:189;Se... |
| 2024-09-20 22:21:37.846 | NRHandoverAttempt | SourcePCI:189;SourceNR-ARFC... |
| 2024-09-20 22:21:37.890 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.900 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.037 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.037 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235347 | 1 | 11.2257 | 7.5787 | -116.4108 | 15.0759 | 102.3352 | 0.0017 | 0.0077 |
| 2024_09_20 22:00 | 3228733 | 2 | 6.8746 | 8.4441 | -116.7430 | 7.5538 | 199.9061 | 0.0001 | 0.0003 |
| 2024_09_20 22:00 | 3254461 | 3 | 5.5713 | 18.3311 | -115.5385 | 12.3128 | 98.1765 | 0.0018 | 0.0028 |
| 2024_09_20 22:00 | 3217165 | 4 | 8.0499 | 11.6506 | -116.7740 | 13.7008 | 147.0428 | 0.0160 | 0.1588 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412714_8F0F0A71 | 504990 | 814 | -84.1 | 504990 | 722 | -80.9 | 504990 | 508 | -84.4 | 504990 | 651 |
| MR_1774412714_137631E0 | 504990 | 722 | -81.3 | 504990 | 814 | -84.9 | 504990 | 508 | -81.5 | 504990 | 651 |
| MR_1774412714_52BDFDA1 | 504990 | 722 | -79.6 | 504990 | 814 | -86.5 | 504990 | 508 | -81.9 | 504990 | 651 |
| MR_1774412714_AF3A2B82 | 504990 | 814 | -86.3 | 504990 | 722 | -78.9 | 504990 | 508 | -85.1 | 504990 | 651 |
| MR_1774412714_993355AA | 504990 | 722 | -78.4 | 504990 | 814 | -85.8 | 504990 | 508 | -81.6 | 504990 | 651 |
| MR_1774412714_9D0A22C4 | 504990 | 722 | -80.6 | 504990 | 814 | -85.5 | 504990 | 508 | -83.3 | 504990 | 651 |
| MR_1774412714_73D0763D | 504990 | 722 | -80.4 | 504990 | 814 | -82.6 | 504990 | 508 | -83.0 | 504990 | 651 |
| MR_1774412714_674E9196 | 504990 | 722 | -79.7 | 504990 | 814 | -83.6 | 504990 | 508 | -84.3 | 504990 | 651 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 642: `b4647e23-e81...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b4647e23-e81d-405b-9df5-fe78bae13d9d` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Lift the tilt angle  of 3267753_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[642] topology](images/train_0642.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3263049_3 by 7 degrees
- `C2`: Decrease A3 Offset threshold for 3263049_3
- `C3`: Lift the tilt angle  of 3267753_2 by 10 degrees **← 정답**
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251843_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase A3 Offset threshold for 3251843_1
- `C7`: Increase transmission power for 3251843_1
- `C8`: Check test server and transmission issues
- `C9`: Add neighbor relationship between 3263049_3 and 3251843_1
- `C10`: Lift the tilt angle of 3263049_3 by 2 degrees
- `C11`: Press down the tilt angle of 3263049_3 by 2 degrees
- `C12`: Decrease transmission power for 3251843_1
- `C13`: Adjust the azimuth of 3267753_2 by 50 degrees
- `C14`: Add neighbor relationship between 3267753_2 and 3251843_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263049_3
- `C16`: Increase transmission power for 3263049_3
- `C17`: Increase A3 Offset threshold for 3263049_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251843_1
- `C19`: Decrease transmission power for 3263049_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263049_3
- `C21`: Decrease A3 Offset threshold for 3251843_1
- `C22`: Press down the tilt angle  of 3267753_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.633 | MS1 | 121.4656608608 | 31.1446310728 | 230 | 504990 | -85.32 | 13.44 | 551.96 | 0.11 | 2.83 | 1574 |
| 2024-09-20 22:21:32.493 | MS1 | 121.4656765917 | 31.1446258543 | 230 | 504990 | -86.44 | 13.17 | 403.02 | 0.18 | 2.31 | 1577 |
| 2024-09-20 22:21:33.888 | MS1 | 121.4656694735 | 31.1446354247 | 230 | 504990 | -89.67 | 17.63 | 435.75 | 0.09 | 2.95 | 1575 |
| 2024-09-20 22:21:34.391 | MS1 | 121.4656632112 | 31.1446185302 | 230 | 504990 | -88.69 | 12.63 | 77.52 | 0.04 | 2.30 | 1563 |
| 2024-09-20 22:21:35.608 | MS1 | 121.4656759839 | 31.1446193210 | 230 | 504990 | -85.35 | 16.18 | 65.86 | 0.09 | 2.32 | 1598 |
| 2024-09-20 22:21:36.465 | MS1 | 121.4656704721 | 31.1446343923 | 230 | 504990 | -87.01 | 13.30 | 94.39 | 0.18 | 2.84 | 1595 |
| 2024-09-20 22:21:37.932 | MS1 | 121.4656627697 | 31.1446199804 | 230 | 504990 | -90.36 | 7.14 | 46.49 | 0.11 | 2.49 | 1568 |
| 2024-09-20 22:21:38.236 | MS1 | 121.4656756650 | 31.1446255046 | 230 | 504990 | -93.93 | 12.79 | 91.62 | 0.14 | 2.58 | 1591 |
| 2024-09-20 22:21:39.214 | MS1 | 121.4656702563 | 31.1446358177 | 230 | 504990 | -89.94 | 11.20 | 90.53 | 0.08 | 2.54 | 1566 |
| 2024-09-20 22:21:40.437 | MS1 | 121.4656679891 | 31.1446328952 | 230 | 504990 | -91.91 | 10.31 | 504.16 | 0.06 | 2.82 | 1589 |
| 2024-09-20 22:21:41.106 | MS1 | 121.4656640529 | 31.1446237584 | 230 | 504990 | -91.10 | 11.63 | 504.64 | 0.06 | 2.57 | 1588 |
| 2024-09-20 22:21:42.972 | MS1 | 121.4656614209 | 31.1446328209 | 230 | 504990 | -90.71 | 12.06 | 350.08 | 0.13 | 2.31 | 1561 |

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
| 3230602 | 4 | 121.4719612648 | 31.1542694047 | 242 | 10 | 9 | 42.9 | TDD | 105 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3251843 | 1 | 121.4695778224 | 31.1464298265 | 294 | 10 | 4 | 28.3 | TDD | 672 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3263049 | 3 | 121.4755378367 | 31.1485627185 | 238 | 0 | 6 | 42.6 | TDD | 230 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3267753 | 2 | 121.4640277608 | 31.1479816932 | 9 | 3 | 8 | 22.9 | TDD | 473 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.035 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.056 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.167 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.167 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.860 | NREventA3 | measId:2;ServCellPCI:906;Se... |
| 2024-09-20 22:21:38.100 | NRHandoverAttempt | SourcePCI:906;SourceNR-ARFC... |
| 2024-09-20 22:21:38.148 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.158 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.304 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.304 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251843 | 1 | 18.5285 | 18.9157 | -117.9460 | 16.5188 | 89.7764 | 0.0185 | 0.0138 |
| 2024_09_20 22:00 | 3267753 | 2 | 14.8714 | 15.8255 | -114.6078 | 12.9695 | 183.7507 | 0.0008 | 0.0003 |
| 2024_09_20 22:00 | 3263049 | 3 | 82.6850 | 82.7484 | -114.1719 | 12.5250 | 174.3349 | 0.0079 | 0.0000 |
| 2024_09_20 22:00 | 3230602 | 4 | 11.1906 | 8.3043 | -114.2612 | 5.1699 | 150.3194 | 0.0051 | 0.0092 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414872_DFA2ABC1 | 504990 | 230 | -87.5 | 504990 | 672 | -91.0 | 504990 | 473 | -102.6 | 504990 | 105 |
| MR_1774414872_73C3209D | 504990 | 230 | -87.9 | 504990 | 672 | -91.0 | 504990 | 473 | -102.1 | 504990 | 105 |
| MR_1774414872_C766E748 | 504990 | 230 | -90.5 | 504990 | 672 | -90.4 | 504990 | 473 | -104.2 | 504990 | 105 |
| MR_1774414872_7483EA06 | 504990 | 230 | -88.5 | 504990 | 672 | -91.2 | 504990 | 473 | -104.9 | 504990 | 105 |
| MR_1774414872_7867CD45 | 504990 | 230 | -90.2 | 504990 | 672 | -91.4 | 504990 | 473 | -104.5 | 504990 | 105 |
| MR_1774414872_3E76FFBC | 504990 | 230 | -87.7 | 504990 | 672 | -89.3 | 504990 | 473 | -103.1 | 504990 | 105 |
| MR_1774414872_BCB00004 | 504990 | 230 | -88.6 | 504990 | 672 | -92.2 | 504990 | 473 | -101.4 | 504990 | 105 |
| MR_1774414872_4E876BCF | 504990 | 230 | -88.4 | 504990 | 672 | -90.5 | 504990 | 473 | -101.2 | 504990 | 105 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 643: `1d735987-1fa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1d735987-1fa6-467f-9503-93386a1ced06` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239642_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[643] topology](images/train_0643.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3239642_5 by 2 degrees
- `C2`: Increase A3 Offset threshold for 3239642_5
- `C3`: Decrease transmission power for 3239642_5
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239642_5 **← 정답**
- `C5`: Press down the tilt angle  of 3245321_6 by 4 degrees
- `C6`: Decrease A3 Offset threshold for 3239642_5
- `C7`: Lift the tilt angle of 3239642_5 by 2 degrees
- `C8`: Add neighbor relationship between 3259264_10 and 3245321_6
- `C9`: Adjust the azimuth of 3245321_6 by 11 degrees
- `C10`: Adjust the azimuth of 3239642_5 by 29 degrees
- `C11`: Increase A3 Offset threshold for 3245321_6
- `C12`: Add neighbor relationship between 3239642_5 and 3245321_6
- `C13`: Decrease A3 Offset threshold for 3245321_6
- `C14`: Check test server and transmission issues
- `C15`: Increase transmission power for 3239642_5
- `C16`: Decrease transmission power for 3245321_6
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245321_6
- `C18`: Lift the tilt angle  of 3245321_6 by 4 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239642_5
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245321_6
- `C22`: Increase transmission power for 3245321_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.333 | MS1 | 121.4656686721 | 31.1446217462 | 527 | 504990 | -94.13 | 12.46 | 495.45 | 0.05 | 2.07 | 1564 |
| 2024-09-20 22:21:32.700 | MS1 | 121.4656626405 | 31.1446206591 | 621 | 504990 | -93.01 | 13.94 | 385.61 | 0.09 | 2.71 | 1581 |
| 2024-09-20 22:21:33.265 | MS1 | 121.4656718461 | 31.1446312445 | 903 | 504990 | -93.76 | 10.48 | 382.31 | 0.11 | 2.75 | 1565 |
| 2024-09-20 22:21:34.741 | MS1 | 121.4656685225 | 31.1446290511 | 752 | 152650 | -94.98 | 7.11 | 84.05 | 0.09 | 1.95 | 978 |
| 2024-09-20 22:21:35.610 | MS1 | 121.4656615449 | 31.1446305928 | 121 | 152650 | -87.25 | 5.12 | 76.78 | 0.08 | 1.99 | 976 |
| 2024-09-20 22:21:36.906 | MS1 | 121.4656652456 | 31.1446231316 | 271 | 152650 | -92.02 | 2.11 | 63.55 | 0.00 | 1.82 | 900 |
| 2024-09-20 22:21:37.395 | MS1 | 121.4656671776 | 31.1446379688 | 711 | 152650 | -91.17 | 7.70 | 73.65 | 0.11 | 1.79 | 988 |
| 2024-09-20 22:21:38.416 | MS1 | 121.4656667123 | 31.1446193249 | 752 | 152650 | -87.68 | 5.98 | 47.66 | 0.07 | 1.94 | 967 |
| 2024-09-20 22:21:39.977 | MS1 | 121.4656719143 | 31.1446246221 | 121 | 152650 | -95.85 | 3.99 | 53.27 | 0.06 | 1.62 | 947 |
| 2024-09-20 22:21:40.804 | MS1 | 121.4656648159 | 31.1446370085 | 271 | 152650 | -93.14 | 2.22 | 70.39 | 0.07 | 2.56 | 1585 |
| 2024-09-20 22:21:41.619 | MS1 | 121.4656728563 | 31.1446311298 | 711 | 152650 | -88.79 | 2.86 | 69.20 | 0.05 | 2.66 | 1560 |
| 2024-09-20 22:21:42.858 | MS1 | 121.4656732211 | 31.1446267818 | 752 | 152650 | -89.52 | 2.08 | 87.01 | 0.17 | 2.19 | 1568 |

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
| 3212222 | 11 | 121.4640297008 | 31.1543397216 | 279 | 2 | 11 | 19.9 | FDD | 752 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3212784 | 4 | 121.4660282446 | 31.1478256726 | 309 | 2 | 2 | 8.9 | TDD | 621 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3214889 | 3 | 121.4671354642 | 31.1549323236 | 355 | 5 | 1 | 5.4 | TDD | 586 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3220866 | 1 | 121.4700868487 | 31.1481583747 | 290 | 3 | 7 | 19.7 | TDD | 290 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3237633 | 9 | 121.4681278407 | 31.1512731660 | 78 | 15 | 8 | 14.7 | FDD | 711 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3239642 | 5 | 121.4724415691 | 31.1546746089 | 181 | 1 | 1 | 28.2 | TDD | 527 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3245321 | 6 | 121.4724424268 | 31.1450812090 | 276 | 3 | 2 | 14.8 | TDD | 892 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3246886 | 2 | 121.4746913786 | 31.1457953395 | 7 | 12 | 7 | 16.0 | TDD | 903 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3249287 | 13 | 121.4660290960 | 31.1529379191 | 0 | 15 | 3 | 25.9 | FDD | 795 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3258096 | 7 | 121.4653789214 | 31.1461847973 | 297 | 2 | 4 | 3.6 | FDD | 132 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3259264 | 10 | 121.4725499150 | 31.1516797227 | 8 | 7 | 3 | 26.0 | FDD | 271 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3264075 | 12 | 121.4696546939 | 31.1475041592 | 346 | 1 | 7 | 3.4 | FDD | 121 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3279433 | 8 | 121.4730790332 | 31.1501463871 | 117 | 8 | 9 | 5.7 | FDD | 998 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |

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
| 2024-09-20 22:21:31.476 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.494 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.614 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.614 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.357 | NREventA2 | measId:1;ServCellPCI:705;Se... |
| 2024-09-20 22:21:35.467 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.687 | NREventA5 | measId:3;ServCellPCI:705;Se... |
| 2024-09-20 22:21:35.764 | NRHandoverAttempt | SourcePCI:705;SourceNR-ARFC... |
| 2024-09-20 22:21:35.809 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.819 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.933 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.933 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220866 | 1 | 8.8891 | 10.4979 | -116.3740 | 14.6067 | 122.6568 | 0.0072 | 0.0047 |
| 2024_09_20 22:00 | 3246886 | 2 | 14.6740 | 14.0540 | -116.1840 | 18.1074 | 145.9241 | 0.0199 | 0.0141 |
| 2024_09_20 22:00 | 3214889 | 3 | 16.3910 | 6.2398 | -114.5527 | 6.4691 | 195.9499 | 0.0046 | 0.0199 |
| 2024_09_20 22:00 | 3212784 | 4 | 6.3456 | 16.0252 | -117.8818 | 11.3675 | 166.0203 | 0.0100 | 0.0014 |
| 2024_09_20 22:00 | 3239642 | 5 | 7.4792 | 8.4885 | -117.2359 | 11.2605 | 198.2151 | 0.0161 | 0.0040 |
| 2024_09_20 22:00 | 3245321 | 6 | 18.2212 | 5.4643 | -115.1789 | 10.5060 | 177.8153 | 0.0105 | 0.0051 |
| 2024_09_20 22:00 | 3258096 | 7 | 15.5386 | 8.3796 | -117.2658 | 4.9602 | 38.7385 | 0.0134 | 0.0191 |
| 2024_09_20 22:00 | 3279433 | 8 | 16.7709 | 14.6192 | -114.7443 | 4.6084 | 38.6196 | 0.0105 | 0.0115 |
| 2024_09_20 22:00 | 3237633 | 9 | 12.1511 | 14.7987 | -117.1223 | 3.7748 | 38.6638 | 0.0126 | 0.0088 |
| 2024_09_20 22:00 | 3259264 | 10 | 16.9046 | 19.0113 | -115.4034 | 3.7241 | 37.2242 | 0.0036 | 0.0029 |
| 2024_09_20 22:00 | 3212222 | 11 | 12.6441 | 9.5838 | -116.7785 | 4.9463 | 24.5298 | 0.0048 | 0.0142 |
| 2024_09_20 22:00 | 3264075 | 12 | 13.3230 | 19.6783 | -115.5996 | 3.5509 | 48.7218 | 0.0001 | 0.0117 |
| 2024_09_20 22:00 | 3249287 | 13 | 11.0249 | 8.6180 | -117.0846 | 3.8116 | 30.8995 | 0.0187 | 0.0143 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414391_EA260856 | 504990 | 903 | -92.5 | 504990 | 892 | -93.3 | 504990 | 586 | -97.4 | 504990 | 290 |
| MR_1774414391_D70633B5 | 152650 | 752 | -94.0 | 152650 | 132 | -101.4 | 152650 | 998 | -105.5 | 152650 | 795 |
| MR_1774414391_1BF2E686 | 504990 | 903 | -93.0 | 504990 | 892 | -95.7 | 504990 | 586 | -99.6 | 504990 | 290 |
| MR_1774414391_D90CC812 | 152650 | 752 | -94.6 | 152650 | 132 | -99.5 | 152650 | 998 | -108.4 | 152650 | 795 |
| MR_1774414391_50843C93 | 152650 | 752 | -96.5 | 152650 | 132 | -103.3 | 152650 | 998 | -105.8 | 152650 | 795 |
| MR_1774414391_70B62889 | 504990 | 903 | -92.9 | 504990 | 892 | -94.7 | 504990 | 586 | -96.5 | 504990 | 290 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 644: `a9ab6d78-9e6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a9ab6d78-9e6a-4391-ac21-b938c5276485` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Decrease A3 Offset threshold for 3254326_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[644] topology](images/train_0644.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3230052_2 and 3216148_3
- `C2`: Increase A3 Offset threshold for 3216148_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216148_3
- `C4`: Press down the tilt angle  of 3216148_3 by 9 degrees
- `C5`: Decrease A3 Offset threshold for 3254326_1 **← 정답**
- `C6`: Lift the tilt angle of 3254326_1 by 10 degrees
- `C7`: Increase transmission power for 3216148_3
- `C8`: Decrease transmission power for 3216148_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216148_3
- `C10`: Check test server and transmission issues
- `C11`: Lift the tilt angle  of 3216148_3 by 9 degrees
- `C12`: Add neighbor relationship between 3254326_1 and 3216148_3
- `C13`: Adjust the azimuth of 3216148_3 by 50 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254326_1
- `C15`: Adjust the azimuth of 3254326_1 by 50 degrees
- `C16`: Increase A3 Offset threshold for 3254326_1
- `C17`: Increase transmission power for 3254326_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254326_1
- `C19`: Press down the tilt angle of 3254326_1 by 10 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease transmission power for 3254326_1
- `C22`: Decrease A3 Offset threshold for 3216148_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.159 | MS1 | 121.4656601257 | 31.1446289969 | 161 | 504990 | -83.21 | 14.13 | 454.78 | 0.13 | 2.68 | 1571 |
| 2024-09-20 22:21:32.717 | MS1 | 121.4656763352 | 31.1446186281 | 161 | 504990 | -83.17 | 13.54 | 494.30 | 0.08 | 2.15 | 1582 |
| 2024-09-20 22:21:33.122 | MS1 | 121.4656663277 | 31.1446266475 | 161 | 504990 | -79.71 | 16.99 | 565.46 | 0.14 | 2.55 | 1591 |
| 2024-09-20 22:21:34.187 | MS1 | 121.4656613395 | 31.1446239542 | 161 | 504990 | -92.35 | -3.67 | 68.75 | 0.03 | 1.48 | 1594 |
| 2024-09-20 22:21:35.185 | MS1 | 121.4656755494 | 31.1446306718 | 161 | 504990 | -86.84 | -2.87 | 43.74 | 0.14 | 1.22 | 1575 |
| 2024-09-20 22:21:36.173 | MS1 | 121.4656748807 | 31.1446320837 | 161 | 504990 | -89.33 | -0.96 | 35.25 | 0.07 | 1.37 | 1595 |
| 2024-09-20 22:21:37.518 | MS1 | 121.4656717593 | 31.1446369479 | 161 | 504990 | -89.78 | -2.73 | 48.95 | 0.17 | 1.44 | 1572 |
| 2024-09-20 22:21:38.950 | MS1 | 121.4656637458 | 31.1446358184 | 161 | 504990 | -85.83 | -3.97 | 39.66 | 0.13 | 1.32 | 1579 |
| 2024-09-20 22:21:39.580 | MS1 | 121.4656660614 | 31.1446344271 | 291 | 504990 | -79.21 | 14.35 | 225.78 | 0.11 | 1.31 | 1582 |
| 2024-09-20 22:21:40.616 | MS1 | 121.4656627705 | 31.1446258945 | 291 | 504990 | -84.71 | 17.43 | 339.02 | 0.08 | 2.61 | 1574 |
| 2024-09-20 22:21:41.156 | MS1 | 121.4656750307 | 31.1446267316 | 291 | 504990 | -80.73 | 16.97 | 422.39 | 0.08 | 2.20 | 1594 |
| 2024-09-20 22:21:42.342 | MS1 | 121.4656718998 | 31.1446348743 | 291 | 504990 | -84.45 | 13.15 | 301.74 | 0.13 | 2.30 | 1565 |

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
| 3216148 | 3 | 121.4741180366 | 31.1464797374 | 316 | 7 | 11 | 22.6 | TDD | 291 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3230052 | 2 | 121.4679071876 | 31.1443702196 | 195 | 2 | 2 | 22.4 | TDD | 450 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3254326 | 1 | 121.4744027334 | 31.1525365893 | 52 | 10 | 12 | 39.6 | TDD | 161 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3256021 | 4 | 121.4640938247 | 31.1554713082 | 162 | 9 | 10 | 48.2 | TDD | 265 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.354 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.378 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.488 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.488 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.187 | NREventA3 | measId:2;ServCellPCI:198;Se... |
| 2024-09-20 22:21:38.427 | NRHandoverAttempt | SourcePCI:198;SourceNR-ARFC... |
| 2024-09-20 22:21:38.474 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.489 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.619 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.619 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254326 | 1 | 11.3911 | 9.7836 | -117.3834 | 18.8907 | 189.6037 | 0.0064 | 0.1902 |
| 2024_09_20 22:00 | 3230052 | 2 | 14.3561 | 19.1183 | -114.8929 | 12.5609 | 99.6324 | 0.0056 | 0.0177 |
| 2024_09_20 22:00 | 3216148 | 3 | 12.9410 | 15.3704 | -117.5465 | 12.6962 | 125.6794 | 0.0028 | 0.0152 |
| 2024_09_20 22:00 | 3256021 | 4 | 19.6440 | 15.3168 | -114.9919 | 15.4993 | 154.9143 | 0.0011 | 0.0156 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414254_B63F330A | 504990 | 291 | -83.9 | 504990 | 161 | -92.3 | 504990 | 450 | -84.5 | 504990 | 265 |
| MR_1774414254_A120E8C4 | 504990 | 291 | -86.1 | 504990 | 161 | -92.1 | 504990 | 450 | -87.7 | 504990 | 265 |
| MR_1774414254_BA61CAF1 | 504990 | 161 | -91.9 | 504990 | 291 | -86.9 | 504990 | 450 | -87.6 | 504990 | 265 |
| MR_1774414254_EB0A23DF | 504990 | 161 | -93.2 | 504990 | 291 | -84.3 | 504990 | 450 | -86.3 | 504990 | 265 |
| MR_1774414254_6BB6DB4E | 504990 | 161 | -91.8 | 504990 | 291 | -84.0 | 504990 | 450 | -85.2 | 504990 | 265 |
| MR_1774414254_55CAAE01 | 504990 | 161 | -92.5 | 504990 | 291 | -86.9 | 504990 | 450 | -87.6 | 504990 | 265 |
| MR_1774414254_06DD7DA6 | 504990 | 291 | -84.1 | 504990 | 161 | -91.7 | 504990 | 450 | -87.4 | 504990 | 265 |
| MR_1774414254_DD67206E | 504990 | 161 | -93.5 | 504990 | 291 | -84.8 | 504990 | 450 | -87.1 | 504990 | 265 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 645: `6c392308-b1d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6c392308-b1dd-4e7c-a0aa-8a6ac97e3b78` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease A3 Offset threshold for 3230068_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[645] topology](images/train_0645.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3229158_3 by 50 degrees
- `C2`: Decrease transmission power for 3230068_2
- `C3`: Check test server and transmission issues
- `C4`: Increase A3 Offset threshold for 3230068_2
- `C5`: Add neighbor relationship between 3212852_4 and 3229158_3
- `C6`: Add neighbor relationship between 3230068_2 and 3229158_3
- `C7`: Decrease transmission power for 3229158_3
- `C8`: Decrease A3 Offset threshold for 3229158_3
- `C9`: Increase A3 Offset threshold for 3229158_3
- `C10`: Press down the tilt angle  of 3229158_3 by 10 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229158_3
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Press down the tilt angle of 3230068_2 by 5 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230068_2
- `C15`: Increase transmission power for 3230068_2
- `C16`: Lift the tilt angle  of 3229158_3 by 10 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229158_3
- `C18`: Increase transmission power for 3229158_3
- `C19`: Lift the tilt angle of 3230068_2 by 5 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230068_2
- `C21`: Adjust the azimuth of 3230068_2 by 33 degrees
- `C22`: Decrease A3 Offset threshold for 3230068_2 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.963 | MS1 | 121.4656730385 | 31.1446320335 | 691 | 504990 | -80.47 | 15.01 | 567.08 | 0.05 | 2.97 | 1585 |
| 2024-09-20 22:21:32.446 | MS1 | 121.4656637342 | 31.1446312149 | 691 | 504990 | -82.08 | 12.01 | 483.58 | 0.19 | 2.63 | 1583 |
| 2024-09-20 22:21:33.184 | MS1 | 121.4656615838 | 31.1446325564 | 691 | 504990 | -83.59 | 13.11 | 439.66 | 0.16 | 2.81 | 1596 |
| 2024-09-20 22:21:34.467 | MS1 | 121.4656726223 | 31.1446279880 | 691 | 504990 | -91.36 | -1.00 | 48.31 | 0.18 | 1.46 | 1564 |
| 2024-09-20 22:21:35.317 | MS1 | 121.4656640343 | 31.1446271058 | 691 | 504990 | -88.69 | -3.98 | 36.87 | 0.17 | 1.05 | 1592 |
| 2024-09-20 22:21:36.517 | MS1 | 121.4656627328 | 31.1446231427 | 691 | 504990 | -87.30 | -3.20 | 47.59 | 0.15 | 1.47 | 1585 |
| 2024-09-20 22:21:37.348 | MS1 | 121.4656636979 | 31.1446350126 | 691 | 504990 | -91.77 | -0.21 | 45.01 | 0.03 | 1.45 | 1594 |
| 2024-09-20 22:21:38.462 | MS1 | 121.4656763772 | 31.1446361695 | 691 | 504990 | -87.49 | -0.47 | 70.23 | 0.12 | 1.33 | 1584 |
| 2024-09-20 22:21:39.899 | MS1 | 121.4656586535 | 31.1446270273 | 378 | 504990 | -82.18 | 12.41 | 293.51 | 0.08 | 1.30 | 1568 |
| 2024-09-20 22:21:40.891 | MS1 | 121.4656737574 | 31.1446283151 | 378 | 504990 | -80.33 | 15.55 | 399.79 | 0.05 | 2.53 | 1586 |
| 2024-09-20 22:21:41.383 | MS1 | 121.4656771194 | 31.1446242092 | 378 | 504990 | -78.31 | 14.84 | 535.96 | 0.15 | 2.04 | 1592 |
| 2024-09-20 22:21:42.539 | MS1 | 121.4656621353 | 31.1446200110 | 378 | 504990 | -83.36 | 15.34 | 500.06 | 0.19 | 2.04 | 1587 |

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
| 3212852 | 4 | 121.4713652306 | 31.1529341653 | 142 | 13 | 11 | 41.7 | TDD | 71 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3229158 | 3 | 121.4651910086 | 31.1497402580 | 0 | 9 | 6 | 34.4 | TDD | 378 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3230068 | 2 | 121.4723877697 | 31.1546320841 | 177 | 3 | 8 | 35.2 | TDD | 691 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3261519 | 1 | 121.4690953258 | 31.1555029264 | 124 | 5 | 11 | 29.3 | TDD | 458 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.240 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.260 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.379 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.379 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.122 | NREventA3 | measId:2;ServCellPCI:38;Ser... |
| 2024-09-20 22:21:38.362 | NRHandoverAttempt | SourcePCI:38;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.401 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.415 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.550 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.550 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261519 | 1 | 19.9141 | 14.4008 | -114.0856 | 7.4999 | 150.5943 | 0.0018 | 0.0168 |
| 2024_09_20 22:00 | 3230068 | 2 | 5.1886 | 8.4133 | -117.1040 | 18.9221 | 187.3869 | 0.0085 | 0.1467 |
| 2024_09_20 22:00 | 3229158 | 3 | 6.9770 | 16.8893 | -114.9561 | 18.2215 | 194.1339 | 0.0087 | 0.0008 |
| 2024_09_20 22:00 | 3212852 | 4 | 15.4439 | 17.7257 | -114.7411 | 12.7485 | 124.8608 | 0.0129 | 0.0183 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414577_1D13D9FD | 504990 | 691 | -90.7 | 504990 | 378 | -85.0 | 504990 | 71 | -88.2 | 504990 | 458 |
| MR_1774414577_8E6D9710 | 504990 | 691 | -92.5 | 504990 | 378 | -85.7 | 504990 | 71 | -89.0 | 504990 | 458 |
| MR_1774414577_78B9F71C | 504990 | 378 | -87.1 | 504990 | 691 | -93.0 | 504990 | 71 | -86.9 | 504990 | 458 |
| MR_1774414577_3AEFA604 | 504990 | 691 | -93.0 | 504990 | 378 | -85.6 | 504990 | 71 | -87.5 | 504990 | 458 |
| MR_1774414577_53E8A760 | 504990 | 691 | -92.2 | 504990 | 378 | -86.7 | 504990 | 71 | -88.4 | 504990 | 458 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 646: `d9b957d4-696...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d9b957d4-696c-4c65-aef5-b05aa876df20` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[646] topology](images/train_0646.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248642_2
- `C2`: Decrease transmission power for 3248642_2
- `C3`: Insufficient data; more data is needed for judgment. **← 정답**
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248642_2
- `C5`: Increase A3 Offset threshold for 3248642_2
- `C6`: Increase A3 Offset threshold for 3218283_4
- `C7`: Increase transmission power for 3248642_2
- `C8`: Adjust the azimuth of 3248642_2 by 50 degrees
- `C9`: Press down the tilt angle of 3248642_2 by 10 degrees
- `C10`: Lift the tilt angle of 3248642_2 by 10 degrees
- `C11`: Decrease transmission power for 3218283_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218283_4
- `C13`: Add neighbor relationship between 3248642_2 and 3218283_4
- `C14`: Decrease A3 Offset threshold for 3218283_4
- `C15`: Decrease A3 Offset threshold for 3248642_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218283_4
- `C17`: Add neighbor relationship between 3249565_1 and 3218283_4
- `C18`: Lift the tilt angle  of 3218283_4 by 10 degrees
- `C19`: Increase transmission power for 3218283_4
- `C20`: Check test server and transmission issues
- `C21`: Adjust the azimuth of 3218283_4 by 50 degrees
- `C22`: Press down the tilt angle  of 3218283_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.369 | MS1 | 121.4656680335 | 31.1446367495 | 938 | 504990 | -91.39 | 15.57 | 554.46 | 0.13 | 2.92 | 1599 |
| 2024-09-20 22:21:32.908 | MS1 | 121.4656713158 | 31.1446245186 | 938 | 504990 | -86.90 | 14.25 | 587.92 | 0.11 | 2.12 | 1594 |
| 2024-09-20 22:21:33.694 | MS1 | 121.4656670393 | 31.1446273752 | 938 | 504990 | -89.46 | 15.32 | 535.70 | 0.07 | 2.38 | 1580 |
| 2024-09-20 22:21:34.626 | MS1 | 121.4656707376 | 31.1446203648 | 938 | 504990 | -87.63 | 17.44 | 51.17 | 0.15 | 2.45 | 1564 |
| 2024-09-20 22:21:35.656 | MS1 | 121.4656774455 | 31.1446308579 | 938 | 504990 | -88.77 | 17.17 | 103.75 | 0.19 | 2.79 | 1582 |
| 2024-09-20 22:21:36.324 | MS1 | 121.4656612353 | 31.1446186301 | 938 | 504990 | -87.52 | 17.24 | 63.24 | 0.03 | 2.55 | 1597 |
| 2024-09-20 22:21:37.832 | MS1 | 121.4656716579 | 31.1446299906 | 938 | 504990 | -93.43 | 10.37 | 86.59 | 0.05 | 2.67 | 1590 |
| 2024-09-20 22:21:38.202 | MS1 | 121.4656716426 | 31.1446332517 | 938 | 504990 | -91.62 | 10.74 | 76.56 | 0.08 | 2.32 | 1573 |
| 2024-09-20 22:21:39.784 | MS1 | 121.4656705348 | 31.1446273424 | 938 | 504990 | -92.04 | 7.27 | 86.03 | 0.03 | 2.61 | 1563 |
| 2024-09-20 22:21:40.718 | MS1 | 121.4656629985 | 31.1446354837 | 938 | 504990 | -89.49 | 7.14 | 467.02 | 0.05 | 2.58 | 1566 |
| 2024-09-20 22:21:41.267 | MS1 | 121.4656708392 | 31.1446208987 | 938 | 504990 | -92.24 | 10.65 | 328.44 | 0.04 | 2.02 | 1600 |
| 2024-09-20 22:21:42.683 | MS1 | 121.4656582719 | 31.1446342174 | 938 | 504990 | -93.47 | 9.00 | 569.63 | 0.01 | 2.50 | 1567 |

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
| 3218283 | 4 | 121.4680737975 | 31.1463670535 | 310 | 15 | 2 | 37.1 | TDD | 443 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3247208 | 3 | 121.4692157813 | 31.1458770437 | 10 | 10 | 9 | 31.3 | TDD | 875 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3248642 | 2 | 121.4747797785 | 31.1550691519 | 272 | 10 | 10 | 34.8 | TDD | 938 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3249565 | 1 | 121.4747796748 | 31.1526409330 | 133 | 4 | 12 | 29.3 | TDD | 829 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.486 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.509 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.630 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.630 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.306 | NREventA3 | measId:2;ServCellPCI:615;Se... |
| 2024-09-20 22:21:38.546 | NRHandoverAttempt | SourcePCI:615;SourceNR-ARFC... |
| 2024-09-20 22:21:38.581 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.596 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.735 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.735 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3249565 | 1 | 93.6362 | 90.3540 | -117.5243 | 19.1935 | 176.6237 | 0.0175 | 0.0122 |
| 2024_09_19 22:00 | 3248642 | 2 | 80.3619 | 84.7008 | -117.2145 | 13.8863 | 165.8931 | 0.0071 | 0.0008 |
| 2024_09_19 22:00 | 3247208 | 3 | 77.5071 | 75.0669 | -116.5487 | 15.1098 | 128.4176 | 0.0048 | 0.0107 |
| 2024_09_19 22:00 | 3218283 | 4 | 77.2908 | 87.2293 | -116.0041 | 14.8975 | 142.2766 | 0.0157 | 0.0112 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414001_E2FDC103 | 504990 | 938 | -87.1 | 504990 | 443 | -88.9 | 504990 | 829 | -102.4 | 504990 | 875 |
| MR_1774414001_2537D307 | 504990 | 938 | -87.7 | 504990 | 443 | -88.4 | 504990 | 829 | -102.4 | 504990 | 875 |
| MR_1774414001_BB8F7474 | 504990 | 938 | -86.5 | 504990 | 443 | -89.7 | 504990 | 829 | -102.4 | 504990 | 875 |
| MR_1774414001_EDD5D5C7 | 504990 | 938 | -89.4 | 504990 | 443 | -87.4 | 504990 | 829 | -101.5 | 504990 | 875 |
| MR_1774414001_E78CC4CD | 504990 | 938 | -87.8 | 504990 | 443 | -89.1 | 504990 | 829 | -103.1 | 504990 | 875 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 647: `81137def-c63...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `81137def-c636-49d8-a499-7e693544cdd8` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[647] topology](images/train_0647.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270287_3
- `C2`: Decrease A3 Offset threshold for 3270287_3
- `C3`: Decrease transmission power for 3270287_3
- `C4`: Decrease A3 Offset threshold for 3239188_4
- `C5`: Add neighbor relationship between 3270287_3 and 3239188_4
- `C6`: Lift the tilt angle  of 3239188_4 by 10 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239188_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270287_3
- `C9`: Adjust the azimuth of 3239188_4 by 50 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239188_4
- `C11`: Add neighbor relationship between 3254971_1 and 3239188_4
- `C12`: Increase transmission power for 3270287_3
- `C13`: Increase A3 Offset threshold for 3239188_4
- `C14`: Decrease transmission power for 3239188_4
- `C15`: Increase transmission power for 3239188_4
- `C16`: Insufficient data; more data is needed for judgment. **← 정답**
- `C17`: Check test server and transmission issues
- `C18`: Press down the tilt angle  of 3239188_4 by 10 degrees
- `C19`: Press down the tilt angle of 3270287_3 by 10 degrees
- `C20`: Lift the tilt angle of 3270287_3 by 10 degrees
- `C21`: Increase A3 Offset threshold for 3270287_3
- `C22`: Adjust the azimuth of 3270287_3 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.312 | MS1 | 121.4656741706 | 31.1446233566 | 1004 | 504990 | -90.78 | 17.45 | 380.32 | 0.09 | 2.88 | 1591 |
| 2024-09-20 22:21:32.214 | MS1 | 121.4656740616 | 31.1446265853 | 1004 | 504990 | -85.15 | 14.63 | 425.42 | 0.10 | 2.37 | 1585 |
| 2024-09-20 22:21:33.567 | MS1 | 121.4656774838 | 31.1446364419 | 1004 | 504990 | -88.34 | 16.40 | 491.35 | 0.19 | 2.95 | 1569 |
| 2024-09-20 22:21:34.331 | MS1 | 121.4656771980 | 31.1446231453 | 1004 | 504990 | -85.49 | 15.27 | 63.18 | 0.03 | 2.40 | 1565 |
| 2024-09-20 22:21:35.187 | MS1 | 121.4656646568 | 31.1446277111 | 1004 | 504990 | -85.49 | 12.30 | 83.68 | 0.16 | 2.79 | 1573 |
| 2024-09-20 22:21:36.432 | MS1 | 121.4656700953 | 31.1446268458 | 1004 | 504990 | -87.87 | 16.35 | 76.32 | 0.05 | 2.21 | 1585 |
| 2024-09-20 22:21:37.328 | MS1 | 121.4656759146 | 31.1446356721 | 1004 | 504990 | -91.85 | 9.30 | 71.07 | 0.17 | 2.87 | 1573 |
| 2024-09-20 22:21:38.856 | MS1 | 121.4656652798 | 31.1446337167 | 1004 | 504990 | -91.20 | 10.75 | 82.39 | 0.02 | 2.10 | 1572 |
| 2024-09-20 22:21:39.849 | MS1 | 121.4656711291 | 31.1446273351 | 1004 | 504990 | -90.30 | 11.34 | 104.25 | 0.14 | 2.26 | 1568 |
| 2024-09-20 22:21:40.510 | MS1 | 121.4656748724 | 31.1446355911 | 1004 | 504990 | -92.37 | 9.22 | 581.48 | 0.00 | 2.07 | 1593 |
| 2024-09-20 22:21:41.443 | MS1 | 121.4656631077 | 31.1446252844 | 1004 | 504990 | -89.38 | 9.86 | 519.70 | 0.11 | 2.52 | 1561 |
| 2024-09-20 22:21:42.193 | MS1 | 121.4656631320 | 31.1446183287 | 1004 | 504990 | -91.82 | 11.09 | 306.35 | 0.07 | 2.39 | 1572 |

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
| 3239188 | 4 | 121.4679468902 | 31.1555678526 | 102 | 10 | 5 | 47.0 | TDD | 630 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3254971 | 1 | 121.4686110996 | 31.1442149229 | 285 | 5 | 4 | 32.8 | TDD | 746 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3260472 | 2 | 121.4704927045 | 31.1483879144 | 298 | 9 | 1 | 33.2 | TDD | 955 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3270287 | 3 | 121.4707555286 | 31.1448267424 | 350 | 10 | 0 | 43.4 | TDD | 1004 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.913 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.928 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.064 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.064 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.718 | NREventA3 | measId:2;ServCellPCI:127;Se... |
| 2024-09-20 22:21:37.958 | NRHandoverAttempt | SourcePCI:127;SourceNR-ARFC... |
| 2024-09-20 22:21:37.995 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.010 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.155 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.155 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3254971 | 1 | 94.4406 | 85.6663 | -114.0146 | 7.1551 | 101.2213 | 0.0043 | 0.0055 |
| 2024_09_19 22:00 | 3260472 | 2 | 91.4911 | 91.4626 | -115.6185 | 17.5640 | 84.4745 | 0.0083 | 0.0013 |
| 2024_09_19 22:00 | 3270287 | 3 | 78.3973 | 83.7984 | -114.2889 | 18.2037 | 127.8948 | 0.0116 | 0.0166 |
| 2024_09_19 22:00 | 3239188 | 4 | 85.7267 | 84.3353 | -114.2795 | 19.0679 | 191.1750 | 0.0048 | 0.0162 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415477_61D36818 | 504990 | 1004 | -85.4 | 504990 | 630 | -91.9 | 504990 | 746 | -98.3 | 504990 | 955 |
| MR_1774415477_6FCB2CF4 | 504990 | 1004 | -83.9 | 504990 | 630 | -91.8 | 504990 | 746 | -96.9 | 504990 | 955 |
| MR_1774415477_09BF03AB | 504990 | 1004 | -86.9 | 504990 | 630 | -93.8 | 504990 | 746 | -98.8 | 504990 | 955 |
| MR_1774415477_BD7EB1EB | 504990 | 1004 | -84.7 | 504990 | 630 | -95.1 | 504990 | 746 | -100.0 | 504990 | 955 |
| MR_1774415477_B6CE5673 | 504990 | 1004 | -84.7 | 504990 | 630 | -91.9 | 504990 | 746 | -100.0 | 504990 | 955 |
| MR_1774415477_46410870 | 504990 | 1004 | -86.8 | 504990 | 630 | -95.6 | 504990 | 746 | -99.0 | 504990 | 955 |
| MR_1774415477_CAF540DA | 504990 | 1004 | -86.7 | 504990 | 630 | -93.2 | 504990 | 746 | -99.9 | 504990 | 955 |
| MR_1774415477_6354F99B | 504990 | 1004 | -83.6 | 504990 | 630 | -93.7 | 504990 | 746 | -99.2 | 504990 | 955 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 648: `7524fe86-3c5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7524fe86-3c56-4915-9459-ac597fdd993d` |
| Tag | **multiple-answer** |
| 정답 | **C7|C10** |
| C7 의미 | Adjust the azimuth of 3256708_1 by 50 degrees |
| C10 의미 | Increase transmission power for 3256708_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[648] topology](images/train_0648.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3279338_2
- `C2`: Add neighbor relationship between 3271530_3 and 3279338_2
- `C3`: Lift the tilt angle of 3256708_1 by 6 degrees
- `C4`: Press down the tilt angle  of 3279338_2 by 1 degrees
- `C5`: Press down the tilt angle of 3256708_1 by 6 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256708_1
- `C7`: Adjust the azimuth of 3256708_1 by 50 degrees **← 정답**
- `C8`: Lift the tilt angle  of 3279338_2 by 1 degrees
- `C9`: Increase A3 Offset threshold for 3256708_1
- `C10`: Increase transmission power for 3256708_1 **← 정답**
- `C11`: Add neighbor relationship between 3256708_1 and 3279338_2
- `C12`: Check test server and transmission issues
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279338_2
- `C14`: Decrease transmission power for 3256708_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256708_1
- `C16`: Decrease A3 Offset threshold for 3256708_1
- `C17`: Decrease transmission power for 3279338_2
- `C18`: Adjust the azimuth of 3279338_2 by 29 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279338_2
- `C21`: Increase A3 Offset threshold for 3279338_2
- `C22`: Increase transmission power for 3279338_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.660 | MS1 | 121.4656696983 | 31.1446355667 | 184 | 504990 | -86.44 | 12.81 | 345.19 | 0.12 | 2.52 | 1562 |
| 2024-09-20 22:21:32.137 | MS1 | 121.4656772670 | 31.1446233518 | 184 | 504990 | -86.55 | 12.41 | 443.47 | 0.20 | 2.36 | 1592 |
| 2024-09-20 22:21:33.116 | MS1 | 121.4656624521 | 31.1446205318 | 184 | 504990 | -93.19 | 17.36 | 516.71 | 0.11 | 2.51 | 1582 |
| 2024-09-20 22:21:34.444 | MS1 | 121.4656724936 | 31.1446232197 | 184 | 504990 | -107.55 | -0.46 | 66.81 | 0.10 | 1.23 | 1560 |
| 2024-09-20 22:21:35.604 | MS1 | 121.4656758532 | 31.1446215632 | 184 | 504990 | -102.42 | 0.87 | 67.59 | 0.13 | 1.36 | 1574 |
| 2024-09-20 22:21:36.137 | MS1 | 121.4656657505 | 31.1446283597 | 184 | 504990 | -103.52 | 1.27 | 70.28 | 0.05 | 1.13 | 1583 |
| 2024-09-20 22:21:37.798 | MS1 | 121.4656670467 | 31.1446199325 | 184 | 504990 | -106.33 | 1.55 | 20.97 | 0.05 | 1.25 | 1589 |
| 2024-09-20 22:21:38.824 | MS1 | 121.4656641474 | 31.1446375524 | 184 | 504990 | -100.54 | 1.57 | 28.31 | 0.10 | 1.06 | 1565 |
| 2024-09-20 22:21:39.174 | MS1 | 121.4656711083 | 31.1446235559 | 184 | 504990 | -100.48 | 1.80 | 73.65 | 0.05 | 1.27 | 1581 |
| 2024-09-20 22:21:40.385 | MS1 | 121.4656635544 | 31.1446209647 | 184 | 504990 | -94.42 | 15.39 | 470.32 | 0.14 | 2.53 | 1561 |
| 2024-09-20 22:21:41.384 | MS1 | 121.4656587961 | 31.1446324279 | 184 | 504990 | -89.52 | 14.56 | 542.99 | 0.15 | 2.96 | 1600 |
| 2024-09-20 22:21:42.380 | MS1 | 121.4656744277 | 31.1446349175 | 184 | 504990 | -92.21 | 14.39 | 372.42 | 0.19 | 2.93 | 1598 |

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
| 3256708 | 1 | 121.4668903735 | 31.1509582537 | 134 | 3 | 8 | 36.9 | TDD | 184 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3258179 | 4 | 121.4677893505 | 31.1502637503 | 339 | 14 | 11 | 31.9 | TDD | 158 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3271530 | 3 | 121.4649780141 | 31.1519290913 | 246 | 2 | 11 | 16.6 | TDD | 917 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3279338 | 2 | 121.4747159298 | 31.1557868572 | 244 | 0 | 1 | 38.7 | TDD | 734 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.128 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.149 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.260 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.260 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.440 | NREventA2 | measId:1;ServCellPCI:794;Se... |
| 2024-09-20 22:21:34.546 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256708 | 1 | 9.7716 | 19.3055 | -115.0131 | 10.3992 | 142.4826 | 0.1135 | 0.0005 |
| 2024_09_20 22:00 | 3279338 | 2 | 11.2785 | 17.7348 | -116.9111 | 14.2308 | 80.4306 | 0.0171 | 0.0044 |
| 2024_09_20 22:00 | 3271530 | 3 | 17.2588 | 14.6892 | -114.8894 | 5.8541 | 127.7212 | 0.0000 | 0.0150 |
| 2024_09_20 22:00 | 3258179 | 4 | 11.4618 | 10.8256 | -115.5117 | 13.0291 | 181.4937 | 0.0131 | 0.0041 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413438_5A026119 | 504990 | 184 | -106.2 | 504990 | 734 | -115.8 | 504990 | 917 | -119.9 | 504990 | 158 |
| MR_1774413438_7168D48E | 504990 | 184 | -108.1 | 504990 | 734 | -114.4 | 504990 | 917 | -118.0 | 504990 | 158 |
| MR_1774413438_C17DFA5F | 504990 | 184 | -107.4 | 504990 | 734 | -113.7 | 504990 | 917 | -120.4 | 504990 | 158 |
| MR_1774413438_6512C001 | 504990 | 184 | -109.1 | 504990 | 734 | -112.4 | 504990 | 917 | -120.1 | 504990 | 158 |
| MR_1774413438_E85D5BB5 | 504990 | 184 | -108.2 | 504990 | 734 | -114.4 | 504990 | 917 | -118.8 | 504990 | 158 |
| MR_1774413438_2C8CF01D | 504990 | 184 | -108.3 | 504990 | 734 | -115.7 | 504990 | 917 | -120.2 | 504990 | 158 |
| MR_1774413438_47CC0E75 | 504990 | 184 | -108.2 | 504990 | 734 | -113.3 | 504990 | 917 | -119.0 | 504990 | 158 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 649: `4a884258-a48...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4a884258-a480-4250-9ffe-80d7ed461f24` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238603_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[649] topology](images/train_0649.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3238603_5
- `C2`: Decrease transmission power for 3238603_5
- `C3`: Check test server and transmission issues
- `C4`: Decrease transmission power for 3238219_4
- `C5`: Add neighbor relationship between 3218459_13 and 3238219_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase transmission power for 3238219_4
- `C8`: Add neighbor relationship between 3238603_5 and 3238219_4
- `C9`: Press down the tilt angle of 3238603_5 by 0 degrees
- `C10`: Increase A3 Offset threshold for 3238219_4
- `C11`: Decrease A3 Offset threshold for 3238603_5
- `C12`: Lift the tilt angle  of 3238219_4 by 1 degrees
- `C13`: Decrease A3 Offset threshold for 3238219_4
- `C14`: Press down the tilt angle  of 3238219_4 by 1 degrees
- `C15`: Increase transmission power for 3238603_5
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238219_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238219_4
- `C18`: Adjust the azimuth of 3238603_5 by 4 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238603_5 **← 정답**
- `C20`: Lift the tilt angle of 3238603_5 by 0 degrees
- `C21`: Adjust the azimuth of 3238219_4 by 32 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238603_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.457 | MS1 | 121.4656605835 | 31.1446258715 | 125 | 504990 | -95.86 | 14.39 | 503.69 | 0.08 | 2.95 | 1579 |
| 2024-09-20 22:21:32.927 | MS1 | 121.4656737998 | 31.1446209614 | 289 | 504990 | -94.59 | 9.79 | 601.80 | 0.16 | 2.76 | 1568 |
| 2024-09-20 22:21:33.518 | MS1 | 121.4656770882 | 31.1446206327 | 583 | 504990 | -95.27 | 14.49 | 495.74 | 0.01 | 2.84 | 1591 |
| 2024-09-20 22:21:34.829 | MS1 | 121.4656734590 | 31.1446370577 | 597 | 152650 | -90.02 | 6.57 | 62.87 | 0.17 | 1.53 | 995 |
| 2024-09-20 22:21:35.156 | MS1 | 121.4656766988 | 31.1446358896 | 699 | 152650 | -96.09 | 4.03 | 63.06 | 0.03 | 1.97 | 932 |
| 2024-09-20 22:21:36.913 | MS1 | 121.4656666038 | 31.1446195732 | 925 | 152650 | -92.92 | 7.26 | 101.39 | 0.15 | 1.67 | 925 |
| 2024-09-20 22:21:37.222 | MS1 | 121.4656739048 | 31.1446324879 | 949 | 152650 | -90.34 | 3.74 | 104.42 | 0.03 | 1.61 | 958 |
| 2024-09-20 22:21:38.460 | MS1 | 121.4656707179 | 31.1446193209 | 597 | 152650 | -91.62 | 3.83 | 66.24 | 0.11 | 1.62 | 910 |
| 2024-09-20 22:21:39.990 | MS1 | 121.4656670400 | 31.1446212250 | 699 | 152650 | -88.06 | 6.72 | 79.20 | 0.12 | 1.96 | 979 |
| 2024-09-20 22:21:40.124 | MS1 | 121.4656686350 | 31.1446367239 | 925 | 152650 | -87.64 | 6.65 | 46.26 | 0.03 | 2.87 | 1594 |
| 2024-09-20 22:21:41.741 | MS1 | 121.4656719353 | 31.1446195811 | 949 | 152650 | -92.85 | 4.27 | 58.51 | 0.16 | 2.95 | 1591 |
| 2024-09-20 22:21:42.495 | MS1 | 121.4656748839 | 31.1446299590 | 597 | 152650 | -94.97 | 7.30 | 58.89 | 0.19 | 2.61 | 1571 |

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
| 3215574 | 8 | 121.4650178640 | 31.1559613662 | 276 | 7 | 9 | 11.9 | FDD | 597 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3218322 | 9 | 121.4758283457 | 31.1451609135 | 88 | 8 | 4 | 27.0 | FDD | 949 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3218459 | 13 | 121.4692051755 | 31.1474145677 | 355 | 14 | 6 | 0.4 | FDD | 925 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3238219 | 4 | 121.4717406550 | 31.1515652896 | 185 | 1 | 9 | 5.9 | TDD | 660 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3238603 | 5 | 121.4750229533 | 31.1477623359 | 245 | 0 | 4 | 7.0 | TDD | 125 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3247382 | 7 | 121.4685200061 | 31.1488579664 | 51 | 1 | 12 | 22.1 | FDD | 45 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3252129 | 12 | 121.4693832772 | 31.1453522804 | 264 | 2 | 0 | 20.9 | FDD | 699 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3265105 | 2 | 121.4731209810 | 31.1474557562 | 281 | 2 | 8 | 16.2 | TDD | 583 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3268524 | 6 | 121.4701589088 | 31.1481481677 | 178 | 14 | 5 | 27.6 | TDD | 735 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3269333 | 10 | 121.4677154774 | 31.1471234581 | 243 | 2 | 1 | 5.1 | FDD | 791 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3271298 | 3 | 121.4741135294 | 31.1449136089 | 333 | 10 | 1 | 12.3 | TDD | 782 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3271571 | 11 | 121.4649660258 | 31.1522183887 | 218 | 1 | 7 | 20.5 | FDD | 185 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3276497 | 1 | 121.4757994902 | 31.1451335626 | 199 | 5 | 7 | 4.8 | TDD | 289 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.788 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.810 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.925 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.925 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.630 | NREventA2 | measId:1;ServCellPCI:761;Se... |
| 2024-09-20 22:21:34.735 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:34.973 | NREventA5 | measId:3;ServCellPCI:761;Se... |
| 2024-09-20 22:21:35.020 | NRHandoverAttempt | SourcePCI:761;SourceNR-ARFC... |
| 2024-09-20 22:21:35.060 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.073 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.196 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.196 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276497 | 1 | 9.8774 | 16.7819 | -115.4386 | 8.0774 | 99.2728 | 0.0074 | 0.0185 |
| 2024_09_20 22:00 | 3265105 | 2 | 11.8599 | 10.5279 | -114.9299 | 14.5522 | 169.5534 | 0.0132 | 0.0036 |
| 2024_09_20 22:00 | 3271298 | 3 | 6.8509 | 5.9002 | -115.1733 | 13.9124 | 179.3019 | 0.0088 | 0.0038 |
| 2024_09_20 22:00 | 3238219 | 4 | 15.0410 | 7.7416 | -114.3986 | 18.0677 | 158.9787 | 0.0188 | 0.0122 |
| 2024_09_20 22:00 | 3238603 | 5 | 12.1986 | 19.4891 | -117.6717 | 7.6037 | 137.2391 | 0.0162 | 0.0198 |
| 2024_09_20 22:00 | 3268524 | 6 | 13.6134 | 18.0636 | -117.3818 | 10.1017 | 125.7252 | 0.0073 | 0.0055 |
| 2024_09_20 22:00 | 3247382 | 7 | 7.8857 | 12.9838 | -116.1734 | 3.1134 | 43.4379 | 0.0032 | 0.0000 |
| 2024_09_20 22:00 | 3215574 | 8 | 12.7926 | 9.3863 | -117.0036 | 3.0583 | 58.2394 | 0.0081 | 0.0082 |
| 2024_09_20 22:00 | 3218322 | 9 | 17.3959 | 11.3477 | -116.3659 | 3.1164 | 37.0861 | 0.0018 | 0.0194 |
| 2024_09_20 22:00 | 3269333 | 10 | 16.8011 | 6.0843 | -116.3535 | 4.9139 | 21.6038 | 0.0060 | 0.0077 |
| 2024_09_20 22:00 | 3271571 | 11 | 9.9605 | 9.1459 | -114.7350 | 3.4917 | 35.4252 | 0.0124 | 0.0046 |
| 2024_09_20 22:00 | 3252129 | 12 | 14.8132 | 8.6359 | -117.4050 | 4.3945 | 38.5029 | 0.0068 | 0.0030 |
| 2024_09_20 22:00 | 3218459 | 13 | 14.4278 | 12.0134 | -114.8454 | 4.4733 | 43.8558 | 0.0144 | 0.0072 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414012_15230233 | 504990 | 583 | -94.9 | 504990 | 660 | -95.0 | 504990 | 735 | -94.7 | 504990 | 782 |
| MR_1774414012_78D432C3 | 504990 | 583 | -97.2 | 504990 | 660 | -95.7 | 504990 | 735 | -94.1 | 504990 | 782 |
| MR_1774414012_A9089484 | 504990 | 583 | -97.1 | 504990 | 660 | -92.5 | 504990 | 735 | -95.6 | 504990 | 782 |
| MR_1774414012_E126B437 | 504990 | 583 | -97.1 | 504990 | 660 | -93.4 | 504990 | 735 | -93.1 | 504990 | 782 |
| MR_1774414012_5E78C15A | 504990 | 583 | -96.1 | 504990 | 660 | -95.1 | 504990 | 735 | -92.7 | 504990 | 782 |
| MR_1774414012_AC7553A4 | 504990 | 583 | -93.8 | 504990 | 660 | -93.5 | 504990 | 735 | -92.8 | 504990 | 782 |
| MR_1774414012_0AF7425A | 504990 | 583 | -96.9 | 504990 | 660 | -92.3 | 504990 | 735 | -94.4 | 504990 | 782 |

> *... 2개 열 생략 (전체 14열)*

---
