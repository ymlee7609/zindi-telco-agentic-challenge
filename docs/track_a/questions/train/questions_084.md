# Track A 문제 분석 — train[830]~train[839]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[830] ~ train[839] (10개)

## 목차

1. [문제 830: `e9e4b3d2-b7c...`](#830) — multiple-answer, 정답: C2|C4|C19|C20
2. [문제 831: `0598cd5d-294...`](#831) — single-answer, 정답: C12
3. [문제 832: `36cd8659-913...`](#832) — single-answer, 정답: C11
4. [문제 833: `c7bd1453-100...`](#833) — single-answer, 정답: C12
5. [문제 834: `92c19daf-85c...`](#834) — single-answer, 정답: C22
6. [문제 835: `ac643219-9c4...`](#835) — single-answer, 정답: C15
7. [문제 836: `5e7c1e4a-0a8...`](#836) — multiple-answer, 정답: C12|C15
8. [문제 837: `76b4bf82-df7...`](#837) — single-answer, 정답: C20
9. [문제 838: `ad0c314e-6e3...`](#838) — single-answer, 정답: C12
10. [문제 839: `f9181293-0f0...`](#839) — single-answer, 정답: C22

---

### 문제 830: `e9e4b3d2-b7c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e9e4b3d2-b7cc-423b-853f-263517b45d07` |
| Tag | **multiple-answer** |
| 정답 | **C2|C4|C19|C20** |
| C2 의미 | Increase A3 Offset threshold for 3229314_3 |
| C4 의미 | Increase A3 Offset threshold for 3273083_1 |
| C19 의미 | Decrease transmission power for 3229314_3 |
| C20 의미 | Press down the tilt angle  of 3229314_3 by 5 degrees |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[830] topology](images/train_0830.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229314_3
- `C2`: Increase A3 Offset threshold for 3229314_3 **← 정답**
- `C3`: Decrease transmission power for 3273083_1
- `C4`: Increase A3 Offset threshold for 3273083_1 **← 정답**
- `C5`: Adjust the azimuth of 3229314_3 by 12 degrees
- `C6`: Adjust the azimuth of 3273083_1 by 34 degrees
- `C7`: Check test server and transmission issues
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease A3 Offset threshold for 3273083_1
- `C10`: Lift the tilt angle  of 3229314_3 by 5 degrees
- `C11`: Increase transmission power for 3273083_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229314_3
- `C13`: Add neighbor relationship between 3260184_4 and 3229314_3
- `C14`: Increase transmission power for 3229314_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273083_1
- `C16`: Add neighbor relationship between 3273083_1 and 3229314_3
- `C17`: Lift the tilt angle of 3273083_1 by 4 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273083_1
- `C19`: Decrease transmission power for 3229314_3 **← 정답**
- `C20`: Press down the tilt angle  of 3229314_3 by 5 degrees **← 정답**
- `C21`: Press down the tilt angle of 3273083_1 by 4 degrees
- `C22`: Decrease A3 Offset threshold for 3229314_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.361 | MS1 | 121.4656756264 | 31.1446348097 | 992 | 504990 | -82.17 | 16.07 | 387.67 | 0.15 | 2.89 | 1575 |
| 2024-09-20 22:21:32.475 | MS1 | 121.4656755504 | 31.1446226816 | 992 | 504990 | -84.15 | 17.94 | 386.02 | 0.16 | 2.40 | 1596 |
| 2024-09-20 22:21:33.159 | MS1 | 121.4656691544 | 31.1446305306 | 992 | 504990 | -77.43 | 13.09 | 458.68 | 0.07 | 2.94 | 1596 |
| 2024-09-20 22:21:34.827 | MS1 | 121.4656657791 | 31.1446205806 | 960 | 504990 | -88.87 | 3.08 | 26.24 | 0.16 | 1.33 | 1579 |
| 2024-09-20 22:21:35.367 | MS1 | 121.4656653116 | 31.1446353545 | 960 | 504990 | -85.76 | 4.55 | 25.81 | 0.15 | 1.47 | 1561 |
| 2024-09-20 22:21:36.710 | MS1 | 121.4656718920 | 31.1446361784 | 992 | 504990 | -84.37 | 2.61 | 60.15 | 0.03 | 1.44 | 1572 |
| 2024-09-20 22:21:37.534 | MS1 | 121.4656687759 | 31.1446210500 | 992 | 504990 | -89.57 | 4.04 | 24.27 | 0.18 | 1.05 | 1583 |
| 2024-09-20 22:21:38.198 | MS1 | 121.4656694657 | 31.1446359699 | 960 | 504990 | -89.01 | 3.15 | 58.89 | 0.01 | 1.39 | 1578 |
| 2024-09-20 22:21:39.532 | MS1 | 121.4656646258 | 31.1446248698 | 960 | 504990 | -82.46 | 1.64 | 66.31 | 0.20 | 1.39 | 1572 |
| 2024-09-20 22:21:40.399 | MS1 | 121.4656658527 | 31.1446195220 | 960 | 504990 | -81.96 | 13.66 | 550.19 | 0.09 | 2.09 | 1560 |
| 2024-09-20 22:21:41.426 | MS1 | 121.4656661360 | 31.1446279646 | 960 | 504990 | -80.29 | 15.46 | 345.48 | 0.18 | 2.26 | 1587 |
| 2024-09-20 22:21:42.153 | MS1 | 121.4656624926 | 31.1446343297 | 960 | 504990 | -79.61 | 17.90 | 468.99 | 0.14 | 2.81 | 1561 |

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
| 3222102 | 2 | 121.4699446358 | 31.1527204143 | 95 | 8 | 12 | 29.7 | TDD | 960 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3229314 | 3 | 121.4722695055 | 31.1480838353 | 250 | 2 | 0 | 35.3 | TDD | 486 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3244518 | 5 | 121.4658211571 | 31.1448902675 | 317 | 10 | 12 | 32.7 | TDD | 538 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3260184 | 4 | 121.4750786720 | 31.1554200794 | 302 | 13 | 3 | 37.8 | TDD | 209 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3273083 | 1 | 121.4700458594 | 31.1491421610 | 254 | 2 | 5 | 17.9 | TDD | 992 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.998 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.013 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.126 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.126 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.853 | NREventA3 | measId:2;ServCellPCI:81;Ser... |
| 2024-09-20 22:21:34.093 | NRHandoverAttempt | SourcePCI:81;SourceNR-ARFCN... |
| 2024-09-20 22:21:34.135 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.150 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.295 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.295 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.853 | NREventA3 | measId:2;ServCellPCI:514;Se... |
| 2024-09-20 22:21:36.093 | NRHandoverAttempt | SourcePCI:514;SourceNR-ARFC... |
| 2024-09-20 22:21:36.126 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.140 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.241 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.241 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.853 | NREventA3 | measId:2;ServCellPCI:81;Ser... |
| 2024-09-20 22:21:38.093 | NRHandoverAttempt | SourcePCI:81;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.138 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.152 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.262 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.262 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273083 | 1 | 16.6609 | 8.6220 | -117.9934 | 12.1109 | 121.4671 | 0.0121 | 0.0154 |
| 2024_09_20 22:00 | 3222102 | 2 | 6.2048 | 17.0621 | -114.2540 | 5.2831 | 178.5882 | 0.0170 | 0.0179 |
| 2024_09_20 22:00 | 3229314 | 3 | 14.0002 | 8.8370 | -115.5924 | 17.9666 | 198.5740 | 0.0068 | 0.0056 |
| 2024_09_20 22:00 | 3260184 | 4 | 12.2806 | 18.0690 | -115.5684 | 17.6661 | 120.3775 | 0.0093 | 0.0069 |
| 2024_09_20 22:00 | 3244518 | 5 | 10.7623 | 19.6218 | -115.0608 | 15.8824 | 178.9587 | 0.0134 | 0.0189 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416118_2D2CFD81 | 504990 | 992 | -87.2 | 504990 | 960 | -86.8 | 504990 | 486 | -91.6 | 504990 | 209 |
| MR_1774416118_A33AD8BA | 504990 | 960 | -88.3 | 504990 | 992 | -86.9 | 504990 | 486 | -89.5 | 504990 | 209 |
| MR_1774416118_1D5F680A | 504990 | 992 | -86.9 | 504990 | 960 | -87.5 | 504990 | 486 | -89.6 | 504990 | 209 |
| MR_1774416118_5B918FE8 | 504990 | 960 | -88.9 | 504990 | 992 | -86.2 | 504990 | 486 | -91.4 | 504990 | 209 |
| MR_1774416118_6797A9A1 | 504990 | 960 | -88.9 | 504990 | 992 | -86.0 | 504990 | 486 | -89.3 | 504990 | 209 |
| MR_1774416118_8B67661E | 504990 | 960 | -89.0 | 504990 | 992 | -86.6 | 504990 | 486 | -89.8 | 504990 | 209 |
| MR_1774416118_847F15EB | 504990 | 960 | -87.8 | 504990 | 992 | -87.6 | 504990 | 486 | -92.6 | 504990 | 209 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 831: `0598cd5d-294...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0598cd5d-294c-4e3e-a298-57eea94b211a` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Lift the tilt angle  of 3247917_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[831] topology](images/train_0831.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3270834_3
- `C2`: Decrease transmission power for 3270834_3
- `C3`: Increase A3 Offset threshold for 3276859_2
- `C4`: Press down the tilt angle of 3270834_3 by 4 degrees
- `C5`: Adjust the azimuth of 3270834_3 by 45 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270834_3
- `C7`: Increase A3 Offset threshold for 3270834_3
- `C8`: Lift the tilt angle of 3270834_3 by 4 degrees
- `C9`: Add neighbor relationship between 3247917_1 and 3276859_2
- `C10`: Check test server and transmission issues
- `C11`: Decrease transmission power for 3276859_2
- `C12`: Lift the tilt angle  of 3247917_1 by 10 degrees **← 정답**
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276859_2
- `C14`: Increase transmission power for 3270834_3
- `C15`: Press down the tilt angle  of 3247917_1 by 10 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276859_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270834_3
- `C18`: Add neighbor relationship between 3270834_3 and 3276859_2
- `C19`: Decrease A3 Offset threshold for 3276859_2
- `C20`: Increase transmission power for 3276859_2
- `C21`: Adjust the azimuth of 3247917_1 by 50 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.817 | MS1 | 121.4656731766 | 31.1446357654 | 719 | 504990 | -90.22 | 13.62 | 503.70 | 0.01 | 2.27 | 1587 |
| 2024-09-20 22:21:32.445 | MS1 | 121.4656730214 | 31.1446368531 | 719 | 504990 | -85.84 | 13.23 | 428.00 | 0.15 | 2.71 | 1565 |
| 2024-09-20 22:21:33.167 | MS1 | 121.4656682159 | 31.1446359342 | 719 | 504990 | -85.56 | 12.20 | 489.93 | 0.06 | 2.08 | 1573 |
| 2024-09-20 22:21:34.771 | MS1 | 121.4656736045 | 31.1446214374 | 719 | 504990 | -91.48 | 14.38 | 56.33 | 0.02 | 2.62 | 1563 |
| 2024-09-20 22:21:35.639 | MS1 | 121.4656676366 | 31.1446189522 | 719 | 504990 | -91.68 | 15.86 | 80.86 | 0.06 | 2.97 | 1573 |
| 2024-09-20 22:21:36.265 | MS1 | 121.4656760823 | 31.1446213976 | 719 | 504990 | -88.27 | 17.85 | 73.94 | 0.13 | 2.66 | 1597 |
| 2024-09-20 22:21:37.477 | MS1 | 121.4656753117 | 31.1446197481 | 719 | 504990 | -90.34 | 9.54 | 74.06 | 0.12 | 2.31 | 1577 |
| 2024-09-20 22:21:38.717 | MS1 | 121.4656653844 | 31.1446288705 | 719 | 504990 | -93.14 | 8.60 | 72.57 | 0.16 | 2.00 | 1587 |
| 2024-09-20 22:21:39.941 | MS1 | 121.4656632397 | 31.1446270507 | 719 | 504990 | -91.67 | 12.53 | 71.27 | 0.10 | 2.02 | 1569 |
| 2024-09-20 22:21:40.716 | MS1 | 121.4656664627 | 31.1446276194 | 719 | 504990 | -91.92 | 7.19 | 570.59 | 0.04 | 2.30 | 1590 |
| 2024-09-20 22:21:41.128 | MS1 | 121.4656700324 | 31.1446247291 | 719 | 504990 | -89.21 | 8.12 | 382.32 | 0.01 | 2.20 | 1574 |
| 2024-09-20 22:21:42.959 | MS1 | 121.4656741448 | 31.1446377930 | 719 | 504990 | -89.24 | 12.57 | 438.27 | 0.15 | 2.30 | 1591 |

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
| 3219584 | 4 | 121.4755792068 | 31.1556528847 | 356 | 3 | 8 | 47.0 | TDD | 951 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3247917 | 1 | 121.4716792085 | 31.1497125253 | 298 | 14 | 9 | 47.5 | TDD | 552 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3270834 | 3 | 121.4665513512 | 31.1557249382 | 139 | 2 | 5 | 37.3 | TDD | 719 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3276859 | 2 | 121.4694800712 | 31.1535142831 | 302 | 11 | 8 | 30.8 | TDD | 289 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.358 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.495 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.495 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.180 | NREventA3 | measId:2;ServCellPCI:1007;S... |
| 2024-09-20 22:21:38.420 | NRHandoverAttempt | SourcePCI:1007;SourceNR-ARF... |
| 2024-09-20 22:21:38.460 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.473 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.574 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.574 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247917 | 1 | 16.8113 | 7.3762 | -115.3356 | 18.2750 | 151.8504 | 0.0187 | 0.0082 |
| 2024_09_20 22:00 | 3276859 | 2 | 7.1051 | 19.3337 | -117.8691 | 15.1926 | 150.8759 | 0.0065 | 0.0007 |
| 2024_09_20 22:00 | 3270834 | 3 | 87.9986 | 83.3585 | -114.7792 | 11.1390 | 90.6607 | 0.0123 | 0.0097 |
| 2024_09_20 22:00 | 3219584 | 4 | 16.5872 | 15.4191 | -114.0812 | 5.0096 | 146.1086 | 0.0095 | 0.0029 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412393_8E57D18F | 504990 | 719 | -93.0 | 504990 | 289 | -96.6 | 504990 | 552 | -102.1 | 504990 | 951 |
| MR_1774412393_2586670C | 504990 | 719 | -89.7 | 504990 | 289 | -94.6 | 504990 | 552 | -103.0 | 504990 | 951 |
| MR_1774412393_95BE1862 | 504990 | 719 | -89.7 | 504990 | 289 | -97.4 | 504990 | 552 | -99.5 | 504990 | 951 |
| MR_1774412393_E59864D4 | 504990 | 719 | -92.2 | 504990 | 289 | -94.9 | 504990 | 552 | -101.3 | 504990 | 951 |
| MR_1774412393_7CB401B8 | 504990 | 719 | -90.9 | 504990 | 289 | -95.4 | 504990 | 552 | -103.2 | 504990 | 951 |
| MR_1774412393_E6E745E7 | 504990 | 719 | -93.0 | 504990 | 289 | -94.6 | 504990 | 552 | -100.6 | 504990 | 951 |
| MR_1774412393_B243E566 | 504990 | 719 | -92.3 | 504990 | 289 | -97.8 | 504990 | 552 | -102.4 | 504990 | 951 |
| MR_1774412393_024C2916 | 504990 | 719 | -91.4 | 504990 | 289 | -98.1 | 504990 | 552 | -99.9 | 504990 | 951 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 832: `36cd8659-913...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `36cd8659-913d-4c28-b67d-1b5f92bde6ff` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Add neighbor relationship between 3277033_3 and 3237894_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[832] topology](images/train_0832.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3277033_3 by 9 degrees
- `C2`: Check test server and transmission issues
- `C3`: Decrease A3 Offset threshold for 3237894_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277033_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277033_3
- `C6`: Decrease transmission power for 3237894_2
- `C7`: Press down the tilt angle  of 3237894_2 by 4 degrees
- `C8`: Adjust the azimuth of 3237894_2 by 27 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237894_2
- `C10`: Lift the tilt angle  of 3237894_2 by 4 degrees
- `C11`: Add neighbor relationship between 3277033_3 and 3237894_2 **← 정답**
- `C12`: Adjust the azimuth of 3277033_3 by 50 degrees
- `C13`: Decrease A3 Offset threshold for 3277033_3
- `C14`: Increase A3 Offset threshold for 3277033_3
- `C15`: Decrease transmission power for 3277033_3
- `C16`: Add neighbor relationship between 3252507_4 and 3237894_2
- `C17`: Increase A3 Offset threshold for 3237894_2
- `C18`: Press down the tilt angle of 3277033_3 by 9 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237894_2
- `C20`: Increase transmission power for 3237894_2
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Increase transmission power for 3277033_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.592 | MS1 | 121.4656615325 | 31.1446224212 | 363 | 504990 | -80.04 | 13.32 | 481.81 | 0.03 | 2.19 | 1575 |
| 2024-09-20 22:21:32.525 | MS1 | 121.4656657107 | 31.1446339343 | 363 | 504990 | -76.56 | 14.73 | 407.55 | 0.11 | 2.35 | 1597 |
| 2024-09-20 22:21:33.234 | MS1 | 121.4656603811 | 31.1446256895 | 363 | 504990 | -80.15 | 14.77 | 590.96 | 0.05 | 2.55 | 1560 |
| 2024-09-20 22:21:34.475 | MS1 | 121.4656760948 | 31.1446200437 | 363 | 504990 | -94.48 | -3.87 | 58.72 | 0.02 | 1.22 | 1569 |
| 2024-09-20 22:21:35.498 | MS1 | 121.4656650675 | 31.1446237436 | 363 | 504990 | -85.73 | -2.52 | 52.65 | 0.10 | 1.36 | 1570 |
| 2024-09-20 22:21:36.701 | MS1 | 121.4656659720 | 31.1446245515 | 363 | 504990 | -90.37 | -2.01 | 38.05 | 0.01 | 1.23 | 1586 |
| 2024-09-20 22:21:37.533 | MS1 | 121.4656749263 | 31.1446217236 | 363 | 504990 | -87.43 | -2.66 | 47.28 | 0.14 | 1.27 | 1581 |
| 2024-09-20 22:21:38.997 | MS1 | 121.4656689854 | 31.1446256681 | 363 | 504990 | -83.92 | 12.73 | 496.10 | 0.07 | 1.24 | 1577 |
| 2024-09-20 22:21:39.460 | MS1 | 121.4656694659 | 31.1446210266 | 363 | 504990 | -82.78 | 15.14 | 503.66 | 0.05 | 1.35 | 1579 |
| 2024-09-20 22:21:40.166 | MS1 | 121.4656751007 | 31.1446251565 | 363 | 504990 | -84.65 | 15.34 | 594.73 | 0.03 | 2.31 | 1597 |
| 2024-09-20 22:21:41.672 | MS1 | 121.4656741787 | 31.1446323756 | 363 | 504990 | -83.98 | 16.34 | 473.79 | 0.02 | 2.86 | 1562 |
| 2024-09-20 22:21:42.110 | MS1 | 121.4656731004 | 31.1446226653 | 363 | 504990 | -78.85 | 17.87 | 472.82 | 0.01 | 2.32 | 1572 |

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
| 3237894 | 2 | 121.4689548492 | 31.1490268324 | 240 | 1 | 4 | 29.5 | TDD | 809 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3241682 | 1 | 121.4709077466 | 31.1491063994 | 114 | 3 | 12 | 34.6 | TDD | 880 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3252507 | 4 | 121.4697879308 | 31.1553226219 | 104 | 2 | 7 | 31.9 | TDD | 846 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3277033 | 3 | 121.4675998364 | 31.1522214296 | 272 | 6 | 2 | 40.3 | TDD | 363 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.607 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.737 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.737 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.407 | NREventA3 | measId:2;ServCellPCI:410;Se... |
| 2024-09-20 22:21:36.407 | NREventA3 | measId:2;ServCellPCI:410;Se... |
| 2024-09-20 22:21:37.407 | NREventA3 | measId:2;ServCellPCI:410;Se... |
| 2024-09-20 22:21:39.907 | NRRRCReestablishAttempt | PCI:410 |
| 2024-09-20 22:21:39.926 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.938 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:40.084 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.084 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241682 | 1 | 9.8420 | 16.8532 | -115.7198 | 17.9601 | 115.5951 | 0.0061 | 0.0166 |
| 2024_09_20 22:00 | 3237894 | 2 | 18.3514 | 19.9914 | -115.3008 | 9.4753 | 154.3869 | 0.0153 | 0.0121 |
| 2024_09_20 22:00 | 3277033 | 3 | 16.4085 | 7.7103 | -117.7784 | 17.0756 | 167.6596 | 0.0133 | 0.1114 |
| 2024_09_20 22:00 | 3252507 | 4 | 5.1463 | 10.2499 | -116.7668 | 10.9513 | 129.4215 | 0.0066 | 0.0127 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415354_5B42CA6B | 504990 | 809 | -88.8 | 504990 | 363 | -94.7 | 504990 | 846 | -100.1 | 504990 | 880 |
| MR_1774415354_25D63DBD | 504990 | 363 | -94.5 | 504990 | 809 | -89.9 | 504990 | 846 | -96.9 | 504990 | 880 |
| MR_1774415354_46FF9BF8 | 504990 | 809 | -92.0 | 504990 | 363 | -92.6 | 504990 | 846 | -97.5 | 504990 | 880 |
| MR_1774415354_0FDA774B | 504990 | 809 | -92.0 | 504990 | 363 | -95.0 | 504990 | 846 | -97.6 | 504990 | 880 |
| MR_1774415354_9A5ED6A1 | 504990 | 363 | -94.5 | 504990 | 809 | -90.2 | 504990 | 846 | -96.8 | 504990 | 880 |
| MR_1774415354_59C12D17 | 504990 | 363 | -94.0 | 504990 | 809 | -90.9 | 504990 | 846 | -99.7 | 504990 | 880 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 833: `c7bd1453-100...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c7bd1453-1003-4db4-a413-45624547c937` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Lift the tilt angle  of 3224700_1 by 5 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[833] topology](images/train_0833.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3272319_2 by 27 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217824_4
- `C3`: Increase transmission power for 3217824_4
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Lift the tilt angle of 3272319_2 by 4 degrees
- `C6`: Add neighbor relationship between 3224700_1 and 3217824_4
- `C7`: Check test server and transmission issues
- `C8`: Increase A3 Offset threshold for 3272319_2
- `C9`: Press down the tilt angle of 3272319_2 by 4 degrees
- `C10`: Increase A3 Offset threshold for 3217824_4
- `C11`: Adjust the azimuth of 3224700_1 by 45 degrees
- `C12`: Lift the tilt angle  of 3224700_1 by 5 degrees **← 정답**
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217824_4
- `C14`: Decrease transmission power for 3217824_4
- `C15`: Increase transmission power for 3272319_2
- `C16`: Add neighbor relationship between 3272319_2 and 3217824_4
- `C17`: Decrease A3 Offset threshold for 3217824_4
- `C18`: Decrease A3 Offset threshold for 3272319_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272319_2
- `C20`: Decrease transmission power for 3272319_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272319_2
- `C22`: Press down the tilt angle  of 3224700_1 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.176 | MS1 | 121.4656673011 | 31.1446335339 | 291 | 504990 | -87.93 | 12.48 | 383.46 | 0.11 | 2.59 | 1568 |
| 2024-09-20 22:21:32.928 | MS1 | 121.4656612564 | 31.1446336743 | 291 | 504990 | -87.73 | 13.00 | 314.29 | 0.11 | 2.52 | 1568 |
| 2024-09-20 22:21:33.527 | MS1 | 121.4656658939 | 31.1446368850 | 291 | 504990 | -87.93 | 12.71 | 450.75 | 0.04 | 2.22 | 1594 |
| 2024-09-20 22:21:34.947 | MS1 | 121.4656708685 | 31.1446367111 | 291 | 504990 | -91.15 | 16.60 | 76.98 | 0.00 | 2.99 | 1579 |
| 2024-09-20 22:21:35.361 | MS1 | 121.4656747009 | 31.1446213802 | 291 | 504990 | -87.43 | 15.69 | 67.37 | 0.05 | 2.11 | 1596 |
| 2024-09-20 22:21:36.772 | MS1 | 121.4656664074 | 31.1446353392 | 291 | 504990 | -90.17 | 17.12 | 102.44 | 0.16 | 2.35 | 1579 |
| 2024-09-20 22:21:37.204 | MS1 | 121.4656732892 | 31.1446228342 | 291 | 504990 | -92.28 | 9.24 | 66.51 | 0.16 | 2.05 | 1590 |
| 2024-09-20 22:21:38.805 | MS1 | 121.4656667112 | 31.1446312321 | 291 | 504990 | -91.87 | 10.08 | 77.74 | 0.17 | 2.44 | 1577 |
| 2024-09-20 22:21:39.874 | MS1 | 121.4656698594 | 31.1446247069 | 291 | 504990 | -91.83 | 10.11 | 79.88 | 0.10 | 2.91 | 1570 |
| 2024-09-20 22:21:40.950 | MS1 | 121.4656686634 | 31.1446251455 | 291 | 504990 | -90.39 | 8.24 | 457.24 | 0.17 | 2.83 | 1585 |
| 2024-09-20 22:21:41.988 | MS1 | 121.4656587590 | 31.1446256477 | 291 | 504990 | -91.59 | 8.64 | 380.86 | 0.07 | 2.83 | 1570 |
| 2024-09-20 22:21:42.255 | MS1 | 121.4656766708 | 31.1446244690 | 291 | 504990 | -92.04 | 10.00 | 377.02 | 0.09 | 2.83 | 1579 |

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
| 3217824 | 4 | 121.4663192317 | 31.1558277886 | 138 | 3 | 3 | 48.7 | TDD | 526 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3224700 | 1 | 121.4695612172 | 31.1468048262 | 73 | 9 | 8 | 38.3 | TDD | 585 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3245111 | 3 | 121.4728603889 | 31.1544406775 | 45 | 2 | 1 | 35.3 | TDD | 454 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3272319 | 2 | 121.4758366730 | 31.1544140109 | 195 | 3 | 10 | 23.9 | TDD | 291 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.149 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.171 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.301 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.301 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.981 | NREventA3 | measId:2;ServCellPCI:323;Se... |
| 2024-09-20 22:21:38.221 | NRHandoverAttempt | SourcePCI:323;SourceNR-ARFC... |
| 2024-09-20 22:21:38.254 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.265 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.372 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.372 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224700 | 1 | 17.0667 | 10.8349 | -117.3920 | 16.5649 | 118.1201 | 0.0112 | 0.0013 |
| 2024_09_20 22:00 | 3272319 | 2 | 92.6927 | 83.7167 | -115.4258 | 5.2668 | 122.1922 | 0.0151 | 0.0122 |
| 2024_09_20 22:00 | 3245111 | 3 | 14.7095 | 18.1281 | -116.0214 | 10.7836 | 135.1636 | 0.0075 | 0.0062 |
| 2024_09_20 22:00 | 3217824 | 4 | 17.3450 | 19.3495 | -114.6790 | 19.9552 | 94.8764 | 0.0066 | 0.0001 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414554_BC99910B | 504990 | 291 | -91.5 | 504990 | 526 | -98.2 | 504990 | 585 | -106.9 | 504990 | 454 |
| MR_1774414554_19DEA13B | 504990 | 291 | -92.3 | 504990 | 526 | -95.0 | 504990 | 585 | -105.0 | 504990 | 454 |
| MR_1774414554_C1979FC5 | 504990 | 291 | -89.2 | 504990 | 526 | -96.9 | 504990 | 585 | -106.8 | 504990 | 454 |
| MR_1774414554_B686E916 | 504990 | 291 | -90.9 | 504990 | 526 | -97.9 | 504990 | 585 | -106.3 | 504990 | 454 |
| MR_1774414554_267CE01A | 504990 | 291 | -91.2 | 504990 | 526 | -95.3 | 504990 | 585 | -105.5 | 504990 | 454 |
| MR_1774414554_A55D755D | 504990 | 291 | -91.2 | 504990 | 526 | -97.4 | 504990 | 585 | -106.5 | 504990 | 454 |
| MR_1774414554_DA53E758 | 504990 | 291 | -91.9 | 504990 | 526 | -97.8 | 504990 | 585 | -104.1 | 504990 | 454 |
| MR_1774414554_78E638BF | 504990 | 291 | -91.7 | 504990 | 526 | -94.8 | 504990 | 585 | -104.2 | 504990 | 454 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 834: `92c19daf-85c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `92c19daf-85c6-4733-afb5-61d715f0d1ea` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[834] topology](images/train_0834.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3218409_1
- `C2`: Decrease transmission power for 3218409_1
- `C3`: Decrease A3 Offset threshold for 3244643_3
- `C4`: Check test server and transmission issues
- `C5`: Press down the tilt angle of 3244643_3 by 5 degrees
- `C6`: Adjust the azimuth of 3218409_1 by 50 degrees
- `C7`: Adjust the azimuth of 3244643_3 by 50 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244643_3
- `C9`: Press down the tilt angle  of 3218409_1 by 10 degrees
- `C10`: Add neighbor relationship between 3244643_3 and 3218409_1
- `C11`: Add neighbor relationship between 3236446_2 and 3218409_1
- `C12`: Lift the tilt angle of 3244643_3 by 5 degrees
- `C13`: Increase A3 Offset threshold for 3244643_3
- `C14`: Decrease transmission power for 3244643_3
- `C15`: Increase A3 Offset threshold for 3218409_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244643_3
- `C17`: Increase transmission power for 3244643_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218409_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218409_1
- `C20`: Lift the tilt angle  of 3218409_1 by 10 degrees
- `C21`: Increase transmission power for 3218409_1
- `C22`: Insufficient data; more data is needed for judgment. **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.169 | MS1 | 121.4656613085 | 31.1446180484 | 828 | 504990 | -86.23 | 15.30 | 453.73 | 0.13 | 2.36 | 1589 |
| 2024-09-20 22:21:32.795 | MS1 | 121.4656580804 | 31.1446311196 | 828 | 504990 | -85.36 | 16.11 | 352.34 | 0.04 | 2.51 | 1582 |
| 2024-09-20 22:21:33.470 | MS1 | 121.4656643452 | 31.1446271852 | 828 | 504990 | -85.76 | 15.06 | 320.47 | 0.11 | 2.91 | 1594 |
| 2024-09-20 22:21:34.467 | MS1 | 121.4656697479 | 31.1446333278 | 828 | 504990 | -87.68 | 13.56 | 61.65 | 0.15 | 2.36 | 1576 |
| 2024-09-20 22:21:35.602 | MS1 | 121.4656600311 | 31.1446194134 | 828 | 504990 | -91.69 | 17.28 | 79.72 | 0.11 | 2.89 | 1560 |
| 2024-09-20 22:21:36.153 | MS1 | 121.4656671260 | 31.1446376022 | 828 | 504990 | -88.62 | 14.73 | 61.13 | 0.08 | 2.56 | 1585 |
| 2024-09-20 22:21:37.924 | MS1 | 121.4656592680 | 31.1446224849 | 828 | 504990 | -91.92 | 10.78 | 54.07 | 0.03 | 2.56 | 1582 |
| 2024-09-20 22:21:38.855 | MS1 | 121.4656601396 | 31.1446232861 | 828 | 504990 | -92.36 | 10.79 | 46.64 | 0.03 | 2.22 | 1583 |
| 2024-09-20 22:21:39.932 | MS1 | 121.4656702491 | 31.1446328359 | 828 | 504990 | -93.88 | 11.86 | 61.73 | 0.03 | 2.24 | 1588 |
| 2024-09-20 22:21:40.809 | MS1 | 121.4656601910 | 31.1446357354 | 828 | 504990 | -92.80 | 7.47 | 541.69 | 0.07 | 2.23 | 1592 |
| 2024-09-20 22:21:41.889 | MS1 | 121.4656602889 | 31.1446272900 | 828 | 504990 | -92.71 | 8.43 | 580.56 | 0.12 | 2.70 | 1582 |
| 2024-09-20 22:21:42.257 | MS1 | 121.4656668714 | 31.1446316185 | 828 | 504990 | -91.28 | 12.39 | 339.33 | 0.10 | 2.73 | 1597 |

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
| 3218409 | 1 | 121.4674304209 | 31.1452533056 | 329 | 3 | 7 | 44.5 | TDD | 537 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3221404 | 4 | 121.4683174604 | 31.1498783598 | 226 | 10 | 1 | 25.4 | TDD | 110 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3236446 | 2 | 121.4661989106 | 31.1452776962 | 71 | 10 | 7 | 42.1 | TDD | 707 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3244643 | 3 | 121.4700472738 | 31.1480261241 | 7 | 0 | 10 | 47.5 | TDD | 828 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.542 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.563 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.677 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.677 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.419 | NREventA3 | measId:2;ServCellPCI:995;Se... |
| 2024-09-20 22:21:38.659 | NRHandoverAttempt | SourcePCI:995;SourceNR-ARFC... |
| 2024-09-20 22:21:38.709 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.722 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.837 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.837 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3218409 | 1 | 79.6838 | 92.5645 | -114.7801 | 9.9863 | 197.8233 | 0.0100 | 0.0113 |
| 2024_09_19 22:00 | 3236446 | 2 | 90.9607 | 76.8916 | -116.3084 | 13.9633 | 102.7319 | 0.0069 | 0.0101 |
| 2024_09_19 22:00 | 3244643 | 3 | 90.4688 | 90.9365 | -114.9404 | 9.1001 | 86.1651 | 0.0018 | 0.0011 |
| 2024_09_19 22:00 | 3221404 | 4 | 75.4714 | 94.4920 | -116.3048 | 11.5553 | 161.6550 | 0.0161 | 0.0080 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414770_B06C7340 | 504990 | 828 | -87.7 | 504990 | 537 | -96.0 | 504990 | 707 | -101.9 | 504990 | 110 |
| MR_1774414770_49802A9F | 504990 | 828 | -87.4 | 504990 | 537 | -96.4 | 504990 | 707 | -99.9 | 504990 | 110 |
| MR_1774414770_2CA22E0C | 504990 | 828 | -88.5 | 504990 | 537 | -93.2 | 504990 | 707 | -101.6 | 504990 | 110 |
| MR_1774414770_FC6AB9F8 | 504990 | 828 | -89.5 | 504990 | 537 | -96.3 | 504990 | 707 | -101.7 | 504990 | 110 |
| MR_1774414770_285E921E | 504990 | 828 | -87.0 | 504990 | 537 | -92.8 | 504990 | 707 | -98.8 | 504990 | 110 |
| MR_1774414770_2F382447 | 504990 | 828 | -89.2 | 504990 | 537 | -95.9 | 504990 | 707 | -100.9 | 504990 | 110 |
| MR_1774414770_F8ACEC97 | 504990 | 828 | -87.1 | 504990 | 537 | -93.7 | 504990 | 707 | -100.3 | 504990 | 110 |
| MR_1774414770_76178864 | 504990 | 828 | -87.7 | 504990 | 537 | -95.7 | 504990 | 707 | -100.7 | 504990 | 110 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 835: `ac643219-9c4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ac643219-9c4e-40ed-b910-3691a7956cda` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[835] topology](images/train_0835.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3273381_4
- `C2`: Decrease transmission power for 3273381_4
- `C3`: Increase transmission power for 3240950_1
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Adjust the azimuth of 3273381_4 by 17 degrees
- `C6`: Add neighbor relationship between 3273381_4 and 3240950_1
- `C7`: Increase A3 Offset threshold for 3240950_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273381_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240950_1
- `C10`: Add neighbor relationship between 3232904_2 and 3240950_1
- `C11`: Press down the tilt angle  of 3240950_1 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273381_4
- `C13`: Decrease A3 Offset threshold for 3240950_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240950_1
- `C15`: Check test server and transmission issues **← 정답**
- `C16`: Decrease transmission power for 3240950_1
- `C17`: Decrease A3 Offset threshold for 3273381_4
- `C18`: Lift the tilt angle  of 3240950_1 by 10 degrees
- `C19`: Adjust the azimuth of 3240950_1 by 6 degrees
- `C20`: Press down the tilt angle of 3273381_4 by 5 degrees
- `C21`: Increase A3 Offset threshold for 3273381_4
- `C22`: Lift the tilt angle of 3273381_4 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.379 | MS1 | 121.4656624575 | 31.1446211321 | 614 | 504990 | -91.03 | 17.29 | 546.36 | 0.03 | 2.50 | 1579 |
| 2024-09-20 22:21:32.634 | MS1 | 121.4656681504 | 31.1446337299 | 614 | 504990 | -88.35 | 12.98 | 579.48 | 0.00 | 2.47 | 1571 |
| 2024-09-20 22:21:33.401 | MS1 | 121.4656639008 | 31.1446265886 | 614 | 504990 | -88.59 | 16.51 | 478.24 | 0.13 | 2.55 | 1577 |
| 2024-09-20 22:21:34.571 | MS1 | 121.4656731295 | 31.1446369643 | 614 | 504990 | -88.87 | 14.43 | 104.00 | 0.04 | 2.38 | 487 |
| 2024-09-20 22:21:35.554 | MS1 | 121.4656635601 | 31.1446185708 | 614 | 504990 | -91.82 | 14.81 | 93.85 | 0.08 | 2.86 | 338 |
| 2024-09-20 22:21:36.807 | MS1 | 121.4656656731 | 31.1446221905 | 614 | 504990 | -89.93 | 15.06 | 62.18 | 0.14 | 2.66 | 395 |
| 2024-09-20 22:21:37.307 | MS1 | 121.4656587962 | 31.1446301459 | 614 | 504990 | -92.29 | 9.28 | 100.84 | 0.16 | 2.20 | 427 |
| 2024-09-20 22:21:38.455 | MS1 | 121.4656640577 | 31.1446365538 | 614 | 504990 | -93.59 | 9.42 | 66.15 | 0.10 | 2.10 | 359 |
| 2024-09-20 22:21:39.771 | MS1 | 121.4656764737 | 31.1446216745 | 614 | 504990 | -93.77 | 7.93 | 47.99 | 0.14 | 2.89 | 339 |
| 2024-09-20 22:21:40.836 | MS1 | 121.4656691093 | 31.1446361224 | 614 | 504990 | -89.28 | 11.34 | 492.98 | 0.09 | 2.57 | 1578 |
| 2024-09-20 22:21:41.123 | MS1 | 121.4656581966 | 31.1446188741 | 614 | 504990 | -90.05 | 8.18 | 325.38 | 0.08 | 2.96 | 1574 |
| 2024-09-20 22:21:42.650 | MS1 | 121.4656580284 | 31.1446362073 | 614 | 504990 | -91.25 | 10.30 | 590.39 | 0.18 | 2.43 | 1589 |

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
| 3232904 | 2 | 121.4715486523 | 31.1556815584 | 289 | 9 | 1 | 17.5 | TDD | 91 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3240950 | 1 | 121.4730680719 | 31.1506292258 | 220 | 11 | 11 | 19.0 | TDD | 293 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3255086 | 3 | 121.4699408375 | 31.1488305564 | 44 | 15 | 8 | 19.9 | TDD | 517 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3273381 | 4 | 121.4660953940 | 31.1494543297 | 201 | 3 | 8 | 21.8 | TDD | 614 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.297 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.318 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.467 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.467 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.148 | NREventA3 | measId:2;ServCellPCI:734;Se... |
| 2024-09-20 22:21:38.388 | NRHandoverAttempt | SourcePCI:734;SourceNR-ARFC... |
| 2024-09-20 22:21:38.438 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.448 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.566 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.566 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240950 | 1 | 16.1827 | 11.1602 | -117.4255 | 10.4808 | 196.0201 | 0.0025 | 0.0105 |
| 2024_09_20 22:00 | 3232904 | 2 | 6.0932 | 8.2085 | -114.4348 | 16.9806 | 193.6091 | 0.0143 | 0.0070 |
| 2024_09_20 22:00 | 3255086 | 3 | 12.0767 | 6.4587 | -115.9102 | 5.8107 | 80.2692 | 0.0178 | 0.0051 |
| 2024_09_20 22:00 | 3273381 | 4 | 5.0561 | 17.5632 | -114.6699 | 18.6386 | 193.7462 | 0.0092 | 0.0148 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414455_9CAA6127 | 504990 | 614 | -91.6 | 504990 | 293 | -93.0 | 504990 | 91 | -97.3 | 504990 | 517 |
| MR_1774414455_091EF1CF | 504990 | 614 | -91.4 | 504990 | 293 | -91.9 | 504990 | 91 | -98.8 | 504990 | 517 |
| MR_1774414455_8B1CE9F0 | 504990 | 614 | -91.4 | 504990 | 293 | -92.8 | 504990 | 91 | -97.3 | 504990 | 517 |
| MR_1774414455_7318B69E | 504990 | 614 | -90.8 | 504990 | 293 | -91.7 | 504990 | 91 | -99.0 | 504990 | 517 |
| MR_1774414455_9A7CE5F4 | 504990 | 614 | -90.0 | 504990 | 293 | -91.3 | 504990 | 91 | -98.1 | 504990 | 517 |
| MR_1774414455_204784F7 | 504990 | 614 | -93.7 | 504990 | 293 | -93.1 | 504990 | 91 | -100.4 | 504990 | 517 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 836: `5e7c1e4a-0a8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5e7c1e4a-0a85-47f7-b29b-6a10317632ef` |
| Tag | **multiple-answer** |
| 정답 | **C12|C15** |
| C12 의미 | Press down the tilt angle  of 3213710_4 by 5 degrees |
| C15 의미 | Decrease transmission power for 3213710_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[836] topology](images/train_0836.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3213710_4 by 6 degrees
- `C2`: Increase A3 Offset threshold for 3213710_4
- `C3`: Lift the tilt angle  of 3213710_4 by 5 degrees
- `C4`: Add neighbor relationship between 3275913_2 and 3213710_4
- `C5`: Press down the tilt angle of 3275913_2 by 6 degrees
- `C6`: Increase A3 Offset threshold for 3275913_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213710_4
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213710_4
- `C10`: Decrease A3 Offset threshold for 3275913_2
- `C11`: Check test server and transmission issues
- `C12`: Press down the tilt angle  of 3213710_4 by 5 degrees **← 정답**
- `C13`: Decrease A3 Offset threshold for 3213710_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275913_2
- `C15`: Decrease transmission power for 3213710_4 **← 정답**
- `C16`: Lift the tilt angle of 3275913_2 by 6 degrees
- `C17`: Add neighbor relationship between 3237173_1 and 3213710_4
- `C18`: Decrease transmission power for 3275913_2
- `C19`: Adjust the azimuth of 3275913_2 by 46 degrees
- `C20`: Increase transmission power for 3275913_2
- `C21`: Increase transmission power for 3213710_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275913_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.984 | MS1 | 121.4656581436 | 31.1446266659 | 179 | 504990 | -83.89 | 13.34 | 460.52 | 0.12 | 2.38 | 1563 |
| 2024-09-20 22:21:32.565 | MS1 | 121.4656776505 | 31.1446288451 | 179 | 504990 | -80.27 | 17.48 | 345.83 | 0.07 | 2.11 | 1581 |
| 2024-09-20 22:21:33.442 | MS1 | 121.4656632327 | 31.1446263828 | 179 | 504990 | -82.95 | 12.82 | 535.52 | 0.04 | 2.68 | 1565 |
| 2024-09-20 22:21:34.147 | MS1 | 121.4656623423 | 31.1446251280 | 179 | 504990 | -90.69 | 0.21 | 70.33 | 0.20 | 1.22 | 1584 |
| 2024-09-20 22:21:35.419 | MS1 | 121.4656663728 | 31.1446247461 | 179 | 504990 | -92.60 | 1.83 | 86.41 | 0.00 | 1.14 | 1576 |
| 2024-09-20 22:21:36.596 | MS1 | 121.4656763607 | 31.1446303193 | 179 | 504990 | -94.42 | 3.10 | 66.62 | 0.04 | 1.40 | 1585 |
| 2024-09-20 22:21:37.360 | MS1 | 121.4656688477 | 31.1446260053 | 179 | 504990 | -87.50 | 2.30 | 91.91 | 0.17 | 1.37 | 1581 |
| 2024-09-20 22:21:38.181 | MS1 | 121.4656612749 | 31.1446338343 | 179 | 504990 | -85.61 | 2.12 | 68.83 | 0.06 | 1.33 | 1593 |
| 2024-09-20 22:21:39.490 | MS1 | 121.4656720938 | 31.1446367839 | 179 | 504990 | -90.52 | 3.42 | 53.98 | 0.04 | 1.17 | 1579 |
| 2024-09-20 22:21:40.595 | MS1 | 121.4656659417 | 31.1446225449 | 179 | 504990 | -80.95 | 16.24 | 391.69 | 0.03 | 2.90 | 1573 |
| 2024-09-20 22:21:41.813 | MS1 | 121.4656614065 | 31.1446298909 | 179 | 504990 | -76.91 | 15.90 | 536.89 | 0.06 | 2.14 | 1589 |
| 2024-09-20 22:21:42.864 | MS1 | 121.4656604459 | 31.1446191687 | 179 | 504990 | -75.21 | 16.95 | 466.09 | 0.03 | 2.32 | 1584 |

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
| 3213710 | 4 | 121.4675934947 | 31.1505858227 | 189 | 2 | 4 | 40.0 | TDD | 789 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3223962 | 3 | 121.4746762161 | 31.1488805498 | 24 | 6 | 4 | 27.1 | TDD | 324 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3237173 | 1 | 121.4753795448 | 31.1549716310 | 351 | 11 | 5 | 41.7 | TDD | 98 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3275913 | 2 | 121.4690455986 | 31.1484414386 | 171 | 1 | 4 | 42.5 | TDD | 179 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.524 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.549 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.659 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.659 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237173 | 1 | 10.4838 | 18.7250 | -114.5113 | 14.5679 | 86.6149 | 0.0151 | 0.0120 |
| 2024_09_20 22:00 | 3275913 | 2 | 10.4790 | 13.2640 | -109.3461 | 10.1937 | 149.0426 | 0.0066 | 0.0097 |
| 2024_09_20 22:00 | 3223962 | 3 | 5.5769 | 14.5133 | -117.2120 | 14.1929 | 127.2639 | 0.0167 | 0.0155 |
| 2024_09_20 22:00 | 3213710 | 4 | 14.4579 | 11.3560 | -117.5002 | 17.7528 | 114.0950 | 0.0138 | 0.0122 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411995_FAB3624F | 504990 | 179 | -90.9 | 504990 | 789 | -91.0 | 504990 | 98 | -93.6 | 504990 | 324 |
| MR_1774411995_E92D6F13 | 504990 | 789 | -91.1 | 504990 | 179 | -91.8 | 504990 | 98 | -92.5 | 504990 | 324 |
| MR_1774411995_02D58590 | 504990 | 789 | -91.9 | 504990 | 179 | -92.7 | 504990 | 98 | -94.1 | 504990 | 324 |
| MR_1774411995_01264469 | 504990 | 179 | -90.1 | 504990 | 789 | -93.0 | 504990 | 98 | -93.4 | 504990 | 324 |
| MR_1774411995_3CB0D586 | 504990 | 179 | -91.8 | 504990 | 789 | -90.3 | 504990 | 98 | -92.3 | 504990 | 324 |
| MR_1774411995_F82B29B4 | 504990 | 179 | -88.9 | 504990 | 789 | -89.8 | 504990 | 98 | -93.7 | 504990 | 324 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 837: `76b4bf82-df7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `76b4bf82-df79-4d96-b0f4-396c737e23ad` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3252331_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[837] topology](images/train_0837.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase transmission power for 3252331_1
- `C3`: Decrease transmission power for 3213035_3
- `C4`: Increase A3 Offset threshold for 3213035_3
- `C5`: Press down the tilt angle  of 3213035_3 by 2 degrees
- `C6`: Add neighbor relationship between 3278109_2 and 3213035_3
- `C7`: Increase A3 Offset threshold for 3252331_1
- `C8`: Press down the tilt angle of 3252331_1 by 4 degrees
- `C9`: Decrease A3 Offset threshold for 3213035_3
- `C10`: Decrease transmission power for 3252331_1
- `C11`: Increase transmission power for 3213035_3
- `C12`: Adjust the azimuth of 3213035_3 by 50 degrees
- `C13`: Add neighbor relationship between 3252331_1 and 3213035_3
- `C14`: Lift the tilt angle  of 3213035_3 by 2 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213035_3
- `C16`: Adjust the azimuth of 3252331_1 by 17 degrees
- `C17`: Decrease A3 Offset threshold for 3252331_1
- `C18`: Check test server and transmission issues
- `C19`: Lift the tilt angle of 3252331_1 by 4 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252331_1 **← 정답**
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252331_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213035_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.267 | MS1 | 121.4656688193 | 31.1446240937 | 193 | 504990 | -89.43 | 16.16 | 417.89 | 0.13 | 2.41 | 1599 |
| 2024-09-20 22:21:32.309 | MS1 | 121.4656729368 | 31.1446340686 | 193 | 504990 | -90.39 | 17.92 | 513.74 | 0.16 | 2.70 | 1576 |
| 2024-09-20 22:21:33.482 | MS1 | 121.4656673865 | 31.1446355665 | 193 | 504990 | -86.22 | 17.71 | 540.57 | 0.11 | 2.52 | 1593 |
| 2024-09-20 22:21:34.231 | MS1 | 121.4656629893 | 31.1446257364 | 193 | 504990 | -90.75 | 13.22 | 70.20 | 0.57 | 2.41 | 596 |
| 2024-09-20 22:21:35.661 | MS1 | 121.4656598733 | 31.1446186495 | 193 | 504990 | -85.66 | 16.67 | 85.12 | 0.54 | 2.30 | 564 |
| 2024-09-20 22:21:36.824 | MS1 | 121.4656719624 | 31.1446199328 | 193 | 504990 | -86.32 | 17.54 | 59.57 | 0.55 | 2.51 | 524 |
| 2024-09-20 22:21:37.884 | MS1 | 121.4656730403 | 31.1446285106 | 193 | 504990 | -93.79 | 9.79 | 66.40 | 0.52 | 2.48 | 645 |
| 2024-09-20 22:21:38.337 | MS1 | 121.4656727249 | 31.1446334821 | 193 | 504990 | -90.33 | 11.24 | 59.16 | 0.58 | 2.16 | 550 |
| 2024-09-20 22:21:39.218 | MS1 | 121.4656722262 | 31.1446346939 | 193 | 504990 | -91.54 | 9.50 | 71.39 | 0.60 | 2.10 | 556 |
| 2024-09-20 22:21:40.604 | MS1 | 121.4656589599 | 31.1446358783 | 193 | 504990 | -93.78 | 10.86 | 327.14 | 0.18 | 2.78 | 1569 |
| 2024-09-20 22:21:41.600 | MS1 | 121.4656587069 | 31.1446213545 | 193 | 504990 | -93.27 | 9.60 | 413.27 | 0.18 | 2.09 | 1573 |
| 2024-09-20 22:21:42.742 | MS1 | 121.4656602356 | 31.1446202555 | 193 | 504990 | -91.61 | 8.30 | 501.35 | 0.03 | 2.20 | 1600 |

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
| 3212784 | 4 | 121.4650680546 | 31.1441381680 | 15 | 14 | 10 | 48.1 | TDD | 607 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3213035 | 3 | 121.4712245297 | 31.1478171152 | 0 | 0 | 2 | 20.0 | TDD | 748 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3252331 | 1 | 121.4683969633 | 31.1552941284 | 175 | 3 | 7 | 26.4 | TDD | 193 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3278109 | 2 | 121.4679893165 | 31.1530516006 | 309 | 14 | 5 | 42.6 | TDD | 659 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.826 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.849 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.950 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.950 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.705 | NREventA3 | measId:2;ServCellPCI:2;Serv... |
| 2024-09-20 22:21:37.945 | NRHandoverAttempt | SourcePCI:2;SourceNR-ARFCN:... |
| 2024-09-20 22:21:37.989 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.004 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.114 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.114 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252331 | 1 | 16.6592 | 12.0162 | -116.0394 | 9.9776 | 189.8733 | 0.0010 | 0.0108 |
| 2024_09_20 22:00 | 3278109 | 2 | 13.7571 | 6.5210 | -114.2174 | 14.0524 | 179.8698 | 0.0034 | 0.0053 |
| 2024_09_20 22:00 | 3213035 | 3 | 9.1382 | 10.4671 | -114.9262 | 7.1086 | 151.0329 | 0.0111 | 0.0156 |
| 2024_09_20 22:00 | 3212784 | 4 | 7.6825 | 11.3599 | -116.5268 | 14.5211 | 111.8504 | 0.0109 | 0.0123 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412435_23CAC8FF | 504990 | 193 | -88.9 | 504990 | 748 | -98.6 | 504990 | 659 | -99.3 | 504990 | 607 |
| MR_1774412435_7EBCED59 | 504990 | 193 | -91.4 | 504990 | 748 | -97.0 | 504990 | 659 | -96.2 | 504990 | 607 |
| MR_1774412435_8405ED42 | 504990 | 193 | -91.7 | 504990 | 748 | -95.2 | 504990 | 659 | -95.7 | 504990 | 607 |
| MR_1774412435_E4D92547 | 504990 | 193 | -88.8 | 504990 | 748 | -98.5 | 504990 | 659 | -99.3 | 504990 | 607 |
| MR_1774412435_82B41C25 | 504990 | 193 | -89.5 | 504990 | 748 | -96.6 | 504990 | 659 | -96.6 | 504990 | 607 |
| MR_1774412435_7F7B0553 | 504990 | 193 | -92.6 | 504990 | 748 | -97.9 | 504990 | 659 | -96.5 | 504990 | 607 |
| MR_1774412435_C2057E0E | 504990 | 193 | -90.9 | 504990 | 748 | -97.5 | 504990 | 659 | -97.9 | 504990 | 607 |
| MR_1774412435_A0DDCCA0 | 504990 | 193 | -92.2 | 504990 | 748 | -95.3 | 504990 | 659 | -96.7 | 504990 | 607 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 838: `ad0c314e-6e3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ad0c314e-6e3f-40ec-a282-2f924f37d5ee` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[838] topology](images/train_0838.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212782_3
- `C2`: Decrease A3 Offset threshold for 3248399_1
- `C3`: Decrease A3 Offset threshold for 3212782_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248399_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248399_1
- `C6`: Increase transmission power for 3212782_3
- `C7`: Press down the tilt angle  of 3212782_3 by 5 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212782_3
- `C9`: Press down the tilt angle of 3248399_1 by 5 degrees
- `C10`: Check test server and transmission issues
- `C11`: Increase transmission power for 3248399_1
- `C12`: Insufficient data; more data is needed for judgment. **← 정답**
- `C13`: Add neighbor relationship between 3248399_1 and 3212782_3
- `C14`: Adjust the azimuth of 3248399_1 by 50 degrees
- `C15`: Adjust the azimuth of 3212782_3 by 50 degrees
- `C16`: Decrease transmission power for 3248399_1
- `C17`: Lift the tilt angle  of 3212782_3 by 5 degrees
- `C18`: Add neighbor relationship between 3225650_2 and 3212782_3
- `C19`: Increase A3 Offset threshold for 3212782_3
- `C20`: Decrease transmission power for 3212782_3
- `C21`: Increase A3 Offset threshold for 3248399_1
- `C22`: Lift the tilt angle of 3248399_1 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.568 | MS1 | 121.4656641786 | 31.1446209781 | 873 | 504990 | -85.60 | 13.52 | 361.59 | 0.19 | 2.07 | 1570 |
| 2024-09-20 22:21:32.621 | MS1 | 121.4656613371 | 31.1446221101 | 873 | 504990 | -86.79 | 14.45 | 378.10 | 0.19 | 2.07 | 1565 |
| 2024-09-20 22:21:33.638 | MS1 | 121.4656738818 | 31.1446273373 | 873 | 504990 | -91.77 | 16.58 | 474.96 | 0.07 | 2.69 | 1581 |
| 2024-09-20 22:21:34.409 | MS1 | 121.4656642611 | 31.1446208861 | 873 | 504990 | -89.78 | 13.59 | 86.31 | 0.14 | 2.68 | 1596 |
| 2024-09-20 22:21:35.175 | MS1 | 121.4656744426 | 31.1446256014 | 873 | 504990 | -90.72 | 16.75 | 88.67 | 0.20 | 2.53 | 1599 |
| 2024-09-20 22:21:36.900 | MS1 | 121.4656741797 | 31.1446226341 | 873 | 504990 | -87.26 | 16.33 | 47.77 | 0.01 | 2.22 | 1566 |
| 2024-09-20 22:21:37.619 | MS1 | 121.4656645925 | 31.1446365055 | 873 | 504990 | -91.77 | 10.71 | 75.31 | 0.15 | 2.55 | 1561 |
| 2024-09-20 22:21:38.371 | MS1 | 121.4656720863 | 31.1446346091 | 873 | 504990 | -93.47 | 9.32 | 65.22 | 0.18 | 2.07 | 1577 |
| 2024-09-20 22:21:39.177 | MS1 | 121.4656698902 | 31.1446198831 | 873 | 504990 | -92.74 | 11.59 | 95.85 | 0.03 | 2.83 | 1585 |
| 2024-09-20 22:21:40.990 | MS1 | 121.4656743186 | 31.1446250212 | 873 | 504990 | -93.94 | 11.08 | 513.54 | 0.14 | 2.18 | 1563 |
| 2024-09-20 22:21:41.934 | MS1 | 121.4656713478 | 31.1446201550 | 873 | 504990 | -90.26 | 12.37 | 452.85 | 0.06 | 2.13 | 1570 |
| 2024-09-20 22:21:42.247 | MS1 | 121.4656703583 | 31.1446258907 | 873 | 504990 | -89.74 | 10.28 | 500.69 | 0.15 | 2.03 | 1589 |

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
| 3212782 | 3 | 121.4668390228 | 31.1512544099 | 0 | 3 | 2 | 21.2 | TDD | 228 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3225650 | 2 | 121.4731091392 | 31.1508619832 | 325 | 1 | 2 | 38.0 | TDD | 540 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3236861 | 4 | 121.4654626399 | 31.1531056040 | 290 | 8 | 1 | 48.5 | TDD | 517 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3248399 | 1 | 121.4697411240 | 31.1465638363 | 307 | 0 | 2 | 35.4 | TDD | 873 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.563 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.586 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.713 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.713 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.373 | NREventA3 | measId:2;ServCellPCI:723;Se... |
| 2024-09-20 22:21:38.613 | NRHandoverAttempt | SourcePCI:723;SourceNR-ARFC... |
| 2024-09-20 22:21:38.659 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.673 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.802 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.802 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3248399 | 1 | 83.9807 | 75.3390 | -117.6676 | 9.5679 | 124.1016 | 0.0098 | 0.0121 |
| 2024_09_19 22:00 | 3225650 | 2 | 80.7311 | 90.3977 | -115.5359 | 11.0304 | 135.2368 | 0.0107 | 0.0093 |
| 2024_09_19 22:00 | 3212782 | 3 | 80.5059 | 77.7540 | -117.8403 | 11.3804 | 184.2442 | 0.0108 | 0.0109 |
| 2024_09_19 22:00 | 3236861 | 4 | 82.9627 | 83.8004 | -117.6232 | 8.7458 | 129.8257 | 0.0027 | 0.0125 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412010_21A8101C | 504990 | 873 | -89.0 | 504990 | 228 | -97.7 | 504990 | 540 | -98.0 | 504990 | 517 |
| MR_1774412010_3E827F9A | 504990 | 873 | -88.1 | 504990 | 228 | -99.2 | 504990 | 540 | -99.2 | 504990 | 517 |
| MR_1774412010_6B0053F5 | 504990 | 873 | -90.5 | 504990 | 228 | -97.0 | 504990 | 540 | -98.1 | 504990 | 517 |
| MR_1774412010_3A4F8912 | 504990 | 873 | -88.5 | 504990 | 228 | -97.6 | 504990 | 540 | -99.7 | 504990 | 517 |
| MR_1774412010_57F72FD1 | 504990 | 873 | -88.0 | 504990 | 228 | -100.7 | 504990 | 540 | -98.6 | 504990 | 517 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 839: `f9181293-0f0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f9181293-0f01-42f1-afa8-b5789b308d00` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3270516_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[839] topology](images/train_0839.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3263162_1
- `C2`: Increase transmission power for 3270516_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263162_1
- `C4`: Increase A3 Offset threshold for 3263162_1
- `C5`: Press down the tilt angle of 3270516_4 by 4 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270516_4
- `C7`: Add neighbor relationship between 3270516_4 and 3263162_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Adjust the azimuth of 3263162_1 by 50 degrees
- `C10`: Increase A3 Offset threshold for 3270516_4
- `C11`: Decrease transmission power for 3270516_4
- `C12`: Decrease A3 Offset threshold for 3263162_1
- `C13`: Press down the tilt angle  of 3263162_1 by 9 degrees
- `C14`: Lift the tilt angle of 3270516_4 by 4 degrees
- `C15`: Add neighbor relationship between 3238602_2 and 3263162_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263162_1
- `C17`: Decrease transmission power for 3263162_1
- `C18`: Adjust the azimuth of 3270516_4 by 33 degrees
- `C19`: Lift the tilt angle  of 3263162_1 by 9 degrees
- `C20`: Check test server and transmission issues
- `C21`: Decrease A3 Offset threshold for 3270516_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270516_4 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.296 | MS1 | 121.4656653526 | 31.1446372112 | 31 | 504990 | -89.13 | 12.52 | 436.64 | 0.16 | 2.58 | 1572 |
| 2024-09-20 22:21:32.594 | MS1 | 121.4656755468 | 31.1446225564 | 31 | 504990 | -91.93 | 17.04 | 377.52 | 0.06 | 2.03 | 1580 |
| 2024-09-20 22:21:33.136 | MS1 | 121.4656659661 | 31.1446217188 | 31 | 504990 | -90.62 | 17.31 | 426.18 | 0.01 | 2.84 | 1596 |
| 2024-09-20 22:21:34.722 | MS1 | 121.4656645329 | 31.1446238801 | 31 | 504990 | -86.35 | 17.45 | 79.02 | 0.63 | 2.29 | 614 |
| 2024-09-20 22:21:35.598 | MS1 | 121.4656625061 | 31.1446197209 | 31 | 504990 | -85.81 | 16.85 | 58.09 | 0.59 | 2.85 | 542 |
| 2024-09-20 22:21:36.708 | MS1 | 121.4656682992 | 31.1446359392 | 31 | 504990 | -85.38 | 12.12 | 56.53 | 0.55 | 2.35 | 563 |
| 2024-09-20 22:21:37.913 | MS1 | 121.4656673177 | 31.1446278955 | 31 | 504990 | -89.95 | 11.93 | 84.49 | 0.67 | 2.53 | 539 |
| 2024-09-20 22:21:38.107 | MS1 | 121.4656717562 | 31.1446210039 | 31 | 504990 | -93.44 | 10.81 | 58.65 | 0.54 | 2.64 | 694 |
| 2024-09-20 22:21:39.565 | MS1 | 121.4656626372 | 31.1446244202 | 31 | 504990 | -90.74 | 10.46 | 92.68 | 0.56 | 2.42 | 526 |
| 2024-09-20 22:21:40.433 | MS1 | 121.4656694287 | 31.1446250915 | 31 | 504990 | -93.81 | 12.75 | 397.94 | 0.13 | 2.10 | 1577 |
| 2024-09-20 22:21:41.548 | MS1 | 121.4656775708 | 31.1446209238 | 31 | 504990 | -90.08 | 9.00 | 389.07 | 0.04 | 2.92 | 1597 |
| 2024-09-20 22:21:42.568 | MS1 | 121.4656612560 | 31.1446308882 | 31 | 504990 | -90.18 | 10.68 | 515.92 | 0.12 | 2.52 | 1567 |

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
| 3210327 | 3 | 121.4691087321 | 31.1531259511 | 252 | 12 | 4 | 23.3 | TDD | 323 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3238602 | 2 | 121.4646511086 | 31.1505199954 | 236 | 15 | 3 | 20.4 | TDD | 938 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3263162 | 1 | 121.4736265177 | 31.1545818558 | 34 | 8 | 8 | 15.7 | TDD | 729 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3270516 | 4 | 121.4758735541 | 31.1491835492 | 275 | 3 | 8 | 22.2 | TDD | 31 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.268 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.287 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.392 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.392 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.136 | NREventA3 | measId:2;ServCellPCI:945;Se... |
| 2024-09-20 22:21:38.376 | NRHandoverAttempt | SourcePCI:945;SourceNR-ARFC... |
| 2024-09-20 22:21:38.415 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.429 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.538 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.538 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263162 | 1 | 19.0531 | 6.4621 | -116.2439 | 11.8133 | 151.6734 | 0.0127 | 0.0099 |
| 2024_09_20 22:00 | 3238602 | 2 | 11.2719 | 8.7425 | -116.6738 | 12.7161 | 110.8275 | 0.0152 | 0.0199 |
| 2024_09_20 22:00 | 3210327 | 3 | 10.2109 | 14.2561 | -116.1078 | 13.8000 | 149.0088 | 0.0179 | 0.0051 |
| 2024_09_20 22:00 | 3270516 | 4 | 5.1765 | 15.8715 | -116.9661 | 6.5135 | 130.4180 | 0.0102 | 0.0073 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414615_159A1E84 | 504990 | 31 | -87.2 | 504990 | 729 | -95.7 | 504990 | 938 | -97.1 | 504990 | 323 |
| MR_1774414615_7581387E | 504990 | 31 | -87.3 | 504990 | 729 | -94.7 | 504990 | 938 | -94.2 | 504990 | 323 |
| MR_1774414615_A5622EB0 | 504990 | 31 | -86.7 | 504990 | 729 | -95.7 | 504990 | 938 | -94.5 | 504990 | 323 |
| MR_1774414615_24EDAF0B | 504990 | 31 | -87.5 | 504990 | 729 | -93.0 | 504990 | 938 | -96.5 | 504990 | 323 |
| MR_1774414615_635B786E | 504990 | 31 | -87.4 | 504990 | 729 | -92.8 | 504990 | 938 | -97.0 | 504990 | 323 |
| MR_1774414615_4FF270B5 | 504990 | 31 | -84.4 | 504990 | 729 | -95.7 | 504990 | 938 | -98.0 | 504990 | 323 |

> *... 2개 열 생략 (전체 14열)*

---
