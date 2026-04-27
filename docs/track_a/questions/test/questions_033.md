# Track A 문제 분석 — test[320]~test[329]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[320] ~ test[329] (10개)

## 목차

1. [문제 320: `7425ee8c-472...`](#320) — single-answer
2. [문제 321: `75d95403-52d...`](#321) — single-answer
3. [문제 322: `afe69cae-79a...`](#322) — multiple-answer
4. [문제 323: `074ac8e7-4c0...`](#323) — single-answer
5. [문제 324: `e7fec92b-76d...`](#324) — single-answer
6. [문제 325: `7bf49ea7-fcf...`](#325) — single-answer
7. [문제 326: `34666e73-9ac...`](#326) — multiple-answer
8. [문제 327: `8a97cbab-5a7...`](#327) — multiple-answer
9. [문제 328: `006d5394-3de...`](#328) — single-answer
10. [문제 329: `bb5989fd-694...`](#329) — single-answer

---

### 문제 320: `7425ee8c-472...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7425ee8c-4722-4b12-8c75-73462dee3ee5` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[320] topology](images/test_0320.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3261540_1 by 6 degrees
- `C2`: Increase transmission power for 3234908_2
- `C3`: Adjust the azimuth of 3234908_2 by 7 degrees
- `C4`: Decrease transmission power for 3261540_1
- `C5`: Decrease A3 Offset threshold for 3261540_1
- `C6`: Add neighbor relationship between 3279121_13 and 3261540_1
- `C7`: Press down the tilt angle of 3234908_2 by 3 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261540_1
- `C9`: Decrease A3 Offset threshold for 3234908_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261540_1
- `C11`: Increase A3 Offset threshold for 3261540_1
- `C12`: Decrease transmission power for 3234908_2
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234908_2
- `C15`: Increase transmission power for 3261540_1
- `C16`: Press down the tilt angle  of 3261540_1 by 6 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234908_2
- `C18`: Increase A3 Offset threshold for 3234908_2
- `C19`: Adjust the azimuth of 3261540_1 by 38 degrees
- `C20`: Check test server and transmission issues
- `C21`: Add neighbor relationship between 3234908_2 and 3261540_1
- `C22`: Lift the tilt angle of 3234908_2 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.950 | MS1 | 121.4656721811 | 31.1446195037 | 962 | 504990 | -93.22 | 12.70 | 433.49 | 0.01 | 2.63 | 1577 |
| 2024-09-20 22:21:32.239 | MS1 | 121.4656660019 | 31.1446357558 | 319 | 504990 | -93.01 | 13.59 | 579.16 | 0.07 | 2.34 | 1566 |
| 2024-09-20 22:21:33.777 | MS1 | 121.4656716787 | 31.1446372897 | 285 | 504990 | -94.11 | 11.90 | 357.88 | 0.03 | 2.42 | 1563 |
| 2024-09-20 22:21:34.701 | MS1 | 121.4656765511 | 31.1446339138 | 138 | 152650 | -94.85 | 3.29 | 81.88 | 0.15 | 1.94 | 964 |
| 2024-09-20 22:21:35.218 | MS1 | 121.4656776826 | 31.1446330897 | 302 | 152650 | -91.70 | 4.81 | 95.45 | 0.12 | 1.68 | 948 |
| 2024-09-20 22:21:36.523 | MS1 | 121.4656613179 | 31.1446368649 | 927 | 152650 | -96.15 | 5.03 | 61.60 | 0.07 | 1.91 | 987 |
| 2024-09-20 22:21:37.840 | MS1 | 121.4656665343 | 31.1446360487 | 964 | 152650 | -89.94 | 5.74 | 53.94 | 0.16 | 1.75 | 984 |
| 2024-09-20 22:21:38.243 | MS1 | 121.4656679767 | 31.1446224851 | 138 | 152650 | -88.61 | 6.82 | 69.12 | 0.14 | 1.63 | 905 |
| 2024-09-20 22:21:39.623 | MS1 | 121.4656702915 | 31.1446261596 | 302 | 152650 | -89.79 | 4.49 | 88.28 | 0.17 | 1.65 | 989 |
| 2024-09-20 22:21:40.617 | MS1 | 121.4656663770 | 31.1446245341 | 927 | 152650 | -92.28 | 4.77 | 92.23 | 0.13 | 2.39 | 1580 |
| 2024-09-20 22:21:41.695 | MS1 | 121.4656759874 | 31.1446351845 | 964 | 152650 | -93.32 | 2.01 | 61.43 | 0.03 | 2.52 | 1583 |
| 2024-09-20 22:21:42.390 | MS1 | 121.4656698880 | 31.1446317773 | 138 | 152650 | -91.57 | 7.90 | 76.22 | 0.02 | 2.44 | 1571 |

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
| 3210504 | 10 | 121.4683933887 | 31.1441715439 | 246 | 15 | 9 | 23.9 | FDD | 302 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3221743 | 3 | 121.4693166229 | 31.1455137124 | 280 | 1 | 2 | 25.8 | TDD | 451 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3229547 | 4 | 121.4743742663 | 31.1476282594 | 32 | 15 | 7 | 7.6 | TDD | 900 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3232816 | 5 | 121.4750710095 | 31.1489706908 | 21 | 12 | 2 | 29.9 | TDD | 285 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3234133 | 7 | 121.4658996559 | 31.1485801375 | 173 | 5 | 10 | 5.1 | FDD | 964 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3234908 | 2 | 121.4685432119 | 31.1555909844 | 186 | 3 | 0 | 9.4 | TDD | 962 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3251488 | 9 | 121.4697119762 | 31.1475913287 | 21 | 12 | 12 | 17.3 | FDD | 138 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3253338 | 11 | 121.4729270774 | 31.1550699997 | 160 | 5 | 2 | 21.9 | FDD | 782 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3261540 | 1 | 121.4719419003 | 31.1453899802 | 300 | 4 | 7 | 18.8 | TDD | 128 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3268960 | 6 | 121.4708199965 | 31.1508092982 | 78 | 3 | 9 | 25.7 | TDD | 319 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3270146 | 8 | 121.4694692711 | 31.1516675463 | 39 | 12 | 2 | 27.2 | FDD | 965 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3270487 | 12 | 121.4748185029 | 31.1498264990 | 74 | 2 | 12 | 18.0 | FDD | 21 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3279121 | 13 | 121.4706374559 | 31.1537882856 | 325 | 7 | 11 | 4.5 | FDD | 927 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |

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
| 2024-09-20 22:21:31.093 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.117 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.265 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.265 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.920 | NREventA2 | measId:1;ServCellPCI:640;Se... |
| 2024-09-20 22:21:35.020 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.270 | NREventA5 | measId:3;ServCellPCI:640;Se... |
| 2024-09-20 22:21:35.309 | NRHandoverAttempt | SourcePCI:640;SourceNR-ARFC... |
| 2024-09-20 22:21:35.353 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.367 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.501 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.501 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261540 | 1 | 8.0449 | 12.6235 | -116.9274 | 8.0176 | 196.8094 | 0.0171 | 0.0045 |
| 2024_09_20 22:00 | 3234908 | 2 | 13.4520 | 8.1141 | -116.9188 | 8.8787 | 180.4962 | 0.0192 | 0.0100 |
| 2024_09_20 22:00 | 3221743 | 3 | 15.7646 | 16.8009 | -117.9356 | 10.7224 | 164.3860 | 0.0195 | 0.0159 |
| 2024_09_20 22:00 | 3229547 | 4 | 13.8767 | 19.2480 | -114.2257 | 12.4140 | 104.9803 | 0.0052 | 0.0000 |
| 2024_09_20 22:00 | 3232816 | 5 | 12.4214 | 10.5937 | -114.0604 | 15.6382 | 127.4490 | 0.0072 | 0.0183 |
| 2024_09_20 22:00 | 3268960 | 6 | 18.6459 | 5.9142 | -116.9926 | 19.1495 | 129.9195 | 0.0128 | 0.0187 |
| 2024_09_20 22:00 | 3234133 | 7 | 12.5157 | 9.7184 | -115.2758 | 4.1475 | 23.8576 | 0.0140 | 0.0055 |
| 2024_09_20 22:00 | 3270146 | 8 | 14.7840 | 7.5638 | -114.9758 | 3.7950 | 48.2098 | 0.0034 | 0.0058 |
| 2024_09_20 22:00 | 3251488 | 9 | 13.9247 | 8.4258 | -114.7941 | 3.9424 | 20.4706 | 0.0033 | 0.0101 |
| 2024_09_20 22:00 | 3210504 | 10 | 13.2831 | 18.0140 | -116.4259 | 4.7718 | 54.5986 | 0.0173 | 0.0176 |
| 2024_09_20 22:00 | 3253338 | 11 | 18.6144 | 8.0845 | -114.7246 | 3.7857 | 30.6235 | 0.0149 | 0.0081 |
| 2024_09_20 22:00 | 3270487 | 12 | 16.2545 | 14.2437 | -115.5661 | 3.3091 | 51.9548 | 0.0111 | 0.0075 |
| 2024_09_20 22:00 | 3279121 | 13 | 5.6410 | 8.8167 | -116.0577 | 4.6788 | 42.6039 | 0.0024 | 0.0135 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412921_77F88E59 | 504990 | 285 | -92.3 | 504990 | 128 | -92.8 | 504990 | 900 | -97.7 | 504990 | 451 |
| MR_1774412921_AEB0395F | 152650 | 138 | -94.8 | 152650 | 965 | -101.3 | 152650 | 21 | -106.9 | 152650 | 782 |
| MR_1774412921_EC765D85 | 504990 | 285 | -92.7 | 504990 | 128 | -96.2 | 504990 | 900 | -96.8 | 504990 | 451 |
| MR_1774412921_F8244A8F | 504990 | 285 | -93.1 | 504990 | 128 | -95.2 | 504990 | 900 | -95.4 | 504990 | 451 |
| MR_1774412921_02032CCB | 152650 | 138 | -94.9 | 152650 | 965 | -101.8 | 152650 | 21 | -107.2 | 152650 | 782 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 321: `75d95403-52d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `75d95403-52d8-46a0-b1bb-6e5f6f25dc5b` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[321] topology](images/test_0321.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Lift the tilt angle of 3246824_3 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246824_3
- `C4`: Add neighbor relationship between 3246824_3 and 3218795_2
- `C5`: Press down the tilt angle  of 3218795_2 by 10 degrees
- `C6`: Decrease transmission power for 3246824_3
- `C7`: Press down the tilt angle of 3246824_3 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3246824_3
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Increase A3 Offset threshold for 3246824_3
- `C11`: Decrease A3 Offset threshold for 3218795_2
- `C12`: Decrease transmission power for 3218795_2
- `C13`: Increase A3 Offset threshold for 3218795_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218795_2
- `C15`: Increase transmission power for 3246824_3
- `C16`: Adjust the azimuth of 3246824_3 by 45 degrees
- `C17`: Adjust the azimuth of 3218795_2 by 21 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218795_2
- `C19`: Increase transmission power for 3218795_2
- `C20`: Add neighbor relationship between 3264924_1 and 3218795_2
- `C21`: Lift the tilt angle  of 3218795_2 by 10 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246824_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.955 | MS1 | 121.4656721658 | 31.1446356016 | 786 | 504990 | -90.03 | 17.91 | 565.55 | 0.17 | 2.71 | 1568 |
| 2024-09-20 22:21:32.721 | MS1 | 121.4656700560 | 31.1446260654 | 786 | 504990 | -87.92 | 13.36 | 597.18 | 0.04 | 2.29 | 1586 |
| 2024-09-20 22:21:33.532 | MS1 | 121.4656670803 | 31.1446308480 | 786 | 504990 | -85.37 | 12.90 | 385.65 | 0.07 | 2.90 | 1561 |
| 2024-09-20 22:21:34.187 | MS1 | 121.4656711805 | 31.1446344807 | 786 | 504990 | -90.76 | 17.61 | 63.56 | 0.06 | 2.37 | 470 |
| 2024-09-20 22:21:35.439 | MS1 | 121.4656746676 | 31.1446299997 | 786 | 504990 | -85.30 | 13.76 | 64.24 | 0.04 | 2.92 | 323 |
| 2024-09-20 22:21:36.920 | MS1 | 121.4656704421 | 31.1446325650 | 786 | 504990 | -90.28 | 17.08 | 72.36 | 0.11 | 2.81 | 449 |
| 2024-09-20 22:21:37.217 | MS1 | 121.4656748350 | 31.1446341833 | 786 | 504990 | -90.52 | 9.57 | 74.16 | 0.19 | 2.73 | 410 |
| 2024-09-20 22:21:38.939 | MS1 | 121.4656613265 | 31.1446330939 | 786 | 504990 | -91.59 | 10.38 | 98.03 | 0.11 | 2.19 | 457 |
| 2024-09-20 22:21:39.145 | MS1 | 121.4656592823 | 31.1446198411 | 786 | 504990 | -89.17 | 11.56 | 89.45 | 0.03 | 2.18 | 388 |
| 2024-09-20 22:21:40.346 | MS1 | 121.4656699245 | 31.1446194617 | 786 | 504990 | -91.66 | 9.00 | 593.81 | 0.02 | 2.53 | 1570 |
| 2024-09-20 22:21:41.563 | MS1 | 121.4656596849 | 31.1446189856 | 786 | 504990 | -93.34 | 10.26 | 430.04 | 0.01 | 2.27 | 1562 |
| 2024-09-20 22:21:42.283 | MS1 | 121.4656767860 | 31.1446374017 | 786 | 504990 | -93.65 | 8.24 | 362.46 | 0.09 | 2.39 | 1575 |

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
| 3218795 | 2 | 121.4681780536 | 31.1459504263 | 217 | 14 | 10 | 19.1 | TDD | 986 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3219661 | 4 | 121.4748252926 | 31.1454792412 | 244 | 2 | 0 | 43.1 | TDD | 104 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3246824 | 3 | 121.4651811322 | 31.1486409556 | 129 | 15 | 11 | 16.4 | TDD | 786 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3264924 | 1 | 121.4679786626 | 31.1517930871 | 63 | 1 | 3 | 25.0 | TDD | 728 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.211 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.235 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.361 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.361 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.017 | NREventA3 | measId:2;ServCellPCI:656;Se... |
| 2024-09-20 22:21:38.257 | NRHandoverAttempt | SourcePCI:656;SourceNR-ARFC... |
| 2024-09-20 22:21:38.292 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.307 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.409 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.409 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264924 | 1 | 13.6846 | 8.9619 | -114.0915 | 7.5211 | 184.3233 | 0.0068 | 0.0190 |
| 2024_09_20 22:00 | 3218795 | 2 | 15.6289 | 17.7698 | -115.5545 | 12.7397 | 170.9570 | 0.0004 | 0.0126 |
| 2024_09_20 22:00 | 3246824 | 3 | 10.9489 | 14.2305 | -115.7562 | 11.2661 | 134.9088 | 0.0121 | 0.0013 |
| 2024_09_20 22:00 | 3219661 | 4 | 15.5978 | 7.5697 | -117.4831 | 16.4972 | 97.9337 | 0.0032 | 0.0096 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414732_2F713BC4 | 504990 | 786 | -92.6 | 504990 | 986 | -91.5 | 504990 | 728 | -104.8 | 504990 | 104 |
| MR_1774414732_F98EEA13 | 504990 | 786 | -91.8 | 504990 | 986 | -89.9 | 504990 | 728 | -107.4 | 504990 | 104 |
| MR_1774414732_71787C4D | 504990 | 786 | -89.7 | 504990 | 986 | -91.3 | 504990 | 728 | -104.0 | 504990 | 104 |
| MR_1774414732_94BF732E | 504990 | 786 | -89.8 | 504990 | 986 | -92.6 | 504990 | 728 | -106.9 | 504990 | 104 |
| MR_1774414732_7BD0D265 | 504990 | 786 | -91.6 | 504990 | 986 | -88.9 | 504990 | 728 | -106.8 | 504990 | 104 |
| MR_1774414732_8A1CC026 | 504990 | 786 | -90.4 | 504990 | 986 | -89.7 | 504990 | 728 | -105.2 | 504990 | 104 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 322: `afe69cae-79a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `afe69cae-79a4-4ed4-b54c-b2d5ab62a2c9` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[322] topology](images/test_0322.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3258809_1 by 25 degrees
- `C2`: Increase transmission power for 3258809_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Lift the tilt angle of 3258809_1 by 10 degrees
- `C5`: Decrease transmission power for 3249671_2
- `C6`: Add neighbor relationship between 3255106_3 and 3249671_2
- `C7`: Increase transmission power for 3249671_2
- `C8`: Press down the tilt angle of 3258809_1 by 10 degrees
- `C9`: Adjust the azimuth of 3249671_2 by 6 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258809_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258809_1
- `C12`: Add neighbor relationship between 3258809_1 and 3249671_2
- `C13`: Lift the tilt angle  of 3249671_2 by 1 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249671_2
- `C15`: Press down the tilt angle  of 3249671_2 by 1 degrees
- `C16`: Increase A3 Offset threshold for 3249671_2
- `C17`: Decrease transmission power for 3258809_1
- `C18`: Check test server and transmission issues
- `C19`: Increase A3 Offset threshold for 3258809_1
- `C20`: Decrease A3 Offset threshold for 3249671_2
- `C21`: Decrease A3 Offset threshold for 3258809_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249671_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.870 | MS1 | 121.4656637818 | 31.1446213664 | 962 | 504990 | -90.22 | 15.79 | 304.75 | 0.04 | 2.84 | 1582 |
| 2024-09-20 22:21:32.461 | MS1 | 121.4656701691 | 31.1446343479 | 962 | 504990 | -94.76 | 16.80 | 443.82 | 0.01 | 2.93 | 1592 |
| 2024-09-20 22:21:33.302 | MS1 | 121.4656745775 | 31.1446290031 | 962 | 504990 | -89.63 | 15.20 | 510.71 | 0.07 | 2.77 | 1565 |
| 2024-09-20 22:21:34.470 | MS1 | 121.4656732462 | 31.1446372114 | 962 | 504990 | -108.61 | 0.61 | 76.96 | 0.06 | 1.48 | 1588 |
| 2024-09-20 22:21:35.176 | MS1 | 121.4656589558 | 31.1446289773 | 962 | 504990 | -101.03 | 0.57 | 18.02 | 0.15 | 1.23 | 1596 |
| 2024-09-20 22:21:36.102 | MS1 | 121.4656689800 | 31.1446268477 | 962 | 504990 | -108.01 | -1.26 | 43.73 | 0.18 | 1.28 | 1568 |
| 2024-09-20 22:21:37.459 | MS1 | 121.4656706783 | 31.1446256265 | 962 | 504990 | -102.09 | 0.83 | 14.75 | 0.11 | 1.30 | 1583 |
| 2024-09-20 22:21:38.533 | MS1 | 121.4656628200 | 31.1446318283 | 962 | 504990 | -101.35 | 0.76 | 55.18 | 0.06 | 1.15 | 1582 |
| 2024-09-20 22:21:39.578 | MS1 | 121.4656622028 | 31.1446288648 | 962 | 504990 | -108.30 | 1.35 | 56.13 | 0.18 | 1.20 | 1574 |
| 2024-09-20 22:21:40.744 | MS1 | 121.4656596485 | 31.1446323060 | 962 | 504990 | -86.37 | 17.36 | 559.24 | 0.13 | 2.99 | 1576 |
| 2024-09-20 22:21:41.957 | MS1 | 121.4656583949 | 31.1446223820 | 962 | 504990 | -87.31 | 13.61 | 593.54 | 0.09 | 2.44 | 1581 |
| 2024-09-20 22:21:42.903 | MS1 | 121.4656726837 | 31.1446325410 | 962 | 504990 | -94.06 | 17.92 | 498.02 | 0.19 | 2.94 | 1585 |

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
| 3249671 | 2 | 121.4711291159 | 31.1546462154 | 211 | 0 | 4 | 28.7 | TDD | 386 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3252341 | 4 | 121.4732327758 | 31.1492939722 | 189 | 6 | 12 | 21.7 | TDD | 327 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3255106 | 3 | 121.4680815816 | 31.1504605999 | 240 | 9 | 2 | 18.6 | TDD | 310 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3258809 | 1 | 121.4731345049 | 31.1442109136 | 299 | 11 | 10 | 41.6 | TDD | 962 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.394 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.411 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.523 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.523 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.774 | NREventA2 | measId:1;ServCellPCI:45;Ser... |
| 2024-09-20 22:21:34.906 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258809 | 1 | 19.2699 | 6.5648 | -114.1776 | 14.0617 | 152.6461 | 0.1132 | 0.0132 |
| 2024_09_20 22:00 | 3249671 | 2 | 9.3659 | 17.9981 | -116.3160 | 6.0609 | 98.7315 | 0.0076 | 0.0185 |
| 2024_09_20 22:00 | 3255106 | 3 | 12.9654 | 15.1922 | -117.3978 | 8.3432 | 102.0531 | 0.0111 | 0.0029 |
| 2024_09_20 22:00 | 3252341 | 4 | 11.9159 | 12.6493 | -115.7122 | 12.1605 | 82.0957 | 0.0065 | 0.0129 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416509_F096829D | 504990 | 962 | -106.9 | 504990 | 386 | -114.4 | 504990 | 310 | -119.3 | 504990 | 327 |
| MR_1774416509_8C787886 | 504990 | 962 | -110.5 | 504990 | 386 | -111.4 | 504990 | 310 | -119.7 | 504990 | 327 |
| MR_1774416509_4C79414C | 504990 | 962 | -107.3 | 504990 | 386 | -113.2 | 504990 | 310 | -121.0 | 504990 | 327 |
| MR_1774416509_CA8F976F | 504990 | 962 | -108.0 | 504990 | 386 | -114.5 | 504990 | 310 | -118.8 | 504990 | 327 |
| MR_1774416509_6D8DAE41 | 504990 | 962 | -107.0 | 504990 | 386 | -113.1 | 504990 | 310 | -121.2 | 504990 | 327 |
| MR_1774416509_2C92B1AA | 504990 | 962 | -108.0 | 504990 | 386 | -114.6 | 504990 | 310 | -121.3 | 504990 | 327 |
| MR_1774416509_0546F15C | 504990 | 962 | -110.4 | 504990 | 386 | -113.4 | 504990 | 310 | -120.2 | 504990 | 327 |
| MR_1774416509_FA9090CE | 504990 | 962 | -106.6 | 504990 | 386 | -111.7 | 504990 | 310 | -119.4 | 504990 | 327 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 323: `074ac8e7-4c0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `074ac8e7-4c04-4046-9145-3a1de23d2dcc` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[323] topology](images/test_0323.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3272326_2 by 5 degrees
- `C2`: Decrease transmission power for 3275888_1
- `C3`: Add neighbor relationship between 3257720_3 and 3275888_1
- `C4`: Increase transmission power for 3272326_2
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease A3 Offset threshold for 3272326_2
- `C7`: Check test server and transmission issues
- `C8`: Press down the tilt angle  of 3275888_1 by 10 degrees
- `C9`: Adjust the azimuth of 3272326_2 by 50 degrees
- `C10`: Lift the tilt angle  of 3275888_1 by 10 degrees
- `C11`: Increase transmission power for 3275888_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272326_2
- `C13`: Add neighbor relationship between 3272326_2 and 3275888_1
- `C14`: Decrease A3 Offset threshold for 3275888_1
- `C15`: Increase A3 Offset threshold for 3272326_2
- `C16`: Increase A3 Offset threshold for 3275888_1
- `C17`: Adjust the azimuth of 3275888_1 by 50 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272326_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275888_1
- `C20`: Press down the tilt angle of 3272326_2 by 5 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275888_1
- `C22`: Decrease transmission power for 3272326_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.766 | MS1 | 121.4656727549 | 31.1446376974 | 874 | 504990 | -90.67 | 12.96 | 477.19 | 0.18 | 2.01 | 1578 |
| 2024-09-20 22:21:32.325 | MS1 | 121.4656601329 | 31.1446324471 | 874 | 504990 | -91.35 | 12.78 | 417.97 | 0.11 | 2.10 | 1578 |
| 2024-09-20 22:21:33.570 | MS1 | 121.4656750016 | 31.1446188787 | 874 | 504990 | -87.05 | 12.66 | 359.53 | 0.11 | 2.13 | 1565 |
| 2024-09-20 22:21:34.610 | MS1 | 121.4656673151 | 31.1446180195 | 874 | 504990 | -91.52 | 14.71 | 88.93 | 0.03 | 2.69 | 1578 |
| 2024-09-20 22:21:35.252 | MS1 | 121.4656721573 | 31.1446214367 | 874 | 504990 | -88.52 | 17.31 | 95.22 | 0.02 | 2.47 | 1560 |
| 2024-09-20 22:21:36.275 | MS1 | 121.4656580579 | 31.1446341523 | 874 | 504990 | -89.37 | 15.67 | 85.52 | 0.04 | 2.87 | 1563 |
| 2024-09-20 22:21:37.810 | MS1 | 121.4656741832 | 31.1446272199 | 874 | 504990 | -89.53 | 12.39 | 73.23 | 0.11 | 2.61 | 1571 |
| 2024-09-20 22:21:38.335 | MS1 | 121.4656686256 | 31.1446317788 | 874 | 504990 | -89.17 | 8.81 | 90.07 | 0.04 | 2.68 | 1581 |
| 2024-09-20 22:21:39.549 | MS1 | 121.4656778250 | 31.1446194210 | 874 | 504990 | -92.58 | 10.79 | 65.65 | 0.02 | 2.51 | 1571 |
| 2024-09-20 22:21:40.789 | MS1 | 121.4656724093 | 31.1446341496 | 874 | 504990 | -91.21 | 10.95 | 537.91 | 0.17 | 2.22 | 1598 |
| 2024-09-20 22:21:41.439 | MS1 | 121.4656635584 | 31.1446289536 | 874 | 504990 | -92.34 | 12.96 | 434.97 | 0.12 | 2.71 | 1562 |
| 2024-09-20 22:21:42.370 | MS1 | 121.4656761095 | 31.1446309848 | 874 | 504990 | -89.52 | 7.10 | 506.20 | 0.10 | 2.22 | 1561 |

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
| 3211402 | 4 | 121.4755194676 | 31.1463171267 | 137 | 9 | 10 | 45.6 | TDD | 876 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3257720 | 3 | 121.4734766067 | 31.1535765651 | 8 | 9 | 5 | 45.9 | TDD | 657 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3272326 | 2 | 121.4731493116 | 31.1484968872 | 121 | 2 | 6 | 38.5 | TDD | 874 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3275888 | 1 | 121.4709129801 | 31.1489589966 | 307 | 14 | 12 | 31.6 | TDD | 969 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.396 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.416 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.557 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.557 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.220 | NREventA3 | measId:2;ServCellPCI:538;Se... |
| 2024-09-20 22:21:38.460 | NRHandoverAttempt | SourcePCI:538;SourceNR-ARFC... |
| 2024-09-20 22:21:38.500 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.513 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.648 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.648 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3275888 | 1 | 78.4919 | 83.6493 | -114.7490 | 8.2916 | 138.3013 | 0.0003 | 0.0173 |
| 2024_09_19 22:00 | 3272326 | 2 | 91.6070 | 83.1876 | -117.1715 | 7.0988 | 113.7775 | 0.0159 | 0.0079 |
| 2024_09_19 22:00 | 3257720 | 3 | 94.3878 | 84.0194 | -114.1386 | 10.6676 | 142.2914 | 0.0174 | 0.0189 |
| 2024_09_19 22:00 | 3211402 | 4 | 76.6124 | 92.2237 | -115.0804 | 17.2853 | 138.8271 | 0.0013 | 0.0045 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416235_A0BA911D | 504990 | 874 | -89.6 | 504990 | 969 | -95.9 | 504990 | 657 | -98.3 | 504990 | 876 |
| MR_1774416235_DDA73DBF | 504990 | 874 | -89.7 | 504990 | 969 | -94.0 | 504990 | 657 | -99.7 | 504990 | 876 |
| MR_1774416235_CFF4FD78 | 504990 | 874 | -90.1 | 504990 | 969 | -96.0 | 504990 | 657 | -98.7 | 504990 | 876 |
| MR_1774416235_139EDCCD | 504990 | 874 | -93.5 | 504990 | 969 | -96.5 | 504990 | 657 | -97.2 | 504990 | 876 |
| MR_1774416235_C566C262 | 504990 | 874 | -93.5 | 504990 | 969 | -97.1 | 504990 | 657 | -97.1 | 504990 | 876 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 324: `e7fec92b-76d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e7fec92b-76d2-4733-98d7-fd2a7616d1f0` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[324] topology](images/test_0324.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3247739_2 by 6 degrees
- `C2`: Adjust the azimuth of 3271205_1 by 2 degrees
- `C3`: Increase A3 Offset threshold for 3217062_4
- `C4`: Press down the tilt angle  of 3247739_2 by 6 degrees
- `C5`: Decrease transmission power for 3271205_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217062_4
- `C7`: Press down the tilt angle of 3271205_1 by 3 degrees
- `C8`: Increase transmission power for 3217062_4
- `C9`: Lift the tilt angle of 3271205_1 by 3 degrees
- `C10`: Increase transmission power for 3271205_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217062_4
- `C12`: Increase A3 Offset threshold for 3271205_1
- `C13`: Decrease A3 Offset threshold for 3271205_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271205_1
- `C15`: Add neighbor relationship between 3247739_2 and 3217062_4
- `C16`: Check test server and transmission issues
- `C17`: Decrease A3 Offset threshold for 3217062_4
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease transmission power for 3217062_4
- `C20`: Adjust the azimuth of 3247739_2 by 50 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271205_1
- `C22`: Add neighbor relationship between 3271205_1 and 3217062_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.358 | MS1 | 121.4656726386 | 31.1446275161 | 64 | 504990 | -90.39 | 14.75 | 352.54 | 0.14 | 2.49 | 1569 |
| 2024-09-20 22:21:32.471 | MS1 | 121.4656669155 | 31.1446307864 | 64 | 504990 | -88.76 | 17.25 | 590.47 | 0.18 | 2.89 | 1576 |
| 2024-09-20 22:21:33.792 | MS1 | 121.4656621685 | 31.1446364346 | 64 | 504990 | -90.06 | 12.46 | 324.52 | 0.10 | 2.99 | 1574 |
| 2024-09-20 22:21:34.227 | MS1 | 121.4656665292 | 31.1446304169 | 64 | 504990 | -91.64 | 13.75 | 52.56 | 0.05 | 2.20 | 1581 |
| 2024-09-20 22:21:35.286 | MS1 | 121.4656726548 | 31.1446355628 | 64 | 504990 | -88.12 | 15.78 | 87.31 | 0.10 | 2.48 | 1596 |
| 2024-09-20 22:21:36.907 | MS1 | 121.4656600793 | 31.1446243839 | 64 | 504990 | -88.34 | 13.60 | 99.55 | 0.17 | 2.64 | 1593 |
| 2024-09-20 22:21:37.299 | MS1 | 121.4656765494 | 31.1446188158 | 64 | 504990 | -92.69 | 12.99 | 95.40 | 0.15 | 2.64 | 1560 |
| 2024-09-20 22:21:38.737 | MS1 | 121.4656628891 | 31.1446335196 | 64 | 504990 | -89.46 | 8.58 | 55.28 | 0.13 | 2.28 | 1587 |
| 2024-09-20 22:21:39.928 | MS1 | 121.4656678026 | 31.1446344023 | 64 | 504990 | -93.21 | 12.61 | 52.41 | 0.20 | 2.17 | 1597 |
| 2024-09-20 22:21:40.239 | MS1 | 121.4656614922 | 31.1446257463 | 64 | 504990 | -92.33 | 11.38 | 304.66 | 0.01 | 2.33 | 1572 |
| 2024-09-20 22:21:41.283 | MS1 | 121.4656745276 | 31.1446360866 | 64 | 504990 | -89.85 | 9.94 | 433.54 | 0.02 | 2.05 | 1576 |
| 2024-09-20 22:21:42.753 | MS1 | 121.4656663233 | 31.1446376719 | 64 | 504990 | -89.37 | 8.12 | 433.68 | 0.06 | 2.08 | 1589 |

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
| 3217062 | 4 | 121.4724231239 | 31.1442520045 | 127 | 5 | 4 | 15.4 | TDD | 616 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3220021 | 3 | 121.4738264855 | 31.1481746608 | 82 | 10 | 2 | 28.8 | TDD | 153 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3247739 | 2 | 121.4641809810 | 31.1460035212 | 5 | 10 | 9 | 21.3 | TDD | 105 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3271205 | 1 | 121.4688605327 | 31.1479829743 | 217 | 0 | 10 | 27.5 | TDD | 64 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.496 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.514 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.650 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.650 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.331 | NREventA3 | measId:2;ServCellPCI:629;Se... |
| 2024-09-20 22:21:38.571 | NRHandoverAttempt | SourcePCI:629;SourceNR-ARFC... |
| 2024-09-20 22:21:38.609 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.621 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.752 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.752 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271205 | 1 | 82.6637 | 79.3553 | -115.9231 | 10.8675 | 82.9921 | 0.0056 | 0.0017 |
| 2024_09_20 22:00 | 3247739 | 2 | 18.1660 | 8.9645 | -114.6691 | 8.0514 | 112.1924 | 0.0054 | 0.0181 |
| 2024_09_20 22:00 | 3220021 | 3 | 18.5478 | 12.2899 | -114.0446 | 17.6263 | 188.3595 | 0.0088 | 0.0112 |
| 2024_09_20 22:00 | 3217062 | 4 | 18.8856 | 11.8497 | -116.7631 | 5.4027 | 123.5722 | 0.0097 | 0.0065 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414995_28647880 | 504990 | 64 | -92.8 | 504990 | 616 | -101.4 | 504990 | 105 | -104.6 | 504990 | 153 |
| MR_1774414995_4FE438DC | 504990 | 64 | -92.5 | 504990 | 616 | -101.0 | 504990 | 105 | -102.1 | 504990 | 153 |
| MR_1774414995_4FF9EA35 | 504990 | 64 | -90.0 | 504990 | 616 | -103.1 | 504990 | 105 | -104.0 | 504990 | 153 |
| MR_1774414995_B4C3A57F | 504990 | 64 | -90.5 | 504990 | 616 | -101.0 | 504990 | 105 | -102.6 | 504990 | 153 |
| MR_1774414995_7089C23E | 504990 | 64 | -92.6 | 504990 | 616 | -100.9 | 504990 | 105 | -101.9 | 504990 | 153 |
| MR_1774414995_BDFFE16B | 504990 | 64 | -89.7 | 504990 | 616 | -100.2 | 504990 | 105 | -104.3 | 504990 | 153 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 325: `7bf49ea7-fcf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7bf49ea7-fcf2-46b4-b0b5-f2980e1e7b6f` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[325] topology](images/test_0325.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3258049_2 by 6 degrees
- `C2`: Increase transmission power for 3258049_2
- `C3`: Adjust the azimuth of 3258049_2 by 50 degrees
- `C4`: Adjust the azimuth of 3267635_1 by 50 degrees
- `C5`: Decrease A3 Offset threshold for 3267635_1
- `C6`: Press down the tilt angle  of 3267635_1 by 6 degrees
- `C7`: Decrease transmission power for 3258049_2
- `C8`: Increase A3 Offset threshold for 3267635_1
- `C9`: Lift the tilt angle of 3258049_2 by 6 degrees
- `C10`: Decrease transmission power for 3267635_1
- `C11`: Add neighbor relationship between 3258049_2 and 3267635_1
- `C12`: Decrease A3 Offset threshold for 3258049_2
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Check test server and transmission issues
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258049_2
- `C16`: Lift the tilt angle  of 3267635_1 by 6 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258049_2
- `C18`: Increase transmission power for 3267635_1
- `C19`: Add neighbor relationship between 3224033_3 and 3267635_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267635_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267635_1
- `C22`: Increase A3 Offset threshold for 3258049_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.976 | MS1 | 121.4656609472 | 31.1446286425 | 492 | 504990 | -76.63 | 16.01 | 545.55 | 0.01 | 2.82 | 1582 |
| 2024-09-20 22:21:32.372 | MS1 | 121.4656649162 | 31.1446322975 | 492 | 504990 | -78.50 | 15.66 | 552.89 | 0.09 | 2.43 | 1573 |
| 2024-09-20 22:21:33.647 | MS1 | 121.4656737738 | 31.1446208282 | 492 | 504990 | -75.97 | 15.14 | 596.00 | 0.10 | 2.88 | 1589 |
| 2024-09-20 22:21:34.380 | MS1 | 121.4656753069 | 31.1446283903 | 492 | 504990 | -85.13 | -1.41 | 46.63 | 0.02 | 1.37 | 1560 |
| 2024-09-20 22:21:35.980 | MS1 | 121.4656764962 | 31.1446344949 | 492 | 504990 | -89.26 | -3.06 | 62.31 | 0.06 | 1.40 | 1582 |
| 2024-09-20 22:21:36.332 | MS1 | 121.4656774141 | 31.1446184546 | 492 | 504990 | -92.10 | -2.40 | 59.66 | 0.07 | 1.32 | 1598 |
| 2024-09-20 22:21:37.577 | MS1 | 121.4656586338 | 31.1446350634 | 492 | 504990 | -88.91 | -1.29 | 28.27 | 0.18 | 1.07 | 1577 |
| 2024-09-20 22:21:38.777 | MS1 | 121.4656587678 | 31.1446237517 | 492 | 504990 | -83.68 | -3.21 | 46.88 | 0.11 | 1.43 | 1598 |
| 2024-09-20 22:21:39.492 | MS1 | 121.4656631724 | 31.1446239323 | 730 | 504990 | -75.54 | 17.01 | 248.89 | 0.11 | 1.26 | 1574 |
| 2024-09-20 22:21:40.216 | MS1 | 121.4656706939 | 31.1446358872 | 730 | 504990 | -84.29 | 15.07 | 555.32 | 0.12 | 2.30 | 1579 |
| 2024-09-20 22:21:41.340 | MS1 | 121.4656653917 | 31.1446367205 | 730 | 504990 | -81.10 | 14.30 | 439.11 | 0.12 | 2.68 | 1583 |
| 2024-09-20 22:21:42.155 | MS1 | 121.4656638245 | 31.1446371003 | 730 | 504990 | -75.23 | 13.23 | 313.66 | 0.04 | 2.04 | 1577 |

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
| 3224033 | 3 | 121.4716889608 | 31.1527138002 | 239 | 11 | 7 | 32.7 | TDD | 556 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3258049 | 2 | 121.4709917537 | 31.1502380783 | 116 | 5 | 0 | 19.1 | TDD | 492 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3267635 | 1 | 121.4644441948 | 31.1542139043 | 118 | 4 | 3 | 37.6 | TDD | 730 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3279736 | 4 | 121.4697954280 | 31.1455187389 | 2 | 10 | 2 | 22.2 | TDD | 7 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.438 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.460 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.587 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.587 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.306 | NREventA3 | measId:2;ServCellPCI:317;Se... |
| 2024-09-20 22:21:38.546 | NRHandoverAttempt | SourcePCI:317;SourceNR-ARFC... |
| 2024-09-20 22:21:38.595 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.605 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.746 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.746 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267635 | 1 | 13.1682 | 18.7587 | -117.7134 | 7.7656 | 178.9159 | 0.0185 | 0.0074 |
| 2024_09_20 22:00 | 3258049 | 2 | 17.5278 | 17.7685 | -115.6825 | 10.9934 | 98.7018 | 0.0088 | 0.1555 |
| 2024_09_20 22:00 | 3224033 | 3 | 8.9450 | 6.6745 | -116.6059 | 9.8326 | 167.8936 | 0.0119 | 0.0159 |
| 2024_09_20 22:00 | 3279736 | 4 | 14.4785 | 7.5457 | -114.6645 | 14.9337 | 102.4594 | 0.0061 | 0.0113 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416259_BD2AAFB5 | 504990 | 492 | -85.0 | 504990 | 730 | -80.5 | 504990 | 556 | -85.0 | 504990 | 7 |
| MR_1774416259_91317611 | 504990 | 730 | -78.9 | 504990 | 492 | -85.2 | 504990 | 556 | -88.2 | 504990 | 7 |
| MR_1774416259_2966A639 | 504990 | 492 | -85.9 | 504990 | 730 | -81.3 | 504990 | 556 | -86.3 | 504990 | 7 |
| MR_1774416259_4437A943 | 504990 | 492 | -86.8 | 504990 | 730 | -81.4 | 504990 | 556 | -86.7 | 504990 | 7 |
| MR_1774416259_92D47C49 | 504990 | 492 | -83.8 | 504990 | 730 | -81.5 | 504990 | 556 | -87.1 | 504990 | 7 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 326: `34666e73-9ac...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `34666e73-9ac4-44a7-a61d-414848e0d4b4` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[326] topology](images/test_0326.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3226183_3
- `C2`: Lift the tilt angle of 3244577_2 by 10 degrees
- `C3`: Increase A3 Offset threshold for 3226183_3
- `C4`: Adjust the azimuth of 3226183_3 by 6 degrees
- `C5`: Add neighbor relationship between 3264133_1 and 3226183_3
- `C6`: Lift the tilt angle  of 3226183_3 by 3 degrees
- `C7`: Decrease A3 Offset threshold for 3226183_3
- `C8`: Increase A3 Offset threshold for 3244577_2
- `C9`: Increase transmission power for 3226183_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244577_2
- `C11`: Press down the tilt angle of 3244577_2 by 10 degrees
- `C12`: Check test server and transmission issues
- `C13`: Press down the tilt angle  of 3226183_3 by 3 degrees
- `C14`: Add neighbor relationship between 3244577_2 and 3226183_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226183_3
- `C16`: Decrease A3 Offset threshold for 3244577_2
- `C17`: Increase transmission power for 3244577_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226183_3
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244577_2
- `C21`: Decrease transmission power for 3244577_2
- `C22`: Adjust the azimuth of 3244577_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.769 | MS1 | 121.4656775847 | 31.1446321130 | 1005 | 504990 | -85.59 | 15.71 | 560.47 | 0.18 | 2.73 | 1577 |
| 2024-09-20 22:21:32.161 | MS1 | 121.4656614486 | 31.1446244945 | 1005 | 504990 | -88.32 | 14.88 | 504.94 | 0.05 | 2.42 | 1585 |
| 2024-09-20 22:21:33.695 | MS1 | 121.4656667946 | 31.1446234487 | 1005 | 504990 | -87.03 | 17.02 | 528.14 | 0.12 | 2.42 | 1579 |
| 2024-09-20 22:21:34.110 | MS1 | 121.4656640507 | 31.1446310705 | 1005 | 504990 | -104.46 | -1.50 | 34.13 | 0.11 | 1.47 | 1597 |
| 2024-09-20 22:21:35.337 | MS1 | 121.4656646256 | 31.1446307077 | 1005 | 504990 | -102.32 | 1.21 | 66.10 | 0.18 | 1.38 | 1567 |
| 2024-09-20 22:21:36.892 | MS1 | 121.4656653585 | 31.1446343794 | 1005 | 504990 | -101.02 | 0.69 | 58.45 | 0.02 | 1.16 | 1594 |
| 2024-09-20 22:21:37.686 | MS1 | 121.4656745083 | 31.1446283988 | 1005 | 504990 | -109.03 | 1.75 | 25.22 | 0.08 | 1.01 | 1599 |
| 2024-09-20 22:21:38.829 | MS1 | 121.4656637700 | 31.1446209577 | 1005 | 504990 | -104.03 | 1.86 | 51.46 | 0.08 | 1.29 | 1577 |
| 2024-09-20 22:21:39.356 | MS1 | 121.4656643789 | 31.1446232000 | 1005 | 504990 | -106.45 | 1.25 | 47.84 | 0.09 | 1.29 | 1588 |
| 2024-09-20 22:21:40.526 | MS1 | 121.4656717533 | 31.1446377816 | 1005 | 504990 | -85.72 | 14.42 | 539.90 | 0.01 | 2.54 | 1560 |
| 2024-09-20 22:21:41.308 | MS1 | 121.4656718757 | 31.1446325857 | 1005 | 504990 | -92.96 | 17.14 | 368.73 | 0.01 | 2.56 | 1577 |
| 2024-09-20 22:21:42.223 | MS1 | 121.4656627978 | 31.1446182934 | 1005 | 504990 | -86.75 | 12.75 | 343.21 | 0.06 | 2.16 | 1570 |

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
| 3226183 | 3 | 121.4735179536 | 31.1465784018 | 260 | 2 | 0 | 18.5 | TDD | 246 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3244577 | 2 | 121.4660492366 | 31.1510377301 | 127 | 7 | 10 | 46.8 | TDD | 1005 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3264133 | 1 | 121.4658938408 | 31.1462823309 | 52 | 15 | 4 | 29.6 | TDD | 848 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3276957 | 4 | 121.4750879269 | 31.1545940164 | 165 | 7 | 1 | 22.3 | TDD | 742 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.565 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.582 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.686 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.686 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.925 | NREventA2 | measId:1;ServCellPCI:842;Se... |
| 2024-09-20 22:21:35.025 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264133 | 1 | 5.9678 | 14.1298 | -116.5451 | 10.3445 | 192.6062 | 0.0038 | 0.0174 |
| 2024_09_20 22:00 | 3244577 | 2 | 19.3629 | 10.0312 | -114.6730 | 18.6882 | 139.8759 | 0.1985 | 0.0134 |
| 2024_09_20 22:00 | 3226183 | 3 | 10.7681 | 16.9931 | -116.8495 | 17.1162 | 196.8547 | 0.0118 | 0.0116 |
| 2024_09_20 22:00 | 3276957 | 4 | 15.1006 | 15.0116 | -114.7007 | 7.0343 | 198.8452 | 0.0117 | 0.0053 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414824_2DEE2E4E | 504990 | 1005 | -103.0 | 504990 | 246 | -106.4 | 504990 | 848 | -116.3 | 504990 | 742 |
| MR_1774414824_0CE0E02C | 504990 | 1005 | -104.6 | 504990 | 246 | -106.9 | 504990 | 848 | -113.8 | 504990 | 742 |
| MR_1774414824_D6B5764C | 504990 | 1005 | -104.0 | 504990 | 246 | -106.5 | 504990 | 848 | -115.3 | 504990 | 742 |
| MR_1774414824_8FC65726 | 504990 | 1005 | -106.0 | 504990 | 246 | -106.7 | 504990 | 848 | -114.1 | 504990 | 742 |
| MR_1774414824_F259BB33 | 504990 | 1005 | -103.3 | 504990 | 246 | -107.5 | 504990 | 848 | -113.5 | 504990 | 742 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 327: `8a97cbab-5a7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8a97cbab-5a71-433b-bd06-a80e02b1c9df` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[327] topology](images/test_0327.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275396_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219958_4
- `C3`: Increase transmission power for 3219958_4
- `C4`: Decrease A3 Offset threshold for 3275396_2
- `C5`: Add neighbor relationship between 3232731_3 and 3219958_4
- `C6`: Decrease transmission power for 3219958_4
- `C7`: Adjust the azimuth of 3219958_4 by 7 degrees
- `C8`: Adjust the azimuth of 3275396_2 by 50 degrees
- `C9`: Press down the tilt angle of 3275396_2 by 4 degrees
- `C10`: Check test server and transmission issues
- `C11`: Add neighbor relationship between 3275396_2 and 3219958_4
- `C12`: Press down the tilt angle  of 3219958_4 by 5 degrees
- `C13`: Lift the tilt angle  of 3219958_4 by 5 degrees
- `C14`: Decrease A3 Offset threshold for 3219958_4
- `C15`: Increase A3 Offset threshold for 3275396_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275396_2
- `C17`: Increase transmission power for 3275396_2
- `C18`: Lift the tilt angle of 3275396_2 by 4 degrees
- `C19`: Increase A3 Offset threshold for 3219958_4
- `C20`: Decrease transmission power for 3275396_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219958_4
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.596 | MS1 | 121.4656612934 | 31.1446367277 | 698 | 504990 | -88.77 | 14.79 | 317.19 | 0.08 | 2.29 | 1594 |
| 2024-09-20 22:21:32.996 | MS1 | 121.4656690155 | 31.1446268112 | 698 | 504990 | -92.13 | 13.98 | 496.56 | 0.17 | 2.69 | 1589 |
| 2024-09-20 22:21:33.823 | MS1 | 121.4656748994 | 31.1446189399 | 698 | 504990 | -91.92 | 13.81 | 537.06 | 0.13 | 2.53 | 1568 |
| 2024-09-20 22:21:34.534 | MS1 | 121.4656775318 | 31.1446331692 | 698 | 504990 | -109.58 | -1.67 | 55.65 | 0.04 | 1.25 | 1586 |
| 2024-09-20 22:21:35.299 | MS1 | 121.4656735450 | 31.1446243086 | 698 | 504990 | -107.20 | 0.64 | 49.69 | 0.16 | 1.08 | 1583 |
| 2024-09-20 22:21:36.355 | MS1 | 121.4656613317 | 31.1446295066 | 698 | 504990 | -107.12 | -1.62 | 18.36 | 0.18 | 1.49 | 1596 |
| 2024-09-20 22:21:37.927 | MS1 | 121.4656706083 | 31.1446286121 | 698 | 504990 | -100.87 | 1.76 | 57.38 | 0.03 | 1.19 | 1591 |
| 2024-09-20 22:21:38.804 | MS1 | 121.4656610939 | 31.1446248406 | 698 | 504990 | -107.13 | 1.91 | 73.51 | 0.12 | 1.27 | 1560 |
| 2024-09-20 22:21:39.549 | MS1 | 121.4656596978 | 31.1446244501 | 698 | 504990 | -105.94 | 0.25 | 40.55 | 0.13 | 1.25 | 1594 |
| 2024-09-20 22:21:40.408 | MS1 | 121.4656626148 | 31.1446366140 | 698 | 504990 | -93.69 | 17.59 | 542.69 | 0.18 | 2.66 | 1582 |
| 2024-09-20 22:21:41.138 | MS1 | 121.4656722427 | 31.1446327824 | 698 | 504990 | -87.71 | 15.97 | 344.99 | 0.08 | 2.62 | 1599 |
| 2024-09-20 22:21:42.470 | MS1 | 121.4656697249 | 31.1446259557 | 698 | 504990 | -85.45 | 12.54 | 382.08 | 0.12 | 2.62 | 1562 |

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
| 3219958 | 4 | 121.4674178361 | 31.1500601437 | 202 | 2 | 7 | 28.9 | TDD | 310 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3232731 | 3 | 121.4677221615 | 31.1521889897 | 154 | 6 | 3 | 43.6 | TDD | 451 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3266794 | 1 | 121.4729970602 | 31.1441707762 | 11 | 5 | 10 | 18.6 | TDD | 224 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3275396 | 2 | 121.4744253706 | 31.1470781602 | 328 | 3 | 11 | 17.5 | TDD | 698 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.481 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.506 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.609 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.609 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.846 | NREventA2 | measId:1;ServCellPCI:58;Ser... |
| 2024-09-20 22:21:34.968 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266794 | 1 | 18.8101 | 18.6460 | -115.0016 | 18.9895 | 191.7772 | 0.0070 | 0.0006 |
| 2024_09_20 22:00 | 3275396 | 2 | 9.1592 | 14.5285 | -115.7702 | 13.3901 | 94.7562 | 0.1449 | 0.0114 |
| 2024_09_20 22:00 | 3232731 | 3 | 12.5294 | 12.0338 | -117.9486 | 17.5976 | 81.4355 | 0.0077 | 0.0139 |
| 2024_09_20 22:00 | 3219958 | 4 | 12.3476 | 6.9330 | -114.4736 | 5.4347 | 129.2783 | 0.0198 | 0.0014 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415986_215EE59A | 504990 | 698 | -109.4 | 504990 | 310 | -113.8 | 504990 | 451 | -121.6 | 504990 | 224 |
| MR_1774415986_6E1F649E | 504990 | 698 | -110.3 | 504990 | 310 | -114.0 | 504990 | 451 | -120.5 | 504990 | 224 |
| MR_1774415986_9B345D83 | 504990 | 698 | -108.2 | 504990 | 310 | -114.5 | 504990 | 451 | -118.5 | 504990 | 224 |
| MR_1774415986_E8E9063E | 504990 | 698 | -109.0 | 504990 | 310 | -110.7 | 504990 | 451 | -118.6 | 504990 | 224 |
| MR_1774415986_D0EEFCF3 | 504990 | 698 | -108.2 | 504990 | 310 | -113.1 | 504990 | 451 | -120.7 | 504990 | 224 |
| MR_1774415986_C68015E6 | 504990 | 698 | -108.7 | 504990 | 310 | -113.1 | 504990 | 451 | -119.9 | 504990 | 224 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 328: `006d5394-3de...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `006d5394-3dec-4a3d-bb7e-d2b8450c39a9` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[328] topology](images/test_0328.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3278835_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263276_2
- `C3`: Lift the tilt angle of 3263276_2 by 5 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278835_1
- `C5`: Add neighbor relationship between 3221714_3 and 3278835_1
- `C6`: Decrease A3 Offset threshold for 3278835_1
- `C7`: Adjust the azimuth of 3278835_1 by 50 degrees
- `C8`: Decrease A3 Offset threshold for 3263276_2
- `C9`: Press down the tilt angle  of 3278835_1 by 10 degrees
- `C10`: Press down the tilt angle of 3263276_2 by 5 degrees
- `C11`: Decrease transmission power for 3263276_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278835_1
- `C13`: Decrease transmission power for 3278835_1
- `C14`: Adjust the azimuth of 3263276_2 by 9 degrees
- `C15`: Lift the tilt angle  of 3278835_1 by 10 degrees
- `C16`: Increase transmission power for 3263276_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263276_2
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Check test server and transmission issues
- `C20`: Add neighbor relationship between 3263276_2 and 3278835_1
- `C21`: Increase A3 Offset threshold for 3263276_2
- `C22`: Increase A3 Offset threshold for 3278835_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.823 | MS1 | 121.4656601042 | 31.1446355516 | 775 | 504990 | -87.14 | 12.51 | 464.85 | 0.16 | 2.92 | 1592 |
| 2024-09-20 22:21:32.598 | MS1 | 121.4656650226 | 31.1446247835 | 775 | 504990 | -86.67 | 12.25 | 398.42 | 0.20 | 2.81 | 1572 |
| 2024-09-20 22:21:33.249 | MS1 | 121.4656750014 | 31.1446189678 | 775 | 504990 | -89.80 | 17.43 | 447.23 | 0.18 | 2.96 | 1560 |
| 2024-09-20 22:21:34.608 | MS1 | 121.4656581484 | 31.1446192245 | 775 | 504990 | -85.01 | 14.30 | 58.21 | 0.60 | 2.46 | 610 |
| 2024-09-20 22:21:35.162 | MS1 | 121.4656620977 | 31.1446186260 | 775 | 504990 | -87.55 | 14.46 | 87.74 | 0.64 | 2.32 | 658 |
| 2024-09-20 22:21:36.753 | MS1 | 121.4656581744 | 31.1446196545 | 775 | 504990 | -88.34 | 14.13 | 89.82 | 0.51 | 2.17 | 610 |
| 2024-09-20 22:21:37.939 | MS1 | 121.4656747696 | 31.1446208664 | 775 | 504990 | -89.30 | 9.74 | 78.20 | 0.63 | 2.27 | 599 |
| 2024-09-20 22:21:38.561 | MS1 | 121.4656595628 | 31.1446316471 | 775 | 504990 | -91.24 | 10.59 | 78.81 | 0.65 | 2.89 | 508 |
| 2024-09-20 22:21:39.582 | MS1 | 121.4656746602 | 31.1446354309 | 775 | 504990 | -90.76 | 11.44 | 87.31 | 0.64 | 2.38 | 587 |
| 2024-09-20 22:21:40.305 | MS1 | 121.4656702065 | 31.1446304610 | 775 | 504990 | -89.51 | 8.32 | 591.77 | 0.15 | 2.89 | 1579 |
| 2024-09-20 22:21:41.977 | MS1 | 121.4656660574 | 31.1446344213 | 775 | 504990 | -89.25 | 9.67 | 531.06 | 0.06 | 2.20 | 1565 |
| 2024-09-20 22:21:42.456 | MS1 | 121.4656591270 | 31.1446348062 | 775 | 504990 | -92.39 | 9.69 | 390.01 | 0.06 | 2.58 | 1561 |

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
| 3221714 | 3 | 121.4731658838 | 31.1507200367 | 158 | 1 | 8 | 22.4 | TDD | 351 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3263276 | 2 | 121.4646476160 | 31.1547368050 | 184 | 3 | 1 | 37.5 | TDD | 775 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3269027 | 4 | 121.4746640760 | 31.1517734737 | 22 | 14 | 7 | 27.7 | TDD | 415 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3278835 | 1 | 121.4661022656 | 31.1539260329 | 353 | 13 | 6 | 47.5 | TDD | 23 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.946 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.965 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.091 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.091 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.802 | NREventA3 | measId:2;ServCellPCI:671;Se... |
| 2024-09-20 22:21:38.042 | NRHandoverAttempt | SourcePCI:671;SourceNR-ARFC... |
| 2024-09-20 22:21:38.078 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.093 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.196 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.196 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278835 | 1 | 17.7530 | 16.2646 | -114.3811 | 16.5800 | 132.5424 | 0.0051 | 0.0184 |
| 2024_09_20 22:00 | 3263276 | 2 | 15.6816 | 7.9074 | -115.3808 | 15.8567 | 197.5513 | 0.0148 | 0.0131 |
| 2024_09_20 22:00 | 3221714 | 3 | 5.6366 | 6.7488 | -114.6858 | 6.5928 | 117.6981 | 0.0096 | 0.0114 |
| 2024_09_20 22:00 | 3269027 | 4 | 13.6770 | 5.3901 | -114.1308 | 7.0930 | 131.4568 | 0.0045 | 0.0127 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413645_ED35F4E6 | 504990 | 775 | -83.8 | 504990 | 23 | -91.5 | 504990 | 351 | -99.8 | 504990 | 415 |
| MR_1774413645_A4EF4BB8 | 504990 | 775 | -83.5 | 504990 | 23 | -91.6 | 504990 | 351 | -99.4 | 504990 | 415 |
| MR_1774413645_D3BCF917 | 504990 | 775 | -83.6 | 504990 | 23 | -89.5 | 504990 | 351 | -101.3 | 504990 | 415 |
| MR_1774413645_9714D93A | 504990 | 775 | -84.5 | 504990 | 23 | -91.5 | 504990 | 351 | -100.7 | 504990 | 415 |
| MR_1774413645_2FE2BAF0 | 504990 | 775 | -86.7 | 504990 | 23 | -88.9 | 504990 | 351 | -99.3 | 504990 | 415 |
| MR_1774413645_D19B668E | 504990 | 775 | -85.7 | 504990 | 23 | -91.3 | 504990 | 351 | -101.0 | 504990 | 415 |
| MR_1774413645_DEB820A7 | 504990 | 775 | -87.0 | 504990 | 23 | -87.9 | 504990 | 351 | -100.9 | 504990 | 415 |
| MR_1774413645_45B06BEB | 504990 | 775 | -86.1 | 504990 | 23 | -90.8 | 504990 | 351 | -100.2 | 504990 | 415 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 329: `bb5989fd-694...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bb5989fd-6942-46e3-93ce-4781517ee241` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[329] topology](images/test_0329.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase A3 Offset threshold for 3244361_6
- `C3`: Adjust the azimuth of 3244361_6 by 8 degrees
- `C4`: Increase A3 Offset threshold for 3214806_2
- `C5`: Check test server and transmission issues
- `C6`: Add neighbor relationship between 3244361_6 and 3214806_2
- `C7`: Increase transmission power for 3214806_2
- `C8`: Lift the tilt angle of 3244361_6 by 5 degrees
- `C9`: Decrease A3 Offset threshold for 3244361_6
- `C10`: Decrease transmission power for 3214806_2
- `C11`: Lift the tilt angle  of 3214806_2 by 6 degrees
- `C12`: Decrease transmission power for 3244361_6
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214806_2
- `C14`: Press down the tilt angle  of 3214806_2 by 6 degrees
- `C15`: Decrease A3 Offset threshold for 3214806_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214806_2
- `C17`: Add neighbor relationship between 3271758_9 and 3214806_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244361_6
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244361_6
- `C20`: Increase transmission power for 3244361_6
- `C21`: Adjust the azimuth of 3214806_2 by 42 degrees
- `C22`: Press down the tilt angle of 3244361_6 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.273 | MS1 | 121.4656634137 | 31.1446370185 | 248 | 504990 | -95.61 | 9.90 | 556.92 | 0.18 | 2.82 | 1572 |
| 2024-09-20 22:21:32.944 | MS1 | 121.4656645994 | 31.1446252496 | 18 | 504990 | -95.75 | 11.60 | 313.43 | 0.09 | 2.44 | 1590 |
| 2024-09-20 22:21:33.663 | MS1 | 121.4656702194 | 31.1446316534 | 83 | 504990 | -94.48 | 9.53 | 344.65 | 0.08 | 2.56 | 1561 |
| 2024-09-20 22:21:34.860 | MS1 | 121.4656743674 | 31.1446235085 | 315 | 152650 | -87.81 | 6.26 | 101.62 | 0.14 | 1.95 | 908 |
| 2024-09-20 22:21:35.346 | MS1 | 121.4656730252 | 31.1446292541 | 340 | 152650 | -89.24 | 5.66 | 68.56 | 0.06 | 1.53 | 966 |
| 2024-09-20 22:21:36.950 | MS1 | 121.4656655661 | 31.1446293237 | 657 | 152650 | -88.55 | 5.56 | 62.74 | 0.10 | 1.61 | 934 |
| 2024-09-20 22:21:37.584 | MS1 | 121.4656602204 | 31.1446301729 | 20 | 152650 | -87.56 | 5.22 | 66.77 | 0.08 | 1.81 | 924 |
| 2024-09-20 22:21:38.386 | MS1 | 121.4656697393 | 31.1446363371 | 315 | 152650 | -88.18 | 3.70 | 52.35 | 0.13 | 1.91 | 947 |
| 2024-09-20 22:21:39.881 | MS1 | 121.4656602837 | 31.1446293764 | 340 | 152650 | -93.15 | 7.37 | 81.39 | 0.14 | 1.80 | 988 |
| 2024-09-20 22:21:40.479 | MS1 | 121.4656681562 | 31.1446231009 | 657 | 152650 | -96.07 | 4.98 | 79.87 | 0.09 | 2.45 | 1591 |
| 2024-09-20 22:21:41.768 | MS1 | 121.4656629222 | 31.1446310684 | 20 | 152650 | -90.88 | 5.49 | 67.05 | 0.15 | 2.22 | 1595 |
| 2024-09-20 22:21:42.266 | MS1 | 121.4656657617 | 31.1446207704 | 315 | 152650 | -94.01 | 6.76 | 69.65 | 0.00 | 2.69 | 1582 |

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
| 3210041 | 11 | 121.4660134947 | 31.1493691642 | 1 | 12 | 6 | 24.4 | FDD | 20 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3210970 | 8 | 121.4671962534 | 31.1520132394 | 150 | 5 | 7 | 17.3 | FDD | 361 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3214806 | 2 | 121.4686605091 | 31.1480343666 | 259 | 5 | 10 | 4.4 | TDD | 71 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3219048 | 12 | 121.4725600580 | 31.1555718733 | 30 | 9 | 7 | 21.4 | FDD | 315 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3224162 | 1 | 121.4745416487 | 31.1532502626 | 343 | 15 | 9 | 28.8 | TDD | 389 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3241579 | 5 | 121.4681179902 | 31.1509692654 | 58 | 13 | 3 | 28.0 | TDD | 55 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3244361 | 6 | 121.4758852328 | 31.1534498730 | 217 | 4 | 2 | 20.0 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3253117 | 10 | 121.4678456486 | 31.1489171833 | 84 | 7 | 0 | 23.3 | FDD | 340 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3253682 | 7 | 121.4723025953 | 31.1484965704 | 132 | 8 | 6 | 3.3 | FDD | 553 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3259114 | 3 | 121.4681057806 | 31.1455353142 | 233 | 14 | 4 | 26.4 | TDD | 18 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3263954 | 13 | 121.4720159366 | 31.1482673602 | 17 | 4 | 9 | 18.3 | FDD | 668 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3271758 | 9 | 121.4657314462 | 31.1510881434 | 279 | 4 | 11 | 19.8 | FDD | 657 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3275148 | 4 | 121.4678738438 | 31.1559878813 | 112 | 11 | 6 | 5.0 | TDD | 83 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.283 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.305 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.446 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.446 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.148 | NREventA2 | measId:1;ServCellPCI:351;Se... |
| 2024-09-20 22:21:35.255 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.503 | NREventA5 | measId:3;ServCellPCI:351;Se... |
| 2024-09-20 22:21:35.535 | NRHandoverAttempt | SourcePCI:351;SourceNR-ARFC... |
| 2024-09-20 22:21:35.572 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.586 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.734 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.734 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224162 | 1 | 19.3328 | 14.2154 | -115.5460 | 14.7256 | 197.3028 | 0.0147 | 0.0063 |
| 2024_09_20 22:00 | 3214806 | 2 | 19.9592 | 9.3584 | -117.9797 | 17.3491 | 91.3072 | 0.0088 | 0.0002 |
| 2024_09_20 22:00 | 3259114 | 3 | 19.2338 | 9.8741 | -114.0283 | 16.6270 | 85.6344 | 0.0026 | 0.0185 |
| 2024_09_20 22:00 | 3275148 | 4 | 12.0636 | 10.4009 | -116.1455 | 10.9381 | 145.3870 | 0.0168 | 0.0086 |
| 2024_09_20 22:00 | 3241579 | 5 | 14.3986 | 16.9416 | -116.4439 | 11.6694 | 163.0987 | 0.0049 | 0.0161 |
| 2024_09_20 22:00 | 3244361 | 6 | 16.1479 | 14.3236 | -114.3475 | 16.4670 | 167.8961 | 0.0113 | 0.0110 |
| 2024_09_20 22:00 | 3253682 | 7 | 16.0546 | 5.8761 | -114.8211 | 3.9167 | 30.2221 | 0.0029 | 0.0185 |
| 2024_09_20 22:00 | 3210970 | 8 | 5.6082 | 14.6932 | -115.8903 | 4.4403 | 58.7941 | 0.0041 | 0.0082 |
| 2024_09_20 22:00 | 3271758 | 9 | 15.4167 | 8.6900 | -115.0599 | 3.2859 | 52.2639 | 0.0174 | 0.0041 |
| 2024_09_20 22:00 | 3253117 | 10 | 17.5261 | 16.5451 | -117.5827 | 3.8399 | 31.4307 | 0.0004 | 0.0155 |
| 2024_09_20 22:00 | 3210041 | 11 | 17.2323 | 7.4054 | -116.4811 | 3.2699 | 39.4255 | 0.0043 | 0.0033 |
| 2024_09_20 22:00 | 3219048 | 12 | 18.2669 | 10.9929 | -117.3070 | 3.9087 | 33.7944 | 0.0100 | 0.0113 |
| 2024_09_20 22:00 | 3263954 | 13 | 6.8273 | 10.2691 | -114.1024 | 3.4178 | 41.8716 | 0.0059 | 0.0025 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416684_CE24DB1E | 152650 | 340 | -90.6 | 152650 | 553 | -94.5 | 152650 | 361 | -94.1 | 152650 | 668 |
| MR_1774416684_B242ED20 | 152650 | 340 | -90.6 | 152650 | 553 | -93.9 | 152650 | 361 | -97.0 | 152650 | 668 |
| MR_1774416684_A3E1E28E | 152650 | 340 | -87.8 | 152650 | 553 | -94.8 | 152650 | 361 | -95.0 | 152650 | 668 |
| MR_1774416684_D813D08C | 152650 | 340 | -91.2 | 152650 | 553 | -93.6 | 152650 | 361 | -96.1 | 152650 | 668 |
| MR_1774416684_ABBBF502 | 504990 | 83 | -95.5 | 504990 | 71 | -90.5 | 504990 | 389 | -94.0 | 504990 | 55 |
| MR_1774416684_67C8CA78 | 504990 | 83 | -93.9 | 504990 | 71 | -89.8 | 504990 | 389 | -92.4 | 504990 | 55 |

> *... 2개 열 생략 (전체 14열)*

---
