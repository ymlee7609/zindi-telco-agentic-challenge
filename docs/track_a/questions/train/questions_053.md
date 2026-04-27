# Track A 문제 분석 — train[520]~train[529]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[520] ~ train[529] (10개)

## 목차

1. [문제 520: `db2cf7a7-983...`](#520) — multiple-answer, 정답: C13|C15
2. [문제 521: `497b2816-d8d...`](#521) — single-answer, 정답: C22
3. [문제 522: `274ad364-620...`](#522) — single-answer, 정답: C15
4. [문제 523: `de9ee636-e3a...`](#523) — single-answer, 정답: C20
5. [문제 524: `73a2602f-45a...`](#524) — single-answer, 정답: C2
6. [문제 525: `0d0ff768-fb9...`](#525) — single-answer, 정답: C11
7. [문제 526: `58ce627e-871...`](#526) — multiple-answer, 정답: C16|C17
8. [문제 527: `8febe998-2cc...`](#527) — single-answer, 정답: C6
9. [문제 528: `5fab8931-738...`](#528) — single-answer, 정답: C7
10. [문제 529: `731c126b-a1a...`](#529) — single-answer, 정답: C21

---

### 문제 520: `db2cf7a7-983...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `db2cf7a7-9837-44f5-ab1d-40c14f87c7fc` |
| Tag | **multiple-answer** |
| 정답 | **C13|C15** |
| C13 의미 | Increase transmission power for 3228979_4 |
| C15 의미 | Adjust the azimuth of 3228979_4 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[520] topology](images/train_0520.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3228979_4 and 3246451_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246451_3
- `C3`: Press down the tilt angle of 3228979_4 by 10 degrees
- `C4`: Decrease A3 Offset threshold for 3246451_3
- `C5`: Lift the tilt angle  of 3246451_3 by 2 degrees
- `C6`: Check test server and transmission issues
- `C7`: Add neighbor relationship between 3214507_2 and 3246451_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228979_4
- `C9`: Decrease transmission power for 3246451_3
- `C10`: Increase transmission power for 3246451_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246451_3
- `C12`: Adjust the azimuth of 3246451_3 by 37 degrees
- `C13`: Increase transmission power for 3228979_4 **← 정답**
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Adjust the azimuth of 3228979_4 by 50 degrees **← 정답**
- `C16`: Lift the tilt angle of 3228979_4 by 10 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228979_4
- `C18`: Increase A3 Offset threshold for 3228979_4
- `C19`: Decrease transmission power for 3228979_4
- `C20`: Increase A3 Offset threshold for 3246451_3
- `C21`: Decrease A3 Offset threshold for 3228979_4
- `C22`: Press down the tilt angle  of 3246451_3 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.637 | MS1 | 121.4656641135 | 31.1446287084 | 722 | 504990 | -93.10 | 13.14 | 515.89 | 0.05 | 2.28 | 1566 |
| 2024-09-20 22:21:32.456 | MS1 | 121.4656717038 | 31.1446357903 | 722 | 504990 | -87.47 | 15.74 | 449.18 | 0.07 | 2.54 | 1583 |
| 2024-09-20 22:21:33.258 | MS1 | 121.4656711233 | 31.1446240391 | 722 | 504990 | -86.94 | 15.95 | 470.29 | 0.10 | 2.51 | 1580 |
| 2024-09-20 22:21:34.164 | MS1 | 121.4656716784 | 31.1446333897 | 722 | 504990 | -101.17 | 0.48 | 50.73 | 0.05 | 1.34 | 1582 |
| 2024-09-20 22:21:35.690 | MS1 | 121.4656749726 | 31.1446181660 | 722 | 504990 | -108.66 | -0.24 | 26.79 | 0.08 | 1.34 | 1590 |
| 2024-09-20 22:21:36.328 | MS1 | 121.4656777984 | 31.1446295757 | 722 | 504990 | -101.95 | 1.14 | 44.66 | 0.18 | 1.28 | 1563 |
| 2024-09-20 22:21:37.232 | MS1 | 121.4656692758 | 31.1446234044 | 722 | 504990 | -102.31 | 1.79 | 69.20 | 0.02 | 1.11 | 1588 |
| 2024-09-20 22:21:38.820 | MS1 | 121.4656724439 | 31.1446240068 | 722 | 504990 | -100.17 | 0.19 | 62.73 | 0.02 | 1.01 | 1594 |
| 2024-09-20 22:21:39.816 | MS1 | 121.4656595226 | 31.1446369982 | 722 | 504990 | -103.46 | -0.36 | 40.11 | 0.09 | 1.20 | 1586 |
| 2024-09-20 22:21:40.995 | MS1 | 121.4656695794 | 31.1446216042 | 722 | 504990 | -86.96 | 13.43 | 332.38 | 0.16 | 2.72 | 1581 |
| 2024-09-20 22:21:41.401 | MS1 | 121.4656664833 | 31.1446303745 | 722 | 504990 | -89.64 | 17.60 | 335.64 | 0.12 | 2.74 | 1594 |
| 2024-09-20 22:21:42.743 | MS1 | 121.4656734052 | 31.1446323854 | 722 | 504990 | -87.08 | 17.21 | 534.29 | 0.05 | 2.36 | 1595 |

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
| 3214507 | 2 | 121.4677909343 | 31.1534311279 | 257 | 1 | 3 | 46.7 | TDD | 489 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3228979 | 4 | 121.4695875732 | 31.1468684177 | 299 | 12 | 10 | 41.3 | TDD | 722 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3235884 | 1 | 121.4747790287 | 31.1481321052 | 127 | 1 | 1 | 48.8 | TDD | 674 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3246451 | 3 | 121.4645954167 | 31.1559845873 | 212 | 0 | 8 | 46.5 | TDD | 946 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.563 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.584 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.726 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.726 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.875 | NREventA2 | measId:1;ServCellPCI:676;Se... |
| 2024-09-20 22:21:34.982 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235884 | 1 | 7.4485 | 8.0301 | -116.1159 | 7.1228 | 114.8018 | 0.0142 | 0.0053 |
| 2024_09_20 22:00 | 3214507 | 2 | 7.3967 | 16.8859 | -116.1277 | 19.2263 | 133.3554 | 0.0014 | 0.0032 |
| 2024_09_20 22:00 | 3246451 | 3 | 16.0176 | 7.5234 | -116.0367 | 5.4569 | 162.3102 | 0.0096 | 0.0123 |
| 2024_09_20 22:00 | 3228979 | 4 | 19.4489 | 13.9351 | -116.3749 | 7.2851 | 193.4536 | 0.1904 | 0.0168 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413620_96E2534B | 504990 | 722 | -101.0 | 504990 | 946 | -104.6 | 504990 | 489 | -112.6 | 504990 | 674 |
| MR_1774413620_1338DCF5 | 504990 | 722 | -101.9 | 504990 | 946 | -107.1 | 504990 | 489 | -112.1 | 504990 | 674 |
| MR_1774413620_304496D8 | 504990 | 722 | -99.5 | 504990 | 946 | -107.9 | 504990 | 489 | -112.4 | 504990 | 674 |
| MR_1774413620_FCF95668 | 504990 | 722 | -99.9 | 504990 | 946 | -105.7 | 504990 | 489 | -111.6 | 504990 | 674 |
| MR_1774413620_228F2C19 | 504990 | 722 | -100.6 | 504990 | 946 | -106.1 | 504990 | 489 | -113.3 | 504990 | 674 |
| MR_1774413620_69B8B25E | 504990 | 722 | -100.4 | 504990 | 946 | -106.6 | 504990 | 489 | -113.5 | 504990 | 674 |
| MR_1774413620_B57A4B3E | 504990 | 722 | -100.5 | 504990 | 946 | -105.1 | 504990 | 489 | -114.2 | 504990 | 674 |
| MR_1774413620_797B5A6B | 504990 | 722 | -99.7 | 504990 | 946 | -107.9 | 504990 | 489 | -112.2 | 504990 | 674 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 521: `497b2816-d8d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `497b2816-d8d8-4fc7-81bf-6e2c5fb20b04` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Lift the tilt angle  of 3244879_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[521] topology](images/train_0521.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271681_1
- `C2`: Adjust the azimuth of 3271681_1 by 44 degrees
- `C3`: Increase transmission power for 3271681_1
- `C4`: Decrease transmission power for 3257071_2
- `C5`: Check test server and transmission issues
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257071_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271681_1
- `C8`: Decrease transmission power for 3271681_1
- `C9`: Adjust the azimuth of 3244879_4 by 50 degrees
- `C10`: Add neighbor relationship between 3244879_4 and 3257071_2
- `C11`: Increase A3 Offset threshold for 3257071_2
- `C12`: Lift the tilt angle of 3271681_1 by 5 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257071_2
- `C14`: Increase transmission power for 3257071_2
- `C15`: Press down the tilt angle  of 3244879_4 by 10 degrees
- `C16`: Decrease A3 Offset threshold for 3271681_1
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Add neighbor relationship between 3271681_1 and 3257071_2
- `C19`: Increase A3 Offset threshold for 3271681_1
- `C20`: Decrease A3 Offset threshold for 3257071_2
- `C21`: Press down the tilt angle of 3271681_1 by 5 degrees
- `C22`: Lift the tilt angle  of 3244879_4 by 10 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.197 | MS1 | 121.4656703878 | 31.1446292616 | 150 | 504990 | -89.85 | 15.12 | 584.63 | 0.03 | 2.30 | 1583 |
| 2024-09-20 22:21:32.546 | MS1 | 121.4656626411 | 31.1446217409 | 150 | 504990 | -90.31 | 16.04 | 402.23 | 0.17 | 2.75 | 1567 |
| 2024-09-20 22:21:33.783 | MS1 | 121.4656662961 | 31.1446220810 | 150 | 504990 | -85.93 | 17.25 | 578.33 | 0.20 | 2.59 | 1592 |
| 2024-09-20 22:21:34.972 | MS1 | 121.4656738452 | 31.1446206328 | 150 | 504990 | -86.60 | 13.04 | 73.09 | 0.17 | 2.97 | 1600 |
| 2024-09-20 22:21:35.271 | MS1 | 121.4656775649 | 31.1446282003 | 150 | 504990 | -85.04 | 14.53 | 60.44 | 0.15 | 2.62 | 1599 |
| 2024-09-20 22:21:36.681 | MS1 | 121.4656675390 | 31.1446327690 | 150 | 504990 | -88.48 | 12.56 | 97.09 | 0.10 | 2.24 | 1569 |
| 2024-09-20 22:21:37.598 | MS1 | 121.4656603329 | 31.1446206713 | 150 | 504990 | -91.94 | 11.73 | 68.81 | 0.19 | 2.70 | 1568 |
| 2024-09-20 22:21:38.624 | MS1 | 121.4656771312 | 31.1446361813 | 150 | 504990 | -89.54 | 12.55 | 52.46 | 0.18 | 2.73 | 1587 |
| 2024-09-20 22:21:39.144 | MS1 | 121.4656581141 | 31.1446379152 | 150 | 504990 | -89.61 | 8.87 | 96.10 | 0.18 | 2.84 | 1581 |
| 2024-09-20 22:21:40.712 | MS1 | 121.4656716620 | 31.1446193540 | 150 | 504990 | -92.51 | 7.39 | 536.16 | 0.04 | 2.55 | 1572 |
| 2024-09-20 22:21:41.824 | MS1 | 121.4656761565 | 31.1446360781 | 150 | 504990 | -93.10 | 12.31 | 300.04 | 0.15 | 2.94 | 1561 |
| 2024-09-20 22:21:42.623 | MS1 | 121.4656583460 | 31.1446355894 | 150 | 504990 | -93.98 | 9.72 | 538.74 | 0.06 | 2.93 | 1598 |

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
| 3225755 | 3 | 121.4667323251 | 31.1461888286 | 92 | 12 | 5 | 48.1 | TDD | 502 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3244879 | 4 | 121.4655860057 | 31.1555825610 | 112 | 15 | 11 | 32.4 | TDD | 759 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3257071 | 2 | 121.4648013442 | 31.1452085287 | 216 | 2 | 2 | 21.5 | TDD | 67 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3271681 | 1 | 121.4730978305 | 31.1448053906 | 224 | 2 | 11 | 39.3 | TDD | 150 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.334 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.353 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.455 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.455 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.140 | NREventA3 | measId:2;ServCellPCI:566;Se... |
| 2024-09-20 22:21:38.380 | NRHandoverAttempt | SourcePCI:566;SourceNR-ARFC... |
| 2024-09-20 22:21:38.423 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.438 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.573 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.573 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271681 | 1 | 77.9452 | 82.9805 | -117.1361 | 14.9195 | 155.6303 | 0.0036 | 0.0192 |
| 2024_09_20 22:00 | 3257071 | 2 | 8.0387 | 9.3476 | -115.1768 | 10.7550 | 87.6975 | 0.0077 | 0.0029 |
| 2024_09_20 22:00 | 3225755 | 3 | 12.8397 | 5.8234 | -115.5042 | 18.1221 | 149.5092 | 0.0073 | 0.0046 |
| 2024_09_20 22:00 | 3244879 | 4 | 11.8396 | 17.5256 | -114.1789 | 19.8514 | 197.7399 | 0.0115 | 0.0021 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414360_B0534636 | 504990 | 150 | -87.5 | 504990 | 67 | -91.1 | 504990 | 759 | -97.4 | 504990 | 502 |
| MR_1774414360_2F0C238E | 504990 | 150 | -88.4 | 504990 | 67 | -92.8 | 504990 | 759 | -98.1 | 504990 | 502 |
| MR_1774414360_6636AEFD | 504990 | 150 | -84.6 | 504990 | 67 | -92.8 | 504990 | 759 | -98.3 | 504990 | 502 |
| MR_1774414360_A1B3212A | 504990 | 150 | -86.2 | 504990 | 67 | -92.6 | 504990 | 759 | -98.5 | 504990 | 502 |
| MR_1774414360_1F805068 | 504990 | 150 | -85.2 | 504990 | 67 | -90.1 | 504990 | 759 | -97.5 | 504990 | 502 |
| MR_1774414360_43CAD890 | 504990 | 150 | -87.9 | 504990 | 67 | -89.8 | 504990 | 759 | -96.7 | 504990 | 502 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 522: `274ad364-620...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `274ad364-6202-4cea-a14a-a83d5b3e68ca` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Lift the tilt angle  of 3229927_4 by 4 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[522] topology](images/train_0522.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3235202_3 by 18 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Add neighbor relationship between 3229927_4 and 3278145_1
- `C4`: Decrease transmission power for 3278145_1
- `C5`: Press down the tilt angle  of 3229927_4 by 4 degrees
- `C6`: Increase A3 Offset threshold for 3278145_1
- `C7`: Lift the tilt angle of 3235202_3 by 4 degrees
- `C8`: Increase transmission power for 3235202_3
- `C9`: Adjust the azimuth of 3229927_4 by 50 degrees
- `C10`: Press down the tilt angle of 3235202_3 by 4 degrees
- `C11`: Increase A3 Offset threshold for 3235202_3
- `C12`: Increase transmission power for 3278145_1
- `C13`: Decrease A3 Offset threshold for 3278145_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278145_1
- `C15`: Lift the tilt angle  of 3229927_4 by 4 degrees **← 정답**
- `C16`: Check test server and transmission issues
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278145_1
- `C18`: Decrease A3 Offset threshold for 3235202_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235202_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235202_3
- `C21`: Decrease transmission power for 3235202_3
- `C22`: Add neighbor relationship between 3235202_3 and 3278145_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.507 | MS1 | 121.4656659302 | 31.1446288438 | 653 | 504990 | -86.65 | 14.92 | 598.51 | 0.05 | 2.92 | 1579 |
| 2024-09-20 22:21:32.964 | MS1 | 121.4656600770 | 31.1446350593 | 653 | 504990 | -88.86 | 14.74 | 579.88 | 0.20 | 2.46 | 1568 |
| 2024-09-20 22:21:33.569 | MS1 | 121.4656651645 | 31.1446292971 | 653 | 504990 | -90.03 | 14.37 | 527.94 | 0.19 | 2.87 | 1585 |
| 2024-09-20 22:21:34.782 | MS1 | 121.4656673180 | 31.1446345367 | 653 | 504990 | -91.11 | 13.05 | 69.44 | 0.04 | 2.98 | 1568 |
| 2024-09-20 22:21:35.317 | MS1 | 121.4656735362 | 31.1446204574 | 653 | 504990 | -87.88 | 15.65 | 70.54 | 0.04 | 2.30 | 1587 |
| 2024-09-20 22:21:36.585 | MS1 | 121.4656671029 | 31.1446281376 | 653 | 504990 | -88.13 | 14.49 | 87.32 | 0.15 | 2.93 | 1595 |
| 2024-09-20 22:21:37.276 | MS1 | 121.4656751807 | 31.1446204014 | 653 | 504990 | -91.46 | 11.88 | 78.03 | 0.16 | 2.62 | 1586 |
| 2024-09-20 22:21:38.728 | MS1 | 121.4656628224 | 31.1446213320 | 653 | 504990 | -89.96 | 12.59 | 65.30 | 0.12 | 2.54 | 1576 |
| 2024-09-20 22:21:39.127 | MS1 | 121.4656762742 | 31.1446303762 | 653 | 504990 | -91.10 | 9.47 | 79.89 | 0.20 | 2.60 | 1584 |
| 2024-09-20 22:21:40.143 | MS1 | 121.4656622088 | 31.1446221356 | 653 | 504990 | -92.56 | 12.58 | 339.95 | 0.19 | 2.78 | 1573 |
| 2024-09-20 22:21:41.471 | MS1 | 121.4656665191 | 31.1446252226 | 653 | 504990 | -93.39 | 10.51 | 514.89 | 0.14 | 2.10 | 1580 |
| 2024-09-20 22:21:42.749 | MS1 | 121.4656760586 | 31.1446267984 | 653 | 504990 | -92.91 | 10.51 | 566.24 | 0.19 | 2.36 | 1565 |

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
| 3229927 | 4 | 121.4732766553 | 31.1556731150 | 6 | 7 | 0 | 40.4 | TDD | 686 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3235202 | 3 | 121.4681879846 | 31.1547967665 | 174 | 2 | 2 | 47.8 | TDD | 653 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3277355 | 2 | 121.4705632324 | 31.1468569572 | 67 | 15 | 0 | 47.9 | TDD | 170 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3278145 | 1 | 121.4661051140 | 31.1541243679 | 251 | 2 | 11 | 45.9 | TDD | 841 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.573 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.593 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.700 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.700 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.452 | NREventA3 | measId:2;ServCellPCI:961;Se... |
| 2024-09-20 22:21:38.692 | NRHandoverAttempt | SourcePCI:961;SourceNR-ARFC... |
| 2024-09-20 22:21:38.736 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.746 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.892 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.892 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278145 | 1 | 13.2066 | 16.7249 | -115.3413 | 13.0893 | 175.8569 | 0.0081 | 0.0095 |
| 2024_09_20 22:00 | 3277355 | 2 | 11.0803 | 6.5495 | -117.7075 | 18.7423 | 103.0895 | 0.0117 | 0.0184 |
| 2024_09_20 22:00 | 3235202 | 3 | 89.0872 | 86.9492 | -115.6320 | 18.2610 | 153.2021 | 0.0187 | 0.0086 |
| 2024_09_20 22:00 | 3229927 | 4 | 16.4729 | 18.4313 | -115.6207 | 9.4197 | 139.2164 | 0.0161 | 0.0167 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411986_195A58FF | 504990 | 653 | -90.6 | 504990 | 841 | -96.8 | 504990 | 686 | -103.9 | 504990 | 170 |
| MR_1774411986_AA327199 | 504990 | 653 | -90.5 | 504990 | 841 | -97.3 | 504990 | 686 | -102.9 | 504990 | 170 |
| MR_1774411986_0B0BAFE2 | 504990 | 653 | -92.1 | 504990 | 841 | -99.7 | 504990 | 686 | -102.1 | 504990 | 170 |
| MR_1774411986_3B131C78 | 504990 | 653 | -92.7 | 504990 | 841 | -99.6 | 504990 | 686 | -104.2 | 504990 | 170 |
| MR_1774411986_DC0853F5 | 504990 | 653 | -91.3 | 504990 | 841 | -97.7 | 504990 | 686 | -104.8 | 504990 | 170 |
| MR_1774411986_574E0B2B | 504990 | 653 | -89.5 | 504990 | 841 | -99.2 | 504990 | 686 | -102.9 | 504990 | 170 |
| MR_1774411986_410EA3DA | 504990 | 653 | -92.7 | 504990 | 841 | -99.6 | 504990 | 686 | -103.8 | 504990 | 170 |
| MR_1774411986_9DF90024 | 504990 | 653 | -90.9 | 504990 | 841 | -99.4 | 504990 | 686 | -104.9 | 504990 | 170 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 523: `de9ee636-e3a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `de9ee636-e3a4-42c7-b3cc-37eae2b6d447` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Add neighbor relationship between 3237555_3 and 3222699_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[523] topology](images/train_0523.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3237555_3 by 50 degrees
- `C2`: Increase A3 Offset threshold for 3237555_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222699_4
- `C4`: Increase A3 Offset threshold for 3222699_4
- `C5`: Decrease A3 Offset threshold for 3222699_4
- `C6`: Decrease A3 Offset threshold for 3237555_3
- `C7`: Press down the tilt angle  of 3222699_4 by 3 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase transmission power for 3222699_4
- `C10`: Increase transmission power for 3237555_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237555_3
- `C12`: Lift the tilt angle of 3237555_3 by 3 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237555_3
- `C14`: Check test server and transmission issues
- `C15`: Add neighbor relationship between 3241634_2 and 3222699_4
- `C16`: Decrease transmission power for 3222699_4
- `C17`: Lift the tilt angle  of 3222699_4 by 3 degrees
- `C18`: Decrease transmission power for 3237555_3
- `C19`: Press down the tilt angle of 3237555_3 by 3 degrees
- `C20`: Add neighbor relationship between 3237555_3 and 3222699_4 **← 정답**
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222699_4
- `C22`: Adjust the azimuth of 3222699_4 by 27 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.171 | MS1 | 121.4656649217 | 31.1446279428 | 500 | 504990 | -79.30 | 12.05 | 536.10 | 0.12 | 2.90 | 1561 |
| 2024-09-20 22:21:32.259 | MS1 | 121.4656715775 | 31.1446338588 | 500 | 504990 | -83.44 | 12.42 | 320.65 | 0.03 | 2.45 | 1562 |
| 2024-09-20 22:21:33.248 | MS1 | 121.4656687307 | 31.1446228172 | 500 | 504990 | -82.27 | 17.12 | 321.41 | 0.16 | 2.90 | 1563 |
| 2024-09-20 22:21:34.243 | MS1 | 121.4656589720 | 31.1446326917 | 500 | 504990 | -87.35 | -1.62 | 42.30 | 0.03 | 1.43 | 1585 |
| 2024-09-20 22:21:35.867 | MS1 | 121.4656596833 | 31.1446376184 | 500 | 504990 | -89.84 | -0.96 | 59.73 | 0.03 | 1.41 | 1587 |
| 2024-09-20 22:21:36.591 | MS1 | 121.4656580877 | 31.1446235729 | 500 | 504990 | -94.12 | -1.66 | 64.68 | 0.15 | 1.25 | 1600 |
| 2024-09-20 22:21:37.670 | MS1 | 121.4656617545 | 31.1446209783 | 500 | 504990 | -86.24 | -0.63 | 64.03 | 0.15 | 1.28 | 1595 |
| 2024-09-20 22:21:38.478 | MS1 | 121.4656653216 | 31.1446273877 | 500 | 504990 | -76.80 | 15.92 | 347.65 | 0.05 | 1.40 | 1584 |
| 2024-09-20 22:21:39.852 | MS1 | 121.4656712104 | 31.1446283284 | 500 | 504990 | -78.62 | 17.54 | 478.01 | 0.11 | 1.03 | 1574 |
| 2024-09-20 22:21:40.234 | MS1 | 121.4656777400 | 31.1446352252 | 500 | 504990 | -79.37 | 13.15 | 584.51 | 0.06 | 2.36 | 1570 |
| 2024-09-20 22:21:41.708 | MS1 | 121.4656723982 | 31.1446232778 | 500 | 504990 | -80.74 | 12.00 | 550.20 | 0.18 | 2.01 | 1582 |
| 2024-09-20 22:21:42.290 | MS1 | 121.4656589293 | 31.1446229516 | 500 | 504990 | -80.64 | 12.06 | 552.90 | 0.15 | 2.88 | 1580 |

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
| 3222699 | 4 | 121.4758174009 | 31.1522996193 | 202 | 2 | 12 | 15.1 | TDD | 903 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3237555 | 3 | 121.4701961111 | 31.1551366271 | 63 | 1 | 5 | 36.6 | TDD | 500 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3239528 | 1 | 121.4688030315 | 31.1480924285 | 99 | 10 | 5 | 32.9 | TDD | 648 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3241634 | 2 | 121.4682590651 | 31.1530340067 | 75 | 3 | 0 | 28.0 | TDD | 714 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.445 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.460 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.583 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.583 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.245 | NREventA3 | measId:2;ServCellPCI:358;Se... |
| 2024-09-20 22:21:36.245 | NREventA3 | measId:2;ServCellPCI:358;Se... |
| 2024-09-20 22:21:37.245 | NREventA3 | measId:2;ServCellPCI:358;Se... |
| 2024-09-20 22:21:39.745 | NRRRCReestablishAttempt | PCI:358 |
| 2024-09-20 22:21:39.757 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.772 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.917 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.917 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239528 | 1 | 14.1694 | 9.3582 | -114.0483 | 6.2631 | 164.3650 | 0.0075 | 0.0105 |
| 2024_09_20 22:00 | 3241634 | 2 | 9.8290 | 19.8433 | -117.7291 | 13.4615 | 102.1350 | 0.0178 | 0.0006 |
| 2024_09_20 22:00 | 3237555 | 3 | 10.2099 | 12.8963 | -116.6567 | 9.1649 | 168.8248 | 0.0013 | 0.1901 |
| 2024_09_20 22:00 | 3222699 | 4 | 10.1397 | 19.3659 | -116.9582 | 11.4949 | 102.5669 | 0.0181 | 0.0104 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414807_FF60CEFE | 504990 | 500 | -86.4 | 504990 | 903 | -82.3 | 504990 | 714 | -91.8 | 504990 | 648 |
| MR_1774414807_DEBD340F | 504990 | 500 | -88.9 | 504990 | 903 | -82.9 | 504990 | 714 | -91.1 | 504990 | 648 |
| MR_1774414807_DE231BC6 | 504990 | 903 | -82.5 | 504990 | 500 | -88.4 | 504990 | 714 | -92.0 | 504990 | 648 |
| MR_1774414807_732669BD | 504990 | 903 | -82.5 | 504990 | 500 | -86.5 | 504990 | 714 | -91.4 | 504990 | 648 |
| MR_1774414807_286A0FD9 | 504990 | 903 | -82.1 | 504990 | 500 | -87.2 | 504990 | 714 | -90.2 | 504990 | 648 |
| MR_1774414807_921A1D0F | 504990 | 500 | -86.0 | 504990 | 903 | -83.5 | 504990 | 714 | -92.6 | 504990 | 648 |
| MR_1774414807_B6C1AAF1 | 504990 | 500 | -87.1 | 504990 | 903 | -84.5 | 504990 | 714 | -93.1 | 504990 | 648 |
| MR_1774414807_0E086F47 | 504990 | 500 | -89.2 | 504990 | 903 | -81.0 | 504990 | 714 | -91.4 | 504990 | 648 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 524: `73a2602f-45a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `73a2602f-45a7-4097-867e-3f4aa0bf96e3` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212211_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[524] topology](images/train_0524.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3212211_1 by 2 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212211_1 **← 정답**
- `C3`: Increase A3 Offset threshold for 3212211_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212211_1
- `C5`: Check test server and transmission issues
- `C6`: Press down the tilt angle of 3212211_1 by 2 degrees
- `C7`: Increase transmission power for 3212211_1
- `C8`: Add neighbor relationship between 3218920_10 and 3253204_2
- `C9`: Decrease transmission power for 3253204_2
- `C10`: Adjust the azimuth of 3253204_2 by 8 degrees
- `C11`: Add neighbor relationship between 3212211_1 and 3253204_2
- `C12`: Decrease A3 Offset threshold for 3253204_2
- `C13`: Increase A3 Offset threshold for 3253204_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253204_2
- `C15`: Decrease transmission power for 3212211_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253204_2
- `C17`: Adjust the azimuth of 3212211_1 by 8 degrees
- `C18`: Press down the tilt angle  of 3253204_2 by 5 degrees
- `C19`: Increase transmission power for 3253204_2
- `C20`: Decrease A3 Offset threshold for 3212211_1
- `C21`: Lift the tilt angle  of 3253204_2 by 5 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.159 | MS1 | 121.4656594892 | 31.1446336637 | 706 | 504990 | -93.62 | 10.55 | 592.97 | 0.11 | 2.69 | 1581 |
| 2024-09-20 22:21:32.162 | MS1 | 121.4656696051 | 31.1446206073 | 568 | 504990 | -95.63 | 10.73 | 582.28 | 0.08 | 2.66 | 1596 |
| 2024-09-20 22:21:33.416 | MS1 | 121.4656648099 | 31.1446206864 | 216 | 504990 | -94.77 | 13.97 | 589.19 | 0.07 | 2.11 | 1578 |
| 2024-09-20 22:21:34.165 | MS1 | 121.4656609621 | 31.1446310028 | 64 | 152650 | -88.00 | 3.90 | 78.10 | 0.08 | 1.53 | 990 |
| 2024-09-20 22:21:35.956 | MS1 | 121.4656595456 | 31.1446234873 | 397 | 152650 | -89.54 | 2.04 | 55.38 | 0.08 | 1.66 | 930 |
| 2024-09-20 22:21:36.938 | MS1 | 121.4656775920 | 31.1446352413 | 687 | 152650 | -93.91 | 2.93 | 65.28 | 0.20 | 1.79 | 905 |
| 2024-09-20 22:21:37.119 | MS1 | 121.4656684919 | 31.1446367634 | 794 | 152650 | -89.43 | 5.44 | 46.33 | 0.13 | 1.63 | 952 |
| 2024-09-20 22:21:38.393 | MS1 | 121.4656631403 | 31.1446220649 | 64 | 152650 | -94.25 | 5.13 | 88.05 | 0.19 | 1.59 | 916 |
| 2024-09-20 22:21:39.630 | MS1 | 121.4656718682 | 31.1446231971 | 397 | 152650 | -88.47 | 6.74 | 78.40 | 0.13 | 1.57 | 934 |
| 2024-09-20 22:21:40.578 | MS1 | 121.4656655153 | 31.1446318236 | 687 | 152650 | -87.87 | 4.98 | 72.45 | 0.12 | 2.23 | 1590 |
| 2024-09-20 22:21:41.651 | MS1 | 121.4656644304 | 31.1446282234 | 794 | 152650 | -95.89 | 7.85 | 60.92 | 0.08 | 2.41 | 1561 |
| 2024-09-20 22:21:42.547 | MS1 | 121.4656605096 | 31.1446321942 | 64 | 152650 | -90.79 | 6.37 | 75.71 | 0.01 | 2.40 | 1595 |

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
| 3212211 | 1 | 121.4711668759 | 31.1492736281 | 217 | 1 | 3 | 16.5 | TDD | 706 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3218920 | 10 | 121.4678935195 | 31.1466862079 | 132 | 6 | 3 | 17.8 | FDD | 687 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3219509 | 7 | 121.4738270676 | 31.1458333710 | 272 | 14 | 0 | 15.4 | FDD | 64 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3228379 | 11 | 121.4668883369 | 31.1547504191 | 171 | 3 | 0 | 27.6 | FDD | 175 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3233774 | 6 | 121.4678277150 | 31.1449999439 | 100 | 7 | 3 | 22.4 | TDD | 216 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3235993 | 9 | 121.4721241256 | 31.1520767444 | 322 | 3 | 2 | 3.4 | FDD | 397 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3237278 | 8 | 121.4694149346 | 31.1520127879 | 227 | 4 | 6 | 12.9 | FDD | 165 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3239424 | 5 | 121.4653153004 | 31.1486383761 | 243 | 15 | 5 | 5.6 | TDD | 573 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3243346 | 12 | 121.4723077380 | 31.1452246387 | 93 | 2 | 5 | 13.9 | FDD | 794 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3253204 | 2 | 121.4679526868 | 31.1557411301 | 198 | 4 | 5 | 15.7 | TDD | 290 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3260842 | 3 | 121.4666607861 | 31.1508755780 | 230 | 1 | 2 | 12.1 | TDD | 878 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3261955 | 13 | 121.4645884306 | 31.1464379661 | 89 | 11 | 12 | 20.6 | FDD | 317 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3270105 | 4 | 121.4697532893 | 31.1536349741 | 90 | 12 | 3 | 11.0 | TDD | 568 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.985 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.003 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.141 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.141 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.857 | NREventA2 | measId:1;ServCellPCI:956;Se... |
| 2024-09-20 22:21:34.994 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.235 | NREventA5 | measId:3;ServCellPCI:956;Se... |
| 2024-09-20 22:21:35.286 | NRHandoverAttempt | SourcePCI:956;SourceNR-ARFC... |
| 2024-09-20 22:21:35.328 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.340 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.474 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.474 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212211 | 1 | 7.7212 | 16.0806 | -117.6657 | 15.7231 | 110.0541 | 0.0020 | 0.0054 |
| 2024_09_20 22:00 | 3253204 | 2 | 18.9440 | 8.6726 | -117.0681 | 9.0486 | 124.8790 | 0.0098 | 0.0172 |
| 2024_09_20 22:00 | 3260842 | 3 | 16.4657 | 9.9645 | -116.4004 | 11.5218 | 172.8551 | 0.0193 | 0.0147 |
| 2024_09_20 22:00 | 3270105 | 4 | 7.5054 | 16.6672 | -115.5557 | 19.5385 | 91.9726 | 0.0051 | 0.0167 |
| 2024_09_20 22:00 | 3239424 | 5 | 11.0472 | 5.5794 | -115.0008 | 6.6621 | 191.3101 | 0.0156 | 0.0046 |
| 2024_09_20 22:00 | 3233774 | 6 | 15.6177 | 19.3635 | -116.1129 | 12.5059 | 94.6191 | 0.0150 | 0.0011 |
| 2024_09_20 22:00 | 3219509 | 7 | 7.2991 | 6.6153 | -114.9146 | 3.6307 | 33.6617 | 0.0014 | 0.0104 |
| 2024_09_20 22:00 | 3237278 | 8 | 10.8040 | 16.3533 | -115.1906 | 3.8071 | 25.9904 | 0.0187 | 0.0072 |
| 2024_09_20 22:00 | 3235993 | 9 | 18.5258 | 17.1554 | -115.5926 | 4.0395 | 57.2881 | 0.0050 | 0.0018 |
| 2024_09_20 22:00 | 3218920 | 10 | 19.4767 | 6.5187 | -117.3852 | 3.1265 | 30.1736 | 0.0060 | 0.0133 |
| 2024_09_20 22:00 | 3228379 | 11 | 12.4468 | 19.2629 | -117.3985 | 4.4057 | 28.0874 | 0.0010 | 0.0129 |
| 2024_09_20 22:00 | 3243346 | 12 | 11.6356 | 9.4962 | -116.5962 | 3.9678 | 52.0081 | 0.0026 | 0.0001 |
| 2024_09_20 22:00 | 3261955 | 13 | 9.1703 | 15.3510 | -114.8976 | 3.5358 | 26.6543 | 0.0192 | 0.0112 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416036_77B0AD4A | 504990 | 216 | -93.9 | 504990 | 290 | -99.5 | 504990 | 573 | -96.9 | 504990 | 878 |
| MR_1774416036_FB1698EA | 504990 | 216 | -94.4 | 504990 | 290 | -97.9 | 504990 | 573 | -99.9 | 504990 | 878 |
| MR_1774416036_6F68E44F | 152650 | 64 | -86.5 | 152650 | 165 | -94.4 | 152650 | 317 | -97.7 | 152650 | 175 |
| MR_1774416036_96FDD481 | 504990 | 216 | -95.6 | 504990 | 290 | -97.0 | 504990 | 573 | -97.9 | 504990 | 878 |
| MR_1774416036_3C0D9788 | 504990 | 216 | -94.0 | 504990 | 290 | -96.9 | 504990 | 573 | -99.3 | 504990 | 878 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 525: `0d0ff768-fb9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0d0ff768-fb9b-42eb-b3cc-68a8681d7461` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[525] topology](images/train_0525.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3261388_4
- `C2`: Press down the tilt angle  of 3261388_4 by 8 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease transmission power for 3261388_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227435_1
- `C6`: Adjust the azimuth of 3227435_1 by 42 degrees
- `C7`: Lift the tilt angle  of 3261388_4 by 8 degrees
- `C8`: Lift the tilt angle of 3227435_1 by 7 degrees
- `C9`: Increase A3 Offset threshold for 3227435_1
- `C10`: Adjust the azimuth of 3261388_4 by 50 degrees
- `C11`: Check test server and transmission issues **← 정답**
- `C12`: Decrease transmission power for 3227435_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227435_1
- `C14`: Press down the tilt angle of 3227435_1 by 7 degrees
- `C15`: Decrease A3 Offset threshold for 3227435_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261388_4
- `C17`: Increase transmission power for 3227435_1
- `C18`: Decrease A3 Offset threshold for 3261388_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261388_4
- `C20`: Add neighbor relationship between 3219199_2 and 3261388_4
- `C21`: Increase transmission power for 3261388_4
- `C22`: Add neighbor relationship between 3227435_1 and 3261388_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.187 | MS1 | 121.4656750249 | 31.1446302801 | 200 | 504990 | -91.99 | 14.78 | 398.42 | 0.17 | 2.42 | 1567 |
| 2024-09-20 22:21:32.870 | MS1 | 121.4656650905 | 31.1446325630 | 200 | 504990 | -85.61 | 15.11 | 496.07 | 0.02 | 2.65 | 1584 |
| 2024-09-20 22:21:33.941 | MS1 | 121.4656620624 | 31.1446208980 | 200 | 504990 | -91.42 | 14.29 | 328.57 | 0.15 | 2.85 | 1592 |
| 2024-09-20 22:21:34.311 | MS1 | 121.4656621659 | 31.1446246252 | 200 | 504990 | -85.90 | 14.90 | 68.78 | 0.09 | 2.20 | 486 |
| 2024-09-20 22:21:35.503 | MS1 | 121.4656663342 | 31.1446183137 | 200 | 504990 | -88.60 | 13.00 | 91.40 | 0.17 | 2.14 | 327 |
| 2024-09-20 22:21:36.309 | MS1 | 121.4656702449 | 31.1446296477 | 200 | 504990 | -85.85 | 14.93 | 76.00 | 0.02 | 2.76 | 334 |
| 2024-09-20 22:21:37.541 | MS1 | 121.4656586685 | 31.1446372376 | 200 | 504990 | -89.03 | 7.09 | 58.31 | 0.13 | 2.53 | 395 |
| 2024-09-20 22:21:38.393 | MS1 | 121.4656727479 | 31.1446332977 | 200 | 504990 | -93.95 | 11.99 | 78.08 | 0.16 | 2.85 | 457 |
| 2024-09-20 22:21:39.414 | MS1 | 121.4656664180 | 31.1446307573 | 200 | 504990 | -92.59 | 11.66 | 58.01 | 0.02 | 3.00 | 425 |
| 2024-09-20 22:21:40.133 | MS1 | 121.4656585897 | 31.1446242153 | 200 | 504990 | -92.30 | 11.77 | 492.87 | 0.07 | 2.46 | 1562 |
| 2024-09-20 22:21:41.233 | MS1 | 121.4656678170 | 31.1446283447 | 200 | 504990 | -90.72 | 11.98 | 589.09 | 0.12 | 2.78 | 1560 |
| 2024-09-20 22:21:42.425 | MS1 | 121.4656720353 | 31.1446253624 | 200 | 504990 | -91.29 | 7.81 | 493.34 | 0.10 | 2.34 | 1595 |

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
| 3219199 | 2 | 121.4700991076 | 31.1557447832 | 250 | 6 | 9 | 36.0 | TDD | 342 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3227435 | 1 | 121.4689836875 | 31.1474069508 | 268 | 3 | 11 | 29.1 | TDD | 200 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3253628 | 3 | 121.4744705481 | 31.1443281803 | 40 | 6 | 4 | 22.3 | TDD | 990 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3261388 | 4 | 121.4758292362 | 31.1496902202 | 181 | 6 | 9 | 29.9 | TDD | 183 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.332 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.352 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.502 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.502 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.220 | NREventA3 | measId:2;ServCellPCI:552;Se... |
| 2024-09-20 22:21:38.460 | NRHandoverAttempt | SourcePCI:552;SourceNR-ARFC... |
| 2024-09-20 22:21:38.501 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.516 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.629 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.629 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227435 | 1 | 17.6921 | 14.6796 | -114.4626 | 6.4901 | 184.2784 | 0.0081 | 0.0066 |
| 2024_09_20 22:00 | 3219199 | 2 | 8.6173 | 5.1042 | -115.4406 | 14.7820 | 137.2721 | 0.0151 | 0.0005 |
| 2024_09_20 22:00 | 3253628 | 3 | 12.9986 | 10.9334 | -114.2439 | 8.9589 | 83.9172 | 0.0021 | 0.0080 |
| 2024_09_20 22:00 | 3261388 | 4 | 16.6141 | 17.5004 | -117.9160 | 12.7397 | 140.8653 | 0.0198 | 0.0002 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415164_7C115D8D | 504990 | 200 | -87.1 | 504990 | 183 | -89.3 | 504990 | 342 | -96.5 | 504990 | 990 |
| MR_1774415164_FAC93F68 | 504990 | 200 | -86.6 | 504990 | 183 | -88.4 | 504990 | 342 | -100.0 | 504990 | 990 |
| MR_1774415164_9F11C9F4 | 504990 | 200 | -86.5 | 504990 | 183 | -87.9 | 504990 | 342 | -96.3 | 504990 | 990 |
| MR_1774415164_38189982 | 504990 | 200 | -86.5 | 504990 | 183 | -86.3 | 504990 | 342 | -99.0 | 504990 | 990 |
| MR_1774415164_A8FD3C52 | 504990 | 200 | -84.4 | 504990 | 183 | -87.6 | 504990 | 342 | -99.6 | 504990 | 990 |
| MR_1774415164_543DF88E | 504990 | 200 | -84.7 | 504990 | 183 | -88.2 | 504990 | 342 | -97.3 | 504990 | 990 |
| MR_1774415164_E152CC6E | 504990 | 200 | -86.3 | 504990 | 183 | -86.2 | 504990 | 342 | -98.5 | 504990 | 990 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 526: `58ce627e-871...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `58ce627e-871e-4db4-8ba8-f0bf6c68b34a` |
| Tag | **multiple-answer** |
| 정답 | **C16|C17** |
| C16 의미 | Adjust the azimuth of 3275628_2 by 50 degrees |
| C17 의미 | Increase transmission power for 3275628_2 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[526] topology](images/train_0526.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3275628_2 by 10 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212346_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275628_2
- `C5`: Increase transmission power for 3212346_1
- `C6`: Decrease A3 Offset threshold for 3275628_2
- `C7`: Add neighbor relationship between 3226182_4 and 3212346_1
- `C8`: Adjust the azimuth of 3212346_1 by 44 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275628_2
- `C10`: Decrease transmission power for 3275628_2
- `C11`: Press down the tilt angle  of 3212346_1 by 3 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212346_1
- `C13`: Decrease transmission power for 3212346_1
- `C14`: Add neighbor relationship between 3275628_2 and 3212346_1
- `C15`: Check test server and transmission issues
- `C16`: Adjust the azimuth of 3275628_2 by 50 degrees **← 정답**
- `C17`: Increase transmission power for 3275628_2 **← 정답**
- `C18`: Increase A3 Offset threshold for 3212346_1
- `C19`: Lift the tilt angle of 3275628_2 by 10 degrees
- `C20`: Lift the tilt angle  of 3212346_1 by 3 degrees
- `C21`: Increase A3 Offset threshold for 3275628_2
- `C22`: Decrease A3 Offset threshold for 3212346_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.661 | MS1 | 121.4656621152 | 31.1446257705 | 561 | 504990 | -92.90 | 14.44 | 293.96 | 0.07 | 2.40 | 1596 |
| 2024-09-20 22:21:32.380 | MS1 | 121.4656742496 | 31.1446259693 | 561 | 504990 | -90.43 | 14.89 | 562.37 | 0.11 | 2.83 | 1566 |
| 2024-09-20 22:21:33.147 | MS1 | 121.4656721088 | 31.1446229778 | 561 | 504990 | -94.29 | 12.03 | 436.36 | 0.13 | 2.81 | 1570 |
| 2024-09-20 22:21:34.330 | MS1 | 121.4656615060 | 31.1446366190 | 561 | 504990 | -103.93 | -1.63 | 53.93 | 0.18 | 1.19 | 1562 |
| 2024-09-20 22:21:35.374 | MS1 | 121.4656736970 | 31.1446304878 | 561 | 504990 | -103.15 | 1.17 | 69.18 | 0.16 | 1.34 | 1597 |
| 2024-09-20 22:21:36.148 | MS1 | 121.4656656182 | 31.1446296939 | 561 | 504990 | -101.81 | -1.86 | 65.77 | 0.01 | 1.29 | 1599 |
| 2024-09-20 22:21:37.624 | MS1 | 121.4656656981 | 31.1446296019 | 561 | 504990 | -105.71 | 0.24 | 52.34 | 0.00 | 1.22 | 1563 |
| 2024-09-20 22:21:38.630 | MS1 | 121.4656643662 | 31.1446214615 | 561 | 504990 | -102.55 | -0.51 | 62.46 | 0.07 | 1.15 | 1590 |
| 2024-09-20 22:21:39.291 | MS1 | 121.4656738103 | 31.1446346300 | 561 | 504990 | -106.85 | -0.88 | 49.01 | 0.07 | 1.16 | 1582 |
| 2024-09-20 22:21:40.415 | MS1 | 121.4656587134 | 31.1446342186 | 561 | 504990 | -87.48 | 17.61 | 598.00 | 0.14 | 2.37 | 1584 |
| 2024-09-20 22:21:41.571 | MS1 | 121.4656761607 | 31.1446351974 | 561 | 504990 | -88.80 | 15.01 | 523.73 | 0.18 | 2.40 | 1585 |
| 2024-09-20 22:21:42.268 | MS1 | 121.4656607124 | 31.1446305236 | 561 | 504990 | -94.11 | 13.35 | 483.41 | 0.10 | 2.57 | 1569 |

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
| 3212346 | 1 | 121.4656707713 | 31.1530715938 | 136 | 1 | 3 | 35.5 | TDD | 100 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3226182 | 4 | 121.4746569957 | 31.1531676723 | 281 | 15 | 10 | 46.7 | TDD | 700 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3257775 | 3 | 121.4667387347 | 31.1463394549 | 358 | 3 | 8 | 18.2 | TDD | 722 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3275628 | 2 | 121.4717220680 | 31.1520047640 | 283 | 11 | 5 | 41.9 | TDD | 561 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.261 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.283 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.396 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.396 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.645 | NREventA2 | measId:1;ServCellPCI:961;Se... |
| 2024-09-20 22:21:34.766 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212346 | 1 | 8.5718 | 6.9569 | -115.6696 | 12.9407 | 83.6592 | 0.0042 | 0.0087 |
| 2024_09_20 22:00 | 3275628 | 2 | 19.2262 | 15.6055 | -117.2479 | 6.4535 | 116.5804 | 0.1400 | 0.0051 |
| 2024_09_20 22:00 | 3257775 | 3 | 14.2069 | 7.9138 | -117.8806 | 13.5278 | 112.7595 | 0.0135 | 0.0173 |
| 2024_09_20 22:00 | 3226182 | 4 | 5.3315 | 5.0356 | -115.4056 | 15.9471 | 82.2666 | 0.0166 | 0.0151 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413675_9926721F | 504990 | 561 | -104.5 | 504990 | 100 | -106.9 | 504990 | 700 | -115.6 | 504990 | 722 |
| MR_1774413675_30BDBC94 | 504990 | 561 | -102.4 | 504990 | 100 | -106.7 | 504990 | 700 | -114.8 | 504990 | 722 |
| MR_1774413675_8EACDD3E | 504990 | 561 | -102.9 | 504990 | 100 | -108.0 | 504990 | 700 | -116.5 | 504990 | 722 |
| MR_1774413675_2CE8F393 | 504990 | 561 | -105.9 | 504990 | 100 | -107.1 | 504990 | 700 | -117.0 | 504990 | 722 |
| MR_1774413675_B3CB051B | 504990 | 561 | -102.8 | 504990 | 100 | -107.7 | 504990 | 700 | -113.7 | 504990 | 722 |
| MR_1774413675_08E7023D | 504990 | 561 | -104.1 | 504990 | 100 | -108.1 | 504990 | 700 | -115.3 | 504990 | 722 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 527: `8febe998-2cc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8febe998-2cc2-47b5-a7f9-2c31eec25200` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Lift the tilt angle  of 3275632_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[527] topology](images/train_0527.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3234107_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234107_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233754_1
- `C4`: Press down the tilt angle  of 3275632_2 by 10 degrees
- `C5`: Increase transmission power for 3233754_1
- `C6`: Lift the tilt angle  of 3275632_2 by 10 degrees **← 정답**
- `C7`: Increase A3 Offset threshold for 3233754_1
- `C8`: Increase transmission power for 3234107_4
- `C9`: Decrease transmission power for 3233754_1
- `C10`: Check test server and transmission issues
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234107_4
- `C12`: Decrease A3 Offset threshold for 3233754_1
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Adjust the azimuth of 3233754_1 by 12 degrees
- `C15`: Add neighbor relationship between 3275632_2 and 3234107_4
- `C16`: Decrease A3 Offset threshold for 3234107_4
- `C17`: Decrease transmission power for 3234107_4
- `C18`: Adjust the azimuth of 3275632_2 by 50 degrees
- `C19`: Lift the tilt angle of 3233754_1 by 6 degrees
- `C20`: Add neighbor relationship between 3233754_1 and 3234107_4
- `C21`: Press down the tilt angle of 3233754_1 by 6 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233754_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.983 | MS1 | 121.4656635024 | 31.1446192806 | 326 | 504990 | -90.77 | 14.74 | 386.61 | 0.13 | 2.70 | 1591 |
| 2024-09-20 22:21:32.271 | MS1 | 121.4656698116 | 31.1446316484 | 326 | 504990 | -87.01 | 13.72 | 336.36 | 0.05 | 2.71 | 1584 |
| 2024-09-20 22:21:33.227 | MS1 | 121.4656650127 | 31.1446367465 | 326 | 504990 | -86.04 | 16.49 | 453.63 | 0.19 | 2.04 | 1569 |
| 2024-09-20 22:21:34.930 | MS1 | 121.4656774113 | 31.1446308424 | 326 | 504990 | -87.90 | 14.21 | 54.45 | 0.15 | 2.73 | 1564 |
| 2024-09-20 22:21:35.239 | MS1 | 121.4656623801 | 31.1446372354 | 326 | 504990 | -87.83 | 16.80 | 59.17 | 0.20 | 2.10 | 1582 |
| 2024-09-20 22:21:36.271 | MS1 | 121.4656614560 | 31.1446244157 | 326 | 504990 | -90.07 | 13.38 | 88.00 | 0.14 | 2.47 | 1579 |
| 2024-09-20 22:21:37.451 | MS1 | 121.4656683190 | 31.1446188518 | 326 | 504990 | -89.47 | 10.25 | 64.36 | 0.02 | 2.13 | 1586 |
| 2024-09-20 22:21:38.213 | MS1 | 121.4656768900 | 31.1446364564 | 326 | 504990 | -90.06 | 8.23 | 90.92 | 0.20 | 2.73 | 1564 |
| 2024-09-20 22:21:39.830 | MS1 | 121.4656623794 | 31.1446276575 | 326 | 504990 | -90.42 | 7.81 | 81.57 | 0.13 | 2.65 | 1574 |
| 2024-09-20 22:21:40.909 | MS1 | 121.4656763805 | 31.1446275891 | 326 | 504990 | -91.45 | 11.95 | 428.55 | 0.05 | 2.57 | 1598 |
| 2024-09-20 22:21:41.874 | MS1 | 121.4656636538 | 31.1446320807 | 326 | 504990 | -92.66 | 10.58 | 418.75 | 0.20 | 2.48 | 1581 |
| 2024-09-20 22:21:42.224 | MS1 | 121.4656714964 | 31.1446247875 | 326 | 504990 | -91.93 | 7.07 | 507.15 | 0.17 | 2.91 | 1599 |

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
| 3233754 | 1 | 121.4661136965 | 31.1504875150 | 196 | 4 | 11 | 17.9 | TDD | 326 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3234107 | 4 | 121.4700729214 | 31.1505703812 | 320 | 7 | 0 | 44.6 | TDD | 511 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3275632 | 2 | 121.4746218190 | 31.1537950366 | 49 | 4 | 12 | 24.6 | TDD | 316 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3278442 | 3 | 121.4647679599 | 31.1476466483 | 131 | 0 | 7 | 30.1 | TDD | 734 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.768 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.788 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.889 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.889 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.652 | NREventA3 | measId:2;ServCellPCI:39;Ser... |
| 2024-09-20 22:21:37.892 | NRHandoverAttempt | SourcePCI:39;SourceNR-ARFCN... |
| 2024-09-20 22:21:37.938 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.950 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.084 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.084 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233754 | 1 | 92.1092 | 75.4490 | -117.2575 | 11.2221 | 99.4441 | 0.0119 | 0.0186 |
| 2024_09_20 22:00 | 3275632 | 2 | 11.4875 | 16.8842 | -115.9407 | 12.7583 | 185.1133 | 0.0149 | 0.0062 |
| 2024_09_20 22:00 | 3278442 | 3 | 19.3760 | 12.3237 | -114.3610 | 10.0493 | 86.4488 | 0.0197 | 0.0004 |
| 2024_09_20 22:00 | 3234107 | 4 | 16.7594 | 6.3163 | -114.2081 | 16.8655 | 157.3015 | 0.0168 | 0.0166 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412838_58A711AF | 504990 | 326 | -89.6 | 504990 | 511 | -97.2 | 504990 | 316 | -99.8 | 504990 | 734 |
| MR_1774412838_CDF72492 | 504990 | 326 | -88.1 | 504990 | 511 | -98.7 | 504990 | 316 | -99.5 | 504990 | 734 |
| MR_1774412838_52C07CDD | 504990 | 326 | -88.9 | 504990 | 511 | -95.7 | 504990 | 316 | -100.6 | 504990 | 734 |
| MR_1774412838_E7DE7CA5 | 504990 | 326 | -89.4 | 504990 | 511 | -98.8 | 504990 | 316 | -98.0 | 504990 | 734 |
| MR_1774412838_F6D0B52F | 504990 | 326 | -88.7 | 504990 | 511 | -98.3 | 504990 | 316 | -100.8 | 504990 | 734 |
| MR_1774412838_1B43D06C | 504990 | 326 | -87.1 | 504990 | 511 | -99.1 | 504990 | 316 | -99.9 | 504990 | 734 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 528: `5fab8931-738...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5fab8931-7388-40c5-8a0f-d99909c009d4` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Lift the tilt angle  of 3236474_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[528] topology](images/train_0528.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Increase A3 Offset threshold for 3259876_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259876_2
- `C4`: Increase A3 Offset threshold for 3260379_1
- `C5`: Increase transmission power for 3260379_1
- `C6`: Decrease A3 Offset threshold for 3259876_2
- `C7`: Lift the tilt angle  of 3236474_4 by 10 degrees **← 정답**
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259876_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260379_1
- `C10`: Adjust the azimuth of 3259876_2 by 2 degrees
- `C11`: Add neighbor relationship between 3236474_4 and 3260379_1
- `C12`: Increase transmission power for 3259876_2
- `C13`: Lift the tilt angle of 3259876_2 by 6 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Add neighbor relationship between 3259876_2 and 3260379_1
- `C16`: Decrease transmission power for 3259876_2
- `C17`: Press down the tilt angle of 3259876_2 by 6 degrees
- `C18`: Adjust the azimuth of 3236474_4 by 50 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260379_1
- `C20`: Decrease A3 Offset threshold for 3260379_1
- `C21`: Press down the tilt angle  of 3236474_4 by 10 degrees
- `C22`: Decrease transmission power for 3260379_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.769 | MS1 | 121.4656761146 | 31.1446210529 | 561 | 504990 | -91.62 | 13.01 | 413.98 | 0.12 | 2.50 | 1565 |
| 2024-09-20 22:21:32.945 | MS1 | 121.4656662358 | 31.1446283839 | 561 | 504990 | -85.32 | 14.78 | 591.58 | 0.02 | 2.63 | 1590 |
| 2024-09-20 22:21:33.185 | MS1 | 121.4656658595 | 31.1446226987 | 561 | 504990 | -86.67 | 13.25 | 414.47 | 0.19 | 2.59 | 1584 |
| 2024-09-20 22:21:34.733 | MS1 | 121.4656754658 | 31.1446203592 | 561 | 504990 | -91.21 | 17.58 | 43.92 | 0.12 | 2.93 | 1574 |
| 2024-09-20 22:21:35.637 | MS1 | 121.4656726506 | 31.1446371503 | 561 | 504990 | -86.25 | 17.30 | 66.45 | 0.01 | 2.57 | 1596 |
| 2024-09-20 22:21:36.940 | MS1 | 121.4656593307 | 31.1446273346 | 561 | 504990 | -88.40 | 12.08 | 92.79 | 0.07 | 2.92 | 1577 |
| 2024-09-20 22:21:37.613 | MS1 | 121.4656624785 | 31.1446353363 | 561 | 504990 | -93.47 | 12.29 | 63.40 | 0.00 | 2.27 | 1587 |
| 2024-09-20 22:21:38.385 | MS1 | 121.4656624519 | 31.1446304547 | 561 | 504990 | -89.69 | 10.10 | 60.03 | 0.18 | 2.32 | 1571 |
| 2024-09-20 22:21:39.392 | MS1 | 121.4656656432 | 31.1446379507 | 561 | 504990 | -91.86 | 8.48 | 105.03 | 0.09 | 2.68 | 1582 |
| 2024-09-20 22:21:40.607 | MS1 | 121.4656631039 | 31.1446260394 | 561 | 504990 | -93.81 | 11.82 | 392.38 | 0.01 | 2.84 | 1579 |
| 2024-09-20 22:21:41.203 | MS1 | 121.4656667201 | 31.1446230410 | 561 | 504990 | -93.81 | 7.87 | 332.08 | 0.12 | 2.76 | 1588 |
| 2024-09-20 22:21:42.944 | MS1 | 121.4656728886 | 31.1446298401 | 561 | 504990 | -92.37 | 12.63 | 395.14 | 0.13 | 2.19 | 1562 |

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
| 3215213 | 3 | 121.4644115614 | 31.1520335643 | 345 | 4 | 7 | 29.8 | TDD | 131 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3236474 | 4 | 121.4659243412 | 31.1541185153 | 328 | 0 | 12 | 38.0 | TDD | 704 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3259876 | 2 | 121.4750480868 | 31.1483557120 | 247 | 3 | 2 | 49.2 | TDD | 561 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3260379 | 1 | 121.4684592300 | 31.1492432223 | 139 | 5 | 6 | 48.8 | TDD | 232 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.356 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.371 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.509 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.509 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.210 | NREventA3 | measId:2;ServCellPCI:384;Se... |
| 2024-09-20 22:21:38.450 | NRHandoverAttempt | SourcePCI:384;SourceNR-ARFC... |
| 2024-09-20 22:21:38.483 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.497 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.622 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.622 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260379 | 1 | 17.6605 | 14.7342 | -114.3620 | 12.0357 | 125.8272 | 0.0036 | 0.0115 |
| 2024_09_20 22:00 | 3259876 | 2 | 84.9834 | 75.6943 | -116.9105 | 18.5872 | 109.4292 | 0.0159 | 0.0139 |
| 2024_09_20 22:00 | 3215213 | 3 | 16.1780 | 8.2900 | -115.8063 | 10.3371 | 136.7483 | 0.0042 | 0.0059 |
| 2024_09_20 22:00 | 3236474 | 4 | 13.5031 | 15.8877 | -116.1401 | 10.6329 | 184.7120 | 0.0080 | 0.0009 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412534_57172F2A | 504990 | 561 | -91.4 | 504990 | 232 | -100.5 | 504990 | 704 | -104.2 | 504990 | 131 |
| MR_1774412534_3731E19A | 504990 | 561 | -90.2 | 504990 | 232 | -99.9 | 504990 | 704 | -104.1 | 504990 | 131 |
| MR_1774412534_4D84A630 | 504990 | 561 | -90.7 | 504990 | 232 | -98.3 | 504990 | 704 | -106.3 | 504990 | 131 |
| MR_1774412534_DA3A221C | 504990 | 561 | -90.9 | 504990 | 232 | -99.8 | 504990 | 704 | -106.0 | 504990 | 131 |
| MR_1774412534_3EA60EB9 | 504990 | 561 | -92.3 | 504990 | 232 | -100.0 | 504990 | 704 | -103.0 | 504990 | 131 |
| MR_1774412534_03448730 | 504990 | 561 | -92.9 | 504990 | 232 | -97.2 | 504990 | 704 | -104.4 | 504990 | 131 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 529: `731c126b-a1a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `731c126b-a1a8-4935-83a3-f2a1ff45662e` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Lift the tilt angle  of 3263299_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[529] topology](images/train_0529.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3263299_4 and 3269718_3
- `C2`: Increase transmission power for 3271784_2
- `C3`: Press down the tilt angle  of 3263299_4 by 10 degrees
- `C4`: Increase A3 Offset threshold for 3271784_2
- `C5`: Decrease transmission power for 3271784_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271784_2
- `C7`: Decrease A3 Offset threshold for 3269718_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271784_2
- `C9`: Lift the tilt angle of 3271784_2 by 5 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269718_3
- `C11`: Press down the tilt angle of 3271784_2 by 5 degrees
- `C12`: Increase A3 Offset threshold for 3269718_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269718_3
- `C14`: Decrease transmission power for 3269718_3
- `C15`: Decrease A3 Offset threshold for 3271784_2
- `C16`: Check test server and transmission issues
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Adjust the azimuth of 3263299_4 by 36 degrees
- `C19`: Increase transmission power for 3269718_3
- `C20`: Add neighbor relationship between 3271784_2 and 3269718_3
- `C21`: Lift the tilt angle  of 3263299_4 by 10 degrees **← 정답**
- `C22`: Adjust the azimuth of 3271784_2 by 14 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.153 | MS1 | 121.4656624354 | 31.1446305165 | 562 | 504990 | -87.60 | 15.77 | 307.37 | 0.18 | 2.90 | 1584 |
| 2024-09-20 22:21:32.332 | MS1 | 121.4656721617 | 31.1446347900 | 562 | 504990 | -88.99 | 12.54 | 403.02 | 0.08 | 2.71 | 1596 |
| 2024-09-20 22:21:33.614 | MS1 | 121.4656730277 | 31.1446230394 | 562 | 504990 | -91.36 | 16.22 | 504.86 | 0.12 | 2.54 | 1589 |
| 2024-09-20 22:21:34.866 | MS1 | 121.4656621645 | 31.1446307155 | 562 | 504990 | -90.18 | 12.22 | 77.86 | 0.11 | 2.20 | 1589 |
| 2024-09-20 22:21:35.488 | MS1 | 121.4656689187 | 31.1446294673 | 562 | 504990 | -89.50 | 12.72 | 53.42 | 0.11 | 2.14 | 1579 |
| 2024-09-20 22:21:36.340 | MS1 | 121.4656756572 | 31.1446255436 | 562 | 504990 | -87.24 | 12.44 | 65.14 | 0.05 | 2.42 | 1567 |
| 2024-09-20 22:21:37.848 | MS1 | 121.4656594068 | 31.1446264133 | 562 | 504990 | -93.44 | 8.72 | 89.45 | 0.19 | 2.25 | 1560 |
| 2024-09-20 22:21:38.782 | MS1 | 121.4656598356 | 31.1446372678 | 562 | 504990 | -92.59 | 9.16 | 83.70 | 0.03 | 2.01 | 1587 |
| 2024-09-20 22:21:39.519 | MS1 | 121.4656699397 | 31.1446299343 | 562 | 504990 | -91.99 | 12.23 | 76.93 | 0.01 | 2.72 | 1597 |
| 2024-09-20 22:21:40.308 | MS1 | 121.4656600792 | 31.1446295160 | 562 | 504990 | -90.05 | 11.65 | 456.97 | 0.06 | 2.32 | 1570 |
| 2024-09-20 22:21:41.589 | MS1 | 121.4656647630 | 31.1446180235 | 562 | 504990 | -91.53 | 8.41 | 316.26 | 0.12 | 2.32 | 1563 |
| 2024-09-20 22:21:42.946 | MS1 | 121.4656580596 | 31.1446274961 | 562 | 504990 | -90.25 | 12.20 | 526.66 | 0.14 | 2.33 | 1576 |

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
| 3240761 | 1 | 121.4704066876 | 31.1550890156 | 44 | 14 | 9 | 33.0 | TDD | 25 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3263299 | 4 | 121.4672577551 | 31.1512785039 | 77 | 0 | 11 | 45.3 | TDD | 212 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3269718 | 3 | 121.4647637181 | 31.1477103051 | 130 | 12 | 3 | 49.2 | TDD | 708 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3271784 | 2 | 121.4731090636 | 31.1534022749 | 230 | 4 | 7 | 24.3 | TDD | 562 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.783 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.808 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.917 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.917 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.677 | NREventA3 | measId:2;ServCellPCI:792;Se... |
| 2024-09-20 22:21:37.917 | NRHandoverAttempt | SourcePCI:792;SourceNR-ARFC... |
| 2024-09-20 22:21:37.954 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.966 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.069 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.069 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240761 | 1 | 19.0001 | 5.8022 | -116.4023 | 7.9632 | 194.6941 | 0.0156 | 0.0198 |
| 2024_09_20 22:00 | 3271784 | 2 | 87.2407 | 80.7471 | -115.9765 | 9.6725 | 154.0034 | 0.0102 | 0.0142 |
| 2024_09_20 22:00 | 3269718 | 3 | 16.5746 | 8.0076 | -117.4776 | 14.3261 | 153.1580 | 0.0123 | 0.0169 |
| 2024_09_20 22:00 | 3263299 | 4 | 15.9223 | 15.2802 | -115.0001 | 7.6870 | 143.2149 | 0.0029 | 0.0044 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416291_53CA1E0E | 504990 | 562 | -92.2 | 504990 | 708 | -97.1 | 504990 | 212 | -99.9 | 504990 | 25 |
| MR_1774416291_ACE05CAF | 504990 | 562 | -89.5 | 504990 | 708 | -95.0 | 504990 | 212 | -100.6 | 504990 | 25 |
| MR_1774416291_F3605F27 | 504990 | 562 | -89.8 | 504990 | 708 | -97.3 | 504990 | 212 | -101.2 | 504990 | 25 |
| MR_1774416291_0BE097CE | 504990 | 562 | -90.4 | 504990 | 708 | -96.8 | 504990 | 212 | -98.9 | 504990 | 25 |
| MR_1774416291_98E035BB | 504990 | 562 | -88.4 | 504990 | 708 | -96.0 | 504990 | 212 | -98.2 | 504990 | 25 |
| MR_1774416291_C911800E | 504990 | 562 | -91.0 | 504990 | 708 | -96.9 | 504990 | 212 | -99.3 | 504990 | 25 |

> *... 2개 열 생략 (전체 14열)*

---
