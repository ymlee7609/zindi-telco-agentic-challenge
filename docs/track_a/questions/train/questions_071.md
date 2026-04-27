# Track A 문제 분석 — train[700]~train[709]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[700] ~ train[709] (10개)

## 목차

1. [문제 700: `72e146c2-25c...`](#700) — single-answer, 정답: C12
2. [문제 701: `85861c53-db1...`](#701) — single-answer, 정답: C2
3. [문제 702: `49564faa-670...`](#702) — multiple-answer, 정답: C5|C11
4. [문제 703: `5c91c350-3ec...`](#703) — multiple-answer, 정답: C9|C11
5. [문제 704: `a02a6b3d-1e3...`](#704) — single-answer, 정답: C7
6. [문제 705: `f4dfd2ef-f5e...`](#705) — single-answer, 정답: C3
7. [문제 706: `5f6743f9-746...`](#706) — multiple-answer, 정답: C1|C5|C12|C20
8. [문제 707: `6420463a-b6e...`](#707) — single-answer, 정답: C14
9. [문제 708: `99383324-93d...`](#708) — single-answer, 정답: C8
10. [문제 709: `48b701e5-c6b...`](#709) — single-answer, 정답: C11

---

### 문제 700: `72e146c2-25c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `72e146c2-25c7-4a89-8f01-1b7d7ea65d75` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Lift the tilt angle  of 3214675_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[700] topology](images/train_0700.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3214675_1 and 3267342_4
- `C2`: Increase transmission power for 3267342_4
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Press down the tilt angle of 3230734_2 by 2 degrees
- `C5`: Increase A3 Offset threshold for 3230734_2
- `C6`: Increase A3 Offset threshold for 3267342_4
- `C7`: Decrease transmission power for 3230734_2
- `C8`: Adjust the azimuth of 3230734_2 by 26 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230734_2
- `C10`: Check test server and transmission issues
- `C11`: Lift the tilt angle of 3230734_2 by 2 degrees
- `C12`: Lift the tilt angle  of 3214675_1 by 10 degrees **← 정답**
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230734_2
- `C14`: Press down the tilt angle  of 3214675_1 by 10 degrees
- `C15`: Adjust the azimuth of 3214675_1 by 50 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267342_4
- `C17`: Decrease transmission power for 3267342_4
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267342_4
- `C19`: Add neighbor relationship between 3230734_2 and 3267342_4
- `C20`: Decrease A3 Offset threshold for 3267342_4
- `C21`: Increase transmission power for 3230734_2
- `C22`: Decrease A3 Offset threshold for 3230734_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.712 | MS1 | 121.4656627716 | 31.1446219619 | 274 | 504990 | -86.13 | 17.97 | 585.94 | 0.06 | 2.67 | 1578 |
| 2024-09-20 22:21:32.537 | MS1 | 121.4656717380 | 31.1446326669 | 274 | 504990 | -88.05 | 17.96 | 412.56 | 0.04 | 2.90 | 1582 |
| 2024-09-20 22:21:33.780 | MS1 | 121.4656659089 | 31.1446253514 | 274 | 504990 | -88.93 | 14.32 | 479.42 | 0.12 | 2.48 | 1573 |
| 2024-09-20 22:21:34.583 | MS1 | 121.4656594072 | 31.1446261704 | 274 | 504990 | -85.39 | 16.99 | 76.89 | 0.10 | 2.93 | 1585 |
| 2024-09-20 22:21:35.707 | MS1 | 121.4656580746 | 31.1446198603 | 274 | 504990 | -87.46 | 16.30 | 72.25 | 0.13 | 2.28 | 1584 |
| 2024-09-20 22:21:36.194 | MS1 | 121.4656753129 | 31.1446320165 | 274 | 504990 | -88.30 | 15.65 | 65.28 | 0.05 | 2.82 | 1560 |
| 2024-09-20 22:21:37.588 | MS1 | 121.4656691210 | 31.1446237458 | 274 | 504990 | -89.47 | 12.01 | 67.90 | 0.09 | 2.63 | 1583 |
| 2024-09-20 22:21:38.807 | MS1 | 121.4656616791 | 31.1446228723 | 274 | 504990 | -90.64 | 8.31 | 60.18 | 0.03 | 2.41 | 1586 |
| 2024-09-20 22:21:39.816 | MS1 | 121.4656687619 | 31.1446282538 | 274 | 504990 | -92.50 | 9.81 | 92.25 | 0.02 | 2.85 | 1561 |
| 2024-09-20 22:21:40.651 | MS1 | 121.4656633001 | 31.1446247449 | 274 | 504990 | -91.42 | 7.84 | 584.37 | 0.05 | 2.39 | 1583 |
| 2024-09-20 22:21:41.865 | MS1 | 121.4656594514 | 31.1446251515 | 274 | 504990 | -89.47 | 8.81 | 545.81 | 0.06 | 2.42 | 1595 |
| 2024-09-20 22:21:42.717 | MS1 | 121.4656759937 | 31.1446251563 | 274 | 504990 | -90.33 | 10.91 | 513.95 | 0.11 | 2.65 | 1575 |

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
| 3213058 | 3 | 121.4759693298 | 31.1475331300 | 2 | 1 | 1 | 37.0 | TDD | 148 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3214675 | 1 | 121.4758346831 | 31.1486157713 | 351 | 14 | 0 | 28.5 | TDD | 969 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3230734 | 2 | 121.4686698093 | 31.1525244947 | 224 | 1 | 12 | 21.8 | TDD | 274 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3267342 | 4 | 121.4697719794 | 31.1511561675 | 352 | 14 | 10 | 25.1 | TDD | 725 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.841 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.857 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.006 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.006 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.680 | NREventA3 | measId:2;ServCellPCI:268;Se... |
| 2024-09-20 22:21:37.920 | NRHandoverAttempt | SourcePCI:268;SourceNR-ARFC... |
| 2024-09-20 22:21:37.958 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.968 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.083 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.083 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214675 | 1 | 12.2779 | 11.7809 | -116.1235 | 7.9263 | 116.6172 | 0.0167 | 0.0177 |
| 2024_09_20 22:00 | 3230734 | 2 | 88.8845 | 87.9040 | -116.5887 | 15.1336 | 115.0329 | 0.0190 | 0.0057 |
| 2024_09_20 22:00 | 3213058 | 3 | 7.9418 | 7.0754 | -115.3399 | 11.8340 | 90.7600 | 0.0018 | 0.0001 |
| 2024_09_20 22:00 | 3267342 | 4 | 16.3740 | 5.7953 | -115.6992 | 19.7651 | 84.6209 | 0.0011 | 0.0089 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412201_13D8722A | 504990 | 274 | -86.4 | 504990 | 725 | -89.3 | 504990 | 969 | -93.2 | 504990 | 148 |
| MR_1774412201_B8989368 | 504990 | 274 | -85.8 | 504990 | 725 | -86.0 | 504990 | 969 | -92.3 | 504990 | 148 |
| MR_1774412201_ECA02974 | 504990 | 274 | -86.0 | 504990 | 725 | -86.5 | 504990 | 969 | -95.2 | 504990 | 148 |
| MR_1774412201_982AC2BA | 504990 | 274 | -83.7 | 504990 | 725 | -87.0 | 504990 | 969 | -95.2 | 504990 | 148 |
| MR_1774412201_C2C97B38 | 504990 | 274 | -86.0 | 504990 | 725 | -87.8 | 504990 | 969 | -91.9 | 504990 | 148 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 701: `85861c53-db1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `85861c53-db18-4ccb-b8f0-32bf171fa765` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[701] topology](images/train_0701.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3278811_2 and 3268899_1
- `C2`: Check test server and transmission issues **← 정답**
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261006_3
- `C4`: Adjust the azimuth of 3261006_3 by 1 degrees
- `C5`: Increase A3 Offset threshold for 3261006_3
- `C6`: Lift the tilt angle  of 3268899_1 by 3 degrees
- `C7`: Add neighbor relationship between 3261006_3 and 3268899_1
- `C8`: Increase transmission power for 3268899_1
- `C9`: Increase A3 Offset threshold for 3268899_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261006_3
- `C11`: Increase transmission power for 3261006_3
- `C12`: Decrease transmission power for 3261006_3
- `C13`: Adjust the azimuth of 3268899_1 by 50 degrees
- `C14`: Decrease A3 Offset threshold for 3268899_1
- `C15`: Decrease transmission power for 3268899_1
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Lift the tilt angle of 3261006_3 by 10 degrees
- `C18`: Press down the tilt angle of 3261006_3 by 10 degrees
- `C19`: Decrease A3 Offset threshold for 3261006_3
- `C20`: Press down the tilt angle  of 3268899_1 by 3 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268899_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268899_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.145 | MS1 | 121.4656713481 | 31.1446352660 | 580 | 504990 | -91.75 | 12.50 | 569.69 | 0.03 | 2.21 | 1569 |
| 2024-09-20 22:21:32.760 | MS1 | 121.4656629810 | 31.1446203154 | 580 | 504990 | -86.50 | 15.56 | 426.63 | 0.08 | 2.29 | 1592 |
| 2024-09-20 22:21:33.998 | MS1 | 121.4656641644 | 31.1446338576 | 580 | 504990 | -89.13 | 12.27 | 409.66 | 0.13 | 2.74 | 1570 |
| 2024-09-20 22:21:34.709 | MS1 | 121.4656634565 | 31.1446243393 | 580 | 504990 | -90.00 | 12.46 | 90.90 | 0.18 | 2.33 | 479 |
| 2024-09-20 22:21:35.898 | MS1 | 121.4656646329 | 31.1446211719 | 580 | 504990 | -87.88 | 12.14 | 67.11 | 0.02 | 2.27 | 452 |
| 2024-09-20 22:21:36.585 | MS1 | 121.4656621282 | 31.1446300168 | 580 | 504990 | -85.01 | 15.05 | 69.35 | 0.03 | 2.23 | 482 |
| 2024-09-20 22:21:37.789 | MS1 | 121.4656607059 | 31.1446332409 | 580 | 504990 | -89.17 | 8.21 | 60.24 | 0.05 | 2.29 | 338 |
| 2024-09-20 22:21:38.204 | MS1 | 121.4656627089 | 31.1446215851 | 580 | 504990 | -90.27 | 12.94 | 76.98 | 0.07 | 2.07 | 474 |
| 2024-09-20 22:21:39.435 | MS1 | 121.4656654853 | 31.1446223387 | 580 | 504990 | -91.10 | 10.58 | 60.13 | 0.07 | 2.65 | 415 |
| 2024-09-20 22:21:40.841 | MS1 | 121.4656622067 | 31.1446250988 | 580 | 504990 | -89.48 | 9.90 | 477.30 | 0.02 | 2.13 | 1595 |
| 2024-09-20 22:21:41.657 | MS1 | 121.4656708007 | 31.1446194979 | 580 | 504990 | -89.53 | 10.23 | 314.34 | 0.07 | 2.03 | 1581 |
| 2024-09-20 22:21:42.702 | MS1 | 121.4656594082 | 31.1446339026 | 580 | 504990 | -89.11 | 7.06 | 368.08 | 0.00 | 2.61 | 1584 |

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
| 3235421 | 4 | 121.4727431717 | 31.1554876153 | 161 | 13 | 2 | 41.8 | TDD | 557 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3261006 | 3 | 121.4749788158 | 31.1555233721 | 215 | 12 | 10 | 32.4 | TDD | 580 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3268899 | 1 | 121.4755623221 | 31.1513954994 | 321 | 1 | 1 | 46.2 | TDD | 680 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3278811 | 2 | 121.4678901000 | 31.1518434053 | 315 | 1 | 11 | 21.4 | TDD | 517 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.084 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.099 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.229 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.229 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.972 | NREventA3 | measId:2;ServCellPCI:825;Se... |
| 2024-09-20 22:21:38.212 | NRHandoverAttempt | SourcePCI:825;SourceNR-ARFC... |
| 2024-09-20 22:21:38.260 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.273 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.396 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.396 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268899 | 1 | 16.8221 | 12.5109 | -117.8371 | 12.5088 | 141.7102 | 0.0191 | 0.0094 |
| 2024_09_20 22:00 | 3278811 | 2 | 12.7409 | 10.6552 | -114.9921 | 6.5957 | 154.3200 | 0.0032 | 0.0046 |
| 2024_09_20 22:00 | 3261006 | 3 | 5.1437 | 7.3096 | -116.9487 | 15.9354 | 169.5821 | 0.0156 | 0.0168 |
| 2024_09_20 22:00 | 3235421 | 4 | 18.1299 | 11.0343 | -114.0912 | 12.2167 | 171.6704 | 0.0169 | 0.0169 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417148_24252B32 | 504990 | 580 | -89.7 | 504990 | 680 | -95.5 | 504990 | 517 | -105.7 | 504990 | 557 |
| MR_1774417148_C053078A | 504990 | 580 | -88.6 | 504990 | 680 | -98.8 | 504990 | 517 | -103.9 | 504990 | 557 |
| MR_1774417148_058B503D | 504990 | 580 | -88.1 | 504990 | 680 | -95.6 | 504990 | 517 | -103.2 | 504990 | 557 |
| MR_1774417148_1B65BC21 | 504990 | 580 | -88.5 | 504990 | 680 | -96.2 | 504990 | 517 | -103.2 | 504990 | 557 |
| MR_1774417148_A993993F | 504990 | 580 | -89.4 | 504990 | 680 | -96.1 | 504990 | 517 | -106.0 | 504990 | 557 |
| MR_1774417148_157ECD7F | 504990 | 580 | -90.0 | 504990 | 680 | -97.3 | 504990 | 517 | -104.8 | 504990 | 557 |
| MR_1774417148_8FF3A45C | 504990 | 580 | -89.3 | 504990 | 680 | -95.7 | 504990 | 517 | -103.0 | 504990 | 557 |
| MR_1774417148_9A2415C0 | 504990 | 580 | -89.6 | 504990 | 680 | -97.2 | 504990 | 517 | -106.8 | 504990 | 557 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 702: `49564faa-670...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `49564faa-670e-4ab5-817c-9fa867a5cb03` |
| Tag | **multiple-answer** |
| 정답 | **C5|C11** |
| C5 의미 | Increase transmission power for 3268880_2 |
| C11 의미 | Adjust the azimuth of 3268880_2 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[702] topology](images/train_0702.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3259925_3 and 3275717_1
- `C2`: Decrease transmission power for 3268880_2
- `C3`: Lift the tilt angle  of 3275717_1 by 3 degrees
- `C4`: Increase A3 Offset threshold for 3268880_2
- `C5`: Increase transmission power for 3268880_2 **← 정답**
- `C6`: Decrease A3 Offset threshold for 3275717_1
- `C7`: Decrease transmission power for 3275717_1
- `C8`: Increase transmission power for 3275717_1
- `C9`: Add neighbor relationship between 3268880_2 and 3275717_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268880_2
- `C11`: Adjust the azimuth of 3268880_2 by 50 degrees **← 정답**
- `C12`: Press down the tilt angle  of 3275717_1 by 3 degrees
- `C13`: Press down the tilt angle of 3268880_2 by 6 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268880_2
- `C15`: Decrease A3 Offset threshold for 3268880_2
- `C16`: Lift the tilt angle of 3268880_2 by 6 degrees
- `C17`: Check test server and transmission issues
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275717_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275717_1
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase A3 Offset threshold for 3275717_1
- `C22`: Adjust the azimuth of 3275717_1 by 28 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.729 | MS1 | 121.4656779506 | 31.1446237789 | 338 | 504990 | -93.77 | 16.33 | 335.62 | 0.06 | 2.20 | 1575 |
| 2024-09-20 22:21:32.341 | MS1 | 121.4656768706 | 31.1446302727 | 338 | 504990 | -91.24 | 16.42 | 324.71 | 0.15 | 2.44 | 1566 |
| 2024-09-20 22:21:33.655 | MS1 | 121.4656635974 | 31.1446269350 | 338 | 504990 | -90.45 | 13.66 | 525.27 | 0.09 | 2.97 | 1589 |
| 2024-09-20 22:21:34.843 | MS1 | 121.4656779337 | 31.1446224596 | 338 | 504990 | -105.90 | 1.36 | 47.06 | 0.20 | 1.23 | 1562 |
| 2024-09-20 22:21:35.870 | MS1 | 121.4656679961 | 31.1446338715 | 338 | 504990 | -101.21 | 0.33 | 74.14 | 0.15 | 1.38 | 1572 |
| 2024-09-20 22:21:36.508 | MS1 | 121.4656638475 | 31.1446281168 | 338 | 504990 | -107.88 | -2.00 | 45.70 | 0.12 | 1.24 | 1560 |
| 2024-09-20 22:21:37.571 | MS1 | 121.4656731588 | 31.1446256484 | 338 | 504990 | -102.68 | 0.84 | 34.36 | 0.08 | 1.07 | 1565 |
| 2024-09-20 22:21:38.284 | MS1 | 121.4656750548 | 31.1446265410 | 338 | 504990 | -100.82 | -0.56 | 26.81 | 0.08 | 1.34 | 1560 |
| 2024-09-20 22:21:39.457 | MS1 | 121.4656742791 | 31.1446247769 | 338 | 504990 | -105.10 | 1.91 | 23.30 | 0.02 | 1.05 | 1589 |
| 2024-09-20 22:21:40.282 | MS1 | 121.4656714801 | 31.1446245695 | 338 | 504990 | -87.83 | 17.69 | 424.73 | 0.01 | 2.77 | 1597 |
| 2024-09-20 22:21:41.468 | MS1 | 121.4656619848 | 31.1446280453 | 338 | 504990 | -94.18 | 17.82 | 351.12 | 0.07 | 2.72 | 1571 |
| 2024-09-20 22:21:42.724 | MS1 | 121.4656704307 | 31.1446281166 | 338 | 504990 | -90.82 | 13.78 | 318.50 | 0.02 | 2.53 | 1563 |

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
| 3222468 | 4 | 121.4709936160 | 31.1492405605 | 203 | 8 | 6 | 46.8 | TDD | 407 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3259925 | 3 | 121.4758334010 | 31.1504092762 | 245 | 9 | 4 | 35.8 | TDD | 803 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3268880 | 2 | 121.4697518680 | 31.1544538833 | 141 | 4 | 4 | 46.5 | TDD | 338 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3275717 | 1 | 121.4735859984 | 31.1467323806 | 281 | 1 | 3 | 29.5 | TDD | 231 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.123 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.139 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.260 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.260 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.425 | NREventA2 | measId:1;ServCellPCI:827;Se... |
| 2024-09-20 22:21:34.547 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275717 | 1 | 9.5039 | 10.5513 | -114.3176 | 5.3534 | 171.3075 | 0.0059 | 0.0069 |
| 2024_09_20 22:00 | 3268880 | 2 | 12.8840 | 19.2451 | -115.4101 | 6.7667 | 120.3182 | 0.1590 | 0.0086 |
| 2024_09_20 22:00 | 3259925 | 3 | 8.9970 | 13.6374 | -116.8814 | 12.0469 | 130.9637 | 0.0186 | 0.0076 |
| 2024_09_20 22:00 | 3222468 | 4 | 18.9525 | 11.3050 | -116.5085 | 16.7234 | 126.2823 | 0.0075 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414064_CBA1BB46 | 504990 | 338 | -105.3 | 504990 | 231 | -110.9 | 504990 | 803 | -117.4 | 504990 | 407 |
| MR_1774414064_467F6E3D | 504990 | 338 | -106.0 | 504990 | 231 | -113.9 | 504990 | 803 | -117.3 | 504990 | 407 |
| MR_1774414064_219D2191 | 504990 | 338 | -105.4 | 504990 | 231 | -113.9 | 504990 | 803 | -119.4 | 504990 | 407 |
| MR_1774414064_F1E712A0 | 504990 | 338 | -104.7 | 504990 | 231 | -113.8 | 504990 | 803 | -118.8 | 504990 | 407 |
| MR_1774414064_9B05CC12 | 504990 | 338 | -107.1 | 504990 | 231 | -114.0 | 504990 | 803 | -118.1 | 504990 | 407 |
| MR_1774414064_AC002F0B | 504990 | 338 | -104.7 | 504990 | 231 | -112.8 | 504990 | 803 | -119.3 | 504990 | 407 |
| MR_1774414064_11C392EC | 504990 | 338 | -105.3 | 504990 | 231 | -112.3 | 504990 | 803 | -117.5 | 504990 | 407 |
| MR_1774414064_E136A5FF | 504990 | 338 | -104.9 | 504990 | 231 | -111.1 | 504990 | 803 | -119.8 | 504990 | 407 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 703: `5c91c350-3ec...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5c91c350-3ec6-4030-a293-6514d9678437` |
| Tag | **multiple-answer** |
| 정답 | **C9|C11** |
| C9 의미 | Press down the tilt angle  of 3240775_1 by 2 degrees |
| C11 의미 | Decrease transmission power for 3240775_1 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[703] topology](images/train_0703.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240775_1
- `C2`: Add neighbor relationship between 3261410_2 and 3240775_1
- `C3`: Increase A3 Offset threshold for 3261410_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261410_2
- `C6`: Add neighbor relationship between 3260338_4 and 3240775_1
- `C7`: Decrease A3 Offset threshold for 3261410_2
- `C8`: Adjust the azimuth of 3240775_1 by 23 degrees
- `C9`: Press down the tilt angle  of 3240775_1 by 2 degrees **← 정답**
- `C10`: Decrease transmission power for 3261410_2
- `C11`: Decrease transmission power for 3240775_1 **← 정답**
- `C12`: Increase transmission power for 3240775_1
- `C13`: Check test server and transmission issues
- `C14`: Lift the tilt angle  of 3240775_1 by 2 degrees
- `C15`: Press down the tilt angle of 3261410_2 by 5 degrees
- `C16`: Lift the tilt angle of 3261410_2 by 5 degrees
- `C17`: Increase transmission power for 3261410_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240775_1
- `C19`: Adjust the azimuth of 3261410_2 by 24 degrees
- `C20`: Increase A3 Offset threshold for 3240775_1
- `C21`: Decrease A3 Offset threshold for 3240775_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261410_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.154 | MS1 | 121.4656737985 | 31.1446202959 | 799 | 504990 | -79.21 | 15.74 | 549.42 | 0.08 | 2.81 | 1579 |
| 2024-09-20 22:21:32.206 | MS1 | 121.4656697927 | 31.1446342857 | 799 | 504990 | -77.65 | 15.74 | 427.56 | 0.06 | 2.93 | 1564 |
| 2024-09-20 22:21:33.188 | MS1 | 121.4656765918 | 31.1446186002 | 799 | 504990 | -82.74 | 16.68 | 583.62 | 0.10 | 2.98 | 1569 |
| 2024-09-20 22:21:34.666 | MS1 | 121.4656691763 | 31.1446370139 | 799 | 504990 | -92.90 | 1.85 | 70.75 | 0.17 | 1.46 | 1572 |
| 2024-09-20 22:21:35.517 | MS1 | 121.4656752586 | 31.1446211799 | 799 | 504990 | -93.84 | 1.86 | 77.38 | 0.17 | 1.42 | 1598 |
| 2024-09-20 22:21:36.731 | MS1 | 121.4656615217 | 31.1446378341 | 799 | 504990 | -88.65 | 0.63 | 64.14 | 0.06 | 1.46 | 1567 |
| 2024-09-20 22:21:37.159 | MS1 | 121.4656749495 | 31.1446367759 | 799 | 504990 | -91.15 | 3.98 | 80.81 | 0.14 | 1.46 | 1563 |
| 2024-09-20 22:21:38.269 | MS1 | 121.4656630844 | 31.1446204200 | 799 | 504990 | -87.39 | 2.40 | 85.89 | 0.01 | 1.25 | 1595 |
| 2024-09-20 22:21:39.149 | MS1 | 121.4656643772 | 31.1446237982 | 799 | 504990 | -94.74 | 2.95 | 65.17 | 0.05 | 1.17 | 1593 |
| 2024-09-20 22:21:40.555 | MS1 | 121.4656741996 | 31.1446294720 | 799 | 504990 | -82.36 | 15.09 | 378.97 | 0.01 | 2.01 | 1594 |
| 2024-09-20 22:21:41.905 | MS1 | 121.4656581648 | 31.1446236342 | 799 | 504990 | -82.33 | 16.86 | 364.18 | 0.15 | 2.74 | 1579 |
| 2024-09-20 22:21:42.176 | MS1 | 121.4656776773 | 31.1446279429 | 799 | 504990 | -80.92 | 13.66 | 500.12 | 0.14 | 2.62 | 1598 |

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
| 3225698 | 3 | 121.4714864094 | 31.1446753725 | 218 | 1 | 3 | 19.0 | TDD | 77 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3240775 | 1 | 121.4697866207 | 31.1518373532 | 229 | 0 | 2 | 31.4 | TDD | 178 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3260338 | 4 | 121.4710782275 | 31.1451706141 | 147 | 12 | 12 | 22.7 | TDD | 759 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3261410 | 2 | 121.4678590196 | 31.1516349053 | 219 | 2 | 10 | 44.1 | TDD | 799 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.895 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.913 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.047 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.047 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240775 | 1 | 13.9513 | 15.8486 | -115.5080 | 19.9337 | 135.6378 | 0.0159 | 0.0125 |
| 2024_09_20 22:00 | 3261410 | 2 | 12.8962 | 16.1008 | -108.8877 | 9.6611 | 102.7257 | 0.0157 | 0.0177 |
| 2024_09_20 22:00 | 3225698 | 3 | 10.9843 | 12.0020 | -117.6703 | 15.2057 | 138.9458 | 0.0190 | 0.0065 |
| 2024_09_20 22:00 | 3260338 | 4 | 14.9284 | 8.5236 | -116.9345 | 8.0258 | 115.5603 | 0.0104 | 0.0198 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414911_AD803472 | 504990 | 799 | -91.9 | 504990 | 178 | -88.8 | 504990 | 759 | -90.5 | 504990 | 77 |
| MR_1774414911_8D4596CD | 504990 | 799 | -93.3 | 504990 | 178 | -89.1 | 504990 | 759 | -90.8 | 504990 | 77 |
| MR_1774414911_8CD15E67 | 504990 | 799 | -94.4 | 504990 | 178 | -90.3 | 504990 | 759 | -90.5 | 504990 | 77 |
| MR_1774414911_444BFCCF | 504990 | 178 | -91.0 | 504990 | 799 | -91.2 | 504990 | 759 | -92.4 | 504990 | 77 |
| MR_1774414911_0F50BABA | 504990 | 799 | -91.3 | 504990 | 178 | -91.5 | 504990 | 759 | -92.5 | 504990 | 77 |
| MR_1774414911_23C2E944 | 504990 | 178 | -92.6 | 504990 | 799 | -87.7 | 504990 | 759 | -93.0 | 504990 | 77 |
| MR_1774414911_710D9DA4 | 504990 | 178 | -94.6 | 504990 | 799 | -90.2 | 504990 | 759 | -90.1 | 504990 | 77 |
| MR_1774414911_681D84AA | 504990 | 178 | -94.1 | 504990 | 799 | -89.4 | 504990 | 759 | -90.5 | 504990 | 77 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 704: `a02a6b3d-1e3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a02a6b3d-1e3d-49c3-b00e-e7f1474ffc08` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[704] topology](images/train_0704.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3261834_1 by 9 degrees
- `C2`: Increase A3 Offset threshold for 3261834_1
- `C3`: Add neighbor relationship between 3261834_1 and 3269121_3
- `C4`: Decrease transmission power for 3261834_1
- `C5`: Add neighbor relationship between 3272838_2 and 3269121_3
- `C6`: Increase A3 Offset threshold for 3269121_3
- `C7`: Check test server and transmission issues **← 정답**
- `C8`: Decrease A3 Offset threshold for 3269121_3
- `C9`: Adjust the azimuth of 3261834_1 by 50 degrees
- `C10`: Lift the tilt angle of 3261834_1 by 9 degrees
- `C11`: Increase transmission power for 3269121_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261834_1
- `C13`: Adjust the azimuth of 3269121_3 by 16 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269121_3
- `C15`: Lift the tilt angle  of 3269121_3 by 10 degrees
- `C16`: Decrease A3 Offset threshold for 3261834_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261834_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Increase transmission power for 3261834_1
- `C20`: Decrease transmission power for 3269121_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269121_3
- `C22`: Press down the tilt angle  of 3269121_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.355 | MS1 | 121.4656715443 | 31.1446326358 | 921 | 504990 | -91.12 | 14.31 | 414.72 | 0.08 | 2.25 | 1593 |
| 2024-09-20 22:21:32.936 | MS1 | 121.4656590478 | 31.1446276801 | 921 | 504990 | -90.24 | 15.89 | 537.20 | 0.11 | 2.39 | 1572 |
| 2024-09-20 22:21:33.574 | MS1 | 121.4656581039 | 31.1446376400 | 921 | 504990 | -86.81 | 13.08 | 506.86 | 0.06 | 2.01 | 1580 |
| 2024-09-20 22:21:34.432 | MS1 | 121.4656739766 | 31.1446234222 | 921 | 504990 | -85.58 | 14.77 | 85.67 | 0.08 | 2.81 | 431 |
| 2024-09-20 22:21:35.842 | MS1 | 121.4656690139 | 31.1446339316 | 921 | 504990 | -89.45 | 14.01 | 83.66 | 0.13 | 2.60 | 411 |
| 2024-09-20 22:21:36.258 | MS1 | 121.4656740167 | 31.1446253759 | 921 | 504990 | -86.58 | 12.02 | 86.51 | 0.16 | 2.76 | 449 |
| 2024-09-20 22:21:37.739 | MS1 | 121.4656589216 | 31.1446181975 | 921 | 504990 | -92.21 | 8.60 | 90.04 | 0.09 | 2.62 | 339 |
| 2024-09-20 22:21:38.558 | MS1 | 121.4656605439 | 31.1446226149 | 921 | 504990 | -92.84 | 12.04 | 56.13 | 0.14 | 2.46 | 319 |
| 2024-09-20 22:21:39.771 | MS1 | 121.4656715695 | 31.1446266431 | 921 | 504990 | -90.09 | 7.64 | 63.13 | 0.14 | 2.18 | 438 |
| 2024-09-20 22:21:40.644 | MS1 | 121.4656749279 | 31.1446239239 | 921 | 504990 | -89.55 | 12.93 | 370.52 | 0.17 | 2.61 | 1572 |
| 2024-09-20 22:21:41.465 | MS1 | 121.4656623595 | 31.1446338115 | 921 | 504990 | -92.32 | 10.90 | 438.32 | 0.16 | 2.22 | 1575 |
| 2024-09-20 22:21:42.404 | MS1 | 121.4656763116 | 31.1446193969 | 921 | 504990 | -93.95 | 9.76 | 482.90 | 0.12 | 2.25 | 1564 |

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
| 3232862 | 4 | 121.4688997659 | 31.1521383463 | 179 | 8 | 8 | 17.4 | TDD | 143 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3261834 | 1 | 121.4719828563 | 31.1530646476 | 84 | 8 | 7 | 17.8 | TDD | 921 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3269121 | 3 | 121.4708564531 | 31.1445450169 | 255 | 11 | 10 | 19.8 | TDD | 134 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3272838 | 2 | 121.4706505968 | 31.1540992714 | 178 | 12 | 3 | 24.1 | TDD | 157 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.930 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.945 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.048 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.048 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.783 | NREventA3 | measId:2;ServCellPCI:95;Ser... |
| 2024-09-20 22:21:38.023 | NRHandoverAttempt | SourcePCI:95;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.064 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.075 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.210 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.210 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261834 | 1 | 16.7798 | 17.7466 | -115.3947 | 6.1134 | 135.4412 | 0.0131 | 0.0003 |
| 2024_09_20 22:00 | 3272838 | 2 | 17.9699 | 15.7505 | -115.0584 | 17.0479 | 164.0604 | 0.0132 | 0.0152 |
| 2024_09_20 22:00 | 3269121 | 3 | 9.1546 | 15.3109 | -116.3178 | 6.9385 | 193.6280 | 0.0171 | 0.0011 |
| 2024_09_20 22:00 | 3232862 | 4 | 16.3756 | 6.7516 | -117.6080 | 7.2661 | 199.9944 | 0.0085 | 0.0015 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413391_57C753B0 | 504990 | 921 | -86.3 | 504990 | 134 | -85.5 | 504990 | 157 | -98.0 | 504990 | 143 |
| MR_1774413391_ABF4ECA9 | 504990 | 921 | -87.0 | 504990 | 134 | -87.5 | 504990 | 157 | -96.4 | 504990 | 143 |
| MR_1774413391_8FF551DD | 504990 | 921 | -85.6 | 504990 | 134 | -86.3 | 504990 | 157 | -95.6 | 504990 | 143 |
| MR_1774413391_17193BB2 | 504990 | 921 | -84.7 | 504990 | 134 | -86.8 | 504990 | 157 | -96.8 | 504990 | 143 |
| MR_1774413391_CD692C20 | 504990 | 921 | -87.5 | 504990 | 134 | -88.7 | 504990 | 157 | -96.8 | 504990 | 143 |
| MR_1774413391_11C4DA3F | 504990 | 921 | -84.5 | 504990 | 134 | -86.5 | 504990 | 157 | -97.9 | 504990 | 143 |
| MR_1774413391_1BD11CAD | 504990 | 921 | -84.5 | 504990 | 134 | -88.4 | 504990 | 157 | -99.1 | 504990 | 143 |
| MR_1774413391_04D13834 | 504990 | 921 | -85.2 | 504990 | 134 | -85.1 | 504990 | 157 | -95.8 | 504990 | 143 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 705: `f4dfd2ef-f5e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f4dfd2ef-f5e8-4149-8f6b-ae5c22783cae` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Lift the tilt angle  of 3229459_3 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[705] topology](images/train_0705.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3229234_2
- `C2`: Decrease transmission power for 3242917_1
- `C3`: Lift the tilt angle  of 3229459_3 by 7 degrees **← 정답**
- `C4`: Adjust the azimuth of 3229459_3 by 50 degrees
- `C5`: Add neighbor relationship between 3229234_2 and 3242917_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242917_1
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease transmission power for 3229234_2
- `C9`: Decrease A3 Offset threshold for 3242917_1
- `C10`: Press down the tilt angle  of 3229459_3 by 7 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229234_2
- `C12`: Increase A3 Offset threshold for 3229234_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229234_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242917_1
- `C15`: Add neighbor relationship between 3229459_3 and 3242917_1
- `C16`: Increase transmission power for 3242917_1
- `C17`: Press down the tilt angle of 3229234_2 by 5 degrees
- `C18`: Decrease A3 Offset threshold for 3229234_2
- `C19`: Lift the tilt angle of 3229234_2 by 5 degrees
- `C20`: Check test server and transmission issues
- `C21`: Adjust the azimuth of 3229234_2 by 35 degrees
- `C22`: Increase A3 Offset threshold for 3242917_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.525 | MS1 | 121.4656595063 | 31.1446232733 | 195 | 504990 | -88.77 | 13.95 | 337.88 | 0.12 | 2.56 | 1568 |
| 2024-09-20 22:21:32.983 | MS1 | 121.4656648526 | 31.1446281109 | 195 | 504990 | -89.61 | 13.62 | 466.40 | 0.16 | 2.71 | 1575 |
| 2024-09-20 22:21:33.648 | MS1 | 121.4656757595 | 31.1446209349 | 195 | 504990 | -89.35 | 16.78 | 431.21 | 0.02 | 2.27 | 1567 |
| 2024-09-20 22:21:34.281 | MS1 | 121.4656688569 | 31.1446285277 | 195 | 504990 | -85.10 | 17.34 | 84.68 | 0.16 | 2.96 | 1598 |
| 2024-09-20 22:21:35.274 | MS1 | 121.4656676491 | 31.1446338265 | 195 | 504990 | -86.14 | 15.92 | 94.57 | 0.02 | 2.62 | 1582 |
| 2024-09-20 22:21:36.970 | MS1 | 121.4656755745 | 31.1446330680 | 195 | 504990 | -87.40 | 16.85 | 70.65 | 0.08 | 2.55 | 1585 |
| 2024-09-20 22:21:37.464 | MS1 | 121.4656689952 | 31.1446318926 | 195 | 504990 | -89.12 | 9.66 | 73.41 | 0.07 | 2.01 | 1596 |
| 2024-09-20 22:21:38.208 | MS1 | 121.4656692237 | 31.1446339932 | 195 | 504990 | -92.24 | 9.59 | 54.78 | 0.11 | 2.77 | 1600 |
| 2024-09-20 22:21:39.710 | MS1 | 121.4656756332 | 31.1446279434 | 195 | 504990 | -91.44 | 8.34 | 102.02 | 0.13 | 2.36 | 1594 |
| 2024-09-20 22:21:40.292 | MS1 | 121.4656596795 | 31.1446378716 | 195 | 504990 | -92.54 | 8.57 | 556.14 | 0.08 | 2.88 | 1578 |
| 2024-09-20 22:21:41.687 | MS1 | 121.4656649606 | 31.1446368476 | 195 | 504990 | -89.50 | 8.73 | 483.66 | 0.13 | 2.11 | 1586 |
| 2024-09-20 22:21:42.556 | MS1 | 121.4656659753 | 31.1446275871 | 195 | 504990 | -90.62 | 10.71 | 572.58 | 0.07 | 2.61 | 1588 |

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
| 3214877 | 4 | 121.4682109340 | 31.1505614133 | 130 | 1 | 11 | 41.2 | TDD | 359 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3229234 | 2 | 121.4704139375 | 31.1450904911 | 229 | 2 | 6 | 20.8 | TDD | 195 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3229459 | 3 | 121.4652517641 | 31.1542495730 | 335 | 8 | 2 | 17.7 | TDD | 303 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3242917 | 1 | 121.4758364013 | 31.1511723622 | 61 | 6 | 7 | 25.4 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.558 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.574 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.681 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.681 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.374 | NREventA3 | measId:2;ServCellPCI:602;Se... |
| 2024-09-20 22:21:38.614 | NRHandoverAttempt | SourcePCI:602;SourceNR-ARFC... |
| 2024-09-20 22:21:38.654 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.667 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.781 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.781 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242917 | 1 | 10.0779 | 8.8570 | -115.1672 | 7.5015 | 153.5149 | 0.0172 | 0.0171 |
| 2024_09_20 22:00 | 3229234 | 2 | 79.7036 | 76.5018 | -114.6486 | 5.6083 | 114.9025 | 0.0180 | 0.0083 |
| 2024_09_20 22:00 | 3229459 | 3 | 18.0462 | 5.7766 | -115.1227 | 16.9448 | 189.9351 | 0.0079 | 0.0123 |
| 2024_09_20 22:00 | 3214877 | 4 | 14.2062 | 16.3704 | -114.9956 | 18.2669 | 109.5531 | 0.0096 | 0.0153 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414989_D760AB76 | 504990 | 195 | -85.5 | 504990 | 441 | -88.2 | 504990 | 303 | -97.2 | 504990 | 359 |
| MR_1774414989_FAE43A8F | 504990 | 195 | -86.7 | 504990 | 441 | -87.7 | 504990 | 303 | -97.2 | 504990 | 359 |
| MR_1774414989_70B65A6D | 504990 | 195 | -83.6 | 504990 | 441 | -89.0 | 504990 | 303 | -98.8 | 504990 | 359 |
| MR_1774414989_6ADE04FD | 504990 | 195 | -85.0 | 504990 | 441 | -87.5 | 504990 | 303 | -96.9 | 504990 | 359 |
| MR_1774414989_82298867 | 504990 | 195 | -85.3 | 504990 | 441 | -88.7 | 504990 | 303 | -96.8 | 504990 | 359 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 706: `5f6743f9-746...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5f6743f9-7466-4949-afcc-4abff69b29aa` |
| Tag | **multiple-answer** |
| 정답 | **C1|C5|C12|C20** |
| C1 의미 | Press down the tilt angle  of 3251828_5 by 4 degrees |
| C5 의미 | Increase A3 Offset threshold for 3218172_1 |
| C12 의미 | Increase A3 Offset threshold for 3251828_5 |
| C20 의미 | Decrease transmission power for 3251828_5 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[706] topology](images/train_0706.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3251828_5 by 4 degrees **← 정답**
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase transmission power for 3251828_5
- `C4`: Press down the tilt angle of 3218172_1 by 2 degrees
- `C5`: Increase A3 Offset threshold for 3218172_1 **← 정답**
- `C6`: Adjust the azimuth of 3251828_5 by 19 degrees
- `C7`: Decrease transmission power for 3218172_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251828_5
- `C9`: Add neighbor relationship between 3234781_4 and 3251828_5
- `C10`: Check test server and transmission issues
- `C11`: Lift the tilt angle of 3218172_1 by 2 degrees
- `C12`: Increase A3 Offset threshold for 3251828_5 **← 정답**
- `C13`: Adjust the azimuth of 3218172_1 by 27 degrees
- `C14`: Decrease A3 Offset threshold for 3218172_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251828_5
- `C16`: Decrease A3 Offset threshold for 3251828_5
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218172_1
- `C18`: Increase transmission power for 3218172_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218172_1
- `C20`: Decrease transmission power for 3251828_5 **← 정답**
- `C21`: Lift the tilt angle  of 3251828_5 by 4 degrees
- `C22`: Add neighbor relationship between 3218172_1 and 3251828_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.947 | MS1 | 121.4656620579 | 31.1446324263 | 772 | 504990 | -80.45 | 12.89 | 496.16 | 0.05 | 2.90 | 1585 |
| 2024-09-20 22:21:32.252 | MS1 | 121.4656723726 | 31.1446182314 | 772 | 504990 | -83.26 | 16.30 | 380.47 | 0.01 | 2.14 | 1583 |
| 2024-09-20 22:21:33.864 | MS1 | 121.4656603393 | 31.1446252031 | 772 | 504990 | -76.89 | 17.74 | 413.99 | 0.19 | 2.51 | 1582 |
| 2024-09-20 22:21:34.580 | MS1 | 121.4656724766 | 31.1446334465 | 679 | 504990 | -88.63 | 1.91 | 43.75 | 0.13 | 1.22 | 1574 |
| 2024-09-20 22:21:35.738 | MS1 | 121.4656673334 | 31.1446329111 | 679 | 504990 | -82.95 | 3.00 | 52.05 | 0.04 | 1.45 | 1573 |
| 2024-09-20 22:21:36.101 | MS1 | 121.4656765897 | 31.1446193444 | 772 | 504990 | -84.19 | 2.03 | 52.55 | 0.06 | 1.19 | 1598 |
| 2024-09-20 22:21:37.961 | MS1 | 121.4656776662 | 31.1446298294 | 772 | 504990 | -86.91 | 2.39 | 55.93 | 0.13 | 1.20 | 1600 |
| 2024-09-20 22:21:38.453 | MS1 | 121.4656585297 | 31.1446182300 | 679 | 504990 | -80.79 | 4.65 | 41.85 | 0.08 | 1.22 | 1594 |
| 2024-09-20 22:21:39.127 | MS1 | 121.4656689676 | 31.1446232810 | 679 | 504990 | -84.62 | 1.14 | 39.20 | 0.18 | 1.26 | 1571 |
| 2024-09-20 22:21:40.264 | MS1 | 121.4656583888 | 31.1446375223 | 679 | 504990 | -83.92 | 15.24 | 361.57 | 0.05 | 2.75 | 1587 |
| 2024-09-20 22:21:41.596 | MS1 | 121.4656732787 | 31.1446214556 | 679 | 504990 | -84.30 | 14.72 | 494.80 | 0.10 | 2.80 | 1589 |
| 2024-09-20 22:21:42.595 | MS1 | 121.4656740853 | 31.1446358061 | 679 | 504990 | -77.32 | 15.64 | 486.25 | 0.05 | 2.81 | 1581 |

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
| 3218172 | 1 | 121.4731475742 | 31.1528005866 | 245 | 1 | 9 | 29.0 | TDD | 772 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3234781 | 4 | 121.4742750549 | 31.1483823912 | 251 | 12 | 7 | 35.3 | TDD | 367 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3251828 | 5 | 121.4752885052 | 31.1515744311 | 249 | 2 | 9 | 31.5 | TDD | 178 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3267127 | 3 | 121.4647481857 | 31.1478739693 | 67 | 15 | 2 | 36.3 | TDD | 490 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3270684 | 2 | 121.4649391502 | 31.1513467100 | 136 | 5 | 4 | 32.2 | TDD | 679 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.851 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.869 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.019 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.019 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.688 | NREventA3 | measId:2;ServCellPCI:878;Se... |
| 2024-09-20 22:21:33.928 | NRHandoverAttempt | SourcePCI:878;SourceNR-ARFC... |
| 2024-09-20 22:21:33.973 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:33.984 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:34.094 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.094 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.688 | NREventA3 | measId:2;ServCellPCI:8;Serv... |
| 2024-09-20 22:21:35.928 | NRHandoverAttempt | SourcePCI:8;SourceNR-ARFCN:... |
| 2024-09-20 22:21:35.960 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.974 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.120 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.120 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.688 | NREventA3 | measId:2;ServCellPCI:878;Se... |
| 2024-09-20 22:21:37.928 | NRHandoverAttempt | SourcePCI:878;SourceNR-ARFC... |
| 2024-09-20 22:21:37.971 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.983 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.109 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.109 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218172 | 1 | 18.9012 | 6.6707 | -115.1078 | 11.4370 | 146.3722 | 0.0005 | 0.0056 |
| 2024_09_20 22:00 | 3270684 | 2 | 11.9364 | 18.1503 | -115.2906 | 19.4508 | 114.0254 | 0.0031 | 0.0021 |
| 2024_09_20 22:00 | 3267127 | 3 | 11.1969 | 10.0606 | -117.0470 | 13.4128 | 174.6773 | 0.0140 | 0.0002 |
| 2024_09_20 22:00 | 3234781 | 4 | 18.6909 | 17.6841 | -116.0825 | 8.3336 | 132.6974 | 0.0105 | 0.0153 |
| 2024_09_20 22:00 | 3251828 | 5 | 18.6631 | 17.0284 | -117.9689 | 14.5920 | 115.6127 | 0.0189 | 0.0020 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416484_D8331406 | 504990 | 772 | -88.3 | 504990 | 679 | -90.3 | 504990 | 178 | -95.0 | 504990 | 367 |
| MR_1774416484_621F4A56 | 504990 | 679 | -88.3 | 504990 | 772 | -90.3 | 504990 | 178 | -95.4 | 504990 | 367 |
| MR_1774416484_C3561CF7 | 504990 | 679 | -89.5 | 504990 | 772 | -89.6 | 504990 | 178 | -92.1 | 504990 | 367 |
| MR_1774416484_0D48DF80 | 504990 | 679 | -87.8 | 504990 | 772 | -88.7 | 504990 | 178 | -94.9 | 504990 | 367 |
| MR_1774416484_FDC496E3 | 504990 | 772 | -90.5 | 504990 | 679 | -88.5 | 504990 | 178 | -92.8 | 504990 | 367 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 707: `6420463a-b6e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6420463a-b6ec-4a12-91f2-8ef10462286e` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3268621_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[707] topology](images/train_0707.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3255822_4
- `C2`: Decrease transmission power for 3255822_4
- `C3`: Check test server and transmission issues
- `C4`: Increase A3 Offset threshold for 3268621_2
- `C5`: Adjust the azimuth of 3255822_4 by 50 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255822_4
- `C7`: Increase transmission power for 3255822_4
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Add neighbor relationship between 3211787_1 and 3255822_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268621_2
- `C11`: Lift the tilt angle of 3268621_2 by 6 degrees
- `C12`: Press down the tilt angle  of 3255822_4 by 10 degrees
- `C13`: Lift the tilt angle  of 3255822_4 by 10 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268621_2 **← 정답**
- `C15`: Increase transmission power for 3268621_2
- `C16`: Add neighbor relationship between 3268621_2 and 3255822_4
- `C17`: Press down the tilt angle of 3268621_2 by 6 degrees
- `C18`: Decrease A3 Offset threshold for 3268621_2
- `C19`: Decrease A3 Offset threshold for 3255822_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255822_4
- `C21`: Adjust the azimuth of 3268621_2 by 44 degrees
- `C22`: Decrease transmission power for 3268621_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.418 | MS1 | 121.4656766397 | 31.1446264567 | 436 | 504990 | -90.38 | 13.38 | 379.19 | 0.19 | 2.60 | 1570 |
| 2024-09-20 22:21:32.480 | MS1 | 121.4656678649 | 31.1446231448 | 436 | 504990 | -85.57 | 13.94 | 521.93 | 0.15 | 2.46 | 1580 |
| 2024-09-20 22:21:33.515 | MS1 | 121.4656773073 | 31.1446200808 | 436 | 504990 | -90.32 | 14.30 | 594.28 | 0.15 | 2.89 | 1581 |
| 2024-09-20 22:21:34.858 | MS1 | 121.4656685645 | 31.1446364813 | 436 | 504990 | -89.59 | 13.56 | 49.50 | 0.61 | 2.59 | 582 |
| 2024-09-20 22:21:35.226 | MS1 | 121.4656777224 | 31.1446279481 | 436 | 504990 | -89.08 | 13.16 | 97.59 | 0.69 | 2.16 | 541 |
| 2024-09-20 22:21:36.568 | MS1 | 121.4656742282 | 31.1446365479 | 436 | 504990 | -88.77 | 16.17 | 87.15 | 0.63 | 2.06 | 692 |
| 2024-09-20 22:21:37.322 | MS1 | 121.4656729993 | 31.1446311931 | 436 | 504990 | -90.18 | 10.05 | 77.53 | 0.62 | 2.97 | 530 |
| 2024-09-20 22:21:38.105 | MS1 | 121.4656728201 | 31.1446205678 | 436 | 504990 | -89.13 | 11.11 | 68.35 | 0.67 | 2.41 | 588 |
| 2024-09-20 22:21:39.211 | MS1 | 121.4656747296 | 31.1446181346 | 436 | 504990 | -90.31 | 8.20 | 76.75 | 0.55 | 2.80 | 548 |
| 2024-09-20 22:21:40.870 | MS1 | 121.4656616115 | 31.1446369612 | 436 | 504990 | -89.85 | 7.04 | 373.74 | 0.19 | 2.78 | 1588 |
| 2024-09-20 22:21:41.196 | MS1 | 121.4656658538 | 31.1446245386 | 436 | 504990 | -91.92 | 11.81 | 580.26 | 0.11 | 2.99 | 1564 |
| 2024-09-20 22:21:42.337 | MS1 | 121.4656585904 | 31.1446257971 | 436 | 504990 | -90.45 | 10.27 | 518.39 | 0.10 | 2.52 | 1583 |

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
| 3211787 | 1 | 121.4729597633 | 31.1444517997 | 251 | 2 | 9 | 45.8 | TDD | 793 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3233519 | 3 | 121.4661618940 | 31.1558868920 | 187 | 7 | 4 | 30.2 | TDD | 93 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3255822 | 4 | 121.4757215875 | 31.1528577952 | 97 | 9 | 1 | 39.8 | TDD | 149 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3268621 | 2 | 121.4741328350 | 31.1454250219 | 220 | 4 | 7 | 24.8 | TDD | 436 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.848 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.864 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:30.964 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.964 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.674 | NREventA3 | measId:2;ServCellPCI:135;Se... |
| 2024-09-20 22:21:37.914 | NRHandoverAttempt | SourcePCI:135;SourceNR-ARFC... |
| 2024-09-20 22:21:37.950 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.960 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.096 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.096 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211787 | 1 | 9.2134 | 19.6145 | -115.8511 | 12.2908 | 147.9680 | 0.0153 | 0.0178 |
| 2024_09_20 22:00 | 3268621 | 2 | 10.2807 | 11.2109 | -116.5187 | 11.3148 | 136.2673 | 0.0192 | 0.0029 |
| 2024_09_20 22:00 | 3233519 | 3 | 14.9911 | 16.3099 | -114.2463 | 16.1323 | 104.6448 | 0.0179 | 0.0082 |
| 2024_09_20 22:00 | 3255822 | 4 | 6.1048 | 9.7286 | -117.9293 | 14.6767 | 151.7778 | 0.0050 | 0.0029 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415950_2A61488E | 504990 | 436 | -89.2 | 504990 | 149 | -98.1 | 504990 | 793 | -97.5 | 504990 | 93 |
| MR_1774415950_11E00135 | 504990 | 436 | -91.5 | 504990 | 149 | -95.5 | 504990 | 793 | -98.5 | 504990 | 93 |
| MR_1774415950_880FBFC3 | 504990 | 436 | -90.3 | 504990 | 149 | -95.7 | 504990 | 793 | -100.4 | 504990 | 93 |
| MR_1774415950_EE5828A6 | 504990 | 436 | -90.9 | 504990 | 149 | -97.9 | 504990 | 793 | -97.6 | 504990 | 93 |
| MR_1774415950_857380EC | 504990 | 436 | -88.7 | 504990 | 149 | -97.7 | 504990 | 793 | -97.8 | 504990 | 93 |
| MR_1774415950_9C58181F | 504990 | 436 | -88.7 | 504990 | 149 | -97.7 | 504990 | 793 | -98.2 | 504990 | 93 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 708: `99383324-93d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `99383324-93d4-45ce-aa4c-1f74aa86d86b` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[708] topology](images/train_0708.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3219826_2 by 24 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210164_1
- `C3`: Adjust the azimuth of 3210164_1 by 50 degrees
- `C4`: Decrease transmission power for 3219826_2
- `C5`: Add neighbor relationship between 3210164_1 and 3219826_2
- `C6`: Increase transmission power for 3210164_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219826_2
- `C8`: Insufficient data; more data is needed for judgment. **← 정답**
- `C9`: Increase A3 Offset threshold for 3219826_2
- `C10`: Increase A3 Offset threshold for 3210164_1
- `C11`: Increase transmission power for 3219826_2
- `C12`: Decrease transmission power for 3210164_1
- `C13`: Check test server and transmission issues
- `C14`: Lift the tilt angle  of 3219826_2 by 3 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210164_1
- `C16`: Press down the tilt angle  of 3219826_2 by 3 degrees
- `C17`: Press down the tilt angle of 3210164_1 by 9 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219826_2
- `C19`: Lift the tilt angle of 3210164_1 by 9 degrees
- `C20`: Decrease A3 Offset threshold for 3210164_1
- `C21`: Decrease A3 Offset threshold for 3219826_2
- `C22`: Add neighbor relationship between 3260601_3 and 3219826_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.956 | MS1 | 121.4656652131 | 31.1446238864 | 888 | 504990 | -85.29 | 15.51 | 372.07 | 0.14 | 2.67 | 1585 |
| 2024-09-20 22:21:32.571 | MS1 | 121.4656756813 | 31.1446290126 | 888 | 504990 | -87.41 | 13.15 | 470.18 | 0.06 | 2.74 | 1589 |
| 2024-09-20 22:21:33.819 | MS1 | 121.4656758509 | 31.1446368433 | 888 | 504990 | -88.53 | 15.27 | 558.51 | 0.13 | 2.43 | 1591 |
| 2024-09-20 22:21:34.595 | MS1 | 121.4656663656 | 31.1446243150 | 888 | 504990 | -91.88 | 14.92 | 63.07 | 0.17 | 2.46 | 1598 |
| 2024-09-20 22:21:35.228 | MS1 | 121.4656724941 | 31.1446278484 | 888 | 504990 | -90.50 | 15.06 | 79.71 | 0.12 | 2.04 | 1570 |
| 2024-09-20 22:21:36.441 | MS1 | 121.4656712495 | 31.1446361707 | 888 | 504990 | -89.58 | 12.08 | 84.94 | 0.09 | 2.36 | 1562 |
| 2024-09-20 22:21:37.149 | MS1 | 121.4656633949 | 31.1446291597 | 888 | 504990 | -92.46 | 11.79 | 78.30 | 0.02 | 2.01 | 1565 |
| 2024-09-20 22:21:38.578 | MS1 | 121.4656670347 | 31.1446350568 | 888 | 504990 | -93.28 | 8.69 | 81.91 | 0.00 | 2.47 | 1577 |
| 2024-09-20 22:21:39.599 | MS1 | 121.4656649303 | 31.1446211400 | 888 | 504990 | -90.74 | 11.86 | 84.15 | 0.18 | 2.83 | 1593 |
| 2024-09-20 22:21:40.469 | MS1 | 121.4656723132 | 31.1446192050 | 888 | 504990 | -93.86 | 12.10 | 602.94 | 0.16 | 2.72 | 1583 |
| 2024-09-20 22:21:41.496 | MS1 | 121.4656709155 | 31.1446267714 | 888 | 504990 | -90.81 | 12.17 | 590.37 | 0.02 | 2.22 | 1568 |
| 2024-09-20 22:21:42.867 | MS1 | 121.4656681968 | 31.1446193883 | 888 | 504990 | -93.22 | 11.21 | 371.90 | 0.13 | 2.48 | 1572 |

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
| 3210164 | 1 | 121.4674509525 | 31.1486120750 | 28 | 6 | 9 | 25.3 | TDD | 888 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3219826 | 2 | 121.4758748081 | 31.1530583581 | 250 | 1 | 9 | 48.1 | TDD | 690 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3260601 | 3 | 121.4708044910 | 31.1495317818 | 105 | 9 | 9 | 21.3 | TDD | 450 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3265012 | 4 | 121.4648231711 | 31.1508786790 | 150 | 12 | 7 | 36.5 | TDD | 380 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.821 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.843 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.951 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.951 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.640 | NREventA3 | measId:2;ServCellPCI:611;Se... |
| 2024-09-20 22:21:37.880 | NRHandoverAttempt | SourcePCI:611;SourceNR-ARFC... |
| 2024-09-20 22:21:37.919 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.933 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.064 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.064 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3210164 | 1 | 80.5841 | 84.8586 | -116.4493 | 16.3979 | 180.7083 | 0.0196 | 0.0036 |
| 2024_09_19 22:00 | 3219826 | 2 | 76.4867 | 86.5577 | -116.4126 | 11.3554 | 132.4771 | 0.0028 | 0.0117 |
| 2024_09_19 22:00 | 3260601 | 3 | 83.5247 | 76.2412 | -117.0708 | 14.1191 | 179.7093 | 0.0008 | 0.0041 |
| 2024_09_19 22:00 | 3265012 | 4 | 91.7323 | 78.7770 | -114.1038 | 9.5252 | 192.0462 | 0.0126 | 0.0147 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415496_88A7EE5F | 504990 | 888 | -93.6 | 504990 | 690 | -97.8 | 504990 | 450 | -101.5 | 504990 | 380 |
| MR_1774415496_5E607B62 | 504990 | 888 | -90.9 | 504990 | 690 | -95.5 | 504990 | 450 | -100.8 | 504990 | 380 |
| MR_1774415496_AFC0AD9E | 504990 | 888 | -90.6 | 504990 | 690 | -97.7 | 504990 | 450 | -101.9 | 504990 | 380 |
| MR_1774415496_E5020AF5 | 504990 | 888 | -91.0 | 504990 | 690 | -95.5 | 504990 | 450 | -99.9 | 504990 | 380 |
| MR_1774415496_FC6897F8 | 504990 | 888 | -92.4 | 504990 | 690 | -95.9 | 504990 | 450 | -98.6 | 504990 | 380 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 709: `48b701e5-c6b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `48b701e5-c6b7-40ff-ac2e-8b2da3937e5d` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213843_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[709] topology](images/train_0709.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3228209_4 by 24 degrees
- `C2`: Press down the tilt angle of 3213843_6 by 3 degrees
- `C3`: Lift the tilt angle of 3213843_6 by 3 degrees
- `C4`: Increase transmission power for 3213843_6
- `C5`: Increase transmission power for 3228209_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228209_4
- `C7`: Increase A3 Offset threshold for 3213843_6
- `C8`: Decrease transmission power for 3228209_4
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease A3 Offset threshold for 3228209_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213843_6 **← 정답**
- `C12`: Increase A3 Offset threshold for 3228209_4
- `C13`: Check test server and transmission issues
- `C14`: Decrease transmission power for 3213843_6
- `C15`: Add neighbor relationship between 3213843_6 and 3228209_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228209_4
- `C17`: Decrease A3 Offset threshold for 3213843_6
- `C18`: Add neighbor relationship between 3239404_12 and 3228209_4
- `C19`: Lift the tilt angle  of 3228209_4 by 2 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213843_6
- `C21`: Adjust the azimuth of 3213843_6 by 49 degrees
- `C22`: Press down the tilt angle  of 3228209_4 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.578 | MS1 | 121.4656759088 | 31.1446341426 | 958 | 504990 | -95.56 | 12.53 | 423.77 | 0.13 | 2.86 | 1591 |
| 2024-09-20 22:21:32.477 | MS1 | 121.4656611743 | 31.1446366435 | 490 | 504990 | -94.58 | 10.11 | 343.33 | 0.06 | 2.81 | 1594 |
| 2024-09-20 22:21:33.640 | MS1 | 121.4656635106 | 31.1446220697 | 648 | 504990 | -95.52 | 14.67 | 305.03 | 0.18 | 2.09 | 1594 |
| 2024-09-20 22:21:34.202 | MS1 | 121.4656664480 | 31.1446323598 | 991 | 152650 | -91.61 | 5.75 | 49.02 | 0.07 | 1.68 | 939 |
| 2024-09-20 22:21:35.243 | MS1 | 121.4656595403 | 31.1446374092 | 546 | 152650 | -91.95 | 7.76 | 55.15 | 0.13 | 1.92 | 914 |
| 2024-09-20 22:21:36.384 | MS1 | 121.4656758297 | 31.1446368769 | 731 | 152650 | -90.96 | 5.48 | 90.06 | 0.09 | 1.98 | 905 |
| 2024-09-20 22:21:37.343 | MS1 | 121.4656667205 | 31.1446247475 | 885 | 152650 | -88.17 | 6.04 | 64.98 | 0.10 | 1.54 | 982 |
| 2024-09-20 22:21:38.372 | MS1 | 121.4656603076 | 31.1446365921 | 991 | 152650 | -91.23 | 2.36 | 51.97 | 0.04 | 1.85 | 947 |
| 2024-09-20 22:21:39.174 | MS1 | 121.4656620322 | 31.1446277103 | 546 | 152650 | -89.41 | 6.42 | 51.46 | 0.09 | 1.66 | 991 |
| 2024-09-20 22:21:40.674 | MS1 | 121.4656776289 | 31.1446328013 | 731 | 152650 | -96.64 | 4.93 | 91.50 | 0.02 | 2.48 | 1597 |
| 2024-09-20 22:21:41.992 | MS1 | 121.4656646561 | 31.1446360098 | 885 | 152650 | -93.95 | 4.60 | 64.84 | 0.07 | 2.05 | 1573 |
| 2024-09-20 22:21:42.804 | MS1 | 121.4656737274 | 31.1446324833 | 991 | 152650 | -95.73 | 7.70 | 87.79 | 0.07 | 2.38 | 1599 |

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
| 3213843 | 6 | 121.4683775512 | 31.1509760879 | 249 | 2 | 11 | 18.7 | TDD | 958 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3215851 | 8 | 121.4745906099 | 31.1513375447 | 15 | 8 | 12 | 15.4 | FDD | 546 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3219180 | 7 | 121.4726227920 | 31.1518843335 | 243 | 7 | 4 | 12.8 | FDD | 736 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3228209 | 4 | 121.4740966000 | 31.1446833256 | 246 | 0 | 11 | 27.0 | TDD | 972 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3234983 | 13 | 121.4751905125 | 31.1458540458 | 146 | 8 | 11 | 16.8 | FDD | 991 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3236360 | 5 | 121.4714748472 | 31.1544581772 | 169 | 5 | 6 | 23.4 | TDD | 882 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3239268 | 3 | 121.4728584121 | 31.1468038314 | 130 | 12 | 1 | 6.8 | TDD | 490 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3239404 | 12 | 121.4655188771 | 31.1545363007 | 29 | 13 | 0 | 27.1 | FDD | 731 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3242553 | 1 | 121.4747749881 | 31.1553790312 | 297 | 7 | 5 | 3.4 | TDD | 1 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3247729 | 9 | 121.4654201885 | 31.1557841878 | 79 | 9 | 1 | 12.6 | FDD | 744 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3253297 | 10 | 121.4725045520 | 31.1472676622 | 268 | 14 | 1 | 19.8 | FDD | 543 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3253397 | 11 | 121.4746457759 | 31.1470905934 | 200 | 3 | 9 | 21.3 | FDD | 885 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3262397 | 2 | 121.4739522492 | 31.1508430963 | 335 | 11 | 0 | 28.9 | TDD | 648 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.369 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.393 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.500 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.500 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.251 | NREventA2 | measId:1;ServCellPCI:298;Se... |
| 2024-09-20 22:21:35.396 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.674 | NREventA5 | measId:3;ServCellPCI:298;Se... |
| 2024-09-20 22:21:35.715 | NRHandoverAttempt | SourcePCI:298;SourceNR-ARFC... |
| 2024-09-20 22:21:35.740 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.753 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.874 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.874 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242553 | 1 | 15.3873 | 17.4384 | -116.8036 | 9.7056 | 188.4299 | 0.0198 | 0.0056 |
| 2024_09_20 22:00 | 3262397 | 2 | 6.1488 | 17.8193 | -114.4718 | 17.0237 | 197.3252 | 0.0112 | 0.0027 |
| 2024_09_20 22:00 | 3239268 | 3 | 15.0392 | 10.9563 | -114.9715 | 19.9272 | 140.1623 | 0.0195 | 0.0030 |
| 2024_09_20 22:00 | 3228209 | 4 | 13.5473 | 18.2342 | -115.7177 | 12.4704 | 198.9540 | 0.0054 | 0.0095 |
| 2024_09_20 22:00 | 3236360 | 5 | 7.8157 | 8.6116 | -114.0291 | 6.2796 | 99.9081 | 0.0077 | 0.0184 |
| 2024_09_20 22:00 | 3213843 | 6 | 16.5461 | 18.0622 | -116.9645 | 8.5009 | 100.4027 | 0.0012 | 0.0179 |
| 2024_09_20 22:00 | 3219180 | 7 | 17.4109 | 11.1917 | -116.5219 | 4.4294 | 31.1298 | 0.0055 | 0.0082 |
| 2024_09_20 22:00 | 3215851 | 8 | 10.8925 | 16.0325 | -115.1032 | 4.8116 | 45.8708 | 0.0036 | 0.0193 |
| 2024_09_20 22:00 | 3247729 | 9 | 9.8055 | 7.8188 | -115.5163 | 4.8088 | 28.8691 | 0.0122 | 0.0034 |
| 2024_09_20 22:00 | 3253297 | 10 | 6.7621 | 19.9814 | -115.7183 | 3.1135 | 38.3450 | 0.0017 | 0.0186 |
| 2024_09_20 22:00 | 3253397 | 11 | 19.2947 | 8.7465 | -115.9704 | 4.9759 | 48.9004 | 0.0171 | 0.0193 |
| 2024_09_20 22:00 | 3239404 | 12 | 17.3363 | 18.6574 | -116.2720 | 4.0416 | 20.2969 | 0.0149 | 0.0171 |
| 2024_09_20 22:00 | 3234983 | 13 | 14.4553 | 5.5811 | -114.1809 | 4.5122 | 52.5723 | 0.0006 | 0.0166 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413086_E12C0288 | 152650 | 991 | -90.2 | 152650 | 736 | -96.1 | 152650 | 543 | -100.2 | 152650 | 744 |
| MR_1774413086_2F2384DE | 504990 | 648 | -96.8 | 504990 | 972 | -94.2 | 504990 | 1 | -97.5 | 504990 | 882 |
| MR_1774413086_B8CDFB09 | 152650 | 991 | -90.6 | 152650 | 736 | -94.1 | 152650 | 543 | -99.9 | 152650 | 744 |
| MR_1774413086_E496E406 | 504990 | 648 | -93.9 | 504990 | 972 | -93.4 | 504990 | 1 | -97.5 | 504990 | 882 |
| MR_1774413086_B2BF753F | 504990 | 648 | -97.3 | 504990 | 972 | -95.2 | 504990 | 1 | -97.8 | 504990 | 882 |
| MR_1774413086_D05371DE | 504990 | 648 | -95.5 | 504990 | 972 | -91.6 | 504990 | 1 | -99.7 | 504990 | 882 |

> *... 2개 열 생략 (전체 14열)*

---
