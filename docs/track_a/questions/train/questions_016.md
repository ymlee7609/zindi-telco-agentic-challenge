# Track A 문제 분석 — train[150]~train[159]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[150] ~ train[159] (10개)

## 목차

1. [문제 150: `8d5ec075-4ef...`](#150) — single-answer, 정답: C21
2. [문제 151: `03a68c70-350...`](#151) — single-answer, 정답: C7
3. [문제 152: `27a6589d-726...`](#152) — single-answer, 정답: C10
4. [문제 153: `cb672d8d-e70...`](#153) — single-answer, 정답: C11
5. [문제 154: `ad16cd0f-7d6...`](#154) — multiple-answer, 정답: C13|C14
6. [문제 155: `dab27456-181...`](#155) — single-answer, 정답: C7
7. [문제 156: `645c62af-945...`](#156) — single-answer, 정답: C11
8. [문제 157: `578578e7-a41...`](#157) — single-answer, 정답: C2
9. [문제 158: `9521614b-c1c...`](#158) — single-answer, 정답: C1
10. [문제 159: `697c329f-035...`](#159) — single-answer, 정답: C14

---

### 문제 150: `8d5ec075-4ef...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8d5ec075-4ef3-4d12-983e-91ff1ecba728` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Add neighbor relationship between 3277465_4 and 3215292_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[150] topology](images/train_0150.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3215292_1
- `C2`: Decrease A3 Offset threshold for 3215292_1
- `C3`: Add neighbor relationship between 3217282_2 and 3215292_1
- `C4`: Press down the tilt angle of 3277465_4 by 9 degrees
- `C5`: Press down the tilt angle  of 3215292_1 by 6 degrees
- `C6`: Decrease transmission power for 3215292_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215292_1
- `C8`: Lift the tilt angle  of 3215292_1 by 6 degrees
- `C9`: Increase transmission power for 3215292_1
- `C10`: Decrease A3 Offset threshold for 3277465_4
- `C11`: Lift the tilt angle of 3277465_4 by 9 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277465_4
- `C13`: Increase transmission power for 3277465_4
- `C14`: Check test server and transmission issues
- `C15`: Adjust the azimuth of 3215292_1 by 30 degrees
- `C16`: Increase A3 Offset threshold for 3277465_4
- `C17`: Adjust the azimuth of 3277465_4 by 50 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215292_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277465_4
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Add neighbor relationship between 3277465_4 and 3215292_1 **← 정답**
- `C22`: Decrease transmission power for 3277465_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.636 | MS1 | 121.4656663073 | 31.1446342865 | 350 | 504990 | -75.70 | 17.79 | 421.11 | 0.12 | 2.20 | 1565 |
| 2024-09-20 22:21:32.687 | MS1 | 121.4656773273 | 31.1446348423 | 350 | 504990 | -78.89 | 14.23 | 510.68 | 0.07 | 2.51 | 1567 |
| 2024-09-20 22:21:33.939 | MS1 | 121.4656748294 | 31.1446375545 | 350 | 504990 | -83.42 | 17.31 | 415.28 | 0.15 | 2.38 | 1572 |
| 2024-09-20 22:21:34.802 | MS1 | 121.4656743770 | 31.1446334779 | 350 | 504990 | -93.08 | -1.86 | 33.95 | 0.08 | 1.00 | 1582 |
| 2024-09-20 22:21:35.740 | MS1 | 121.4656639324 | 31.1446189651 | 350 | 504990 | -87.89 | -2.03 | 45.51 | 0.02 | 1.27 | 1577 |
| 2024-09-20 22:21:36.372 | MS1 | 121.4656596467 | 31.1446329133 | 350 | 504990 | -93.74 | -3.84 | 73.28 | 0.05 | 1.03 | 1561 |
| 2024-09-20 22:21:37.630 | MS1 | 121.4656599069 | 31.1446349934 | 350 | 504990 | -85.72 | -3.97 | 60.47 | 0.04 | 1.31 | 1563 |
| 2024-09-20 22:21:38.330 | MS1 | 121.4656701989 | 31.1446226827 | 350 | 504990 | -79.53 | 15.64 | 323.98 | 0.16 | 1.44 | 1589 |
| 2024-09-20 22:21:39.440 | MS1 | 121.4656680504 | 31.1446220679 | 350 | 504990 | -76.87 | 13.68 | 444.65 | 0.16 | 1.12 | 1592 |
| 2024-09-20 22:21:40.608 | MS1 | 121.4656697090 | 31.1446360907 | 350 | 504990 | -78.14 | 17.59 | 532.58 | 0.11 | 2.33 | 1574 |
| 2024-09-20 22:21:41.584 | MS1 | 121.4656694153 | 31.1446327003 | 350 | 504990 | -76.34 | 13.09 | 407.00 | 0.00 | 2.98 | 1583 |
| 2024-09-20 22:21:42.781 | MS1 | 121.4656727566 | 31.1446265408 | 350 | 504990 | -80.48 | 15.48 | 401.74 | 0.19 | 2.31 | 1571 |

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
| 3215292 | 1 | 121.4709228610 | 31.1558712036 | 232 | 4 | 6 | 41.7 | TDD | 217 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3217282 | 2 | 121.4744657447 | 31.1493226933 | 128 | 12 | 8 | 20.7 | TDD | 201 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3266846 | 3 | 121.4753442825 | 31.1532091557 | 94 | 6 | 9 | 35.5 | TDD | 958 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3277465 | 4 | 121.4706576592 | 31.1550455290 | 299 | 8 | 1 | 29.0 | TDD | 350 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.272 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.393 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.393 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.092 | NREventA3 | measId:2;ServCellPCI:939;Se... |
| 2024-09-20 22:21:36.092 | NREventA3 | measId:2;ServCellPCI:939;Se... |
| 2024-09-20 22:21:37.092 | NREventA3 | measId:2;ServCellPCI:939;Se... |
| 2024-09-20 22:21:39.592 | NRRRCReestablishAttempt | PCI:939 |
| 2024-09-20 22:21:39.612 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.626 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.762 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.762 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215292 | 1 | 19.1813 | 16.0340 | -115.7431 | 6.4080 | 166.5952 | 0.0046 | 0.0181 |
| 2024_09_20 22:00 | 3217282 | 2 | 10.4449 | 9.8588 | -114.4049 | 7.9927 | 136.2485 | 0.0103 | 0.0122 |
| 2024_09_20 22:00 | 3266846 | 3 | 15.4198 | 8.8345 | -114.0704 | 6.8491 | 142.3785 | 0.0131 | 0.0181 |
| 2024_09_20 22:00 | 3277465 | 4 | 12.5656 | 14.1091 | -115.5140 | 14.9806 | 98.0810 | 0.0075 | 0.1659 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415966_0AAE5125 | 504990 | 350 | -93.2 | 504990 | 217 | -87.6 | 504990 | 201 | -90.9 | 504990 | 958 |
| MR_1774415966_41F9466A | 504990 | 350 | -92.2 | 504990 | 217 | -90.1 | 504990 | 201 | -93.2 | 504990 | 958 |
| MR_1774415966_176C7187 | 504990 | 217 | -87.5 | 504990 | 350 | -94.3 | 504990 | 201 | -90.6 | 504990 | 958 |
| MR_1774415966_3A5CE6AF | 504990 | 217 | -88.7 | 504990 | 350 | -95.0 | 504990 | 201 | -92.9 | 504990 | 958 |
| MR_1774415966_B42D3835 | 504990 | 217 | -88.0 | 504990 | 350 | -94.6 | 504990 | 201 | -92.6 | 504990 | 958 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 151: `03a68c70-350...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `03a68c70-350d-44ef-89b9-6194f4c8fd2b` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Add neighbor relationship between 3233851_4 and 3240520_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[151] topology](images/train_0151.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3233851_4 by 7 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase A3 Offset threshold for 3240520_3
- `C4`: Increase transmission power for 3240520_3
- `C5`: Add neighbor relationship between 3211645_2 and 3240520_3
- `C6`: Increase transmission power for 3233851_4
- `C7`: Add neighbor relationship between 3233851_4 and 3240520_3 **← 정답**
- `C8`: Decrease transmission power for 3240520_3
- `C9`: Adjust the azimuth of 3233851_4 by 50 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240520_3
- `C11`: Decrease transmission power for 3233851_4
- `C12`: Press down the tilt angle of 3233851_4 by 7 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240520_3
- `C14`: Decrease A3 Offset threshold for 3240520_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233851_4
- `C16`: Increase A3 Offset threshold for 3233851_4
- `C17`: Check test server and transmission issues
- `C18`: Press down the tilt angle  of 3240520_3 by 5 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233851_4
- `C20`: Lift the tilt angle  of 3240520_3 by 5 degrees
- `C21`: Decrease A3 Offset threshold for 3233851_4
- `C22`: Adjust the azimuth of 3240520_3 by 40 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.847 | MS1 | 121.4656608575 | 31.1446229625 | 549 | 504990 | -84.08 | 16.49 | 538.12 | 0.13 | 2.63 | 1576 |
| 2024-09-20 22:21:32.573 | MS1 | 121.4656699916 | 31.1446316646 | 549 | 504990 | -77.99 | 17.81 | 397.14 | 0.13 | 2.90 | 1572 |
| 2024-09-20 22:21:33.844 | MS1 | 121.4656605869 | 31.1446203713 | 549 | 504990 | -82.59 | 15.92 | 409.74 | 0.02 | 2.37 | 1596 |
| 2024-09-20 22:21:34.966 | MS1 | 121.4656590010 | 31.1446301083 | 549 | 504990 | -91.18 | -1.65 | 73.09 | 0.10 | 1.09 | 1567 |
| 2024-09-20 22:21:35.757 | MS1 | 121.4656666658 | 31.1446214915 | 549 | 504990 | -91.28 | -3.31 | 44.50 | 0.03 | 1.21 | 1598 |
| 2024-09-20 22:21:36.250 | MS1 | 121.4656703568 | 31.1446207442 | 549 | 504990 | -92.41 | -1.97 | 38.54 | 0.15 | 1.36 | 1589 |
| 2024-09-20 22:21:37.627 | MS1 | 121.4656763781 | 31.1446258829 | 549 | 504990 | -92.75 | -0.84 | 66.36 | 0.15 | 1.29 | 1588 |
| 2024-09-20 22:21:38.270 | MS1 | 121.4656714279 | 31.1446378369 | 549 | 504990 | -83.34 | 17.12 | 490.88 | 0.03 | 1.01 | 1591 |
| 2024-09-20 22:21:39.972 | MS1 | 121.4656665550 | 31.1446347213 | 549 | 504990 | -77.45 | 14.53 | 565.66 | 0.02 | 1.35 | 1599 |
| 2024-09-20 22:21:40.385 | MS1 | 121.4656772384 | 31.1446372904 | 549 | 504990 | -81.55 | 13.23 | 493.44 | 0.07 | 2.47 | 1597 |
| 2024-09-20 22:21:41.248 | MS1 | 121.4656624567 | 31.1446324133 | 549 | 504990 | -83.67 | 15.80 | 318.28 | 0.08 | 2.01 | 1591 |
| 2024-09-20 22:21:42.348 | MS1 | 121.4656738500 | 31.1446309994 | 549 | 504990 | -84.68 | 12.16 | 303.32 | 0.15 | 2.76 | 1587 |

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
| 3211645 | 2 | 121.4717679165 | 31.1472309809 | 3 | 11 | 6 | 24.4 | TDD | 874 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3220904 | 1 | 121.4731685885 | 31.1467206963 | 261 | 8 | 10 | 46.4 | TDD | 865 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3233851 | 4 | 121.4667331102 | 31.1507739657 | 52 | 5 | 5 | 26.9 | TDD | 549 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3240520 | 3 | 121.4721821056 | 31.1502776059 | 185 | 2 | 1 | 45.0 | TDD | 3 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.598 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.620 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.762 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.762 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.408 | NREventA3 | measId:2;ServCellPCI:82;Ser... |
| 2024-09-20 22:21:36.408 | NREventA3 | measId:2;ServCellPCI:82;Ser... |
| 2024-09-20 22:21:37.408 | NREventA3 | measId:2;ServCellPCI:82;Ser... |
| 2024-09-20 22:21:39.908 | NRRRCReestablishAttempt | PCI:82 |
| 2024-09-20 22:21:39.918 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.931 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:40.054 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.054 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220904 | 1 | 12.4615 | 5.4686 | -117.2609 | 8.1312 | 157.9510 | 0.0144 | 0.0137 |
| 2024_09_20 22:00 | 3211645 | 2 | 19.9698 | 10.9240 | -114.0659 | 12.8493 | 114.6383 | 0.0017 | 0.0044 |
| 2024_09_20 22:00 | 3240520 | 3 | 13.2724 | 8.7204 | -115.0122 | 12.2107 | 167.0693 | 0.0071 | 0.0131 |
| 2024_09_20 22:00 | 3233851 | 4 | 6.4018 | 6.1516 | -117.9467 | 19.0511 | 90.7666 | 0.0008 | 0.1067 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416174_6FF8D2F4 | 504990 | 3 | -84.4 | 504990 | 549 | -90.3 | 504990 | 874 | -90.1 | 504990 | 865 |
| MR_1774416174_64345DDA | 504990 | 3 | -86.5 | 504990 | 549 | -90.4 | 504990 | 874 | -87.1 | 504990 | 865 |
| MR_1774416174_98B9C0E0 | 504990 | 3 | -85.2 | 504990 | 549 | -91.4 | 504990 | 874 | -87.1 | 504990 | 865 |
| MR_1774416174_1356FB4D | 504990 | 549 | -89.6 | 504990 | 3 | -85.1 | 504990 | 874 | -87.0 | 504990 | 865 |
| MR_1774416174_13C176CB | 504990 | 549 | -92.7 | 504990 | 3 | -84.7 | 504990 | 874 | -89.3 | 504990 | 865 |
| MR_1774416174_B8BBE1D8 | 504990 | 3 | -87.4 | 504990 | 549 | -89.3 | 504990 | 874 | -88.9 | 504990 | 865 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 152: `27a6589d-726...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `27a6589d-726a-44a9-91f7-b8cd05eed497` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Add neighbor relationship between 3248517_1 and 3245645_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[152] topology](images/train_0152.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3248517_1
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Adjust the azimuth of 3245645_4 by 33 degrees
- `C4`: Decrease A3 Offset threshold for 3245645_4
- `C5`: Add neighbor relationship between 3260045_2 and 3245645_4
- `C6`: Press down the tilt angle  of 3245645_4 by 2 degrees
- `C7`: Press down the tilt angle of 3248517_1 by 3 degrees
- `C8`: Increase A3 Offset threshold for 3248517_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245645_4
- `C10`: Add neighbor relationship between 3248517_1 and 3245645_4 **← 정답**
- `C11`: Lift the tilt angle of 3248517_1 by 3 degrees
- `C12`: Adjust the azimuth of 3248517_1 by 50 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248517_1
- `C14`: Increase transmission power for 3248517_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248517_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245645_4
- `C17`: Check test server and transmission issues
- `C18`: Increase A3 Offset threshold for 3245645_4
- `C19`: Increase transmission power for 3245645_4
- `C20`: Decrease transmission power for 3248517_1
- `C21`: Decrease transmission power for 3245645_4
- `C22`: Lift the tilt angle  of 3245645_4 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.923 | MS1 | 121.4656690809 | 31.1446319658 | 560 | 504990 | -78.05 | 17.83 | 406.63 | 0.07 | 2.74 | 1568 |
| 2024-09-20 22:21:32.265 | MS1 | 121.4656770703 | 31.1446353095 | 560 | 504990 | -79.11 | 17.99 | 295.10 | 0.10 | 2.58 | 1589 |
| 2024-09-20 22:21:33.171 | MS1 | 121.4656710315 | 31.1446222197 | 560 | 504990 | -76.37 | 16.58 | 462.87 | 0.19 | 2.39 | 1591 |
| 2024-09-20 22:21:34.614 | MS1 | 121.4656595466 | 31.1446355244 | 560 | 504990 | -93.40 | -3.34 | 45.00 | 0.01 | 1.04 | 1595 |
| 2024-09-20 22:21:35.575 | MS1 | 121.4656751412 | 31.1446192112 | 560 | 504990 | -92.88 | -3.45 | 42.67 | 0.03 | 1.48 | 1574 |
| 2024-09-20 22:21:36.389 | MS1 | 121.4656639660 | 31.1446208708 | 560 | 504990 | -88.13 | -0.91 | 43.56 | 0.18 | 1.42 | 1581 |
| 2024-09-20 22:21:37.978 | MS1 | 121.4656699431 | 31.1446205074 | 560 | 504990 | -93.25 | -1.90 | 46.46 | 0.12 | 1.04 | 1597 |
| 2024-09-20 22:21:38.724 | MS1 | 121.4656634748 | 31.1446244275 | 560 | 504990 | -78.42 | 17.68 | 315.33 | 0.05 | 1.14 | 1591 |
| 2024-09-20 22:21:39.109 | MS1 | 121.4656760674 | 31.1446249032 | 560 | 504990 | -82.42 | 14.74 | 592.45 | 0.07 | 1.20 | 1565 |
| 2024-09-20 22:21:40.229 | MS1 | 121.4656682877 | 31.1446246477 | 560 | 504990 | -84.58 | 17.87 | 594.09 | 0.15 | 2.12 | 1571 |
| 2024-09-20 22:21:41.607 | MS1 | 121.4656743325 | 31.1446323535 | 560 | 504990 | -84.17 | 12.19 | 352.94 | 0.14 | 2.25 | 1568 |
| 2024-09-20 22:21:42.768 | MS1 | 121.4656610720 | 31.1446335279 | 560 | 504990 | -83.99 | 14.71 | 432.43 | 0.10 | 2.12 | 1599 |

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
| 3239199 | 3 | 121.4700095776 | 31.1553326178 | 15 | 0 | 3 | 40.4 | TDD | 122 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3245645 | 4 | 121.4701398752 | 31.1544790124 | 234 | 1 | 7 | 15.6 | TDD | 372 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3248517 | 1 | 121.4666431103 | 31.1534597931 | 73 | 0 | 2 | 45.7 | TDD | 560 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3260045 | 2 | 121.4696481708 | 31.1469298612 | 101 | 12 | 12 | 46.9 | TDD | 240 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.178 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.199 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.332 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.332 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.002 | NREventA3 | measId:2;ServCellPCI:527;Se... |
| 2024-09-20 22:21:36.002 | NREventA3 | measId:2;ServCellPCI:527;Se... |
| 2024-09-20 22:21:37.002 | NREventA3 | measId:2;ServCellPCI:527;Se... |
| 2024-09-20 22:21:39.502 | NRRRCReestablishAttempt | PCI:527 |
| 2024-09-20 22:21:39.518 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.529 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.663 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.663 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248517 | 1 | 15.5996 | 9.3066 | -117.6491 | 5.4032 | 187.8068 | 0.0059 | 0.1675 |
| 2024_09_20 22:00 | 3260045 | 2 | 14.4682 | 10.2836 | -114.3755 | 8.1192 | 97.9062 | 0.0022 | 0.0091 |
| 2024_09_20 22:00 | 3239199 | 3 | 13.0024 | 14.2645 | -117.1971 | 17.8088 | 180.2562 | 0.0111 | 0.0180 |
| 2024_09_20 22:00 | 3245645 | 4 | 10.6886 | 6.2273 | -115.4595 | 16.1337 | 169.1187 | 0.0140 | 0.0126 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417221_F2A599AF | 504990 | 372 | -89.3 | 504990 | 560 | -92.5 | 504990 | 240 | -95.5 | 504990 | 122 |
| MR_1774417221_C3EB54C0 | 504990 | 560 | -95.1 | 504990 | 372 | -88.4 | 504990 | 240 | -95.3 | 504990 | 122 |
| MR_1774417221_4B5145DE | 504990 | 372 | -86.5 | 504990 | 560 | -93.9 | 504990 | 240 | -95.0 | 504990 | 122 |
| MR_1774417221_B009921C | 504990 | 372 | -87.4 | 504990 | 560 | -91.9 | 504990 | 240 | -92.8 | 504990 | 122 |
| MR_1774417221_A579AF24 | 504990 | 372 | -90.1 | 504990 | 560 | -92.4 | 504990 | 240 | -92.1 | 504990 | 122 |
| MR_1774417221_6626F937 | 504990 | 372 | -89.6 | 504990 | 560 | -92.1 | 504990 | 240 | -93.6 | 504990 | 122 |
| MR_1774417221_A925B01B | 504990 | 560 | -94.1 | 504990 | 372 | -87.7 | 504990 | 240 | -92.6 | 504990 | 122 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 153: `cb672d8d-e70...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cb672d8d-e701-484a-b7c5-af206304f9ae` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Add neighbor relationship between 3245582_4 and 3250147_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[153] topology](images/train_0153.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245582_4
- `C2`: Adjust the azimuth of 3250147_3 by 36 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250147_3
- `C4`: Decrease A3 Offset threshold for 3250147_3
- `C5`: Increase transmission power for 3250147_3
- `C6`: Lift the tilt angle of 3245582_4 by 10 degrees
- `C7`: Check test server and transmission issues
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250147_3
- `C9`: Adjust the azimuth of 3245582_4 by 50 degrees
- `C10`: Increase A3 Offset threshold for 3245582_4
- `C11`: Add neighbor relationship between 3245582_4 and 3250147_3 **← 정답**
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245582_4
- `C13`: Press down the tilt angle of 3245582_4 by 10 degrees
- `C14`: Decrease transmission power for 3250147_3
- `C15`: Increase transmission power for 3245582_4
- `C16`: Decrease transmission power for 3245582_4
- `C17`: Add neighbor relationship between 3220060_1 and 3250147_3
- `C18`: Increase A3 Offset threshold for 3250147_3
- `C19`: Lift the tilt angle  of 3250147_3 by 3 degrees
- `C20`: Decrease A3 Offset threshold for 3245582_4
- `C21`: Press down the tilt angle  of 3250147_3 by 3 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.147 | MS1 | 121.4656616446 | 31.1446240119 | 970 | 504990 | -76.35 | 13.57 | 516.61 | 0.19 | 2.45 | 1588 |
| 2024-09-20 22:21:32.526 | MS1 | 121.4656764941 | 31.1446369103 | 970 | 504990 | -77.46 | 12.54 | 542.40 | 0.16 | 2.83 | 1562 |
| 2024-09-20 22:21:33.357 | MS1 | 121.4656646674 | 31.1446370010 | 970 | 504990 | -80.52 | 12.35 | 389.40 | 0.08 | 2.28 | 1592 |
| 2024-09-20 22:21:34.633 | MS1 | 121.4656768461 | 31.1446286605 | 970 | 504990 | -94.59 | -3.27 | 73.19 | 0.09 | 1.21 | 1586 |
| 2024-09-20 22:21:35.971 | MS1 | 121.4656645051 | 31.1446369325 | 970 | 504990 | -86.46 | -3.91 | 52.89 | 0.11 | 1.24 | 1585 |
| 2024-09-20 22:21:36.331 | MS1 | 121.4656605573 | 31.1446362288 | 970 | 504990 | -94.11 | -1.82 | 24.83 | 0.08 | 1.26 | 1589 |
| 2024-09-20 22:21:37.871 | MS1 | 121.4656625220 | 31.1446318908 | 970 | 504990 | -87.40 | -0.94 | 30.67 | 0.06 | 1.23 | 1564 |
| 2024-09-20 22:21:38.863 | MS1 | 121.4656669362 | 31.1446230670 | 970 | 504990 | -83.18 | 14.92 | 529.91 | 0.08 | 1.19 | 1592 |
| 2024-09-20 22:21:39.264 | MS1 | 121.4656767918 | 31.1446227717 | 970 | 504990 | -78.29 | 13.04 | 435.21 | 0.12 | 1.40 | 1586 |
| 2024-09-20 22:21:40.797 | MS1 | 121.4656674445 | 31.1446372856 | 970 | 504990 | -82.82 | 12.38 | 329.93 | 0.04 | 2.73 | 1589 |
| 2024-09-20 22:21:41.455 | MS1 | 121.4656735305 | 31.1446281183 | 970 | 504990 | -75.82 | 13.50 | 456.65 | 0.12 | 2.16 | 1576 |
| 2024-09-20 22:21:42.664 | MS1 | 121.4656621544 | 31.1446354657 | 970 | 504990 | -79.97 | 17.93 | 392.10 | 0.10 | 2.78 | 1598 |

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
| 3220060 | 1 | 121.4698600009 | 31.1484288530 | 7 | 15 | 10 | 46.8 | TDD | 194 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3245582 | 4 | 121.4690384841 | 31.1473626889 | 146 | 10 | 9 | 35.6 | TDD | 970 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3250147 | 3 | 121.4720706031 | 31.1445742597 | 307 | 0 | 3 | 32.7 | TDD | 770 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3268971 | 2 | 121.4757961280 | 31.1470776011 | 166 | 13 | 6 | 44.0 | TDD | 26 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.383 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.404 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.519 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.519 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.221 | NREventA3 | measId:2;ServCellPCI:798;Se... |
| 2024-09-20 22:21:36.221 | NREventA3 | measId:2;ServCellPCI:798;Se... |
| 2024-09-20 22:21:37.221 | NREventA3 | measId:2;ServCellPCI:798;Se... |
| 2024-09-20 22:21:39.721 | NRRRCReestablishAttempt | PCI:798 |
| 2024-09-20 22:21:39.740 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.750 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.876 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.876 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220060 | 1 | 8.7455 | 18.1929 | -116.0844 | 17.1749 | 136.7241 | 0.0155 | 0.0021 |
| 2024_09_20 22:00 | 3268971 | 2 | 13.3798 | 10.7990 | -117.3437 | 16.7721 | 178.1676 | 0.0008 | 0.0157 |
| 2024_09_20 22:00 | 3250147 | 3 | 11.1086 | 13.8786 | -117.2176 | 6.1731 | 129.2220 | 0.0081 | 0.0120 |
| 2024_09_20 22:00 | 3245582 | 4 | 19.1590 | 11.7465 | -117.0287 | 7.7489 | 198.4376 | 0.0024 | 0.1863 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412872_784C79FA | 504990 | 970 | -95.5 | 504990 | 770 | -89.5 | 504990 | 194 | -92.8 | 504990 | 26 |
| MR_1774412872_7598FFDA | 504990 | 770 | -90.8 | 504990 | 970 | -96.0 | 504990 | 194 | -92.4 | 504990 | 26 |
| MR_1774412872_4C298CE3 | 504990 | 970 | -92.8 | 504990 | 770 | -88.3 | 504990 | 194 | -91.9 | 504990 | 26 |
| MR_1774412872_2D54D12C | 504990 | 970 | -96.3 | 504990 | 770 | -89.2 | 504990 | 194 | -90.6 | 504990 | 26 |
| MR_1774412872_E335F4D7 | 504990 | 970 | -93.5 | 504990 | 770 | -89.6 | 504990 | 194 | -93.2 | 504990 | 26 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 154: `ad16cd0f-7d6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ad16cd0f-7d6a-417a-bc54-fb0c50c8824a` |
| Tag | **multiple-answer** |
| 정답 | **C13|C14** |
| C13 의미 | Adjust the azimuth of 3259782_1 by 27 degrees |
| C14 의미 | Increase transmission power for 3259782_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[154] topology](images/train_0154.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259782_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243804_3
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Lift the tilt angle  of 3243804_3 by 4 degrees
- `C5`: Add neighbor relationship between 3230823_2 and 3243804_3
- `C6`: Adjust the azimuth of 3243804_3 by 34 degrees
- `C7`: Press down the tilt angle of 3259782_1 by 10 degrees
- `C8`: Decrease transmission power for 3243804_3
- `C9`: Add neighbor relationship between 3259782_1 and 3243804_3
- `C10`: Increase transmission power for 3243804_3
- `C11`: Lift the tilt angle of 3259782_1 by 10 degrees
- `C12`: Increase A3 Offset threshold for 3243804_3
- `C13`: Adjust the azimuth of 3259782_1 by 27 degrees **← 정답**
- `C14`: Increase transmission power for 3259782_1 **← 정답**
- `C15`: Press down the tilt angle  of 3243804_3 by 4 degrees
- `C16`: Decrease transmission power for 3259782_1
- `C17`: Decrease A3 Offset threshold for 3259782_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243804_3
- `C19`: Increase A3 Offset threshold for 3259782_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259782_1
- `C21`: Decrease A3 Offset threshold for 3243804_3
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.104 | MS1 | 121.4656730761 | 31.1446227130 | 674 | 504990 | -94.80 | 16.34 | 377.15 | 0.04 | 2.11 | 1600 |
| 2024-09-20 22:21:32.919 | MS1 | 121.4656707933 | 31.1446204752 | 674 | 504990 | -87.80 | 12.70 | 378.64 | 0.07 | 2.16 | 1584 |
| 2024-09-20 22:21:33.414 | MS1 | 121.4656590428 | 31.1446283803 | 674 | 504990 | -91.33 | 16.71 | 367.00 | 0.15 | 2.38 | 1582 |
| 2024-09-20 22:21:34.371 | MS1 | 121.4656746196 | 31.1446371139 | 674 | 504990 | -106.30 | -0.15 | 35.02 | 0.19 | 1.48 | 1593 |
| 2024-09-20 22:21:35.801 | MS1 | 121.4656667663 | 31.1446210611 | 674 | 504990 | -108.12 | 1.04 | 36.10 | 0.10 | 1.02 | 1574 |
| 2024-09-20 22:21:36.363 | MS1 | 121.4656660321 | 31.1446252970 | 674 | 504990 | -106.37 | 1.16 | 73.60 | 0.18 | 1.42 | 1570 |
| 2024-09-20 22:21:37.536 | MS1 | 121.4656605738 | 31.1446324760 | 674 | 504990 | -109.63 | 0.30 | 44.14 | 0.15 | 1.03 | 1592 |
| 2024-09-20 22:21:38.943 | MS1 | 121.4656657845 | 31.1446189146 | 674 | 504990 | -105.29 | -0.60 | 67.48 | 0.02 | 1.44 | 1566 |
| 2024-09-20 22:21:39.674 | MS1 | 121.4656720547 | 31.1446302047 | 674 | 504990 | -105.26 | -1.78 | 32.11 | 0.03 | 1.44 | 1575 |
| 2024-09-20 22:21:40.329 | MS1 | 121.4656634927 | 31.1446348250 | 674 | 504990 | -90.15 | 12.10 | 533.54 | 0.02 | 2.62 | 1600 |
| 2024-09-20 22:21:41.207 | MS1 | 121.4656744475 | 31.1446376870 | 674 | 504990 | -93.50 | 15.23 | 345.10 | 0.19 | 2.23 | 1565 |
| 2024-09-20 22:21:42.190 | MS1 | 121.4656692943 | 31.1446312267 | 674 | 504990 | -93.81 | 16.64 | 502.29 | 0.16 | 2.26 | 1570 |

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
| 3210550 | 4 | 121.4700015612 | 31.1477832786 | 334 | 4 | 8 | 27.5 | TDD | 310 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3230823 | 2 | 121.4681925776 | 31.1487888700 | 90 | 14 | 9 | 46.5 | TDD | 740 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3243804 | 3 | 121.4642299765 | 31.1505665189 | 134 | 1 | 10 | 34.6 | TDD | 101 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3259782 | 1 | 121.4759173365 | 31.1552666201 | 247 | 15 | 8 | 16.1 | TDD | 674 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.300 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.323 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.459 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.459 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.616 | NREventA2 | measId:1;ServCellPCI:145;Se... |
| 2024-09-20 22:21:34.724 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259782 | 1 | 16.1761 | 13.7843 | -116.8424 | 12.9349 | 152.0981 | 0.1458 | 0.0102 |
| 2024_09_20 22:00 | 3230823 | 2 | 6.6964 | 5.4867 | -115.6842 | 17.3774 | 187.8888 | 0.0176 | 0.0069 |
| 2024_09_20 22:00 | 3243804 | 3 | 5.8576 | 19.1227 | -114.0022 | 6.9066 | 145.4466 | 0.0196 | 0.0032 |
| 2024_09_20 22:00 | 3210550 | 4 | 19.8772 | 5.1376 | -115.6841 | 8.6106 | 144.2866 | 0.0126 | 0.0010 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416603_16E73FD8 | 504990 | 674 | -106.3 | 504990 | 101 | -113.4 | 504990 | 740 | -121.8 | 504990 | 310 |
| MR_1774416603_8A07F4D4 | 504990 | 674 | -104.8 | 504990 | 101 | -111.6 | 504990 | 740 | -118.5 | 504990 | 310 |
| MR_1774416603_94734219 | 504990 | 674 | -106.4 | 504990 | 101 | -114.7 | 504990 | 740 | -119.5 | 504990 | 310 |
| MR_1774416603_4BF059CE | 504990 | 674 | -107.4 | 504990 | 101 | -113.4 | 504990 | 740 | -119.6 | 504990 | 310 |
| MR_1774416603_B59E63A3 | 504990 | 674 | -105.4 | 504990 | 101 | -112.4 | 504990 | 740 | -121.3 | 504990 | 310 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 155: `dab27456-181...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dab27456-1815-4a20-ae20-7a86035af9e6` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[155] topology](images/train_0155.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3235930_1 by 8 degrees
- `C2`: Decrease transmission power for 3235930_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279041_3
- `C4`: Lift the tilt angle of 3279041_3 by 10 degrees
- `C5`: Increase A3 Offset threshold for 3235930_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235930_1
- `C7`: Check test server and transmission issues **← 정답**
- `C8`: Decrease A3 Offset threshold for 3235930_1
- `C9`: Increase transmission power for 3279041_3
- `C10`: Lift the tilt angle  of 3235930_1 by 8 degrees
- `C11`: Adjust the azimuth of 3235930_1 by 50 degrees
- `C12`: Add neighbor relationship between 3274156_4 and 3235930_1
- `C13`: Add neighbor relationship between 3279041_3 and 3235930_1
- `C14`: Increase A3 Offset threshold for 3279041_3
- `C15`: Adjust the azimuth of 3279041_3 by 31 degrees
- `C16`: Increase transmission power for 3235930_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235930_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease A3 Offset threshold for 3279041_3
- `C20`: Decrease transmission power for 3279041_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279041_3
- `C22`: Press down the tilt angle of 3279041_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.802 | MS1 | 121.4656762172 | 31.1446321833 | 490 | 504990 | -89.62 | 13.42 | 404.73 | 0.01 | 2.58 | 1576 |
| 2024-09-20 22:21:32.451 | MS1 | 121.4656592358 | 31.1446374474 | 490 | 504990 | -86.68 | 15.53 | 488.76 | 0.01 | 2.20 | 1563 |
| 2024-09-20 22:21:33.604 | MS1 | 121.4656765330 | 31.1446251342 | 490 | 504990 | -87.80 | 15.32 | 326.78 | 0.02 | 2.11 | 1573 |
| 2024-09-20 22:21:34.673 | MS1 | 121.4656608106 | 31.1446295561 | 490 | 504990 | -85.29 | 15.40 | 97.11 | 0.20 | 2.46 | 334 |
| 2024-09-20 22:21:35.782 | MS1 | 121.4656680390 | 31.1446318577 | 490 | 504990 | -85.68 | 12.48 | 72.43 | 0.19 | 2.44 | 440 |
| 2024-09-20 22:21:36.310 | MS1 | 121.4656696007 | 31.1446213560 | 490 | 504990 | -88.05 | 16.36 | 49.75 | 0.02 | 2.03 | 413 |
| 2024-09-20 22:21:37.184 | MS1 | 121.4656616848 | 31.1446345299 | 490 | 504990 | -91.58 | 10.01 | 90.03 | 0.01 | 2.45 | 424 |
| 2024-09-20 22:21:38.719 | MS1 | 121.4656766805 | 31.1446374261 | 490 | 504990 | -89.15 | 8.17 | 60.45 | 0.08 | 2.12 | 470 |
| 2024-09-20 22:21:39.749 | MS1 | 121.4656749364 | 31.1446367568 | 490 | 504990 | -93.07 | 12.27 | 85.01 | 0.05 | 2.83 | 397 |
| 2024-09-20 22:21:40.865 | MS1 | 121.4656746874 | 31.1446244830 | 490 | 504990 | -90.66 | 9.29 | 572.64 | 0.17 | 2.26 | 1599 |
| 2024-09-20 22:21:41.585 | MS1 | 121.4656652232 | 31.1446213032 | 490 | 504990 | -90.01 | 8.53 | 432.99 | 0.18 | 2.56 | 1577 |
| 2024-09-20 22:21:42.696 | MS1 | 121.4656604446 | 31.1446246737 | 490 | 504990 | -91.92 | 8.55 | 350.42 | 0.05 | 2.23 | 1576 |

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
| 3235930 | 1 | 121.4707112398 | 31.1542709069 | 51 | 7 | 3 | 22.5 | TDD | 283 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3248134 | 2 | 121.4747799123 | 31.1543083899 | 161 | 9 | 9 | 46.6 | TDD | 786 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3274156 | 4 | 121.4702905092 | 31.1495349916 | 242 | 8 | 12 | 22.0 | TDD | 931 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3279041 | 3 | 121.4691724015 | 31.1547471989 | 227 | 13 | 5 | 18.7 | TDD | 490 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.631 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.646 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.795 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.795 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.474 | NREventA3 | measId:2;ServCellPCI:347;Se... |
| 2024-09-20 22:21:38.714 | NRHandoverAttempt | SourcePCI:347;SourceNR-ARFC... |
| 2024-09-20 22:21:38.755 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.770 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.917 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.917 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235930 | 1 | 15.2614 | 9.7883 | -117.6667 | 8.6438 | 156.1341 | 0.0034 | 0.0171 |
| 2024_09_20 22:00 | 3248134 | 2 | 8.4260 | 9.3437 | -117.6066 | 17.2437 | 154.4109 | 0.0161 | 0.0037 |
| 2024_09_20 22:00 | 3279041 | 3 | 6.3179 | 7.7543 | -115.0125 | 15.3969 | 152.9011 | 0.0098 | 0.0188 |
| 2024_09_20 22:00 | 3274156 | 4 | 15.2607 | 11.1391 | -115.6677 | 14.8407 | 182.7966 | 0.0113 | 0.0125 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414871_D1794DA1 | 504990 | 490 | -86.1 | 504990 | 283 | -93.4 | 504990 | 931 | -94.0 | 504990 | 786 |
| MR_1774414871_2D139EB5 | 504990 | 490 | -85.1 | 504990 | 283 | -94.1 | 504990 | 931 | -94.5 | 504990 | 786 |
| MR_1774414871_C0DB7C10 | 504990 | 490 | -84.8 | 504990 | 283 | -91.6 | 504990 | 931 | -95.0 | 504990 | 786 |
| MR_1774414871_A68651CE | 504990 | 490 | -85.2 | 504990 | 283 | -93.5 | 504990 | 931 | -92.9 | 504990 | 786 |
| MR_1774414871_01C03C32 | 504990 | 490 | -85.8 | 504990 | 283 | -90.7 | 504990 | 931 | -92.7 | 504990 | 786 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 156: `645c62af-945...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `645c62af-9457-4a9d-a703-c4ec247a7f01` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[156] topology](images/train_0156.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3258458_4
- `C2`: Increase A3 Offset threshold for 3231955_2
- `C3`: Press down the tilt angle of 3258458_4 by 2 degrees
- `C4`: Decrease transmission power for 3258458_4
- `C5`: Press down the tilt angle  of 3231955_2 by 10 degrees
- `C6`: Adjust the azimuth of 3258458_4 by 7 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258458_4
- `C9`: Adjust the azimuth of 3231955_2 by 50 degrees
- `C10`: Decrease A3 Offset threshold for 3258458_4
- `C11`: Check test server and transmission issues **← 정답**
- `C12`: Decrease A3 Offset threshold for 3231955_2
- `C13`: Decrease transmission power for 3231955_2
- `C14`: Add neighbor relationship between 3232956_3 and 3231955_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231955_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258458_4
- `C17`: Add neighbor relationship between 3258458_4 and 3231955_2
- `C18`: Lift the tilt angle  of 3231955_2 by 10 degrees
- `C19`: Increase transmission power for 3231955_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231955_2
- `C21`: Increase A3 Offset threshold for 3258458_4
- `C22`: Lift the tilt angle of 3258458_4 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.123 | MS1 | 121.4656743885 | 31.1446341955 | 863 | 504990 | -88.49 | 17.84 | 567.75 | 0.10 | 2.01 | 1583 |
| 2024-09-20 22:21:32.596 | MS1 | 121.4656700821 | 31.1446372137 | 863 | 504990 | -87.54 | 14.36 | 340.58 | 0.08 | 2.19 | 1600 |
| 2024-09-20 22:21:33.998 | MS1 | 121.4656601759 | 31.1446223373 | 863 | 504990 | -85.31 | 15.61 | 421.73 | 0.15 | 2.90 | 1600 |
| 2024-09-20 22:21:34.438 | MS1 | 121.4656621623 | 31.1446283943 | 863 | 504990 | -91.76 | 12.21 | 67.23 | 0.09 | 2.30 | 392 |
| 2024-09-20 22:21:35.561 | MS1 | 121.4656633441 | 31.1446228830 | 863 | 504990 | -86.92 | 16.12 | 66.82 | 0.16 | 2.64 | 409 |
| 2024-09-20 22:21:36.337 | MS1 | 121.4656752881 | 31.1446249838 | 863 | 504990 | -88.43 | 16.01 | 77.83 | 0.06 | 2.68 | 470 |
| 2024-09-20 22:21:37.597 | MS1 | 121.4656770382 | 31.1446350804 | 863 | 504990 | -89.12 | 7.92 | 79.91 | 0.15 | 2.19 | 411 |
| 2024-09-20 22:21:38.554 | MS1 | 121.4656701761 | 31.1446290537 | 863 | 504990 | -92.45 | 10.75 | 76.01 | 0.13 | 2.92 | 481 |
| 2024-09-20 22:21:39.880 | MS1 | 121.4656763554 | 31.1446320247 | 863 | 504990 | -91.64 | 12.40 | 83.82 | 0.04 | 2.22 | 402 |
| 2024-09-20 22:21:40.198 | MS1 | 121.4656776264 | 31.1446252492 | 863 | 504990 | -92.32 | 10.13 | 381.21 | 0.12 | 2.61 | 1595 |
| 2024-09-20 22:21:41.644 | MS1 | 121.4656610902 | 31.1446287742 | 863 | 504990 | -91.10 | 12.86 | 371.78 | 0.11 | 2.96 | 1596 |
| 2024-09-20 22:21:42.247 | MS1 | 121.4656590642 | 31.1446299475 | 863 | 504990 | -91.63 | 7.44 | 512.38 | 0.06 | 2.85 | 1573 |

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
| 3231955 | 2 | 121.4681101305 | 31.1497862827 | 75 | 10 | 1 | 34.0 | TDD | 516 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3232956 | 3 | 121.4691462415 | 31.1458702220 | 301 | 1 | 6 | 40.9 | TDD | 252 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3239524 | 1 | 121.4741460225 | 31.1444128853 | 264 | 10 | 2 | 40.6 | TDD | 643 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3258458 | 4 | 121.4652405834 | 31.1556234409 | 171 | 1 | 7 | 18.7 | TDD | 863 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.782 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.801 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.910 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.910 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.604 | NREventA3 | measId:2;ServCellPCI:951;Se... |
| 2024-09-20 22:21:37.844 | NRHandoverAttempt | SourcePCI:951;SourceNR-ARFC... |
| 2024-09-20 22:21:37.892 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.905 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.040 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.040 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239524 | 1 | 18.9197 | 10.5347 | -114.4682 | 17.6425 | 84.1299 | 0.0062 | 0.0132 |
| 2024_09_20 22:00 | 3231955 | 2 | 6.1279 | 17.0952 | -115.0193 | 9.2457 | 135.3822 | 0.0115 | 0.0042 |
| 2024_09_20 22:00 | 3232956 | 3 | 6.0425 | 13.9779 | -116.8906 | 8.9294 | 102.3290 | 0.0146 | 0.0170 |
| 2024_09_20 22:00 | 3258458 | 4 | 9.7921 | 8.9545 | -116.7579 | 5.8120 | 183.2673 | 0.0146 | 0.0044 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415249_B41EE6B2 | 504990 | 863 | -92.2 | 504990 | 516 | -98.6 | 504990 | 252 | -102.1 | 504990 | 643 |
| MR_1774415249_9AAA8723 | 504990 | 863 | -90.1 | 504990 | 516 | -98.3 | 504990 | 252 | -100.4 | 504990 | 643 |
| MR_1774415249_D2DD7755 | 504990 | 863 | -91.3 | 504990 | 516 | -97.0 | 504990 | 252 | -101.1 | 504990 | 643 |
| MR_1774415249_F6BA79D3 | 504990 | 863 | -93.2 | 504990 | 516 | -96.2 | 504990 | 252 | -101.2 | 504990 | 643 |
| MR_1774415249_CA291076 | 504990 | 863 | -89.8 | 504990 | 516 | -98.8 | 504990 | 252 | -101.4 | 504990 | 643 |
| MR_1774415249_B3031559 | 504990 | 863 | -93.1 | 504990 | 516 | -96.8 | 504990 | 252 | -99.3 | 504990 | 643 |
| MR_1774415249_D607A33A | 504990 | 863 | -90.0 | 504990 | 516 | -99.2 | 504990 | 252 | -99.0 | 504990 | 643 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 157: `578578e7-a41...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `578578e7-a410-4c9c-8cb8-a54babdaf60c` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242598_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[157] topology](images/train_0157.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3224361_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242598_1 **← 정답**
- `C3`: Add neighbor relationship between 3225258_9 and 3224361_3
- `C4`: Press down the tilt angle  of 3224361_3 by 5 degrees
- `C5`: Check test server and transmission issues
- `C6`: Increase A3 Offset threshold for 3224361_3
- `C7`: Increase transmission power for 3242598_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224361_3
- `C9`: Decrease transmission power for 3242598_1
- `C10`: Lift the tilt angle  of 3224361_3 by 5 degrees
- `C11`: Add neighbor relationship between 3242598_1 and 3224361_3
- `C12`: Adjust the azimuth of 3242598_1 by 6 degrees
- `C13`: Increase A3 Offset threshold for 3242598_1
- `C14`: Lift the tilt angle of 3242598_1 by 4 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224361_3
- `C16`: Decrease A3 Offset threshold for 3224361_3
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease transmission power for 3224361_3
- `C19`: Decrease A3 Offset threshold for 3242598_1
- `C20`: Press down the tilt angle of 3242598_1 by 4 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242598_1
- `C22`: Adjust the azimuth of 3224361_3 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.192 | MS1 | 121.4656648291 | 31.1446276897 | 448 | 504990 | -93.90 | 14.78 | 314.93 | 0.20 | 2.37 | 1588 |
| 2024-09-20 22:21:32.539 | MS1 | 121.4656621603 | 31.1446365473 | 345 | 504990 | -94.39 | 14.33 | 379.29 | 0.05 | 2.20 | 1590 |
| 2024-09-20 22:21:33.505 | MS1 | 121.4656597211 | 31.1446301926 | 962 | 504990 | -94.58 | 13.60 | 322.73 | 0.19 | 2.42 | 1582 |
| 2024-09-20 22:21:34.837 | MS1 | 121.4656627185 | 31.1446304120 | 879 | 152650 | -88.13 | 3.35 | 58.13 | 0.14 | 1.75 | 981 |
| 2024-09-20 22:21:35.846 | MS1 | 121.4656662328 | 31.1446263571 | 929 | 152650 | -91.47 | 5.86 | 67.35 | 0.14 | 1.57 | 945 |
| 2024-09-20 22:21:36.695 | MS1 | 121.4656728793 | 31.1446265373 | 556 | 152650 | -91.92 | 6.09 | 65.37 | 0.09 | 1.75 | 906 |
| 2024-09-20 22:21:37.743 | MS1 | 121.4656734364 | 31.1446335962 | 613 | 152650 | -92.29 | 6.90 | 84.87 | 0.06 | 1.79 | 991 |
| 2024-09-20 22:21:38.472 | MS1 | 121.4656730066 | 31.1446280273 | 879 | 152650 | -93.02 | 3.36 | 91.25 | 0.11 | 1.93 | 906 |
| 2024-09-20 22:21:39.271 | MS1 | 121.4656647733 | 31.1446332766 | 929 | 152650 | -94.66 | 7.83 | 51.19 | 0.16 | 1.63 | 998 |
| 2024-09-20 22:21:40.965 | MS1 | 121.4656779072 | 31.1446342359 | 556 | 152650 | -88.97 | 3.49 | 77.15 | 0.05 | 2.87 | 1586 |
| 2024-09-20 22:21:41.726 | MS1 | 121.4656613458 | 31.1446350545 | 613 | 152650 | -87.19 | 7.45 | 88.71 | 0.19 | 2.05 | 1582 |
| 2024-09-20 22:21:42.129 | MS1 | 121.4656688873 | 31.1446375014 | 879 | 152650 | -89.64 | 6.73 | 54.69 | 0.09 | 2.76 | 1566 |

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
| 3217054 | 10 | 121.4662713820 | 31.1500695521 | 200 | 5 | 1 | 20.9 | FDD | 879 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3221512 | 11 | 121.4644282118 | 31.1524117425 | 39 | 9 | 3 | 21.3 | FDD | 848 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3223695 | 13 | 121.4689648140 | 31.1500243408 | 237 | 12 | 7 | 5.7 | FDD | 445 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3224361 | 3 | 121.4695700585 | 31.1453092010 | 256 | 1 | 3 | 26.5 | TDD | 871 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3225258 | 9 | 121.4720174673 | 31.1473279154 | 54 | 10 | 9 | 21.7 | FDD | 556 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3237050 | 5 | 121.4733634712 | 31.1535585445 | 97 | 2 | 4 | 27.1 | TDD | 983 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3238044 | 7 | 121.4650426967 | 31.1502248038 | 221 | 9 | 7 | 20.1 | FDD | 929 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3242598 | 1 | 121.4733329287 | 31.1453752066 | 258 | 3 | 7 | 14.6 | TDD | 448 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3261341 | 8 | 121.4708567946 | 31.1487750589 | 63 | 14 | 8 | 27.1 | FDD | 613 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3263940 | 2 | 121.4707400135 | 31.1547858885 | 277 | 15 | 6 | 10.7 | TDD | 962 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3270253 | 4 | 121.4691735097 | 31.1556718851 | 104 | 11 | 0 | 15.7 | TDD | 337 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3272766 | 12 | 121.4706223423 | 31.1497881644 | 223 | 14 | 3 | 20.1 | FDD | 370 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3275878 | 6 | 121.4680412998 | 31.1522071269 | 332 | 0 | 8 | 12.1 | TDD | 345 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.418 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.441 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.549 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.549 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.226 | NREventA2 | measId:1;ServCellPCI:908;Se... |
| 2024-09-20 22:21:35.338 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.634 | NREventA5 | measId:3;ServCellPCI:908;Se... |
| 2024-09-20 22:21:35.667 | NRHandoverAttempt | SourcePCI:908;SourceNR-ARFC... |
| 2024-09-20 22:21:35.702 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.716 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.819 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.819 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242598 | 1 | 16.8555 | 5.0588 | -117.3555 | 10.3749 | 160.2446 | 0.0120 | 0.0134 |
| 2024_09_20 22:00 | 3263940 | 2 | 10.1377 | 18.2300 | -115.5802 | 14.3775 | 129.4595 | 0.0089 | 0.0042 |
| 2024_09_20 22:00 | 3224361 | 3 | 19.1597 | 11.6609 | -116.9421 | 6.1303 | 168.0279 | 0.0130 | 0.0174 |
| 2024_09_20 22:00 | 3270253 | 4 | 9.8874 | 14.5625 | -116.7260 | 11.1645 | 191.0245 | 0.0144 | 0.0198 |
| 2024_09_20 22:00 | 3237050 | 5 | 7.7796 | 5.5247 | -116.0616 | 11.9005 | 176.1261 | 0.0042 | 0.0086 |
| 2024_09_20 22:00 | 3275878 | 6 | 11.6515 | 8.6000 | -114.4213 | 18.4018 | 163.2783 | 0.0133 | 0.0021 |
| 2024_09_20 22:00 | 3238044 | 7 | 5.3113 | 6.5026 | -116.7682 | 4.6592 | 28.9620 | 0.0162 | 0.0114 |
| 2024_09_20 22:00 | 3261341 | 8 | 7.0987 | 10.4776 | -116.0350 | 4.2585 | 49.8445 | 0.0177 | 0.0197 |
| 2024_09_20 22:00 | 3225258 | 9 | 14.9793 | 9.5075 | -115.5532 | 3.9115 | 36.5724 | 0.0088 | 0.0115 |
| 2024_09_20 22:00 | 3217054 | 10 | 5.4739 | 6.1719 | -115.4035 | 4.4235 | 55.9205 | 0.0188 | 0.0189 |
| 2024_09_20 22:00 | 3221512 | 11 | 7.6707 | 6.5789 | -115.6812 | 4.2091 | 28.2013 | 0.0095 | 0.0137 |
| 2024_09_20 22:00 | 3272766 | 12 | 15.1369 | 10.7216 | -116.5800 | 3.7404 | 20.4129 | 0.0014 | 0.0004 |
| 2024_09_20 22:00 | 3223695 | 13 | 11.4811 | 7.6193 | -116.9567 | 4.7622 | 56.2149 | 0.0191 | 0.0165 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412912_AF640BF4 | 504990 | 962 | -93.4 | 504990 | 871 | -94.2 | 504990 | 983 | -99.0 | 504990 | 337 |
| MR_1774412912_277C1DFD | 152650 | 879 | -89.5 | 152650 | 848 | -95.4 | 152650 | 370 | -97.4 | 152650 | 445 |
| MR_1774412912_42A67036 | 152650 | 879 | -86.2 | 152650 | 848 | -96.9 | 152650 | 370 | -98.9 | 152650 | 445 |
| MR_1774412912_D2BC64F7 | 152650 | 879 | -89.1 | 152650 | 848 | -96.6 | 152650 | 370 | -98.8 | 152650 | 445 |
| MR_1774412912_3E6A1009 | 504990 | 962 | -92.7 | 504990 | 871 | -94.1 | 504990 | 983 | -98.6 | 504990 | 337 |
| MR_1774412912_E955CF78 | 152650 | 879 | -88.3 | 152650 | 848 | -96.6 | 152650 | 370 | -98.0 | 152650 | 445 |
| MR_1774412912_C7D2E468 | 152650 | 879 | -88.5 | 152650 | 848 | -96.7 | 152650 | 370 | -98.7 | 152650 | 445 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 158: `9521614b-c1c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9521614b-c1cd-4f70-b370-490dfd74a211` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Add neighbor relationship between 3229986_4 and 3238308_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[158] topology](images/train_0158.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3229986_4 and 3238308_3 **← 정답**
- `C2`: Adjust the azimuth of 3238308_3 by 1 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238308_3
- `C4`: Increase transmission power for 3229986_4
- `C5`: Decrease A3 Offset threshold for 3238308_3
- `C6`: Press down the tilt angle  of 3238308_3 by 4 degrees
- `C7`: Lift the tilt angle  of 3238308_3 by 4 degrees
- `C8`: Increase A3 Offset threshold for 3238308_3
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Adjust the azimuth of 3229986_4 by 50 degrees
- `C11`: Decrease transmission power for 3238308_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229986_4
- `C13`: Add neighbor relationship between 3256486_1 and 3238308_3
- `C14`: Decrease transmission power for 3229986_4
- `C15`: Lift the tilt angle of 3229986_4 by 10 degrees
- `C16`: Increase transmission power for 3238308_3
- `C17`: Decrease A3 Offset threshold for 3229986_4
- `C18`: Press down the tilt angle of 3229986_4 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3229986_4
- `C20`: Check test server and transmission issues
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238308_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229986_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.899 | MS1 | 121.4656654219 | 31.1446231807 | 38 | 504990 | -76.80 | 17.91 | 314.99 | 0.09 | 2.74 | 1570 |
| 2024-09-20 22:21:32.474 | MS1 | 121.4656600041 | 31.1446222689 | 38 | 504990 | -79.68 | 16.38 | 510.79 | 0.04 | 2.06 | 1588 |
| 2024-09-20 22:21:33.152 | MS1 | 121.4656611451 | 31.1446285915 | 38 | 504990 | -83.47 | 13.43 | 465.74 | 0.19 | 2.98 | 1578 |
| 2024-09-20 22:21:34.623 | MS1 | 121.4656661267 | 31.1446353259 | 38 | 504990 | -93.61 | -2.27 | 62.03 | 0.19 | 1.11 | 1596 |
| 2024-09-20 22:21:35.674 | MS1 | 121.4656668713 | 31.1446305806 | 38 | 504990 | -91.78 | -0.05 | 49.48 | 0.14 | 1.17 | 1596 |
| 2024-09-20 22:21:36.396 | MS1 | 121.4656724054 | 31.1446345596 | 38 | 504990 | -92.84 | -1.53 | 49.69 | 0.05 | 1.31 | 1563 |
| 2024-09-20 22:21:37.595 | MS1 | 121.4656755785 | 31.1446232980 | 38 | 504990 | -87.46 | -1.51 | 59.27 | 0.04 | 1.03 | 1588 |
| 2024-09-20 22:21:38.404 | MS1 | 121.4656623951 | 31.1446337997 | 38 | 504990 | -76.36 | 16.77 | 397.81 | 0.12 | 1.27 | 1582 |
| 2024-09-20 22:21:39.267 | MS1 | 121.4656625845 | 31.1446217947 | 38 | 504990 | -76.20 | 13.05 | 380.40 | 0.07 | 1.32 | 1589 |
| 2024-09-20 22:21:40.786 | MS1 | 121.4656597681 | 31.1446338212 | 38 | 504990 | -82.59 | 16.32 | 387.89 | 0.05 | 2.88 | 1593 |
| 2024-09-20 22:21:41.773 | MS1 | 121.4656582123 | 31.1446234080 | 38 | 504990 | -79.92 | 16.51 | 342.37 | 0.07 | 2.44 | 1588 |
| 2024-09-20 22:21:42.884 | MS1 | 121.4656587753 | 31.1446272403 | 38 | 504990 | -79.24 | 15.90 | 417.72 | 0.17 | 2.16 | 1561 |

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
| 3221397 | 2 | 121.4738877852 | 31.1535641710 | 219 | 6 | 0 | 27.5 | TDD | 108 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3229986 | 4 | 121.4710000409 | 31.1539654685 | 78 | 8 | 3 | 40.7 | TDD | 38 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3238308 | 3 | 121.4753819558 | 31.1514210144 | 232 | 3 | 3 | 24.8 | TDD | 509 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3256486 | 1 | 121.4724493598 | 31.1533271351 | 181 | 0 | 1 | 34.2 | TDD | 449 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.424 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.445 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.575 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.575 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.281 | NREventA3 | measId:2;ServCellPCI:476;Se... |
| 2024-09-20 22:21:36.281 | NREventA3 | measId:2;ServCellPCI:476;Se... |
| 2024-09-20 22:21:37.281 | NREventA3 | measId:2;ServCellPCI:476;Se... |
| 2024-09-20 22:21:39.781 | NRRRCReestablishAttempt | PCI:476 |
| 2024-09-20 22:21:39.791 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.801 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.931 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.931 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256486 | 1 | 6.5423 | 17.4902 | -116.6474 | 9.9671 | 81.4266 | 0.0017 | 0.0034 |
| 2024_09_20 22:00 | 3221397 | 2 | 6.2787 | 8.2550 | -115.9857 | 17.0599 | 147.8730 | 0.0053 | 0.0130 |
| 2024_09_20 22:00 | 3238308 | 3 | 16.5270 | 7.7312 | -117.4002 | 11.0608 | 163.9233 | 0.0086 | 0.0014 |
| 2024_09_20 22:00 | 3229986 | 4 | 19.6254 | 8.7371 | -115.5427 | 5.9239 | 143.5040 | 0.0175 | 0.1776 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416028_D8EAE838 | 504990 | 38 | -91.7 | 504990 | 509 | -87.2 | 504990 | 449 | -95.1 | 504990 | 108 |
| MR_1774416028_2D3253DF | 504990 | 38 | -93.2 | 504990 | 509 | -90.7 | 504990 | 449 | -95.2 | 504990 | 108 |
| MR_1774416028_FF43EFDD | 504990 | 38 | -94.8 | 504990 | 509 | -88.0 | 504990 | 449 | -96.7 | 504990 | 108 |
| MR_1774416028_79E2A616 | 504990 | 38 | -92.0 | 504990 | 509 | -90.1 | 504990 | 449 | -96.0 | 504990 | 108 |
| MR_1774416028_13D0AE04 | 504990 | 509 | -89.0 | 504990 | 38 | -93.3 | 504990 | 449 | -93.6 | 504990 | 108 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 159: `697c329f-035...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `697c329f-0356-434c-b362-1bf0aeb4835d` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease A3 Offset threshold for 3242040_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[159] topology](images/train_0159.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3242040_1
- `C2`: Decrease transmission power for 3242040_1
- `C3`: Adjust the azimuth of 3242040_1 by 9 degrees
- `C4`: Increase A3 Offset threshold for 3242040_1
- `C5`: Add neighbor relationship between 3220135_2 and 3257496_4
- `C6`: Decrease transmission power for 3257496_4
- `C7`: Adjust the azimuth of 3257496_4 by 50 degrees
- `C8`: Add neighbor relationship between 3242040_1 and 3257496_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242040_1
- `C10`: Increase A3 Offset threshold for 3257496_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257496_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257496_4
- `C13`: Check test server and transmission issues
- `C14`: Decrease A3 Offset threshold for 3242040_1 **← 정답**
- `C15`: Decrease A3 Offset threshold for 3257496_4
- `C16`: Increase transmission power for 3257496_4
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Press down the tilt angle of 3242040_1 by 10 degrees
- `C19`: Lift the tilt angle  of 3257496_4 by 4 degrees
- `C20`: Press down the tilt angle  of 3257496_4 by 4 degrees
- `C21`: Lift the tilt angle of 3242040_1 by 10 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242040_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.152 | MS1 | 121.4656621104 | 31.1446309487 | 200 | 504990 | -84.29 | 14.71 | 358.22 | 0.18 | 2.79 | 1574 |
| 2024-09-20 22:21:32.369 | MS1 | 121.4656742560 | 31.1446231855 | 200 | 504990 | -84.77 | 13.00 | 401.35 | 0.16 | 2.93 | 1563 |
| 2024-09-20 22:21:33.865 | MS1 | 121.4656707634 | 31.1446290941 | 200 | 504990 | -81.93 | 15.88 | 560.04 | 0.08 | 2.38 | 1600 |
| 2024-09-20 22:21:34.991 | MS1 | 121.4656719016 | 31.1446245602 | 200 | 504990 | -90.36 | -2.85 | 42.61 | 0.16 | 1.39 | 1594 |
| 2024-09-20 22:21:35.481 | MS1 | 121.4656681698 | 31.1446351371 | 200 | 504990 | -85.14 | -2.06 | 73.64 | 0.14 | 1.39 | 1564 |
| 2024-09-20 22:21:36.627 | MS1 | 121.4656677295 | 31.1446315544 | 200 | 504990 | -84.57 | -0.30 | 29.15 | 0.12 | 1.00 | 1589 |
| 2024-09-20 22:21:37.589 | MS1 | 121.4656662499 | 31.1446205571 | 200 | 504990 | -88.02 | -0.64 | 41.86 | 0.03 | 1.50 | 1580 |
| 2024-09-20 22:21:38.521 | MS1 | 121.4656744925 | 31.1446262205 | 200 | 504990 | -83.59 | -2.05 | 50.41 | 0.10 | 1.08 | 1572 |
| 2024-09-20 22:21:39.581 | MS1 | 121.4656753374 | 31.1446353122 | 685 | 504990 | -77.55 | 15.56 | 159.35 | 0.19 | 1.01 | 1599 |
| 2024-09-20 22:21:40.858 | MS1 | 121.4656751877 | 31.1446235100 | 685 | 504990 | -78.45 | 15.58 | 378.31 | 0.07 | 2.15 | 1597 |
| 2024-09-20 22:21:41.170 | MS1 | 121.4656683996 | 31.1446357907 | 685 | 504990 | -78.01 | 17.53 | 359.06 | 0.18 | 2.78 | 1572 |
| 2024-09-20 22:21:42.715 | MS1 | 121.4656700038 | 31.1446252177 | 685 | 504990 | -81.13 | 17.56 | 465.21 | 0.05 | 2.67 | 1600 |

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
| 3220135 | 2 | 121.4695192012 | 31.1531158773 | 214 | 3 | 7 | 25.5 | TDD | 946 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3242040 | 1 | 121.4669518625 | 31.1465790241 | 200 | 10 | 9 | 46.1 | TDD | 200 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3257496 | 4 | 121.4742266712 | 31.1554228935 | 89 | 3 | 0 | 22.6 | TDD | 685 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3258371 | 3 | 121.4753696438 | 31.1479145196 | 177 | 15 | 5 | 16.5 | TDD | 725 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.826 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.850 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.978 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.978 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.661 | NREventA3 | measId:2;ServCellPCI:361;Se... |
| 2024-09-20 22:21:37.901 | NRHandoverAttempt | SourcePCI:361;SourceNR-ARFC... |
| 2024-09-20 22:21:37.944 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.958 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.099 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.099 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242040 | 1 | 9.0862 | 17.3705 | -116.5707 | 17.0991 | 119.9624 | 0.0039 | 0.1356 |
| 2024_09_20 22:00 | 3220135 | 2 | 19.9156 | 19.3865 | -115.3993 | 7.1652 | 159.5617 | 0.0044 | 0.0080 |
| 2024_09_20 22:00 | 3258371 | 3 | 11.6940 | 5.4040 | -117.5127 | 8.8702 | 114.3072 | 0.0187 | 0.0160 |
| 2024_09_20 22:00 | 3257496 | 4 | 17.6044 | 8.4489 | -116.0108 | 7.2434 | 139.6997 | 0.0086 | 0.0091 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416850_095B6C2B | 504990 | 200 | -88.5 | 504990 | 685 | -83.4 | 504990 | 946 | -91.3 | 504990 | 725 |
| MR_1774416850_BF337B3A | 504990 | 200 | -90.8 | 504990 | 685 | -86.4 | 504990 | 946 | -91.3 | 504990 | 725 |
| MR_1774416850_6981E9C8 | 504990 | 200 | -90.8 | 504990 | 685 | -86.7 | 504990 | 946 | -88.9 | 504990 | 725 |
| MR_1774416850_35FDF867 | 504990 | 200 | -88.8 | 504990 | 685 | -83.6 | 504990 | 946 | -90.4 | 504990 | 725 |
| MR_1774416850_8C234F01 | 504990 | 685 | -83.4 | 504990 | 200 | -89.6 | 504990 | 946 | -90.8 | 504990 | 725 |
| MR_1774416850_A040A318 | 504990 | 685 | -83.5 | 504990 | 200 | -88.8 | 504990 | 946 | -88.6 | 504990 | 725 |
| MR_1774416850_F58EA2E8 | 504990 | 685 | -86.8 | 504990 | 200 | -92.0 | 504990 | 946 | -91.6 | 504990 | 725 |
| MR_1774416850_CC2CD04A | 504990 | 200 | -90.2 | 504990 | 685 | -86.3 | 504990 | 946 | -89.8 | 504990 | 725 |

> *... 2개 열 생략 (전체 14열)*

---
