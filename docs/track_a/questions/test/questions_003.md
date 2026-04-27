# Track A 문제 분석 — test[20]~test[29]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[20] ~ test[29] (10개)

## 목차

1. [문제 20: `f1d0426c-94a...`](#20) — single-answer
2. [문제 21: `558e64d5-26a...`](#21) — single-answer
3. [문제 22: `06b971d7-131...`](#22) — single-answer
4. [문제 23: `28312271-c54...`](#23) — single-answer
5. [문제 24: `aa431504-d22...`](#24) — single-answer
6. [문제 25: `8ed1021f-abd...`](#25) — single-answer
7. [문제 26: `be3d8972-47e...`](#26) — single-answer
8. [문제 27: `873fc69e-de6...`](#27) — single-answer
9. [문제 28: `953a2987-d2c...`](#28) — single-answer
10. [문제 29: `57895e51-e6e...`](#29) — single-answer

---

### 문제 20: `f1d0426c-94a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f1d0426c-94a2-496e-b5c5-d8ead9e867ca` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[20] topology](images/test_0020.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252744_1
- `C2`: Decrease A3 Offset threshold for 3252744_1
- `C3`: Increase A3 Offset threshold for 3277712_6
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277712_6
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277712_6
- `C7`: Increase A3 Offset threshold for 3252744_1
- `C8`: Press down the tilt angle  of 3252744_1 by 4 degrees
- `C9`: Lift the tilt angle of 3277712_6 by 5 degrees
- `C10`: Decrease transmission power for 3277712_6
- `C11`: Adjust the azimuth of 3277712_6 by 4 degrees
- `C12`: Press down the tilt angle of 3277712_6 by 5 degrees
- `C13`: Decrease A3 Offset threshold for 3277712_6
- `C14`: Increase transmission power for 3252744_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252744_1
- `C16`: Increase transmission power for 3277712_6
- `C17`: Adjust the azimuth of 3252744_1 by 38 degrees
- `C18`: Decrease transmission power for 3252744_1
- `C19`: Add neighbor relationship between 3277712_6 and 3252744_1
- `C20`: Check test server and transmission issues
- `C21`: Lift the tilt angle  of 3252744_1 by 4 degrees
- `C22`: Add neighbor relationship between 3218837_13 and 3252744_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.626 | MS1 | 121.4656596872 | 31.1446375754 | 316 | 504990 | -94.68 | 12.60 | 494.04 | 0.00 | 2.52 | 1595 |
| 2024-09-20 22:21:32.771 | MS1 | 121.4656708507 | 31.1446288734 | 258 | 504990 | -94.69 | 11.25 | 596.13 | 0.19 | 2.94 | 1596 |
| 2024-09-20 22:21:33.131 | MS1 | 121.4656661675 | 31.1446286489 | 782 | 504990 | -94.94 | 11.26 | 338.42 | 0.02 | 2.79 | 1564 |
| 2024-09-20 22:21:34.185 | MS1 | 121.4656742545 | 31.1446271095 | 119 | 152650 | -96.56 | 6.25 | 103.79 | 0.19 | 1.73 | 982 |
| 2024-09-20 22:21:35.884 | MS1 | 121.4656745823 | 31.1446243609 | 687 | 152650 | -92.95 | 7.99 | 91.52 | 0.13 | 1.57 | 984 |
| 2024-09-20 22:21:36.140 | MS1 | 121.4656646838 | 31.1446252840 | 636 | 152650 | -93.34 | 2.43 | 80.16 | 0.17 | 1.73 | 967 |
| 2024-09-20 22:21:37.850 | MS1 | 121.4656773781 | 31.1446225877 | 502 | 152650 | -96.89 | 5.67 | 63.26 | 0.06 | 2.00 | 937 |
| 2024-09-20 22:21:38.990 | MS1 | 121.4656586503 | 31.1446239330 | 119 | 152650 | -93.80 | 4.51 | 61.19 | 0.11 | 1.75 | 904 |
| 2024-09-20 22:21:39.559 | MS1 | 121.4656692717 | 31.1446281228 | 687 | 152650 | -96.06 | 6.08 | 108.23 | 0.20 | 1.75 | 912 |
| 2024-09-20 22:21:40.297 | MS1 | 121.4656774776 | 31.1446329169 | 636 | 152650 | -89.92 | 7.81 | 77.80 | 0.09 | 2.56 | 1564 |
| 2024-09-20 22:21:41.701 | MS1 | 121.4656608680 | 31.1446291954 | 502 | 152650 | -87.51 | 3.53 | 44.06 | 0.15 | 2.46 | 1566 |
| 2024-09-20 22:21:42.317 | MS1 | 121.4656617781 | 31.1446206068 | 119 | 152650 | -94.85 | 3.98 | 84.34 | 0.18 | 2.89 | 1587 |

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
| 3218837 | 13 | 121.4686945758 | 31.1545287713 | 258 | 9 | 7 | 15.0 | FDD | 636 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3219565 | 4 | 121.4647410799 | 31.1541686461 | 74 | 7 | 2 | 7.2 | TDD | 782 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3224446 | 3 | 121.4708823019 | 31.1536170275 | 323 | 13 | 2 | 3.3 | TDD | 616 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3226828 | 5 | 121.4700485671 | 31.1530000327 | 327 | 5 | 4 | 28.7 | TDD | 78 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3228613 | 7 | 121.4731056148 | 31.1514909284 | 115 | 10 | 1 | 24.3 | FDD | 939 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3248735 | 9 | 121.4673122923 | 31.1484436192 | 224 | 10 | 2 | 14.1 | FDD | 687 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3252423 | 12 | 121.4736264196 | 31.1449944163 | 78 | 1 | 12 | 7.4 | FDD | 119 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3252744 | 1 | 121.4695231252 | 31.1543411577 | 237 | 3 | 1 | 24.0 | TDD | 385 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3258279 | 11 | 121.4722308865 | 31.1529746599 | 291 | 14 | 9 | 17.8 | FDD | 502 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3267859 | 10 | 121.4708775504 | 31.1487734690 | 41 | 10 | 7 | 8.8 | FDD | 366 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3274293 | 8 | 121.4759460466 | 31.1451848841 | 180 | 10 | 10 | 13.4 | FDD | 174 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3275593 | 2 | 121.4686764488 | 31.1450476506 | 129 | 15 | 5 | 4.1 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3277712 | 6 | 121.4680154972 | 31.1447358635 | 263 | 2 | 8 | 11.2 | TDD | 316 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.136 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.155 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.295 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.295 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.018 | NREventA2 | measId:1;ServCellPCI:601;Se... |
| 2024-09-20 22:21:35.151 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.419 | NREventA5 | measId:3;ServCellPCI:601;Se... |
| 2024-09-20 22:21:35.459 | NRHandoverAttempt | SourcePCI:601;SourceNR-ARFC... |
| 2024-09-20 22:21:35.508 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.523 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.629 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.629 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252744 | 1 | 14.1954 | 17.4293 | -116.8487 | 5.5482 | 90.4916 | 0.0011 | 0.0073 |
| 2024_09_20 22:00 | 3275593 | 2 | 14.2052 | 14.8814 | -114.9497 | 7.9229 | 134.0170 | 0.0096 | 0.0114 |
| 2024_09_20 22:00 | 3224446 | 3 | 10.5900 | 14.3938 | -116.8502 | 12.8659 | 191.6522 | 0.0019 | 0.0182 |
| 2024_09_20 22:00 | 3219565 | 4 | 6.8210 | 14.9164 | -116.6687 | 8.6660 | 136.6845 | 0.0045 | 0.0133 |
| 2024_09_20 22:00 | 3226828 | 5 | 7.9901 | 10.1250 | -116.5678 | 12.7999 | 90.0324 | 0.0132 | 0.0190 |
| 2024_09_20 22:00 | 3277712 | 6 | 9.6796 | 6.0207 | -114.7567 | 9.7128 | 179.0610 | 0.0194 | 0.0101 |
| 2024_09_20 22:00 | 3228613 | 7 | 10.1770 | 12.5083 | -116.7816 | 3.8665 | 52.9224 | 0.0007 | 0.0072 |
| 2024_09_20 22:00 | 3274293 | 8 | 15.2989 | 19.5813 | -115.5360 | 4.3188 | 59.5714 | 0.0184 | 0.0057 |
| 2024_09_20 22:00 | 3248735 | 9 | 7.3087 | 5.2249 | -115.9019 | 3.8562 | 24.8976 | 0.0011 | 0.0160 |
| 2024_09_20 22:00 | 3267859 | 10 | 12.0277 | 10.2053 | -115.6731 | 3.0830 | 39.7255 | 0.0083 | 0.0137 |
| 2024_09_20 22:00 | 3258279 | 11 | 6.0865 | 7.5100 | -114.7538 | 4.7745 | 54.4107 | 0.0076 | 0.0190 |
| 2024_09_20 22:00 | 3252423 | 12 | 17.5336 | 9.5208 | -114.2240 | 4.1246 | 52.1341 | 0.0109 | 0.0056 |
| 2024_09_20 22:00 | 3218837 | 13 | 15.6373 | 18.9701 | -115.3401 | 3.6966 | 20.2985 | 0.0085 | 0.0102 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414952_E81ADFDB | 504990 | 782 | -95.9 | 504990 | 385 | -96.7 | 504990 | 616 | -103.1 | 504990 | 78 |
| MR_1774414952_BC27E7C9 | 152650 | 687 | -94.7 | 152650 | 174 | -95.8 | 152650 | 939 | -105.6 | 152650 | 366 |
| MR_1774414952_2CDCAF7D | 152650 | 687 | -91.9 | 152650 | 174 | -96.4 | 152650 | 939 | -104.5 | 152650 | 366 |
| MR_1774414952_D98D483A | 152650 | 687 | -92.4 | 152650 | 174 | -99.0 | 152650 | 939 | -105.5 | 152650 | 366 |
| MR_1774414952_5FDAA10C | 152650 | 687 | -91.5 | 152650 | 174 | -97.9 | 152650 | 939 | -104.5 | 152650 | 366 |
| MR_1774414952_6A1FD0AE | 152650 | 687 | -93.3 | 152650 | 174 | -98.1 | 152650 | 939 | -103.4 | 152650 | 366 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 21: `558e64d5-26a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `558e64d5-26af-4977-9551-8e1630686b19` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[21] topology](images/test_0021.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3267044_4 by 50 degrees
- `C2`: Lift the tilt angle of 3273385_1 by 9 degrees
- `C3`: Add neighbor relationship between 3273385_1 and 3267044_4
- `C4`: Decrease A3 Offset threshold for 3267044_4
- `C5`: Increase A3 Offset threshold for 3267044_4
- `C6`: Press down the tilt angle  of 3267044_4 by 10 degrees
- `C7`: Decrease transmission power for 3267044_4
- `C8`: Check test server and transmission issues
- `C9`: Increase transmission power for 3273385_1
- `C10`: Increase A3 Offset threshold for 3273385_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273385_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267044_4
- `C13`: Add neighbor relationship between 3210862_2 and 3267044_4
- `C14`: Decrease A3 Offset threshold for 3273385_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273385_1
- `C16`: Adjust the azimuth of 3273385_1 by 50 degrees
- `C17`: Increase transmission power for 3267044_4
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267044_4
- `C19`: Press down the tilt angle of 3273385_1 by 9 degrees
- `C20`: Lift the tilt angle  of 3267044_4 by 10 degrees
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease transmission power for 3273385_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.920 | MS1 | 121.4656580365 | 31.1446203082 | 537 | 504990 | -75.18 | 16.34 | 506.90 | 0.15 | 2.42 | 1567 |
| 2024-09-20 22:21:32.224 | MS1 | 121.4656737576 | 31.1446343234 | 537 | 504990 | -83.87 | 17.34 | 564.47 | 0.12 | 2.20 | 1563 |
| 2024-09-20 22:21:33.298 | MS1 | 121.4656629005 | 31.1446279056 | 537 | 504990 | -82.79 | 12.04 | 430.08 | 0.09 | 2.26 | 1579 |
| 2024-09-20 22:21:34.444 | MS1 | 121.4656723329 | 31.1446196375 | 537 | 504990 | -88.28 | -1.14 | 57.77 | 0.01 | 1.25 | 1583 |
| 2024-09-20 22:21:35.324 | MS1 | 121.4656640535 | 31.1446223664 | 537 | 504990 | -86.45 | -1.18 | 67.54 | 0.02 | 1.02 | 1571 |
| 2024-09-20 22:21:36.435 | MS1 | 121.4656587040 | 31.1446220858 | 537 | 504990 | -90.45 | -2.71 | 45.61 | 0.08 | 1.39 | 1592 |
| 2024-09-20 22:21:37.957 | MS1 | 121.4656716249 | 31.1446306174 | 537 | 504990 | -83.68 | -3.01 | 31.79 | 0.02 | 1.40 | 1571 |
| 2024-09-20 22:21:38.899 | MS1 | 121.4656698174 | 31.1446357547 | 537 | 504990 | -84.31 | -1.39 | 45.23 | 0.15 | 1.05 | 1565 |
| 2024-09-20 22:21:39.447 | MS1 | 121.4656758570 | 31.1446220154 | 222 | 504990 | -80.90 | 16.81 | 245.89 | 0.15 | 1.12 | 1580 |
| 2024-09-20 22:21:40.783 | MS1 | 121.4656649122 | 31.1446250757 | 222 | 504990 | -84.24 | 16.04 | 510.09 | 0.19 | 2.23 | 1588 |
| 2024-09-20 22:21:41.311 | MS1 | 121.4656679582 | 31.1446323126 | 222 | 504990 | -78.49 | 13.63 | 411.81 | 0.11 | 2.97 | 1579 |
| 2024-09-20 22:21:42.244 | MS1 | 121.4656654909 | 31.1446257941 | 222 | 504990 | -77.30 | 14.04 | 455.93 | 0.19 | 2.88 | 1579 |

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
| 3210862 | 2 | 121.4652218585 | 31.1476364854 | 32 | 10 | 5 | 26.0 | TDD | 890 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3249187 | 3 | 121.4738324926 | 31.1468203557 | 28 | 3 | 7 | 39.0 | TDD | 885 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3267044 | 4 | 121.4650120716 | 31.1474926656 | 229 | 3 | 8 | 39.1 | TDD | 222 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3273385 | 1 | 121.4644240420 | 31.1543649635 | 326 | 7 | 5 | 35.3 | TDD | 537 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.380 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.396 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.544 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.544 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.246 | NREventA3 | measId:2;ServCellPCI:204;Se... |
| 2024-09-20 22:21:38.486 | NRHandoverAttempt | SourcePCI:204;SourceNR-ARFC... |
| 2024-09-20 22:21:38.521 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.532 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.680 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.680 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273385 | 1 | 15.0667 | 18.0678 | -114.9279 | 13.2803 | 154.8066 | 0.0043 | 0.1236 |
| 2024_09_20 22:00 | 3210862 | 2 | 10.9089 | 14.5396 | -116.5699 | 15.4484 | 191.6450 | 0.0186 | 0.0104 |
| 2024_09_20 22:00 | 3249187 | 3 | 6.9322 | 6.5961 | -117.2147 | 9.0541 | 83.0477 | 0.0160 | 0.0149 |
| 2024_09_20 22:00 | 3267044 | 4 | 7.4179 | 13.5818 | -116.9770 | 6.6447 | 176.8504 | 0.0113 | 0.0095 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414832_D8F96575 | 504990 | 222 | -82.8 | 504990 | 537 | -87.7 | 504990 | 890 | -87.8 | 504990 | 885 |
| MR_1774414832_142AF665 | 504990 | 537 | -88.3 | 504990 | 222 | -83.6 | 504990 | 890 | -88.4 | 504990 | 885 |
| MR_1774414832_48C64EC4 | 504990 | 537 | -89.2 | 504990 | 222 | -85.3 | 504990 | 890 | -87.7 | 504990 | 885 |
| MR_1774414832_D2ED9984 | 504990 | 222 | -81.5 | 504990 | 537 | -88.8 | 504990 | 890 | -88.1 | 504990 | 885 |
| MR_1774414832_A3207DE4 | 504990 | 537 | -86.9 | 504990 | 222 | -82.5 | 504990 | 890 | -88.4 | 504990 | 885 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 22: `06b971d7-131...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `06b971d7-131a-4a2c-976f-a433d6f028cd` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[22] topology](images/test_0022.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215626_1
- `C2`: Decrease A3 Offset threshold for 3215626_1
- `C3`: Decrease transmission power for 3215626_1
- `C4`: Lift the tilt angle of 3234507_3 by 5 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215626_1
- `C6`: Add neighbor relationship between 3234507_3 and 3215626_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234507_3
- `C8`: Press down the tilt angle  of 3215626_1 by 8 degrees
- `C9`: Add neighbor relationship between 3231015_4 and 3215626_1
- `C10`: Check test server and transmission issues
- `C11`: Decrease transmission power for 3234507_3
- `C12`: Decrease A3 Offset threshold for 3234507_3
- `C13`: Increase A3 Offset threshold for 3215626_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234507_3
- `C15`: Increase transmission power for 3234507_3
- `C16`: Press down the tilt angle of 3234507_3 by 5 degrees
- `C17`: Adjust the azimuth of 3215626_1 by 2 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Increase A3 Offset threshold for 3234507_3
- `C20`: Increase transmission power for 3215626_1
- `C21`: Adjust the azimuth of 3234507_3 by 50 degrees
- `C22`: Lift the tilt angle  of 3215626_1 by 8 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.818 | MS1 | 121.4656600984 | 31.1446378509 | 174 | 504990 | -86.24 | 17.70 | 523.83 | 0.10 | 2.73 | 1581 |
| 2024-09-20 22:21:32.297 | MS1 | 121.4656774730 | 31.1446347139 | 174 | 504990 | -91.05 | 14.04 | 379.25 | 0.16 | 2.20 | 1577 |
| 2024-09-20 22:21:33.176 | MS1 | 121.4656662164 | 31.1446328986 | 174 | 504990 | -86.78 | 14.78 | 327.98 | 0.11 | 2.66 | 1577 |
| 2024-09-20 22:21:34.748 | MS1 | 121.4656716563 | 31.1446377874 | 174 | 504990 | -88.49 | 13.82 | 55.04 | 0.13 | 2.36 | 1560 |
| 2024-09-20 22:21:35.508 | MS1 | 121.4656618896 | 31.1446316702 | 174 | 504990 | -86.06 | 14.65 | 71.18 | 0.09 | 2.39 | 1589 |
| 2024-09-20 22:21:36.512 | MS1 | 121.4656725997 | 31.1446371211 | 174 | 504990 | -89.03 | 13.21 | 68.43 | 0.00 | 2.12 | 1591 |
| 2024-09-20 22:21:37.868 | MS1 | 121.4656592302 | 31.1446225326 | 174 | 504990 | -91.81 | 11.12 | 49.44 | 0.19 | 2.52 | 1568 |
| 2024-09-20 22:21:38.512 | MS1 | 121.4656711266 | 31.1446277340 | 174 | 504990 | -92.44 | 7.08 | 100.90 | 0.18 | 2.72 | 1561 |
| 2024-09-20 22:21:39.405 | MS1 | 121.4656709670 | 31.1446373099 | 174 | 504990 | -89.40 | 9.31 | 75.87 | 0.13 | 2.04 | 1572 |
| 2024-09-20 22:21:40.319 | MS1 | 121.4656665016 | 31.1446292491 | 174 | 504990 | -91.27 | 12.35 | 447.05 | 0.18 | 2.05 | 1579 |
| 2024-09-20 22:21:41.387 | MS1 | 121.4656634837 | 31.1446235234 | 174 | 504990 | -91.10 | 10.00 | 572.56 | 0.07 | 2.13 | 1586 |
| 2024-09-20 22:21:42.728 | MS1 | 121.4656719461 | 31.1446185746 | 174 | 504990 | -89.91 | 9.51 | 499.17 | 0.15 | 2.54 | 1582 |

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
| 3215626 | 1 | 121.4657076615 | 31.1473622799 | 183 | 3 | 11 | 28.5 | TDD | 648 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3231015 | 4 | 121.4647230647 | 31.1511215522 | 327 | 12 | 6 | 17.7 | TDD | 287 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3234507 | 3 | 121.4649811388 | 31.1501610924 | 235 | 1 | 8 | 47.2 | TDD | 174 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3240612 | 2 | 121.4677669361 | 31.1559104368 | 312 | 12 | 4 | 16.6 | TDD | 706 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.864 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.880 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.015 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.015 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.732 | NREventA3 | measId:2;ServCellPCI:845;Se... |
| 2024-09-20 22:21:37.972 | NRHandoverAttempt | SourcePCI:845;SourceNR-ARFC... |
| 2024-09-20 22:21:38.008 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.019 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.150 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.150 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3215626 | 1 | 83.3136 | 93.2745 | -117.6960 | 7.7961 | 177.0442 | 0.0128 | 0.0052 |
| 2024_09_19 22:00 | 3240612 | 2 | 83.2710 | 89.8707 | -117.0229 | 9.8355 | 170.6291 | 0.0038 | 0.0140 |
| 2024_09_19 22:00 | 3234507 | 3 | 80.4179 | 88.8493 | -114.5203 | 9.0321 | 103.7182 | 0.0118 | 0.0093 |
| 2024_09_19 22:00 | 3231015 | 4 | 89.3753 | 94.8361 | -117.7357 | 9.9401 | 91.1495 | 0.0033 | 0.0049 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415976_BE006AF8 | 504990 | 174 | -86.9 | 504990 | 648 | -90.5 | 504990 | 287 | -99.4 | 504990 | 706 |
| MR_1774415976_D9446958 | 504990 | 174 | -90.4 | 504990 | 648 | -91.7 | 504990 | 287 | -99.6 | 504990 | 706 |
| MR_1774415976_B9FD62E6 | 504990 | 174 | -89.1 | 504990 | 648 | -89.8 | 504990 | 287 | -101.6 | 504990 | 706 |
| MR_1774415976_F8922487 | 504990 | 174 | -86.6 | 504990 | 648 | -90.5 | 504990 | 287 | -99.0 | 504990 | 706 |
| MR_1774415976_F8A6890C | 504990 | 174 | -89.6 | 504990 | 648 | -88.9 | 504990 | 287 | -101.7 | 504990 | 706 |
| MR_1774415976_81A700D7 | 504990 | 174 | -89.1 | 504990 | 648 | -88.7 | 504990 | 287 | -99.5 | 504990 | 706 |
| MR_1774415976_890D30E5 | 504990 | 174 | -90.4 | 504990 | 648 | -90.4 | 504990 | 287 | -99.6 | 504990 | 706 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 23: `28312271-c54...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `28312271-c54b-4840-8596-5645346e0ba7` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[23] topology](images/test_0023.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242508_1
- `C2`: Decrease A3 Offset threshold for 3252524_2
- `C3`: Add neighbor relationship between 3252524_2 and 3242508_1
- `C4`: Press down the tilt angle of 3252524_2 by 5 degrees
- `C5`: Lift the tilt angle of 3252524_2 by 5 degrees
- `C6`: Decrease A3 Offset threshold for 3242508_1
- `C7`: Decrease transmission power for 3252524_2
- `C8`: Check test server and transmission issues
- `C9`: Adjust the azimuth of 3242508_1 by 50 degrees
- `C10`: Increase A3 Offset threshold for 3252524_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252524_2
- `C12`: Add neighbor relationship between 3263093_4 and 3242508_1
- `C13`: Increase A3 Offset threshold for 3242508_1
- `C14`: Adjust the azimuth of 3252524_2 by 50 degrees
- `C15`: Decrease transmission power for 3242508_1
- `C16`: Lift the tilt angle  of 3242508_1 by 10 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242508_1
- `C18`: Increase transmission power for 3252524_2
- `C19`: Press down the tilt angle  of 3242508_1 by 10 degrees
- `C20`: Increase transmission power for 3242508_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252524_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.957 | MS1 | 121.4656622135 | 31.1446237411 | 301 | 504990 | -91.80 | 14.72 | 454.84 | 0.05 | 2.93 | 1589 |
| 2024-09-20 22:21:32.464 | MS1 | 121.4656614447 | 31.1446313554 | 301 | 504990 | -89.38 | 13.75 | 457.28 | 0.04 | 2.79 | 1568 |
| 2024-09-20 22:21:33.668 | MS1 | 121.4656719915 | 31.1446312662 | 301 | 504990 | -89.13 | 13.97 | 569.09 | 0.06 | 2.22 | 1571 |
| 2024-09-20 22:21:34.483 | MS1 | 121.4656602532 | 31.1446223052 | 301 | 504990 | -86.97 | 17.41 | 79.81 | 0.15 | 2.92 | 408 |
| 2024-09-20 22:21:35.496 | MS1 | 121.4656641438 | 31.1446299250 | 301 | 504990 | -89.88 | 16.91 | 50.63 | 0.19 | 2.03 | 309 |
| 2024-09-20 22:21:36.729 | MS1 | 121.4656718112 | 31.1446300916 | 301 | 504990 | -89.73 | 13.55 | 87.23 | 0.09 | 2.92 | 425 |
| 2024-09-20 22:21:37.546 | MS1 | 121.4656641059 | 31.1446272672 | 301 | 504990 | -89.44 | 7.85 | 84.71 | 0.13 | 2.67 | 418 |
| 2024-09-20 22:21:38.933 | MS1 | 121.4656750696 | 31.1446281222 | 301 | 504990 | -91.60 | 11.42 | 84.33 | 0.01 | 2.88 | 496 |
| 2024-09-20 22:21:39.968 | MS1 | 121.4656768778 | 31.1446358714 | 301 | 504990 | -93.69 | 9.98 | 74.28 | 0.06 | 2.73 | 309 |
| 2024-09-20 22:21:40.478 | MS1 | 121.4656648792 | 31.1446230597 | 301 | 504990 | -91.26 | 9.23 | 388.44 | 0.02 | 2.19 | 1583 |
| 2024-09-20 22:21:41.216 | MS1 | 121.4656732883 | 31.1446181868 | 301 | 504990 | -90.67 | 10.86 | 351.93 | 0.09 | 2.66 | 1561 |
| 2024-09-20 22:21:42.658 | MS1 | 121.4656597794 | 31.1446224250 | 301 | 504990 | -89.98 | 9.27 | 350.46 | 0.12 | 2.48 | 1573 |

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
| 3216417 | 3 | 121.4756691309 | 31.1555554770 | 66 | 9 | 5 | 35.0 | TDD | 685 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3242508 | 1 | 121.4738331834 | 31.1559342400 | 270 | 13 | 12 | 19.7 | TDD | 306 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3252524 | 2 | 121.4685820003 | 31.1472578863 | 27 | 1 | 12 | 25.0 | TDD | 301 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3263093 | 4 | 121.4746791077 | 31.1547650508 | 214 | 4 | 8 | 28.5 | TDD | 143 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.800 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.817 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.928 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.928 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.661 | NREventA3 | measId:2;ServCellPCI:553;Se... |
| 2024-09-20 22:21:37.901 | NRHandoverAttempt | SourcePCI:553;SourceNR-ARFC... |
| 2024-09-20 22:21:37.936 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.948 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.086 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.086 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242508 | 1 | 17.1057 | 6.0064 | -116.8664 | 8.6971 | 181.6515 | 0.0190 | 0.0003 |
| 2024_09_20 22:00 | 3252524 | 2 | 10.5309 | 7.1690 | -117.8525 | 13.1674 | 113.6226 | 0.0129 | 0.0189 |
| 2024_09_20 22:00 | 3216417 | 3 | 12.7750 | 13.3158 | -117.1206 | 8.4996 | 142.2168 | 0.0137 | 0.0035 |
| 2024_09_20 22:00 | 3263093 | 4 | 19.3597 | 10.0720 | -115.8444 | 11.8545 | 86.6879 | 0.0167 | 0.0045 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415787_7E86AADA | 504990 | 301 | -86.1 | 504990 | 306 | -92.3 | 504990 | 143 | -94.6 | 504990 | 685 |
| MR_1774415787_CF24DC04 | 504990 | 301 | -86.3 | 504990 | 306 | -94.0 | 504990 | 143 | -92.9 | 504990 | 685 |
| MR_1774415787_81A99D82 | 504990 | 301 | -87.0 | 504990 | 306 | -93.7 | 504990 | 143 | -94.7 | 504990 | 685 |
| MR_1774415787_1976AA3E | 504990 | 301 | -86.1 | 504990 | 306 | -95.0 | 504990 | 143 | -95.8 | 504990 | 685 |
| MR_1774415787_47E3E3EE | 504990 | 301 | -88.8 | 504990 | 306 | -95.0 | 504990 | 143 | -93.7 | 504990 | 685 |
| MR_1774415787_72067496 | 504990 | 301 | -85.9 | 504990 | 306 | -93.2 | 504990 | 143 | -92.7 | 504990 | 685 |
| MR_1774415787_9E8E8554 | 504990 | 301 | -86.7 | 504990 | 306 | -95.1 | 504990 | 143 | -95.2 | 504990 | 685 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 24: `aa431504-d22...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `aa431504-d22a-44dc-b539-c364985b6f75` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[24] topology](images/test_0024.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3260286_2 by 10 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233423_3
- `C3`: Adjust the azimuth of 3260286_2 by 50 degrees
- `C4`: Increase transmission power for 3260286_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260286_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233423_3
- `C7`: Decrease transmission power for 3260286_2
- `C8`: Decrease A3 Offset threshold for 3233423_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260286_2
- `C10`: Press down the tilt angle  of 3233423_3 by 7 degrees
- `C11`: Add neighbor relationship between 3246187_4 and 3233423_3
- `C12`: Add neighbor relationship between 3260286_2 and 3233423_3
- `C13`: Check test server and transmission issues
- `C14`: Decrease A3 Offset threshold for 3260286_2
- `C15`: Increase A3 Offset threshold for 3233423_3
- `C16`: Decrease transmission power for 3233423_3
- `C17`: Press down the tilt angle of 3260286_2 by 10 degrees
- `C18`: Increase A3 Offset threshold for 3260286_2
- `C19`: Adjust the azimuth of 3233423_3 by 50 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase transmission power for 3233423_3
- `C22`: Lift the tilt angle  of 3233423_3 by 7 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.897 | MS1 | 121.4656777780 | 31.1446264440 | 820 | 504990 | -87.18 | 16.58 | 480.24 | 0.17 | 2.77 | 1597 |
| 2024-09-20 22:21:32.347 | MS1 | 121.4656727024 | 31.1446289457 | 820 | 504990 | -85.62 | 13.59 | 318.94 | 0.16 | 2.18 | 1570 |
| 2024-09-20 22:21:33.907 | MS1 | 121.4656613330 | 31.1446186455 | 820 | 504990 | -91.00 | 12.11 | 579.68 | 0.03 | 2.97 | 1600 |
| 2024-09-20 22:21:34.606 | MS1 | 121.4656751335 | 31.1446254076 | 820 | 504990 | -85.82 | 12.96 | 71.84 | 0.15 | 2.09 | 1589 |
| 2024-09-20 22:21:35.366 | MS1 | 121.4656707812 | 31.1446204772 | 820 | 504990 | -88.53 | 12.62 | 92.97 | 0.15 | 2.67 | 1569 |
| 2024-09-20 22:21:36.442 | MS1 | 121.4656602395 | 31.1446232333 | 820 | 504990 | -88.34 | 12.78 | 77.29 | 0.16 | 2.28 | 1567 |
| 2024-09-20 22:21:37.644 | MS1 | 121.4656584312 | 31.1446378707 | 820 | 504990 | -90.36 | 9.89 | 56.70 | 0.16 | 2.12 | 1595 |
| 2024-09-20 22:21:38.774 | MS1 | 121.4656626749 | 31.1446301266 | 820 | 504990 | -91.04 | 7.27 | 87.74 | 0.20 | 2.99 | 1566 |
| 2024-09-20 22:21:39.819 | MS1 | 121.4656750313 | 31.1446201917 | 820 | 504990 | -92.56 | 8.04 | 103.58 | 0.14 | 2.41 | 1576 |
| 2024-09-20 22:21:40.864 | MS1 | 121.4656617219 | 31.1446347853 | 820 | 504990 | -92.61 | 9.92 | 306.51 | 0.19 | 2.90 | 1594 |
| 2024-09-20 22:21:41.433 | MS1 | 121.4656714856 | 31.1446344811 | 820 | 504990 | -91.51 | 11.82 | 389.53 | 0.13 | 2.44 | 1595 |
| 2024-09-20 22:21:42.899 | MS1 | 121.4656693960 | 31.1446229885 | 820 | 504990 | -92.67 | 10.22 | 480.48 | 0.02 | 2.10 | 1576 |

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
| 3233423 | 3 | 121.4756224048 | 31.1531939399 | 60 | 6 | 0 | 20.6 | TDD | 957 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3246187 | 4 | 121.4676615970 | 31.1499095668 | 149 | 12 | 6 | 17.7 | TDD | 303 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3260286 | 2 | 121.4694919956 | 31.1469129786 | 154 | 6 | 1 | 34.3 | TDD | 820 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3278249 | 1 | 121.4660221089 | 31.1534249454 | 107 | 8 | 6 | 36.0 | TDD | 586 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.552 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.575 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.679 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.679 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.444 | NREventA3 | measId:2;ServCellPCI:156;Se... |
| 2024-09-20 22:21:38.684 | NRHandoverAttempt | SourcePCI:156;SourceNR-ARFC... |
| 2024-09-20 22:21:38.724 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.738 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.867 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.867 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3278249 | 1 | 93.0359 | 83.2540 | -116.7288 | 14.2054 | 162.2633 | 0.0173 | 0.0121 |
| 2024_09_19 22:00 | 3260286 | 2 | 82.4160 | 93.8845 | -116.0658 | 11.0842 | 115.7881 | 0.0091 | 0.0112 |
| 2024_09_19 22:00 | 3233423 | 3 | 79.4995 | 92.0014 | -116.8918 | 13.6005 | 97.9306 | 0.0032 | 0.0071 |
| 2024_09_19 22:00 | 3246187 | 4 | 83.3239 | 85.4727 | -117.4872 | 19.7449 | 129.6883 | 0.0072 | 0.0030 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412186_6C14D621 | 504990 | 820 | -84.0 | 504990 | 957 | -85.4 | 504990 | 303 | -97.1 | 504990 | 586 |
| MR_1774412186_2029E86F | 504990 | 820 | -85.8 | 504990 | 957 | -84.8 | 504990 | 303 | -99.3 | 504990 | 586 |
| MR_1774412186_8BBACC85 | 504990 | 820 | -84.9 | 504990 | 957 | -88.1 | 504990 | 303 | -97.9 | 504990 | 586 |
| MR_1774412186_74F6D85A | 504990 | 820 | -87.8 | 504990 | 957 | -85.0 | 504990 | 303 | -100.5 | 504990 | 586 |
| MR_1774412186_37E7F0EC | 504990 | 820 | -86.7 | 504990 | 957 | -85.7 | 504990 | 303 | -100.0 | 504990 | 586 |
| MR_1774412186_351DAFFA | 504990 | 820 | -87.2 | 504990 | 957 | -85.8 | 504990 | 303 | -99.8 | 504990 | 586 |
| MR_1774412186_EE40E008 | 504990 | 820 | -84.9 | 504990 | 957 | -88.2 | 504990 | 303 | -98.4 | 504990 | 586 |
| MR_1774412186_A389729D | 504990 | 820 | -83.9 | 504990 | 957 | -86.4 | 504990 | 303 | -99.9 | 504990 | 586 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 25: `8ed1021f-abd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8ed1021f-abd2-4fdb-9a4e-b0b6a4869c11` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[25] topology](images/test_0025.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3258213_2 by 12 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258213_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251904_6
- `C4`: Decrease A3 Offset threshold for 3251904_6
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Adjust the azimuth of 3251904_6 by 14 degrees
- `C7`: Press down the tilt angle of 3258213_2 by 5 degrees
- `C8`: Lift the tilt angle of 3258213_2 by 5 degrees
- `C9`: Lift the tilt angle  of 3251904_6 by 1 degrees
- `C10`: Decrease transmission power for 3251904_6
- `C11`: Increase A3 Offset threshold for 3258213_2
- `C12`: Decrease transmission power for 3258213_2
- `C13`: Add neighbor relationship between 3258213_2 and 3251904_6
- `C14`: Press down the tilt angle  of 3251904_6 by 1 degrees
- `C15`: Check test server and transmission issues
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258213_2
- `C17`: Decrease A3 Offset threshold for 3258213_2
- `C18`: Increase A3 Offset threshold for 3251904_6
- `C19`: Increase transmission power for 3258213_2
- `C20`: Add neighbor relationship between 3227563_11 and 3251904_6
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251904_6
- `C22`: Increase transmission power for 3251904_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.502 | MS1 | 121.4656646579 | 31.1446351532 | 164 | 504990 | -94.41 | 12.68 | 457.82 | 0.07 | 2.65 | 1562 |
| 2024-09-20 22:21:32.891 | MS1 | 121.4656736551 | 31.1446318650 | 224 | 504990 | -94.08 | 12.19 | 406.47 | 0.04 | 2.35 | 1594 |
| 2024-09-20 22:21:33.310 | MS1 | 121.4656616214 | 31.1446328883 | 391 | 504990 | -95.08 | 9.46 | 590.06 | 0.11 | 2.41 | 1597 |
| 2024-09-20 22:21:34.941 | MS1 | 121.4656615642 | 31.1446195929 | 828 | 152650 | -88.30 | 2.12 | 65.73 | 0.15 | 1.96 | 953 |
| 2024-09-20 22:21:35.903 | MS1 | 121.4656593686 | 31.1446351028 | 9 | 152650 | -96.07 | 5.57 | 57.12 | 0.20 | 1.52 | 979 |
| 2024-09-20 22:21:36.903 | MS1 | 121.4656659588 | 31.1446202655 | 113 | 152650 | -89.52 | 2.68 | 75.99 | 0.14 | 1.60 | 970 |
| 2024-09-20 22:21:37.435 | MS1 | 121.4656698065 | 31.1446369950 | 885 | 152650 | -93.31 | 2.87 | 88.64 | 0.14 | 1.65 | 998 |
| 2024-09-20 22:21:38.806 | MS1 | 121.4656708328 | 31.1446366663 | 828 | 152650 | -92.55 | 5.37 | 86.90 | 0.09 | 1.95 | 969 |
| 2024-09-20 22:21:39.878 | MS1 | 121.4656678414 | 31.1446374544 | 9 | 152650 | -87.11 | 7.69 | 82.74 | 0.01 | 1.64 | 988 |
| 2024-09-20 22:21:40.186 | MS1 | 121.4656749134 | 31.1446368475 | 113 | 152650 | -88.92 | 5.82 | 65.28 | 0.00 | 2.26 | 1584 |
| 2024-09-20 22:21:41.202 | MS1 | 121.4656696020 | 31.1446247040 | 885 | 152650 | -96.11 | 4.19 | 59.32 | 0.04 | 2.93 | 1594 |
| 2024-09-20 22:21:42.599 | MS1 | 121.4656664736 | 31.1446298781 | 828 | 152650 | -89.66 | 4.62 | 54.21 | 0.19 | 2.88 | 1591 |

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
| 3219918 | 8 | 121.4758082122 | 31.1518012606 | 141 | 7 | 5 | 15.5 | FDD | 871 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3221027 | 9 | 121.4713441428 | 31.1482494550 | 125 | 3 | 2 | 4.9 | FDD | 9 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3227563 | 11 | 121.4741425851 | 31.1553786023 | 310 | 14 | 5 | 11.8 | FDD | 113 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3235380 | 13 | 121.4719033868 | 31.1509426486 | 174 | 9 | 12 | 17.0 | FDD | 828 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3237866 | 7 | 121.4703469996 | 31.1528073713 | 155 | 5 | 6 | 12.9 | FDD | 320 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3251904 | 6 | 121.4663876997 | 31.1491778126 | 202 | 1 | 11 | 2.9 | TDD | 26 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3252077 | 10 | 121.4758677036 | 31.1546047452 | 324 | 1 | 9 | 2.5 | FDD | 169 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3257441 | 5 | 121.4704305377 | 31.1481752164 | 113 | 4 | 10 | 30.0 | TDD | 658 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3257918 | 12 | 121.4665917477 | 31.1460887300 | 163 | 12 | 6 | 16.3 | FDD | 885 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3258213 | 2 | 121.4648109103 | 31.1483510010 | 157 | 4 | 9 | 4.5 | TDD | 164 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3258882 | 4 | 121.4687701506 | 31.1492310836 | 157 | 5 | 4 | 0.4 | TDD | 391 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3269905 | 3 | 121.4754973332 | 31.1521334420 | 230 | 15 | 9 | 23.4 | TDD | 838 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3271144 | 1 | 121.4721569629 | 31.1472210587 | 136 | 11 | 4 | 1.3 | TDD | 224 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.121 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.146 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.278 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.278 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.944 | NREventA2 | measId:1;ServCellPCI:52;Ser... |
| 2024-09-20 22:21:35.049 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.255 | NREventA5 | measId:3;ServCellPCI:52;Ser... |
| 2024-09-20 22:21:35.326 | NRHandoverAttempt | SourcePCI:52;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.359 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.374 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.521 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.521 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271144 | 1 | 5.2488 | 18.0934 | -115.1990 | 14.6498 | 128.3882 | 0.0033 | 0.0013 |
| 2024_09_20 22:00 | 3258213 | 2 | 7.4148 | 18.9230 | -114.5736 | 10.7960 | 92.5940 | 0.0194 | 0.0100 |
| 2024_09_20 22:00 | 3269905 | 3 | 19.1078 | 18.0980 | -115.8559 | 7.7784 | 155.8122 | 0.0153 | 0.0005 |
| 2024_09_20 22:00 | 3258882 | 4 | 18.6465 | 13.2062 | -115.8368 | 9.8019 | 87.4187 | 0.0049 | 0.0146 |
| 2024_09_20 22:00 | 3257441 | 5 | 16.2555 | 6.5834 | -114.7069 | 13.1501 | 194.4238 | 0.0106 | 0.0057 |
| 2024_09_20 22:00 | 3251904 | 6 | 11.5027 | 7.3839 | -117.8072 | 11.5444 | 94.9884 | 0.0128 | 0.0193 |
| 2024_09_20 22:00 | 3237866 | 7 | 6.7223 | 12.9210 | -117.6148 | 4.0188 | 42.8054 | 0.0110 | 0.0184 |
| 2024_09_20 22:00 | 3219918 | 8 | 8.5688 | 7.9215 | -117.4817 | 3.1772 | 35.0117 | 0.0060 | 0.0062 |
| 2024_09_20 22:00 | 3221027 | 9 | 10.4797 | 14.6849 | -116.7427 | 3.5977 | 55.5461 | 0.0000 | 0.0182 |
| 2024_09_20 22:00 | 3252077 | 10 | 15.6564 | 10.2191 | -114.4620 | 4.6285 | 53.9165 | 0.0018 | 0.0028 |
| 2024_09_20 22:00 | 3227563 | 11 | 11.3936 | 5.6885 | -117.3827 | 3.9479 | 20.2663 | 0.0054 | 0.0154 |
| 2024_09_20 22:00 | 3257918 | 12 | 6.9781 | 16.3601 | -117.5408 | 3.0777 | 44.6923 | 0.0005 | 0.0000 |
| 2024_09_20 22:00 | 3235380 | 13 | 12.2493 | 10.7841 | -116.0410 | 4.7786 | 53.4745 | 0.0084 | 0.0010 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412327_4D580DE9 | 504990 | 391 | -96.4 | 504990 | 26 | -93.2 | 504990 | 658 | -97.0 | 504990 | 838 |
| MR_1774412327_2992DA5F | 152650 | 828 | -89.0 | 152650 | 320 | -91.9 | 152650 | 871 | -96.6 | 152650 | 169 |
| MR_1774412327_9951DE9A | 504990 | 391 | -93.2 | 504990 | 26 | -93.3 | 504990 | 658 | -98.8 | 504990 | 838 |
| MR_1774412327_78215D6B | 504990 | 391 | -95.0 | 504990 | 26 | -94.1 | 504990 | 658 | -97.4 | 504990 | 838 |
| MR_1774412327_3DA89693 | 504990 | 391 | -95.2 | 504990 | 26 | -93.1 | 504990 | 658 | -98.7 | 504990 | 838 |
| MR_1774412327_4946B7E3 | 504990 | 391 | -93.3 | 504990 | 26 | -91.0 | 504990 | 658 | -96.4 | 504990 | 838 |
| MR_1774412327_E831E3F3 | 152650 | 828 | -86.4 | 152650 | 320 | -93.5 | 152650 | 871 | -94.8 | 152650 | 169 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 26: `be3d8972-47e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `be3d8972-47e7-4f0a-8979-e1fe1d272212` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[26] topology](images/test_0026.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3224649_6 by 4 degrees
- `C2`: Decrease transmission power for 3224649_6
- `C3`: Increase transmission power for 3211720_3
- `C4`: Decrease A3 Offset threshold for 3224649_6
- `C5`: Increase transmission power for 3224649_6
- `C6`: Adjust the azimuth of 3211720_3 by 16 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211720_3
- `C8`: Decrease A3 Offset threshold for 3211720_3
- `C9`: Add neighbor relationship between 3211720_3 and 3224649_6
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211720_3
- `C11`: Adjust the azimuth of 3224649_6 by 34 degrees
- `C12`: Decrease transmission power for 3211720_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224649_6
- `C14`: Check test server and transmission issues
- `C15`: Increase A3 Offset threshold for 3224649_6
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224649_6
- `C17`: Add neighbor relationship between 3244524_10 and 3224649_6
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Lift the tilt angle of 3211720_3 by 3 degrees
- `C20`: Increase A3 Offset threshold for 3211720_3
- `C21`: Press down the tilt angle of 3211720_3 by 3 degrees
- `C22`: Press down the tilt angle  of 3224649_6 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.144 | MS1 | 121.4656752043 | 31.1446291412 | 588 | 504990 | -95.96 | 12.55 | 506.66 | 0.02 | 2.71 | 1598 |
| 2024-09-20 22:21:32.153 | MS1 | 121.4656642427 | 31.1446269996 | 68 | 504990 | -93.34 | 13.54 | 571.28 | 0.18 | 2.18 | 1563 |
| 2024-09-20 22:21:33.707 | MS1 | 121.4656768702 | 31.1446348977 | 687 | 504990 | -95.51 | 10.05 | 574.13 | 0.14 | 2.72 | 1596 |
| 2024-09-20 22:21:34.443 | MS1 | 121.4656667395 | 31.1446330714 | 413 | 152650 | -91.63 | 4.32 | 86.11 | 0.03 | 1.51 | 926 |
| 2024-09-20 22:21:35.924 | MS1 | 121.4656679453 | 31.1446321308 | 284 | 152650 | -95.27 | 5.85 | 78.46 | 0.08 | 1.54 | 963 |
| 2024-09-20 22:21:36.799 | MS1 | 121.4656727665 | 31.1446181188 | 917 | 152650 | -92.01 | 6.28 | 78.62 | 0.12 | 1.66 | 952 |
| 2024-09-20 22:21:37.756 | MS1 | 121.4656588738 | 31.1446279732 | 619 | 152650 | -94.97 | 3.42 | 64.74 | 0.03 | 2.00 | 918 |
| 2024-09-20 22:21:38.123 | MS1 | 121.4656772273 | 31.1446353832 | 413 | 152650 | -91.60 | 2.28 | 54.76 | 0.08 | 1.98 | 973 |
| 2024-09-20 22:21:39.918 | MS1 | 121.4656630194 | 31.1446196244 | 284 | 152650 | -96.52 | 7.10 | 77.97 | 0.18 | 1.64 | 948 |
| 2024-09-20 22:21:40.911 | MS1 | 121.4656752600 | 31.1446370127 | 917 | 152650 | -93.65 | 2.22 | 96.72 | 0.08 | 2.81 | 1565 |
| 2024-09-20 22:21:41.887 | MS1 | 121.4656713716 | 31.1446350539 | 619 | 152650 | -95.04 | 3.29 | 83.58 | 0.15 | 2.50 | 1577 |
| 2024-09-20 22:21:42.961 | MS1 | 121.4656746625 | 31.1446224330 | 413 | 152650 | -89.13 | 5.96 | 58.02 | 0.01 | 2.12 | 1598 |

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
| 3211720 | 3 | 121.4739866546 | 31.1504837524 | 215 | 2 | 7 | 25.3 | TDD | 588 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3212784 | 11 | 121.4711678941 | 31.1454315846 | 241 | 4 | 8 | 16.7 | FDD | 251 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3218932 | 5 | 121.4686424185 | 31.1506556120 | 210 | 10 | 6 | 18.7 | TDD | 687 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3224649 | 6 | 121.4748916046 | 31.1464673988 | 291 | 4 | 7 | 3.2 | TDD | 473 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3224944 | 7 | 121.4755564435 | 31.1558018672 | 341 | 15 | 9 | 8.0 | FDD | 962 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3237597 | 9 | 121.4758835547 | 31.1462980395 | 40 | 5 | 5 | 27.6 | FDD | 525 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3244524 | 10 | 121.4709584400 | 31.1527983838 | 305 | 12 | 7 | 5.5 | FDD | 917 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3246001 | 13 | 121.4750586965 | 31.1510353567 | 33 | 4 | 5 | 1.1 | FDD | 413 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3251327 | 12 | 121.4679036555 | 31.1475733716 | 42 | 7 | 2 | 6.0 | FDD | 284 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3258100 | 2 | 121.4727816524 | 31.1517949093 | 229 | 15 | 2 | 19.5 | TDD | 68 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3258677 | 1 | 121.4681526674 | 31.1472100191 | 185 | 8 | 11 | 15.6 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3264781 | 4 | 121.4689293537 | 31.1547102144 | 30 | 15 | 9 | 17.8 | TDD | 492 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3279078 | 8 | 121.4665208099 | 31.1515102732 | 266 | 1 | 7 | 14.4 | FDD | 619 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |

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
| 2024-09-20 22:21:31.325 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.341 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.453 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.453 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.160 | NREventA2 | measId:1;ServCellPCI:594;Se... |
| 2024-09-20 22:21:35.270 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.561 | NREventA5 | measId:3;ServCellPCI:594;Se... |
| 2024-09-20 22:21:35.594 | NRHandoverAttempt | SourcePCI:594;SourceNR-ARFC... |
| 2024-09-20 22:21:35.625 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.636 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.763 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.763 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258677 | 1 | 12.5564 | 6.3814 | -116.3090 | 19.3973 | 136.1224 | 0.0104 | 0.0057 |
| 2024_09_20 22:00 | 3258100 | 2 | 17.9065 | 11.1484 | -115.9311 | 17.3248 | 81.1705 | 0.0067 | 0.0000 |
| 2024_09_20 22:00 | 3211720 | 3 | 18.8970 | 6.3904 | -114.6374 | 5.4699 | 157.1763 | 0.0192 | 0.0176 |
| 2024_09_20 22:00 | 3264781 | 4 | 7.6961 | 19.0967 | -117.5300 | 9.1652 | 84.7972 | 0.0148 | 0.0180 |
| 2024_09_20 22:00 | 3218932 | 5 | 5.6623 | 5.3159 | -116.5239 | 16.5496 | 123.2609 | 0.0007 | 0.0126 |
| 2024_09_20 22:00 | 3224649 | 6 | 15.7251 | 14.1174 | -116.8666 | 16.1136 | 143.9398 | 0.0127 | 0.0032 |
| 2024_09_20 22:00 | 3224944 | 7 | 18.7279 | 6.6296 | -116.1897 | 4.8496 | 29.2647 | 0.0068 | 0.0144 |
| 2024_09_20 22:00 | 3279078 | 8 | 11.9878 | 16.0403 | -117.0755 | 4.8878 | 43.0205 | 0.0093 | 0.0110 |
| 2024_09_20 22:00 | 3237597 | 9 | 9.8417 | 16.7327 | -116.0579 | 3.1879 | 34.9109 | 0.0177 | 0.0196 |
| 2024_09_20 22:00 | 3244524 | 10 | 10.0095 | 13.2899 | -115.6794 | 3.8014 | 46.7406 | 0.0057 | 0.0193 |
| 2024_09_20 22:00 | 3212784 | 11 | 5.7178 | 13.1873 | -116.9696 | 3.2700 | 57.7044 | 0.0137 | 0.0059 |
| 2024_09_20 22:00 | 3251327 | 12 | 11.2328 | 18.5056 | -117.0541 | 4.5694 | 55.2664 | 0.0159 | 0.0148 |
| 2024_09_20 22:00 | 3246001 | 13 | 8.6928 | 8.6434 | -116.3169 | 4.1241 | 53.0660 | 0.0032 | 0.0115 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416449_61C220E8 | 152650 | 413 | -90.3 | 152650 | 251 | -97.6 | 152650 | 962 | -101.5 | 152650 | 525 |
| MR_1774416449_A138E0A2 | 152650 | 413 | -92.1 | 152650 | 251 | -97.7 | 152650 | 962 | -100.3 | 152650 | 525 |
| MR_1774416449_4792D2A5 | 504990 | 687 | -96.8 | 504990 | 473 | -96.0 | 504990 | 129 | -101.2 | 504990 | 492 |
| MR_1774416449_49EDF623 | 152650 | 413 | -89.7 | 152650 | 251 | -97.1 | 152650 | 962 | -99.6 | 152650 | 525 |
| MR_1774416449_E3955FBE | 504990 | 687 | -94.0 | 504990 | 473 | -96.9 | 504990 | 129 | -98.5 | 504990 | 492 |
| MR_1774416449_9F4E5C26 | 152650 | 413 | -91.0 | 152650 | 251 | -96.9 | 152650 | 962 | -100.0 | 152650 | 525 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 27: `873fc69e-de6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `873fc69e-de64-43c8-ae3b-8f02060b47eb` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[27] topology](images/test_0027.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258197_4
- `C2`: Lift the tilt angle of 3258197_4 by 5 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232615_3
- `C4`: Adjust the azimuth of 3232615_3 by 50 degrees
- `C5`: Check test server and transmission issues
- `C6`: Increase A3 Offset threshold for 3232615_3
- `C7`: Increase transmission power for 3232615_3
- `C8`: Decrease transmission power for 3258197_4
- `C9`: Add neighbor relationship between 3218124_2 and 3232615_3
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Press down the tilt angle of 3258197_4 by 5 degrees
- `C12`: Press down the tilt angle  of 3232615_3 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3258197_4
- `C14`: Increase A3 Offset threshold for 3258197_4
- `C15`: Add neighbor relationship between 3258197_4 and 3232615_3
- `C16`: Lift the tilt angle  of 3232615_3 by 10 degrees
- `C17`: Adjust the azimuth of 3258197_4 by 23 degrees
- `C18`: Decrease transmission power for 3232615_3
- `C19`: Increase transmission power for 3258197_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232615_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258197_4
- `C22`: Decrease A3 Offset threshold for 3232615_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.507 | MS1 | 121.4656593913 | 31.1446375515 | 711 | 504990 | -89.41 | 17.92 | 567.31 | 0.14 | 2.52 | 1584 |
| 2024-09-20 22:21:32.360 | MS1 | 121.4656628025 | 31.1446376189 | 711 | 504990 | -91.75 | 14.72 | 460.53 | 0.11 | 2.73 | 1593 |
| 2024-09-20 22:21:33.599 | MS1 | 121.4656658728 | 31.1446213312 | 711 | 504990 | -89.45 | 16.33 | 473.34 | 0.04 | 2.82 | 1573 |
| 2024-09-20 22:21:34.417 | MS1 | 121.4656750886 | 31.1446346778 | 711 | 504990 | -87.42 | 17.85 | 100.91 | 0.60 | 2.05 | 661 |
| 2024-09-20 22:21:35.350 | MS1 | 121.4656716639 | 31.1446283831 | 711 | 504990 | -91.87 | 12.75 | 51.79 | 0.57 | 2.24 | 606 |
| 2024-09-20 22:21:36.653 | MS1 | 121.4656604817 | 31.1446232400 | 711 | 504990 | -90.37 | 14.17 | 60.37 | 0.63 | 2.49 | 559 |
| 2024-09-20 22:21:37.436 | MS1 | 121.4656759296 | 31.1446186213 | 711 | 504990 | -89.74 | 10.42 | 87.91 | 0.53 | 2.90 | 648 |
| 2024-09-20 22:21:38.122 | MS1 | 121.4656682429 | 31.1446221740 | 711 | 504990 | -92.39 | 11.46 | 73.09 | 0.56 | 2.32 | 585 |
| 2024-09-20 22:21:39.797 | MS1 | 121.4656766744 | 31.1446230633 | 711 | 504990 | -90.87 | 11.39 | 90.01 | 0.54 | 2.89 | 530 |
| 2024-09-20 22:21:40.166 | MS1 | 121.4656716023 | 31.1446372794 | 711 | 504990 | -93.56 | 9.49 | 537.91 | 0.05 | 2.50 | 1576 |
| 2024-09-20 22:21:41.330 | MS1 | 121.4656695588 | 31.1446249997 | 711 | 504990 | -89.80 | 12.51 | 588.96 | 0.06 | 2.96 | 1600 |
| 2024-09-20 22:21:42.739 | MS1 | 121.4656754349 | 31.1446359122 | 711 | 504990 | -90.66 | 10.05 | 406.76 | 0.05 | 2.78 | 1581 |

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
| 3218124 | 2 | 121.4758929869 | 31.1481656547 | 205 | 11 | 1 | 37.7 | TDD | 475 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3232615 | 3 | 121.4655420631 | 31.1517338372 | 39 | 9 | 7 | 26.2 | TDD | 973 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3258197 | 4 | 121.4687459483 | 31.1487859144 | 235 | 1 | 1 | 36.2 | TDD | 711 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3260560 | 1 | 121.4732582252 | 31.1474504025 | 20 | 10 | 0 | 41.9 | TDD | 65 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.985 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.009 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.137 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.137 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.845 | NREventA3 | measId:2;ServCellPCI:810;Se... |
| 2024-09-20 22:21:38.085 | NRHandoverAttempt | SourcePCI:810;SourceNR-ARFC... |
| 2024-09-20 22:21:38.130 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.145 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.293 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.293 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260560 | 1 | 17.3530 | 14.1968 | -116.3115 | 14.6236 | 197.0461 | 0.0088 | 0.0143 |
| 2024_09_20 22:00 | 3218124 | 2 | 17.0472 | 18.2150 | -116.9461 | 16.0618 | 162.0483 | 0.0042 | 0.0063 |
| 2024_09_20 22:00 | 3232615 | 3 | 8.8814 | 8.3871 | -114.2959 | 15.8952 | 81.5540 | 0.0028 | 0.0036 |
| 2024_09_20 22:00 | 3258197 | 4 | 9.0678 | 19.4879 | -115.0780 | 8.2089 | 186.5805 | 0.0048 | 0.0133 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412397_919C46A9 | 504990 | 711 | -91.7 | 504990 | 973 | -99.6 | 504990 | 475 | -102.8 | 504990 | 65 |
| MR_1774412397_ACC725F9 | 504990 | 711 | -91.2 | 504990 | 973 | -97.6 | 504990 | 475 | -103.8 | 504990 | 65 |
| MR_1774412397_D71F19AB | 504990 | 711 | -92.5 | 504990 | 973 | -97.2 | 504990 | 475 | -104.1 | 504990 | 65 |
| MR_1774412397_BF8C4201 | 504990 | 711 | -93.3 | 504990 | 973 | -97.0 | 504990 | 475 | -102.7 | 504990 | 65 |
| MR_1774412397_88BE2926 | 504990 | 711 | -91.5 | 504990 | 973 | -99.4 | 504990 | 475 | -104.2 | 504990 | 65 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 28: `953a2987-d2c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `953a2987-d2cb-4697-8f77-760546a1845c` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[28] topology](images/test_0028.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3219010_3 by 5 degrees
- `C2`: Check test server and transmission issues
- `C3`: Lift the tilt angle of 3241856_2 by 7 degrees
- `C4`: Adjust the azimuth of 3219010_3 by 32 degrees
- `C5`: Press down the tilt angle of 3241856_2 by 7 degrees
- `C6`: Decrease A3 Offset threshold for 3219010_3
- `C7`: Adjust the azimuth of 3241856_2 by 11 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219010_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241856_2
- `C10`: Press down the tilt angle  of 3219010_3 by 5 degrees
- `C11`: Decrease A3 Offset threshold for 3241856_2
- `C12`: Increase transmission power for 3219010_3
- `C13`: Increase transmission power for 3241856_2
- `C14`: Add neighbor relationship between 3224033_4 and 3219010_3
- `C15`: Increase A3 Offset threshold for 3241856_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219010_3
- `C17`: Add neighbor relationship between 3241856_2 and 3219010_3
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241856_2
- `C20`: Increase A3 Offset threshold for 3219010_3
- `C21`: Decrease transmission power for 3241856_2
- `C22`: Decrease transmission power for 3219010_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.893 | MS1 | 121.4656587490 | 31.1446324149 | 329 | 504990 | -80.00 | 12.24 | 581.17 | 0.12 | 2.74 | 1565 |
| 2024-09-20 22:21:32.533 | MS1 | 121.4656697026 | 31.1446359389 | 329 | 504990 | -81.67 | 15.99 | 528.36 | 0.07 | 2.44 | 1580 |
| 2024-09-20 22:21:33.200 | MS1 | 121.4656584289 | 31.1446308426 | 329 | 504990 | -81.70 | 14.07 | 332.65 | 0.11 | 2.90 | 1561 |
| 2024-09-20 22:21:34.584 | MS1 | 121.4656682788 | 31.1446254397 | 329 | 504990 | -93.72 | -2.41 | 71.84 | 0.06 | 1.43 | 1577 |
| 2024-09-20 22:21:35.820 | MS1 | 121.4656613750 | 31.1446228432 | 329 | 504990 | -91.36 | -3.42 | 56.93 | 0.09 | 1.44 | 1585 |
| 2024-09-20 22:21:36.199 | MS1 | 121.4656655143 | 31.1446349399 | 329 | 504990 | -90.98 | -0.96 | 30.88 | 0.12 | 1.31 | 1571 |
| 2024-09-20 22:21:37.587 | MS1 | 121.4656763138 | 31.1446292607 | 329 | 504990 | -92.19 | -3.97 | 60.36 | 0.06 | 1.42 | 1596 |
| 2024-09-20 22:21:38.197 | MS1 | 121.4656604103 | 31.1446288921 | 329 | 504990 | -78.89 | 16.68 | 336.42 | 0.03 | 1.03 | 1597 |
| 2024-09-20 22:21:39.607 | MS1 | 121.4656642523 | 31.1446323766 | 329 | 504990 | -82.53 | 15.85 | 418.76 | 0.06 | 1.49 | 1582 |
| 2024-09-20 22:21:40.598 | MS1 | 121.4656688323 | 31.1446376022 | 329 | 504990 | -80.48 | 14.74 | 517.64 | 0.06 | 2.35 | 1573 |
| 2024-09-20 22:21:41.823 | MS1 | 121.4656709412 | 31.1446261085 | 329 | 504990 | -79.76 | 17.37 | 353.82 | 0.17 | 2.43 | 1565 |
| 2024-09-20 22:21:42.523 | MS1 | 121.4656613591 | 31.1446348499 | 329 | 504990 | -80.81 | 14.37 | 354.14 | 0.17 | 2.56 | 1572 |

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
| 3219010 | 3 | 121.4740565823 | 31.1519095350 | 257 | 3 | 12 | 35.1 | TDD | 428 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3224033 | 4 | 121.4646300558 | 31.1524205631 | 1 | 3 | 12 | 46.1 | TDD | 484 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3241856 | 2 | 121.4728835263 | 31.1528342212 | 206 | 4 | 7 | 49.9 | TDD | 329 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3272847 | 1 | 121.4684790694 | 31.1491734613 | 273 | 13 | 5 | 47.7 | TDD | 24 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.796 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.818 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.948 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.948 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.631 | NREventA3 | measId:2;ServCellPCI:839;Se... |
| 2024-09-20 22:21:35.631 | NREventA3 | measId:2;ServCellPCI:839;Se... |
| 2024-09-20 22:21:36.631 | NREventA3 | measId:2;ServCellPCI:839;Se... |
| 2024-09-20 22:21:39.131 | NRRRCReestablishAttempt | PCI:839 |
| 2024-09-20 22:21:39.150 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.160 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.292 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.292 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272847 | 1 | 5.4838 | 17.9453 | -117.8172 | 6.3420 | 91.0122 | 0.0123 | 0.0010 |
| 2024_09_20 22:00 | 3241856 | 2 | 18.9481 | 6.0241 | -115.8180 | 19.9936 | 84.1681 | 0.0199 | 0.1767 |
| 2024_09_20 22:00 | 3219010 | 3 | 10.8294 | 15.4763 | -117.0607 | 6.1199 | 90.3499 | 0.0046 | 0.0007 |
| 2024_09_20 22:00 | 3224033 | 4 | 15.5292 | 11.3028 | -114.4309 | 16.0285 | 188.7063 | 0.0167 | 0.0093 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416757_FEB61AA6 | 504990 | 329 | -94.1 | 504990 | 428 | -88.9 | 504990 | 484 | -93.8 | 504990 | 24 |
| MR_1774416757_A28AB2C7 | 504990 | 329 | -95.2 | 504990 | 428 | -89.2 | 504990 | 484 | -91.6 | 504990 | 24 |
| MR_1774416757_0EE61C05 | 504990 | 428 | -88.3 | 504990 | 329 | -94.1 | 504990 | 484 | -93.4 | 504990 | 24 |
| MR_1774416757_1B88E306 | 504990 | 329 | -94.3 | 504990 | 428 | -90.8 | 504990 | 484 | -91.5 | 504990 | 24 |
| MR_1774416757_025A9E44 | 504990 | 329 | -95.2 | 504990 | 428 | -90.6 | 504990 | 484 | -91.6 | 504990 | 24 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 29: `57895e51-e6e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `57895e51-e6e0-4d9a-bf80-94cd2cee557f` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[29] topology](images/test_0029.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272719_6
- `C2`: Press down the tilt angle of 3272719_6 by 5 degrees
- `C3`: Increase A3 Offset threshold for 3272719_6
- `C4`: Increase transmission power for 3272719_6
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219066_5
- `C6`: Decrease transmission power for 3219066_5
- `C7`: Add neighbor relationship between 3216455_11 and 3219066_5
- `C8`: Press down the tilt angle  of 3219066_5 by 5 degrees
- `C9`: Decrease A3 Offset threshold for 3219066_5
- `C10`: Check test server and transmission issues
- `C11`: Add neighbor relationship between 3272719_6 and 3219066_5
- `C12`: Adjust the azimuth of 3219066_5 by 33 degrees
- `C13`: Lift the tilt angle  of 3219066_5 by 5 degrees
- `C14`: Decrease A3 Offset threshold for 3272719_6
- `C15`: Increase A3 Offset threshold for 3219066_5
- `C16`: Lift the tilt angle of 3272719_6 by 5 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219066_5
- `C18`: Decrease transmission power for 3272719_6
- `C19`: Increase transmission power for 3219066_5
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Adjust the azimuth of 3272719_6 by 12 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272719_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.904 | MS1 | 121.4656665783 | 31.1446212006 | 511 | 504990 | -94.39 | 9.81 | 568.59 | 0.11 | 2.16 | 1576 |
| 2024-09-20 22:21:32.359 | MS1 | 121.4656776003 | 31.1446367287 | 821 | 504990 | -93.49 | 10.49 | 337.82 | 0.18 | 2.76 | 1563 |
| 2024-09-20 22:21:33.904 | MS1 | 121.4656710752 | 31.1446379201 | 713 | 504990 | -95.88 | 9.41 | 341.92 | 0.17 | 2.81 | 1561 |
| 2024-09-20 22:21:34.166 | MS1 | 121.4656758131 | 31.1446235294 | 479 | 152650 | -93.25 | 4.36 | 44.60 | 0.16 | 1.88 | 935 |
| 2024-09-20 22:21:35.393 | MS1 | 121.4656597939 | 31.1446242205 | 228 | 152650 | -90.15 | 7.95 | 104.72 | 0.06 | 1.74 | 978 |
| 2024-09-20 22:21:36.711 | MS1 | 121.4656767724 | 31.1446183074 | 787 | 152650 | -96.09 | 2.52 | 52.38 | 0.11 | 1.51 | 918 |
| 2024-09-20 22:21:37.401 | MS1 | 121.4656778200 | 31.1446184396 | 611 | 152650 | -90.01 | 6.03 | 46.39 | 0.03 | 1.73 | 929 |
| 2024-09-20 22:21:38.465 | MS1 | 121.4656762727 | 31.1446260632 | 479 | 152650 | -92.76 | 3.26 | 84.29 | 0.19 | 1.65 | 902 |
| 2024-09-20 22:21:39.873 | MS1 | 121.4656734092 | 31.1446223030 | 228 | 152650 | -96.16 | 3.36 | 67.07 | 0.08 | 1.92 | 941 |
| 2024-09-20 22:21:40.466 | MS1 | 121.4656580375 | 31.1446236564 | 787 | 152650 | -96.90 | 7.92 | 80.07 | 0.10 | 2.93 | 1568 |
| 2024-09-20 22:21:41.275 | MS1 | 121.4656703658 | 31.1446373108 | 611 | 152650 | -92.04 | 7.73 | 67.33 | 0.18 | 2.56 | 1594 |
| 2024-09-20 22:21:42.427 | MS1 | 121.4656591086 | 31.1446201082 | 479 | 152650 | -88.91 | 5.69 | 65.35 | 0.16 | 2.46 | 1578 |

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
| 3213228 | 12 | 121.4666934306 | 31.1448413029 | 284 | 7 | 8 | 23.1 | FDD | 565 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3215307 | 1 | 121.4655027099 | 31.1473966526 | 264 | 14 | 7 | 12.4 | TDD | 999 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3216455 | 11 | 121.4641491134 | 31.1459951380 | 358 | 12 | 4 | 14.9 | FDD | 787 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3219066 | 5 | 121.4744213101 | 31.1496379261 | 203 | 4 | 0 | 8.8 | TDD | 475 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3223367 | 13 | 121.4749593326 | 31.1458752100 | 353 | 9 | 4 | 16.7 | FDD | 287 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3224914 | 2 | 121.4661936919 | 31.1505766652 | 7 | 12 | 2 | 19.1 | TDD | 713 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3254284 | 8 | 121.4644445099 | 31.1501240778 | 225 | 13 | 3 | 7.8 | FDD | 228 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3259378 | 4 | 121.4755526998 | 31.1525970729 | 168 | 11 | 6 | 13.1 | TDD | 821 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3260871 | 3 | 121.4663699026 | 31.1486436933 | 11 | 9 | 12 | 23.4 | TDD | 241 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3272520 | 10 | 121.4741084260 | 31.1501868394 | 170 | 0 | 11 | 26.3 | FDD | 79 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3272719 | 6 | 121.4670422953 | 31.1529520948 | 176 | 5 | 8 | 1.6 | TDD | 511 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3274130 | 9 | 121.4720633881 | 31.1468846670 | 113 | 1 | 1 | 5.4 | FDD | 479 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3277729 | 7 | 121.4681120696 | 31.1503680250 | 282 | 3 | 2 | 0.5 | FDD | 611 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |

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
| 2024-09-20 22:21:31.422 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.442 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.591 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.591 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.240 | NREventA2 | measId:1;ServCellPCI:556;Se... |
| 2024-09-20 22:21:35.343 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.623 | NREventA5 | measId:3;ServCellPCI:556;Se... |
| 2024-09-20 22:21:35.691 | NRHandoverAttempt | SourcePCI:556;SourceNR-ARFC... |
| 2024-09-20 22:21:35.715 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.725 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.864 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.864 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215307 | 1 | 6.2617 | 6.2023 | -117.1026 | 10.4126 | 168.1948 | 0.0100 | 0.0186 |
| 2024_09_20 22:00 | 3224914 | 2 | 18.3356 | 12.9283 | -115.8242 | 7.5465 | 117.4535 | 0.0194 | 0.0191 |
| 2024_09_20 22:00 | 3260871 | 3 | 10.7519 | 18.8423 | -117.3648 | 16.1467 | 160.7951 | 0.0176 | 0.0155 |
| 2024_09_20 22:00 | 3259378 | 4 | 10.1086 | 5.4666 | -116.6615 | 15.9967 | 167.1233 | 0.0089 | 0.0076 |
| 2024_09_20 22:00 | 3219066 | 5 | 6.6932 | 6.8218 | -117.0903 | 6.6442 | 136.9965 | 0.0161 | 0.0195 |
| 2024_09_20 22:00 | 3272719 | 6 | 15.7777 | 17.1587 | -116.6879 | 6.5358 | 139.7891 | 0.0171 | 0.0005 |
| 2024_09_20 22:00 | 3277729 | 7 | 7.5723 | 12.3540 | -117.6028 | 4.6237 | 30.9731 | 0.0125 | 0.0123 |
| 2024_09_20 22:00 | 3254284 | 8 | 9.7522 | 6.8600 | -114.3156 | 4.3521 | 40.5525 | 0.0069 | 0.0074 |
| 2024_09_20 22:00 | 3274130 | 9 | 5.5995 | 7.2020 | -114.2614 | 3.3100 | 32.6850 | 0.0067 | 0.0070 |
| 2024_09_20 22:00 | 3272520 | 10 | 9.9840 | 6.7211 | -114.9663 | 4.7659 | 28.5067 | 0.0094 | 0.0073 |
| 2024_09_20 22:00 | 3216455 | 11 | 17.3889 | 10.0230 | -115.4786 | 4.2620 | 50.4063 | 0.0091 | 0.0015 |
| 2024_09_20 22:00 | 3213228 | 12 | 8.5434 | 15.1817 | -114.9806 | 3.0681 | 21.6840 | 0.0035 | 0.0063 |
| 2024_09_20 22:00 | 3223367 | 13 | 9.7781 | 19.0198 | -115.2727 | 3.4886 | 49.1583 | 0.0002 | 0.0195 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414388_E8F6DABA | 504990 | 713 | -94.0 | 504990 | 475 | -92.2 | 504990 | 241 | -99.8 | 504990 | 999 |
| MR_1774414388_A0AF161F | 152650 | 479 | -92.8 | 152650 | 287 | -96.1 | 152650 | 565 | -98.9 | 152650 | 79 |
| MR_1774414388_EDC3A5C7 | 504990 | 713 | -97.0 | 504990 | 475 | -92.7 | 504990 | 241 | -101.3 | 504990 | 999 |
| MR_1774414388_36F9E471 | 152650 | 479 | -91.9 | 152650 | 287 | -97.5 | 152650 | 565 | -98.5 | 152650 | 79 |
| MR_1774414388_29519F2E | 152650 | 479 | -92.1 | 152650 | 287 | -96.0 | 152650 | 565 | -101.4 | 152650 | 79 |
| MR_1774414388_53FA5A78 | 152650 | 479 | -92.5 | 152650 | 287 | -94.2 | 152650 | 565 | -98.9 | 152650 | 79 |

> *... 2개 열 생략 (전체 14열)*

---
