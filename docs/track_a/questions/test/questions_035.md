# Track A 문제 분석 — test[340]~test[349]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[340] ~ test[349] (10개)

## 목차

1. [문제 340: `41b6d944-0a9...`](#340) — single-answer
2. [문제 341: `04a262c3-c8e...`](#341) — single-answer
3. [문제 342: `0333cb46-4b4...`](#342) — single-answer
4. [문제 343: `aeef5efd-cdf...`](#343) — single-answer
5. [문제 344: `fba0b836-05b...`](#344) — single-answer
6. [문제 345: `374ba283-89a...`](#345) — single-answer
7. [문제 346: `d457e694-57f...`](#346) — single-answer
8. [문제 347: `f28753e3-1fd...`](#347) — multiple-answer
9. [문제 348: `453ce562-7d8...`](#348) — single-answer
10. [문제 349: `739c9d1a-6d9...`](#349) — single-answer

---

### 문제 340: `41b6d944-0a9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `41b6d944-0a96-411b-ad13-96453eccad8f` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[340] topology](images/test_0340.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3242487_1
- `C2`: Lift the tilt angle  of 3246716_2 by 8 degrees
- `C3`: Increase A3 Offset threshold for 3246716_2
- `C4`: Increase transmission power for 3246716_2
- `C5`: Adjust the azimuth of 3246716_2 by 50 degrees
- `C6`: Decrease A3 Offset threshold for 3246716_2
- `C7`: Add neighbor relationship between 3242487_1 and 3246716_2
- `C8`: Increase A3 Offset threshold for 3242487_1
- `C9`: Add neighbor relationship between 3266323_3 and 3246716_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Adjust the azimuth of 3242487_1 by 28 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246716_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242487_1
- `C14`: Lift the tilt angle of 3242487_1 by 5 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246716_2
- `C16`: Decrease transmission power for 3246716_2
- `C17`: Decrease A3 Offset threshold for 3242487_1
- `C18`: Check test server and transmission issues
- `C19`: Press down the tilt angle  of 3246716_2 by 8 degrees
- `C20`: Decrease transmission power for 3242487_1
- `C21`: Press down the tilt angle of 3242487_1 by 5 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242487_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.720 | MS1 | 121.4656774640 | 31.1446220157 | 883 | 504990 | -90.68 | 16.51 | 321.11 | 0.16 | 2.29 | 1582 |
| 2024-09-20 22:21:32.334 | MS1 | 121.4656588990 | 31.1446242777 | 883 | 504990 | -89.61 | 14.33 | 598.11 | 0.14 | 2.15 | 1593 |
| 2024-09-20 22:21:33.379 | MS1 | 121.4656736333 | 31.1446186345 | 883 | 504990 | -85.37 | 13.50 | 479.32 | 0.04 | 2.65 | 1566 |
| 2024-09-20 22:21:34.742 | MS1 | 121.4656775598 | 31.1446253919 | 883 | 504990 | -86.49 | 13.35 | 66.39 | 0.68 | 2.84 | 577 |
| 2024-09-20 22:21:35.378 | MS1 | 121.4656720641 | 31.1446279260 | 883 | 504990 | -91.26 | 12.29 | 51.04 | 0.68 | 2.09 | 624 |
| 2024-09-20 22:21:36.573 | MS1 | 121.4656646957 | 31.1446327071 | 883 | 504990 | -90.56 | 14.09 | 61.97 | 0.52 | 2.92 | 505 |
| 2024-09-20 22:21:37.377 | MS1 | 121.4656696944 | 31.1446246853 | 883 | 504990 | -89.51 | 12.05 | 72.48 | 0.53 | 2.75 | 641 |
| 2024-09-20 22:21:38.793 | MS1 | 121.4656671948 | 31.1446378075 | 883 | 504990 | -92.69 | 7.23 | 103.70 | 0.66 | 2.61 | 631 |
| 2024-09-20 22:21:39.858 | MS1 | 121.4656598692 | 31.1446220520 | 883 | 504990 | -91.01 | 7.09 | 93.95 | 0.59 | 2.41 | 504 |
| 2024-09-20 22:21:40.751 | MS1 | 121.4656771771 | 31.1446204272 | 883 | 504990 | -89.17 | 7.87 | 368.83 | 0.04 | 2.80 | 1564 |
| 2024-09-20 22:21:41.706 | MS1 | 121.4656609368 | 31.1446345702 | 883 | 504990 | -92.98 | 12.86 | 353.13 | 0.05 | 2.82 | 1572 |
| 2024-09-20 22:21:42.294 | MS1 | 121.4656609801 | 31.1446204463 | 883 | 504990 | -91.30 | 11.71 | 498.46 | 0.20 | 2.37 | 1594 |

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
| 3212707 | 4 | 121.4683239946 | 31.1548207106 | 162 | 2 | 2 | 43.0 | TDD | 542 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3242487 | 1 | 121.4758262567 | 31.1541603066 | 250 | 4 | 7 | 21.0 | TDD | 883 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3246716 | 2 | 121.4666820313 | 31.1552544195 | 103 | 7 | 7 | 24.3 | TDD | 907 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3266323 | 3 | 121.4701882269 | 31.1528609709 | 253 | 1 | 0 | 16.5 | TDD | 213 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.050 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.068 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.186 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.186 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.933 | NREventA3 | measId:2;ServCellPCI:176;Se... |
| 2024-09-20 22:21:38.173 | NRHandoverAttempt | SourcePCI:176;SourceNR-ARFC... |
| 2024-09-20 22:21:38.213 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.225 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.361 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.361 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242487 | 1 | 12.4738 | 11.7650 | -114.4519 | 12.0232 | 150.9348 | 0.0159 | 0.0128 |
| 2024_09_20 22:00 | 3246716 | 2 | 7.0619 | 11.2106 | -115.3843 | 18.6346 | 111.9077 | 0.0046 | 0.0122 |
| 2024_09_20 22:00 | 3266323 | 3 | 7.9233 | 9.9277 | -116.0563 | 18.6851 | 88.2174 | 0.0178 | 0.0141 |
| 2024_09_20 22:00 | 3212707 | 4 | 6.9614 | 14.3219 | -114.4088 | 17.7869 | 171.9615 | 0.0132 | 0.0178 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414237_64719131 | 504990 | 883 | -86.3 | 504990 | 907 | -89.5 | 504990 | 213 | -94.1 | 504990 | 542 |
| MR_1774414237_5F26455A | 504990 | 883 | -85.6 | 504990 | 907 | -88.7 | 504990 | 213 | -96.8 | 504990 | 542 |
| MR_1774414237_E9A3D10D | 504990 | 883 | -87.4 | 504990 | 907 | -88.3 | 504990 | 213 | -93.7 | 504990 | 542 |
| MR_1774414237_19A149F5 | 504990 | 883 | -87.2 | 504990 | 907 | -89.1 | 504990 | 213 | -94.8 | 504990 | 542 |
| MR_1774414237_A4061E01 | 504990 | 883 | -88.3 | 504990 | 907 | -88.6 | 504990 | 213 | -94.9 | 504990 | 542 |
| MR_1774414237_41573326 | 504990 | 883 | -86.7 | 504990 | 907 | -90.8 | 504990 | 213 | -95.6 | 504990 | 542 |
| MR_1774414237_9F4EDAA8 | 504990 | 883 | -88.2 | 504990 | 907 | -90.0 | 504990 | 213 | -96.2 | 504990 | 542 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 341: `04a262c3-c8e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `04a262c3-c8ea-4282-9e81-3857bd6d5871` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[341] topology](images/test_0341.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248163_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248163_2
- `C3`: Increase A3 Offset threshold for 3229286_1
- `C4`: Increase transmission power for 3248163_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229286_1
- `C6`: Add neighbor relationship between 3229286_1 and 3248163_2
- `C7`: Increase A3 Offset threshold for 3248163_2
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Press down the tilt angle of 3229286_1 by 9 degrees
- `C10`: Decrease transmission power for 3248163_2
- `C11`: Decrease A3 Offset threshold for 3248163_2
- `C12`: Press down the tilt angle  of 3248163_2 by 2 degrees
- `C13`: Adjust the azimuth of 3248163_2 by 1 degrees
- `C14`: Check test server and transmission issues
- `C15`: Lift the tilt angle  of 3248163_2 by 2 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229286_1
- `C17`: Add neighbor relationship between 3277285_3 and 3248163_2
- `C18`: Adjust the azimuth of 3229286_1 by 50 degrees
- `C19`: Increase transmission power for 3229286_1
- `C20`: Decrease transmission power for 3229286_1
- `C21`: Decrease A3 Offset threshold for 3229286_1
- `C22`: Lift the tilt angle of 3229286_1 by 9 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.400 | MS1 | 121.4656642994 | 31.1446324294 | 977 | 504990 | -78.50 | 13.19 | 317.50 | 0.11 | 2.96 | 1571 |
| 2024-09-20 22:21:32.556 | MS1 | 121.4656652901 | 31.1446200815 | 977 | 504990 | -75.62 | 12.84 | 585.53 | 0.06 | 2.23 | 1600 |
| 2024-09-20 22:21:33.732 | MS1 | 121.4656690604 | 31.1446203345 | 977 | 504990 | -75.53 | 13.74 | 326.76 | 0.11 | 2.06 | 1593 |
| 2024-09-20 22:21:34.242 | MS1 | 121.4656660747 | 31.1446235648 | 977 | 504990 | -92.53 | -3.51 | 37.46 | 0.17 | 1.49 | 1565 |
| 2024-09-20 22:21:35.862 | MS1 | 121.4656632060 | 31.1446326086 | 977 | 504990 | -85.84 | -2.33 | 59.93 | 0.04 | 1.39 | 1587 |
| 2024-09-20 22:21:36.979 | MS1 | 121.4656662042 | 31.1446342155 | 977 | 504990 | -87.48 | -1.71 | 53.54 | 0.15 | 1.45 | 1591 |
| 2024-09-20 22:21:37.373 | MS1 | 121.4656603812 | 31.1446221744 | 977 | 504990 | -86.94 | -2.19 | 45.80 | 0.03 | 1.38 | 1572 |
| 2024-09-20 22:21:38.982 | MS1 | 121.4656592879 | 31.1446288086 | 977 | 504990 | -80.09 | 15.77 | 577.55 | 0.11 | 1.21 | 1561 |
| 2024-09-20 22:21:39.567 | MS1 | 121.4656632184 | 31.1446290731 | 977 | 504990 | -82.20 | 13.72 | 578.58 | 0.10 | 1.26 | 1579 |
| 2024-09-20 22:21:40.477 | MS1 | 121.4656697953 | 31.1446227744 | 977 | 504990 | -84.78 | 12.73 | 319.00 | 0.08 | 2.08 | 1588 |
| 2024-09-20 22:21:41.352 | MS1 | 121.4656631690 | 31.1446246961 | 977 | 504990 | -75.65 | 16.45 | 331.60 | 0.05 | 2.07 | 1597 |
| 2024-09-20 22:21:42.330 | MS1 | 121.4656697812 | 31.1446216375 | 977 | 504990 | -77.17 | 15.40 | 538.91 | 0.18 | 2.29 | 1590 |

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
| 3229286 | 1 | 121.4716078521 | 31.1554816336 | 271 | 7 | 1 | 44.3 | TDD | 977 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3248163 | 2 | 121.4703882115 | 31.1523491697 | 209 | 0 | 7 | 31.7 | TDD | 971 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3264449 | 4 | 121.4677419668 | 31.1492933340 | 20 | 14 | 7 | 31.9 | TDD | 325 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3277285 | 3 | 121.4746211647 | 31.1529804195 | 55 | 13 | 5 | 24.5 | TDD | 852 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.369 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.388 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.520 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.520 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.175 | NREventA3 | measId:2;ServCellPCI:204;Se... |
| 2024-09-20 22:21:36.175 | NREventA3 | measId:2;ServCellPCI:204;Se... |
| 2024-09-20 22:21:37.175 | NREventA3 | measId:2;ServCellPCI:204;Se... |
| 2024-09-20 22:21:39.675 | NRRRCReestablishAttempt | PCI:204 |
| 2024-09-20 22:21:39.695 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.709 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.847 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.847 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229286 | 1 | 7.3425 | 6.9632 | -114.1531 | 19.3296 | 115.0483 | 0.0006 | 0.1428 |
| 2024_09_20 22:00 | 3248163 | 2 | 19.8506 | 6.2687 | -117.2591 | 18.4747 | 133.4302 | 0.0035 | 0.0189 |
| 2024_09_20 22:00 | 3277285 | 3 | 16.2497 | 9.5207 | -114.2687 | 10.3123 | 120.4950 | 0.0098 | 0.0004 |
| 2024_09_20 22:00 | 3264449 | 4 | 8.0538 | 14.9483 | -116.6614 | 9.7921 | 100.2787 | 0.0033 | 0.0071 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412995_0CFDA305 | 504990 | 971 | -87.6 | 504990 | 977 | -91.2 | 504990 | 852 | -92.9 | 504990 | 325 |
| MR_1774412995_1725B7D7 | 504990 | 971 | -89.1 | 504990 | 977 | -94.3 | 504990 | 852 | -91.5 | 504990 | 325 |
| MR_1774412995_A6177312 | 504990 | 971 | -86.1 | 504990 | 977 | -92.8 | 504990 | 852 | -94.1 | 504990 | 325 |
| MR_1774412995_30CF037A | 504990 | 971 | -87.0 | 504990 | 977 | -92.2 | 504990 | 852 | -91.7 | 504990 | 325 |
| MR_1774412995_8CD6F727 | 504990 | 977 | -93.7 | 504990 | 971 | -88.8 | 504990 | 852 | -90.3 | 504990 | 325 |
| MR_1774412995_AD5A2532 | 504990 | 977 | -91.5 | 504990 | 971 | -86.3 | 504990 | 852 | -92.2 | 504990 | 325 |
| MR_1774412995_678950EF | 504990 | 977 | -91.3 | 504990 | 971 | -88.1 | 504990 | 852 | -93.3 | 504990 | 325 |
| MR_1774412995_725C6458 | 504990 | 971 | -88.7 | 504990 | 977 | -92.4 | 504990 | 852 | -91.5 | 504990 | 325 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 342: `0333cb46-4b4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0333cb46-4b46-4732-b56e-7d0c26daf4c3` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[342] topology](images/test_0342.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3259623_2
- `C2`: Press down the tilt angle  of 3259623_2 by 10 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Add neighbor relationship between 3255392_3 and 3259623_2
- `C5`: Decrease A3 Offset threshold for 3256496_1
- `C6`: Decrease transmission power for 3256496_1
- `C7`: Adjust the azimuth of 3259623_2 by 50 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259623_2
- `C9`: Lift the tilt angle  of 3259623_2 by 10 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259623_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256496_1
- `C12`: Press down the tilt angle of 3256496_1 by 10 degrees
- `C13`: Check test server and transmission issues
- `C14`: Increase A3 Offset threshold for 3256496_1
- `C15`: Increase transmission power for 3256496_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256496_1
- `C17`: Decrease A3 Offset threshold for 3259623_2
- `C18`: Increase A3 Offset threshold for 3259623_2
- `C19`: Adjust the azimuth of 3256496_1 by 50 degrees
- `C20`: Lift the tilt angle of 3256496_1 by 10 degrees
- `C21`: Decrease transmission power for 3259623_2
- `C22`: Add neighbor relationship between 3256496_1 and 3259623_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.191 | MS1 | 121.4656719342 | 31.1446183922 | 305 | 504990 | -83.06 | 14.09 | 365.20 | 0.19 | 2.78 | 1585 |
| 2024-09-20 22:21:32.240 | MS1 | 121.4656661253 | 31.1446199115 | 305 | 504990 | -80.25 | 15.30 | 471.34 | 0.04 | 2.86 | 1572 |
| 2024-09-20 22:21:33.682 | MS1 | 121.4656747891 | 31.1446230527 | 305 | 504990 | -78.08 | 17.03 | 473.40 | 0.01 | 2.24 | 1579 |
| 2024-09-20 22:21:34.450 | MS1 | 121.4656626756 | 31.1446351709 | 305 | 504990 | -88.14 | -2.04 | 55.76 | 0.14 | 1.41 | 1572 |
| 2024-09-20 22:21:35.125 | MS1 | 121.4656773903 | 31.1446213900 | 305 | 504990 | -85.88 | -1.63 | 27.13 | 0.14 | 1.34 | 1575 |
| 2024-09-20 22:21:36.326 | MS1 | 121.4656709540 | 31.1446206189 | 305 | 504990 | -85.89 | -1.20 | 60.74 | 0.17 | 1.14 | 1566 |
| 2024-09-20 22:21:37.766 | MS1 | 121.4656687083 | 31.1446269653 | 305 | 504990 | -91.88 | -1.69 | 37.42 | 0.18 | 1.47 | 1591 |
| 2024-09-20 22:21:38.583 | MS1 | 121.4656638698 | 31.1446315948 | 305 | 504990 | -85.34 | -1.94 | 53.44 | 0.18 | 1.09 | 1572 |
| 2024-09-20 22:21:39.575 | MS1 | 121.4656652238 | 31.1446190592 | 988 | 504990 | -78.65 | 14.25 | 163.93 | 0.18 | 1.02 | 1586 |
| 2024-09-20 22:21:40.606 | MS1 | 121.4656695449 | 31.1446372528 | 988 | 504990 | -84.92 | 14.20 | 546.87 | 0.08 | 2.91 | 1591 |
| 2024-09-20 22:21:41.850 | MS1 | 121.4656691609 | 31.1446199311 | 988 | 504990 | -84.28 | 13.55 | 385.50 | 0.15 | 2.29 | 1561 |
| 2024-09-20 22:21:42.361 | MS1 | 121.4656594796 | 31.1446271305 | 988 | 504990 | -78.96 | 15.33 | 430.91 | 0.13 | 2.07 | 1589 |

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
| 3255392 | 3 | 121.4684577319 | 31.1451214325 | 292 | 8 | 4 | 42.2 | TDD | 389 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3256496 | 1 | 121.4678275096 | 31.1447547863 | 167 | 8 | 3 | 21.7 | TDD | 305 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3259623 | 2 | 121.4642451289 | 31.1457019042 | 358 | 8 | 12 | 22.9 | TDD | 988 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3277322 | 4 | 121.4714335100 | 31.1515183058 | 206 | 15 | 10 | 32.5 | TDD | 801 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.492 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.514 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.620 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.620 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.294 | NREventA3 | measId:2;ServCellPCI:356;Se... |
| 2024-09-20 22:21:38.534 | NRHandoverAttempt | SourcePCI:356;SourceNR-ARFC... |
| 2024-09-20 22:21:38.572 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.585 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.728 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.728 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256496 | 1 | 7.0049 | 17.7952 | -114.3774 | 17.0946 | 176.2674 | 0.0030 | 0.1098 |
| 2024_09_20 22:00 | 3259623 | 2 | 5.3625 | 10.9001 | -114.2253 | 6.7005 | 116.4609 | 0.0120 | 0.0119 |
| 2024_09_20 22:00 | 3255392 | 3 | 18.8629 | 13.9085 | -114.1948 | 16.1515 | 86.5881 | 0.0004 | 0.0094 |
| 2024_09_20 22:00 | 3277322 | 4 | 16.0029 | 17.6557 | -114.0771 | 12.7174 | 82.8856 | 0.0085 | 0.0182 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415298_279EECD6 | 504990 | 988 | -81.5 | 504990 | 305 | -89.4 | 504990 | 389 | -81.9 | 504990 | 801 |
| MR_1774415298_1EE111A9 | 504990 | 988 | -83.9 | 504990 | 305 | -87.7 | 504990 | 389 | -83.0 | 504990 | 801 |
| MR_1774415298_8ED553A7 | 504990 | 988 | -82.5 | 504990 | 305 | -89.1 | 504990 | 389 | -82.3 | 504990 | 801 |
| MR_1774415298_4DD0436C | 504990 | 988 | -82.9 | 504990 | 305 | -90.0 | 504990 | 389 | -83.4 | 504990 | 801 |
| MR_1774415298_969557C4 | 504990 | 988 | -81.1 | 504990 | 305 | -88.8 | 504990 | 389 | -82.2 | 504990 | 801 |
| MR_1774415298_D78A3CE5 | 504990 | 305 | -86.5 | 504990 | 988 | -81.6 | 504990 | 389 | -83.5 | 504990 | 801 |
| MR_1774415298_74612B7E | 504990 | 305 | -88.2 | 504990 | 988 | -81.5 | 504990 | 389 | -83.2 | 504990 | 801 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 343: `aeef5efd-cdf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `aeef5efd-cdf4-48ab-be26-e7a00241d653` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[343] topology](images/test_0343.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3217965_3 by 5 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263788_4
- `C3`: Adjust the azimuth of 3263788_4 by 50 degrees
- `C4`: Increase A3 Offset threshold for 3263788_4
- `C5`: Check test server and transmission issues
- `C6`: Add neighbor relationship between 3263788_4 and 3217965_3
- `C7`: Decrease A3 Offset threshold for 3217965_3
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Press down the tilt angle of 3263788_4 by 9 degrees
- `C10`: Lift the tilt angle of 3263788_4 by 9 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217965_3
- `C12`: Decrease transmission power for 3263788_4
- `C13`: Decrease transmission power for 3217965_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217965_3
- `C15`: Increase transmission power for 3263788_4
- `C16`: Lift the tilt angle  of 3217965_3 by 5 degrees
- `C17`: Decrease A3 Offset threshold for 3263788_4
- `C18`: Increase A3 Offset threshold for 3217965_3
- `C19`: Adjust the azimuth of 3217965_3 by 50 degrees
- `C20`: Add neighbor relationship between 3264706_2 and 3217965_3
- `C21`: Increase transmission power for 3217965_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263788_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.125 | MS1 | 121.4656607023 | 31.1446243515 | 718 | 504990 | -82.80 | 15.15 | 410.97 | 0.08 | 2.52 | 1587 |
| 2024-09-20 22:21:32.800 | MS1 | 121.4656661067 | 31.1446361125 | 718 | 504990 | -83.24 | 17.14 | 573.63 | 0.09 | 2.68 | 1591 |
| 2024-09-20 22:21:33.416 | MS1 | 121.4656734972 | 31.1446316499 | 718 | 504990 | -78.77 | 17.30 | 467.91 | 0.19 | 2.44 | 1595 |
| 2024-09-20 22:21:34.374 | MS1 | 121.4656648293 | 31.1446193393 | 718 | 504990 | -85.06 | -3.87 | 66.28 | 0.08 | 1.24 | 1578 |
| 2024-09-20 22:21:35.737 | MS1 | 121.4656682422 | 31.1446318810 | 718 | 504990 | -85.72 | -2.54 | 31.50 | 0.09 | 1.11 | 1581 |
| 2024-09-20 22:21:36.872 | MS1 | 121.4656587653 | 31.1446246987 | 718 | 504990 | -86.89 | -3.59 | 69.41 | 0.13 | 1.14 | 1575 |
| 2024-09-20 22:21:37.596 | MS1 | 121.4656593749 | 31.1446271925 | 718 | 504990 | -84.22 | -1.49 | 50.34 | 0.05 | 1.08 | 1596 |
| 2024-09-20 22:21:38.639 | MS1 | 121.4656651513 | 31.1446250523 | 718 | 504990 | -88.11 | -3.09 | 39.69 | 0.16 | 1.41 | 1595 |
| 2024-09-20 22:21:39.951 | MS1 | 121.4656592007 | 31.1446368834 | 836 | 504990 | -77.67 | 13.35 | 261.21 | 0.16 | 1.50 | 1599 |
| 2024-09-20 22:21:40.475 | MS1 | 121.4656658915 | 31.1446233523 | 836 | 504990 | -76.30 | 13.55 | 591.98 | 0.06 | 2.63 | 1583 |
| 2024-09-20 22:21:41.977 | MS1 | 121.4656639063 | 31.1446257363 | 836 | 504990 | -81.66 | 16.00 | 587.64 | 0.16 | 2.98 | 1560 |
| 2024-09-20 22:21:42.833 | MS1 | 121.4656711796 | 31.1446305706 | 836 | 504990 | -84.39 | 16.10 | 474.02 | 0.09 | 2.28 | 1595 |

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
| 3217965 | 3 | 121.4640646409 | 31.1502296323 | 324 | 1 | 3 | 43.3 | TDD | 836 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3233762 | 1 | 121.4645538534 | 31.1453280113 | 173 | 9 | 5 | 19.0 | TDD | 976 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3263788 | 4 | 121.4753152624 | 31.1455962967 | 4 | 7 | 11 | 35.0 | TDD | 718 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3264706 | 2 | 121.4726625431 | 31.1555967800 | 25 | 1 | 4 | 49.5 | TDD | 835 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.623 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.647 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.751 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.751 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.426 | NREventA3 | measId:2;ServCellPCI:230;Se... |
| 2024-09-20 22:21:38.666 | NRHandoverAttempt | SourcePCI:230;SourceNR-ARFC... |
| 2024-09-20 22:21:38.709 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.719 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.819 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.819 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233762 | 1 | 12.3299 | 10.7349 | -115.6207 | 7.6021 | 142.5260 | 0.0176 | 0.0057 |
| 2024_09_20 22:00 | 3264706 | 2 | 12.7455 | 15.8942 | -116.4873 | 5.7854 | 148.4444 | 0.0200 | 0.0153 |
| 2024_09_20 22:00 | 3217965 | 3 | 7.2093 | 11.3656 | -117.5118 | 19.7831 | 189.4633 | 0.0191 | 0.0056 |
| 2024_09_20 22:00 | 3263788 | 4 | 11.6114 | 17.0803 | -116.6951 | 7.2117 | 146.7991 | 0.0178 | 0.1142 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413739_E046487D | 504990 | 836 | -79.9 | 504990 | 718 | -84.1 | 504990 | 835 | -86.5 | 504990 | 976 |
| MR_1774413739_574ED8DB | 504990 | 718 | -84.0 | 504990 | 836 | -77.8 | 504990 | 835 | -88.7 | 504990 | 976 |
| MR_1774413739_5DD5EB3C | 504990 | 718 | -84.9 | 504990 | 836 | -78.4 | 504990 | 835 | -87.6 | 504990 | 976 |
| MR_1774413739_1E9EBF12 | 504990 | 718 | -86.1 | 504990 | 836 | -80.1 | 504990 | 835 | -87.5 | 504990 | 976 |
| MR_1774413739_429027CB | 504990 | 836 | -78.0 | 504990 | 718 | -83.1 | 504990 | 835 | -87.7 | 504990 | 976 |
| MR_1774413739_0D69680A | 504990 | 836 | -77.6 | 504990 | 718 | -85.8 | 504990 | 835 | -89.1 | 504990 | 976 |
| MR_1774413739_2D2119F7 | 504990 | 836 | -78.8 | 504990 | 718 | -83.4 | 504990 | 835 | -86.9 | 504990 | 976 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 344: `fba0b836-05b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fba0b836-05b4-46ff-86f0-b5f98261a3fc` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[344] topology](images/test_0344.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228188_2
- `C2`: Lift the tilt angle  of 3224623_1 by 2 degrees
- `C3`: Adjust the azimuth of 3228188_2 by 27 degrees
- `C4`: Adjust the azimuth of 3224623_1 by 50 degrees
- `C5`: Lift the tilt angle of 3228188_2 by 8 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224623_1
- `C7`: Check test server and transmission issues
- `C8`: Increase A3 Offset threshold for 3228188_2
- `C9`: Decrease transmission power for 3224623_1
- `C10`: Increase transmission power for 3228188_2
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Press down the tilt angle of 3228188_2 by 8 degrees
- `C13`: Decrease transmission power for 3228188_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228188_2
- `C15`: Add neighbor relationship between 3245118_3 and 3224623_1
- `C16`: Decrease A3 Offset threshold for 3224623_1
- `C17`: Add neighbor relationship between 3228188_2 and 3224623_1
- `C18`: Increase A3 Offset threshold for 3224623_1
- `C19`: Decrease A3 Offset threshold for 3228188_2
- `C20`: Increase transmission power for 3224623_1
- `C21`: Press down the tilt angle  of 3224623_1 by 2 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224623_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.234 | MS1 | 121.4656653733 | 31.1446217814 | 929 | 504990 | -90.17 | 15.54 | 413.27 | 0.14 | 2.74 | 1575 |
| 2024-09-20 22:21:32.142 | MS1 | 121.4656738652 | 31.1446338583 | 929 | 504990 | -86.35 | 12.98 | 578.98 | 0.01 | 2.35 | 1593 |
| 2024-09-20 22:21:33.980 | MS1 | 121.4656588498 | 31.1446287889 | 929 | 504990 | -87.79 | 16.85 | 370.17 | 0.07 | 2.17 | 1579 |
| 2024-09-20 22:21:34.512 | MS1 | 121.4656612979 | 31.1446221491 | 929 | 504990 | -85.68 | 14.91 | 80.17 | 0.13 | 2.45 | 413 |
| 2024-09-20 22:21:35.505 | MS1 | 121.4656709219 | 31.1446215578 | 929 | 504990 | -85.60 | 14.05 | 92.73 | 0.10 | 2.45 | 480 |
| 2024-09-20 22:21:36.596 | MS1 | 121.4656702447 | 31.1446253362 | 929 | 504990 | -88.21 | 13.55 | 84.75 | 0.02 | 2.44 | 489 |
| 2024-09-20 22:21:37.133 | MS1 | 121.4656710425 | 31.1446312640 | 929 | 504990 | -92.91 | 9.69 | 100.67 | 0.00 | 2.94 | 329 |
| 2024-09-20 22:21:38.426 | MS1 | 121.4656660516 | 31.1446233792 | 929 | 504990 | -89.47 | 12.28 | 67.44 | 0.00 | 2.82 | 496 |
| 2024-09-20 22:21:39.199 | MS1 | 121.4656710311 | 31.1446267332 | 929 | 504990 | -90.99 | 8.27 | 58.49 | 0.07 | 2.29 | 364 |
| 2024-09-20 22:21:40.310 | MS1 | 121.4656596250 | 31.1446276433 | 929 | 504990 | -89.03 | 9.76 | 399.91 | 0.02 | 2.49 | 1571 |
| 2024-09-20 22:21:41.135 | MS1 | 121.4656605415 | 31.1446268626 | 929 | 504990 | -90.50 | 10.58 | 511.12 | 0.08 | 2.38 | 1597 |
| 2024-09-20 22:21:42.207 | MS1 | 121.4656735150 | 31.1446225281 | 929 | 504990 | -89.76 | 8.49 | 550.43 | 0.03 | 2.23 | 1584 |

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
| 3210850 | 4 | 121.4748468257 | 31.1447212225 | 103 | 3 | 1 | 24.3 | TDD | 326 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3224623 | 1 | 121.4681760265 | 31.1539769780 | 94 | 0 | 4 | 31.8 | TDD | 833 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3228188 | 2 | 121.4670795357 | 31.1557159168 | 159 | 6 | 7 | 34.5 | TDD | 929 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3245118 | 3 | 121.4658286734 | 31.1514572718 | 257 | 12 | 5 | 20.5 | TDD | 918 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.843 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.948 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.948 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.689 | NREventA3 | measId:2;ServCellPCI:541;Se... |
| 2024-09-20 22:21:37.929 | NRHandoverAttempt | SourcePCI:541;SourceNR-ARFC... |
| 2024-09-20 22:21:37.962 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.976 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.120 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.120 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224623 | 1 | 9.2930 | 13.9325 | -117.9334 | 9.9295 | 160.9743 | 0.0092 | 0.0190 |
| 2024_09_20 22:00 | 3228188 | 2 | 12.1474 | 16.3694 | -116.3902 | 18.6634 | 196.9065 | 0.0067 | 0.0165 |
| 2024_09_20 22:00 | 3245118 | 3 | 14.0467 | 9.6110 | -117.5217 | 5.4046 | 126.5625 | 0.0140 | 0.0060 |
| 2024_09_20 22:00 | 3210850 | 4 | 12.2733 | 18.0545 | -114.3190 | 19.0145 | 155.5866 | 0.0125 | 0.0139 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412912_7F28B819 | 504990 | 929 | -86.2 | 504990 | 833 | -90.7 | 504990 | 918 | -96.9 | 504990 | 326 |
| MR_1774412912_224CB120 | 504990 | 929 | -84.0 | 504990 | 833 | -90.2 | 504990 | 918 | -95.1 | 504990 | 326 |
| MR_1774412912_16C68D6C | 504990 | 929 | -84.2 | 504990 | 833 | -89.6 | 504990 | 918 | -96.2 | 504990 | 326 |
| MR_1774412912_C265D22F | 504990 | 929 | -85.4 | 504990 | 833 | -90.5 | 504990 | 918 | -96.1 | 504990 | 326 |
| MR_1774412912_71B49654 | 504990 | 929 | -84.5 | 504990 | 833 | -90.7 | 504990 | 918 | -95.4 | 504990 | 326 |
| MR_1774412912_015844D3 | 504990 | 929 | -84.2 | 504990 | 833 | -89.3 | 504990 | 918 | -96.3 | 504990 | 326 |
| MR_1774412912_8683B8C1 | 504990 | 929 | -86.4 | 504990 | 833 | -89.7 | 504990 | 918 | -94.2 | 504990 | 326 |
| MR_1774412912_F165D770 | 504990 | 929 | -86.5 | 504990 | 833 | -87.8 | 504990 | 918 | -97.7 | 504990 | 326 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 345: `374ba283-89a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `374ba283-89a9-4eb1-a2cf-db324ae82aef` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[345] topology](images/test_0345.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3261297_2
- `C2`: Increase A3 Offset threshold for 3261297_2
- `C3`: Lift the tilt angle of 3271299_4 by 3 degrees
- `C4`: Lift the tilt angle  of 3237287_1 by 10 degrees
- `C5`: Add neighbor relationship between 3271299_4 and 3261297_2
- `C6`: Add neighbor relationship between 3237287_1 and 3261297_2
- `C7`: Increase transmission power for 3271299_4
- `C8`: Increase transmission power for 3261297_2
- `C9`: Press down the tilt angle of 3271299_4 by 3 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261297_2
- `C11`: Decrease transmission power for 3261297_2
- `C12`: Decrease A3 Offset threshold for 3271299_4
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Adjust the azimuth of 3237287_1 by 50 degrees
- `C15`: Check test server and transmission issues
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271299_4
- `C17`: Adjust the azimuth of 3271299_4 by 31 degrees
- `C18`: Press down the tilt angle  of 3237287_1 by 10 degrees
- `C19`: Decrease transmission power for 3271299_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271299_4
- `C21`: Increase A3 Offset threshold for 3271299_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261297_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.521 | MS1 | 121.4656740119 | 31.1446310343 | 676 | 504990 | -89.13 | 16.28 | 446.56 | 0.09 | 2.62 | 1593 |
| 2024-09-20 22:21:32.360 | MS1 | 121.4656744014 | 31.1446358246 | 676 | 504990 | -87.14 | 16.06 | 331.29 | 0.07 | 2.58 | 1567 |
| 2024-09-20 22:21:33.943 | MS1 | 121.4656737022 | 31.1446356004 | 676 | 504990 | -85.85 | 12.91 | 296.61 | 0.19 | 2.02 | 1594 |
| 2024-09-20 22:21:34.270 | MS1 | 121.4656645756 | 31.1446375751 | 676 | 504990 | -85.01 | 17.50 | 69.88 | 0.07 | 2.57 | 1596 |
| 2024-09-20 22:21:35.223 | MS1 | 121.4656625837 | 31.1446227431 | 676 | 504990 | -91.15 | 17.27 | 51.27 | 0.15 | 2.19 | 1564 |
| 2024-09-20 22:21:36.542 | MS1 | 121.4656695852 | 31.1446340813 | 676 | 504990 | -91.16 | 12.86 | 73.70 | 0.15 | 2.53 | 1586 |
| 2024-09-20 22:21:37.522 | MS1 | 121.4656611935 | 31.1446301870 | 676 | 504990 | -90.45 | 7.42 | 63.89 | 0.15 | 2.34 | 1577 |
| 2024-09-20 22:21:38.878 | MS1 | 121.4656719580 | 31.1446351883 | 676 | 504990 | -90.17 | 9.18 | 82.19 | 0.09 | 2.01 | 1585 |
| 2024-09-20 22:21:39.576 | MS1 | 121.4656644527 | 31.1446305674 | 676 | 504990 | -91.69 | 9.28 | 82.76 | 0.11 | 2.94 | 1587 |
| 2024-09-20 22:21:40.382 | MS1 | 121.4656761998 | 31.1446370286 | 676 | 504990 | -90.43 | 7.97 | 333.28 | 0.19 | 2.93 | 1596 |
| 2024-09-20 22:21:41.634 | MS1 | 121.4656650945 | 31.1446231563 | 676 | 504990 | -89.67 | 10.48 | 430.15 | 0.17 | 2.72 | 1564 |
| 2024-09-20 22:21:42.288 | MS1 | 121.4656729225 | 31.1446205085 | 676 | 504990 | -93.10 | 9.69 | 579.70 | 0.05 | 2.27 | 1563 |

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
| 3237287 | 1 | 121.4685640672 | 31.1445066274 | 98 | 10 | 5 | 46.6 | TDD | 264 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3261297 | 2 | 121.4713511912 | 31.1462553669 | 50 | 14 | 7 | 36.7 | TDD | 650 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3271299 | 4 | 121.4759913644 | 31.1540696155 | 254 | 2 | 8 | 29.0 | TDD | 676 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3277284 | 3 | 121.4745859818 | 31.1488523988 | 351 | 0 | 6 | 49.2 | TDD | 304 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.973 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.997 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.136 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.136 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.865 | NREventA3 | measId:2;ServCellPCI:942;Se... |
| 2024-09-20 22:21:38.105 | NRHandoverAttempt | SourcePCI:942;SourceNR-ARFC... |
| 2024-09-20 22:21:38.146 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.156 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.295 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.295 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237287 | 1 | 14.9975 | 12.6205 | -117.0681 | 9.3123 | 83.1998 | 0.0126 | 0.0184 |
| 2024_09_20 22:00 | 3261297 | 2 | 17.6583 | 17.2737 | -116.9036 | 14.3185 | 98.2810 | 0.0148 | 0.0072 |
| 2024_09_20 22:00 | 3277284 | 3 | 15.5243 | 19.9765 | -114.6064 | 18.3337 | 94.2632 | 0.0077 | 0.0022 |
| 2024_09_20 22:00 | 3271299 | 4 | 87.9271 | 92.3697 | -114.7647 | 10.1003 | 159.4054 | 0.0026 | 0.0059 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414839_2B390E64 | 504990 | 676 | -83.9 | 504990 | 650 | -87.7 | 504990 | 264 | -93.8 | 504990 | 304 |
| MR_1774414839_DCEE94BB | 504990 | 676 | -83.2 | 504990 | 650 | -88.8 | 504990 | 264 | -95.9 | 504990 | 304 |
| MR_1774414839_71BBEF9A | 504990 | 676 | -85.2 | 504990 | 650 | -89.7 | 504990 | 264 | -93.0 | 504990 | 304 |
| MR_1774414839_304CA68F | 504990 | 676 | -84.4 | 504990 | 650 | -87.2 | 504990 | 264 | -94.5 | 504990 | 304 |
| MR_1774414839_EEEDEDE0 | 504990 | 676 | -83.3 | 504990 | 650 | -89.9 | 504990 | 264 | -94.8 | 504990 | 304 |
| MR_1774414839_30BD33A4 | 504990 | 676 | -86.2 | 504990 | 650 | -89.5 | 504990 | 264 | -95.5 | 504990 | 304 |
| MR_1774414839_4A9A7399 | 504990 | 676 | -86.1 | 504990 | 650 | -90.5 | 504990 | 264 | -93.5 | 504990 | 304 |
| MR_1774414839_2E60AC12 | 504990 | 676 | -83.6 | 504990 | 650 | -88.8 | 504990 | 264 | -94.9 | 504990 | 304 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 346: `d457e694-57f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d457e694-57ff-4e93-9d32-eb01a93237a8` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[346] topology](images/test_0346.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3246426_1 and 3223559_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223559_2
- `C3`: Increase transmission power for 3210485_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210485_3
- `C5`: Add neighbor relationship between 3210485_3 and 3223559_2
- `C6`: Decrease A3 Offset threshold for 3223559_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223559_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210485_3
- `C9`: Decrease A3 Offset threshold for 3210485_3
- `C10`: Increase transmission power for 3223559_2
- `C11`: Lift the tilt angle of 3210485_3 by 10 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease transmission power for 3210485_3
- `C14`: Press down the tilt angle  of 3223559_2 by 6 degrees
- `C15`: Check test server and transmission issues
- `C16`: Increase A3 Offset threshold for 3210485_3
- `C17`: Adjust the azimuth of 3210485_3 by 50 degrees
- `C18`: Adjust the azimuth of 3223559_2 by 10 degrees
- `C19`: Press down the tilt angle of 3210485_3 by 10 degrees
- `C20`: Decrease transmission power for 3223559_2
- `C21`: Increase A3 Offset threshold for 3223559_2
- `C22`: Lift the tilt angle  of 3223559_2 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.343 | MS1 | 121.4656634979 | 31.1446302332 | 844 | 504990 | -91.53 | 13.08 | 400.55 | 0.17 | 2.37 | 1570 |
| 2024-09-20 22:21:32.585 | MS1 | 121.4656608975 | 31.1446309367 | 844 | 504990 | -90.30 | 13.00 | 561.06 | 0.09 | 2.04 | 1577 |
| 2024-09-20 22:21:33.463 | MS1 | 121.4656729193 | 31.1446263893 | 844 | 504990 | -88.64 | 14.47 | 383.48 | 0.12 | 2.98 | 1578 |
| 2024-09-20 22:21:34.483 | MS1 | 121.4656676168 | 31.1446225328 | 844 | 504990 | -85.94 | 13.29 | 64.84 | 0.01 | 2.18 | 1586 |
| 2024-09-20 22:21:35.478 | MS1 | 121.4656722767 | 31.1446353358 | 844 | 504990 | -86.58 | 16.81 | 79.86 | 0.04 | 2.70 | 1585 |
| 2024-09-20 22:21:36.155 | MS1 | 121.4656778541 | 31.1446302887 | 844 | 504990 | -86.16 | 16.38 | 96.88 | 0.06 | 2.17 | 1596 |
| 2024-09-20 22:21:37.953 | MS1 | 121.4656605385 | 31.1446194005 | 844 | 504990 | -93.92 | 10.11 | 56.51 | 0.04 | 2.16 | 1584 |
| 2024-09-20 22:21:38.176 | MS1 | 121.4656761797 | 31.1446182742 | 844 | 504990 | -93.64 | 10.92 | 78.05 | 0.17 | 2.36 | 1588 |
| 2024-09-20 22:21:39.629 | MS1 | 121.4656679224 | 31.1446257694 | 844 | 504990 | -92.58 | 8.53 | 56.53 | 0.05 | 2.70 | 1588 |
| 2024-09-20 22:21:40.169 | MS1 | 121.4656594211 | 31.1446195648 | 844 | 504990 | -93.90 | 10.22 | 345.31 | 0.01 | 2.61 | 1568 |
| 2024-09-20 22:21:41.387 | MS1 | 121.4656600908 | 31.1446346588 | 844 | 504990 | -92.27 | 9.93 | 356.36 | 0.07 | 2.58 | 1587 |
| 2024-09-20 22:21:42.524 | MS1 | 121.4656609549 | 31.1446326835 | 844 | 504990 | -93.31 | 8.37 | 584.83 | 0.07 | 2.62 | 1565 |

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
| 3210485 | 3 | 121.4658006309 | 31.1444652628 | 77 | 8 | 7 | 49.7 | TDD | 844 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3223559 | 2 | 121.4752103189 | 31.1510838087 | 242 | 4 | 10 | 44.9 | TDD | 674 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3246426 | 1 | 121.4759023181 | 31.1442965216 | 230 | 15 | 10 | 15.6 | TDD | 808 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3257095 | 4 | 121.4670962470 | 31.1465462799 | 269 | 9 | 12 | 18.1 | TDD | 554 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.338 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.356 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.481 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.481 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.209 | NREventA3 | measId:2;ServCellPCI:387;Se... |
| 2024-09-20 22:21:38.449 | NRHandoverAttempt | SourcePCI:387;SourceNR-ARFC... |
| 2024-09-20 22:21:38.491 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.502 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.652 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.652 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3246426 | 1 | 81.7439 | 78.8995 | -117.6899 | 14.5324 | 147.9686 | 0.0130 | 0.0004 |
| 2024_09_19 22:00 | 3223559 | 2 | 82.5034 | 76.7060 | -115.9814 | 19.9837 | 143.2821 | 0.0184 | 0.0047 |
| 2024_09_19 22:00 | 3210485 | 3 | 75.1749 | 88.0805 | -117.3373 | 19.6512 | 192.8175 | 0.0153 | 0.0048 |
| 2024_09_19 22:00 | 3257095 | 4 | 89.0751 | 83.5972 | -117.6967 | 12.1928 | 177.4933 | 0.0105 | 0.0074 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412643_74B18B2A | 504990 | 844 | -87.4 | 504990 | 674 | -92.3 | 504990 | 808 | -98.2 | 504990 | 554 |
| MR_1774412643_F19B67C6 | 504990 | 844 | -84.4 | 504990 | 674 | -91.2 | 504990 | 808 | -100.5 | 504990 | 554 |
| MR_1774412643_01B68531 | 504990 | 844 | -86.1 | 504990 | 674 | -91.9 | 504990 | 808 | -100.3 | 504990 | 554 |
| MR_1774412643_40D60710 | 504990 | 844 | -85.7 | 504990 | 674 | -92.0 | 504990 | 808 | -100.5 | 504990 | 554 |
| MR_1774412643_6AFE6579 | 504990 | 844 | -87.6 | 504990 | 674 | -91.4 | 504990 | 808 | -99.3 | 504990 | 554 |
| MR_1774412643_0711D9D7 | 504990 | 844 | -87.8 | 504990 | 674 | -91.9 | 504990 | 808 | -97.3 | 504990 | 554 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 347: `f28753e3-1fd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f28753e3-1fdc-4642-8fb5-03339ac1fb3e` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[347] topology](images/test_0347.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3266248_2
- `C2`: Press down the tilt angle of 3266248_2 by 6 degrees
- `C3`: Increase A3 Offset threshold for 3239942_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266248_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239942_4
- `C6`: Increase transmission power for 3266248_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266248_2
- `C8`: Adjust the azimuth of 3266248_2 by 48 degrees
- `C9`: Decrease transmission power for 3239942_4
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Add neighbor relationship between 3266248_2 and 3239942_4
- `C12`: Increase transmission power for 3239942_4
- `C13`: Add neighbor relationship between 3227800_1 and 3239942_4
- `C14`: Decrease transmission power for 3266248_2
- `C15`: Adjust the azimuth of 3239942_4 by 2 degrees
- `C16`: Increase A3 Offset threshold for 3266248_2
- `C17`: Decrease A3 Offset threshold for 3239942_4
- `C18`: Lift the tilt angle  of 3239942_4 by 3 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239942_4
- `C20`: Press down the tilt angle  of 3239942_4 by 3 degrees
- `C21`: Check test server and transmission issues
- `C22`: Lift the tilt angle of 3266248_2 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.489 | MS1 | 121.4656690688 | 31.1446270133 | 157 | 504990 | -77.98 | 16.64 | 435.20 | 0.12 | 2.47 | 1569 |
| 2024-09-20 22:21:32.408 | MS1 | 121.4656748821 | 31.1446330076 | 157 | 504990 | -78.52 | 13.01 | 544.74 | 0.15 | 2.09 | 1582 |
| 2024-09-20 22:21:33.507 | MS1 | 121.4656767156 | 31.1446339035 | 157 | 504990 | -81.93 | 16.02 | 390.15 | 0.09 | 2.38 | 1577 |
| 2024-09-20 22:21:34.533 | MS1 | 121.4656673750 | 31.1446271429 | 157 | 504990 | -90.61 | 1.41 | 58.29 | 0.12 | 1.14 | 1570 |
| 2024-09-20 22:21:35.947 | MS1 | 121.4656591872 | 31.1446254864 | 157 | 504990 | -93.86 | 0.23 | 55.11 | 0.05 | 1.41 | 1594 |
| 2024-09-20 22:21:36.531 | MS1 | 121.4656651858 | 31.1446312643 | 157 | 504990 | -89.92 | 2.69 | 69.96 | 0.12 | 1.35 | 1574 |
| 2024-09-20 22:21:37.638 | MS1 | 121.4656754817 | 31.1446221158 | 157 | 504990 | -91.73 | 0.43 | 86.17 | 0.02 | 1.33 | 1585 |
| 2024-09-20 22:21:38.668 | MS1 | 121.4656755908 | 31.1446294404 | 157 | 504990 | -90.20 | 3.89 | 51.10 | 0.19 | 1.42 | 1573 |
| 2024-09-20 22:21:39.428 | MS1 | 121.4656657787 | 31.1446187192 | 157 | 504990 | -85.87 | 1.16 | 91.24 | 0.07 | 1.40 | 1569 |
| 2024-09-20 22:21:40.423 | MS1 | 121.4656607927 | 31.1446299361 | 157 | 504990 | -80.50 | 15.29 | 314.97 | 0.04 | 2.83 | 1565 |
| 2024-09-20 22:21:41.931 | MS1 | 121.4656643496 | 31.1446313511 | 157 | 504990 | -75.91 | 15.89 | 491.48 | 0.06 | 2.30 | 1571 |
| 2024-09-20 22:21:42.371 | MS1 | 121.4656696008 | 31.1446196363 | 157 | 504990 | -77.82 | 14.92 | 540.50 | 0.01 | 2.37 | 1574 |

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
| 3211638 | 3 | 121.4676930117 | 31.1479830220 | 127 | 2 | 1 | 41.6 | TDD | 862 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3227800 | 1 | 121.4664385129 | 31.1503376718 | 209 | 15 | 10 | 27.4 | TDD | 987 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3239942 | 4 | 121.4690762022 | 31.1549248483 | 198 | 2 | 11 | 17.7 | TDD | 119 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3266248 | 2 | 121.4730228594 | 31.1472714067 | 295 | 4 | 3 | 21.4 | TDD | 157 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.839 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.864 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.012 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.012 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227800 | 1 | 19.0245 | 18.1900 | -115.3062 | 16.6082 | 191.8046 | 0.0134 | 0.0121 |
| 2024_09_20 22:00 | 3266248 | 2 | 17.9884 | 17.6900 | -108.2958 | 13.7304 | 102.6884 | 0.0006 | 0.0169 |
| 2024_09_20 22:00 | 3211638 | 3 | 13.7224 | 5.3649 | -117.6919 | 6.1070 | 143.9175 | 0.0108 | 0.0092 |
| 2024_09_20 22:00 | 3239942 | 4 | 13.6668 | 6.3703 | -115.4761 | 13.6841 | 176.4521 | 0.0166 | 0.0095 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413886_73474F68 | 504990 | 119 | -89.1 | 504990 | 157 | -85.8 | 504990 | 987 | -91.6 | 504990 | 862 |
| MR_1774413886_B51DD135 | 504990 | 157 | -89.7 | 504990 | 119 | -87.6 | 504990 | 987 | -90.4 | 504990 | 862 |
| MR_1774413886_04703363 | 504990 | 157 | -89.6 | 504990 | 119 | -88.6 | 504990 | 987 | -89.9 | 504990 | 862 |
| MR_1774413886_D890732A | 504990 | 119 | -89.5 | 504990 | 157 | -88.2 | 504990 | 987 | -88.8 | 504990 | 862 |
| MR_1774413886_D1B8033A | 504990 | 157 | -90.2 | 504990 | 119 | -86.6 | 504990 | 987 | -88.1 | 504990 | 862 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 348: `453ce562-7d8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `453ce562-7d86-43a8-9564-9eb845bb5bff` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[348] topology](images/test_0348.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3212881_4
- `C2`: Decrease transmission power for 3225494_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225494_2
- `C4`: Increase transmission power for 3225494_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225494_2
- `C6`: Decrease A3 Offset threshold for 3212881_4
- `C7`: Press down the tilt angle  of 3212881_4 by 10 degrees
- `C8`: Adjust the azimuth of 3212881_4 by 50 degrees
- `C9`: Decrease transmission power for 3212881_4
- `C10`: Press down the tilt angle of 3225494_2 by 10 degrees
- `C11`: Increase A3 Offset threshold for 3225494_2
- `C12`: Decrease A3 Offset threshold for 3225494_2
- `C13`: Lift the tilt angle of 3225494_2 by 10 degrees
- `C14`: Add neighbor relationship between 3225494_2 and 3212881_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212881_4
- `C16`: Lift the tilt angle  of 3212881_4 by 10 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Check test server and transmission issues
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212881_4
- `C20`: Increase transmission power for 3212881_4
- `C21`: Adjust the azimuth of 3225494_2 by 50 degrees
- `C22`: Add neighbor relationship between 3214018_1 and 3212881_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.144 | MS1 | 121.4656687493 | 31.1446299083 | 633 | 504990 | -83.89 | 12.53 | 439.28 | 0.01 | 2.33 | 1591 |
| 2024-09-20 22:21:32.366 | MS1 | 121.4656759155 | 31.1446279399 | 633 | 504990 | -75.50 | 14.23 | 409.46 | 0.04 | 2.54 | 1579 |
| 2024-09-20 22:21:33.165 | MS1 | 121.4656590608 | 31.1446334071 | 633 | 504990 | -81.17 | 14.72 | 312.13 | 0.17 | 2.14 | 1574 |
| 2024-09-20 22:21:34.939 | MS1 | 121.4656602277 | 31.1446210587 | 633 | 504990 | -83.20 | -2.66 | 65.17 | 0.16 | 1.20 | 1571 |
| 2024-09-20 22:21:35.762 | MS1 | 121.4656591779 | 31.1446234016 | 633 | 504990 | -90.13 | -2.58 | 36.88 | 0.13 | 1.09 | 1570 |
| 2024-09-20 22:21:36.639 | MS1 | 121.4656671069 | 31.1446240953 | 633 | 504990 | -89.40 | -0.50 | 48.31 | 0.07 | 1.06 | 1562 |
| 2024-09-20 22:21:37.301 | MS1 | 121.4656666052 | 31.1446365017 | 633 | 504990 | -88.28 | -0.19 | 58.08 | 0.19 | 1.47 | 1570 |
| 2024-09-20 22:21:38.272 | MS1 | 121.4656641379 | 31.1446226749 | 633 | 504990 | -89.20 | -1.47 | 65.65 | 0.05 | 1.23 | 1571 |
| 2024-09-20 22:21:39.625 | MS1 | 121.4656643872 | 31.1446239385 | 831 | 504990 | -80.55 | 17.16 | 296.70 | 0.15 | 1.08 | 1562 |
| 2024-09-20 22:21:40.305 | MS1 | 121.4656766466 | 31.1446326152 | 831 | 504990 | -79.00 | 14.88 | 362.17 | 0.06 | 2.03 | 1579 |
| 2024-09-20 22:21:41.345 | MS1 | 121.4656762480 | 31.1446191749 | 831 | 504990 | -80.53 | 15.34 | 383.20 | 0.09 | 2.11 | 1573 |
| 2024-09-20 22:21:42.581 | MS1 | 121.4656746374 | 31.1446300593 | 831 | 504990 | -83.31 | 14.11 | 390.33 | 0.08 | 2.36 | 1580 |

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
| 3212881 | 4 | 121.4754093364 | 31.1495814460 | 50 | 9 | 5 | 23.9 | TDD | 831 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3214018 | 1 | 121.4725063978 | 31.1453641274 | 181 | 1 | 8 | 27.8 | TDD | 976 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3217069 | 3 | 121.4647730184 | 31.1493739655 | 211 | 1 | 8 | 37.9 | TDD | 630 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3225494 | 2 | 121.4667201577 | 31.1447450210 | 359 | 0 | 7 | 47.6 | TDD | 633 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.054 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.079 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.216 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.216 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.902 | NREventA3 | measId:2;ServCellPCI:338;Se... |
| 2024-09-20 22:21:38.142 | NRHandoverAttempt | SourcePCI:338;SourceNR-ARFC... |
| 2024-09-20 22:21:38.172 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.185 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.289 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.289 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214018 | 1 | 6.5227 | 7.4106 | -117.4039 | 11.9568 | 145.6935 | 0.0041 | 0.0189 |
| 2024_09_20 22:00 | 3225494 | 2 | 12.5718 | 6.9995 | -117.3896 | 18.6919 | 114.0740 | 0.0088 | 0.1668 |
| 2024_09_20 22:00 | 3217069 | 3 | 13.0836 | 15.8940 | -114.0090 | 9.1362 | 165.6611 | 0.0098 | 0.0176 |
| 2024_09_20 22:00 | 3212881 | 4 | 17.5667 | 17.3993 | -115.4309 | 19.7613 | 188.1231 | 0.0162 | 0.0116 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416679_A71D08CE | 504990 | 831 | -78.7 | 504990 | 633 | -83.7 | 504990 | 976 | -85.0 | 504990 | 630 |
| MR_1774416679_A7D743CB | 504990 | 633 | -83.3 | 504990 | 831 | -79.1 | 504990 | 976 | -83.6 | 504990 | 630 |
| MR_1774416679_7471559A | 504990 | 633 | -81.4 | 504990 | 831 | -79.4 | 504990 | 976 | -83.2 | 504990 | 630 |
| MR_1774416679_2F35E2DA | 504990 | 831 | -79.0 | 504990 | 633 | -81.2 | 504990 | 976 | -83.1 | 504990 | 630 |
| MR_1774416679_FDB848AC | 504990 | 633 | -82.1 | 504990 | 831 | -78.5 | 504990 | 976 | -86.4 | 504990 | 630 |
| MR_1774416679_D9884927 | 504990 | 831 | -78.1 | 504990 | 633 | -83.7 | 504990 | 976 | -86.2 | 504990 | 630 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 349: `739c9d1a-6d9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `739c9d1a-6d93-440d-9784-59bb5cf7a49c` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[349] topology](images/test_0349.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3221082_4 by 10 degrees
- `C2`: Decrease A3 Offset threshold for 3221082_4
- `C3`: Adjust the azimuth of 3272849_3 by 3 degrees
- `C4`: Lift the tilt angle of 3221082_4 by 10 degrees
- `C5`: Decrease transmission power for 3221082_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272849_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221082_4
- `C8`: Decrease transmission power for 3272849_3
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Increase A3 Offset threshold for 3221082_4
- `C11`: Add neighbor relationship between 3235938_2 and 3272849_3
- `C12`: Increase transmission power for 3221082_4
- `C13`: Adjust the azimuth of 3221082_4 by 50 degrees
- `C14`: Lift the tilt angle  of 3272849_3 by 6 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221082_4
- `C16`: Press down the tilt angle  of 3272849_3 by 6 degrees
- `C17`: Check test server and transmission issues
- `C18`: Decrease A3 Offset threshold for 3272849_3
- `C19`: Increase A3 Offset threshold for 3272849_3
- `C20`: Increase transmission power for 3272849_3
- `C21`: Add neighbor relationship between 3221082_4 and 3272849_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272849_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.707 | MS1 | 121.4656770306 | 31.1446314695 | 964 | 504990 | -91.53 | 17.77 | 368.87 | 0.07 | 2.71 | 1585 |
| 2024-09-20 22:21:32.872 | MS1 | 121.4656606546 | 31.1446191373 | 964 | 504990 | -86.21 | 14.47 | 530.73 | 0.18 | 2.88 | 1592 |
| 2024-09-20 22:21:33.390 | MS1 | 121.4656662908 | 31.1446326610 | 964 | 504990 | -91.24 | 12.66 | 549.53 | 0.10 | 2.64 | 1561 |
| 2024-09-20 22:21:34.966 | MS1 | 121.4656672825 | 31.1446350752 | 964 | 504990 | -89.56 | 17.95 | 60.62 | 0.15 | 2.35 | 1593 |
| 2024-09-20 22:21:35.856 | MS1 | 121.4656676513 | 31.1446252713 | 964 | 504990 | -85.18 | 14.08 | 81.51 | 0.20 | 2.14 | 1585 |
| 2024-09-20 22:21:36.824 | MS1 | 121.4656603374 | 31.1446307715 | 964 | 504990 | -85.80 | 17.89 | 58.73 | 0.00 | 2.99 | 1586 |
| 2024-09-20 22:21:37.288 | MS1 | 121.4656735553 | 31.1446316723 | 964 | 504990 | -91.91 | 9.95 | 54.43 | 0.16 | 2.84 | 1589 |
| 2024-09-20 22:21:38.995 | MS1 | 121.4656779576 | 31.1446286066 | 964 | 504990 | -92.32 | 8.12 | 50.79 | 0.19 | 2.45 | 1568 |
| 2024-09-20 22:21:39.460 | MS1 | 121.4656778232 | 31.1446238356 | 964 | 504990 | -93.09 | 9.94 | 81.86 | 0.09 | 2.82 | 1576 |
| 2024-09-20 22:21:40.359 | MS1 | 121.4656586783 | 31.1446239658 | 964 | 504990 | -93.00 | 9.52 | 425.17 | 0.01 | 2.35 | 1599 |
| 2024-09-20 22:21:41.928 | MS1 | 121.4656647871 | 31.1446276447 | 964 | 504990 | -89.88 | 10.68 | 461.23 | 0.19 | 2.12 | 1591 |
| 2024-09-20 22:21:42.839 | MS1 | 121.4656648411 | 31.1446295353 | 964 | 504990 | -93.41 | 11.27 | 493.99 | 0.13 | 2.20 | 1570 |

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
| 3221082 | 4 | 121.4697207663 | 31.1549261065 | 5 | 14 | 0 | 21.6 | TDD | 964 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3223992 | 1 | 121.4710239743 | 31.1441323768 | 292 | 10 | 8 | 24.4 | TDD | 385 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3235938 | 2 | 121.4719159558 | 31.1534485747 | 263 | 14 | 9 | 39.2 | TDD | 178 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3272849 | 3 | 121.4657158301 | 31.1517872012 | 183 | 4 | 2 | 24.5 | TDD | 875 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.815 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.840 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.941 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.941 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.646 | NREventA3 | measId:2;ServCellPCI:517;Se... |
| 2024-09-20 22:21:37.886 | NRHandoverAttempt | SourcePCI:517;SourceNR-ARFC... |
| 2024-09-20 22:21:37.925 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.936 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.068 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.068 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3223992 | 1 | 75.9454 | 82.3944 | -115.2273 | 12.2103 | 118.1383 | 0.0077 | 0.0027 |
| 2024_09_19 22:00 | 3235938 | 2 | 90.4502 | 86.9051 | -116.9349 | 10.2953 | 173.3782 | 0.0092 | 0.0172 |
| 2024_09_19 22:00 | 3272849 | 3 | 90.8940 | 87.3079 | -115.8234 | 12.9948 | 159.1469 | 0.0199 | 0.0100 |
| 2024_09_19 22:00 | 3221082 | 4 | 79.1311 | 91.0689 | -114.3338 | 7.5634 | 106.9717 | 0.0199 | 0.0112 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413710_9AF75823 | 504990 | 964 | -90.3 | 504990 | 875 | -91.2 | 504990 | 178 | -102.2 | 504990 | 385 |
| MR_1774413710_9F67F8C8 | 504990 | 964 | -90.4 | 504990 | 875 | -92.3 | 504990 | 178 | -104.2 | 504990 | 385 |
| MR_1774413710_B92FCE15 | 504990 | 964 | -90.6 | 504990 | 875 | -90.6 | 504990 | 178 | -101.8 | 504990 | 385 |
| MR_1774413710_E7C30D85 | 504990 | 964 | -91.0 | 504990 | 875 | -91.2 | 504990 | 178 | -102.5 | 504990 | 385 |
| MR_1774413710_4A6BA8EA | 504990 | 964 | -91.2 | 504990 | 875 | -89.7 | 504990 | 178 | -100.8 | 504990 | 385 |
| MR_1774413710_AEF4067F | 504990 | 964 | -90.4 | 504990 | 875 | -91.4 | 504990 | 178 | -101.6 | 504990 | 385 |

> *... 2개 열 생략 (전체 14열)*

---
