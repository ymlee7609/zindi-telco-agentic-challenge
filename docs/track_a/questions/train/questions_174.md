# Track A 문제 분석 — train[1730]~train[1739]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1730] ~ train[1739] (10개)

## 목차

1. [문제 1730: `4aafbafb-e9a...`](#1730) — single-answer, 정답: C11
2. [문제 1731: `f30c823c-883...`](#1731) — single-answer, 정답: C16
3. [문제 1732: `b1e55fa6-3c1...`](#1732) — single-answer, 정답: C9
4. [문제 1733: `eae0bc6f-19a...`](#1733) — single-answer, 정답: C7
5. [문제 1734: `579141cc-05d...`](#1734) — multiple-answer, 정답: C10|C12
6. [문제 1735: `82386feb-499...`](#1735) — single-answer, 정답: C13
7. [문제 1736: `a437b9cb-ec3...`](#1736) — single-answer, 정답: C15
8. [문제 1737: `ff359d84-8e4...`](#1737) — single-answer, 정답: C14
9. [문제 1738: `c4456484-754...`](#1738) — single-answer, 정답: C18
10. [문제 1739: `6915143c-691...`](#1739) — multiple-answer, 정답: C5|C9|C13|C19

---

### 문제 1730: `4aafbafb-e9a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4aafbafb-e9a7-4c04-afd8-903fd9056b7b` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Lift the tilt angle  of 3273949_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1730] topology](images/train_1730.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256939_2
- `C2`: Check test server and transmission issues
- `C3`: Increase transmission power for 3270844_1
- `C4`: Increase A3 Offset threshold for 3270844_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270844_1
- `C7`: Decrease A3 Offset threshold for 3256939_2
- `C8`: Press down the tilt angle of 3256939_2 by 3 degrees
- `C9`: Add neighbor relationship between 3256939_2 and 3270844_1
- `C10`: Increase transmission power for 3256939_2
- `C11`: Lift the tilt angle  of 3273949_3 by 10 degrees **← 정답**
- `C12`: Increase A3 Offset threshold for 3256939_2
- `C13`: Adjust the azimuth of 3256939_2 by 47 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256939_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270844_1
- `C16`: Lift the tilt angle of 3256939_2 by 3 degrees
- `C17`: Decrease A3 Offset threshold for 3270844_1
- `C18`: Adjust the azimuth of 3273949_3 by 50 degrees
- `C19`: Press down the tilt angle  of 3273949_3 by 10 degrees
- `C20`: Decrease transmission power for 3256939_2
- `C21`: Decrease transmission power for 3270844_1
- `C22`: Add neighbor relationship between 3273949_3 and 3270844_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.457 | MS1 | 121.4656658714 | 31.1446335615 | 803 | 504990 | -87.99 | 15.80 | 595.30 | 0.09 | 2.46 | 1592 |
| 2024-09-20 22:21:32.643 | MS1 | 121.4656612525 | 31.1446322550 | 803 | 504990 | -86.87 | 16.40 | 446.77 | 0.17 | 2.90 | 1599 |
| 2024-09-20 22:21:33.398 | MS1 | 121.4656629101 | 31.1446379230 | 803 | 504990 | -86.94 | 12.86 | 350.10 | 0.07 | 2.46 | 1565 |
| 2024-09-20 22:21:34.167 | MS1 | 121.4656713272 | 31.1446224125 | 803 | 504990 | -91.04 | 14.57 | 55.84 | 0.07 | 2.23 | 1577 |
| 2024-09-20 22:21:35.849 | MS1 | 121.4656716912 | 31.1446203894 | 803 | 504990 | -86.31 | 17.63 | 94.72 | 0.07 | 2.56 | 1563 |
| 2024-09-20 22:21:36.120 | MS1 | 121.4656621982 | 31.1446340610 | 803 | 504990 | -88.57 | 16.07 | 49.39 | 0.19 | 2.31 | 1583 |
| 2024-09-20 22:21:37.258 | MS1 | 121.4656778629 | 31.1446369665 | 803 | 504990 | -93.34 | 11.31 | 87.30 | 0.19 | 2.50 | 1579 |
| 2024-09-20 22:21:38.110 | MS1 | 121.4656672000 | 31.1446275748 | 803 | 504990 | -89.03 | 12.91 | 98.90 | 0.13 | 2.02 | 1563 |
| 2024-09-20 22:21:39.455 | MS1 | 121.4656775301 | 31.1446181582 | 803 | 504990 | -91.81 | 10.28 | 58.21 | 0.04 | 2.88 | 1560 |
| 2024-09-20 22:21:40.165 | MS1 | 121.4656643766 | 31.1446257442 | 803 | 504990 | -93.79 | 11.59 | 378.59 | 0.03 | 2.22 | 1563 |
| 2024-09-20 22:21:41.729 | MS1 | 121.4656654506 | 31.1446373990 | 803 | 504990 | -89.30 | 8.09 | 480.68 | 0.19 | 2.02 | 1600 |
| 2024-09-20 22:21:42.498 | MS1 | 121.4656771937 | 31.1446371708 | 803 | 504990 | -90.16 | 11.79 | 453.39 | 0.01 | 2.69 | 1570 |

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
| 3256939 | 2 | 121.4745681337 | 31.1474685072 | 203 | 0 | 5 | 45.3 | TDD | 803 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3270844 | 1 | 121.4727162193 | 31.1470445796 | 93 | 10 | 0 | 32.8 | TDD | 106 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3273949 | 3 | 121.4673759530 | 31.1518151838 | 96 | 1 | 10 | 43.2 | TDD | 834 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3275158 | 4 | 121.4678240167 | 31.1486465562 | 68 | 3 | 6 | 47.5 | TDD | 79 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.401 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.418 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.563 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.563 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.264 | NREventA3 | measId:2;ServCellPCI:682;Se... |
| 2024-09-20 22:21:38.504 | NRHandoverAttempt | SourcePCI:682;SourceNR-ARFC... |
| 2024-09-20 22:21:38.554 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.569 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.711 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.711 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270844 | 1 | 17.4658 | 7.6360 | -115.9379 | 15.9611 | 115.8112 | 0.0099 | 0.0043 |
| 2024_09_20 22:00 | 3256939 | 2 | 87.2950 | 93.8139 | -116.5714 | 11.5732 | 130.8989 | 0.0058 | 0.0108 |
| 2024_09_20 22:00 | 3273949 | 3 | 13.7613 | 6.2937 | -115.6148 | 5.5241 | 101.7815 | 0.0034 | 0.0087 |
| 2024_09_20 22:00 | 3275158 | 4 | 11.9811 | 5.3692 | -117.4846 | 14.3552 | 173.4980 | 0.0018 | 0.0121 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416433_5C146CFB | 504990 | 803 | -91.2 | 504990 | 106 | -94.5 | 504990 | 834 | -99.9 | 504990 | 79 |
| MR_1774416433_DAA89382 | 504990 | 803 | -91.1 | 504990 | 106 | -92.3 | 504990 | 834 | -99.3 | 504990 | 79 |
| MR_1774416433_DA1A6675 | 504990 | 803 | -92.2 | 504990 | 106 | -92.6 | 504990 | 834 | -101.2 | 504990 | 79 |
| MR_1774416433_109AD443 | 504990 | 803 | -89.4 | 504990 | 106 | -94.9 | 504990 | 834 | -101.0 | 504990 | 79 |
| MR_1774416433_40EA6C61 | 504990 | 803 | -92.3 | 504990 | 106 | -92.9 | 504990 | 834 | -99.2 | 504990 | 79 |
| MR_1774416433_A2B9CDD6 | 504990 | 803 | -91.3 | 504990 | 106 | -94.8 | 504990 | 834 | -102.5 | 504990 | 79 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1731: `f30c823c-883...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f30c823c-883d-4395-9ccb-fd55d88e41b2` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1731] topology](images/train_1731.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3223809_1 and 3236249_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264044_2
- `C3`: Decrease transmission power for 3264044_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236249_3
- `C5`: Press down the tilt angle  of 3236249_3 by 10 degrees
- `C6`: Increase A3 Offset threshold for 3236249_3
- `C7`: Adjust the azimuth of 3236249_3 by 47 degrees
- `C8`: Add neighbor relationship between 3264044_2 and 3236249_3
- `C9`: Lift the tilt angle  of 3236249_3 by 10 degrees
- `C10`: Decrease transmission power for 3236249_3
- `C11`: Decrease A3 Offset threshold for 3264044_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236249_3
- `C13`: Increase transmission power for 3264044_2
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Lift the tilt angle of 3264044_2 by 10 degrees
- `C16`: Check test server and transmission issues **← 정답**
- `C17`: Decrease A3 Offset threshold for 3236249_3
- `C18`: Increase transmission power for 3236249_3
- `C19`: Press down the tilt angle of 3264044_2 by 10 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264044_2
- `C21`: Increase A3 Offset threshold for 3264044_2
- `C22`: Adjust the azimuth of 3264044_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.600 | MS1 | 121.4656639211 | 31.1446292776 | 73 | 504990 | -85.09 | 16.53 | 500.16 | 0.15 | 2.06 | 1577 |
| 2024-09-20 22:21:32.299 | MS1 | 121.4656586316 | 31.1446312723 | 73 | 504990 | -87.60 | 16.41 | 537.40 | 0.04 | 2.38 | 1568 |
| 2024-09-20 22:21:33.191 | MS1 | 121.4656690404 | 31.1446349700 | 73 | 504990 | -89.79 | 13.95 | 551.77 | 0.08 | 2.92 | 1569 |
| 2024-09-20 22:21:34.981 | MS1 | 121.4656753117 | 31.1446331076 | 73 | 504990 | -89.01 | 14.47 | 80.29 | 0.00 | 2.14 | 322 |
| 2024-09-20 22:21:35.637 | MS1 | 121.4656623084 | 31.1446286415 | 73 | 504990 | -88.07 | 16.41 | 64.45 | 0.00 | 2.20 | 355 |
| 2024-09-20 22:21:36.606 | MS1 | 121.4656738255 | 31.1446299934 | 73 | 504990 | -88.21 | 14.24 | 81.66 | 0.09 | 2.41 | 440 |
| 2024-09-20 22:21:37.784 | MS1 | 121.4656758408 | 31.1446196179 | 73 | 504990 | -92.09 | 9.01 | 53.46 | 0.08 | 2.03 | 423 |
| 2024-09-20 22:21:38.893 | MS1 | 121.4656606915 | 31.1446332443 | 73 | 504990 | -89.32 | 8.16 | 84.19 | 0.02 | 2.78 | 392 |
| 2024-09-20 22:21:39.521 | MS1 | 121.4656695030 | 31.1446267240 | 73 | 504990 | -89.04 | 11.47 | 107.13 | 0.04 | 2.76 | 400 |
| 2024-09-20 22:21:40.508 | MS1 | 121.4656634946 | 31.1446321194 | 73 | 504990 | -90.28 | 8.80 | 306.84 | 0.15 | 2.01 | 1596 |
| 2024-09-20 22:21:41.154 | MS1 | 121.4656607348 | 31.1446317265 | 73 | 504990 | -93.99 | 8.30 | 401.63 | 0.00 | 2.92 | 1585 |
| 2024-09-20 22:21:42.275 | MS1 | 121.4656674736 | 31.1446216944 | 73 | 504990 | -89.79 | 10.78 | 401.63 | 0.17 | 2.45 | 1592 |

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
| 3223809 | 1 | 121.4640563123 | 31.1548416047 | 255 | 11 | 5 | 37.0 | TDD | 680 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3236249 | 3 | 121.4675261710 | 31.1481725413 | 157 | 13 | 0 | 31.3 | TDD | 153 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3246498 | 4 | 121.4689531634 | 31.1507865583 | 218 | 14 | 2 | 19.8 | TDD | 1002 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3264044 | 2 | 121.4722610904 | 31.1443550554 | 129 | 14 | 2 | 43.2 | TDD | 73 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.439 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.463 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.589 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.589 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.325 | NREventA3 | measId:2;ServCellPCI:973;Se... |
| 2024-09-20 22:21:38.565 | NRHandoverAttempt | SourcePCI:973;SourceNR-ARFC... |
| 2024-09-20 22:21:38.603 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.616 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.735 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.735 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223809 | 1 | 11.1124 | 16.2331 | -116.4139 | 10.1275 | 111.3174 | 0.0035 | 0.0179 |
| 2024_09_20 22:00 | 3264044 | 2 | 12.6301 | 6.7623 | -114.1011 | 9.9976 | 104.5777 | 0.0102 | 0.0144 |
| 2024_09_20 22:00 | 3236249 | 3 | 8.9119 | 15.9046 | -117.5964 | 8.5795 | 91.4262 | 0.0188 | 0.0132 |
| 2024_09_20 22:00 | 3246498 | 4 | 8.1679 | 12.6673 | -117.4755 | 15.7838 | 122.1829 | 0.0088 | 0.0071 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415514_12BBBFB7 | 504990 | 73 | -89.2 | 504990 | 153 | -95.1 | 504990 | 680 | -97.3 | 504990 | 1002 |
| MR_1774415514_8EED840F | 504990 | 73 | -88.4 | 504990 | 153 | -95.5 | 504990 | 680 | -97.2 | 504990 | 1002 |
| MR_1774415514_77708285 | 504990 | 73 | -88.4 | 504990 | 153 | -95.5 | 504990 | 680 | -97.6 | 504990 | 1002 |
| MR_1774415514_DCF60F8C | 504990 | 73 | -90.8 | 504990 | 153 | -94.9 | 504990 | 680 | -94.5 | 504990 | 1002 |
| MR_1774415514_1BB4563A | 504990 | 73 | -88.0 | 504990 | 153 | -95.5 | 504990 | 680 | -97.8 | 504990 | 1002 |
| MR_1774415514_D5032C67 | 504990 | 73 | -87.1 | 504990 | 153 | -95.8 | 504990 | 680 | -95.6 | 504990 | 1002 |
| MR_1774415514_7713CA14 | 504990 | 73 | -90.7 | 504990 | 153 | -94.0 | 504990 | 680 | -96.9 | 504990 | 1002 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1732: `b1e55fa6-3c1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b1e55fa6-3c12-4e9a-aaba-68cea8c07bc8` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3245725_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1732] topology](images/train_1732.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269766_2
- `C2`: Decrease A3 Offset threshold for 3269766_2
- `C3`: Check test server and transmission issues
- `C4`: Press down the tilt angle of 3245725_1 by 4 degrees
- `C5`: Increase A3 Offset threshold for 3269766_2
- `C6`: Decrease transmission power for 3245725_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269766_2
- `C8`: Decrease A3 Offset threshold for 3245725_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245725_1 **← 정답**
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245725_1
- `C11`: Lift the tilt angle  of 3269766_2 by 10 degrees
- `C12`: Add neighbor relationship between 3245725_1 and 3269766_2
- `C13`: Increase A3 Offset threshold for 3245725_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Lift the tilt angle of 3245725_1 by 4 degrees
- `C16`: Adjust the azimuth of 3245725_1 by 3 degrees
- `C17`: Increase transmission power for 3245725_1
- `C18`: Increase transmission power for 3269766_2
- `C19`: Press down the tilt angle  of 3269766_2 by 10 degrees
- `C20`: Add neighbor relationship between 3244405_3 and 3269766_2
- `C21`: Adjust the azimuth of 3269766_2 by 50 degrees
- `C22`: Decrease transmission power for 3269766_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.532 | MS1 | 121.4656599077 | 31.1446282351 | 144 | 504990 | -87.98 | 13.79 | 480.84 | 0.12 | 2.10 | 1575 |
| 2024-09-20 22:21:32.332 | MS1 | 121.4656727962 | 31.1446319474 | 144 | 504990 | -88.79 | 12.15 | 411.94 | 0.17 | 2.92 | 1590 |
| 2024-09-20 22:21:33.285 | MS1 | 121.4656659883 | 31.1446285647 | 144 | 504990 | -91.75 | 15.44 | 472.69 | 0.07 | 2.76 | 1594 |
| 2024-09-20 22:21:34.255 | MS1 | 121.4656624553 | 31.1446215838 | 144 | 504990 | -85.22 | 15.61 | 57.46 | 0.68 | 2.53 | 696 |
| 2024-09-20 22:21:35.924 | MS1 | 121.4656717435 | 31.1446301119 | 144 | 504990 | -89.94 | 13.10 | 76.21 | 0.66 | 2.69 | 588 |
| 2024-09-20 22:21:36.140 | MS1 | 121.4656632353 | 31.1446352936 | 144 | 504990 | -89.37 | 16.06 | 64.23 | 0.55 | 2.24 | 644 |
| 2024-09-20 22:21:37.759 | MS1 | 121.4656744669 | 31.1446252673 | 144 | 504990 | -91.62 | 7.04 | 70.76 | 0.70 | 2.47 | 510 |
| 2024-09-20 22:21:38.942 | MS1 | 121.4656733030 | 31.1446294045 | 144 | 504990 | -93.03 | 12.61 | 51.24 | 0.70 | 2.51 | 585 |
| 2024-09-20 22:21:39.841 | MS1 | 121.4656760422 | 31.1446215371 | 144 | 504990 | -91.38 | 11.46 | 69.99 | 0.68 | 2.34 | 624 |
| 2024-09-20 22:21:40.191 | MS1 | 121.4656736662 | 31.1446271926 | 144 | 504990 | -93.56 | 9.22 | 364.29 | 0.01 | 2.92 | 1585 |
| 2024-09-20 22:21:41.481 | MS1 | 121.4656593365 | 31.1446206501 | 144 | 504990 | -90.80 | 9.73 | 337.40 | 0.06 | 2.83 | 1582 |
| 2024-09-20 22:21:42.736 | MS1 | 121.4656694025 | 31.1446205619 | 144 | 504990 | -90.46 | 7.49 | 381.52 | 0.14 | 2.74 | 1590 |

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
| 3244405 | 3 | 121.4675630644 | 31.1527710933 | 41 | 2 | 5 | 21.7 | TDD | 381 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3245725 | 1 | 121.4699143499 | 31.1552712456 | 202 | 2 | 10 | 38.8 | TDD | 144 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3268228 | 4 | 121.4696894131 | 31.1517258979 | 104 | 12 | 0 | 33.5 | TDD | 54 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3269766 | 2 | 121.4706259108 | 31.1500925378 | 33 | 13 | 0 | 34.1 | TDD | 68 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.543 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.558 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.665 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.665 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.369 | NREventA3 | measId:2;ServCellPCI:173;Se... |
| 2024-09-20 22:21:38.609 | NRHandoverAttempt | SourcePCI:173;SourceNR-ARFC... |
| 2024-09-20 22:21:38.642 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.654 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.796 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.796 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245725 | 1 | 5.7478 | 10.8800 | -116.6881 | 6.9874 | 120.1759 | 0.0188 | 0.0048 |
| 2024_09_20 22:00 | 3269766 | 2 | 15.6001 | 10.3217 | -115.3522 | 16.7198 | 175.0908 | 0.0094 | 0.0173 |
| 2024_09_20 22:00 | 3244405 | 3 | 6.4187 | 12.8794 | -114.8458 | 19.1302 | 94.5510 | 0.0112 | 0.0120 |
| 2024_09_20 22:00 | 3268228 | 4 | 19.1964 | 18.4035 | -117.0882 | 9.8396 | 174.8164 | 0.0133 | 0.0077 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413524_4E7B91DF | 504990 | 144 | -85.0 | 504990 | 68 | -92.0 | 504990 | 381 | -93.4 | 504990 | 54 |
| MR_1774413524_F613D225 | 504990 | 144 | -84.9 | 504990 | 68 | -90.8 | 504990 | 381 | -92.3 | 504990 | 54 |
| MR_1774413524_E9FB62BD | 504990 | 144 | -85.1 | 504990 | 68 | -92.5 | 504990 | 381 | -93.6 | 504990 | 54 |
| MR_1774413524_36B4DF83 | 504990 | 144 | -84.5 | 504990 | 68 | -92.6 | 504990 | 381 | -94.7 | 504990 | 54 |
| MR_1774413524_90FE555A | 504990 | 144 | -84.7 | 504990 | 68 | -91.6 | 504990 | 381 | -93.4 | 504990 | 54 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1733: `eae0bc6f-19a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `eae0bc6f-19a4-4e51-9f37-90d45e8c6d7a` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254875_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1733] topology](images/train_1733.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3254875_4
- `C2`: Decrease transmission power for 3230404_1
- `C3`: Decrease A3 Offset threshold for 3230404_1
- `C4`: Add neighbor relationship between 3269454_12 and 3230404_1
- `C5`: Decrease transmission power for 3254875_4
- `C6`: Adjust the azimuth of 3254875_4 by 28 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254875_4 **← 정답**
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230404_1
- `C9`: Adjust the azimuth of 3230404_1 by 6 degrees
- `C10`: Add neighbor relationship between 3254875_4 and 3230404_1
- `C11`: Lift the tilt angle of 3254875_4 by 5 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230404_1
- `C13`: Press down the tilt angle of 3254875_4 by 5 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254875_4
- `C15`: Increase A3 Offset threshold for 3254875_4
- `C16`: Increase A3 Offset threshold for 3230404_1
- `C17`: Check test server and transmission issues
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Increase transmission power for 3230404_1
- `C20`: Lift the tilt angle  of 3230404_1 by 4 degrees
- `C21`: Press down the tilt angle  of 3230404_1 by 4 degrees
- `C22`: Increase transmission power for 3254875_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.118 | MS1 | 121.4656643898 | 31.1446194977 | 402 | 504990 | -94.16 | 13.70 | 386.07 | 0.02 | 2.04 | 1594 |
| 2024-09-20 22:21:32.192 | MS1 | 121.4656668855 | 31.1446304367 | 263 | 504990 | -94.53 | 13.13 | 421.72 | 0.13 | 2.21 | 1588 |
| 2024-09-20 22:21:33.746 | MS1 | 121.4656738526 | 31.1446199167 | 635 | 504990 | -93.62 | 11.67 | 523.30 | 0.05 | 2.28 | 1598 |
| 2024-09-20 22:21:34.975 | MS1 | 121.4656715120 | 31.1446343374 | 749 | 152650 | -88.95 | 2.22 | 97.39 | 0.15 | 1.84 | 989 |
| 2024-09-20 22:21:35.672 | MS1 | 121.4656635090 | 31.1446214523 | 179 | 152650 | -93.42 | 4.64 | 68.00 | 0.07 | 1.63 | 973 |
| 2024-09-20 22:21:36.951 | MS1 | 121.4656762650 | 31.1446199969 | 886 | 152650 | -92.93 | 5.48 | 68.75 | 0.14 | 1.97 | 933 |
| 2024-09-20 22:21:37.578 | MS1 | 121.4656761519 | 31.1446316091 | 100 | 152650 | -87.31 | 3.98 | 103.53 | 0.01 | 1.68 | 942 |
| 2024-09-20 22:21:38.780 | MS1 | 121.4656655143 | 31.1446317207 | 749 | 152650 | -95.61 | 7.71 | 98.37 | 0.01 | 1.63 | 950 |
| 2024-09-20 22:21:39.999 | MS1 | 121.4656679671 | 31.1446345433 | 179 | 152650 | -91.74 | 4.96 | 77.92 | 0.04 | 1.86 | 949 |
| 2024-09-20 22:21:40.393 | MS1 | 121.4656636876 | 31.1446241767 | 886 | 152650 | -94.99 | 4.18 | 76.56 | 0.00 | 2.71 | 1573 |
| 2024-09-20 22:21:41.295 | MS1 | 121.4656610562 | 31.1446249715 | 100 | 152650 | -91.72 | 2.22 | 57.64 | 0.02 | 2.64 | 1562 |
| 2024-09-20 22:21:42.528 | MS1 | 121.4656645528 | 31.1446221352 | 749 | 152650 | -90.09 | 2.98 | 59.13 | 0.16 | 2.58 | 1575 |

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
| 3211029 | 11 | 121.4664482499 | 31.1539498230 | 166 | 11 | 12 | 2.1 | FDD | 179 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3222698 | 6 | 121.4662453953 | 31.1498626778 | 319 | 1 | 9 | 22.4 | TDD | 635 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3230192 | 10 | 121.4756585342 | 31.1453573295 | 22 | 3 | 5 | 18.6 | FDD | 749 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3230404 | 1 | 121.4665471260 | 31.1499057192 | 194 | 1 | 10 | 26.6 | TDD | 995 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3232211 | 5 | 121.4684328313 | 31.1532197675 | 77 | 9 | 11 | 7.0 | TDD | 243 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3249882 | 2 | 121.4726070495 | 31.1538211646 | 7 | 11 | 11 | 28.7 | TDD | 294 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3254875 | 4 | 121.4679393742 | 31.1507412545 | 226 | 4 | 8 | 9.2 | TDD | 402 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3255403 | 13 | 121.4660864166 | 31.1491646336 | 275 | 0 | 0 | 27.5 | FDD | 378 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3261845 | 8 | 121.4645714816 | 31.1525314995 | 189 | 1 | 5 | 14.8 | FDD | 455 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3264422 | 3 | 121.4671310119 | 31.1440933441 | 231 | 7 | 9 | 29.4 | TDD | 263 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3269454 | 12 | 121.4755090071 | 31.1494529803 | 320 | 4 | 1 | 7.4 | FDD | 886 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3272460 | 7 | 121.4679024647 | 31.1496947057 | 26 | 7 | 11 | 28.3 | FDD | 100 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3276837 | 9 | 121.4646532576 | 31.1530162777 | 348 | 12 | 2 | 19.7 | FDD | 1000 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |

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
| 2024-09-20 22:21:31.595 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.697 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.697 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.414 | NREventA2 | measId:1;ServCellPCI:651;Se... |
| 2024-09-20 22:21:35.563 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.781 | NREventA5 | measId:3;ServCellPCI:651;Se... |
| 2024-09-20 22:21:35.835 | NRHandoverAttempt | SourcePCI:651;SourceNR-ARFC... |
| 2024-09-20 22:21:35.874 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.889 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.997 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.997 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230404 | 1 | 7.5672 | 6.5039 | -116.2621 | 15.1427 | 94.8723 | 0.0067 | 0.0172 |
| 2024_09_20 22:00 | 3249882 | 2 | 18.0903 | 6.7214 | -116.9374 | 13.1147 | 175.8286 | 0.0011 | 0.0025 |
| 2024_09_20 22:00 | 3264422 | 3 | 11.2789 | 8.8759 | -116.5038 | 6.2366 | 149.5416 | 0.0168 | 0.0106 |
| 2024_09_20 22:00 | 3254875 | 4 | 6.5355 | 10.7373 | -115.1058 | 19.1189 | 95.4875 | 0.0080 | 0.0120 |
| 2024_09_20 22:00 | 3232211 | 5 | 15.8792 | 18.7217 | -115.3084 | 19.7732 | 114.5927 | 0.0033 | 0.0147 |
| 2024_09_20 22:00 | 3222698 | 6 | 11.4909 | 13.4203 | -115.3624 | 17.1894 | 197.7170 | 0.0101 | 0.0164 |
| 2024_09_20 22:00 | 3272460 | 7 | 9.7971 | 10.4807 | -117.7770 | 4.7533 | 42.5617 | 0.0174 | 0.0048 |
| 2024_09_20 22:00 | 3261845 | 8 | 6.0415 | 8.5927 | -114.6144 | 3.7523 | 55.0662 | 0.0106 | 0.0008 |
| 2024_09_20 22:00 | 3276837 | 9 | 18.5744 | 6.6486 | -116.0738 | 4.2585 | 36.8323 | 0.0011 | 0.0016 |
| 2024_09_20 22:00 | 3230192 | 10 | 7.9352 | 16.6514 | -114.9608 | 4.4320 | 33.5051 | 0.0003 | 0.0188 |
| 2024_09_20 22:00 | 3211029 | 11 | 12.0895 | 12.5321 | -115.2659 | 4.8121 | 29.6744 | 0.0050 | 0.0020 |
| 2024_09_20 22:00 | 3269454 | 12 | 7.9139 | 19.3140 | -116.4747 | 3.9176 | 42.0036 | 0.0071 | 0.0142 |
| 2024_09_20 22:00 | 3255403 | 13 | 10.8783 | 16.2050 | -115.6700 | 3.0573 | 55.0918 | 0.0011 | 0.0196 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417196_1405037A | 152650 | 749 | -89.6 | 152650 | 455 | -93.8 | 152650 | 378 | -94.2 | 152650 | 1000 |
| MR_1774417196_849A792A | 504990 | 635 | -92.5 | 504990 | 995 | -90.1 | 504990 | 243 | -98.3 | 504990 | 294 |
| MR_1774417196_6D2D476B | 504990 | 635 | -93.7 | 504990 | 995 | -89.7 | 504990 | 243 | -101.8 | 504990 | 294 |
| MR_1774417196_B09738A7 | 504990 | 635 | -93.9 | 504990 | 995 | -87.4 | 504990 | 243 | -99.9 | 504990 | 294 |
| MR_1774417196_2FE6E071 | 504990 | 635 | -93.7 | 504990 | 995 | -89.9 | 504990 | 243 | -101.2 | 504990 | 294 |
| MR_1774417196_01D201C8 | 152650 | 749 | -87.2 | 152650 | 455 | -91.5 | 152650 | 378 | -94.5 | 152650 | 1000 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1734: `579141cc-05d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `579141cc-05db-41b8-aa5e-5f0c5a2cb07e` |
| Tag | **multiple-answer** |
| 정답 | **C10|C12** |
| C10 의미 | Decrease transmission power for 3243122_3 |
| C12 의미 | Press down the tilt angle  of 3243122_3 by 4 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1734] topology](images/train_1734.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3251754_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243122_3
- `C3`: Increase transmission power for 3243122_3
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease A3 Offset threshold for 3251754_1
- `C6`: Increase A3 Offset threshold for 3243122_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251754_1
- `C8`: Lift the tilt angle of 3251754_1 by 3 degrees
- `C9`: Decrease A3 Offset threshold for 3243122_3
- `C10`: Decrease transmission power for 3243122_3 **← 정답**
- `C11`: Check test server and transmission issues
- `C12`: Press down the tilt angle  of 3243122_3 by 4 degrees **← 정답**
- `C13`: Decrease transmission power for 3251754_1
- `C14`: Add neighbor relationship between 3223235_2 and 3243122_3
- `C15`: Increase transmission power for 3251754_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251754_1
- `C17`: Lift the tilt angle  of 3243122_3 by 4 degrees
- `C18`: Press down the tilt angle of 3251754_1 by 3 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243122_3
- `C20`: Adjust the azimuth of 3251754_1 by 11 degrees
- `C21`: Adjust the azimuth of 3243122_3 by 8 degrees
- `C22`: Add neighbor relationship between 3251754_1 and 3243122_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.565 | MS1 | 121.4656584006 | 31.1446339163 | 880 | 504990 | -84.34 | 16.65 | 472.93 | 0.06 | 2.65 | 1570 |
| 2024-09-20 22:21:32.613 | MS1 | 121.4656610849 | 31.1446263517 | 880 | 504990 | -79.01 | 15.74 | 350.65 | 0.18 | 2.50 | 1579 |
| 2024-09-20 22:21:33.397 | MS1 | 121.4656684263 | 31.1446270927 | 880 | 504990 | -82.07 | 16.61 | 474.41 | 0.05 | 2.50 | 1570 |
| 2024-09-20 22:21:34.247 | MS1 | 121.4656775615 | 31.1446228295 | 880 | 504990 | -91.05 | 3.86 | 62.16 | 0.03 | 1.14 | 1564 |
| 2024-09-20 22:21:35.759 | MS1 | 121.4656602374 | 31.1446311569 | 880 | 504990 | -85.97 | 1.29 | 74.89 | 0.07 | 1.39 | 1595 |
| 2024-09-20 22:21:36.484 | MS1 | 121.4656580706 | 31.1446275578 | 880 | 504990 | -94.59 | 1.98 | 56.59 | 0.16 | 1.34 | 1584 |
| 2024-09-20 22:21:37.409 | MS1 | 121.4656593227 | 31.1446323879 | 880 | 504990 | -87.54 | 3.84 | 56.33 | 0.11 | 1.17 | 1582 |
| 2024-09-20 22:21:38.275 | MS1 | 121.4656642611 | 31.1446222442 | 880 | 504990 | -94.35 | 2.89 | 49.53 | 0.07 | 1.39 | 1571 |
| 2024-09-20 22:21:39.345 | MS1 | 121.4656752037 | 31.1446237899 | 880 | 504990 | -85.89 | 3.47 | 71.77 | 0.03 | 1.01 | 1570 |
| 2024-09-20 22:21:40.702 | MS1 | 121.4656772587 | 31.1446377504 | 880 | 504990 | -75.91 | 15.17 | 325.64 | 0.19 | 2.90 | 1600 |
| 2024-09-20 22:21:41.350 | MS1 | 121.4656688001 | 31.1446281499 | 880 | 504990 | -81.40 | 17.85 | 433.33 | 0.04 | 2.51 | 1589 |
| 2024-09-20 22:21:42.550 | MS1 | 121.4656691707 | 31.1446206136 | 880 | 504990 | -77.71 | 14.76 | 456.65 | 0.20 | 2.45 | 1570 |

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
| 3214595 | 4 | 121.4755983602 | 31.1468037497 | 245 | 1 | 10 | 30.0 | TDD | 940 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3223235 | 2 | 121.4694644287 | 31.1467943316 | 311 | 14 | 1 | 40.0 | TDD | 186 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3243122 | 3 | 121.4729179409 | 31.1469722558 | 241 | 1 | 9 | 32.6 | TDD | 171 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3251754 | 1 | 121.4692905489 | 31.1520194332 | 214 | 1 | 10 | 37.7 | TDD | 880 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.481 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.503 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.635 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.635 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251754 | 1 | 15.8171 | 7.0254 | -108.5908 | 10.9404 | 188.7518 | 0.0140 | 0.0082 |
| 2024_09_20 22:00 | 3223235 | 2 | 17.3433 | 13.6495 | -114.1699 | 5.0859 | 184.1479 | 0.0058 | 0.0081 |
| 2024_09_20 22:00 | 3243122 | 3 | 19.5138 | 14.0198 | -117.0720 | 8.0352 | 168.9581 | 0.0181 | 0.0008 |
| 2024_09_20 22:00 | 3214595 | 4 | 17.8924 | 5.8315 | -116.7786 | 16.1668 | 172.9262 | 0.0147 | 0.0013 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417046_95AF2AD8 | 504990 | 880 | -89.1 | 504990 | 171 | -89.4 | 504990 | 186 | -91.9 | 504990 | 940 |
| MR_1774417046_95FBF8EB | 504990 | 880 | -89.3 | 504990 | 171 | -90.6 | 504990 | 186 | -90.2 | 504990 | 940 |
| MR_1774417046_692C61D3 | 504990 | 880 | -90.3 | 504990 | 171 | -90.7 | 504990 | 186 | -91.4 | 504990 | 940 |
| MR_1774417046_56C9CA6E | 504990 | 171 | -91.3 | 504990 | 880 | -89.5 | 504990 | 186 | -92.3 | 504990 | 940 |
| MR_1774417046_7C4EAA80 | 504990 | 880 | -90.7 | 504990 | 171 | -90.3 | 504990 | 186 | -92.2 | 504990 | 940 |
| MR_1774417046_92553C7A | 504990 | 880 | -89.4 | 504990 | 171 | -87.3 | 504990 | 186 | -90.3 | 504990 | 940 |
| MR_1774417046_5B8668DB | 504990 | 171 | -89.2 | 504990 | 880 | -87.0 | 504990 | 186 | -91.5 | 504990 | 940 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1735: `82386feb-499...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `82386feb-499c-480c-8137-00734a843add` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Lift the tilt angle  of 3217443_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1735] topology](images/train_1735.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3215482_4 and 3267903_2
- `C2`: Decrease transmission power for 3267903_2
- `C3`: Add neighbor relationship between 3217443_3 and 3267903_2
- `C4`: Increase A3 Offset threshold for 3215482_4
- `C5`: Lift the tilt angle of 3215482_4 by 3 degrees
- `C6`: Increase A3 Offset threshold for 3267903_2
- `C7`: Press down the tilt angle  of 3217443_3 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267903_2
- `C9`: Adjust the azimuth of 3217443_3 by 50 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Check test server and transmission issues
- `C12`: Increase transmission power for 3215482_4
- `C13`: Lift the tilt angle  of 3217443_3 by 10 degrees **← 정답**
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267903_2
- `C15`: Decrease transmission power for 3215482_4
- `C16`: Decrease A3 Offset threshold for 3215482_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215482_4
- `C18`: Increase transmission power for 3267903_2
- `C19`: Press down the tilt angle of 3215482_4 by 3 degrees
- `C20`: Decrease A3 Offset threshold for 3267903_2
- `C21`: Adjust the azimuth of 3215482_4 by 48 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215482_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.971 | MS1 | 121.4656733535 | 31.1446221178 | 677 | 504990 | -90.00 | 12.21 | 577.94 | 0.14 | 2.90 | 1583 |
| 2024-09-20 22:21:32.326 | MS1 | 121.4656740836 | 31.1446265219 | 677 | 504990 | -88.96 | 14.06 | 466.34 | 0.10 | 2.40 | 1561 |
| 2024-09-20 22:21:33.994 | MS1 | 121.4656704987 | 31.1446238677 | 677 | 504990 | -88.62 | 13.81 | 342.40 | 0.11 | 2.37 | 1565 |
| 2024-09-20 22:21:34.892 | MS1 | 121.4656726916 | 31.1446200726 | 677 | 504990 | -85.91 | 14.59 | 58.47 | 0.01 | 2.64 | 1560 |
| 2024-09-20 22:21:35.759 | MS1 | 121.4656765464 | 31.1446206623 | 677 | 504990 | -88.16 | 12.46 | 97.00 | 0.05 | 2.89 | 1577 |
| 2024-09-20 22:21:36.246 | MS1 | 121.4656665972 | 31.1446213818 | 677 | 504990 | -91.51 | 17.59 | 81.92 | 0.06 | 2.35 | 1600 |
| 2024-09-20 22:21:37.899 | MS1 | 121.4656691373 | 31.1446349972 | 677 | 504990 | -91.11 | 10.08 | 61.13 | 0.05 | 2.85 | 1564 |
| 2024-09-20 22:21:38.425 | MS1 | 121.4656644615 | 31.1446345315 | 677 | 504990 | -91.05 | 10.04 | 58.55 | 0.03 | 2.25 | 1583 |
| 2024-09-20 22:21:39.526 | MS1 | 121.4656652937 | 31.1446269357 | 677 | 504990 | -89.78 | 11.81 | 52.23 | 0.14 | 2.49 | 1597 |
| 2024-09-20 22:21:40.681 | MS1 | 121.4656753619 | 31.1446255111 | 677 | 504990 | -93.52 | 11.52 | 432.33 | 0.08 | 2.66 | 1578 |
| 2024-09-20 22:21:41.598 | MS1 | 121.4656596434 | 31.1446276946 | 677 | 504990 | -92.85 | 7.67 | 528.82 | 0.04 | 2.62 | 1580 |
| 2024-09-20 22:21:42.423 | MS1 | 121.4656731475 | 31.1446370939 | 677 | 504990 | -91.38 | 9.32 | 346.13 | 0.06 | 2.30 | 1579 |

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
| 3215482 | 4 | 121.4716745235 | 31.1507817573 | 268 | 2 | 0 | 22.6 | TDD | 677 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3217443 | 3 | 121.4750162812 | 31.1483542961 | 41 | 3 | 6 | 26.8 | TDD | 885 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3244347 | 1 | 121.4748546386 | 31.1553382017 | 335 | 1 | 1 | 20.0 | TDD | 377 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3267903 | 2 | 121.4686320134 | 31.1534958352 | 22 | 14 | 8 | 31.5 | TDD | 307 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.592 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.610 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.730 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.730 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.398 | NREventA3 | measId:2;ServCellPCI:191;Se... |
| 2024-09-20 22:21:38.638 | NRHandoverAttempt | SourcePCI:191;SourceNR-ARFC... |
| 2024-09-20 22:21:38.681 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.692 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.812 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.812 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244347 | 1 | 11.8078 | 10.9275 | -116.1614 | 15.7485 | 170.6464 | 0.0028 | 0.0138 |
| 2024_09_20 22:00 | 3267903 | 2 | 19.0030 | 7.3764 | -117.1295 | 6.0668 | 128.1643 | 0.0153 | 0.0076 |
| 2024_09_20 22:00 | 3217443 | 3 | 5.7975 | 5.0275 | -116.9588 | 7.2013 | 119.4220 | 0.0066 | 0.0149 |
| 2024_09_20 22:00 | 3215482 | 4 | 87.8960 | 85.4966 | -116.0709 | 6.6752 | 157.9210 | 0.0182 | 0.0185 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415692_AFFA2EAB | 504990 | 677 | -85.8 | 504990 | 307 | -93.8 | 504990 | 885 | -93.6 | 504990 | 377 |
| MR_1774415692_F0F78316 | 504990 | 677 | -86.9 | 504990 | 307 | -94.6 | 504990 | 885 | -92.2 | 504990 | 377 |
| MR_1774415692_7C925BFB | 504990 | 677 | -85.2 | 504990 | 307 | -93.5 | 504990 | 885 | -92.1 | 504990 | 377 |
| MR_1774415692_23CE809C | 504990 | 677 | -84.0 | 504990 | 307 | -92.5 | 504990 | 885 | -94.5 | 504990 | 377 |
| MR_1774415692_16E20ADE | 504990 | 677 | -84.5 | 504990 | 307 | -93.3 | 504990 | 885 | -95.7 | 504990 | 377 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1736: `a437b9cb-ec3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a437b9cb-ec38-4b1c-a9bc-9c439d5ba232` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3248117_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1736] topology](images/train_1736.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3248117_3 by 2 degrees
- `C2`: Add neighbor relationship between 3224691_4 and 3217660_2
- `C3`: Add neighbor relationship between 3248117_3 and 3217660_2
- `C4`: Increase A3 Offset threshold for 3217660_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217660_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248117_3
- `C7`: Check test server and transmission issues
- `C8`: Decrease transmission power for 3217660_2
- `C9`: Lift the tilt angle  of 3217660_2 by 2 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217660_2
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Adjust the azimuth of 3217660_2 by 50 degrees
- `C13`: Increase transmission power for 3248117_3
- `C14`: Press down the tilt angle  of 3217660_2 by 2 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248117_3 **← 정답**
- `C16`: Adjust the azimuth of 3248117_3 by 27 degrees
- `C17`: Decrease transmission power for 3248117_3
- `C18`: Increase transmission power for 3217660_2
- `C19`: Decrease A3 Offset threshold for 3248117_3
- `C20`: Lift the tilt angle of 3248117_3 by 2 degrees
- `C21`: Decrease A3 Offset threshold for 3217660_2
- `C22`: Increase A3 Offset threshold for 3248117_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.208 | MS1 | 121.4656626210 | 31.1446355830 | 35 | 504990 | -91.97 | 16.71 | 456.46 | 0.07 | 2.86 | 1569 |
| 2024-09-20 22:21:32.169 | MS1 | 121.4656650617 | 31.1446298138 | 35 | 504990 | -91.66 | 17.28 | 498.97 | 0.08 | 2.49 | 1593 |
| 2024-09-20 22:21:33.510 | MS1 | 121.4656591178 | 31.1446378942 | 35 | 504990 | -90.02 | 13.43 | 484.61 | 0.18 | 2.48 | 1583 |
| 2024-09-20 22:21:34.124 | MS1 | 121.4656775098 | 31.1446239317 | 35 | 504990 | -90.54 | 17.22 | 79.87 | 0.51 | 2.89 | 564 |
| 2024-09-20 22:21:35.299 | MS1 | 121.4656714715 | 31.1446263736 | 35 | 504990 | -90.55 | 17.79 | 70.96 | 0.53 | 2.26 | 529 |
| 2024-09-20 22:21:36.982 | MS1 | 121.4656759033 | 31.1446265310 | 35 | 504990 | -90.64 | 16.45 | 49.70 | 0.68 | 2.48 | 629 |
| 2024-09-20 22:21:37.926 | MS1 | 121.4656638891 | 31.1446365568 | 35 | 504990 | -90.67 | 9.06 | 85.25 | 0.62 | 2.34 | 632 |
| 2024-09-20 22:21:38.752 | MS1 | 121.4656588691 | 31.1446226611 | 35 | 504990 | -92.92 | 9.41 | 63.66 | 0.54 | 2.44 | 534 |
| 2024-09-20 22:21:39.939 | MS1 | 121.4656768276 | 31.1446196442 | 35 | 504990 | -91.97 | 12.70 | 79.51 | 0.53 | 2.97 | 622 |
| 2024-09-20 22:21:40.238 | MS1 | 121.4656645328 | 31.1446341652 | 35 | 504990 | -92.40 | 11.28 | 582.93 | 0.13 | 2.52 | 1568 |
| 2024-09-20 22:21:41.737 | MS1 | 121.4656749276 | 31.1446249766 | 35 | 504990 | -93.09 | 12.16 | 596.22 | 0.18 | 2.45 | 1580 |
| 2024-09-20 22:21:42.153 | MS1 | 121.4656661875 | 31.1446222841 | 35 | 504990 | -91.14 | 12.89 | 373.34 | 0.20 | 2.95 | 1560 |

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
| 3217660 | 2 | 121.4654717162 | 31.1547279168 | 341 | 1 | 2 | 21.1 | TDD | 962 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3224691 | 4 | 121.4693771121 | 31.1532369061 | 267 | 10 | 12 | 38.6 | TDD | 106 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3237962 | 1 | 121.4690920659 | 31.1529389065 | 203 | 15 | 11 | 19.2 | TDD | 576 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3248117 | 3 | 121.4681302985 | 31.1496760345 | 176 | 0 | 1 | 21.6 | TDD | 35 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.979 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.995 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.131 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.131 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.833 | NREventA3 | measId:2;ServCellPCI:875;Se... |
| 2024-09-20 22:21:38.073 | NRHandoverAttempt | SourcePCI:875;SourceNR-ARFC... |
| 2024-09-20 22:21:38.103 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.114 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.232 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.232 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237962 | 1 | 8.0580 | 12.6369 | -114.8660 | 15.8962 | 144.6519 | 0.0132 | 0.0159 |
| 2024_09_20 22:00 | 3217660 | 2 | 16.3670 | 5.5400 | -114.4972 | 5.6557 | 151.4942 | 0.0049 | 0.0026 |
| 2024_09_20 22:00 | 3248117 | 3 | 14.5414 | 19.3244 | -116.6484 | 6.7763 | 181.6794 | 0.0042 | 0.0143 |
| 2024_09_20 22:00 | 3224691 | 4 | 15.7270 | 8.4103 | -117.4031 | 10.1892 | 181.8350 | 0.0156 | 0.0003 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413339_B4A1165E | 504990 | 35 | -91.2 | 504990 | 962 | -96.3 | 504990 | 106 | -97.3 | 504990 | 576 |
| MR_1774413339_B9A41F34 | 504990 | 35 | -89.7 | 504990 | 962 | -96.0 | 504990 | 106 | -97.8 | 504990 | 576 |
| MR_1774413339_877DBBB3 | 504990 | 35 | -89.8 | 504990 | 962 | -97.5 | 504990 | 106 | -97.6 | 504990 | 576 |
| MR_1774413339_73789617 | 504990 | 35 | -89.0 | 504990 | 962 | -96.8 | 504990 | 106 | -96.1 | 504990 | 576 |
| MR_1774413339_4F9DF8BA | 504990 | 35 | -90.4 | 504990 | 962 | -97.2 | 504990 | 106 | -94.9 | 504990 | 576 |
| MR_1774413339_C69B1AD2 | 504990 | 35 | -91.7 | 504990 | 962 | -95.5 | 504990 | 106 | -96.3 | 504990 | 576 |
| MR_1774413339_FBEE316D | 504990 | 35 | -91.0 | 504990 | 962 | -97.8 | 504990 | 106 | -95.9 | 504990 | 576 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1737: `ff359d84-8e4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ff359d84-8e43-4a38-848f-d394053b111a` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease A3 Offset threshold for 3248786_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1737] topology](images/train_1737.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3248786_3 and 3230037_2
- `C2`: Increase A3 Offset threshold for 3230037_2
- `C3`: Decrease transmission power for 3230037_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Adjust the azimuth of 3230037_2 by 6 degrees
- `C6`: Lift the tilt angle  of 3230037_2 by 4 degrees
- `C7`: Press down the tilt angle of 3248786_3 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248786_3
- `C9`: Increase A3 Offset threshold for 3248786_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230037_2
- `C11`: Increase transmission power for 3248786_3
- `C12`: Adjust the azimuth of 3248786_3 by 50 degrees
- `C13`: Check test server and transmission issues
- `C14`: Decrease A3 Offset threshold for 3248786_3 **← 정답**
- `C15`: Decrease A3 Offset threshold for 3230037_2
- `C16`: Decrease transmission power for 3248786_3
- `C17`: Add neighbor relationship between 3245790_1 and 3230037_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248786_3
- `C19`: Lift the tilt angle of 3248786_3 by 10 degrees
- `C20`: Increase transmission power for 3230037_2
- `C21`: Press down the tilt angle  of 3230037_2 by 4 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230037_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.866 | MS1 | 121.4656774111 | 31.1446310036 | 348 | 504990 | -81.08 | 13.32 | 574.43 | 0.09 | 2.25 | 1591 |
| 2024-09-20 22:21:32.381 | MS1 | 121.4656598989 | 31.1446347982 | 348 | 504990 | -82.25 | 16.81 | 588.62 | 0.14 | 2.25 | 1600 |
| 2024-09-20 22:21:33.773 | MS1 | 121.4656726705 | 31.1446369369 | 348 | 504990 | -77.01 | 15.37 | 492.44 | 0.13 | 2.14 | 1592 |
| 2024-09-20 22:21:34.773 | MS1 | 121.4656709905 | 31.1446292894 | 348 | 504990 | -92.96 | -0.16 | 43.05 | 0.18 | 1.14 | 1590 |
| 2024-09-20 22:21:35.628 | MS1 | 121.4656665759 | 31.1446240787 | 348 | 504990 | -92.43 | -0.70 | 37.27 | 0.18 | 1.07 | 1566 |
| 2024-09-20 22:21:36.261 | MS1 | 121.4656675261 | 31.1446375124 | 348 | 504990 | -85.23 | -1.17 | 58.13 | 0.01 | 1.41 | 1570 |
| 2024-09-20 22:21:37.761 | MS1 | 121.4656631232 | 31.1446252564 | 348 | 504990 | -86.97 | -2.84 | 30.97 | 0.16 | 1.40 | 1581 |
| 2024-09-20 22:21:38.307 | MS1 | 121.4656762392 | 31.1446269735 | 348 | 504990 | -87.40 | -0.03 | 52.49 | 0.15 | 1.01 | 1586 |
| 2024-09-20 22:21:39.687 | MS1 | 121.4656666345 | 31.1446310693 | 123 | 504990 | -77.90 | 13.16 | 245.79 | 0.11 | 1.22 | 1579 |
| 2024-09-20 22:21:40.359 | MS1 | 121.4656776473 | 31.1446195447 | 123 | 504990 | -77.54 | 13.57 | 340.96 | 0.16 | 2.59 | 1599 |
| 2024-09-20 22:21:41.303 | MS1 | 121.4656685553 | 31.1446272375 | 123 | 504990 | -83.30 | 15.81 | 360.30 | 0.05 | 2.71 | 1589 |
| 2024-09-20 22:21:42.796 | MS1 | 121.4656654613 | 31.1446271314 | 123 | 504990 | -78.38 | 17.15 | 565.96 | 0.07 | 2.45 | 1564 |

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
| 3230037 | 2 | 121.4751852384 | 31.1534217354 | 217 | 3 | 1 | 31.9 | TDD | 123 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3245790 | 1 | 121.4711390725 | 31.1521068886 | 69 | 9 | 12 | 19.2 | TDD | 824 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3248786 | 3 | 121.4690953479 | 31.1460210124 | 132 | 12 | 8 | 17.8 | TDD | 348 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3262690 | 4 | 121.4645717653 | 31.1542107499 | 120 | 15 | 4 | 35.5 | TDD | 838 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.767 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.787 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.904 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.904 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.602 | NREventA3 | measId:2;ServCellPCI:13;Ser... |
| 2024-09-20 22:21:37.842 | NRHandoverAttempt | SourcePCI:13;SourceNR-ARFCN... |
| 2024-09-20 22:21:37.881 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.896 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.046 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.046 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245790 | 1 | 6.3268 | 15.5126 | -116.6151 | 9.4795 | 90.4536 | 0.0033 | 0.0031 |
| 2024_09_20 22:00 | 3230037 | 2 | 11.4695 | 14.3177 | -116.2099 | 10.2461 | 109.3619 | 0.0091 | 0.0042 |
| 2024_09_20 22:00 | 3248786 | 3 | 18.3070 | 9.1294 | -117.5482 | 6.8453 | 144.7282 | 0.0099 | 0.1737 |
| 2024_09_20 22:00 | 3262690 | 4 | 9.4587 | 5.8335 | -115.6468 | 9.5517 | 117.9284 | 0.0025 | 0.0035 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415222_78032511 | 504990 | 123 | -86.6 | 504990 | 348 | -91.6 | 504990 | 824 | -88.9 | 504990 | 838 |
| MR_1774415222_776003EB | 504990 | 123 | -85.0 | 504990 | 348 | -91.6 | 504990 | 824 | -90.3 | 504990 | 838 |
| MR_1774415222_3D7D27EC | 504990 | 123 | -86.9 | 504990 | 348 | -93.1 | 504990 | 824 | -88.6 | 504990 | 838 |
| MR_1774415222_5BC8F262 | 504990 | 348 | -91.7 | 504990 | 123 | -86.4 | 504990 | 824 | -89.3 | 504990 | 838 |
| MR_1774415222_D3A80EEC | 504990 | 348 | -92.0 | 504990 | 123 | -87.4 | 504990 | 824 | -89.5 | 504990 | 838 |
| MR_1774415222_80E0BD9D | 504990 | 123 | -85.7 | 504990 | 348 | -92.9 | 504990 | 824 | -90.3 | 504990 | 838 |
| MR_1774415222_D13ED578 | 504990 | 123 | -87.9 | 504990 | 348 | -92.4 | 504990 | 824 | -90.2 | 504990 | 838 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1738: `c4456484-754...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c4456484-7542-4ed0-b00b-317662be690f` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3255098_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1738] topology](images/train_1738.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3234400_4
- `C2`: Lift the tilt angle of 3255098_1 by 2 degrees
- `C3`: Increase A3 Offset threshold for 3255098_1
- `C4`: Adjust the azimuth of 3234400_4 by 50 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Add neighbor relationship between 3236084_3 and 3234400_4
- `C7`: Increase transmission power for 3255098_1
- `C8`: Adjust the azimuth of 3255098_1 by 49 degrees
- `C9`: Decrease A3 Offset threshold for 3234400_4
- `C10`: Decrease A3 Offset threshold for 3255098_1
- `C11`: Lift the tilt angle  of 3234400_4 by 10 degrees
- `C12`: Press down the tilt angle of 3255098_1 by 2 degrees
- `C13`: Increase A3 Offset threshold for 3234400_4
- `C14`: Check test server and transmission issues
- `C15`: Add neighbor relationship between 3255098_1 and 3234400_4
- `C16`: Decrease transmission power for 3255098_1
- `C17`: Press down the tilt angle  of 3234400_4 by 10 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255098_1 **← 정답**
- `C19`: Decrease transmission power for 3234400_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234400_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234400_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255098_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.937 | MS1 | 121.4656669456 | 31.1446259407 | 345 | 504990 | -86.29 | 14.69 | 506.85 | 0.08 | 2.07 | 1586 |
| 2024-09-20 22:21:32.502 | MS1 | 121.4656739450 | 31.1446355847 | 345 | 504990 | -86.14 | 15.74 | 534.77 | 0.02 | 2.35 | 1569 |
| 2024-09-20 22:21:33.287 | MS1 | 121.4656701370 | 31.1446336968 | 345 | 504990 | -88.17 | 15.61 | 508.23 | 0.17 | 2.14 | 1593 |
| 2024-09-20 22:21:34.110 | MS1 | 121.4656596560 | 31.1446247458 | 345 | 504990 | -88.38 | 12.49 | 59.32 | 0.59 | 2.50 | 510 |
| 2024-09-20 22:21:35.461 | MS1 | 121.4656585028 | 31.1446181504 | 345 | 504990 | -88.71 | 16.48 | 87.91 | 0.65 | 2.05 | 655 |
| 2024-09-20 22:21:36.573 | MS1 | 121.4656705396 | 31.1446352553 | 345 | 504990 | -91.72 | 14.63 | 91.87 | 0.54 | 2.65 | 535 |
| 2024-09-20 22:21:37.512 | MS1 | 121.4656735209 | 31.1446236460 | 345 | 504990 | -92.42 | 12.85 | 91.80 | 0.53 | 2.57 | 596 |
| 2024-09-20 22:21:38.873 | MS1 | 121.4656636766 | 31.1446194289 | 345 | 504990 | -89.41 | 8.83 | 76.47 | 0.67 | 2.56 | 508 |
| 2024-09-20 22:21:39.834 | MS1 | 121.4656709544 | 31.1446222194 | 345 | 504990 | -89.21 | 12.21 | 68.08 | 0.50 | 2.00 | 594 |
| 2024-09-20 22:21:40.202 | MS1 | 121.4656617419 | 31.1446208870 | 345 | 504990 | -92.24 | 7.50 | 317.41 | 0.01 | 2.31 | 1565 |
| 2024-09-20 22:21:41.476 | MS1 | 121.4656658579 | 31.1446268942 | 345 | 504990 | -91.91 | 11.85 | 580.91 | 0.04 | 2.75 | 1568 |
| 2024-09-20 22:21:42.549 | MS1 | 121.4656707856 | 31.1446298320 | 345 | 504990 | -93.83 | 9.00 | 373.56 | 0.04 | 2.13 | 1594 |

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
| 3234400 | 4 | 121.4667363047 | 31.1498102003 | 100 | 8 | 2 | 33.1 | TDD | 70 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3236084 | 3 | 121.4758951163 | 31.1485479350 | 208 | 8 | 0 | 40.9 | TDD | 21 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3241019 | 2 | 121.4646357373 | 31.1487848590 | 146 | 4 | 9 | 35.2 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3255098 | 1 | 121.4745127961 | 31.1452921171 | 216 | 0 | 7 | 23.6 | TDD | 345 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.778 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.803 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.938 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.938 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.636 | NREventA3 | measId:2;ServCellPCI:649;Se... |
| 2024-09-20 22:21:37.876 | NRHandoverAttempt | SourcePCI:649;SourceNR-ARFC... |
| 2024-09-20 22:21:37.910 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.922 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.050 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.050 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255098 | 1 | 14.7572 | 10.6115 | -114.6123 | 10.2454 | 93.8009 | 0.0186 | 0.0129 |
| 2024_09_20 22:00 | 3241019 | 2 | 7.5082 | 10.6831 | -114.1206 | 10.7281 | 181.2232 | 0.0128 | 0.0142 |
| 2024_09_20 22:00 | 3236084 | 3 | 15.2892 | 12.4943 | -114.9738 | 14.3554 | 177.5452 | 0.0191 | 0.0101 |
| 2024_09_20 22:00 | 3234400 | 4 | 15.0589 | 15.9993 | -114.0411 | 18.8641 | 193.3500 | 0.0067 | 0.0109 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414506_326A8559 | 504990 | 345 | -89.7 | 504990 | 70 | -95.4 | 504990 | 21 | -98.7 | 504990 | 866 |
| MR_1774414506_D55C0568 | 504990 | 345 | -87.2 | 504990 | 70 | -95.9 | 504990 | 21 | -96.1 | 504990 | 866 |
| MR_1774414506_CCDBFA27 | 504990 | 345 | -89.9 | 504990 | 70 | -97.9 | 504990 | 21 | -98.6 | 504990 | 866 |
| MR_1774414506_110C5C43 | 504990 | 345 | -89.0 | 504990 | 70 | -96.0 | 504990 | 21 | -96.5 | 504990 | 866 |
| MR_1774414506_4AFCCCE1 | 504990 | 345 | -89.7 | 504990 | 70 | -98.2 | 504990 | 21 | -96.5 | 504990 | 866 |
| MR_1774414506_AEA000AB | 504990 | 345 | -89.9 | 504990 | 70 | -96.5 | 504990 | 21 | -98.2 | 504990 | 866 |
| MR_1774414506_838206C8 | 504990 | 345 | -86.8 | 504990 | 70 | -96.4 | 504990 | 21 | -99.4 | 504990 | 866 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1739: `6915143c-691...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6915143c-6918-4e15-8471-505c0bbe0308` |
| Tag | **multiple-answer** |
| 정답 | **C5|C9|C13|C19** |
| C5 의미 | Press down the tilt angle  of 3273482_5 by 3 degrees |
| C9 의미 | Increase A3 Offset threshold for 3220304_2 |
| C13 의미 | Decrease transmission power for 3273482_5 |
| C19 의미 | Increase A3 Offset threshold for 3273482_5 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1739] topology](images/train_1739.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3273482_5 by 3 degrees
- `C2`: Increase transmission power for 3273482_5
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Adjust the azimuth of 3273482_5 by 35 degrees
- `C5`: Press down the tilt angle  of 3273482_5 by 3 degrees **← 정답**
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220304_2
- `C7`: Adjust the azimuth of 3220304_2 by 35 degrees
- `C8`: Lift the tilt angle of 3220304_2 by 3 degrees
- `C9`: Increase A3 Offset threshold for 3220304_2 **← 정답**
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273482_5
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220304_2
- `C12`: Decrease A3 Offset threshold for 3273482_5
- `C13`: Decrease transmission power for 3273482_5 **← 정답**
- `C14`: Add neighbor relationship between 3245879_1 and 3273482_5
- `C15`: Decrease A3 Offset threshold for 3220304_2
- `C16`: Decrease transmission power for 3220304_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273482_5
- `C18`: Add neighbor relationship between 3220304_2 and 3273482_5
- `C19`: Increase A3 Offset threshold for 3273482_5 **← 정답**
- `C20`: Check test server and transmission issues
- `C21`: Press down the tilt angle of 3220304_2 by 3 degrees
- `C22`: Increase transmission power for 3220304_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.806 | MS1 | 121.4656607743 | 31.1446212942 | 823 | 504990 | -82.57 | 14.14 | 450.37 | 0.10 | 2.53 | 1580 |
| 2024-09-20 22:21:32.379 | MS1 | 121.4656615331 | 31.1446377967 | 823 | 504990 | -77.03 | 12.75 | 537.56 | 0.17 | 2.60 | 1587 |
| 2024-09-20 22:21:33.905 | MS1 | 121.4656746558 | 31.1446369406 | 823 | 504990 | -81.50 | 12.85 | 315.60 | 0.11 | 2.11 | 1594 |
| 2024-09-20 22:21:34.851 | MS1 | 121.4656609502 | 31.1446184477 | 376 | 504990 | -86.01 | 2.79 | 58.27 | 0.01 | 1.49 | 1564 |
| 2024-09-20 22:21:35.706 | MS1 | 121.4656749988 | 31.1446253939 | 376 | 504990 | -88.36 | 4.48 | 58.31 | 0.18 | 1.27 | 1580 |
| 2024-09-20 22:21:36.628 | MS1 | 121.4656746014 | 31.1446291814 | 823 | 504990 | -81.57 | 4.75 | 69.53 | 0.17 | 1.16 | 1586 |
| 2024-09-20 22:21:37.480 | MS1 | 121.4656627738 | 31.1446288868 | 823 | 504990 | -86.87 | 1.49 | 83.50 | 0.16 | 1.02 | 1593 |
| 2024-09-20 22:21:38.837 | MS1 | 121.4656638592 | 31.1446206224 | 376 | 504990 | -84.90 | 3.71 | 54.48 | 0.07 | 1.13 | 1592 |
| 2024-09-20 22:21:39.635 | MS1 | 121.4656714179 | 31.1446338732 | 376 | 504990 | -82.34 | 2.35 | 46.87 | 0.03 | 1.19 | 1579 |
| 2024-09-20 22:21:40.351 | MS1 | 121.4656653558 | 31.1446261344 | 376 | 504990 | -77.09 | 17.76 | 409.33 | 0.06 | 2.80 | 1583 |
| 2024-09-20 22:21:41.561 | MS1 | 121.4656700731 | 31.1446278906 | 376 | 504990 | -80.33 | 16.47 | 511.76 | 0.17 | 2.36 | 1589 |
| 2024-09-20 22:21:42.603 | MS1 | 121.4656756252 | 31.1446377498 | 376 | 504990 | -78.42 | 16.31 | 314.42 | 0.00 | 2.31 | 1579 |

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
| 3220304 | 2 | 121.4741162918 | 31.1529556892 | 186 | 2 | 11 | 23.5 | TDD | 823 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3236692 | 4 | 121.4684214150 | 31.1456065855 | 136 | 7 | 8 | 43.0 | TDD | 570 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3245879 | 1 | 121.4712438019 | 31.1517855378 | 225 | 1 | 5 | 45.9 | TDD | 596 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3254348 | 3 | 121.4732636314 | 31.1478401350 | 259 | 10 | 7 | 40.0 | TDD | 376 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3273482 | 5 | 121.4719712443 | 31.1477175060 | 275 | 1 | 4 | 18.7 | TDD | 735 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.294 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.314 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.416 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.416 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.121 | NREventA3 | measId:2;ServCellPCI:26;Ser... |
| 2024-09-20 22:21:34.361 | NRHandoverAttempt | SourcePCI:26;SourceNR-ARFCN... |
| 2024-09-20 22:21:34.393 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.406 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:34.520 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.520 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.121 | NREventA3 | measId:2;ServCellPCI:644;Se... |
| 2024-09-20 22:21:36.361 | NRHandoverAttempt | SourcePCI:644;SourceNR-ARFC... |
| 2024-09-20 22:21:36.401 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.414 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.535 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.535 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.121 | NREventA3 | measId:2;ServCellPCI:26;Ser... |
| 2024-09-20 22:21:38.361 | NRHandoverAttempt | SourcePCI:26;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.399 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.410 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.528 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.528 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245879 | 1 | 5.3783 | 16.0666 | -117.9033 | 7.3190 | 96.4324 | 0.0032 | 0.0197 |
| 2024_09_20 22:00 | 3220304 | 2 | 8.1826 | 19.4677 | -115.9202 | 11.0018 | 127.6773 | 0.0116 | 0.0115 |
| 2024_09_20 22:00 | 3254348 | 3 | 14.7689 | 5.4347 | -116.8067 | 10.5305 | 104.4548 | 0.0016 | 0.0090 |
| 2024_09_20 22:00 | 3236692 | 4 | 18.7725 | 8.7942 | -115.9250 | 18.7328 | 81.7861 | 0.0018 | 0.0009 |
| 2024_09_20 22:00 | 3273482 | 5 | 9.0800 | 7.2283 | -114.4018 | 9.6949 | 169.0453 | 0.0120 | 0.0069 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413354_283880FB | 504990 | 376 | -86.6 | 504990 | 823 | -84.8 | 504990 | 735 | -87.2 | 504990 | 596 |
| MR_1774413354_18918EA3 | 504990 | 376 | -85.1 | 504990 | 823 | -85.0 | 504990 | 735 | -88.6 | 504990 | 596 |
| MR_1774413354_75D03689 | 504990 | 376 | -87.0 | 504990 | 823 | -82.5 | 504990 | 735 | -87.9 | 504990 | 596 |
| MR_1774413354_1783975F | 504990 | 376 | -84.1 | 504990 | 823 | -82.1 | 504990 | 735 | -88.5 | 504990 | 596 |
| MR_1774413354_B37E567E | 504990 | 823 | -87.8 | 504990 | 376 | -84.3 | 504990 | 735 | -89.7 | 504990 | 596 |
| MR_1774413354_2418B443 | 504990 | 376 | -86.5 | 504990 | 823 | -85.4 | 504990 | 735 | -86.5 | 504990 | 596 |

> *... 2개 열 생략 (전체 14열)*

---
