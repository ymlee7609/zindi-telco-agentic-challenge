# Track A 문제 분석 — test[260]~test[269]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[260] ~ test[269] (10개)

## 목차

1. [문제 260: `ef719179-ad0...`](#260) — single-answer
2. [문제 261: `f7701cea-ddc...`](#261) — single-answer
3. [문제 262: `68d7b65d-ee1...`](#262) — single-answer
4. [문제 263: `57e9e338-fbb...`](#263) — single-answer
5. [문제 264: `7d220d58-fc5...`](#264) — single-answer
6. [문제 265: `490929ca-ead...`](#265) — multiple-answer
7. [문제 266: `e30770a1-3c8...`](#266) — single-answer
8. [문제 267: `5f7ac8ba-db1...`](#267) — single-answer
9. [문제 268: `cb1e7dd1-c6b...`](#268) — single-answer
10. [문제 269: `22b185a7-d5d...`](#269) — single-answer

---

### 문제 260: `ef719179-ad0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ef719179-ad0f-42a1-8e59-64d297df9e20` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[260] topology](images/test_0260.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3253637_4 by 5 degrees
- `C2`: Decrease A3 Offset threshold for 3210216_1
- `C3`: Add neighbor relationship between 3253637_4 and 3210216_1
- `C4`: Decrease A3 Offset threshold for 3253637_4
- `C5`: Increase transmission power for 3210216_1
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Add neighbor relationship between 3249244_3 and 3210216_1
- `C8`: Press down the tilt angle  of 3210216_1 by 10 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210216_1
- `C10`: Decrease transmission power for 3253637_4
- `C11`: Press down the tilt angle of 3253637_4 by 5 degrees
- `C12`: Lift the tilt angle  of 3210216_1 by 10 degrees
- `C13`: Adjust the azimuth of 3253637_4 by 50 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253637_4
- `C15`: Adjust the azimuth of 3210216_1 by 50 degrees
- `C16`: Increase transmission power for 3253637_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253637_4
- `C18`: Increase A3 Offset threshold for 3210216_1
- `C19`: Decrease transmission power for 3210216_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210216_1
- `C21`: Check test server and transmission issues
- `C22`: Increase A3 Offset threshold for 3253637_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.546 | MS1 | 121.4656691600 | 31.1446221910 | 429 | 504990 | -91.99 | 14.30 | 489.99 | 0.02 | 2.49 | 1572 |
| 2024-09-20 22:21:32.211 | MS1 | 121.4656705496 | 31.1446379199 | 429 | 504990 | -85.00 | 16.53 | 507.56 | 0.06 | 2.70 | 1560 |
| 2024-09-20 22:21:33.818 | MS1 | 121.4656599173 | 31.1446236668 | 429 | 504990 | -86.02 | 15.65 | 492.84 | 0.09 | 2.30 | 1569 |
| 2024-09-20 22:21:34.802 | MS1 | 121.4656638189 | 31.1446201837 | 429 | 504990 | -85.05 | 17.41 | 91.25 | 0.08 | 2.59 | 478 |
| 2024-09-20 22:21:35.178 | MS1 | 121.4656663243 | 31.1446313863 | 429 | 504990 | -89.43 | 14.24 | 63.73 | 0.18 | 2.17 | 412 |
| 2024-09-20 22:21:36.350 | MS1 | 121.4656769589 | 31.1446240144 | 429 | 504990 | -89.99 | 14.96 | 103.44 | 0.01 | 2.83 | 327 |
| 2024-09-20 22:21:37.390 | MS1 | 121.4656766917 | 31.1446203933 | 429 | 504990 | -91.45 | 10.66 | 89.35 | 0.02 | 2.12 | 309 |
| 2024-09-20 22:21:38.448 | MS1 | 121.4656759471 | 31.1446331710 | 429 | 504990 | -90.65 | 10.29 | 73.69 | 0.10 | 2.79 | 416 |
| 2024-09-20 22:21:39.285 | MS1 | 121.4656775104 | 31.1446258480 | 429 | 504990 | -92.18 | 12.35 | 86.47 | 0.03 | 2.79 | 459 |
| 2024-09-20 22:21:40.230 | MS1 | 121.4656761932 | 31.1446361944 | 429 | 504990 | -93.14 | 12.38 | 515.31 | 0.11 | 2.99 | 1581 |
| 2024-09-20 22:21:41.683 | MS1 | 121.4656624061 | 31.1446242673 | 429 | 504990 | -90.18 | 7.73 | 403.10 | 0.08 | 2.14 | 1596 |
| 2024-09-20 22:21:42.358 | MS1 | 121.4656777094 | 31.1446268291 | 429 | 504990 | -93.00 | 7.18 | 552.43 | 0.17 | 2.55 | 1575 |

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
| 3210216 | 1 | 121.4657423500 | 31.1502727764 | 4 | 8 | 1 | 22.2 | TDD | 656 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3249244 | 3 | 121.4703975927 | 31.1442395331 | 22 | 8 | 3 | 33.4 | TDD | 836 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3253637 | 4 | 121.4755495241 | 31.1522598209 | 84 | 3 | 7 | 38.5 | TDD | 429 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3271158 | 2 | 121.4688510510 | 31.1534245609 | 102 | 4 | 4 | 24.3 | TDD | 593 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.274 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.291 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.395 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.395 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.076 | NREventA3 | measId:2;ServCellPCI:374;Se... |
| 2024-09-20 22:21:38.316 | NRHandoverAttempt | SourcePCI:374;SourceNR-ARFC... |
| 2024-09-20 22:21:38.346 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.357 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.485 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.485 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210216 | 1 | 12.6320 | 17.9963 | -115.8408 | 14.7477 | 174.6160 | 0.0076 | 0.0196 |
| 2024_09_20 22:00 | 3271158 | 2 | 19.5149 | 15.9071 | -117.5519 | 5.1943 | 116.3499 | 0.0047 | 0.0027 |
| 2024_09_20 22:00 | 3249244 | 3 | 10.3245 | 18.1802 | -114.8014 | 7.3121 | 132.0543 | 0.0195 | 0.0104 |
| 2024_09_20 22:00 | 3253637 | 4 | 18.6195 | 15.9579 | -114.5734 | 14.5717 | 99.7029 | 0.0098 | 0.0067 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413123_B4792611 | 504990 | 429 | -84.7 | 504990 | 656 | -87.3 | 504990 | 836 | -93.2 | 504990 | 593 |
| MR_1774413123_75EF71DF | 504990 | 429 | -84.6 | 504990 | 656 | -87.9 | 504990 | 836 | -93.2 | 504990 | 593 |
| MR_1774413123_ABF87C51 | 504990 | 429 | -84.7 | 504990 | 656 | -88.7 | 504990 | 836 | -94.7 | 504990 | 593 |
| MR_1774413123_7BA3C95D | 504990 | 429 | -85.2 | 504990 | 656 | -86.1 | 504990 | 836 | -92.1 | 504990 | 593 |
| MR_1774413123_51E341A7 | 504990 | 429 | -86.1 | 504990 | 656 | -89.4 | 504990 | 836 | -94.3 | 504990 | 593 |
| MR_1774413123_4DA4993C | 504990 | 429 | -85.0 | 504990 | 656 | -86.7 | 504990 | 836 | -94.4 | 504990 | 593 |
| MR_1774413123_AB371BF1 | 504990 | 429 | -86.4 | 504990 | 656 | -89.7 | 504990 | 836 | -92.4 | 504990 | 593 |
| MR_1774413123_89D3AD80 | 504990 | 429 | -85.3 | 504990 | 656 | -87.7 | 504990 | 836 | -91.6 | 504990 | 593 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 261: `f7701cea-ddc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f7701cea-ddcd-4570-8c03-8109b7b8666d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[261] topology](images/test_0261.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3237343_3 by 50 degrees
- `C2`: Decrease A3 Offset threshold for 3237343_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237343_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256927_2
- `C5`: Decrease transmission power for 3256927_2
- `C6`: Increase A3 Offset threshold for 3237343_3
- `C7`: Increase transmission power for 3256927_2
- `C8`: Check test server and transmission issues
- `C9`: Add neighbor relationship between 3238094_4 and 3237343_3
- `C10`: Press down the tilt angle of 3256927_2 by 3 degrees
- `C11`: Add neighbor relationship between 3256927_2 and 3237343_3
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Increase A3 Offset threshold for 3256927_2
- `C14`: Increase transmission power for 3237343_3
- `C15`: Press down the tilt angle  of 3237343_3 by 5 degrees
- `C16`: Lift the tilt angle  of 3237343_3 by 5 degrees
- `C17`: Adjust the azimuth of 3256927_2 by 41 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237343_3
- `C19`: Decrease A3 Offset threshold for 3256927_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256927_2
- `C21`: Lift the tilt angle of 3256927_2 by 3 degrees
- `C22`: Decrease transmission power for 3237343_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.153 | MS1 | 121.4656594879 | 31.1446272748 | 701 | 504990 | -83.44 | 17.13 | 413.91 | 0.03 | 2.61 | 1596 |
| 2024-09-20 22:21:32.242 | MS1 | 121.4656610589 | 31.1446276114 | 701 | 504990 | -77.61 | 14.62 | 441.78 | 0.09 | 3.00 | 1564 |
| 2024-09-20 22:21:33.947 | MS1 | 121.4656764119 | 31.1446284434 | 701 | 504990 | -78.45 | 13.40 | 554.33 | 0.07 | 2.80 | 1589 |
| 2024-09-20 22:21:34.666 | MS1 | 121.4656648439 | 31.1446317576 | 701 | 504990 | -86.58 | -2.60 | 67.89 | 0.18 | 1.22 | 1579 |
| 2024-09-20 22:21:35.647 | MS1 | 121.4656748561 | 31.1446227814 | 701 | 504990 | -91.64 | -3.13 | 67.48 | 0.05 | 1.06 | 1578 |
| 2024-09-20 22:21:36.942 | MS1 | 121.4656605210 | 31.1446307952 | 701 | 504990 | -85.68 | -1.36 | 51.45 | 0.01 | 1.08 | 1572 |
| 2024-09-20 22:21:37.504 | MS1 | 121.4656607314 | 31.1446316155 | 701 | 504990 | -89.08 | -3.98 | 31.91 | 0.19 | 1.27 | 1575 |
| 2024-09-20 22:21:38.836 | MS1 | 121.4656660095 | 31.1446350825 | 701 | 504990 | -85.72 | -1.98 | 67.57 | 0.08 | 1.06 | 1580 |
| 2024-09-20 22:21:39.766 | MS1 | 121.4656678307 | 31.1446350791 | 273 | 504990 | -83.55 | 12.30 | 277.33 | 0.19 | 1.23 | 1580 |
| 2024-09-20 22:21:40.310 | MS1 | 121.4656776143 | 31.1446220761 | 273 | 504990 | -80.99 | 16.87 | 344.27 | 0.04 | 2.27 | 1592 |
| 2024-09-20 22:21:41.507 | MS1 | 121.4656682228 | 31.1446256188 | 273 | 504990 | -79.36 | 15.31 | 356.89 | 0.01 | 2.51 | 1570 |
| 2024-09-20 22:21:42.984 | MS1 | 121.4656725667 | 31.1446341882 | 273 | 504990 | -78.17 | 13.67 | 467.58 | 0.14 | 2.85 | 1575 |

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
| 3237343 | 3 | 121.4733177201 | 31.1486304669 | 321 | 3 | 12 | 24.0 | TDD | 273 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3238094 | 4 | 121.4651710985 | 31.1511746519 | 292 | 8 | 9 | 23.3 | TDD | 777 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3248683 | 1 | 121.4662327957 | 31.1506339180 | 116 | 3 | 5 | 25.4 | TDD | 593 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3256927 | 2 | 121.4655966451 | 31.1531776360 | 221 | 1 | 12 | 29.8 | TDD | 701 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.592 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.697 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.697 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.467 | NREventA3 | measId:2;ServCellPCI:188;Se... |
| 2024-09-20 22:21:38.707 | NRHandoverAttempt | SourcePCI:188;SourceNR-ARFC... |
| 2024-09-20 22:21:38.749 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.761 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.906 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.906 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248683 | 1 | 14.8792 | 14.3978 | -115.0464 | 10.6860 | 117.7076 | 0.0158 | 0.0130 |
| 2024_09_20 22:00 | 3256927 | 2 | 11.9715 | 6.0968 | -115.5923 | 6.3438 | 152.1103 | 0.0095 | 0.1247 |
| 2024_09_20 22:00 | 3237343 | 3 | 11.7000 | 10.0501 | -114.6290 | 9.3249 | 173.9018 | 0.0038 | 0.0138 |
| 2024_09_20 22:00 | 3238094 | 4 | 16.5858 | 7.8306 | -117.0384 | 17.4632 | 119.0332 | 0.0026 | 0.0137 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415523_E92BCF8C | 504990 | 701 | -85.8 | 504990 | 273 | -80.9 | 504990 | 777 | -80.9 | 504990 | 593 |
| MR_1774415523_3B820406 | 504990 | 273 | -79.4 | 504990 | 701 | -86.3 | 504990 | 777 | -81.4 | 504990 | 593 |
| MR_1774415523_9CF396FE | 504990 | 701 | -85.0 | 504990 | 273 | -82.5 | 504990 | 777 | -83.1 | 504990 | 593 |
| MR_1774415523_C225F078 | 504990 | 273 | -81.9 | 504990 | 701 | -88.4 | 504990 | 777 | -82.2 | 504990 | 593 |
| MR_1774415523_8AD9706D | 504990 | 701 | -86.2 | 504990 | 273 | -83.3 | 504990 | 777 | -80.0 | 504990 | 593 |
| MR_1774415523_1EBD897F | 504990 | 701 | -86.7 | 504990 | 273 | -81.9 | 504990 | 777 | -80.7 | 504990 | 593 |
| MR_1774415523_2DB22A93 | 504990 | 701 | -86.3 | 504990 | 273 | -80.0 | 504990 | 777 | -83.4 | 504990 | 593 |
| MR_1774415523_AA538E55 | 504990 | 273 | -80.7 | 504990 | 701 | -86.7 | 504990 | 777 | -79.9 | 504990 | 593 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 262: `68d7b65d-ee1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `68d7b65d-ee19-456b-aadd-77595e6c9edd` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[262] topology](images/test_0262.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Press down the tilt angle  of 3252654_4 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271357_2
- `C4`: Increase A3 Offset threshold for 3252654_4
- `C5`: Adjust the azimuth of 3252654_4 by 27 degrees
- `C6`: Decrease transmission power for 3271357_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271357_2
- `C8`: Lift the tilt angle of 3271357_2 by 10 degrees
- `C9`: Decrease A3 Offset threshold for 3271357_2
- `C10`: Add neighbor relationship between 3218239_3 and 3252654_4
- `C11`: Check test server and transmission issues
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252654_4
- `C13`: Add neighbor relationship between 3271357_2 and 3252654_4
- `C14`: Adjust the azimuth of 3271357_2 by 50 degrees
- `C15`: Increase transmission power for 3271357_2
- `C16`: Lift the tilt angle  of 3252654_4 by 10 degrees
- `C17`: Decrease transmission power for 3252654_4
- `C18`: Decrease A3 Offset threshold for 3252654_4
- `C19`: Increase transmission power for 3252654_4
- `C20`: Press down the tilt angle of 3271357_2 by 10 degrees
- `C21`: Increase A3 Offset threshold for 3271357_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252654_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.974 | MS1 | 121.4656663337 | 31.1446370888 | 567 | 504990 | -75.06 | 13.13 | 434.19 | 0.18 | 2.10 | 1577 |
| 2024-09-20 22:21:32.452 | MS1 | 121.4656774425 | 31.1446298194 | 567 | 504990 | -81.84 | 17.64 | 426.40 | 0.07 | 2.20 | 1581 |
| 2024-09-20 22:21:33.222 | MS1 | 121.4656642484 | 31.1446370713 | 567 | 504990 | -84.01 | 12.44 | 426.18 | 0.10 | 2.31 | 1580 |
| 2024-09-20 22:21:34.463 | MS1 | 121.4656660508 | 31.1446350880 | 567 | 504990 | -87.70 | -0.13 | 37.76 | 0.03 | 1.01 | 1587 |
| 2024-09-20 22:21:35.179 | MS1 | 121.4656754872 | 31.1446253107 | 567 | 504990 | -91.42 | -3.37 | 65.41 | 0.13 | 1.46 | 1563 |
| 2024-09-20 22:21:36.312 | MS1 | 121.4656611435 | 31.1446359301 | 567 | 504990 | -88.24 | -2.99 | 33.45 | 0.06 | 1.26 | 1560 |
| 2024-09-20 22:21:37.550 | MS1 | 121.4656584977 | 31.1446295559 | 567 | 504990 | -90.62 | -3.41 | 49.37 | 0.09 | 1.19 | 1580 |
| 2024-09-20 22:21:38.138 | MS1 | 121.4656623862 | 31.1446329569 | 567 | 504990 | -85.43 | -1.64 | 62.59 | 0.11 | 1.39 | 1585 |
| 2024-09-20 22:21:39.968 | MS1 | 121.4656586152 | 31.1446346090 | 919 | 504990 | -82.35 | 14.72 | 198.25 | 0.11 | 1.23 | 1560 |
| 2024-09-20 22:21:40.428 | MS1 | 121.4656591168 | 31.1446221987 | 919 | 504990 | -76.16 | 14.41 | 369.72 | 0.01 | 3.00 | 1563 |
| 2024-09-20 22:21:41.568 | MS1 | 121.4656589722 | 31.1446266704 | 919 | 504990 | -83.36 | 13.25 | 538.78 | 0.19 | 2.48 | 1574 |
| 2024-09-20 22:21:42.379 | MS1 | 121.4656621719 | 31.1446259118 | 919 | 504990 | -80.36 | 17.50 | 484.43 | 0.03 | 2.19 | 1597 |

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
| 3218239 | 3 | 121.4755184419 | 31.1471106165 | 350 | 12 | 0 | 17.3 | TDD | 973 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3224918 | 1 | 121.4666645208 | 31.1467809250 | 74 | 14 | 4 | 19.3 | TDD | 665 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3252654 | 4 | 121.4712261506 | 31.1465027970 | 222 | 14 | 3 | 43.8 | TDD | 919 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3271357 | 2 | 121.4750694837 | 31.1489411243 | 111 | 13 | 3 | 47.3 | TDD | 567 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.352 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.377 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.489 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.489 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.192 | NREventA3 | measId:2;ServCellPCI:760;Se... |
| 2024-09-20 22:21:38.432 | NRHandoverAttempt | SourcePCI:760;SourceNR-ARFC... |
| 2024-09-20 22:21:38.465 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.480 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.625 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.625 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224918 | 1 | 19.2834 | 6.4766 | -115.2804 | 10.0721 | 111.5121 | 0.0156 | 0.0157 |
| 2024_09_20 22:00 | 3271357 | 2 | 10.6585 | 11.4801 | -115.0355 | 11.1791 | 127.3425 | 0.0136 | 0.1637 |
| 2024_09_20 22:00 | 3218239 | 3 | 7.4651 | 17.7638 | -116.2123 | 18.7107 | 142.9344 | 0.0186 | 0.0100 |
| 2024_09_20 22:00 | 3252654 | 4 | 16.9240 | 18.5147 | -116.5686 | 11.3541 | 142.1466 | 0.0065 | 0.0045 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412471_EDA08F6A | 504990 | 567 | -89.6 | 504990 | 919 | -81.1 | 504990 | 973 | -85.1 | 504990 | 665 |
| MR_1774412471_BCBE1906 | 504990 | 567 | -85.9 | 504990 | 919 | -81.2 | 504990 | 973 | -84.0 | 504990 | 665 |
| MR_1774412471_BC03859D | 504990 | 919 | -81.9 | 504990 | 567 | -87.1 | 504990 | 973 | -82.6 | 504990 | 665 |
| MR_1774412471_06D397B7 | 504990 | 567 | -86.5 | 504990 | 919 | -81.3 | 504990 | 973 | -85.1 | 504990 | 665 |
| MR_1774412471_3E5B6445 | 504990 | 919 | -82.5 | 504990 | 567 | -89.1 | 504990 | 973 | -85.3 | 504990 | 665 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 263: `57e9e338-fbb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `57e9e338-fbbc-496d-b2aa-a466df5c99f8` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[263] topology](images/test_0263.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3235845_3
- `C2`: Adjust the azimuth of 3235845_3 by 37 degrees
- `C3`: Adjust the azimuth of 3255782_4 by 16 degrees
- `C4`: Increase transmission power for 3255782_4
- `C5`: Decrease A3 Offset threshold for 3235845_3
- `C6`: Add neighbor relationship between 3235845_3 and 3255782_4
- `C7`: Press down the tilt angle  of 3255782_4 by 6 degrees
- `C8`: Decrease transmission power for 3255782_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235845_3
- `C10`: Add neighbor relationship between 3229488_13 and 3255782_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255782_4
- `C12`: Press down the tilt angle of 3235845_3 by 2 degrees
- `C13`: Lift the tilt angle of 3235845_3 by 2 degrees
- `C14`: Increase A3 Offset threshold for 3255782_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235845_3
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease A3 Offset threshold for 3255782_4
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255782_4
- `C19`: Lift the tilt angle  of 3255782_4 by 6 degrees
- `C20`: Check test server and transmission issues
- `C21`: Increase A3 Offset threshold for 3235845_3
- `C22`: Decrease transmission power for 3235845_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.217 | MS1 | 121.4656606984 | 31.1446253976 | 822 | 504990 | -93.78 | 14.21 | 535.68 | 0.02 | 2.64 | 1572 |
| 2024-09-20 22:21:32.989 | MS1 | 121.4656766812 | 31.1446306915 | 601 | 504990 | -95.92 | 11.42 | 396.48 | 0.13 | 2.04 | 1560 |
| 2024-09-20 22:21:33.217 | MS1 | 121.4656752626 | 31.1446212435 | 128 | 504990 | -94.44 | 14.77 | 430.88 | 0.10 | 2.27 | 1600 |
| 2024-09-20 22:21:34.667 | MS1 | 121.4656761361 | 31.1446358188 | 36 | 152650 | -93.92 | 5.70 | 53.55 | 0.10 | 1.71 | 977 |
| 2024-09-20 22:21:35.521 | MS1 | 121.4656725619 | 31.1446364255 | 568 | 152650 | -89.25 | 5.38 | 56.42 | 0.05 | 1.81 | 958 |
| 2024-09-20 22:21:36.823 | MS1 | 121.4656590090 | 31.1446180181 | 410 | 152650 | -90.68 | 4.38 | 79.62 | 0.10 | 1.59 | 983 |
| 2024-09-20 22:21:37.124 | MS1 | 121.4656719230 | 31.1446365295 | 720 | 152650 | -91.93 | 4.70 | 73.88 | 0.04 | 1.85 | 930 |
| 2024-09-20 22:21:38.999 | MS1 | 121.4656591540 | 31.1446258149 | 36 | 152650 | -93.09 | 5.32 | 46.51 | 0.01 | 1.64 | 900 |
| 2024-09-20 22:21:39.137 | MS1 | 121.4656629391 | 31.1446319010 | 568 | 152650 | -87.78 | 7.49 | 72.93 | 0.02 | 1.65 | 906 |
| 2024-09-20 22:21:40.947 | MS1 | 121.4656729271 | 31.1446195282 | 410 | 152650 | -94.99 | 6.76 | 74.20 | 0.13 | 2.45 | 1577 |
| 2024-09-20 22:21:41.202 | MS1 | 121.4656607108 | 31.1446252448 | 720 | 152650 | -94.81 | 4.38 | 84.50 | 0.19 | 2.62 | 1573 |
| 2024-09-20 22:21:42.855 | MS1 | 121.4656653546 | 31.1446184783 | 36 | 152650 | -88.32 | 5.80 | 78.15 | 0.14 | 2.10 | 1580 |

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
| 3229488 | 13 | 121.4705119241 | 31.1556939460 | 34 | 4 | 6 | 7.5 | FDD | 410 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3230501 | 5 | 121.4709931717 | 31.1460010846 | 215 | 1 | 8 | 5.3 | TDD | 601 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3235845 | 3 | 121.4715433777 | 31.1556601019 | 168 | 2 | 5 | 2.0 | TDD | 822 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3240391 | 10 | 121.4654318289 | 31.1474771701 | 220 | 12 | 2 | 25.6 | FDD | 593 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3242607 | 2 | 121.4713370692 | 31.1457947374 | 13 | 8 | 10 | 25.6 | TDD | 771 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3243890 | 8 | 121.4731578471 | 31.1542456897 | 329 | 10 | 5 | 23.0 | FDD | 686 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3245754 | 11 | 121.4716762165 | 31.1518170528 | 202 | 0 | 11 | 8.3 | FDD | 662 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3255782 | 4 | 121.4694436246 | 31.1510409129 | 223 | 5 | 5 | 7.8 | TDD | 440 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3258110 | 12 | 121.4642474214 | 31.1479163184 | 143 | 9 | 10 | 20.1 | FDD | 568 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3262048 | 6 | 121.4660932371 | 31.1496493447 | 173 | 1 | 1 | 24.7 | TDD | 831 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3264497 | 1 | 121.4715954505 | 31.1510620954 | 231 | 11 | 10 | 0.2 | TDD | 128 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3272330 | 9 | 121.4649282622 | 31.1510012629 | 196 | 12 | 9 | 0.8 | FDD | 720 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3276740 | 7 | 121.4644726951 | 31.1440479279 | 52 | 11 | 12 | 6.4 | FDD | 36 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |

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
| 2024-09-20 22:21:31.018 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.033 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.139 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.139 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.825 | NREventA2 | measId:1;ServCellPCI:768;Se... |
| 2024-09-20 22:21:34.927 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.160 | NREventA5 | measId:3;ServCellPCI:768;Se... |
| 2024-09-20 22:21:35.192 | NRHandoverAttempt | SourcePCI:768;SourceNR-ARFC... |
| 2024-09-20 22:21:35.237 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.249 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.372 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.372 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264497 | 1 | 10.4327 | 11.1685 | -116.8802 | 18.8376 | 163.2170 | 0.0175 | 0.0175 |
| 2024_09_20 22:00 | 3242607 | 2 | 12.7044 | 5.0476 | -117.2348 | 16.0063 | 100.1941 | 0.0198 | 0.0056 |
| 2024_09_20 22:00 | 3235845 | 3 | 18.8490 | 10.3805 | -117.9428 | 6.0139 | 162.1444 | 0.0120 | 0.0117 |
| 2024_09_20 22:00 | 3255782 | 4 | 18.2922 | 10.7214 | -115.9352 | 17.6368 | 178.6660 | 0.0102 | 0.0188 |
| 2024_09_20 22:00 | 3230501 | 5 | 16.1960 | 6.7136 | -115.2704 | 13.8159 | 192.2473 | 0.0169 | 0.0166 |
| 2024_09_20 22:00 | 3262048 | 6 | 7.7399 | 8.6210 | -114.7894 | 7.1436 | 82.6478 | 0.0133 | 0.0091 |
| 2024_09_20 22:00 | 3276740 | 7 | 19.8100 | 10.1907 | -115.1615 | 4.8465 | 25.5657 | 0.0152 | 0.0084 |
| 2024_09_20 22:00 | 3243890 | 8 | 18.8918 | 13.7436 | -116.6773 | 4.7120 | 44.3056 | 0.0139 | 0.0174 |
| 2024_09_20 22:00 | 3272330 | 9 | 11.4051 | 14.7859 | -116.8750 | 3.6007 | 47.9361 | 0.0062 | 0.0058 |
| 2024_09_20 22:00 | 3240391 | 10 | 13.9131 | 18.7084 | -116.1332 | 4.2994 | 31.4872 | 0.0035 | 0.0191 |
| 2024_09_20 22:00 | 3245754 | 11 | 12.7608 | 10.4613 | -116.0989 | 3.6793 | 29.6785 | 0.0000 | 0.0105 |
| 2024_09_20 22:00 | 3258110 | 12 | 8.0221 | 19.9864 | -114.4233 | 3.0832 | 37.4712 | 0.0182 | 0.0000 |
| 2024_09_20 22:00 | 3229488 | 13 | 10.4284 | 7.0640 | -116.0541 | 3.3682 | 47.3405 | 0.0176 | 0.0117 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417009_BB3D1A4C | 152650 | 36 | -93.4 | 152650 | 686 | -100.0 | 152650 | 662 | -103.4 | 152650 | 593 |
| MR_1774417009_00F4FB64 | 152650 | 36 | -92.8 | 152650 | 686 | -99.7 | 152650 | 662 | -101.6 | 152650 | 593 |
| MR_1774417009_A63343BE | 504990 | 128 | -95.6 | 504990 | 440 | -100.3 | 504990 | 771 | -101.8 | 504990 | 831 |
| MR_1774417009_8BC9BA05 | 504990 | 128 | -93.7 | 504990 | 440 | -97.8 | 504990 | 771 | -101.2 | 504990 | 831 |
| MR_1774417009_1B3774DF | 504990 | 128 | -94.8 | 504990 | 440 | -100.4 | 504990 | 771 | -102.2 | 504990 | 831 |
| MR_1774417009_A274519D | 504990 | 128 | -95.0 | 504990 | 440 | -99.4 | 504990 | 771 | -99.7 | 504990 | 831 |
| MR_1774417009_3ACD82B0 | 152650 | 36 | -92.9 | 152650 | 686 | -99.7 | 152650 | 662 | -101.6 | 152650 | 593 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 264: `7d220d58-fc5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7d220d58-fc5a-4975-b1b8-b95c4a90b169` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[264] topology](images/test_0264.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3251567_3
- `C2`: Press down the tilt angle  of 3251567_3 by 10 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251567_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241275_1
- `C5`: Add neighbor relationship between 3255518_4 and 3251567_3
- `C6`: Decrease A3 Offset threshold for 3251567_3
- `C7`: Increase transmission power for 3241275_1
- `C8`: Press down the tilt angle of 3241275_1 by 9 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241275_1
- `C11`: Adjust the azimuth of 3251567_3 by 4 degrees
- `C12`: Increase A3 Offset threshold for 3251567_3
- `C13`: Add neighbor relationship between 3241275_1 and 3251567_3
- `C14`: Lift the tilt angle  of 3251567_3 by 10 degrees
- `C15`: Decrease transmission power for 3241275_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251567_3
- `C17`: Increase transmission power for 3251567_3
- `C18`: Lift the tilt angle of 3241275_1 by 9 degrees
- `C19`: Check test server and transmission issues
- `C20`: Adjust the azimuth of 3241275_1 by 44 degrees
- `C21`: Decrease A3 Offset threshold for 3241275_1
- `C22`: Increase A3 Offset threshold for 3241275_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.890 | MS1 | 121.4656761596 | 31.1446331147 | 459 | 504990 | -91.11 | 12.37 | 546.60 | 0.16 | 2.40 | 1598 |
| 2024-09-20 22:21:32.627 | MS1 | 121.4656757828 | 31.1446264760 | 459 | 504990 | -89.79 | 15.85 | 357.45 | 0.09 | 2.98 | 1566 |
| 2024-09-20 22:21:33.987 | MS1 | 121.4656701609 | 31.1446277013 | 459 | 504990 | -85.60 | 15.31 | 563.38 | 0.15 | 2.49 | 1594 |
| 2024-09-20 22:21:34.141 | MS1 | 121.4656648724 | 31.1446258927 | 459 | 504990 | -90.07 | 16.31 | 56.98 | 0.05 | 2.49 | 1590 |
| 2024-09-20 22:21:35.576 | MS1 | 121.4656673979 | 31.1446352162 | 459 | 504990 | -87.62 | 14.32 | 63.57 | 0.00 | 2.01 | 1589 |
| 2024-09-20 22:21:36.101 | MS1 | 121.4656751143 | 31.1446234907 | 459 | 504990 | -89.02 | 13.70 | 89.36 | 0.09 | 2.50 | 1592 |
| 2024-09-20 22:21:37.140 | MS1 | 121.4656691380 | 31.1446355565 | 459 | 504990 | -89.08 | 9.92 | 59.44 | 0.04 | 2.81 | 1570 |
| 2024-09-20 22:21:38.984 | MS1 | 121.4656634910 | 31.1446364046 | 459 | 504990 | -89.78 | 12.52 | 95.53 | 0.03 | 2.12 | 1578 |
| 2024-09-20 22:21:39.847 | MS1 | 121.4656758278 | 31.1446187214 | 459 | 504990 | -93.38 | 11.10 | 64.88 | 0.09 | 2.68 | 1571 |
| 2024-09-20 22:21:40.130 | MS1 | 121.4656661522 | 31.1446221868 | 459 | 504990 | -90.18 | 7.86 | 313.36 | 0.18 | 2.91 | 1591 |
| 2024-09-20 22:21:41.142 | MS1 | 121.4656585040 | 31.1446195169 | 459 | 504990 | -92.02 | 12.07 | 419.81 | 0.10 | 2.67 | 1582 |
| 2024-09-20 22:21:42.702 | MS1 | 121.4656680487 | 31.1446257872 | 459 | 504990 | -92.38 | 10.36 | 348.93 | 0.18 | 2.18 | 1577 |

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
| 3241275 | 1 | 121.4656104360 | 31.1549442230 | 224 | 8 | 7 | 26.0 | TDD | 459 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3251567 | 3 | 121.4722631885 | 31.1535495160 | 216 | 10 | 3 | 48.6 | TDD | 909 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3255518 | 4 | 121.4719820426 | 31.1474328493 | 33 | 12 | 3 | 22.9 | TDD | 974 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3259473 | 2 | 121.4654385184 | 31.1525935810 | 140 | 8 | 8 | 16.8 | TDD | 100 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.159 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.175 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.296 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.296 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.989 | NREventA3 | measId:2;ServCellPCI:956;Se... |
| 2024-09-20 22:21:38.229 | NRHandoverAttempt | SourcePCI:956;SourceNR-ARFC... |
| 2024-09-20 22:21:38.276 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.286 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.435 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.435 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3241275 | 1 | 86.2815 | 94.3962 | -116.8011 | 12.6424 | 115.0920 | 0.0176 | 0.0106 |
| 2024_09_19 22:00 | 3259473 | 2 | 84.5399 | 87.5917 | -116.3453 | 19.3064 | 150.4765 | 0.0045 | 0.0164 |
| 2024_09_19 22:00 | 3251567 | 3 | 83.1686 | 91.4025 | -114.2931 | 12.9326 | 176.1806 | 0.0110 | 0.0180 |
| 2024_09_19 22:00 | 3255518 | 4 | 90.1105 | 76.4245 | -117.7940 | 15.8005 | 169.9797 | 0.0137 | 0.0015 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413380_90640909 | 504990 | 459 | -89.6 | 504990 | 909 | -94.5 | 504990 | 974 | -101.5 | 504990 | 100 |
| MR_1774413380_F26959B1 | 504990 | 459 | -89.2 | 504990 | 909 | -92.4 | 504990 | 974 | -100.0 | 504990 | 100 |
| MR_1774413380_CA8FDAB1 | 504990 | 459 | -88.5 | 504990 | 909 | -94.3 | 504990 | 974 | -101.8 | 504990 | 100 |
| MR_1774413380_2CC25AB7 | 504990 | 459 | -91.9 | 504990 | 909 | -90.8 | 504990 | 974 | -102.2 | 504990 | 100 |
| MR_1774413380_CBFC79B9 | 504990 | 459 | -91.5 | 504990 | 909 | -93.8 | 504990 | 974 | -101.6 | 504990 | 100 |
| MR_1774413380_4A38252D | 504990 | 459 | -88.4 | 504990 | 909 | -94.3 | 504990 | 974 | -102.3 | 504990 | 100 |
| MR_1774413380_977FF96C | 504990 | 459 | -91.8 | 504990 | 909 | -93.3 | 504990 | 974 | -100.3 | 504990 | 100 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 265: `490929ca-ead...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `490929ca-ead4-42e2-ae8e-06e33b3a7751` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[265] topology](images/test_0265.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3238939_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238939_3
- `C3`: Decrease transmission power for 3238939_3
- `C4`: Lift the tilt angle  of 3276010_2 by 4 degrees
- `C5`: Decrease transmission power for 3276010_2
- `C6`: Add neighbor relationship between 3238939_3 and 3276010_2
- `C7`: Increase A3 Offset threshold for 3276010_2
- `C8`: Decrease A3 Offset threshold for 3238939_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276010_2
- `C10`: Adjust the azimuth of 3276010_2 by 43 degrees
- `C11`: Increase transmission power for 3238939_3
- `C12`: Adjust the azimuth of 3238939_3 by 20 degrees
- `C13`: Lift the tilt angle of 3238939_3 by 6 degrees
- `C14`: Decrease A3 Offset threshold for 3276010_2
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Add neighbor relationship between 3275017_5 and 3276010_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238939_3
- `C18`: Press down the tilt angle of 3238939_3 by 6 degrees
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle  of 3276010_2 by 4 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276010_2
- `C22`: Increase transmission power for 3276010_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.931 | MS1 | 121.4656743570 | 31.1446307944 | 42 | 504990 | -76.15 | 13.59 | 458.31 | 0.18 | 2.37 | 1584 |
| 2024-09-20 22:21:32.635 | MS1 | 121.4656771601 | 31.1446344965 | 42 | 504990 | -82.15 | 15.83 | 430.80 | 0.07 | 2.87 | 1566 |
| 2024-09-20 22:21:33.219 | MS1 | 121.4656740749 | 31.1446267265 | 42 | 504990 | -78.21 | 13.53 | 399.35 | 0.07 | 2.88 | 1576 |
| 2024-09-20 22:21:34.599 | MS1 | 121.4656737054 | 31.1446367427 | 82 | 504990 | -87.14 | 2.86 | 54.71 | 0.15 | 1.40 | 1580 |
| 2024-09-20 22:21:35.710 | MS1 | 121.4656698853 | 31.1446363664 | 82 | 504990 | -88.98 | 2.93 | 37.35 | 0.02 | 1.24 | 1562 |
| 2024-09-20 22:21:36.444 | MS1 | 121.4656775652 | 31.1446352990 | 42 | 504990 | -87.32 | 4.67 | 66.70 | 0.00 | 1.21 | 1570 |
| 2024-09-20 22:21:37.712 | MS1 | 121.4656686252 | 31.1446374891 | 42 | 504990 | -86.95 | 4.37 | 53.58 | 0.06 | 1.03 | 1569 |
| 2024-09-20 22:21:38.939 | MS1 | 121.4656733084 | 31.1446212115 | 82 | 504990 | -87.09 | 5.00 | 76.21 | 0.12 | 1.08 | 1586 |
| 2024-09-20 22:21:39.499 | MS1 | 121.4656723594 | 31.1446201195 | 82 | 504990 | -84.76 | 1.64 | 66.42 | 0.14 | 1.49 | 1572 |
| 2024-09-20 22:21:40.155 | MS1 | 121.4656630885 | 31.1446222755 | 82 | 504990 | -77.28 | 17.24 | 318.52 | 0.16 | 2.93 | 1582 |
| 2024-09-20 22:21:41.318 | MS1 | 121.4656688843 | 31.1446267013 | 82 | 504990 | -78.27 | 13.63 | 399.51 | 0.07 | 2.08 | 1569 |
| 2024-09-20 22:21:42.878 | MS1 | 121.4656628187 | 31.1446283116 | 82 | 504990 | -76.07 | 12.35 | 378.36 | 0.09 | 2.59 | 1568 |

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
| 3223733 | 4 | 121.4655117978 | 31.1549857562 | 251 | 13 | 7 | 43.1 | TDD | 82 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3230021 | 1 | 121.4681625087 | 31.1461359226 | 120 | 8 | 3 | 28.0 | TDD | 609 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3238939 | 3 | 121.4645253540 | 31.1485060874 | 146 | 1 | 1 | 37.2 | TDD | 42 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3275017 | 5 | 121.4719304091 | 31.1557443017 | 297 | 13 | 1 | 16.3 | TDD | 631 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3276010 | 2 | 121.4678260965 | 31.1540642566 | 234 | 2 | 8 | 31.9 | TDD | 869 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.968 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.993 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.138 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.138 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.810 | NREventA3 | measId:2;ServCellPCI:379;Se... |
| 2024-09-20 22:21:34.050 | NRHandoverAttempt | SourcePCI:379;SourceNR-ARFC... |
| 2024-09-20 22:21:34.089 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.101 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:34.223 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.223 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.810 | NREventA3 | measId:2;ServCellPCI:330;Se... |
| 2024-09-20 22:21:36.050 | NRHandoverAttempt | SourcePCI:330;SourceNR-ARFC... |
| 2024-09-20 22:21:36.086 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.096 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:36.244 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.244 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.810 | NREventA3 | measId:2;ServCellPCI:379;Se... |
| 2024-09-20 22:21:38.050 | NRHandoverAttempt | SourcePCI:379;SourceNR-ARFC... |
| 2024-09-20 22:21:38.085 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.098 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.207 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.207 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230021 | 1 | 12.1903 | 11.9725 | -115.0199 | 16.6083 | 85.3487 | 0.0101 | 0.0010 |
| 2024_09_20 22:00 | 3276010 | 2 | 18.0008 | 16.5898 | -116.5394 | 11.4855 | 198.6645 | 0.0176 | 0.0090 |
| 2024_09_20 22:00 | 3238939 | 3 | 18.7749 | 15.5214 | -114.1519 | 7.4569 | 118.2518 | 0.0017 | 0.0015 |
| 2024_09_20 22:00 | 3223733 | 4 | 14.1327 | 8.1607 | -115.7478 | 10.6668 | 183.3047 | 0.0098 | 0.0035 |
| 2024_09_20 22:00 | 3275017 | 5 | 7.4420 | 12.0653 | -116.1809 | 11.6823 | 122.2907 | 0.0133 | 0.0090 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417030_9E5A2A11 | 504990 | 82 | -87.6 | 504990 | 42 | -87.1 | 504990 | 869 | -88.6 | 504990 | 631 |
| MR_1774417030_6FECFE12 | 504990 | 42 | -87.8 | 504990 | 82 | -89.7 | 504990 | 869 | -88.7 | 504990 | 631 |
| MR_1774417030_8CFE6881 | 504990 | 82 | -87.0 | 504990 | 42 | -87.4 | 504990 | 869 | -90.5 | 504990 | 631 |
| MR_1774417030_B5EDC357 | 504990 | 82 | -88.2 | 504990 | 42 | -87.5 | 504990 | 869 | -87.5 | 504990 | 631 |
| MR_1774417030_95D99F37 | 504990 | 82 | -86.4 | 504990 | 42 | -89.9 | 504990 | 869 | -88.5 | 504990 | 631 |
| MR_1774417030_9A2BC2E1 | 504990 | 82 | -87.8 | 504990 | 42 | -88.7 | 504990 | 869 | -88.5 | 504990 | 631 |
| MR_1774417030_50056A5E | 504990 | 82 | -87.9 | 504990 | 42 | -89.9 | 504990 | 869 | -88.7 | 504990 | 631 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 266: `e30770a1-3c8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e30770a1-3c80-4146-b484-8d97433cb0e5` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[266] topology](images/test_0266.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Increase transmission power for 3230534_3
- `C3`: Lift the tilt angle of 3230534_3 by 7 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236196_4
- `C5`: Lift the tilt angle  of 3236196_4 by 8 degrees
- `C6`: Increase transmission power for 3236196_4
- `C7`: Decrease A3 Offset threshold for 3236196_4
- `C8`: Add neighbor relationship between 3230534_3 and 3236196_4
- `C9`: Decrease transmission power for 3236196_4
- `C10`: Increase A3 Offset threshold for 3236196_4
- `C11`: Add neighbor relationship between 3279736_2 and 3236196_4
- `C12`: Adjust the azimuth of 3236196_4 by 50 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236196_4
- `C14`: Decrease transmission power for 3230534_3
- `C15`: Press down the tilt angle  of 3236196_4 by 8 degrees
- `C16`: Press down the tilt angle of 3230534_3 by 7 degrees
- `C17`: Adjust the azimuth of 3230534_3 by 50 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230534_3
- `C19`: Increase A3 Offset threshold for 3230534_3
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230534_3
- `C22`: Decrease A3 Offset threshold for 3230534_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.391 | MS1 | 121.4656632000 | 31.1446271059 | 516 | 504990 | -87.44 | 16.12 | 327.81 | 0.15 | 2.98 | 1579 |
| 2024-09-20 22:21:32.714 | MS1 | 121.4656652813 | 31.1446221007 | 516 | 504990 | -86.05 | 13.19 | 527.38 | 0.02 | 2.74 | 1585 |
| 2024-09-20 22:21:33.698 | MS1 | 121.4656623579 | 31.1446209050 | 516 | 504990 | -88.04 | 15.55 | 483.95 | 0.11 | 2.52 | 1583 |
| 2024-09-20 22:21:34.286 | MS1 | 121.4656758390 | 31.1446180358 | 516 | 504990 | -91.36 | 15.01 | 102.16 | 0.13 | 2.61 | 395 |
| 2024-09-20 22:21:35.324 | MS1 | 121.4656588402 | 31.1446180279 | 516 | 504990 | -85.03 | 17.80 | 53.30 | 0.01 | 2.76 | 426 |
| 2024-09-20 22:21:36.227 | MS1 | 121.4656596863 | 31.1446345564 | 516 | 504990 | -85.13 | 14.02 | 89.08 | 0.19 | 2.20 | 496 |
| 2024-09-20 22:21:37.912 | MS1 | 121.4656681220 | 31.1446275318 | 516 | 504990 | -92.16 | 7.31 | 84.19 | 0.02 | 2.75 | 370 |
| 2024-09-20 22:21:38.874 | MS1 | 121.4656748225 | 31.1446198982 | 516 | 504990 | -92.28 | 10.97 | 82.53 | 0.03 | 2.06 | 384 |
| 2024-09-20 22:21:39.525 | MS1 | 121.4656774526 | 31.1446300922 | 516 | 504990 | -93.52 | 8.51 | 74.55 | 0.09 | 2.16 | 403 |
| 2024-09-20 22:21:40.440 | MS1 | 121.4656632766 | 31.1446256506 | 516 | 504990 | -89.80 | 9.59 | 549.08 | 0.10 | 3.00 | 1595 |
| 2024-09-20 22:21:41.980 | MS1 | 121.4656647790 | 31.1446324939 | 516 | 504990 | -91.58 | 8.04 | 539.91 | 0.02 | 2.29 | 1577 |
| 2024-09-20 22:21:42.312 | MS1 | 121.4656683575 | 31.1446366827 | 516 | 504990 | -92.16 | 12.03 | 392.02 | 0.08 | 2.04 | 1570 |

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
| 3230534 | 3 | 121.4745075004 | 31.1506936947 | 79 | 5 | 9 | 44.3 | TDD | 516 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3236196 | 4 | 121.4731031253 | 31.1465964145 | 306 | 4 | 7 | 47.0 | TDD | 389 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3239554 | 1 | 121.4699561888 | 31.1491399207 | 293 | 9 | 6 | 38.7 | TDD | 889 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3279736 | 2 | 121.4749593958 | 31.1453748671 | 28 | 5 | 7 | 24.7 | TDD | 322 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.844 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.863 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.997 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.997 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.699 | NREventA3 | measId:2;ServCellPCI:158;Se... |
| 2024-09-20 22:21:37.939 | NRHandoverAttempt | SourcePCI:158;SourceNR-ARFC... |
| 2024-09-20 22:21:37.981 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.994 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.095 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.095 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239554 | 1 | 13.0164 | 19.2273 | -117.7682 | 8.7983 | 135.9121 | 0.0175 | 0.0111 |
| 2024_09_20 22:00 | 3279736 | 2 | 15.5674 | 11.9695 | -115.8643 | 17.2340 | 108.4059 | 0.0086 | 0.0171 |
| 2024_09_20 22:00 | 3230534 | 3 | 5.9041 | 6.1186 | -116.1714 | 11.5531 | 148.5930 | 0.0153 | 0.0042 |
| 2024_09_20 22:00 | 3236196 | 4 | 6.4859 | 15.8952 | -116.1462 | 11.1489 | 173.5829 | 0.0124 | 0.0131 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417130_FFF2C6E0 | 504990 | 516 | -86.8 | 504990 | 389 | -91.5 | 504990 | 322 | -94.3 | 504990 | 889 |
| MR_1774417130_FA0E0D25 | 504990 | 516 | -85.7 | 504990 | 389 | -92.8 | 504990 | 322 | -94.4 | 504990 | 889 |
| MR_1774417130_04750123 | 504990 | 516 | -84.2 | 504990 | 389 | -92.8 | 504990 | 322 | -97.6 | 504990 | 889 |
| MR_1774417130_0A2C91C2 | 504990 | 516 | -85.5 | 504990 | 389 | -91.0 | 504990 | 322 | -95.7 | 504990 | 889 |
| MR_1774417130_4BEA7C1D | 504990 | 516 | -84.0 | 504990 | 389 | -90.9 | 504990 | 322 | -95.9 | 504990 | 889 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 267: `5f7ac8ba-db1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5f7ac8ba-db13-48b8-8ca1-69f48195bdb2` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[267] topology](images/test_0267.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3257324_2 by 50 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257324_2
- `C3`: Press down the tilt angle of 3257324_2 by 4 degrees
- `C4`: Increase A3 Offset threshold for 3259738_4
- `C5`: Increase transmission power for 3257324_2
- `C6`: Lift the tilt angle  of 3259738_4 by 10 degrees
- `C7`: Decrease transmission power for 3259738_4
- `C8`: Lift the tilt angle of 3257324_2 by 4 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259738_4
- `C11`: Decrease transmission power for 3257324_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259738_4
- `C13`: Adjust the azimuth of 3259738_4 by 50 degrees
- `C14`: Press down the tilt angle  of 3259738_4 by 10 degrees
- `C15`: Add neighbor relationship between 3257324_2 and 3259738_4
- `C16`: Add neighbor relationship between 3213724_1 and 3259738_4
- `C17`: Check test server and transmission issues
- `C18`: Decrease A3 Offset threshold for 3259738_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257324_2
- `C20`: Increase A3 Offset threshold for 3257324_2
- `C21`: Increase transmission power for 3259738_4
- `C22`: Decrease A3 Offset threshold for 3257324_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.808 | MS1 | 121.4656634941 | 31.1446364647 | 577 | 504990 | -81.52 | 17.97 | 353.33 | 0.07 | 2.38 | 1563 |
| 2024-09-20 22:21:32.721 | MS1 | 121.4656596642 | 31.1446198046 | 577 | 504990 | -84.35 | 12.08 | 441.48 | 0.10 | 2.26 | 1588 |
| 2024-09-20 22:21:33.185 | MS1 | 121.4656746956 | 31.1446288625 | 577 | 504990 | -76.78 | 16.51 | 577.27 | 0.00 | 2.60 | 1567 |
| 2024-09-20 22:21:34.207 | MS1 | 121.4656621085 | 31.1446360799 | 577 | 504990 | -90.26 | -2.07 | 48.15 | 0.15 | 1.25 | 1568 |
| 2024-09-20 22:21:35.924 | MS1 | 121.4656707034 | 31.1446338905 | 577 | 504990 | -83.59 | -3.37 | 72.20 | 0.12 | 1.46 | 1579 |
| 2024-09-20 22:21:36.691 | MS1 | 121.4656712416 | 31.1446201470 | 577 | 504990 | -85.36 | -3.51 | 41.25 | 0.09 | 1.34 | 1588 |
| 2024-09-20 22:21:37.336 | MS1 | 121.4656752124 | 31.1446270121 | 577 | 504990 | -91.72 | -1.15 | 45.73 | 0.01 | 1.41 | 1575 |
| 2024-09-20 22:21:38.998 | MS1 | 121.4656739324 | 31.1446246331 | 577 | 504990 | -87.59 | -2.01 | 56.39 | 0.04 | 1.37 | 1589 |
| 2024-09-20 22:21:39.774 | MS1 | 121.4656644019 | 31.1446227797 | 980 | 504990 | -82.33 | 13.73 | 216.76 | 0.01 | 1.22 | 1590 |
| 2024-09-20 22:21:40.867 | MS1 | 121.4656671798 | 31.1446266809 | 980 | 504990 | -76.85 | 14.88 | 413.64 | 0.12 | 2.04 | 1593 |
| 2024-09-20 22:21:41.226 | MS1 | 121.4656674911 | 31.1446325330 | 980 | 504990 | -75.09 | 13.28 | 349.79 | 0.04 | 2.41 | 1589 |
| 2024-09-20 22:21:42.349 | MS1 | 121.4656619353 | 31.1446253519 | 980 | 504990 | -79.42 | 13.30 | 478.55 | 0.05 | 2.10 | 1590 |

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
| 3213724 | 1 | 121.4735930190 | 31.1512424420 | 212 | 9 | 1 | 21.2 | TDD | 960 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3222736 | 3 | 121.4727074139 | 31.1547484364 | 253 | 10 | 1 | 37.6 | TDD | 929 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3257324 | 2 | 121.4648389261 | 31.1521003293 | 230 | 1 | 11 | 48.6 | TDD | 577 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3259738 | 4 | 121.4645935041 | 31.1544861748 | 51 | 10 | 3 | 16.8 | TDD | 980 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.355 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.374 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.482 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.482 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.243 | NREventA3 | measId:2;ServCellPCI:262;Se... |
| 2024-09-20 22:21:38.483 | NRHandoverAttempt | SourcePCI:262;SourceNR-ARFC... |
| 2024-09-20 22:21:38.533 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.547 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.676 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.676 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213724 | 1 | 16.9086 | 12.4407 | -116.8420 | 11.0477 | 144.5137 | 0.0112 | 0.0181 |
| 2024_09_20 22:00 | 3257324 | 2 | 13.3161 | 6.7909 | -116.9390 | 16.9832 | 190.1988 | 0.0060 | 0.1354 |
| 2024_09_20 22:00 | 3222736 | 3 | 14.5448 | 12.5993 | -117.7275 | 16.6651 | 105.4715 | 0.0105 | 0.0173 |
| 2024_09_20 22:00 | 3259738 | 4 | 5.7083 | 19.1049 | -117.3849 | 5.4205 | 114.1166 | 0.0066 | 0.0010 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414672_48E20349 | 504990 | 577 | -88.4 | 504990 | 980 | -85.9 | 504990 | 960 | -94.3 | 504990 | 929 |
| MR_1774414672_26A2BDB7 | 504990 | 577 | -91.7 | 504990 | 980 | -86.4 | 504990 | 960 | -93.7 | 504990 | 929 |
| MR_1774414672_C15611E0 | 504990 | 980 | -82.6 | 504990 | 577 | -90.8 | 504990 | 960 | -94.5 | 504990 | 929 |
| MR_1774414672_44551F79 | 504990 | 577 | -91.1 | 504990 | 980 | -83.1 | 504990 | 960 | -93.3 | 504990 | 929 |
| MR_1774414672_CE2C75B0 | 504990 | 980 | -84.5 | 504990 | 577 | -90.6 | 504990 | 960 | -96.2 | 504990 | 929 |
| MR_1774414672_941275F8 | 504990 | 577 | -91.7 | 504990 | 980 | -84.5 | 504990 | 960 | -93.6 | 504990 | 929 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 268: `cb1e7dd1-c6b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cb1e7dd1-c6b9-4bfa-98ad-2c446b47c449` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[268] topology](images/test_0268.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3256096_3 by 1 degrees
- `C2`: Add neighbor relationship between 3256096_3 and 3250807_1
- `C3`: Decrease transmission power for 3256096_3
- `C4`: Adjust the azimuth of 3250807_1 by 50 degrees
- `C5`: Decrease transmission power for 3250807_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256096_3
- `C7`: Add neighbor relationship between 3224275_2 and 3250807_1
- `C8`: Press down the tilt angle  of 3250807_1 by 10 degrees
- `C9`: Decrease A3 Offset threshold for 3256096_3
- `C10`: Adjust the azimuth of 3256096_3 by 34 degrees
- `C11`: Check test server and transmission issues
- `C12`: Increase transmission power for 3256096_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250807_1
- `C14`: Increase A3 Offset threshold for 3250807_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256096_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250807_1
- `C17`: Lift the tilt angle  of 3250807_1 by 10 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Increase A3 Offset threshold for 3256096_3
- `C20`: Decrease A3 Offset threshold for 3250807_1
- `C21`: Press down the tilt angle of 3256096_3 by 1 degrees
- `C22`: Increase transmission power for 3250807_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.566 | MS1 | 121.4656597417 | 31.1446313622 | 421 | 504990 | -86.12 | 15.42 | 484.69 | 0.13 | 2.77 | 1560 |
| 2024-09-20 22:21:32.891 | MS1 | 121.4656614307 | 31.1446218077 | 421 | 504990 | -90.49 | 12.56 | 439.04 | 0.17 | 2.84 | 1579 |
| 2024-09-20 22:21:33.572 | MS1 | 121.4656673730 | 31.1446277807 | 421 | 504990 | -86.15 | 12.98 | 397.95 | 0.12 | 2.28 | 1600 |
| 2024-09-20 22:21:34.463 | MS1 | 121.4656604565 | 31.1446264806 | 421 | 504990 | -90.12 | 16.46 | 53.95 | 0.53 | 2.57 | 632 |
| 2024-09-20 22:21:35.798 | MS1 | 121.4656593310 | 31.1446241102 | 421 | 504990 | -89.58 | 16.49 | 71.23 | 0.68 | 2.68 | 557 |
| 2024-09-20 22:21:36.992 | MS1 | 121.4656706080 | 31.1446354864 | 421 | 504990 | -91.91 | 14.14 | 89.41 | 0.56 | 2.55 | 558 |
| 2024-09-20 22:21:37.510 | MS1 | 121.4656616475 | 31.1446277324 | 421 | 504990 | -91.49 | 9.78 | 77.35 | 0.56 | 2.51 | 597 |
| 2024-09-20 22:21:38.403 | MS1 | 121.4656719181 | 31.1446195313 | 421 | 504990 | -90.23 | 11.32 | 85.97 | 0.59 | 2.01 | 615 |
| 2024-09-20 22:21:39.332 | MS1 | 121.4656619847 | 31.1446349551 | 421 | 504990 | -92.80 | 9.53 | 87.29 | 0.61 | 2.86 | 664 |
| 2024-09-20 22:21:40.936 | MS1 | 121.4656701922 | 31.1446349247 | 421 | 504990 | -89.00 | 7.41 | 508.62 | 0.04 | 2.94 | 1566 |
| 2024-09-20 22:21:41.181 | MS1 | 121.4656703657 | 31.1446359397 | 421 | 504990 | -92.84 | 9.43 | 453.02 | 0.05 | 2.07 | 1579 |
| 2024-09-20 22:21:42.202 | MS1 | 121.4656618257 | 31.1446225460 | 421 | 504990 | -90.70 | 8.45 | 460.74 | 0.12 | 2.51 | 1571 |

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
| 3224275 | 2 | 121.4685248734 | 31.1478951497 | 37 | 13 | 2 | 48.4 | TDD | 715 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3239313 | 4 | 121.4715542795 | 31.1459450981 | 27 | 9 | 10 | 17.6 | TDD | 783 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3250807 | 1 | 121.4728905764 | 31.1443853616 | 353 | 10 | 6 | 37.8 | TDD | 233 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3256096 | 3 | 121.4679028201 | 31.1542643473 | 225 | 0 | 11 | 16.2 | TDD | 421 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.078 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.094 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.244 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.244 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.916 | NREventA3 | measId:2;ServCellPCI:635;Se... |
| 2024-09-20 22:21:38.156 | NRHandoverAttempt | SourcePCI:635;SourceNR-ARFC... |
| 2024-09-20 22:21:38.202 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.214 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.316 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.316 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250807 | 1 | 5.0434 | 11.4272 | -116.3121 | 13.8942 | 146.0910 | 0.0076 | 0.0092 |
| 2024_09_20 22:00 | 3224275 | 2 | 7.1999 | 12.1254 | -114.3003 | 11.7322 | 138.0523 | 0.0056 | 0.0095 |
| 2024_09_20 22:00 | 3256096 | 3 | 5.6421 | 7.1308 | -117.1700 | 7.2426 | 156.5929 | 0.0035 | 0.0176 |
| 2024_09_20 22:00 | 3239313 | 4 | 18.8455 | 11.6052 | -117.4044 | 5.7545 | 192.2580 | 0.0133 | 0.0122 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416748_450F2B63 | 504990 | 421 | -89.7 | 504990 | 233 | -93.3 | 504990 | 715 | -102.3 | 504990 | 783 |
| MR_1774416748_8FBE915B | 504990 | 421 | -91.3 | 504990 | 233 | -93.4 | 504990 | 715 | -103.0 | 504990 | 783 |
| MR_1774416748_C4329573 | 504990 | 421 | -88.6 | 504990 | 233 | -93.2 | 504990 | 715 | -103.4 | 504990 | 783 |
| MR_1774416748_AFE79A7F | 504990 | 421 | -89.2 | 504990 | 233 | -94.4 | 504990 | 715 | -103.1 | 504990 | 783 |
| MR_1774416748_455F5A57 | 504990 | 421 | -89.9 | 504990 | 233 | -93.4 | 504990 | 715 | -102.2 | 504990 | 783 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 269: `22b185a7-d5d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `22b185a7-d5d6-411b-86b5-4cae5a7cd1ff` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[269] topology](images/test_0269.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3278553_3 by 50 degrees
- `C2`: Increase A3 Offset threshold for 3278553_3
- `C3`: Lift the tilt angle  of 3269993_1 by 3 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278553_3
- `C6`: Lift the tilt angle of 3278553_3 by 10 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269993_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278553_3
- `C9`: Decrease A3 Offset threshold for 3269993_1
- `C10`: Increase transmission power for 3269993_1
- `C11`: Press down the tilt angle  of 3269993_1 by 3 degrees
- `C12`: Decrease transmission power for 3269993_1
- `C13`: Press down the tilt angle of 3278553_3 by 10 degrees
- `C14`: Check test server and transmission issues
- `C15`: Decrease A3 Offset threshold for 3278553_3
- `C16`: Add neighbor relationship between 3226070_2 and 3269993_1
- `C17`: Increase A3 Offset threshold for 3269993_1
- `C18`: Add neighbor relationship between 3278553_3 and 3269993_1
- `C19`: Increase transmission power for 3278553_3
- `C20`: Decrease transmission power for 3278553_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269993_1
- `C22`: Adjust the azimuth of 3269993_1 by 12 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.622 | MS1 | 121.4656720614 | 31.1446227780 | 430 | 504990 | -83.36 | 13.45 | 557.30 | 0.05 | 2.29 | 1574 |
| 2024-09-20 22:21:32.468 | MS1 | 121.4656670551 | 31.1446261631 | 430 | 504990 | -82.71 | 15.43 | 395.19 | 0.14 | 2.44 | 1586 |
| 2024-09-20 22:21:33.593 | MS1 | 121.4656672368 | 31.1446283830 | 430 | 504990 | -76.75 | 12.30 | 325.06 | 0.05 | 2.04 | 1578 |
| 2024-09-20 22:21:34.933 | MS1 | 121.4656651173 | 31.1446188004 | 430 | 504990 | -94.97 | -0.87 | 61.35 | 0.07 | 1.00 | 1573 |
| 2024-09-20 22:21:35.268 | MS1 | 121.4656638325 | 31.1446369304 | 430 | 504990 | -91.14 | -2.32 | 77.18 | 0.05 | 1.29 | 1583 |
| 2024-09-20 22:21:36.614 | MS1 | 121.4656715469 | 31.1446234741 | 430 | 504990 | -85.86 | -0.45 | 43.74 | 0.00 | 1.41 | 1560 |
| 2024-09-20 22:21:37.891 | MS1 | 121.4656659619 | 31.1446269591 | 430 | 504990 | -89.23 | -1.72 | 43.50 | 0.20 | 1.32 | 1589 |
| 2024-09-20 22:21:38.506 | MS1 | 121.4656774006 | 31.1446197690 | 430 | 504990 | -84.48 | 17.46 | 424.62 | 0.17 | 1.09 | 1571 |
| 2024-09-20 22:21:39.904 | MS1 | 121.4656596639 | 31.1446235217 | 430 | 504990 | -78.03 | 16.85 | 380.47 | 0.08 | 1.05 | 1593 |
| 2024-09-20 22:21:40.919 | MS1 | 121.4656776869 | 31.1446363776 | 430 | 504990 | -84.55 | 14.42 | 449.36 | 0.13 | 2.34 | 1588 |
| 2024-09-20 22:21:41.578 | MS1 | 121.4656697828 | 31.1446246841 | 430 | 504990 | -83.71 | 17.02 | 562.25 | 0.01 | 2.32 | 1598 |
| 2024-09-20 22:21:42.468 | MS1 | 121.4656680793 | 31.1446362668 | 430 | 504990 | -78.91 | 15.96 | 352.11 | 0.16 | 2.36 | 1576 |

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
| 3226070 | 2 | 121.4752179923 | 31.1496696746 | 257 | 1 | 7 | 17.8 | TDD | 892 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3243317 | 4 | 121.4670625668 | 31.1463129376 | 112 | 15 | 3 | 38.5 | TDD | 447 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3269993 | 1 | 121.4744396222 | 31.1507908349 | 219 | 1 | 11 | 40.5 | TDD | 298 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3278553 | 3 | 121.4699669454 | 31.1507003408 | 144 | 14 | 2 | 34.6 | TDD | 430 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.600 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.615 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.728 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.728 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.455 | NREventA3 | measId:2;ServCellPCI:185;Se... |
| 2024-09-20 22:21:36.455 | NREventA3 | measId:2;ServCellPCI:185;Se... |
| 2024-09-20 22:21:37.455 | NREventA3 | measId:2;ServCellPCI:185;Se... |
| 2024-09-20 22:21:39.955 | NRRRCReestablishAttempt | PCI:185 |
| 2024-09-20 22:21:39.975 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.990 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:40.130 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.130 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269993 | 1 | 19.8248 | 17.7435 | -117.9327 | 9.6259 | 135.0709 | 0.0164 | 0.0025 |
| 2024_09_20 22:00 | 3226070 | 2 | 14.4064 | 6.5009 | -116.4680 | 17.2596 | 149.7052 | 0.0096 | 0.0022 |
| 2024_09_20 22:00 | 3278553 | 3 | 19.9872 | 5.7298 | -115.2021 | 14.1007 | 98.2371 | 0.0104 | 0.1705 |
| 2024_09_20 22:00 | 3243317 | 4 | 16.9421 | 15.5450 | -116.3609 | 14.6334 | 126.4430 | 0.0135 | 0.0108 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412725_B1BC0A6F | 504990 | 430 | -94.7 | 504990 | 298 | -89.7 | 504990 | 892 | -93.5 | 504990 | 447 |
| MR_1774412725_CDFC1C64 | 504990 | 298 | -88.8 | 504990 | 430 | -94.7 | 504990 | 892 | -93.0 | 504990 | 447 |
| MR_1774412725_0DC24179 | 504990 | 430 | -96.7 | 504990 | 298 | -91.0 | 504990 | 892 | -93.8 | 504990 | 447 |
| MR_1774412725_22C18403 | 504990 | 430 | -94.5 | 504990 | 298 | -88.3 | 504990 | 892 | -93.7 | 504990 | 447 |
| MR_1774412725_7727677B | 504990 | 298 | -91.1 | 504990 | 430 | -95.9 | 504990 | 892 | -94.6 | 504990 | 447 |
| MR_1774412725_32BE4FCA | 504990 | 430 | -93.5 | 504990 | 298 | -90.5 | 504990 | 892 | -94.6 | 504990 | 447 |
| MR_1774412725_01658327 | 504990 | 298 | -91.4 | 504990 | 430 | -94.1 | 504990 | 892 | -92.7 | 504990 | 447 |

> *... 2개 열 생략 (전체 14열)*

---
