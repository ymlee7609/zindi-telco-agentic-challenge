# Track A 문제 분석 — test[30]~test[39]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[30] ~ test[39] (10개)

## 목차

1. [문제 30: `ec36b28f-50f...`](#30) — multiple-answer
2. [문제 31: `a13f26bb-650...`](#31) — single-answer
3. [문제 32: `a94886e5-732...`](#32) — single-answer
4. [문제 33: `dc8c7b18-2e5...`](#33) — multiple-answer
5. [문제 34: `db60dc66-0cf...`](#34) — single-answer
6. [문제 35: `473e08dd-1ac...`](#35) — multiple-answer
7. [문제 36: `261da544-08a...`](#36) — single-answer
8. [문제 37: `8b1ccd46-7cc...`](#37) — single-answer
9. [문제 38: `55477a77-37d...`](#38) — single-answer
10. [문제 39: `82e04c0a-479...`](#39) — multiple-answer

---

### 문제 30: `ec36b28f-50f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ec36b28f-50fb-4ea4-9bae-cf5add603526` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[30] topology](images/test_0030.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3228764_1 by 15 degrees
- `C2`: Increase A3 Offset threshold for 3237916_2
- `C3`: Check test server and transmission issues
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237916_2
- `C5`: Adjust the azimuth of 3237916_2 by 18 degrees
- `C6`: Press down the tilt angle of 3228764_1 by 6 degrees
- `C7`: Increase transmission power for 3237916_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228764_1
- `C9`: Lift the tilt angle of 3228764_1 by 6 degrees
- `C10`: Press down the tilt angle  of 3237916_2 by 6 degrees
- `C11`: Decrease transmission power for 3228764_1
- `C12`: Decrease A3 Offset threshold for 3228764_1
- `C13`: Increase A3 Offset threshold for 3228764_1
- `C14`: Decrease A3 Offset threshold for 3237916_2
- `C15`: Add neighbor relationship between 3227032_3 and 3237916_2
- `C16`: Increase transmission power for 3228764_1
- `C17`: Add neighbor relationship between 3228764_1 and 3237916_2
- `C18`: Decrease transmission power for 3237916_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237916_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228764_1
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Lift the tilt angle  of 3237916_2 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.162 | MS1 | 121.4656622493 | 31.1446251008 | 936 | 504990 | -78.83 | 16.89 | 393.96 | 0.16 | 2.18 | 1569 |
| 2024-09-20 22:21:32.783 | MS1 | 121.4656688105 | 31.1446266638 | 936 | 504990 | -80.77 | 13.54 | 571.69 | 0.01 | 2.89 | 1598 |
| 2024-09-20 22:21:33.584 | MS1 | 121.4656683287 | 31.1446276367 | 936 | 504990 | -84.44 | 15.53 | 535.66 | 0.13 | 2.38 | 1590 |
| 2024-09-20 22:21:34.852 | MS1 | 121.4656630270 | 31.1446274980 | 936 | 504990 | -91.80 | 1.53 | 94.23 | 0.06 | 1.18 | 1575 |
| 2024-09-20 22:21:35.912 | MS1 | 121.4656608739 | 31.1446334795 | 936 | 504990 | -91.30 | 3.02 | 73.03 | 0.10 | 1.00 | 1591 |
| 2024-09-20 22:21:36.627 | MS1 | 121.4656690653 | 31.1446239685 | 936 | 504990 | -93.12 | 0.42 | 63.35 | 0.11 | 1.27 | 1594 |
| 2024-09-20 22:21:37.977 | MS1 | 121.4656762678 | 31.1446277538 | 936 | 504990 | -89.79 | 0.53 | 76.71 | 0.03 | 1.09 | 1593 |
| 2024-09-20 22:21:38.687 | MS1 | 121.4656604598 | 31.1446300661 | 936 | 504990 | -87.16 | 3.65 | 64.17 | 0.06 | 1.24 | 1568 |
| 2024-09-20 22:21:39.302 | MS1 | 121.4656776808 | 31.1446321884 | 936 | 504990 | -88.98 | 3.00 | 74.21 | 0.15 | 1.15 | 1588 |
| 2024-09-20 22:21:40.628 | MS1 | 121.4656580280 | 31.1446290688 | 936 | 504990 | -82.28 | 14.11 | 441.87 | 0.17 | 2.79 | 1563 |
| 2024-09-20 22:21:41.725 | MS1 | 121.4656756781 | 31.1446234597 | 936 | 504990 | -82.25 | 16.43 | 521.83 | 0.18 | 2.40 | 1592 |
| 2024-09-20 22:21:42.220 | MS1 | 121.4656641064 | 31.1446294425 | 936 | 504990 | -84.09 | 17.14 | 513.66 | 0.03 | 2.10 | 1570 |

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
| 3227032 | 3 | 121.4713497093 | 31.1534576783 | 256 | 14 | 10 | 29.3 | TDD | 888 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3228764 | 1 | 121.4718913066 | 31.1470401080 | 231 | 3 | 11 | 32.4 | TDD | 936 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3237916 | 2 | 121.4694540674 | 31.1473367901 | 212 | 1 | 3 | 37.5 | TDD | 634 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3263866 | 4 | 121.4734850796 | 31.1457349487 | 177 | 6 | 5 | 24.6 | TDD | 104 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.735 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.759 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.872 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.872 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228764 | 1 | 14.5272 | 5.5337 | -109.8862 | 11.8818 | 130.4279 | 0.0027 | 0.0194 |
| 2024_09_20 22:00 | 3237916 | 2 | 18.9105 | 14.8145 | -117.3512 | 9.0193 | 93.7073 | 0.0096 | 0.0108 |
| 2024_09_20 22:00 | 3227032 | 3 | 7.7398 | 12.2946 | -115.3197 | 16.9123 | 123.5171 | 0.0059 | 0.0022 |
| 2024_09_20 22:00 | 3263866 | 4 | 17.8990 | 5.1809 | -116.2157 | 9.0720 | 147.5751 | 0.0151 | 0.0116 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414211_35231CC9 | 504990 | 634 | -91.5 | 504990 | 936 | -91.5 | 504990 | 888 | -91.0 | 504990 | 104 |
| MR_1774414211_F078C54F | 504990 | 936 | -93.1 | 504990 | 634 | -93.3 | 504990 | 888 | -91.9 | 504990 | 104 |
| MR_1774414211_C736E49B | 504990 | 634 | -93.0 | 504990 | 936 | -90.1 | 504990 | 888 | -91.3 | 504990 | 104 |
| MR_1774414211_598D4188 | 504990 | 936 | -90.8 | 504990 | 634 | -91.9 | 504990 | 888 | -92.8 | 504990 | 104 |
| MR_1774414211_EC7BC1C5 | 504990 | 936 | -90.4 | 504990 | 634 | -93.7 | 504990 | 888 | -94.1 | 504990 | 104 |
| MR_1774414211_CD103DEE | 504990 | 634 | -92.6 | 504990 | 936 | -92.5 | 504990 | 888 | -91.3 | 504990 | 104 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 31: `a13f26bb-650...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a13f26bb-650c-41e0-bda7-4eb1fa2f15b7` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[31] topology](images/test_0031.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Press down the tilt angle of 3271527_1 by 5 degrees
- `C3`: Decrease transmission power for 3271527_1
- `C4`: Adjust the azimuth of 3271527_1 by 45 degrees
- `C5`: Increase A3 Offset threshold for 3271527_1
- `C6`: Increase A3 Offset threshold for 3261740_4
- `C7`: Decrease A3 Offset threshold for 3271527_1
- `C8`: Increase transmission power for 3271527_1
- `C9`: Press down the tilt angle  of 3261740_4 by 3 degrees
- `C10`: Decrease transmission power for 3261740_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271527_1
- `C12`: Add neighbor relationship between 3235388_2 and 3261740_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261740_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271527_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261740_4
- `C17`: Adjust the azimuth of 3261740_4 by 6 degrees
- `C18`: Decrease A3 Offset threshold for 3261740_4
- `C19`: Increase transmission power for 3261740_4
- `C20`: Add neighbor relationship between 3271527_1 and 3261740_4
- `C21`: Lift the tilt angle  of 3261740_4 by 3 degrees
- `C22`: Lift the tilt angle of 3271527_1 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.649 | MS1 | 121.4656753926 | 31.1446258466 | 592 | 504990 | -75.32 | 16.35 | 446.88 | 0.08 | 2.15 | 1594 |
| 2024-09-20 22:21:32.521 | MS1 | 121.4656636443 | 31.1446193418 | 592 | 504990 | -75.55 | 13.75 | 479.93 | 0.18 | 2.39 | 1599 |
| 2024-09-20 22:21:33.513 | MS1 | 121.4656732152 | 31.1446358233 | 592 | 504990 | -82.01 | 15.32 | 353.54 | 0.15 | 2.32 | 1596 |
| 2024-09-20 22:21:34.340 | MS1 | 121.4656674425 | 31.1446294044 | 592 | 504990 | -92.92 | -3.97 | 60.48 | 0.06 | 1.11 | 1587 |
| 2024-09-20 22:21:35.606 | MS1 | 121.4656670967 | 31.1446267837 | 592 | 504990 | -84.84 | -2.03 | 63.94 | 0.07 | 1.17 | 1571 |
| 2024-09-20 22:21:36.889 | MS1 | 121.4656597874 | 31.1446327399 | 592 | 504990 | -88.47 | -3.48 | 44.20 | 0.04 | 1.27 | 1575 |
| 2024-09-20 22:21:37.891 | MS1 | 121.4656586127 | 31.1446304615 | 592 | 504990 | -87.76 | -0.61 | 59.65 | 0.19 | 1.17 | 1574 |
| 2024-09-20 22:21:38.767 | MS1 | 121.4656632604 | 31.1446214685 | 592 | 504990 | -89.38 | -3.19 | 62.60 | 0.17 | 1.09 | 1576 |
| 2024-09-20 22:21:39.566 | MS1 | 121.4656591066 | 31.1446225788 | 670 | 504990 | -79.75 | 16.31 | 252.75 | 0.00 | 1.23 | 1589 |
| 2024-09-20 22:21:40.888 | MS1 | 121.4656756459 | 31.1446263367 | 670 | 504990 | -80.05 | 15.40 | 590.32 | 0.19 | 2.24 | 1568 |
| 2024-09-20 22:21:41.604 | MS1 | 121.4656608472 | 31.1446379958 | 670 | 504990 | -75.71 | 16.80 | 479.77 | 0.01 | 2.70 | 1566 |
| 2024-09-20 22:21:42.588 | MS1 | 121.4656605650 | 31.1446213605 | 670 | 504990 | -79.85 | 13.60 | 444.89 | 0.11 | 2.94 | 1575 |

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
| 3224718 | 3 | 121.4640686529 | 31.1546766845 | 215 | 6 | 10 | 20.1 | TDD | 508 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3235388 | 2 | 121.4643147718 | 31.1487415430 | 338 | 13 | 10 | 25.1 | TDD | 898 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3261740 | 4 | 121.4729686978 | 31.1442238748 | 268 | 1 | 2 | 28.6 | TDD | 670 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3271527 | 1 | 121.4720257446 | 31.1508203823 | 176 | 3 | 4 | 29.2 | TDD | 592 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.875 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.895 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.014 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.014 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.729 | NREventA3 | measId:2;ServCellPCI:484;Se... |
| 2024-09-20 22:21:37.969 | NRHandoverAttempt | SourcePCI:484;SourceNR-ARFC... |
| 2024-09-20 22:21:38.012 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.026 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.150 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.150 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271527 | 1 | 6.6744 | 19.2204 | -114.3406 | 13.1846 | 137.4903 | 0.0182 | 0.1288 |
| 2024_09_20 22:00 | 3235388 | 2 | 12.1819 | 6.6325 | -117.4517 | 8.2613 | 147.8058 | 0.0109 | 0.0015 |
| 2024_09_20 22:00 | 3224718 | 3 | 8.7223 | 19.1163 | -116.7355 | 13.1293 | 137.5366 | 0.0144 | 0.0030 |
| 2024_09_20 22:00 | 3261740 | 4 | 16.0988 | 8.0501 | -117.0445 | 16.4548 | 137.2487 | 0.0012 | 0.0159 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413886_CB26B893 | 504990 | 592 | -91.1 | 504990 | 670 | -85.8 | 504990 | 898 | -89.0 | 504990 | 508 |
| MR_1774413886_4FB212DD | 504990 | 592 | -94.2 | 504990 | 670 | -86.8 | 504990 | 898 | -89.1 | 504990 | 508 |
| MR_1774413886_DEA6CC3B | 504990 | 592 | -92.8 | 504990 | 670 | -87.6 | 504990 | 898 | -86.4 | 504990 | 508 |
| MR_1774413886_AA8CABB9 | 504990 | 592 | -94.1 | 504990 | 670 | -85.3 | 504990 | 898 | -86.0 | 504990 | 508 |
| MR_1774413886_C00DFD1C | 504990 | 670 | -84.9 | 504990 | 592 | -91.8 | 504990 | 898 | -85.7 | 504990 | 508 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 32: `a94886e5-732...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a94886e5-732b-4786-9a3d-a0730a1aa23d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[32] topology](images/test_0032.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease A3 Offset threshold for 3271811_2
- `C3`: Decrease transmission power for 3271811_2
- `C4`: Increase A3 Offset threshold for 3271811_2
- `C5`: Press down the tilt angle  of 3271811_2 by 4 degrees
- `C6`: Decrease transmission power for 3213404_4
- `C7`: Add neighbor relationship between 3269191_11 and 3271811_2
- `C8`: Lift the tilt angle  of 3271811_2 by 4 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213404_4
- `C10`: Increase A3 Offset threshold for 3213404_4
- `C11`: Adjust the azimuth of 3271811_2 by 17 degrees
- `C12`: Add neighbor relationship between 3213404_4 and 3271811_2
- `C13`: Increase transmission power for 3213404_4
- `C14`: Press down the tilt angle of 3213404_4 by 5 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271811_2
- `C16`: Decrease A3 Offset threshold for 3213404_4
- `C17`: Adjust the azimuth of 3213404_4 by 20 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213404_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271811_2
- `C20`: Increase transmission power for 3271811_2
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Lift the tilt angle of 3213404_4 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.493 | MS1 | 121.4656761266 | 31.1446330705 | 435 | 504990 | -95.27 | 9.17 | 328.17 | 0.09 | 2.83 | 1600 |
| 2024-09-20 22:21:32.516 | MS1 | 121.4656666448 | 31.1446375719 | 28 | 504990 | -95.96 | 14.22 | 576.38 | 0.18 | 2.65 | 1562 |
| 2024-09-20 22:21:33.945 | MS1 | 121.4656627739 | 31.1446225005 | 556 | 504990 | -95.29 | 13.45 | 447.96 | 0.14 | 2.27 | 1563 |
| 2024-09-20 22:21:34.176 | MS1 | 121.4656583584 | 31.1446203191 | 165 | 152650 | -87.23 | 2.55 | 54.42 | 0.16 | 1.79 | 906 |
| 2024-09-20 22:21:35.335 | MS1 | 121.4656775524 | 31.1446243471 | 510 | 152650 | -96.30 | 5.98 | 94.95 | 0.11 | 1.51 | 959 |
| 2024-09-20 22:21:36.150 | MS1 | 121.4656651490 | 31.1446308749 | 624 | 152650 | -88.86 | 7.12 | 77.10 | 0.16 | 1.97 | 938 |
| 2024-09-20 22:21:37.730 | MS1 | 121.4656668764 | 31.1446253752 | 929 | 152650 | -87.59 | 4.23 | 88.01 | 0.04 | 1.57 | 988 |
| 2024-09-20 22:21:38.305 | MS1 | 121.4656737850 | 31.1446224026 | 165 | 152650 | -89.76 | 7.46 | 62.17 | 0.01 | 1.69 | 939 |
| 2024-09-20 22:21:39.587 | MS1 | 121.4656766202 | 31.1446289267 | 510 | 152650 | -96.98 | 6.44 | 93.44 | 0.03 | 1.96 | 907 |
| 2024-09-20 22:21:40.996 | MS1 | 121.4656648987 | 31.1446261699 | 624 | 152650 | -93.78 | 3.52 | 41.30 | 0.06 | 2.72 | 1562 |
| 2024-09-20 22:21:41.696 | MS1 | 121.4656739875 | 31.1446358417 | 929 | 152650 | -96.61 | 5.23 | 60.41 | 0.04 | 2.15 | 1578 |
| 2024-09-20 22:21:42.977 | MS1 | 121.4656733941 | 31.1446307934 | 165 | 152650 | -95.46 | 7.22 | 61.87 | 0.03 | 2.04 | 1563 |

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
| 3213404 | 4 | 121.4691819213 | 31.1516967861 | 183 | 3 | 0 | 27.3 | TDD | 435 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3213962 | 1 | 121.4641702463 | 31.1483793346 | 5 | 13 | 11 | 10.5 | TDD | 66 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3218747 | 13 | 121.4676496185 | 31.1510423956 | 73 | 10 | 5 | 19.9 | FDD | 510 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3219064 | 12 | 121.4704911957 | 31.1481136557 | 276 | 2 | 2 | 23.8 | FDD | 817 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3226680 | 9 | 121.4692474124 | 31.1546777180 | 286 | 2 | 9 | 18.2 | FDD | 165 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3227767 | 7 | 121.4692622203 | 31.1475306841 | 6 | 14 | 5 | 10.8 | FDD | 929 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3228699 | 3 | 121.4742095589 | 31.1499438826 | 349 | 12 | 12 | 29.6 | TDD | 556 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3237739 | 10 | 121.4748801436 | 31.1481646741 | 128 | 12 | 3 | 6.0 | FDD | 654 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3263131 | 5 | 121.4734639619 | 31.1511692358 | 148 | 3 | 3 | 7.5 | TDD | 22 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3269191 | 11 | 121.4754906511 | 31.1491799807 | 166 | 2 | 3 | 27.2 | FDD | 624 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3271655 | 6 | 121.4754390173 | 31.1559353437 | 318 | 1 | 3 | 16.5 | TDD | 28 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3271811 | 2 | 121.4751857176 | 31.1492444414 | 223 | 2 | 1 | 29.9 | TDD | 616 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3275729 | 8 | 121.4716839999 | 31.1474326027 | 99 | 9 | 6 | 26.7 | FDD | 227 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |

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
| 2024-09-20 22:21:30.874 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.892 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.032 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.032 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.767 | NREventA2 | measId:1;ServCellPCI:173;Se... |
| 2024-09-20 22:21:34.884 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.184 | NREventA5 | measId:3;ServCellPCI:173;Se... |
| 2024-09-20 22:21:35.218 | NRHandoverAttempt | SourcePCI:173;SourceNR-ARFC... |
| 2024-09-20 22:21:35.264 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.278 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.388 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.388 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213962 | 1 | 15.5991 | 13.0811 | -116.9211 | 9.1372 | 80.2318 | 0.0034 | 0.0177 |
| 2024_09_20 22:00 | 3271811 | 2 | 10.7350 | 14.2925 | -117.6750 | 12.2090 | 189.2120 | 0.0198 | 0.0127 |
| 2024_09_20 22:00 | 3228699 | 3 | 9.7189 | 7.9990 | -114.7151 | 5.2646 | 147.4738 | 0.0096 | 0.0110 |
| 2024_09_20 22:00 | 3213404 | 4 | 13.1444 | 11.5434 | -116.3793 | 7.5248 | 182.7732 | 0.0168 | 0.0188 |
| 2024_09_20 22:00 | 3263131 | 5 | 9.4681 | 17.9560 | -114.0212 | 15.5068 | 118.7669 | 0.0067 | 0.0066 |
| 2024_09_20 22:00 | 3271655 | 6 | 8.7207 | 15.5449 | -115.7805 | 5.6846 | 185.5598 | 0.0193 | 0.0069 |
| 2024_09_20 22:00 | 3227767 | 7 | 13.6492 | 17.2307 | -117.4075 | 4.2447 | 36.1221 | 0.0017 | 0.0044 |
| 2024_09_20 22:00 | 3275729 | 8 | 8.3772 | 17.2978 | -115.3116 | 3.2621 | 25.6649 | 0.0055 | 0.0171 |
| 2024_09_20 22:00 | 3226680 | 9 | 10.4439 | 11.2003 | -115.4037 | 3.3710 | 44.5600 | 0.0031 | 0.0004 |
| 2024_09_20 22:00 | 3237739 | 10 | 13.6571 | 19.3488 | -114.7216 | 3.2939 | 58.5487 | 0.0174 | 0.0130 |
| 2024_09_20 22:00 | 3269191 | 11 | 17.5359 | 6.6475 | -115.0376 | 3.1527 | 40.1857 | 0.0027 | 0.0064 |
| 2024_09_20 22:00 | 3219064 | 12 | 18.8805 | 11.8530 | -116.5788 | 3.2071 | 39.1835 | 0.0027 | 0.0157 |
| 2024_09_20 22:00 | 3218747 | 13 | 7.1359 | 13.6109 | -114.0623 | 3.1173 | 27.5843 | 0.0008 | 0.0127 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414468_DACFCD8C | 152650 | 165 | -86.9 | 152650 | 817 | -94.2 | 152650 | 654 | -96.8 | 152650 | 227 |
| MR_1774414468_85707D11 | 152650 | 165 | -85.3 | 152650 | 817 | -92.7 | 152650 | 654 | -99.2 | 152650 | 227 |
| MR_1774414468_9EDD4381 | 152650 | 165 | -85.4 | 152650 | 817 | -94.1 | 152650 | 654 | -96.3 | 152650 | 227 |
| MR_1774414468_1BF027B4 | 152650 | 165 | -89.0 | 152650 | 817 | -93.2 | 152650 | 654 | -96.2 | 152650 | 227 |
| MR_1774414468_06649C15 | 504990 | 556 | -96.9 | 504990 | 616 | -95.8 | 504990 | 66 | -99.4 | 504990 | 22 |
| MR_1774414468_DBC094F6 | 152650 | 165 | -85.8 | 152650 | 817 | -95.4 | 152650 | 654 | -96.5 | 152650 | 227 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 33: `dc8c7b18-2e5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dc8c7b18-2e52-4d8f-b283-e7c8af8eaccd` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[33] topology](images/test_0033.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3228895_2 by 17 degrees
- `C2`: Check test server and transmission issues
- `C3`: Press down the tilt angle of 3228895_2 by 10 degrees
- `C4`: Increase transmission power for 3216306_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216306_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216306_1
- `C7`: Lift the tilt angle  of 3216306_1 by 5 degrees
- `C8`: Add neighbor relationship between 3228895_2 and 3216306_1
- `C9`: Decrease transmission power for 3228895_2
- `C10`: Press down the tilt angle  of 3216306_1 by 5 degrees
- `C11`: Adjust the azimuth of 3216306_1 by 12 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228895_2
- `C13`: Decrease A3 Offset threshold for 3228895_2
- `C14`: Increase transmission power for 3228895_2
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Increase A3 Offset threshold for 3216306_1
- `C17`: Decrease transmission power for 3216306_1
- `C18`: Decrease A3 Offset threshold for 3216306_1
- `C19`: Increase A3 Offset threshold for 3228895_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228895_2
- `C21`: Lift the tilt angle of 3228895_2 by 10 degrees
- `C22`: Add neighbor relationship between 3219805_3 and 3216306_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.232 | MS1 | 121.4656586933 | 31.1446252502 | 577 | 504990 | -88.06 | 12.73 | 416.00 | 0.15 | 2.98 | 1579 |
| 2024-09-20 22:21:32.235 | MS1 | 121.4656611953 | 31.1446316816 | 577 | 504990 | -92.88 | 16.32 | 504.21 | 0.15 | 2.90 | 1589 |
| 2024-09-20 22:21:33.737 | MS1 | 121.4656734881 | 31.1446374937 | 577 | 504990 | -87.25 | 16.70 | 381.42 | 0.08 | 2.61 | 1587 |
| 2024-09-20 22:21:34.413 | MS1 | 121.4656596548 | 31.1446366036 | 577 | 504990 | -100.83 | 1.58 | 63.70 | 0.14 | 1.45 | 1574 |
| 2024-09-20 22:21:35.574 | MS1 | 121.4656582085 | 31.1446273473 | 577 | 504990 | -104.98 | 0.94 | 40.76 | 0.06 | 1.13 | 1582 |
| 2024-09-20 22:21:36.595 | MS1 | 121.4656639992 | 31.1446234549 | 577 | 504990 | -100.32 | -1.80 | 28.74 | 0.17 | 1.05 | 1577 |
| 2024-09-20 22:21:37.123 | MS1 | 121.4656654047 | 31.1446326027 | 577 | 504990 | -100.64 | 0.67 | 59.20 | 0.04 | 1.28 | 1579 |
| 2024-09-20 22:21:38.826 | MS1 | 121.4656599881 | 31.1446277891 | 577 | 504990 | -106.57 | -0.28 | 71.48 | 0.19 | 1.44 | 1590 |
| 2024-09-20 22:21:39.205 | MS1 | 121.4656658795 | 31.1446267973 | 577 | 504990 | -103.43 | -1.30 | 73.19 | 0.05 | 1.28 | 1585 |
| 2024-09-20 22:21:40.289 | MS1 | 121.4656683813 | 31.1446365779 | 577 | 504990 | -88.68 | 15.70 | 306.33 | 0.03 | 2.34 | 1593 |
| 2024-09-20 22:21:41.546 | MS1 | 121.4656765986 | 31.1446303836 | 577 | 504990 | -90.39 | 12.54 | 531.24 | 0.15 | 2.20 | 1582 |
| 2024-09-20 22:21:42.188 | MS1 | 121.4656765066 | 31.1446326043 | 577 | 504990 | -94.26 | 13.62 | 557.97 | 0.13 | 2.62 | 1597 |

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
| 3214634 | 4 | 121.4689488349 | 31.1498263978 | 141 | 13 | 4 | 46.7 | TDD | 783 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3216306 | 1 | 121.4654653923 | 31.1555870802 | 191 | 4 | 12 | 16.5 | TDD | 544 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3219805 | 3 | 121.4736118597 | 31.1496312842 | 323 | 10 | 5 | 28.8 | TDD | 103 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3228895 | 2 | 121.4731980198 | 31.1453128746 | 247 | 11 | 2 | 21.5 | TDD | 577 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.330 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.348 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.448 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.448 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.707 | NREventA2 | measId:1;ServCellPCI:393;Se... |
| 2024-09-20 22:21:34.852 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216306 | 1 | 11.3244 | 6.8986 | -116.7994 | 6.6069 | 191.6531 | 0.0048 | 0.0056 |
| 2024_09_20 22:00 | 3228895 | 2 | 17.7365 | 10.5246 | -116.6148 | 8.1293 | 110.6528 | 0.1558 | 0.0099 |
| 2024_09_20 22:00 | 3219805 | 3 | 16.3572 | 7.0400 | -117.9893 | 16.5999 | 95.0187 | 0.0052 | 0.0131 |
| 2024_09_20 22:00 | 3214634 | 4 | 17.3762 | 5.9338 | -116.2071 | 11.0758 | 162.3868 | 0.0066 | 0.0010 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414531_E14FD891 | 504990 | 577 | -100.4 | 504990 | 544 | -107.8 | 504990 | 103 | -113.8 | 504990 | 783 |
| MR_1774414531_A25749C2 | 504990 | 577 | -102.2 | 504990 | 544 | -106.8 | 504990 | 103 | -113.5 | 504990 | 783 |
| MR_1774414531_873C26DA | 504990 | 577 | -99.2 | 504990 | 544 | -107.4 | 504990 | 103 | -114.1 | 504990 | 783 |
| MR_1774414531_4FAA5C9F | 504990 | 577 | -100.8 | 504990 | 544 | -108.8 | 504990 | 103 | -113.4 | 504990 | 783 |
| MR_1774414531_4EE68C68 | 504990 | 577 | -100.7 | 504990 | 544 | -105.8 | 504990 | 103 | -111.6 | 504990 | 783 |
| MR_1774414531_542DAFBE | 504990 | 577 | -100.3 | 504990 | 544 | -109.4 | 504990 | 103 | -110.8 | 504990 | 783 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 34: `db60dc66-0cf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `db60dc66-0cf4-4294-a2a5-9561ac03d18a` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[34] topology](images/test_0034.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3215240_2 by 2 degrees
- `C2`: Add neighbor relationship between 3232266_9 and 3215240_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215240_2
- `C4`: Decrease transmission power for 3215240_2
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215240_2
- `C7`: Increase A3 Offset threshold for 3224256_6
- `C8`: Add neighbor relationship between 3224256_6 and 3215240_2
- `C9`: Adjust the azimuth of 3224256_6 by 32 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224256_6
- `C11`: Check test server and transmission issues
- `C12`: Decrease A3 Offset threshold for 3224256_6
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224256_6
- `C14`: Lift the tilt angle  of 3215240_2 by 2 degrees
- `C15`: Increase transmission power for 3215240_2
- `C16`: Decrease transmission power for 3224256_6
- `C17`: Lift the tilt angle of 3224256_6 by 3 degrees
- `C18`: Decrease A3 Offset threshold for 3215240_2
- `C19`: Increase transmission power for 3224256_6
- `C20`: Increase A3 Offset threshold for 3215240_2
- `C21`: Press down the tilt angle of 3224256_6 by 3 degrees
- `C22`: Adjust the azimuth of 3215240_2 by 28 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.616 | MS1 | 121.4656623685 | 31.1446236466 | 540 | 504990 | -94.34 | 13.87 | 514.66 | 0.11 | 2.47 | 1600 |
| 2024-09-20 22:21:32.210 | MS1 | 121.4656742725 | 31.1446375991 | 248 | 504990 | -94.81 | 11.03 | 384.08 | 0.16 | 2.20 | 1595 |
| 2024-09-20 22:21:33.167 | MS1 | 121.4656765262 | 31.1446193750 | 145 | 504990 | -93.10 | 14.83 | 497.90 | 0.06 | 2.44 | 1566 |
| 2024-09-20 22:21:34.306 | MS1 | 121.4656764767 | 31.1446311352 | 641 | 152650 | -89.06 | 3.21 | 91.48 | 0.13 | 1.96 | 998 |
| 2024-09-20 22:21:35.475 | MS1 | 121.4656644612 | 31.1446340997 | 108 | 152650 | -89.36 | 3.07 | 64.50 | 0.10 | 1.99 | 974 |
| 2024-09-20 22:21:36.129 | MS1 | 121.4656733491 | 31.1446313222 | 324 | 152650 | -90.96 | 6.28 | 100.91 | 0.11 | 1.96 | 933 |
| 2024-09-20 22:21:37.476 | MS1 | 121.4656683088 | 31.1446330811 | 481 | 152650 | -88.83 | 5.85 | 54.72 | 0.09 | 1.87 | 907 |
| 2024-09-20 22:21:38.940 | MS1 | 121.4656734028 | 31.1446309891 | 641 | 152650 | -88.54 | 4.97 | 76.66 | 0.07 | 1.79 | 905 |
| 2024-09-20 22:21:39.160 | MS1 | 121.4656710988 | 31.1446201459 | 108 | 152650 | -95.86 | 2.48 | 59.24 | 0.06 | 1.85 | 903 |
| 2024-09-20 22:21:40.700 | MS1 | 121.4656644428 | 31.1446325173 | 324 | 152650 | -95.84 | 7.38 | 66.20 | 0.17 | 2.25 | 1567 |
| 2024-09-20 22:21:41.118 | MS1 | 121.4656607708 | 31.1446319557 | 481 | 152650 | -92.00 | 5.71 | 77.05 | 0.11 | 2.88 | 1560 |
| 2024-09-20 22:21:42.539 | MS1 | 121.4656679354 | 31.1446266711 | 641 | 152650 | -96.23 | 2.19 | 78.37 | 0.16 | 2.30 | 1595 |

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
| 3210643 | 12 | 121.4713818073 | 31.1457471441 | 84 | 7 | 5 | 28.8 | FDD | 82 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3213555 | 8 | 121.4748499846 | 31.1533077818 | 84 | 5 | 9 | 3.4 | FDD | 481 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3215240 | 2 | 121.4671280616 | 31.1539272386 | 216 | 1 | 0 | 17.2 | TDD | 910 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3219222 | 5 | 121.4684190035 | 31.1448913845 | 238 | 3 | 12 | 21.0 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3221126 | 13 | 121.4658902550 | 31.1536702374 | 288 | 12 | 8 | 29.8 | FDD | 883 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3224256 | 6 | 121.4687180814 | 31.1467066937 | 264 | 3 | 2 | 3.2 | TDD | 540 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3232266 | 9 | 121.4665913358 | 31.1443337913 | 133 | 7 | 12 | 11.2 | FDD | 324 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3243333 | 1 | 121.4689664564 | 31.1471425328 | 251 | 10 | 4 | 22.7 | TDD | 652 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3245645 | 3 | 121.4679256443 | 31.1465328699 | 141 | 4 | 11 | 1.4 | TDD | 528 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3258299 | 4 | 121.4653973998 | 31.1446224502 | 352 | 0 | 6 | 7.4 | TDD | 145 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3258775 | 10 | 121.4693160976 | 31.1552220156 | 0 | 7 | 8 | 17.5 | FDD | 165 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3260781 | 11 | 121.4737255254 | 31.1458237087 | 198 | 7 | 0 | 24.6 | FDD | 108 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3260801 | 7 | 121.4667949893 | 31.1551528296 | 291 | 14 | 1 | 28.9 | FDD | 641 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |

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
| 2024-09-20 22:21:31.580 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.604 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.720 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.720 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.408 | NREventA2 | measId:1;ServCellPCI:580;Se... |
| 2024-09-20 22:21:35.548 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.818 | NREventA5 | measId:3;ServCellPCI:580;Se... |
| 2024-09-20 22:21:35.891 | NRHandoverAttempt | SourcePCI:580;SourceNR-ARFC... |
| 2024-09-20 22:21:35.916 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.929 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.076 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.076 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243333 | 1 | 17.3732 | 5.2268 | -115.9065 | 5.1210 | 190.5360 | 0.0050 | 0.0186 |
| 2024_09_20 22:00 | 3215240 | 2 | 11.4984 | 12.2790 | -114.8313 | 15.0680 | 159.7785 | 0.0115 | 0.0166 |
| 2024_09_20 22:00 | 3245645 | 3 | 7.9982 | 14.2974 | -116.8751 | 8.4198 | 180.9598 | 0.0164 | 0.0189 |
| 2024_09_20 22:00 | 3258299 | 4 | 15.6772 | 16.5149 | -115.6969 | 5.5989 | 184.4690 | 0.0005 | 0.0029 |
| 2024_09_20 22:00 | 3219222 | 5 | 16.2997 | 16.7828 | -115.7402 | 16.2745 | 183.6215 | 0.0171 | 0.0118 |
| 2024_09_20 22:00 | 3224256 | 6 | 11.8074 | 6.9643 | -114.2099 | 8.9072 | 186.4115 | 0.0073 | 0.0111 |
| 2024_09_20 22:00 | 3260801 | 7 | 9.7462 | 12.3753 | -115.5838 | 3.4030 | 20.2027 | 0.0045 | 0.0186 |
| 2024_09_20 22:00 | 3213555 | 8 | 10.3933 | 12.1315 | -116.1368 | 4.7402 | 46.9038 | 0.0069 | 0.0138 |
| 2024_09_20 22:00 | 3232266 | 9 | 6.1166 | 15.1207 | -116.9263 | 4.0194 | 53.3975 | 0.0098 | 0.0117 |
| 2024_09_20 22:00 | 3258775 | 10 | 18.8203 | 7.3218 | -114.5051 | 3.4401 | 25.6509 | 0.0198 | 0.0089 |
| 2024_09_20 22:00 | 3260781 | 11 | 13.2605 | 17.9672 | -115.3877 | 4.1282 | 36.4920 | 0.0178 | 0.0153 |
| 2024_09_20 22:00 | 3210643 | 12 | 15.3544 | 6.0327 | -115.1014 | 4.7422 | 55.4400 | 0.0139 | 0.0093 |
| 2024_09_20 22:00 | 3221126 | 13 | 8.1431 | 14.8789 | -116.9347 | 3.7002 | 26.4551 | 0.0178 | 0.0086 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413566_4C3D3D9D | 152650 | 641 | -89.5 | 152650 | 165 | -95.3 | 152650 | 82 | -98.4 | 152650 | 883 |
| MR_1774413566_9EF9E9BD | 152650 | 641 | -87.6 | 152650 | 165 | -93.4 | 152650 | 82 | -96.9 | 152650 | 883 |
| MR_1774413566_0374D698 | 504990 | 145 | -93.4 | 504990 | 910 | -89.6 | 504990 | 652 | -98.4 | 504990 | 528 |
| MR_1774413566_A69F0084 | 152650 | 641 | -88.4 | 152650 | 165 | -95.5 | 152650 | 82 | -98.4 | 152650 | 883 |
| MR_1774413566_EDE8DEBF | 152650 | 641 | -88.1 | 152650 | 165 | -92.2 | 152650 | 82 | -99.6 | 152650 | 883 |
| MR_1774413566_25988A4C | 504990 | 145 | -93.7 | 504990 | 910 | -88.7 | 504990 | 652 | -99.9 | 504990 | 528 |
| MR_1774413566_90DC9CFF | 504990 | 145 | -93.4 | 504990 | 910 | -89.6 | 504990 | 652 | -99.6 | 504990 | 528 |
| MR_1774413566_10885CA3 | 504990 | 145 | -92.5 | 504990 | 910 | -88.3 | 504990 | 652 | -100.1 | 504990 | 528 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 35: `473e08dd-1ac...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `473e08dd-1acf-49c8-9730-8e1962f202cf` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[35] topology](images/test_0035.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Press down the tilt angle of 3218846_2 by 7 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218846_2
- `C4`: Decrease transmission power for 3218846_2
- `C5`: Adjust the azimuth of 3218846_2 by 50 degrees
- `C6`: Decrease transmission power for 3258202_3
- `C7`: Increase transmission power for 3258202_3
- `C8`: Press down the tilt angle  of 3258202_3 by 2 degrees
- `C9`: Increase A3 Offset threshold for 3218846_2
- `C10`: Increase A3 Offset threshold for 3258202_3
- `C11`: Add neighbor relationship between 3268665_1 and 3258202_3
- `C12`: Decrease A3 Offset threshold for 3218846_2
- `C13`: Decrease A3 Offset threshold for 3258202_3
- `C14`: Increase transmission power for 3218846_2
- `C15`: Add neighbor relationship between 3218846_2 and 3258202_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218846_2
- `C17`: Adjust the azimuth of 3258202_3 by 12 degrees
- `C18`: Lift the tilt angle of 3218846_2 by 7 degrees
- `C19`: Lift the tilt angle  of 3258202_3 by 2 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258202_3
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258202_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.368 | MS1 | 121.4656588083 | 31.1446280537 | 738 | 504990 | -93.49 | 17.92 | 448.43 | 0.03 | 2.73 | 1577 |
| 2024-09-20 22:21:32.540 | MS1 | 121.4656704356 | 31.1446237244 | 738 | 504990 | -86.47 | 14.61 | 414.64 | 0.15 | 2.01 | 1578 |
| 2024-09-20 22:21:33.887 | MS1 | 121.4656735316 | 31.1446344558 | 738 | 504990 | -85.57 | 12.85 | 319.03 | 0.06 | 2.73 | 1579 |
| 2024-09-20 22:21:34.411 | MS1 | 121.4656586492 | 31.1446349651 | 738 | 504990 | -106.64 | -0.34 | 37.41 | 0.09 | 1.21 | 1561 |
| 2024-09-20 22:21:35.441 | MS1 | 121.4656726533 | 31.1446239440 | 738 | 504990 | -102.30 | -1.60 | 66.76 | 0.20 | 1.19 | 1566 |
| 2024-09-20 22:21:36.624 | MS1 | 121.4656751481 | 31.1446212622 | 738 | 504990 | -101.38 | -0.09 | 28.70 | 0.08 | 1.20 | 1571 |
| 2024-09-20 22:21:37.518 | MS1 | 121.4656725127 | 31.1446194598 | 738 | 504990 | -109.04 | -0.99 | 62.69 | 0.14 | 1.08 | 1570 |
| 2024-09-20 22:21:38.907 | MS1 | 121.4656745073 | 31.1446183648 | 738 | 504990 | -103.49 | -0.18 | 44.68 | 0.18 | 1.25 | 1579 |
| 2024-09-20 22:21:39.450 | MS1 | 121.4656682935 | 31.1446349272 | 738 | 504990 | -107.93 | -1.34 | 54.15 | 0.17 | 1.39 | 1587 |
| 2024-09-20 22:21:40.160 | MS1 | 121.4656640246 | 31.1446256865 | 738 | 504990 | -90.31 | 15.87 | 501.21 | 0.04 | 2.38 | 1590 |
| 2024-09-20 22:21:41.581 | MS1 | 121.4656689324 | 31.1446272387 | 738 | 504990 | -86.86 | 14.63 | 392.21 | 0.03 | 2.34 | 1568 |
| 2024-09-20 22:21:42.326 | MS1 | 121.4656636693 | 31.1446235376 | 738 | 504990 | -94.31 | 12.42 | 604.47 | 0.05 | 2.25 | 1598 |

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
| 3218846 | 2 | 121.4649774114 | 31.1489756377 | 94 | 5 | 2 | 18.5 | TDD | 738 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3231406 | 4 | 121.4758645704 | 31.1445124138 | 45 | 13 | 8 | 44.4 | TDD | 466 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3258202 | 3 | 121.4752022989 | 31.1509397531 | 220 | 1 | 10 | 17.9 | TDD | 323 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3268665 | 1 | 121.4747624614 | 31.1529777614 | 77 | 11 | 7 | 34.6 | TDD | 489 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.586 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.609 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.756 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.756 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.911 | NREventA2 | measId:1;ServCellPCI:720;Se... |
| 2024-09-20 22:21:35.048 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268665 | 1 | 13.1081 | 10.1221 | -116.2703 | 5.1988 | 162.7328 | 0.0087 | 0.0174 |
| 2024_09_20 22:00 | 3218846 | 2 | 8.9929 | 17.1532 | -116.8802 | 8.6333 | 172.4124 | 0.1344 | 0.0096 |
| 2024_09_20 22:00 | 3258202 | 3 | 10.5366 | 7.5323 | -115.2994 | 5.9234 | 139.8585 | 0.0021 | 0.0129 |
| 2024_09_20 22:00 | 3231406 | 4 | 19.5867 | 16.3323 | -115.3382 | 11.2700 | 125.9531 | 0.0015 | 0.0111 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412078_32A4F310 | 504990 | 738 | -106.5 | 504990 | 323 | -113.6 | 504990 | 489 | -118.6 | 504990 | 466 |
| MR_1774412078_539F571E | 504990 | 738 | -108.5 | 504990 | 323 | -116.1 | 504990 | 489 | -120.3 | 504990 | 466 |
| MR_1774412078_1A2F4A68 | 504990 | 738 | -106.6 | 504990 | 323 | -113.6 | 504990 | 489 | -119.9 | 504990 | 466 |
| MR_1774412078_90D00169 | 504990 | 738 | -105.8 | 504990 | 323 | -113.8 | 504990 | 489 | -118.7 | 504990 | 466 |
| MR_1774412078_51710976 | 504990 | 738 | -107.7 | 504990 | 323 | -115.3 | 504990 | 489 | -121.1 | 504990 | 466 |
| MR_1774412078_2561990A | 504990 | 738 | -105.2 | 504990 | 323 | -113.6 | 504990 | 489 | -120.8 | 504990 | 466 |
| MR_1774412078_C8A2C668 | 504990 | 738 | -106.9 | 504990 | 323 | -115.2 | 504990 | 489 | -120.2 | 504990 | 466 |
| MR_1774412078_B8549602 | 504990 | 738 | -105.4 | 504990 | 323 | -113.2 | 504990 | 489 | -119.5 | 504990 | 466 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 36: `261da544-08a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `261da544-08ac-48da-80f0-d3f9ada44f29` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[36] topology](images/test_0036.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Lift the tilt angle  of 3229050_2 by 10 degrees
- `C3`: Press down the tilt angle  of 3229050_2 by 10 degrees
- `C4`: Add neighbor relationship between 3240455_3 and 3237822_1
- `C5`: Add neighbor relationship between 3229050_2 and 3237822_1
- `C6`: Lift the tilt angle of 3240455_3 by 6 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240455_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237822_1
- `C9`: Decrease transmission power for 3240455_3
- `C10`: Adjust the azimuth of 3229050_2 by 48 degrees
- `C11`: Increase transmission power for 3237822_1
- `C12`: Press down the tilt angle of 3240455_3 by 6 degrees
- `C13`: Increase A3 Offset threshold for 3240455_3
- `C14`: Decrease A3 Offset threshold for 3240455_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237822_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240455_3
- `C17`: Adjust the azimuth of 3240455_3 by 42 degrees
- `C18`: Increase A3 Offset threshold for 3237822_1
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease transmission power for 3237822_1
- `C21`: Increase transmission power for 3240455_3
- `C22`: Decrease A3 Offset threshold for 3237822_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.999 | MS1 | 121.4656714416 | 31.1446232802 | 124 | 504990 | -87.33 | 16.63 | 579.43 | 0.02 | 2.73 | 1580 |
| 2024-09-20 22:21:32.920 | MS1 | 121.4656616588 | 31.1446237033 | 124 | 504990 | -90.91 | 16.82 | 351.30 | 0.07 | 2.46 | 1569 |
| 2024-09-20 22:21:33.192 | MS1 | 121.4656723197 | 31.1446191248 | 124 | 504990 | -85.18 | 16.09 | 531.14 | 0.09 | 2.09 | 1586 |
| 2024-09-20 22:21:34.544 | MS1 | 121.4656697708 | 31.1446190689 | 124 | 504990 | -87.65 | 14.82 | 94.57 | 0.13 | 2.55 | 1592 |
| 2024-09-20 22:21:35.883 | MS1 | 121.4656724458 | 31.1446373745 | 124 | 504990 | -86.49 | 17.00 | 55.23 | 0.20 | 2.50 | 1581 |
| 2024-09-20 22:21:36.259 | MS1 | 121.4656713646 | 31.1446286134 | 124 | 504990 | -87.87 | 14.32 | 69.85 | 0.04 | 2.24 | 1563 |
| 2024-09-20 22:21:37.689 | MS1 | 121.4656671938 | 31.1446286024 | 124 | 504990 | -89.84 | 8.04 | 64.43 | 0.15 | 2.13 | 1590 |
| 2024-09-20 22:21:38.407 | MS1 | 121.4656599449 | 31.1446237669 | 124 | 504990 | -90.22 | 10.11 | 80.29 | 0.10 | 2.10 | 1580 |
| 2024-09-20 22:21:39.447 | MS1 | 121.4656637606 | 31.1446245450 | 124 | 504990 | -91.86 | 10.59 | 89.11 | 0.09 | 2.66 | 1582 |
| 2024-09-20 22:21:40.194 | MS1 | 121.4656767654 | 31.1446303086 | 124 | 504990 | -92.73 | 7.07 | 519.96 | 0.16 | 2.85 | 1573 |
| 2024-09-20 22:21:41.482 | MS1 | 121.4656763032 | 31.1446378018 | 124 | 504990 | -89.73 | 10.11 | 307.99 | 0.04 | 2.85 | 1596 |
| 2024-09-20 22:21:42.326 | MS1 | 121.4656776226 | 31.1446317952 | 124 | 504990 | -93.22 | 11.80 | 337.71 | 0.03 | 2.53 | 1582 |

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
| 3229050 | 2 | 121.4732647350 | 31.1501829204 | 29 | 15 | 2 | 47.1 | TDD | 851 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3237822 | 1 | 121.4753618687 | 31.1540465833 | 173 | 9 | 5 | 16.3 | TDD | 569 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3240455 | 3 | 121.4758393105 | 31.1544505907 | 180 | 4 | 3 | 45.1 | TDD | 124 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3275526 | 4 | 121.4663968176 | 31.1454741235 | 131 | 3 | 5 | 35.7 | TDD | 793 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.878 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.896 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.003 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.003 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.716 | NREventA3 | measId:2;ServCellPCI:725;Se... |
| 2024-09-20 22:21:37.956 | NRHandoverAttempt | SourcePCI:725;SourceNR-ARFC... |
| 2024-09-20 22:21:37.996 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.008 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.134 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.134 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237822 | 1 | 10.9557 | 14.1496 | -114.7253 | 9.6700 | 116.5170 | 0.0113 | 0.0011 |
| 2024_09_20 22:00 | 3229050 | 2 | 13.8499 | 6.6838 | -115.9356 | 8.7531 | 107.9187 | 0.0067 | 0.0008 |
| 2024_09_20 22:00 | 3240455 | 3 | 90.0941 | 80.4292 | -116.0882 | 9.5045 | 93.1242 | 0.0102 | 0.0124 |
| 2024_09_20 22:00 | 3275526 | 4 | 14.8800 | 13.9905 | -114.4178 | 9.0348 | 164.9454 | 0.0057 | 0.0075 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416817_C532469D | 504990 | 124 | -88.4 | 504990 | 569 | -95.0 | 504990 | 851 | -99.9 | 504990 | 793 |
| MR_1774416817_3D5504D9 | 504990 | 124 | -86.1 | 504990 | 569 | -94.5 | 504990 | 851 | -101.0 | 504990 | 793 |
| MR_1774416817_03B26BA3 | 504990 | 124 | -86.1 | 504990 | 569 | -93.3 | 504990 | 851 | -102.4 | 504990 | 793 |
| MR_1774416817_8FE2930B | 504990 | 124 | -86.1 | 504990 | 569 | -94.7 | 504990 | 851 | -99.9 | 504990 | 793 |
| MR_1774416817_AC7774CD | 504990 | 124 | -85.9 | 504990 | 569 | -92.7 | 504990 | 851 | -101.2 | 504990 | 793 |
| MR_1774416817_4565D11C | 504990 | 124 | -85.7 | 504990 | 569 | -95.5 | 504990 | 851 | -101.4 | 504990 | 793 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 37: `8b1ccd46-7cc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8b1ccd46-7cca-465e-9c02-1862afaa907d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[37] topology](images/test_0037.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3212500_5 by 27 degrees
- `C2`: Increase transmission power for 3212500_5
- `C3`: Press down the tilt angle  of 3212500_5 by 3 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235327_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235327_2
- `C6`: Lift the tilt angle of 3235327_2 by 1 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease A3 Offset threshold for 3235327_2
- `C9`: Decrease transmission power for 3212500_5
- `C10`: Increase transmission power for 3235327_2
- `C11`: Press down the tilt angle of 3235327_2 by 1 degrees
- `C12`: Increase A3 Offset threshold for 3212500_5
- `C13`: Add neighbor relationship between 3235327_2 and 3212500_5
- `C14`: Add neighbor relationship between 3255243_8 and 3212500_5
- `C15`: Increase A3 Offset threshold for 3235327_2
- `C16`: Adjust the azimuth of 3235327_2 by 8 degrees
- `C17`: Decrease A3 Offset threshold for 3212500_5
- `C18`: Lift the tilt angle  of 3212500_5 by 3 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212500_5
- `C20`: Decrease transmission power for 3235327_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212500_5
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.898 | MS1 | 121.4656675479 | 31.1446356638 | 426 | 504990 | -95.38 | 10.09 | 536.66 | 0.01 | 2.55 | 1586 |
| 2024-09-20 22:21:32.604 | MS1 | 121.4656682396 | 31.1446285769 | 893 | 504990 | -93.83 | 13.53 | 341.50 | 0.17 | 2.48 | 1591 |
| 2024-09-20 22:21:33.532 | MS1 | 121.4656751635 | 31.1446280071 | 166 | 504990 | -93.01 | 10.34 | 552.19 | 0.07 | 2.19 | 1585 |
| 2024-09-20 22:21:34.318 | MS1 | 121.4656585637 | 31.1446324244 | 673 | 152650 | -95.75 | 4.53 | 65.39 | 0.18 | 1.81 | 927 |
| 2024-09-20 22:21:35.155 | MS1 | 121.4656668791 | 31.1446225537 | 739 | 152650 | -93.23 | 4.80 | 52.87 | 0.02 | 1.57 | 948 |
| 2024-09-20 22:21:36.826 | MS1 | 121.4656661253 | 31.1446250152 | 66 | 152650 | -93.46 | 7.77 | 42.09 | 0.10 | 1.82 | 959 |
| 2024-09-20 22:21:37.460 | MS1 | 121.4656749578 | 31.1446186413 | 216 | 152650 | -93.70 | 6.29 | 83.42 | 0.06 | 1.79 | 983 |
| 2024-09-20 22:21:38.839 | MS1 | 121.4656581796 | 31.1446360986 | 673 | 152650 | -96.11 | 5.78 | 54.48 | 0.07 | 1.96 | 991 |
| 2024-09-20 22:21:39.458 | MS1 | 121.4656685196 | 31.1446374439 | 739 | 152650 | -89.53 | 3.08 | 61.31 | 0.01 | 1.56 | 943 |
| 2024-09-20 22:21:40.782 | MS1 | 121.4656670729 | 31.1446372526 | 66 | 152650 | -96.87 | 7.21 | 93.23 | 0.06 | 2.32 | 1569 |
| 2024-09-20 22:21:41.563 | MS1 | 121.4656645245 | 31.1446308592 | 216 | 152650 | -87.40 | 5.93 | 84.69 | 0.19 | 2.88 | 1592 |
| 2024-09-20 22:21:42.390 | MS1 | 121.4656675928 | 31.1446348528 | 673 | 152650 | -87.11 | 6.07 | 58.23 | 0.01 | 2.56 | 1561 |

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
| 3212500 | 5 | 121.4643613787 | 31.1529349199 | 145 | 2 | 7 | 12.4 | TDD | 625 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3214706 | 4 | 121.4707607290 | 31.1486174072 | 110 | 13 | 4 | 14.0 | TDD | 143 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3235327 | 2 | 121.4680699507 | 31.1464715417 | 220 | 1 | 6 | 2.6 | TDD | 426 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3238857 | 1 | 121.4736513747 | 31.1452137092 | 187 | 14 | 0 | 1.1 | TDD | 166 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3244243 | 11 | 121.4684973108 | 31.1498186528 | 78 | 0 | 1 | 22.4 | FDD | 216 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3245212 | 7 | 121.4658273646 | 31.1478667575 | 47 | 13 | 0 | 25.2 | FDD | 673 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3251254 | 6 | 121.4721325157 | 31.1552680433 | 186 | 15 | 12 | 19.5 | TDD | 893 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3255243 | 8 | 121.4642328038 | 31.1482094392 | 34 | 6 | 2 | 3.3 | FDD | 66 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3256858 | 10 | 121.4679134862 | 31.1473250222 | 206 | 11 | 9 | 10.1 | FDD | 566 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3262809 | 12 | 121.4707762832 | 31.1443134029 | 307 | 6 | 6 | 28.6 | FDD | 348 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3272216 | 9 | 121.4727063373 | 31.1479933296 | 292 | 13 | 11 | 22.2 | FDD | 739 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3272837 | 3 | 121.4699631751 | 31.1544543641 | 286 | 3 | 0 | 16.3 | TDD | 942 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3279660 | 13 | 121.4702491644 | 31.1461533151 | 174 | 14 | 2 | 8.3 | FDD | 191 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |

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
| 2024-09-20 22:21:30.935 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.959 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.101 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.101 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.771 | NREventA2 | measId:1;ServCellPCI:564;Se... |
| 2024-09-20 22:21:34.878 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.119 | NREventA5 | measId:3;ServCellPCI:564;Se... |
| 2024-09-20 22:21:35.196 | NRHandoverAttempt | SourcePCI:564;SourceNR-ARFC... |
| 2024-09-20 22:21:35.240 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.250 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.371 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.371 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238857 | 1 | 6.5142 | 12.9243 | -115.5794 | 6.4094 | 101.3303 | 0.0156 | 0.0179 |
| 2024_09_20 22:00 | 3235327 | 2 | 16.9563 | 18.6226 | -114.4245 | 10.6562 | 122.5533 | 0.0023 | 0.0081 |
| 2024_09_20 22:00 | 3272837 | 3 | 9.8486 | 12.2631 | -115.4120 | 7.8830 | 83.0975 | 0.0137 | 0.0017 |
| 2024_09_20 22:00 | 3214706 | 4 | 6.6798 | 11.1189 | -117.7041 | 12.8201 | 157.1090 | 0.0091 | 0.0087 |
| 2024_09_20 22:00 | 3212500 | 5 | 15.6998 | 5.1937 | -115.4350 | 10.2373 | 81.1215 | 0.0028 | 0.0081 |
| 2024_09_20 22:00 | 3251254 | 6 | 12.1312 | 7.0528 | -116.2701 | 9.6149 | 168.2648 | 0.0037 | 0.0120 |
| 2024_09_20 22:00 | 3245212 | 7 | 15.4236 | 18.8173 | -116.0691 | 4.0277 | 23.5369 | 0.0042 | 0.0048 |
| 2024_09_20 22:00 | 3255243 | 8 | 18.2319 | 19.7881 | -117.4576 | 3.2229 | 24.0116 | 0.0017 | 0.0085 |
| 2024_09_20 22:00 | 3272216 | 9 | 11.9786 | 8.2480 | -114.9593 | 3.2685 | 23.7398 | 0.0169 | 0.0013 |
| 2024_09_20 22:00 | 3256858 | 10 | 6.6422 | 17.3385 | -114.3851 | 3.8141 | 41.3401 | 0.0105 | 0.0061 |
| 2024_09_20 22:00 | 3244243 | 11 | 8.5714 | 5.2669 | -114.0656 | 3.0341 | 30.3954 | 0.0141 | 0.0123 |
| 2024_09_20 22:00 | 3262809 | 12 | 5.4769 | 18.6564 | -114.4940 | 3.8135 | 51.9399 | 0.0164 | 0.0007 |
| 2024_09_20 22:00 | 3279660 | 13 | 7.8342 | 15.9212 | -114.7753 | 4.6335 | 26.9452 | 0.0143 | 0.0069 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414746_70980761 | 504990 | 166 | -93.8 | 504990 | 625 | -91.5 | 504990 | 942 | -97.1 | 504990 | 143 |
| MR_1774414746_85574CA1 | 504990 | 166 | -93.3 | 504990 | 625 | -93.7 | 504990 | 942 | -97.3 | 504990 | 143 |
| MR_1774414746_254E345D | 504990 | 166 | -91.3 | 504990 | 625 | -91.8 | 504990 | 942 | -98.2 | 504990 | 143 |
| MR_1774414746_D400E8F7 | 504990 | 166 | -94.5 | 504990 | 625 | -93.8 | 504990 | 942 | -97.3 | 504990 | 143 |
| MR_1774414746_3A905372 | 152650 | 673 | -94.6 | 152650 | 566 | -103.9 | 152650 | 191 | -107.5 | 152650 | 348 |
| MR_1774414746_78C83E9A | 504990 | 166 | -91.3 | 504990 | 625 | -91.3 | 504990 | 942 | -96.3 | 504990 | 143 |
| MR_1774414746_8AF6E73B | 152650 | 673 | -97.2 | 152650 | 566 | -102.8 | 152650 | 191 | -104.3 | 152650 | 348 |
| MR_1774414746_2610C6E2 | 152650 | 673 | -94.5 | 152650 | 566 | -101.5 | 152650 | 191 | -104.8 | 152650 | 348 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 38: `55477a77-37d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `55477a77-37d4-467a-9511-9f99866644b2` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[38] topology](images/test_0038.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278124_2
- `C2`: Adjust the azimuth of 3278124_2 by 28 degrees
- `C3`: Increase A3 Offset threshold for 3278124_2
- `C4`: Adjust the azimuth of 3227859_1 by 44 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278124_2
- `C6`: Press down the tilt angle of 3227859_1 by 10 degrees
- `C7`: Decrease A3 Offset threshold for 3278124_2
- `C8`: Lift the tilt angle of 3227859_1 by 10 degrees
- `C9`: Lift the tilt angle  of 3278124_2 by 10 degrees
- `C10`: Increase transmission power for 3227859_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227859_1
- `C12`: Add neighbor relationship between 3227859_1 and 3278124_2
- `C13`: Increase transmission power for 3278124_2
- `C14`: Increase A3 Offset threshold for 3227859_1
- `C15`: Press down the tilt angle  of 3278124_2 by 10 degrees
- `C16`: Decrease transmission power for 3278124_2
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227859_1
- `C19`: Decrease transmission power for 3227859_1
- `C20`: Decrease A3 Offset threshold for 3227859_1
- `C21`: Check test server and transmission issues
- `C22`: Add neighbor relationship between 3223580_4 and 3278124_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.641 | MS1 | 121.4656652818 | 31.1446276151 | 777 | 504990 | -90.98 | 14.77 | 302.60 | 0.10 | 2.54 | 1585 |
| 2024-09-20 22:21:32.625 | MS1 | 121.4656760785 | 31.1446272491 | 777 | 504990 | -88.90 | 16.26 | 365.70 | 0.07 | 2.88 | 1600 |
| 2024-09-20 22:21:33.178 | MS1 | 121.4656610867 | 31.1446328412 | 777 | 504990 | -86.53 | 13.95 | 534.91 | 0.10 | 2.48 | 1581 |
| 2024-09-20 22:21:34.859 | MS1 | 121.4656627256 | 31.1446235508 | 777 | 504990 | -91.87 | 17.24 | 53.72 | 0.11 | 2.91 | 1560 |
| 2024-09-20 22:21:35.474 | MS1 | 121.4656708449 | 31.1446321943 | 777 | 504990 | -90.04 | 13.75 | 78.99 | 0.04 | 2.32 | 1585 |
| 2024-09-20 22:21:36.237 | MS1 | 121.4656758383 | 31.1446232685 | 777 | 504990 | -86.94 | 17.43 | 92.73 | 0.04 | 2.73 | 1599 |
| 2024-09-20 22:21:37.205 | MS1 | 121.4656727972 | 31.1446253259 | 777 | 504990 | -91.27 | 11.10 | 103.39 | 0.11 | 2.16 | 1561 |
| 2024-09-20 22:21:38.383 | MS1 | 121.4656750916 | 31.1446300490 | 777 | 504990 | -89.78 | 12.19 | 90.38 | 0.05 | 2.18 | 1582 |
| 2024-09-20 22:21:39.486 | MS1 | 121.4656714593 | 31.1446293066 | 777 | 504990 | -92.12 | 7.96 | 88.09 | 0.12 | 2.15 | 1590 |
| 2024-09-20 22:21:40.979 | MS1 | 121.4656741922 | 31.1446339904 | 777 | 504990 | -93.43 | 10.46 | 441.43 | 0.12 | 2.60 | 1570 |
| 2024-09-20 22:21:41.293 | MS1 | 121.4656600557 | 31.1446257840 | 777 | 504990 | -92.61 | 12.58 | 571.77 | 0.16 | 2.66 | 1590 |
| 2024-09-20 22:21:42.869 | MS1 | 121.4656762250 | 31.1446309412 | 777 | 504990 | -91.99 | 12.79 | 407.42 | 0.20 | 2.35 | 1567 |

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
| 3223580 | 4 | 121.4676177202 | 31.1516301612 | 218 | 3 | 12 | 31.0 | TDD | 663 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3227859 | 1 | 121.4701711809 | 31.1447309183 | 224 | 6 | 9 | 34.6 | TDD | 777 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3275239 | 3 | 121.4709501634 | 31.1535744474 | 188 | 0 | 6 | 15.5 | TDD | 673 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3278124 | 2 | 121.4720432161 | 31.1510292357 | 248 | 13 | 1 | 34.7 | TDD | 975 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.343 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.358 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.499 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.499 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.208 | NREventA3 | measId:2;ServCellPCI:176;Se... |
| 2024-09-20 22:21:38.448 | NRHandoverAttempt | SourcePCI:176;SourceNR-ARFC... |
| 2024-09-20 22:21:38.484 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.498 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.629 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.629 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3227859 | 1 | 90.5319 | 88.4456 | -114.2078 | 15.8085 | 120.2597 | 0.0146 | 0.0010 |
| 2024_09_19 22:00 | 3278124 | 2 | 78.2851 | 82.2493 | -116.2904 | 9.5686 | 114.6929 | 0.0042 | 0.0172 |
| 2024_09_19 22:00 | 3275239 | 3 | 82.8170 | 79.1762 | -115.4509 | 11.7452 | 119.9981 | 0.0119 | 0.0046 |
| 2024_09_19 22:00 | 3223580 | 4 | 87.8266 | 92.8498 | -116.1944 | 13.7895 | 85.3320 | 0.0019 | 0.0025 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417031_96FAC555 | 504990 | 777 | -90.1 | 504990 | 975 | -98.8 | 504990 | 663 | -100.8 | 504990 | 673 |
| MR_1774417031_3E9BFC5C | 504990 | 777 | -93.1 | 504990 | 975 | -100.1 | 504990 | 663 | -102.6 | 504990 | 673 |
| MR_1774417031_4094FFCD | 504990 | 777 | -91.3 | 504990 | 975 | -102.4 | 504990 | 663 | -100.6 | 504990 | 673 |
| MR_1774417031_5E29446A | 504990 | 777 | -90.1 | 504990 | 975 | -100.3 | 504990 | 663 | -103.1 | 504990 | 673 |
| MR_1774417031_3E7690DD | 504990 | 777 | -91.4 | 504990 | 975 | -102.6 | 504990 | 663 | -99.4 | 504990 | 673 |
| MR_1774417031_37DADF31 | 504990 | 777 | -93.2 | 504990 | 975 | -101.8 | 504990 | 663 | -101.0 | 504990 | 673 |
| MR_1774417031_7CAC8295 | 504990 | 777 | -93.4 | 504990 | 975 | -100.4 | 504990 | 663 | -101.3 | 504990 | 673 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 39: `82e04c0a-479...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `82e04c0a-479d-4be8-a0eb-5456ad418b75` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[39] topology](images/test_0039.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234531_3
- `C2`: Increase transmission power for 3234531_3
- `C3`: Press down the tilt angle  of 3234531_3 by 5 degrees
- `C4`: Decrease A3 Offset threshold for 3234531_3
- `C5`: Lift the tilt angle  of 3234531_3 by 5 degrees
- `C6`: Adjust the azimuth of 3234531_3 by 24 degrees
- `C7`: Press down the tilt angle of 3255973_4 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234531_3
- `C9`: Decrease A3 Offset threshold for 3255973_4
- `C10`: Decrease transmission power for 3234531_3
- `C11`: Decrease transmission power for 3255973_4
- `C12`: Check test server and transmission issues
- `C13`: Increase A3 Offset threshold for 3255973_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255973_4
- `C15`: Increase transmission power for 3255973_4
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Lift the tilt angle of 3255973_4 by 10 degrees
- `C18`: Add neighbor relationship between 3255973_4 and 3234531_3
- `C19`: Add neighbor relationship between 3266763_1 and 3234531_3
- `C20`: Adjust the azimuth of 3255973_4 by 50 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255973_4
- `C22`: Increase A3 Offset threshold for 3234531_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.325 | MS1 | 121.4656705061 | 31.1446227311 | 238 | 504990 | -94.14 | 13.07 | 465.70 | 0.17 | 2.36 | 1590 |
| 2024-09-20 22:21:32.803 | MS1 | 121.4656630530 | 31.1446190620 | 238 | 504990 | -87.88 | 13.59 | 571.99 | 0.12 | 2.75 | 1566 |
| 2024-09-20 22:21:33.934 | MS1 | 121.4656721294 | 31.1446213451 | 238 | 504990 | -90.06 | 15.20 | 459.58 | 0.08 | 2.69 | 1573 |
| 2024-09-20 22:21:34.602 | MS1 | 121.4656742373 | 31.1446270638 | 238 | 504990 | -109.07 | 0.48 | 48.00 | 0.00 | 1.11 | 1599 |
| 2024-09-20 22:21:35.968 | MS1 | 121.4656683495 | 31.1446300007 | 238 | 504990 | -105.02 | -1.29 | 44.81 | 0.10 | 1.09 | 1568 |
| 2024-09-20 22:21:36.330 | MS1 | 121.4656657971 | 31.1446342784 | 238 | 504990 | -109.57 | 1.89 | 22.93 | 0.19 | 1.33 | 1590 |
| 2024-09-20 22:21:37.201 | MS1 | 121.4656617935 | 31.1446351488 | 238 | 504990 | -100.34 | 0.22 | 22.52 | 0.19 | 1.20 | 1590 |
| 2024-09-20 22:21:38.938 | MS1 | 121.4656641664 | 31.1446289861 | 238 | 504990 | -104.80 | -1.01 | 60.73 | 0.19 | 1.31 | 1574 |
| 2024-09-20 22:21:39.940 | MS1 | 121.4656772766 | 31.1446330272 | 238 | 504990 | -101.29 | 0.07 | 65.81 | 0.00 | 1.33 | 1592 |
| 2024-09-20 22:21:40.232 | MS1 | 121.4656735816 | 31.1446242627 | 238 | 504990 | -89.07 | 13.55 | 345.11 | 0.12 | 2.98 | 1572 |
| 2024-09-20 22:21:41.876 | MS1 | 121.4656779910 | 31.1446346317 | 238 | 504990 | -94.77 | 13.25 | 399.58 | 0.18 | 2.04 | 1560 |
| 2024-09-20 22:21:42.189 | MS1 | 121.4656688145 | 31.1446196910 | 238 | 504990 | -92.79 | 12.22 | 417.36 | 0.16 | 2.43 | 1561 |

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
| 3214123 | 2 | 121.4721786231 | 31.1517056053 | 58 | 14 | 5 | 42.5 | TDD | 556 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3234531 | 3 | 121.4723870681 | 31.1525190596 | 240 | 2 | 11 | 48.2 | TDD | 317 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3255973 | 4 | 121.4654477928 | 31.1536008035 | 107 | 15 | 2 | 38.4 | TDD | 238 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3266763 | 1 | 121.4674295142 | 31.1453474492 | 167 | 10 | 7 | 41.2 | TDD | 947 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.538 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.554 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.690 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.690 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.875 | NREventA2 | measId:1;ServCellPCI:698;Se... |
| 2024-09-20 22:21:35.009 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266763 | 1 | 8.6197 | 7.3099 | -117.5489 | 16.8230 | 101.2888 | 0.0150 | 0.0005 |
| 2024_09_20 22:00 | 3214123 | 2 | 5.5872 | 17.8717 | -116.4148 | 11.9715 | 127.1462 | 0.0081 | 0.0006 |
| 2024_09_20 22:00 | 3234531 | 3 | 7.0999 | 15.4561 | -116.4324 | 7.1111 | 93.7145 | 0.0003 | 0.0130 |
| 2024_09_20 22:00 | 3255973 | 4 | 9.8316 | 16.9478 | -117.0467 | 5.9448 | 184.9870 | 0.1222 | 0.0179 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416044_01AA49E7 | 504990 | 238 | -110.6 | 504990 | 317 | -112.5 | 504990 | 947 | -118.8 | 504990 | 556 |
| MR_1774416044_230943D4 | 504990 | 238 | -109.8 | 504990 | 317 | -111.7 | 504990 | 947 | -118.3 | 504990 | 556 |
| MR_1774416044_EB15D620 | 504990 | 238 | -107.1 | 504990 | 317 | -111.3 | 504990 | 947 | -118.6 | 504990 | 556 |
| MR_1774416044_A3A5A35A | 504990 | 238 | -110.4 | 504990 | 317 | -113.9 | 504990 | 947 | -119.2 | 504990 | 556 |
| MR_1774416044_06930AAB | 504990 | 238 | -107.8 | 504990 | 317 | -112.0 | 504990 | 947 | -116.9 | 504990 | 556 |
| MR_1774416044_17C6CA35 | 504990 | 238 | -107.2 | 504990 | 317 | -110.8 | 504990 | 947 | -119.3 | 504990 | 556 |

> *... 2개 열 생략 (전체 14열)*

---
