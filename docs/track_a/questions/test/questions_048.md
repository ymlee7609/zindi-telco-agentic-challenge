# Track A 문제 분석 — test[470]~test[479]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[470] ~ test[479] (10개)

## 목차

1. [문제 470: `c315a094-589...`](#470) — single-answer
2. [문제 471: `1af6a259-71b...`](#471) — multiple-answer
3. [문제 472: `411f9e52-9f4...`](#472) — single-answer
4. [문제 473: `efd34331-bd2...`](#473) — single-answer
5. [문제 474: `2b0b5c18-06c...`](#474) — single-answer
6. [문제 475: `85114ee1-3ac...`](#475) — single-answer
7. [문제 476: `9224ad4a-0eb...`](#476) — multiple-answer
8. [문제 477: `81e4c4d8-23e...`](#477) — single-answer
9. [문제 478: `86b8d1cc-5b7...`](#478) — single-answer
10. [문제 479: `17c4c305-458...`](#479) — single-answer

---

### 문제 470: `c315a094-589...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c315a094-589c-44a7-8f5f-e7f99ec63aff` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[470] topology](images/test_0470.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213942_3
- `C2`: Adjust the azimuth of 3263042_4 by 0 degrees
- `C3`: Add neighbor relationship between 3235999_1 and 3213942_3
- `C4`: Decrease A3 Offset threshold for 3263042_4
- `C5`: Lift the tilt angle of 3263042_4 by 5 degrees
- `C6`: Add neighbor relationship between 3263042_4 and 3213942_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263042_4
- `C8`: Check test server and transmission issues
- `C9`: Press down the tilt angle of 3263042_4 by 5 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase transmission power for 3263042_4
- `C12`: Press down the tilt angle  of 3235999_1 by 8 degrees
- `C13`: Decrease transmission power for 3213942_3
- `C14`: Lift the tilt angle  of 3235999_1 by 8 degrees
- `C15`: Decrease transmission power for 3263042_4
- `C16`: Increase transmission power for 3213942_3
- `C17`: Adjust the azimuth of 3235999_1 by 50 degrees
- `C18`: Increase A3 Offset threshold for 3263042_4
- `C19`: Increase A3 Offset threshold for 3213942_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263042_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213942_3
- `C22`: Decrease A3 Offset threshold for 3213942_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.714 | MS1 | 121.4656774206 | 31.1446324772 | 887 | 504990 | -86.45 | 12.86 | 476.67 | 0.09 | 2.74 | 1595 |
| 2024-09-20 22:21:32.798 | MS1 | 121.4656600168 | 31.1446303563 | 887 | 504990 | -91.83 | 16.02 | 512.00 | 0.17 | 2.84 | 1584 |
| 2024-09-20 22:21:33.195 | MS1 | 121.4656689949 | 31.1446217922 | 887 | 504990 | -86.80 | 13.53 | 570.05 | 0.12 | 2.29 | 1573 |
| 2024-09-20 22:21:34.450 | MS1 | 121.4656743399 | 31.1446215392 | 887 | 504990 | -90.78 | 12.71 | 68.83 | 0.15 | 2.94 | 1560 |
| 2024-09-20 22:21:35.545 | MS1 | 121.4656585161 | 31.1446250942 | 887 | 504990 | -89.05 | 16.78 | 97.94 | 0.19 | 2.33 | 1586 |
| 2024-09-20 22:21:36.883 | MS1 | 121.4656647586 | 31.1446345010 | 887 | 504990 | -87.35 | 15.42 | 97.48 | 0.04 | 2.84 | 1571 |
| 2024-09-20 22:21:37.551 | MS1 | 121.4656712649 | 31.1446347768 | 887 | 504990 | -89.55 | 7.45 | 102.72 | 0.03 | 2.91 | 1597 |
| 2024-09-20 22:21:38.646 | MS1 | 121.4656754759 | 31.1446217133 | 887 | 504990 | -91.56 | 10.97 | 61.39 | 0.01 | 2.64 | 1561 |
| 2024-09-20 22:21:39.422 | MS1 | 121.4656743902 | 31.1446187937 | 887 | 504990 | -90.49 | 8.30 | 78.70 | 0.09 | 2.05 | 1600 |
| 2024-09-20 22:21:40.724 | MS1 | 121.4656738523 | 31.1446352699 | 887 | 504990 | -92.83 | 10.07 | 516.36 | 0.05 | 2.88 | 1577 |
| 2024-09-20 22:21:41.902 | MS1 | 121.4656629416 | 31.1446231820 | 887 | 504990 | -89.63 | 11.50 | 511.92 | 0.06 | 2.49 | 1585 |
| 2024-09-20 22:21:42.235 | MS1 | 121.4656678684 | 31.1446327805 | 887 | 504990 | -89.23 | 11.25 | 436.23 | 0.09 | 2.75 | 1560 |

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
| 3213942 | 3 | 121.4746964485 | 31.1526940124 | 327 | 7 | 11 | 26.7 | TDD | 318 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3226020 | 2 | 121.4645361388 | 31.1492463940 | 357 | 7 | 3 | 38.6 | TDD | 189 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3235999 | 1 | 121.4694519933 | 31.1467434609 | 37 | 1 | 0 | 43.0 | TDD | 8 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3263042 | 4 | 121.4719278031 | 31.1473181022 | 243 | 1 | 3 | 47.3 | TDD | 887 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.416 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.436 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.557 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.557 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.302 | NREventA3 | measId:2;ServCellPCI:551;Se... |
| 2024-09-20 22:21:38.542 | NRHandoverAttempt | SourcePCI:551;SourceNR-ARFC... |
| 2024-09-20 22:21:38.581 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.595 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.701 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.701 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235999 | 1 | 8.7049 | 11.4210 | -117.9984 | 5.1215 | 133.2517 | 0.0117 | 0.0181 |
| 2024_09_20 22:00 | 3226020 | 2 | 11.9182 | 6.3746 | -117.7937 | 6.0539 | 164.5047 | 0.0008 | 0.0006 |
| 2024_09_20 22:00 | 3213942 | 3 | 7.3633 | 16.1172 | -115.9085 | 16.5496 | 197.5339 | 0.0116 | 0.0121 |
| 2024_09_20 22:00 | 3263042 | 4 | 78.0417 | 90.3298 | -114.5119 | 12.9514 | 194.1652 | 0.0002 | 0.0104 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413899_C018B282 | 504990 | 887 | -89.8 | 504990 | 318 | -92.1 | 504990 | 8 | -98.6 | 504990 | 189 |
| MR_1774413899_00590E3A | 504990 | 887 | -89.0 | 504990 | 318 | -92.9 | 504990 | 8 | -101.2 | 504990 | 189 |
| MR_1774413899_61B7D9E3 | 504990 | 887 | -91.3 | 504990 | 318 | -92.6 | 504990 | 8 | -100.9 | 504990 | 189 |
| MR_1774413899_81338C29 | 504990 | 887 | -89.9 | 504990 | 318 | -95.6 | 504990 | 8 | -100.9 | 504990 | 189 |
| MR_1774413899_F18F3754 | 504990 | 887 | -90.6 | 504990 | 318 | -93.9 | 504990 | 8 | -99.7 | 504990 | 189 |
| MR_1774413899_9EDD3CFD | 504990 | 887 | -90.9 | 504990 | 318 | -95.5 | 504990 | 8 | -100.7 | 504990 | 189 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 471: `1af6a259-71b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1af6a259-71b8-4058-8cfd-26e89184d672` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[471] topology](images/test_0471.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267137_3
- `C2`: Lift the tilt angle  of 3267137_3 by 3 degrees
- `C3`: Increase A3 Offset threshold for 3211588_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211588_2
- `C5`: Increase transmission power for 3267137_3
- `C6`: Decrease transmission power for 3267137_3
- `C7`: Lift the tilt angle of 3211588_2 by 10 degrees
- `C8`: Add neighbor relationship between 3211588_2 and 3267137_3
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211588_2
- `C11`: Adjust the azimuth of 3211588_2 by 50 degrees
- `C12`: Adjust the azimuth of 3267137_3 by 43 degrees
- `C13`: Press down the tilt angle  of 3267137_3 by 3 degrees
- `C14`: Decrease A3 Offset threshold for 3211588_2
- `C15`: Add neighbor relationship between 3212847_4 and 3267137_3
- `C16`: Increase transmission power for 3211588_2
- `C17`: Increase A3 Offset threshold for 3267137_3
- `C18`: Decrease transmission power for 3211588_2
- `C19`: Press down the tilt angle of 3211588_2 by 10 degrees
- `C20`: Check test server and transmission issues
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267137_3
- `C22`: Decrease A3 Offset threshold for 3267137_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.947 | MS1 | 121.4656639752 | 31.1446195697 | 732 | 504990 | -86.68 | 14.23 | 384.66 | 0.06 | 2.45 | 1579 |
| 2024-09-20 22:21:32.567 | MS1 | 121.4656641986 | 31.1446361636 | 732 | 504990 | -92.57 | 12.79 | 520.82 | 0.06 | 2.76 | 1600 |
| 2024-09-20 22:21:33.519 | MS1 | 121.4656715265 | 31.1446187795 | 732 | 504990 | -90.33 | 14.62 | 374.74 | 0.16 | 2.40 | 1594 |
| 2024-09-20 22:21:34.520 | MS1 | 121.4656778756 | 31.1446186166 | 732 | 504990 | -105.06 | -1.29 | 51.50 | 0.05 | 1.14 | 1589 |
| 2024-09-20 22:21:35.882 | MS1 | 121.4656663782 | 31.1446203777 | 732 | 504990 | -109.27 | 0.56 | 66.52 | 0.03 | 1.44 | 1598 |
| 2024-09-20 22:21:36.767 | MS1 | 121.4656691329 | 31.1446372682 | 732 | 504990 | -109.22 | -1.85 | 18.37 | 0.16 | 1.23 | 1560 |
| 2024-09-20 22:21:37.381 | MS1 | 121.4656747881 | 31.1446363417 | 732 | 504990 | -105.65 | 0.95 | 61.45 | 0.06 | 1.16 | 1571 |
| 2024-09-20 22:21:38.903 | MS1 | 121.4656612207 | 31.1446285723 | 732 | 504990 | -107.53 | -0.00 | 55.16 | 0.11 | 1.50 | 1568 |
| 2024-09-20 22:21:39.137 | MS1 | 121.4656698765 | 31.1446371338 | 732 | 504990 | -102.50 | 0.60 | 58.45 | 0.04 | 1.45 | 1600 |
| 2024-09-20 22:21:40.592 | MS1 | 121.4656679367 | 31.1446279347 | 732 | 504990 | -89.37 | 14.10 | 398.56 | 0.11 | 2.77 | 1598 |
| 2024-09-20 22:21:41.173 | MS1 | 121.4656583048 | 31.1446304785 | 732 | 504990 | -91.47 | 17.38 | 368.17 | 0.12 | 2.02 | 1596 |
| 2024-09-20 22:21:42.977 | MS1 | 121.4656658486 | 31.1446214467 | 732 | 504990 | -85.81 | 14.33 | 426.64 | 0.07 | 2.82 | 1589 |

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
| 3211588 | 2 | 121.4736135393 | 31.1503589466 | 156 | 13 | 10 | 47.5 | TDD | 732 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3212847 | 4 | 121.4663979271 | 31.1443504146 | 292 | 12 | 8 | 38.8 | TDD | 671 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3249834 | 1 | 121.4684387942 | 31.1541192243 | 251 | 7 | 4 | 28.5 | TDD | 763 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3267137 | 3 | 121.4742043362 | 31.1454508897 | 307 | 0 | 8 | 49.3 | TDD | 86 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.852 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.870 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.005 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.005 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.153 | NREventA2 | measId:1;ServCellPCI:53;Ser... |
| 2024-09-20 22:21:34.288 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249834 | 1 | 17.6193 | 8.4974 | -115.4258 | 10.6074 | 136.2259 | 0.0112 | 0.0044 |
| 2024_09_20 22:00 | 3211588 | 2 | 18.6729 | 19.9592 | -117.7988 | 11.7729 | 126.2134 | 0.1067 | 0.0091 |
| 2024_09_20 22:00 | 3267137 | 3 | 6.5437 | 8.6584 | -116.3238 | 10.8205 | 115.7855 | 0.0093 | 0.0097 |
| 2024_09_20 22:00 | 3212847 | 4 | 10.5243 | 10.5389 | -116.8941 | 13.6969 | 139.3487 | 0.0156 | 0.0016 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416235_36CE0452 | 504990 | 732 | -104.0 | 504990 | 86 | -109.3 | 504990 | 671 | -116.8 | 504990 | 763 |
| MR_1774416235_158CEB38 | 504990 | 732 | -103.3 | 504990 | 86 | -109.4 | 504990 | 671 | -116.6 | 504990 | 763 |
| MR_1774416235_7757966D | 504990 | 732 | -103.1 | 504990 | 86 | -110.0 | 504990 | 671 | -117.2 | 504990 | 763 |
| MR_1774416235_A317D47A | 504990 | 732 | -103.5 | 504990 | 86 | -107.6 | 504990 | 671 | -116.6 | 504990 | 763 |
| MR_1774416235_609BE9C8 | 504990 | 732 | -106.8 | 504990 | 86 | -108.5 | 504990 | 671 | -116.2 | 504990 | 763 |
| MR_1774416235_5408DD66 | 504990 | 732 | -105.8 | 504990 | 86 | -108.7 | 504990 | 671 | -117.3 | 504990 | 763 |
| MR_1774416235_36089D76 | 504990 | 732 | -104.1 | 504990 | 86 | -107.5 | 504990 | 671 | -118.0 | 504990 | 763 |
| MR_1774416235_0878AE7A | 504990 | 732 | -105.1 | 504990 | 86 | -111.1 | 504990 | 671 | -117.2 | 504990 | 763 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 472: `411f9e52-9f4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `411f9e52-9f4f-4952-9eb1-5b9e1841e7f6` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[472] topology](images/test_0472.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3230454_1 by 10 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230454_1
- `C3`: Add neighbor relationship between 3272656_2 and 3230454_1
- `C4`: Add neighbor relationship between 3249422_3 and 3230454_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272656_2
- `C6`: Decrease A3 Offset threshold for 3272656_2
- `C7`: Press down the tilt angle of 3272656_2 by 10 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272656_2
- `C9`: Increase A3 Offset threshold for 3230454_1
- `C10`: Decrease A3 Offset threshold for 3230454_1
- `C11`: Adjust the azimuth of 3272656_2 by 50 degrees
- `C12`: Increase transmission power for 3230454_1
- `C13`: Decrease transmission power for 3230454_1
- `C14`: Check test server and transmission issues
- `C15`: Decrease transmission power for 3272656_2
- `C16`: Lift the tilt angle of 3272656_2 by 10 degrees
- `C17`: Lift the tilt angle  of 3230454_1 by 10 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230454_1
- `C19`: Increase A3 Offset threshold for 3272656_2
- `C20`: Increase transmission power for 3272656_2
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Adjust the azimuth of 3230454_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.855 | MS1 | 121.4656697394 | 31.1446256775 | 249 | 504990 | -77.01 | 14.97 | 487.71 | 0.02 | 2.94 | 1564 |
| 2024-09-20 22:21:32.632 | MS1 | 121.4656650819 | 31.1446344687 | 249 | 504990 | -80.19 | 14.63 | 414.00 | 0.09 | 2.43 | 1578 |
| 2024-09-20 22:21:33.323 | MS1 | 121.4656595525 | 31.1446347833 | 249 | 504990 | -81.65 | 14.47 | 321.10 | 0.05 | 2.35 | 1589 |
| 2024-09-20 22:21:34.427 | MS1 | 121.4656759992 | 31.1446342212 | 249 | 504990 | -87.87 | -0.86 | 48.82 | 0.05 | 1.43 | 1590 |
| 2024-09-20 22:21:35.719 | MS1 | 121.4656770534 | 31.1446371637 | 249 | 504990 | -87.65 | -2.40 | 64.55 | 0.02 | 1.32 | 1588 |
| 2024-09-20 22:21:36.882 | MS1 | 121.4656648117 | 31.1446339966 | 249 | 504990 | -91.06 | -1.14 | 61.11 | 0.20 | 1.31 | 1584 |
| 2024-09-20 22:21:37.782 | MS1 | 121.4656599638 | 31.1446347248 | 249 | 504990 | -88.32 | -3.68 | 70.15 | 0.18 | 1.23 | 1571 |
| 2024-09-20 22:21:38.660 | MS1 | 121.4656724409 | 31.1446262507 | 249 | 504990 | -83.85 | -1.62 | 50.34 | 0.11 | 1.41 | 1600 |
| 2024-09-20 22:21:39.200 | MS1 | 121.4656622326 | 31.1446251446 | 352 | 504990 | -82.26 | 14.68 | 238.84 | 0.02 | 1.38 | 1588 |
| 2024-09-20 22:21:40.428 | MS1 | 121.4656625205 | 31.1446319047 | 352 | 504990 | -79.64 | 14.08 | 541.27 | 0.04 | 2.45 | 1563 |
| 2024-09-20 22:21:41.692 | MS1 | 121.4656769957 | 31.1446331743 | 352 | 504990 | -77.31 | 12.01 | 309.86 | 0.17 | 2.57 | 1576 |
| 2024-09-20 22:21:42.834 | MS1 | 121.4656731531 | 31.1446328807 | 352 | 504990 | -75.94 | 17.38 | 350.67 | 0.06 | 2.82 | 1577 |

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
| 3230454 | 1 | 121.4671460195 | 31.1463418849 | 124 | 10 | 2 | 27.4 | TDD | 352 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3249422 | 3 | 121.4690293455 | 31.1505707200 | 319 | 7 | 8 | 30.3 | TDD | 938 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3272656 | 2 | 121.4748071845 | 31.1476281640 | 102 | 15 | 4 | 40.6 | TDD | 249 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3274182 | 4 | 121.4739090100 | 31.1513182977 | 296 | 15 | 8 | 22.5 | TDD | 417 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.821 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.845 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.985 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.985 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.671 | NREventA3 | measId:2;ServCellPCI:85;Ser... |
| 2024-09-20 22:21:37.911 | NRHandoverAttempt | SourcePCI:85;SourceNR-ARFCN... |
| 2024-09-20 22:21:37.945 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.960 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.099 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.099 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230454 | 1 | 10.1874 | 19.4495 | -115.0791 | 16.0727 | 178.9202 | 0.0069 | 0.0002 |
| 2024_09_20 22:00 | 3272656 | 2 | 19.4275 | 15.6488 | -116.4941 | 6.2801 | 123.2748 | 0.0040 | 0.1763 |
| 2024_09_20 22:00 | 3249422 | 3 | 19.1810 | 18.8658 | -117.0094 | 9.0035 | 162.5003 | 0.0098 | 0.0068 |
| 2024_09_20 22:00 | 3274182 | 4 | 7.7954 | 10.6278 | -117.2848 | 6.4907 | 84.6212 | 0.0157 | 0.0028 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412415_D1473CC2 | 504990 | 352 | -83.7 | 504990 | 249 | -89.2 | 504990 | 938 | -84.0 | 504990 | 417 |
| MR_1774412415_C8AFD221 | 504990 | 249 | -86.0 | 504990 | 352 | -82.1 | 504990 | 938 | -80.4 | 504990 | 417 |
| MR_1774412415_38BB9F87 | 504990 | 249 | -87.1 | 504990 | 352 | -80.8 | 504990 | 938 | -80.8 | 504990 | 417 |
| MR_1774412415_A45307DD | 504990 | 249 | -89.2 | 504990 | 352 | -80.7 | 504990 | 938 | -82.1 | 504990 | 417 |
| MR_1774412415_14EAA282 | 504990 | 249 | -88.7 | 504990 | 352 | -80.9 | 504990 | 938 | -83.3 | 504990 | 417 |
| MR_1774412415_157DDDF2 | 504990 | 249 | -87.6 | 504990 | 352 | -80.7 | 504990 | 938 | -80.8 | 504990 | 417 |
| MR_1774412415_A9FC8C02 | 504990 | 249 | -89.2 | 504990 | 352 | -84.0 | 504990 | 938 | -82.8 | 504990 | 417 |
| MR_1774412415_8D85C37D | 504990 | 249 | -87.1 | 504990 | 352 | -81.3 | 504990 | 938 | -83.1 | 504990 | 417 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 473: `efd34331-bd2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `efd34331-bd21-4967-97af-f8fce4cc7038` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[473] topology](images/test_0473.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3239220_1
- `C2`: Adjust the azimuth of 3239220_1 by 50 degrees
- `C3`: Decrease transmission power for 3239220_1
- `C4`: Lift the tilt angle  of 3239220_1 by 7 degrees
- `C5`: Decrease transmission power for 3215666_2
- `C6`: Add neighbor relationship between 3215666_2 and 3239220_1
- `C7`: Press down the tilt angle of 3215666_2 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239220_1
- `C9`: Check test server and transmission issues
- `C10`: Adjust the azimuth of 3215666_2 by 50 degrees
- `C11`: Increase A3 Offset threshold for 3215666_2
- `C12`: Press down the tilt angle  of 3239220_1 by 7 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239220_1
- `C14`: Increase transmission power for 3215666_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215666_2
- `C16`: Add neighbor relationship between 3251748_3 and 3239220_1
- `C17`: Lift the tilt angle of 3215666_2 by 10 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215666_2
- `C20`: Decrease A3 Offset threshold for 3239220_1
- `C21`: Decrease A3 Offset threshold for 3215666_2
- `C22`: Increase A3 Offset threshold for 3239220_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.331 | MS1 | 121.4656589405 | 31.1446274193 | 219 | 504990 | -87.21 | 17.40 | 383.22 | 0.01 | 2.82 | 1585 |
| 2024-09-20 22:21:32.641 | MS1 | 121.4656688339 | 31.1446251621 | 219 | 504990 | -87.11 | 15.75 | 406.35 | 0.01 | 2.06 | 1583 |
| 2024-09-20 22:21:33.763 | MS1 | 121.4656627899 | 31.1446339356 | 219 | 504990 | -90.34 | 16.15 | 475.86 | 0.15 | 2.33 | 1565 |
| 2024-09-20 22:21:34.520 | MS1 | 121.4656707992 | 31.1446222719 | 219 | 504990 | -86.75 | 16.96 | 87.87 | 0.18 | 2.42 | 424 |
| 2024-09-20 22:21:35.510 | MS1 | 121.4656731090 | 31.1446272953 | 219 | 504990 | -86.79 | 16.71 | 80.96 | 0.17 | 2.94 | 330 |
| 2024-09-20 22:21:36.584 | MS1 | 121.4656633188 | 31.1446235217 | 219 | 504990 | -88.66 | 12.73 | 50.07 | 0.09 | 2.99 | 313 |
| 2024-09-20 22:21:37.457 | MS1 | 121.4656749639 | 31.1446271877 | 219 | 504990 | -93.44 | 8.60 | 88.98 | 0.19 | 2.06 | 427 |
| 2024-09-20 22:21:38.376 | MS1 | 121.4656609101 | 31.1446342050 | 219 | 504990 | -89.84 | 11.40 | 61.06 | 0.16 | 2.99 | 416 |
| 2024-09-20 22:21:39.179 | MS1 | 121.4656707135 | 31.1446288774 | 219 | 504990 | -92.08 | 8.68 | 77.01 | 0.18 | 2.46 | 336 |
| 2024-09-20 22:21:40.671 | MS1 | 121.4656633866 | 31.1446217786 | 219 | 504990 | -91.24 | 7.59 | 444.79 | 0.06 | 2.57 | 1578 |
| 2024-09-20 22:21:41.245 | MS1 | 121.4656655934 | 31.1446249851 | 219 | 504990 | -90.02 | 7.71 | 571.33 | 0.18 | 2.79 | 1580 |
| 2024-09-20 22:21:42.251 | MS1 | 121.4656758579 | 31.1446309579 | 219 | 504990 | -94.00 | 10.32 | 375.95 | 0.12 | 2.73 | 1562 |

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
| 3215666 | 2 | 121.4753015536 | 31.1523552614 | 50 | 12 | 6 | 24.2 | TDD | 219 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3215783 | 4 | 121.4743026130 | 31.1467956389 | 301 | 8 | 9 | 37.1 | TDD | 415 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3239220 | 1 | 121.4671462735 | 31.1517296757 | 313 | 4 | 11 | 41.7 | TDD | 73 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3251748 | 3 | 121.4685044388 | 31.1518276993 | 131 | 15 | 6 | 44.3 | TDD | 124 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.161 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.186 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.298 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.298 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.992 | NREventA3 | measId:2;ServCellPCI:982;Se... |
| 2024-09-20 22:21:38.232 | NRHandoverAttempt | SourcePCI:982;SourceNR-ARFC... |
| 2024-09-20 22:21:38.274 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.285 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.408 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.408 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239220 | 1 | 10.7041 | 10.3381 | -114.2643 | 11.5475 | 172.1018 | 0.0155 | 0.0163 |
| 2024_09_20 22:00 | 3215666 | 2 | 5.6143 | 12.6031 | -116.0055 | 8.8088 | 168.9975 | 0.0115 | 0.0103 |
| 2024_09_20 22:00 | 3251748 | 3 | 5.9266 | 15.4329 | -114.3657 | 11.0963 | 98.8035 | 0.0188 | 0.0193 |
| 2024_09_20 22:00 | 3215783 | 4 | 11.2978 | 9.3635 | -114.1741 | 11.2689 | 198.8123 | 0.0040 | 0.0083 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415784_651BA3E2 | 504990 | 219 | -87.2 | 504990 | 73 | -92.5 | 504990 | 124 | -95.8 | 504990 | 415 |
| MR_1774415784_36CB26D1 | 504990 | 219 | -88.5 | 504990 | 73 | -92.2 | 504990 | 124 | -95.2 | 504990 | 415 |
| MR_1774415784_19440A18 | 504990 | 219 | -88.7 | 504990 | 73 | -93.5 | 504990 | 124 | -98.5 | 504990 | 415 |
| MR_1774415784_9FE4904B | 504990 | 219 | -87.1 | 504990 | 73 | -92.3 | 504990 | 124 | -98.3 | 504990 | 415 |
| MR_1774415784_FA86DA5C | 504990 | 219 | -87.7 | 504990 | 73 | -92.2 | 504990 | 124 | -96.4 | 504990 | 415 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 474: `2b0b5c18-06c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2b0b5c18-06ca-445f-98e3-c040f2aeb22b` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[474] topology](images/test_0474.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3267267_3 by 6 degrees
- `C2`: Add neighbor relationship between 3267267_3 and 3267181_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267181_2
- `C4`: Increase transmission power for 3267181_2
- `C5`: Lift the tilt angle of 3267267_3 by 6 degrees
- `C6`: Adjust the azimuth of 3267267_3 by 12 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267267_3
- `C8`: Increase A3 Offset threshold for 3267181_2
- `C9`: Adjust the azimuth of 3273033_4 by 50 degrees
- `C10`: Increase A3 Offset threshold for 3267267_3
- `C11`: Decrease A3 Offset threshold for 3267181_2
- `C12`: Check test server and transmission issues
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267181_2
- `C14`: Press down the tilt angle  of 3273033_4 by 5 degrees
- `C15`: Decrease A3 Offset threshold for 3267267_3
- `C16`: Decrease transmission power for 3267267_3
- `C17`: Increase transmission power for 3267267_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267267_3
- `C19`: Decrease transmission power for 3267181_2
- `C20`: Lift the tilt angle  of 3273033_4 by 5 degrees
- `C21`: Add neighbor relationship between 3273033_4 and 3267181_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.326 | MS1 | 121.4656580893 | 31.1446302737 | 428 | 504990 | -88.35 | 17.65 | 499.91 | 0.13 | 2.91 | 1578 |
| 2024-09-20 22:21:32.670 | MS1 | 121.4656599401 | 31.1446297542 | 428 | 504990 | -90.22 | 15.79 | 480.13 | 0.17 | 2.72 | 1600 |
| 2024-09-20 22:21:33.574 | MS1 | 121.4656727463 | 31.1446257705 | 428 | 504990 | -91.86 | 13.67 | 357.74 | 0.11 | 2.62 | 1565 |
| 2024-09-20 22:21:34.188 | MS1 | 121.4656585540 | 31.1446268958 | 428 | 504990 | -85.55 | 12.92 | 54.23 | 0.13 | 2.11 | 1593 |
| 2024-09-20 22:21:35.668 | MS1 | 121.4656634808 | 31.1446256935 | 428 | 504990 | -88.41 | 14.38 | 67.93 | 0.03 | 2.07 | 1579 |
| 2024-09-20 22:21:36.758 | MS1 | 121.4656742575 | 31.1446181523 | 428 | 504990 | -89.44 | 17.89 | 53.11 | 0.06 | 2.31 | 1592 |
| 2024-09-20 22:21:37.193 | MS1 | 121.4656679663 | 31.1446187021 | 428 | 504990 | -93.29 | 9.50 | 76.62 | 0.01 | 2.12 | 1588 |
| 2024-09-20 22:21:38.272 | MS1 | 121.4656644537 | 31.1446214673 | 428 | 504990 | -91.21 | 10.57 | 95.35 | 0.07 | 2.90 | 1600 |
| 2024-09-20 22:21:39.757 | MS1 | 121.4656748828 | 31.1446257944 | 428 | 504990 | -93.52 | 11.81 | 66.89 | 0.17 | 2.65 | 1575 |
| 2024-09-20 22:21:40.900 | MS1 | 121.4656774973 | 31.1446331039 | 428 | 504990 | -90.15 | 8.49 | 511.83 | 0.00 | 2.77 | 1578 |
| 2024-09-20 22:21:41.129 | MS1 | 121.4656608528 | 31.1446328016 | 428 | 504990 | -90.70 | 8.64 | 308.13 | 0.05 | 2.95 | 1595 |
| 2024-09-20 22:21:42.433 | MS1 | 121.4656615431 | 31.1446265952 | 428 | 504990 | -89.71 | 9.92 | 552.48 | 0.05 | 2.66 | 1595 |

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
| 3267181 | 2 | 121.4653215511 | 31.1476387593 | 83 | 2 | 0 | 18.4 | TDD | 523 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3267267 | 3 | 121.4751796370 | 31.1526682137 | 213 | 4 | 1 | 39.9 | TDD | 428 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3271717 | 1 | 121.4705602422 | 31.1558084972 | 212 | 9 | 5 | 15.6 | TDD | 368 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3273033 | 4 | 121.4676807044 | 31.1486167307 | 23 | 3 | 1 | 47.4 | TDD | 973 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.276 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.293 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.416 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.416 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.119 | NREventA3 | measId:2;ServCellPCI:452;Se... |
| 2024-09-20 22:21:38.359 | NRHandoverAttempt | SourcePCI:452;SourceNR-ARFC... |
| 2024-09-20 22:21:38.402 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.417 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.556 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.556 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271717 | 1 | 11.5117 | 15.1890 | -114.9420 | 7.4395 | 176.1498 | 0.0036 | 0.0081 |
| 2024_09_20 22:00 | 3267181 | 2 | 6.2047 | 5.8422 | -115.6378 | 16.2355 | 147.7367 | 0.0044 | 0.0080 |
| 2024_09_20 22:00 | 3267267 | 3 | 86.8422 | 92.3593 | -114.5222 | 6.3937 | 197.7115 | 0.0049 | 0.0155 |
| 2024_09_20 22:00 | 3273033 | 4 | 15.6829 | 9.3122 | -116.5221 | 11.0983 | 91.1899 | 0.0183 | 0.0198 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412599_DAB6B0D3 | 504990 | 428 | -84.0 | 504990 | 523 | -91.4 | 504990 | 973 | -91.0 | 504990 | 368 |
| MR_1774412599_F60C070C | 504990 | 428 | -84.9 | 504990 | 523 | -88.8 | 504990 | 973 | -92.6 | 504990 | 368 |
| MR_1774412599_74CFC621 | 504990 | 428 | -85.6 | 504990 | 523 | -90.6 | 504990 | 973 | -90.8 | 504990 | 368 |
| MR_1774412599_5F7F917F | 504990 | 428 | -85.5 | 504990 | 523 | -88.8 | 504990 | 973 | -93.0 | 504990 | 368 |
| MR_1774412599_BCE3D593 | 504990 | 428 | -86.7 | 504990 | 523 | -89.3 | 504990 | 973 | -94.3 | 504990 | 368 |
| MR_1774412599_BFA207D5 | 504990 | 428 | -84.6 | 504990 | 523 | -90.5 | 504990 | 973 | -92.9 | 504990 | 368 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 475: `85114ee1-3ac...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `85114ee1-3aca-4d8e-b020-594cc0d393a5` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[475] topology](images/test_0475.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3261123_2 by 50 degrees
- `C2`: Lift the tilt angle of 3217710_1 by 10 degrees
- `C3`: Increase transmission power for 3217710_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217710_1
- `C5`: Decrease transmission power for 3217710_1
- `C6`: Adjust the azimuth of 3217710_1 by 50 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261123_2
- `C8`: Press down the tilt angle of 3217710_1 by 10 degrees
- `C9`: Add neighbor relationship between 3217710_1 and 3261123_2
- `C10`: Check test server and transmission issues
- `C11`: Add neighbor relationship between 3224126_3 and 3261123_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261123_2
- `C13`: Increase A3 Offset threshold for 3217710_1
- `C14`: Increase A3 Offset threshold for 3261123_2
- `C15`: Decrease A3 Offset threshold for 3217710_1
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Lift the tilt angle  of 3261123_2 by 4 degrees
- `C18`: Decrease transmission power for 3261123_2
- `C19`: Increase transmission power for 3261123_2
- `C20`: Decrease A3 Offset threshold for 3261123_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217710_1
- `C22`: Press down the tilt angle  of 3261123_2 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.142 | MS1 | 121.4656631292 | 31.1446274072 | 751 | 504990 | -86.78 | 12.64 | 509.09 | 0.12 | 2.99 | 1600 |
| 2024-09-20 22:21:32.260 | MS1 | 121.4656680321 | 31.1446359991 | 751 | 504990 | -91.50 | 13.30 | 564.74 | 0.06 | 2.54 | 1578 |
| 2024-09-20 22:21:33.228 | MS1 | 121.4656582863 | 31.1446244442 | 751 | 504990 | -91.59 | 16.37 | 361.21 | 0.04 | 2.51 | 1577 |
| 2024-09-20 22:21:34.719 | MS1 | 121.4656596934 | 31.1446376366 | 751 | 504990 | -86.90 | 12.07 | 77.61 | 0.15 | 2.22 | 451 |
| 2024-09-20 22:21:35.349 | MS1 | 121.4656761567 | 31.1446360833 | 751 | 504990 | -90.51 | 14.69 | 107.45 | 0.17 | 2.00 | 427 |
| 2024-09-20 22:21:36.147 | MS1 | 121.4656679562 | 31.1446313978 | 751 | 504990 | -90.74 | 12.43 | 80.37 | 0.11 | 2.73 | 486 |
| 2024-09-20 22:21:37.827 | MS1 | 121.4656732449 | 31.1446212956 | 751 | 504990 | -93.98 | 12.77 | 75.49 | 0.15 | 2.84 | 401 |
| 2024-09-20 22:21:38.975 | MS1 | 121.4656622028 | 31.1446378992 | 751 | 504990 | -93.56 | 10.71 | 99.79 | 0.02 | 2.29 | 455 |
| 2024-09-20 22:21:39.989 | MS1 | 121.4656627628 | 31.1446370753 | 751 | 504990 | -93.46 | 7.59 | 60.92 | 0.08 | 2.97 | 427 |
| 2024-09-20 22:21:40.499 | MS1 | 121.4656712308 | 31.1446313608 | 751 | 504990 | -89.94 | 9.85 | 368.80 | 0.10 | 2.25 | 1594 |
| 2024-09-20 22:21:41.897 | MS1 | 121.4656694056 | 31.1446209203 | 751 | 504990 | -93.74 | 11.69 | 434.16 | 0.10 | 2.82 | 1570 |
| 2024-09-20 22:21:42.193 | MS1 | 121.4656604053 | 31.1446182952 | 751 | 504990 | -93.29 | 11.39 | 594.54 | 0.03 | 2.37 | 1564 |

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
| 3217710 | 1 | 121.4661116647 | 31.1520664743 | 29 | 8 | 5 | 44.9 | TDD | 751 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3224126 | 3 | 121.4660443459 | 31.1488405933 | 313 | 4 | 1 | 16.4 | TDD | 678 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3259114 | 4 | 121.4714109429 | 31.1446130135 | 346 | 3 | 12 | 24.2 | TDD | 727 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3261123 | 2 | 121.4681859559 | 31.1485081954 | 267 | 1 | 7 | 27.9 | TDD | 133 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.293 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.316 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.448 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.448 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.163 | NREventA3 | measId:2;ServCellPCI:221;Se... |
| 2024-09-20 22:21:38.403 | NRHandoverAttempt | SourcePCI:221;SourceNR-ARFC... |
| 2024-09-20 22:21:38.447 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.461 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.608 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.608 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217710 | 1 | 18.0188 | 13.5252 | -115.9969 | 13.7719 | 90.0392 | 0.0156 | 0.0114 |
| 2024_09_20 22:00 | 3261123 | 2 | 5.5233 | 5.9475 | -114.5277 | 12.2968 | 160.1024 | 0.0126 | 0.0003 |
| 2024_09_20 22:00 | 3224126 | 3 | 12.5630 | 11.0385 | -114.6318 | 18.9540 | 141.8004 | 0.0153 | 0.0024 |
| 2024_09_20 22:00 | 3259114 | 4 | 7.4808 | 5.0409 | -117.0492 | 13.7594 | 149.5609 | 0.0010 | 0.0153 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412274_DAF6ED6D | 504990 | 751 | -88.1 | 504990 | 133 | -90.3 | 504990 | 678 | -98.6 | 504990 | 727 |
| MR_1774412274_9D5A544B | 504990 | 751 | -86.6 | 504990 | 133 | -89.7 | 504990 | 678 | -100.9 | 504990 | 727 |
| MR_1774412274_2CACE3E4 | 504990 | 751 | -86.2 | 504990 | 133 | -91.6 | 504990 | 678 | -97.5 | 504990 | 727 |
| MR_1774412274_EBF3223B | 504990 | 751 | -86.9 | 504990 | 133 | -92.0 | 504990 | 678 | -100.0 | 504990 | 727 |
| MR_1774412274_99BE9CBF | 504990 | 751 | -87.4 | 504990 | 133 | -90.2 | 504990 | 678 | -97.6 | 504990 | 727 |
| MR_1774412274_8721F7DC | 504990 | 751 | -85.0 | 504990 | 133 | -91.9 | 504990 | 678 | -99.1 | 504990 | 727 |
| MR_1774412274_0E5D5AA4 | 504990 | 751 | -87.5 | 504990 | 133 | -89.3 | 504990 | 678 | -100.1 | 504990 | 727 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 476: `9224ad4a-0eb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9224ad4a-0eb9-46d3-b18c-e9a7eb7604b9` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[476] topology](images/test_0476.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240077_4
- `C2`: Adjust the azimuth of 3240207_1 by 50 degrees
- `C3`: Increase transmission power for 3240207_1
- `C4`: Decrease A3 Offset threshold for 3240077_4
- `C5`: Add neighbor relationship between 3269401_3 and 3240077_4
- `C6`: Increase transmission power for 3240077_4
- `C7`: Lift the tilt angle of 3240207_1 by 10 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240207_1
- `C9`: Lift the tilt angle  of 3240077_4 by 4 degrees
- `C10`: Decrease A3 Offset threshold for 3240207_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease transmission power for 3240077_4
- `C13`: Decrease transmission power for 3240207_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240077_4
- `C15`: Add neighbor relationship between 3240207_1 and 3240077_4
- `C16`: Press down the tilt angle of 3240207_1 by 10 degrees
- `C17`: Check test server and transmission issues
- `C18`: Increase A3 Offset threshold for 3240077_4
- `C19`: Adjust the azimuth of 3240077_4 by 47 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240207_1
- `C21`: Press down the tilt angle  of 3240077_4 by 4 degrees
- `C22`: Increase A3 Offset threshold for 3240207_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.148 | MS1 | 121.4656698819 | 31.1446186748 | 344 | 504990 | -94.34 | 14.50 | 384.63 | 0.10 | 2.64 | 1584 |
| 2024-09-20 22:21:32.922 | MS1 | 121.4656711643 | 31.1446373866 | 344 | 504990 | -92.91 | 15.11 | 515.59 | 0.14 | 2.62 | 1581 |
| 2024-09-20 22:21:33.380 | MS1 | 121.4656728607 | 31.1446280325 | 344 | 504990 | -94.12 | 16.38 | 514.96 | 0.07 | 2.81 | 1589 |
| 2024-09-20 22:21:34.431 | MS1 | 121.4656746393 | 31.1446321798 | 344 | 504990 | -104.67 | 0.47 | 80.32 | 0.07 | 1.08 | 1561 |
| 2024-09-20 22:21:35.639 | MS1 | 121.4656653414 | 31.1446193403 | 344 | 504990 | -106.34 | 1.20 | 23.77 | 0.20 | 1.42 | 1565 |
| 2024-09-20 22:21:36.268 | MS1 | 121.4656752267 | 31.1446369818 | 344 | 504990 | -107.92 | -1.39 | 52.26 | 0.10 | 1.07 | 1566 |
| 2024-09-20 22:21:37.991 | MS1 | 121.4656738861 | 31.1446250786 | 344 | 504990 | -107.64 | -0.73 | 25.98 | 0.19 | 1.38 | 1575 |
| 2024-09-20 22:21:38.600 | MS1 | 121.4656625118 | 31.1446379551 | 344 | 504990 | -104.51 | 0.31 | 23.50 | 0.11 | 1.07 | 1571 |
| 2024-09-20 22:21:39.247 | MS1 | 121.4656727642 | 31.1446323441 | 344 | 504990 | -103.92 | 1.80 | 74.76 | 0.19 | 1.19 | 1569 |
| 2024-09-20 22:21:40.814 | MS1 | 121.4656771025 | 31.1446187850 | 344 | 504990 | -88.69 | 13.66 | 580.22 | 0.18 | 2.36 | 1584 |
| 2024-09-20 22:21:41.348 | MS1 | 121.4656776149 | 31.1446274731 | 344 | 504990 | -85.88 | 14.81 | 477.36 | 0.18 | 2.35 | 1598 |
| 2024-09-20 22:21:42.964 | MS1 | 121.4656756326 | 31.1446379835 | 344 | 504990 | -89.31 | 16.53 | 373.97 | 0.05 | 2.39 | 1599 |

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
| 3228913 | 2 | 121.4676135135 | 31.1476578777 | 254 | 8 | 3 | 42.0 | TDD | 752 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3240077 | 4 | 121.4683118843 | 31.1510316078 | 247 | 2 | 12 | 27.8 | TDD | 615 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3240207 | 1 | 121.4652264999 | 31.1465352308 | 103 | 11 | 6 | 20.5 | TDD | 344 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3269401 | 3 | 121.4748044721 | 31.1470054280 | 112 | 3 | 2 | 46.3 | TDD | 604 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.319 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.336 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.445 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.445 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.670 | NREventA2 | measId:1;ServCellPCI:565;Se... |
| 2024-09-20 22:21:34.790 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240207 | 1 | 7.2399 | 9.2604 | -115.7869 | 5.5449 | 106.7644 | 0.1687 | 0.0087 |
| 2024_09_20 22:00 | 3228913 | 2 | 9.6604 | 15.2591 | -117.1845 | 11.8233 | 142.2060 | 0.0004 | 0.0189 |
| 2024_09_20 22:00 | 3269401 | 3 | 8.3463 | 5.9012 | -117.5261 | 8.5678 | 190.3519 | 0.0116 | 0.0010 |
| 2024_09_20 22:00 | 3240077 | 4 | 8.4008 | 16.3191 | -116.4549 | 6.3028 | 114.2363 | 0.0043 | 0.0109 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414816_94577B93 | 504990 | 344 | -104.7 | 504990 | 615 | -108.2 | 504990 | 604 | -117.2 | 504990 | 752 |
| MR_1774414816_7CC116F8 | 504990 | 344 | -105.3 | 504990 | 615 | -109.8 | 504990 | 604 | -113.5 | 504990 | 752 |
| MR_1774414816_8F20AC02 | 504990 | 344 | -104.1 | 504990 | 615 | -108.9 | 504990 | 604 | -114.0 | 504990 | 752 |
| MR_1774414816_12EA8804 | 504990 | 344 | -103.0 | 504990 | 615 | -107.9 | 504990 | 604 | -116.7 | 504990 | 752 |
| MR_1774414816_1B4B6E4C | 504990 | 344 | -105.9 | 504990 | 615 | -107.6 | 504990 | 604 | -114.4 | 504990 | 752 |
| MR_1774414816_730908EC | 504990 | 344 | -103.7 | 504990 | 615 | -110.4 | 504990 | 604 | -116.5 | 504990 | 752 |
| MR_1774414816_C80CAC64 | 504990 | 344 | -102.9 | 504990 | 615 | -111.1 | 504990 | 604 | -115.2 | 504990 | 752 |
| MR_1774414816_BFD25F26 | 504990 | 344 | -104.6 | 504990 | 615 | -111.0 | 504990 | 604 | -116.3 | 504990 | 752 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 477: `81e4c4d8-23e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `81e4c4d8-23e0-42ab-a9ab-160e44205757` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[477] topology](images/test_0477.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3240949_3
- `C2`: Increase transmission power for 3240949_3
- `C3`: Add neighbor relationship between 3211071_7 and 3240949_3
- `C4`: Press down the tilt angle  of 3240949_3 by 4 degrees
- `C5`: Adjust the azimuth of 3269264_6 by 3 degrees
- `C6`: Adjust the azimuth of 3240949_3 by 22 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269264_6
- `C8`: Increase transmission power for 3269264_6
- `C9`: Increase A3 Offset threshold for 3240949_3
- `C10`: Lift the tilt angle of 3269264_6 by 5 degrees
- `C11`: Decrease A3 Offset threshold for 3240949_3
- `C12`: Check test server and transmission issues
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269264_6
- `C14`: Decrease transmission power for 3269264_6
- `C15`: Decrease A3 Offset threshold for 3269264_6
- `C16`: Add neighbor relationship between 3269264_6 and 3240949_3
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Lift the tilt angle  of 3240949_3 by 4 degrees
- `C19`: Increase A3 Offset threshold for 3269264_6
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240949_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240949_3
- `C22`: Press down the tilt angle of 3269264_6 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.128 | MS1 | 121.4656615246 | 31.1446255110 | 438 | 504990 | -93.19 | 12.05 | 387.63 | 0.17 | 2.22 | 1576 |
| 2024-09-20 22:21:32.745 | MS1 | 121.4656595686 | 31.1446265668 | 367 | 504990 | -95.84 | 14.30 | 418.26 | 0.10 | 2.30 | 1571 |
| 2024-09-20 22:21:33.226 | MS1 | 121.4656637737 | 31.1446180949 | 598 | 504990 | -93.02 | 13.27 | 460.85 | 0.08 | 2.21 | 1590 |
| 2024-09-20 22:21:34.492 | MS1 | 121.4656653807 | 31.1446340250 | 857 | 152650 | -91.49 | 6.54 | 99.01 | 0.14 | 1.60 | 988 |
| 2024-09-20 22:21:35.517 | MS1 | 121.4656735352 | 31.1446271261 | 726 | 152650 | -87.80 | 2.21 | 62.44 | 0.11 | 1.64 | 980 |
| 2024-09-20 22:21:36.507 | MS1 | 121.4656767049 | 31.1446259720 | 752 | 152650 | -89.72 | 4.48 | 64.65 | 0.09 | 1.72 | 905 |
| 2024-09-20 22:21:37.413 | MS1 | 121.4656731522 | 31.1446278989 | 824 | 152650 | -96.67 | 5.20 | 61.64 | 0.04 | 1.66 | 973 |
| 2024-09-20 22:21:38.738 | MS1 | 121.4656635791 | 31.1446372033 | 857 | 152650 | -88.07 | 6.89 | 46.97 | 0.13 | 1.56 | 988 |
| 2024-09-20 22:21:39.910 | MS1 | 121.4656676675 | 31.1446243795 | 726 | 152650 | -87.63 | 4.94 | 68.92 | 0.05 | 1.72 | 964 |
| 2024-09-20 22:21:40.256 | MS1 | 121.4656701134 | 31.1446351500 | 752 | 152650 | -89.74 | 7.79 | 87.44 | 0.11 | 2.99 | 1596 |
| 2024-09-20 22:21:41.364 | MS1 | 121.4656608909 | 31.1446273842 | 824 | 152650 | -90.33 | 2.76 | 78.44 | 0.00 | 2.41 | 1600 |
| 2024-09-20 22:21:42.244 | MS1 | 121.4656730903 | 31.1446248165 | 857 | 152650 | -94.20 | 5.36 | 76.89 | 0.03 | 2.05 | 1578 |

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
| 3211071 | 7 | 121.4699923230 | 31.1554135791 | 319 | 7 | 11 | 6.0 | FDD | 752 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3211349 | 11 | 121.4692648867 | 31.1550139452 | 294 | 11 | 4 | 11.9 | FDD | 824 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3212753 | 13 | 121.4752913584 | 31.1554938016 | 22 | 13 | 3 | 15.5 | FDD | 509 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3218388 | 1 | 121.4708271736 | 31.1517762784 | 119 | 4 | 1 | 2.1 | TDD | 710 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3221754 | 10 | 121.4748884139 | 31.1493640700 | 189 | 11 | 2 | 26.7 | FDD | 726 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3224451 | 5 | 121.4720691640 | 31.1527787587 | 115 | 7 | 7 | 21.3 | TDD | 598 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3228246 | 2 | 121.4663007693 | 31.1503333932 | 1 | 6 | 4 | 22.2 | TDD | 263 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3229815 | 8 | 121.4640393363 | 31.1497740995 | 210 | 1 | 1 | 26.9 | FDD | 274 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3240949 | 3 | 121.4691164227 | 31.1455070136 | 232 | 2 | 2 | 11.5 | TDD | 778 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3255218 | 9 | 121.4672917311 | 31.1472036149 | 357 | 2 | 6 | 20.8 | FDD | 466 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3257712 | 4 | 121.4742434824 | 31.1528873032 | 341 | 13 | 5 | 22.5 | TDD | 367 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3269264 | 6 | 121.4748721984 | 31.1506218073 | 236 | 4 | 5 | 25.5 | TDD | 438 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3279497 | 12 | 121.4710665913 | 31.1467392691 | 49 | 10 | 0 | 26.4 | FDD | 857 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |

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
| 2024-09-20 22:21:31.577 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.594 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.737 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.737 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.467 | NREventA2 | measId:1;ServCellPCI:884;Se... |
| 2024-09-20 22:21:35.609 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.895 | NREventA5 | measId:3;ServCellPCI:884;Se... |
| 2024-09-20 22:21:35.964 | NRHandoverAttempt | SourcePCI:884;SourceNR-ARFC... |
| 2024-09-20 22:21:35.995 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.006 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.155 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.155 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218388 | 1 | 6.1553 | 16.9717 | -115.8239 | 7.5257 | 156.5711 | 0.0168 | 0.0126 |
| 2024_09_20 22:00 | 3228246 | 2 | 15.2412 | 14.6182 | -116.3631 | 18.3610 | 134.9086 | 0.0187 | 0.0151 |
| 2024_09_20 22:00 | 3240949 | 3 | 11.9582 | 5.3547 | -114.8534 | 5.5139 | 176.8388 | 0.0108 | 0.0131 |
| 2024_09_20 22:00 | 3257712 | 4 | 6.8882 | 15.1114 | -115.8013 | 16.2598 | 132.1343 | 0.0052 | 0.0059 |
| 2024_09_20 22:00 | 3224451 | 5 | 11.0868 | 5.6222 | -117.5087 | 19.4203 | 118.0984 | 0.0007 | 0.0166 |
| 2024_09_20 22:00 | 3269264 | 6 | 7.5068 | 6.6875 | -116.3529 | 7.0803 | 180.3376 | 0.0162 | 0.0164 |
| 2024_09_20 22:00 | 3211071 | 7 | 15.1865 | 17.1391 | -115.9475 | 3.4435 | 21.3431 | 0.0058 | 0.0100 |
| 2024_09_20 22:00 | 3229815 | 8 | 15.5605 | 7.1381 | -117.9970 | 3.4696 | 41.2531 | 0.0176 | 0.0125 |
| 2024_09_20 22:00 | 3255218 | 9 | 14.2696 | 13.1512 | -114.7304 | 4.7663 | 35.9327 | 0.0190 | 0.0034 |
| 2024_09_20 22:00 | 3221754 | 10 | 13.1079 | 15.8779 | -116.8332 | 3.8730 | 48.3864 | 0.0134 | 0.0012 |
| 2024_09_20 22:00 | 3211349 | 11 | 8.3866 | 6.3473 | -115.6512 | 3.2432 | 26.2778 | 0.0026 | 0.0014 |
| 2024_09_20 22:00 | 3279497 | 12 | 14.0107 | 11.1099 | -115.8076 | 3.5759 | 41.6605 | 0.0061 | 0.0005 |
| 2024_09_20 22:00 | 3212753 | 13 | 11.6327 | 7.5447 | -114.1309 | 3.6659 | 33.7884 | 0.0039 | 0.0029 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417213_F245783D | 504990 | 598 | -91.6 | 504990 | 778 | -88.7 | 504990 | 263 | -96.6 | 504990 | 710 |
| MR_1774417213_D659D59E | 504990 | 598 | -91.5 | 504990 | 778 | -91.8 | 504990 | 263 | -97.1 | 504990 | 710 |
| MR_1774417213_52980462 | 504990 | 598 | -94.0 | 504990 | 778 | -89.8 | 504990 | 263 | -98.5 | 504990 | 710 |
| MR_1774417213_0F96A97F | 152650 | 857 | -93.1 | 152650 | 509 | -94.8 | 152650 | 274 | -101.0 | 152650 | 466 |
| MR_1774417213_7272D187 | 152650 | 857 | -92.7 | 152650 | 509 | -94.1 | 152650 | 274 | -99.0 | 152650 | 466 |
| MR_1774417213_F32C0439 | 504990 | 598 | -92.1 | 504990 | 778 | -90.2 | 504990 | 263 | -96.7 | 504990 | 710 |
| MR_1774417213_1A0D6104 | 152650 | 857 | -90.3 | 152650 | 509 | -93.1 | 152650 | 274 | -98.6 | 152650 | 466 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 478: `86b8d1cc-5b7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `86b8d1cc-5b7c-4ed8-b008-7c9d03b6dba3` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[478] topology](images/test_0478.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3267623_1
- `C2`: Increase transmission power for 3267623_1
- `C3`: Increase transmission power for 3264723_3
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Lift the tilt angle of 3264723_3 by 6 degrees
- `C6`: Adjust the azimuth of 3267623_1 by 5 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264723_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267623_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264723_3
- `C10`: Lift the tilt angle  of 3267623_1 by 4 degrees
- `C11`: Increase A3 Offset threshold for 3264723_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267623_1
- `C13`: Add neighbor relationship between 3227953_4 and 3267623_1
- `C14`: Adjust the azimuth of 3264723_3 by 50 degrees
- `C15`: Decrease A3 Offset threshold for 3267623_1
- `C16`: Press down the tilt angle  of 3267623_1 by 4 degrees
- `C17`: Decrease A3 Offset threshold for 3264723_3
- `C18`: Decrease transmission power for 3264723_3
- `C19`: Decrease transmission power for 3267623_1
- `C20`: Add neighbor relationship between 3264723_3 and 3267623_1
- `C21`: Check test server and transmission issues
- `C22`: Press down the tilt angle of 3264723_3 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.527 | MS1 | 121.4656758658 | 31.1446207357 | 60 | 504990 | -80.35 | 13.06 | 441.76 | 0.17 | 2.00 | 1599 |
| 2024-09-20 22:21:32.901 | MS1 | 121.4656761919 | 31.1446199882 | 60 | 504990 | -81.09 | 15.91 | 415.77 | 0.10 | 2.65 | 1587 |
| 2024-09-20 22:21:33.751 | MS1 | 121.4656700856 | 31.1446282693 | 60 | 504990 | -84.34 | 13.40 | 445.60 | 0.01 | 2.96 | 1580 |
| 2024-09-20 22:21:34.357 | MS1 | 121.4656692733 | 31.1446294302 | 60 | 504990 | -94.48 | -0.98 | 61.17 | 0.07 | 1.47 | 1577 |
| 2024-09-20 22:21:35.875 | MS1 | 121.4656714437 | 31.1446307957 | 60 | 504990 | -88.98 | -0.92 | 57.58 | 0.18 | 1.04 | 1583 |
| 2024-09-20 22:21:36.125 | MS1 | 121.4656591957 | 31.1446220413 | 60 | 504990 | -93.92 | -1.06 | 58.44 | 0.15 | 1.33 | 1570 |
| 2024-09-20 22:21:37.927 | MS1 | 121.4656693900 | 31.1446220725 | 60 | 504990 | -87.86 | -3.61 | 64.57 | 0.11 | 1.38 | 1591 |
| 2024-09-20 22:21:38.707 | MS1 | 121.4656727889 | 31.1446361903 | 60 | 504990 | -77.32 | 16.28 | 301.73 | 0.18 | 1.29 | 1582 |
| 2024-09-20 22:21:39.562 | MS1 | 121.4656628770 | 31.1446283809 | 60 | 504990 | -79.84 | 14.24 | 573.58 | 0.01 | 1.21 | 1573 |
| 2024-09-20 22:21:40.163 | MS1 | 121.4656592857 | 31.1446193585 | 60 | 504990 | -83.05 | 17.00 | 401.82 | 0.10 | 2.52 | 1597 |
| 2024-09-20 22:21:41.139 | MS1 | 121.4656644135 | 31.1446290481 | 60 | 504990 | -82.97 | 16.35 | 443.48 | 0.00 | 2.54 | 1595 |
| 2024-09-20 22:21:42.643 | MS1 | 121.4656719576 | 31.1446239397 | 60 | 504990 | -83.29 | 13.12 | 455.48 | 0.09 | 2.25 | 1592 |

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
| 3227953 | 4 | 121.4642345552 | 31.1527249715 | 168 | 8 | 7 | 46.8 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3256337 | 2 | 121.4727324174 | 31.1526174293 | 283 | 2 | 10 | 27.8 | TDD | 770 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3264723 | 3 | 121.4640804977 | 31.1507408560 | 337 | 3 | 7 | 38.2 | TDD | 60 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3267623 | 1 | 121.4741667432 | 31.1450554380 | 272 | 1 | 5 | 36.9 | TDD | 602 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.332 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.350 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.468 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.468 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.168 | NREventA3 | measId:2;ServCellPCI:271;Se... |
| 2024-09-20 22:21:36.168 | NREventA3 | measId:2;ServCellPCI:271;Se... |
| 2024-09-20 22:21:37.168 | NREventA3 | measId:2;ServCellPCI:271;Se... |
| 2024-09-20 22:21:39.668 | NRRRCReestablishAttempt | PCI:271 |
| 2024-09-20 22:21:39.678 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.688 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.833 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.833 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267623 | 1 | 8.4213 | 11.1855 | -114.3761 | 18.1810 | 149.8389 | 0.0008 | 0.0035 |
| 2024_09_20 22:00 | 3256337 | 2 | 8.4987 | 6.1582 | -114.0637 | 12.3982 | 144.7714 | 0.0004 | 0.0120 |
| 2024_09_20 22:00 | 3264723 | 3 | 12.2545 | 6.1884 | -117.4429 | 7.5882 | 105.4460 | 0.0002 | 0.1742 |
| 2024_09_20 22:00 | 3227953 | 4 | 16.5626 | 8.3224 | -115.4643 | 10.7609 | 178.6214 | 0.0026 | 0.0111 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413269_BD671DDA | 504990 | 602 | -89.0 | 504990 | 60 | -94.2 | 504990 | 309 | -90.7 | 504990 | 770 |
| MR_1774413269_10B8A971 | 504990 | 60 | -94.8 | 504990 | 602 | -90.0 | 504990 | 309 | -89.3 | 504990 | 770 |
| MR_1774413269_F3E01B34 | 504990 | 60 | -96.5 | 504990 | 602 | -90.0 | 504990 | 309 | -91.7 | 504990 | 770 |
| MR_1774413269_4E397C2A | 504990 | 60 | -93.4 | 504990 | 602 | -89.4 | 504990 | 309 | -91.5 | 504990 | 770 |
| MR_1774413269_867B34FD | 504990 | 602 | -89.3 | 504990 | 60 | -92.7 | 504990 | 309 | -89.4 | 504990 | 770 |
| MR_1774413269_909A6968 | 504990 | 60 | -95.0 | 504990 | 602 | -90.7 | 504990 | 309 | -90.4 | 504990 | 770 |
| MR_1774413269_D79839A3 | 504990 | 602 | -89.2 | 504990 | 60 | -94.3 | 504990 | 309 | -90.5 | 504990 | 770 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 479: `17c4c305-458...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `17c4c305-4583-41a7-8a0e-c940c7a3d5fb` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[479] topology](images/test_0479.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3229843_4
- `C2`: Check test server and transmission issues
- `C3`: Press down the tilt angle  of 3223516_1 by 10 degrees
- `C4`: Add neighbor relationship between 3223516_1 and 3229843_4
- `C5`: Press down the tilt angle of 3226030_2 by 3 degrees
- `C6`: Increase transmission power for 3226030_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229843_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226030_2
- `C9`: Decrease A3 Offset threshold for 3229843_4
- `C10`: Add neighbor relationship between 3226030_2 and 3229843_4
- `C11`: Lift the tilt angle of 3226030_2 by 3 degrees
- `C12`: Adjust the azimuth of 3223516_1 by 13 degrees
- `C13`: Adjust the azimuth of 3226030_2 by 7 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226030_2
- `C16`: Decrease transmission power for 3226030_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229843_4
- `C18`: Decrease A3 Offset threshold for 3226030_2
- `C19`: Increase transmission power for 3229843_4
- `C20`: Increase A3 Offset threshold for 3229843_4
- `C21`: Lift the tilt angle  of 3223516_1 by 10 degrees
- `C22`: Increase A3 Offset threshold for 3226030_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.571 | MS1 | 121.4656735858 | 31.1446204643 | 481 | 504990 | -89.28 | 16.19 | 502.87 | 0.04 | 2.22 | 1595 |
| 2024-09-20 22:21:32.586 | MS1 | 121.4656731787 | 31.1446244367 | 481 | 504990 | -87.58 | 12.49 | 555.69 | 0.09 | 2.47 | 1566 |
| 2024-09-20 22:21:33.786 | MS1 | 121.4656745684 | 31.1446330578 | 481 | 504990 | -86.70 | 13.43 | 348.95 | 0.10 | 2.81 | 1589 |
| 2024-09-20 22:21:34.447 | MS1 | 121.4656631230 | 31.1446296415 | 481 | 504990 | -91.99 | 17.00 | 91.28 | 0.14 | 2.50 | 1595 |
| 2024-09-20 22:21:35.959 | MS1 | 121.4656679579 | 31.1446273093 | 481 | 504990 | -91.17 | 12.60 | 63.53 | 0.16 | 2.75 | 1580 |
| 2024-09-20 22:21:36.538 | MS1 | 121.4656589646 | 31.1446201890 | 481 | 504990 | -90.07 | 13.28 | 85.58 | 0.16 | 2.74 | 1581 |
| 2024-09-20 22:21:37.932 | MS1 | 121.4656702727 | 31.1446327726 | 481 | 504990 | -91.91 | 10.83 | 76.86 | 0.19 | 2.21 | 1571 |
| 2024-09-20 22:21:38.931 | MS1 | 121.4656582555 | 31.1446253157 | 481 | 504990 | -93.57 | 10.42 | 105.17 | 0.08 | 2.24 | 1594 |
| 2024-09-20 22:21:39.419 | MS1 | 121.4656693478 | 31.1446327828 | 481 | 504990 | -93.52 | 7.23 | 68.03 | 0.06 | 2.52 | 1579 |
| 2024-09-20 22:21:40.674 | MS1 | 121.4656661357 | 31.1446279143 | 481 | 504990 | -93.45 | 9.21 | 364.61 | 0.03 | 2.11 | 1596 |
| 2024-09-20 22:21:41.997 | MS1 | 121.4656716183 | 31.1446256938 | 481 | 504990 | -92.76 | 12.96 | 379.96 | 0.05 | 2.01 | 1574 |
| 2024-09-20 22:21:42.366 | MS1 | 121.4656614173 | 31.1446364446 | 481 | 504990 | -93.21 | 9.10 | 597.52 | 0.20 | 2.72 | 1571 |

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
| 3223516 | 1 | 121.4708884606 | 31.1442427241 | 36 | 2 | 7 | 20.3 | TDD | 200 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3226030 | 2 | 121.4701413072 | 31.1472194534 | 243 | 1 | 10 | 15.6 | TDD | 481 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3226537 | 3 | 121.4682387823 | 31.1499463062 | 178 | 3 | 6 | 35.3 | TDD | 306 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3229843 | 4 | 121.4755456003 | 31.1511648298 | 245 | 10 | 9 | 18.1 | TDD | 775 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.807 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.832 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.958 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.958 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.683 | NREventA3 | measId:2;ServCellPCI:643;Se... |
| 2024-09-20 22:21:37.923 | NRHandoverAttempt | SourcePCI:643;SourceNR-ARFC... |
| 2024-09-20 22:21:37.963 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.973 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.074 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.074 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223516 | 1 | 12.7977 | 11.0745 | -114.6535 | 5.8975 | 116.9109 | 0.0082 | 0.0037 |
| 2024_09_20 22:00 | 3226030 | 2 | 83.5292 | 76.5505 | -117.6953 | 12.3734 | 181.7127 | 0.0170 | 0.0136 |
| 2024_09_20 22:00 | 3226537 | 3 | 16.3186 | 18.3121 | -114.5815 | 12.6500 | 158.9425 | 0.0025 | 0.0008 |
| 2024_09_20 22:00 | 3229843 | 4 | 13.7316 | 7.3235 | -116.6301 | 6.7289 | 106.8580 | 0.0186 | 0.0093 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413304_D5C619ED | 504990 | 481 | -91.0 | 504990 | 775 | -93.0 | 504990 | 200 | -100.2 | 504990 | 306 |
| MR_1774413304_A3F78D79 | 504990 | 481 | -91.2 | 504990 | 775 | -95.1 | 504990 | 200 | -98.9 | 504990 | 306 |
| MR_1774413304_25224D45 | 504990 | 481 | -91.2 | 504990 | 775 | -93.8 | 504990 | 200 | -98.8 | 504990 | 306 |
| MR_1774413304_74D5D63A | 504990 | 481 | -91.3 | 504990 | 775 | -92.9 | 504990 | 200 | -97.5 | 504990 | 306 |
| MR_1774413304_B675739C | 504990 | 481 | -92.8 | 504990 | 775 | -93.1 | 504990 | 200 | -99.6 | 504990 | 306 |
| MR_1774413304_59E4C4CC | 504990 | 481 | -90.9 | 504990 | 775 | -96.0 | 504990 | 200 | -96.9 | 504990 | 306 |
| MR_1774413304_3712BBA5 | 504990 | 481 | -91.7 | 504990 | 775 | -92.8 | 504990 | 200 | -96.9 | 504990 | 306 |
| MR_1774413304_3E5B601A | 504990 | 481 | -92.1 | 504990 | 775 | -96.0 | 504990 | 200 | -99.9 | 504990 | 306 |

> *... 2개 열 생략 (전체 14열)*

---
