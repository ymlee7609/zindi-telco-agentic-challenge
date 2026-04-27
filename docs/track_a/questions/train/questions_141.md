# Track A 문제 분석 — train[1400]~train[1409]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1400] ~ train[1409] (10개)

## 목차

1. [문제 1400: `5319d6f4-a8d...`](#1400) — single-answer, 정답: C22
2. [문제 1401: `31a67c8e-3be...`](#1401) — single-answer, 정답: C22
3. [문제 1402: `5c40b895-1d7...`](#1402) — single-answer, 정답: C14
4. [문제 1403: `38714a94-d69...`](#1403) — single-answer, 정답: C3
5. [문제 1404: `39b42f1a-947...`](#1404) — single-answer, 정답: C5
6. [문제 1405: `c7c57306-e8d...`](#1405) — single-answer, 정답: C2
7. [문제 1406: `64b36b49-71c...`](#1406) — single-answer, 정답: C14
8. [문제 1407: `e210dde1-649...`](#1407) — single-answer, 정답: C2
9. [문제 1408: `831c9315-e78...`](#1408) — single-answer, 정답: C6
10. [문제 1409: `d87e7bd8-347...`](#1409) — single-answer, 정답: C18

---

### 문제 1400: `5319d6f4-a8d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5319d6f4-a8d5-4272-8842-03ba2680394c` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241133_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1400] topology](images/train_1400.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3225062_3 by 3 degrees
- `C2`: Decrease transmission power for 3225062_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225062_3
- `C4`: Increase transmission power for 3225062_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241133_6
- `C6`: Adjust the azimuth of 3225062_3 by 38 degrees
- `C7`: Lift the tilt angle of 3241133_6 by 1 degrees
- `C8`: Press down the tilt angle  of 3225062_3 by 3 degrees
- `C9`: Increase A3 Offset threshold for 3225062_3
- `C10`: Add neighbor relationship between 3252622_12 and 3225062_3
- `C11`: Decrease A3 Offset threshold for 3241133_6
- `C12`: Decrease transmission power for 3241133_6
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225062_3
- `C14`: Check test server and transmission issues
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Adjust the azimuth of 3241133_6 by 48 degrees
- `C17`: Decrease A3 Offset threshold for 3225062_3
- `C18`: Increase A3 Offset threshold for 3241133_6
- `C19`: Press down the tilt angle of 3241133_6 by 1 degrees
- `C20`: Increase transmission power for 3241133_6
- `C21`: Add neighbor relationship between 3241133_6 and 3225062_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241133_6 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.270 | MS1 | 121.4656745268 | 31.1446205164 | 894 | 504990 | -94.49 | 12.36 | 331.06 | 0.09 | 2.24 | 1595 |
| 2024-09-20 22:21:32.333 | MS1 | 121.4656667943 | 31.1446352244 | 944 | 504990 | -95.75 | 11.78 | 562.64 | 0.14 | 2.62 | 1592 |
| 2024-09-20 22:21:33.864 | MS1 | 121.4656739002 | 31.1446376155 | 188 | 504990 | -95.74 | 14.77 | 542.04 | 0.17 | 2.55 | 1567 |
| 2024-09-20 22:21:34.818 | MS1 | 121.4656711919 | 31.1446318299 | 991 | 152650 | -87.91 | 4.32 | 56.16 | 0.09 | 1.91 | 968 |
| 2024-09-20 22:21:35.267 | MS1 | 121.4656594884 | 31.1446330622 | 709 | 152650 | -96.75 | 7.75 | 88.99 | 0.01 | 1.77 | 932 |
| 2024-09-20 22:21:36.251 | MS1 | 121.4656624369 | 31.1446304102 | 23 | 152650 | -96.85 | 2.59 | 45.39 | 0.12 | 1.70 | 905 |
| 2024-09-20 22:21:37.473 | MS1 | 121.4656777908 | 31.1446378005 | 548 | 152650 | -88.86 | 3.14 | 47.78 | 0.08 | 1.73 | 975 |
| 2024-09-20 22:21:38.419 | MS1 | 121.4656722342 | 31.1446202211 | 991 | 152650 | -93.97 | 5.25 | 72.16 | 0.05 | 1.59 | 929 |
| 2024-09-20 22:21:39.520 | MS1 | 121.4656721797 | 31.1446217910 | 709 | 152650 | -94.63 | 2.92 | 67.46 | 0.07 | 1.64 | 944 |
| 2024-09-20 22:21:40.563 | MS1 | 121.4656610169 | 31.1446295892 | 23 | 152650 | -96.65 | 6.15 | 69.20 | 0.14 | 2.38 | 1563 |
| 2024-09-20 22:21:41.402 | MS1 | 121.4656752523 | 31.1446290144 | 548 | 152650 | -89.99 | 4.60 | 66.25 | 0.19 | 2.02 | 1562 |
| 2024-09-20 22:21:42.451 | MS1 | 121.4656737440 | 31.1446253482 | 991 | 152650 | -91.50 | 4.74 | 87.60 | 0.14 | 2.58 | 1576 |

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
| 3225062 | 3 | 121.4679057980 | 31.1545927168 | 153 | 2 | 7 | 22.7 | TDD | 303 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3226012 | 1 | 121.4664729755 | 31.1478026056 | 123 | 10 | 8 | 0.1 | TDD | 513 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3234531 | 13 | 121.4688718659 | 31.1523716333 | 157 | 11 | 12 | 13.4 | FDD | 991 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3237745 | 2 | 121.4695563976 | 31.1442598040 | 35 | 7 | 9 | 22.6 | TDD | 508 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3241133 | 6 | 121.4728574806 | 31.1465873973 | 300 | 0 | 9 | 12.3 | TDD | 894 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3241695 | 10 | 121.4711802866 | 31.1464175576 | 239 | 8 | 3 | 9.3 | FDD | 709 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3244550 | 8 | 121.4672828832 | 31.1516176257 | 329 | 3 | 7 | 10.0 | FDD | 801 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3244983 | 9 | 121.4660815549 | 31.1557046369 | 73 | 3 | 12 | 14.9 | FDD | 548 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3249328 | 5 | 121.4724636136 | 31.1472725092 | 358 | 6 | 2 | 24.3 | TDD | 188 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3252622 | 12 | 121.4658827351 | 31.1533250544 | 102 | 14 | 9 | 28.8 | FDD | 23 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3275520 | 11 | 121.4668486007 | 31.1527215056 | 248 | 13 | 2 | 19.1 | FDD | 174 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3276848 | 4 | 121.4660968195 | 31.1526745030 | 169 | 1 | 8 | 27.2 | TDD | 944 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3277795 | 7 | 121.4746859095 | 31.1483420032 | 246 | 13 | 5 | 12.4 | FDD | 129 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |

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
| 2024-09-20 22:21:31.434 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.454 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.577 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.577 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.245 | NREventA2 | measId:1;ServCellPCI:408;Se... |
| 2024-09-20 22:21:35.347 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.637 | NREventA5 | measId:3;ServCellPCI:408;Se... |
| 2024-09-20 22:21:35.673 | NRHandoverAttempt | SourcePCI:408;SourceNR-ARFC... |
| 2024-09-20 22:21:35.717 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.731 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.872 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.872 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226012 | 1 | 19.2434 | 17.7900 | -115.5615 | 14.2601 | 88.6917 | 0.0064 | 0.0192 |
| 2024_09_20 22:00 | 3237745 | 2 | 18.0372 | 12.2279 | -117.0338 | 11.6027 | 170.0658 | 0.0070 | 0.0153 |
| 2024_09_20 22:00 | 3225062 | 3 | 8.3023 | 8.7897 | -114.4690 | 19.2139 | 161.4842 | 0.0079 | 0.0026 |
| 2024_09_20 22:00 | 3276848 | 4 | 15.4298 | 10.8285 | -117.5272 | 14.4706 | 191.9579 | 0.0092 | 0.0038 |
| 2024_09_20 22:00 | 3249328 | 5 | 19.0013 | 11.8681 | -116.5184 | 9.2378 | 169.9558 | 0.0185 | 0.0135 |
| 2024_09_20 22:00 | 3241133 | 6 | 10.3855 | 5.4146 | -116.8007 | 6.6782 | 126.6433 | 0.0159 | 0.0078 |
| 2024_09_20 22:00 | 3277795 | 7 | 7.3323 | 8.4672 | -114.2887 | 4.7741 | 29.4908 | 0.0084 | 0.0075 |
| 2024_09_20 22:00 | 3244550 | 8 | 19.1188 | 9.7796 | -114.1032 | 4.6813 | 47.9330 | 0.0049 | 0.0078 |
| 2024_09_20 22:00 | 3244983 | 9 | 6.8072 | 8.3292 | -115.2316 | 4.0579 | 23.8055 | 0.0159 | 0.0198 |
| 2024_09_20 22:00 | 3241695 | 10 | 12.9441 | 11.0464 | -115.2661 | 3.5703 | 20.2388 | 0.0062 | 0.0176 |
| 2024_09_20 22:00 | 3275520 | 11 | 12.3023 | 11.9074 | -117.5281 | 3.1622 | 39.7457 | 0.0067 | 0.0116 |
| 2024_09_20 22:00 | 3252622 | 12 | 5.2754 | 12.1594 | -116.8456 | 4.6877 | 54.5573 | 0.0134 | 0.0112 |
| 2024_09_20 22:00 | 3234531 | 13 | 13.0503 | 8.0116 | -117.1291 | 4.4520 | 32.4377 | 0.0112 | 0.0117 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416901_34021081 | 152650 | 991 | -88.4 | 152650 | 129 | -90.4 | 152650 | 174 | -98.0 | 152650 | 801 |
| MR_1774416901_E2AF0BDF | 504990 | 188 | -96.6 | 504990 | 303 | -95.4 | 504990 | 508 | -91.9 | 504990 | 513 |
| MR_1774416901_11B3118A | 504990 | 188 | -95.3 | 504990 | 303 | -95.5 | 504990 | 508 | -93.8 | 504990 | 513 |
| MR_1774416901_C8DD3B76 | 504990 | 188 | -96.9 | 504990 | 303 | -92.9 | 504990 | 508 | -92.4 | 504990 | 513 |
| MR_1774416901_10380E5D | 152650 | 991 | -86.1 | 152650 | 129 | -91.6 | 152650 | 174 | -96.0 | 152650 | 801 |
| MR_1774416901_CB5873DB | 152650 | 991 | -87.2 | 152650 | 129 | -89.0 | 152650 | 174 | -97.2 | 152650 | 801 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1401: `31a67c8e-3be...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `31a67c8e-3be1-452f-9075-dedde71d7b2e` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1401] topology](images/train_1401.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3244866_3 by 10 degrees
- `C2`: Increase transmission power for 3244866_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244866_3
- `C4`: Decrease transmission power for 3244866_3
- `C5`: Increase transmission power for 3237668_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237668_1
- `C7`: Adjust the azimuth of 3237668_1 by 50 degrees
- `C8`: Add neighbor relationship between 3248822_2 and 3244866_3
- `C9`: Increase A3 Offset threshold for 3237668_1
- `C10`: Press down the tilt angle of 3237668_1 by 10 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease A3 Offset threshold for 3244866_3
- `C13`: Decrease transmission power for 3237668_1
- `C14`: Add neighbor relationship between 3237668_1 and 3244866_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244866_3
- `C16`: Increase A3 Offset threshold for 3244866_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237668_1
- `C18`: Adjust the azimuth of 3244866_3 by 4 degrees
- `C19`: Decrease A3 Offset threshold for 3237668_1
- `C20`: Press down the tilt angle  of 3244866_3 by 10 degrees
- `C21`: Lift the tilt angle of 3237668_1 by 10 degrees
- `C22`: Check test server and transmission issues **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.964 | MS1 | 121.4656659776 | 31.1446360368 | 202 | 504990 | -85.62 | 16.21 | 450.71 | 0.02 | 2.13 | 1567 |
| 2024-09-20 22:21:32.386 | MS1 | 121.4656682292 | 31.1446338563 | 202 | 504990 | -89.88 | 13.58 | 325.73 | 0.08 | 2.20 | 1578 |
| 2024-09-20 22:21:33.736 | MS1 | 121.4656695470 | 31.1446182772 | 202 | 504990 | -85.06 | 15.31 | 391.84 | 0.12 | 2.44 | 1562 |
| 2024-09-20 22:21:34.211 | MS1 | 121.4656753940 | 31.1446305429 | 202 | 504990 | -89.78 | 17.55 | 72.68 | 0.11 | 2.06 | 347 |
| 2024-09-20 22:21:35.994 | MS1 | 121.4656586473 | 31.1446328491 | 202 | 504990 | -90.52 | 12.68 | 51.92 | 0.18 | 2.84 | 500 |
| 2024-09-20 22:21:36.339 | MS1 | 121.4656709393 | 31.1446345990 | 202 | 504990 | -86.35 | 16.56 | 87.47 | 0.11 | 2.30 | 440 |
| 2024-09-20 22:21:37.350 | MS1 | 121.4656728575 | 31.1446369059 | 202 | 504990 | -92.07 | 8.36 | 97.73 | 0.07 | 2.21 | 458 |
| 2024-09-20 22:21:38.544 | MS1 | 121.4656650773 | 31.1446221755 | 202 | 504990 | -89.07 | 12.57 | 43.82 | 0.03 | 2.63 | 412 |
| 2024-09-20 22:21:39.563 | MS1 | 121.4656666994 | 31.1446266834 | 202 | 504990 | -93.44 | 10.92 | 61.65 | 0.19 | 2.58 | 396 |
| 2024-09-20 22:21:40.160 | MS1 | 121.4656626497 | 31.1446338497 | 202 | 504990 | -90.10 | 12.99 | 404.94 | 0.07 | 2.51 | 1562 |
| 2024-09-20 22:21:41.105 | MS1 | 121.4656592994 | 31.1446298434 | 202 | 504990 | -93.57 | 10.25 | 307.38 | 0.09 | 2.97 | 1598 |
| 2024-09-20 22:21:42.804 | MS1 | 121.4656716970 | 31.1446184074 | 202 | 504990 | -92.57 | 9.78 | 584.96 | 0.01 | 2.53 | 1582 |

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
| 3213878 | 4 | 121.4650026026 | 31.1502153949 | 189 | 8 | 3 | 17.6 | TDD | 459 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3237668 | 1 | 121.4728232792 | 31.1441091691 | 164 | 14 | 4 | 49.5 | TDD | 202 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3244866 | 3 | 121.4656805301 | 31.1543329678 | 176 | 12 | 8 | 21.8 | TDD | 766 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3248822 | 2 | 121.4703854423 | 31.1549431247 | 141 | 3 | 1 | 16.0 | TDD | 475 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.344 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.365 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.488 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.488 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.234 | NREventA3 | measId:2;ServCellPCI:955;Se... |
| 2024-09-20 22:21:38.474 | NRHandoverAttempt | SourcePCI:955;SourceNR-ARFC... |
| 2024-09-20 22:21:38.513 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.524 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.624 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.624 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237668 | 1 | 10.2815 | 15.5537 | -115.9878 | 18.6144 | 193.2457 | 0.0043 | 0.0080 |
| 2024_09_20 22:00 | 3248822 | 2 | 6.0509 | 14.2098 | -114.6792 | 7.9985 | 193.6449 | 0.0103 | 0.0132 |
| 2024_09_20 22:00 | 3244866 | 3 | 17.8176 | 19.5187 | -117.7750 | 18.9992 | 96.4755 | 0.0011 | 0.0141 |
| 2024_09_20 22:00 | 3213878 | 4 | 15.6260 | 6.4063 | -114.6197 | 9.8280 | 98.5633 | 0.0150 | 0.0058 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412391_A5FAFE6D | 504990 | 202 | -90.0 | 504990 | 766 | -100.6 | 504990 | 475 | -99.2 | 504990 | 459 |
| MR_1774412391_5AE313B0 | 504990 | 202 | -88.4 | 504990 | 766 | -100.2 | 504990 | 475 | -99.1 | 504990 | 459 |
| MR_1774412391_FA6C6298 | 504990 | 202 | -89.9 | 504990 | 766 | -98.6 | 504990 | 475 | -99.8 | 504990 | 459 |
| MR_1774412391_D7AE301D | 504990 | 202 | -91.2 | 504990 | 766 | -100.7 | 504990 | 475 | -97.9 | 504990 | 459 |
| MR_1774412391_204710CD | 504990 | 202 | -91.5 | 504990 | 766 | -99.2 | 504990 | 475 | -100.7 | 504990 | 459 |
| MR_1774412391_3C574483 | 504990 | 202 | -88.1 | 504990 | 766 | -98.4 | 504990 | 475 | -101.4 | 504990 | 459 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1402: `5c40b895-1d7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5c40b895-1d7d-4d4c-a24e-68ee6118cc15` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1402] topology](images/train_1402.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3255623_4
- `C2`: Press down the tilt angle  of 3255623_4 by 10 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228578_2
- `C4`: Increase transmission power for 3228578_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255623_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228578_2
- `C7`: Decrease A3 Offset threshold for 3255623_4
- `C8`: Lift the tilt angle of 3228578_2 by 10 degrees
- `C9`: Press down the tilt angle of 3228578_2 by 10 degrees
- `C10`: Add neighbor relationship between 3226706_3 and 3255623_4
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Add neighbor relationship between 3228578_2 and 3255623_4
- `C13`: Decrease A3 Offset threshold for 3228578_2
- `C14`: Check test server and transmission issues **← 정답**
- `C15`: Increase A3 Offset threshold for 3228578_2
- `C16`: Decrease transmission power for 3228578_2
- `C17`: Increase transmission power for 3255623_4
- `C18`: Increase A3 Offset threshold for 3255623_4
- `C19`: Adjust the azimuth of 3255623_4 by 50 degrees
- `C20`: Adjust the azimuth of 3228578_2 by 50 degrees
- `C21`: Lift the tilt angle  of 3255623_4 by 10 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255623_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.961 | MS1 | 121.4656642063 | 31.1446251176 | 474 | 504990 | -90.22 | 12.89 | 329.55 | 0.07 | 2.77 | 1567 |
| 2024-09-20 22:21:32.158 | MS1 | 121.4656723500 | 31.1446319521 | 474 | 504990 | -87.57 | 12.85 | 589.15 | 0.19 | 2.67 | 1595 |
| 2024-09-20 22:21:33.921 | MS1 | 121.4656687171 | 31.1446342269 | 474 | 504990 | -86.33 | 17.22 | 520.91 | 0.09 | 2.08 | 1567 |
| 2024-09-20 22:21:34.938 | MS1 | 121.4656657836 | 31.1446297589 | 474 | 504990 | -86.40 | 16.69 | 74.78 | 0.06 | 2.27 | 487 |
| 2024-09-20 22:21:35.633 | MS1 | 121.4656667334 | 31.1446349297 | 474 | 504990 | -85.08 | 13.99 | 49.25 | 0.06 | 2.58 | 407 |
| 2024-09-20 22:21:36.998 | MS1 | 121.4656599857 | 31.1446264082 | 474 | 504990 | -87.05 | 14.80 | 97.53 | 0.15 | 2.65 | 396 |
| 2024-09-20 22:21:37.171 | MS1 | 121.4656737667 | 31.1446271186 | 474 | 504990 | -93.16 | 8.74 | 81.06 | 0.15 | 2.20 | 494 |
| 2024-09-20 22:21:38.545 | MS1 | 121.4656590972 | 31.1446234776 | 474 | 504990 | -91.30 | 9.11 | 79.01 | 0.19 | 2.50 | 446 |
| 2024-09-20 22:21:39.753 | MS1 | 121.4656704228 | 31.1446206123 | 474 | 504990 | -93.15 | 8.92 | 71.13 | 0.14 | 2.33 | 485 |
| 2024-09-20 22:21:40.499 | MS1 | 121.4656622077 | 31.1446283208 | 474 | 504990 | -93.94 | 9.66 | 391.02 | 0.16 | 2.94 | 1560 |
| 2024-09-20 22:21:41.837 | MS1 | 121.4656590449 | 31.1446340589 | 474 | 504990 | -91.68 | 10.91 | 442.52 | 0.09 | 2.58 | 1599 |
| 2024-09-20 22:21:42.937 | MS1 | 121.4656726229 | 31.1446254857 | 474 | 504990 | -90.75 | 8.58 | 523.69 | 0.15 | 2.70 | 1570 |

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
| 3226706 | 3 | 121.4650474783 | 31.1527590778 | 154 | 3 | 9 | 46.9 | TDD | 643 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3228578 | 2 | 121.4712229251 | 31.1500872796 | 32 | 9 | 11 | 38.1 | TDD | 474 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3236301 | 1 | 121.4656676026 | 31.1441287128 | 30 | 10 | 5 | 29.1 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3255623 | 4 | 121.4675610540 | 31.1454568833 | 355 | 12 | 3 | 42.0 | TDD | 389 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.535 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.558 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.677 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.677 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.395 | NREventA3 | measId:2;ServCellPCI:446;Se... |
| 2024-09-20 22:21:38.635 | NRHandoverAttempt | SourcePCI:446;SourceNR-ARFC... |
| 2024-09-20 22:21:38.683 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.693 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.799 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.799 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236301 | 1 | 16.4755 | 6.9928 | -117.9677 | 6.1631 | 88.4965 | 0.0041 | 0.0138 |
| 2024_09_20 22:00 | 3228578 | 2 | 17.4047 | 5.9971 | -117.5289 | 18.8169 | 134.1579 | 0.0085 | 0.0002 |
| 2024_09_20 22:00 | 3226706 | 3 | 9.0888 | 19.2219 | -115.1832 | 7.7670 | 105.8492 | 0.0105 | 0.0035 |
| 2024_09_20 22:00 | 3255623 | 4 | 19.2308 | 15.9052 | -115.9789 | 12.1900 | 153.2944 | 0.0180 | 0.0176 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416427_D474764E | 504990 | 474 | -85.3 | 504990 | 389 | -96.1 | 504990 | 643 | -94.9 | 504990 | 129 |
| MR_1774416427_854CE603 | 504990 | 474 | -87.1 | 504990 | 389 | -94.6 | 504990 | 643 | -94.1 | 504990 | 129 |
| MR_1774416427_065D2E93 | 504990 | 474 | -87.6 | 504990 | 389 | -93.8 | 504990 | 643 | -97.4 | 504990 | 129 |
| MR_1774416427_5023D633 | 504990 | 474 | -87.1 | 504990 | 389 | -94.0 | 504990 | 643 | -94.2 | 504990 | 129 |
| MR_1774416427_9D807CD2 | 504990 | 474 | -86.3 | 504990 | 389 | -94.5 | 504990 | 643 | -95.3 | 504990 | 129 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1403: `38714a94-d69...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `38714a94-d69b-49e7-9a63-cd9b7c711b59` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease A3 Offset threshold for 3274889_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1403] topology](images/train_1403.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3274889_4 by 10 degrees
- `C2`: Lift the tilt angle of 3274889_4 by 10 degrees
- `C3`: Decrease A3 Offset threshold for 3274889_4 **← 정답**
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226115_1
- `C5`: Increase transmission power for 3274889_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274889_4
- `C7`: Increase A3 Offset threshold for 3274889_4
- `C8`: Press down the tilt angle  of 3226115_1 by 10 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226115_1
- `C10`: Increase transmission power for 3226115_1
- `C11`: Adjust the azimuth of 3226115_1 by 19 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Lift the tilt angle  of 3226115_1 by 10 degrees
- `C14`: Increase A3 Offset threshold for 3226115_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274889_4
- `C16`: Adjust the azimuth of 3274889_4 by 3 degrees
- `C17`: Decrease transmission power for 3226115_1
- `C18`: Check test server and transmission issues
- `C19`: Add neighbor relationship between 3258878_3 and 3226115_1
- `C20`: Add neighbor relationship between 3274889_4 and 3226115_1
- `C21`: Decrease A3 Offset threshold for 3226115_1
- `C22`: Decrease transmission power for 3274889_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.139 | MS1 | 121.4656728708 | 31.1446268382 | 683 | 504990 | -77.29 | 15.96 | 526.61 | 0.07 | 2.17 | 1584 |
| 2024-09-20 22:21:32.892 | MS1 | 121.4656589817 | 31.1446246648 | 683 | 504990 | -77.77 | 16.57 | 533.32 | 0.07 | 2.30 | 1579 |
| 2024-09-20 22:21:33.686 | MS1 | 121.4656718482 | 31.1446223883 | 683 | 504990 | -80.80 | 12.98 | 432.81 | 0.11 | 2.62 | 1594 |
| 2024-09-20 22:21:34.160 | MS1 | 121.4656632187 | 31.1446221808 | 683 | 504990 | -92.75 | -1.98 | 39.21 | 0.03 | 1.10 | 1579 |
| 2024-09-20 22:21:35.814 | MS1 | 121.4656672808 | 31.1446269485 | 683 | 504990 | -92.23 | -0.61 | 56.76 | 0.16 | 1.22 | 1592 |
| 2024-09-20 22:21:36.786 | MS1 | 121.4656587257 | 31.1446216253 | 683 | 504990 | -87.83 | -1.47 | 62.41 | 0.12 | 1.11 | 1584 |
| 2024-09-20 22:21:37.505 | MS1 | 121.4656755079 | 31.1446315727 | 683 | 504990 | -84.32 | -0.46 | 57.87 | 0.16 | 1.44 | 1594 |
| 2024-09-20 22:21:38.913 | MS1 | 121.4656610598 | 31.1446340114 | 683 | 504990 | -85.55 | -2.71 | 63.11 | 0.02 | 1.27 | 1586 |
| 2024-09-20 22:21:39.457 | MS1 | 121.4656700602 | 31.1446360865 | 258 | 504990 | -79.58 | 14.86 | 303.13 | 0.10 | 1.34 | 1578 |
| 2024-09-20 22:21:40.674 | MS1 | 121.4656742548 | 31.1446330066 | 258 | 504990 | -81.28 | 13.27 | 323.00 | 0.08 | 2.04 | 1593 |
| 2024-09-20 22:21:41.230 | MS1 | 121.4656740062 | 31.1446321348 | 258 | 504990 | -77.09 | 17.40 | 573.05 | 0.06 | 2.41 | 1579 |
| 2024-09-20 22:21:42.139 | MS1 | 121.4656671559 | 31.1446361012 | 258 | 504990 | -80.51 | 12.53 | 414.94 | 0.17 | 2.39 | 1567 |

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
| 3226115 | 1 | 121.4729447538 | 31.1542971398 | 194 | 11 | 4 | 22.1 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3249959 | 2 | 121.4703800971 | 31.1474473574 | 196 | 8 | 11 | 34.6 | TDD | 371 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3258878 | 3 | 121.4643753379 | 31.1487978380 | 186 | 8 | 6 | 45.8 | TDD | 155 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3274889 | 4 | 121.4673334658 | 31.1462622236 | 224 | 10 | 4 | 37.0 | TDD | 683 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.339 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.356 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.505 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.505 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.219 | NREventA3 | measId:2;ServCellPCI:578;Se... |
| 2024-09-20 22:21:38.459 | NRHandoverAttempt | SourcePCI:578;SourceNR-ARFC... |
| 2024-09-20 22:21:38.499 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.511 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.655 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.655 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226115 | 1 | 14.6590 | 6.5792 | -116.0915 | 8.3629 | 89.8830 | 0.0052 | 0.0182 |
| 2024_09_20 22:00 | 3249959 | 2 | 19.3477 | 9.8332 | -114.4848 | 9.9300 | 190.5163 | 0.0136 | 0.0124 |
| 2024_09_20 22:00 | 3258878 | 3 | 12.6986 | 8.6979 | -116.1671 | 14.2595 | 159.3469 | 0.0192 | 0.0145 |
| 2024_09_20 22:00 | 3274889 | 4 | 19.2094 | 9.7534 | -114.3882 | 13.9013 | 123.1104 | 0.0154 | 0.1793 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416047_5169D055 | 504990 | 258 | -86.2 | 504990 | 683 | -91.9 | 504990 | 155 | -87.3 | 504990 | 371 |
| MR_1774416047_9C21EBA4 | 504990 | 683 | -93.5 | 504990 | 258 | -85.9 | 504990 | 155 | -88.4 | 504990 | 371 |
| MR_1774416047_2916CC0C | 504990 | 258 | -85.9 | 504990 | 683 | -92.3 | 504990 | 155 | -89.6 | 504990 | 371 |
| MR_1774416047_525C4D10 | 504990 | 683 | -93.7 | 504990 | 258 | -88.9 | 504990 | 155 | -86.9 | 504990 | 371 |
| MR_1774416047_647835D2 | 504990 | 683 | -92.3 | 504990 | 258 | -88.6 | 504990 | 155 | -86.4 | 504990 | 371 |
| MR_1774416047_5C242860 | 504990 | 683 | -93.4 | 504990 | 258 | -89.1 | 504990 | 155 | -89.7 | 504990 | 371 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1404: `39b42f1a-947...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `39b42f1a-9476-47f5-a896-c02a35770200` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Lift the tilt angle  of 3229880_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1404] topology](images/train_1404.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase A3 Offset threshold for 3247450_3
- `C3`: Increase transmission power for 3247450_3
- `C4`: Add neighbor relationship between 3229880_1 and 3247450_3
- `C5`: Lift the tilt angle  of 3229880_1 by 10 degrees **← 정답**
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247450_3
- `C7`: Press down the tilt angle  of 3229880_1 by 10 degrees
- `C8`: Decrease transmission power for 3247450_3
- `C9`: Decrease transmission power for 3228263_4
- `C10`: Adjust the azimuth of 3228263_4 by 21 degrees
- `C11`: Increase A3 Offset threshold for 3228263_4
- `C12`: Add neighbor relationship between 3228263_4 and 3247450_3
- `C13`: Press down the tilt angle of 3228263_4 by 4 degrees
- `C14`: Decrease A3 Offset threshold for 3247450_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228263_4
- `C16`: Increase transmission power for 3228263_4
- `C17`: Adjust the azimuth of 3229880_1 by 50 degrees
- `C18`: Check test server and transmission issues
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228263_4
- `C20`: Decrease A3 Offset threshold for 3228263_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247450_3
- `C22`: Lift the tilt angle of 3228263_4 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.263 | MS1 | 121.4656714053 | 31.1446255518 | 391 | 504990 | -88.86 | 17.31 | 588.09 | 0.04 | 2.27 | 1586 |
| 2024-09-20 22:21:32.299 | MS1 | 121.4656643369 | 31.1446266915 | 391 | 504990 | -89.80 | 16.53 | 559.33 | 0.01 | 2.04 | 1580 |
| 2024-09-20 22:21:33.580 | MS1 | 121.4656690012 | 31.1446224014 | 391 | 504990 | -88.86 | 15.42 | 442.95 | 0.07 | 2.36 | 1564 |
| 2024-09-20 22:21:34.473 | MS1 | 121.4656753521 | 31.1446256868 | 391 | 504990 | -85.60 | 14.58 | 66.59 | 0.11 | 2.82 | 1589 |
| 2024-09-20 22:21:35.156 | MS1 | 121.4656619519 | 31.1446291214 | 391 | 504990 | -88.63 | 16.68 | 67.54 | 0.06 | 2.51 | 1575 |
| 2024-09-20 22:21:36.881 | MS1 | 121.4656779234 | 31.1446278825 | 391 | 504990 | -88.67 | 16.03 | 59.18 | 0.13 | 2.33 | 1569 |
| 2024-09-20 22:21:37.611 | MS1 | 121.4656623591 | 31.1446315647 | 391 | 504990 | -93.61 | 12.68 | 54.15 | 0.01 | 2.87 | 1573 |
| 2024-09-20 22:21:38.695 | MS1 | 121.4656711417 | 31.1446250311 | 391 | 504990 | -89.74 | 9.77 | 87.19 | 0.07 | 2.26 | 1593 |
| 2024-09-20 22:21:39.445 | MS1 | 121.4656745687 | 31.1446341228 | 391 | 504990 | -93.93 | 10.11 | 56.59 | 0.03 | 2.45 | 1575 |
| 2024-09-20 22:21:40.313 | MS1 | 121.4656622219 | 31.1446310277 | 391 | 504990 | -93.30 | 12.07 | 372.91 | 0.03 | 2.29 | 1595 |
| 2024-09-20 22:21:41.720 | MS1 | 121.4656640960 | 31.1446280622 | 391 | 504990 | -93.39 | 8.61 | 520.45 | 0.17 | 2.97 | 1584 |
| 2024-09-20 22:21:42.903 | MS1 | 121.4656738427 | 31.1446294917 | 391 | 504990 | -92.44 | 7.97 | 556.54 | 0.15 | 2.98 | 1588 |

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
| 3228263 | 4 | 121.4732236549 | 31.1475957908 | 224 | 2 | 12 | 31.2 | TDD | 391 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3229880 | 1 | 121.4743752511 | 31.1500980928 | 67 | 14 | 3 | 42.8 | TDD | 219 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3236421 | 2 | 121.4717689390 | 31.1511212887 | 56 | 15 | 8 | 46.7 | TDD | 44 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3247450 | 3 | 121.4643667654 | 31.1465879026 | 68 | 13 | 12 | 21.8 | TDD | 101 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.827 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.852 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.954 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.954 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.656 | NREventA3 | measId:2;ServCellPCI:124;Se... |
| 2024-09-20 22:21:37.896 | NRHandoverAttempt | SourcePCI:124;SourceNR-ARFC... |
| 2024-09-20 22:21:37.939 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.949 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.071 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.071 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229880 | 1 | 10.6496 | 15.2168 | -116.9266 | 16.7216 | 162.9944 | 0.0049 | 0.0121 |
| 2024_09_20 22:00 | 3236421 | 2 | 7.7587 | 13.5452 | -115.3414 | 7.7808 | 170.1123 | 0.0189 | 0.0173 |
| 2024_09_20 22:00 | 3247450 | 3 | 6.7065 | 16.0146 | -114.5222 | 16.6099 | 192.9002 | 0.0059 | 0.0052 |
| 2024_09_20 22:00 | 3228263 | 4 | 84.0577 | 88.8761 | -116.2655 | 14.1692 | 152.1865 | 0.0160 | 0.0035 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412274_14F69493 | 504990 | 391 | -86.4 | 504990 | 101 | -89.7 | 504990 | 219 | -95.3 | 504990 | 44 |
| MR_1774412274_FB9F913C | 504990 | 391 | -84.1 | 504990 | 101 | -89.9 | 504990 | 219 | -94.5 | 504990 | 44 |
| MR_1774412274_5AF9B45F | 504990 | 391 | -85.5 | 504990 | 101 | -90.1 | 504990 | 219 | -98.1 | 504990 | 44 |
| MR_1774412274_1FA4D9C0 | 504990 | 391 | -87.6 | 504990 | 101 | -89.5 | 504990 | 219 | -97.3 | 504990 | 44 |
| MR_1774412274_372B22DC | 504990 | 391 | -86.0 | 504990 | 101 | -90.0 | 504990 | 219 | -95.7 | 504990 | 44 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1405: `c7c57306-e8d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c7c57306-e8d0-443b-982e-69edf249c771` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1405] topology](images/train_1405.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3277159_1
- `C2`: Check test server and transmission issues **← 정답**
- `C3`: Press down the tilt angle  of 3277159_1 by 10 degrees
- `C4`: Adjust the azimuth of 3267108_3 by 50 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277159_1
- `C6`: Decrease A3 Offset threshold for 3267108_3
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Press down the tilt angle of 3267108_3 by 10 degrees
- `C9`: Decrease A3 Offset threshold for 3277159_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267108_3
- `C11`: Add neighbor relationship between 3235527_2 and 3277159_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277159_1
- `C13`: Increase A3 Offset threshold for 3277159_1
- `C14`: Increase transmission power for 3267108_3
- `C15`: Decrease transmission power for 3277159_1
- `C16`: Lift the tilt angle of 3267108_3 by 10 degrees
- `C17`: Increase A3 Offset threshold for 3267108_3
- `C18`: Decrease transmission power for 3267108_3
- `C19`: Add neighbor relationship between 3267108_3 and 3277159_1
- `C20`: Lift the tilt angle  of 3277159_1 by 10 degrees
- `C21`: Adjust the azimuth of 3277159_1 by 16 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267108_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.461 | MS1 | 121.4656683446 | 31.1446325804 | 1004 | 504990 | -91.70 | 12.08 | 452.32 | 0.10 | 2.83 | 1577 |
| 2024-09-20 22:21:32.594 | MS1 | 121.4656699900 | 31.1446290610 | 1004 | 504990 | -87.85 | 15.80 | 543.22 | 0.15 | 2.89 | 1564 |
| 2024-09-20 22:21:33.602 | MS1 | 121.4656696302 | 31.1446334429 | 1004 | 504990 | -88.08 | 12.79 | 596.04 | 0.10 | 2.10 | 1589 |
| 2024-09-20 22:21:34.229 | MS1 | 121.4656775979 | 31.1446312664 | 1004 | 504990 | -86.50 | 16.96 | 67.00 | 0.19 | 2.31 | 425 |
| 2024-09-20 22:21:35.288 | MS1 | 121.4656718378 | 31.1446372322 | 1004 | 504990 | -90.00 | 17.15 | 67.54 | 0.06 | 2.40 | 370 |
| 2024-09-20 22:21:36.650 | MS1 | 121.4656772067 | 31.1446314511 | 1004 | 504990 | -90.09 | 17.18 | 93.18 | 0.13 | 2.71 | 320 |
| 2024-09-20 22:21:37.461 | MS1 | 121.4656751433 | 31.1446235412 | 1004 | 504990 | -91.26 | 10.19 | 64.58 | 0.15 | 2.34 | 497 |
| 2024-09-20 22:21:38.719 | MS1 | 121.4656727081 | 31.1446219786 | 1004 | 504990 | -89.34 | 10.43 | 75.72 | 0.02 | 2.33 | 447 |
| 2024-09-20 22:21:39.771 | MS1 | 121.4656694716 | 31.1446303888 | 1004 | 504990 | -93.58 | 11.25 | 66.53 | 0.06 | 2.06 | 411 |
| 2024-09-20 22:21:40.837 | MS1 | 121.4656666974 | 31.1446373314 | 1004 | 504990 | -90.49 | 9.22 | 533.62 | 0.01 | 2.17 | 1581 |
| 2024-09-20 22:21:41.884 | MS1 | 121.4656595181 | 31.1446346565 | 1004 | 504990 | -90.35 | 8.34 | 529.38 | 0.07 | 2.12 | 1565 |
| 2024-09-20 22:21:42.525 | MS1 | 121.4656600115 | 31.1446207688 | 1004 | 504990 | -93.97 | 7.41 | 317.29 | 0.08 | 2.77 | 1593 |

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
| 3218958 | 4 | 121.4734183514 | 31.1481065721 | 296 | 11 | 2 | 22.3 | TDD | 287 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3235527 | 2 | 121.4759783609 | 31.1484031223 | 269 | 10 | 9 | 22.6 | TDD | 676 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3267108 | 3 | 121.4710241975 | 31.1507978361 | 326 | 13 | 11 | 32.6 | TDD | 1004 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3277159 | 1 | 121.4689778574 | 31.1447457583 | 284 | 9 | 1 | 25.6 | TDD | 125 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.591 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.611 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.758 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.758 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.444 | NREventA3 | measId:2;ServCellPCI:366;Se... |
| 2024-09-20 22:21:38.684 | NRHandoverAttempt | SourcePCI:366;SourceNR-ARFC... |
| 2024-09-20 22:21:38.719 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.729 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.871 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.871 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277159 | 1 | 5.1730 | 5.5950 | -117.8948 | 15.7359 | 85.6514 | 0.0130 | 0.0140 |
| 2024_09_20 22:00 | 3235527 | 2 | 8.7388 | 18.2315 | -114.2599 | 14.4311 | 186.5933 | 0.0089 | 0.0062 |
| 2024_09_20 22:00 | 3267108 | 3 | 12.0123 | 11.5867 | -115.1919 | 17.2000 | 141.1136 | 0.0025 | 0.0089 |
| 2024_09_20 22:00 | 3218958 | 4 | 19.8127 | 16.7622 | -115.4851 | 17.6055 | 162.2074 | 0.0024 | 0.0181 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414118_7E459AF9 | 504990 | 1004 | -85.9 | 504990 | 125 | -91.9 | 504990 | 676 | -95.3 | 504990 | 287 |
| MR_1774414118_2607CE36 | 504990 | 1004 | -85.1 | 504990 | 125 | -94.3 | 504990 | 676 | -95.1 | 504990 | 287 |
| MR_1774414118_939A7ECE | 504990 | 1004 | -86.3 | 504990 | 125 | -92.3 | 504990 | 676 | -97.4 | 504990 | 287 |
| MR_1774414118_B0F7578C | 504990 | 1004 | -86.4 | 504990 | 125 | -90.8 | 504990 | 676 | -93.7 | 504990 | 287 |
| MR_1774414118_05C8F0E7 | 504990 | 1004 | -87.7 | 504990 | 125 | -93.3 | 504990 | 676 | -96.8 | 504990 | 287 |
| MR_1774414118_8389F8FC | 504990 | 1004 | -86.1 | 504990 | 125 | -93.4 | 504990 | 676 | -96.5 | 504990 | 287 |
| MR_1774414118_F76DEFE7 | 504990 | 1004 | -85.4 | 504990 | 125 | -92.4 | 504990 | 676 | -95.0 | 504990 | 287 |
| MR_1774414118_422F93FA | 504990 | 1004 | -84.6 | 504990 | 125 | -90.8 | 504990 | 676 | -96.5 | 504990 | 287 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1406: `64b36b49-71c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `64b36b49-71c7-446a-a56e-716d287be8f2` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1406] topology](images/train_1406.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3230388_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230388_2
- `C3`: Decrease A3 Offset threshold for 3252668_4
- `C4`: Decrease A3 Offset threshold for 3230388_2
- `C5`: Lift the tilt angle  of 3252668_4 by 10 degrees
- `C6`: Increase A3 Offset threshold for 3252668_4
- `C7`: Add neighbor relationship between 3230388_2 and 3252668_4
- `C8`: Lift the tilt angle of 3230388_2 by 10 degrees
- `C9`: Decrease transmission power for 3252668_4
- `C10`: Adjust the azimuth of 3252668_4 by 50 degrees
- `C11`: Increase transmission power for 3252668_4
- `C12`: Press down the tilt angle  of 3252668_4 by 10 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252668_4
- `C14`: Check test server and transmission issues **← 정답**
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252668_4
- `C16`: Increase A3 Offset threshold for 3230388_2
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Press down the tilt angle of 3230388_2 by 10 degrees
- `C19`: Increase transmission power for 3230388_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230388_2
- `C21`: Adjust the azimuth of 3230388_2 by 30 degrees
- `C22`: Add neighbor relationship between 3213598_3 and 3252668_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.941 | MS1 | 121.4656604533 | 31.1446281497 | 843 | 504990 | -88.07 | 16.99 | 425.11 | 0.09 | 2.47 | 1589 |
| 2024-09-20 22:21:32.547 | MS1 | 121.4656773077 | 31.1446333137 | 843 | 504990 | -89.00 | 16.86 | 558.17 | 0.09 | 2.07 | 1569 |
| 2024-09-20 22:21:33.804 | MS1 | 121.4656642573 | 31.1446376317 | 843 | 504990 | -89.08 | 15.64 | 394.49 | 0.18 | 2.98 | 1594 |
| 2024-09-20 22:21:34.127 | MS1 | 121.4656705459 | 31.1446318626 | 843 | 504990 | -91.87 | 15.42 | 79.27 | 0.09 | 2.77 | 400 |
| 2024-09-20 22:21:35.983 | MS1 | 121.4656606855 | 31.1446241040 | 843 | 504990 | -87.91 | 15.96 | 92.59 | 0.09 | 2.50 | 452 |
| 2024-09-20 22:21:36.537 | MS1 | 121.4656682360 | 31.1446322646 | 843 | 504990 | -90.46 | 14.68 | 96.66 | 0.17 | 2.64 | 462 |
| 2024-09-20 22:21:37.857 | MS1 | 121.4656635134 | 31.1446285066 | 843 | 504990 | -93.48 | 8.59 | 59.49 | 0.17 | 2.27 | 497 |
| 2024-09-20 22:21:38.763 | MS1 | 121.4656673707 | 31.1446372772 | 843 | 504990 | -89.26 | 9.04 | 95.13 | 0.13 | 2.00 | 379 |
| 2024-09-20 22:21:39.509 | MS1 | 121.4656631628 | 31.1446261710 | 843 | 504990 | -93.60 | 8.33 | 91.49 | 0.06 | 2.09 | 457 |
| 2024-09-20 22:21:40.599 | MS1 | 121.4656632064 | 31.1446217457 | 843 | 504990 | -92.04 | 9.51 | 299.24 | 0.10 | 2.52 | 1600 |
| 2024-09-20 22:21:41.840 | MS1 | 121.4656740288 | 31.1446206562 | 843 | 504990 | -90.07 | 11.22 | 591.94 | 0.03 | 2.82 | 1580 |
| 2024-09-20 22:21:42.716 | MS1 | 121.4656766580 | 31.1446328707 | 843 | 504990 | -91.77 | 8.89 | 433.21 | 0.09 | 2.92 | 1571 |

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
| 3213598 | 3 | 121.4752814497 | 31.1521627614 | 130 | 8 | 9 | 16.5 | TDD | 587 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3224590 | 1 | 121.4736905763 | 31.1462599358 | 152 | 12 | 9 | 37.9 | TDD | 865 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3230388 | 2 | 121.4714736997 | 31.1547819059 | 176 | 12 | 10 | 46.9 | TDD | 843 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3252668 | 4 | 121.4699253427 | 31.1445863686 | 202 | 8 | 7 | 25.4 | TDD | 853 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.106 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.126 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.244 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.244 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.925 | NREventA3 | measId:2;ServCellPCI:995;Se... |
| 2024-09-20 22:21:38.165 | NRHandoverAttempt | SourcePCI:995;SourceNR-ARFC... |
| 2024-09-20 22:21:38.201 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.215 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.363 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.363 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224590 | 1 | 12.3032 | 10.3441 | -117.7670 | 16.1553 | 143.0436 | 0.0117 | 0.0148 |
| 2024_09_20 22:00 | 3230388 | 2 | 17.5426 | 15.2991 | -117.0770 | 9.3514 | 139.2959 | 0.0070 | 0.0008 |
| 2024_09_20 22:00 | 3213598 | 3 | 11.2832 | 14.2572 | -114.8590 | 14.7628 | 104.4243 | 0.0117 | 0.0127 |
| 2024_09_20 22:00 | 3252668 | 4 | 18.3407 | 10.1086 | -116.2452 | 5.3221 | 136.9320 | 0.0024 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412899_A971E4DE | 504990 | 843 | -92.5 | 504990 | 853 | -96.8 | 504990 | 587 | -102.8 | 504990 | 865 |
| MR_1774412899_181BAAE3 | 504990 | 843 | -91.9 | 504990 | 853 | -96.8 | 504990 | 587 | -100.3 | 504990 | 865 |
| MR_1774412899_92B71E83 | 504990 | 843 | -91.6 | 504990 | 853 | -95.9 | 504990 | 587 | -103.0 | 504990 | 865 |
| MR_1774412899_6ED3FCEF | 504990 | 843 | -90.7 | 504990 | 853 | -94.1 | 504990 | 587 | -102.1 | 504990 | 865 |
| MR_1774412899_CA7CD61D | 504990 | 843 | -90.7 | 504990 | 853 | -95.0 | 504990 | 587 | -102.9 | 504990 | 865 |
| MR_1774412899_05567057 | 504990 | 843 | -90.3 | 504990 | 853 | -95.2 | 504990 | 587 | -103.6 | 504990 | 865 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1407: `e210dde1-649...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e210dde1-6494-45c5-a90d-2762b54830c4` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3222202_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1407] topology](images/train_1407.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3222202_4 by 36 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222202_4 **← 정답**
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264309_1
- `C4`: Add neighbor relationship between 3222202_4 and 3264309_1
- `C5`: Increase transmission power for 3222202_4
- `C6`: Press down the tilt angle of 3222202_4 by 2 degrees
- `C7`: Increase transmission power for 3264309_1
- `C8`: Decrease A3 Offset threshold for 3222202_4
- `C9`: Check test server and transmission issues
- `C10`: Increase A3 Offset threshold for 3264309_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264309_1
- `C12`: Adjust the azimuth of 3264309_1 by 50 degrees
- `C13`: Decrease transmission power for 3222202_4
- `C14`: Increase A3 Offset threshold for 3222202_4
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Add neighbor relationship between 3277793_3 and 3264309_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222202_4
- `C18`: Press down the tilt angle  of 3264309_1 by 10 degrees
- `C19`: Decrease transmission power for 3264309_1
- `C20`: Decrease A3 Offset threshold for 3264309_1
- `C21`: Lift the tilt angle of 3222202_4 by 2 degrees
- `C22`: Lift the tilt angle  of 3264309_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.807 | MS1 | 121.4656758278 | 31.1446276496 | 254 | 504990 | -87.91 | 16.60 | 364.00 | 0.18 | 2.91 | 1565 |
| 2024-09-20 22:21:32.555 | MS1 | 121.4656695950 | 31.1446343019 | 254 | 504990 | -90.99 | 12.20 | 311.98 | 0.11 | 2.17 | 1575 |
| 2024-09-20 22:21:33.319 | MS1 | 121.4656776799 | 31.1446204409 | 254 | 504990 | -86.22 | 15.68 | 368.33 | 0.11 | 2.95 | 1585 |
| 2024-09-20 22:21:34.120 | MS1 | 121.4656773231 | 31.1446265879 | 254 | 504990 | -90.77 | 12.61 | 80.89 | 0.64 | 2.85 | 608 |
| 2024-09-20 22:21:35.181 | MS1 | 121.4656696649 | 31.1446256348 | 254 | 504990 | -87.70 | 17.26 | 54.24 | 0.54 | 2.39 | 697 |
| 2024-09-20 22:21:36.888 | MS1 | 121.4656647681 | 31.1446367827 | 254 | 504990 | -85.58 | 14.66 | 100.53 | 0.65 | 2.38 | 510 |
| 2024-09-20 22:21:37.693 | MS1 | 121.4656691812 | 31.1446308439 | 254 | 504990 | -91.01 | 12.39 | 81.90 | 0.54 | 2.38 | 667 |
| 2024-09-20 22:21:38.552 | MS1 | 121.4656659421 | 31.1446253382 | 254 | 504990 | -91.23 | 10.69 | 48.65 | 0.56 | 2.25 | 596 |
| 2024-09-20 22:21:39.317 | MS1 | 121.4656716503 | 31.1446279553 | 254 | 504990 | -90.03 | 7.18 | 54.17 | 0.69 | 2.12 | 598 |
| 2024-09-20 22:21:40.737 | MS1 | 121.4656719095 | 31.1446264886 | 254 | 504990 | -89.70 | 9.43 | 395.15 | 0.01 | 2.83 | 1587 |
| 2024-09-20 22:21:41.586 | MS1 | 121.4656581183 | 31.1446307606 | 254 | 504990 | -93.28 | 7.65 | 570.32 | 0.09 | 2.27 | 1569 |
| 2024-09-20 22:21:42.404 | MS1 | 121.4656759473 | 31.1446294374 | 254 | 504990 | -89.41 | 11.96 | 341.12 | 0.06 | 2.46 | 1563 |

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
| 3222202 | 4 | 121.4701037536 | 31.1532931347 | 168 | 0 | 3 | 34.2 | TDD | 254 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3247707 | 2 | 121.4643343520 | 31.1476819070 | 113 | 13 | 4 | 46.0 | TDD | 418 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3264309 | 1 | 121.4747997057 | 31.1529010194 | 330 | 10 | 8 | 39.0 | TDD | 121 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3277793 | 3 | 121.4666493210 | 31.1472185267 | 73 | 11 | 1 | 28.8 | TDD | 562 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.106 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.128 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.230 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.230 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.959 | NREventA3 | measId:2;ServCellPCI:138;Se... |
| 2024-09-20 22:21:38.199 | NRHandoverAttempt | SourcePCI:138;SourceNR-ARFC... |
| 2024-09-20 22:21:38.230 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.241 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.349 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.349 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264309 | 1 | 11.1851 | 11.8846 | -117.8626 | 11.6566 | 121.7097 | 0.0114 | 0.0030 |
| 2024_09_20 22:00 | 3247707 | 2 | 16.0416 | 16.8515 | -114.7618 | 14.4827 | 128.8603 | 0.0007 | 0.0142 |
| 2024_09_20 22:00 | 3277793 | 3 | 12.0440 | 13.7078 | -115.8624 | 18.9481 | 130.3186 | 0.0028 | 0.0138 |
| 2024_09_20 22:00 | 3222202 | 4 | 11.8410 | 17.0712 | -114.1493 | 10.2125 | 195.0845 | 0.0134 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414420_A60171DB | 504990 | 254 | -90.4 | 504990 | 121 | -96.0 | 504990 | 562 | -102.2 | 504990 | 418 |
| MR_1774414420_034BC217 | 504990 | 254 | -91.4 | 504990 | 121 | -97.5 | 504990 | 562 | -102.8 | 504990 | 418 |
| MR_1774414420_343BDC13 | 504990 | 254 | -90.9 | 504990 | 121 | -95.6 | 504990 | 562 | -104.7 | 504990 | 418 |
| MR_1774414420_F14DFC5D | 504990 | 254 | -89.7 | 504990 | 121 | -97.9 | 504990 | 562 | -104.3 | 504990 | 418 |
| MR_1774414420_B9A7DE8B | 504990 | 254 | -89.0 | 504990 | 121 | -97.3 | 504990 | 562 | -104.4 | 504990 | 418 |
| MR_1774414420_AA243DBF | 504990 | 254 | -89.9 | 504990 | 121 | -95.8 | 504990 | 562 | -105.8 | 504990 | 418 |
| MR_1774414420_BF262D19 | 504990 | 254 | -90.2 | 504990 | 121 | -96.0 | 504990 | 562 | -105.1 | 504990 | 418 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1408: `831c9315-e78...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `831c9315-e78b-4153-8060-c48fed78c219` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223333_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1408] topology](images/train_1408.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3223333_5 by 5 degrees
- `C2`: Adjust the azimuth of 3212147_4 by 36 degrees
- `C3`: Increase transmission power for 3223333_5
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223333_5
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223333_5 **← 정답**
- `C7`: Increase transmission power for 3212147_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212147_4
- `C9`: Decrease transmission power for 3212147_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212147_4
- `C11`: Increase A3 Offset threshold for 3212147_4
- `C12`: Press down the tilt angle  of 3212147_4 by 6 degrees
- `C13`: Check test server and transmission issues
- `C14`: Decrease A3 Offset threshold for 3212147_4
- `C15`: Lift the tilt angle of 3223333_5 by 5 degrees
- `C16`: Add neighbor relationship between 3253209_11 and 3212147_4
- `C17`: Add neighbor relationship between 3223333_5 and 3212147_4
- `C18`: Lift the tilt angle  of 3212147_4 by 6 degrees
- `C19`: Decrease transmission power for 3223333_5
- `C20`: Decrease A3 Offset threshold for 3223333_5
- `C21`: Adjust the azimuth of 3223333_5 by 45 degrees
- `C22`: Increase A3 Offset threshold for 3223333_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.125 | MS1 | 121.4656591458 | 31.1446236474 | 280 | 504990 | -95.70 | 10.01 | 319.62 | 0.18 | 2.34 | 1589 |
| 2024-09-20 22:21:32.936 | MS1 | 121.4656642173 | 31.1446271679 | 771 | 504990 | -95.01 | 10.86 | 384.49 | 0.16 | 2.44 | 1583 |
| 2024-09-20 22:21:33.328 | MS1 | 121.4656736653 | 31.1446357721 | 218 | 504990 | -93.22 | 14.95 | 594.81 | 0.19 | 2.61 | 1587 |
| 2024-09-20 22:21:34.640 | MS1 | 121.4656653448 | 31.1446294435 | 994 | 152650 | -89.24 | 4.57 | 77.58 | 0.07 | 1.64 | 907 |
| 2024-09-20 22:21:35.534 | MS1 | 121.4656695055 | 31.1446181257 | 847 | 152650 | -95.95 | 5.62 | 58.19 | 0.08 | 1.74 | 949 |
| 2024-09-20 22:21:36.276 | MS1 | 121.4656615006 | 31.1446368419 | 429 | 152650 | -89.04 | 4.06 | 58.04 | 0.15 | 1.50 | 906 |
| 2024-09-20 22:21:37.603 | MS1 | 121.4656662481 | 31.1446370405 | 744 | 152650 | -88.97 | 4.80 | 76.45 | 0.10 | 1.50 | 927 |
| 2024-09-20 22:21:38.771 | MS1 | 121.4656607459 | 31.1446362397 | 994 | 152650 | -89.90 | 6.52 | 60.92 | 0.19 | 1.91 | 932 |
| 2024-09-20 22:21:39.754 | MS1 | 121.4656745823 | 31.1446251165 | 847 | 152650 | -90.08 | 2.38 | 60.52 | 0.04 | 1.67 | 945 |
| 2024-09-20 22:21:40.590 | MS1 | 121.4656712778 | 31.1446284200 | 429 | 152650 | -96.14 | 7.30 | 61.85 | 0.02 | 2.05 | 1587 |
| 2024-09-20 22:21:41.401 | MS1 | 121.4656763070 | 31.1446324167 | 744 | 152650 | -91.11 | 5.17 | 64.96 | 0.09 | 2.96 | 1574 |
| 2024-09-20 22:21:42.281 | MS1 | 121.4656625526 | 31.1446314526 | 994 | 152650 | -96.61 | 6.74 | 94.98 | 0.01 | 2.22 | 1597 |

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
| 3212147 | 4 | 121.4727856703 | 31.1502743356 | 191 | 5 | 12 | 10.9 | TDD | 912 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3217407 | 1 | 121.4710486951 | 31.1540693317 | 162 | 4 | 2 | 16.9 | TDD | 771 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3219603 | 7 | 121.4702154268 | 31.1470268641 | 265 | 7 | 0 | 4.0 | FDD | 994 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3223333 | 5 | 121.4757230519 | 31.1486367495 | 290 | 5 | 4 | 5.5 | TDD | 280 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3227605 | 3 | 121.4681440193 | 31.1543071149 | 71 | 11 | 5 | 16.5 | TDD | 135 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3240826 | 9 | 121.4712005767 | 31.1457203428 | 156 | 9 | 7 | 26.9 | FDD | 168 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3247872 | 2 | 121.4712467163 | 31.1479875653 | 225 | 15 | 4 | 12.2 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3251581 | 12 | 121.4759839047 | 31.1471267621 | 116 | 0 | 0 | 17.8 | FDD | 847 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3253209 | 11 | 121.4672643022 | 31.1533177333 | 347 | 15 | 0 | 11.0 | FDD | 429 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3261633 | 13 | 121.4756676217 | 31.1476001521 | 67 | 2 | 10 | 2.5 | FDD | 857 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3261736 | 8 | 121.4661115024 | 31.1503741612 | 108 | 5 | 4 | 16.2 | FDD | 744 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3269079 | 10 | 121.4725202831 | 31.1509706865 | 206 | 7 | 3 | 0.0 | FDD | 234 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3271631 | 6 | 121.4659899749 | 31.1447726568 | 324 | 8 | 10 | 20.4 | TDD | 218 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.202 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.227 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.371 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.371 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.014 | NREventA2 | measId:1;ServCellPCI:311;Se... |
| 2024-09-20 22:21:35.152 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.401 | NREventA5 | measId:3;ServCellPCI:311;Se... |
| 2024-09-20 22:21:35.452 | NRHandoverAttempt | SourcePCI:311;SourceNR-ARFC... |
| 2024-09-20 22:21:35.482 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.496 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.605 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.605 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217407 | 1 | 8.9377 | 5.9927 | -117.2741 | 14.2944 | 112.0721 | 0.0122 | 0.0079 |
| 2024_09_20 22:00 | 3247872 | 2 | 17.5086 | 6.0529 | -114.5504 | 9.6700 | 194.4127 | 0.0011 | 0.0167 |
| 2024_09_20 22:00 | 3227605 | 3 | 13.8214 | 14.9627 | -114.7152 | 9.8462 | 174.3539 | 0.0008 | 0.0137 |
| 2024_09_20 22:00 | 3212147 | 4 | 16.5640 | 14.9199 | -114.0300 | 11.6264 | 164.3483 | 0.0078 | 0.0131 |
| 2024_09_20 22:00 | 3223333 | 5 | 14.8077 | 9.1716 | -115.9038 | 18.2071 | 170.0500 | 0.0137 | 0.0156 |
| 2024_09_20 22:00 | 3271631 | 6 | 13.4664 | 11.3671 | -116.5639 | 19.6239 | 111.6451 | 0.0072 | 0.0190 |
| 2024_09_20 22:00 | 3219603 | 7 | 9.2742 | 19.2604 | -114.5436 | 4.0665 | 45.5138 | 0.0031 | 0.0043 |
| 2024_09_20 22:00 | 3261736 | 8 | 18.7642 | 5.3821 | -116.6025 | 3.8740 | 42.1510 | 0.0035 | 0.0072 |
| 2024_09_20 22:00 | 3240826 | 9 | 17.3585 | 9.3668 | -116.2641 | 3.6749 | 31.9097 | 0.0080 | 0.0097 |
| 2024_09_20 22:00 | 3269079 | 10 | 18.3025 | 14.7026 | -114.1244 | 4.5957 | 24.4338 | 0.0143 | 0.0188 |
| 2024_09_20 22:00 | 3253209 | 11 | 13.8966 | 10.6375 | -117.8267 | 4.1198 | 49.8826 | 0.0107 | 0.0158 |
| 2024_09_20 22:00 | 3251581 | 12 | 17.4374 | 14.3250 | -114.2923 | 4.2952 | 51.8550 | 0.0037 | 0.0136 |
| 2024_09_20 22:00 | 3261633 | 13 | 12.5184 | 5.1356 | -116.4443 | 3.6719 | 27.5652 | 0.0192 | 0.0176 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413407_2402DBF8 | 152650 | 994 | -90.1 | 152650 | 234 | -93.8 | 152650 | 857 | -96.2 | 152650 | 168 |
| MR_1774413407_E088A788 | 152650 | 994 | -88.9 | 152650 | 234 | -93.9 | 152650 | 857 | -96.1 | 152650 | 168 |
| MR_1774413407_A9A78116 | 504990 | 218 | -91.9 | 504990 | 912 | -98.8 | 504990 | 135 | -100.9 | 504990 | 355 |
| MR_1774413407_3FFE628A | 152650 | 994 | -87.4 | 152650 | 234 | -93.6 | 152650 | 857 | -95.6 | 152650 | 168 |
| MR_1774413407_6E408BF5 | 504990 | 218 | -95.2 | 504990 | 912 | -97.0 | 504990 | 135 | -98.6 | 504990 | 355 |
| MR_1774413407_C422A433 | 504990 | 218 | -92.0 | 504990 | 912 | -96.1 | 504990 | 135 | -101.0 | 504990 | 355 |
| MR_1774413407_BA7F24F9 | 152650 | 994 | -89.7 | 152650 | 234 | -91.8 | 152650 | 857 | -94.8 | 152650 | 168 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1409: `d87e7bd8-347...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d87e7bd8-3475-4d81-b96b-9682767d88da` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Add neighbor relationship between 3211073_4 and 3213627_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1409] topology](images/train_1409.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3211073_4
- `C2`: Add neighbor relationship between 3222710_3 and 3213627_2
- `C3`: Decrease transmission power for 3211073_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211073_4
- `C5`: Press down the tilt angle  of 3213627_2 by 3 degrees
- `C6`: Adjust the azimuth of 3213627_2 by 38 degrees
- `C7`: Adjust the azimuth of 3211073_4 by 50 degrees
- `C8`: Increase A3 Offset threshold for 3211073_4
- `C9`: Increase transmission power for 3211073_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213627_2
- `C11`: Lift the tilt angle  of 3213627_2 by 3 degrees
- `C12`: Increase transmission power for 3213627_2
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease A3 Offset threshold for 3213627_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213627_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211073_4
- `C17`: Increase A3 Offset threshold for 3213627_2
- `C18`: Add neighbor relationship between 3211073_4 and 3213627_2 **← 정답**
- `C19`: Check test server and transmission issues
- `C20`: Decrease transmission power for 3213627_2
- `C21`: Press down the tilt angle of 3211073_4 by 8 degrees
- `C22`: Lift the tilt angle of 3211073_4 by 8 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.865 | MS1 | 121.4656717429 | 31.1446290760 | 943 | 504990 | -79.97 | 15.76 | 448.43 | 0.20 | 2.48 | 1572 |
| 2024-09-20 22:21:32.232 | MS1 | 121.4656721541 | 31.1446369716 | 943 | 504990 | -84.38 | 16.78 | 434.93 | 0.12 | 2.56 | 1564 |
| 2024-09-20 22:21:33.557 | MS1 | 121.4656685748 | 31.1446314244 | 943 | 504990 | -79.08 | 16.00 | 350.17 | 0.13 | 2.02 | 1565 |
| 2024-09-20 22:21:34.739 | MS1 | 121.4656734113 | 31.1446322653 | 943 | 504990 | -87.13 | -3.03 | 44.40 | 0.15 | 1.07 | 1579 |
| 2024-09-20 22:21:35.245 | MS1 | 121.4656753345 | 31.1446372858 | 943 | 504990 | -86.57 | -3.75 | 65.14 | 0.19 | 1.40 | 1566 |
| 2024-09-20 22:21:36.877 | MS1 | 121.4656678377 | 31.1446213400 | 943 | 504990 | -94.66 | -3.90 | 32.31 | 0.04 | 1.04 | 1576 |
| 2024-09-20 22:21:37.356 | MS1 | 121.4656711438 | 31.1446300935 | 943 | 504990 | -88.18 | -0.40 | 36.50 | 0.08 | 1.14 | 1600 |
| 2024-09-20 22:21:38.811 | MS1 | 121.4656610852 | 31.1446319330 | 943 | 504990 | -77.55 | 13.50 | 365.53 | 0.12 | 1.39 | 1565 |
| 2024-09-20 22:21:39.995 | MS1 | 121.4656611885 | 31.1446321275 | 943 | 504990 | -84.54 | 14.65 | 510.85 | 0.11 | 1.03 | 1587 |
| 2024-09-20 22:21:40.302 | MS1 | 121.4656704237 | 31.1446246959 | 943 | 504990 | -81.33 | 17.50 | 420.53 | 0.16 | 2.83 | 1566 |
| 2024-09-20 22:21:41.830 | MS1 | 121.4656711328 | 31.1446214144 | 943 | 504990 | -84.75 | 13.03 | 532.62 | 0.02 | 2.08 | 1582 |
| 2024-09-20 22:21:42.273 | MS1 | 121.4656733091 | 31.1446227072 | 943 | 504990 | -82.82 | 14.32 | 441.52 | 0.02 | 2.58 | 1580 |

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
| 3211073 | 4 | 121.4676500567 | 31.1515428955 | 95 | 5 | 11 | 42.6 | TDD | 943 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3213627 | 2 | 121.4723485271 | 31.1557295702 | 169 | 1 | 0 | 46.3 | TDD | 933 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3222710 | 3 | 121.4722370021 | 31.1518977221 | 242 | 13 | 3 | 22.3 | TDD | 582 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3248927 | 1 | 121.4652531310 | 31.1542881940 | 141 | 0 | 6 | 24.1 | TDD | 828 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.148 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.163 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.308 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.308 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.980 | NREventA3 | measId:2;ServCellPCI:595;Se... |
| 2024-09-20 22:21:35.980 | NREventA3 | measId:2;ServCellPCI:595;Se... |
| 2024-09-20 22:21:36.980 | NREventA3 | measId:2;ServCellPCI:595;Se... |
| 2024-09-20 22:21:39.480 | NRRRCReestablishAttempt | PCI:595 |
| 2024-09-20 22:21:39.493 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.506 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.647 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.647 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248927 | 1 | 9.5297 | 9.8728 | -114.0130 | 9.2044 | 113.7720 | 0.0138 | 0.0002 |
| 2024_09_20 22:00 | 3213627 | 2 | 12.7869 | 9.3342 | -116.8181 | 19.5358 | 121.5425 | 0.0168 | 0.0039 |
| 2024_09_20 22:00 | 3222710 | 3 | 17.8963 | 10.1339 | -114.2155 | 12.1962 | 151.5314 | 0.0126 | 0.0108 |
| 2024_09_20 22:00 | 3211073 | 4 | 5.7116 | 10.0897 | -114.4719 | 9.0864 | 97.4727 | 0.0018 | 0.1699 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415667_F56E78FF | 504990 | 933 | -83.5 | 504990 | 943 | -87.9 | 504990 | 582 | -92.0 | 504990 | 828 |
| MR_1774415667_6C7ACE30 | 504990 | 933 | -82.4 | 504990 | 943 | -88.6 | 504990 | 582 | -92.7 | 504990 | 828 |
| MR_1774415667_2F50BD00 | 504990 | 943 | -88.5 | 504990 | 933 | -83.5 | 504990 | 582 | -90.2 | 504990 | 828 |
| MR_1774415667_D67C2A14 | 504990 | 933 | -83.4 | 504990 | 943 | -85.7 | 504990 | 582 | -89.2 | 504990 | 828 |
| MR_1774415667_C27C6604 | 504990 | 943 | -85.9 | 504990 | 933 | -80.0 | 504990 | 582 | -89.8 | 504990 | 828 |

> *... 2개 열 생략 (전체 14열)*

---
