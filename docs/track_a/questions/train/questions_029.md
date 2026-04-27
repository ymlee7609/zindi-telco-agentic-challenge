# Track A 문제 분석 — train[280]~train[289]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[280] ~ train[289] (10개)

## 목차

1. [문제 280: `1c759601-b6c...`](#280) — single-answer, 정답: C21
2. [문제 281: `da3e9f4e-ae0...`](#281) — single-answer, 정답: C1
3. [문제 282: `4a83c201-295...`](#282) — multiple-answer, 정답: C7|C17
4. [문제 283: `3223be40-ea5...`](#283) — single-answer, 정답: C8
5. [문제 284: `8b1805fc-1d2...`](#284) — single-answer, 정답: C13
6. [문제 285: `bbc0ac89-b28...`](#285) — single-answer, 정답: C7
7. [문제 286: `b11fb2e2-378...`](#286) — single-answer, 정답: C13
8. [문제 287: `ba229729-56f...`](#287) — single-answer, 정답: C9
9. [문제 288: `18b16782-4ec...`](#288) — single-answer, 정답: C18
10. [문제 289: `f3790a15-472...`](#289) — single-answer, 정답: C9

---

### 문제 280: `1c759601-b6c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1c759601-b6c6-41c4-a4aa-9a4d8f4b6db8` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257276_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[280] topology](images/train_0280.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3257276_5
- `C2`: Add neighbor relationship between 3257276_5 and 3233214_6
- `C3`: Increase A3 Offset threshold for 3233214_6
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233214_6
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257276_5
- `C6`: Check test server and transmission issues
- `C7`: Press down the tilt angle of 3257276_5 by 0 degrees
- `C8`: Increase transmission power for 3257276_5
- `C9`: Add neighbor relationship between 3232448_10 and 3233214_6
- `C10`: Adjust the azimuth of 3257276_5 by 45 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233214_6
- `C13`: Decrease A3 Offset threshold for 3233214_6
- `C14`: Press down the tilt angle  of 3233214_6 by 4 degrees
- `C15`: Lift the tilt angle of 3257276_5 by 0 degrees
- `C16`: Lift the tilt angle  of 3233214_6 by 4 degrees
- `C17`: Increase transmission power for 3233214_6
- `C18`: Decrease A3 Offset threshold for 3257276_5
- `C19`: Decrease transmission power for 3257276_5
- `C20`: Decrease transmission power for 3233214_6
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257276_5 **← 정답**
- `C22`: Adjust the azimuth of 3233214_6 by 36 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.433 | MS1 | 121.4656769757 | 31.1446236178 | 54 | 504990 | -93.88 | 10.92 | 313.55 | 0.12 | 2.73 | 1573 |
| 2024-09-20 22:21:32.501 | MS1 | 121.4656695817 | 31.1446242704 | 681 | 504990 | -95.01 | 11.83 | 346.81 | 0.03 | 2.36 | 1573 |
| 2024-09-20 22:21:33.469 | MS1 | 121.4656699576 | 31.1446187474 | 84 | 504990 | -95.41 | 9.15 | 405.05 | 0.18 | 2.30 | 1562 |
| 2024-09-20 22:21:34.282 | MS1 | 121.4656669377 | 31.1446315019 | 542 | 152650 | -89.64 | 2.79 | 51.47 | 0.18 | 1.71 | 992 |
| 2024-09-20 22:21:35.228 | MS1 | 121.4656709530 | 31.1446320134 | 619 | 152650 | -90.51 | 7.96 | 86.42 | 0.13 | 1.58 | 957 |
| 2024-09-20 22:21:36.697 | MS1 | 121.4656768706 | 31.1446199286 | 845 | 152650 | -94.79 | 5.62 | 85.15 | 0.16 | 1.88 | 919 |
| 2024-09-20 22:21:37.508 | MS1 | 121.4656584257 | 31.1446241002 | 487 | 152650 | -89.95 | 5.65 | 98.59 | 0.07 | 1.91 | 990 |
| 2024-09-20 22:21:38.598 | MS1 | 121.4656701779 | 31.1446239821 | 542 | 152650 | -96.90 | 4.91 | 68.51 | 0.01 | 1.86 | 950 |
| 2024-09-20 22:21:39.788 | MS1 | 121.4656758154 | 31.1446194039 | 619 | 152650 | -96.49 | 3.80 | 64.03 | 0.06 | 1.91 | 989 |
| 2024-09-20 22:21:40.444 | MS1 | 121.4656655043 | 31.1446184583 | 845 | 152650 | -92.84 | 5.67 | 69.87 | 0.19 | 2.42 | 1594 |
| 2024-09-20 22:21:41.167 | MS1 | 121.4656712356 | 31.1446290598 | 487 | 152650 | -87.23 | 6.08 | 52.59 | 0.13 | 2.76 | 1566 |
| 2024-09-20 22:21:42.476 | MS1 | 121.4656765505 | 31.1446247727 | 542 | 152650 | -87.27 | 6.50 | 97.79 | 0.05 | 2.83 | 1571 |

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
| 3210706 | 3 | 121.4666178761 | 31.1442454668 | 13 | 14 | 7 | 9.5 | TDD | 747 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3213556 | 12 | 121.4756350169 | 31.1516742942 | 103 | 12 | 7 | 23.5 | FDD | 59 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3220824 | 2 | 121.4749877120 | 31.1440117120 | 230 | 10 | 4 | 17.9 | TDD | 681 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3221878 | 1 | 121.4701887823 | 31.1449509654 | 82 | 2 | 9 | 5.6 | TDD | 416 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3232411 | 9 | 121.4643719060 | 31.1493539329 | 102 | 14 | 10 | 1.7 | FDD | 619 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3232448 | 10 | 121.4734537625 | 31.1478980477 | 246 | 9 | 8 | 11.0 | FDD | 845 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3233214 | 6 | 121.4740042117 | 31.1535716525 | 183 | 3 | 9 | 24.9 | TDD | 732 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3236389 | 8 | 121.4674763883 | 31.1538514443 | 58 | 10 | 9 | 5.0 | FDD | 487 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3237521 | 13 | 121.4660538350 | 31.1486520947 | 161 | 10 | 4 | 10.9 | FDD | 542 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3256915 | 4 | 121.4658908374 | 31.1519858684 | 91 | 9 | 7 | 3.1 | TDD | 84 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3257276 | 5 | 121.4693920527 | 31.1495173612 | 258 | 0 | 12 | 0.9 | TDD | 54 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3261081 | 7 | 121.4698229845 | 31.1490470642 | 60 | 10 | 0 | 6.4 | FDD | 742 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3262355 | 11 | 121.4727267840 | 31.1508890318 | 322 | 13 | 1 | 8.1 | FDD | 110 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |

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
| 2024-09-20 22:21:31.266 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.286 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.427 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.427 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.129 | NREventA2 | measId:1;ServCellPCI:674;Se... |
| 2024-09-20 22:21:35.254 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.498 | NREventA5 | measId:3;ServCellPCI:674;Se... |
| 2024-09-20 22:21:35.564 | NRHandoverAttempt | SourcePCI:674;SourceNR-ARFC... |
| 2024-09-20 22:21:35.594 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.605 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.743 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.743 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221878 | 1 | 8.2597 | 19.9206 | -117.2774 | 14.3198 | 166.1622 | 0.0126 | 0.0125 |
| 2024_09_20 22:00 | 3220824 | 2 | 7.4383 | 18.9382 | -114.9956 | 18.2068 | 81.0178 | 0.0096 | 0.0058 |
| 2024_09_20 22:00 | 3210706 | 3 | 15.9769 | 15.0909 | -114.4405 | 12.8539 | 154.7177 | 0.0117 | 0.0178 |
| 2024_09_20 22:00 | 3256915 | 4 | 9.8704 | 13.7070 | -116.1741 | 17.4910 | 99.6546 | 0.0084 | 0.0033 |
| 2024_09_20 22:00 | 3257276 | 5 | 14.2356 | 15.2691 | -115.3239 | 10.2438 | 131.1333 | 0.0010 | 0.0140 |
| 2024_09_20 22:00 | 3233214 | 6 | 10.6561 | 19.6098 | -116.3778 | 11.2712 | 96.6528 | 0.0182 | 0.0119 |
| 2024_09_20 22:00 | 3261081 | 7 | 19.5951 | 18.2595 | -114.7277 | 3.7020 | 37.5575 | 0.0073 | 0.0014 |
| 2024_09_20 22:00 | 3236389 | 8 | 5.3862 | 7.2959 | -115.3664 | 4.1995 | 23.1117 | 0.0162 | 0.0149 |
| 2024_09_20 22:00 | 3232411 | 9 | 6.5206 | 9.8327 | -114.0815 | 4.5337 | 20.6558 | 0.0051 | 0.0103 |
| 2024_09_20 22:00 | 3232448 | 10 | 15.5558 | 8.0206 | -115.9555 | 4.9961 | 36.4747 | 0.0139 | 0.0066 |
| 2024_09_20 22:00 | 3262355 | 11 | 11.1015 | 10.0365 | -116.1644 | 3.8143 | 30.7903 | 0.0010 | 0.0018 |
| 2024_09_20 22:00 | 3213556 | 12 | 8.8609 | 11.9510 | -115.2106 | 3.1396 | 28.5873 | 0.0200 | 0.0150 |
| 2024_09_20 22:00 | 3237521 | 13 | 8.3562 | 6.8214 | -114.5645 | 4.6810 | 25.2313 | 0.0130 | 0.0152 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415133_E40F7A33 | 152650 | 542 | -91.5 | 152650 | 59 | -92.5 | 152650 | 110 | -94.7 | 152650 | 742 |
| MR_1774415133_22380C76 | 152650 | 542 | -89.5 | 152650 | 59 | -92.7 | 152650 | 110 | -96.6 | 152650 | 742 |
| MR_1774415133_342B9656 | 504990 | 84 | -96.2 | 504990 | 732 | -90.2 | 504990 | 416 | -95.3 | 504990 | 747 |
| MR_1774415133_2098C3BD | 504990 | 84 | -96.6 | 504990 | 732 | -91.2 | 504990 | 416 | -95.6 | 504990 | 747 |
| MR_1774415133_1734B0A6 | 152650 | 542 | -90.0 | 152650 | 59 | -91.9 | 152650 | 110 | -94.8 | 152650 | 742 |
| MR_1774415133_2806E3D3 | 152650 | 542 | -88.8 | 152650 | 59 | -92.7 | 152650 | 110 | -95.4 | 152650 | 742 |
| MR_1774415133_C570A4C4 | 504990 | 84 | -95.0 | 504990 | 732 | -90.6 | 504990 | 416 | -97.1 | 504990 | 747 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 281: `da3e9f4e-ae0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `da3e9f4e-ae0d-4902-9375-bddbce160c5e` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Lift the tilt angle  of 3234315_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[281] topology](images/train_0281.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3234315_3 by 10 degrees **← 정답**
- `C2`: Decrease transmission power for 3250217_4
- `C3`: Press down the tilt angle of 3250217_4 by 2 degrees
- `C4`: Check test server and transmission issues
- `C5`: Decrease A3 Offset threshold for 3250217_4
- `C6`: Add neighbor relationship between 3234315_3 and 3268056_2
- `C7`: Press down the tilt angle  of 3234315_3 by 10 degrees
- `C8`: Lift the tilt angle of 3250217_4 by 2 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250217_4
- `C10`: Increase transmission power for 3268056_2
- `C11`: Adjust the azimuth of 3234315_3 by 50 degrees
- `C12`: Decrease A3 Offset threshold for 3268056_2
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Add neighbor relationship between 3250217_4 and 3268056_2
- `C15`: Increase transmission power for 3250217_4
- `C16`: Decrease transmission power for 3268056_2
- `C17`: Adjust the azimuth of 3250217_4 by 24 degrees
- `C18`: Increase A3 Offset threshold for 3268056_2
- `C19`: Increase A3 Offset threshold for 3250217_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250217_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268056_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268056_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.823 | MS1 | 121.4656754492 | 31.1446377186 | 323 | 504990 | -89.00 | 17.09 | 488.79 | 0.06 | 2.45 | 1592 |
| 2024-09-20 22:21:32.987 | MS1 | 121.4656651573 | 31.1446320135 | 323 | 504990 | -90.09 | 13.75 | 540.77 | 0.18 | 2.67 | 1584 |
| 2024-09-20 22:21:33.808 | MS1 | 121.4656713851 | 31.1446292822 | 323 | 504990 | -86.56 | 17.52 | 344.80 | 0.06 | 2.19 | 1588 |
| 2024-09-20 22:21:34.392 | MS1 | 121.4656696400 | 31.1446296833 | 323 | 504990 | -85.50 | 15.56 | 57.12 | 0.04 | 2.13 | 1588 |
| 2024-09-20 22:21:35.736 | MS1 | 121.4656731249 | 31.1446321613 | 323 | 504990 | -90.40 | 17.87 | 94.80 | 0.12 | 2.74 | 1584 |
| 2024-09-20 22:21:36.158 | MS1 | 121.4656769200 | 31.1446335451 | 323 | 504990 | -90.45 | 13.20 | 97.67 | 0.08 | 2.29 | 1560 |
| 2024-09-20 22:21:37.468 | MS1 | 121.4656646922 | 31.1446281227 | 323 | 504990 | -90.95 | 12.98 | 73.70 | 0.16 | 2.50 | 1576 |
| 2024-09-20 22:21:38.970 | MS1 | 121.4656701542 | 31.1446292347 | 323 | 504990 | -91.54 | 7.09 | 61.82 | 0.05 | 2.33 | 1592 |
| 2024-09-20 22:21:39.658 | MS1 | 121.4656737618 | 31.1446188387 | 323 | 504990 | -92.18 | 11.77 | 98.46 | 0.01 | 2.64 | 1561 |
| 2024-09-20 22:21:40.913 | MS1 | 121.4656706647 | 31.1446226632 | 323 | 504990 | -92.94 | 11.94 | 562.88 | 0.09 | 2.01 | 1589 |
| 2024-09-20 22:21:41.952 | MS1 | 121.4656646872 | 31.1446280173 | 323 | 504990 | -93.66 | 10.87 | 354.19 | 0.15 | 2.43 | 1590 |
| 2024-09-20 22:21:42.396 | MS1 | 121.4656664569 | 31.1446361574 | 323 | 504990 | -91.31 | 7.32 | 432.94 | 0.14 | 2.63 | 1561 |

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
| 3234315 | 3 | 121.4743374519 | 31.1499955155 | 350 | 14 | 12 | 37.3 | TDD | 786 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3240457 | 1 | 121.4739348261 | 31.1466963566 | 314 | 11 | 10 | 30.3 | TDD | 72 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3250217 | 4 | 121.4656666676 | 31.1510900143 | 156 | 0 | 11 | 22.3 | TDD | 323 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3268056 | 2 | 121.4741719536 | 31.1513091245 | 16 | 11 | 11 | 41.2 | TDD | 897 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.799 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.823 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.945 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.945 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.663 | NREventA3 | measId:2;ServCellPCI:144;Se... |
| 2024-09-20 22:21:37.903 | NRHandoverAttempt | SourcePCI:144;SourceNR-ARFC... |
| 2024-09-20 22:21:37.935 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.946 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.068 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.068 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240457 | 1 | 8.2137 | 9.4566 | -115.3293 | 6.6572 | 174.8272 | 0.0126 | 0.0009 |
| 2024_09_20 22:00 | 3268056 | 2 | 6.5657 | 15.0137 | -116.3574 | 13.6145 | 185.6158 | 0.0056 | 0.0182 |
| 2024_09_20 22:00 | 3234315 | 3 | 18.3725 | 13.0051 | -117.5342 | 6.3649 | 109.9575 | 0.0156 | 0.0170 |
| 2024_09_20 22:00 | 3250217 | 4 | 85.7619 | 76.2813 | -115.3206 | 11.4760 | 99.2014 | 0.0139 | 0.0116 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414385_3C98DB8C | 504990 | 323 | -84.5 | 504990 | 897 | -87.8 | 504990 | 786 | -95.2 | 504990 | 72 |
| MR_1774414385_78E575F2 | 504990 | 323 | -86.4 | 504990 | 897 | -87.8 | 504990 | 786 | -94.9 | 504990 | 72 |
| MR_1774414385_5B894DFE | 504990 | 323 | -85.1 | 504990 | 897 | -86.9 | 504990 | 786 | -96.1 | 504990 | 72 |
| MR_1774414385_45B4808E | 504990 | 323 | -86.1 | 504990 | 897 | -88.1 | 504990 | 786 | -94.4 | 504990 | 72 |
| MR_1774414385_CFA654D3 | 504990 | 323 | -84.7 | 504990 | 897 | -86.4 | 504990 | 786 | -95.4 | 504990 | 72 |
| MR_1774414385_E8D3C2C0 | 504990 | 323 | -84.9 | 504990 | 897 | -85.9 | 504990 | 786 | -95.9 | 504990 | 72 |
| MR_1774414385_57A0B0FD | 504990 | 323 | -86.2 | 504990 | 897 | -88.9 | 504990 | 786 | -94.5 | 504990 | 72 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 282: `4a83c201-295...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4a83c201-2956-466d-b5e0-32a06a09996c` |
| Tag | **multiple-answer** |
| 정답 | **C7|C17** |
| C7 의미 | Adjust the azimuth of 3216846_3 by 50 degrees |
| C17 의미 | Increase transmission power for 3216846_3 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[282] topology](images/train_0282.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3216846_3
- `C2`: Add neighbor relationship between 3277634_4 and 3243930_2
- `C3`: Check test server and transmission issues
- `C4`: Adjust the azimuth of 3243930_2 by 41 degrees
- `C5`: Add neighbor relationship between 3216846_3 and 3243930_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243930_2
- `C7`: Adjust the azimuth of 3216846_3 by 50 degrees **← 정답**
- `C8`: Increase transmission power for 3243930_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216846_3
- `C10`: Decrease A3 Offset threshold for 3216846_3
- `C11`: Lift the tilt angle of 3216846_3 by 10 degrees
- `C12`: Press down the tilt angle of 3216846_3 by 10 degrees
- `C13`: Increase A3 Offset threshold for 3243930_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216846_3
- `C15`: Decrease A3 Offset threshold for 3243930_2
- `C16`: Lift the tilt angle  of 3243930_2 by 5 degrees
- `C17`: Increase transmission power for 3216846_3 **← 정답**
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243930_2
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease transmission power for 3243930_2
- `C21`: Decrease transmission power for 3216846_3
- `C22`: Press down the tilt angle  of 3243930_2 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.338 | MS1 | 121.4656757987 | 31.1446212202 | 254 | 504990 | -93.34 | 14.54 | 524.56 | 0.13 | 2.78 | 1592 |
| 2024-09-20 22:21:32.978 | MS1 | 121.4656590670 | 31.1446183510 | 254 | 504990 | -87.70 | 15.42 | 445.32 | 0.19 | 2.09 | 1595 |
| 2024-09-20 22:21:33.858 | MS1 | 121.4656692393 | 31.1446302775 | 254 | 504990 | -86.82 | 12.41 | 372.65 | 0.07 | 2.93 | 1586 |
| 2024-09-20 22:21:34.595 | MS1 | 121.4656653266 | 31.1446225758 | 254 | 504990 | -104.47 | -1.25 | 45.79 | 0.10 | 1.19 | 1563 |
| 2024-09-20 22:21:35.771 | MS1 | 121.4656638773 | 31.1446234758 | 254 | 504990 | -107.57 | -1.30 | 26.41 | 0.11 | 1.43 | 1588 |
| 2024-09-20 22:21:36.134 | MS1 | 121.4656691865 | 31.1446273218 | 254 | 504990 | -109.78 | -0.75 | 29.48 | 0.06 | 1.02 | 1588 |
| 2024-09-20 22:21:37.383 | MS1 | 121.4656778397 | 31.1446210616 | 254 | 504990 | -109.40 | -1.19 | 80.93 | 0.07 | 1.36 | 1571 |
| 2024-09-20 22:21:38.162 | MS1 | 121.4656593892 | 31.1446367427 | 254 | 504990 | -100.42 | -1.22 | 25.38 | 0.14 | 1.42 | 1577 |
| 2024-09-20 22:21:39.662 | MS1 | 121.4656582059 | 31.1446341432 | 254 | 504990 | -104.71 | 0.81 | 17.02 | 0.10 | 1.00 | 1594 |
| 2024-09-20 22:21:40.554 | MS1 | 121.4656708845 | 31.1446261477 | 254 | 504990 | -85.43 | 13.64 | 375.88 | 0.08 | 2.39 | 1581 |
| 2024-09-20 22:21:41.828 | MS1 | 121.4656592315 | 31.1446192559 | 254 | 504990 | -92.95 | 15.67 | 350.04 | 0.09 | 2.32 | 1582 |
| 2024-09-20 22:21:42.321 | MS1 | 121.4656708319 | 31.1446184307 | 254 | 504990 | -94.12 | 17.36 | 319.13 | 0.20 | 2.81 | 1575 |

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
| 3216846 | 3 | 121.4711433266 | 31.1521913051 | 150 | 11 | 6 | 24.5 | TDD | 254 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3243930 | 2 | 121.4701402582 | 31.1450482754 | 305 | 2 | 11 | 22.3 | TDD | 655 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3277312 | 1 | 121.4745408160 | 31.1539112566 | 290 | 11 | 2 | 47.7 | TDD | 328 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3277634 | 4 | 121.4705185059 | 31.1462095914 | 145 | 4 | 0 | 16.5 | TDD | 15 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.280 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.295 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.400 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.400 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.660 | NREventA2 | measId:1;ServCellPCI:704;Se... |
| 2024-09-20 22:21:34.793 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277312 | 1 | 14.5961 | 5.9437 | -114.2037 | 14.7539 | 135.3626 | 0.0189 | 0.0142 |
| 2024_09_20 22:00 | 3243930 | 2 | 9.8266 | 13.6278 | -114.4238 | 13.6900 | 120.9268 | 0.0079 | 0.0008 |
| 2024_09_20 22:00 | 3216846 | 3 | 14.3549 | 5.5218 | -115.6670 | 13.8691 | 187.6704 | 0.1475 | 0.0029 |
| 2024_09_20 22:00 | 3277634 | 4 | 19.4642 | 8.1986 | -117.2312 | 17.1996 | 140.2607 | 0.0078 | 0.0062 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412421_95A53EC2 | 504990 | 254 | -105.2 | 504990 | 655 | -110.0 | 504990 | 15 | -120.0 | 504990 | 328 |
| MR_1774412421_2034E3D9 | 504990 | 254 | -106.2 | 504990 | 655 | -111.8 | 504990 | 15 | -118.9 | 504990 | 328 |
| MR_1774412421_B18C2E23 | 504990 | 254 | -105.0 | 504990 | 655 | -113.0 | 504990 | 15 | -119.2 | 504990 | 328 |
| MR_1774412421_17500A21 | 504990 | 254 | -104.9 | 504990 | 655 | -110.1 | 504990 | 15 | -119.3 | 504990 | 328 |
| MR_1774412421_1B71DA36 | 504990 | 254 | -105.2 | 504990 | 655 | -111.5 | 504990 | 15 | -120.8 | 504990 | 328 |
| MR_1774412421_5282C981 | 504990 | 254 | -106.1 | 504990 | 655 | -112.5 | 504990 | 15 | -121.2 | 504990 | 328 |
| MR_1774412421_F2910DE4 | 504990 | 254 | -104.8 | 504990 | 655 | -111.6 | 504990 | 15 | -117.8 | 504990 | 328 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 283: `3223be40-ea5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3223be40-ea56-4ea8-ba4a-392731afebd0` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[283] topology](images/train_0283.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276998_2
- `C3`: Increase transmission power for 3254333_4
- `C4`: Press down the tilt angle  of 3254333_4 by 10 degrees
- `C5`: Press down the tilt angle of 3276998_2 by 10 degrees
- `C6`: Adjust the azimuth of 3276998_2 by 11 degrees
- `C7`: Decrease transmission power for 3254333_4
- `C8`: Check test server and transmission issues **← 정답**
- `C9`: Decrease A3 Offset threshold for 3254333_4
- `C10`: Add neighbor relationship between 3214105_3 and 3254333_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276998_2
- `C12`: Lift the tilt angle  of 3254333_4 by 10 degrees
- `C13`: Increase transmission power for 3276998_2
- `C14`: Add neighbor relationship between 3276998_2 and 3254333_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254333_4
- `C16`: Decrease transmission power for 3276998_2
- `C17`: Lift the tilt angle of 3276998_2 by 10 degrees
- `C18`: Adjust the azimuth of 3254333_4 by 50 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254333_4
- `C20`: Increase A3 Offset threshold for 3254333_4
- `C21`: Increase A3 Offset threshold for 3276998_2
- `C22`: Decrease A3 Offset threshold for 3276998_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.330 | MS1 | 121.4656732461 | 31.1446279676 | 946 | 504990 | -90.99 | 16.29 | 360.72 | 0.19 | 2.74 | 1580 |
| 2024-09-20 22:21:32.599 | MS1 | 121.4656731130 | 31.1446248627 | 946 | 504990 | -87.47 | 12.02 | 596.26 | 0.17 | 2.69 | 1581 |
| 2024-09-20 22:21:33.571 | MS1 | 121.4656679057 | 31.1446327292 | 946 | 504990 | -91.69 | 14.81 | 346.21 | 0.19 | 2.99 | 1561 |
| 2024-09-20 22:21:34.731 | MS1 | 121.4656757538 | 31.1446338401 | 946 | 504990 | -86.96 | 12.04 | 79.20 | 0.02 | 2.26 | 312 |
| 2024-09-20 22:21:35.968 | MS1 | 121.4656619697 | 31.1446203800 | 946 | 504990 | -90.65 | 16.22 | 53.42 | 0.15 | 2.11 | 456 |
| 2024-09-20 22:21:36.390 | MS1 | 121.4656657068 | 31.1446225527 | 946 | 504990 | -91.84 | 13.76 | 83.31 | 0.13 | 2.61 | 432 |
| 2024-09-20 22:21:37.362 | MS1 | 121.4656699756 | 31.1446353015 | 946 | 504990 | -90.02 | 9.78 | 67.83 | 0.00 | 2.42 | 420 |
| 2024-09-20 22:21:38.811 | MS1 | 121.4656654178 | 31.1446351761 | 946 | 504990 | -92.87 | 9.89 | 91.55 | 0.03 | 2.47 | 345 |
| 2024-09-20 22:21:39.982 | MS1 | 121.4656725907 | 31.1446338049 | 946 | 504990 | -92.20 | 8.61 | 74.85 | 0.18 | 2.84 | 311 |
| 2024-09-20 22:21:40.973 | MS1 | 121.4656581939 | 31.1446193196 | 946 | 504990 | -90.82 | 8.72 | 427.81 | 0.02 | 2.78 | 1578 |
| 2024-09-20 22:21:41.445 | MS1 | 121.4656635239 | 31.1446316793 | 946 | 504990 | -89.14 | 10.99 | 320.53 | 0.14 | 2.10 | 1574 |
| 2024-09-20 22:21:42.304 | MS1 | 121.4656772884 | 31.1446309882 | 946 | 504990 | -90.65 | 8.80 | 327.63 | 0.15 | 2.25 | 1569 |

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
| 3214105 | 3 | 121.4694168187 | 31.1480409447 | 44 | 6 | 7 | 20.0 | TDD | 955 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3254333 | 4 | 121.4662138385 | 31.1506900858 | 288 | 15 | 6 | 20.6 | TDD | 900 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3266930 | 1 | 121.4685554517 | 31.1495271620 | 323 | 9 | 3 | 47.4 | TDD | 817 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3276998 | 2 | 121.4727871131 | 31.1498420677 | 218 | 11 | 7 | 21.5 | TDD | 946 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.569 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.590 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.729 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.729 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.403 | NREventA3 | measId:2;ServCellPCI:74;Ser... |
| 2024-09-20 22:21:38.643 | NRHandoverAttempt | SourcePCI:74;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.684 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.698 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.838 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.838 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266930 | 1 | 6.2020 | 13.3223 | -115.9870 | 14.0699 | 102.7110 | 0.0121 | 0.0150 |
| 2024_09_20 22:00 | 3276998 | 2 | 18.5285 | 18.5063 | -117.4456 | 12.3549 | 81.4791 | 0.0001 | 0.0133 |
| 2024_09_20 22:00 | 3214105 | 3 | 16.8307 | 8.3774 | -114.0681 | 11.2758 | 158.4541 | 0.0044 | 0.0116 |
| 2024_09_20 22:00 | 3254333 | 4 | 10.6119 | 7.1884 | -116.3696 | 13.9042 | 99.1741 | 0.0173 | 0.0087 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413966_4C495819 | 504990 | 946 | -86.8 | 504990 | 900 | -88.5 | 504990 | 955 | -94.0 | 504990 | 817 |
| MR_1774413966_4751FAFF | 504990 | 946 | -87.9 | 504990 | 900 | -85.7 | 504990 | 955 | -94.3 | 504990 | 817 |
| MR_1774413966_EE47E0F8 | 504990 | 946 | -86.3 | 504990 | 900 | -87.6 | 504990 | 955 | -94.1 | 504990 | 817 |
| MR_1774413966_2627E8AE | 504990 | 946 | -88.2 | 504990 | 900 | -85.3 | 504990 | 955 | -93.8 | 504990 | 817 |
| MR_1774413966_2082FEC5 | 504990 | 946 | -88.2 | 504990 | 900 | -84.8 | 504990 | 955 | -93.1 | 504990 | 817 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 284: `8b1805fc-1d2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8b1805fc-1d26-4946-b58b-d88b850b79bf` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[284] topology](images/train_0284.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3261341_4 and 3232209_1
- `C2`: Press down the tilt angle of 3211906_2 by 9 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211906_2
- `C4`: Adjust the azimuth of 3211906_2 by 44 degrees
- `C5`: Increase A3 Offset threshold for 3211906_2
- `C6`: Decrease A3 Offset threshold for 3211906_2
- `C7`: Decrease transmission power for 3232209_1
- `C8`: Adjust the azimuth of 3232209_1 by 50 degrees
- `C9`: Decrease A3 Offset threshold for 3232209_1
- `C10`: Lift the tilt angle  of 3232209_1 by 10 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232209_1
- `C12`: Increase transmission power for 3211906_2
- `C13`: Check test server and transmission issues **← 정답**
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232209_1
- `C16`: Press down the tilt angle  of 3232209_1 by 10 degrees
- `C17`: Lift the tilt angle of 3211906_2 by 9 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211906_2
- `C19`: Add neighbor relationship between 3211906_2 and 3232209_1
- `C20`: Increase A3 Offset threshold for 3232209_1
- `C21`: Decrease transmission power for 3211906_2
- `C22`: Increase transmission power for 3232209_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.576 | MS1 | 121.4656711592 | 31.1446200824 | 755 | 504990 | -85.15 | 17.55 | 520.60 | 0.10 | 2.02 | 1580 |
| 2024-09-20 22:21:32.252 | MS1 | 121.4656599757 | 31.1446272288 | 755 | 504990 | -89.91 | 17.30 | 563.98 | 0.02 | 2.01 | 1562 |
| 2024-09-20 22:21:33.729 | MS1 | 121.4656653829 | 31.1446283217 | 755 | 504990 | -85.76 | 14.53 | 483.82 | 0.19 | 2.19 | 1564 |
| 2024-09-20 22:21:34.119 | MS1 | 121.4656630562 | 31.1446259290 | 755 | 504990 | -91.24 | 12.86 | 85.76 | 0.08 | 2.21 | 389 |
| 2024-09-20 22:21:35.914 | MS1 | 121.4656651558 | 31.1446376499 | 755 | 504990 | -85.58 | 14.47 | 70.29 | 0.19 | 2.41 | 451 |
| 2024-09-20 22:21:36.466 | MS1 | 121.4656589839 | 31.1446259237 | 755 | 504990 | -90.54 | 14.30 | 74.29 | 0.06 | 2.90 | 401 |
| 2024-09-20 22:21:37.373 | MS1 | 121.4656640439 | 31.1446244529 | 755 | 504990 | -93.99 | 12.48 | 81.77 | 0.06 | 2.42 | 350 |
| 2024-09-20 22:21:38.822 | MS1 | 121.4656717129 | 31.1446231115 | 755 | 504990 | -89.13 | 9.62 | 80.99 | 0.03 | 2.67 | 360 |
| 2024-09-20 22:21:39.519 | MS1 | 121.4656743848 | 31.1446295374 | 755 | 504990 | -89.22 | 9.33 | 101.98 | 0.01 | 2.78 | 322 |
| 2024-09-20 22:21:40.131 | MS1 | 121.4656612583 | 31.1446260479 | 755 | 504990 | -90.35 | 7.32 | 489.49 | 0.01 | 2.90 | 1590 |
| 2024-09-20 22:21:41.284 | MS1 | 121.4656674917 | 31.1446333942 | 755 | 504990 | -92.65 | 12.88 | 433.48 | 0.19 | 2.29 | 1597 |
| 2024-09-20 22:21:42.526 | MS1 | 121.4656604526 | 31.1446360160 | 755 | 504990 | -89.33 | 12.88 | 494.14 | 0.15 | 3.00 | 1565 |

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
| 3211906 | 2 | 121.4724633316 | 31.1487346397 | 191 | 6 | 5 | 40.4 | TDD | 755 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3232209 | 1 | 121.4668510961 | 31.1449348876 | 11 | 10 | 1 | 36.3 | TDD | 97 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3253517 | 3 | 121.4728481535 | 31.1516661154 | 9 | 12 | 8 | 41.0 | TDD | 69 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3261341 | 4 | 121.4647751932 | 31.1553072691 | 260 | 11 | 8 | 37.2 | TDD | 966 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.173 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.194 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.331 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.331 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.995 | NREventA3 | measId:2;ServCellPCI:829;Se... |
| 2024-09-20 22:21:38.235 | NRHandoverAttempt | SourcePCI:829;SourceNR-ARFC... |
| 2024-09-20 22:21:38.276 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.287 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.432 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.432 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232209 | 1 | 11.3361 | 6.6246 | -115.4965 | 18.0101 | 193.0073 | 0.0049 | 0.0127 |
| 2024_09_20 22:00 | 3211906 | 2 | 15.9803 | 11.2493 | -117.5363 | 9.6032 | 138.0066 | 0.0087 | 0.0127 |
| 2024_09_20 22:00 | 3253517 | 3 | 9.5232 | 14.4717 | -117.9331 | 16.8272 | 133.6234 | 0.0054 | 0.0060 |
| 2024_09_20 22:00 | 3261341 | 4 | 18.7397 | 10.2514 | -115.5592 | 14.1276 | 134.4253 | 0.0146 | 0.0100 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412200_3F360A26 | 504990 | 755 | -91.0 | 504990 | 97 | -100.0 | 504990 | 966 | -103.4 | 504990 | 69 |
| MR_1774412200_691F8420 | 504990 | 755 | -92.0 | 504990 | 97 | -101.1 | 504990 | 966 | -102.1 | 504990 | 69 |
| MR_1774412200_15E66111 | 504990 | 755 | -92.7 | 504990 | 97 | -101.6 | 504990 | 966 | -101.7 | 504990 | 69 |
| MR_1774412200_7A09AB13 | 504990 | 755 | -91.7 | 504990 | 97 | -98.9 | 504990 | 966 | -100.0 | 504990 | 69 |
| MR_1774412200_130B895C | 504990 | 755 | -92.9 | 504990 | 97 | -99.9 | 504990 | 966 | -103.5 | 504990 | 69 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 285: `bbc0ac89-b28...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bbc0ac89-b28d-45ca-8653-f5d19fcbec4f` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[285] topology](images/train_0285.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247492_1
- `C2`: Decrease A3 Offset threshold for 3256151_3
- `C3`: Increase transmission power for 3247492_1
- `C4`: Add neighbor relationship between 3256151_3 and 3247492_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256151_3
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Check test server and transmission issues **← 정답**
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247492_1
- `C9`: Press down the tilt angle of 3256151_3 by 10 degrees
- `C10`: Increase A3 Offset threshold for 3247492_1
- `C11`: Add neighbor relationship between 3263085_4 and 3247492_1
- `C12`: Lift the tilt angle  of 3247492_1 by 4 degrees
- `C13`: Decrease transmission power for 3247492_1
- `C14`: Increase A3 Offset threshold for 3256151_3
- `C15`: Lift the tilt angle of 3256151_3 by 10 degrees
- `C16`: Decrease transmission power for 3256151_3
- `C17`: Increase transmission power for 3256151_3
- `C18`: Adjust the azimuth of 3247492_1 by 50 degrees
- `C19`: Press down the tilt angle  of 3247492_1 by 4 degrees
- `C20`: Adjust the azimuth of 3256151_3 by 50 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256151_3
- `C22`: Decrease A3 Offset threshold for 3247492_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.951 | MS1 | 121.4656631021 | 31.1446357360 | 18 | 504990 | -87.64 | 14.53 | 500.36 | 0.04 | 2.06 | 1595 |
| 2024-09-20 22:21:32.160 | MS1 | 121.4656667978 | 31.1446340464 | 18 | 504990 | -89.04 | 13.15 | 428.49 | 0.04 | 2.61 | 1576 |
| 2024-09-20 22:21:33.642 | MS1 | 121.4656698511 | 31.1446301175 | 18 | 504990 | -87.54 | 15.24 | 354.62 | 0.03 | 2.68 | 1564 |
| 2024-09-20 22:21:34.769 | MS1 | 121.4656654531 | 31.1446294094 | 18 | 504990 | -85.29 | 15.70 | 63.20 | 0.05 | 2.45 | 308 |
| 2024-09-20 22:21:35.216 | MS1 | 121.4656773820 | 31.1446290477 | 18 | 504990 | -85.01 | 14.59 | 94.19 | 0.00 | 2.95 | 302 |
| 2024-09-20 22:21:36.782 | MS1 | 121.4656743524 | 31.1446371137 | 18 | 504990 | -86.51 | 17.60 | 71.48 | 0.10 | 2.32 | 329 |
| 2024-09-20 22:21:37.530 | MS1 | 121.4656624034 | 31.1446378007 | 18 | 504990 | -91.94 | 9.30 | 102.72 | 0.07 | 2.28 | 439 |
| 2024-09-20 22:21:38.910 | MS1 | 121.4656681853 | 31.1446274872 | 18 | 504990 | -89.15 | 9.41 | 71.52 | 0.08 | 2.75 | 346 |
| 2024-09-20 22:21:39.868 | MS1 | 121.4656601113 | 31.1446359819 | 18 | 504990 | -89.71 | 11.59 | 65.65 | 0.11 | 2.09 | 414 |
| 2024-09-20 22:21:40.876 | MS1 | 121.4656724015 | 31.1446275612 | 18 | 504990 | -90.79 | 8.64 | 529.40 | 0.04 | 2.22 | 1572 |
| 2024-09-20 22:21:41.979 | MS1 | 121.4656640147 | 31.1446215621 | 18 | 504990 | -91.49 | 7.61 | 331.05 | 0.01 | 2.67 | 1589 |
| 2024-09-20 22:21:42.785 | MS1 | 121.4656590906 | 31.1446357116 | 18 | 504990 | -92.08 | 11.05 | 434.33 | 0.04 | 2.61 | 1577 |

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
| 3247492 | 1 | 121.4752677667 | 31.1529711261 | 290 | 3 | 1 | 17.8 | TDD | 671 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3256151 | 3 | 121.4670686153 | 31.1465990314 | 269 | 11 | 3 | 15.5 | TDD | 18 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3263085 | 4 | 121.4677646371 | 31.1548272326 | 231 | 3 | 12 | 30.7 | TDD | 639 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3272890 | 2 | 121.4701617798 | 31.1543915524 | 206 | 7 | 1 | 38.9 | TDD | 257 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.070 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.087 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.212 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.212 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.896 | NREventA3 | measId:2;ServCellPCI:358;Se... |
| 2024-09-20 22:21:38.136 | NRHandoverAttempt | SourcePCI:358;SourceNR-ARFC... |
| 2024-09-20 22:21:38.166 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.179 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.294 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.294 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247492 | 1 | 12.9020 | 6.4200 | -116.9368 | 18.9765 | 187.3319 | 0.0106 | 0.0001 |
| 2024_09_20 22:00 | 3272890 | 2 | 12.5278 | 7.1698 | -117.1877 | 14.9034 | 111.1875 | 0.0050 | 0.0076 |
| 2024_09_20 22:00 | 3256151 | 3 | 18.8227 | 18.3932 | -116.8338 | 6.6006 | 185.2326 | 0.0173 | 0.0136 |
| 2024_09_20 22:00 | 3263085 | 4 | 17.7714 | 11.0871 | -115.5020 | 5.5207 | 94.4991 | 0.0050 | 0.0143 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415262_BF02F9C9 | 504990 | 18 | -87.2 | 504990 | 671 | -92.2 | 504990 | 639 | -95.3 | 504990 | 257 |
| MR_1774415262_F84BB192 | 504990 | 18 | -86.5 | 504990 | 671 | -91.3 | 504990 | 639 | -96.3 | 504990 | 257 |
| MR_1774415262_F55D438D | 504990 | 18 | -83.6 | 504990 | 671 | -94.9 | 504990 | 639 | -95.6 | 504990 | 257 |
| MR_1774415262_2C57BB14 | 504990 | 18 | -83.6 | 504990 | 671 | -92.3 | 504990 | 639 | -93.1 | 504990 | 257 |
| MR_1774415262_E2884638 | 504990 | 18 | -85.1 | 504990 | 671 | -94.6 | 504990 | 639 | -96.5 | 504990 | 257 |
| MR_1774415262_9EEB2EBC | 504990 | 18 | -85.3 | 504990 | 671 | -94.2 | 504990 | 639 | -95.7 | 504990 | 257 |
| MR_1774415262_65B1B70A | 504990 | 18 | -86.5 | 504990 | 671 | -94.3 | 504990 | 639 | -94.0 | 504990 | 257 |
| MR_1774415262_76CDD343 | 504990 | 18 | -85.0 | 504990 | 671 | -93.9 | 504990 | 639 | -95.5 | 504990 | 257 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 286: `b11fb2e2-378...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b11fb2e2-3786-4b0d-b6f3-4a984c2bd425` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Lift the tilt angle  of 3229811_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[286] topology](images/train_0286.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3250834_3
- `C2`: Increase A3 Offset threshold for 3217633_4
- `C3`: Decrease A3 Offset threshold for 3217633_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250834_3
- `C5`: Lift the tilt angle of 3250834_3 by 5 degrees
- `C6`: Adjust the azimuth of 3229811_2 by 31 degrees
- `C7`: Press down the tilt angle  of 3229811_2 by 10 degrees
- `C8`: Check test server and transmission issues
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217633_4
- `C10`: Decrease transmission power for 3217633_4
- `C11`: Increase transmission power for 3250834_3
- `C12`: Press down the tilt angle of 3250834_3 by 5 degrees
- `C13`: Lift the tilt angle  of 3229811_2 by 10 degrees **← 정답**
- `C14`: Add neighbor relationship between 3250834_3 and 3217633_4
- `C15`: Adjust the azimuth of 3250834_3 by 40 degrees
- `C16`: Add neighbor relationship between 3229811_2 and 3217633_4
- `C17`: Increase A3 Offset threshold for 3250834_3
- `C18`: Increase transmission power for 3217633_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250834_3
- `C20`: Decrease transmission power for 3250834_3
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217633_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.438 | MS1 | 121.4656606887 | 31.1446225820 | 237 | 504990 | -87.20 | 16.26 | 537.76 | 0.11 | 2.13 | 1592 |
| 2024-09-20 22:21:32.964 | MS1 | 121.4656611483 | 31.1446190333 | 237 | 504990 | -86.97 | 17.58 | 519.26 | 0.06 | 2.49 | 1589 |
| 2024-09-20 22:21:33.936 | MS1 | 121.4656661407 | 31.1446311259 | 237 | 504990 | -91.04 | 17.96 | 545.95 | 0.06 | 2.30 | 1574 |
| 2024-09-20 22:21:34.625 | MS1 | 121.4656624259 | 31.1446363744 | 237 | 504990 | -87.95 | 12.16 | 92.42 | 0.02 | 2.35 | 1571 |
| 2024-09-20 22:21:35.161 | MS1 | 121.4656745477 | 31.1446188624 | 237 | 504990 | -88.87 | 12.20 | 50.51 | 0.04 | 2.58 | 1570 |
| 2024-09-20 22:21:36.639 | MS1 | 121.4656778993 | 31.1446370677 | 237 | 504990 | -85.07 | 15.31 | 65.76 | 0.18 | 2.20 | 1599 |
| 2024-09-20 22:21:37.917 | MS1 | 121.4656583906 | 31.1446209861 | 237 | 504990 | -90.73 | 11.85 | 76.50 | 0.05 | 2.17 | 1590 |
| 2024-09-20 22:21:38.477 | MS1 | 121.4656753216 | 31.1446262839 | 237 | 504990 | -89.29 | 10.25 | 82.72 | 0.07 | 2.44 | 1579 |
| 2024-09-20 22:21:39.257 | MS1 | 121.4656662893 | 31.1446250845 | 237 | 504990 | -92.41 | 9.04 | 106.13 | 0.19 | 2.31 | 1568 |
| 2024-09-20 22:21:40.813 | MS1 | 121.4656724634 | 31.1446234479 | 237 | 504990 | -91.32 | 8.59 | 354.17 | 0.15 | 2.50 | 1583 |
| 2024-09-20 22:21:41.412 | MS1 | 121.4656756069 | 31.1446335966 | 237 | 504990 | -92.97 | 10.56 | 415.76 | 0.01 | 2.36 | 1587 |
| 2024-09-20 22:21:42.468 | MS1 | 121.4656633685 | 31.1446288651 | 237 | 504990 | -92.31 | 7.98 | 489.10 | 0.05 | 2.62 | 1593 |

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
| 3217633 | 4 | 121.4713768642 | 31.1515335094 | 184 | 8 | 7 | 42.7 | TDD | 467 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3224048 | 1 | 121.4758808539 | 31.1552896422 | 329 | 0 | 4 | 20.4 | TDD | 226 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3229811 | 2 | 121.4696853578 | 31.1488590024 | 35 | 15 | 8 | 22.4 | TDD | 619 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3250834 | 3 | 121.4725088748 | 31.1495522288 | 190 | 2 | 7 | 44.8 | TDD | 237 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.517 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.534 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.682 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.682 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.337 | NREventA3 | measId:2;ServCellPCI:116;Se... |
| 2024-09-20 22:21:38.577 | NRHandoverAttempt | SourcePCI:116;SourceNR-ARFC... |
| 2024-09-20 22:21:38.615 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.630 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.779 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.779 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224048 | 1 | 12.0310 | 14.7427 | -115.9561 | 19.2921 | 158.0933 | 0.0057 | 0.0050 |
| 2024_09_20 22:00 | 3229811 | 2 | 6.0023 | 17.9343 | -116.2680 | 14.0304 | 160.9675 | 0.0029 | 0.0099 |
| 2024_09_20 22:00 | 3250834 | 3 | 77.2457 | 76.9860 | -116.1128 | 11.1924 | 80.8254 | 0.0172 | 0.0048 |
| 2024_09_20 22:00 | 3217633 | 4 | 16.3417 | 11.4129 | -115.3365 | 8.5184 | 119.8074 | 0.0119 | 0.0013 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413451_D2F6EC09 | 504990 | 237 | -89.5 | 504990 | 467 | -92.0 | 504990 | 619 | -103.2 | 504990 | 226 |
| MR_1774413451_E6E829F5 | 504990 | 237 | -88.3 | 504990 | 467 | -92.4 | 504990 | 619 | -103.1 | 504990 | 226 |
| MR_1774413451_6EB2B20E | 504990 | 237 | -89.3 | 504990 | 467 | -90.3 | 504990 | 619 | -101.8 | 504990 | 226 |
| MR_1774413451_844131E6 | 504990 | 237 | -88.4 | 504990 | 467 | -89.4 | 504990 | 619 | -102.9 | 504990 | 226 |
| MR_1774413451_25C3CB6B | 504990 | 237 | -86.8 | 504990 | 467 | -89.2 | 504990 | 619 | -101.4 | 504990 | 226 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 287: `ba229729-56f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ba229729-56ff-4676-ac60-5a1b59f83949` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Lift the tilt angle  of 3222399_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[287] topology](images/train_0287.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272752_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233493_2
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272752_4
- `C5`: Adjust the azimuth of 3222399_3 by 49 degrees
- `C6`: Increase A3 Offset threshold for 3233493_2
- `C7`: Check test server and transmission issues
- `C8`: Add neighbor relationship between 3233493_2 and 3272752_4
- `C9`: Lift the tilt angle  of 3222399_3 by 10 degrees **← 정답**
- `C10`: Adjust the azimuth of 3233493_2 by 31 degrees
- `C11`: Increase A3 Offset threshold for 3272752_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233493_2
- `C13`: Increase transmission power for 3233493_2
- `C14`: Press down the tilt angle of 3233493_2 by 3 degrees
- `C15`: Decrease transmission power for 3233493_2
- `C16`: Decrease A3 Offset threshold for 3272752_4
- `C17`: Increase transmission power for 3272752_4
- `C18`: Lift the tilt angle of 3233493_2 by 3 degrees
- `C19`: Decrease A3 Offset threshold for 3233493_2
- `C20`: Decrease transmission power for 3272752_4
- `C21`: Add neighbor relationship between 3222399_3 and 3272752_4
- `C22`: Press down the tilt angle  of 3222399_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.651 | MS1 | 121.4656773633 | 31.1446313555 | 177 | 504990 | -91.76 | 12.62 | 406.29 | 0.12 | 2.60 | 1584 |
| 2024-09-20 22:21:32.306 | MS1 | 121.4656763529 | 31.1446283833 | 177 | 504990 | -86.92 | 16.57 | 553.52 | 0.19 | 2.77 | 1568 |
| 2024-09-20 22:21:33.688 | MS1 | 121.4656606279 | 31.1446358572 | 177 | 504990 | -89.21 | 16.88 | 590.37 | 0.08 | 2.79 | 1596 |
| 2024-09-20 22:21:34.305 | MS1 | 121.4656683571 | 31.1446377346 | 177 | 504990 | -88.25 | 12.03 | 81.29 | 0.16 | 2.41 | 1563 |
| 2024-09-20 22:21:35.708 | MS1 | 121.4656752036 | 31.1446281576 | 177 | 504990 | -88.47 | 16.82 | 71.91 | 0.08 | 2.04 | 1592 |
| 2024-09-20 22:21:36.653 | MS1 | 121.4656609722 | 31.1446190414 | 177 | 504990 | -90.96 | 13.29 | 56.04 | 0.12 | 2.75 | 1595 |
| 2024-09-20 22:21:37.317 | MS1 | 121.4656649196 | 31.1446349678 | 177 | 504990 | -89.00 | 12.97 | 66.20 | 0.08 | 2.11 | 1590 |
| 2024-09-20 22:21:38.937 | MS1 | 121.4656684038 | 31.1446284433 | 177 | 504990 | -90.50 | 7.58 | 58.80 | 0.00 | 2.06 | 1596 |
| 2024-09-20 22:21:39.965 | MS1 | 121.4656609466 | 31.1446291398 | 177 | 504990 | -89.27 | 10.38 | 68.55 | 0.04 | 2.54 | 1562 |
| 2024-09-20 22:21:40.469 | MS1 | 121.4656680811 | 31.1446187397 | 177 | 504990 | -93.24 | 12.83 | 449.04 | 0.08 | 2.96 | 1591 |
| 2024-09-20 22:21:41.684 | MS1 | 121.4656676741 | 31.1446199259 | 177 | 504990 | -93.01 | 8.42 | 352.84 | 0.19 | 2.77 | 1567 |
| 2024-09-20 22:21:42.140 | MS1 | 121.4656600167 | 31.1446210891 | 177 | 504990 | -93.45 | 7.16 | 304.98 | 0.08 | 2.80 | 1583 |

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
| 3222399 | 3 | 121.4665695576 | 31.1483446207 | 89 | 13 | 2 | 31.5 | TDD | 212 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3233493 | 2 | 121.4749485129 | 31.1519325187 | 258 | 1 | 1 | 48.3 | TDD | 177 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3262188 | 1 | 121.4749708063 | 31.1518192855 | 113 | 9 | 0 | 22.8 | TDD | 280 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3272752 | 4 | 121.4701731437 | 31.1468278698 | 289 | 14 | 0 | 32.2 | TDD | 575 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.253 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.270 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.392 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.392 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.075 | NREventA3 | measId:2;ServCellPCI:122;Se... |
| 2024-09-20 22:21:38.315 | NRHandoverAttempt | SourcePCI:122;SourceNR-ARFC... |
| 2024-09-20 22:21:38.346 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.359 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.465 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.465 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262188 | 1 | 19.7337 | 19.0478 | -115.9325 | 5.5723 | 141.3973 | 0.0022 | 0.0110 |
| 2024_09_20 22:00 | 3233493 | 2 | 89.5117 | 87.5913 | -117.1071 | 11.6544 | 81.9484 | 0.0124 | 0.0166 |
| 2024_09_20 22:00 | 3222399 | 3 | 7.9741 | 12.2299 | -116.5885 | 18.8206 | 199.6789 | 0.0152 | 0.0169 |
| 2024_09_20 22:00 | 3272752 | 4 | 7.8391 | 13.3051 | -117.1113 | 11.8551 | 85.5983 | 0.0143 | 0.0039 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413616_7A23A222 | 504990 | 177 | -89.6 | 504990 | 575 | -91.0 | 504990 | 212 | -101.1 | 504990 | 280 |
| MR_1774413616_51BB5D64 | 504990 | 177 | -88.9 | 504990 | 575 | -88.2 | 504990 | 212 | -99.2 | 504990 | 280 |
| MR_1774413616_ABB49BCE | 504990 | 177 | -86.4 | 504990 | 575 | -91.4 | 504990 | 212 | -101.1 | 504990 | 280 |
| MR_1774413616_04929C90 | 504990 | 177 | -89.8 | 504990 | 575 | -88.5 | 504990 | 212 | -102.6 | 504990 | 280 |
| MR_1774413616_20054BA5 | 504990 | 177 | -87.3 | 504990 | 575 | -89.7 | 504990 | 212 | -101.7 | 504990 | 280 |
| MR_1774413616_D1A7FE19 | 504990 | 177 | -87.2 | 504990 | 575 | -89.2 | 504990 | 212 | -101.2 | 504990 | 280 |
| MR_1774413616_BAA3D539 | 504990 | 177 | -89.8 | 504990 | 575 | -87.9 | 504990 | 212 | -101.5 | 504990 | 280 |
| MR_1774413616_38364FF1 | 504990 | 177 | -88.4 | 504990 | 575 | -89.4 | 504990 | 212 | -102.3 | 504990 | 280 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 288: `18b16782-4ec...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `18b16782-4ec6-4fb9-9772-de7e14e0dab0` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Lift the tilt angle  of 3243879_1 by 6 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[288] topology](images/train_0288.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3249830_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218360_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249830_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218360_2
- `C5`: Adjust the azimuth of 3243879_1 by 43 degrees
- `C6`: Increase transmission power for 3218360_2
- `C7`: Add neighbor relationship between 3249830_4 and 3218360_2
- `C8`: Increase A3 Offset threshold for 3249830_4
- `C9`: Press down the tilt angle  of 3243879_1 by 6 degrees
- `C10`: Check test server and transmission issues
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase transmission power for 3249830_4
- `C13`: Adjust the azimuth of 3249830_4 by 50 degrees
- `C14`: Press down the tilt angle of 3249830_4 by 4 degrees
- `C15`: Decrease A3 Offset threshold for 3249830_4
- `C16`: Decrease transmission power for 3218360_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249830_4
- `C18`: Lift the tilt angle  of 3243879_1 by 6 degrees **← 정답**
- `C19`: Decrease A3 Offset threshold for 3218360_2
- `C20`: Add neighbor relationship between 3243879_1 and 3218360_2
- `C21`: Increase A3 Offset threshold for 3218360_2
- `C22`: Lift the tilt angle of 3249830_4 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.373 | MS1 | 121.4656773733 | 31.1446247848 | 764 | 504990 | -89.70 | 12.25 | 319.22 | 0.19 | 2.47 | 1589 |
| 2024-09-20 22:21:32.743 | MS1 | 121.4656630355 | 31.1446309904 | 764 | 504990 | -88.43 | 12.57 | 524.01 | 0.13 | 2.32 | 1571 |
| 2024-09-20 22:21:33.581 | MS1 | 121.4656660382 | 31.1446347386 | 764 | 504990 | -90.61 | 17.12 | 594.91 | 0.09 | 2.01 | 1594 |
| 2024-09-20 22:21:34.244 | MS1 | 121.4656696405 | 31.1446365793 | 764 | 504990 | -91.63 | 15.97 | 93.71 | 0.10 | 2.25 | 1576 |
| 2024-09-20 22:21:35.109 | MS1 | 121.4656715070 | 31.1446192864 | 764 | 504990 | -91.77 | 13.35 | 73.49 | 0.14 | 2.47 | 1597 |
| 2024-09-20 22:21:36.941 | MS1 | 121.4656635270 | 31.1446262480 | 764 | 504990 | -91.30 | 15.95 | 95.58 | 0.18 | 2.71 | 1591 |
| 2024-09-20 22:21:37.156 | MS1 | 121.4656698729 | 31.1446301429 | 764 | 504990 | -92.47 | 7.12 | 60.51 | 0.10 | 2.49 | 1597 |
| 2024-09-20 22:21:38.623 | MS1 | 121.4656766458 | 31.1446341783 | 764 | 504990 | -89.37 | 10.52 | 96.91 | 0.19 | 2.52 | 1586 |
| 2024-09-20 22:21:39.124 | MS1 | 121.4656753624 | 31.1446225239 | 764 | 504990 | -93.03 | 11.55 | 78.60 | 0.11 | 2.11 | 1570 |
| 2024-09-20 22:21:40.664 | MS1 | 121.4656712691 | 31.1446345110 | 764 | 504990 | -91.25 | 10.61 | 500.76 | 0.05 | 2.70 | 1579 |
| 2024-09-20 22:21:41.188 | MS1 | 121.4656734952 | 31.1446217529 | 764 | 504990 | -90.96 | 11.31 | 324.34 | 0.13 | 2.31 | 1566 |
| 2024-09-20 22:21:42.625 | MS1 | 121.4656739521 | 31.1446221839 | 764 | 504990 | -91.83 | 7.62 | 369.75 | 0.15 | 2.94 | 1581 |

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
| 3218360 | 2 | 121.4711192781 | 31.1482502543 | 189 | 4 | 10 | 25.4 | TDD | 349 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3243879 | 1 | 121.4651406742 | 31.1534341514 | 84 | 13 | 5 | 16.2 | TDD | 456 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3249830 | 4 | 121.4669703378 | 31.1494339911 | 243 | 1 | 1 | 25.1 | TDD | 764 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3272835 | 3 | 121.4655034896 | 31.1465989192 | 125 | 11 | 4 | 31.6 | TDD | 972 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.023 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.046 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.159 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.159 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.842 | NREventA3 | measId:2;ServCellPCI:995;Se... |
| 2024-09-20 22:21:38.082 | NRHandoverAttempt | SourcePCI:995;SourceNR-ARFC... |
| 2024-09-20 22:21:38.132 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.144 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.288 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.288 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243879 | 1 | 15.1045 | 11.1959 | -116.7745 | 12.2201 | 115.6745 | 0.0123 | 0.0150 |
| 2024_09_20 22:00 | 3218360 | 2 | 8.3089 | 11.2467 | -114.3940 | 17.2410 | 153.5989 | 0.0163 | 0.0075 |
| 2024_09_20 22:00 | 3272835 | 3 | 18.2920 | 12.1165 | -114.5433 | 7.8589 | 84.9791 | 0.0192 | 0.0094 |
| 2024_09_20 22:00 | 3249830 | 4 | 85.1578 | 78.1414 | -115.0908 | 19.7946 | 187.1770 | 0.0152 | 0.0060 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414469_74DE79CB | 504990 | 764 | -89.9 | 504990 | 349 | -98.8 | 504990 | 456 | -102.1 | 504990 | 972 |
| MR_1774414469_5594F03C | 504990 | 764 | -91.4 | 504990 | 349 | -97.4 | 504990 | 456 | -105.0 | 504990 | 972 |
| MR_1774414469_9CBA8AF9 | 504990 | 764 | -89.7 | 504990 | 349 | -95.0 | 504990 | 456 | -104.8 | 504990 | 972 |
| MR_1774414469_BD051AA7 | 504990 | 764 | -93.3 | 504990 | 349 | -97.8 | 504990 | 456 | -104.4 | 504990 | 972 |
| MR_1774414469_31311808 | 504990 | 764 | -93.3 | 504990 | 349 | -96.1 | 504990 | 456 | -104.8 | 504990 | 972 |
| MR_1774414469_5FE54753 | 504990 | 764 | -91.9 | 504990 | 349 | -98.2 | 504990 | 456 | -103.5 | 504990 | 972 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 289: `f3790a15-472...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f3790a15-4721-4614-95ea-ecead1f616c1` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease A3 Offset threshold for 3237532_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[289] topology](images/train_0289.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3256879_1 and 3225259_4
- `C2`: Increase A3 Offset threshold for 3237532_2
- `C3`: Lift the tilt angle  of 3225259_4 by 10 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237532_2
- `C5`: Decrease transmission power for 3237532_2
- `C6`: Adjust the azimuth of 3225259_4 by 50 degrees
- `C7`: Press down the tilt angle of 3237532_2 by 10 degrees
- `C8`: Press down the tilt angle  of 3225259_4 by 10 degrees
- `C9`: Decrease A3 Offset threshold for 3237532_2 **← 정답**
- `C10`: Check test server and transmission issues
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225259_4
- `C12`: Add neighbor relationship between 3237532_2 and 3225259_4
- `C13`: Adjust the azimuth of 3237532_2 by 50 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225259_4
- `C15`: Increase transmission power for 3225259_4
- `C16`: Increase A3 Offset threshold for 3225259_4
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase transmission power for 3237532_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237532_2
- `C20`: Decrease A3 Offset threshold for 3225259_4
- `C21`: Decrease transmission power for 3225259_4
- `C22`: Lift the tilt angle of 3237532_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.105 | MS1 | 121.4656708475 | 31.1446345598 | 900 | 504990 | -84.80 | 14.15 | 338.14 | 0.02 | 2.16 | 1598 |
| 2024-09-20 22:21:32.899 | MS1 | 121.4656727863 | 31.1446353301 | 900 | 504990 | -79.44 | 12.58 | 439.65 | 0.14 | 2.95 | 1575 |
| 2024-09-20 22:21:33.835 | MS1 | 121.4656753438 | 31.1446330069 | 900 | 504990 | -75.66 | 16.06 | 420.71 | 0.11 | 2.35 | 1571 |
| 2024-09-20 22:21:34.103 | MS1 | 121.4656647791 | 31.1446347487 | 900 | 504990 | -88.38 | -0.47 | 35.79 | 0.06 | 1.15 | 1560 |
| 2024-09-20 22:21:35.824 | MS1 | 121.4656679975 | 31.1446236545 | 900 | 504990 | -87.86 | -3.25 | 33.57 | 0.08 | 1.21 | 1580 |
| 2024-09-20 22:21:36.708 | MS1 | 121.4656740966 | 31.1446277260 | 900 | 504990 | -91.53 | -3.35 | 44.34 | 0.06 | 1.11 | 1564 |
| 2024-09-20 22:21:37.138 | MS1 | 121.4656608449 | 31.1446242830 | 900 | 504990 | -89.32 | -1.82 | 51.22 | 0.01 | 1.28 | 1589 |
| 2024-09-20 22:21:38.930 | MS1 | 121.4656590801 | 31.1446243638 | 900 | 504990 | -85.68 | -3.05 | 27.12 | 0.14 | 1.37 | 1569 |
| 2024-09-20 22:21:39.330 | MS1 | 121.4656627147 | 31.1446255148 | 598 | 504990 | -82.02 | 15.45 | 279.72 | 0.04 | 1.41 | 1587 |
| 2024-09-20 22:21:40.648 | MS1 | 121.4656740357 | 31.1446237763 | 598 | 504990 | -75.43 | 17.78 | 413.91 | 0.04 | 2.90 | 1569 |
| 2024-09-20 22:21:41.400 | MS1 | 121.4656601560 | 31.1446196755 | 598 | 504990 | -75.52 | 16.55 | 480.34 | 0.15 | 2.10 | 1592 |
| 2024-09-20 22:21:42.105 | MS1 | 121.4656702099 | 31.1446320780 | 598 | 504990 | -80.90 | 16.24 | 408.91 | 0.05 | 2.97 | 1561 |

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
| 3221507 | 3 | 121.4641436716 | 31.1533788697 | 123 | 1 | 8 | 29.9 | TDD | 781 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3225259 | 4 | 121.4720630729 | 31.1499170556 | 155 | 7 | 10 | 39.0 | TDD | 598 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3237532 | 2 | 121.4680949559 | 31.1492132925 | 51 | 13 | 5 | 42.8 | TDD | 900 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3256879 | 1 | 121.4758713607 | 31.1514079103 | 174 | 10 | 6 | 20.8 | TDD | 201 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.944 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.962 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.095 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.095 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.810 | NREventA3 | measId:2;ServCellPCI:282;Se... |
| 2024-09-20 22:21:38.050 | NRHandoverAttempt | SourcePCI:282;SourceNR-ARFC... |
| 2024-09-20 22:21:38.080 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.094 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.230 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.230 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256879 | 1 | 18.7083 | 12.0618 | -114.5594 | 18.0190 | 167.3777 | 0.0157 | 0.0142 |
| 2024_09_20 22:00 | 3237532 | 2 | 6.3161 | 13.5309 | -116.0706 | 9.3570 | 180.1544 | 0.0007 | 0.1826 |
| 2024_09_20 22:00 | 3221507 | 3 | 14.7616 | 14.3323 | -115.6569 | 16.3814 | 148.5868 | 0.0069 | 0.0046 |
| 2024_09_20 22:00 | 3225259 | 4 | 9.6186 | 8.8539 | -115.3469 | 19.8127 | 104.5469 | 0.0111 | 0.0024 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414054_F2E38630 | 504990 | 900 | -87.0 | 504990 | 598 | -84.6 | 504990 | 201 | -81.8 | 504990 | 781 |
| MR_1774414054_B26B375D | 504990 | 900 | -88.8 | 504990 | 598 | -81.1 | 504990 | 201 | -83.8 | 504990 | 781 |
| MR_1774414054_0ED89D60 | 504990 | 598 | -81.3 | 504990 | 900 | -88.0 | 504990 | 201 | -84.6 | 504990 | 781 |
| MR_1774414054_C880ECC8 | 504990 | 900 | -89.0 | 504990 | 598 | -81.0 | 504990 | 201 | -81.7 | 504990 | 781 |
| MR_1774414054_7ABA5732 | 504990 | 900 | -86.7 | 504990 | 598 | -81.2 | 504990 | 201 | -82.5 | 504990 | 781 |
| MR_1774414054_18423FFE | 504990 | 900 | -88.0 | 504990 | 598 | -83.7 | 504990 | 201 | -82.1 | 504990 | 781 |
| MR_1774414054_BF682734 | 504990 | 900 | -87.2 | 504990 | 598 | -83.5 | 504990 | 201 | -81.8 | 504990 | 781 |

> *... 2개 열 생략 (전체 14열)*

---
