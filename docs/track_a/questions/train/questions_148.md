# Track A 문제 분석 — train[1470]~train[1479]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1470] ~ train[1479] (10개)

## 목차

1. [문제 1470: `6c0f7445-51f...`](#1470) — single-answer, 정답: C20
2. [문제 1471: `a37fea44-18b...`](#1471) — single-answer, 정답: C11
3. [문제 1472: `cadcbc7d-baa...`](#1472) — single-answer, 정답: C16
4. [문제 1473: `64bc2b02-123...`](#1473) — multiple-answer, 정답: C6|C10|C14|C21
5. [문제 1474: `3b49f521-e11...`](#1474) — multiple-answer, 정답: C18|C21
6. [문제 1475: `1bcc7fc7-21d...`](#1475) — single-answer, 정답: C12
7. [문제 1476: `9458f9f5-c4d...`](#1476) — single-answer, 정답: C13
8. [문제 1477: `e7505cce-480...`](#1477) — single-answer, 정답: C21
9. [문제 1478: `ef1e3a6d-edb...`](#1478) — single-answer, 정답: C12
10. [문제 1479: `5b5dc2f1-718...`](#1479) — single-answer, 정답: C12

---

### 문제 1470: `6c0f7445-51f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6c0f7445-51f8-444b-9c80-046d72ed019a` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease A3 Offset threshold for 3242800_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1470] topology](images/train_1470.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3242800_2 by 1 degrees
- `C2`: Press down the tilt angle  of 3278068_4 by 10 degrees
- `C3`: Adjust the azimuth of 3242800_2 by 50 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242800_2
- `C6`: Add neighbor relationship between 3222088_1 and 3278068_4
- `C7`: Increase A3 Offset threshold for 3278068_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278068_4
- `C9`: Increase transmission power for 3278068_4
- `C10`: Adjust the azimuth of 3278068_4 by 20 degrees
- `C11`: Lift the tilt angle  of 3278068_4 by 10 degrees
- `C12`: Add neighbor relationship between 3242800_2 and 3278068_4
- `C13`: Decrease transmission power for 3278068_4
- `C14`: Decrease A3 Offset threshold for 3278068_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278068_4
- `C16`: Increase A3 Offset threshold for 3242800_2
- `C17`: Check test server and transmission issues
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242800_2
- `C19`: Press down the tilt angle of 3242800_2 by 1 degrees
- `C20`: Decrease A3 Offset threshold for 3242800_2 **← 정답**
- `C21`: Increase transmission power for 3242800_2
- `C22`: Decrease transmission power for 3242800_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.697 | MS1 | 121.4656756183 | 31.1446229622 | 737 | 504990 | -82.51 | 16.21 | 566.10 | 0.13 | 2.05 | 1577 |
| 2024-09-20 22:21:32.548 | MS1 | 121.4656768931 | 31.1446306760 | 737 | 504990 | -77.40 | 13.48 | 412.29 | 0.03 | 2.30 | 1586 |
| 2024-09-20 22:21:33.659 | MS1 | 121.4656633493 | 31.1446350454 | 737 | 504990 | -79.63 | 15.81 | 520.66 | 0.17 | 2.39 | 1576 |
| 2024-09-20 22:21:34.197 | MS1 | 121.4656687225 | 31.1446205583 | 737 | 504990 | -90.92 | -0.94 | 40.16 | 0.08 | 1.15 | 1561 |
| 2024-09-20 22:21:35.957 | MS1 | 121.4656717116 | 31.1446212027 | 737 | 504990 | -92.58 | -3.53 | 53.87 | 0.18 | 1.29 | 1566 |
| 2024-09-20 22:21:36.623 | MS1 | 121.4656779993 | 31.1446328631 | 737 | 504990 | -89.86 | -1.91 | 39.27 | 0.11 | 1.46 | 1574 |
| 2024-09-20 22:21:37.401 | MS1 | 121.4656768575 | 31.1446375273 | 737 | 504990 | -84.22 | -2.35 | 37.72 | 0.06 | 1.19 | 1581 |
| 2024-09-20 22:21:38.837 | MS1 | 121.4656615277 | 31.1446325734 | 737 | 504990 | -84.53 | -0.14 | 44.48 | 0.13 | 1.05 | 1567 |
| 2024-09-20 22:21:39.207 | MS1 | 121.4656689322 | 31.1446324708 | 654 | 504990 | -82.93 | 13.66 | 265.88 | 0.00 | 1.49 | 1599 |
| 2024-09-20 22:21:40.491 | MS1 | 121.4656747790 | 31.1446195107 | 654 | 504990 | -83.07 | 16.93 | 354.81 | 0.09 | 2.80 | 1591 |
| 2024-09-20 22:21:41.915 | MS1 | 121.4656724617 | 31.1446317753 | 654 | 504990 | -77.70 | 17.24 | 388.75 | 0.12 | 2.11 | 1591 |
| 2024-09-20 22:21:42.728 | MS1 | 121.4656588373 | 31.1446364785 | 654 | 504990 | -78.04 | 15.82 | 350.28 | 0.02 | 2.29 | 1595 |

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
| 3222088 | 1 | 121.4736817170 | 31.1491262184 | 150 | 13 | 5 | 19.6 | TDD | 576 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3242800 | 2 | 121.4676711107 | 31.1551890549 | 294 | 0 | 12 | 25.7 | TDD | 737 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3257644 | 3 | 121.4727795996 | 31.1511421789 | 305 | 1 | 3 | 24.4 | TDD | 605 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3278068 | 4 | 121.4653763729 | 31.1441373000 | 7 | 10 | 5 | 37.3 | TDD | 654 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.285 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.303 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.438 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.438 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.140 | NREventA3 | measId:2;ServCellPCI:873;Se... |
| 2024-09-20 22:21:38.380 | NRHandoverAttempt | SourcePCI:873;SourceNR-ARFC... |
| 2024-09-20 22:21:38.427 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.440 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.554 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.554 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222088 | 1 | 17.2727 | 13.0039 | -114.8100 | 7.2383 | 197.2152 | 0.0092 | 0.0117 |
| 2024_09_20 22:00 | 3242800 | 2 | 17.9004 | 18.0136 | -116.0540 | 8.4895 | 155.9539 | 0.0010 | 0.1816 |
| 2024_09_20 22:00 | 3257644 | 3 | 8.7770 | 18.2060 | -114.7205 | 9.3206 | 95.2668 | 0.0063 | 0.0132 |
| 2024_09_20 22:00 | 3278068 | 4 | 18.2002 | 14.6568 | -114.6876 | 15.4685 | 158.0403 | 0.0062 | 0.0180 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414523_02C99419 | 504990 | 654 | -86.0 | 504990 | 737 | -89.0 | 504990 | 576 | -87.5 | 504990 | 605 |
| MR_1774414523_C7CC2F6F | 504990 | 654 | -85.7 | 504990 | 737 | -90.4 | 504990 | 576 | -87.6 | 504990 | 605 |
| MR_1774414523_0EAA8442 | 504990 | 654 | -86.8 | 504990 | 737 | -89.3 | 504990 | 576 | -88.1 | 504990 | 605 |
| MR_1774414523_D14D8405 | 504990 | 737 | -92.9 | 504990 | 654 | -84.2 | 504990 | 576 | -88.7 | 504990 | 605 |
| MR_1774414523_59609143 | 504990 | 737 | -89.2 | 504990 | 654 | -85.5 | 504990 | 576 | -89.0 | 504990 | 605 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1471: `a37fea44-18b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a37fea44-18bd-4c33-9d9f-860ddb443968` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1471] topology](images/train_1471.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3250366_3
- `C2`: Increase A3 Offset threshold for 3245787_2
- `C3`: Add neighbor relationship between 3250366_3 and 3245787_2
- `C4`: Increase transmission power for 3250366_3
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Press down the tilt angle of 3250366_3 by 10 degrees
- `C7`: Lift the tilt angle of 3250366_3 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245787_2
- `C9`: Increase A3 Offset threshold for 3250366_3
- `C10`: Adjust the azimuth of 3245787_2 by 50 degrees
- `C11`: Check test server and transmission issues **← 정답**
- `C12`: Decrease transmission power for 3245787_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250366_3
- `C14`: Press down the tilt angle  of 3245787_2 by 10 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250366_3
- `C16`: Adjust the azimuth of 3250366_3 by 50 degrees
- `C17`: Decrease A3 Offset threshold for 3245787_2
- `C18`: Increase transmission power for 3245787_2
- `C19`: Lift the tilt angle  of 3245787_2 by 10 degrees
- `C20`: Decrease transmission power for 3250366_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245787_2
- `C22`: Add neighbor relationship between 3224465_1 and 3245787_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.205 | MS1 | 121.4656592154 | 31.1446287102 | 261 | 504990 | -90.79 | 12.29 | 354.50 | 0.11 | 2.52 | 1592 |
| 2024-09-20 22:21:32.846 | MS1 | 121.4656625429 | 31.1446203120 | 261 | 504990 | -90.03 | 12.41 | 579.95 | 0.11 | 2.28 | 1564 |
| 2024-09-20 22:21:33.599 | MS1 | 121.4656632672 | 31.1446364551 | 261 | 504990 | -89.40 | 15.32 | 398.91 | 0.09 | 2.72 | 1564 |
| 2024-09-20 22:21:34.429 | MS1 | 121.4656767171 | 31.1446313327 | 261 | 504990 | -89.49 | 15.17 | 84.15 | 0.10 | 2.55 | 496 |
| 2024-09-20 22:21:35.535 | MS1 | 121.4656640690 | 31.1446313228 | 261 | 504990 | -86.54 | 14.80 | 88.65 | 0.19 | 2.25 | 320 |
| 2024-09-20 22:21:36.485 | MS1 | 121.4656695606 | 31.1446331322 | 261 | 504990 | -91.31 | 13.33 | 58.02 | 0.09 | 2.15 | 320 |
| 2024-09-20 22:21:37.592 | MS1 | 121.4656618339 | 31.1446324027 | 261 | 504990 | -92.65 | 11.86 | 72.55 | 0.19 | 2.12 | 419 |
| 2024-09-20 22:21:38.140 | MS1 | 121.4656657394 | 31.1446295010 | 261 | 504990 | -92.13 | 11.61 | 104.16 | 0.02 | 2.10 | 391 |
| 2024-09-20 22:21:39.919 | MS1 | 121.4656752451 | 31.1446252653 | 261 | 504990 | -89.45 | 11.93 | 74.20 | 0.13 | 2.05 | 417 |
| 2024-09-20 22:21:40.700 | MS1 | 121.4656690759 | 31.1446320359 | 261 | 504990 | -91.21 | 12.53 | 466.33 | 0.17 | 2.30 | 1561 |
| 2024-09-20 22:21:41.763 | MS1 | 121.4656690623 | 31.1446211984 | 261 | 504990 | -90.76 | 7.60 | 467.74 | 0.20 | 2.65 | 1593 |
| 2024-09-20 22:21:42.288 | MS1 | 121.4656714523 | 31.1446333396 | 261 | 504990 | -93.30 | 12.82 | 327.34 | 0.19 | 2.15 | 1600 |

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
| 3224465 | 1 | 121.4713646962 | 31.1557606749 | 66 | 6 | 9 | 26.4 | TDD | 752 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3245787 | 2 | 121.4721028928 | 31.1517326044 | 100 | 9 | 4 | 36.6 | TDD | 810 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3250366 | 3 | 121.4662420309 | 31.1475451071 | 351 | 14 | 5 | 42.9 | TDD | 261 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3251171 | 4 | 121.4693373862 | 31.1504906955 | 31 | 4 | 9 | 33.6 | TDD | 656 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.501 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.521 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.660 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.660 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.338 | NREventA3 | measId:2;ServCellPCI:514;Se... |
| 2024-09-20 22:21:38.578 | NRHandoverAttempt | SourcePCI:514;SourceNR-ARFC... |
| 2024-09-20 22:21:38.613 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.625 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.731 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.731 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224465 | 1 | 6.9973 | 11.9799 | -115.7816 | 15.8252 | 144.7703 | 0.0181 | 0.0139 |
| 2024_09_20 22:00 | 3245787 | 2 | 6.1047 | 18.9307 | -115.3739 | 9.9308 | 88.2943 | 0.0103 | 0.0116 |
| 2024_09_20 22:00 | 3250366 | 3 | 19.5630 | 13.0095 | -114.7854 | 11.4158 | 130.4761 | 0.0133 | 0.0053 |
| 2024_09_20 22:00 | 3251171 | 4 | 13.2148 | 7.6654 | -116.6308 | 12.5285 | 88.2706 | 0.0016 | 0.0164 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415171_71F1BB88 | 504990 | 261 | -89.8 | 504990 | 810 | -92.6 | 504990 | 752 | -98.3 | 504990 | 656 |
| MR_1774415171_35329B84 | 504990 | 261 | -88.5 | 504990 | 810 | -96.0 | 504990 | 752 | -96.7 | 504990 | 656 |
| MR_1774415171_272ED743 | 504990 | 261 | -90.7 | 504990 | 810 | -93.9 | 504990 | 752 | -98.6 | 504990 | 656 |
| MR_1774415171_ADA326E1 | 504990 | 261 | -88.0 | 504990 | 810 | -94.8 | 504990 | 752 | -98.1 | 504990 | 656 |
| MR_1774415171_D3D6C615 | 504990 | 261 | -91.1 | 504990 | 810 | -95.9 | 504990 | 752 | -96.7 | 504990 | 656 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1472: `cadcbc7d-baa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cadcbc7d-baa8-46af-861e-14bbdc441121` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease A3 Offset threshold for 3239345_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1472] topology](images/train_1472.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3235985_4 and 3256377_2
- `C2`: Increase transmission power for 3256377_2
- `C3`: Adjust the azimuth of 3256377_2 by 50 degrees
- `C4`: Decrease transmission power for 3256377_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256377_2
- `C6`: Decrease A3 Offset threshold for 3256377_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239345_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239345_1
- `C9`: Adjust the azimuth of 3239345_1 by 50 degrees
- `C10`: Increase A3 Offset threshold for 3256377_2
- `C11`: Press down the tilt angle  of 3256377_2 by 3 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease transmission power for 3239345_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256377_2
- `C15`: Press down the tilt angle of 3239345_1 by 10 degrees
- `C16`: Decrease A3 Offset threshold for 3239345_1 **← 정답**
- `C17`: Add neighbor relationship between 3239345_1 and 3256377_2
- `C18`: Lift the tilt angle  of 3256377_2 by 3 degrees
- `C19`: Check test server and transmission issues
- `C20`: Increase transmission power for 3239345_1
- `C21`: Lift the tilt angle of 3239345_1 by 10 degrees
- `C22`: Increase A3 Offset threshold for 3239345_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.889 | MS1 | 121.4656673704 | 31.1446279091 | 826 | 504990 | -78.96 | 14.45 | 519.61 | 0.19 | 2.26 | 1569 |
| 2024-09-20 22:21:32.122 | MS1 | 121.4656762248 | 31.1446364283 | 826 | 504990 | -81.04 | 14.45 | 461.96 | 0.18 | 2.59 | 1591 |
| 2024-09-20 22:21:33.757 | MS1 | 121.4656696517 | 31.1446367877 | 826 | 504990 | -77.40 | 12.68 | 574.04 | 0.03 | 2.39 | 1587 |
| 2024-09-20 22:21:34.503 | MS1 | 121.4656632952 | 31.1446269647 | 826 | 504990 | -89.50 | -3.62 | 58.45 | 0.08 | 1.27 | 1577 |
| 2024-09-20 22:21:35.212 | MS1 | 121.4656675386 | 31.1446292772 | 826 | 504990 | -86.83 | -1.58 | 75.05 | 0.02 | 1.03 | 1584 |
| 2024-09-20 22:21:36.796 | MS1 | 121.4656608811 | 31.1446334923 | 826 | 504990 | -86.50 | -0.33 | 58.54 | 0.18 | 1.32 | 1573 |
| 2024-09-20 22:21:37.493 | MS1 | 121.4656665981 | 31.1446298359 | 826 | 504990 | -90.32 | -3.44 | 34.83 | 0.07 | 1.34 | 1590 |
| 2024-09-20 22:21:38.262 | MS1 | 121.4656660360 | 31.1446303661 | 826 | 504990 | -90.63 | -0.94 | 60.87 | 0.07 | 1.44 | 1594 |
| 2024-09-20 22:21:39.213 | MS1 | 121.4656614156 | 31.1446212845 | 325 | 504990 | -80.88 | 13.62 | 237.92 | 0.08 | 1.38 | 1589 |
| 2024-09-20 22:21:40.790 | MS1 | 121.4656754553 | 31.1446196005 | 325 | 504990 | -77.87 | 14.43 | 327.72 | 0.10 | 2.49 | 1581 |
| 2024-09-20 22:21:41.320 | MS1 | 121.4656680911 | 31.1446291928 | 325 | 504990 | -77.75 | 13.51 | 504.21 | 0.03 | 2.39 | 1599 |
| 2024-09-20 22:21:42.804 | MS1 | 121.4656669201 | 31.1446246631 | 325 | 504990 | -77.09 | 15.58 | 580.92 | 0.18 | 2.17 | 1597 |

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
| 3235985 | 4 | 121.4713889727 | 31.1486913348 | 130 | 14 | 5 | 36.9 | TDD | 687 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3239345 | 1 | 121.4641036660 | 31.1539137090 | 108 | 9 | 2 | 40.6 | TDD | 826 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3241409 | 3 | 121.4715625978 | 31.1485675150 | 111 | 5 | 2 | 21.7 | TDD | 237 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3256377 | 2 | 121.4755691321 | 31.1505938060 | 96 | 1 | 2 | 39.2 | TDD | 325 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.953 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.975 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.119 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.119 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.845 | NREventA3 | measId:2;ServCellPCI:182;Se... |
| 2024-09-20 22:21:38.085 | NRHandoverAttempt | SourcePCI:182;SourceNR-ARFC... |
| 2024-09-20 22:21:38.124 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.138 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.239 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.239 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239345 | 1 | 5.8535 | 5.0820 | -117.7457 | 12.5398 | 129.7403 | 0.0094 | 0.1520 |
| 2024_09_20 22:00 | 3256377 | 2 | 9.3151 | 14.4653 | -115.9316 | 8.5231 | 130.2471 | 0.0147 | 0.0020 |
| 2024_09_20 22:00 | 3241409 | 3 | 5.0606 | 19.3545 | -115.8728 | 8.2134 | 86.8234 | 0.0134 | 0.0148 |
| 2024_09_20 22:00 | 3235985 | 4 | 17.0693 | 5.5307 | -117.5611 | 13.5372 | 178.7053 | 0.0139 | 0.0102 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412699_4BB5BD0D | 504990 | 325 | -84.5 | 504990 | 826 | -89.0 | 504990 | 687 | -87.0 | 504990 | 237 |
| MR_1774412699_9B9ABC0E | 504990 | 826 | -88.7 | 504990 | 325 | -84.5 | 504990 | 687 | -86.4 | 504990 | 237 |
| MR_1774412699_BCEDDF94 | 504990 | 826 | -87.9 | 504990 | 325 | -81.9 | 504990 | 687 | -88.2 | 504990 | 237 |
| MR_1774412699_98525867 | 504990 | 826 | -89.3 | 504990 | 325 | -81.7 | 504990 | 687 | -85.5 | 504990 | 237 |
| MR_1774412699_AF54DD38 | 504990 | 826 | -90.6 | 504990 | 325 | -84.7 | 504990 | 687 | -86.1 | 504990 | 237 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1473: `64bc2b02-123...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `64bc2b02-123e-4dbd-8fd2-ba28ee693eda` |
| Tag | **multiple-answer** |
| 정답 | **C6|C10|C14|C21** |
| C6 의미 | Decrease transmission power for 3219300_1 |
| C10 의미 | Press down the tilt angle  of 3219300_1 by 6 degrees |
| C14 의미 | Increase A3 Offset threshold for 3219300_1 |
| C21 의미 | Increase A3 Offset threshold for 3277987_3 |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1473] topology](images/train_1473.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Adjust the azimuth of 3219300_1 by 22 degrees
- `C3`: Lift the tilt angle  of 3219300_1 by 6 degrees
- `C4`: Lift the tilt angle of 3277987_3 by 2 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219300_1
- `C6`: Decrease transmission power for 3219300_1 **← 정답**
- `C7`: Decrease A3 Offset threshold for 3219300_1
- `C8`: Check test server and transmission issues
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277987_3
- `C10`: Press down the tilt angle  of 3219300_1 by 6 degrees **← 정답**
- `C11`: Add neighbor relationship between 3263229_4 and 3219300_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277987_3
- `C13`: Add neighbor relationship between 3277987_3 and 3219300_1
- `C14`: Increase A3 Offset threshold for 3219300_1 **← 정답**
- `C15`: Increase transmission power for 3277987_3
- `C16`: Increase transmission power for 3219300_1
- `C17`: Adjust the azimuth of 3277987_3 by 45 degrees
- `C18`: Press down the tilt angle of 3277987_3 by 2 degrees
- `C19`: Decrease A3 Offset threshold for 3277987_3
- `C20`: Decrease transmission power for 3277987_3
- `C21`: Increase A3 Offset threshold for 3277987_3 **← 정답**
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219300_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.454 | MS1 | 121.4656738420 | 31.1446215499 | 78 | 504990 | -77.46 | 13.97 | 364.00 | 0.07 | 2.89 | 1593 |
| 2024-09-20 22:21:32.707 | MS1 | 121.4656762837 | 31.1446312356 | 78 | 504990 | -83.08 | 15.11 | 446.63 | 0.13 | 2.36 | 1592 |
| 2024-09-20 22:21:33.313 | MS1 | 121.4656674091 | 31.1446308937 | 78 | 504990 | -83.64 | 17.37 | 552.64 | 0.08 | 2.97 | 1560 |
| 2024-09-20 22:21:34.689 | MS1 | 121.4656604785 | 31.1446246775 | 167 | 504990 | -83.31 | 4.48 | 78.58 | 0.09 | 1.07 | 1580 |
| 2024-09-20 22:21:35.793 | MS1 | 121.4656738000 | 31.1446239751 | 167 | 504990 | -81.56 | 2.86 | 66.37 | 0.10 | 1.07 | 1583 |
| 2024-09-20 22:21:36.712 | MS1 | 121.4656745385 | 31.1446361426 | 78 | 504990 | -82.58 | 2.28 | 50.37 | 0.17 | 1.16 | 1598 |
| 2024-09-20 22:21:37.419 | MS1 | 121.4656603752 | 31.1446359715 | 78 | 504990 | -83.63 | 4.16 | 56.42 | 0.09 | 1.01 | 1578 |
| 2024-09-20 22:21:38.425 | MS1 | 121.4656724301 | 31.1446304579 | 167 | 504990 | -82.72 | 1.64 | 26.02 | 0.04 | 1.46 | 1587 |
| 2024-09-20 22:21:39.472 | MS1 | 121.4656709127 | 31.1446252492 | 167 | 504990 | -81.20 | 3.18 | 25.77 | 0.02 | 1.22 | 1561 |
| 2024-09-20 22:21:40.159 | MS1 | 121.4656618768 | 31.1446359289 | 167 | 504990 | -76.30 | 13.11 | 516.03 | 0.10 | 2.70 | 1589 |
| 2024-09-20 22:21:41.213 | MS1 | 121.4656680349 | 31.1446200564 | 167 | 504990 | -81.38 | 14.91 | 438.70 | 0.08 | 2.36 | 1567 |
| 2024-09-20 22:21:42.215 | MS1 | 121.4656675594 | 31.1446362626 | 167 | 504990 | -76.52 | 15.68 | 572.19 | 0.16 | 2.96 | 1562 |

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
| 3219300 | 1 | 121.4715263647 | 31.1483387266 | 211 | 3 | 10 | 33.0 | TDD | 864 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3237755 | 5 | 121.4673636803 | 31.1509340676 | 6 | 8 | 8 | 38.8 | TDD | 446 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3240441 | 2 | 121.4726677798 | 31.1461411715 | 90 | 4 | 7 | 43.1 | TDD | 167 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3263229 | 4 | 121.4692746733 | 31.1479611970 | 252 | 0 | 10 | 23.9 | TDD | 150 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3277987 | 3 | 121.4675592889 | 31.1534882516 | 235 | 1 | 8 | 21.7 | TDD | 78 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.361 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.380 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.526 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.526 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.212 | NREventA3 | measId:2;ServCellPCI:911;Se... |
| 2024-09-20 22:21:34.452 | NRHandoverAttempt | SourcePCI:911;SourceNR-ARFC... |
| 2024-09-20 22:21:34.498 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.513 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.652 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.652 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.212 | NREventA3 | measId:2;ServCellPCI:100;Se... |
| 2024-09-20 22:21:36.452 | NRHandoverAttempt | SourcePCI:100;SourceNR-ARFC... |
| 2024-09-20 22:21:36.498 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.509 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.618 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.618 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.212 | NREventA3 | measId:2;ServCellPCI:911;Se... |
| 2024-09-20 22:21:38.452 | NRHandoverAttempt | SourcePCI:911;SourceNR-ARFC... |
| 2024-09-20 22:21:38.491 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.505 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.616 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.616 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219300 | 1 | 7.1796 | 19.4883 | -116.3877 | 7.8224 | 112.0807 | 0.0025 | 0.0023 |
| 2024_09_20 22:00 | 3240441 | 2 | 14.2283 | 13.9816 | -116.7903 | 9.9211 | 101.1431 | 0.0052 | 0.0167 |
| 2024_09_20 22:00 | 3277987 | 3 | 6.3816 | 7.5257 | -116.0447 | 16.4746 | 87.3710 | 0.0071 | 0.0139 |
| 2024_09_20 22:00 | 3263229 | 4 | 14.5840 | 9.7038 | -114.7661 | 6.6761 | 157.7096 | 0.0088 | 0.0185 |
| 2024_09_20 22:00 | 3237755 | 5 | 9.3948 | 17.2058 | -116.7081 | 8.2398 | 156.5490 | 0.0144 | 0.0032 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415071_5CAD121A | 504990 | 78 | -83.1 | 504990 | 167 | -81.2 | 504990 | 864 | -83.7 | 504990 | 150 |
| MR_1774415071_324355E5 | 504990 | 78 | -82.4 | 504990 | 167 | -82.8 | 504990 | 864 | -82.1 | 504990 | 150 |
| MR_1774415071_C32AE177 | 504990 | 167 | -85.0 | 504990 | 78 | -83.0 | 504990 | 864 | -81.9 | 504990 | 150 |
| MR_1774415071_F9DAA7C3 | 504990 | 78 | -84.1 | 504990 | 167 | -80.7 | 504990 | 864 | -84.3 | 504990 | 150 |
| MR_1774415071_D2DB2347 | 504990 | 167 | -82.2 | 504990 | 78 | -82.4 | 504990 | 864 | -82.4 | 504990 | 150 |
| MR_1774415071_CC9FD93F | 504990 | 167 | -84.7 | 504990 | 78 | -83.2 | 504990 | 864 | -83.7 | 504990 | 150 |
| MR_1774415071_6490F108 | 504990 | 167 | -85.2 | 504990 | 78 | -81.6 | 504990 | 864 | -82.0 | 504990 | 150 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1474: `3b49f521-e11...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3b49f521-e110-447f-8287-0b6b1695037c` |
| Tag | **multiple-answer** |
| 정답 | **C18|C21** |
| C18 의미 | Decrease transmission power for 3255549_4 |
| C21 의미 | Press down the tilt angle  of 3255549_4 by 2 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1474] topology](images/train_1474.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255549_4
- `C2`: Check test server and transmission issues
- `C3`: Increase A3 Offset threshold for 3252395_2
- `C4`: Decrease transmission power for 3252395_2
- `C5`: Increase A3 Offset threshold for 3255549_4
- `C6`: Adjust the azimuth of 3252395_2 by 27 degrees
- `C7`: Add neighbor relationship between 3240967_3 and 3255549_4
- `C8`: Decrease A3 Offset threshold for 3255549_4
- `C9`: Lift the tilt angle of 3252395_2 by 2 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252395_2
- `C11`: Increase transmission power for 3255549_4
- `C12`: Lift the tilt angle  of 3255549_4 by 2 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Press down the tilt angle of 3252395_2 by 2 degrees
- `C15`: Adjust the azimuth of 3255549_4 by 12 degrees
- `C16`: Decrease A3 Offset threshold for 3252395_2
- `C17`: Increase transmission power for 3252395_2
- `C18`: Decrease transmission power for 3255549_4 **← 정답**
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252395_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255549_4
- `C21`: Press down the tilt angle  of 3255549_4 by 2 degrees **← 정답**
- `C22`: Add neighbor relationship between 3252395_2 and 3255549_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.993 | MS1 | 121.4656695442 | 31.1446303299 | 875 | 504990 | -83.18 | 14.92 | 309.88 | 0.15 | 2.03 | 1561 |
| 2024-09-20 22:21:32.612 | MS1 | 121.4656700764 | 31.1446304867 | 875 | 504990 | -78.31 | 12.90 | 373.98 | 0.16 | 2.91 | 1588 |
| 2024-09-20 22:21:33.277 | MS1 | 121.4656583948 | 31.1446241315 | 875 | 504990 | -82.57 | 17.14 | 420.07 | 0.08 | 2.72 | 1567 |
| 2024-09-20 22:21:34.190 | MS1 | 121.4656681956 | 31.1446180749 | 875 | 504990 | -93.81 | 3.82 | 78.76 | 0.04 | 1.49 | 1577 |
| 2024-09-20 22:21:35.222 | MS1 | 121.4656696321 | 31.1446193303 | 875 | 504990 | -92.50 | 2.33 | 44.52 | 0.06 | 1.07 | 1600 |
| 2024-09-20 22:21:36.223 | MS1 | 121.4656733378 | 31.1446276160 | 875 | 504990 | -88.53 | 0.55 | 78.72 | 0.01 | 1.46 | 1584 |
| 2024-09-20 22:21:37.403 | MS1 | 121.4656610419 | 31.1446368063 | 875 | 504990 | -85.12 | 1.26 | 81.13 | 0.14 | 1.49 | 1589 |
| 2024-09-20 22:21:38.578 | MS1 | 121.4656715158 | 31.1446311008 | 875 | 504990 | -94.94 | 2.30 | 52.72 | 0.17 | 1.36 | 1586 |
| 2024-09-20 22:21:39.754 | MS1 | 121.4656700579 | 31.1446309045 | 875 | 504990 | -90.30 | 1.98 | 73.87 | 0.02 | 1.31 | 1580 |
| 2024-09-20 22:21:40.684 | MS1 | 121.4656647524 | 31.1446256709 | 875 | 504990 | -80.66 | 14.37 | 526.49 | 0.06 | 2.23 | 1576 |
| 2024-09-20 22:21:41.626 | MS1 | 121.4656629672 | 31.1446270713 | 875 | 504990 | -78.85 | 17.57 | 445.82 | 0.06 | 2.60 | 1576 |
| 2024-09-20 22:21:42.653 | MS1 | 121.4656744393 | 31.1446368793 | 875 | 504990 | -84.46 | 13.94 | 552.53 | 0.19 | 2.46 | 1584 |

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
| 3240363 | 1 | 121.4679368679 | 31.1543844734 | 50 | 5 | 10 | 36.1 | TDD | 8 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3240967 | 3 | 121.4754491846 | 31.1453452419 | 178 | 3 | 10 | 37.1 | TDD | 909 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3252395 | 2 | 121.4734755873 | 31.1534656546 | 244 | 1 | 0 | 16.8 | TDD | 875 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3255549 | 4 | 121.4681104828 | 31.1474159548 | 229 | 0 | 0 | 15.8 | TDD | 230 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.193 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.211 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.311 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.311 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240363 | 1 | 9.8627 | 19.7781 | -114.8520 | 6.2520 | 107.3167 | 0.0015 | 0.0059 |
| 2024_09_20 22:00 | 3252395 | 2 | 14.7386 | 13.2589 | -108.3204 | 8.6823 | 105.5422 | 0.0054 | 0.0147 |
| 2024_09_20 22:00 | 3240967 | 3 | 15.2991 | 17.2916 | -117.9802 | 15.0802 | 126.4072 | 0.0114 | 0.0131 |
| 2024_09_20 22:00 | 3255549 | 4 | 7.2302 | 14.7018 | -114.9510 | 5.3026 | 131.3912 | 0.0025 | 0.0107 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413064_8CF3C6D6 | 504990 | 875 | -95.7 | 504990 | 230 | -90.1 | 504990 | 909 | -94.2 | 504990 | 8 |
| MR_1774413064_9B64BC2B | 504990 | 875 | -95.6 | 504990 | 230 | -90.2 | 504990 | 909 | -94.3 | 504990 | 8 |
| MR_1774413064_778EBD32 | 504990 | 875 | -95.6 | 504990 | 230 | -89.9 | 504990 | 909 | -94.4 | 504990 | 8 |
| MR_1774413064_316E355D | 504990 | 875 | -92.7 | 504990 | 230 | -91.3 | 504990 | 909 | -94.9 | 504990 | 8 |
| MR_1774413064_67F491B2 | 504990 | 230 | -95.1 | 504990 | 875 | -91.9 | 504990 | 909 | -94.1 | 504990 | 8 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1475: `1bcc7fc7-21d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1bcc7fc7-21d6-4c03-b9da-730e7bd59fae` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1475] topology](images/train_1475.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3226200_2 by 10 degrees
- `C2`: Add neighbor relationship between 3218315_3 and 3234982_4
- `C3`: Lift the tilt angle  of 3234982_4 by 3 degrees
- `C4`: Decrease transmission power for 3234982_4
- `C5`: Adjust the azimuth of 3226200_2 by 21 degrees
- `C6`: Add neighbor relationship between 3226200_2 and 3234982_4
- `C7`: Increase transmission power for 3234982_4
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234982_4
- `C10`: Decrease transmission power for 3226200_2
- `C11`: Press down the tilt angle of 3226200_2 by 10 degrees
- `C12`: Check test server and transmission issues **← 정답**
- `C13`: Increase A3 Offset threshold for 3226200_2
- `C14`: Increase A3 Offset threshold for 3234982_4
- `C15`: Press down the tilt angle  of 3234982_4 by 3 degrees
- `C16`: Decrease A3 Offset threshold for 3234982_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226200_2
- `C18`: Increase transmission power for 3226200_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234982_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226200_2
- `C21`: Decrease A3 Offset threshold for 3226200_2
- `C22`: Adjust the azimuth of 3234982_4 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.845 | MS1 | 121.4656631974 | 31.1446212347 | 298 | 504990 | -88.20 | 12.95 | 310.79 | 0.15 | 2.75 | 1579 |
| 2024-09-20 22:21:32.500 | MS1 | 121.4656738295 | 31.1446324011 | 298 | 504990 | -87.36 | 16.86 | 540.24 | 0.20 | 2.27 | 1591 |
| 2024-09-20 22:21:33.944 | MS1 | 121.4656616516 | 31.1446277676 | 298 | 504990 | -89.85 | 14.01 | 353.21 | 0.13 | 2.91 | 1564 |
| 2024-09-20 22:21:34.904 | MS1 | 121.4656682252 | 31.1446241917 | 298 | 504990 | -89.59 | 13.50 | 71.83 | 0.07 | 2.45 | 479 |
| 2024-09-20 22:21:35.841 | MS1 | 121.4656778347 | 31.1446238695 | 298 | 504990 | -88.20 | 12.92 | 74.37 | 0.13 | 2.48 | 351 |
| 2024-09-20 22:21:36.284 | MS1 | 121.4656622041 | 31.1446238409 | 298 | 504990 | -88.03 | 14.86 | 96.25 | 0.07 | 2.14 | 359 |
| 2024-09-20 22:21:37.105 | MS1 | 121.4656741249 | 31.1446279707 | 298 | 504990 | -90.62 | 8.41 | 92.13 | 0.18 | 2.99 | 477 |
| 2024-09-20 22:21:38.578 | MS1 | 121.4656595500 | 31.1446199097 | 298 | 504990 | -92.88 | 7.22 | 84.29 | 0.00 | 2.93 | 314 |
| 2024-09-20 22:21:39.258 | MS1 | 121.4656703924 | 31.1446211418 | 298 | 504990 | -92.23 | 9.68 | 104.19 | 0.19 | 2.12 | 391 |
| 2024-09-20 22:21:40.404 | MS1 | 121.4656692262 | 31.1446279382 | 298 | 504990 | -90.09 | 8.67 | 509.17 | 0.08 | 2.72 | 1580 |
| 2024-09-20 22:21:41.219 | MS1 | 121.4656675223 | 31.1446299475 | 298 | 504990 | -91.95 | 12.00 | 437.90 | 0.07 | 2.63 | 1560 |
| 2024-09-20 22:21:42.919 | MS1 | 121.4656718417 | 31.1446278281 | 298 | 504990 | -89.21 | 9.53 | 533.24 | 0.01 | 2.34 | 1597 |

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
| 3218315 | 3 | 121.4722256160 | 31.1493813052 | 0 | 10 | 1 | 22.3 | TDD | 988 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3226200 | 2 | 121.4648646441 | 31.1458273988 | 129 | 2 | 4 | 29.3 | TDD | 298 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3234982 | 4 | 121.4693810458 | 31.1467813583 | 90 | 1 | 8 | 18.5 | TDD | 559 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3261073 | 1 | 121.4670172105 | 31.1501667305 | 70 | 15 | 0 | 33.7 | TDD | 8 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.959 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.959 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.629 | NREventA3 | measId:2;ServCellPCI:308;Se... |
| 2024-09-20 22:21:37.869 | NRHandoverAttempt | SourcePCI:308;SourceNR-ARFC... |
| 2024-09-20 22:21:37.907 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.922 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.027 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.027 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261073 | 1 | 14.3890 | 5.5609 | -115.2616 | 7.2362 | 164.7468 | 0.0100 | 0.0080 |
| 2024_09_20 22:00 | 3226200 | 2 | 19.9755 | 19.9082 | -114.5245 | 10.8027 | 116.9231 | 0.0090 | 0.0138 |
| 2024_09_20 22:00 | 3218315 | 3 | 15.3860 | 6.4604 | -117.9498 | 14.7869 | 192.7638 | 0.0061 | 0.0185 |
| 2024_09_20 22:00 | 3234982 | 4 | 15.2804 | 14.2492 | -116.3436 | 8.9647 | 139.9068 | 0.0176 | 0.0191 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413973_464B54FC | 504990 | 298 | -88.5 | 504990 | 559 | -94.7 | 504990 | 988 | -98.2 | 504990 | 8 |
| MR_1774413973_35423789 | 504990 | 298 | -90.3 | 504990 | 559 | -96.7 | 504990 | 988 | -97.6 | 504990 | 8 |
| MR_1774413973_5C7F9635 | 504990 | 298 | -87.9 | 504990 | 559 | -97.6 | 504990 | 988 | -96.4 | 504990 | 8 |
| MR_1774413973_D9F51D5F | 504990 | 298 | -88.6 | 504990 | 559 | -96.0 | 504990 | 988 | -96.7 | 504990 | 8 |
| MR_1774413973_C18FFC1F | 504990 | 298 | -90.6 | 504990 | 559 | -95.4 | 504990 | 988 | -98.3 | 504990 | 8 |
| MR_1774413973_2597872E | 504990 | 298 | -90.1 | 504990 | 559 | -97.5 | 504990 | 988 | -98.2 | 504990 | 8 |
| MR_1774413973_E74CB1F9 | 504990 | 298 | -88.0 | 504990 | 559 | -96.0 | 504990 | 988 | -96.7 | 504990 | 8 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1476: `9458f9f5-c4d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9458f9f5-c4df-4a4c-adab-f68c5fdfc0ca` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease A3 Offset threshold for 3224831_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1476] topology](images/train_1476.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250962_4
- `C2`: Increase transmission power for 3250962_4
- `C3`: Press down the tilt angle  of 3250962_4 by 10 degrees
- `C4`: Lift the tilt angle  of 3250962_4 by 10 degrees
- `C5`: Press down the tilt angle of 3224831_1 by 5 degrees
- `C6`: Add neighbor relationship between 3224831_1 and 3250962_4
- `C7`: Check test server and transmission issues
- `C8`: Decrease transmission power for 3250962_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224831_1
- `C10`: Adjust the azimuth of 3250962_4 by 50 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease A3 Offset threshold for 3250962_4
- `C13`: Decrease A3 Offset threshold for 3224831_1 **← 정답**
- `C14`: Increase transmission power for 3224831_1
- `C15`: Decrease transmission power for 3224831_1
- `C16`: Lift the tilt angle of 3224831_1 by 5 degrees
- `C17`: Adjust the azimuth of 3224831_1 by 34 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250962_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224831_1
- `C20`: Add neighbor relationship between 3259806_2 and 3250962_4
- `C21`: Increase A3 Offset threshold for 3250962_4
- `C22`: Increase A3 Offset threshold for 3224831_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.643 | MS1 | 121.4656686278 | 31.1446264794 | 265 | 504990 | -79.65 | 13.65 | 585.21 | 0.08 | 2.89 | 1575 |
| 2024-09-20 22:21:32.220 | MS1 | 121.4656598598 | 31.1446301047 | 265 | 504990 | -81.64 | 14.20 | 471.36 | 0.04 | 2.97 | 1579 |
| 2024-09-20 22:21:33.774 | MS1 | 121.4656718522 | 31.1446365544 | 265 | 504990 | -81.10 | 14.86 | 304.67 | 0.05 | 2.91 | 1564 |
| 2024-09-20 22:21:34.722 | MS1 | 121.4656717780 | 31.1446254293 | 265 | 504990 | -86.26 | -0.49 | 70.49 | 0.18 | 1.06 | 1570 |
| 2024-09-20 22:21:35.352 | MS1 | 121.4656621042 | 31.1446316860 | 265 | 504990 | -85.71 | -0.26 | 38.98 | 0.12 | 1.12 | 1571 |
| 2024-09-20 22:21:36.817 | MS1 | 121.4656601754 | 31.1446182411 | 265 | 504990 | -84.74 | -3.61 | 57.93 | 0.04 | 1.32 | 1600 |
| 2024-09-20 22:21:37.572 | MS1 | 121.4656628425 | 31.1446271335 | 265 | 504990 | -87.59 | -1.85 | 37.39 | 0.09 | 1.12 | 1571 |
| 2024-09-20 22:21:38.196 | MS1 | 121.4656630377 | 31.1446332509 | 265 | 504990 | -90.30 | -2.48 | 67.86 | 0.11 | 1.18 | 1570 |
| 2024-09-20 22:21:39.924 | MS1 | 121.4656581527 | 31.1446342483 | 295 | 504990 | -80.95 | 17.57 | 285.24 | 0.07 | 1.43 | 1580 |
| 2024-09-20 22:21:40.116 | MS1 | 121.4656679197 | 31.1446375831 | 295 | 504990 | -82.79 | 16.35 | 594.84 | 0.03 | 2.04 | 1587 |
| 2024-09-20 22:21:41.982 | MS1 | 121.4656726692 | 31.1446290086 | 295 | 504990 | -78.09 | 13.72 | 315.51 | 0.16 | 2.73 | 1560 |
| 2024-09-20 22:21:42.507 | MS1 | 121.4656750241 | 31.1446288870 | 295 | 504990 | -82.82 | 15.05 | 363.61 | 0.13 | 2.70 | 1568 |

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
| 3217765 | 3 | 121.4642993898 | 31.1518370373 | 152 | 4 | 1 | 20.7 | TDD | 435 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3224831 | 1 | 121.4730253585 | 31.1485041374 | 204 | 3 | 2 | 28.7 | TDD | 265 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3250962 | 4 | 121.4745442171 | 31.1510353808 | 316 | 12 | 6 | 26.6 | TDD | 295 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3259806 | 2 | 121.4713738439 | 31.1451189366 | 295 | 1 | 11 | 36.4 | TDD | 586 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.146 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.169 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.274 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.274 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.962 | NREventA3 | measId:2;ServCellPCI:695;Se... |
| 2024-09-20 22:21:38.202 | NRHandoverAttempt | SourcePCI:695;SourceNR-ARFC... |
| 2024-09-20 22:21:38.252 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.267 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.406 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.406 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224831 | 1 | 7.6708 | 19.7789 | -115.5749 | 9.2547 | 171.9723 | 0.0191 | 0.1833 |
| 2024_09_20 22:00 | 3259806 | 2 | 17.1102 | 9.1062 | -115.4159 | 16.1525 | 124.1493 | 0.0011 | 0.0164 |
| 2024_09_20 22:00 | 3217765 | 3 | 6.8555 | 8.2055 | -116.7906 | 10.1492 | 193.3440 | 0.0159 | 0.0146 |
| 2024_09_20 22:00 | 3250962 | 4 | 19.6697 | 9.1667 | -115.8599 | 17.4962 | 134.6783 | 0.0107 | 0.0023 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413364_E154067F | 504990 | 295 | -81.2 | 504990 | 265 | -84.5 | 504990 | 586 | -84.9 | 504990 | 435 |
| MR_1774413364_E58B3F83 | 504990 | 265 | -88.0 | 504990 | 295 | -82.9 | 504990 | 586 | -83.9 | 504990 | 435 |
| MR_1774413364_48D0E0D1 | 504990 | 295 | -80.9 | 504990 | 265 | -85.0 | 504990 | 586 | -83.4 | 504990 | 435 |
| MR_1774413364_7760FF97 | 504990 | 265 | -84.9 | 504990 | 295 | -83.9 | 504990 | 586 | -86.3 | 504990 | 435 |
| MR_1774413364_7BEFED55 | 504990 | 265 | -86.2 | 504990 | 295 | -81.7 | 504990 | 586 | -85.5 | 504990 | 435 |
| MR_1774413364_1F24F6DE | 504990 | 295 | -81.1 | 504990 | 265 | -85.9 | 504990 | 586 | -85.2 | 504990 | 435 |
| MR_1774413364_1D3A0BDF | 504990 | 295 | -80.4 | 504990 | 265 | -86.7 | 504990 | 586 | -85.4 | 504990 | 435 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1477: `e7505cce-480...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e7505cce-4804-431f-aa68-0c787a0bfec9` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Lift the tilt angle  of 3220715_3 by 6 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1477] topology](images/train_1477.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3258519_4
- `C2`: Increase transmission power for 3210140_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210140_1
- `C4`: Press down the tilt angle of 3258519_4 by 3 degrees
- `C5`: Adjust the azimuth of 3220715_3 by 50 degrees
- `C6`: Decrease A3 Offset threshold for 3210140_1
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210140_1
- `C9`: Lift the tilt angle of 3258519_4 by 3 degrees
- `C10`: Decrease A3 Offset threshold for 3258519_4
- `C11`: Check test server and transmission issues
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258519_4
- `C13`: Increase transmission power for 3258519_4
- `C14`: Adjust the azimuth of 3258519_4 by 31 degrees
- `C15`: Add neighbor relationship between 3220715_3 and 3210140_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258519_4
- `C17`: Press down the tilt angle  of 3220715_3 by 6 degrees
- `C18`: Decrease transmission power for 3210140_1
- `C19`: Add neighbor relationship between 3258519_4 and 3210140_1
- `C20`: Increase A3 Offset threshold for 3210140_1
- `C21`: Lift the tilt angle  of 3220715_3 by 6 degrees **← 정답**
- `C22`: Decrease transmission power for 3258519_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.835 | MS1 | 121.4656668025 | 31.1446296336 | 975 | 504990 | -88.44 | 17.71 | 555.46 | 0.05 | 2.36 | 1595 |
| 2024-09-20 22:21:32.617 | MS1 | 121.4656756779 | 31.1446202423 | 975 | 504990 | -91.48 | 14.10 | 303.72 | 0.01 | 2.78 | 1600 |
| 2024-09-20 22:21:33.153 | MS1 | 121.4656680450 | 31.1446276541 | 975 | 504990 | -88.57 | 17.66 | 526.35 | 0.13 | 2.03 | 1593 |
| 2024-09-20 22:21:34.214 | MS1 | 121.4656716058 | 31.1446248854 | 975 | 504990 | -86.52 | 13.25 | 77.13 | 0.10 | 2.76 | 1582 |
| 2024-09-20 22:21:35.407 | MS1 | 121.4656770045 | 31.1446187296 | 975 | 504990 | -85.49 | 17.66 | 54.50 | 0.03 | 2.89 | 1581 |
| 2024-09-20 22:21:36.920 | MS1 | 121.4656670699 | 31.1446196806 | 975 | 504990 | -90.54 | 15.02 | 51.11 | 0.19 | 2.58 | 1589 |
| 2024-09-20 22:21:37.259 | MS1 | 121.4656705011 | 31.1446183810 | 975 | 504990 | -93.68 | 10.77 | 83.97 | 0.06 | 2.89 | 1574 |
| 2024-09-20 22:21:38.771 | MS1 | 121.4656741584 | 31.1446349349 | 975 | 504990 | -91.45 | 10.45 | 70.60 | 0.11 | 2.53 | 1591 |
| 2024-09-20 22:21:39.552 | MS1 | 121.4656597740 | 31.1446278749 | 975 | 504990 | -93.90 | 10.49 | 77.67 | 0.11 | 2.46 | 1585 |
| 2024-09-20 22:21:40.748 | MS1 | 121.4656653685 | 31.1446184548 | 975 | 504990 | -90.34 | 9.83 | 571.53 | 0.05 | 2.31 | 1588 |
| 2024-09-20 22:21:41.885 | MS1 | 121.4656638977 | 31.1446194065 | 975 | 504990 | -91.45 | 13.00 | 398.63 | 0.02 | 2.23 | 1576 |
| 2024-09-20 22:21:42.470 | MS1 | 121.4656598529 | 31.1446289081 | 975 | 504990 | -90.88 | 11.81 | 502.72 | 0.09 | 2.94 | 1572 |

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
| 3210140 | 1 | 121.4748950872 | 31.1539183234 | 149 | 5 | 11 | 15.7 | TDD | 792 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3220381 | 2 | 121.4645669554 | 31.1485627414 | 306 | 15 | 9 | 17.7 | TDD | 528 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3220715 | 3 | 121.4690640823 | 31.1467141671 | 156 | 8 | 2 | 28.7 | TDD | 285 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3258519 | 4 | 121.4751440473 | 31.1506036876 | 265 | 2 | 12 | 20.3 | TDD | 975 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.338 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.482 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.482 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.171 | NREventA3 | measId:2;ServCellPCI:283;Se... |
| 2024-09-20 22:21:38.411 | NRHandoverAttempt | SourcePCI:283;SourceNR-ARFC... |
| 2024-09-20 22:21:38.452 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.465 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.590 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.590 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210140 | 1 | 8.4119 | 19.7085 | -117.2609 | 19.2689 | 182.1803 | 0.0161 | 0.0044 |
| 2024_09_20 22:00 | 3220381 | 2 | 17.0188 | 15.7446 | -114.3229 | 6.3292 | 178.8041 | 0.0018 | 0.0165 |
| 2024_09_20 22:00 | 3220715 | 3 | 14.2922 | 17.1205 | -116.5617 | 16.6304 | 161.0619 | 0.0022 | 0.0138 |
| 2024_09_20 22:00 | 3258519 | 4 | 88.7602 | 77.4712 | -117.8591 | 8.5668 | 120.1777 | 0.0031 | 0.0135 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415766_1712395F | 504990 | 975 | -84.6 | 504990 | 792 | -90.0 | 504990 | 285 | -99.6 | 504990 | 528 |
| MR_1774415766_7C129789 | 504990 | 975 | -85.6 | 504990 | 792 | -88.8 | 504990 | 285 | -99.8 | 504990 | 528 |
| MR_1774415766_7B173E32 | 504990 | 975 | -87.7 | 504990 | 792 | -91.4 | 504990 | 285 | -97.2 | 504990 | 528 |
| MR_1774415766_5446053E | 504990 | 975 | -88.2 | 504990 | 792 | -90.8 | 504990 | 285 | -98.0 | 504990 | 528 |
| MR_1774415766_FE3382D0 | 504990 | 975 | -86.6 | 504990 | 792 | -89.4 | 504990 | 285 | -100.3 | 504990 | 528 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1478: `ef1e3a6d-edb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ef1e3a6d-edb5-4089-a48a-60bc09b3e780` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease A3 Offset threshold for 3270883_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1478] topology](images/train_1478.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3270883_3
- `C2`: Check test server and transmission issues
- `C3`: Decrease transmission power for 3270883_3
- `C4`: Add neighbor relationship between 3276142_2 and 3266692_4
- `C5`: Decrease transmission power for 3266692_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270883_3
- `C7`: Lift the tilt angle of 3270883_3 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3266692_4
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Press down the tilt angle  of 3266692_4 by 8 degrees
- `C11`: Add neighbor relationship between 3270883_3 and 3266692_4
- `C12`: Decrease A3 Offset threshold for 3270883_3 **← 정답**
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270883_3
- `C14`: Adjust the azimuth of 3266692_4 by 50 degrees
- `C15`: Press down the tilt angle of 3270883_3 by 10 degrees
- `C16`: Adjust the azimuth of 3270883_3 by 50 degrees
- `C17`: Increase transmission power for 3270883_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266692_4
- `C19`: Increase transmission power for 3266692_4
- `C20`: Increase A3 Offset threshold for 3266692_4
- `C21`: Lift the tilt angle  of 3266692_4 by 8 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266692_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.119 | MS1 | 121.4656634766 | 31.1446364253 | 572 | 504990 | -77.95 | 14.30 | 404.46 | 0.02 | 2.70 | 1582 |
| 2024-09-20 22:21:32.747 | MS1 | 121.4656631341 | 31.1446340233 | 572 | 504990 | -80.24 | 13.19 | 517.89 | 0.01 | 2.62 | 1569 |
| 2024-09-20 22:21:33.876 | MS1 | 121.4656580313 | 31.1446264673 | 572 | 504990 | -82.37 | 16.12 | 488.90 | 0.06 | 2.63 | 1569 |
| 2024-09-20 22:21:34.322 | MS1 | 121.4656777755 | 31.1446292771 | 572 | 504990 | -87.83 | -0.73 | 60.74 | 0.16 | 1.14 | 1581 |
| 2024-09-20 22:21:35.431 | MS1 | 121.4656764663 | 31.1446281628 | 572 | 504990 | -90.06 | -1.16 | 24.41 | 0.13 | 1.22 | 1561 |
| 2024-09-20 22:21:36.907 | MS1 | 121.4656618691 | 31.1446351023 | 572 | 504990 | -89.61 | -0.95 | 41.01 | 0.08 | 1.10 | 1564 |
| 2024-09-20 22:21:37.765 | MS1 | 121.4656710777 | 31.1446310459 | 572 | 504990 | -84.07 | -1.90 | 57.56 | 0.19 | 1.22 | 1578 |
| 2024-09-20 22:21:38.690 | MS1 | 121.4656740733 | 31.1446252422 | 572 | 504990 | -86.64 | -3.98 | 38.49 | 0.05 | 1.38 | 1572 |
| 2024-09-20 22:21:39.689 | MS1 | 121.4656628020 | 31.1446253011 | 183 | 504990 | -78.14 | 16.10 | 291.80 | 0.05 | 1.03 | 1585 |
| 2024-09-20 22:21:40.931 | MS1 | 121.4656638485 | 31.1446200387 | 183 | 504990 | -77.06 | 17.67 | 576.82 | 0.14 | 2.95 | 1573 |
| 2024-09-20 22:21:41.981 | MS1 | 121.4656757583 | 31.1446375449 | 183 | 504990 | -79.86 | 16.62 | 454.24 | 0.06 | 2.13 | 1591 |
| 2024-09-20 22:21:42.798 | MS1 | 121.4656747096 | 31.1446204585 | 183 | 504990 | -84.51 | 14.54 | 513.36 | 0.12 | 2.90 | 1571 |

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
| 3263277 | 1 | 121.4644222196 | 31.1441564018 | 150 | 0 | 4 | 37.1 | TDD | 894 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3266692 | 4 | 121.4653516142 | 31.1537463450 | 22 | 5 | 3 | 47.6 | TDD | 183 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3270883 | 3 | 121.4663913075 | 31.1484186767 | 115 | 13 | 2 | 19.2 | TDD | 572 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3276142 | 2 | 121.4753656912 | 31.1451554949 | 195 | 15 | 3 | 16.8 | TDD | 412 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.231 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.246 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.378 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.378 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.043 | NREventA3 | measId:2;ServCellPCI:30;Ser... |
| 2024-09-20 22:21:38.283 | NRHandoverAttempt | SourcePCI:30;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.332 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.343 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.478 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.478 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263277 | 1 | 15.9471 | 13.3380 | -114.9958 | 8.9077 | 108.8258 | 0.0101 | 0.0168 |
| 2024_09_20 22:00 | 3276142 | 2 | 9.8749 | 17.7077 | -115.3209 | 15.1514 | 156.2882 | 0.0146 | 0.0096 |
| 2024_09_20 22:00 | 3270883 | 3 | 15.8058 | 18.9157 | -114.7960 | 11.2233 | 173.3499 | 0.0111 | 0.1353 |
| 2024_09_20 22:00 | 3266692 | 4 | 5.0319 | 8.8240 | -115.7767 | 13.4815 | 128.7885 | 0.0012 | 0.0168 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413518_CC36D033 | 504990 | 572 | -87.1 | 504990 | 183 | -84.6 | 504990 | 412 | -85.8 | 504990 | 894 |
| MR_1774413518_CF32399B | 504990 | 572 | -87.7 | 504990 | 183 | -81.9 | 504990 | 412 | -84.6 | 504990 | 894 |
| MR_1774413518_B4BF4DFB | 504990 | 572 | -87.6 | 504990 | 183 | -82.6 | 504990 | 412 | -86.3 | 504990 | 894 |
| MR_1774413518_47462DF6 | 504990 | 572 | -89.6 | 504990 | 183 | -84.9 | 504990 | 412 | -85.0 | 504990 | 894 |
| MR_1774413518_85FA8BD4 | 504990 | 572 | -87.0 | 504990 | 183 | -84.2 | 504990 | 412 | -83.4 | 504990 | 894 |
| MR_1774413518_7F2B1C25 | 504990 | 572 | -86.6 | 504990 | 183 | -83.3 | 504990 | 412 | -84.3 | 504990 | 894 |
| MR_1774413518_406D3988 | 504990 | 183 | -82.6 | 504990 | 572 | -86.4 | 504990 | 412 | -83.3 | 504990 | 894 |
| MR_1774413518_C9A09A55 | 504990 | 572 | -88.3 | 504990 | 183 | -82.6 | 504990 | 412 | -84.4 | 504990 | 894 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1479: `5b5dc2f1-718...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5b5dc2f1-7189-418e-96f6-f78a6d234583` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3212656_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1479] topology](images/train_1479.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3272082_3 by 10 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212656_1
- `C3`: Decrease A3 Offset threshold for 3212656_1
- `C4`: Add neighbor relationship between 3212656_1 and 3272082_3
- `C5`: Decrease transmission power for 3272082_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272082_3
- `C7`: Increase transmission power for 3272082_3
- `C8`: Decrease transmission power for 3212656_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272082_3
- `C10`: Lift the tilt angle of 3212656_1 by 4 degrees
- `C11`: Increase A3 Offset threshold for 3272082_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212656_1 **← 정답**
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Increase transmission power for 3212656_1
- `C15`: Check test server and transmission issues
- `C16`: Press down the tilt angle of 3212656_1 by 4 degrees
- `C17`: Adjust the azimuth of 3272082_3 by 48 degrees
- `C18`: Lift the tilt angle  of 3272082_3 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3212656_1
- `C20`: Adjust the azimuth of 3212656_1 by 27 degrees
- `C21`: Decrease A3 Offset threshold for 3272082_3
- `C22`: Add neighbor relationship between 3253422_4 and 3272082_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.769 | MS1 | 121.4656702378 | 31.1446329925 | 312 | 504990 | -91.99 | 15.73 | 572.12 | 0.06 | 2.67 | 1588 |
| 2024-09-20 22:21:32.752 | MS1 | 121.4656669444 | 31.1446194799 | 312 | 504990 | -88.77 | 13.08 | 501.59 | 0.12 | 2.52 | 1599 |
| 2024-09-20 22:21:33.687 | MS1 | 121.4656732218 | 31.1446300897 | 312 | 504990 | -87.73 | 17.25 | 304.15 | 0.18 | 2.62 | 1565 |
| 2024-09-20 22:21:34.400 | MS1 | 121.4656775264 | 31.1446313653 | 312 | 504990 | -90.62 | 12.18 | 78.07 | 0.68 | 2.12 | 551 |
| 2024-09-20 22:21:35.516 | MS1 | 121.4656712167 | 31.1446337416 | 312 | 504990 | -91.11 | 14.96 | 61.34 | 0.64 | 2.26 | 603 |
| 2024-09-20 22:21:36.472 | MS1 | 121.4656590216 | 31.1446256624 | 312 | 504990 | -87.38 | 12.70 | 81.75 | 0.59 | 2.48 | 615 |
| 2024-09-20 22:21:37.888 | MS1 | 121.4656769273 | 31.1446187834 | 312 | 504990 | -90.67 | 12.82 | 95.14 | 0.53 | 2.65 | 626 |
| 2024-09-20 22:21:38.266 | MS1 | 121.4656732400 | 31.1446293937 | 312 | 504990 | -92.00 | 12.17 | 51.14 | 0.67 | 2.65 | 666 |
| 2024-09-20 22:21:39.589 | MS1 | 121.4656702425 | 31.1446326707 | 312 | 504990 | -90.99 | 8.30 | 75.18 | 0.57 | 2.67 | 699 |
| 2024-09-20 22:21:40.226 | MS1 | 121.4656770123 | 31.1446203085 | 312 | 504990 | -89.70 | 11.49 | 337.30 | 0.06 | 2.05 | 1595 |
| 2024-09-20 22:21:41.120 | MS1 | 121.4656619176 | 31.1446239316 | 312 | 504990 | -93.51 | 9.88 | 393.87 | 0.12 | 2.39 | 1577 |
| 2024-09-20 22:21:42.304 | MS1 | 121.4656705001 | 31.1446354795 | 312 | 504990 | -90.28 | 10.43 | 463.47 | 0.08 | 2.15 | 1575 |

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
| 3212656 | 1 | 121.4717407464 | 31.1559584822 | 178 | 2 | 2 | 39.9 | TDD | 312 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3228373 | 2 | 121.4721526174 | 31.1534073905 | 354 | 3 | 11 | 37.2 | TDD | 986 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3253422 | 4 | 121.4697539397 | 31.1524444827 | 275 | 9 | 7 | 19.7 | TDD | 462 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3272082 | 3 | 121.4697112586 | 31.1466371239 | 288 | 15 | 12 | 28.0 | TDD | 878 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.437 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.457 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.593 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.593 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.297 | NREventA3 | measId:2;ServCellPCI:49;Ser... |
| 2024-09-20 22:21:38.537 | NRHandoverAttempt | SourcePCI:49;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.577 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.587 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.725 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.725 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212656 | 1 | 12.7265 | 11.3920 | -115.0439 | 18.7687 | 94.9991 | 0.0148 | 0.0181 |
| 2024_09_20 22:00 | 3228373 | 2 | 5.0743 | 9.6611 | -116.4173 | 8.2535 | 189.3190 | 0.0016 | 0.0028 |
| 2024_09_20 22:00 | 3272082 | 3 | 15.6232 | 5.7732 | -114.3354 | 5.8240 | 82.6711 | 0.0003 | 0.0034 |
| 2024_09_20 22:00 | 3253422 | 4 | 13.2975 | 10.7830 | -117.2862 | 15.4147 | 144.8763 | 0.0048 | 0.0079 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413907_0B446A3B | 504990 | 312 | -92.3 | 504990 | 878 | -96.1 | 504990 | 462 | -99.3 | 504990 | 986 |
| MR_1774413907_94F8872E | 504990 | 312 | -89.9 | 504990 | 878 | -95.3 | 504990 | 462 | -101.4 | 504990 | 986 |
| MR_1774413907_F9391249 | 504990 | 312 | -91.0 | 504990 | 878 | -92.8 | 504990 | 462 | -102.1 | 504990 | 986 |
| MR_1774413907_21A1AA76 | 504990 | 312 | -88.8 | 504990 | 878 | -95.0 | 504990 | 462 | -99.1 | 504990 | 986 |
| MR_1774413907_4797CE44 | 504990 | 312 | -89.3 | 504990 | 878 | -94.2 | 504990 | 462 | -101.0 | 504990 | 986 |
| MR_1774413907_FB1AA76E | 504990 | 312 | -91.1 | 504990 | 878 | -96.0 | 504990 | 462 | -99.3 | 504990 | 986 |
| MR_1774413907_B50EB782 | 504990 | 312 | -89.5 | 504990 | 878 | -96.3 | 504990 | 462 | -101.7 | 504990 | 986 |

> *... 2개 열 생략 (전체 14열)*

---
