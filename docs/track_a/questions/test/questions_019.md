# Track A 문제 분석 — test[180]~test[189]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[180] ~ test[189] (10개)

## 목차

1. [문제 180: `ddb980fe-bf9...`](#180) — single-answer
2. [문제 181: `ead37073-edf...`](#181) — single-answer
3. [문제 182: `951b9766-909...`](#182) — single-answer
4. [문제 183: `c3c50ed6-25e...`](#183) — single-answer
5. [문제 184: `11ef6de0-a0b...`](#184) — single-answer
6. [문제 185: `21d519a0-d46...`](#185) — single-answer
7. [문제 186: `9194a6b3-99e...`](#186) — single-answer
8. [문제 187: `1d55d74e-bd5...`](#187) — single-answer
9. [문제 188: `cec59a76-39f...`](#188) — single-answer
10. [문제 189: `52731b2a-aa5...`](#189) — single-answer

---

### 문제 180: `ddb980fe-bf9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ddb980fe-bf9f-4bed-b6c1-8acee32b02a0` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[180] topology](images/test_0180.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3241197_2
- `C2`: Add neighbor relationship between 3241497_3 and 3239845_1
- `C3`: Press down the tilt angle of 3241197_2 by 10 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239845_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239845_1
- `C6`: Increase transmission power for 3241197_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241197_2
- `C8`: Decrease A3 Offset threshold for 3239845_1
- `C9`: Decrease transmission power for 3239845_1
- `C10`: Add neighbor relationship between 3241197_2 and 3239845_1
- `C11`: Increase A3 Offset threshold for 3239845_1
- `C12`: Press down the tilt angle  of 3239845_1 by 10 degrees
- `C13`: Decrease transmission power for 3241197_2
- `C14`: Lift the tilt angle of 3241197_2 by 10 degrees
- `C15`: Increase transmission power for 3239845_1
- `C16`: Lift the tilt angle  of 3239845_1 by 10 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Adjust the azimuth of 3241197_2 by 50 degrees
- `C19`: Check test server and transmission issues
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241197_2
- `C21`: Decrease A3 Offset threshold for 3241197_2
- `C22`: Adjust the azimuth of 3239845_1 by 46 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.510 | MS1 | 121.4656778900 | 31.1446208560 | 410 | 504990 | -87.36 | 13.79 | 350.42 | 0.06 | 2.26 | 1600 |
| 2024-09-20 22:21:32.566 | MS1 | 121.4656620486 | 31.1446212995 | 410 | 504990 | -91.87 | 16.58 | 581.55 | 0.04 | 2.10 | 1561 |
| 2024-09-20 22:21:33.263 | MS1 | 121.4656768491 | 31.1446373523 | 410 | 504990 | -86.80 | 13.38 | 553.62 | 0.11 | 2.29 | 1573 |
| 2024-09-20 22:21:34.582 | MS1 | 121.4656589427 | 31.1446251485 | 410 | 504990 | -89.06 | 12.57 | 78.82 | 0.05 | 2.74 | 1560 |
| 2024-09-20 22:21:35.259 | MS1 | 121.4656718392 | 31.1446224249 | 410 | 504990 | -87.71 | 17.82 | 81.47 | 0.11 | 2.90 | 1579 |
| 2024-09-20 22:21:36.388 | MS1 | 121.4656638313 | 31.1446188731 | 410 | 504990 | -91.84 | 17.26 | 88.54 | 0.19 | 2.14 | 1561 |
| 2024-09-20 22:21:37.422 | MS1 | 121.4656778188 | 31.1446250307 | 410 | 504990 | -89.15 | 7.81 | 79.17 | 0.12 | 2.50 | 1573 |
| 2024-09-20 22:21:38.378 | MS1 | 121.4656708408 | 31.1446219194 | 410 | 504990 | -90.99 | 12.87 | 62.08 | 0.16 | 2.11 | 1581 |
| 2024-09-20 22:21:39.797 | MS1 | 121.4656732431 | 31.1446265849 | 410 | 504990 | -93.53 | 9.73 | 93.11 | 0.07 | 2.38 | 1578 |
| 2024-09-20 22:21:40.320 | MS1 | 121.4656727610 | 31.1446358446 | 410 | 504990 | -93.20 | 10.44 | 323.86 | 0.20 | 2.60 | 1596 |
| 2024-09-20 22:21:41.562 | MS1 | 121.4656658548 | 31.1446334863 | 410 | 504990 | -89.35 | 7.59 | 310.93 | 0.19 | 2.86 | 1561 |
| 2024-09-20 22:21:42.560 | MS1 | 121.4656616328 | 31.1446204728 | 410 | 504990 | -93.01 | 9.48 | 411.23 | 0.10 | 2.77 | 1597 |

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
| 3217767 | 4 | 121.4733508073 | 31.1543800697 | 154 | 1 | 12 | 40.4 | TDD | 94 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3239845 | 1 | 121.4702933302 | 31.1459145800 | 206 | 14 | 2 | 42.9 | TDD | 808 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3241197 | 2 | 121.4683647666 | 31.1449420240 | 313 | 14 | 11 | 39.7 | TDD | 410 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3241497 | 3 | 121.4656773597 | 31.1446660250 | 19 | 8 | 9 | 43.4 | TDD | 332 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.832 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.857 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.981 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.981 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.644 | NREventA3 | measId:2;ServCellPCI:28;Ser... |
| 2024-09-20 22:21:37.884 | NRHandoverAttempt | SourcePCI:28;SourceNR-ARFCN... |
| 2024-09-20 22:21:37.934 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.944 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.055 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.055 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3239845 | 1 | 75.8790 | 77.8040 | -117.3300 | 12.9907 | 198.2899 | 0.0135 | 0.0060 |
| 2024_09_19 22:00 | 3241197 | 2 | 87.8624 | 86.4644 | -117.2370 | 16.2745 | 130.1300 | 0.0106 | 0.0005 |
| 2024_09_19 22:00 | 3241497 | 3 | 81.5400 | 93.2975 | -117.0970 | 15.6052 | 184.1392 | 0.0046 | 0.0046 |
| 2024_09_19 22:00 | 3217767 | 4 | 93.6510 | 76.3021 | -114.8758 | 11.2434 | 179.8694 | 0.0004 | 0.0035 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417190_F5563986 | 504990 | 410 | -90.3 | 504990 | 808 | -91.5 | 504990 | 332 | -99.0 | 504990 | 94 |
| MR_1774417190_5932009E | 504990 | 410 | -88.9 | 504990 | 808 | -94.1 | 504990 | 332 | -99.3 | 504990 | 94 |
| MR_1774417190_0C1D2ECD | 504990 | 410 | -88.7 | 504990 | 808 | -90.9 | 504990 | 332 | -99.7 | 504990 | 94 |
| MR_1774417190_9FF93E2E | 504990 | 410 | -90.0 | 504990 | 808 | -90.6 | 504990 | 332 | -102.1 | 504990 | 94 |
| MR_1774417190_4AA35AED | 504990 | 410 | -90.2 | 504990 | 808 | -91.8 | 504990 | 332 | -100.3 | 504990 | 94 |
| MR_1774417190_8657DD36 | 504990 | 410 | -89.4 | 504990 | 808 | -93.2 | 504990 | 332 | -101.4 | 504990 | 94 |
| MR_1774417190_09C160F6 | 504990 | 410 | -90.1 | 504990 | 808 | -92.2 | 504990 | 332 | -102.6 | 504990 | 94 |
| MR_1774417190_F45C0574 | 504990 | 410 | -90.9 | 504990 | 808 | -92.7 | 504990 | 332 | -102.7 | 504990 | 94 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 181: `ead37073-edf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ead37073-edfa-48c8-8689-69022c35be38` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[181] topology](images/test_0181.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3273155_6
- `C2`: Increase transmission power for 3273155_6
- `C3`: Increase A3 Offset threshold for 3250858_4
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease transmission power for 3273155_6
- `C6`: Lift the tilt angle  of 3273155_6 by 5 degrees
- `C7`: Decrease A3 Offset threshold for 3273155_6
- `C8`: Press down the tilt angle of 3250858_4 by 1 degrees
- `C9`: Adjust the azimuth of 3250858_4 by 44 degrees
- `C10`: Decrease transmission power for 3250858_4
- `C11`: Increase transmission power for 3250858_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250858_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250858_4
- `C14`: Decrease A3 Offset threshold for 3250858_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273155_6
- `C16`: Lift the tilt angle of 3250858_4 by 1 degrees
- `C17`: Press down the tilt angle  of 3273155_6 by 5 degrees
- `C18`: Check test server and transmission issues
- `C19`: Adjust the azimuth of 3273155_6 by 2 degrees
- `C20`: Add neighbor relationship between 3228644_11 and 3273155_6
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273155_6
- `C22`: Add neighbor relationship between 3250858_4 and 3273155_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.970 | MS1 | 121.4656606694 | 31.1446231775 | 566 | 504990 | -94.62 | 13.40 | 366.00 | 0.03 | 2.07 | 1600 |
| 2024-09-20 22:21:32.823 | MS1 | 121.4656653413 | 31.1446201319 | 573 | 504990 | -94.79 | 12.61 | 467.86 | 0.01 | 2.53 | 1585 |
| 2024-09-20 22:21:33.988 | MS1 | 121.4656604311 | 31.1446228769 | 71 | 504990 | -95.73 | 10.93 | 323.08 | 0.02 | 2.27 | 1574 |
| 2024-09-20 22:21:34.860 | MS1 | 121.4656696298 | 31.1446244161 | 585 | 152650 | -89.76 | 2.67 | 60.71 | 0.14 | 1.69 | 954 |
| 2024-09-20 22:21:35.385 | MS1 | 121.4656591834 | 31.1446211172 | 33 | 152650 | -92.16 | 7.53 | 73.49 | 0.04 | 1.87 | 994 |
| 2024-09-20 22:21:36.271 | MS1 | 121.4656644587 | 31.1446259691 | 476 | 152650 | -92.35 | 6.06 | 97.17 | 0.02 | 1.96 | 913 |
| 2024-09-20 22:21:37.425 | MS1 | 121.4656755896 | 31.1446239024 | 831 | 152650 | -87.98 | 7.62 | 55.04 | 0.15 | 1.53 | 990 |
| 2024-09-20 22:21:38.878 | MS1 | 121.4656643300 | 31.1446354635 | 585 | 152650 | -93.39 | 6.79 | 82.74 | 0.18 | 1.51 | 928 |
| 2024-09-20 22:21:39.980 | MS1 | 121.4656714743 | 31.1446290486 | 33 | 152650 | -87.17 | 6.92 | 67.22 | 0.10 | 1.75 | 942 |
| 2024-09-20 22:21:40.634 | MS1 | 121.4656717904 | 31.1446240979 | 476 | 152650 | -93.04 | 4.96 | 67.80 | 0.17 | 2.14 | 1600 |
| 2024-09-20 22:21:41.756 | MS1 | 121.4656587360 | 31.1446299581 | 831 | 152650 | -91.83 | 7.56 | 56.74 | 0.04 | 2.77 | 1593 |
| 2024-09-20 22:21:42.396 | MS1 | 121.4656750863 | 31.1446215512 | 585 | 152650 | -87.82 | 5.44 | 68.53 | 0.01 | 2.65 | 1579 |

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
| 3217845 | 12 | 121.4645536593 | 31.1546827524 | 8 | 3 | 5 | 6.7 | FDD | 542 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3219654 | 7 | 121.4647527192 | 31.1515057134 | 266 | 6 | 8 | 17.0 | FDD | 33 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3227627 | 9 | 121.4709744323 | 31.1533777376 | 14 | 3 | 2 | 4.5 | FDD | 585 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3228644 | 11 | 121.4730168181 | 31.1448858071 | 73 | 6 | 1 | 8.1 | FDD | 476 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3232576 | 8 | 121.4746002116 | 31.1521145497 | 150 | 6 | 8 | 15.1 | FDD | 803 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3240297 | 13 | 121.4653132239 | 31.1464797877 | 289 | 9 | 11 | 1.0 | FDD | 831 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3241420 | 2 | 121.4755814936 | 31.1493636079 | 50 | 12 | 8 | 16.0 | TDD | 516 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3250858 | 4 | 121.4741830282 | 31.1559120778 | 169 | 1 | 8 | 0.8 | TDD | 566 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3253973 | 5 | 121.4749230229 | 31.1509005667 | 247 | 10 | 6 | 10.7 | TDD | 573 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3257617 | 1 | 121.4753491919 | 31.1510602279 | 5 | 12 | 2 | 9.6 | TDD | 676 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3265437 | 10 | 121.4749716530 | 31.1494102460 | 286 | 2 | 8 | 6.8 | FDD | 309 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3267697 | 3 | 121.4756547736 | 31.1461553532 | 330 | 5 | 7 | 14.9 | TDD | 71 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3273155 | 6 | 121.4645384637 | 31.1495768686 | 171 | 4 | 1 | 12.9 | TDD | 287 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.743 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.764 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.879 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.879 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.617 | NREventA2 | measId:1;ServCellPCI:335;Se... |
| 2024-09-20 22:21:34.741 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:34.957 | NREventA5 | measId:3;ServCellPCI:335;Se... |
| 2024-09-20 22:21:35.033 | NRHandoverAttempt | SourcePCI:335;SourceNR-ARFC... |
| 2024-09-20 22:21:35.073 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.085 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.228 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.228 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257617 | 1 | 5.6646 | 16.4541 | -116.3449 | 9.9164 | 123.4234 | 0.0071 | 0.0084 |
| 2024_09_20 22:00 | 3241420 | 2 | 9.0672 | 8.2283 | -115.2966 | 8.7094 | 101.6318 | 0.0015 | 0.0191 |
| 2024_09_20 22:00 | 3267697 | 3 | 18.4862 | 8.9856 | -117.6102 | 16.7795 | 160.1903 | 0.0088 | 0.0068 |
| 2024_09_20 22:00 | 3250858 | 4 | 9.5514 | 17.6470 | -114.9587 | 9.4584 | 134.3006 | 0.0057 | 0.0025 |
| 2024_09_20 22:00 | 3253973 | 5 | 13.5297 | 13.3582 | -115.2333 | 19.0721 | 96.2300 | 0.0176 | 0.0060 |
| 2024_09_20 22:00 | 3273155 | 6 | 18.0325 | 16.2096 | -116.6475 | 10.0128 | 180.9016 | 0.0028 | 0.0141 |
| 2024_09_20 22:00 | 3219654 | 7 | 6.6895 | 19.0389 | -117.1909 | 4.7883 | 32.3877 | 0.0179 | 0.0114 |
| 2024_09_20 22:00 | 3232576 | 8 | 13.1209 | 17.2708 | -117.3739 | 4.9495 | 21.4693 | 0.0147 | 0.0060 |
| 2024_09_20 22:00 | 3227627 | 9 | 5.3370 | 13.8972 | -114.9153 | 4.9486 | 33.8036 | 0.0170 | 0.0085 |
| 2024_09_20 22:00 | 3265437 | 10 | 9.5435 | 6.2146 | -114.9622 | 3.6940 | 24.5254 | 0.0185 | 0.0149 |
| 2024_09_20 22:00 | 3228644 | 11 | 10.0395 | 18.5087 | -114.8402 | 3.7754 | 38.7750 | 0.0075 | 0.0138 |
| 2024_09_20 22:00 | 3217845 | 12 | 7.2416 | 8.5157 | -117.6166 | 3.2582 | 56.0172 | 0.0030 | 0.0066 |
| 2024_09_20 22:00 | 3240297 | 13 | 6.3378 | 18.1973 | -114.3676 | 4.0851 | 36.0036 | 0.0122 | 0.0150 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412996_3364A98E | 152650 | 585 | -87.9 | 152650 | 803 | -96.5 | 152650 | 542 | -97.0 | 152650 | 309 |
| MR_1774412996_8A6B28C8 | 504990 | 71 | -95.2 | 504990 | 287 | -95.8 | 504990 | 676 | -98.5 | 504990 | 516 |
| MR_1774412996_339A4E7D | 152650 | 585 | -90.1 | 152650 | 803 | -93.2 | 152650 | 542 | -97.7 | 152650 | 309 |
| MR_1774412996_E41E3B41 | 504990 | 71 | -97.1 | 504990 | 287 | -96.6 | 504990 | 676 | -101.0 | 504990 | 516 |
| MR_1774412996_6DD5C764 | 504990 | 71 | -94.9 | 504990 | 287 | -98.9 | 504990 | 676 | -99.2 | 504990 | 516 |
| MR_1774412996_9BD0CA21 | 504990 | 71 | -97.4 | 504990 | 287 | -96.6 | 504990 | 676 | -98.8 | 504990 | 516 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 182: `951b9766-909...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `951b9766-9099-47fa-9e9c-d2c9ec51bef7` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[182] topology](images/test_0182.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215370_2
- `C2`: Add neighbor relationship between 3278569_3 and 3215370_2
- `C3`: Increase A3 Offset threshold for 3215370_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease transmission power for 3278569_3
- `C6`: Add neighbor relationship between 3273557_4 and 3215370_2
- `C7`: Decrease A3 Offset threshold for 3215370_2
- `C8`: Press down the tilt angle  of 3215370_2 by 10 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215370_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278569_3
- `C11`: Adjust the azimuth of 3278569_3 by 50 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278569_3
- `C13`: Lift the tilt angle  of 3215370_2 by 10 degrees
- `C14`: Decrease transmission power for 3215370_2
- `C15`: Increase transmission power for 3278569_3
- `C16`: Increase transmission power for 3215370_2
- `C17`: Decrease A3 Offset threshold for 3278569_3
- `C18`: Press down the tilt angle of 3278569_3 by 6 degrees
- `C19`: Lift the tilt angle of 3278569_3 by 6 degrees
- `C20`: Check test server and transmission issues
- `C21`: Increase A3 Offset threshold for 3278569_3
- `C22`: Adjust the azimuth of 3215370_2 by 20 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.866 | MS1 | 121.4656733473 | 31.1446359043 | 228 | 504990 | -84.97 | 17.96 | 388.98 | 0.12 | 2.39 | 1566 |
| 2024-09-20 22:21:32.726 | MS1 | 121.4656642099 | 31.1446367700 | 228 | 504990 | -75.77 | 13.20 | 554.56 | 0.15 | 2.78 | 1577 |
| 2024-09-20 22:21:33.729 | MS1 | 121.4656644853 | 31.1446282227 | 228 | 504990 | -78.40 | 13.84 | 537.09 | 0.13 | 2.64 | 1579 |
| 2024-09-20 22:21:34.815 | MS1 | 121.4656648835 | 31.1446197163 | 228 | 504990 | -83.63 | -3.64 | 49.02 | 0.06 | 1.24 | 1598 |
| 2024-09-20 22:21:35.653 | MS1 | 121.4656677253 | 31.1446200056 | 228 | 504990 | -86.44 | -1.45 | 42.56 | 0.12 | 1.08 | 1577 |
| 2024-09-20 22:21:36.718 | MS1 | 121.4656625937 | 31.1446196492 | 228 | 504990 | -87.47 | -0.98 | 69.67 | 0.10 | 1.36 | 1576 |
| 2024-09-20 22:21:37.400 | MS1 | 121.4656716331 | 31.1446371135 | 228 | 504990 | -83.77 | -3.49 | 61.69 | 0.11 | 1.25 | 1581 |
| 2024-09-20 22:21:38.736 | MS1 | 121.4656580711 | 31.1446379413 | 228 | 504990 | -86.12 | -0.38 | 50.32 | 0.14 | 1.42 | 1568 |
| 2024-09-20 22:21:39.683 | MS1 | 121.4656771756 | 31.1446370910 | 899 | 504990 | -82.86 | 13.34 | 240.55 | 0.09 | 1.24 | 1593 |
| 2024-09-20 22:21:40.528 | MS1 | 121.4656728464 | 31.1446213546 | 899 | 504990 | -80.66 | 15.37 | 499.42 | 0.10 | 2.96 | 1592 |
| 2024-09-20 22:21:41.766 | MS1 | 121.4656711247 | 31.1446198870 | 899 | 504990 | -83.35 | 13.97 | 503.41 | 0.06 | 2.92 | 1592 |
| 2024-09-20 22:21:42.379 | MS1 | 121.4656707887 | 31.1446259242 | 899 | 504990 | -80.93 | 12.96 | 361.11 | 0.08 | 2.18 | 1566 |

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
| 3215370 | 2 | 121.4642878702 | 31.1499031348 | 147 | 15 | 4 | 29.2 | TDD | 899 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3273557 | 4 | 121.4749091974 | 31.1555116175 | 232 | 14 | 3 | 31.9 | TDD | 383 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3278569 | 3 | 121.4742330172 | 31.1441060236 | 192 | 3 | 5 | 44.2 | TDD | 228 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3279043 | 1 | 121.4715010488 | 31.1544573247 | 66 | 7 | 5 | 16.7 | TDD | 3 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.595 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.617 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.756 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.756 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.469 | NREventA3 | measId:2;ServCellPCI:152;Se... |
| 2024-09-20 22:21:38.709 | NRHandoverAttempt | SourcePCI:152;SourceNR-ARFC... |
| 2024-09-20 22:21:38.749 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.759 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.869 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.869 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279043 | 1 | 14.7975 | 6.7639 | -117.2495 | 10.9965 | 167.3871 | 0.0130 | 0.0074 |
| 2024_09_20 22:00 | 3215370 | 2 | 13.4011 | 5.2575 | -116.8211 | 11.9879 | 193.0227 | 0.0087 | 0.0183 |
| 2024_09_20 22:00 | 3278569 | 3 | 17.1507 | 16.2967 | -115.2393 | 10.5545 | 198.0501 | 0.0148 | 0.1072 |
| 2024_09_20 22:00 | 3273557 | 4 | 12.4098 | 7.7149 | -115.2012 | 16.9868 | 93.6031 | 0.0013 | 0.0036 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414288_5B4B45BF | 504990 | 899 | -76.9 | 504990 | 228 | -84.8 | 504990 | 383 | -81.8 | 504990 | 3 |
| MR_1774414288_24E157B1 | 504990 | 228 | -82.4 | 504990 | 899 | -80.2 | 504990 | 383 | -81.7 | 504990 | 3 |
| MR_1774414288_A3DFEEEE | 504990 | 228 | -84.9 | 504990 | 899 | -79.1 | 504990 | 383 | -84.3 | 504990 | 3 |
| MR_1774414288_F353649A | 504990 | 228 | -83.8 | 504990 | 899 | -76.4 | 504990 | 383 | -81.7 | 504990 | 3 |
| MR_1774414288_AAA63F35 | 504990 | 228 | -82.9 | 504990 | 899 | -76.5 | 504990 | 383 | -83.1 | 504990 | 3 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 183: `c3c50ed6-25e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c3c50ed6-25ec-426b-b6eb-f9fb8a1c6ccd` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[183] topology](images/test_0183.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3264799_2 by 50 degrees
- `C2`: Add neighbor relationship between 3264799_2 and 3232934_1
- `C3`: Decrease transmission power for 3232934_1
- `C4`: Adjust the azimuth of 3234155_4 by 4 degrees
- `C5`: Increase transmission power for 3234155_4
- `C6`: Lift the tilt angle  of 3264799_2 by 10 degrees
- `C7`: Lift the tilt angle of 3234155_4 by 5 degrees
- `C8`: Press down the tilt angle of 3234155_4 by 5 degrees
- `C9`: Increase A3 Offset threshold for 3232934_1
- `C10`: Add neighbor relationship between 3234155_4 and 3232934_1
- `C11`: Increase A3 Offset threshold for 3234155_4
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234155_4
- `C14`: Decrease transmission power for 3234155_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234155_4
- `C16`: Decrease A3 Offset threshold for 3232934_1
- `C17`: Decrease A3 Offset threshold for 3234155_4
- `C18`: Increase transmission power for 3232934_1
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle  of 3264799_2 by 10 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232934_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232934_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.821 | MS1 | 121.4656621659 | 31.1446196469 | 990 | 504990 | -85.41 | 13.30 | 565.24 | 0.09 | 2.72 | 1575 |
| 2024-09-20 22:21:32.571 | MS1 | 121.4656624792 | 31.1446360847 | 990 | 504990 | -91.95 | 17.36 | 413.52 | 0.06 | 2.55 | 1566 |
| 2024-09-20 22:21:33.904 | MS1 | 121.4656735981 | 31.1446283770 | 990 | 504990 | -90.96 | 12.15 | 490.16 | 0.10 | 2.43 | 1600 |
| 2024-09-20 22:21:34.630 | MS1 | 121.4656645243 | 31.1446299516 | 990 | 504990 | -91.03 | 17.58 | 95.99 | 0.05 | 2.58 | 1571 |
| 2024-09-20 22:21:35.516 | MS1 | 121.4656772740 | 31.1446234669 | 990 | 504990 | -88.22 | 12.19 | 70.27 | 0.18 | 2.39 | 1573 |
| 2024-09-20 22:21:36.471 | MS1 | 121.4656751200 | 31.1446272385 | 990 | 504990 | -90.71 | 12.62 | 56.36 | 0.05 | 2.02 | 1579 |
| 2024-09-20 22:21:37.747 | MS1 | 121.4656684415 | 31.1446377658 | 990 | 504990 | -90.61 | 11.93 | 79.59 | 0.12 | 2.16 | 1578 |
| 2024-09-20 22:21:38.205 | MS1 | 121.4656769988 | 31.1446202082 | 990 | 504990 | -91.74 | 9.43 | 102.34 | 0.15 | 2.94 | 1592 |
| 2024-09-20 22:21:39.573 | MS1 | 121.4656659664 | 31.1446279653 | 990 | 504990 | -91.80 | 11.41 | 77.55 | 0.19 | 2.33 | 1596 |
| 2024-09-20 22:21:40.966 | MS1 | 121.4656772450 | 31.1446205470 | 990 | 504990 | -92.39 | 7.57 | 406.57 | 0.16 | 2.60 | 1588 |
| 2024-09-20 22:21:41.880 | MS1 | 121.4656742239 | 31.1446208208 | 990 | 504990 | -90.79 | 9.02 | 585.14 | 0.01 | 2.16 | 1571 |
| 2024-09-20 22:21:42.317 | MS1 | 121.4656721857 | 31.1446298678 | 990 | 504990 | -92.93 | 12.81 | 412.61 | 0.11 | 2.60 | 1564 |

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
| 3213571 | 3 | 121.4702413106 | 31.1514727009 | 86 | 14 | 6 | 21.1 | TDD | 573 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3232934 | 1 | 121.4677496326 | 31.1495802491 | 331 | 11 | 7 | 25.6 | TDD | 296 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3234155 | 4 | 121.4666649385 | 31.1516229225 | 191 | 2 | 5 | 43.0 | TDD | 990 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3264799 | 2 | 121.4723271264 | 31.1462285464 | 340 | 2 | 8 | 24.3 | TDD | 979 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.209 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.232 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.361 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.361 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.015 | NREventA3 | measId:2;ServCellPCI:65;Ser... |
| 2024-09-20 22:21:38.255 | NRHandoverAttempt | SourcePCI:65;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.293 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.308 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.417 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.417 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232934 | 1 | 19.4602 | 6.5846 | -116.5782 | 7.2290 | 97.8978 | 0.0194 | 0.0169 |
| 2024_09_20 22:00 | 3264799 | 2 | 11.8278 | 15.6733 | -117.5229 | 10.0804 | 87.0342 | 0.0180 | 0.0062 |
| 2024_09_20 22:00 | 3213571 | 3 | 12.9725 | 11.1377 | -116.1884 | 14.1466 | 101.1491 | 0.0192 | 0.0189 |
| 2024_09_20 22:00 | 3234155 | 4 | 83.1266 | 93.8988 | -115.7633 | 17.8152 | 170.8416 | 0.0177 | 0.0060 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416525_FC8DCF82 | 504990 | 990 | -89.2 | 504990 | 296 | -96.3 | 504990 | 979 | -100.4 | 504990 | 573 |
| MR_1774416525_D0169A85 | 504990 | 990 | -89.4 | 504990 | 296 | -96.3 | 504990 | 979 | -98.7 | 504990 | 573 |
| MR_1774416525_DF2013F2 | 504990 | 990 | -90.7 | 504990 | 296 | -98.0 | 504990 | 979 | -97.9 | 504990 | 573 |
| MR_1774416525_6EA16B6E | 504990 | 990 | -91.9 | 504990 | 296 | -99.4 | 504990 | 979 | -98.6 | 504990 | 573 |
| MR_1774416525_554FCCFE | 504990 | 990 | -92.6 | 504990 | 296 | -98.7 | 504990 | 979 | -100.5 | 504990 | 573 |
| MR_1774416525_598978CD | 504990 | 990 | -92.5 | 504990 | 296 | -98.0 | 504990 | 979 | -98.8 | 504990 | 573 |
| MR_1774416525_70E144FA | 504990 | 990 | -89.4 | 504990 | 296 | -96.0 | 504990 | 979 | -99.2 | 504990 | 573 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 184: `11ef6de0-a0b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `11ef6de0-a0b8-486a-a3d0-742617c3b99a` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[184] topology](images/test_0184.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3243918_4 and 3268980_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268980_1
- `C3`: Increase A3 Offset threshold for 3268980_1
- `C4`: Adjust the azimuth of 3268980_1 by 19 degrees
- `C5`: Press down the tilt angle  of 3268980_1 by 2 degrees
- `C6`: Press down the tilt angle of 3267958_2 by 10 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267958_2
- `C8`: Increase A3 Offset threshold for 3267958_2
- `C9`: Increase transmission power for 3267958_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268980_1
- `C11`: Decrease transmission power for 3267958_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease A3 Offset threshold for 3268980_1
- `C14`: Decrease transmission power for 3268980_1
- `C15`: Lift the tilt angle  of 3268980_1 by 2 degrees
- `C16`: Adjust the azimuth of 3267958_2 by 40 degrees
- `C17`: Check test server and transmission issues
- `C18`: Increase transmission power for 3268980_1
- `C19`: Add neighbor relationship between 3267958_2 and 3268980_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267958_2
- `C21`: Decrease A3 Offset threshold for 3267958_2
- `C22`: Lift the tilt angle of 3267958_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.650 | MS1 | 121.4656694767 | 31.1446200876 | 964 | 504990 | -81.32 | 13.58 | 516.62 | 0.16 | 2.27 | 1577 |
| 2024-09-20 22:21:32.576 | MS1 | 121.4656671791 | 31.1446296307 | 964 | 504990 | -83.81 | 16.87 | 382.43 | 0.19 | 2.28 | 1578 |
| 2024-09-20 22:21:33.345 | MS1 | 121.4656676838 | 31.1446372905 | 964 | 504990 | -75.44 | 17.03 | 345.50 | 0.11 | 2.38 | 1580 |
| 2024-09-20 22:21:34.820 | MS1 | 121.4656593086 | 31.1446233085 | 964 | 504990 | -90.38 | -2.20 | 39.12 | 0.15 | 1.43 | 1593 |
| 2024-09-20 22:21:35.476 | MS1 | 121.4656598213 | 31.1446284674 | 964 | 504990 | -91.41 | -1.84 | 39.69 | 0.15 | 1.12 | 1588 |
| 2024-09-20 22:21:36.794 | MS1 | 121.4656762982 | 31.1446222990 | 964 | 504990 | -89.95 | -2.61 | 32.57 | 0.10 | 1.28 | 1583 |
| 2024-09-20 22:21:37.810 | MS1 | 121.4656607805 | 31.1446303743 | 964 | 504990 | -89.35 | -1.19 | 53.38 | 0.01 | 1.40 | 1572 |
| 2024-09-20 22:21:38.419 | MS1 | 121.4656723424 | 31.1446267524 | 964 | 504990 | -81.94 | 16.96 | 589.86 | 0.12 | 1.10 | 1566 |
| 2024-09-20 22:21:39.115 | MS1 | 121.4656666080 | 31.1446338198 | 964 | 504990 | -81.87 | 14.27 | 362.24 | 0.12 | 1.39 | 1581 |
| 2024-09-20 22:21:40.186 | MS1 | 121.4656775068 | 31.1446355860 | 964 | 504990 | -83.58 | 16.92 | 447.52 | 0.19 | 2.32 | 1563 |
| 2024-09-20 22:21:41.810 | MS1 | 121.4656754899 | 31.1446366490 | 964 | 504990 | -76.63 | 17.02 | 525.12 | 0.12 | 2.99 | 1580 |
| 2024-09-20 22:21:42.200 | MS1 | 121.4656601327 | 31.1446205815 | 964 | 504990 | -75.90 | 13.64 | 506.69 | 0.11 | 2.43 | 1592 |

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
| 3243918 | 4 | 121.4695927705 | 31.1503445715 | 338 | 2 | 0 | 46.6 | TDD | 606 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3260498 | 3 | 121.4694959684 | 31.1493881313 | 270 | 6 | 11 | 29.8 | TDD | 821 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3267958 | 2 | 121.4752225673 | 31.1554410509 | 257 | 10 | 5 | 30.8 | TDD | 964 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3268980 | 1 | 121.4688703239 | 31.1536919070 | 216 | 0 | 12 | 34.0 | TDD | 318 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.533 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.555 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.661 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.661 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.377 | NREventA3 | measId:2;ServCellPCI:394;Se... |
| 2024-09-20 22:21:36.377 | NREventA3 | measId:2;ServCellPCI:394;Se... |
| 2024-09-20 22:21:37.377 | NREventA3 | measId:2;ServCellPCI:394;Se... |
| 2024-09-20 22:21:39.877 | NRRRCReestablishAttempt | PCI:394 |
| 2024-09-20 22:21:39.894 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.905 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:40.031 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.031 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268980 | 1 | 14.6680 | 6.8195 | -116.5673 | 7.6830 | 139.6742 | 0.0173 | 0.0052 |
| 2024_09_20 22:00 | 3267958 | 2 | 16.9786 | 12.6802 | -115.6466 | 13.1857 | 158.1902 | 0.0134 | 0.1523 |
| 2024_09_20 22:00 | 3260498 | 3 | 11.8906 | 7.0913 | -116.0213 | 15.9273 | 188.6595 | 0.0006 | 0.0108 |
| 2024_09_20 22:00 | 3243918 | 4 | 5.3508 | 6.5752 | -114.3228 | 13.7528 | 104.7177 | 0.0180 | 0.0018 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415980_30C28F94 | 504990 | 964 | -91.7 | 504990 | 318 | -86.3 | 504990 | 606 | -88.8 | 504990 | 821 |
| MR_1774415980_C23D821F | 504990 | 318 | -83.2 | 504990 | 964 | -91.1 | 504990 | 606 | -87.5 | 504990 | 821 |
| MR_1774415980_4470D012 | 504990 | 964 | -91.5 | 504990 | 318 | -83.7 | 504990 | 606 | -90.1 | 504990 | 821 |
| MR_1774415980_CB6A1EB0 | 504990 | 964 | -88.8 | 504990 | 318 | -83.2 | 504990 | 606 | -90.3 | 504990 | 821 |
| MR_1774415980_A4ABF01C | 504990 | 964 | -90.0 | 504990 | 318 | -87.0 | 504990 | 606 | -90.2 | 504990 | 821 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 185: `21d519a0-d46...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `21d519a0-d463-4b80-9582-34f7a35cfe09` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[185] topology](images/test_0185.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3246327_2
- `C2`: Increase transmission power for 3246327_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246327_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276783_1
- `C5`: Add neighbor relationship between 3246327_2 and 3276783_1
- `C6`: Adjust the azimuth of 3276783_1 by 40 degrees
- `C7`: Adjust the azimuth of 3246327_2 by 50 degrees
- `C8`: Increase A3 Offset threshold for 3246327_2
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Lift the tilt angle of 3246327_2 by 6 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246327_2
- `C12`: Increase transmission power for 3276783_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276783_1
- `C14`: Decrease A3 Offset threshold for 3276783_1
- `C15`: Decrease A3 Offset threshold for 3246327_2
- `C16`: Add neighbor relationship between 3212272_4 and 3276783_1
- `C17`: Press down the tilt angle  of 3276783_1 by 2 degrees
- `C18`: Increase A3 Offset threshold for 3276783_1
- `C19`: Decrease transmission power for 3276783_1
- `C20`: Check test server and transmission issues
- `C21`: Press down the tilt angle of 3246327_2 by 6 degrees
- `C22`: Lift the tilt angle  of 3276783_1 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.419 | MS1 | 121.4656675462 | 31.1446223378 | 580 | 504990 | -75.74 | 13.20 | 403.68 | 0.06 | 2.16 | 1565 |
| 2024-09-20 22:21:32.310 | MS1 | 121.4656721234 | 31.1446366965 | 580 | 504990 | -83.65 | 13.40 | 548.95 | 0.09 | 2.72 | 1562 |
| 2024-09-20 22:21:33.241 | MS1 | 121.4656760056 | 31.1446260408 | 580 | 504990 | -81.48 | 15.84 | 552.12 | 0.07 | 2.35 | 1600 |
| 2024-09-20 22:21:34.686 | MS1 | 121.4656668286 | 31.1446343800 | 580 | 504990 | -89.52 | -1.45 | 42.43 | 0.16 | 1.23 | 1592 |
| 2024-09-20 22:21:35.317 | MS1 | 121.4656614479 | 31.1446281126 | 580 | 504990 | -88.06 | -2.66 | 44.16 | 0.09 | 1.08 | 1598 |
| 2024-09-20 22:21:36.832 | MS1 | 121.4656674673 | 31.1446223184 | 580 | 504990 | -87.94 | -0.75 | 59.27 | 0.02 | 1.10 | 1587 |
| 2024-09-20 22:21:37.547 | MS1 | 121.4656697702 | 31.1446367777 | 580 | 504990 | -87.65 | -0.05 | 69.52 | 0.00 | 1.22 | 1567 |
| 2024-09-20 22:21:38.531 | MS1 | 121.4656641903 | 31.1446231544 | 580 | 504990 | -83.01 | 14.92 | 554.07 | 0.13 | 1.39 | 1584 |
| 2024-09-20 22:21:39.715 | MS1 | 121.4656637313 | 31.1446313132 | 580 | 504990 | -75.62 | 15.84 | 460.13 | 0.07 | 1.10 | 1570 |
| 2024-09-20 22:21:40.533 | MS1 | 121.4656719541 | 31.1446277577 | 580 | 504990 | -76.51 | 14.31 | 549.54 | 0.06 | 2.75 | 1567 |
| 2024-09-20 22:21:41.749 | MS1 | 121.4656678913 | 31.1446203079 | 580 | 504990 | -77.81 | 15.98 | 347.41 | 0.15 | 2.50 | 1579 |
| 2024-09-20 22:21:42.422 | MS1 | 121.4656680739 | 31.1446263757 | 580 | 504990 | -77.22 | 12.40 | 533.55 | 0.13 | 2.33 | 1586 |

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
| 3212272 | 4 | 121.4737109873 | 31.1497803495 | 207 | 0 | 11 | 47.8 | TDD | 459 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3230840 | 3 | 121.4716563109 | 31.1502327111 | 299 | 10 | 3 | 31.1 | TDD | 20 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3246327 | 2 | 121.4757311381 | 31.1470419383 | 173 | 5 | 9 | 23.3 | TDD | 580 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3276783 | 1 | 121.4668829474 | 31.1559111737 | 225 | 0 | 5 | 45.3 | TDD | 907 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.604 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.629 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.776 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.776 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.450 | NREventA3 | measId:2;ServCellPCI:227;Se... |
| 2024-09-20 22:21:36.450 | NREventA3 | measId:2;ServCellPCI:227;Se... |
| 2024-09-20 22:21:37.450 | NREventA3 | measId:2;ServCellPCI:227;Se... |
| 2024-09-20 22:21:39.950 | NRRRCReestablishAttempt | PCI:227 |
| 2024-09-20 22:21:39.963 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.976 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:40.097 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.097 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276783 | 1 | 12.6718 | 19.2230 | -115.4760 | 5.6079 | 133.2508 | 0.0166 | 0.0148 |
| 2024_09_20 22:00 | 3246327 | 2 | 16.0040 | 5.5537 | -117.8580 | 14.4775 | 190.4351 | 0.0057 | 0.1318 |
| 2024_09_20 22:00 | 3230840 | 3 | 13.2331 | 11.6231 | -116.6953 | 11.9815 | 124.3990 | 0.0192 | 0.0001 |
| 2024_09_20 22:00 | 3212272 | 4 | 11.5911 | 8.4027 | -116.8781 | 15.3077 | 132.8743 | 0.0170 | 0.0192 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415580_F7D8EF54 | 504990 | 580 | -91.4 | 504990 | 907 | -82.9 | 504990 | 459 | -87.3 | 504990 | 20 |
| MR_1774415580_C853E3F1 | 504990 | 907 | -83.6 | 504990 | 580 | -90.0 | 504990 | 459 | -88.8 | 504990 | 20 |
| MR_1774415580_5740B959 | 504990 | 580 | -89.6 | 504990 | 907 | -82.6 | 504990 | 459 | -89.5 | 504990 | 20 |
| MR_1774415580_9EC31384 | 504990 | 580 | -90.8 | 504990 | 907 | -82.7 | 504990 | 459 | -90.4 | 504990 | 20 |
| MR_1774415580_A5D993EA | 504990 | 580 | -87.9 | 504990 | 907 | -85.4 | 504990 | 459 | -89.2 | 504990 | 20 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 186: `9194a6b3-99e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9194a6b3-99eb-422e-aa06-fe97fc6fb439` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[186] topology](images/test_0186.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3224039_2 by 0 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264901_6
- `C3`: Add neighbor relationship between 3224039_2 and 3264901_6
- `C4`: Add neighbor relationship between 3277513_8 and 3264901_6
- `C5`: Increase A3 Offset threshold for 3264901_6
- `C6`: Lift the tilt angle  of 3264901_6 by 5 degrees
- `C7`: Adjust the azimuth of 3224039_2 by 32 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224039_2
- `C9`: Check test server and transmission issues
- `C10`: Adjust the azimuth of 3264901_6 by 18 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease A3 Offset threshold for 3224039_2
- `C13`: Increase transmission power for 3264901_6
- `C14`: Increase A3 Offset threshold for 3224039_2
- `C15`: Increase transmission power for 3224039_2
- `C16`: Press down the tilt angle  of 3264901_6 by 5 degrees
- `C17`: Decrease A3 Offset threshold for 3264901_6
- `C18`: Press down the tilt angle of 3224039_2 by 0 degrees
- `C19`: Decrease transmission power for 3224039_2
- `C20`: Decrease transmission power for 3264901_6
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224039_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264901_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.388 | MS1 | 121.4656687242 | 31.1446368317 | 586 | 504990 | -94.79 | 13.25 | 461.24 | 0.16 | 2.11 | 1574 |
| 2024-09-20 22:21:32.251 | MS1 | 121.4656765316 | 31.1446199106 | 79 | 504990 | -94.21 | 13.21 | 347.02 | 0.18 | 2.98 | 1578 |
| 2024-09-20 22:21:33.279 | MS1 | 121.4656687660 | 31.1446256772 | 823 | 504990 | -94.93 | 10.96 | 434.04 | 0.07 | 2.20 | 1593 |
| 2024-09-20 22:21:34.782 | MS1 | 121.4656668988 | 31.1446206091 | 544 | 152650 | -93.93 | 4.58 | 52.22 | 0.05 | 1.86 | 992 |
| 2024-09-20 22:21:35.339 | MS1 | 121.4656711557 | 31.1446224166 | 613 | 152650 | -93.41 | 6.54 | 57.88 | 0.12 | 1.85 | 935 |
| 2024-09-20 22:21:36.679 | MS1 | 121.4656721983 | 31.1446364451 | 384 | 152650 | -87.62 | 7.72 | 70.82 | 0.04 | 1.69 | 963 |
| 2024-09-20 22:21:37.985 | MS1 | 121.4656651215 | 31.1446369153 | 303 | 152650 | -91.44 | 5.62 | 85.51 | 0.05 | 1.86 | 958 |
| 2024-09-20 22:21:38.391 | MS1 | 121.4656768956 | 31.1446200285 | 544 | 152650 | -96.86 | 6.59 | 74.62 | 0.12 | 1.88 | 925 |
| 2024-09-20 22:21:39.733 | MS1 | 121.4656698335 | 31.1446225529 | 613 | 152650 | -88.09 | 4.59 | 57.09 | 0.11 | 1.56 | 905 |
| 2024-09-20 22:21:40.588 | MS1 | 121.4656692554 | 31.1446306009 | 384 | 152650 | -96.39 | 6.43 | 72.27 | 0.00 | 2.62 | 1586 |
| 2024-09-20 22:21:41.169 | MS1 | 121.4656590932 | 31.1446268847 | 303 | 152650 | -90.63 | 6.02 | 61.99 | 0.01 | 2.52 | 1579 |
| 2024-09-20 22:21:42.486 | MS1 | 121.4656755383 | 31.1446225313 | 544 | 152650 | -87.58 | 6.01 | 94.39 | 0.10 | 2.91 | 1591 |

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
| 3212508 | 3 | 121.4722983262 | 31.1506296307 | 51 | 7 | 5 | 26.8 | TDD | 79 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3216092 | 7 | 121.4749445461 | 31.1559636842 | 175 | 2 | 11 | 22.1 | FDD | 544 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3217125 | 13 | 121.4707374927 | 31.1464793090 | 118 | 15 | 1 | 25.5 | FDD | 923 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3220445 | 4 | 121.4646809897 | 31.1459835450 | 137 | 3 | 6 | 27.0 | TDD | 527 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3224039 | 2 | 121.4757340379 | 31.1467203263 | 224 | 0 | 5 | 6.0 | TDD | 586 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3224964 | 1 | 121.4742171844 | 31.1472379681 | 36 | 11 | 4 | 21.9 | TDD | 608 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3250755 | 10 | 121.4737878476 | 31.1525477734 | 319 | 11 | 0 | 29.3 | FDD | 303 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3264901 | 6 | 121.4723760625 | 31.1543955284 | 228 | 5 | 9 | 6.2 | TDD | 638 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3271569 | 5 | 121.4662492005 | 31.1501631580 | 106 | 5 | 1 | 27.1 | TDD | 823 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3276068 | 9 | 121.4728910044 | 31.1520992392 | 325 | 11 | 5 | 25.9 | FDD | 613 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3276746 | 11 | 121.4670366766 | 31.1557430002 | 171 | 9 | 6 | 18.3 | FDD | 824 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3277513 | 8 | 121.4678125408 | 31.1445590356 | 47 | 11 | 5 | 16.2 | FDD | 384 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3279721 | 12 | 121.4748370804 | 31.1479574108 | 9 | 14 | 2 | 23.3 | FDD | 377 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |

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
| 2024-09-20 22:21:31.391 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.415 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.542 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.542 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.217 | NREventA2 | measId:1;ServCellPCI:160;Se... |
| 2024-09-20 22:21:35.319 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.575 | NREventA5 | measId:3;ServCellPCI:160;Se... |
| 2024-09-20 22:21:35.638 | NRHandoverAttempt | SourcePCI:160;SourceNR-ARFC... |
| 2024-09-20 22:21:35.683 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.693 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.800 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.800 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224964 | 1 | 9.4822 | 12.2291 | -117.8084 | 10.8989 | 134.5200 | 0.0196 | 0.0132 |
| 2024_09_20 22:00 | 3224039 | 2 | 5.7333 | 6.7386 | -114.5180 | 16.6791 | 178.9181 | 0.0014 | 0.0149 |
| 2024_09_20 22:00 | 3212508 | 3 | 19.5464 | 14.8512 | -117.5241 | 19.4108 | 167.6002 | 0.0012 | 0.0108 |
| 2024_09_20 22:00 | 3220445 | 4 | 13.7980 | 17.0493 | -115.1676 | 19.3021 | 117.2860 | 0.0116 | 0.0036 |
| 2024_09_20 22:00 | 3271569 | 5 | 19.3809 | 9.8551 | -115.2213 | 9.9241 | 99.0381 | 0.0124 | 0.0182 |
| 2024_09_20 22:00 | 3264901 | 6 | 7.2282 | 6.2726 | -116.7216 | 8.4170 | 104.7082 | 0.0036 | 0.0047 |
| 2024_09_20 22:00 | 3216092 | 7 | 10.5667 | 9.3845 | -115.2444 | 4.6924 | 57.0550 | 0.0036 | 0.0062 |
| 2024_09_20 22:00 | 3277513 | 8 | 18.6876 | 8.2270 | -115.6992 | 4.6276 | 47.5043 | 0.0115 | 0.0127 |
| 2024_09_20 22:00 | 3276068 | 9 | 15.3555 | 14.4595 | -115.1476 | 3.1843 | 23.4729 | 0.0195 | 0.0191 |
| 2024_09_20 22:00 | 3250755 | 10 | 17.2354 | 10.1914 | -114.2995 | 3.3485 | 37.5225 | 0.0132 | 0.0090 |
| 2024_09_20 22:00 | 3276746 | 11 | 17.1576 | 6.1385 | -114.4060 | 3.7035 | 44.2596 | 0.0033 | 0.0005 |
| 2024_09_20 22:00 | 3279721 | 12 | 8.0269 | 15.9441 | -115.9002 | 4.3335 | 36.2514 | 0.0104 | 0.0136 |
| 2024_09_20 22:00 | 3217125 | 13 | 9.4832 | 10.3634 | -117.1566 | 4.2392 | 25.3098 | 0.0140 | 0.0131 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415679_0E5A1C5F | 504990 | 823 | -96.2 | 504990 | 638 | -93.7 | 504990 | 608 | -97.2 | 504990 | 527 |
| MR_1774415679_72C8CD53 | 504990 | 823 | -94.6 | 504990 | 638 | -94.8 | 504990 | 608 | -97.3 | 504990 | 527 |
| MR_1774415679_DE0E9748 | 504990 | 823 | -94.7 | 504990 | 638 | -93.4 | 504990 | 608 | -99.8 | 504990 | 527 |
| MR_1774415679_B20DE837 | 504990 | 823 | -95.5 | 504990 | 638 | -95.7 | 504990 | 608 | -95.9 | 504990 | 527 |
| MR_1774415679_620BF19D | 152650 | 544 | -92.8 | 152650 | 824 | -98.2 | 152650 | 377 | -101.8 | 152650 | 923 |
| MR_1774415679_76E2A3D7 | 504990 | 823 | -95.7 | 504990 | 638 | -96.6 | 504990 | 608 | -96.8 | 504990 | 527 |
| MR_1774415679_6A8D47A9 | 504990 | 823 | -96.2 | 504990 | 638 | -96.8 | 504990 | 608 | -96.2 | 504990 | 527 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 187: `1d55d74e-bd5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1d55d74e-bd5c-409c-a7c7-bf9dd0beadc5` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[187] topology](images/test_0187.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3231872_1 by 11 degrees
- `C2`: Lift the tilt angle of 3248469_3 by 10 degrees
- `C3`: Increase transmission power for 3231872_1
- `C4`: Add neighbor relationship between 3248469_3 and 3231872_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248469_3
- `C6`: Increase A3 Offset threshold for 3248469_3
- `C7`: Lift the tilt angle  of 3231872_1 by 10 degrees
- `C8`: Decrease transmission power for 3231872_1
- `C9`: Press down the tilt angle  of 3231872_1 by 10 degrees
- `C10`: Press down the tilt angle of 3248469_3 by 10 degrees
- `C11`: Decrease A3 Offset threshold for 3248469_3
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Increase A3 Offset threshold for 3231872_1
- `C14`: Adjust the azimuth of 3248469_3 by 50 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248469_3
- `C16`: Check test server and transmission issues
- `C17`: Decrease A3 Offset threshold for 3231872_1
- `C18`: Increase transmission power for 3248469_3
- `C19`: Decrease transmission power for 3248469_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231872_1
- `C21`: Add neighbor relationship between 3211705_2 and 3231872_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231872_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.557 | MS1 | 121.4656771262 | 31.1446309297 | 467 | 504990 | -77.21 | 15.10 | 367.40 | 0.14 | 2.26 | 1561 |
| 2024-09-20 22:21:32.457 | MS1 | 121.4656705813 | 31.1446218944 | 467 | 504990 | -84.55 | 13.97 | 443.09 | 0.05 | 2.19 | 1586 |
| 2024-09-20 22:21:33.411 | MS1 | 121.4656625796 | 31.1446250915 | 467 | 504990 | -80.18 | 15.01 | 591.67 | 0.09 | 2.16 | 1592 |
| 2024-09-20 22:21:34.323 | MS1 | 121.4656771407 | 31.1446192405 | 467 | 504990 | -91.31 | -2.56 | 60.73 | 0.08 | 1.42 | 1592 |
| 2024-09-20 22:21:35.586 | MS1 | 121.4656667083 | 31.1446230916 | 467 | 504990 | -91.52 | -1.70 | 31.97 | 0.11 | 1.14 | 1591 |
| 2024-09-20 22:21:36.503 | MS1 | 121.4656718537 | 31.1446265820 | 467 | 504990 | -84.05 | -3.01 | 49.38 | 0.16 | 1.02 | 1599 |
| 2024-09-20 22:21:37.527 | MS1 | 121.4656683920 | 31.1446320093 | 467 | 504990 | -90.24 | -3.80 | 70.35 | 0.03 | 1.44 | 1570 |
| 2024-09-20 22:21:38.598 | MS1 | 121.4656710541 | 31.1446372417 | 467 | 504990 | -91.64 | -0.18 | 71.79 | 0.18 | 1.21 | 1597 |
| 2024-09-20 22:21:39.850 | MS1 | 121.4656587217 | 31.1446366976 | 816 | 504990 | -82.77 | 15.72 | 229.25 | 0.02 | 1.08 | 1565 |
| 2024-09-20 22:21:40.261 | MS1 | 121.4656736844 | 31.1446276032 | 816 | 504990 | -84.64 | 15.45 | 407.32 | 0.13 | 2.64 | 1577 |
| 2024-09-20 22:21:41.714 | MS1 | 121.4656580226 | 31.1446266669 | 816 | 504990 | -78.82 | 16.27 | 554.91 | 0.16 | 2.50 | 1582 |
| 2024-09-20 22:21:42.540 | MS1 | 121.4656775230 | 31.1446219385 | 816 | 504990 | -82.02 | 16.53 | 350.78 | 0.11 | 2.86 | 1571 |

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
| 3211705 | 2 | 121.4727498781 | 31.1500286894 | 319 | 9 | 10 | 32.0 | TDD | 609 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3231872 | 1 | 121.4672039081 | 31.1466324674 | 202 | 9 | 6 | 33.5 | TDD | 816 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3240235 | 4 | 121.4755011670 | 31.1456935836 | 80 | 4 | 10 | 47.4 | TDD | 161 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3248469 | 3 | 121.4753956240 | 31.1499878205 | 134 | 10 | 8 | 37.9 | TDD | 467 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.547 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.564 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.691 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.691 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.384 | NREventA3 | measId:2;ServCellPCI:626;Se... |
| 2024-09-20 22:21:38.624 | NRHandoverAttempt | SourcePCI:626;SourceNR-ARFC... |
| 2024-09-20 22:21:38.664 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.676 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.779 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.779 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231872 | 1 | 14.4778 | 7.5398 | -117.9977 | 7.3429 | 122.2152 | 0.0198 | 0.0162 |
| 2024_09_20 22:00 | 3211705 | 2 | 8.0692 | 5.5960 | -115.8100 | 17.0441 | 123.9078 | 0.0122 | 0.0117 |
| 2024_09_20 22:00 | 3248469 | 3 | 17.4681 | 12.7600 | -117.5744 | 14.6597 | 96.8384 | 0.0044 | 0.1787 |
| 2024_09_20 22:00 | 3240235 | 4 | 17.4783 | 7.3123 | -116.2308 | 19.8340 | 102.9341 | 0.0097 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412261_0CB986D5 | 504990 | 467 | -92.7 | 504990 | 816 | -86.2 | 504990 | 609 | -84.9 | 504990 | 161 |
| MR_1774412261_17A056BD | 504990 | 816 | -86.1 | 504990 | 467 | -91.8 | 504990 | 609 | -86.5 | 504990 | 161 |
| MR_1774412261_2953B1BF | 504990 | 816 | -85.4 | 504990 | 467 | -93.1 | 504990 | 609 | -88.1 | 504990 | 161 |
| MR_1774412261_3DCC3493 | 504990 | 467 | -92.1 | 504990 | 816 | -84.5 | 504990 | 609 | -85.3 | 504990 | 161 |
| MR_1774412261_8B0311B1 | 504990 | 816 | -86.2 | 504990 | 467 | -90.5 | 504990 | 609 | -85.6 | 504990 | 161 |
| MR_1774412261_99730078 | 504990 | 816 | -86.1 | 504990 | 467 | -90.7 | 504990 | 609 | -88.5 | 504990 | 161 |
| MR_1774412261_860A721F | 504990 | 816 | -87.0 | 504990 | 467 | -92.2 | 504990 | 609 | -85.7 | 504990 | 161 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 188: `cec59a76-39f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cec59a76-39fb-42db-9cda-bbdecd4bd9ab` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[188] topology](images/test_0188.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3234316_4
- `C2`: Adjust the azimuth of 3257341_3 by 42 degrees
- `C3`: Increase transmission power for 3234316_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257341_3
- `C5`: Press down the tilt angle  of 3257341_3 by 2 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234316_4
- `C7`: Check test server and transmission issues
- `C8`: Increase A3 Offset threshold for 3257341_3
- `C9`: Decrease transmission power for 3234316_4
- `C10`: Increase transmission power for 3257341_3
- `C11`: Lift the tilt angle  of 3257341_3 by 2 degrees
- `C12`: Decrease transmission power for 3257341_3
- `C13`: Decrease A3 Offset threshold for 3257341_3
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Add neighbor relationship between 3235377_1 and 3257341_3
- `C16`: Increase A3 Offset threshold for 3234316_4
- `C17`: Lift the tilt angle of 3234316_4 by 10 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234316_4
- `C19`: Adjust the azimuth of 3234316_4 by 50 degrees
- `C20`: Add neighbor relationship between 3234316_4 and 3257341_3
- `C21`: Press down the tilt angle of 3234316_4 by 10 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257341_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.529 | MS1 | 121.4656747953 | 31.1446182222 | 30 | 504990 | -75.67 | 17.41 | 302.10 | 0.16 | 2.53 | 1569 |
| 2024-09-20 22:21:32.706 | MS1 | 121.4656643739 | 31.1446276525 | 30 | 504990 | -80.60 | 14.62 | 410.89 | 0.04 | 2.87 | 1589 |
| 2024-09-20 22:21:33.334 | MS1 | 121.4656748285 | 31.1446264790 | 30 | 504990 | -77.30 | 16.93 | 364.63 | 0.05 | 2.60 | 1583 |
| 2024-09-20 22:21:34.338 | MS1 | 121.4656701820 | 31.1446370018 | 30 | 504990 | -86.77 | -3.87 | 59.96 | 0.17 | 1.44 | 1585 |
| 2024-09-20 22:21:35.165 | MS1 | 121.4656659896 | 31.1446192708 | 30 | 504990 | -87.99 | -1.45 | 39.67 | 0.01 | 1.33 | 1587 |
| 2024-09-20 22:21:36.302 | MS1 | 121.4656767851 | 31.1446232956 | 30 | 504990 | -85.45 | -0.07 | 57.40 | 0.05 | 1.36 | 1581 |
| 2024-09-20 22:21:37.670 | MS1 | 121.4656747336 | 31.1446351589 | 30 | 504990 | -86.36 | -1.96 | 40.34 | 0.09 | 1.49 | 1578 |
| 2024-09-20 22:21:38.946 | MS1 | 121.4656752031 | 31.1446206413 | 30 | 504990 | -83.33 | 16.72 | 473.61 | 0.16 | 1.03 | 1587 |
| 2024-09-20 22:21:39.871 | MS1 | 121.4656688733 | 31.1446329383 | 30 | 504990 | -84.19 | 13.22 | 567.18 | 0.03 | 1.20 | 1579 |
| 2024-09-20 22:21:40.426 | MS1 | 121.4656605924 | 31.1446345872 | 30 | 504990 | -78.68 | 15.84 | 560.55 | 0.04 | 2.63 | 1560 |
| 2024-09-20 22:21:41.957 | MS1 | 121.4656745255 | 31.1446194945 | 30 | 504990 | -84.23 | 17.67 | 561.95 | 0.18 | 2.48 | 1570 |
| 2024-09-20 22:21:42.138 | MS1 | 121.4656708798 | 31.1446180375 | 30 | 504990 | -79.94 | 16.13 | 431.59 | 0.12 | 2.70 | 1561 |

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
| 3219538 | 2 | 121.4673317540 | 31.1511571531 | 25 | 7 | 5 | 45.7 | TDD | 628 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3234316 | 4 | 121.4756252453 | 31.1521946546 | 116 | 12 | 7 | 19.1 | TDD | 30 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3235377 | 1 | 121.4666437265 | 31.1539081045 | 330 | 11 | 1 | 29.1 | TDD | 700 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3257341 | 3 | 121.4733437241 | 31.1465766033 | 211 | 0 | 12 | 25.5 | TDD | 694 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.403 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.420 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.530 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.530 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.274 | NREventA3 | measId:2;ServCellPCI:70;Ser... |
| 2024-09-20 22:21:36.274 | NREventA3 | measId:2;ServCellPCI:70;Ser... |
| 2024-09-20 22:21:37.274 | NREventA3 | measId:2;ServCellPCI:70;Ser... |
| 2024-09-20 22:21:39.774 | NRRRCReestablishAttempt | PCI:70 |
| 2024-09-20 22:21:39.791 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.803 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.946 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.946 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235377 | 1 | 18.2449 | 18.7935 | -114.2800 | 19.2825 | 173.0146 | 0.0173 | 0.0163 |
| 2024_09_20 22:00 | 3219538 | 2 | 19.4333 | 17.9056 | -116.4609 | 10.2101 | 144.0697 | 0.0115 | 0.0051 |
| 2024_09_20 22:00 | 3257341 | 3 | 15.9866 | 17.9195 | -115.7264 | 16.4862 | 180.3380 | 0.0006 | 0.0096 |
| 2024_09_20 22:00 | 3234316 | 4 | 16.3888 | 19.5109 | -115.1145 | 7.3352 | 171.2379 | 0.0000 | 0.1089 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413571_E41C1412 | 504990 | 30 | -86.5 | 504990 | 694 | -80.4 | 504990 | 700 | -85.3 | 504990 | 628 |
| MR_1774413571_3E69CA25 | 504990 | 30 | -87.0 | 504990 | 694 | -82.4 | 504990 | 700 | -85.4 | 504990 | 628 |
| MR_1774413571_2A1EDB63 | 504990 | 30 | -85.7 | 504990 | 694 | -82.1 | 504990 | 700 | -86.5 | 504990 | 628 |
| MR_1774413571_40ED6884 | 504990 | 30 | -85.8 | 504990 | 694 | -79.1 | 504990 | 700 | -84.7 | 504990 | 628 |
| MR_1774413571_797E643C | 504990 | 30 | -88.1 | 504990 | 694 | -81.9 | 504990 | 700 | -86.2 | 504990 | 628 |
| MR_1774413571_F39B3CA9 | 504990 | 694 | -82.6 | 504990 | 30 | -87.0 | 504990 | 700 | -85.9 | 504990 | 628 |
| MR_1774413571_9E61FF10 | 504990 | 694 | -80.1 | 504990 | 30 | -86.0 | 504990 | 700 | -86.9 | 504990 | 628 |
| MR_1774413571_84C1702A | 504990 | 694 | -79.5 | 504990 | 30 | -85.6 | 504990 | 700 | -84.7 | 504990 | 628 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 189: `52731b2a-aa5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `52731b2a-aa57-4a41-8de9-3d3ab90d058d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[189] topology](images/test_0189.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3256682_2 by 2 degrees
- `C2`: Decrease transmission power for 3256682_2
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Adjust the azimuth of 3256682_2 by 37 degrees
- `C5`: Add neighbor relationship between 3256682_2 and 3254533_1
- `C6`: Decrease A3 Offset threshold for 3256682_2
- `C7`: Lift the tilt angle  of 3258860_3 by 10 degrees
- `C8`: Lift the tilt angle of 3256682_2 by 2 degrees
- `C9`: Increase transmission power for 3256682_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256682_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256682_2
- `C12`: Decrease A3 Offset threshold for 3254533_1
- `C13`: Increase A3 Offset threshold for 3256682_2
- `C14`: Decrease transmission power for 3254533_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254533_1
- `C16`: Adjust the azimuth of 3258860_3 by 50 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254533_1
- `C18`: Check test server and transmission issues
- `C19`: Add neighbor relationship between 3258860_3 and 3254533_1
- `C20`: Increase transmission power for 3254533_1
- `C21`: Increase A3 Offset threshold for 3254533_1
- `C22`: Press down the tilt angle  of 3258860_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.796 | MS1 | 121.4656602484 | 31.1446190655 | 764 | 504990 | -88.33 | 13.49 | 312.72 | 0.05 | 2.96 | 1565 |
| 2024-09-20 22:21:32.127 | MS1 | 121.4656649261 | 31.1446331231 | 764 | 504990 | -90.46 | 16.02 | 555.58 | 0.15 | 2.55 | 1576 |
| 2024-09-20 22:21:33.339 | MS1 | 121.4656676157 | 31.1446233374 | 764 | 504990 | -89.30 | 17.23 | 558.09 | 0.14 | 2.67 | 1566 |
| 2024-09-20 22:21:34.255 | MS1 | 121.4656602415 | 31.1446367577 | 764 | 504990 | -91.58 | 13.51 | 81.88 | 0.11 | 2.44 | 1575 |
| 2024-09-20 22:21:35.932 | MS1 | 121.4656765407 | 31.1446235457 | 764 | 504990 | -85.59 | 12.82 | 91.00 | 0.18 | 2.57 | 1586 |
| 2024-09-20 22:21:36.192 | MS1 | 121.4656671452 | 31.1446204283 | 764 | 504990 | -87.84 | 12.34 | 84.53 | 0.16 | 2.46 | 1579 |
| 2024-09-20 22:21:37.456 | MS1 | 121.4656736498 | 31.1446276073 | 764 | 504990 | -89.68 | 7.58 | 70.27 | 0.09 | 2.31 | 1564 |
| 2024-09-20 22:21:38.775 | MS1 | 121.4656617641 | 31.1446300391 | 764 | 504990 | -93.64 | 8.51 | 92.02 | 0.08 | 2.67 | 1574 |
| 2024-09-20 22:21:39.517 | MS1 | 121.4656615711 | 31.1446297619 | 764 | 504990 | -90.35 | 7.15 | 61.03 | 0.16 | 2.82 | 1596 |
| 2024-09-20 22:21:40.531 | MS1 | 121.4656661701 | 31.1446304033 | 764 | 504990 | -90.54 | 9.93 | 304.87 | 0.14 | 2.74 | 1577 |
| 2024-09-20 22:21:41.483 | MS1 | 121.4656743217 | 31.1446304008 | 764 | 504990 | -89.56 | 7.29 | 301.73 | 0.10 | 2.53 | 1573 |
| 2024-09-20 22:21:42.471 | MS1 | 121.4656751891 | 31.1446309438 | 764 | 504990 | -92.02 | 10.06 | 417.62 | 0.03 | 2.98 | 1564 |

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
| 3243033 | 4 | 121.4654701809 | 31.1450742061 | 168 | 1 | 11 | 20.4 | TDD | 935 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3254533 | 1 | 121.4731237232 | 31.1474287939 | 135 | 11 | 10 | 22.4 | TDD | 193 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3256682 | 2 | 121.4753827682 | 31.1485576745 | 208 | 0 | 12 | 37.5 | TDD | 764 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3258860 | 3 | 121.4693908154 | 31.1505489319 | 339 | 0 | 6 | 17.3 | TDD | 869 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.490 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.509 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.615 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.615 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.324 | NREventA3 | measId:2;ServCellPCI:176;Se... |
| 2024-09-20 22:21:38.564 | NRHandoverAttempt | SourcePCI:176;SourceNR-ARFC... |
| 2024-09-20 22:21:38.612 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.624 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.738 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.738 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254533 | 1 | 9.9051 | 17.2995 | -116.4744 | 6.9750 | 107.6239 | 0.0151 | 0.0161 |
| 2024_09_20 22:00 | 3256682 | 2 | 91.0035 | 92.2948 | -117.1012 | 18.9121 | 162.4141 | 0.0014 | 0.0003 |
| 2024_09_20 22:00 | 3258860 | 3 | 14.2302 | 8.5220 | -116.1189 | 18.7951 | 131.8818 | 0.0052 | 0.0163 |
| 2024_09_20 22:00 | 3243033 | 4 | 5.4289 | 8.8058 | -117.1809 | 7.3370 | 170.4727 | 0.0052 | 0.0038 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413938_E893E58A | 504990 | 764 | -91.4 | 504990 | 193 | -98.4 | 504990 | 869 | -102.8 | 504990 | 935 |
| MR_1774413938_E54A5ED7 | 504990 | 764 | -91.0 | 504990 | 193 | -99.3 | 504990 | 869 | -104.6 | 504990 | 935 |
| MR_1774413938_DC1EE832 | 504990 | 764 | -93.3 | 504990 | 193 | -100.8 | 504990 | 869 | -102.4 | 504990 | 935 |
| MR_1774413938_58F888AF | 504990 | 764 | -93.2 | 504990 | 193 | -99.6 | 504990 | 869 | -104.5 | 504990 | 935 |
| MR_1774413938_FB120D0E | 504990 | 764 | -90.9 | 504990 | 193 | -101.5 | 504990 | 869 | -104.5 | 504990 | 935 |
| MR_1774413938_E45F18F5 | 504990 | 764 | -90.9 | 504990 | 193 | -101.2 | 504990 | 869 | -103.0 | 504990 | 935 |

> *... 2개 열 생략 (전체 14열)*

---
