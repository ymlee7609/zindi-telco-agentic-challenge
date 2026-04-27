# Track A 문제 분석 — train[1910]~train[1919]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1910] ~ train[1919] (10개)

## 목차

1. [문제 1910: `9159ca15-809...`](#1910) — single-answer, 정답: C18
2. [문제 1911: `0233a690-aa6...`](#1911) — single-answer, 정답: C22
3. [문제 1912: `a5645390-5f8...`](#1912) — single-answer, 정답: C7
4. [문제 1913: `dc153043-f07...`](#1913) — multiple-answer, 정답: C7|C11|C17|C20
5. [문제 1914: `a128771a-799...`](#1914) — single-answer, 정답: C6
6. [문제 1915: `b65167f5-367...`](#1915) — single-answer, 정답: C15
7. [문제 1916: `3af70b0a-922...`](#1916) — single-answer, 정답: C14
8. [문제 1917: `1c2bd16a-61d...`](#1917) — single-answer, 정답: C10
9. [문제 1918: `1f03cc47-a2a...`](#1918) — single-answer, 정답: C12
10. [문제 1919: `0d3a7d5b-0cd...`](#1919) — single-answer, 정답: C10

---

### 문제 1910: `9159ca15-809...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9159ca15-8094-4bba-92a1-2dbd2df5b397` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1910] topology](images/train_1910.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3211985_4 by 7 degrees
- `C2`: Lift the tilt angle  of 3236443_1 by 10 degrees
- `C3`: Add neighbor relationship between 3211985_4 and 3236443_1
- `C4`: Increase transmission power for 3236443_1
- `C5`: Increase transmission power for 3211985_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211985_4
- `C7`: Increase A3 Offset threshold for 3236443_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Add neighbor relationship between 3223891_2 and 3236443_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236443_1
- `C11`: Decrease transmission power for 3236443_1
- `C12`: Adjust the azimuth of 3236443_1 by 50 degrees
- `C13`: Adjust the azimuth of 3211985_4 by 50 degrees
- `C14`: Increase A3 Offset threshold for 3211985_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236443_1
- `C16`: Decrease A3 Offset threshold for 3211985_4
- `C17`: Decrease transmission power for 3211985_4
- `C18`: Check test server and transmission issues **← 정답**
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211985_4
- `C20`: Decrease A3 Offset threshold for 3236443_1
- `C21`: Lift the tilt angle of 3211985_4 by 7 degrees
- `C22`: Press down the tilt angle  of 3236443_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.222 | MS1 | 121.4656721742 | 31.1446329674 | 711 | 504990 | -90.94 | 13.62 | 380.28 | 0.17 | 2.12 | 1574 |
| 2024-09-20 22:21:32.861 | MS1 | 121.4656762738 | 31.1446305781 | 711 | 504990 | -91.81 | 13.01 | 376.79 | 0.08 | 2.47 | 1570 |
| 2024-09-20 22:21:33.708 | MS1 | 121.4656643146 | 31.1446268619 | 711 | 504990 | -88.48 | 14.32 | 484.17 | 0.18 | 2.82 | 1578 |
| 2024-09-20 22:21:34.274 | MS1 | 121.4656741024 | 31.1446274734 | 711 | 504990 | -88.83 | 13.11 | 83.59 | 0.18 | 2.52 | 477 |
| 2024-09-20 22:21:35.272 | MS1 | 121.4656673844 | 31.1446326177 | 711 | 504990 | -87.71 | 17.05 | 51.99 | 0.17 | 2.59 | 464 |
| 2024-09-20 22:21:36.310 | MS1 | 121.4656655642 | 31.1446243410 | 711 | 504990 | -87.79 | 14.09 | 85.29 | 0.12 | 2.46 | 383 |
| 2024-09-20 22:21:37.782 | MS1 | 121.4656599463 | 31.1446192210 | 711 | 504990 | -89.88 | 8.00 | 62.66 | 0.19 | 2.95 | 304 |
| 2024-09-20 22:21:38.493 | MS1 | 121.4656757189 | 31.1446346633 | 711 | 504990 | -90.14 | 10.66 | 107.26 | 0.05 | 2.16 | 372 |
| 2024-09-20 22:21:39.690 | MS1 | 121.4656697705 | 31.1446181362 | 711 | 504990 | -93.98 | 7.23 | 101.24 | 0.14 | 2.05 | 389 |
| 2024-09-20 22:21:40.338 | MS1 | 121.4656737087 | 31.1446193559 | 711 | 504990 | -92.08 | 11.27 | 313.70 | 0.04 | 2.38 | 1577 |
| 2024-09-20 22:21:41.404 | MS1 | 121.4656669356 | 31.1446233153 | 711 | 504990 | -91.61 | 7.95 | 548.38 | 0.18 | 2.81 | 1570 |
| 2024-09-20 22:21:42.829 | MS1 | 121.4656757370 | 31.1446329811 | 711 | 504990 | -92.08 | 7.46 | 408.10 | 0.10 | 2.94 | 1577 |

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
| 3211985 | 4 | 121.4721072988 | 31.1506564703 | 313 | 4 | 10 | 40.0 | TDD | 711 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3223891 | 2 | 121.4727165391 | 31.1448558218 | 342 | 3 | 2 | 24.4 | TDD | 140 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3236443 | 1 | 121.4682334309 | 31.1440187886 | 90 | 4 | 12 | 48.3 | TDD | 872 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3256250 | 3 | 121.4664362687 | 31.1498651746 | 44 | 15 | 6 | 44.4 | TDD | 205 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.323 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.339 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.449 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.449 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.189 | NREventA3 | measId:2;ServCellPCI:189;Se... |
| 2024-09-20 22:21:38.429 | NRHandoverAttempt | SourcePCI:189;SourceNR-ARFC... |
| 2024-09-20 22:21:38.462 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.477 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.584 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.584 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236443 | 1 | 10.5347 | 8.5080 | -116.0254 | 8.2765 | 136.9251 | 0.0178 | 0.0027 |
| 2024_09_20 22:00 | 3223891 | 2 | 13.3007 | 15.7739 | -116.4682 | 16.5835 | 136.1463 | 0.0188 | 0.0014 |
| 2024_09_20 22:00 | 3256250 | 3 | 18.7872 | 14.7370 | -115.9168 | 7.8178 | 191.4168 | 0.0168 | 0.0074 |
| 2024_09_20 22:00 | 3211985 | 4 | 10.8606 | 5.8859 | -114.9739 | 7.3547 | 147.3240 | 0.0033 | 0.0045 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415379_E8B037E1 | 504990 | 711 | -88.0 | 504990 | 872 | -96.3 | 504990 | 140 | -99.9 | 504990 | 205 |
| MR_1774415379_A4ECFF54 | 504990 | 711 | -87.5 | 504990 | 872 | -94.6 | 504990 | 140 | -97.2 | 504990 | 205 |
| MR_1774415379_666954E4 | 504990 | 711 | -88.8 | 504990 | 872 | -95.5 | 504990 | 140 | -100.4 | 504990 | 205 |
| MR_1774415379_6D1681AC | 504990 | 711 | -89.3 | 504990 | 872 | -94.7 | 504990 | 140 | -98.9 | 504990 | 205 |
| MR_1774415379_3BD52332 | 504990 | 711 | -87.0 | 504990 | 872 | -96.7 | 504990 | 140 | -98.5 | 504990 | 205 |
| MR_1774415379_302A9043 | 504990 | 711 | -89.3 | 504990 | 872 | -97.9 | 504990 | 140 | -98.1 | 504990 | 205 |
| MR_1774415379_F3CEF5B5 | 504990 | 711 | -90.5 | 504990 | 872 | -96.9 | 504990 | 140 | -98.4 | 504990 | 205 |
| MR_1774415379_3CA148B6 | 504990 | 711 | -89.5 | 504990 | 872 | -98.1 | 504990 | 140 | -99.4 | 504990 | 205 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1911: `0233a690-aa6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0233a690-aa6d-4241-96b1-ae00bc01f8b1` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1911] topology](images/train_1911.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase transmission power for 3246987_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244333_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246987_1
- `C5`: Press down the tilt angle  of 3244333_2 by 10 degrees
- `C6`: Press down the tilt angle of 3246987_1 by 5 degrees
- `C7`: Decrease transmission power for 3244333_2
- `C8`: Increase A3 Offset threshold for 3246987_1
- `C9`: Decrease A3 Offset threshold for 3246987_1
- `C10`: Adjust the azimuth of 3244333_2 by 50 degrees
- `C11`: Decrease transmission power for 3246987_1
- `C12`: Increase A3 Offset threshold for 3244333_2
- `C13`: Adjust the azimuth of 3246987_1 by 50 degrees
- `C14`: Add neighbor relationship between 3210332_3 and 3244333_2
- `C15`: Increase transmission power for 3244333_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246987_1
- `C17`: Lift the tilt angle  of 3244333_2 by 10 degrees
- `C18`: Decrease A3 Offset threshold for 3244333_2
- `C19`: Add neighbor relationship between 3246987_1 and 3244333_2
- `C20`: Lift the tilt angle of 3246987_1 by 5 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244333_2
- `C22`: Check test server and transmission issues **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.515 | MS1 | 121.4656643080 | 31.1446358652 | 330 | 504990 | -87.90 | 15.71 | 572.07 | 0.18 | 2.70 | 1589 |
| 2024-09-20 22:21:32.612 | MS1 | 121.4656600046 | 31.1446201860 | 330 | 504990 | -91.51 | 13.37 | 555.03 | 0.05 | 2.44 | 1577 |
| 2024-09-20 22:21:33.780 | MS1 | 121.4656709615 | 31.1446210216 | 330 | 504990 | -91.39 | 12.23 | 472.38 | 0.11 | 2.24 | 1582 |
| 2024-09-20 22:21:34.411 | MS1 | 121.4656597448 | 31.1446356045 | 330 | 504990 | -87.48 | 16.50 | 97.80 | 0.03 | 2.22 | 370 |
| 2024-09-20 22:21:35.532 | MS1 | 121.4656748749 | 31.1446203478 | 330 | 504990 | -88.65 | 17.33 | 60.77 | 0.12 | 2.91 | 443 |
| 2024-09-20 22:21:36.545 | MS1 | 121.4656654462 | 31.1446299466 | 330 | 504990 | -87.12 | 16.41 | 54.99 | 0.19 | 2.07 | 486 |
| 2024-09-20 22:21:37.923 | MS1 | 121.4656591598 | 31.1446304246 | 330 | 504990 | -92.87 | 9.12 | 68.07 | 0.05 | 2.83 | 401 |
| 2024-09-20 22:21:38.555 | MS1 | 121.4656723729 | 31.1446315545 | 330 | 504990 | -89.41 | 7.40 | 70.48 | 0.06 | 2.71 | 451 |
| 2024-09-20 22:21:39.366 | MS1 | 121.4656602902 | 31.1446274131 | 330 | 504990 | -92.81 | 9.82 | 83.90 | 0.03 | 2.39 | 339 |
| 2024-09-20 22:21:40.743 | MS1 | 121.4656589769 | 31.1446356433 | 330 | 504990 | -92.81 | 11.72 | 384.85 | 0.05 | 2.87 | 1560 |
| 2024-09-20 22:21:41.737 | MS1 | 121.4656721287 | 31.1446323215 | 330 | 504990 | -91.05 | 10.38 | 350.27 | 0.09 | 2.40 | 1576 |
| 2024-09-20 22:21:42.596 | MS1 | 121.4656691024 | 31.1446202560 | 330 | 504990 | -89.72 | 7.41 | 482.31 | 0.18 | 2.42 | 1580 |

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
| 3210332 | 3 | 121.4719718455 | 31.1458555740 | 262 | 9 | 5 | 43.9 | TDD | 901 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3236609 | 4 | 121.4643803684 | 31.1482481378 | 132 | 13 | 10 | 33.7 | TDD | 925 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3244333 | 2 | 121.4672042234 | 31.1521331824 | 107 | 13 | 10 | 47.2 | TDD | 836 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3246987 | 1 | 121.4702007495 | 31.1500688576 | 338 | 4 | 10 | 17.7 | TDD | 330 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.871 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.894 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.029 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.029 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.686 | NREventA3 | measId:2;ServCellPCI:450;Se... |
| 2024-09-20 22:21:37.926 | NRHandoverAttempt | SourcePCI:450;SourceNR-ARFC... |
| 2024-09-20 22:21:37.964 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.978 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.094 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.094 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246987 | 1 | 6.2616 | 13.4385 | -117.4025 | 12.7610 | 115.1008 | 0.0159 | 0.0161 |
| 2024_09_20 22:00 | 3244333 | 2 | 12.8584 | 5.7803 | -117.0099 | 14.2937 | 106.6912 | 0.0004 | 0.0089 |
| 2024_09_20 22:00 | 3210332 | 3 | 18.8423 | 5.8659 | -114.1410 | 19.0680 | 157.2457 | 0.0127 | 0.0044 |
| 2024_09_20 22:00 | 3236609 | 4 | 8.2251 | 8.6532 | -114.0315 | 8.9499 | 131.7900 | 0.0130 | 0.0154 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415717_4B2D650E | 504990 | 330 | -86.3 | 504990 | 836 | -95.6 | 504990 | 901 | -99.0 | 504990 | 925 |
| MR_1774415717_2C854B98 | 504990 | 330 | -88.3 | 504990 | 836 | -95.7 | 504990 | 901 | -101.4 | 504990 | 925 |
| MR_1774415717_29C2A427 | 504990 | 330 | -88.2 | 504990 | 836 | -93.2 | 504990 | 901 | -99.7 | 504990 | 925 |
| MR_1774415717_EB6AD9FB | 504990 | 330 | -88.1 | 504990 | 836 | -94.5 | 504990 | 901 | -99.6 | 504990 | 925 |
| MR_1774415717_97BAEB56 | 504990 | 330 | -88.2 | 504990 | 836 | -95.6 | 504990 | 901 | -99.7 | 504990 | 925 |
| MR_1774415717_8BD7C55E | 504990 | 330 | -87.9 | 504990 | 836 | -92.7 | 504990 | 901 | -98.9 | 504990 | 925 |
| MR_1774415717_1271E580 | 504990 | 330 | -88.1 | 504990 | 836 | -93.4 | 504990 | 901 | -97.7 | 504990 | 925 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1912: `a5645390-5f8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a5645390-5f8d-4dcd-86c1-add4a2a64c40` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Add neighbor relationship between 3273965_2 and 3229260_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1912] topology](images/train_1912.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229260_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273965_2
- `C3`: Increase transmission power for 3229260_3
- `C4`: Decrease A3 Offset threshold for 3273965_2
- `C5`: Increase transmission power for 3273965_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229260_3
- `C7`: Add neighbor relationship between 3273965_2 and 3229260_3 **← 정답**
- `C8`: Decrease transmission power for 3229260_3
- `C9`: Lift the tilt angle  of 3229260_3 by 4 degrees
- `C10`: Lift the tilt angle of 3273965_2 by 10 degrees
- `C11`: Increase A3 Offset threshold for 3229260_3
- `C12`: Increase A3 Offset threshold for 3273965_2
- `C13`: Decrease A3 Offset threshold for 3229260_3
- `C14`: Press down the tilt angle  of 3229260_3 by 4 degrees
- `C15`: Press down the tilt angle of 3273965_2 by 10 degrees
- `C16`: Check test server and transmission issues
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273965_2
- `C18`: Adjust the azimuth of 3273965_2 by 33 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease transmission power for 3273965_2
- `C21`: Add neighbor relationship between 3253188_1 and 3229260_3
- `C22`: Adjust the azimuth of 3229260_3 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.882 | MS1 | 121.4656653279 | 31.1446300063 | 3 | 504990 | -75.40 | 17.45 | 432.59 | 0.03 | 2.18 | 1585 |
| 2024-09-20 22:21:32.183 | MS1 | 121.4656605738 | 31.1446241480 | 3 | 504990 | -77.54 | 13.46 | 591.03 | 0.05 | 2.59 | 1592 |
| 2024-09-20 22:21:33.921 | MS1 | 121.4656689961 | 31.1446226606 | 3 | 504990 | -82.97 | 14.14 | 422.48 | 0.02 | 2.98 | 1573 |
| 2024-09-20 22:21:34.872 | MS1 | 121.4656615830 | 31.1446226737 | 3 | 504990 | -87.20 | -2.33 | 40.74 | 0.14 | 1.41 | 1560 |
| 2024-09-20 22:21:35.410 | MS1 | 121.4656664423 | 31.1446345900 | 3 | 504990 | -91.00 | -2.55 | 33.51 | 0.07 | 1.45 | 1560 |
| 2024-09-20 22:21:36.354 | MS1 | 121.4656604174 | 31.1446346342 | 3 | 504990 | -91.66 | -0.96 | 48.86 | 0.14 | 1.19 | 1574 |
| 2024-09-20 22:21:37.591 | MS1 | 121.4656776570 | 31.1446251167 | 3 | 504990 | -87.85 | -1.44 | 59.27 | 0.12 | 1.08 | 1586 |
| 2024-09-20 22:21:38.685 | MS1 | 121.4656683823 | 31.1446199604 | 3 | 504990 | -76.52 | 15.75 | 432.72 | 0.13 | 1.37 | 1595 |
| 2024-09-20 22:21:39.994 | MS1 | 121.4656604653 | 31.1446274841 | 3 | 504990 | -81.40 | 13.48 | 521.12 | 0.14 | 1.16 | 1591 |
| 2024-09-20 22:21:40.122 | MS1 | 121.4656599538 | 31.1446252744 | 3 | 504990 | -81.67 | 15.54 | 570.74 | 0.13 | 2.40 | 1579 |
| 2024-09-20 22:21:41.960 | MS1 | 121.4656591172 | 31.1446248866 | 3 | 504990 | -78.19 | 12.55 | 400.03 | 0.15 | 2.46 | 1560 |
| 2024-09-20 22:21:42.780 | MS1 | 121.4656606537 | 31.1446180185 | 3 | 504990 | -76.70 | 15.45 | 427.12 | 0.02 | 2.11 | 1564 |

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
| 3229260 | 3 | 121.4673166326 | 31.1490927672 | 200 | 2 | 8 | 17.3 | TDD | 677 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3253188 | 1 | 121.4653800167 | 31.1484249292 | 31 | 2 | 2 | 42.4 | TDD | 679 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3273965 | 2 | 121.4665390882 | 31.1440344474 | 276 | 1 | 3 | 39.7 | TDD | 3 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3279405 | 4 | 121.4685139665 | 31.1525920053 | 250 | 14 | 10 | 44.3 | TDD | 135 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.118 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.143 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.259 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.259 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.001 | NREventA3 | measId:2;ServCellPCI:282;Se... |
| 2024-09-20 22:21:36.001 | NREventA3 | measId:2;ServCellPCI:282;Se... |
| 2024-09-20 22:21:37.001 | NREventA3 | measId:2;ServCellPCI:282;Se... |
| 2024-09-20 22:21:39.501 | NRRRCReestablishAttempt | PCI:282 |
| 2024-09-20 22:21:39.514 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.528 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.660 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.660 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253188 | 1 | 16.6937 | 11.0928 | -116.3824 | 11.1038 | 87.4332 | 0.0044 | 0.0193 |
| 2024_09_20 22:00 | 3273965 | 2 | 5.0995 | 7.9317 | -116.4051 | 15.9561 | 119.3158 | 0.0178 | 0.1193 |
| 2024_09_20 22:00 | 3229260 | 3 | 6.9095 | 10.3495 | -115.4636 | 7.1892 | 106.6289 | 0.0161 | 0.0078 |
| 2024_09_20 22:00 | 3279405 | 4 | 6.2882 | 13.2502 | -115.6737 | 13.9607 | 165.3009 | 0.0059 | 0.0067 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412733_FC07DEC5 | 504990 | 677 | -81.8 | 504990 | 3 | -89.0 | 504990 | 679 | -89.4 | 504990 | 135 |
| MR_1774412733_E3AB70FD | 504990 | 677 | -81.7 | 504990 | 3 | -86.6 | 504990 | 679 | -88.9 | 504990 | 135 |
| MR_1774412733_8FA82516 | 504990 | 3 | -86.0 | 504990 | 677 | -82.2 | 504990 | 679 | -88.1 | 504990 | 135 |
| MR_1774412733_421E7FC7 | 504990 | 3 | -85.8 | 504990 | 677 | -82.9 | 504990 | 679 | -89.0 | 504990 | 135 |
| MR_1774412733_E56FCA4E | 504990 | 677 | -80.1 | 504990 | 3 | -85.3 | 504990 | 679 | -87.4 | 504990 | 135 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1913: `dc153043-f07...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dc153043-f07f-4f0d-addf-f87a6611be3d` |
| Tag | **multiple-answer** |
| 정답 | **C7|C11|C17|C20** |
| C7 의미 | Increase A3 Offset threshold for 3240111_3 |
| C11 의미 | Increase A3 Offset threshold for 3239645_1 |
| C17 의미 | Press down the tilt angle  of 3240111_3 by 2 degrees |
| C20 의미 | Decrease transmission power for 3240111_3 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1913] topology](images/train_1913.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3239645_1
- `C2`: Increase transmission power for 3240111_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240111_3
- `C4`: Decrease A3 Offset threshold for 3239645_1
- `C5`: Adjust the azimuth of 3239645_1 by 14 degrees
- `C6`: Lift the tilt angle  of 3240111_3 by 2 degrees
- `C7`: Increase A3 Offset threshold for 3240111_3 **← 정답**
- `C8`: Press down the tilt angle of 3239645_1 by 5 degrees
- `C9`: Decrease transmission power for 3239645_1
- `C10`: Decrease A3 Offset threshold for 3240111_3
- `C11`: Increase A3 Offset threshold for 3239645_1 **← 정답**
- `C12`: Add neighbor relationship between 3239645_1 and 3240111_3
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Adjust the azimuth of 3240111_3 by 28 degrees
- `C15`: Lift the tilt angle of 3239645_1 by 5 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239645_1
- `C17`: Press down the tilt angle  of 3240111_3 by 2 degrees **← 정답**
- `C18`: Check test server and transmission issues
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240111_3
- `C20`: Decrease transmission power for 3240111_3 **← 정답**
- `C21`: Add neighbor relationship between 3237346_4 and 3240111_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239645_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.225 | MS1 | 121.4656687980 | 31.1446324766 | 97 | 504990 | -78.35 | 16.37 | 567.51 | 0.19 | 2.27 | 1582 |
| 2024-09-20 22:21:32.619 | MS1 | 121.4656696494 | 31.1446351640 | 97 | 504990 | -81.99 | 15.09 | 516.31 | 0.00 | 2.29 | 1581 |
| 2024-09-20 22:21:33.326 | MS1 | 121.4656714343 | 31.1446239947 | 97 | 504990 | -75.53 | 17.71 | 444.47 | 0.17 | 2.15 | 1593 |
| 2024-09-20 22:21:34.875 | MS1 | 121.4656736032 | 31.1446288941 | 307 | 504990 | -89.20 | 1.56 | 63.83 | 0.20 | 1.33 | 1572 |
| 2024-09-20 22:21:35.797 | MS1 | 121.4656624852 | 31.1446225321 | 307 | 504990 | -89.82 | 1.19 | 51.12 | 0.03 | 1.10 | 1596 |
| 2024-09-20 22:21:36.623 | MS1 | 121.4656629667 | 31.1446376506 | 97 | 504990 | -84.10 | 2.38 | 54.95 | 0.13 | 1.21 | 1584 |
| 2024-09-20 22:21:37.226 | MS1 | 121.4656698996 | 31.1446323748 | 97 | 504990 | -83.51 | 3.67 | 70.12 | 0.10 | 1.22 | 1597 |
| 2024-09-20 22:21:38.760 | MS1 | 121.4656587190 | 31.1446322970 | 307 | 504990 | -88.00 | 4.75 | 61.31 | 0.14 | 1.36 | 1599 |
| 2024-09-20 22:21:39.869 | MS1 | 121.4656743405 | 31.1446258409 | 307 | 504990 | -89.33 | 4.31 | 81.09 | 0.12 | 1.20 | 1581 |
| 2024-09-20 22:21:40.319 | MS1 | 121.4656685531 | 31.1446330701 | 307 | 504990 | -82.20 | 12.44 | 574.22 | 0.19 | 2.69 | 1592 |
| 2024-09-20 22:21:41.680 | MS1 | 121.4656764267 | 31.1446193088 | 307 | 504990 | -80.98 | 13.07 | 451.87 | 0.05 | 2.15 | 1560 |
| 2024-09-20 22:21:42.763 | MS1 | 121.4656759483 | 31.1446213676 | 307 | 504990 | -80.23 | 16.29 | 546.10 | 0.20 | 2.58 | 1597 |

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
| 3236977 | 2 | 121.4661845986 | 31.1470831629 | 279 | 14 | 11 | 43.3 | TDD | 362 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3237346 | 4 | 121.4759378394 | 31.1556695362 | 29 | 13 | 7 | 38.8 | TDD | 206 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3239337 | 5 | 121.4645461393 | 31.1536614444 | 19 | 9 | 8 | 49.7 | TDD | 307 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3239645 | 1 | 121.4657061953 | 31.1490968895 | 166 | 1 | 4 | 33.0 | TDD | 97 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3240111 | 3 | 121.4706228785 | 31.1539885483 | 232 | 0 | 1 | 48.6 | TDD | 397 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.283 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.303 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.437 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.437 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.169 | NREventA3 | measId:2;ServCellPCI:657;Se... |
| 2024-09-20 22:21:34.409 | NRHandoverAttempt | SourcePCI:657;SourceNR-ARFC... |
| 2024-09-20 22:21:34.459 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.471 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:34.618 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.618 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.169 | NREventA3 | measId:2;ServCellPCI:721;Se... |
| 2024-09-20 22:21:36.409 | NRHandoverAttempt | SourcePCI:721;SourceNR-ARFC... |
| 2024-09-20 22:21:36.443 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.453 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:36.577 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.577 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.169 | NREventA3 | measId:2;ServCellPCI:657;Se... |
| 2024-09-20 22:21:38.409 | NRHandoverAttempt | SourcePCI:657;SourceNR-ARFC... |
| 2024-09-20 22:21:38.439 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.451 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.557 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.557 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239645 | 1 | 5.1707 | 18.7892 | -115.2741 | 19.8190 | 95.3025 | 0.0078 | 0.0181 |
| 2024_09_20 22:00 | 3236977 | 2 | 16.6019 | 19.2424 | -116.2136 | 6.2010 | 101.0090 | 0.0070 | 0.0137 |
| 2024_09_20 22:00 | 3240111 | 3 | 19.2060 | 16.3465 | -117.7584 | 15.1846 | 116.6084 | 0.0036 | 0.0067 |
| 2024_09_20 22:00 | 3237346 | 4 | 15.1826 | 11.5934 | -114.1859 | 13.5074 | 118.4568 | 0.0022 | 0.0141 |
| 2024_09_20 22:00 | 3239337 | 5 | 16.0161 | 16.7439 | -115.9300 | 8.4513 | 87.6422 | 0.0193 | 0.0070 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417015_C72B8559 | 504990 | 97 | -90.4 | 504990 | 307 | -88.6 | 504990 | 397 | -89.7 | 504990 | 206 |
| MR_1774417015_1707BC15 | 504990 | 97 | -90.8 | 504990 | 307 | -90.2 | 504990 | 397 | -89.7 | 504990 | 206 |
| MR_1774417015_08E04D52 | 504990 | 97 | -88.6 | 504990 | 307 | -90.1 | 504990 | 397 | -87.2 | 504990 | 206 |
| MR_1774417015_67AB7F74 | 504990 | 307 | -90.1 | 504990 | 97 | -86.8 | 504990 | 397 | -89.1 | 504990 | 206 |
| MR_1774417015_096D3490 | 504990 | 97 | -88.2 | 504990 | 307 | -87.1 | 504990 | 397 | -87.1 | 504990 | 206 |
| MR_1774417015_815DFA9E | 504990 | 97 | -88.3 | 504990 | 307 | -89.8 | 504990 | 397 | -88.3 | 504990 | 206 |
| MR_1774417015_C1A9DA6F | 504990 | 307 | -88.7 | 504990 | 97 | -86.7 | 504990 | 397 | -87.4 | 504990 | 206 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1914: `a128771a-799...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a128771a-799f-48f8-acd8-f38cb0f28b0a` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Add neighbor relationship between 3215993_3 and 3216115_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1914] topology](images/train_1914.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3215993_3
- `C2`: Press down the tilt angle  of 3216115_4 by 6 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215993_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215993_3
- `C5`: Increase transmission power for 3215993_3
- `C6`: Add neighbor relationship between 3215993_3 and 3216115_4 **← 정답**
- `C7`: Press down the tilt angle of 3215993_3 by 3 degrees
- `C8`: Adjust the azimuth of 3215993_3 by 50 degrees
- `C9`: Lift the tilt angle  of 3216115_4 by 6 degrees
- `C10`: Add neighbor relationship between 3241362_1 and 3216115_4
- `C11`: Decrease A3 Offset threshold for 3215993_3
- `C12`: Increase A3 Offset threshold for 3216115_4
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Increase A3 Offset threshold for 3215993_3
- `C15`: Increase transmission power for 3216115_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216115_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216115_4
- `C18`: Decrease A3 Offset threshold for 3216115_4
- `C19`: Lift the tilt angle of 3215993_3 by 3 degrees
- `C20`: Adjust the azimuth of 3216115_4 by 19 degrees
- `C21`: Check test server and transmission issues
- `C22`: Decrease transmission power for 3216115_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.470 | MS1 | 121.4656587575 | 31.1446249274 | 205 | 504990 | -79.82 | 12.22 | 493.32 | 0.19 | 3.00 | 1591 |
| 2024-09-20 22:21:32.165 | MS1 | 121.4656588907 | 31.1446217077 | 205 | 504990 | -83.34 | 15.36 | 533.15 | 0.11 | 2.09 | 1595 |
| 2024-09-20 22:21:33.231 | MS1 | 121.4656719892 | 31.1446252289 | 205 | 504990 | -84.15 | 12.36 | 320.09 | 0.15 | 2.28 | 1587 |
| 2024-09-20 22:21:34.494 | MS1 | 121.4656748149 | 31.1446215863 | 205 | 504990 | -94.55 | -3.76 | 58.18 | 0.10 | 1.19 | 1594 |
| 2024-09-20 22:21:35.118 | MS1 | 121.4656642821 | 31.1446347757 | 205 | 504990 | -88.66 | -1.22 | 60.21 | 0.15 | 1.32 | 1561 |
| 2024-09-20 22:21:36.245 | MS1 | 121.4656607494 | 31.1446372135 | 205 | 504990 | -88.03 | -2.70 | 57.73 | 0.13 | 1.10 | 1582 |
| 2024-09-20 22:21:37.815 | MS1 | 121.4656745798 | 31.1446296658 | 205 | 504990 | -87.23 | -2.20 | 39.83 | 0.09 | 1.36 | 1579 |
| 2024-09-20 22:21:38.873 | MS1 | 121.4656660655 | 31.1446338546 | 205 | 504990 | -77.08 | 12.47 | 437.56 | 0.14 | 1.35 | 1595 |
| 2024-09-20 22:21:39.396 | MS1 | 121.4656673248 | 31.1446316005 | 205 | 504990 | -83.15 | 14.39 | 325.64 | 0.04 | 1.06 | 1561 |
| 2024-09-20 22:21:40.831 | MS1 | 121.4656677452 | 31.1446347264 | 205 | 504990 | -78.21 | 17.25 | 418.38 | 0.03 | 2.51 | 1567 |
| 2024-09-20 22:21:41.726 | MS1 | 121.4656732783 | 31.1446346297 | 205 | 504990 | -81.79 | 13.51 | 401.90 | 0.01 | 2.04 | 1569 |
| 2024-09-20 22:21:42.226 | MS1 | 121.4656714167 | 31.1446189099 | 205 | 504990 | -75.01 | 12.09 | 585.96 | 0.02 | 2.34 | 1582 |

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
| 3215993 | 3 | 121.4717039806 | 31.1505472911 | 146 | 1 | 5 | 30.2 | TDD | 205 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3216115 | 4 | 121.4704444506 | 31.1460851511 | 231 | 4 | 2 | 15.4 | TDD | 447 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3241362 | 1 | 121.4757705103 | 31.1447671363 | 98 | 12 | 7 | 21.0 | TDD | 307 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3243673 | 2 | 121.4663765839 | 31.1517727611 | 178 | 14 | 11 | 48.0 | TDD | 155 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.216 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.348 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.348 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.053 | NREventA3 | measId:2;ServCellPCI:187;Se... |
| 2024-09-20 22:21:36.053 | NREventA3 | measId:2;ServCellPCI:187;Se... |
| 2024-09-20 22:21:37.053 | NREventA3 | measId:2;ServCellPCI:187;Se... |
| 2024-09-20 22:21:39.553 | NRRRCReestablishAttempt | PCI:187 |
| 2024-09-20 22:21:39.564 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.574 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.720 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.720 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241362 | 1 | 18.1922 | 11.0610 | -116.0379 | 13.7681 | 183.1238 | 0.0072 | 0.0034 |
| 2024_09_20 22:00 | 3243673 | 2 | 9.9310 | 8.9321 | -115.7207 | 8.9645 | 127.5724 | 0.0124 | 0.0153 |
| 2024_09_20 22:00 | 3215993 | 3 | 12.0288 | 18.5211 | -116.4361 | 9.3620 | 177.7689 | 0.0026 | 0.1627 |
| 2024_09_20 22:00 | 3216115 | 4 | 5.4310 | 16.1641 | -116.3772 | 18.1196 | 97.2089 | 0.0107 | 0.0104 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413535_915E4532 | 504990 | 205 | -93.3 | 504990 | 447 | -91.6 | 504990 | 307 | -93.4 | 504990 | 155 |
| MR_1774413535_385E499C | 504990 | 447 | -90.3 | 504990 | 205 | -94.1 | 504990 | 307 | -94.8 | 504990 | 155 |
| MR_1774413535_5C3528B7 | 504990 | 205 | -93.3 | 504990 | 447 | -90.9 | 504990 | 307 | -96.8 | 504990 | 155 |
| MR_1774413535_A341B75E | 504990 | 205 | -95.2 | 504990 | 447 | -90.5 | 504990 | 307 | -95.8 | 504990 | 155 |
| MR_1774413535_71482DB1 | 504990 | 447 | -88.2 | 504990 | 205 | -96.5 | 504990 | 307 | -95.6 | 504990 | 155 |
| MR_1774413535_74937CE9 | 504990 | 447 | -88.8 | 504990 | 205 | -92.9 | 504990 | 307 | -95.4 | 504990 | 155 |
| MR_1774413535_55FA519E | 504990 | 447 | -88.8 | 504990 | 205 | -96.0 | 504990 | 307 | -94.3 | 504990 | 155 |
| MR_1774413535_91D5768B | 504990 | 447 | -88.9 | 504990 | 205 | -96.2 | 504990 | 307 | -93.8 | 504990 | 155 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1915: `b65167f5-367...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b65167f5-3679-4353-a1ea-fafc4f6ab953` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214916_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1915] topology](images/train_1915.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214916_3
- `C3`: Increase transmission power for 3212586_5
- `C4`: Press down the tilt angle of 3214916_3 by 6 degrees
- `C5`: Add neighbor relationship between 3214916_3 and 3212586_5
- `C6`: Add neighbor relationship between 3221050_11 and 3212586_5
- `C7`: Adjust the azimuth of 3214916_3 by 48 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212586_5
- `C9`: Press down the tilt angle  of 3212586_5 by 5 degrees
- `C10`: Increase A3 Offset threshold for 3214916_3
- `C11`: Increase transmission power for 3214916_3
- `C12`: Adjust the azimuth of 3212586_5 by 33 degrees
- `C13`: Lift the tilt angle of 3214916_3 by 6 degrees
- `C14`: Decrease A3 Offset threshold for 3212586_5
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214916_3 **← 정답**
- `C16`: Lift the tilt angle  of 3212586_5 by 5 degrees
- `C17`: Decrease A3 Offset threshold for 3214916_3
- `C18`: Decrease transmission power for 3212586_5
- `C19`: Decrease transmission power for 3214916_3
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase A3 Offset threshold for 3212586_5
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212586_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.483 | MS1 | 121.4656618144 | 31.1446339551 | 269 | 504990 | -95.57 | 11.25 | 339.14 | 0.15 | 2.18 | 1588 |
| 2024-09-20 22:21:32.128 | MS1 | 121.4656645034 | 31.1446224558 | 328 | 504990 | -93.85 | 12.90 | 472.96 | 0.09 | 2.32 | 1574 |
| 2024-09-20 22:21:33.629 | MS1 | 121.4656766555 | 31.1446186592 | 151 | 504990 | -95.55 | 10.43 | 326.83 | 0.03 | 2.94 | 1564 |
| 2024-09-20 22:21:34.563 | MS1 | 121.4656683061 | 31.1446350642 | 867 | 152650 | -88.06 | 7.80 | 54.04 | 0.14 | 1.67 | 978 |
| 2024-09-20 22:21:35.387 | MS1 | 121.4656645634 | 31.1446218369 | 813 | 152650 | -88.77 | 2.75 | 61.02 | 0.04 | 1.83 | 904 |
| 2024-09-20 22:21:36.372 | MS1 | 121.4656634859 | 31.1446242313 | 470 | 152650 | -95.47 | 3.92 | 57.35 | 0.05 | 1.82 | 960 |
| 2024-09-20 22:21:37.101 | MS1 | 121.4656760114 | 31.1446344910 | 894 | 152650 | -88.03 | 2.57 | 82.93 | 0.19 | 1.84 | 986 |
| 2024-09-20 22:21:38.664 | MS1 | 121.4656694229 | 31.1446209849 | 867 | 152650 | -92.56 | 6.27 | 52.08 | 0.14 | 1.57 | 949 |
| 2024-09-20 22:21:39.556 | MS1 | 121.4656729098 | 31.1446341008 | 813 | 152650 | -89.27 | 6.81 | 84.13 | 0.04 | 1.57 | 962 |
| 2024-09-20 22:21:40.559 | MS1 | 121.4656714450 | 31.1446256023 | 470 | 152650 | -94.20 | 6.26 | 67.04 | 0.05 | 2.99 | 1572 |
| 2024-09-20 22:21:41.247 | MS1 | 121.4656684202 | 31.1446222858 | 894 | 152650 | -92.65 | 3.76 | 81.74 | 0.01 | 2.67 | 1582 |
| 2024-09-20 22:21:42.641 | MS1 | 121.4656774613 | 31.1446297691 | 867 | 152650 | -95.56 | 6.21 | 88.84 | 0.03 | 2.65 | 1592 |

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
| 3211389 | 4 | 121.4673949498 | 31.1488631094 | 62 | 1 | 3 | 21.4 | TDD | 15 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3212586 | 5 | 121.4700979527 | 31.1519791586 | 240 | 5 | 5 | 0.2 | TDD | 565 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3213466 | 1 | 121.4702506993 | 31.1492946514 | 140 | 3 | 12 | 23.2 | TDD | 328 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3214916 | 3 | 121.4692519216 | 31.1517890199 | 251 | 4 | 2 | 24.3 | TDD | 269 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3215731 | 2 | 121.4685788466 | 31.1514875228 | 158 | 14 | 7 | 21.6 | TDD | 523 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3221050 | 11 | 121.4710211153 | 31.1470220006 | 266 | 5 | 7 | 24.4 | FDD | 470 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3226340 | 10 | 121.4715044369 | 31.1445288571 | 296 | 12 | 3 | 6.1 | FDD | 979 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3247172 | 6 | 121.4735104122 | 31.1529550086 | 169 | 2 | 8 | 5.0 | TDD | 151 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3248047 | 8 | 121.4649209841 | 31.1486727926 | 30 | 12 | 12 | 19.1 | FDD | 811 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3251586 | 9 | 121.4757029010 | 31.1507889501 | 220 | 2 | 9 | 5.3 | FDD | 813 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3262746 | 13 | 121.4662241568 | 31.1521026994 | 143 | 2 | 2 | 9.6 | FDD | 894 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3274460 | 12 | 121.4742218211 | 31.1466751198 | 316 | 2 | 2 | 9.3 | FDD | 215 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3277891 | 7 | 121.4721557294 | 31.1485146760 | 304 | 0 | 0 | 30.0 | FDD | 867 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |

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
| 2024-09-20 22:21:31.639 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.739 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.739 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.468 | NREventA2 | measId:1;ServCellPCI:582;Se... |
| 2024-09-20 22:21:35.593 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.852 | NREventA5 | measId:3;ServCellPCI:582;Se... |
| 2024-09-20 22:21:35.925 | NRHandoverAttempt | SourcePCI:582;SourceNR-ARFC... |
| 2024-09-20 22:21:35.954 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.967 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.102 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.102 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213466 | 1 | 7.8560 | 10.4746 | -114.5092 | 13.1436 | 191.7048 | 0.0031 | 0.0095 |
| 2024_09_20 22:00 | 3215731 | 2 | 5.4448 | 7.4343 | -116.8402 | 7.1873 | 197.1052 | 0.0025 | 0.0097 |
| 2024_09_20 22:00 | 3214916 | 3 | 5.3682 | 5.7482 | -117.0992 | 12.1175 | 127.6789 | 0.0200 | 0.0046 |
| 2024_09_20 22:00 | 3211389 | 4 | 17.0537 | 6.9756 | -114.9205 | 6.3363 | 161.5265 | 0.0134 | 0.0079 |
| 2024_09_20 22:00 | 3212586 | 5 | 13.4681 | 13.5140 | -114.8875 | 7.7169 | 162.5919 | 0.0022 | 0.0043 |
| 2024_09_20 22:00 | 3247172 | 6 | 18.7933 | 16.3587 | -115.0630 | 7.6275 | 177.3416 | 0.0062 | 0.0010 |
| 2024_09_20 22:00 | 3277891 | 7 | 17.3129 | 13.9236 | -114.9224 | 4.4359 | 46.5344 | 0.0163 | 0.0110 |
| 2024_09_20 22:00 | 3248047 | 8 | 17.2285 | 12.7140 | -117.6708 | 3.9389 | 50.0621 | 0.0076 | 0.0015 |
| 2024_09_20 22:00 | 3251586 | 9 | 10.3463 | 16.9410 | -116.1229 | 4.0241 | 33.2735 | 0.0149 | 0.0066 |
| 2024_09_20 22:00 | 3226340 | 10 | 9.3934 | 10.3304 | -115.0544 | 4.1667 | 59.5431 | 0.0057 | 0.0185 |
| 2024_09_20 22:00 | 3221050 | 11 | 18.3921 | 5.1474 | -117.9361 | 4.1119 | 36.4963 | 0.0033 | 0.0016 |
| 2024_09_20 22:00 | 3274460 | 12 | 19.8910 | 17.6042 | -114.7648 | 3.7601 | 41.3405 | 0.0048 | 0.0036 |
| 2024_09_20 22:00 | 3262746 | 13 | 10.1565 | 8.8689 | -114.0822 | 3.2569 | 25.7077 | 0.0000 | 0.0079 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416203_EAA4A090 | 504990 | 151 | -94.5 | 504990 | 565 | -92.5 | 504990 | 15 | -101.6 | 504990 | 523 |
| MR_1774416203_A6A9192D | 504990 | 151 | -93.9 | 504990 | 565 | -90.2 | 504990 | 15 | -102.3 | 504990 | 523 |
| MR_1774416203_6DE26743 | 504990 | 151 | -95.0 | 504990 | 565 | -91.7 | 504990 | 15 | -102.9 | 504990 | 523 |
| MR_1774416203_3A3E0A21 | 152650 | 867 | -87.5 | 152650 | 811 | -92.9 | 152650 | 979 | -96.9 | 152650 | 215 |
| MR_1774416203_AA8AAB31 | 504990 | 151 | -95.5 | 504990 | 565 | -93.1 | 504990 | 15 | -102.8 | 504990 | 523 |
| MR_1774416203_754045CD | 152650 | 867 | -87.8 | 152650 | 811 | -93.7 | 152650 | 979 | -96.4 | 152650 | 215 |
| MR_1774416203_39D5F361 | 152650 | 867 | -87.8 | 152650 | 811 | -94.6 | 152650 | 979 | -99.1 | 152650 | 215 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1916: `3af70b0a-922...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3af70b0a-922a-4073-92a9-42ab2468390f` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3243558_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1916] topology](images/train_1916.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3263321_1
- `C2`: Add neighbor relationship between 3255533_2 and 3263321_1
- `C3`: Adjust the azimuth of 3263321_1 by 50 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Increase A3 Offset threshold for 3263321_1
- `C6`: Lift the tilt angle  of 3263321_1 by 10 degrees
- `C7`: Increase A3 Offset threshold for 3243558_4
- `C8`: Increase transmission power for 3263321_1
- `C9`: Decrease A3 Offset threshold for 3243558_4
- `C10`: Decrease transmission power for 3243558_4
- `C11`: Decrease A3 Offset threshold for 3263321_1
- `C12`: Increase transmission power for 3243558_4
- `C13`: Press down the tilt angle of 3243558_4 by 3 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243558_4 **← 정답**
- `C15`: Adjust the azimuth of 3243558_4 by 49 degrees
- `C16`: Add neighbor relationship between 3243558_4 and 3263321_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263321_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263321_1
- `C19`: Check test server and transmission issues
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243558_4
- `C21`: Lift the tilt angle of 3243558_4 by 3 degrees
- `C22`: Press down the tilt angle  of 3263321_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.478 | MS1 | 121.4656671910 | 31.1446297102 | 447 | 504990 | -91.47 | 14.32 | 512.72 | 0.05 | 2.85 | 1598 |
| 2024-09-20 22:21:32.909 | MS1 | 121.4656662418 | 31.1446290109 | 447 | 504990 | -91.27 | 17.37 | 374.26 | 0.13 | 2.38 | 1572 |
| 2024-09-20 22:21:33.300 | MS1 | 121.4656651554 | 31.1446202313 | 447 | 504990 | -91.71 | 15.42 | 351.19 | 0.11 | 2.81 | 1562 |
| 2024-09-20 22:21:34.843 | MS1 | 121.4656622405 | 31.1446343149 | 447 | 504990 | -88.86 | 12.28 | 95.97 | 0.52 | 2.56 | 556 |
| 2024-09-20 22:21:35.685 | MS1 | 121.4656739025 | 31.1446198208 | 447 | 504990 | -89.96 | 12.86 | 85.03 | 0.54 | 2.47 | 541 |
| 2024-09-20 22:21:36.315 | MS1 | 121.4656653182 | 31.1446319039 | 447 | 504990 | -86.86 | 12.14 | 73.17 | 0.59 | 2.97 | 602 |
| 2024-09-20 22:21:37.487 | MS1 | 121.4656683538 | 31.1446183310 | 447 | 504990 | -92.40 | 12.75 | 100.31 | 0.64 | 2.89 | 501 |
| 2024-09-20 22:21:38.128 | MS1 | 121.4656749565 | 31.1446283780 | 447 | 504990 | -90.59 | 10.29 | 81.48 | 0.68 | 2.80 | 639 |
| 2024-09-20 22:21:39.675 | MS1 | 121.4656754191 | 31.1446283218 | 447 | 504990 | -92.82 | 9.76 | 52.29 | 0.68 | 2.26 | 502 |
| 2024-09-20 22:21:40.305 | MS1 | 121.4656666075 | 31.1446338314 | 447 | 504990 | -93.09 | 10.78 | 591.80 | 0.12 | 2.73 | 1560 |
| 2024-09-20 22:21:41.516 | MS1 | 121.4656584776 | 31.1446244216 | 447 | 504990 | -93.40 | 7.93 | 449.80 | 0.19 | 2.41 | 1578 |
| 2024-09-20 22:21:42.225 | MS1 | 121.4656654814 | 31.1446345435 | 447 | 504990 | -90.50 | 9.90 | 402.45 | 0.09 | 2.92 | 1597 |

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
| 3240905 | 3 | 121.4663220474 | 31.1531456165 | 353 | 3 | 3 | 38.3 | TDD | 405 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3243558 | 4 | 121.4753702591 | 31.1510405035 | 183 | 1 | 3 | 40.8 | TDD | 447 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3255533 | 2 | 121.4723061928 | 31.1531810479 | 154 | 15 | 5 | 46.5 | TDD | 213 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3263321 | 1 | 121.4653646207 | 31.1452747110 | 9 | 10 | 2 | 46.9 | TDD | 772 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.056 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.076 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.189 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.189 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.864 | NREventA3 | measId:2;ServCellPCI:931;Se... |
| 2024-09-20 22:21:38.104 | NRHandoverAttempt | SourcePCI:931;SourceNR-ARFC... |
| 2024-09-20 22:21:38.136 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.149 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.281 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.281 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263321 | 1 | 17.6203 | 13.2698 | -117.1507 | 15.1752 | 88.3778 | 0.0121 | 0.0113 |
| 2024_09_20 22:00 | 3255533 | 2 | 9.0422 | 16.3802 | -116.9559 | 17.8875 | 187.9027 | 0.0005 | 0.0002 |
| 2024_09_20 22:00 | 3240905 | 3 | 17.0762 | 13.7328 | -116.2014 | 12.7596 | 87.2235 | 0.0137 | 0.0089 |
| 2024_09_20 22:00 | 3243558 | 4 | 14.3871 | 9.2172 | -117.7439 | 18.6503 | 178.0280 | 0.0020 | 0.0073 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413323_7B36A861 | 504990 | 447 | -89.7 | 504990 | 772 | -98.3 | 504990 | 213 | -99.1 | 504990 | 405 |
| MR_1774413323_EB7398FD | 504990 | 447 | -90.2 | 504990 | 772 | -97.8 | 504990 | 213 | -97.1 | 504990 | 405 |
| MR_1774413323_38DDCFFB | 504990 | 447 | -90.5 | 504990 | 772 | -99.9 | 504990 | 213 | -97.5 | 504990 | 405 |
| MR_1774413323_90AFA30D | 504990 | 447 | -87.4 | 504990 | 772 | -100.0 | 504990 | 213 | -98.8 | 504990 | 405 |
| MR_1774413323_54C544E7 | 504990 | 447 | -90.4 | 504990 | 772 | -99.8 | 504990 | 213 | -99.6 | 504990 | 405 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1917: `1c2bd16a-61d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1c2bd16a-61d7-4f0c-8e6b-976a303c09a7` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275894_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1917] topology](images/train_1917.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3240263_5
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240263_5
- `C3`: Lift the tilt angle of 3275894_4 by 1 degrees
- `C4`: Check test server and transmission issues
- `C5`: Decrease A3 Offset threshold for 3275894_4
- `C6`: Press down the tilt angle of 3275894_4 by 1 degrees
- `C7`: Increase A3 Offset threshold for 3240263_5
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240263_5
- `C9`: Increase transmission power for 3240263_5
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275894_4 **← 정답**
- `C11`: Add neighbor relationship between 3275894_4 and 3240263_5
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275894_4
- `C13`: Press down the tilt angle  of 3240263_5 by 6 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Lift the tilt angle  of 3240263_5 by 6 degrees
- `C16`: Adjust the azimuth of 3275894_4 by 30 degrees
- `C17`: Increase A3 Offset threshold for 3275894_4
- `C18`: Increase transmission power for 3275894_4
- `C19`: Adjust the azimuth of 3240263_5 by 20 degrees
- `C20`: Decrease A3 Offset threshold for 3240263_5
- `C21`: Add neighbor relationship between 3217962_11 and 3240263_5
- `C22`: Decrease transmission power for 3275894_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.822 | MS1 | 121.4656774448 | 31.1446297275 | 307 | 504990 | -94.16 | 12.75 | 439.26 | 0.01 | 2.14 | 1600 |
| 2024-09-20 22:21:32.562 | MS1 | 121.4656613721 | 31.1446354025 | 92 | 504990 | -94.44 | 13.42 | 512.07 | 0.19 | 2.52 | 1566 |
| 2024-09-20 22:21:33.362 | MS1 | 121.4656730724 | 31.1446224796 | 394 | 504990 | -95.48 | 11.05 | 501.43 | 0.18 | 2.78 | 1599 |
| 2024-09-20 22:21:34.592 | MS1 | 121.4656713762 | 31.1446306489 | 974 | 152650 | -95.84 | 3.84 | 60.17 | 0.10 | 1.53 | 982 |
| 2024-09-20 22:21:35.593 | MS1 | 121.4656709550 | 31.1446288206 | 853 | 152650 | -87.26 | 6.25 | 58.65 | 0.13 | 1.68 | 970 |
| 2024-09-20 22:21:36.431 | MS1 | 121.4656778035 | 31.1446374528 | 592 | 152650 | -93.56 | 5.83 | 75.90 | 0.08 | 1.79 | 991 |
| 2024-09-20 22:21:37.936 | MS1 | 121.4656777619 | 31.1446344430 | 235 | 152650 | -95.45 | 3.24 | 78.75 | 0.15 | 1.62 | 979 |
| 2024-09-20 22:21:38.630 | MS1 | 121.4656684882 | 31.1446373388 | 974 | 152650 | -95.11 | 7.87 | 56.96 | 0.06 | 1.53 | 969 |
| 2024-09-20 22:21:39.838 | MS1 | 121.4656735970 | 31.1446375203 | 853 | 152650 | -93.56 | 5.32 | 103.74 | 0.02 | 1.89 | 953 |
| 2024-09-20 22:21:40.852 | MS1 | 121.4656608422 | 31.1446352932 | 592 | 152650 | -91.65 | 3.15 | 83.08 | 0.19 | 2.96 | 1583 |
| 2024-09-20 22:21:41.645 | MS1 | 121.4656778963 | 31.1446187198 | 235 | 152650 | -95.51 | 3.66 | 58.97 | 0.05 | 2.37 | 1574 |
| 2024-09-20 22:21:42.605 | MS1 | 121.4656689170 | 31.1446276062 | 974 | 152650 | -90.79 | 6.03 | 82.60 | 0.11 | 2.30 | 1561 |

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
| 3211562 | 6 | 121.4663609515 | 31.1502996985 | 313 | 10 | 0 | 15.6 | TDD | 92 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3212361 | 8 | 121.4691835966 | 31.1539935533 | 294 | 13 | 6 | 2.1 | FDD | 552 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3217962 | 11 | 121.4753788189 | 31.1478945712 | 263 | 5 | 3 | 24.5 | FDD | 592 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3226950 | 10 | 121.4640012185 | 31.1486842155 | 55 | 4 | 5 | 26.6 | FDD | 974 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3230791 | 1 | 121.4658604831 | 31.1455538623 | 59 | 11 | 11 | 29.4 | TDD | 394 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3235098 | 3 | 121.4742036160 | 31.1502269081 | 61 | 6 | 11 | 4.9 | TDD | 49 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3240263 | 5 | 121.4681872620 | 31.1493273493 | 185 | 4 | 11 | 17.5 | TDD | 281 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3250308 | 2 | 121.4721604763 | 31.1450829802 | 292 | 9 | 12 | 7.6 | TDD | 587 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3261010 | 13 | 121.4672911667 | 31.1491014645 | 126 | 1 | 2 | 2.0 | FDD | 793 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3262399 | 12 | 121.4654892114 | 31.1488653444 | 348 | 4 | 2 | 13.9 | FDD | 853 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3265624 | 7 | 121.4669100568 | 31.1476229263 | 109 | 8 | 11 | 18.7 | FDD | 808 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3266350 | 9 | 121.4664420277 | 31.1507745216 | 14 | 10 | 9 | 9.6 | FDD | 235 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3275894 | 4 | 121.4710687559 | 31.1554401553 | 233 | 0 | 9 | 15.6 | TDD | 307 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.576 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.597 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.697 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.697 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.376 | NREventA2 | measId:1;ServCellPCI:318;Se... |
| 2024-09-20 22:21:35.506 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.784 | NREventA5 | measId:3;ServCellPCI:318;Se... |
| 2024-09-20 22:21:35.858 | NRHandoverAttempt | SourcePCI:318;SourceNR-ARFC... |
| 2024-09-20 22:21:35.894 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.907 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.048 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.048 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230791 | 1 | 11.8547 | 13.5448 | -117.8153 | 8.7126 | 85.9998 | 0.0013 | 0.0183 |
| 2024_09_20 22:00 | 3250308 | 2 | 7.7035 | 7.6126 | -114.5087 | 13.5858 | 81.0524 | 0.0020 | 0.0054 |
| 2024_09_20 22:00 | 3235098 | 3 | 17.5381 | 17.8970 | -117.8752 | 11.3939 | 199.2823 | 0.0105 | 0.0119 |
| 2024_09_20 22:00 | 3275894 | 4 | 16.4213 | 18.3659 | -117.5918 | 14.9035 | 159.3000 | 0.0128 | 0.0178 |
| 2024_09_20 22:00 | 3240263 | 5 | 5.5652 | 10.8455 | -116.2677 | 11.6487 | 128.6133 | 0.0036 | 0.0184 |
| 2024_09_20 22:00 | 3211562 | 6 | 7.5911 | 8.3739 | -117.3538 | 17.8850 | 161.1448 | 0.0032 | 0.0154 |
| 2024_09_20 22:00 | 3265624 | 7 | 7.4685 | 16.9869 | -115.2666 | 3.8125 | 20.9887 | 0.0077 | 0.0161 |
| 2024_09_20 22:00 | 3212361 | 8 | 8.5454 | 17.8867 | -117.0072 | 3.8533 | 21.8516 | 0.0100 | 0.0197 |
| 2024_09_20 22:00 | 3266350 | 9 | 5.6504 | 9.4128 | -115.0457 | 4.4215 | 54.1791 | 0.0184 | 0.0110 |
| 2024_09_20 22:00 | 3226950 | 10 | 10.5817 | 9.9916 | -115.7520 | 3.4896 | 59.4103 | 0.0031 | 0.0127 |
| 2024_09_20 22:00 | 3217962 | 11 | 13.9726 | 5.3974 | -117.0923 | 4.9884 | 52.8850 | 0.0143 | 0.0096 |
| 2024_09_20 22:00 | 3262399 | 12 | 15.6111 | 10.9978 | -115.0687 | 3.1507 | 35.2376 | 0.0112 | 0.0074 |
| 2024_09_20 22:00 | 3261010 | 13 | 13.4406 | 17.0309 | -114.6073 | 3.8011 | 27.0124 | 0.0009 | 0.0142 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415853_92EAF6A5 | 504990 | 394 | -94.9 | 504990 | 281 | -91.5 | 504990 | 49 | -99.3 | 504990 | 587 |
| MR_1774415853_174EE838 | 504990 | 394 | -95.2 | 504990 | 281 | -90.9 | 504990 | 49 | -101.4 | 504990 | 587 |
| MR_1774415853_BB4BAF5E | 152650 | 974 | -97.6 | 152650 | 793 | -103.0 | 152650 | 808 | -105.9 | 152650 | 552 |
| MR_1774415853_2E8DB054 | 504990 | 394 | -95.3 | 504990 | 281 | -92.0 | 504990 | 49 | -102.6 | 504990 | 587 |
| MR_1774415853_DD6E761B | 504990 | 394 | -93.7 | 504990 | 281 | -93.1 | 504990 | 49 | -101.1 | 504990 | 587 |
| MR_1774415853_CAFF7C51 | 152650 | 974 | -94.1 | 152650 | 793 | -103.7 | 152650 | 808 | -104.3 | 152650 | 552 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1918: `1f03cc47-a2a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1f03cc47-a2ae-4c43-b60a-d2cacd30171d` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1918] topology](images/train_1918.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3239694_3 by 7 degrees
- `C2`: Decrease transmission power for 3267091_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239694_3
- `C4`: Adjust the azimuth of 3267091_2 by 34 degrees
- `C5`: Decrease A3 Offset threshold for 3267091_2
- `C6`: Add neighbor relationship between 3239694_3 and 3267091_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239694_3
- `C8`: Decrease A3 Offset threshold for 3239694_3
- `C9`: Decrease transmission power for 3239694_3
- `C10`: Increase transmission power for 3239694_3
- `C11`: Lift the tilt angle of 3239694_3 by 7 degrees
- `C12`: Check test server and transmission issues **← 정답**
- `C13`: Increase A3 Offset threshold for 3267091_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267091_2
- `C15`: Adjust the azimuth of 3239694_3 by 37 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase transmission power for 3267091_2
- `C18`: Lift the tilt angle  of 3267091_2 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3239694_3
- `C20`: Press down the tilt angle  of 3267091_2 by 10 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267091_2
- `C22`: Add neighbor relationship between 3224134_1 and 3267091_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.725 | MS1 | 121.4656722429 | 31.1446269788 | 900 | 504990 | -88.47 | 14.83 | 340.94 | 0.00 | 2.91 | 1570 |
| 2024-09-20 22:21:32.287 | MS1 | 121.4656643443 | 31.1446353646 | 900 | 504990 | -85.93 | 14.14 | 448.98 | 0.10 | 2.96 | 1587 |
| 2024-09-20 22:21:33.488 | MS1 | 121.4656600793 | 31.1446366407 | 900 | 504990 | -89.27 | 13.19 | 568.83 | 0.17 | 2.92 | 1567 |
| 2024-09-20 22:21:34.185 | MS1 | 121.4656636847 | 31.1446291585 | 900 | 504990 | -91.11 | 15.09 | 77.92 | 0.02 | 2.67 | 317 |
| 2024-09-20 22:21:35.678 | MS1 | 121.4656658521 | 31.1446278199 | 900 | 504990 | -90.97 | 13.17 | 61.38 | 0.03 | 2.69 | 499 |
| 2024-09-20 22:21:36.786 | MS1 | 121.4656606034 | 31.1446266779 | 900 | 504990 | -89.02 | 16.07 | 91.35 | 0.17 | 2.98 | 348 |
| 2024-09-20 22:21:37.188 | MS1 | 121.4656696953 | 31.1446305342 | 900 | 504990 | -93.93 | 7.81 | 92.30 | 0.02 | 2.73 | 360 |
| 2024-09-20 22:21:38.383 | MS1 | 121.4656630301 | 31.1446363975 | 900 | 504990 | -90.49 | 11.48 | 64.87 | 0.11 | 2.75 | 460 |
| 2024-09-20 22:21:39.922 | MS1 | 121.4656743612 | 31.1446378127 | 900 | 504990 | -89.34 | 10.86 | 76.42 | 0.06 | 2.52 | 428 |
| 2024-09-20 22:21:40.249 | MS1 | 121.4656775037 | 31.1446217143 | 900 | 504990 | -93.22 | 11.94 | 397.47 | 0.15 | 2.48 | 1569 |
| 2024-09-20 22:21:41.775 | MS1 | 121.4656762933 | 31.1446331915 | 900 | 504990 | -90.46 | 7.35 | 410.19 | 0.01 | 2.64 | 1560 |
| 2024-09-20 22:21:42.777 | MS1 | 121.4656726150 | 31.1446252003 | 900 | 504990 | -90.19 | 8.86 | 557.04 | 0.01 | 2.84 | 1576 |

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
| 3224134 | 1 | 121.4733691352 | 31.1496218594 | 259 | 5 | 11 | 45.7 | TDD | 384 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3230774 | 4 | 121.4681559849 | 31.1515396493 | 88 | 15 | 3 | 29.9 | TDD | 478 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3239694 | 3 | 121.4744057223 | 31.1523461103 | 187 | 5 | 2 | 44.4 | TDD | 900 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3267091 | 2 | 121.4686924901 | 31.1445360248 | 238 | 9 | 5 | 39.2 | TDD | 939 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.813 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.835 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.970 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.970 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.616 | NREventA3 | measId:2;ServCellPCI:34;Ser... |
| 2024-09-20 22:21:37.856 | NRHandoverAttempt | SourcePCI:34;SourceNR-ARFCN... |
| 2024-09-20 22:21:37.887 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.902 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.002 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.002 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224134 | 1 | 13.8228 | 12.5603 | -116.5077 | 14.4429 | 182.5193 | 0.0085 | 0.0124 |
| 2024_09_20 22:00 | 3267091 | 2 | 14.5625 | 10.5006 | -117.3086 | 11.5123 | 194.2621 | 0.0092 | 0.0036 |
| 2024_09_20 22:00 | 3239694 | 3 | 11.1789 | 9.9027 | -115.4673 | 6.2628 | 82.5069 | 0.0017 | 0.0057 |
| 2024_09_20 22:00 | 3230774 | 4 | 8.4055 | 9.9458 | -116.2693 | 19.3151 | 134.0199 | 0.0017 | 0.0097 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414784_D8EA8659 | 504990 | 900 | -89.6 | 504990 | 939 | -95.3 | 504990 | 384 | -102.8 | 504990 | 478 |
| MR_1774414784_A11977E0 | 504990 | 900 | -92.6 | 504990 | 939 | -94.8 | 504990 | 384 | -99.6 | 504990 | 478 |
| MR_1774414784_39514A1C | 504990 | 900 | -90.4 | 504990 | 939 | -97.0 | 504990 | 384 | -99.7 | 504990 | 478 |
| MR_1774414784_94BE375C | 504990 | 900 | -89.3 | 504990 | 939 | -94.9 | 504990 | 384 | -101.5 | 504990 | 478 |
| MR_1774414784_D9EB7897 | 504990 | 900 | -92.9 | 504990 | 939 | -94.9 | 504990 | 384 | -100.0 | 504990 | 478 |
| MR_1774414784_3A2ADAD8 | 504990 | 900 | -91.3 | 504990 | 939 | -98.3 | 504990 | 384 | -101.0 | 504990 | 478 |
| MR_1774414784_0E3E4715 | 504990 | 900 | -93.0 | 504990 | 939 | -96.4 | 504990 | 384 | -102.4 | 504990 | 478 |
| MR_1774414784_5A8F223C | 504990 | 900 | -90.3 | 504990 | 939 | -96.6 | 504990 | 384 | -100.7 | 504990 | 478 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1919: `0d3a7d5b-0cd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0d3a7d5b-0cdd-4b9f-b7ed-518b4a13ee98` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Add neighbor relationship between 3259079_4 and 3268923_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1919] topology](images/train_1919.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3221202_3 and 3268923_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268923_1
- `C3`: Lift the tilt angle  of 3268923_1 by 4 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259079_4
- `C6`: Decrease transmission power for 3259079_4
- `C7`: Press down the tilt angle  of 3268923_1 by 4 degrees
- `C8`: Increase A3 Offset threshold for 3259079_4
- `C9`: Decrease transmission power for 3268923_1
- `C10`: Add neighbor relationship between 3259079_4 and 3268923_1 **← 정답**
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268923_1
- `C12`: Adjust the azimuth of 3268923_1 by 50 degrees
- `C13`: Adjust the azimuth of 3259079_4 by 50 degrees
- `C14`: Increase transmission power for 3259079_4
- `C15`: Decrease A3 Offset threshold for 3259079_4
- `C16`: Decrease A3 Offset threshold for 3268923_1
- `C17`: Press down the tilt angle of 3259079_4 by 2 degrees
- `C18`: Increase transmission power for 3268923_1
- `C19`: Increase A3 Offset threshold for 3268923_1
- `C20`: Lift the tilt angle of 3259079_4 by 2 degrees
- `C21`: Check test server and transmission issues
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259079_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.967 | MS1 | 121.4656687352 | 31.1446316014 | 375 | 504990 | -81.51 | 17.80 | 578.12 | 0.16 | 2.32 | 1572 |
| 2024-09-20 22:21:32.944 | MS1 | 121.4656736874 | 31.1446296818 | 375 | 504990 | -75.75 | 14.46 | 339.25 | 0.15 | 2.91 | 1595 |
| 2024-09-20 22:21:33.890 | MS1 | 121.4656717974 | 31.1446364443 | 375 | 504990 | -83.46 | 14.79 | 482.73 | 0.05 | 2.40 | 1563 |
| 2024-09-20 22:21:34.301 | MS1 | 121.4656764237 | 31.1446312773 | 375 | 504990 | -93.19 | -2.42 | 36.44 | 0.06 | 1.12 | 1561 |
| 2024-09-20 22:21:35.930 | MS1 | 121.4656670878 | 31.1446375028 | 375 | 504990 | -87.37 | -1.42 | 69.96 | 0.12 | 1.45 | 1571 |
| 2024-09-20 22:21:36.461 | MS1 | 121.4656690860 | 31.1446297332 | 375 | 504990 | -85.01 | -0.64 | 61.64 | 0.04 | 1.30 | 1595 |
| 2024-09-20 22:21:37.324 | MS1 | 121.4656640890 | 31.1446325508 | 375 | 504990 | -92.72 | -2.36 | 56.94 | 0.10 | 1.39 | 1598 |
| 2024-09-20 22:21:38.386 | MS1 | 121.4656628047 | 31.1446205063 | 375 | 504990 | -77.25 | 17.11 | 561.93 | 0.04 | 1.09 | 1565 |
| 2024-09-20 22:21:39.551 | MS1 | 121.4656591884 | 31.1446355598 | 375 | 504990 | -75.53 | 15.00 | 568.60 | 0.06 | 1.24 | 1599 |
| 2024-09-20 22:21:40.467 | MS1 | 121.4656723170 | 31.1446323447 | 375 | 504990 | -83.33 | 15.42 | 359.95 | 0.05 | 2.16 | 1571 |
| 2024-09-20 22:21:41.278 | MS1 | 121.4656690902 | 31.1446285524 | 375 | 504990 | -80.45 | 15.37 | 532.28 | 0.03 | 2.95 | 1596 |
| 2024-09-20 22:21:42.301 | MS1 | 121.4656735187 | 31.1446345927 | 375 | 504990 | -80.11 | 13.96 | 535.13 | 0.15 | 2.73 | 1562 |

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
| 3221202 | 3 | 121.4669614162 | 31.1478554508 | 288 | 2 | 6 | 43.4 | TDD | 396 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3258238 | 2 | 121.4658962646 | 31.1445370329 | 212 | 3 | 12 | 38.5 | TDD | 155 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3259079 | 4 | 121.4640980361 | 31.1555154126 | 357 | 1 | 8 | 22.9 | TDD | 375 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3268923 | 1 | 121.4664187592 | 31.1536365839 | 234 | 3 | 12 | 19.3 | TDD | 120 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.297 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.403 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.403 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.154 | NREventA3 | measId:2;ServCellPCI:71;Ser... |
| 2024-09-20 22:21:36.154 | NREventA3 | measId:2;ServCellPCI:71;Ser... |
| 2024-09-20 22:21:37.154 | NREventA3 | measId:2;ServCellPCI:71;Ser... |
| 2024-09-20 22:21:39.654 | NRRRCReestablishAttempt | PCI:71 |
| 2024-09-20 22:21:39.666 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.681 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.809 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.809 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268923 | 1 | 9.8451 | 10.1765 | -117.6376 | 5.3115 | 99.0739 | 0.0019 | 0.0061 |
| 2024_09_20 22:00 | 3258238 | 2 | 9.9490 | 8.2055 | -114.5492 | 6.1883 | 96.7550 | 0.0093 | 0.0098 |
| 2024_09_20 22:00 | 3221202 | 3 | 8.1366 | 9.0005 | -116.3307 | 7.5460 | 141.3386 | 0.0051 | 0.0113 |
| 2024_09_20 22:00 | 3259079 | 4 | 16.6384 | 9.1203 | -117.2149 | 9.5335 | 162.4934 | 0.0000 | 0.1416 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413703_30FA74C8 | 504990 | 375 | -93.7 | 504990 | 120 | -88.3 | 504990 | 396 | -93.2 | 504990 | 155 |
| MR_1774413703_85587869 | 504990 | 120 | -87.8 | 504990 | 375 | -94.3 | 504990 | 396 | -91.6 | 504990 | 155 |
| MR_1774413703_B21A56D6 | 504990 | 375 | -94.6 | 504990 | 120 | -88.2 | 504990 | 396 | -91.4 | 504990 | 155 |
| MR_1774413703_D2B2DBC0 | 504990 | 120 | -88.1 | 504990 | 375 | -92.0 | 504990 | 396 | -90.1 | 504990 | 155 |
| MR_1774413703_749A0250 | 504990 | 120 | -87.1 | 504990 | 375 | -95.1 | 504990 | 396 | -93.1 | 504990 | 155 |
| MR_1774413703_A01AA410 | 504990 | 120 | -89.1 | 504990 | 375 | -94.3 | 504990 | 396 | -90.1 | 504990 | 155 |
| MR_1774413703_E3668049 | 504990 | 375 | -92.8 | 504990 | 120 | -90.7 | 504990 | 396 | -93.0 | 504990 | 155 |
| MR_1774413703_30A9FCE9 | 504990 | 120 | -89.1 | 504990 | 375 | -92.8 | 504990 | 396 | -90.4 | 504990 | 155 |

> *... 2개 열 생략 (전체 14열)*

---
