# Track A 문제 분석 — train[330]~train[339]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[330] ~ train[339] (10개)

## 목차

1. [문제 330: `5e75818d-b2c...`](#330) — single-answer, 정답: C6
2. [문제 331: `e5015853-a25...`](#331) — single-answer, 정답: C12
3. [문제 332: `2f0b8382-c1a...`](#332) — single-answer, 정답: C21
4. [문제 333: `d166c12c-d82...`](#333) — single-answer, 정답: C1
5. [문제 334: `22a8890e-c80...`](#334) — single-answer, 정답: C8
6. [문제 335: `be218f76-998...`](#335) — single-answer, 정답: C17
7. [문제 336: `e3ef95a5-690...`](#336) — single-answer, 정답: C18
8. [문제 337: `0fad3aeb-539...`](#337) — single-answer, 정답: C4
9. [문제 338: `8dfb76d8-31b...`](#338) — single-answer, 정답: C2
10. [문제 339: `84e89524-69a...`](#339) — single-answer, 정답: C11

---

### 문제 330: `5e75818d-b2c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5e75818d-b2c5-43bd-9b87-1084399e3e14` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Lift the tilt angle  of 3210086_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[330] topology](images/train_0330.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3219659_1
- `C2`: Press down the tilt angle  of 3210086_3 by 10 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216023_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216023_2
- `C5`: Increase transmission power for 3216023_2
- `C6`: Lift the tilt angle  of 3210086_3 by 10 degrees **← 정답**
- `C7`: Adjust the azimuth of 3210086_3 by 50 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Press down the tilt angle of 3216023_2 by 5 degrees
- `C10`: Decrease transmission power for 3219659_1
- `C11`: Decrease A3 Offset threshold for 3219659_1
- `C12`: Adjust the azimuth of 3216023_2 by 42 degrees
- `C13`: Increase A3 Offset threshold for 3216023_2
- `C14`: Add neighbor relationship between 3216023_2 and 3219659_1
- `C15`: Increase A3 Offset threshold for 3219659_1
- `C16`: Check test server and transmission issues
- `C17`: Lift the tilt angle of 3216023_2 by 5 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219659_1
- `C19`: Decrease transmission power for 3216023_2
- `C20`: Decrease A3 Offset threshold for 3216023_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219659_1
- `C22`: Add neighbor relationship between 3210086_3 and 3219659_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.586 | MS1 | 121.4656738016 | 31.1446184739 | 89 | 504990 | -91.24 | 12.92 | 389.62 | 0.13 | 2.39 | 1574 |
| 2024-09-20 22:21:32.212 | MS1 | 121.4656598401 | 31.1446327833 | 89 | 504990 | -89.66 | 16.78 | 377.12 | 0.17 | 2.28 | 1587 |
| 2024-09-20 22:21:33.930 | MS1 | 121.4656763682 | 31.1446249345 | 89 | 504990 | -90.09 | 13.99 | 485.29 | 0.19 | 2.59 | 1560 |
| 2024-09-20 22:21:34.227 | MS1 | 121.4656727452 | 31.1446182936 | 89 | 504990 | -87.89 | 17.13 | 60.38 | 0.12 | 2.75 | 1588 |
| 2024-09-20 22:21:35.747 | MS1 | 121.4656730612 | 31.1446187861 | 89 | 504990 | -85.47 | 16.13 | 52.90 | 0.13 | 2.56 | 1583 |
| 2024-09-20 22:21:36.576 | MS1 | 121.4656725657 | 31.1446204908 | 89 | 504990 | -90.41 | 14.52 | 99.36 | 0.09 | 2.21 | 1594 |
| 2024-09-20 22:21:37.215 | MS1 | 121.4656663043 | 31.1446240965 | 89 | 504990 | -92.99 | 11.51 | 64.79 | 0.09 | 2.19 | 1592 |
| 2024-09-20 22:21:38.746 | MS1 | 121.4656688114 | 31.1446299869 | 89 | 504990 | -93.14 | 7.66 | 65.88 | 0.14 | 2.20 | 1572 |
| 2024-09-20 22:21:39.990 | MS1 | 121.4656733804 | 31.1446327331 | 89 | 504990 | -90.69 | 12.22 | 73.31 | 0.20 | 2.22 | 1600 |
| 2024-09-20 22:21:40.173 | MS1 | 121.4656624982 | 31.1446344872 | 89 | 504990 | -89.87 | 8.90 | 412.70 | 0.19 | 2.78 | 1572 |
| 2024-09-20 22:21:41.887 | MS1 | 121.4656696781 | 31.1446270147 | 89 | 504990 | -90.86 | 9.58 | 536.91 | 0.04 | 2.74 | 1575 |
| 2024-09-20 22:21:42.123 | MS1 | 121.4656592513 | 31.1446195975 | 89 | 504990 | -92.02 | 7.15 | 555.77 | 0.15 | 2.38 | 1586 |

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
| 3210086 | 3 | 121.4748992362 | 31.1494821557 | 324 | 7 | 11 | 27.9 | TDD | 339 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3216023 | 2 | 121.4745755337 | 31.1536378189 | 178 | 4 | 9 | 17.3 | TDD | 89 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3219659 | 1 | 121.4643117840 | 31.1539912857 | 111 | 13 | 1 | 21.1 | TDD | 681 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3225727 | 4 | 121.4729468178 | 31.1506711338 | 195 | 5 | 4 | 19.8 | TDD | 25 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.879 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.899 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.017 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.017 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.735 | NREventA3 | measId:2;ServCellPCI:446;Se... |
| 2024-09-20 22:21:37.975 | NRHandoverAttempt | SourcePCI:446;SourceNR-ARFC... |
| 2024-09-20 22:21:38.005 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.020 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.155 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.155 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219659 | 1 | 11.4221 | 18.6045 | -114.6006 | 8.5815 | 88.9130 | 0.0071 | 0.0029 |
| 2024_09_20 22:00 | 3216023 | 2 | 80.8874 | 86.8761 | -114.6934 | 12.0049 | 169.0525 | 0.0007 | 0.0066 |
| 2024_09_20 22:00 | 3210086 | 3 | 18.6296 | 6.3757 | -117.0931 | 8.0459 | 106.3206 | 0.0062 | 0.0167 |
| 2024_09_20 22:00 | 3225727 | 4 | 10.6273 | 10.0838 | -114.6991 | 12.9134 | 188.6741 | 0.0110 | 0.0191 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412847_84AB206A | 504990 | 89 | -88.2 | 504990 | 681 | -88.1 | 504990 | 339 | -100.1 | 504990 | 25 |
| MR_1774412847_2F95FF3C | 504990 | 89 | -87.4 | 504990 | 681 | -87.7 | 504990 | 339 | -98.9 | 504990 | 25 |
| MR_1774412847_1DCB83E9 | 504990 | 89 | -87.4 | 504990 | 681 | -87.1 | 504990 | 339 | -99.5 | 504990 | 25 |
| MR_1774412847_F9C60807 | 504990 | 89 | -89.8 | 504990 | 681 | -87.5 | 504990 | 339 | -100.4 | 504990 | 25 |
| MR_1774412847_01F1B4FA | 504990 | 89 | -88.7 | 504990 | 681 | -86.6 | 504990 | 339 | -99.3 | 504990 | 25 |
| MR_1774412847_14D859D6 | 504990 | 89 | -86.7 | 504990 | 681 | -88.1 | 504990 | 339 | -99.3 | 504990 | 25 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 331: `e5015853-a25...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e5015853-a252-4dd0-885b-c4dd1d0ae5e8` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[331] topology](images/train_0331.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3271202_1 by 10 degrees
- `C2`: Decrease A3 Offset threshold for 3220512_4
- `C3`: Add neighbor relationship between 3278862_2 and 3220512_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220512_4
- `C5`: Increase A3 Offset threshold for 3220512_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220512_4
- `C7`: Lift the tilt angle of 3271202_1 by 10 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271202_1
- `C9`: Decrease A3 Offset threshold for 3271202_1
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease transmission power for 3271202_1
- `C12`: Check test server and transmission issues **← 정답**
- `C13`: Decrease transmission power for 3220512_4
- `C14`: Increase transmission power for 3271202_1
- `C15`: Increase A3 Offset threshold for 3271202_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271202_1
- `C17`: Add neighbor relationship between 3271202_1 and 3220512_4
- `C18`: Increase transmission power for 3220512_4
- `C19`: Adjust the azimuth of 3271202_1 by 50 degrees
- `C20`: Adjust the azimuth of 3220512_4 by 18 degrees
- `C21`: Lift the tilt angle  of 3220512_4 by 9 degrees
- `C22`: Press down the tilt angle  of 3220512_4 by 9 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.384 | MS1 | 121.4656747692 | 31.1446239705 | 151 | 504990 | -90.33 | 17.86 | 354.97 | 0.06 | 2.28 | 1578 |
| 2024-09-20 22:21:32.307 | MS1 | 121.4656714460 | 31.1446267474 | 151 | 504990 | -91.22 | 14.09 | 314.48 | 0.19 | 2.42 | 1571 |
| 2024-09-20 22:21:33.820 | MS1 | 121.4656656202 | 31.1446344549 | 151 | 504990 | -87.30 | 12.40 | 537.05 | 0.17 | 2.12 | 1573 |
| 2024-09-20 22:21:34.690 | MS1 | 121.4656678324 | 31.1446320319 | 151 | 504990 | -86.95 | 14.49 | 50.33 | 0.18 | 2.23 | 382 |
| 2024-09-20 22:21:35.951 | MS1 | 121.4656606318 | 31.1446274098 | 151 | 504990 | -85.85 | 12.66 | 60.42 | 0.16 | 2.66 | 333 |
| 2024-09-20 22:21:36.547 | MS1 | 121.4656626033 | 31.1446209942 | 151 | 504990 | -85.85 | 12.62 | 43.39 | 0.19 | 2.35 | 385 |
| 2024-09-20 22:21:37.181 | MS1 | 121.4656669350 | 31.1446251407 | 151 | 504990 | -91.80 | 9.64 | 78.63 | 0.04 | 2.57 | 401 |
| 2024-09-20 22:21:38.814 | MS1 | 121.4656604840 | 31.1446184031 | 151 | 504990 | -90.48 | 8.00 | 54.45 | 0.04 | 2.08 | 350 |
| 2024-09-20 22:21:39.138 | MS1 | 121.4656653439 | 31.1446336447 | 151 | 504990 | -89.13 | 12.42 | 88.51 | 0.13 | 2.88 | 363 |
| 2024-09-20 22:21:40.604 | MS1 | 121.4656580590 | 31.1446210774 | 151 | 504990 | -92.09 | 7.90 | 510.32 | 0.06 | 2.84 | 1570 |
| 2024-09-20 22:21:41.603 | MS1 | 121.4656751730 | 31.1446367689 | 151 | 504990 | -92.04 | 9.39 | 346.93 | 0.19 | 2.56 | 1579 |
| 2024-09-20 22:21:42.208 | MS1 | 121.4656765327 | 31.1446337978 | 151 | 504990 | -91.18 | 10.14 | 333.65 | 0.05 | 2.10 | 1594 |

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
| 3220512 | 4 | 121.4751213211 | 31.1457593427 | 244 | 7 | 7 | 28.7 | TDD | 367 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3236695 | 3 | 121.4657039222 | 31.1445913445 | 181 | 4 | 8 | 37.2 | TDD | 519 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3271202 | 1 | 121.4692946686 | 31.1458154298 | 154 | 6 | 0 | 27.8 | TDD | 151 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3278862 | 2 | 121.4713611913 | 31.1457511217 | 292 | 3 | 9 | 16.8 | TDD | 978 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.040 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.061 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.211 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.211 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.882 | NREventA3 | measId:2;ServCellPCI:954;Se... |
| 2024-09-20 22:21:38.122 | NRHandoverAttempt | SourcePCI:954;SourceNR-ARFC... |
| 2024-09-20 22:21:38.160 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.173 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.276 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.276 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271202 | 1 | 14.1800 | 16.0479 | -114.5061 | 7.8604 | 105.7882 | 0.0073 | 0.0102 |
| 2024_09_20 22:00 | 3278862 | 2 | 18.2274 | 13.2212 | -116.7285 | 12.9950 | 97.0538 | 0.0032 | 0.0097 |
| 2024_09_20 22:00 | 3236695 | 3 | 10.7431 | 9.6207 | -117.2935 | 6.9780 | 170.0836 | 0.0014 | 0.0173 |
| 2024_09_20 22:00 | 3220512 | 4 | 16.5907 | 7.9614 | -114.5859 | 15.7417 | 168.8398 | 0.0142 | 0.0089 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413752_A01CB061 | 504990 | 151 | -87.3 | 504990 | 367 | -87.8 | 504990 | 978 | -96.9 | 504990 | 519 |
| MR_1774413752_49DC8550 | 504990 | 151 | -86.0 | 504990 | 367 | -90.6 | 504990 | 978 | -98.6 | 504990 | 519 |
| MR_1774413752_3214DD8C | 504990 | 151 | -86.5 | 504990 | 367 | -87.4 | 504990 | 978 | -95.4 | 504990 | 519 |
| MR_1774413752_1CE1989D | 504990 | 151 | -85.3 | 504990 | 367 | -87.0 | 504990 | 978 | -96.7 | 504990 | 519 |
| MR_1774413752_16811AEB | 504990 | 151 | -87.6 | 504990 | 367 | -88.8 | 504990 | 978 | -95.1 | 504990 | 519 |
| MR_1774413752_7B93634B | 504990 | 151 | -85.3 | 504990 | 367 | -89.6 | 504990 | 978 | -98.5 | 504990 | 519 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 332: `2f0b8382-c1a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2f0b8382-c1a5-475f-a77c-2c2ed500da0c` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250705_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[332] topology](images/train_0332.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237529_3
- `C3`: Press down the tilt angle  of 3237529_3 by 6 degrees
- `C4`: Press down the tilt angle of 3250705_6 by 4 degrees
- `C5`: Decrease transmission power for 3250705_6
- `C6`: Add neighbor relationship between 3250705_6 and 3237529_3
- `C7`: Add neighbor relationship between 3222724_10 and 3237529_3
- `C8`: Lift the tilt angle  of 3237529_3 by 6 degrees
- `C9`: Adjust the azimuth of 3237529_3 by 4 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250705_6
- `C12`: Increase A3 Offset threshold for 3237529_3
- `C13`: Adjust the azimuth of 3250705_6 by 15 degrees
- `C14`: Decrease A3 Offset threshold for 3250705_6
- `C15`: Increase transmission power for 3250705_6
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237529_3
- `C17`: Increase transmission power for 3237529_3
- `C18`: Lift the tilt angle of 3250705_6 by 4 degrees
- `C19`: Decrease A3 Offset threshold for 3237529_3
- `C20`: Increase A3 Offset threshold for 3250705_6
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250705_6 **← 정답**
- `C22`: Decrease transmission power for 3237529_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.816 | MS1 | 121.4656708466 | 31.1446243654 | 286 | 504990 | -95.61 | 10.25 | 415.47 | 0.20 | 2.48 | 1570 |
| 2024-09-20 22:21:32.259 | MS1 | 121.4656737060 | 31.1446185977 | 79 | 504990 | -93.50 | 13.20 | 434.52 | 0.15 | 2.16 | 1564 |
| 2024-09-20 22:21:33.368 | MS1 | 121.4656656124 | 31.1446345572 | 712 | 504990 | -94.02 | 13.88 | 346.18 | 0.17 | 2.04 | 1567 |
| 2024-09-20 22:21:34.211 | MS1 | 121.4656630571 | 31.1446346503 | 484 | 152650 | -88.26 | 7.59 | 84.84 | 0.15 | 1.58 | 971 |
| 2024-09-20 22:21:35.917 | MS1 | 121.4656730373 | 31.1446228490 | 447 | 152650 | -93.40 | 6.31 | 58.46 | 0.16 | 1.97 | 948 |
| 2024-09-20 22:21:36.600 | MS1 | 121.4656779683 | 31.1446341303 | 488 | 152650 | -88.60 | 6.36 | 43.56 | 0.09 | 1.86 | 961 |
| 2024-09-20 22:21:37.101 | MS1 | 121.4656751593 | 31.1446251637 | 431 | 152650 | -87.57 | 3.20 | 56.09 | 0.05 | 1.75 | 934 |
| 2024-09-20 22:21:38.569 | MS1 | 121.4656729210 | 31.1446350669 | 484 | 152650 | -94.82 | 3.81 | 52.28 | 0.11 | 1.68 | 994 |
| 2024-09-20 22:21:39.595 | MS1 | 121.4656695683 | 31.1446378351 | 447 | 152650 | -90.70 | 3.77 | 74.90 | 0.01 | 1.52 | 921 |
| 2024-09-20 22:21:40.483 | MS1 | 121.4656779060 | 31.1446345398 | 488 | 152650 | -88.37 | 7.90 | 86.97 | 0.17 | 2.10 | 1578 |
| 2024-09-20 22:21:41.394 | MS1 | 121.4656772030 | 31.1446299571 | 431 | 152650 | -93.91 | 5.56 | 95.58 | 0.00 | 2.62 | 1583 |
| 2024-09-20 22:21:42.985 | MS1 | 121.4656629749 | 31.1446343283 | 484 | 152650 | -89.86 | 2.98 | 92.03 | 0.10 | 2.73 | 1575 |

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
| 3216361 | 13 | 121.4649317286 | 31.1443318211 | 166 | 9 | 1 | 28.3 | FDD | 447 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3216984 | 9 | 121.4710888761 | 31.1459808777 | 125 | 4 | 12 | 8.8 | FDD | 484 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3219372 | 1 | 121.4741585647 | 31.1497806424 | 342 | 9 | 9 | 1.5 | TDD | 481 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3222552 | 12 | 121.4652325217 | 31.1453678213 | 206 | 13 | 6 | 10.9 | FDD | 663 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3222724 | 10 | 121.4676622804 | 31.1471787096 | 208 | 6 | 6 | 13.0 | FDD | 488 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3228529 | 8 | 121.4741446940 | 31.1497586421 | 51 | 10 | 2 | 23.4 | FDD | 833 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3237529 | 3 | 121.4711851856 | 31.1543249935 | 202 | 5 | 3 | 17.7 | TDD | 845 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3243383 | 11 | 121.4693168018 | 31.1476096667 | 128 | 13 | 11 | 9.7 | FDD | 431 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3243545 | 2 | 121.4672771677 | 31.1488685108 | 220 | 12 | 6 | 13.7 | TDD | 712 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3246165 | 7 | 121.4716279604 | 31.1505496384 | 307 | 3 | 5 | 4.1 | FDD | 512 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3246484 | 4 | 121.4651796781 | 31.1539349760 | 358 | 7 | 4 | 27.2 | TDD | 79 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3250705 | 6 | 121.4666228873 | 31.1513085921 | 202 | 4 | 6 | 1.0 | TDD | 286 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3250868 | 5 | 121.4655778627 | 31.1557798456 | 138 | 8 | 12 | 18.9 | TDD | 274 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.918 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.933 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.083 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.083 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.793 | NREventA2 | measId:1;ServCellPCI:578;Se... |
| 2024-09-20 22:21:34.934 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.168 | NREventA5 | measId:3;ServCellPCI:578;Se... |
| 2024-09-20 22:21:35.237 | NRHandoverAttempt | SourcePCI:578;SourceNR-ARFC... |
| 2024-09-20 22:21:35.266 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.281 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.428 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.428 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219372 | 1 | 5.8218 | 17.8930 | -117.5493 | 19.0170 | 143.0020 | 0.0021 | 0.0084 |
| 2024_09_20 22:00 | 3243545 | 2 | 16.9158 | 18.0429 | -116.1635 | 6.3299 | 191.7812 | 0.0041 | 0.0041 |
| 2024_09_20 22:00 | 3237529 | 3 | 14.0018 | 12.3416 | -116.5627 | 7.1079 | 113.0983 | 0.0097 | 0.0162 |
| 2024_09_20 22:00 | 3246484 | 4 | 18.9278 | 18.9676 | -114.2900 | 14.0384 | 193.5353 | 0.0102 | 0.0084 |
| 2024_09_20 22:00 | 3250868 | 5 | 7.8589 | 16.6646 | -115.1408 | 16.7189 | 175.9699 | 0.0018 | 0.0190 |
| 2024_09_20 22:00 | 3250705 | 6 | 17.6244 | 6.5137 | -116.5475 | 5.4020 | 134.1665 | 0.0048 | 0.0176 |
| 2024_09_20 22:00 | 3246165 | 7 | 19.6069 | 10.5064 | -114.8426 | 3.3705 | 50.2694 | 0.0147 | 0.0013 |
| 2024_09_20 22:00 | 3228529 | 8 | 12.1678 | 13.2220 | -117.5043 | 4.0752 | 56.2988 | 0.0016 | 0.0174 |
| 2024_09_20 22:00 | 3216984 | 9 | 14.0194 | 8.4362 | -114.2058 | 3.3213 | 46.2582 | 0.0151 | 0.0182 |
| 2024_09_20 22:00 | 3222724 | 10 | 16.7694 | 12.2240 | -116.3111 | 3.8561 | 26.9482 | 0.0012 | 0.0192 |
| 2024_09_20 22:00 | 3243383 | 11 | 12.7438 | 18.1206 | -116.8343 | 3.0040 | 34.0419 | 0.0043 | 0.0166 |
| 2024_09_20 22:00 | 3222552 | 12 | 10.1374 | 6.1750 | -117.7298 | 4.1918 | 42.8661 | 0.0082 | 0.0014 |
| 2024_09_20 22:00 | 3216361 | 13 | 14.7505 | 18.1608 | -117.0374 | 4.7756 | 48.7323 | 0.0002 | 0.0123 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413559_6C857F3D | 152650 | 484 | -89.4 | 152650 | 663 | -95.6 | 152650 | 833 | -97.3 | 152650 | 512 |
| MR_1774413559_20922813 | 152650 | 484 | -89.6 | 152650 | 663 | -95.4 | 152650 | 833 | -97.6 | 152650 | 512 |
| MR_1774413559_7312E91F | 152650 | 484 | -88.1 | 152650 | 663 | -94.7 | 152650 | 833 | -94.6 | 152650 | 512 |
| MR_1774413559_A5323019 | 504990 | 712 | -96.0 | 504990 | 845 | -95.3 | 504990 | 274 | -94.7 | 504990 | 481 |
| MR_1774413559_FEEA1DF7 | 504990 | 712 | -92.4 | 504990 | 845 | -96.1 | 504990 | 274 | -92.8 | 504990 | 481 |
| MR_1774413559_5FAC7AA0 | 504990 | 712 | -93.6 | 504990 | 845 | -92.6 | 504990 | 274 | -94.4 | 504990 | 481 |
| MR_1774413559_DEF2F987 | 504990 | 712 | -95.7 | 504990 | 845 | -93.0 | 504990 | 274 | -95.4 | 504990 | 481 |
| MR_1774413559_E793A215 | 504990 | 712 | -94.9 | 504990 | 845 | -92.7 | 504990 | 274 | -93.1 | 504990 | 481 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 333: `d166c12c-d82...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d166c12c-d821-4dc4-9e77-2a3ef37cc6b6` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Decrease A3 Offset threshold for 3263793_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[333] topology](images/train_0333.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3263793_1 **← 정답**
- `C2`: Press down the tilt angle of 3263793_1 by 7 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233330_3
- `C4`: Adjust the azimuth of 3233330_3 by 50 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233330_3
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Add neighbor relationship between 3263793_1 and 3233330_3
- `C8`: Press down the tilt angle  of 3233330_3 by 8 degrees
- `C9`: Increase A3 Offset threshold for 3263793_1
- `C10`: Increase A3 Offset threshold for 3233330_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263793_1
- `C12`: Lift the tilt angle  of 3233330_3 by 8 degrees
- `C13`: Check test server and transmission issues
- `C14`: Lift the tilt angle of 3263793_1 by 7 degrees
- `C15`: Add neighbor relationship between 3246324_2 and 3233330_3
- `C16`: Increase transmission power for 3263793_1
- `C17`: Decrease A3 Offset threshold for 3233330_3
- `C18`: Adjust the azimuth of 3263793_1 by 50 degrees
- `C19`: Decrease transmission power for 3233330_3
- `C20`: Decrease transmission power for 3263793_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263793_1
- `C22`: Increase transmission power for 3233330_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.995 | MS1 | 121.4656681018 | 31.1446241581 | 449 | 504990 | -79.71 | 15.39 | 542.89 | 0.13 | 2.47 | 1598 |
| 2024-09-20 22:21:32.494 | MS1 | 121.4656616178 | 31.1446293543 | 449 | 504990 | -76.06 | 14.31 | 384.67 | 0.02 | 2.57 | 1560 |
| 2024-09-20 22:21:33.383 | MS1 | 121.4656679228 | 31.1446368963 | 449 | 504990 | -75.98 | 15.16 | 393.11 | 0.11 | 2.17 | 1590 |
| 2024-09-20 22:21:34.709 | MS1 | 121.4656694739 | 31.1446271168 | 449 | 504990 | -91.15 | -0.69 | 24.07 | 0.11 | 1.50 | 1563 |
| 2024-09-20 22:21:35.158 | MS1 | 121.4656702949 | 31.1446198640 | 449 | 504990 | -89.23 | -2.79 | 80.46 | 0.12 | 1.23 | 1580 |
| 2024-09-20 22:21:36.391 | MS1 | 121.4656617088 | 31.1446330902 | 449 | 504990 | -87.51 | -1.78 | 27.49 | 0.03 | 1.22 | 1574 |
| 2024-09-20 22:21:37.432 | MS1 | 121.4656611882 | 31.1446273118 | 449 | 504990 | -88.37 | -0.86 | 59.24 | 0.03 | 1.13 | 1590 |
| 2024-09-20 22:21:38.737 | MS1 | 121.4656757357 | 31.1446252891 | 449 | 504990 | -91.77 | -1.12 | 70.33 | 0.10 | 1.39 | 1573 |
| 2024-09-20 22:21:39.176 | MS1 | 121.4656777866 | 31.1446181985 | 869 | 504990 | -75.09 | 14.51 | 171.82 | 0.10 | 1.39 | 1566 |
| 2024-09-20 22:21:40.402 | MS1 | 121.4656764825 | 31.1446331042 | 869 | 504990 | -80.72 | 17.45 | 551.82 | 0.03 | 2.05 | 1596 |
| 2024-09-20 22:21:41.706 | MS1 | 121.4656665964 | 31.1446235958 | 869 | 504990 | -81.27 | 15.50 | 319.68 | 0.18 | 2.43 | 1591 |
| 2024-09-20 22:21:42.538 | MS1 | 121.4656756859 | 31.1446249978 | 869 | 504990 | -76.01 | 12.74 | 429.89 | 0.15 | 2.36 | 1587 |

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
| 3233330 | 3 | 121.4735506659 | 31.1472932545 | 142 | 6 | 1 | 33.1 | TDD | 869 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3241411 | 4 | 121.4731056981 | 31.1516690915 | 135 | 8 | 8 | 34.9 | TDD | 285 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3246324 | 2 | 121.4696103526 | 31.1553461136 | 174 | 11 | 8 | 34.4 | TDD | 650 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3263793 | 1 | 121.4705017621 | 31.1530921439 | 89 | 5 | 4 | 33.8 | TDD | 449 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.386 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.408 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.519 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.519 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.263 | NREventA3 | measId:2;ServCellPCI:31;Ser... |
| 2024-09-20 22:21:38.503 | NRHandoverAttempt | SourcePCI:31;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.553 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.568 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.695 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.695 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263793 | 1 | 6.4157 | 17.7538 | -116.4669 | 6.7674 | 126.5275 | 0.0104 | 0.1253 |
| 2024_09_20 22:00 | 3246324 | 2 | 10.4495 | 16.1977 | -116.8386 | 8.7488 | 95.6419 | 0.0106 | 0.0171 |
| 2024_09_20 22:00 | 3233330 | 3 | 14.0161 | 7.4754 | -115.0511 | 10.5768 | 107.4528 | 0.0154 | 0.0148 |
| 2024_09_20 22:00 | 3241411 | 4 | 16.9976 | 10.3283 | -116.3753 | 12.1097 | 165.0676 | 0.0153 | 0.0069 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414459_CC64EE7A | 504990 | 869 | -86.6 | 504990 | 449 | -89.6 | 504990 | 650 | -85.2 | 504990 | 285 |
| MR_1774414459_3DC4EED3 | 504990 | 449 | -89.7 | 504990 | 869 | -85.3 | 504990 | 650 | -88.6 | 504990 | 285 |
| MR_1774414459_2DB38548 | 504990 | 869 | -87.0 | 504990 | 449 | -91.6 | 504990 | 650 | -87.7 | 504990 | 285 |
| MR_1774414459_AC547457 | 504990 | 449 | -92.2 | 504990 | 869 | -84.8 | 504990 | 650 | -87.4 | 504990 | 285 |
| MR_1774414459_4889B217 | 504990 | 449 | -92.4 | 504990 | 869 | -87.7 | 504990 | 650 | -86.4 | 504990 | 285 |
| MR_1774414459_D90B0E50 | 504990 | 869 | -87.4 | 504990 | 449 | -92.9 | 504990 | 650 | -87.0 | 504990 | 285 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 334: `22a8890e-c80...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `22a8890e-c803-4643-9ef7-06d50869adb4` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[334] topology](images/train_0334.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3212717_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212717_1
- `C3`: Lift the tilt angle of 3212717_1 by 10 degrees
- `C4`: Decrease transmission power for 3212717_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Adjust the azimuth of 3212717_1 by 50 degrees
- `C7`: Increase A3 Offset threshold for 3212717_1
- `C8`: Check test server and transmission issues **← 정답**
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212717_1
- `C10`: Increase transmission power for 3255615_2
- `C11`: Add neighbor relationship between 3227780_4 and 3255615_2
- `C12`: Increase transmission power for 3212717_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255615_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255615_2
- `C15`: Decrease transmission power for 3255615_2
- `C16`: Add neighbor relationship between 3212717_1 and 3255615_2
- `C17`: Decrease A3 Offset threshold for 3255615_2
- `C18`: Increase A3 Offset threshold for 3255615_2
- `C19`: Lift the tilt angle  of 3255615_2 by 10 degrees
- `C20`: Press down the tilt angle of 3212717_1 by 10 degrees
- `C21`: Adjust the azimuth of 3255615_2 by 50 degrees
- `C22`: Press down the tilt angle  of 3255615_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.583 | MS1 | 121.4656633245 | 31.1446345522 | 544 | 504990 | -89.23 | 13.61 | 382.28 | 0.13 | 2.98 | 1599 |
| 2024-09-20 22:21:32.330 | MS1 | 121.4656765085 | 31.1446297336 | 544 | 504990 | -90.92 | 16.02 | 488.19 | 0.00 | 2.54 | 1574 |
| 2024-09-20 22:21:33.913 | MS1 | 121.4656738942 | 31.1446250653 | 544 | 504990 | -85.77 | 13.32 | 328.99 | 0.05 | 2.45 | 1581 |
| 2024-09-20 22:21:34.232 | MS1 | 121.4656620604 | 31.1446331059 | 544 | 504990 | -89.77 | 16.20 | 99.16 | 0.11 | 2.20 | 380 |
| 2024-09-20 22:21:35.911 | MS1 | 121.4656709999 | 31.1446203277 | 544 | 504990 | -89.22 | 16.25 | 72.28 | 0.16 | 2.93 | 347 |
| 2024-09-20 22:21:36.505 | MS1 | 121.4656776263 | 31.1446237051 | 544 | 504990 | -89.35 | 15.81 | 57.42 | 0.13 | 2.64 | 380 |
| 2024-09-20 22:21:37.737 | MS1 | 121.4656708222 | 31.1446359868 | 544 | 504990 | -93.73 | 7.07 | 75.82 | 0.16 | 2.46 | 326 |
| 2024-09-20 22:21:38.634 | MS1 | 121.4656746392 | 31.1446312418 | 544 | 504990 | -89.19 | 8.67 | 87.87 | 0.11 | 2.01 | 368 |
| 2024-09-20 22:21:39.936 | MS1 | 121.4656629739 | 31.1446203708 | 544 | 504990 | -89.51 | 11.37 | 91.57 | 0.11 | 2.31 | 405 |
| 2024-09-20 22:21:40.381 | MS1 | 121.4656617418 | 31.1446234941 | 544 | 504990 | -93.90 | 7.40 | 524.68 | 0.09 | 2.97 | 1584 |
| 2024-09-20 22:21:41.356 | MS1 | 121.4656592079 | 31.1446186153 | 544 | 504990 | -93.26 | 11.26 | 453.69 | 0.16 | 2.29 | 1589 |
| 2024-09-20 22:21:42.480 | MS1 | 121.4656775683 | 31.1446317822 | 544 | 504990 | -91.14 | 9.41 | 380.46 | 0.13 | 2.99 | 1589 |

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
| 3212717 | 1 | 121.4725770596 | 31.1542597993 | 346 | 9 | 1 | 27.5 | TDD | 544 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3220748 | 3 | 121.4759119280 | 31.1490841797 | 146 | 5 | 0 | 46.3 | TDD | 20 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3227780 | 4 | 121.4737520217 | 31.1451960310 | 333 | 6 | 12 | 44.3 | TDD | 93 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3255615 | 2 | 121.4662883365 | 31.1453924895 | 104 | 12 | 5 | 16.7 | TDD | 746 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.975 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.997 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.126 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.126 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.827 | NREventA3 | measId:2;ServCellPCI:219;Se... |
| 2024-09-20 22:21:38.067 | NRHandoverAttempt | SourcePCI:219;SourceNR-ARFC... |
| 2024-09-20 22:21:38.112 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.125 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.260 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.260 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212717 | 1 | 13.7820 | 18.2818 | -115.4145 | 12.8966 | 141.3245 | 0.0075 | 0.0146 |
| 2024_09_20 22:00 | 3255615 | 2 | 5.6027 | 15.7160 | -116.1539 | 12.6387 | 192.3224 | 0.0133 | 0.0052 |
| 2024_09_20 22:00 | 3220748 | 3 | 13.1419 | 9.0176 | -117.4358 | 11.7573 | 194.2961 | 0.0115 | 0.0000 |
| 2024_09_20 22:00 | 3227780 | 4 | 8.9357 | 18.8762 | -115.7421 | 11.9256 | 93.0691 | 0.0196 | 0.0160 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412599_D74B2E96 | 504990 | 544 | -88.3 | 504990 | 746 | -90.7 | 504990 | 93 | -98.1 | 504990 | 20 |
| MR_1774412599_305497BA | 504990 | 544 | -88.2 | 504990 | 746 | -91.1 | 504990 | 93 | -99.9 | 504990 | 20 |
| MR_1774412599_B190936B | 504990 | 544 | -90.6 | 504990 | 746 | -93.4 | 504990 | 93 | -98.5 | 504990 | 20 |
| MR_1774412599_10475C7A | 504990 | 544 | -89.5 | 504990 | 746 | -92.8 | 504990 | 93 | -98.5 | 504990 | 20 |
| MR_1774412599_6CF389A1 | 504990 | 544 | -91.1 | 504990 | 746 | -90.4 | 504990 | 93 | -97.7 | 504990 | 20 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 335: `be218f76-998...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `be218f76-9988-4701-bce1-a6010457e38d` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Add neighbor relationship between 3232200_1 and 3245976_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[335] topology](images/train_0335.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Check test server and transmission issues
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232200_1
- `C4`: Increase transmission power for 3245976_2
- `C5`: Decrease A3 Offset threshold for 3232200_1
- `C6`: Lift the tilt angle of 3232200_1 by 9 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232200_1
- `C8`: Increase A3 Offset threshold for 3232200_1
- `C9`: Decrease transmission power for 3232200_1
- `C10`: Press down the tilt angle of 3232200_1 by 9 degrees
- `C11`: Adjust the azimuth of 3245976_2 by 43 degrees
- `C12`: Decrease transmission power for 3245976_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245976_2
- `C14`: Increase transmission power for 3232200_1
- `C15`: Add neighbor relationship between 3215629_4 and 3245976_2
- `C16`: Press down the tilt angle  of 3245976_2 by 5 degrees
- `C17`: Add neighbor relationship between 3232200_1 and 3245976_2 **← 정답**
- `C18`: Adjust the azimuth of 3232200_1 by 27 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245976_2
- `C20`: Lift the tilt angle  of 3245976_2 by 5 degrees
- `C21`: Increase A3 Offset threshold for 3245976_2
- `C22`: Decrease A3 Offset threshold for 3245976_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.373 | MS1 | 121.4656605241 | 31.1446328553 | 952 | 504990 | -83.55 | 12.41 | 385.18 | 0.16 | 2.33 | 1576 |
| 2024-09-20 22:21:32.659 | MS1 | 121.4656725826 | 31.1446209288 | 952 | 504990 | -82.96 | 14.23 | 560.15 | 0.12 | 2.80 | 1587 |
| 2024-09-20 22:21:33.310 | MS1 | 121.4656705268 | 31.1446303825 | 952 | 504990 | -79.33 | 12.51 | 345.15 | 0.15 | 2.54 | 1589 |
| 2024-09-20 22:21:34.791 | MS1 | 121.4656665962 | 31.1446348925 | 952 | 504990 | -88.02 | -3.33 | 55.24 | 0.02 | 1.43 | 1566 |
| 2024-09-20 22:21:35.704 | MS1 | 121.4656643018 | 31.1446343158 | 952 | 504990 | -86.37 | -2.70 | 50.55 | 0.08 | 1.08 | 1598 |
| 2024-09-20 22:21:36.912 | MS1 | 121.4656674334 | 31.1446331936 | 952 | 504990 | -86.86 | -0.81 | 50.58 | 0.08 | 1.48 | 1566 |
| 2024-09-20 22:21:37.839 | MS1 | 121.4656631475 | 31.1446351081 | 952 | 504990 | -88.69 | -0.73 | 40.16 | 0.03 | 1.03 | 1567 |
| 2024-09-20 22:21:38.699 | MS1 | 121.4656667610 | 31.1446353638 | 952 | 504990 | -82.64 | 17.56 | 423.00 | 0.15 | 1.03 | 1574 |
| 2024-09-20 22:21:39.255 | MS1 | 121.4656596191 | 31.1446234002 | 952 | 504990 | -78.23 | 16.64 | 603.79 | 0.01 | 1.44 | 1563 |
| 2024-09-20 22:21:40.280 | MS1 | 121.4656601482 | 31.1446183647 | 952 | 504990 | -79.88 | 13.33 | 428.82 | 0.20 | 2.30 | 1590 |
| 2024-09-20 22:21:41.901 | MS1 | 121.4656600871 | 31.1446200520 | 952 | 504990 | -75.23 | 12.17 | 396.12 | 0.17 | 2.25 | 1592 |
| 2024-09-20 22:21:42.311 | MS1 | 121.4656661225 | 31.1446267456 | 952 | 504990 | -79.90 | 14.87 | 381.18 | 0.12 | 2.53 | 1575 |

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
| 3211922 | 3 | 121.4711548114 | 31.1442211934 | 318 | 5 | 1 | 24.9 | TDD | 163 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3215629 | 4 | 121.4715255996 | 31.1488257767 | 203 | 7 | 11 | 34.1 | TDD | 249 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3232200 | 1 | 121.4648042191 | 31.1551437597 | 149 | 8 | 4 | 29.4 | TDD | 952 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3245976 | 2 | 121.4759105302 | 31.1500358861 | 195 | 3 | 8 | 49.6 | TDD | 665 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.338 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.360 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.495 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.495 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.225 | NREventA3 | measId:2;ServCellPCI:852;Se... |
| 2024-09-20 22:21:36.225 | NREventA3 | measId:2;ServCellPCI:852;Se... |
| 2024-09-20 22:21:37.225 | NREventA3 | measId:2;ServCellPCI:852;Se... |
| 2024-09-20 22:21:39.725 | NRRRCReestablishAttempt | PCI:852 |
| 2024-09-20 22:21:39.736 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.749 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.898 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.898 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232200 | 1 | 19.8303 | 9.6090 | -117.8168 | 14.0937 | 98.8550 | 0.0018 | 0.1635 |
| 2024_09_20 22:00 | 3245976 | 2 | 16.7257 | 15.3807 | -117.1306 | 17.4439 | 121.1581 | 0.0046 | 0.0123 |
| 2024_09_20 22:00 | 3211922 | 3 | 19.2796 | 6.9754 | -114.9763 | 6.5404 | 95.1821 | 0.0169 | 0.0144 |
| 2024_09_20 22:00 | 3215629 | 4 | 14.8895 | 10.6463 | -116.8709 | 12.7084 | 193.5405 | 0.0165 | 0.0167 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416384_344AA8F6 | 504990 | 952 | -89.1 | 504990 | 665 | -83.9 | 504990 | 249 | -87.5 | 504990 | 163 |
| MR_1774416384_F98EB4AF | 504990 | 665 | -81.0 | 504990 | 952 | -89.7 | 504990 | 249 | -88.1 | 504990 | 163 |
| MR_1774416384_94E740BE | 504990 | 952 | -89.1 | 504990 | 665 | -83.5 | 504990 | 249 | -89.4 | 504990 | 163 |
| MR_1774416384_432EF3F0 | 504990 | 665 | -81.6 | 504990 | 952 | -88.3 | 504990 | 249 | -89.4 | 504990 | 163 |
| MR_1774416384_21F5C42E | 504990 | 952 | -87.5 | 504990 | 665 | -82.0 | 504990 | 249 | -90.0 | 504990 | 163 |
| MR_1774416384_64F79EAE | 504990 | 665 | -80.7 | 504990 | 952 | -87.2 | 504990 | 249 | -89.7 | 504990 | 163 |
| MR_1774416384_1ADB1C9E | 504990 | 952 | -88.4 | 504990 | 665 | -83.2 | 504990 | 249 | -86.6 | 504990 | 163 |
| MR_1774416384_7F4F82BC | 504990 | 952 | -89.1 | 504990 | 665 | -83.0 | 504990 | 249 | -88.2 | 504990 | 163 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 336: `e3ef95a5-690...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e3ef95a5-690e-468e-9c42-e57328c6f1c1` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3252276_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[336] topology](images/train_0336.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3225469_2
- `C2`: Press down the tilt angle  of 3225469_2 by 8 degrees
- `C3`: Increase A3 Offset threshold for 3225469_2
- `C4`: Adjust the azimuth of 3225469_2 by 50 degrees
- `C5`: Increase transmission power for 3225469_2
- `C6`: Lift the tilt angle of 3252276_4 by 5 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225469_2
- `C8`: Check test server and transmission issues
- `C9`: Press down the tilt angle of 3252276_4 by 5 degrees
- `C10`: Increase transmission power for 3252276_4
- `C11`: Decrease transmission power for 3252276_4
- `C12`: Decrease transmission power for 3225469_2
- `C13`: Adjust the azimuth of 3252276_4 by 8 degrees
- `C14`: Increase A3 Offset threshold for 3252276_4
- `C15`: Add neighbor relationship between 3245404_1 and 3225469_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225469_2
- `C17`: Lift the tilt angle  of 3225469_2 by 8 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252276_4 **← 정답**
- `C19`: Add neighbor relationship between 3252276_4 and 3225469_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252276_4
- `C21`: Decrease A3 Offset threshold for 3252276_4
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.956 | MS1 | 121.4656643931 | 31.1446188563 | 927 | 504990 | -91.94 | 12.13 | 455.54 | 0.20 | 2.54 | 1592 |
| 2024-09-20 22:21:32.618 | MS1 | 121.4656588812 | 31.1446298521 | 927 | 504990 | -87.33 | 14.42 | 594.71 | 0.10 | 2.55 | 1561 |
| 2024-09-20 22:21:33.288 | MS1 | 121.4656626618 | 31.1446233901 | 927 | 504990 | -85.85 | 15.90 | 459.15 | 0.11 | 2.52 | 1572 |
| 2024-09-20 22:21:34.820 | MS1 | 121.4656616376 | 31.1446341649 | 927 | 504990 | -91.28 | 14.48 | 87.41 | 0.60 | 2.39 | 522 |
| 2024-09-20 22:21:35.231 | MS1 | 121.4656723201 | 31.1446288676 | 927 | 504990 | -91.22 | 17.45 | 91.34 | 0.69 | 2.69 | 618 |
| 2024-09-20 22:21:36.634 | MS1 | 121.4656661691 | 31.1446280168 | 927 | 504990 | -88.78 | 12.07 | 61.81 | 0.57 | 2.80 | 624 |
| 2024-09-20 22:21:37.478 | MS1 | 121.4656624650 | 31.1446275290 | 927 | 504990 | -91.48 | 11.77 | 72.58 | 0.56 | 2.98 | 563 |
| 2024-09-20 22:21:38.360 | MS1 | 121.4656728711 | 31.1446350242 | 927 | 504990 | -92.60 | 7.27 | 67.31 | 0.51 | 2.40 | 699 |
| 2024-09-20 22:21:39.553 | MS1 | 121.4656667113 | 31.1446191942 | 927 | 504990 | -89.10 | 11.61 | 57.44 | 0.51 | 2.95 | 621 |
| 2024-09-20 22:21:40.981 | MS1 | 121.4656602689 | 31.1446184440 | 927 | 504990 | -89.17 | 11.12 | 353.29 | 0.01 | 2.92 | 1561 |
| 2024-09-20 22:21:41.996 | MS1 | 121.4656697530 | 31.1446275282 | 927 | 504990 | -92.62 | 7.74 | 415.51 | 0.13 | 2.16 | 1585 |
| 2024-09-20 22:21:42.128 | MS1 | 121.4656583195 | 31.1446319649 | 927 | 504990 | -93.59 | 8.13 | 475.06 | 0.08 | 2.77 | 1592 |

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
| 3224981 | 3 | 121.4751538729 | 31.1544907492 | 278 | 0 | 10 | 23.0 | TDD | 381 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3225469 | 2 | 121.4687050544 | 31.1455793574 | 118 | 0 | 6 | 42.0 | TDD | 357 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3245404 | 1 | 121.4680582374 | 31.1559101034 | 76 | 6 | 12 | 17.0 | TDD | 585 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3252276 | 4 | 121.4735950341 | 31.1550169143 | 221 | 3 | 4 | 48.6 | TDD | 927 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.533 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.548 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.687 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.687 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.341 | NREventA3 | measId:2;ServCellPCI:969;Se... |
| 2024-09-20 22:21:38.581 | NRHandoverAttempt | SourcePCI:969;SourceNR-ARFC... |
| 2024-09-20 22:21:38.619 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.632 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.780 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.780 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245404 | 1 | 18.1697 | 19.4487 | -116.9399 | 5.0055 | 145.0416 | 0.0133 | 0.0054 |
| 2024_09_20 22:00 | 3225469 | 2 | 12.6864 | 13.3666 | -117.2190 | 18.5102 | 104.6933 | 0.0116 | 0.0110 |
| 2024_09_20 22:00 | 3224981 | 3 | 14.5941 | 6.6056 | -114.2123 | 8.3650 | 87.0710 | 0.0120 | 0.0170 |
| 2024_09_20 22:00 | 3252276 | 4 | 9.0644 | 17.0199 | -117.8279 | 18.2708 | 159.5263 | 0.0008 | 0.0096 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413276_0E2DFF76 | 504990 | 927 | -92.2 | 504990 | 357 | -96.5 | 504990 | 585 | -99.8 | 504990 | 381 |
| MR_1774413276_B413B514 | 504990 | 927 | -92.4 | 504990 | 357 | -97.9 | 504990 | 585 | -100.6 | 504990 | 381 |
| MR_1774413276_9AB28ABC | 504990 | 927 | -92.1 | 504990 | 357 | -99.2 | 504990 | 585 | -98.5 | 504990 | 381 |
| MR_1774413276_44EFF7AB | 504990 | 927 | -92.7 | 504990 | 357 | -98.4 | 504990 | 585 | -102.2 | 504990 | 381 |
| MR_1774413276_75BC40BF | 504990 | 927 | -92.8 | 504990 | 357 | -99.8 | 504990 | 585 | -99.3 | 504990 | 381 |
| MR_1774413276_0D43DF6C | 504990 | 927 | -91.8 | 504990 | 357 | -99.3 | 504990 | 585 | -99.3 | 504990 | 381 |
| MR_1774413276_40768462 | 504990 | 927 | -89.6 | 504990 | 357 | -96.5 | 504990 | 585 | -100.4 | 504990 | 381 |
| MR_1774413276_2A752E5E | 504990 | 927 | -92.5 | 504990 | 357 | -96.4 | 504990 | 585 | -99.7 | 504990 | 381 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 337: `0fad3aeb-539...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0fad3aeb-539a-41f2-81cd-0dce416ecee9` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Add neighbor relationship between 3277908_1 and 3247727_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[337] topology](images/train_0337.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3247727_2
- `C2`: Check test server and transmission issues
- `C3`: Lift the tilt angle of 3277908_1 by 4 degrees
- `C4`: Add neighbor relationship between 3277908_1 and 3247727_2 **← 정답**
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247727_2
- `C6`: Press down the tilt angle  of 3247727_2 by 3 degrees
- `C7`: Increase transmission power for 3247727_2
- `C8`: Press down the tilt angle of 3277908_1 by 4 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277908_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277908_1
- `C11`: Lift the tilt angle  of 3247727_2 by 3 degrees
- `C12`: Add neighbor relationship between 3253347_3 and 3247727_2
- `C13`: Decrease transmission power for 3247727_2
- `C14`: Adjust the azimuth of 3277908_1 by 50 degrees
- `C15`: Decrease transmission power for 3277908_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247727_2
- `C17`: Decrease A3 Offset threshold for 3247727_2
- `C18`: Increase transmission power for 3277908_1
- `C19`: Increase A3 Offset threshold for 3277908_1
- `C20`: Adjust the azimuth of 3247727_2 by 41 degrees
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease A3 Offset threshold for 3277908_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.588 | MS1 | 121.4656752302 | 31.1446356510 | 635 | 504990 | -84.31 | 15.49 | 478.13 | 0.01 | 2.30 | 1577 |
| 2024-09-20 22:21:32.677 | MS1 | 121.4656693126 | 31.1446216139 | 635 | 504990 | -80.94 | 16.51 | 410.26 | 0.04 | 2.00 | 1578 |
| 2024-09-20 22:21:33.675 | MS1 | 121.4656670759 | 31.1446347670 | 635 | 504990 | -79.99 | 14.32 | 577.29 | 0.13 | 2.73 | 1570 |
| 2024-09-20 22:21:34.194 | MS1 | 121.4656581856 | 31.1446209598 | 635 | 504990 | -85.89 | -0.41 | 72.30 | 0.13 | 1.43 | 1572 |
| 2024-09-20 22:21:35.267 | MS1 | 121.4656641033 | 31.1446234771 | 635 | 504990 | -89.69 | -1.79 | 47.42 | 0.14 | 1.18 | 1574 |
| 2024-09-20 22:21:36.531 | MS1 | 121.4656646470 | 31.1446275000 | 635 | 504990 | -94.90 | -2.89 | 68.44 | 0.08 | 1.37 | 1596 |
| 2024-09-20 22:21:37.926 | MS1 | 121.4656695802 | 31.1446347623 | 635 | 504990 | -89.09 | -2.29 | 29.92 | 0.04 | 1.32 | 1597 |
| 2024-09-20 22:21:38.495 | MS1 | 121.4656712862 | 31.1446274052 | 635 | 504990 | -82.81 | 17.77 | 394.24 | 0.14 | 1.28 | 1597 |
| 2024-09-20 22:21:39.238 | MS1 | 121.4656720878 | 31.1446240370 | 635 | 504990 | -82.21 | 15.24 | 436.50 | 0.05 | 1.25 | 1596 |
| 2024-09-20 22:21:40.215 | MS1 | 121.4656666625 | 31.1446350015 | 635 | 504990 | -82.24 | 12.83 | 497.73 | 0.13 | 2.78 | 1583 |
| 2024-09-20 22:21:41.807 | MS1 | 121.4656769502 | 31.1446217602 | 635 | 504990 | -76.78 | 13.89 | 314.83 | 0.03 | 2.28 | 1597 |
| 2024-09-20 22:21:42.129 | MS1 | 121.4656665778 | 31.1446368173 | 635 | 504990 | -79.33 | 17.70 | 557.11 | 0.08 | 2.37 | 1592 |

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
| 3226796 | 4 | 121.4715290851 | 31.1509792942 | 207 | 6 | 6 | 24.4 | TDD | 820 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3247727 | 2 | 121.4654374337 | 31.1495377858 | 219 | 1 | 11 | 17.6 | TDD | 988 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3253347 | 3 | 121.4729020164 | 31.1469726495 | 12 | 8 | 1 | 18.1 | TDD | 558 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3277908 | 1 | 121.4704208598 | 31.1494693261 | 358 | 2 | 7 | 28.4 | TDD | 635 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.925 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.947 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.085 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.085 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.736 | NREventA3 | measId:2;ServCellPCI:211;Se... |
| 2024-09-20 22:21:35.736 | NREventA3 | measId:2;ServCellPCI:211;Se... |
| 2024-09-20 22:21:36.736 | NREventA3 | measId:2;ServCellPCI:211;Se... |
| 2024-09-20 22:21:39.236 | NRRRCReestablishAttempt | PCI:211 |
| 2024-09-20 22:21:39.254 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.268 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.411 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.411 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277908 | 1 | 15.5339 | 12.9172 | -117.8251 | 14.4066 | 122.9890 | 0.0037 | 0.1432 |
| 2024_09_20 22:00 | 3247727 | 2 | 5.8179 | 17.5890 | -115.9036 | 14.1795 | 84.7870 | 0.0188 | 0.0101 |
| 2024_09_20 22:00 | 3253347 | 3 | 10.1757 | 13.2313 | -114.8828 | 6.1177 | 123.1739 | 0.0135 | 0.0124 |
| 2024_09_20 22:00 | 3226796 | 4 | 15.6926 | 18.4614 | -116.4460 | 16.9606 | 162.5988 | 0.0022 | 0.0080 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417213_A3A759E1 | 504990 | 988 | -80.9 | 504990 | 635 | -84.3 | 504990 | 558 | -84.2 | 504990 | 820 |
| MR_1774417213_232672BA | 504990 | 635 | -85.1 | 504990 | 988 | -81.8 | 504990 | 558 | -85.5 | 504990 | 820 |
| MR_1774417213_BBF2C34D | 504990 | 635 | -84.2 | 504990 | 988 | -81.1 | 504990 | 558 | -85.4 | 504990 | 820 |
| MR_1774417213_6F992891 | 504990 | 988 | -80.6 | 504990 | 635 | -85.4 | 504990 | 558 | -85.7 | 504990 | 820 |
| MR_1774417213_59FC15D3 | 504990 | 988 | -82.6 | 504990 | 635 | -86.6 | 504990 | 558 | -83.9 | 504990 | 820 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 338: `8dfb76d8-31b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8dfb76d8-31b2-4a7f-9613-b54b579a1311` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Decrease A3 Offset threshold for 3237178_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[338] topology](images/train_0338.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3270700_3
- `C2`: Decrease A3 Offset threshold for 3237178_4 **← 정답**
- `C3`: Decrease transmission power for 3237178_4
- `C4`: Add neighbor relationship between 3271549_1 and 3270700_3
- `C5`: Add neighbor relationship between 3237178_4 and 3270700_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237178_4
- `C7`: Increase A3 Offset threshold for 3237178_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270700_3
- `C9`: Increase transmission power for 3270700_3
- `C10`: Decrease transmission power for 3270700_3
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Lift the tilt angle  of 3270700_3 by 10 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270700_3
- `C14`: Adjust the azimuth of 3270700_3 by 50 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237178_4
- `C16`: Increase transmission power for 3237178_4
- `C17`: Press down the tilt angle  of 3270700_3 by 10 degrees
- `C18`: Adjust the azimuth of 3237178_4 by 50 degrees
- `C19`: Press down the tilt angle of 3237178_4 by 2 degrees
- `C20`: Lift the tilt angle of 3237178_4 by 2 degrees
- `C21`: Check test server and transmission issues
- `C22`: Increase A3 Offset threshold for 3270700_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.743 | MS1 | 121.4656654262 | 31.1446288782 | 415 | 504990 | -81.03 | 12.48 | 547.73 | 0.14 | 2.00 | 1594 |
| 2024-09-20 22:21:32.186 | MS1 | 121.4656737859 | 31.1446280160 | 415 | 504990 | -79.67 | 17.99 | 510.69 | 0.00 | 2.02 | 1593 |
| 2024-09-20 22:21:33.264 | MS1 | 121.4656691867 | 31.1446193492 | 415 | 504990 | -79.58 | 12.42 | 385.25 | 0.12 | 2.08 | 1565 |
| 2024-09-20 22:21:34.708 | MS1 | 121.4656642158 | 31.1446373551 | 415 | 504990 | -86.97 | -3.20 | 56.20 | 0.07 | 1.40 | 1572 |
| 2024-09-20 22:21:35.607 | MS1 | 121.4656666537 | 31.1446339862 | 415 | 504990 | -86.61 | -1.57 | 41.68 | 0.12 | 1.41 | 1569 |
| 2024-09-20 22:21:36.638 | MS1 | 121.4656770714 | 31.1446223290 | 415 | 504990 | -83.81 | -1.51 | 58.75 | 0.13 | 1.40 | 1575 |
| 2024-09-20 22:21:37.758 | MS1 | 121.4656698778 | 31.1446224106 | 415 | 504990 | -91.77 | -1.25 | 82.33 | 0.03 | 1.48 | 1580 |
| 2024-09-20 22:21:38.656 | MS1 | 121.4656611941 | 31.1446182159 | 415 | 504990 | -84.59 | -0.37 | 52.61 | 0.00 | 1.02 | 1579 |
| 2024-09-20 22:21:39.709 | MS1 | 121.4656630254 | 31.1446379001 | 589 | 504990 | -82.34 | 13.18 | 182.42 | 0.10 | 1.24 | 1577 |
| 2024-09-20 22:21:40.664 | MS1 | 121.4656586041 | 31.1446238461 | 589 | 504990 | -78.51 | 16.92 | 553.20 | 0.13 | 2.59 | 1590 |
| 2024-09-20 22:21:41.296 | MS1 | 121.4656586872 | 31.1446379912 | 589 | 504990 | -78.90 | 16.28 | 522.82 | 0.08 | 2.03 | 1581 |
| 2024-09-20 22:21:42.997 | MS1 | 121.4656647631 | 31.1446363563 | 589 | 504990 | -78.54 | 12.49 | 335.32 | 0.02 | 2.37 | 1569 |

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
| 3237178 | 4 | 121.4643171749 | 31.1539702576 | 101 | 0 | 1 | 39.2 | TDD | 415 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3256970 | 2 | 121.4752342805 | 31.1505366539 | 39 | 8 | 1 | 31.6 | TDD | 420 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3270700 | 3 | 121.4653046741 | 31.1488543897 | 45 | 13 | 8 | 33.2 | TDD | 589 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3271549 | 1 | 121.4712913535 | 31.1508917830 | 301 | 9 | 1 | 32.9 | TDD | 873 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.838 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.861 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.996 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.996 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.706 | NREventA3 | measId:2;ServCellPCI:586;Se... |
| 2024-09-20 22:21:37.946 | NRHandoverAttempt | SourcePCI:586;SourceNR-ARFC... |
| 2024-09-20 22:21:37.985 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.999 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.115 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.115 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271549 | 1 | 10.1740 | 13.9938 | -116.8338 | 5.5509 | 115.4955 | 0.0138 | 0.0068 |
| 2024_09_20 22:00 | 3256970 | 2 | 10.3245 | 5.6583 | -115.0654 | 15.6215 | 188.7451 | 0.0037 | 0.0108 |
| 2024_09_20 22:00 | 3270700 | 3 | 14.5696 | 5.1026 | -117.4576 | 10.9699 | 121.4075 | 0.0110 | 0.0182 |
| 2024_09_20 22:00 | 3237178 | 4 | 14.8350 | 18.5846 | -115.6291 | 16.4998 | 89.2967 | 0.0074 | 0.1010 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416519_D21436BE | 504990 | 415 | -88.6 | 504990 | 589 | -83.0 | 504990 | 873 | -85.2 | 504990 | 420 |
| MR_1774416519_FE907495 | 504990 | 589 | -82.9 | 504990 | 415 | -88.4 | 504990 | 873 | -83.0 | 504990 | 420 |
| MR_1774416519_93F51BE1 | 504990 | 589 | -82.8 | 504990 | 415 | -86.0 | 504990 | 873 | -82.0 | 504990 | 420 |
| MR_1774416519_600F301B | 504990 | 589 | -83.2 | 504990 | 415 | -87.3 | 504990 | 873 | -82.4 | 504990 | 420 |
| MR_1774416519_74F999D5 | 504990 | 415 | -85.3 | 504990 | 589 | -83.2 | 504990 | 873 | -84.7 | 504990 | 420 |
| MR_1774416519_7578D8B5 | 504990 | 415 | -86.0 | 504990 | 589 | -81.9 | 504990 | 873 | -82.6 | 504990 | 420 |
| MR_1774416519_F690436C | 504990 | 415 | -88.9 | 504990 | 589 | -81.1 | 504990 | 873 | -84.5 | 504990 | 420 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 339: `84e89524-69a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `84e89524-69a1-49dc-9184-09e75e26a5af` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[339] topology](images/train_0339.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3245800_1
- `C2`: Decrease transmission power for 3216904_4
- `C3`: Increase transmission power for 3216904_4
- `C4`: Increase transmission power for 3245800_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Adjust the azimuth of 3216904_4 by 50 degrees
- `C7`: Lift the tilt angle of 3216904_4 by 7 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216904_4
- `C9`: Decrease A3 Offset threshold for 3245800_1
- `C10`: Decrease transmission power for 3245800_1
- `C11`: Check test server and transmission issues **← 정답**
- `C12`: Decrease A3 Offset threshold for 3216904_4
- `C13`: Adjust the azimuth of 3245800_1 by 10 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245800_1
- `C15`: Lift the tilt angle  of 3245800_1 by 5 degrees
- `C16`: Increase A3 Offset threshold for 3216904_4
- `C17`: Add neighbor relationship between 3216904_4 and 3245800_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245800_1
- `C19`: Add neighbor relationship between 3248502_2 and 3245800_1
- `C20`: Press down the tilt angle of 3216904_4 by 7 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216904_4
- `C22`: Press down the tilt angle  of 3245800_1 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.996 | MS1 | 121.4656654453 | 31.1446371122 | 239 | 504990 | -85.56 | 13.64 | 395.81 | 0.07 | 2.76 | 1576 |
| 2024-09-20 22:21:32.111 | MS1 | 121.4656760852 | 31.1446316352 | 239 | 504990 | -85.66 | 15.91 | 480.60 | 0.14 | 2.96 | 1571 |
| 2024-09-20 22:21:33.775 | MS1 | 121.4656728737 | 31.1446281234 | 239 | 504990 | -86.91 | 15.53 | 346.37 | 0.03 | 2.85 | 1574 |
| 2024-09-20 22:21:34.792 | MS1 | 121.4656749011 | 31.1446253411 | 239 | 504990 | -89.40 | 14.07 | 94.70 | 0.06 | 2.07 | 326 |
| 2024-09-20 22:21:35.617 | MS1 | 121.4656719979 | 31.1446284219 | 239 | 504990 | -86.99 | 13.70 | 65.54 | 0.03 | 2.61 | 369 |
| 2024-09-20 22:21:36.524 | MS1 | 121.4656699519 | 31.1446341368 | 239 | 504990 | -86.87 | 15.59 | 84.17 | 0.12 | 2.66 | 342 |
| 2024-09-20 22:21:37.329 | MS1 | 121.4656606252 | 31.1446271659 | 239 | 504990 | -89.04 | 11.44 | 64.89 | 0.17 | 2.25 | 350 |
| 2024-09-20 22:21:38.453 | MS1 | 121.4656777886 | 31.1446296907 | 239 | 504990 | -93.41 | 9.91 | 76.39 | 0.19 | 2.91 | 421 |
| 2024-09-20 22:21:39.669 | MS1 | 121.4656746298 | 31.1446352842 | 239 | 504990 | -91.98 | 10.20 | 72.56 | 0.13 | 2.33 | 439 |
| 2024-09-20 22:21:40.908 | MS1 | 121.4656759349 | 31.1446302124 | 239 | 504990 | -90.22 | 7.45 | 542.17 | 0.10 | 2.55 | 1584 |
| 2024-09-20 22:21:41.985 | MS1 | 121.4656593725 | 31.1446318592 | 239 | 504990 | -93.57 | 12.93 | 467.79 | 0.11 | 2.87 | 1567 |
| 2024-09-20 22:21:42.387 | MS1 | 121.4656597389 | 31.1446294630 | 239 | 504990 | -93.20 | 9.33 | 316.26 | 0.02 | 2.97 | 1568 |

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
| 3216904 | 4 | 121.4673151529 | 31.1498329343 | 79 | 5 | 11 | 24.2 | TDD | 239 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3245800 | 1 | 121.4736332628 | 31.1473165281 | 258 | 4 | 4 | 20.3 | TDD | 29 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3246797 | 3 | 121.4640588236 | 31.1449217769 | 0 | 14 | 0 | 34.3 | TDD | 342 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3248502 | 2 | 121.4700856240 | 31.1483481461 | 188 | 6 | 5 | 25.1 | TDD | 421 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.119 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.142 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.286 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.286 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.981 | NREventA3 | measId:2;ServCellPCI:993;Se... |
| 2024-09-20 22:21:38.221 | NRHandoverAttempt | SourcePCI:993;SourceNR-ARFC... |
| 2024-09-20 22:21:38.252 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.262 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.410 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.410 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245800 | 1 | 15.3294 | 7.8851 | -116.1957 | 5.7984 | 128.3902 | 0.0138 | 0.0180 |
| 2024_09_20 22:00 | 3248502 | 2 | 19.5716 | 17.7052 | -116.5391 | 14.9930 | 158.6198 | 0.0125 | 0.0043 |
| 2024_09_20 22:00 | 3246797 | 3 | 5.9190 | 8.6715 | -116.3137 | 16.6417 | 105.3251 | 0.0067 | 0.0056 |
| 2024_09_20 22:00 | 3216904 | 4 | 6.6210 | 18.3257 | -116.7624 | 10.2445 | 109.0005 | 0.0022 | 0.0102 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414810_267045B5 | 504990 | 239 | -90.1 | 504990 | 29 | -90.0 | 504990 | 421 | -97.6 | 504990 | 342 |
| MR_1774414810_D92DA26D | 504990 | 239 | -87.8 | 504990 | 29 | -90.5 | 504990 | 421 | -97.8 | 504990 | 342 |
| MR_1774414810_4E696A57 | 504990 | 239 | -90.1 | 504990 | 29 | -92.3 | 504990 | 421 | -98.9 | 504990 | 342 |
| MR_1774414810_69B1E8FD | 504990 | 239 | -89.3 | 504990 | 29 | -91.6 | 504990 | 421 | -97.6 | 504990 | 342 |
| MR_1774414810_881B4FA3 | 504990 | 239 | -89.5 | 504990 | 29 | -92.1 | 504990 | 421 | -100.8 | 504990 | 342 |
| MR_1774414810_26071BBC | 504990 | 239 | -89.5 | 504990 | 29 | -90.5 | 504990 | 421 | -99.4 | 504990 | 342 |
| MR_1774414810_104B7281 | 504990 | 239 | -89.6 | 504990 | 29 | -90.3 | 504990 | 421 | -98.2 | 504990 | 342 |

> *... 2개 열 생략 (전체 14열)*

---
