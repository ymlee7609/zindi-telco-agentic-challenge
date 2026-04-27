# Track A 문제 분석 — train[1160]~train[1169]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1160] ~ train[1169] (10개)

## 목차

1. [문제 1160: `6346519a-636...`](#1160) — multiple-answer, 정답: C8|C16|C17|C22
2. [문제 1161: `86b4a0a1-c24...`](#1161) — multiple-answer, 정답: C6|C13
3. [문제 1162: `2a250d4b-956...`](#1162) — single-answer, 정답: C7
4. [문제 1163: `e015a67c-204...`](#1163) — single-answer, 정답: C18
5. [문제 1164: `24617268-8b6...`](#1164) — single-answer, 정답: C8
6. [문제 1165: `a7a8d981-2a4...`](#1165) — multiple-answer, 정답: C15|C17
7. [문제 1166: `80e38bc8-34a...`](#1166) — single-answer, 정답: C14
8. [문제 1167: `87d91957-e44...`](#1167) — single-answer, 정답: C11
9. [문제 1168: `b33d7bf2-81c...`](#1168) — single-answer, 정답: C10
10. [문제 1169: `6d1837d8-c6d...`](#1169) — single-answer, 정답: C4

---

### 문제 1160: `6346519a-636...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6346519a-6369-4c75-9d61-48988489afdd` |
| Tag | **multiple-answer** |
| 정답 | **C8|C16|C17|C22** |
| C8 의미 | Increase A3 Offset threshold for 3217429_1 |
| C16 의미 | Decrease transmission power for 3217429_1 |
| C17 의미 | Press down the tilt angle  of 3217429_1 by 3 degrees |
| C22 의미 | Increase A3 Offset threshold for 3225786_3 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1160] topology](images/train_1160.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3225786_3 by 2 degrees
- `C2`: Check test server and transmission issues
- `C3`: Add neighbor relationship between 3265741_4 and 3217429_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225786_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225786_3
- `C6`: Lift the tilt angle  of 3217429_1 by 3 degrees
- `C7`: Decrease A3 Offset threshold for 3217429_1
- `C8`: Increase A3 Offset threshold for 3217429_1 **← 정답**
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217429_1
- `C10`: Decrease A3 Offset threshold for 3225786_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217429_1
- `C12`: Adjust the azimuth of 3217429_1 by 30 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Increase transmission power for 3217429_1
- `C15`: Decrease transmission power for 3225786_3
- `C16`: Decrease transmission power for 3217429_1 **← 정답**
- `C17`: Press down the tilt angle  of 3217429_1 by 3 degrees **← 정답**
- `C18`: Add neighbor relationship between 3225786_3 and 3217429_1
- `C19`: Adjust the azimuth of 3225786_3 by 18 degrees
- `C20`: Press down the tilt angle of 3225786_3 by 2 degrees
- `C21`: Increase transmission power for 3225786_3
- `C22`: Increase A3 Offset threshold for 3225786_3 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.678 | MS1 | 121.4656689584 | 31.1446306090 | 537 | 504990 | -83.17 | 13.89 | 329.33 | 0.20 | 2.41 | 1571 |
| 2024-09-20 22:21:32.380 | MS1 | 121.4656582700 | 31.1446273861 | 537 | 504990 | -79.53 | 15.28 | 345.47 | 0.09 | 2.04 | 1562 |
| 2024-09-20 22:21:33.743 | MS1 | 121.4656747452 | 31.1446294372 | 537 | 504990 | -77.13 | 15.62 | 423.46 | 0.00 | 2.61 | 1574 |
| 2024-09-20 22:21:34.718 | MS1 | 121.4656608271 | 31.1446364452 | 735 | 504990 | -87.96 | 3.36 | 87.48 | 0.15 | 1.43 | 1586 |
| 2024-09-20 22:21:35.377 | MS1 | 121.4656609248 | 31.1446372648 | 735 | 504990 | -81.92 | 4.49 | 55.09 | 0.07 | 1.43 | 1574 |
| 2024-09-20 22:21:36.542 | MS1 | 121.4656702401 | 31.1446363703 | 537 | 504990 | -82.71 | 3.84 | 34.99 | 0.11 | 1.40 | 1575 |
| 2024-09-20 22:21:37.887 | MS1 | 121.4656621428 | 31.1446295053 | 537 | 504990 | -89.89 | 3.76 | 63.42 | 0.01 | 1.39 | 1594 |
| 2024-09-20 22:21:38.749 | MS1 | 121.4656678006 | 31.1446296376 | 735 | 504990 | -88.13 | 1.99 | 38.01 | 0.11 | 1.41 | 1598 |
| 2024-09-20 22:21:39.925 | MS1 | 121.4656616094 | 31.1446291294 | 735 | 504990 | -85.28 | 3.67 | 49.45 | 0.07 | 1.05 | 1586 |
| 2024-09-20 22:21:40.106 | MS1 | 121.4656695968 | 31.1446287226 | 735 | 504990 | -78.02 | 15.75 | 516.53 | 0.15 | 2.44 | 1561 |
| 2024-09-20 22:21:41.185 | MS1 | 121.4656652558 | 31.1446232701 | 735 | 504990 | -82.16 | 13.59 | 376.03 | 0.12 | 2.94 | 1575 |
| 2024-09-20 22:21:42.351 | MS1 | 121.4656765374 | 31.1446265648 | 735 | 504990 | -83.73 | 17.09 | 498.39 | 0.07 | 2.21 | 1598 |

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
| 3213664 | 2 | 121.4747213471 | 31.1446958476 | 325 | 15 | 12 | 41.0 | TDD | 470 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3217429 | 1 | 121.4655976609 | 31.1522452109 | 150 | 1 | 10 | 23.8 | TDD | 878 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3225786 | 3 | 121.4646608654 | 31.1506484482 | 154 | 0 | 7 | 29.2 | TDD | 537 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3265741 | 4 | 121.4735235621 | 31.1558930342 | 288 | 13 | 12 | 41.1 | TDD | 411 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3274268 | 5 | 121.4685215300 | 31.1470575521 | 114 | 15 | 8 | 46.7 | TDD | 735 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.217 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.238 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.373 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.373 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.110 | NREventA3 | measId:2;ServCellPCI:831;Se... |
| 2024-09-20 22:21:34.350 | NRHandoverAttempt | SourcePCI:831;SourceNR-ARFC... |
| 2024-09-20 22:21:34.391 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.403 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:34.551 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.551 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.110 | NREventA3 | measId:2;ServCellPCI:374;Se... |
| 2024-09-20 22:21:36.350 | NRHandoverAttempt | SourcePCI:374;SourceNR-ARFC... |
| 2024-09-20 22:21:36.395 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.408 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.545 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.545 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.110 | NREventA3 | measId:2;ServCellPCI:831;Se... |
| 2024-09-20 22:21:38.350 | NRHandoverAttempt | SourcePCI:831;SourceNR-ARFC... |
| 2024-09-20 22:21:38.395 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.407 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.549 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.549 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217429 | 1 | 10.8400 | 19.1530 | -116.5009 | 8.4325 | 186.1855 | 0.0158 | 0.0029 |
| 2024_09_20 22:00 | 3213664 | 2 | 18.4223 | 17.4029 | -115.3266 | 7.3905 | 195.6921 | 0.0141 | 0.0071 |
| 2024_09_20 22:00 | 3225786 | 3 | 18.6657 | 5.8916 | -115.1393 | 12.0714 | 199.2975 | 0.0109 | 0.0057 |
| 2024_09_20 22:00 | 3265741 | 4 | 17.7620 | 6.3271 | -115.1440 | 10.8788 | 99.2559 | 0.0148 | 0.0159 |
| 2024_09_20 22:00 | 3274268 | 5 | 8.0396 | 15.8310 | -117.9558 | 17.4485 | 185.0807 | 0.0123 | 0.0105 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413493_D1880B56 | 504990 | 735 | -89.9 | 504990 | 537 | -88.3 | 504990 | 878 | -93.4 | 504990 | 411 |
| MR_1774413493_E72D10C4 | 504990 | 735 | -89.9 | 504990 | 537 | -90.7 | 504990 | 878 | -93.3 | 504990 | 411 |
| MR_1774413493_395C3A67 | 504990 | 735 | -86.6 | 504990 | 537 | -87.9 | 504990 | 878 | -92.0 | 504990 | 411 |
| MR_1774413493_EC9DDD2A | 504990 | 537 | -87.9 | 504990 | 735 | -88.2 | 504990 | 878 | -92.5 | 504990 | 411 |
| MR_1774413493_6E186D49 | 504990 | 735 | -89.5 | 504990 | 537 | -90.0 | 504990 | 878 | -92.8 | 504990 | 411 |
| MR_1774413493_6EE43559 | 504990 | 537 | -87.4 | 504990 | 735 | -91.2 | 504990 | 878 | -92.9 | 504990 | 411 |
| MR_1774413493_040D74C3 | 504990 | 537 | -88.4 | 504990 | 735 | -89.4 | 504990 | 878 | -94.6 | 504990 | 411 |
| MR_1774413493_2451FCC3 | 504990 | 735 | -87.5 | 504990 | 537 | -91.0 | 504990 | 878 | -92.3 | 504990 | 411 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1161: `86b4a0a1-c24...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `86b4a0a1-c241-4ebc-b6ac-ab1d20fff793` |
| Tag | **multiple-answer** |
| 정답 | **C6|C13** |
| C6 의미 | Adjust the azimuth of 3275150_4 by 47 degrees |
| C13 의미 | Increase transmission power for 3275150_4 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1161] topology](images/train_1161.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251810_2
- `C3`: Lift the tilt angle  of 3251810_2 by 6 degrees
- `C4`: Decrease A3 Offset threshold for 3275150_4
- `C5`: Press down the tilt angle of 3275150_4 by 10 degrees
- `C6`: Adjust the azimuth of 3275150_4 by 47 degrees **← 정답**
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275150_4
- `C8`: Increase A3 Offset threshold for 3275150_4
- `C9`: Increase A3 Offset threshold for 3251810_2
- `C10`: Decrease A3 Offset threshold for 3251810_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275150_4
- `C12`: Press down the tilt angle  of 3251810_2 by 6 degrees
- `C13`: Increase transmission power for 3275150_4 **← 정답**
- `C14`: Increase transmission power for 3251810_2
- `C15`: Decrease transmission power for 3275150_4
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Add neighbor relationship between 3275150_4 and 3251810_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251810_2
- `C19`: Lift the tilt angle of 3275150_4 by 10 degrees
- `C20`: Decrease transmission power for 3251810_2
- `C21`: Add neighbor relationship between 3222760_1 and 3251810_2
- `C22`: Adjust the azimuth of 3251810_2 by 35 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.992 | MS1 | 121.4656585377 | 31.1446224793 | 159 | 504990 | -90.97 | 17.83 | 437.83 | 0.04 | 2.08 | 1593 |
| 2024-09-20 22:21:32.692 | MS1 | 121.4656672497 | 31.1446268108 | 159 | 504990 | -88.47 | 17.01 | 534.77 | 0.12 | 2.18 | 1577 |
| 2024-09-20 22:21:33.754 | MS1 | 121.4656628123 | 31.1446240856 | 159 | 504990 | -87.55 | 17.61 | 336.38 | 0.00 | 2.77 | 1580 |
| 2024-09-20 22:21:34.660 | MS1 | 121.4656701173 | 31.1446222369 | 159 | 504990 | -102.91 | 0.70 | 64.27 | 0.06 | 1.29 | 1591 |
| 2024-09-20 22:21:35.270 | MS1 | 121.4656594381 | 31.1446222773 | 159 | 504990 | -102.29 | 0.06 | 87.02 | 0.03 | 1.10 | 1578 |
| 2024-09-20 22:21:36.746 | MS1 | 121.4656581393 | 31.1446214222 | 159 | 504990 | -102.84 | -0.52 | 76.90 | 0.17 | 1.33 | 1595 |
| 2024-09-20 22:21:37.379 | MS1 | 121.4656704156 | 31.1446194858 | 159 | 504990 | -104.93 | 0.50 | 72.57 | 0.06 | 1.14 | 1560 |
| 2024-09-20 22:21:38.210 | MS1 | 121.4656683311 | 31.1446334093 | 159 | 504990 | -105.73 | 1.48 | 23.37 | 0.06 | 1.40 | 1579 |
| 2024-09-20 22:21:39.517 | MS1 | 121.4656751821 | 31.1446352802 | 159 | 504990 | -105.31 | -1.33 | 60.40 | 0.14 | 1.31 | 1581 |
| 2024-09-20 22:21:40.702 | MS1 | 121.4656642570 | 31.1446237576 | 159 | 504990 | -87.88 | 13.42 | 480.61 | 0.06 | 2.19 | 1580 |
| 2024-09-20 22:21:41.344 | MS1 | 121.4656632631 | 31.1446364275 | 159 | 504990 | -88.86 | 14.76 | 497.08 | 0.17 | 2.72 | 1577 |
| 2024-09-20 22:21:42.399 | MS1 | 121.4656704267 | 31.1446347936 | 159 | 504990 | -90.59 | 12.02 | 422.81 | 0.08 | 2.25 | 1567 |

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
| 3222760 | 1 | 121.4672352457 | 31.1474097547 | 212 | 13 | 3 | 26.6 | TDD | 560 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3229306 | 3 | 121.4658568343 | 31.1503905550 | 164 | 7 | 9 | 36.2 | TDD | 368 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3251810 | 2 | 121.4728859645 | 31.1552152766 | 175 | 4 | 10 | 41.1 | TDD | 34 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3275150 | 4 | 121.4718678810 | 31.1472000168 | 291 | 15 | 6 | 20.5 | TDD | 159 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.749 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.773 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.902 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.902 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.145 | NREventA2 | measId:1;ServCellPCI:185;Se... |
| 2024-09-20 22:21:34.257 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222760 | 1 | 12.2063 | 10.8812 | -117.7124 | 12.9591 | 171.1877 | 0.0114 | 0.0187 |
| 2024_09_20 22:00 | 3251810 | 2 | 16.5011 | 8.3889 | -114.6813 | 11.4259 | 136.2898 | 0.0069 | 0.0075 |
| 2024_09_20 22:00 | 3229306 | 3 | 6.0247 | 19.7183 | -114.8673 | 7.1246 | 169.8191 | 0.0049 | 0.0158 |
| 2024_09_20 22:00 | 3275150 | 4 | 10.7554 | 19.1629 | -116.6607 | 11.7009 | 148.6915 | 0.1635 | 0.0081 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414801_18D975BA | 504990 | 159 | -102.2 | 504990 | 34 | -111.2 | 504990 | 560 | -115.9 | 504990 | 368 |
| MR_1774414801_7F4A870A | 504990 | 159 | -104.5 | 504990 | 34 | -108.1 | 504990 | 560 | -118.4 | 504990 | 368 |
| MR_1774414801_0E25C9A4 | 504990 | 159 | -102.5 | 504990 | 34 | -109.8 | 504990 | 560 | -118.9 | 504990 | 368 |
| MR_1774414801_621EA036 | 504990 | 159 | -104.1 | 504990 | 34 | -110.9 | 504990 | 560 | -118.9 | 504990 | 368 |
| MR_1774414801_A5E530A4 | 504990 | 159 | -101.3 | 504990 | 34 | -111.3 | 504990 | 560 | -118.2 | 504990 | 368 |
| MR_1774414801_FCAD7E3A | 504990 | 159 | -102.4 | 504990 | 34 | -108.7 | 504990 | 560 | -118.5 | 504990 | 368 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1162: `2a250d4b-956...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2a250d4b-956c-4f3e-b4b8-8afe33804936` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232143_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1162] topology](images/train_1162.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3232143_2
- `C2`: Check test server and transmission issues
- `C3`: Increase A3 Offset threshold for 3232143_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245285_6
- `C5`: Decrease transmission power for 3232143_2
- `C6`: Lift the tilt angle  of 3245285_6 by 4 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232143_2 **← 정답**
- `C8`: Adjust the azimuth of 3232143_2 by 33 degrees
- `C9`: Add neighbor relationship between 3232143_2 and 3245285_6
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase A3 Offset threshold for 3245285_6
- `C12`: Press down the tilt angle  of 3245285_6 by 4 degrees
- `C13`: Adjust the azimuth of 3245285_6 by 35 degrees
- `C14`: Decrease transmission power for 3245285_6
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245285_6
- `C16`: Add neighbor relationship between 3222764_10 and 3245285_6
- `C17`: Press down the tilt angle of 3232143_2 by 1 degrees
- `C18`: Decrease A3 Offset threshold for 3245285_6
- `C19`: Lift the tilt angle of 3232143_2 by 1 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232143_2
- `C21`: Increase transmission power for 3245285_6
- `C22`: Decrease A3 Offset threshold for 3232143_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.304 | MS1 | 121.4656766878 | 31.1446280498 | 199 | 504990 | -93.41 | 12.67 | 392.85 | 0.07 | 2.89 | 1600 |
| 2024-09-20 22:21:32.929 | MS1 | 121.4656719086 | 31.1446365384 | 873 | 504990 | -93.03 | 11.34 | 312.28 | 0.05 | 2.01 | 1593 |
| 2024-09-20 22:21:33.703 | MS1 | 121.4656657096 | 31.1446348073 | 992 | 504990 | -94.24 | 12.72 | 529.79 | 0.13 | 2.54 | 1591 |
| 2024-09-20 22:21:34.582 | MS1 | 121.4656713394 | 31.1446200561 | 603 | 152650 | -94.55 | 2.36 | 66.36 | 0.16 | 1.70 | 928 |
| 2024-09-20 22:21:35.151 | MS1 | 121.4656616566 | 31.1446356417 | 683 | 152650 | -88.06 | 3.70 | 93.82 | 0.03 | 1.66 | 911 |
| 2024-09-20 22:21:36.195 | MS1 | 121.4656623513 | 31.1446270318 | 421 | 152650 | -96.31 | 6.74 | 87.86 | 0.19 | 1.54 | 937 |
| 2024-09-20 22:21:37.268 | MS1 | 121.4656769452 | 31.1446217598 | 640 | 152650 | -93.25 | 2.29 | 81.45 | 0.12 | 1.51 | 904 |
| 2024-09-20 22:21:38.924 | MS1 | 121.4656715258 | 31.1446264851 | 603 | 152650 | -95.02 | 5.53 | 65.37 | 0.07 | 1.51 | 994 |
| 2024-09-20 22:21:39.891 | MS1 | 121.4656677594 | 31.1446364792 | 683 | 152650 | -96.79 | 4.23 | 92.57 | 0.03 | 1.54 | 970 |
| 2024-09-20 22:21:40.905 | MS1 | 121.4656601027 | 31.1446188861 | 421 | 152650 | -96.41 | 7.04 | 59.21 | 0.16 | 2.63 | 1562 |
| 2024-09-20 22:21:41.512 | MS1 | 121.4656686904 | 31.1446196405 | 640 | 152650 | -95.75 | 2.98 | 89.16 | 0.18 | 2.47 | 1579 |
| 2024-09-20 22:21:42.641 | MS1 | 121.4656657270 | 31.1446274491 | 603 | 152650 | -89.50 | 3.71 | 92.25 | 0.03 | 2.19 | 1571 |

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
| 3222764 | 10 | 121.4733807376 | 31.1516917140 | 150 | 0 | 0 | 20.6 | FDD | 421 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3227014 | 5 | 121.4721639421 | 31.1469304261 | 153 | 14 | 10 | 4.2 | TDD | 829 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3232143 | 2 | 121.4721535835 | 31.1505170775 | 190 | 0 | 8 | 15.3 | TDD | 199 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3233981 | 8 | 121.4649336781 | 31.1526188308 | 65 | 7 | 12 | 10.2 | FDD | 897 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3244142 | 4 | 121.4752742036 | 31.1511926500 | 195 | 5 | 8 | 14.4 | TDD | 777 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3245285 | 6 | 121.4749592905 | 31.1465677259 | 291 | 3 | 9 | 17.0 | TDD | 62 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3249512 | 1 | 121.4690080585 | 31.1462451322 | 247 | 9 | 7 | 11.6 | TDD | 992 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3255037 | 12 | 121.4717326742 | 31.1447145424 | 268 | 2 | 5 | 6.1 | FDD | 945 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3257082 | 3 | 121.4720458496 | 31.1535843837 | 284 | 8 | 9 | 26.7 | TDD | 873 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3258626 | 9 | 121.4735668638 | 31.1498460871 | 66 | 10 | 12 | 24.0 | FDD | 768 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3259935 | 7 | 121.4759206837 | 31.1518870201 | 119 | 4 | 3 | 21.1 | FDD | 640 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3270991 | 13 | 121.4737741053 | 31.1485851055 | 10 | 8 | 3 | 14.2 | FDD | 603 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3271051 | 11 | 121.4740663460 | 31.1522850312 | 267 | 2 | 10 | 25.1 | FDD | 683 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |

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
| 2024-09-20 22:21:31.307 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.330 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.431 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.431 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.156 | NREventA2 | measId:1;ServCellPCI:853;Se... |
| 2024-09-20 22:21:35.296 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.530 | NREventA5 | measId:3;ServCellPCI:853;Se... |
| 2024-09-20 22:21:35.591 | NRHandoverAttempt | SourcePCI:853;SourceNR-ARFC... |
| 2024-09-20 22:21:35.641 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.651 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.796 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.796 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249512 | 1 | 7.8313 | 10.1546 | -116.8132 | 8.8340 | 80.2399 | 0.0111 | 0.0067 |
| 2024_09_20 22:00 | 3232143 | 2 | 5.2051 | 19.3570 | -116.4601 | 15.3598 | 84.4964 | 0.0073 | 0.0171 |
| 2024_09_20 22:00 | 3257082 | 3 | 12.7492 | 18.0412 | -116.7320 | 6.7533 | 176.2776 | 0.0059 | 0.0150 |
| 2024_09_20 22:00 | 3244142 | 4 | 12.5640 | 19.0853 | -115.4577 | 7.3503 | 88.4444 | 0.0145 | 0.0111 |
| 2024_09_20 22:00 | 3227014 | 5 | 15.2508 | 10.4011 | -117.3278 | 13.6541 | 106.3541 | 0.0185 | 0.0059 |
| 2024_09_20 22:00 | 3245285 | 6 | 14.7182 | 8.7975 | -116.6180 | 19.8412 | 158.7501 | 0.0137 | 0.0179 |
| 2024_09_20 22:00 | 3259935 | 7 | 8.6754 | 6.6286 | -114.5322 | 4.6379 | 51.9119 | 0.0125 | 0.0105 |
| 2024_09_20 22:00 | 3233981 | 8 | 11.3831 | 9.3576 | -114.2322 | 3.9383 | 57.4937 | 0.0168 | 0.0113 |
| 2024_09_20 22:00 | 3258626 | 9 | 14.0441 | 16.6129 | -114.5756 | 3.0763 | 24.5751 | 0.0041 | 0.0161 |
| 2024_09_20 22:00 | 3222764 | 10 | 15.3689 | 15.0603 | -116.9141 | 4.4256 | 31.2807 | 0.0080 | 0.0096 |
| 2024_09_20 22:00 | 3271051 | 11 | 5.4067 | 14.4271 | -114.1499 | 3.4265 | 55.8659 | 0.0179 | 0.0120 |
| 2024_09_20 22:00 | 3255037 | 12 | 10.6710 | 18.9947 | -116.9125 | 3.3801 | 56.6249 | 0.0061 | 0.0037 |
| 2024_09_20 22:00 | 3270991 | 13 | 13.5947 | 9.2482 | -115.7640 | 3.8442 | 47.3349 | 0.0066 | 0.0034 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412650_FE9CBAA8 | 152650 | 603 | -92.6 | 152650 | 897 | -98.9 | 152650 | 768 | -105.5 | 152650 | 945 |
| MR_1774412650_16BA0932 | 504990 | 992 | -96.0 | 504990 | 62 | -93.5 | 504990 | 829 | -97.3 | 504990 | 777 |
| MR_1774412650_B94CAA84 | 152650 | 603 | -94.9 | 152650 | 897 | -99.8 | 152650 | 768 | -104.6 | 152650 | 945 |
| MR_1774412650_6058BA7A | 152650 | 603 | -95.1 | 152650 | 897 | -98.8 | 152650 | 768 | -105.8 | 152650 | 945 |
| MR_1774412650_A1904466 | 152650 | 603 | -96.1 | 152650 | 897 | -97.8 | 152650 | 768 | -102.8 | 152650 | 945 |
| MR_1774412650_87F817B0 | 504990 | 992 | -94.0 | 504990 | 62 | -92.1 | 504990 | 829 | -99.6 | 504990 | 777 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1163: `e015a67c-204...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e015a67c-204f-411e-98f5-e7641d0fadf8` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Add neighbor relationship between 3257713_4 and 3243204_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1163] topology](images/train_1163.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257713_4
- `C2`: Lift the tilt angle of 3257713_4 by 5 degrees
- `C3`: Check test server and transmission issues
- `C4`: Increase transmission power for 3243204_3
- `C5`: Increase A3 Offset threshold for 3257713_4
- `C6`: Adjust the azimuth of 3257713_4 by 50 degrees
- `C7`: Add neighbor relationship between 3213021_1 and 3243204_3
- `C8`: Lift the tilt angle  of 3243204_3 by 5 degrees
- `C9`: Decrease transmission power for 3257713_4
- `C10`: Decrease A3 Offset threshold for 3243204_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243204_3
- `C12`: Increase A3 Offset threshold for 3243204_3
- `C13`: Adjust the azimuth of 3243204_3 by 28 degrees
- `C14`: Decrease A3 Offset threshold for 3257713_4
- `C15`: Increase transmission power for 3257713_4
- `C16`: Press down the tilt angle  of 3243204_3 by 5 degrees
- `C17`: Press down the tilt angle of 3257713_4 by 5 degrees
- `C18`: Add neighbor relationship between 3257713_4 and 3243204_3 **← 정답**
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243204_3
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease transmission power for 3243204_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257713_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.802 | MS1 | 121.4656596054 | 31.1446308171 | 182 | 504990 | -83.25 | 17.64 | 358.22 | 0.17 | 2.31 | 1565 |
| 2024-09-20 22:21:32.211 | MS1 | 121.4656623048 | 31.1446190026 | 182 | 504990 | -75.30 | 17.38 | 483.67 | 0.09 | 2.91 | 1566 |
| 2024-09-20 22:21:33.782 | MS1 | 121.4656695813 | 31.1446375944 | 182 | 504990 | -76.43 | 16.70 | 378.27 | 0.14 | 2.29 | 1560 |
| 2024-09-20 22:21:34.931 | MS1 | 121.4656719822 | 31.1446318751 | 182 | 504990 | -89.35 | -3.86 | 32.20 | 0.07 | 1.46 | 1600 |
| 2024-09-20 22:21:35.143 | MS1 | 121.4656689677 | 31.1446270657 | 182 | 504990 | -91.11 | -0.81 | 51.08 | 0.10 | 1.11 | 1592 |
| 2024-09-20 22:21:36.588 | MS1 | 121.4656600366 | 31.1446306380 | 182 | 504990 | -92.18 | -0.26 | 28.48 | 0.04 | 1.13 | 1586 |
| 2024-09-20 22:21:37.507 | MS1 | 121.4656667963 | 31.1446332182 | 182 | 504990 | -90.78 | -0.54 | 56.98 | 0.03 | 1.07 | 1571 |
| 2024-09-20 22:21:38.560 | MS1 | 121.4656678263 | 31.1446350692 | 182 | 504990 | -80.70 | 15.55 | 571.61 | 0.07 | 1.05 | 1560 |
| 2024-09-20 22:21:39.179 | MS1 | 121.4656643817 | 31.1446365922 | 182 | 504990 | -76.77 | 14.19 | 374.82 | 0.00 | 1.24 | 1597 |
| 2024-09-20 22:21:40.862 | MS1 | 121.4656741918 | 31.1446364597 | 182 | 504990 | -83.15 | 15.87 | 489.91 | 0.13 | 2.55 | 1561 |
| 2024-09-20 22:21:41.286 | MS1 | 121.4656740579 | 31.1446297150 | 182 | 504990 | -80.97 | 13.13 | 464.41 | 0.06 | 2.07 | 1568 |
| 2024-09-20 22:21:42.775 | MS1 | 121.4656725625 | 31.1446181207 | 182 | 504990 | -75.94 | 12.07 | 333.13 | 0.04 | 2.32 | 1584 |

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
| 3213021 | 1 | 121.4669277679 | 31.1453544379 | 166 | 4 | 7 | 46.2 | TDD | 624 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3243204 | 3 | 121.4734166608 | 31.1440074104 | 303 | 3 | 3 | 31.4 | TDD | 115 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3257713 | 4 | 121.4724383006 | 31.1504740644 | 297 | 2 | 3 | 40.6 | TDD | 182 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3269209 | 2 | 121.4670344457 | 31.1458090099 | 18 | 0 | 9 | 38.3 | TDD | 570 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.509 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.532 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.644 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.644 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.352 | NREventA3 | measId:2;ServCellPCI:359;Se... |
| 2024-09-20 22:21:36.352 | NREventA3 | measId:2;ServCellPCI:359;Se... |
| 2024-09-20 22:21:37.352 | NREventA3 | measId:2;ServCellPCI:359;Se... |
| 2024-09-20 22:21:39.852 | NRRRCReestablishAttempt | PCI:359 |
| 2024-09-20 22:21:39.862 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.876 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:40.022 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.022 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213021 | 1 | 9.3338 | 10.0950 | -114.7391 | 10.4303 | 109.0391 | 0.0200 | 0.0181 |
| 2024_09_20 22:00 | 3269209 | 2 | 14.6671 | 16.0996 | -114.2219 | 6.5023 | 187.2341 | 0.0190 | 0.0059 |
| 2024_09_20 22:00 | 3243204 | 3 | 15.7492 | 16.7145 | -117.0454 | 6.3538 | 101.7596 | 0.0132 | 0.0174 |
| 2024_09_20 22:00 | 3257713 | 4 | 13.5393 | 9.0354 | -114.9091 | 10.0246 | 118.9438 | 0.0189 | 0.1846 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414859_FA64C460 | 504990 | 115 | -86.1 | 504990 | 182 | -88.4 | 504990 | 624 | -95.5 | 504990 | 570 |
| MR_1774414859_D6E31CBB | 504990 | 182 | -89.6 | 504990 | 115 | -83.1 | 504990 | 624 | -93.0 | 504990 | 570 |
| MR_1774414859_DD8A53C5 | 504990 | 182 | -90.6 | 504990 | 115 | -84.6 | 504990 | 624 | -93.3 | 504990 | 570 |
| MR_1774414859_DDE1BACF | 504990 | 115 | -85.3 | 504990 | 182 | -87.4 | 504990 | 624 | -91.6 | 504990 | 570 |
| MR_1774414859_F8301098 | 504990 | 182 | -89.3 | 504990 | 115 | -85.3 | 504990 | 624 | -95.1 | 504990 | 570 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1164: `24617268-8b6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `24617268-8b6c-40df-b8be-09ab076bb93f` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1164] topology](images/train_1164.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3247720_1
- `C2`: Add neighbor relationship between 3247720_1 and 3240427_2
- `C3`: Add neighbor relationship between 3253694_3 and 3240427_2
- `C4`: Adjust the azimuth of 3247720_1 by 50 degrees
- `C5`: Decrease A3 Offset threshold for 3247720_1
- `C6`: Press down the tilt angle of 3247720_1 by 3 degrees
- `C7`: Adjust the azimuth of 3240427_2 by 50 degrees
- `C8`: Insufficient data; more data is needed for judgment. **← 정답**
- `C9`: Check test server and transmission issues
- `C10`: Decrease A3 Offset threshold for 3240427_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247720_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240427_2
- `C13`: Decrease transmission power for 3247720_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247720_1
- `C15`: Lift the tilt angle of 3247720_1 by 3 degrees
- `C16`: Press down the tilt angle  of 3240427_2 by 10 degrees
- `C17`: Decrease transmission power for 3240427_2
- `C18`: Increase transmission power for 3240427_2
- `C19`: Increase transmission power for 3247720_1
- `C20`: Lift the tilt angle  of 3240427_2 by 10 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240427_2
- `C22`: Increase A3 Offset threshold for 3240427_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.610 | MS1 | 121.4656725478 | 31.1446271868 | 632 | 504990 | -90.92 | 16.88 | 357.98 | 0.20 | 2.82 | 1581 |
| 2024-09-20 22:21:32.662 | MS1 | 121.4656620295 | 31.1446360487 | 632 | 504990 | -88.39 | 13.27 | 435.54 | 0.12 | 2.99 | 1598 |
| 2024-09-20 22:21:33.176 | MS1 | 121.4656609260 | 31.1446231927 | 632 | 504990 | -86.42 | 14.12 | 456.44 | 0.16 | 2.25 | 1599 |
| 2024-09-20 22:21:34.546 | MS1 | 121.4656756730 | 31.1446328878 | 632 | 504990 | -90.91 | 12.39 | 59.82 | 0.11 | 2.58 | 1593 |
| 2024-09-20 22:21:35.272 | MS1 | 121.4656593918 | 31.1446222368 | 632 | 504990 | -88.96 | 16.94 | 89.81 | 0.14 | 2.72 | 1562 |
| 2024-09-20 22:21:36.429 | MS1 | 121.4656654308 | 31.1446332857 | 632 | 504990 | -85.43 | 14.39 | 44.31 | 0.13 | 2.73 | 1571 |
| 2024-09-20 22:21:37.211 | MS1 | 121.4656588217 | 31.1446229798 | 632 | 504990 | -90.12 | 11.76 | 88.92 | 0.10 | 2.79 | 1590 |
| 2024-09-20 22:21:38.656 | MS1 | 121.4656667940 | 31.1446323343 | 632 | 504990 | -91.39 | 12.48 | 63.64 | 0.01 | 2.00 | 1560 |
| 2024-09-20 22:21:39.921 | MS1 | 121.4656617516 | 31.1446250786 | 632 | 504990 | -91.77 | 10.50 | 98.56 | 0.00 | 2.34 | 1560 |
| 2024-09-20 22:21:40.259 | MS1 | 121.4656607447 | 31.1446372070 | 632 | 504990 | -91.68 | 12.10 | 583.35 | 0.18 | 2.53 | 1583 |
| 2024-09-20 22:21:41.179 | MS1 | 121.4656682220 | 31.1446347155 | 632 | 504990 | -89.61 | 10.73 | 594.33 | 0.18 | 2.46 | 1589 |
| 2024-09-20 22:21:42.827 | MS1 | 121.4656639139 | 31.1446276278 | 632 | 504990 | -89.78 | 8.55 | 347.24 | 0.04 | 2.50 | 1597 |

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
| 3210610 | 4 | 121.4677043035 | 31.1546941404 | 87 | 4 | 9 | 23.5 | TDD | 367 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3240427 | 2 | 121.4720919019 | 31.1503495315 | 173 | 8 | 12 | 29.7 | TDD | 41 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3247720 | 1 | 121.4685658378 | 31.1532845797 | 354 | 1 | 3 | 28.9 | TDD | 632 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3253694 | 3 | 121.4743861782 | 31.1505667159 | 156 | 3 | 5 | 32.9 | TDD | 897 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.945 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.969 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.112 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.112 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.756 | NREventA3 | measId:2;ServCellPCI:943;Se... |
| 2024-09-20 22:21:37.996 | NRHandoverAttempt | SourcePCI:943;SourceNR-ARFC... |
| 2024-09-20 22:21:38.037 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.052 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.173 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.173 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3247720 | 1 | 87.3437 | 87.1236 | -114.6657 | 14.4118 | 159.5224 | 0.0163 | 0.0121 |
| 2024_09_19 22:00 | 3240427 | 2 | 88.7413 | 89.5782 | -117.8036 | 17.0385 | 189.3755 | 0.0193 | 0.0188 |
| 2024_09_19 22:00 | 3253694 | 3 | 90.5659 | 76.5431 | -114.4048 | 7.6909 | 81.5912 | 0.0104 | 0.0023 |
| 2024_09_19 22:00 | 3210610 | 4 | 86.7139 | 89.4483 | -114.9414 | 5.9846 | 113.9088 | 0.0177 | 0.0149 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412698_343500DB | 504990 | 632 | -91.6 | 504990 | 41 | -97.2 | 504990 | 897 | -99.5 | 504990 | 367 |
| MR_1774412698_9D4D56C6 | 504990 | 632 | -91.7 | 504990 | 41 | -93.8 | 504990 | 897 | -99.7 | 504990 | 367 |
| MR_1774412698_008C9461 | 504990 | 632 | -91.2 | 504990 | 41 | -96.0 | 504990 | 897 | -99.2 | 504990 | 367 |
| MR_1774412698_986E0607 | 504990 | 632 | -89.7 | 504990 | 41 | -94.2 | 504990 | 897 | -99.6 | 504990 | 367 |
| MR_1774412698_BA6484E3 | 504990 | 632 | -92.2 | 504990 | 41 | -93.6 | 504990 | 897 | -101.3 | 504990 | 367 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1165: `a7a8d981-2a4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a7a8d981-2a47-4a38-b3ca-e7b5910ff819` |
| Tag | **multiple-answer** |
| 정답 | **C15|C17** |
| C15 의미 | Adjust the azimuth of 3277827_2 by 50 degrees |
| C17 의미 | Increase transmission power for 3277827_2 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1165] topology](images/train_1165.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3218123_3 by 34 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277827_2
- `C3`: Decrease transmission power for 3218123_3
- `C4`: Increase transmission power for 3218123_3
- `C5`: Press down the tilt angle of 3277827_2 by 10 degrees
- `C6`: Decrease A3 Offset threshold for 3277827_2
- `C7`: Decrease A3 Offset threshold for 3218123_3
- `C8`: Lift the tilt angle  of 3218123_3 by 6 degrees
- `C9`: Press down the tilt angle  of 3218123_3 by 6 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218123_3
- `C11`: Add neighbor relationship between 3277827_2 and 3218123_3
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease transmission power for 3277827_2
- `C14`: Add neighbor relationship between 3263623_4 and 3218123_3
- `C15`: Adjust the azimuth of 3277827_2 by 50 degrees **← 정답**
- `C16`: Increase A3 Offset threshold for 3218123_3
- `C17`: Increase transmission power for 3277827_2 **← 정답**
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218123_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277827_2
- `C20`: Increase A3 Offset threshold for 3277827_2
- `C21`: Lift the tilt angle of 3277827_2 by 10 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.303 | MS1 | 121.4656592710 | 31.1446226330 | 171 | 504990 | -90.60 | 16.70 | 392.30 | 0.10 | 2.96 | 1598 |
| 2024-09-20 22:21:32.821 | MS1 | 121.4656747875 | 31.1446315608 | 171 | 504990 | -89.88 | 12.26 | 344.66 | 0.04 | 2.57 | 1590 |
| 2024-09-20 22:21:33.885 | MS1 | 121.4656674543 | 31.1446304610 | 171 | 504990 | -86.39 | 12.18 | 477.63 | 0.06 | 2.63 | 1600 |
| 2024-09-20 22:21:34.877 | MS1 | 121.4656732867 | 31.1446234087 | 171 | 504990 | -105.59 | -1.53 | 54.95 | 0.06 | 1.06 | 1571 |
| 2024-09-20 22:21:35.895 | MS1 | 121.4656686913 | 31.1446314692 | 171 | 504990 | -103.46 | 1.02 | 55.35 | 0.15 | 1.14 | 1590 |
| 2024-09-20 22:21:36.802 | MS1 | 121.4656769942 | 31.1446353011 | 171 | 504990 | -104.75 | -0.97 | 63.31 | 0.17 | 1.34 | 1592 |
| 2024-09-20 22:21:37.364 | MS1 | 121.4656710569 | 31.1446341731 | 171 | 504990 | -108.03 | 0.13 | 79.54 | 0.13 | 1.04 | 1600 |
| 2024-09-20 22:21:38.514 | MS1 | 121.4656601893 | 31.1446302110 | 171 | 504990 | -102.83 | -1.50 | 53.37 | 0.08 | 1.49 | 1582 |
| 2024-09-20 22:21:39.536 | MS1 | 121.4656681776 | 31.1446288297 | 171 | 504990 | -104.15 | -1.99 | 54.70 | 0.10 | 1.49 | 1594 |
| 2024-09-20 22:21:40.582 | MS1 | 121.4656743379 | 31.1446369438 | 171 | 504990 | -92.80 | 14.55 | 550.39 | 0.08 | 2.84 | 1600 |
| 2024-09-20 22:21:41.960 | MS1 | 121.4656760025 | 31.1446218258 | 171 | 504990 | -91.16 | 14.52 | 597.66 | 0.19 | 2.43 | 1575 |
| 2024-09-20 22:21:42.374 | MS1 | 121.4656586265 | 31.1446353992 | 171 | 504990 | -87.20 | 16.37 | 470.30 | 0.06 | 3.00 | 1569 |

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
| 3218123 | 3 | 121.4741809068 | 31.1449051596 | 234 | 4 | 10 | 21.8 | TDD | 687 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3218464 | 1 | 121.4659066052 | 31.1456754343 | 297 | 1 | 7 | 31.3 | TDD | 353 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3263623 | 4 | 121.4752992123 | 31.1558608372 | 56 | 4 | 2 | 27.8 | TDD | 499 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3277827 | 2 | 121.4645324795 | 31.1466729883 | 87 | 5 | 12 | 34.4 | TDD | 171 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.971 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.989 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.092 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.092 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.304 | NREventA2 | measId:1;ServCellPCI:957;Se... |
| 2024-09-20 22:21:34.410 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218464 | 1 | 7.2498 | 18.4435 | -117.1192 | 10.0428 | 147.3971 | 0.0006 | 0.0162 |
| 2024_09_20 22:00 | 3277827 | 2 | 16.4490 | 6.0635 | -116.7242 | 19.4084 | 81.2739 | 0.1883 | 0.0129 |
| 2024_09_20 22:00 | 3218123 | 3 | 14.7795 | 19.2749 | -115.2809 | 17.6640 | 169.6295 | 0.0155 | 0.0060 |
| 2024_09_20 22:00 | 3263623 | 4 | 16.3583 | 11.2456 | -117.5024 | 14.4062 | 121.8962 | 0.0001 | 0.0044 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415037_911827A9 | 504990 | 171 | -103.8 | 504990 | 687 | -110.2 | 504990 | 499 | -116.8 | 504990 | 353 |
| MR_1774415037_3DF344DF | 504990 | 171 | -106.4 | 504990 | 687 | -109.7 | 504990 | 499 | -115.0 | 504990 | 353 |
| MR_1774415037_AEBCBA00 | 504990 | 171 | -104.8 | 504990 | 687 | -109.2 | 504990 | 499 | -113.7 | 504990 | 353 |
| MR_1774415037_D7455A08 | 504990 | 171 | -107.0 | 504990 | 687 | -109.0 | 504990 | 499 | -116.5 | 504990 | 353 |
| MR_1774415037_A7CF316B | 504990 | 171 | -106.3 | 504990 | 687 | -108.7 | 504990 | 499 | -113.5 | 504990 | 353 |
| MR_1774415037_D3CB9A68 | 504990 | 171 | -104.1 | 504990 | 687 | -109.1 | 504990 | 499 | -116.0 | 504990 | 353 |
| MR_1774415037_8D848D57 | 504990 | 171 | -107.2 | 504990 | 687 | -110.7 | 504990 | 499 | -116.9 | 504990 | 353 |
| MR_1774415037_174AB588 | 504990 | 171 | -104.2 | 504990 | 687 | -109.8 | 504990 | 499 | -116.9 | 504990 | 353 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1166: `80e38bc8-34a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `80e38bc8-34a6-43b2-8cf8-4f5026c47332` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease A3 Offset threshold for 3251457_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1166] topology](images/train_1166.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3251457_1 by 50 degrees
- `C2`: Lift the tilt angle of 3251457_1 by 2 degrees
- `C3`: Decrease A3 Offset threshold for 3268253_4
- `C4`: Increase transmission power for 3268253_4
- `C5`: Increase transmission power for 3251457_1
- `C6`: Increase A3 Offset threshold for 3251457_1
- `C7`: Decrease transmission power for 3251457_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268253_4
- `C9`: Check test server and transmission issues
- `C10`: Lift the tilt angle  of 3268253_4 by 10 degrees
- `C11`: Increase A3 Offset threshold for 3268253_4
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251457_1
- `C14`: Decrease A3 Offset threshold for 3251457_1 **← 정답**
- `C15`: Adjust the azimuth of 3268253_4 by 17 degrees
- `C16`: Add neighbor relationship between 3266048_2 and 3268253_4
- `C17`: Add neighbor relationship between 3251457_1 and 3268253_4
- `C18`: Press down the tilt angle  of 3268253_4 by 10 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268253_4
- `C20`: Press down the tilt angle of 3251457_1 by 2 degrees
- `C21`: Decrease transmission power for 3268253_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251457_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.804 | MS1 | 121.4656607998 | 31.1446204656 | 968 | 504990 | -82.50 | 17.08 | 449.78 | 0.04 | 2.73 | 1585 |
| 2024-09-20 22:21:32.793 | MS1 | 121.4656730276 | 31.1446259684 | 968 | 504990 | -78.32 | 12.17 | 408.94 | 0.20 | 2.88 | 1599 |
| 2024-09-20 22:21:33.244 | MS1 | 121.4656779874 | 31.1446322810 | 968 | 504990 | -77.25 | 17.29 | 516.49 | 0.03 | 2.22 | 1569 |
| 2024-09-20 22:21:34.239 | MS1 | 121.4656742079 | 31.1446276530 | 968 | 504990 | -92.93 | -2.83 | 60.30 | 0.16 | 1.26 | 1574 |
| 2024-09-20 22:21:35.190 | MS1 | 121.4656759131 | 31.1446318345 | 968 | 504990 | -85.49 | -1.90 | 66.33 | 0.05 | 1.06 | 1574 |
| 2024-09-20 22:21:36.836 | MS1 | 121.4656586010 | 31.1446370665 | 968 | 504990 | -90.90 | -3.86 | 72.63 | 0.05 | 1.18 | 1574 |
| 2024-09-20 22:21:37.452 | MS1 | 121.4656640517 | 31.1446330524 | 968 | 504990 | -86.89 | -2.79 | 50.94 | 0.10 | 1.18 | 1585 |
| 2024-09-20 22:21:38.680 | MS1 | 121.4656702939 | 31.1446261722 | 968 | 504990 | -86.40 | -3.61 | 55.22 | 0.07 | 1.14 | 1563 |
| 2024-09-20 22:21:39.807 | MS1 | 121.4656744736 | 31.1446340083 | 52 | 504990 | -77.09 | 14.16 | 301.86 | 0.05 | 1.29 | 1564 |
| 2024-09-20 22:21:40.128 | MS1 | 121.4656753877 | 31.1446307361 | 52 | 504990 | -76.18 | 13.24 | 379.68 | 0.01 | 2.47 | 1590 |
| 2024-09-20 22:21:41.193 | MS1 | 121.4656689528 | 31.1446293590 | 52 | 504990 | -78.67 | 16.37 | 400.10 | 0.07 | 2.51 | 1591 |
| 2024-09-20 22:21:42.409 | MS1 | 121.4656698430 | 31.1446298181 | 52 | 504990 | -81.27 | 12.29 | 565.34 | 0.18 | 2.23 | 1575 |

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
| 3251457 | 1 | 121.4723122430 | 31.1556198631 | 301 | 0 | 1 | 48.9 | TDD | 968 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3266048 | 2 | 121.4690182389 | 31.1493876547 | 255 | 3 | 1 | 38.2 | TDD | 826 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3268253 | 4 | 121.4703263386 | 31.1507872442 | 230 | 8 | 8 | 36.2 | TDD | 52 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3272556 | 3 | 121.4725851260 | 31.1486976206 | 310 | 2 | 12 | 21.6 | TDD | 498 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.487 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.507 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.649 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.649 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.333 | NREventA3 | measId:2;ServCellPCI:624;Se... |
| 2024-09-20 22:21:38.573 | NRHandoverAttempt | SourcePCI:624;SourceNR-ARFC... |
| 2024-09-20 22:21:38.621 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.633 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.763 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.763 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251457 | 1 | 5.7086 | 11.7563 | -115.0322 | 5.3437 | 161.2147 | 0.0046 | 0.1575 |
| 2024_09_20 22:00 | 3266048 | 2 | 9.3214 | 15.7539 | -117.8740 | 16.0798 | 187.2291 | 0.0166 | 0.0032 |
| 2024_09_20 22:00 | 3272556 | 3 | 10.4268 | 9.8367 | -117.2619 | 11.0325 | 148.5148 | 0.0043 | 0.0142 |
| 2024_09_20 22:00 | 3268253 | 4 | 12.5059 | 13.4304 | -115.0530 | 6.5752 | 195.0916 | 0.0029 | 0.0172 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414087_BBEB9C6E | 504990 | 52 | -88.5 | 504990 | 968 | -93.0 | 504990 | 826 | -94.7 | 504990 | 498 |
| MR_1774414087_8AA59890 | 504990 | 968 | -93.3 | 504990 | 52 | -88.9 | 504990 | 826 | -92.8 | 504990 | 498 |
| MR_1774414087_264EAEB2 | 504990 | 968 | -91.6 | 504990 | 52 | -89.8 | 504990 | 826 | -95.4 | 504990 | 498 |
| MR_1774414087_4E9DC8C8 | 504990 | 968 | -94.6 | 504990 | 52 | -86.4 | 504990 | 826 | -92.3 | 504990 | 498 |
| MR_1774414087_D3C09F7C | 504990 | 52 | -88.6 | 504990 | 968 | -94.9 | 504990 | 826 | -93.8 | 504990 | 498 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1167: `87d91957-e44...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `87d91957-e442-4c87-b96c-a05f5030b199` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1167] topology](images/train_1167.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3275128_1 and 3243337_2
- `C2`: Press down the tilt angle  of 3243337_2 by 10 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243337_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275128_1
- `C5`: Check test server and transmission issues
- `C6`: Increase A3 Offset threshold for 3275128_1
- `C7`: Adjust the azimuth of 3275128_1 by 50 degrees
- `C8`: Adjust the azimuth of 3243337_2 by 50 degrees
- `C9`: Lift the tilt angle  of 3243337_2 by 10 degrees
- `C10`: Increase transmission power for 3243337_2
- `C11`: Insufficient data; more data is needed for judgment. **← 정답**
- `C12`: Decrease A3 Offset threshold for 3275128_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243337_2
- `C14`: Increase transmission power for 3275128_1
- `C15`: Decrease A3 Offset threshold for 3243337_2
- `C16`: Decrease transmission power for 3275128_1
- `C17`: Add neighbor relationship between 3253443_3 and 3243337_2
- `C18`: Increase A3 Offset threshold for 3243337_2
- `C19`: Lift the tilt angle of 3275128_1 by 10 degrees
- `C20`: Press down the tilt angle of 3275128_1 by 10 degrees
- `C21`: Decrease transmission power for 3243337_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275128_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.621 | MS1 | 121.4656688552 | 31.1446290611 | 665 | 504990 | -86.48 | 13.66 | 373.36 | 0.19 | 2.98 | 1600 |
| 2024-09-20 22:21:32.347 | MS1 | 121.4656684682 | 31.1446345241 | 665 | 504990 | -90.17 | 12.23 | 385.55 | 0.07 | 2.17 | 1590 |
| 2024-09-20 22:21:33.493 | MS1 | 121.4656752286 | 31.1446276613 | 665 | 504990 | -86.69 | 12.00 | 590.05 | 0.06 | 2.90 | 1572 |
| 2024-09-20 22:21:34.624 | MS1 | 121.4656649341 | 31.1446221327 | 665 | 504990 | -88.16 | 17.86 | 72.64 | 0.03 | 2.50 | 1586 |
| 2024-09-20 22:21:35.725 | MS1 | 121.4656690290 | 31.1446372919 | 665 | 504990 | -91.91 | 14.31 | 101.98 | 0.20 | 2.72 | 1584 |
| 2024-09-20 22:21:36.811 | MS1 | 121.4656750268 | 31.1446353028 | 665 | 504990 | -85.78 | 15.30 | 73.61 | 0.20 | 2.71 | 1566 |
| 2024-09-20 22:21:37.162 | MS1 | 121.4656707096 | 31.1446218426 | 665 | 504990 | -91.09 | 7.65 | 71.24 | 0.05 | 2.34 | 1579 |
| 2024-09-20 22:21:38.707 | MS1 | 121.4656631954 | 31.1446246100 | 665 | 504990 | -93.17 | 7.08 | 59.67 | 0.06 | 2.98 | 1591 |
| 2024-09-20 22:21:39.193 | MS1 | 121.4656675728 | 31.1446199676 | 665 | 504990 | -89.36 | 7.52 | 76.02 | 0.18 | 2.69 | 1584 |
| 2024-09-20 22:21:40.122 | MS1 | 121.4656746733 | 31.1446377036 | 665 | 504990 | -93.76 | 9.35 | 574.64 | 0.09 | 2.70 | 1564 |
| 2024-09-20 22:21:41.696 | MS1 | 121.4656590529 | 31.1446188608 | 665 | 504990 | -91.13 | 10.18 | 472.56 | 0.09 | 2.27 | 1583 |
| 2024-09-20 22:21:42.736 | MS1 | 121.4656607644 | 31.1446356786 | 665 | 504990 | -92.13 | 12.67 | 431.36 | 0.17 | 2.95 | 1573 |

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
| 3243287 | 4 | 121.4680522435 | 31.1506702434 | 282 | 14 | 11 | 33.6 | TDD | 313 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3243337 | 2 | 121.4648718312 | 31.1516815251 | 42 | 11 | 2 | 38.8 | TDD | 508 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3253443 | 3 | 121.4652301476 | 31.1475774203 | 353 | 12 | 3 | 41.0 | TDD | 863 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3275128 | 1 | 121.4706875031 | 31.1554232589 | 132 | 10 | 2 | 22.7 | TDD | 665 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.790 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.808 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.929 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.929 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.604 | NREventA3 | measId:2;ServCellPCI:461;Se... |
| 2024-09-20 22:21:37.844 | NRHandoverAttempt | SourcePCI:461;SourceNR-ARFC... |
| 2024-09-20 22:21:37.880 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.892 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.027 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.027 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3275128 | 1 | 85.8716 | 81.3465 | -114.1803 | 6.5654 | 146.7762 | 0.0010 | 0.0021 |
| 2024_09_19 22:00 | 3243337 | 2 | 75.6628 | 83.1628 | -115.6926 | 9.3422 | 174.3387 | 0.0065 | 0.0031 |
| 2024_09_19 22:00 | 3253443 | 3 | 75.4078 | 77.0684 | -116.1445 | 8.4146 | 159.4097 | 0.0091 | 0.0195 |
| 2024_09_19 22:00 | 3243287 | 4 | 86.3986 | 86.5024 | -117.2010 | 15.4164 | 138.7458 | 0.0035 | 0.0130 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412245_ECD0A656 | 504990 | 665 | -89.6 | 504990 | 508 | -94.5 | 504990 | 863 | -100.5 | 504990 | 313 |
| MR_1774412245_6A70B7FC | 504990 | 665 | -89.4 | 504990 | 508 | -94.0 | 504990 | 863 | -101.7 | 504990 | 313 |
| MR_1774412245_86D2AA14 | 504990 | 665 | -87.7 | 504990 | 508 | -95.0 | 504990 | 863 | -102.2 | 504990 | 313 |
| MR_1774412245_079DFE48 | 504990 | 665 | -89.3 | 504990 | 508 | -96.9 | 504990 | 863 | -99.9 | 504990 | 313 |
| MR_1774412245_C9F54E8A | 504990 | 665 | -89.7 | 504990 | 508 | -94.3 | 504990 | 863 | -102.1 | 504990 | 313 |
| MR_1774412245_66DCCDF6 | 504990 | 665 | -88.3 | 504990 | 508 | -94.1 | 504990 | 863 | -101.6 | 504990 | 313 |
| MR_1774412245_3CAFE1F4 | 504990 | 665 | -89.0 | 504990 | 508 | -94.7 | 504990 | 863 | -102.5 | 504990 | 313 |
| MR_1774412245_18F9DAFD | 504990 | 665 | -86.6 | 504990 | 508 | -94.8 | 504990 | 863 | -100.7 | 504990 | 313 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1168: `b33d7bf2-81c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b33d7bf2-81c8-48c2-af08-9ca93d616bbb` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Add neighbor relationship between 3214385_1 and 3225335_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1168] topology](images/train_1168.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3217272_4 and 3225335_3
- `C2`: Adjust the azimuth of 3214385_1 by 31 degrees
- `C3`: Increase transmission power for 3214385_1
- `C4`: Decrease A3 Offset threshold for 3214385_1
- `C5`: Increase A3 Offset threshold for 3225335_3
- `C6`: Press down the tilt angle of 3214385_1 by 10 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225335_3
- `C8`: Decrease transmission power for 3214385_1
- `C9`: Lift the tilt angle  of 3225335_3 by 5 degrees
- `C10`: Add neighbor relationship between 3214385_1 and 3225335_3 **← 정답**
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Press down the tilt angle  of 3225335_3 by 5 degrees
- `C13`: Adjust the azimuth of 3225335_3 by 38 degrees
- `C14`: Check test server and transmission issues
- `C15`: Increase transmission power for 3225335_3
- `C16`: Lift the tilt angle of 3214385_1 by 10 degrees
- `C17`: Increase A3 Offset threshold for 3214385_1
- `C18`: Decrease A3 Offset threshold for 3225335_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214385_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214385_1
- `C21`: Decrease transmission power for 3225335_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225335_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.515 | MS1 | 121.4656703677 | 31.1446248650 | 520 | 504990 | -79.62 | 14.48 | 458.62 | 0.07 | 2.81 | 1588 |
| 2024-09-20 22:21:32.893 | MS1 | 121.4656713680 | 31.1446289349 | 520 | 504990 | -80.45 | 15.58 | 452.27 | 0.15 | 2.33 | 1596 |
| 2024-09-20 22:21:33.789 | MS1 | 121.4656767583 | 31.1446329969 | 520 | 504990 | -75.32 | 17.05 | 515.56 | 0.04 | 2.82 | 1595 |
| 2024-09-20 22:21:34.495 | MS1 | 121.4656711413 | 31.1446349625 | 520 | 504990 | -93.73 | -2.14 | 49.55 | 0.13 | 1.08 | 1592 |
| 2024-09-20 22:21:35.628 | MS1 | 121.4656606942 | 31.1446288987 | 520 | 504990 | -85.11 | -1.27 | 53.69 | 0.09 | 1.39 | 1594 |
| 2024-09-20 22:21:36.996 | MS1 | 121.4656665964 | 31.1446246882 | 520 | 504990 | -90.22 | -2.29 | 74.24 | 0.08 | 1.30 | 1592 |
| 2024-09-20 22:21:37.678 | MS1 | 121.4656659308 | 31.1446364044 | 520 | 504990 | -86.21 | -0.46 | 74.35 | 0.09 | 1.37 | 1567 |
| 2024-09-20 22:21:38.829 | MS1 | 121.4656769216 | 31.1446307865 | 520 | 504990 | -78.20 | 13.23 | 328.63 | 0.08 | 1.44 | 1569 |
| 2024-09-20 22:21:39.220 | MS1 | 121.4656724722 | 31.1446254699 | 520 | 504990 | -77.07 | 17.06 | 427.03 | 0.19 | 1.11 | 1582 |
| 2024-09-20 22:21:40.664 | MS1 | 121.4656682035 | 31.1446207256 | 520 | 504990 | -79.24 | 12.17 | 344.76 | 0.15 | 2.99 | 1566 |
| 2024-09-20 22:21:41.211 | MS1 | 121.4656726253 | 31.1446362322 | 520 | 504990 | -81.29 | 16.47 | 375.65 | 0.06 | 2.43 | 1571 |
| 2024-09-20 22:21:42.740 | MS1 | 121.4656751119 | 31.1446215171 | 520 | 504990 | -84.97 | 17.37 | 395.61 | 0.18 | 2.02 | 1562 |

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
| 3214385 | 1 | 121.4654876201 | 31.1479352473 | 146 | 12 | 7 | 45.6 | TDD | 520 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3217272 | 4 | 121.4729186052 | 31.1549987264 | 136 | 15 | 6 | 30.2 | TDD | 887 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3225335 | 3 | 121.4746183930 | 31.1470632122 | 290 | 4 | 3 | 17.5 | TDD | 183 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3230115 | 2 | 121.4701691910 | 31.1449895115 | 323 | 14 | 7 | 30.1 | TDD | 488 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.819 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.843 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.943 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.943 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.683 | NREventA3 | measId:2;ServCellPCI:440;Se... |
| 2024-09-20 22:21:35.683 | NREventA3 | measId:2;ServCellPCI:440;Se... |
| 2024-09-20 22:21:36.683 | NREventA3 | measId:2;ServCellPCI:440;Se... |
| 2024-09-20 22:21:39.183 | NRRRCReestablishAttempt | PCI:440 |
| 2024-09-20 22:21:39.198 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.210 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.339 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.339 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214385 | 1 | 10.2518 | 17.2624 | -117.9935 | 11.1716 | 103.6442 | 0.0154 | 0.1191 |
| 2024_09_20 22:00 | 3230115 | 2 | 18.0967 | 10.1002 | -116.0109 | 12.3532 | 131.5914 | 0.0065 | 0.0107 |
| 2024_09_20 22:00 | 3225335 | 3 | 14.0717 | 12.3740 | -117.8152 | 9.1560 | 184.1519 | 0.0171 | 0.0107 |
| 2024_09_20 22:00 | 3217272 | 4 | 8.0646 | 15.6912 | -115.7192 | 6.4613 | 126.3557 | 0.0002 | 0.0046 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411981_F6BF401D | 504990 | 520 | -92.6 | 504990 | 183 | -86.8 | 504990 | 887 | -95.7 | 504990 | 488 |
| MR_1774411981_64B2CAD9 | 504990 | 520 | -94.5 | 504990 | 183 | -88.6 | 504990 | 887 | -96.9 | 504990 | 488 |
| MR_1774411981_143EEAB5 | 504990 | 520 | -92.0 | 504990 | 183 | -88.9 | 504990 | 887 | -97.2 | 504990 | 488 |
| MR_1774411981_343C8A62 | 504990 | 520 | -95.5 | 504990 | 183 | -87.0 | 504990 | 887 | -96.1 | 504990 | 488 |
| MR_1774411981_83231CB6 | 504990 | 183 | -88.2 | 504990 | 520 | -95.7 | 504990 | 887 | -98.5 | 504990 | 488 |
| MR_1774411981_88E7F583 | 504990 | 183 | -87.2 | 504990 | 520 | -94.2 | 504990 | 887 | -95.8 | 504990 | 488 |
| MR_1774411981_ADDA41C1 | 504990 | 520 | -95.7 | 504990 | 183 | -87.0 | 504990 | 887 | -97.7 | 504990 | 488 |
| MR_1774411981_89B7172F | 504990 | 183 | -88.6 | 504990 | 520 | -93.5 | 504990 | 887 | -95.6 | 504990 | 488 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1169: `6d1837d8-c6d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6d1837d8-c6dd-4c43-999f-70ceee4cf90d` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Decrease A3 Offset threshold for 3271149_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1169] topology](images/train_1169.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase transmission power for 3276526_1
- `C3`: Decrease A3 Offset threshold for 3276526_1
- `C4`: Decrease A3 Offset threshold for 3271149_2 **← 정답**
- `C5`: Check test server and transmission issues
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271149_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276526_1
- `C8`: Lift the tilt angle  of 3276526_1 by 5 degrees
- `C9`: Increase A3 Offset threshold for 3271149_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271149_2
- `C11`: Lift the tilt angle of 3271149_2 by 10 degrees
- `C12`: Increase transmission power for 3271149_2
- `C13`: Adjust the azimuth of 3276526_1 by 44 degrees
- `C14`: Decrease transmission power for 3276526_1
- `C15`: Adjust the azimuth of 3271149_2 by 46 degrees
- `C16`: Add neighbor relationship between 3237947_3 and 3276526_1
- `C17`: Add neighbor relationship between 3271149_2 and 3276526_1
- `C18`: Press down the tilt angle  of 3276526_1 by 5 degrees
- `C19`: Press down the tilt angle of 3271149_2 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3276526_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276526_1
- `C22`: Decrease transmission power for 3271149_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.675 | MS1 | 121.4656717998 | 31.1446215308 | 684 | 504990 | -78.72 | 12.90 | 354.75 | 0.18 | 2.14 | 1571 |
| 2024-09-20 22:21:32.620 | MS1 | 121.4656743553 | 31.1446199247 | 684 | 504990 | -77.11 | 12.36 | 595.36 | 0.08 | 2.02 | 1564 |
| 2024-09-20 22:21:33.651 | MS1 | 121.4656653240 | 31.1446222276 | 684 | 504990 | -84.22 | 15.94 | 534.86 | 0.10 | 2.09 | 1561 |
| 2024-09-20 22:21:34.765 | MS1 | 121.4656695017 | 31.1446194913 | 684 | 504990 | -86.75 | -3.25 | 32.31 | 0.13 | 1.43 | 1586 |
| 2024-09-20 22:21:35.685 | MS1 | 121.4656708905 | 31.1446235442 | 684 | 504990 | -85.84 | -2.02 | 41.69 | 0.16 | 1.31 | 1596 |
| 2024-09-20 22:21:36.865 | MS1 | 121.4656672600 | 31.1446236188 | 684 | 504990 | -84.25 | -0.04 | 48.43 | 0.06 | 1.31 | 1588 |
| 2024-09-20 22:21:37.434 | MS1 | 121.4656619440 | 31.1446364638 | 684 | 504990 | -86.27 | -3.92 | 61.78 | 0.15 | 1.17 | 1591 |
| 2024-09-20 22:21:38.137 | MS1 | 121.4656587577 | 31.1446231528 | 684 | 504990 | -86.47 | -1.85 | 67.92 | 0.16 | 1.38 | 1566 |
| 2024-09-20 22:21:39.655 | MS1 | 121.4656765282 | 31.1446296050 | 325 | 504990 | -76.09 | 17.65 | 214.00 | 0.11 | 1.08 | 1578 |
| 2024-09-20 22:21:40.958 | MS1 | 121.4656726937 | 31.1446287495 | 325 | 504990 | -75.88 | 15.30 | 333.13 | 0.17 | 2.61 | 1580 |
| 2024-09-20 22:21:41.226 | MS1 | 121.4656602773 | 31.1446373187 | 325 | 504990 | -81.23 | 12.24 | 595.56 | 0.07 | 2.12 | 1594 |
| 2024-09-20 22:21:42.189 | MS1 | 121.4656686501 | 31.1446263185 | 325 | 504990 | -77.02 | 14.70 | 512.57 | 0.01 | 2.54 | 1581 |

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
| 3230818 | 4 | 121.4727276280 | 31.1540684274 | 228 | 0 | 9 | 41.0 | TDD | 701 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3237947 | 3 | 121.4648792118 | 31.1461273098 | 77 | 1 | 9 | 19.4 | TDD | 821 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3271149 | 2 | 121.4658621392 | 31.1557996393 | 227 | 12 | 5 | 37.3 | TDD | 684 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3276526 | 1 | 121.4658069670 | 31.1487429459 | 226 | 1 | 8 | 34.6 | TDD | 325 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.911 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.926 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.052 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.052 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.764 | NREventA3 | measId:2;ServCellPCI:137;Se... |
| 2024-09-20 22:21:38.004 | NRHandoverAttempt | SourcePCI:137;SourceNR-ARFC... |
| 2024-09-20 22:21:38.047 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.058 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.197 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.197 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276526 | 1 | 14.6341 | 7.9547 | -114.7197 | 10.4897 | 94.3429 | 0.0134 | 0.0169 |
| 2024_09_20 22:00 | 3271149 | 2 | 14.3453 | 18.4968 | -117.6356 | 7.2856 | 104.6183 | 0.0172 | 0.1884 |
| 2024_09_20 22:00 | 3237947 | 3 | 8.2044 | 17.3939 | -116.3723 | 15.9645 | 167.0577 | 0.0019 | 0.0109 |
| 2024_09_20 22:00 | 3230818 | 4 | 9.7489 | 18.0229 | -115.8318 | 11.7304 | 105.7306 | 0.0168 | 0.0103 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415583_54FFAFA3 | 504990 | 325 | -82.0 | 504990 | 684 | -88.3 | 504990 | 821 | -89.2 | 504990 | 701 |
| MR_1774415583_18E9F0FC | 504990 | 325 | -80.2 | 504990 | 684 | -86.8 | 504990 | 821 | -89.1 | 504990 | 701 |
| MR_1774415583_3B278194 | 504990 | 684 | -87.6 | 504990 | 325 | -82.6 | 504990 | 821 | -90.7 | 504990 | 701 |
| MR_1774415583_A4ACFCE9 | 504990 | 684 | -87.6 | 504990 | 325 | -81.9 | 504990 | 821 | -91.3 | 504990 | 701 |
| MR_1774415583_2A934C1A | 504990 | 325 | -81.7 | 504990 | 684 | -85.3 | 504990 | 821 | -89.4 | 504990 | 701 |
| MR_1774415583_D278A7E8 | 504990 | 684 | -85.0 | 504990 | 325 | -82.1 | 504990 | 821 | -92.2 | 504990 | 701 |
| MR_1774415583_A7CD50C4 | 504990 | 325 | -80.0 | 504990 | 684 | -86.8 | 504990 | 821 | -89.1 | 504990 | 701 |

> *... 2개 열 생략 (전체 14열)*

---
