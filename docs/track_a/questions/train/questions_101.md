# Track A 문제 분석 — train[1000]~train[1009]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1000] ~ train[1009] (10개)

## 목차

1. [문제 1000: `33f119da-794...`](#1000) — single-answer, 정답: C17
2. [문제 1001: `b754623b-626...`](#1001) — single-answer, 정답: C9
3. [문제 1002: `9957ae44-d20...`](#1002) — single-answer, 정답: C17
4. [문제 1003: `27c0cd07-2f0...`](#1003) — single-answer, 정답: C9
5. [문제 1004: `a0da0f22-dbf...`](#1004) — single-answer, 정답: C16
6. [문제 1005: `5960ce5b-c2c...`](#1005) — single-answer, 정답: C8
7. [문제 1006: `76ca4839-ae5...`](#1006) — multiple-answer, 정답: C1|C8|C10|C17
8. [문제 1007: `8a1a57d5-774...`](#1007) — multiple-answer, 정답: C3|C20
9. [문제 1008: `b8c1026a-703...`](#1008) — single-answer, 정답: C22
10. [문제 1009: `4476c282-156...`](#1009) — single-answer, 정답: C3

---

### 문제 1000: `33f119da-794...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `33f119da-7948-479a-abcf-f76c650b20db` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1000] topology](images/train_1000.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3225611_4 by 10 degrees
- `C2`: Add neighbor relationship between 3225611_4 and 3222735_2
- `C3`: Increase transmission power for 3225611_4
- `C4`: Adjust the azimuth of 3225611_4 by 42 degrees
- `C5`: Adjust the azimuth of 3222735_2 by 50 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222735_2
- `C7`: Increase A3 Offset threshold for 3225611_4
- `C8`: Decrease transmission power for 3222735_2
- `C9`: Decrease transmission power for 3225611_4
- `C10`: Lift the tilt angle  of 3222735_2 by 6 degrees
- `C11`: Press down the tilt angle  of 3222735_2 by 6 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222735_2
- `C14`: Decrease A3 Offset threshold for 3225611_4
- `C15`: Press down the tilt angle of 3225611_4 by 10 degrees
- `C16`: Add neighbor relationship between 3211196_1 and 3222735_2
- `C17`: Check test server and transmission issues **← 정답**
- `C18`: Increase transmission power for 3222735_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225611_4
- `C20`: Decrease A3 Offset threshold for 3222735_2
- `C21`: Increase A3 Offset threshold for 3222735_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225611_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.391 | MS1 | 121.4656635921 | 31.1446347863 | 103 | 504990 | -91.38 | 16.63 | 422.32 | 0.01 | 2.28 | 1565 |
| 2024-09-20 22:21:32.170 | MS1 | 121.4656645845 | 31.1446218048 | 103 | 504990 | -91.98 | 12.63 | 364.65 | 0.14 | 2.89 | 1567 |
| 2024-09-20 22:21:33.778 | MS1 | 121.4656620051 | 31.1446357539 | 103 | 504990 | -88.96 | 12.62 | 505.36 | 0.07 | 2.86 | 1589 |
| 2024-09-20 22:21:34.960 | MS1 | 121.4656721477 | 31.1446369756 | 103 | 504990 | -91.83 | 13.35 | 58.89 | 0.01 | 2.04 | 345 |
| 2024-09-20 22:21:35.149 | MS1 | 121.4656676868 | 31.1446206966 | 103 | 504990 | -89.55 | 13.92 | 61.62 | 0.05 | 2.26 | 405 |
| 2024-09-20 22:21:36.655 | MS1 | 121.4656718832 | 31.1446276855 | 103 | 504990 | -88.46 | 15.04 | 62.11 | 0.02 | 2.07 | 319 |
| 2024-09-20 22:21:37.631 | MS1 | 121.4656647052 | 31.1446247373 | 103 | 504990 | -91.48 | 10.23 | 84.54 | 0.11 | 2.32 | 361 |
| 2024-09-20 22:21:38.180 | MS1 | 121.4656750606 | 31.1446364524 | 103 | 504990 | -93.20 | 7.75 | 71.78 | 0.08 | 2.95 | 342 |
| 2024-09-20 22:21:39.535 | MS1 | 121.4656685807 | 31.1446350947 | 103 | 504990 | -93.59 | 11.65 | 85.49 | 0.17 | 2.34 | 392 |
| 2024-09-20 22:21:40.111 | MS1 | 121.4656645811 | 31.1446279977 | 103 | 504990 | -89.22 | 9.94 | 469.68 | 0.07 | 2.30 | 1594 |
| 2024-09-20 22:21:41.997 | MS1 | 121.4656661258 | 31.1446199624 | 103 | 504990 | -89.94 | 11.95 | 430.17 | 0.14 | 2.90 | 1598 |
| 2024-09-20 22:21:42.386 | MS1 | 121.4656775929 | 31.1446256536 | 103 | 504990 | -89.36 | 12.97 | 515.48 | 0.06 | 2.00 | 1591 |

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
| 3211196 | 1 | 121.4741233519 | 31.1472868948 | 12 | 8 | 1 | 44.7 | TDD | 577 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3222735 | 2 | 121.4701476843 | 31.1550659879 | 258 | 4 | 11 | 44.4 | TDD | 212 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3225611 | 4 | 121.4719388690 | 31.1466120527 | 208 | 6 | 5 | 47.5 | TDD | 103 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3270484 | 3 | 121.4749815911 | 31.1446201562 | 49 | 4 | 6 | 19.7 | TDD | 252 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.028 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.133 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.133 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.835 | NREventA3 | measId:2;ServCellPCI:457;Se... |
| 2024-09-20 22:21:38.075 | NRHandoverAttempt | SourcePCI:457;SourceNR-ARFC... |
| 2024-09-20 22:21:38.115 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.129 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.264 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.264 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211196 | 1 | 19.3510 | 14.2382 | -117.8375 | 5.1895 | 102.1478 | 0.0010 | 0.0055 |
| 2024_09_20 22:00 | 3222735 | 2 | 17.1465 | 17.9255 | -115.7744 | 8.3266 | 192.8286 | 0.0193 | 0.0068 |
| 2024_09_20 22:00 | 3270484 | 3 | 14.3859 | 5.3958 | -117.2714 | 17.1188 | 161.6484 | 0.0126 | 0.0169 |
| 2024_09_20 22:00 | 3225611 | 4 | 12.8773 | 18.6206 | -115.3755 | 10.6120 | 125.5181 | 0.0179 | 0.0165 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412613_6B1E0E27 | 504990 | 103 | -92.2 | 504990 | 212 | -99.4 | 504990 | 577 | -101.4 | 504990 | 252 |
| MR_1774412613_6FD2925B | 504990 | 103 | -91.2 | 504990 | 212 | -101.4 | 504990 | 577 | -101.9 | 504990 | 252 |
| MR_1774412613_09DF4DD8 | 504990 | 103 | -91.7 | 504990 | 212 | -100.0 | 504990 | 577 | -101.1 | 504990 | 252 |
| MR_1774412613_267300F9 | 504990 | 103 | -92.0 | 504990 | 212 | -98.7 | 504990 | 577 | -102.6 | 504990 | 252 |
| MR_1774412613_78A94084 | 504990 | 103 | -93.2 | 504990 | 212 | -99.6 | 504990 | 577 | -102.4 | 504990 | 252 |
| MR_1774412613_74CEC910 | 504990 | 103 | -92.0 | 504990 | 212 | -101.2 | 504990 | 577 | -99.6 | 504990 | 252 |
| MR_1774412613_28F541A5 | 504990 | 103 | -91.8 | 504990 | 212 | -98.3 | 504990 | 577 | -101.9 | 504990 | 252 |
| MR_1774412613_504BE6E1 | 504990 | 103 | -90.7 | 504990 | 212 | -99.0 | 504990 | 577 | -103.4 | 504990 | 252 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1001: `b754623b-626...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b754623b-626e-493e-b14f-e3354952d29e` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease A3 Offset threshold for 3258795_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1001] topology](images/train_1001.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3228237_2 by 6 degrees
- `C2`: Lift the tilt angle of 3258795_1 by 10 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258795_1
- `C5`: Increase transmission power for 3228237_2
- `C6`: Check test server and transmission issues
- `C7`: Adjust the azimuth of 3228237_2 by 50 degrees
- `C8`: Decrease A3 Offset threshold for 3228237_2
- `C9`: Decrease A3 Offset threshold for 3258795_1 **← 정답**
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258795_1
- `C11`: Adjust the azimuth of 3258795_1 by 50 degrees
- `C12`: Add neighbor relationship between 3258795_1 and 3228237_2
- `C13`: Decrease transmission power for 3228237_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228237_2
- `C15`: Increase A3 Offset threshold for 3258795_1
- `C16`: Press down the tilt angle  of 3228237_2 by 6 degrees
- `C17`: Decrease transmission power for 3258795_1
- `C18`: Add neighbor relationship between 3251887_4 and 3228237_2
- `C19`: Increase transmission power for 3258795_1
- `C20`: Press down the tilt angle of 3258795_1 by 10 degrees
- `C21`: Increase A3 Offset threshold for 3228237_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228237_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.361 | MS1 | 121.4656663440 | 31.1446308198 | 314 | 504990 | -76.99 | 15.20 | 392.54 | 0.08 | 2.76 | 1591 |
| 2024-09-20 22:21:32.697 | MS1 | 121.4656743249 | 31.1446209220 | 314 | 504990 | -77.20 | 16.57 | 520.45 | 0.01 | 2.23 | 1584 |
| 2024-09-20 22:21:33.162 | MS1 | 121.4656662507 | 31.1446283007 | 314 | 504990 | -81.20 | 16.89 | 602.49 | 0.06 | 2.13 | 1586 |
| 2024-09-20 22:21:34.755 | MS1 | 121.4656690892 | 31.1446209018 | 314 | 504990 | -87.60 | -3.62 | 40.35 | 0.07 | 1.15 | 1585 |
| 2024-09-20 22:21:35.600 | MS1 | 121.4656601689 | 31.1446281979 | 314 | 504990 | -87.04 | -1.54 | 61.87 | 0.01 | 1.30 | 1583 |
| 2024-09-20 22:21:36.941 | MS1 | 121.4656716061 | 31.1446195196 | 314 | 504990 | -89.26 | -0.49 | 49.90 | 0.07 | 1.49 | 1569 |
| 2024-09-20 22:21:37.827 | MS1 | 121.4656705123 | 31.1446337412 | 314 | 504990 | -85.91 | -0.76 | 41.63 | 0.17 | 1.14 | 1596 |
| 2024-09-20 22:21:38.775 | MS1 | 121.4656618780 | 31.1446345474 | 314 | 504990 | -84.63 | -3.95 | 62.62 | 0.17 | 1.04 | 1577 |
| 2024-09-20 22:21:39.284 | MS1 | 121.4656605466 | 31.1446194434 | 484 | 504990 | -84.06 | 17.83 | 183.64 | 0.05 | 1.18 | 1561 |
| 2024-09-20 22:21:40.269 | MS1 | 121.4656621472 | 31.1446227021 | 484 | 504990 | -78.53 | 13.00 | 334.82 | 0.03 | 2.91 | 1585 |
| 2024-09-20 22:21:41.663 | MS1 | 121.4656673433 | 31.1446340843 | 484 | 504990 | -75.09 | 15.18 | 320.52 | 0.07 | 2.26 | 1572 |
| 2024-09-20 22:21:42.582 | MS1 | 121.4656667971 | 31.1446333388 | 484 | 504990 | -80.80 | 17.85 | 321.45 | 0.14 | 2.88 | 1576 |

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
| 3228237 | 2 | 121.4723409694 | 31.1555138485 | 75 | 5 | 2 | 34.9 | TDD | 484 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3230605 | 3 | 121.4751563349 | 31.1443771225 | 34 | 6 | 4 | 35.5 | TDD | 470 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3251887 | 4 | 121.4710156062 | 31.1465111117 | 269 | 10 | 12 | 41.9 | TDD | 534 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3258795 | 1 | 121.4722836823 | 31.1456852423 | 30 | 11 | 0 | 43.6 | TDD | 314 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.563 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.585 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.716 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.716 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.413 | NREventA3 | measId:2;ServCellPCI:10;Ser... |
| 2024-09-20 22:21:38.653 | NRHandoverAttempt | SourcePCI:10;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.685 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.697 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.817 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.817 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258795 | 1 | 8.3287 | 9.0406 | -116.2362 | 10.2554 | 132.0899 | 0.0038 | 0.1818 |
| 2024_09_20 22:00 | 3228237 | 2 | 9.9916 | 10.6791 | -115.8132 | 5.9132 | 196.5135 | 0.0124 | 0.0037 |
| 2024_09_20 22:00 | 3230605 | 3 | 13.4036 | 13.7128 | -114.6805 | 14.4267 | 94.7834 | 0.0158 | 0.0124 |
| 2024_09_20 22:00 | 3251887 | 4 | 19.2288 | 12.2132 | -117.0616 | 10.0692 | 168.8073 | 0.0051 | 0.0171 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413717_C249C5AA | 504990 | 484 | -83.5 | 504990 | 314 | -87.0 | 504990 | 534 | -89.5 | 504990 | 470 |
| MR_1774413717_85E8E2AA | 504990 | 484 | -83.3 | 504990 | 314 | -88.9 | 504990 | 534 | -87.9 | 504990 | 470 |
| MR_1774413717_20598411 | 504990 | 314 | -87.1 | 504990 | 484 | -82.5 | 504990 | 534 | -86.7 | 504990 | 470 |
| MR_1774413717_D942181F | 504990 | 484 | -81.8 | 504990 | 314 | -87.2 | 504990 | 534 | -88.6 | 504990 | 470 |
| MR_1774413717_F4344C7B | 504990 | 314 | -87.2 | 504990 | 484 | -83.1 | 504990 | 534 | -87.2 | 504990 | 470 |
| MR_1774413717_2FA5E64F | 504990 | 484 | -84.7 | 504990 | 314 | -88.8 | 504990 | 534 | -90.4 | 504990 | 470 |
| MR_1774413717_7C4FA2A9 | 504990 | 484 | -83.4 | 504990 | 314 | -87.8 | 504990 | 534 | -87.2 | 504990 | 470 |
| MR_1774413717_DAEB2681 | 504990 | 484 | -82.6 | 504990 | 314 | -86.0 | 504990 | 534 | -87.0 | 504990 | 470 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1002: `9957ae44-d20...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9957ae44-d206-45da-b1ca-e99560ab1f7e` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1002] topology](images/train_1002.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3221405_2
- `C2`: Increase transmission power for 3265491_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221405_2
- `C4`: Press down the tilt angle  of 3265491_1 by 10 degrees
- `C5`: Add neighbor relationship between 3221405_2 and 3265491_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265491_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221405_2
- `C8`: Decrease A3 Offset threshold for 3221405_2
- `C9`: Adjust the azimuth of 3265491_1 by 50 degrees
- `C10`: Lift the tilt angle of 3221405_2 by 1 degrees
- `C11`: Add neighbor relationship between 3232180_3 and 3265491_1
- `C12`: Adjust the azimuth of 3221405_2 by 50 degrees
- `C13`: Lift the tilt angle  of 3265491_1 by 10 degrees
- `C14`: Check test server and transmission issues
- `C15`: Decrease A3 Offset threshold for 3265491_1
- `C16`: Increase A3 Offset threshold for 3221405_2
- `C17`: Insufficient data; more data is needed for judgment. **← 정답**
- `C18`: Increase A3 Offset threshold for 3265491_1
- `C19`: Decrease transmission power for 3265491_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265491_1
- `C21`: Press down the tilt angle of 3221405_2 by 1 degrees
- `C22`: Increase transmission power for 3221405_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.400 | MS1 | 121.4656655035 | 31.1446360339 | 233 | 504990 | -91.93 | 14.09 | 340.17 | 0.06 | 2.62 | 1598 |
| 2024-09-20 22:21:32.514 | MS1 | 121.4656683407 | 31.1446281980 | 233 | 504990 | -85.23 | 17.17 | 575.34 | 0.01 | 2.49 | 1598 |
| 2024-09-20 22:21:33.844 | MS1 | 121.4656752828 | 31.1446337499 | 233 | 504990 | -85.77 | 15.14 | 483.23 | 0.12 | 2.52 | 1569 |
| 2024-09-20 22:21:34.744 | MS1 | 121.4656610572 | 31.1446248266 | 233 | 504990 | -85.11 | 17.59 | 89.26 | 0.04 | 2.21 | 1589 |
| 2024-09-20 22:21:35.353 | MS1 | 121.4656770318 | 31.1446282227 | 233 | 504990 | -91.50 | 15.28 | 92.92 | 0.00 | 2.94 | 1582 |
| 2024-09-20 22:21:36.349 | MS1 | 121.4656748505 | 31.1446326495 | 233 | 504990 | -91.34 | 15.68 | 69.52 | 0.12 | 2.69 | 1584 |
| 2024-09-20 22:21:37.438 | MS1 | 121.4656711669 | 31.1446315646 | 233 | 504990 | -91.80 | 12.94 | 91.34 | 0.15 | 2.93 | 1596 |
| 2024-09-20 22:21:38.619 | MS1 | 121.4656778264 | 31.1446274829 | 233 | 504990 | -93.30 | 7.54 | 64.22 | 0.04 | 2.46 | 1589 |
| 2024-09-20 22:21:39.561 | MS1 | 121.4656659047 | 31.1446196119 | 233 | 504990 | -91.98 | 10.22 | 86.52 | 0.09 | 2.11 | 1578 |
| 2024-09-20 22:21:40.538 | MS1 | 121.4656729515 | 31.1446241733 | 233 | 504990 | -92.28 | 8.56 | 320.82 | 0.19 | 2.97 | 1582 |
| 2024-09-20 22:21:41.646 | MS1 | 121.4656715528 | 31.1446294748 | 233 | 504990 | -93.76 | 9.76 | 398.45 | 0.17 | 2.94 | 1566 |
| 2024-09-20 22:21:42.270 | MS1 | 121.4656638706 | 31.1446277134 | 233 | 504990 | -93.72 | 9.28 | 482.77 | 0.15 | 2.42 | 1598 |

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
| 3221405 | 2 | 121.4691170912 | 31.1533956730 | 16 | 0 | 8 | 15.6 | TDD | 233 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3232180 | 3 | 121.4725789005 | 31.1523371728 | 106 | 11 | 2 | 39.9 | TDD | 805 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3241731 | 4 | 121.4666077308 | 31.1512561451 | 279 | 11 | 6 | 43.0 | TDD | 70 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3265491 | 1 | 121.4726635434 | 31.1493984682 | 40 | 14 | 11 | 43.5 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.850 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.865 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.971 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.971 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.698 | NREventA3 | measId:2;ServCellPCI:180;Se... |
| 2024-09-20 22:21:37.938 | NRHandoverAttempt | SourcePCI:180;SourceNR-ARFC... |
| 2024-09-20 22:21:37.982 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.996 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.116 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.116 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3265491 | 1 | 82.5151 | 91.5390 | -115.4482 | 14.6850 | 151.7271 | 0.0075 | 0.0098 |
| 2024_09_19 22:00 | 3221405 | 2 | 86.1870 | 77.5274 | -114.4360 | 18.7134 | 117.9696 | 0.0055 | 0.0139 |
| 2024_09_19 22:00 | 3232180 | 3 | 77.0462 | 91.1702 | -116.6797 | 16.2096 | 186.7956 | 0.0062 | 0.0104 |
| 2024_09_19 22:00 | 3241731 | 4 | 78.6263 | 80.6770 | -115.3770 | 8.5796 | 156.3589 | 0.0143 | 0.0017 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414605_413A4C9F | 504990 | 233 | -84.1 | 504990 | 176 | -83.7 | 504990 | 805 | -100.4 | 504990 | 70 |
| MR_1774414605_1229104F | 504990 | 233 | -85.4 | 504990 | 176 | -83.9 | 504990 | 805 | -100.7 | 504990 | 70 |
| MR_1774414605_D828DD3E | 504990 | 233 | -83.5 | 504990 | 176 | -83.5 | 504990 | 805 | -98.2 | 504990 | 70 |
| MR_1774414605_2DAC28FB | 504990 | 233 | -83.3 | 504990 | 176 | -83.9 | 504990 | 805 | -99.6 | 504990 | 70 |
| MR_1774414605_99D659D7 | 504990 | 233 | -84.8 | 504990 | 176 | -86.3 | 504990 | 805 | -98.4 | 504990 | 70 |
| MR_1774414605_0E807C08 | 504990 | 233 | -83.3 | 504990 | 176 | -83.0 | 504990 | 805 | -97.5 | 504990 | 70 |
| MR_1774414605_FEE58B25 | 504990 | 233 | -85.4 | 504990 | 176 | -84.9 | 504990 | 805 | -100.7 | 504990 | 70 |
| MR_1774414605_9A057617 | 504990 | 233 | -85.3 | 504990 | 176 | -83.8 | 504990 | 805 | -99.4 | 504990 | 70 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1003: `27c0cd07-2f0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `27c0cd07-2f01-4795-9755-5ffd7298f451` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease A3 Offset threshold for 3240818_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1003] topology](images/train_1003.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3240818_4 by 5 degrees
- `C2`: Check test server and transmission issues
- `C3`: Increase A3 Offset threshold for 3263680_1
- `C4`: Press down the tilt angle  of 3263680_1 by 10 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263680_1
- `C6`: Increase transmission power for 3240818_4
- `C7`: Decrease transmission power for 3263680_1
- `C8`: Adjust the azimuth of 3263680_1 by 50 degrees
- `C9`: Decrease A3 Offset threshold for 3240818_4 **← 정답**
- `C10`: Increase A3 Offset threshold for 3240818_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240818_4
- `C12`: Lift the tilt angle  of 3263680_1 by 10 degrees
- `C13`: Lift the tilt angle of 3240818_4 by 5 degrees
- `C14`: Increase transmission power for 3263680_1
- `C15`: Add neighbor relationship between 3239294_2 and 3263680_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263680_1
- `C17`: Adjust the azimuth of 3240818_4 by 28 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Add neighbor relationship between 3240818_4 and 3263680_1
- `C20`: Decrease transmission power for 3240818_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240818_4
- `C22`: Decrease A3 Offset threshold for 3263680_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.259 | MS1 | 121.4656644317 | 31.1446314931 | 445 | 504990 | -76.62 | 16.82 | 324.01 | 0.01 | 2.58 | 1600 |
| 2024-09-20 22:21:32.931 | MS1 | 121.4656746407 | 31.1446348240 | 445 | 504990 | -78.57 | 15.40 | 361.51 | 0.01 | 2.88 | 1570 |
| 2024-09-20 22:21:33.799 | MS1 | 121.4656756246 | 31.1446268569 | 445 | 504990 | -78.04 | 13.62 | 517.66 | 0.18 | 2.53 | 1563 |
| 2024-09-20 22:21:34.849 | MS1 | 121.4656712784 | 31.1446258754 | 445 | 504990 | -92.13 | -3.51 | 74.34 | 0.03 | 1.12 | 1569 |
| 2024-09-20 22:21:35.423 | MS1 | 121.4656731161 | 31.1446308024 | 445 | 504990 | -87.25 | -1.29 | 26.65 | 0.20 | 1.21 | 1581 |
| 2024-09-20 22:21:36.704 | MS1 | 121.4656704042 | 31.1446258936 | 445 | 504990 | -84.35 | -3.39 | 62.99 | 0.09 | 1.22 | 1564 |
| 2024-09-20 22:21:37.465 | MS1 | 121.4656615513 | 31.1446362596 | 445 | 504990 | -85.99 | -2.50 | 25.27 | 0.19 | 1.22 | 1567 |
| 2024-09-20 22:21:38.680 | MS1 | 121.4656657280 | 31.1446217486 | 445 | 504990 | -86.24 | -1.38 | 50.01 | 0.06 | 1.35 | 1573 |
| 2024-09-20 22:21:39.907 | MS1 | 121.4656673410 | 31.1446294126 | 129 | 504990 | -81.84 | 16.13 | 229.05 | 0.16 | 1.29 | 1574 |
| 2024-09-20 22:21:40.275 | MS1 | 121.4656585918 | 31.1446322773 | 129 | 504990 | -80.26 | 16.77 | 593.75 | 0.04 | 2.89 | 1584 |
| 2024-09-20 22:21:41.194 | MS1 | 121.4656652630 | 31.1446377776 | 129 | 504990 | -77.38 | 16.89 | 327.31 | 0.05 | 2.46 | 1578 |
| 2024-09-20 22:21:42.851 | MS1 | 121.4656614046 | 31.1446262016 | 129 | 504990 | -77.13 | 16.52 | 545.62 | 0.13 | 2.07 | 1585 |

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
| 3239294 | 2 | 121.4666745157 | 31.1444022416 | 114 | 11 | 8 | 15.8 | TDD | 945 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3240818 | 4 | 121.4665630906 | 31.1502838937 | 160 | 4 | 5 | 16.5 | TDD | 445 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3253637 | 3 | 121.4736442059 | 31.1516253629 | 213 | 2 | 6 | 34.3 | TDD | 837 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3263680 | 1 | 121.4657978663 | 31.1446494915 | 144 | 3 | 8 | 31.2 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.459 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.475 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.579 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.579 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.325 | NREventA3 | measId:2;ServCellPCI:528;Se... |
| 2024-09-20 22:21:38.565 | NRHandoverAttempt | SourcePCI:528;SourceNR-ARFC... |
| 2024-09-20 22:21:38.595 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.606 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.745 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.745 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263680 | 1 | 15.1399 | 14.4177 | -116.4284 | 5.4006 | 145.7006 | 0.0121 | 0.0184 |
| 2024_09_20 22:00 | 3239294 | 2 | 6.3642 | 5.4726 | -115.3337 | 14.4253 | 139.8201 | 0.0115 | 0.0150 |
| 2024_09_20 22:00 | 3253637 | 3 | 9.3340 | 5.4046 | -114.4110 | 14.0069 | 150.4169 | 0.0090 | 0.0131 |
| 2024_09_20 22:00 | 3240818 | 4 | 14.5579 | 16.7798 | -117.0633 | 13.9326 | 123.7133 | 0.0096 | 0.1504 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413309_957CC9AF | 504990 | 445 | -93.4 | 504990 | 129 | -86.0 | 504990 | 945 | -94.6 | 504990 | 837 |
| MR_1774413309_AB27539A | 504990 | 129 | -85.7 | 504990 | 445 | -93.1 | 504990 | 945 | -95.7 | 504990 | 837 |
| MR_1774413309_F39D7DE8 | 504990 | 445 | -90.5 | 504990 | 129 | -85.7 | 504990 | 945 | -94.1 | 504990 | 837 |
| MR_1774413309_E25EA7AC | 504990 | 129 | -85.5 | 504990 | 445 | -92.3 | 504990 | 945 | -96.8 | 504990 | 837 |
| MR_1774413309_E45D4787 | 504990 | 129 | -85.1 | 504990 | 445 | -92.1 | 504990 | 945 | -96.3 | 504990 | 837 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1004: `a0da0f22-dbf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a0da0f22-dbfc-4de1-be41-ee33e860bef1` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Add neighbor relationship between 3239556_3 and 3211580_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1004] topology](images/train_1004.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3211580_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211580_2
- `C3`: Increase A3 Offset threshold for 3239556_3
- `C4`: Adjust the azimuth of 3211580_2 by 39 degrees
- `C5`: Add neighbor relationship between 3231045_1 and 3211580_2
- `C6`: Press down the tilt angle  of 3211580_2 by 3 degrees
- `C7`: Increase transmission power for 3239556_3
- `C8`: Adjust the azimuth of 3239556_3 by 50 degrees
- `C9`: Increase A3 Offset threshold for 3211580_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239556_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239556_3
- `C12`: Decrease transmission power for 3239556_3
- `C13`: Decrease A3 Offset threshold for 3239556_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211580_2
- `C15`: Check test server and transmission issues
- `C16`: Add neighbor relationship between 3239556_3 and 3211580_2 **← 정답**
- `C17`: Press down the tilt angle of 3239556_3 by 3 degrees
- `C18`: Increase transmission power for 3211580_2
- `C19`: Decrease A3 Offset threshold for 3211580_2
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Lift the tilt angle  of 3211580_2 by 3 degrees
- `C22`: Lift the tilt angle of 3239556_3 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.538 | MS1 | 121.4656737128 | 31.1446358918 | 557 | 504990 | -76.24 | 14.91 | 324.04 | 0.03 | 2.74 | 1599 |
| 2024-09-20 22:21:32.882 | MS1 | 121.4656665136 | 31.1446216076 | 557 | 504990 | -77.23 | 15.65 | 493.09 | 0.03 | 2.10 | 1579 |
| 2024-09-20 22:21:33.712 | MS1 | 121.4656748995 | 31.1446221712 | 557 | 504990 | -83.91 | 14.74 | 359.60 | 0.17 | 2.81 | 1562 |
| 2024-09-20 22:21:34.310 | MS1 | 121.4656698804 | 31.1446272395 | 557 | 504990 | -93.65 | -0.64 | 49.11 | 0.13 | 1.47 | 1576 |
| 2024-09-20 22:21:35.879 | MS1 | 121.4656675329 | 31.1446216776 | 557 | 504990 | -92.14 | -2.08 | 53.79 | 0.13 | 1.14 | 1560 |
| 2024-09-20 22:21:36.463 | MS1 | 121.4656766907 | 31.1446347131 | 557 | 504990 | -94.96 | -0.82 | 27.66 | 0.03 | 1.14 | 1574 |
| 2024-09-20 22:21:37.197 | MS1 | 121.4656638379 | 31.1446262757 | 557 | 504990 | -91.82 | -2.29 | 48.30 | 0.19 | 1.01 | 1578 |
| 2024-09-20 22:21:38.559 | MS1 | 121.4656584747 | 31.1446217452 | 557 | 504990 | -79.83 | 16.71 | 348.67 | 0.03 | 1.13 | 1598 |
| 2024-09-20 22:21:39.774 | MS1 | 121.4656587119 | 31.1446247759 | 557 | 504990 | -78.87 | 14.35 | 575.28 | 0.15 | 1.22 | 1569 |
| 2024-09-20 22:21:40.561 | MS1 | 121.4656618221 | 31.1446369179 | 557 | 504990 | -79.29 | 15.51 | 460.76 | 0.01 | 2.73 | 1591 |
| 2024-09-20 22:21:41.761 | MS1 | 121.4656627806 | 31.1446254594 | 557 | 504990 | -80.67 | 13.30 | 558.94 | 0.14 | 2.20 | 1588 |
| 2024-09-20 22:21:42.288 | MS1 | 121.4656606861 | 31.1446205259 | 557 | 504990 | -80.75 | 15.93 | 598.31 | 0.04 | 2.93 | 1578 |

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
| 3211580 | 2 | 121.4679237873 | 31.1541517169 | 230 | 0 | 10 | 47.9 | TDD | 145 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3217560 | 4 | 121.4659751754 | 31.1519773565 | 107 | 9 | 1 | 28.2 | TDD | 958 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3231045 | 1 | 121.4645444226 | 31.1519026566 | 175 | 1 | 1 | 46.7 | TDD | 200 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3239556 | 3 | 121.4647199615 | 31.1530272999 | 243 | 2 | 8 | 22.8 | TDD | 557 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.739 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.761 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.897 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.897 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.630 | NREventA3 | measId:2;ServCellPCI:866;Se... |
| 2024-09-20 22:21:35.630 | NREventA3 | measId:2;ServCellPCI:866;Se... |
| 2024-09-20 22:21:36.630 | NREventA3 | measId:2;ServCellPCI:866;Se... |
| 2024-09-20 22:21:39.130 | NRRRCReestablishAttempt | PCI:866 |
| 2024-09-20 22:21:39.144 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.154 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.297 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.297 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231045 | 1 | 19.3151 | 5.5773 | -117.7466 | 19.0731 | 153.4124 | 0.0174 | 0.0063 |
| 2024_09_20 22:00 | 3211580 | 2 | 10.4064 | 9.1683 | -116.8032 | 5.1533 | 197.3152 | 0.0102 | 0.0030 |
| 2024_09_20 22:00 | 3239556 | 3 | 7.6575 | 15.6477 | -114.7991 | 18.9077 | 147.4236 | 0.0042 | 0.1457 |
| 2024_09_20 22:00 | 3217560 | 4 | 12.3061 | 19.1926 | -114.2152 | 18.6026 | 166.3783 | 0.0177 | 0.0115 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414563_70ACB88C | 504990 | 557 | -94.5 | 504990 | 145 | -88.4 | 504990 | 200 | -89.9 | 504990 | 958 |
| MR_1774414563_90699B0D | 504990 | 145 | -90.6 | 504990 | 557 | -91.8 | 504990 | 200 | -89.8 | 504990 | 958 |
| MR_1774414563_811A94A3 | 504990 | 145 | -86.7 | 504990 | 557 | -93.8 | 504990 | 200 | -87.8 | 504990 | 958 |
| MR_1774414563_6A26241A | 504990 | 557 | -95.0 | 504990 | 145 | -87.7 | 504990 | 200 | -90.0 | 504990 | 958 |
| MR_1774414563_7CDF7E34 | 504990 | 145 | -87.5 | 504990 | 557 | -92.9 | 504990 | 200 | -89.4 | 504990 | 958 |
| MR_1774414563_35E7A403 | 504990 | 557 | -92.4 | 504990 | 145 | -87.5 | 504990 | 200 | -87.6 | 504990 | 958 |
| MR_1774414563_CAE9AFA9 | 504990 | 145 | -87.3 | 504990 | 557 | -95.6 | 504990 | 200 | -91.0 | 504990 | 958 |
| MR_1774414563_A9C0DB84 | 504990 | 145 | -89.8 | 504990 | 557 | -94.8 | 504990 | 200 | -89.4 | 504990 | 958 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1005: `5960ce5b-c2c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5960ce5b-c2cc-4059-9ad1-d81da20ee237` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1005] topology](images/train_1005.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258195_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241747_4
- `C3`: Add neighbor relationship between 3258195_1 and 3241747_4
- `C4`: Adjust the azimuth of 3258195_1 by 50 degrees
- `C5`: Increase transmission power for 3258195_1
- `C6`: Decrease transmission power for 3241747_4
- `C7`: Add neighbor relationship between 3270514_3 and 3241747_4
- `C8`: Insufficient data; more data is needed for judgment. **← 정답**
- `C9`: Increase A3 Offset threshold for 3241747_4
- `C10`: Increase A3 Offset threshold for 3258195_1
- `C11`: Lift the tilt angle of 3258195_1 by 10 degrees
- `C12`: Decrease transmission power for 3258195_1
- `C13`: Press down the tilt angle  of 3241747_4 by 9 degrees
- `C14`: Decrease A3 Offset threshold for 3241747_4
- `C15`: Lift the tilt angle  of 3241747_4 by 9 degrees
- `C16`: Increase transmission power for 3241747_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241747_4
- `C18`: Decrease A3 Offset threshold for 3258195_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258195_1
- `C20`: Press down the tilt angle of 3258195_1 by 10 degrees
- `C21`: Check test server and transmission issues
- `C22`: Adjust the azimuth of 3241747_4 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.534 | MS1 | 121.4656694747 | 31.1446200553 | 569 | 504990 | -89.55 | 15.91 | 556.30 | 0.04 | 2.58 | 1591 |
| 2024-09-20 22:21:32.369 | MS1 | 121.4656762408 | 31.1446289991 | 569 | 504990 | -87.35 | 12.93 | 325.17 | 0.14 | 2.14 | 1576 |
| 2024-09-20 22:21:33.944 | MS1 | 121.4656637595 | 31.1446284790 | 569 | 504990 | -89.94 | 13.57 | 328.33 | 0.10 | 2.46 | 1569 |
| 2024-09-20 22:21:34.868 | MS1 | 121.4656768528 | 31.1446360328 | 569 | 504990 | -89.18 | 13.39 | 75.18 | 0.14 | 2.28 | 1588 |
| 2024-09-20 22:21:35.409 | MS1 | 121.4656728441 | 31.1446212367 | 569 | 504990 | -87.24 | 16.57 | 83.51 | 0.19 | 2.78 | 1586 |
| 2024-09-20 22:21:36.425 | MS1 | 121.4656764042 | 31.1446271213 | 569 | 504990 | -89.60 | 13.37 | 70.49 | 0.03 | 2.30 | 1562 |
| 2024-09-20 22:21:37.149 | MS1 | 121.4656616225 | 31.1446362205 | 569 | 504990 | -90.09 | 9.38 | 61.81 | 0.12 | 2.46 | 1592 |
| 2024-09-20 22:21:38.613 | MS1 | 121.4656776405 | 31.1446235377 | 569 | 504990 | -90.30 | 10.58 | 61.98 | 0.07 | 2.17 | 1575 |
| 2024-09-20 22:21:39.994 | MS1 | 121.4656684999 | 31.1446280013 | 569 | 504990 | -92.76 | 11.81 | 76.53 | 0.01 | 2.32 | 1587 |
| 2024-09-20 22:21:40.723 | MS1 | 121.4656763101 | 31.1446324111 | 569 | 504990 | -91.97 | 12.20 | 522.56 | 0.03 | 2.98 | 1594 |
| 2024-09-20 22:21:41.270 | MS1 | 121.4656605275 | 31.1446209366 | 569 | 504990 | -91.24 | 11.76 | 302.21 | 0.16 | 2.96 | 1563 |
| 2024-09-20 22:21:42.268 | MS1 | 121.4656620502 | 31.1446332733 | 569 | 504990 | -93.34 | 8.27 | 428.57 | 0.13 | 2.92 | 1586 |

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
| 3227994 | 2 | 121.4718120116 | 31.1548679112 | 241 | 2 | 0 | 40.5 | TDD | 595 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3241747 | 4 | 121.4652772309 | 31.1527112020 | 44 | 6 | 3 | 43.8 | TDD | 381 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3258195 | 1 | 121.4749803532 | 31.1463662397 | 108 | 9 | 0 | 24.5 | TDD | 569 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3270514 | 3 | 121.4727416859 | 31.1553451129 | 343 | 10 | 7 | 35.9 | TDD | 356 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.562 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.585 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.711 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.711 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.397 | NREventA3 | measId:2;ServCellPCI:657;Se... |
| 2024-09-20 22:21:38.637 | NRHandoverAttempt | SourcePCI:657;SourceNR-ARFC... |
| 2024-09-20 22:21:38.677 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.690 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.799 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.799 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3258195 | 1 | 85.6707 | 92.8757 | -114.0214 | 10.0844 | 145.5678 | 0.0057 | 0.0061 |
| 2024_09_19 22:00 | 3227994 | 2 | 79.6394 | 91.1800 | -116.5861 | 13.8779 | 131.5346 | 0.0191 | 0.0107 |
| 2024_09_19 22:00 | 3270514 | 3 | 78.6021 | 84.2222 | -114.9278 | 10.1190 | 101.2889 | 0.0098 | 0.0002 |
| 2024_09_19 22:00 | 3241747 | 4 | 93.0593 | 80.8276 | -117.7473 | 11.5451 | 189.3544 | 0.0169 | 0.0181 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417091_BB08E1DC | 504990 | 569 | -91.2 | 504990 | 381 | -89.5 | 504990 | 356 | -96.8 | 504990 | 595 |
| MR_1774417091_5C12911C | 504990 | 569 | -89.2 | 504990 | 381 | -88.3 | 504990 | 356 | -95.5 | 504990 | 595 |
| MR_1774417091_5D7038A8 | 504990 | 569 | -88.6 | 504990 | 381 | -90.8 | 504990 | 356 | -96.2 | 504990 | 595 |
| MR_1774417091_AF06E58A | 504990 | 569 | -89.1 | 504990 | 381 | -87.9 | 504990 | 356 | -96.2 | 504990 | 595 |
| MR_1774417091_8EF8F2FD | 504990 | 569 | -90.2 | 504990 | 381 | -90.1 | 504990 | 356 | -95.7 | 504990 | 595 |
| MR_1774417091_6AB958B4 | 504990 | 569 | -88.9 | 504990 | 381 | -88.6 | 504990 | 356 | -96.1 | 504990 | 595 |
| MR_1774417091_FDE553C2 | 504990 | 569 | -88.3 | 504990 | 381 | -90.5 | 504990 | 356 | -99.3 | 504990 | 595 |
| MR_1774417091_817080D1 | 504990 | 569 | -88.9 | 504990 | 381 | -88.3 | 504990 | 356 | -98.7 | 504990 | 595 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1006: `76ca4839-ae5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `76ca4839-ae57-40ae-b691-fb2b96de77e3` |
| Tag | **multiple-answer** |
| 정답 | **C1|C8|C10|C17** |
| C1 의미 | Increase A3 Offset threshold for 3225077_3 |
| C8 의미 | Press down the tilt angle  of 3225077_3 by 3 degrees |
| C10 의미 | Decrease transmission power for 3225077_3 |
| C17 의미 | Increase A3 Offset threshold for 3230978_1 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1006] topology](images/train_1006.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3225077_3 **← 정답**
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase transmission power for 3225077_3
- `C4`: Lift the tilt angle  of 3225077_3 by 3 degrees
- `C5`: Decrease A3 Offset threshold for 3230978_1
- `C6`: Decrease A3 Offset threshold for 3225077_3
- `C7`: Increase transmission power for 3230978_1
- `C8`: Press down the tilt angle  of 3225077_3 by 3 degrees **← 정답**
- `C9`: Decrease transmission power for 3230978_1
- `C10`: Decrease transmission power for 3225077_3 **← 정답**
- `C11`: Add neighbor relationship between 3230978_1 and 3225077_3
- `C12`: Add neighbor relationship between 3240815_4 and 3225077_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225077_3
- `C14`: Adjust the azimuth of 3230978_1 by 19 degrees
- `C15`: Press down the tilt angle of 3230978_1 by 3 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225077_3
- `C17`: Increase A3 Offset threshold for 3230978_1 **← 정답**
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230978_1
- `C19`: Check test server and transmission issues
- `C20`: Adjust the azimuth of 3225077_3 by 39 degrees
- `C21`: Lift the tilt angle of 3230978_1 by 3 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230978_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.179 | MS1 | 121.4656771756 | 31.1446335009 | 960 | 504990 | -84.19 | 12.75 | 409.69 | 0.19 | 2.97 | 1571 |
| 2024-09-20 22:21:32.488 | MS1 | 121.4656659222 | 31.1446261646 | 960 | 504990 | -81.04 | 16.34 | 474.67 | 0.18 | 2.19 | 1596 |
| 2024-09-20 22:21:33.183 | MS1 | 121.4656596653 | 31.1446296052 | 960 | 504990 | -75.38 | 16.16 | 364.04 | 0.04 | 2.53 | 1563 |
| 2024-09-20 22:21:34.689 | MS1 | 121.4656585712 | 31.1446302694 | 203 | 504990 | -85.90 | 3.07 | 58.09 | 0.13 | 1.05 | 1596 |
| 2024-09-20 22:21:35.565 | MS1 | 121.4656602386 | 31.1446249382 | 203 | 504990 | -83.15 | 4.00 | 77.00 | 0.11 | 1.05 | 1570 |
| 2024-09-20 22:21:36.194 | MS1 | 121.4656640817 | 31.1446339767 | 960 | 504990 | -87.73 | 3.22 | 38.31 | 0.01 | 1.17 | 1565 |
| 2024-09-20 22:21:37.398 | MS1 | 121.4656585198 | 31.1446290453 | 960 | 504990 | -80.54 | 1.40 | 77.09 | 0.15 | 1.23 | 1565 |
| 2024-09-20 22:21:38.301 | MS1 | 121.4656760694 | 31.1446200944 | 203 | 504990 | -80.11 | 1.23 | 61.46 | 0.06 | 1.38 | 1563 |
| 2024-09-20 22:21:39.451 | MS1 | 121.4656634515 | 31.1446272678 | 203 | 504990 | -86.23 | 4.33 | 68.80 | 0.06 | 1.49 | 1600 |
| 2024-09-20 22:21:40.923 | MS1 | 121.4656770398 | 31.1446379647 | 203 | 504990 | -80.83 | 14.57 | 460.50 | 0.14 | 2.43 | 1586 |
| 2024-09-20 22:21:41.613 | MS1 | 121.4656639079 | 31.1446185226 | 203 | 504990 | -84.24 | 12.43 | 418.42 | 0.20 | 2.52 | 1587 |
| 2024-09-20 22:21:42.645 | MS1 | 121.4656585313 | 31.1446183405 | 203 | 504990 | -80.06 | 14.04 | 329.79 | 0.14 | 2.31 | 1577 |

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
| 3218934 | 5 | 121.4669109305 | 31.1474004558 | 337 | 10 | 10 | 24.1 | TDD | 203 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3225077 | 3 | 121.4711346711 | 31.1541383933 | 167 | 1 | 0 | 33.2 | TDD | 8 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3230978 | 1 | 121.4698741251 | 31.1525619733 | 223 | 1 | 3 | 42.0 | TDD | 960 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3240815 | 4 | 121.4759686781 | 31.1484233697 | 323 | 11 | 3 | 29.5 | TDD | 1001 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3250467 | 2 | 121.4752661769 | 31.1480743583 | 39 | 12 | 7 | 35.7 | TDD | 226 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.014 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.029 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.141 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.141 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.857 | NREventA3 | measId:2;ServCellPCI:785;Se... |
| 2024-09-20 22:21:34.097 | NRHandoverAttempt | SourcePCI:785;SourceNR-ARFC... |
| 2024-09-20 22:21:34.142 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.156 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:34.279 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.279 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.857 | NREventA3 | measId:2;ServCellPCI:921;Se... |
| 2024-09-20 22:21:36.097 | NRHandoverAttempt | SourcePCI:921;SourceNR-ARFC... |
| 2024-09-20 22:21:36.132 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.143 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.291 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.291 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.857 | NREventA3 | measId:2;ServCellPCI:785;Se... |
| 2024-09-20 22:21:38.097 | NRHandoverAttempt | SourcePCI:785;SourceNR-ARFC... |
| 2024-09-20 22:21:38.138 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.152 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.299 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.299 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230978 | 1 | 7.1391 | 6.5979 | -115.9139 | 6.2728 | 133.1238 | 0.0086 | 0.0052 |
| 2024_09_20 22:00 | 3250467 | 2 | 14.8842 | 13.3600 | -114.4901 | 9.6415 | 166.2343 | 0.0024 | 0.0128 |
| 2024_09_20 22:00 | 3225077 | 3 | 7.7449 | 14.7017 | -115.3025 | 19.5392 | 146.7506 | 0.0062 | 0.0144 |
| 2024_09_20 22:00 | 3240815 | 4 | 19.6161 | 7.1877 | -115.7722 | 12.3088 | 169.9356 | 0.0184 | 0.0011 |
| 2024_09_20 22:00 | 3218934 | 5 | 11.4221 | 6.2425 | -114.0244 | 10.1193 | 106.1975 | 0.0056 | 0.0094 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416981_BAB13681 | 504990 | 960 | -84.7 | 504990 | 203 | -88.4 | 504990 | 8 | -89.1 | 504990 | 1001 |
| MR_1774416981_CB3638EF | 504990 | 960 | -85.4 | 504990 | 203 | -88.5 | 504990 | 8 | -86.8 | 504990 | 1001 |
| MR_1774416981_684618A2 | 504990 | 203 | -84.9 | 504990 | 960 | -85.3 | 504990 | 8 | -88.7 | 504990 | 1001 |
| MR_1774416981_7929D578 | 504990 | 203 | -84.1 | 504990 | 960 | -88.8 | 504990 | 8 | -86.4 | 504990 | 1001 |
| MR_1774416981_053A6B65 | 504990 | 203 | -84.5 | 504990 | 960 | -85.7 | 504990 | 8 | -86.3 | 504990 | 1001 |
| MR_1774416981_FF43C907 | 504990 | 203 | -84.1 | 504990 | 960 | -86.9 | 504990 | 8 | -87.9 | 504990 | 1001 |
| MR_1774416981_9CD21287 | 504990 | 203 | -86.5 | 504990 | 960 | -85.6 | 504990 | 8 | -89.4 | 504990 | 1001 |
| MR_1774416981_54833526 | 504990 | 960 | -87.6 | 504990 | 203 | -88.8 | 504990 | 8 | -88.5 | 504990 | 1001 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1007: `8a1a57d5-774...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8a1a57d5-774a-4adb-b62d-65b0b6d6039d` |
| Tag | **multiple-answer** |
| 정답 | **C3|C20** |
| C3 의미 | Adjust the azimuth of 3265154_1 by 45 degrees |
| C20 의미 | Increase transmission power for 3265154_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1007] topology](images/train_1007.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225957_3
- `C2`: Lift the tilt angle of 3265154_1 by 10 degrees
- `C3`: Adjust the azimuth of 3265154_1 by 45 degrees **← 정답**
- `C4`: Decrease A3 Offset threshold for 3265154_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265154_1
- `C7`: Increase A3 Offset threshold for 3265154_1
- `C8`: Decrease transmission power for 3265154_1
- `C9`: Increase A3 Offset threshold for 3225957_3
- `C10`: Lift the tilt angle  of 3225957_3 by 4 degrees
- `C11`: Check test server and transmission issues
- `C12`: Add neighbor relationship between 3257807_4 and 3225957_3
- `C13`: Decrease A3 Offset threshold for 3225957_3
- `C14`: Increase transmission power for 3225957_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265154_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225957_3
- `C17`: Decrease transmission power for 3225957_3
- `C18`: Press down the tilt angle of 3265154_1 by 10 degrees
- `C19`: Press down the tilt angle  of 3225957_3 by 4 degrees
- `C20`: Increase transmission power for 3265154_1 **← 정답**
- `C21`: Add neighbor relationship between 3265154_1 and 3225957_3
- `C22`: Adjust the azimuth of 3225957_3 by 26 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.518 | MS1 | 121.4656714915 | 31.1446215896 | 592 | 504990 | -87.39 | 17.10 | 348.35 | 0.16 | 2.78 | 1593 |
| 2024-09-20 22:21:32.399 | MS1 | 121.4656683090 | 31.1446215084 | 592 | 504990 | -89.58 | 12.92 | 467.89 | 0.01 | 2.84 | 1570 |
| 2024-09-20 22:21:33.105 | MS1 | 121.4656757557 | 31.1446333467 | 592 | 504990 | -88.03 | 16.57 | 547.55 | 0.03 | 2.60 | 1577 |
| 2024-09-20 22:21:34.393 | MS1 | 121.4656590526 | 31.1446205897 | 592 | 504990 | -108.93 | -1.17 | 57.40 | 0.17 | 1.29 | 1568 |
| 2024-09-20 22:21:35.959 | MS1 | 121.4656777388 | 31.1446351589 | 592 | 504990 | -108.61 | -1.02 | 72.21 | 0.14 | 1.30 | 1572 |
| 2024-09-20 22:21:36.616 | MS1 | 121.4656584864 | 31.1446258873 | 592 | 504990 | -105.80 | -0.06 | 33.83 | 0.10 | 1.15 | 1580 |
| 2024-09-20 22:21:37.557 | MS1 | 121.4656580240 | 31.1446378641 | 592 | 504990 | -103.63 | 1.28 | 47.33 | 0.02 | 1.34 | 1565 |
| 2024-09-20 22:21:38.863 | MS1 | 121.4656765187 | 31.1446351479 | 592 | 504990 | -101.75 | -0.68 | 19.09 | 0.00 | 1.03 | 1569 |
| 2024-09-20 22:21:39.924 | MS1 | 121.4656586411 | 31.1446191089 | 592 | 504990 | -105.43 | 0.24 | 31.32 | 0.08 | 1.13 | 1581 |
| 2024-09-20 22:21:40.428 | MS1 | 121.4656766152 | 31.1446378148 | 592 | 504990 | -94.38 | 16.27 | 305.02 | 0.16 | 2.38 | 1570 |
| 2024-09-20 22:21:41.440 | MS1 | 121.4656710137 | 31.1446298714 | 592 | 504990 | -91.92 | 13.78 | 306.11 | 0.06 | 2.01 | 1572 |
| 2024-09-20 22:21:42.146 | MS1 | 121.4656689765 | 31.1446274336 | 592 | 504990 | -86.90 | 17.52 | 309.17 | 0.17 | 2.53 | 1595 |

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
| 3215778 | 2 | 121.4740805103 | 31.1445952949 | 218 | 7 | 7 | 44.6 | TDD | 11 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3225957 | 3 | 121.4652255016 | 31.1558970902 | 204 | 3 | 8 | 18.8 | TDD | 829 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3257807 | 4 | 121.4757533358 | 31.1526524972 | 358 | 5 | 2 | 20.7 | TDD | 694 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3265154 | 1 | 121.4724535999 | 31.1486931868 | 280 | 12 | 12 | 49.5 | TDD | 592 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.933 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.038 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.038 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.274 | NREventA2 | measId:1;ServCellPCI:123;Se... |
| 2024-09-20 22:21:34.383 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265154 | 1 | 18.7063 | 16.4275 | -116.7192 | 19.9940 | 167.9971 | 0.1100 | 0.0070 |
| 2024_09_20 22:00 | 3215778 | 2 | 15.8002 | 9.4594 | -116.1975 | 6.4470 | 193.3802 | 0.0188 | 0.0150 |
| 2024_09_20 22:00 | 3225957 | 3 | 10.0208 | 6.6407 | -116.7393 | 17.3257 | 90.2907 | 0.0008 | 0.0075 |
| 2024_09_20 22:00 | 3257807 | 4 | 15.1876 | 10.8402 | -114.0554 | 12.6177 | 88.6188 | 0.0145 | 0.0160 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412094_3C6209BB | 504990 | 592 | -109.5 | 504990 | 829 | -115.2 | 504990 | 694 | -121.0 | 504990 | 11 |
| MR_1774412094_D83EBAB1 | 504990 | 592 | -107.8 | 504990 | 829 | -114.5 | 504990 | 694 | -119.7 | 504990 | 11 |
| MR_1774412094_F00DEFC9 | 504990 | 592 | -109.5 | 504990 | 829 | -115.2 | 504990 | 694 | -122.3 | 504990 | 11 |
| MR_1774412094_A4B2AD20 | 504990 | 592 | -107.0 | 504990 | 829 | -114.0 | 504990 | 694 | -119.9 | 504990 | 11 |
| MR_1774412094_07593676 | 504990 | 592 | -107.8 | 504990 | 829 | -112.9 | 504990 | 694 | -122.0 | 504990 | 11 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1008: `b8c1026a-703...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b8c1026a-7030-4fb2-8d5d-df790b5bd1f5` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3271808_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1008] topology](images/train_1008.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3271808_1 by 31 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219956_3
- `C3`: Decrease transmission power for 3219956_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271808_1
- `C5`: Lift the tilt angle  of 3219956_3 by 9 degrees
- `C6`: Add neighbor relationship between 3271808_1 and 3219956_3
- `C7`: Check test server and transmission issues
- `C8`: Press down the tilt angle  of 3219956_3 by 9 degrees
- `C9`: Press down the tilt angle of 3271808_1 by 5 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219956_3
- `C11`: Lift the tilt angle of 3271808_1 by 5 degrees
- `C12`: Decrease transmission power for 3271808_1
- `C13`: Increase A3 Offset threshold for 3271808_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase A3 Offset threshold for 3219956_3
- `C16`: Add neighbor relationship between 3228300_2 and 3219956_3
- `C17`: Adjust the azimuth of 3219956_3 by 50 degrees
- `C18`: Increase transmission power for 3271808_1
- `C19`: Decrease A3 Offset threshold for 3271808_1
- `C20`: Decrease A3 Offset threshold for 3219956_3
- `C21`: Increase transmission power for 3219956_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271808_1 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.942 | MS1 | 121.4656616593 | 31.1446208483 | 418 | 504990 | -91.73 | 14.09 | 391.20 | 0.16 | 2.39 | 1599 |
| 2024-09-20 22:21:32.265 | MS1 | 121.4656663276 | 31.1446312185 | 418 | 504990 | -87.90 | 17.60 | 563.11 | 0.13 | 2.95 | 1564 |
| 2024-09-20 22:21:33.743 | MS1 | 121.4656690503 | 31.1446260184 | 418 | 504990 | -85.21 | 17.74 | 552.58 | 0.13 | 2.72 | 1560 |
| 2024-09-20 22:21:34.796 | MS1 | 121.4656777966 | 31.1446221726 | 418 | 504990 | -89.25 | 14.81 | 90.79 | 0.56 | 2.86 | 624 |
| 2024-09-20 22:21:35.401 | MS1 | 121.4656650421 | 31.1446186102 | 418 | 504990 | -88.65 | 15.14 | 74.68 | 0.55 | 2.69 | 557 |
| 2024-09-20 22:21:36.491 | MS1 | 121.4656693565 | 31.1446201074 | 418 | 504990 | -90.91 | 13.25 | 67.69 | 0.61 | 2.98 | 615 |
| 2024-09-20 22:21:37.559 | MS1 | 121.4656724637 | 31.1446209964 | 418 | 504990 | -91.88 | 7.95 | 78.17 | 0.67 | 2.40 | 651 |
| 2024-09-20 22:21:38.445 | MS1 | 121.4656612512 | 31.1446307321 | 418 | 504990 | -93.55 | 9.21 | 65.73 | 0.68 | 2.67 | 590 |
| 2024-09-20 22:21:39.227 | MS1 | 121.4656682240 | 31.1446233646 | 418 | 504990 | -93.51 | 7.15 | 69.35 | 0.66 | 2.17 | 658 |
| 2024-09-20 22:21:40.471 | MS1 | 121.4656768449 | 31.1446182849 | 418 | 504990 | -91.34 | 10.03 | 499.53 | 0.20 | 2.26 | 1580 |
| 2024-09-20 22:21:41.854 | MS1 | 121.4656767449 | 31.1446180434 | 418 | 504990 | -90.88 | 11.99 | 358.16 | 0.18 | 2.97 | 1576 |
| 2024-09-20 22:21:42.601 | MS1 | 121.4656632218 | 31.1446196357 | 418 | 504990 | -93.18 | 7.79 | 323.72 | 0.13 | 2.44 | 1565 |

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
| 3219956 | 3 | 121.4668849914 | 31.1544517783 | 349 | 7 | 0 | 38.9 | TDD | 941 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3228300 | 2 | 121.4721754102 | 31.1540424019 | 182 | 11 | 7 | 49.1 | TDD | 372 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3264256 | 4 | 121.4689345283 | 31.1555383291 | 140 | 3 | 1 | 47.0 | TDD | 438 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3271808 | 1 | 121.4710191332 | 31.1495733779 | 192 | 3 | 7 | 27.9 | TDD | 418 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.521 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.536 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.643 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.643 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.344 | NREventA3 | measId:2;ServCellPCI:283;Se... |
| 2024-09-20 22:21:38.584 | NRHandoverAttempt | SourcePCI:283;SourceNR-ARFC... |
| 2024-09-20 22:21:38.618 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.633 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.767 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.767 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271808 | 1 | 8.0425 | 17.7283 | -116.4819 | 17.3757 | 184.5299 | 0.0036 | 0.0116 |
| 2024_09_20 22:00 | 3228300 | 2 | 5.1134 | 13.5561 | -116.2657 | 17.0596 | 159.4378 | 0.0110 | 0.0135 |
| 2024_09_20 22:00 | 3219956 | 3 | 8.6337 | 9.2837 | -115.4928 | 15.0896 | 161.0488 | 0.0124 | 0.0145 |
| 2024_09_20 22:00 | 3264256 | 4 | 11.8435 | 15.4993 | -116.1931 | 11.0139 | 133.4177 | 0.0144 | 0.0079 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413555_7AB0AA02 | 504990 | 418 | -87.7 | 504990 | 941 | -97.2 | 504990 | 372 | -100.6 | 504990 | 438 |
| MR_1774413555_285CC910 | 504990 | 418 | -88.1 | 504990 | 941 | -97.0 | 504990 | 372 | -100.9 | 504990 | 438 |
| MR_1774413555_C0B23CAD | 504990 | 418 | -88.6 | 504990 | 941 | -94.7 | 504990 | 372 | -103.6 | 504990 | 438 |
| MR_1774413555_BEDC4811 | 504990 | 418 | -87.9 | 504990 | 941 | -93.8 | 504990 | 372 | -102.2 | 504990 | 438 |
| MR_1774413555_B954E9F2 | 504990 | 418 | -88.7 | 504990 | 941 | -93.6 | 504990 | 372 | -102.9 | 504990 | 438 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1009: `4476c282-156...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4476c282-156b-423b-9b99-f4d590e0eb63` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3227464_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1009] topology](images/train_1009.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3227464_2 by 3 degrees
- `C2`: Press down the tilt angle of 3227464_2 by 3 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227464_2 **← 정답**
- `C4`: Lift the tilt angle  of 3256282_1 by 4 degrees
- `C5`: Increase transmission power for 3227464_2
- `C6`: Add neighbor relationship between 3227464_2 and 3256282_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256282_1
- `C8`: Add neighbor relationship between 3255851_3 and 3256282_1
- `C9`: Increase transmission power for 3256282_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256282_1
- `C11`: Decrease transmission power for 3256282_1
- `C12`: Adjust the azimuth of 3256282_1 by 50 degrees
- `C13`: Decrease A3 Offset threshold for 3256282_1
- `C14`: Decrease A3 Offset threshold for 3227464_2
- `C15`: Decrease transmission power for 3227464_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227464_2
- `C18`: Check test server and transmission issues
- `C19`: Increase A3 Offset threshold for 3256282_1
- `C20`: Press down the tilt angle  of 3256282_1 by 4 degrees
- `C21`: Increase A3 Offset threshold for 3227464_2
- `C22`: Adjust the azimuth of 3227464_2 by 13 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.139 | MS1 | 121.4656654806 | 31.1446218462 | 833 | 504990 | -91.76 | 14.45 | 352.09 | 0.01 | 2.95 | 1594 |
| 2024-09-20 22:21:32.998 | MS1 | 121.4656668313 | 31.1446250518 | 833 | 504990 | -88.89 | 13.06 | 395.62 | 0.05 | 2.03 | 1583 |
| 2024-09-20 22:21:33.757 | MS1 | 121.4656689883 | 31.1446241412 | 833 | 504990 | -90.61 | 12.31 | 307.08 | 0.14 | 2.73 | 1581 |
| 2024-09-20 22:21:34.366 | MS1 | 121.4656677628 | 31.1446334007 | 833 | 504990 | -90.40 | 15.39 | 85.46 | 0.62 | 2.59 | 621 |
| 2024-09-20 22:21:35.659 | MS1 | 121.4656778688 | 31.1446263308 | 833 | 504990 | -85.16 | 16.77 | 79.46 | 0.54 | 2.74 | 660 |
| 2024-09-20 22:21:36.827 | MS1 | 121.4656659214 | 31.1446337284 | 833 | 504990 | -86.51 | 14.41 | 57.32 | 0.70 | 2.90 | 641 |
| 2024-09-20 22:21:37.166 | MS1 | 121.4656723086 | 31.1446327967 | 833 | 504990 | -91.69 | 8.56 | 86.97 | 0.58 | 2.02 | 538 |
| 2024-09-20 22:21:38.519 | MS1 | 121.4656581864 | 31.1446326345 | 833 | 504990 | -90.85 | 7.77 | 74.77 | 0.63 | 2.24 | 528 |
| 2024-09-20 22:21:39.134 | MS1 | 121.4656751504 | 31.1446338716 | 833 | 504990 | -93.96 | 8.90 | 49.60 | 0.61 | 2.16 | 508 |
| 2024-09-20 22:21:40.233 | MS1 | 121.4656623742 | 31.1446210518 | 833 | 504990 | -91.49 | 7.61 | 345.69 | 0.07 | 2.95 | 1570 |
| 2024-09-20 22:21:41.230 | MS1 | 121.4656605602 | 31.1446263793 | 833 | 504990 | -93.18 | 7.76 | 537.87 | 0.05 | 2.24 | 1586 |
| 2024-09-20 22:21:42.250 | MS1 | 121.4656608569 | 31.1446340145 | 833 | 504990 | -89.86 | 11.47 | 399.12 | 0.19 | 2.93 | 1595 |

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
| 3227464 | 2 | 121.4741083625 | 31.1490173210 | 226 | 2 | 10 | 19.1 | TDD | 833 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3255851 | 3 | 121.4674676213 | 31.1455054521 | 307 | 8 | 10 | 31.6 | TDD | 909 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3256282 | 1 | 121.4677941973 | 31.1537145503 | 37 | 1 | 2 | 49.2 | TDD | 456 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3272074 | 4 | 121.4724292091 | 31.1442268563 | 282 | 5 | 2 | 18.2 | TDD | 785 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.325 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.343 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.475 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.475 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.223 | NREventA3 | measId:2;ServCellPCI:174;Se... |
| 2024-09-20 22:21:38.463 | NRHandoverAttempt | SourcePCI:174;SourceNR-ARFC... |
| 2024-09-20 22:21:38.504 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.515 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.655 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.655 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256282 | 1 | 12.2236 | 15.4155 | -115.6862 | 18.1873 | 171.2599 | 0.0185 | 0.0159 |
| 2024_09_20 22:00 | 3227464 | 2 | 11.0545 | 19.1883 | -116.4722 | 19.4669 | 85.0632 | 0.0081 | 0.0104 |
| 2024_09_20 22:00 | 3255851 | 3 | 12.2959 | 5.8236 | -115.7375 | 14.7649 | 119.9196 | 0.0084 | 0.0072 |
| 2024_09_20 22:00 | 3272074 | 4 | 13.3851 | 10.9980 | -115.4702 | 17.7169 | 92.5071 | 0.0159 | 0.0180 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414278_F1019711 | 504990 | 833 | -90.9 | 504990 | 456 | -99.3 | 504990 | 909 | -102.2 | 504990 | 785 |
| MR_1774414278_88BEDB7E | 504990 | 833 | -88.6 | 504990 | 456 | -97.7 | 504990 | 909 | -100.6 | 504990 | 785 |
| MR_1774414278_161F4DDC | 504990 | 833 | -91.7 | 504990 | 456 | -100.3 | 504990 | 909 | -100.7 | 504990 | 785 |
| MR_1774414278_51639D9A | 504990 | 833 | -90.0 | 504990 | 456 | -99.4 | 504990 | 909 | -99.4 | 504990 | 785 |
| MR_1774414278_C3DF8B65 | 504990 | 833 | -91.2 | 504990 | 456 | -100.9 | 504990 | 909 | -99.9 | 504990 | 785 |

> *... 2개 열 생략 (전체 14열)*

---
