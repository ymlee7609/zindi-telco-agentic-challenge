# Track A 문제 분석 — test[460]~test[469]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[460] ~ test[469] (10개)

## 목차

1. [문제 460: `a577deab-98f...`](#460) — single-answer
2. [문제 461: `876ed32a-9d2...`](#461) — single-answer
3. [문제 462: `f36fa200-266...`](#462) — single-answer
4. [문제 463: `30773ba2-557...`](#463) — single-answer
5. [문제 464: `cde99b8d-9cf...`](#464) — single-answer
6. [문제 465: `7d3b4269-14d...`](#465) — single-answer
7. [문제 466: `62ef2bda-632...`](#466) — single-answer
8. [문제 467: `306eb76b-a77...`](#467) — multiple-answer
9. [문제 468: `d86c1476-bc3...`](#468) — single-answer
10. [문제 469: `0b51cf22-a36...`](#469) — single-answer

---

### 문제 460: `a577deab-98f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a577deab-98fa-437f-9d62-8a24dd68eb29` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[460] topology](images/test_0460.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3247872_1 by 10 degrees
- `C2`: Add neighbor relationship between 3247872_1 and 3272622_4
- `C3`: Press down the tilt angle of 3247872_1 by 10 degrees
- `C4`: Decrease transmission power for 3247872_1
- `C5`: Increase transmission power for 3272622_4
- `C6`: Decrease transmission power for 3272622_4
- `C7`: Decrease A3 Offset threshold for 3272622_4
- `C8`: Increase A3 Offset threshold for 3272622_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247872_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272622_4
- `C11`: Increase A3 Offset threshold for 3247872_1
- `C12`: Adjust the azimuth of 3247872_1 by 29 degrees
- `C13`: Press down the tilt angle  of 3272622_4 by 10 degrees
- `C14`: Decrease A3 Offset threshold for 3247872_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Check test server and transmission issues
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247872_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272622_4
- `C19`: Adjust the azimuth of 3272622_4 by 9 degrees
- `C20`: Increase transmission power for 3247872_1
- `C21`: Lift the tilt angle  of 3272622_4 by 10 degrees
- `C22`: Add neighbor relationship between 3215942_3 and 3272622_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.653 | MS1 | 121.4656631395 | 31.1446362978 | 336 | 504990 | -79.65 | 16.02 | 402.63 | 0.16 | 2.93 | 1560 |
| 2024-09-20 22:21:32.486 | MS1 | 121.4656728162 | 31.1446367094 | 336 | 504990 | -80.64 | 17.13 | 593.82 | 0.04 | 2.58 | 1596 |
| 2024-09-20 22:21:33.212 | MS1 | 121.4656770683 | 31.1446378242 | 336 | 504990 | -83.39 | 13.47 | 499.01 | 0.19 | 2.28 | 1576 |
| 2024-09-20 22:21:34.375 | MS1 | 121.4656602313 | 31.1446232468 | 336 | 504990 | -89.34 | -2.98 | 55.61 | 0.12 | 1.25 | 1600 |
| 2024-09-20 22:21:35.759 | MS1 | 121.4656628559 | 31.1446269415 | 336 | 504990 | -84.39 | -1.88 | 56.69 | 0.08 | 1.08 | 1581 |
| 2024-09-20 22:21:36.170 | MS1 | 121.4656592060 | 31.1446221323 | 336 | 504990 | -87.92 | -2.07 | 30.06 | 0.17 | 1.21 | 1571 |
| 2024-09-20 22:21:37.967 | MS1 | 121.4656674974 | 31.1446253995 | 336 | 504990 | -91.41 | -1.33 | 54.62 | 0.16 | 1.04 | 1592 |
| 2024-09-20 22:21:38.820 | MS1 | 121.4656730398 | 31.1446319251 | 336 | 504990 | -87.09 | -2.53 | 71.56 | 0.01 | 1.36 | 1579 |
| 2024-09-20 22:21:39.841 | MS1 | 121.4656687920 | 31.1446197125 | 623 | 504990 | -82.41 | 14.35 | 241.79 | 0.18 | 1.07 | 1596 |
| 2024-09-20 22:21:40.192 | MS1 | 121.4656645460 | 31.1446345219 | 623 | 504990 | -79.10 | 16.31 | 573.11 | 0.02 | 2.67 | 1572 |
| 2024-09-20 22:21:41.175 | MS1 | 121.4656611625 | 31.1446310018 | 623 | 504990 | -84.58 | 15.58 | 418.34 | 0.11 | 2.36 | 1589 |
| 2024-09-20 22:21:42.294 | MS1 | 121.4656723100 | 31.1446221776 | 623 | 504990 | -78.38 | 15.05 | 527.64 | 0.20 | 2.07 | 1597 |

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
| 3215942 | 3 | 121.4686069818 | 31.1448260930 | 141 | 13 | 8 | 48.6 | TDD | 112 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3221313 | 2 | 121.4721887287 | 31.1455336205 | 153 | 0 | 5 | 49.1 | TDD | 476 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3247872 | 1 | 121.4697830436 | 31.1495610673 | 187 | 13 | 3 | 43.7 | TDD | 336 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3272622 | 4 | 121.4672839333 | 31.1468218395 | 203 | 12 | 8 | 49.0 | TDD | 623 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.020 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.044 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.191 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.191 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.870 | NREventA3 | measId:2;ServCellPCI:9;Serv... |
| 2024-09-20 22:21:38.110 | NRHandoverAttempt | SourcePCI:9;SourceNR-ARFCN:... |
| 2024-09-20 22:21:38.147 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.157 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.282 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.282 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247872 | 1 | 18.8415 | 14.2868 | -114.7518 | 18.9651 | 128.8976 | 0.0141 | 0.1892 |
| 2024_09_20 22:00 | 3221313 | 2 | 14.9338 | 10.8921 | -117.0728 | 16.2448 | 179.9359 | 0.0120 | 0.0075 |
| 2024_09_20 22:00 | 3215942 | 3 | 9.3717 | 17.0392 | -117.3657 | 8.1542 | 110.5016 | 0.0190 | 0.0136 |
| 2024_09_20 22:00 | 3272622 | 4 | 17.2573 | 5.1882 | -116.5877 | 11.7365 | 116.5047 | 0.0185 | 0.0177 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415239_E8CA491E | 504990 | 336 | -90.5 | 504990 | 623 | -81.5 | 504990 | 112 | -85.1 | 504990 | 476 |
| MR_1774415239_7CCD730A | 504990 | 623 | -80.3 | 504990 | 336 | -90.4 | 504990 | 112 | -84.5 | 504990 | 476 |
| MR_1774415239_62152322 | 504990 | 623 | -82.7 | 504990 | 336 | -90.6 | 504990 | 112 | -86.7 | 504990 | 476 |
| MR_1774415239_AD75866B | 504990 | 336 | -91.3 | 504990 | 623 | -83.7 | 504990 | 112 | -86.7 | 504990 | 476 |
| MR_1774415239_6136870B | 504990 | 336 | -88.4 | 504990 | 623 | -83.2 | 504990 | 112 | -84.4 | 504990 | 476 |
| MR_1774415239_28A0FF89 | 504990 | 336 | -87.6 | 504990 | 623 | -83.1 | 504990 | 112 | -86.0 | 504990 | 476 |
| MR_1774415239_B0B24AC0 | 504990 | 336 | -91.0 | 504990 | 623 | -81.2 | 504990 | 112 | -84.7 | 504990 | 476 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 461: `876ed32a-9d2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `876ed32a-9d20-451a-ab34-cf00a359c9ab` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[461] topology](images/test_0461.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3214994_2 by 50 degrees
- `C2`: Decrease transmission power for 3216557_1
- `C3`: Increase A3 Offset threshold for 3214994_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216557_1
- `C5`: Check test server and transmission issues
- `C6`: Add neighbor relationship between 3214713_3 and 3216557_1
- `C7`: Lift the tilt angle  of 3216557_1 by 8 degrees
- `C8`: Press down the tilt angle  of 3216557_1 by 8 degrees
- `C9`: Decrease A3 Offset threshold for 3216557_1
- `C10`: Add neighbor relationship between 3214994_2 and 3216557_1
- `C11`: Lift the tilt angle of 3214994_2 by 10 degrees
- `C12`: Press down the tilt angle of 3214994_2 by 10 degrees
- `C13`: Adjust the azimuth of 3216557_1 by 37 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214994_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214994_2
- `C16`: Decrease A3 Offset threshold for 3214994_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216557_1
- `C18`: Increase A3 Offset threshold for 3216557_1
- `C19`: Increase transmission power for 3214994_2
- `C20`: Increase transmission power for 3216557_1
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease transmission power for 3214994_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.448 | MS1 | 121.4656752615 | 31.1446331281 | 522 | 504990 | -76.82 | 16.54 | 499.59 | 0.10 | 2.08 | 1581 |
| 2024-09-20 22:21:32.355 | MS1 | 121.4656749525 | 31.1446209815 | 522 | 504990 | -83.27 | 15.22 | 389.25 | 0.16 | 2.01 | 1589 |
| 2024-09-20 22:21:33.855 | MS1 | 121.4656754030 | 31.1446350463 | 522 | 504990 | -84.03 | 14.22 | 451.38 | 0.15 | 2.02 | 1577 |
| 2024-09-20 22:21:34.137 | MS1 | 121.4656650616 | 31.1446193256 | 522 | 504990 | -87.49 | -0.85 | 24.48 | 0.02 | 1.23 | 1589 |
| 2024-09-20 22:21:35.733 | MS1 | 121.4656752905 | 31.1446254097 | 522 | 504990 | -92.19 | -4.00 | 56.72 | 0.05 | 1.50 | 1562 |
| 2024-09-20 22:21:36.682 | MS1 | 121.4656647596 | 31.1446183509 | 522 | 504990 | -84.18 | -3.30 | 71.18 | 0.02 | 1.25 | 1561 |
| 2024-09-20 22:21:37.639 | MS1 | 121.4656700134 | 31.1446369297 | 522 | 504990 | -86.05 | -2.71 | 77.55 | 0.11 | 1.03 | 1582 |
| 2024-09-20 22:21:38.677 | MS1 | 121.4656697429 | 31.1446344614 | 522 | 504990 | -92.60 | -1.18 | 34.02 | 0.09 | 1.01 | 1575 |
| 2024-09-20 22:21:39.254 | MS1 | 121.4656745942 | 31.1446372411 | 17 | 504990 | -75.76 | 16.74 | 250.65 | 0.10 | 1.29 | 1584 |
| 2024-09-20 22:21:40.527 | MS1 | 121.4656622494 | 31.1446253454 | 17 | 504990 | -79.42 | 17.87 | 519.75 | 0.01 | 2.59 | 1594 |
| 2024-09-20 22:21:41.550 | MS1 | 121.4656625341 | 31.1446256789 | 17 | 504990 | -75.67 | 15.03 | 370.22 | 0.09 | 2.67 | 1590 |
| 2024-09-20 22:21:42.728 | MS1 | 121.4656636254 | 31.1446337523 | 17 | 504990 | -82.37 | 12.62 | 441.11 | 0.02 | 2.31 | 1566 |

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
| 3214713 | 3 | 121.4742295231 | 31.1499255272 | 265 | 4 | 11 | 37.8 | TDD | 604 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3214994 | 2 | 121.4720035277 | 31.1489291747 | 64 | 11 | 5 | 35.1 | TDD | 522 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3216557 | 1 | 121.4717585300 | 31.1507835283 | 183 | 6 | 4 | 27.8 | TDD | 17 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3232389 | 4 | 121.4671163726 | 31.1476693440 | 138 | 5 | 0 | 48.6 | TDD | 1005 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.443 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.460 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.571 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.571 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.308 | NREventA3 | measId:2;ServCellPCI:239;Se... |
| 2024-09-20 22:21:38.548 | NRHandoverAttempt | SourcePCI:239;SourceNR-ARFC... |
| 2024-09-20 22:21:38.593 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.605 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.747 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.747 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216557 | 1 | 10.1242 | 6.3809 | -114.9195 | 15.8606 | 181.2662 | 0.0115 | 0.0183 |
| 2024_09_20 22:00 | 3214994 | 2 | 8.8978 | 6.5830 | -117.3374 | 6.1980 | 114.4381 | 0.0083 | 0.1442 |
| 2024_09_20 22:00 | 3214713 | 3 | 13.7375 | 8.0289 | -116.8956 | 16.1405 | 158.6128 | 0.0194 | 0.0001 |
| 2024_09_20 22:00 | 3232389 | 4 | 10.6053 | 16.2723 | -116.5772 | 8.1117 | 142.8145 | 0.0084 | 0.0144 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416597_B1FDEA93 | 504990 | 522 | -85.8 | 504990 | 17 | -81.6 | 504990 | 604 | -85.6 | 504990 | 1005 |
| MR_1774416597_9F9330B5 | 504990 | 522 | -88.4 | 504990 | 17 | -82.3 | 504990 | 604 | -87.3 | 504990 | 1005 |
| MR_1774416597_9518B01C | 504990 | 522 | -86.3 | 504990 | 17 | -82.5 | 504990 | 604 | -86.0 | 504990 | 1005 |
| MR_1774416597_601F41CE | 504990 | 17 | -80.4 | 504990 | 522 | -86.5 | 504990 | 604 | -86.4 | 504990 | 1005 |
| MR_1774416597_BC794D26 | 504990 | 522 | -87.4 | 504990 | 17 | -83.9 | 504990 | 604 | -88.7 | 504990 | 1005 |
| MR_1774416597_C319225A | 504990 | 522 | -86.3 | 504990 | 17 | -83.0 | 504990 | 604 | -87.4 | 504990 | 1005 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 462: `f36fa200-266...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f36fa200-2663-43b7-9c2e-38e2d86d4cdd` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[462] topology](images/test_0462.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3230391_4
- `C2`: Increase A3 Offset threshold for 3266520_6
- `C3`: Check test server and transmission issues
- `C4`: Increase A3 Offset threshold for 3230391_4
- `C5`: Add neighbor relationship between 3239961_8 and 3266520_6
- `C6`: Decrease transmission power for 3230391_4
- `C7`: Increase transmission power for 3266520_6
- `C8`: Adjust the azimuth of 3230391_4 by 27 degrees
- `C9`: Decrease A3 Offset threshold for 3230391_4
- `C10`: Adjust the azimuth of 3266520_6 by 30 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230391_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266520_6
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease A3 Offset threshold for 3266520_6
- `C15`: Lift the tilt angle of 3230391_4 by 3 degrees
- `C16`: Press down the tilt angle  of 3266520_6 by 4 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266520_6
- `C18`: Add neighbor relationship between 3230391_4 and 3266520_6
- `C19`: Decrease transmission power for 3266520_6
- `C20`: Press down the tilt angle of 3230391_4 by 3 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230391_4
- `C22`: Lift the tilt angle  of 3266520_6 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.485 | MS1 | 121.4656775755 | 31.1446189795 | 589 | 504990 | -93.12 | 13.51 | 417.61 | 0.05 | 2.87 | 1586 |
| 2024-09-20 22:21:32.860 | MS1 | 121.4656606741 | 31.1446196876 | 824 | 504990 | -93.62 | 13.89 | 425.75 | 0.11 | 2.30 | 1576 |
| 2024-09-20 22:21:33.992 | MS1 | 121.4656733469 | 31.1446231185 | 41 | 504990 | -95.81 | 9.22 | 402.57 | 0.07 | 2.96 | 1588 |
| 2024-09-20 22:21:34.320 | MS1 | 121.4656661492 | 31.1446203800 | 62 | 152650 | -92.99 | 7.48 | 61.24 | 0.17 | 1.81 | 955 |
| 2024-09-20 22:21:35.129 | MS1 | 121.4656708989 | 31.1446367758 | 906 | 152650 | -91.52 | 7.51 | 50.45 | 0.18 | 1.98 | 920 |
| 2024-09-20 22:21:36.228 | MS1 | 121.4656622355 | 31.1446376268 | 451 | 152650 | -89.58 | 4.18 | 103.17 | 0.10 | 1.72 | 946 |
| 2024-09-20 22:21:37.407 | MS1 | 121.4656666900 | 31.1446304995 | 982 | 152650 | -93.27 | 6.27 | 81.96 | 0.02 | 1.84 | 936 |
| 2024-09-20 22:21:38.809 | MS1 | 121.4656594239 | 31.1446271160 | 62 | 152650 | -96.60 | 7.68 | 54.26 | 0.06 | 1.87 | 952 |
| 2024-09-20 22:21:39.135 | MS1 | 121.4656712087 | 31.1446229929 | 906 | 152650 | -88.40 | 3.08 | 72.61 | 0.12 | 1.72 | 922 |
| 2024-09-20 22:21:40.799 | MS1 | 121.4656668785 | 31.1446190261 | 451 | 152650 | -87.64 | 3.65 | 96.72 | 0.17 | 2.89 | 1593 |
| 2024-09-20 22:21:41.810 | MS1 | 121.4656585565 | 31.1446318984 | 982 | 152650 | -96.36 | 4.32 | 80.91 | 0.04 | 2.48 | 1574 |
| 2024-09-20 22:21:42.685 | MS1 | 121.4656638393 | 31.1446342995 | 62 | 152650 | -93.38 | 3.46 | 72.18 | 0.07 | 3.00 | 1580 |

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
| 3225110 | 11 | 121.4646142652 | 31.1553296537 | 170 | 15 | 1 | 28.5 | FDD | 657 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3229628 | 9 | 121.4663507609 | 31.1553066078 | 152 | 3 | 5 | 5.4 | FDD | 906 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3230391 | 4 | 121.4737800794 | 31.1465183649 | 228 | 3 | 2 | 5.5 | TDD | 589 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3232098 | 5 | 121.4693808877 | 31.1464555749 | 63 | 0 | 2 | 13.9 | TDD | 824 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3234617 | 13 | 121.4698925814 | 31.1498232365 | 342 | 13 | 2 | 15.8 | FDD | 62 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3235907 | 1 | 121.4692837833 | 31.1442701385 | 28 | 4 | 8 | 17.8 | TDD | 769 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3239961 | 8 | 121.4730963146 | 31.1550459826 | 331 | 2 | 5 | 28.0 | FDD | 451 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3241525 | 3 | 121.4726690418 | 31.1542547420 | 149 | 10 | 12 | 28.6 | TDD | 41 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3249113 | 10 | 121.4699219942 | 31.1472615021 | 176 | 6 | 10 | 10.8 | FDD | 751 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3254671 | 2 | 121.4746905901 | 31.1525375334 | 306 | 11 | 10 | 25.6 | TDD | 551 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3255602 | 12 | 121.4646377913 | 31.1486661070 | 249 | 0 | 0 | 14.7 | FDD | 982 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3266520 | 6 | 121.4686708749 | 31.1487681390 | 182 | 2 | 8 | 18.8 | TDD | 729 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3273188 | 7 | 121.4707618331 | 31.1485842590 | 87 | 12 | 8 | 7.3 | FDD | 770 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |

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
| 2024-09-20 22:21:31.532 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.551 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.662 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.662 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.417 | NREventA2 | measId:1;ServCellPCI:754;Se... |
| 2024-09-20 22:21:35.520 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.728 | NREventA5 | measId:3;ServCellPCI:754;Se... |
| 2024-09-20 22:21:35.758 | NRHandoverAttempt | SourcePCI:754;SourceNR-ARFC... |
| 2024-09-20 22:21:35.804 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.814 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.954 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.954 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235907 | 1 | 12.7350 | 16.2439 | -116.7355 | 15.4051 | 133.9955 | 0.0132 | 0.0142 |
| 2024_09_20 22:00 | 3254671 | 2 | 8.5721 | 17.2630 | -115.7926 | 18.7617 | 130.6614 | 0.0156 | 0.0034 |
| 2024_09_20 22:00 | 3241525 | 3 | 6.3567 | 5.2351 | -114.2888 | 13.3505 | 153.2542 | 0.0134 | 0.0176 |
| 2024_09_20 22:00 | 3230391 | 4 | 10.5379 | 13.2347 | -117.3346 | 14.1262 | 148.3091 | 0.0003 | 0.0120 |
| 2024_09_20 22:00 | 3232098 | 5 | 8.2305 | 11.0977 | -115.9154 | 16.3158 | 131.1649 | 0.0133 | 0.0070 |
| 2024_09_20 22:00 | 3266520 | 6 | 18.3911 | 7.6309 | -117.4434 | 5.9587 | 186.4728 | 0.0059 | 0.0061 |
| 2024_09_20 22:00 | 3273188 | 7 | 17.1890 | 19.6847 | -115.1176 | 3.5375 | 56.2094 | 0.0126 | 0.0160 |
| 2024_09_20 22:00 | 3239961 | 8 | 10.9994 | 6.4088 | -117.5795 | 4.4404 | 42.6737 | 0.0024 | 0.0164 |
| 2024_09_20 22:00 | 3229628 | 9 | 14.5388 | 5.3458 | -114.0250 | 4.0791 | 48.3650 | 0.0196 | 0.0034 |
| 2024_09_20 22:00 | 3249113 | 10 | 19.5428 | 18.3060 | -117.5708 | 4.9612 | 23.3545 | 0.0093 | 0.0190 |
| 2024_09_20 22:00 | 3225110 | 11 | 10.1384 | 16.9228 | -116.5786 | 3.3502 | 24.6842 | 0.0110 | 0.0070 |
| 2024_09_20 22:00 | 3255602 | 12 | 14.5474 | 17.8460 | -116.4173 | 4.2302 | 30.3264 | 0.0165 | 0.0003 |
| 2024_09_20 22:00 | 3234617 | 13 | 17.7585 | 9.8868 | -114.8103 | 4.4466 | 20.5065 | 0.0164 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416281_4F7E9091 | 152650 | 62 | -92.3 | 152650 | 770 | -95.3 | 152650 | 657 | -105.0 | 152650 | 751 |
| MR_1774416281_F05880A9 | 504990 | 41 | -96.4 | 504990 | 729 | -101.2 | 504990 | 551 | -100.4 | 504990 | 769 |
| MR_1774416281_A192AAE4 | 504990 | 41 | -94.8 | 504990 | 729 | -101.8 | 504990 | 551 | -99.5 | 504990 | 769 |
| MR_1774416281_8D9EE58E | 152650 | 62 | -93.6 | 152650 | 770 | -97.5 | 152650 | 657 | -104.9 | 152650 | 751 |
| MR_1774416281_F73D41DF | 504990 | 41 | -94.3 | 504990 | 729 | -98.8 | 504990 | 551 | -98.9 | 504990 | 769 |
| MR_1774416281_70BA14F4 | 504990 | 41 | -93.8 | 504990 | 729 | -100.2 | 504990 | 551 | -101.3 | 504990 | 769 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 463: `30773ba2-557...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `30773ba2-5573-4f07-96ee-9d00c33f3c44` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[463] topology](images/test_0463.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3224556_3 by 2 degrees
- `C2`: Add neighbor relationship between 3243798_7 and 3224556_3
- `C3`: Decrease A3 Offset threshold for 3247776_2
- `C4`: Adjust the azimuth of 3247776_2 by 24 degrees
- `C5`: Check test server and transmission issues
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224556_3
- `C8`: Decrease transmission power for 3247776_2
- `C9`: Lift the tilt angle of 3247776_2 by 3 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247776_2
- `C11`: Increase A3 Offset threshold for 3224556_3
- `C12`: Decrease transmission power for 3224556_3
- `C13`: Increase transmission power for 3247776_2
- `C14`: Press down the tilt angle  of 3224556_3 by 2 degrees
- `C15`: Increase A3 Offset threshold for 3247776_2
- `C16`: Increase transmission power for 3224556_3
- `C17`: Decrease A3 Offset threshold for 3224556_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247776_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224556_3
- `C20`: Adjust the azimuth of 3224556_3 by 40 degrees
- `C21`: Add neighbor relationship between 3247776_2 and 3224556_3
- `C22`: Press down the tilt angle of 3247776_2 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.213 | MS1 | 121.4656646047 | 31.1446194571 | 686 | 504990 | -95.80 | 13.57 | 571.04 | 0.03 | 2.39 | 1566 |
| 2024-09-20 22:21:32.377 | MS1 | 121.4656651425 | 31.1446225548 | 954 | 504990 | -95.34 | 12.37 | 467.01 | 0.17 | 2.83 | 1569 |
| 2024-09-20 22:21:33.839 | MS1 | 121.4656649883 | 31.1446335363 | 695 | 504990 | -93.62 | 13.26 | 375.85 | 0.05 | 2.01 | 1586 |
| 2024-09-20 22:21:34.516 | MS1 | 121.4656767863 | 31.1446373581 | 494 | 152650 | -92.07 | 4.80 | 69.25 | 0.06 | 1.56 | 910 |
| 2024-09-20 22:21:35.923 | MS1 | 121.4656764168 | 31.1446270998 | 246 | 152650 | -88.49 | 2.52 | 80.23 | 0.13 | 1.63 | 938 |
| 2024-09-20 22:21:36.858 | MS1 | 121.4656624977 | 31.1446379385 | 194 | 152650 | -96.81 | 5.61 | 72.76 | 0.10 | 1.59 | 913 |
| 2024-09-20 22:21:37.301 | MS1 | 121.4656724157 | 31.1446185894 | 195 | 152650 | -90.49 | 4.65 | 86.64 | 0.18 | 1.75 | 978 |
| 2024-09-20 22:21:38.809 | MS1 | 121.4656597485 | 31.1446342443 | 494 | 152650 | -91.24 | 7.23 | 88.99 | 0.13 | 1.57 | 938 |
| 2024-09-20 22:21:39.859 | MS1 | 121.4656627300 | 31.1446365163 | 246 | 152650 | -88.13 | 3.31 | 89.64 | 0.05 | 1.97 | 914 |
| 2024-09-20 22:21:40.443 | MS1 | 121.4656764854 | 31.1446302705 | 194 | 152650 | -88.04 | 6.38 | 61.25 | 0.08 | 2.88 | 1600 |
| 2024-09-20 22:21:41.928 | MS1 | 121.4656753730 | 31.1446344945 | 195 | 152650 | -95.62 | 4.00 | 55.55 | 0.04 | 2.38 | 1578 |
| 2024-09-20 22:21:42.697 | MS1 | 121.4656610519 | 31.1446331585 | 494 | 152650 | -92.14 | 3.01 | 88.48 | 0.12 | 2.17 | 1580 |

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
| 3210497 | 12 | 121.4722230814 | 31.1476897081 | 335 | 5 | 8 | 17.1 | FDD | 184 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3224556 | 3 | 121.4747371452 | 31.1531094399 | 182 | 2 | 2 | 4.0 | TDD | 82 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3228145 | 6 | 121.4652065329 | 31.1513325261 | 136 | 15 | 2 | 27.2 | TDD | 188 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3232197 | 5 | 121.4698036223 | 31.1503304852 | 103 | 12 | 9 | 28.5 | TDD | 954 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3241626 | 10 | 121.4739839603 | 31.1479159435 | 264 | 14 | 10 | 28.2 | FDD | 494 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3243798 | 7 | 121.4732236633 | 31.1558380247 | 136 | 9 | 5 | 5.9 | FDD | 194 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3247776 | 2 | 121.4754007642 | 31.1541406772 | 197 | 2 | 4 | 15.1 | TDD | 686 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3254106 | 13 | 121.4716365111 | 31.1531457310 | 347 | 9 | 11 | 18.4 | FDD | 571 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3263544 | 1 | 121.4713174731 | 31.1524871719 | 193 | 4 | 1 | 26.7 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3266446 | 11 | 121.4691144953 | 31.1459141984 | 167 | 10 | 5 | 24.6 | FDD | 246 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3266703 | 9 | 121.4701081779 | 31.1503339723 | 12 | 10 | 6 | 22.0 | FDD | 935 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3272973 | 4 | 121.4679116053 | 31.1450887622 | 224 | 14 | 5 | 4.6 | TDD | 695 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3274460 | 8 | 121.4675326828 | 31.1474049024 | 53 | 13 | 3 | 24.1 | FDD | 195 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |

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
| 2024-09-20 22:21:30.833 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.857 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.001 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.001 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.640 | NREventA2 | measId:1;ServCellPCI:949;Se... |
| 2024-09-20 22:21:34.782 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.029 | NREventA5 | measId:3;ServCellPCI:949;Se... |
| 2024-09-20 22:21:35.092 | NRHandoverAttempt | SourcePCI:949;SourceNR-ARFC... |
| 2024-09-20 22:21:35.138 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.149 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.271 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.271 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263544 | 1 | 6.1811 | 14.3072 | -116.9835 | 12.8891 | 104.7175 | 0.0094 | 0.0013 |
| 2024_09_20 22:00 | 3247776 | 2 | 14.8383 | 18.9719 | -117.5653 | 9.2016 | 143.5862 | 0.0087 | 0.0035 |
| 2024_09_20 22:00 | 3224556 | 3 | 5.4370 | 13.1186 | -117.5612 | 19.5614 | 123.1693 | 0.0115 | 0.0115 |
| 2024_09_20 22:00 | 3272973 | 4 | 14.1715 | 16.4440 | -114.3854 | 9.4500 | 91.2237 | 0.0089 | 0.0144 |
| 2024_09_20 22:00 | 3232197 | 5 | 13.8602 | 5.0114 | -115.3950 | 16.1113 | 101.0492 | 0.0128 | 0.0091 |
| 2024_09_20 22:00 | 3228145 | 6 | 13.2920 | 8.0084 | -114.5945 | 16.2290 | 143.7566 | 0.0187 | 0.0081 |
| 2024_09_20 22:00 | 3243798 | 7 | 13.3745 | 8.0000 | -116.3830 | 4.8701 | 27.3613 | 0.0020 | 0.0017 |
| 2024_09_20 22:00 | 3274460 | 8 | 9.0503 | 13.8258 | -116.6220 | 4.3748 | 22.9911 | 0.0046 | 0.0196 |
| 2024_09_20 22:00 | 3266703 | 9 | 15.7571 | 7.0309 | -116.8407 | 3.5743 | 26.2611 | 0.0060 | 0.0054 |
| 2024_09_20 22:00 | 3241626 | 10 | 13.5232 | 14.5292 | -116.4882 | 3.4779 | 53.9439 | 0.0089 | 0.0122 |
| 2024_09_20 22:00 | 3266446 | 11 | 11.2945 | 13.6731 | -114.4126 | 4.7691 | 37.7084 | 0.0151 | 0.0200 |
| 2024_09_20 22:00 | 3210497 | 12 | 16.2665 | 5.2388 | -116.8426 | 4.7636 | 57.3461 | 0.0113 | 0.0093 |
| 2024_09_20 22:00 | 3254106 | 13 | 14.2785 | 10.0172 | -115.7252 | 3.1160 | 20.4834 | 0.0133 | 0.0200 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415028_D3CC4E79 | 152650 | 494 | -91.4 | 152650 | 935 | -96.4 | 152650 | 571 | -98.8 | 152650 | 184 |
| MR_1774415028_329D6557 | 504990 | 695 | -94.7 | 504990 | 82 | -92.7 | 504990 | 188 | -93.1 | 504990 | 129 |
| MR_1774415028_32556176 | 504990 | 695 | -93.4 | 504990 | 82 | -89.7 | 504990 | 188 | -92.2 | 504990 | 129 |
| MR_1774415028_28307A94 | 152650 | 494 | -90.6 | 152650 | 935 | -98.1 | 152650 | 571 | -100.5 | 152650 | 184 |
| MR_1774415028_D90C8DD9 | 504990 | 695 | -92.2 | 504990 | 82 | -92.7 | 504990 | 188 | -92.3 | 504990 | 129 |
| MR_1774415028_40E6B74C | 504990 | 695 | -93.6 | 504990 | 82 | -90.8 | 504990 | 188 | -93.1 | 504990 | 129 |
| MR_1774415028_47281260 | 504990 | 695 | -95.4 | 504990 | 82 | -92.6 | 504990 | 188 | -92.9 | 504990 | 129 |
| MR_1774415028_71C5F5FB | 504990 | 695 | -92.6 | 504990 | 82 | -89.6 | 504990 | 188 | -94.2 | 504990 | 129 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 464: `cde99b8d-9cf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cde99b8d-9cf0-4b85-8405-ab7f1332f668` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[464] topology](images/test_0464.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236547_1
- `C3`: Decrease transmission power for 3215999_3
- `C4`: Press down the tilt angle  of 3236547_1 by 10 degrees
- `C5`: Add neighbor relationship between 3267737_2 and 3236547_1
- `C6`: Decrease transmission power for 3236547_1
- `C7`: Lift the tilt angle of 3215999_3 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215999_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236547_1
- `C10`: Adjust the azimuth of 3236547_1 by 50 degrees
- `C11`: Add neighbor relationship between 3215999_3 and 3236547_1
- `C12`: Decrease A3 Offset threshold for 3215999_3
- `C13`: Press down the tilt angle of 3215999_3 by 10 degrees
- `C14`: Check test server and transmission issues
- `C15`: Increase transmission power for 3236547_1
- `C16`: Increase A3 Offset threshold for 3215999_3
- `C17`: Adjust the azimuth of 3215999_3 by 39 degrees
- `C18`: Increase transmission power for 3215999_3
- `C19`: Increase A3 Offset threshold for 3236547_1
- `C20`: Decrease A3 Offset threshold for 3236547_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215999_3
- `C22`: Lift the tilt angle  of 3236547_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.459 | MS1 | 121.4656667495 | 31.1446342899 | 421 | 504990 | -77.10 | 17.22 | 308.67 | 0.14 | 2.57 | 1565 |
| 2024-09-20 22:21:32.666 | MS1 | 121.4656728506 | 31.1446277023 | 421 | 504990 | -77.13 | 12.92 | 327.70 | 0.19 | 2.42 | 1570 |
| 2024-09-20 22:21:33.220 | MS1 | 121.4656750357 | 31.1446322896 | 421 | 504990 | -80.54 | 13.41 | 413.21 | 0.02 | 2.42 | 1580 |
| 2024-09-20 22:21:34.371 | MS1 | 121.4656609408 | 31.1446344499 | 421 | 504990 | -84.32 | -3.91 | 68.33 | 0.17 | 1.03 | 1581 |
| 2024-09-20 22:21:35.863 | MS1 | 121.4656609789 | 31.1446219581 | 421 | 504990 | -85.28 | -0.25 | 53.57 | 0.05 | 1.26 | 1580 |
| 2024-09-20 22:21:36.922 | MS1 | 121.4656736469 | 31.1446346268 | 421 | 504990 | -88.77 | -1.56 | 53.85 | 0.05 | 1.45 | 1579 |
| 2024-09-20 22:21:37.484 | MS1 | 121.4656706159 | 31.1446188924 | 421 | 504990 | -87.05 | -2.10 | 32.44 | 0.14 | 1.23 | 1590 |
| 2024-09-20 22:21:38.228 | MS1 | 121.4656615546 | 31.1446205520 | 421 | 504990 | -86.52 | -0.79 | 47.37 | 0.15 | 1.04 | 1580 |
| 2024-09-20 22:21:39.353 | MS1 | 121.4656610739 | 31.1446224259 | 698 | 504990 | -80.71 | 14.93 | 188.34 | 0.12 | 1.49 | 1572 |
| 2024-09-20 22:21:40.623 | MS1 | 121.4656707761 | 31.1446256067 | 698 | 504990 | -84.60 | 12.28 | 467.39 | 0.18 | 2.41 | 1568 |
| 2024-09-20 22:21:41.742 | MS1 | 121.4656655356 | 31.1446227548 | 698 | 504990 | -75.70 | 16.11 | 548.40 | 0.14 | 2.13 | 1584 |
| 2024-09-20 22:21:42.839 | MS1 | 121.4656776820 | 31.1446309564 | 698 | 504990 | -83.67 | 13.07 | 560.10 | 0.15 | 2.59 | 1589 |

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
| 3215999 | 3 | 121.4707530152 | 31.1514769583 | 173 | 11 | 2 | 49.4 | TDD | 421 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3236547 | 1 | 121.4741823539 | 31.1454646497 | 75 | 11 | 7 | 23.5 | TDD | 698 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3262150 | 4 | 121.4691830284 | 31.1510630749 | 108 | 6 | 12 | 36.6 | TDD | 397 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3267737 | 2 | 121.4663147167 | 31.1508224289 | 292 | 3 | 10 | 33.2 | TDD | 412 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.024 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.044 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.181 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.181 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.908 | NREventA3 | measId:2;ServCellPCI:737;Se... |
| 2024-09-20 22:21:38.148 | NRHandoverAttempt | SourcePCI:737;SourceNR-ARFC... |
| 2024-09-20 22:21:38.191 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.206 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.327 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.327 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236547 | 1 | 16.6397 | 15.1759 | -116.4195 | 13.5775 | 117.7309 | 0.0174 | 0.0061 |
| 2024_09_20 22:00 | 3267737 | 2 | 8.0010 | 5.6280 | -114.8599 | 6.3679 | 102.5393 | 0.0156 | 0.0156 |
| 2024_09_20 22:00 | 3215999 | 3 | 5.2098 | 5.1180 | -116.9088 | 15.7192 | 98.7158 | 0.0053 | 0.1311 |
| 2024_09_20 22:00 | 3262150 | 4 | 17.8018 | 9.5047 | -115.1341 | 12.8918 | 135.8523 | 0.0055 | 0.0012 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416053_884F04C7 | 504990 | 698 | -80.2 | 504990 | 421 | -82.5 | 504990 | 412 | -84.8 | 504990 | 397 |
| MR_1774416053_6962687A | 504990 | 421 | -82.5 | 504990 | 698 | -77.2 | 504990 | 412 | -85.5 | 504990 | 397 |
| MR_1774416053_F7CD0B05 | 504990 | 698 | -79.6 | 504990 | 421 | -84.5 | 504990 | 412 | -85.6 | 504990 | 397 |
| MR_1774416053_E9020ECF | 504990 | 698 | -80.1 | 504990 | 421 | -84.3 | 504990 | 412 | -85.2 | 504990 | 397 |
| MR_1774416053_41B57197 | 504990 | 421 | -85.1 | 504990 | 698 | -79.6 | 504990 | 412 | -85.1 | 504990 | 397 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 465: `7d3b4269-14d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7d3b4269-14da-4f3a-88e9-ef870a78e642` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[465] topology](images/test_0465.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3221244_4
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase A3 Offset threshold for 3221244_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241285_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221244_4
- `C6`: Press down the tilt angle  of 3221244_4 by 6 degrees
- `C7`: Increase A3 Offset threshold for 3241285_2
- `C8`: Adjust the azimuth of 3241285_2 by 50 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221244_4
- `C10`: Increase transmission power for 3221244_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241285_2
- `C12`: Check test server and transmission issues
- `C13`: Lift the tilt angle  of 3221244_4 by 6 degrees
- `C14`: Add neighbor relationship between 3241285_2 and 3221244_4
- `C15`: Decrease A3 Offset threshold for 3241285_2
- `C16`: Decrease transmission power for 3221244_4
- `C17`: Add neighbor relationship between 3234248_3 and 3221244_4
- `C18`: Lift the tilt angle of 3241285_2 by 3 degrees
- `C19`: Press down the tilt angle of 3241285_2 by 3 degrees
- `C20`: Increase transmission power for 3241285_2
- `C21`: Adjust the azimuth of 3221244_4 by 50 degrees
- `C22`: Decrease transmission power for 3241285_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.738 | MS1 | 121.4656646719 | 31.1446242986 | 58 | 504990 | -76.45 | 15.69 | 601.17 | 0.04 | 2.50 | 1599 |
| 2024-09-20 22:21:32.820 | MS1 | 121.4656742035 | 31.1446226180 | 58 | 504990 | -75.13 | 13.61 | 304.54 | 0.15 | 2.44 | 1562 |
| 2024-09-20 22:21:33.350 | MS1 | 121.4656585674 | 31.1446245401 | 58 | 504990 | -77.65 | 12.81 | 319.02 | 0.14 | 2.74 | 1569 |
| 2024-09-20 22:21:34.919 | MS1 | 121.4656629626 | 31.1446337009 | 58 | 504990 | -90.99 | -1.22 | 41.59 | 0.13 | 1.45 | 1590 |
| 2024-09-20 22:21:35.551 | MS1 | 121.4656720119 | 31.1446350463 | 58 | 504990 | -86.36 | -0.76 | 60.11 | 0.16 | 1.17 | 1562 |
| 2024-09-20 22:21:36.731 | MS1 | 121.4656586778 | 31.1446375169 | 58 | 504990 | -92.20 | -3.68 | 29.91 | 0.01 | 1.14 | 1563 |
| 2024-09-20 22:21:37.349 | MS1 | 121.4656697977 | 31.1446199475 | 58 | 504990 | -89.35 | -3.28 | 69.32 | 0.08 | 1.14 | 1579 |
| 2024-09-20 22:21:38.670 | MS1 | 121.4656748562 | 31.1446210116 | 58 | 504990 | -89.64 | -1.07 | 35.54 | 0.02 | 1.26 | 1597 |
| 2024-09-20 22:21:39.959 | MS1 | 121.4656598037 | 31.1446268161 | 511 | 504990 | -80.62 | 13.03 | 203.93 | 0.15 | 1.04 | 1578 |
| 2024-09-20 22:21:40.450 | MS1 | 121.4656607356 | 31.1446337541 | 511 | 504990 | -76.71 | 17.63 | 297.92 | 0.18 | 2.13 | 1596 |
| 2024-09-20 22:21:41.732 | MS1 | 121.4656756203 | 31.1446195005 | 511 | 504990 | -80.94 | 13.00 | 360.47 | 0.11 | 2.07 | 1592 |
| 2024-09-20 22:21:42.241 | MS1 | 121.4656748619 | 31.1446299856 | 511 | 504990 | -82.67 | 14.53 | 382.15 | 0.03 | 2.33 | 1593 |

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
| 3221244 | 4 | 121.4755083046 | 31.1478400319 | 57 | 4 | 8 | 28.7 | TDD | 511 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3234248 | 3 | 121.4717119989 | 31.1478658134 | 221 | 4 | 8 | 39.1 | TDD | 164 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3241285 | 2 | 121.4710459480 | 31.1446671921 | 72 | 1 | 7 | 16.3 | TDD | 58 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3274565 | 1 | 121.4683529898 | 31.1502762655 | 211 | 4 | 1 | 40.6 | TDD | 160 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.575 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.590 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.737 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.737 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.473 | NREventA3 | measId:2;ServCellPCI:540;Se... |
| 2024-09-20 22:21:38.713 | NRHandoverAttempt | SourcePCI:540;SourceNR-ARFC... |
| 2024-09-20 22:21:38.755 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.769 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.881 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.881 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274565 | 1 | 6.4326 | 19.9446 | -115.2963 | 18.4358 | 176.8246 | 0.0013 | 0.0115 |
| 2024_09_20 22:00 | 3241285 | 2 | 19.4288 | 14.1509 | -116.1625 | 14.5743 | 142.0791 | 0.0123 | 0.1919 |
| 2024_09_20 22:00 | 3234248 | 3 | 8.2748 | 16.7496 | -115.6160 | 14.7657 | 142.4384 | 0.0186 | 0.0194 |
| 2024_09_20 22:00 | 3221244 | 4 | 18.3729 | 6.2674 | -116.5096 | 13.6970 | 126.7762 | 0.0125 | 0.0071 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415978_2B0262FB | 504990 | 511 | -84.9 | 504990 | 58 | -89.6 | 504990 | 164 | -86.0 | 504990 | 160 |
| MR_1774415978_270309B6 | 504990 | 511 | -86.2 | 504990 | 58 | -91.0 | 504990 | 164 | -85.8 | 504990 | 160 |
| MR_1774415978_86A76A53 | 504990 | 58 | -91.7 | 504990 | 511 | -85.4 | 504990 | 164 | -85.2 | 504990 | 160 |
| MR_1774415978_0E58CA50 | 504990 | 58 | -92.8 | 504990 | 511 | -83.4 | 504990 | 164 | -85.8 | 504990 | 160 |
| MR_1774415978_47116EAC | 504990 | 58 | -92.3 | 504990 | 511 | -85.3 | 504990 | 164 | -85.1 | 504990 | 160 |
| MR_1774415978_EFDBA9F4 | 504990 | 58 | -89.8 | 504990 | 511 | -85.0 | 504990 | 164 | -88.6 | 504990 | 160 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 466: `62ef2bda-632...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `62ef2bda-6321-4d14-8552-23ba22c8070d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[466] topology](images/test_0466.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258939_4
- `C2`: Add neighbor relationship between 3224805_3 and 3258939_4
- `C3`: Adjust the azimuth of 3224805_3 by 50 degrees
- `C4`: Increase transmission power for 3258939_4
- `C5`: Decrease A3 Offset threshold for 3258939_4
- `C6`: Increase A3 Offset threshold for 3224805_3
- `C7`: Adjust the azimuth of 3258939_4 by 41 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224805_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224805_3
- `C10`: Press down the tilt angle of 3224805_3 by 10 degrees
- `C11`: Decrease transmission power for 3258939_4
- `C12`: Decrease transmission power for 3224805_3
- `C13`: Check test server and transmission issues
- `C14`: Add neighbor relationship between 3267048_2 and 3258939_4
- `C15`: Press down the tilt angle  of 3258939_4 by 4 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258939_4
- `C17`: Increase A3 Offset threshold for 3258939_4
- `C18`: Decrease A3 Offset threshold for 3224805_3
- `C19`: Lift the tilt angle of 3224805_3 by 10 degrees
- `C20`: Increase transmission power for 3224805_3
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Lift the tilt angle  of 3258939_4 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.163 | MS1 | 121.4656586541 | 31.1446340260 | 758 | 504990 | -80.88 | 16.23 | 332.97 | 0.01 | 2.53 | 1596 |
| 2024-09-20 22:21:32.733 | MS1 | 121.4656646347 | 31.1446318683 | 758 | 504990 | -79.14 | 16.29 | 491.98 | 0.02 | 2.10 | 1582 |
| 2024-09-20 22:21:33.506 | MS1 | 121.4656628308 | 31.1446213590 | 758 | 504990 | -84.78 | 13.17 | 364.01 | 0.19 | 2.09 | 1581 |
| 2024-09-20 22:21:34.268 | MS1 | 121.4656625340 | 31.1446330507 | 758 | 504990 | -89.19 | -1.55 | 45.89 | 0.10 | 1.02 | 1588 |
| 2024-09-20 22:21:35.118 | MS1 | 121.4656729718 | 31.1446268876 | 758 | 504990 | -87.24 | -2.30 | 46.77 | 0.05 | 1.40 | 1582 |
| 2024-09-20 22:21:36.892 | MS1 | 121.4656773722 | 31.1446229060 | 758 | 504990 | -87.53 | -1.38 | 31.14 | 0.14 | 1.08 | 1562 |
| 2024-09-20 22:21:37.340 | MS1 | 121.4656753444 | 31.1446368554 | 758 | 504990 | -87.13 | -0.26 | 31.24 | 0.19 | 1.03 | 1580 |
| 2024-09-20 22:21:38.753 | MS1 | 121.4656769028 | 31.1446353430 | 758 | 504990 | -78.23 | 16.03 | 524.78 | 0.13 | 1.23 | 1587 |
| 2024-09-20 22:21:39.730 | MS1 | 121.4656777087 | 31.1446226964 | 758 | 504990 | -84.47 | 13.27 | 461.01 | 0.15 | 1.04 | 1590 |
| 2024-09-20 22:21:40.207 | MS1 | 121.4656680915 | 31.1446284319 | 758 | 504990 | -78.17 | 16.39 | 497.89 | 0.01 | 2.54 | 1587 |
| 2024-09-20 22:21:41.304 | MS1 | 121.4656712103 | 31.1446288210 | 758 | 504990 | -75.52 | 16.62 | 558.06 | 0.02 | 2.16 | 1589 |
| 2024-09-20 22:21:42.637 | MS1 | 121.4656691373 | 31.1446261839 | 758 | 504990 | -79.46 | 16.18 | 513.64 | 0.04 | 2.03 | 1586 |

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
| 3215520 | 1 | 121.4716654622 | 31.1465680210 | 183 | 0 | 1 | 18.6 | TDD | 194 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3224805 | 3 | 121.4652631960 | 31.1489436504 | 116 | 10 | 9 | 30.8 | TDD | 758 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3258939 | 4 | 121.4715707560 | 31.1506341362 | 179 | 1 | 3 | 48.0 | TDD | 327 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3267048 | 2 | 121.4651501546 | 31.1502248959 | 175 | 10 | 5 | 30.5 | TDD | 771 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.355 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.461 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.461 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.159 | NREventA3 | measId:2;ServCellPCI:13;Ser... |
| 2024-09-20 22:21:36.159 | NREventA3 | measId:2;ServCellPCI:13;Ser... |
| 2024-09-20 22:21:37.159 | NREventA3 | measId:2;ServCellPCI:13;Ser... |
| 2024-09-20 22:21:39.659 | NRRRCReestablishAttempt | PCI:13 |
| 2024-09-20 22:21:39.670 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.682 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.827 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.827 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215520 | 1 | 6.3903 | 7.1115 | -114.0718 | 11.3974 | 160.5746 | 0.0151 | 0.0101 |
| 2024_09_20 22:00 | 3267048 | 2 | 5.3234 | 18.4798 | -117.7351 | 15.4189 | 95.6174 | 0.0165 | 0.0182 |
| 2024_09_20 22:00 | 3224805 | 3 | 11.4415 | 10.2443 | -116.4887 | 6.9020 | 160.7321 | 0.0023 | 0.1816 |
| 2024_09_20 22:00 | 3258939 | 4 | 16.7565 | 9.4981 | -115.7974 | 9.8539 | 145.0048 | 0.0078 | 0.0069 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416676_35AC1D55 | 504990 | 327 | -84.7 | 504990 | 758 | -87.8 | 504990 | 771 | -84.8 | 504990 | 194 |
| MR_1774416676_7E2A5319 | 504990 | 758 | -90.1 | 504990 | 327 | -83.4 | 504990 | 771 | -84.7 | 504990 | 194 |
| MR_1774416676_420C7F07 | 504990 | 327 | -85.3 | 504990 | 758 | -90.0 | 504990 | 771 | -86.9 | 504990 | 194 |
| MR_1774416676_6BAA439B | 504990 | 327 | -83.4 | 504990 | 758 | -88.2 | 504990 | 771 | -87.9 | 504990 | 194 |
| MR_1774416676_5E1A9602 | 504990 | 327 | -85.2 | 504990 | 758 | -87.2 | 504990 | 771 | -84.7 | 504990 | 194 |
| MR_1774416676_7E6D8BAB | 504990 | 758 | -90.0 | 504990 | 327 | -82.5 | 504990 | 771 | -85.2 | 504990 | 194 |
| MR_1774416676_D10EAB30 | 504990 | 758 | -90.5 | 504990 | 327 | -82.7 | 504990 | 771 | -87.6 | 504990 | 194 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 467: `306eb76b-a77...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `306eb76b-a77c-4a9b-b44e-5dc10d932ee9` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[467] topology](images/test_0467.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3263914_3
- `C2`: Decrease transmission power for 3263914_3
- `C3`: Increase transmission power for 3263701_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263914_3
- `C5`: Increase A3 Offset threshold for 3263701_2
- `C6`: Lift the tilt angle  of 3263701_2 by 3 degrees
- `C7`: Press down the tilt angle of 3263914_3 by 10 degrees
- `C8`: Increase A3 Offset threshold for 3263914_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263914_3
- `C10`: Decrease transmission power for 3263701_2
- `C11`: Adjust the azimuth of 3263701_2 by 47 degrees
- `C12`: Add neighbor relationship between 3254136_4 and 3263701_2
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Lift the tilt angle of 3263914_3 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3263701_2
- `C16`: Increase transmission power for 3263914_3
- `C17`: Adjust the azimuth of 3263914_3 by 41 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263701_2
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle  of 3263701_2 by 3 degrees
- `C21`: Add neighbor relationship between 3263914_3 and 3263701_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263701_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.928 | MS1 | 121.4656717642 | 31.1446357333 | 613 | 504990 | -91.10 | 14.99 | 404.54 | 0.18 | 2.50 | 1580 |
| 2024-09-20 22:21:32.281 | MS1 | 121.4656733848 | 31.1446348237 | 613 | 504990 | -93.97 | 12.69 | 437.66 | 0.01 | 2.22 | 1573 |
| 2024-09-20 22:21:33.735 | MS1 | 121.4656708327 | 31.1446378602 | 613 | 504990 | -93.07 | 15.78 | 522.02 | 0.04 | 2.35 | 1583 |
| 2024-09-20 22:21:34.725 | MS1 | 121.4656627893 | 31.1446296255 | 613 | 504990 | -109.81 | 0.79 | 85.80 | 0.00 | 1.41 | 1577 |
| 2024-09-20 22:21:35.593 | MS1 | 121.4656756175 | 31.1446230758 | 613 | 504990 | -108.24 | -1.66 | 60.42 | 0.01 | 1.25 | 1592 |
| 2024-09-20 22:21:36.466 | MS1 | 121.4656681287 | 31.1446182047 | 613 | 504990 | -104.82 | 0.13 | 32.17 | 0.20 | 1.07 | 1596 |
| 2024-09-20 22:21:37.461 | MS1 | 121.4656687988 | 31.1446343886 | 613 | 504990 | -106.22 | -0.55 | 30.92 | 0.14 | 1.21 | 1593 |
| 2024-09-20 22:21:38.871 | MS1 | 121.4656609264 | 31.1446318189 | 613 | 504990 | -107.39 | -0.33 | 64.95 | 0.15 | 1.44 | 1584 |
| 2024-09-20 22:21:39.367 | MS1 | 121.4656672276 | 31.1446266178 | 613 | 504990 | -100.45 | -1.91 | 25.65 | 0.12 | 1.18 | 1595 |
| 2024-09-20 22:21:40.306 | MS1 | 121.4656603081 | 31.1446202320 | 613 | 504990 | -94.60 | 14.49 | 340.87 | 0.01 | 2.95 | 1564 |
| 2024-09-20 22:21:41.944 | MS1 | 121.4656585842 | 31.1446235141 | 613 | 504990 | -94.00 | 14.94 | 563.96 | 0.08 | 2.41 | 1599 |
| 2024-09-20 22:21:42.844 | MS1 | 121.4656743680 | 31.1446284785 | 613 | 504990 | -85.06 | 12.55 | 353.23 | 0.02 | 2.51 | 1586 |

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
| 3210569 | 1 | 121.4694130213 | 31.1534766391 | 99 | 1 | 10 | 30.0 | TDD | 818 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3254136 | 4 | 121.4740703675 | 31.1489563756 | 85 | 6 | 7 | 22.3 | TDD | 294 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3263701 | 2 | 121.4716781089 | 31.1516115330 | 263 | 0 | 7 | 45.7 | TDD | 828 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3263914 | 3 | 121.4650554137 | 31.1451091507 | 174 | 10 | 4 | 19.2 | TDD | 613 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.318 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.343 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.471 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.471 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.657 | NREventA2 | measId:1;ServCellPCI:551;Se... |
| 2024-09-20 22:21:34.777 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210569 | 1 | 12.3758 | 19.6946 | -116.8858 | 13.8788 | 109.2349 | 0.0185 | 0.0082 |
| 2024_09_20 22:00 | 3263701 | 2 | 7.2627 | 10.8715 | -114.2023 | 11.3289 | 184.0453 | 0.0134 | 0.0032 |
| 2024_09_20 22:00 | 3263914 | 3 | 16.7127 | 11.2302 | -114.0002 | 5.5117 | 113.1257 | 0.1599 | 0.0038 |
| 2024_09_20 22:00 | 3254136 | 4 | 14.7683 | 6.7260 | -115.5375 | 7.1727 | 141.0871 | 0.0165 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414997_0ADB1A51 | 504990 | 613 | -109.5 | 504990 | 828 | -113.8 | 504990 | 294 | -119.3 | 504990 | 818 |
| MR_1774414997_E90DB507 | 504990 | 613 | -110.8 | 504990 | 828 | -113.0 | 504990 | 294 | -119.7 | 504990 | 818 |
| MR_1774414997_EDD9D055 | 504990 | 613 | -109.3 | 504990 | 828 | -115.1 | 504990 | 294 | -117.8 | 504990 | 818 |
| MR_1774414997_F14F99F8 | 504990 | 613 | -109.6 | 504990 | 828 | -113.9 | 504990 | 294 | -118.8 | 504990 | 818 |
| MR_1774414997_4DAFE531 | 504990 | 613 | -109.7 | 504990 | 828 | -116.7 | 504990 | 294 | -120.8 | 504990 | 818 |
| MR_1774414997_A312CD41 | 504990 | 613 | -109.0 | 504990 | 828 | -114.5 | 504990 | 294 | -120.6 | 504990 | 818 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 468: `d86c1476-bc3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d86c1476-bc33-49b9-bb53-c7b2424d31cf` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[468] topology](images/test_0468.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3231729_3 by 10 degrees
- `C2`: Decrease A3 Offset threshold for 3231729_3
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase transmission power for 3212026_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231729_3
- `C6`: Adjust the azimuth of 3212026_2 by 50 degrees
- `C7`: Decrease transmission power for 3231729_3
- `C8`: Increase transmission power for 3231729_3
- `C9`: Lift the tilt angle  of 3212026_2 by 3 degrees
- `C10`: Add neighbor relationship between 3225190_1 and 3212026_2
- `C11`: Decrease A3 Offset threshold for 3212026_2
- `C12`: Add neighbor relationship between 3231729_3 and 3212026_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212026_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231729_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212026_2
- `C16`: Press down the tilt angle of 3231729_3 by 10 degrees
- `C17`: Decrease transmission power for 3212026_2
- `C18`: Check test server and transmission issues
- `C19`: Increase A3 Offset threshold for 3212026_2
- `C20`: Press down the tilt angle  of 3212026_2 by 3 degrees
- `C21`: Adjust the azimuth of 3231729_3 by 50 degrees
- `C22`: Increase A3 Offset threshold for 3231729_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.941 | MS1 | 121.4656593204 | 31.1446346503 | 332 | 504990 | -80.63 | 17.80 | 368.45 | 0.14 | 2.86 | 1577 |
| 2024-09-20 22:21:32.587 | MS1 | 121.4656742108 | 31.1446245476 | 332 | 504990 | -76.09 | 16.95 | 555.25 | 0.09 | 2.66 | 1589 |
| 2024-09-20 22:21:33.689 | MS1 | 121.4656725786 | 31.1446276057 | 332 | 504990 | -76.76 | 13.30 | 323.36 | 0.11 | 2.08 | 1566 |
| 2024-09-20 22:21:34.358 | MS1 | 121.4656719699 | 31.1446316517 | 332 | 504990 | -83.64 | -1.60 | 57.23 | 0.08 | 1.21 | 1560 |
| 2024-09-20 22:21:35.371 | MS1 | 121.4656745944 | 31.1446341144 | 332 | 504990 | -87.50 | -1.77 | 61.35 | 0.12 | 1.49 | 1583 |
| 2024-09-20 22:21:36.254 | MS1 | 121.4656644112 | 31.1446260505 | 332 | 504990 | -86.29 | -3.77 | 40.75 | 0.07 | 1.02 | 1598 |
| 2024-09-20 22:21:37.909 | MS1 | 121.4656739634 | 31.1446300809 | 332 | 504990 | -85.60 | -2.88 | 41.48 | 0.13 | 1.47 | 1600 |
| 2024-09-20 22:21:38.499 | MS1 | 121.4656730022 | 31.1446325580 | 332 | 504990 | -91.81 | -3.86 | 53.97 | 0.19 | 1.00 | 1588 |
| 2024-09-20 22:21:39.320 | MS1 | 121.4656771900 | 31.1446292342 | 371 | 504990 | -82.89 | 15.27 | 245.44 | 0.17 | 1.10 | 1566 |
| 2024-09-20 22:21:40.299 | MS1 | 121.4656596985 | 31.1446352653 | 371 | 504990 | -77.26 | 17.19 | 477.54 | 0.08 | 2.23 | 1579 |
| 2024-09-20 22:21:41.716 | MS1 | 121.4656711531 | 31.1446256897 | 371 | 504990 | -77.32 | 12.48 | 311.55 | 0.10 | 2.63 | 1588 |
| 2024-09-20 22:21:42.643 | MS1 | 121.4656700931 | 31.1446354793 | 371 | 504990 | -83.70 | 16.72 | 586.56 | 0.04 | 2.73 | 1560 |

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
| 3212026 | 2 | 121.4687397341 | 31.1542970403 | 3 | 1 | 2 | 30.1 | TDD | 371 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3221924 | 4 | 121.4706001905 | 31.1456600750 | 335 | 1 | 6 | 32.6 | TDD | 484 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3225190 | 1 | 121.4653524410 | 31.1493452965 | 214 | 3 | 0 | 18.9 | TDD | 216 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3231729 | 3 | 121.4665208872 | 31.1528888700 | 74 | 9 | 0 | 22.3 | TDD | 332 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.955 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.980 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.123 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.123 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.828 | NREventA3 | measId:2;ServCellPCI:541;Se... |
| 2024-09-20 22:21:38.068 | NRHandoverAttempt | SourcePCI:541;SourceNR-ARFC... |
| 2024-09-20 22:21:38.116 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.130 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.236 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.236 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225190 | 1 | 18.2371 | 16.3146 | -115.2870 | 10.2093 | 121.4019 | 0.0108 | 0.0063 |
| 2024_09_20 22:00 | 3212026 | 2 | 16.7027 | 8.4472 | -115.7825 | 9.3119 | 197.0129 | 0.0010 | 0.0121 |
| 2024_09_20 22:00 | 3231729 | 3 | 15.1859 | 19.1965 | -115.7653 | 9.2156 | 99.1387 | 0.0128 | 0.1392 |
| 2024_09_20 22:00 | 3221924 | 4 | 15.1036 | 13.0668 | -114.1999 | 7.7906 | 146.3597 | 0.0092 | 0.0181 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412068_EA848473 | 504990 | 371 | -76.6 | 504990 | 332 | -84.7 | 504990 | 216 | -81.4 | 504990 | 484 |
| MR_1774412068_650CB75F | 504990 | 332 | -84.3 | 504990 | 371 | -78.2 | 504990 | 216 | -81.8 | 504990 | 484 |
| MR_1774412068_B743E70E | 504990 | 371 | -76.0 | 504990 | 332 | -82.2 | 504990 | 216 | -80.8 | 504990 | 484 |
| MR_1774412068_39BBC1C3 | 504990 | 332 | -83.9 | 504990 | 371 | -77.5 | 504990 | 216 | -84.2 | 504990 | 484 |
| MR_1774412068_20A716B6 | 504990 | 332 | -82.1 | 504990 | 371 | -76.7 | 504990 | 216 | -83.9 | 504990 | 484 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 469: `0b51cf22-a36...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0b51cf22-a36d-422a-aa3e-dfa9bc30773d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[469] topology](images/test_0469.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3242657_1
- `C2`: Lift the tilt angle  of 3278382_4 by 6 degrees
- `C3`: Check test server and transmission issues
- `C4`: Decrease A3 Offset threshold for 3242657_1
- `C5`: Press down the tilt angle  of 3278382_4 by 6 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248828_2
- `C7`: Increase A3 Offset threshold for 3242657_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242657_1
- `C9`: Adjust the azimuth of 3248828_2 by 47 degrees
- `C10`: Decrease transmission power for 3248828_2
- `C11`: Add neighbor relationship between 3278382_4 and 3242657_1
- `C12`: Increase transmission power for 3248828_2
- `C13`: Decrease transmission power for 3242657_1
- `C14`: Add neighbor relationship between 3248828_2 and 3242657_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Adjust the azimuth of 3278382_4 by 50 degrees
- `C17`: Decrease A3 Offset threshold for 3248828_2
- `C18`: Press down the tilt angle of 3248828_2 by 4 degrees
- `C19`: Increase A3 Offset threshold for 3248828_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242657_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248828_2
- `C22`: Lift the tilt angle of 3248828_2 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.235 | MS1 | 121.4656777777 | 31.1446207607 | 435 | 504990 | -91.53 | 14.46 | 563.68 | 0.19 | 2.01 | 1593 |
| 2024-09-20 22:21:32.768 | MS1 | 121.4656672649 | 31.1446222749 | 435 | 504990 | -87.70 | 17.95 | 540.66 | 0.15 | 2.77 | 1563 |
| 2024-09-20 22:21:33.989 | MS1 | 121.4656635640 | 31.1446339843 | 435 | 504990 | -89.11 | 15.46 | 589.70 | 0.16 | 2.95 | 1599 |
| 2024-09-20 22:21:34.450 | MS1 | 121.4656764465 | 31.1446342148 | 435 | 504990 | -86.65 | 16.00 | 54.47 | 0.02 | 2.56 | 1585 |
| 2024-09-20 22:21:35.859 | MS1 | 121.4656604773 | 31.1446297572 | 435 | 504990 | -88.68 | 17.48 | 70.94 | 0.19 | 2.98 | 1575 |
| 2024-09-20 22:21:36.886 | MS1 | 121.4656682480 | 31.1446325090 | 435 | 504990 | -90.67 | 12.88 | 83.20 | 0.15 | 2.76 | 1566 |
| 2024-09-20 22:21:37.995 | MS1 | 121.4656646312 | 31.1446185962 | 435 | 504990 | -91.87 | 10.55 | 67.60 | 0.07 | 2.37 | 1579 |
| 2024-09-20 22:21:38.634 | MS1 | 121.4656713901 | 31.1446302880 | 435 | 504990 | -92.24 | 9.13 | 102.06 | 0.09 | 2.75 | 1595 |
| 2024-09-20 22:21:39.191 | MS1 | 121.4656653102 | 31.1446217214 | 435 | 504990 | -91.47 | 9.77 | 57.29 | 0.07 | 2.87 | 1565 |
| 2024-09-20 22:21:40.355 | MS1 | 121.4656756877 | 31.1446316026 | 435 | 504990 | -89.78 | 8.47 | 585.13 | 0.15 | 2.99 | 1598 |
| 2024-09-20 22:21:41.132 | MS1 | 121.4656732371 | 31.1446220759 | 435 | 504990 | -93.37 | 9.52 | 451.56 | 0.17 | 2.45 | 1570 |
| 2024-09-20 22:21:42.525 | MS1 | 121.4656599399 | 31.1446195183 | 435 | 504990 | -92.54 | 11.39 | 342.60 | 0.09 | 2.99 | 1583 |

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
| 3242657 | 1 | 121.4728600414 | 31.1525436281 | 317 | 4 | 2 | 44.5 | TDD | 471 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3248828 | 2 | 121.4714130198 | 31.1527783277 | 164 | 2 | 7 | 42.4 | TDD | 435 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3277981 | 3 | 121.4671814582 | 31.1509691120 | 51 | 10 | 2 | 24.0 | TDD | 659 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3278382 | 4 | 121.4675908945 | 31.1505940536 | 298 | 11 | 2 | 40.7 | TDD | 499 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.114 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.136 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.251 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.251 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.002 | NREventA3 | measId:2;ServCellPCI:314;Se... |
| 2024-09-20 22:21:38.242 | NRHandoverAttempt | SourcePCI:314;SourceNR-ARFC... |
| 2024-09-20 22:21:38.291 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.302 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.411 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.411 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242657 | 1 | 14.0182 | 6.4428 | -114.2405 | 14.0242 | 114.7504 | 0.0011 | 0.0039 |
| 2024_09_20 22:00 | 3248828 | 2 | 76.2651 | 83.2436 | -116.1934 | 9.4793 | 177.7094 | 0.0166 | 0.0130 |
| 2024_09_20 22:00 | 3277981 | 3 | 9.3370 | 14.7763 | -115.4331 | 13.3756 | 175.7235 | 0.0022 | 0.0155 |
| 2024_09_20 22:00 | 3278382 | 4 | 19.1807 | 8.7172 | -117.7730 | 15.4173 | 131.0740 | 0.0009 | 0.0139 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416860_6D85D9C5 | 504990 | 435 | -86.4 | 504990 | 471 | -91.9 | 504990 | 499 | -100.7 | 504990 | 659 |
| MR_1774416860_0E2F6861 | 504990 | 435 | -85.3 | 504990 | 471 | -94.5 | 504990 | 499 | -99.6 | 504990 | 659 |
| MR_1774416860_54854B27 | 504990 | 435 | -87.3 | 504990 | 471 | -91.4 | 504990 | 499 | -101.4 | 504990 | 659 |
| MR_1774416860_D6FCD6E2 | 504990 | 435 | -87.4 | 504990 | 471 | -94.7 | 504990 | 499 | -102.6 | 504990 | 659 |
| MR_1774416860_F5E3BB2E | 504990 | 435 | -86.9 | 504990 | 471 | -92.5 | 504990 | 499 | -102.1 | 504990 | 659 |
| MR_1774416860_C76FFDF6 | 504990 | 435 | -86.0 | 504990 | 471 | -92.8 | 504990 | 499 | -103.1 | 504990 | 659 |
| MR_1774416860_411E8D51 | 504990 | 435 | -87.3 | 504990 | 471 | -93.1 | 504990 | 499 | -101.9 | 504990 | 659 |
| MR_1774416860_DEDC1303 | 504990 | 435 | -88.4 | 504990 | 471 | -92.8 | 504990 | 499 | -99.9 | 504990 | 659 |

> *... 2개 열 생략 (전체 14열)*

---
