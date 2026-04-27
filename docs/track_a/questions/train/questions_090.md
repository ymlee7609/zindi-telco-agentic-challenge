# Track A 문제 분석 — train[890]~train[899]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[890] ~ train[899] (10개)

## 목차

1. [문제 890: `14127e81-3b8...`](#890) — single-answer, 정답: C7
2. [문제 891: `5bfa9dd1-ca8...`](#891) — multiple-answer, 정답: C3|C15
3. [문제 892: `220e43a9-54c...`](#892) — single-answer, 정답: C5
4. [문제 893: `7a62f650-e7e...`](#893) — single-answer, 정답: C11
5. [문제 894: `13c760ee-4d4...`](#894) — single-answer, 정답: C4
6. [문제 895: `dc98be69-4ac...`](#895) — single-answer, 정답: C12
7. [문제 896: `a6135277-6e7...`](#896) — single-answer, 정답: C17
8. [문제 897: `ff87d90f-f00...`](#897) — single-answer, 정답: C3
9. [문제 898: `9ebb53e6-1e5...`](#898) — single-answer, 정답: C21
10. [문제 899: `697d8783-60f...`](#899) — single-answer, 정답: C15

---

### 문제 890: `14127e81-3b8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `14127e81-3b84-4730-951f-26c8b214d40c` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236382_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[890] topology](images/train_0890.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease A3 Offset threshold for 3236382_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236382_4
- `C4`: Press down the tilt angle of 3236382_4 by 3 degrees
- `C5`: Increase transmission power for 3236382_4
- `C6`: Add neighbor relationship between 3239218_7 and 3211645_6
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236382_4 **← 정답**
- `C8`: Adjust the azimuth of 3211645_6 by 48 degrees
- `C9`: Increase transmission power for 3211645_6
- `C10`: Adjust the azimuth of 3236382_4 by 18 degrees
- `C11`: Increase A3 Offset threshold for 3236382_4
- `C12`: Add neighbor relationship between 3236382_4 and 3211645_6
- `C13`: Decrease A3 Offset threshold for 3211645_6
- `C14`: Decrease transmission power for 3211645_6
- `C15`: Lift the tilt angle  of 3211645_6 by 4 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211645_6
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211645_6
- `C18`: Decrease transmission power for 3236382_4
- `C19`: Press down the tilt angle  of 3211645_6 by 4 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Lift the tilt angle of 3236382_4 by 3 degrees
- `C22`: Increase A3 Offset threshold for 3211645_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.157 | MS1 | 121.4656778016 | 31.1446195162 | 44 | 504990 | -93.87 | 9.46 | 561.81 | 0.17 | 2.33 | 1593 |
| 2024-09-20 22:21:32.763 | MS1 | 121.4656678714 | 31.1446379975 | 773 | 504990 | -94.52 | 9.98 | 500.11 | 0.14 | 2.75 | 1564 |
| 2024-09-20 22:21:33.236 | MS1 | 121.4656684250 | 31.1446347947 | 882 | 504990 | -95.11 | 9.85 | 456.42 | 0.18 | 2.37 | 1568 |
| 2024-09-20 22:21:34.164 | MS1 | 121.4656719897 | 31.1446240639 | 811 | 152650 | -91.16 | 5.52 | 74.72 | 0.12 | 1.67 | 944 |
| 2024-09-20 22:21:35.320 | MS1 | 121.4656662217 | 31.1446182427 | 686 | 152650 | -87.65 | 5.55 | 98.55 | 0.03 | 1.55 | 908 |
| 2024-09-20 22:21:36.958 | MS1 | 121.4656764582 | 31.1446275922 | 354 | 152650 | -95.51 | 5.30 | 76.49 | 0.03 | 1.78 | 968 |
| 2024-09-20 22:21:37.154 | MS1 | 121.4656683299 | 31.1446234929 | 937 | 152650 | -88.71 | 3.74 | 94.47 | 0.14 | 2.00 | 917 |
| 2024-09-20 22:21:38.841 | MS1 | 121.4656674937 | 31.1446193815 | 811 | 152650 | -95.92 | 6.59 | 81.08 | 0.14 | 1.55 | 973 |
| 2024-09-20 22:21:39.810 | MS1 | 121.4656647366 | 31.1446292225 | 686 | 152650 | -87.78 | 2.42 | 87.69 | 0.19 | 1.99 | 972 |
| 2024-09-20 22:21:40.601 | MS1 | 121.4656731684 | 31.1446209566 | 354 | 152650 | -95.88 | 6.87 | 89.73 | 0.12 | 2.93 | 1560 |
| 2024-09-20 22:21:41.109 | MS1 | 121.4656608684 | 31.1446272119 | 937 | 152650 | -90.95 | 4.01 | 48.25 | 0.14 | 2.88 | 1561 |
| 2024-09-20 22:21:42.507 | MS1 | 121.4656586497 | 31.1446288235 | 811 | 152650 | -94.64 | 6.33 | 69.95 | 0.12 | 2.69 | 1573 |

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
| 3211645 | 6 | 121.4715070079 | 31.1559849473 | 252 | 3 | 5 | 28.5 | TDD | 468 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3211862 | 13 | 121.4744757291 | 31.1461131246 | 55 | 3 | 7 | 22.7 | FDD | 127 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3216082 | 3 | 121.4730690568 | 31.1463759424 | 183 | 9 | 12 | 4.5 | TDD | 613 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3223288 | 8 | 121.4749094905 | 31.1453552525 | 329 | 2 | 6 | 14.5 | FDD | 418 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3227723 | 12 | 121.4665744056 | 31.1548751881 | 196 | 4 | 5 | 12.6 | FDD | 466 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3232955 | 9 | 121.4755970657 | 31.1490009868 | 83 | 7 | 3 | 29.6 | FDD | 937 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3236382 | 4 | 121.4737005983 | 31.1538560971 | 235 | 2 | 11 | 14.5 | TDD | 44 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3237062 | 5 | 121.4654243185 | 31.1528865440 | 335 | 14 | 6 | 12.4 | TDD | 882 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3239218 | 7 | 121.4655183870 | 31.1558393507 | 146 | 9 | 4 | 10.8 | FDD | 354 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3255950 | 10 | 121.4729751253 | 31.1487953702 | 66 | 15 | 2 | 14.1 | FDD | 811 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3262373 | 11 | 121.4747128569 | 31.1468382374 | 284 | 4 | 4 | 27.9 | FDD | 686 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3272084 | 2 | 121.4709244869 | 31.1476128106 | 335 | 7 | 10 | 28.9 | TDD | 773 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3277830 | 1 | 121.4755156564 | 31.1502362013 | 53 | 10 | 10 | 11.6 | TDD | 67 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.782 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.802 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.940 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.940 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.667 | NREventA2 | measId:1;ServCellPCI:463;Se... |
| 2024-09-20 22:21:34.803 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.029 | NREventA5 | measId:3;ServCellPCI:463;Se... |
| 2024-09-20 22:21:35.081 | NRHandoverAttempt | SourcePCI:463;SourceNR-ARFC... |
| 2024-09-20 22:21:35.107 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.121 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.227 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.227 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277830 | 1 | 18.1194 | 7.2466 | -116.4015 | 16.4656 | 125.7372 | 0.0099 | 0.0197 |
| 2024_09_20 22:00 | 3272084 | 2 | 6.8731 | 15.8193 | -115.0610 | 16.7511 | 173.1513 | 0.0162 | 0.0013 |
| 2024_09_20 22:00 | 3216082 | 3 | 6.4290 | 18.8282 | -117.6786 | 13.6574 | 81.2909 | 0.0084 | 0.0082 |
| 2024_09_20 22:00 | 3236382 | 4 | 7.9177 | 10.8715 | -117.5786 | 14.1619 | 169.0580 | 0.0054 | 0.0168 |
| 2024_09_20 22:00 | 3237062 | 5 | 9.2115 | 5.9216 | -116.1697 | 11.9995 | 141.6564 | 0.0103 | 0.0053 |
| 2024_09_20 22:00 | 3211645 | 6 | 19.7172 | 14.5583 | -116.6564 | 13.3351 | 114.0439 | 0.0035 | 0.0036 |
| 2024_09_20 22:00 | 3239218 | 7 | 10.0254 | 10.5642 | -116.7463 | 3.4096 | 30.3660 | 0.0196 | 0.0000 |
| 2024_09_20 22:00 | 3223288 | 8 | 15.4474 | 8.6859 | -116.1708 | 3.0261 | 25.8309 | 0.0191 | 0.0031 |
| 2024_09_20 22:00 | 3232955 | 9 | 10.3908 | 17.0256 | -117.6258 | 4.4644 | 52.6031 | 0.0023 | 0.0146 |
| 2024_09_20 22:00 | 3255950 | 10 | 15.0250 | 16.9104 | -114.1176 | 3.6041 | 34.8753 | 0.0052 | 0.0172 |
| 2024_09_20 22:00 | 3262373 | 11 | 11.3174 | 9.9784 | -117.8584 | 4.7841 | 57.0398 | 0.0108 | 0.0054 |
| 2024_09_20 22:00 | 3227723 | 12 | 5.1722 | 7.2969 | -114.8636 | 4.9575 | 33.3125 | 0.0163 | 0.0131 |
| 2024_09_20 22:00 | 3211862 | 13 | 16.5250 | 18.8799 | -116.2617 | 3.6556 | 57.0424 | 0.0122 | 0.0158 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416481_E9F5AC59 | 504990 | 882 | -95.2 | 504990 | 468 | -95.9 | 504990 | 67 | -100.0 | 504990 | 613 |
| MR_1774416481_66045D21 | 504990 | 882 | -96.4 | 504990 | 468 | -95.1 | 504990 | 67 | -99.0 | 504990 | 613 |
| MR_1774416481_8E4FE60E | 504990 | 882 | -93.9 | 504990 | 468 | -95.1 | 504990 | 67 | -101.6 | 504990 | 613 |
| MR_1774416481_63BC2925 | 504990 | 882 | -96.1 | 504990 | 468 | -95.5 | 504990 | 67 | -99.6 | 504990 | 613 |
| MR_1774416481_E2B07306 | 504990 | 882 | -94.6 | 504990 | 468 | -93.4 | 504990 | 67 | -101.0 | 504990 | 613 |
| MR_1774416481_D17E7718 | 152650 | 811 | -91.2 | 152650 | 466 | -95.6 | 152650 | 418 | -98.2 | 152650 | 127 |
| MR_1774416481_3CEDC1C9 | 152650 | 811 | -90.8 | 152650 | 466 | -97.7 | 152650 | 418 | -99.3 | 152650 | 127 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 891: `5bfa9dd1-ca8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5bfa9dd1-ca87-49ae-a8e7-27785fd87ddf` |
| Tag | **multiple-answer** |
| 정답 | **C3|C15** |
| C3 의미 | Increase transmission power for 3215864_2 |
| C15 의미 | Adjust the azimuth of 3215864_2 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[891] topology](images/train_0891.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252891_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215864_2
- `C3`: Increase transmission power for 3215864_2 **← 정답**
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252891_3
- `C5`: Lift the tilt angle of 3215864_2 by 10 degrees
- `C6`: Increase A3 Offset threshold for 3215864_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215864_2
- `C9`: Press down the tilt angle of 3215864_2 by 10 degrees
- `C10`: Add neighbor relationship between 3215864_2 and 3252891_3
- `C11`: Decrease A3 Offset threshold for 3252891_3
- `C12`: Check test server and transmission issues
- `C13`: Adjust the azimuth of 3252891_3 by 23 degrees
- `C14`: Increase A3 Offset threshold for 3252891_3
- `C15`: Adjust the azimuth of 3215864_2 by 50 degrees **← 정답**
- `C16`: Decrease transmission power for 3215864_2
- `C17`: Increase transmission power for 3252891_3
- `C18`: Decrease transmission power for 3252891_3
- `C19`: Lift the tilt angle  of 3252891_3 by 5 degrees
- `C20`: Add neighbor relationship between 3256785_1 and 3252891_3
- `C21`: Decrease A3 Offset threshold for 3215864_2
- `C22`: Press down the tilt angle  of 3252891_3 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.625 | MS1 | 121.4656741408 | 31.1446202840 | 557 | 504990 | -88.64 | 15.50 | 336.55 | 0.14 | 2.98 | 1596 |
| 2024-09-20 22:21:32.564 | MS1 | 121.4656677289 | 31.1446353958 | 557 | 504990 | -85.29 | 13.01 | 572.83 | 0.01 | 2.57 | 1600 |
| 2024-09-20 22:21:33.205 | MS1 | 121.4656741361 | 31.1446244223 | 557 | 504990 | -90.96 | 17.48 | 508.51 | 0.05 | 2.57 | 1599 |
| 2024-09-20 22:21:34.285 | MS1 | 121.4656748410 | 31.1446304010 | 557 | 504990 | -102.02 | -1.94 | 60.41 | 0.06 | 1.48 | 1585 |
| 2024-09-20 22:21:35.637 | MS1 | 121.4656763372 | 31.1446212312 | 557 | 504990 | -103.81 | -1.98 | 53.98 | 0.05 | 1.23 | 1568 |
| 2024-09-20 22:21:36.765 | MS1 | 121.4656754957 | 31.1446233699 | 557 | 504990 | -101.84 | -1.49 | 23.46 | 0.13 | 1.16 | 1567 |
| 2024-09-20 22:21:37.830 | MS1 | 121.4656633341 | 31.1446361946 | 557 | 504990 | -103.92 | 0.74 | 22.79 | 0.13 | 1.30 | 1597 |
| 2024-09-20 22:21:38.394 | MS1 | 121.4656688437 | 31.1446327801 | 557 | 504990 | -108.28 | 1.52 | 46.90 | 0.17 | 1.19 | 1563 |
| 2024-09-20 22:21:39.468 | MS1 | 121.4656609731 | 31.1446259415 | 557 | 504990 | -106.47 | -0.51 | 35.27 | 0.12 | 1.20 | 1567 |
| 2024-09-20 22:21:40.296 | MS1 | 121.4656618759 | 31.1446314468 | 557 | 504990 | -92.45 | 12.81 | 442.15 | 0.14 | 2.55 | 1578 |
| 2024-09-20 22:21:41.330 | MS1 | 121.4656685540 | 31.1446333457 | 557 | 504990 | -89.89 | 15.94 | 477.11 | 0.11 | 2.42 | 1599 |
| 2024-09-20 22:21:42.895 | MS1 | 121.4656600147 | 31.1446298384 | 557 | 504990 | -86.22 | 17.89 | 393.57 | 0.16 | 2.31 | 1563 |

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
| 3215864 | 2 | 121.4665154761 | 31.1484566966 | 115 | 9 | 2 | 15.5 | TDD | 557 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3252891 | 3 | 121.4751054374 | 31.1505578609 | 211 | 3 | 11 | 38.3 | TDD | 742 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3256785 | 1 | 121.4718896160 | 31.1474699193 | 52 | 10 | 2 | 48.7 | TDD | 860 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3266883 | 4 | 121.4653584121 | 31.1527417357 | 72 | 14 | 7 | 19.2 | TDD | 165 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.318 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.338 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.441 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.441 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.680 | NREventA2 | measId:1;ServCellPCI:633;Se... |
| 2024-09-20 22:21:34.813 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256785 | 1 | 6.0591 | 16.8835 | -116.0692 | 12.5536 | 126.9553 | 0.0174 | 0.0046 |
| 2024_09_20 22:00 | 3215864 | 2 | 15.3611 | 10.8239 | -114.3120 | 14.5797 | 104.0991 | 0.1824 | 0.0160 |
| 2024_09_20 22:00 | 3252891 | 3 | 8.0591 | 15.4019 | -114.9335 | 5.5499 | 176.1456 | 0.0042 | 0.0112 |
| 2024_09_20 22:00 | 3266883 | 4 | 13.9600 | 16.6699 | -116.6554 | 13.3063 | 96.3937 | 0.0124 | 0.0172 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413671_CC2DFCC0 | 504990 | 557 | -100.4 | 504990 | 742 | -106.0 | 504990 | 860 | -112.5 | 504990 | 165 |
| MR_1774413671_8B90F8E3 | 504990 | 557 | -103.3 | 504990 | 742 | -106.9 | 504990 | 860 | -110.7 | 504990 | 165 |
| MR_1774413671_29DC5DFF | 504990 | 557 | -101.4 | 504990 | 742 | -108.1 | 504990 | 860 | -112.6 | 504990 | 165 |
| MR_1774413671_5D5E85B3 | 504990 | 557 | -102.5 | 504990 | 742 | -105.8 | 504990 | 860 | -112.2 | 504990 | 165 |
| MR_1774413671_8653C460 | 504990 | 557 | -100.7 | 504990 | 742 | -107.5 | 504990 | 860 | -110.9 | 504990 | 165 |
| MR_1774413671_A9AB590B | 504990 | 557 | -103.5 | 504990 | 742 | -107.6 | 504990 | 860 | -110.9 | 504990 | 165 |
| MR_1774413671_C845D920 | 504990 | 557 | -103.2 | 504990 | 742 | -107.5 | 504990 | 860 | -112.0 | 504990 | 165 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 892: `220e43a9-54c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `220e43a9-54cd-442a-b388-f06cb14236e7` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Decrease A3 Offset threshold for 3277604_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[892] topology](images/train_0892.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3277604_3
- `C2`: Add neighbor relationship between 3252873_2 and 3250886_1
- `C3`: Increase A3 Offset threshold for 3277604_3
- `C4`: Adjust the azimuth of 3250886_1 by 50 degrees
- `C5`: Decrease A3 Offset threshold for 3277604_3 **← 정답**
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277604_3
- `C7`: Add neighbor relationship between 3277604_3 and 3250886_1
- `C8`: Lift the tilt angle of 3277604_3 by 5 degrees
- `C9`: Decrease transmission power for 3250886_1
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Lift the tilt angle  of 3250886_1 by 10 degrees
- `C12`: Check test server and transmission issues
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250886_1
- `C14`: Press down the tilt angle  of 3250886_1 by 10 degrees
- `C15`: Increase transmission power for 3277604_3
- `C16`: Adjust the azimuth of 3277604_3 by 6 degrees
- `C17`: Decrease A3 Offset threshold for 3250886_1
- `C18`: Increase A3 Offset threshold for 3250886_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277604_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250886_1
- `C21`: Increase transmission power for 3250886_1
- `C22`: Press down the tilt angle of 3277604_3 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.550 | MS1 | 121.4656663934 | 31.1446236073 | 915 | 504990 | -80.22 | 16.79 | 381.94 | 0.08 | 2.32 | 1573 |
| 2024-09-20 22:21:32.238 | MS1 | 121.4656638857 | 31.1446183483 | 915 | 504990 | -83.55 | 17.50 | 480.76 | 0.15 | 2.15 | 1560 |
| 2024-09-20 22:21:33.320 | MS1 | 121.4656750720 | 31.1446355449 | 915 | 504990 | -75.47 | 17.38 | 451.63 | 0.13 | 2.25 | 1582 |
| 2024-09-20 22:21:34.828 | MS1 | 121.4656665797 | 31.1446324801 | 915 | 504990 | -88.98 | -1.12 | 55.55 | 0.04 | 1.20 | 1563 |
| 2024-09-20 22:21:35.876 | MS1 | 121.4656606000 | 31.1446233322 | 915 | 504990 | -84.58 | -2.14 | 40.76 | 0.02 | 1.33 | 1585 |
| 2024-09-20 22:21:36.952 | MS1 | 121.4656764348 | 31.1446375287 | 915 | 504990 | -84.40 | -3.73 | 43.11 | 0.19 | 1.08 | 1582 |
| 2024-09-20 22:21:37.994 | MS1 | 121.4656631320 | 31.1446260350 | 915 | 504990 | -86.26 | -3.03 | 56.35 | 0.17 | 1.28 | 1600 |
| 2024-09-20 22:21:38.232 | MS1 | 121.4656583331 | 31.1446288734 | 915 | 504990 | -92.92 | -1.61 | 57.15 | 0.03 | 1.29 | 1579 |
| 2024-09-20 22:21:39.640 | MS1 | 121.4656709362 | 31.1446324063 | 393 | 504990 | -77.94 | 13.92 | 277.59 | 0.16 | 1.50 | 1589 |
| 2024-09-20 22:21:40.536 | MS1 | 121.4656640083 | 31.1446201481 | 393 | 504990 | -83.09 | 12.37 | 511.03 | 0.06 | 2.06 | 1584 |
| 2024-09-20 22:21:41.135 | MS1 | 121.4656671678 | 31.1446316904 | 393 | 504990 | -84.83 | 15.49 | 536.25 | 0.10 | 2.72 | 1591 |
| 2024-09-20 22:21:42.531 | MS1 | 121.4656665249 | 31.1446342743 | 393 | 504990 | -78.70 | 17.18 | 526.97 | 0.13 | 2.90 | 1561 |

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
| 3217010 | 4 | 121.4658837442 | 31.1555874075 | 32 | 14 | 8 | 40.1 | TDD | 43 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3250886 | 1 | 121.4753479645 | 31.1480870736 | 121 | 15 | 6 | 32.9 | TDD | 393 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3252873 | 2 | 121.4669100542 | 31.1495366848 | 244 | 11 | 12 | 41.0 | TDD | 986 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3277604 | 3 | 121.4675888142 | 31.1513500087 | 188 | 4 | 6 | 17.0 | TDD | 915 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.617 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.641 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.743 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.743 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.487 | NREventA3 | measId:2;ServCellPCI:719;Se... |
| 2024-09-20 22:21:38.727 | NRHandoverAttempt | SourcePCI:719;SourceNR-ARFC... |
| 2024-09-20 22:21:38.760 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.772 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.918 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.918 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250886 | 1 | 18.8678 | 16.7676 | -115.8285 | 19.1353 | 98.9703 | 0.0014 | 0.0122 |
| 2024_09_20 22:00 | 3252873 | 2 | 7.6192 | 13.6393 | -117.1958 | 16.9873 | 142.2860 | 0.0013 | 0.0078 |
| 2024_09_20 22:00 | 3277604 | 3 | 15.2564 | 9.9653 | -117.8694 | 16.8810 | 100.1502 | 0.0062 | 0.1982 |
| 2024_09_20 22:00 | 3217010 | 4 | 14.5768 | 17.8154 | -115.9314 | 17.3398 | 126.3019 | 0.0048 | 0.0028 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417033_D431D685 | 504990 | 393 | -84.1 | 504990 | 915 | -90.4 | 504990 | 986 | -86.4 | 504990 | 43 |
| MR_1774417033_EF2C4885 | 504990 | 393 | -86.3 | 504990 | 915 | -87.5 | 504990 | 986 | -84.0 | 504990 | 43 |
| MR_1774417033_A1CF1717 | 504990 | 393 | -85.5 | 504990 | 915 | -87.6 | 504990 | 986 | -86.8 | 504990 | 43 |
| MR_1774417033_99816B00 | 504990 | 915 | -88.9 | 504990 | 393 | -84.3 | 504990 | 986 | -84.1 | 504990 | 43 |
| MR_1774417033_DCA6F671 | 504990 | 915 | -89.2 | 504990 | 393 | -86.3 | 504990 | 986 | -85.1 | 504990 | 43 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 893: `7a62f650-e7e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7a62f650-e7e8-48d6-a986-5de9baaec7cd` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Add neighbor relationship between 3246440_3 and 3275709_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[893] topology](images/train_0893.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275709_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275709_2
- `C3`: Lift the tilt angle of 3246440_3 by 10 degrees
- `C4`: Increase A3 Offset threshold for 3246440_3
- `C5`: Press down the tilt angle  of 3275709_2 by 2 degrees
- `C6`: Increase transmission power for 3246440_3
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Check test server and transmission issues
- `C9`: Increase A3 Offset threshold for 3275709_2
- `C10`: Decrease A3 Offset threshold for 3246440_3
- `C11`: Add neighbor relationship between 3246440_3 and 3275709_2 **← 정답**
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246440_3
- `C13`: Increase transmission power for 3275709_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246440_3
- `C15`: Adjust the azimuth of 3275709_2 by 49 degrees
- `C16`: Decrease transmission power for 3246440_3
- `C17`: Press down the tilt angle of 3246440_3 by 10 degrees
- `C18`: Decrease A3 Offset threshold for 3275709_2
- `C19`: Lift the tilt angle  of 3275709_2 by 2 degrees
- `C20`: Adjust the azimuth of 3246440_3 by 50 degrees
- `C21`: Add neighbor relationship between 3228484_1 and 3275709_2
- `C22`: Decrease transmission power for 3275709_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.836 | MS1 | 121.4656631533 | 31.1446258173 | 259 | 504990 | -84.68 | 16.69 | 379.26 | 0.05 | 2.61 | 1599 |
| 2024-09-20 22:21:32.571 | MS1 | 121.4656635237 | 31.1446355716 | 259 | 504990 | -77.98 | 14.45 | 460.03 | 0.06 | 2.16 | 1569 |
| 2024-09-20 22:21:33.878 | MS1 | 121.4656599339 | 31.1446216660 | 259 | 504990 | -80.95 | 16.91 | 325.92 | 0.14 | 2.59 | 1583 |
| 2024-09-20 22:21:34.739 | MS1 | 121.4656712439 | 31.1446355850 | 259 | 504990 | -91.22 | -2.41 | 54.88 | 0.13 | 1.04 | 1594 |
| 2024-09-20 22:21:35.452 | MS1 | 121.4656714723 | 31.1446269039 | 259 | 504990 | -87.16 | -2.33 | 63.61 | 0.03 | 1.31 | 1572 |
| 2024-09-20 22:21:36.227 | MS1 | 121.4656688983 | 31.1446352803 | 259 | 504990 | -92.09 | -0.25 | 38.31 | 0.05 | 1.25 | 1586 |
| 2024-09-20 22:21:37.435 | MS1 | 121.4656702330 | 31.1446360365 | 259 | 504990 | -88.53 | -0.56 | 58.68 | 0.05 | 1.37 | 1591 |
| 2024-09-20 22:21:38.400 | MS1 | 121.4656748530 | 31.1446275112 | 259 | 504990 | -83.92 | 12.22 | 392.19 | 0.05 | 1.12 | 1560 |
| 2024-09-20 22:21:39.467 | MS1 | 121.4656689708 | 31.1446219637 | 259 | 504990 | -79.59 | 12.55 | 515.83 | 0.15 | 1.19 | 1560 |
| 2024-09-20 22:21:40.461 | MS1 | 121.4656733301 | 31.1446365441 | 259 | 504990 | -83.32 | 12.42 | 343.38 | 0.08 | 2.80 | 1572 |
| 2024-09-20 22:21:41.907 | MS1 | 121.4656616825 | 31.1446283097 | 259 | 504990 | -77.53 | 12.35 | 318.72 | 0.20 | 2.56 | 1585 |
| 2024-09-20 22:21:42.483 | MS1 | 121.4656722543 | 31.1446350909 | 259 | 504990 | -81.82 | 13.42 | 344.16 | 0.09 | 2.54 | 1589 |

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
| 3228484 | 1 | 121.4698750017 | 31.1448765244 | 356 | 6 | 8 | 37.5 | TDD | 1 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3246440 | 3 | 121.4691870787 | 31.1448445381 | 66 | 13 | 8 | 21.6 | TDD | 259 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3275709 | 2 | 121.4643035770 | 31.1553699723 | 125 | 0 | 0 | 43.5 | TDD | 170 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3277053 | 4 | 121.4685128543 | 31.1492748256 | 182 | 3 | 0 | 34.1 | TDD | 478 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.590 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.606 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.730 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.730 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.473 | NREventA3 | measId:2;ServCellPCI:628;Se... |
| 2024-09-20 22:21:36.473 | NREventA3 | measId:2;ServCellPCI:628;Se... |
| 2024-09-20 22:21:37.473 | NREventA3 | measId:2;ServCellPCI:628;Se... |
| 2024-09-20 22:21:39.973 | NRRRCReestablishAttempt | PCI:628 |
| 2024-09-20 22:21:39.992 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:40.003 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:40.151 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.151 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228484 | 1 | 16.5136 | 15.2706 | -115.9593 | 18.3577 | 105.2940 | 0.0155 | 0.0177 |
| 2024_09_20 22:00 | 3275709 | 2 | 12.2118 | 11.0399 | -116.7344 | 6.8158 | 87.8191 | 0.0001 | 0.0011 |
| 2024_09_20 22:00 | 3246440 | 3 | 7.8612 | 6.3581 | -116.1677 | 15.4999 | 139.4394 | 0.0078 | 0.1262 |
| 2024_09_20 22:00 | 3277053 | 4 | 13.2310 | 11.1888 | -117.7002 | 9.3044 | 133.4004 | 0.0095 | 0.0032 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417076_C4C8E76A | 504990 | 259 | -90.6 | 504990 | 170 | -85.1 | 504990 | 1 | -88.6 | 504990 | 478 |
| MR_1774417076_7C9375EC | 504990 | 170 | -85.6 | 504990 | 259 | -92.1 | 504990 | 1 | -89.6 | 504990 | 478 |
| MR_1774417076_671EEEC1 | 504990 | 259 | -90.0 | 504990 | 170 | -85.3 | 504990 | 1 | -87.4 | 504990 | 478 |
| MR_1774417076_67424328 | 504990 | 170 | -85.7 | 504990 | 259 | -90.7 | 504990 | 1 | -89.2 | 504990 | 478 |
| MR_1774417076_5C886759 | 504990 | 170 | -85.5 | 504990 | 259 | -91.1 | 504990 | 1 | -88.3 | 504990 | 478 |
| MR_1774417076_C91C14BC | 504990 | 170 | -83.7 | 504990 | 259 | -89.7 | 504990 | 1 | -87.9 | 504990 | 478 |
| MR_1774417076_CF1FDED9 | 504990 | 170 | -83.6 | 504990 | 259 | -90.1 | 504990 | 1 | -89.5 | 504990 | 478 |
| MR_1774417076_3785BC02 | 504990 | 170 | -86.5 | 504990 | 259 | -90.8 | 504990 | 1 | -86.2 | 504990 | 478 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 894: `13c760ee-4d4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `13c760ee-4d40-4cf4-8d32-3c907c870376` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262601_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[894] topology](images/train_0894.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3248663_1 by 3 degrees
- `C2`: Check test server and transmission issues
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262601_2 **← 정답**
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248663_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262601_2
- `C7`: Increase A3 Offset threshold for 3248663_1
- `C8`: Press down the tilt angle of 3262601_2 by 5 degrees
- `C9`: Decrease A3 Offset threshold for 3248663_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248663_1
- `C11`: Press down the tilt angle  of 3248663_1 by 3 degrees
- `C12`: Adjust the azimuth of 3248663_1 by 12 degrees
- `C13`: Add neighbor relationship between 3214288_9 and 3248663_1
- `C14`: Decrease transmission power for 3262601_2
- `C15`: Increase transmission power for 3248663_1
- `C16`: Adjust the azimuth of 3262601_2 by 50 degrees
- `C17`: Lift the tilt angle of 3262601_2 by 5 degrees
- `C18`: Increase A3 Offset threshold for 3262601_2
- `C19`: Decrease transmission power for 3248663_1
- `C20`: Increase transmission power for 3262601_2
- `C21`: Add neighbor relationship between 3262601_2 and 3248663_1
- `C22`: Decrease A3 Offset threshold for 3262601_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.660 | MS1 | 121.4656617372 | 31.1446205426 | 293 | 504990 | -94.50 | 13.86 | 425.88 | 0.02 | 2.59 | 1597 |
| 2024-09-20 22:21:32.466 | MS1 | 121.4656582650 | 31.1446317013 | 143 | 504990 | -95.84 | 11.94 | 350.94 | 0.05 | 2.50 | 1562 |
| 2024-09-20 22:21:33.444 | MS1 | 121.4656776663 | 31.1446291573 | 136 | 504990 | -93.16 | 14.50 | 574.89 | 0.12 | 2.67 | 1566 |
| 2024-09-20 22:21:34.361 | MS1 | 121.4656715461 | 31.1446315369 | 495 | 152650 | -91.30 | 6.09 | 73.51 | 0.01 | 1.88 | 914 |
| 2024-09-20 22:21:35.334 | MS1 | 121.4656628980 | 31.1446240754 | 815 | 152650 | -96.53 | 5.53 | 86.75 | 0.16 | 1.97 | 934 |
| 2024-09-20 22:21:36.811 | MS1 | 121.4656644492 | 31.1446335553 | 560 | 152650 | -91.34 | 7.94 | 91.37 | 0.09 | 1.97 | 966 |
| 2024-09-20 22:21:37.362 | MS1 | 121.4656651948 | 31.1446295223 | 698 | 152650 | -92.10 | 7.48 | 81.88 | 0.06 | 1.69 | 966 |
| 2024-09-20 22:21:38.514 | MS1 | 121.4656674055 | 31.1446289666 | 495 | 152650 | -95.54 | 3.12 | 85.10 | 0.20 | 1.75 | 926 |
| 2024-09-20 22:21:39.976 | MS1 | 121.4656749998 | 31.1446206136 | 815 | 152650 | -93.25 | 3.06 | 86.35 | 0.07 | 1.78 | 953 |
| 2024-09-20 22:21:40.273 | MS1 | 121.4656691792 | 31.1446189275 | 560 | 152650 | -87.79 | 7.52 | 70.00 | 0.13 | 2.59 | 1582 |
| 2024-09-20 22:21:41.831 | MS1 | 121.4656634596 | 31.1446273326 | 698 | 152650 | -94.99 | 7.19 | 91.13 | 0.18 | 2.61 | 1581 |
| 2024-09-20 22:21:42.559 | MS1 | 121.4656713436 | 31.1446186216 | 495 | 152650 | -89.45 | 3.05 | 83.90 | 0.16 | 2.46 | 1573 |

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
| 3214288 | 9 | 121.4741297737 | 31.1446698462 | 107 | 3 | 10 | 17.2 | FDD | 560 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3218665 | 12 | 121.4702089910 | 31.1542152389 | 27 | 7 | 5 | 21.6 | FDD | 504 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3225509 | 5 | 121.4757732720 | 31.1455776020 | 231 | 5 | 0 | 13.9 | TDD | 821 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3225653 | 8 | 121.4660818152 | 31.1462936773 | 263 | 15 | 12 | 20.8 | FDD | 815 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3229641 | 7 | 121.4644052412 | 31.1559968881 | 96 | 0 | 7 | 1.7 | FDD | 34 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3240107 | 13 | 121.4668792818 | 31.1503900827 | 33 | 15 | 5 | 25.9 | FDD | 698 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3241135 | 11 | 121.4664983953 | 31.1558682952 | 225 | 9 | 12 | 20.3 | FDD | 214 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3245959 | 3 | 121.4728930967 | 31.1534609761 | 271 | 9 | 12 | 8.9 | TDD | 136 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3248663 | 1 | 121.4702597500 | 31.1442780319 | 287 | 1 | 8 | 13.8 | TDD | 451 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3249295 | 6 | 121.4683230259 | 31.1468982148 | 85 | 2 | 4 | 22.5 | TDD | 344 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3251558 | 4 | 121.4663152479 | 31.1447403956 | 353 | 5 | 5 | 5.7 | TDD | 143 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3259480 | 10 | 121.4727446781 | 31.1471503881 | 66 | 4 | 3 | 14.1 | FDD | 495 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3262601 | 2 | 121.4661512894 | 31.1495721453 | 135 | 3 | 4 | 18.4 | TDD | 293 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.010 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.027 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.162 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.162 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.868 | NREventA2 | measId:1;ServCellPCI:544;Se... |
| 2024-09-20 22:21:34.985 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.247 | NREventA5 | measId:3;ServCellPCI:544;Se... |
| 2024-09-20 22:21:35.283 | NRHandoverAttempt | SourcePCI:544;SourceNR-ARFC... |
| 2024-09-20 22:21:35.322 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.337 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.442 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.442 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248663 | 1 | 16.6115 | 16.1155 | -115.7065 | 14.8007 | 141.0638 | 0.0118 | 0.0146 |
| 2024_09_20 22:00 | 3262601 | 2 | 9.6087 | 9.9327 | -117.2188 | 14.9760 | 130.7456 | 0.0046 | 0.0125 |
| 2024_09_20 22:00 | 3245959 | 3 | 7.3441 | 9.0531 | -115.2603 | 12.3732 | 106.4224 | 0.0190 | 0.0034 |
| 2024_09_20 22:00 | 3251558 | 4 | 13.7510 | 15.6070 | -115.4090 | 11.0585 | 188.4991 | 0.0047 | 0.0150 |
| 2024_09_20 22:00 | 3225509 | 5 | 5.1850 | 12.0655 | -114.9863 | 19.6942 | 170.1841 | 0.0128 | 0.0063 |
| 2024_09_20 22:00 | 3249295 | 6 | 5.8200 | 10.4457 | -114.8889 | 6.9609 | 162.0688 | 0.0082 | 0.0197 |
| 2024_09_20 22:00 | 3229641 | 7 | 9.7670 | 12.7050 | -116.1399 | 3.4021 | 30.8730 | 0.0045 | 0.0002 |
| 2024_09_20 22:00 | 3225653 | 8 | 9.5824 | 6.2573 | -116.3590 | 3.5399 | 21.7257 | 0.0073 | 0.0108 |
| 2024_09_20 22:00 | 3214288 | 9 | 17.8480 | 14.0345 | -114.1491 | 4.4152 | 37.1911 | 0.0096 | 0.0060 |
| 2024_09_20 22:00 | 3259480 | 10 | 9.1904 | 11.6520 | -116.1201 | 3.8778 | 22.6560 | 0.0100 | 0.0028 |
| 2024_09_20 22:00 | 3241135 | 11 | 14.1187 | 9.5447 | -117.4594 | 3.6066 | 20.1260 | 0.0106 | 0.0174 |
| 2024_09_20 22:00 | 3218665 | 12 | 16.5562 | 9.7428 | -115.8336 | 4.2040 | 50.1124 | 0.0172 | 0.0146 |
| 2024_09_20 22:00 | 3240107 | 13 | 12.8049 | 17.3605 | -116.6841 | 4.0763 | 44.0609 | 0.0088 | 0.0140 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413846_187B7A2F | 152650 | 495 | -92.7 | 152650 | 34 | -99.1 | 152650 | 214 | -103.3 | 152650 | 504 |
| MR_1774413846_60354912 | 504990 | 136 | -91.3 | 504990 | 451 | -92.6 | 504990 | 821 | -94.2 | 504990 | 344 |
| MR_1774413846_2BB7CF4E | 152650 | 495 | -90.4 | 152650 | 34 | -99.0 | 152650 | 214 | -101.2 | 152650 | 504 |
| MR_1774413846_C1AAF752 | 504990 | 136 | -92.5 | 504990 | 451 | -93.4 | 504990 | 821 | -96.5 | 504990 | 344 |
| MR_1774413846_33AC027C | 152650 | 495 | -90.1 | 152650 | 34 | -97.5 | 152650 | 214 | -102.1 | 152650 | 504 |
| MR_1774413846_6191237E | 152650 | 495 | -92.9 | 152650 | 34 | -99.3 | 152650 | 214 | -102.5 | 152650 | 504 |
| MR_1774413846_DB155B35 | 504990 | 136 | -91.4 | 504990 | 451 | -92.4 | 504990 | 821 | -95.3 | 504990 | 344 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 895: `dc98be69-4ac...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dc98be69-4ace-4bd6-9402-cabde7e91bff` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Add neighbor relationship between 3242739_4 and 3252385_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[895] topology](images/train_0895.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3250642_3 and 3252385_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242739_4
- `C3`: Increase A3 Offset threshold for 3242739_4
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252385_1
- `C6`: Adjust the azimuth of 3242739_4 by 50 degrees
- `C7`: Decrease A3 Offset threshold for 3252385_1
- `C8`: Adjust the azimuth of 3252385_1 by 46 degrees
- `C9`: Press down the tilt angle of 3242739_4 by 10 degrees
- `C10`: Lift the tilt angle of 3242739_4 by 10 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242739_4
- `C12`: Add neighbor relationship between 3242739_4 and 3252385_1 **← 정답**
- `C13`: Press down the tilt angle  of 3252385_1 by 4 degrees
- `C14`: Increase transmission power for 3252385_1
- `C15`: Decrease transmission power for 3252385_1
- `C16`: Increase A3 Offset threshold for 3252385_1
- `C17`: Lift the tilt angle  of 3252385_1 by 4 degrees
- `C18`: Decrease A3 Offset threshold for 3242739_4
- `C19`: Decrease transmission power for 3242739_4
- `C20`: Check test server and transmission issues
- `C21`: Increase transmission power for 3242739_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252385_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.923 | MS1 | 121.4656621266 | 31.1446343013 | 615 | 504990 | -84.49 | 13.82 | 320.58 | 0.11 | 2.90 | 1577 |
| 2024-09-20 22:21:32.708 | MS1 | 121.4656614675 | 31.1446362712 | 615 | 504990 | -84.08 | 14.79 | 352.46 | 0.06 | 2.20 | 1561 |
| 2024-09-20 22:21:33.561 | MS1 | 121.4656683145 | 31.1446287424 | 615 | 504990 | -79.17 | 16.44 | 533.73 | 0.14 | 2.62 | 1561 |
| 2024-09-20 22:21:34.841 | MS1 | 121.4656769024 | 31.1446286500 | 615 | 504990 | -89.47 | -1.17 | 52.51 | 0.10 | 1.01 | 1574 |
| 2024-09-20 22:21:35.100 | MS1 | 121.4656738593 | 31.1446220130 | 615 | 504990 | -88.85 | -2.83 | 28.80 | 0.10 | 1.02 | 1586 |
| 2024-09-20 22:21:36.357 | MS1 | 121.4656770718 | 31.1446244341 | 615 | 504990 | -88.81 | -3.99 | 72.46 | 0.07 | 1.49 | 1581 |
| 2024-09-20 22:21:37.890 | MS1 | 121.4656779980 | 31.1446251336 | 615 | 504990 | -89.81 | -2.97 | 59.56 | 0.18 | 1.34 | 1588 |
| 2024-09-20 22:21:38.935 | MS1 | 121.4656594630 | 31.1446306615 | 615 | 504990 | -80.63 | 17.15 | 384.85 | 0.17 | 1.45 | 1594 |
| 2024-09-20 22:21:39.995 | MS1 | 121.4656632559 | 31.1446207056 | 615 | 504990 | -82.02 | 12.86 | 426.88 | 0.06 | 1.49 | 1560 |
| 2024-09-20 22:21:40.317 | MS1 | 121.4656627497 | 31.1446195927 | 615 | 504990 | -83.01 | 13.48 | 573.75 | 0.09 | 2.48 | 1568 |
| 2024-09-20 22:21:41.782 | MS1 | 121.4656712540 | 31.1446196916 | 615 | 504990 | -76.32 | 13.93 | 514.52 | 0.20 | 2.36 | 1571 |
| 2024-09-20 22:21:42.501 | MS1 | 121.4656740499 | 31.1446258754 | 615 | 504990 | -77.19 | 13.56 | 397.10 | 0.06 | 2.87 | 1570 |

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
| 3210008 | 2 | 121.4647621427 | 31.1532896412 | 325 | 12 | 11 | 41.6 | TDD | 490 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3242739 | 4 | 121.4653316329 | 31.1446430904 | 35 | 15 | 2 | 32.3 | TDD | 615 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3250642 | 3 | 121.4720374255 | 31.1530594473 | 268 | 1 | 1 | 19.2 | TDD | 292 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3252385 | 1 | 121.4746827876 | 31.1451762651 | 312 | 1 | 9 | 42.6 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.778 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.797 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.904 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.904 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.644 | NREventA3 | measId:2;ServCellPCI:517;Se... |
| 2024-09-20 22:21:35.644 | NREventA3 | measId:2;ServCellPCI:517;Se... |
| 2024-09-20 22:21:36.644 | NREventA3 | measId:2;ServCellPCI:517;Se... |
| 2024-09-20 22:21:39.144 | NRRRCReestablishAttempt | PCI:517 |
| 2024-09-20 22:21:39.164 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.174 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.322 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.322 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252385 | 1 | 18.6002 | 15.4255 | -117.3645 | 5.3218 | 123.8893 | 0.0083 | 0.0036 |
| 2024_09_20 22:00 | 3210008 | 2 | 17.5053 | 8.9536 | -116.0325 | 14.2283 | 147.0401 | 0.0158 | 0.0133 |
| 2024_09_20 22:00 | 3250642 | 3 | 12.8472 | 7.3954 | -114.6313 | 19.6173 | 196.1438 | 0.0100 | 0.0114 |
| 2024_09_20 22:00 | 3242739 | 4 | 17.1787 | 13.9633 | -117.2594 | 11.6440 | 87.2124 | 0.0111 | 0.1490 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412695_F39EA565 | 504990 | 866 | -86.0 | 504990 | 615 | -87.5 | 504990 | 292 | -92.6 | 504990 | 490 |
| MR_1774412695_04B15074 | 504990 | 866 | -85.4 | 504990 | 615 | -87.6 | 504990 | 292 | -91.9 | 504990 | 490 |
| MR_1774412695_3BA3E71B | 504990 | 866 | -83.5 | 504990 | 615 | -91.0 | 504990 | 292 | -91.7 | 504990 | 490 |
| MR_1774412695_6057C510 | 504990 | 615 | -89.6 | 504990 | 866 | -87.0 | 504990 | 292 | -94.5 | 504990 | 490 |
| MR_1774412695_A072FDAA | 504990 | 615 | -89.9 | 504990 | 866 | -86.2 | 504990 | 292 | -94.8 | 504990 | 490 |
| MR_1774412695_F9FC545F | 504990 | 615 | -90.6 | 504990 | 866 | -84.2 | 504990 | 292 | -93.1 | 504990 | 490 |
| MR_1774412695_1ACC96D8 | 504990 | 615 | -88.9 | 504990 | 866 | -83.5 | 504990 | 292 | -94.0 | 504990 | 490 |
| MR_1774412695_1FB6483C | 504990 | 615 | -89.7 | 504990 | 866 | -83.5 | 504990 | 292 | -95.4 | 504990 | 490 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 896: `a6135277-6e7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a6135277-6e7f-49b3-8aa2-b58471fafa08` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3257012_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[896] topology](images/train_0896.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3257012_3
- `C2`: Increase transmission power for 3239518_4
- `C3`: Add neighbor relationship between 3261216_1 and 3239518_4
- `C4`: Decrease A3 Offset threshold for 3257012_3
- `C5`: Lift the tilt angle of 3257012_3 by 2 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Press down the tilt angle  of 3239518_4 by 5 degrees
- `C8`: Press down the tilt angle of 3257012_3 by 2 degrees
- `C9`: Adjust the azimuth of 3257012_3 by 19 degrees
- `C10`: Lift the tilt angle  of 3239518_4 by 5 degrees
- `C11`: Increase transmission power for 3257012_3
- `C12`: Increase A3 Offset threshold for 3257012_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239518_4
- `C14`: Adjust the azimuth of 3239518_4 by 50 degrees
- `C15`: Check test server and transmission issues
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257012_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257012_3 **← 정답**
- `C18`: Increase A3 Offset threshold for 3239518_4
- `C19`: Add neighbor relationship between 3257012_3 and 3239518_4
- `C20`: Decrease A3 Offset threshold for 3239518_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239518_4
- `C22`: Decrease transmission power for 3239518_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.319 | MS1 | 121.4656778861 | 31.1446195543 | 178 | 504990 | -86.63 | 14.48 | 470.48 | 0.16 | 2.50 | 1581 |
| 2024-09-20 22:21:32.894 | MS1 | 121.4656601354 | 31.1446321156 | 178 | 504990 | -89.31 | 16.79 | 364.87 | 0.07 | 2.89 | 1563 |
| 2024-09-20 22:21:33.293 | MS1 | 121.4656670224 | 31.1446213243 | 178 | 504990 | -85.23 | 17.72 | 340.41 | 0.11 | 2.46 | 1582 |
| 2024-09-20 22:21:34.793 | MS1 | 121.4656587851 | 31.1446368294 | 178 | 504990 | -85.37 | 16.80 | 59.67 | 0.62 | 2.07 | 515 |
| 2024-09-20 22:21:35.731 | MS1 | 121.4656763741 | 31.1446187632 | 178 | 504990 | -88.20 | 16.54 | 70.66 | 0.64 | 2.61 | 513 |
| 2024-09-20 22:21:36.246 | MS1 | 121.4656586963 | 31.1446322939 | 178 | 504990 | -88.39 | 12.90 | 68.33 | 0.68 | 2.28 | 593 |
| 2024-09-20 22:21:37.685 | MS1 | 121.4656765134 | 31.1446285172 | 178 | 504990 | -93.23 | 7.56 | 79.69 | 0.52 | 2.89 | 646 |
| 2024-09-20 22:21:38.116 | MS1 | 121.4656736409 | 31.1446270393 | 178 | 504990 | -89.04 | 8.71 | 59.61 | 0.55 | 2.70 | 611 |
| 2024-09-20 22:21:39.863 | MS1 | 121.4656672030 | 31.1446241060 | 178 | 504990 | -89.83 | 10.02 | 95.13 | 0.60 | 2.41 | 519 |
| 2024-09-20 22:21:40.793 | MS1 | 121.4656609361 | 31.1446315429 | 178 | 504990 | -92.64 | 12.85 | 307.92 | 0.04 | 2.52 | 1595 |
| 2024-09-20 22:21:41.662 | MS1 | 121.4656616225 | 31.1446225882 | 178 | 504990 | -93.57 | 8.55 | 590.91 | 0.02 | 2.31 | 1590 |
| 2024-09-20 22:21:42.743 | MS1 | 121.4656694182 | 31.1446182566 | 178 | 504990 | -89.59 | 9.02 | 519.99 | 0.02 | 2.63 | 1567 |

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
| 3239518 | 4 | 121.4641862968 | 31.1496346860 | 296 | 2 | 1 | 29.7 | TDD | 595 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3257012 | 3 | 121.4734812296 | 31.1519656035 | 203 | 0 | 8 | 32.8 | TDD | 178 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3261216 | 1 | 121.4752563245 | 31.1559361447 | 261 | 14 | 5 | 28.1 | TDD | 448 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3271134 | 2 | 121.4670391565 | 31.1492508159 | 90 | 7 | 2 | 37.5 | TDD | 721 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.237 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.254 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.355 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.355 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.038 | NREventA3 | measId:2;ServCellPCI:985;Se... |
| 2024-09-20 22:21:38.278 | NRHandoverAttempt | SourcePCI:985;SourceNR-ARFC... |
| 2024-09-20 22:21:38.325 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.336 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.471 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.471 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261216 | 1 | 10.4733 | 6.7231 | -114.0006 | 19.7987 | 104.0631 | 0.0095 | 0.0072 |
| 2024_09_20 22:00 | 3271134 | 2 | 10.0167 | 17.1793 | -114.1678 | 8.9132 | 181.9854 | 0.0074 | 0.0084 |
| 2024_09_20 22:00 | 3257012 | 3 | 17.5760 | 8.1576 | -116.0987 | 10.4041 | 95.0079 | 0.0007 | 0.0140 |
| 2024_09_20 22:00 | 3239518 | 4 | 13.6975 | 11.5609 | -117.4850 | 5.8435 | 147.5438 | 0.0126 | 0.0107 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413846_07C6E5B9 | 504990 | 178 | -85.0 | 504990 | 595 | -93.3 | 504990 | 448 | -94.8 | 504990 | 721 |
| MR_1774413846_2897675F | 504990 | 178 | -87.3 | 504990 | 595 | -93.4 | 504990 | 448 | -95.4 | 504990 | 721 |
| MR_1774413846_F5ED3D3B | 504990 | 178 | -86.1 | 504990 | 595 | -92.0 | 504990 | 448 | -92.8 | 504990 | 721 |
| MR_1774413846_3CB19765 | 504990 | 178 | -84.8 | 504990 | 595 | -91.0 | 504990 | 448 | -94.6 | 504990 | 721 |
| MR_1774413846_29FFB5CD | 504990 | 178 | -85.2 | 504990 | 595 | -94.2 | 504990 | 448 | -92.7 | 504990 | 721 |
| MR_1774413846_0AD5B592 | 504990 | 178 | -84.4 | 504990 | 595 | -92.0 | 504990 | 448 | -95.4 | 504990 | 721 |
| MR_1774413846_00CD3D58 | 504990 | 178 | -85.0 | 504990 | 595 | -92.9 | 504990 | 448 | -95.3 | 504990 | 721 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 897: `ff87d90f-f00...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ff87d90f-f00d-4f3d-aca6-d921516a2c37` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240095_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[897] topology](images/train_0897.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3228542_6 by 41 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228542_6
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240095_2 **← 정답**
- `C4`: Press down the tilt angle  of 3228542_6 by 5 degrees
- `C5`: Press down the tilt angle of 3240095_2 by 1 degrees
- `C6`: Decrease A3 Offset threshold for 3240095_2
- `C7`: Check test server and transmission issues
- `C8`: Adjust the azimuth of 3240095_2 by 42 degrees
- `C9`: Lift the tilt angle of 3240095_2 by 1 degrees
- `C10`: Add neighbor relationship between 3240095_2 and 3228542_6
- `C11`: Add neighbor relationship between 3257194_10 and 3228542_6
- `C12`: Increase transmission power for 3240095_2
- `C13`: Increase transmission power for 3228542_6
- `C14`: Lift the tilt angle  of 3228542_6 by 5 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Increase A3 Offset threshold for 3240095_2
- `C17`: Increase A3 Offset threshold for 3228542_6
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240095_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228542_6
- `C20`: Decrease transmission power for 3228542_6
- `C21`: Decrease transmission power for 3240095_2
- `C22`: Decrease A3 Offset threshold for 3228542_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.705 | MS1 | 121.4656602784 | 31.1446335270 | 428 | 504990 | -93.12 | 14.38 | 552.64 | 0.11 | 2.70 | 1576 |
| 2024-09-20 22:21:32.273 | MS1 | 121.4656777545 | 31.1446190813 | 310 | 504990 | -93.44 | 11.40 | 388.04 | 0.07 | 2.78 | 1580 |
| 2024-09-20 22:21:33.141 | MS1 | 121.4656716234 | 31.1446272952 | 53 | 504990 | -94.00 | 13.56 | 325.68 | 0.05 | 2.35 | 1571 |
| 2024-09-20 22:21:34.326 | MS1 | 121.4656623332 | 31.1446276575 | 155 | 152650 | -90.93 | 3.60 | 51.00 | 0.06 | 1.68 | 994 |
| 2024-09-20 22:21:35.219 | MS1 | 121.4656616115 | 31.1446215878 | 276 | 152650 | -94.87 | 7.04 | 101.05 | 0.15 | 1.54 | 937 |
| 2024-09-20 22:21:36.494 | MS1 | 121.4656618907 | 31.1446244008 | 312 | 152650 | -88.76 | 2.59 | 97.83 | 0.17 | 1.69 | 927 |
| 2024-09-20 22:21:37.902 | MS1 | 121.4656646965 | 31.1446303527 | 26 | 152650 | -93.94 | 6.80 | 60.98 | 0.17 | 1.61 | 914 |
| 2024-09-20 22:21:38.435 | MS1 | 121.4656704298 | 31.1446311846 | 155 | 152650 | -94.91 | 7.59 | 84.64 | 0.12 | 1.68 | 927 |
| 2024-09-20 22:21:39.517 | MS1 | 121.4656729644 | 31.1446281889 | 276 | 152650 | -91.30 | 5.68 | 73.29 | 0.10 | 1.59 | 991 |
| 2024-09-20 22:21:40.441 | MS1 | 121.4656762019 | 31.1446274887 | 312 | 152650 | -87.64 | 6.05 | 79.83 | 0.12 | 2.29 | 1599 |
| 2024-09-20 22:21:41.133 | MS1 | 121.4656772356 | 31.1446248323 | 26 | 152650 | -93.02 | 5.05 | 44.56 | 0.17 | 2.39 | 1562 |
| 2024-09-20 22:21:42.917 | MS1 | 121.4656754870 | 31.1446257170 | 155 | 152650 | -87.86 | 4.07 | 50.94 | 0.16 | 2.64 | 1575 |

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
| 3213781 | 12 | 121.4672911836 | 31.1530543638 | 277 | 8 | 5 | 25.3 | FDD | 155 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3214501 | 3 | 121.4741339401 | 31.1502026080 | 326 | 13 | 4 | 5.2 | TDD | 53 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3228542 | 6 | 121.4720999955 | 31.1508267814 | 263 | 3 | 10 | 26.8 | TDD | 639 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3240095 | 2 | 121.4681567879 | 31.1452632927 | 211 | 1 | 10 | 1.5 | TDD | 428 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3240857 | 13 | 121.4702543272 | 31.1479407346 | 57 | 8 | 2 | 6.3 | FDD | 92 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3241122 | 11 | 121.4671740756 | 31.1514028104 | 317 | 3 | 7 | 24.9 | FDD | 26 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3248546 | 8 | 121.4643581850 | 31.1498244974 | 287 | 14 | 12 | 13.9 | FDD | 276 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3252397 | 4 | 121.4748091071 | 31.1442931634 | 110 | 7 | 1 | 28.5 | TDD | 310 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3257194 | 10 | 121.4744832666 | 31.1552854075 | 224 | 6 | 8 | 7.0 | FDD | 312 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3258473 | 9 | 121.4689167189 | 31.1493971931 | 330 | 5 | 4 | 26.9 | FDD | 757 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3263014 | 5 | 121.4742015874 | 31.1490303600 | 90 | 3 | 1 | 12.7 | TDD | 637 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3268876 | 7 | 121.4737668844 | 31.1493276517 | 23 | 10 | 11 | 18.8 | FDD | 722 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3269962 | 1 | 121.4643787041 | 31.1476029223 | 125 | 5 | 5 | 7.9 | TDD | 136 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.234 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.257 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.384 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.384 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.068 | NREventA2 | measId:1;ServCellPCI:729;Se... |
| 2024-09-20 22:21:35.188 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.436 | NREventA5 | measId:3;ServCellPCI:729;Se... |
| 2024-09-20 22:21:35.486 | NRHandoverAttempt | SourcePCI:729;SourceNR-ARFC... |
| 2024-09-20 22:21:35.528 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.540 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.644 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.644 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269962 | 1 | 19.8664 | 6.7821 | -116.0617 | 7.4730 | 170.0665 | 0.0005 | 0.0034 |
| 2024_09_20 22:00 | 3240095 | 2 | 19.0343 | 14.8732 | -116.2067 | 10.2505 | 110.7666 | 0.0002 | 0.0070 |
| 2024_09_20 22:00 | 3214501 | 3 | 18.8272 | 7.5184 | -115.9846 | 17.4129 | 141.0657 | 0.0105 | 0.0049 |
| 2024_09_20 22:00 | 3252397 | 4 | 15.2536 | 17.3165 | -114.8616 | 14.6386 | 176.2947 | 0.0178 | 0.0100 |
| 2024_09_20 22:00 | 3263014 | 5 | 12.6762 | 17.6986 | -115.2212 | 7.9793 | 178.1726 | 0.0114 | 0.0113 |
| 2024_09_20 22:00 | 3228542 | 6 | 6.5624 | 13.2268 | -115.6068 | 6.1909 | 92.8908 | 0.0139 | 0.0075 |
| 2024_09_20 22:00 | 3268876 | 7 | 15.4940 | 10.9530 | -116.3942 | 4.9887 | 23.2771 | 0.0116 | 0.0139 |
| 2024_09_20 22:00 | 3248546 | 8 | 12.4908 | 12.0206 | -117.1853 | 3.0612 | 21.3115 | 0.0086 | 0.0079 |
| 2024_09_20 22:00 | 3258473 | 9 | 13.9288 | 15.8524 | -116.5697 | 3.1989 | 42.3723 | 0.0195 | 0.0059 |
| 2024_09_20 22:00 | 3257194 | 10 | 15.1073 | 17.5314 | -114.3473 | 3.5625 | 39.5448 | 0.0111 | 0.0099 |
| 2024_09_20 22:00 | 3241122 | 11 | 7.0455 | 11.1835 | -114.2200 | 3.3999 | 43.5124 | 0.0018 | 0.0186 |
| 2024_09_20 22:00 | 3213781 | 12 | 6.2347 | 15.8695 | -115.5871 | 4.3106 | 22.3296 | 0.0139 | 0.0026 |
| 2024_09_20 22:00 | 3240857 | 13 | 9.5535 | 8.9082 | -116.8283 | 3.0303 | 37.1264 | 0.0101 | 0.0135 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416178_37C0215A | 504990 | 53 | -94.9 | 504990 | 639 | -100.5 | 504990 | 136 | -100.7 | 504990 | 637 |
| MR_1774416178_A3DDAE05 | 152650 | 155 | -90.6 | 152650 | 92 | -93.3 | 152650 | 722 | -103.3 | 152650 | 757 |
| MR_1774416178_92967DC0 | 152650 | 155 | -91.6 | 152650 | 92 | -93.7 | 152650 | 722 | -103.3 | 152650 | 757 |
| MR_1774416178_381726D4 | 504990 | 53 | -94.5 | 504990 | 639 | -97.0 | 504990 | 136 | -99.6 | 504990 | 637 |
| MR_1774416178_790E861C | 152650 | 155 | -92.1 | 152650 | 92 | -92.9 | 152650 | 722 | -102.2 | 152650 | 757 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 898: `9ebb53e6-1e5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9ebb53e6-1e57-4bcb-b596-2f2f738a30bc` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[898] topology](images/train_0898.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3245847_3 by 10 degrees
- `C2`: Add neighbor relationship between 3266054_1 and 3245847_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245847_3
- `C4`: Decrease transmission power for 3245847_3
- `C5`: Decrease transmission power for 3266054_1
- `C6`: Increase A3 Offset threshold for 3245847_3
- `C7`: Lift the tilt angle of 3266054_1 by 10 degrees
- `C8`: Adjust the azimuth of 3245847_3 by 50 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245847_3
- `C10`: Increase A3 Offset threshold for 3266054_1
- `C11`: Press down the tilt angle of 3266054_1 by 10 degrees
- `C12`: Adjust the azimuth of 3266054_1 by 50 degrees
- `C13`: Decrease A3 Offset threshold for 3245847_3
- `C14`: Add neighbor relationship between 3234813_4 and 3245847_3
- `C15`: Increase transmission power for 3245847_3
- `C16`: Lift the tilt angle  of 3245847_3 by 10 degrees
- `C17`: Decrease A3 Offset threshold for 3266054_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Increase transmission power for 3266054_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266054_1
- `C21`: Check test server and transmission issues **← 정답**
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266054_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.530 | MS1 | 121.4656593776 | 31.1446377437 | 928 | 504990 | -88.86 | 14.55 | 345.28 | 0.19 | 2.28 | 1579 |
| 2024-09-20 22:21:32.544 | MS1 | 121.4656636984 | 31.1446374728 | 928 | 504990 | -85.08 | 17.96 | 539.96 | 0.19 | 2.36 | 1574 |
| 2024-09-20 22:21:33.980 | MS1 | 121.4656739951 | 31.1446368680 | 928 | 504990 | -87.84 | 15.16 | 319.40 | 0.07 | 2.15 | 1575 |
| 2024-09-20 22:21:34.910 | MS1 | 121.4656715509 | 31.1446316534 | 928 | 504990 | -91.94 | 15.66 | 99.76 | 0.07 | 2.52 | 449 |
| 2024-09-20 22:21:35.870 | MS1 | 121.4656670952 | 31.1446351145 | 928 | 504990 | -86.07 | 17.54 | 46.22 | 0.13 | 2.69 | 457 |
| 2024-09-20 22:21:36.555 | MS1 | 121.4656669301 | 31.1446198938 | 928 | 504990 | -91.23 | 16.96 | 88.76 | 0.15 | 2.56 | 322 |
| 2024-09-20 22:21:37.864 | MS1 | 121.4656710447 | 31.1446189460 | 928 | 504990 | -93.12 | 7.45 | 80.74 | 0.19 | 2.10 | 354 |
| 2024-09-20 22:21:38.690 | MS1 | 121.4656755449 | 31.1446365253 | 928 | 504990 | -92.93 | 11.61 | 83.82 | 0.05 | 2.33 | 448 |
| 2024-09-20 22:21:39.538 | MS1 | 121.4656674966 | 31.1446205554 | 928 | 504990 | -90.30 | 9.74 | 75.49 | 0.02 | 2.36 | 414 |
| 2024-09-20 22:21:40.491 | MS1 | 121.4656643248 | 31.1446356379 | 928 | 504990 | -92.79 | 11.12 | 401.26 | 0.07 | 2.02 | 1574 |
| 2024-09-20 22:21:41.643 | MS1 | 121.4656634429 | 31.1446262924 | 928 | 504990 | -91.28 | 11.84 | 449.12 | 0.04 | 2.10 | 1588 |
| 2024-09-20 22:21:42.770 | MS1 | 121.4656758888 | 31.1446336885 | 928 | 504990 | -90.08 | 9.29 | 449.50 | 0.08 | 2.94 | 1562 |

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
| 3231886 | 2 | 121.4715651677 | 31.1510851620 | 156 | 13 | 2 | 38.7 | TDD | 436 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3234813 | 4 | 121.4684443697 | 31.1502751317 | 354 | 9 | 1 | 26.3 | TDD | 356 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3245847 | 3 | 121.4739427498 | 31.1449137571 | 205 | 15 | 9 | 32.5 | TDD | 724 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3266054 | 1 | 121.4703584998 | 31.1467864058 | 341 | 7 | 2 | 41.3 | TDD | 928 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.064 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.089 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.198 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.198 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.910 | NREventA3 | measId:2;ServCellPCI:870;Se... |
| 2024-09-20 22:21:38.150 | NRHandoverAttempt | SourcePCI:870;SourceNR-ARFC... |
| 2024-09-20 22:21:38.184 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.194 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.338 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.338 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266054 | 1 | 8.2136 | 15.8419 | -116.7713 | 6.7108 | 86.2052 | 0.0170 | 0.0143 |
| 2024_09_20 22:00 | 3231886 | 2 | 7.1747 | 11.2846 | -117.1594 | 6.8640 | 125.7150 | 0.0070 | 0.0028 |
| 2024_09_20 22:00 | 3245847 | 3 | 17.9479 | 5.8209 | -116.0208 | 7.0285 | 127.3835 | 0.0188 | 0.0094 |
| 2024_09_20 22:00 | 3234813 | 4 | 19.1049 | 7.8635 | -115.1431 | 8.3539 | 162.4243 | 0.0062 | 0.0154 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413487_C52D8CE7 | 504990 | 928 | -93.5 | 504990 | 724 | -101.5 | 504990 | 356 | -102.7 | 504990 | 436 |
| MR_1774413487_BA3510B3 | 504990 | 928 | -91.5 | 504990 | 724 | -97.9 | 504990 | 356 | -102.6 | 504990 | 436 |
| MR_1774413487_BD0CDDA5 | 504990 | 928 | -91.0 | 504990 | 724 | -101.2 | 504990 | 356 | -104.7 | 504990 | 436 |
| MR_1774413487_805822A6 | 504990 | 928 | -92.2 | 504990 | 724 | -98.9 | 504990 | 356 | -103.3 | 504990 | 436 |
| MR_1774413487_EAAA1FC9 | 504990 | 928 | -93.5 | 504990 | 724 | -99.7 | 504990 | 356 | -105.0 | 504990 | 436 |
| MR_1774413487_833FF2E0 | 504990 | 928 | -92.7 | 504990 | 724 | -98.5 | 504990 | 356 | -103.7 | 504990 | 436 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 899: `697d8783-60f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `697d8783-60fd-46e2-8f43-be82d932f234` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[899] topology](images/train_0899.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3238993_3
- `C2`: Press down the tilt angle of 3275062_4 by 10 degrees
- `C3`: Decrease transmission power for 3238993_3
- `C4`: Add neighbor relationship between 3275062_4 and 3238993_3
- `C5`: Press down the tilt angle  of 3238993_3 by 8 degrees
- `C6`: Decrease A3 Offset threshold for 3275062_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238993_3
- `C8`: Check test server and transmission issues
- `C9`: Lift the tilt angle of 3275062_4 by 10 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275062_4
- `C11`: Decrease transmission power for 3275062_4
- `C12`: Decrease A3 Offset threshold for 3238993_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275062_4
- `C14`: Lift the tilt angle  of 3238993_3 by 8 degrees
- `C15`: Insufficient data; more data is needed for judgment. **← 정답**
- `C16`: Increase transmission power for 3275062_4
- `C17`: Adjust the azimuth of 3238993_3 by 50 degrees
- `C18`: Increase A3 Offset threshold for 3275062_4
- `C19`: Increase A3 Offset threshold for 3238993_3
- `C20`: Add neighbor relationship between 3249911_1 and 3238993_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238993_3
- `C22`: Adjust the azimuth of 3275062_4 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.520 | MS1 | 121.4656718787 | 31.1446206889 | 44 | 504990 | -85.94 | 13.95 | 416.31 | 0.12 | 2.46 | 1588 |
| 2024-09-20 22:21:32.836 | MS1 | 121.4656722038 | 31.1446201474 | 44 | 504990 | -87.38 | 15.05 | 579.21 | 0.10 | 2.83 | 1581 |
| 2024-09-20 22:21:33.364 | MS1 | 121.4656597174 | 31.1446327217 | 44 | 504990 | -90.66 | 13.99 | 470.86 | 0.07 | 2.17 | 1589 |
| 2024-09-20 22:21:34.146 | MS1 | 121.4656666354 | 31.1446289974 | 44 | 504990 | -86.01 | 14.69 | 84.07 | 0.19 | 2.70 | 1590 |
| 2024-09-20 22:21:35.814 | MS1 | 121.4656647834 | 31.1446228923 | 44 | 504990 | -89.38 | 13.56 | 63.05 | 0.11 | 2.37 | 1572 |
| 2024-09-20 22:21:36.592 | MS1 | 121.4656709935 | 31.1446187632 | 44 | 504990 | -88.70 | 15.85 | 46.37 | 0.05 | 2.34 | 1565 |
| 2024-09-20 22:21:37.634 | MS1 | 121.4656666351 | 31.1446217533 | 44 | 504990 | -91.39 | 9.74 | 63.02 | 0.06 | 2.02 | 1598 |
| 2024-09-20 22:21:38.539 | MS1 | 121.4656599351 | 31.1446371067 | 44 | 504990 | -91.82 | 8.40 | 55.14 | 0.14 | 2.11 | 1570 |
| 2024-09-20 22:21:39.922 | MS1 | 121.4656626354 | 31.1446309004 | 44 | 504990 | -92.41 | 10.98 | 89.08 | 0.02 | 2.79 | 1585 |
| 2024-09-20 22:21:40.583 | MS1 | 121.4656612435 | 31.1446270126 | 44 | 504990 | -90.17 | 12.39 | 533.55 | 0.02 | 2.09 | 1567 |
| 2024-09-20 22:21:41.340 | MS1 | 121.4656750687 | 31.1446258773 | 44 | 504990 | -90.41 | 7.12 | 473.69 | 0.05 | 2.67 | 1578 |
| 2024-09-20 22:21:42.615 | MS1 | 121.4656612286 | 31.1446222356 | 44 | 504990 | -89.72 | 7.47 | 401.59 | 0.09 | 2.93 | 1580 |

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
| 3238993 | 3 | 121.4746936681 | 31.1550031286 | 40 | 7 | 11 | 35.0 | TDD | 802 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3246647 | 2 | 121.4667633730 | 31.1523290400 | 107 | 2 | 10 | 23.6 | TDD | 220 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3249911 | 1 | 121.4672403881 | 31.1462739581 | 15 | 9 | 0 | 43.1 | TDD | 970 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3275062 | 4 | 121.4736163328 | 31.1492651956 | 114 | 15 | 1 | 30.3 | TDD | 44 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.233 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.256 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.392 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.392 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.072 | NREventA3 | measId:2;ServCellPCI:604;Se... |
| 2024-09-20 22:21:38.312 | NRHandoverAttempt | SourcePCI:604;SourceNR-ARFC... |
| 2024-09-20 22:21:38.352 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.365 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.501 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.501 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3249911 | 1 | 82.9836 | 81.9425 | -115.6799 | 17.1803 | 177.1003 | 0.0022 | 0.0104 |
| 2024_09_19 22:00 | 3246647 | 2 | 80.0802 | 84.1933 | -117.1872 | 12.4835 | 178.9942 | 0.0189 | 0.0154 |
| 2024_09_19 22:00 | 3238993 | 3 | 87.2309 | 84.3860 | -116.8448 | 14.4312 | 123.1758 | 0.0149 | 0.0097 |
| 2024_09_19 22:00 | 3275062 | 4 | 76.7166 | 82.5219 | -115.5623 | 11.9209 | 110.0127 | 0.0110 | 0.0072 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416625_67C041B1 | 504990 | 44 | -84.6 | 504990 | 802 | -94.3 | 504990 | 970 | -98.8 | 504990 | 220 |
| MR_1774416625_3179E273 | 504990 | 44 | -85.5 | 504990 | 802 | -96.5 | 504990 | 970 | -99.4 | 504990 | 220 |
| MR_1774416625_FACA7BCA | 504990 | 44 | -86.7 | 504990 | 802 | -93.7 | 504990 | 970 | -97.1 | 504990 | 220 |
| MR_1774416625_9799AE5D | 504990 | 44 | -87.4 | 504990 | 802 | -94.3 | 504990 | 970 | -100.1 | 504990 | 220 |
| MR_1774416625_3DB8FE13 | 504990 | 44 | -84.1 | 504990 | 802 | -96.0 | 504990 | 970 | -98.6 | 504990 | 220 |

> *... 2개 열 생략 (전체 14열)*

---
