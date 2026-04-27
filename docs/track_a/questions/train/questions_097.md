# Track A 문제 분석 — train[960]~train[969]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[960] ~ train[969] (10개)

## 목차

1. [문제 960: `8130b0f3-fcf...`](#960) — single-answer, 정답: C8
2. [문제 961: `b83eca4d-126...`](#961) — single-answer, 정답: C10
3. [문제 962: `469e0588-e30...`](#962) — single-answer, 정답: C13
4. [문제 963: `c59718bf-f01...`](#963) — multiple-answer, 정답: C5|C21
5. [문제 964: `1dd96e43-ea3...`](#964) — single-answer, 정답: C19
6. [문제 965: `553918b6-f38...`](#965) — single-answer, 정답: C12
7. [문제 966: `f82f304c-719...`](#966) — multiple-answer, 정답: C2|C11
8. [문제 967: `a8dea54c-083...`](#967) — single-answer, 정답: C10
9. [문제 968: `c7465c6b-92b...`](#968) — multiple-answer, 정답: C9|C11
10. [문제 969: `0afb51e8-e6b...`](#969) — single-answer, 정답: C19

---

### 문제 960: `8130b0f3-fcf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8130b0f3-fcf0-461d-83e8-8956053f30b2` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248521_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[960] topology](images/train_0960.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3220601_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220601_4
- `C3`: Add neighbor relationship between 3224975_11 and 3220601_4
- `C4`: Lift the tilt angle  of 3220601_4 by 6 degrees
- `C5`: Decrease A3 Offset threshold for 3248521_5
- `C6`: Adjust the azimuth of 3220601_4 by 20 degrees
- `C7`: Decrease A3 Offset threshold for 3220601_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248521_5 **← 정답**
- `C9`: Increase A3 Offset threshold for 3220601_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220601_4
- `C11`: Increase transmission power for 3248521_5
- `C12`: Decrease transmission power for 3248521_5
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248521_5
- `C14`: Adjust the azimuth of 3248521_5 by 24 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Increase A3 Offset threshold for 3248521_5
- `C17`: Decrease transmission power for 3220601_4
- `C18`: Press down the tilt angle  of 3220601_4 by 6 degrees
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle of 3248521_5 by 2 degrees
- `C21`: Add neighbor relationship between 3248521_5 and 3220601_4
- `C22`: Lift the tilt angle of 3248521_5 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.307 | MS1 | 121.4656662561 | 31.1446196007 | 374 | 504990 | -95.04 | 13.42 | 338.32 | 0.01 | 2.04 | 1568 |
| 2024-09-20 22:21:32.873 | MS1 | 121.4656655785 | 31.1446289605 | 344 | 504990 | -95.87 | 13.36 | 394.74 | 0.13 | 2.82 | 1600 |
| 2024-09-20 22:21:33.247 | MS1 | 121.4656688208 | 31.1446192946 | 679 | 504990 | -95.87 | 14.39 | 362.99 | 0.10 | 2.36 | 1598 |
| 2024-09-20 22:21:34.934 | MS1 | 121.4656746310 | 31.1446285988 | 169 | 152650 | -89.68 | 6.08 | 49.46 | 0.16 | 1.99 | 960 |
| 2024-09-20 22:21:35.283 | MS1 | 121.4656592915 | 31.1446245383 | 554 | 152650 | -93.46 | 7.49 | 77.43 | 0.05 | 1.61 | 925 |
| 2024-09-20 22:21:36.213 | MS1 | 121.4656609315 | 31.1446246127 | 532 | 152650 | -93.74 | 4.50 | 89.47 | 0.01 | 1.63 | 921 |
| 2024-09-20 22:21:37.822 | MS1 | 121.4656750465 | 31.1446301678 | 354 | 152650 | -96.10 | 7.86 | 106.38 | 0.05 | 1.88 | 901 |
| 2024-09-20 22:21:38.329 | MS1 | 121.4656601562 | 31.1446365513 | 169 | 152650 | -95.05 | 7.35 | 61.73 | 0.17 | 1.86 | 974 |
| 2024-09-20 22:21:39.638 | MS1 | 121.4656618671 | 31.1446181948 | 554 | 152650 | -94.11 | 4.16 | 43.39 | 0.01 | 1.63 | 938 |
| 2024-09-20 22:21:40.835 | MS1 | 121.4656624559 | 31.1446329556 | 532 | 152650 | -88.29 | 3.14 | 94.06 | 0.01 | 2.23 | 1590 |
| 2024-09-20 22:21:41.677 | MS1 | 121.4656614317 | 31.1446263523 | 354 | 152650 | -88.79 | 2.31 | 54.72 | 0.10 | 2.68 | 1571 |
| 2024-09-20 22:21:42.874 | MS1 | 121.4656733263 | 31.1446250318 | 169 | 152650 | -91.09 | 6.16 | 86.18 | 0.18 | 2.66 | 1572 |

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
| 3220601 | 4 | 121.4738805837 | 31.1499908081 | 253 | 5 | 0 | 9.7 | TDD | 491 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3224975 | 11 | 121.4662682961 | 31.1552113450 | 42 | 12 | 2 | 25.0 | FDD | 532 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3233903 | 2 | 121.4738591712 | 31.1494974528 | 59 | 13 | 6 | 22.3 | TDD | 679 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3237171 | 9 | 121.4720416905 | 31.1453285320 | 204 | 15 | 1 | 5.0 | FDD | 554 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3241680 | 1 | 121.4736122712 | 31.1513363223 | 268 | 4 | 5 | 4.2 | TDD | 452 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3246333 | 13 | 121.4666789859 | 31.1495442381 | 22 | 1 | 10 | 9.6 | FDD | 157 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3248521 | 5 | 121.4724476251 | 31.1537892710 | 236 | 1 | 10 | 22.2 | TDD | 374 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3248984 | 12 | 121.4708956357 | 31.1507599679 | 274 | 11 | 1 | 6.0 | FDD | 955 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3250878 | 8 | 121.4682800848 | 31.1468846800 | 123 | 10 | 12 | 16.6 | FDD | 169 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3261636 | 3 | 121.4712484892 | 31.1445709887 | 230 | 8 | 11 | 12.7 | TDD | 903 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3265194 | 10 | 121.4752720711 | 31.1525154799 | 339 | 15 | 9 | 21.4 | FDD | 459 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3270923 | 6 | 121.4657382263 | 31.1486575515 | 330 | 5 | 7 | 21.9 | TDD | 344 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3271496 | 7 | 121.4685059973 | 31.1533147438 | 9 | 15 | 2 | 10.4 | FDD | 354 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |

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
| 2024-09-20 22:21:31.322 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.344 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.449 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.449 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.204 | NREventA2 | measId:1;ServCellPCI:757;Se... |
| 2024-09-20 22:21:35.327 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.589 | NREventA5 | measId:3;ServCellPCI:757;Se... |
| 2024-09-20 22:21:35.633 | NRHandoverAttempt | SourcePCI:757;SourceNR-ARFC... |
| 2024-09-20 22:21:35.656 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.666 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.783 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.783 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241680 | 1 | 14.4973 | 5.2937 | -115.6858 | 5.2632 | 177.4830 | 0.0179 | 0.0128 |
| 2024_09_20 22:00 | 3233903 | 2 | 19.4710 | 9.1016 | -117.1245 | 15.6408 | 145.0307 | 0.0129 | 0.0166 |
| 2024_09_20 22:00 | 3261636 | 3 | 19.0090 | 10.6526 | -117.4355 | 15.7764 | 115.8155 | 0.0089 | 0.0122 |
| 2024_09_20 22:00 | 3220601 | 4 | 13.8449 | 7.1025 | -116.7259 | 5.2331 | 180.2056 | 0.0175 | 0.0014 |
| 2024_09_20 22:00 | 3248521 | 5 | 16.8169 | 15.7655 | -115.3514 | 9.1720 | 196.8116 | 0.0114 | 0.0168 |
| 2024_09_20 22:00 | 3270923 | 6 | 13.7637 | 15.1830 | -115.0535 | 19.8990 | 171.7931 | 0.0166 | 0.0153 |
| 2024_09_20 22:00 | 3271496 | 7 | 6.2627 | 14.3187 | -117.9220 | 3.6759 | 31.5941 | 0.0081 | 0.0063 |
| 2024_09_20 22:00 | 3250878 | 8 | 7.3657 | 6.1387 | -117.0710 | 4.7610 | 45.0016 | 0.0080 | 0.0008 |
| 2024_09_20 22:00 | 3237171 | 9 | 10.3460 | 15.7471 | -114.5332 | 4.7126 | 23.0921 | 0.0063 | 0.0051 |
| 2024_09_20 22:00 | 3265194 | 10 | 18.5641 | 7.6637 | -115.4285 | 4.6234 | 55.8723 | 0.0109 | 0.0096 |
| 2024_09_20 22:00 | 3224975 | 11 | 19.7991 | 6.5123 | -115.0786 | 3.1741 | 20.7450 | 0.0143 | 0.0156 |
| 2024_09_20 22:00 | 3248984 | 12 | 13.1073 | 18.8017 | -117.5029 | 3.6406 | 30.2204 | 0.0136 | 0.0082 |
| 2024_09_20 22:00 | 3246333 | 13 | 13.4259 | 14.9697 | -114.7303 | 3.9509 | 38.8336 | 0.0102 | 0.0178 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415323_DEE18B02 | 504990 | 679 | -94.5 | 504990 | 491 | -95.9 | 504990 | 452 | -98.1 | 504990 | 903 |
| MR_1774415323_9EA692F1 | 152650 | 169 | -90.2 | 152650 | 955 | -96.0 | 152650 | 459 | -97.1 | 152650 | 157 |
| MR_1774415323_79A8FD22 | 152650 | 169 | -88.0 | 152650 | 955 | -92.4 | 152650 | 459 | -98.7 | 152650 | 157 |
| MR_1774415323_EEE1426B | 504990 | 679 | -94.2 | 504990 | 491 | -96.4 | 504990 | 452 | -100.0 | 504990 | 903 |
| MR_1774415323_56794969 | 152650 | 169 | -90.3 | 152650 | 955 | -95.7 | 152650 | 459 | -98.9 | 152650 | 157 |
| MR_1774415323_CD69F06F | 152650 | 169 | -89.4 | 152650 | 955 | -95.5 | 152650 | 459 | -98.4 | 152650 | 157 |
| MR_1774415323_A08E99DE | 504990 | 679 | -96.9 | 504990 | 491 | -94.3 | 504990 | 452 | -96.6 | 504990 | 903 |
| MR_1774415323_9209ABEF | 152650 | 169 | -88.4 | 152650 | 955 | -92.6 | 152650 | 459 | -99.3 | 152650 | 157 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 961: `b83eca4d-126...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b83eca4d-1269-41ba-936b-3bc3519a05a9` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[961] topology](images/train_0961.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3225217_4 by 50 degrees
- `C2`: Lift the tilt angle  of 3225217_4 by 10 degrees
- `C3`: Increase transmission power for 3234766_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225217_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234766_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234766_1
- `C7`: Decrease transmission power for 3234766_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease A3 Offset threshold for 3225217_4
- `C10`: Check test server and transmission issues **← 정답**
- `C11`: Lift the tilt angle of 3234766_1 by 10 degrees
- `C12`: Decrease A3 Offset threshold for 3234766_1
- `C13`: Adjust the azimuth of 3234766_1 by 50 degrees
- `C14`: Decrease transmission power for 3225217_4
- `C15`: Add neighbor relationship between 3234766_1 and 3225217_4
- `C16`: Press down the tilt angle  of 3225217_4 by 10 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225217_4
- `C18`: Increase A3 Offset threshold for 3234766_1
- `C19`: Add neighbor relationship between 3272516_2 and 3225217_4
- `C20`: Increase transmission power for 3225217_4
- `C21`: Increase A3 Offset threshold for 3225217_4
- `C22`: Press down the tilt angle of 3234766_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.242 | MS1 | 121.4656612680 | 31.1446343809 | 504 | 504990 | -89.80 | 17.17 | 547.29 | 0.12 | 2.07 | 1600 |
| 2024-09-20 22:21:32.967 | MS1 | 121.4656672578 | 31.1446374243 | 504 | 504990 | -89.70 | 15.77 | 319.67 | 0.06 | 2.80 | 1595 |
| 2024-09-20 22:21:33.922 | MS1 | 121.4656684112 | 31.1446340194 | 504 | 504990 | -87.58 | 14.42 | 439.92 | 0.17 | 2.62 | 1568 |
| 2024-09-20 22:21:34.910 | MS1 | 121.4656592105 | 31.1446330587 | 504 | 504990 | -86.40 | 12.64 | 65.66 | 0.16 | 2.22 | 473 |
| 2024-09-20 22:21:35.779 | MS1 | 121.4656708201 | 31.1446292454 | 504 | 504990 | -85.31 | 12.45 | 48.70 | 0.16 | 2.23 | 500 |
| 2024-09-20 22:21:36.949 | MS1 | 121.4656581019 | 31.1446326776 | 504 | 504990 | -86.37 | 12.00 | 80.75 | 0.18 | 2.86 | 439 |
| 2024-09-20 22:21:37.890 | MS1 | 121.4656726119 | 31.1446309164 | 504 | 504990 | -90.10 | 12.76 | 84.11 | 0.02 | 2.77 | 347 |
| 2024-09-20 22:21:38.695 | MS1 | 121.4656769256 | 31.1446260166 | 504 | 504990 | -89.88 | 12.53 | 80.60 | 0.03 | 2.52 | 384 |
| 2024-09-20 22:21:39.114 | MS1 | 121.4656753873 | 31.1446251979 | 504 | 504990 | -92.15 | 8.65 | 80.08 | 0.04 | 2.63 | 409 |
| 2024-09-20 22:21:40.943 | MS1 | 121.4656716758 | 31.1446268276 | 504 | 504990 | -91.49 | 11.32 | 385.63 | 0.19 | 2.35 | 1579 |
| 2024-09-20 22:21:41.350 | MS1 | 121.4656590156 | 31.1446361935 | 504 | 504990 | -92.63 | 9.73 | 360.17 | 0.14 | 2.81 | 1590 |
| 2024-09-20 22:21:42.339 | MS1 | 121.4656734743 | 31.1446209540 | 504 | 504990 | -92.18 | 12.20 | 438.83 | 0.17 | 2.47 | 1589 |

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
| 3225217 | 4 | 121.4652854756 | 31.1513465699 | 239 | 12 | 7 | 28.1 | TDD | 791 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3225712 | 3 | 121.4653167313 | 31.1492118991 | 70 | 10 | 9 | 16.2 | TDD | 685 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3234766 | 1 | 121.4712845181 | 31.1534711464 | 93 | 15 | 9 | 18.4 | TDD | 504 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3272516 | 2 | 121.4641097031 | 31.1486926177 | 163 | 1 | 5 | 29.9 | TDD | 50 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.094 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.110 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.235 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.235 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.928 | NREventA3 | measId:2;ServCellPCI:580;Se... |
| 2024-09-20 22:21:38.168 | NRHandoverAttempt | SourcePCI:580;SourceNR-ARFC... |
| 2024-09-20 22:21:38.202 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.213 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.320 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.320 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234766 | 1 | 16.9287 | 16.1354 | -115.6746 | 14.8936 | 160.4992 | 0.0012 | 0.0039 |
| 2024_09_20 22:00 | 3272516 | 2 | 6.4182 | 8.9717 | -116.0342 | 14.9850 | 163.2692 | 0.0144 | 0.0031 |
| 2024_09_20 22:00 | 3225712 | 3 | 19.7178 | 15.8621 | -114.2941 | 18.5571 | 158.8740 | 0.0085 | 0.0134 |
| 2024_09_20 22:00 | 3225217 | 4 | 13.0760 | 15.2400 | -114.1907 | 9.8434 | 95.5670 | 0.0121 | 0.0131 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413177_7E192511 | 504990 | 504 | -86.1 | 504990 | 791 | -86.4 | 504990 | 50 | -93.3 | 504990 | 685 |
| MR_1774413177_81E7A601 | 504990 | 504 | -86.1 | 504990 | 791 | -86.8 | 504990 | 50 | -93.1 | 504990 | 685 |
| MR_1774413177_4DFEA0A0 | 504990 | 504 | -87.6 | 504990 | 791 | -86.0 | 504990 | 50 | -94.2 | 504990 | 685 |
| MR_1774413177_DC104E8D | 504990 | 504 | -85.3 | 504990 | 791 | -87.9 | 504990 | 50 | -94.4 | 504990 | 685 |
| MR_1774413177_D07CB9DD | 504990 | 504 | -85.9 | 504990 | 791 | -87.5 | 504990 | 50 | -91.5 | 504990 | 685 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 962: `469e0588-e30...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `469e0588-e307-4a45-9a13-ecb789cceb68` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3249615_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[962] topology](images/train_0962.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3217028_2
- `C2`: Adjust the azimuth of 3249615_4 by 18 degrees
- `C3`: Press down the tilt angle  of 3217028_2 by 5 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease A3 Offset threshold for 3217028_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217028_2
- `C7`: Decrease transmission power for 3249615_4
- `C8`: Increase A3 Offset threshold for 3249615_4
- `C9`: Lift the tilt angle  of 3217028_2 by 5 degrees
- `C10`: Adjust the azimuth of 3217028_2 by 50 degrees
- `C11`: Add neighbor relationship between 3229744_3 and 3217028_2
- `C12`: Add neighbor relationship between 3249615_4 and 3217028_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249615_4 **← 정답**
- `C14`: Increase A3 Offset threshold for 3217028_2
- `C15`: Lift the tilt angle of 3249615_4 by 5 degrees
- `C16`: Check test server and transmission issues
- `C17`: Press down the tilt angle of 3249615_4 by 5 degrees
- `C18`: Increase transmission power for 3217028_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249615_4
- `C20`: Increase transmission power for 3249615_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217028_2
- `C22`: Decrease A3 Offset threshold for 3249615_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.748 | MS1 | 121.4656758760 | 31.1446358847 | 975 | 504990 | -90.24 | 12.54 | 448.18 | 0.06 | 2.26 | 1581 |
| 2024-09-20 22:21:32.983 | MS1 | 121.4656773290 | 31.1446326166 | 975 | 504990 | -89.72 | 14.27 | 346.52 | 0.19 | 2.46 | 1570 |
| 2024-09-20 22:21:33.654 | MS1 | 121.4656605420 | 31.1446316160 | 975 | 504990 | -87.82 | 13.41 | 304.53 | 0.03 | 2.13 | 1564 |
| 2024-09-20 22:21:34.753 | MS1 | 121.4656740669 | 31.1446365564 | 975 | 504990 | -89.15 | 14.85 | 91.79 | 0.54 | 2.56 | 663 |
| 2024-09-20 22:21:35.145 | MS1 | 121.4656627878 | 31.1446324074 | 975 | 504990 | -89.13 | 13.55 | 64.56 | 0.69 | 2.76 | 505 |
| 2024-09-20 22:21:36.133 | MS1 | 121.4656665103 | 31.1446345203 | 975 | 504990 | -86.70 | 17.53 | 57.28 | 0.66 | 2.50 | 556 |
| 2024-09-20 22:21:37.913 | MS1 | 121.4656778953 | 31.1446317026 | 975 | 504990 | -92.76 | 8.44 | 99.00 | 0.60 | 2.72 | 514 |
| 2024-09-20 22:21:38.553 | MS1 | 121.4656700571 | 31.1446237838 | 975 | 504990 | -89.30 | 11.33 | 100.33 | 0.64 | 2.03 | 511 |
| 2024-09-20 22:21:39.320 | MS1 | 121.4656580245 | 31.1446356535 | 975 | 504990 | -91.37 | 7.89 | 61.63 | 0.55 | 2.06 | 625 |
| 2024-09-20 22:21:40.699 | MS1 | 121.4656678974 | 31.1446242890 | 975 | 504990 | -90.44 | 9.09 | 330.97 | 0.17 | 2.51 | 1587 |
| 2024-09-20 22:21:41.782 | MS1 | 121.4656758636 | 31.1446197451 | 975 | 504990 | -90.99 | 11.63 | 567.70 | 0.06 | 2.40 | 1575 |
| 2024-09-20 22:21:42.520 | MS1 | 121.4656745310 | 31.1446180922 | 975 | 504990 | -91.17 | 9.56 | 479.94 | 0.01 | 2.77 | 1570 |

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
| 3217028 | 2 | 121.4667455052 | 31.1523992919 | 99 | 3 | 1 | 25.5 | TDD | 970 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3229744 | 3 | 121.4759727464 | 31.1529793142 | 288 | 11 | 2 | 37.4 | TDD | 691 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3230891 | 1 | 121.4680709572 | 31.1541069609 | 89 | 11 | 11 | 44.1 | TDD | 352 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3249615 | 4 | 121.4756633697 | 31.1461002626 | 278 | 2 | 11 | 42.6 | TDD | 975 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.125 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.142 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.291 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.291 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.003 | NREventA3 | measId:2;ServCellPCI:119;Se... |
| 2024-09-20 22:21:38.243 | NRHandoverAttempt | SourcePCI:119;SourceNR-ARFC... |
| 2024-09-20 22:21:38.286 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.298 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.407 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.407 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230891 | 1 | 13.8527 | 9.3037 | -116.7054 | 14.4492 | 163.2123 | 0.0017 | 0.0006 |
| 2024_09_20 22:00 | 3217028 | 2 | 10.0288 | 5.5290 | -114.0420 | 5.5042 | 80.9876 | 0.0138 | 0.0140 |
| 2024_09_20 22:00 | 3229744 | 3 | 8.6742 | 13.2036 | -116.6956 | 11.1881 | 97.5622 | 0.0160 | 0.0041 |
| 2024_09_20 22:00 | 3249615 | 4 | 16.2348 | 12.8529 | -115.4567 | 5.9411 | 115.5292 | 0.0200 | 0.0049 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416818_F6AE4F6A | 504990 | 975 | -88.5 | 504990 | 970 | -94.4 | 504990 | 691 | -97.0 | 504990 | 352 |
| MR_1774416818_C5792E2B | 504990 | 975 | -87.3 | 504990 | 970 | -96.4 | 504990 | 691 | -97.8 | 504990 | 352 |
| MR_1774416818_F01A3189 | 504990 | 975 | -89.2 | 504990 | 970 | -93.4 | 504990 | 691 | -97.1 | 504990 | 352 |
| MR_1774416818_4BA57EF0 | 504990 | 975 | -90.4 | 504990 | 970 | -95.4 | 504990 | 691 | -97.5 | 504990 | 352 |
| MR_1774416818_F98F355D | 504990 | 975 | -89.7 | 504990 | 970 | -95.8 | 504990 | 691 | -100.2 | 504990 | 352 |
| MR_1774416818_5AEBCA33 | 504990 | 975 | -87.7 | 504990 | 970 | -93.8 | 504990 | 691 | -97.2 | 504990 | 352 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 963: `c59718bf-f01...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c59718bf-f013-4222-b065-cae44df5f6a7` |
| Tag | **multiple-answer** |
| 정답 | **C5|C21** |
| C5 의미 | Adjust the azimuth of 3224055_1 by 50 degrees |
| C21 의미 | Increase transmission power for 3224055_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[963] topology](images/train_0963.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224055_1
- `C2`: Decrease transmission power for 3224055_1
- `C3`: Decrease A3 Offset threshold for 3224055_1
- `C4`: Lift the tilt angle of 3224055_1 by 10 degrees
- `C5`: Adjust the azimuth of 3224055_1 by 50 degrees **← 정답**
- `C6`: Add neighbor relationship between 3275860_2 and 3247213_3
- `C7`: Decrease transmission power for 3247213_3
- `C8`: Press down the tilt angle  of 3247213_3 by 2 degrees
- `C9`: Adjust the azimuth of 3247213_3 by 33 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224055_1
- `C11`: Press down the tilt angle of 3224055_1 by 10 degrees
- `C12`: Decrease A3 Offset threshold for 3247213_3
- `C13`: Increase A3 Offset threshold for 3247213_3
- `C14`: Increase transmission power for 3247213_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247213_3
- `C16`: Add neighbor relationship between 3224055_1 and 3247213_3
- `C17`: Check test server and transmission issues
- `C18`: Lift the tilt angle  of 3247213_3 by 2 degrees
- `C19`: Increase A3 Offset threshold for 3224055_1
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase transmission power for 3224055_1 **← 정답**
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247213_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.705 | MS1 | 121.4656594776 | 31.1446221385 | 769 | 504990 | -86.48 | 17.89 | 508.46 | 0.02 | 2.05 | 1593 |
| 2024-09-20 22:21:32.264 | MS1 | 121.4656722060 | 31.1446229305 | 769 | 504990 | -87.58 | 12.42 | 460.38 | 0.16 | 2.19 | 1593 |
| 2024-09-20 22:21:33.327 | MS1 | 121.4656728791 | 31.1446252079 | 769 | 504990 | -88.60 | 12.57 | 351.96 | 0.20 | 2.92 | 1578 |
| 2024-09-20 22:21:34.320 | MS1 | 121.4656634933 | 31.1446224478 | 769 | 504990 | -102.05 | 1.92 | 31.28 | 0.13 | 1.12 | 1568 |
| 2024-09-20 22:21:35.374 | MS1 | 121.4656679081 | 31.1446353397 | 769 | 504990 | -105.12 | -0.74 | 42.03 | 0.15 | 1.04 | 1575 |
| 2024-09-20 22:21:36.806 | MS1 | 121.4656723671 | 31.1446199603 | 769 | 504990 | -104.70 | 0.38 | 81.73 | 0.07 | 1.43 | 1593 |
| 2024-09-20 22:21:37.283 | MS1 | 121.4656607190 | 31.1446367894 | 769 | 504990 | -100.65 | 0.32 | 35.14 | 0.11 | 1.15 | 1594 |
| 2024-09-20 22:21:38.254 | MS1 | 121.4656765613 | 31.1446345258 | 769 | 504990 | -102.07 | -0.62 | 53.44 | 0.05 | 1.21 | 1597 |
| 2024-09-20 22:21:39.689 | MS1 | 121.4656764590 | 31.1446232848 | 769 | 504990 | -105.64 | -1.82 | 69.75 | 0.19 | 1.07 | 1568 |
| 2024-09-20 22:21:40.561 | MS1 | 121.4656605274 | 31.1446290056 | 769 | 504990 | -86.49 | 14.88 | 585.51 | 0.08 | 2.57 | 1570 |
| 2024-09-20 22:21:41.529 | MS1 | 121.4656748008 | 31.1446320162 | 769 | 504990 | -88.45 | 13.38 | 480.45 | 0.09 | 2.06 | 1593 |
| 2024-09-20 22:21:42.831 | MS1 | 121.4656661650 | 31.1446320241 | 769 | 504990 | -93.95 | 12.86 | 357.57 | 0.12 | 2.68 | 1581 |

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
| 3224055 | 1 | 121.4641700961 | 31.1477177314 | 86 | 10 | 2 | 28.8 | TDD | 769 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3230574 | 4 | 121.4700315236 | 31.1526635281 | 99 | 13 | 6 | 36.1 | TDD | 607 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3247213 | 3 | 121.4723724252 | 31.1531586934 | 247 | 1 | 12 | 25.3 | TDD | 452 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3275860 | 2 | 121.4671402033 | 31.1538648496 | 236 | 2 | 1 | 33.4 | TDD | 451 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.124 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.147 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.280 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.280 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.447 | NREventA2 | measId:1;ServCellPCI:886;Se... |
| 2024-09-20 22:21:34.586 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224055 | 1 | 12.1783 | 5.0635 | -116.3249 | 19.0619 | 153.7813 | 0.1219 | 0.0118 |
| 2024_09_20 22:00 | 3275860 | 2 | 19.7223 | 18.2823 | -117.8540 | 15.2270 | 172.7142 | 0.0024 | 0.0178 |
| 2024_09_20 22:00 | 3247213 | 3 | 10.7744 | 11.6946 | -117.8866 | 11.5665 | 176.0202 | 0.0133 | 0.0187 |
| 2024_09_20 22:00 | 3230574 | 4 | 5.2969 | 18.7390 | -115.2429 | 18.4849 | 129.1493 | 0.0196 | 0.0063 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414253_B8EBCA92 | 504990 | 769 | -100.9 | 504990 | 452 | -104.4 | 504990 | 451 | -111.7 | 504990 | 607 |
| MR_1774414253_227A91F1 | 504990 | 769 | -100.3 | 504990 | 452 | -105.1 | 504990 | 451 | -112.7 | 504990 | 607 |
| MR_1774414253_C7115EE3 | 504990 | 769 | -103.2 | 504990 | 452 | -106.3 | 504990 | 451 | -113.5 | 504990 | 607 |
| MR_1774414253_89BC35FA | 504990 | 769 | -103.3 | 504990 | 452 | -105.8 | 504990 | 451 | -110.9 | 504990 | 607 |
| MR_1774414253_362D54CB | 504990 | 769 | -103.5 | 504990 | 452 | -103.5 | 504990 | 451 | -111.9 | 504990 | 607 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 964: `1dd96e43-ea3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1dd96e43-ea32-4ddb-bb41-4359573871c9` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[964] topology](images/train_0964.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3279976_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279976_4
- `C3`: Add neighbor relationship between 3211803_3 and 3279976_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279976_4
- `C5`: Decrease transmission power for 3274267_2
- `C6`: Lift the tilt angle  of 3279976_4 by 8 degrees
- `C7`: Press down the tilt angle of 3274267_2 by 10 degrees
- `C8`: Increase A3 Offset threshold for 3279976_4
- `C9`: Lift the tilt angle of 3274267_2 by 10 degrees
- `C10`: Check test server and transmission issues
- `C11`: Adjust the azimuth of 3279976_4 by 50 degrees
- `C12`: Decrease A3 Offset threshold for 3279976_4
- `C13`: Decrease A3 Offset threshold for 3274267_2
- `C14`: Increase A3 Offset threshold for 3274267_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274267_2
- `C16`: Decrease transmission power for 3279976_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274267_2
- `C18`: Increase transmission power for 3274267_2
- `C19`: Insufficient data; more data is needed for judgment. **← 정답**
- `C20`: Add neighbor relationship between 3274267_2 and 3279976_4
- `C21`: Adjust the azimuth of 3274267_2 by 50 degrees
- `C22`: Press down the tilt angle  of 3279976_4 by 8 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.820 | MS1 | 121.4656642576 | 31.1446239658 | 243 | 504990 | -91.34 | 14.18 | 528.71 | 0.13 | 2.08 | 1592 |
| 2024-09-20 22:21:32.908 | MS1 | 121.4656755506 | 31.1446348408 | 243 | 504990 | -85.59 | 16.25 | 357.66 | 0.04 | 2.48 | 1596 |
| 2024-09-20 22:21:33.785 | MS1 | 121.4656595577 | 31.1446203034 | 243 | 504990 | -90.13 | 17.29 | 464.87 | 0.05 | 2.72 | 1589 |
| 2024-09-20 22:21:34.998 | MS1 | 121.4656662822 | 31.1446294890 | 243 | 504990 | -85.12 | 15.03 | 94.47 | 0.09 | 2.53 | 1580 |
| 2024-09-20 22:21:35.722 | MS1 | 121.4656607851 | 31.1446248021 | 243 | 504990 | -86.88 | 15.70 | 57.29 | 0.06 | 2.86 | 1566 |
| 2024-09-20 22:21:36.483 | MS1 | 121.4656727981 | 31.1446321607 | 243 | 504990 | -89.25 | 16.97 | 60.88 | 0.03 | 2.21 | 1571 |
| 2024-09-20 22:21:37.327 | MS1 | 121.4656649592 | 31.1446257749 | 243 | 504990 | -89.16 | 7.46 | 76.22 | 0.04 | 2.21 | 1598 |
| 2024-09-20 22:21:38.557 | MS1 | 121.4656692941 | 31.1446320167 | 243 | 504990 | -89.64 | 7.82 | 53.32 | 0.12 | 2.72 | 1582 |
| 2024-09-20 22:21:39.967 | MS1 | 121.4656647096 | 31.1446344513 | 243 | 504990 | -93.23 | 11.59 | 59.50 | 0.13 | 2.02 | 1568 |
| 2024-09-20 22:21:40.341 | MS1 | 121.4656657277 | 31.1446279192 | 243 | 504990 | -91.79 | 9.08 | 471.61 | 0.06 | 2.90 | 1595 |
| 2024-09-20 22:21:41.841 | MS1 | 121.4656766490 | 31.1446209061 | 243 | 504990 | -90.36 | 11.65 | 410.11 | 0.05 | 2.69 | 1582 |
| 2024-09-20 22:21:42.426 | MS1 | 121.4656672108 | 31.1446235197 | 243 | 504990 | -89.05 | 8.14 | 552.65 | 0.13 | 2.46 | 1569 |

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
| 3211803 | 3 | 121.4755703829 | 31.1493681418 | 129 | 4 | 2 | 16.6 | TDD | 630 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3274267 | 2 | 121.4640367584 | 31.1495054794 | 264 | 12 | 1 | 41.0 | TDD | 243 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3274529 | 1 | 121.4695891786 | 31.1527810705 | 196 | 3 | 3 | 24.7 | TDD | 378 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3279976 | 4 | 121.4641972718 | 31.1515452460 | 64 | 6 | 5 | 21.9 | TDD | 207 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.853 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.874 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.012 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.012 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.730 | NREventA3 | measId:2;ServCellPCI:982;Se... |
| 2024-09-20 22:21:37.970 | NRHandoverAttempt | SourcePCI:982;SourceNR-ARFC... |
| 2024-09-20 22:21:38.017 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.031 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.164 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.164 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3274529 | 1 | 92.1728 | 92.0669 | -116.9193 | 13.3196 | 139.9391 | 0.0094 | 0.0178 |
| 2024_09_19 22:00 | 3274267 | 2 | 93.5511 | 91.0211 | -115.9062 | 9.6875 | 87.8920 | 0.0096 | 0.0186 |
| 2024_09_19 22:00 | 3211803 | 3 | 79.8095 | 77.4215 | -114.1545 | 14.2006 | 117.3465 | 0.0135 | 0.0192 |
| 2024_09_19 22:00 | 3279976 | 4 | 93.6017 | 91.4862 | -117.5048 | 11.4754 | 187.5726 | 0.0074 | 0.0167 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415775_89B6E8AC | 504990 | 243 | -86.6 | 504990 | 207 | -85.7 | 504990 | 630 | -97.0 | 504990 | 378 |
| MR_1774415775_9483CD7D | 504990 | 243 | -85.7 | 504990 | 207 | -89.0 | 504990 | 630 | -97.5 | 504990 | 378 |
| MR_1774415775_B16AE024 | 504990 | 243 | -83.8 | 504990 | 207 | -85.9 | 504990 | 630 | -97.6 | 504990 | 378 |
| MR_1774415775_4C550EDF | 504990 | 243 | -86.8 | 504990 | 207 | -88.8 | 504990 | 630 | -94.9 | 504990 | 378 |
| MR_1774415775_6C711E22 | 504990 | 243 | -85.4 | 504990 | 207 | -89.2 | 504990 | 630 | -94.1 | 504990 | 378 |
| MR_1774415775_974B8AF8 | 504990 | 243 | -86.7 | 504990 | 207 | -85.9 | 504990 | 630 | -94.3 | 504990 | 378 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 965: `553918b6-f38...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `553918b6-f38b-4601-bc1d-c38add2d2795` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[965] topology](images/train_0965.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3274583_1
- `C2`: Add neighbor relationship between 3244353_3 and 3274583_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274583_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228816_2
- `C5`: Decrease transmission power for 3228816_2
- `C6`: Lift the tilt angle of 3228816_2 by 10 degrees
- `C7`: Decrease A3 Offset threshold for 3228816_2
- `C8`: Check test server and transmission issues
- `C9`: Adjust the azimuth of 3228816_2 by 50 degrees
- `C10`: Press down the tilt angle of 3228816_2 by 10 degrees
- `C11`: Decrease transmission power for 3274583_1
- `C12`: Insufficient data; more data is needed for judgment. **← 정답**
- `C13`: Press down the tilt angle  of 3274583_1 by 8 degrees
- `C14`: Add neighbor relationship between 3228816_2 and 3274583_1
- `C15`: Decrease A3 Offset threshold for 3274583_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228816_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274583_1
- `C18`: Increase transmission power for 3228816_2
- `C19`: Increase A3 Offset threshold for 3228816_2
- `C20`: Increase transmission power for 3274583_1
- `C21`: Lift the tilt angle  of 3274583_1 by 8 degrees
- `C22`: Adjust the azimuth of 3274583_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.229 | MS1 | 121.4656632537 | 31.1446327723 | 244 | 504990 | -86.66 | 15.17 | 516.13 | 0.11 | 2.46 | 1586 |
| 2024-09-20 22:21:32.921 | MS1 | 121.4656661275 | 31.1446209888 | 244 | 504990 | -85.18 | 15.92 | 343.93 | 0.20 | 2.40 | 1560 |
| 2024-09-20 22:21:33.659 | MS1 | 121.4656710909 | 31.1446320838 | 244 | 504990 | -86.40 | 17.19 | 326.77 | 0.03 | 2.44 | 1575 |
| 2024-09-20 22:21:34.325 | MS1 | 121.4656623936 | 31.1446287924 | 244 | 504990 | -87.28 | 16.32 | 56.93 | 0.16 | 2.29 | 1593 |
| 2024-09-20 22:21:35.863 | MS1 | 121.4656732413 | 31.1446287314 | 244 | 504990 | -88.43 | 17.00 | 88.33 | 0.12 | 2.92 | 1598 |
| 2024-09-20 22:21:36.564 | MS1 | 121.4656589461 | 31.1446198092 | 244 | 504990 | -85.19 | 14.95 | 44.99 | 0.18 | 2.18 | 1576 |
| 2024-09-20 22:21:37.452 | MS1 | 121.4656690173 | 31.1446265701 | 244 | 504990 | -93.67 | 10.64 | 90.80 | 0.19 | 2.33 | 1573 |
| 2024-09-20 22:21:38.703 | MS1 | 121.4656727181 | 31.1446311890 | 244 | 504990 | -92.80 | 10.89 | 82.28 | 0.13 | 2.90 | 1574 |
| 2024-09-20 22:21:39.772 | MS1 | 121.4656684395 | 31.1446351795 | 244 | 504990 | -92.27 | 7.25 | 74.29 | 0.04 | 2.83 | 1569 |
| 2024-09-20 22:21:40.401 | MS1 | 121.4656612508 | 31.1446188402 | 244 | 504990 | -93.49 | 12.92 | 307.44 | 0.15 | 2.85 | 1574 |
| 2024-09-20 22:21:41.319 | MS1 | 121.4656679083 | 31.1446304028 | 244 | 504990 | -91.02 | 11.59 | 497.79 | 0.11 | 2.44 | 1587 |
| 2024-09-20 22:21:42.384 | MS1 | 121.4656767406 | 31.1446241532 | 244 | 504990 | -90.65 | 11.88 | 417.02 | 0.19 | 2.33 | 1565 |

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
| 3228816 | 2 | 121.4751956421 | 31.1510196616 | 42 | 13 | 5 | 44.1 | TDD | 244 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3230402 | 4 | 121.4668381758 | 31.1441351497 | 351 | 14 | 7 | 34.7 | TDD | 863 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3244353 | 3 | 121.4747950894 | 31.1451450135 | 222 | 10 | 10 | 32.2 | TDD | 6 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3274583 | 1 | 121.4684351891 | 31.1559880956 | 202 | 7 | 11 | 26.4 | TDD | 220 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.247 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.267 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.387 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.387 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.067 | NREventA3 | measId:2;ServCellPCI:649;Se... |
| 2024-09-20 22:21:38.307 | NRHandoverAttempt | SourcePCI:649;SourceNR-ARFC... |
| 2024-09-20 22:21:38.339 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.352 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.462 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.462 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3274583 | 1 | 76.1032 | 83.8525 | -117.6301 | 8.7577 | 123.7014 | 0.0076 | 0.0111 |
| 2024_09_19 22:00 | 3228816 | 2 | 77.7898 | 84.4089 | -117.1293 | 9.4962 | 93.0047 | 0.0029 | 0.0189 |
| 2024_09_19 22:00 | 3244353 | 3 | 84.0540 | 80.6153 | -117.2501 | 6.5810 | 109.3106 | 0.0152 | 0.0149 |
| 2024_09_19 22:00 | 3230402 | 4 | 91.8075 | 87.1770 | -116.8136 | 11.7582 | 110.6242 | 0.0180 | 0.0139 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413526_68DB7AD6 | 504990 | 244 | -86.1 | 504990 | 220 | -87.7 | 504990 | 6 | -101.6 | 504990 | 863 |
| MR_1774413526_8E6945A7 | 504990 | 244 | -88.2 | 504990 | 220 | -87.8 | 504990 | 6 | -98.0 | 504990 | 863 |
| MR_1774413526_810B5D5F | 504990 | 244 | -88.6 | 504990 | 220 | -89.5 | 504990 | 6 | -99.1 | 504990 | 863 |
| MR_1774413526_ED6CFFBA | 504990 | 244 | -87.3 | 504990 | 220 | -89.2 | 504990 | 6 | -101.4 | 504990 | 863 |
| MR_1774413526_DD306489 | 504990 | 244 | -86.4 | 504990 | 220 | -87.2 | 504990 | 6 | -99.4 | 504990 | 863 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 966: `f82f304c-719...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f82f304c-719e-40c8-830a-fc89d0b7bd50` |
| Tag | **multiple-answer** |
| 정답 | **C2|C11** |
| C2 의미 | Adjust the azimuth of 3223518_1 by 50 degrees |
| C11 의미 | Increase transmission power for 3223518_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[966] topology](images/train_0966.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223518_1
- `C2`: Adjust the azimuth of 3223518_1 by 50 degrees **← 정답**
- `C3`: Increase transmission power for 3219118_4
- `C4`: Increase A3 Offset threshold for 3223518_1
- `C5`: Adjust the azimuth of 3219118_4 by 37 degrees
- `C6`: Check test server and transmission issues
- `C7`: Press down the tilt angle  of 3219118_4 by 4 degrees
- `C8`: Lift the tilt angle of 3223518_1 by 10 degrees
- `C9`: Decrease transmission power for 3219118_4
- `C10`: Add neighbor relationship between 3255982_2 and 3219118_4
- `C11`: Increase transmission power for 3223518_1 **← 정답**
- `C12`: Increase A3 Offset threshold for 3219118_4
- `C13`: Press down the tilt angle of 3223518_1 by 10 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease transmission power for 3223518_1
- `C16`: Decrease A3 Offset threshold for 3219118_4
- `C17`: Decrease A3 Offset threshold for 3223518_1
- `C18`: Add neighbor relationship between 3223518_1 and 3219118_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219118_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219118_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223518_1
- `C22`: Lift the tilt angle  of 3219118_4 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.667 | MS1 | 121.4656762112 | 31.1446327486 | 810 | 504990 | -92.91 | 17.40 | 551.97 | 0.08 | 2.51 | 1586 |
| 2024-09-20 22:21:32.479 | MS1 | 121.4656728428 | 31.1446345997 | 810 | 504990 | -89.76 | 13.24 | 416.78 | 0.05 | 2.84 | 1596 |
| 2024-09-20 22:21:33.310 | MS1 | 121.4656623862 | 31.1446192031 | 810 | 504990 | -86.14 | 17.04 | 469.46 | 0.13 | 2.86 | 1560 |
| 2024-09-20 22:21:34.596 | MS1 | 121.4656742665 | 31.1446201917 | 810 | 504990 | -106.69 | 1.39 | 52.29 | 0.07 | 1.44 | 1587 |
| 2024-09-20 22:21:35.452 | MS1 | 121.4656767989 | 31.1446277050 | 810 | 504990 | -108.34 | 0.31 | 81.85 | 0.20 | 1.42 | 1585 |
| 2024-09-20 22:21:36.764 | MS1 | 121.4656684092 | 31.1446362489 | 810 | 504990 | -103.29 | 1.39 | 58.13 | 0.10 | 1.45 | 1582 |
| 2024-09-20 22:21:37.176 | MS1 | 121.4656752870 | 31.1446351274 | 810 | 504990 | -102.07 | -0.66 | 61.58 | 0.17 | 1.43 | 1568 |
| 2024-09-20 22:21:38.316 | MS1 | 121.4656768170 | 31.1446215152 | 810 | 504990 | -100.90 | -1.37 | 42.61 | 0.16 | 1.46 | 1584 |
| 2024-09-20 22:21:39.430 | MS1 | 121.4656670574 | 31.1446311044 | 810 | 504990 | -100.56 | -1.98 | 45.73 | 0.18 | 1.49 | 1564 |
| 2024-09-20 22:21:40.945 | MS1 | 121.4656649265 | 31.1446288932 | 810 | 504990 | -85.15 | 12.86 | 465.38 | 0.20 | 2.15 | 1567 |
| 2024-09-20 22:21:41.776 | MS1 | 121.4656617443 | 31.1446240291 | 810 | 504990 | -87.50 | 17.45 | 344.96 | 0.17 | 2.14 | 1590 |
| 2024-09-20 22:21:42.343 | MS1 | 121.4656705380 | 31.1446229913 | 810 | 504990 | -93.52 | 16.94 | 439.74 | 0.07 | 2.52 | 1581 |

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
| 3219118 | 4 | 121.4641628358 | 31.1541748992 | 135 | 2 | 0 | 42.2 | TDD | 735 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3223518 | 1 | 121.4700838444 | 31.1451948468 | 320 | 15 | 0 | 20.4 | TDD | 810 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3237519 | 3 | 121.4729453733 | 31.1547136628 | 28 | 2 | 4 | 38.9 | TDD | 149 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3255982 | 2 | 121.4656743264 | 31.1488016193 | 310 | 15 | 4 | 34.2 | TDD | 427 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.289 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.313 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.416 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.416 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.612 | NREventA2 | measId:1;ServCellPCI:799;Se... |
| 2024-09-20 22:21:34.755 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223518 | 1 | 14.3367 | 19.5936 | -114.3148 | 17.8361 | 178.1804 | 0.1105 | 0.0056 |
| 2024_09_20 22:00 | 3255982 | 2 | 13.5076 | 19.9633 | -116.5937 | 16.4819 | 191.7756 | 0.0130 | 0.0067 |
| 2024_09_20 22:00 | 3237519 | 3 | 7.1196 | 11.4408 | -117.6262 | 11.1344 | 140.4665 | 0.0020 | 0.0056 |
| 2024_09_20 22:00 | 3219118 | 4 | 15.4351 | 5.8992 | -115.1915 | 16.8608 | 142.7917 | 0.0104 | 0.0067 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414295_57394BD2 | 504990 | 810 | -107.6 | 504990 | 735 | -114.0 | 504990 | 427 | -117.8 | 504990 | 149 |
| MR_1774414295_412B7211 | 504990 | 810 | -106.4 | 504990 | 735 | -112.4 | 504990 | 427 | -115.7 | 504990 | 149 |
| MR_1774414295_14E2D99F | 504990 | 810 | -107.6 | 504990 | 735 | -113.7 | 504990 | 427 | -117.9 | 504990 | 149 |
| MR_1774414295_316D7EBE | 504990 | 810 | -107.9 | 504990 | 735 | -110.5 | 504990 | 427 | -114.5 | 504990 | 149 |
| MR_1774414295_C78F32D9 | 504990 | 810 | -105.7 | 504990 | 735 | -113.4 | 504990 | 427 | -117.6 | 504990 | 149 |
| MR_1774414295_3B76661C | 504990 | 810 | -108.2 | 504990 | 735 | -110.4 | 504990 | 427 | -117.7 | 504990 | 149 |
| MR_1774414295_59F86DEE | 504990 | 810 | -107.8 | 504990 | 735 | -112.5 | 504990 | 427 | -115.1 | 504990 | 149 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 967: `a8dea54c-083...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a8dea54c-083f-496f-a810-826816a60ebf` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[967] topology](images/train_0967.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3257617_1
- `C2`: Increase A3 Offset threshold for 3266662_4
- `C3`: Lift the tilt angle of 3266662_4 by 10 degrees
- `C4`: Add neighbor relationship between 3222426_2 and 3257617_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266662_4
- `C6`: Decrease transmission power for 3266662_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257617_1
- `C8`: Decrease A3 Offset threshold for 3266662_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257617_1
- `C10`: Check test server and transmission issues **← 정답**
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266662_4
- `C12`: Adjust the azimuth of 3266662_4 by 50 degrees
- `C13`: Press down the tilt angle of 3266662_4 by 10 degrees
- `C14`: Increase transmission power for 3257617_1
- `C15`: Adjust the azimuth of 3257617_1 by 27 degrees
- `C16`: Add neighbor relationship between 3266662_4 and 3257617_1
- `C17`: Increase A3 Offset threshold for 3257617_1
- `C18`: Decrease transmission power for 3257617_1
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Lift the tilt angle  of 3257617_1 by 10 degrees
- `C21`: Increase transmission power for 3266662_4
- `C22`: Press down the tilt angle  of 3257617_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.489 | MS1 | 121.4656772851 | 31.1446346210 | 333 | 504990 | -90.26 | 16.91 | 596.81 | 0.01 | 2.20 | 1566 |
| 2024-09-20 22:21:32.212 | MS1 | 121.4656590745 | 31.1446360207 | 333 | 504990 | -85.42 | 15.95 | 311.36 | 0.08 | 2.22 | 1585 |
| 2024-09-20 22:21:33.776 | MS1 | 121.4656624054 | 31.1446318456 | 333 | 504990 | -91.39 | 15.46 | 524.62 | 0.15 | 2.89 | 1583 |
| 2024-09-20 22:21:34.858 | MS1 | 121.4656765851 | 31.1446270094 | 333 | 504990 | -90.27 | 13.93 | 88.53 | 0.09 | 2.33 | 461 |
| 2024-09-20 22:21:35.237 | MS1 | 121.4656727836 | 31.1446248241 | 333 | 504990 | -88.14 | 16.33 | 50.24 | 0.19 | 2.40 | 451 |
| 2024-09-20 22:21:36.545 | MS1 | 121.4656582914 | 31.1446285450 | 333 | 504990 | -85.18 | 14.85 | 67.73 | 0.17 | 2.56 | 474 |
| 2024-09-20 22:21:37.687 | MS1 | 121.4656634533 | 31.1446260655 | 333 | 504990 | -91.18 | 7.80 | 67.57 | 0.05 | 2.56 | 392 |
| 2024-09-20 22:21:38.991 | MS1 | 121.4656661531 | 31.1446304915 | 333 | 504990 | -89.56 | 11.10 | 83.47 | 0.07 | 2.58 | 367 |
| 2024-09-20 22:21:39.815 | MS1 | 121.4656694904 | 31.1446241790 | 333 | 504990 | -92.30 | 7.71 | 59.87 | 0.16 | 2.64 | 347 |
| 2024-09-20 22:21:40.370 | MS1 | 121.4656596752 | 31.1446368914 | 333 | 504990 | -91.16 | 9.25 | 574.91 | 0.16 | 2.22 | 1586 |
| 2024-09-20 22:21:41.786 | MS1 | 121.4656751405 | 31.1446275379 | 333 | 504990 | -90.09 | 12.46 | 423.67 | 0.11 | 2.37 | 1593 |
| 2024-09-20 22:21:42.585 | MS1 | 121.4656643135 | 31.1446341258 | 333 | 504990 | -93.21 | 8.37 | 307.46 | 0.07 | 2.17 | 1568 |

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
| 3222196 | 3 | 121.4721969100 | 31.1552601458 | 288 | 2 | 6 | 36.0 | TDD | 836 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3222426 | 2 | 121.4746967248 | 31.1519748466 | 140 | 8 | 8 | 45.3 | TDD | 227 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3257617 | 1 | 121.4647776058 | 31.1531913428 | 202 | 10 | 9 | 36.2 | TDD | 432 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3266662 | 4 | 121.4757754671 | 31.1445293455 | 167 | 12 | 12 | 18.4 | TDD | 333 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.356 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.381 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.510 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.510 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.186 | NREventA3 | measId:2;ServCellPCI:530;Se... |
| 2024-09-20 22:21:38.426 | NRHandoverAttempt | SourcePCI:530;SourceNR-ARFC... |
| 2024-09-20 22:21:38.463 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.473 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.590 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.590 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257617 | 1 | 12.5282 | 16.6171 | -116.8194 | 11.4743 | 154.6269 | 0.0023 | 0.0115 |
| 2024_09_20 22:00 | 3222426 | 2 | 19.9234 | 17.8553 | -117.7835 | 6.2211 | 181.9749 | 0.0093 | 0.0154 |
| 2024_09_20 22:00 | 3222196 | 3 | 6.8632 | 12.5117 | -117.8581 | 7.2623 | 199.8408 | 0.0176 | 0.0023 |
| 2024_09_20 22:00 | 3266662 | 4 | 17.0776 | 18.3240 | -117.5683 | 17.5331 | 164.4642 | 0.0104 | 0.0058 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415469_11F77042 | 504990 | 333 | -91.9 | 504990 | 432 | -93.4 | 504990 | 227 | -97.0 | 504990 | 836 |
| MR_1774415469_4314F2D8 | 504990 | 333 | -92.0 | 504990 | 432 | -93.2 | 504990 | 227 | -98.9 | 504990 | 836 |
| MR_1774415469_6C5AB892 | 504990 | 333 | -90.2 | 504990 | 432 | -90.5 | 504990 | 227 | -96.6 | 504990 | 836 |
| MR_1774415469_A611FFCA | 504990 | 333 | -89.2 | 504990 | 432 | -91.6 | 504990 | 227 | -96.2 | 504990 | 836 |
| MR_1774415469_9E8FC66F | 504990 | 333 | -92.0 | 504990 | 432 | -91.4 | 504990 | 227 | -96.9 | 504990 | 836 |
| MR_1774415469_D9E7E096 | 504990 | 333 | -88.4 | 504990 | 432 | -90.5 | 504990 | 227 | -98.6 | 504990 | 836 |
| MR_1774415469_ED42E0E7 | 504990 | 333 | -88.8 | 504990 | 432 | -93.4 | 504990 | 227 | -97.1 | 504990 | 836 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 968: `c7465c6b-92b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c7465c6b-92bd-4dd8-a184-e36e4b79550d` |
| Tag | **multiple-answer** |
| 정답 | **C9|C11** |
| C9 의미 | Increase transmission power for 3243575_4 |
| C11 의미 | Adjust the azimuth of 3243575_4 by 32 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[968] topology](images/train_0968.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3243575_4
- `C2`: Decrease A3 Offset threshold for 3247800_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243575_4
- `C4`: Add neighbor relationship between 3243575_4 and 3247800_2
- `C5`: Add neighbor relationship between 3243031_3 and 3247800_2
- `C6`: Press down the tilt angle  of 3247800_2 by 3 degrees
- `C7`: Decrease transmission power for 3247800_2
- `C8`: Decrease A3 Offset threshold for 3243575_4
- `C9`: Increase transmission power for 3243575_4 **← 정답**
- `C10`: Increase A3 Offset threshold for 3247800_2
- `C11`: Adjust the azimuth of 3243575_4 by 32 degrees **← 정답**
- `C12`: Lift the tilt angle of 3243575_4 by 7 degrees
- `C13`: Increase A3 Offset threshold for 3243575_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247800_2
- `C15`: Lift the tilt angle  of 3247800_2 by 3 degrees
- `C16`: Adjust the azimuth of 3247800_2 by 12 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247800_2
- `C19`: Press down the tilt angle of 3243575_4 by 7 degrees
- `C20`: Check test server and transmission issues
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243575_4
- `C22`: Increase transmission power for 3247800_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.918 | MS1 | 121.4656598730 | 31.1446276249 | 878 | 504990 | -90.53 | 17.55 | 575.71 | 0.00 | 2.71 | 1590 |
| 2024-09-20 22:21:32.450 | MS1 | 121.4656737189 | 31.1446292717 | 878 | 504990 | -89.13 | 14.16 | 319.43 | 0.10 | 2.17 | 1570 |
| 2024-09-20 22:21:33.884 | MS1 | 121.4656591257 | 31.1446377273 | 878 | 504990 | -85.99 | 14.25 | 508.71 | 0.11 | 2.28 | 1577 |
| 2024-09-20 22:21:34.305 | MS1 | 121.4656632161 | 31.1446258045 | 878 | 504990 | -104.54 | 1.32 | 48.14 | 0.01 | 1.08 | 1593 |
| 2024-09-20 22:21:35.453 | MS1 | 121.4656747919 | 31.1446338180 | 878 | 504990 | -105.03 | 1.73 | 50.14 | 0.03 | 1.18 | 1566 |
| 2024-09-20 22:21:36.653 | MS1 | 121.4656712329 | 31.1446275058 | 878 | 504990 | -108.55 | 0.95 | 29.19 | 0.12 | 1.05 | 1586 |
| 2024-09-20 22:21:37.269 | MS1 | 121.4656621064 | 31.1446267358 | 878 | 504990 | -108.33 | 0.30 | 29.23 | 0.19 | 1.07 | 1563 |
| 2024-09-20 22:21:38.827 | MS1 | 121.4656599339 | 31.1446316233 | 878 | 504990 | -109.14 | 1.31 | 49.78 | 0.12 | 1.46 | 1570 |
| 2024-09-20 22:21:39.650 | MS1 | 121.4656693866 | 31.1446337904 | 878 | 504990 | -107.35 | 0.28 | 57.31 | 0.04 | 1.49 | 1567 |
| 2024-09-20 22:21:40.266 | MS1 | 121.4656762659 | 31.1446228297 | 878 | 504990 | -92.17 | 17.51 | 447.71 | 0.09 | 2.84 | 1579 |
| 2024-09-20 22:21:41.938 | MS1 | 121.4656779545 | 31.1446299445 | 878 | 504990 | -90.66 | 17.80 | 491.47 | 0.00 | 2.16 | 1560 |
| 2024-09-20 22:21:42.481 | MS1 | 121.4656684823 | 31.1446359377 | 878 | 504990 | -86.86 | 12.73 | 371.95 | 0.00 | 2.60 | 1569 |

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
| 3243031 | 3 | 121.4754307253 | 31.1537056154 | 303 | 15 | 4 | 26.1 | TDD | 525 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3243575 | 4 | 121.4650924939 | 31.1483230775 | 140 | 5 | 0 | 17.6 | TDD | 878 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3247800 | 2 | 121.4747807509 | 31.1456834175 | 274 | 1 | 0 | 31.9 | TDD | 193 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3269899 | 1 | 121.4755568113 | 31.1443233112 | 67 | 1 | 12 | 40.2 | TDD | 672 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.598 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.619 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.752 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.752 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.995 | NREventA2 | measId:1;ServCellPCI:952;Se... |
| 2024-09-20 22:21:35.101 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269899 | 1 | 15.7483 | 15.0457 | -116.3189 | 7.4272 | 87.8421 | 0.0018 | 0.0114 |
| 2024_09_20 22:00 | 3247800 | 2 | 9.5655 | 9.1713 | -114.8324 | 12.0364 | 128.3309 | 0.0034 | 0.0039 |
| 2024_09_20 22:00 | 3243031 | 3 | 19.2837 | 14.7459 | -115.0705 | 18.6204 | 191.8212 | 0.0197 | 0.0106 |
| 2024_09_20 22:00 | 3243575 | 4 | 11.7744 | 10.4434 | -116.0605 | 19.2877 | 128.8792 | 0.1737 | 0.0142 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416924_C9269ABF | 504990 | 878 | -103.3 | 504990 | 193 | -113.2 | 504990 | 525 | -120.1 | 504990 | 672 |
| MR_1774416924_96DC2916 | 504990 | 878 | -104.6 | 504990 | 193 | -112.7 | 504990 | 525 | -121.2 | 504990 | 672 |
| MR_1774416924_B83EE489 | 504990 | 878 | -102.7 | 504990 | 193 | -112.4 | 504990 | 525 | -117.9 | 504990 | 672 |
| MR_1774416924_3F792FE7 | 504990 | 878 | -104.0 | 504990 | 193 | -112.4 | 504990 | 525 | -119.1 | 504990 | 672 |
| MR_1774416924_EC285129 | 504990 | 878 | -102.9 | 504990 | 193 | -112.6 | 504990 | 525 | -120.5 | 504990 | 672 |
| MR_1774416924_A63C3529 | 504990 | 878 | -105.3 | 504990 | 193 | -113.8 | 504990 | 525 | -118.8 | 504990 | 672 |
| MR_1774416924_29A5C2C7 | 504990 | 878 | -102.8 | 504990 | 193 | -110.7 | 504990 | 525 | -117.5 | 504990 | 672 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 969: `0afb51e8-e6b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0afb51e8-e6b4-4e93-8186-f3ea8f97d6c5` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3214736_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[969] topology](images/train_0969.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3222850_2 by 10 degrees
- `C2`: Increase A3 Offset threshold for 3222850_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222850_2
- `C4`: Lift the tilt angle of 3214736_1 by 3 degrees
- `C5`: Decrease transmission power for 3222850_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214736_1
- `C7`: Increase transmission power for 3222850_2
- `C8`: Add neighbor relationship between 3214736_1 and 3222850_2
- `C9`: Adjust the azimuth of 3222850_2 by 50 degrees
- `C10`: Add neighbor relationship between 3223254_3 and 3222850_2
- `C11`: Decrease A3 Offset threshold for 3222850_2
- `C12`: Press down the tilt angle of 3214736_1 by 3 degrees
- `C13`: Increase transmission power for 3214736_1
- `C14`: Increase A3 Offset threshold for 3214736_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222850_2
- `C16`: Lift the tilt angle  of 3222850_2 by 10 degrees
- `C17`: Adjust the azimuth of 3214736_1 by 1 degrees
- `C18`: Decrease transmission power for 3214736_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214736_1 **← 정답**
- `C20`: Decrease A3 Offset threshold for 3214736_1
- `C21`: Check test server and transmission issues
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.393 | MS1 | 121.4656588583 | 31.1446184879 | 248 | 504990 | -86.29 | 12.65 | 466.56 | 0.02 | 2.86 | 1578 |
| 2024-09-20 22:21:32.882 | MS1 | 121.4656648612 | 31.1446226782 | 248 | 504990 | -85.30 | 17.49 | 303.59 | 0.05 | 2.82 | 1571 |
| 2024-09-20 22:21:33.281 | MS1 | 121.4656774926 | 31.1446189530 | 248 | 504990 | -85.60 | 15.12 | 341.04 | 0.19 | 2.39 | 1591 |
| 2024-09-20 22:21:34.938 | MS1 | 121.4656663551 | 31.1446378937 | 248 | 504990 | -87.91 | 12.61 | 96.36 | 0.50 | 2.11 | 599 |
| 2024-09-20 22:21:35.810 | MS1 | 121.4656617988 | 31.1446182417 | 248 | 504990 | -89.67 | 14.26 | 72.35 | 0.60 | 2.93 | 607 |
| 2024-09-20 22:21:36.500 | MS1 | 121.4656679699 | 31.1446304650 | 248 | 504990 | -88.98 | 13.72 | 81.54 | 0.66 | 2.33 | 584 |
| 2024-09-20 22:21:37.340 | MS1 | 121.4656754960 | 31.1446344413 | 248 | 504990 | -91.29 | 9.38 | 81.22 | 0.55 | 2.31 | 650 |
| 2024-09-20 22:21:38.422 | MS1 | 121.4656615489 | 31.1446332244 | 248 | 504990 | -92.05 | 9.96 | 71.35 | 0.61 | 2.45 | 661 |
| 2024-09-20 22:21:39.437 | MS1 | 121.4656648280 | 31.1446336191 | 248 | 504990 | -89.35 | 9.14 | 72.68 | 0.67 | 2.59 | 508 |
| 2024-09-20 22:21:40.960 | MS1 | 121.4656618530 | 31.1446185432 | 248 | 504990 | -90.68 | 8.65 | 519.98 | 0.09 | 2.16 | 1567 |
| 2024-09-20 22:21:41.608 | MS1 | 121.4656712154 | 31.1446192530 | 248 | 504990 | -89.32 | 7.43 | 463.79 | 0.16 | 2.77 | 1584 |
| 2024-09-20 22:21:42.196 | MS1 | 121.4656682110 | 31.1446362716 | 248 | 504990 | -91.46 | 11.19 | 468.28 | 0.15 | 2.54 | 1586 |

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
| 3214736 | 1 | 121.4720445441 | 31.1473423059 | 243 | 2 | 1 | 17.7 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3222850 | 2 | 121.4678744663 | 31.1552163956 | 24 | 15 | 4 | 25.2 | TDD | 780 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3223254 | 3 | 121.4678717560 | 31.1542916595 | 262 | 10 | 10 | 29.1 | TDD | 252 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3252738 | 4 | 121.4726309250 | 31.1525089608 | 143 | 10 | 3 | 49.9 | TDD | 439 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.993 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.008 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.139 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.139 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.837 | NREventA3 | measId:2;ServCellPCI:544;Se... |
| 2024-09-20 22:21:38.077 | NRHandoverAttempt | SourcePCI:544;SourceNR-ARFC... |
| 2024-09-20 22:21:38.112 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.127 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.250 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.250 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214736 | 1 | 11.6948 | 12.0997 | -115.2543 | 5.0591 | 134.2879 | 0.0043 | 0.0078 |
| 2024_09_20 22:00 | 3222850 | 2 | 12.9389 | 18.0639 | -114.2760 | 5.9743 | 104.7506 | 0.0080 | 0.0192 |
| 2024_09_20 22:00 | 3223254 | 3 | 6.9188 | 12.4194 | -117.4883 | 16.8145 | 84.1703 | 0.0017 | 0.0166 |
| 2024_09_20 22:00 | 3252738 | 4 | 16.3525 | 18.6854 | -116.1917 | 14.1725 | 199.7095 | 0.0163 | 0.0112 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412882_211C30B0 | 504990 | 248 | -86.8 | 504990 | 780 | -96.0 | 504990 | 252 | -101.2 | 504990 | 439 |
| MR_1774412882_734750B8 | 504990 | 248 | -85.9 | 504990 | 780 | -96.0 | 504990 | 252 | -99.4 | 504990 | 439 |
| MR_1774412882_3D9CB5FA | 504990 | 248 | -87.4 | 504990 | 780 | -94.3 | 504990 | 252 | -100.4 | 504990 | 439 |
| MR_1774412882_992E629C | 504990 | 248 | -86.9 | 504990 | 780 | -94.6 | 504990 | 252 | -100.5 | 504990 | 439 |
| MR_1774412882_F1AA11DD | 504990 | 248 | -88.3 | 504990 | 780 | -97.6 | 504990 | 252 | -101.2 | 504990 | 439 |
| MR_1774412882_0D117FAF | 504990 | 248 | -87.6 | 504990 | 780 | -97.4 | 504990 | 252 | -102.3 | 504990 | 439 |
| MR_1774412882_A344A7AC | 504990 | 248 | -86.5 | 504990 | 780 | -94.7 | 504990 | 252 | -101.2 | 504990 | 439 |
| MR_1774412882_3A788EF2 | 504990 | 248 | -87.5 | 504990 | 780 | -96.7 | 504990 | 252 | -100.2 | 504990 | 439 |

> *... 2개 열 생략 (전체 14열)*

---
