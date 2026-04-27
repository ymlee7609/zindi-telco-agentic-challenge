# Track A 문제 분석 — train[440]~train[449]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[440] ~ train[449] (10개)

## 목차

1. [문제 440: `74d9c32e-20c...`](#440) — single-answer, 정답: C16
2. [문제 441: `b03091a9-dee...`](#441) — single-answer, 정답: C17
3. [문제 442: `18a246d5-058...`](#442) — single-answer, 정답: C1
4. [문제 443: `30fc74c5-e2b...`](#443) — single-answer, 정답: C2
5. [문제 444: `efb96657-c8a...`](#444) — single-answer, 정답: C7
6. [문제 445: `0739c14e-bec...`](#445) — multiple-answer, 정답: C7|C9|C15|C19
7. [문제 446: `48a74824-fef...`](#446) — single-answer, 정답: C19
8. [문제 447: `f53ae612-73f...`](#447) — single-answer, 정답: C14
9. [문제 448: `faaa7fd2-987...`](#448) — single-answer, 정답: C16
10. [문제 449: `a038c634-fe2...`](#449) — single-answer, 정답: C6

---

### 문제 440: `74d9c32e-20c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `74d9c32e-20cb-4815-bc47-0047664f94b8` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3236776_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[440] topology](images/train_0440.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3236776_1
- `C2`: Add neighbor relationship between 3236776_1 and 3233356_3
- `C3`: Decrease A3 Offset threshold for 3236776_1
- `C4`: Decrease transmission power for 3233356_3
- `C5`: Increase A3 Offset threshold for 3233356_3
- `C6`: Lift the tilt angle  of 3233356_3 by 6 degrees
- `C7`: Lift the tilt angle of 3236776_1 by 5 degrees
- `C8`: Increase transmission power for 3233356_3
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Check test server and transmission issues
- `C11`: Add neighbor relationship between 3234237_2 and 3233356_3
- `C12`: Adjust the azimuth of 3236776_1 by 47 degrees
- `C13`: Decrease transmission power for 3236776_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233356_3
- `C15`: Adjust the azimuth of 3233356_3 by 50 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236776_1 **← 정답**
- `C17`: Increase A3 Offset threshold for 3236776_1
- `C18`: Press down the tilt angle of 3236776_1 by 5 degrees
- `C19`: Press down the tilt angle  of 3233356_3 by 6 degrees
- `C20`: Decrease A3 Offset threshold for 3233356_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233356_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236776_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.208 | MS1 | 121.4656619658 | 31.1446313439 | 50 | 504990 | -88.38 | 15.33 | 505.96 | 0.19 | 2.14 | 1571 |
| 2024-09-20 22:21:32.697 | MS1 | 121.4656582286 | 31.1446339057 | 50 | 504990 | -85.29 | 13.13 | 520.15 | 0.14 | 2.69 | 1574 |
| 2024-09-20 22:21:33.718 | MS1 | 121.4656623734 | 31.1446337459 | 50 | 504990 | -90.44 | 13.67 | 490.91 | 0.07 | 2.11 | 1600 |
| 2024-09-20 22:21:34.889 | MS1 | 121.4656739184 | 31.1446338076 | 50 | 504990 | -91.28 | 17.07 | 67.21 | 0.56 | 2.08 | 520 |
| 2024-09-20 22:21:35.168 | MS1 | 121.4656776938 | 31.1446312367 | 50 | 504990 | -85.68 | 17.63 | 50.99 | 0.66 | 2.25 | 567 |
| 2024-09-20 22:21:36.758 | MS1 | 121.4656655753 | 31.1446199608 | 50 | 504990 | -88.74 | 13.06 | 77.94 | 0.52 | 2.75 | 631 |
| 2024-09-20 22:21:37.730 | MS1 | 121.4656766625 | 31.1446290474 | 50 | 504990 | -90.81 | 7.56 | 70.84 | 0.60 | 2.18 | 682 |
| 2024-09-20 22:21:38.712 | MS1 | 121.4656704347 | 31.1446336213 | 50 | 504990 | -93.42 | 10.96 | 76.69 | 0.56 | 2.28 | 648 |
| 2024-09-20 22:21:39.224 | MS1 | 121.4656775344 | 31.1446322690 | 50 | 504990 | -89.80 | 10.15 | 78.32 | 0.58 | 2.23 | 528 |
| 2024-09-20 22:21:40.897 | MS1 | 121.4656671508 | 31.1446282605 | 50 | 504990 | -91.89 | 11.25 | 451.03 | 0.20 | 2.64 | 1593 |
| 2024-09-20 22:21:41.675 | MS1 | 121.4656619658 | 31.1446276743 | 50 | 504990 | -92.96 | 7.41 | 412.70 | 0.20 | 2.17 | 1586 |
| 2024-09-20 22:21:42.390 | MS1 | 121.4656581607 | 31.1446295291 | 50 | 504990 | -90.12 | 9.84 | 583.82 | 0.10 | 2.60 | 1562 |

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
| 3233356 | 3 | 121.4711301814 | 31.1526694301 | 76 | 3 | 5 | 49.4 | TDD | 405 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3234237 | 2 | 121.4704666612 | 31.1556714481 | 121 | 3 | 0 | 44.5 | TDD | 548 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3236776 | 1 | 121.4697410072 | 31.1519776270 | 252 | 3 | 8 | 38.3 | TDD | 50 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3278330 | 4 | 121.4708142830 | 31.1528301226 | 59 | 12 | 10 | 32.6 | TDD | 406 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.002 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.131 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.131 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.843 | NREventA3 | measId:2;ServCellPCI:529;Se... |
| 2024-09-20 22:21:38.083 | NRHandoverAttempt | SourcePCI:529;SourceNR-ARFC... |
| 2024-09-20 22:21:38.128 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.138 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.266 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.266 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236776 | 1 | 5.1527 | 17.1628 | -117.1373 | 18.7181 | 152.4489 | 0.0118 | 0.0194 |
| 2024_09_20 22:00 | 3234237 | 2 | 9.1154 | 19.3060 | -114.4732 | 14.1075 | 134.2716 | 0.0066 | 0.0123 |
| 2024_09_20 22:00 | 3233356 | 3 | 11.0203 | 11.5675 | -117.5291 | 7.4867 | 179.6165 | 0.0180 | 0.0007 |
| 2024_09_20 22:00 | 3278330 | 4 | 12.0281 | 16.3057 | -116.7976 | 13.4818 | 103.8554 | 0.0044 | 0.0090 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413688_47796387 | 504990 | 50 | -92.4 | 504990 | 405 | -97.1 | 504990 | 548 | -103.6 | 504990 | 406 |
| MR_1774413688_62007BA5 | 504990 | 50 | -91.8 | 504990 | 405 | -97.3 | 504990 | 548 | -101.5 | 504990 | 406 |
| MR_1774413688_8CBCE835 | 504990 | 50 | -93.2 | 504990 | 405 | -97.5 | 504990 | 548 | -101.3 | 504990 | 406 |
| MR_1774413688_A782FB54 | 504990 | 50 | -90.5 | 504990 | 405 | -97.8 | 504990 | 548 | -102.1 | 504990 | 406 |
| MR_1774413688_E77098EA | 504990 | 50 | -90.5 | 504990 | 405 | -98.0 | 504990 | 548 | -102.9 | 504990 | 406 |
| MR_1774413688_ACD2E357 | 504990 | 50 | -92.0 | 504990 | 405 | -96.8 | 504990 | 548 | -103.9 | 504990 | 406 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 441: `b03091a9-dee...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b03091a9-dee1-4250-90ca-28884720eb77` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[441] topology](images/train_0441.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271378_4
- `C2`: Lift the tilt angle  of 3271378_4 by 10 degrees
- `C3`: Increase transmission power for 3261408_3
- `C4`: Decrease A3 Offset threshold for 3261408_3
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease A3 Offset threshold for 3271378_4
- `C7`: Add neighbor relationship between 3250675_2 and 3271378_4
- `C8`: Adjust the azimuth of 3271378_4 by 24 degrees
- `C9`: Increase A3 Offset threshold for 3271378_4
- `C10`: Decrease transmission power for 3271378_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261408_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261408_3
- `C13`: Increase A3 Offset threshold for 3261408_3
- `C14`: Lift the tilt angle of 3261408_3 by 8 degrees
- `C15`: Decrease transmission power for 3261408_3
- `C16`: Adjust the azimuth of 3261408_3 by 50 degrees
- `C17`: Check test server and transmission issues **← 정답**
- `C18`: Press down the tilt angle of 3261408_3 by 8 degrees
- `C19`: Add neighbor relationship between 3261408_3 and 3271378_4
- `C20`: Press down the tilt angle  of 3271378_4 by 10 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271378_4
- `C22`: Increase transmission power for 3271378_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.352 | MS1 | 121.4656599572 | 31.1446193875 | 268 | 504990 | -90.34 | 16.33 | 486.49 | 0.18 | 2.96 | 1575 |
| 2024-09-20 22:21:32.542 | MS1 | 121.4656726189 | 31.1446369832 | 268 | 504990 | -85.47 | 16.97 | 304.05 | 0.01 | 2.56 | 1569 |
| 2024-09-20 22:21:33.479 | MS1 | 121.4656641422 | 31.1446223495 | 268 | 504990 | -87.92 | 15.64 | 522.04 | 0.14 | 2.14 | 1581 |
| 2024-09-20 22:21:34.389 | MS1 | 121.4656643222 | 31.1446300759 | 268 | 504990 | -87.22 | 12.05 | 94.33 | 0.14 | 2.97 | 402 |
| 2024-09-20 22:21:35.324 | MS1 | 121.4656720118 | 31.1446186733 | 268 | 504990 | -90.62 | 13.70 | 57.72 | 0.08 | 2.35 | 490 |
| 2024-09-20 22:21:36.658 | MS1 | 121.4656613721 | 31.1446305195 | 268 | 504990 | -86.29 | 16.04 | 76.54 | 0.00 | 2.25 | 400 |
| 2024-09-20 22:21:37.756 | MS1 | 121.4656682176 | 31.1446238524 | 268 | 504990 | -90.30 | 11.10 | 76.07 | 0.18 | 2.88 | 429 |
| 2024-09-20 22:21:38.238 | MS1 | 121.4656722606 | 31.1446251356 | 268 | 504990 | -93.04 | 10.85 | 60.80 | 0.10 | 2.28 | 311 |
| 2024-09-20 22:21:39.646 | MS1 | 121.4656725685 | 31.1446277938 | 268 | 504990 | -90.63 | 8.61 | 55.59 | 0.02 | 2.84 | 486 |
| 2024-09-20 22:21:40.951 | MS1 | 121.4656722767 | 31.1446244138 | 268 | 504990 | -90.44 | 11.93 | 454.28 | 0.05 | 2.34 | 1560 |
| 2024-09-20 22:21:41.479 | MS1 | 121.4656584687 | 31.1446361304 | 268 | 504990 | -92.03 | 8.06 | 444.75 | 0.12 | 2.21 | 1591 |
| 2024-09-20 22:21:42.794 | MS1 | 121.4656694381 | 31.1446189375 | 268 | 504990 | -91.51 | 8.73 | 506.37 | 0.05 | 2.52 | 1563 |

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
| 3250675 | 2 | 121.4684380114 | 31.1496252234 | 136 | 11 | 9 | 45.8 | TDD | 122 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3261408 | 3 | 121.4700072705 | 31.1447351545 | 50 | 5 | 2 | 24.5 | TDD | 268 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3271378 | 4 | 121.4673410988 | 31.1526622781 | 166 | 15 | 2 | 26.7 | TDD | 213 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3273086 | 1 | 121.4703410821 | 31.1444171417 | 26 | 8 | 7 | 37.5 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.240 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.262 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.381 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.381 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.104 | NREventA3 | measId:2;ServCellPCI:812;Se... |
| 2024-09-20 22:21:38.344 | NRHandoverAttempt | SourcePCI:812;SourceNR-ARFC... |
| 2024-09-20 22:21:38.386 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.401 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.539 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.539 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273086 | 1 | 19.5568 | 13.0524 | -116.6662 | 7.1823 | 91.0468 | 0.0072 | 0.0016 |
| 2024_09_20 22:00 | 3250675 | 2 | 12.2887 | 13.2369 | -114.8069 | 17.0520 | 145.3796 | 0.0098 | 0.0013 |
| 2024_09_20 22:00 | 3261408 | 3 | 9.9929 | 12.7862 | -116.5633 | 9.2112 | 191.0593 | 0.0119 | 0.0132 |
| 2024_09_20 22:00 | 3271378 | 4 | 9.1994 | 12.5143 | -115.3282 | 19.3528 | 188.7286 | 0.0076 | 0.0186 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412292_428B5364 | 504990 | 268 | -87.7 | 504990 | 213 | -96.4 | 504990 | 122 | -100.1 | 504990 | 129 |
| MR_1774412292_761AE832 | 504990 | 268 | -87.9 | 504990 | 213 | -94.0 | 504990 | 122 | -98.0 | 504990 | 129 |
| MR_1774412292_E73EE2F7 | 504990 | 268 | -87.4 | 504990 | 213 | -94.4 | 504990 | 122 | -97.6 | 504990 | 129 |
| MR_1774412292_A37092E8 | 504990 | 268 | -88.2 | 504990 | 213 | -94.5 | 504990 | 122 | -96.6 | 504990 | 129 |
| MR_1774412292_9CB5422E | 504990 | 268 | -88.1 | 504990 | 213 | -96.7 | 504990 | 122 | -98.8 | 504990 | 129 |
| MR_1774412292_7047DF7B | 504990 | 268 | -87.5 | 504990 | 213 | -96.2 | 504990 | 122 | -97.8 | 504990 | 129 |
| MR_1774412292_13C8EE4A | 504990 | 268 | -88.1 | 504990 | 213 | -97.6 | 504990 | 122 | -97.2 | 504990 | 129 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 442: `18a246d5-058...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `18a246d5-0583-4353-aa6e-203e3da14f76` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[442] topology](images/train_0442.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment. **← 정답**
- `C2`: Decrease transmission power for 3258206_1
- `C3`: Press down the tilt angle of 3215048_3 by 10 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215048_3
- `C5`: Press down the tilt angle  of 3258206_1 by 10 degrees
- `C6`: Increase transmission power for 3258206_1
- `C7`: Adjust the azimuth of 3258206_1 by 50 degrees
- `C8`: Lift the tilt angle of 3215048_3 by 10 degrees
- `C9`: Decrease transmission power for 3215048_3
- `C10`: Increase transmission power for 3215048_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258206_1
- `C12`: Lift the tilt angle  of 3258206_1 by 10 degrees
- `C13`: Increase A3 Offset threshold for 3258206_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215048_3
- `C15`: Decrease A3 Offset threshold for 3215048_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258206_1
- `C17`: Add neighbor relationship between 3233765_2 and 3258206_1
- `C18`: Check test server and transmission issues
- `C19`: Adjust the azimuth of 3215048_3 by 50 degrees
- `C20`: Add neighbor relationship between 3215048_3 and 3258206_1
- `C21`: Increase A3 Offset threshold for 3215048_3
- `C22`: Decrease A3 Offset threshold for 3258206_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.124 | MS1 | 121.4656623608 | 31.1446265476 | 683 | 504990 | -91.95 | 12.67 | 378.92 | 0.11 | 2.27 | 1572 |
| 2024-09-20 22:21:32.711 | MS1 | 121.4656760789 | 31.1446215114 | 683 | 504990 | -87.16 | 12.32 | 332.17 | 0.05 | 2.96 | 1594 |
| 2024-09-20 22:21:33.507 | MS1 | 121.4656629821 | 31.1446281076 | 683 | 504990 | -91.47 | 12.55 | 532.58 | 0.18 | 3.00 | 1592 |
| 2024-09-20 22:21:34.141 | MS1 | 121.4656690096 | 31.1446310798 | 683 | 504990 | -85.20 | 14.25 | 77.61 | 0.08 | 2.29 | 1583 |
| 2024-09-20 22:21:35.198 | MS1 | 121.4656698546 | 31.1446203416 | 683 | 504990 | -89.90 | 16.03 | 64.57 | 0.16 | 2.52 | 1579 |
| 2024-09-20 22:21:36.337 | MS1 | 121.4656724851 | 31.1446189303 | 683 | 504990 | -87.75 | 13.05 | 76.28 | 0.03 | 2.66 | 1570 |
| 2024-09-20 22:21:37.851 | MS1 | 121.4656779792 | 31.1446299236 | 683 | 504990 | -93.13 | 11.70 | 62.46 | 0.14 | 2.88 | 1584 |
| 2024-09-20 22:21:38.223 | MS1 | 121.4656767107 | 31.1446312312 | 683 | 504990 | -93.51 | 7.79 | 91.14 | 0.17 | 2.16 | 1578 |
| 2024-09-20 22:21:39.649 | MS1 | 121.4656604542 | 31.1446258997 | 683 | 504990 | -89.18 | 11.13 | 82.57 | 0.03 | 2.31 | 1576 |
| 2024-09-20 22:21:40.709 | MS1 | 121.4656657945 | 31.1446197405 | 683 | 504990 | -93.70 | 11.75 | 412.23 | 0.07 | 2.67 | 1591 |
| 2024-09-20 22:21:41.666 | MS1 | 121.4656648312 | 31.1446246814 | 683 | 504990 | -92.43 | 11.45 | 596.13 | 0.06 | 2.66 | 1585 |
| 2024-09-20 22:21:42.231 | MS1 | 121.4656650145 | 31.1446347728 | 683 | 504990 | -93.28 | 12.02 | 521.16 | 0.20 | 2.89 | 1579 |

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
| 3215048 | 3 | 121.4681711890 | 31.1512187776 | 134 | 9 | 5 | 37.4 | TDD | 683 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3233765 | 2 | 121.4650830918 | 31.1539776003 | 336 | 15 | 5 | 23.0 | TDD | 370 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3248852 | 4 | 121.4669979070 | 31.1476360380 | 344 | 10 | 4 | 28.4 | TDD | 164 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3258206 | 1 | 121.4664155989 | 31.1555295179 | 281 | 11 | 0 | 24.8 | TDD | 980 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.222 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.238 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.348 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.348 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.083 | NREventA3 | measId:2;ServCellPCI:802;Se... |
| 2024-09-20 22:21:38.323 | NRHandoverAttempt | SourcePCI:802;SourceNR-ARFC... |
| 2024-09-20 22:21:38.357 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.367 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.476 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.476 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3258206 | 1 | 94.9407 | 83.8774 | -116.9942 | 16.7003 | 165.3559 | 0.0126 | 0.0002 |
| 2024_09_19 22:00 | 3233765 | 2 | 81.7870 | 91.0954 | -115.2334 | 12.8416 | 135.2329 | 0.0044 | 0.0192 |
| 2024_09_19 22:00 | 3215048 | 3 | 92.6118 | 87.2790 | -116.1537 | 9.8401 | 186.7419 | 0.0042 | 0.0122 |
| 2024_09_19 22:00 | 3248852 | 4 | 85.0063 | 81.5444 | -114.8489 | 9.2665 | 105.0276 | 0.0146 | 0.0023 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412736_4279C566 | 504990 | 683 | -84.2 | 504990 | 980 | -88.4 | 504990 | 370 | -95.2 | 504990 | 164 |
| MR_1774412736_616C1FE9 | 504990 | 683 | -86.2 | 504990 | 980 | -88.7 | 504990 | 370 | -93.7 | 504990 | 164 |
| MR_1774412736_1F9BC227 | 504990 | 683 | -83.6 | 504990 | 980 | -86.9 | 504990 | 370 | -94.6 | 504990 | 164 |
| MR_1774412736_46569577 | 504990 | 683 | -86.3 | 504990 | 980 | -85.8 | 504990 | 370 | -95.2 | 504990 | 164 |
| MR_1774412736_53C78CA7 | 504990 | 683 | -86.5 | 504990 | 980 | -87.3 | 504990 | 370 | -94.3 | 504990 | 164 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 443: `30fc74c5-e2b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `30fc74c5-e2bd-4358-9147-e6e9778da50c` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Lift the tilt angle  of 3214423_2 by 5 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[443] topology](images/train_0443.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Lift the tilt angle  of 3214423_2 by 5 degrees **← 정답**
- `C3`: Decrease transmission power for 3251042_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228371_3
- `C5`: Adjust the azimuth of 3251042_1 by 24 degrees
- `C6`: Check test server and transmission issues
- `C7`: Increase transmission power for 3228371_3
- `C8`: Increase transmission power for 3251042_1
- `C9`: Press down the tilt angle of 3251042_1 by 1 degrees
- `C10`: Increase A3 Offset threshold for 3251042_1
- `C11`: Add neighbor relationship between 3214423_2 and 3228371_3
- `C12`: Decrease transmission power for 3228371_3
- `C13`: Decrease A3 Offset threshold for 3228371_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251042_1
- `C15`: Lift the tilt angle of 3251042_1 by 1 degrees
- `C16`: Add neighbor relationship between 3251042_1 and 3228371_3
- `C17`: Increase A3 Offset threshold for 3228371_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251042_1
- `C19`: Decrease A3 Offset threshold for 3251042_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228371_3
- `C21`: Adjust the azimuth of 3214423_2 by 23 degrees
- `C22`: Press down the tilt angle  of 3214423_2 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.257 | MS1 | 121.4656748754 | 31.1446285059 | 217 | 504990 | -86.59 | 16.98 | 317.28 | 0.18 | 2.68 | 1572 |
| 2024-09-20 22:21:32.369 | MS1 | 121.4656732542 | 31.1446291632 | 217 | 504990 | -87.04 | 17.34 | 426.05 | 0.11 | 2.54 | 1570 |
| 2024-09-20 22:21:33.667 | MS1 | 121.4656585846 | 31.1446291601 | 217 | 504990 | -91.79 | 16.85 | 319.61 | 0.02 | 2.04 | 1581 |
| 2024-09-20 22:21:34.128 | MS1 | 121.4656657477 | 31.1446242571 | 217 | 504990 | -86.96 | 13.62 | 45.11 | 0.12 | 2.67 | 1590 |
| 2024-09-20 22:21:35.526 | MS1 | 121.4656761410 | 31.1446182093 | 217 | 504990 | -87.68 | 17.78 | 65.52 | 0.09 | 2.71 | 1568 |
| 2024-09-20 22:21:36.355 | MS1 | 121.4656669876 | 31.1446360944 | 217 | 504990 | -88.19 | 16.64 | 105.73 | 0.04 | 2.68 | 1578 |
| 2024-09-20 22:21:37.209 | MS1 | 121.4656773266 | 31.1446342998 | 217 | 504990 | -93.25 | 7.28 | 51.39 | 0.07 | 2.81 | 1596 |
| 2024-09-20 22:21:38.513 | MS1 | 121.4656779602 | 31.1446241831 | 217 | 504990 | -90.66 | 12.68 | 48.50 | 0.08 | 2.05 | 1568 |
| 2024-09-20 22:21:39.846 | MS1 | 121.4656710674 | 31.1446199631 | 217 | 504990 | -93.83 | 7.38 | 80.36 | 0.18 | 2.22 | 1573 |
| 2024-09-20 22:21:40.107 | MS1 | 121.4656761954 | 31.1446353254 | 217 | 504990 | -93.81 | 10.10 | 475.66 | 0.11 | 2.30 | 1595 |
| 2024-09-20 22:21:41.768 | MS1 | 121.4656585191 | 31.1446272550 | 217 | 504990 | -93.64 | 10.40 | 533.98 | 0.05 | 2.66 | 1560 |
| 2024-09-20 22:21:42.970 | MS1 | 121.4656697357 | 31.1446190249 | 217 | 504990 | -89.90 | 9.06 | 478.62 | 0.18 | 2.15 | 1594 |

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
| 3214423 | 2 | 121.4664579856 | 31.1471830859 | 326 | 10 | 10 | 44.6 | TDD | 209 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3228371 | 3 | 121.4725339414 | 31.1452783051 | 241 | 3 | 6 | 23.3 | TDD | 193 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3228960 | 4 | 121.4734313084 | 31.1544292549 | 319 | 6 | 12 | 49.5 | TDD | 605 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3251042 | 1 | 121.4747398276 | 31.1529306659 | 247 | 0 | 9 | 21.8 | TDD | 217 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.946 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.082 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.082 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.808 | NREventA3 | measId:2;ServCellPCI:130;Se... |
| 2024-09-20 22:21:38.048 | NRHandoverAttempt | SourcePCI:130;SourceNR-ARFC... |
| 2024-09-20 22:21:38.094 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.105 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.237 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.237 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251042 | 1 | 82.6087 | 78.9252 | -115.4333 | 9.2499 | 192.9147 | 0.0200 | 0.0058 |
| 2024_09_20 22:00 | 3214423 | 2 | 14.5141 | 12.4085 | -116.4309 | 12.9301 | 146.5782 | 0.0027 | 0.0062 |
| 2024_09_20 22:00 | 3228371 | 3 | 14.8145 | 13.4636 | -117.3607 | 17.5491 | 157.4274 | 0.0133 | 0.0097 |
| 2024_09_20 22:00 | 3228960 | 4 | 7.7032 | 13.8505 | -115.5988 | 11.8315 | 173.8683 | 0.0123 | 0.0081 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417017_F3ED900D | 504990 | 217 | -85.3 | 504990 | 193 | -95.9 | 504990 | 209 | -97.7 | 504990 | 605 |
| MR_1774417017_C1DE7BCA | 504990 | 217 | -87.8 | 504990 | 193 | -97.4 | 504990 | 209 | -98.3 | 504990 | 605 |
| MR_1774417017_3EFFE1CE | 504990 | 217 | -88.6 | 504990 | 193 | -97.2 | 504990 | 209 | -99.5 | 504990 | 605 |
| MR_1774417017_6E17EEAB | 504990 | 217 | -87.6 | 504990 | 193 | -96.2 | 504990 | 209 | -97.4 | 504990 | 605 |
| MR_1774417017_52E1FD5B | 504990 | 217 | -88.6 | 504990 | 193 | -95.0 | 504990 | 209 | -97.6 | 504990 | 605 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 444: `efb96657-c8a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `efb96657-c8a8-4cd1-a92b-0a1468ef73e6` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Add neighbor relationship between 3246380_1 and 3210887_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[444] topology](images/train_0444.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3210887_2
- `C2`: Decrease transmission power for 3210887_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246380_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246380_1
- `C5`: Lift the tilt angle  of 3210887_2 by 1 degrees
- `C6`: Increase transmission power for 3210887_2
- `C7`: Add neighbor relationship between 3246380_1 and 3210887_2 **← 정답**
- `C8`: Increase transmission power for 3246380_1
- `C9`: Press down the tilt angle of 3246380_1 by 6 degrees
- `C10`: Adjust the azimuth of 3246380_1 by 50 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210887_2
- `C12`: Increase A3 Offset threshold for 3246380_1
- `C13`: Adjust the azimuth of 3210887_2 by 21 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210887_2
- `C15`: Press down the tilt angle  of 3210887_2 by 1 degrees
- `C16`: Decrease A3 Offset threshold for 3210887_2
- `C17`: Decrease transmission power for 3246380_1
- `C18`: Check test server and transmission issues
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Lift the tilt angle of 3246380_1 by 6 degrees
- `C21`: Add neighbor relationship between 3213342_3 and 3210887_2
- `C22`: Decrease A3 Offset threshold for 3246380_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.828 | MS1 | 121.4656674123 | 31.1446311206 | 821 | 504990 | -75.89 | 12.58 | 430.51 | 0.12 | 2.73 | 1581 |
| 2024-09-20 22:21:32.917 | MS1 | 121.4656678308 | 31.1446184835 | 821 | 504990 | -77.62 | 15.63 | 390.84 | 0.08 | 2.69 | 1578 |
| 2024-09-20 22:21:33.526 | MS1 | 121.4656750793 | 31.1446278527 | 821 | 504990 | -78.65 | 14.61 | 387.34 | 0.06 | 2.69 | 1575 |
| 2024-09-20 22:21:34.435 | MS1 | 121.4656602466 | 31.1446202886 | 821 | 504990 | -89.26 | -3.90 | 43.83 | 0.08 | 1.27 | 1585 |
| 2024-09-20 22:21:35.488 | MS1 | 121.4656626120 | 31.1446193585 | 821 | 504990 | -90.04 | -3.17 | 33.88 | 0.13 | 1.25 | 1577 |
| 2024-09-20 22:21:36.379 | MS1 | 121.4656621633 | 31.1446261469 | 821 | 504990 | -91.78 | -3.62 | 49.91 | 0.10 | 1.49 | 1571 |
| 2024-09-20 22:21:37.916 | MS1 | 121.4656675670 | 31.1446377211 | 821 | 504990 | -92.25 | -0.35 | 62.12 | 0.03 | 1.46 | 1600 |
| 2024-09-20 22:21:38.864 | MS1 | 121.4656591864 | 31.1446203900 | 821 | 504990 | -81.87 | 12.53 | 428.32 | 0.09 | 1.44 | 1580 |
| 2024-09-20 22:21:39.556 | MS1 | 121.4656695865 | 31.1446265706 | 821 | 504990 | -81.47 | 16.77 | 546.53 | 0.02 | 1.35 | 1587 |
| 2024-09-20 22:21:40.737 | MS1 | 121.4656718923 | 31.1446264630 | 821 | 504990 | -83.75 | 13.46 | 384.83 | 0.12 | 2.21 | 1589 |
| 2024-09-20 22:21:41.436 | MS1 | 121.4656637761 | 31.1446372616 | 821 | 504990 | -76.70 | 13.96 | 520.36 | 0.06 | 2.99 | 1578 |
| 2024-09-20 22:21:42.109 | MS1 | 121.4656647400 | 31.1446214059 | 821 | 504990 | -80.55 | 15.55 | 538.82 | 0.12 | 2.42 | 1591 |

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
| 3210887 | 2 | 121.4759009416 | 31.1483724788 | 268 | 0 | 2 | 19.8 | TDD | 347 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3213342 | 3 | 121.4719466496 | 31.1473399795 | 347 | 11 | 6 | 40.4 | TDD | 541 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3232350 | 4 | 121.4648612507 | 31.1473333212 | 247 | 14 | 8 | 43.2 | TDD | 606 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3246380 | 1 | 121.4732009371 | 31.1552811761 | 151 | 4 | 1 | 36.3 | TDD | 821 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.846 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.865 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.978 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.978 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.746 | NREventA3 | measId:2;ServCellPCI:90;Ser... |
| 2024-09-20 22:21:35.746 | NREventA3 | measId:2;ServCellPCI:90;Ser... |
| 2024-09-20 22:21:36.746 | NREventA3 | measId:2;ServCellPCI:90;Ser... |
| 2024-09-20 22:21:39.246 | NRRRCReestablishAttempt | PCI:90 |
| 2024-09-20 22:21:39.258 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.270 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.404 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.404 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246380 | 1 | 16.4541 | 18.6207 | -117.6601 | 19.7366 | 178.6005 | 0.0016 | 0.1669 |
| 2024_09_20 22:00 | 3210887 | 2 | 10.6289 | 13.3513 | -115.7259 | 6.4874 | 169.8839 | 0.0051 | 0.0148 |
| 2024_09_20 22:00 | 3213342 | 3 | 11.4863 | 9.4652 | -117.3355 | 5.8652 | 116.9765 | 0.0045 | 0.0051 |
| 2024_09_20 22:00 | 3232350 | 4 | 18.4899 | 9.7340 | -115.8840 | 11.4533 | 92.6611 | 0.0105 | 0.0162 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415907_CC0B9993 | 504990 | 347 | -83.0 | 504990 | 821 | -87.3 | 504990 | 541 | -92.0 | 504990 | 606 |
| MR_1774415907_D914BB50 | 504990 | 821 | -89.8 | 504990 | 347 | -84.6 | 504990 | 541 | -92.0 | 504990 | 606 |
| MR_1774415907_FCD04B58 | 504990 | 347 | -83.5 | 504990 | 821 | -89.2 | 504990 | 541 | -91.7 | 504990 | 606 |
| MR_1774415907_80E1A6E5 | 504990 | 821 | -90.4 | 504990 | 347 | -85.3 | 504990 | 541 | -92.1 | 504990 | 606 |
| MR_1774415907_48404E1A | 504990 | 347 | -86.5 | 504990 | 821 | -89.1 | 504990 | 541 | -90.2 | 504990 | 606 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 445: `0739c14e-bec...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0739c14e-bec3-45e6-bc58-8209cc2ceb7f` |
| Tag | **multiple-answer** |
| 정답 | **C7|C9|C15|C19** |
| C7 의미 | Increase A3 Offset threshold for 3244227_2 |
| C9 의미 | Press down the tilt angle  of 3244227_2 by 3 degrees |
| C15 의미 | Decrease transmission power for 3244227_2 |
| C19 의미 | Increase A3 Offset threshold for 3262079_4 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[445] topology](images/train_0445.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3262079_4 and 3244227_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262079_4
- `C3`: Check test server and transmission issues
- `C4`: Decrease A3 Offset threshold for 3262079_4
- `C5`: Decrease transmission power for 3262079_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase A3 Offset threshold for 3244227_2 **← 정답**
- `C8`: Increase transmission power for 3262079_4
- `C9`: Press down the tilt angle  of 3244227_2 by 3 degrees **← 정답**
- `C10`: Lift the tilt angle  of 3244227_2 by 3 degrees
- `C11`: Decrease A3 Offset threshold for 3244227_2
- `C12`: Add neighbor relationship between 3220555_3 and 3244227_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244227_2
- `C14`: Increase transmission power for 3244227_2
- `C15`: Decrease transmission power for 3244227_2 **← 정답**
- `C16`: Press down the tilt angle of 3262079_4 by 5 degrees
- `C17`: Adjust the azimuth of 3262079_4 by 36 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244227_2
- `C19`: Increase A3 Offset threshold for 3262079_4 **← 정답**
- `C20`: Adjust the azimuth of 3244227_2 by 30 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262079_4
- `C22`: Lift the tilt angle of 3262079_4 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.647 | MS1 | 121.4656649839 | 31.1446306136 | 658 | 504990 | -81.85 | 14.69 | 365.64 | 0.15 | 2.26 | 1584 |
| 2024-09-20 22:21:32.267 | MS1 | 121.4656699918 | 31.1446264450 | 658 | 504990 | -76.14 | 17.56 | 309.65 | 0.18 | 2.05 | 1566 |
| 2024-09-20 22:21:33.878 | MS1 | 121.4656588705 | 31.1446350651 | 658 | 504990 | -79.81 | 13.42 | 371.69 | 0.11 | 2.61 | 1585 |
| 2024-09-20 22:21:34.212 | MS1 | 121.4656703396 | 31.1446183945 | 631 | 504990 | -80.79 | 1.03 | 46.72 | 0.10 | 1.44 | 1577 |
| 2024-09-20 22:21:35.247 | MS1 | 121.4656770715 | 31.1446310369 | 631 | 504990 | -86.32 | 4.54 | 70.08 | 0.06 | 1.10 | 1563 |
| 2024-09-20 22:21:36.647 | MS1 | 121.4656581885 | 31.1446326400 | 658 | 504990 | -86.71 | 1.18 | 71.25 | 0.04 | 1.28 | 1569 |
| 2024-09-20 22:21:37.818 | MS1 | 121.4656752972 | 31.1446315653 | 658 | 504990 | -85.42 | 1.77 | 40.83 | 0.16 | 1.20 | 1572 |
| 2024-09-20 22:21:38.971 | MS1 | 121.4656724974 | 31.1446360231 | 631 | 504990 | -80.98 | 1.16 | 23.24 | 0.09 | 1.30 | 1569 |
| 2024-09-20 22:21:39.619 | MS1 | 121.4656684140 | 31.1446356671 | 631 | 504990 | -80.65 | 4.21 | 82.03 | 0.11 | 1.47 | 1564 |
| 2024-09-20 22:21:40.614 | MS1 | 121.4656744656 | 31.1446272258 | 631 | 504990 | -77.92 | 15.36 | 474.28 | 0.02 | 2.76 | 1560 |
| 2024-09-20 22:21:41.706 | MS1 | 121.4656677887 | 31.1446294657 | 631 | 504990 | -83.76 | 13.33 | 357.72 | 0.18 | 2.63 | 1564 |
| 2024-09-20 22:21:42.770 | MS1 | 121.4656627951 | 31.1446212416 | 631 | 504990 | -83.86 | 16.95 | 314.17 | 0.02 | 2.81 | 1587 |

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
| 3220555 | 3 | 121.4727587879 | 31.1502593788 | 318 | 4 | 5 | 48.3 | TDD | 272 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3231838 | 1 | 121.4743498331 | 31.1456554576 | 332 | 2 | 11 | 39.7 | TDD | 631 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3244227 | 2 | 121.4660642391 | 31.1547242512 | 212 | 1 | 8 | 39.9 | TDD | 904 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3261405 | 5 | 121.4733098852 | 31.1443616928 | 128 | 1 | 12 | 37.4 | TDD | 695 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3262079 | 4 | 121.4709090549 | 31.1522552904 | 174 | 3 | 9 | 36.3 | TDD | 658 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.870 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.888 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.027 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.027 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.711 | NREventA3 | measId:2;ServCellPCI:217;Se... |
| 2024-09-20 22:21:33.951 | NRHandoverAttempt | SourcePCI:217;SourceNR-ARFC... |
| 2024-09-20 22:21:33.993 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.008 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.147 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.147 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.711 | NREventA3 | measId:2;ServCellPCI:560;Se... |
| 2024-09-20 22:21:35.951 | NRHandoverAttempt | SourcePCI:560;SourceNR-ARFC... |
| 2024-09-20 22:21:35.984 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.997 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.117 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.117 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.711 | NREventA3 | measId:2;ServCellPCI:217;Se... |
| 2024-09-20 22:21:37.951 | NRHandoverAttempt | SourcePCI:217;SourceNR-ARFC... |
| 2024-09-20 22:21:37.988 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.998 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.133 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.133 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231838 | 1 | 18.1498 | 18.4892 | -115.6490 | 13.1893 | 126.8665 | 0.0042 | 0.0055 |
| 2024_09_20 22:00 | 3244227 | 2 | 9.5140 | 13.1423 | -117.1556 | 17.9977 | 82.4435 | 0.0078 | 0.0197 |
| 2024_09_20 22:00 | 3220555 | 3 | 11.1581 | 11.1096 | -115.8213 | 18.1501 | 166.6379 | 0.0001 | 0.0092 |
| 2024_09_20 22:00 | 3262079 | 4 | 5.8510 | 7.0545 | -117.1342 | 11.5686 | 174.8307 | 0.0172 | 0.0068 |
| 2024_09_20 22:00 | 3261405 | 5 | 16.5090 | 15.2789 | -114.4850 | 7.6280 | 143.2773 | 0.0056 | 0.0145 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414945_A32C1103 | 504990 | 658 | -79.6 | 504990 | 631 | -80.3 | 504990 | 904 | -88.8 | 504990 | 272 |
| MR_1774414945_0E13EE4B | 504990 | 658 | -80.9 | 504990 | 631 | -81.2 | 504990 | 904 | -87.5 | 504990 | 272 |
| MR_1774414945_E6AA09BF | 504990 | 658 | -80.8 | 504990 | 631 | -82.3 | 504990 | 904 | -88.2 | 504990 | 272 |
| MR_1774414945_327F2435 | 504990 | 658 | -82.0 | 504990 | 631 | -82.2 | 504990 | 904 | -89.4 | 504990 | 272 |
| MR_1774414945_2AAE76B7 | 504990 | 631 | -79.7 | 504990 | 658 | -79.7 | 504990 | 904 | -88.0 | 504990 | 272 |
| MR_1774414945_A14BDC3C | 504990 | 631 | -78.8 | 504990 | 658 | -79.6 | 504990 | 904 | -85.8 | 504990 | 272 |
| MR_1774414945_ADCAC872 | 504990 | 658 | -79.7 | 504990 | 631 | -82.4 | 504990 | 904 | -89.0 | 504990 | 272 |
| MR_1774414945_F3E36DB1 | 504990 | 631 | -79.9 | 504990 | 658 | -80.1 | 504990 | 904 | -88.3 | 504990 | 272 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 446: `48a74824-fef...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `48a74824-fef0-43cb-ab01-f9884fe7bed7` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[446] topology](images/train_0446.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3268161_2 by 10 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224064_4
- `C3`: Adjust the azimuth of 3224064_4 by 31 degrees
- `C4`: Increase A3 Offset threshold for 3224064_4
- `C5`: Press down the tilt angle  of 3224064_4 by 10 degrees
- `C6`: Adjust the azimuth of 3268161_2 by 19 degrees
- `C7`: Lift the tilt angle  of 3224064_4 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268161_2
- `C9`: Increase transmission power for 3268161_2
- `C10`: Check test server and transmission issues
- `C11`: Decrease transmission power for 3268161_2
- `C12`: Decrease A3 Offset threshold for 3224064_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268161_2
- `C14`: Add neighbor relationship between 3268161_2 and 3224064_4
- `C15`: Decrease transmission power for 3224064_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224064_4
- `C17`: Decrease A3 Offset threshold for 3268161_2
- `C18`: Increase transmission power for 3224064_4
- `C19`: Insufficient data; more data is needed for judgment. **← 정답**
- `C20`: Increase A3 Offset threshold for 3268161_2
- `C21`: Add neighbor relationship between 3210052_3 and 3224064_4
- `C22`: Press down the tilt angle of 3268161_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.371 | MS1 | 121.4656620171 | 31.1446361947 | 74 | 504990 | -87.62 | 12.44 | 390.76 | 0.07 | 2.50 | 1571 |
| 2024-09-20 22:21:32.549 | MS1 | 121.4656622140 | 31.1446269165 | 74 | 504990 | -85.48 | 12.68 | 501.30 | 0.03 | 2.02 | 1586 |
| 2024-09-20 22:21:33.355 | MS1 | 121.4656678132 | 31.1446340567 | 74 | 504990 | -85.31 | 15.61 | 500.38 | 0.08 | 2.67 | 1598 |
| 2024-09-20 22:21:34.252 | MS1 | 121.4656589965 | 31.1446353759 | 74 | 504990 | -90.13 | 12.89 | 68.39 | 0.08 | 2.42 | 1598 |
| 2024-09-20 22:21:35.670 | MS1 | 121.4656652871 | 31.1446340079 | 74 | 504990 | -89.53 | 12.44 | 82.70 | 0.18 | 2.91 | 1563 |
| 2024-09-20 22:21:36.342 | MS1 | 121.4656692141 | 31.1446256607 | 74 | 504990 | -91.81 | 17.91 | 68.22 | 0.19 | 2.91 | 1572 |
| 2024-09-20 22:21:37.236 | MS1 | 121.4656764412 | 31.1446215264 | 74 | 504990 | -91.49 | 9.61 | 63.98 | 0.00 | 2.27 | 1582 |
| 2024-09-20 22:21:38.127 | MS1 | 121.4656688381 | 31.1446319656 | 74 | 504990 | -92.26 | 9.40 | 54.46 | 0.12 | 2.57 | 1598 |
| 2024-09-20 22:21:39.362 | MS1 | 121.4656695259 | 31.1446322345 | 74 | 504990 | -91.25 | 7.29 | 64.44 | 0.19 | 2.50 | 1582 |
| 2024-09-20 22:21:40.534 | MS1 | 121.4656712013 | 31.1446264765 | 74 | 504990 | -91.35 | 9.79 | 546.64 | 0.04 | 2.91 | 1594 |
| 2024-09-20 22:21:41.630 | MS1 | 121.4656706270 | 31.1446324451 | 74 | 504990 | -91.98 | 8.88 | 441.47 | 0.06 | 2.69 | 1594 |
| 2024-09-20 22:21:42.929 | MS1 | 121.4656680365 | 31.1446318430 | 74 | 504990 | -92.67 | 9.74 | 292.33 | 0.12 | 2.74 | 1590 |

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
| 3210052 | 3 | 121.4718798014 | 31.1452249609 | 292 | 2 | 0 | 44.4 | TDD | 668 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3224064 | 4 | 121.4679180981 | 31.1463394135 | 259 | 12 | 6 | 46.0 | TDD | 742 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3268161 | 2 | 121.4684768608 | 31.1544629431 | 213 | 10 | 0 | 47.5 | TDD | 74 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3280000 | 1 | 121.4704109121 | 31.1461216884 | 142 | 14 | 6 | 21.4 | TDD | 320 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.779 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.794 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.921 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.921 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.605 | NREventA3 | measId:2;ServCellPCI:279;Se... |
| 2024-09-20 22:21:37.845 | NRHandoverAttempt | SourcePCI:279;SourceNR-ARFC... |
| 2024-09-20 22:21:37.891 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.905 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.007 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.007 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3280000 | 1 | 79.9965 | 93.6738 | -116.6295 | 18.9296 | 114.2776 | 0.0098 | 0.0062 |
| 2024_09_19 22:00 | 3268161 | 2 | 94.7915 | 86.0529 | -117.5873 | 10.6842 | 183.4249 | 0.0034 | 0.0035 |
| 2024_09_19 22:00 | 3210052 | 3 | 77.5989 | 85.1584 | -114.6860 | 13.3927 | 118.3234 | 0.0104 | 0.0145 |
| 2024_09_19 22:00 | 3224064 | 4 | 77.1016 | 82.3008 | -116.7791 | 14.4071 | 153.1101 | 0.0141 | 0.0090 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415490_38509AD1 | 504990 | 74 | -91.9 | 504990 | 742 | -97.3 | 504990 | 668 | -100.2 | 504990 | 320 |
| MR_1774415490_3DEBD18D | 504990 | 74 | -89.2 | 504990 | 742 | -98.2 | 504990 | 668 | -98.4 | 504990 | 320 |
| MR_1774415490_A0473464 | 504990 | 74 | -90.2 | 504990 | 742 | -95.7 | 504990 | 668 | -98.3 | 504990 | 320 |
| MR_1774415490_73075EB6 | 504990 | 74 | -91.7 | 504990 | 742 | -97.6 | 504990 | 668 | -98.9 | 504990 | 320 |
| MR_1774415490_3B0FF32D | 504990 | 74 | -91.7 | 504990 | 742 | -95.5 | 504990 | 668 | -101.6 | 504990 | 320 |
| MR_1774415490_D8C8AEEF | 504990 | 74 | -89.1 | 504990 | 742 | -98.3 | 504990 | 668 | -98.3 | 504990 | 320 |
| MR_1774415490_CB4F854E | 504990 | 74 | -90.6 | 504990 | 742 | -94.7 | 504990 | 668 | -99.8 | 504990 | 320 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 447: `f53ae612-73f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f53ae612-73f6-4db8-9aae-ee01b2004afe` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[447] topology](images/train_0447.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3257049_2
- `C2`: Decrease A3 Offset threshold for 3247564_1
- `C3`: Press down the tilt angle of 3247564_1 by 10 degrees
- `C4`: Increase transmission power for 3257049_2
- `C5`: Increase A3 Offset threshold for 3257049_2
- `C6`: Decrease transmission power for 3247564_1
- `C7`: Increase A3 Offset threshold for 3247564_1
- `C8`: Increase transmission power for 3247564_1
- `C9`: Adjust the azimuth of 3247564_1 by 2 degrees
- `C10`: Press down the tilt angle  of 3257049_2 by 10 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247564_1
- `C12`: Decrease transmission power for 3257049_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257049_2
- `C14`: Check test server and transmission issues **← 정답**
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247564_1
- `C16`: Add neighbor relationship between 3210493_4 and 3257049_2
- `C17`: Add neighbor relationship between 3247564_1 and 3257049_2
- `C18`: Lift the tilt angle  of 3257049_2 by 10 degrees
- `C19`: Lift the tilt angle of 3247564_1 by 10 degrees
- `C20`: Adjust the azimuth of 3257049_2 by 32 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257049_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.722 | MS1 | 121.4656718242 | 31.1446375863 | 130 | 504990 | -89.85 | 15.13 | 587.43 | 0.07 | 2.89 | 1589 |
| 2024-09-20 22:21:32.885 | MS1 | 121.4656603516 | 31.1446318982 | 130 | 504990 | -85.73 | 15.12 | 323.28 | 0.08 | 2.65 | 1561 |
| 2024-09-20 22:21:33.558 | MS1 | 121.4656762646 | 31.1446343144 | 130 | 504990 | -89.01 | 16.61 | 466.44 | 0.05 | 2.49 | 1596 |
| 2024-09-20 22:21:34.487 | MS1 | 121.4656777000 | 31.1446360458 | 130 | 504990 | -85.83 | 12.90 | 63.92 | 0.07 | 2.22 | 484 |
| 2024-09-20 22:21:35.116 | MS1 | 121.4656606088 | 31.1446317304 | 130 | 504990 | -85.08 | 16.01 | 50.89 | 0.11 | 2.33 | 495 |
| 2024-09-20 22:21:36.102 | MS1 | 121.4656777472 | 31.1446368253 | 130 | 504990 | -85.18 | 16.32 | 49.47 | 0.12 | 2.24 | 354 |
| 2024-09-20 22:21:37.419 | MS1 | 121.4656684934 | 31.1446313912 | 130 | 504990 | -92.01 | 7.74 | 77.79 | 0.09 | 2.30 | 436 |
| 2024-09-20 22:21:38.293 | MS1 | 121.4656637356 | 31.1446284141 | 130 | 504990 | -92.83 | 10.91 | 46.80 | 0.09 | 2.69 | 454 |
| 2024-09-20 22:21:39.299 | MS1 | 121.4656657890 | 31.1446267181 | 130 | 504990 | -90.35 | 9.84 | 46.78 | 0.02 | 2.39 | 418 |
| 2024-09-20 22:21:40.800 | MS1 | 121.4656774926 | 31.1446241653 | 130 | 504990 | -90.13 | 8.05 | 531.61 | 0.20 | 2.78 | 1573 |
| 2024-09-20 22:21:41.166 | MS1 | 121.4656688684 | 31.1446252359 | 130 | 504990 | -90.13 | 12.72 | 381.30 | 0.20 | 2.86 | 1593 |
| 2024-09-20 22:21:42.935 | MS1 | 121.4656632643 | 31.1446262768 | 130 | 504990 | -90.00 | 7.83 | 478.18 | 0.13 | 2.80 | 1580 |

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
| 3210493 | 4 | 121.4712310551 | 31.1537824627 | 112 | 6 | 9 | 49.7 | TDD | 189 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3247564 | 1 | 121.4703651494 | 31.1499250174 | 215 | 7 | 0 | 43.9 | TDD | 130 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3257049 | 2 | 121.4714175980 | 31.1451178982 | 296 | 13 | 0 | 17.2 | TDD | 10 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3274070 | 3 | 121.4665374095 | 31.1533899328 | 116 | 2 | 0 | 25.0 | TDD | 716 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.996 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.019 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.124 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.124 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.855 | NREventA3 | measId:2;ServCellPCI:672;Se... |
| 2024-09-20 22:21:38.095 | NRHandoverAttempt | SourcePCI:672;SourceNR-ARFC... |
| 2024-09-20 22:21:38.139 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.153 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.287 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.287 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247564 | 1 | 13.9859 | 17.7073 | -114.6868 | 13.1148 | 163.9025 | 0.0164 | 0.0062 |
| 2024_09_20 22:00 | 3257049 | 2 | 15.4797 | 5.4223 | -115.0214 | 16.2294 | 131.3338 | 0.0068 | 0.0160 |
| 2024_09_20 22:00 | 3274070 | 3 | 11.1281 | 7.6588 | -117.8721 | 5.0622 | 104.3767 | 0.0166 | 0.0196 |
| 2024_09_20 22:00 | 3210493 | 4 | 6.3489 | 11.9475 | -116.7327 | 6.1493 | 193.3967 | 0.0065 | 0.0086 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414918_FCCB31BC | 504990 | 130 | -85.2 | 504990 | 10 | -92.2 | 504990 | 189 | -93.8 | 504990 | 716 |
| MR_1774414918_C4D1DEAA | 504990 | 130 | -84.5 | 504990 | 10 | -93.4 | 504990 | 189 | -94.2 | 504990 | 716 |
| MR_1774414918_19428911 | 504990 | 130 | -85.5 | 504990 | 10 | -92.7 | 504990 | 189 | -94.8 | 504990 | 716 |
| MR_1774414918_A45A4A1B | 504990 | 130 | -86.3 | 504990 | 10 | -94.1 | 504990 | 189 | -96.0 | 504990 | 716 |
| MR_1774414918_C2FE1B2A | 504990 | 130 | -84.4 | 504990 | 10 | -94.5 | 504990 | 189 | -94.6 | 504990 | 716 |
| MR_1774414918_8AF783B7 | 504990 | 130 | -85.7 | 504990 | 10 | -94.0 | 504990 | 189 | -93.7 | 504990 | 716 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 448: `faaa7fd2-987...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `faaa7fd2-9875-4247-b503-6b51ea4caeea` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255015_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[448] topology](images/train_0448.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3213379_5
- `C2`: Add neighbor relationship between 3255015_2 and 3213379_5
- `C3`: Lift the tilt angle  of 3213379_5 by 2 degrees
- `C4`: Lift the tilt angle of 3255015_2 by 3 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255015_2
- `C6`: Decrease transmission power for 3213379_5
- `C7`: Decrease A3 Offset threshold for 3255015_2
- `C8`: Increase transmission power for 3255015_2
- `C9`: Adjust the azimuth of 3255015_2 by 39 degrees
- `C10`: Check test server and transmission issues
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213379_5
- `C13`: Increase transmission power for 3213379_5
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213379_5
- `C15`: Decrease transmission power for 3255015_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255015_2 **← 정답**
- `C17`: Add neighbor relationship between 3260299_12 and 3213379_5
- `C18`: Increase A3 Offset threshold for 3213379_5
- `C19`: Press down the tilt angle  of 3213379_5 by 2 degrees
- `C20`: Adjust the azimuth of 3213379_5 by 0 degrees
- `C21`: Increase A3 Offset threshold for 3255015_2
- `C22`: Press down the tilt angle of 3255015_2 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.497 | MS1 | 121.4656718168 | 31.1446180013 | 456 | 504990 | -94.91 | 13.60 | 392.63 | 0.03 | 2.91 | 1576 |
| 2024-09-20 22:21:32.218 | MS1 | 121.4656666781 | 31.1446273034 | 424 | 504990 | -94.54 | 10.30 | 473.89 | 0.04 | 2.57 | 1572 |
| 2024-09-20 22:21:33.318 | MS1 | 121.4656617228 | 31.1446247197 | 289 | 504990 | -95.74 | 10.46 | 439.58 | 0.08 | 2.01 | 1584 |
| 2024-09-20 22:21:34.726 | MS1 | 121.4656658426 | 31.1446187172 | 100 | 152650 | -96.36 | 2.62 | 60.61 | 0.07 | 1.83 | 925 |
| 2024-09-20 22:21:35.981 | MS1 | 121.4656725356 | 31.1446374902 | 777 | 152650 | -91.09 | 3.04 | 56.71 | 0.07 | 1.55 | 982 |
| 2024-09-20 22:21:36.989 | MS1 | 121.4656673401 | 31.1446195055 | 436 | 152650 | -89.49 | 5.26 | 107.70 | 0.07 | 1.83 | 946 |
| 2024-09-20 22:21:37.916 | MS1 | 121.4656708937 | 31.1446358057 | 841 | 152650 | -94.66 | 3.71 | 76.83 | 0.13 | 1.64 | 992 |
| 2024-09-20 22:21:38.137 | MS1 | 121.4656649833 | 31.1446264555 | 100 | 152650 | -90.20 | 4.74 | 53.49 | 0.11 | 1.69 | 936 |
| 2024-09-20 22:21:39.556 | MS1 | 121.4656651184 | 31.1446272177 | 777 | 152650 | -96.49 | 2.55 | 72.68 | 0.06 | 1.83 | 989 |
| 2024-09-20 22:21:40.165 | MS1 | 121.4656615199 | 31.1446299881 | 436 | 152650 | -87.07 | 6.59 | 56.47 | 0.02 | 2.07 | 1566 |
| 2024-09-20 22:21:41.271 | MS1 | 121.4656613043 | 31.1446253255 | 841 | 152650 | -95.90 | 6.80 | 72.65 | 0.10 | 2.64 | 1565 |
| 2024-09-20 22:21:42.970 | MS1 | 121.4656743005 | 31.1446376859 | 100 | 152650 | -91.11 | 3.92 | 61.78 | 0.10 | 2.27 | 1571 |

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
| 3210433 | 6 | 121.4753752500 | 31.1481580652 | 170 | 6 | 2 | 5.8 | TDD | 955 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3210916 | 13 | 121.4682099816 | 31.1467372555 | 328 | 10 | 4 | 18.4 | FDD | 950 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3213379 | 5 | 121.4708209026 | 31.1510548217 | 214 | 1 | 6 | 21.6 | TDD | 633 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3214713 | 3 | 121.4648615008 | 31.1510097906 | 216 | 7 | 2 | 29.1 | TDD | 424 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3218369 | 8 | 121.4668708571 | 31.1516686519 | 91 | 9 | 12 | 8.9 | FDD | 100 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3224862 | 9 | 121.4719135433 | 31.1558156360 | 356 | 9 | 2 | 5.5 | FDD | 69 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3231317 | 7 | 121.4719759546 | 31.1545711289 | 354 | 10 | 6 | 14.7 | FDD | 481 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3247745 | 11 | 121.4727949132 | 31.1525737695 | 162 | 3 | 2 | 11.5 | FDD | 777 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3248494 | 1 | 121.4687161574 | 31.1527725009 | 61 | 12 | 2 | 6.1 | TDD | 289 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3255015 | 2 | 121.4653982351 | 31.1542568714 | 218 | 3 | 11 | 4.7 | TDD | 456 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3260299 | 12 | 121.4660886538 | 31.1504897285 | 150 | 10 | 9 | 2.4 | FDD | 436 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3262221 | 4 | 121.4744753971 | 31.1514428673 | 202 | 10 | 0 | 26.7 | TDD | 682 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3265024 | 10 | 121.4673017272 | 31.1530478269 | 291 | 6 | 9 | 15.4 | FDD | 841 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |

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
| 2024-09-20 22:21:30.933 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.956 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.060 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.060 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.810 | NREventA2 | measId:1;ServCellPCI:674;Se... |
| 2024-09-20 22:21:34.954 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.159 | NREventA5 | measId:3;ServCellPCI:674;Se... |
| 2024-09-20 22:21:35.230 | NRHandoverAttempt | SourcePCI:674;SourceNR-ARFC... |
| 2024-09-20 22:21:35.252 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.265 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.381 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.381 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248494 | 1 | 7.8167 | 9.7953 | -114.7882 | 19.2002 | 183.0695 | 0.0111 | 0.0111 |
| 2024_09_20 22:00 | 3255015 | 2 | 18.0579 | 18.6957 | -114.1188 | 7.7677 | 127.6263 | 0.0097 | 0.0165 |
| 2024_09_20 22:00 | 3214713 | 3 | 12.8980 | 10.0826 | -117.7948 | 7.6715 | 141.1308 | 0.0097 | 0.0172 |
| 2024_09_20 22:00 | 3262221 | 4 | 15.8163 | 12.8776 | -116.5205 | 18.5541 | 166.0333 | 0.0041 | 0.0091 |
| 2024_09_20 22:00 | 3213379 | 5 | 17.3344 | 12.5663 | -117.9357 | 12.2906 | 182.5255 | 0.0180 | 0.0040 |
| 2024_09_20 22:00 | 3210433 | 6 | 6.1572 | 13.6588 | -115.8614 | 10.4598 | 119.5509 | 0.0172 | 0.0113 |
| 2024_09_20 22:00 | 3231317 | 7 | 19.0569 | 8.3729 | -114.3843 | 4.1347 | 31.6675 | 0.0118 | 0.0057 |
| 2024_09_20 22:00 | 3218369 | 8 | 7.1898 | 18.8566 | -114.4091 | 3.6965 | 51.5088 | 0.0137 | 0.0034 |
| 2024_09_20 22:00 | 3224862 | 9 | 9.4443 | 18.0001 | -116.7796 | 4.8601 | 27.0796 | 0.0188 | 0.0084 |
| 2024_09_20 22:00 | 3265024 | 10 | 7.3982 | 8.2706 | -114.3165 | 3.3063 | 48.7419 | 0.0125 | 0.0001 |
| 2024_09_20 22:00 | 3247745 | 11 | 12.2536 | 19.4734 | -116.5408 | 4.3417 | 45.6018 | 0.0163 | 0.0130 |
| 2024_09_20 22:00 | 3260299 | 12 | 10.1750 | 11.1757 | -116.8431 | 3.7075 | 29.8118 | 0.0011 | 0.0157 |
| 2024_09_20 22:00 | 3210916 | 13 | 5.6730 | 18.3650 | -116.9334 | 3.9316 | 20.6414 | 0.0162 | 0.0038 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415892_596B8732 | 504990 | 289 | -95.8 | 504990 | 633 | -96.5 | 504990 | 955 | -97.6 | 504990 | 682 |
| MR_1774415892_C3BA8135 | 504990 | 289 | -94.2 | 504990 | 633 | -93.6 | 504990 | 955 | -99.4 | 504990 | 682 |
| MR_1774415892_A0092627 | 152650 | 100 | -97.8 | 152650 | 950 | -99.7 | 152650 | 481 | -105.9 | 152650 | 69 |
| MR_1774415892_AE157575 | 152650 | 100 | -94.9 | 152650 | 950 | -99.9 | 152650 | 481 | -105.7 | 152650 | 69 |
| MR_1774415892_790D7F56 | 152650 | 100 | -96.0 | 152650 | 950 | -99.8 | 152650 | 481 | -105.1 | 152650 | 69 |
| MR_1774415892_B04324F6 | 152650 | 100 | -97.4 | 152650 | 950 | -101.7 | 152650 | 481 | -104.5 | 152650 | 69 |
| MR_1774415892_A28F27F9 | 504990 | 289 | -93.8 | 504990 | 633 | -95.2 | 504990 | 955 | -98.3 | 504990 | 682 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 449: `a038c634-fe2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a038c634-fe27-4ba9-8303-dcc8c0b6dd1d` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease A3 Offset threshold for 3243160_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[449] topology](images/train_0449.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3250267_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase A3 Offset threshold for 3243160_1
- `C4`: Adjust the azimuth of 3250267_2 by 24 degrees
- `C5`: Press down the tilt angle of 3243160_1 by 10 degrees
- `C6`: Decrease A3 Offset threshold for 3243160_1 **← 정답**
- `C7`: Press down the tilt angle  of 3250267_2 by 10 degrees
- `C8`: Increase transmission power for 3250267_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243160_1
- `C10`: Decrease transmission power for 3250267_2
- `C11`: Check test server and transmission issues
- `C12`: Lift the tilt angle  of 3250267_2 by 10 degrees
- `C13`: Adjust the azimuth of 3243160_1 by 50 degrees
- `C14`: Increase A3 Offset threshold for 3250267_2
- `C15`: Decrease transmission power for 3243160_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250267_2
- `C17`: Lift the tilt angle of 3243160_1 by 10 degrees
- `C18`: Add neighbor relationship between 3243160_1 and 3250267_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250267_2
- `C20`: Add neighbor relationship between 3234445_4 and 3250267_2
- `C21`: Increase transmission power for 3243160_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243160_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.705 | MS1 | 121.4656597022 | 31.1446239804 | 976 | 504990 | -84.61 | 12.06 | 519.06 | 0.17 | 2.30 | 1581 |
| 2024-09-20 22:21:32.621 | MS1 | 121.4656653864 | 31.1446246745 | 976 | 504990 | -79.71 | 15.95 | 391.63 | 0.20 | 2.89 | 1582 |
| 2024-09-20 22:21:33.109 | MS1 | 121.4656611250 | 31.1446292068 | 976 | 504990 | -81.98 | 16.72 | 398.29 | 0.10 | 2.42 | 1591 |
| 2024-09-20 22:21:34.732 | MS1 | 121.4656657417 | 31.1446261565 | 976 | 504990 | -90.89 | -2.70 | 63.50 | 0.14 | 1.35 | 1578 |
| 2024-09-20 22:21:35.667 | MS1 | 121.4656684623 | 31.1446327703 | 976 | 504990 | -86.79 | -1.52 | 71.68 | 0.04 | 1.02 | 1572 |
| 2024-09-20 22:21:36.844 | MS1 | 121.4656677195 | 31.1446351796 | 976 | 504990 | -91.90 | -1.75 | 53.21 | 0.11 | 1.12 | 1573 |
| 2024-09-20 22:21:37.585 | MS1 | 121.4656756171 | 31.1446331609 | 976 | 504990 | -85.69 | -1.59 | 63.41 | 0.06 | 1.33 | 1576 |
| 2024-09-20 22:21:38.322 | MS1 | 121.4656725472 | 31.1446314449 | 976 | 504990 | -89.72 | -1.68 | 49.03 | 0.14 | 1.18 | 1593 |
| 2024-09-20 22:21:39.774 | MS1 | 121.4656712402 | 31.1446332178 | 827 | 504990 | -80.85 | 12.20 | 169.75 | 0.18 | 1.22 | 1563 |
| 2024-09-20 22:21:40.947 | MS1 | 121.4656729420 | 31.1446188242 | 827 | 504990 | -84.31 | 13.64 | 445.20 | 0.04 | 2.07 | 1597 |
| 2024-09-20 22:21:41.450 | MS1 | 121.4656762633 | 31.1446180993 | 827 | 504990 | -84.24 | 17.35 | 566.56 | 0.15 | 2.67 | 1598 |
| 2024-09-20 22:21:42.971 | MS1 | 121.4656735647 | 31.1446201293 | 827 | 504990 | -75.25 | 17.91 | 461.91 | 0.06 | 2.77 | 1592 |

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
| 3234445 | 4 | 121.4668958227 | 31.1550234773 | 121 | 10 | 8 | 38.9 | TDD | 775 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3243160 | 1 | 121.4653636586 | 31.1471068641 | 58 | 14 | 0 | 27.5 | TDD | 976 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3250267 | 2 | 121.4729947727 | 31.1530082037 | 241 | 12 | 9 | 30.1 | TDD | 827 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3273500 | 3 | 121.4640311828 | 31.1495035435 | 52 | 2 | 1 | 42.9 | TDD | 861 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.497 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.517 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.648 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.648 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.383 | NREventA3 | measId:2;ServCellPCI:882;Se... |
| 2024-09-20 22:21:38.623 | NRHandoverAttempt | SourcePCI:882;SourceNR-ARFC... |
| 2024-09-20 22:21:38.660 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.674 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.781 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.781 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243160 | 1 | 15.0976 | 17.9540 | -116.0015 | 18.5884 | 92.8498 | 0.0091 | 0.1855 |
| 2024_09_20 22:00 | 3250267 | 2 | 11.0058 | 16.9789 | -115.6526 | 5.6381 | 152.3945 | 0.0160 | 0.0157 |
| 2024_09_20 22:00 | 3273500 | 3 | 19.5030 | 13.6681 | -117.3941 | 11.9502 | 169.5246 | 0.0076 | 0.0179 |
| 2024_09_20 22:00 | 3234445 | 4 | 13.3288 | 5.7448 | -115.9711 | 5.2012 | 163.5388 | 0.0152 | 0.0010 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414609_EA04741B | 504990 | 976 | -90.6 | 504990 | 827 | -86.8 | 504990 | 775 | -90.4 | 504990 | 861 |
| MR_1774414609_572DEBA7 | 504990 | 976 | -89.7 | 504990 | 827 | -84.7 | 504990 | 775 | -93.5 | 504990 | 861 |
| MR_1774414609_55A52FF8 | 504990 | 976 | -91.1 | 504990 | 827 | -85.4 | 504990 | 775 | -92.0 | 504990 | 861 |
| MR_1774414609_803F9A33 | 504990 | 976 | -92.0 | 504990 | 827 | -83.9 | 504990 | 775 | -91.0 | 504990 | 861 |
| MR_1774414609_BFD8E367 | 504990 | 976 | -91.5 | 504990 | 827 | -83.8 | 504990 | 775 | -93.8 | 504990 | 861 |
| MR_1774414609_3C6FD4CD | 504990 | 976 | -89.3 | 504990 | 827 | -84.7 | 504990 | 775 | -90.8 | 504990 | 861 |
| MR_1774414609_1819994C | 504990 | 827 | -85.5 | 504990 | 976 | -90.3 | 504990 | 775 | -92.8 | 504990 | 861 |

> *... 2개 열 생략 (전체 14열)*

---
