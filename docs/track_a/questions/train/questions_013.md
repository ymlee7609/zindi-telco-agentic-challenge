# Track A 문제 분석 — train[120]~train[129]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[120] ~ train[129] (10개)

## 목차

1. [문제 120: `93a254e0-090...`](#120) — single-answer, 정답: C3
2. [문제 121: `a898f1f7-aab...`](#121) — single-answer, 정답: C14
3. [문제 122: `468157b8-d11...`](#122) — multiple-answer, 정답: C11|C12
4. [문제 123: `056f3d8d-b11...`](#123) — single-answer, 정답: C1
5. [문제 124: `dfa8e9f8-6fa...`](#124) — single-answer, 정답: C9
6. [문제 125: `86de99d1-e06...`](#125) — single-answer, 정답: C6
7. [문제 126: `ca034a30-c57...`](#126) — single-answer, 정답: C10
8. [문제 127: `129e51ff-45f...`](#127) — single-answer, 정답: C16
9. [문제 128: `2d46c9b7-910...`](#128) — single-answer, 정답: C20
10. [문제 129: `699572cb-cc8...`](#129) — single-answer, 정답: C1

---

### 문제 120: `93a254e0-090...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `93a254e0-090c-4b80-b8db-d07a8646ae3a` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease A3 Offset threshold for 3254684_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[120] topology](images/train_0120.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3257033_1 by 3 degrees
- `C2`: Increase A3 Offset threshold for 3257033_1
- `C3`: Decrease A3 Offset threshold for 3254684_3 **← 정답**
- `C4`: Lift the tilt angle of 3254684_3 by 8 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease A3 Offset threshold for 3257033_1
- `C7`: Press down the tilt angle of 3254684_3 by 8 degrees
- `C8`: Add neighbor relationship between 3254684_3 and 3257033_1
- `C9`: Press down the tilt angle  of 3257033_1 by 3 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254684_3
- `C11`: Decrease transmission power for 3257033_1
- `C12`: Increase transmission power for 3257033_1
- `C13`: Adjust the azimuth of 3254684_3 by 50 degrees
- `C14`: Decrease transmission power for 3254684_3
- `C15`: Increase transmission power for 3254684_3
- `C16`: Increase A3 Offset threshold for 3254684_3
- `C17`: Adjust the azimuth of 3257033_1 by 50 degrees
- `C18`: Check test server and transmission issues
- `C19`: Add neighbor relationship between 3261423_4 and 3257033_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257033_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257033_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254684_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.655 | MS1 | 121.4656723955 | 31.1446321451 | 748 | 504990 | -83.72 | 14.03 | 426.45 | 0.17 | 2.29 | 1567 |
| 2024-09-20 22:21:32.360 | MS1 | 121.4656677087 | 31.1446314188 | 748 | 504990 | -77.55 | 15.80 | 519.84 | 0.09 | 2.74 | 1588 |
| 2024-09-20 22:21:33.900 | MS1 | 121.4656714447 | 31.1446307754 | 748 | 504990 | -76.29 | 12.09 | 449.45 | 0.06 | 2.97 | 1586 |
| 2024-09-20 22:21:34.858 | MS1 | 121.4656700505 | 31.1446196230 | 748 | 504990 | -92.03 | -3.54 | 64.89 | 0.16 | 1.35 | 1577 |
| 2024-09-20 22:21:35.212 | MS1 | 121.4656699119 | 31.1446378462 | 748 | 504990 | -85.64 | -3.49 | 66.38 | 0.11 | 1.11 | 1570 |
| 2024-09-20 22:21:36.772 | MS1 | 121.4656750978 | 31.1446188144 | 748 | 504990 | -85.96 | -3.09 | 72.71 | 0.01 | 1.48 | 1564 |
| 2024-09-20 22:21:37.294 | MS1 | 121.4656668373 | 31.1446269335 | 748 | 504990 | -87.70 | -0.57 | 68.12 | 0.10 | 1.22 | 1566 |
| 2024-09-20 22:21:38.868 | MS1 | 121.4656771095 | 31.1446217096 | 748 | 504990 | -90.31 | -1.03 | 44.50 | 0.01 | 1.38 | 1566 |
| 2024-09-20 22:21:39.609 | MS1 | 121.4656754036 | 31.1446300206 | 570 | 504990 | -76.27 | 14.46 | 245.73 | 0.02 | 1.15 | 1577 |
| 2024-09-20 22:21:40.536 | MS1 | 121.4656722175 | 31.1446304650 | 570 | 504990 | -75.30 | 15.55 | 461.00 | 0.04 | 2.38 | 1591 |
| 2024-09-20 22:21:41.516 | MS1 | 121.4656729744 | 31.1446220128 | 570 | 504990 | -80.85 | 17.61 | 361.55 | 0.06 | 2.41 | 1580 |
| 2024-09-20 22:21:42.957 | MS1 | 121.4656771676 | 31.1446193642 | 570 | 504990 | -82.37 | 13.47 | 378.94 | 0.05 | 2.76 | 1570 |

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
| 3254684 | 3 | 121.4758027106 | 31.1517598166 | 139 | 6 | 2 | 35.0 | TDD | 748 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3257033 | 1 | 121.4704888712 | 31.1521501889 | 317 | 1 | 0 | 39.5 | TDD | 570 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3261423 | 4 | 121.4702697480 | 31.1499396051 | 294 | 8 | 10 | 24.7 | TDD | 354 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3264427 | 2 | 121.4739193607 | 31.1477017454 | 291 | 8 | 9 | 35.0 | TDD | 659 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.228 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.245 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.382 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.382 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.120 | NREventA3 | measId:2;ServCellPCI:229;Se... |
| 2024-09-20 22:21:38.360 | NRHandoverAttempt | SourcePCI:229;SourceNR-ARFC... |
| 2024-09-20 22:21:38.400 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.414 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.534 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.534 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257033 | 1 | 19.8297 | 18.6141 | -114.8403 | 18.0398 | 155.8081 | 0.0065 | 0.0146 |
| 2024_09_20 22:00 | 3264427 | 2 | 16.6331 | 10.3887 | -117.3376 | 12.6981 | 137.0355 | 0.0104 | 0.0003 |
| 2024_09_20 22:00 | 3254684 | 3 | 5.2638 | 19.8819 | -114.8396 | 18.1480 | 106.7048 | 0.0121 | 0.1788 |
| 2024_09_20 22:00 | 3261423 | 4 | 16.0887 | 19.9900 | -114.1533 | 10.7713 | 138.0912 | 0.0190 | 0.0123 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412495_E8A3F26C | 504990 | 748 | -91.1 | 504990 | 570 | -87.0 | 504990 | 354 | -88.0 | 504990 | 659 |
| MR_1774412495_5A1BAEFA | 504990 | 748 | -91.7 | 504990 | 570 | -88.3 | 504990 | 354 | -88.1 | 504990 | 659 |
| MR_1774412495_55FB4F00 | 504990 | 570 | -88.0 | 504990 | 748 | -92.0 | 504990 | 354 | -89.2 | 504990 | 659 |
| MR_1774412495_8FEBC9D5 | 504990 | 570 | -86.0 | 504990 | 748 | -92.1 | 504990 | 354 | -86.3 | 504990 | 659 |
| MR_1774412495_7852C479 | 504990 | 570 | -85.8 | 504990 | 748 | -93.1 | 504990 | 354 | -89.1 | 504990 | 659 |
| MR_1774412495_226B61DA | 504990 | 570 | -88.2 | 504990 | 748 | -91.1 | 504990 | 354 | -86.5 | 504990 | 659 |
| MR_1774412495_789DAF3E | 504990 | 570 | -87.1 | 504990 | 748 | -91.6 | 504990 | 354 | -89.6 | 504990 | 659 |
| MR_1774412495_D7E1E605 | 504990 | 748 | -92.0 | 504990 | 570 | -85.6 | 504990 | 354 | -87.3 | 504990 | 659 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 121: `a898f1f7-aab...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a898f1f7-aab3-40b7-8b2a-2595141eb6eb` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[121] topology](images/train_0121.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3225542_1 by 9 degrees
- `C2`: Add neighbor relationship between 3258202_3 and 3225542_1
- `C3`: Decrease A3 Offset threshold for 3258202_3
- `C4`: Increase transmission power for 3258202_3
- `C5`: Increase A3 Offset threshold for 3258202_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258202_3
- `C7`: Decrease A3 Offset threshold for 3225542_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225542_1
- `C9`: Adjust the azimuth of 3258202_3 by 50 degrees
- `C10`: Press down the tilt angle of 3258202_3 by 10 degrees
- `C11`: Adjust the azimuth of 3225542_1 by 50 degrees
- `C12`: Add neighbor relationship between 3257949_2 and 3225542_1
- `C13`: Decrease transmission power for 3258202_3
- `C14`: Check test server and transmission issues **← 정답**
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258202_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225542_1
- `C18`: Lift the tilt angle of 3258202_3 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3225542_1
- `C20`: Lift the tilt angle  of 3225542_1 by 9 degrees
- `C21`: Decrease transmission power for 3225542_1
- `C22`: Increase transmission power for 3225542_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.662 | MS1 | 121.4656715536 | 31.1446195541 | 675 | 504990 | -89.42 | 15.60 | 457.26 | 0.08 | 2.66 | 1599 |
| 2024-09-20 22:21:32.356 | MS1 | 121.4656653781 | 31.1446341167 | 675 | 504990 | -86.02 | 13.33 | 565.60 | 0.10 | 2.69 | 1576 |
| 2024-09-20 22:21:33.711 | MS1 | 121.4656663992 | 31.1446255911 | 675 | 504990 | -86.95 | 17.84 | 420.28 | 0.12 | 2.72 | 1570 |
| 2024-09-20 22:21:34.231 | MS1 | 121.4656614328 | 31.1446237932 | 675 | 504990 | -91.10 | 16.03 | 91.74 | 0.01 | 2.93 | 458 |
| 2024-09-20 22:21:35.788 | MS1 | 121.4656692766 | 31.1446196615 | 675 | 504990 | -87.15 | 15.35 | 64.11 | 0.11 | 2.55 | 382 |
| 2024-09-20 22:21:36.711 | MS1 | 121.4656624220 | 31.1446232056 | 675 | 504990 | -86.06 | 12.08 | 74.19 | 0.08 | 2.33 | 403 |
| 2024-09-20 22:21:37.648 | MS1 | 121.4656723159 | 31.1446194569 | 675 | 504990 | -93.82 | 9.94 | 78.63 | 0.14 | 2.71 | 335 |
| 2024-09-20 22:21:38.310 | MS1 | 121.4656647325 | 31.1446224819 | 675 | 504990 | -93.05 | 11.74 | 73.16 | 0.16 | 2.91 | 371 |
| 2024-09-20 22:21:39.456 | MS1 | 121.4656758559 | 31.1446373795 | 675 | 504990 | -91.38 | 7.76 | 60.50 | 0.13 | 2.08 | 345 |
| 2024-09-20 22:21:40.741 | MS1 | 121.4656707232 | 31.1446267201 | 675 | 504990 | -93.25 | 11.37 | 432.28 | 0.04 | 2.03 | 1576 |
| 2024-09-20 22:21:41.460 | MS1 | 121.4656765672 | 31.1446232924 | 675 | 504990 | -92.43 | 8.69 | 559.98 | 0.07 | 2.87 | 1561 |
| 2024-09-20 22:21:42.987 | MS1 | 121.4656631899 | 31.1446339159 | 675 | 504990 | -91.70 | 12.87 | 340.15 | 0.16 | 2.64 | 1565 |

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
| 3220716 | 4 | 121.4716904325 | 31.1483068289 | 286 | 10 | 8 | 32.9 | TDD | 846 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3225542 | 1 | 121.4679924483 | 31.1449598605 | 127 | 1 | 12 | 30.3 | TDD | 416 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3257949 | 2 | 121.4665869871 | 31.1509261084 | 250 | 3 | 7 | 32.2 | TDD | 585 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3258202 | 3 | 121.4642321702 | 31.1501611473 | 71 | 14 | 3 | 36.4 | TDD | 675 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.927 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.947 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.071 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.071 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.760 | NREventA3 | measId:2;ServCellPCI:744;Se... |
| 2024-09-20 22:21:38.000 | NRHandoverAttempt | SourcePCI:744;SourceNR-ARFC... |
| 2024-09-20 22:21:38.036 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.046 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.164 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.164 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225542 | 1 | 11.1089 | 18.4418 | -114.9659 | 15.6433 | 84.5000 | 0.0116 | 0.0130 |
| 2024_09_20 22:00 | 3257949 | 2 | 15.0243 | 18.7747 | -116.0171 | 6.5903 | 87.5249 | 0.0080 | 0.0088 |
| 2024_09_20 22:00 | 3258202 | 3 | 17.8841 | 18.4069 | -116.6283 | 12.3166 | 143.6521 | 0.0100 | 0.0111 |
| 2024_09_20 22:00 | 3220716 | 4 | 15.2014 | 15.5999 | -114.6010 | 12.3149 | 125.9522 | 0.0086 | 0.0124 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414878_C0731391 | 504990 | 675 | -92.9 | 504990 | 416 | -99.7 | 504990 | 585 | -103.1 | 504990 | 846 |
| MR_1774414878_184C90D1 | 504990 | 675 | -91.3 | 504990 | 416 | -97.6 | 504990 | 585 | -103.6 | 504990 | 846 |
| MR_1774414878_6EE2AADA | 504990 | 675 | -89.5 | 504990 | 416 | -98.9 | 504990 | 585 | -101.9 | 504990 | 846 |
| MR_1774414878_02FC4135 | 504990 | 675 | -92.9 | 504990 | 416 | -101.4 | 504990 | 585 | -102.1 | 504990 | 846 |
| MR_1774414878_3FA27C3D | 504990 | 675 | -91.1 | 504990 | 416 | -98.4 | 504990 | 585 | -102.1 | 504990 | 846 |
| MR_1774414878_74E6D08F | 504990 | 675 | -92.3 | 504990 | 416 | -100.6 | 504990 | 585 | -103.7 | 504990 | 846 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 122: `468157b8-d11...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `468157b8-d113-4f89-b834-3b424b5f02dc` |
| Tag | **multiple-answer** |
| 정답 | **C11|C12** |
| C11 의미 | Adjust the azimuth of 3267521_2 by 42 degrees |
| C12 의미 | Increase transmission power for 3267521_2 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[122] topology](images/train_0122.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3216022_1 by 2 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease transmission power for 3267521_2
- `C4`: Increase A3 Offset threshold for 3267521_2
- `C5`: Adjust the azimuth of 3216022_1 by 6 degrees
- `C6`: Increase transmission power for 3216022_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267521_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216022_1
- `C9`: Add neighbor relationship between 3211557_4 and 3216022_1
- `C10`: Press down the tilt angle  of 3216022_1 by 2 degrees
- `C11`: Adjust the azimuth of 3267521_2 by 42 degrees **← 정답**
- `C12`: Increase transmission power for 3267521_2 **← 정답**
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216022_1
- `C14`: Decrease A3 Offset threshold for 3267521_2
- `C15`: Decrease transmission power for 3216022_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267521_2
- `C17`: Check test server and transmission issues
- `C18`: Lift the tilt angle of 3267521_2 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3216022_1
- `C20`: Decrease A3 Offset threshold for 3216022_1
- `C21`: Press down the tilt angle of 3267521_2 by 10 degrees
- `C22`: Add neighbor relationship between 3267521_2 and 3216022_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.132 | MS1 | 121.4656645195 | 31.1446191006 | 634 | 504990 | -92.13 | 14.12 | 365.64 | 0.08 | 2.82 | 1591 |
| 2024-09-20 22:21:32.738 | MS1 | 121.4656704969 | 31.1446230213 | 634 | 504990 | -88.60 | 13.66 | 545.75 | 0.06 | 2.39 | 1592 |
| 2024-09-20 22:21:33.152 | MS1 | 121.4656778873 | 31.1446200037 | 634 | 504990 | -85.79 | 16.98 | 470.11 | 0.02 | 2.73 | 1588 |
| 2024-09-20 22:21:34.616 | MS1 | 121.4656610072 | 31.1446300259 | 634 | 504990 | -104.06 | -0.28 | 36.96 | 0.20 | 1.33 | 1576 |
| 2024-09-20 22:21:35.432 | MS1 | 121.4656598648 | 31.1446229245 | 634 | 504990 | -109.94 | 0.03 | 81.29 | 0.06 | 1.29 | 1571 |
| 2024-09-20 22:21:36.481 | MS1 | 121.4656730946 | 31.1446287878 | 634 | 504990 | -102.56 | -1.97 | 63.26 | 0.08 | 1.49 | 1573 |
| 2024-09-20 22:21:37.760 | MS1 | 121.4656773324 | 31.1446300050 | 634 | 504990 | -107.27 | -0.12 | 24.41 | 0.07 | 1.28 | 1560 |
| 2024-09-20 22:21:38.568 | MS1 | 121.4656724986 | 31.1446204458 | 634 | 504990 | -107.98 | 1.43 | 69.43 | 0.14 | 1.37 | 1580 |
| 2024-09-20 22:21:39.272 | MS1 | 121.4656602083 | 31.1446200687 | 634 | 504990 | -103.30 | -1.27 | 32.08 | 0.03 | 1.06 | 1599 |
| 2024-09-20 22:21:40.331 | MS1 | 121.4656763679 | 31.1446346190 | 634 | 504990 | -93.30 | 16.22 | 333.75 | 0.08 | 2.22 | 1590 |
| 2024-09-20 22:21:41.168 | MS1 | 121.4656717954 | 31.1446257187 | 634 | 504990 | -93.01 | 13.27 | 502.83 | 0.02 | 2.48 | 1593 |
| 2024-09-20 22:21:42.461 | MS1 | 121.4656709519 | 31.1446231780 | 634 | 504990 | -92.46 | 15.58 | 335.08 | 0.09 | 2.78 | 1560 |

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
| 3211557 | 4 | 121.4688514619 | 31.1492487127 | 336 | 2 | 3 | 42.8 | TDD | 41 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3216022 | 1 | 121.4641619379 | 31.1549671203 | 179 | 0 | 0 | 49.3 | TDD | 329 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3225465 | 3 | 121.4672850197 | 31.1442287033 | 249 | 0 | 3 | 16.2 | TDD | 971 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3267521 | 2 | 121.4748919933 | 31.1473795814 | 209 | 7 | 11 | 46.6 | TDD | 634 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.457 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.472 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.607 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.607 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.829 | NREventA2 | measId:1;ServCellPCI:144;Se... |
| 2024-09-20 22:21:34.974 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216022 | 1 | 13.0867 | 18.6217 | -117.4218 | 6.0574 | 94.6014 | 0.0067 | 0.0085 |
| 2024_09_20 22:00 | 3267521 | 2 | 16.1285 | 6.1948 | -114.3455 | 12.2934 | 115.2546 | 0.1262 | 0.0048 |
| 2024_09_20 22:00 | 3225465 | 3 | 16.3836 | 15.8304 | -116.3126 | 10.5438 | 142.1319 | 0.0190 | 0.0196 |
| 2024_09_20 22:00 | 3211557 | 4 | 14.2311 | 5.1842 | -114.9897 | 16.2830 | 182.3780 | 0.0085 | 0.0112 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415419_4CFBDB93 | 504990 | 634 | -103.6 | 504990 | 329 | -109.6 | 504990 | 41 | -114.2 | 504990 | 971 |
| MR_1774415419_8BE7AF97 | 504990 | 634 | -102.8 | 504990 | 329 | -112.0 | 504990 | 41 | -113.3 | 504990 | 971 |
| MR_1774415419_39A579B6 | 504990 | 634 | -103.8 | 504990 | 329 | -109.3 | 504990 | 41 | -113.7 | 504990 | 971 |
| MR_1774415419_EC8B36DB | 504990 | 634 | -105.5 | 504990 | 329 | -111.1 | 504990 | 41 | -113.1 | 504990 | 971 |
| MR_1774415419_F4845C60 | 504990 | 634 | -104.5 | 504990 | 329 | -109.9 | 504990 | 41 | -114.3 | 504990 | 971 |
| MR_1774415419_BCD35906 | 504990 | 634 | -105.6 | 504990 | 329 | -110.8 | 504990 | 41 | -112.7 | 504990 | 971 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 123: `056f3d8d-b11...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `056f3d8d-b111-4118-9c27-c6b432bd13d7` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246071_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[123] topology](images/train_0123.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246071_6 **← 정답**
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246071_6
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255766_1
- `C4`: Increase transmission power for 3255766_1
- `C5`: Adjust the azimuth of 3246071_6 by 22 degrees
- `C6`: Lift the tilt angle  of 3255766_1 by 5 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255766_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Press down the tilt angle of 3246071_6 by 2 degrees
- `C10`: Press down the tilt angle  of 3255766_1 by 5 degrees
- `C11`: Adjust the azimuth of 3255766_1 by 26 degrees
- `C12`: Add neighbor relationship between 3246071_6 and 3255766_1
- `C13`: Lift the tilt angle of 3246071_6 by 2 degrees
- `C14`: Decrease A3 Offset threshold for 3246071_6
- `C15`: Add neighbor relationship between 3262209_12 and 3255766_1
- `C16`: Decrease transmission power for 3255766_1
- `C17`: Increase A3 Offset threshold for 3255766_1
- `C18`: Decrease A3 Offset threshold for 3255766_1
- `C19`: Check test server and transmission issues
- `C20`: Decrease transmission power for 3246071_6
- `C21`: Increase transmission power for 3246071_6
- `C22`: Increase A3 Offset threshold for 3246071_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.221 | MS1 | 121.4656654758 | 31.1446267935 | 886 | 504990 | -95.93 | 10.28 | 398.68 | 0.10 | 2.79 | 1562 |
| 2024-09-20 22:21:32.375 | MS1 | 121.4656650441 | 31.1446192666 | 309 | 504990 | -94.75 | 10.84 | 427.49 | 0.03 | 2.84 | 1584 |
| 2024-09-20 22:21:33.839 | MS1 | 121.4656597482 | 31.1446285399 | 357 | 504990 | -94.17 | 12.69 | 403.01 | 0.06 | 2.55 | 1570 |
| 2024-09-20 22:21:34.365 | MS1 | 121.4656728328 | 31.1446202500 | 312 | 152650 | -91.76 | 4.54 | 71.52 | 0.12 | 1.80 | 1000 |
| 2024-09-20 22:21:35.223 | MS1 | 121.4656651745 | 31.1446184539 | 423 | 152650 | -87.08 | 2.61 | 80.65 | 0.09 | 1.91 | 960 |
| 2024-09-20 22:21:36.743 | MS1 | 121.4656741409 | 31.1446321144 | 697 | 152650 | -95.34 | 6.72 | 60.46 | 0.02 | 1.94 | 929 |
| 2024-09-20 22:21:37.146 | MS1 | 121.4656633190 | 31.1446266852 | 745 | 152650 | -91.67 | 7.87 | 94.66 | 0.12 | 1.56 | 919 |
| 2024-09-20 22:21:38.334 | MS1 | 121.4656615256 | 31.1446301488 | 312 | 152650 | -94.90 | 5.07 | 56.83 | 0.05 | 1.85 | 911 |
| 2024-09-20 22:21:39.276 | MS1 | 121.4656640661 | 31.1446260798 | 423 | 152650 | -88.36 | 4.62 | 86.80 | 0.08 | 1.69 | 908 |
| 2024-09-20 22:21:40.489 | MS1 | 121.4656622957 | 31.1446186674 | 697 | 152650 | -95.38 | 4.06 | 54.55 | 0.00 | 2.60 | 1571 |
| 2024-09-20 22:21:41.865 | MS1 | 121.4656714740 | 31.1446324999 | 745 | 152650 | -93.31 | 5.87 | 71.11 | 0.15 | 2.41 | 1569 |
| 2024-09-20 22:21:42.881 | MS1 | 121.4656731757 | 31.1446359074 | 312 | 152650 | -90.38 | 3.70 | 53.80 | 0.00 | 2.40 | 1588 |

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
| 3218529 | 8 | 121.4695172185 | 31.1557244671 | 272 | 10 | 1 | 24.8 | FDD | 423 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3230962 | 10 | 121.4653489167 | 31.1442699490 | 9 | 8 | 10 | 17.6 | FDD | 235 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3239714 | 3 | 121.4671370320 | 31.1450340253 | 74 | 2 | 2 | 2.6 | TDD | 357 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3241363 | 2 | 121.4663598003 | 31.1495333665 | 204 | 6 | 0 | 28.2 | TDD | 503 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3242492 | 13 | 121.4677802986 | 31.1467536567 | 131 | 14 | 8 | 4.9 | FDD | 63 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3246071 | 6 | 121.4755500334 | 31.1442021049 | 251 | 1 | 6 | 24.0 | TDD | 886 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3248877 | 7 | 121.4668944632 | 31.1465087723 | 112 | 5 | 7 | 12.3 | FDD | 739 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3248960 | 5 | 121.4710954615 | 31.1528619999 | 293 | 10 | 12 | 24.9 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3255766 | 1 | 121.4689131634 | 31.1544651253 | 222 | 4 | 6 | 22.0 | TDD | 419 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3258134 | 9 | 121.4716378483 | 31.1496004988 | 288 | 9 | 8 | 4.2 | FDD | 745 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3262209 | 12 | 121.4673548030 | 31.1534090132 | 211 | 2 | 5 | 13.4 | FDD | 697 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3266960 | 4 | 121.4706311897 | 31.1551716599 | 198 | 10 | 11 | 16.4 | TDD | 981 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3275447 | 11 | 121.4680578839 | 31.1559065104 | 88 | 5 | 10 | 26.7 | FDD | 312 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |

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
| 2024-09-20 22:21:31.010 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.026 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.165 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.165 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.843 | NREventA2 | measId:1;ServCellPCI:33;Ser... |
| 2024-09-20 22:21:34.979 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.200 | NREventA5 | measId:3;ServCellPCI:33;Ser... |
| 2024-09-20 22:21:35.235 | NRHandoverAttempt | SourcePCI:33;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.263 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.278 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.412 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.412 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255766 | 1 | 13.2872 | 19.8973 | -114.0490 | 13.2536 | 86.9968 | 0.0014 | 0.0115 |
| 2024_09_20 22:00 | 3241363 | 2 | 5.8541 | 13.9475 | -116.3873 | 6.7546 | 98.3182 | 0.0183 | 0.0157 |
| 2024_09_20 22:00 | 3239714 | 3 | 10.6235 | 8.8936 | -114.8309 | 16.1281 | 157.9624 | 0.0191 | 0.0081 |
| 2024_09_20 22:00 | 3266960 | 4 | 6.2381 | 14.9508 | -117.5621 | 9.9231 | 149.4922 | 0.0077 | 0.0051 |
| 2024_09_20 22:00 | 3248960 | 5 | 11.1774 | 19.6291 | -116.8422 | 8.0966 | 104.2953 | 0.0103 | 0.0078 |
| 2024_09_20 22:00 | 3246071 | 6 | 6.4627 | 18.0840 | -117.3639 | 11.7105 | 135.0587 | 0.0007 | 0.0139 |
| 2024_09_20 22:00 | 3248877 | 7 | 5.6806 | 7.7783 | -115.8179 | 3.4613 | 49.1368 | 0.0135 | 0.0074 |
| 2024_09_20 22:00 | 3218529 | 8 | 13.6615 | 17.1444 | -115.4113 | 3.7040 | 37.2253 | 0.0098 | 0.0155 |
| 2024_09_20 22:00 | 3258134 | 9 | 19.4343 | 11.6546 | -114.2114 | 4.9993 | 21.0803 | 0.0146 | 0.0125 |
| 2024_09_20 22:00 | 3230962 | 10 | 5.7472 | 7.1433 | -117.6034 | 4.8611 | 44.9854 | 0.0090 | 0.0186 |
| 2024_09_20 22:00 | 3275447 | 11 | 13.9737 | 8.4683 | -114.7406 | 3.9630 | 53.4496 | 0.0031 | 0.0062 |
| 2024_09_20 22:00 | 3262209 | 12 | 7.2309 | 13.1185 | -114.3322 | 3.6946 | 43.5174 | 0.0128 | 0.0078 |
| 2024_09_20 22:00 | 3242492 | 13 | 7.3581 | 13.7991 | -117.9264 | 4.9712 | 47.2945 | 0.0037 | 0.0024 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415709_A08EA086 | 152650 | 312 | -90.4 | 152650 | 739 | -98.9 | 152650 | 235 | -101.1 | 152650 | 63 |
| MR_1774415709_A47B9F6D | 152650 | 312 | -91.2 | 152650 | 739 | -96.9 | 152650 | 235 | -101.4 | 152650 | 63 |
| MR_1774415709_43EA3337 | 504990 | 357 | -95.2 | 504990 | 419 | -91.3 | 504990 | 981 | -95.2 | 504990 | 503 |
| MR_1774415709_D6E6CE2C | 504990 | 357 | -94.5 | 504990 | 419 | -92.8 | 504990 | 981 | -96.0 | 504990 | 503 |
| MR_1774415709_C9A0D13B | 152650 | 312 | -90.8 | 152650 | 739 | -100.1 | 152650 | 235 | -99.8 | 152650 | 63 |
| MR_1774415709_DB677B8E | 152650 | 312 | -93.7 | 152650 | 739 | -99.5 | 152650 | 235 | -102.7 | 152650 | 63 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 124: `dfa8e9f8-6fa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dfa8e9f8-6fa8-437b-bad3-d193e2a24ffe` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Add neighbor relationship between 3243161_1 and 3220388_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[124] topology](images/train_0124.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243161_1
- `C2`: Increase transmission power for 3220388_3
- `C3`: Lift the tilt angle  of 3220388_3 by 3 degrees
- `C4`: Increase transmission power for 3243161_1
- `C5`: Add neighbor relationship between 3237195_4 and 3220388_3
- `C6`: Decrease A3 Offset threshold for 3243161_1
- `C7`: Adjust the azimuth of 3220388_3 by 39 degrees
- `C8`: Adjust the azimuth of 3243161_1 by 50 degrees
- `C9`: Add neighbor relationship between 3243161_1 and 3220388_3 **← 정답**
- `C10`: Decrease A3 Offset threshold for 3220388_3
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Check test server and transmission issues
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243161_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220388_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220388_3
- `C16`: Decrease transmission power for 3220388_3
- `C17`: Increase A3 Offset threshold for 3243161_1
- `C18`: Press down the tilt angle of 3243161_1 by 10 degrees
- `C19`: Press down the tilt angle  of 3220388_3 by 3 degrees
- `C20`: Lift the tilt angle of 3243161_1 by 10 degrees
- `C21`: Increase A3 Offset threshold for 3220388_3
- `C22`: Decrease transmission power for 3243161_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.287 | MS1 | 121.4656603533 | 31.1446346588 | 464 | 504990 | -76.29 | 16.09 | 591.88 | 0.10 | 2.36 | 1568 |
| 2024-09-20 22:21:32.754 | MS1 | 121.4656729156 | 31.1446379855 | 464 | 504990 | -78.43 | 16.87 | 443.18 | 0.07 | 2.22 | 1570 |
| 2024-09-20 22:21:33.695 | MS1 | 121.4656736542 | 31.1446228860 | 464 | 504990 | -81.49 | 17.35 | 419.04 | 0.11 | 2.99 | 1584 |
| 2024-09-20 22:21:34.222 | MS1 | 121.4656623520 | 31.1446189581 | 464 | 504990 | -88.17 | -3.91 | 52.61 | 0.18 | 1.41 | 1580 |
| 2024-09-20 22:21:35.347 | MS1 | 121.4656665458 | 31.1446313282 | 464 | 504990 | -90.01 | -0.70 | 70.04 | 0.09 | 1.19 | 1579 |
| 2024-09-20 22:21:36.665 | MS1 | 121.4656600953 | 31.1446213125 | 464 | 504990 | -91.48 | -0.80 | 41.55 | 0.05 | 1.30 | 1583 |
| 2024-09-20 22:21:37.221 | MS1 | 121.4656639012 | 31.1446363662 | 464 | 504990 | -85.48 | -3.04 | 43.36 | 0.09 | 1.10 | 1570 |
| 2024-09-20 22:21:38.971 | MS1 | 121.4656694999 | 31.1446316102 | 464 | 504990 | -80.41 | 13.56 | 498.91 | 0.08 | 1.18 | 1582 |
| 2024-09-20 22:21:39.753 | MS1 | 121.4656602207 | 31.1446186317 | 464 | 504990 | -80.85 | 17.67 | 521.47 | 0.10 | 1.16 | 1593 |
| 2024-09-20 22:21:40.820 | MS1 | 121.4656584395 | 31.1446189298 | 464 | 504990 | -82.85 | 17.34 | 316.77 | 0.19 | 2.39 | 1588 |
| 2024-09-20 22:21:41.843 | MS1 | 121.4656661284 | 31.1446198281 | 464 | 504990 | -81.76 | 17.33 | 303.70 | 0.08 | 2.58 | 1578 |
| 2024-09-20 22:21:42.166 | MS1 | 121.4656588170 | 31.1446327272 | 464 | 504990 | -82.34 | 16.26 | 370.19 | 0.13 | 2.72 | 1572 |

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
| 3220388 | 3 | 121.4640627323 | 31.1520759440 | 209 | 1 | 10 | 22.4 | TDD | 556 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3237195 | 4 | 121.4672610027 | 31.1516363179 | 332 | 1 | 8 | 24.3 | TDD | 656 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3243161 | 1 | 121.4707720975 | 31.1524517164 | 74 | 12 | 7 | 40.9 | TDD | 464 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3266569 | 2 | 121.4680492683 | 31.1527618053 | 132 | 7 | 12 | 24.8 | TDD | 819 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.234 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.335 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.335 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.026 | NREventA3 | measId:2;ServCellPCI:597;Se... |
| 2024-09-20 22:21:36.026 | NREventA3 | measId:2;ServCellPCI:597;Se... |
| 2024-09-20 22:21:37.026 | NREventA3 | measId:2;ServCellPCI:597;Se... |
| 2024-09-20 22:21:39.526 | NRRRCReestablishAttempt | PCI:597 |
| 2024-09-20 22:21:39.540 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.553 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.678 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.678 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243161 | 1 | 14.6325 | 6.2981 | -115.2089 | 9.6851 | 176.4979 | 0.0090 | 0.1005 |
| 2024_09_20 22:00 | 3266569 | 2 | 8.7935 | 7.2678 | -114.5083 | 8.3228 | 156.0131 | 0.0046 | 0.0124 |
| 2024_09_20 22:00 | 3220388 | 3 | 19.3457 | 18.4983 | -117.4848 | 13.6455 | 143.4710 | 0.0061 | 0.0005 |
| 2024_09_20 22:00 | 3237195 | 4 | 14.8391 | 6.4371 | -116.7144 | 9.7127 | 100.3970 | 0.0030 | 0.0140 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416531_C034CB21 | 504990 | 556 | -82.7 | 504990 | 464 | -87.7 | 504990 | 656 | -89.2 | 504990 | 819 |
| MR_1774416531_DF73218F | 504990 | 556 | -84.8 | 504990 | 464 | -88.9 | 504990 | 656 | -88.3 | 504990 | 819 |
| MR_1774416531_88720E96 | 504990 | 464 | -89.5 | 504990 | 556 | -84.5 | 504990 | 656 | -89.9 | 504990 | 819 |
| MR_1774416531_9C00C4C8 | 504990 | 464 | -86.6 | 504990 | 556 | -82.6 | 504990 | 656 | -87.8 | 504990 | 819 |
| MR_1774416531_26D54B4C | 504990 | 464 | -87.0 | 504990 | 556 | -82.4 | 504990 | 656 | -89.8 | 504990 | 819 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 125: `86de99d1-e06...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `86de99d1-e06b-4f2a-bd25-d88cb5aaf2f0` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Lift the tilt angle  of 3243283_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[125] topology](images/train_0125.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3244242_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase A3 Offset threshold for 3238221_1
- `C4`: Check test server and transmission issues
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244242_2
- `C6`: Lift the tilt angle  of 3243283_4 by 10 degrees **← 정답**
- `C7`: Decrease transmission power for 3244242_2
- `C8`: Press down the tilt angle of 3238221_1 by 2 degrees
- `C9`: Adjust the azimuth of 3243283_4 by 50 degrees
- `C10`: Adjust the azimuth of 3238221_1 by 5 degrees
- `C11`: Increase A3 Offset threshold for 3244242_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244242_2
- `C13`: Add neighbor relationship between 3238221_1 and 3244242_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238221_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238221_1
- `C16`: Press down the tilt angle  of 3243283_4 by 10 degrees
- `C17`: Decrease A3 Offset threshold for 3244242_2
- `C18`: Lift the tilt angle of 3238221_1 by 2 degrees
- `C19`: Add neighbor relationship between 3243283_4 and 3244242_2
- `C20`: Increase transmission power for 3238221_1
- `C21`: Decrease A3 Offset threshold for 3238221_1
- `C22`: Decrease transmission power for 3238221_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.597 | MS1 | 121.4656670622 | 31.1446320412 | 58 | 504990 | -89.57 | 16.66 | 549.88 | 0.16 | 2.54 | 1583 |
| 2024-09-20 22:21:32.636 | MS1 | 121.4656661244 | 31.1446378971 | 58 | 504990 | -89.60 | 13.99 | 467.65 | 0.05 | 2.89 | 1577 |
| 2024-09-20 22:21:33.581 | MS1 | 121.4656663406 | 31.1446296363 | 58 | 504990 | -86.14 | 12.39 | 376.60 | 0.08 | 2.04 | 1583 |
| 2024-09-20 22:21:34.510 | MS1 | 121.4656676636 | 31.1446186063 | 58 | 504990 | -88.82 | 16.92 | 84.66 | 0.13 | 2.17 | 1586 |
| 2024-09-20 22:21:35.140 | MS1 | 121.4656660060 | 31.1446329575 | 58 | 504990 | -89.06 | 13.75 | 66.77 | 0.18 | 2.45 | 1596 |
| 2024-09-20 22:21:36.458 | MS1 | 121.4656706448 | 31.1446193022 | 58 | 504990 | -89.72 | 13.23 | 78.76 | 0.04 | 2.98 | 1567 |
| 2024-09-20 22:21:37.602 | MS1 | 121.4656739960 | 31.1446285050 | 58 | 504990 | -93.72 | 10.49 | 64.38 | 0.07 | 2.89 | 1577 |
| 2024-09-20 22:21:38.166 | MS1 | 121.4656605090 | 31.1446257261 | 58 | 504990 | -93.55 | 8.22 | 92.12 | 0.12 | 2.07 | 1600 |
| 2024-09-20 22:21:39.182 | MS1 | 121.4656737377 | 31.1446308735 | 58 | 504990 | -91.07 | 10.72 | 79.59 | 0.05 | 2.55 | 1568 |
| 2024-09-20 22:21:40.888 | MS1 | 121.4656598244 | 31.1446268843 | 58 | 504990 | -90.01 | 11.59 | 549.09 | 0.01 | 2.49 | 1578 |
| 2024-09-20 22:21:41.743 | MS1 | 121.4656625375 | 31.1446330811 | 58 | 504990 | -92.33 | 12.02 | 512.85 | 0.15 | 2.70 | 1560 |
| 2024-09-20 22:21:42.638 | MS1 | 121.4656772550 | 31.1446263870 | 58 | 504990 | -91.21 | 11.19 | 441.48 | 0.11 | 2.75 | 1579 |

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
| 3235187 | 3 | 121.4730999434 | 31.1452258944 | 38 | 12 | 9 | 16.9 | TDD | 444 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3238221 | 1 | 121.4741607546 | 31.1524913196 | 218 | 1 | 3 | 25.5 | TDD | 58 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3243283 | 4 | 121.4643192107 | 31.1535726191 | 49 | 12 | 8 | 28.0 | TDD | 874 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3244242 | 2 | 121.4655460393 | 31.1491079100 | 7 | 14 | 11 | 25.5 | TDD | 323 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.055 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.076 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.181 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.181 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.902 | NREventA3 | measId:2;ServCellPCI:314;Se... |
| 2024-09-20 22:21:38.142 | NRHandoverAttempt | SourcePCI:314;SourceNR-ARFC... |
| 2024-09-20 22:21:38.179 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.191 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.293 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.293 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238221 | 1 | 93.0303 | 86.6937 | -114.3400 | 17.3494 | 110.4785 | 0.0200 | 0.0141 |
| 2024_09_20 22:00 | 3244242 | 2 | 10.2036 | 18.3939 | -115.7061 | 15.6150 | 144.6692 | 0.0105 | 0.0117 |
| 2024_09_20 22:00 | 3235187 | 3 | 19.2163 | 14.1328 | -115.4828 | 13.0388 | 109.0381 | 0.0095 | 0.0083 |
| 2024_09_20 22:00 | 3243283 | 4 | 15.8833 | 6.3245 | -114.9208 | 9.0998 | 143.5305 | 0.0155 | 0.0010 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412478_344AB20C | 504990 | 58 | -89.9 | 504990 | 323 | -91.6 | 504990 | 874 | -96.4 | 504990 | 444 |
| MR_1774412478_EAEEFEC2 | 504990 | 58 | -90.7 | 504990 | 323 | -92.1 | 504990 | 874 | -95.4 | 504990 | 444 |
| MR_1774412478_62D8FA63 | 504990 | 58 | -87.8 | 504990 | 323 | -93.1 | 504990 | 874 | -96.8 | 504990 | 444 |
| MR_1774412478_8C65B239 | 504990 | 58 | -90.2 | 504990 | 323 | -92.5 | 504990 | 874 | -97.7 | 504990 | 444 |
| MR_1774412478_88CCBFA2 | 504990 | 58 | -88.4 | 504990 | 323 | -93.0 | 504990 | 874 | -97.9 | 504990 | 444 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 126: `ca034a30-c57...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ca034a30-c573-4e02-a53a-9685474938ab` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[126] topology](images/train_0126.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3256438_3
- `C2`: Press down the tilt angle of 3257016_1 by 2 degrees
- `C3`: Add neighbor relationship between 3232608_2 and 3256438_3
- `C4`: Increase transmission power for 3257016_1
- `C5`: Adjust the azimuth of 3257016_1 by 50 degrees
- `C6`: Check test server and transmission issues
- `C7`: Adjust the azimuth of 3256438_3 by 3 degrees
- `C8`: Add neighbor relationship between 3257016_1 and 3256438_3
- `C9`: Lift the tilt angle  of 3256438_3 by 8 degrees
- `C10`: Insufficient data; more data is needed for judgment. **← 정답**
- `C11`: Increase A3 Offset threshold for 3256438_3
- `C12`: Press down the tilt angle  of 3256438_3 by 8 degrees
- `C13`: Increase transmission power for 3256438_3
- `C14`: Increase A3 Offset threshold for 3257016_1
- `C15`: Decrease transmission power for 3256438_3
- `C16`: Lift the tilt angle of 3257016_1 by 2 degrees
- `C17`: Decrease transmission power for 3257016_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256438_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256438_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257016_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257016_1
- `C22`: Decrease A3 Offset threshold for 3257016_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.549 | MS1 | 121.4656677331 | 31.1446352372 | 144 | 504990 | -91.33 | 13.00 | 354.30 | 0.08 | 2.17 | 1593 |
| 2024-09-20 22:21:32.533 | MS1 | 121.4656701144 | 31.1446209450 | 144 | 504990 | -85.41 | 13.55 | 534.07 | 0.05 | 2.54 | 1591 |
| 2024-09-20 22:21:33.871 | MS1 | 121.4656659490 | 31.1446316813 | 144 | 504990 | -91.40 | 15.15 | 366.06 | 0.09 | 2.44 | 1577 |
| 2024-09-20 22:21:34.943 | MS1 | 121.4656680240 | 31.1446187931 | 144 | 504990 | -88.00 | 17.72 | 100.35 | 0.14 | 2.40 | 1577 |
| 2024-09-20 22:21:35.177 | MS1 | 121.4656747633 | 31.1446286417 | 144 | 504990 | -85.70 | 13.18 | 82.26 | 0.16 | 2.89 | 1572 |
| 2024-09-20 22:21:36.839 | MS1 | 121.4656670335 | 31.1446343950 | 144 | 504990 | -90.66 | 17.73 | 80.43 | 0.02 | 2.30 | 1565 |
| 2024-09-20 22:21:37.350 | MS1 | 121.4656658918 | 31.1446250245 | 144 | 504990 | -92.41 | 7.84 | 64.77 | 0.11 | 2.39 | 1599 |
| 2024-09-20 22:21:38.117 | MS1 | 121.4656744191 | 31.1446288007 | 144 | 504990 | -93.12 | 10.24 | 86.67 | 0.13 | 2.22 | 1594 |
| 2024-09-20 22:21:39.251 | MS1 | 121.4656738076 | 31.1446364989 | 144 | 504990 | -93.01 | 11.16 | 57.66 | 0.10 | 2.16 | 1584 |
| 2024-09-20 22:21:40.812 | MS1 | 121.4656649746 | 31.1446248832 | 144 | 504990 | -92.09 | 10.99 | 481.80 | 0.03 | 2.15 | 1583 |
| 2024-09-20 22:21:41.723 | MS1 | 121.4656650507 | 31.1446345792 | 144 | 504990 | -89.34 | 10.72 | 558.28 | 0.08 | 2.18 | 1565 |
| 2024-09-20 22:21:42.822 | MS1 | 121.4656628397 | 31.1446276436 | 144 | 504990 | -90.19 | 7.36 | 312.86 | 0.05 | 2.74 | 1594 |

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
| 3228732 | 4 | 121.4676695736 | 31.1469059656 | 274 | 15 | 6 | 30.7 | TDD | 533 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3232608 | 2 | 121.4752412206 | 31.1458346451 | 338 | 15 | 6 | 43.2 | TDD | 139 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3256438 | 3 | 121.4690643446 | 31.1530827160 | 202 | 5 | 6 | 45.0 | TDD | 348 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3257016 | 1 | 121.4700261945 | 31.1488239619 | 31 | 0 | 3 | 22.2 | TDD | 144 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.473 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.492 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.599 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.599 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.342 | NREventA3 | measId:2;ServCellPCI:545;Se... |
| 2024-09-20 22:21:38.582 | NRHandoverAttempt | SourcePCI:545;SourceNR-ARFC... |
| 2024-09-20 22:21:38.614 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.627 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.738 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.738 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3257016 | 1 | 86.9543 | 78.9073 | -117.9644 | 8.4830 | 174.5202 | 0.0109 | 0.0099 |
| 2024_09_19 22:00 | 3232608 | 2 | 82.9014 | 94.6639 | -114.4371 | 5.1511 | 173.7734 | 0.0032 | 0.0099 |
| 2024_09_19 22:00 | 3256438 | 3 | 88.3421 | 87.4538 | -114.5644 | 6.2063 | 124.0808 | 0.0195 | 0.0144 |
| 2024_09_19 22:00 | 3228732 | 4 | 93.9581 | 80.9129 | -114.6185 | 8.9902 | 105.7969 | 0.0198 | 0.0073 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416333_FBA9DF3B | 504990 | 144 | -86.1 | 504990 | 348 | -90.5 | 504990 | 139 | -99.5 | 504990 | 533 |
| MR_1774416333_18A8885E | 504990 | 144 | -84.7 | 504990 | 348 | -90.2 | 504990 | 139 | -97.7 | 504990 | 533 |
| MR_1774416333_6DE1577E | 504990 | 144 | -84.0 | 504990 | 348 | -86.9 | 504990 | 139 | -100.0 | 504990 | 533 |
| MR_1774416333_851B6AB2 | 504990 | 144 | -87.3 | 504990 | 348 | -87.0 | 504990 | 139 | -98.6 | 504990 | 533 |
| MR_1774416333_DE888AA4 | 504990 | 144 | -84.4 | 504990 | 348 | -88.4 | 504990 | 139 | -99.5 | 504990 | 533 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 127: `129e51ff-45f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `129e51ff-45f3-4de9-b42d-cd62e5314397` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Lift the tilt angle  of 3242405_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[127] topology](images/train_0127.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3210668_3 by 1 degrees
- `C2`: Increase A3 Offset threshold for 3210668_3
- `C3`: Add neighbor relationship between 3242405_4 and 3220050_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220050_1
- `C5`: Increase A3 Offset threshold for 3220050_1
- `C6`: Press down the tilt angle of 3210668_3 by 1 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210668_3
- `C8`: Decrease A3 Offset threshold for 3220050_1
- `C9`: Increase transmission power for 3210668_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210668_3
- `C11`: Decrease transmission power for 3210668_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220050_1
- `C13`: Press down the tilt angle  of 3242405_4 by 10 degrees
- `C14`: Adjust the azimuth of 3242405_4 by 50 degrees
- `C15`: Add neighbor relationship between 3210668_3 and 3220050_1
- `C16`: Lift the tilt angle  of 3242405_4 by 10 degrees **← 정답**
- `C17`: Check test server and transmission issues
- `C18`: Decrease A3 Offset threshold for 3210668_3
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Adjust the azimuth of 3210668_3 by 39 degrees
- `C21`: Decrease transmission power for 3220050_1
- `C22`: Increase transmission power for 3220050_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.715 | MS1 | 121.4656727821 | 31.1446310014 | 606 | 504990 | -89.65 | 13.30 | 587.43 | 0.06 | 2.26 | 1597 |
| 2024-09-20 22:21:32.367 | MS1 | 121.4656679185 | 31.1446303960 | 606 | 504990 | -89.80 | 13.53 | 595.32 | 0.01 | 2.47 | 1582 |
| 2024-09-20 22:21:33.545 | MS1 | 121.4656607560 | 31.1446320388 | 606 | 504990 | -88.75 | 13.23 | 436.30 | 0.09 | 2.46 | 1594 |
| 2024-09-20 22:21:34.297 | MS1 | 121.4656616113 | 31.1446297696 | 606 | 504990 | -87.27 | 14.82 | 55.87 | 0.03 | 2.12 | 1570 |
| 2024-09-20 22:21:35.399 | MS1 | 121.4656614086 | 31.1446294074 | 606 | 504990 | -86.37 | 15.24 | 82.31 | 0.20 | 2.28 | 1591 |
| 2024-09-20 22:21:36.824 | MS1 | 121.4656687578 | 31.1446351720 | 606 | 504990 | -90.28 | 17.65 | 83.65 | 0.08 | 2.10 | 1564 |
| 2024-09-20 22:21:37.639 | MS1 | 121.4656709462 | 31.1446198794 | 606 | 504990 | -92.71 | 9.86 | 68.99 | 0.06 | 2.26 | 1571 |
| 2024-09-20 22:21:38.528 | MS1 | 121.4656742841 | 31.1446246505 | 606 | 504990 | -93.10 | 9.02 | 94.90 | 0.13 | 2.92 | 1578 |
| 2024-09-20 22:21:39.762 | MS1 | 121.4656674972 | 31.1446348018 | 606 | 504990 | -93.53 | 10.85 | 73.32 | 0.07 | 2.11 | 1580 |
| 2024-09-20 22:21:40.467 | MS1 | 121.4656709701 | 31.1446336982 | 606 | 504990 | -89.40 | 9.02 | 488.19 | 0.06 | 2.37 | 1561 |
| 2024-09-20 22:21:41.208 | MS1 | 121.4656731505 | 31.1446221754 | 606 | 504990 | -92.20 | 7.21 | 324.66 | 0.03 | 2.93 | 1587 |
| 2024-09-20 22:21:42.606 | MS1 | 121.4656702877 | 31.1446368149 | 606 | 504990 | -89.71 | 8.84 | 421.60 | 0.14 | 2.22 | 1596 |

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
| 3210668 | 3 | 121.4744461831 | 31.1492462802 | 277 | 0 | 2 | 18.2 | TDD | 606 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3220050 | 1 | 121.4735927212 | 31.1475530763 | 180 | 15 | 10 | 34.2 | TDD | 753 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3237950 | 2 | 121.4661945273 | 31.1507510951 | 206 | 8 | 6 | 19.5 | TDD | 293 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3242405 | 4 | 121.4659670927 | 31.1510640706 | 44 | 4 | 0 | 25.7 | TDD | 941 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.443 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.460 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.590 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.590 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.319 | NREventA3 | measId:2;ServCellPCI:409;Se... |
| 2024-09-20 22:21:38.559 | NRHandoverAttempt | SourcePCI:409;SourceNR-ARFC... |
| 2024-09-20 22:21:38.605 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.617 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.726 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.726 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220050 | 1 | 12.7666 | 17.7999 | -115.4916 | 19.0883 | 133.3834 | 0.0184 | 0.0129 |
| 2024_09_20 22:00 | 3237950 | 2 | 7.2868 | 17.5921 | -116.2585 | 6.0002 | 182.8369 | 0.0012 | 0.0189 |
| 2024_09_20 22:00 | 3210668 | 3 | 79.3199 | 77.1737 | -117.3300 | 7.3130 | 108.6968 | 0.0179 | 0.0081 |
| 2024_09_20 22:00 | 3242405 | 4 | 15.4727 | 16.3292 | -115.6806 | 16.2623 | 179.0816 | 0.0138 | 0.0016 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413842_1522C31C | 504990 | 606 | -86.7 | 504990 | 753 | -86.8 | 504990 | 941 | -101.8 | 504990 | 293 |
| MR_1774413842_5E746CE6 | 504990 | 606 | -87.6 | 504990 | 753 | -86.7 | 504990 | 941 | -100.4 | 504990 | 293 |
| MR_1774413842_B4620D00 | 504990 | 606 | -87.7 | 504990 | 753 | -88.2 | 504990 | 941 | -100.6 | 504990 | 293 |
| MR_1774413842_6537789A | 504990 | 606 | -88.9 | 504990 | 753 | -87.7 | 504990 | 941 | -102.1 | 504990 | 293 |
| MR_1774413842_50F8C6BA | 504990 | 606 | -88.8 | 504990 | 753 | -87.0 | 504990 | 941 | -100.8 | 504990 | 293 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 128: `2d46c9b7-910...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2d46c9b7-9101-4815-b663-94a3a7fa94fb` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3279060_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[128] topology](images/train_0128.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279060_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227263_1
- `C3`: Lift the tilt angle  of 3227263_1 by 10 degrees
- `C4`: Decrease A3 Offset threshold for 3227263_1
- `C5`: Adjust the azimuth of 3227263_1 by 50 degrees
- `C6`: Lift the tilt angle of 3279060_4 by 4 degrees
- `C7`: Decrease A3 Offset threshold for 3279060_4
- `C8`: Increase A3 Offset threshold for 3279060_4
- `C9`: Decrease transmission power for 3279060_4
- `C10`: Press down the tilt angle  of 3227263_1 by 10 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227263_1
- `C13`: Adjust the azimuth of 3279060_4 by 34 degrees
- `C14`: Increase transmission power for 3227263_1
- `C15`: Increase A3 Offset threshold for 3227263_1
- `C16`: Add neighbor relationship between 3254240_2 and 3227263_1
- `C17`: Press down the tilt angle of 3279060_4 by 4 degrees
- `C18`: Check test server and transmission issues
- `C19`: Add neighbor relationship between 3279060_4 and 3227263_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279060_4 **← 정답**
- `C21`: Decrease transmission power for 3227263_1
- `C22`: Increase transmission power for 3279060_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.698 | MS1 | 121.4656690690 | 31.1446282291 | 582 | 504990 | -86.16 | 17.22 | 548.80 | 0.14 | 2.27 | 1566 |
| 2024-09-20 22:21:32.927 | MS1 | 121.4656760317 | 31.1446273393 | 582 | 504990 | -90.68 | 17.87 | 375.31 | 0.05 | 2.52 | 1581 |
| 2024-09-20 22:21:33.124 | MS1 | 121.4656742028 | 31.1446326766 | 582 | 504990 | -87.86 | 15.21 | 444.50 | 0.00 | 2.75 | 1576 |
| 2024-09-20 22:21:34.516 | MS1 | 121.4656683303 | 31.1446260321 | 582 | 504990 | -90.83 | 17.01 | 58.17 | 0.55 | 2.36 | 674 |
| 2024-09-20 22:21:35.717 | MS1 | 121.4656635220 | 31.1446297718 | 582 | 504990 | -88.82 | 13.26 | 74.84 | 0.67 | 3.00 | 591 |
| 2024-09-20 22:21:36.471 | MS1 | 121.4656642518 | 31.1446369752 | 582 | 504990 | -88.72 | 12.09 | 77.78 | 0.61 | 2.96 | 685 |
| 2024-09-20 22:21:37.824 | MS1 | 121.4656663993 | 31.1446293536 | 582 | 504990 | -91.67 | 8.06 | 91.98 | 0.57 | 2.92 | 560 |
| 2024-09-20 22:21:38.863 | MS1 | 121.4656584764 | 31.1446286235 | 582 | 504990 | -89.84 | 7.95 | 94.10 | 0.58 | 2.53 | 674 |
| 2024-09-20 22:21:39.639 | MS1 | 121.4656700959 | 31.1446323814 | 582 | 504990 | -93.42 | 9.77 | 87.54 | 0.62 | 2.06 | 687 |
| 2024-09-20 22:21:40.445 | MS1 | 121.4656740769 | 31.1446308029 | 582 | 504990 | -93.11 | 9.26 | 368.75 | 0.06 | 2.61 | 1578 |
| 2024-09-20 22:21:41.292 | MS1 | 121.4656618024 | 31.1446271317 | 582 | 504990 | -90.44 | 11.25 | 311.45 | 0.08 | 2.24 | 1590 |
| 2024-09-20 22:21:42.151 | MS1 | 121.4656627406 | 31.1446373181 | 582 | 504990 | -91.95 | 9.84 | 382.75 | 0.13 | 2.73 | 1565 |

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
| 3221774 | 3 | 121.4667973548 | 31.1455445050 | 281 | 3 | 2 | 45.6 | TDD | 492 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3227263 | 1 | 121.4658981093 | 31.1464534715 | 286 | 7 | 1 | 21.0 | TDD | 570 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3254240 | 2 | 121.4715003155 | 31.1539095011 | 241 | 12 | 9 | 22.7 | TDD | 708 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3279060 | 4 | 121.4747629735 | 31.1546272251 | 184 | 3 | 6 | 36.5 | TDD | 582 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.924 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.944 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.066 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.066 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.757 | NREventA3 | measId:2;ServCellPCI:306;Se... |
| 2024-09-20 22:21:37.997 | NRHandoverAttempt | SourcePCI:306;SourceNR-ARFC... |
| 2024-09-20 22:21:38.027 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.039 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.176 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.176 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227263 | 1 | 7.5215 | 10.3207 | -117.8708 | 8.3563 | 184.2638 | 0.0045 | 0.0023 |
| 2024_09_20 22:00 | 3254240 | 2 | 19.6701 | 11.5458 | -114.3666 | 17.3602 | 124.8561 | 0.0099 | 0.0098 |
| 2024_09_20 22:00 | 3221774 | 3 | 8.7366 | 7.3122 | -115.8915 | 5.4436 | 102.2707 | 0.0113 | 0.0169 |
| 2024_09_20 22:00 | 3279060 | 4 | 18.1896 | 9.9004 | -116.3010 | 11.2837 | 148.7934 | 0.0132 | 0.0101 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413689_C2D9CA1D | 504990 | 582 | -90.7 | 504990 | 570 | -96.5 | 504990 | 708 | -103.5 | 504990 | 492 |
| MR_1774413689_DD2A81B1 | 504990 | 582 | -90.5 | 504990 | 570 | -97.3 | 504990 | 708 | -103.6 | 504990 | 492 |
| MR_1774413689_8793E7F0 | 504990 | 582 | -90.6 | 504990 | 570 | -98.2 | 504990 | 708 | -105.9 | 504990 | 492 |
| MR_1774413689_1ECCA098 | 504990 | 582 | -91.6 | 504990 | 570 | -96.6 | 504990 | 708 | -104.9 | 504990 | 492 |
| MR_1774413689_C1006CE1 | 504990 | 582 | -92.5 | 504990 | 570 | -98.6 | 504990 | 708 | -103.4 | 504990 | 492 |
| MR_1774413689_C3D06D56 | 504990 | 582 | -90.5 | 504990 | 570 | -97.7 | 504990 | 708 | -106.1 | 504990 | 492 |
| MR_1774413689_E33A4391 | 504990 | 582 | -91.5 | 504990 | 570 | -97.6 | 504990 | 708 | -104.0 | 504990 | 492 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 129: `699572cb-cc8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `699572cb-cc82-4fe9-96e0-b53cde7d96c7` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Decrease A3 Offset threshold for 3235024_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[129] topology](images/train_0129.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3235024_4 **← 정답**
- `C2`: Check test server and transmission issues
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213393_3
- `C4`: Increase A3 Offset threshold for 3235024_4
- `C5`: Increase transmission power for 3213393_3
- `C6`: Adjust the azimuth of 3235024_4 by 0 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235024_4
- `C8`: Decrease transmission power for 3213393_3
- `C9`: Decrease transmission power for 3235024_4
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Adjust the azimuth of 3213393_3 by 50 degrees
- `C12`: Lift the tilt angle  of 3213393_3 by 10 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235024_4
- `C14`: Increase A3 Offset threshold for 3213393_3
- `C15`: Lift the tilt angle of 3235024_4 by 10 degrees
- `C16`: Add neighbor relationship between 3235024_4 and 3213393_3
- `C17`: Press down the tilt angle  of 3213393_3 by 10 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213393_3
- `C19`: Increase transmission power for 3235024_4
- `C20`: Add neighbor relationship between 3238910_1 and 3213393_3
- `C21`: Decrease A3 Offset threshold for 3213393_3
- `C22`: Press down the tilt angle of 3235024_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.967 | MS1 | 121.4656606363 | 31.1446281802 | 621 | 504990 | -80.11 | 13.75 | 467.42 | 0.18 | 2.87 | 1578 |
| 2024-09-20 22:21:32.613 | MS1 | 121.4656583797 | 31.1446216829 | 621 | 504990 | -81.24 | 17.69 | 585.50 | 0.07 | 2.24 | 1584 |
| 2024-09-20 22:21:33.947 | MS1 | 121.4656592192 | 31.1446304951 | 621 | 504990 | -80.31 | 14.63 | 434.63 | 0.19 | 2.85 | 1586 |
| 2024-09-20 22:21:34.563 | MS1 | 121.4656643224 | 31.1446357466 | 621 | 504990 | -91.37 | -3.52 | 63.29 | 0.18 | 1.00 | 1582 |
| 2024-09-20 22:21:35.365 | MS1 | 121.4656597127 | 31.1446287590 | 621 | 504990 | -90.95 | -1.32 | 55.73 | 0.15 | 1.17 | 1582 |
| 2024-09-20 22:21:36.434 | MS1 | 121.4656773604 | 31.1446297206 | 621 | 504990 | -91.27 | -0.73 | 44.63 | 0.01 | 1.30 | 1581 |
| 2024-09-20 22:21:37.611 | MS1 | 121.4656628888 | 31.1446269130 | 621 | 504990 | -92.90 | -3.66 | 33.92 | 0.07 | 1.18 | 1565 |
| 2024-09-20 22:21:38.765 | MS1 | 121.4656646464 | 31.1446215133 | 621 | 504990 | -85.04 | -2.00 | 68.65 | 0.18 | 1.18 | 1567 |
| 2024-09-20 22:21:39.229 | MS1 | 121.4656754820 | 31.1446222909 | 148 | 504990 | -84.25 | 17.68 | 236.37 | 0.18 | 1.45 | 1595 |
| 2024-09-20 22:21:40.647 | MS1 | 121.4656772653 | 31.1446363525 | 148 | 504990 | -76.73 | 15.21 | 565.32 | 0.16 | 2.84 | 1560 |
| 2024-09-20 22:21:41.196 | MS1 | 121.4656736278 | 31.1446350402 | 148 | 504990 | -79.39 | 17.08 | 588.71 | 0.13 | 2.44 | 1582 |
| 2024-09-20 22:21:42.524 | MS1 | 121.4656732840 | 31.1446238357 | 148 | 504990 | -79.06 | 17.74 | 570.64 | 0.02 | 2.58 | 1573 |

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
| 3213393 | 3 | 121.4743963138 | 31.1502864882 | 325 | 11 | 7 | 41.8 | TDD | 148 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3235024 | 4 | 121.4726315351 | 31.1471778425 | 247 | 15 | 2 | 38.6 | TDD | 621 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3238910 | 1 | 121.4715230311 | 31.1442018706 | 156 | 10 | 10 | 39.2 | TDD | 568 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3262274 | 2 | 121.4740226189 | 31.1445281703 | 214 | 1 | 3 | 29.1 | TDD | 768 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.352 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.375 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.514 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.514 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.162 | NREventA3 | measId:2;ServCellPCI:525;Se... |
| 2024-09-20 22:21:38.402 | NRHandoverAttempt | SourcePCI:525;SourceNR-ARFC... |
| 2024-09-20 22:21:38.438 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.449 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.576 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.576 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238910 | 1 | 6.3918 | 11.0815 | -116.0311 | 10.4291 | 155.1462 | 0.0176 | 0.0127 |
| 2024_09_20 22:00 | 3262274 | 2 | 10.4463 | 5.3022 | -116.0149 | 5.3999 | 96.3909 | 0.0077 | 0.0020 |
| 2024_09_20 22:00 | 3213393 | 3 | 15.7306 | 11.4361 | -116.1906 | 14.1162 | 169.1929 | 0.0024 | 0.0111 |
| 2024_09_20 22:00 | 3235024 | 4 | 17.6536 | 13.4849 | -116.6905 | 19.5318 | 194.3297 | 0.0084 | 0.1971 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414651_CE895FC2 | 504990 | 621 | -91.4 | 504990 | 148 | -84.0 | 504990 | 568 | -85.5 | 504990 | 768 |
| MR_1774414651_3665C64A | 504990 | 148 | -85.4 | 504990 | 621 | -91.4 | 504990 | 568 | -88.1 | 504990 | 768 |
| MR_1774414651_F67638D1 | 504990 | 621 | -89.8 | 504990 | 148 | -87.4 | 504990 | 568 | -86.7 | 504990 | 768 |
| MR_1774414651_5F654EC9 | 504990 | 621 | -91.7 | 504990 | 148 | -83.5 | 504990 | 568 | -85.0 | 504990 | 768 |
| MR_1774414651_CBA4726C | 504990 | 148 | -84.5 | 504990 | 621 | -93.3 | 504990 | 568 | -87.2 | 504990 | 768 |
| MR_1774414651_DFA788E5 | 504990 | 148 | -84.9 | 504990 | 621 | -90.2 | 504990 | 568 | -88.0 | 504990 | 768 |

> *... 2개 열 생략 (전체 14열)*

---
