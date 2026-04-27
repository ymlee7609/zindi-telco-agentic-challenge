# Track A 문제 분석 — train[910]~train[919]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[910] ~ train[919] (10개)

## 목차

1. [문제 910: `19e3b835-36a...`](#910) — single-answer, 정답: C14
2. [문제 911: `a32b4ef9-051...`](#911) — single-answer, 정답: C10
3. [문제 912: `99642227-331...`](#912) — single-answer, 정답: C18
4. [문제 913: `d6e192d6-35d...`](#913) — single-answer, 정답: C14
5. [문제 914: `456498b8-8ad...`](#914) — single-answer, 정답: C7
6. [문제 915: `31e1b226-d8c...`](#915) — single-answer, 정답: C11
7. [문제 916: `e7fcea03-ded...`](#916) — single-answer, 정답: C3
8. [문제 917: `5738e211-b22...`](#917) — multiple-answer, 정답: C6|C18
9. [문제 918: `50bd7ca4-08b...`](#918) — single-answer, 정답: C13
10. [문제 919: `46de010f-263...`](#919) — multiple-answer, 정답: C4|C10|C11|C20

---

### 문제 910: `19e3b835-36a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `19e3b835-36a0-4b21-b636-f25bfe3cd1fb` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220330_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[910] topology](images/train_0910.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3220330_5 by 1 degrees
- `C2`: Lift the tilt angle  of 3271939_4 by 6 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271939_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220330_5
- `C5`: Increase transmission power for 3271939_4
- `C6`: Add neighbor relationship between 3257840_13 and 3271939_4
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Press down the tilt angle  of 3271939_4 by 6 degrees
- `C9`: Increase transmission power for 3220330_5
- `C10`: Adjust the azimuth of 3271939_4 by 27 degrees
- `C11`: Lift the tilt angle of 3220330_5 by 1 degrees
- `C12`: Check test server and transmission issues
- `C13`: Adjust the azimuth of 3220330_5 by 3 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220330_5 **← 정답**
- `C15`: Increase A3 Offset threshold for 3271939_4
- `C16`: Add neighbor relationship between 3220330_5 and 3271939_4
- `C17`: Decrease transmission power for 3220330_5
- `C18`: Decrease A3 Offset threshold for 3271939_4
- `C19`: Decrease transmission power for 3271939_4
- `C20`: Decrease A3 Offset threshold for 3220330_5
- `C21`: Increase A3 Offset threshold for 3220330_5
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271939_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.406 | MS1 | 121.4656745942 | 31.1446282905 | 90 | 504990 | -94.81 | 11.03 | 342.99 | 0.11 | 2.14 | 1591 |
| 2024-09-20 22:21:32.153 | MS1 | 121.4656634596 | 31.1446225364 | 976 | 504990 | -93.33 | 10.81 | 561.81 | 0.00 | 2.29 | 1566 |
| 2024-09-20 22:21:33.140 | MS1 | 121.4656592672 | 31.1446311067 | 533 | 504990 | -93.38 | 12.47 | 536.08 | 0.10 | 2.17 | 1600 |
| 2024-09-20 22:21:34.158 | MS1 | 121.4656665641 | 31.1446340968 | 812 | 152650 | -90.65 | 6.15 | 82.28 | 0.00 | 1.79 | 932 |
| 2024-09-20 22:21:35.460 | MS1 | 121.4656592744 | 31.1446310750 | 998 | 152650 | -90.18 | 3.26 | 58.02 | 0.19 | 1.72 | 985 |
| 2024-09-20 22:21:36.736 | MS1 | 121.4656593211 | 31.1446268363 | 51 | 152650 | -96.92 | 4.72 | 57.23 | 0.19 | 1.87 | 922 |
| 2024-09-20 22:21:37.900 | MS1 | 121.4656645685 | 31.1446223822 | 800 | 152650 | -91.91 | 4.96 | 65.26 | 0.05 | 1.88 | 996 |
| 2024-09-20 22:21:38.875 | MS1 | 121.4656587006 | 31.1446212163 | 812 | 152650 | -93.36 | 3.59 | 60.51 | 0.07 | 1.94 | 994 |
| 2024-09-20 22:21:39.231 | MS1 | 121.4656661319 | 31.1446296670 | 998 | 152650 | -93.19 | 2.98 | 95.80 | 0.05 | 1.92 | 931 |
| 2024-09-20 22:21:40.987 | MS1 | 121.4656735919 | 31.1446196136 | 51 | 152650 | -89.20 | 6.86 | 96.16 | 0.12 | 2.95 | 1589 |
| 2024-09-20 22:21:41.804 | MS1 | 121.4656746928 | 31.1446236158 | 800 | 152650 | -96.85 | 4.76 | 64.84 | 0.10 | 2.84 | 1577 |
| 2024-09-20 22:21:42.658 | MS1 | 121.4656641232 | 31.1446231562 | 812 | 152650 | -88.38 | 4.93 | 79.21 | 0.09 | 2.72 | 1560 |

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
| 3211452 | 2 | 121.4712925155 | 31.1463783539 | 71 | 6 | 12 | 25.3 | TDD | 725 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3217068 | 10 | 121.4749709879 | 31.1524259492 | 343 | 15 | 4 | 25.4 | FDD | 523 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3217300 | 3 | 121.4733083319 | 31.1536580889 | 18 | 4 | 4 | 15.9 | TDD | 533 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3219065 | 1 | 121.4738279977 | 31.1462622878 | 20 | 0 | 10 | 16.4 | TDD | 976 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3220330 | 5 | 121.4742644659 | 31.1499886862 | 231 | 0 | 4 | 15.1 | TDD | 90 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3247162 | 9 | 121.4684551181 | 31.1464902574 | 344 | 9 | 1 | 8.2 | FDD | 42 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3250258 | 6 | 121.4729073657 | 31.1443995105 | 110 | 3 | 0 | 7.1 | TDD | 381 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3257840 | 13 | 121.4654104033 | 31.1474774138 | 141 | 8 | 12 | 4.4 | FDD | 51 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3258845 | 8 | 121.4698508552 | 31.1517612611 | 28 | 7 | 7 | 26.1 | FDD | 998 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3263502 | 11 | 121.4705134849 | 31.1504480864 | 7 | 4 | 9 | 11.2 | FDD | 812 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3271939 | 4 | 121.4675837816 | 31.1538241322 | 217 | 5 | 1 | 17.2 | TDD | 182 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3274869 | 12 | 121.4671523183 | 31.1550142835 | 318 | 13 | 3 | 18.9 | FDD | 14 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3277292 | 7 | 121.4681698655 | 31.1520172131 | 268 | 15 | 5 | 16.3 | FDD | 800 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |

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
| 2024-09-20 22:21:31.138 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.156 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.263 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.263 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.031 | NREventA2 | measId:1;ServCellPCI:831;Se... |
| 2024-09-20 22:21:35.180 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.398 | NREventA5 | measId:3;ServCellPCI:831;Se... |
| 2024-09-20 22:21:35.464 | NRHandoverAttempt | SourcePCI:831;SourceNR-ARFC... |
| 2024-09-20 22:21:35.491 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.505 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.639 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.639 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219065 | 1 | 14.7499 | 6.4780 | -117.9482 | 14.1108 | 132.6818 | 0.0179 | 0.0079 |
| 2024_09_20 22:00 | 3211452 | 2 | 13.4500 | 14.8334 | -115.7208 | 11.2526 | 152.8868 | 0.0005 | 0.0043 |
| 2024_09_20 22:00 | 3217300 | 3 | 14.8298 | 7.3051 | -117.0245 | 5.2020 | 193.2043 | 0.0019 | 0.0038 |
| 2024_09_20 22:00 | 3271939 | 4 | 8.7164 | 19.9760 | -117.6096 | 15.2961 | 141.4795 | 0.0087 | 0.0140 |
| 2024_09_20 22:00 | 3220330 | 5 | 9.1863 | 18.7807 | -117.1584 | 6.1109 | 176.3482 | 0.0200 | 0.0182 |
| 2024_09_20 22:00 | 3250258 | 6 | 5.7697 | 6.9539 | -114.6434 | 12.0009 | 188.9665 | 0.0108 | 0.0066 |
| 2024_09_20 22:00 | 3277292 | 7 | 6.8041 | 9.3415 | -117.6547 | 3.8401 | 49.3726 | 0.0109 | 0.0183 |
| 2024_09_20 22:00 | 3258845 | 8 | 13.0195 | 6.4966 | -117.3839 | 4.8976 | 23.0995 | 0.0086 | 0.0114 |
| 2024_09_20 22:00 | 3247162 | 9 | 10.8009 | 7.8303 | -117.8127 | 4.4748 | 44.9661 | 0.0105 | 0.0007 |
| 2024_09_20 22:00 | 3217068 | 10 | 8.5335 | 6.7896 | -114.3616 | 4.4268 | 40.4894 | 0.0110 | 0.0048 |
| 2024_09_20 22:00 | 3263502 | 11 | 15.1699 | 5.7348 | -117.5118 | 4.3777 | 49.1759 | 0.0134 | 0.0040 |
| 2024_09_20 22:00 | 3274869 | 12 | 9.7532 | 8.5208 | -114.2301 | 4.0855 | 45.2219 | 0.0024 | 0.0095 |
| 2024_09_20 22:00 | 3257840 | 13 | 12.7433 | 5.1994 | -116.0752 | 4.9239 | 27.8789 | 0.0194 | 0.0070 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417123_AF18DB62 | 152650 | 812 | -89.3 | 152650 | 42 | -93.2 | 152650 | 523 | -100.8 | 152650 | 14 |
| MR_1774417123_790FF0FA | 152650 | 812 | -91.2 | 152650 | 42 | -94.2 | 152650 | 523 | -101.8 | 152650 | 14 |
| MR_1774417123_75A63B9C | 504990 | 533 | -95.2 | 504990 | 182 | -92.6 | 504990 | 725 | -96.1 | 504990 | 381 |
| MR_1774417123_14E00376 | 504990 | 533 | -94.3 | 504990 | 182 | -91.6 | 504990 | 725 | -95.4 | 504990 | 381 |
| MR_1774417123_82517CE8 | 152650 | 812 | -92.1 | 152650 | 42 | -94.9 | 152650 | 523 | -102.6 | 152650 | 14 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 911: `a32b4ef9-051...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a32b4ef9-051c-470f-ae40-2f5116c3faca` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[911] topology](images/train_0911.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3257747_1 by 10 degrees
- `C2`: Press down the tilt angle of 3257747_1 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244562_4
- `C4`: Increase A3 Offset threshold for 3257747_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257747_1
- `C6`: Add neighbor relationship between 3257747_1 and 3244562_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257747_1
- `C8`: Increase transmission power for 3244562_4
- `C9`: Check test server and transmission issues
- `C10`: Insufficient data; more data is needed for judgment. **← 정답**
- `C11`: Increase transmission power for 3257747_1
- `C12`: Press down the tilt angle  of 3244562_4 by 9 degrees
- `C13`: Decrease transmission power for 3244562_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244562_4
- `C15`: Decrease transmission power for 3257747_1
- `C16`: Decrease A3 Offset threshold for 3244562_4
- `C17`: Lift the tilt angle  of 3244562_4 by 9 degrees
- `C18`: Add neighbor relationship between 3253016_3 and 3244562_4
- `C19`: Adjust the azimuth of 3257747_1 by 50 degrees
- `C20`: Adjust the azimuth of 3244562_4 by 26 degrees
- `C21`: Increase A3 Offset threshold for 3244562_4
- `C22`: Decrease A3 Offset threshold for 3257747_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.539 | MS1 | 121.4656740829 | 31.1446237793 | 888 | 504990 | -87.40 | 13.54 | 588.20 | 0.08 | 2.60 | 1586 |
| 2024-09-20 22:21:32.641 | MS1 | 121.4656632331 | 31.1446280201 | 888 | 504990 | -90.39 | 13.08 | 456.62 | 0.10 | 2.86 | 1588 |
| 2024-09-20 22:21:33.822 | MS1 | 121.4656748658 | 31.1446318653 | 888 | 504990 | -85.43 | 17.79 | 605.69 | 0.12 | 2.65 | 1593 |
| 2024-09-20 22:21:34.100 | MS1 | 121.4656751541 | 31.1446288892 | 888 | 504990 | -89.79 | 17.01 | 94.67 | 0.12 | 2.67 | 1592 |
| 2024-09-20 22:21:35.851 | MS1 | 121.4656610400 | 31.1446181112 | 888 | 504990 | -85.83 | 12.86 | 52.64 | 0.09 | 2.85 | 1572 |
| 2024-09-20 22:21:36.351 | MS1 | 121.4656737998 | 31.1446332569 | 888 | 504990 | -86.90 | 16.90 | 95.14 | 0.16 | 2.35 | 1570 |
| 2024-09-20 22:21:37.222 | MS1 | 121.4656767775 | 31.1446196684 | 888 | 504990 | -89.13 | 7.20 | 81.11 | 0.06 | 2.04 | 1588 |
| 2024-09-20 22:21:38.436 | MS1 | 121.4656592373 | 31.1446191123 | 888 | 504990 | -91.62 | 7.67 | 47.11 | 0.12 | 2.14 | 1564 |
| 2024-09-20 22:21:39.219 | MS1 | 121.4656684540 | 31.1446344430 | 888 | 504990 | -92.79 | 8.40 | 52.96 | 0.18 | 2.04 | 1576 |
| 2024-09-20 22:21:40.661 | MS1 | 121.4656668467 | 31.1446213394 | 888 | 504990 | -93.17 | 8.80 | 402.49 | 0.00 | 2.69 | 1567 |
| 2024-09-20 22:21:41.868 | MS1 | 121.4656619369 | 31.1446230461 | 888 | 504990 | -93.39 | 11.87 | 347.63 | 0.09 | 2.75 | 1592 |
| 2024-09-20 22:21:42.131 | MS1 | 121.4656724297 | 31.1446341942 | 888 | 504990 | -90.55 | 9.31 | 306.44 | 0.07 | 2.22 | 1563 |

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
| 3233508 | 2 | 121.4730604038 | 31.1544273322 | 316 | 10 | 11 | 42.5 | TDD | 73 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3244562 | 4 | 121.4759316984 | 31.1446172194 | 244 | 7 | 6 | 32.1 | TDD | 181 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3253016 | 3 | 121.4677653335 | 31.1501635459 | 276 | 14 | 5 | 44.4 | TDD | 523 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3257747 | 1 | 121.4729197154 | 31.1472777539 | 69 | 8 | 3 | 20.1 | TDD | 888 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.383 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.383 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.073 | NREventA3 | measId:2;ServCellPCI:659;Se... |
| 2024-09-20 22:21:38.313 | NRHandoverAttempt | SourcePCI:659;SourceNR-ARFC... |
| 2024-09-20 22:21:38.352 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.362 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.484 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.484 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3257747 | 1 | 88.7452 | 92.0591 | -115.0720 | 12.4103 | 134.7612 | 0.0162 | 0.0199 |
| 2024_09_19 22:00 | 3233508 | 2 | 92.4709 | 89.6675 | -116.1385 | 8.5576 | 138.5742 | 0.0111 | 0.0183 |
| 2024_09_19 22:00 | 3253016 | 3 | 84.8606 | 82.7025 | -117.4035 | 11.3691 | 98.3858 | 0.0173 | 0.0048 |
| 2024_09_19 22:00 | 3244562 | 4 | 79.5886 | 89.7099 | -115.6798 | 18.4397 | 164.5683 | 0.0100 | 0.0117 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415270_43F6F415 | 504990 | 888 | -89.8 | 504990 | 181 | -94.3 | 504990 | 523 | -94.2 | 504990 | 73 |
| MR_1774415270_6F2447E5 | 504990 | 888 | -91.0 | 504990 | 181 | -95.7 | 504990 | 523 | -96.8 | 504990 | 73 |
| MR_1774415270_C6F5DE0F | 504990 | 888 | -88.4 | 504990 | 181 | -94.0 | 504990 | 523 | -94.5 | 504990 | 73 |
| MR_1774415270_161090DC | 504990 | 888 | -91.3 | 504990 | 181 | -93.7 | 504990 | 523 | -95.3 | 504990 | 73 |
| MR_1774415270_7FC6D1C7 | 504990 | 888 | -89.4 | 504990 | 181 | -93.2 | 504990 | 523 | -96.7 | 504990 | 73 |
| MR_1774415270_63DAB15B | 504990 | 888 | -90.8 | 504990 | 181 | -94.3 | 504990 | 523 | -95.3 | 504990 | 73 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 912: `99642227-331...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `99642227-331a-4035-889b-1ee68b8d5bed` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[912] topology](images/train_0912.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3213058_4 and 3224576_1
- `C2`: Increase transmission power for 3257805_2
- `C3`: Decrease transmission power for 3257805_2
- `C4`: Press down the tilt angle of 3257805_2 by 10 degrees
- `C5`: Lift the tilt angle  of 3224576_1 by 7 degrees
- `C6`: Increase A3 Offset threshold for 3257805_2
- `C7`: Decrease A3 Offset threshold for 3257805_2
- `C8`: Add neighbor relationship between 3257805_2 and 3224576_1
- `C9`: Adjust the azimuth of 3257805_2 by 50 degrees
- `C10`: Press down the tilt angle  of 3224576_1 by 7 degrees
- `C11`: Lift the tilt angle of 3257805_2 by 10 degrees
- `C12`: Adjust the azimuth of 3224576_1 by 50 degrees
- `C13`: Increase A3 Offset threshold for 3224576_1
- `C14`: Decrease A3 Offset threshold for 3224576_1
- `C15`: Increase transmission power for 3224576_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224576_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257805_2
- `C18`: Check test server and transmission issues **← 정답**
- `C19`: Decrease transmission power for 3224576_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224576_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257805_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.411 | MS1 | 121.4656619715 | 31.1446342111 | 670 | 504990 | -90.41 | 13.00 | 562.00 | 0.19 | 2.85 | 1567 |
| 2024-09-20 22:21:32.884 | MS1 | 121.4656613154 | 31.1446291812 | 670 | 504990 | -85.99 | 16.86 | 307.51 | 0.19 | 2.77 | 1568 |
| 2024-09-20 22:21:33.338 | MS1 | 121.4656632555 | 31.1446222800 | 670 | 504990 | -90.06 | 12.57 | 460.44 | 0.15 | 2.34 | 1568 |
| 2024-09-20 22:21:34.464 | MS1 | 121.4656590057 | 31.1446183760 | 670 | 504990 | -86.97 | 12.54 | 78.70 | 0.17 | 2.83 | 335 |
| 2024-09-20 22:21:35.703 | MS1 | 121.4656680352 | 31.1446323122 | 670 | 504990 | -90.98 | 13.09 | 60.38 | 0.13 | 2.64 | 315 |
| 2024-09-20 22:21:36.101 | MS1 | 121.4656674281 | 31.1446231746 | 670 | 504990 | -89.76 | 12.65 | 87.06 | 0.15 | 2.28 | 340 |
| 2024-09-20 22:21:37.141 | MS1 | 121.4656721194 | 31.1446311511 | 670 | 504990 | -90.12 | 8.83 | 96.21 | 0.06 | 2.37 | 435 |
| 2024-09-20 22:21:38.246 | MS1 | 121.4656692237 | 31.1446315569 | 670 | 504990 | -92.02 | 11.76 | 68.60 | 0.12 | 2.73 | 308 |
| 2024-09-20 22:21:39.841 | MS1 | 121.4656637004 | 31.1446234825 | 670 | 504990 | -91.69 | 7.33 | 73.81 | 0.11 | 2.01 | 331 |
| 2024-09-20 22:21:40.567 | MS1 | 121.4656704397 | 31.1446197850 | 670 | 504990 | -92.01 | 9.77 | 428.05 | 0.09 | 2.05 | 1572 |
| 2024-09-20 22:21:41.382 | MS1 | 121.4656714437 | 31.1446232724 | 670 | 504990 | -93.56 | 10.30 | 553.43 | 0.17 | 2.88 | 1561 |
| 2024-09-20 22:21:42.620 | MS1 | 121.4656741148 | 31.1446331251 | 670 | 504990 | -92.60 | 9.75 | 342.87 | 0.04 | 2.79 | 1575 |

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
| 3213058 | 4 | 121.4716380915 | 31.1442784687 | 149 | 2 | 7 | 43.8 | TDD | 200 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3224576 | 1 | 121.4706246495 | 31.1529501198 | 46 | 5 | 7 | 29.5 | TDD | 296 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3257805 | 2 | 121.4668185007 | 31.1490805177 | 327 | 9 | 4 | 21.7 | TDD | 670 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3262131 | 3 | 121.4691198199 | 31.1548653563 | 281 | 11 | 10 | 18.6 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.879 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.989 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.989 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.675 | NREventA3 | measId:2;ServCellPCI:902;Se... |
| 2024-09-20 22:21:37.915 | NRHandoverAttempt | SourcePCI:902;SourceNR-ARFC... |
| 2024-09-20 22:21:37.962 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.974 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.077 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.077 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224576 | 1 | 19.6307 | 12.7815 | -115.2566 | 6.3534 | 134.8568 | 0.0051 | 0.0118 |
| 2024_09_20 22:00 | 3257805 | 2 | 13.2445 | 9.1458 | -116.5436 | 12.4410 | 133.3307 | 0.0190 | 0.0174 |
| 2024_09_20 22:00 | 3262131 | 3 | 7.9328 | 9.0159 | -115.3727 | 16.0831 | 126.0443 | 0.0075 | 0.0081 |
| 2024_09_20 22:00 | 3213058 | 4 | 15.0167 | 7.0406 | -117.7122 | 11.7913 | 160.1362 | 0.0134 | 0.0119 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414479_5A5C482C | 504990 | 670 | -85.9 | 504990 | 296 | -97.8 | 504990 | 200 | -99.5 | 504990 | 176 |
| MR_1774414479_F5770FBB | 504990 | 670 | -86.8 | 504990 | 296 | -97.7 | 504990 | 200 | -100.8 | 504990 | 176 |
| MR_1774414479_068A7F53 | 504990 | 670 | -86.4 | 504990 | 296 | -97.8 | 504990 | 200 | -98.5 | 504990 | 176 |
| MR_1774414479_9B2B25E6 | 504990 | 670 | -87.8 | 504990 | 296 | -97.2 | 504990 | 200 | -99.7 | 504990 | 176 |
| MR_1774414479_FF14A276 | 504990 | 670 | -86.4 | 504990 | 296 | -94.6 | 504990 | 200 | -99.0 | 504990 | 176 |
| MR_1774414479_FFACD183 | 504990 | 670 | -88.4 | 504990 | 296 | -97.1 | 504990 | 200 | -99.8 | 504990 | 176 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 913: `d6e192d6-35d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d6e192d6-35d7-4300-9a32-6352d9d44f64` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3267592_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[913] topology](images/train_0913.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3279135_2
- `C2`: Adjust the azimuth of 3267592_3 by 44 degrees
- `C3`: Press down the tilt angle  of 3279135_2 by 10 degrees
- `C4`: Decrease transmission power for 3267592_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279135_2
- `C6`: Decrease A3 Offset threshold for 3267592_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279135_2
- `C8`: Adjust the azimuth of 3279135_2 by 50 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Add neighbor relationship between 3266474_1 and 3279135_2
- `C11`: Add neighbor relationship between 3267592_3 and 3279135_2
- `C12`: Increase A3 Offset threshold for 3279135_2
- `C13`: Lift the tilt angle  of 3279135_2 by 10 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267592_3 **← 정답**
- `C15`: Increase transmission power for 3267592_3
- `C16`: Check test server and transmission issues
- `C17`: Decrease A3 Offset threshold for 3279135_2
- `C18`: Increase A3 Offset threshold for 3267592_3
- `C19`: Lift the tilt angle of 3267592_3 by 4 degrees
- `C20`: Increase transmission power for 3279135_2
- `C21`: Press down the tilt angle of 3267592_3 by 4 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267592_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.795 | MS1 | 121.4656631735 | 31.1446305085 | 562 | 504990 | -88.42 | 13.02 | 438.79 | 0.16 | 2.15 | 1598 |
| 2024-09-20 22:21:32.583 | MS1 | 121.4656752426 | 31.1446214581 | 562 | 504990 | -88.49 | 16.73 | 589.30 | 0.14 | 2.26 | 1584 |
| 2024-09-20 22:21:33.436 | MS1 | 121.4656761016 | 31.1446355882 | 562 | 504990 | -88.62 | 13.49 | 428.70 | 0.03 | 2.97 | 1562 |
| 2024-09-20 22:21:34.162 | MS1 | 121.4656775458 | 31.1446220234 | 562 | 504990 | -89.55 | 15.17 | 90.26 | 0.66 | 2.90 | 576 |
| 2024-09-20 22:21:35.566 | MS1 | 121.4656609207 | 31.1446180952 | 562 | 504990 | -90.99 | 14.31 | 91.42 | 0.51 | 2.36 | 579 |
| 2024-09-20 22:21:36.832 | MS1 | 121.4656677647 | 31.1446296446 | 562 | 504990 | -86.14 | 15.49 | 78.44 | 0.51 | 2.29 | 669 |
| 2024-09-20 22:21:37.278 | MS1 | 121.4656764620 | 31.1446335015 | 562 | 504990 | -92.09 | 10.93 | 59.03 | 0.55 | 2.38 | 516 |
| 2024-09-20 22:21:38.778 | MS1 | 121.4656778872 | 31.1446252520 | 562 | 504990 | -89.42 | 11.75 | 67.48 | 0.57 | 2.10 | 620 |
| 2024-09-20 22:21:39.467 | MS1 | 121.4656666025 | 31.1446232109 | 562 | 504990 | -92.08 | 9.27 | 60.26 | 0.66 | 2.09 | 528 |
| 2024-09-20 22:21:40.669 | MS1 | 121.4656776355 | 31.1446261473 | 562 | 504990 | -93.62 | 10.06 | 371.08 | 0.13 | 2.88 | 1593 |
| 2024-09-20 22:21:41.184 | MS1 | 121.4656737357 | 31.1446203149 | 562 | 504990 | -91.71 | 12.51 | 420.71 | 0.13 | 2.30 | 1582 |
| 2024-09-20 22:21:42.483 | MS1 | 121.4656610465 | 31.1446237356 | 562 | 504990 | -93.79 | 11.77 | 364.45 | 0.03 | 2.63 | 1576 |

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
| 3237052 | 4 | 121.4687250253 | 31.1486205290 | 114 | 3 | 1 | 34.5 | TDD | 105 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3266474 | 1 | 121.4735228456 | 31.1467183322 | 118 | 0 | 12 | 19.4 | TDD | 496 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3267592 | 3 | 121.4641743121 | 31.1523857001 | 215 | 2 | 7 | 24.3 | TDD | 562 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3279135 | 2 | 121.4689747827 | 31.1446338803 | 351 | 5 | 8 | 37.1 | TDD | 369 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.147 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.164 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.307 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.307 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.972 | NREventA3 | measId:2;ServCellPCI:439;Se... |
| 2024-09-20 22:21:38.212 | NRHandoverAttempt | SourcePCI:439;SourceNR-ARFC... |
| 2024-09-20 22:21:38.253 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.265 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.414 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.414 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266474 | 1 | 19.5435 | 6.5415 | -117.3481 | 19.5971 | 132.7733 | 0.0174 | 0.0031 |
| 2024_09_20 22:00 | 3279135 | 2 | 6.7154 | 13.1262 | -116.5344 | 13.2487 | 132.5374 | 0.0177 | 0.0059 |
| 2024_09_20 22:00 | 3267592 | 3 | 6.9579 | 18.8147 | -114.7867 | 7.8417 | 199.4927 | 0.0106 | 0.0012 |
| 2024_09_20 22:00 | 3237052 | 4 | 19.3535 | 11.5548 | -116.5263 | 17.3341 | 130.0112 | 0.0154 | 0.0098 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412297_89661BF4 | 504990 | 562 | -90.4 | 504990 | 369 | -93.0 | 504990 | 496 | -97.0 | 504990 | 105 |
| MR_1774412297_61E0C08A | 504990 | 562 | -89.9 | 504990 | 369 | -95.7 | 504990 | 496 | -98.3 | 504990 | 105 |
| MR_1774412297_2F66410B | 504990 | 562 | -87.6 | 504990 | 369 | -96.0 | 504990 | 496 | -99.3 | 504990 | 105 |
| MR_1774412297_F261808B | 504990 | 562 | -89.5 | 504990 | 369 | -96.4 | 504990 | 496 | -99.5 | 504990 | 105 |
| MR_1774412297_20432197 | 504990 | 562 | -89.0 | 504990 | 369 | -96.4 | 504990 | 496 | -98.8 | 504990 | 105 |
| MR_1774412297_0B7F4C44 | 504990 | 562 | -89.9 | 504990 | 369 | -96.7 | 504990 | 496 | -97.1 | 504990 | 105 |
| MR_1774412297_8909AAC3 | 504990 | 562 | -89.7 | 504990 | 369 | -93.9 | 504990 | 496 | -98.6 | 504990 | 105 |
| MR_1774412297_F80F43F1 | 504990 | 562 | -89.1 | 504990 | 369 | -96.4 | 504990 | 496 | -98.6 | 504990 | 105 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 914: `456498b8-8ad...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `456498b8-8ad2-43f0-a894-fc7734edae0c` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease A3 Offset threshold for 3244715_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[914] topology](images/train_0914.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276709_4
- `C2`: Adjust the azimuth of 3244715_2 by 50 degrees
- `C3`: Add neighbor relationship between 3257386_3 and 3276709_4
- `C4`: Decrease transmission power for 3244715_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276709_4
- `C6`: Increase transmission power for 3244715_2
- `C7`: Decrease A3 Offset threshold for 3244715_2 **← 정답**
- `C8`: Check test server and transmission issues
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244715_2
- `C10`: Decrease transmission power for 3276709_4
- `C11`: Add neighbor relationship between 3244715_2 and 3276709_4
- `C12`: Lift the tilt angle of 3244715_2 by 10 degrees
- `C13`: Increase transmission power for 3276709_4
- `C14`: Adjust the azimuth of 3276709_4 by 50 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244715_2
- `C16`: Decrease A3 Offset threshold for 3276709_4
- `C17`: Press down the tilt angle of 3244715_2 by 10 degrees
- `C18`: Increase A3 Offset threshold for 3244715_2
- `C19`: Press down the tilt angle  of 3276709_4 by 3 degrees
- `C20`: Increase A3 Offset threshold for 3276709_4
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Lift the tilt angle  of 3276709_4 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.938 | MS1 | 121.4656591886 | 31.1446190724 | 866 | 504990 | -81.91 | 14.28 | 329.47 | 0.20 | 2.59 | 1576 |
| 2024-09-20 22:21:32.635 | MS1 | 121.4656752424 | 31.1446211172 | 866 | 504990 | -79.22 | 12.66 | 349.14 | 0.15 | 2.01 | 1592 |
| 2024-09-20 22:21:33.797 | MS1 | 121.4656706218 | 31.1446251958 | 866 | 504990 | -83.94 | 15.83 | 437.75 | 0.02 | 2.87 | 1570 |
| 2024-09-20 22:21:34.199 | MS1 | 121.4656620875 | 31.1446361800 | 866 | 504990 | -84.82 | -3.10 | 73.69 | 0.18 | 1.40 | 1582 |
| 2024-09-20 22:21:35.701 | MS1 | 121.4656755100 | 31.1446316643 | 866 | 504990 | -91.05 | -1.88 | 60.13 | 0.07 | 1.43 | 1590 |
| 2024-09-20 22:21:36.160 | MS1 | 121.4656610839 | 31.1446234317 | 866 | 504990 | -85.94 | -1.13 | 26.58 | 0.19 | 1.25 | 1570 |
| 2024-09-20 22:21:37.586 | MS1 | 121.4656590736 | 31.1446192523 | 866 | 504990 | -90.35 | -3.91 | 56.03 | 0.08 | 1.27 | 1583 |
| 2024-09-20 22:21:38.923 | MS1 | 121.4656635491 | 31.1446359980 | 866 | 504990 | -89.94 | -0.33 | 62.14 | 0.17 | 1.26 | 1585 |
| 2024-09-20 22:21:39.787 | MS1 | 121.4656763924 | 31.1446183769 | 942 | 504990 | -75.89 | 15.71 | 142.61 | 0.05 | 1.01 | 1582 |
| 2024-09-20 22:21:40.653 | MS1 | 121.4656605356 | 31.1446295323 | 942 | 504990 | -84.10 | 14.64 | 379.20 | 0.12 | 2.57 | 1564 |
| 2024-09-20 22:21:41.703 | MS1 | 121.4656684027 | 31.1446242601 | 942 | 504990 | -80.09 | 13.41 | 527.96 | 0.16 | 2.30 | 1568 |
| 2024-09-20 22:21:42.965 | MS1 | 121.4656693154 | 31.1446293966 | 942 | 504990 | -79.81 | 17.70 | 507.74 | 0.13 | 2.83 | 1597 |

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
| 3221608 | 1 | 121.4668712710 | 31.1492404110 | 250 | 8 | 9 | 44.0 | TDD | 369 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3244715 | 2 | 121.4705095832 | 31.1452977126 | 12 | 8 | 7 | 49.5 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3257386 | 3 | 121.4723262023 | 31.1518234150 | 99 | 1 | 7 | 29.8 | TDD | 515 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3276709 | 4 | 121.4669922977 | 31.1493302321 | 306 | 0 | 11 | 24.1 | TDD | 942 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.811 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.826 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.934 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.934 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.626 | NREventA3 | measId:2;ServCellPCI:775;Se... |
| 2024-09-20 22:21:37.866 | NRHandoverAttempt | SourcePCI:775;SourceNR-ARFC... |
| 2024-09-20 22:21:37.896 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.907 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.022 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.022 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221608 | 1 | 18.3878 | 10.3463 | -117.3117 | 13.1925 | 144.5609 | 0.0036 | 0.0007 |
| 2024_09_20 22:00 | 3244715 | 2 | 7.4617 | 18.3924 | -117.3611 | 16.7967 | 127.4307 | 0.0097 | 0.1795 |
| 2024_09_20 22:00 | 3257386 | 3 | 8.5590 | 6.9289 | -116.2666 | 5.7200 | 128.5262 | 0.0076 | 0.0053 |
| 2024_09_20 22:00 | 3276709 | 4 | 11.3901 | 16.6277 | -117.4999 | 7.2655 | 182.0152 | 0.0136 | 0.0172 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415820_F93669D4 | 504990 | 942 | -77.8 | 504990 | 866 | -84.7 | 504990 | 515 | -81.2 | 504990 | 369 |
| MR_1774415820_C8AEF66A | 504990 | 942 | -77.8 | 504990 | 866 | -83.1 | 504990 | 515 | -80.6 | 504990 | 369 |
| MR_1774415820_53B79A56 | 504990 | 942 | -78.8 | 504990 | 866 | -84.0 | 504990 | 515 | -79.9 | 504990 | 369 |
| MR_1774415820_A1CBC3D8 | 504990 | 866 | -84.3 | 504990 | 942 | -79.1 | 504990 | 515 | -81.8 | 504990 | 369 |
| MR_1774415820_A10F0B51 | 504990 | 866 | -83.6 | 504990 | 942 | -80.7 | 504990 | 515 | -79.3 | 504990 | 369 |
| MR_1774415820_81C9400C | 504990 | 866 | -84.8 | 504990 | 942 | -77.3 | 504990 | 515 | -79.9 | 504990 | 369 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 915: `31e1b226-d8c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `31e1b226-d8c9-44f2-901a-440596173a78` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Lift the tilt angle  of 3232418_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[915] topology](images/train_0915.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3225077_1 by 34 degrees
- `C2`: Press down the tilt angle of 3225077_1 by 3 degrees
- `C3`: Add neighbor relationship between 3225077_1 and 3228423_3
- `C4`: Increase transmission power for 3228423_3
- `C5`: Decrease transmission power for 3228423_3
- `C6`: Increase A3 Offset threshold for 3225077_1
- `C7`: Check test server and transmission issues
- `C8`: Decrease A3 Offset threshold for 3228423_3
- `C9`: Add neighbor relationship between 3232418_4 and 3228423_3
- `C10`: Increase transmission power for 3225077_1
- `C11`: Lift the tilt angle  of 3232418_4 by 10 degrees **← 정답**
- `C12`: Increase A3 Offset threshold for 3228423_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228423_3
- `C14`: Press down the tilt angle  of 3232418_4 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3225077_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225077_1
- `C17`: Adjust the azimuth of 3232418_4 by 29 degrees
- `C18`: Decrease transmission power for 3225077_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228423_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225077_1
- `C21`: Lift the tilt angle of 3225077_1 by 3 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.682 | MS1 | 121.4656586260 | 31.1446244310 | 991 | 504990 | -89.17 | 15.55 | 556.53 | 0.04 | 2.71 | 1581 |
| 2024-09-20 22:21:32.495 | MS1 | 121.4656768742 | 31.1446309628 | 991 | 504990 | -90.70 | 12.80 | 507.66 | 0.04 | 2.69 | 1595 |
| 2024-09-20 22:21:33.447 | MS1 | 121.4656749976 | 31.1446252329 | 991 | 504990 | -89.34 | 13.84 | 305.83 | 0.02 | 2.35 | 1595 |
| 2024-09-20 22:21:34.290 | MS1 | 121.4656765787 | 31.1446228430 | 991 | 504990 | -88.27 | 17.10 | 66.15 | 0.10 | 2.51 | 1574 |
| 2024-09-20 22:21:35.322 | MS1 | 121.4656766955 | 31.1446252098 | 991 | 504990 | -87.33 | 17.59 | 52.22 | 0.14 | 2.90 | 1597 |
| 2024-09-20 22:21:36.249 | MS1 | 121.4656657552 | 31.1446199628 | 991 | 504990 | -90.00 | 16.21 | 73.90 | 0.12 | 2.72 | 1587 |
| 2024-09-20 22:21:37.285 | MS1 | 121.4656737933 | 31.1446364611 | 991 | 504990 | -92.00 | 11.87 | 64.73 | 0.16 | 2.92 | 1577 |
| 2024-09-20 22:21:38.222 | MS1 | 121.4656627432 | 31.1446305691 | 991 | 504990 | -92.22 | 9.86 | 66.56 | 0.15 | 2.43 | 1576 |
| 2024-09-20 22:21:39.486 | MS1 | 121.4656696955 | 31.1446247216 | 991 | 504990 | -92.65 | 10.23 | 65.30 | 0.07 | 2.27 | 1590 |
| 2024-09-20 22:21:40.359 | MS1 | 121.4656607961 | 31.1446227933 | 991 | 504990 | -91.19 | 7.62 | 341.08 | 0.19 | 2.24 | 1574 |
| 2024-09-20 22:21:41.664 | MS1 | 121.4656765286 | 31.1446321296 | 991 | 504990 | -90.38 | 7.53 | 316.04 | 0.20 | 2.65 | 1569 |
| 2024-09-20 22:21:42.157 | MS1 | 121.4656759384 | 31.1446190170 | 991 | 504990 | -93.10 | 7.58 | 316.93 | 0.19 | 2.40 | 1570 |

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
| 3225077 | 1 | 121.4707665719 | 31.1447770258 | 234 | 0 | 3 | 24.5 | TDD | 991 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3228423 | 3 | 121.4718843573 | 31.1559042545 | 176 | 13 | 5 | 16.9 | TDD | 292 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3232418 | 4 | 121.4710058294 | 31.1558608636 | 272 | 2 | 11 | 46.4 | TDD | 502 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3279420 | 2 | 121.4708841225 | 31.1531310419 | 20 | 14 | 11 | 29.2 | TDD | 980 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.204 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.219 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.324 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.324 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.015 | NREventA3 | measId:2;ServCellPCI:767;Se... |
| 2024-09-20 22:21:38.255 | NRHandoverAttempt | SourcePCI:767;SourceNR-ARFC... |
| 2024-09-20 22:21:38.304 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.319 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.427 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.427 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225077 | 1 | 80.0478 | 85.2427 | -114.3622 | 18.9198 | 127.2384 | 0.0148 | 0.0005 |
| 2024_09_20 22:00 | 3279420 | 2 | 6.6468 | 6.6534 | -115.2994 | 18.5937 | 129.9373 | 0.0010 | 0.0031 |
| 2024_09_20 22:00 | 3228423 | 3 | 13.0429 | 17.7550 | -114.0115 | 8.7845 | 142.6031 | 0.0129 | 0.0063 |
| 2024_09_20 22:00 | 3232418 | 4 | 6.3816 | 13.2749 | -114.3515 | 7.2112 | 134.4932 | 0.0050 | 0.0160 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412714_3D41C4EC | 504990 | 991 | -89.3 | 504990 | 292 | -91.6 | 504990 | 502 | -98.4 | 504990 | 980 |
| MR_1774412714_803DCDE7 | 504990 | 991 | -88.3 | 504990 | 292 | -90.3 | 504990 | 502 | -100.3 | 504990 | 980 |
| MR_1774412714_986FB57A | 504990 | 991 | -87.8 | 504990 | 292 | -89.7 | 504990 | 502 | -100.7 | 504990 | 980 |
| MR_1774412714_A3BFD7F1 | 504990 | 991 | -90.2 | 504990 | 292 | -89.3 | 504990 | 502 | -98.0 | 504990 | 980 |
| MR_1774412714_AE09624F | 504990 | 991 | -86.3 | 504990 | 292 | -91.8 | 504990 | 502 | -98.8 | 504990 | 980 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 916: `e7fcea03-ded...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e7fcea03-dedb-4bd8-945c-a07d8b8e83ab` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210461_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[916] topology](images/train_0916.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3210461_4
- `C2`: Lift the tilt angle of 3210461_4 by 4 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210461_4 **← 정답**
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210461_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279720_5
- `C6`: Decrease A3 Offset threshold for 3210461_4
- `C7`: Press down the tilt angle of 3210461_4 by 4 degrees
- `C8`: Press down the tilt angle  of 3279720_5 by 4 degrees
- `C9`: Increase A3 Offset threshold for 3210461_4
- `C10`: Add neighbor relationship between 3242752_11 and 3279720_5
- `C11`: Increase transmission power for 3210461_4
- `C12`: Check test server and transmission issues
- `C13`: Decrease transmission power for 3279720_5
- `C14`: Adjust the azimuth of 3210461_4 by 23 degrees
- `C15`: Increase A3 Offset threshold for 3279720_5
- `C16`: Decrease A3 Offset threshold for 3279720_5
- `C17`: Adjust the azimuth of 3279720_5 by 46 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Increase transmission power for 3279720_5
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279720_5
- `C21`: Add neighbor relationship between 3210461_4 and 3279720_5
- `C22`: Lift the tilt angle  of 3279720_5 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.522 | MS1 | 121.4656767683 | 31.1446279764 | 122 | 504990 | -94.89 | 13.40 | 536.15 | 0.06 | 2.66 | 1585 |
| 2024-09-20 22:21:32.591 | MS1 | 121.4656661377 | 31.1446250185 | 926 | 504990 | -95.81 | 10.65 | 310.11 | 0.06 | 2.50 | 1581 |
| 2024-09-20 22:21:33.422 | MS1 | 121.4656679546 | 31.1446239069 | 76 | 504990 | -94.56 | 9.59 | 481.00 | 0.00 | 2.50 | 1583 |
| 2024-09-20 22:21:34.331 | MS1 | 121.4656727562 | 31.1446270600 | 455 | 152650 | -93.56 | 6.00 | 82.35 | 0.16 | 1.71 | 924 |
| 2024-09-20 22:21:35.974 | MS1 | 121.4656609120 | 31.1446378837 | 290 | 152650 | -89.36 | 4.88 | 66.72 | 0.20 | 1.93 | 928 |
| 2024-09-20 22:21:36.296 | MS1 | 121.4656605826 | 31.1446332930 | 240 | 152650 | -88.66 | 2.88 | 93.11 | 0.14 | 1.91 | 930 |
| 2024-09-20 22:21:37.499 | MS1 | 121.4656766076 | 31.1446230805 | 996 | 152650 | -91.95 | 6.38 | 87.26 | 0.17 | 1.50 | 955 |
| 2024-09-20 22:21:38.247 | MS1 | 121.4656581807 | 31.1446259477 | 455 | 152650 | -88.44 | 3.79 | 98.96 | 0.02 | 1.66 | 976 |
| 2024-09-20 22:21:39.513 | MS1 | 121.4656686362 | 31.1446337306 | 290 | 152650 | -87.20 | 6.93 | 52.20 | 0.08 | 1.86 | 975 |
| 2024-09-20 22:21:40.595 | MS1 | 121.4656644713 | 31.1446205004 | 240 | 152650 | -89.11 | 7.94 | 81.12 | 0.17 | 2.28 | 1600 |
| 2024-09-20 22:21:41.206 | MS1 | 121.4656775724 | 31.1446299918 | 996 | 152650 | -88.53 | 2.26 | 68.58 | 0.03 | 2.30 | 1575 |
| 2024-09-20 22:21:42.491 | MS1 | 121.4656594299 | 31.1446329554 | 455 | 152650 | -93.08 | 3.22 | 56.28 | 0.14 | 2.01 | 1599 |

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
| 3210461 | 4 | 121.4712579483 | 31.1530979139 | 232 | 3 | 1 | 16.8 | TDD | 122 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3211598 | 2 | 121.4705582435 | 31.1495394912 | 291 | 7 | 12 | 27.3 | TDD | 76 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3213033 | 8 | 121.4755564808 | 31.1545573594 | 263 | 15 | 11 | 29.7 | FDD | 290 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3224317 | 6 | 121.4726646179 | 31.1463142201 | 209 | 1 | 2 | 28.6 | TDD | 926 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3236809 | 7 | 121.4648646015 | 31.1519499226 | 305 | 10 | 12 | 8.6 | FDD | 448 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3237875 | 3 | 121.4735574495 | 31.1536929558 | 106 | 2 | 7 | 7.1 | TDD | 952 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3242752 | 11 | 121.4641504311 | 31.1495143681 | 42 | 13 | 8 | 0.2 | FDD | 240 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3251130 | 10 | 121.4731432638 | 31.1495645631 | 336 | 13 | 7 | 0.8 | FDD | 455 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3253632 | 13 | 121.4730731953 | 31.1451340436 | 202 | 12 | 7 | 28.2 | FDD | 893 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3267405 | 1 | 121.4661929010 | 31.1543735995 | 31 | 3 | 7 | 19.5 | TDD | 651 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3277066 | 12 | 121.4677529297 | 31.1500935371 | 125 | 12 | 5 | 9.2 | FDD | 281 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3278454 | 9 | 121.4688923212 | 31.1548865546 | 87 | 10 | 0 | 3.0 | FDD | 996 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3279720 | 5 | 121.4643180966 | 31.1536521547 | 219 | 3 | 8 | 11.7 | TDD | 219 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.418 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.442 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.581 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.581 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.257 | NREventA2 | measId:1;ServCellPCI:332;Se... |
| 2024-09-20 22:21:35.401 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.658 | NREventA5 | measId:3;ServCellPCI:332;Se... |
| 2024-09-20 22:21:35.700 | NRHandoverAttempt | SourcePCI:332;SourceNR-ARFC... |
| 2024-09-20 22:21:35.735 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.750 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.861 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.861 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267405 | 1 | 12.9909 | 19.4233 | -117.9503 | 13.2793 | 173.9304 | 0.0121 | 0.0138 |
| 2024_09_20 22:00 | 3211598 | 2 | 8.8990 | 7.1865 | -116.5595 | 15.3060 | 152.7317 | 0.0035 | 0.0026 |
| 2024_09_20 22:00 | 3237875 | 3 | 16.0477 | 17.7585 | -117.6689 | 11.5894 | 156.0319 | 0.0110 | 0.0176 |
| 2024_09_20 22:00 | 3210461 | 4 | 7.4925 | 18.9376 | -115.9048 | 13.8678 | 82.4884 | 0.0098 | 0.0061 |
| 2024_09_20 22:00 | 3279720 | 5 | 14.1520 | 14.5822 | -117.8311 | 9.6034 | 165.8693 | 0.0119 | 0.0085 |
| 2024_09_20 22:00 | 3224317 | 6 | 9.0728 | 11.0803 | -117.6429 | 6.0751 | 146.3319 | 0.0033 | 0.0194 |
| 2024_09_20 22:00 | 3236809 | 7 | 13.0039 | 13.0431 | -114.5920 | 3.0498 | 49.6222 | 0.0071 | 0.0029 |
| 2024_09_20 22:00 | 3213033 | 8 | 13.3777 | 14.3104 | -114.6810 | 3.0980 | 59.2070 | 0.0019 | 0.0102 |
| 2024_09_20 22:00 | 3278454 | 9 | 6.4063 | 16.3723 | -114.1110 | 3.2395 | 22.3849 | 0.0191 | 0.0004 |
| 2024_09_20 22:00 | 3251130 | 10 | 7.6624 | 5.2730 | -114.8389 | 3.8585 | 50.5303 | 0.0101 | 0.0114 |
| 2024_09_20 22:00 | 3242752 | 11 | 10.3885 | 6.0592 | -115.0053 | 3.8556 | 54.1049 | 0.0170 | 0.0179 |
| 2024_09_20 22:00 | 3277066 | 12 | 8.0736 | 8.9268 | -116.7506 | 4.1954 | 41.1634 | 0.0181 | 0.0080 |
| 2024_09_20 22:00 | 3253632 | 13 | 8.7196 | 6.5822 | -115.2130 | 3.9905 | 46.1993 | 0.0077 | 0.0023 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414044_6BB578F9 | 152650 | 455 | -93.3 | 152650 | 448 | -98.8 | 152650 | 893 | -99.6 | 152650 | 281 |
| MR_1774414044_94397047 | 504990 | 76 | -92.7 | 504990 | 219 | -93.5 | 504990 | 651 | -101.9 | 504990 | 952 |
| MR_1774414044_6CFEF1AA | 504990 | 76 | -95.9 | 504990 | 219 | -90.7 | 504990 | 651 | -101.6 | 504990 | 952 |
| MR_1774414044_78A7E58E | 152650 | 455 | -95.0 | 152650 | 448 | -98.2 | 152650 | 893 | -99.5 | 152650 | 281 |
| MR_1774414044_CAF20A83 | 152650 | 455 | -95.1 | 152650 | 448 | -97.7 | 152650 | 893 | -99.6 | 152650 | 281 |
| MR_1774414044_51DEE741 | 152650 | 455 | -94.1 | 152650 | 448 | -99.1 | 152650 | 893 | -99.7 | 152650 | 281 |
| MR_1774414044_267E1B13 | 152650 | 455 | -94.2 | 152650 | 448 | -99.6 | 152650 | 893 | -100.1 | 152650 | 281 |
| MR_1774414044_5F122F68 | 152650 | 455 | -91.7 | 152650 | 448 | -98.5 | 152650 | 893 | -101.6 | 152650 | 281 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 917: `5738e211-b22...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5738e211-b225-4fcf-b8a8-465514b168f3` |
| Tag | **multiple-answer** |
| 정답 | **C6|C18** |
| C6 의미 | Adjust the azimuth of 3243806_2 by 40 degrees |
| C18 의미 | Increase transmission power for 3243806_2 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[917] topology](images/train_0917.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3264333_4
- `C2`: Lift the tilt angle of 3243806_2 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264333_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243806_2
- `C5`: Decrease A3 Offset threshold for 3243806_2
- `C6`: Adjust the azimuth of 3243806_2 by 40 degrees **← 정답**
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243806_2
- `C8`: Add neighbor relationship between 3243806_2 and 3264333_4
- `C9`: Decrease transmission power for 3264333_4
- `C10`: Decrease transmission power for 3243806_2
- `C11`: Increase A3 Offset threshold for 3264333_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264333_4
- `C13`: Press down the tilt angle of 3243806_2 by 10 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Adjust the azimuth of 3264333_4 by 16 degrees
- `C16`: Press down the tilt angle  of 3264333_4 by 5 degrees
- `C17`: Lift the tilt angle  of 3264333_4 by 5 degrees
- `C18`: Increase transmission power for 3243806_2 **← 정답**
- `C19`: Check test server and transmission issues
- `C20`: Decrease A3 Offset threshold for 3264333_4
- `C21`: Add neighbor relationship between 3276014_1 and 3264333_4
- `C22`: Increase A3 Offset threshold for 3243806_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.473 | MS1 | 121.4656667453 | 31.1446350354 | 406 | 504990 | -92.98 | 14.95 | 444.36 | 0.01 | 2.51 | 1592 |
| 2024-09-20 22:21:32.281 | MS1 | 121.4656646441 | 31.1446368677 | 406 | 504990 | -92.95 | 12.40 | 514.06 | 0.09 | 2.09 | 1597 |
| 2024-09-20 22:21:33.799 | MS1 | 121.4656674540 | 31.1446272915 | 406 | 504990 | -91.71 | 12.86 | 568.37 | 0.19 | 2.85 | 1574 |
| 2024-09-20 22:21:34.815 | MS1 | 121.4656777892 | 31.1446321661 | 406 | 504990 | -106.07 | -1.02 | 72.30 | 0.15 | 1.23 | 1582 |
| 2024-09-20 22:21:35.919 | MS1 | 121.4656718496 | 31.1446259674 | 406 | 504990 | -108.65 | 1.89 | 77.52 | 0.13 | 1.34 | 1586 |
| 2024-09-20 22:21:36.635 | MS1 | 121.4656735286 | 31.1446193702 | 406 | 504990 | -104.61 | 1.62 | 58.80 | 0.07 | 1.27 | 1597 |
| 2024-09-20 22:21:37.736 | MS1 | 121.4656647762 | 31.1446273726 | 406 | 504990 | -101.11 | -0.88 | 65.77 | 0.18 | 1.10 | 1591 |
| 2024-09-20 22:21:38.698 | MS1 | 121.4656677534 | 31.1446229862 | 406 | 504990 | -107.17 | -1.28 | 59.43 | 0.15 | 1.47 | 1588 |
| 2024-09-20 22:21:39.580 | MS1 | 121.4656686531 | 31.1446263505 | 406 | 504990 | -107.19 | 0.12 | 52.00 | 0.02 | 1.16 | 1583 |
| 2024-09-20 22:21:40.881 | MS1 | 121.4656731887 | 31.1446377180 | 406 | 504990 | -86.88 | 13.43 | 528.38 | 0.03 | 2.71 | 1597 |
| 2024-09-20 22:21:41.715 | MS1 | 121.4656701435 | 31.1446278988 | 406 | 504990 | -92.31 | 17.69 | 435.29 | 0.14 | 2.47 | 1588 |
| 2024-09-20 22:21:42.154 | MS1 | 121.4656715596 | 31.1446273520 | 406 | 504990 | -93.84 | 12.77 | 333.67 | 0.19 | 2.87 | 1563 |

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
| 3218648 | 3 | 121.4755025310 | 31.1558215947 | 114 | 6 | 9 | 17.9 | TDD | 557 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3243806 | 2 | 121.4666900335 | 31.1486698851 | 152 | 13 | 10 | 24.4 | TDD | 406 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3264333 | 4 | 121.4751267357 | 31.1519857598 | 244 | 4 | 1 | 26.7 | TDD | 694 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3276014 | 1 | 121.4643798102 | 31.1485194917 | 180 | 3 | 5 | 15.6 | TDD | 162 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.402 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.424 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.544 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.544 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.750 | NREventA2 | measId:1;ServCellPCI:488;Se... |
| 2024-09-20 22:21:34.888 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276014 | 1 | 18.1033 | 7.3048 | -115.1995 | 8.4253 | 101.7924 | 0.0148 | 0.0101 |
| 2024_09_20 22:00 | 3243806 | 2 | 8.5292 | 9.7752 | -117.5075 | 17.5281 | 153.0763 | 0.1637 | 0.0147 |
| 2024_09_20 22:00 | 3218648 | 3 | 15.0409 | 17.0814 | -115.4474 | 7.4587 | 174.4100 | 0.0105 | 0.0113 |
| 2024_09_20 22:00 | 3264333 | 4 | 14.5667 | 11.2192 | -116.2614 | 9.8360 | 106.3003 | 0.0071 | 0.0068 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414910_506E7315 | 504990 | 406 | -107.4 | 504990 | 694 | -110.3 | 504990 | 162 | -116.0 | 504990 | 557 |
| MR_1774414910_579FEC64 | 504990 | 406 | -105.9 | 504990 | 694 | -110.9 | 504990 | 162 | -113.9 | 504990 | 557 |
| MR_1774414910_A5EE12EC | 504990 | 406 | -108.0 | 504990 | 694 | -108.3 | 504990 | 162 | -112.7 | 504990 | 557 |
| MR_1774414910_2FF1C3CF | 504990 | 406 | -104.6 | 504990 | 694 | -108.8 | 504990 | 162 | -115.6 | 504990 | 557 |
| MR_1774414910_1DEB5692 | 504990 | 406 | -104.9 | 504990 | 694 | -109.4 | 504990 | 162 | -115.4 | 504990 | 557 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 918: `50bd7ca4-08b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `50bd7ca4-08b6-42a4-85f9-797846d5f195` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Add neighbor relationship between 3261153_3 and 3265678_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[918] topology](images/train_0918.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3261153_3 by 5 degrees
- `C2`: Adjust the azimuth of 3265678_2 by 31 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265678_2
- `C4`: Press down the tilt angle of 3261153_3 by 5 degrees
- `C5`: Increase A3 Offset threshold for 3265678_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265678_2
- `C7`: Decrease A3 Offset threshold for 3261153_3
- `C8`: Increase transmission power for 3265678_2
- `C9`: Add neighbor relationship between 3236573_1 and 3265678_2
- `C10`: Check test server and transmission issues
- `C11`: Increase transmission power for 3261153_3
- `C12`: Decrease transmission power for 3265678_2
- `C13`: Add neighbor relationship between 3261153_3 and 3265678_2 **← 정답**
- `C14`: Adjust the azimuth of 3261153_3 by 50 degrees
- `C15`: Lift the tilt angle  of 3265678_2 by 6 degrees
- `C16`: Press down the tilt angle  of 3265678_2 by 6 degrees
- `C17`: Decrease A3 Offset threshold for 3265678_2
- `C18`: Increase A3 Offset threshold for 3261153_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261153_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261153_3
- `C21`: Decrease transmission power for 3261153_3
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.645 | MS1 | 121.4656727594 | 31.1446227229 | 823 | 504990 | -78.14 | 15.47 | 603.64 | 0.01 | 2.01 | 1594 |
| 2024-09-20 22:21:32.719 | MS1 | 121.4656619230 | 31.1446354987 | 823 | 504990 | -83.99 | 17.74 | 543.54 | 0.01 | 2.73 | 1560 |
| 2024-09-20 22:21:33.960 | MS1 | 121.4656586238 | 31.1446192030 | 823 | 504990 | -82.15 | 12.74 | 329.84 | 0.18 | 2.14 | 1574 |
| 2024-09-20 22:21:34.506 | MS1 | 121.4656731246 | 31.1446269696 | 823 | 504990 | -91.80 | -0.09 | 44.49 | 0.01 | 1.33 | 1587 |
| 2024-09-20 22:21:35.675 | MS1 | 121.4656745017 | 31.1446341993 | 823 | 504990 | -87.88 | -1.62 | 72.25 | 0.01 | 1.38 | 1563 |
| 2024-09-20 22:21:36.292 | MS1 | 121.4656732575 | 31.1446198411 | 823 | 504990 | -85.55 | -0.31 | 37.83 | 0.06 | 1.31 | 1576 |
| 2024-09-20 22:21:37.298 | MS1 | 121.4656649367 | 31.1446245354 | 823 | 504990 | -93.87 | -3.30 | 50.16 | 0.05 | 1.32 | 1599 |
| 2024-09-20 22:21:38.596 | MS1 | 121.4656739589 | 31.1446319012 | 823 | 504990 | -75.76 | 15.89 | 313.90 | 0.04 | 1.24 | 1564 |
| 2024-09-20 22:21:39.880 | MS1 | 121.4656606979 | 31.1446220287 | 823 | 504990 | -75.14 | 13.21 | 496.05 | 0.17 | 1.21 | 1580 |
| 2024-09-20 22:21:40.736 | MS1 | 121.4656735252 | 31.1446305121 | 823 | 504990 | -84.10 | 12.14 | 454.01 | 0.05 | 2.47 | 1560 |
| 2024-09-20 22:21:41.596 | MS1 | 121.4656629909 | 31.1446294457 | 823 | 504990 | -78.23 | 16.36 | 592.01 | 0.04 | 2.39 | 1578 |
| 2024-09-20 22:21:42.798 | MS1 | 121.4656678522 | 31.1446377982 | 823 | 504990 | -80.90 | 17.59 | 403.27 | 0.06 | 2.60 | 1588 |

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
| 3236573 | 1 | 121.4730839314 | 31.1460664963 | 294 | 7 | 11 | 42.4 | TDD | 562 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3238761 | 4 | 121.4642833353 | 31.1458415227 | 27 | 5 | 4 | 31.9 | TDD | 759 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3261153 | 3 | 121.4719440678 | 31.1558788664 | 355 | 3 | 7 | 44.9 | TDD | 823 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3265678 | 2 | 121.4656181987 | 31.1522542659 | 149 | 3 | 6 | 40.5 | TDD | 283 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.938 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.963 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.105 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.105 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.830 | NREventA3 | measId:2;ServCellPCI:539;Se... |
| 2024-09-20 22:21:35.830 | NREventA3 | measId:2;ServCellPCI:539;Se... |
| 2024-09-20 22:21:36.830 | NREventA3 | measId:2;ServCellPCI:539;Se... |
| 2024-09-20 22:21:39.330 | NRRRCReestablishAttempt | PCI:539 |
| 2024-09-20 22:21:39.347 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.360 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.502 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.502 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236573 | 1 | 11.0967 | 10.6216 | -117.5060 | 10.4887 | 107.7102 | 0.0025 | 0.0018 |
| 2024_09_20 22:00 | 3265678 | 2 | 9.1567 | 17.5083 | -114.1854 | 13.2523 | 164.5195 | 0.0149 | 0.0014 |
| 2024_09_20 22:00 | 3261153 | 3 | 13.8174 | 14.3979 | -116.6686 | 17.2148 | 81.2388 | 0.0054 | 0.1297 |
| 2024_09_20 22:00 | 3238761 | 4 | 15.8071 | 5.3666 | -117.9023 | 10.3708 | 113.3356 | 0.0143 | 0.0134 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413987_44D98509 | 504990 | 283 | -89.4 | 504990 | 823 | -91.2 | 504990 | 562 | -93.1 | 504990 | 759 |
| MR_1774413987_F456BAE3 | 504990 | 283 | -87.3 | 504990 | 823 | -93.3 | 504990 | 562 | -93.2 | 504990 | 759 |
| MR_1774413987_50B8E76A | 504990 | 283 | -85.8 | 504990 | 823 | -91.8 | 504990 | 562 | -93.1 | 504990 | 759 |
| MR_1774413987_E1098B4C | 504990 | 823 | -92.0 | 504990 | 283 | -87.6 | 504990 | 562 | -96.6 | 504990 | 759 |
| MR_1774413987_C8C4EA56 | 504990 | 283 | -86.8 | 504990 | 823 | -93.8 | 504990 | 562 | -95.8 | 504990 | 759 |
| MR_1774413987_B342659F | 504990 | 283 | -88.5 | 504990 | 823 | -90.2 | 504990 | 562 | -94.2 | 504990 | 759 |
| MR_1774413987_6C7B8DBA | 504990 | 283 | -87.9 | 504990 | 823 | -90.1 | 504990 | 562 | -96.2 | 504990 | 759 |
| MR_1774413987_A94CDD95 | 504990 | 823 | -91.5 | 504990 | 283 | -86.1 | 504990 | 562 | -95.6 | 504990 | 759 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 919: `46de010f-263...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `46de010f-263a-45f5-a5d2-d50e34dcefe7` |
| Tag | **multiple-answer** |
| 정답 | **C4|C10|C11|C20** |
| C4 의미 | Decrease transmission power for 3262930_5 |
| C10 의미 | Increase A3 Offset threshold for 3262930_5 |
| C11 의미 | Increase A3 Offset threshold for 3234967_4 |
| C20 의미 | Press down the tilt angle  of 3262930_5 by 4 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[919] topology](images/train_0919.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3234967_4
- `C2`: Adjust the azimuth of 3234967_4 by 15 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234967_4
- `C4`: Decrease transmission power for 3262930_5 **← 정답**
- `C5`: Lift the tilt angle of 3234967_4 by 5 degrees
- `C6`: Check test server and transmission issues
- `C7`: Increase transmission power for 3234967_4
- `C8`: Decrease A3 Offset threshold for 3262930_5
- `C9`: Press down the tilt angle of 3234967_4 by 5 degrees
- `C10`: Increase A3 Offset threshold for 3262930_5 **← 정답**
- `C11`: Increase A3 Offset threshold for 3234967_4 **← 정답**
- `C12`: Add neighbor relationship between 3234967_4 and 3262930_5
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262930_5
- `C14`: Lift the tilt angle  of 3262930_5 by 4 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262930_5
- `C16`: Adjust the azimuth of 3262930_5 by 25 degrees
- `C17`: Add neighbor relationship between 3241357_2 and 3262930_5
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease transmission power for 3234967_4
- `C20`: Press down the tilt angle  of 3262930_5 by 4 degrees **← 정답**
- `C21`: Increase transmission power for 3262930_5
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234967_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.882 | MS1 | 121.4656585463 | 31.1446287928 | 534 | 504990 | -80.24 | 13.28 | 366.02 | 0.19 | 2.03 | 1576 |
| 2024-09-20 22:21:32.312 | MS1 | 121.4656710305 | 31.1446284054 | 534 | 504990 | -79.01 | 12.88 | 346.61 | 0.05 | 2.16 | 1570 |
| 2024-09-20 22:21:33.634 | MS1 | 121.4656606421 | 31.1446331416 | 534 | 504990 | -80.28 | 12.09 | 329.29 | 0.02 | 2.81 | 1592 |
| 2024-09-20 22:21:34.208 | MS1 | 121.4656607867 | 31.1446235578 | 553 | 504990 | -89.49 | 1.26 | 48.77 | 0.14 | 1.31 | 1590 |
| 2024-09-20 22:21:35.110 | MS1 | 121.4656682281 | 31.1446334627 | 553 | 504990 | -82.51 | 3.77 | 35.01 | 0.15 | 1.28 | 1570 |
| 2024-09-20 22:21:36.773 | MS1 | 121.4656663146 | 31.1446294121 | 534 | 504990 | -86.78 | 2.94 | 53.97 | 0.14 | 1.48 | 1572 |
| 2024-09-20 22:21:37.971 | MS1 | 121.4656764020 | 31.1446377856 | 534 | 504990 | -84.32 | 3.02 | 70.90 | 0.07 | 1.25 | 1560 |
| 2024-09-20 22:21:38.898 | MS1 | 121.4656741050 | 31.1446333134 | 553 | 504990 | -80.85 | 3.46 | 69.61 | 0.04 | 1.12 | 1600 |
| 2024-09-20 22:21:39.184 | MS1 | 121.4656744711 | 31.1446304400 | 553 | 504990 | -86.87 | 1.23 | 74.83 | 0.08 | 1.27 | 1593 |
| 2024-09-20 22:21:40.723 | MS1 | 121.4656606993 | 31.1446244463 | 553 | 504990 | -83.38 | 14.60 | 594.14 | 0.17 | 2.26 | 1570 |
| 2024-09-20 22:21:41.745 | MS1 | 121.4656686962 | 31.1446367878 | 553 | 504990 | -81.61 | 17.21 | 479.37 | 0.04 | 2.33 | 1586 |
| 2024-09-20 22:21:42.957 | MS1 | 121.4656721052 | 31.1446249777 | 553 | 504990 | -76.46 | 12.85 | 398.04 | 0.05 | 2.40 | 1596 |

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
| 3234967 | 4 | 121.4711589438 | 31.1556013388 | 218 | 3 | 5 | 39.8 | TDD | 534 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3241357 | 2 | 121.4748800629 | 31.1468751063 | 335 | 0 | 1 | 34.3 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3241647 | 3 | 121.4744993185 | 31.1544240698 | 104 | 11 | 12 | 48.0 | TDD | 277 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3257764 | 1 | 121.4689133393 | 31.1466846344 | 203 | 7 | 2 | 30.7 | TDD | 553 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3262930 | 5 | 121.4727432136 | 31.1540928672 | 188 | 2 | 7 | 33.2 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.489 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.636 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.636 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.291 | NREventA3 | measId:2;ServCellPCI:808;Se... |
| 2024-09-20 22:21:34.531 | NRHandoverAttempt | SourcePCI:808;SourceNR-ARFC... |
| 2024-09-20 22:21:34.561 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.574 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:34.680 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.680 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.291 | NREventA3 | measId:2;ServCellPCI:182;Se... |
| 2024-09-20 22:21:36.531 | NRHandoverAttempt | SourcePCI:182;SourceNR-ARFC... |
| 2024-09-20 22:21:36.570 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.581 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.705 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.705 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.291 | NREventA3 | measId:2;ServCellPCI:808;Se... |
| 2024-09-20 22:21:38.531 | NRHandoverAttempt | SourcePCI:808;SourceNR-ARFC... |
| 2024-09-20 22:21:38.572 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.583 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.691 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.691 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257764 | 1 | 10.9500 | 13.6673 | -114.0223 | 13.3365 | 192.1078 | 0.0028 | 0.0176 |
| 2024_09_20 22:00 | 3241357 | 2 | 19.3072 | 18.5421 | -115.8196 | 10.9580 | 155.2617 | 0.0137 | 0.0140 |
| 2024_09_20 22:00 | 3241647 | 3 | 13.6665 | 10.5936 | -117.1232 | 12.8379 | 121.6410 | 0.0068 | 0.0183 |
| 2024_09_20 22:00 | 3234967 | 4 | 19.5372 | 17.7711 | -114.7276 | 14.7532 | 119.2382 | 0.0081 | 0.0158 |
| 2024_09_20 22:00 | 3262930 | 5 | 13.7195 | 5.1941 | -116.3853 | 15.6286 | 131.7378 | 0.0013 | 0.0196 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414682_2ADF6A8C | 504990 | 553 | -91.1 | 504990 | 534 | -91.8 | 504990 | 382 | -95.2 | 504990 | 309 |
| MR_1774414682_96378C6B | 504990 | 534 | -88.4 | 504990 | 553 | -89.8 | 504990 | 382 | -94.8 | 504990 | 309 |
| MR_1774414682_F3D17FE4 | 504990 | 553 | -88.9 | 504990 | 534 | -92.4 | 504990 | 382 | -93.8 | 504990 | 309 |
| MR_1774414682_FB588CBB | 504990 | 534 | -87.9 | 504990 | 553 | -91.0 | 504990 | 382 | -94.5 | 504990 | 309 |
| MR_1774414682_F23A1071 | 504990 | 553 | -90.4 | 504990 | 534 | -91.1 | 504990 | 382 | -92.5 | 504990 | 309 |
| MR_1774414682_6D5462A0 | 504990 | 534 | -90.6 | 504990 | 553 | -88.9 | 504990 | 382 | -93.1 | 504990 | 309 |

> *... 2개 열 생략 (전체 14열)*

---
