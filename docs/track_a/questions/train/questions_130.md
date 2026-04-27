# Track A 문제 분석 — train[1290]~train[1299]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1290] ~ train[1299] (10개)

## 목차

1. [문제 1290: `55781c47-35c...`](#1290) — single-answer, 정답: C19
2. [문제 1291: `9715ff06-b04...`](#1291) — single-answer, 정답: C18
3. [문제 1292: `607c6d1d-e66...`](#1292) — single-answer, 정답: C9
4. [문제 1293: `a861e6a7-53f...`](#1293) — single-answer, 정답: C10
5. [문제 1294: `3f619aca-c1e...`](#1294) — single-answer, 정답: C16
6. [문제 1295: `5bab95fb-d92...`](#1295) — multiple-answer, 정답: C6|C10|C11|C17
7. [문제 1296: `737d86f4-49a...`](#1296) — single-answer, 정답: C6
8. [문제 1297: `4ee02f20-f89...`](#1297) — multiple-answer, 정답: C1|C12
9. [문제 1298: `69b27230-efd...`](#1298) — single-answer, 정답: C4
10. [문제 1299: `3bc58231-24c...`](#1299) — single-answer, 정답: C1

---

### 문제 1290: `55781c47-35c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `55781c47-35ca-4763-8e7e-d5d11e9a7fac` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230102_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1290] topology](images/train_1290.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3216901_4
- `C2`: Increase A3 Offset threshold for 3230102_5
- `C3`: Increase A3 Offset threshold for 3216901_4
- `C4`: Add neighbor relationship between 3249019_7 and 3216901_4
- `C5`: Add neighbor relationship between 3230102_5 and 3216901_4
- `C6`: Lift the tilt angle of 3230102_5 by 4 degrees
- `C7`: Decrease A3 Offset threshold for 3230102_5
- `C8`: Decrease transmission power for 3230102_5
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216901_4
- `C11`: Decrease transmission power for 3216901_4
- `C12`: Increase transmission power for 3230102_5
- `C13`: Adjust the azimuth of 3230102_5 by 34 degrees
- `C14`: Decrease A3 Offset threshold for 3216901_4
- `C15`: Press down the tilt angle  of 3216901_4 by 1 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230102_5
- `C17`: Lift the tilt angle  of 3216901_4 by 1 degrees
- `C18`: Adjust the azimuth of 3216901_4 by 19 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230102_5 **← 정답**
- `C20`: Check test server and transmission issues
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216901_4
- `C22`: Press down the tilt angle of 3230102_5 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.926 | MS1 | 121.4656618902 | 31.1446215146 | 760 | 504990 | -93.09 | 9.77 | 491.95 | 0.17 | 2.92 | 1568 |
| 2024-09-20 22:21:32.816 | MS1 | 121.4656650098 | 31.1446307080 | 939 | 504990 | -93.63 | 11.69 | 444.59 | 0.10 | 2.96 | 1581 |
| 2024-09-20 22:21:33.367 | MS1 | 121.4656680637 | 31.1446214448 | 123 | 504990 | -94.15 | 13.71 | 327.94 | 0.17 | 2.26 | 1591 |
| 2024-09-20 22:21:34.668 | MS1 | 121.4656635443 | 31.1446349233 | 489 | 152650 | -88.06 | 2.33 | 56.82 | 0.01 | 1.85 | 941 |
| 2024-09-20 22:21:35.530 | MS1 | 121.4656598540 | 31.1446291961 | 247 | 152650 | -94.87 | 5.19 | 89.06 | 0.13 | 1.62 | 972 |
| 2024-09-20 22:21:36.426 | MS1 | 121.4656682280 | 31.1446341510 | 167 | 152650 | -95.19 | 5.95 | 88.61 | 0.04 | 1.88 | 942 |
| 2024-09-20 22:21:37.440 | MS1 | 121.4656772038 | 31.1446365474 | 857 | 152650 | -87.24 | 6.39 | 74.83 | 0.19 | 1.51 | 944 |
| 2024-09-20 22:21:38.779 | MS1 | 121.4656778171 | 31.1446232549 | 489 | 152650 | -91.65 | 7.76 | 64.08 | 0.11 | 1.83 | 967 |
| 2024-09-20 22:21:39.385 | MS1 | 121.4656775760 | 31.1446233574 | 247 | 152650 | -94.52 | 2.76 | 71.13 | 0.04 | 1.74 | 995 |
| 2024-09-20 22:21:40.434 | MS1 | 121.4656659761 | 31.1446190705 | 167 | 152650 | -96.06 | 6.76 | 61.08 | 0.18 | 2.26 | 1565 |
| 2024-09-20 22:21:41.809 | MS1 | 121.4656715425 | 31.1446200384 | 857 | 152650 | -94.18 | 4.58 | 69.48 | 0.11 | 2.85 | 1594 |
| 2024-09-20 22:21:42.895 | MS1 | 121.4656643793 | 31.1446349011 | 489 | 152650 | -90.41 | 6.08 | 79.80 | 0.09 | 2.42 | 1587 |

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
| 3213736 | 12 | 121.4719199334 | 31.1558115033 | 239 | 11 | 3 | 28.6 | FDD | 857 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3216901 | 4 | 121.4700640103 | 31.1499548463 | 234 | 1 | 3 | 0.9 | TDD | 468 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3224526 | 6 | 121.4709964941 | 31.1537017247 | 180 | 6 | 0 | 8.7 | TDD | 123 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3225612 | 11 | 121.4677943689 | 31.1487981313 | 281 | 2 | 3 | 11.7 | FDD | 247 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3230102 | 5 | 121.4643219998 | 31.1548658012 | 140 | 3 | 3 | 23.8 | TDD | 760 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3235962 | 10 | 121.4688570191 | 31.1553532751 | 143 | 5 | 11 | 23.5 | FDD | 910 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3249019 | 7 | 121.4640690199 | 31.1480763834 | 277 | 15 | 7 | 13.1 | FDD | 167 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3255283 | 9 | 121.4665267219 | 31.1453292397 | 159 | 4 | 6 | 14.3 | FDD | 557 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3261094 | 3 | 121.4721583846 | 31.1526119569 | 150 | 13 | 3 | 26.6 | TDD | 939 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3261351 | 1 | 121.4686796855 | 31.1452794580 | 150 | 9 | 1 | 29.9 | TDD | 578 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3268561 | 13 | 121.4748287851 | 31.1474168740 | 49 | 5 | 6 | 11.5 | FDD | 93 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3274608 | 8 | 121.4725960718 | 31.1501740923 | 357 | 13 | 8 | 17.9 | FDD | 489 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3278651 | 2 | 121.4647231479 | 31.1538447059 | 335 | 6 | 8 | 15.9 | TDD | 8 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.340 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.357 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.465 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.465 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.209 | NREventA2 | measId:1;ServCellPCI:621;Se... |
| 2024-09-20 22:21:35.316 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.596 | NREventA5 | measId:3;ServCellPCI:621;Se... |
| 2024-09-20 22:21:35.670 | NRHandoverAttempt | SourcePCI:621;SourceNR-ARFC... |
| 2024-09-20 22:21:35.707 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.722 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.870 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.870 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261351 | 1 | 10.6764 | 17.5922 | -117.4103 | 10.8089 | 126.1610 | 0.0051 | 0.0062 |
| 2024_09_20 22:00 | 3278651 | 2 | 12.0786 | 18.5673 | -114.6977 | 17.4662 | 162.8120 | 0.0019 | 0.0126 |
| 2024_09_20 22:00 | 3261094 | 3 | 5.7479 | 18.4025 | -114.5755 | 18.0619 | 135.7642 | 0.0191 | 0.0037 |
| 2024_09_20 22:00 | 3216901 | 4 | 17.4266 | 15.3086 | -115.7885 | 19.8686 | 93.6748 | 0.0013 | 0.0072 |
| 2024_09_20 22:00 | 3230102 | 5 | 8.4454 | 11.9635 | -117.5167 | 13.9202 | 118.9658 | 0.0148 | 0.0188 |
| 2024_09_20 22:00 | 3224526 | 6 | 9.8827 | 19.2291 | -117.5154 | 7.3458 | 127.0900 | 0.0036 | 0.0096 |
| 2024_09_20 22:00 | 3249019 | 7 | 13.9235 | 5.7695 | -116.1051 | 4.5071 | 48.2840 | 0.0048 | 0.0174 |
| 2024_09_20 22:00 | 3274608 | 8 | 17.0811 | 12.4099 | -115.4635 | 4.5143 | 29.3610 | 0.0141 | 0.0070 |
| 2024_09_20 22:00 | 3255283 | 9 | 19.0214 | 16.6359 | -117.9507 | 4.7048 | 23.5534 | 0.0062 | 0.0096 |
| 2024_09_20 22:00 | 3235962 | 10 | 16.3830 | 5.4800 | -114.7611 | 4.6656 | 44.3366 | 0.0034 | 0.0144 |
| 2024_09_20 22:00 | 3225612 | 11 | 16.8686 | 9.6677 | -117.6648 | 3.2416 | 33.7065 | 0.0135 | 0.0007 |
| 2024_09_20 22:00 | 3213736 | 12 | 5.9457 | 8.6462 | -116.7944 | 4.6655 | 32.4930 | 0.0142 | 0.0089 |
| 2024_09_20 22:00 | 3268561 | 13 | 13.6331 | 7.8557 | -117.8886 | 3.9811 | 28.1191 | 0.0054 | 0.0049 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414202_3C7B56F4 | 152650 | 489 | -89.9 | 152650 | 93 | -90.9 | 152650 | 910 | -100.8 | 152650 | 557 |
| MR_1774414202_60F4B6EA | 504990 | 123 | -92.7 | 504990 | 468 | -91.2 | 504990 | 578 | -90.8 | 504990 | 8 |
| MR_1774414202_A6C5F4DF | 504990 | 123 | -93.8 | 504990 | 468 | -91.2 | 504990 | 578 | -93.6 | 504990 | 8 |
| MR_1774414202_A4E127CD | 504990 | 123 | -93.8 | 504990 | 468 | -88.7 | 504990 | 578 | -91.5 | 504990 | 8 |
| MR_1774414202_1D139DBD | 152650 | 489 | -88.0 | 152650 | 93 | -89.5 | 152650 | 910 | -100.7 | 152650 | 557 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1291: `9715ff06-b04...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9715ff06-b041-4419-a46e-704614780d1f` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Add neighbor relationship between 3227661_3 and 3267028_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1291] topology](images/train_1291.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3224282_4 and 3267028_2
- `C2`: Lift the tilt angle  of 3267028_2 by 4 degrees
- `C3`: Decrease transmission power for 3267028_2
- `C4`: Decrease A3 Offset threshold for 3227661_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267028_2
- `C6`: Increase A3 Offset threshold for 3267028_2
- `C7`: Increase transmission power for 3227661_3
- `C8`: Check test server and transmission issues
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267028_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase A3 Offset threshold for 3227661_3
- `C12`: Adjust the azimuth of 3267028_2 by 31 degrees
- `C13`: Adjust the azimuth of 3227661_3 by 50 degrees
- `C14`: Decrease A3 Offset threshold for 3267028_2
- `C15`: Increase transmission power for 3267028_2
- `C16`: Decrease transmission power for 3227661_3
- `C17`: Lift the tilt angle of 3227661_3 by 7 degrees
- `C18`: Add neighbor relationship between 3227661_3 and 3267028_2 **← 정답**
- `C19`: Press down the tilt angle  of 3267028_2 by 4 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227661_3
- `C21`: Press down the tilt angle of 3227661_3 by 7 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227661_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.343 | MS1 | 121.4656613774 | 31.1446323254 | 14 | 504990 | -84.16 | 16.49 | 549.27 | 0.08 | 2.81 | 1560 |
| 2024-09-20 22:21:32.801 | MS1 | 121.4656635447 | 31.1446363779 | 14 | 504990 | -78.75 | 16.25 | 473.98 | 0.12 | 2.01 | 1583 |
| 2024-09-20 22:21:33.940 | MS1 | 121.4656662724 | 31.1446313756 | 14 | 504990 | -76.15 | 13.90 | 587.49 | 0.19 | 2.61 | 1568 |
| 2024-09-20 22:21:34.791 | MS1 | 121.4656640807 | 31.1446313960 | 14 | 504990 | -92.88 | -2.54 | 24.88 | 0.17 | 1.12 | 1588 |
| 2024-09-20 22:21:35.321 | MS1 | 121.4656773116 | 31.1446248133 | 14 | 504990 | -90.57 | -3.74 | 36.09 | 0.02 | 1.23 | 1600 |
| 2024-09-20 22:21:36.883 | MS1 | 121.4656628327 | 31.1446192341 | 14 | 504990 | -94.47 | -1.74 | 57.90 | 0.06 | 1.47 | 1600 |
| 2024-09-20 22:21:37.160 | MS1 | 121.4656641011 | 31.1446215134 | 14 | 504990 | -88.94 | -0.07 | 47.89 | 0.13 | 1.01 | 1561 |
| 2024-09-20 22:21:38.305 | MS1 | 121.4656685376 | 31.1446253870 | 14 | 504990 | -78.60 | 17.24 | 524.22 | 0.12 | 1.08 | 1598 |
| 2024-09-20 22:21:39.537 | MS1 | 121.4656751864 | 31.1446273698 | 14 | 504990 | -82.52 | 16.08 | 486.00 | 0.18 | 1.26 | 1572 |
| 2024-09-20 22:21:40.515 | MS1 | 121.4656773007 | 31.1446277920 | 14 | 504990 | -77.44 | 14.41 | 325.26 | 0.11 | 2.12 | 1560 |
| 2024-09-20 22:21:41.555 | MS1 | 121.4656726231 | 31.1446310296 | 14 | 504990 | -79.20 | 15.94 | 554.81 | 0.19 | 2.18 | 1587 |
| 2024-09-20 22:21:42.160 | MS1 | 121.4656693786 | 31.1446377236 | 14 | 504990 | -83.91 | 16.00 | 338.57 | 0.02 | 2.17 | 1584 |

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
| 3224282 | 4 | 121.4759743442 | 31.1536458924 | 188 | 10 | 4 | 32.2 | TDD | 887 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3227661 | 3 | 121.4693539701 | 31.1543794717 | 330 | 5 | 11 | 42.5 | TDD | 14 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3259625 | 1 | 121.4686431190 | 31.1475027411 | 192 | 14 | 2 | 28.1 | TDD | 449 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3267028 | 2 | 121.4703767586 | 31.1445660038 | 302 | 2 | 4 | 16.4 | TDD | 572 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.934 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.957 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.071 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.071 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.814 | NREventA3 | measId:2;ServCellPCI:418;Se... |
| 2024-09-20 22:21:35.814 | NREventA3 | measId:2;ServCellPCI:418;Se... |
| 2024-09-20 22:21:36.814 | NREventA3 | measId:2;ServCellPCI:418;Se... |
| 2024-09-20 22:21:39.314 | NRRRCReestablishAttempt | PCI:418 |
| 2024-09-20 22:21:39.331 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.343 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.485 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.485 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259625 | 1 | 10.1163 | 18.8638 | -117.6574 | 17.8994 | 128.5366 | 0.0116 | 0.0079 |
| 2024_09_20 22:00 | 3267028 | 2 | 10.0373 | 16.4096 | -115.7599 | 17.5154 | 169.1489 | 0.0198 | 0.0080 |
| 2024_09_20 22:00 | 3227661 | 3 | 19.3532 | 6.2551 | -114.8694 | 10.0858 | 146.1003 | 0.0024 | 0.1042 |
| 2024_09_20 22:00 | 3224282 | 4 | 15.4581 | 18.5073 | -117.8468 | 18.4066 | 155.0531 | 0.0102 | 0.0078 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415381_36B65F7B | 504990 | 14 | -93.8 | 504990 | 572 | -88.6 | 504990 | 887 | -97.5 | 504990 | 449 |
| MR_1774415381_624BD85F | 504990 | 14 | -91.3 | 504990 | 572 | -85.8 | 504990 | 887 | -97.3 | 504990 | 449 |
| MR_1774415381_53AA79D5 | 504990 | 572 | -86.4 | 504990 | 14 | -91.6 | 504990 | 887 | -98.6 | 504990 | 449 |
| MR_1774415381_7D05D77E | 504990 | 14 | -92.9 | 504990 | 572 | -89.3 | 504990 | 887 | -96.7 | 504990 | 449 |
| MR_1774415381_C654DF9B | 504990 | 14 | -93.5 | 504990 | 572 | -87.4 | 504990 | 887 | -97.9 | 504990 | 449 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1292: `607c6d1d-e66...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `607c6d1d-e669-4917-9622-4ce5a56419f7` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Add neighbor relationship between 3251520_1 and 3228957_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1292] topology](images/train_1292.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3251520_1
- `C2`: Lift the tilt angle of 3251520_1 by 8 degrees
- `C3`: Add neighbor relationship between 3276604_3 and 3228957_2
- `C4`: Decrease A3 Offset threshold for 3251520_1
- `C5`: Lift the tilt angle  of 3228957_2 by 4 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251520_1
- `C7`: Increase A3 Offset threshold for 3228957_2
- `C8`: Press down the tilt angle of 3251520_1 by 8 degrees
- `C9`: Add neighbor relationship between 3251520_1 and 3228957_2 **← 정답**
- `C10`: Increase transmission power for 3251520_1
- `C11`: Increase transmission power for 3228957_2
- `C12`: Decrease transmission power for 3228957_2
- `C13`: Check test server and transmission issues
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228957_2
- `C15`: Adjust the azimuth of 3251520_1 by 6 degrees
- `C16`: Decrease A3 Offset threshold for 3228957_2
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Press down the tilt angle  of 3228957_2 by 4 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228957_2
- `C20`: Adjust the azimuth of 3228957_2 by 5 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251520_1
- `C22`: Decrease transmission power for 3251520_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.565 | MS1 | 121.4656679343 | 31.1446337372 | 981 | 504990 | -77.87 | 14.91 | 476.05 | 0.12 | 2.43 | 1578 |
| 2024-09-20 22:21:32.104 | MS1 | 121.4656692907 | 31.1446316038 | 981 | 504990 | -75.78 | 12.28 | 344.04 | 0.01 | 2.44 | 1588 |
| 2024-09-20 22:21:33.808 | MS1 | 121.4656701474 | 31.1446254824 | 981 | 504990 | -75.64 | 17.10 | 394.54 | 0.05 | 2.59 | 1597 |
| 2024-09-20 22:21:34.593 | MS1 | 121.4656627817 | 31.1446255401 | 981 | 504990 | -86.67 | -2.03 | 67.66 | 0.13 | 1.10 | 1573 |
| 2024-09-20 22:21:35.714 | MS1 | 121.4656638846 | 31.1446362409 | 981 | 504990 | -90.74 | -0.10 | 52.77 | 0.09 | 1.06 | 1562 |
| 2024-09-20 22:21:36.628 | MS1 | 121.4656585873 | 31.1446298694 | 981 | 504990 | -87.01 | -3.49 | 56.73 | 0.09 | 1.44 | 1565 |
| 2024-09-20 22:21:37.630 | MS1 | 121.4656696228 | 31.1446327791 | 981 | 504990 | -86.60 | -2.29 | 52.31 | 0.08 | 1.14 | 1567 |
| 2024-09-20 22:21:38.896 | MS1 | 121.4656601232 | 31.1446285014 | 981 | 504990 | -79.71 | 13.88 | 490.41 | 0.17 | 1.33 | 1580 |
| 2024-09-20 22:21:39.612 | MS1 | 121.4656734465 | 31.1446233001 | 981 | 504990 | -75.74 | 12.41 | 417.70 | 0.02 | 1.12 | 1571 |
| 2024-09-20 22:21:40.388 | MS1 | 121.4656640265 | 31.1446327930 | 981 | 504990 | -76.63 | 13.88 | 521.38 | 0.04 | 2.31 | 1560 |
| 2024-09-20 22:21:41.905 | MS1 | 121.4656691469 | 31.1446347194 | 981 | 504990 | -84.72 | 17.33 | 539.24 | 0.06 | 2.16 | 1579 |
| 2024-09-20 22:21:42.990 | MS1 | 121.4656613674 | 31.1446200316 | 981 | 504990 | -78.37 | 15.85 | 416.63 | 0.20 | 2.02 | 1597 |

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
| 3228957 | 2 | 121.4723613548 | 31.1477369639 | 247 | 3 | 7 | 18.9 | TDD | 353 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3232006 | 4 | 121.4753790860 | 31.1546856881 | 261 | 9 | 1 | 21.8 | TDD | 93 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3251520 | 1 | 121.4749056980 | 31.1548798894 | 212 | 7 | 0 | 16.7 | TDD | 981 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3276604 | 3 | 121.4714689204 | 31.1501102864 | 220 | 13 | 4 | 44.4 | TDD | 930 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.320 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.342 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.476 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.476 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.155 | NREventA3 | measId:2;ServCellPCI:465;Se... |
| 2024-09-20 22:21:36.155 | NREventA3 | measId:2;ServCellPCI:465;Se... |
| 2024-09-20 22:21:37.155 | NREventA3 | measId:2;ServCellPCI:465;Se... |
| 2024-09-20 22:21:39.655 | NRRRCReestablishAttempt | PCI:465 |
| 2024-09-20 22:21:39.665 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.680 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.809 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.809 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251520 | 1 | 18.7318 | 10.2725 | -116.0626 | 17.0620 | 173.4936 | 0.0142 | 0.1683 |
| 2024_09_20 22:00 | 3228957 | 2 | 10.3648 | 8.0530 | -115.6045 | 17.2022 | 169.8505 | 0.0138 | 0.0071 |
| 2024_09_20 22:00 | 3276604 | 3 | 17.6201 | 8.7848 | -117.2736 | 15.4436 | 116.3816 | 0.0106 | 0.0185 |
| 2024_09_20 22:00 | 3232006 | 4 | 6.0760 | 7.7096 | -117.9990 | 13.0974 | 135.2912 | 0.0028 | 0.0095 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412249_5ABDCE9D | 504990 | 981 | -86.3 | 504990 | 353 | -82.4 | 504990 | 930 | -88.9 | 504990 | 93 |
| MR_1774412249_FDCCBFA2 | 504990 | 353 | -82.2 | 504990 | 981 | -88.0 | 504990 | 930 | -88.8 | 504990 | 93 |
| MR_1774412249_F38305AC | 504990 | 981 | -88.5 | 504990 | 353 | -82.3 | 504990 | 930 | -86.4 | 504990 | 93 |
| MR_1774412249_13FB4B02 | 504990 | 981 | -87.2 | 504990 | 353 | -83.5 | 504990 | 930 | -88.1 | 504990 | 93 |
| MR_1774412249_76AE95F4 | 504990 | 981 | -85.7 | 504990 | 353 | -83.0 | 504990 | 930 | -87.7 | 504990 | 93 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1293: `a861e6a7-53f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a861e6a7-53f1-4288-b806-b2a1f10ba4fe` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243856_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1293] topology](images/train_1293.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3229506_3
- `C2`: Decrease A3 Offset threshold for 3229506_3
- `C3`: Press down the tilt angle of 3243856_1 by 6 degrees
- `C4`: Increase transmission power for 3243856_1
- `C5`: Lift the tilt angle  of 3229506_3 by 3 degrees
- `C6`: Decrease transmission power for 3229506_3
- `C7`: Increase transmission power for 3229506_3
- `C8`: Decrease A3 Offset threshold for 3243856_1
- `C9`: Decrease transmission power for 3243856_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243856_1 **← 정답**
- `C11`: Lift the tilt angle of 3243856_1 by 6 degrees
- `C12`: Adjust the azimuth of 3229506_3 by 25 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229506_3
- `C14`: Add neighbor relationship between 3243856_1 and 3229506_3
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Increase A3 Offset threshold for 3243856_1
- `C17`: Press down the tilt angle  of 3229506_3 by 3 degrees
- `C18`: Adjust the azimuth of 3243856_1 by 4 degrees
- `C19`: Check test server and transmission issues
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243856_1
- `C21`: Add neighbor relationship between 3226483_7 and 3229506_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229506_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.541 | MS1 | 121.4656622491 | 31.1446223814 | 579 | 504990 | -93.34 | 13.97 | 341.05 | 0.01 | 2.12 | 1593 |
| 2024-09-20 22:21:32.176 | MS1 | 121.4656753068 | 31.1446305935 | 292 | 504990 | -93.63 | 14.95 | 375.20 | 0.04 | 2.51 | 1561 |
| 2024-09-20 22:21:33.354 | MS1 | 121.4656653665 | 31.1446262099 | 245 | 504990 | -94.13 | 10.31 | 317.31 | 0.06 | 2.99 | 1562 |
| 2024-09-20 22:21:34.101 | MS1 | 121.4656770241 | 31.1446318724 | 313 | 152650 | -95.27 | 7.82 | 61.02 | 0.05 | 1.94 | 960 |
| 2024-09-20 22:21:35.221 | MS1 | 121.4656744709 | 31.1446249208 | 769 | 152650 | -87.96 | 3.44 | 73.89 | 0.06 | 1.82 | 940 |
| 2024-09-20 22:21:36.895 | MS1 | 121.4656771510 | 31.1446192144 | 160 | 152650 | -89.89 | 2.48 | 74.76 | 0.03 | 1.94 | 940 |
| 2024-09-20 22:21:37.225 | MS1 | 121.4656708455 | 31.1446267114 | 356 | 152650 | -92.34 | 6.73 | 59.49 | 0.07 | 1.71 | 941 |
| 2024-09-20 22:21:38.382 | MS1 | 121.4656732919 | 31.1446217067 | 313 | 152650 | -95.81 | 3.79 | 95.59 | 0.11 | 1.70 | 966 |
| 2024-09-20 22:21:39.453 | MS1 | 121.4656603724 | 31.1446254921 | 769 | 152650 | -92.60 | 4.03 | 86.99 | 0.10 | 1.73 | 925 |
| 2024-09-20 22:21:40.878 | MS1 | 121.4656736428 | 31.1446371608 | 160 | 152650 | -95.07 | 5.14 | 59.32 | 0.01 | 2.99 | 1569 |
| 2024-09-20 22:21:41.448 | MS1 | 121.4656710038 | 31.1446317421 | 356 | 152650 | -89.96 | 5.67 | 67.71 | 0.10 | 2.58 | 1576 |
| 2024-09-20 22:21:42.710 | MS1 | 121.4656629324 | 31.1446227683 | 313 | 152650 | -90.88 | 4.96 | 60.56 | 0.07 | 2.35 | 1598 |

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
| 3217429 | 12 | 121.4656017259 | 31.1552054817 | 212 | 12 | 7 | 3.5 | FDD | 313 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3221939 | 4 | 121.4723682743 | 31.1531526641 | 283 | 1 | 10 | 16.7 | TDD | 1005 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3226483 | 7 | 121.4713306292 | 31.1448840848 | 6 | 1 | 2 | 1.5 | FDD | 160 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3228623 | 9 | 121.4674858086 | 31.1543887466 | 130 | 9 | 6 | 24.9 | FDD | 356 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3229506 | 3 | 121.4706425731 | 31.1495088934 | 196 | 3 | 7 | 3.4 | TDD | 775 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3230167 | 10 | 121.4669867103 | 31.1551528411 | 348 | 4 | 7 | 3.3 | FDD | 7 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3231782 | 6 | 121.4735937986 | 31.1470493626 | 125 | 8 | 1 | 26.8 | TDD | 118 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3239000 | 2 | 121.4739211633 | 31.1537548095 | 12 | 0 | 1 | 2.7 | TDD | 292 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3240034 | 5 | 121.4699265271 | 31.1527370990 | 40 | 7 | 12 | 19.2 | TDD | 245 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3243856 | 1 | 121.4745224555 | 31.1445752328 | 274 | 5 | 6 | 12.4 | TDD | 579 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3245366 | 8 | 121.4743413259 | 31.1520644709 | 205 | 4 | 6 | 24.4 | FDD | 769 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3256204 | 11 | 121.4643400170 | 31.1491058656 | 100 | 15 | 9 | 9.2 | FDD | 370 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3263039 | 13 | 121.4757613861 | 31.1442426152 | 234 | 11 | 10 | 23.2 | FDD | 795 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |

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
| 2024-09-20 22:21:30.825 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.842 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.970 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.970 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.678 | NREventA2 | measId:1;ServCellPCI:598;Se... |
| 2024-09-20 22:21:34.812 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.103 | NREventA5 | measId:3;ServCellPCI:598;Se... |
| 2024-09-20 22:21:35.162 | NRHandoverAttempt | SourcePCI:598;SourceNR-ARFC... |
| 2024-09-20 22:21:35.212 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.225 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.333 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.333 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243856 | 1 | 11.2832 | 15.0759 | -116.6450 | 13.2640 | 177.4307 | 0.0159 | 0.0023 |
| 2024_09_20 22:00 | 3239000 | 2 | 14.5950 | 17.1243 | -116.0250 | 15.0437 | 93.8930 | 0.0037 | 0.0175 |
| 2024_09_20 22:00 | 3229506 | 3 | 8.7938 | 8.6657 | -114.7029 | 14.4709 | 182.4245 | 0.0139 | 0.0127 |
| 2024_09_20 22:00 | 3221939 | 4 | 11.8561 | 18.9142 | -114.2340 | 13.8852 | 91.6347 | 0.0105 | 0.0081 |
| 2024_09_20 22:00 | 3240034 | 5 | 9.5984 | 12.8723 | -114.1055 | 12.6342 | 87.8219 | 0.0134 | 0.0126 |
| 2024_09_20 22:00 | 3231782 | 6 | 10.0924 | 6.0777 | -115.6124 | 19.6473 | 185.4264 | 0.0081 | 0.0051 |
| 2024_09_20 22:00 | 3226483 | 7 | 19.8821 | 13.2658 | -114.0675 | 3.8467 | 20.4844 | 0.0009 | 0.0046 |
| 2024_09_20 22:00 | 3245366 | 8 | 17.5286 | 19.9194 | -117.4801 | 4.9571 | 44.4080 | 0.0063 | 0.0155 |
| 2024_09_20 22:00 | 3228623 | 9 | 19.1401 | 6.2598 | -114.1728 | 4.7010 | 49.7641 | 0.0061 | 0.0105 |
| 2024_09_20 22:00 | 3230167 | 10 | 5.6092 | 11.8165 | -115.9805 | 3.0200 | 30.8291 | 0.0191 | 0.0136 |
| 2024_09_20 22:00 | 3256204 | 11 | 8.8019 | 12.3448 | -114.5841 | 3.7195 | 56.1376 | 0.0175 | 0.0104 |
| 2024_09_20 22:00 | 3217429 | 12 | 11.4127 | 18.0634 | -116.8265 | 4.3908 | 57.8944 | 0.0047 | 0.0026 |
| 2024_09_20 22:00 | 3263039 | 13 | 13.2425 | 7.6048 | -115.3386 | 4.4337 | 31.3191 | 0.0195 | 0.0145 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416726_212280F6 | 152650 | 313 | -95.9 | 152650 | 370 | -103.0 | 152650 | 795 | -99.5 | 152650 | 7 |
| MR_1774416726_3052422B | 152650 | 313 | -95.5 | 152650 | 370 | -101.1 | 152650 | 795 | -100.7 | 152650 | 7 |
| MR_1774416726_6D21D42E | 504990 | 245 | -92.8 | 504990 | 775 | -94.6 | 504990 | 118 | -94.9 | 504990 | 1005 |
| MR_1774416726_5D026B2E | 152650 | 313 | -95.3 | 152650 | 370 | -100.4 | 152650 | 795 | -100.6 | 152650 | 7 |
| MR_1774416726_470E5FFE | 152650 | 313 | -96.4 | 152650 | 370 | -101.1 | 152650 | 795 | -99.4 | 152650 | 7 |
| MR_1774416726_2A76D2C4 | 504990 | 245 | -94.4 | 504990 | 775 | -93.8 | 504990 | 118 | -94.6 | 504990 | 1005 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1294: `3f619aca-c1e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3f619aca-c1e7-4b7c-beeb-e8c5930ec0b4` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243376_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1294] topology](images/train_1294.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3269606_2 by 4 degrees
- `C2`: Increase A3 Offset threshold for 3243376_6
- `C3`: Increase transmission power for 3269606_2
- `C4`: Lift the tilt angle of 3243376_6 by 5 degrees
- `C5`: Add neighbor relationship between 3243376_6 and 3269606_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269606_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243376_6
- `C8`: Increase transmission power for 3243376_6
- `C9`: Decrease transmission power for 3243376_6
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269606_2
- `C11`: Increase A3 Offset threshold for 3269606_2
- `C12`: Press down the tilt angle of 3243376_6 by 5 degrees
- `C13`: Check test server and transmission issues
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Adjust the azimuth of 3243376_6 by 19 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243376_6 **← 정답**
- `C17`: Press down the tilt angle  of 3269606_2 by 4 degrees
- `C18`: Decrease A3 Offset threshold for 3243376_6
- `C19`: Decrease transmission power for 3269606_2
- `C20`: Add neighbor relationship between 3221659_12 and 3269606_2
- `C21`: Adjust the azimuth of 3269606_2 by 46 degrees
- `C22`: Decrease A3 Offset threshold for 3269606_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.651 | MS1 | 121.4656735418 | 31.1446204725 | 478 | 504990 | -93.54 | 14.02 | 551.41 | 0.14 | 2.70 | 1598 |
| 2024-09-20 22:21:32.101 | MS1 | 121.4656765287 | 31.1446337474 | 60 | 504990 | -93.43 | 14.54 | 442.24 | 0.02 | 2.18 | 1563 |
| 2024-09-20 22:21:33.469 | MS1 | 121.4656635107 | 31.1446314738 | 955 | 504990 | -94.39 | 10.78 | 381.87 | 0.14 | 2.29 | 1593 |
| 2024-09-20 22:21:34.809 | MS1 | 121.4656691380 | 31.1446210380 | 990 | 152650 | -93.64 | 6.61 | 55.38 | 0.12 | 1.62 | 966 |
| 2024-09-20 22:21:35.958 | MS1 | 121.4656687991 | 31.1446270795 | 812 | 152650 | -92.51 | 3.51 | 75.51 | 0.13 | 1.97 | 912 |
| 2024-09-20 22:21:36.351 | MS1 | 121.4656733899 | 31.1446276676 | 440 | 152650 | -87.81 | 2.69 | 91.92 | 0.19 | 1.82 | 999 |
| 2024-09-20 22:21:37.667 | MS1 | 121.4656733436 | 31.1446263945 | 876 | 152650 | -94.21 | 6.78 | 62.85 | 0.05 | 1.66 | 917 |
| 2024-09-20 22:21:38.607 | MS1 | 121.4656717320 | 31.1446214003 | 990 | 152650 | -88.16 | 4.50 | 85.08 | 0.04 | 1.50 | 924 |
| 2024-09-20 22:21:39.436 | MS1 | 121.4656620936 | 31.1446270386 | 812 | 152650 | -88.51 | 7.37 | 70.31 | 0.03 | 1.55 | 910 |
| 2024-09-20 22:21:40.314 | MS1 | 121.4656768005 | 31.1446276151 | 440 | 152650 | -95.34 | 7.32 | 101.21 | 0.15 | 2.00 | 1594 |
| 2024-09-20 22:21:41.568 | MS1 | 121.4656739947 | 31.1446369913 | 876 | 152650 | -88.64 | 5.55 | 73.77 | 0.15 | 2.43 | 1579 |
| 2024-09-20 22:21:42.174 | MS1 | 121.4656746133 | 31.1446352173 | 990 | 152650 | -89.59 | 6.59 | 86.94 | 0.10 | 2.24 | 1586 |

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
| 3210601 | 13 | 121.4640086559 | 31.1540534072 | 317 | 10 | 6 | 1.7 | FDD | 990 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3215041 | 8 | 121.4705130435 | 31.1508728172 | 35 | 13 | 4 | 20.4 | FDD | 229 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3221493 | 1 | 121.4734431490 | 31.1443907038 | 76 | 10 | 10 | 24.6 | TDD | 59 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3221659 | 12 | 121.4686898457 | 31.1530024032 | 305 | 8 | 0 | 2.1 | FDD | 440 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3229838 | 5 | 121.4755035486 | 31.1474164523 | 297 | 11 | 6 | 1.9 | TDD | 60 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3231587 | 11 | 121.4743587040 | 31.1444752559 | 293 | 0 | 10 | 2.7 | FDD | 275 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3232843 | 3 | 121.4702602952 | 31.1487385473 | 103 | 6 | 8 | 2.0 | TDD | 721 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3235304 | 10 | 121.4755163185 | 31.1531767697 | 248 | 14 | 2 | 20.1 | FDD | 812 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3238747 | 7 | 121.4736949242 | 31.1515885794 | 23 | 6 | 5 | 11.2 | FDD | 164 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3243376 | 6 | 121.4732550062 | 31.1503813061 | 247 | 4 | 12 | 21.2 | TDD | 478 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3250286 | 9 | 121.4719211238 | 31.1508347062 | 61 | 11 | 12 | 23.6 | FDD | 876 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3269448 | 4 | 121.4723480367 | 31.1459296495 | 58 | 3 | 12 | 21.8 | TDD | 955 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3269606 | 2 | 121.4711343600 | 31.1466970780 | 200 | 1 | 3 | 25.6 | TDD | 74 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.927 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.942 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.059 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.059 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.819 | NREventA2 | measId:1;ServCellPCI:758;Se... |
| 2024-09-20 22:21:34.966 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.197 | NREventA5 | measId:3;ServCellPCI:758;Se... |
| 2024-09-20 22:21:35.276 | NRHandoverAttempt | SourcePCI:758;SourceNR-ARFC... |
| 2024-09-20 22:21:35.298 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.309 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.428 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.428 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221493 | 1 | 15.0954 | 16.7019 | -117.4315 | 18.1444 | 89.8943 | 0.0013 | 0.0076 |
| 2024_09_20 22:00 | 3269606 | 2 | 14.4587 | 11.7265 | -114.3179 | 13.4056 | 172.4245 | 0.0015 | 0.0137 |
| 2024_09_20 22:00 | 3232843 | 3 | 16.6331 | 17.8465 | -114.6693 | 5.6011 | 151.7448 | 0.0126 | 0.0084 |
| 2024_09_20 22:00 | 3269448 | 4 | 14.0115 | 14.8581 | -117.4683 | 10.1330 | 176.6550 | 0.0192 | 0.0003 |
| 2024_09_20 22:00 | 3229838 | 5 | 7.5023 | 17.4550 | -117.7211 | 18.1113 | 80.0625 | 0.0011 | 0.0149 |
| 2024_09_20 22:00 | 3243376 | 6 | 19.7787 | 5.8738 | -114.6661 | 19.2440 | 133.9396 | 0.0182 | 0.0105 |
| 2024_09_20 22:00 | 3238747 | 7 | 19.0628 | 19.3095 | -114.4152 | 4.5653 | 45.2998 | 0.0019 | 0.0060 |
| 2024_09_20 22:00 | 3215041 | 8 | 13.1024 | 9.9893 | -117.8689 | 3.6454 | 22.4877 | 0.0194 | 0.0021 |
| 2024_09_20 22:00 | 3250286 | 9 | 11.9370 | 5.1563 | -114.6298 | 4.3030 | 58.6302 | 0.0175 | 0.0091 |
| 2024_09_20 22:00 | 3235304 | 10 | 12.8699 | 19.1011 | -114.4492 | 3.7027 | 29.9366 | 0.0001 | 0.0031 |
| 2024_09_20 22:00 | 3231587 | 11 | 12.4082 | 8.1720 | -115.3269 | 4.5953 | 25.9047 | 0.0189 | 0.0064 |
| 2024_09_20 22:00 | 3221659 | 12 | 15.9330 | 8.0121 | -115.2373 | 3.2296 | 57.2041 | 0.0032 | 0.0111 |
| 2024_09_20 22:00 | 3210601 | 13 | 5.3896 | 12.5595 | -114.2645 | 4.7869 | 25.4638 | 0.0158 | 0.0034 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413852_9E6B9CA5 | 152650 | 990 | -92.4 | 152650 | 164 | -101.2 | 152650 | 275 | -99.5 | 152650 | 229 |
| MR_1774413852_C4B07BCF | 504990 | 955 | -95.8 | 504990 | 74 | -92.9 | 504990 | 721 | -100.7 | 504990 | 59 |
| MR_1774413852_8CBE3EEA | 504990 | 955 | -94.6 | 504990 | 74 | -92.1 | 504990 | 721 | -101.5 | 504990 | 59 |
| MR_1774413852_5E2D2142 | 152650 | 990 | -93.7 | 152650 | 164 | -101.6 | 152650 | 275 | -102.1 | 152650 | 229 |
| MR_1774413852_91C7460C | 152650 | 990 | -95.4 | 152650 | 164 | -98.7 | 152650 | 275 | -99.9 | 152650 | 229 |
| MR_1774413852_94B7A33D | 504990 | 955 | -96.3 | 504990 | 74 | -91.6 | 504990 | 721 | -99.4 | 504990 | 59 |
| MR_1774413852_866E46E8 | 152650 | 990 | -94.8 | 152650 | 164 | -98.9 | 152650 | 275 | -100.0 | 152650 | 229 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1295: `5bab95fb-d92...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5bab95fb-d92b-40cb-9d97-00a0fe63fdbe` |
| Tag | **multiple-answer** |
| 정답 | **C6|C10|C11|C17** |
| C6 의미 | Increase A3 Offset threshold for 3256076_4 |
| C10 의미 | Press down the tilt angle  of 3275073_1 by 5 degrees |
| C11 의미 | Decrease transmission power for 3275073_1 |
| C17 의미 | Increase A3 Offset threshold for 3275073_1 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1295] topology](images/train_1295.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3275073_1 by 5 degrees
- `C2`: Add neighbor relationship between 3256076_4 and 3275073_1
- `C3`: Decrease transmission power for 3256076_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256076_4
- `C5`: Decrease A3 Offset threshold for 3256076_4
- `C6`: Increase A3 Offset threshold for 3256076_4 **← 정답**
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275073_1
- `C8`: Lift the tilt angle of 3256076_4 by 1 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Press down the tilt angle  of 3275073_1 by 5 degrees **← 정답**
- `C11`: Decrease transmission power for 3275073_1 **← 정답**
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256076_4
- `C13`: Increase transmission power for 3275073_1
- `C14`: Decrease A3 Offset threshold for 3275073_1
- `C15`: Check test server and transmission issues
- `C16`: Adjust the azimuth of 3275073_1 by 17 degrees
- `C17`: Increase A3 Offset threshold for 3275073_1 **← 정답**
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275073_1
- `C19`: Increase transmission power for 3256076_4
- `C20`: Adjust the azimuth of 3256076_4 by 31 degrees
- `C21`: Add neighbor relationship between 3258514_3 and 3275073_1
- `C22`: Press down the tilt angle of 3256076_4 by 1 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.372 | MS1 | 121.4656744598 | 31.1446280144 | 632 | 504990 | -80.51 | 13.10 | 359.45 | 0.16 | 2.26 | 1584 |
| 2024-09-20 22:21:32.389 | MS1 | 121.4656706665 | 31.1446345937 | 632 | 504990 | -81.30 | 17.65 | 444.65 | 0.10 | 2.77 | 1564 |
| 2024-09-20 22:21:33.370 | MS1 | 121.4656773551 | 31.1446345376 | 632 | 504990 | -76.56 | 12.82 | 363.11 | 0.04 | 2.55 | 1596 |
| 2024-09-20 22:21:34.396 | MS1 | 121.4656684213 | 31.1446271041 | 274 | 504990 | -86.45 | 2.98 | 41.79 | 0.06 | 1.32 | 1582 |
| 2024-09-20 22:21:35.121 | MS1 | 121.4656597232 | 31.1446328453 | 274 | 504990 | -85.67 | 1.94 | 54.69 | 0.13 | 1.28 | 1589 |
| 2024-09-20 22:21:36.925 | MS1 | 121.4656758945 | 31.1446235841 | 632 | 504990 | -82.11 | 2.31 | 46.26 | 0.17 | 1.16 | 1562 |
| 2024-09-20 22:21:37.586 | MS1 | 121.4656776633 | 31.1446365219 | 632 | 504990 | -85.99 | 2.52 | 54.40 | 0.13 | 1.06 | 1584 |
| 2024-09-20 22:21:38.970 | MS1 | 121.4656708632 | 31.1446214363 | 274 | 504990 | -80.18 | 4.97 | 23.53 | 0.08 | 1.33 | 1563 |
| 2024-09-20 22:21:39.620 | MS1 | 121.4656636763 | 31.1446280766 | 274 | 504990 | -84.13 | 3.62 | 81.00 | 0.17 | 1.29 | 1595 |
| 2024-09-20 22:21:40.910 | MS1 | 121.4656613836 | 31.1446265872 | 274 | 504990 | -84.34 | 17.45 | 399.91 | 0.04 | 2.81 | 1565 |
| 2024-09-20 22:21:41.309 | MS1 | 121.4656755314 | 31.1446196294 | 274 | 504990 | -76.49 | 13.77 | 361.54 | 0.06 | 2.74 | 1590 |
| 2024-09-20 22:21:42.322 | MS1 | 121.4656650396 | 31.1446190869 | 274 | 504990 | -75.04 | 13.58 | 317.22 | 0.17 | 2.60 | 1593 |

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
| 3246795 | 5 | 121.4711964281 | 31.1519636078 | 339 | 7 | 0 | 27.2 | TDD | 187 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3256076 | 4 | 121.4677376840 | 31.1524421203 | 162 | 0 | 0 | 20.7 | TDD | 632 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3258514 | 3 | 121.4714217494 | 31.1490120068 | 207 | 15 | 0 | 36.9 | TDD | 596 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3268879 | 2 | 121.4736583671 | 31.1479775500 | 146 | 2 | 3 | 42.9 | TDD | 274 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3275073 | 1 | 121.4642755877 | 31.1553285556 | 191 | 3 | 11 | 36.1 | TDD | 846 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.522 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.542 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.656 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.656 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.379 | NREventA3 | measId:2;ServCellPCI:444;Se... |
| 2024-09-20 22:21:34.619 | NRHandoverAttempt | SourcePCI:444;SourceNR-ARFC... |
| 2024-09-20 22:21:34.667 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.682 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.812 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.812 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.379 | NREventA3 | measId:2;ServCellPCI:523;Se... |
| 2024-09-20 22:21:36.619 | NRHandoverAttempt | SourcePCI:523;SourceNR-ARFC... |
| 2024-09-20 22:21:36.654 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.666 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:36.790 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.790 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.379 | NREventA3 | measId:2;ServCellPCI:444;Se... |
| 2024-09-20 22:21:38.619 | NRHandoverAttempt | SourcePCI:444;SourceNR-ARFC... |
| 2024-09-20 22:21:38.655 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.666 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.789 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.789 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275073 | 1 | 5.4635 | 17.9018 | -115.9451 | 12.1271 | 155.0665 | 0.0150 | 0.0095 |
| 2024_09_20 22:00 | 3268879 | 2 | 16.8031 | 6.0065 | -117.9944 | 11.0550 | 91.4165 | 0.0007 | 0.0138 |
| 2024_09_20 22:00 | 3258514 | 3 | 17.7359 | 16.4558 | -115.5004 | 8.2979 | 113.8464 | 0.0144 | 0.0008 |
| 2024_09_20 22:00 | 3256076 | 4 | 14.4579 | 15.8931 | -114.1042 | 9.2257 | 89.0593 | 0.0188 | 0.0082 |
| 2024_09_20 22:00 | 3246795 | 5 | 15.6335 | 7.0460 | -115.5137 | 12.4360 | 98.4574 | 0.0007 | 0.0000 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413517_A1EABE5D | 504990 | 274 | -87.0 | 504990 | 632 | -81.8 | 504990 | 846 | -86.2 | 504990 | 596 |
| MR_1774413517_65762F97 | 504990 | 274 | -84.9 | 504990 | 632 | -80.5 | 504990 | 846 | -87.0 | 504990 | 596 |
| MR_1774413517_83174479 | 504990 | 274 | -84.7 | 504990 | 632 | -80.8 | 504990 | 846 | -84.7 | 504990 | 596 |
| MR_1774413517_847D8305 | 504990 | 274 | -87.6 | 504990 | 632 | -80.5 | 504990 | 846 | -87.1 | 504990 | 596 |
| MR_1774413517_26DB3DFE | 504990 | 274 | -85.0 | 504990 | 632 | -81.4 | 504990 | 846 | -87.3 | 504990 | 596 |
| MR_1774413517_CAAFFD31 | 504990 | 632 | -88.4 | 504990 | 274 | -83.8 | 504990 | 846 | -85.4 | 504990 | 596 |
| MR_1774413517_6037C5A6 | 504990 | 274 | -86.3 | 504990 | 632 | -80.2 | 504990 | 846 | -84.2 | 504990 | 596 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1296: `737d86f4-49a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `737d86f4-49a3-47df-ac40-a476146083a8` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3245487_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1296] topology](images/train_1296.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3245487_4 and 3241542_1
- `C2`: Decrease A3 Offset threshold for 3241542_1
- `C3`: Decrease transmission power for 3245487_4
- `C4`: Decrease transmission power for 3241542_1
- `C5`: Lift the tilt angle of 3245487_4 by 4 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245487_4 **← 정답**
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241542_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase A3 Offset threshold for 3245487_4
- `C10`: Adjust the azimuth of 3245487_4 by 49 degrees
- `C11`: Lift the tilt angle  of 3241542_1 by 10 degrees
- `C12`: Decrease A3 Offset threshold for 3245487_4
- `C13`: Press down the tilt angle  of 3241542_1 by 10 degrees
- `C14`: Adjust the azimuth of 3241542_1 by 50 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241542_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245487_4
- `C17`: Increase A3 Offset threshold for 3241542_1
- `C18`: Add neighbor relationship between 3257583_3 and 3241542_1
- `C19`: Increase transmission power for 3245487_4
- `C20`: Increase transmission power for 3241542_1
- `C21`: Check test server and transmission issues
- `C22`: Press down the tilt angle of 3245487_4 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.152 | MS1 | 121.4656732094 | 31.1446209745 | 565 | 504990 | -91.11 | 15.17 | 370.92 | 0.15 | 2.19 | 1570 |
| 2024-09-20 22:21:32.597 | MS1 | 121.4656764614 | 31.1446306273 | 565 | 504990 | -90.87 | 15.43 | 484.96 | 0.02 | 2.62 | 1571 |
| 2024-09-20 22:21:33.149 | MS1 | 121.4656646048 | 31.1446181322 | 565 | 504990 | -88.18 | 17.69 | 549.75 | 0.10 | 2.20 | 1569 |
| 2024-09-20 22:21:34.203 | MS1 | 121.4656617765 | 31.1446364866 | 565 | 504990 | -85.95 | 14.28 | 95.71 | 0.66 | 2.14 | 629 |
| 2024-09-20 22:21:35.452 | MS1 | 121.4656737046 | 31.1446350915 | 565 | 504990 | -91.12 | 17.70 | 66.73 | 0.63 | 2.89 | 550 |
| 2024-09-20 22:21:36.329 | MS1 | 121.4656584168 | 31.1446190792 | 565 | 504990 | -91.61 | 15.72 | 75.85 | 0.52 | 2.66 | 598 |
| 2024-09-20 22:21:37.569 | MS1 | 121.4656676685 | 31.1446246340 | 565 | 504990 | -90.53 | 7.92 | 89.05 | 0.64 | 2.59 | 592 |
| 2024-09-20 22:21:38.328 | MS1 | 121.4656697791 | 31.1446364107 | 565 | 504990 | -90.63 | 9.54 | 56.38 | 0.59 | 2.08 | 628 |
| 2024-09-20 22:21:39.131 | MS1 | 121.4656732743 | 31.1446261094 | 565 | 504990 | -91.32 | 9.14 | 62.34 | 0.56 | 2.74 | 623 |
| 2024-09-20 22:21:40.146 | MS1 | 121.4656584989 | 31.1446241672 | 565 | 504990 | -90.83 | 11.94 | 467.70 | 0.06 | 2.93 | 1589 |
| 2024-09-20 22:21:41.790 | MS1 | 121.4656661565 | 31.1446301378 | 565 | 504990 | -92.05 | 7.92 | 434.88 | 0.11 | 2.04 | 1577 |
| 2024-09-20 22:21:42.567 | MS1 | 121.4656605361 | 31.1446191533 | 565 | 504990 | -89.88 | 7.91 | 347.85 | 0.08 | 2.77 | 1591 |

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
| 3239631 | 2 | 121.4648676524 | 31.1555272518 | 123 | 8 | 4 | 42.2 | TDD | 467 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3241542 | 1 | 121.4695544154 | 31.1493926443 | 110 | 9 | 6 | 21.7 | TDD | 10 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3245487 | 4 | 121.4752063500 | 31.1530184843 | 273 | 3 | 5 | 16.8 | TDD | 565 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3257583 | 3 | 121.4748107731 | 31.1537767805 | 102 | 7 | 12 | 43.5 | TDD | 812 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.970 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.990 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.128 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.128 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.802 | NREventA3 | measId:2;ServCellPCI:589;Se... |
| 2024-09-20 22:21:38.042 | NRHandoverAttempt | SourcePCI:589;SourceNR-ARFC... |
| 2024-09-20 22:21:38.082 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.093 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.225 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.225 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241542 | 1 | 6.2464 | 6.3940 | -117.8409 | 6.6991 | 129.9283 | 0.0077 | 0.0122 |
| 2024_09_20 22:00 | 3239631 | 2 | 11.0206 | 19.4071 | -114.5143 | 17.1206 | 160.2427 | 0.0021 | 0.0099 |
| 2024_09_20 22:00 | 3257583 | 3 | 19.3561 | 8.6184 | -114.4901 | 9.4346 | 153.8503 | 0.0196 | 0.0173 |
| 2024_09_20 22:00 | 3245487 | 4 | 6.2257 | 10.6289 | -117.0304 | 8.0948 | 139.1783 | 0.0008 | 0.0007 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415315_9CE2A219 | 504990 | 565 | -85.2 | 504990 | 10 | -92.5 | 504990 | 812 | -94.8 | 504990 | 467 |
| MR_1774415315_167DC259 | 504990 | 565 | -87.9 | 504990 | 10 | -89.9 | 504990 | 812 | -96.5 | 504990 | 467 |
| MR_1774415315_6D6BF8DA | 504990 | 565 | -85.7 | 504990 | 10 | -91.2 | 504990 | 812 | -94.9 | 504990 | 467 |
| MR_1774415315_2E5E261A | 504990 | 565 | -86.5 | 504990 | 10 | -92.7 | 504990 | 812 | -96.3 | 504990 | 467 |
| MR_1774415315_1E82ED08 | 504990 | 565 | -86.5 | 504990 | 10 | -90.4 | 504990 | 812 | -94.9 | 504990 | 467 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1297: `4ee02f20-f89...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4ee02f20-f893-4b82-8281-7328721b28bd` |
| Tag | **multiple-answer** |
| 정답 | **C1|C12** |
| C1 의미 | Adjust the azimuth of 3242280_1 by 50 degrees |
| C12 의미 | Increase transmission power for 3242280_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1297] topology](images/train_1297.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3242280_1 by 50 degrees **← 정답**
- `C2`: Lift the tilt angle of 3242280_1 by 9 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260483_2
- `C4`: Increase A3 Offset threshold for 3260483_2
- `C5`: Press down the tilt angle  of 3260483_2 by 3 degrees
- `C6`: Decrease transmission power for 3242280_1
- `C7`: Press down the tilt angle of 3242280_1 by 9 degrees
- `C8`: Increase A3 Offset threshold for 3242280_1
- `C9`: Add neighbor relationship between 3257564_3 and 3260483_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Check test server and transmission issues
- `C12`: Increase transmission power for 3242280_1 **← 정답**
- `C13`: Increase transmission power for 3260483_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260483_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242280_1
- `C16`: Decrease transmission power for 3260483_2
- `C17`: Add neighbor relationship between 3242280_1 and 3260483_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242280_1
- `C19`: Lift the tilt angle  of 3260483_2 by 3 degrees
- `C20`: Decrease A3 Offset threshold for 3242280_1
- `C21`: Decrease A3 Offset threshold for 3260483_2
- `C22`: Adjust the azimuth of 3260483_2 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.455 | MS1 | 121.4656729867 | 31.1446335335 | 891 | 504990 | -87.65 | 15.98 | 351.64 | 0.12 | 2.09 | 1561 |
| 2024-09-20 22:21:32.807 | MS1 | 121.4656624791 | 31.1446335407 | 891 | 504990 | -86.12 | 12.20 | 499.37 | 0.04 | 2.99 | 1583 |
| 2024-09-20 22:21:33.752 | MS1 | 121.4656588571 | 31.1446292263 | 891 | 504990 | -91.86 | 13.57 | 460.86 | 0.07 | 2.59 | 1580 |
| 2024-09-20 22:21:34.475 | MS1 | 121.4656598156 | 31.1446367567 | 891 | 504990 | -100.09 | -1.54 | 73.00 | 0.15 | 1.23 | 1562 |
| 2024-09-20 22:21:35.160 | MS1 | 121.4656646530 | 31.1446252839 | 891 | 504990 | -103.38 | -1.42 | 82.55 | 0.02 | 1.22 | 1592 |
| 2024-09-20 22:21:36.777 | MS1 | 121.4656738103 | 31.1446277999 | 891 | 504990 | -101.89 | -1.62 | 32.44 | 0.19 | 1.24 | 1563 |
| 2024-09-20 22:21:37.349 | MS1 | 121.4656775983 | 31.1446359253 | 891 | 504990 | -104.20 | 1.82 | 38.18 | 0.09 | 1.49 | 1572 |
| 2024-09-20 22:21:38.292 | MS1 | 121.4656768240 | 31.1446313805 | 891 | 504990 | -106.94 | 1.33 | 81.66 | 0.14 | 1.26 | 1576 |
| 2024-09-20 22:21:39.776 | MS1 | 121.4656746150 | 31.1446295898 | 891 | 504990 | -108.59 | 0.03 | 50.95 | 0.09 | 1.21 | 1570 |
| 2024-09-20 22:21:40.531 | MS1 | 121.4656707164 | 31.1446302331 | 891 | 504990 | -87.62 | 12.24 | 411.18 | 0.07 | 2.30 | 1561 |
| 2024-09-20 22:21:41.283 | MS1 | 121.4656688765 | 31.1446204607 | 891 | 504990 | -89.11 | 16.06 | 476.30 | 0.06 | 2.49 | 1582 |
| 2024-09-20 22:21:42.380 | MS1 | 121.4656632425 | 31.1446218052 | 891 | 504990 | -86.66 | 14.16 | 326.45 | 0.12 | 2.38 | 1569 |

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
| 3242280 | 1 | 121.4747512554 | 31.1482187523 | 309 | 6 | 1 | 49.7 | TDD | 891 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3257564 | 3 | 121.4683840250 | 31.1528887125 | 129 | 11 | 7 | 47.1 | TDD | 683 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3259297 | 4 | 121.4724385389 | 31.1459849742 | 295 | 9 | 8 | 37.5 | TDD | 95 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3260483 | 2 | 121.4651770490 | 31.1556612859 | 176 | 2 | 8 | 19.7 | TDD | 923 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.902 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.922 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.046 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.046 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.291 | NREventA2 | measId:1;ServCellPCI:964;Se... |
| 2024-09-20 22:21:34.414 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242280 | 1 | 11.7409 | 10.7933 | -114.7014 | 12.0772 | 133.3482 | 0.1644 | 0.0138 |
| 2024_09_20 22:00 | 3260483 | 2 | 15.8177 | 10.6473 | -116.3084 | 14.8050 | 136.5961 | 0.0082 | 0.0076 |
| 2024_09_20 22:00 | 3257564 | 3 | 9.0670 | 18.3148 | -117.5993 | 5.6525 | 192.9856 | 0.0115 | 0.0039 |
| 2024_09_20 22:00 | 3259297 | 4 | 11.5634 | 18.9273 | -115.8545 | 7.4745 | 110.8689 | 0.0148 | 0.0065 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416708_41F57FC2 | 504990 | 891 | -100.1 | 504990 | 923 | -105.5 | 504990 | 683 | -109.0 | 504990 | 95 |
| MR_1774416708_A78C346A | 504990 | 891 | -100.5 | 504990 | 923 | -105.2 | 504990 | 683 | -112.1 | 504990 | 95 |
| MR_1774416708_E5284C04 | 504990 | 891 | -98.6 | 504990 | 923 | -102.3 | 504990 | 683 | -110.4 | 504990 | 95 |
| MR_1774416708_90620B4E | 504990 | 891 | -99.3 | 504990 | 923 | -102.3 | 504990 | 683 | -110.5 | 504990 | 95 |
| MR_1774416708_B7A12095 | 504990 | 891 | -101.8 | 504990 | 923 | -102.0 | 504990 | 683 | -111.4 | 504990 | 95 |
| MR_1774416708_4CCB698E | 504990 | 891 | -99.8 | 504990 | 923 | -104.1 | 504990 | 683 | -111.7 | 504990 | 95 |
| MR_1774416708_EA98DDCF | 504990 | 891 | -100.0 | 504990 | 923 | -103.6 | 504990 | 683 | -111.1 | 504990 | 95 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1298: `69b27230-efd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `69b27230-efd0-4699-b5e4-9ffe874ffdc3` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1298] topology](images/train_1298.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227350_3
- `C2`: Increase transmission power for 3227350_3
- `C3`: Lift the tilt angle  of 3230037_2 by 10 degrees
- `C4`: Insufficient data; more data is needed for judgment. **← 정답**
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230037_2
- `C6`: Increase A3 Offset threshold for 3227350_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230037_2
- `C8`: Add neighbor relationship between 3221356_1 and 3230037_2
- `C9`: Lift the tilt angle of 3227350_3 by 5 degrees
- `C10`: Decrease A3 Offset threshold for 3230037_2
- `C11`: Add neighbor relationship between 3227350_3 and 3230037_2
- `C12`: Decrease transmission power for 3230037_2
- `C13`: Adjust the azimuth of 3230037_2 by 0 degrees
- `C14`: Press down the tilt angle of 3227350_3 by 5 degrees
- `C15`: Decrease transmission power for 3227350_3
- `C16`: Press down the tilt angle  of 3230037_2 by 10 degrees
- `C17`: Check test server and transmission issues
- `C18`: Adjust the azimuth of 3227350_3 by 50 degrees
- `C19`: Increase A3 Offset threshold for 3230037_2
- `C20`: Increase transmission power for 3230037_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227350_3
- `C22`: Decrease A3 Offset threshold for 3227350_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.433 | MS1 | 121.4656645415 | 31.1446241261 | 71 | 504990 | -91.56 | 12.43 | 527.39 | 0.18 | 2.90 | 1566 |
| 2024-09-20 22:21:32.680 | MS1 | 121.4656592485 | 31.1446232366 | 71 | 504990 | -86.92 | 12.42 | 476.15 | 0.14 | 2.51 | 1594 |
| 2024-09-20 22:21:33.142 | MS1 | 121.4656620602 | 31.1446245677 | 71 | 504990 | -89.70 | 16.29 | 552.41 | 0.19 | 2.64 | 1575 |
| 2024-09-20 22:21:34.898 | MS1 | 121.4656779316 | 31.1446331702 | 71 | 504990 | -88.52 | 17.99 | 83.80 | 0.17 | 2.33 | 1569 |
| 2024-09-20 22:21:35.415 | MS1 | 121.4656615492 | 31.1446369724 | 71 | 504990 | -85.03 | 16.42 | 90.90 | 0.13 | 2.59 | 1580 |
| 2024-09-20 22:21:36.987 | MS1 | 121.4656665810 | 31.1446271915 | 71 | 504990 | -87.44 | 17.00 | 69.87 | 0.16 | 2.17 | 1566 |
| 2024-09-20 22:21:37.321 | MS1 | 121.4656669770 | 31.1446369722 | 71 | 504990 | -93.09 | 8.27 | 62.29 | 0.03 | 2.19 | 1568 |
| 2024-09-20 22:21:38.939 | MS1 | 121.4656685789 | 31.1446379540 | 71 | 504990 | -89.61 | 11.01 | 78.69 | 0.19 | 2.14 | 1589 |
| 2024-09-20 22:21:39.799 | MS1 | 121.4656664951 | 31.1446295313 | 71 | 504990 | -91.50 | 11.16 | 44.53 | 0.03 | 2.33 | 1591 |
| 2024-09-20 22:21:40.966 | MS1 | 121.4656726995 | 31.1446311107 | 71 | 504990 | -93.00 | 11.91 | 435.42 | 0.02 | 2.54 | 1590 |
| 2024-09-20 22:21:41.903 | MS1 | 121.4656580322 | 31.1446232560 | 71 | 504990 | -89.22 | 8.94 | 423.49 | 0.02 | 2.68 | 1569 |
| 2024-09-20 22:21:42.798 | MS1 | 121.4656675333 | 31.1446182413 | 71 | 504990 | -93.45 | 7.36 | 371.67 | 0.06 | 2.54 | 1593 |

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
| 3221356 | 1 | 121.4714242362 | 31.1462015569 | 79 | 7 | 8 | 33.7 | TDD | 153 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3227350 | 3 | 121.4694204039 | 31.1467801336 | 302 | 0 | 3 | 40.8 | TDD | 71 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3230037 | 2 | 121.4693025623 | 31.1535163560 | 199 | 13 | 10 | 34.6 | TDD | 597 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3269944 | 4 | 121.4677021757 | 31.1476170517 | 84 | 7 | 5 | 40.0 | TDD | 911 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.931 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.949 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.058 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.058 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.744 | NREventA3 | measId:2;ServCellPCI:337;Se... |
| 2024-09-20 22:21:37.984 | NRHandoverAttempt | SourcePCI:337;SourceNR-ARFC... |
| 2024-09-20 22:21:38.018 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.029 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.139 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.139 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3221356 | 1 | 84.7936 | 81.0095 | -117.9206 | 10.4688 | 89.8200 | 0.0005 | 0.0184 |
| 2024_09_19 22:00 | 3230037 | 2 | 86.2444 | 83.8777 | -117.6178 | 19.3065 | 136.6917 | 0.0104 | 0.0102 |
| 2024_09_19 22:00 | 3227350 | 3 | 80.1690 | 78.3480 | -117.3785 | 18.7796 | 138.0504 | 0.0009 | 0.0094 |
| 2024_09_19 22:00 | 3269944 | 4 | 77.1282 | 81.7624 | -116.1068 | 15.4632 | 146.8860 | 0.0075 | 0.0005 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414656_F1F04A7A | 504990 | 71 | -89.9 | 504990 | 597 | -89.7 | 504990 | 153 | -95.3 | 504990 | 911 |
| MR_1774414656_141C0D0B | 504990 | 71 | -90.2 | 504990 | 597 | -91.0 | 504990 | 153 | -96.4 | 504990 | 911 |
| MR_1774414656_90FCC0AB | 504990 | 71 | -86.7 | 504990 | 597 | -90.6 | 504990 | 153 | -95.9 | 504990 | 911 |
| MR_1774414656_334D899F | 504990 | 71 | -87.0 | 504990 | 597 | -92.6 | 504990 | 153 | -95.5 | 504990 | 911 |
| MR_1774414656_5E3969C9 | 504990 | 71 | -87.7 | 504990 | 597 | -89.8 | 504990 | 153 | -93.4 | 504990 | 911 |
| MR_1774414656_27FD63D8 | 504990 | 71 | -89.3 | 504990 | 597 | -90.5 | 504990 | 153 | -97.1 | 504990 | 911 |
| MR_1774414656_ECEA4847 | 504990 | 71 | -90.4 | 504990 | 597 | -93.3 | 504990 | 153 | -95.4 | 504990 | 911 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1299: `3bc58231-24c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3bc58231-24ca-4fdf-a010-0ce5eaf770a7` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1299] topology](images/train_1299.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues **← 정답**
- `C2`: Press down the tilt angle  of 3236510_3 by 10 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236510_3
- `C4`: Increase transmission power for 3236510_3
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Lift the tilt angle of 3218267_2 by 9 degrees
- `C7`: Add neighbor relationship between 3257249_4 and 3236510_3
- `C8`: Adjust the azimuth of 3218267_2 by 42 degrees
- `C9`: Add neighbor relationship between 3218267_2 and 3236510_3
- `C10`: Lift the tilt angle  of 3236510_3 by 10 degrees
- `C11`: Decrease A3 Offset threshold for 3236510_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218267_2
- `C13`: Increase transmission power for 3218267_2
- `C14`: Increase A3 Offset threshold for 3218267_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236510_3
- `C16`: Adjust the azimuth of 3236510_3 by 50 degrees
- `C17`: Decrease A3 Offset threshold for 3218267_2
- `C18`: Increase A3 Offset threshold for 3236510_3
- `C19`: Decrease transmission power for 3218267_2
- `C20`: Decrease transmission power for 3236510_3
- `C21`: Press down the tilt angle of 3218267_2 by 9 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218267_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.483 | MS1 | 121.4656654198 | 31.1446352526 | 907 | 504990 | -90.94 | 16.63 | 530.71 | 0.09 | 2.97 | 1576 |
| 2024-09-20 22:21:32.695 | MS1 | 121.4656772312 | 31.1446231889 | 907 | 504990 | -90.59 | 12.79 | 555.16 | 0.15 | 2.63 | 1596 |
| 2024-09-20 22:21:33.811 | MS1 | 121.4656735902 | 31.1446348009 | 907 | 504990 | -90.66 | 13.18 | 468.37 | 0.08 | 2.05 | 1590 |
| 2024-09-20 22:21:34.102 | MS1 | 121.4656729718 | 31.1446228964 | 907 | 504990 | -91.85 | 16.76 | 97.05 | 0.12 | 2.21 | 353 |
| 2024-09-20 22:21:35.304 | MS1 | 121.4656685113 | 31.1446247789 | 907 | 504990 | -85.97 | 17.17 | 92.60 | 0.14 | 2.91 | 467 |
| 2024-09-20 22:21:36.587 | MS1 | 121.4656713391 | 31.1446234533 | 907 | 504990 | -85.18 | 14.98 | 84.92 | 0.16 | 2.87 | 410 |
| 2024-09-20 22:21:37.291 | MS1 | 121.4656777099 | 31.1446273058 | 907 | 504990 | -93.07 | 8.15 | 85.42 | 0.08 | 2.75 | 312 |
| 2024-09-20 22:21:38.377 | MS1 | 121.4656595369 | 31.1446345639 | 907 | 504990 | -90.20 | 8.48 | 81.64 | 0.08 | 2.84 | 462 |
| 2024-09-20 22:21:39.369 | MS1 | 121.4656622930 | 31.1446349412 | 907 | 504990 | -92.50 | 11.40 | 62.26 | 0.17 | 2.28 | 445 |
| 2024-09-20 22:21:40.821 | MS1 | 121.4656598103 | 31.1446288449 | 907 | 504990 | -91.13 | 7.75 | 558.28 | 0.18 | 2.71 | 1586 |
| 2024-09-20 22:21:41.859 | MS1 | 121.4656582632 | 31.1446187914 | 907 | 504990 | -89.44 | 10.14 | 469.15 | 0.17 | 2.51 | 1591 |
| 2024-09-20 22:21:42.994 | MS1 | 121.4656697845 | 31.1446345872 | 907 | 504990 | -91.98 | 10.66 | 567.35 | 0.08 | 2.83 | 1571 |

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
| 3211784 | 1 | 121.4730479375 | 31.1466797712 | 83 | 15 | 0 | 16.1 | TDD | 811 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3218267 | 2 | 121.4747722495 | 31.1506291636 | 190 | 8 | 6 | 27.2 | TDD | 907 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3236510 | 3 | 121.4700405203 | 31.1450287590 | 131 | 8 | 6 | 45.4 | TDD | 726 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3257249 | 4 | 121.4675170945 | 31.1508133196 | 147 | 6 | 8 | 45.8 | TDD | 263 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.963 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.988 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.105 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.105 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.840 | NREventA3 | measId:2;ServCellPCI:204;Se... |
| 2024-09-20 22:21:38.080 | NRHandoverAttempt | SourcePCI:204;SourceNR-ARFC... |
| 2024-09-20 22:21:38.127 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.139 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.239 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.239 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211784 | 1 | 12.5655 | 11.1855 | -115.8875 | 12.1669 | 165.4380 | 0.0165 | 0.0047 |
| 2024_09_20 22:00 | 3218267 | 2 | 15.6351 | 6.8828 | -114.7720 | 15.5892 | 87.2212 | 0.0148 | 0.0069 |
| 2024_09_20 22:00 | 3236510 | 3 | 17.0122 | 18.0778 | -114.0885 | 16.0146 | 136.7959 | 0.0034 | 0.0125 |
| 2024_09_20 22:00 | 3257249 | 4 | 14.8583 | 6.9342 | -116.9505 | 7.5362 | 155.9211 | 0.0145 | 0.0011 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417189_7DF1F587 | 504990 | 907 | -93.2 | 504990 | 726 | -94.0 | 504990 | 263 | -101.5 | 504990 | 811 |
| MR_1774417189_582B4695 | 504990 | 907 | -90.8 | 504990 | 726 | -93.7 | 504990 | 263 | -102.4 | 504990 | 811 |
| MR_1774417189_F722B7A5 | 504990 | 907 | -93.5 | 504990 | 726 | -95.8 | 504990 | 263 | -100.2 | 504990 | 811 |
| MR_1774417189_E57FABAA | 504990 | 907 | -90.9 | 504990 | 726 | -95.1 | 504990 | 263 | -99.5 | 504990 | 811 |
| MR_1774417189_0EE2BC49 | 504990 | 907 | -92.4 | 504990 | 726 | -95.1 | 504990 | 263 | -99.9 | 504990 | 811 |
| MR_1774417189_F737E4DB | 504990 | 907 | -93.1 | 504990 | 726 | -93.2 | 504990 | 263 | -100.2 | 504990 | 811 |
| MR_1774417189_97011BEB | 504990 | 907 | -90.5 | 504990 | 726 | -94.2 | 504990 | 263 | -101.2 | 504990 | 811 |
| MR_1774417189_B4BCFA07 | 504990 | 907 | -92.9 | 504990 | 726 | -92.1 | 504990 | 263 | -100.1 | 504990 | 811 |

> *... 2개 열 생략 (전체 14열)*

---
