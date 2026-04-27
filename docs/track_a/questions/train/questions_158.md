# Track A 문제 분석 — train[1570]~train[1579]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1570] ~ train[1579] (10개)

## 목차

1. [문제 1570: `dc4109fc-c5d...`](#1570) — multiple-answer, 정답: C5|C7
2. [문제 1571: `099cc5ee-2b2...`](#1571) — multiple-answer, 정답: C3|C7|C15|C21
3. [문제 1572: `c682ddcf-d46...`](#1572) — single-answer, 정답: C8
4. [문제 1573: `1636d995-c13...`](#1573) — single-answer, 정답: C9
5. [문제 1574: `d1e37124-1ea...`](#1574) — single-answer, 정답: C1
6. [문제 1575: `7b254636-496...`](#1575) — single-answer, 정답: C11
7. [문제 1576: `868ec53a-73b...`](#1576) — single-answer, 정답: C6
8. [문제 1577: `51c56ab5-29c...`](#1577) — single-answer, 정답: C4
9. [문제 1578: `f2d473a1-010...`](#1578) — single-answer, 정답: C20
10. [문제 1579: `47eec279-fbc...`](#1579) — single-answer, 정답: C2

---

### 문제 1570: `dc4109fc-c5d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dc4109fc-c5db-4a2f-bc90-907c3dcc56c5` |
| Tag | **multiple-answer** |
| 정답 | **C5|C7** |
| C5 의미 | Decrease transmission power for 3225959_1 |
| C7 의미 | Press down the tilt angle  of 3225959_1 by 6 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1570] topology](images/train_1570.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3225959_1
- `C2`: Add neighbor relationship between 3228229_4 and 3225959_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225959_1
- `C4`: Lift the tilt angle  of 3225959_1 by 6 degrees
- `C5`: Decrease transmission power for 3225959_1 **← 정답**
- `C6`: Adjust the azimuth of 3228229_4 by 2 degrees
- `C7`: Press down the tilt angle  of 3225959_1 by 6 degrees **← 정답**
- `C8`: Press down the tilt angle of 3228229_4 by 3 degrees
- `C9`: Add neighbor relationship between 3264482_3 and 3225959_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228229_4
- `C11`: Adjust the azimuth of 3225959_1 by 4 degrees
- `C12`: Check test server and transmission issues
- `C13`: Decrease transmission power for 3228229_4
- `C14`: Decrease A3 Offset threshold for 3225959_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228229_4
- `C17`: Lift the tilt angle of 3228229_4 by 3 degrees
- `C18`: Decrease A3 Offset threshold for 3228229_4
- `C19`: Increase transmission power for 3225959_1
- `C20`: Increase A3 Offset threshold for 3228229_4
- `C21`: Increase transmission power for 3228229_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225959_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.269 | MS1 | 121.4656642131 | 31.1446282019 | 670 | 504990 | -79.36 | 12.63 | 547.01 | 0.10 | 2.73 | 1571 |
| 2024-09-20 22:21:32.918 | MS1 | 121.4656582741 | 31.1446266852 | 670 | 504990 | -81.50 | 13.70 | 324.18 | 0.06 | 2.31 | 1572 |
| 2024-09-20 22:21:33.329 | MS1 | 121.4656633808 | 31.1446252799 | 670 | 504990 | -79.55 | 12.18 | 541.77 | 0.16 | 2.39 | 1571 |
| 2024-09-20 22:21:34.536 | MS1 | 121.4656584442 | 31.1446189333 | 670 | 504990 | -85.50 | 2.69 | 54.27 | 0.17 | 1.09 | 1569 |
| 2024-09-20 22:21:35.139 | MS1 | 121.4656586902 | 31.1446286761 | 670 | 504990 | -86.64 | 3.99 | 85.57 | 0.12 | 1.45 | 1585 |
| 2024-09-20 22:21:36.225 | MS1 | 121.4656717396 | 31.1446320530 | 670 | 504990 | -89.48 | 3.35 | 49.88 | 0.06 | 1.25 | 1561 |
| 2024-09-20 22:21:37.971 | MS1 | 121.4656604128 | 31.1446210904 | 670 | 504990 | -86.48 | 0.11 | 53.75 | 0.04 | 1.10 | 1583 |
| 2024-09-20 22:21:38.490 | MS1 | 121.4656659803 | 31.1446376346 | 670 | 504990 | -85.89 | 1.79 | 60.51 | 0.19 | 1.05 | 1580 |
| 2024-09-20 22:21:39.348 | MS1 | 121.4656613177 | 31.1446335952 | 670 | 504990 | -86.60 | 1.68 | 68.35 | 0.00 | 1.49 | 1561 |
| 2024-09-20 22:21:40.706 | MS1 | 121.4656657373 | 31.1446292082 | 670 | 504990 | -83.33 | 14.21 | 545.58 | 0.05 | 2.50 | 1561 |
| 2024-09-20 22:21:41.331 | MS1 | 121.4656699108 | 31.1446234909 | 670 | 504990 | -78.06 | 15.99 | 531.79 | 0.13 | 2.67 | 1599 |
| 2024-09-20 22:21:42.920 | MS1 | 121.4656755001 | 31.1446243009 | 670 | 504990 | -83.16 | 15.20 | 452.18 | 0.08 | 2.13 | 1576 |

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
| 3220050 | 2 | 121.4746509970 | 31.1486702587 | 113 | 6 | 11 | 15.1 | TDD | 312 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3225959 | 1 | 121.4727991052 | 31.1510878990 | 227 | 3 | 1 | 49.4 | TDD | 704 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3228229 | 4 | 121.4731992579 | 31.1513674552 | 222 | 1 | 9 | 31.2 | TDD | 670 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3264482 | 3 | 121.4746319758 | 31.1559707243 | 306 | 6 | 5 | 20.8 | TDD | 541 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.613 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.719 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.719 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225959 | 1 | 8.5484 | 14.6502 | -114.6396 | 8.6400 | 87.9986 | 0.0072 | 0.0170 |
| 2024_09_20 22:00 | 3220050 | 2 | 14.7555 | 15.8921 | -115.1193 | 12.4823 | 175.3368 | 0.0141 | 0.0063 |
| 2024_09_20 22:00 | 3264482 | 3 | 14.1708 | 5.9421 | -114.4870 | 10.0585 | 166.1498 | 0.0026 | 0.0162 |
| 2024_09_20 22:00 | 3228229 | 4 | 14.4897 | 9.6654 | -108.3771 | 6.5355 | 80.7350 | 0.0127 | 0.0034 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414269_44A57FC8 | 504990 | 704 | -84.0 | 504990 | 670 | -83.9 | 504990 | 541 | -84.6 | 504990 | 312 |
| MR_1774414269_3F217E68 | 504990 | 704 | -85.5 | 504990 | 670 | -84.9 | 504990 | 541 | -85.8 | 504990 | 312 |
| MR_1774414269_6C6F6264 | 504990 | 704 | -85.8 | 504990 | 670 | -85.0 | 504990 | 541 | -85.6 | 504990 | 312 |
| MR_1774414269_048492CF | 504990 | 704 | -87.4 | 504990 | 670 | -83.7 | 504990 | 541 | -85.8 | 504990 | 312 |
| MR_1774414269_68AEEFA2 | 504990 | 670 | -86.7 | 504990 | 704 | -83.7 | 504990 | 541 | -83.9 | 504990 | 312 |
| MR_1774414269_62A02DE8 | 504990 | 704 | -86.9 | 504990 | 670 | -86.1 | 504990 | 541 | -85.0 | 504990 | 312 |
| MR_1774414269_B7A7C97A | 504990 | 670 | -87.1 | 504990 | 704 | -83.4 | 504990 | 541 | -84.4 | 504990 | 312 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1571: `099cc5ee-2b2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `099cc5ee-2b2a-44f0-b377-d6f701957288` |
| Tag | **multiple-answer** |
| 정답 | **C3|C7|C15|C21** |
| C3 의미 | Decrease transmission power for 3220391_5 |
| C7 의미 | Increase A3 Offset threshold for 3225397_3 |
| C15 의미 | Increase A3 Offset threshold for 3220391_5 |
| C21 의미 | Press down the tilt angle  of 3220391_5 by 4 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1571] topology](images/train_1571.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3220391_5
- `C2`: Check test server and transmission issues
- `C3`: Decrease transmission power for 3220391_5 **← 정답**
- `C4`: Press down the tilt angle of 3225397_3 by 2 degrees
- `C5`: Decrease A3 Offset threshold for 3225397_3
- `C6`: Decrease transmission power for 3225397_3
- `C7`: Increase A3 Offset threshold for 3225397_3 **← 정답**
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220391_5
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225397_3
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase transmission power for 3220391_5
- `C12`: Adjust the azimuth of 3225397_3 by 38 degrees
- `C13`: Add neighbor relationship between 3251135_4 and 3220391_5
- `C14`: Lift the tilt angle of 3225397_3 by 2 degrees
- `C15`: Increase A3 Offset threshold for 3220391_5 **← 정답**
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220391_5
- `C17`: Adjust the azimuth of 3220391_5 by 17 degrees
- `C18`: Increase transmission power for 3225397_3
- `C19`: Lift the tilt angle  of 3220391_5 by 4 degrees
- `C20`: Add neighbor relationship between 3225397_3 and 3220391_5
- `C21`: Press down the tilt angle  of 3220391_5 by 4 degrees **← 정답**
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225397_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.765 | MS1 | 121.4656698904 | 31.1446278197 | 122 | 504990 | -82.90 | 12.94 | 577.05 | 0.06 | 2.46 | 1563 |
| 2024-09-20 22:21:32.383 | MS1 | 121.4656686921 | 31.1446322543 | 122 | 504990 | -84.10 | 15.39 | 315.78 | 0.14 | 2.71 | 1586 |
| 2024-09-20 22:21:33.228 | MS1 | 121.4656777940 | 31.1446194690 | 122 | 504990 | -78.47 | 15.43 | 495.56 | 0.06 | 2.15 | 1587 |
| 2024-09-20 22:21:34.860 | MS1 | 121.4656608196 | 31.1446200403 | 221 | 504990 | -89.25 | 2.06 | 51.10 | 0.19 | 1.47 | 1575 |
| 2024-09-20 22:21:35.559 | MS1 | 121.4656729523 | 31.1446235925 | 221 | 504990 | -83.78 | 4.43 | 49.77 | 0.17 | 1.37 | 1567 |
| 2024-09-20 22:21:36.354 | MS1 | 121.4656649813 | 31.1446332798 | 122 | 504990 | -86.13 | 1.23 | 46.92 | 0.02 | 1.15 | 1573 |
| 2024-09-20 22:21:37.465 | MS1 | 121.4656600564 | 31.1446354623 | 122 | 504990 | -80.09 | 2.49 | 40.96 | 0.00 | 1.11 | 1596 |
| 2024-09-20 22:21:38.473 | MS1 | 121.4656771195 | 31.1446242391 | 221 | 504990 | -88.41 | 4.38 | 60.45 | 0.12 | 1.36 | 1588 |
| 2024-09-20 22:21:39.307 | MS1 | 121.4656610144 | 31.1446238403 | 221 | 504990 | -80.46 | 3.46 | 58.43 | 0.05 | 1.33 | 1581 |
| 2024-09-20 22:21:40.547 | MS1 | 121.4656693655 | 31.1446351861 | 221 | 504990 | -80.83 | 15.01 | 388.97 | 0.20 | 2.64 | 1596 |
| 2024-09-20 22:21:41.707 | MS1 | 121.4656725635 | 31.1446236129 | 221 | 504990 | -76.10 | 16.94 | 566.97 | 0.11 | 2.88 | 1561 |
| 2024-09-20 22:21:42.604 | MS1 | 121.4656623270 | 31.1446237704 | 221 | 504990 | -76.02 | 13.61 | 374.40 | 0.14 | 2.71 | 1591 |

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
| 3220391 | 5 | 121.4730602409 | 31.1475517976 | 262 | 2 | 10 | 25.8 | TDD | 893 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3225397 | 3 | 121.4701570227 | 31.1479665051 | 191 | 0 | 9 | 20.3 | TDD | 122 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3245561 | 1 | 121.4755488583 | 31.1519994285 | 352 | 13 | 11 | 21.2 | TDD | 822 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3247941 | 2 | 121.4711093664 | 31.1503175369 | 280 | 12 | 12 | 30.8 | TDD | 221 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3251135 | 4 | 121.4664336510 | 31.1448667177 | 50 | 14 | 1 | 33.9 | TDD | 892 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.048 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.068 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.212 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.212 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.903 | NREventA3 | measId:2;ServCellPCI:753;Se... |
| 2024-09-20 22:21:34.143 | NRHandoverAttempt | SourcePCI:753;SourceNR-ARFC... |
| 2024-09-20 22:21:34.184 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.194 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:34.313 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.313 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.903 | NREventA3 | measId:2;ServCellPCI:885;Se... |
| 2024-09-20 22:21:36.143 | NRHandoverAttempt | SourcePCI:885;SourceNR-ARFC... |
| 2024-09-20 22:21:36.175 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.190 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.296 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.296 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.903 | NREventA3 | measId:2;ServCellPCI:753;Se... |
| 2024-09-20 22:21:38.143 | NRHandoverAttempt | SourcePCI:753;SourceNR-ARFC... |
| 2024-09-20 22:21:38.180 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.195 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.325 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.325 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245561 | 1 | 7.3963 | 8.1530 | -117.5949 | 9.1622 | 86.1675 | 0.0199 | 0.0070 |
| 2024_09_20 22:00 | 3247941 | 2 | 14.8965 | 9.5103 | -115.9859 | 15.4852 | 157.0844 | 0.0000 | 0.0138 |
| 2024_09_20 22:00 | 3225397 | 3 | 13.9546 | 12.7914 | -117.8165 | 18.2664 | 176.8799 | 0.0060 | 0.0139 |
| 2024_09_20 22:00 | 3251135 | 4 | 19.8558 | 19.8111 | -117.4757 | 6.3695 | 103.8974 | 0.0125 | 0.0085 |
| 2024_09_20 22:00 | 3220391 | 5 | 7.4408 | 15.9053 | -115.4910 | 18.5894 | 118.2454 | 0.0054 | 0.0113 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415434_9A6ECB00 | 504990 | 221 | -89.1 | 504990 | 122 | -90.3 | 504990 | 893 | -95.5 | 504990 | 892 |
| MR_1774415434_237D21AB | 504990 | 221 | -88.9 | 504990 | 122 | -90.4 | 504990 | 893 | -94.3 | 504990 | 892 |
| MR_1774415434_F5A2EEB1 | 504990 | 221 | -91.1 | 504990 | 122 | -89.2 | 504990 | 893 | -96.7 | 504990 | 892 |
| MR_1774415434_FF2AF136 | 504990 | 221 | -90.5 | 504990 | 122 | -87.3 | 504990 | 893 | -95.6 | 504990 | 892 |
| MR_1774415434_20FE4D19 | 504990 | 122 | -88.2 | 504990 | 221 | -88.5 | 504990 | 893 | -96.1 | 504990 | 892 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1572: `c682ddcf-d46...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c682ddcf-d466-44d9-9342-c20ac8b0e8f1` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260853_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1572] topology](images/train_1572.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3260853_4 by 1 degrees
- `C2`: Decrease A3 Offset threshold for 3260853_4
- `C3`: Decrease A3 Offset threshold for 3217200_6
- `C4`: Increase transmission power for 3260853_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260853_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease transmission power for 3217200_6
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260853_4 **← 정답**
- `C9`: Press down the tilt angle  of 3217200_6 by 2 degrees
- `C10`: Increase A3 Offset threshold for 3217200_6
- `C11`: Add neighbor relationship between 3260853_4 and 3217200_6
- `C12`: Increase A3 Offset threshold for 3260853_4
- `C13`: Check test server and transmission issues
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217200_6
- `C15`: Decrease transmission power for 3260853_4
- `C16`: Adjust the azimuth of 3217200_6 by 15 degrees
- `C17`: Increase transmission power for 3217200_6
- `C18`: Adjust the azimuth of 3260853_4 by 44 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217200_6
- `C20`: Press down the tilt angle of 3260853_4 by 1 degrees
- `C21`: Add neighbor relationship between 3249468_13 and 3217200_6
- `C22`: Lift the tilt angle  of 3217200_6 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.483 | MS1 | 121.4656624343 | 31.1446230841 | 660 | 504990 | -93.41 | 11.35 | 523.83 | 0.09 | 2.08 | 1588 |
| 2024-09-20 22:21:32.452 | MS1 | 121.4656749786 | 31.1446318673 | 9 | 504990 | -95.86 | 10.42 | 335.56 | 0.17 | 2.09 | 1594 |
| 2024-09-20 22:21:33.494 | MS1 | 121.4656643993 | 31.1446377559 | 314 | 504990 | -93.15 | 9.11 | 534.40 | 0.01 | 2.74 | 1598 |
| 2024-09-20 22:21:34.313 | MS1 | 121.4656696802 | 31.1446300345 | 774 | 152650 | -94.83 | 5.81 | 73.01 | 0.18 | 1.85 | 974 |
| 2024-09-20 22:21:35.977 | MS1 | 121.4656712158 | 31.1446194689 | 723 | 152650 | -87.01 | 5.00 | 59.71 | 0.20 | 1.84 | 953 |
| 2024-09-20 22:21:36.725 | MS1 | 121.4656664919 | 31.1446354767 | 253 | 152650 | -87.19 | 3.01 | 84.99 | 0.15 | 1.64 | 989 |
| 2024-09-20 22:21:37.823 | MS1 | 121.4656599339 | 31.1446221105 | 795 | 152650 | -91.83 | 2.02 | 92.56 | 0.12 | 1.51 | 928 |
| 2024-09-20 22:21:38.698 | MS1 | 121.4656706156 | 31.1446245616 | 774 | 152650 | -88.65 | 2.82 | 90.88 | 0.07 | 1.94 | 948 |
| 2024-09-20 22:21:39.691 | MS1 | 121.4656771310 | 31.1446312290 | 723 | 152650 | -95.46 | 6.67 | 78.44 | 0.17 | 1.92 | 922 |
| 2024-09-20 22:21:40.426 | MS1 | 121.4656739183 | 31.1446261339 | 253 | 152650 | -96.02 | 2.35 | 70.88 | 0.16 | 2.48 | 1596 |
| 2024-09-20 22:21:41.403 | MS1 | 121.4656777061 | 31.1446249294 | 795 | 152650 | -87.38 | 4.92 | 90.84 | 0.10 | 2.75 | 1586 |
| 2024-09-20 22:21:42.720 | MS1 | 121.4656773298 | 31.1446233701 | 774 | 152650 | -95.72 | 6.03 | 86.98 | 0.10 | 2.84 | 1575 |

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
| 3215256 | 10 | 121.4645398764 | 31.1453219813 | 271 | 5 | 1 | 17.6 | FDD | 244 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3217200 | 6 | 121.4658631746 | 31.1457092090 | 204 | 0 | 5 | 4.0 | TDD | 988 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3223842 | 12 | 121.4665129635 | 31.1501474109 | 241 | 10 | 4 | 27.6 | FDD | 795 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3225563 | 9 | 121.4719230394 | 31.1458376502 | 234 | 8 | 10 | 5.7 | FDD | 723 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3227753 | 3 | 121.4746191606 | 31.1531329103 | 226 | 2 | 10 | 21.9 | TDD | 172 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3234807 | 2 | 121.4675967204 | 31.1530733407 | 207 | 13 | 10 | 3.0 | TDD | 9 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3246159 | 5 | 121.4718206234 | 31.1478177271 | 56 | 2 | 9 | 13.7 | TDD | 314 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3249468 | 13 | 121.4688732481 | 31.1481345824 | 140 | 5 | 6 | 26.4 | FDD | 253 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3253861 | 7 | 121.4757995431 | 31.1514342919 | 326 | 0 | 8 | 19.7 | FDD | 774 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3257082 | 1 | 121.4724197403 | 31.1444163541 | 193 | 13 | 7 | 9.2 | TDD | 194 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3260853 | 4 | 121.4750052423 | 31.1475313998 | 206 | 0 | 1 | 10.5 | TDD | 660 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3264313 | 8 | 121.4698949050 | 31.1459261719 | 254 | 14 | 10 | 14.4 | FDD | 943 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3269902 | 11 | 121.4757515692 | 31.1519013905 | 110 | 8 | 4 | 21.0 | FDD | 984 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |

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
| 2024-09-20 22:21:30.927 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.948 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.066 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.066 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.800 | NREventA2 | measId:1;ServCellPCI:127;Se... |
| 2024-09-20 22:21:34.911 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.181 | NREventA5 | measId:3;ServCellPCI:127;Se... |
| 2024-09-20 22:21:35.212 | NRHandoverAttempt | SourcePCI:127;SourceNR-ARFC... |
| 2024-09-20 22:21:35.258 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.270 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.378 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.378 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257082 | 1 | 8.6790 | 13.4986 | -115.6661 | 5.1158 | 111.9717 | 0.0037 | 0.0080 |
| 2024_09_20 22:00 | 3234807 | 2 | 10.7032 | 17.4425 | -117.2650 | 12.5479 | 113.6506 | 0.0053 | 0.0098 |
| 2024_09_20 22:00 | 3227753 | 3 | 18.2445 | 15.9349 | -116.3312 | 15.4783 | 130.2009 | 0.0149 | 0.0200 |
| 2024_09_20 22:00 | 3260853 | 4 | 13.6061 | 19.1286 | -115.5568 | 16.5537 | 130.1283 | 0.0006 | 0.0006 |
| 2024_09_20 22:00 | 3246159 | 5 | 8.9973 | 10.8118 | -117.4333 | 8.6332 | 161.9000 | 0.0105 | 0.0092 |
| 2024_09_20 22:00 | 3217200 | 6 | 6.1001 | 7.3389 | -115.1601 | 6.3348 | 171.0815 | 0.0040 | 0.0040 |
| 2024_09_20 22:00 | 3253861 | 7 | 17.1845 | 10.2041 | -116.7157 | 4.1832 | 33.3952 | 0.0128 | 0.0068 |
| 2024_09_20 22:00 | 3264313 | 8 | 16.8292 | 12.2064 | -116.2873 | 3.1485 | 58.4601 | 0.0003 | 0.0127 |
| 2024_09_20 22:00 | 3225563 | 9 | 6.1744 | 5.7138 | -117.3934 | 4.6370 | 40.5377 | 0.0084 | 0.0057 |
| 2024_09_20 22:00 | 3215256 | 10 | 9.5692 | 8.3439 | -114.9247 | 4.9623 | 20.2613 | 0.0136 | 0.0065 |
| 2024_09_20 22:00 | 3269902 | 11 | 7.8199 | 8.2086 | -114.3490 | 3.0021 | 43.3711 | 0.0132 | 0.0139 |
| 2024_09_20 22:00 | 3223842 | 12 | 7.0487 | 12.1904 | -116.4847 | 4.3769 | 28.8218 | 0.0039 | 0.0089 |
| 2024_09_20 22:00 | 3249468 | 13 | 6.4877 | 9.9740 | -117.6654 | 4.1474 | 31.2514 | 0.0022 | 0.0190 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416648_DEBD1DCD | 152650 | 774 | -94.1 | 152650 | 984 | -104.4 | 152650 | 943 | -103.8 | 152650 | 244 |
| MR_1774416648_E6C1A95D | 152650 | 774 | -92.9 | 152650 | 984 | -102.2 | 152650 | 943 | -107.4 | 152650 | 244 |
| MR_1774416648_5C792895 | 152650 | 774 | -94.1 | 152650 | 984 | -104.0 | 152650 | 943 | -107.3 | 152650 | 244 |
| MR_1774416648_D426753E | 152650 | 774 | -94.8 | 152650 | 984 | -103.7 | 152650 | 943 | -107.7 | 152650 | 244 |
| MR_1774416648_DC99FFDF | 152650 | 774 | -94.6 | 152650 | 984 | -104.2 | 152650 | 943 | -105.2 | 152650 | 244 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1573: `1636d995-c13...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1636d995-c13d-47db-ae8d-fbd414aaeb40` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Lift the tilt angle  of 3210873_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1573] topology](images/train_1573.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262336_3
- `C2`: Increase transmission power for 3262336_3
- `C3`: Check test server and transmission issues
- `C4`: Press down the tilt angle of 3221665_2 by 6 degrees
- `C5`: Add neighbor relationship between 3210873_1 and 3262336_3
- `C6`: Decrease A3 Offset threshold for 3262336_3
- `C7`: Decrease transmission power for 3262336_3
- `C8`: Decrease A3 Offset threshold for 3221665_2
- `C9`: Lift the tilt angle  of 3210873_1 by 10 degrees **← 정답**
- `C10`: Adjust the azimuth of 3210873_1 by 21 degrees
- `C11`: Increase transmission power for 3221665_2
- `C12`: Increase A3 Offset threshold for 3262336_3
- `C13`: Press down the tilt angle  of 3210873_1 by 10 degrees
- `C14`: Decrease transmission power for 3221665_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221665_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Add neighbor relationship between 3221665_2 and 3262336_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262336_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221665_2
- `C20`: Adjust the azimuth of 3221665_2 by 21 degrees
- `C21`: Increase A3 Offset threshold for 3221665_2
- `C22`: Lift the tilt angle of 3221665_2 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.824 | MS1 | 121.4656607705 | 31.1446241173 | 659 | 504990 | -89.07 | 17.71 | 548.19 | 0.17 | 2.18 | 1600 |
| 2024-09-20 22:21:32.327 | MS1 | 121.4656644319 | 31.1446291407 | 659 | 504990 | -91.36 | 16.84 | 368.62 | 0.05 | 2.41 | 1594 |
| 2024-09-20 22:21:33.257 | MS1 | 121.4656773267 | 31.1446346088 | 659 | 504990 | -89.03 | 17.82 | 574.66 | 0.01 | 2.15 | 1571 |
| 2024-09-20 22:21:34.369 | MS1 | 121.4656588877 | 31.1446354045 | 659 | 504990 | -87.35 | 14.09 | 55.58 | 0.05 | 2.10 | 1599 |
| 2024-09-20 22:21:35.117 | MS1 | 121.4656636226 | 31.1446281583 | 659 | 504990 | -88.65 | 16.68 | 60.13 | 0.12 | 2.49 | 1561 |
| 2024-09-20 22:21:36.575 | MS1 | 121.4656742379 | 31.1446295179 | 659 | 504990 | -86.18 | 12.22 | 71.86 | 0.07 | 2.07 | 1598 |
| 2024-09-20 22:21:37.544 | MS1 | 121.4656664541 | 31.1446372890 | 659 | 504990 | -90.25 | 12.56 | 72.68 | 0.07 | 2.52 | 1580 |
| 2024-09-20 22:21:38.327 | MS1 | 121.4656707800 | 31.1446290973 | 659 | 504990 | -92.87 | 7.12 | 72.21 | 0.06 | 2.19 | 1592 |
| 2024-09-20 22:21:39.770 | MS1 | 121.4656633305 | 31.1446344474 | 659 | 504990 | -92.49 | 11.91 | 75.31 | 0.09 | 2.56 | 1580 |
| 2024-09-20 22:21:40.255 | MS1 | 121.4656690218 | 31.1446305338 | 659 | 504990 | -89.41 | 12.51 | 435.61 | 0.16 | 2.93 | 1583 |
| 2024-09-20 22:21:41.244 | MS1 | 121.4656657107 | 31.1446215842 | 659 | 504990 | -89.63 | 9.95 | 603.60 | 0.02 | 2.28 | 1589 |
| 2024-09-20 22:21:42.132 | MS1 | 121.4656662822 | 31.1446181466 | 659 | 504990 | -92.62 | 9.38 | 405.70 | 0.13 | 2.88 | 1575 |

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
| 3210873 | 1 | 121.4725711809 | 31.1519208908 | 111 | 10 | 6 | 23.0 | TDD | 19 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3221665 | 2 | 121.4719873790 | 31.1485598241 | 255 | 3 | 7 | 38.1 | TDD | 659 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3231876 | 4 | 121.4758260254 | 31.1444622154 | 9 | 15 | 5 | 35.2 | TDD | 588 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3262336 | 3 | 121.4673038505 | 31.1458423298 | 250 | 12 | 9 | 21.8 | TDD | 699 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.864 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.889 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.004 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.004 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.677 | NREventA3 | measId:2;ServCellPCI:199;Se... |
| 2024-09-20 22:21:37.917 | NRHandoverAttempt | SourcePCI:199;SourceNR-ARFC... |
| 2024-09-20 22:21:37.954 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.966 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.071 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.071 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210873 | 1 | 16.8507 | 15.9270 | -115.7683 | 5.7395 | 167.5608 | 0.0077 | 0.0172 |
| 2024_09_20 22:00 | 3221665 | 2 | 81.1950 | 75.0943 | -116.5798 | 9.4456 | 185.3345 | 0.0028 | 0.0128 |
| 2024_09_20 22:00 | 3262336 | 3 | 19.0334 | 14.1612 | -115.5390 | 9.7213 | 145.6303 | 0.0185 | 0.0129 |
| 2024_09_20 22:00 | 3231876 | 4 | 16.7466 | 18.6979 | -117.3926 | 16.0008 | 114.7454 | 0.0043 | 0.0183 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415142_0F87B47C | 504990 | 659 | -87.1 | 504990 | 699 | -93.2 | 504990 | 19 | -94.9 | 504990 | 588 |
| MR_1774415142_D8D40B43 | 504990 | 659 | -85.4 | 504990 | 699 | -93.3 | 504990 | 19 | -95.1 | 504990 | 588 |
| MR_1774415142_9A3FBF10 | 504990 | 659 | -87.1 | 504990 | 699 | -95.8 | 504990 | 19 | -95.2 | 504990 | 588 |
| MR_1774415142_445EAF21 | 504990 | 659 | -85.5 | 504990 | 699 | -94.7 | 504990 | 19 | -96.3 | 504990 | 588 |
| MR_1774415142_40348BBC | 504990 | 659 | -86.7 | 504990 | 699 | -92.2 | 504990 | 19 | -94.2 | 504990 | 588 |
| MR_1774415142_2ACFF2DB | 504990 | 659 | -87.4 | 504990 | 699 | -93.6 | 504990 | 19 | -94.3 | 504990 | 588 |
| MR_1774415142_1093C539 | 504990 | 659 | -85.4 | 504990 | 699 | -93.8 | 504990 | 19 | -95.0 | 504990 | 588 |
| MR_1774415142_0EE2C2AE | 504990 | 659 | -88.3 | 504990 | 699 | -95.2 | 504990 | 19 | -94.1 | 504990 | 588 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1574: `d1e37124-1ea...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d1e37124-1eaa-4176-a714-f879b4157c89` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Lift the tilt angle  of 3269977_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1574] topology](images/train_1574.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3269977_2 by 10 degrees **← 정답**
- `C2`: Increase transmission power for 3250691_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Press down the tilt angle  of 3269977_2 by 10 degrees
- `C5`: Press down the tilt angle of 3275556_4 by 2 degrees
- `C6`: Adjust the azimuth of 3275556_4 by 46 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250691_1
- `C8`: Adjust the azimuth of 3269977_2 by 50 degrees
- `C9`: Decrease A3 Offset threshold for 3250691_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275556_4
- `C11`: Lift the tilt angle of 3275556_4 by 2 degrees
- `C12`: Add neighbor relationship between 3269977_2 and 3250691_1
- `C13`: Decrease A3 Offset threshold for 3275556_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250691_1
- `C15`: Increase A3 Offset threshold for 3275556_4
- `C16`: Increase A3 Offset threshold for 3250691_1
- `C17`: Add neighbor relationship between 3275556_4 and 3250691_1
- `C18`: Increase transmission power for 3275556_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275556_4
- `C20`: Decrease transmission power for 3275556_4
- `C21`: Check test server and transmission issues
- `C22`: Decrease transmission power for 3250691_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.340 | MS1 | 121.4656595248 | 31.1446282638 | 639 | 504990 | -91.10 | 14.88 | 541.42 | 0.00 | 2.11 | 1576 |
| 2024-09-20 22:21:32.128 | MS1 | 121.4656685854 | 31.1446368656 | 639 | 504990 | -89.40 | 14.80 | 418.65 | 0.01 | 2.54 | 1579 |
| 2024-09-20 22:21:33.305 | MS1 | 121.4656687573 | 31.1446227810 | 639 | 504990 | -89.40 | 17.07 | 395.14 | 0.07 | 2.34 | 1560 |
| 2024-09-20 22:21:34.659 | MS1 | 121.4656777605 | 31.1446322592 | 639 | 504990 | -89.56 | 15.09 | 69.16 | 0.19 | 2.12 | 1575 |
| 2024-09-20 22:21:35.214 | MS1 | 121.4656582407 | 31.1446257996 | 639 | 504990 | -88.92 | 17.76 | 57.76 | 0.12 | 2.08 | 1575 |
| 2024-09-20 22:21:36.785 | MS1 | 121.4656605874 | 31.1446287692 | 639 | 504990 | -87.64 | 12.53 | 80.54 | 0.13 | 2.87 | 1573 |
| 2024-09-20 22:21:37.750 | MS1 | 121.4656618913 | 31.1446268222 | 639 | 504990 | -90.99 | 8.80 | 82.77 | 0.03 | 2.80 | 1583 |
| 2024-09-20 22:21:38.562 | MS1 | 121.4656634134 | 31.1446273641 | 639 | 504990 | -93.62 | 11.18 | 62.43 | 0.07 | 2.77 | 1572 |
| 2024-09-20 22:21:39.212 | MS1 | 121.4656678612 | 31.1446199748 | 639 | 504990 | -89.02 | 8.59 | 83.26 | 0.04 | 2.73 | 1588 |
| 2024-09-20 22:21:40.396 | MS1 | 121.4656717880 | 31.1446222467 | 639 | 504990 | -89.56 | 12.96 | 440.67 | 0.13 | 2.12 | 1583 |
| 2024-09-20 22:21:41.404 | MS1 | 121.4656623605 | 31.1446296042 | 639 | 504990 | -89.33 | 7.48 | 443.50 | 0.03 | 2.55 | 1598 |
| 2024-09-20 22:21:42.110 | MS1 | 121.4656687619 | 31.1446188192 | 639 | 504990 | -91.67 | 8.48 | 521.15 | 0.01 | 2.75 | 1588 |

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
| 3250691 | 1 | 121.4649514800 | 31.1445624096 | 189 | 13 | 5 | 24.0 | TDD | 152 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3269977 | 2 | 121.4742823685 | 31.1481992337 | 295 | 0 | 1 | 16.9 | TDD | 713 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3270262 | 3 | 121.4707461424 | 31.1487147119 | 74 | 9 | 5 | 47.0 | TDD | 754 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3275556 | 4 | 121.4732799846 | 31.1533677732 | 171 | 0 | 1 | 40.8 | TDD | 639 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.472 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.490 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.598 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.598 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.306 | NREventA3 | measId:2;ServCellPCI:222;Se... |
| 2024-09-20 22:21:38.546 | NRHandoverAttempt | SourcePCI:222;SourceNR-ARFC... |
| 2024-09-20 22:21:38.595 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.610 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.749 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.749 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250691 | 1 | 15.7602 | 8.0838 | -116.9274 | 9.4200 | 190.4104 | 0.0059 | 0.0091 |
| 2024_09_20 22:00 | 3269977 | 2 | 13.6893 | 16.1828 | -117.5161 | 9.0962 | 152.8573 | 0.0078 | 0.0154 |
| 2024_09_20 22:00 | 3270262 | 3 | 17.1656 | 6.2103 | -115.3891 | 9.5042 | 116.4711 | 0.0119 | 0.0149 |
| 2024_09_20 22:00 | 3275556 | 4 | 93.1277 | 79.3337 | -115.8604 | 6.3774 | 185.3430 | 0.0094 | 0.0088 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412393_610FAD50 | 504990 | 639 | -90.6 | 504990 | 152 | -90.5 | 504990 | 713 | -103.0 | 504990 | 754 |
| MR_1774412393_F4333FA3 | 504990 | 639 | -89.6 | 504990 | 152 | -89.2 | 504990 | 713 | -103.1 | 504990 | 754 |
| MR_1774412393_C0B98FC4 | 504990 | 639 | -87.9 | 504990 | 152 | -89.4 | 504990 | 713 | -102.4 | 504990 | 754 |
| MR_1774412393_6179C7D2 | 504990 | 639 | -88.8 | 504990 | 152 | -88.0 | 504990 | 713 | -101.5 | 504990 | 754 |
| MR_1774412393_CBF651D5 | 504990 | 639 | -89.2 | 504990 | 152 | -90.7 | 504990 | 713 | -101.5 | 504990 | 754 |
| MR_1774412393_A623C0CB | 504990 | 639 | -91.6 | 504990 | 152 | -89.2 | 504990 | 713 | -104.1 | 504990 | 754 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1575: `7b254636-496...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7b254636-4963-445a-91db-01a1ab929e69` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1575] topology](images/train_1575.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3237155_2
- `C2`: Decrease A3 Offset threshold for 3241362_4
- `C3`: Add neighbor relationship between 3231283_3 and 3237155_2
- `C4`: Press down the tilt angle of 3241362_4 by 2 degrees
- `C5`: Press down the tilt angle  of 3237155_2 by 10 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241362_4
- `C7`: Decrease transmission power for 3241362_4
- `C8`: Adjust the azimuth of 3237155_2 by 50 degrees
- `C9`: Increase A3 Offset threshold for 3237155_2
- `C10`: Lift the tilt angle  of 3237155_2 by 10 degrees
- `C11`: Check test server and transmission issues **← 정답**
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Lift the tilt angle of 3241362_4 by 2 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237155_2
- `C15`: Increase A3 Offset threshold for 3241362_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237155_2
- `C17`: Add neighbor relationship between 3241362_4 and 3237155_2
- `C18`: Increase transmission power for 3241362_4
- `C19`: Adjust the azimuth of 3241362_4 by 50 degrees
- `C20`: Increase transmission power for 3237155_2
- `C21`: Decrease transmission power for 3237155_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241362_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.154 | MS1 | 121.4656642366 | 31.1446262264 | 979 | 504990 | -89.27 | 15.45 | 530.22 | 0.05 | 2.27 | 1577 |
| 2024-09-20 22:21:32.227 | MS1 | 121.4656646018 | 31.1446351344 | 979 | 504990 | -86.60 | 13.79 | 349.83 | 0.09 | 2.41 | 1565 |
| 2024-09-20 22:21:33.466 | MS1 | 121.4656725285 | 31.1446288999 | 979 | 504990 | -86.56 | 13.35 | 532.70 | 0.07 | 2.55 | 1568 |
| 2024-09-20 22:21:34.174 | MS1 | 121.4656754547 | 31.1446312013 | 979 | 504990 | -91.75 | 17.42 | 79.17 | 0.12 | 2.65 | 484 |
| 2024-09-20 22:21:35.734 | MS1 | 121.4656653276 | 31.1446300762 | 979 | 504990 | -85.72 | 17.69 | 74.63 | 0.03 | 2.39 | 471 |
| 2024-09-20 22:21:36.899 | MS1 | 121.4656775512 | 31.1446315452 | 979 | 504990 | -88.51 | 15.11 | 77.89 | 0.09 | 2.98 | 494 |
| 2024-09-20 22:21:37.147 | MS1 | 121.4656747905 | 31.1446302361 | 979 | 504990 | -92.79 | 8.54 | 83.06 | 0.09 | 2.65 | 468 |
| 2024-09-20 22:21:38.980 | MS1 | 121.4656735167 | 31.1446280202 | 979 | 504990 | -92.53 | 9.12 | 96.19 | 0.16 | 2.02 | 434 |
| 2024-09-20 22:21:39.638 | MS1 | 121.4656771224 | 31.1446356669 | 979 | 504990 | -89.50 | 11.76 | 57.44 | 0.18 | 2.96 | 412 |
| 2024-09-20 22:21:40.435 | MS1 | 121.4656617622 | 31.1446281280 | 979 | 504990 | -90.15 | 9.81 | 321.34 | 0.18 | 2.74 | 1569 |
| 2024-09-20 22:21:41.549 | MS1 | 121.4656759549 | 31.1446332348 | 979 | 504990 | -89.76 | 11.83 | 607.14 | 0.10 | 2.02 | 1567 |
| 2024-09-20 22:21:42.149 | MS1 | 121.4656627897 | 31.1446345559 | 979 | 504990 | -92.97 | 8.41 | 386.84 | 0.12 | 2.20 | 1562 |

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
| 3231283 | 3 | 121.4750473113 | 31.1537710591 | 118 | 12 | 10 | 39.8 | TDD | 627 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3237155 | 2 | 121.4699237939 | 31.1514924153 | 14 | 13 | 12 | 45.6 | TDD | 242 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3241362 | 4 | 121.4654369756 | 31.1558937636 | 68 | 1 | 0 | 26.1 | TDD | 979 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3275704 | 1 | 121.4716365940 | 31.1510419376 | 193 | 1 | 6 | 34.2 | TDD | 1 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.008 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.031 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.164 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.164 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.894 | NREventA3 | measId:2;ServCellPCI:917;Se... |
| 2024-09-20 22:21:38.134 | NRHandoverAttempt | SourcePCI:917;SourceNR-ARFC... |
| 2024-09-20 22:21:38.181 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.191 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.339 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.339 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275704 | 1 | 9.3684 | 7.1884 | -115.1732 | 19.1624 | 145.4644 | 0.0161 | 0.0078 |
| 2024_09_20 22:00 | 3237155 | 2 | 13.3608 | 11.2010 | -115.2207 | 15.1070 | 107.2718 | 0.0059 | 0.0163 |
| 2024_09_20 22:00 | 3231283 | 3 | 9.1438 | 9.4017 | -117.0878 | 19.4103 | 144.4491 | 0.0058 | 0.0189 |
| 2024_09_20 22:00 | 3241362 | 4 | 15.0845 | 13.7144 | -117.2486 | 12.6748 | 166.8088 | 0.0066 | 0.0147 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415135_BB7C41EA | 504990 | 979 | -90.0 | 504990 | 242 | -93.4 | 504990 | 627 | -103.0 | 504990 | 1 |
| MR_1774415135_3B91E6CE | 504990 | 979 | -91.8 | 504990 | 242 | -93.4 | 504990 | 627 | -103.8 | 504990 | 1 |
| MR_1774415135_512C5DDD | 504990 | 979 | -92.3 | 504990 | 242 | -93.1 | 504990 | 627 | -102.2 | 504990 | 1 |
| MR_1774415135_C5052150 | 504990 | 979 | -93.2 | 504990 | 242 | -90.8 | 504990 | 627 | -102.4 | 504990 | 1 |
| MR_1774415135_0E2598D3 | 504990 | 979 | -92.2 | 504990 | 242 | -92.9 | 504990 | 627 | -103.8 | 504990 | 1 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1576: `868ec53a-73b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `868ec53a-73b4-4a3f-bb48-712ca5901f2e` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1576] topology](images/train_1576.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3258475_1
- `C2`: Press down the tilt angle  of 3258475_1 by 10 degrees
- `C3`: Lift the tilt angle of 3239432_3 by 2 degrees
- `C4`: Increase transmission power for 3258475_1
- `C5`: Press down the tilt angle of 3239432_3 by 2 degrees
- `C6`: Check test server and transmission issues **← 정답**
- `C7`: Lift the tilt angle  of 3258475_1 by 10 degrees
- `C8`: Add neighbor relationship between 3239432_3 and 3258475_1
- `C9`: Adjust the azimuth of 3239432_3 by 47 degrees
- `C10`: Decrease A3 Offset threshold for 3258475_1
- `C11`: Increase transmission power for 3239432_3
- `C12`: Increase A3 Offset threshold for 3258475_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258475_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239432_3
- `C16`: Add neighbor relationship between 3214104_4 and 3258475_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239432_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258475_1
- `C19`: Adjust the azimuth of 3258475_1 by 50 degrees
- `C20`: Increase A3 Offset threshold for 3239432_3
- `C21`: Decrease transmission power for 3239432_3
- `C22`: Decrease A3 Offset threshold for 3239432_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.769 | MS1 | 121.4656639402 | 31.1446354336 | 863 | 504990 | -87.70 | 16.99 | 564.17 | 0.17 | 2.67 | 1581 |
| 2024-09-20 22:21:32.940 | MS1 | 121.4656701522 | 31.1446270131 | 863 | 504990 | -86.11 | 12.00 | 433.61 | 0.08 | 2.48 | 1574 |
| 2024-09-20 22:21:33.898 | MS1 | 121.4656717198 | 31.1446236307 | 863 | 504990 | -87.33 | 15.19 | 544.86 | 0.03 | 2.37 | 1599 |
| 2024-09-20 22:21:34.472 | MS1 | 121.4656733429 | 31.1446369479 | 863 | 504990 | -91.06 | 17.80 | 49.91 | 0.05 | 2.03 | 332 |
| 2024-09-20 22:21:35.145 | MS1 | 121.4656669014 | 31.1446369867 | 863 | 504990 | -85.90 | 12.30 | 108.01 | 0.09 | 2.49 | 366 |
| 2024-09-20 22:21:36.541 | MS1 | 121.4656719387 | 31.1446185334 | 863 | 504990 | -88.81 | 15.84 | 76.87 | 0.12 | 2.41 | 476 |
| 2024-09-20 22:21:37.782 | MS1 | 121.4656588770 | 31.1446254914 | 863 | 504990 | -89.30 | 7.32 | 88.71 | 0.13 | 2.01 | 392 |
| 2024-09-20 22:21:38.309 | MS1 | 121.4656633264 | 31.1446324994 | 863 | 504990 | -91.15 | 12.66 | 79.74 | 0.20 | 2.45 | 342 |
| 2024-09-20 22:21:39.614 | MS1 | 121.4656720766 | 31.1446265897 | 863 | 504990 | -90.07 | 7.90 | 87.47 | 0.00 | 2.89 | 426 |
| 2024-09-20 22:21:40.175 | MS1 | 121.4656697993 | 31.1446321233 | 863 | 504990 | -89.14 | 9.78 | 306.34 | 0.19 | 2.32 | 1563 |
| 2024-09-20 22:21:41.282 | MS1 | 121.4656756458 | 31.1446201621 | 863 | 504990 | -90.12 | 10.22 | 503.22 | 0.04 | 2.93 | 1571 |
| 2024-09-20 22:21:42.880 | MS1 | 121.4656657392 | 31.1446286717 | 863 | 504990 | -91.30 | 12.16 | 405.72 | 0.08 | 2.14 | 1579 |

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
| 3214104 | 4 | 121.4710109618 | 31.1499458875 | 16 | 4 | 3 | 26.0 | TDD | 127 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3239432 | 3 | 121.4652362212 | 31.1538193225 | 131 | 0 | 5 | 41.1 | TDD | 863 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3254803 | 2 | 121.4758448041 | 31.1481804478 | 315 | 9 | 8 | 33.0 | TDD | 437 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3258475 | 1 | 121.4649611096 | 31.1450810101 | 310 | 11 | 5 | 18.9 | TDD | 658 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.327 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.345 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.449 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.449 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.178 | NREventA3 | measId:2;ServCellPCI:178;Se... |
| 2024-09-20 22:21:38.418 | NRHandoverAttempt | SourcePCI:178;SourceNR-ARFC... |
| 2024-09-20 22:21:38.452 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.462 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.592 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.592 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258475 | 1 | 10.5349 | 16.2631 | -115.8313 | 18.8954 | 198.1023 | 0.0032 | 0.0117 |
| 2024_09_20 22:00 | 3254803 | 2 | 11.1344 | 16.8834 | -114.5724 | 7.2228 | 199.8451 | 0.0023 | 0.0141 |
| 2024_09_20 22:00 | 3239432 | 3 | 8.0754 | 14.5951 | -115.7536 | 5.9810 | 194.3817 | 0.0093 | 0.0014 |
| 2024_09_20 22:00 | 3214104 | 4 | 15.9750 | 6.3661 | -117.8031 | 12.0695 | 174.6382 | 0.0160 | 0.0063 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414074_742EC34D | 504990 | 863 | -90.1 | 504990 | 658 | -97.0 | 504990 | 127 | -101.8 | 504990 | 437 |
| MR_1774414074_591E71F0 | 504990 | 863 | -91.9 | 504990 | 658 | -98.8 | 504990 | 127 | -101.9 | 504990 | 437 |
| MR_1774414074_0884FAFE | 504990 | 863 | -91.3 | 504990 | 658 | -99.3 | 504990 | 127 | -103.7 | 504990 | 437 |
| MR_1774414074_5C066433 | 504990 | 863 | -89.3 | 504990 | 658 | -100.0 | 504990 | 127 | -102.9 | 504990 | 437 |
| MR_1774414074_743BFA96 | 504990 | 863 | -90.8 | 504990 | 658 | -98.9 | 504990 | 127 | -101.1 | 504990 | 437 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1577: `51c56ab5-29c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `51c56ab5-29c6-4648-84af-52189ce617c9` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Decrease A3 Offset threshold for 3276627_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1577] topology](images/train_1577.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3243689_1
- `C2`: Decrease transmission power for 3243689_1
- `C3`: Add neighbor relationship between 3264261_3 and 3243689_1
- `C4`: Decrease A3 Offset threshold for 3276627_2 **← 정답**
- `C5`: Adjust the azimuth of 3243689_1 by 50 degrees
- `C6`: Decrease transmission power for 3276627_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Press down the tilt angle of 3276627_2 by 10 degrees
- `C9`: Increase A3 Offset threshold for 3243689_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276627_2
- `C11`: Increase A3 Offset threshold for 3276627_2
- `C12`: Increase transmission power for 3243689_1
- `C13`: Press down the tilt angle  of 3243689_1 by 4 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243689_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243689_1
- `C16`: Lift the tilt angle  of 3243689_1 by 4 degrees
- `C17`: Lift the tilt angle of 3276627_2 by 10 degrees
- `C18`: Add neighbor relationship between 3276627_2 and 3243689_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276627_2
- `C20`: Check test server and transmission issues
- `C21`: Increase transmission power for 3276627_2
- `C22`: Adjust the azimuth of 3276627_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.675 | MS1 | 121.4656763325 | 31.1446301534 | 587 | 504990 | -78.89 | 17.64 | 544.28 | 0.15 | 2.31 | 1560 |
| 2024-09-20 22:21:32.476 | MS1 | 121.4656634931 | 31.1446181624 | 587 | 504990 | -82.62 | 16.47 | 528.77 | 0.14 | 2.91 | 1567 |
| 2024-09-20 22:21:33.143 | MS1 | 121.4656650106 | 31.1446284694 | 587 | 504990 | -78.68 | 15.89 | 353.56 | 0.20 | 2.81 | 1590 |
| 2024-09-20 22:21:34.130 | MS1 | 121.4656724416 | 31.1446296780 | 587 | 504990 | -87.48 | -3.63 | 56.11 | 0.13 | 1.44 | 1561 |
| 2024-09-20 22:21:35.177 | MS1 | 121.4656592850 | 31.1446342815 | 587 | 504990 | -89.81 | -3.54 | 33.28 | 0.01 | 1.05 | 1597 |
| 2024-09-20 22:21:36.936 | MS1 | 121.4656586163 | 31.1446351120 | 587 | 504990 | -87.71 | -1.33 | 43.78 | 0.01 | 1.45 | 1595 |
| 2024-09-20 22:21:37.716 | MS1 | 121.4656769616 | 31.1446191600 | 587 | 504990 | -92.78 | -3.80 | 73.93 | 0.03 | 1.09 | 1598 |
| 2024-09-20 22:21:38.834 | MS1 | 121.4656617763 | 31.1446295786 | 587 | 504990 | -84.91 | -2.60 | 80.60 | 0.06 | 1.03 | 1597 |
| 2024-09-20 22:21:39.576 | MS1 | 121.4656642332 | 31.1446269641 | 193 | 504990 | -76.05 | 13.01 | 190.80 | 0.00 | 1.07 | 1571 |
| 2024-09-20 22:21:40.628 | MS1 | 121.4656731769 | 31.1446196678 | 193 | 504990 | -84.16 | 13.79 | 493.98 | 0.15 | 2.96 | 1560 |
| 2024-09-20 22:21:41.925 | MS1 | 121.4656775406 | 31.1446216728 | 193 | 504990 | -79.74 | 14.07 | 510.88 | 0.05 | 2.92 | 1570 |
| 2024-09-20 22:21:42.262 | MS1 | 121.4656728678 | 31.1446285818 | 193 | 504990 | -84.97 | 14.37 | 474.67 | 0.16 | 2.18 | 1589 |

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
| 3243689 | 1 | 121.4717770216 | 31.1515746140 | 85 | 2 | 1 | 25.8 | TDD | 193 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3264261 | 3 | 121.4734638447 | 31.1552391626 | 191 | 5 | 3 | 33.7 | TDD | 372 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3268468 | 4 | 121.4697259904 | 31.1448881943 | 220 | 11 | 11 | 22.0 | TDD | 756 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3276627 | 2 | 121.4758434807 | 31.1467558879 | 40 | 9 | 8 | 16.9 | TDD | 587 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.130 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.152 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.302 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.302 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.019 | NREventA3 | measId:2;ServCellPCI:355;Se... |
| 2024-09-20 22:21:38.259 | NRHandoverAttempt | SourcePCI:355;SourceNR-ARFC... |
| 2024-09-20 22:21:38.293 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.307 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.455 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.455 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243689 | 1 | 12.5569 | 12.9137 | -116.7056 | 9.1452 | 149.2044 | 0.0040 | 0.0086 |
| 2024_09_20 22:00 | 3276627 | 2 | 11.1306 | 16.9230 | -117.4165 | 17.1866 | 188.9397 | 0.0164 | 0.1504 |
| 2024_09_20 22:00 | 3264261 | 3 | 15.7915 | 5.3596 | -114.8976 | 19.3663 | 163.7980 | 0.0055 | 0.0033 |
| 2024_09_20 22:00 | 3268468 | 4 | 16.0660 | 8.1088 | -114.2146 | 11.1022 | 86.0167 | 0.0041 | 0.0154 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414389_9432748C | 504990 | 587 | -86.2 | 504990 | 193 | -79.3 | 504990 | 372 | -81.3 | 504990 | 756 |
| MR_1774414389_8DD5378A | 504990 | 587 | -89.1 | 504990 | 193 | -79.9 | 504990 | 372 | -80.5 | 504990 | 756 |
| MR_1774414389_6B92AA56 | 504990 | 587 | -88.6 | 504990 | 193 | -79.7 | 504990 | 372 | -80.6 | 504990 | 756 |
| MR_1774414389_7EDE3E8E | 504990 | 587 | -87.5 | 504990 | 193 | -79.2 | 504990 | 372 | -83.7 | 504990 | 756 |
| MR_1774414389_9B189309 | 504990 | 587 | -88.4 | 504990 | 193 | -79.4 | 504990 | 372 | -80.2 | 504990 | 756 |
| MR_1774414389_57D994DE | 504990 | 193 | -79.8 | 504990 | 587 | -87.5 | 504990 | 372 | -80.3 | 504990 | 756 |
| MR_1774414389_64D9045E | 504990 | 193 | -78.4 | 504990 | 587 | -88.0 | 504990 | 372 | -80.5 | 504990 | 756 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1578: `f2d473a1-010...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f2d473a1-0103-4937-9596-8113c26f4029` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3213766_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1578] topology](images/train_1578.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3215380_2 and 3223041_1
- `C2`: Check test server and transmission issues
- `C3`: Add neighbor relationship between 3213766_3 and 3223041_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223041_1
- `C5`: Press down the tilt angle  of 3223041_1 by 10 degrees
- `C6`: Increase A3 Offset threshold for 3213766_3
- `C7`: Decrease A3 Offset threshold for 3223041_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Adjust the azimuth of 3213766_3 by 47 degrees
- `C10`: Increase transmission power for 3213766_3
- `C11`: Press down the tilt angle of 3213766_3 by 2 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223041_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213766_3
- `C14`: Decrease transmission power for 3223041_1
- `C15`: Increase transmission power for 3223041_1
- `C16`: Lift the tilt angle  of 3223041_1 by 10 degrees
- `C17`: Lift the tilt angle of 3213766_3 by 2 degrees
- `C18`: Increase A3 Offset threshold for 3223041_1
- `C19`: Decrease A3 Offset threshold for 3213766_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213766_3 **← 정답**
- `C21`: Adjust the azimuth of 3223041_1 by 50 degrees
- `C22`: Decrease transmission power for 3213766_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.944 | MS1 | 121.4656682598 | 31.1446334586 | 315 | 504990 | -91.87 | 17.69 | 347.01 | 0.14 | 2.92 | 1587 |
| 2024-09-20 22:21:32.493 | MS1 | 121.4656658129 | 31.1446289261 | 315 | 504990 | -87.97 | 15.36 | 417.37 | 0.01 | 2.40 | 1573 |
| 2024-09-20 22:21:33.763 | MS1 | 121.4656703839 | 31.1446271558 | 315 | 504990 | -90.56 | 17.66 | 356.50 | 0.18 | 2.45 | 1595 |
| 2024-09-20 22:21:34.678 | MS1 | 121.4656752285 | 31.1446253886 | 315 | 504990 | -88.57 | 12.53 | 87.64 | 0.53 | 2.01 | 656 |
| 2024-09-20 22:21:35.766 | MS1 | 121.4656584785 | 31.1446288077 | 315 | 504990 | -88.84 | 13.89 | 71.28 | 0.67 | 2.65 | 519 |
| 2024-09-20 22:21:36.595 | MS1 | 121.4656710519 | 31.1446366455 | 315 | 504990 | -91.17 | 12.98 | 62.43 | 0.56 | 2.90 | 532 |
| 2024-09-20 22:21:37.117 | MS1 | 121.4656743323 | 31.1446182807 | 315 | 504990 | -91.92 | 9.37 | 51.66 | 0.57 | 2.10 | 665 |
| 2024-09-20 22:21:38.465 | MS1 | 121.4656742501 | 31.1446379945 | 315 | 504990 | -93.96 | 9.24 | 66.62 | 0.65 | 2.68 | 562 |
| 2024-09-20 22:21:39.392 | MS1 | 121.4656667568 | 31.1446220704 | 315 | 504990 | -90.82 | 9.17 | 82.76 | 0.54 | 2.63 | 647 |
| 2024-09-20 22:21:40.694 | MS1 | 121.4656660190 | 31.1446298967 | 315 | 504990 | -92.30 | 12.19 | 449.91 | 0.01 | 2.48 | 1568 |
| 2024-09-20 22:21:41.554 | MS1 | 121.4656742714 | 31.1446212510 | 315 | 504990 | -90.58 | 8.04 | 409.77 | 0.12 | 2.47 | 1593 |
| 2024-09-20 22:21:42.919 | MS1 | 121.4656691043 | 31.1446230217 | 315 | 504990 | -90.61 | 12.41 | 444.21 | 0.20 | 2.79 | 1571 |

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
| 3213766 | 3 | 121.4688597608 | 31.1544245564 | 243 | 0 | 7 | 33.3 | TDD | 315 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3215380 | 2 | 121.4666830126 | 31.1550744257 | 285 | 7 | 10 | 26.3 | TDD | 784 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3223041 | 1 | 121.4694769395 | 31.1452037153 | 85 | 7 | 8 | 26.4 | TDD | 776 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3275900 | 4 | 121.4697317815 | 31.1511269992 | 315 | 13 | 1 | 41.5 | TDD | 889 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.324 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.347 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.496 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.496 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.197 | NREventA3 | measId:2;ServCellPCI:463;Se... |
| 2024-09-20 22:21:38.437 | NRHandoverAttempt | SourcePCI:463;SourceNR-ARFC... |
| 2024-09-20 22:21:38.478 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.488 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.614 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.614 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223041 | 1 | 17.8485 | 15.8480 | -117.0973 | 6.1067 | 165.2390 | 0.0007 | 0.0060 |
| 2024_09_20 22:00 | 3215380 | 2 | 5.8608 | 12.6330 | -114.2661 | 13.3176 | 177.5314 | 0.0045 | 0.0083 |
| 2024_09_20 22:00 | 3213766 | 3 | 5.5101 | 12.1605 | -115.9147 | 16.1281 | 130.7838 | 0.0159 | 0.0051 |
| 2024_09_20 22:00 | 3275900 | 4 | 16.9026 | 12.7686 | -115.6703 | 13.5728 | 163.4841 | 0.0147 | 0.0128 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415262_B4784DA4 | 504990 | 315 | -87.4 | 504990 | 776 | -88.6 | 504990 | 784 | -100.4 | 504990 | 889 |
| MR_1774415262_2702F7B8 | 504990 | 315 | -87.1 | 504990 | 776 | -88.0 | 504990 | 784 | -100.8 | 504990 | 889 |
| MR_1774415262_DC8FD225 | 504990 | 315 | -88.9 | 504990 | 776 | -87.4 | 504990 | 784 | -102.2 | 504990 | 889 |
| MR_1774415262_A32FE536 | 504990 | 315 | -89.1 | 504990 | 776 | -89.3 | 504990 | 784 | -103.9 | 504990 | 889 |
| MR_1774415262_45087110 | 504990 | 315 | -88.6 | 504990 | 776 | -88.1 | 504990 | 784 | -101.4 | 504990 | 889 |
| MR_1774415262_9E6CFDC3 | 504990 | 315 | -87.8 | 504990 | 776 | -87.2 | 504990 | 784 | -100.9 | 504990 | 889 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1579: `47eec279-fbc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `47eec279-fbc4-415f-9b07-382ec665f93b` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1579] topology](images/train_1579.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3212803_4 by 10 degrees
- `C2`: Check test server and transmission issues **← 정답**
- `C3`: Press down the tilt angle  of 3255118_1 by 10 degrees
- `C4`: Increase transmission power for 3255118_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255118_1
- `C6`: Add neighbor relationship between 3212803_4 and 3255118_1
- `C7`: Decrease A3 Offset threshold for 3212803_4
- `C8`: Decrease A3 Offset threshold for 3255118_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212803_4
- `C10`: Lift the tilt angle  of 3255118_1 by 10 degrees
- `C11`: Decrease transmission power for 3255118_1
- `C12`: Press down the tilt angle of 3212803_4 by 10 degrees
- `C13`: Increase A3 Offset threshold for 3212803_4
- `C14`: Add neighbor relationship between 3258984_3 and 3255118_1
- `C15`: Adjust the azimuth of 3255118_1 by 50 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase A3 Offset threshold for 3255118_1
- `C18`: Increase transmission power for 3212803_4
- `C19`: Adjust the azimuth of 3212803_4 by 31 degrees
- `C20`: Decrease transmission power for 3212803_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212803_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255118_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.599 | MS1 | 121.4656646265 | 31.1446181197 | 711 | 504990 | -89.03 | 13.05 | 550.54 | 0.19 | 2.58 | 1565 |
| 2024-09-20 22:21:32.847 | MS1 | 121.4656608016 | 31.1446303957 | 711 | 504990 | -90.98 | 16.31 | 441.98 | 0.14 | 2.87 | 1581 |
| 2024-09-20 22:21:33.931 | MS1 | 121.4656666353 | 31.1446261280 | 711 | 504990 | -88.20 | 12.86 | 425.10 | 0.12 | 2.27 | 1597 |
| 2024-09-20 22:21:34.416 | MS1 | 121.4656713150 | 31.1446300836 | 711 | 504990 | -91.96 | 17.19 | 74.80 | 0.04 | 2.31 | 388 |
| 2024-09-20 22:21:35.934 | MS1 | 121.4656773009 | 31.1446234085 | 711 | 504990 | -85.32 | 14.51 | 62.51 | 0.00 | 2.90 | 306 |
| 2024-09-20 22:21:36.538 | MS1 | 121.4656615252 | 31.1446324641 | 711 | 504990 | -88.03 | 15.42 | 83.99 | 0.13 | 2.83 | 420 |
| 2024-09-20 22:21:37.791 | MS1 | 121.4656715687 | 31.1446267311 | 711 | 504990 | -91.97 | 7.66 | 53.93 | 0.04 | 2.86 | 378 |
| 2024-09-20 22:21:38.132 | MS1 | 121.4656722877 | 31.1446239725 | 711 | 504990 | -93.95 | 12.78 | 51.29 | 0.10 | 2.60 | 484 |
| 2024-09-20 22:21:39.955 | MS1 | 121.4656688401 | 31.1446371213 | 711 | 504990 | -92.02 | 10.32 | 48.71 | 0.10 | 2.06 | 495 |
| 2024-09-20 22:21:40.803 | MS1 | 121.4656634377 | 31.1446280829 | 711 | 504990 | -92.29 | 12.93 | 510.76 | 0.00 | 2.02 | 1600 |
| 2024-09-20 22:21:41.146 | MS1 | 121.4656636217 | 31.1446263752 | 711 | 504990 | -89.14 | 11.91 | 422.74 | 0.03 | 2.79 | 1568 |
| 2024-09-20 22:21:42.152 | MS1 | 121.4656593274 | 31.1446245048 | 711 | 504990 | -91.01 | 9.45 | 398.72 | 0.04 | 2.21 | 1566 |

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
| 3212803 | 4 | 121.4641585615 | 31.1493492769 | 134 | 10 | 7 | 35.0 | TDD | 711 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3255118 | 1 | 121.4717771767 | 31.1483364742 | 285 | 7 | 5 | 35.4 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3258984 | 3 | 121.4726948283 | 31.1463720811 | 94 | 8 | 3 | 32.7 | TDD | 93 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3268590 | 2 | 121.4666086581 | 31.1494185159 | 344 | 14 | 4 | 37.2 | TDD | 362 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.585 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.602 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.712 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.712 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.391 | NREventA3 | measId:2;ServCellPCI:418;Se... |
| 2024-09-20 22:21:38.631 | NRHandoverAttempt | SourcePCI:418;SourceNR-ARFC... |
| 2024-09-20 22:21:38.676 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.688 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.789 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.789 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255118 | 1 | 16.9191 | 11.8493 | -114.3471 | 17.9875 | 140.8032 | 0.0013 | 0.0162 |
| 2024_09_20 22:00 | 3268590 | 2 | 11.8827 | 14.7686 | -117.0938 | 10.4100 | 80.4918 | 0.0075 | 0.0052 |
| 2024_09_20 22:00 | 3258984 | 3 | 12.8144 | 13.7357 | -116.6534 | 10.8527 | 90.8320 | 0.0078 | 0.0129 |
| 2024_09_20 22:00 | 3212803 | 4 | 19.6509 | 8.0734 | -114.5657 | 18.9947 | 172.1414 | 0.0141 | 0.0187 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414401_7E638E32 | 504990 | 711 | -91.5 | 504990 | 129 | -91.0 | 504990 | 93 | -103.2 | 504990 | 362 |
| MR_1774414401_4A2C725A | 504990 | 711 | -91.2 | 504990 | 129 | -92.0 | 504990 | 93 | -101.0 | 504990 | 362 |
| MR_1774414401_B83DB3AD | 504990 | 711 | -91.5 | 504990 | 129 | -93.1 | 504990 | 93 | -102.6 | 504990 | 362 |
| MR_1774414401_1A363687 | 504990 | 711 | -93.6 | 504990 | 129 | -93.1 | 504990 | 93 | -101.5 | 504990 | 362 |
| MR_1774414401_1E862BCC | 504990 | 711 | -92.8 | 504990 | 129 | -92.6 | 504990 | 93 | -102.8 | 504990 | 362 |
| MR_1774414401_A95D8A82 | 504990 | 711 | -90.1 | 504990 | 129 | -94.6 | 504990 | 93 | -103.5 | 504990 | 362 |
| MR_1774414401_496C437F | 504990 | 711 | -93.9 | 504990 | 129 | -91.4 | 504990 | 93 | -101.6 | 504990 | 362 |

> *... 2개 열 생략 (전체 14열)*

---
