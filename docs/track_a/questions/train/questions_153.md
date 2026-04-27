# Track A 문제 분석 — train[1520]~train[1529]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1520] ~ train[1529] (10개)

## 목차

1. [문제 1520: `2cd5711c-6bc...`](#1520) — single-answer, 정답: C1
2. [문제 1521: `317b2473-5ee...`](#1521) — single-answer, 정답: C1
3. [문제 1522: `699fd9b7-0be...`](#1522) — single-answer, 정답: C21
4. [문제 1523: `a71fc88e-2d6...`](#1523) — single-answer, 정답: C5
5. [문제 1524: `95a880e0-14a...`](#1524) — single-answer, 정답: C18
6. [문제 1525: `0579b3e4-17b...`](#1525) — single-answer, 정답: C7
7. [문제 1526: `278c1825-875...`](#1526) — single-answer, 정답: C15
8. [문제 1527: `1d08f74a-a9d...`](#1527) — single-answer, 정답: C10
9. [문제 1528: `48a07e15-6bf...`](#1528) — single-answer, 정답: C19
10. [문제 1529: `2f96744c-629...`](#1529) — single-answer, 정답: C4

---

### 문제 1520: `2cd5711c-6bc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2cd5711c-6bc3-4f93-b171-e8fb227489a7` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266431_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1520] topology](images/train_1520.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266431_3 **← 정답**
- `C2`: Decrease transmission power for 3236193_5
- `C3`: Decrease A3 Offset threshold for 3266431_3
- `C4`: Add neighbor relationship between 3237394_9 and 3236193_5
- `C5`: Add neighbor relationship between 3266431_3 and 3236193_5
- `C6`: Increase transmission power for 3266431_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236193_5
- `C8`: Increase A3 Offset threshold for 3266431_3
- `C9`: Press down the tilt angle  of 3236193_5 by 5 degrees
- `C10`: Decrease A3 Offset threshold for 3236193_5
- `C11`: Increase transmission power for 3236193_5
- `C12`: Lift the tilt angle  of 3236193_5 by 5 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266431_3
- `C14`: Check test server and transmission issues
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Press down the tilt angle of 3266431_3 by 6 degrees
- `C17`: Increase A3 Offset threshold for 3236193_5
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236193_5
- `C19`: Lift the tilt angle of 3266431_3 by 6 degrees
- `C20`: Decrease transmission power for 3266431_3
- `C21`: Adjust the azimuth of 3236193_5 by 2 degrees
- `C22`: Adjust the azimuth of 3266431_3 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.776 | MS1 | 121.4656642532 | 31.1446290676 | 817 | 504990 | -94.53 | 12.40 | 453.91 | 0.14 | 2.56 | 1565 |
| 2024-09-20 22:21:32.464 | MS1 | 121.4656693343 | 31.1446360572 | 623 | 504990 | -93.23 | 9.33 | 538.01 | 0.15 | 2.09 | 1570 |
| 2024-09-20 22:21:33.509 | MS1 | 121.4656728934 | 31.1446368435 | 507 | 504990 | -93.75 | 12.99 | 564.55 | 0.15 | 2.89 | 1564 |
| 2024-09-20 22:21:34.529 | MS1 | 121.4656638108 | 31.1446190060 | 638 | 152650 | -91.05 | 5.89 | 43.04 | 0.06 | 1.82 | 937 |
| 2024-09-20 22:21:35.500 | MS1 | 121.4656663408 | 31.1446329354 | 340 | 152650 | -90.13 | 3.64 | 55.40 | 0.12 | 1.67 | 935 |
| 2024-09-20 22:21:36.270 | MS1 | 121.4656771468 | 31.1446235017 | 653 | 152650 | -87.80 | 2.04 | 92.00 | 0.05 | 1.61 | 999 |
| 2024-09-20 22:21:37.271 | MS1 | 121.4656718644 | 31.1446193231 | 410 | 152650 | -87.42 | 7.83 | 52.74 | 0.14 | 1.99 | 977 |
| 2024-09-20 22:21:38.122 | MS1 | 121.4656732215 | 31.1446340805 | 638 | 152650 | -96.22 | 5.65 | 72.14 | 0.17 | 1.96 | 932 |
| 2024-09-20 22:21:39.807 | MS1 | 121.4656736411 | 31.1446235835 | 340 | 152650 | -87.49 | 3.05 | 83.87 | 0.08 | 1.67 | 960 |
| 2024-09-20 22:21:40.195 | MS1 | 121.4656582776 | 31.1446276888 | 653 | 152650 | -92.14 | 3.90 | 91.39 | 0.02 | 2.16 | 1573 |
| 2024-09-20 22:21:41.925 | MS1 | 121.4656694538 | 31.1446336367 | 410 | 152650 | -93.49 | 6.67 | 78.16 | 0.18 | 2.26 | 1597 |
| 2024-09-20 22:21:42.271 | MS1 | 121.4656591642 | 31.1446333845 | 638 | 152650 | -93.95 | 6.31 | 66.69 | 0.03 | 2.69 | 1575 |

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
| 3211264 | 12 | 121.4676583012 | 31.1559237074 | 159 | 6 | 1 | 18.1 | FDD | 638 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3215402 | 7 | 121.4724206987 | 31.1540854546 | 91 | 8 | 5 | 26.9 | FDD | 393 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3229859 | 10 | 121.4717922743 | 31.1539528695 | 70 | 0 | 8 | 11.6 | FDD | 340 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3233369 | 8 | 121.4734110034 | 31.1549862935 | 166 | 12 | 3 | 25.6 | FDD | 970 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3234438 | 1 | 121.4656731702 | 31.1469209790 | 347 | 13 | 0 | 11.3 | TDD | 36 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3236193 | 5 | 121.4651900357 | 31.1512339577 | 178 | 3 | 11 | 25.8 | TDD | 820 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3237394 | 9 | 121.4644176786 | 31.1498088350 | 228 | 13 | 10 | 12.3 | FDD | 653 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3247768 | 2 | 121.4644383742 | 31.1504653953 | 62 | 2 | 0 | 5.4 | TDD | 623 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3252993 | 4 | 121.4758550110 | 31.1462692799 | 64 | 2 | 5 | 22.0 | TDD | 850 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3266431 | 3 | 121.4653723519 | 31.1449020788 | 89 | 5 | 3 | 0.4 | TDD | 817 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3277221 | 6 | 121.4692707909 | 31.1478434274 | 39 | 9 | 6 | 22.7 | TDD | 507 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3277848 | 11 | 121.4660176354 | 31.1532978603 | 214 | 2 | 4 | 8.0 | FDD | 410 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3279164 | 13 | 121.4737178562 | 31.1489650059 | 139 | 7 | 6 | 16.5 | FDD | 31 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |

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
| 2024-09-20 22:21:31.036 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.054 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.185 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.185 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.857 | NREventA2 | measId:1;ServCellPCI:549;Se... |
| 2024-09-20 22:21:34.969 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.226 | NREventA5 | measId:3;ServCellPCI:549;Se... |
| 2024-09-20 22:21:35.272 | NRHandoverAttempt | SourcePCI:549;SourceNR-ARFC... |
| 2024-09-20 22:21:35.322 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.335 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.444 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.444 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234438 | 1 | 15.7002 | 17.9394 | -116.0342 | 15.1586 | 140.9377 | 0.0033 | 0.0086 |
| 2024_09_20 22:00 | 3247768 | 2 | 13.9815 | 5.3453 | -117.5430 | 10.6917 | 152.4990 | 0.0096 | 0.0131 |
| 2024_09_20 22:00 | 3266431 | 3 | 14.1832 | 14.1184 | -117.5266 | 7.4090 | 93.1123 | 0.0134 | 0.0039 |
| 2024_09_20 22:00 | 3252993 | 4 | 11.6216 | 18.1725 | -115.6110 | 7.1743 | 156.8647 | 0.0147 | 0.0135 |
| 2024_09_20 22:00 | 3236193 | 5 | 8.4808 | 5.3515 | -117.4978 | 16.1576 | 180.5302 | 0.0054 | 0.0049 |
| 2024_09_20 22:00 | 3277221 | 6 | 15.3996 | 9.3044 | -116.7512 | 11.7992 | 139.6019 | 0.0050 | 0.0176 |
| 2024_09_20 22:00 | 3215402 | 7 | 16.3102 | 8.8418 | -114.1910 | 4.6579 | 20.8269 | 0.0069 | 0.0119 |
| 2024_09_20 22:00 | 3233369 | 8 | 7.1050 | 19.5950 | -116.5105 | 4.7676 | 30.9400 | 0.0075 | 0.0188 |
| 2024_09_20 22:00 | 3237394 | 9 | 19.7750 | 17.7368 | -117.0224 | 4.6690 | 53.3535 | 0.0125 | 0.0168 |
| 2024_09_20 22:00 | 3229859 | 10 | 14.2044 | 13.3636 | -115.9594 | 3.6317 | 23.5223 | 0.0044 | 0.0155 |
| 2024_09_20 22:00 | 3277848 | 11 | 7.4084 | 15.2649 | -114.7048 | 4.2852 | 26.2141 | 0.0078 | 0.0029 |
| 2024_09_20 22:00 | 3211264 | 12 | 18.0048 | 12.1765 | -114.0486 | 3.5983 | 48.7282 | 0.0179 | 0.0141 |
| 2024_09_20 22:00 | 3279164 | 13 | 17.8476 | 18.5400 | -115.7393 | 4.9097 | 25.8787 | 0.0162 | 0.0106 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417176_BE695329 | 504990 | 507 | -95.4 | 504990 | 820 | -94.5 | 504990 | 36 | -94.4 | 504990 | 850 |
| MR_1774417176_8CCE75AD | 152650 | 638 | -91.4 | 152650 | 970 | -94.3 | 152650 | 31 | -102.7 | 152650 | 393 |
| MR_1774417176_FB64B694 | 152650 | 638 | -90.2 | 152650 | 970 | -95.4 | 152650 | 31 | -100.5 | 152650 | 393 |
| MR_1774417176_D0D67E79 | 152650 | 638 | -89.3 | 152650 | 970 | -96.4 | 152650 | 31 | -102.9 | 152650 | 393 |
| MR_1774417176_0BEB4FAC | 504990 | 507 | -94.4 | 504990 | 820 | -92.2 | 504990 | 36 | -96.8 | 504990 | 850 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1521: `317b2473-5ee...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `317b2473-5eeb-434b-9d47-6545e9da5d7d` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1521] topology](images/train_1521.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues **← 정답**
- `C2`: Adjust the azimuth of 3229275_1 by 50 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229275_1
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease A3 Offset threshold for 3229275_1
- `C6`: Decrease transmission power for 3244023_3
- `C7`: Decrease transmission power for 3229275_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229275_1
- `C9`: Press down the tilt angle of 3229275_1 by 4 degrees
- `C10`: Press down the tilt angle  of 3244023_3 by 10 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244023_3
- `C12`: Adjust the azimuth of 3244023_3 by 50 degrees
- `C13`: Increase A3 Offset threshold for 3244023_3
- `C14`: Add neighbor relationship between 3229275_1 and 3244023_3
- `C15`: Increase transmission power for 3244023_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244023_3
- `C17`: Lift the tilt angle  of 3244023_3 by 10 degrees
- `C18`: Decrease A3 Offset threshold for 3244023_3
- `C19`: Lift the tilt angle of 3229275_1 by 4 degrees
- `C20`: Add neighbor relationship between 3264631_2 and 3244023_3
- `C21`: Increase transmission power for 3229275_1
- `C22`: Increase A3 Offset threshold for 3229275_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.251 | MS1 | 121.4656655358 | 31.1446180064 | 592 | 504990 | -90.39 | 15.06 | 513.72 | 0.17 | 2.03 | 1581 |
| 2024-09-20 22:21:32.669 | MS1 | 121.4656607489 | 31.1446257312 | 592 | 504990 | -87.12 | 14.56 | 350.69 | 0.11 | 2.25 | 1591 |
| 2024-09-20 22:21:33.657 | MS1 | 121.4656600466 | 31.1446335883 | 592 | 504990 | -87.36 | 16.55 | 473.58 | 0.10 | 2.26 | 1573 |
| 2024-09-20 22:21:34.986 | MS1 | 121.4656778368 | 31.1446254314 | 592 | 504990 | -90.59 | 16.60 | 65.43 | 0.05 | 2.18 | 328 |
| 2024-09-20 22:21:35.597 | MS1 | 121.4656582373 | 31.1446260155 | 592 | 504990 | -87.45 | 17.19 | 91.34 | 0.06 | 2.44 | 342 |
| 2024-09-20 22:21:36.190 | MS1 | 121.4656638757 | 31.1446214934 | 592 | 504990 | -90.97 | 13.14 | 72.37 | 0.09 | 2.25 | 378 |
| 2024-09-20 22:21:37.410 | MS1 | 121.4656645776 | 31.1446367293 | 592 | 504990 | -90.31 | 7.24 | 55.00 | 0.06 | 2.33 | 391 |
| 2024-09-20 22:21:38.173 | MS1 | 121.4656779135 | 31.1446366534 | 592 | 504990 | -91.74 | 9.79 | 94.01 | 0.15 | 2.87 | 493 |
| 2024-09-20 22:21:39.633 | MS1 | 121.4656726586 | 31.1446235068 | 592 | 504990 | -93.52 | 11.84 | 56.10 | 0.08 | 2.53 | 353 |
| 2024-09-20 22:21:40.765 | MS1 | 121.4656666638 | 31.1446184941 | 592 | 504990 | -92.64 | 8.30 | 347.08 | 0.00 | 2.85 | 1593 |
| 2024-09-20 22:21:41.245 | MS1 | 121.4656774842 | 31.1446208795 | 592 | 504990 | -90.63 | 11.69 | 462.14 | 0.19 | 2.68 | 1600 |
| 2024-09-20 22:21:42.984 | MS1 | 121.4656709223 | 31.1446379854 | 592 | 504990 | -89.85 | 10.49 | 478.78 | 0.13 | 2.61 | 1571 |

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
| 3220980 | 4 | 121.4756478602 | 31.1507670961 | 45 | 12 | 10 | 32.9 | TDD | 668 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3229275 | 1 | 121.4695397009 | 31.1473432548 | 159 | 1 | 11 | 21.6 | TDD | 592 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3244023 | 3 | 121.4737667274 | 31.1469773500 | 302 | 10 | 4 | 26.0 | TDD | 426 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3264631 | 2 | 121.4755594041 | 31.1522761556 | 333 | 3 | 4 | 25.1 | TDD | 148 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.131 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.155 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.279 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.279 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.024 | NREventA3 | measId:2;ServCellPCI:866;Se... |
| 2024-09-20 22:21:38.264 | NRHandoverAttempt | SourcePCI:866;SourceNR-ARFC... |
| 2024-09-20 22:21:38.306 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.316 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.465 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.465 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229275 | 1 | 18.2820 | 11.0542 | -114.5156 | 13.3615 | 111.6555 | 0.0183 | 0.0197 |
| 2024_09_20 22:00 | 3264631 | 2 | 12.4460 | 18.3087 | -116.2047 | 17.2170 | 80.3889 | 0.0095 | 0.0048 |
| 2024_09_20 22:00 | 3244023 | 3 | 18.5055 | 14.8648 | -117.9286 | 6.0414 | 199.3407 | 0.0148 | 0.0183 |
| 2024_09_20 22:00 | 3220980 | 4 | 12.5419 | 18.3551 | -117.5066 | 16.8950 | 159.1918 | 0.0063 | 0.0065 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416695_DE98CDB1 | 504990 | 592 | -88.7 | 504990 | 426 | -95.8 | 504990 | 148 | -99.2 | 504990 | 668 |
| MR_1774416695_2E746B60 | 504990 | 592 | -92.4 | 504990 | 426 | -93.7 | 504990 | 148 | -97.4 | 504990 | 668 |
| MR_1774416695_367576B2 | 504990 | 592 | -92.4 | 504990 | 426 | -96.0 | 504990 | 148 | -100.0 | 504990 | 668 |
| MR_1774416695_8B8D1861 | 504990 | 592 | -92.1 | 504990 | 426 | -93.9 | 504990 | 148 | -100.3 | 504990 | 668 |
| MR_1774416695_BDC55998 | 504990 | 592 | -89.4 | 504990 | 426 | -96.6 | 504990 | 148 | -99.3 | 504990 | 668 |
| MR_1774416695_BBF6BB78 | 504990 | 592 | -88.8 | 504990 | 426 | -95.6 | 504990 | 148 | -97.3 | 504990 | 668 |
| MR_1774416695_9A38975D | 504990 | 592 | -90.4 | 504990 | 426 | -94.4 | 504990 | 148 | -99.1 | 504990 | 668 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1522: `699fd9b7-0be...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `699fd9b7-0bed-47c1-bde7-6d4d6fb8b121` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Lift the tilt angle  of 3266513_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1522] topology](images/train_1522.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3246282_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252824_1
- `C3`: Adjust the azimuth of 3266513_4 by 50 degrees
- `C4`: Increase A3 Offset threshold for 3246282_3
- `C5`: Press down the tilt angle  of 3266513_4 by 10 degrees
- `C6`: Lift the tilt angle of 3252824_1 by 3 degrees
- `C7`: Check test server and transmission issues
- `C8`: Add neighbor relationship between 3252824_1 and 3246282_3
- `C9`: Increase transmission power for 3252824_1
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Adjust the azimuth of 3252824_1 by 4 degrees
- `C12`: Add neighbor relationship between 3266513_4 and 3246282_3
- `C13`: Increase transmission power for 3246282_3
- `C14`: Increase A3 Offset threshold for 3252824_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246282_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246282_3
- `C17`: Press down the tilt angle of 3252824_1 by 3 degrees
- `C18`: Decrease A3 Offset threshold for 3246282_3
- `C19`: Decrease transmission power for 3252824_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252824_1
- `C21`: Lift the tilt angle  of 3266513_4 by 10 degrees **← 정답**
- `C22`: Decrease A3 Offset threshold for 3252824_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.995 | MS1 | 121.4656685012 | 31.1446280537 | 978 | 504990 | -89.76 | 16.55 | 378.29 | 0.10 | 2.01 | 1584 |
| 2024-09-20 22:21:32.516 | MS1 | 121.4656596485 | 31.1446334002 | 978 | 504990 | -86.53 | 12.10 | 574.66 | 0.06 | 2.56 | 1571 |
| 2024-09-20 22:21:33.960 | MS1 | 121.4656749301 | 31.1446283022 | 978 | 504990 | -91.17 | 15.08 | 463.89 | 0.03 | 2.25 | 1576 |
| 2024-09-20 22:21:34.398 | MS1 | 121.4656732102 | 31.1446191165 | 978 | 504990 | -85.93 | 15.46 | 62.31 | 0.08 | 2.32 | 1563 |
| 2024-09-20 22:21:35.929 | MS1 | 121.4656601732 | 31.1446197752 | 978 | 504990 | -87.91 | 15.68 | 73.00 | 0.05 | 2.55 | 1561 |
| 2024-09-20 22:21:36.501 | MS1 | 121.4656708078 | 31.1446199754 | 978 | 504990 | -89.29 | 13.92 | 62.26 | 0.04 | 2.24 | 1579 |
| 2024-09-20 22:21:37.378 | MS1 | 121.4656752773 | 31.1446234603 | 978 | 504990 | -91.95 | 10.74 | 90.61 | 0.02 | 2.13 | 1566 |
| 2024-09-20 22:21:38.398 | MS1 | 121.4656588081 | 31.1446312509 | 978 | 504990 | -93.51 | 11.93 | 60.10 | 0.12 | 2.88 | 1579 |
| 2024-09-20 22:21:39.401 | MS1 | 121.4656659524 | 31.1446330662 | 978 | 504990 | -89.23 | 9.78 | 68.33 | 0.00 | 2.88 | 1578 |
| 2024-09-20 22:21:40.395 | MS1 | 121.4656720573 | 31.1446297099 | 978 | 504990 | -91.32 | 7.28 | 583.51 | 0.11 | 2.68 | 1595 |
| 2024-09-20 22:21:41.312 | MS1 | 121.4656670147 | 31.1446280531 | 978 | 504990 | -91.64 | 9.16 | 468.56 | 0.02 | 2.90 | 1596 |
| 2024-09-20 22:21:42.894 | MS1 | 121.4656628487 | 31.1446281021 | 978 | 504990 | -93.34 | 12.24 | 487.73 | 0.17 | 2.74 | 1587 |

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
| 3236388 | 2 | 121.4739950049 | 31.1469070567 | 143 | 11 | 12 | 39.9 | TDD | 11 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3246282 | 3 | 121.4742307932 | 31.1458677648 | 28 | 7 | 8 | 45.7 | TDD | 334 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3252824 | 1 | 121.4689950054 | 31.1550060766 | 199 | 1 | 11 | 46.3 | TDD | 978 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3266513 | 4 | 121.4689976439 | 31.1549147213 | 5 | 3 | 5 | 23.8 | TDD | 359 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.854 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.878 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.010 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.010 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.694 | NREventA3 | measId:2;ServCellPCI:924;Se... |
| 2024-09-20 22:21:37.934 | NRHandoverAttempt | SourcePCI:924;SourceNR-ARFC... |
| 2024-09-20 22:21:37.964 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.978 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.087 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.087 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252824 | 1 | 82.4537 | 92.9919 | -116.8044 | 18.1341 | 173.6630 | 0.0056 | 0.0147 |
| 2024_09_20 22:00 | 3236388 | 2 | 11.8235 | 15.4755 | -114.1149 | 14.9477 | 152.0315 | 0.0187 | 0.0131 |
| 2024_09_20 22:00 | 3246282 | 3 | 8.3303 | 7.8748 | -116.4880 | 13.4612 | 124.0642 | 0.0070 | 0.0183 |
| 2024_09_20 22:00 | 3266513 | 4 | 8.8182 | 7.1169 | -117.0787 | 11.0538 | 102.9557 | 0.0190 | 0.0008 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416147_D753E410 | 504990 | 978 | -86.1 | 504990 | 334 | -92.5 | 504990 | 359 | -100.6 | 504990 | 11 |
| MR_1774416147_F0B1D8CD | 504990 | 978 | -84.3 | 504990 | 334 | -93.0 | 504990 | 359 | -100.3 | 504990 | 11 |
| MR_1774416147_F79F238F | 504990 | 978 | -85.5 | 504990 | 334 | -92.7 | 504990 | 359 | -101.2 | 504990 | 11 |
| MR_1774416147_A9788100 | 504990 | 978 | -85.6 | 504990 | 334 | -92.8 | 504990 | 359 | -101.4 | 504990 | 11 |
| MR_1774416147_19BB37E3 | 504990 | 978 | -84.8 | 504990 | 334 | -93.9 | 504990 | 359 | -97.9 | 504990 | 11 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1523: `a71fc88e-2d6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a71fc88e-2d68-4a40-a706-f26c2fe23f7b` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Lift the tilt angle  of 3278556_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1523] topology](images/train_1523.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3250099_3 by 29 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241606_1
- `C3`: Lift the tilt angle of 3250099_3 by 1 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241606_1
- `C5`: Lift the tilt angle  of 3278556_4 by 10 degrees **← 정답**
- `C6`: Adjust the azimuth of 3278556_4 by 8 degrees
- `C7`: Increase transmission power for 3250099_3
- `C8`: Increase transmission power for 3241606_1
- `C9`: Decrease transmission power for 3241606_1
- `C10`: Add neighbor relationship between 3250099_3 and 3241606_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250099_3
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Press down the tilt angle of 3250099_3 by 1 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250099_3
- `C15`: Add neighbor relationship between 3278556_4 and 3241606_1
- `C16`: Decrease transmission power for 3250099_3
- `C17`: Increase A3 Offset threshold for 3241606_1
- `C18`: Decrease A3 Offset threshold for 3250099_3
- `C19`: Decrease A3 Offset threshold for 3241606_1
- `C20`: Increase A3 Offset threshold for 3250099_3
- `C21`: Check test server and transmission issues
- `C22`: Press down the tilt angle  of 3278556_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.979 | MS1 | 121.4656710029 | 31.1446316434 | 357 | 504990 | -91.09 | 14.01 | 497.99 | 0.18 | 2.42 | 1567 |
| 2024-09-20 22:21:32.831 | MS1 | 121.4656605073 | 31.1446279413 | 357 | 504990 | -91.62 | 15.87 | 492.89 | 0.02 | 2.49 | 1599 |
| 2024-09-20 22:21:33.493 | MS1 | 121.4656721805 | 31.1446308824 | 357 | 504990 | -88.46 | 15.37 | 449.99 | 0.03 | 2.76 | 1582 |
| 2024-09-20 22:21:34.788 | MS1 | 121.4656605486 | 31.1446296772 | 357 | 504990 | -90.18 | 16.82 | 78.69 | 0.00 | 2.65 | 1582 |
| 2024-09-20 22:21:35.823 | MS1 | 121.4656608649 | 31.1446371978 | 357 | 504990 | -90.78 | 15.66 | 66.52 | 0.18 | 2.54 | 1591 |
| 2024-09-20 22:21:36.351 | MS1 | 121.4656622575 | 31.1446213274 | 357 | 504990 | -91.43 | 16.99 | 82.46 | 0.19 | 2.99 | 1576 |
| 2024-09-20 22:21:37.398 | MS1 | 121.4656672849 | 31.1446299965 | 357 | 504990 | -89.46 | 10.59 | 61.50 | 0.17 | 2.10 | 1585 |
| 2024-09-20 22:21:38.238 | MS1 | 121.4656619552 | 31.1446277957 | 357 | 504990 | -92.88 | 11.92 | 83.73 | 0.11 | 2.45 | 1560 |
| 2024-09-20 22:21:39.908 | MS1 | 121.4656593726 | 31.1446305283 | 357 | 504990 | -92.80 | 10.73 | 87.93 | 0.01 | 2.28 | 1594 |
| 2024-09-20 22:21:40.915 | MS1 | 121.4656599060 | 31.1446284910 | 357 | 504990 | -89.16 | 8.42 | 338.43 | 0.09 | 2.77 | 1583 |
| 2024-09-20 22:21:41.891 | MS1 | 121.4656712213 | 31.1446352420 | 357 | 504990 | -89.57 | 8.90 | 446.27 | 0.17 | 2.73 | 1560 |
| 2024-09-20 22:21:42.807 | MS1 | 121.4656658967 | 31.1446199062 | 357 | 504990 | -90.35 | 8.07 | 588.72 | 0.08 | 2.06 | 1591 |

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
| 3241606 | 1 | 121.4719945601 | 31.1512357328 | 227 | 11 | 0 | 31.8 | TDD | 656 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3250099 | 3 | 121.4708162345 | 31.1554852563 | 231 | 0 | 3 | 26.7 | TDD | 357 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3264409 | 2 | 121.4727126779 | 31.1557684934 | 140 | 13 | 7 | 36.6 | TDD | 68 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3278556 | 4 | 121.4662962292 | 31.1501065330 | 77 | 5 | 11 | 18.7 | TDD | 14 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.494 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.510 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.618 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.618 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.329 | NREventA3 | measId:2;ServCellPCI:724;Se... |
| 2024-09-20 22:21:38.569 | NRHandoverAttempt | SourcePCI:724;SourceNR-ARFC... |
| 2024-09-20 22:21:38.604 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.618 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.724 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.724 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241606 | 1 | 12.8681 | 13.1879 | -115.7279 | 6.9549 | 180.0155 | 0.0070 | 0.0175 |
| 2024_09_20 22:00 | 3264409 | 2 | 12.3396 | 14.0549 | -116.1667 | 13.3798 | 124.6717 | 0.0026 | 0.0175 |
| 2024_09_20 22:00 | 3250099 | 3 | 92.6589 | 83.2583 | -117.4077 | 18.3770 | 189.3245 | 0.0112 | 0.0191 |
| 2024_09_20 22:00 | 3278556 | 4 | 5.7627 | 12.4594 | -115.0018 | 6.4581 | 127.9804 | 0.0033 | 0.0196 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412077_681736BD | 504990 | 357 | -88.6 | 504990 | 656 | -89.9 | 504990 | 14 | -100.4 | 504990 | 68 |
| MR_1774412077_88E635B3 | 504990 | 357 | -89.2 | 504990 | 656 | -90.8 | 504990 | 14 | -102.4 | 504990 | 68 |
| MR_1774412077_376D696A | 504990 | 357 | -90.8 | 504990 | 656 | -92.4 | 504990 | 14 | -100.0 | 504990 | 68 |
| MR_1774412077_CEF68D62 | 504990 | 357 | -90.3 | 504990 | 656 | -91.8 | 504990 | 14 | -101.2 | 504990 | 68 |
| MR_1774412077_D22A8815 | 504990 | 357 | -89.7 | 504990 | 656 | -91.3 | 504990 | 14 | -101.9 | 504990 | 68 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1524: `95a880e0-14a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `95a880e0-14ae-4578-8fa4-2998ad04c6b4` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Add neighbor relationship between 3278478_4 and 3211917_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1524] topology](images/train_1524.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3278478_4
- `C2`: Increase transmission power for 3211917_1
- `C3`: Lift the tilt angle of 3278478_4 by 5 degrees
- `C4`: Lift the tilt angle  of 3211917_1 by 6 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211917_1
- `C6`: Decrease transmission power for 3211917_1
- `C7`: Decrease A3 Offset threshold for 3278478_4
- `C8`: Adjust the azimuth of 3211917_1 by 7 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211917_1
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278478_4
- `C12`: Press down the tilt angle of 3278478_4 by 5 degrees
- `C13`: Decrease A3 Offset threshold for 3211917_1
- `C14`: Check test server and transmission issues
- `C15`: Decrease transmission power for 3278478_4
- `C16`: Add neighbor relationship between 3243198_2 and 3211917_1
- `C17`: Increase transmission power for 3278478_4
- `C18`: Add neighbor relationship between 3278478_4 and 3211917_1 **← 정답**
- `C19`: Increase A3 Offset threshold for 3211917_1
- `C20`: Press down the tilt angle  of 3211917_1 by 6 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278478_4
- `C22`: Adjust the azimuth of 3278478_4 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.859 | MS1 | 121.4656723978 | 31.1446340684 | 823 | 504990 | -76.77 | 15.93 | 478.67 | 0.05 | 2.20 | 1563 |
| 2024-09-20 22:21:32.233 | MS1 | 121.4656767063 | 31.1446375176 | 823 | 504990 | -75.72 | 15.65 | 543.49 | 0.06 | 2.96 | 1579 |
| 2024-09-20 22:21:33.896 | MS1 | 121.4656605938 | 31.1446273752 | 823 | 504990 | -76.83 | 13.51 | 525.07 | 0.15 | 2.91 | 1592 |
| 2024-09-20 22:21:34.880 | MS1 | 121.4656657016 | 31.1446256055 | 823 | 504990 | -85.55 | -0.56 | 35.13 | 0.14 | 1.32 | 1572 |
| 2024-09-20 22:21:35.368 | MS1 | 121.4656672791 | 31.1446217052 | 823 | 504990 | -92.54 | -2.68 | 75.50 | 0.04 | 1.44 | 1594 |
| 2024-09-20 22:21:36.213 | MS1 | 121.4656744282 | 31.1446222249 | 823 | 504990 | -94.24 | -3.30 | 55.12 | 0.03 | 1.02 | 1573 |
| 2024-09-20 22:21:37.898 | MS1 | 121.4656739876 | 31.1446271842 | 823 | 504990 | -85.56 | -1.88 | 50.28 | 0.16 | 1.21 | 1581 |
| 2024-09-20 22:21:38.517 | MS1 | 121.4656763315 | 31.1446319437 | 823 | 504990 | -81.49 | 14.31 | 390.98 | 0.16 | 1.25 | 1582 |
| 2024-09-20 22:21:39.811 | MS1 | 121.4656644984 | 31.1446235563 | 823 | 504990 | -84.32 | 16.17 | 520.02 | 0.02 | 1.02 | 1576 |
| 2024-09-20 22:21:40.144 | MS1 | 121.4656606716 | 31.1446286686 | 823 | 504990 | -76.01 | 15.84 | 310.08 | 0.10 | 2.73 | 1562 |
| 2024-09-20 22:21:41.726 | MS1 | 121.4656775795 | 31.1446343288 | 823 | 504990 | -81.89 | 13.31 | 557.71 | 0.01 | 2.51 | 1575 |
| 2024-09-20 22:21:42.713 | MS1 | 121.4656659807 | 31.1446330659 | 823 | 504990 | -79.48 | 16.04 | 393.58 | 0.06 | 2.08 | 1593 |

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
| 3211917 | 1 | 121.4664918876 | 31.1548225503 | 177 | 5 | 9 | 15.4 | TDD | 803 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3243198 | 2 | 121.4744186254 | 31.1459422775 | 151 | 14 | 11 | 43.0 | TDD | 982 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3266998 | 3 | 121.4724028187 | 31.1547294156 | 177 | 9 | 4 | 32.1 | TDD | 158 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3278478 | 4 | 121.4688900400 | 31.1481674090 | 161 | 0 | 9 | 45.1 | TDD | 823 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.814 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.836 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.964 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.964 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.619 | NREventA3 | measId:2;ServCellPCI:300;Se... |
| 2024-09-20 22:21:35.619 | NREventA3 | measId:2;ServCellPCI:300;Se... |
| 2024-09-20 22:21:36.619 | NREventA3 | measId:2;ServCellPCI:300;Se... |
| 2024-09-20 22:21:39.119 | NRRRCReestablishAttempt | PCI:300 |
| 2024-09-20 22:21:39.135 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.145 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.280 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.280 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211917 | 1 | 18.4597 | 16.0777 | -114.0172 | 8.1512 | 114.9316 | 0.0129 | 0.0010 |
| 2024_09_20 22:00 | 3243198 | 2 | 10.0124 | 15.8810 | -114.1376 | 16.0861 | 102.4728 | 0.0119 | 0.0110 |
| 2024_09_20 22:00 | 3266998 | 3 | 6.5005 | 15.9322 | -117.0880 | 17.3364 | 111.0401 | 0.0012 | 0.0134 |
| 2024_09_20 22:00 | 3278478 | 4 | 9.6183 | 16.8464 | -115.6569 | 18.7128 | 85.5209 | 0.0129 | 0.1804 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415678_5029B4B8 | 504990 | 803 | -80.9 | 504990 | 823 | -85.3 | 504990 | 982 | -84.2 | 504990 | 158 |
| MR_1774415678_32F0D8D8 | 504990 | 823 | -87.3 | 504990 | 803 | -78.5 | 504990 | 982 | -85.5 | 504990 | 158 |
| MR_1774415678_C2232FF7 | 504990 | 823 | -87.3 | 504990 | 803 | -80.0 | 504990 | 982 | -82.0 | 504990 | 158 |
| MR_1774415678_3DF0359E | 504990 | 803 | -79.9 | 504990 | 823 | -84.9 | 504990 | 982 | -85.3 | 504990 | 158 |
| MR_1774415678_8A171D19 | 504990 | 803 | -78.3 | 504990 | 823 | -86.9 | 504990 | 982 | -82.3 | 504990 | 158 |
| MR_1774415678_F8D3D859 | 504990 | 803 | -79.3 | 504990 | 823 | -85.2 | 504990 | 982 | -84.4 | 504990 | 158 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1525: `0579b3e4-17b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0579b3e4-17b6-444b-b283-b6abdb7731b7` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232363_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1525] topology](images/train_1525.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3228919_8 and 3228383_3
- `C2`: Lift the tilt angle of 3232363_6 by 2 degrees
- `C3`: Press down the tilt angle of 3232363_6 by 2 degrees
- `C4`: Decrease A3 Offset threshold for 3228383_3
- `C5`: Decrease A3 Offset threshold for 3232363_6
- `C6`: Press down the tilt angle  of 3228383_3 by 4 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232363_6 **← 정답**
- `C8`: Increase A3 Offset threshold for 3228383_3
- `C9`: Lift the tilt angle  of 3228383_3 by 4 degrees
- `C10`: Increase transmission power for 3232363_6
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228383_3
- `C12`: Increase transmission power for 3228383_3
- `C13`: Adjust the azimuth of 3228383_3 by 38 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease transmission power for 3232363_6
- `C16`: Add neighbor relationship between 3232363_6 and 3228383_3
- `C17`: Increase A3 Offset threshold for 3232363_6
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228383_3
- `C19`: Adjust the azimuth of 3232363_6 by 1 degrees
- `C20`: Check test server and transmission issues
- `C21`: Decrease transmission power for 3228383_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232363_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.586 | MS1 | 121.4656622227 | 31.1446219907 | 987 | 504990 | -94.25 | 13.13 | 441.74 | 0.13 | 2.97 | 1574 |
| 2024-09-20 22:21:32.904 | MS1 | 121.4656724950 | 31.1446251475 | 131 | 504990 | -93.14 | 13.42 | 481.06 | 0.10 | 2.29 | 1586 |
| 2024-09-20 22:21:33.986 | MS1 | 121.4656629679 | 31.1446196811 | 246 | 504990 | -93.08 | 9.57 | 547.73 | 0.11 | 2.03 | 1582 |
| 2024-09-20 22:21:34.372 | MS1 | 121.4656629577 | 31.1446345844 | 142 | 152650 | -90.23 | 2.69 | 98.69 | 0.03 | 1.84 | 904 |
| 2024-09-20 22:21:35.632 | MS1 | 121.4656714497 | 31.1446366037 | 506 | 152650 | -96.80 | 4.09 | 54.24 | 0.17 | 1.76 | 968 |
| 2024-09-20 22:21:36.493 | MS1 | 121.4656605173 | 31.1446201982 | 422 | 152650 | -90.68 | 2.67 | 77.93 | 0.04 | 1.81 | 968 |
| 2024-09-20 22:21:37.379 | MS1 | 121.4656609002 | 31.1446377366 | 821 | 152650 | -95.98 | 2.22 | 65.80 | 0.20 | 1.66 | 952 |
| 2024-09-20 22:21:38.106 | MS1 | 121.4656739706 | 31.1446339520 | 142 | 152650 | -91.87 | 3.30 | 98.47 | 0.04 | 1.58 | 986 |
| 2024-09-20 22:21:39.676 | MS1 | 121.4656607101 | 31.1446288730 | 506 | 152650 | -89.82 | 5.48 | 91.56 | 0.20 | 1.58 | 947 |
| 2024-09-20 22:21:40.579 | MS1 | 121.4656669243 | 31.1446309315 | 422 | 152650 | -89.53 | 7.94 | 83.87 | 0.16 | 2.49 | 1566 |
| 2024-09-20 22:21:41.130 | MS1 | 121.4656722870 | 31.1446375916 | 821 | 152650 | -93.36 | 7.72 | 95.74 | 0.17 | 2.45 | 1562 |
| 2024-09-20 22:21:42.232 | MS1 | 121.4656593144 | 31.1446276724 | 142 | 152650 | -92.77 | 2.31 | 50.44 | 0.07 | 2.64 | 1573 |

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
| 3213760 | 5 | 121.4662599121 | 31.1486954720 | 256 | 2 | 5 | 26.9 | TDD | 920 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3228383 | 3 | 121.4682268863 | 31.1515707335 | 160 | 3 | 11 | 14.8 | TDD | 460 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3228919 | 8 | 121.4647203145 | 31.1460809202 | 86 | 9 | 5 | 10.4 | FDD | 422 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3232363 | 6 | 121.4724372640 | 31.1495741038 | 229 | 1 | 10 | 18.9 | TDD | 987 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3232446 | 7 | 121.4715691290 | 31.1512562214 | 289 | 9 | 1 | 9.5 | FDD | 609 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3235788 | 13 | 121.4688472096 | 31.1480159898 | 33 | 14 | 6 | 5.0 | FDD | 506 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3236241 | 10 | 121.4750362492 | 31.1495828432 | 91 | 13 | 12 | 2.0 | FDD | 142 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3243138 | 12 | 121.4742709750 | 31.1555294004 | 166 | 2 | 10 | 6.1 | FDD | 821 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3247149 | 9 | 121.4720679176 | 31.1549438295 | 277 | 0 | 3 | 16.4 | FDD | 939 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3257719 | 4 | 121.4743340709 | 31.1451893595 | 9 | 8 | 9 | 23.5 | TDD | 246 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3265862 | 1 | 121.4656543788 | 31.1533074970 | 25 | 0 | 10 | 7.0 | TDD | 131 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3268057 | 2 | 121.4725868100 | 31.1504676405 | 306 | 13 | 6 | 8.9 | TDD | 600 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3270780 | 11 | 121.4677751383 | 31.1478823470 | 52 | 1 | 4 | 1.0 | FDD | 819 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |

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
| 2024-09-20 22:21:31.278 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.299 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.400 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.400 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.174 | NREventA2 | measId:1;ServCellPCI:713;Se... |
| 2024-09-20 22:21:35.286 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.562 | NREventA5 | measId:3;ServCellPCI:713;Se... |
| 2024-09-20 22:21:35.617 | NRHandoverAttempt | SourcePCI:713;SourceNR-ARFC... |
| 2024-09-20 22:21:35.665 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.677 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.783 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.783 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265862 | 1 | 14.8611 | 18.8256 | -115.4324 | 14.0683 | 176.4713 | 0.0009 | 0.0196 |
| 2024_09_20 22:00 | 3268057 | 2 | 10.0241 | 13.7887 | -117.0652 | 16.0366 | 151.8944 | 0.0027 | 0.0097 |
| 2024_09_20 22:00 | 3228383 | 3 | 19.5904 | 8.3593 | -117.2022 | 9.6529 | 131.4297 | 0.0161 | 0.0149 |
| 2024_09_20 22:00 | 3257719 | 4 | 13.5956 | 10.0735 | -114.4586 | 17.7003 | 122.6399 | 0.0192 | 0.0051 |
| 2024_09_20 22:00 | 3213760 | 5 | 19.0941 | 5.3656 | -115.5318 | 14.9593 | 149.7441 | 0.0028 | 0.0024 |
| 2024_09_20 22:00 | 3232363 | 6 | 11.6216 | 10.0215 | -116.4203 | 18.0844 | 196.1331 | 0.0101 | 0.0181 |
| 2024_09_20 22:00 | 3232446 | 7 | 6.3909 | 8.2684 | -114.7116 | 4.4749 | 59.9149 | 0.0100 | 0.0121 |
| 2024_09_20 22:00 | 3228919 | 8 | 17.9178 | 12.6003 | -115.6624 | 4.7465 | 30.0896 | 0.0085 | 0.0108 |
| 2024_09_20 22:00 | 3247149 | 9 | 9.7467 | 7.4453 | -117.3120 | 4.4080 | 30.8538 | 0.0016 | 0.0027 |
| 2024_09_20 22:00 | 3236241 | 10 | 18.6137 | 8.4487 | -114.4948 | 3.8047 | 37.8460 | 0.0145 | 0.0076 |
| 2024_09_20 22:00 | 3270780 | 11 | 19.0238 | 10.7700 | -115.1062 | 3.4834 | 40.1923 | 0.0054 | 0.0041 |
| 2024_09_20 22:00 | 3243138 | 12 | 7.9708 | 10.1471 | -114.3135 | 4.6798 | 42.0533 | 0.0016 | 0.0096 |
| 2024_09_20 22:00 | 3235788 | 13 | 12.4850 | 13.7947 | -116.7549 | 4.2838 | 46.8993 | 0.0021 | 0.0017 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415199_E9199F01 | 152650 | 142 | -88.2 | 152650 | 609 | -96.4 | 152650 | 819 | -99.8 | 152650 | 939 |
| MR_1774415199_A1F463EE | 504990 | 246 | -91.3 | 504990 | 460 | -92.3 | 504990 | 920 | -96.1 | 504990 | 600 |
| MR_1774415199_54E13174 | 504990 | 246 | -93.0 | 504990 | 460 | -93.2 | 504990 | 920 | -97.9 | 504990 | 600 |
| MR_1774415199_3C51C11E | 152650 | 142 | -89.4 | 152650 | 609 | -95.6 | 152650 | 819 | -101.7 | 152650 | 939 |
| MR_1774415199_0B02BD11 | 152650 | 142 | -92.0 | 152650 | 609 | -94.5 | 152650 | 819 | -103.7 | 152650 | 939 |
| MR_1774415199_EC150C65 | 152650 | 142 | -91.1 | 152650 | 609 | -97.1 | 152650 | 819 | -100.2 | 152650 | 939 |
| MR_1774415199_4A0D4C44 | 504990 | 246 | -93.6 | 504990 | 460 | -93.5 | 504990 | 920 | -98.3 | 504990 | 600 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1526: `278c1825-875...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `278c1825-875f-461e-936d-a1b04d8e3151` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Lift the tilt angle  of 3241411_1 by 4 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1526] topology](images/train_1526.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3241411_1 and 3230547_2
- `C2`: Decrease A3 Offset threshold for 3230138_4
- `C3`: Adjust the azimuth of 3230138_4 by 48 degrees
- `C4`: Adjust the azimuth of 3241411_1 by 50 degrees
- `C5`: Add neighbor relationship between 3230138_4 and 3230547_2
- `C6`: Decrease A3 Offset threshold for 3230547_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230547_2
- `C9`: Lift the tilt angle of 3230138_4 by 5 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230138_4
- `C11`: Press down the tilt angle  of 3241411_1 by 4 degrees
- `C12`: Increase transmission power for 3230138_4
- `C13`: Press down the tilt angle of 3230138_4 by 5 degrees
- `C14`: Decrease transmission power for 3230547_2
- `C15`: Lift the tilt angle  of 3241411_1 by 4 degrees **← 정답**
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230138_4
- `C17`: Increase transmission power for 3230547_2
- `C18`: Increase A3 Offset threshold for 3230547_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230547_2
- `C20`: Increase A3 Offset threshold for 3230138_4
- `C21`: Decrease transmission power for 3230138_4
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.303 | MS1 | 121.4656597226 | 31.1446211961 | 703 | 504990 | -91.34 | 12.81 | 494.63 | 0.18 | 2.27 | 1592 |
| 2024-09-20 22:21:32.196 | MS1 | 121.4656773067 | 31.1446205828 | 703 | 504990 | -89.45 | 14.49 | 402.99 | 0.11 | 2.43 | 1589 |
| 2024-09-20 22:21:33.905 | MS1 | 121.4656585169 | 31.1446248240 | 703 | 504990 | -88.51 | 13.60 | 386.35 | 0.13 | 2.58 | 1596 |
| 2024-09-20 22:21:34.413 | MS1 | 121.4656612752 | 31.1446203631 | 703 | 504990 | -88.79 | 13.80 | 68.25 | 0.19 | 2.65 | 1581 |
| 2024-09-20 22:21:35.491 | MS1 | 121.4656754049 | 31.1446359434 | 703 | 504990 | -90.30 | 14.65 | 89.48 | 0.13 | 2.12 | 1560 |
| 2024-09-20 22:21:36.248 | MS1 | 121.4656668754 | 31.1446229287 | 703 | 504990 | -88.79 | 15.33 | 62.99 | 0.13 | 2.84 | 1572 |
| 2024-09-20 22:21:37.531 | MS1 | 121.4656671390 | 31.1446274118 | 703 | 504990 | -92.87 | 9.23 | 60.14 | 0.06 | 2.45 | 1565 |
| 2024-09-20 22:21:38.650 | MS1 | 121.4656584041 | 31.1446253208 | 703 | 504990 | -93.83 | 9.93 | 70.03 | 0.14 | 2.66 | 1562 |
| 2024-09-20 22:21:39.686 | MS1 | 121.4656649485 | 31.1446189182 | 703 | 504990 | -91.97 | 10.83 | 65.30 | 0.16 | 2.58 | 1569 |
| 2024-09-20 22:21:40.585 | MS1 | 121.4656666864 | 31.1446289415 | 703 | 504990 | -93.22 | 11.24 | 333.66 | 0.17 | 2.59 | 1600 |
| 2024-09-20 22:21:41.915 | MS1 | 121.4656751309 | 31.1446187182 | 703 | 504990 | -91.64 | 7.95 | 363.95 | 0.15 | 2.55 | 1563 |
| 2024-09-20 22:21:42.470 | MS1 | 121.4656587546 | 31.1446347567 | 703 | 504990 | -92.16 | 11.74 | 396.62 | 0.17 | 2.12 | 1567 |

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
| 3230138 | 4 | 121.4736480161 | 31.1503234032 | 182 | 4 | 8 | 22.7 | TDD | 703 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3230547 | 2 | 121.4755447228 | 31.1558187835 | 44 | 3 | 9 | 24.3 | TDD | 338 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3241411 | 1 | 121.4649917865 | 31.1478298049 | 327 | 5 | 10 | 24.4 | TDD | 673 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3260577 | 3 | 121.4663453756 | 31.1498163622 | 304 | 1 | 4 | 19.1 | TDD | 445 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.370 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.387 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.519 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.519 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.207 | NREventA3 | measId:2;ServCellPCI:310;Se... |
| 2024-09-20 22:21:38.447 | NRHandoverAttempt | SourcePCI:310;SourceNR-ARFC... |
| 2024-09-20 22:21:38.493 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.505 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.640 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.640 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241411 | 1 | 18.8755 | 16.1518 | -117.6343 | 18.6527 | 101.6163 | 0.0142 | 0.0149 |
| 2024_09_20 22:00 | 3230547 | 2 | 5.7361 | 15.7143 | -115.7707 | 8.9758 | 172.5022 | 0.0021 | 0.0054 |
| 2024_09_20 22:00 | 3260577 | 3 | 17.9394 | 10.7001 | -114.0161 | 17.2608 | 102.5326 | 0.0167 | 0.0094 |
| 2024_09_20 22:00 | 3230138 | 4 | 91.1779 | 92.2201 | -117.1933 | 11.1934 | 129.6158 | 0.0157 | 0.0169 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417110_DE7065D1 | 504990 | 703 | -89.7 | 504990 | 338 | -91.6 | 504990 | 673 | -102.9 | 504990 | 445 |
| MR_1774417110_AD839154 | 504990 | 703 | -87.0 | 504990 | 338 | -95.3 | 504990 | 673 | -100.1 | 504990 | 445 |
| MR_1774417110_9E4967B8 | 504990 | 703 | -88.0 | 504990 | 338 | -92.8 | 504990 | 673 | -101.1 | 504990 | 445 |
| MR_1774417110_F274187E | 504990 | 703 | -89.7 | 504990 | 338 | -94.9 | 504990 | 673 | -100.7 | 504990 | 445 |
| MR_1774417110_B519E03F | 504990 | 703 | -88.0 | 504990 | 338 | -93.0 | 504990 | 673 | -102.1 | 504990 | 445 |
| MR_1774417110_329E2919 | 504990 | 703 | -88.9 | 504990 | 338 | -95.4 | 504990 | 673 | -102.7 | 504990 | 445 |
| MR_1774417110_C8196B6E | 504990 | 703 | -89.8 | 504990 | 338 | -93.6 | 504990 | 673 | -101.5 | 504990 | 445 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1527: `1d08f74a-a9d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1d08f74a-a9d9-478d-95cf-03aa3e3fe7f8` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Lift the tilt angle  of 3214533_2 by 9 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1527] topology](images/train_1527.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3214533_2 by 9 degrees
- `C2`: Decrease A3 Offset threshold for 3277752_4
- `C3`: Increase transmission power for 3243706_1
- `C4`: Add neighbor relationship between 3243706_1 and 3277752_4
- `C5`: Increase A3 Offset threshold for 3277752_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Add neighbor relationship between 3214533_2 and 3277752_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243706_1
- `C9`: Decrease transmission power for 3277752_4
- `C10`: Lift the tilt angle  of 3214533_2 by 9 degrees **← 정답**
- `C11`: Decrease A3 Offset threshold for 3243706_1
- `C12`: Lift the tilt angle of 3243706_1 by 4 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243706_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277752_4
- `C15`: Increase transmission power for 3277752_4
- `C16`: Check test server and transmission issues
- `C17`: Adjust the azimuth of 3243706_1 by 9 degrees
- `C18`: Press down the tilt angle of 3243706_1 by 4 degrees
- `C19`: Decrease transmission power for 3243706_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277752_4
- `C21`: Increase A3 Offset threshold for 3243706_1
- `C22`: Adjust the azimuth of 3214533_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.896 | MS1 | 121.4656712634 | 31.1446330599 | 919 | 504990 | -85.37 | 13.60 | 581.06 | 0.16 | 2.39 | 1565 |
| 2024-09-20 22:21:32.830 | MS1 | 121.4656709715 | 31.1446234500 | 919 | 504990 | -91.94 | 13.72 | 356.05 | 0.08 | 2.25 | 1591 |
| 2024-09-20 22:21:33.825 | MS1 | 121.4656642477 | 31.1446306740 | 919 | 504990 | -85.01 | 16.90 | 402.52 | 0.05 | 2.30 | 1598 |
| 2024-09-20 22:21:34.322 | MS1 | 121.4656587521 | 31.1446184080 | 919 | 504990 | -90.55 | 13.83 | 62.87 | 0.14 | 2.73 | 1585 |
| 2024-09-20 22:21:35.318 | MS1 | 121.4656718427 | 31.1446342703 | 919 | 504990 | -90.78 | 13.99 | 57.21 | 0.02 | 2.55 | 1575 |
| 2024-09-20 22:21:36.255 | MS1 | 121.4656722627 | 31.1446202465 | 919 | 504990 | -87.00 | 16.07 | 48.22 | 0.10 | 2.44 | 1597 |
| 2024-09-20 22:21:37.690 | MS1 | 121.4656638155 | 31.1446377830 | 919 | 504990 | -92.38 | 12.72 | 83.44 | 0.09 | 2.87 | 1575 |
| 2024-09-20 22:21:38.451 | MS1 | 121.4656760872 | 31.1446316046 | 919 | 504990 | -90.21 | 10.90 | 61.20 | 0.09 | 2.20 | 1575 |
| 2024-09-20 22:21:39.631 | MS1 | 121.4656778293 | 31.1446278893 | 919 | 504990 | -92.71 | 7.08 | 58.53 | 0.06 | 2.02 | 1576 |
| 2024-09-20 22:21:40.984 | MS1 | 121.4656718153 | 31.1446329466 | 919 | 504990 | -89.98 | 10.41 | 527.19 | 0.04 | 2.86 | 1590 |
| 2024-09-20 22:21:41.612 | MS1 | 121.4656603554 | 31.1446229689 | 919 | 504990 | -90.58 | 12.84 | 484.33 | 0.06 | 2.09 | 1571 |
| 2024-09-20 22:21:42.375 | MS1 | 121.4656754893 | 31.1446247118 | 919 | 504990 | -91.89 | 11.49 | 408.67 | 0.17 | 2.79 | 1597 |

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
| 3214533 | 2 | 121.4640628469 | 31.1514293695 | 112 | 15 | 4 | 35.5 | TDD | 185 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3229732 | 3 | 121.4650830131 | 31.1444665255 | 100 | 15 | 6 | 44.0 | TDD | 84 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3243706 | 1 | 121.4751117434 | 31.1541573351 | 229 | 3 | 10 | 19.8 | TDD | 919 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3277752 | 4 | 121.4684177363 | 31.1546765097 | 307 | 7 | 5 | 38.3 | TDD | 575 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.948 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.972 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.114 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.114 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.825 | NREventA3 | measId:2;ServCellPCI:632;Se... |
| 2024-09-20 22:21:38.065 | NRHandoverAttempt | SourcePCI:632;SourceNR-ARFC... |
| 2024-09-20 22:21:38.096 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.110 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.253 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.253 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243706 | 1 | 76.2661 | 93.2679 | -114.0854 | 5.4881 | 123.4269 | 0.0070 | 0.0134 |
| 2024_09_20 22:00 | 3214533 | 2 | 19.6335 | 8.6459 | -116.6663 | 14.6816 | 177.5287 | 0.0071 | 0.0177 |
| 2024_09_20 22:00 | 3229732 | 3 | 12.1332 | 5.4361 | -114.5805 | 9.0357 | 114.2783 | 0.0141 | 0.0166 |
| 2024_09_20 22:00 | 3277752 | 4 | 8.7120 | 10.5480 | -117.3196 | 12.8983 | 92.9712 | 0.0011 | 0.0200 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412782_EDEBF327 | 504990 | 919 | -90.6 | 504990 | 575 | -92.5 | 504990 | 185 | -101.9 | 504990 | 84 |
| MR_1774412782_3D7824BD | 504990 | 919 | -89.9 | 504990 | 575 | -95.1 | 504990 | 185 | -101.2 | 504990 | 84 |
| MR_1774412782_B2BFC438 | 504990 | 919 | -91.0 | 504990 | 575 | -94.5 | 504990 | 185 | -103.5 | 504990 | 84 |
| MR_1774412782_EFA42137 | 504990 | 919 | -89.6 | 504990 | 575 | -93.7 | 504990 | 185 | -104.6 | 504990 | 84 |
| MR_1774412782_00D42AAB | 504990 | 919 | -90.2 | 504990 | 575 | -92.0 | 504990 | 185 | -102.2 | 504990 | 84 |
| MR_1774412782_46C8D914 | 504990 | 919 | -89.8 | 504990 | 575 | -94.5 | 504990 | 185 | -101.8 | 504990 | 84 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1528: `48a07e15-6bf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `48a07e15-6bf2-480b-af87-ae03903830c9` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1528] topology](images/train_1528.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3217108_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225789_3
- `C3`: Lift the tilt angle  of 3217108_1 by 10 degrees
- `C4`: Increase transmission power for 3225789_3
- `C5`: Increase A3 Offset threshold for 3225789_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217108_1
- `C7`: Lift the tilt angle of 3225789_3 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3225789_3
- `C9`: Press down the tilt angle  of 3217108_1 by 10 degrees
- `C10`: Press down the tilt angle of 3225789_3 by 10 degrees
- `C11`: Adjust the azimuth of 3225789_3 by 11 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225789_3
- `C13`: Check test server and transmission issues
- `C14`: Adjust the azimuth of 3217108_1 by 31 degrees
- `C15`: Add neighbor relationship between 3225789_3 and 3217108_1
- `C16`: Decrease transmission power for 3225789_3
- `C17`: Add neighbor relationship between 3273046_2 and 3217108_1
- `C18`: Decrease A3 Offset threshold for 3217108_1
- `C19`: Insufficient data; more data is needed for judgment. **← 정답**
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217108_1
- `C21`: Increase A3 Offset threshold for 3217108_1
- `C22`: Decrease transmission power for 3217108_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.739 | MS1 | 121.4656741760 | 31.1446251562 | 988 | 504990 | -87.76 | 12.31 | 572.38 | 0.10 | 2.35 | 1597 |
| 2024-09-20 22:21:32.977 | MS1 | 121.4656605090 | 31.1446358477 | 988 | 504990 | -91.11 | 12.28 | 539.00 | 0.17 | 2.27 | 1599 |
| 2024-09-20 22:21:33.181 | MS1 | 121.4656770297 | 31.1446270308 | 988 | 504990 | -89.02 | 12.07 | 476.02 | 0.17 | 2.28 | 1582 |
| 2024-09-20 22:21:34.912 | MS1 | 121.4656633688 | 31.1446300321 | 988 | 504990 | -87.65 | 12.74 | 50.70 | 0.09 | 2.58 | 1591 |
| 2024-09-20 22:21:35.896 | MS1 | 121.4656626140 | 31.1446180216 | 988 | 504990 | -89.05 | 14.91 | 61.23 | 0.05 | 2.01 | 1566 |
| 2024-09-20 22:21:36.285 | MS1 | 121.4656603044 | 31.1446210383 | 988 | 504990 | -90.66 | 17.27 | 71.55 | 0.00 | 2.78 | 1584 |
| 2024-09-20 22:21:37.480 | MS1 | 121.4656680264 | 31.1446275434 | 988 | 504990 | -89.87 | 8.13 | 71.58 | 0.05 | 2.85 | 1579 |
| 2024-09-20 22:21:38.564 | MS1 | 121.4656623724 | 31.1446224932 | 988 | 504990 | -93.18 | 7.19 | 101.69 | 0.06 | 2.44 | 1594 |
| 2024-09-20 22:21:39.489 | MS1 | 121.4656664841 | 31.1446320728 | 988 | 504990 | -89.49 | 8.76 | 53.75 | 0.18 | 2.22 | 1595 |
| 2024-09-20 22:21:40.468 | MS1 | 121.4656604479 | 31.1446276109 | 988 | 504990 | -91.98 | 9.32 | 570.75 | 0.16 | 2.78 | 1573 |
| 2024-09-20 22:21:41.989 | MS1 | 121.4656755792 | 31.1446198169 | 988 | 504990 | -90.03 | 12.69 | 580.18 | 0.05 | 2.63 | 1576 |
| 2024-09-20 22:21:42.960 | MS1 | 121.4656759707 | 31.1446318403 | 988 | 504990 | -93.12 | 10.74 | 330.45 | 0.01 | 2.35 | 1586 |

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
| 3217108 | 1 | 121.4717189005 | 31.1464070730 | 220 | 11 | 10 | 24.4 | TDD | 281 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3225789 | 3 | 121.4740846265 | 31.1497788693 | 223 | 9 | 2 | 47.0 | TDD | 988 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3271384 | 4 | 121.4704769422 | 31.1479948176 | 142 | 10 | 0 | 24.8 | TDD | 1007 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3273046 | 2 | 121.4716213762 | 31.1464706969 | 28 | 2 | 8 | 44.3 | TDD | 754 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.107 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.107 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.794 | NREventA3 | measId:2;ServCellPCI:999;Se... |
| 2024-09-20 22:21:38.034 | NRHandoverAttempt | SourcePCI:999;SourceNR-ARFC... |
| 2024-09-20 22:21:38.070 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.083 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.216 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.216 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3217108 | 1 | 93.3745 | 93.2669 | -115.4808 | 5.4668 | 171.0054 | 0.0181 | 0.0185 |
| 2024_09_19 22:00 | 3273046 | 2 | 82.5307 | 77.8980 | -115.1460 | 17.8228 | 173.4596 | 0.0134 | 0.0011 |
| 2024_09_19 22:00 | 3225789 | 3 | 79.9340 | 91.4660 | -114.1300 | 10.8200 | 161.8241 | 0.0068 | 0.0172 |
| 2024_09_19 22:00 | 3271384 | 4 | 87.4342 | 90.0870 | -114.9768 | 14.7785 | 95.0585 | 0.0115 | 0.0118 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412333_0B5FB8B2 | 504990 | 988 | -86.2 | 504990 | 281 | -88.4 | 504990 | 754 | -98.1 | 504990 | 1007 |
| MR_1774412333_4878BB07 | 504990 | 988 | -85.8 | 504990 | 281 | -86.7 | 504990 | 754 | -97.4 | 504990 | 1007 |
| MR_1774412333_03F7E18F | 504990 | 988 | -88.8 | 504990 | 281 | -89.8 | 504990 | 754 | -97.6 | 504990 | 1007 |
| MR_1774412333_E4A3646F | 504990 | 988 | -85.8 | 504990 | 281 | -87.3 | 504990 | 754 | -95.7 | 504990 | 1007 |
| MR_1774412333_74414372 | 504990 | 988 | -88.7 | 504990 | 281 | -87.4 | 504990 | 754 | -94.6 | 504990 | 1007 |
| MR_1774412333_2C0EC804 | 504990 | 988 | -89.1 | 504990 | 281 | -87.4 | 504990 | 754 | -94.7 | 504990 | 1007 |
| MR_1774412333_03E56CC8 | 504990 | 988 | -88.9 | 504990 | 281 | -89.3 | 504990 | 754 | -95.8 | 504990 | 1007 |
| MR_1774412333_50695422 | 504990 | 988 | -85.9 | 504990 | 281 | -89.7 | 504990 | 754 | -94.3 | 504990 | 1007 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1529: `2f96744c-629...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2f96744c-6296-42f5-bcc6-5010a9247f7e` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Lift the tilt angle  of 3226204_1 by 5 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1529] topology](images/train_1529.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3218726_3 by 6 degrees
- `C2`: Increase transmission power for 3258755_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218726_3
- `C4`: Lift the tilt angle  of 3226204_1 by 5 degrees **← 정답**
- `C5`: Decrease transmission power for 3258755_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218726_3
- `C7`: Lift the tilt angle of 3218726_3 by 6 degrees
- `C8`: Decrease A3 Offset threshold for 3218726_3
- `C9`: Add neighbor relationship between 3226204_1 and 3258755_2
- `C10`: Increase A3 Offset threshold for 3218726_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258755_2
- `C12`: Check test server and transmission issues
- `C13`: Adjust the azimuth of 3218726_3 by 49 degrees
- `C14`: Increase A3 Offset threshold for 3258755_2
- `C15`: Press down the tilt angle  of 3226204_1 by 5 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase transmission power for 3218726_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258755_2
- `C19`: Decrease transmission power for 3218726_3
- `C20`: Add neighbor relationship between 3218726_3 and 3258755_2
- `C21`: Adjust the azimuth of 3226204_1 by 50 degrees
- `C22`: Decrease A3 Offset threshold for 3258755_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.150 | MS1 | 121.4656770398 | 31.1446269091 | 349 | 504990 | -88.70 | 12.83 | 513.76 | 0.06 | 2.86 | 1599 |
| 2024-09-20 22:21:32.395 | MS1 | 121.4656676703 | 31.1446267185 | 349 | 504990 | -91.66 | 14.74 | 484.56 | 0.03 | 2.60 | 1584 |
| 2024-09-20 22:21:33.710 | MS1 | 121.4656772759 | 31.1446253923 | 349 | 504990 | -89.84 | 13.21 | 296.81 | 0.08 | 2.77 | 1596 |
| 2024-09-20 22:21:34.117 | MS1 | 121.4656712957 | 31.1446192447 | 349 | 504990 | -85.73 | 17.03 | 85.18 | 0.17 | 2.27 | 1579 |
| 2024-09-20 22:21:35.549 | MS1 | 121.4656630020 | 31.1446259370 | 349 | 504990 | -85.51 | 15.05 | 71.31 | 0.08 | 2.40 | 1582 |
| 2024-09-20 22:21:36.879 | MS1 | 121.4656710184 | 31.1446263540 | 349 | 504990 | -91.68 | 12.17 | 74.00 | 0.19 | 2.97 | 1592 |
| 2024-09-20 22:21:37.115 | MS1 | 121.4656656901 | 31.1446370860 | 349 | 504990 | -93.13 | 10.63 | 63.43 | 0.15 | 2.01 | 1590 |
| 2024-09-20 22:21:38.563 | MS1 | 121.4656588305 | 31.1446352389 | 349 | 504990 | -90.31 | 8.51 | 52.46 | 0.07 | 2.62 | 1580 |
| 2024-09-20 22:21:39.126 | MS1 | 121.4656761724 | 31.1446278564 | 349 | 504990 | -89.08 | 10.33 | 87.43 | 0.14 | 2.37 | 1587 |
| 2024-09-20 22:21:40.279 | MS1 | 121.4656605974 | 31.1446359832 | 349 | 504990 | -89.61 | 12.22 | 562.98 | 0.09 | 2.70 | 1566 |
| 2024-09-20 22:21:41.835 | MS1 | 121.4656615489 | 31.1446273590 | 349 | 504990 | -89.62 | 12.34 | 313.20 | 0.17 | 2.94 | 1572 |
| 2024-09-20 22:21:42.373 | MS1 | 121.4656691544 | 31.1446187581 | 349 | 504990 | -93.34 | 10.39 | 510.62 | 0.19 | 2.13 | 1570 |

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
| 3218726 | 3 | 121.4729571129 | 31.1447104883 | 220 | 2 | 3 | 46.8 | TDD | 349 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3226204 | 1 | 121.4747503445 | 31.1476085939 | 32 | 14 | 1 | 48.7 | TDD | 346 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3246793 | 4 | 121.4715430840 | 31.1464249051 | 227 | 14 | 0 | 48.0 | TDD | 366 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3258755 | 2 | 121.4709719041 | 31.1479093445 | 139 | 3 | 2 | 16.4 | TDD | 950 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.925 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.947 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.082 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.082 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.737 | NREventA3 | measId:2;ServCellPCI:301;Se... |
| 2024-09-20 22:21:37.977 | NRHandoverAttempt | SourcePCI:301;SourceNR-ARFC... |
| 2024-09-20 22:21:38.024 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.034 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.172 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.172 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226204 | 1 | 8.6954 | 14.7100 | -114.4697 | 14.3581 | 174.5255 | 0.0030 | 0.0159 |
| 2024_09_20 22:00 | 3258755 | 2 | 11.5279 | 16.8029 | -117.6418 | 13.8006 | 98.3538 | 0.0069 | 0.0069 |
| 2024_09_20 22:00 | 3218726 | 3 | 90.5174 | 83.7928 | -115.5613 | 9.1804 | 158.4648 | 0.0162 | 0.0057 |
| 2024_09_20 22:00 | 3246793 | 4 | 11.0060 | 11.5239 | -117.5458 | 14.8837 | 91.7841 | 0.0163 | 0.0147 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416218_27BDEC97 | 504990 | 349 | -86.2 | 504990 | 950 | -91.0 | 504990 | 346 | -92.0 | 504990 | 366 |
| MR_1774416218_67587690 | 504990 | 349 | -87.7 | 504990 | 950 | -87.3 | 504990 | 346 | -91.9 | 504990 | 366 |
| MR_1774416218_446D879A | 504990 | 349 | -84.3 | 504990 | 950 | -89.5 | 504990 | 346 | -92.9 | 504990 | 366 |
| MR_1774416218_0D181767 | 504990 | 349 | -86.3 | 504990 | 950 | -89.0 | 504990 | 346 | -92.4 | 504990 | 366 |
| MR_1774416218_9C3F2E99 | 504990 | 349 | -84.2 | 504990 | 950 | -88.9 | 504990 | 346 | -91.8 | 504990 | 366 |
| MR_1774416218_59E8F6FC | 504990 | 349 | -87.6 | 504990 | 950 | -87.6 | 504990 | 346 | -94.3 | 504990 | 366 |
| MR_1774416218_974F7A37 | 504990 | 349 | -84.2 | 504990 | 950 | -87.6 | 504990 | 346 | -91.0 | 504990 | 366 |

> *... 2개 열 생략 (전체 14열)*

---
