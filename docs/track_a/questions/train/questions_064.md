# Track A 문제 분석 — train[630]~train[639]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[630] ~ train[639] (10개)

## 목차

1. [문제 630: `39c15917-132...`](#630) — multiple-answer, 정답: C2|C7|C14|C19
2. [문제 631: `49c5b101-853...`](#631) — single-answer, 정답: C8
3. [문제 632: `8f6645eb-304...`](#632) — single-answer, 정답: C6
4. [문제 633: `9c3c7eaf-864...`](#633) — single-answer, 정답: C11
5. [문제 634: `205abd53-9df...`](#634) — single-answer, 정답: C3
6. [문제 635: `3f06fe67-ced...`](#635) — single-answer, 정답: C11
7. [문제 636: `6d0bc0cb-52b...`](#636) — single-answer, 정답: C8
8. [문제 637: `075b3193-3bc...`](#637) — single-answer, 정답: C15
9. [문제 638: `0c1161b1-493...`](#638) — multiple-answer, 정답: C10|C14
10. [문제 639: `2c2c23c9-90c...`](#639) — single-answer, 정답: C10

---

### 문제 630: `39c15917-132...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `39c15917-132f-491c-8bda-fc1b5ad1c816` |
| Tag | **multiple-answer** |
| 정답 | **C2|C7|C14|C19** |
| C2 의미 | Increase A3 Offset threshold for 3278673_1 |
| C7 의미 | Press down the tilt angle  of 3278673_1 by 2 degrees |
| C14 의미 | Increase A3 Offset threshold for 3273087_5 |
| C19 의미 | Decrease transmission power for 3278673_1 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[630] topology](images/train_0630.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Increase A3 Offset threshold for 3278673_1 **← 정답**
- `C3`: Increase transmission power for 3278673_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273087_5
- `C5`: Lift the tilt angle  of 3278673_1 by 2 degrees
- `C6`: Adjust the azimuth of 3278673_1 by 37 degrees
- `C7`: Press down the tilt angle  of 3278673_1 by 2 degrees **← 정답**
- `C8`: Increase transmission power for 3273087_5
- `C9`: Lift the tilt angle of 3273087_5 by 5 degrees
- `C10`: Add neighbor relationship between 3225418_2 and 3278673_1
- `C11`: Press down the tilt angle of 3273087_5 by 5 degrees
- `C12`: Decrease A3 Offset threshold for 3278673_1
- `C13`: Adjust the azimuth of 3273087_5 by 14 degrees
- `C14`: Increase A3 Offset threshold for 3273087_5 **← 정답**
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278673_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278673_1
- `C18`: Decrease A3 Offset threshold for 3273087_5
- `C19`: Decrease transmission power for 3278673_1 **← 정답**
- `C20`: Decrease transmission power for 3273087_5
- `C21`: Add neighbor relationship between 3273087_5 and 3278673_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273087_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.322 | MS1 | 121.4656630174 | 31.1446366111 | 573 | 504990 | -80.08 | 17.68 | 579.02 | 0.12 | 2.71 | 1569 |
| 2024-09-20 22:21:32.938 | MS1 | 121.4656588354 | 31.1446362056 | 573 | 504990 | -79.09 | 12.03 | 307.42 | 0.08 | 2.05 | 1593 |
| 2024-09-20 22:21:33.118 | MS1 | 121.4656711318 | 31.1446335217 | 573 | 504990 | -82.33 | 14.64 | 545.80 | 0.04 | 2.11 | 1600 |
| 2024-09-20 22:21:34.360 | MS1 | 121.4656718609 | 31.1446355855 | 20 | 504990 | -81.74 | 4.45 | 60.09 | 0.15 | 1.09 | 1595 |
| 2024-09-20 22:21:35.648 | MS1 | 121.4656610780 | 31.1446184568 | 20 | 504990 | -88.86 | 4.42 | 49.65 | 0.20 | 1.29 | 1563 |
| 2024-09-20 22:21:36.139 | MS1 | 121.4656741733 | 31.1446357871 | 573 | 504990 | -84.57 | 4.62 | 81.92 | 0.03 | 1.42 | 1562 |
| 2024-09-20 22:21:37.855 | MS1 | 121.4656684952 | 31.1446189631 | 573 | 504990 | -86.13 | 4.92 | 58.77 | 0.18 | 1.29 | 1584 |
| 2024-09-20 22:21:38.697 | MS1 | 121.4656761158 | 31.1446214620 | 20 | 504990 | -85.64 | 4.58 | 46.59 | 0.10 | 1.49 | 1585 |
| 2024-09-20 22:21:39.335 | MS1 | 121.4656634186 | 31.1446339036 | 20 | 504990 | -83.40 | 1.89 | 73.06 | 0.02 | 1.12 | 1580 |
| 2024-09-20 22:21:40.234 | MS1 | 121.4656700188 | 31.1446187137 | 20 | 504990 | -84.80 | 13.46 | 485.05 | 0.01 | 2.60 | 1562 |
| 2024-09-20 22:21:41.352 | MS1 | 121.4656765302 | 31.1446313343 | 20 | 504990 | -82.98 | 12.05 | 348.47 | 0.11 | 2.41 | 1583 |
| 2024-09-20 22:21:42.984 | MS1 | 121.4656607453 | 31.1446187213 | 20 | 504990 | -81.12 | 17.42 | 419.17 | 0.16 | 2.74 | 1577 |

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
| 3225418 | 2 | 121.4726217601 | 31.1465004768 | 52 | 7 | 1 | 29.2 | TDD | 466 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3241712 | 3 | 121.4695681961 | 31.1547389242 | 146 | 1 | 3 | 48.4 | TDD | 20 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3242830 | 4 | 121.4685945689 | 31.1478225351 | 5 | 7 | 1 | 21.9 | TDD | 412 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3273087 | 5 | 121.4713055400 | 31.1556251000 | 190 | 4 | 0 | 29.9 | TDD | 573 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3278673 | 1 | 121.4679534926 | 31.1540217737 | 229 | 0 | 9 | 32.9 | TDD | 704 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.562 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.584 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.713 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.713 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.392 | NREventA3 | measId:2;ServCellPCI:613;Se... |
| 2024-09-20 22:21:34.632 | NRHandoverAttempt | SourcePCI:613;SourceNR-ARFC... |
| 2024-09-20 22:21:34.672 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.687 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.825 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.825 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.392 | NREventA3 | measId:2;ServCellPCI:652;Se... |
| 2024-09-20 22:21:36.632 | NRHandoverAttempt | SourcePCI:652;SourceNR-ARFC... |
| 2024-09-20 22:21:36.671 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.683 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:36.810 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.810 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.392 | NREventA3 | measId:2;ServCellPCI:613;Se... |
| 2024-09-20 22:21:38.632 | NRHandoverAttempt | SourcePCI:613;SourceNR-ARFC... |
| 2024-09-20 22:21:38.680 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.695 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.818 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.818 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278673 | 1 | 9.3430 | 16.8668 | -114.4605 | 10.0614 | 132.2161 | 0.0171 | 0.0087 |
| 2024_09_20 22:00 | 3225418 | 2 | 17.5062 | 17.9040 | -117.8064 | 18.6879 | 195.1655 | 0.0001 | 0.0058 |
| 2024_09_20 22:00 | 3241712 | 3 | 15.7113 | 14.3121 | -116.6263 | 15.4990 | 182.3438 | 0.0040 | 0.0160 |
| 2024_09_20 22:00 | 3242830 | 4 | 19.6158 | 11.7687 | -117.3681 | 17.6536 | 102.5642 | 0.0060 | 0.0076 |
| 2024_09_20 22:00 | 3273087 | 5 | 11.1916 | 14.5056 | -116.3432 | 16.0668 | 84.0903 | 0.0157 | 0.0111 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415768_2644ACF2 | 504990 | 573 | -80.6 | 504990 | 20 | -76.5 | 504990 | 704 | -85.2 | 504990 | 466 |
| MR_1774415768_3134AFFB | 504990 | 20 | -82.8 | 504990 | 573 | -78.5 | 504990 | 704 | -82.3 | 504990 | 466 |
| MR_1774415768_4FC0A4AF | 504990 | 573 | -82.1 | 504990 | 20 | -77.5 | 504990 | 704 | -81.9 | 504990 | 466 |
| MR_1774415768_7EA3DB1B | 504990 | 573 | -80.3 | 504990 | 20 | -78.0 | 504990 | 704 | -82.2 | 504990 | 466 |
| MR_1774415768_1ED8E714 | 504990 | 20 | -82.7 | 504990 | 573 | -78.2 | 504990 | 704 | -84.9 | 504990 | 466 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 631: `49c5b101-853...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `49c5b101-8539-4bab-ae18-6917e8e6a15e` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[631] topology](images/train_0631.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Add neighbor relationship between 3252476_4 and 3259642_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232713_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259642_2
- `C5`: Press down the tilt angle of 3232713_1 by 10 degrees
- `C6`: Decrease transmission power for 3259642_2
- `C7`: Add neighbor relationship between 3232713_1 and 3259642_2
- `C8`: Insufficient data; more data is needed for judgment. **← 정답**
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259642_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232713_1
- `C11`: Lift the tilt angle  of 3259642_2 by 10 degrees
- `C12`: Adjust the azimuth of 3232713_1 by 42 degrees
- `C13`: Decrease A3 Offset threshold for 3259642_2
- `C14`: Press down the tilt angle  of 3259642_2 by 10 degrees
- `C15`: Decrease transmission power for 3232713_1
- `C16`: Lift the tilt angle of 3232713_1 by 10 degrees
- `C17`: Adjust the azimuth of 3259642_2 by 36 degrees
- `C18`: Increase transmission power for 3259642_2
- `C19`: Increase A3 Offset threshold for 3232713_1
- `C20`: Increase A3 Offset threshold for 3259642_2
- `C21`: Decrease A3 Offset threshold for 3232713_1
- `C22`: Increase transmission power for 3232713_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.403 | MS1 | 121.4656774082 | 31.1446271170 | 72 | 504990 | -89.41 | 13.65 | 367.31 | 0.02 | 2.77 | 1590 |
| 2024-09-20 22:21:32.383 | MS1 | 121.4656762329 | 31.1446331607 | 72 | 504990 | -90.66 | 16.43 | 509.11 | 0.03 | 2.58 | 1589 |
| 2024-09-20 22:21:33.412 | MS1 | 121.4656606501 | 31.1446233375 | 72 | 504990 | -85.02 | 15.31 | 414.47 | 0.15 | 2.37 | 1567 |
| 2024-09-20 22:21:34.210 | MS1 | 121.4656693252 | 31.1446254394 | 72 | 504990 | -90.91 | 14.16 | 59.62 | 0.09 | 2.21 | 1591 |
| 2024-09-20 22:21:35.378 | MS1 | 121.4656759033 | 31.1446185522 | 72 | 504990 | -86.23 | 13.39 | 72.77 | 0.01 | 2.80 | 1592 |
| 2024-09-20 22:21:36.134 | MS1 | 121.4656711542 | 31.1446339274 | 72 | 504990 | -88.52 | 16.41 | 84.36 | 0.03 | 2.94 | 1596 |
| 2024-09-20 22:21:37.432 | MS1 | 121.4656705550 | 31.1446182023 | 72 | 504990 | -92.98 | 10.79 | 99.09 | 0.08 | 2.16 | 1576 |
| 2024-09-20 22:21:38.553 | MS1 | 121.4656773128 | 31.1446376015 | 72 | 504990 | -89.49 | 8.69 | 76.90 | 0.17 | 2.80 | 1589 |
| 2024-09-20 22:21:39.165 | MS1 | 121.4656626225 | 31.1446283574 | 72 | 504990 | -92.03 | 10.20 | 57.95 | 0.16 | 2.33 | 1563 |
| 2024-09-20 22:21:40.857 | MS1 | 121.4656615572 | 31.1446239387 | 72 | 504990 | -93.99 | 7.65 | 347.96 | 0.06 | 2.75 | 1574 |
| 2024-09-20 22:21:41.525 | MS1 | 121.4656595529 | 31.1446197394 | 72 | 504990 | -90.08 | 9.09 | 345.38 | 0.02 | 2.51 | 1577 |
| 2024-09-20 22:21:42.683 | MS1 | 121.4656696575 | 31.1446184318 | 72 | 504990 | -90.40 | 7.01 | 409.09 | 0.17 | 2.33 | 1575 |

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
| 3232713 | 1 | 121.4686990889 | 31.1495526322 | 166 | 12 | 5 | 44.2 | TDD | 72 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3252476 | 4 | 121.4711521977 | 31.1530707750 | 146 | 13 | 3 | 22.3 | TDD | 63 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3259642 | 2 | 121.4697579917 | 31.1532498444 | 166 | 10 | 8 | 23.0 | TDD | 571 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3263715 | 3 | 121.4651457335 | 31.1534491563 | 93 | 8 | 5 | 42.4 | TDD | 987 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.158 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.176 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.276 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.276 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.986 | NREventA3 | measId:2;ServCellPCI:303;Se... |
| 2024-09-20 22:21:38.226 | NRHandoverAttempt | SourcePCI:303;SourceNR-ARFC... |
| 2024-09-20 22:21:38.269 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.283 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.426 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.426 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3232713 | 1 | 80.5228 | 91.7378 | -115.0979 | 9.3996 | 181.0015 | 0.0099 | 0.0012 |
| 2024_09_19 22:00 | 3259642 | 2 | 77.0546 | 77.8434 | -114.2899 | 18.4281 | 151.1692 | 0.0186 | 0.0109 |
| 2024_09_19 22:00 | 3263715 | 3 | 92.0413 | 86.3348 | -117.6616 | 7.2334 | 153.4754 | 0.0037 | 0.0174 |
| 2024_09_19 22:00 | 3252476 | 4 | 76.9156 | 88.5862 | -117.8987 | 9.8506 | 119.8479 | 0.0029 | 0.0082 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412394_F1CA31AF | 504990 | 72 | -89.8 | 504990 | 571 | -101.6 | 504990 | 63 | -101.4 | 504990 | 987 |
| MR_1774412394_A04D30AB | 504990 | 72 | -92.1 | 504990 | 571 | -100.9 | 504990 | 63 | -101.4 | 504990 | 987 |
| MR_1774412394_609D09F8 | 504990 | 72 | -89.0 | 504990 | 571 | -101.3 | 504990 | 63 | -103.8 | 504990 | 987 |
| MR_1774412394_75876E22 | 504990 | 72 | -91.3 | 504990 | 571 | -98.7 | 504990 | 63 | -102.8 | 504990 | 987 |
| MR_1774412394_5D99F96D | 504990 | 72 | -91.0 | 504990 | 571 | -98.1 | 504990 | 63 | -102.2 | 504990 | 987 |
| MR_1774412394_B0F34107 | 504990 | 72 | -89.8 | 504990 | 571 | -98.6 | 504990 | 63 | -103.9 | 504990 | 987 |
| MR_1774412394_090489A2 | 504990 | 72 | -90.6 | 504990 | 571 | -100.2 | 504990 | 63 | -101.0 | 504990 | 987 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 632: `8f6645eb-304...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8f6645eb-304d-49fa-86b2-c73aeb955348` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[632] topology](images/train_0632.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254623_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260222_1
- `C3`: Increase transmission power for 3260222_1
- `C4`: Add neighbor relationship between 3212374_4 and 3260222_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260222_1
- `C6`: Insufficient data; more data is needed for judgment. **← 정답**
- `C7`: Check test server and transmission issues
- `C8`: Increase A3 Offset threshold for 3254623_3
- `C9`: Increase transmission power for 3254623_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254623_3
- `C11`: Add neighbor relationship between 3254623_3 and 3260222_1
- `C12`: Press down the tilt angle of 3254623_3 by 3 degrees
- `C13`: Increase A3 Offset threshold for 3260222_1
- `C14`: Adjust the azimuth of 3260222_1 by 50 degrees
- `C15`: Adjust the azimuth of 3254623_3 by 5 degrees
- `C16`: Lift the tilt angle  of 3260222_1 by 10 degrees
- `C17`: Decrease transmission power for 3260222_1
- `C18`: Press down the tilt angle  of 3260222_1 by 10 degrees
- `C19`: Decrease A3 Offset threshold for 3260222_1
- `C20`: Decrease A3 Offset threshold for 3254623_3
- `C21`: Lift the tilt angle of 3254623_3 by 3 degrees
- `C22`: Decrease transmission power for 3254623_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.586 | MS1 | 121.4656733866 | 31.1446357084 | 734 | 504990 | -89.01 | 15.70 | 510.19 | 0.09 | 2.38 | 1562 |
| 2024-09-20 22:21:32.224 | MS1 | 121.4656659336 | 31.1446368211 | 734 | 504990 | -88.02 | 15.15 | 347.91 | 0.08 | 2.00 | 1565 |
| 2024-09-20 22:21:33.864 | MS1 | 121.4656769086 | 31.1446372726 | 734 | 504990 | -90.51 | 12.07 | 375.83 | 0.03 | 2.02 | 1580 |
| 2024-09-20 22:21:34.383 | MS1 | 121.4656659378 | 31.1446296025 | 734 | 504990 | -88.11 | 17.66 | 97.85 | 0.10 | 2.73 | 1570 |
| 2024-09-20 22:21:35.228 | MS1 | 121.4656674252 | 31.1446212457 | 734 | 504990 | -89.91 | 13.78 | 77.68 | 0.03 | 2.28 | 1600 |
| 2024-09-20 22:21:36.704 | MS1 | 121.4656681715 | 31.1446338706 | 734 | 504990 | -89.19 | 14.99 | 69.50 | 0.06 | 2.36 | 1568 |
| 2024-09-20 22:21:37.687 | MS1 | 121.4656644669 | 31.1446196035 | 734 | 504990 | -93.89 | 9.20 | 73.51 | 0.17 | 2.30 | 1590 |
| 2024-09-20 22:21:38.601 | MS1 | 121.4656768289 | 31.1446186273 | 734 | 504990 | -92.97 | 8.00 | 81.46 | 0.01 | 2.39 | 1600 |
| 2024-09-20 22:21:39.755 | MS1 | 121.4656659667 | 31.1446191930 | 734 | 504990 | -93.15 | 11.95 | 56.17 | 0.16 | 2.95 | 1590 |
| 2024-09-20 22:21:40.985 | MS1 | 121.4656760452 | 31.1446269980 | 734 | 504990 | -90.69 | 7.43 | 333.98 | 0.13 | 2.44 | 1582 |
| 2024-09-20 22:21:41.824 | MS1 | 121.4656690023 | 31.1446265940 | 734 | 504990 | -90.84 | 11.98 | 365.42 | 0.03 | 2.33 | 1599 |
| 2024-09-20 22:21:42.545 | MS1 | 121.4656674856 | 31.1446264433 | 734 | 504990 | -90.53 | 12.75 | 309.16 | 0.17 | 2.91 | 1593 |

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
| 3212374 | 4 | 121.4655695298 | 31.1493234063 | 125 | 14 | 12 | 19.3 | TDD | 502 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3252141 | 2 | 121.4641991894 | 31.1444877506 | 304 | 8 | 9 | 45.7 | TDD | 233 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3254623 | 3 | 121.4728514412 | 31.1527243213 | 212 | 1 | 11 | 33.3 | TDD | 734 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3260222 | 1 | 121.4652958248 | 31.1454320543 | 43 | 14 | 10 | 18.8 | TDD | 193 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.249 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.396 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.396 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.040 | NREventA3 | measId:2;ServCellPCI:556;Se... |
| 2024-09-20 22:21:38.280 | NRHandoverAttempt | SourcePCI:556;SourceNR-ARFC... |
| 2024-09-20 22:21:38.317 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.328 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.436 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.436 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3260222 | 1 | 80.2729 | 86.3690 | -116.2652 | 9.8925 | 175.3132 | 0.0101 | 0.0128 |
| 2024_09_19 22:00 | 3252141 | 2 | 87.9465 | 90.8801 | -117.2986 | 8.8864 | 133.7771 | 0.0141 | 0.0097 |
| 2024_09_19 22:00 | 3254623 | 3 | 78.2243 | 91.5181 | -117.1830 | 14.4864 | 104.1234 | 0.0141 | 0.0177 |
| 2024_09_19 22:00 | 3212374 | 4 | 79.3137 | 88.9126 | -117.5061 | 13.4069 | 125.7876 | 0.0149 | 0.0167 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412115_6F1B8E18 | 504990 | 734 | -86.7 | 504990 | 193 | -94.9 | 504990 | 502 | -98.7 | 504990 | 233 |
| MR_1774412115_31EC96EA | 504990 | 734 | -86.2 | 504990 | 193 | -94.9 | 504990 | 502 | -98.6 | 504990 | 233 |
| MR_1774412115_4205AD29 | 504990 | 734 | -87.4 | 504990 | 193 | -96.0 | 504990 | 502 | -97.4 | 504990 | 233 |
| MR_1774412115_3E685C53 | 504990 | 734 | -86.4 | 504990 | 193 | -95.3 | 504990 | 502 | -96.4 | 504990 | 233 |
| MR_1774412115_E98948DF | 504990 | 734 | -88.8 | 504990 | 193 | -97.0 | 504990 | 502 | -98.6 | 504990 | 233 |
| MR_1774412115_59F2E1B0 | 504990 | 734 | -88.9 | 504990 | 193 | -94.9 | 504990 | 502 | -97.2 | 504990 | 233 |
| MR_1774412115_19D13291 | 504990 | 734 | -86.8 | 504990 | 193 | -93.4 | 504990 | 502 | -98.4 | 504990 | 233 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 633: `9c3c7eaf-864...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9c3c7eaf-864f-4927-a1ca-4ae55192452f` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Add neighbor relationship between 3231770_1 and 3250581_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[633] topology](images/train_0633.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250581_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease A3 Offset threshold for 3231770_1
- `C4`: Decrease transmission power for 3231770_1
- `C5`: Adjust the azimuth of 3250581_2 by 18 degrees
- `C6`: Lift the tilt angle of 3231770_1 by 10 degrees
- `C7`: Increase transmission power for 3231770_1
- `C8`: Increase transmission power for 3250581_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250581_2
- `C10`: Increase A3 Offset threshold for 3250581_2
- `C11`: Add neighbor relationship between 3231770_1 and 3250581_2 **← 정답**
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231770_1
- `C13`: Check test server and transmission issues
- `C14`: Decrease A3 Offset threshold for 3250581_2
- `C15`: Lift the tilt angle  of 3250581_2 by 3 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231770_1
- `C17`: Add neighbor relationship between 3222290_4 and 3250581_2
- `C18`: Press down the tilt angle of 3231770_1 by 10 degrees
- `C19`: Decrease transmission power for 3250581_2
- `C20`: Adjust the azimuth of 3231770_1 by 50 degrees
- `C21`: Press down the tilt angle  of 3250581_2 by 3 degrees
- `C22`: Increase A3 Offset threshold for 3231770_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.990 | MS1 | 121.4656714193 | 31.1446356394 | 40 | 504990 | -80.83 | 12.89 | 460.44 | 0.16 | 2.71 | 1587 |
| 2024-09-20 22:21:32.410 | MS1 | 121.4656650926 | 31.1446191470 | 40 | 504990 | -81.89 | 12.43 | 332.21 | 0.03 | 2.53 | 1570 |
| 2024-09-20 22:21:33.641 | MS1 | 121.4656684264 | 31.1446276478 | 40 | 504990 | -80.17 | 14.30 | 375.84 | 0.16 | 2.32 | 1585 |
| 2024-09-20 22:21:34.235 | MS1 | 121.4656611380 | 31.1446346579 | 40 | 504990 | -86.07 | -1.74 | 40.33 | 0.10 | 1.28 | 1598 |
| 2024-09-20 22:21:35.579 | MS1 | 121.4656667220 | 31.1446311989 | 40 | 504990 | -94.28 | -3.08 | 71.46 | 0.19 | 1.22 | 1562 |
| 2024-09-20 22:21:36.556 | MS1 | 121.4656753799 | 31.1446377439 | 40 | 504990 | -88.03 | -1.10 | 48.51 | 0.10 | 1.24 | 1572 |
| 2024-09-20 22:21:37.596 | MS1 | 121.4656778480 | 31.1446215110 | 40 | 504990 | -88.63 | -1.48 | 41.30 | 0.15 | 1.42 | 1578 |
| 2024-09-20 22:21:38.379 | MS1 | 121.4656708834 | 31.1446317251 | 40 | 504990 | -82.45 | 16.29 | 557.82 | 0.16 | 1.01 | 1574 |
| 2024-09-20 22:21:39.621 | MS1 | 121.4656640111 | 31.1446299538 | 40 | 504990 | -83.39 | 12.78 | 310.89 | 0.13 | 1.40 | 1561 |
| 2024-09-20 22:21:40.817 | MS1 | 121.4656645756 | 31.1446363711 | 40 | 504990 | -81.47 | 14.92 | 362.94 | 0.14 | 2.29 | 1580 |
| 2024-09-20 22:21:41.596 | MS1 | 121.4656695916 | 31.1446265655 | 40 | 504990 | -82.56 | 12.86 | 351.22 | 0.15 | 2.09 | 1566 |
| 2024-09-20 22:21:42.755 | MS1 | 121.4656725313 | 31.1446205734 | 40 | 504990 | -76.04 | 12.64 | 454.97 | 0.06 | 2.96 | 1574 |

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
| 3222290 | 4 | 121.4730604198 | 31.1519057117 | 358 | 11 | 12 | 21.3 | TDD | 149 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3231770 | 1 | 121.4730327221 | 31.1479114443 | 80 | 9 | 3 | 25.7 | TDD | 40 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3245329 | 3 | 121.4690526465 | 31.1446539101 | 191 | 10 | 6 | 24.0 | TDD | 544 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3250581 | 2 | 121.4694719755 | 31.1480077951 | 206 | 1 | 3 | 17.1 | TDD | 553 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.024 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.045 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.186 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.186 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.870 | NREventA3 | measId:2;ServCellPCI:660;Se... |
| 2024-09-20 22:21:35.870 | NREventA3 | measId:2;ServCellPCI:660;Se... |
| 2024-09-20 22:21:36.870 | NREventA3 | measId:2;ServCellPCI:660;Se... |
| 2024-09-20 22:21:39.370 | NRRRCReestablishAttempt | PCI:660 |
| 2024-09-20 22:21:39.389 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.400 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.526 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.526 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231770 | 1 | 8.6063 | 16.3311 | -115.3485 | 17.4055 | 126.8915 | 0.0110 | 0.1873 |
| 2024_09_20 22:00 | 3250581 | 2 | 7.9293 | 15.2736 | -116.7199 | 7.9814 | 158.6729 | 0.0186 | 0.0179 |
| 2024_09_20 22:00 | 3245329 | 3 | 12.6529 | 7.9551 | -116.7305 | 17.2498 | 124.3582 | 0.0002 | 0.0120 |
| 2024_09_20 22:00 | 3222290 | 4 | 5.8862 | 13.6880 | -116.8516 | 19.6823 | 151.5117 | 0.0041 | 0.0074 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414998_2B22C457 | 504990 | 553 | -82.6 | 504990 | 40 | -84.3 | 504990 | 149 | -88.4 | 504990 | 544 |
| MR_1774414998_A3060E95 | 504990 | 40 | -85.3 | 504990 | 553 | -79.9 | 504990 | 149 | -88.4 | 504990 | 544 |
| MR_1774414998_D1A6EBC4 | 504990 | 40 | -87.0 | 504990 | 553 | -80.9 | 504990 | 149 | -88.9 | 504990 | 544 |
| MR_1774414998_2ACD52C6 | 504990 | 40 | -85.7 | 504990 | 553 | -80.2 | 504990 | 149 | -87.9 | 504990 | 544 |
| MR_1774414998_ABA2B4EB | 504990 | 553 | -80.4 | 504990 | 40 | -84.8 | 504990 | 149 | -88.4 | 504990 | 544 |
| MR_1774414998_8BA8094F | 504990 | 40 | -88.0 | 504990 | 553 | -80.3 | 504990 | 149 | -88.0 | 504990 | 544 |
| MR_1774414998_98D5CDC7 | 504990 | 40 | -87.3 | 504990 | 553 | -80.2 | 504990 | 149 | -85.3 | 504990 | 544 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 634: `205abd53-9df...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `205abd53-9df9-488d-9ee9-7ba191b6a080` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease A3 Offset threshold for 3240928_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[634] topology](images/train_0634.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3244941_2 by 10 degrees
- `C2`: Decrease transmission power for 3240928_1
- `C3`: Decrease A3 Offset threshold for 3240928_1 **← 정답**
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Press down the tilt angle  of 3244941_2 by 10 degrees
- `C6`: Increase A3 Offset threshold for 3244941_2
- `C7`: Check test server and transmission issues
- `C8`: Add neighbor relationship between 3278656_4 and 3244941_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240928_1
- `C10`: Adjust the azimuth of 3244941_2 by 50 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244941_2
- `C12`: Decrease transmission power for 3244941_2
- `C13`: Increase A3 Offset threshold for 3240928_1
- `C14`: Increase transmission power for 3240928_1
- `C15`: Increase transmission power for 3244941_2
- `C16`: Add neighbor relationship between 3240928_1 and 3244941_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240928_1
- `C18`: Press down the tilt angle of 3240928_1 by 5 degrees
- `C19`: Decrease A3 Offset threshold for 3244941_2
- `C20`: Adjust the azimuth of 3240928_1 by 50 degrees
- `C21`: Lift the tilt angle of 3240928_1 by 5 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244941_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.148 | MS1 | 121.4656707110 | 31.1446334981 | 346 | 504990 | -80.69 | 16.48 | 436.25 | 0.13 | 2.81 | 1593 |
| 2024-09-20 22:21:32.676 | MS1 | 121.4656596138 | 31.1446323534 | 346 | 504990 | -78.01 | 14.48 | 586.39 | 0.13 | 2.61 | 1592 |
| 2024-09-20 22:21:33.384 | MS1 | 121.4656669405 | 31.1446314221 | 346 | 504990 | -82.56 | 16.85 | 374.62 | 0.09 | 2.33 | 1566 |
| 2024-09-20 22:21:34.365 | MS1 | 121.4656764712 | 31.1446225544 | 346 | 504990 | -92.66 | -3.81 | 43.76 | 0.14 | 1.05 | 1595 |
| 2024-09-20 22:21:35.938 | MS1 | 121.4656703639 | 31.1446288700 | 346 | 504990 | -84.62 | -3.28 | 82.10 | 0.00 | 1.03 | 1563 |
| 2024-09-20 22:21:36.605 | MS1 | 121.4656616372 | 31.1446277077 | 346 | 504990 | -87.29 | -0.50 | 43.94 | 0.18 | 1.01 | 1576 |
| 2024-09-20 22:21:37.752 | MS1 | 121.4656739361 | 31.1446203955 | 346 | 504990 | -87.01 | -3.51 | 73.07 | 0.09 | 1.15 | 1588 |
| 2024-09-20 22:21:38.423 | MS1 | 121.4656756067 | 31.1446182291 | 346 | 504990 | -88.73 | -2.60 | 42.04 | 0.08 | 1.04 | 1574 |
| 2024-09-20 22:21:39.681 | MS1 | 121.4656588325 | 31.1446355277 | 366 | 504990 | -81.83 | 13.12 | 245.73 | 0.02 | 1.08 | 1576 |
| 2024-09-20 22:21:40.593 | MS1 | 121.4656593214 | 31.1446205122 | 366 | 504990 | -84.81 | 16.28 | 378.54 | 0.17 | 2.34 | 1584 |
| 2024-09-20 22:21:41.928 | MS1 | 121.4656665715 | 31.1446258071 | 366 | 504990 | -82.54 | 15.16 | 519.18 | 0.02 | 2.77 | 1561 |
| 2024-09-20 22:21:42.942 | MS1 | 121.4656730890 | 31.1446204516 | 366 | 504990 | -80.96 | 12.06 | 556.07 | 0.14 | 2.36 | 1581 |

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
| 3240928 | 1 | 121.4744316439 | 31.1540165537 | 351 | 3 | 2 | 49.4 | TDD | 346 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3244941 | 2 | 121.4758297108 | 31.1467424166 | 355 | 12 | 1 | 15.4 | TDD | 366 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3274236 | 3 | 121.4672687249 | 31.1531924464 | 192 | 6 | 12 | 37.4 | TDD | 114 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3278656 | 4 | 121.4675694215 | 31.1463135260 | 284 | 10 | 1 | 19.6 | TDD | 143 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.270 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.401 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.401 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.104 | NREventA3 | measId:2;ServCellPCI:86;Ser... |
| 2024-09-20 22:21:38.344 | NRHandoverAttempt | SourcePCI:86;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.380 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.391 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.516 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.516 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240928 | 1 | 16.2865 | 6.9176 | -114.6352 | 12.4455 | 141.7417 | 0.0101 | 0.1322 |
| 2024_09_20 22:00 | 3244941 | 2 | 5.6755 | 19.9802 | -115.5384 | 14.0612 | 168.5631 | 0.0131 | 0.0104 |
| 2024_09_20 22:00 | 3274236 | 3 | 7.0869 | 15.0210 | -115.6823 | 11.0479 | 199.7565 | 0.0151 | 0.0172 |
| 2024_09_20 22:00 | 3278656 | 4 | 9.6066 | 14.0265 | -115.9058 | 17.4923 | 112.4950 | 0.0183 | 0.0147 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412897_09D42D93 | 504990 | 346 | -93.4 | 504990 | 366 | -85.1 | 504990 | 143 | -89.1 | 504990 | 114 |
| MR_1774412897_8548F882 | 504990 | 366 | -88.8 | 504990 | 346 | -90.7 | 504990 | 143 | -89.2 | 504990 | 114 |
| MR_1774412897_17D64E5D | 504990 | 366 | -87.6 | 504990 | 346 | -92.4 | 504990 | 143 | -86.1 | 504990 | 114 |
| MR_1774412897_9611C875 | 504990 | 346 | -93.2 | 504990 | 366 | -85.9 | 504990 | 143 | -87.5 | 504990 | 114 |
| MR_1774412897_E5406CE4 | 504990 | 366 | -88.5 | 504990 | 346 | -90.8 | 504990 | 143 | -87.3 | 504990 | 114 |
| MR_1774412897_1AA59312 | 504990 | 366 | -88.2 | 504990 | 346 | -91.2 | 504990 | 143 | -86.8 | 504990 | 114 |
| MR_1774412897_AE989C1F | 504990 | 346 | -92.7 | 504990 | 366 | -88.0 | 504990 | 143 | -87.3 | 504990 | 114 |
| MR_1774412897_1F0D084D | 504990 | 366 | -87.1 | 504990 | 346 | -92.4 | 504990 | 143 | -89.6 | 504990 | 114 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 635: `3f06fe67-ced...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3f06fe67-ced8-4b30-8ace-c83045501b50` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229735_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[635] topology](images/train_0635.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3252772_1
- `C2`: Add neighbor relationship between 3265477_7 and 3252772_1
- `C3`: Adjust the azimuth of 3252772_1 by 42 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Lift the tilt angle  of 3252772_1 by 3 degrees
- `C6`: Decrease A3 Offset threshold for 3229735_2
- `C7`: Check test server and transmission issues
- `C8`: Increase transmission power for 3229735_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252772_1
- `C10`: Adjust the azimuth of 3229735_2 by 1 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229735_2 **← 정답**
- `C12`: Decrease A3 Offset threshold for 3252772_1
- `C13`: Press down the tilt angle  of 3252772_1 by 3 degrees
- `C14`: Increase transmission power for 3252772_1
- `C15`: Increase A3 Offset threshold for 3252772_1
- `C16`: Press down the tilt angle of 3229735_2 by 5 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229735_2
- `C18`: Add neighbor relationship between 3229735_2 and 3252772_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252772_1
- `C20`: Increase A3 Offset threshold for 3229735_2
- `C21`: Lift the tilt angle of 3229735_2 by 5 degrees
- `C22`: Decrease transmission power for 3229735_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.879 | MS1 | 121.4656608543 | 31.1446329949 | 234 | 504990 | -95.62 | 11.76 | 340.91 | 0.00 | 2.03 | 1584 |
| 2024-09-20 22:21:32.133 | MS1 | 121.4656597305 | 31.1446361794 | 528 | 504990 | -93.10 | 10.97 | 353.41 | 0.09 | 2.45 | 1592 |
| 2024-09-20 22:21:33.479 | MS1 | 121.4656713410 | 31.1446303718 | 691 | 504990 | -95.29 | 12.53 | 407.76 | 0.08 | 2.90 | 1599 |
| 2024-09-20 22:21:34.279 | MS1 | 121.4656685072 | 31.1446378270 | 706 | 152650 | -94.33 | 4.74 | 82.33 | 0.14 | 1.50 | 937 |
| 2024-09-20 22:21:35.491 | MS1 | 121.4656768374 | 31.1446208274 | 460 | 152650 | -94.68 | 6.10 | 79.89 | 0.07 | 1.52 | 928 |
| 2024-09-20 22:21:36.591 | MS1 | 121.4656638734 | 31.1446289318 | 576 | 152650 | -88.42 | 7.23 | 64.00 | 0.14 | 1.57 | 903 |
| 2024-09-20 22:21:37.146 | MS1 | 121.4656647295 | 31.1446300664 | 49 | 152650 | -95.97 | 5.70 | 57.24 | 0.01 | 1.83 | 930 |
| 2024-09-20 22:21:38.882 | MS1 | 121.4656712921 | 31.1446292150 | 706 | 152650 | -90.58 | 5.07 | 58.28 | 0.19 | 1.58 | 922 |
| 2024-09-20 22:21:39.988 | MS1 | 121.4656690752 | 31.1446350890 | 460 | 152650 | -96.39 | 4.48 | 84.50 | 0.01 | 1.82 | 926 |
| 2024-09-20 22:21:40.935 | MS1 | 121.4656763856 | 31.1446259048 | 576 | 152650 | -89.68 | 2.87 | 60.35 | 0.08 | 2.14 | 1588 |
| 2024-09-20 22:21:41.369 | MS1 | 121.4656661408 | 31.1446357150 | 49 | 152650 | -95.85 | 2.24 | 77.50 | 0.02 | 2.86 | 1580 |
| 2024-09-20 22:21:42.144 | MS1 | 121.4656640935 | 31.1446304128 | 706 | 152650 | -90.35 | 7.70 | 56.97 | 0.10 | 2.11 | 1563 |

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
| 3216644 | 4 | 121.4710830148 | 31.1502894406 | 181 | 12 | 3 | 13.6 | TDD | 913 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3223925 | 8 | 121.4645011264 | 31.1505364899 | 29 | 10 | 4 | 5.1 | FDD | 706 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3228862 | 9 | 121.4704092163 | 31.1551919971 | 22 | 9 | 11 | 4.5 | FDD | 355 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3229735 | 2 | 121.4694619075 | 31.1454446878 | 255 | 1 | 4 | 24.7 | TDD | 234 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3236645 | 13 | 121.4656875238 | 31.1479836634 | 256 | 3 | 11 | 17.5 | FDD | 127 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3241152 | 6 | 121.4689230159 | 31.1493527897 | 252 | 9 | 5 | 6.2 | TDD | 55 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3244740 | 5 | 121.4732906251 | 31.1446320750 | 279 | 5 | 9 | 6.6 | TDD | 691 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3248998 | 3 | 121.4642284044 | 31.1495182612 | 286 | 0 | 3 | 10.3 | TDD | 528 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3252772 | 1 | 121.4735110933 | 31.1442204676 | 315 | 1 | 4 | 20.7 | TDD | 5 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3263422 | 11 | 121.4654885504 | 31.1467988078 | 191 | 2 | 0 | 21.9 | FDD | 460 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3264141 | 10 | 121.4669442289 | 31.1504196996 | 197 | 12 | 5 | 28.6 | FDD | 393 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3265477 | 7 | 121.4749347497 | 31.1448753030 | 292 | 10 | 6 | 7.2 | FDD | 576 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3270239 | 12 | 121.4693079586 | 31.1536095149 | 296 | 12 | 2 | 9.9 | FDD | 49 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |

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
| 2024-09-20 22:21:31.640 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.657 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.769 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.769 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.492 | NREventA2 | measId:1;ServCellPCI:884;Se... |
| 2024-09-20 22:21:35.604 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.819 | NREventA5 | measId:3;ServCellPCI:884;Se... |
| 2024-09-20 22:21:35.853 | NRHandoverAttempt | SourcePCI:884;SourceNR-ARFC... |
| 2024-09-20 22:21:35.884 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.898 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.024 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.024 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252772 | 1 | 16.1120 | 16.3022 | -114.2877 | 10.9510 | 183.9773 | 0.0053 | 0.0191 |
| 2024_09_20 22:00 | 3229735 | 2 | 8.7898 | 9.7489 | -116.1168 | 13.7047 | 195.6655 | 0.0131 | 0.0063 |
| 2024_09_20 22:00 | 3248998 | 3 | 19.1030 | 15.8673 | -114.7475 | 17.2588 | 91.9270 | 0.0042 | 0.0170 |
| 2024_09_20 22:00 | 3216644 | 4 | 5.1197 | 7.3621 | -117.5188 | 18.4212 | 185.9056 | 0.0182 | 0.0014 |
| 2024_09_20 22:00 | 3244740 | 5 | 15.8819 | 5.4042 | -117.5950 | 6.1579 | 103.5505 | 0.0015 | 0.0126 |
| 2024_09_20 22:00 | 3241152 | 6 | 6.8171 | 11.6772 | -117.6612 | 11.5814 | 141.1098 | 0.0006 | 0.0042 |
| 2024_09_20 22:00 | 3265477 | 7 | 17.9263 | 17.4318 | -115.6464 | 4.0628 | 32.9634 | 0.0096 | 0.0005 |
| 2024_09_20 22:00 | 3223925 | 8 | 10.8140 | 10.8480 | -116.2892 | 4.2802 | 58.4253 | 0.0188 | 0.0196 |
| 2024_09_20 22:00 | 3228862 | 9 | 6.0087 | 15.1073 | -117.3883 | 4.7573 | 55.9897 | 0.0090 | 0.0052 |
| 2024_09_20 22:00 | 3264141 | 10 | 15.7713 | 18.8545 | -116.5101 | 3.0355 | 54.1540 | 0.0030 | 0.0098 |
| 2024_09_20 22:00 | 3263422 | 11 | 12.3237 | 19.3861 | -116.2342 | 4.3044 | 39.0218 | 0.0114 | 0.0119 |
| 2024_09_20 22:00 | 3270239 | 12 | 18.6867 | 6.2700 | -117.0046 | 3.0465 | 52.6083 | 0.0112 | 0.0193 |
| 2024_09_20 22:00 | 3236645 | 13 | 12.5664 | 19.8125 | -116.5096 | 4.4019 | 32.2565 | 0.0044 | 0.0048 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416365_4930DF07 | 152650 | 706 | -93.9 | 152650 | 355 | -99.3 | 152650 | 127 | -100.2 | 152650 | 393 |
| MR_1774416365_76711C46 | 152650 | 706 | -96.2 | 152650 | 355 | -100.0 | 152650 | 127 | -101.2 | 152650 | 393 |
| MR_1774416365_BEA621E3 | 152650 | 706 | -95.4 | 152650 | 355 | -99.9 | 152650 | 127 | -102.2 | 152650 | 393 |
| MR_1774416365_6C447481 | 152650 | 706 | -94.8 | 152650 | 355 | -98.9 | 152650 | 127 | -99.9 | 152650 | 393 |
| MR_1774416365_79330CC3 | 504990 | 691 | -96.7 | 504990 | 5 | -96.4 | 504990 | 55 | -97.3 | 504990 | 913 |
| MR_1774416365_0663FBE4 | 504990 | 691 | -94.4 | 504990 | 5 | -95.7 | 504990 | 55 | -94.3 | 504990 | 913 |
| MR_1774416365_91830D0C | 152650 | 706 | -94.4 | 152650 | 355 | -98.0 | 152650 | 127 | -99.5 | 152650 | 393 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 636: `6d0bc0cb-52b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6d0bc0cb-52bf-43f7-ac72-afb1ce43147c` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3243631_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[636] topology](images/train_0636.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3272138_1
- `C2`: Decrease A3 Offset threshold for 3272138_1
- `C3`: Press down the tilt angle  of 3272138_1 by 10 degrees
- `C4`: Increase A3 Offset threshold for 3243631_4
- `C5`: Add neighbor relationship between 3222305_3 and 3272138_1
- `C6`: Check test server and transmission issues
- `C7`: Adjust the azimuth of 3272138_1 by 50 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243631_4 **← 정답**
- `C9`: Increase transmission power for 3243631_4
- `C10`: Add neighbor relationship between 3243631_4 and 3272138_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase A3 Offset threshold for 3272138_1
- `C13`: Lift the tilt angle  of 3272138_1 by 10 degrees
- `C14`: Lift the tilt angle of 3243631_4 by 5 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272138_1
- `C16`: Decrease A3 Offset threshold for 3243631_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243631_4
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272138_1
- `C19`: Decrease transmission power for 3243631_4
- `C20`: Increase transmission power for 3272138_1
- `C21`: Press down the tilt angle of 3243631_4 by 5 degrees
- `C22`: Adjust the azimuth of 3243631_4 by 46 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.478 | MS1 | 121.4656581277 | 31.1446371625 | 327 | 504990 | -89.61 | 13.33 | 418.26 | 0.12 | 2.21 | 1569 |
| 2024-09-20 22:21:32.938 | MS1 | 121.4656701959 | 31.1446187635 | 327 | 504990 | -91.25 | 14.67 | 358.14 | 0.05 | 2.78 | 1593 |
| 2024-09-20 22:21:33.642 | MS1 | 121.4656697539 | 31.1446232337 | 327 | 504990 | -86.19 | 14.27 | 580.02 | 0.14 | 2.84 | 1598 |
| 2024-09-20 22:21:34.992 | MS1 | 121.4656754111 | 31.1446321875 | 327 | 504990 | -90.20 | 14.28 | 89.92 | 0.59 | 2.21 | 673 |
| 2024-09-20 22:21:35.641 | MS1 | 121.4656735411 | 31.1446246927 | 327 | 504990 | -88.24 | 13.28 | 88.88 | 0.58 | 2.75 | 551 |
| 2024-09-20 22:21:36.276 | MS1 | 121.4656595681 | 31.1446315223 | 327 | 504990 | -87.64 | 15.76 | 61.09 | 0.61 | 2.41 | 686 |
| 2024-09-20 22:21:37.236 | MS1 | 121.4656672369 | 31.1446223802 | 327 | 504990 | -90.59 | 8.69 | 95.35 | 0.63 | 2.29 | 669 |
| 2024-09-20 22:21:38.818 | MS1 | 121.4656764291 | 31.1446253229 | 327 | 504990 | -93.29 | 11.77 | 71.29 | 0.60 | 2.06 | 689 |
| 2024-09-20 22:21:39.866 | MS1 | 121.4656631441 | 31.1446324121 | 327 | 504990 | -93.24 | 10.46 | 56.71 | 0.55 | 2.47 | 541 |
| 2024-09-20 22:21:40.388 | MS1 | 121.4656714205 | 31.1446346802 | 327 | 504990 | -90.93 | 8.62 | 344.72 | 0.06 | 2.40 | 1561 |
| 2024-09-20 22:21:41.809 | MS1 | 121.4656733926 | 31.1446349953 | 327 | 504990 | -93.82 | 12.67 | 377.18 | 0.07 | 2.56 | 1600 |
| 2024-09-20 22:21:42.507 | MS1 | 121.4656591409 | 31.1446327020 | 327 | 504990 | -93.21 | 12.66 | 382.06 | 0.06 | 2.55 | 1572 |

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
| 3222305 | 3 | 121.4679334947 | 31.1524490024 | 276 | 3 | 8 | 26.3 | TDD | 86 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3243631 | 4 | 121.4670242705 | 31.1538591757 | 233 | 4 | 11 | 21.0 | TDD | 327 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3260411 | 2 | 121.4755763929 | 31.1541618093 | 280 | 1 | 3 | 39.9 | TDD | 554 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3272138 | 1 | 121.4660615086 | 31.1461026120 | 115 | 15 | 11 | 49.0 | TDD | 864 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.908 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.926 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.028 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.028 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.791 | NREventA3 | measId:2;ServCellPCI:439;Se... |
| 2024-09-20 22:21:38.031 | NRHandoverAttempt | SourcePCI:439;SourceNR-ARFC... |
| 2024-09-20 22:21:38.072 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.087 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.222 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.222 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272138 | 1 | 12.9062 | 17.8859 | -116.6628 | 13.9323 | 160.9003 | 0.0062 | 0.0190 |
| 2024_09_20 22:00 | 3260411 | 2 | 17.2275 | 16.6379 | -117.4087 | 18.4082 | 147.5842 | 0.0050 | 0.0047 |
| 2024_09_20 22:00 | 3222305 | 3 | 6.8544 | 11.2195 | -114.6226 | 6.7631 | 159.5559 | 0.0200 | 0.0116 |
| 2024_09_20 22:00 | 3243631 | 4 | 14.9518 | 13.8861 | -116.7825 | 19.4309 | 135.8264 | 0.0156 | 0.0180 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413001_5A4B4147 | 504990 | 327 | -91.4 | 504990 | 864 | -90.0 | 504990 | 86 | -97.9 | 504990 | 554 |
| MR_1774413001_C3DB3F50 | 504990 | 327 | -90.6 | 504990 | 864 | -93.0 | 504990 | 86 | -97.1 | 504990 | 554 |
| MR_1774413001_7043E52D | 504990 | 327 | -90.0 | 504990 | 864 | -89.8 | 504990 | 86 | -98.1 | 504990 | 554 |
| MR_1774413001_AEAFDCCD | 504990 | 327 | -90.3 | 504990 | 864 | -89.5 | 504990 | 86 | -98.0 | 504990 | 554 |
| MR_1774413001_DA757B93 | 504990 | 327 | -91.0 | 504990 | 864 | -92.2 | 504990 | 86 | -96.5 | 504990 | 554 |
| MR_1774413001_2238EA1E | 504990 | 327 | -89.4 | 504990 | 864 | -91.1 | 504990 | 86 | -95.9 | 504990 | 554 |
| MR_1774413001_F93460B6 | 504990 | 327 | -90.9 | 504990 | 864 | -90.1 | 504990 | 86 | -96.0 | 504990 | 554 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 637: `075b3193-3bc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `075b3193-3bcf-4792-af01-792ae9f096bb` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3229012_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[637] topology](images/train_0637.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3229012_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252033_1
- `C3`: Decrease transmission power for 3229012_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252033_1
- `C5`: Press down the tilt angle of 3229012_3 by 5 degrees
- `C6`: Check test server and transmission issues
- `C7`: Adjust the azimuth of 3252033_1 by 50 degrees
- `C8`: Decrease A3 Offset threshold for 3252033_1
- `C9`: Add neighbor relationship between 3229012_3 and 3252033_1
- `C10`: Adjust the azimuth of 3229012_3 by 34 degrees
- `C11`: Press down the tilt angle  of 3252033_1 by 10 degrees
- `C12`: Lift the tilt angle  of 3252033_1 by 10 degrees
- `C13`: Decrease transmission power for 3252033_1
- `C14`: Increase transmission power for 3229012_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229012_3 **← 정답**
- `C16`: Increase transmission power for 3252033_1
- `C17`: Add neighbor relationship between 3249910_4 and 3252033_1
- `C18`: Increase A3 Offset threshold for 3252033_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229012_3
- `C20`: Lift the tilt angle of 3229012_3 by 5 degrees
- `C21`: Increase A3 Offset threshold for 3229012_3
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.639 | MS1 | 121.4656614876 | 31.1446260431 | 403 | 504990 | -89.25 | 12.97 | 492.91 | 0.16 | 2.32 | 1587 |
| 2024-09-20 22:21:32.428 | MS1 | 121.4656709257 | 31.1446369403 | 403 | 504990 | -91.62 | 14.07 | 510.06 | 0.16 | 2.20 | 1590 |
| 2024-09-20 22:21:33.708 | MS1 | 121.4656660814 | 31.1446296443 | 403 | 504990 | -90.02 | 15.41 | 451.06 | 0.00 | 2.80 | 1563 |
| 2024-09-20 22:21:34.385 | MS1 | 121.4656750200 | 31.1446295553 | 403 | 504990 | -91.13 | 12.36 | 72.02 | 0.66 | 2.09 | 570 |
| 2024-09-20 22:21:35.135 | MS1 | 121.4656771551 | 31.1446352981 | 403 | 504990 | -87.95 | 17.39 | 71.69 | 0.60 | 2.51 | 684 |
| 2024-09-20 22:21:36.545 | MS1 | 121.4656625511 | 31.1446264376 | 403 | 504990 | -88.30 | 13.85 | 74.14 | 0.55 | 2.84 | 532 |
| 2024-09-20 22:21:37.691 | MS1 | 121.4656599019 | 31.1446299014 | 403 | 504990 | -91.51 | 7.78 | 99.94 | 0.57 | 2.21 | 510 |
| 2024-09-20 22:21:38.665 | MS1 | 121.4656621357 | 31.1446351185 | 403 | 504990 | -93.16 | 7.62 | 81.37 | 0.68 | 2.62 | 588 |
| 2024-09-20 22:21:39.774 | MS1 | 121.4656769022 | 31.1446262898 | 403 | 504990 | -91.88 | 11.81 | 70.28 | 0.56 | 2.70 | 594 |
| 2024-09-20 22:21:40.555 | MS1 | 121.4656645235 | 31.1446372233 | 403 | 504990 | -89.49 | 9.30 | 332.06 | 0.17 | 2.89 | 1578 |
| 2024-09-20 22:21:41.369 | MS1 | 121.4656754187 | 31.1446245511 | 403 | 504990 | -90.96 | 7.20 | 331.30 | 0.15 | 2.88 | 1586 |
| 2024-09-20 22:21:42.462 | MS1 | 121.4656712063 | 31.1446250892 | 403 | 504990 | -93.39 | 11.46 | 388.95 | 0.01 | 2.67 | 1586 |

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
| 3210462 | 2 | 121.4741795963 | 31.1538292638 | 183 | 8 | 3 | 44.0 | TDD | 603 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3229012 | 3 | 121.4715842489 | 31.1533725001 | 176 | 4 | 9 | 22.2 | TDD | 403 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3249910 | 4 | 121.4726727444 | 31.1492585135 | 103 | 5 | 4 | 28.4 | TDD | 917 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3252033 | 1 | 121.4736050706 | 31.1466604711 | 324 | 14 | 2 | 15.5 | TDD | 840 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.729 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.754 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.893 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.893 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.624 | NREventA3 | measId:2;ServCellPCI:969;Se... |
| 2024-09-20 22:21:37.864 | NRHandoverAttempt | SourcePCI:969;SourceNR-ARFC... |
| 2024-09-20 22:21:37.912 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.925 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.052 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.052 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252033 | 1 | 7.3996 | 6.9458 | -117.9785 | 15.5887 | 113.3339 | 0.0077 | 0.0039 |
| 2024_09_20 22:00 | 3210462 | 2 | 5.4830 | 11.5303 | -117.6783 | 9.0736 | 142.7291 | 0.0002 | 0.0089 |
| 2024_09_20 22:00 | 3229012 | 3 | 11.5311 | 8.0803 | -114.6466 | 10.6651 | 199.3243 | 0.0089 | 0.0085 |
| 2024_09_20 22:00 | 3249910 | 4 | 11.2302 | 5.8544 | -114.2343 | 18.1478 | 154.6414 | 0.0064 | 0.0011 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415530_DA5CD58C | 504990 | 403 | -90.5 | 504990 | 840 | -98.5 | 504990 | 917 | -101.7 | 504990 | 603 |
| MR_1774415530_A200A26A | 504990 | 403 | -92.7 | 504990 | 840 | -99.5 | 504990 | 917 | -99.3 | 504990 | 603 |
| MR_1774415530_727B924E | 504990 | 403 | -90.2 | 504990 | 840 | -98.8 | 504990 | 917 | -98.5 | 504990 | 603 |
| MR_1774415530_1614D807 | 504990 | 403 | -89.1 | 504990 | 840 | -98.4 | 504990 | 917 | -101.8 | 504990 | 603 |
| MR_1774415530_5C423AE0 | 504990 | 403 | -89.3 | 504990 | 840 | -99.5 | 504990 | 917 | -100.4 | 504990 | 603 |
| MR_1774415530_632F9196 | 504990 | 403 | -92.6 | 504990 | 840 | -98.1 | 504990 | 917 | -100.6 | 504990 | 603 |
| MR_1774415530_E1398F98 | 504990 | 403 | -90.5 | 504990 | 840 | -99.9 | 504990 | 917 | -98.3 | 504990 | 603 |
| MR_1774415530_86A94625 | 504990 | 403 | -91.1 | 504990 | 840 | -99.1 | 504990 | 917 | -101.8 | 504990 | 603 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 638: `0c1161b1-493...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0c1161b1-493f-4ede-9e62-d766945fc8a5` |
| Tag | **multiple-answer** |
| 정답 | **C10|C14** |
| C10 의미 | Press down the tilt angle  of 3234335_4 by 6 degrees |
| C14 의미 | Decrease transmission power for 3234335_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[638] topology](images/train_0638.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Adjust the azimuth of 3212333_1 by 42 degrees
- `C3`: Lift the tilt angle  of 3234335_4 by 6 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212333_1
- `C5`: Increase transmission power for 3234335_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212333_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234335_4
- `C8`: Increase A3 Offset threshold for 3234335_4
- `C9`: Add neighbor relationship between 3269492_3 and 3234335_4
- `C10`: Press down the tilt angle  of 3234335_4 by 6 degrees **← 정답**
- `C11`: Decrease A3 Offset threshold for 3212333_1
- `C12`: Lift the tilt angle of 3212333_1 by 2 degrees
- `C13`: Increase A3 Offset threshold for 3212333_1
- `C14`: Decrease transmission power for 3234335_4 **← 정답**
- `C15`: Increase transmission power for 3212333_1
- `C16`: Decrease transmission power for 3212333_1
- `C17`: Check test server and transmission issues
- `C18`: Press down the tilt angle of 3212333_1 by 2 degrees
- `C19`: Adjust the azimuth of 3234335_4 by 13 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234335_4
- `C21`: Add neighbor relationship between 3212333_1 and 3234335_4
- `C22`: Decrease A3 Offset threshold for 3234335_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.546 | MS1 | 121.4656762765 | 31.1446299212 | 26 | 504990 | -80.64 | 17.00 | 472.87 | 0.04 | 2.39 | 1571 |
| 2024-09-20 22:21:32.422 | MS1 | 121.4656624649 | 31.1446211204 | 26 | 504990 | -75.12 | 17.40 | 338.46 | 0.07 | 2.90 | 1578 |
| 2024-09-20 22:21:33.468 | MS1 | 121.4656643966 | 31.1446353824 | 26 | 504990 | -81.04 | 14.47 | 594.11 | 0.14 | 2.70 | 1560 |
| 2024-09-20 22:21:34.607 | MS1 | 121.4656642280 | 31.1446278300 | 26 | 504990 | -88.63 | 1.16 | 76.18 | 0.15 | 1.06 | 1573 |
| 2024-09-20 22:21:35.426 | MS1 | 121.4656624902 | 31.1446275085 | 26 | 504990 | -94.76 | 3.58 | 41.56 | 0.13 | 1.12 | 1589 |
| 2024-09-20 22:21:36.921 | MS1 | 121.4656647957 | 31.1446200770 | 26 | 504990 | -86.36 | 3.58 | 46.74 | 0.03 | 1.30 | 1570 |
| 2024-09-20 22:21:37.205 | MS1 | 121.4656631192 | 31.1446296337 | 26 | 504990 | -93.73 | 2.67 | 51.23 | 0.19 | 1.25 | 1574 |
| 2024-09-20 22:21:38.985 | MS1 | 121.4656602833 | 31.1446234375 | 26 | 504990 | -86.23 | 0.47 | 58.34 | 0.02 | 1.39 | 1588 |
| 2024-09-20 22:21:39.252 | MS1 | 121.4656711182 | 31.1446222800 | 26 | 504990 | -91.67 | 1.06 | 64.31 | 0.03 | 1.18 | 1566 |
| 2024-09-20 22:21:40.228 | MS1 | 121.4656689634 | 31.1446243070 | 26 | 504990 | -81.59 | 17.78 | 393.78 | 0.06 | 2.21 | 1565 |
| 2024-09-20 22:21:41.831 | MS1 | 121.4656611436 | 31.1446287346 | 26 | 504990 | -76.81 | 16.82 | 499.00 | 0.13 | 2.71 | 1585 |
| 2024-09-20 22:21:42.266 | MS1 | 121.4656588303 | 31.1446370680 | 26 | 504990 | -79.90 | 13.84 | 396.40 | 0.01 | 2.36 | 1590 |

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
| 3212333 | 1 | 121.4677839994 | 31.1557092665 | 147 | 1 | 7 | 23.6 | TDD | 26 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3214519 | 2 | 121.4696949023 | 31.1516562726 | 117 | 7 | 2 | 28.2 | TDD | 476 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3234335 | 4 | 121.4646209512 | 31.1521956939 | 160 | 4 | 6 | 23.3 | TDD | 174 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3269492 | 3 | 121.4717749853 | 31.1498442431 | 303 | 10 | 8 | 43.5 | TDD | 66 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.994 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.012 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.113 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.113 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212333 | 1 | 17.2150 | 19.1399 | -109.5676 | 14.1973 | 158.3021 | 0.0119 | 0.0070 |
| 2024_09_20 22:00 | 3214519 | 2 | 14.2419 | 10.9412 | -117.8347 | 11.8137 | 143.1841 | 0.0066 | 0.0115 |
| 2024_09_20 22:00 | 3269492 | 3 | 11.7764 | 5.9181 | -115.8415 | 9.9795 | 101.7813 | 0.0130 | 0.0131 |
| 2024_09_20 22:00 | 3234335 | 4 | 6.1293 | 5.1784 | -117.3699 | 12.3161 | 86.1863 | 0.0122 | 0.0105 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412293_E12A71FD | 504990 | 26 | -87.3 | 504990 | 174 | -88.9 | 504990 | 66 | -89.9 | 504990 | 476 |
| MR_1774412293_552AA0E6 | 504990 | 26 | -89.4 | 504990 | 174 | -87.8 | 504990 | 66 | -90.4 | 504990 | 476 |
| MR_1774412293_98B3FA42 | 504990 | 174 | -89.2 | 504990 | 26 | -88.4 | 504990 | 66 | -90.4 | 504990 | 476 |
| MR_1774412293_11D88A61 | 504990 | 26 | -89.8 | 504990 | 174 | -90.3 | 504990 | 66 | -90.8 | 504990 | 476 |
| MR_1774412293_3820B4DD | 504990 | 26 | -86.6 | 504990 | 174 | -90.0 | 504990 | 66 | -88.6 | 504990 | 476 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 639: `2c2c23c9-90c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2c2c23c9-90c3-40c4-9a4a-a72be26866ae` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Lift the tilt angle  of 3250771_2 by 5 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[639] topology](images/train_0639.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273253_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272039_3
- `C3`: Press down the tilt angle  of 3250771_2 by 5 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273253_4
- `C5`: Increase transmission power for 3272039_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272039_3
- `C7`: Decrease transmission power for 3273253_4
- `C8`: Adjust the azimuth of 3272039_3 by 3 degrees
- `C9`: Lift the tilt angle of 3272039_3 by 5 degrees
- `C10`: Lift the tilt angle  of 3250771_2 by 5 degrees **← 정답**
- `C11`: Increase A3 Offset threshold for 3273253_4
- `C12`: Decrease transmission power for 3272039_3
- `C13`: Press down the tilt angle of 3272039_3 by 5 degrees
- `C14`: Increase transmission power for 3273253_4
- `C15`: Add neighbor relationship between 3272039_3 and 3273253_4
- `C16`: Decrease A3 Offset threshold for 3272039_3
- `C17`: Add neighbor relationship between 3250771_2 and 3273253_4
- `C18`: Decrease A3 Offset threshold for 3273253_4
- `C19`: Check test server and transmission issues
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase A3 Offset threshold for 3272039_3
- `C22`: Adjust the azimuth of 3250771_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.354 | MS1 | 121.4656658436 | 31.1446356091 | 980 | 504990 | -90.93 | 12.04 | 560.54 | 0.18 | 2.27 | 1567 |
| 2024-09-20 22:21:32.173 | MS1 | 121.4656642262 | 31.1446325176 | 980 | 504990 | -89.42 | 13.77 | 357.95 | 0.20 | 2.63 | 1595 |
| 2024-09-20 22:21:33.865 | MS1 | 121.4656684486 | 31.1446359068 | 980 | 504990 | -86.50 | 12.64 | 561.14 | 0.13 | 2.46 | 1581 |
| 2024-09-20 22:21:34.706 | MS1 | 121.4656680246 | 31.1446254797 | 980 | 504990 | -87.78 | 13.30 | 83.19 | 0.11 | 2.27 | 1585 |
| 2024-09-20 22:21:35.853 | MS1 | 121.4656591379 | 31.1446191437 | 980 | 504990 | -85.02 | 13.59 | 79.40 | 0.18 | 2.63 | 1581 |
| 2024-09-20 22:21:36.667 | MS1 | 121.4656601663 | 31.1446373495 | 980 | 504990 | -89.20 | 13.47 | 54.62 | 0.05 | 2.18 | 1598 |
| 2024-09-20 22:21:37.923 | MS1 | 121.4656584379 | 31.1446234940 | 980 | 504990 | -92.45 | 7.86 | 44.59 | 0.00 | 2.41 | 1586 |
| 2024-09-20 22:21:38.676 | MS1 | 121.4656708806 | 31.1446304109 | 980 | 504990 | -90.19 | 9.85 | 67.00 | 0.02 | 2.70 | 1566 |
| 2024-09-20 22:21:39.777 | MS1 | 121.4656642334 | 31.1446310091 | 980 | 504990 | -90.34 | 11.07 | 88.60 | 0.20 | 2.63 | 1579 |
| 2024-09-20 22:21:40.763 | MS1 | 121.4656605094 | 31.1446195016 | 980 | 504990 | -92.49 | 11.09 | 386.29 | 0.02 | 2.88 | 1564 |
| 2024-09-20 22:21:41.356 | MS1 | 121.4656720223 | 31.1446342928 | 980 | 504990 | -93.13 | 10.05 | 524.23 | 0.07 | 2.41 | 1590 |
| 2024-09-20 22:21:42.516 | MS1 | 121.4656683392 | 31.1446213110 | 980 | 504990 | -89.71 | 9.18 | 449.56 | 0.16 | 2.74 | 1600 |

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
| 3212007 | 1 | 121.4703910591 | 31.1443488457 | 170 | 3 | 9 | 38.0 | TDD | 616 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3250771 | 2 | 121.4659125901 | 31.1454151978 | 77 | 2 | 5 | 44.4 | TDD | 138 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3272039 | 3 | 121.4691301910 | 31.1458330248 | 245 | 2 | 0 | 18.2 | TDD | 980 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3273253 | 4 | 121.4689289040 | 31.1534967387 | 334 | 4 | 11 | 26.5 | TDD | 748 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.555 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.575 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.719 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.719 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.439 | NREventA3 | measId:2;ServCellPCI:56;Ser... |
| 2024-09-20 22:21:38.679 | NRHandoverAttempt | SourcePCI:56;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.722 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.733 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.850 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.850 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212007 | 1 | 6.1724 | 19.6935 | -116.9853 | 15.6219 | 148.7776 | 0.0090 | 0.0006 |
| 2024_09_20 22:00 | 3250771 | 2 | 18.0506 | 16.4079 | -116.4085 | 15.8528 | 144.3368 | 0.0192 | 0.0071 |
| 2024_09_20 22:00 | 3272039 | 3 | 85.0732 | 84.5868 | -114.5284 | 19.4004 | 83.0346 | 0.0138 | 0.0012 |
| 2024_09_20 22:00 | 3273253 | 4 | 9.2005 | 19.3870 | -115.1472 | 13.8517 | 170.8063 | 0.0104 | 0.0033 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414005_ED7B53FD | 504990 | 980 | -87.8 | 504990 | 748 | -89.4 | 504990 | 138 | -101.6 | 504990 | 616 |
| MR_1774414005_025644A8 | 504990 | 980 | -88.8 | 504990 | 748 | -90.1 | 504990 | 138 | -99.0 | 504990 | 616 |
| MR_1774414005_35D8B0B3 | 504990 | 980 | -87.5 | 504990 | 748 | -90.4 | 504990 | 138 | -101.2 | 504990 | 616 |
| MR_1774414005_B1BBA546 | 504990 | 980 | -86.6 | 504990 | 748 | -87.9 | 504990 | 138 | -101.6 | 504990 | 616 |
| MR_1774414005_95CAAA28 | 504990 | 980 | -89.5 | 504990 | 748 | -91.3 | 504990 | 138 | -100.5 | 504990 | 616 |

> *... 2개 열 생략 (전체 14열)*

---
