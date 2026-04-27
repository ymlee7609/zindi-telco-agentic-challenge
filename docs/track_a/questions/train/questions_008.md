# Track A 문제 분석 — train[70]~train[79]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[70] ~ train[79] (10개)

## 목차

1. [문제 70: `728faaa3-550...`](#70) — single-answer, 정답: C4
2. [문제 71: `76417976-cb0...`](#71) — single-answer, 정답: C20
3. [문제 72: `fa23ce05-0f5...`](#72) — single-answer, 정답: C15
4. [문제 73: `06b994e5-505...`](#73) — single-answer, 정답: C11
5. [문제 74: `8c362eb1-6ae...`](#74) — single-answer, 정답: C9
6. [문제 75: `da7d2a6a-a3e...`](#75) — single-answer, 정답: C20
7. [문제 76: `0b8db212-993...`](#76) — single-answer, 정답: C13
8. [문제 77: `4f3e39bd-e73...`](#77) — single-answer, 정답: C1
9. [문제 78: `79964092-9cd...`](#78) — single-answer, 정답: C10
10. [문제 79: `65e93bbb-664...`](#79) — multiple-answer, 정답: C10|C13|C15|C21

---

### 문제 70: `728faaa3-550...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `728faaa3-5509-4f8c-a7eb-dddeed381604` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[70] topology](images/train_0070.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3262975_3
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease A3 Offset threshold for 3251604_4
- `C4`: Check test server and transmission issues **← 정답**
- `C5`: Press down the tilt angle  of 3251604_4 by 10 degrees
- `C6`: Increase transmission power for 3262975_3
- `C7`: Increase A3 Offset threshold for 3251604_4
- `C8`: Decrease transmission power for 3251604_4
- `C9`: Decrease transmission power for 3262975_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262975_3
- `C11`: Lift the tilt angle  of 3251604_4 by 10 degrees
- `C12`: Add neighbor relationship between 3262975_3 and 3251604_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251604_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251604_4
- `C15`: Add neighbor relationship between 3248394_2 and 3251604_4
- `C16`: Press down the tilt angle of 3262975_3 by 5 degrees
- `C17`: Adjust the azimuth of 3251604_4 by 50 degrees
- `C18`: Decrease A3 Offset threshold for 3262975_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262975_3
- `C20`: Adjust the azimuth of 3262975_3 by 50 degrees
- `C21`: Lift the tilt angle of 3262975_3 by 5 degrees
- `C22`: Increase transmission power for 3251604_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.158 | MS1 | 121.4656758440 | 31.1446335030 | 579 | 504990 | -86.64 | 13.38 | 527.92 | 0.05 | 2.33 | 1580 |
| 2024-09-20 22:21:32.243 | MS1 | 121.4656773291 | 31.1446292784 | 579 | 504990 | -86.03 | 13.82 | 316.15 | 0.07 | 2.90 | 1585 |
| 2024-09-20 22:21:33.161 | MS1 | 121.4656667003 | 31.1446339945 | 579 | 504990 | -89.20 | 15.05 | 377.89 | 0.08 | 2.05 | 1564 |
| 2024-09-20 22:21:34.895 | MS1 | 121.4656741031 | 31.1446266291 | 579 | 504990 | -88.80 | 12.81 | 72.57 | 0.11 | 2.36 | 433 |
| 2024-09-20 22:21:35.993 | MS1 | 121.4656589320 | 31.1446251391 | 579 | 504990 | -91.51 | 17.36 | 78.93 | 0.20 | 2.13 | 341 |
| 2024-09-20 22:21:36.665 | MS1 | 121.4656691781 | 31.1446253066 | 579 | 504990 | -89.12 | 17.11 | 83.92 | 0.10 | 2.87 | 305 |
| 2024-09-20 22:21:37.324 | MS1 | 121.4656768214 | 31.1446300656 | 579 | 504990 | -89.93 | 9.13 | 46.21 | 0.14 | 2.86 | 444 |
| 2024-09-20 22:21:38.984 | MS1 | 121.4656733021 | 31.1446186093 | 579 | 504990 | -89.27 | 12.17 | 47.16 | 0.11 | 2.15 | 395 |
| 2024-09-20 22:21:39.852 | MS1 | 121.4656650277 | 31.1446323034 | 579 | 504990 | -92.70 | 11.28 | 82.31 | 0.06 | 2.99 | 447 |
| 2024-09-20 22:21:40.277 | MS1 | 121.4656658592 | 31.1446267307 | 579 | 504990 | -91.88 | 11.49 | 575.66 | 0.07 | 2.90 | 1586 |
| 2024-09-20 22:21:41.777 | MS1 | 121.4656609329 | 31.1446197547 | 579 | 504990 | -91.09 | 12.21 | 453.22 | 0.13 | 2.98 | 1563 |
| 2024-09-20 22:21:42.538 | MS1 | 121.4656613042 | 31.1446198510 | 579 | 504990 | -90.04 | 8.02 | 371.72 | 0.01 | 2.11 | 1580 |

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
| 3248394 | 2 | 121.4723956824 | 31.1459257280 | 72 | 15 | 1 | 38.5 | TDD | 705 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3251604 | 4 | 121.4706134830 | 31.1480072744 | 100 | 15 | 4 | 48.3 | TDD | 126 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3262975 | 3 | 121.4700036076 | 31.1449250647 | 136 | 2 | 5 | 23.3 | TDD | 579 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3272237 | 1 | 121.4699422172 | 31.1521471023 | 48 | 4 | 5 | 23.9 | TDD | 904 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.071 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.091 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.223 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.223 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.943 | NREventA3 | measId:2;ServCellPCI:236;Se... |
| 2024-09-20 22:21:38.183 | NRHandoverAttempt | SourcePCI:236;SourceNR-ARFC... |
| 2024-09-20 22:21:38.218 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.229 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.373 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.373 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272237 | 1 | 6.0187 | 5.1352 | -115.3295 | 8.1687 | 185.1656 | 0.0054 | 0.0034 |
| 2024_09_20 22:00 | 3248394 | 2 | 10.5988 | 6.5339 | -114.8028 | 13.9831 | 140.5444 | 0.0028 | 0.0165 |
| 2024_09_20 22:00 | 3262975 | 3 | 14.9460 | 8.0818 | -117.9966 | 17.3518 | 194.2329 | 0.0055 | 0.0077 |
| 2024_09_20 22:00 | 3251604 | 4 | 15.1404 | 7.9552 | -115.8213 | 14.1381 | 118.0233 | 0.0170 | 0.0184 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413702_2E867AE1 | 504990 | 579 | -90.2 | 504990 | 126 | -94.7 | 504990 | 705 | -95.3 | 504990 | 904 |
| MR_1774413702_64704B25 | 504990 | 579 | -88.1 | 504990 | 126 | -95.6 | 504990 | 705 | -94.1 | 504990 | 904 |
| MR_1774413702_42A21FCB | 504990 | 579 | -88.6 | 504990 | 126 | -93.7 | 504990 | 705 | -94.7 | 504990 | 904 |
| MR_1774413702_739716A4 | 504990 | 579 | -87.9 | 504990 | 126 | -92.5 | 504990 | 705 | -97.6 | 504990 | 904 |
| MR_1774413702_8291A47F | 504990 | 579 | -86.9 | 504990 | 126 | -96.1 | 504990 | 705 | -96.8 | 504990 | 904 |
| MR_1774413702_4ED34C6B | 504990 | 579 | -88.7 | 504990 | 126 | -94.9 | 504990 | 705 | -94.7 | 504990 | 904 |
| MR_1774413702_76A41AAC | 504990 | 579 | -89.4 | 504990 | 126 | -95.6 | 504990 | 705 | -97.3 | 504990 | 904 |
| MR_1774413702_790B5B07 | 504990 | 579 | -88.6 | 504990 | 126 | -96.0 | 504990 | 705 | -97.1 | 504990 | 904 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 71: `76417976-cb0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `76417976-cb00-47f7-8604-180ca3d4f886` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3214472_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[71] topology](images/train_0071.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3214472_4
- `C2`: Decrease A3 Offset threshold for 3222907_1
- `C3`: Decrease A3 Offset threshold for 3214472_4
- `C4`: Increase transmission power for 3222907_1
- `C5`: Add neighbor relationship between 3246328_2 and 3222907_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214472_4
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Press down the tilt angle of 3214472_4 by 6 degrees
- `C9`: Increase A3 Offset threshold for 3222907_1
- `C10`: Decrease transmission power for 3214472_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222907_1
- `C12`: Lift the tilt angle of 3214472_4 by 6 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222907_1
- `C14`: Adjust the azimuth of 3214472_4 by 27 degrees
- `C15`: Increase A3 Offset threshold for 3214472_4
- `C16`: Check test server and transmission issues
- `C17`: Decrease transmission power for 3222907_1
- `C18`: Press down the tilt angle  of 3222907_1 by 10 degrees
- `C19`: Add neighbor relationship between 3214472_4 and 3222907_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214472_4 **← 정답**
- `C21`: Lift the tilt angle  of 3222907_1 by 10 degrees
- `C22`: Adjust the azimuth of 3222907_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.934 | MS1 | 121.4656757171 | 31.1446257700 | 463 | 504990 | -86.15 | 12.44 | 316.86 | 0.20 | 2.58 | 1562 |
| 2024-09-20 22:21:32.325 | MS1 | 121.4656711857 | 31.1446375582 | 463 | 504990 | -85.13 | 14.06 | 334.14 | 0.10 | 2.77 | 1580 |
| 2024-09-20 22:21:33.822 | MS1 | 121.4656673932 | 31.1446299273 | 463 | 504990 | -91.53 | 17.81 | 603.13 | 0.12 | 2.84 | 1589 |
| 2024-09-20 22:21:34.874 | MS1 | 121.4656625647 | 31.1446369164 | 463 | 504990 | -86.49 | 17.58 | 79.17 | 0.61 | 2.02 | 517 |
| 2024-09-20 22:21:35.349 | MS1 | 121.4656716550 | 31.1446225437 | 463 | 504990 | -90.34 | 17.44 | 104.74 | 0.56 | 2.26 | 698 |
| 2024-09-20 22:21:36.509 | MS1 | 121.4656610810 | 31.1446208442 | 463 | 504990 | -89.03 | 15.33 | 47.85 | 0.51 | 2.90 | 553 |
| 2024-09-20 22:21:37.562 | MS1 | 121.4656631465 | 31.1446347829 | 463 | 504990 | -92.53 | 11.70 | 66.44 | 0.65 | 2.39 | 578 |
| 2024-09-20 22:21:38.472 | MS1 | 121.4656656764 | 31.1446304095 | 463 | 504990 | -89.78 | 12.36 | 88.26 | 0.61 | 2.36 | 583 |
| 2024-09-20 22:21:39.778 | MS1 | 121.4656660304 | 31.1446189205 | 463 | 504990 | -91.92 | 11.54 | 51.61 | 0.67 | 2.41 | 636 |
| 2024-09-20 22:21:40.551 | MS1 | 121.4656666322 | 31.1446214109 | 463 | 504990 | -93.31 | 8.37 | 444.34 | 0.13 | 2.11 | 1564 |
| 2024-09-20 22:21:41.378 | MS1 | 121.4656628378 | 31.1446189870 | 463 | 504990 | -92.20 | 7.34 | 544.14 | 0.19 | 2.85 | 1600 |
| 2024-09-20 22:21:42.455 | MS1 | 121.4656678741 | 31.1446224800 | 463 | 504990 | -90.09 | 12.92 | 416.31 | 0.13 | 2.38 | 1596 |

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
| 3214472 | 4 | 121.4742213430 | 31.1546292620 | 189 | 4 | 5 | 47.9 | TDD | 463 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3222907 | 1 | 121.4733559763 | 31.1509042622 | 59 | 15 | 8 | 32.5 | TDD | 1 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3246328 | 2 | 121.4706228783 | 31.1440554659 | 216 | 0 | 7 | 27.0 | TDD | 860 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3263487 | 3 | 121.4667086067 | 31.1542847125 | 81 | 7 | 5 | 46.8 | TDD | 254 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.858 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.876 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.990 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.990 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.662 | NREventA3 | measId:2;ServCellPCI:278;Se... |
| 2024-09-20 22:21:37.902 | NRHandoverAttempt | SourcePCI:278;SourceNR-ARFC... |
| 2024-09-20 22:21:37.935 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.946 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.076 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.076 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222907 | 1 | 15.1223 | 11.9115 | -115.3269 | 12.9406 | 143.2070 | 0.0153 | 0.0053 |
| 2024_09_20 22:00 | 3246328 | 2 | 6.8463 | 8.9395 | -117.0612 | 16.0406 | 122.2972 | 0.0188 | 0.0084 |
| 2024_09_20 22:00 | 3263487 | 3 | 12.0086 | 18.5556 | -115.8740 | 18.6618 | 136.7271 | 0.0091 | 0.0040 |
| 2024_09_20 22:00 | 3214472 | 4 | 16.8267 | 13.0569 | -114.7316 | 5.8581 | 195.8813 | 0.0047 | 0.0112 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414687_4E67C1E2 | 504990 | 463 | -86.6 | 504990 | 1 | -94.3 | 504990 | 860 | -94.5 | 504990 | 254 |
| MR_1774414687_12C155EB | 504990 | 463 | -87.9 | 504990 | 1 | -95.8 | 504990 | 860 | -95.4 | 504990 | 254 |
| MR_1774414687_9FE8D245 | 504990 | 463 | -86.6 | 504990 | 1 | -96.9 | 504990 | 860 | -95.7 | 504990 | 254 |
| MR_1774414687_5931B0AB | 504990 | 463 | -87.1 | 504990 | 1 | -95.0 | 504990 | 860 | -95.0 | 504990 | 254 |
| MR_1774414687_60F1B2BC | 504990 | 463 | -86.8 | 504990 | 1 | -95.0 | 504990 | 860 | -96.2 | 504990 | 254 |
| MR_1774414687_4BA6F439 | 504990 | 463 | -87.2 | 504990 | 1 | -94.1 | 504990 | 860 | -97.5 | 504990 | 254 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 72: `fa23ce05-0f5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fa23ce05-0f52-4e50-ab14-e96da45ed675` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3270365_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[72] topology](images/train_0072.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3270365_1 and 3247409_3
- `C2`: Decrease A3 Offset threshold for 3247409_3
- `C3`: Adjust the azimuth of 3247409_3 by 50 degrees
- `C4`: Add neighbor relationship between 3245267_2 and 3247409_3
- `C5`: Decrease A3 Offset threshold for 3270365_1
- `C6`: Lift the tilt angle  of 3247409_3 by 10 degrees
- `C7`: Increase transmission power for 3270365_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270365_1
- `C9`: Increase A3 Offset threshold for 3270365_1
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease transmission power for 3247409_3
- `C12`: Press down the tilt angle  of 3247409_3 by 10 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247409_3
- `C14`: Adjust the azimuth of 3270365_1 by 36 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270365_1 **← 정답**
- `C16`: Decrease transmission power for 3270365_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247409_3
- `C18`: Increase A3 Offset threshold for 3247409_3
- `C19`: Increase transmission power for 3247409_3
- `C20`: Lift the tilt angle of 3270365_1 by 6 degrees
- `C21`: Check test server and transmission issues
- `C22`: Press down the tilt angle of 3270365_1 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.514 | MS1 | 121.4656747891 | 31.1446297108 | 784 | 504990 | -91.02 | 14.31 | 445.79 | 0.06 | 2.41 | 1569 |
| 2024-09-20 22:21:32.522 | MS1 | 121.4656607765 | 31.1446367535 | 784 | 504990 | -87.23 | 17.64 | 500.99 | 0.02 | 2.11 | 1590 |
| 2024-09-20 22:21:33.713 | MS1 | 121.4656768454 | 31.1446222258 | 784 | 504990 | -86.28 | 18.00 | 599.12 | 0.09 | 2.58 | 1584 |
| 2024-09-20 22:21:34.338 | MS1 | 121.4656584159 | 31.1446359420 | 784 | 504990 | -85.35 | 15.07 | 52.68 | 0.60 | 2.05 | 571 |
| 2024-09-20 22:21:35.624 | MS1 | 121.4656751207 | 31.1446346698 | 784 | 504990 | -89.20 | 16.71 | 93.73 | 0.59 | 2.35 | 523 |
| 2024-09-20 22:21:36.123 | MS1 | 121.4656771864 | 31.1446365404 | 784 | 504990 | -86.58 | 12.91 | 104.15 | 0.67 | 2.43 | 672 |
| 2024-09-20 22:21:37.330 | MS1 | 121.4656652753 | 31.1446297239 | 784 | 504990 | -91.15 | 12.71 | 62.13 | 0.57 | 2.03 | 568 |
| 2024-09-20 22:21:38.577 | MS1 | 121.4656777061 | 31.1446212704 | 784 | 504990 | -90.39 | 12.41 | 91.38 | 0.53 | 2.00 | 578 |
| 2024-09-20 22:21:39.565 | MS1 | 121.4656767351 | 31.1446229784 | 784 | 504990 | -90.28 | 11.18 | 95.78 | 0.53 | 2.71 | 536 |
| 2024-09-20 22:21:40.113 | MS1 | 121.4656657847 | 31.1446185504 | 784 | 504990 | -89.79 | 9.11 | 546.84 | 0.11 | 2.30 | 1573 |
| 2024-09-20 22:21:41.312 | MS1 | 121.4656614495 | 31.1446298945 | 784 | 504990 | -92.00 | 7.62 | 471.12 | 0.14 | 2.78 | 1587 |
| 2024-09-20 22:21:42.914 | MS1 | 121.4656602019 | 31.1446243418 | 784 | 504990 | -93.35 | 9.57 | 421.54 | 0.19 | 2.37 | 1587 |

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
| 3245267 | 2 | 121.4702043310 | 31.1467340713 | 179 | 1 | 3 | 16.3 | TDD | 272 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3247409 | 3 | 121.4740242146 | 31.1473912775 | 65 | 10 | 11 | 25.6 | TDD | 730 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3270358 | 4 | 121.4723248449 | 31.1445958783 | 312 | 7 | 7 | 42.7 | TDD | 521 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3270365 | 1 | 121.4642985722 | 31.1476971985 | 195 | 1 | 8 | 31.5 | TDD | 784 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.619 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.638 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.788 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.788 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.479 | NREventA3 | measId:2;ServCellPCI:635;Se... |
| 2024-09-20 22:21:38.719 | NRHandoverAttempt | SourcePCI:635;SourceNR-ARFC... |
| 2024-09-20 22:21:38.766 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.781 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.889 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.889 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270365 | 1 | 19.3677 | 9.8830 | -116.5094 | 7.0494 | 127.6146 | 0.0125 | 0.0068 |
| 2024_09_20 22:00 | 3245267 | 2 | 17.9777 | 9.2576 | -114.2309 | 9.9148 | 146.7740 | 0.0040 | 0.0189 |
| 2024_09_20 22:00 | 3247409 | 3 | 7.4574 | 14.9293 | -116.7633 | 19.5603 | 185.5588 | 0.0159 | 0.0081 |
| 2024_09_20 22:00 | 3270358 | 4 | 9.3731 | 9.9464 | -117.9711 | 17.8701 | 192.3675 | 0.0037 | 0.0192 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417137_857D5E00 | 504990 | 784 | -85.5 | 504990 | 730 | -89.7 | 504990 | 272 | -96.7 | 504990 | 521 |
| MR_1774417137_E4E82A19 | 504990 | 784 | -84.3 | 504990 | 730 | -92.9 | 504990 | 272 | -96.8 | 504990 | 521 |
| MR_1774417137_9594EC24 | 504990 | 784 | -83.9 | 504990 | 730 | -90.9 | 504990 | 272 | -99.1 | 504990 | 521 |
| MR_1774417137_C5BAE194 | 504990 | 784 | -86.9 | 504990 | 730 | -89.2 | 504990 | 272 | -97.4 | 504990 | 521 |
| MR_1774417137_922FFDE2 | 504990 | 784 | -87.3 | 504990 | 730 | -91.5 | 504990 | 272 | -98.2 | 504990 | 521 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 73: `06b994e5-505...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `06b994e5-505c-43a6-84cb-8f430297be7e` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Lift the tilt angle  of 3215319_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[73] topology](images/train_0073.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268515_4
- `C2`: Adjust the azimuth of 3215319_3 by 10 degrees
- `C3`: Increase A3 Offset threshold for 3268515_4
- `C4`: Press down the tilt angle  of 3215319_3 by 10 degrees
- `C5`: Adjust the azimuth of 3268515_4 by 10 degrees
- `C6`: Add neighbor relationship between 3215319_3 and 3224937_2
- `C7`: Decrease transmission power for 3268515_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268515_4
- `C9`: Decrease A3 Offset threshold for 3268515_4
- `C10`: Increase transmission power for 3224937_2
- `C11`: Lift the tilt angle  of 3215319_3 by 10 degrees **← 정답**
- `C12`: Decrease A3 Offset threshold for 3224937_2
- `C13`: Add neighbor relationship between 3268515_4 and 3224937_2
- `C14`: Lift the tilt angle of 3268515_4 by 5 degrees
- `C15`: Increase A3 Offset threshold for 3224937_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase transmission power for 3268515_4
- `C18`: Check test server and transmission issues
- `C19`: Decrease transmission power for 3224937_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224937_2
- `C21`: Press down the tilt angle of 3268515_4 by 5 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224937_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.196 | MS1 | 121.4656696440 | 31.1446264575 | 95 | 504990 | -85.28 | 16.00 | 466.00 | 0.10 | 2.14 | 1582 |
| 2024-09-20 22:21:32.605 | MS1 | 121.4656646307 | 31.1446189252 | 95 | 504990 | -90.57 | 15.86 | 453.85 | 0.05 | 2.68 | 1564 |
| 2024-09-20 22:21:33.308 | MS1 | 121.4656734589 | 31.1446312248 | 95 | 504990 | -85.23 | 16.03 | 373.95 | 0.05 | 2.05 | 1595 |
| 2024-09-20 22:21:34.775 | MS1 | 121.4656666676 | 31.1446306188 | 95 | 504990 | -88.84 | 12.70 | 56.45 | 0.11 | 2.94 | 1592 |
| 2024-09-20 22:21:35.786 | MS1 | 121.4656644972 | 31.1446330232 | 95 | 504990 | -88.13 | 14.24 | 70.31 | 0.07 | 2.66 | 1584 |
| 2024-09-20 22:21:36.729 | MS1 | 121.4656671254 | 31.1446226137 | 95 | 504990 | -85.59 | 12.48 | 61.22 | 0.14 | 2.20 | 1586 |
| 2024-09-20 22:21:37.441 | MS1 | 121.4656666085 | 31.1446204764 | 95 | 504990 | -93.80 | 9.34 | 79.80 | 0.06 | 2.63 | 1594 |
| 2024-09-20 22:21:38.809 | MS1 | 121.4656677868 | 31.1446295846 | 95 | 504990 | -91.61 | 9.65 | 59.80 | 0.08 | 2.57 | 1567 |
| 2024-09-20 22:21:39.204 | MS1 | 121.4656662374 | 31.1446233160 | 95 | 504990 | -89.64 | 8.52 | 67.25 | 0.18 | 2.64 | 1591 |
| 2024-09-20 22:21:40.343 | MS1 | 121.4656763580 | 31.1446319633 | 95 | 504990 | -91.62 | 7.64 | 299.49 | 0.08 | 2.16 | 1596 |
| 2024-09-20 22:21:41.798 | MS1 | 121.4656626166 | 31.1446363873 | 95 | 504990 | -93.63 | 7.37 | 385.64 | 0.19 | 2.47 | 1586 |
| 2024-09-20 22:21:42.264 | MS1 | 121.4656660674 | 31.1446305523 | 95 | 504990 | -91.01 | 12.43 | 332.81 | 0.19 | 2.78 | 1588 |

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
| 3215319 | 3 | 121.4715083701 | 31.1549725506 | 312 | 6 | 11 | 41.1 | TDD | 899 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3224937 | 2 | 121.4641643393 | 31.1536514757 | 182 | 8 | 11 | 27.8 | TDD | 683 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3256152 | 1 | 121.4693859682 | 31.1452622404 | 126 | 4 | 8 | 41.9 | TDD | 400 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3268515 | 4 | 121.4702206761 | 31.1452410332 | 251 | 0 | 12 | 37.9 | TDD | 95 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.535 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.551 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.701 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.701 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.422 | NREventA3 | measId:2;ServCellPCI:83;Ser... |
| 2024-09-20 22:21:38.662 | NRHandoverAttempt | SourcePCI:83;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.712 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.727 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.832 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.832 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256152 | 1 | 5.0502 | 13.2109 | -116.9012 | 8.9486 | 155.4960 | 0.0085 | 0.0140 |
| 2024_09_20 22:00 | 3224937 | 2 | 9.1769 | 17.1515 | -114.6968 | 15.0734 | 138.9410 | 0.0176 | 0.0016 |
| 2024_09_20 22:00 | 3215319 | 3 | 7.7054 | 18.1477 | -114.4184 | 11.6618 | 179.9947 | 0.0130 | 0.0000 |
| 2024_09_20 22:00 | 3268515 | 4 | 78.7041 | 87.4263 | -114.5331 | 7.4787 | 190.1100 | 0.0002 | 0.0178 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416899_6393543C | 504990 | 95 | -89.7 | 504990 | 683 | -96.0 | 504990 | 899 | -103.1 | 504990 | 400 |
| MR_1774416899_B89F4698 | 504990 | 95 | -90.0 | 504990 | 683 | -94.6 | 504990 | 899 | -99.4 | 504990 | 400 |
| MR_1774416899_C972130A | 504990 | 95 | -90.8 | 504990 | 683 | -94.7 | 504990 | 899 | -100.0 | 504990 | 400 |
| MR_1774416899_56168B43 | 504990 | 95 | -88.4 | 504990 | 683 | -94.5 | 504990 | 899 | -99.6 | 504990 | 400 |
| MR_1774416899_D19D9124 | 504990 | 95 | -87.0 | 504990 | 683 | -94.4 | 504990 | 899 | -102.6 | 504990 | 400 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 74: `8c362eb1-6ae...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8c362eb1-6ae9-43aa-bd9d-7b2173bae2d7` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Add neighbor relationship between 3234858_1 and 3245572_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[74] topology](images/train_0074.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease transmission power for 3245572_3
- `C3`: Add neighbor relationship between 3229430_2 and 3245572_3
- `C4`: Lift the tilt angle of 3234858_1 by 10 degrees
- `C5`: Press down the tilt angle  of 3245572_3 by 2 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234858_1
- `C7`: Decrease A3 Offset threshold for 3234858_1
- `C8`: Increase A3 Offset threshold for 3234858_1
- `C9`: Add neighbor relationship between 3234858_1 and 3245572_3 **← 정답**
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234858_1
- `C11`: Increase A3 Offset threshold for 3245572_3
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Press down the tilt angle of 3234858_1 by 10 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245572_3
- `C15`: Adjust the azimuth of 3245572_3 by 31 degrees
- `C16`: Adjust the azimuth of 3234858_1 by 50 degrees
- `C17`: Decrease A3 Offset threshold for 3245572_3
- `C18`: Lift the tilt angle  of 3245572_3 by 2 degrees
- `C19`: Increase transmission power for 3245572_3
- `C20`: Increase transmission power for 3234858_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245572_3
- `C22`: Decrease transmission power for 3234858_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.770 | MS1 | 121.4656628833 | 31.1446211254 | 194 | 504990 | -84.48 | 14.39 | 328.74 | 0.13 | 2.84 | 1574 |
| 2024-09-20 22:21:32.845 | MS1 | 121.4656616738 | 31.1446249322 | 194 | 504990 | -83.59 | 15.96 | 511.52 | 0.15 | 2.29 | 1594 |
| 2024-09-20 22:21:33.386 | MS1 | 121.4656668759 | 31.1446308285 | 194 | 504990 | -76.55 | 14.45 | 513.17 | 0.00 | 2.27 | 1594 |
| 2024-09-20 22:21:34.101 | MS1 | 121.4656736270 | 31.1446344210 | 194 | 504990 | -93.14 | -3.02 | 32.22 | 0.10 | 1.16 | 1571 |
| 2024-09-20 22:21:35.402 | MS1 | 121.4656726592 | 31.1446215196 | 194 | 504990 | -89.78 | -2.09 | 45.90 | 0.09 | 1.21 | 1561 |
| 2024-09-20 22:21:36.388 | MS1 | 121.4656663250 | 31.1446322174 | 194 | 504990 | -89.63 | -2.78 | 34.61 | 0.04 | 1.07 | 1587 |
| 2024-09-20 22:21:37.260 | MS1 | 121.4656689786 | 31.1446189331 | 194 | 504990 | -86.62 | -1.53 | 54.80 | 0.02 | 1.20 | 1575 |
| 2024-09-20 22:21:38.182 | MS1 | 121.4656728833 | 31.1446193442 | 194 | 504990 | -76.41 | 14.23 | 425.57 | 0.10 | 1.39 | 1563 |
| 2024-09-20 22:21:39.423 | MS1 | 121.4656681388 | 31.1446214907 | 194 | 504990 | -77.48 | 15.13 | 347.49 | 0.03 | 1.46 | 1576 |
| 2024-09-20 22:21:40.896 | MS1 | 121.4656723047 | 31.1446317131 | 194 | 504990 | -79.35 | 16.29 | 567.42 | 0.18 | 2.78 | 1596 |
| 2024-09-20 22:21:41.879 | MS1 | 121.4656612939 | 31.1446379822 | 194 | 504990 | -77.51 | 13.62 | 470.66 | 0.16 | 2.62 | 1586 |
| 2024-09-20 22:21:42.253 | MS1 | 121.4656616983 | 31.1446240832 | 194 | 504990 | -78.15 | 17.34 | 398.95 | 0.14 | 2.59 | 1592 |

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
| 3211026 | 4 | 121.4689353599 | 31.1543736117 | 86 | 3 | 7 | 28.1 | TDD | 330 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3229430 | 2 | 121.4722107250 | 31.1462897335 | 237 | 2 | 6 | 42.2 | TDD | 635 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3234858 | 1 | 121.4751113980 | 31.1447521891 | 217 | 8 | 6 | 34.0 | TDD | 194 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3245572 | 3 | 121.4718058155 | 31.1524917474 | 183 | 1 | 4 | 24.0 | TDD | 4 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.713 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.730 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.842 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.842 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.611 | NREventA3 | measId:2;ServCellPCI:30;Ser... |
| 2024-09-20 22:21:35.611 | NREventA3 | measId:2;ServCellPCI:30;Ser... |
| 2024-09-20 22:21:36.611 | NREventA3 | measId:2;ServCellPCI:30;Ser... |
| 2024-09-20 22:21:39.111 | NRRRCReestablishAttempt | PCI:30 |
| 2024-09-20 22:21:39.129 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.144 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.282 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.282 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234858 | 1 | 6.7155 | 12.6475 | -117.7144 | 17.6448 | 87.0533 | 0.0017 | 0.1574 |
| 2024_09_20 22:00 | 3229430 | 2 | 11.0019 | 16.4865 | -114.5977 | 17.8755 | 158.8751 | 0.0021 | 0.0117 |
| 2024_09_20 22:00 | 3245572 | 3 | 5.9675 | 5.0719 | -117.9086 | 15.0869 | 87.7389 | 0.0054 | 0.0062 |
| 2024_09_20 22:00 | 3211026 | 4 | 13.7117 | 16.0119 | -114.5549 | 7.5708 | 124.3778 | 0.0066 | 0.0076 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414262_5DDE1CEC | 504990 | 4 | -88.5 | 504990 | 194 | -93.6 | 504990 | 635 | -96.3 | 504990 | 330 |
| MR_1774414262_48D20DEF | 504990 | 194 | -93.9 | 504990 | 4 | -89.1 | 504990 | 635 | -97.6 | 504990 | 330 |
| MR_1774414262_2D2F11E9 | 504990 | 194 | -92.6 | 504990 | 4 | -87.5 | 504990 | 635 | -99.0 | 504990 | 330 |
| MR_1774414262_FBFF97E5 | 504990 | 4 | -88.9 | 504990 | 194 | -94.4 | 504990 | 635 | -95.5 | 504990 | 330 |
| MR_1774414262_0909ECE6 | 504990 | 4 | -88.5 | 504990 | 194 | -92.0 | 504990 | 635 | -97.8 | 504990 | 330 |
| MR_1774414262_060587E5 | 504990 | 4 | -86.5 | 504990 | 194 | -95.0 | 504990 | 635 | -97.0 | 504990 | 330 |
| MR_1774414262_97E19272 | 504990 | 4 | -86.6 | 504990 | 194 | -94.2 | 504990 | 635 | -97.5 | 504990 | 330 |
| MR_1774414262_AEEDE184 | 504990 | 194 | -92.9 | 504990 | 4 | -87.2 | 504990 | 635 | -99.2 | 504990 | 330 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 75: `da7d2a6a-a3e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `da7d2a6a-a3ec-43a5-adc9-885ee6844f56` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Lift the tilt angle  of 3271497_4 by 6 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[75] topology](images/train_0075.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3265550_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226541_1
- `C3`: Lift the tilt angle of 3226541_1 by 4 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265550_2
- `C5`: Press down the tilt angle  of 3271497_4 by 6 degrees
- `C6`: Press down the tilt angle of 3226541_1 by 4 degrees
- `C7`: Increase transmission power for 3226541_1
- `C8`: Increase transmission power for 3265550_2
- `C9`: Add neighbor relationship between 3226541_1 and 3265550_2
- `C10`: Check test server and transmission issues
- `C11`: Adjust the azimuth of 3271497_4 by 50 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265550_2
- `C13`: Increase A3 Offset threshold for 3226541_1
- `C14`: Decrease transmission power for 3226541_1
- `C15`: Adjust the azimuth of 3226541_1 by 8 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226541_1
- `C17`: Increase A3 Offset threshold for 3265550_2
- `C18`: Decrease A3 Offset threshold for 3226541_1
- `C19`: Add neighbor relationship between 3271497_4 and 3265550_2
- `C20`: Lift the tilt angle  of 3271497_4 by 6 degrees **← 정답**
- `C21`: Decrease A3 Offset threshold for 3265550_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.647 | MS1 | 121.4656704794 | 31.1446184616 | 499 | 504990 | -89.70 | 15.19 | 436.78 | 0.16 | 2.95 | 1587 |
| 2024-09-20 22:21:32.119 | MS1 | 121.4656674608 | 31.1446300285 | 499 | 504990 | -89.03 | 17.86 | 569.35 | 0.10 | 2.87 | 1593 |
| 2024-09-20 22:21:33.562 | MS1 | 121.4656660002 | 31.1446303944 | 499 | 504990 | -90.95 | 12.24 | 427.26 | 0.13 | 2.37 | 1586 |
| 2024-09-20 22:21:34.299 | MS1 | 121.4656707231 | 31.1446354175 | 499 | 504990 | -87.62 | 12.00 | 65.88 | 0.08 | 2.28 | 1590 |
| 2024-09-20 22:21:35.968 | MS1 | 121.4656770061 | 31.1446219498 | 499 | 504990 | -87.02 | 15.45 | 78.83 | 0.16 | 2.48 | 1576 |
| 2024-09-20 22:21:36.382 | MS1 | 121.4656683142 | 31.1446297316 | 499 | 504990 | -88.35 | 14.10 | 56.60 | 0.07 | 2.55 | 1597 |
| 2024-09-20 22:21:37.415 | MS1 | 121.4656743763 | 31.1446332006 | 499 | 504990 | -92.52 | 9.98 | 72.70 | 0.14 | 2.22 | 1589 |
| 2024-09-20 22:21:38.775 | MS1 | 121.4656617951 | 31.1446352571 | 499 | 504990 | -89.15 | 12.42 | 80.45 | 0.06 | 2.45 | 1570 |
| 2024-09-20 22:21:39.815 | MS1 | 121.4656671291 | 31.1446285255 | 499 | 504990 | -91.38 | 7.21 | 67.41 | 0.04 | 2.68 | 1591 |
| 2024-09-20 22:21:40.448 | MS1 | 121.4656593094 | 31.1446304926 | 499 | 504990 | -91.32 | 12.05 | 551.43 | 0.14 | 2.87 | 1578 |
| 2024-09-20 22:21:41.888 | MS1 | 121.4656658729 | 31.1446341368 | 499 | 504990 | -89.61 | 12.10 | 583.54 | 0.16 | 2.06 | 1575 |
| 2024-09-20 22:21:42.265 | MS1 | 121.4656615451 | 31.1446213183 | 499 | 504990 | -89.75 | 12.19 | 471.12 | 0.17 | 2.76 | 1597 |

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
| 3226541 | 1 | 121.4721786439 | 31.1469644845 | 239 | 1 | 7 | 35.0 | TDD | 499 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3265550 | 2 | 121.4676244927 | 31.1495194573 | 112 | 4 | 0 | 16.3 | TDD | 252 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3271497 | 4 | 121.4672336111 | 31.1500422300 | 21 | 5 | 12 | 39.8 | TDD | 467 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3271658 | 3 | 121.4661554243 | 31.1494866939 | 293 | 3 | 2 | 30.6 | TDD | 435 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.508 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.529 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.637 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.637 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.349 | NREventA3 | measId:2;ServCellPCI:650;Se... |
| 2024-09-20 22:21:38.589 | NRHandoverAttempt | SourcePCI:650;SourceNR-ARFC... |
| 2024-09-20 22:21:38.639 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.649 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.758 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.758 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226541 | 1 | 90.0362 | 77.7048 | -114.9180 | 17.6872 | 102.1015 | 0.0090 | 0.0029 |
| 2024_09_20 22:00 | 3265550 | 2 | 17.4439 | 11.8395 | -114.9519 | 5.2257 | 196.3124 | 0.0066 | 0.0024 |
| 2024_09_20 22:00 | 3271658 | 3 | 9.8434 | 7.5474 | -115.6048 | 11.9594 | 112.6889 | 0.0046 | 0.0059 |
| 2024_09_20 22:00 | 3271497 | 4 | 17.3342 | 11.1172 | -114.1179 | 15.1202 | 151.1366 | 0.0073 | 0.0146 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413603_E330A216 | 504990 | 499 | -86.9 | 504990 | 252 | -89.5 | 504990 | 467 | -93.2 | 504990 | 435 |
| MR_1774413603_F9CA9A22 | 504990 | 499 | -88.2 | 504990 | 252 | -93.1 | 504990 | 467 | -93.9 | 504990 | 435 |
| MR_1774413603_9CD9FAA1 | 504990 | 499 | -88.4 | 504990 | 252 | -92.4 | 504990 | 467 | -94.1 | 504990 | 435 |
| MR_1774413603_66C9B678 | 504990 | 499 | -87.2 | 504990 | 252 | -90.1 | 504990 | 467 | -93.8 | 504990 | 435 |
| MR_1774413603_FAE7FDCF | 504990 | 499 | -88.3 | 504990 | 252 | -93.3 | 504990 | 467 | -94.3 | 504990 | 435 |
| MR_1774413603_4D74B15D | 504990 | 499 | -89.3 | 504990 | 252 | -90.2 | 504990 | 467 | -93.0 | 504990 | 435 |
| MR_1774413603_9E3F99B3 | 504990 | 499 | -89.4 | 504990 | 252 | -93.0 | 504990 | 467 | -92.7 | 504990 | 435 |
| MR_1774413603_B756BD51 | 504990 | 499 | -87.5 | 504990 | 252 | -91.8 | 504990 | 467 | -96.2 | 504990 | 435 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 76: `0b8db212-993...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0b8db212-9936-45b9-9b6b-44c9b270d481` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Lift the tilt angle  of 3255874_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[76] topology](images/train_0076.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3255874_1 and 3257369_3
- `C2`: Press down the tilt angle  of 3255874_1 by 10 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212169_2
- `C4`: Increase A3 Offset threshold for 3257369_3
- `C5`: Check test server and transmission issues
- `C6`: Adjust the azimuth of 3255874_1 by 50 degrees
- `C7`: Increase transmission power for 3212169_2
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease transmission power for 3212169_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257369_3
- `C11`: Adjust the azimuth of 3212169_2 by 10 degrees
- `C12`: Press down the tilt angle of 3212169_2 by 1 degrees
- `C13`: Lift the tilt angle  of 3255874_1 by 10 degrees **← 정답**
- `C14`: Decrease A3 Offset threshold for 3257369_3
- `C15`: Decrease transmission power for 3257369_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257369_3
- `C17`: Decrease A3 Offset threshold for 3212169_2
- `C18`: Add neighbor relationship between 3212169_2 and 3257369_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212169_2
- `C20`: Increase transmission power for 3257369_3
- `C21`: Increase A3 Offset threshold for 3212169_2
- `C22`: Lift the tilt angle of 3212169_2 by 1 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.811 | MS1 | 121.4656734603 | 31.1446189470 | 742 | 504990 | -87.63 | 12.74 | 310.53 | 0.13 | 2.64 | 1565 |
| 2024-09-20 22:21:32.100 | MS1 | 121.4656605426 | 31.1446244243 | 742 | 504990 | -85.36 | 16.40 | 525.09 | 0.08 | 2.71 | 1584 |
| 2024-09-20 22:21:33.808 | MS1 | 121.4656743476 | 31.1446352516 | 742 | 504990 | -87.00 | 14.54 | 564.52 | 0.08 | 2.33 | 1577 |
| 2024-09-20 22:21:34.371 | MS1 | 121.4656670960 | 31.1446181630 | 742 | 504990 | -86.41 | 17.35 | 84.71 | 0.18 | 2.48 | 1568 |
| 2024-09-20 22:21:35.789 | MS1 | 121.4656754173 | 31.1446344880 | 742 | 504990 | -88.26 | 16.11 | 94.61 | 0.08 | 2.69 | 1592 |
| 2024-09-20 22:21:36.639 | MS1 | 121.4656725839 | 31.1446351778 | 742 | 504990 | -90.97 | 15.62 | 85.94 | 0.10 | 2.98 | 1571 |
| 2024-09-20 22:21:37.796 | MS1 | 121.4656610753 | 31.1446296245 | 742 | 504990 | -93.65 | 8.64 | 63.60 | 0.04 | 2.71 | 1562 |
| 2024-09-20 22:21:38.907 | MS1 | 121.4656712645 | 31.1446360799 | 742 | 504990 | -91.11 | 11.76 | 80.67 | 0.10 | 2.28 | 1564 |
| 2024-09-20 22:21:39.570 | MS1 | 121.4656709861 | 31.1446334650 | 742 | 504990 | -92.90 | 10.86 | 83.93 | 0.08 | 2.53 | 1566 |
| 2024-09-20 22:21:40.285 | MS1 | 121.4656713567 | 31.1446313151 | 742 | 504990 | -93.53 | 10.01 | 590.98 | 0.14 | 3.00 | 1600 |
| 2024-09-20 22:21:41.632 | MS1 | 121.4656725153 | 31.1446326749 | 742 | 504990 | -89.20 | 10.11 | 435.14 | 0.15 | 2.60 | 1579 |
| 2024-09-20 22:21:42.548 | MS1 | 121.4656632470 | 31.1446244281 | 742 | 504990 | -90.47 | 9.61 | 488.53 | 0.08 | 2.93 | 1592 |

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
| 3212169 | 2 | 121.4651118269 | 31.1554737736 | 188 | 0 | 2 | 17.2 | TDD | 742 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3255874 | 1 | 121.4718286979 | 31.1464138382 | 343 | 10 | 2 | 26.4 | TDD | 191 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3257369 | 3 | 121.4703825564 | 31.1458970278 | 121 | 9 | 6 | 37.2 | TDD | 430 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3262420 | 4 | 121.4688586493 | 31.1469971213 | 235 | 1 | 12 | 49.6 | TDD | 535 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.489 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.615 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.615 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.285 | NREventA3 | measId:2;ServCellPCI:990;Se... |
| 2024-09-20 22:21:38.525 | NRHandoverAttempt | SourcePCI:990;SourceNR-ARFC... |
| 2024-09-20 22:21:38.556 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.566 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.691 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.691 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255874 | 1 | 18.0466 | 13.6107 | -114.4199 | 8.9773 | 90.4265 | 0.0163 | 0.0096 |
| 2024_09_20 22:00 | 3212169 | 2 | 82.1245 | 92.6559 | -115.6569 | 13.6914 | 199.4045 | 0.0126 | 0.0138 |
| 2024_09_20 22:00 | 3257369 | 3 | 12.5102 | 17.2994 | -116.7628 | 19.1674 | 151.1599 | 0.0146 | 0.0165 |
| 2024_09_20 22:00 | 3262420 | 4 | 10.0235 | 17.0624 | -114.6468 | 16.0979 | 94.6155 | 0.0184 | 0.0197 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413137_2317D9BA | 504990 | 742 | -88.2 | 504990 | 430 | -91.6 | 504990 | 191 | -94.5 | 504990 | 535 |
| MR_1774413137_0EB1A0B1 | 504990 | 742 | -86.0 | 504990 | 430 | -92.3 | 504990 | 191 | -92.4 | 504990 | 535 |
| MR_1774413137_03C01618 | 504990 | 742 | -88.0 | 504990 | 430 | -94.2 | 504990 | 191 | -91.6 | 504990 | 535 |
| MR_1774413137_19BF43B8 | 504990 | 742 | -85.1 | 504990 | 430 | -93.3 | 504990 | 191 | -93.1 | 504990 | 535 |
| MR_1774413137_AC9EEA2B | 504990 | 742 | -87.1 | 504990 | 430 | -91.5 | 504990 | 191 | -92.3 | 504990 | 535 |
| MR_1774413137_A0DCF192 | 504990 | 742 | -87.2 | 504990 | 430 | -94.0 | 504990 | 191 | -93.5 | 504990 | 535 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 77: `4f3e39bd-e73...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4f3e39bd-e73a-40a8-afab-2567b09509e0` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Decrease A3 Offset threshold for 3246887_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[77] topology](images/train_0077.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3246887_3 **← 정답**
- `C2`: Decrease transmission power for 3244251_1
- `C3`: Increase transmission power for 3244251_1
- `C4`: Press down the tilt angle  of 3244251_1 by 10 degrees
- `C5`: Increase A3 Offset threshold for 3246887_3
- `C6`: Decrease transmission power for 3246887_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246887_3
- `C8`: Decrease A3 Offset threshold for 3244251_1
- `C9`: Lift the tilt angle of 3246887_3 by 10 degrees
- `C10`: Increase A3 Offset threshold for 3244251_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244251_1
- `C12`: Lift the tilt angle  of 3244251_1 by 10 degrees
- `C13`: Increase transmission power for 3246887_3
- `C14`: Adjust the azimuth of 3244251_1 by 50 degrees
- `C15`: Adjust the azimuth of 3246887_3 by 50 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244251_1
- `C17`: Check test server and transmission issues
- `C18`: Add neighbor relationship between 3260885_2 and 3244251_1
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Add neighbor relationship between 3246887_3 and 3244251_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246887_3
- `C22`: Press down the tilt angle of 3246887_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.532 | MS1 | 121.4656658115 | 31.1446330336 | 62 | 504990 | -78.02 | 16.36 | 338.35 | 0.05 | 2.60 | 1585 |
| 2024-09-20 22:21:32.522 | MS1 | 121.4656670035 | 31.1446318117 | 62 | 504990 | -77.47 | 14.90 | 490.55 | 0.19 | 2.02 | 1566 |
| 2024-09-20 22:21:33.229 | MS1 | 121.4656723564 | 31.1446291218 | 62 | 504990 | -76.08 | 12.12 | 564.83 | 0.05 | 2.80 | 1562 |
| 2024-09-20 22:21:34.788 | MS1 | 121.4656616101 | 31.1446292084 | 62 | 504990 | -86.85 | -3.26 | 46.83 | 0.10 | 1.40 | 1566 |
| 2024-09-20 22:21:35.348 | MS1 | 121.4656763470 | 31.1446254950 | 62 | 504990 | -90.19 | -3.94 | 45.81 | 0.16 | 1.02 | 1576 |
| 2024-09-20 22:21:36.311 | MS1 | 121.4656610402 | 31.1446274069 | 62 | 504990 | -83.08 | -3.35 | 41.46 | 0.08 | 1.02 | 1580 |
| 2024-09-20 22:21:37.837 | MS1 | 121.4656637515 | 31.1446376464 | 62 | 504990 | -92.34 | -3.55 | 64.98 | 0.03 | 1.14 | 1586 |
| 2024-09-20 22:21:38.388 | MS1 | 121.4656648792 | 31.1446309558 | 62 | 504990 | -89.92 | -3.48 | 22.00 | 0.17 | 1.02 | 1580 |
| 2024-09-20 22:21:39.394 | MS1 | 121.4656592995 | 31.1446300025 | 696 | 504990 | -79.58 | 17.33 | 220.85 | 0.04 | 1.23 | 1590 |
| 2024-09-20 22:21:40.282 | MS1 | 121.4656719845 | 31.1446231034 | 696 | 504990 | -80.12 | 15.93 | 419.49 | 0.06 | 2.17 | 1574 |
| 2024-09-20 22:21:41.360 | MS1 | 121.4656754112 | 31.1446334106 | 696 | 504990 | -81.01 | 18.00 | 472.86 | 0.02 | 2.72 | 1596 |
| 2024-09-20 22:21:42.180 | MS1 | 121.4656596071 | 31.1446285129 | 696 | 504990 | -82.55 | 15.35 | 447.15 | 0.07 | 2.72 | 1577 |

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
| 3244251 | 1 | 121.4718056193 | 31.1499259574 | 110 | 11 | 9 | 29.1 | TDD | 696 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3246887 | 3 | 121.4674242265 | 31.1515420729 | 15 | 9 | 5 | 21.7 | TDD | 62 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3260885 | 2 | 121.4677644131 | 31.1460399766 | 90 | 8 | 3 | 35.1 | TDD | 643 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3277858 | 4 | 121.4666673271 | 31.1515999057 | 46 | 4 | 2 | 34.9 | TDD | 767 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.468 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.488 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.592 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.592 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.297 | NREventA3 | measId:2;ServCellPCI:754;Se... |
| 2024-09-20 22:21:38.537 | NRHandoverAttempt | SourcePCI:754;SourceNR-ARFC... |
| 2024-09-20 22:21:38.571 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.583 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.703 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.703 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244251 | 1 | 7.0104 | 18.4270 | -116.3885 | 8.5940 | 190.2645 | 0.0046 | 0.0127 |
| 2024_09_20 22:00 | 3260885 | 2 | 10.2819 | 8.7095 | -114.2735 | 6.0882 | 194.3853 | 0.0031 | 0.0145 |
| 2024_09_20 22:00 | 3246887 | 3 | 11.2140 | 7.8898 | -115.9853 | 17.1774 | 100.9015 | 0.0002 | 0.1303 |
| 2024_09_20 22:00 | 3277858 | 4 | 17.8714 | 7.2385 | -115.4656 | 10.4458 | 199.6480 | 0.0024 | 0.0105 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413996_554A520B | 504990 | 62 | -87.9 | 504990 | 696 | -80.0 | 504990 | 643 | -83.0 | 504990 | 767 |
| MR_1774413996_CB9AD499 | 504990 | 62 | -88.6 | 504990 | 696 | -81.8 | 504990 | 643 | -81.3 | 504990 | 767 |
| MR_1774413996_B2974BC3 | 504990 | 62 | -87.4 | 504990 | 696 | -79.5 | 504990 | 643 | -80.7 | 504990 | 767 |
| MR_1774413996_6C7ED9C1 | 504990 | 696 | -82.3 | 504990 | 62 | -85.7 | 504990 | 643 | -83.9 | 504990 | 767 |
| MR_1774413996_1331CADC | 504990 | 62 | -87.9 | 504990 | 696 | -82.1 | 504990 | 643 | -82.7 | 504990 | 767 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 78: `79964092-9cd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `79964092-9cda-4cd4-9fcb-8284464bd1e6` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3211228_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[78] topology](images/train_0078.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264259_2
- `C2`: Decrease A3 Offset threshold for 3211228_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Check test server and transmission issues
- `C5`: Lift the tilt angle of 3211228_1 by 2 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211228_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264259_2
- `C8`: Decrease transmission power for 3264259_2
- `C9`: Decrease A3 Offset threshold for 3264259_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211228_1 **← 정답**
- `C11`: Add neighbor relationship between 3211228_1 and 3264259_2
- `C12`: Increase transmission power for 3264259_2
- `C13`: Lift the tilt angle  of 3264259_2 by 6 degrees
- `C14`: Press down the tilt angle of 3211228_1 by 2 degrees
- `C15`: Increase A3 Offset threshold for 3264259_2
- `C16`: Adjust the azimuth of 3264259_2 by 50 degrees
- `C17`: Increase A3 Offset threshold for 3211228_1
- `C18`: Press down the tilt angle  of 3264259_2 by 6 degrees
- `C19`: Adjust the azimuth of 3211228_1 by 33 degrees
- `C20`: Add neighbor relationship between 3270563_3 and 3264259_2
- `C21`: Decrease transmission power for 3211228_1
- `C22`: Increase transmission power for 3211228_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.349 | MS1 | 121.4656674888 | 31.1446357962 | 848 | 504990 | -91.52 | 13.99 | 454.96 | 0.12 | 2.02 | 1568 |
| 2024-09-20 22:21:32.801 | MS1 | 121.4656667545 | 31.1446233443 | 848 | 504990 | -90.92 | 17.68 | 412.59 | 0.05 | 2.30 | 1585 |
| 2024-09-20 22:21:33.746 | MS1 | 121.4656627691 | 31.1446235874 | 848 | 504990 | -88.80 | 15.85 | 346.31 | 0.07 | 2.15 | 1578 |
| 2024-09-20 22:21:34.207 | MS1 | 121.4656643813 | 31.1446325263 | 848 | 504990 | -88.16 | 13.85 | 67.15 | 0.66 | 2.62 | 594 |
| 2024-09-20 22:21:35.682 | MS1 | 121.4656701666 | 31.1446184742 | 848 | 504990 | -87.00 | 13.40 | 93.95 | 0.55 | 2.91 | 638 |
| 2024-09-20 22:21:36.745 | MS1 | 121.4656654251 | 31.1446219536 | 848 | 504990 | -88.01 | 14.09 | 68.03 | 0.64 | 2.05 | 544 |
| 2024-09-20 22:21:37.308 | MS1 | 121.4656600626 | 31.1446181721 | 848 | 504990 | -91.77 | 12.72 | 50.73 | 0.55 | 2.42 | 642 |
| 2024-09-20 22:21:38.640 | MS1 | 121.4656748412 | 31.1446341987 | 848 | 504990 | -89.84 | 12.28 | 63.39 | 0.52 | 2.84 | 564 |
| 2024-09-20 22:21:39.974 | MS1 | 121.4656624528 | 31.1446302082 | 848 | 504990 | -93.96 | 10.17 | 53.82 | 0.59 | 2.98 | 576 |
| 2024-09-20 22:21:40.919 | MS1 | 121.4656727695 | 31.1446370343 | 848 | 504990 | -91.61 | 7.37 | 432.77 | 0.15 | 2.54 | 1585 |
| 2024-09-20 22:21:41.136 | MS1 | 121.4656736414 | 31.1446342363 | 848 | 504990 | -90.16 | 10.37 | 588.19 | 0.07 | 2.33 | 1567 |
| 2024-09-20 22:21:42.215 | MS1 | 121.4656747399 | 31.1446289497 | 848 | 504990 | -89.69 | 7.78 | 318.81 | 0.16 | 2.58 | 1580 |

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
| 3211228 | 1 | 121.4640682985 | 31.1551129555 | 206 | 0 | 9 | 33.5 | TDD | 848 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3253869 | 4 | 121.4667998910 | 31.1441999122 | 277 | 8 | 10 | 18.0 | TDD | 680 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3264259 | 2 | 121.4705609700 | 31.1555807139 | 86 | 4 | 1 | 49.4 | TDD | 457 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3270563 | 3 | 121.4750930132 | 31.1537848581 | 25 | 0 | 5 | 36.5 | TDD | 203 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.101 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.231 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.231 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.884 | NREventA3 | measId:2;ServCellPCI:134;Se... |
| 2024-09-20 22:21:38.124 | NRHandoverAttempt | SourcePCI:134;SourceNR-ARFC... |
| 2024-09-20 22:21:38.159 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.169 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.306 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.306 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211228 | 1 | 9.0439 | 16.7213 | -115.1522 | 12.9518 | 161.8500 | 0.0095 | 0.0185 |
| 2024_09_20 22:00 | 3264259 | 2 | 14.7423 | 5.6069 | -117.5234 | 15.3410 | 147.5253 | 0.0071 | 0.0166 |
| 2024_09_20 22:00 | 3270563 | 3 | 12.6551 | 8.8854 | -114.1106 | 7.4007 | 133.7881 | 0.0174 | 0.0007 |
| 2024_09_20 22:00 | 3253869 | 4 | 9.1055 | 17.2975 | -114.4269 | 18.8357 | 83.1653 | 0.0056 | 0.0120 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414113_E6928299 | 504990 | 848 | -89.8 | 504990 | 457 | -92.3 | 504990 | 203 | -98.3 | 504990 | 680 |
| MR_1774414113_0034256A | 504990 | 848 | -87.5 | 504990 | 457 | -93.4 | 504990 | 203 | -101.9 | 504990 | 680 |
| MR_1774414113_50170AEE | 504990 | 848 | -89.8 | 504990 | 457 | -93.8 | 504990 | 203 | -101.5 | 504990 | 680 |
| MR_1774414113_EFD47E2D | 504990 | 848 | -88.5 | 504990 | 457 | -92.3 | 504990 | 203 | -101.0 | 504990 | 680 |
| MR_1774414113_A13C4D90 | 504990 | 848 | -89.9 | 504990 | 457 | -93.6 | 504990 | 203 | -99.1 | 504990 | 680 |
| MR_1774414113_CA2AFB43 | 504990 | 848 | -89.9 | 504990 | 457 | -92.0 | 504990 | 203 | -100.6 | 504990 | 680 |
| MR_1774414113_2CEB46A8 | 504990 | 848 | -87.1 | 504990 | 457 | -92.3 | 504990 | 203 | -100.1 | 504990 | 680 |
| MR_1774414113_912D54B2 | 504990 | 848 | -88.1 | 504990 | 457 | -92.2 | 504990 | 203 | -98.7 | 504990 | 680 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 79: `65e93bbb-664...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `65e93bbb-6649-4c6f-b760-df22ae943159` |
| Tag | **multiple-answer** |
| 정답 | **C10|C13|C15|C21** |
| C10 의미 | Press down the tilt angle  of 3242939_3 by 4 degrees |
| C13 의미 | Increase A3 Offset threshold for 3242690_4 |
| C15 의미 | Increase A3 Offset threshold for 3242939_3 |
| C21 의미 | Decrease transmission power for 3242939_3 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[79] topology](images/train_0079.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3242690_4 by 2 degrees
- `C2`: Adjust the azimuth of 3242939_3 by 8 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242939_3
- `C4`: Decrease A3 Offset threshold for 3242690_4
- `C5`: Lift the tilt angle  of 3242939_3 by 4 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242690_4
- `C8`: Add neighbor relationship between 3242690_4 and 3242939_3
- `C9`: Check test server and transmission issues
- `C10`: Press down the tilt angle  of 3242939_3 by 4 degrees **← 정답**
- `C11`: Increase transmission power for 3242939_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242939_3
- `C13`: Increase A3 Offset threshold for 3242690_4 **← 정답**
- `C14`: Lift the tilt angle of 3242690_4 by 2 degrees
- `C15`: Increase A3 Offset threshold for 3242939_3 **← 정답**
- `C16`: Decrease transmission power for 3242690_4
- `C17`: Decrease A3 Offset threshold for 3242939_3
- `C18`: Add neighbor relationship between 3226509_5 and 3242939_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242690_4
- `C20`: Increase transmission power for 3242690_4
- `C21`: Decrease transmission power for 3242939_3 **← 정답**
- `C22`: Adjust the azimuth of 3242690_4 by 11 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.901 | MS1 | 121.4656713972 | 31.1446276156 | 182 | 504990 | -75.79 | 16.36 | 482.53 | 0.14 | 2.07 | 1571 |
| 2024-09-20 22:21:32.111 | MS1 | 121.4656582125 | 31.1446223920 | 182 | 504990 | -79.10 | 14.88 | 351.06 | 0.16 | 2.27 | 1577 |
| 2024-09-20 22:21:33.263 | MS1 | 121.4656659282 | 31.1446368562 | 182 | 504990 | -79.35 | 13.37 | 597.03 | 0.05 | 2.74 | 1584 |
| 2024-09-20 22:21:34.182 | MS1 | 121.4656608073 | 31.1446334447 | 298 | 504990 | -80.73 | 4.48 | 28.34 | 0.03 | 1.24 | 1573 |
| 2024-09-20 22:21:35.241 | MS1 | 121.4656722982 | 31.1446370887 | 298 | 504990 | -88.75 | 4.94 | 62.56 | 0.12 | 1.41 | 1598 |
| 2024-09-20 22:21:36.407 | MS1 | 121.4656630476 | 31.1446217582 | 182 | 504990 | -82.33 | 3.35 | 48.15 | 0.20 | 1.26 | 1577 |
| 2024-09-20 22:21:37.543 | MS1 | 121.4656644628 | 31.1446194544 | 182 | 504990 | -89.37 | 1.99 | 37.32 | 0.12 | 1.30 | 1588 |
| 2024-09-20 22:21:38.481 | MS1 | 121.4656674360 | 31.1446352706 | 298 | 504990 | -84.66 | 1.48 | 39.41 | 0.10 | 1.36 | 1583 |
| 2024-09-20 22:21:39.679 | MS1 | 121.4656715872 | 31.1446202374 | 298 | 504990 | -88.43 | 3.74 | 66.84 | 0.09 | 1.16 | 1592 |
| 2024-09-20 22:21:40.435 | MS1 | 121.4656768306 | 31.1446353524 | 298 | 504990 | -80.14 | 15.58 | 315.65 | 0.11 | 2.17 | 1600 |
| 2024-09-20 22:21:41.186 | MS1 | 121.4656651005 | 31.1446303706 | 298 | 504990 | -83.99 | 12.69 | 396.51 | 0.03 | 2.33 | 1563 |
| 2024-09-20 22:21:42.756 | MS1 | 121.4656637437 | 31.1446355385 | 298 | 504990 | -77.80 | 15.98 | 487.45 | 0.11 | 2.84 | 1598 |

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
| 3223251 | 2 | 121.4705051520 | 31.1499681000 | 36 | 3 | 11 | 28.0 | TDD | 298 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3226509 | 5 | 121.4759983127 | 31.1456531197 | 101 | 12 | 0 | 39.0 | TDD | 383 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3232855 | 1 | 121.4641090000 | 31.1452215320 | 140 | 11 | 3 | 29.6 | TDD | 163 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3242690 | 4 | 121.4675590750 | 31.1525001297 | 181 | 1 | 3 | 16.3 | TDD | 182 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3242939 | 3 | 121.4745750149 | 31.1473626277 | 242 | 1 | 0 | 42.4 | TDD | 788 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.421 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.554 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.554 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.267 | NREventA3 | measId:2;ServCellPCI:918;Se... |
| 2024-09-20 22:21:34.507 | NRHandoverAttempt | SourcePCI:918;SourceNR-ARFC... |
| 2024-09-20 22:21:34.553 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.565 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:34.707 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.707 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.267 | NREventA3 | measId:2;ServCellPCI:765;Se... |
| 2024-09-20 22:21:36.507 | NRHandoverAttempt | SourcePCI:765;SourceNR-ARFC... |
| 2024-09-20 22:21:36.547 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.557 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:36.687 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.687 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.267 | NREventA3 | measId:2;ServCellPCI:918;Se... |
| 2024-09-20 22:21:38.507 | NRHandoverAttempt | SourcePCI:918;SourceNR-ARFC... |
| 2024-09-20 22:21:38.555 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.569 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.690 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.690 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232855 | 1 | 12.7369 | 6.7279 | -116.6972 | 16.3474 | 90.0389 | 0.0154 | 0.0139 |
| 2024_09_20 22:00 | 3223251 | 2 | 7.5467 | 12.4505 | -114.1314 | 11.1395 | 132.9806 | 0.0053 | 0.0184 |
| 2024_09_20 22:00 | 3242939 | 3 | 15.9031 | 5.0581 | -116.3684 | 10.1981 | 92.9268 | 0.0145 | 0.0108 |
| 2024_09_20 22:00 | 3242690 | 4 | 17.2323 | 15.6258 | -117.8196 | 15.6768 | 175.5160 | 0.0165 | 0.0011 |
| 2024_09_20 22:00 | 3226509 | 5 | 6.9138 | 9.6416 | -114.8687 | 16.6311 | 133.8954 | 0.0032 | 0.0007 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413474_B6400E09 | 504990 | 298 | -82.3 | 504990 | 182 | -81.9 | 504990 | 788 | -84.1 | 504990 | 383 |
| MR_1774413474_F7E5B59C | 504990 | 298 | -81.4 | 504990 | 182 | -81.8 | 504990 | 788 | -80.8 | 504990 | 383 |
| MR_1774413474_0B11E96F | 504990 | 182 | -79.4 | 504990 | 298 | -81.5 | 504990 | 788 | -84.2 | 504990 | 383 |
| MR_1774413474_3531E8E5 | 504990 | 298 | -82.4 | 504990 | 182 | -80.4 | 504990 | 788 | -82.5 | 504990 | 383 |
| MR_1774413474_AC6BAD77 | 504990 | 182 | -79.6 | 504990 | 298 | -80.5 | 504990 | 788 | -83.8 | 504990 | 383 |
| MR_1774413474_96E28CCC | 504990 | 182 | -78.9 | 504990 | 298 | -82.1 | 504990 | 788 | -82.5 | 504990 | 383 |
| MR_1774413474_2AE6829F | 504990 | 298 | -79.2 | 504990 | 182 | -82.0 | 504990 | 788 | -82.0 | 504990 | 383 |
| MR_1774413474_488DB69A | 504990 | 182 | -80.5 | 504990 | 298 | -80.7 | 504990 | 788 | -82.9 | 504990 | 383 |

> *... 2개 열 생략 (전체 14열)*

---
