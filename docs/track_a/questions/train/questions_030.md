# Track A 문제 분석 — train[290]~train[299]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[290] ~ train[299] (10개)

## 목차

1. [문제 290: `a2294752-720...`](#290) — single-answer, 정답: C11
2. [문제 291: `ef6eef32-487...`](#291) — single-answer, 정답: C21
3. [문제 292: `37a77ecb-de1...`](#292) — single-answer, 정답: C12
4. [문제 293: `72967bfe-43b...`](#293) — single-answer, 정답: C6
5. [문제 294: `20180d32-2e6...`](#294) — single-answer, 정답: C9
6. [문제 295: `1b2bdcdb-032...`](#295) — single-answer, 정답: C9
7. [문제 296: `dda39d18-c15...`](#296) — single-answer, 정답: C22
8. [문제 297: `16cbff27-91f...`](#297) — single-answer, 정답: C15
9. [문제 298: `00d45095-5be...`](#298) — single-answer, 정답: C19
10. [문제 299: `eb2f6671-b1c...`](#299) — single-answer, 정답: C12

---

### 문제 290: `a2294752-720...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a2294752-720e-4652-81e1-d54cc68e1524` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Lift the tilt angle  of 3222684_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[290] topology](images/train_0290.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3264063_3 by 2 degrees
- `C2`: Decrease A3 Offset threshold for 3264063_3
- `C3`: Check test server and transmission issues
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264063_3
- `C5`: Add neighbor relationship between 3222684_4 and 3234369_1
- `C6`: Adjust the azimuth of 3222684_4 by 50 degrees
- `C7`: Lift the tilt angle of 3264063_3 by 2 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234369_1
- `C9`: Decrease transmission power for 3264063_3
- `C10`: Decrease transmission power for 3234369_1
- `C11`: Lift the tilt angle  of 3222684_4 by 10 degrees **← 정답**
- `C12`: Adjust the azimuth of 3264063_3 by 45 degrees
- `C13`: Increase transmission power for 3264063_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264063_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234369_1
- `C16`: Increase A3 Offset threshold for 3264063_3
- `C17`: Press down the tilt angle  of 3222684_4 by 10 degrees
- `C18`: Decrease A3 Offset threshold for 3234369_1
- `C19`: Increase A3 Offset threshold for 3234369_1
- `C20`: Increase transmission power for 3234369_1
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Add neighbor relationship between 3264063_3 and 3234369_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.254 | MS1 | 121.4656708672 | 31.1446198129 | 179 | 504990 | -88.98 | 14.77 | 482.14 | 0.10 | 2.14 | 1593 |
| 2024-09-20 22:21:32.166 | MS1 | 121.4656765213 | 31.1446310615 | 179 | 504990 | -86.03 | 13.60 | 517.92 | 0.05 | 2.92 | 1582 |
| 2024-09-20 22:21:33.537 | MS1 | 121.4656581783 | 31.1446291477 | 179 | 504990 | -88.02 | 13.16 | 575.18 | 0.11 | 2.54 | 1592 |
| 2024-09-20 22:21:34.610 | MS1 | 121.4656677412 | 31.1446256998 | 179 | 504990 | -85.49 | 14.55 | 90.82 | 0.03 | 2.81 | 1567 |
| 2024-09-20 22:21:35.104 | MS1 | 121.4656639270 | 31.1446239307 | 179 | 504990 | -86.36 | 13.16 | 76.70 | 0.15 | 2.43 | 1560 |
| 2024-09-20 22:21:36.450 | MS1 | 121.4656631722 | 31.1446239877 | 179 | 504990 | -91.33 | 17.32 | 88.60 | 0.10 | 2.81 | 1570 |
| 2024-09-20 22:21:37.570 | MS1 | 121.4656625671 | 31.1446346680 | 179 | 504990 | -90.75 | 12.43 | 79.12 | 0.07 | 2.40 | 1600 |
| 2024-09-20 22:21:38.865 | MS1 | 121.4656704385 | 31.1446182289 | 179 | 504990 | -91.58 | 9.37 | 59.62 | 0.04 | 2.37 | 1582 |
| 2024-09-20 22:21:39.334 | MS1 | 121.4656768465 | 31.1446342931 | 179 | 504990 | -91.92 | 10.48 | 101.98 | 0.01 | 2.06 | 1589 |
| 2024-09-20 22:21:40.608 | MS1 | 121.4656644858 | 31.1446308105 | 179 | 504990 | -91.26 | 9.78 | 571.89 | 0.01 | 2.69 | 1581 |
| 2024-09-20 22:21:41.536 | MS1 | 121.4656740655 | 31.1446214590 | 179 | 504990 | -92.56 | 9.86 | 518.52 | 0.05 | 2.89 | 1579 |
| 2024-09-20 22:21:42.433 | MS1 | 121.4656696978 | 31.1446306701 | 179 | 504990 | -90.00 | 9.29 | 342.55 | 0.09 | 2.84 | 1594 |

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
| 3222684 | 4 | 121.4709925074 | 31.1469792000 | 335 | 1 | 2 | 27.4 | TDD | 494 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3230602 | 2 | 121.4660110892 | 31.1473152682 | 61 | 11 | 9 | 36.9 | TDD | 514 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3234369 | 1 | 121.4707666169 | 31.1555890168 | 318 | 15 | 1 | 32.4 | TDD | 561 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3264063 | 3 | 121.4730819316 | 31.1512369121 | 179 | 0 | 2 | 41.1 | TDD | 179 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.540 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.564 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.711 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.711 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.360 | NREventA3 | measId:2;ServCellPCI:222;Se... |
| 2024-09-20 22:21:38.600 | NRHandoverAttempt | SourcePCI:222;SourceNR-ARFC... |
| 2024-09-20 22:21:38.633 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.643 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.781 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.781 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234369 | 1 | 5.5573 | 18.0482 | -115.1780 | 19.1855 | 162.8927 | 0.0064 | 0.0065 |
| 2024_09_20 22:00 | 3230602 | 2 | 6.2716 | 12.4202 | -115.6906 | 12.0822 | 128.6146 | 0.0040 | 0.0149 |
| 2024_09_20 22:00 | 3264063 | 3 | 79.0487 | 82.9007 | -116.4545 | 7.4958 | 113.0507 | 0.0013 | 0.0179 |
| 2024_09_20 22:00 | 3222684 | 4 | 12.2038 | 17.0378 | -116.1865 | 15.0816 | 148.0345 | 0.0008 | 0.0062 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415728_AC7D3B05 | 504990 | 179 | -84.2 | 504990 | 561 | -90.1 | 504990 | 494 | -98.6 | 504990 | 514 |
| MR_1774415728_C4831559 | 504990 | 179 | -83.6 | 504990 | 561 | -90.5 | 504990 | 494 | -101.2 | 504990 | 514 |
| MR_1774415728_8999105F | 504990 | 179 | -87.5 | 504990 | 561 | -93.2 | 504990 | 494 | -99.2 | 504990 | 514 |
| MR_1774415728_97632587 | 504990 | 179 | -87.4 | 504990 | 561 | -91.0 | 504990 | 494 | -101.2 | 504990 | 514 |
| MR_1774415728_95A02F27 | 504990 | 179 | -85.1 | 504990 | 561 | -91.7 | 504990 | 494 | -98.7 | 504990 | 514 |
| MR_1774415728_D434368C | 504990 | 179 | -85.4 | 504990 | 561 | -91.4 | 504990 | 494 | -100.2 | 504990 | 514 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 291: `ef6eef32-487...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ef6eef32-4873-46ab-ad5a-15f604a0931f` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease A3 Offset threshold for 3217459_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[291] topology](images/train_0291.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3272624_2
- `C2`: Decrease transmission power for 3272624_2
- `C3`: Increase A3 Offset threshold for 3217459_4
- `C4`: Increase transmission power for 3272624_2
- `C5`: Increase transmission power for 3217459_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272624_2
- `C7`: Check test server and transmission issues
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217459_4
- `C9`: Add neighbor relationship between 3217459_4 and 3272624_2
- `C10`: Decrease transmission power for 3217459_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272624_2
- `C12`: Lift the tilt angle  of 3272624_2 by 4 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Add neighbor relationship between 3264165_1 and 3272624_2
- `C15`: Increase A3 Offset threshold for 3272624_2
- `C16`: Adjust the azimuth of 3272624_2 by 50 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217459_4
- `C18`: Press down the tilt angle  of 3272624_2 by 4 degrees
- `C19`: Lift the tilt angle of 3217459_4 by 10 degrees
- `C20`: Adjust the azimuth of 3217459_4 by 50 degrees
- `C21`: Decrease A3 Offset threshold for 3217459_4 **← 정답**
- `C22`: Press down the tilt angle of 3217459_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.272 | MS1 | 121.4656732600 | 31.1446331434 | 830 | 504990 | -76.20 | 15.88 | 501.27 | 0.01 | 2.60 | 1585 |
| 2024-09-20 22:21:32.627 | MS1 | 121.4656779797 | 31.1446364690 | 830 | 504990 | -75.81 | 12.43 | 428.41 | 0.10 | 2.39 | 1575 |
| 2024-09-20 22:21:33.833 | MS1 | 121.4656680941 | 31.1446266428 | 830 | 504990 | -75.34 | 12.04 | 509.25 | 0.02 | 2.66 | 1575 |
| 2024-09-20 22:21:34.105 | MS1 | 121.4656642943 | 31.1446340686 | 830 | 504990 | -87.77 | -0.83 | 27.61 | 0.00 | 1.38 | 1574 |
| 2024-09-20 22:21:35.162 | MS1 | 121.4656645156 | 31.1446185682 | 830 | 504990 | -85.36 | -2.53 | 49.10 | 0.19 | 1.42 | 1560 |
| 2024-09-20 22:21:36.183 | MS1 | 121.4656631261 | 31.1446271786 | 830 | 504990 | -91.04 | -2.14 | 55.78 | 0.07 | 1.19 | 1577 |
| 2024-09-20 22:21:37.340 | MS1 | 121.4656608586 | 31.1446371466 | 830 | 504990 | -86.07 | -1.69 | 61.15 | 0.06 | 1.25 | 1563 |
| 2024-09-20 22:21:38.624 | MS1 | 121.4656641400 | 31.1446315400 | 830 | 504990 | -88.90 | -2.47 | 68.62 | 0.07 | 1.28 | 1567 |
| 2024-09-20 22:21:39.693 | MS1 | 121.4656643140 | 31.1446233156 | 794 | 504990 | -83.50 | 16.31 | 212.11 | 0.12 | 1.18 | 1563 |
| 2024-09-20 22:21:40.575 | MS1 | 121.4656771861 | 31.1446228122 | 794 | 504990 | -84.58 | 14.99 | 325.58 | 0.07 | 2.88 | 1596 |
| 2024-09-20 22:21:41.535 | MS1 | 121.4656689356 | 31.1446297830 | 794 | 504990 | -76.34 | 13.61 | 377.06 | 0.13 | 2.91 | 1571 |
| 2024-09-20 22:21:42.963 | MS1 | 121.4656593666 | 31.1446213987 | 794 | 504990 | -84.29 | 13.52 | 349.52 | 0.15 | 2.19 | 1567 |

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
| 3217459 | 4 | 121.4704276653 | 31.1503998126 | 334 | 7 | 3 | 37.8 | TDD | 830 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3257694 | 3 | 121.4649268046 | 31.1483692515 | 35 | 2 | 7 | 47.2 | TDD | 771 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3264165 | 1 | 121.4695360827 | 31.1447537959 | 346 | 8 | 4 | 40.4 | TDD | 296 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3272624 | 2 | 121.4710241292 | 31.1537813345 | 322 | 3 | 5 | 24.8 | TDD | 794 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.218 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.238 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.369 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.369 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.048 | NREventA3 | measId:2;ServCellPCI:329;Se... |
| 2024-09-20 22:21:38.288 | NRHandoverAttempt | SourcePCI:329;SourceNR-ARFC... |
| 2024-09-20 22:21:38.319 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.329 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.429 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.429 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264165 | 1 | 17.0354 | 7.9599 | -116.0665 | 10.5338 | 110.1391 | 0.0040 | 0.0161 |
| 2024_09_20 22:00 | 3272624 | 2 | 17.1727 | 15.5844 | -116.5493 | 7.0019 | 141.2749 | 0.0116 | 0.0140 |
| 2024_09_20 22:00 | 3257694 | 3 | 14.9605 | 6.3740 | -116.8244 | 19.9036 | 178.5874 | 0.0025 | 0.0197 |
| 2024_09_20 22:00 | 3217459 | 4 | 11.1024 | 16.3140 | -115.9948 | 13.2249 | 112.7581 | 0.0094 | 0.1590 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414397_9725BE99 | 504990 | 830 | -86.4 | 504990 | 794 | -80.5 | 504990 | 296 | -85.6 | 504990 | 771 |
| MR_1774414397_5CDBD23B | 504990 | 830 | -88.1 | 504990 | 794 | -81.4 | 504990 | 296 | -87.5 | 504990 | 771 |
| MR_1774414397_46B61BC7 | 504990 | 830 | -88.4 | 504990 | 794 | -81.2 | 504990 | 296 | -88.6 | 504990 | 771 |
| MR_1774414397_5D02543B | 504990 | 830 | -85.9 | 504990 | 794 | -81.8 | 504990 | 296 | -85.6 | 504990 | 771 |
| MR_1774414397_BF748F73 | 504990 | 794 | -81.9 | 504990 | 830 | -88.5 | 504990 | 296 | -88.5 | 504990 | 771 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 292: `37a77ecb-de1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `37a77ecb-de11-4fd9-8fcd-af72e854e4cd` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Add neighbor relationship between 3238432_2 and 3211055_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[292] topology](images/train_0292.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3238432_2 by 6 degrees
- `C2`: Increase A3 Offset threshold for 3211055_3
- `C3`: Press down the tilt angle of 3238432_2 by 6 degrees
- `C4`: Increase A3 Offset threshold for 3238432_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211055_3
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Check test server and transmission issues
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238432_2
- `C9`: Press down the tilt angle  of 3211055_3 by 2 degrees
- `C10`: Decrease transmission power for 3238432_2
- `C11`: Add neighbor relationship between 3256857_1 and 3211055_3
- `C12`: Add neighbor relationship between 3238432_2 and 3211055_3 **← 정답**
- `C13`: Decrease A3 Offset threshold for 3211055_3
- `C14`: Adjust the azimuth of 3211055_3 by 28 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211055_3
- `C16`: Lift the tilt angle  of 3211055_3 by 2 degrees
- `C17`: Decrease transmission power for 3211055_3
- `C18`: Increase transmission power for 3211055_3
- `C19`: Adjust the azimuth of 3238432_2 by 50 degrees
- `C20`: Decrease A3 Offset threshold for 3238432_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238432_2
- `C22`: Increase transmission power for 3238432_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.586 | MS1 | 121.4656762592 | 31.1446278507 | 316 | 504990 | -77.20 | 14.18 | 297.62 | 0.17 | 2.94 | 1594 |
| 2024-09-20 22:21:32.945 | MS1 | 121.4656746437 | 31.1446228746 | 316 | 504990 | -83.72 | 12.15 | 453.04 | 0.20 | 2.71 | 1579 |
| 2024-09-20 22:21:33.153 | MS1 | 121.4656618522 | 31.1446242072 | 316 | 504990 | -77.29 | 16.82 | 417.25 | 0.11 | 2.44 | 1583 |
| 2024-09-20 22:21:34.787 | MS1 | 121.4656761363 | 31.1446194624 | 316 | 504990 | -93.43 | -3.52 | 28.79 | 0.12 | 1.06 | 1578 |
| 2024-09-20 22:21:35.251 | MS1 | 121.4656721563 | 31.1446335458 | 316 | 504990 | -90.37 | -0.69 | 43.91 | 0.15 | 1.15 | 1571 |
| 2024-09-20 22:21:36.429 | MS1 | 121.4656765550 | 31.1446330247 | 316 | 504990 | -85.17 | -1.11 | 38.54 | 0.05 | 1.34 | 1567 |
| 2024-09-20 22:21:37.424 | MS1 | 121.4656598927 | 31.1446298095 | 316 | 504990 | -93.21 | -2.35 | 61.43 | 0.06 | 1.21 | 1580 |
| 2024-09-20 22:21:38.704 | MS1 | 121.4656616426 | 31.1446280891 | 316 | 504990 | -81.48 | 15.30 | 345.82 | 0.07 | 1.48 | 1562 |
| 2024-09-20 22:21:39.923 | MS1 | 121.4656754074 | 31.1446185073 | 316 | 504990 | -81.19 | 13.10 | 355.12 | 0.01 | 1.30 | 1587 |
| 2024-09-20 22:21:40.692 | MS1 | 121.4656620160 | 31.1446321288 | 316 | 504990 | -77.64 | 15.49 | 479.13 | 0.08 | 2.42 | 1592 |
| 2024-09-20 22:21:41.665 | MS1 | 121.4656760653 | 31.1446295368 | 316 | 504990 | -84.01 | 16.27 | 588.56 | 0.03 | 2.18 | 1570 |
| 2024-09-20 22:21:42.459 | MS1 | 121.4656613589 | 31.1446278703 | 316 | 504990 | -82.39 | 15.53 | 513.99 | 0.14 | 2.21 | 1593 |

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
| 3211055 | 3 | 121.4741057486 | 31.1484743074 | 214 | 0 | 1 | 28.3 | TDD | 292 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3238432 | 2 | 121.4687719627 | 31.1480134972 | 291 | 4 | 10 | 19.6 | TDD | 316 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3256857 | 1 | 121.4674000571 | 31.1479454718 | 284 | 1 | 12 | 27.8 | TDD | 553 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3262074 | 4 | 121.4757750981 | 31.1509011204 | 266 | 5 | 9 | 36.5 | TDD | 633 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.835 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.852 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.981 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.981 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.662 | NREventA3 | measId:2;ServCellPCI:743;Se... |
| 2024-09-20 22:21:35.662 | NREventA3 | measId:2;ServCellPCI:743;Se... |
| 2024-09-20 22:21:36.662 | NREventA3 | measId:2;ServCellPCI:743;Se... |
| 2024-09-20 22:21:39.162 | NRRRCReestablishAttempt | PCI:743 |
| 2024-09-20 22:21:39.172 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.182 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.302 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.302 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256857 | 1 | 11.7447 | 9.2647 | -116.7810 | 7.1998 | 154.1920 | 0.0148 | 0.0170 |
| 2024_09_20 22:00 | 3238432 | 2 | 15.4984 | 13.9466 | -114.9573 | 6.4688 | 156.8255 | 0.0117 | 0.1660 |
| 2024_09_20 22:00 | 3211055 | 3 | 7.0087 | 8.1239 | -114.4294 | 9.3819 | 121.6511 | 0.0044 | 0.0075 |
| 2024_09_20 22:00 | 3262074 | 4 | 15.3732 | 11.4570 | -117.1865 | 11.9113 | 195.9884 | 0.0059 | 0.0075 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413753_7126C684 | 504990 | 316 | -94.3 | 504990 | 292 | -87.8 | 504990 | 553 | -96.2 | 504990 | 633 |
| MR_1774413753_896C09B9 | 504990 | 316 | -94.4 | 504990 | 292 | -88.1 | 504990 | 553 | -96.2 | 504990 | 633 |
| MR_1774413753_F0EE21FD | 504990 | 316 | -92.4 | 504990 | 292 | -88.6 | 504990 | 553 | -98.7 | 504990 | 633 |
| MR_1774413753_1CAED24E | 504990 | 316 | -92.8 | 504990 | 292 | -85.9 | 504990 | 553 | -98.5 | 504990 | 633 |
| MR_1774413753_EEB5620B | 504990 | 316 | -91.7 | 504990 | 292 | -87.8 | 504990 | 553 | -98.0 | 504990 | 633 |
| MR_1774413753_D64C45F9 | 504990 | 292 | -86.9 | 504990 | 316 | -92.7 | 504990 | 553 | -96.7 | 504990 | 633 |
| MR_1774413753_B4A58010 | 504990 | 316 | -92.4 | 504990 | 292 | -88.3 | 504990 | 553 | -97.9 | 504990 | 633 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 293: `72967bfe-43b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `72967bfe-43bd-4fe2-ad3c-5715a1be4e58` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[293] topology](images/train_0293.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3220466_2 by 8 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262071_1
- `C3`: Press down the tilt angle of 3262071_1 by 8 degrees
- `C4`: Increase A3 Offset threshold for 3220466_2
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Check test server and transmission issues **← 정답**
- `C7`: Add neighbor relationship between 3262071_1 and 3220466_2
- `C8`: Add neighbor relationship between 3227788_3 and 3220466_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262071_1
- `C10`: Increase A3 Offset threshold for 3262071_1
- `C11`: Increase transmission power for 3262071_1
- `C12`: Lift the tilt angle of 3262071_1 by 8 degrees
- `C13`: Decrease transmission power for 3220466_2
- `C14`: Decrease A3 Offset threshold for 3262071_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220466_2
- `C16`: Decrease transmission power for 3262071_1
- `C17`: Decrease A3 Offset threshold for 3220466_2
- `C18`: Lift the tilt angle  of 3220466_2 by 8 degrees
- `C19`: Increase transmission power for 3220466_2
- `C20`: Adjust the azimuth of 3220466_2 by 28 degrees
- `C21`: Adjust the azimuth of 3262071_1 by 50 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220466_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.277 | MS1 | 121.4656657039 | 31.1446209037 | 296 | 504990 | -90.29 | 16.88 | 576.74 | 0.16 | 2.22 | 1584 |
| 2024-09-20 22:21:32.344 | MS1 | 121.4656756060 | 31.1446211548 | 296 | 504990 | -86.97 | 15.25 | 311.93 | 0.16 | 2.76 | 1592 |
| 2024-09-20 22:21:33.442 | MS1 | 121.4656643868 | 31.1446183292 | 296 | 504990 | -88.49 | 12.55 | 544.26 | 0.11 | 2.43 | 1587 |
| 2024-09-20 22:21:34.489 | MS1 | 121.4656724278 | 31.1446373657 | 296 | 504990 | -90.59 | 13.21 | 67.49 | 0.11 | 2.13 | 337 |
| 2024-09-20 22:21:35.809 | MS1 | 121.4656688800 | 31.1446240328 | 296 | 504990 | -87.86 | 14.06 | 59.52 | 0.04 | 2.14 | 442 |
| 2024-09-20 22:21:36.176 | MS1 | 121.4656688215 | 31.1446253201 | 296 | 504990 | -90.95 | 12.08 | 57.10 | 0.11 | 2.84 | 390 |
| 2024-09-20 22:21:37.512 | MS1 | 121.4656699546 | 31.1446232174 | 296 | 504990 | -89.93 | 11.97 | 55.40 | 0.15 | 2.32 | 320 |
| 2024-09-20 22:21:38.771 | MS1 | 121.4656699865 | 31.1446271299 | 296 | 504990 | -93.41 | 12.16 | 73.16 | 0.09 | 2.54 | 428 |
| 2024-09-20 22:21:39.275 | MS1 | 121.4656596628 | 31.1446287124 | 296 | 504990 | -89.09 | 9.33 | 60.87 | 0.17 | 2.09 | 427 |
| 2024-09-20 22:21:40.112 | MS1 | 121.4656668331 | 31.1446229793 | 296 | 504990 | -90.60 | 11.15 | 368.47 | 0.03 | 2.15 | 1567 |
| 2024-09-20 22:21:41.637 | MS1 | 121.4656710655 | 31.1446317219 | 296 | 504990 | -89.77 | 7.27 | 396.81 | 0.11 | 2.58 | 1566 |
| 2024-09-20 22:21:42.912 | MS1 | 121.4656694374 | 31.1446185798 | 296 | 504990 | -93.11 | 7.18 | 469.78 | 0.16 | 2.66 | 1585 |

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
| 3220466 | 2 | 121.4741526494 | 31.1482650019 | 271 | 6 | 1 | 29.6 | TDD | 505 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3227788 | 3 | 121.4709340052 | 31.1455552211 | 55 | 2 | 9 | 43.5 | TDD | 153 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3230167 | 4 | 121.4662465997 | 31.1449276189 | 204 | 0 | 0 | 49.9 | TDD | 365 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3262071 | 1 | 121.4744366149 | 31.1460119683 | 55 | 5 | 0 | 41.7 | TDD | 296 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.898 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.917 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.063 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.063 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.709 | NREventA3 | measId:2;ServCellPCI:916;Se... |
| 2024-09-20 22:21:37.949 | NRHandoverAttempt | SourcePCI:916;SourceNR-ARFC... |
| 2024-09-20 22:21:37.983 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.993 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.113 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.113 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262071 | 1 | 19.4243 | 8.5655 | -115.7492 | 13.7538 | 163.8064 | 0.0199 | 0.0069 |
| 2024_09_20 22:00 | 3220466 | 2 | 9.2328 | 15.0177 | -114.1124 | 10.7182 | 122.9899 | 0.0085 | 0.0105 |
| 2024_09_20 22:00 | 3227788 | 3 | 12.8471 | 14.0743 | -115.2813 | 9.3720 | 135.2872 | 0.0038 | 0.0173 |
| 2024_09_20 22:00 | 3230167 | 4 | 12.6002 | 16.5422 | -117.6446 | 19.5759 | 143.8349 | 0.0049 | 0.0108 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412450_F31B2D56 | 504990 | 296 | -89.8 | 504990 | 505 | -89.2 | 504990 | 153 | -102.9 | 504990 | 365 |
| MR_1774412450_A1E3F935 | 504990 | 296 | -91.8 | 504990 | 505 | -91.6 | 504990 | 153 | -101.1 | 504990 | 365 |
| MR_1774412450_1DEE5969 | 504990 | 296 | -90.5 | 504990 | 505 | -92.0 | 504990 | 153 | -103.2 | 504990 | 365 |
| MR_1774412450_5553E117 | 504990 | 296 | -91.3 | 504990 | 505 | -92.0 | 504990 | 153 | -101.1 | 504990 | 365 |
| MR_1774412450_521FD235 | 504990 | 296 | -91.2 | 504990 | 505 | -90.9 | 504990 | 153 | -101.0 | 504990 | 365 |
| MR_1774412450_BBD3CF5A | 504990 | 296 | -90.0 | 504990 | 505 | -89.1 | 504990 | 153 | -103.0 | 504990 | 365 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 294: `20180d32-2e6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `20180d32-2e67-46b3-8fd9-9ae519776251` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3270562_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[294] topology](images/train_0294.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3217937_1 and 3275518_2
- `C2`: Increase transmission power for 3270562_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275518_2
- `C4`: Press down the tilt angle of 3270562_4 by 3 degrees
- `C5`: Increase transmission power for 3275518_2
- `C6`: Lift the tilt angle  of 3275518_2 by 10 degrees
- `C7`: Decrease transmission power for 3275518_2
- `C8`: Increase A3 Offset threshold for 3270562_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270562_4 **← 정답**
- `C10`: Adjust the azimuth of 3270562_4 by 21 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270562_4
- `C12`: Check test server and transmission issues
- `C13`: Increase A3 Offset threshold for 3275518_2
- `C14`: Press down the tilt angle  of 3275518_2 by 10 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275518_2
- `C16`: Lift the tilt angle of 3270562_4 by 3 degrees
- `C17`: Decrease transmission power for 3270562_4
- `C18`: Adjust the azimuth of 3275518_2 by 50 degrees
- `C19`: Decrease A3 Offset threshold for 3270562_4
- `C20`: Add neighbor relationship between 3270562_4 and 3275518_2
- `C21`: Decrease A3 Offset threshold for 3275518_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.125 | MS1 | 121.4656642337 | 31.1446199187 | 917 | 504990 | -85.36 | 14.25 | 344.39 | 0.19 | 2.61 | 1569 |
| 2024-09-20 22:21:32.346 | MS1 | 121.4656754093 | 31.1446350898 | 917 | 504990 | -86.59 | 14.70 | 593.86 | 0.13 | 2.06 | 1597 |
| 2024-09-20 22:21:33.249 | MS1 | 121.4656629186 | 31.1446283400 | 917 | 504990 | -89.57 | 12.81 | 513.33 | 0.19 | 2.76 | 1574 |
| 2024-09-20 22:21:34.192 | MS1 | 121.4656594485 | 31.1446370092 | 917 | 504990 | -86.47 | 14.79 | 78.97 | 0.50 | 2.23 | 572 |
| 2024-09-20 22:21:35.825 | MS1 | 121.4656653070 | 31.1446197958 | 917 | 504990 | -86.83 | 16.44 | 101.02 | 0.70 | 2.50 | 510 |
| 2024-09-20 22:21:36.847 | MS1 | 121.4656659250 | 31.1446198163 | 917 | 504990 | -89.60 | 16.27 | 63.20 | 0.61 | 2.42 | 587 |
| 2024-09-20 22:21:37.850 | MS1 | 121.4656672604 | 31.1446215443 | 917 | 504990 | -89.91 | 9.58 | 90.74 | 0.57 | 2.92 | 585 |
| 2024-09-20 22:21:38.504 | MS1 | 121.4656713245 | 31.1446312560 | 917 | 504990 | -92.56 | 11.65 | 87.68 | 0.52 | 2.85 | 682 |
| 2024-09-20 22:21:39.787 | MS1 | 121.4656668133 | 31.1446223273 | 917 | 504990 | -89.58 | 10.81 | 103.17 | 0.66 | 2.95 | 561 |
| 2024-09-20 22:21:40.305 | MS1 | 121.4656726879 | 31.1446233495 | 917 | 504990 | -91.61 | 7.62 | 497.90 | 0.06 | 2.14 | 1565 |
| 2024-09-20 22:21:41.186 | MS1 | 121.4656740386 | 31.1446279949 | 917 | 504990 | -92.11 | 11.21 | 551.51 | 0.10 | 2.71 | 1593 |
| 2024-09-20 22:21:42.171 | MS1 | 121.4656715618 | 31.1446355955 | 917 | 504990 | -93.76 | 11.04 | 584.21 | 0.04 | 2.64 | 1574 |

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
| 3217937 | 1 | 121.4655097462 | 31.1451061175 | 308 | 14 | 10 | 47.1 | TDD | 26 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3224910 | 3 | 121.4662721043 | 31.1472054294 | 308 | 3 | 2 | 22.6 | TDD | 861 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3270562 | 4 | 121.4660432102 | 31.1559823865 | 203 | 2 | 9 | 19.9 | TDD | 917 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3275518 | 2 | 121.4657219870 | 31.1452713726 | 268 | 12 | 1 | 18.9 | TDD | 260 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.612 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.637 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.761 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.761 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.440 | NREventA3 | measId:2;ServCellPCI:737;Se... |
| 2024-09-20 22:21:38.680 | NRHandoverAttempt | SourcePCI:737;SourceNR-ARFC... |
| 2024-09-20 22:21:38.725 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.740 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.842 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.842 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217937 | 1 | 6.5368 | 19.3481 | -115.1975 | 14.0635 | 149.6624 | 0.0180 | 0.0113 |
| 2024_09_20 22:00 | 3275518 | 2 | 10.4187 | 8.5309 | -116.6502 | 17.2164 | 80.0541 | 0.0115 | 0.0172 |
| 2024_09_20 22:00 | 3224910 | 3 | 7.1347 | 8.9425 | -114.2101 | 11.1257 | 190.7035 | 0.0181 | 0.0079 |
| 2024_09_20 22:00 | 3270562 | 4 | 6.3962 | 6.1583 | -115.0484 | 9.5045 | 126.8253 | 0.0170 | 0.0047 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416981_8D245E5A | 504990 | 917 | -84.6 | 504990 | 260 | -89.2 | 504990 | 26 | -96.5 | 504990 | 861 |
| MR_1774416981_0771B3BC | 504990 | 917 | -85.6 | 504990 | 260 | -90.5 | 504990 | 26 | -95.6 | 504990 | 861 |
| MR_1774416981_F8FC3653 | 504990 | 917 | -87.0 | 504990 | 260 | -90.0 | 504990 | 26 | -96.7 | 504990 | 861 |
| MR_1774416981_82AF36B2 | 504990 | 917 | -87.0 | 504990 | 260 | -88.6 | 504990 | 26 | -98.5 | 504990 | 861 |
| MR_1774416981_F2F86BDC | 504990 | 917 | -86.8 | 504990 | 260 | -88.2 | 504990 | 26 | -98.5 | 504990 | 861 |
| MR_1774416981_6C4081DA | 504990 | 917 | -88.2 | 504990 | 260 | -89.5 | 504990 | 26 | -98.2 | 504990 | 861 |
| MR_1774416981_AC8D3724 | 504990 | 917 | -87.0 | 504990 | 260 | -87.8 | 504990 | 26 | -96.2 | 504990 | 861 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 295: `1b2bdcdb-032...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1b2bdcdb-0329-4c74-976b-a4fcbd375cc5` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Lift the tilt angle  of 3222166_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[295] topology](images/train_0295.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231839_3
- `C2`: Decrease transmission power for 3259883_2
- `C3`: Press down the tilt angle  of 3222166_1 by 10 degrees
- `C4`: Press down the tilt angle of 3259883_2 by 4 degrees
- `C5`: Increase A3 Offset threshold for 3259883_2
- `C6`: Add neighbor relationship between 3222166_1 and 3231839_3
- `C7`: Lift the tilt angle of 3259883_2 by 4 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259883_2
- `C9`: Lift the tilt angle  of 3222166_1 by 10 degrees **← 정답**
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259883_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231839_3
- `C12`: Decrease A3 Offset threshold for 3231839_3
- `C13`: Check test server and transmission issues
- `C14`: Add neighbor relationship between 3259883_2 and 3231839_3
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease transmission power for 3231839_3
- `C17`: Increase A3 Offset threshold for 3231839_3
- `C18`: Decrease A3 Offset threshold for 3259883_2
- `C19`: Adjust the azimuth of 3259883_2 by 14 degrees
- `C20`: Increase transmission power for 3259883_2
- `C21`: Increase transmission power for 3231839_3
- `C22`: Adjust the azimuth of 3222166_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.367 | MS1 | 121.4656702213 | 31.1446252770 | 855 | 504990 | -85.50 | 14.73 | 594.68 | 0.13 | 2.57 | 1582 |
| 2024-09-20 22:21:32.337 | MS1 | 121.4656715506 | 31.1446330983 | 855 | 504990 | -88.53 | 12.01 | 544.95 | 0.01 | 2.49 | 1570 |
| 2024-09-20 22:21:33.438 | MS1 | 121.4656666449 | 31.1446354725 | 855 | 504990 | -88.34 | 16.14 | 391.83 | 0.08 | 2.57 | 1599 |
| 2024-09-20 22:21:34.703 | MS1 | 121.4656679393 | 31.1446318546 | 855 | 504990 | -90.64 | 16.56 | 98.69 | 0.00 | 2.67 | 1575 |
| 2024-09-20 22:21:35.499 | MS1 | 121.4656776071 | 31.1446257015 | 855 | 504990 | -91.97 | 16.80 | 43.44 | 0.11 | 2.51 | 1587 |
| 2024-09-20 22:21:36.112 | MS1 | 121.4656712579 | 31.1446370930 | 855 | 504990 | -90.59 | 16.30 | 77.33 | 0.08 | 2.87 | 1565 |
| 2024-09-20 22:21:37.534 | MS1 | 121.4656602234 | 31.1446341843 | 855 | 504990 | -91.69 | 7.10 | 80.93 | 0.08 | 2.70 | 1565 |
| 2024-09-20 22:21:38.899 | MS1 | 121.4656626404 | 31.1446230207 | 855 | 504990 | -90.98 | 12.75 | 77.42 | 0.16 | 2.12 | 1578 |
| 2024-09-20 22:21:39.269 | MS1 | 121.4656666024 | 31.1446354973 | 855 | 504990 | -90.11 | 10.63 | 47.20 | 0.15 | 2.16 | 1570 |
| 2024-09-20 22:21:40.136 | MS1 | 121.4656732373 | 31.1446193100 | 855 | 504990 | -93.80 | 8.53 | 507.63 | 0.09 | 2.47 | 1594 |
| 2024-09-20 22:21:41.847 | MS1 | 121.4656593320 | 31.1446242432 | 855 | 504990 | -90.74 | 8.08 | 467.31 | 0.13 | 2.64 | 1577 |
| 2024-09-20 22:21:42.719 | MS1 | 121.4656771097 | 31.1446295215 | 855 | 504990 | -89.93 | 8.52 | 355.89 | 0.17 | 2.90 | 1583 |

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
| 3220965 | 4 | 121.4721676302 | 31.1531718767 | 202 | 8 | 11 | 35.5 | TDD | 7 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3222166 | 1 | 121.4681386639 | 31.1535106664 | 335 | 14 | 10 | 34.1 | TDD | 961 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3231839 | 3 | 121.4724191959 | 31.1470389658 | 338 | 12 | 4 | 41.5 | TDD | 206 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3259883 | 2 | 121.4651766185 | 31.1551106655 | 164 | 2 | 11 | 33.9 | TDD | 855 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.527 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.542 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.645 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.645 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.360 | NREventA3 | measId:2;ServCellPCI:507;Se... |
| 2024-09-20 22:21:38.600 | NRHandoverAttempt | SourcePCI:507;SourceNR-ARFC... |
| 2024-09-20 22:21:38.650 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.661 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.788 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.788 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222166 | 1 | 7.7229 | 19.4611 | -116.6314 | 7.1111 | 102.8201 | 0.0166 | 0.0138 |
| 2024_09_20 22:00 | 3259883 | 2 | 80.2877 | 94.5548 | -116.1109 | 12.5755 | 83.5941 | 0.0026 | 0.0052 |
| 2024_09_20 22:00 | 3231839 | 3 | 6.4009 | 5.1553 | -117.3676 | 18.5652 | 95.1863 | 0.0022 | 0.0160 |
| 2024_09_20 22:00 | 3220965 | 4 | 15.8151 | 10.1389 | -117.5224 | 13.5307 | 183.3295 | 0.0145 | 0.0053 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417164_3ECDB14F | 504990 | 855 | -89.3 | 504990 | 206 | -88.9 | 504990 | 961 | -99.3 | 504990 | 7 |
| MR_1774417164_63D1DFD8 | 504990 | 855 | -91.1 | 504990 | 206 | -90.3 | 504990 | 961 | -97.6 | 504990 | 7 |
| MR_1774417164_B44BC205 | 504990 | 855 | -90.4 | 504990 | 206 | -88.5 | 504990 | 961 | -98.4 | 504990 | 7 |
| MR_1774417164_D9608A9F | 504990 | 855 | -90.7 | 504990 | 206 | -91.5 | 504990 | 961 | -99.7 | 504990 | 7 |
| MR_1774417164_6079EF14 | 504990 | 855 | -89.0 | 504990 | 206 | -91.7 | 504990 | 961 | -99.9 | 504990 | 7 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 296: `dda39d18-c15...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dda39d18-c159-4940-b81e-0bf801e1ed6c` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Add neighbor relationship between 3273326_3 and 3223519_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[296] topology](images/train_0296.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3273326_3
- `C2`: Adjust the azimuth of 3273326_3 by 50 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273326_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223519_2
- `C5`: Decrease transmission power for 3223519_2
- `C6`: Press down the tilt angle of 3273326_3 by 10 degrees
- `C7`: Press down the tilt angle  of 3223519_2 by 5 degrees
- `C8`: Increase transmission power for 3223519_2
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Add neighbor relationship between 3224375_4 and 3223519_2
- `C11`: Lift the tilt angle  of 3223519_2 by 5 degrees
- `C12`: Lift the tilt angle of 3273326_3 by 10 degrees
- `C13`: Adjust the azimuth of 3223519_2 by 22 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223519_2
- `C15`: Check test server and transmission issues
- `C16`: Increase A3 Offset threshold for 3273326_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273326_3
- `C18`: Increase A3 Offset threshold for 3223519_2
- `C19`: Decrease transmission power for 3273326_3
- `C20`: Increase transmission power for 3273326_3
- `C21`: Decrease A3 Offset threshold for 3223519_2
- `C22`: Add neighbor relationship between 3273326_3 and 3223519_2 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.916 | MS1 | 121.4656649726 | 31.1446207020 | 254 | 504990 | -79.10 | 12.24 | 462.15 | 0.05 | 2.80 | 1561 |
| 2024-09-20 22:21:32.495 | MS1 | 121.4656721314 | 31.1446370275 | 254 | 504990 | -81.91 | 13.72 | 411.42 | 0.13 | 2.01 | 1560 |
| 2024-09-20 22:21:33.333 | MS1 | 121.4656679604 | 31.1446263680 | 254 | 504990 | -79.87 | 16.92 | 547.04 | 0.05 | 2.83 | 1581 |
| 2024-09-20 22:21:34.739 | MS1 | 121.4656627925 | 31.1446315233 | 254 | 504990 | -85.96 | -0.48 | 34.92 | 0.10 | 1.08 | 1581 |
| 2024-09-20 22:21:35.887 | MS1 | 121.4656700459 | 31.1446289969 | 254 | 504990 | -87.75 | -0.19 | 71.31 | 0.12 | 1.08 | 1587 |
| 2024-09-20 22:21:36.489 | MS1 | 121.4656654892 | 31.1446206545 | 254 | 504990 | -87.05 | -1.03 | 33.29 | 0.09 | 1.05 | 1593 |
| 2024-09-20 22:21:37.618 | MS1 | 121.4656601224 | 31.1446235995 | 254 | 504990 | -86.70 | -2.50 | 35.47 | 0.11 | 1.22 | 1598 |
| 2024-09-20 22:21:38.504 | MS1 | 121.4656620371 | 31.1446333760 | 254 | 504990 | -82.48 | 12.50 | 364.38 | 0.04 | 1.07 | 1580 |
| 2024-09-20 22:21:39.633 | MS1 | 121.4656606332 | 31.1446307324 | 254 | 504990 | -81.03 | 16.93 | 367.41 | 0.19 | 1.25 | 1578 |
| 2024-09-20 22:21:40.500 | MS1 | 121.4656594531 | 31.1446344563 | 254 | 504990 | -78.90 | 14.04 | 341.20 | 0.17 | 2.94 | 1600 |
| 2024-09-20 22:21:41.985 | MS1 | 121.4656592439 | 31.1446370018 | 254 | 504990 | -78.16 | 14.21 | 292.88 | 0.18 | 2.50 | 1565 |
| 2024-09-20 22:21:42.941 | MS1 | 121.4656613549 | 31.1446352618 | 254 | 504990 | -81.63 | 12.30 | 363.75 | 0.08 | 2.28 | 1563 |

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
| 3223519 | 2 | 121.4646117997 | 31.1485396439 | 189 | 2 | 0 | 23.8 | TDD | 650 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3224375 | 4 | 121.4644015758 | 31.1518447464 | 173 | 12 | 1 | 27.1 | TDD | 138 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3241289 | 1 | 121.4655506588 | 31.1499052889 | 229 | 5 | 1 | 31.7 | TDD | 536 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3273326 | 3 | 121.4732305788 | 31.1553834427 | 117 | 12 | 9 | 39.3 | TDD | 254 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.942 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.964 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.078 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.078 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.815 | NREventA3 | measId:2;ServCellPCI:83;Ser... |
| 2024-09-20 22:21:35.815 | NREventA3 | measId:2;ServCellPCI:83;Ser... |
| 2024-09-20 22:21:36.815 | NREventA3 | measId:2;ServCellPCI:83;Ser... |
| 2024-09-20 22:21:39.315 | NRRRCReestablishAttempt | PCI:83 |
| 2024-09-20 22:21:39.333 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.343 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.465 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.465 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241289 | 1 | 9.3607 | 6.2827 | -115.3243 | 12.4399 | 177.0544 | 0.0128 | 0.0002 |
| 2024_09_20 22:00 | 3223519 | 2 | 18.7647 | 17.1487 | -116.1647 | 18.2039 | 185.5074 | 0.0185 | 0.0042 |
| 2024_09_20 22:00 | 3273326 | 3 | 9.3351 | 8.7734 | -115.9032 | 18.8086 | 162.0561 | 0.0200 | 0.1614 |
| 2024_09_20 22:00 | 3224375 | 4 | 18.2054 | 11.7913 | -117.8223 | 11.6373 | 121.5887 | 0.0009 | 0.0142 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412276_40BE7DAB | 504990 | 650 | -83.0 | 504990 | 254 | -85.0 | 504990 | 138 | -82.9 | 504990 | 536 |
| MR_1774412276_61EE1167 | 504990 | 254 | -87.8 | 504990 | 650 | -82.8 | 504990 | 138 | -84.5 | 504990 | 536 |
| MR_1774412276_513264B1 | 504990 | 254 | -86.7 | 504990 | 650 | -79.3 | 504990 | 138 | -81.7 | 504990 | 536 |
| MR_1774412276_DA3C24F9 | 504990 | 650 | -80.5 | 504990 | 254 | -84.5 | 504990 | 138 | -82.3 | 504990 | 536 |
| MR_1774412276_107002F7 | 504990 | 650 | -80.6 | 504990 | 254 | -87.3 | 504990 | 138 | -81.8 | 504990 | 536 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 297: `16cbff27-91f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `16cbff27-91ff-4939-b2b9-aae890190c95` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[297] topology](images/train_0297.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease transmission power for 3222031_1
- `C3`: Lift the tilt angle  of 3222031_1 by 5 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227629_4
- `C5`: Increase transmission power for 3222031_1
- `C6`: Press down the tilt angle of 3227629_4 by 10 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227629_4
- `C8`: Add neighbor relationship between 3235662_2 and 3222031_1
- `C9`: Press down the tilt angle  of 3222031_1 by 5 degrees
- `C10`: Lift the tilt angle of 3227629_4 by 10 degrees
- `C11`: Increase A3 Offset threshold for 3222031_1
- `C12`: Adjust the azimuth of 3222031_1 by 44 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222031_1
- `C14`: Increase transmission power for 3227629_4
- `C15`: Check test server and transmission issues **← 정답**
- `C16`: Decrease transmission power for 3227629_4
- `C17`: Add neighbor relationship between 3227629_4 and 3222031_1
- `C18`: Decrease A3 Offset threshold for 3222031_1
- `C19`: Increase A3 Offset threshold for 3227629_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222031_1
- `C21`: Decrease A3 Offset threshold for 3227629_4
- `C22`: Adjust the azimuth of 3227629_4 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.161 | MS1 | 121.4656693176 | 31.1446376381 | 181 | 504990 | -89.11 | 14.47 | 591.35 | 0.18 | 2.55 | 1578 |
| 2024-09-20 22:21:32.588 | MS1 | 121.4656672883 | 31.1446180424 | 181 | 504990 | -91.06 | 14.48 | 475.30 | 0.13 | 2.66 | 1575 |
| 2024-09-20 22:21:33.497 | MS1 | 121.4656678818 | 31.1446294417 | 181 | 504990 | -91.82 | 13.65 | 435.50 | 0.17 | 2.60 | 1574 |
| 2024-09-20 22:21:34.573 | MS1 | 121.4656630282 | 31.1446191734 | 181 | 504990 | -85.69 | 16.17 | 68.42 | 0.05 | 2.19 | 347 |
| 2024-09-20 22:21:35.153 | MS1 | 121.4656597982 | 31.1446342178 | 181 | 504990 | -87.75 | 13.25 | 90.21 | 0.08 | 2.84 | 377 |
| 2024-09-20 22:21:36.765 | MS1 | 121.4656696597 | 31.1446368080 | 181 | 504990 | -91.44 | 13.58 | 79.58 | 0.17 | 2.47 | 446 |
| 2024-09-20 22:21:37.633 | MS1 | 121.4656745828 | 31.1446274072 | 181 | 504990 | -90.24 | 7.67 | 87.05 | 0.01 | 2.60 | 368 |
| 2024-09-20 22:21:38.230 | MS1 | 121.4656598400 | 31.1446246664 | 181 | 504990 | -93.46 | 9.46 | 81.84 | 0.17 | 2.83 | 453 |
| 2024-09-20 22:21:39.690 | MS1 | 121.4656601843 | 31.1446294043 | 181 | 504990 | -89.54 | 9.20 | 79.40 | 0.18 | 2.30 | 370 |
| 2024-09-20 22:21:40.369 | MS1 | 121.4656740760 | 31.1446263882 | 181 | 504990 | -89.88 | 11.77 | 480.41 | 0.05 | 2.62 | 1594 |
| 2024-09-20 22:21:41.805 | MS1 | 121.4656743925 | 31.1446323329 | 181 | 504990 | -91.80 | 9.89 | 414.30 | 0.01 | 2.93 | 1583 |
| 2024-09-20 22:21:42.647 | MS1 | 121.4656696638 | 31.1446311212 | 181 | 504990 | -89.97 | 10.31 | 501.22 | 0.11 | 2.45 | 1573 |

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
| 3222031 | 1 | 121.4659214124 | 31.1534753820 | 225 | 2 | 0 | 48.4 | TDD | 313 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3223855 | 3 | 121.4658221047 | 31.1528931485 | 4 | 4 | 9 | 48.7 | TDD | 225 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3227629 | 4 | 121.4704471467 | 31.1517766295 | 133 | 8 | 7 | 24.2 | TDD | 181 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3235662 | 2 | 121.4641180257 | 31.1482976450 | 92 | 0 | 0 | 41.6 | TDD | 549 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.980 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.004 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.154 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.154 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.782 | NREventA3 | measId:2;ServCellPCI:582;Se... |
| 2024-09-20 22:21:38.022 | NRHandoverAttempt | SourcePCI:582;SourceNR-ARFC... |
| 2024-09-20 22:21:38.060 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.072 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.196 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.196 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222031 | 1 | 10.8281 | 18.5722 | -117.5921 | 12.2158 | 118.6207 | 0.0034 | 0.0069 |
| 2024_09_20 22:00 | 3235662 | 2 | 17.5677 | 11.7668 | -117.8041 | 8.2719 | 195.0780 | 0.0002 | 0.0102 |
| 2024_09_20 22:00 | 3223855 | 3 | 19.0052 | 17.6458 | -116.5642 | 5.6333 | 196.6755 | 0.0110 | 0.0165 |
| 2024_09_20 22:00 | 3227629 | 4 | 19.1784 | 13.0464 | -116.5593 | 10.6969 | 144.9663 | 0.0034 | 0.0170 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416485_3C459B01 | 504990 | 181 | -84.0 | 504990 | 313 | -96.1 | 504990 | 549 | -99.9 | 504990 | 225 |
| MR_1774416485_4AB40B97 | 504990 | 181 | -84.4 | 504990 | 313 | -95.1 | 504990 | 549 | -101.0 | 504990 | 225 |
| MR_1774416485_FA512CAA | 504990 | 181 | -85.6 | 504990 | 313 | -96.3 | 504990 | 549 | -99.3 | 504990 | 225 |
| MR_1774416485_9A4432CF | 504990 | 181 | -87.6 | 504990 | 313 | -95.2 | 504990 | 549 | -98.8 | 504990 | 225 |
| MR_1774416485_0C6C2A3E | 504990 | 181 | -85.5 | 504990 | 313 | -95.1 | 504990 | 549 | -99.8 | 504990 | 225 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 298: `00d45095-5be...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `00d45095-5be8-4800-9150-15a7f1057a77` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3222959_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[298] topology](images/train_0298.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease A3 Offset threshold for 3243840_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243840_4
- `C4`: Increase transmission power for 3243840_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243840_4
- `C6`: Check test server and transmission issues
- `C7`: Increase A3 Offset threshold for 3243840_4
- `C8`: Increase A3 Offset threshold for 3222959_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222959_3
- `C10`: Lift the tilt angle  of 3243840_4 by 10 degrees
- `C11`: Press down the tilt angle of 3222959_3 by 5 degrees
- `C12`: Press down the tilt angle  of 3243840_4 by 10 degrees
- `C13`: Decrease transmission power for 3222959_3
- `C14`: Add neighbor relationship between 3232940_1 and 3243840_4
- `C15`: Increase transmission power for 3222959_3
- `C16`: Adjust the azimuth of 3222959_3 by 21 degrees
- `C17`: Decrease transmission power for 3243840_4
- `C18`: Lift the tilt angle of 3222959_3 by 5 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222959_3 **← 정답**
- `C20`: Adjust the azimuth of 3243840_4 by 50 degrees
- `C21`: Decrease A3 Offset threshold for 3222959_3
- `C22`: Add neighbor relationship between 3222959_3 and 3243840_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.968 | MS1 | 121.4656754805 | 31.1446253821 | 605 | 504990 | -85.78 | 15.76 | 546.59 | 0.06 | 2.37 | 1577 |
| 2024-09-20 22:21:32.746 | MS1 | 121.4656695075 | 31.1446328669 | 605 | 504990 | -88.63 | 16.56 | 503.82 | 0.16 | 2.32 | 1585 |
| 2024-09-20 22:21:33.294 | MS1 | 121.4656772745 | 31.1446284206 | 605 | 504990 | -86.39 | 15.93 | 483.39 | 0.15 | 2.89 | 1560 |
| 2024-09-20 22:21:34.189 | MS1 | 121.4656770783 | 31.1446220281 | 605 | 504990 | -90.11 | 16.53 | 83.96 | 0.67 | 2.08 | 689 |
| 2024-09-20 22:21:35.538 | MS1 | 121.4656609514 | 31.1446305023 | 605 | 504990 | -90.17 | 15.23 | 82.70 | 0.57 | 2.66 | 700 |
| 2024-09-20 22:21:36.550 | MS1 | 121.4656588660 | 31.1446322756 | 605 | 504990 | -91.25 | 15.14 | 93.39 | 0.63 | 2.93 | 657 |
| 2024-09-20 22:21:37.365 | MS1 | 121.4656760809 | 31.1446290928 | 605 | 504990 | -90.93 | 8.57 | 53.14 | 0.65 | 2.79 | 665 |
| 2024-09-20 22:21:38.438 | MS1 | 121.4656752728 | 31.1446239541 | 605 | 504990 | -93.71 | 8.06 | 66.78 | 0.58 | 2.44 | 595 |
| 2024-09-20 22:21:39.636 | MS1 | 121.4656660872 | 31.1446268968 | 605 | 504990 | -93.05 | 7.54 | 85.25 | 0.64 | 2.06 | 576 |
| 2024-09-20 22:21:40.802 | MS1 | 121.4656612980 | 31.1446303765 | 605 | 504990 | -91.20 | 11.56 | 494.52 | 0.16 | 2.78 | 1596 |
| 2024-09-20 22:21:41.149 | MS1 | 121.4656630109 | 31.1446240985 | 605 | 504990 | -91.76 | 8.01 | 351.48 | 0.16 | 2.52 | 1599 |
| 2024-09-20 22:21:42.274 | MS1 | 121.4656644699 | 31.1446213197 | 605 | 504990 | -93.84 | 12.50 | 543.52 | 0.16 | 2.70 | 1582 |

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
| 3222959 | 3 | 121.4642386463 | 31.1548023209 | 152 | 4 | 11 | 17.0 | TDD | 605 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3232940 | 1 | 121.4676861409 | 31.1458204316 | 97 | 3 | 10 | 46.3 | TDD | 819 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3243840 | 4 | 121.4658900501 | 31.1496330820 | 304 | 13 | 6 | 41.4 | TDD | 590 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3257879 | 2 | 121.4704734205 | 31.1517904832 | 359 | 5 | 12 | 49.8 | TDD | 196 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.857 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.881 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.988 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.988 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.709 | NREventA3 | measId:2;ServCellPCI:217;Se... |
| 2024-09-20 22:21:37.949 | NRHandoverAttempt | SourcePCI:217;SourceNR-ARFC... |
| 2024-09-20 22:21:37.994 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.009 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.133 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.133 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232940 | 1 | 5.0372 | 8.4933 | -114.1471 | 11.6808 | 182.5563 | 0.0109 | 0.0064 |
| 2024_09_20 22:00 | 3257879 | 2 | 13.9317 | 11.3314 | -115.6169 | 7.9849 | 196.1185 | 0.0100 | 0.0127 |
| 2024_09_20 22:00 | 3222959 | 3 | 15.9519 | 11.1722 | -115.8767 | 11.7698 | 109.2081 | 0.0051 | 0.0037 |
| 2024_09_20 22:00 | 3243840 | 4 | 13.2906 | 16.3241 | -114.4210 | 15.3823 | 145.1124 | 0.0184 | 0.0050 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416152_B24F6AF4 | 504990 | 605 | -90.0 | 504990 | 590 | -97.6 | 504990 | 819 | -101.3 | 504990 | 196 |
| MR_1774416152_B3CC0843 | 504990 | 605 | -88.3 | 504990 | 590 | -95.0 | 504990 | 819 | -102.5 | 504990 | 196 |
| MR_1774416152_4861A1CE | 504990 | 605 | -92.1 | 504990 | 590 | -96.6 | 504990 | 819 | -99.6 | 504990 | 196 |
| MR_1774416152_711CFD22 | 504990 | 605 | -89.6 | 504990 | 590 | -95.1 | 504990 | 819 | -103.0 | 504990 | 196 |
| MR_1774416152_0686EF07 | 504990 | 605 | -88.5 | 504990 | 590 | -94.6 | 504990 | 819 | -103.0 | 504990 | 196 |
| MR_1774416152_57EFB85E | 504990 | 605 | -90.1 | 504990 | 590 | -95.0 | 504990 | 819 | -100.9 | 504990 | 196 |
| MR_1774416152_79F8D155 | 504990 | 605 | -89.6 | 504990 | 590 | -96.5 | 504990 | 819 | -100.0 | 504990 | 196 |
| MR_1774416152_9B3F3316 | 504990 | 605 | -88.4 | 504990 | 590 | -94.8 | 504990 | 819 | -100.9 | 504990 | 196 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 299: `eb2f6671-b1c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `eb2f6671-b1cb-4c33-a960-5a9cf5c9f410` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247443_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[299] topology](images/train_0299.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3271433_3 by 5 degrees
- `C2`: Increase transmission power for 3247443_5
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271433_3
- `C4`: Decrease transmission power for 3247443_5
- `C5`: Increase transmission power for 3271433_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271433_3
- `C7`: Add neighbor relationship between 3257024_12 and 3271433_3
- `C8`: Press down the tilt angle  of 3271433_3 by 5 degrees
- `C9`: Adjust the azimuth of 3247443_5 by 49 degrees
- `C10`: Check test server and transmission issues
- `C11`: Decrease A3 Offset threshold for 3247443_5
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247443_5 **← 정답**
- `C13`: Add neighbor relationship between 3247443_5 and 3271433_3
- `C14`: Decrease A3 Offset threshold for 3271433_3
- `C15`: Decrease transmission power for 3271433_3
- `C16`: Increase A3 Offset threshold for 3271433_3
- `C17`: Adjust the azimuth of 3271433_3 by 44 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Increase A3 Offset threshold for 3247443_5
- `C20`: Lift the tilt angle of 3247443_5 by 4 degrees
- `C21`: Press down the tilt angle of 3247443_5 by 4 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247443_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.311 | MS1 | 121.4656635248 | 31.1446180250 | 470 | 504990 | -94.24 | 10.76 | 466.46 | 0.15 | 2.01 | 1598 |
| 2024-09-20 22:21:32.362 | MS1 | 121.4656707458 | 31.1446246594 | 803 | 504990 | -94.88 | 9.52 | 561.09 | 0.09 | 2.97 | 1586 |
| 2024-09-20 22:21:33.688 | MS1 | 121.4656635648 | 31.1446356289 | 56 | 504990 | -94.90 | 12.08 | 319.12 | 0.19 | 2.99 | 1564 |
| 2024-09-20 22:21:34.618 | MS1 | 121.4656721271 | 31.1446200748 | 339 | 152650 | -92.79 | 4.48 | 66.95 | 0.13 | 1.97 | 907 |
| 2024-09-20 22:21:35.696 | MS1 | 121.4656670079 | 31.1446342434 | 648 | 152650 | -94.89 | 5.90 | 74.16 | 0.04 | 1.67 | 958 |
| 2024-09-20 22:21:36.180 | MS1 | 121.4656665956 | 31.1446186994 | 433 | 152650 | -90.30 | 3.11 | 85.91 | 0.01 | 1.66 | 976 |
| 2024-09-20 22:21:37.752 | MS1 | 121.4656617452 | 31.1446218996 | 325 | 152650 | -93.89 | 4.46 | 53.73 | 0.17 | 1.91 | 913 |
| 2024-09-20 22:21:38.445 | MS1 | 121.4656770545 | 31.1446198029 | 339 | 152650 | -88.06 | 5.39 | 103.63 | 0.03 | 1.67 | 924 |
| 2024-09-20 22:21:39.299 | MS1 | 121.4656774747 | 31.1446276237 | 648 | 152650 | -96.44 | 5.88 | 65.13 | 0.04 | 1.85 | 997 |
| 2024-09-20 22:21:40.994 | MS1 | 121.4656596587 | 31.1446293134 | 433 | 152650 | -95.00 | 5.24 | 95.76 | 0.10 | 2.56 | 1573 |
| 2024-09-20 22:21:41.996 | MS1 | 121.4656734447 | 31.1446242870 | 325 | 152650 | -95.33 | 7.56 | 49.64 | 0.13 | 2.09 | 1586 |
| 2024-09-20 22:21:42.124 | MS1 | 121.4656641292 | 31.1446371413 | 339 | 152650 | -92.51 | 6.36 | 68.24 | 0.08 | 2.33 | 1598 |

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
| 3218046 | 7 | 121.4657796788 | 31.1457885359 | 144 | 5 | 5 | 7.2 | FDD | 738 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3220256 | 4 | 121.4665747597 | 31.1453840334 | 6 | 7 | 2 | 3.7 | TDD | 178 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3223655 | 2 | 121.4693838620 | 31.1475208982 | 76 | 4 | 11 | 7.5 | TDD | 41 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3226552 | 9 | 121.4645178510 | 31.1462449783 | 187 | 11 | 2 | 0.1 | FDD | 325 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3229616 | 13 | 121.4668770520 | 31.1543569360 | 296 | 2 | 0 | 6.1 | FDD | 339 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3244279 | 8 | 121.4729423688 | 31.1512552901 | 356 | 11 | 1 | 16.5 | FDD | 484 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3245213 | 10 | 121.4696516949 | 31.1457121925 | 325 | 4 | 5 | 9.9 | FDD | 648 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3247443 | 5 | 121.4734627904 | 31.1558227931 | 162 | 3 | 4 | 17.6 | TDD | 470 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3248282 | 6 | 121.4726571893 | 31.1450505488 | 100 | 4 | 0 | 23.7 | TDD | 56 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3257024 | 12 | 121.4719509828 | 31.1483575313 | 246 | 9 | 3 | 19.9 | FDD | 433 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3270595 | 11 | 121.4660815923 | 31.1540262908 | 184 | 3 | 7 | 9.0 | FDD | 553 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3271433 | 3 | 121.4659358936 | 31.1546721283 | 225 | 4 | 8 | 21.9 | TDD | 849 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3276149 | 1 | 121.4648490264 | 31.1549949085 | 161 | 11 | 9 | 19.7 | TDD | 803 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.739 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.761 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.896 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.896 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.638 | NREventA2 | measId:1;ServCellPCI:190;Se... |
| 2024-09-20 22:21:34.764 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:34.978 | NREventA5 | measId:3;ServCellPCI:190;Se... |
| 2024-09-20 22:21:35.018 | NRHandoverAttempt | SourcePCI:190;SourceNR-ARFC... |
| 2024-09-20 22:21:35.056 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.070 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.203 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.203 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276149 | 1 | 12.9110 | 11.0984 | -115.1157 | 10.4097 | 151.2502 | 0.0157 | 0.0026 |
| 2024_09_20 22:00 | 3223655 | 2 | 14.6332 | 18.7542 | -116.4405 | 12.7137 | 152.1101 | 0.0124 | 0.0021 |
| 2024_09_20 22:00 | 3271433 | 3 | 19.7800 | 18.4271 | -116.4367 | 17.8487 | 123.6686 | 0.0116 | 0.0058 |
| 2024_09_20 22:00 | 3220256 | 4 | 16.0018 | 12.0732 | -115.7501 | 9.5331 | 163.7479 | 0.0124 | 0.0154 |
| 2024_09_20 22:00 | 3247443 | 5 | 8.3787 | 19.8291 | -114.9956 | 9.8645 | 96.0301 | 0.0125 | 0.0050 |
| 2024_09_20 22:00 | 3248282 | 6 | 17.7312 | 5.3234 | -116.7455 | 6.2493 | 196.6032 | 0.0141 | 0.0146 |
| 2024_09_20 22:00 | 3218046 | 7 | 19.1791 | 12.0747 | -114.2054 | 4.9650 | 50.6346 | 0.0141 | 0.0043 |
| 2024_09_20 22:00 | 3244279 | 8 | 7.6922 | 12.0194 | -117.7009 | 4.8667 | 46.3310 | 0.0051 | 0.0011 |
| 2024_09_20 22:00 | 3226552 | 9 | 15.3828 | 5.6546 | -116.2068 | 3.5646 | 21.9611 | 0.0026 | 0.0095 |
| 2024_09_20 22:00 | 3245213 | 10 | 18.1899 | 11.7889 | -116.8258 | 4.7555 | 33.0405 | 0.0178 | 0.0184 |
| 2024_09_20 22:00 | 3270595 | 11 | 5.5488 | 14.8118 | -116.0408 | 3.0102 | 58.1787 | 0.0082 | 0.0081 |
| 2024_09_20 22:00 | 3257024 | 12 | 5.4942 | 6.1484 | -114.8818 | 4.7558 | 39.0355 | 0.0056 | 0.0116 |
| 2024_09_20 22:00 | 3229616 | 13 | 13.3792 | 11.3347 | -116.9242 | 4.5812 | 40.2398 | 0.0072 | 0.0086 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415565_B73B0623 | 152650 | 339 | -93.7 | 152650 | 738 | -94.1 | 152650 | 553 | -100.7 | 152650 | 484 |
| MR_1774415565_784779D3 | 152650 | 339 | -91.2 | 152650 | 738 | -97.4 | 152650 | 553 | -104.0 | 152650 | 484 |
| MR_1774415565_315AD376 | 504990 | 56 | -95.9 | 504990 | 849 | -94.0 | 504990 | 41 | -95.9 | 504990 | 178 |
| MR_1774415565_13FDC171 | 152650 | 339 | -90.9 | 152650 | 738 | -95.0 | 152650 | 553 | -101.3 | 152650 | 484 |
| MR_1774415565_96EF90D6 | 152650 | 339 | -93.1 | 152650 | 738 | -97.1 | 152650 | 553 | -101.2 | 152650 | 484 |

> *... 2개 열 생략 (전체 14열)*

---
