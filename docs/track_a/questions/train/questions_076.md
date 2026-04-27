# Track A 문제 분석 — train[750]~train[759]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[750] ~ train[759] (10개)

## 목차

1. [문제 750: `e59447d0-140...`](#750) — single-answer, 정답: C3
2. [문제 751: `9db58ac7-3f1...`](#751) — single-answer, 정답: C11
3. [문제 752: `8f4038cc-e40...`](#752) — single-answer, 정답: C7
4. [문제 753: `72ebd516-e82...`](#753) — single-answer, 정답: C14
5. [문제 754: `f1776955-d3b...`](#754) — single-answer, 정답: C22
6. [문제 755: `4c95d882-f56...`](#755) — single-answer, 정답: C15
7. [문제 756: `4541ed8c-d7b...`](#756) — single-answer, 정답: C9
8. [문제 757: `c77ea585-cd6...`](#757) — single-answer, 정답: C7
9. [문제 758: `53018b61-ab0...`](#758) — single-answer, 정답: C12
10. [문제 759: `ff55e947-d77...`](#759) — single-answer, 정답: C8

---

### 문제 750: `e59447d0-140...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e59447d0-140b-4851-a81e-085ebc511a99` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[750] topology](images/train_0750.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3262124_2
- `C2`: Adjust the azimuth of 3258855_1 by 50 degrees
- `C3`: Check test server and transmission issues **← 정답**
- `C4`: Decrease A3 Offset threshold for 3262124_2
- `C5`: Increase transmission power for 3258855_1
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258855_1
- `C8`: Add neighbor relationship between 3262124_2 and 3258855_1
- `C9`: Decrease A3 Offset threshold for 3258855_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262124_2
- `C11`: Increase transmission power for 3262124_2
- `C12`: Increase A3 Offset threshold for 3262124_2
- `C13`: Increase A3 Offset threshold for 3258855_1
- `C14`: Press down the tilt angle  of 3258855_1 by 10 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262124_2
- `C16`: Adjust the azimuth of 3262124_2 by 50 degrees
- `C17`: Lift the tilt angle  of 3258855_1 by 10 degrees
- `C18`: Add neighbor relationship between 3257696_3 and 3258855_1
- `C19`: Lift the tilt angle of 3262124_2 by 10 degrees
- `C20`: Press down the tilt angle of 3262124_2 by 10 degrees
- `C21`: Decrease transmission power for 3258855_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258855_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.742 | MS1 | 121.4656692754 | 31.1446187615 | 753 | 504990 | -90.67 | 15.32 | 547.03 | 0.12 | 2.22 | 1567 |
| 2024-09-20 22:21:32.405 | MS1 | 121.4656635817 | 31.1446373529 | 753 | 504990 | -90.60 | 13.68 | 598.73 | 0.11 | 2.63 | 1565 |
| 2024-09-20 22:21:33.327 | MS1 | 121.4656765921 | 31.1446344473 | 753 | 504990 | -90.42 | 12.46 | 357.93 | 0.10 | 2.64 | 1562 |
| 2024-09-20 22:21:34.838 | MS1 | 121.4656633399 | 31.1446358130 | 753 | 504990 | -90.13 | 12.46 | 88.31 | 0.07 | 2.46 | 371 |
| 2024-09-20 22:21:35.134 | MS1 | 121.4656760064 | 31.1446372333 | 753 | 504990 | -91.94 | 16.29 | 70.02 | 0.15 | 2.20 | 318 |
| 2024-09-20 22:21:36.324 | MS1 | 121.4656729419 | 31.1446293652 | 753 | 504990 | -91.57 | 17.25 | 85.54 | 0.06 | 2.55 | 365 |
| 2024-09-20 22:21:37.548 | MS1 | 121.4656765717 | 31.1446220963 | 753 | 504990 | -91.45 | 11.36 | 59.86 | 0.13 | 2.66 | 352 |
| 2024-09-20 22:21:38.892 | MS1 | 121.4656741141 | 31.1446318211 | 753 | 504990 | -91.11 | 10.31 | 101.93 | 0.07 | 2.81 | 457 |
| 2024-09-20 22:21:39.774 | MS1 | 121.4656756171 | 31.1446217739 | 753 | 504990 | -91.34 | 10.16 | 51.74 | 0.11 | 2.55 | 470 |
| 2024-09-20 22:21:40.922 | MS1 | 121.4656630871 | 31.1446295612 | 753 | 504990 | -90.05 | 9.76 | 483.95 | 0.12 | 3.00 | 1577 |
| 2024-09-20 22:21:41.616 | MS1 | 121.4656629281 | 31.1446183949 | 753 | 504990 | -89.39 | 8.66 | 493.36 | 0.08 | 2.86 | 1573 |
| 2024-09-20 22:21:42.157 | MS1 | 121.4656700724 | 31.1446341316 | 753 | 504990 | -93.16 | 10.66 | 481.59 | 0.04 | 2.93 | 1568 |

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
| 3257696 | 3 | 121.4751383594 | 31.1549474275 | 165 | 13 | 1 | 32.1 | TDD | 153 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3258855 | 1 | 121.4669631990 | 31.1486178043 | 353 | 9 | 11 | 35.2 | TDD | 267 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3262124 | 2 | 121.4746627595 | 31.1542211563 | 294 | 12 | 7 | 23.4 | TDD | 753 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3273650 | 4 | 121.4754573149 | 31.1525268868 | 71 | 13 | 6 | 20.8 | TDD | 595 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.465 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.480 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.604 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.604 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.353 | NREventA3 | measId:2;ServCellPCI:542;Se... |
| 2024-09-20 22:21:38.593 | NRHandoverAttempt | SourcePCI:542;SourceNR-ARFC... |
| 2024-09-20 22:21:38.635 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.650 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.755 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.755 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258855 | 1 | 11.5974 | 15.5089 | -114.2490 | 19.3778 | 169.8667 | 0.0147 | 0.0176 |
| 2024_09_20 22:00 | 3262124 | 2 | 5.1643 | 6.8701 | -116.1829 | 17.0376 | 137.5199 | 0.0028 | 0.0082 |
| 2024_09_20 22:00 | 3257696 | 3 | 11.9720 | 17.8094 | -116.3589 | 8.6175 | 88.3134 | 0.0069 | 0.0184 |
| 2024_09_20 22:00 | 3273650 | 4 | 13.2143 | 10.2075 | -116.1501 | 10.8573 | 110.4561 | 0.0133 | 0.0135 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412594_9AEE9767 | 504990 | 753 | -91.0 | 504990 | 267 | -97.0 | 504990 | 153 | -100.8 | 504990 | 595 |
| MR_1774412594_72AD2E1D | 504990 | 753 | -89.9 | 504990 | 267 | -94.8 | 504990 | 153 | -100.6 | 504990 | 595 |
| MR_1774412594_3596728E | 504990 | 753 | -88.9 | 504990 | 267 | -96.5 | 504990 | 153 | -100.4 | 504990 | 595 |
| MR_1774412594_86557EA5 | 504990 | 753 | -88.2 | 504990 | 267 | -93.8 | 504990 | 153 | -100.7 | 504990 | 595 |
| MR_1774412594_D5850C74 | 504990 | 753 | -89.3 | 504990 | 267 | -96.4 | 504990 | 153 | -101.8 | 504990 | 595 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 751: `9db58ac7-3f1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9db58ac7-3f1b-4cfb-bf60-0121293e5546` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease A3 Offset threshold for 3210425_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[751] topology](images/train_0751.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3248500_1
- `C2`: Press down the tilt angle of 3210425_4 by 10 degrees
- `C3`: Adjust the azimuth of 3248500_1 by 17 degrees
- `C4`: Decrease transmission power for 3210425_4
- `C5`: Lift the tilt angle  of 3248500_1 by 5 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248500_1
- `C7`: Increase A3 Offset threshold for 3248500_1
- `C8`: Add neighbor relationship between 3248624_2 and 3248500_1
- `C9`: Add neighbor relationship between 3210425_4 and 3248500_1
- `C10`: Increase A3 Offset threshold for 3210425_4
- `C11`: Decrease A3 Offset threshold for 3210425_4 **← 정답**
- `C12`: Increase transmission power for 3248500_1
- `C13`: Increase transmission power for 3210425_4
- `C14`: Decrease A3 Offset threshold for 3248500_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248500_1
- `C16`: Press down the tilt angle  of 3248500_1 by 5 degrees
- `C17`: Adjust the azimuth of 3210425_4 by 50 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210425_4
- `C19`: Check test server and transmission issues
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210425_4
- `C22`: Lift the tilt angle of 3210425_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.482 | MS1 | 121.4656699426 | 31.1446342560 | 814 | 504990 | -82.82 | 17.54 | 514.91 | 0.08 | 2.93 | 1567 |
| 2024-09-20 22:21:32.687 | MS1 | 121.4656590623 | 31.1446370173 | 814 | 504990 | -75.64 | 15.49 | 540.07 | 0.17 | 2.19 | 1583 |
| 2024-09-20 22:21:33.914 | MS1 | 121.4656754622 | 31.1446243093 | 814 | 504990 | -80.24 | 16.81 | 325.62 | 0.17 | 2.50 | 1598 |
| 2024-09-20 22:21:34.439 | MS1 | 121.4656686789 | 31.1446322823 | 814 | 504990 | -91.03 | -3.91 | 57.60 | 0.11 | 1.08 | 1599 |
| 2024-09-20 22:21:35.999 | MS1 | 121.4656770470 | 31.1446236314 | 814 | 504990 | -92.26 | -3.99 | 77.08 | 0.09 | 1.25 | 1567 |
| 2024-09-20 22:21:36.273 | MS1 | 121.4656652032 | 31.1446315585 | 814 | 504990 | -85.75 | -3.69 | 44.12 | 0.04 | 1.21 | 1588 |
| 2024-09-20 22:21:37.578 | MS1 | 121.4656644503 | 31.1446285628 | 814 | 504990 | -90.13 | -2.62 | 57.34 | 0.03 | 1.30 | 1567 |
| 2024-09-20 22:21:38.538 | MS1 | 121.4656706696 | 31.1446301167 | 814 | 504990 | -90.50 | -2.56 | 51.06 | 0.09 | 1.45 | 1583 |
| 2024-09-20 22:21:39.769 | MS1 | 121.4656608160 | 31.1446279886 | 164 | 504990 | -83.52 | 14.77 | 176.08 | 0.07 | 1.17 | 1582 |
| 2024-09-20 22:21:40.617 | MS1 | 121.4656605076 | 31.1446293558 | 164 | 504990 | -75.98 | 16.77 | 369.45 | 0.14 | 2.49 | 1598 |
| 2024-09-20 22:21:41.521 | MS1 | 121.4656691096 | 31.1446312154 | 164 | 504990 | -84.53 | 12.60 | 404.01 | 0.09 | 2.59 | 1569 |
| 2024-09-20 22:21:42.541 | MS1 | 121.4656647791 | 31.1446251741 | 164 | 504990 | -83.08 | 17.40 | 325.14 | 0.11 | 2.21 | 1578 |

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
| 3210425 | 4 | 121.4693365773 | 31.1466252618 | 22 | 10 | 9 | 37.4 | TDD | 814 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3248500 | 1 | 121.4712696811 | 31.1460577201 | 270 | 2 | 11 | 28.3 | TDD | 164 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3248624 | 2 | 121.4666391405 | 31.1557436204 | 107 | 12 | 5 | 18.0 | TDD | 404 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3254477 | 3 | 121.4646377277 | 31.1542289500 | 311 | 9 | 7 | 32.7 | TDD | 765 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.440 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.561 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.561 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.281 | NREventA3 | measId:2;ServCellPCI:210;Se... |
| 2024-09-20 22:21:38.521 | NRHandoverAttempt | SourcePCI:210;SourceNR-ARFC... |
| 2024-09-20 22:21:38.554 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.569 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.696 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.696 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248500 | 1 | 9.9510 | 17.9821 | -116.6160 | 19.6014 | 193.6901 | 0.0181 | 0.0153 |
| 2024_09_20 22:00 | 3248624 | 2 | 13.5554 | 10.2688 | -117.7840 | 14.2453 | 124.5431 | 0.0033 | 0.0200 |
| 2024_09_20 22:00 | 3254477 | 3 | 16.9504 | 10.2909 | -114.9729 | 16.8376 | 161.6786 | 0.0180 | 0.0196 |
| 2024_09_20 22:00 | 3210425 | 4 | 10.7033 | 13.7885 | -115.4224 | 10.3134 | 144.8793 | 0.0050 | 0.1197 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413911_2B309442 | 504990 | 164 | -86.3 | 504990 | 814 | -90.4 | 504990 | 404 | -89.8 | 504990 | 765 |
| MR_1774413911_EBB97862 | 504990 | 164 | -86.3 | 504990 | 814 | -92.9 | 504990 | 404 | -86.5 | 504990 | 765 |
| MR_1774413911_1B501FF9 | 504990 | 164 | -85.6 | 504990 | 814 | -89.2 | 504990 | 404 | -87.7 | 504990 | 765 |
| MR_1774413911_4983B760 | 504990 | 814 | -90.8 | 504990 | 164 | -87.5 | 504990 | 404 | -86.4 | 504990 | 765 |
| MR_1774413911_2B9D74C5 | 504990 | 814 | -89.3 | 504990 | 164 | -85.6 | 504990 | 404 | -86.9 | 504990 | 765 |
| MR_1774413911_FF402617 | 504990 | 814 | -90.8 | 504990 | 164 | -86.6 | 504990 | 404 | -87.4 | 504990 | 765 |
| MR_1774413911_A07AFD3E | 504990 | 814 | -90.4 | 504990 | 164 | -87.5 | 504990 | 404 | -88.6 | 504990 | 765 |
| MR_1774413911_6ED059D6 | 504990 | 814 | -92.8 | 504990 | 164 | -86.7 | 504990 | 404 | -88.9 | 504990 | 765 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 752: `8f4038cc-e40...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8f4038cc-e400-481f-ab32-369692f67096` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217243_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[752] topology](images/train_0752.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3212735_2 by 2 degrees
- `C2`: Increase A3 Offset threshold for 3217243_4
- `C3`: Add neighbor relationship between 3255456_8 and 3212735_2
- `C4`: Increase transmission power for 3212735_2
- `C5`: Adjust the azimuth of 3212735_2 by 0 degrees
- `C6`: Lift the tilt angle  of 3212735_2 by 2 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217243_4 **← 정답**
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Add neighbor relationship between 3217243_4 and 3212735_2
- `C10`: Increase transmission power for 3217243_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217243_4
- `C12`: Adjust the azimuth of 3217243_4 by 39 degrees
- `C13`: Press down the tilt angle of 3217243_4 by 5 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212735_2
- `C15`: Decrease transmission power for 3212735_2
- `C16`: Increase A3 Offset threshold for 3212735_2
- `C17`: Decrease A3 Offset threshold for 3217243_4
- `C18`: Lift the tilt angle of 3217243_4 by 5 degrees
- `C19`: Decrease transmission power for 3217243_4
- `C20`: Decrease A3 Offset threshold for 3212735_2
- `C21`: Check test server and transmission issues
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212735_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.451 | MS1 | 121.4656679078 | 31.1446330815 | 115 | 504990 | -95.52 | 9.14 | 361.52 | 0.06 | 2.71 | 1590 |
| 2024-09-20 22:21:32.764 | MS1 | 121.4656632658 | 31.1446259985 | 582 | 504990 | -94.64 | 11.02 | 498.11 | 0.04 | 2.77 | 1570 |
| 2024-09-20 22:21:33.474 | MS1 | 121.4656724828 | 31.1446276181 | 26 | 504990 | -95.74 | 11.34 | 328.02 | 0.01 | 2.18 | 1574 |
| 2024-09-20 22:21:34.138 | MS1 | 121.4656704185 | 31.1446357807 | 774 | 152650 | -88.50 | 3.10 | 48.05 | 0.07 | 1.65 | 984 |
| 2024-09-20 22:21:35.720 | MS1 | 121.4656690177 | 31.1446364860 | 307 | 152650 | -87.84 | 3.67 | 66.67 | 0.15 | 1.74 | 996 |
| 2024-09-20 22:21:36.115 | MS1 | 121.4656642475 | 31.1446227553 | 326 | 152650 | -87.73 | 2.53 | 58.43 | 0.10 | 1.58 | 939 |
| 2024-09-20 22:21:37.407 | MS1 | 121.4656634676 | 31.1446240928 | 484 | 152650 | -96.35 | 3.96 | 86.80 | 0.08 | 1.99 | 911 |
| 2024-09-20 22:21:38.896 | MS1 | 121.4656671580 | 31.1446281996 | 774 | 152650 | -89.82 | 3.72 | 66.40 | 0.08 | 1.54 | 993 |
| 2024-09-20 22:21:39.417 | MS1 | 121.4656735776 | 31.1446180000 | 307 | 152650 | -95.33 | 6.51 | 63.74 | 0.15 | 1.65 | 926 |
| 2024-09-20 22:21:40.701 | MS1 | 121.4656648036 | 31.1446253582 | 326 | 152650 | -96.49 | 2.62 | 57.45 | 0.05 | 2.64 | 1575 |
| 2024-09-20 22:21:41.997 | MS1 | 121.4656738653 | 31.1446330054 | 484 | 152650 | -91.62 | 2.03 | 77.91 | 0.10 | 2.51 | 1579 |
| 2024-09-20 22:21:42.569 | MS1 | 121.4656692126 | 31.1446300197 | 774 | 152650 | -91.56 | 4.91 | 81.09 | 0.19 | 2.07 | 1590 |

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
| 3210024 | 13 | 121.4700575088 | 31.1535159485 | 78 | 3 | 11 | 3.7 | FDD | 180 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3211005 | 9 | 121.4745761188 | 31.1470889463 | 87 | 5 | 3 | 15.4 | FDD | 774 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3212735 | 2 | 121.4682003284 | 31.1508497724 | 199 | 1 | 1 | 8.5 | TDD | 71 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3214857 | 1 | 121.4740338986 | 31.1443227400 | 200 | 12 | 0 | 23.5 | TDD | 582 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3217243 | 4 | 121.4679553674 | 31.1517275842 | 234 | 4 | 12 | 7.8 | TDD | 115 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3218403 | 6 | 121.4747704189 | 31.1458371506 | 290 | 2 | 2 | 9.6 | TDD | 925 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3228654 | 12 | 121.4750520020 | 31.1538793509 | 175 | 0 | 5 | 8.6 | FDD | 307 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3235999 | 11 | 121.4746510665 | 31.1487939216 | 89 | 14 | 7 | 4.5 | FDD | 973 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3237926 | 3 | 121.4670444765 | 31.1451129002 | 10 | 12 | 11 | 26.8 | TDD | 490 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3254409 | 5 | 121.4706191695 | 31.1452363630 | 292 | 10 | 12 | 23.7 | TDD | 26 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3255456 | 8 | 121.4697247364 | 31.1514315305 | 231 | 11 | 9 | 5.0 | FDD | 326 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3257538 | 10 | 121.4698935266 | 31.1554016465 | 245 | 6 | 7 | 7.3 | FDD | 747 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3274441 | 7 | 121.4730852334 | 31.1455498524 | 38 | 11 | 9 | 21.3 | FDD | 484 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |

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
| 2024-09-20 22:21:31.492 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.510 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.615 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.615 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.303 | NREventA2 | measId:1;ServCellPCI:297;Se... |
| 2024-09-20 22:21:35.440 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.670 | NREventA5 | measId:3;ServCellPCI:297;Se... |
| 2024-09-20 22:21:35.722 | NRHandoverAttempt | SourcePCI:297;SourceNR-ARFC... |
| 2024-09-20 22:21:35.747 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.761 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.880 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.880 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214857 | 1 | 17.8327 | 18.1950 | -115.3362 | 9.6250 | 199.1809 | 0.0042 | 0.0056 |
| 2024_09_20 22:00 | 3212735 | 2 | 9.7247 | 9.0590 | -116.7247 | 18.8120 | 120.9247 | 0.0112 | 0.0065 |
| 2024_09_20 22:00 | 3237926 | 3 | 5.6118 | 6.2422 | -114.0021 | 15.7301 | 153.2182 | 0.0085 | 0.0053 |
| 2024_09_20 22:00 | 3217243 | 4 | 18.5338 | 10.9624 | -115.2675 | 5.0260 | 156.8324 | 0.0186 | 0.0081 |
| 2024_09_20 22:00 | 3254409 | 5 | 8.7986 | 8.5068 | -117.2892 | 6.0084 | 163.7672 | 0.0160 | 0.0192 |
| 2024_09_20 22:00 | 3218403 | 6 | 19.3412 | 16.1638 | -115.6428 | 6.5235 | 189.9978 | 0.0015 | 0.0103 |
| 2024_09_20 22:00 | 3274441 | 7 | 11.7097 | 10.5540 | -117.1733 | 4.8519 | 58.0833 | 0.0140 | 0.0115 |
| 2024_09_20 22:00 | 3255456 | 8 | 13.8074 | 9.0224 | -115.4206 | 3.3063 | 51.3558 | 0.0178 | 0.0057 |
| 2024_09_20 22:00 | 3211005 | 9 | 17.3606 | 18.3548 | -116.4718 | 3.8380 | 25.7266 | 0.0057 | 0.0022 |
| 2024_09_20 22:00 | 3257538 | 10 | 11.7735 | 13.8278 | -114.5184 | 3.5501 | 20.0175 | 0.0009 | 0.0077 |
| 2024_09_20 22:00 | 3235999 | 11 | 13.6686 | 17.3167 | -116.5831 | 4.7022 | 48.2939 | 0.0001 | 0.0073 |
| 2024_09_20 22:00 | 3228654 | 12 | 10.6439 | 14.1839 | -117.7221 | 3.6724 | 42.7400 | 0.0092 | 0.0141 |
| 2024_09_20 22:00 | 3210024 | 13 | 9.4193 | 14.3477 | -115.3412 | 4.1280 | 40.3307 | 0.0196 | 0.0132 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416215_1E860074 | 152650 | 774 | -89.7 | 152650 | 180 | -94.9 | 152650 | 973 | -100.4 | 152650 | 747 |
| MR_1774416215_59A39D8D | 504990 | 26 | -94.5 | 504990 | 71 | -96.1 | 504990 | 925 | -102.5 | 504990 | 490 |
| MR_1774416215_A1B6A7C5 | 504990 | 26 | -97.6 | 504990 | 71 | -96.5 | 504990 | 925 | -101.3 | 504990 | 490 |
| MR_1774416215_3A831E49 | 504990 | 26 | -96.9 | 504990 | 71 | -96.2 | 504990 | 925 | -100.4 | 504990 | 490 |
| MR_1774416215_C91870B6 | 152650 | 774 | -90.3 | 152650 | 180 | -94.6 | 152650 | 973 | -100.7 | 152650 | 747 |
| MR_1774416215_543163F3 | 152650 | 774 | -88.6 | 152650 | 180 | -95.3 | 152650 | 973 | -100.3 | 152650 | 747 |
| MR_1774416215_A9C7E410 | 152650 | 774 | -87.2 | 152650 | 180 | -95.7 | 152650 | 973 | -101.4 | 152650 | 747 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 753: `72ebd516-e82...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `72ebd516-e823-4957-a092-07c85ab0c8c6` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[753] topology](images/train_0753.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3262710_1 by 8 degrees
- `C2`: Decrease transmission power for 3215513_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215513_3
- `C4`: Decrease A3 Offset threshold for 3215513_3
- `C5`: Lift the tilt angle  of 3215513_3 by 9 degrees
- `C6`: Increase transmission power for 3262710_1
- `C7`: Decrease A3 Offset threshold for 3262710_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215513_3
- `C9`: Adjust the azimuth of 3215513_3 by 26 degrees
- `C10`: Adjust the azimuth of 3262710_1 by 50 degrees
- `C11`: Increase A3 Offset threshold for 3215513_3
- `C12`: Press down the tilt angle  of 3215513_3 by 9 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262710_1
- `C14`: Insufficient data; more data is needed for judgment. **← 정답**
- `C15`: Increase A3 Offset threshold for 3262710_1
- `C16`: Check test server and transmission issues
- `C17`: Add neighbor relationship between 3235295_4 and 3215513_3
- `C18`: Decrease transmission power for 3262710_1
- `C19`: Add neighbor relationship between 3262710_1 and 3215513_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262710_1
- `C21`: Increase transmission power for 3215513_3
- `C22`: Press down the tilt angle of 3262710_1 by 8 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.400 | MS1 | 121.4656699459 | 31.1446335550 | 617 | 504990 | -85.55 | 14.02 | 437.14 | 0.17 | 2.14 | 1570 |
| 2024-09-20 22:21:32.819 | MS1 | 121.4656636476 | 31.1446312809 | 617 | 504990 | -91.68 | 13.02 | 424.68 | 0.07 | 2.22 | 1565 |
| 2024-09-20 22:21:33.548 | MS1 | 121.4656731292 | 31.1446198075 | 617 | 504990 | -86.39 | 17.14 | 313.22 | 0.13 | 2.33 | 1565 |
| 2024-09-20 22:21:34.242 | MS1 | 121.4656739739 | 31.1446331189 | 617 | 504990 | -91.62 | 17.21 | 56.24 | 0.13 | 2.81 | 1592 |
| 2024-09-20 22:21:35.865 | MS1 | 121.4656588128 | 31.1446377909 | 617 | 504990 | -87.10 | 12.44 | 92.56 | 0.09 | 2.29 | 1597 |
| 2024-09-20 22:21:36.461 | MS1 | 121.4656586770 | 31.1446287283 | 617 | 504990 | -87.69 | 16.81 | 82.69 | 0.10 | 2.02 | 1598 |
| 2024-09-20 22:21:37.909 | MS1 | 121.4656642242 | 31.1446241118 | 617 | 504990 | -90.84 | 7.09 | 63.89 | 0.02 | 2.46 | 1599 |
| 2024-09-20 22:21:38.343 | MS1 | 121.4656768987 | 31.1446296574 | 617 | 504990 | -91.70 | 12.61 | 89.62 | 0.12 | 2.68 | 1568 |
| 2024-09-20 22:21:39.412 | MS1 | 121.4656688360 | 31.1446281740 | 617 | 504990 | -93.46 | 9.61 | 88.40 | 0.15 | 2.39 | 1581 |
| 2024-09-20 22:21:40.820 | MS1 | 121.4656581018 | 31.1446219968 | 617 | 504990 | -91.31 | 11.97 | 590.73 | 0.06 | 2.62 | 1565 |
| 2024-09-20 22:21:41.160 | MS1 | 121.4656758893 | 31.1446334074 | 617 | 504990 | -90.19 | 10.01 | 444.84 | 0.08 | 2.92 | 1586 |
| 2024-09-20 22:21:42.526 | MS1 | 121.4656627692 | 31.1446191976 | 617 | 504990 | -91.77 | 9.94 | 366.23 | 0.03 | 2.89 | 1587 |

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
| 3215513 | 3 | 121.4661323263 | 31.1532656522 | 209 | 6 | 6 | 42.3 | TDD | 645 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3235295 | 4 | 121.4700346256 | 31.1455807620 | 160 | 10 | 12 | 28.8 | TDD | 822 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3253516 | 2 | 121.4640489079 | 31.1448879236 | 1 | 14 | 12 | 37.8 | TDD | 185 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3262710 | 1 | 121.4729926815 | 31.1533268412 | 108 | 7 | 8 | 16.2 | TDD | 617 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.638 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.658 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.788 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.788 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.478 | NREventA3 | measId:2;ServCellPCI:749;Se... |
| 2024-09-20 22:21:38.718 | NRHandoverAttempt | SourcePCI:749;SourceNR-ARFC... |
| 2024-09-20 22:21:38.755 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.770 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.918 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.918 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3262710 | 1 | 87.9430 | 83.8811 | -114.5392 | 14.1599 | 178.6354 | 0.0122 | 0.0026 |
| 2024_09_19 22:00 | 3253516 | 2 | 86.3831 | 87.1157 | -116.3234 | 16.0247 | 108.0806 | 0.0104 | 0.0121 |
| 2024_09_19 22:00 | 3215513 | 3 | 83.6357 | 89.1925 | -117.9901 | 5.7295 | 80.0073 | 0.0012 | 0.0172 |
| 2024_09_19 22:00 | 3235295 | 4 | 75.8355 | 87.8947 | -116.8305 | 12.0865 | 135.1861 | 0.0151 | 0.0089 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416602_31EE6AA3 | 504990 | 617 | -90.6 | 504990 | 645 | -98.9 | 504990 | 822 | -98.5 | 504990 | 185 |
| MR_1774416602_CA86AA06 | 504990 | 617 | -91.3 | 504990 | 645 | -99.1 | 504990 | 822 | -100.0 | 504990 | 185 |
| MR_1774416602_47F0CD2D | 504990 | 617 | -93.0 | 504990 | 645 | -98.8 | 504990 | 822 | -97.6 | 504990 | 185 |
| MR_1774416602_876E6E1D | 504990 | 617 | -89.9 | 504990 | 645 | -100.3 | 504990 | 822 | -97.8 | 504990 | 185 |
| MR_1774416602_58E1BB55 | 504990 | 617 | -89.9 | 504990 | 645 | -99.2 | 504990 | 822 | -98.6 | 504990 | 185 |
| MR_1774416602_622D32A2 | 504990 | 617 | -93.2 | 504990 | 645 | -99.0 | 504990 | 822 | -97.7 | 504990 | 185 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 754: `f1776955-d3b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f1776955-d3ba-4374-8d5d-ad7c1f44d5a0` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease A3 Offset threshold for 3265137_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[754] topology](images/train_0754.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3235390_3 by 50 degrees
- `C2`: Press down the tilt angle  of 3235390_3 by 8 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235390_3
- `C4`: Adjust the azimuth of 3265137_2 by 50 degrees
- `C5`: Increase transmission power for 3265137_2
- `C6`: Increase A3 Offset threshold for 3235390_3
- `C7`: Add neighbor relationship between 3265137_2 and 3235390_3
- `C8`: Decrease A3 Offset threshold for 3235390_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265137_2
- `C10`: Add neighbor relationship between 3271961_4 and 3235390_3
- `C11`: Press down the tilt angle of 3265137_2 by 10 degrees
- `C12`: Increase transmission power for 3235390_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265137_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235390_3
- `C15`: Lift the tilt angle  of 3235390_3 by 8 degrees
- `C16`: Check test server and transmission issues
- `C17`: Lift the tilt angle of 3265137_2 by 10 degrees
- `C18`: Decrease transmission power for 3235390_3
- `C19`: Increase A3 Offset threshold for 3265137_2
- `C20`: Decrease transmission power for 3265137_2
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease A3 Offset threshold for 3265137_2 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.615 | MS1 | 121.4656756216 | 31.1446254109 | 610 | 504990 | -83.10 | 16.75 | 424.72 | 0.08 | 2.14 | 1588 |
| 2024-09-20 22:21:32.456 | MS1 | 121.4656642206 | 31.1446228362 | 610 | 504990 | -81.52 | 13.97 | 330.66 | 0.09 | 2.97 | 1574 |
| 2024-09-20 22:21:33.251 | MS1 | 121.4656663959 | 31.1446325450 | 610 | 504990 | -81.65 | 16.49 | 415.64 | 0.18 | 2.91 | 1580 |
| 2024-09-20 22:21:34.240 | MS1 | 121.4656628045 | 31.1446370256 | 610 | 504990 | -86.78 | -0.72 | 52.87 | 0.13 | 1.16 | 1577 |
| 2024-09-20 22:21:35.755 | MS1 | 121.4656739323 | 31.1446239792 | 610 | 504990 | -85.32 | -3.92 | 32.93 | 0.13 | 1.39 | 1582 |
| 2024-09-20 22:21:36.867 | MS1 | 121.4656759248 | 31.1446291486 | 610 | 504990 | -88.62 | -1.54 | 74.74 | 0.14 | 1.21 | 1599 |
| 2024-09-20 22:21:37.469 | MS1 | 121.4656679700 | 31.1446325159 | 610 | 504990 | -86.37 | -3.08 | 43.62 | 0.08 | 1.15 | 1592 |
| 2024-09-20 22:21:38.471 | MS1 | 121.4656694113 | 31.1446247828 | 610 | 504990 | -83.54 | -1.46 | 73.46 | 0.01 | 1.21 | 1585 |
| 2024-09-20 22:21:39.189 | MS1 | 121.4656632195 | 31.1446352906 | 548 | 504990 | -79.41 | 17.28 | 292.18 | 0.03 | 1.47 | 1569 |
| 2024-09-20 22:21:40.320 | MS1 | 121.4656687160 | 31.1446346738 | 548 | 504990 | -79.61 | 13.46 | 345.77 | 0.18 | 2.67 | 1586 |
| 2024-09-20 22:21:41.740 | MS1 | 121.4656756149 | 31.1446225067 | 548 | 504990 | -83.26 | 13.70 | 416.91 | 0.05 | 2.13 | 1578 |
| 2024-09-20 22:21:42.222 | MS1 | 121.4656622584 | 31.1446311344 | 548 | 504990 | -84.02 | 12.16 | 419.76 | 0.04 | 2.40 | 1584 |

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
| 3235390 | 3 | 121.4645750799 | 31.1550919777 | 112 | 7 | 11 | 17.9 | TDD | 548 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3241798 | 1 | 121.4648237174 | 31.1462031878 | 52 | 10 | 4 | 42.5 | TDD | 953 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3265137 | 2 | 121.4663523526 | 31.1541314628 | 282 | 9 | 1 | 21.9 | TDD | 610 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3271961 | 4 | 121.4671343461 | 31.1550515261 | 323 | 5 | 8 | 47.8 | TDD | 911 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.005 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.025 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.152 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.152 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.893 | NREventA3 | measId:2;ServCellPCI:950;Se... |
| 2024-09-20 22:21:38.133 | NRHandoverAttempt | SourcePCI:950;SourceNR-ARFC... |
| 2024-09-20 22:21:38.180 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.193 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.341 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.341 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241798 | 1 | 9.9419 | 8.8152 | -116.0560 | 18.8015 | 161.6625 | 0.0038 | 0.0190 |
| 2024_09_20 22:00 | 3265137 | 2 | 12.1518 | 17.7565 | -116.8573 | 5.2104 | 182.3347 | 0.0149 | 0.1670 |
| 2024_09_20 22:00 | 3235390 | 3 | 19.2169 | 8.4519 | -115.2604 | 17.2486 | 90.8371 | 0.0070 | 0.0143 |
| 2024_09_20 22:00 | 3271961 | 4 | 16.3500 | 12.7597 | -115.4475 | 16.8497 | 122.8704 | 0.0018 | 0.0063 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414835_7330049A | 504990 | 548 | -82.4 | 504990 | 610 | -87.7 | 504990 | 911 | -87.3 | 504990 | 953 |
| MR_1774414835_9ACA46E6 | 504990 | 610 | -85.0 | 504990 | 548 | -80.8 | 504990 | 911 | -88.2 | 504990 | 953 |
| MR_1774414835_F8F601B2 | 504990 | 548 | -80.9 | 504990 | 610 | -85.3 | 504990 | 911 | -88.0 | 504990 | 953 |
| MR_1774414835_D38EDA73 | 504990 | 610 | -86.5 | 504990 | 548 | -83.0 | 504990 | 911 | -87.3 | 504990 | 953 |
| MR_1774414835_62FB890F | 504990 | 548 | -79.7 | 504990 | 610 | -86.2 | 504990 | 911 | -88.3 | 504990 | 953 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 755: `4c95d882-f56...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4c95d882-f563-4062-a838-68836a037236` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3233894_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[755] topology](images/train_0755.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3211950_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233894_1
- `C3`: Lift the tilt angle of 3233894_1 by 3 degrees
- `C4`: Increase A3 Offset threshold for 3211950_2
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211950_2
- `C7`: Decrease A3 Offset threshold for 3211950_2
- `C8`: Press down the tilt angle of 3233894_1 by 3 degrees
- `C9`: Increase transmission power for 3211950_2
- `C10`: Lift the tilt angle  of 3211950_2 by 10 degrees
- `C11`: Check test server and transmission issues
- `C12`: Decrease transmission power for 3233894_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211950_2
- `C14`: Add neighbor relationship between 3225586_3 and 3211950_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233894_1 **← 정답**
- `C16`: Increase A3 Offset threshold for 3233894_1
- `C17`: Adjust the azimuth of 3211950_2 by 9 degrees
- `C18`: Add neighbor relationship between 3233894_1 and 3211950_2
- `C19`: Adjust the azimuth of 3233894_1 by 5 degrees
- `C20`: Increase transmission power for 3233894_1
- `C21`: Decrease A3 Offset threshold for 3233894_1
- `C22`: Press down the tilt angle  of 3211950_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.404 | MS1 | 121.4656658051 | 31.1446362588 | 814 | 504990 | -89.54 | 14.37 | 445.71 | 0.06 | 2.99 | 1587 |
| 2024-09-20 22:21:32.234 | MS1 | 121.4656665798 | 31.1446369743 | 814 | 504990 | -86.47 | 13.77 | 592.22 | 0.05 | 2.86 | 1582 |
| 2024-09-20 22:21:33.228 | MS1 | 121.4656646866 | 31.1446280973 | 814 | 504990 | -87.78 | 14.00 | 331.36 | 0.04 | 2.18 | 1593 |
| 2024-09-20 22:21:34.553 | MS1 | 121.4656705294 | 31.1446317525 | 814 | 504990 | -88.50 | 12.91 | 87.23 | 0.51 | 2.95 | 604 |
| 2024-09-20 22:21:35.294 | MS1 | 121.4656636796 | 31.1446200145 | 814 | 504990 | -86.57 | 16.02 | 68.68 | 0.54 | 2.55 | 694 |
| 2024-09-20 22:21:36.676 | MS1 | 121.4656706990 | 31.1446253630 | 814 | 504990 | -91.25 | 13.73 | 64.62 | 0.64 | 2.86 | 647 |
| 2024-09-20 22:21:37.550 | MS1 | 121.4656654571 | 31.1446294025 | 814 | 504990 | -89.89 | 9.51 | 105.62 | 0.63 | 2.90 | 583 |
| 2024-09-20 22:21:38.949 | MS1 | 121.4656771246 | 31.1446340880 | 814 | 504990 | -91.95 | 9.65 | 64.10 | 0.60 | 2.66 | 547 |
| 2024-09-20 22:21:39.859 | MS1 | 121.4656740234 | 31.1446199006 | 814 | 504990 | -93.18 | 8.95 | 51.55 | 0.60 | 2.08 | 538 |
| 2024-09-20 22:21:40.985 | MS1 | 121.4656692831 | 31.1446247032 | 814 | 504990 | -89.64 | 7.70 | 517.41 | 0.15 | 2.89 | 1562 |
| 2024-09-20 22:21:41.791 | MS1 | 121.4656587023 | 31.1446294627 | 814 | 504990 | -90.68 | 11.14 | 582.44 | 0.01 | 2.05 | 1574 |
| 2024-09-20 22:21:42.437 | MS1 | 121.4656587763 | 31.1446297661 | 814 | 504990 | -91.99 | 9.88 | 365.87 | 0.07 | 2.56 | 1587 |

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
| 3211950 | 2 | 121.4672734388 | 31.1446889133 | 276 | 8 | 4 | 39.1 | TDD | 411 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3225586 | 3 | 121.4700828610 | 31.1489583823 | 270 | 6 | 6 | 46.6 | TDD | 734 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3233894 | 1 | 121.4644323510 | 31.1545789472 | 179 | 1 | 3 | 31.9 | TDD | 814 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3265991 | 4 | 121.4740602986 | 31.1530780743 | 311 | 2 | 8 | 35.9 | TDD | 551 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.575 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.596 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.742 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.742 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.424 | NREventA3 | measId:2;ServCellPCI:480;Se... |
| 2024-09-20 22:21:38.664 | NRHandoverAttempt | SourcePCI:480;SourceNR-ARFC... |
| 2024-09-20 22:21:38.694 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.705 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.843 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.843 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233894 | 1 | 17.6442 | 16.3597 | -114.2066 | 16.5950 | 157.8652 | 0.0094 | 0.0139 |
| 2024_09_20 22:00 | 3211950 | 2 | 16.8745 | 7.6586 | -114.3549 | 16.9513 | 146.3474 | 0.0025 | 0.0097 |
| 2024_09_20 22:00 | 3225586 | 3 | 13.0662 | 9.1243 | -117.1100 | 18.4894 | 162.7695 | 0.0071 | 0.0030 |
| 2024_09_20 22:00 | 3265991 | 4 | 5.1091 | 19.1599 | -115.0555 | 16.8841 | 106.2793 | 0.0071 | 0.0030 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412032_9567AA74 | 504990 | 814 | -89.2 | 504990 | 411 | -95.8 | 504990 | 734 | -95.8 | 504990 | 551 |
| MR_1774412032_28A4A62D | 504990 | 814 | -87.7 | 504990 | 411 | -93.4 | 504990 | 734 | -97.2 | 504990 | 551 |
| MR_1774412032_2D9D38A2 | 504990 | 814 | -90.4 | 504990 | 411 | -97.0 | 504990 | 734 | -95.6 | 504990 | 551 |
| MR_1774412032_F5FDD605 | 504990 | 814 | -86.6 | 504990 | 411 | -96.8 | 504990 | 734 | -97.4 | 504990 | 551 |
| MR_1774412032_A65A6BFB | 504990 | 814 | -87.8 | 504990 | 411 | -96.9 | 504990 | 734 | -95.6 | 504990 | 551 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 756: `4541ed8c-d7b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4541ed8c-d7b2-4826-8f2c-bba061ce879b` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212293_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[756] topology](images/train_0756.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3229089_6 by 5 degrees
- `C2`: Increase transmission power for 3229089_6
- `C3`: Increase A3 Offset threshold for 3212293_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229089_6
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212293_2
- `C6`: Adjust the azimuth of 3212293_2 by 30 degrees
- `C7`: Check test server and transmission issues
- `C8`: Lift the tilt angle of 3212293_2 by 6 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212293_2 **← 정답**
- `C10`: Increase A3 Offset threshold for 3229089_6
- `C11`: Add neighbor relationship between 3212293_2 and 3229089_6
- `C12`: Adjust the azimuth of 3229089_6 by 21 degrees
- `C13`: Press down the tilt angle  of 3229089_6 by 5 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Add neighbor relationship between 3271448_7 and 3229089_6
- `C16`: Decrease A3 Offset threshold for 3212293_2
- `C17`: Press down the tilt angle of 3212293_2 by 6 degrees
- `C18`: Increase transmission power for 3212293_2
- `C19`: Decrease transmission power for 3229089_6
- `C20`: Decrease transmission power for 3212293_2
- `C21`: Decrease A3 Offset threshold for 3229089_6
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229089_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.105 | MS1 | 121.4656774421 | 31.1446239557 | 100 | 504990 | -93.37 | 12.74 | 511.36 | 0.15 | 2.95 | 1592 |
| 2024-09-20 22:21:32.988 | MS1 | 121.4656740407 | 31.1446242016 | 866 | 504990 | -93.75 | 12.22 | 441.68 | 0.19 | 2.49 | 1571 |
| 2024-09-20 22:21:33.184 | MS1 | 121.4656602741 | 31.1446275059 | 102 | 504990 | -95.78 | 9.64 | 594.54 | 0.19 | 2.26 | 1585 |
| 2024-09-20 22:21:34.358 | MS1 | 121.4656715229 | 31.1446359692 | 426 | 152650 | -88.14 | 5.02 | 51.32 | 0.13 | 1.83 | 999 |
| 2024-09-20 22:21:35.749 | MS1 | 121.4656600401 | 31.1446369693 | 52 | 152650 | -90.66 | 2.25 | 81.86 | 0.08 | 1.69 | 912 |
| 2024-09-20 22:21:36.825 | MS1 | 121.4656744263 | 31.1446206544 | 736 | 152650 | -90.96 | 2.81 | 87.58 | 0.05 | 1.70 | 945 |
| 2024-09-20 22:21:37.438 | MS1 | 121.4656599483 | 31.1446204997 | 826 | 152650 | -87.30 | 3.00 | 89.37 | 0.05 | 1.51 | 984 |
| 2024-09-20 22:21:38.868 | MS1 | 121.4656696078 | 31.1446274570 | 426 | 152650 | -92.13 | 4.09 | 63.39 | 0.07 | 1.66 | 944 |
| 2024-09-20 22:21:39.856 | MS1 | 121.4656772630 | 31.1446367548 | 52 | 152650 | -88.31 | 2.85 | 65.60 | 0.13 | 1.90 | 934 |
| 2024-09-20 22:21:40.849 | MS1 | 121.4656626471 | 31.1446331368 | 736 | 152650 | -89.98 | 6.28 | 83.78 | 0.12 | 2.12 | 1600 |
| 2024-09-20 22:21:41.747 | MS1 | 121.4656620441 | 31.1446323820 | 826 | 152650 | -93.95 | 3.24 | 56.74 | 0.14 | 2.72 | 1594 |
| 2024-09-20 22:21:42.579 | MS1 | 121.4656754284 | 31.1446337660 | 426 | 152650 | -95.18 | 5.78 | 59.24 | 0.13 | 2.89 | 1598 |

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
| 3212293 | 2 | 121.4648873037 | 31.1521244321 | 205 | 4 | 2 | 26.8 | TDD | 100 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3217707 | 12 | 121.4700155657 | 31.1508146749 | 310 | 12 | 10 | 21.5 | FDD | 826 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3227333 | 4 | 121.4725994649 | 31.1538183634 | 315 | 6 | 4 | 5.7 | TDD | 722 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3227397 | 10 | 121.4707447573 | 31.1491853319 | 131 | 12 | 3 | 21.5 | FDD | 206 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3229089 | 6 | 121.4712353115 | 31.1509368318 | 238 | 4 | 1 | 7.8 | TDD | 350 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3232229 | 3 | 121.4671928179 | 31.1559684858 | 177 | 14 | 8 | 15.2 | TDD | 102 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3234661 | 11 | 121.4697260693 | 31.1499114075 | 304 | 8 | 7 | 9.8 | FDD | 52 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3243747 | 9 | 121.4644320903 | 31.1552847412 | 64 | 9 | 2 | 26.2 | FDD | 46 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3245791 | 5 | 121.4729259343 | 31.1466163023 | 106 | 6 | 6 | 6.0 | TDD | 25 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3256842 | 8 | 121.4754096858 | 31.1488441384 | 115 | 14 | 3 | 1.4 | FDD | 426 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3258619 | 1 | 121.4685259279 | 31.1547297248 | 53 | 2 | 7 | 0.1 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3271448 | 7 | 121.4687699079 | 31.1541812441 | 151 | 11 | 8 | 8.2 | FDD | 736 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3276746 | 13 | 121.4680735693 | 31.1518747847 | 121 | 5 | 6 | 20.4 | FDD | 157 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |

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
| 2024-09-20 22:21:31.154 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.174 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.313 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.313 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.997 | NREventA2 | measId:1;ServCellPCI:263;Se... |
| 2024-09-20 22:21:35.140 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.415 | NREventA5 | measId:3;ServCellPCI:263;Se... |
| 2024-09-20 22:21:35.493 | NRHandoverAttempt | SourcePCI:263;SourceNR-ARFC... |
| 2024-09-20 22:21:35.542 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.552 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.700 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.700 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258619 | 1 | 15.7602 | 15.8805 | -117.8153 | 11.5546 | 181.4205 | 0.0088 | 0.0149 |
| 2024_09_20 22:00 | 3212293 | 2 | 16.1940 | 17.5109 | -117.5254 | 6.2817 | 192.1222 | 0.0028 | 0.0031 |
| 2024_09_20 22:00 | 3232229 | 3 | 10.9476 | 11.9715 | -114.3987 | 14.8523 | 96.1907 | 0.0033 | 0.0075 |
| 2024_09_20 22:00 | 3227333 | 4 | 5.8588 | 16.1747 | -115.6312 | 11.7535 | 166.6457 | 0.0112 | 0.0004 |
| 2024_09_20 22:00 | 3245791 | 5 | 6.8420 | 19.3595 | -115.4506 | 11.7401 | 179.1652 | 0.0096 | 0.0114 |
| 2024_09_20 22:00 | 3229089 | 6 | 13.5540 | 14.4531 | -117.1414 | 16.4253 | 92.3351 | 0.0074 | 0.0058 |
| 2024_09_20 22:00 | 3271448 | 7 | 11.7445 | 9.8644 | -115.9209 | 4.0703 | 23.8108 | 0.0084 | 0.0142 |
| 2024_09_20 22:00 | 3256842 | 8 | 5.1029 | 19.5596 | -115.0138 | 4.2322 | 26.1951 | 0.0172 | 0.0149 |
| 2024_09_20 22:00 | 3243747 | 9 | 12.8654 | 13.7333 | -115.5656 | 3.5272 | 58.8195 | 0.0019 | 0.0197 |
| 2024_09_20 22:00 | 3227397 | 10 | 5.9844 | 17.0596 | -116.8648 | 3.4419 | 58.1529 | 0.0186 | 0.0037 |
| 2024_09_20 22:00 | 3234661 | 11 | 13.0697 | 15.8920 | -115.5991 | 4.7120 | 23.0560 | 0.0149 | 0.0133 |
| 2024_09_20 22:00 | 3217707 | 12 | 14.3180 | 7.6712 | -115.2925 | 3.3187 | 46.6638 | 0.0037 | 0.0143 |
| 2024_09_20 22:00 | 3276746 | 13 | 8.3717 | 10.3712 | -116.1203 | 3.4962 | 55.5794 | 0.0011 | 0.0160 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415726_F52869D7 | 152650 | 426 | -88.6 | 152650 | 157 | -90.7 | 152650 | 46 | -94.1 | 152650 | 206 |
| MR_1774415726_4C9CD54A | 152650 | 426 | -88.9 | 152650 | 157 | -90.4 | 152650 | 46 | -93.5 | 152650 | 206 |
| MR_1774415726_9DA9FE7F | 152650 | 426 | -88.5 | 152650 | 157 | -90.1 | 152650 | 46 | -93.5 | 152650 | 206 |
| MR_1774415726_F71279B2 | 504990 | 102 | -95.7 | 504990 | 350 | -94.9 | 504990 | 722 | -99.1 | 504990 | 25 |
| MR_1774415726_A892326D | 152650 | 426 | -88.6 | 152650 | 157 | -89.9 | 152650 | 46 | -92.8 | 152650 | 206 |
| MR_1774415726_43D3CFFD | 504990 | 102 | -94.8 | 504990 | 350 | -95.5 | 504990 | 722 | -98.0 | 504990 | 25 |
| MR_1774415726_CCD906AF | 504990 | 102 | -95.0 | 504990 | 350 | -96.3 | 504990 | 722 | -99.0 | 504990 | 25 |
| MR_1774415726_41F20BCF | 504990 | 102 | -97.0 | 504990 | 350 | -95.1 | 504990 | 722 | -96.5 | 504990 | 25 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 757: `c77ea585-cd6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c77ea585-cd6e-437b-a878-2e191ead2e9d` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[757] topology](images/train_0757.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease transmission power for 3234426_2
- `C3`: Decrease A3 Offset threshold for 3267673_3
- `C4`: Decrease A3 Offset threshold for 3234426_2
- `C5`: Increase A3 Offset threshold for 3267673_3
- `C6`: Add neighbor relationship between 3267673_3 and 3234426_2
- `C7`: Insufficient data; more data is needed for judgment. **← 정답**
- `C8`: Press down the tilt angle of 3267673_3 by 10 degrees
- `C9`: Lift the tilt angle of 3267673_3 by 10 degrees
- `C10`: Adjust the azimuth of 3267673_3 by 4 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267673_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234426_2
- `C13`: Increase transmission power for 3267673_3
- `C14`: Increase A3 Offset threshold for 3234426_2
- `C15`: Increase transmission power for 3234426_2
- `C16`: Lift the tilt angle  of 3234426_2 by 7 degrees
- `C17`: Add neighbor relationship between 3266382_1 and 3234426_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267673_3
- `C19`: Adjust the azimuth of 3234426_2 by 50 degrees
- `C20`: Decrease transmission power for 3267673_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234426_2
- `C22`: Press down the tilt angle  of 3234426_2 by 7 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.557 | MS1 | 121.4656691619 | 31.1446265824 | 55 | 504990 | -88.02 | 17.19 | 313.95 | 0.16 | 2.40 | 1582 |
| 2024-09-20 22:21:32.758 | MS1 | 121.4656763229 | 31.1446374217 | 55 | 504990 | -87.68 | 12.89 | 513.09 | 0.10 | 2.35 | 1589 |
| 2024-09-20 22:21:33.443 | MS1 | 121.4656607427 | 31.1446359872 | 55 | 504990 | -88.35 | 13.27 | 354.10 | 0.09 | 2.25 | 1578 |
| 2024-09-20 22:21:34.668 | MS1 | 121.4656715114 | 31.1446302118 | 55 | 504990 | -89.47 | 14.46 | 46.66 | 0.19 | 2.21 | 1586 |
| 2024-09-20 22:21:35.926 | MS1 | 121.4656586563 | 31.1446331902 | 55 | 504990 | -87.90 | 15.66 | 81.19 | 0.13 | 2.02 | 1575 |
| 2024-09-20 22:21:36.398 | MS1 | 121.4656630988 | 31.1446249511 | 55 | 504990 | -91.03 | 17.45 | 60.94 | 0.03 | 2.12 | 1576 |
| 2024-09-20 22:21:37.545 | MS1 | 121.4656652778 | 31.1446225156 | 55 | 504990 | -92.98 | 11.65 | 58.58 | 0.06 | 2.82 | 1593 |
| 2024-09-20 22:21:38.515 | MS1 | 121.4656744650 | 31.1446202039 | 55 | 504990 | -93.96 | 10.25 | 91.21 | 0.18 | 2.55 | 1586 |
| 2024-09-20 22:21:39.207 | MS1 | 121.4656679601 | 31.1446334140 | 55 | 504990 | -93.01 | 8.99 | 49.82 | 0.17 | 2.40 | 1574 |
| 2024-09-20 22:21:40.684 | MS1 | 121.4656581074 | 31.1446350086 | 55 | 504990 | -93.83 | 9.63 | 508.54 | 0.12 | 2.19 | 1560 |
| 2024-09-20 22:21:41.942 | MS1 | 121.4656725989 | 31.1446203658 | 55 | 504990 | -91.64 | 11.53 | 434.58 | 0.07 | 2.56 | 1583 |
| 2024-09-20 22:21:42.348 | MS1 | 121.4656706475 | 31.1446188175 | 55 | 504990 | -93.61 | 12.41 | 418.64 | 0.10 | 2.28 | 1590 |

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
| 3218017 | 4 | 121.4733275066 | 31.1529151613 | 285 | 15 | 7 | 21.4 | TDD | 399 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3234426 | 2 | 121.4678724639 | 31.1477980192 | 48 | 3 | 3 | 29.2 | TDD | 419 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3266382 | 1 | 121.4725811602 | 31.1457307940 | 255 | 9 | 6 | 37.6 | TDD | 424 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3267673 | 3 | 121.4675950193 | 31.1444145785 | 281 | 7 | 7 | 37.8 | TDD | 55 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.965 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.986 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.095 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.095 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.856 | NREventA3 | measId:2;ServCellPCI:79;Ser... |
| 2024-09-20 22:21:38.096 | NRHandoverAttempt | SourcePCI:79;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.146 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.161 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.273 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.273 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3266382 | 1 | 90.8135 | 94.2394 | -117.5199 | 10.4658 | 136.5528 | 0.0171 | 0.0157 |
| 2024_09_19 22:00 | 3234426 | 2 | 92.2234 | 77.5448 | -114.4567 | 7.0427 | 100.6617 | 0.0101 | 0.0145 |
| 2024_09_19 22:00 | 3267673 | 3 | 85.0333 | 82.4740 | -117.4257 | 9.3330 | 196.0970 | 0.0187 | 0.0022 |
| 2024_09_19 22:00 | 3218017 | 4 | 86.6117 | 79.6426 | -114.7052 | 9.6485 | 154.8442 | 0.0074 | 0.0139 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412560_5B8F21A9 | 504990 | 55 | -89.3 | 504990 | 419 | -96.4 | 504990 | 424 | -99.8 | 504990 | 399 |
| MR_1774412560_3AB0FE07 | 504990 | 55 | -87.8 | 504990 | 419 | -96.5 | 504990 | 424 | -98.6 | 504990 | 399 |
| MR_1774412560_DEFEB046 | 504990 | 55 | -88.6 | 504990 | 419 | -97.0 | 504990 | 424 | -99.1 | 504990 | 399 |
| MR_1774412560_DA540023 | 504990 | 55 | -88.3 | 504990 | 419 | -96.5 | 504990 | 424 | -96.5 | 504990 | 399 |
| MR_1774412560_0743915B | 504990 | 55 | -88.6 | 504990 | 419 | -97.8 | 504990 | 424 | -96.9 | 504990 | 399 |
| MR_1774412560_9FE3F3D3 | 504990 | 55 | -90.5 | 504990 | 419 | -96.3 | 504990 | 424 | -100.1 | 504990 | 399 |
| MR_1774412560_B94A70DF | 504990 | 55 | -88.2 | 504990 | 419 | -96.6 | 504990 | 424 | -99.5 | 504990 | 399 |
| MR_1774412560_AA309AC4 | 504990 | 55 | -88.3 | 504990 | 419 | -96.7 | 504990 | 424 | -96.9 | 504990 | 399 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 758: `53018b61-ab0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `53018b61-ab07-4818-a768-afd7898ee380` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[758] topology](images/train_0758.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269549_3
- `C2`: Decrease A3 Offset threshold for 3269549_3
- `C3`: Check test server and transmission issues
- `C4`: Increase A3 Offset threshold for 3269549_3
- `C5`: Press down the tilt angle of 3269549_3 by 10 degrees
- `C6`: Adjust the azimuth of 3219778_2 by 50 degrees
- `C7`: Adjust the azimuth of 3269549_3 by 50 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269549_3
- `C9`: Add neighbor relationship between 3269549_3 and 3219778_2
- `C10`: Add neighbor relationship between 3238446_1 and 3219778_2
- `C11`: Increase A3 Offset threshold for 3219778_2
- `C12`: Insufficient data; more data is needed for judgment. **← 정답**
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219778_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219778_2
- `C15`: Increase transmission power for 3219778_2
- `C16`: Decrease transmission power for 3269549_3
- `C17`: Decrease transmission power for 3219778_2
- `C18`: Lift the tilt angle of 3269549_3 by 10 degrees
- `C19`: Lift the tilt angle  of 3219778_2 by 10 degrees
- `C20`: Decrease A3 Offset threshold for 3219778_2
- `C21`: Increase transmission power for 3269549_3
- `C22`: Press down the tilt angle  of 3219778_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.432 | MS1 | 121.4656624539 | 31.1446189543 | 164 | 504990 | -86.19 | 12.52 | 495.12 | 0.08 | 2.66 | 1583 |
| 2024-09-20 22:21:32.979 | MS1 | 121.4656703926 | 31.1446236690 | 164 | 504990 | -86.69 | 14.18 | 468.31 | 0.12 | 2.93 | 1565 |
| 2024-09-20 22:21:33.334 | MS1 | 121.4656770654 | 31.1446257901 | 164 | 504990 | -89.16 | 17.66 | 429.90 | 0.15 | 2.27 | 1565 |
| 2024-09-20 22:21:34.547 | MS1 | 121.4656739637 | 31.1446379835 | 164 | 504990 | -91.41 | 17.12 | 63.95 | 0.13 | 2.02 | 1592 |
| 2024-09-20 22:21:35.357 | MS1 | 121.4656669945 | 31.1446350533 | 164 | 504990 | -86.63 | 14.48 | 84.08 | 0.06 | 2.71 | 1579 |
| 2024-09-20 22:21:36.841 | MS1 | 121.4656614318 | 31.1446244270 | 164 | 504990 | -85.22 | 16.15 | 73.31 | 0.15 | 2.08 | 1560 |
| 2024-09-20 22:21:37.307 | MS1 | 121.4656612871 | 31.1446189029 | 164 | 504990 | -89.26 | 9.35 | 91.35 | 0.14 | 2.56 | 1582 |
| 2024-09-20 22:21:38.274 | MS1 | 121.4656583859 | 31.1446310938 | 164 | 504990 | -91.02 | 12.23 | 67.32 | 0.19 | 2.36 | 1579 |
| 2024-09-20 22:21:39.782 | MS1 | 121.4656742101 | 31.1446181298 | 164 | 504990 | -89.48 | 8.09 | 83.40 | 0.12 | 2.72 | 1584 |
| 2024-09-20 22:21:40.402 | MS1 | 121.4656623049 | 31.1446214174 | 164 | 504990 | -92.73 | 7.15 | 324.71 | 0.19 | 2.13 | 1560 |
| 2024-09-20 22:21:41.775 | MS1 | 121.4656767123 | 31.1446371601 | 164 | 504990 | -90.68 | 10.26 | 345.19 | 0.13 | 2.70 | 1563 |
| 2024-09-20 22:21:42.217 | MS1 | 121.4656657427 | 31.1446197593 | 164 | 504990 | -90.01 | 8.61 | 459.88 | 0.20 | 2.82 | 1570 |

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
| 3219778 | 2 | 121.4720835450 | 31.1531471074 | 307 | 9 | 0 | 23.8 | TDD | 402 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3238446 | 1 | 121.4741805456 | 31.1557468722 | 178 | 13 | 7 | 27.3 | TDD | 593 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3267847 | 4 | 121.4669004621 | 31.1542863467 | 262 | 14 | 7 | 36.6 | TDD | 878 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3269549 | 3 | 121.4658672667 | 31.1485075172 | 66 | 12 | 1 | 20.8 | TDD | 164 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.825 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.844 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.966 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.966 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.649 | NREventA3 | measId:2;ServCellPCI:603;Se... |
| 2024-09-20 22:21:37.889 | NRHandoverAttempt | SourcePCI:603;SourceNR-ARFC... |
| 2024-09-20 22:21:37.929 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.940 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.076 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.076 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3238446 | 1 | 79.5679 | 93.0591 | -116.4663 | 8.2588 | 93.0237 | 0.0109 | 0.0156 |
| 2024_09_19 22:00 | 3219778 | 2 | 93.3741 | 94.1142 | -116.4095 | 7.0521 | 193.4435 | 0.0086 | 0.0029 |
| 2024_09_19 22:00 | 3269549 | 3 | 94.2642 | 86.3893 | -116.0116 | 14.2748 | 167.7698 | 0.0016 | 0.0198 |
| 2024_09_19 22:00 | 3267847 | 4 | 91.6410 | 76.6344 | -115.0578 | 17.4802 | 129.4334 | 0.0024 | 0.0039 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414827_D44BB0D6 | 504990 | 164 | -90.6 | 504990 | 402 | -99.0 | 504990 | 593 | -100.4 | 504990 | 878 |
| MR_1774414827_FF9FAF64 | 504990 | 164 | -91.3 | 504990 | 402 | -98.9 | 504990 | 593 | -101.4 | 504990 | 878 |
| MR_1774414827_124AAE35 | 504990 | 164 | -91.4 | 504990 | 402 | -99.9 | 504990 | 593 | -102.8 | 504990 | 878 |
| MR_1774414827_0853AB8A | 504990 | 164 | -91.1 | 504990 | 402 | -99.6 | 504990 | 593 | -101.6 | 504990 | 878 |
| MR_1774414827_5A3E11FE | 504990 | 164 | -93.4 | 504990 | 402 | -99.4 | 504990 | 593 | -103.6 | 504990 | 878 |
| MR_1774414827_694097C6 | 504990 | 164 | -92.3 | 504990 | 402 | -98.0 | 504990 | 593 | -101.1 | 504990 | 878 |
| MR_1774414827_5DE75A8C | 504990 | 164 | -90.4 | 504990 | 402 | -98.9 | 504990 | 593 | -102.5 | 504990 | 878 |
| MR_1774414827_83FECCDE | 504990 | 164 | -91.8 | 504990 | 402 | -98.3 | 504990 | 593 | -103.8 | 504990 | 878 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 759: `ff55e947-d77...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ff55e947-d77a-4f58-9ef1-ccbba886dc80` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[759] topology](images/train_0759.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3212284_2
- `C2`: Decrease transmission power for 3212284_2
- `C3`: Lift the tilt angle  of 3212284_2 by 10 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212284_2
- `C5`: Press down the tilt angle  of 3212284_2 by 10 degrees
- `C6`: Increase transmission power for 3212284_2
- `C7`: Add neighbor relationship between 3269634_1 and 3212284_2
- `C8`: Insufficient data; more data is needed for judgment. **← 정답**
- `C9`: Lift the tilt angle of 3269634_1 by 10 degrees
- `C10`: Decrease transmission power for 3269634_1
- `C11`: Adjust the azimuth of 3269634_1 by 50 degrees
- `C12`: Increase A3 Offset threshold for 3212284_2
- `C13`: Decrease A3 Offset threshold for 3269634_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212284_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269634_1
- `C16`: Adjust the azimuth of 3212284_2 by 50 degrees
- `C17`: Add neighbor relationship between 3270440_4 and 3212284_2
- `C18`: Press down the tilt angle of 3269634_1 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3269634_1
- `C20`: Check test server and transmission issues
- `C21`: Increase transmission power for 3269634_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269634_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.409 | MS1 | 121.4656619947 | 31.1446227519 | 976 | 504990 | -88.32 | 12.60 | 435.00 | 0.09 | 2.91 | 1589 |
| 2024-09-20 22:21:32.394 | MS1 | 121.4656704212 | 31.1446190320 | 976 | 504990 | -90.80 | 15.69 | 459.67 | 0.12 | 2.27 | 1600 |
| 2024-09-20 22:21:33.425 | MS1 | 121.4656664547 | 31.1446205502 | 976 | 504990 | -88.46 | 17.00 | 320.13 | 0.04 | 2.90 | 1566 |
| 2024-09-20 22:21:34.670 | MS1 | 121.4656689377 | 31.1446263704 | 976 | 504990 | -86.81 | 16.52 | 73.25 | 0.02 | 2.81 | 1592 |
| 2024-09-20 22:21:35.773 | MS1 | 121.4656756745 | 31.1446325932 | 976 | 504990 | -90.47 | 15.08 | 70.80 | 0.11 | 2.03 | 1580 |
| 2024-09-20 22:21:36.580 | MS1 | 121.4656767305 | 31.1446375770 | 976 | 504990 | -89.25 | 14.64 | 86.16 | 0.00 | 2.08 | 1573 |
| 2024-09-20 22:21:37.591 | MS1 | 121.4656765933 | 31.1446364771 | 976 | 504990 | -89.41 | 9.11 | 57.01 | 0.09 | 2.59 | 1595 |
| 2024-09-20 22:21:38.372 | MS1 | 121.4656711634 | 31.1446198133 | 976 | 504990 | -92.18 | 7.71 | 73.25 | 0.18 | 2.01 | 1596 |
| 2024-09-20 22:21:39.510 | MS1 | 121.4656603015 | 31.1446195422 | 976 | 504990 | -92.53 | 11.97 | 56.62 | 0.06 | 2.94 | 1572 |
| 2024-09-20 22:21:40.724 | MS1 | 121.4656671390 | 31.1446301255 | 976 | 504990 | -92.12 | 11.77 | 417.99 | 0.14 | 2.49 | 1572 |
| 2024-09-20 22:21:41.678 | MS1 | 121.4656694765 | 31.1446192137 | 976 | 504990 | -89.03 | 8.88 | 565.69 | 0.00 | 2.20 | 1582 |
| 2024-09-20 22:21:42.118 | MS1 | 121.4656666531 | 31.1446267192 | 976 | 504990 | -90.45 | 11.91 | 484.61 | 0.20 | 2.48 | 1571 |

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
| 3212284 | 2 | 121.4661020757 | 31.1497348344 | 26 | 12 | 11 | 32.2 | TDD | 201 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3269634 | 1 | 121.4686790291 | 31.1526083329 | 37 | 11 | 3 | 20.0 | TDD | 976 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3270440 | 4 | 121.4651633309 | 31.1467425770 | 231 | 12 | 6 | 46.2 | TDD | 134 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3276770 | 3 | 121.4667296279 | 31.1483018803 | 90 | 15 | 0 | 37.3 | TDD | 104 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.233 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.254 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.366 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.366 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.097 | NREventA3 | measId:2;ServCellPCI:808;Se... |
| 2024-09-20 22:21:38.337 | NRHandoverAttempt | SourcePCI:808;SourceNR-ARFC... |
| 2024-09-20 22:21:38.377 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.387 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.537 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.537 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3269634 | 1 | 77.3082 | 77.9444 | -116.5551 | 8.3372 | 107.0777 | 0.0177 | 0.0142 |
| 2024_09_19 22:00 | 3212284 | 2 | 81.0023 | 78.1257 | -115.4733 | 14.7663 | 175.7997 | 0.0048 | 0.0027 |
| 2024_09_19 22:00 | 3276770 | 3 | 75.1880 | 77.3882 | -114.4935 | 7.4078 | 186.7837 | 0.0188 | 0.0089 |
| 2024_09_19 22:00 | 3270440 | 4 | 93.7849 | 82.7079 | -115.1004 | 12.1144 | 141.3356 | 0.0128 | 0.0051 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415589_52997BFA | 504990 | 976 | -87.3 | 504990 | 201 | -94.2 | 504990 | 134 | -93.6 | 504990 | 104 |
| MR_1774415589_952007E7 | 504990 | 976 | -84.9 | 504990 | 201 | -91.6 | 504990 | 134 | -95.1 | 504990 | 104 |
| MR_1774415589_DE454038 | 504990 | 976 | -87.9 | 504990 | 201 | -92.0 | 504990 | 134 | -92.9 | 504990 | 104 |
| MR_1774415589_B6A6C105 | 504990 | 976 | -86.6 | 504990 | 201 | -90.6 | 504990 | 134 | -92.8 | 504990 | 104 |
| MR_1774415589_AF8221DA | 504990 | 976 | -87.4 | 504990 | 201 | -94.0 | 504990 | 134 | -94.3 | 504990 | 104 |
| MR_1774415589_9857681B | 504990 | 976 | -85.8 | 504990 | 201 | -93.9 | 504990 | 134 | -92.4 | 504990 | 104 |
| MR_1774415589_AE7F9F73 | 504990 | 976 | -86.2 | 504990 | 201 | -92.5 | 504990 | 134 | -92.4 | 504990 | 104 |

> *... 2개 열 생략 (전체 14열)*

---
