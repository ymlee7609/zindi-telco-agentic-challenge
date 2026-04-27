# Track A 문제 분석 — test[10]~test[19]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[10] ~ test[19] (10개)

## 목차

1. [문제 10: `404fb825-860...`](#10) — multiple-answer
2. [문제 11: `c95c7270-9e7...`](#11) — single-answer
3. [문제 12: `a7b35fcb-2fe...`](#12) — single-answer
4. [문제 13: `b0ef4fd7-e69...`](#13) — single-answer
5. [문제 14: `6f1825be-13f...`](#14) — single-answer
6. [문제 15: `74abdf87-76b...`](#15) — multiple-answer
7. [문제 16: `acb898f7-5e9...`](#16) — single-answer
8. [문제 17: `06df7252-3bf...`](#17) — single-answer
9. [문제 18: `e5930631-de9...`](#18) — single-answer
10. [문제 19: `c0d6fcb9-3c9...`](#19) — single-answer

---

### 문제 10: `404fb825-860...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `404fb825-8603-4497-91ce-92e40d4a2164` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[10] topology](images/test_0010.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3222669_5
- `C2`: Decrease transmission power for 3219245_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219245_3
- `C4`: Press down the tilt angle  of 3222669_5 by 5 degrees
- `C5`: Increase transmission power for 3219245_3
- `C6`: Check test server and transmission issues
- `C7`: Press down the tilt angle of 3219245_3 by 4 degrees
- `C8`: Add neighbor relationship between 3241350_2 and 3222669_5
- `C9`: Adjust the azimuth of 3222669_5 by 50 degrees
- `C10`: Lift the tilt angle  of 3222669_5 by 5 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222669_5
- `C13`: Increase A3 Offset threshold for 3222669_5
- `C14`: Increase transmission power for 3222669_5
- `C15`: Decrease A3 Offset threshold for 3222669_5
- `C16`: Lift the tilt angle of 3219245_3 by 4 degrees
- `C17`: Add neighbor relationship between 3219245_3 and 3222669_5
- `C18`: Adjust the azimuth of 3219245_3 by 32 degrees
- `C19`: Decrease A3 Offset threshold for 3219245_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219245_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222669_5
- `C22`: Increase A3 Offset threshold for 3219245_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.241 | MS1 | 121.4656690513 | 31.1446219502 | 625 | 504990 | -75.22 | 12.67 | 406.28 | 0.12 | 2.96 | 1596 |
| 2024-09-20 22:21:32.912 | MS1 | 121.4656614028 | 31.1446348025 | 625 | 504990 | -82.87 | 16.32 | 311.39 | 0.17 | 2.04 | 1589 |
| 2024-09-20 22:21:33.740 | MS1 | 121.4656606789 | 31.1446323185 | 625 | 504990 | -78.43 | 13.91 | 507.41 | 0.00 | 2.22 | 1591 |
| 2024-09-20 22:21:34.127 | MS1 | 121.4656589727 | 31.1446218656 | 789 | 504990 | -85.87 | 3.54 | 58.09 | 0.09 | 1.49 | 1566 |
| 2024-09-20 22:21:35.536 | MS1 | 121.4656634828 | 31.1446292845 | 789 | 504990 | -81.78 | 2.99 | 59.72 | 0.07 | 1.28 | 1584 |
| 2024-09-20 22:21:36.251 | MS1 | 121.4656673116 | 31.1446298388 | 625 | 504990 | -81.91 | 1.48 | 33.34 | 0.15 | 1.33 | 1585 |
| 2024-09-20 22:21:37.707 | MS1 | 121.4656658214 | 31.1446339461 | 625 | 504990 | -82.03 | 3.92 | 67.73 | 0.13 | 1.31 | 1562 |
| 2024-09-20 22:21:38.377 | MS1 | 121.4656618796 | 31.1446247099 | 789 | 504990 | -86.24 | 2.61 | 79.15 | 0.08 | 1.18 | 1560 |
| 2024-09-20 22:21:39.596 | MS1 | 121.4656696063 | 31.1446231577 | 789 | 504990 | -81.41 | 3.83 | 64.99 | 0.02 | 1.25 | 1575 |
| 2024-09-20 22:21:40.756 | MS1 | 121.4656744297 | 31.1446322347 | 789 | 504990 | -81.90 | 12.29 | 360.34 | 0.01 | 2.94 | 1561 |
| 2024-09-20 22:21:41.766 | MS1 | 121.4656688650 | 31.1446345270 | 789 | 504990 | -83.32 | 13.20 | 599.04 | 0.04 | 2.36 | 1566 |
| 2024-09-20 22:21:42.409 | MS1 | 121.4656649778 | 31.1446184028 | 789 | 504990 | -81.30 | 13.97 | 365.22 | 0.04 | 2.17 | 1584 |

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
| 3219245 | 3 | 121.4724680091 | 31.1450108987 | 298 | 1 | 3 | 31.1 | TDD | 625 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3222669 | 5 | 121.4756639456 | 31.1548483835 | 170 | 4 | 9 | 15.9 | TDD | 254 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3241350 | 2 | 121.4695809888 | 31.1536512721 | 15 | 15 | 7 | 27.3 | TDD | 517 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3263736 | 1 | 121.4724822250 | 31.1556150325 | 330 | 0 | 1 | 29.4 | TDD | 545 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3268406 | 4 | 121.4698629124 | 31.1546044232 | 87 | 3 | 0 | 41.2 | TDD | 789 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.619 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.639 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.762 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.762 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.472 | NREventA3 | measId:2;ServCellPCI:410;Se... |
| 2024-09-20 22:21:34.712 | NRHandoverAttempt | SourcePCI:410;SourceNR-ARFC... |
| 2024-09-20 22:21:34.748 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.763 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.877 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.877 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.472 | NREventA3 | measId:2;ServCellPCI:618;Se... |
| 2024-09-20 22:21:36.712 | NRHandoverAttempt | SourcePCI:618;SourceNR-ARFC... |
| 2024-09-20 22:21:36.747 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.757 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:36.868 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.868 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.472 | NREventA3 | measId:2;ServCellPCI:410;Se... |
| 2024-09-20 22:21:38.712 | NRHandoverAttempt | SourcePCI:410;SourceNR-ARFC... |
| 2024-09-20 22:21:38.755 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.767 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.869 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.869 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263736 | 1 | 18.4740 | 15.0383 | -115.9350 | 7.8792 | 170.2647 | 0.0067 | 0.0162 |
| 2024_09_20 22:00 | 3241350 | 2 | 14.2175 | 12.8112 | -114.3504 | 7.1226 | 134.0251 | 0.0153 | 0.0157 |
| 2024_09_20 22:00 | 3219245 | 3 | 15.5941 | 16.5613 | -115.2477 | 8.8212 | 80.0041 | 0.0012 | 0.0113 |
| 2024_09_20 22:00 | 3268406 | 4 | 11.1848 | 10.2856 | -116.6173 | 17.2558 | 149.6734 | 0.0038 | 0.0167 |
| 2024_09_20 22:00 | 3222669 | 5 | 9.0224 | 13.1938 | -115.9545 | 16.5589 | 154.5134 | 0.0058 | 0.0005 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416238_097335DA | 504990 | 789 | -85.9 | 504990 | 625 | -84.2 | 504990 | 254 | -91.9 | 504990 | 517 |
| MR_1774416238_343B9A10 | 504990 | 789 | -85.0 | 504990 | 625 | -84.4 | 504990 | 254 | -93.0 | 504990 | 517 |
| MR_1774416238_A077CC18 | 504990 | 789 | -85.7 | 504990 | 625 | -84.0 | 504990 | 254 | -92.8 | 504990 | 517 |
| MR_1774416238_824C218E | 504990 | 789 | -86.1 | 504990 | 625 | -83.2 | 504990 | 254 | -90.5 | 504990 | 517 |
| MR_1774416238_DA08B41E | 504990 | 625 | -84.3 | 504990 | 789 | -85.1 | 504990 | 254 | -92.7 | 504990 | 517 |
| MR_1774416238_700F2FF7 | 504990 | 789 | -87.2 | 504990 | 625 | -82.3 | 504990 | 254 | -92.1 | 504990 | 517 |
| MR_1774416238_EBB41359 | 504990 | 625 | -85.8 | 504990 | 789 | -84.6 | 504990 | 254 | -89.4 | 504990 | 517 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 11: `c95c7270-9e7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c95c7270-9e74-47b8-b475-eff7d7c3b5eb` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[11] topology](images/test_0011.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251610_1
- `C2`: Add neighbor relationship between 3228887_4 and 3268643_3
- `C3`: Decrease transmission power for 3251610_1
- `C4`: Press down the tilt angle of 3251610_1 by 5 degrees
- `C5`: Add neighbor relationship between 3251610_1 and 3268643_3
- `C6`: Lift the tilt angle of 3251610_1 by 5 degrees
- `C7`: Lift the tilt angle  of 3228887_4 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268643_3
- `C9`: Increase A3 Offset threshold for 3251610_1
- `C10`: Increase A3 Offset threshold for 3268643_3
- `C11`: Decrease A3 Offset threshold for 3268643_3
- `C12`: Adjust the azimuth of 3251610_1 by 34 degrees
- `C13`: Press down the tilt angle  of 3228887_4 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251610_1
- `C15`: Check test server and transmission issues
- `C16`: Increase transmission power for 3251610_1
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase transmission power for 3268643_3
- `C19`: Adjust the azimuth of 3228887_4 by 50 degrees
- `C20`: Decrease A3 Offset threshold for 3251610_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268643_3
- `C22`: Decrease transmission power for 3268643_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.410 | MS1 | 121.4656583786 | 31.1446317182 | 411 | 504990 | -86.87 | 17.44 | 379.63 | 0.13 | 2.11 | 1567 |
| 2024-09-20 22:21:32.714 | MS1 | 121.4656706011 | 31.1446210375 | 411 | 504990 | -85.36 | 12.28 | 420.57 | 0.19 | 2.42 | 1572 |
| 2024-09-20 22:21:33.862 | MS1 | 121.4656750486 | 31.1446227088 | 411 | 504990 | -86.36 | 15.84 | 330.26 | 0.13 | 2.10 | 1585 |
| 2024-09-20 22:21:34.236 | MS1 | 121.4656631897 | 31.1446295688 | 411 | 504990 | -88.42 | 17.50 | 75.32 | 0.05 | 2.48 | 1581 |
| 2024-09-20 22:21:35.180 | MS1 | 121.4656690250 | 31.1446333901 | 411 | 504990 | -90.97 | 17.82 | 83.16 | 0.09 | 2.94 | 1585 |
| 2024-09-20 22:21:36.292 | MS1 | 121.4656750789 | 31.1446290465 | 411 | 504990 | -86.69 | 13.98 | 56.83 | 0.12 | 2.21 | 1590 |
| 2024-09-20 22:21:37.593 | MS1 | 121.4656658579 | 31.1446349630 | 411 | 504990 | -89.67 | 12.84 | 58.40 | 0.20 | 2.49 | 1576 |
| 2024-09-20 22:21:38.834 | MS1 | 121.4656604898 | 31.1446220304 | 411 | 504990 | -93.17 | 9.88 | 71.37 | 0.19 | 2.73 | 1584 |
| 2024-09-20 22:21:39.618 | MS1 | 121.4656619445 | 31.1446246374 | 411 | 504990 | -89.82 | 12.75 | 64.60 | 0.14 | 2.44 | 1581 |
| 2024-09-20 22:21:40.509 | MS1 | 121.4656757537 | 31.1446323155 | 411 | 504990 | -93.01 | 7.49 | 345.26 | 0.09 | 2.59 | 1585 |
| 2024-09-20 22:21:41.688 | MS1 | 121.4656596591 | 31.1446180262 | 411 | 504990 | -90.68 | 11.56 | 503.13 | 0.03 | 2.87 | 1585 |
| 2024-09-20 22:21:42.414 | MS1 | 121.4656603154 | 31.1446292035 | 411 | 504990 | -92.37 | 11.02 | 582.56 | 0.03 | 2.01 | 1598 |

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
| 3228887 | 4 | 121.4748232518 | 31.1520449777 | 93 | 7 | 3 | 24.0 | TDD | 543 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3251610 | 1 | 121.4719032199 | 31.1544542897 | 242 | 3 | 12 | 33.3 | TDD | 411 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3258983 | 2 | 121.4644182992 | 31.1495575648 | 182 | 2 | 12 | 49.2 | TDD | 116 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3268643 | 3 | 121.4727657432 | 31.1554089379 | 111 | 8 | 5 | 49.3 | TDD | 574 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.946 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.969 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.091 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.091 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.794 | NREventA3 | measId:2;ServCellPCI:141;Se... |
| 2024-09-20 22:21:38.034 | NRHandoverAttempt | SourcePCI:141;SourceNR-ARFC... |
| 2024-09-20 22:21:38.081 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.093 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.214 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.214 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251610 | 1 | 92.7373 | 75.6132 | -117.5909 | 11.6300 | 143.4197 | 0.0157 | 0.0196 |
| 2024_09_20 22:00 | 3258983 | 2 | 14.1949 | 12.7644 | -117.8989 | 13.3025 | 112.3440 | 0.0189 | 0.0083 |
| 2024_09_20 22:00 | 3268643 | 3 | 12.6153 | 12.3345 | -114.4309 | 9.8490 | 126.0508 | 0.0143 | 0.0003 |
| 2024_09_20 22:00 | 3228887 | 4 | 18.3309 | 11.8537 | -116.0913 | 19.7142 | 131.1851 | 0.0145 | 0.0103 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413748_9C8C2444 | 504990 | 411 | -89.8 | 504990 | 574 | -93.5 | 504990 | 543 | -97.1 | 504990 | 116 |
| MR_1774413748_3D515F9B | 504990 | 411 | -87.5 | 504990 | 574 | -94.3 | 504990 | 543 | -96.6 | 504990 | 116 |
| MR_1774413748_9FD0CEA4 | 504990 | 411 | -86.6 | 504990 | 574 | -94.6 | 504990 | 543 | -98.9 | 504990 | 116 |
| MR_1774413748_23BAD1A6 | 504990 | 411 | -86.8 | 504990 | 574 | -96.0 | 504990 | 543 | -97.9 | 504990 | 116 |
| MR_1774413748_B1CB6A5F | 504990 | 411 | -88.2 | 504990 | 574 | -94.3 | 504990 | 543 | -95.3 | 504990 | 116 |
| MR_1774413748_8D7B798E | 504990 | 411 | -86.8 | 504990 | 574 | -94.7 | 504990 | 543 | -96.0 | 504990 | 116 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 12: `a7b35fcb-2fe...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a7b35fcb-2fe5-4c3a-bf50-58fd5f3d7d1b` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[12] topology](images/test_0012.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261833_3
- `C2`: Increase A3 Offset threshold for 3261833_3
- `C3`: Decrease transmission power for 3261833_3
- `C4`: Lift the tilt angle of 3277409_1 by 10 degrees
- `C5`: Press down the tilt angle of 3277409_1 by 10 degrees
- `C6`: Adjust the azimuth of 3261833_3 by 50 degrees
- `C7`: Add neighbor relationship between 3277409_1 and 3261833_3
- `C8`: Adjust the azimuth of 3277409_1 by 50 degrees
- `C9`: Check test server and transmission issues
- `C10`: Decrease A3 Offset threshold for 3261833_3
- `C11`: Decrease transmission power for 3277409_1
- `C12`: Add neighbor relationship between 3279331_2 and 3261833_3
- `C13`: Lift the tilt angle  of 3261833_3 by 2 degrees
- `C14`: Decrease A3 Offset threshold for 3277409_1
- `C15`: Increase A3 Offset threshold for 3277409_1
- `C16`: Increase transmission power for 3261833_3
- `C17`: Increase transmission power for 3277409_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261833_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277409_1
- `C20`: Press down the tilt angle  of 3261833_3 by 2 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277409_1
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.563 | MS1 | 121.4656672517 | 31.1446374917 | 960 | 504990 | -85.36 | 16.26 | 330.44 | 0.15 | 2.68 | 1569 |
| 2024-09-20 22:21:32.417 | MS1 | 121.4656744837 | 31.1446264059 | 960 | 504990 | -88.78 | 15.67 | 435.21 | 0.14 | 2.21 | 1590 |
| 2024-09-20 22:21:33.592 | MS1 | 121.4656757206 | 31.1446227339 | 960 | 504990 | -87.15 | 16.84 | 386.46 | 0.08 | 2.78 | 1574 |
| 2024-09-20 22:21:34.160 | MS1 | 121.4656733514 | 31.1446351311 | 960 | 504990 | -87.15 | 15.12 | 87.56 | 0.12 | 2.23 | 1580 |
| 2024-09-20 22:21:35.263 | MS1 | 121.4656637393 | 31.1446248131 | 960 | 504990 | -87.76 | 15.96 | 98.32 | 0.13 | 2.36 | 1586 |
| 2024-09-20 22:21:36.608 | MS1 | 121.4656614114 | 31.1446329964 | 960 | 504990 | -88.39 | 13.65 | 87.25 | 0.17 | 2.59 | 1575 |
| 2024-09-20 22:21:37.964 | MS1 | 121.4656645544 | 31.1446270323 | 960 | 504990 | -92.11 | 12.43 | 78.88 | 0.07 | 2.19 | 1599 |
| 2024-09-20 22:21:38.358 | MS1 | 121.4656686932 | 31.1446352679 | 960 | 504990 | -92.50 | 12.04 | 92.10 | 0.05 | 2.35 | 1565 |
| 2024-09-20 22:21:39.853 | MS1 | 121.4656776346 | 31.1446309581 | 960 | 504990 | -91.67 | 8.24 | 99.43 | 0.09 | 2.25 | 1588 |
| 2024-09-20 22:21:40.712 | MS1 | 121.4656710150 | 31.1446205718 | 960 | 504990 | -92.06 | 11.84 | 381.83 | 0.01 | 2.57 | 1561 |
| 2024-09-20 22:21:41.970 | MS1 | 121.4656699428 | 31.1446182611 | 960 | 504990 | -91.47 | 7.67 | 587.74 | 0.10 | 2.82 | 1593 |
| 2024-09-20 22:21:42.941 | MS1 | 121.4656654694 | 31.1446290414 | 960 | 504990 | -90.35 | 10.52 | 487.13 | 0.10 | 2.58 | 1581 |

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
| 3234934 | 4 | 121.4708580777 | 31.1557125174 | 162 | 15 | 0 | 35.8 | TDD | 103 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3261833 | 3 | 121.4642628918 | 31.1531113237 | 19 | 1 | 2 | 15.3 | TDD | 59 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3277409 | 1 | 121.4658489662 | 31.1510248130 | 7 | 9 | 1 | 35.2 | TDD | 960 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3279331 | 2 | 121.4683967401 | 31.1442396956 | 332 | 5 | 2 | 31.3 | TDD | 991 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.966 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.990 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.112 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.112 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.798 | NREventA3 | measId:2;ServCellPCI:756;Se... |
| 2024-09-20 22:21:38.038 | NRHandoverAttempt | SourcePCI:756;SourceNR-ARFC... |
| 2024-09-20 22:21:38.085 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.099 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.222 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.222 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3277409 | 1 | 86.1109 | 85.2127 | -114.9692 | 10.0460 | 174.7373 | 0.0074 | 0.0106 |
| 2024_09_19 22:00 | 3279331 | 2 | 90.8570 | 82.3614 | -115.2460 | 5.5476 | 115.3053 | 0.0036 | 0.0134 |
| 2024_09_19 22:00 | 3261833 | 3 | 91.2962 | 92.2217 | -116.3293 | 8.6397 | 98.1565 | 0.0188 | 0.0090 |
| 2024_09_19 22:00 | 3234934 | 4 | 92.6048 | 92.6256 | -117.2033 | 8.5143 | 170.0527 | 0.0025 | 0.0100 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412795_8BA60F68 | 504990 | 960 | -88.3 | 504990 | 59 | -93.0 | 504990 | 991 | -98.0 | 504990 | 103 |
| MR_1774412795_95F20F58 | 504990 | 960 | -85.2 | 504990 | 59 | -93.1 | 504990 | 991 | -98.8 | 504990 | 103 |
| MR_1774412795_AF83698C | 504990 | 960 | -85.4 | 504990 | 59 | -94.2 | 504990 | 991 | -99.8 | 504990 | 103 |
| MR_1774412795_9251BC63 | 504990 | 960 | -86.7 | 504990 | 59 | -91.4 | 504990 | 991 | -99.1 | 504990 | 103 |
| MR_1774412795_41672F2A | 504990 | 960 | -88.8 | 504990 | 59 | -93.8 | 504990 | 991 | -98.2 | 504990 | 103 |
| MR_1774412795_B86EB9E0 | 504990 | 960 | -87.3 | 504990 | 59 | -92.6 | 504990 | 991 | -96.8 | 504990 | 103 |
| MR_1774412795_8BED1BAF | 504990 | 960 | -86.5 | 504990 | 59 | -92.8 | 504990 | 991 | -97.4 | 504990 | 103 |
| MR_1774412795_CF91C42B | 504990 | 960 | -85.8 | 504990 | 59 | -91.5 | 504990 | 991 | -97.6 | 504990 | 103 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 13: `b0ef4fd7-e69...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b0ef4fd7-e69f-4659-b71b-a5af2b53c24d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[13] topology](images/test_0013.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Lift the tilt angle of 3258873_1 by 3 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258873_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257793_2
- `C5`: Decrease transmission power for 3257793_2
- `C6`: Increase A3 Offset threshold for 3258873_1
- `C7`: Press down the tilt angle  of 3257793_2 by 6 degrees
- `C8`: Adjust the azimuth of 3258873_1 by 50 degrees
- `C9`: Increase transmission power for 3258873_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258873_1
- `C11`: Decrease A3 Offset threshold for 3257793_2
- `C12`: Check test server and transmission issues
- `C13`: Increase transmission power for 3257793_2
- `C14`: Press down the tilt angle of 3258873_1 by 3 degrees
- `C15`: Decrease transmission power for 3258873_1
- `C16`: Decrease A3 Offset threshold for 3258873_1
- `C17`: Add neighbor relationship between 3253474_3 and 3257793_2
- `C18`: Increase A3 Offset threshold for 3257793_2
- `C19`: Add neighbor relationship between 3258873_1 and 3257793_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257793_2
- `C21`: Lift the tilt angle  of 3257793_2 by 6 degrees
- `C22`: Adjust the azimuth of 3257793_2 by 32 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.807 | MS1 | 121.4656610288 | 31.1446331852 | 696 | 504990 | -80.32 | 15.93 | 338.50 | 0.15 | 2.55 | 1565 |
| 2024-09-20 22:21:32.389 | MS1 | 121.4656747675 | 31.1446318309 | 696 | 504990 | -79.16 | 12.75 | 403.76 | 0.01 | 2.93 | 1585 |
| 2024-09-20 22:21:33.534 | MS1 | 121.4656730140 | 31.1446222771 | 696 | 504990 | -78.33 | 15.77 | 302.37 | 0.20 | 2.55 | 1562 |
| 2024-09-20 22:21:34.552 | MS1 | 121.4656751830 | 31.1446229935 | 696 | 504990 | -92.41 | -2.03 | 49.67 | 0.07 | 1.05 | 1581 |
| 2024-09-20 22:21:35.276 | MS1 | 121.4656584440 | 31.1446227772 | 696 | 504990 | -85.17 | -0.14 | 58.17 | 0.18 | 1.28 | 1581 |
| 2024-09-20 22:21:36.510 | MS1 | 121.4656746774 | 31.1446376037 | 696 | 504990 | -86.84 | -1.12 | 66.92 | 0.03 | 1.28 | 1576 |
| 2024-09-20 22:21:37.416 | MS1 | 121.4656769516 | 31.1446201885 | 696 | 504990 | -87.11 | -3.58 | 36.30 | 0.18 | 1.37 | 1592 |
| 2024-09-20 22:21:38.786 | MS1 | 121.4656617403 | 31.1446349367 | 696 | 504990 | -80.71 | 13.37 | 377.12 | 0.08 | 1.22 | 1595 |
| 2024-09-20 22:21:39.343 | MS1 | 121.4656771480 | 31.1446226098 | 696 | 504990 | -79.34 | 17.63 | 472.47 | 0.12 | 1.39 | 1574 |
| 2024-09-20 22:21:40.659 | MS1 | 121.4656644559 | 31.1446187724 | 696 | 504990 | -75.14 | 15.32 | 477.42 | 0.06 | 2.23 | 1578 |
| 2024-09-20 22:21:41.404 | MS1 | 121.4656725646 | 31.1446239527 | 696 | 504990 | -76.31 | 15.85 | 402.24 | 0.14 | 2.77 | 1579 |
| 2024-09-20 22:21:42.823 | MS1 | 121.4656624869 | 31.1446343859 | 696 | 504990 | -80.86 | 13.96 | 414.88 | 0.10 | 2.39 | 1583 |

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
| 3228664 | 4 | 121.4728977860 | 31.1538317832 | 307 | 0 | 9 | 24.0 | TDD | 575 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3253474 | 3 | 121.4682767940 | 31.1507220188 | 292 | 3 | 11 | 38.1 | TDD | 845 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3257793 | 2 | 121.4744878889 | 31.1466531415 | 287 | 3 | 11 | 40.1 | TDD | 632 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3258873 | 1 | 121.4742820131 | 31.1495614750 | 86 | 2 | 3 | 19.3 | TDD | 696 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.554 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.572 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.683 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.683 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.438 | NREventA3 | measId:2;ServCellPCI:257;Se... |
| 2024-09-20 22:21:36.438 | NREventA3 | measId:2;ServCellPCI:257;Se... |
| 2024-09-20 22:21:37.438 | NREventA3 | measId:2;ServCellPCI:257;Se... |
| 2024-09-20 22:21:39.938 | NRRRCReestablishAttempt | PCI:257 |
| 2024-09-20 22:21:39.951 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.962 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:40.094 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.094 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258873 | 1 | 11.9481 | 9.9529 | -116.3198 | 7.0199 | 198.6901 | 0.0157 | 0.1161 |
| 2024_09_20 22:00 | 3257793 | 2 | 16.5046 | 16.9613 | -116.7629 | 5.9041 | 88.0691 | 0.0103 | 0.0027 |
| 2024_09_20 22:00 | 3253474 | 3 | 15.0627 | 10.5178 | -115.9070 | 12.3526 | 119.8982 | 0.0174 | 0.0151 |
| 2024_09_20 22:00 | 3228664 | 4 | 18.7948 | 9.2351 | -117.8198 | 17.3061 | 174.8244 | 0.0044 | 0.0195 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414767_96F11D76 | 504990 | 632 | -89.3 | 504990 | 696 | -90.7 | 504990 | 845 | -95.2 | 504990 | 575 |
| MR_1774414767_9CA60B94 | 504990 | 696 | -90.6 | 504990 | 632 | -87.3 | 504990 | 845 | -96.8 | 504990 | 575 |
| MR_1774414767_DE6C1B71 | 504990 | 632 | -87.4 | 504990 | 696 | -92.9 | 504990 | 845 | -94.3 | 504990 | 575 |
| MR_1774414767_2BA90639 | 504990 | 696 | -90.8 | 504990 | 632 | -86.6 | 504990 | 845 | -94.9 | 504990 | 575 |
| MR_1774414767_1C74CA21 | 504990 | 696 | -93.4 | 504990 | 632 | -86.8 | 504990 | 845 | -97.7 | 504990 | 575 |
| MR_1774414767_2902274D | 504990 | 696 | -92.3 | 504990 | 632 | -88.6 | 504990 | 845 | -95.0 | 504990 | 575 |
| MR_1774414767_E50D3DE3 | 504990 | 696 | -92.4 | 504990 | 632 | -89.4 | 504990 | 845 | -97.9 | 504990 | 575 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 14: `6f1825be-13f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6f1825be-13f8-4604-948b-aac796e32344` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[14] topology](images/test_0014.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3226314_2
- `C2`: Adjust the azimuth of 3276042_1 by 50 degrees
- `C3`: Increase transmission power for 3226314_2
- `C4`: Adjust the azimuth of 3226314_2 by 50 degrees
- `C5`: Decrease transmission power for 3226314_2
- `C6`: Increase A3 Offset threshold for 3276042_1
- `C7`: Increase transmission power for 3276042_1
- `C8`: Decrease A3 Offset threshold for 3226314_2
- `C9`: Decrease A3 Offset threshold for 3276042_1
- `C10`: Press down the tilt angle of 3276042_1 by 10 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276042_1
- `C12`: Lift the tilt angle  of 3226314_2 by 6 degrees
- `C13`: Add neighbor relationship between 3276042_1 and 3226314_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226314_2
- `C15`: Press down the tilt angle  of 3226314_2 by 6 degrees
- `C16`: Lift the tilt angle of 3276042_1 by 10 degrees
- `C17`: Decrease transmission power for 3276042_1
- `C18`: Add neighbor relationship between 3239887_4 and 3226314_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276042_1
- `C20`: Check test server and transmission issues
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226314_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.325 | MS1 | 121.4656735918 | 31.1446238091 | 233 | 504990 | -82.13 | 15.99 | 372.64 | 0.17 | 2.05 | 1592 |
| 2024-09-20 22:21:32.801 | MS1 | 121.4656709847 | 31.1446345760 | 233 | 504990 | -77.27 | 12.32 | 412.87 | 0.14 | 2.34 | 1572 |
| 2024-09-20 22:21:33.422 | MS1 | 121.4656690022 | 31.1446267641 | 233 | 504990 | -77.31 | 12.42 | 510.55 | 0.18 | 2.45 | 1573 |
| 2024-09-20 22:21:34.822 | MS1 | 121.4656677606 | 31.1446280571 | 233 | 504990 | -87.75 | -2.58 | 58.56 | 0.03 | 1.11 | 1588 |
| 2024-09-20 22:21:35.403 | MS1 | 121.4656767680 | 31.1446295396 | 233 | 504990 | -88.29 | -1.47 | 41.09 | 0.09 | 1.49 | 1561 |
| 2024-09-20 22:21:36.685 | MS1 | 121.4656739137 | 31.1446328293 | 233 | 504990 | -90.33 | -3.06 | 41.03 | 0.05 | 1.31 | 1593 |
| 2024-09-20 22:21:37.220 | MS1 | 121.4656590304 | 31.1446189474 | 233 | 504990 | -89.73 | -2.77 | 65.03 | 0.00 | 1.26 | 1577 |
| 2024-09-20 22:21:38.247 | MS1 | 121.4656663897 | 31.1446375830 | 233 | 504990 | -90.03 | -0.74 | 50.74 | 0.02 | 1.28 | 1567 |
| 2024-09-20 22:21:39.706 | MS1 | 121.4656648100 | 31.1446316827 | 134 | 504990 | -83.35 | 13.14 | 215.93 | 0.08 | 1.31 | 1571 |
| 2024-09-20 22:21:40.513 | MS1 | 121.4656644740 | 31.1446195536 | 134 | 504990 | -77.10 | 17.95 | 517.16 | 0.15 | 2.09 | 1599 |
| 2024-09-20 22:21:41.245 | MS1 | 121.4656726220 | 31.1446361579 | 134 | 504990 | -81.25 | 12.84 | 375.34 | 0.05 | 2.52 | 1567 |
| 2024-09-20 22:21:42.313 | MS1 | 121.4656695849 | 31.1446317429 | 134 | 504990 | -81.27 | 16.27 | 333.32 | 0.06 | 2.74 | 1578 |

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
| 3226314 | 2 | 121.4731605342 | 31.1520998704 | 92 | 4 | 11 | 39.4 | TDD | 134 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3239887 | 4 | 121.4662766717 | 31.1516303696 | 250 | 8 | 1 | 21.1 | TDD | 889 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3269916 | 3 | 121.4745786067 | 31.1529945926 | 80 | 13 | 12 | 34.6 | TDD | 230 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3276042 | 1 | 121.4652589861 | 31.1460775378 | 232 | 5 | 1 | 25.1 | TDD | 233 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.291 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.417 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.417 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.146 | NREventA3 | measId:2;ServCellPCI:626;Se... |
| 2024-09-20 22:21:38.386 | NRHandoverAttempt | SourcePCI:626;SourceNR-ARFC... |
| 2024-09-20 22:21:38.421 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.434 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.535 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.535 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276042 | 1 | 16.7415 | 6.9719 | -116.5182 | 5.3918 | 139.3642 | 0.0136 | 0.1081 |
| 2024_09_20 22:00 | 3226314 | 2 | 14.1292 | 9.4282 | -117.0583 | 11.9298 | 160.2277 | 0.0146 | 0.0109 |
| 2024_09_20 22:00 | 3269916 | 3 | 19.9097 | 19.3969 | -117.2324 | 10.7234 | 154.0894 | 0.0126 | 0.0025 |
| 2024_09_20 22:00 | 3239887 | 4 | 6.5544 | 6.1518 | -114.7291 | 18.6411 | 152.9158 | 0.0113 | 0.0193 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414022_6736161D | 504990 | 233 | -88.1 | 504990 | 134 | -83.8 | 504990 | 889 | -84.5 | 504990 | 230 |
| MR_1774414022_E9A74323 | 504990 | 233 | -88.7 | 504990 | 134 | -83.9 | 504990 | 889 | -83.3 | 504990 | 230 |
| MR_1774414022_343DD5F3 | 504990 | 134 | -81.8 | 504990 | 233 | -89.3 | 504990 | 889 | -81.8 | 504990 | 230 |
| MR_1774414022_EB2DABAE | 504990 | 233 | -88.5 | 504990 | 134 | -81.6 | 504990 | 889 | -81.6 | 504990 | 230 |
| MR_1774414022_B24AECC7 | 504990 | 233 | -86.4 | 504990 | 134 | -83.8 | 504990 | 889 | -82.6 | 504990 | 230 |
| MR_1774414022_E285E0B6 | 504990 | 233 | -86.2 | 504990 | 134 | -82.8 | 504990 | 889 | -82.2 | 504990 | 230 |
| MR_1774414022_76322DE1 | 504990 | 233 | -89.6 | 504990 | 134 | -81.7 | 504990 | 889 | -84.1 | 504990 | 230 |
| MR_1774414022_FE22FACF | 504990 | 233 | -87.8 | 504990 | 134 | -83.4 | 504990 | 889 | -84.7 | 504990 | 230 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 15: `74abdf87-76b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `74abdf87-76b3-434f-aecf-735dd4d82345` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[15] topology](images/test_0015.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase A3 Offset threshold for 3217635_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217635_2
- `C4`: Decrease A3 Offset threshold for 3263986_4
- `C5`: Decrease transmission power for 3263986_4
- `C6`: Lift the tilt angle of 3263986_4 by 3 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263986_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217635_2
- `C9`: Increase transmission power for 3217635_2
- `C10`: Adjust the azimuth of 3263986_4 by 25 degrees
- `C11`: Check test server and transmission issues
- `C12`: Increase transmission power for 3263986_4
- `C13`: Press down the tilt angle of 3263986_4 by 3 degrees
- `C14`: Decrease A3 Offset threshold for 3217635_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263986_4
- `C16`: Press down the tilt angle  of 3217635_2 by 5 degrees
- `C17`: Increase A3 Offset threshold for 3263986_4
- `C18`: Add neighbor relationship between 3272714_5 and 3217635_2
- `C19`: Decrease transmission power for 3217635_2
- `C20`: Add neighbor relationship between 3263986_4 and 3217635_2
- `C21`: Adjust the azimuth of 3217635_2 by 35 degrees
- `C22`: Lift the tilt angle  of 3217635_2 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.162 | MS1 | 121.4656774852 | 31.1446223939 | 110 | 504990 | -80.58 | 16.06 | 416.99 | 0.08 | 2.53 | 1574 |
| 2024-09-20 22:21:32.640 | MS1 | 121.4656696136 | 31.1446366646 | 110 | 504990 | -75.85 | 14.02 | 439.11 | 0.08 | 2.60 | 1592 |
| 2024-09-20 22:21:33.538 | MS1 | 121.4656598493 | 31.1446318667 | 110 | 504990 | -77.61 | 15.87 | 493.00 | 0.03 | 2.91 | 1564 |
| 2024-09-20 22:21:34.238 | MS1 | 121.4656771003 | 31.1446250300 | 204 | 504990 | -84.50 | 4.34 | 78.08 | 0.13 | 1.08 | 1560 |
| 2024-09-20 22:21:35.625 | MS1 | 121.4656604490 | 31.1446187317 | 204 | 504990 | -81.20 | 3.06 | 51.39 | 0.09 | 1.05 | 1591 |
| 2024-09-20 22:21:36.979 | MS1 | 121.4656646142 | 31.1446229021 | 110 | 504990 | -89.90 | 2.60 | 74.48 | 0.09 | 1.28 | 1565 |
| 2024-09-20 22:21:37.691 | MS1 | 121.4656763717 | 31.1446231850 | 110 | 504990 | -82.28 | 4.61 | 27.48 | 0.11 | 1.47 | 1567 |
| 2024-09-20 22:21:38.434 | MS1 | 121.4656729755 | 31.1446224151 | 204 | 504990 | -84.57 | 1.86 | 47.25 | 0.19 | 1.47 | 1560 |
| 2024-09-20 22:21:39.641 | MS1 | 121.4656671400 | 31.1446230243 | 204 | 504990 | -82.92 | 4.94 | 44.95 | 0.09 | 1.47 | 1575 |
| 2024-09-20 22:21:40.388 | MS1 | 121.4656731275 | 31.1446208809 | 204 | 504990 | -79.40 | 16.03 | 421.44 | 0.04 | 2.21 | 1586 |
| 2024-09-20 22:21:41.632 | MS1 | 121.4656632146 | 31.1446196153 | 204 | 504990 | -76.69 | 14.74 | 448.17 | 0.16 | 2.28 | 1588 |
| 2024-09-20 22:21:42.499 | MS1 | 121.4656581374 | 31.1446287012 | 204 | 504990 | -82.52 | 16.68 | 500.43 | 0.04 | 2.05 | 1560 |

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
| 3217635 | 2 | 121.4642226976 | 31.1495145586 | 201 | 1 | 9 | 42.3 | TDD | 1000 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3220806 | 1 | 121.4683676608 | 31.1445511224 | 161 | 3 | 8 | 42.8 | TDD | 903 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3252405 | 3 | 121.4702799750 | 31.1446476384 | 152 | 0 | 1 | 15.2 | TDD | 204 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3263986 | 4 | 121.4697126698 | 31.1479827758 | 251 | 0 | 11 | 24.3 | TDD | 110 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3272714 | 5 | 121.4747790256 | 31.1476093139 | 5 | 11 | 9 | 42.5 | TDD | 606 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.781 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.804 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.935 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.935 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.613 | NREventA3 | measId:2;ServCellPCI:511;Se... |
| 2024-09-20 22:21:33.853 | NRHandoverAttempt | SourcePCI:511;SourceNR-ARFC... |
| 2024-09-20 22:21:33.893 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:33.907 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:34.008 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.008 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.613 | NREventA3 | measId:2;ServCellPCI:889;Se... |
| 2024-09-20 22:21:35.853 | NRHandoverAttempt | SourcePCI:889;SourceNR-ARFC... |
| 2024-09-20 22:21:35.886 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.898 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:36.009 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.009 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.613 | NREventA3 | measId:2;ServCellPCI:511;Se... |
| 2024-09-20 22:21:37.853 | NRHandoverAttempt | SourcePCI:511;SourceNR-ARFC... |
| 2024-09-20 22:21:37.884 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.894 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.030 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.030 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220806 | 1 | 18.8285 | 17.4336 | -115.1010 | 11.1240 | 98.7658 | 0.0169 | 0.0199 |
| 2024_09_20 22:00 | 3217635 | 2 | 10.0939 | 12.4829 | -115.6481 | 19.3469 | 168.2652 | 0.0171 | 0.0017 |
| 2024_09_20 22:00 | 3252405 | 3 | 6.8233 | 6.7092 | -117.0511 | 7.3778 | 104.4697 | 0.0151 | 0.0015 |
| 2024_09_20 22:00 | 3263986 | 4 | 9.2661 | 12.7804 | -114.0458 | 16.7401 | 140.0376 | 0.0088 | 0.0100 |
| 2024_09_20 22:00 | 3272714 | 5 | 18.0947 | 11.0552 | -116.3365 | 11.4782 | 189.8895 | 0.0072 | 0.0170 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415836_AF002C61 | 504990 | 204 | -84.1 | 504990 | 110 | -78.8 | 504990 | 1000 | -84.0 | 504990 | 606 |
| MR_1774415836_42B64D6C | 504990 | 204 | -86.0 | 504990 | 110 | -80.4 | 504990 | 1000 | -81.3 | 504990 | 606 |
| MR_1774415836_99F21731 | 504990 | 110 | -84.4 | 504990 | 204 | -78.8 | 504990 | 1000 | -84.0 | 504990 | 606 |
| MR_1774415836_EA288FB5 | 504990 | 204 | -82.5 | 504990 | 110 | -79.2 | 504990 | 1000 | -81.6 | 504990 | 606 |
| MR_1774415836_67D84A1C | 504990 | 204 | -84.1 | 504990 | 110 | -81.5 | 504990 | 1000 | -82.5 | 504990 | 606 |
| MR_1774415836_9B1963AC | 504990 | 110 | -84.4 | 504990 | 204 | -79.3 | 504990 | 1000 | -83.2 | 504990 | 606 |
| MR_1774415836_47827F51 | 504990 | 204 | -85.7 | 504990 | 110 | -80.1 | 504990 | 1000 | -82.4 | 504990 | 606 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 16: `acb898f7-5e9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `acb898f7-5e9f-4c39-ba2f-ac677ae6355c` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[16] topology](images/test_0016.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3247667_2
- `C2`: Decrease A3 Offset threshold for 3245655_4
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Adjust the azimuth of 3247667_2 by 49 degrees
- `C5`: Increase transmission power for 3247667_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247667_2
- `C7`: Adjust the azimuth of 3245655_4 by 50 degrees
- `C8`: Lift the tilt angle of 3245655_4 by 10 degrees
- `C9`: Add neighbor relationship between 3245655_4 and 3247667_2
- `C10`: Increase transmission power for 3245655_4
- `C11`: Check test server and transmission issues
- `C12`: Decrease transmission power for 3247667_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245655_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245655_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247667_2
- `C16`: Decrease A3 Offset threshold for 3247667_2
- `C17`: Decrease transmission power for 3245655_4
- `C18`: Press down the tilt angle of 3245655_4 by 10 degrees
- `C19`: Press down the tilt angle  of 3247667_2 by 5 degrees
- `C20`: Add neighbor relationship between 3270925_1 and 3247667_2
- `C21`: Lift the tilt angle  of 3247667_2 by 5 degrees
- `C22`: Increase A3 Offset threshold for 3245655_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.907 | MS1 | 121.4656696881 | 31.1446213847 | 965 | 504990 | -84.67 | 17.79 | 485.50 | 0.07 | 2.46 | 1596 |
| 2024-09-20 22:21:32.518 | MS1 | 121.4656588255 | 31.1446309846 | 965 | 504990 | -83.30 | 17.47 | 584.36 | 0.20 | 2.15 | 1569 |
| 2024-09-20 22:21:33.131 | MS1 | 121.4656623802 | 31.1446280985 | 965 | 504990 | -80.84 | 12.89 | 325.22 | 0.13 | 2.25 | 1599 |
| 2024-09-20 22:21:34.835 | MS1 | 121.4656689582 | 31.1446306471 | 965 | 504990 | -88.94 | -1.97 | 37.78 | 0.10 | 1.19 | 1578 |
| 2024-09-20 22:21:35.271 | MS1 | 121.4656700616 | 31.1446215655 | 965 | 504990 | -91.51 | -2.81 | 51.29 | 0.05 | 1.26 | 1591 |
| 2024-09-20 22:21:36.107 | MS1 | 121.4656725454 | 31.1446207645 | 965 | 504990 | -91.25 | -2.28 | 40.79 | 0.04 | 1.14 | 1584 |
| 2024-09-20 22:21:37.347 | MS1 | 121.4656639861 | 31.1446378438 | 965 | 504990 | -87.80 | -0.98 | 47.05 | 0.19 | 1.49 | 1586 |
| 2024-09-20 22:21:38.135 | MS1 | 121.4656777761 | 31.1446279185 | 965 | 504990 | -77.08 | 17.56 | 450.80 | 0.03 | 1.26 | 1594 |
| 2024-09-20 22:21:39.289 | MS1 | 121.4656668973 | 31.1446355216 | 965 | 504990 | -77.13 | 12.07 | 345.64 | 0.02 | 1.46 | 1567 |
| 2024-09-20 22:21:40.293 | MS1 | 121.4656580399 | 31.1446198788 | 965 | 504990 | -79.50 | 16.15 | 424.97 | 0.19 | 2.74 | 1575 |
| 2024-09-20 22:21:41.932 | MS1 | 121.4656605943 | 31.1446359996 | 965 | 504990 | -84.46 | 14.07 | 558.68 | 0.01 | 2.70 | 1562 |
| 2024-09-20 22:21:42.688 | MS1 | 121.4656602203 | 31.1446221943 | 965 | 504990 | -75.06 | 14.79 | 397.86 | 0.05 | 2.07 | 1575 |

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
| 3245655 | 4 | 121.4703182087 | 31.1506419335 | 339 | 7 | 3 | 39.9 | TDD | 965 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3247667 | 2 | 121.4737672566 | 31.1452532853 | 314 | 2 | 3 | 39.2 | TDD | 195 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3247692 | 3 | 121.4758775972 | 31.1463880249 | 135 | 14 | 9 | 21.7 | TDD | 1004 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3270925 | 1 | 121.4746865976 | 31.1535560903 | 17 | 15 | 1 | 32.9 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.491 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.513 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.661 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.661 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.309 | NREventA3 | measId:2;ServCellPCI:574;Se... |
| 2024-09-20 22:21:36.309 | NREventA3 | measId:2;ServCellPCI:574;Se... |
| 2024-09-20 22:21:37.309 | NREventA3 | measId:2;ServCellPCI:574;Se... |
| 2024-09-20 22:21:39.809 | NRRRCReestablishAttempt | PCI:574 |
| 2024-09-20 22:21:39.820 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.835 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.982 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.982 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270925 | 1 | 7.6635 | 19.5374 | -115.1091 | 18.2322 | 194.1574 | 0.0048 | 0.0115 |
| 2024_09_20 22:00 | 3247667 | 2 | 5.4149 | 10.6940 | -116.4589 | 6.8200 | 168.5816 | 0.0080 | 0.0087 |
| 2024_09_20 22:00 | 3247692 | 3 | 13.6081 | 6.1492 | -117.6052 | 18.8626 | 162.4498 | 0.0031 | 0.0160 |
| 2024_09_20 22:00 | 3245655 | 4 | 19.0339 | 15.5445 | -117.1559 | 5.0276 | 103.1930 | 0.0006 | 0.1615 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412844_2BEBF3EB | 504990 | 195 | -85.0 | 504990 | 965 | -88.2 | 504990 | 258 | -84.9 | 504990 | 1004 |
| MR_1774412844_137A04D3 | 504990 | 965 | -87.2 | 504990 | 195 | -83.2 | 504990 | 258 | -85.4 | 504990 | 1004 |
| MR_1774412844_0D893FC1 | 504990 | 195 | -83.7 | 504990 | 965 | -87.9 | 504990 | 258 | -86.2 | 504990 | 1004 |
| MR_1774412844_3004224A | 504990 | 195 | -83.8 | 504990 | 965 | -90.1 | 504990 | 258 | -88.3 | 504990 | 1004 |
| MR_1774412844_83F3A527 | 504990 | 195 | -85.2 | 504990 | 965 | -89.2 | 504990 | 258 | -87.7 | 504990 | 1004 |
| MR_1774412844_12FA9DC6 | 504990 | 965 | -89.6 | 504990 | 195 | -85.9 | 504990 | 258 | -88.3 | 504990 | 1004 |
| MR_1774412844_910355AF | 504990 | 965 | -90.4 | 504990 | 195 | -85.9 | 504990 | 258 | -87.0 | 504990 | 1004 |
| MR_1774412844_8A68FC48 | 504990 | 965 | -89.9 | 504990 | 195 | -85.5 | 504990 | 258 | -88.8 | 504990 | 1004 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 17: `06df7252-3bf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `06df7252-3bfe-4a3d-9806-189404de1c9b` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[17] topology](images/test_0017.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3239150_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239150_4
- `C3`: Add neighbor relationship between 3249480_3 and 3254483_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254483_1
- `C5`: Decrease transmission power for 3254483_1
- `C6`: Increase A3 Offset threshold for 3254483_1
- `C7`: Adjust the azimuth of 3239150_4 by 50 degrees
- `C8`: Decrease A3 Offset threshold for 3254483_1
- `C9`: Increase A3 Offset threshold for 3239150_4
- `C10`: Add neighbor relationship between 3239150_4 and 3254483_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239150_4
- `C12`: Lift the tilt angle of 3239150_4 by 2 degrees
- `C13`: Lift the tilt angle  of 3254483_1 by 10 degrees
- `C14`: Press down the tilt angle  of 3254483_1 by 10 degrees
- `C15`: Check test server and transmission issues
- `C16`: Press down the tilt angle of 3239150_4 by 2 degrees
- `C17`: Increase transmission power for 3254483_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254483_1
- `C19`: Decrease transmission power for 3239150_4
- `C20`: Increase transmission power for 3239150_4
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Adjust the azimuth of 3254483_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.479 | MS1 | 121.4656761904 | 31.1446231150 | 663 | 504990 | -81.89 | 15.81 | 560.46 | 0.12 | 2.39 | 1591 |
| 2024-09-20 22:21:32.604 | MS1 | 121.4656590754 | 31.1446286200 | 663 | 504990 | -76.16 | 17.93 | 471.26 | 0.04 | 2.07 | 1571 |
| 2024-09-20 22:21:33.453 | MS1 | 121.4656596413 | 31.1446364725 | 663 | 504990 | -82.08 | 12.50 | 451.08 | 0.09 | 2.51 | 1585 |
| 2024-09-20 22:21:34.743 | MS1 | 121.4656676624 | 31.1446206072 | 663 | 504990 | -84.08 | -2.07 | 42.45 | 0.12 | 1.10 | 1577 |
| 2024-09-20 22:21:35.707 | MS1 | 121.4656709207 | 31.1446305496 | 663 | 504990 | -86.10 | -0.50 | 64.39 | 0.12 | 1.25 | 1583 |
| 2024-09-20 22:21:36.548 | MS1 | 121.4656672145 | 31.1446267715 | 663 | 504990 | -92.27 | -1.34 | 69.08 | 0.09 | 1.48 | 1591 |
| 2024-09-20 22:21:37.583 | MS1 | 121.4656760735 | 31.1446264657 | 663 | 504990 | -87.81 | -2.89 | 46.48 | 0.05 | 1.05 | 1586 |
| 2024-09-20 22:21:38.681 | MS1 | 121.4656756917 | 31.1446228859 | 663 | 504990 | -88.41 | -3.91 | 57.57 | 0.05 | 1.16 | 1592 |
| 2024-09-20 22:21:39.531 | MS1 | 121.4656610215 | 31.1446224767 | 584 | 504990 | -83.53 | 13.74 | 228.64 | 0.14 | 1.11 | 1592 |
| 2024-09-20 22:21:40.546 | MS1 | 121.4656694869 | 31.1446257543 | 584 | 504990 | -77.00 | 17.11 | 306.00 | 0.19 | 2.83 | 1585 |
| 2024-09-20 22:21:41.327 | MS1 | 121.4656697529 | 31.1446228861 | 584 | 504990 | -78.37 | 12.04 | 342.47 | 0.19 | 2.33 | 1569 |
| 2024-09-20 22:21:42.591 | MS1 | 121.4656591920 | 31.1446315721 | 584 | 504990 | -78.45 | 17.27 | 393.99 | 0.16 | 2.17 | 1591 |

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
| 3235668 | 2 | 121.4660798414 | 31.1554756432 | 62 | 6 | 1 | 34.9 | TDD | 433 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3239150 | 4 | 121.4712838150 | 31.1550834542 | 141 | 0 | 4 | 43.1 | TDD | 663 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3249480 | 3 | 121.4753372878 | 31.1548120622 | 57 | 11 | 8 | 16.3 | TDD | 315 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3254483 | 1 | 121.4661940028 | 31.1522941868 | 309 | 15 | 3 | 42.3 | TDD | 584 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.328 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.344 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.494 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.494 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.181 | NREventA3 | measId:2;ServCellPCI:177;Se... |
| 2024-09-20 22:21:38.421 | NRHandoverAttempt | SourcePCI:177;SourceNR-ARFC... |
| 2024-09-20 22:21:38.455 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.465 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.602 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.602 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254483 | 1 | 6.4167 | 16.2839 | -117.9829 | 5.2733 | 174.3123 | 0.0082 | 0.0110 |
| 2024_09_20 22:00 | 3235668 | 2 | 15.9752 | 19.9677 | -117.0821 | 16.3456 | 109.0500 | 0.0084 | 0.0183 |
| 2024_09_20 22:00 | 3249480 | 3 | 9.6547 | 15.3063 | -115.0720 | 5.7774 | 177.7154 | 0.0174 | 0.0182 |
| 2024_09_20 22:00 | 3239150 | 4 | 11.1178 | 7.3460 | -117.3661 | 10.6674 | 149.4735 | 0.0000 | 0.1706 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412933_16C3B7CC | 504990 | 663 | -84.9 | 504990 | 584 | -80.5 | 504990 | 315 | -88.2 | 504990 | 433 |
| MR_1774412933_C9FD3044 | 504990 | 584 | -79.3 | 504990 | 663 | -82.4 | 504990 | 315 | -86.7 | 504990 | 433 |
| MR_1774412933_3E5D9E0C | 504990 | 663 | -82.7 | 504990 | 584 | -77.8 | 504990 | 315 | -89.9 | 504990 | 433 |
| MR_1774412933_75325BAF | 504990 | 663 | -82.8 | 504990 | 584 | -78.5 | 504990 | 315 | -89.9 | 504990 | 433 |
| MR_1774412933_95BA744B | 504990 | 663 | -82.9 | 504990 | 584 | -79.4 | 504990 | 315 | -89.9 | 504990 | 433 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 18: `e5930631-de9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e5930631-de96-4c81-bd7a-e1bbaaa9bede` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[18] topology](images/test_0018.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3222646_1
- `C2`: Press down the tilt angle of 3258910_5 by 4 degrees
- `C3`: Adjust the azimuth of 3258910_5 by 25 degrees
- `C4`: Increase A3 Offset threshold for 3222646_1
- `C5`: Add neighbor relationship between 3270722_11 and 3222646_1
- `C6`: Press down the tilt angle  of 3222646_1 by 2 degrees
- `C7`: Add neighbor relationship between 3258910_5 and 3222646_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258910_5
- `C9`: Adjust the azimuth of 3222646_1 by 40 degrees
- `C10`: Decrease transmission power for 3258910_5
- `C11`: Check test server and transmission issues
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Lift the tilt angle  of 3222646_1 by 2 degrees
- `C14`: Decrease A3 Offset threshold for 3222646_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258910_5
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222646_1
- `C17`: Decrease A3 Offset threshold for 3258910_5
- `C18`: Lift the tilt angle of 3258910_5 by 4 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222646_1
- `C20`: Increase transmission power for 3258910_5
- `C21`: Increase A3 Offset threshold for 3258910_5
- `C22`: Decrease transmission power for 3222646_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.432 | MS1 | 121.4656644934 | 31.1446323915 | 636 | 504990 | -93.69 | 10.39 | 433.10 | 0.09 | 2.86 | 1592 |
| 2024-09-20 22:21:32.604 | MS1 | 121.4656635012 | 31.1446313740 | 171 | 504990 | -94.96 | 13.57 | 299.46 | 0.16 | 2.94 | 1581 |
| 2024-09-20 22:21:33.636 | MS1 | 121.4656631057 | 31.1446252687 | 877 | 504990 | -95.71 | 10.68 | 594.65 | 0.08 | 2.69 | 1592 |
| 2024-09-20 22:21:34.705 | MS1 | 121.4656762036 | 31.1446239455 | 901 | 152650 | -87.54 | 7.68 | 72.47 | 0.18 | 1.81 | 951 |
| 2024-09-20 22:21:35.526 | MS1 | 121.4656600795 | 31.1446208686 | 475 | 152650 | -94.35 | 5.74 | 63.24 | 0.02 | 1.63 | 966 |
| 2024-09-20 22:21:36.320 | MS1 | 121.4656642866 | 31.1446214922 | 25 | 152650 | -87.66 | 7.70 | 90.66 | 0.15 | 1.55 | 965 |
| 2024-09-20 22:21:37.169 | MS1 | 121.4656604209 | 31.1446375813 | 387 | 152650 | -94.28 | 3.37 | 84.88 | 0.04 | 1.94 | 937 |
| 2024-09-20 22:21:38.797 | MS1 | 121.4656662419 | 31.1446252297 | 901 | 152650 | -96.53 | 6.60 | 87.48 | 0.06 | 1.93 | 975 |
| 2024-09-20 22:21:39.470 | MS1 | 121.4656589731 | 31.1446360025 | 475 | 152650 | -92.89 | 4.61 | 79.17 | 0.13 | 1.92 | 981 |
| 2024-09-20 22:21:40.870 | MS1 | 121.4656730960 | 31.1446379135 | 25 | 152650 | -91.90 | 6.14 | 70.80 | 0.18 | 2.38 | 1573 |
| 2024-09-20 22:21:41.309 | MS1 | 121.4656689110 | 31.1446270438 | 387 | 152650 | -90.20 | 7.54 | 72.33 | 0.15 | 2.94 | 1576 |
| 2024-09-20 22:21:42.491 | MS1 | 121.4656645222 | 31.1446301331 | 901 | 152650 | -90.13 | 7.82 | 42.18 | 0.00 | 2.22 | 1568 |

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
| 3210617 | 12 | 121.4710511259 | 31.1499293218 | 257 | 5 | 2 | 20.1 | FDD | 475 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3212066 | 10 | 121.4689124962 | 31.1526880611 | 37 | 0 | 12 | 12.4 | FDD | 554 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3220002 | 2 | 121.4745472534 | 31.1502285097 | 144 | 3 | 11 | 6.0 | TDD | 171 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3222453 | 13 | 121.4729009487 | 31.1444145498 | 15 | 4 | 4 | 1.7 | FDD | 990 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3222646 | 1 | 121.4727704718 | 31.1491703971 | 193 | 0 | 4 | 26.8 | TDD | 993 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3233007 | 7 | 121.4683127167 | 31.1537529243 | 69 | 10 | 0 | 19.0 | FDD | 387 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3244987 | 6 | 121.4667820870 | 31.1488998513 | 289 | 9 | 0 | 5.6 | TDD | 701 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3258496 | 8 | 121.4701439293 | 31.1544534314 | 140 | 7 | 11 | 7.9 | FDD | 901 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3258910 | 5 | 121.4678892918 | 31.1485675669 | 181 | 4 | 4 | 3.1 | TDD | 636 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3264810 | 4 | 121.4671527538 | 31.1489033002 | 327 | 0 | 10 | 13.2 | TDD | 981 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3269545 | 9 | 121.4665359345 | 31.1477037550 | 212 | 12 | 1 | 17.4 | FDD | 201 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3270722 | 11 | 121.4754104985 | 31.1528380516 | 270 | 11 | 6 | 4.7 | FDD | 25 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3277969 | 3 | 121.4700353206 | 31.1502951578 | 31 | 11 | 1 | 26.7 | TDD | 877 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.227 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.243 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.358 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.358 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.045 | NREventA2 | measId:1;ServCellPCI:703;Se... |
| 2024-09-20 22:21:35.182 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.401 | NREventA5 | measId:3;ServCellPCI:703;Se... |
| 2024-09-20 22:21:35.432 | NRHandoverAttempt | SourcePCI:703;SourceNR-ARFC... |
| 2024-09-20 22:21:35.458 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.470 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.603 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.603 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222646 | 1 | 10.4120 | 7.0834 | -114.7625 | 15.6220 | 140.8778 | 0.0004 | 0.0048 |
| 2024_09_20 22:00 | 3220002 | 2 | 15.4443 | 17.8809 | -117.4392 | 9.9529 | 85.6719 | 0.0048 | 0.0074 |
| 2024_09_20 22:00 | 3277969 | 3 | 15.7574 | 11.3908 | -117.6781 | 9.2514 | 89.9884 | 0.0060 | 0.0034 |
| 2024_09_20 22:00 | 3264810 | 4 | 14.4029 | 17.6569 | -116.1592 | 12.5187 | 110.6688 | 0.0020 | 0.0130 |
| 2024_09_20 22:00 | 3258910 | 5 | 18.8137 | 17.3827 | -114.4424 | 14.8780 | 161.4366 | 0.0124 | 0.0020 |
| 2024_09_20 22:00 | 3244987 | 6 | 15.8478 | 18.1412 | -115.7135 | 17.1567 | 113.4287 | 0.0198 | 0.0003 |
| 2024_09_20 22:00 | 3233007 | 7 | 11.5620 | 17.7149 | -117.4013 | 3.1059 | 50.1763 | 0.0199 | 0.0078 |
| 2024_09_20 22:00 | 3258496 | 8 | 13.0227 | 8.9089 | -117.7653 | 4.1010 | 42.2161 | 0.0053 | 0.0128 |
| 2024_09_20 22:00 | 3269545 | 9 | 16.8849 | 14.3531 | -114.1358 | 4.6453 | 49.3814 | 0.0024 | 0.0039 |
| 2024_09_20 22:00 | 3212066 | 10 | 9.3440 | 17.0600 | -117.2446 | 4.5109 | 31.8528 | 0.0009 | 0.0066 |
| 2024_09_20 22:00 | 3270722 | 11 | 8.2675 | 11.3151 | -116.9141 | 3.0114 | 40.4700 | 0.0185 | 0.0166 |
| 2024_09_20 22:00 | 3210617 | 12 | 19.7855 | 7.2555 | -117.7541 | 3.7825 | 32.7265 | 0.0168 | 0.0078 |
| 2024_09_20 22:00 | 3222453 | 13 | 6.9728 | 16.8469 | -114.9908 | 3.0730 | 49.9309 | 0.0182 | 0.0020 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412921_4AAA4813 | 152650 | 901 | -86.2 | 152650 | 990 | -92.9 | 152650 | 554 | -96.3 | 152650 | 201 |
| MR_1774412921_FF154060 | 152650 | 901 | -89.2 | 152650 | 990 | -93.3 | 152650 | 554 | -96.5 | 152650 | 201 |
| MR_1774412921_204AE5C2 | 152650 | 901 | -86.8 | 152650 | 990 | -95.2 | 152650 | 554 | -95.8 | 152650 | 201 |
| MR_1774412921_ACD2D161 | 152650 | 901 | -86.1 | 152650 | 990 | -92.1 | 152650 | 554 | -95.9 | 152650 | 201 |
| MR_1774412921_BEA9825A | 152650 | 901 | -88.2 | 152650 | 990 | -95.2 | 152650 | 554 | -96.0 | 152650 | 201 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 19: `c0d6fcb9-3c9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c0d6fcb9-3c93-45ad-9a1b-98cce32086d0` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[19] topology](images/test_0019.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3269406_3
- `C2`: Add neighbor relationship between 3269406_3 and 3233506_1
- `C3`: Adjust the azimuth of 3269406_3 by 41 degrees
- `C4`: Press down the tilt angle of 3269406_3 by 4 degrees
- `C5`: Increase transmission power for 3269406_3
- `C6`: Decrease A3 Offset threshold for 3269406_3
- `C7`: Lift the tilt angle  of 3233506_1 by 6 degrees
- `C8`: Increase A3 Offset threshold for 3269406_3
- `C9`: Add neighbor relationship between 3244401_4 and 3233506_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269406_3
- `C11`: Lift the tilt angle of 3269406_3 by 4 degrees
- `C12`: Decrease transmission power for 3233506_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269406_3
- `C14`: Increase transmission power for 3233506_1
- `C15`: Check test server and transmission issues
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233506_1
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Press down the tilt angle  of 3233506_1 by 6 degrees
- `C19`: Increase A3 Offset threshold for 3233506_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233506_1
- `C21`: Decrease A3 Offset threshold for 3233506_1
- `C22`: Adjust the azimuth of 3233506_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.871 | MS1 | 121.4656684347 | 31.1446209735 | 691 | 504990 | -91.38 | 16.35 | 572.07 | 0.15 | 2.78 | 1592 |
| 2024-09-20 22:21:32.152 | MS1 | 121.4656717245 | 31.1446211221 | 691 | 504990 | -90.48 | 13.27 | 370.35 | 0.19 | 2.95 | 1565 |
| 2024-09-20 22:21:33.167 | MS1 | 121.4656693468 | 31.1446243490 | 691 | 504990 | -89.41 | 16.64 | 464.59 | 0.05 | 2.51 | 1583 |
| 2024-09-20 22:21:34.211 | MS1 | 121.4656600886 | 31.1446300285 | 691 | 504990 | -90.40 | 16.75 | 55.41 | 0.67 | 2.64 | 661 |
| 2024-09-20 22:21:35.952 | MS1 | 121.4656733250 | 31.1446376251 | 691 | 504990 | -91.55 | 14.31 | 99.65 | 0.53 | 2.16 | 583 |
| 2024-09-20 22:21:36.575 | MS1 | 121.4656637009 | 31.1446203557 | 691 | 504990 | -88.85 | 15.57 | 80.95 | 0.60 | 2.03 | 672 |
| 2024-09-20 22:21:37.116 | MS1 | 121.4656681420 | 31.1446312715 | 691 | 504990 | -91.48 | 10.55 | 57.22 | 0.68 | 2.12 | 588 |
| 2024-09-20 22:21:38.923 | MS1 | 121.4656777410 | 31.1446189943 | 691 | 504990 | -90.82 | 7.31 | 96.64 | 0.68 | 2.21 | 504 |
| 2024-09-20 22:21:39.665 | MS1 | 121.4656586104 | 31.1446226257 | 691 | 504990 | -89.96 | 9.41 | 54.66 | 0.60 | 2.13 | 696 |
| 2024-09-20 22:21:40.844 | MS1 | 121.4656763641 | 31.1446221301 | 691 | 504990 | -93.46 | 12.52 | 304.97 | 0.08 | 2.89 | 1590 |
| 2024-09-20 22:21:41.362 | MS1 | 121.4656692423 | 31.1446281331 | 691 | 504990 | -91.31 | 9.72 | 502.66 | 0.11 | 2.98 | 1591 |
| 2024-09-20 22:21:42.374 | MS1 | 121.4656658261 | 31.1446254031 | 691 | 504990 | -89.58 | 10.09 | 517.15 | 0.20 | 2.03 | 1583 |

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
| 3216184 | 2 | 121.4705055249 | 31.1545485314 | 296 | 3 | 2 | 33.4 | TDD | 778 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3233506 | 1 | 121.4692131894 | 31.1479484846 | 303 | 1 | 0 | 44.0 | TDD | 897 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3244401 | 4 | 121.4691695585 | 31.1502492474 | 138 | 11 | 3 | 28.7 | TDD | 582 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3269406 | 3 | 121.4651979405 | 31.1556529345 | 219 | 3 | 11 | 26.2 | TDD | 691 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.134 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.158 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.280 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.280 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.004 | NREventA3 | measId:2;ServCellPCI:660;Se... |
| 2024-09-20 22:21:38.244 | NRHandoverAttempt | SourcePCI:660;SourceNR-ARFC... |
| 2024-09-20 22:21:38.283 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.295 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.418 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.418 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233506 | 1 | 7.3383 | 10.5626 | -114.1264 | 11.9505 | 83.3143 | 0.0058 | 0.0154 |
| 2024_09_20 22:00 | 3216184 | 2 | 15.1622 | 17.0398 | -116.7962 | 10.0634 | 170.3374 | 0.0085 | 0.0077 |
| 2024_09_20 22:00 | 3269406 | 3 | 13.7295 | 15.6648 | -116.8358 | 10.2481 | 191.1321 | 0.0049 | 0.0108 |
| 2024_09_20 22:00 | 3244401 | 4 | 14.2194 | 7.6178 | -116.7779 | 19.1740 | 139.1021 | 0.0039 | 0.0172 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414049_F417EF2B | 504990 | 691 | -88.9 | 504990 | 897 | -91.2 | 504990 | 582 | -103.4 | 504990 | 778 |
| MR_1774414049_DACF9EB9 | 504990 | 691 | -90.9 | 504990 | 897 | -92.3 | 504990 | 582 | -103.2 | 504990 | 778 |
| MR_1774414049_AD159DF0 | 504990 | 691 | -89.9 | 504990 | 897 | -92.1 | 504990 | 582 | -104.8 | 504990 | 778 |
| MR_1774414049_82AAC4E8 | 504990 | 691 | -88.4 | 504990 | 897 | -92.5 | 504990 | 582 | -102.6 | 504990 | 778 |
| MR_1774414049_8844F69C | 504990 | 691 | -91.8 | 504990 | 897 | -90.5 | 504990 | 582 | -106.2 | 504990 | 778 |
| MR_1774414049_00652937 | 504990 | 691 | -91.3 | 504990 | 897 | -92.4 | 504990 | 582 | -104.1 | 504990 | 778 |
| MR_1774414049_9C244FAD | 504990 | 691 | -89.6 | 504990 | 897 | -93.0 | 504990 | 582 | -105.5 | 504990 | 778 |

> *... 2개 열 생략 (전체 14열)*

---
