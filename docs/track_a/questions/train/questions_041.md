# Track A 문제 분석 — train[400]~train[409]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[400] ~ train[409] (10개)

## 목차

1. [문제 400: `07b3c8ed-0d2...`](#400) — single-answer, 정답: C22
2. [문제 401: `063683eb-f85...`](#401) — single-answer, 정답: C13
3. [문제 402: `ed6e1a8b-026...`](#402) — single-answer, 정답: C1
4. [문제 403: `2fbf3ce2-446...`](#403) — single-answer, 정답: C22
5. [문제 404: `a43a8de8-536...`](#404) — single-answer, 정답: C8
6. [문제 405: `7da66ddc-4a2...`](#405) — single-answer, 정답: C3
7. [문제 406: `53a67654-1fe...`](#406) — single-answer, 정답: C14
8. [문제 407: `e2719360-d7f...`](#407) — single-answer, 정답: C4
9. [문제 408: `827d13a1-a31...`](#408) — single-answer, 정답: C20
10. [문제 409: `06064651-752...`](#409) — single-answer, 정답: C15

---

### 문제 400: `07b3c8ed-0d2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `07b3c8ed-0d2a-4bc9-9a06-b31837fd4176` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Lift the tilt angle  of 3253243_3 by 9 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[400] topology](images/train_0400.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3217656_1
- `C2`: Press down the tilt angle of 3217656_1 by 3 degrees
- `C3`: Lift the tilt angle of 3217656_1 by 3 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease transmission power for 3217656_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278979_4
- `C7`: Add neighbor relationship between 3217656_1 and 3278979_4
- `C8`: Increase transmission power for 3278979_4
- `C9`: Press down the tilt angle  of 3253243_3 by 9 degrees
- `C10`: Decrease A3 Offset threshold for 3278979_4
- `C11`: Adjust the azimuth of 3253243_3 by 50 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217656_1
- `C13`: Decrease transmission power for 3278979_4
- `C14`: Check test server and transmission issues
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217656_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278979_4
- `C17`: Increase A3 Offset threshold for 3217656_1
- `C18`: Increase transmission power for 3217656_1
- `C19`: Adjust the azimuth of 3217656_1 by 36 degrees
- `C20`: Add neighbor relationship between 3253243_3 and 3278979_4
- `C21`: Increase A3 Offset threshold for 3278979_4
- `C22`: Lift the tilt angle  of 3253243_3 by 9 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.674 | MS1 | 121.4656660714 | 31.1446328061 | 307 | 504990 | -85.70 | 12.27 | 360.24 | 0.03 | 2.31 | 1583 |
| 2024-09-20 22:21:32.508 | MS1 | 121.4656614748 | 31.1446268488 | 307 | 504990 | -86.77 | 12.01 | 561.59 | 0.15 | 2.41 | 1573 |
| 2024-09-20 22:21:33.562 | MS1 | 121.4656626481 | 31.1446301424 | 307 | 504990 | -85.05 | 15.85 | 552.90 | 0.07 | 2.96 | 1587 |
| 2024-09-20 22:21:34.154 | MS1 | 121.4656777900 | 31.1446289923 | 307 | 504990 | -89.61 | 17.96 | 73.00 | 0.17 | 2.29 | 1568 |
| 2024-09-20 22:21:35.887 | MS1 | 121.4656661347 | 31.1446213859 | 307 | 504990 | -89.24 | 17.01 | 88.84 | 0.08 | 2.74 | 1565 |
| 2024-09-20 22:21:36.249 | MS1 | 121.4656606270 | 31.1446323981 | 307 | 504990 | -87.25 | 17.83 | 65.26 | 0.11 | 2.11 | 1591 |
| 2024-09-20 22:21:37.603 | MS1 | 121.4656699287 | 31.1446186010 | 307 | 504990 | -89.72 | 7.87 | 78.52 | 0.15 | 2.30 | 1591 |
| 2024-09-20 22:21:38.748 | MS1 | 121.4656677171 | 31.1446329276 | 307 | 504990 | -92.07 | 9.74 | 46.02 | 0.02 | 2.97 | 1563 |
| 2024-09-20 22:21:39.808 | MS1 | 121.4656671179 | 31.1446244989 | 307 | 504990 | -92.48 | 11.71 | 64.55 | 0.02 | 2.96 | 1561 |
| 2024-09-20 22:21:40.943 | MS1 | 121.4656663117 | 31.1446312573 | 307 | 504990 | -89.20 | 12.11 | 347.40 | 0.02 | 2.64 | 1578 |
| 2024-09-20 22:21:41.900 | MS1 | 121.4656676460 | 31.1446210471 | 307 | 504990 | -93.97 | 12.07 | 386.61 | 0.13 | 2.09 | 1597 |
| 2024-09-20 22:21:42.116 | MS1 | 121.4656707536 | 31.1446263428 | 307 | 504990 | -91.09 | 7.76 | 433.20 | 0.13 | 2.09 | 1593 |

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
| 3217656 | 1 | 121.4688322707 | 31.1470860136 | 264 | 1 | 8 | 16.5 | TDD | 307 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3229327 | 2 | 121.4735520565 | 31.1446065337 | 8 | 4 | 8 | 35.2 | TDD | 924 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3253243 | 3 | 121.4747281766 | 31.1552100678 | 154 | 10 | 10 | 44.2 | TDD | 828 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3278979 | 4 | 121.4658688988 | 31.1480753486 | 257 | 3 | 10 | 40.0 | TDD | 111 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.198 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.214 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.338 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.338 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.999 | NREventA3 | measId:2;ServCellPCI:129;Se... |
| 2024-09-20 22:21:38.239 | NRHandoverAttempt | SourcePCI:129;SourceNR-ARFC... |
| 2024-09-20 22:21:38.275 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.285 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.416 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.416 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217656 | 1 | 85.2333 | 90.1130 | -117.2788 | 18.9990 | 128.4552 | 0.0013 | 0.0187 |
| 2024_09_20 22:00 | 3229327 | 2 | 9.8070 | 5.1894 | -114.2872 | 8.4791 | 179.4032 | 0.0064 | 0.0147 |
| 2024_09_20 22:00 | 3253243 | 3 | 14.6887 | 19.1040 | -117.5052 | 16.0649 | 120.3219 | 0.0174 | 0.0115 |
| 2024_09_20 22:00 | 3278979 | 4 | 15.8740 | 5.2875 | -116.3069 | 12.2317 | 177.7250 | 0.0176 | 0.0077 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417203_E8837509 | 504990 | 307 | -88.6 | 504990 | 111 | -98.0 | 504990 | 828 | -98.5 | 504990 | 924 |
| MR_1774417203_540C2514 | 504990 | 307 | -90.9 | 504990 | 111 | -95.4 | 504990 | 828 | -96.9 | 504990 | 924 |
| MR_1774417203_325008A5 | 504990 | 307 | -90.5 | 504990 | 111 | -97.8 | 504990 | 828 | -96.3 | 504990 | 924 |
| MR_1774417203_0121583A | 504990 | 307 | -89.8 | 504990 | 111 | -95.7 | 504990 | 828 | -97.3 | 504990 | 924 |
| MR_1774417203_A7A47ADD | 504990 | 307 | -89.6 | 504990 | 111 | -95.5 | 504990 | 828 | -97.2 | 504990 | 924 |
| MR_1774417203_9D77CC03 | 504990 | 307 | -90.1 | 504990 | 111 | -96.1 | 504990 | 828 | -98.6 | 504990 | 924 |
| MR_1774417203_D7F7BC93 | 504990 | 307 | -89.2 | 504990 | 111 | -96.2 | 504990 | 828 | -98.5 | 504990 | 924 |
| MR_1774417203_1E6E5E18 | 504990 | 307 | -87.7 | 504990 | 111 | -95.1 | 504990 | 828 | -99.7 | 504990 | 924 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 401: `063683eb-f85...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `063683eb-f852-4c94-91f7-b5a589201de7` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272735_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[401] topology](images/train_0401.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3272735_1 by 4 degrees
- `C2`: Decrease A3 Offset threshold for 3272735_1
- `C3`: Adjust the azimuth of 3252910_2 by 10 degrees
- `C4`: Increase A3 Offset threshold for 3272735_1
- `C5`: Press down the tilt angle  of 3252910_2 by 4 degrees
- `C6`: Add neighbor relationship between 3272735_1 and 3252910_2
- `C7`: Adjust the azimuth of 3272735_1 by 10 degrees
- `C8`: Add neighbor relationship between 3247311_7 and 3252910_2
- `C9`: Increase transmission power for 3252910_2
- `C10`: Increase A3 Offset threshold for 3252910_2
- `C11`: Check test server and transmission issues
- `C12`: Increase transmission power for 3272735_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272735_1 **← 정답**
- `C14`: Press down the tilt angle of 3272735_1 by 4 degrees
- `C15`: Lift the tilt angle  of 3252910_2 by 4 degrees
- `C16`: Decrease A3 Offset threshold for 3252910_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252910_2
- `C18`: Decrease transmission power for 3272735_1
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease transmission power for 3252910_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252910_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272735_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.488 | MS1 | 121.4656773368 | 31.1446243024 | 544 | 504990 | -93.22 | 14.75 | 378.82 | 0.15 | 2.90 | 1586 |
| 2024-09-20 22:21:32.217 | MS1 | 121.4656715742 | 31.1446195253 | 680 | 504990 | -95.22 | 14.12 | 457.29 | 0.12 | 2.40 | 1573 |
| 2024-09-20 22:21:33.743 | MS1 | 121.4656772112 | 31.1446203471 | 820 | 504990 | -94.20 | 12.76 | 336.62 | 0.06 | 2.65 | 1585 |
| 2024-09-20 22:21:34.386 | MS1 | 121.4656661368 | 31.1446272386 | 218 | 152650 | -92.31 | 7.40 | 90.55 | 0.12 | 1.95 | 918 |
| 2024-09-20 22:21:35.569 | MS1 | 121.4656698434 | 31.1446202667 | 223 | 152650 | -90.29 | 2.67 | 77.77 | 0.14 | 1.67 | 918 |
| 2024-09-20 22:21:36.716 | MS1 | 121.4656777442 | 31.1446249633 | 778 | 152650 | -91.12 | 5.34 | 82.18 | 0.11 | 1.99 | 980 |
| 2024-09-20 22:21:37.560 | MS1 | 121.4656583187 | 31.1446212052 | 502 | 152650 | -92.29 | 5.62 | 102.35 | 0.05 | 1.60 | 976 |
| 2024-09-20 22:21:38.534 | MS1 | 121.4656757577 | 31.1446348633 | 218 | 152650 | -94.26 | 7.94 | 106.78 | 0.09 | 1.87 | 950 |
| 2024-09-20 22:21:39.412 | MS1 | 121.4656634841 | 31.1446186454 | 223 | 152650 | -94.76 | 5.97 | 102.09 | 0.14 | 1.50 | 994 |
| 2024-09-20 22:21:40.954 | MS1 | 121.4656672627 | 31.1446336214 | 778 | 152650 | -89.84 | 7.98 | 82.98 | 0.12 | 2.42 | 1591 |
| 2024-09-20 22:21:41.880 | MS1 | 121.4656629688 | 31.1446214061 | 502 | 152650 | -94.85 | 2.72 | 71.70 | 0.14 | 2.52 | 1583 |
| 2024-09-20 22:21:42.995 | MS1 | 121.4656583326 | 31.1446290793 | 218 | 152650 | -90.77 | 5.08 | 98.20 | 0.08 | 2.94 | 1594 |

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
| 3214788 | 9 | 121.4646383600 | 31.1446376985 | 346 | 5 | 10 | 0.3 | FDD | 373 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3220023 | 12 | 121.4756794848 | 31.1506934911 | 231 | 10 | 7 | 11.6 | FDD | 890 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3223907 | 11 | 121.4644321131 | 31.1501973335 | 34 | 1 | 7 | 5.8 | FDD | 218 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3224015 | 3 | 121.4685919977 | 31.1542211737 | 207 | 1 | 8 | 3.5 | TDD | 680 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3226297 | 10 | 121.4742460284 | 31.1475044195 | 46 | 0 | 5 | 10.2 | FDD | 502 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3235344 | 6 | 121.4690640588 | 31.1508523283 | 188 | 1 | 3 | 17.8 | TDD | 347 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3247311 | 7 | 121.4713035183 | 31.1484016892 | 277 | 11 | 3 | 1.1 | FDD | 778 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3252910 | 2 | 121.4723109202 | 31.1455722853 | 251 | 2 | 10 | 27.3 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3253878 | 4 | 121.4656999202 | 31.1539414053 | 276 | 14 | 11 | 28.5 | TDD | 820 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3259819 | 8 | 121.4759608792 | 31.1537379419 | 314 | 14 | 1 | 22.5 | FDD | 305 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3259850 | 13 | 121.4681941378 | 31.1546078493 | 314 | 3 | 3 | 16.7 | FDD | 223 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3263472 | 5 | 121.4725377807 | 31.1553869273 | 326 | 15 | 2 | 28.1 | TDD | 857 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3272735 | 1 | 121.4730631753 | 31.1442043032 | 264 | 3 | 3 | 12.6 | TDD | 544 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.151 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.171 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.283 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.283 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.026 | NREventA2 | measId:1;ServCellPCI:673;Se... |
| 2024-09-20 22:21:35.155 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.363 | NREventA5 | measId:3;ServCellPCI:673;Se... |
| 2024-09-20 22:21:35.435 | NRHandoverAttempt | SourcePCI:673;SourceNR-ARFC... |
| 2024-09-20 22:21:35.477 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.487 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.624 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.624 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272735 | 1 | 16.5630 | 6.8379 | -116.0932 | 5.9811 | 171.1123 | 0.0134 | 0.0030 |
| 2024_09_20 22:00 | 3252910 | 2 | 9.6991 | 11.6970 | -117.3435 | 8.1786 | 145.5987 | 0.0148 | 0.0059 |
| 2024_09_20 22:00 | 3224015 | 3 | 18.4362 | 15.0573 | -114.5722 | 12.4327 | 187.0862 | 0.0111 | 0.0086 |
| 2024_09_20 22:00 | 3253878 | 4 | 8.7649 | 8.3430 | -114.2930 | 14.7895 | 165.6715 | 0.0199 | 0.0086 |
| 2024_09_20 22:00 | 3263472 | 5 | 12.1270 | 9.3995 | -117.4432 | 15.6329 | 121.9417 | 0.0135 | 0.0046 |
| 2024_09_20 22:00 | 3235344 | 6 | 8.8171 | 14.9121 | -115.7531 | 16.2915 | 181.4572 | 0.0101 | 0.0197 |
| 2024_09_20 22:00 | 3247311 | 7 | 8.9033 | 6.4838 | -115.8734 | 4.0004 | 52.4713 | 0.0037 | 0.0096 |
| 2024_09_20 22:00 | 3259819 | 8 | 14.2440 | 7.2412 | -117.8841 | 4.7499 | 49.4029 | 0.0154 | 0.0063 |
| 2024_09_20 22:00 | 3214788 | 9 | 17.7766 | 10.4912 | -117.2636 | 3.3587 | 31.9794 | 0.0098 | 0.0026 |
| 2024_09_20 22:00 | 3226297 | 10 | 16.6958 | 18.3893 | -116.9486 | 4.6348 | 46.1788 | 0.0038 | 0.0129 |
| 2024_09_20 22:00 | 3223907 | 11 | 6.8409 | 17.5930 | -114.4249 | 3.4895 | 59.9690 | 0.0188 | 0.0067 |
| 2024_09_20 22:00 | 3220023 | 12 | 19.2510 | 13.9086 | -114.2292 | 4.6245 | 57.6962 | 0.0013 | 0.0002 |
| 2024_09_20 22:00 | 3259850 | 13 | 8.9583 | 5.5444 | -116.2280 | 3.8934 | 25.9599 | 0.0197 | 0.0001 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412559_43AA600E | 504990 | 820 | -95.5 | 504990 | 129 | -92.7 | 504990 | 347 | -96.3 | 504990 | 857 |
| MR_1774412559_5CDA6CA5 | 152650 | 218 | -94.0 | 152650 | 305 | -96.9 | 152650 | 890 | -99.0 | 152650 | 373 |
| MR_1774412559_B0122E38 | 152650 | 218 | -92.6 | 152650 | 305 | -100.2 | 152650 | 890 | -99.5 | 152650 | 373 |
| MR_1774412559_9056EA00 | 504990 | 820 | -92.9 | 504990 | 129 | -92.8 | 504990 | 347 | -97.1 | 504990 | 857 |
| MR_1774412559_7E2B51CB | 152650 | 218 | -91.2 | 152650 | 305 | -98.0 | 152650 | 890 | -100.6 | 152650 | 373 |
| MR_1774412559_771D0D98 | 504990 | 820 | -94.4 | 504990 | 129 | -93.0 | 504990 | 347 | -97.9 | 504990 | 857 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 402: `ed6e1a8b-026...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ed6e1a8b-0268-498b-84dd-32b74cab8af2` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3277977_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[402] topology](images/train_0402.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277977_3 **← 정답**
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271993_1
- `C3`: Decrease A3 Offset threshold for 3271993_1
- `C4`: Increase A3 Offset threshold for 3271993_1
- `C5`: Decrease A3 Offset threshold for 3277977_3
- `C6`: Adjust the azimuth of 3271993_1 by 50 degrees
- `C7`: Increase transmission power for 3277977_3
- `C8`: Decrease transmission power for 3277977_3
- `C9`: Adjust the azimuth of 3277977_3 by 38 degrees
- `C10`: Lift the tilt angle of 3277977_3 by 4 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271993_1
- `C12`: Add neighbor relationship between 3272085_2 and 3271993_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277977_3
- `C14`: Increase A3 Offset threshold for 3277977_3
- `C15`: Decrease transmission power for 3271993_1
- `C16`: Press down the tilt angle  of 3271993_1 by 10 degrees
- `C17`: Check test server and transmission issues
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Lift the tilt angle  of 3271993_1 by 10 degrees
- `C20`: Press down the tilt angle of 3277977_3 by 4 degrees
- `C21`: Add neighbor relationship between 3277977_3 and 3271993_1
- `C22`: Increase transmission power for 3271993_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.900 | MS1 | 121.4656756173 | 31.1446330686 | 597 | 504990 | -86.05 | 12.78 | 532.88 | 0.09 | 2.35 | 1576 |
| 2024-09-20 22:21:32.558 | MS1 | 121.4656715738 | 31.1446373453 | 597 | 504990 | -86.84 | 14.51 | 486.38 | 0.07 | 2.61 | 1583 |
| 2024-09-20 22:21:33.308 | MS1 | 121.4656712025 | 31.1446237958 | 597 | 504990 | -91.24 | 17.26 | 494.55 | 0.04 | 2.15 | 1573 |
| 2024-09-20 22:21:34.973 | MS1 | 121.4656581991 | 31.1446290438 | 597 | 504990 | -87.28 | 12.70 | 98.56 | 0.68 | 2.58 | 580 |
| 2024-09-20 22:21:35.388 | MS1 | 121.4656670550 | 31.1446266335 | 597 | 504990 | -89.93 | 17.06 | 64.89 | 0.69 | 2.89 | 601 |
| 2024-09-20 22:21:36.132 | MS1 | 121.4656745531 | 31.1446183807 | 597 | 504990 | -85.96 | 15.03 | 70.54 | 0.55 | 2.28 | 690 |
| 2024-09-20 22:21:37.101 | MS1 | 121.4656653068 | 31.1446271242 | 597 | 504990 | -89.97 | 11.64 | 58.15 | 0.66 | 2.90 | 582 |
| 2024-09-20 22:21:38.452 | MS1 | 121.4656647360 | 31.1446246090 | 597 | 504990 | -91.32 | 8.71 | 81.94 | 0.62 | 2.26 | 625 |
| 2024-09-20 22:21:39.920 | MS1 | 121.4656706218 | 31.1446333418 | 597 | 504990 | -91.62 | 8.48 | 95.37 | 0.61 | 2.06 | 598 |
| 2024-09-20 22:21:40.405 | MS1 | 121.4656768220 | 31.1446330194 | 597 | 504990 | -89.65 | 11.14 | 579.73 | 0.06 | 2.79 | 1577 |
| 2024-09-20 22:21:41.979 | MS1 | 121.4656700912 | 31.1446302334 | 597 | 504990 | -93.44 | 8.40 | 534.60 | 0.19 | 2.23 | 1593 |
| 2024-09-20 22:21:42.936 | MS1 | 121.4656720759 | 31.1446334710 | 597 | 504990 | -92.85 | 11.65 | 410.75 | 0.07 | 2.01 | 1592 |

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
| 3217319 | 4 | 121.4658710728 | 31.1530589199 | 106 | 2 | 2 | 39.8 | TDD | 317 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3271993 | 1 | 121.4652459544 | 31.1451980254 | 93 | 11 | 7 | 19.3 | TDD | 101 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3272085 | 2 | 121.4698144203 | 31.1545983798 | 139 | 13 | 2 | 26.7 | TDD | 338 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3277977 | 3 | 121.4743675195 | 31.1504266068 | 194 | 2 | 2 | 32.1 | TDD | 597 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.571 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.588 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.711 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.711 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.461 | NREventA3 | measId:2;ServCellPCI:544;Se... |
| 2024-09-20 22:21:38.701 | NRHandoverAttempt | SourcePCI:544;SourceNR-ARFC... |
| 2024-09-20 22:21:38.739 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.751 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.853 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.853 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271993 | 1 | 17.9384 | 6.4691 | -116.0725 | 11.4895 | 90.9192 | 0.0012 | 0.0075 |
| 2024_09_20 22:00 | 3272085 | 2 | 11.0423 | 12.8000 | -114.3429 | 7.7574 | 169.9654 | 0.0116 | 0.0172 |
| 2024_09_20 22:00 | 3277977 | 3 | 18.9213 | 16.5280 | -114.0768 | 11.9005 | 82.3584 | 0.0139 | 0.0145 |
| 2024_09_20 22:00 | 3217319 | 4 | 10.4171 | 7.9983 | -115.5711 | 10.8783 | 196.9387 | 0.0086 | 0.0024 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412147_499477A5 | 504990 | 597 | -87.2 | 504990 | 101 | -87.5 | 504990 | 338 | -95.7 | 504990 | 317 |
| MR_1774412147_2654855F | 504990 | 597 | -86.4 | 504990 | 101 | -89.2 | 504990 | 338 | -93.6 | 504990 | 317 |
| MR_1774412147_EF7C3396 | 504990 | 597 | -85.5 | 504990 | 101 | -88.6 | 504990 | 338 | -95.1 | 504990 | 317 |
| MR_1774412147_A62B8F42 | 504990 | 597 | -88.7 | 504990 | 101 | -88.8 | 504990 | 338 | -92.8 | 504990 | 317 |
| MR_1774412147_B371B8FB | 504990 | 597 | -86.4 | 504990 | 101 | -86.0 | 504990 | 338 | -92.6 | 504990 | 317 |
| MR_1774412147_0945C26E | 504990 | 597 | -86.9 | 504990 | 101 | -85.7 | 504990 | 338 | -96.2 | 504990 | 317 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 403: `2fbf3ce2-446...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2fbf3ce2-4467-4372-a5ae-9c99fff2a50a` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Lift the tilt angle  of 3254419_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[403] topology](images/train_0403.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3254419_3 and 3222822_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234432_1
- `C3`: Check test server and transmission issues
- `C4`: Adjust the azimuth of 3234432_1 by 25 degrees
- `C5`: Decrease A3 Offset threshold for 3222822_2
- `C6`: Decrease transmission power for 3222822_2
- `C7`: Increase A3 Offset threshold for 3234432_1
- `C8`: Adjust the azimuth of 3254419_3 by 50 degrees
- `C9`: Decrease A3 Offset threshold for 3234432_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222822_2
- `C11`: Increase transmission power for 3234432_1
- `C12`: Increase A3 Offset threshold for 3222822_2
- `C13`: Press down the tilt angle of 3234432_1 by 5 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Add neighbor relationship between 3234432_1 and 3222822_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222822_2
- `C17`: Decrease transmission power for 3234432_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234432_1
- `C19`: Increase transmission power for 3222822_2
- `C20`: Lift the tilt angle of 3234432_1 by 5 degrees
- `C21`: Press down the tilt angle  of 3254419_3 by 10 degrees
- `C22`: Lift the tilt angle  of 3254419_3 by 10 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.500 | MS1 | 121.4656677759 | 31.1446350921 | 70 | 504990 | -88.56 | 17.11 | 420.54 | 0.09 | 2.15 | 1562 |
| 2024-09-20 22:21:32.890 | MS1 | 121.4656738960 | 31.1446282904 | 70 | 504990 | -87.83 | 17.18 | 557.68 | 0.12 | 2.59 | 1584 |
| 2024-09-20 22:21:33.993 | MS1 | 121.4656668293 | 31.1446197738 | 70 | 504990 | -89.08 | 16.15 | 299.51 | 0.07 | 2.79 | 1587 |
| 2024-09-20 22:21:34.731 | MS1 | 121.4656619647 | 31.1446274014 | 70 | 504990 | -91.14 | 12.85 | 46.03 | 0.02 | 2.31 | 1581 |
| 2024-09-20 22:21:35.387 | MS1 | 121.4656619252 | 31.1446190063 | 70 | 504990 | -89.00 | 15.34 | 64.71 | 0.09 | 2.36 | 1591 |
| 2024-09-20 22:21:36.127 | MS1 | 121.4656621620 | 31.1446304035 | 70 | 504990 | -86.83 | 15.75 | 65.21 | 0.10 | 2.66 | 1578 |
| 2024-09-20 22:21:37.485 | MS1 | 121.4656701536 | 31.1446307171 | 70 | 504990 | -90.26 | 9.58 | 90.78 | 0.02 | 2.72 | 1581 |
| 2024-09-20 22:21:38.658 | MS1 | 121.4656774504 | 31.1446345387 | 70 | 504990 | -91.74 | 10.26 | 87.11 | 0.15 | 2.08 | 1590 |
| 2024-09-20 22:21:39.364 | MS1 | 121.4656720416 | 31.1446195630 | 70 | 504990 | -92.36 | 11.56 | 84.81 | 0.17 | 2.62 | 1570 |
| 2024-09-20 22:21:40.178 | MS1 | 121.4656585777 | 31.1446223163 | 70 | 504990 | -93.86 | 8.37 | 451.01 | 0.16 | 2.32 | 1579 |
| 2024-09-20 22:21:41.269 | MS1 | 121.4656679547 | 31.1446196879 | 70 | 504990 | -91.49 | 12.01 | 392.48 | 0.06 | 2.33 | 1573 |
| 2024-09-20 22:21:42.208 | MS1 | 121.4656590624 | 31.1446268690 | 70 | 504990 | -89.79 | 8.89 | 498.54 | 0.07 | 2.00 | 1561 |

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
| 3222822 | 2 | 121.4651905890 | 31.1451451948 | 264 | 11 | 12 | 48.7 | TDD | 131 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3234432 | 1 | 121.4707616006 | 31.1548175547 | 178 | 3 | 7 | 48.0 | TDD | 70 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3235192 | 4 | 121.4697203726 | 31.1521467775 | 1 | 1 | 7 | 17.5 | TDD | 670 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3254419 | 3 | 121.4742385300 | 31.1491535957 | 324 | 4 | 7 | 28.4 | TDD | 974 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.891 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.911 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.040 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.040 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.756 | NREventA3 | measId:2;ServCellPCI:530;Se... |
| 2024-09-20 22:21:37.996 | NRHandoverAttempt | SourcePCI:530;SourceNR-ARFC... |
| 2024-09-20 22:21:38.045 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.059 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.172 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.172 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234432 | 1 | 76.4440 | 94.0713 | -115.9948 | 5.3167 | 102.7877 | 0.0064 | 0.0172 |
| 2024_09_20 22:00 | 3222822 | 2 | 11.6005 | 16.6133 | -115.0908 | 16.8589 | 127.8485 | 0.0044 | 0.0064 |
| 2024_09_20 22:00 | 3254419 | 3 | 17.1158 | 13.3391 | -115.8606 | 16.4259 | 191.4219 | 0.0008 | 0.0149 |
| 2024_09_20 22:00 | 3235192 | 4 | 16.1250 | 17.3145 | -114.2452 | 17.0818 | 150.3042 | 0.0198 | 0.0168 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415529_0CCC6E9E | 504990 | 70 | -92.3 | 504990 | 131 | -95.2 | 504990 | 974 | -100.3 | 504990 | 670 |
| MR_1774415529_76D43082 | 504990 | 70 | -90.8 | 504990 | 131 | -94.9 | 504990 | 974 | -102.0 | 504990 | 670 |
| MR_1774415529_534BC82F | 504990 | 70 | -91.6 | 504990 | 131 | -95.8 | 504990 | 974 | -100.8 | 504990 | 670 |
| MR_1774415529_A8139D67 | 504990 | 70 | -92.8 | 504990 | 131 | -96.7 | 504990 | 974 | -99.0 | 504990 | 670 |
| MR_1774415529_4505861C | 504990 | 70 | -89.5 | 504990 | 131 | -97.6 | 504990 | 974 | -102.9 | 504990 | 670 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 404: `a43a8de8-536...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a43a8de8-536c-454a-9cbf-0b8b3f113112` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213756_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[404] topology](images/train_0404.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3276247_6
- `C2`: Increase A3 Offset threshold for 3213756_5
- `C3`: Decrease A3 Offset threshold for 3213756_5
- `C4`: Press down the tilt angle  of 3276247_6 by 5 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213756_5
- `C6`: Add neighbor relationship between 3234671_7 and 3276247_6
- `C7`: Add neighbor relationship between 3213756_5 and 3276247_6
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213756_5 **← 정답**
- `C9`: Press down the tilt angle of 3213756_5 by 6 degrees
- `C10`: Increase transmission power for 3276247_6
- `C11`: Lift the tilt angle  of 3276247_6 by 5 degrees
- `C12`: Decrease transmission power for 3213756_5
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Adjust the azimuth of 3276247_6 by 23 degrees
- `C15`: Lift the tilt angle of 3213756_5 by 6 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276247_6
- `C17`: Increase A3 Offset threshold for 3276247_6
- `C18`: Check test server and transmission issues
- `C19`: Increase transmission power for 3213756_5
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276247_6
- `C21`: Adjust the azimuth of 3213756_5 by 5 degrees
- `C22`: Decrease transmission power for 3276247_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.870 | MS1 | 121.4656694412 | 31.1446224739 | 756 | 504990 | -93.19 | 11.02 | 565.12 | 0.00 | 2.03 | 1573 |
| 2024-09-20 22:21:32.994 | MS1 | 121.4656671443 | 31.1446299546 | 425 | 504990 | -94.95 | 12.44 | 309.83 | 0.15 | 2.29 | 1580 |
| 2024-09-20 22:21:33.537 | MS1 | 121.4656747113 | 31.1446245505 | 692 | 504990 | -95.38 | 12.17 | 583.11 | 0.05 | 2.08 | 1598 |
| 2024-09-20 22:21:34.118 | MS1 | 121.4656663251 | 31.1446216683 | 315 | 152650 | -89.18 | 2.14 | 78.61 | 0.04 | 1.92 | 901 |
| 2024-09-20 22:21:35.551 | MS1 | 121.4656735302 | 31.1446331724 | 238 | 152650 | -93.91 | 6.58 | 83.97 | 0.05 | 1.68 | 948 |
| 2024-09-20 22:21:36.215 | MS1 | 121.4656692034 | 31.1446223360 | 420 | 152650 | -96.11 | 2.54 | 59.82 | 0.07 | 1.83 | 962 |
| 2024-09-20 22:21:37.352 | MS1 | 121.4656583782 | 31.1446311369 | 885 | 152650 | -92.58 | 5.46 | 52.81 | 0.12 | 1.90 | 920 |
| 2024-09-20 22:21:38.978 | MS1 | 121.4656642173 | 31.1446321896 | 315 | 152650 | -93.21 | 7.81 | 84.87 | 0.11 | 1.99 | 943 |
| 2024-09-20 22:21:39.576 | MS1 | 121.4656715167 | 31.1446282750 | 238 | 152650 | -94.34 | 6.31 | 86.78 | 0.05 | 1.97 | 900 |
| 2024-09-20 22:21:40.159 | MS1 | 121.4656741288 | 31.1446346499 | 420 | 152650 | -96.30 | 4.96 | 84.31 | 0.12 | 2.91 | 1561 |
| 2024-09-20 22:21:41.126 | MS1 | 121.4656643823 | 31.1446315677 | 885 | 152650 | -94.45 | 6.86 | 53.97 | 0.04 | 2.34 | 1588 |
| 2024-09-20 22:21:42.792 | MS1 | 121.4656761203 | 31.1446180591 | 315 | 152650 | -95.34 | 5.57 | 57.27 | 0.10 | 2.16 | 1584 |

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
| 3213756 | 5 | 121.4664154142 | 31.1484971797 | 185 | 4 | 0 | 15.0 | TDD | 756 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3216107 | 13 | 121.4668591474 | 31.1524123920 | 335 | 3 | 5 | 19.1 | FDD | 61 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3220898 | 10 | 121.4759827428 | 31.1502802152 | 110 | 12 | 10 | 16.7 | FDD | 787 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3222526 | 8 | 121.4709625896 | 31.1443674585 | 268 | 6 | 1 | 4.3 | FDD | 426 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3228156 | 9 | 121.4642399517 | 31.1536737890 | 217 | 2 | 9 | 18.6 | FDD | 238 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3233632 | 11 | 121.4754279527 | 31.1472798478 | 194 | 14 | 0 | 29.3 | FDD | 885 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3234671 | 7 | 121.4657065107 | 31.1460836533 | 176 | 9 | 4 | 8.9 | FDD | 420 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3255650 | 1 | 121.4661598857 | 31.1486160512 | 113 | 8 | 10 | 5.4 | TDD | 425 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3265453 | 3 | 121.4756863120 | 31.1449043711 | 111 | 3 | 4 | 28.9 | TDD | 49 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3274484 | 12 | 121.4677315824 | 31.1536202579 | 38 | 13 | 10 | 1.9 | FDD | 315 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3276247 | 6 | 121.4723729676 | 31.1524341010 | 193 | 4 | 4 | 11.0 | TDD | 798 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3276334 | 4 | 121.4705960644 | 31.1540592691 | 98 | 6 | 3 | 15.9 | TDD | 692 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3276858 | 2 | 121.4714843474 | 31.1502715610 | 329 | 3 | 1 | 29.6 | TDD | 430 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.112 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.127 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.227 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.227 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.986 | NREventA2 | measId:1;ServCellPCI:18;Ser... |
| 2024-09-20 22:21:35.101 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.384 | NREventA5 | measId:3;ServCellPCI:18;Ser... |
| 2024-09-20 22:21:35.426 | NRHandoverAttempt | SourcePCI:18;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.466 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.479 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.587 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.587 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255650 | 1 | 13.7595 | 17.8776 | -115.1995 | 11.9013 | 141.2759 | 0.0066 | 0.0130 |
| 2024_09_20 22:00 | 3276858 | 2 | 18.4822 | 12.7438 | -115.5370 | 12.7727 | 190.2111 | 0.0185 | 0.0155 |
| 2024_09_20 22:00 | 3265453 | 3 | 19.0453 | 9.7944 | -117.1912 | 15.3092 | 169.9403 | 0.0018 | 0.0093 |
| 2024_09_20 22:00 | 3276334 | 4 | 14.7137 | 16.6776 | -116.0099 | 18.8276 | 136.1946 | 0.0058 | 0.0175 |
| 2024_09_20 22:00 | 3213756 | 5 | 10.9701 | 16.0441 | -115.8398 | 18.1483 | 107.0962 | 0.0126 | 0.0061 |
| 2024_09_20 22:00 | 3276247 | 6 | 7.0500 | 17.8811 | -114.5276 | 15.4892 | 88.5028 | 0.0200 | 0.0163 |
| 2024_09_20 22:00 | 3234671 | 7 | 6.3253 | 18.1747 | -116.8935 | 4.1151 | 27.8342 | 0.0102 | 0.0006 |
| 2024_09_20 22:00 | 3222526 | 8 | 10.8909 | 17.5340 | -116.3195 | 4.4515 | 29.9746 | 0.0014 | 0.0005 |
| 2024_09_20 22:00 | 3228156 | 9 | 5.5610 | 11.7932 | -114.4277 | 3.1538 | 27.2176 | 0.0043 | 0.0102 |
| 2024_09_20 22:00 | 3220898 | 10 | 6.4959 | 19.6277 | -117.7283 | 4.7231 | 45.5474 | 0.0088 | 0.0077 |
| 2024_09_20 22:00 | 3233632 | 11 | 14.4945 | 7.3593 | -115.5945 | 3.5026 | 27.9585 | 0.0041 | 0.0064 |
| 2024_09_20 22:00 | 3274484 | 12 | 11.4156 | 7.2523 | -115.4134 | 4.6664 | 24.7797 | 0.0104 | 0.0021 |
| 2024_09_20 22:00 | 3216107 | 13 | 9.4897 | 12.8962 | -115.2925 | 3.9633 | 28.5029 | 0.0051 | 0.0198 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414862_5F31D5FE | 152650 | 315 | -90.1 | 152650 | 787 | -94.0 | 152650 | 426 | -96.3 | 152650 | 61 |
| MR_1774414862_F9CEFE01 | 152650 | 315 | -87.4 | 152650 | 787 | -96.1 | 152650 | 426 | -97.9 | 152650 | 61 |
| MR_1774414862_355977E5 | 504990 | 692 | -96.5 | 504990 | 798 | -91.2 | 504990 | 430 | -94.2 | 504990 | 49 |
| MR_1774414862_A32AA191 | 152650 | 315 | -88.5 | 152650 | 787 | -92.7 | 152650 | 426 | -97.3 | 152650 | 61 |
| MR_1774414862_CD107535 | 152650 | 315 | -90.0 | 152650 | 787 | -93.7 | 152650 | 426 | -96.8 | 152650 | 61 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 405: `7da66ddc-4a2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7da66ddc-4a28-4c39-becc-23dd53c719f1` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Add neighbor relationship between 3234305_1 and 3265803_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[405] topology](images/train_0405.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3234305_1 by 10 degrees
- `C2`: Lift the tilt angle of 3234305_1 by 10 degrees
- `C3`: Add neighbor relationship between 3234305_1 and 3265803_4 **← 정답**
- `C4`: Add neighbor relationship between 3223612_2 and 3265803_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234305_1
- `C6`: Press down the tilt angle  of 3265803_4 by 5 degrees
- `C7`: Decrease A3 Offset threshold for 3265803_4
- `C8`: Increase A3 Offset threshold for 3234305_1
- `C9`: Check test server and transmission issues
- `C10`: Adjust the azimuth of 3234305_1 by 50 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Lift the tilt angle  of 3265803_4 by 5 degrees
- `C13`: Increase transmission power for 3265803_4
- `C14`: Increase A3 Offset threshold for 3265803_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265803_4
- `C16`: Increase transmission power for 3234305_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265803_4
- `C18`: Decrease A3 Offset threshold for 3234305_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234305_1
- `C20`: Decrease transmission power for 3265803_4
- `C21`: Decrease transmission power for 3234305_1
- `C22`: Adjust the azimuth of 3265803_4 by 23 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.633 | MS1 | 121.4656677874 | 31.1446291201 | 297 | 504990 | -76.80 | 14.62 | 312.70 | 0.19 | 2.67 | 1586 |
| 2024-09-20 22:21:32.241 | MS1 | 121.4656647345 | 31.1446201485 | 297 | 504990 | -81.99 | 15.62 | 559.35 | 0.07 | 2.87 | 1600 |
| 2024-09-20 22:21:33.504 | MS1 | 121.4656698166 | 31.1446311654 | 297 | 504990 | -79.85 | 12.92 | 587.74 | 0.01 | 3.00 | 1583 |
| 2024-09-20 22:21:34.219 | MS1 | 121.4656697871 | 31.1446272700 | 297 | 504990 | -85.60 | -2.31 | 26.20 | 0.18 | 1.20 | 1569 |
| 2024-09-20 22:21:35.579 | MS1 | 121.4656774785 | 31.1446245635 | 297 | 504990 | -85.24 | -0.54 | 39.88 | 0.19 | 1.15 | 1571 |
| 2024-09-20 22:21:36.254 | MS1 | 121.4656769774 | 31.1446184257 | 297 | 504990 | -86.46 | -1.20 | 43.99 | 0.13 | 1.36 | 1570 |
| 2024-09-20 22:21:37.227 | MS1 | 121.4656632306 | 31.1446185372 | 297 | 504990 | -85.41 | -2.45 | 41.51 | 0.01 | 1.39 | 1582 |
| 2024-09-20 22:21:38.960 | MS1 | 121.4656703540 | 31.1446350574 | 297 | 504990 | -75.59 | 16.17 | 600.33 | 0.00 | 1.22 | 1578 |
| 2024-09-20 22:21:39.278 | MS1 | 121.4656680267 | 31.1446214392 | 297 | 504990 | -81.52 | 17.58 | 551.44 | 0.17 | 1.04 | 1584 |
| 2024-09-20 22:21:40.959 | MS1 | 121.4656587497 | 31.1446214478 | 297 | 504990 | -78.74 | 14.45 | 316.57 | 0.00 | 2.21 | 1587 |
| 2024-09-20 22:21:41.310 | MS1 | 121.4656665741 | 31.1446262623 | 297 | 504990 | -83.71 | 15.26 | 491.43 | 0.02 | 2.08 | 1566 |
| 2024-09-20 22:21:42.821 | MS1 | 121.4656635754 | 31.1446379550 | 297 | 504990 | -82.45 | 12.90 | 396.58 | 0.19 | 2.27 | 1585 |

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
| 3212457 | 3 | 121.4718635391 | 31.1547046039 | 16 | 12 | 10 | 17.7 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3223612 | 2 | 121.4668472172 | 31.1520435590 | 185 | 3 | 0 | 15.4 | TDD | 331 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3234305 | 1 | 121.4671186423 | 31.1493993227 | 4 | 10 | 11 | 30.7 | TDD | 297 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3265803 | 4 | 121.4756560328 | 31.1470933117 | 231 | 3 | 2 | 36.5 | TDD | 701 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.614 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.631 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.754 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.754 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.474 | NREventA3 | measId:2;ServCellPCI:267;Se... |
| 2024-09-20 22:21:36.474 | NREventA3 | measId:2;ServCellPCI:267;Se... |
| 2024-09-20 22:21:37.474 | NREventA3 | measId:2;ServCellPCI:267;Se... |
| 2024-09-20 22:21:39.974 | NRRRCReestablishAttempt | PCI:267 |
| 2024-09-20 22:21:39.994 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:40.004 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:40.124 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.124 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234305 | 1 | 16.9185 | 19.0265 | -114.8691 | 13.8555 | 115.6224 | 0.0009 | 0.1331 |
| 2024_09_20 22:00 | 3223612 | 2 | 16.0041 | 12.5814 | -114.2687 | 10.9853 | 185.6972 | 0.0153 | 0.0193 |
| 2024_09_20 22:00 | 3212457 | 3 | 6.8414 | 13.4954 | -114.9057 | 8.2445 | 132.0264 | 0.0143 | 0.0195 |
| 2024_09_20 22:00 | 3265803 | 4 | 15.3474 | 10.0433 | -116.9823 | 5.8513 | 177.2736 | 0.0200 | 0.0008 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414908_05E8B882 | 504990 | 297 | -84.2 | 504990 | 701 | -79.5 | 504990 | 331 | -91.3 | 504990 | 355 |
| MR_1774414908_11F60266 | 504990 | 701 | -78.8 | 504990 | 297 | -85.4 | 504990 | 331 | -88.6 | 504990 | 355 |
| MR_1774414908_A6264571 | 504990 | 297 | -84.9 | 504990 | 701 | -80.1 | 504990 | 331 | -91.5 | 504990 | 355 |
| MR_1774414908_01A8467A | 504990 | 701 | -80.0 | 504990 | 297 | -87.2 | 504990 | 331 | -89.6 | 504990 | 355 |
| MR_1774414908_E02FB478 | 504990 | 701 | -78.5 | 504990 | 297 | -85.8 | 504990 | 331 | -91.3 | 504990 | 355 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 406: `53a67654-1fe...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `53a67654-1fe5-4da7-a1d2-398b053b07ca` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3217382_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[406] topology](images/train_0406.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease transmission power for 3217382_1
- `C3`: Decrease transmission power for 3216296_4
- `C4`: Press down the tilt angle of 3217382_1 by 2 degrees
- `C5`: Adjust the azimuth of 3217382_1 by 13 degrees
- `C6`: Increase transmission power for 3216296_4
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217382_1
- `C9`: Adjust the azimuth of 3216296_4 by 50 degrees
- `C10`: Increase A3 Offset threshold for 3216296_4
- `C11`: Lift the tilt angle  of 3216296_4 by 2 degrees
- `C12`: Decrease A3 Offset threshold for 3217382_1
- `C13`: Decrease A3 Offset threshold for 3216296_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217382_1 **← 정답**
- `C15`: Press down the tilt angle  of 3216296_4 by 2 degrees
- `C16`: Increase transmission power for 3217382_1
- `C17`: Increase A3 Offset threshold for 3217382_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216296_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216296_4
- `C20`: Add neighbor relationship between 3217382_1 and 3216296_4
- `C21`: Add neighbor relationship between 3251749_3 and 3216296_4
- `C22`: Lift the tilt angle of 3217382_1 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.158 | MS1 | 121.4656717465 | 31.1446257985 | 674 | 504990 | -86.29 | 12.43 | 413.72 | 0.10 | 2.71 | 1577 |
| 2024-09-20 22:21:32.949 | MS1 | 121.4656630351 | 31.1446242153 | 674 | 504990 | -90.97 | 14.96 | 500.47 | 0.17 | 2.07 | 1580 |
| 2024-09-20 22:21:33.206 | MS1 | 121.4656712275 | 31.1446359947 | 674 | 504990 | -88.15 | 15.22 | 550.90 | 0.06 | 2.12 | 1600 |
| 2024-09-20 22:21:34.475 | MS1 | 121.4656606009 | 31.1446296527 | 674 | 504990 | -85.55 | 12.83 | 92.32 | 0.53 | 2.58 | 553 |
| 2024-09-20 22:21:35.965 | MS1 | 121.4656603878 | 31.1446197285 | 674 | 504990 | -86.66 | 17.88 | 67.60 | 0.55 | 2.89 | 502 |
| 2024-09-20 22:21:36.130 | MS1 | 121.4656631637 | 31.1446298405 | 674 | 504990 | -87.60 | 13.41 | 71.97 | 0.62 | 2.72 | 548 |
| 2024-09-20 22:21:37.180 | MS1 | 121.4656670455 | 31.1446273571 | 674 | 504990 | -89.99 | 11.14 | 96.32 | 0.62 | 2.82 | 694 |
| 2024-09-20 22:21:38.261 | MS1 | 121.4656662368 | 31.1446264830 | 674 | 504990 | -92.16 | 12.43 | 83.52 | 0.63 | 2.20 | 695 |
| 2024-09-20 22:21:39.670 | MS1 | 121.4656754342 | 31.1446379037 | 674 | 504990 | -90.71 | 8.47 | 61.61 | 0.51 | 2.89 | 561 |
| 2024-09-20 22:21:40.366 | MS1 | 121.4656611074 | 31.1446262902 | 674 | 504990 | -93.72 | 11.74 | 523.45 | 0.04 | 2.47 | 1594 |
| 2024-09-20 22:21:41.887 | MS1 | 121.4656620604 | 31.1446229414 | 674 | 504990 | -89.35 | 12.49 | 518.22 | 0.12 | 2.48 | 1585 |
| 2024-09-20 22:21:42.848 | MS1 | 121.4656646569 | 31.1446233242 | 674 | 504990 | -93.01 | 11.36 | 608.41 | 0.16 | 2.08 | 1582 |

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
| 3216296 | 4 | 121.4679042084 | 31.1528019976 | 349 | 0 | 1 | 26.8 | TDD | 230 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3217382 | 1 | 121.4658620479 | 31.1512661137 | 194 | 0 | 9 | 19.9 | TDD | 674 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3246511 | 2 | 121.4684287890 | 31.1531896226 | 99 | 12 | 5 | 36.7 | TDD | 778 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3251749 | 3 | 121.4697238092 | 31.1495110194 | 269 | 11 | 8 | 25.5 | TDD | 979 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.047 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.066 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.167 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.167 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.872 | NREventA3 | measId:2;ServCellPCI:355;Se... |
| 2024-09-20 22:21:38.112 | NRHandoverAttempt | SourcePCI:355;SourceNR-ARFC... |
| 2024-09-20 22:21:38.161 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.173 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.284 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.284 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217382 | 1 | 9.7291 | 6.2014 | -114.4174 | 13.4437 | 186.0191 | 0.0091 | 0.0193 |
| 2024_09_20 22:00 | 3246511 | 2 | 11.4104 | 5.2924 | -114.5447 | 19.5544 | 143.6763 | 0.0047 | 0.0165 |
| 2024_09_20 22:00 | 3251749 | 3 | 16.0959 | 7.2942 | -116.9985 | 6.3972 | 196.8191 | 0.0132 | 0.0096 |
| 2024_09_20 22:00 | 3216296 | 4 | 13.0585 | 18.0007 | -117.9387 | 18.1547 | 80.2513 | 0.0001 | 0.0146 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414197_AD45B57A | 504990 | 674 | -84.7 | 504990 | 230 | -92.4 | 504990 | 979 | -91.5 | 504990 | 778 |
| MR_1774414197_5DE0C528 | 504990 | 674 | -84.4 | 504990 | 230 | -91.4 | 504990 | 979 | -94.3 | 504990 | 778 |
| MR_1774414197_08F208EB | 504990 | 674 | -85.1 | 504990 | 230 | -92.1 | 504990 | 979 | -92.7 | 504990 | 778 |
| MR_1774414197_93261838 | 504990 | 674 | -85.4 | 504990 | 230 | -92.3 | 504990 | 979 | -91.8 | 504990 | 778 |
| MR_1774414197_75659EE9 | 504990 | 674 | -83.6 | 504990 | 230 | -90.9 | 504990 | 979 | -93.9 | 504990 | 778 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 407: `e2719360-d7f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e2719360-d7f6-4df9-8c89-71fadc46bb9d` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Lift the tilt angle  of 3213383_3 by 6 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[407] topology](images/train_0407.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264579_2
- `C2`: Increase A3 Offset threshold for 3264579_2
- `C3`: Adjust the azimuth of 3213383_3 by 50 degrees
- `C4`: Lift the tilt angle  of 3213383_3 by 6 degrees **← 정답**
- `C5`: Lift the tilt angle of 3264579_2 by 4 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease transmission power for 3263057_1
- `C8`: Increase A3 Offset threshold for 3263057_1
- `C9`: Increase transmission power for 3263057_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264579_2
- `C11`: Check test server and transmission issues
- `C12`: Decrease transmission power for 3264579_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263057_1
- `C14`: Press down the tilt angle of 3264579_2 by 4 degrees
- `C15`: Increase transmission power for 3264579_2
- `C16`: Add neighbor relationship between 3264579_2 and 3263057_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263057_1
- `C18`: Decrease A3 Offset threshold for 3263057_1
- `C19`: Decrease A3 Offset threshold for 3264579_2
- `C20`: Adjust the azimuth of 3264579_2 by 28 degrees
- `C21`: Press down the tilt angle  of 3213383_3 by 6 degrees
- `C22`: Add neighbor relationship between 3213383_3 and 3263057_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.132 | MS1 | 121.4656602921 | 31.1446233907 | 211 | 504990 | -86.92 | 13.96 | 308.88 | 0.01 | 2.40 | 1565 |
| 2024-09-20 22:21:32.233 | MS1 | 121.4656609533 | 31.1446280148 | 211 | 504990 | -86.22 | 14.58 | 406.81 | 0.15 | 2.68 | 1587 |
| 2024-09-20 22:21:33.852 | MS1 | 121.4656682977 | 31.1446278149 | 211 | 504990 | -90.57 | 15.97 | 385.68 | 0.01 | 2.18 | 1585 |
| 2024-09-20 22:21:34.800 | MS1 | 121.4656705526 | 31.1446196580 | 211 | 504990 | -85.09 | 14.37 | 99.19 | 0.10 | 2.65 | 1579 |
| 2024-09-20 22:21:35.531 | MS1 | 121.4656717364 | 31.1446322728 | 211 | 504990 | -89.33 | 14.93 | 86.66 | 0.07 | 2.11 | 1579 |
| 2024-09-20 22:21:36.923 | MS1 | 121.4656738912 | 31.1446189746 | 211 | 504990 | -88.89 | 16.94 | 66.60 | 0.20 | 2.14 | 1589 |
| 2024-09-20 22:21:37.348 | MS1 | 121.4656776258 | 31.1446200734 | 211 | 504990 | -90.96 | 9.05 | 75.87 | 0.01 | 2.87 | 1560 |
| 2024-09-20 22:21:38.256 | MS1 | 121.4656685125 | 31.1446206228 | 211 | 504990 | -90.62 | 7.86 | 80.46 | 0.09 | 2.30 | 1598 |
| 2024-09-20 22:21:39.248 | MS1 | 121.4656674772 | 31.1446252074 | 211 | 504990 | -93.94 | 8.69 | 72.87 | 0.15 | 2.31 | 1600 |
| 2024-09-20 22:21:40.416 | MS1 | 121.4656662070 | 31.1446245056 | 211 | 504990 | -93.32 | 8.29 | 355.40 | 0.14 | 2.47 | 1574 |
| 2024-09-20 22:21:41.470 | MS1 | 121.4656746873 | 31.1446214228 | 211 | 504990 | -91.27 | 7.83 | 551.72 | 0.01 | 2.70 | 1567 |
| 2024-09-20 22:21:42.971 | MS1 | 121.4656774739 | 31.1446320172 | 211 | 504990 | -90.87 | 11.84 | 499.44 | 0.11 | 2.31 | 1592 |

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
| 3210292 | 4 | 121.4724643807 | 31.1468179430 | 186 | 10 | 8 | 19.8 | TDD | 377 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3213383 | 3 | 121.4733818082 | 31.1538248536 | 31 | 2 | 0 | 23.5 | TDD | 852 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3263057 | 1 | 121.4691138443 | 31.1461596862 | 171 | 0 | 4 | 37.0 | TDD | 617 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3264579 | 2 | 121.4737871700 | 31.1535692895 | 190 | 2 | 1 | 38.4 | TDD | 211 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.467 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.484 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.634 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.634 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.290 | NREventA3 | measId:2;ServCellPCI:256;Se... |
| 2024-09-20 22:21:38.530 | NRHandoverAttempt | SourcePCI:256;SourceNR-ARFC... |
| 2024-09-20 22:21:38.565 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.580 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.687 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.687 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263057 | 1 | 12.8015 | 9.4051 | -114.1670 | 5.5895 | 129.3031 | 0.0081 | 0.0072 |
| 2024_09_20 22:00 | 3264579 | 2 | 92.5429 | 75.6753 | -116.2277 | 13.4894 | 129.3278 | 0.0187 | 0.0076 |
| 2024_09_20 22:00 | 3213383 | 3 | 10.6797 | 19.8816 | -116.4911 | 10.5286 | 131.2496 | 0.0190 | 0.0000 |
| 2024_09_20 22:00 | 3210292 | 4 | 18.0450 | 9.2891 | -116.1913 | 6.5742 | 120.0388 | 0.0033 | 0.0112 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416231_03B81D44 | 504990 | 211 | -85.2 | 504990 | 617 | -85.2 | 504990 | 852 | -99.5 | 504990 | 377 |
| MR_1774416231_583A0FDC | 504990 | 211 | -85.7 | 504990 | 617 | -85.7 | 504990 | 852 | -96.2 | 504990 | 377 |
| MR_1774416231_9D26CDC3 | 504990 | 211 | -84.0 | 504990 | 617 | -86.3 | 504990 | 852 | -96.7 | 504990 | 377 |
| MR_1774416231_4AD215C6 | 504990 | 211 | -85.7 | 504990 | 617 | -83.3 | 504990 | 852 | -95.9 | 504990 | 377 |
| MR_1774416231_83998BAB | 504990 | 211 | -83.7 | 504990 | 617 | -86.6 | 504990 | 852 | -99.2 | 504990 | 377 |
| MR_1774416231_E3DC4503 | 504990 | 211 | -83.3 | 504990 | 617 | -84.2 | 504990 | 852 | -98.5 | 504990 | 377 |
| MR_1774416231_00A588EF | 504990 | 211 | -84.3 | 504990 | 617 | -84.8 | 504990 | 852 | -99.7 | 504990 | 377 |
| MR_1774416231_9911430B | 504990 | 211 | -86.1 | 504990 | 617 | -85.2 | 504990 | 852 | -97.1 | 504990 | 377 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 408: `827d13a1-a31...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `827d13a1-a31d-4c34-8e9b-153998c7b25b` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[408] topology](images/train_0408.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3233952_1
- `C2`: Lift the tilt angle of 3233952_1 by 10 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Adjust the azimuth of 3277250_3 by 26 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277250_3
- `C6`: Increase A3 Offset threshold for 3277250_3
- `C7`: Press down the tilt angle of 3233952_1 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3277250_3
- `C9`: Add neighbor relationship between 3233952_1 and 3277250_3
- `C10`: Press down the tilt angle  of 3277250_3 by 10 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277250_3
- `C12`: Decrease A3 Offset threshold for 3233952_1
- `C13`: Increase transmission power for 3277250_3
- `C14`: Add neighbor relationship between 3252749_4 and 3277250_3
- `C15`: Adjust the azimuth of 3233952_1 by 50 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233952_1
- `C17`: Lift the tilt angle  of 3277250_3 by 10 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233952_1
- `C19`: Decrease transmission power for 3277250_3
- `C20`: Check test server and transmission issues **← 정답**
- `C21`: Increase A3 Offset threshold for 3233952_1
- `C22`: Decrease transmission power for 3233952_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.409 | MS1 | 121.4656616415 | 31.1446205543 | 647 | 504990 | -89.55 | 13.96 | 364.21 | 0.20 | 2.66 | 1580 |
| 2024-09-20 22:21:32.242 | MS1 | 121.4656598748 | 31.1446347170 | 647 | 504990 | -86.35 | 16.13 | 511.36 | 0.03 | 2.63 | 1560 |
| 2024-09-20 22:21:33.692 | MS1 | 121.4656707903 | 31.1446265350 | 647 | 504990 | -91.96 | 13.42 | 425.91 | 0.12 | 2.41 | 1582 |
| 2024-09-20 22:21:34.269 | MS1 | 121.4656675938 | 31.1446375728 | 647 | 504990 | -89.32 | 14.86 | 55.80 | 0.05 | 2.42 | 444 |
| 2024-09-20 22:21:35.796 | MS1 | 121.4656715350 | 31.1446216951 | 647 | 504990 | -88.52 | 12.74 | 61.76 | 0.03 | 2.34 | 397 |
| 2024-09-20 22:21:36.471 | MS1 | 121.4656644085 | 31.1446372995 | 647 | 504990 | -89.66 | 12.19 | 79.81 | 0.16 | 2.31 | 495 |
| 2024-09-20 22:21:37.425 | MS1 | 121.4656757701 | 31.1446293726 | 647 | 504990 | -92.83 | 7.29 | 50.73 | 0.12 | 2.77 | 454 |
| 2024-09-20 22:21:38.708 | MS1 | 121.4656761027 | 31.1446350867 | 647 | 504990 | -92.16 | 9.90 | 66.88 | 0.01 | 2.41 | 500 |
| 2024-09-20 22:21:39.895 | MS1 | 121.4656637248 | 31.1446354760 | 647 | 504990 | -93.91 | 8.27 | 85.76 | 0.12 | 2.18 | 489 |
| 2024-09-20 22:21:40.933 | MS1 | 121.4656693180 | 31.1446367322 | 647 | 504990 | -91.11 | 8.76 | 397.53 | 0.10 | 2.97 | 1579 |
| 2024-09-20 22:21:41.986 | MS1 | 121.4656778634 | 31.1446251893 | 647 | 504990 | -92.40 | 7.38 | 373.61 | 0.05 | 2.84 | 1599 |
| 2024-09-20 22:21:42.240 | MS1 | 121.4656652051 | 31.1446198062 | 647 | 504990 | -92.86 | 11.98 | 339.72 | 0.17 | 2.17 | 1562 |

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
| 3233952 | 1 | 121.4682288820 | 31.1527350592 | 118 | 10 | 8 | 24.0 | TDD | 647 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3252749 | 4 | 121.4641318743 | 31.1527066693 | 338 | 3 | 11 | 27.5 | TDD | 879 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3269180 | 2 | 121.4687551632 | 31.1537269136 | 197 | 15 | 9 | 26.5 | TDD | 393 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3277250 | 3 | 121.4676063522 | 31.1528678607 | 165 | 14 | 10 | 24.3 | TDD | 446 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.386 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.406 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.556 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.556 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.283 | NREventA3 | measId:2;ServCellPCI:784;Se... |
| 2024-09-20 22:21:38.523 | NRHandoverAttempt | SourcePCI:784;SourceNR-ARFC... |
| 2024-09-20 22:21:38.553 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.567 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.714 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.714 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233952 | 1 | 13.1668 | 15.2286 | -116.7787 | 14.5348 | 148.6058 | 0.0133 | 0.0046 |
| 2024_09_20 22:00 | 3269180 | 2 | 19.1499 | 5.7828 | -115.2912 | 13.2299 | 152.9398 | 0.0132 | 0.0122 |
| 2024_09_20 22:00 | 3277250 | 3 | 16.2084 | 5.4121 | -116.2928 | 16.0228 | 128.1243 | 0.0199 | 0.0170 |
| 2024_09_20 22:00 | 3252749 | 4 | 18.1305 | 17.6395 | -117.2970 | 17.6740 | 166.8624 | 0.0015 | 0.0105 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414472_EB0D219D | 504990 | 647 | -87.8 | 504990 | 446 | -92.7 | 504990 | 879 | -99.5 | 504990 | 393 |
| MR_1774414472_6BE8C3EC | 504990 | 647 | -89.4 | 504990 | 446 | -93.5 | 504990 | 879 | -99.3 | 504990 | 393 |
| MR_1774414472_61408D83 | 504990 | 647 | -87.8 | 504990 | 446 | -95.5 | 504990 | 879 | -101.9 | 504990 | 393 |
| MR_1774414472_0B28EAEF | 504990 | 647 | -91.0 | 504990 | 446 | -92.0 | 504990 | 879 | -99.7 | 504990 | 393 |
| MR_1774414472_9F93E665 | 504990 | 647 | -87.6 | 504990 | 446 | -93.3 | 504990 | 879 | -101.8 | 504990 | 393 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 409: `06064651-752...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `06064651-752f-4c5f-b1e9-cdf78e9525f5` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244233_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[409] topology](images/train_0409.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3231586_4
- `C2`: Check test server and transmission issues
- `C3`: Decrease transmission power for 3244233_5
- `C4`: Adjust the azimuth of 3231586_4 by 14 degrees
- `C5`: Increase A3 Offset threshold for 3244233_5
- `C6`: Adjust the azimuth of 3244233_5 by 45 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231586_4
- `C8`: Increase transmission power for 3231586_4
- `C9`: Add neighbor relationship between 3216820_12 and 3231586_4
- `C10`: Lift the tilt angle  of 3231586_4 by 4 degrees
- `C11`: Decrease A3 Offset threshold for 3244233_5
- `C12`: Add neighbor relationship between 3244233_5 and 3231586_4
- `C13`: Decrease A3 Offset threshold for 3231586_4
- `C14`: Increase A3 Offset threshold for 3231586_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244233_5 **← 정답**
- `C16`: Press down the tilt angle  of 3231586_4 by 4 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase transmission power for 3244233_5
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231586_4
- `C20`: Press down the tilt angle of 3244233_5 by 0 degrees
- `C21`: Lift the tilt angle of 3244233_5 by 0 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244233_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.604 | MS1 | 121.4656649104 | 31.1446279927 | 953 | 504990 | -94.80 | 9.57 | 408.04 | 0.02 | 2.46 | 1598 |
| 2024-09-20 22:21:32.763 | MS1 | 121.4656590499 | 31.1446346801 | 986 | 504990 | -94.74 | 12.56 | 383.00 | 0.17 | 2.46 | 1593 |
| 2024-09-20 22:21:33.880 | MS1 | 121.4656759010 | 31.1446373210 | 513 | 504990 | -95.13 | 13.74 | 541.23 | 0.03 | 2.31 | 1594 |
| 2024-09-20 22:21:34.856 | MS1 | 121.4656714354 | 31.1446238051 | 484 | 152650 | -91.19 | 6.18 | 60.29 | 0.06 | 1.69 | 945 |
| 2024-09-20 22:21:35.752 | MS1 | 121.4656778753 | 31.1446188117 | 120 | 152650 | -87.32 | 2.46 | 94.97 | 0.00 | 1.62 | 943 |
| 2024-09-20 22:21:36.710 | MS1 | 121.4656769197 | 31.1446302481 | 54 | 152650 | -93.88 | 4.70 | 102.94 | 0.11 | 1.62 | 939 |
| 2024-09-20 22:21:37.830 | MS1 | 121.4656646031 | 31.1446344735 | 229 | 152650 | -95.55 | 6.88 | 72.54 | 0.02 | 1.60 | 907 |
| 2024-09-20 22:21:38.366 | MS1 | 121.4656709207 | 31.1446197704 | 484 | 152650 | -92.95 | 6.80 | 51.03 | 0.16 | 1.87 | 922 |
| 2024-09-20 22:21:39.244 | MS1 | 121.4656592528 | 31.1446299768 | 120 | 152650 | -94.61 | 2.00 | 82.21 | 0.02 | 1.51 | 963 |
| 2024-09-20 22:21:40.516 | MS1 | 121.4656712729 | 31.1446181208 | 54 | 152650 | -91.34 | 7.19 | 82.20 | 0.11 | 2.82 | 1591 |
| 2024-09-20 22:21:41.798 | MS1 | 121.4656684916 | 31.1446284606 | 229 | 152650 | -92.32 | 6.58 | 73.12 | 0.03 | 2.88 | 1585 |
| 2024-09-20 22:21:42.727 | MS1 | 121.4656758655 | 31.1446350411 | 484 | 152650 | -92.62 | 2.08 | 84.98 | 0.18 | 2.41 | 1599 |

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
| 3210153 | 3 | 121.4641455000 | 31.1496212135 | 34 | 10 | 3 | 22.4 | TDD | 333 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3211184 | 13 | 121.4648132068 | 31.1559018737 | 216 | 12 | 3 | 14.6 | FDD | 120 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3214640 | 11 | 121.4664776147 | 31.1546700819 | 296 | 12 | 5 | 28.0 | FDD | 589 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3216820 | 12 | 121.4664167105 | 31.1520832708 | 31 | 5 | 2 | 5.5 | FDD | 54 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3221667 | 6 | 121.4697192092 | 31.1470900050 | 302 | 14 | 12 | 2.5 | TDD | 986 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3231586 | 4 | 121.4679412310 | 31.1552955476 | 176 | 3 | 11 | 23.1 | TDD | 984 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3239115 | 7 | 121.4653784120 | 31.1514911711 | 316 | 5 | 12 | 18.5 | FDD | 1 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3244233 | 5 | 121.4687048336 | 31.1542466836 | 240 | 0 | 5 | 0.2 | TDD | 953 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3246948 | 8 | 121.4648022386 | 31.1513467027 | 45 | 9 | 9 | 8.0 | FDD | 484 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3247486 | 1 | 121.4757774084 | 31.1543728987 | 77 | 7 | 10 | 12.3 | TDD | 161 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3247926 | 9 | 121.4685051884 | 31.1464421617 | 29 | 4 | 9 | 16.1 | FDD | 229 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3252997 | 2 | 121.4646318439 | 31.1466716284 | 171 | 1 | 9 | 23.2 | TDD | 513 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3272241 | 10 | 121.4733649417 | 31.1529074864 | 4 | 8 | 10 | 0.8 | FDD | 232 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |

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
| 2024-09-20 22:21:31.573 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.591 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.694 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.694 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.462 | NREventA2 | measId:1;ServCellPCI:259;Se... |
| 2024-09-20 22:21:35.583 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.811 | NREventA5 | measId:3;ServCellPCI:259;Se... |
| 2024-09-20 22:21:35.874 | NRHandoverAttempt | SourcePCI:259;SourceNR-ARFC... |
| 2024-09-20 22:21:35.919 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.932 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.067 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.067 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247486 | 1 | 6.8302 | 17.1323 | -116.7866 | 12.3429 | 140.6628 | 0.0106 | 0.0194 |
| 2024_09_20 22:00 | 3252997 | 2 | 15.0033 | 10.6097 | -114.3592 | 17.7868 | 85.5561 | 0.0015 | 0.0123 |
| 2024_09_20 22:00 | 3210153 | 3 | 10.5718 | 11.3281 | -117.4092 | 9.4895 | 147.1657 | 0.0107 | 0.0116 |
| 2024_09_20 22:00 | 3231586 | 4 | 7.4663 | 13.4519 | -117.7953 | 10.4138 | 150.4046 | 0.0176 | 0.0161 |
| 2024_09_20 22:00 | 3244233 | 5 | 17.8858 | 10.5280 | -114.6697 | 15.7241 | 183.3364 | 0.0003 | 0.0039 |
| 2024_09_20 22:00 | 3221667 | 6 | 11.0561 | 9.3227 | -116.7011 | 15.6900 | 135.3472 | 0.0099 | 0.0156 |
| 2024_09_20 22:00 | 3239115 | 7 | 15.7225 | 10.5681 | -117.6792 | 4.5432 | 50.1161 | 0.0076 | 0.0165 |
| 2024_09_20 22:00 | 3246948 | 8 | 16.0255 | 13.7771 | -114.3765 | 3.6660 | 23.9346 | 0.0121 | 0.0106 |
| 2024_09_20 22:00 | 3247926 | 9 | 17.8950 | 16.8150 | -115.9555 | 3.2121 | 38.0641 | 0.0039 | 0.0161 |
| 2024_09_20 22:00 | 3272241 | 10 | 18.9489 | 13.4833 | -117.4499 | 4.0338 | 44.6767 | 0.0186 | 0.0196 |
| 2024_09_20 22:00 | 3214640 | 11 | 14.6961 | 15.6522 | -114.8195 | 4.1713 | 38.6490 | 0.0072 | 0.0054 |
| 2024_09_20 22:00 | 3216820 | 12 | 7.2507 | 18.5720 | -117.2782 | 4.9953 | 40.3687 | 0.0007 | 0.0149 |
| 2024_09_20 22:00 | 3211184 | 13 | 15.1777 | 13.8497 | -115.8810 | 3.4449 | 43.4659 | 0.0014 | 0.0084 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413733_87199CA4 | 504990 | 513 | -93.4 | 504990 | 984 | -96.1 | 504990 | 161 | -104.4 | 504990 | 333 |
| MR_1774413733_78D35B39 | 504990 | 513 | -94.1 | 504990 | 984 | -94.5 | 504990 | 161 | -102.1 | 504990 | 333 |
| MR_1774413733_F74934D8 | 152650 | 484 | -89.9 | 152650 | 232 | -93.0 | 152650 | 1 | -97.2 | 152650 | 589 |
| MR_1774413733_2751C454 | 152650 | 484 | -92.4 | 152650 | 232 | -93.9 | 152650 | 1 | -99.0 | 152650 | 589 |
| MR_1774413733_676C919F | 152650 | 484 | -93.1 | 152650 | 232 | -95.5 | 152650 | 1 | -97.6 | 152650 | 589 |
| MR_1774413733_68BDDBC6 | 152650 | 484 | -92.3 | 152650 | 232 | -93.6 | 152650 | 1 | -97.1 | 152650 | 589 |
| MR_1774413733_032AA453 | 504990 | 513 | -93.5 | 504990 | 984 | -95.9 | 504990 | 161 | -102.4 | 504990 | 333 |
| MR_1774413733_CA462884 | 152650 | 484 | -90.0 | 152650 | 232 | -94.4 | 152650 | 1 | -96.7 | 152650 | 589 |

> *... 2개 열 생략 (전체 14열)*

---
