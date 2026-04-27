# Track A 문제 분석 — train[300]~train[309]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[300] ~ train[309] (10개)

## 목차

1. [문제 300: `b151ed0a-f28...`](#300) — single-answer, 정답: C13
2. [문제 301: `2f5b918c-5d1...`](#301) — single-answer, 정답: C1
3. [문제 302: `1730396d-9db...`](#302) — multiple-answer, 정답: C16|C22
4. [문제 303: `f7f5179f-7a6...`](#303) — multiple-answer, 정답: C2|C12
5. [문제 304: `9bb9f929-f7f...`](#304) — single-answer, 정답: C19
6. [문제 305: `0ceec2b3-965...`](#305) — single-answer, 정답: C10
7. [문제 306: `a64bf070-be9...`](#306) — single-answer, 정답: C13
8. [문제 307: `8b93f2b7-099...`](#307) — single-answer, 정답: C3
9. [문제 308: `5c53a9cc-111...`](#308) — single-answer, 정답: C14
10. [문제 309: `890d3724-170...`](#309) — single-answer, 정답: C13

---

### 문제 300: `b151ed0a-f28...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b151ed0a-f28c-4803-945b-850bf690bf53` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3250050_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[300] topology](images/train_0300.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3231883_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231883_1
- `C3`: Adjust the azimuth of 3231883_1 by 50 degrees
- `C4`: Add neighbor relationship between 3245982_4 and 3231883_1
- `C5`: Decrease transmission power for 3250050_2
- `C6`: Lift the tilt angle of 3250050_2 by 4 degrees
- `C7`: Increase A3 Offset threshold for 3250050_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250050_2
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Add neighbor relationship between 3250050_2 and 3231883_1
- `C11`: Decrease A3 Offset threshold for 3231883_1
- `C12`: Decrease transmission power for 3231883_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250050_2 **← 정답**
- `C14`: Increase A3 Offset threshold for 3231883_1
- `C15`: Check test server and transmission issues
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231883_1
- `C17`: Press down the tilt angle of 3250050_2 by 4 degrees
- `C18`: Press down the tilt angle  of 3231883_1 by 4 degrees
- `C19`: Increase transmission power for 3250050_2
- `C20`: Adjust the azimuth of 3250050_2 by 35 degrees
- `C21`: Decrease A3 Offset threshold for 3250050_2
- `C22`: Lift the tilt angle  of 3231883_1 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.583 | MS1 | 121.4656590742 | 31.1446203599 | 345 | 504990 | -89.41 | 15.62 | 404.02 | 0.02 | 2.88 | 1578 |
| 2024-09-20 22:21:32.371 | MS1 | 121.4656590292 | 31.1446338811 | 345 | 504990 | -91.37 | 12.74 | 536.04 | 0.10 | 2.65 | 1572 |
| 2024-09-20 22:21:33.812 | MS1 | 121.4656582727 | 31.1446314360 | 345 | 504990 | -87.29 | 12.56 | 389.07 | 0.16 | 2.77 | 1566 |
| 2024-09-20 22:21:34.276 | MS1 | 121.4656684270 | 31.1446316515 | 345 | 504990 | -91.70 | 12.50 | 83.72 | 0.58 | 2.21 | 560 |
| 2024-09-20 22:21:35.962 | MS1 | 121.4656719328 | 31.1446285147 | 345 | 504990 | -90.58 | 14.93 | 85.97 | 0.67 | 2.75 | 525 |
| 2024-09-20 22:21:36.719 | MS1 | 121.4656704748 | 31.1446271498 | 345 | 504990 | -88.30 | 12.26 | 44.58 | 0.51 | 2.34 | 548 |
| 2024-09-20 22:21:37.364 | MS1 | 121.4656580533 | 31.1446238578 | 345 | 504990 | -89.50 | 7.95 | 62.12 | 0.59 | 2.66 | 675 |
| 2024-09-20 22:21:38.278 | MS1 | 121.4656778182 | 31.1446288428 | 345 | 504990 | -90.13 | 8.87 | 66.18 | 0.66 | 2.90 | 629 |
| 2024-09-20 22:21:39.722 | MS1 | 121.4656724916 | 31.1446187048 | 345 | 504990 | -91.86 | 9.95 | 61.07 | 0.50 | 2.67 | 583 |
| 2024-09-20 22:21:40.108 | MS1 | 121.4656614523 | 31.1446245340 | 345 | 504990 | -91.27 | 12.71 | 361.45 | 0.15 | 2.15 | 1582 |
| 2024-09-20 22:21:41.634 | MS1 | 121.4656771546 | 31.1446230333 | 345 | 504990 | -89.57 | 11.72 | 545.45 | 0.18 | 2.65 | 1564 |
| 2024-09-20 22:21:42.831 | MS1 | 121.4656726381 | 31.1446254944 | 345 | 504990 | -92.05 | 12.47 | 369.00 | 0.02 | 2.51 | 1593 |

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
| 3231883 | 1 | 121.4648136380 | 31.1484876761 | 22 | 2 | 0 | 17.0 | TDD | 152 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3245982 | 4 | 121.4691282623 | 31.1460000516 | 152 | 11 | 11 | 17.9 | TDD | 888 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3250050 | 2 | 121.4728675836 | 31.1480932700 | 276 | 2 | 4 | 32.7 | TDD | 345 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3250916 | 3 | 121.4671677519 | 31.1514870122 | 356 | 12 | 11 | 15.2 | TDD | 568 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.513 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.538 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.661 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.661 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.332 | NREventA3 | measId:2;ServCellPCI:779;Se... |
| 2024-09-20 22:21:38.572 | NRHandoverAttempt | SourcePCI:779;SourceNR-ARFC... |
| 2024-09-20 22:21:38.613 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.624 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.768 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.768 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231883 | 1 | 11.9803 | 19.7561 | -115.8156 | 17.4206 | 155.8821 | 0.0126 | 0.0073 |
| 2024_09_20 22:00 | 3250050 | 2 | 13.8484 | 8.9550 | -115.9609 | 19.4150 | 168.3917 | 0.0120 | 0.0036 |
| 2024_09_20 22:00 | 3250916 | 3 | 5.6819 | 9.2368 | -116.7242 | 5.2287 | 172.2123 | 0.0079 | 0.0019 |
| 2024_09_20 22:00 | 3245982 | 4 | 18.0046 | 16.3654 | -114.2446 | 7.8394 | 141.8613 | 0.0086 | 0.0007 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417185_AA4CCA4F | 504990 | 345 | -91.1 | 504990 | 152 | -93.9 | 504990 | 888 | -103.5 | 504990 | 568 |
| MR_1774417185_5C3AAABE | 504990 | 345 | -91.0 | 504990 | 152 | -97.0 | 504990 | 888 | -103.5 | 504990 | 568 |
| MR_1774417185_32A8B3D0 | 504990 | 345 | -90.5 | 504990 | 152 | -96.1 | 504990 | 888 | -101.9 | 504990 | 568 |
| MR_1774417185_B3245E5F | 504990 | 345 | -91.1 | 504990 | 152 | -96.6 | 504990 | 888 | -102.5 | 504990 | 568 |
| MR_1774417185_90460664 | 504990 | 345 | -91.1 | 504990 | 152 | -96.2 | 504990 | 888 | -101.9 | 504990 | 568 |
| MR_1774417185_E98822BE | 504990 | 345 | -93.5 | 504990 | 152 | -97.5 | 504990 | 888 | -101.7 | 504990 | 568 |
| MR_1774417185_0156A8B4 | 504990 | 345 | -92.1 | 504990 | 152 | -97.1 | 504990 | 888 | -102.6 | 504990 | 568 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 301: `2f5b918c-5d1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2f5b918c-5d1a-4606-9e69-1f8d1439ef79` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[301] topology](images/train_0301.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment. **← 정답**
- `C2`: Decrease transmission power for 3269529_3
- `C3`: Adjust the azimuth of 3215448_4 by 50 degrees
- `C4`: Decrease A3 Offset threshold for 3215448_4
- `C5`: Decrease A3 Offset threshold for 3269529_3
- `C6`: Add neighbor relationship between 3269529_3 and 3215448_4
- `C7`: Lift the tilt angle  of 3215448_4 by 7 degrees
- `C8`: Decrease transmission power for 3215448_4
- `C9`: Lift the tilt angle of 3269529_3 by 10 degrees
- `C10`: Adjust the azimuth of 3269529_3 by 50 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269529_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215448_4
- `C13`: Press down the tilt angle of 3269529_3 by 10 degrees
- `C14`: Add neighbor relationship between 3214076_2 and 3215448_4
- `C15`: Increase transmission power for 3269529_3
- `C16`: Increase A3 Offset threshold for 3215448_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215448_4
- `C18`: Check test server and transmission issues
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269529_3
- `C20`: Press down the tilt angle  of 3215448_4 by 7 degrees
- `C21`: Increase A3 Offset threshold for 3269529_3
- `C22`: Increase transmission power for 3215448_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.626 | MS1 | 121.4656713043 | 31.1446330039 | 138 | 504990 | -89.97 | 15.35 | 481.59 | 0.12 | 2.86 | 1589 |
| 2024-09-20 22:21:32.876 | MS1 | 121.4656676535 | 31.1446220841 | 138 | 504990 | -91.39 | 17.93 | 452.96 | 0.17 | 2.16 | 1594 |
| 2024-09-20 22:21:33.881 | MS1 | 121.4656643472 | 31.1446282871 | 138 | 504990 | -86.95 | 16.37 | 536.24 | 0.06 | 2.89 | 1593 |
| 2024-09-20 22:21:34.308 | MS1 | 121.4656705256 | 31.1446237674 | 138 | 504990 | -91.32 | 17.08 | 99.43 | 0.07 | 2.86 | 1582 |
| 2024-09-20 22:21:35.597 | MS1 | 121.4656761805 | 31.1446310067 | 138 | 504990 | -86.40 | 14.93 | 97.82 | 0.11 | 2.31 | 1600 |
| 2024-09-20 22:21:36.557 | MS1 | 121.4656623209 | 31.1446337868 | 138 | 504990 | -89.11 | 16.18 | 87.79 | 0.13 | 2.74 | 1572 |
| 2024-09-20 22:21:37.521 | MS1 | 121.4656610594 | 31.1446360914 | 138 | 504990 | -89.82 | 8.13 | 56.55 | 0.07 | 2.96 | 1600 |
| 2024-09-20 22:21:38.401 | MS1 | 121.4656740780 | 31.1446369904 | 138 | 504990 | -92.02 | 9.30 | 80.39 | 0.07 | 2.72 | 1574 |
| 2024-09-20 22:21:39.924 | MS1 | 121.4656621588 | 31.1446200619 | 138 | 504990 | -89.07 | 8.25 | 102.04 | 0.14 | 2.02 | 1564 |
| 2024-09-20 22:21:40.711 | MS1 | 121.4656723579 | 31.1446187387 | 138 | 504990 | -92.21 | 8.04 | 464.10 | 0.05 | 2.67 | 1579 |
| 2024-09-20 22:21:41.146 | MS1 | 121.4656673487 | 31.1446365626 | 138 | 504990 | -93.08 | 9.31 | 436.54 | 0.15 | 2.41 | 1577 |
| 2024-09-20 22:21:42.945 | MS1 | 121.4656646685 | 31.1446315726 | 138 | 504990 | -90.97 | 7.26 | 325.86 | 0.12 | 2.12 | 1592 |

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
| 3214076 | 2 | 121.4708190967 | 31.1542109732 | 231 | 4 | 6 | 30.1 | TDD | 489 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3215448 | 4 | 121.4698677754 | 31.1485319820 | 97 | 3 | 9 | 43.4 | TDD | 804 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3257924 | 1 | 121.4663205717 | 31.1525455935 | 173 | 15 | 3 | 16.3 | TDD | 304 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3269529 | 3 | 121.4729818532 | 31.1513465013 | 289 | 15 | 4 | 44.2 | TDD | 138 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.378 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.401 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.506 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.506 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.193 | NREventA3 | measId:2;ServCellPCI:54;Ser... |
| 2024-09-20 22:21:38.433 | NRHandoverAttempt | SourcePCI:54;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.477 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.487 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.637 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.637 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3257924 | 1 | 76.4535 | 79.0273 | -116.3016 | 10.3076 | 190.2480 | 0.0082 | 0.0173 |
| 2024_09_19 22:00 | 3214076 | 2 | 92.5350 | 78.3450 | -117.8489 | 13.4004 | 164.2666 | 0.0110 | 0.0186 |
| 2024_09_19 22:00 | 3269529 | 3 | 83.0485 | 80.2630 | -114.0933 | 17.3090 | 118.0986 | 0.0154 | 0.0127 |
| 2024_09_19 22:00 | 3215448 | 4 | 79.5301 | 93.6474 | -115.8178 | 11.0073 | 113.5867 | 0.0113 | 0.0009 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415431_C058AC2C | 504990 | 138 | -91.6 | 504990 | 804 | -94.6 | 504990 | 489 | -96.9 | 504990 | 304 |
| MR_1774415431_0AD7815C | 504990 | 138 | -92.0 | 504990 | 804 | -97.4 | 504990 | 489 | -97.6 | 504990 | 304 |
| MR_1774415431_FEE7C9ED | 504990 | 138 | -89.5 | 504990 | 804 | -95.2 | 504990 | 489 | -96.2 | 504990 | 304 |
| MR_1774415431_1B9AC230 | 504990 | 138 | -90.1 | 504990 | 804 | -97.2 | 504990 | 489 | -96.2 | 504990 | 304 |
| MR_1774415431_D86BBA94 | 504990 | 138 | -91.2 | 504990 | 804 | -98.0 | 504990 | 489 | -95.8 | 504990 | 304 |
| MR_1774415431_F79213E6 | 504990 | 138 | -89.8 | 504990 | 804 | -98.2 | 504990 | 489 | -97.4 | 504990 | 304 |
| MR_1774415431_19039331 | 504990 | 138 | -92.4 | 504990 | 804 | -96.2 | 504990 | 489 | -99.1 | 504990 | 304 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 302: `1730396d-9db...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1730396d-9dbf-418b-8084-6fd2fafb4a2e` |
| Tag | **multiple-answer** |
| 정답 | **C16|C22** |
| C16 의미 | Press down the tilt angle  of 3274140_2 by 3 degrees |
| C22 의미 | Decrease transmission power for 3274140_2 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[302] topology](images/train_0302.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230078_3
- `C2`: Decrease transmission power for 3230078_3
- `C3`: Check test server and transmission issues
- `C4`: Adjust the azimuth of 3274140_2 by 1 degrees
- `C5`: Increase A3 Offset threshold for 3274140_2
- `C6`: Increase A3 Offset threshold for 3230078_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274140_2
- `C8`: Add neighbor relationship between 3256712_4 and 3274140_2
- `C9`: Decrease A3 Offset threshold for 3274140_2
- `C10`: Add neighbor relationship between 3230078_3 and 3274140_2
- `C11`: Press down the tilt angle of 3230078_3 by 4 degrees
- `C12`: Lift the tilt angle  of 3274140_2 by 3 degrees
- `C13`: Lift the tilt angle of 3230078_3 by 4 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274140_2
- `C15`: Adjust the azimuth of 3230078_3 by 41 degrees
- `C16`: Press down the tilt angle  of 3274140_2 by 3 degrees **← 정답**
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230078_3
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Increase transmission power for 3274140_2
- `C20`: Increase transmission power for 3230078_3
- `C21`: Decrease A3 Offset threshold for 3230078_3
- `C22`: Decrease transmission power for 3274140_2 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.116 | MS1 | 121.4656682738 | 31.1446227830 | 355 | 504990 | -76.84 | 17.28 | 544.36 | 0.03 | 2.76 | 1585 |
| 2024-09-20 22:21:32.600 | MS1 | 121.4656732721 | 31.1446343224 | 355 | 504990 | -83.41 | 16.67 | 541.95 | 0.05 | 2.78 | 1578 |
| 2024-09-20 22:21:33.503 | MS1 | 121.4656706378 | 31.1446223826 | 355 | 504990 | -77.53 | 17.03 | 500.62 | 0.16 | 2.50 | 1599 |
| 2024-09-20 22:21:34.595 | MS1 | 121.4656743678 | 31.1446296341 | 355 | 504990 | -93.84 | 2.83 | 53.01 | 0.15 | 1.31 | 1573 |
| 2024-09-20 22:21:35.620 | MS1 | 121.4656717407 | 31.1446345755 | 355 | 504990 | -90.92 | 3.76 | 33.94 | 0.15 | 1.36 | 1594 |
| 2024-09-20 22:21:36.849 | MS1 | 121.4656722732 | 31.1446233728 | 355 | 504990 | -93.41 | 0.07 | 63.85 | 0.12 | 1.48 | 1582 |
| 2024-09-20 22:21:37.354 | MS1 | 121.4656585293 | 31.1446307746 | 355 | 504990 | -91.51 | 3.15 | 77.98 | 0.00 | 1.05 | 1566 |
| 2024-09-20 22:21:38.130 | MS1 | 121.4656722802 | 31.1446336034 | 355 | 504990 | -89.01 | 0.42 | 62.05 | 0.14 | 1.21 | 1585 |
| 2024-09-20 22:21:39.810 | MS1 | 121.4656754854 | 31.1446252662 | 355 | 504990 | -86.81 | 3.76 | 66.95 | 0.19 | 1.10 | 1582 |
| 2024-09-20 22:21:40.236 | MS1 | 121.4656760250 | 31.1446352219 | 355 | 504990 | -80.81 | 13.17 | 361.46 | 0.02 | 2.30 | 1588 |
| 2024-09-20 22:21:41.890 | MS1 | 121.4656583371 | 31.1446350838 | 355 | 504990 | -83.65 | 12.57 | 425.96 | 0.08 | 2.50 | 1599 |
| 2024-09-20 22:21:42.179 | MS1 | 121.4656734332 | 31.1446332830 | 355 | 504990 | -76.35 | 16.88 | 321.53 | 0.17 | 2.78 | 1586 |

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
| 3230078 | 3 | 121.4730772579 | 31.1485828114 | 279 | 2 | 9 | 30.1 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3251156 | 1 | 121.4729408638 | 31.1544129292 | 73 | 5 | 1 | 29.0 | TDD | 697 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3256712 | 4 | 121.4663249085 | 31.1479413663 | 262 | 1 | 5 | 25.4 | TDD | 542 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3274140 | 2 | 121.4684491820 | 31.1538663196 | 195 | 0 | 1 | 46.7 | TDD | 586 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.845 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.970 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.970 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251156 | 1 | 18.4897 | 15.1890 | -116.9441 | 16.2483 | 156.6248 | 0.0005 | 0.0081 |
| 2024_09_20 22:00 | 3274140 | 2 | 8.7251 | 15.0272 | -115.1080 | 18.9527 | 146.3856 | 0.0080 | 0.0102 |
| 2024_09_20 22:00 | 3230078 | 3 | 10.2961 | 10.0509 | -108.6987 | 18.9615 | 111.1156 | 0.0170 | 0.0036 |
| 2024_09_20 22:00 | 3256712 | 4 | 16.2651 | 14.9612 | -115.8921 | 11.2822 | 132.8815 | 0.0162 | 0.0105 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415996_EB9DC9F6 | 504990 | 355 | -92.7 | 504990 | 586 | -93.8 | 504990 | 542 | -96.2 | 504990 | 697 |
| MR_1774415996_9C19DB4C | 504990 | 586 | -93.2 | 504990 | 355 | -95.5 | 504990 | 542 | -93.9 | 504990 | 697 |
| MR_1774415996_961AD36F | 504990 | 355 | -94.3 | 504990 | 586 | -95.4 | 504990 | 542 | -95.0 | 504990 | 697 |
| MR_1774415996_043A0ABC | 504990 | 586 | -91.9 | 504990 | 355 | -94.4 | 504990 | 542 | -96.5 | 504990 | 697 |
| MR_1774415996_934D7DBC | 504990 | 586 | -92.9 | 504990 | 355 | -94.3 | 504990 | 542 | -96.3 | 504990 | 697 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 303: `f7f5179f-7a6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f7f5179f-7a68-4bd4-aed4-8ea29192e6ec` |
| Tag | **multiple-answer** |
| 정답 | **C2|C12** |
| C2 의미 | Press down the tilt angle  of 3219232_1 by 2 degrees |
| C12 의미 | Decrease transmission power for 3219232_1 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[303] topology](images/train_0303.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3249613_3 by 2 degrees
- `C2`: Press down the tilt angle  of 3219232_1 by 2 degrees **← 정답**
- `C3`: Increase transmission power for 3249613_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219232_1
- `C5`: Adjust the azimuth of 3219232_1 by 21 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249613_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249613_3
- `C8`: Lift the tilt angle  of 3219232_1 by 2 degrees
- `C9`: Increase transmission power for 3219232_1
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease A3 Offset threshold for 3249613_3
- `C12`: Decrease transmission power for 3219232_1 **← 정답**
- `C13`: Increase A3 Offset threshold for 3249613_3
- `C14`: Increase A3 Offset threshold for 3219232_1
- `C15`: Press down the tilt angle of 3249613_3 by 2 degrees
- `C16`: Add neighbor relationship between 3244676_4 and 3219232_1
- `C17`: Check test server and transmission issues
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219232_1
- `C19`: Decrease transmission power for 3249613_3
- `C20`: Adjust the azimuth of 3249613_3 by 12 degrees
- `C21`: Decrease A3 Offset threshold for 3219232_1
- `C22`: Add neighbor relationship between 3249613_3 and 3219232_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.593 | MS1 | 121.4656603072 | 31.1446335785 | 757 | 504990 | -81.84 | 15.82 | 323.19 | 0.15 | 2.50 | 1585 |
| 2024-09-20 22:21:32.975 | MS1 | 121.4656700536 | 31.1446315955 | 757 | 504990 | -76.10 | 15.12 | 522.87 | 0.09 | 2.93 | 1597 |
| 2024-09-20 22:21:33.698 | MS1 | 121.4656618246 | 31.1446293412 | 757 | 504990 | -82.27 | 16.29 | 565.96 | 0.02 | 2.90 | 1591 |
| 2024-09-20 22:21:34.124 | MS1 | 121.4656744035 | 31.1446324148 | 757 | 504990 | -86.21 | 1.51 | 46.72 | 0.20 | 1.22 | 1560 |
| 2024-09-20 22:21:35.630 | MS1 | 121.4656585327 | 31.1446366178 | 757 | 504990 | -86.21 | 0.02 | 68.41 | 0.05 | 1.35 | 1587 |
| 2024-09-20 22:21:36.727 | MS1 | 121.4656750958 | 31.1446328444 | 757 | 504990 | -85.72 | 2.88 | 77.82 | 0.08 | 1.08 | 1579 |
| 2024-09-20 22:21:37.203 | MS1 | 121.4656600340 | 31.1446347754 | 757 | 504990 | -85.51 | 1.38 | 78.94 | 0.10 | 1.37 | 1576 |
| 2024-09-20 22:21:38.152 | MS1 | 121.4656756977 | 31.1446216374 | 757 | 504990 | -89.04 | 2.63 | 68.39 | 0.10 | 1.11 | 1578 |
| 2024-09-20 22:21:39.827 | MS1 | 121.4656636859 | 31.1446185171 | 757 | 504990 | -87.04 | 3.85 | 61.61 | 0.06 | 1.11 | 1570 |
| 2024-09-20 22:21:40.832 | MS1 | 121.4656666033 | 31.1446183376 | 757 | 504990 | -75.46 | 14.24 | 548.80 | 0.10 | 2.53 | 1567 |
| 2024-09-20 22:21:41.726 | MS1 | 121.4656700270 | 31.1446198193 | 757 | 504990 | -76.85 | 15.09 | 373.41 | 0.19 | 2.40 | 1598 |
| 2024-09-20 22:21:42.961 | MS1 | 121.4656751931 | 31.1446277539 | 757 | 504990 | -76.25 | 14.23 | 577.05 | 0.12 | 2.01 | 1594 |

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
| 3219232 | 1 | 121.4667680628 | 31.1533905974 | 207 | 0 | 11 | 34.8 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3219661 | 2 | 121.4732354894 | 31.1548975702 | 213 | 7 | 10 | 27.6 | TDD | 315 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3244676 | 4 | 121.4720270793 | 31.1515016118 | 213 | 2 | 1 | 23.0 | TDD | 271 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3249613 | 3 | 121.4731316290 | 31.1534991371 | 204 | 0 | 1 | 35.3 | TDD | 757 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.089 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.113 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.230 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.230 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219232 | 1 | 15.4354 | 10.5340 | -114.8665 | 18.9270 | 103.9183 | 0.0075 | 0.0078 |
| 2024_09_20 22:00 | 3219661 | 2 | 17.4441 | 7.6269 | -117.3570 | 10.7401 | 166.8509 | 0.0183 | 0.0127 |
| 2024_09_20 22:00 | 3249613 | 3 | 18.4919 | 13.8755 | -108.7491 | 7.2198 | 105.2659 | 0.0132 | 0.0095 |
| 2024_09_20 22:00 | 3244676 | 4 | 8.7041 | 12.8033 | -116.2450 | 16.1514 | 107.8487 | 0.0008 | 0.0135 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412975_CC8F8BA1 | 504990 | 176 | -85.6 | 504990 | 757 | -84.0 | 504990 | 271 | -85.4 | 504990 | 315 |
| MR_1774412975_B49676EC | 504990 | 757 | -87.4 | 504990 | 176 | -84.3 | 504990 | 271 | -82.6 | 504990 | 315 |
| MR_1774412975_416C2DE1 | 504990 | 176 | -85.0 | 504990 | 757 | -83.2 | 504990 | 271 | -83.9 | 504990 | 315 |
| MR_1774412975_A844760F | 504990 | 757 | -87.9 | 504990 | 176 | -81.8 | 504990 | 271 | -84.1 | 504990 | 315 |
| MR_1774412975_7F721E6E | 504990 | 757 | -86.8 | 504990 | 176 | -82.9 | 504990 | 271 | -83.3 | 504990 | 315 |
| MR_1774412975_F4E42F80 | 504990 | 176 | -86.7 | 504990 | 757 | -82.3 | 504990 | 271 | -83.3 | 504990 | 315 |
| MR_1774412975_F28CE678 | 504990 | 757 | -86.2 | 504990 | 176 | -80.9 | 504990 | 271 | -82.6 | 504990 | 315 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 304: `9bb9f929-f7f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9bb9f929-f7fe-4456-b7b6-ee1f35bccbef` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Add neighbor relationship between 3230356_4 and 3216347_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[304] topology](images/train_0304.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216347_3
- `C3`: Adjust the azimuth of 3230356_4 by 6 degrees
- `C4`: Check test server and transmission issues
- `C5`: Increase transmission power for 3230356_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230356_4
- `C7`: Increase A3 Offset threshold for 3230356_4
- `C8`: Increase A3 Offset threshold for 3216347_3
- `C9`: Lift the tilt angle  of 3216347_3 by 4 degrees
- `C10`: Add neighbor relationship between 3250244_2 and 3216347_3
- `C11`: Decrease transmission power for 3216347_3
- `C12`: Decrease A3 Offset threshold for 3216347_3
- `C13`: Decrease transmission power for 3230356_4
- `C14`: Adjust the azimuth of 3216347_3 by 6 degrees
- `C15`: Press down the tilt angle  of 3216347_3 by 4 degrees
- `C16`: Decrease A3 Offset threshold for 3230356_4
- `C17`: Lift the tilt angle of 3230356_4 by 10 degrees
- `C18`: Increase transmission power for 3216347_3
- `C19`: Add neighbor relationship between 3230356_4 and 3216347_3 **← 정답**
- `C20`: Press down the tilt angle of 3230356_4 by 10 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230356_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216347_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.249 | MS1 | 121.4656748967 | 31.1446254784 | 262 | 504990 | -81.51 | 13.40 | 542.62 | 0.04 | 2.92 | 1567 |
| 2024-09-20 22:21:32.308 | MS1 | 121.4656632199 | 31.1446306798 | 262 | 504990 | -79.49 | 16.29 | 497.17 | 0.08 | 2.62 | 1594 |
| 2024-09-20 22:21:33.655 | MS1 | 121.4656753249 | 31.1446372837 | 262 | 504990 | -83.66 | 17.74 | 455.94 | 0.10 | 2.28 | 1597 |
| 2024-09-20 22:21:34.322 | MS1 | 121.4656728132 | 31.1446254203 | 262 | 504990 | -88.82 | -1.55 | 64.26 | 0.19 | 1.19 | 1575 |
| 2024-09-20 22:21:35.931 | MS1 | 121.4656655623 | 31.1446320185 | 262 | 504990 | -88.62 | -2.52 | 27.89 | 0.14 | 1.09 | 1592 |
| 2024-09-20 22:21:36.694 | MS1 | 121.4656615272 | 31.1446368611 | 262 | 504990 | -93.33 | -1.00 | 58.32 | 0.12 | 1.22 | 1577 |
| 2024-09-20 22:21:37.129 | MS1 | 121.4656591371 | 31.1446231511 | 262 | 504990 | -85.74 | -3.28 | 44.04 | 0.13 | 1.27 | 1588 |
| 2024-09-20 22:21:38.837 | MS1 | 121.4656703001 | 31.1446223372 | 262 | 504990 | -83.26 | 14.29 | 345.32 | 0.01 | 1.36 | 1593 |
| 2024-09-20 22:21:39.189 | MS1 | 121.4656735778 | 31.1446253285 | 262 | 504990 | -84.58 | 15.01 | 324.54 | 0.20 | 1.48 | 1595 |
| 2024-09-20 22:21:40.651 | MS1 | 121.4656680485 | 31.1446245568 | 262 | 504990 | -77.12 | 14.78 | 577.13 | 0.11 | 2.10 | 1562 |
| 2024-09-20 22:21:41.815 | MS1 | 121.4656744655 | 31.1446362065 | 262 | 504990 | -78.10 | 14.50 | 353.40 | 0.15 | 2.92 | 1567 |
| 2024-09-20 22:21:42.317 | MS1 | 121.4656614763 | 31.1446196238 | 262 | 504990 | -76.60 | 16.93 | 471.25 | 0.05 | 2.49 | 1589 |

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
| 3216347 | 3 | 121.4676930087 | 31.1525441560 | 186 | 2 | 0 | 38.3 | TDD | 579 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3229658 | 1 | 121.4705059768 | 31.1540338393 | 275 | 7 | 1 | 18.0 | TDD | 457 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3230356 | 4 | 121.4660241862 | 31.1529557805 | 176 | 14 | 5 | 17.6 | TDD | 262 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3250244 | 2 | 121.4658478730 | 31.1473566219 | 109 | 13 | 5 | 23.3 | TDD | 730 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.489 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.510 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.623 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.623 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.364 | NREventA3 | measId:2;ServCellPCI:835;Se... |
| 2024-09-20 22:21:36.364 | NREventA3 | measId:2;ServCellPCI:835;Se... |
| 2024-09-20 22:21:37.364 | NREventA3 | measId:2;ServCellPCI:835;Se... |
| 2024-09-20 22:21:39.864 | NRRRCReestablishAttempt | PCI:835 |
| 2024-09-20 22:21:39.884 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.895 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:40.017 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.017 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229658 | 1 | 8.0886 | 12.3114 | -116.5488 | 16.6492 | 91.2914 | 0.0075 | 0.0034 |
| 2024_09_20 22:00 | 3250244 | 2 | 11.7535 | 10.6603 | -114.7270 | 12.9996 | 90.2170 | 0.0015 | 0.0100 |
| 2024_09_20 22:00 | 3216347 | 3 | 15.0984 | 12.9554 | -114.6245 | 7.7802 | 109.8982 | 0.0184 | 0.0107 |
| 2024_09_20 22:00 | 3230356 | 4 | 17.2749 | 19.5742 | -114.1588 | 14.7846 | 131.2567 | 0.0087 | 0.1047 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413507_E1040B26 | 504990 | 579 | -81.7 | 504990 | 262 | -88.0 | 504990 | 730 | -86.5 | 504990 | 457 |
| MR_1774413507_EFB776D9 | 504990 | 262 | -87.6 | 504990 | 579 | -81.9 | 504990 | 730 | -86.5 | 504990 | 457 |
| MR_1774413507_8C3FFEB4 | 504990 | 579 | -83.5 | 504990 | 262 | -87.2 | 504990 | 730 | -84.6 | 504990 | 457 |
| MR_1774413507_F8069C6F | 504990 | 262 | -87.7 | 504990 | 579 | -81.5 | 504990 | 730 | -83.1 | 504990 | 457 |
| MR_1774413507_A52E7FE2 | 504990 | 262 | -86.9 | 504990 | 579 | -83.8 | 504990 | 730 | -83.2 | 504990 | 457 |
| MR_1774413507_8768A627 | 504990 | 579 | -84.5 | 504990 | 262 | -89.6 | 504990 | 730 | -83.4 | 504990 | 457 |
| MR_1774413507_3D6DF9EC | 504990 | 579 | -84.0 | 504990 | 262 | -89.0 | 504990 | 730 | -85.6 | 504990 | 457 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 305: `0ceec2b3-965...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0ceec2b3-9652-46e7-ac91-d75ab0443c12` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Add neighbor relationship between 3237513_2 and 3243793_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[305] topology](images/train_0305.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243793_1
- `C2`: Decrease A3 Offset threshold for 3243793_1
- `C3`: Increase A3 Offset threshold for 3237513_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease transmission power for 3237513_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237513_2
- `C7`: Increase A3 Offset threshold for 3243793_1
- `C8`: Decrease A3 Offset threshold for 3237513_2
- `C9`: Adjust the azimuth of 3243793_1 by 12 degrees
- `C10`: Add neighbor relationship between 3237513_2 and 3243793_1 **← 정답**
- `C11`: Lift the tilt angle  of 3243793_1 by 2 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243793_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237513_2
- `C14`: Check test server and transmission issues
- `C15`: Decrease transmission power for 3243793_1
- `C16`: Increase transmission power for 3243793_1
- `C17`: Add neighbor relationship between 3255524_4 and 3243793_1
- `C18`: Increase transmission power for 3237513_2
- `C19`: Press down the tilt angle  of 3243793_1 by 2 degrees
- `C20`: Lift the tilt angle of 3237513_2 by 10 degrees
- `C21`: Adjust the azimuth of 3237513_2 by 50 degrees
- `C22`: Press down the tilt angle of 3237513_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.516 | MS1 | 121.4656742050 | 31.1446256661 | 201 | 504990 | -78.85 | 17.76 | 488.92 | 0.04 | 2.50 | 1576 |
| 2024-09-20 22:21:32.899 | MS1 | 121.4656683977 | 31.1446363525 | 201 | 504990 | -81.69 | 12.80 | 582.35 | 0.03 | 2.35 | 1571 |
| 2024-09-20 22:21:33.789 | MS1 | 121.4656768115 | 31.1446289787 | 201 | 504990 | -81.06 | 13.78 | 337.93 | 0.18 | 2.40 | 1575 |
| 2024-09-20 22:21:34.231 | MS1 | 121.4656756478 | 31.1446372147 | 201 | 504990 | -88.05 | -3.85 | 56.88 | 0.18 | 1.22 | 1587 |
| 2024-09-20 22:21:35.863 | MS1 | 121.4656675012 | 31.1446274161 | 201 | 504990 | -92.31 | -3.94 | 30.01 | 0.02 | 1.22 | 1571 |
| 2024-09-20 22:21:36.577 | MS1 | 121.4656630512 | 31.1446224373 | 201 | 504990 | -85.92 | -2.85 | 64.08 | 0.04 | 1.32 | 1583 |
| 2024-09-20 22:21:37.795 | MS1 | 121.4656718401 | 31.1446342567 | 201 | 504990 | -86.49 | -0.24 | 42.55 | 0.07 | 1.06 | 1566 |
| 2024-09-20 22:21:38.291 | MS1 | 121.4656708479 | 31.1446314830 | 201 | 504990 | -78.42 | 13.77 | 560.63 | 0.16 | 1.05 | 1574 |
| 2024-09-20 22:21:39.415 | MS1 | 121.4656629220 | 31.1446221850 | 201 | 504990 | -79.03 | 13.49 | 567.30 | 0.03 | 1.34 | 1576 |
| 2024-09-20 22:21:40.234 | MS1 | 121.4656705654 | 31.1446246821 | 201 | 504990 | -76.51 | 15.15 | 431.26 | 0.15 | 2.75 | 1597 |
| 2024-09-20 22:21:41.849 | MS1 | 121.4656617839 | 31.1446263474 | 201 | 504990 | -82.19 | 13.67 | 585.03 | 0.07 | 2.41 | 1585 |
| 2024-09-20 22:21:42.475 | MS1 | 121.4656628896 | 31.1446201278 | 201 | 504990 | -77.15 | 16.76 | 592.94 | 0.00 | 2.06 | 1580 |

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
| 3237513 | 2 | 121.4680719292 | 31.1469393860 | 129 | 10 | 9 | 41.4 | TDD | 201 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3243793 | 1 | 121.4752659562 | 31.1536871484 | 234 | 1 | 5 | 22.1 | TDD | 48 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3255524 | 4 | 121.4667002776 | 31.1530311401 | 21 | 7 | 6 | 34.2 | TDD | 575 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3275584 | 3 | 121.4696653836 | 31.1514574362 | 112 | 13 | 7 | 33.3 | TDD | 788 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.853 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.870 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.979 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.979 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.746 | NREventA3 | measId:2;ServCellPCI:624;Se... |
| 2024-09-20 22:21:35.746 | NREventA3 | measId:2;ServCellPCI:624;Se... |
| 2024-09-20 22:21:36.746 | NREventA3 | measId:2;ServCellPCI:624;Se... |
| 2024-09-20 22:21:39.246 | NRRRCReestablishAttempt | PCI:624 |
| 2024-09-20 22:21:39.259 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.274 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.408 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.408 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243793 | 1 | 19.0575 | 19.7223 | -117.0330 | 8.0674 | 94.3114 | 0.0003 | 0.0109 |
| 2024_09_20 22:00 | 3237513 | 2 | 14.4797 | 18.9405 | -115.9416 | 9.5094 | 159.8983 | 0.0007 | 0.1967 |
| 2024_09_20 22:00 | 3275584 | 3 | 18.7044 | 11.8854 | -115.4255 | 7.1520 | 153.2180 | 0.0081 | 0.0195 |
| 2024_09_20 22:00 | 3255524 | 4 | 7.1687 | 12.4103 | -114.5450 | 7.8517 | 111.3848 | 0.0102 | 0.0114 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414108_F7AED102 | 504990 | 48 | -83.9 | 504990 | 201 | -87.7 | 504990 | 575 | -85.3 | 504990 | 788 |
| MR_1774414108_0C45B4D5 | 504990 | 201 | -88.7 | 504990 | 48 | -81.4 | 504990 | 575 | -83.2 | 504990 | 788 |
| MR_1774414108_64D1A0C7 | 504990 | 201 | -87.0 | 504990 | 48 | -82.7 | 504990 | 575 | -83.8 | 504990 | 788 |
| MR_1774414108_7C02ADEC | 504990 | 201 | -86.7 | 504990 | 48 | -84.1 | 504990 | 575 | -85.3 | 504990 | 788 |
| MR_1774414108_9E611088 | 504990 | 201 | -87.9 | 504990 | 48 | -83.6 | 504990 | 575 | -83.6 | 504990 | 788 |
| MR_1774414108_2D0E21B7 | 504990 | 201 | -89.1 | 504990 | 48 | -82.0 | 504990 | 575 | -84.9 | 504990 | 788 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 306: `a64bf070-be9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a64bf070-be91-4904-9b39-f44d3bd9766a` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Add neighbor relationship between 3239829_1 and 3261819_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[306] topology](images/train_0306.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239829_1
- `C2`: Decrease transmission power for 3239829_1
- `C3`: Increase transmission power for 3261819_4
- `C4`: Lift the tilt angle  of 3261819_4 by 3 degrees
- `C5`: Increase transmission power for 3239829_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261819_4
- `C7`: Decrease A3 Offset threshold for 3239829_1
- `C8`: Increase A3 Offset threshold for 3239829_1
- `C9`: Press down the tilt angle of 3239829_1 by 10 degrees
- `C10`: Check test server and transmission issues
- `C11`: Add neighbor relationship between 3245316_2 and 3261819_4
- `C12`: Decrease A3 Offset threshold for 3261819_4
- `C13`: Add neighbor relationship between 3239829_1 and 3261819_4 **← 정답**
- `C14`: Adjust the azimuth of 3261819_4 by 18 degrees
- `C15`: Adjust the azimuth of 3239829_1 by 16 degrees
- `C16`: Lift the tilt angle of 3239829_1 by 10 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Press down the tilt angle  of 3261819_4 by 3 degrees
- `C19`: Increase A3 Offset threshold for 3261819_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239829_1
- `C21`: Decrease transmission power for 3261819_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261819_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.537 | MS1 | 121.4656681985 | 31.1446341697 | 293 | 504990 | -80.77 | 16.34 | 407.79 | 0.00 | 2.10 | 1576 |
| 2024-09-20 22:21:32.152 | MS1 | 121.4656704989 | 31.1446338491 | 293 | 504990 | -82.27 | 12.92 | 345.90 | 0.13 | 2.95 | 1583 |
| 2024-09-20 22:21:33.735 | MS1 | 121.4656691222 | 31.1446346788 | 293 | 504990 | -81.93 | 14.17 | 493.18 | 0.11 | 2.81 | 1594 |
| 2024-09-20 22:21:34.334 | MS1 | 121.4656615585 | 31.1446263970 | 293 | 504990 | -88.71 | -1.87 | 56.31 | 0.08 | 1.03 | 1579 |
| 2024-09-20 22:21:35.874 | MS1 | 121.4656593995 | 31.1446244416 | 293 | 504990 | -92.94 | -2.97 | 76.72 | 0.13 | 1.23 | 1572 |
| 2024-09-20 22:21:36.711 | MS1 | 121.4656633228 | 31.1446200988 | 293 | 504990 | -94.85 | -1.36 | 48.43 | 0.06 | 1.03 | 1583 |
| 2024-09-20 22:21:37.145 | MS1 | 121.4656607099 | 31.1446290431 | 293 | 504990 | -90.12 | -3.66 | 55.47 | 0.18 | 1.38 | 1580 |
| 2024-09-20 22:21:38.551 | MS1 | 121.4656645388 | 31.1446359121 | 293 | 504990 | -81.97 | 12.73 | 325.86 | 0.18 | 1.19 | 1596 |
| 2024-09-20 22:21:39.212 | MS1 | 121.4656766454 | 31.1446318134 | 293 | 504990 | -82.98 | 12.24 | 319.47 | 0.11 | 1.18 | 1600 |
| 2024-09-20 22:21:40.577 | MS1 | 121.4656587550 | 31.1446283023 | 293 | 504990 | -79.08 | 14.24 | 437.09 | 0.09 | 2.06 | 1600 |
| 2024-09-20 22:21:41.752 | MS1 | 121.4656733135 | 31.1446274202 | 293 | 504990 | -81.54 | 13.93 | 376.98 | 0.03 | 2.35 | 1565 |
| 2024-09-20 22:21:42.916 | MS1 | 121.4656616574 | 31.1446365152 | 293 | 504990 | -84.74 | 16.16 | 593.58 | 0.08 | 2.59 | 1582 |

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
| 3239829 | 1 | 121.4683577370 | 31.1484386141 | 195 | 10 | 0 | 21.4 | TDD | 293 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3245316 | 2 | 121.4717257360 | 31.1543840118 | 148 | 5 | 1 | 43.8 | TDD | 244 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3261819 | 4 | 121.4740259962 | 31.1471382434 | 269 | 1 | 2 | 34.2 | TDD | 479 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3262711 | 3 | 121.4738491482 | 31.1466931139 | 358 | 7 | 5 | 42.9 | TDD | 269 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.064 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.089 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.190 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.190 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.917 | NREventA3 | measId:2;ServCellPCI:896;Se... |
| 2024-09-20 22:21:35.917 | NREventA3 | measId:2;ServCellPCI:896;Se... |
| 2024-09-20 22:21:36.917 | NREventA3 | measId:2;ServCellPCI:896;Se... |
| 2024-09-20 22:21:39.417 | NRRRCReestablishAttempt | PCI:896 |
| 2024-09-20 22:21:39.435 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.448 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.587 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.587 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239829 | 1 | 9.3612 | 7.9226 | -116.0708 | 12.4901 | 123.5067 | 0.0032 | 0.1646 |
| 2024_09_20 22:00 | 3245316 | 2 | 12.8863 | 17.3763 | -116.3658 | 6.2180 | 171.3398 | 0.0035 | 0.0050 |
| 2024_09_20 22:00 | 3262711 | 3 | 7.4058 | 13.1647 | -116.7029 | 8.4550 | 146.4143 | 0.0007 | 0.0136 |
| 2024_09_20 22:00 | 3261819 | 4 | 14.5567 | 8.4499 | -115.6662 | 11.6621 | 149.1095 | 0.0079 | 0.0042 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415031_B5A9C41A | 504990 | 293 | -89.8 | 504990 | 479 | -84.5 | 504990 | 244 | -90.5 | 504990 | 269 |
| MR_1774415031_A959683F | 504990 | 293 | -90.4 | 504990 | 479 | -83.5 | 504990 | 244 | -90.8 | 504990 | 269 |
| MR_1774415031_B7A3260D | 504990 | 293 | -86.7 | 504990 | 479 | -84.0 | 504990 | 244 | -93.5 | 504990 | 269 |
| MR_1774415031_FEFEDC49 | 504990 | 293 | -86.8 | 504990 | 479 | -82.7 | 504990 | 244 | -93.7 | 504990 | 269 |
| MR_1774415031_917D3688 | 504990 | 479 | -84.4 | 504990 | 293 | -88.2 | 504990 | 244 | -92.1 | 504990 | 269 |
| MR_1774415031_94CD7657 | 504990 | 293 | -87.2 | 504990 | 479 | -82.6 | 504990 | 244 | -90.1 | 504990 | 269 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 307: `8b93f2b7-099...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8b93f2b7-099c-454a-8e30-7d9752363d4d` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[307] topology](images/train_0307.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3274112_2 by 6 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276790_3
- `C3`: Check test server and transmission issues **← 정답**
- `C4`: Decrease transmission power for 3274112_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276790_3
- `C6`: Adjust the azimuth of 3274112_2 by 50 degrees
- `C7`: Adjust the azimuth of 3276790_3 by 4 degrees
- `C8`: Decrease transmission power for 3276790_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274112_2
- `C10`: Decrease A3 Offset threshold for 3276790_3
- `C11`: Add neighbor relationship between 3274112_2 and 3276790_3
- `C12`: Increase transmission power for 3274112_2
- `C13`: Increase transmission power for 3276790_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274112_2
- `C15`: Increase A3 Offset threshold for 3274112_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease A3 Offset threshold for 3274112_2
- `C18`: Lift the tilt angle  of 3276790_3 by 10 degrees
- `C19`: Lift the tilt angle of 3274112_2 by 6 degrees
- `C20`: Press down the tilt angle  of 3276790_3 by 10 degrees
- `C21`: Increase A3 Offset threshold for 3276790_3
- `C22`: Add neighbor relationship between 3239434_4 and 3276790_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.752 | MS1 | 121.4656729639 | 31.1446257651 | 411 | 504990 | -88.81 | 16.71 | 511.72 | 0.09 | 2.63 | 1593 |
| 2024-09-20 22:21:32.716 | MS1 | 121.4656660207 | 31.1446239343 | 411 | 504990 | -86.36 | 15.42 | 532.94 | 0.14 | 2.73 | 1568 |
| 2024-09-20 22:21:33.570 | MS1 | 121.4656628207 | 31.1446354305 | 411 | 504990 | -87.05 | 14.58 | 323.94 | 0.00 | 2.86 | 1591 |
| 2024-09-20 22:21:34.250 | MS1 | 121.4656700343 | 31.1446291494 | 411 | 504990 | -91.17 | 14.36 | 51.65 | 0.00 | 2.24 | 352 |
| 2024-09-20 22:21:35.178 | MS1 | 121.4656650222 | 31.1446336000 | 411 | 504990 | -88.70 | 12.52 | 51.60 | 0.16 | 2.97 | 328 |
| 2024-09-20 22:21:36.616 | MS1 | 121.4656728718 | 31.1446248355 | 411 | 504990 | -86.37 | 12.99 | 66.92 | 0.02 | 2.10 | 454 |
| 2024-09-20 22:21:37.897 | MS1 | 121.4656716147 | 31.1446356497 | 411 | 504990 | -89.77 | 8.50 | 81.55 | 0.02 | 2.20 | 329 |
| 2024-09-20 22:21:38.137 | MS1 | 121.4656739643 | 31.1446314419 | 411 | 504990 | -89.03 | 7.41 | 104.76 | 0.07 | 2.69 | 440 |
| 2024-09-20 22:21:39.377 | MS1 | 121.4656616178 | 31.1446251863 | 411 | 504990 | -93.83 | 9.73 | 79.48 | 0.09 | 2.10 | 316 |
| 2024-09-20 22:21:40.881 | MS1 | 121.4656611090 | 31.1446321362 | 411 | 504990 | -93.02 | 8.89 | 493.86 | 0.13 | 2.99 | 1598 |
| 2024-09-20 22:21:41.924 | MS1 | 121.4656667419 | 31.1446187555 | 411 | 504990 | -89.93 | 11.05 | 356.32 | 0.02 | 2.47 | 1587 |
| 2024-09-20 22:21:42.823 | MS1 | 121.4656719441 | 31.1446352646 | 411 | 504990 | -90.87 | 7.16 | 338.05 | 0.02 | 2.30 | 1585 |

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
| 3239434 | 4 | 121.4739711123 | 31.1493342912 | 4 | 2 | 3 | 20.0 | TDD | 243 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3246378 | 1 | 121.4659982974 | 31.1495903005 | 195 | 4 | 0 | 15.0 | TDD | 161 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3274112 | 2 | 121.4651727924 | 31.1546908150 | 342 | 5 | 10 | 19.3 | TDD | 411 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3276790 | 3 | 121.4648072596 | 31.1451795729 | 123 | 6 | 12 | 21.3 | TDD | 481 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.247 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.271 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.373 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.373 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.091 | NREventA3 | measId:2;ServCellPCI:581;Se... |
| 2024-09-20 22:21:38.331 | NRHandoverAttempt | SourcePCI:581;SourceNR-ARFC... |
| 2024-09-20 22:21:38.377 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.391 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.531 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.531 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246378 | 1 | 10.0917 | 9.6632 | -114.3736 | 19.4209 | 110.6864 | 0.0060 | 0.0165 |
| 2024_09_20 22:00 | 3274112 | 2 | 5.3875 | 19.8385 | -114.6983 | 15.0601 | 132.6514 | 0.0139 | 0.0183 |
| 2024_09_20 22:00 | 3276790 | 3 | 19.9716 | 9.6853 | -117.1335 | 6.7414 | 112.8461 | 0.0057 | 0.0172 |
| 2024_09_20 22:00 | 3239434 | 4 | 5.0193 | 5.4142 | -117.1417 | 9.4027 | 187.8636 | 0.0057 | 0.0124 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416756_39C7189A | 504990 | 411 | -90.0 | 504990 | 481 | -99.7 | 504990 | 243 | -102.5 | 504990 | 161 |
| MR_1774416756_9519798F | 504990 | 411 | -90.3 | 504990 | 481 | -99.0 | 504990 | 243 | -100.3 | 504990 | 161 |
| MR_1774416756_15E9618D | 504990 | 411 | -91.9 | 504990 | 481 | -101.2 | 504990 | 243 | -100.5 | 504990 | 161 |
| MR_1774416756_0E93F3C7 | 504990 | 411 | -89.5 | 504990 | 481 | -101.3 | 504990 | 243 | -101.3 | 504990 | 161 |
| MR_1774416756_B0552E04 | 504990 | 411 | -92.0 | 504990 | 481 | -101.4 | 504990 | 243 | -99.2 | 504990 | 161 |
| MR_1774416756_EEB3927B | 504990 | 411 | -90.9 | 504990 | 481 | -99.1 | 504990 | 243 | -102.4 | 504990 | 161 |
| MR_1774416756_3D369D85 | 504990 | 411 | -91.7 | 504990 | 481 | -101.8 | 504990 | 243 | -102.5 | 504990 | 161 |
| MR_1774416756_F90A53E0 | 504990 | 411 | -92.4 | 504990 | 481 | -98.7 | 504990 | 243 | -99.6 | 504990 | 161 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 308: `5c53a9cc-111...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5c53a9cc-111a-4198-97a3-7a3537e64851` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[308] topology](images/train_0308.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3226882_4
- `C2`: Increase transmission power for 3226882_4
- `C3`: Adjust the azimuth of 3226882_4 by 50 degrees
- `C4`: Increase A3 Offset threshold for 3210466_2
- `C5`: Decrease A3 Offset threshold for 3226882_4
- `C6`: Adjust the azimuth of 3210466_2 by 50 degrees
- `C7`: Press down the tilt angle of 3226882_4 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226882_4
- `C9`: Decrease A3 Offset threshold for 3210466_2
- `C10`: Lift the tilt angle  of 3210466_2 by 10 degrees
- `C11`: Decrease transmission power for 3226882_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210466_2
- `C13`: Lift the tilt angle of 3226882_4 by 10 degrees
- `C14`: Insufficient data; more data is needed for judgment. **← 정답**
- `C15`: Check test server and transmission issues
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226882_4
- `C17`: Press down the tilt angle  of 3210466_2 by 10 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210466_2
- `C19`: Add neighbor relationship between 3268015_3 and 3210466_2
- `C20`: Increase transmission power for 3210466_2
- `C21`: Decrease transmission power for 3210466_2
- `C22`: Add neighbor relationship between 3226882_4 and 3210466_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.121 | MS1 | 121.4656767554 | 31.1446374932 | 455 | 504990 | -87.14 | 12.58 | 513.41 | 0.16 | 2.63 | 1580 |
| 2024-09-20 22:21:32.362 | MS1 | 121.4656674939 | 31.1446289823 | 455 | 504990 | -85.76 | 17.83 | 291.77 | 0.08 | 2.50 | 1585 |
| 2024-09-20 22:21:33.683 | MS1 | 121.4656633934 | 31.1446376438 | 455 | 504990 | -85.84 | 12.22 | 540.22 | 0.12 | 2.72 | 1579 |
| 2024-09-20 22:21:34.110 | MS1 | 121.4656713018 | 31.1446274398 | 455 | 504990 | -86.24 | 16.80 | 54.78 | 0.05 | 2.43 | 1578 |
| 2024-09-20 22:21:35.614 | MS1 | 121.4656657740 | 31.1446233114 | 455 | 504990 | -89.11 | 13.03 | 75.50 | 0.16 | 2.50 | 1589 |
| 2024-09-20 22:21:36.219 | MS1 | 121.4656680689 | 31.1446325227 | 455 | 504990 | -86.00 | 16.54 | 84.16 | 0.07 | 2.04 | 1560 |
| 2024-09-20 22:21:37.128 | MS1 | 121.4656723845 | 31.1446315128 | 455 | 504990 | -93.35 | 11.66 | 47.55 | 0.19 | 2.86 | 1600 |
| 2024-09-20 22:21:38.370 | MS1 | 121.4656743192 | 31.1446211414 | 455 | 504990 | -90.23 | 7.16 | 85.50 | 0.03 | 2.01 | 1565 |
| 2024-09-20 22:21:39.218 | MS1 | 121.4656603796 | 31.1446300443 | 455 | 504990 | -89.24 | 7.19 | 91.09 | 0.16 | 2.51 | 1583 |
| 2024-09-20 22:21:40.967 | MS1 | 121.4656767056 | 31.1446350957 | 455 | 504990 | -90.48 | 7.10 | 329.37 | 0.13 | 2.47 | 1577 |
| 2024-09-20 22:21:41.578 | MS1 | 121.4656749488 | 31.1446295622 | 455 | 504990 | -93.14 | 9.96 | 439.82 | 0.19 | 2.79 | 1581 |
| 2024-09-20 22:21:42.970 | MS1 | 121.4656641649 | 31.1446347998 | 455 | 504990 | -90.69 | 12.06 | 532.93 | 0.06 | 2.12 | 1561 |

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
| 3210466 | 2 | 121.4706416902 | 31.1457824440 | 174 | 9 | 3 | 30.3 | TDD | 893 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3226882 | 4 | 121.4641046829 | 31.1520817349 | 247 | 13 | 6 | 24.9 | TDD | 455 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3227723 | 1 | 121.4702027224 | 31.1519526233 | 91 | 7 | 4 | 19.0 | TDD | 530 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3268015 | 3 | 121.4655695125 | 31.1540318855 | 160 | 5 | 11 | 25.1 | TDD | 798 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.103 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.123 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.231 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.231 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.002 | NREventA3 | measId:2;ServCellPCI:82;Ser... |
| 2024-09-20 22:21:38.242 | NRHandoverAttempt | SourcePCI:82;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.287 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.298 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.406 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.406 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3227723 | 1 | 89.1773 | 81.0020 | -117.9433 | 8.3552 | 174.7468 | 0.0159 | 0.0197 |
| 2024_09_19 22:00 | 3210466 | 2 | 82.5512 | 79.7367 | -115.3435 | 7.9127 | 195.3418 | 0.0097 | 0.0026 |
| 2024_09_19 22:00 | 3268015 | 3 | 88.1038 | 93.2902 | -115.6893 | 17.9882 | 99.8582 | 0.0084 | 0.0049 |
| 2024_09_19 22:00 | 3226882 | 4 | 85.9519 | 87.9565 | -116.6655 | 17.1879 | 93.6867 | 0.0029 | 0.0033 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413747_2AC8C8D2 | 504990 | 455 | -84.4 | 504990 | 893 | -88.8 | 504990 | 798 | -97.7 | 504990 | 530 |
| MR_1774413747_8C2CEA87 | 504990 | 455 | -86.5 | 504990 | 893 | -86.2 | 504990 | 798 | -98.8 | 504990 | 530 |
| MR_1774413747_D82233EB | 504990 | 455 | -88.2 | 504990 | 893 | -88.8 | 504990 | 798 | -98.3 | 504990 | 530 |
| MR_1774413747_30069B1B | 504990 | 455 | -86.3 | 504990 | 893 | -86.9 | 504990 | 798 | -97.5 | 504990 | 530 |
| MR_1774413747_A3A62E16 | 504990 | 455 | -87.5 | 504990 | 893 | -88.2 | 504990 | 798 | -97.1 | 504990 | 530 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 309: `890d3724-170...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `890d3724-1701-457a-acc6-1458a7367f2d` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3275142_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[309] topology](images/train_0309.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266390_1
- `C2`: Decrease A3 Offset threshold for 3266390_1
- `C3`: Add neighbor relationship between 3225034_3 and 3266390_1
- `C4`: Increase transmission power for 3266390_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266390_1
- `C6`: Adjust the azimuth of 3275142_2 by 14 degrees
- `C7`: Lift the tilt angle of 3275142_2 by 1 degrees
- `C8`: Press down the tilt angle of 3275142_2 by 1 degrees
- `C9`: Increase A3 Offset threshold for 3266390_1
- `C10`: Decrease A3 Offset threshold for 3275142_2
- `C11`: Press down the tilt angle  of 3266390_1 by 9 degrees
- `C12`: Lift the tilt angle  of 3266390_1 by 9 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275142_2 **← 정답**
- `C14`: Add neighbor relationship between 3275142_2 and 3266390_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275142_2
- `C16`: Decrease transmission power for 3275142_2
- `C17`: Increase transmission power for 3275142_2
- `C18`: Check test server and transmission issues
- `C19`: Decrease transmission power for 3266390_1
- `C20`: Increase A3 Offset threshold for 3275142_2
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Adjust the azimuth of 3266390_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.862 | MS1 | 121.4656707985 | 31.1446262011 | 449 | 504990 | -85.60 | 13.15 | 332.99 | 0.12 | 2.66 | 1600 |
| 2024-09-20 22:21:32.500 | MS1 | 121.4656592685 | 31.1446210268 | 449 | 504990 | -91.42 | 17.61 | 565.00 | 0.11 | 2.89 | 1561 |
| 2024-09-20 22:21:33.743 | MS1 | 121.4656646177 | 31.1446290748 | 449 | 504990 | -91.54 | 13.79 | 548.42 | 0.12 | 2.45 | 1567 |
| 2024-09-20 22:21:34.124 | MS1 | 121.4656637791 | 31.1446253621 | 449 | 504990 | -90.67 | 16.54 | 92.72 | 0.58 | 2.99 | 631 |
| 2024-09-20 22:21:35.712 | MS1 | 121.4656675375 | 31.1446355270 | 449 | 504990 | -86.27 | 16.69 | 108.64 | 0.61 | 2.13 | 502 |
| 2024-09-20 22:21:36.910 | MS1 | 121.4656662045 | 31.1446372712 | 449 | 504990 | -88.21 | 14.85 | 77.69 | 0.55 | 2.93 | 519 |
| 2024-09-20 22:21:37.225 | MS1 | 121.4656588758 | 31.1446242807 | 449 | 504990 | -92.03 | 11.40 | 80.60 | 0.56 | 2.89 | 545 |
| 2024-09-20 22:21:38.864 | MS1 | 121.4656604616 | 31.1446195469 | 449 | 504990 | -92.90 | 11.48 | 61.29 | 0.62 | 2.36 | 537 |
| 2024-09-20 22:21:39.136 | MS1 | 121.4656580364 | 31.1446346614 | 449 | 504990 | -90.95 | 9.69 | 82.88 | 0.65 | 2.47 | 697 |
| 2024-09-20 22:21:40.215 | MS1 | 121.4656595375 | 31.1446241985 | 449 | 504990 | -91.16 | 7.65 | 527.75 | 0.15 | 2.18 | 1560 |
| 2024-09-20 22:21:41.498 | MS1 | 121.4656606985 | 31.1446230069 | 449 | 504990 | -92.01 | 10.21 | 393.88 | 0.01 | 2.46 | 1576 |
| 2024-09-20 22:21:42.344 | MS1 | 121.4656739883 | 31.1446366228 | 449 | 504990 | -89.45 | 10.60 | 458.01 | 0.17 | 2.72 | 1565 |

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
| 3225034 | 3 | 121.4703822521 | 31.1521372043 | 20 | 2 | 10 | 35.2 | TDD | 851 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3266390 | 1 | 121.4652463205 | 31.1523184182 | 88 | 7 | 11 | 25.9 | TDD | 520 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3272767 | 4 | 121.4756131053 | 31.1452572583 | 105 | 12 | 8 | 47.4 | TDD | 230 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3275142 | 2 | 121.4722076041 | 31.1475690327 | 228 | 0 | 7 | 17.6 | TDD | 449 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.087 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.106 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.208 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.208 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.986 | NREventA3 | measId:2;ServCellPCI:163;Se... |
| 2024-09-20 22:21:38.226 | NRHandoverAttempt | SourcePCI:163;SourceNR-ARFC... |
| 2024-09-20 22:21:38.258 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.271 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.399 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.399 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266390 | 1 | 17.5599 | 15.3247 | -115.5340 | 18.1719 | 102.5547 | 0.0145 | 0.0024 |
| 2024_09_20 22:00 | 3275142 | 2 | 15.9768 | 14.7920 | -117.2937 | 14.3450 | 110.3458 | 0.0066 | 0.0137 |
| 2024_09_20 22:00 | 3225034 | 3 | 8.8628 | 12.3394 | -116.9339 | 7.1819 | 106.3311 | 0.0102 | 0.0190 |
| 2024_09_20 22:00 | 3272767 | 4 | 5.1551 | 18.8717 | -114.7832 | 18.4413 | 95.8430 | 0.0156 | 0.0089 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414294_31255D9B | 504990 | 449 | -91.2 | 504990 | 520 | -94.7 | 504990 | 851 | -95.9 | 504990 | 230 |
| MR_1774414294_55E65D8A | 504990 | 449 | -92.1 | 504990 | 520 | -96.4 | 504990 | 851 | -97.4 | 504990 | 230 |
| MR_1774414294_2ADC4AC6 | 504990 | 449 | -90.4 | 504990 | 520 | -95.4 | 504990 | 851 | -94.8 | 504990 | 230 |
| MR_1774414294_F6B62352 | 504990 | 449 | -90.1 | 504990 | 520 | -94.3 | 504990 | 851 | -98.3 | 504990 | 230 |
| MR_1774414294_4696B65B | 504990 | 449 | -90.7 | 504990 | 520 | -94.6 | 504990 | 851 | -97.1 | 504990 | 230 |
| MR_1774414294_6898A1EF | 504990 | 449 | -91.6 | 504990 | 520 | -95.0 | 504990 | 851 | -97.2 | 504990 | 230 |
| MR_1774414294_F1075907 | 504990 | 449 | -89.6 | 504990 | 520 | -93.7 | 504990 | 851 | -96.6 | 504990 | 230 |
| MR_1774414294_EBE543DF | 504990 | 449 | -92.4 | 504990 | 520 | -96.2 | 504990 | 851 | -96.9 | 504990 | 230 |

> *... 2개 열 생략 (전체 14열)*

---
