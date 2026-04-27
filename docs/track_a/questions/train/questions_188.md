# Track A 문제 분석 — train[1870]~train[1879]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1870] ~ train[1879] (10개)

## 목차

1. [문제 1870: `43f94789-73b...`](#1870) — single-answer, 정답: C7
2. [문제 1871: `84e4a106-091...`](#1871) — multiple-answer, 정답: C7|C12|C17|C19
3. [문제 1872: `80be75ea-bfd...`](#1872) — single-answer, 정답: C3
4. [문제 1873: `4bac8bb1-11f...`](#1873) — single-answer, 정답: C4
5. [문제 1874: `eb1bfdff-968...`](#1874) — single-answer, 정답: C21
6. [문제 1875: `0a950fec-131...`](#1875) — single-answer, 정답: C1
7. [문제 1876: `a7276ee3-83e...`](#1876) — single-answer, 정답: C9
8. [문제 1877: `c7af2e46-262...`](#1877) — single-answer, 정답: C15
9. [문제 1878: `7508150a-e00...`](#1878) — multiple-answer, 정답: C5|C7
10. [문제 1879: `6852b271-6f8...`](#1879) — single-answer, 정답: C11

---

### 문제 1870: `43f94789-73b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `43f94789-73b4-4cba-8a53-52310587533b` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256924_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1870] topology](images/train_1870.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3246960_3
- `C2`: Increase transmission power for 3256924_6
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246960_3
- `C4`: Decrease transmission power for 3256924_6
- `C5`: Lift the tilt angle  of 3246960_3 by 2 degrees
- `C6`: Press down the tilt angle  of 3246960_3 by 2 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256924_6 **← 정답**
- `C8`: Adjust the azimuth of 3246960_3 by 38 degrees
- `C9`: Lift the tilt angle of 3256924_6 by 2 degrees
- `C10`: Increase A3 Offset threshold for 3256924_6
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256924_6
- `C12`: Decrease A3 Offset threshold for 3246960_3
- `C13`: Press down the tilt angle of 3256924_6 by 2 degrees
- `C14`: Check test server and transmission issues
- `C15`: Decrease transmission power for 3246960_3
- `C16`: Add neighbor relationship between 3256924_6 and 3246960_3
- `C17`: Increase transmission power for 3246960_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246960_3
- `C19`: Adjust the azimuth of 3256924_6 by 10 degrees
- `C20`: Decrease A3 Offset threshold for 3256924_6
- `C21`: Add neighbor relationship between 3247852_13 and 3246960_3
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.530 | MS1 | 121.4656716090 | 31.1446217535 | 282 | 504990 | -93.85 | 12.72 | 413.18 | 0.01 | 2.34 | 1574 |
| 2024-09-20 22:21:32.187 | MS1 | 121.4656736859 | 31.1446232202 | 580 | 504990 | -95.81 | 13.05 | 319.95 | 0.16 | 2.65 | 1593 |
| 2024-09-20 22:21:33.123 | MS1 | 121.4656610019 | 31.1446293891 | 53 | 504990 | -95.60 | 9.98 | 342.59 | 0.11 | 2.61 | 1574 |
| 2024-09-20 22:21:34.268 | MS1 | 121.4656625293 | 31.1446355133 | 82 | 152650 | -88.34 | 3.06 | 70.83 | 0.02 | 1.86 | 917 |
| 2024-09-20 22:21:35.383 | MS1 | 121.4656765185 | 31.1446287792 | 397 | 152650 | -92.23 | 2.98 | 74.38 | 0.15 | 1.79 | 992 |
| 2024-09-20 22:21:36.500 | MS1 | 121.4656705765 | 31.1446332259 | 187 | 152650 | -89.14 | 5.43 | 65.24 | 0.11 | 1.60 | 995 |
| 2024-09-20 22:21:37.638 | MS1 | 121.4656607432 | 31.1446372363 | 274 | 152650 | -92.10 | 3.05 | 63.86 | 0.06 | 1.51 | 938 |
| 2024-09-20 22:21:38.846 | MS1 | 121.4656725530 | 31.1446205635 | 82 | 152650 | -88.03 | 2.60 | 85.20 | 0.07 | 1.76 | 947 |
| 2024-09-20 22:21:39.499 | MS1 | 121.4656633051 | 31.1446340918 | 397 | 152650 | -87.68 | 6.10 | 64.19 | 0.03 | 1.99 | 965 |
| 2024-09-20 22:21:40.257 | MS1 | 121.4656661334 | 31.1446220175 | 187 | 152650 | -90.05 | 6.99 | 61.11 | 0.07 | 2.02 | 1592 |
| 2024-09-20 22:21:41.740 | MS1 | 121.4656610268 | 31.1446260700 | 274 | 152650 | -90.35 | 4.45 | 59.48 | 0.08 | 2.40 | 1592 |
| 2024-09-20 22:21:42.274 | MS1 | 121.4656718589 | 31.1446237158 | 82 | 152650 | -88.03 | 2.98 | 93.02 | 0.08 | 2.54 | 1588 |

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
| 3212071 | 11 | 121.4734640697 | 31.1543199962 | 284 | 6 | 10 | 13.5 | FDD | 82 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3212950 | 9 | 121.4653936606 | 31.1450586458 | 38 | 15 | 4 | 5.2 | FDD | 274 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3215777 | 1 | 121.4738078219 | 31.1443627940 | 260 | 7 | 3 | 14.1 | TDD | 580 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3221353 | 12 | 121.4707582839 | 31.1547994516 | 59 | 9 | 0 | 28.4 | FDD | 215 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3224092 | 2 | 121.4757395401 | 31.1476143500 | 355 | 6 | 2 | 12.9 | TDD | 392 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3240176 | 7 | 121.4736304534 | 31.1482321816 | 233 | 4 | 3 | 10.3 | FDD | 130 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3246960 | 3 | 121.4726046820 | 31.1545743042 | 249 | 2 | 8 | 8.8 | TDD | 844 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3247852 | 13 | 121.4675662345 | 31.1559609045 | 320 | 6 | 1 | 22.4 | FDD | 187 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3249755 | 8 | 121.4744590229 | 31.1509747368 | 147 | 7 | 9 | 1.5 | FDD | 397 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3256924 | 6 | 121.4731615222 | 31.1474196266 | 256 | 1 | 6 | 14.7 | TDD | 282 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3258069 | 5 | 121.4679230849 | 31.1549387202 | 37 | 3 | 12 | 25.4 | TDD | 53 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3262339 | 10 | 121.4680869209 | 31.1487343923 | 70 | 14 | 12 | 0.6 | FDD | 786 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3267436 | 4 | 121.4695682167 | 31.1482770566 | 208 | 9 | 0 | 12.7 | TDD | 528 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.461 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.478 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.581 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.581 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.263 | NREventA2 | measId:1;ServCellPCI:397;Se... |
| 2024-09-20 22:21:35.373 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.650 | NREventA5 | measId:3;ServCellPCI:397;Se... |
| 2024-09-20 22:21:35.681 | NRHandoverAttempt | SourcePCI:397;SourceNR-ARFC... |
| 2024-09-20 22:21:35.717 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.730 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.833 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.833 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215777 | 1 | 7.4243 | 11.4400 | -116.1398 | 16.4429 | 130.5800 | 0.0158 | 0.0018 |
| 2024_09_20 22:00 | 3224092 | 2 | 18.7288 | 5.3310 | -116.2845 | 19.1248 | 197.2016 | 0.0118 | 0.0190 |
| 2024_09_20 22:00 | 3246960 | 3 | 11.7008 | 18.9824 | -117.6072 | 7.4037 | 180.6966 | 0.0091 | 0.0160 |
| 2024_09_20 22:00 | 3267436 | 4 | 11.2308 | 5.0492 | -114.0461 | 9.2231 | 167.3650 | 0.0050 | 0.0018 |
| 2024_09_20 22:00 | 3258069 | 5 | 7.0727 | 16.8819 | -117.6012 | 18.0635 | 141.0612 | 0.0105 | 0.0114 |
| 2024_09_20 22:00 | 3256924 | 6 | 8.1611 | 7.2732 | -116.4218 | 18.1982 | 164.9790 | 0.0100 | 0.0058 |
| 2024_09_20 22:00 | 3240176 | 7 | 12.5681 | 18.3767 | -116.7738 | 3.1904 | 37.7884 | 0.0163 | 0.0035 |
| 2024_09_20 22:00 | 3249755 | 8 | 9.3211 | 17.8708 | -117.9291 | 3.4570 | 29.5599 | 0.0147 | 0.0022 |
| 2024_09_20 22:00 | 3212950 | 9 | 18.6273 | 19.8878 | -114.8672 | 4.3352 | 37.9263 | 0.0005 | 0.0025 |
| 2024_09_20 22:00 | 3262339 | 10 | 17.6811 | 18.8830 | -114.2122 | 3.5314 | 24.4322 | 0.0023 | 0.0145 |
| 2024_09_20 22:00 | 3212071 | 11 | 19.2196 | 15.6007 | -115.4627 | 3.7526 | 50.6741 | 0.0068 | 0.0040 |
| 2024_09_20 22:00 | 3221353 | 12 | 18.7984 | 7.9738 | -114.2438 | 4.8418 | 55.8303 | 0.0137 | 0.0073 |
| 2024_09_20 22:00 | 3247852 | 13 | 5.9149 | 9.8259 | -116.8292 | 4.5412 | 58.9064 | 0.0027 | 0.0007 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417069_182E7D3D | 504990 | 53 | -94.8 | 504990 | 844 | -92.0 | 504990 | 528 | -97.9 | 504990 | 392 |
| MR_1774417069_9401B4DD | 504990 | 53 | -96.3 | 504990 | 844 | -90.8 | 504990 | 528 | -98.1 | 504990 | 392 |
| MR_1774417069_3CF470ED | 504990 | 53 | -96.6 | 504990 | 844 | -90.0 | 504990 | 528 | -97.4 | 504990 | 392 |
| MR_1774417069_699BAC71 | 504990 | 53 | -96.8 | 504990 | 844 | -91.0 | 504990 | 528 | -97.3 | 504990 | 392 |
| MR_1774417069_B79969F5 | 504990 | 53 | -94.1 | 504990 | 844 | -90.3 | 504990 | 528 | -100.8 | 504990 | 392 |
| MR_1774417069_528ECDF3 | 152650 | 82 | -86.9 | 152650 | 786 | -91.7 | 152650 | 130 | -95.1 | 152650 | 215 |
| MR_1774417069_481CFAF0 | 504990 | 53 | -94.2 | 504990 | 844 | -92.5 | 504990 | 528 | -100.9 | 504990 | 392 |
| MR_1774417069_57574B75 | 504990 | 53 | -97.2 | 504990 | 844 | -90.5 | 504990 | 528 | -99.6 | 504990 | 392 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1871: `84e4a106-091...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `84e4a106-0914-4853-9e40-3d2ce02c675f` |
| Tag | **multiple-answer** |
| 정답 | **C7|C12|C17|C19** |
| C7 의미 | Press down the tilt angle  of 3238005_4 by 5 degrees |
| C12 의미 | Increase A3 Offset threshold for 3238005_4 |
| C17 의미 | Increase A3 Offset threshold for 3250926_1 |
| C19 의미 | Decrease transmission power for 3238005_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1871] topology](images/train_1871.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3250926_1 and 3238005_4
- `C2`: Adjust the azimuth of 3238005_4 by 28 degrees
- `C3`: Add neighbor relationship between 3216597_3 and 3238005_4
- `C4`: Decrease transmission power for 3250926_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250926_1
- `C6`: Decrease A3 Offset threshold for 3238005_4
- `C7`: Press down the tilt angle  of 3238005_4 by 5 degrees **← 정답**
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238005_4
- `C9`: Decrease A3 Offset threshold for 3250926_1
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Adjust the azimuth of 3250926_1 by 5 degrees
- `C12`: Increase A3 Offset threshold for 3238005_4 **← 정답**
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238005_4
- `C14`: Increase transmission power for 3250926_1
- `C15`: Lift the tilt angle of 3250926_1 by 6 degrees
- `C16`: Increase transmission power for 3238005_4
- `C17`: Increase A3 Offset threshold for 3250926_1 **← 정답**
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250926_1
- `C19`: Decrease transmission power for 3238005_4 **← 정답**
- `C20`: Check test server and transmission issues
- `C21`: Lift the tilt angle  of 3238005_4 by 5 degrees
- `C22`: Press down the tilt angle of 3250926_1 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.299 | MS1 | 121.4656608371 | 31.1446215700 | 804 | 504990 | -75.87 | 16.63 | 508.60 | 0.09 | 2.42 | 1570 |
| 2024-09-20 22:21:32.998 | MS1 | 121.4656672496 | 31.1446254155 | 804 | 504990 | -81.09 | 15.71 | 422.13 | 0.06 | 2.25 | 1595 |
| 2024-09-20 22:21:33.125 | MS1 | 121.4656707377 | 31.1446206567 | 804 | 504990 | -81.56 | 12.45 | 513.63 | 0.13 | 2.12 | 1592 |
| 2024-09-20 22:21:34.252 | MS1 | 121.4656751607 | 31.1446254938 | 5 | 504990 | -83.19 | 1.59 | 46.76 | 0.06 | 1.22 | 1592 |
| 2024-09-20 22:21:35.178 | MS1 | 121.4656618843 | 31.1446236176 | 5 | 504990 | -89.45 | 4.31 | 25.34 | 0.09 | 1.17 | 1578 |
| 2024-09-20 22:21:36.601 | MS1 | 121.4656599636 | 31.1446212400 | 804 | 504990 | -87.10 | 1.07 | 70.11 | 0.02 | 1.29 | 1566 |
| 2024-09-20 22:21:37.505 | MS1 | 121.4656581527 | 31.1446309284 | 804 | 504990 | -85.75 | 3.68 | 31.25 | 0.03 | 1.08 | 1562 |
| 2024-09-20 22:21:38.275 | MS1 | 121.4656655775 | 31.1446183370 | 5 | 504990 | -82.25 | 1.83 | 35.90 | 0.11 | 1.15 | 1571 |
| 2024-09-20 22:21:39.511 | MS1 | 121.4656772809 | 31.1446314354 | 5 | 504990 | -85.36 | 1.87 | 77.08 | 0.13 | 1.47 | 1588 |
| 2024-09-20 22:21:40.607 | MS1 | 121.4656604305 | 31.1446319819 | 5 | 504990 | -77.20 | 15.61 | 602.92 | 0.09 | 2.73 | 1584 |
| 2024-09-20 22:21:41.787 | MS1 | 121.4656580315 | 31.1446191056 | 5 | 504990 | -81.99 | 12.06 | 354.70 | 0.11 | 2.15 | 1589 |
| 2024-09-20 22:21:42.194 | MS1 | 121.4656589219 | 31.1446232845 | 5 | 504990 | -78.96 | 16.43 | 562.79 | 0.06 | 2.17 | 1596 |

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
| 3216597 | 3 | 121.4724924816 | 31.1469703953 | 238 | 14 | 1 | 20.4 | TDD | 839 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3233089 | 5 | 121.4757442187 | 31.1529304461 | 27 | 7 | 4 | 17.6 | TDD | 342 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3238005 | 4 | 121.4731084893 | 31.1494479487 | 261 | 3 | 1 | 33.1 | TDD | 946 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3241414 | 2 | 121.4722485533 | 31.1516130715 | 42 | 0 | 10 | 41.3 | TDD | 5 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3250926 | 1 | 121.4703356236 | 31.1546801337 | 197 | 5 | 8 | 19.1 | TDD | 804 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.553 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.578 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.703 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.703 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.445 | NREventA3 | measId:2;ServCellPCI:128;Se... |
| 2024-09-20 22:21:34.685 | NRHandoverAttempt | SourcePCI:128;SourceNR-ARFC... |
| 2024-09-20 22:21:34.731 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.743 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:34.865 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.865 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.445 | NREventA3 | measId:2;ServCellPCI:735;Se... |
| 2024-09-20 22:21:36.685 | NRHandoverAttempt | SourcePCI:735;SourceNR-ARFC... |
| 2024-09-20 22:21:36.726 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.739 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.863 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.863 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.445 | NREventA3 | measId:2;ServCellPCI:128;Se... |
| 2024-09-20 22:21:38.685 | NRHandoverAttempt | SourcePCI:128;SourceNR-ARFC... |
| 2024-09-20 22:21:38.717 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.727 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.846 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.846 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250926 | 1 | 16.3634 | 12.2192 | -117.1305 | 14.3929 | 187.0289 | 0.0034 | 0.0085 |
| 2024_09_20 22:00 | 3241414 | 2 | 18.8681 | 9.4652 | -117.3313 | 19.3710 | 183.9513 | 0.0058 | 0.0001 |
| 2024_09_20 22:00 | 3216597 | 3 | 10.5025 | 9.5288 | -117.8304 | 8.3218 | 179.0724 | 0.0049 | 0.0170 |
| 2024_09_20 22:00 | 3238005 | 4 | 19.8527 | 8.5181 | -116.1771 | 19.3341 | 192.1785 | 0.0061 | 0.0015 |
| 2024_09_20 22:00 | 3233089 | 5 | 11.4686 | 17.7969 | -116.7031 | 15.2869 | 150.3737 | 0.0074 | 0.0118 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415908_DA6B6198 | 504990 | 804 | -81.8 | 504990 | 5 | -79.6 | 504990 | 946 | -81.9 | 504990 | 839 |
| MR_1774415908_0703258D | 504990 | 804 | -82.2 | 504990 | 5 | -80.8 | 504990 | 946 | -81.8 | 504990 | 839 |
| MR_1774415908_72D4EF3A | 504990 | 5 | -82.8 | 504990 | 804 | -80.7 | 504990 | 946 | -83.4 | 504990 | 839 |
| MR_1774415908_CC7D24AE | 504990 | 5 | -84.9 | 504990 | 804 | -79.3 | 504990 | 946 | -82.7 | 504990 | 839 |
| MR_1774415908_40C52D17 | 504990 | 804 | -81.6 | 504990 | 5 | -81.2 | 504990 | 946 | -82.7 | 504990 | 839 |
| MR_1774415908_D8B55664 | 504990 | 804 | -85.0 | 504990 | 5 | -82.4 | 504990 | 946 | -82.4 | 504990 | 839 |
| MR_1774415908_68938593 | 504990 | 5 | -84.0 | 504990 | 804 | -81.3 | 504990 | 946 | -80.3 | 504990 | 839 |
| MR_1774415908_977DD458 | 504990 | 5 | -84.6 | 504990 | 804 | -80.6 | 504990 | 946 | -83.1 | 504990 | 839 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1872: `80be75ea-bfd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `80be75ea-bfd3-4bbe-96a6-eddc77e837a5` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234253_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1872] topology](images/train_1872.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3234253_3
- `C2`: Increase A3 Offset threshold for 3234253_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234253_3 **← 정답**
- `C4`: Decrease transmission power for 3224408_6
- `C5`: Decrease A3 Offset threshold for 3224408_6
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234253_3
- `C7`: Increase A3 Offset threshold for 3224408_6
- `C8`: Lift the tilt angle  of 3224408_6 by 4 degrees
- `C9`: Check test server and transmission issues
- `C10`: Press down the tilt angle of 3234253_3 by 5 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Lift the tilt angle of 3234253_3 by 5 degrees
- `C13`: Add neighbor relationship between 3234253_3 and 3224408_6
- `C14`: Adjust the azimuth of 3234253_3 by 4 degrees
- `C15`: Adjust the azimuth of 3224408_6 by 18 degrees
- `C16`: Increase transmission power for 3224408_6
- `C17`: Decrease transmission power for 3234253_3
- `C18`: Decrease A3 Offset threshold for 3234253_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224408_6
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224408_6
- `C21`: Press down the tilt angle  of 3224408_6 by 4 degrees
- `C22`: Add neighbor relationship between 3278478_8 and 3224408_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.661 | MS1 | 121.4656583179 | 31.1446265858 | 392 | 504990 | -93.45 | 13.57 | 382.79 | 0.10 | 2.30 | 1566 |
| 2024-09-20 22:21:32.772 | MS1 | 121.4656735850 | 31.1446330856 | 97 | 504990 | -93.07 | 9.97 | 310.52 | 0.12 | 2.60 | 1576 |
| 2024-09-20 22:21:33.868 | MS1 | 121.4656746644 | 31.1446379538 | 467 | 504990 | -93.88 | 10.09 | 567.65 | 0.09 | 2.70 | 1575 |
| 2024-09-20 22:21:34.895 | MS1 | 121.4656699057 | 31.1446230285 | 404 | 152650 | -93.27 | 7.78 | 76.94 | 0.10 | 1.77 | 952 |
| 2024-09-20 22:21:35.675 | MS1 | 121.4656615619 | 31.1446266133 | 240 | 152650 | -94.98 | 5.35 | 45.14 | 0.05 | 1.56 | 982 |
| 2024-09-20 22:21:36.708 | MS1 | 121.4656746781 | 31.1446266515 | 451 | 152650 | -95.00 | 3.14 | 79.19 | 0.08 | 1.96 | 957 |
| 2024-09-20 22:21:37.358 | MS1 | 121.4656750346 | 31.1446246995 | 603 | 152650 | -90.89 | 2.84 | 106.42 | 0.19 | 1.55 | 963 |
| 2024-09-20 22:21:38.140 | MS1 | 121.4656621610 | 31.1446369616 | 404 | 152650 | -88.11 | 4.89 | 84.18 | 0.09 | 1.94 | 998 |
| 2024-09-20 22:21:39.518 | MS1 | 121.4656665843 | 31.1446202567 | 240 | 152650 | -95.11 | 2.39 | 87.70 | 0.19 | 1.97 | 909 |
| 2024-09-20 22:21:40.525 | MS1 | 121.4656720043 | 31.1446210091 | 451 | 152650 | -94.81 | 2.03 | 96.51 | 0.11 | 2.30 | 1564 |
| 2024-09-20 22:21:41.806 | MS1 | 121.4656703554 | 31.1446316491 | 603 | 152650 | -91.01 | 6.24 | 75.29 | 0.19 | 2.35 | 1580 |
| 2024-09-20 22:21:42.898 | MS1 | 121.4656778281 | 31.1446305509 | 404 | 152650 | -90.89 | 7.50 | 57.14 | 0.03 | 2.30 | 1598 |

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
| 3224408 | 6 | 121.4722542612 | 31.1516544250 | 237 | 3 | 1 | 16.6 | TDD | 696 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3229455 | 12 | 121.4675209785 | 31.1503562343 | 347 | 4 | 0 | 26.2 | FDD | 980 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3234253 | 3 | 121.4658227186 | 31.1532832327 | 185 | 4 | 1 | 14.0 | TDD | 392 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3235357 | 1 | 121.4759516875 | 31.1445022958 | 9 | 11 | 0 | 16.0 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3237936 | 4 | 121.4693571472 | 31.1491155462 | 46 | 4 | 10 | 22.2 | TDD | 467 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3247233 | 2 | 121.4702509623 | 31.1464448060 | 203 | 12 | 2 | 18.4 | TDD | 97 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3251581 | 10 | 121.4668776349 | 31.1505341140 | 290 | 12 | 2 | 9.1 | FDD | 240 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3252901 | 7 | 121.4756540793 | 31.1478637565 | 63 | 0 | 6 | 24.2 | FDD | 737 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3253793 | 9 | 121.4735150841 | 31.1515175179 | 27 | 9 | 10 | 14.3 | FDD | 231 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3265621 | 11 | 121.4753161670 | 31.1545017916 | 263 | 10 | 1 | 13.4 | FDD | 404 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3270109 | 13 | 121.4640294841 | 31.1529678415 | 21 | 7 | 7 | 24.2 | FDD | 603 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3270912 | 5 | 121.4691881445 | 31.1555082101 | 197 | 5 | 2 | 10.4 | TDD | 789 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3278478 | 8 | 121.4722416809 | 31.1462369829 | 171 | 9 | 9 | 25.1 | FDD | 451 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |

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
| 2024-09-20 22:21:31.467 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.487 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.628 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.628 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.360 | NREventA2 | measId:1;ServCellPCI:226;Se... |
| 2024-09-20 22:21:35.461 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.717 | NREventA5 | measId:3;ServCellPCI:226;Se... |
| 2024-09-20 22:21:35.789 | NRHandoverAttempt | SourcePCI:226;SourceNR-ARFC... |
| 2024-09-20 22:21:35.826 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.839 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.944 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.944 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235357 | 1 | 5.7992 | 8.0588 | -116.9770 | 8.8350 | 154.6028 | 0.0061 | 0.0123 |
| 2024_09_20 22:00 | 3247233 | 2 | 16.3091 | 5.0097 | -116.8227 | 11.8982 | 89.6225 | 0.0107 | 0.0124 |
| 2024_09_20 22:00 | 3234253 | 3 | 6.3097 | 6.4451 | -114.0743 | 6.6926 | 108.2421 | 0.0192 | 0.0165 |
| 2024_09_20 22:00 | 3237936 | 4 | 16.2200 | 19.5064 | -116.5335 | 6.2251 | 125.5666 | 0.0197 | 0.0057 |
| 2024_09_20 22:00 | 3270912 | 5 | 8.3839 | 12.5335 | -117.6086 | 14.1946 | 176.0808 | 0.0066 | 0.0141 |
| 2024_09_20 22:00 | 3224408 | 6 | 5.9921 | 18.5441 | -116.6343 | 16.3041 | 89.7625 | 0.0160 | 0.0053 |
| 2024_09_20 22:00 | 3252901 | 7 | 9.0224 | 10.9443 | -117.7814 | 3.1102 | 42.8352 | 0.0020 | 0.0165 |
| 2024_09_20 22:00 | 3278478 | 8 | 11.6528 | 18.3600 | -114.6370 | 4.7562 | 42.4786 | 0.0059 | 0.0148 |
| 2024_09_20 22:00 | 3253793 | 9 | 16.5055 | 9.6447 | -116.6804 | 3.0994 | 38.0985 | 0.0092 | 0.0084 |
| 2024_09_20 22:00 | 3251581 | 10 | 14.1536 | 9.6081 | -115.0328 | 3.0819 | 32.7400 | 0.0172 | 0.0107 |
| 2024_09_20 22:00 | 3265621 | 11 | 7.6840 | 11.9226 | -117.4998 | 4.2885 | 41.9461 | 0.0188 | 0.0134 |
| 2024_09_20 22:00 | 3229455 | 12 | 18.5697 | 12.6254 | -116.9245 | 4.4047 | 46.7048 | 0.0151 | 0.0049 |
| 2024_09_20 22:00 | 3270109 | 13 | 10.5556 | 10.4754 | -114.2017 | 3.6103 | 57.5192 | 0.0033 | 0.0131 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414116_09816F8F | 152650 | 404 | -94.7 | 152650 | 231 | -100.1 | 152650 | 980 | -102.7 | 152650 | 737 |
| MR_1774414116_7408624C | 504990 | 467 | -93.5 | 504990 | 696 | -95.5 | 504990 | 248 | -97.5 | 504990 | 789 |
| MR_1774414116_63FF47F5 | 504990 | 467 | -94.2 | 504990 | 696 | -97.1 | 504990 | 248 | -95.5 | 504990 | 789 |
| MR_1774414116_6B1BA34B | 504990 | 467 | -93.1 | 504990 | 696 | -96.1 | 504990 | 248 | -96.7 | 504990 | 789 |
| MR_1774414116_9FA3F593 | 152650 | 404 | -92.2 | 152650 | 231 | -98.1 | 152650 | 980 | -103.8 | 152650 | 737 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1873: `4bac8bb1-11f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4bac8bb1-11f9-4061-a322-bf097cbcd078` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Lift the tilt angle  of 3248460_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1873] topology](images/train_1873.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3249476_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249476_2
- `C3`: Decrease A3 Offset threshold for 3249476_2
- `C4`: Lift the tilt angle  of 3248460_3 by 10 degrees **← 정답**
- `C5`: Increase transmission power for 3249476_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278406_4
- `C7`: Decrease A3 Offset threshold for 3278406_4
- `C8`: Adjust the azimuth of 3278406_4 by 36 degrees
- `C9`: Add neighbor relationship between 3278406_4 and 3249476_2
- `C10`: Increase A3 Offset threshold for 3278406_4
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Check test server and transmission issues
- `C13`: Decrease transmission power for 3278406_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278406_4
- `C15`: Press down the tilt angle of 3278406_4 by 2 degrees
- `C16`: Press down the tilt angle  of 3248460_3 by 10 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249476_2
- `C18`: Adjust the azimuth of 3248460_3 by 4 degrees
- `C19`: Increase transmission power for 3278406_4
- `C20`: Add neighbor relationship between 3248460_3 and 3249476_2
- `C21`: Lift the tilt angle of 3278406_4 by 2 degrees
- `C22`: Increase A3 Offset threshold for 3249476_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.562 | MS1 | 121.4656740480 | 31.1446289136 | 743 | 504990 | -86.63 | 12.08 | 407.12 | 0.16 | 2.22 | 1599 |
| 2024-09-20 22:21:32.714 | MS1 | 121.4656654290 | 31.1446195812 | 743 | 504990 | -87.89 | 15.41 | 306.45 | 0.11 | 2.09 | 1588 |
| 2024-09-20 22:21:33.797 | MS1 | 121.4656715959 | 31.1446302063 | 743 | 504990 | -87.91 | 14.16 | 388.28 | 0.12 | 2.22 | 1569 |
| 2024-09-20 22:21:34.896 | MS1 | 121.4656651134 | 31.1446339492 | 743 | 504990 | -86.86 | 13.15 | 57.33 | 0.18 | 2.15 | 1568 |
| 2024-09-20 22:21:35.937 | MS1 | 121.4656754728 | 31.1446281744 | 743 | 504990 | -89.23 | 16.75 | 68.86 | 0.05 | 2.87 | 1588 |
| 2024-09-20 22:21:36.893 | MS1 | 121.4656716282 | 31.1446349049 | 743 | 504990 | -88.94 | 15.23 | 95.67 | 0.12 | 2.50 | 1564 |
| 2024-09-20 22:21:37.220 | MS1 | 121.4656768706 | 31.1446313991 | 743 | 504990 | -89.00 | 11.86 | 74.91 | 0.12 | 2.18 | 1590 |
| 2024-09-20 22:21:38.935 | MS1 | 121.4656757434 | 31.1446367295 | 743 | 504990 | -92.13 | 8.30 | 73.54 | 0.04 | 2.38 | 1585 |
| 2024-09-20 22:21:39.569 | MS1 | 121.4656706529 | 31.1446370745 | 743 | 504990 | -92.27 | 9.01 | 72.11 | 0.15 | 2.07 | 1600 |
| 2024-09-20 22:21:40.187 | MS1 | 121.4656773104 | 31.1446270090 | 743 | 504990 | -90.98 | 11.72 | 449.93 | 0.07 | 2.86 | 1593 |
| 2024-09-20 22:21:41.787 | MS1 | 121.4656634973 | 31.1446268998 | 743 | 504990 | -91.63 | 9.12 | 586.28 | 0.12 | 2.83 | 1595 |
| 2024-09-20 22:21:42.914 | MS1 | 121.4656628036 | 31.1446180757 | 743 | 504990 | -91.02 | 8.70 | 538.58 | 0.05 | 2.38 | 1573 |

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
| 3228082 | 1 | 121.4714417674 | 31.1536536187 | 222 | 12 | 5 | 38.3 | TDD | 808 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3248460 | 3 | 121.4642033200 | 31.1478932685 | 104 | 12 | 9 | 19.1 | TDD | 419 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3249476 | 2 | 121.4640971379 | 31.1461718722 | 143 | 12 | 4 | 40.6 | TDD | 227 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3278406 | 4 | 121.4749896768 | 31.1487541636 | 207 | 1 | 3 | 22.8 | TDD | 743 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.805 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.828 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.959 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.959 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.623 | NREventA3 | measId:2;ServCellPCI:41;Ser... |
| 2024-09-20 22:21:37.863 | NRHandoverAttempt | SourcePCI:41;SourceNR-ARFCN... |
| 2024-09-20 22:21:37.898 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.910 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.013 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.013 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228082 | 1 | 6.7460 | 11.5996 | -114.2192 | 18.3378 | 108.0689 | 0.0049 | 0.0128 |
| 2024_09_20 22:00 | 3249476 | 2 | 8.8383 | 7.1204 | -117.9235 | 6.8364 | 157.0265 | 0.0057 | 0.0067 |
| 2024_09_20 22:00 | 3248460 | 3 | 18.8748 | 12.7542 | -115.7887 | 6.6111 | 113.3111 | 0.0068 | 0.0142 |
| 2024_09_20 22:00 | 3278406 | 4 | 76.6474 | 89.5514 | -114.1344 | 12.7646 | 148.6676 | 0.0175 | 0.0153 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415925_2851BC14 | 504990 | 743 | -85.0 | 504990 | 227 | -94.7 | 504990 | 419 | -98.0 | 504990 | 808 |
| MR_1774415925_C3EFED8D | 504990 | 743 | -88.7 | 504990 | 227 | -93.4 | 504990 | 419 | -100.1 | 504990 | 808 |
| MR_1774415925_0B4EA06B | 504990 | 743 | -87.7 | 504990 | 227 | -96.5 | 504990 | 419 | -98.2 | 504990 | 808 |
| MR_1774415925_27AA210A | 504990 | 743 | -88.3 | 504990 | 227 | -95.4 | 504990 | 419 | -99.7 | 504990 | 808 |
| MR_1774415925_504A4E17 | 504990 | 743 | -85.4 | 504990 | 227 | -96.7 | 504990 | 419 | -98.7 | 504990 | 808 |
| MR_1774415925_121A37D0 | 504990 | 743 | -86.6 | 504990 | 227 | -95.3 | 504990 | 419 | -98.0 | 504990 | 808 |
| MR_1774415925_B6402ACF | 504990 | 743 | -85.2 | 504990 | 227 | -93.9 | 504990 | 419 | -97.9 | 504990 | 808 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1874: `eb1bfdff-968...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `eb1bfdff-9683-4c8a-9b90-6dbaaf78f641` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1874] topology](images/train_1874.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3231605_4 by 50 degrees
- `C2`: Decrease transmission power for 3231605_4
- `C3`: Press down the tilt angle  of 3267150_3 by 10 degrees
- `C4`: Decrease A3 Offset threshold for 3231605_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267150_3
- `C6`: Decrease A3 Offset threshold for 3267150_3
- `C7`: Increase A3 Offset threshold for 3267150_3
- `C8`: Lift the tilt angle  of 3267150_3 by 10 degrees
- `C9`: Add neighbor relationship between 3214277_2 and 3267150_3
- `C10`: Increase transmission power for 3267150_3
- `C11`: Lift the tilt angle of 3231605_4 by 9 degrees
- `C12`: Press down the tilt angle of 3231605_4 by 9 degrees
- `C13`: Adjust the azimuth of 3267150_3 by 6 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231605_4
- `C15`: Add neighbor relationship between 3231605_4 and 3267150_3
- `C16`: Decrease transmission power for 3267150_3
- `C17`: Check test server and transmission issues
- `C18`: Increase transmission power for 3231605_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231605_4
- `C20`: Increase A3 Offset threshold for 3231605_4
- `C21`: Insufficient data; more data is needed for judgment. **← 정답**
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267150_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.366 | MS1 | 121.4656749402 | 31.1446308010 | 957 | 504990 | -90.77 | 17.98 | 489.94 | 0.08 | 2.91 | 1575 |
| 2024-09-20 22:21:32.858 | MS1 | 121.4656587525 | 31.1446262152 | 957 | 504990 | -86.35 | 12.60 | 490.77 | 0.09 | 2.58 | 1599 |
| 2024-09-20 22:21:33.272 | MS1 | 121.4656698601 | 31.1446334545 | 957 | 504990 | -87.81 | 15.24 | 419.17 | 0.13 | 2.98 | 1576 |
| 2024-09-20 22:21:34.897 | MS1 | 121.4656695416 | 31.1446362360 | 957 | 504990 | -87.69 | 15.64 | 68.53 | 0.15 | 2.11 | 1565 |
| 2024-09-20 22:21:35.439 | MS1 | 121.4656635683 | 31.1446199007 | 957 | 504990 | -90.48 | 15.37 | 81.34 | 0.00 | 2.44 | 1572 |
| 2024-09-20 22:21:36.255 | MS1 | 121.4656604535 | 31.1446267556 | 957 | 504990 | -85.66 | 12.15 | 80.37 | 0.04 | 2.60 | 1583 |
| 2024-09-20 22:21:37.787 | MS1 | 121.4656634746 | 31.1446372222 | 957 | 504990 | -91.56 | 7.51 | 52.38 | 0.10 | 2.65 | 1583 |
| 2024-09-20 22:21:38.550 | MS1 | 121.4656705871 | 31.1446186787 | 957 | 504990 | -93.47 | 11.56 | 63.13 | 0.09 | 2.66 | 1599 |
| 2024-09-20 22:21:39.870 | MS1 | 121.4656718832 | 31.1446236963 | 957 | 504990 | -91.60 | 10.97 | 63.26 | 0.14 | 2.89 | 1568 |
| 2024-09-20 22:21:40.324 | MS1 | 121.4656601426 | 31.1446266222 | 957 | 504990 | -89.07 | 12.62 | 306.16 | 0.08 | 2.10 | 1560 |
| 2024-09-20 22:21:41.242 | MS1 | 121.4656596878 | 31.1446269526 | 957 | 504990 | -92.88 | 10.90 | 561.25 | 0.11 | 2.31 | 1595 |
| 2024-09-20 22:21:42.685 | MS1 | 121.4656656982 | 31.1446228718 | 957 | 504990 | -89.53 | 8.64 | 342.31 | 0.06 | 2.77 | 1585 |

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
| 3214277 | 2 | 121.4652074238 | 31.1480791482 | 160 | 9 | 11 | 36.1 | TDD | 121 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3231605 | 4 | 121.4752265969 | 31.1522483218 | 284 | 8 | 9 | 15.6 | TDD | 957 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3263694 | 1 | 121.4726019573 | 31.1506084321 | 217 | 11 | 8 | 49.7 | TDD | 616 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3267150 | 3 | 121.4686693043 | 31.1457821455 | 252 | 12 | 11 | 46.9 | TDD | 93 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.505 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.529 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.664 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.664 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.399 | NREventA3 | measId:2;ServCellPCI:265;Se... |
| 2024-09-20 22:21:38.639 | NRHandoverAttempt | SourcePCI:265;SourceNR-ARFC... |
| 2024-09-20 22:21:38.676 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.690 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.802 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.802 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3263694 | 1 | 88.0178 | 84.3855 | -114.2470 | 16.6535 | 158.1988 | 0.0195 | 0.0162 |
| 2024_09_19 22:00 | 3214277 | 2 | 77.2530 | 81.1430 | -117.9934 | 11.2532 | 189.6544 | 0.0000 | 0.0092 |
| 2024_09_19 22:00 | 3267150 | 3 | 77.1827 | 84.3953 | -114.2957 | 11.1990 | 87.1086 | 0.0106 | 0.0116 |
| 2024_09_19 22:00 | 3231605 | 4 | 88.0589 | 86.1702 | -114.2153 | 16.3000 | 82.6076 | 0.0185 | 0.0036 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416408_1E0C9C9F | 504990 | 957 | -87.7 | 504990 | 93 | -89.5 | 504990 | 121 | -99.8 | 504990 | 616 |
| MR_1774416408_B7FB3F7B | 504990 | 957 | -89.5 | 504990 | 93 | -89.3 | 504990 | 121 | -99.8 | 504990 | 616 |
| MR_1774416408_699E06B4 | 504990 | 957 | -87.1 | 504990 | 93 | -89.0 | 504990 | 121 | -98.9 | 504990 | 616 |
| MR_1774416408_608C1F62 | 504990 | 957 | -87.1 | 504990 | 93 | -88.0 | 504990 | 121 | -96.5 | 504990 | 616 |
| MR_1774416408_445E23CE | 504990 | 957 | -89.4 | 504990 | 93 | -87.9 | 504990 | 121 | -99.8 | 504990 | 616 |
| MR_1774416408_F8ED83C1 | 504990 | 957 | -87.3 | 504990 | 93 | -86.0 | 504990 | 121 | -98.8 | 504990 | 616 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1875: `0a950fec-131...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0a950fec-1319-41f7-8818-986ada007fba` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Lift the tilt angle  of 3225806_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1875] topology](images/train_1875.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3225806_4 by 10 degrees **← 정답**
- `C2`: Increase transmission power for 3268043_1
- `C3`: Adjust the azimuth of 3274185_2 by 12 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268043_1
- `C5`: Decrease transmission power for 3268043_1
- `C6`: Decrease A3 Offset threshold for 3268043_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268043_1
- `C8`: Increase A3 Offset threshold for 3268043_1
- `C9`: Add neighbor relationship between 3274185_2 and 3268043_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274185_2
- `C11`: Increase A3 Offset threshold for 3274185_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Increase transmission power for 3274185_2
- `C14`: Check test server and transmission issues
- `C15`: Press down the tilt angle  of 3225806_4 by 10 degrees
- `C16`: Decrease transmission power for 3274185_2
- `C17`: Lift the tilt angle of 3274185_2 by 5 degrees
- `C18`: Press down the tilt angle of 3274185_2 by 5 degrees
- `C19`: Adjust the azimuth of 3225806_4 by 23 degrees
- `C20`: Decrease A3 Offset threshold for 3274185_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274185_2
- `C22`: Add neighbor relationship between 3225806_4 and 3268043_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.738 | MS1 | 121.4656647404 | 31.1446337355 | 306 | 504990 | -85.11 | 12.74 | 422.00 | 0.07 | 2.18 | 1596 |
| 2024-09-20 22:21:32.197 | MS1 | 121.4656583464 | 31.1446347442 | 306 | 504990 | -87.09 | 13.44 | 310.95 | 0.15 | 2.02 | 1600 |
| 2024-09-20 22:21:33.875 | MS1 | 121.4656727169 | 31.1446301672 | 306 | 504990 | -89.31 | 17.43 | 454.36 | 0.01 | 2.01 | 1589 |
| 2024-09-20 22:21:34.633 | MS1 | 121.4656613420 | 31.1446183154 | 306 | 504990 | -85.88 | 13.55 | 52.41 | 0.14 | 2.14 | 1600 |
| 2024-09-20 22:21:35.134 | MS1 | 121.4656723263 | 31.1446199790 | 306 | 504990 | -90.41 | 15.16 | 108.38 | 0.12 | 2.72 | 1584 |
| 2024-09-20 22:21:36.439 | MS1 | 121.4656620449 | 31.1446314474 | 306 | 504990 | -85.09 | 15.55 | 106.71 | 0.20 | 2.27 | 1595 |
| 2024-09-20 22:21:37.211 | MS1 | 121.4656742087 | 31.1446359271 | 306 | 504990 | -90.70 | 8.80 | 67.47 | 0.01 | 2.21 | 1586 |
| 2024-09-20 22:21:38.951 | MS1 | 121.4656662907 | 31.1446366215 | 306 | 504990 | -90.63 | 8.80 | 63.79 | 0.04 | 2.25 | 1580 |
| 2024-09-20 22:21:39.916 | MS1 | 121.4656639567 | 31.1446235691 | 306 | 504990 | -93.47 | 9.33 | 79.97 | 0.12 | 2.14 | 1572 |
| 2024-09-20 22:21:40.800 | MS1 | 121.4656595875 | 31.1446281110 | 306 | 504990 | -92.27 | 10.58 | 344.51 | 0.06 | 2.33 | 1584 |
| 2024-09-20 22:21:41.556 | MS1 | 121.4656728724 | 31.1446302921 | 306 | 504990 | -91.90 | 12.41 | 597.96 | 0.06 | 2.97 | 1579 |
| 2024-09-20 22:21:42.963 | MS1 | 121.4656772220 | 31.1446223655 | 306 | 504990 | -91.43 | 12.59 | 441.96 | 0.18 | 2.08 | 1562 |

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
| 3216318 | 3 | 121.4743498633 | 31.1506719519 | 126 | 12 | 8 | 28.8 | TDD | 755 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3225806 | 4 | 121.4755470356 | 31.1441683889 | 331 | 10 | 3 | 17.8 | TDD | 495 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3268043 | 1 | 121.4668436391 | 31.1466983478 | 229 | 6 | 10 | 36.1 | TDD | 417 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3274185 | 2 | 121.4671600297 | 31.1483393499 | 187 | 2 | 5 | 19.2 | TDD | 306 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.606 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.711 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.711 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.460 | NREventA3 | measId:2;ServCellPCI:790;Se... |
| 2024-09-20 22:21:38.700 | NRHandoverAttempt | SourcePCI:790;SourceNR-ARFC... |
| 2024-09-20 22:21:38.741 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.754 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.878 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.878 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268043 | 1 | 19.9331 | 11.6988 | -115.1850 | 13.0176 | 144.2928 | 0.0095 | 0.0171 |
| 2024_09_20 22:00 | 3274185 | 2 | 76.7684 | 75.6646 | -117.1559 | 15.1664 | 175.1725 | 0.0179 | 0.0075 |
| 2024_09_20 22:00 | 3216318 | 3 | 14.3560 | 5.7584 | -115.6771 | 6.3405 | 167.3746 | 0.0101 | 0.0194 |
| 2024_09_20 22:00 | 3225806 | 4 | 11.8021 | 15.8780 | -115.8400 | 11.0689 | 190.8723 | 0.0172 | 0.0154 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417018_B9A1E163 | 504990 | 306 | -84.4 | 504990 | 417 | -90.0 | 504990 | 495 | -93.8 | 504990 | 755 |
| MR_1774417018_96889045 | 504990 | 306 | -85.3 | 504990 | 417 | -90.0 | 504990 | 495 | -95.7 | 504990 | 755 |
| MR_1774417018_CB3C962A | 504990 | 306 | -87.6 | 504990 | 417 | -90.0 | 504990 | 495 | -93.4 | 504990 | 755 |
| MR_1774417018_61248266 | 504990 | 306 | -85.9 | 504990 | 417 | -90.8 | 504990 | 495 | -93.8 | 504990 | 755 |
| MR_1774417018_B969A9FE | 504990 | 306 | -84.0 | 504990 | 417 | -88.4 | 504990 | 495 | -94.5 | 504990 | 755 |
| MR_1774417018_32402C5E | 504990 | 306 | -84.2 | 504990 | 417 | -89.4 | 504990 | 495 | -95.3 | 504990 | 755 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1876: `a7276ee3-83e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a7276ee3-83ea-4bd3-b404-e27d6759079e` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1876] topology](images/train_1876.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257870_2
- `C2`: Decrease transmission power for 3239158_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257870_2
- `C4`: Lift the tilt angle  of 3239158_1 by 2 degrees
- `C5`: Decrease A3 Offset threshold for 3239158_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239158_1
- `C7`: Add neighbor relationship between 3257870_2 and 3239158_1
- `C8`: Adjust the azimuth of 3257870_2 by 50 degrees
- `C9`: Check test server and transmission issues **← 정답**
- `C10`: Adjust the azimuth of 3239158_1 by 50 degrees
- `C11`: Increase A3 Offset threshold for 3239158_1
- `C12`: Increase transmission power for 3239158_1
- `C13`: Press down the tilt angle  of 3239158_1 by 2 degrees
- `C14`: Decrease A3 Offset threshold for 3257870_2
- `C15`: Increase transmission power for 3257870_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Lift the tilt angle of 3257870_2 by 10 degrees
- `C18`: Increase A3 Offset threshold for 3257870_2
- `C19`: Press down the tilt angle of 3257870_2 by 10 degrees
- `C20`: Add neighbor relationship between 3211594_3 and 3239158_1
- `C21`: Decrease transmission power for 3257870_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239158_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.731 | MS1 | 121.4656730488 | 31.1446317526 | 972 | 504990 | -89.08 | 15.47 | 580.83 | 0.08 | 2.10 | 1572 |
| 2024-09-20 22:21:32.488 | MS1 | 121.4656597299 | 31.1446276970 | 972 | 504990 | -91.13 | 14.96 | 351.80 | 0.15 | 2.92 | 1593 |
| 2024-09-20 22:21:33.713 | MS1 | 121.4656689492 | 31.1446326117 | 972 | 504990 | -89.10 | 17.99 | 542.08 | 0.04 | 2.66 | 1584 |
| 2024-09-20 22:21:34.200 | MS1 | 121.4656767637 | 31.1446243233 | 972 | 504990 | -89.48 | 16.63 | 58.59 | 0.04 | 2.10 | 315 |
| 2024-09-20 22:21:35.997 | MS1 | 121.4656648297 | 31.1446240750 | 972 | 504990 | -86.35 | 12.55 | 60.71 | 0.19 | 2.56 | 306 |
| 2024-09-20 22:21:36.171 | MS1 | 121.4656688781 | 31.1446315702 | 972 | 504990 | -87.70 | 12.90 | 99.51 | 0.11 | 2.37 | 420 |
| 2024-09-20 22:21:37.961 | MS1 | 121.4656738705 | 31.1446229214 | 972 | 504990 | -93.69 | 11.51 | 69.12 | 0.16 | 2.89 | 396 |
| 2024-09-20 22:21:38.326 | MS1 | 121.4656778043 | 31.1446373333 | 972 | 504990 | -90.56 | 8.09 | 105.06 | 0.03 | 2.63 | 366 |
| 2024-09-20 22:21:39.136 | MS1 | 121.4656626172 | 31.1446215334 | 972 | 504990 | -93.19 | 8.04 | 87.42 | 0.15 | 2.92 | 479 |
| 2024-09-20 22:21:40.363 | MS1 | 121.4656649975 | 31.1446289759 | 972 | 504990 | -92.37 | 9.74 | 336.44 | 0.13 | 2.12 | 1592 |
| 2024-09-20 22:21:41.959 | MS1 | 121.4656770574 | 31.1446247435 | 972 | 504990 | -91.48 | 8.31 | 484.30 | 0.06 | 2.11 | 1580 |
| 2024-09-20 22:21:42.245 | MS1 | 121.4656732716 | 31.1446207503 | 972 | 504990 | -91.41 | 10.82 | 469.70 | 0.10 | 2.01 | 1570 |

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
| 3211594 | 3 | 121.4725046460 | 31.1440968007 | 112 | 13 | 0 | 17.7 | TDD | 765 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3239158 | 1 | 121.4643663195 | 31.1557251616 | 29 | 1 | 3 | 21.7 | TDD | 851 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3249726 | 4 | 121.4652121903 | 31.1549268238 | 111 | 13 | 6 | 32.1 | TDD | 950 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3257870 | 2 | 121.4750190158 | 31.1519547176 | 136 | 15 | 11 | 47.5 | TDD | 972 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.762 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.783 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.889 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.889 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.652 | NREventA3 | measId:2;ServCellPCI:912;Se... |
| 2024-09-20 22:21:37.892 | NRHandoverAttempt | SourcePCI:912;SourceNR-ARFC... |
| 2024-09-20 22:21:37.924 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.939 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.053 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.053 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239158 | 1 | 8.0374 | 13.8033 | -115.1921 | 16.0429 | 195.9459 | 0.0039 | 0.0190 |
| 2024_09_20 22:00 | 3257870 | 2 | 16.2165 | 5.5089 | -115.4587 | 5.7697 | 100.0203 | 0.0105 | 0.0089 |
| 2024_09_20 22:00 | 3211594 | 3 | 17.4443 | 14.1607 | -114.7557 | 12.0702 | 190.4861 | 0.0157 | 0.0163 |
| 2024_09_20 22:00 | 3249726 | 4 | 8.1637 | 12.3736 | -117.6154 | 8.4821 | 164.1385 | 0.0074 | 0.0012 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413804_97DEC7C7 | 504990 | 972 | -88.0 | 504990 | 851 | -90.1 | 504990 | 765 | -98.6 | 504990 | 950 |
| MR_1774413804_97A57507 | 504990 | 972 | -88.4 | 504990 | 851 | -92.9 | 504990 | 765 | -97.9 | 504990 | 950 |
| MR_1774413804_181D9DA3 | 504990 | 972 | -89.1 | 504990 | 851 | -92.4 | 504990 | 765 | -100.2 | 504990 | 950 |
| MR_1774413804_03CA7138 | 504990 | 972 | -89.4 | 504990 | 851 | -92.6 | 504990 | 765 | -99.0 | 504990 | 950 |
| MR_1774413804_D14F13C9 | 504990 | 972 | -90.2 | 504990 | 851 | -89.4 | 504990 | 765 | -99.7 | 504990 | 950 |
| MR_1774413804_2C52E87C | 504990 | 972 | -91.0 | 504990 | 851 | -91.1 | 504990 | 765 | -100.2 | 504990 | 950 |
| MR_1774413804_1A5CD741 | 504990 | 972 | -88.6 | 504990 | 851 | -92.4 | 504990 | 765 | -96.4 | 504990 | 950 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1877: `c7af2e46-262...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c7af2e46-2623-4bc0-978d-2c378c3f4475` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3262762_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1877] topology](images/train_1877.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3211962_4
- `C2`: Lift the tilt angle  of 3211962_4 by 10 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211962_4
- `C5`: Decrease transmission power for 3262762_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262762_1
- `C7`: Increase A3 Offset threshold for 3262762_1
- `C8`: Decrease transmission power for 3211962_4
- `C9`: Adjust the azimuth of 3262762_1 by 12 degrees
- `C10`: Press down the tilt angle  of 3211962_4 by 10 degrees
- `C11`: Lift the tilt angle of 3262762_1 by 6 degrees
- `C12`: Add neighbor relationship between 3231018_3 and 3211962_4
- `C13`: Increase transmission power for 3262762_1
- `C14`: Press down the tilt angle of 3262762_1 by 6 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262762_1 **← 정답**
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211962_4
- `C17`: Decrease A3 Offset threshold for 3211962_4
- `C18`: Decrease A3 Offset threshold for 3262762_1
- `C19`: Adjust the azimuth of 3211962_4 by 25 degrees
- `C20`: Increase A3 Offset threshold for 3211962_4
- `C21`: Check test server and transmission issues
- `C22`: Add neighbor relationship between 3262762_1 and 3211962_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.581 | MS1 | 121.4656659042 | 31.1446222728 | 194 | 504990 | -88.33 | 16.38 | 462.04 | 0.15 | 2.31 | 1572 |
| 2024-09-20 22:21:32.512 | MS1 | 121.4656664379 | 31.1446233738 | 194 | 504990 | -88.38 | 15.08 | 385.09 | 0.09 | 2.19 | 1563 |
| 2024-09-20 22:21:33.629 | MS1 | 121.4656702482 | 31.1446366797 | 194 | 504990 | -85.92 | 13.14 | 414.03 | 0.05 | 2.20 | 1579 |
| 2024-09-20 22:21:34.958 | MS1 | 121.4656707336 | 31.1446194392 | 194 | 504990 | -91.90 | 12.16 | 54.27 | 0.51 | 2.30 | 580 |
| 2024-09-20 22:21:35.449 | MS1 | 121.4656661195 | 31.1446331179 | 194 | 504990 | -89.51 | 13.72 | 67.83 | 0.59 | 2.53 | 672 |
| 2024-09-20 22:21:36.725 | MS1 | 121.4656681617 | 31.1446192488 | 194 | 504990 | -87.31 | 17.81 | 61.26 | 0.54 | 2.90 | 583 |
| 2024-09-20 22:21:37.772 | MS1 | 121.4656768656 | 31.1446255059 | 194 | 504990 | -93.16 | 12.41 | 89.02 | 0.55 | 2.52 | 588 |
| 2024-09-20 22:21:38.308 | MS1 | 121.4656759902 | 31.1446197341 | 194 | 504990 | -89.04 | 10.88 | 49.77 | 0.61 | 2.68 | 518 |
| 2024-09-20 22:21:39.285 | MS1 | 121.4656682093 | 31.1446355446 | 194 | 504990 | -89.07 | 9.43 | 64.51 | 0.67 | 2.23 | 579 |
| 2024-09-20 22:21:40.269 | MS1 | 121.4656630183 | 31.1446208409 | 194 | 504990 | -90.87 | 12.32 | 354.17 | 0.03 | 2.28 | 1599 |
| 2024-09-20 22:21:41.467 | MS1 | 121.4656710520 | 31.1446202723 | 194 | 504990 | -92.38 | 10.56 | 379.30 | 0.07 | 2.68 | 1582 |
| 2024-09-20 22:21:42.265 | MS1 | 121.4656669551 | 31.1446206643 | 194 | 504990 | -93.34 | 10.66 | 353.29 | 0.03 | 2.79 | 1567 |

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
| 3211962 | 4 | 121.4655837752 | 31.1440535069 | 343 | 5 | 10 | 24.1 | TDD | 402 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3231018 | 3 | 121.4681277108 | 31.1548270268 | 240 | 10 | 1 | 46.4 | TDD | 174 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3261057 | 2 | 121.4721899741 | 31.1441174478 | 273 | 9 | 10 | 44.8 | TDD | 620 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3262762 | 1 | 121.4700053866 | 31.1514045320 | 221 | 3 | 5 | 43.5 | TDD | 194 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.109 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.129 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.247 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.247 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.008 | NREventA3 | measId:2;ServCellPCI:50;Ser... |
| 2024-09-20 22:21:38.248 | NRHandoverAttempt | SourcePCI:50;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.295 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.308 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.427 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.427 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262762 | 1 | 19.9076 | 14.2340 | -115.9735 | 16.4687 | 99.8962 | 0.0053 | 0.0122 |
| 2024_09_20 22:00 | 3261057 | 2 | 14.3981 | 15.6687 | -115.7250 | 19.5708 | 190.7580 | 0.0116 | 0.0113 |
| 2024_09_20 22:00 | 3231018 | 3 | 7.9187 | 16.1451 | -117.0831 | 17.6668 | 130.3606 | 0.0029 | 0.0184 |
| 2024_09_20 22:00 | 3211962 | 4 | 18.6774 | 14.7540 | -114.5701 | 8.5139 | 145.8024 | 0.0017 | 0.0016 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413299_545D46C6 | 504990 | 194 | -93.3 | 504990 | 402 | -96.1 | 504990 | 174 | -99.0 | 504990 | 620 |
| MR_1774413299_536EB4A4 | 504990 | 194 | -93.0 | 504990 | 402 | -95.5 | 504990 | 174 | -101.8 | 504990 | 620 |
| MR_1774413299_F5F0D454 | 504990 | 194 | -90.6 | 504990 | 402 | -96.0 | 504990 | 174 | -100.4 | 504990 | 620 |
| MR_1774413299_EB811726 | 504990 | 194 | -93.7 | 504990 | 402 | -97.1 | 504990 | 174 | -98.9 | 504990 | 620 |
| MR_1774413299_FAD019DE | 504990 | 194 | -90.1 | 504990 | 402 | -96.8 | 504990 | 174 | -102.3 | 504990 | 620 |
| MR_1774413299_6A49F0E3 | 504990 | 194 | -93.0 | 504990 | 402 | -95.2 | 504990 | 174 | -100.7 | 504990 | 620 |
| MR_1774413299_D1450E02 | 504990 | 194 | -92.2 | 504990 | 402 | -93.6 | 504990 | 174 | -101.1 | 504990 | 620 |
| MR_1774413299_BF9BD4F9 | 504990 | 194 | -91.3 | 504990 | 402 | -93.7 | 504990 | 174 | -102.5 | 504990 | 620 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1878: `7508150a-e00...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7508150a-e008-49de-8e54-d8b2204598d9` |
| Tag | **multiple-answer** |
| 정답 | **C5|C7** |
| C5 의미 | Press down the tilt angle  of 3248336_3 by 4 degrees |
| C7 의미 | Decrease transmission power for 3248336_3 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1878] topology](images/train_1878.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274664_1
- `C2`: Increase transmission power for 3274664_1
- `C3`: Decrease transmission power for 3274664_1
- `C4`: Lift the tilt angle  of 3248336_3 by 4 degrees
- `C5`: Press down the tilt angle  of 3248336_3 by 4 degrees **← 정답**
- `C6`: Adjust the azimuth of 3248336_3 by 3 degrees
- `C7`: Decrease transmission power for 3248336_3 **← 정답**
- `C8`: Decrease A3 Offset threshold for 3248336_3
- `C9`: Increase transmission power for 3248336_3
- `C10`: Adjust the azimuth of 3274664_1 by 23 degrees
- `C11`: Lift the tilt angle of 3274664_1 by 4 degrees
- `C12`: Decrease A3 Offset threshold for 3274664_1
- `C13`: Increase A3 Offset threshold for 3248336_3
- `C14`: Press down the tilt angle of 3274664_1 by 4 degrees
- `C15`: Add neighbor relationship between 3219139_2 and 3248336_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248336_3
- `C17`: Check test server and transmission issues
- `C18`: Add neighbor relationship between 3274664_1 and 3248336_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248336_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274664_1
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Increase A3 Offset threshold for 3274664_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.797 | MS1 | 121.4656691760 | 31.1446334746 | 137 | 504990 | -80.40 | 15.69 | 492.65 | 0.06 | 2.58 | 1596 |
| 2024-09-20 22:21:32.912 | MS1 | 121.4656779748 | 31.1446309195 | 137 | 504990 | -78.77 | 14.23 | 463.23 | 0.10 | 2.04 | 1588 |
| 2024-09-20 22:21:33.755 | MS1 | 121.4656735011 | 31.1446347170 | 137 | 504990 | -80.69 | 13.90 | 337.42 | 0.05 | 2.37 | 1573 |
| 2024-09-20 22:21:34.527 | MS1 | 121.4656662214 | 31.1446209641 | 137 | 504990 | -87.58 | 2.80 | 81.06 | 0.04 | 1.46 | 1595 |
| 2024-09-20 22:21:35.578 | MS1 | 121.4656746223 | 31.1446238305 | 137 | 504990 | -87.84 | 3.05 | 48.67 | 0.08 | 1.24 | 1600 |
| 2024-09-20 22:21:36.214 | MS1 | 121.4656614431 | 31.1446374168 | 137 | 504990 | -93.56 | 3.24 | 60.72 | 0.12 | 1.40 | 1568 |
| 2024-09-20 22:21:37.665 | MS1 | 121.4656703421 | 31.1446329664 | 137 | 504990 | -90.85 | 3.42 | 75.09 | 0.12 | 1.21 | 1580 |
| 2024-09-20 22:21:38.768 | MS1 | 121.4656642025 | 31.1446225597 | 137 | 504990 | -85.14 | 2.10 | 83.96 | 0.04 | 1.44 | 1585 |
| 2024-09-20 22:21:39.151 | MS1 | 121.4656760575 | 31.1446258143 | 137 | 504990 | -90.71 | 1.41 | 77.80 | 0.05 | 1.30 | 1598 |
| 2024-09-20 22:21:40.917 | MS1 | 121.4656701708 | 31.1446217110 | 137 | 504990 | -76.26 | 17.10 | 379.82 | 0.20 | 2.48 | 1577 |
| 2024-09-20 22:21:41.871 | MS1 | 121.4656695672 | 31.1446261483 | 137 | 504990 | -80.43 | 17.94 | 421.74 | 0.19 | 2.39 | 1594 |
| 2024-09-20 22:21:42.133 | MS1 | 121.4656618624 | 31.1446219300 | 137 | 504990 | -77.96 | 16.84 | 456.52 | 0.17 | 2.22 | 1592 |

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
| 3219139 | 2 | 121.4697667001 | 31.1489897457 | 63 | 15 | 9 | 38.0 | TDD | 914 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3223998 | 4 | 121.4720857357 | 31.1454415008 | 354 | 8 | 9 | 49.8 | TDD | 165 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3248336 | 3 | 121.4720714998 | 31.1554200392 | 210 | 3 | 11 | 27.7 | TDD | 411 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3274664 | 1 | 121.4757278308 | 31.1543603298 | 198 | 3 | 5 | 36.6 | TDD | 137 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.942 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.967 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.080 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.080 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274664 | 1 | 15.2039 | 11.6977 | -109.0476 | 7.4606 | 170.3083 | 0.0025 | 0.0097 |
| 2024_09_20 22:00 | 3219139 | 2 | 9.8548 | 5.9881 | -114.2861 | 10.2272 | 101.9845 | 0.0151 | 0.0135 |
| 2024_09_20 22:00 | 3248336 | 3 | 9.0712 | 19.1231 | -117.9838 | 7.1862 | 103.5929 | 0.0138 | 0.0081 |
| 2024_09_20 22:00 | 3223998 | 4 | 6.3125 | 7.8651 | -115.9261 | 18.6032 | 82.7890 | 0.0022 | 0.0035 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413119_037C55A7 | 504990 | 411 | -87.6 | 504990 | 137 | -90.2 | 504990 | 914 | -88.0 | 504990 | 165 |
| MR_1774413119_B389C968 | 504990 | 137 | -87.5 | 504990 | 411 | -88.4 | 504990 | 914 | -89.2 | 504990 | 165 |
| MR_1774413119_2FBD0794 | 504990 | 137 | -86.7 | 504990 | 411 | -89.7 | 504990 | 914 | -89.9 | 504990 | 165 |
| MR_1774413119_FB5A7F34 | 504990 | 137 | -88.4 | 504990 | 411 | -88.1 | 504990 | 914 | -88.0 | 504990 | 165 |
| MR_1774413119_F095C431 | 504990 | 137 | -89.1 | 504990 | 411 | -90.0 | 504990 | 914 | -89.2 | 504990 | 165 |
| MR_1774413119_C7539186 | 504990 | 137 | -88.7 | 504990 | 411 | -90.3 | 504990 | 914 | -89.0 | 504990 | 165 |
| MR_1774413119_3F3CBA5B | 504990 | 137 | -85.7 | 504990 | 411 | -89.9 | 504990 | 914 | -90.2 | 504990 | 165 |
| MR_1774413119_4C817C3A | 504990 | 137 | -86.3 | 504990 | 411 | -88.9 | 504990 | 914 | -89.3 | 504990 | 165 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1879: `6852b271-6f8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6852b271-6f8d-41aa-92c0-c26c7e26423f` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1879] topology](images/train_1879.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3233729_1 by 9 degrees
- `C2`: Press down the tilt angle  of 3233729_1 by 10 degrees
- `C3`: Press down the tilt angle of 3229201_2 by 10 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233729_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229201_2
- `C6`: Add neighbor relationship between 3229201_2 and 3233729_1
- `C7`: Check test server and transmission issues
- `C8`: Lift the tilt angle of 3229201_2 by 10 degrees
- `C9`: Decrease transmission power for 3229201_2
- `C10`: Decrease A3 Offset threshold for 3233729_1
- `C11`: Insufficient data; more data is needed for judgment. **← 정답**
- `C12`: Increase transmission power for 3233729_1
- `C13`: Decrease A3 Offset threshold for 3229201_2
- `C14`: Increase A3 Offset threshold for 3229201_2
- `C15`: Increase transmission power for 3229201_2
- `C16`: Add neighbor relationship between 3227626_4 and 3233729_1
- `C17`: Lift the tilt angle  of 3233729_1 by 10 degrees
- `C18`: Increase A3 Offset threshold for 3233729_1
- `C19`: Decrease transmission power for 3233729_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229201_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233729_1
- `C22`: Adjust the azimuth of 3229201_2 by 20 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.403 | MS1 | 121.4656612001 | 31.1446314731 | 889 | 504990 | -88.89 | 13.44 | 420.93 | 0.12 | 2.41 | 1579 |
| 2024-09-20 22:21:32.124 | MS1 | 121.4656671528 | 31.1446191265 | 889 | 504990 | -86.41 | 12.76 | 463.69 | 0.06 | 2.31 | 1599 |
| 2024-09-20 22:21:33.463 | MS1 | 121.4656741518 | 31.1446327974 | 889 | 504990 | -91.22 | 17.14 | 334.75 | 0.14 | 2.64 | 1577 |
| 2024-09-20 22:21:34.209 | MS1 | 121.4656631644 | 31.1446270843 | 889 | 504990 | -89.11 | 14.47 | 84.75 | 0.11 | 2.06 | 1573 |
| 2024-09-20 22:21:35.305 | MS1 | 121.4656709786 | 31.1446308029 | 889 | 504990 | -88.04 | 14.43 | 71.98 | 0.01 | 2.44 | 1570 |
| 2024-09-20 22:21:36.366 | MS1 | 121.4656608854 | 31.1446269445 | 889 | 504990 | -87.38 | 16.66 | 103.12 | 0.01 | 2.44 | 1583 |
| 2024-09-20 22:21:37.154 | MS1 | 121.4656688680 | 31.1446309674 | 889 | 504990 | -92.08 | 8.78 | 53.88 | 0.10 | 2.67 | 1593 |
| 2024-09-20 22:21:38.855 | MS1 | 121.4656774271 | 31.1446298772 | 889 | 504990 | -91.84 | 8.33 | 51.32 | 0.11 | 2.40 | 1576 |
| 2024-09-20 22:21:39.983 | MS1 | 121.4656779261 | 31.1446293309 | 889 | 504990 | -89.86 | 11.42 | 76.01 | 0.01 | 2.39 | 1560 |
| 2024-09-20 22:21:40.272 | MS1 | 121.4656681400 | 31.1446225802 | 889 | 504990 | -90.20 | 12.70 | 575.06 | 0.15 | 2.70 | 1564 |
| 2024-09-20 22:21:41.590 | MS1 | 121.4656710399 | 31.1446216687 | 889 | 504990 | -93.33 | 12.35 | 358.14 | 0.03 | 2.13 | 1581 |
| 2024-09-20 22:21:42.500 | MS1 | 121.4656738774 | 31.1446249740 | 889 | 504990 | -89.33 | 7.45 | 382.64 | 0.17 | 2.14 | 1560 |

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
| 3227626 | 4 | 121.4687359782 | 31.1559021799 | 169 | 5 | 2 | 28.7 | TDD | 456 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3229201 | 2 | 121.4717820275 | 31.1468816021 | 227 | 11 | 8 | 45.4 | TDD | 889 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3231937 | 3 | 121.4689412396 | 31.1522350343 | 339 | 5 | 1 | 31.1 | TDD | 652 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3233729 | 1 | 121.4657244152 | 31.1502589775 | 171 | 10 | 6 | 32.3 | TDD | 72 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.003 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.133 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.133 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.859 | NREventA3 | measId:2;ServCellPCI:309;Se... |
| 2024-09-20 22:21:38.099 | NRHandoverAttempt | SourcePCI:309;SourceNR-ARFC... |
| 2024-09-20 22:21:38.133 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.144 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.282 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.282 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3233729 | 1 | 77.2655 | 87.1396 | -117.7086 | 19.3754 | 189.5048 | 0.0048 | 0.0120 |
| 2024_09_19 22:00 | 3229201 | 2 | 89.6533 | 83.1990 | -117.5880 | 18.6954 | 134.2666 | 0.0040 | 0.0161 |
| 2024_09_19 22:00 | 3231937 | 3 | 93.3525 | 76.5647 | -115.0958 | 15.6365 | 189.5145 | 0.0014 | 0.0137 |
| 2024_09_19 22:00 | 3227626 | 4 | 81.2752 | 75.1314 | -116.4183 | 7.0369 | 143.4414 | 0.0186 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412746_C34DA73C | 504990 | 889 | -89.7 | 504990 | 72 | -95.3 | 504990 | 456 | -94.5 | 504990 | 652 |
| MR_1774412746_9E1DE009 | 504990 | 889 | -90.9 | 504990 | 72 | -92.1 | 504990 | 456 | -94.9 | 504990 | 652 |
| MR_1774412746_819AFCA8 | 504990 | 889 | -89.2 | 504990 | 72 | -92.8 | 504990 | 456 | -95.1 | 504990 | 652 |
| MR_1774412746_DF5054D0 | 504990 | 889 | -90.6 | 504990 | 72 | -92.0 | 504990 | 456 | -94.2 | 504990 | 652 |
| MR_1774412746_E23CF97D | 504990 | 889 | -90.4 | 504990 | 72 | -92.2 | 504990 | 456 | -94.9 | 504990 | 652 |
| MR_1774412746_D1B0DBC9 | 504990 | 889 | -88.7 | 504990 | 72 | -94.8 | 504990 | 456 | -95.9 | 504990 | 652 |

> *... 2개 열 생략 (전체 14열)*

---
