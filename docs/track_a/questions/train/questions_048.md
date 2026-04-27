# Track A 문제 분석 — train[470]~train[479]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[470] ~ train[479] (10개)

## 목차

1. [문제 470: `cc406aa5-938...`](#470) — single-answer, 정답: C17
2. [문제 471: `973d50b2-30b...`](#471) — single-answer, 정답: C22
3. [문제 472: `5a1aa619-ac6...`](#472) — single-answer, 정답: C14
4. [문제 473: `5725ac00-d22...`](#473) — single-answer, 정답: C12
5. [문제 474: `b41bb46b-ec6...`](#474) — single-answer, 정답: C12
6. [문제 475: `9d99b57a-645...`](#475) — multiple-answer, 정답: C8|C14
7. [문제 476: `052c75fe-1bf...`](#476) — single-answer, 정답: C16
8. [문제 477: `e1c827c9-3b5...`](#477) — single-answer, 정답: C17
9. [문제 478: `6761b803-c03...`](#478) — single-answer, 정답: C15
10. [문제 479: `8df726bc-e0a...`](#479) — single-answer, 정답: C17

---

### 문제 470: `cc406aa5-938...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cc406aa5-9380-4fcf-8fd2-9e1d41c145f0` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275639_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[470] topology](images/train_0470.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3275639_6 by 1 degrees
- `C2`: Decrease A3 Offset threshold for 3257783_5
- `C3`: Press down the tilt angle  of 3257783_5 by 0 degrees
- `C4`: Decrease A3 Offset threshold for 3275639_6
- `C5`: Increase A3 Offset threshold for 3257783_5
- `C6`: Check test server and transmission issues
- `C7`: Lift the tilt angle of 3275639_6 by 1 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257783_5
- `C9`: Lift the tilt angle  of 3257783_5 by 0 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257783_5
- `C11`: Decrease transmission power for 3257783_5
- `C12`: Adjust the azimuth of 3257783_5 by 38 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Add neighbor relationship between 3279168_8 and 3257783_5
- `C15`: Adjust the azimuth of 3275639_6 by 46 degrees
- `C16`: Increase transmission power for 3257783_5
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275639_6 **← 정답**
- `C18`: Increase transmission power for 3275639_6
- `C19`: Decrease transmission power for 3275639_6
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275639_6
- `C21`: Increase A3 Offset threshold for 3275639_6
- `C22`: Add neighbor relationship between 3275639_6 and 3257783_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.265 | MS1 | 121.4656749679 | 31.1446318166 | 829 | 504990 | -95.21 | 11.45 | 317.59 | 0.16 | 2.07 | 1590 |
| 2024-09-20 22:21:32.902 | MS1 | 121.4656699898 | 31.1446317294 | 808 | 504990 | -94.94 | 9.73 | 464.40 | 0.06 | 2.23 | 1600 |
| 2024-09-20 22:21:33.506 | MS1 | 121.4656693718 | 31.1446209091 | 326 | 504990 | -95.69 | 10.10 | 495.27 | 0.13 | 2.80 | 1565 |
| 2024-09-20 22:21:34.118 | MS1 | 121.4656620280 | 31.1446284927 | 522 | 152650 | -95.96 | 4.79 | 76.08 | 0.20 | 1.95 | 921 |
| 2024-09-20 22:21:35.518 | MS1 | 121.4656617280 | 31.1446219538 | 946 | 152650 | -89.25 | 7.07 | 58.02 | 0.15 | 1.82 | 907 |
| 2024-09-20 22:21:36.678 | MS1 | 121.4656735307 | 31.1446325485 | 361 | 152650 | -87.63 | 6.48 | 66.14 | 0.00 | 1.68 | 930 |
| 2024-09-20 22:21:37.712 | MS1 | 121.4656696922 | 31.1446253141 | 393 | 152650 | -95.07 | 6.98 | 92.10 | 0.03 | 1.99 | 985 |
| 2024-09-20 22:21:38.894 | MS1 | 121.4656701027 | 31.1446335590 | 522 | 152650 | -96.93 | 3.42 | 81.44 | 0.12 | 1.56 | 998 |
| 2024-09-20 22:21:39.715 | MS1 | 121.4656609716 | 31.1446268540 | 946 | 152650 | -89.93 | 4.58 | 77.37 | 0.14 | 1.62 | 997 |
| 2024-09-20 22:21:40.786 | MS1 | 121.4656613372 | 31.1446373947 | 361 | 152650 | -89.72 | 2.18 | 75.68 | 0.19 | 2.28 | 1579 |
| 2024-09-20 22:21:41.904 | MS1 | 121.4656723864 | 31.1446180586 | 393 | 152650 | -90.29 | 6.90 | 72.34 | 0.05 | 2.44 | 1596 |
| 2024-09-20 22:21:42.849 | MS1 | 121.4656627929 | 31.1446353452 | 522 | 152650 | -92.88 | 6.29 | 64.66 | 0.18 | 2.12 | 1596 |

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
| 3229908 | 4 | 121.4681110704 | 31.1481726459 | 22 | 7 | 0 | 23.7 | TDD | 622 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3238990 | 3 | 121.4687439102 | 31.1450949892 | 48 | 14 | 11 | 23.9 | TDD | 525 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3251639 | 9 | 121.4679863397 | 31.1447478247 | 2 | 3 | 1 | 13.8 | FDD | 522 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3257783 | 5 | 121.4653187496 | 31.1559688585 | 141 | 0 | 12 | 5.8 | TDD | 976 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3261220 | 10 | 121.4716944279 | 31.1473529796 | 352 | 8 | 8 | 3.8 | FDD | 393 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3262030 | 1 | 121.4706047285 | 31.1501615305 | 341 | 0 | 0 | 28.7 | TDD | 326 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3262556 | 13 | 121.4711308008 | 31.1508986730 | 150 | 10 | 2 | 23.5 | FDD | 29 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3266983 | 12 | 121.4737220600 | 31.1495942848 | 223 | 3 | 1 | 23.2 | FDD | 472 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3268574 | 11 | 121.4686117702 | 31.1501096888 | 228 | 12 | 12 | 21.6 | FDD | 946 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3270407 | 7 | 121.4755409200 | 31.1501812911 | 293 | 11 | 1 | 13.6 | FDD | 804 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3272722 | 2 | 121.4755289405 | 31.1553112054 | 175 | 2 | 7 | 27.4 | TDD | 808 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3275639 | 6 | 121.4757279082 | 31.1514903398 | 185 | 1 | 12 | 0.2 | TDD | 829 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3279168 | 8 | 121.4732712250 | 31.1527412674 | 180 | 11 | 1 | 15.7 | FDD | 361 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |

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
| 2024-09-20 22:21:31.539 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.560 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.688 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.688 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.349 | NREventA2 | measId:1;ServCellPCI:897;Se... |
| 2024-09-20 22:21:35.487 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.703 | NREventA5 | measId:3;ServCellPCI:897;Se... |
| 2024-09-20 22:21:35.733 | NRHandoverAttempt | SourcePCI:897;SourceNR-ARFC... |
| 2024-09-20 22:21:35.755 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.768 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.897 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.897 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262030 | 1 | 13.2963 | 19.2596 | -117.1659 | 11.3800 | 156.4919 | 0.0030 | 0.0198 |
| 2024_09_20 22:00 | 3272722 | 2 | 10.8961 | 15.8959 | -117.9230 | 19.8378 | 189.0401 | 0.0126 | 0.0113 |
| 2024_09_20 22:00 | 3238990 | 3 | 16.4582 | 9.4409 | -117.9580 | 10.5415 | 199.3951 | 0.0125 | 0.0130 |
| 2024_09_20 22:00 | 3229908 | 4 | 14.6163 | 5.5131 | -114.9068 | 14.8881 | 81.1971 | 0.0078 | 0.0113 |
| 2024_09_20 22:00 | 3257783 | 5 | 13.8115 | 12.1708 | -115.3687 | 14.6079 | 92.0263 | 0.0027 | 0.0092 |
| 2024_09_20 22:00 | 3275639 | 6 | 9.6578 | 5.4997 | -116.7962 | 11.1329 | 80.8130 | 0.0069 | 0.0141 |
| 2024_09_20 22:00 | 3270407 | 7 | 15.0943 | 10.8242 | -114.1803 | 3.0417 | 42.1349 | 0.0007 | 0.0146 |
| 2024_09_20 22:00 | 3279168 | 8 | 14.3377 | 14.1382 | -117.5080 | 3.8205 | 58.0264 | 0.0048 | 0.0130 |
| 2024_09_20 22:00 | 3251639 | 9 | 12.2838 | 10.7212 | -114.8549 | 4.4239 | 50.5125 | 0.0097 | 0.0046 |
| 2024_09_20 22:00 | 3261220 | 10 | 14.8674 | 13.3689 | -117.1969 | 3.4629 | 56.5189 | 0.0096 | 0.0017 |
| 2024_09_20 22:00 | 3268574 | 11 | 17.6573 | 7.7617 | -114.0678 | 4.4257 | 21.4549 | 0.0101 | 0.0056 |
| 2024_09_20 22:00 | 3266983 | 12 | 13.4688 | 12.6224 | -117.3615 | 4.0195 | 55.2261 | 0.0175 | 0.0076 |
| 2024_09_20 22:00 | 3262556 | 13 | 11.9089 | 9.3521 | -115.0447 | 3.4211 | 31.1574 | 0.0029 | 0.0130 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412712_92B627DC | 152650 | 522 | -94.9 | 152650 | 29 | -97.3 | 152650 | 804 | -103.2 | 152650 | 472 |
| MR_1774412712_438A48E6 | 504990 | 326 | -97.2 | 504990 | 976 | -99.0 | 504990 | 622 | -99.4 | 504990 | 525 |
| MR_1774412712_8597F436 | 504990 | 326 | -95.7 | 504990 | 976 | -96.3 | 504990 | 622 | -100.4 | 504990 | 525 |
| MR_1774412712_6ABFAF1F | 152650 | 522 | -96.3 | 152650 | 29 | -97.9 | 152650 | 804 | -105.0 | 152650 | 472 |
| MR_1774412712_F8744431 | 152650 | 522 | -97.5 | 152650 | 29 | -100.4 | 152650 | 804 | -105.6 | 152650 | 472 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 471: `973d50b2-30b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `973d50b2-30b2-4733-9d22-e22a33a529c0` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3239160_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[471] topology](images/train_0471.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Add neighbor relationship between 3273226_2 and 3210483_1
- `C3`: Adjust the azimuth of 3210483_1 by 50 degrees
- `C4`: Add neighbor relationship between 3239160_4 and 3210483_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239160_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210483_1
- `C7`: Lift the tilt angle  of 3210483_1 by 7 degrees
- `C8`: Decrease transmission power for 3239160_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210483_1
- `C10`: Lift the tilt angle of 3239160_4 by 2 degrees
- `C11`: Increase transmission power for 3210483_1
- `C12`: Increase A3 Offset threshold for 3239160_4
- `C13`: Press down the tilt angle  of 3210483_1 by 7 degrees
- `C14`: Increase transmission power for 3239160_4
- `C15`: Check test server and transmission issues
- `C16`: Decrease A3 Offset threshold for 3239160_4
- `C17`: Decrease A3 Offset threshold for 3210483_1
- `C18`: Adjust the azimuth of 3239160_4 by 39 degrees
- `C19`: Press down the tilt angle of 3239160_4 by 2 degrees
- `C20`: Increase A3 Offset threshold for 3210483_1
- `C21`: Decrease transmission power for 3210483_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239160_4 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.155 | MS1 | 121.4656676255 | 31.1446233857 | 797 | 504990 | -90.17 | 15.42 | 395.66 | 0.13 | 2.16 | 1567 |
| 2024-09-20 22:21:32.691 | MS1 | 121.4656758697 | 31.1446237051 | 797 | 504990 | -91.59 | 16.81 | 367.46 | 0.06 | 2.14 | 1583 |
| 2024-09-20 22:21:33.221 | MS1 | 121.4656637621 | 31.1446284318 | 797 | 504990 | -90.01 | 17.90 | 569.45 | 0.05 | 2.07 | 1592 |
| 2024-09-20 22:21:34.106 | MS1 | 121.4656673489 | 31.1446230448 | 797 | 504990 | -85.21 | 13.37 | 87.32 | 0.50 | 2.21 | 655 |
| 2024-09-20 22:21:35.488 | MS1 | 121.4656763123 | 31.1446307324 | 797 | 504990 | -85.88 | 14.85 | 53.96 | 0.59 | 2.84 | 600 |
| 2024-09-20 22:21:36.442 | MS1 | 121.4656778935 | 31.1446199245 | 797 | 504990 | -89.71 | 13.60 | 82.36 | 0.60 | 2.05 | 664 |
| 2024-09-20 22:21:37.337 | MS1 | 121.4656730545 | 31.1446259429 | 797 | 504990 | -89.09 | 9.36 | 63.65 | 0.69 | 2.87 | 510 |
| 2024-09-20 22:21:38.722 | MS1 | 121.4656596993 | 31.1446304340 | 797 | 504990 | -90.57 | 8.94 | 76.58 | 0.69 | 2.67 | 535 |
| 2024-09-20 22:21:39.434 | MS1 | 121.4656580299 | 31.1446307752 | 797 | 504990 | -89.13 | 12.61 | 76.93 | 0.68 | 2.64 | 615 |
| 2024-09-20 22:21:40.519 | MS1 | 121.4656666663 | 31.1446209864 | 797 | 504990 | -93.56 | 11.70 | 556.88 | 0.08 | 2.81 | 1563 |
| 2024-09-20 22:21:41.204 | MS1 | 121.4656712667 | 31.1446289133 | 797 | 504990 | -91.94 | 10.64 | 584.48 | 0.15 | 2.98 | 1585 |
| 2024-09-20 22:21:42.155 | MS1 | 121.4656729032 | 31.1446373206 | 797 | 504990 | -91.49 | 8.03 | 381.56 | 0.09 | 2.29 | 1570 |

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
| 3210483 | 1 | 121.4706437141 | 31.1476590831 | 71 | 3 | 12 | 44.4 | TDD | 376 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3238653 | 3 | 121.4651738909 | 31.1529543021 | 39 | 5 | 0 | 34.0 | TDD | 985 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3239160 | 4 | 121.4757379049 | 31.1552125224 | 258 | 1 | 0 | 25.1 | TDD | 797 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3273226 | 2 | 121.4739193220 | 31.1557597494 | 30 | 13 | 6 | 30.7 | TDD | 737 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.464 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.483 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.596 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.596 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.295 | NREventA3 | measId:2;ServCellPCI:97;Ser... |
| 2024-09-20 22:21:38.535 | NRHandoverAttempt | SourcePCI:97;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.568 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.581 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.720 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.720 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210483 | 1 | 8.5829 | 12.6192 | -117.5973 | 9.9032 | 169.1123 | 0.0100 | 0.0061 |
| 2024_09_20 22:00 | 3273226 | 2 | 18.4152 | 14.4737 | -114.7537 | 12.3815 | 100.3650 | 0.0001 | 0.0039 |
| 2024_09_20 22:00 | 3238653 | 3 | 10.6882 | 17.9024 | -115.4318 | 12.8823 | 102.8683 | 0.0177 | 0.0083 |
| 2024_09_20 22:00 | 3239160 | 4 | 18.5758 | 10.8794 | -114.5970 | 10.5412 | 82.8239 | 0.0129 | 0.0123 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416984_30AC1DF0 | 504990 | 797 | -84.3 | 504990 | 376 | -91.4 | 504990 | 737 | -94.1 | 504990 | 985 |
| MR_1774416984_B6ABB5CD | 504990 | 797 | -86.2 | 504990 | 376 | -94.1 | 504990 | 737 | -94.7 | 504990 | 985 |
| MR_1774416984_161E51C8 | 504990 | 797 | -84.3 | 504990 | 376 | -92.4 | 504990 | 737 | -95.6 | 504990 | 985 |
| MR_1774416984_8BF90792 | 504990 | 797 | -84.0 | 504990 | 376 | -92.0 | 504990 | 737 | -93.4 | 504990 | 985 |
| MR_1774416984_425D43B6 | 504990 | 797 | -85.4 | 504990 | 376 | -92.8 | 504990 | 737 | -95.6 | 504990 | 985 |
| MR_1774416984_275F93AE | 504990 | 797 | -85.0 | 504990 | 376 | -94.7 | 504990 | 737 | -94.2 | 504990 | 985 |
| MR_1774416984_5E426F25 | 504990 | 797 | -86.8 | 504990 | 376 | -94.7 | 504990 | 737 | -95.7 | 504990 | 985 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 472: `5a1aa619-ac6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5a1aa619-ac6b-44e4-8f8f-2c8d35cad2e8` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Lift the tilt angle  of 3273607_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[472] topology](images/train_0472.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3263203_1
- `C2`: Increase A3 Offset threshold for 3261991_2
- `C3`: Adjust the azimuth of 3273607_3 by 49 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263203_1
- `C5`: Adjust the azimuth of 3263203_1 by 42 degrees
- `C6`: Press down the tilt angle of 3263203_1 by 6 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease transmission power for 3261991_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263203_1
- `C10`: Decrease A3 Offset threshold for 3263203_1
- `C11`: Press down the tilt angle  of 3273607_3 by 10 degrees
- `C12`: Check test server and transmission issues
- `C13`: Increase A3 Offset threshold for 3263203_1
- `C14`: Lift the tilt angle  of 3273607_3 by 10 degrees **← 정답**
- `C15`: Lift the tilt angle of 3263203_1 by 6 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261991_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261991_2
- `C18`: Decrease transmission power for 3263203_1
- `C19`: Increase transmission power for 3261991_2
- `C20`: Add neighbor relationship between 3263203_1 and 3261991_2
- `C21`: Add neighbor relationship between 3273607_3 and 3261991_2
- `C22`: Decrease A3 Offset threshold for 3261991_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.820 | MS1 | 121.4656696423 | 31.1446324816 | 282 | 504990 | -91.39 | 16.38 | 385.10 | 0.07 | 2.18 | 1577 |
| 2024-09-20 22:21:32.676 | MS1 | 121.4656607007 | 31.1446286297 | 282 | 504990 | -88.02 | 17.45 | 360.97 | 0.08 | 2.45 | 1581 |
| 2024-09-20 22:21:33.317 | MS1 | 121.4656773204 | 31.1446347222 | 282 | 504990 | -87.24 | 15.57 | 473.97 | 0.11 | 2.19 | 1575 |
| 2024-09-20 22:21:34.917 | MS1 | 121.4656724687 | 31.1446228043 | 282 | 504990 | -88.76 | 12.06 | 60.46 | 0.14 | 2.64 | 1575 |
| 2024-09-20 22:21:35.543 | MS1 | 121.4656691786 | 31.1446239394 | 282 | 504990 | -88.17 | 13.17 | 96.52 | 0.07 | 2.77 | 1572 |
| 2024-09-20 22:21:36.128 | MS1 | 121.4656765001 | 31.1446267846 | 282 | 504990 | -88.50 | 12.37 | 58.57 | 0.09 | 2.66 | 1600 |
| 2024-09-20 22:21:37.176 | MS1 | 121.4656710849 | 31.1446209653 | 282 | 504990 | -93.29 | 7.63 | 47.67 | 0.11 | 2.80 | 1560 |
| 2024-09-20 22:21:38.399 | MS1 | 121.4656728283 | 31.1446364434 | 282 | 504990 | -93.10 | 7.24 | 95.59 | 0.03 | 2.85 | 1571 |
| 2024-09-20 22:21:39.910 | MS1 | 121.4656749078 | 31.1446275509 | 282 | 504990 | -89.05 | 9.29 | 57.91 | 0.01 | 2.80 | 1591 |
| 2024-09-20 22:21:40.272 | MS1 | 121.4656754385 | 31.1446279471 | 282 | 504990 | -92.55 | 9.55 | 519.46 | 0.12 | 2.98 | 1593 |
| 2024-09-20 22:21:41.212 | MS1 | 121.4656765285 | 31.1446282969 | 282 | 504990 | -91.64 | 8.54 | 444.23 | 0.13 | 2.50 | 1597 |
| 2024-09-20 22:21:42.285 | MS1 | 121.4656654930 | 31.1446191128 | 282 | 504990 | -93.00 | 10.45 | 497.56 | 0.04 | 2.11 | 1566 |

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
| 3211487 | 4 | 121.4656780463 | 31.1491608285 | 59 | 3 | 4 | 24.9 | TDD | 998 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3261991 | 2 | 121.4658609275 | 31.1490549444 | 133 | 14 | 10 | 24.2 | TDD | 899 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3263203 | 1 | 121.4646517761 | 31.1471297935 | 203 | 2 | 10 | 18.5 | TDD | 282 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3273607 | 3 | 121.4693509353 | 31.1509404310 | 77 | 14 | 3 | 25.0 | TDD | 758 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.433 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.450 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.594 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.594 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.267 | NREventA3 | measId:2;ServCellPCI:747;Se... |
| 2024-09-20 22:21:38.507 | NRHandoverAttempt | SourcePCI:747;SourceNR-ARFC... |
| 2024-09-20 22:21:38.552 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.562 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.671 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.671 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263203 | 1 | 81.1873 | 91.1217 | -115.2785 | 5.3730 | 186.8094 | 0.0069 | 0.0163 |
| 2024_09_20 22:00 | 3261991 | 2 | 9.5493 | 16.1642 | -116.2470 | 17.5422 | 91.5192 | 0.0143 | 0.0004 |
| 2024_09_20 22:00 | 3273607 | 3 | 14.7519 | 13.8926 | -116.9801 | 15.3419 | 187.2208 | 0.0065 | 0.0183 |
| 2024_09_20 22:00 | 3211487 | 4 | 5.1872 | 7.8987 | -115.9125 | 12.9033 | 168.1608 | 0.0079 | 0.0050 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412745_6F4C494E | 504990 | 282 | -87.7 | 504990 | 899 | -86.9 | 504990 | 758 | -99.2 | 504990 | 998 |
| MR_1774412745_7EDF8682 | 504990 | 282 | -88.1 | 504990 | 899 | -90.2 | 504990 | 758 | -97.4 | 504990 | 998 |
| MR_1774412745_81FA26E9 | 504990 | 282 | -89.0 | 504990 | 899 | -89.1 | 504990 | 758 | -97.3 | 504990 | 998 |
| MR_1774412745_595D1DF4 | 504990 | 282 | -89.9 | 504990 | 899 | -87.9 | 504990 | 758 | -99.3 | 504990 | 998 |
| MR_1774412745_2FD4B26D | 504990 | 282 | -89.9 | 504990 | 899 | -90.1 | 504990 | 758 | -100.8 | 504990 | 998 |
| MR_1774412745_204C8508 | 504990 | 282 | -88.4 | 504990 | 899 | -87.6 | 504990 | 758 | -100.5 | 504990 | 998 |
| MR_1774412745_47C2985E | 504990 | 282 | -89.7 | 504990 | 899 | -88.2 | 504990 | 758 | -99.4 | 504990 | 998 |
| MR_1774412745_834796BD | 504990 | 282 | -88.4 | 504990 | 899 | -89.8 | 504990 | 758 | -97.3 | 504990 | 998 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 473: `5725ac00-d22...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5725ac00-d220-4b2b-ade0-4e3058fbc68e` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3278192_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[473] topology](images/train_0473.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3234326_3 by 10 degrees
- `C2`: Increase transmission power for 3234326_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234326_3
- `C4`: Decrease A3 Offset threshold for 3278192_1
- `C5`: Decrease transmission power for 3234326_3
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Lift the tilt angle of 3278192_1 by 3 degrees
- `C8`: Check test server and transmission issues
- `C9`: Add neighbor relationship between 3278192_1 and 3234326_3
- `C10`: Add neighbor relationship between 3249491_4 and 3234326_3
- `C11`: Increase A3 Offset threshold for 3278192_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278192_1 **← 정답**
- `C13`: Press down the tilt angle of 3278192_1 by 3 degrees
- `C14`: Increase transmission power for 3278192_1
- `C15`: Adjust the azimuth of 3278192_1 by 8 degrees
- `C16`: Adjust the azimuth of 3234326_3 by 50 degrees
- `C17`: Decrease transmission power for 3278192_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278192_1
- `C19`: Increase A3 Offset threshold for 3234326_3
- `C20`: Decrease A3 Offset threshold for 3234326_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234326_3
- `C22`: Lift the tilt angle  of 3234326_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.714 | MS1 | 121.4656619262 | 31.1446336085 | 922 | 504990 | -89.46 | 13.64 | 389.05 | 0.06 | 2.29 | 1563 |
| 2024-09-20 22:21:32.775 | MS1 | 121.4656648289 | 31.1446277750 | 922 | 504990 | -86.88 | 12.61 | 447.67 | 0.00 | 2.06 | 1573 |
| 2024-09-20 22:21:33.659 | MS1 | 121.4656636183 | 31.1446363051 | 922 | 504990 | -86.18 | 14.46 | 555.64 | 0.09 | 2.04 | 1584 |
| 2024-09-20 22:21:34.506 | MS1 | 121.4656737880 | 31.1446256365 | 922 | 504990 | -86.74 | 14.44 | 85.35 | 0.52 | 2.70 | 628 |
| 2024-09-20 22:21:35.731 | MS1 | 121.4656582080 | 31.1446237338 | 922 | 504990 | -86.29 | 16.54 | 66.36 | 0.68 | 2.64 | 500 |
| 2024-09-20 22:21:36.836 | MS1 | 121.4656721162 | 31.1446327607 | 922 | 504990 | -85.72 | 16.83 | 66.99 | 0.65 | 2.57 | 660 |
| 2024-09-20 22:21:37.352 | MS1 | 121.4656589642 | 31.1446364378 | 922 | 504990 | -92.73 | 11.62 | 52.83 | 0.65 | 2.95 | 681 |
| 2024-09-20 22:21:38.229 | MS1 | 121.4656767418 | 31.1446253462 | 922 | 504990 | -89.51 | 10.81 | 46.57 | 0.53 | 2.37 | 565 |
| 2024-09-20 22:21:39.512 | MS1 | 121.4656731761 | 31.1446231304 | 922 | 504990 | -90.22 | 10.62 | 65.02 | 0.57 | 2.92 | 614 |
| 2024-09-20 22:21:40.876 | MS1 | 121.4656691118 | 31.1446339237 | 922 | 504990 | -92.15 | 11.41 | 502.57 | 0.02 | 2.17 | 1564 |
| 2024-09-20 22:21:41.248 | MS1 | 121.4656760401 | 31.1446325755 | 922 | 504990 | -93.46 | 12.78 | 431.93 | 0.02 | 2.27 | 1592 |
| 2024-09-20 22:21:42.447 | MS1 | 121.4656594329 | 31.1446337181 | 922 | 504990 | -91.42 | 8.30 | 536.91 | 0.10 | 2.35 | 1583 |

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
| 3234326 | 3 | 121.4656518289 | 31.1448246791 | 0 | 2 | 10 | 50.0 | TDD | 68 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3249491 | 4 | 121.4644758664 | 31.1548377599 | 62 | 12 | 0 | 41.7 | TDD | 702 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3256552 | 2 | 121.4655542916 | 31.1526657366 | 78 | 1 | 3 | 47.9 | TDD | 139 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3278192 | 1 | 121.4704468057 | 31.1556088859 | 192 | 1 | 3 | 39.2 | TDD | 922 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.559 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.574 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.697 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.697 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.421 | NREventA3 | measId:2;ServCellPCI:951;Se... |
| 2024-09-20 22:21:38.661 | NRHandoverAttempt | SourcePCI:951;SourceNR-ARFC... |
| 2024-09-20 22:21:38.703 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.718 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.842 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.842 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278192 | 1 | 11.7909 | 12.6518 | -116.2701 | 12.9961 | 141.5280 | 0.0137 | 0.0109 |
| 2024_09_20 22:00 | 3256552 | 2 | 13.4827 | 11.3444 | -114.9864 | 19.0034 | 103.3393 | 0.0106 | 0.0047 |
| 2024_09_20 22:00 | 3234326 | 3 | 7.0180 | 7.1988 | -115.5007 | 14.9657 | 154.9542 | 0.0157 | 0.0174 |
| 2024_09_20 22:00 | 3249491 | 4 | 13.9723 | 12.4133 | -116.1414 | 7.5724 | 146.7389 | 0.0008 | 0.0160 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416896_B0E691F5 | 504990 | 922 | -87.4 | 504990 | 68 | -91.8 | 504990 | 702 | -98.6 | 504990 | 139 |
| MR_1774416896_174EA0D6 | 504990 | 922 | -88.3 | 504990 | 68 | -90.7 | 504990 | 702 | -100.2 | 504990 | 139 |
| MR_1774416896_4F1D2590 | 504990 | 922 | -88.3 | 504990 | 68 | -88.6 | 504990 | 702 | -99.2 | 504990 | 139 |
| MR_1774416896_5B835028 | 504990 | 922 | -85.6 | 504990 | 68 | -91.5 | 504990 | 702 | -98.2 | 504990 | 139 |
| MR_1774416896_FBDFF620 | 504990 | 922 | -88.5 | 504990 | 68 | -90.8 | 504990 | 702 | -101.0 | 504990 | 139 |
| MR_1774416896_FDEE93EC | 504990 | 922 | -88.6 | 504990 | 68 | -90.3 | 504990 | 702 | -102.0 | 504990 | 139 |
| MR_1774416896_126A8B0E | 504990 | 922 | -87.9 | 504990 | 68 | -92.0 | 504990 | 702 | -98.9 | 504990 | 139 |
| MR_1774416896_92C2C389 | 504990 | 922 | -88.5 | 504990 | 68 | -90.2 | 504990 | 702 | -98.5 | 504990 | 139 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 474: `b41bb46b-ec6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b41bb46b-ec68-40f3-ae32-c0b31e01f342` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212068_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[474] topology](images/train_0474.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3212068_1
- `C2`: Decrease transmission power for 3224249_5
- `C3`: Increase transmission power for 3224249_5
- `C4`: Check test server and transmission issues
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224249_5
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224249_5
- `C7`: Decrease A3 Offset threshold for 3212068_1
- `C8`: Press down the tilt angle of 3212068_1 by 1 degrees
- `C9`: Press down the tilt angle  of 3224249_5 by 0 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212068_1
- `C11`: Adjust the azimuth of 3224249_5 by 27 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212068_1 **← 정답**
- `C13`: Adjust the azimuth of 3212068_1 by 39 degrees
- `C14`: Increase A3 Offset threshold for 3224249_5
- `C15`: Lift the tilt angle of 3212068_1 by 1 degrees
- `C16`: Decrease A3 Offset threshold for 3224249_5
- `C17`: Add neighbor relationship between 3235663_11 and 3224249_5
- `C18`: Decrease transmission power for 3212068_1
- `C19`: Increase A3 Offset threshold for 3212068_1
- `C20`: Add neighbor relationship between 3212068_1 and 3224249_5
- `C21`: Lift the tilt angle  of 3224249_5 by 0 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.505 | MS1 | 121.4656666567 | 31.1446336263 | 129 | 504990 | -95.47 | 14.81 | 425.78 | 0.17 | 2.58 | 1587 |
| 2024-09-20 22:21:32.951 | MS1 | 121.4656762096 | 31.1446297155 | 8 | 504990 | -95.51 | 9.31 | 392.37 | 0.02 | 2.30 | 1570 |
| 2024-09-20 22:21:33.498 | MS1 | 121.4656590770 | 31.1446228653 | 653 | 504990 | -93.94 | 9.08 | 315.21 | 0.08 | 2.58 | 1585 |
| 2024-09-20 22:21:34.173 | MS1 | 121.4656779190 | 31.1446299535 | 645 | 152650 | -90.59 | 7.07 | 87.88 | 0.08 | 1.75 | 939 |
| 2024-09-20 22:21:35.596 | MS1 | 121.4656640877 | 31.1446370655 | 451 | 152650 | -96.88 | 5.21 | 88.09 | 0.00 | 1.73 | 916 |
| 2024-09-20 22:21:36.124 | MS1 | 121.4656591593 | 31.1446221759 | 495 | 152650 | -87.49 | 3.13 | 97.08 | 0.17 | 1.72 | 901 |
| 2024-09-20 22:21:37.790 | MS1 | 121.4656680510 | 31.1446332066 | 427 | 152650 | -91.81 | 6.04 | 56.61 | 0.15 | 1.85 | 993 |
| 2024-09-20 22:21:38.628 | MS1 | 121.4656765036 | 31.1446210944 | 645 | 152650 | -87.66 | 6.28 | 89.43 | 0.05 | 1.62 | 992 |
| 2024-09-20 22:21:39.930 | MS1 | 121.4656711431 | 31.1446185956 | 451 | 152650 | -95.25 | 7.29 | 71.43 | 0.16 | 1.93 | 960 |
| 2024-09-20 22:21:40.708 | MS1 | 121.4656678640 | 31.1446259528 | 495 | 152650 | -94.32 | 5.82 | 73.04 | 0.16 | 2.11 | 1563 |
| 2024-09-20 22:21:41.735 | MS1 | 121.4656663744 | 31.1446298974 | 427 | 152650 | -87.26 | 5.28 | 96.20 | 0.03 | 2.48 | 1573 |
| 2024-09-20 22:21:42.270 | MS1 | 121.4656738412 | 31.1446323312 | 645 | 152650 | -88.94 | 5.24 | 65.69 | 0.19 | 2.72 | 1580 |

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
| 3212068 | 1 | 121.4644983941 | 31.1519410857 | 211 | 0 | 2 | 7.7 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3217387 | 4 | 121.4678461135 | 31.1491562247 | 309 | 3 | 11 | 14.3 | TDD | 653 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3224249 | 5 | 121.4759059647 | 31.1532651476 | 198 | 0 | 10 | 6.8 | TDD | 465 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3228678 | 8 | 121.4674426315 | 31.1506450733 | 343 | 11 | 2 | 7.8 | FDD | 645 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3233688 | 10 | 121.4643066461 | 31.1472789494 | 223 | 6 | 5 | 20.0 | FDD | 395 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3235663 | 11 | 121.4757381745 | 31.1516176757 | 117 | 13 | 3 | 29.0 | FDD | 495 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3244000 | 7 | 121.4736757799 | 31.1488702039 | 61 | 0 | 8 | 2.3 | FDD | 451 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3247578 | 12 | 121.4685813138 | 31.1494275137 | 211 | 3 | 7 | 21.8 | FDD | 156 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3249862 | 9 | 121.4646719494 | 31.1509067799 | 358 | 3 | 6 | 29.9 | FDD | 427 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3252511 | 13 | 121.4699157899 | 31.1551620070 | 159 | 3 | 7 | 13.5 | FDD | 638 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3271794 | 2 | 121.4709424261 | 31.1502109124 | 35 | 6 | 2 | 28.5 | TDD | 614 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3273716 | 3 | 121.4664953597 | 31.1459676254 | 202 | 11 | 10 | 6.7 | TDD | 8 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3274076 | 6 | 121.4681186370 | 31.1495182345 | 194 | 15 | 2 | 10.7 | TDD | 629 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.214 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.229 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.373 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.373 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.113 | NREventA2 | measId:1;ServCellPCI:668;Se... |
| 2024-09-20 22:21:35.245 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.532 | NREventA5 | measId:3;ServCellPCI:668;Se... |
| 2024-09-20 22:21:35.578 | NRHandoverAttempt | SourcePCI:668;SourceNR-ARFC... |
| 2024-09-20 22:21:35.610 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.622 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.759 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.759 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212068 | 1 | 19.7465 | 15.5218 | -117.4901 | 8.8761 | 89.8488 | 0.0083 | 0.0085 |
| 2024_09_20 22:00 | 3271794 | 2 | 14.8430 | 16.7652 | -114.3394 | 13.2862 | 150.9077 | 0.0030 | 0.0063 |
| 2024_09_20 22:00 | 3273716 | 3 | 17.4453 | 13.0529 | -117.9310 | 12.3749 | 177.0358 | 0.0196 | 0.0018 |
| 2024_09_20 22:00 | 3217387 | 4 | 12.8542 | 7.4527 | -117.9796 | 9.1605 | 124.7548 | 0.0068 | 0.0144 |
| 2024_09_20 22:00 | 3224249 | 5 | 8.1281 | 19.1180 | -115.1505 | 10.9803 | 124.0609 | 0.0158 | 0.0100 |
| 2024_09_20 22:00 | 3274076 | 6 | 17.3447 | 8.9627 | -114.2922 | 14.2345 | 143.5792 | 0.0073 | 0.0011 |
| 2024_09_20 22:00 | 3244000 | 7 | 12.3662 | 12.4483 | -117.6816 | 3.9569 | 43.5845 | 0.0005 | 0.0046 |
| 2024_09_20 22:00 | 3228678 | 8 | 19.2120 | 12.8722 | -115.6848 | 3.9929 | 22.5564 | 0.0004 | 0.0060 |
| 2024_09_20 22:00 | 3249862 | 9 | 6.4056 | 12.4906 | -115.4551 | 4.9688 | 21.7358 | 0.0032 | 0.0041 |
| 2024_09_20 22:00 | 3233688 | 10 | 18.8178 | 5.6571 | -117.9716 | 4.2996 | 26.8589 | 0.0132 | 0.0193 |
| 2024_09_20 22:00 | 3235663 | 11 | 5.6576 | 16.7224 | -114.9011 | 4.6113 | 24.2787 | 0.0146 | 0.0192 |
| 2024_09_20 22:00 | 3247578 | 12 | 15.8768 | 13.9431 | -115.9510 | 4.5601 | 58.1182 | 0.0023 | 0.0104 |
| 2024_09_20 22:00 | 3252511 | 13 | 16.0794 | 14.4256 | -114.5232 | 4.7667 | 45.5233 | 0.0068 | 0.0051 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416173_D79E0BCB | 152650 | 645 | -89.1 | 152650 | 638 | -94.0 | 152650 | 395 | -98.4 | 152650 | 156 |
| MR_1774416173_18E78FCA | 152650 | 645 | -90.0 | 152650 | 638 | -93.4 | 152650 | 395 | -100.6 | 152650 | 156 |
| MR_1774416173_E737F826 | 504990 | 653 | -92.5 | 504990 | 465 | -94.9 | 504990 | 629 | -93.3 | 504990 | 614 |
| MR_1774416173_FC98FC71 | 152650 | 645 | -91.4 | 152650 | 638 | -94.4 | 152650 | 395 | -97.8 | 152650 | 156 |
| MR_1774416173_3F4EA533 | 504990 | 653 | -93.2 | 504990 | 465 | -92.8 | 504990 | 629 | -95.3 | 504990 | 614 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 475: `9d99b57a-645...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9d99b57a-645e-4aa1-9228-1f7aaaa49540` |
| Tag | **multiple-answer** |
| 정답 | **C8|C14** |
| C8 의미 | Press down the tilt angle  of 3238456_3 by 3 degrees |
| C14 의미 | Decrease transmission power for 3238456_3 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[475] topology](images/train_0475.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3238456_3 by 14 degrees
- `C2`: Add neighbor relationship between 3233214_1 and 3238456_3
- `C3`: Increase A3 Offset threshold for 3233214_1
- `C4`: Add neighbor relationship between 3213972_4 and 3238456_3
- `C5`: Decrease transmission power for 3233214_1
- `C6`: Lift the tilt angle of 3233214_1 by 5 degrees
- `C7`: Adjust the azimuth of 3233214_1 by 7 degrees
- `C8`: Press down the tilt angle  of 3238456_3 by 3 degrees **← 정답**
- `C9`: Increase transmission power for 3238456_3
- `C10`: Press down the tilt angle of 3233214_1 by 5 degrees
- `C11`: Lift the tilt angle  of 3238456_3 by 3 degrees
- `C12`: Decrease A3 Offset threshold for 3233214_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233214_1
- `C14`: Decrease transmission power for 3238456_3 **← 정답**
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238456_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233214_1
- `C17`: Check test server and transmission issues
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238456_3
- `C19`: Increase A3 Offset threshold for 3238456_3
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease A3 Offset threshold for 3238456_3
- `C22`: Increase transmission power for 3233214_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.532 | MS1 | 121.4656635481 | 31.1446302651 | 504 | 504990 | -75.37 | 14.01 | 384.62 | 0.08 | 2.50 | 1563 |
| 2024-09-20 22:21:32.911 | MS1 | 121.4656649835 | 31.1446229979 | 504 | 504990 | -82.04 | 12.44 | 447.56 | 0.16 | 2.31 | 1590 |
| 2024-09-20 22:21:33.688 | MS1 | 121.4656580388 | 31.1446222273 | 504 | 504990 | -83.09 | 17.45 | 586.01 | 0.06 | 2.24 | 1567 |
| 2024-09-20 22:21:34.454 | MS1 | 121.4656745333 | 31.1446290281 | 504 | 504990 | -86.84 | 0.98 | 88.25 | 0.09 | 1.42 | 1589 |
| 2024-09-20 22:21:35.234 | MS1 | 121.4656736754 | 31.1446281424 | 504 | 504990 | -88.85 | 1.24 | 57.52 | 0.00 | 1.05 | 1589 |
| 2024-09-20 22:21:36.150 | MS1 | 121.4656732812 | 31.1446359529 | 504 | 504990 | -90.39 | 2.14 | 65.90 | 0.04 | 1.29 | 1563 |
| 2024-09-20 22:21:37.781 | MS1 | 121.4656602833 | 31.1446274869 | 504 | 504990 | -93.87 | 2.97 | 40.62 | 0.07 | 1.04 | 1569 |
| 2024-09-20 22:21:38.510 | MS1 | 121.4656637448 | 31.1446203909 | 504 | 504990 | -93.86 | 0.69 | 82.55 | 0.17 | 1.29 | 1593 |
| 2024-09-20 22:21:39.389 | MS1 | 121.4656748399 | 31.1446222878 | 504 | 504990 | -94.74 | 0.94 | 72.84 | 0.17 | 1.28 | 1600 |
| 2024-09-20 22:21:40.356 | MS1 | 121.4656669511 | 31.1446227361 | 504 | 504990 | -82.74 | 12.89 | 566.92 | 0.00 | 2.58 | 1565 |
| 2024-09-20 22:21:41.993 | MS1 | 121.4656672608 | 31.1446315868 | 504 | 504990 | -75.57 | 16.17 | 487.22 | 0.12 | 2.36 | 1563 |
| 2024-09-20 22:21:42.603 | MS1 | 121.4656663710 | 31.1446213053 | 504 | 504990 | -78.38 | 13.86 | 486.27 | 0.14 | 2.57 | 1570 |

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
| 3213972 | 4 | 121.4700923905 | 31.1440868712 | 292 | 6 | 9 | 33.0 | TDD | 739 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3233214 | 1 | 121.4665825412 | 31.1497985199 | 196 | 2 | 12 | 28.5 | TDD | 504 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3238456 | 3 | 121.4644066459 | 31.1534396830 | 159 | 0 | 6 | 49.8 | TDD | 971 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3258868 | 2 | 121.4682318531 | 31.1446195338 | 273 | 5 | 3 | 30.2 | TDD | 241 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.561 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.580 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.728 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.728 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233214 | 1 | 15.6583 | 9.3052 | -108.4079 | 8.1945 | 175.0943 | 0.0105 | 0.0070 |
| 2024_09_20 22:00 | 3258868 | 2 | 12.1486 | 13.3119 | -114.7058 | 8.1542 | 169.4025 | 0.0117 | 0.0150 |
| 2024_09_20 22:00 | 3238456 | 3 | 15.7757 | 13.3756 | -117.9270 | 15.5596 | 115.1357 | 0.0158 | 0.0071 |
| 2024_09_20 22:00 | 3213972 | 4 | 14.3789 | 16.7073 | -115.5386 | 9.3213 | 82.2233 | 0.0034 | 0.0084 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414205_C56BBE54 | 504990 | 504 | -85.1 | 504990 | 971 | -85.2 | 504990 | 739 | -85.6 | 504990 | 241 |
| MR_1774414205_C62BA6C0 | 504990 | 504 | -88.8 | 504990 | 971 | -87.5 | 504990 | 739 | -88.8 | 504990 | 241 |
| MR_1774414205_85491FA7 | 504990 | 504 | -87.8 | 504990 | 971 | -85.1 | 504990 | 739 | -85.5 | 504990 | 241 |
| MR_1774414205_310ECC4E | 504990 | 971 | -87.5 | 504990 | 504 | -86.1 | 504990 | 739 | -88.5 | 504990 | 241 |
| MR_1774414205_BB1C9720 | 504990 | 504 | -88.4 | 504990 | 971 | -85.2 | 504990 | 739 | -85.5 | 504990 | 241 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 476: `052c75fe-1bf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `052c75fe-1bfc-4338-a69a-9f01b64ff0f1` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279750_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[476] topology](images/train_0476.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3279750_1
- `C2`: Increase transmission power for 3236861_4
- `C3`: Increase A3 Offset threshold for 3279750_1
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Adjust the azimuth of 3279750_1 by 42 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279750_1
- `C7`: Increase transmission power for 3279750_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236861_4
- `C9`: Increase A3 Offset threshold for 3236861_4
- `C10`: Add neighbor relationship between 3279750_1 and 3236861_4
- `C11`: Add neighbor relationship between 3267165_8 and 3236861_4
- `C12`: Press down the tilt angle of 3279750_1 by 1 degrees
- `C13`: Lift the tilt angle  of 3236861_4 by 5 degrees
- `C14`: Decrease A3 Offset threshold for 3236861_4
- `C15`: Lift the tilt angle of 3279750_1 by 1 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279750_1 **← 정답**
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236861_4
- `C18`: Decrease A3 Offset threshold for 3279750_1
- `C19`: Check test server and transmission issues
- `C20`: Adjust the azimuth of 3236861_4 by 29 degrees
- `C21`: Decrease transmission power for 3236861_4
- `C22`: Press down the tilt angle  of 3236861_4 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.595 | MS1 | 121.4656706538 | 31.1446224164 | 230 | 504990 | -95.29 | 11.31 | 449.18 | 0.08 | 2.37 | 1576 |
| 2024-09-20 22:21:32.615 | MS1 | 121.4656764420 | 31.1446331078 | 857 | 504990 | -94.94 | 9.87 | 563.05 | 0.09 | 2.83 | 1591 |
| 2024-09-20 22:21:33.787 | MS1 | 121.4656684410 | 31.1446271528 | 45 | 504990 | -94.12 | 13.83 | 541.40 | 0.16 | 2.25 | 1574 |
| 2024-09-20 22:21:34.113 | MS1 | 121.4656639191 | 31.1446224506 | 314 | 152650 | -87.72 | 3.56 | 68.65 | 0.10 | 1.80 | 901 |
| 2024-09-20 22:21:35.905 | MS1 | 121.4656685540 | 31.1446340219 | 826 | 152650 | -96.95 | 6.95 | 98.20 | 0.01 | 1.98 | 995 |
| 2024-09-20 22:21:36.524 | MS1 | 121.4656637399 | 31.1446206283 | 462 | 152650 | -89.34 | 6.32 | 65.73 | 0.15 | 1.86 | 994 |
| 2024-09-20 22:21:37.201 | MS1 | 121.4656686873 | 31.1446279722 | 975 | 152650 | -88.15 | 5.62 | 45.65 | 0.12 | 1.78 | 910 |
| 2024-09-20 22:21:38.647 | MS1 | 121.4656707452 | 31.1446353645 | 314 | 152650 | -88.38 | 3.41 | 52.72 | 0.12 | 1.63 | 980 |
| 2024-09-20 22:21:39.489 | MS1 | 121.4656673617 | 31.1446302431 | 826 | 152650 | -91.91 | 6.94 | 98.67 | 0.01 | 1.94 | 927 |
| 2024-09-20 22:21:40.111 | MS1 | 121.4656705911 | 31.1446345581 | 462 | 152650 | -90.55 | 4.52 | 80.52 | 0.05 | 2.43 | 1592 |
| 2024-09-20 22:21:41.976 | MS1 | 121.4656680411 | 31.1446300291 | 975 | 152650 | -89.40 | 7.73 | 47.98 | 0.05 | 2.83 | 1586 |
| 2024-09-20 22:21:42.609 | MS1 | 121.4656627831 | 31.1446265789 | 314 | 152650 | -93.21 | 4.42 | 62.29 | 0.09 | 2.91 | 1581 |

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
| 3213090 | 12 | 121.4744409603 | 31.1462985940 | 252 | 13 | 8 | 3.2 | FDD | 314 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3225759 | 11 | 121.4667953169 | 31.1458073155 | 264 | 1 | 10 | 1.3 | FDD | 468 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3236861 | 4 | 121.4658341099 | 31.1451677870 | 166 | 3 | 1 | 1.9 | TDD | 536 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3237315 | 10 | 121.4714844632 | 31.1443091748 | 146 | 0 | 2 | 17.3 | FDD | 464 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3237900 | 2 | 121.4656801285 | 31.1490211742 | 199 | 0 | 10 | 29.4 | TDD | 45 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3252300 | 6 | 121.4648975744 | 31.1479135338 | 179 | 13 | 10 | 26.4 | TDD | 186 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3259772 | 13 | 121.4673064591 | 31.1453403885 | 148 | 7 | 10 | 14.2 | FDD | 826 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3265485 | 7 | 121.4698595848 | 31.1443887921 | 28 | 4 | 0 | 16.1 | FDD | 421 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3266907 | 5 | 121.4671686692 | 31.1532913623 | 8 | 3 | 11 | 3.9 | TDD | 857 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3267165 | 8 | 121.4650502871 | 31.1537428696 | 278 | 11 | 5 | 10.9 | FDD | 462 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3277146 | 3 | 121.4687677384 | 31.1525208071 | 155 | 11 | 10 | 18.8 | TDD | 55 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3279038 | 9 | 121.4744317321 | 31.1526344139 | 191 | 4 | 5 | 23.9 | FDD | 975 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3279750 | 1 | 121.4703916804 | 31.1530848440 | 164 | 1 | 1 | 5.1 | TDD | 230 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.107 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.126 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.270 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.270 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.998 | NREventA2 | measId:1;ServCellPCI:665;Se... |
| 2024-09-20 22:21:35.135 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.363 | NREventA5 | measId:3;ServCellPCI:665;Se... |
| 2024-09-20 22:21:35.405 | NRHandoverAttempt | SourcePCI:665;SourceNR-ARFC... |
| 2024-09-20 22:21:35.434 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.446 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.586 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.586 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279750 | 1 | 18.5532 | 14.7866 | -114.0282 | 18.1501 | 138.1296 | 0.0127 | 0.0194 |
| 2024_09_20 22:00 | 3237900 | 2 | 15.0045 | 13.4681 | -114.6516 | 18.1032 | 179.2065 | 0.0020 | 0.0037 |
| 2024_09_20 22:00 | 3277146 | 3 | 8.5418 | 17.6740 | -115.8724 | 12.4021 | 116.7068 | 0.0141 | 0.0180 |
| 2024_09_20 22:00 | 3236861 | 4 | 12.2810 | 16.2753 | -115.4873 | 14.0235 | 155.7981 | 0.0114 | 0.0007 |
| 2024_09_20 22:00 | 3266907 | 5 | 6.2019 | 7.7749 | -114.3212 | 19.8828 | 179.1951 | 0.0157 | 0.0106 |
| 2024_09_20 22:00 | 3252300 | 6 | 18.4554 | 17.7048 | -115.7939 | 6.4571 | 115.5978 | 0.0135 | 0.0050 |
| 2024_09_20 22:00 | 3265485 | 7 | 17.5923 | 12.0282 | -115.2552 | 3.6053 | 45.9111 | 0.0125 | 0.0020 |
| 2024_09_20 22:00 | 3267165 | 8 | 5.9211 | 15.9302 | -115.4930 | 4.1639 | 52.7710 | 0.0160 | 0.0085 |
| 2024_09_20 22:00 | 3279038 | 9 | 6.8830 | 8.8726 | -117.3645 | 3.9454 | 56.1930 | 0.0138 | 0.0119 |
| 2024_09_20 22:00 | 3237315 | 10 | 8.5187 | 10.6848 | -115.4527 | 3.2000 | 43.0887 | 0.0150 | 0.0192 |
| 2024_09_20 22:00 | 3225759 | 11 | 19.1333 | 15.8459 | -117.6746 | 4.1471 | 43.5682 | 0.0057 | 0.0035 |
| 2024_09_20 22:00 | 3213090 | 12 | 17.7631 | 12.7959 | -115.4216 | 4.6469 | 58.3781 | 0.0006 | 0.0194 |
| 2024_09_20 22:00 | 3259772 | 13 | 8.6142 | 8.7688 | -115.7127 | 4.5777 | 24.6437 | 0.0149 | 0.0059 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414670_29E67F18 | 504990 | 45 | -93.2 | 504990 | 536 | -97.6 | 504990 | 186 | -97.2 | 504990 | 55 |
| MR_1774414670_EB79B992 | 152650 | 314 | -87.5 | 152650 | 464 | -92.0 | 152650 | 468 | -96.0 | 152650 | 421 |
| MR_1774414670_DF251444 | 152650 | 314 | -89.7 | 152650 | 464 | -91.8 | 152650 | 468 | -98.1 | 152650 | 421 |
| MR_1774414670_EFBDC57E | 504990 | 45 | -95.3 | 504990 | 536 | -97.7 | 504990 | 186 | -97.7 | 504990 | 55 |
| MR_1774414670_183A9574 | 504990 | 45 | -93.1 | 504990 | 536 | -94.5 | 504990 | 186 | -95.7 | 504990 | 55 |
| MR_1774414670_DF77E870 | 504990 | 45 | -92.2 | 504990 | 536 | -95.4 | 504990 | 186 | -94.7 | 504990 | 55 |
| MR_1774414670_3125BC0B | 152650 | 314 | -88.2 | 152650 | 464 | -94.1 | 152650 | 468 | -94.3 | 152650 | 421 |
| MR_1774414670_BE437D31 | 152650 | 314 | -89.4 | 152650 | 464 | -94.7 | 152650 | 468 | -96.2 | 152650 | 421 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 477: `e1c827c9-3b5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e1c827c9-3b50-4610-a489-db004179f0ea` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215921_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[477] topology](images/train_0477.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3215921_4 and 3234699_1
- `C2`: Increase transmission power for 3234699_1
- `C3`: Decrease A3 Offset threshold for 3215921_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234699_1
- `C5`: Increase A3 Offset threshold for 3215921_4
- `C6`: Adjust the azimuth of 3234699_1 by 23 degrees
- `C7`: Lift the tilt angle of 3215921_4 by 1 degrees
- `C8`: Adjust the azimuth of 3215921_4 by 45 degrees
- `C9`: Increase transmission power for 3215921_4
- `C10`: Decrease transmission power for 3234699_1
- `C11`: Decrease A3 Offset threshold for 3234699_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234699_1
- `C13`: Press down the tilt angle of 3215921_4 by 1 degrees
- `C14`: Press down the tilt angle  of 3234699_1 by 6 degrees
- `C15`: Increase A3 Offset threshold for 3234699_1
- `C16`: Lift the tilt angle  of 3234699_1 by 6 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215921_4 **← 정답**
- `C18`: Decrease transmission power for 3215921_4
- `C19`: Check test server and transmission issues
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215921_4
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Add neighbor relationship between 3224493_11 and 3234699_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.813 | MS1 | 121.4656617710 | 31.1446301035 | 49 | 504990 | -93.44 | 12.40 | 410.47 | 0.13 | 2.95 | 1599 |
| 2024-09-20 22:21:32.416 | MS1 | 121.4656713400 | 31.1446327548 | 12 | 504990 | -93.31 | 14.91 | 520.12 | 0.06 | 2.59 | 1598 |
| 2024-09-20 22:21:33.617 | MS1 | 121.4656621483 | 31.1446289515 | 370 | 504990 | -95.47 | 11.02 | 550.52 | 0.16 | 2.10 | 1573 |
| 2024-09-20 22:21:34.655 | MS1 | 121.4656591397 | 31.1446314791 | 241 | 152650 | -96.75 | 6.12 | 76.10 | 0.19 | 1.66 | 942 |
| 2024-09-20 22:21:35.708 | MS1 | 121.4656726632 | 31.1446341589 | 603 | 152650 | -93.55 | 6.89 | 85.29 | 0.08 | 1.56 | 973 |
| 2024-09-20 22:21:36.568 | MS1 | 121.4656667313 | 31.1446300455 | 728 | 152650 | -92.17 | 6.13 | 99.88 | 0.07 | 1.84 | 969 |
| 2024-09-20 22:21:37.697 | MS1 | 121.4656590527 | 31.1446232283 | 181 | 152650 | -92.29 | 4.80 | 52.32 | 0.14 | 1.72 | 982 |
| 2024-09-20 22:21:38.226 | MS1 | 121.4656728520 | 31.1446268937 | 241 | 152650 | -93.03 | 7.16 | 90.35 | 0.09 | 1.77 | 997 |
| 2024-09-20 22:21:39.317 | MS1 | 121.4656598876 | 31.1446330998 | 603 | 152650 | -94.76 | 4.43 | 80.00 | 0.03 | 1.69 | 982 |
| 2024-09-20 22:21:40.596 | MS1 | 121.4656603419 | 31.1446321103 | 728 | 152650 | -93.94 | 7.60 | 86.64 | 0.01 | 2.23 | 1566 |
| 2024-09-20 22:21:41.831 | MS1 | 121.4656584417 | 31.1446335543 | 181 | 152650 | -90.49 | 7.00 | 77.24 | 0.15 | 2.64 | 1579 |
| 2024-09-20 22:21:42.646 | MS1 | 121.4656709801 | 31.1446254975 | 241 | 152650 | -96.02 | 6.56 | 72.26 | 0.03 | 2.66 | 1578 |

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
| 3215921 | 4 | 121.4742280105 | 31.1451326452 | 221 | 1 | 4 | 3.6 | TDD | 49 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3224493 | 11 | 121.4653247654 | 31.1480895634 | 66 | 14 | 5 | 25.9 | FDD | 728 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3232192 | 5 | 121.4726855912 | 31.1475912277 | 254 | 12 | 1 | 6.5 | TDD | 370 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3234699 | 1 | 121.4661661073 | 31.1526469167 | 160 | 4 | 7 | 24.7 | TDD | 647 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3234980 | 3 | 121.4741429213 | 31.1522547262 | 273 | 6 | 8 | 22.9 | TDD | 12 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3237733 | 7 | 121.4701392523 | 31.1550697754 | 325 | 2 | 1 | 5.4 | FDD | 517 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3238682 | 2 | 121.4672153666 | 31.1468156715 | 187 | 15 | 11 | 0.8 | TDD | 521 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3252294 | 10 | 121.4641154817 | 31.1492002801 | 200 | 2 | 11 | 27.1 | FDD | 181 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3253263 | 9 | 121.4758483718 | 31.1463158569 | 331 | 7 | 6 | 16.4 | FDD | 51 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3265601 | 12 | 121.4743734868 | 31.1482201200 | 251 | 14 | 11 | 19.3 | FDD | 603 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3267502 | 8 | 121.4670771198 | 31.1475609721 | 119 | 0 | 0 | 14.9 | FDD | 241 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3274488 | 6 | 121.4746850360 | 31.1490969712 | 184 | 2 | 2 | 2.1 | TDD | 849 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3274608 | 13 | 121.4709681816 | 31.1533948089 | 149 | 0 | 4 | 15.8 | FDD | 735 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |

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
| 2024-09-20 22:21:31.389 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.409 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.529 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.529 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.282 | NREventA2 | measId:1;ServCellPCI:665;Se... |
| 2024-09-20 22:21:35.394 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.605 | NREventA5 | measId:3;ServCellPCI:665;Se... |
| 2024-09-20 22:21:35.682 | NRHandoverAttempt | SourcePCI:665;SourceNR-ARFC... |
| 2024-09-20 22:21:35.710 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.722 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.842 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.842 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234699 | 1 | 15.5337 | 17.3983 | -114.1788 | 12.7104 | 129.0957 | 0.0105 | 0.0175 |
| 2024_09_20 22:00 | 3238682 | 2 | 16.1848 | 19.3626 | -117.7870 | 7.4075 | 144.8488 | 0.0004 | 0.0003 |
| 2024_09_20 22:00 | 3234980 | 3 | 19.7256 | 7.3977 | -116.7384 | 12.0909 | 193.8423 | 0.0042 | 0.0071 |
| 2024_09_20 22:00 | 3215921 | 4 | 13.4568 | 14.6018 | -114.8640 | 17.9533 | 191.5672 | 0.0105 | 0.0111 |
| 2024_09_20 22:00 | 3232192 | 5 | 9.4498 | 17.9275 | -116.4038 | 9.9377 | 167.6408 | 0.0140 | 0.0024 |
| 2024_09_20 22:00 | 3274488 | 6 | 5.4535 | 19.5847 | -116.8950 | 17.9010 | 83.3788 | 0.0016 | 0.0040 |
| 2024_09_20 22:00 | 3237733 | 7 | 13.1185 | 11.6657 | -116.0840 | 4.9152 | 44.2188 | 0.0065 | 0.0026 |
| 2024_09_20 22:00 | 3267502 | 8 | 14.8704 | 19.3808 | -115.9245 | 3.3932 | 58.0315 | 0.0171 | 0.0193 |
| 2024_09_20 22:00 | 3253263 | 9 | 15.6349 | 10.9066 | -117.7924 | 4.4362 | 53.9244 | 0.0002 | 0.0168 |
| 2024_09_20 22:00 | 3252294 | 10 | 15.1515 | 13.2695 | -116.8784 | 3.9498 | 38.4515 | 0.0097 | 0.0185 |
| 2024_09_20 22:00 | 3224493 | 11 | 14.2053 | 11.0296 | -117.1822 | 3.4395 | 44.9951 | 0.0052 | 0.0184 |
| 2024_09_20 22:00 | 3265601 | 12 | 12.9367 | 17.9018 | -116.0629 | 3.5714 | 41.8355 | 0.0072 | 0.0124 |
| 2024_09_20 22:00 | 3274608 | 13 | 9.1034 | 13.8162 | -114.4344 | 3.0017 | 55.1621 | 0.0048 | 0.0105 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416545_66B029FE | 504990 | 370 | -97.4 | 504990 | 647 | -93.1 | 504990 | 521 | -100.9 | 504990 | 849 |
| MR_1774416545_FF992FDA | 504990 | 370 | -94.2 | 504990 | 647 | -95.3 | 504990 | 521 | -101.4 | 504990 | 849 |
| MR_1774416545_BFD870A8 | 152650 | 241 | -98.0 | 152650 | 517 | -104.8 | 152650 | 735 | -102.7 | 152650 | 51 |
| MR_1774416545_6498F21F | 152650 | 241 | -94.9 | 152650 | 517 | -104.5 | 152650 | 735 | -104.8 | 152650 | 51 |
| MR_1774416545_92B9D014 | 152650 | 241 | -98.4 | 152650 | 517 | -102.1 | 152650 | 735 | -105.1 | 152650 | 51 |
| MR_1774416545_7B6C7573 | 152650 | 241 | -97.4 | 152650 | 517 | -104.6 | 152650 | 735 | -103.6 | 152650 | 51 |
| MR_1774416545_20BBEDC0 | 504990 | 370 | -94.9 | 504990 | 647 | -92.0 | 504990 | 521 | -101.8 | 504990 | 849 |
| MR_1774416545_1C2CC03C | 504990 | 370 | -95.2 | 504990 | 647 | -91.8 | 504990 | 521 | -101.7 | 504990 | 849 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 478: `6761b803-c03...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6761b803-c039-4f32-b670-d84a66fb74c6` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[478] topology](images/train_0478.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3235258_2
- `C2`: Decrease transmission power for 3231428_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231428_4
- `C4`: Decrease transmission power for 3235258_2
- `C5`: Add neighbor relationship between 3262943_3 and 3231428_4
- `C6`: Press down the tilt angle of 3235258_2 by 7 degrees
- `C7`: Lift the tilt angle  of 3231428_4 by 8 degrees
- `C8`: Increase transmission power for 3231428_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231428_4
- `C10`: Increase A3 Offset threshold for 3235258_2
- `C11`: Decrease A3 Offset threshold for 3235258_2
- `C12`: Increase A3 Offset threshold for 3231428_4
- `C13`: Press down the tilt angle  of 3231428_4 by 8 degrees
- `C14`: Decrease A3 Offset threshold for 3231428_4
- `C15`: Check test server and transmission issues **← 정답**
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235258_2
- `C18`: Add neighbor relationship between 3235258_2 and 3231428_4
- `C19`: Lift the tilt angle of 3235258_2 by 7 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235258_2
- `C21`: Adjust the azimuth of 3231428_4 by 50 degrees
- `C22`: Adjust the azimuth of 3235258_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.916 | MS1 | 121.4656610516 | 31.1446308683 | 716 | 504990 | -87.48 | 15.83 | 507.03 | 0.17 | 2.61 | 1599 |
| 2024-09-20 22:21:32.496 | MS1 | 121.4656731433 | 31.1446199316 | 716 | 504990 | -89.04 | 14.27 | 317.23 | 0.09 | 2.24 | 1566 |
| 2024-09-20 22:21:33.704 | MS1 | 121.4656739108 | 31.1446228625 | 716 | 504990 | -88.11 | 13.42 | 458.51 | 0.07 | 2.19 | 1585 |
| 2024-09-20 22:21:34.741 | MS1 | 121.4656709156 | 31.1446294090 | 716 | 504990 | -90.61 | 15.05 | 78.19 | 0.06 | 2.35 | 305 |
| 2024-09-20 22:21:35.376 | MS1 | 121.4656613857 | 31.1446356309 | 716 | 504990 | -89.82 | 12.12 | 72.75 | 0.02 | 2.52 | 374 |
| 2024-09-20 22:21:36.964 | MS1 | 121.4656726696 | 31.1446348886 | 716 | 504990 | -89.28 | 13.73 | 81.01 | 0.06 | 2.91 | 313 |
| 2024-09-20 22:21:37.728 | MS1 | 121.4656720714 | 31.1446182535 | 716 | 504990 | -89.83 | 10.14 | 65.30 | 0.16 | 2.99 | 477 |
| 2024-09-20 22:21:38.338 | MS1 | 121.4656717185 | 31.1446320908 | 716 | 504990 | -93.26 | 8.81 | 48.35 | 0.10 | 2.20 | 490 |
| 2024-09-20 22:21:39.892 | MS1 | 121.4656702345 | 31.1446277175 | 716 | 504990 | -90.70 | 11.30 | 79.57 | 0.07 | 2.42 | 362 |
| 2024-09-20 22:21:40.799 | MS1 | 121.4656741212 | 31.1446278509 | 716 | 504990 | -89.79 | 8.13 | 334.68 | 0.11 | 2.80 | 1600 |
| 2024-09-20 22:21:41.102 | MS1 | 121.4656752277 | 31.1446274254 | 716 | 504990 | -90.65 | 10.47 | 313.56 | 0.14 | 2.87 | 1582 |
| 2024-09-20 22:21:42.407 | MS1 | 121.4656741264 | 31.1446240068 | 716 | 504990 | -92.80 | 11.89 | 322.59 | 0.06 | 2.57 | 1582 |

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
| 3231428 | 4 | 121.4687230469 | 31.1487846274 | 1 | 4 | 6 | 38.4 | TDD | 933 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3235258 | 2 | 121.4709113738 | 31.1558087602 | 359 | 5 | 4 | 37.3 | TDD | 716 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3256352 | 1 | 121.4663560665 | 31.1489853932 | 199 | 15 | 0 | 32.3 | TDD | 877 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3262943 | 3 | 121.4754865602 | 31.1493577819 | 3 | 3 | 11 | 26.2 | TDD | 869 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.239 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.363 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.363 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.056 | NREventA3 | measId:2;ServCellPCI:485;Se... |
| 2024-09-20 22:21:38.296 | NRHandoverAttempt | SourcePCI:485;SourceNR-ARFC... |
| 2024-09-20 22:21:38.333 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.344 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.473 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.473 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256352 | 1 | 18.1039 | 5.1230 | -117.7593 | 6.7494 | 95.9556 | 0.0132 | 0.0122 |
| 2024_09_20 22:00 | 3235258 | 2 | 6.9526 | 11.0851 | -117.5215 | 9.3746 | 137.2302 | 0.0164 | 0.0008 |
| 2024_09_20 22:00 | 3262943 | 3 | 5.8141 | 12.9290 | -115.0817 | 6.2250 | 158.9573 | 0.0023 | 0.0058 |
| 2024_09_20 22:00 | 3231428 | 4 | 8.1730 | 15.7539 | -117.0100 | 15.9093 | 175.8017 | 0.0062 | 0.0112 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412522_A2B82A32 | 504990 | 716 | -91.3 | 504990 | 933 | -101.3 | 504990 | 869 | -101.8 | 504990 | 877 |
| MR_1774412522_1A5BEB1E | 504990 | 716 | -90.0 | 504990 | 933 | -99.6 | 504990 | 869 | -100.0 | 504990 | 877 |
| MR_1774412522_3B1374DF | 504990 | 716 | -88.9 | 504990 | 933 | -100.7 | 504990 | 869 | -98.8 | 504990 | 877 |
| MR_1774412522_A99C32A3 | 504990 | 716 | -92.6 | 504990 | 933 | -98.4 | 504990 | 869 | -101.0 | 504990 | 877 |
| MR_1774412522_A16EB37A | 504990 | 716 | -88.8 | 504990 | 933 | -97.7 | 504990 | 869 | -100.6 | 504990 | 877 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 479: `8df726bc-e0a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8df726bc-e0ac-4ed9-864b-6c58c89dbcac` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3260676_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[479] topology](images/train_0479.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3255821_4 by 7 degrees
- `C2`: Decrease A3 Offset threshold for 3255821_4
- `C3`: Add neighbor relationship between 3260676_2 and 3255821_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260676_2
- `C5`: Increase A3 Offset threshold for 3255821_4
- `C6`: Decrease transmission power for 3260676_2
- `C7`: Adjust the azimuth of 3260676_2 by 34 degrees
- `C8`: Add neighbor relationship between 3271284_1 and 3255821_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255821_4
- `C10`: Increase transmission power for 3260676_2
- `C11`: Press down the tilt angle  of 3255821_4 by 7 degrees
- `C12`: Press down the tilt angle of 3260676_2 by 2 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease transmission power for 3255821_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255821_4
- `C16`: Decrease A3 Offset threshold for 3260676_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260676_2 **← 정답**
- `C18`: Increase transmission power for 3255821_4
- `C19`: Adjust the azimuth of 3255821_4 by 50 degrees
- `C20`: Check test server and transmission issues
- `C21`: Lift the tilt angle of 3260676_2 by 2 degrees
- `C22`: Increase A3 Offset threshold for 3260676_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.363 | MS1 | 121.4656772469 | 31.1446183160 | 715 | 504990 | -87.78 | 12.71 | 306.49 | 0.01 | 2.45 | 1573 |
| 2024-09-20 22:21:32.628 | MS1 | 121.4656592825 | 31.1446240972 | 715 | 504990 | -87.12 | 12.98 | 333.61 | 0.11 | 2.70 | 1565 |
| 2024-09-20 22:21:33.178 | MS1 | 121.4656625748 | 31.1446191788 | 715 | 504990 | -90.35 | 13.36 | 589.95 | 0.00 | 2.53 | 1571 |
| 2024-09-20 22:21:34.419 | MS1 | 121.4656592748 | 31.1446299773 | 715 | 504990 | -89.80 | 17.55 | 54.97 | 0.57 | 2.64 | 540 |
| 2024-09-20 22:21:35.359 | MS1 | 121.4656716469 | 31.1446218701 | 715 | 504990 | -85.44 | 13.82 | 59.16 | 0.68 | 2.78 | 573 |
| 2024-09-20 22:21:36.545 | MS1 | 121.4656692187 | 31.1446376121 | 715 | 504990 | -91.96 | 12.34 | 88.39 | 0.61 | 2.46 | 650 |
| 2024-09-20 22:21:37.787 | MS1 | 121.4656652383 | 31.1446358340 | 715 | 504990 | -92.72 | 11.90 | 77.13 | 0.64 | 2.28 | 539 |
| 2024-09-20 22:21:38.808 | MS1 | 121.4656647957 | 31.1446304504 | 715 | 504990 | -89.44 | 7.28 | 90.92 | 0.70 | 2.33 | 516 |
| 2024-09-20 22:21:39.476 | MS1 | 121.4656716466 | 31.1446191949 | 715 | 504990 | -89.59 | 12.98 | 58.05 | 0.51 | 2.20 | 623 |
| 2024-09-20 22:21:40.430 | MS1 | 121.4656769503 | 31.1446239229 | 715 | 504990 | -90.94 | 10.76 | 388.98 | 0.13 | 2.44 | 1595 |
| 2024-09-20 22:21:41.496 | MS1 | 121.4656778679 | 31.1446298094 | 715 | 504990 | -89.27 | 8.32 | 446.70 | 0.02 | 2.30 | 1564 |
| 2024-09-20 22:21:42.560 | MS1 | 121.4656636085 | 31.1446367943 | 715 | 504990 | -90.95 | 11.54 | 325.88 | 0.01 | 2.19 | 1586 |

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
| 3225188 | 3 | 121.4676990751 | 31.1513458060 | 358 | 2 | 2 | 41.3 | TDD | 716 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3255821 | 4 | 121.4640239772 | 31.1456111661 | 257 | 0 | 6 | 24.0 | TDD | 23 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3260676 | 2 | 121.4666488040 | 31.1538010082 | 151 | 0 | 1 | 35.4 | TDD | 715 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3271284 | 1 | 121.4657805415 | 31.1504671123 | 235 | 8 | 3 | 24.1 | TDD | 226 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.020 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.159 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.159 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.806 | NREventA3 | measId:2;ServCellPCI:209;Se... |
| 2024-09-20 22:21:38.046 | NRHandoverAttempt | SourcePCI:209;SourceNR-ARFC... |
| 2024-09-20 22:21:38.096 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.106 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.252 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.252 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271284 | 1 | 17.5546 | 19.6962 | -117.0756 | 17.5952 | 136.1466 | 0.0162 | 0.0170 |
| 2024_09_20 22:00 | 3260676 | 2 | 17.0570 | 17.8691 | -117.7880 | 9.3354 | 163.3324 | 0.0148 | 0.0166 |
| 2024_09_20 22:00 | 3225188 | 3 | 14.4634 | 11.2363 | -116.0717 | 8.3767 | 176.3614 | 0.0134 | 0.0036 |
| 2024_09_20 22:00 | 3255821 | 4 | 10.3994 | 14.3530 | -117.3036 | 8.2378 | 182.6058 | 0.0137 | 0.0172 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412527_429DA265 | 504990 | 715 | -89.1 | 504990 | 23 | -90.4 | 504990 | 226 | -101.2 | 504990 | 716 |
| MR_1774412527_1EEDD53C | 504990 | 715 | -88.4 | 504990 | 23 | -94.1 | 504990 | 226 | -104.2 | 504990 | 716 |
| MR_1774412527_BEF1655D | 504990 | 715 | -91.7 | 504990 | 23 | -92.5 | 504990 | 226 | -102.4 | 504990 | 716 |
| MR_1774412527_2647A07E | 504990 | 715 | -88.5 | 504990 | 23 | -92.2 | 504990 | 226 | -104.4 | 504990 | 716 |
| MR_1774412527_7FA0B94E | 504990 | 715 | -89.6 | 504990 | 23 | -90.8 | 504990 | 226 | -104.5 | 504990 | 716 |
| MR_1774412527_2F57BB13 | 504990 | 715 | -90.1 | 504990 | 23 | -92.2 | 504990 | 226 | -101.4 | 504990 | 716 |

> *... 2개 열 생략 (전체 14열)*

---
