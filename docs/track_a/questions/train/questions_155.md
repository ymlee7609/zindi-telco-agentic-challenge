# Track A 문제 분석 — train[1540]~train[1549]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1540] ~ train[1549] (10개)

## 목차

1. [문제 1540: `1979ae3b-0d3...`](#1540) — multiple-answer, 정답: C2|C16
2. [문제 1541: `a19753a8-36a...`](#1541) — single-answer, 정답: C6
3. [문제 1542: `5c8bc1c7-fad...`](#1542) — single-answer, 정답: C15
4. [문제 1543: `2efbf45c-ab0...`](#1543) — single-answer, 정답: C15
5. [문제 1544: `9c407d01-281...`](#1544) — multiple-answer, 정답: C21|C22
6. [문제 1545: `5030830a-90d...`](#1545) — single-answer, 정답: C9
7. [문제 1546: `ad8f13b9-cc3...`](#1546) — single-answer, 정답: C5
8. [문제 1547: `7fe88618-894...`](#1547) — single-answer, 정답: C15
9. [문제 1548: `30694f84-507...`](#1548) — single-answer, 정답: C12
10. [문제 1549: `ba7e9076-7ef...`](#1549) — single-answer, 정답: C18

---

### 문제 1540: `1979ae3b-0d3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1979ae3b-0d38-4faf-b104-b4c8336c4eb9` |
| Tag | **multiple-answer** |
| 정답 | **C2|C16** |
| C2 의미 | Increase transmission power for 3231779_2 |
| C16 의미 | Adjust the azimuth of 3231779_2 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1540] topology](images/train_1540.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231779_2
- `C2`: Increase transmission power for 3231779_2 **← 정답**
- `C3`: Press down the tilt angle  of 3242082_3 by 5 degrees
- `C4`: Decrease A3 Offset threshold for 3242082_3
- `C5`: Lift the tilt angle of 3231779_2 by 7 degrees
- `C6`: Press down the tilt angle of 3231779_2 by 7 degrees
- `C7`: Increase A3 Offset threshold for 3231779_2
- `C8`: Decrease A3 Offset threshold for 3231779_2
- `C9`: Decrease transmission power for 3242082_3
- `C10`: Add neighbor relationship between 3267821_1 and 3242082_3
- `C11`: Adjust the azimuth of 3242082_3 by 17 degrees
- `C12`: Decrease transmission power for 3231779_2
- `C13`: Lift the tilt angle  of 3242082_3 by 5 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242082_3
- `C15`: Increase A3 Offset threshold for 3242082_3
- `C16`: Adjust the azimuth of 3231779_2 by 50 degrees **← 정답**
- `C17`: Add neighbor relationship between 3231779_2 and 3242082_3
- `C18`: Check test server and transmission issues
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231779_2
- `C20`: Increase transmission power for 3242082_3
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242082_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.584 | MS1 | 121.4656757603 | 31.1446368241 | 539 | 504990 | -93.95 | 13.53 | 529.92 | 0.05 | 2.91 | 1580 |
| 2024-09-20 22:21:32.105 | MS1 | 121.4656695191 | 31.1446220570 | 539 | 504990 | -93.11 | 17.24 | 402.12 | 0.10 | 2.53 | 1594 |
| 2024-09-20 22:21:33.639 | MS1 | 121.4656626736 | 31.1446375108 | 539 | 504990 | -86.87 | 12.91 | 405.93 | 0.11 | 2.26 | 1577 |
| 2024-09-20 22:21:34.751 | MS1 | 121.4656676009 | 31.1446243414 | 539 | 504990 | -107.47 | -0.40 | 41.34 | 0.07 | 1.12 | 1563 |
| 2024-09-20 22:21:35.147 | MS1 | 121.4656773237 | 31.1446236028 | 539 | 504990 | -104.00 | -0.83 | 49.99 | 0.14 | 1.32 | 1577 |
| 2024-09-20 22:21:36.295 | MS1 | 121.4656616419 | 31.1446240930 | 539 | 504990 | -108.45 | 0.57 | 66.90 | 0.00 | 1.50 | 1592 |
| 2024-09-20 22:21:37.157 | MS1 | 121.4656658315 | 31.1446322134 | 539 | 504990 | -102.04 | 1.34 | 68.64 | 0.16 | 1.30 | 1590 |
| 2024-09-20 22:21:38.573 | MS1 | 121.4656671773 | 31.1446340392 | 539 | 504990 | -106.07 | 0.11 | 39.49 | 0.09 | 1.01 | 1574 |
| 2024-09-20 22:21:39.458 | MS1 | 121.4656736834 | 31.1446302770 | 539 | 504990 | -105.11 | 1.32 | 72.81 | 0.17 | 1.29 | 1569 |
| 2024-09-20 22:21:40.181 | MS1 | 121.4656613592 | 31.1446285068 | 539 | 504990 | -88.99 | 17.63 | 552.76 | 0.07 | 2.56 | 1568 |
| 2024-09-20 22:21:41.427 | MS1 | 121.4656631162 | 31.1446248352 | 539 | 504990 | -87.84 | 13.70 | 385.67 | 0.11 | 2.48 | 1566 |
| 2024-09-20 22:21:42.159 | MS1 | 121.4656713776 | 31.1446367958 | 539 | 504990 | -86.55 | 17.97 | 374.28 | 0.01 | 2.60 | 1564 |

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
| 3231779 | 2 | 121.4757920562 | 31.1553441426 | 282 | 6 | 6 | 21.6 | TDD | 539 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3242082 | 3 | 121.4641671187 | 31.1551270243 | 190 | 3 | 9 | 31.6 | TDD | 366 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3248217 | 4 | 121.4750218270 | 31.1443951687 | 287 | 15 | 10 | 40.5 | TDD | 906 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3267821 | 1 | 121.4682451835 | 31.1469366112 | 201 | 12 | 2 | 15.7 | TDD | 98 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.279 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.304 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.405 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.405 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.631 | NREventA2 | measId:1;ServCellPCI:177;Se... |
| 2024-09-20 22:21:34.769 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267821 | 1 | 19.8444 | 11.6080 | -115.6942 | 7.6780 | 175.7913 | 0.0027 | 0.0140 |
| 2024_09_20 22:00 | 3231779 | 2 | 14.4626 | 19.4882 | -115.9724 | 9.7146 | 135.1489 | 0.1541 | 0.0177 |
| 2024_09_20 22:00 | 3242082 | 3 | 16.5277 | 17.8953 | -114.5811 | 9.7642 | 199.0993 | 0.0082 | 0.0016 |
| 2024_09_20 22:00 | 3248217 | 4 | 13.5635 | 19.2862 | -116.0142 | 10.8666 | 116.8382 | 0.0117 | 0.0152 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412782_B70E8DAB | 504990 | 539 | -106.7 | 504990 | 366 | -115.6 | 504990 | 98 | -118.0 | 504990 | 906 |
| MR_1774412782_95877E6D | 504990 | 539 | -108.0 | 504990 | 366 | -115.5 | 504990 | 98 | -118.1 | 504990 | 906 |
| MR_1774412782_5295363D | 504990 | 539 | -107.2 | 504990 | 366 | -116.2 | 504990 | 98 | -120.7 | 504990 | 906 |
| MR_1774412782_071A08A3 | 504990 | 539 | -108.1 | 504990 | 366 | -115.3 | 504990 | 98 | -120.3 | 504990 | 906 |
| MR_1774412782_FF73AFD5 | 504990 | 539 | -106.8 | 504990 | 366 | -116.1 | 504990 | 98 | -118.5 | 504990 | 906 |
| MR_1774412782_7261AEAE | 504990 | 539 | -107.9 | 504990 | 366 | -115.4 | 504990 | 98 | -118.0 | 504990 | 906 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1541: `a19753a8-36a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a19753a8-36a6-41ed-9331-91e58accd33e` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3269862_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1541] topology](images/train_1541.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3269862_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269862_1
- `C3`: Add neighbor relationship between 3269862_1 and 3222542_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222542_3
- `C5`: Increase transmission power for 3222542_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269862_1 **← 정답**
- `C7`: Lift the tilt angle of 3269862_1 by 3 degrees
- `C8`: Adjust the azimuth of 3222542_3 by 50 degrees
- `C9`: Adjust the azimuth of 3269862_1 by 35 degrees
- `C10`: Increase transmission power for 3269862_1
- `C11`: Increase A3 Offset threshold for 3269862_1
- `C12`: Add neighbor relationship between 3265104_2 and 3222542_3
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222542_3
- `C15`: Decrease transmission power for 3222542_3
- `C16`: Check test server and transmission issues
- `C17`: Increase A3 Offset threshold for 3222542_3
- `C18`: Press down the tilt angle of 3269862_1 by 3 degrees
- `C19`: Press down the tilt angle  of 3222542_3 by 10 degrees
- `C20`: Decrease transmission power for 3269862_1
- `C21`: Decrease A3 Offset threshold for 3222542_3
- `C22`: Lift the tilt angle  of 3222542_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.950 | MS1 | 121.4656731535 | 31.1446294243 | 520 | 504990 | -87.39 | 15.07 | 581.69 | 0.03 | 2.76 | 1586 |
| 2024-09-20 22:21:32.400 | MS1 | 121.4656768898 | 31.1446319309 | 520 | 504990 | -85.62 | 15.36 | 466.19 | 0.20 | 2.80 | 1565 |
| 2024-09-20 22:21:33.861 | MS1 | 121.4656689507 | 31.1446327641 | 520 | 504990 | -85.39 | 14.96 | 576.69 | 0.15 | 2.99 | 1573 |
| 2024-09-20 22:21:34.164 | MS1 | 121.4656656998 | 31.1446247625 | 520 | 504990 | -85.54 | 16.56 | 61.74 | 0.67 | 2.34 | 675 |
| 2024-09-20 22:21:35.361 | MS1 | 121.4656615957 | 31.1446205376 | 520 | 504990 | -91.92 | 13.64 | 92.63 | 0.51 | 2.88 | 631 |
| 2024-09-20 22:21:36.405 | MS1 | 121.4656637851 | 31.1446365885 | 520 | 504990 | -91.56 | 15.94 | 79.35 | 0.58 | 2.63 | 668 |
| 2024-09-20 22:21:37.392 | MS1 | 121.4656618239 | 31.1446238415 | 520 | 504990 | -91.78 | 10.32 | 90.53 | 0.56 | 2.82 | 601 |
| 2024-09-20 22:21:38.295 | MS1 | 121.4656613938 | 31.1446215189 | 520 | 504990 | -91.70 | 11.67 | 89.02 | 0.69 | 2.78 | 543 |
| 2024-09-20 22:21:39.815 | MS1 | 121.4656745937 | 31.1446261726 | 520 | 504990 | -90.40 | 12.66 | 68.80 | 0.68 | 2.36 | 617 |
| 2024-09-20 22:21:40.374 | MS1 | 121.4656606948 | 31.1446307376 | 520 | 504990 | -93.62 | 7.62 | 435.36 | 0.14 | 2.24 | 1576 |
| 2024-09-20 22:21:41.649 | MS1 | 121.4656777957 | 31.1446318641 | 520 | 504990 | -90.70 | 12.98 | 375.12 | 0.07 | 2.93 | 1574 |
| 2024-09-20 22:21:42.347 | MS1 | 121.4656655743 | 31.1446288286 | 520 | 504990 | -91.03 | 8.93 | 374.99 | 0.05 | 2.64 | 1581 |

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
| 3222542 | 3 | 121.4661612204 | 31.1444932436 | 118 | 12 | 2 | 21.2 | TDD | 204 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3231834 | 4 | 121.4744225905 | 31.1513226084 | 144 | 11 | 10 | 22.5 | TDD | 701 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3265104 | 2 | 121.4746799317 | 31.1471991971 | 4 | 15 | 7 | 32.7 | TDD | 80 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3269862 | 1 | 121.4757275856 | 31.1509118147 | 199 | 1 | 11 | 43.5 | TDD | 520 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.055 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.196 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.196 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.919 | NREventA3 | measId:2;ServCellPCI:825;Se... |
| 2024-09-20 22:21:38.159 | NRHandoverAttempt | SourcePCI:825;SourceNR-ARFC... |
| 2024-09-20 22:21:38.192 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.204 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.351 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.351 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269862 | 1 | 6.8523 | 18.8531 | -114.7689 | 12.3847 | 83.4089 | 0.0065 | 0.0106 |
| 2024_09_20 22:00 | 3265104 | 2 | 8.7331 | 16.7241 | -116.5468 | 19.0804 | 95.7326 | 0.0154 | 0.0154 |
| 2024_09_20 22:00 | 3222542 | 3 | 19.8784 | 7.6027 | -117.0806 | 5.6141 | 188.9883 | 0.0070 | 0.0123 |
| 2024_09_20 22:00 | 3231834 | 4 | 10.6145 | 7.5916 | -114.6848 | 6.8055 | 199.0715 | 0.0027 | 0.0192 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415930_B7AC53B1 | 504990 | 520 | -86.0 | 504990 | 204 | -90.3 | 504990 | 80 | -96.4 | 504990 | 701 |
| MR_1774415930_3DEBB08B | 504990 | 520 | -85.9 | 504990 | 204 | -93.2 | 504990 | 80 | -97.5 | 504990 | 701 |
| MR_1774415930_79CDE265 | 504990 | 520 | -83.7 | 504990 | 204 | -91.1 | 504990 | 80 | -95.2 | 504990 | 701 |
| MR_1774415930_0BB5DC1D | 504990 | 520 | -83.9 | 504990 | 204 | -90.8 | 504990 | 80 | -97.2 | 504990 | 701 |
| MR_1774415930_1D6642BD | 504990 | 520 | -86.0 | 504990 | 204 | -90.3 | 504990 | 80 | -96.4 | 504990 | 701 |
| MR_1774415930_03BF7077 | 504990 | 520 | -84.1 | 504990 | 204 | -94.0 | 504990 | 80 | -96.0 | 504990 | 701 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1542: `5c8bc1c7-fad...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5c8bc1c7-fad9-400c-ba57-c681b024dc62` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210085_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1542] topology](images/train_1542.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3210085_3 by 13 degrees
- `C2`: Increase transmission power for 3263494_5
- `C3`: Increase transmission power for 3210085_3
- `C4`: Add neighbor relationship between 3210085_3 and 3263494_5
- `C5`: Decrease A3 Offset threshold for 3210085_3
- `C6`: Check test server and transmission issues
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Lift the tilt angle of 3210085_3 by 4 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210085_3
- `C10`: Decrease transmission power for 3263494_5
- `C11`: Decrease transmission power for 3210085_3
- `C12`: Increase A3 Offset threshold for 3263494_5
- `C13`: Adjust the azimuth of 3263494_5 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263494_5
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210085_3 **← 정답**
- `C16`: Add neighbor relationship between 3250467_10 and 3263494_5
- `C17`: Press down the tilt angle  of 3263494_5 by 1 degrees
- `C18`: Decrease A3 Offset threshold for 3263494_5
- `C19`: Increase A3 Offset threshold for 3210085_3
- `C20`: Press down the tilt angle of 3210085_3 by 4 degrees
- `C21`: Lift the tilt angle  of 3263494_5 by 1 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263494_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.830 | MS1 | 121.4656701401 | 31.1446355268 | 492 | 504990 | -93.07 | 14.56 | 492.34 | 0.19 | 2.31 | 1560 |
| 2024-09-20 22:21:32.369 | MS1 | 121.4656695563 | 31.1446371438 | 207 | 504990 | -95.44 | 10.26 | 573.25 | 0.07 | 2.10 | 1583 |
| 2024-09-20 22:21:33.126 | MS1 | 121.4656653655 | 31.1446209465 | 674 | 504990 | -95.82 | 10.49 | 504.27 | 0.06 | 2.58 | 1591 |
| 2024-09-20 22:21:34.756 | MS1 | 121.4656603909 | 31.1446312021 | 352 | 152650 | -88.02 | 3.17 | 98.79 | 0.10 | 1.69 | 962 |
| 2024-09-20 22:21:35.960 | MS1 | 121.4656652246 | 31.1446312247 | 583 | 152650 | -96.69 | 2.06 | 49.48 | 0.11 | 1.87 | 930 |
| 2024-09-20 22:21:36.197 | MS1 | 121.4656662641 | 31.1446197690 | 746 | 152650 | -93.34 | 4.77 | 96.40 | 0.20 | 1.90 | 960 |
| 2024-09-20 22:21:37.940 | MS1 | 121.4656672435 | 31.1446272188 | 659 | 152650 | -91.62 | 3.57 | 54.41 | 0.16 | 1.62 | 971 |
| 2024-09-20 22:21:38.714 | MS1 | 121.4656631661 | 31.1446195230 | 352 | 152650 | -95.45 | 7.07 | 99.91 | 0.02 | 1.54 | 937 |
| 2024-09-20 22:21:39.505 | MS1 | 121.4656706831 | 31.1446207758 | 583 | 152650 | -89.76 | 2.68 | 93.06 | 0.17 | 1.59 | 979 |
| 2024-09-20 22:21:40.991 | MS1 | 121.4656688597 | 31.1446236406 | 746 | 152650 | -92.34 | 3.80 | 76.68 | 0.18 | 2.23 | 1596 |
| 2024-09-20 22:21:41.538 | MS1 | 121.4656676544 | 31.1446226630 | 659 | 152650 | -91.51 | 3.06 | 73.41 | 0.16 | 2.91 | 1597 |
| 2024-09-20 22:21:42.454 | MS1 | 121.4656731862 | 31.1446266183 | 352 | 152650 | -89.28 | 6.95 | 97.30 | 0.08 | 2.55 | 1588 |

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
| 3210085 | 3 | 121.4726993439 | 31.1477708690 | 229 | 3 | 2 | 8.5 | TDD | 492 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3212712 | 4 | 121.4655316966 | 31.1469189091 | 334 | 11 | 2 | 6.6 | TDD | 207 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3220276 | 6 | 121.4650532539 | 31.1493046547 | 320 | 0 | 12 | 27.6 | TDD | 695 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3226786 | 13 | 121.4752111389 | 31.1545771462 | 336 | 4 | 0 | 19.4 | FDD | 606 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3227467 | 2 | 121.4715050160 | 31.1524365891 | 84 | 12 | 7 | 1.0 | TDD | 520 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3234849 | 8 | 121.4688039206 | 31.1552519450 | 16 | 7 | 7 | 8.8 | FDD | 583 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3239285 | 12 | 121.4703482358 | 31.1524522784 | 241 | 1 | 11 | 2.5 | FDD | 637 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3247804 | 1 | 121.4729121994 | 31.1530447276 | 62 | 5 | 12 | 2.4 | TDD | 674 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3250467 | 10 | 121.4729844135 | 31.1556735709 | 280 | 9 | 6 | 13.7 | FDD | 746 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3253394 | 11 | 121.4718915880 | 31.1499140068 | 270 | 10 | 7 | 5.4 | FDD | 659 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3254983 | 7 | 121.4746305601 | 31.1508277426 | 118 | 7 | 2 | 17.5 | FDD | 352 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3263494 | 5 | 121.4758028599 | 31.1448369757 | 259 | 0 | 8 | 11.3 | TDD | 86 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3265798 | 9 | 121.4733834971 | 31.1519549510 | 54 | 9 | 9 | 18.5 | FDD | 168 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |

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
| 2024-09-20 22:21:31.115 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.134 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.242 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.242 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.988 | NREventA2 | measId:1;ServCellPCI:139;Se... |
| 2024-09-20 22:21:35.116 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.379 | NREventA5 | measId:3;ServCellPCI:139;Se... |
| 2024-09-20 22:21:35.436 | NRHandoverAttempt | SourcePCI:139;SourceNR-ARFC... |
| 2024-09-20 22:21:35.484 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.496 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.645 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.645 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247804 | 1 | 7.3359 | 13.3962 | -117.7991 | 8.4997 | 130.1676 | 0.0013 | 0.0195 |
| 2024_09_20 22:00 | 3227467 | 2 | 6.6643 | 17.0494 | -117.8947 | 5.3734 | 178.3219 | 0.0057 | 0.0000 |
| 2024_09_20 22:00 | 3210085 | 3 | 9.0061 | 14.1014 | -117.4004 | 17.7761 | 145.9773 | 0.0199 | 0.0154 |
| 2024_09_20 22:00 | 3212712 | 4 | 9.7343 | 6.5495 | -115.2379 | 7.7295 | 130.4584 | 0.0172 | 0.0032 |
| 2024_09_20 22:00 | 3263494 | 5 | 19.5940 | 18.1480 | -116.6609 | 6.1882 | 151.1504 | 0.0171 | 0.0159 |
| 2024_09_20 22:00 | 3220276 | 6 | 8.3799 | 11.9385 | -115.7895 | 7.1051 | 98.6374 | 0.0165 | 0.0086 |
| 2024_09_20 22:00 | 3254983 | 7 | 9.7685 | 13.3856 | -114.8733 | 3.9923 | 23.4494 | 0.0115 | 0.0118 |
| 2024_09_20 22:00 | 3234849 | 8 | 18.2260 | 16.0764 | -115.9527 | 4.6703 | 41.4600 | 0.0188 | 0.0073 |
| 2024_09_20 22:00 | 3265798 | 9 | 14.1028 | 16.4758 | -117.2545 | 3.4270 | 57.5558 | 0.0027 | 0.0157 |
| 2024_09_20 22:00 | 3250467 | 10 | 10.1096 | 7.8681 | -114.8401 | 4.6558 | 25.8100 | 0.0115 | 0.0125 |
| 2024_09_20 22:00 | 3253394 | 11 | 5.4955 | 7.9002 | -117.1370 | 3.1353 | 54.0781 | 0.0185 | 0.0144 |
| 2024_09_20 22:00 | 3239285 | 12 | 17.2604 | 15.1878 | -117.2176 | 4.2877 | 59.5527 | 0.0091 | 0.0101 |
| 2024_09_20 22:00 | 3226786 | 13 | 12.5191 | 15.6799 | -115.2903 | 3.2209 | 40.3315 | 0.0188 | 0.0125 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413442_456C0EF3 | 504990 | 674 | -95.0 | 504990 | 86 | -93.7 | 504990 | 695 | -98.0 | 504990 | 520 |
| MR_1774413442_7ABB047F | 504990 | 674 | -97.3 | 504990 | 86 | -94.8 | 504990 | 695 | -98.8 | 504990 | 520 |
| MR_1774413442_CE1CCA54 | 504990 | 674 | -95.3 | 504990 | 86 | -94.5 | 504990 | 695 | -98.8 | 504990 | 520 |
| MR_1774413442_9AC99525 | 152650 | 352 | -89.5 | 152650 | 606 | -96.3 | 152650 | 637 | -93.5 | 152650 | 168 |
| MR_1774413442_50C8F44D | 152650 | 352 | -88.7 | 152650 | 606 | -95.6 | 152650 | 637 | -94.9 | 152650 | 168 |
| MR_1774413442_5B6DC8A2 | 504990 | 674 | -97.2 | 504990 | 86 | -92.0 | 504990 | 695 | -97.7 | 504990 | 520 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1543: `2efbf45c-ab0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2efbf45c-ab02-4c53-bc5f-1a529793f986` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease A3 Offset threshold for 3252480_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1543] topology](images/train_1543.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3264872_1
- `C2`: Increase transmission power for 3252480_3
- `C3`: Adjust the azimuth of 3264872_1 by 50 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264872_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252480_3
- `C6`: Add neighbor relationship between 3252480_3 and 3264872_1
- `C7`: Lift the tilt angle of 3252480_3 by 7 degrees
- `C8`: Add neighbor relationship between 3258743_4 and 3264872_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Lift the tilt angle  of 3264872_1 by 10 degrees
- `C11`: Decrease A3 Offset threshold for 3264872_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252480_3
- `C13`: Press down the tilt angle  of 3264872_1 by 10 degrees
- `C14`: Press down the tilt angle of 3252480_3 by 7 degrees
- `C15`: Decrease A3 Offset threshold for 3252480_3 **← 정답**
- `C16`: Decrease transmission power for 3252480_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264872_1
- `C18`: Increase A3 Offset threshold for 3252480_3
- `C19`: Adjust the azimuth of 3252480_3 by 50 degrees
- `C20`: Check test server and transmission issues
- `C21`: Increase A3 Offset threshold for 3264872_1
- `C22`: Increase transmission power for 3264872_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.291 | MS1 | 121.4656750677 | 31.1446355796 | 606 | 504990 | -84.56 | 13.35 | 529.11 | 0.03 | 3.00 | 1566 |
| 2024-09-20 22:21:32.971 | MS1 | 121.4656589844 | 31.1446357435 | 606 | 504990 | -84.62 | 12.40 | 494.86 | 0.12 | 2.27 | 1596 |
| 2024-09-20 22:21:33.934 | MS1 | 121.4656738477 | 31.1446271920 | 606 | 504990 | -84.00 | 15.13 | 420.95 | 0.19 | 2.12 | 1592 |
| 2024-09-20 22:21:34.471 | MS1 | 121.4656609371 | 31.1446306424 | 606 | 504990 | -90.81 | -0.84 | 46.91 | 0.02 | 1.08 | 1569 |
| 2024-09-20 22:21:35.691 | MS1 | 121.4656598748 | 31.1446191040 | 606 | 504990 | -91.74 | -1.77 | 36.47 | 0.05 | 1.15 | 1596 |
| 2024-09-20 22:21:36.207 | MS1 | 121.4656585801 | 31.1446209120 | 606 | 504990 | -89.18 | -2.55 | 36.32 | 0.10 | 1.03 | 1562 |
| 2024-09-20 22:21:37.880 | MS1 | 121.4656755540 | 31.1446216558 | 606 | 504990 | -88.32 | -3.67 | 80.14 | 0.06 | 1.41 | 1596 |
| 2024-09-20 22:21:38.916 | MS1 | 121.4656690855 | 31.1446181943 | 606 | 504990 | -91.57 | -2.62 | 61.02 | 0.06 | 1.23 | 1577 |
| 2024-09-20 22:21:39.159 | MS1 | 121.4656636367 | 31.1446276077 | 824 | 504990 | -80.63 | 17.48 | 203.95 | 0.08 | 1.01 | 1572 |
| 2024-09-20 22:21:40.203 | MS1 | 121.4656626010 | 31.1446280622 | 824 | 504990 | -76.86 | 16.32 | 401.46 | 0.03 | 2.56 | 1565 |
| 2024-09-20 22:21:41.903 | MS1 | 121.4656671850 | 31.1446308546 | 824 | 504990 | -82.94 | 12.66 | 352.16 | 0.11 | 2.44 | 1600 |
| 2024-09-20 22:21:42.921 | MS1 | 121.4656637234 | 31.1446345058 | 824 | 504990 | -76.19 | 15.66 | 363.77 | 0.16 | 2.57 | 1598 |

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
| 3216393 | 2 | 121.4681914739 | 31.1473204898 | 63 | 10 | 11 | 29.7 | TDD | 732 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3252480 | 3 | 121.4661128762 | 31.1479401203 | 135 | 4 | 1 | 17.0 | TDD | 606 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3258743 | 4 | 121.4693654198 | 31.1502233584 | 192 | 0 | 6 | 35.0 | TDD | 271 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3264872 | 1 | 121.4668118766 | 31.1536987129 | 116 | 8 | 0 | 45.6 | TDD | 824 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.248 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.264 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.372 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.372 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.086 | NREventA3 | measId:2;ServCellPCI:483;Se... |
| 2024-09-20 22:21:38.326 | NRHandoverAttempt | SourcePCI:483;SourceNR-ARFC... |
| 2024-09-20 22:21:38.375 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.388 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.496 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.496 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264872 | 1 | 13.8322 | 8.5158 | -115.2589 | 16.8867 | 179.6767 | 0.0108 | 0.0045 |
| 2024_09_20 22:00 | 3216393 | 2 | 18.3288 | 18.9788 | -116.6026 | 11.4603 | 109.5805 | 0.0077 | 0.0182 |
| 2024_09_20 22:00 | 3252480 | 3 | 10.0171 | 9.9285 | -114.2915 | 17.2920 | 181.4181 | 0.0033 | 0.1625 |
| 2024_09_20 22:00 | 3258743 | 4 | 12.8616 | 12.4085 | -114.8661 | 11.4402 | 100.5920 | 0.0068 | 0.0042 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416497_0738B4BC | 504990 | 606 | -92.0 | 504990 | 824 | -84.6 | 504990 | 271 | -88.1 | 504990 | 732 |
| MR_1774416497_E4C89134 | 504990 | 606 | -90.3 | 504990 | 824 | -86.7 | 504990 | 271 | -89.6 | 504990 | 732 |
| MR_1774416497_0E891D02 | 504990 | 824 | -83.9 | 504990 | 606 | -91.2 | 504990 | 271 | -87.5 | 504990 | 732 |
| MR_1774416497_99701240 | 504990 | 824 | -85.4 | 504990 | 606 | -92.5 | 504990 | 271 | -89.5 | 504990 | 732 |
| MR_1774416497_D3EA2E4E | 504990 | 824 | -86.0 | 504990 | 606 | -89.7 | 504990 | 271 | -86.8 | 504990 | 732 |
| MR_1774416497_028182A7 | 504990 | 824 | -85.8 | 504990 | 606 | -91.2 | 504990 | 271 | -87.1 | 504990 | 732 |
| MR_1774416497_6A31D562 | 504990 | 824 | -85.7 | 504990 | 606 | -91.3 | 504990 | 271 | -87.5 | 504990 | 732 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1544: `9c407d01-281...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9c407d01-2812-448d-91b4-3fce35e72b4d` |
| Tag | **multiple-answer** |
| 정답 | **C21|C22** |
| C21 의미 | Adjust the azimuth of 3246883_3 by 50 degrees |
| C22 의미 | Increase transmission power for 3246883_3 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1544] topology](images/train_1544.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3246883_3 by 10 degrees
- `C2`: Adjust the azimuth of 3243064_1 by 38 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Lift the tilt angle  of 3243064_1 by 5 degrees
- `C5`: Decrease transmission power for 3246883_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246883_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246883_3
- `C8`: Decrease transmission power for 3243064_1
- `C9`: Press down the tilt angle  of 3243064_1 by 5 degrees
- `C10`: Increase A3 Offset threshold for 3243064_1
- `C11`: Add neighbor relationship between 3241682_2 and 3243064_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243064_1
- `C13`: Increase transmission power for 3243064_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243064_1
- `C15`: Increase A3 Offset threshold for 3246883_3
- `C16`: Check test server and transmission issues
- `C17`: Decrease A3 Offset threshold for 3243064_1
- `C18`: Decrease A3 Offset threshold for 3246883_3
- `C19`: Add neighbor relationship between 3246883_3 and 3243064_1
- `C20`: Press down the tilt angle of 3246883_3 by 10 degrees
- `C21`: Adjust the azimuth of 3246883_3 by 50 degrees **← 정답**
- `C22`: Increase transmission power for 3246883_3 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.713 | MS1 | 121.4656694854 | 31.1446281502 | 164 | 504990 | -87.58 | 13.89 | 360.79 | 0.11 | 2.18 | 1600 |
| 2024-09-20 22:21:32.510 | MS1 | 121.4656590428 | 31.1446180361 | 164 | 504990 | -91.22 | 13.79 | 351.63 | 0.13 | 2.40 | 1584 |
| 2024-09-20 22:21:33.296 | MS1 | 121.4656591015 | 31.1446245068 | 164 | 504990 | -85.44 | 13.86 | 582.08 | 0.06 | 2.98 | 1599 |
| 2024-09-20 22:21:34.980 | MS1 | 121.4656665822 | 31.1446347661 | 164 | 504990 | -108.73 | -0.81 | 25.21 | 0.07 | 1.27 | 1563 |
| 2024-09-20 22:21:35.519 | MS1 | 121.4656667347 | 31.1446189305 | 164 | 504990 | -101.96 | -1.32 | 29.51 | 0.08 | 1.30 | 1562 |
| 2024-09-20 22:21:36.609 | MS1 | 121.4656710015 | 31.1446303171 | 164 | 504990 | -107.55 | 1.81 | 68.90 | 0.00 | 1.17 | 1584 |
| 2024-09-20 22:21:37.414 | MS1 | 121.4656600903 | 31.1446266745 | 164 | 504990 | -102.86 | 0.14 | 24.17 | 0.10 | 1.47 | 1592 |
| 2024-09-20 22:21:38.379 | MS1 | 121.4656724181 | 31.1446223474 | 164 | 504990 | -108.85 | 1.41 | 77.83 | 0.19 | 1.39 | 1589 |
| 2024-09-20 22:21:39.586 | MS1 | 121.4656600164 | 31.1446325483 | 164 | 504990 | -102.30 | -0.72 | 51.88 | 0.07 | 1.21 | 1586 |
| 2024-09-20 22:21:40.148 | MS1 | 121.4656580456 | 31.1446200157 | 164 | 504990 | -90.54 | 15.73 | 421.35 | 0.07 | 2.02 | 1585 |
| 2024-09-20 22:21:41.297 | MS1 | 121.4656639913 | 31.1446205581 | 164 | 504990 | -87.67 | 17.63 | 582.59 | 0.06 | 2.76 | 1592 |
| 2024-09-20 22:21:42.113 | MS1 | 121.4656714395 | 31.1446312699 | 164 | 504990 | -92.78 | 13.48 | 424.04 | 0.01 | 2.80 | 1563 |

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
| 3241682 | 2 | 121.4712213981 | 31.1461452131 | 227 | 0 | 3 | 18.5 | TDD | 818 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3243064 | 1 | 121.4729478006 | 31.1463576397 | 292 | 2 | 1 | 42.5 | TDD | 857 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3246883 | 3 | 121.4679489231 | 31.1513808005 | 123 | 7 | 10 | 46.3 | TDD | 164 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3265274 | 4 | 121.4742923607 | 31.1506930750 | 181 | 14 | 7 | 40.0 | TDD | 884 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.248 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.273 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.381 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.381 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.645 | NREventA2 | measId:1;ServCellPCI:223;Se... |
| 2024-09-20 22:21:34.781 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243064 | 1 | 19.1049 | 7.7922 | -115.1468 | 15.5125 | 116.2420 | 0.0133 | 0.0163 |
| 2024_09_20 22:00 | 3241682 | 2 | 14.3069 | 13.6047 | -115.0053 | 6.0351 | 142.2330 | 0.0020 | 0.0133 |
| 2024_09_20 22:00 | 3246883 | 3 | 18.5649 | 18.0762 | -117.5686 | 12.5267 | 110.8676 | 0.1113 | 0.0114 |
| 2024_09_20 22:00 | 3265274 | 4 | 8.7213 | 16.6813 | -114.1217 | 8.8757 | 192.7621 | 0.0017 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415771_473EA89A | 504990 | 164 | -107.2 | 504990 | 857 | -114.5 | 504990 | 818 | -118.8 | 504990 | 884 |
| MR_1774415771_030C0893 | 504990 | 164 | -110.1 | 504990 | 857 | -116.0 | 504990 | 818 | -120.1 | 504990 | 884 |
| MR_1774415771_94BC9AB7 | 504990 | 164 | -108.5 | 504990 | 857 | -115.6 | 504990 | 818 | -119.8 | 504990 | 884 |
| MR_1774415771_1CA2E478 | 504990 | 164 | -109.5 | 504990 | 857 | -114.4 | 504990 | 818 | -119.7 | 504990 | 884 |
| MR_1774415771_CEA66CC2 | 504990 | 164 | -107.0 | 504990 | 857 | -113.0 | 504990 | 818 | -120.8 | 504990 | 884 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1545: `5030830a-90d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5030830a-90d0-4132-8a43-b8d937212139` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease A3 Offset threshold for 3243086_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1545] topology](images/train_1545.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3243086_1 by 10 degrees
- `C2`: Press down the tilt angle  of 3225463_4 by 9 degrees
- `C3`: Decrease transmission power for 3225463_4
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Check test server and transmission issues
- `C6`: Increase A3 Offset threshold for 3225463_4
- `C7`: Add neighbor relationship between 3243086_1 and 3225463_4
- `C8`: Increase transmission power for 3225463_4
- `C9`: Decrease A3 Offset threshold for 3243086_1 **← 정답**
- `C10`: Increase transmission power for 3243086_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225463_4
- `C12`: Decrease A3 Offset threshold for 3225463_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225463_4
- `C14`: Decrease transmission power for 3243086_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243086_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243086_1
- `C17`: Add neighbor relationship between 3268057_3 and 3225463_4
- `C18`: Lift the tilt angle  of 3225463_4 by 9 degrees
- `C19`: Adjust the azimuth of 3243086_1 by 50 degrees
- `C20`: Adjust the azimuth of 3225463_4 by 50 degrees
- `C21`: Increase A3 Offset threshold for 3243086_1
- `C22`: Press down the tilt angle of 3243086_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.777 | MS1 | 121.4656730731 | 31.1446377085 | 980 | 504990 | -77.97 | 15.39 | 349.57 | 0.02 | 2.75 | 1573 |
| 2024-09-20 22:21:32.418 | MS1 | 121.4656602324 | 31.1446288894 | 980 | 504990 | -82.55 | 12.48 | 422.88 | 0.05 | 2.88 | 1582 |
| 2024-09-20 22:21:33.928 | MS1 | 121.4656633835 | 31.1446191202 | 980 | 504990 | -80.01 | 14.03 | 579.98 | 0.03 | 2.44 | 1572 |
| 2024-09-20 22:21:34.868 | MS1 | 121.4656686135 | 31.1446206966 | 980 | 504990 | -84.35 | -0.31 | 55.31 | 0.05 | 1.20 | 1599 |
| 2024-09-20 22:21:35.331 | MS1 | 121.4656712907 | 31.1446335768 | 980 | 504990 | -86.85 | -1.42 | 52.40 | 0.20 | 1.25 | 1571 |
| 2024-09-20 22:21:36.161 | MS1 | 121.4656779097 | 31.1446351062 | 980 | 504990 | -90.26 | -0.75 | 51.44 | 0.01 | 1.37 | 1580 |
| 2024-09-20 22:21:37.411 | MS1 | 121.4656764587 | 31.1446277696 | 980 | 504990 | -90.13 | -2.07 | 64.84 | 0.12 | 1.49 | 1591 |
| 2024-09-20 22:21:38.794 | MS1 | 121.4656648066 | 31.1446223127 | 980 | 504990 | -92.08 | -0.92 | 36.54 | 0.03 | 1.03 | 1594 |
| 2024-09-20 22:21:39.590 | MS1 | 121.4656703000 | 31.1446255052 | 222 | 504990 | -75.24 | 14.51 | 189.96 | 0.03 | 1.15 | 1591 |
| 2024-09-20 22:21:40.432 | MS1 | 121.4656584187 | 31.1446356108 | 222 | 504990 | -78.47 | 17.72 | 543.56 | 0.13 | 2.42 | 1561 |
| 2024-09-20 22:21:41.888 | MS1 | 121.4656774978 | 31.1446276098 | 222 | 504990 | -75.52 | 14.94 | 338.03 | 0.08 | 2.61 | 1586 |
| 2024-09-20 22:21:42.639 | MS1 | 121.4656763969 | 31.1446317944 | 222 | 504990 | -75.67 | 16.60 | 559.83 | 0.05 | 2.55 | 1593 |

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
| 3225463 | 4 | 121.4698876415 | 31.1509520437 | 105 | 7 | 8 | 22.4 | TDD | 222 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3232342 | 2 | 121.4722424004 | 31.1457534464 | 310 | 12 | 1 | 37.1 | TDD | 267 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3243086 | 1 | 121.4725816404 | 31.1509652992 | 329 | 13 | 3 | 40.5 | TDD | 980 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3268057 | 3 | 121.4684418970 | 31.1445893447 | 281 | 13 | 2 | 27.8 | TDD | 924 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.582 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.605 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.711 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.711 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.467 | NREventA3 | measId:2;ServCellPCI:241;Se... |
| 2024-09-20 22:21:38.707 | NRHandoverAttempt | SourcePCI:241;SourceNR-ARFC... |
| 2024-09-20 22:21:38.749 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.763 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.873 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.873 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243086 | 1 | 16.0683 | 5.7234 | -117.8417 | 7.9731 | 109.3629 | 0.0166 | 0.1515 |
| 2024_09_20 22:00 | 3232342 | 2 | 12.3744 | 12.9562 | -117.1975 | 7.9465 | 85.0991 | 0.0065 | 0.0033 |
| 2024_09_20 22:00 | 3268057 | 3 | 17.4460 | 9.9396 | -116.9699 | 12.6954 | 142.3032 | 0.0170 | 0.0086 |
| 2024_09_20 22:00 | 3225463 | 4 | 14.8629 | 10.2588 | -114.8855 | 9.8095 | 81.6089 | 0.0137 | 0.0141 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416790_76099B6E | 504990 | 222 | -80.5 | 504990 | 980 | -84.0 | 504990 | 924 | -81.5 | 504990 | 267 |
| MR_1774416790_EAA6BFC7 | 504990 | 980 | -82.7 | 504990 | 222 | -78.3 | 504990 | 924 | -80.6 | 504990 | 267 |
| MR_1774416790_8F55701E | 504990 | 980 | -84.2 | 504990 | 222 | -79.5 | 504990 | 924 | -82.8 | 504990 | 267 |
| MR_1774416790_4260DA12 | 504990 | 222 | -77.8 | 504990 | 980 | -85.9 | 504990 | 924 | -80.6 | 504990 | 267 |
| MR_1774416790_7BDA574E | 504990 | 222 | -81.2 | 504990 | 980 | -85.5 | 504990 | 924 | -82.5 | 504990 | 267 |
| MR_1774416790_1DF3FBF1 | 504990 | 980 | -86.3 | 504990 | 222 | -81.2 | 504990 | 924 | -82.1 | 504990 | 267 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1546: `ad8f13b9-cc3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ad8f13b9-cc34-4ff2-8661-f258491e8c61` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1546] topology](images/train_1546.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3224199_4 by 2 degrees
- `C2`: Decrease transmission power for 3224199_4
- `C3`: Add neighbor relationship between 3235266_2 and 3224199_4
- `C4`: Lift the tilt angle of 3235266_2 by 10 degrees
- `C5`: Insufficient data; more data is needed for judgment. **← 정답**
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235266_2
- `C7`: Decrease A3 Offset threshold for 3224199_4
- `C8`: Press down the tilt angle of 3235266_2 by 10 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224199_4
- `C10`: Adjust the azimuth of 3235266_2 by 50 degrees
- `C11`: Increase A3 Offset threshold for 3224199_4
- `C12`: Adjust the azimuth of 3224199_4 by 18 degrees
- `C13`: Increase transmission power for 3224199_4
- `C14`: Increase A3 Offset threshold for 3235266_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224199_4
- `C16`: Increase transmission power for 3235266_2
- `C17`: Add neighbor relationship between 3243519_1 and 3224199_4
- `C18`: Press down the tilt angle  of 3224199_4 by 2 degrees
- `C19`: Check test server and transmission issues
- `C20`: Decrease transmission power for 3235266_2
- `C21`: Decrease A3 Offset threshold for 3235266_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235266_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.517 | MS1 | 121.4656682413 | 31.1446251293 | 110 | 504990 | -85.17 | 13.52 | 303.95 | 0.17 | 2.93 | 1581 |
| 2024-09-20 22:21:32.499 | MS1 | 121.4656773584 | 31.1446265262 | 110 | 504990 | -91.64 | 15.94 | 420.01 | 0.15 | 2.61 | 1572 |
| 2024-09-20 22:21:33.575 | MS1 | 121.4656677173 | 31.1446241091 | 110 | 504990 | -85.58 | 13.35 | 480.93 | 0.11 | 2.69 | 1562 |
| 2024-09-20 22:21:34.461 | MS1 | 121.4656681552 | 31.1446353615 | 110 | 504990 | -85.11 | 17.32 | 96.21 | 0.02 | 2.90 | 1595 |
| 2024-09-20 22:21:35.549 | MS1 | 121.4656732999 | 31.1446261388 | 110 | 504990 | -85.24 | 16.51 | 74.15 | 0.07 | 2.55 | 1587 |
| 2024-09-20 22:21:36.650 | MS1 | 121.4656687443 | 31.1446256872 | 110 | 504990 | -88.22 | 16.19 | 98.57 | 0.01 | 2.42 | 1573 |
| 2024-09-20 22:21:37.666 | MS1 | 121.4656710772 | 31.1446181865 | 110 | 504990 | -90.00 | 9.58 | 73.77 | 0.07 | 2.53 | 1592 |
| 2024-09-20 22:21:38.332 | MS1 | 121.4656648097 | 31.1446338537 | 110 | 504990 | -91.39 | 12.78 | 53.55 | 0.01 | 2.14 | 1574 |
| 2024-09-20 22:21:39.177 | MS1 | 121.4656639750 | 31.1446368445 | 110 | 504990 | -93.57 | 10.59 | 56.00 | 0.16 | 2.95 | 1565 |
| 2024-09-20 22:21:40.730 | MS1 | 121.4656695543 | 31.1446256578 | 110 | 504990 | -89.60 | 11.52 | 356.74 | 0.16 | 2.11 | 1581 |
| 2024-09-20 22:21:41.374 | MS1 | 121.4656769327 | 31.1446229804 | 110 | 504990 | -89.61 | 9.98 | 414.88 | 0.02 | 2.09 | 1569 |
| 2024-09-20 22:21:42.165 | MS1 | 121.4656688059 | 31.1446260756 | 110 | 504990 | -90.06 | 11.02 | 557.88 | 0.16 | 2.65 | 1580 |

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
| 3224199 | 4 | 121.4690409834 | 31.1542033818 | 179 | 0 | 11 | 30.4 | TDD | 398 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3235266 | 2 | 121.4703662952 | 31.1494638280 | 316 | 9 | 3 | 42.9 | TDD | 110 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3243519 | 1 | 121.4703805628 | 31.1480985662 | 181 | 15 | 5 | 47.4 | TDD | 57 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3265180 | 3 | 121.4641567006 | 31.1462481704 | 8 | 7 | 2 | 39.5 | TDD | 164 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.582 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.602 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.718 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.718 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.419 | NREventA3 | measId:2;ServCellPCI:905;Se... |
| 2024-09-20 22:21:38.659 | NRHandoverAttempt | SourcePCI:905;SourceNR-ARFC... |
| 2024-09-20 22:21:38.689 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.700 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.819 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.819 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3243519 | 1 | 76.2278 | 78.1323 | -117.1715 | 19.1008 | 161.6560 | 0.0193 | 0.0176 |
| 2024_09_19 22:00 | 3235266 | 2 | 78.8121 | 78.0710 | -115.0667 | 5.8506 | 163.0783 | 0.0004 | 0.0143 |
| 2024_09_19 22:00 | 3265180 | 3 | 79.7771 | 92.9920 | -114.5930 | 18.2536 | 110.4698 | 0.0173 | 0.0163 |
| 2024_09_19 22:00 | 3224199 | 4 | 78.8955 | 78.3709 | -114.0485 | 5.5745 | 89.1977 | 0.0192 | 0.0136 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412744_B26DEA1A | 504990 | 110 | -84.6 | 504990 | 398 | -90.4 | 504990 | 57 | -95.1 | 504990 | 164 |
| MR_1774412744_C731ECA7 | 504990 | 110 | -83.8 | 504990 | 398 | -89.9 | 504990 | 57 | -92.8 | 504990 | 164 |
| MR_1774412744_313BB00C | 504990 | 110 | -87.1 | 504990 | 398 | -88.4 | 504990 | 57 | -92.4 | 504990 | 164 |
| MR_1774412744_FE7A9A3A | 504990 | 110 | -84.8 | 504990 | 398 | -87.0 | 504990 | 57 | -92.9 | 504990 | 164 |
| MR_1774412744_46A6F916 | 504990 | 110 | -84.3 | 504990 | 398 | -89.7 | 504990 | 57 | -93.2 | 504990 | 164 |
| MR_1774412744_38B3C2B0 | 504990 | 110 | -83.1 | 504990 | 398 | -88.0 | 504990 | 57 | -92.4 | 504990 | 164 |
| MR_1774412744_6CDDA8BF | 504990 | 110 | -84.2 | 504990 | 398 | -88.6 | 504990 | 57 | -93.1 | 504990 | 164 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1547: `7fe88618-894...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7fe88618-894f-4f30-ae8b-341ad44a9f6a` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1547] topology](images/train_1547.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3258626_1 by 19 degrees
- `C2`: Add neighbor relationship between 3251803_3 and 3258626_1
- `C3`: Increase A3 Offset threshold for 3258626_1
- `C4`: Increase A3 Offset threshold for 3248733_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258626_1
- `C6`: Press down the tilt angle  of 3258626_1 by 6 degrees
- `C7`: Lift the tilt angle of 3248733_4 by 10 degrees
- `C8`: Add neighbor relationship between 3248733_4 and 3258626_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248733_4
- `C10`: Increase transmission power for 3258626_1
- `C11`: Decrease A3 Offset threshold for 3248733_4
- `C12`: Adjust the azimuth of 3248733_4 by 50 degrees
- `C13`: Press down the tilt angle of 3248733_4 by 10 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248733_4
- `C15`: Insufficient data; more data is needed for judgment. **← 정답**
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258626_1
- `C17`: Decrease transmission power for 3258626_1
- `C18`: Check test server and transmission issues
- `C19`: Decrease transmission power for 3248733_4
- `C20`: Increase transmission power for 3248733_4
- `C21`: Decrease A3 Offset threshold for 3258626_1
- `C22`: Lift the tilt angle  of 3258626_1 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.854 | MS1 | 121.4656687823 | 31.1446298528 | 679 | 504990 | -85.84 | 12.28 | 582.05 | 0.17 | 2.18 | 1576 |
| 2024-09-20 22:21:32.473 | MS1 | 121.4656615054 | 31.1446313846 | 679 | 504990 | -85.17 | 14.01 | 380.03 | 0.04 | 2.22 | 1599 |
| 2024-09-20 22:21:33.129 | MS1 | 121.4656683995 | 31.1446181166 | 679 | 504990 | -91.99 | 16.90 | 519.75 | 0.09 | 2.78 | 1571 |
| 2024-09-20 22:21:34.431 | MS1 | 121.4656635366 | 31.1446251854 | 679 | 504990 | -88.43 | 14.00 | 86.86 | 0.13 | 2.05 | 1578 |
| 2024-09-20 22:21:35.979 | MS1 | 121.4656742162 | 31.1446208941 | 679 | 504990 | -87.80 | 17.91 | 91.87 | 0.19 | 2.83 | 1568 |
| 2024-09-20 22:21:36.303 | MS1 | 121.4656696201 | 31.1446200743 | 679 | 504990 | -86.32 | 17.14 | 65.83 | 0.17 | 2.31 | 1572 |
| 2024-09-20 22:21:37.407 | MS1 | 121.4656638653 | 31.1446346177 | 679 | 504990 | -93.89 | 9.61 | 78.60 | 0.00 | 2.22 | 1595 |
| 2024-09-20 22:21:38.441 | MS1 | 121.4656753380 | 31.1446328677 | 679 | 504990 | -90.48 | 10.65 | 91.68 | 0.07 | 2.79 | 1568 |
| 2024-09-20 22:21:39.245 | MS1 | 121.4656746028 | 31.1446187988 | 679 | 504990 | -90.24 | 7.43 | 57.34 | 0.17 | 2.67 | 1565 |
| 2024-09-20 22:21:40.184 | MS1 | 121.4656670344 | 31.1446295285 | 679 | 504990 | -93.06 | 7.05 | 566.22 | 0.14 | 2.20 | 1576 |
| 2024-09-20 22:21:41.261 | MS1 | 121.4656710500 | 31.1446316193 | 679 | 504990 | -92.50 | 12.46 | 568.03 | 0.16 | 2.60 | 1567 |
| 2024-09-20 22:21:42.390 | MS1 | 121.4656645797 | 31.1446339267 | 679 | 504990 | -90.14 | 10.09 | 604.05 | 0.15 | 2.74 | 1566 |

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
| 3241770 | 2 | 121.4742715747 | 31.1531889428 | 42 | 14 | 12 | 26.6 | TDD | 675 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3248733 | 4 | 121.4683280726 | 31.1462853689 | 2 | 13 | 10 | 19.7 | TDD | 679 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3251803 | 3 | 121.4703559170 | 31.1544986566 | 341 | 3 | 7 | 25.8 | TDD | 172 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3258626 | 1 | 121.4744340885 | 31.1548583409 | 235 | 5 | 12 | 24.5 | TDD | 656 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.901 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.023 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.023 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.710 | NREventA3 | measId:2;ServCellPCI:294;Se... |
| 2024-09-20 22:21:37.950 | NRHandoverAttempt | SourcePCI:294;SourceNR-ARFC... |
| 2024-09-20 22:21:37.998 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.011 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.126 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.126 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3258626 | 1 | 76.2153 | 90.8034 | -115.0031 | 6.3850 | 145.1184 | 0.0115 | 0.0169 |
| 2024_09_19 22:00 | 3241770 | 2 | 85.0763 | 90.7934 | -114.1474 | 6.9242 | 82.6756 | 0.0148 | 0.0141 |
| 2024_09_19 22:00 | 3251803 | 3 | 83.4709 | 84.0368 | -116.0509 | 16.3280 | 184.8394 | 0.0176 | 0.0197 |
| 2024_09_19 22:00 | 3248733 | 4 | 92.0012 | 79.7260 | -114.7491 | 16.8969 | 196.0049 | 0.0030 | 0.0144 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414695_443C115E | 504990 | 679 | -87.7 | 504990 | 656 | -89.8 | 504990 | 172 | -98.1 | 504990 | 675 |
| MR_1774414695_8AFCA6EA | 504990 | 679 | -89.4 | 504990 | 656 | -90.1 | 504990 | 172 | -100.3 | 504990 | 675 |
| MR_1774414695_30B00CD0 | 504990 | 679 | -88.6 | 504990 | 656 | -86.8 | 504990 | 172 | -97.3 | 504990 | 675 |
| MR_1774414695_98307B16 | 504990 | 679 | -88.9 | 504990 | 656 | -89.5 | 504990 | 172 | -99.1 | 504990 | 675 |
| MR_1774414695_06A2241C | 504990 | 679 | -89.8 | 504990 | 656 | -88.6 | 504990 | 172 | -98.4 | 504990 | 675 |
| MR_1774414695_A24C7B3E | 504990 | 679 | -86.8 | 504990 | 656 | -88.0 | 504990 | 172 | -97.6 | 504990 | 675 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1548: `30694f84-507...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `30694f84-5075-4ba6-99ef-f1aceec795e0` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224526_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1548] topology](images/train_1548.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224526_1
- `C2`: Press down the tilt angle of 3224526_1 by 3 degrees
- `C3`: Decrease A3 Offset threshold for 3224526_1
- `C4`: Lift the tilt angle  of 3239877_4 by 2 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Add neighbor relationship between 3255421_7 and 3239877_4
- `C7`: Add neighbor relationship between 3224526_1 and 3239877_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239877_4
- `C9`: Increase A3 Offset threshold for 3239877_4
- `C10`: Increase A3 Offset threshold for 3224526_1
- `C11`: Decrease transmission power for 3224526_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224526_1 **← 정답**
- `C13`: Press down the tilt angle  of 3239877_4 by 2 degrees
- `C14`: Adjust the azimuth of 3239877_4 by 38 degrees
- `C15`: Check test server and transmission issues
- `C16`: Adjust the azimuth of 3224526_1 by 47 degrees
- `C17`: Decrease A3 Offset threshold for 3239877_4
- `C18`: Increase transmission power for 3224526_1
- `C19`: Increase transmission power for 3239877_4
- `C20`: Decrease transmission power for 3239877_4
- `C21`: Lift the tilt angle of 3224526_1 by 3 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239877_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.850 | MS1 | 121.4656661250 | 31.1446336462 | 71 | 504990 | -95.82 | 13.23 | 491.65 | 0.17 | 2.36 | 1595 |
| 2024-09-20 22:21:32.233 | MS1 | 121.4656731165 | 31.1446193680 | 24 | 504990 | -94.86 | 13.58 | 334.46 | 0.13 | 2.23 | 1578 |
| 2024-09-20 22:21:33.820 | MS1 | 121.4656769118 | 31.1446378564 | 782 | 504990 | -95.25 | 10.06 | 490.59 | 0.11 | 2.92 | 1570 |
| 2024-09-20 22:21:34.328 | MS1 | 121.4656715571 | 31.1446194217 | 951 | 152650 | -94.36 | 4.70 | 100.66 | 0.07 | 1.54 | 992 |
| 2024-09-20 22:21:35.570 | MS1 | 121.4656648938 | 31.1446280413 | 202 | 152650 | -96.32 | 2.69 | 64.77 | 0.03 | 1.88 | 956 |
| 2024-09-20 22:21:36.999 | MS1 | 121.4656601578 | 31.1446271297 | 162 | 152650 | -90.35 | 4.13 | 93.12 | 0.20 | 1.83 | 983 |
| 2024-09-20 22:21:37.312 | MS1 | 121.4656611126 | 31.1446287423 | 137 | 152650 | -93.97 | 3.43 | 66.20 | 0.18 | 1.66 | 926 |
| 2024-09-20 22:21:38.478 | MS1 | 121.4656765205 | 31.1446376472 | 951 | 152650 | -96.22 | 6.59 | 83.75 | 0.15 | 1.91 | 914 |
| 2024-09-20 22:21:39.856 | MS1 | 121.4656612837 | 31.1446285639 | 202 | 152650 | -87.14 | 4.96 | 99.20 | 0.11 | 1.78 | 947 |
| 2024-09-20 22:21:40.382 | MS1 | 121.4656606773 | 31.1446339675 | 162 | 152650 | -96.83 | 6.80 | 80.47 | 0.12 | 2.30 | 1597 |
| 2024-09-20 22:21:41.927 | MS1 | 121.4656651726 | 31.1446274651 | 137 | 152650 | -94.65 | 6.25 | 75.14 | 0.19 | 2.36 | 1589 |
| 2024-09-20 22:21:42.924 | MS1 | 121.4656707632 | 31.1446314881 | 951 | 152650 | -90.94 | 4.18 | 56.70 | 0.09 | 2.01 | 1592 |

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
| 3220505 | 5 | 121.4706337468 | 31.1465185198 | 62 | 6 | 1 | 4.1 | TDD | 24 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3220697 | 11 | 121.4658122633 | 31.1446063704 | 80 | 15 | 3 | 21.6 | FDD | 779 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3223389 | 13 | 121.4702406212 | 31.1548549132 | 262 | 8 | 5 | 20.5 | FDD | 951 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3224526 | 1 | 121.4641179203 | 31.1525011161 | 217 | 2 | 10 | 12.9 | TDD | 71 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3228683 | 3 | 121.4702017554 | 31.1447558562 | 34 | 10 | 1 | 18.5 | TDD | 782 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3231224 | 9 | 121.4656495943 | 31.1557083113 | 283 | 7 | 9 | 0.9 | FDD | 137 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3235670 | 2 | 121.4721543837 | 31.1476865891 | 339 | 0 | 0 | 2.1 | TDD | 556 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3239877 | 4 | 121.4730263194 | 31.1463285006 | 293 | 0 | 4 | 21.6 | TDD | 147 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3255090 | 6 | 121.4713066320 | 31.1498062982 | 53 | 4 | 5 | 5.7 | TDD | 477 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3255421 | 7 | 121.4723308908 | 31.1457065993 | 142 | 14 | 4 | 22.5 | FDD | 162 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3256123 | 8 | 121.4652016003 | 31.1441379052 | 192 | 8 | 10 | 28.6 | FDD | 711 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3269340 | 12 | 121.4666506606 | 31.1524947176 | 64 | 9 | 10 | 16.5 | FDD | 686 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3278754 | 10 | 121.4658789087 | 31.1460404876 | 92 | 1 | 0 | 11.6 | FDD | 202 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |

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
| 2024-09-20 22:21:31.189 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.208 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.350 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.350 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.036 | NREventA2 | measId:1;ServCellPCI:488;Se... |
| 2024-09-20 22:21:35.182 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.451 | NREventA5 | measId:3;ServCellPCI:488;Se... |
| 2024-09-20 22:21:35.518 | NRHandoverAttempt | SourcePCI:488;SourceNR-ARFC... |
| 2024-09-20 22:21:35.542 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.557 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.686 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.686 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224526 | 1 | 11.4644 | 11.0089 | -114.9191 | 10.4668 | 117.1855 | 0.0155 | 0.0096 |
| 2024_09_20 22:00 | 3235670 | 2 | 8.0536 | 17.3307 | -116.9239 | 17.6807 | 168.8815 | 0.0125 | 0.0115 |
| 2024_09_20 22:00 | 3228683 | 3 | 18.7577 | 5.9403 | -115.2151 | 5.6295 | 138.9283 | 0.0014 | 0.0175 |
| 2024_09_20 22:00 | 3239877 | 4 | 5.4750 | 6.0552 | -116.7014 | 17.0019 | 83.8958 | 0.0164 | 0.0032 |
| 2024_09_20 22:00 | 3220505 | 5 | 8.8644 | 13.6344 | -116.2229 | 13.7675 | 187.8471 | 0.0152 | 0.0178 |
| 2024_09_20 22:00 | 3255090 | 6 | 10.5832 | 16.8699 | -114.9205 | 11.5863 | 162.1390 | 0.0105 | 0.0175 |
| 2024_09_20 22:00 | 3255421 | 7 | 10.6260 | 17.1001 | -116.0249 | 4.1985 | 22.7615 | 0.0058 | 0.0007 |
| 2024_09_20 22:00 | 3256123 | 8 | 11.6232 | 14.1099 | -115.8720 | 4.3181 | 55.7544 | 0.0059 | 0.0067 |
| 2024_09_20 22:00 | 3231224 | 9 | 14.5573 | 6.4486 | -116.4691 | 4.3919 | 34.6469 | 0.0162 | 0.0132 |
| 2024_09_20 22:00 | 3278754 | 10 | 18.8835 | 18.7882 | -117.3878 | 3.6454 | 34.8428 | 0.0109 | 0.0018 |
| 2024_09_20 22:00 | 3220697 | 11 | 9.3208 | 7.3203 | -117.4936 | 4.8902 | 22.6624 | 0.0046 | 0.0187 |
| 2024_09_20 22:00 | 3269340 | 12 | 13.4649 | 10.8033 | -114.6996 | 4.5990 | 23.3321 | 0.0118 | 0.0024 |
| 2024_09_20 22:00 | 3223389 | 13 | 11.3180 | 6.1439 | -114.0993 | 3.4525 | 40.4382 | 0.0135 | 0.0046 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416042_5BFE1C39 | 152650 | 202 | -97.7 | 152650 | 686 | -99.2 | 152650 | 711 | -108.0 | 152650 | 779 |
| MR_1774416042_B9DF4D46 | 152650 | 202 | -97.8 | 152650 | 686 | -102.6 | 152650 | 711 | -106.7 | 152650 | 779 |
| MR_1774416042_36B9E981 | 504990 | 782 | -93.9 | 504990 | 147 | -96.8 | 504990 | 556 | -100.9 | 504990 | 477 |
| MR_1774416042_3E1F6697 | 504990 | 782 | -94.3 | 504990 | 147 | -96.1 | 504990 | 556 | -100.2 | 504990 | 477 |
| MR_1774416042_CDE0B47F | 152650 | 202 | -95.6 | 152650 | 686 | -101.3 | 152650 | 711 | -108.8 | 152650 | 779 |
| MR_1774416042_5B89F924 | 152650 | 202 | -96.2 | 152650 | 686 | -102.9 | 152650 | 711 | -108.8 | 152650 | 779 |
| MR_1774416042_FDC2E83A | 504990 | 782 | -95.7 | 504990 | 147 | -94.1 | 504990 | 556 | -98.6 | 504990 | 477 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1549: `ba7e9076-7ef...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ba7e9076-7efe-4e64-89ca-f3c756fef62b` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1549] topology](images/train_1549.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3278515_1
- `C2`: Add neighbor relationship between 3229596_4 and 3278515_1
- `C3`: Decrease transmission power for 3256863_3
- `C4`: Press down the tilt angle of 3256863_3 by 10 degrees
- `C5`: Lift the tilt angle  of 3278515_1 by 7 degrees
- `C6`: Check test server and transmission issues
- `C7`: Decrease transmission power for 3278515_1
- `C8`: Increase transmission power for 3256863_3
- `C9`: Press down the tilt angle  of 3278515_1 by 7 degrees
- `C10`: Decrease A3 Offset threshold for 3256863_3
- `C11`: Increase A3 Offset threshold for 3256863_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256863_3
- `C13`: Increase transmission power for 3278515_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278515_1
- `C15`: Adjust the azimuth of 3256863_3 by 23 degrees
- `C16`: Adjust the azimuth of 3278515_1 by 50 degrees
- `C17`: Add neighbor relationship between 3256863_3 and 3278515_1
- `C18`: Insufficient data; more data is needed for judgment. **← 정답**
- `C19`: Lift the tilt angle of 3256863_3 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3278515_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256863_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278515_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.889 | MS1 | 121.4656711170 | 31.1446270861 | 725 | 504990 | -90.22 | 13.69 | 541.87 | 0.09 | 2.75 | 1576 |
| 2024-09-20 22:21:32.822 | MS1 | 121.4656720416 | 31.1446215403 | 725 | 504990 | -89.57 | 16.06 | 418.82 | 0.07 | 2.84 | 1590 |
| 2024-09-20 22:21:33.497 | MS1 | 121.4656683095 | 31.1446372646 | 725 | 504990 | -87.50 | 12.06 | 412.70 | 0.18 | 2.57 | 1569 |
| 2024-09-20 22:21:34.941 | MS1 | 121.4656689022 | 31.1446184602 | 725 | 504990 | -86.81 | 14.15 | 63.82 | 0.17 | 2.23 | 1598 |
| 2024-09-20 22:21:35.679 | MS1 | 121.4656604224 | 31.1446223751 | 725 | 504990 | -88.32 | 14.57 | 104.26 | 0.01 | 2.73 | 1583 |
| 2024-09-20 22:21:36.792 | MS1 | 121.4656719878 | 31.1446231369 | 725 | 504990 | -91.70 | 16.91 | 78.11 | 0.14 | 2.16 | 1566 |
| 2024-09-20 22:21:37.994 | MS1 | 121.4656580176 | 31.1446232832 | 725 | 504990 | -90.53 | 9.36 | 81.83 | 0.01 | 2.02 | 1593 |
| 2024-09-20 22:21:38.526 | MS1 | 121.4656740396 | 31.1446341894 | 725 | 504990 | -89.29 | 10.31 | 89.72 | 0.05 | 2.22 | 1593 |
| 2024-09-20 22:21:39.501 | MS1 | 121.4656606497 | 31.1446253049 | 725 | 504990 | -91.90 | 7.85 | 51.19 | 0.12 | 2.89 | 1567 |
| 2024-09-20 22:21:40.249 | MS1 | 121.4656603795 | 31.1446285288 | 725 | 504990 | -90.01 | 8.74 | 547.07 | 0.02 | 2.86 | 1572 |
| 2024-09-20 22:21:41.695 | MS1 | 121.4656612436 | 31.1446346359 | 725 | 504990 | -91.28 | 9.55 | 376.30 | 0.10 | 2.05 | 1564 |
| 2024-09-20 22:21:42.545 | MS1 | 121.4656676973 | 31.1446355980 | 725 | 504990 | -90.57 | 12.51 | 392.09 | 0.07 | 2.16 | 1587 |

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
| 3229596 | 4 | 121.4739368042 | 31.1534856846 | 12 | 14 | 7 | 45.0 | TDD | 189 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3256863 | 3 | 121.4726095025 | 31.1531647417 | 192 | 15 | 3 | 39.7 | TDD | 725 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3264121 | 2 | 121.4709429067 | 31.1469998840 | 114 | 13 | 10 | 34.0 | TDD | 332 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3278515 | 1 | 121.4702652908 | 31.1540492873 | 319 | 5 | 5 | 42.3 | TDD | 137 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.797 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.817 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.931 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.931 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.636 | NREventA3 | measId:2;ServCellPCI:611;Se... |
| 2024-09-20 22:21:37.876 | NRHandoverAttempt | SourcePCI:611;SourceNR-ARFC... |
| 2024-09-20 22:21:37.910 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.921 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.036 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.036 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3278515 | 1 | 78.3591 | 81.2439 | -116.7005 | 10.8262 | 85.8207 | 0.0158 | 0.0113 |
| 2024_09_19 22:00 | 3264121 | 2 | 78.7423 | 79.4969 | -116.0784 | 9.1604 | 81.2565 | 0.0196 | 0.0010 |
| 2024_09_19 22:00 | 3256863 | 3 | 93.0584 | 75.0634 | -117.8519 | 8.6533 | 141.4689 | 0.0030 | 0.0125 |
| 2024_09_19 22:00 | 3229596 | 4 | 90.5267 | 80.2454 | -114.1692 | 8.7705 | 171.5628 | 0.0139 | 0.0014 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415434_9E406EB5 | 504990 | 725 | -86.0 | 504990 | 137 | -89.9 | 504990 | 189 | -94.1 | 504990 | 332 |
| MR_1774415434_CF803164 | 504990 | 725 | -88.4 | 504990 | 137 | -91.7 | 504990 | 189 | -96.3 | 504990 | 332 |
| MR_1774415434_FACFE28C | 504990 | 725 | -88.1 | 504990 | 137 | -91.7 | 504990 | 189 | -92.8 | 504990 | 332 |
| MR_1774415434_52945437 | 504990 | 725 | -87.4 | 504990 | 137 | -88.6 | 504990 | 189 | -96.6 | 504990 | 332 |
| MR_1774415434_9899011A | 504990 | 725 | -85.1 | 504990 | 137 | -88.9 | 504990 | 189 | -95.2 | 504990 | 332 |
| MR_1774415434_21AFDCF7 | 504990 | 725 | -88.4 | 504990 | 137 | -90.0 | 504990 | 189 | -96.5 | 504990 | 332 |

> *... 2개 열 생략 (전체 14열)*

---
