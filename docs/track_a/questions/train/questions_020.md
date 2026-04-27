# Track A 문제 분석 — train[190]~train[199]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[190] ~ train[199] (10개)

## 목차

1. [문제 190: `daaf33c0-3f1...`](#190) — single-answer, 정답: C15
2. [문제 191: `0bfc423f-1a5...`](#191) — single-answer, 정답: C17
3. [문제 192: `d109fada-1fb...`](#192) — single-answer, 정답: C12
4. [문제 193: `855d9ee6-106...`](#193) — multiple-answer, 정답: C3|C5
5. [문제 194: `d6fae17f-d30...`](#194) — multiple-answer, 정답: C3|C10|C19|C21
6. [문제 195: `65985739-0d7...`](#195) — single-answer, 정답: C7
7. [문제 196: `36ef8a0f-f52...`](#196) — single-answer, 정답: C9
8. [문제 197: `7ef76f7b-c3e...`](#197) — single-answer, 정답: C11
9. [문제 198: `9b37b9d1-fcd...`](#198) — single-answer, 정답: C20
10. [문제 199: `1cbf6751-d99...`](#199) — multiple-answer, 정답: C4|C20

---

### 문제 190: `daaf33c0-3f1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `daaf33c0-3f10-4061-9259-a29f9f3f5c81` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Add neighbor relationship between 3229300_1 and 3230670_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[190] topology](images/train_0190.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229300_1
- `C2`: Decrease A3 Offset threshold for 3229300_1
- `C3`: Increase transmission power for 3229300_1
- `C4`: Add neighbor relationship between 3260330_2 and 3230670_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229300_1
- `C6`: Adjust the azimuth of 3229300_1 by 50 degrees
- `C7`: Press down the tilt angle of 3229300_1 by 3 degrees
- `C8`: Lift the tilt angle of 3229300_1 by 3 degrees
- `C9`: Lift the tilt angle  of 3230670_3 by 4 degrees
- `C10`: Adjust the azimuth of 3230670_3 by 10 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230670_3
- `C12`: Increase transmission power for 3230670_3
- `C13`: Decrease transmission power for 3229300_1
- `C14`: Decrease A3 Offset threshold for 3230670_3
- `C15`: Add neighbor relationship between 3229300_1 and 3230670_3 **← 정답**
- `C16`: Press down the tilt angle  of 3230670_3 by 4 degrees
- `C17`: Increase A3 Offset threshold for 3229300_1
- `C18`: Decrease transmission power for 3230670_3
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase A3 Offset threshold for 3230670_3
- `C21`: Check test server and transmission issues
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230670_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.115 | MS1 | 121.4656739853 | 31.1446243063 | 501 | 504990 | -83.09 | 17.97 | 388.39 | 0.11 | 2.16 | 1592 |
| 2024-09-20 22:21:32.916 | MS1 | 121.4656703002 | 31.1446307664 | 501 | 504990 | -81.60 | 16.15 | 523.69 | 0.03 | 2.87 | 1591 |
| 2024-09-20 22:21:33.280 | MS1 | 121.4656730424 | 31.1446195700 | 501 | 504990 | -79.78 | 16.89 | 320.86 | 0.19 | 2.35 | 1593 |
| 2024-09-20 22:21:34.672 | MS1 | 121.4656685539 | 31.1446246909 | 501 | 504990 | -91.75 | -2.30 | 34.48 | 0.13 | 1.33 | 1599 |
| 2024-09-20 22:21:35.399 | MS1 | 121.4656756227 | 31.1446237193 | 501 | 504990 | -91.61 | -0.96 | 41.43 | 0.08 | 1.37 | 1579 |
| 2024-09-20 22:21:36.711 | MS1 | 121.4656742076 | 31.1446182707 | 501 | 504990 | -88.64 | -0.95 | 49.34 | 0.11 | 1.26 | 1600 |
| 2024-09-20 22:21:37.602 | MS1 | 121.4656584058 | 31.1446246917 | 501 | 504990 | -86.54 | -1.64 | 45.97 | 0.16 | 1.22 | 1592 |
| 2024-09-20 22:21:38.671 | MS1 | 121.4656670159 | 31.1446183488 | 501 | 504990 | -80.79 | 16.55 | 553.78 | 0.08 | 1.02 | 1563 |
| 2024-09-20 22:21:39.647 | MS1 | 121.4656732853 | 31.1446275819 | 501 | 504990 | -81.46 | 17.37 | 541.87 | 0.02 | 1.31 | 1588 |
| 2024-09-20 22:21:40.548 | MS1 | 121.4656650244 | 31.1446343352 | 501 | 504990 | -78.16 | 12.49 | 444.16 | 0.19 | 2.34 | 1572 |
| 2024-09-20 22:21:41.987 | MS1 | 121.4656767257 | 31.1446206064 | 501 | 504990 | -77.32 | 16.78 | 431.12 | 0.02 | 2.35 | 1589 |
| 2024-09-20 22:21:42.855 | MS1 | 121.4656769527 | 31.1446254457 | 501 | 504990 | -80.46 | 13.06 | 503.07 | 0.15 | 2.45 | 1566 |

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
| 3229300 | 1 | 121.4721081127 | 31.1484845007 | 114 | 1 | 8 | 24.8 | TDD | 501 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3230670 | 3 | 121.4720662293 | 31.1531953840 | 223 | 3 | 12 | 27.7 | TDD | 877 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3260330 | 2 | 121.4730701936 | 31.1492584093 | 322 | 3 | 11 | 17.3 | TDD | 548 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3271579 | 4 | 121.4719570371 | 31.1544865511 | 88 | 12 | 10 | 25.1 | TDD | 324 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.603 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.618 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.743 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.743 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.437 | NREventA3 | measId:2;ServCellPCI:874;Se... |
| 2024-09-20 22:21:36.437 | NREventA3 | measId:2;ServCellPCI:874;Se... |
| 2024-09-20 22:21:37.437 | NREventA3 | measId:2;ServCellPCI:874;Se... |
| 2024-09-20 22:21:39.937 | NRRRCReestablishAttempt | PCI:874 |
| 2024-09-20 22:21:39.951 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.964 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:40.084 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.084 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229300 | 1 | 13.5259 | 16.1595 | -115.4012 | 6.9901 | 87.6490 | 0.0144 | 0.1190 |
| 2024_09_20 22:00 | 3260330 | 2 | 7.7736 | 18.4230 | -116.1652 | 8.9886 | 162.8461 | 0.0032 | 0.0176 |
| 2024_09_20 22:00 | 3230670 | 3 | 13.0033 | 15.0553 | -117.8691 | 11.4443 | 131.5923 | 0.0180 | 0.0098 |
| 2024_09_20 22:00 | 3271579 | 4 | 13.3065 | 17.2962 | -115.0510 | 15.9123 | 164.0087 | 0.0180 | 0.0159 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416535_77B59547 | 504990 | 501 | -91.6 | 504990 | 877 | -87.7 | 504990 | 548 | -91.1 | 504990 | 324 |
| MR_1774416535_599FDAD3 | 504990 | 877 | -87.2 | 504990 | 501 | -91.4 | 504990 | 548 | -91.0 | 504990 | 324 |
| MR_1774416535_610930A1 | 504990 | 877 | -86.9 | 504990 | 501 | -91.0 | 504990 | 548 | -89.7 | 504990 | 324 |
| MR_1774416535_9EE743FD | 504990 | 877 | -86.7 | 504990 | 501 | -91.4 | 504990 | 548 | -90.0 | 504990 | 324 |
| MR_1774416535_EE6B47E4 | 504990 | 501 | -92.3 | 504990 | 877 | -87.7 | 504990 | 548 | -91.4 | 504990 | 324 |
| MR_1774416535_93878B40 | 504990 | 501 | -91.2 | 504990 | 877 | -87.9 | 504990 | 548 | -91.3 | 504990 | 324 |
| MR_1774416535_02175905 | 504990 | 877 | -85.2 | 504990 | 501 | -92.4 | 504990 | 548 | -90.7 | 504990 | 324 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 191: `0bfc423f-1a5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0bfc423f-1a58-412c-b0ff-10319bd9482d` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Add neighbor relationship between 3277963_4 and 3264470_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[191] topology](images/train_0191.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3277963_4
- `C2`: Decrease transmission power for 3264470_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277963_4
- `C4`: Lift the tilt angle  of 3264470_1 by 6 degrees
- `C5`: Adjust the azimuth of 3264470_1 by 33 degrees
- `C6`: Adjust the azimuth of 3277963_4 by 50 degrees
- `C7`: Increase transmission power for 3264470_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264470_1
- `C10`: Increase A3 Offset threshold for 3264470_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264470_1
- `C12`: Decrease A3 Offset threshold for 3264470_1
- `C13`: Increase A3 Offset threshold for 3277963_4
- `C14`: Press down the tilt angle  of 3264470_1 by 6 degrees
- `C15`: Check test server and transmission issues
- `C16`: Lift the tilt angle of 3277963_4 by 7 degrees
- `C17`: Add neighbor relationship between 3277963_4 and 3264470_1 **← 정답**
- `C18`: Press down the tilt angle of 3277963_4 by 7 degrees
- `C19`: Decrease A3 Offset threshold for 3277963_4
- `C20`: Decrease transmission power for 3277963_4
- `C21`: Add neighbor relationship between 3227101_3 and 3264470_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277963_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.241 | MS1 | 121.4656704669 | 31.1446361273 | 447 | 504990 | -84.01 | 17.57 | 581.74 | 0.08 | 2.22 | 1571 |
| 2024-09-20 22:21:32.561 | MS1 | 121.4656724331 | 31.1446363396 | 447 | 504990 | -81.77 | 17.88 | 578.01 | 0.01 | 2.93 | 1561 |
| 2024-09-20 22:21:33.544 | MS1 | 121.4656757095 | 31.1446193503 | 447 | 504990 | -76.07 | 15.62 | 383.54 | 0.10 | 2.70 | 1586 |
| 2024-09-20 22:21:34.427 | MS1 | 121.4656639996 | 31.1446184931 | 447 | 504990 | -87.45 | -2.10 | 39.54 | 0.16 | 1.48 | 1580 |
| 2024-09-20 22:21:35.130 | MS1 | 121.4656657450 | 31.1446278190 | 447 | 504990 | -88.95 | -0.22 | 59.45 | 0.07 | 1.21 | 1560 |
| 2024-09-20 22:21:36.627 | MS1 | 121.4656710067 | 31.1446340619 | 447 | 504990 | -90.16 | -3.33 | 61.44 | 0.02 | 1.47 | 1573 |
| 2024-09-20 22:21:37.445 | MS1 | 121.4656651356 | 31.1446352458 | 447 | 504990 | -89.49 | -1.65 | 71.77 | 0.08 | 1.17 | 1561 |
| 2024-09-20 22:21:38.191 | MS1 | 121.4656600098 | 31.1446205312 | 447 | 504990 | -76.43 | 16.18 | 495.51 | 0.19 | 1.06 | 1582 |
| 2024-09-20 22:21:39.923 | MS1 | 121.4656593197 | 31.1446191956 | 447 | 504990 | -84.94 | 14.50 | 583.82 | 0.11 | 1.47 | 1584 |
| 2024-09-20 22:21:40.602 | MS1 | 121.4656604341 | 31.1446344275 | 447 | 504990 | -84.49 | 15.74 | 435.06 | 0.17 | 2.84 | 1578 |
| 2024-09-20 22:21:41.309 | MS1 | 121.4656726281 | 31.1446293928 | 447 | 504990 | -83.34 | 12.12 | 358.06 | 0.17 | 2.99 | 1583 |
| 2024-09-20 22:21:42.495 | MS1 | 121.4656726275 | 31.1446261795 | 447 | 504990 | -83.75 | 14.98 | 390.64 | 0.09 | 2.03 | 1573 |

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
| 3227079 | 2 | 121.4671062137 | 31.1547041981 | 228 | 8 | 0 | 21.3 | TDD | 454 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3227101 | 3 | 121.4657128437 | 31.1462147223 | 270 | 2 | 6 | 35.4 | TDD | 374 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3264470 | 1 | 121.4746640966 | 31.1501179891 | 267 | 3 | 6 | 46.0 | TDD | 702 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3277963 | 4 | 121.4713151405 | 31.1512100270 | 114 | 4 | 11 | 42.3 | TDD | 447 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.621 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.744 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.744 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.489 | NREventA3 | measId:2;ServCellPCI:821;Se... |
| 2024-09-20 22:21:36.489 | NREventA3 | measId:2;ServCellPCI:821;Se... |
| 2024-09-20 22:21:37.489 | NREventA3 | measId:2;ServCellPCI:821;Se... |
| 2024-09-20 22:21:39.989 | NRRRCReestablishAttempt | PCI:821 |
| 2024-09-20 22:21:40.004 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:40.014 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:40.156 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.156 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264470 | 1 | 5.9003 | 17.1274 | -115.0155 | 14.6142 | 94.1919 | 0.0169 | 0.0171 |
| 2024_09_20 22:00 | 3227079 | 2 | 7.0862 | 18.7395 | -114.5434 | 8.8090 | 187.3516 | 0.0044 | 0.0051 |
| 2024_09_20 22:00 | 3227101 | 3 | 8.9307 | 13.6039 | -116.7895 | 14.9988 | 99.8877 | 0.0057 | 0.0107 |
| 2024_09_20 22:00 | 3277963 | 4 | 17.4365 | 15.4732 | -116.1929 | 15.0194 | 171.7879 | 0.0072 | 0.1475 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416837_C040584B | 504990 | 447 | -88.3 | 504990 | 702 | -83.0 | 504990 | 374 | -85.8 | 504990 | 454 |
| MR_1774416837_B683E9A6 | 504990 | 702 | -80.2 | 504990 | 447 | -87.7 | 504990 | 374 | -86.8 | 504990 | 454 |
| MR_1774416837_0322AF98 | 504990 | 702 | -83.0 | 504990 | 447 | -87.8 | 504990 | 374 | -84.4 | 504990 | 454 |
| MR_1774416837_51E4E0D9 | 504990 | 702 | -83.3 | 504990 | 447 | -86.2 | 504990 | 374 | -86.2 | 504990 | 454 |
| MR_1774416837_91F60A7A | 504990 | 447 | -89.4 | 504990 | 702 | -82.7 | 504990 | 374 | -83.7 | 504990 | 454 |
| MR_1774416837_A4C5F3F0 | 504990 | 447 | -89.1 | 504990 | 702 | -82.2 | 504990 | 374 | -84.7 | 504990 | 454 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 192: `d109fada-1fb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d109fada-1fba-437c-ade0-94e341adda23` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[192] topology](images/train_0192.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3244140_1 by 6 degrees
- `C2`: Add neighbor relationship between 3244140_1 and 3227514_3
- `C3`: Increase transmission power for 3244140_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244140_1
- `C5`: Add neighbor relationship between 3264768_4 and 3227514_3
- `C6`: Increase A3 Offset threshold for 3227514_3
- `C7`: Decrease A3 Offset threshold for 3244140_1
- `C8`: Decrease transmission power for 3227514_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244140_1
- `C10`: Increase A3 Offset threshold for 3244140_1
- `C11`: Adjust the azimuth of 3244140_1 by 50 degrees
- `C12`: Check test server and transmission issues **← 정답**
- `C13`: Decrease transmission power for 3244140_1
- `C14`: Lift the tilt angle of 3244140_1 by 6 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227514_3
- `C16`: Lift the tilt angle  of 3227514_3 by 4 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227514_3
- `C18`: Increase transmission power for 3227514_3
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Press down the tilt angle  of 3227514_3 by 4 degrees
- `C21`: Adjust the azimuth of 3227514_3 by 15 degrees
- `C22`: Decrease A3 Offset threshold for 3227514_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.354 | MS1 | 121.4656718802 | 31.1446338669 | 525 | 504990 | -85.97 | 16.02 | 371.97 | 0.10 | 2.97 | 1569 |
| 2024-09-20 22:21:32.290 | MS1 | 121.4656670660 | 31.1446345091 | 525 | 504990 | -87.61 | 14.54 | 494.77 | 0.04 | 2.88 | 1578 |
| 2024-09-20 22:21:33.399 | MS1 | 121.4656688683 | 31.1446213696 | 525 | 504990 | -89.62 | 16.14 | 333.57 | 0.07 | 2.58 | 1584 |
| 2024-09-20 22:21:34.191 | MS1 | 121.4656688700 | 31.1446235595 | 525 | 504990 | -88.40 | 16.81 | 70.68 | 0.05 | 2.99 | 467 |
| 2024-09-20 22:21:35.289 | MS1 | 121.4656668132 | 31.1446310507 | 525 | 504990 | -90.39 | 12.02 | 102.21 | 0.10 | 2.58 | 369 |
| 2024-09-20 22:21:36.265 | MS1 | 121.4656751216 | 31.1446301119 | 525 | 504990 | -90.63 | 13.38 | 84.55 | 0.15 | 2.40 | 409 |
| 2024-09-20 22:21:37.421 | MS1 | 121.4656777166 | 31.1446274269 | 525 | 504990 | -91.76 | 12.34 | 75.88 | 0.03 | 2.26 | 334 |
| 2024-09-20 22:21:38.599 | MS1 | 121.4656724601 | 31.1446213697 | 525 | 504990 | -93.90 | 9.21 | 66.77 | 0.03 | 2.75 | 335 |
| 2024-09-20 22:21:39.170 | MS1 | 121.4656713478 | 31.1446263712 | 525 | 504990 | -92.25 | 10.82 | 79.36 | 0.05 | 2.53 | 302 |
| 2024-09-20 22:21:40.267 | MS1 | 121.4656739897 | 31.1446287126 | 525 | 504990 | -89.43 | 10.65 | 490.39 | 0.07 | 2.09 | 1593 |
| 2024-09-20 22:21:41.444 | MS1 | 121.4656742819 | 31.1446226495 | 525 | 504990 | -93.43 | 7.57 | 317.16 | 0.11 | 2.29 | 1600 |
| 2024-09-20 22:21:42.866 | MS1 | 121.4656650917 | 31.1446334172 | 525 | 504990 | -91.37 | 9.15 | 455.42 | 0.02 | 2.24 | 1572 |

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
| 3227514 | 3 | 121.4735203257 | 31.1503531247 | 215 | 1 | 12 | 48.8 | TDD | 661 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3244140 | 1 | 121.4653089848 | 31.1462875200 | 113 | 1 | 1 | 15.2 | TDD | 525 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3264768 | 4 | 121.4674736700 | 31.1552597775 | 12 | 0 | 1 | 25.9 | TDD | 782 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3267799 | 2 | 121.4733093230 | 31.1509434735 | 139 | 3 | 6 | 16.9 | TDD | 917 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.475 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.497 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.621 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.621 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.337 | NREventA3 | measId:2;ServCellPCI:403;Se... |
| 2024-09-20 22:21:38.577 | NRHandoverAttempt | SourcePCI:403;SourceNR-ARFC... |
| 2024-09-20 22:21:38.627 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.640 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.778 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.778 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244140 | 1 | 11.8400 | 14.0025 | -114.7982 | 18.7007 | 198.5712 | 0.0033 | 0.0173 |
| 2024_09_20 22:00 | 3267799 | 2 | 15.8570 | 17.5257 | -117.8347 | 6.7093 | 182.5012 | 0.0179 | 0.0187 |
| 2024_09_20 22:00 | 3227514 | 3 | 13.2162 | 9.3349 | -117.6301 | 13.7415 | 89.8965 | 0.0143 | 0.0107 |
| 2024_09_20 22:00 | 3264768 | 4 | 14.7553 | 9.6724 | -115.0786 | 8.2515 | 99.8741 | 0.0194 | 0.0056 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415218_CBA6E752 | 504990 | 525 | -88.4 | 504990 | 661 | -96.7 | 504990 | 782 | -102.7 | 504990 | 917 |
| MR_1774415218_3705AFEA | 504990 | 525 | -89.6 | 504990 | 661 | -96.5 | 504990 | 782 | -99.8 | 504990 | 917 |
| MR_1774415218_014AEAAD | 504990 | 525 | -86.5 | 504990 | 661 | -97.7 | 504990 | 782 | -100.6 | 504990 | 917 |
| MR_1774415218_D3E3E3FA | 504990 | 525 | -90.0 | 504990 | 661 | -98.5 | 504990 | 782 | -101.0 | 504990 | 917 |
| MR_1774415218_F429681B | 504990 | 525 | -86.6 | 504990 | 661 | -97.4 | 504990 | 782 | -99.4 | 504990 | 917 |
| MR_1774415218_8458AD41 | 504990 | 525 | -88.4 | 504990 | 661 | -95.4 | 504990 | 782 | -102.5 | 504990 | 917 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 193: `855d9ee6-106...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `855d9ee6-1063-40c8-946a-fc6fdc87224c` |
| Tag | **multiple-answer** |
| 정답 | **C3|C5** |
| C3 의미 | Increase transmission power for 3245711_3 |
| C5 의미 | Adjust the azimuth of 3245711_3 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[193] topology](images/train_0193.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245711_3
- `C2`: Increase A3 Offset threshold for 3245711_3
- `C3`: Increase transmission power for 3245711_3 **← 정답**
- `C4`: Check test server and transmission issues
- `C5`: Adjust the azimuth of 3245711_3 by 50 degrees **← 정답**
- `C6`: Decrease A3 Offset threshold for 3245711_3
- `C7`: Add neighbor relationship between 3261082_4 and 3247235_2
- `C8`: Decrease transmission power for 3247235_2
- `C9`: Press down the tilt angle of 3245711_3 by 10 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247235_2
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Lift the tilt angle of 3245711_3 by 10 degrees
- `C13`: Decrease transmission power for 3245711_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245711_3
- `C15`: Add neighbor relationship between 3245711_3 and 3247235_2
- `C16`: Adjust the azimuth of 3247235_2 by 10 degrees
- `C17`: Increase transmission power for 3247235_2
- `C18`: Press down the tilt angle  of 3247235_2 by 6 degrees
- `C19`: Lift the tilt angle  of 3247235_2 by 6 degrees
- `C20`: Decrease A3 Offset threshold for 3247235_2
- `C21`: Increase A3 Offset threshold for 3247235_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247235_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.479 | MS1 | 121.4656645586 | 31.1446371705 | 575 | 504990 | -87.24 | 15.28 | 395.15 | 0.07 | 2.73 | 1592 |
| 2024-09-20 22:21:32.985 | MS1 | 121.4656603128 | 31.1446341724 | 575 | 504990 | -89.40 | 14.34 | 471.59 | 0.15 | 2.44 | 1581 |
| 2024-09-20 22:21:33.971 | MS1 | 121.4656605970 | 31.1446250468 | 575 | 504990 | -90.72 | 15.64 | 335.40 | 0.08 | 2.89 | 1570 |
| 2024-09-20 22:21:34.354 | MS1 | 121.4656689278 | 31.1446180404 | 575 | 504990 | -100.96 | -0.30 | 44.41 | 0.09 | 1.00 | 1595 |
| 2024-09-20 22:21:35.620 | MS1 | 121.4656599840 | 31.1446207446 | 575 | 504990 | -101.34 | 1.26 | 66.97 | 0.16 | 1.27 | 1584 |
| 2024-09-20 22:21:36.438 | MS1 | 121.4656624664 | 31.1446301959 | 575 | 504990 | -100.88 | 1.85 | 76.22 | 0.17 | 1.07 | 1569 |
| 2024-09-20 22:21:37.558 | MS1 | 121.4656644631 | 31.1446373803 | 575 | 504990 | -100.85 | 0.35 | 37.94 | 0.19 | 1.08 | 1589 |
| 2024-09-20 22:21:38.195 | MS1 | 121.4656759151 | 31.1446224725 | 575 | 504990 | -101.73 | 1.95 | 52.94 | 0.08 | 1.09 | 1579 |
| 2024-09-20 22:21:39.277 | MS1 | 121.4656616137 | 31.1446193692 | 575 | 504990 | -107.08 | 1.25 | 66.12 | 0.14 | 1.36 | 1561 |
| 2024-09-20 22:21:40.465 | MS1 | 121.4656672744 | 31.1446308368 | 575 | 504990 | -92.35 | 12.16 | 507.81 | 0.13 | 2.60 | 1583 |
| 2024-09-20 22:21:41.510 | MS1 | 121.4656708778 | 31.1446375064 | 575 | 504990 | -88.05 | 14.01 | 314.21 | 0.20 | 2.72 | 1581 |
| 2024-09-20 22:21:42.531 | MS1 | 121.4656639427 | 31.1446369321 | 575 | 504990 | -91.98 | 17.15 | 588.24 | 0.16 | 2.11 | 1569 |

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
| 3228293 | 1 | 121.4694152452 | 31.1528446148 | 115 | 1 | 0 | 29.1 | TDD | 416 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3245711 | 3 | 121.4688409882 | 31.1505750934 | 133 | 12 | 7 | 17.1 | TDD | 575 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3247235 | 2 | 121.4753624020 | 31.1473070287 | 242 | 3 | 12 | 48.1 | TDD | 676 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3261082 | 4 | 121.4748296067 | 31.1548149419 | 252 | 15 | 11 | 27.5 | TDD | 47 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.494 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.494 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.657 | NREventA2 | measId:1;ServCellPCI:705;Se... |
| 2024-09-20 22:21:34.767 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228293 | 1 | 11.2129 | 6.1738 | -116.8792 | 14.1282 | 197.5253 | 0.0099 | 0.0060 |
| 2024_09_20 22:00 | 3247235 | 2 | 6.7179 | 17.9922 | -114.2533 | 6.5200 | 177.5690 | 0.0069 | 0.0078 |
| 2024_09_20 22:00 | 3245711 | 3 | 15.2913 | 9.3126 | -115.8438 | 11.6514 | 122.4302 | 0.1419 | 0.0180 |
| 2024_09_20 22:00 | 3261082 | 4 | 9.0162 | 9.0344 | -115.1021 | 19.1041 | 150.1561 | 0.0105 | 0.0046 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416897_978AE1CB | 504990 | 575 | -99.1 | 504990 | 676 | -108.0 | 504990 | 47 | -113.3 | 504990 | 416 |
| MR_1774416897_97D4B66C | 504990 | 575 | -101.3 | 504990 | 676 | -107.0 | 504990 | 47 | -113.0 | 504990 | 416 |
| MR_1774416897_D2DD92C8 | 504990 | 575 | -102.2 | 504990 | 676 | -106.1 | 504990 | 47 | -111.4 | 504990 | 416 |
| MR_1774416897_56B77F43 | 504990 | 575 | -101.0 | 504990 | 676 | -106.7 | 504990 | 47 | -112.5 | 504990 | 416 |
| MR_1774416897_8A831511 | 504990 | 575 | -101.4 | 504990 | 676 | -105.9 | 504990 | 47 | -111.7 | 504990 | 416 |
| MR_1774416897_B7E2AE8B | 504990 | 575 | -102.2 | 504990 | 676 | -108.8 | 504990 | 47 | -112.8 | 504990 | 416 |
| MR_1774416897_7E308595 | 504990 | 575 | -99.9 | 504990 | 676 | -105.4 | 504990 | 47 | -113.7 | 504990 | 416 |
| MR_1774416897_81800574 | 504990 | 575 | -100.4 | 504990 | 676 | -106.9 | 504990 | 47 | -113.5 | 504990 | 416 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 194: `d6fae17f-d30...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d6fae17f-d308-4353-a0a9-9173ea702491` |
| Tag | **multiple-answer** |
| 정답 | **C3|C10|C19|C21** |
| C3 의미 | Increase A3 Offset threshold for 3270965_3 |
| C10 의미 | Decrease transmission power for 3257926_4 |
| C19 의미 | Increase A3 Offset threshold for 3257926_4 |
| C21 의미 | Press down the tilt angle  of 3257926_4 by 2 degrees |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[194] topology](images/train_0194.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3270965_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270965_3
- `C3`: Increase A3 Offset threshold for 3270965_3 **← 정답**
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270965_3
- `C5`: Increase transmission power for 3257926_4
- `C6`: Adjust the azimuth of 3257926_4 by 0 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257926_4
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Lift the tilt angle  of 3257926_4 by 2 degrees
- `C10`: Decrease transmission power for 3257926_4 **← 정답**
- `C11`: Check test server and transmission issues
- `C12`: Decrease A3 Offset threshold for 3270965_3
- `C13`: Adjust the azimuth of 3270965_3 by 7 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257926_4
- `C15`: Decrease transmission power for 3270965_3
- `C16`: Decrease A3 Offset threshold for 3257926_4
- `C17`: Press down the tilt angle of 3270965_3 by 4 degrees
- `C18`: Add neighbor relationship between 3274057_5 and 3257926_4
- `C19`: Increase A3 Offset threshold for 3257926_4 **← 정답**
- `C20`: Add neighbor relationship between 3270965_3 and 3257926_4
- `C21`: Press down the tilt angle  of 3257926_4 by 2 degrees **← 정답**
- `C22`: Lift the tilt angle of 3270965_3 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.294 | MS1 | 121.4656710843 | 31.1446201588 | 233 | 504990 | -79.38 | 13.90 | 465.44 | 0.04 | 2.48 | 1575 |
| 2024-09-20 22:21:32.700 | MS1 | 121.4656744729 | 31.1446312509 | 233 | 504990 | -75.12 | 17.73 | 565.78 | 0.19 | 2.82 | 1600 |
| 2024-09-20 22:21:33.434 | MS1 | 121.4656649863 | 31.1446272400 | 233 | 504990 | -84.26 | 13.67 | 338.65 | 0.19 | 2.27 | 1584 |
| 2024-09-20 22:21:34.986 | MS1 | 121.4656722740 | 31.1446280353 | 359 | 504990 | -87.85 | 3.48 | 54.85 | 0.04 | 1.25 | 1593 |
| 2024-09-20 22:21:35.184 | MS1 | 121.4656743802 | 31.1446343272 | 359 | 504990 | -88.88 | 3.05 | 64.64 | 0.03 | 1.26 | 1583 |
| 2024-09-20 22:21:36.497 | MS1 | 121.4656688769 | 31.1446357436 | 233 | 504990 | -84.73 | 1.65 | 48.70 | 0.10 | 1.11 | 1574 |
| 2024-09-20 22:21:37.261 | MS1 | 121.4656637766 | 31.1446283064 | 233 | 504990 | -88.99 | 1.69 | 49.56 | 0.04 | 1.15 | 1582 |
| 2024-09-20 22:21:38.388 | MS1 | 121.4656771946 | 31.1446209295 | 359 | 504990 | -88.69 | 1.19 | 28.35 | 0.05 | 1.17 | 1563 |
| 2024-09-20 22:21:39.535 | MS1 | 121.4656642280 | 31.1446363364 | 359 | 504990 | -87.10 | 2.95 | 61.18 | 0.15 | 1.26 | 1580 |
| 2024-09-20 22:21:40.904 | MS1 | 121.4656632281 | 31.1446184411 | 359 | 504990 | -79.48 | 12.76 | 344.41 | 0.07 | 2.60 | 1599 |
| 2024-09-20 22:21:41.819 | MS1 | 121.4656628939 | 31.1446370142 | 359 | 504990 | -81.11 | 12.84 | 553.82 | 0.08 | 2.89 | 1577 |
| 2024-09-20 22:21:42.895 | MS1 | 121.4656767757 | 31.1446226597 | 359 | 504990 | -80.31 | 12.75 | 431.32 | 0.12 | 2.80 | 1560 |

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
| 3257926 | 4 | 121.4686854341 | 31.1486858774 | 212 | 0 | 1 | 15.7 | TDD | 817 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3270965 | 3 | 121.4692183665 | 31.1541741366 | 205 | 3 | 1 | 24.2 | TDD | 233 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3272447 | 1 | 121.4758156155 | 31.1527077544 | 308 | 13 | 6 | 25.4 | TDD | 65 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3274057 | 5 | 121.4703365210 | 31.1492973967 | 108 | 11 | 1 | 39.4 | TDD | 470 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3278884 | 2 | 121.4728329607 | 31.1477686856 | 151 | 8 | 3 | 23.5 | TDD | 359 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.987 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.004 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.133 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.133 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.837 | NREventA3 | measId:2;ServCellPCI:285;Se... |
| 2024-09-20 22:21:34.077 | NRHandoverAttempt | SourcePCI:285;SourceNR-ARFC... |
| 2024-09-20 22:21:34.126 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.137 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:34.252 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.252 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.837 | NREventA3 | measId:2;ServCellPCI:12;Ser... |
| 2024-09-20 22:21:36.077 | NRHandoverAttempt | SourcePCI:12;SourceNR-ARFCN... |
| 2024-09-20 22:21:36.127 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.139 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:36.247 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.247 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.837 | NREventA3 | measId:2;ServCellPCI:285;Se... |
| 2024-09-20 22:21:38.077 | NRHandoverAttempt | SourcePCI:285;SourceNR-ARFC... |
| 2024-09-20 22:21:38.127 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.140 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.244 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.244 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272447 | 1 | 10.1301 | 15.4838 | -114.9782 | 14.4265 | 168.9657 | 0.0000 | 0.0107 |
| 2024_09_20 22:00 | 3278884 | 2 | 5.8577 | 15.2934 | -114.5234 | 9.9613 | 135.7889 | 0.0194 | 0.0067 |
| 2024_09_20 22:00 | 3270965 | 3 | 12.6253 | 7.1121 | -114.6482 | 19.2880 | 95.4338 | 0.0021 | 0.0124 |
| 2024_09_20 22:00 | 3257926 | 4 | 14.3062 | 12.2500 | -115.8000 | 12.7046 | 192.6030 | 0.0094 | 0.0183 |
| 2024_09_20 22:00 | 3274057 | 5 | 8.6086 | 7.5451 | -115.1155 | 9.6991 | 186.5366 | 0.0026 | 0.0010 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412381_164CF04C | 504990 | 359 | -88.8 | 504990 | 233 | -86.0 | 504990 | 817 | -84.4 | 504990 | 470 |
| MR_1774412381_8EC6DE6F | 504990 | 233 | -87.8 | 504990 | 359 | -87.1 | 504990 | 817 | -84.1 | 504990 | 470 |
| MR_1774412381_5844BC48 | 504990 | 359 | -85.9 | 504990 | 233 | -85.4 | 504990 | 817 | -84.9 | 504990 | 470 |
| MR_1774412381_18E5B532 | 504990 | 359 | -88.2 | 504990 | 233 | -85.9 | 504990 | 817 | -84.7 | 504990 | 470 |
| MR_1774412381_9AACA92F | 504990 | 359 | -88.6 | 504990 | 233 | -86.5 | 504990 | 817 | -86.4 | 504990 | 470 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 195: `65985739-0d7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `65985739-0d7f-4762-b6db-658df1b99b36` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[195] topology](images/train_0195.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3279753_1 and 3239725_2
- `C2`: Increase transmission power for 3239725_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239725_2
- `C4`: Lift the tilt angle of 3279753_1 by 10 degrees
- `C5`: Adjust the azimuth of 3239725_2 by 34 degrees
- `C6`: Add neighbor relationship between 3234637_4 and 3239725_2
- `C7`: Insufficient data; more data is needed for judgment. **← 정답**
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279753_1
- `C9`: Decrease A3 Offset threshold for 3279753_1
- `C10`: Decrease A3 Offset threshold for 3239725_2
- `C11`: Increase A3 Offset threshold for 3239725_2
- `C12`: Increase transmission power for 3279753_1
- `C13`: Press down the tilt angle of 3279753_1 by 10 degrees
- `C14`: Decrease transmission power for 3239725_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279753_1
- `C16`: Adjust the azimuth of 3279753_1 by 43 degrees
- `C17`: Check test server and transmission issues
- `C18`: Lift the tilt angle  of 3239725_2 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3279753_1
- `C20`: Decrease transmission power for 3279753_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239725_2
- `C22`: Press down the tilt angle  of 3239725_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.208 | MS1 | 121.4656645755 | 31.1446363926 | 680 | 504990 | -88.47 | 16.81 | 501.73 | 0.06 | 2.09 | 1562 |
| 2024-09-20 22:21:32.715 | MS1 | 121.4656769958 | 31.1446329142 | 680 | 504990 | -86.82 | 14.30 | 416.50 | 0.17 | 2.62 | 1571 |
| 2024-09-20 22:21:33.842 | MS1 | 121.4656634210 | 31.1446247531 | 680 | 504990 | -91.29 | 16.01 | 470.27 | 0.17 | 2.31 | 1591 |
| 2024-09-20 22:21:34.987 | MS1 | 121.4656723908 | 31.1446217043 | 680 | 504990 | -85.33 | 13.47 | 59.01 | 0.10 | 2.38 | 1578 |
| 2024-09-20 22:21:35.938 | MS1 | 121.4656727316 | 31.1446200313 | 680 | 504990 | -90.01 | 17.44 | 87.28 | 0.17 | 2.36 | 1591 |
| 2024-09-20 22:21:36.532 | MS1 | 121.4656599240 | 31.1446283440 | 680 | 504990 | -90.19 | 15.03 | 84.56 | 0.06 | 2.38 | 1599 |
| 2024-09-20 22:21:37.450 | MS1 | 121.4656608550 | 31.1446199559 | 680 | 504990 | -92.33 | 11.13 | 84.04 | 0.00 | 2.89 | 1598 |
| 2024-09-20 22:21:38.952 | MS1 | 121.4656588375 | 31.1446253018 | 680 | 504990 | -90.68 | 10.96 | 67.02 | 0.07 | 2.01 | 1596 |
| 2024-09-20 22:21:39.915 | MS1 | 121.4656640764 | 31.1446292246 | 680 | 504990 | -89.89 | 7.56 | 90.20 | 0.07 | 2.80 | 1596 |
| 2024-09-20 22:21:40.299 | MS1 | 121.4656690162 | 31.1446284065 | 680 | 504990 | -90.05 | 11.27 | 469.34 | 0.10 | 2.19 | 1575 |
| 2024-09-20 22:21:41.258 | MS1 | 121.4656691730 | 31.1446355659 | 680 | 504990 | -90.50 | 11.60 | 355.68 | 0.08 | 2.69 | 1589 |
| 2024-09-20 22:21:42.315 | MS1 | 121.4656643883 | 31.1446236208 | 680 | 504990 | -91.28 | 8.44 | 378.68 | 0.05 | 2.25 | 1582 |

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
| 3228648 | 3 | 121.4751389897 | 31.1541847362 | 276 | 7 | 11 | 30.2 | TDD | 648 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3234637 | 4 | 121.4727296932 | 31.1506457560 | 190 | 10 | 6 | 17.7 | TDD | 399 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3239725 | 2 | 121.4651597048 | 31.1453990429 | 185 | 13 | 11 | 30.9 | TDD | 511 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3279753 | 1 | 121.4680307930 | 31.1440173119 | 330 | 15 | 2 | 23.6 | TDD | 680 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.617 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.636 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.782 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.782 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.486 | NREventA3 | measId:2;ServCellPCI:22;Ser... |
| 2024-09-20 22:21:38.726 | NRHandoverAttempt | SourcePCI:22;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.766 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.777 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.923 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.923 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3279753 | 1 | 89.6669 | 75.3377 | -115.7192 | 13.0796 | 87.1193 | 0.0102 | 0.0039 |
| 2024_09_19 22:00 | 3239725 | 2 | 79.5095 | 81.0054 | -116.4717 | 8.5574 | 187.1981 | 0.0059 | 0.0012 |
| 2024_09_19 22:00 | 3228648 | 3 | 75.5172 | 86.3962 | -114.3622 | 12.5943 | 105.6069 | 0.0131 | 0.0045 |
| 2024_09_19 22:00 | 3234637 | 4 | 94.9744 | 87.3422 | -116.5631 | 12.8552 | 96.6038 | 0.0142 | 0.0039 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413438_A532EAE9 | 504990 | 680 | -86.0 | 504990 | 511 | -84.6 | 504990 | 399 | -96.8 | 504990 | 648 |
| MR_1774413438_2EE27C38 | 504990 | 680 | -86.2 | 504990 | 511 | -86.1 | 504990 | 399 | -96.7 | 504990 | 648 |
| MR_1774413438_58AFC78B | 504990 | 680 | -84.0 | 504990 | 511 | -86.3 | 504990 | 399 | -96.2 | 504990 | 648 |
| MR_1774413438_40870BB6 | 504990 | 680 | -85.2 | 504990 | 511 | -84.3 | 504990 | 399 | -94.7 | 504990 | 648 |
| MR_1774413438_DDF25C73 | 504990 | 680 | -85.9 | 504990 | 511 | -86.8 | 504990 | 399 | -95.9 | 504990 | 648 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 196: `36ef8a0f-f52...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `36ef8a0f-f525-421e-bb2e-0794e404a23b` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253849_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[196] topology](images/train_0196.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3264991_4 by 6 degrees
- `C2`: Adjust the azimuth of 3264991_4 by 34 degrees
- `C3`: Increase transmission power for 3264991_4
- `C4`: Lift the tilt angle of 3253849_5 by 4 degrees
- `C5`: Decrease A3 Offset threshold for 3264991_4
- `C6`: Increase A3 Offset threshold for 3264991_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264991_4
- `C8`: Adjust the azimuth of 3253849_5 by 41 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253849_5 **← 정답**
- `C10`: Press down the tilt angle of 3253849_5 by 4 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253849_5
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264991_4
- `C13`: Decrease A3 Offset threshold for 3253849_5
- `C14`: Increase A3 Offset threshold for 3253849_5
- `C15`: Add neighbor relationship between 3272026_13 and 3264991_4
- `C16`: Decrease transmission power for 3264991_4
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease transmission power for 3253849_5
- `C19`: Increase transmission power for 3253849_5
- `C20`: Press down the tilt angle  of 3264991_4 by 6 degrees
- `C21`: Check test server and transmission issues
- `C22`: Add neighbor relationship between 3253849_5 and 3264991_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.183 | MS1 | 121.4656657689 | 31.1446214483 | 237 | 504990 | -93.10 | 13.42 | 518.09 | 0.15 | 2.16 | 1584 |
| 2024-09-20 22:21:32.389 | MS1 | 121.4656592119 | 31.1446303051 | 807 | 504990 | -93.23 | 13.23 | 406.95 | 0.14 | 2.80 | 1597 |
| 2024-09-20 22:21:33.556 | MS1 | 121.4656634577 | 31.1446261186 | 89 | 504990 | -94.56 | 10.52 | 484.21 | 0.07 | 2.60 | 1583 |
| 2024-09-20 22:21:34.877 | MS1 | 121.4656666326 | 31.1446225342 | 455 | 152650 | -92.16 | 7.28 | 87.72 | 0.01 | 1.81 | 996 |
| 2024-09-20 22:21:35.848 | MS1 | 121.4656649157 | 31.1446190101 | 981 | 152650 | -95.76 | 4.89 | 53.95 | 0.18 | 1.98 | 987 |
| 2024-09-20 22:21:36.995 | MS1 | 121.4656741474 | 31.1446284926 | 313 | 152650 | -94.72 | 5.43 | 58.11 | 0.16 | 1.53 | 924 |
| 2024-09-20 22:21:37.382 | MS1 | 121.4656752685 | 31.1446281703 | 43 | 152650 | -89.72 | 5.79 | 77.84 | 0.13 | 1.89 | 964 |
| 2024-09-20 22:21:38.151 | MS1 | 121.4656753641 | 31.1446314522 | 455 | 152650 | -95.80 | 6.96 | 104.27 | 0.15 | 1.88 | 992 |
| 2024-09-20 22:21:39.389 | MS1 | 121.4656706474 | 31.1446331987 | 981 | 152650 | -87.67 | 7.14 | 73.48 | 0.08 | 1.87 | 974 |
| 2024-09-20 22:21:40.527 | MS1 | 121.4656698351 | 31.1446226336 | 313 | 152650 | -92.69 | 4.06 | 43.32 | 0.12 | 2.14 | 1578 |
| 2024-09-20 22:21:41.412 | MS1 | 121.4656607109 | 31.1446347781 | 43 | 152650 | -92.14 | 4.90 | 67.70 | 0.02 | 2.57 | 1581 |
| 2024-09-20 22:21:42.754 | MS1 | 121.4656623086 | 31.1446207921 | 455 | 152650 | -91.31 | 4.29 | 83.66 | 0.20 | 2.82 | 1563 |

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
| 3220798 | 1 | 121.4682403355 | 31.1503748325 | 93 | 12 | 9 | 13.9 | TDD | 98 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3225853 | 6 | 121.4746569429 | 31.1544854643 | 283 | 11 | 9 | 15.2 | TDD | 89 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3226050 | 10 | 121.4681812530 | 31.1469283831 | 19 | 5 | 3 | 24.7 | FDD | 981 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3228894 | 3 | 121.4680905369 | 31.1457997797 | 298 | 8 | 5 | 8.5 | TDD | 807 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3229648 | 12 | 121.4667662416 | 31.1542760919 | 325 | 1 | 2 | 22.8 | FDD | 344 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3238150 | 8 | 121.4649892936 | 31.1455246661 | 122 | 14 | 12 | 27.9 | FDD | 43 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3246329 | 9 | 121.4749994972 | 31.1518338376 | 33 | 14 | 9 | 27.6 | FDD | 208 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3251928 | 7 | 121.4684385698 | 31.1469658006 | 275 | 5 | 1 | 1.6 | FDD | 455 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3253849 | 5 | 121.4701885696 | 31.1457989813 | 294 | 4 | 6 | 2.7 | TDD | 237 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3256839 | 11 | 121.4647872757 | 31.1495520357 | 241 | 2 | 0 | 17.9 | FDD | 758 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3264223 | 2 | 121.4756981447 | 31.1453219498 | 93 | 11 | 1 | 5.4 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3264991 | 4 | 121.4729985208 | 31.1520475407 | 186 | 4 | 1 | 29.8 | TDD | 332 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3272026 | 13 | 121.4648665830 | 31.1503649968 | 142 | 6 | 9 | 26.0 | FDD | 313 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |

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
| 2024-09-20 22:21:31.128 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.145 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.252 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.252 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.993 | NREventA2 | measId:1;ServCellPCI:868;Se... |
| 2024-09-20 22:21:35.096 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.394 | NREventA5 | measId:3;ServCellPCI:868;Se... |
| 2024-09-20 22:21:35.439 | NRHandoverAttempt | SourcePCI:868;SourceNR-ARFC... |
| 2024-09-20 22:21:35.474 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.488 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.597 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.597 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220798 | 1 | 18.7341 | 13.3392 | -115.3743 | 12.5312 | 197.4271 | 0.0165 | 0.0048 |
| 2024_09_20 22:00 | 3264223 | 2 | 12.2073 | 16.5960 | -114.5575 | 8.5144 | 195.4503 | 0.0151 | 0.0173 |
| 2024_09_20 22:00 | 3228894 | 3 | 19.7789 | 14.6622 | -116.4426 | 14.8529 | 124.3369 | 0.0000 | 0.0134 |
| 2024_09_20 22:00 | 3264991 | 4 | 19.8526 | 16.6066 | -117.5722 | 16.5866 | 181.7813 | 0.0073 | 0.0120 |
| 2024_09_20 22:00 | 3253849 | 5 | 8.8453 | 17.4836 | -114.1628 | 19.3469 | 149.0753 | 0.0091 | 0.0192 |
| 2024_09_20 22:00 | 3225853 | 6 | 10.5377 | 18.3981 | -116.2904 | 10.6632 | 144.4878 | 0.0018 | 0.0153 |
| 2024_09_20 22:00 | 3251928 | 7 | 14.8458 | 18.1886 | -117.2995 | 4.0497 | 38.0607 | 0.0162 | 0.0013 |
| 2024_09_20 22:00 | 3238150 | 8 | 12.3162 | 10.6543 | -115.0332 | 4.8082 | 51.6386 | 0.0084 | 0.0077 |
| 2024_09_20 22:00 | 3246329 | 9 | 12.3123 | 6.5245 | -115.3805 | 4.1876 | 47.9289 | 0.0174 | 0.0006 |
| 2024_09_20 22:00 | 3226050 | 10 | 18.0325 | 5.9168 | -114.6525 | 3.5437 | 37.1079 | 0.0178 | 0.0141 |
| 2024_09_20 22:00 | 3256839 | 11 | 11.5102 | 11.2357 | -116.4276 | 4.3613 | 54.6281 | 0.0136 | 0.0104 |
| 2024_09_20 22:00 | 3229648 | 12 | 12.5904 | 6.2106 | -114.6136 | 3.4328 | 35.8669 | 0.0026 | 0.0083 |
| 2024_09_20 22:00 | 3272026 | 13 | 15.7117 | 5.5413 | -116.4702 | 4.4432 | 37.2899 | 0.0076 | 0.0144 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416722_32D4CDFA | 152650 | 455 | -91.5 | 152650 | 208 | -99.0 | 152650 | 344 | -101.5 | 152650 | 758 |
| MR_1774416722_1A47CBA2 | 504990 | 89 | -93.1 | 504990 | 332 | -93.8 | 504990 | 355 | -100.9 | 504990 | 98 |
| MR_1774416722_F9D080DD | 152650 | 455 | -93.2 | 152650 | 208 | -97.8 | 152650 | 344 | -102.0 | 152650 | 758 |
| MR_1774416722_79BEE080 | 152650 | 455 | -91.9 | 152650 | 208 | -96.6 | 152650 | 344 | -101.6 | 152650 | 758 |
| MR_1774416722_12612176 | 504990 | 89 | -93.0 | 504990 | 332 | -96.2 | 504990 | 355 | -100.3 | 504990 | 98 |
| MR_1774416722_BF52D841 | 152650 | 455 | -91.8 | 152650 | 208 | -98.0 | 152650 | 344 | -99.2 | 152650 | 758 |
| MR_1774416722_C437AB17 | 504990 | 89 | -92.8 | 504990 | 332 | -95.6 | 504990 | 355 | -102.1 | 504990 | 98 |
| MR_1774416722_38F6EC25 | 152650 | 455 | -94.1 | 152650 | 208 | -96.0 | 152650 | 344 | -98.7 | 152650 | 758 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 197: `7ef76f7b-c3e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7ef76f7b-c3e0-493b-9c2f-657fd70b324e` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3246576_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[197] topology](images/train_0197.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3250221_3
- `C2`: Adjust the azimuth of 3250221_3 by 50 degrees
- `C3`: Lift the tilt angle  of 3250221_3 by 8 degrees
- `C4`: Check test server and transmission issues
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Add neighbor relationship between 3246576_1 and 3250221_3
- `C7`: Decrease transmission power for 3250221_3
- `C8`: Increase A3 Offset threshold for 3246576_1
- `C9`: Lift the tilt angle of 3246576_1 by 1 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250221_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246576_1 **← 정답**
- `C12`: Increase transmission power for 3246576_1
- `C13`: Increase A3 Offset threshold for 3250221_3
- `C14`: Press down the tilt angle  of 3250221_3 by 8 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250221_3
- `C16`: Press down the tilt angle of 3246576_1 by 1 degrees
- `C17`: Decrease transmission power for 3246576_1
- `C18`: Add neighbor relationship between 3266365_4 and 3250221_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246576_1
- `C20`: Adjust the azimuth of 3246576_1 by 22 degrees
- `C21`: Decrease A3 Offset threshold for 3246576_1
- `C22`: Decrease A3 Offset threshold for 3250221_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.949 | MS1 | 121.4656688495 | 31.1446379766 | 235 | 504990 | -91.29 | 16.38 | 508.05 | 0.10 | 2.03 | 1584 |
| 2024-09-20 22:21:32.944 | MS1 | 121.4656609492 | 31.1446350925 | 235 | 504990 | -88.39 | 17.73 | 481.69 | 0.01 | 2.22 | 1580 |
| 2024-09-20 22:21:33.653 | MS1 | 121.4656650533 | 31.1446306313 | 235 | 504990 | -85.23 | 16.62 | 326.20 | 0.10 | 2.58 | 1571 |
| 2024-09-20 22:21:34.218 | MS1 | 121.4656700617 | 31.1446259466 | 235 | 504990 | -90.13 | 12.51 | 72.10 | 0.63 | 2.56 | 510 |
| 2024-09-20 22:21:35.276 | MS1 | 121.4656703855 | 31.1446262832 | 235 | 504990 | -91.89 | 13.31 | 73.83 | 0.54 | 2.93 | 557 |
| 2024-09-20 22:21:36.637 | MS1 | 121.4656663800 | 31.1446332225 | 235 | 504990 | -88.65 | 12.12 | 76.09 | 0.66 | 2.01 | 657 |
| 2024-09-20 22:21:37.853 | MS1 | 121.4656617780 | 31.1446374957 | 235 | 504990 | -89.89 | 11.96 | 50.14 | 0.59 | 2.95 | 698 |
| 2024-09-20 22:21:38.803 | MS1 | 121.4656591321 | 31.1446249506 | 235 | 504990 | -91.31 | 12.64 | 47.19 | 0.65 | 2.67 | 535 |
| 2024-09-20 22:21:39.777 | MS1 | 121.4656716782 | 31.1446342900 | 235 | 504990 | -89.84 | 7.56 | 62.04 | 0.55 | 2.53 | 623 |
| 2024-09-20 22:21:40.208 | MS1 | 121.4656731371 | 31.1446299080 | 235 | 504990 | -93.89 | 8.65 | 370.74 | 0.16 | 2.39 | 1570 |
| 2024-09-20 22:21:41.373 | MS1 | 121.4656687335 | 31.1446364934 | 235 | 504990 | -89.46 | 10.45 | 299.30 | 0.07 | 2.79 | 1583 |
| 2024-09-20 22:21:42.137 | MS1 | 121.4656720649 | 31.1446314578 | 235 | 504990 | -93.69 | 7.59 | 586.35 | 0.10 | 2.28 | 1585 |

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
| 3226463 | 2 | 121.4684377647 | 31.1472836137 | 334 | 15 | 10 | 17.9 | TDD | 316 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3246576 | 1 | 121.4647223073 | 31.1552364735 | 154 | 0 | 5 | 24.8 | TDD | 235 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3250221 | 3 | 121.4674795180 | 31.1483244943 | 304 | 3 | 0 | 41.4 | TDD | 93 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3266365 | 4 | 121.4662254142 | 31.1462847546 | 57 | 15 | 10 | 43.0 | TDD | 439 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.574 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.597 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.702 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.702 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.472 | NREventA3 | measId:2;ServCellPCI:791;Se... |
| 2024-09-20 22:21:38.712 | NRHandoverAttempt | SourcePCI:791;SourceNR-ARFC... |
| 2024-09-20 22:21:38.759 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.773 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.911 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.911 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246576 | 1 | 16.5278 | 9.1315 | -114.8551 | 12.2798 | 111.9379 | 0.0073 | 0.0143 |
| 2024_09_20 22:00 | 3226463 | 2 | 13.7929 | 17.9087 | -114.4298 | 16.5984 | 124.6105 | 0.0136 | 0.0028 |
| 2024_09_20 22:00 | 3250221 | 3 | 10.0578 | 17.2420 | -114.1635 | 17.1506 | 130.8675 | 0.0097 | 0.0015 |
| 2024_09_20 22:00 | 3266365 | 4 | 8.6533 | 6.5662 | -114.1431 | 9.9308 | 185.6803 | 0.0123 | 0.0024 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415723_B4E706DA | 504990 | 235 | -89.1 | 504990 | 93 | -91.6 | 504990 | 439 | -97.1 | 504990 | 316 |
| MR_1774415723_C1961A9D | 504990 | 235 | -90.0 | 504990 | 93 | -92.2 | 504990 | 439 | -99.0 | 504990 | 316 |
| MR_1774415723_5DA9F96D | 504990 | 235 | -92.0 | 504990 | 93 | -89.7 | 504990 | 439 | -97.6 | 504990 | 316 |
| MR_1774415723_6D1EFA34 | 504990 | 235 | -90.8 | 504990 | 93 | -90.9 | 504990 | 439 | -96.2 | 504990 | 316 |
| MR_1774415723_F585EAFA | 504990 | 235 | -91.5 | 504990 | 93 | -88.8 | 504990 | 439 | -97.2 | 504990 | 316 |
| MR_1774415723_1657607D | 504990 | 235 | -89.0 | 504990 | 93 | -91.1 | 504990 | 439 | -98.4 | 504990 | 316 |
| MR_1774415723_8B44BABC | 504990 | 235 | -89.1 | 504990 | 93 | -88.5 | 504990 | 439 | -98.7 | 504990 | 316 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 198: `9b37b9d1-fcd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9b37b9d1-fcde-4fc2-b481-863f3b5a52bd` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[198] topology](images/train_0198.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease transmission power for 3224995_1
- `C3`: Press down the tilt angle  of 3224995_1 by 10 degrees
- `C4`: Adjust the azimuth of 3251113_4 by 50 degrees
- `C5`: Increase transmission power for 3224995_1
- `C6`: Decrease A3 Offset threshold for 3251113_4
- `C7`: Decrease transmission power for 3251113_4
- `C8`: Lift the tilt angle  of 3224995_1 by 10 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251113_4
- `C10`: Adjust the azimuth of 3224995_1 by 50 degrees
- `C11`: Increase A3 Offset threshold for 3224995_1
- `C12`: Press down the tilt angle of 3251113_4 by 10 degrees
- `C13`: Increase A3 Offset threshold for 3251113_4
- `C14`: Increase transmission power for 3251113_4
- `C15`: Lift the tilt angle of 3251113_4 by 10 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251113_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224995_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224995_1
- `C19`: Add neighbor relationship between 3234078_2 and 3224995_1
- `C20`: Check test server and transmission issues **← 정답**
- `C21`: Decrease A3 Offset threshold for 3224995_1
- `C22`: Add neighbor relationship between 3251113_4 and 3224995_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.390 | MS1 | 121.4656616069 | 31.1446355671 | 422 | 504990 | -87.19 | 15.79 | 493.32 | 0.12 | 2.60 | 1579 |
| 2024-09-20 22:21:32.924 | MS1 | 121.4656738581 | 31.1446221790 | 422 | 504990 | -89.75 | 15.35 | 593.44 | 0.06 | 2.84 | 1560 |
| 2024-09-20 22:21:33.464 | MS1 | 121.4656766951 | 31.1446366486 | 422 | 504990 | -89.33 | 12.35 | 356.78 | 0.15 | 2.36 | 1587 |
| 2024-09-20 22:21:34.983 | MS1 | 121.4656610176 | 31.1446230841 | 422 | 504990 | -86.20 | 15.86 | 99.07 | 0.05 | 2.28 | 451 |
| 2024-09-20 22:21:35.230 | MS1 | 121.4656669436 | 31.1446245650 | 422 | 504990 | -85.18 | 17.24 | 88.65 | 0.04 | 2.36 | 345 |
| 2024-09-20 22:21:36.216 | MS1 | 121.4656761229 | 31.1446356952 | 422 | 504990 | -85.57 | 14.78 | 47.35 | 0.08 | 2.05 | 328 |
| 2024-09-20 22:21:37.856 | MS1 | 121.4656717969 | 31.1446354392 | 422 | 504990 | -92.54 | 11.73 | 49.02 | 0.15 | 2.54 | 340 |
| 2024-09-20 22:21:38.935 | MS1 | 121.4656699655 | 31.1446355440 | 422 | 504990 | -93.49 | 10.70 | 93.28 | 0.10 | 2.04 | 368 |
| 2024-09-20 22:21:39.238 | MS1 | 121.4656676727 | 31.1446334580 | 422 | 504990 | -91.51 | 7.26 | 76.39 | 0.18 | 2.57 | 480 |
| 2024-09-20 22:21:40.917 | MS1 | 121.4656763836 | 31.1446379473 | 422 | 504990 | -90.47 | 10.50 | 582.87 | 0.17 | 2.57 | 1570 |
| 2024-09-20 22:21:41.173 | MS1 | 121.4656750600 | 31.1446245017 | 422 | 504990 | -90.66 | 9.00 | 482.17 | 0.06 | 2.05 | 1582 |
| 2024-09-20 22:21:42.233 | MS1 | 121.4656779638 | 31.1446376608 | 422 | 504990 | -93.31 | 10.00 | 563.52 | 0.05 | 2.82 | 1590 |

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
| 3224995 | 1 | 121.4745907154 | 31.1495227732 | 345 | 13 | 12 | 23.6 | TDD | 904 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3234078 | 2 | 121.4736263584 | 31.1447750904 | 14 | 12 | 1 | 21.1 | TDD | 762 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3251113 | 4 | 121.4733385537 | 31.1444063911 | 203 | 14 | 4 | 41.0 | TDD | 422 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3267789 | 3 | 121.4740816297 | 31.1471902043 | 55 | 14 | 10 | 25.1 | TDD | 826 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.133 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.152 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.257 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.257 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.995 | NREventA3 | measId:2;ServCellPCI:722;Se... |
| 2024-09-20 22:21:38.235 | NRHandoverAttempt | SourcePCI:722;SourceNR-ARFC... |
| 2024-09-20 22:21:38.265 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.275 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.399 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.399 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224995 | 1 | 6.4247 | 15.2837 | -117.8148 | 19.8656 | 175.6128 | 0.0108 | 0.0117 |
| 2024_09_20 22:00 | 3234078 | 2 | 16.3420 | 17.4496 | -115.7093 | 5.3293 | 154.0595 | 0.0054 | 0.0183 |
| 2024_09_20 22:00 | 3267789 | 3 | 15.4847 | 15.2143 | -114.1721 | 6.3070 | 183.6419 | 0.0025 | 0.0027 |
| 2024_09_20 22:00 | 3251113 | 4 | 5.4748 | 19.7279 | -117.8473 | 14.7108 | 163.9789 | 0.0155 | 0.0056 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412137_AEEB2B4E | 504990 | 422 | -86.8 | 504990 | 904 | -85.6 | 504990 | 762 | -93.7 | 504990 | 826 |
| MR_1774412137_DF96F7FA | 504990 | 422 | -85.8 | 504990 | 904 | -87.4 | 504990 | 762 | -95.7 | 504990 | 826 |
| MR_1774412137_797C0323 | 504990 | 422 | -86.5 | 504990 | 904 | -88.0 | 504990 | 762 | -97.3 | 504990 | 826 |
| MR_1774412137_772B4024 | 504990 | 422 | -84.6 | 504990 | 904 | -87.8 | 504990 | 762 | -94.3 | 504990 | 826 |
| MR_1774412137_7FE77F9F | 504990 | 422 | -85.4 | 504990 | 904 | -86.3 | 504990 | 762 | -95.6 | 504990 | 826 |
| MR_1774412137_498F76FE | 504990 | 422 | -87.3 | 504990 | 904 | -87.1 | 504990 | 762 | -94.9 | 504990 | 826 |
| MR_1774412137_6EBBFB7F | 504990 | 422 | -85.9 | 504990 | 904 | -87.7 | 504990 | 762 | -97.0 | 504990 | 826 |
| MR_1774412137_A7374AB0 | 504990 | 422 | -87.7 | 504990 | 904 | -86.1 | 504990 | 762 | -96.2 | 504990 | 826 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 199: `1cbf6751-d99...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1cbf6751-d99b-464e-9c90-0ee4812f828a` |
| Tag | **multiple-answer** |
| 정답 | **C4|C20** |
| C4 의미 | Increase transmission power for 3246606_2 |
| C20 의미 | Adjust the azimuth of 3246606_2 by 47 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[199] topology](images/train_0199.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3263310_1
- `C2`: Increase A3 Offset threshold for 3263310_1
- `C3`: Add neighbor relationship between 3264853_4 and 3263310_1
- `C4`: Increase transmission power for 3246606_2 **← 정답**
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263310_1
- `C6`: Decrease A3 Offset threshold for 3246606_2
- `C7`: Increase A3 Offset threshold for 3246606_2
- `C8`: Press down the tilt angle of 3246606_2 by 10 degrees
- `C9`: Check test server and transmission issues
- `C10`: Adjust the azimuth of 3263310_1 by 30 degrees
- `C11`: Add neighbor relationship between 3246606_2 and 3263310_1
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263310_1
- `C14`: Press down the tilt angle  of 3263310_1 by 4 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246606_2
- `C16`: Lift the tilt angle of 3246606_2 by 10 degrees
- `C17`: Decrease transmission power for 3246606_2
- `C18`: Decrease transmission power for 3263310_1
- `C19`: Increase transmission power for 3263310_1
- `C20`: Adjust the azimuth of 3246606_2 by 47 degrees **← 정답**
- `C21`: Lift the tilt angle  of 3263310_1 by 4 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246606_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.236 | MS1 | 121.4656662800 | 31.1446297003 | 298 | 504990 | -88.25 | 13.00 | 431.46 | 0.03 | 2.01 | 1564 |
| 2024-09-20 22:21:32.588 | MS1 | 121.4656660865 | 31.1446215277 | 298 | 504990 | -88.14 | 13.13 | 500.98 | 0.03 | 2.85 | 1594 |
| 2024-09-20 22:21:33.346 | MS1 | 121.4656657550 | 31.1446260225 | 298 | 504990 | -89.22 | 15.01 | 450.81 | 0.07 | 2.49 | 1580 |
| 2024-09-20 22:21:34.100 | MS1 | 121.4656627230 | 31.1446290650 | 298 | 504990 | -100.53 | -0.73 | 42.03 | 0.18 | 1.21 | 1592 |
| 2024-09-20 22:21:35.524 | MS1 | 121.4656699598 | 31.1446343032 | 298 | 504990 | -102.92 | -0.04 | 29.54 | 0.06 | 1.44 | 1583 |
| 2024-09-20 22:21:36.172 | MS1 | 121.4656625479 | 31.1446280288 | 298 | 504990 | -101.90 | 0.03 | 39.86 | 0.07 | 1.13 | 1595 |
| 2024-09-20 22:21:37.432 | MS1 | 121.4656682827 | 31.1446341991 | 298 | 504990 | -100.73 | -1.59 | 50.12 | 0.18 | 1.48 | 1589 |
| 2024-09-20 22:21:38.992 | MS1 | 121.4656778844 | 31.1446292692 | 298 | 504990 | -100.36 | 1.52 | 68.42 | 0.02 | 1.46 | 1595 |
| 2024-09-20 22:21:39.660 | MS1 | 121.4656593693 | 31.1446213268 | 298 | 504990 | -107.81 | 1.62 | 65.26 | 0.05 | 1.44 | 1595 |
| 2024-09-20 22:21:40.358 | MS1 | 121.4656747950 | 31.1446362552 | 298 | 504990 | -90.18 | 16.05 | 523.22 | 0.16 | 2.09 | 1587 |
| 2024-09-20 22:21:41.184 | MS1 | 121.4656662224 | 31.1446242286 | 298 | 504990 | -94.79 | 14.05 | 546.80 | 0.16 | 2.99 | 1571 |
| 2024-09-20 22:21:42.309 | MS1 | 121.4656605072 | 31.1446344936 | 298 | 504990 | -89.53 | 13.45 | 466.77 | 0.03 | 2.38 | 1591 |

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
| 3223301 | 3 | 121.4752174907 | 31.1487406576 | 293 | 5 | 12 | 16.9 | TDD | 477 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3246606 | 2 | 121.4682704796 | 31.1528754591 | 148 | 10 | 6 | 42.7 | TDD | 298 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3263310 | 1 | 121.4688942046 | 31.1445512439 | 242 | 0 | 8 | 21.1 | TDD | 25 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3264853 | 4 | 121.4670721437 | 31.1508235622 | 278 | 3 | 10 | 48.4 | TDD | 479 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.990 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.013 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.130 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.130 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.305 | NREventA2 | measId:1;ServCellPCI:472;Se... |
| 2024-09-20 22:21:34.433 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263310 | 1 | 11.8096 | 17.1713 | -116.5625 | 11.7951 | 146.5058 | 0.0056 | 0.0015 |
| 2024_09_20 22:00 | 3246606 | 2 | 18.2750 | 10.5370 | -114.0083 | 19.8846 | 115.2803 | 0.1332 | 0.0074 |
| 2024_09_20 22:00 | 3223301 | 3 | 16.3015 | 18.6275 | -115.4598 | 18.4190 | 82.5443 | 0.0077 | 0.0157 |
| 2024_09_20 22:00 | 3264853 | 4 | 16.6715 | 10.5484 | -116.2247 | 6.7469 | 149.3612 | 0.0075 | 0.0173 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415012_440AFB23 | 504990 | 298 | -98.8 | 504990 | 25 | -103.5 | 504990 | 479 | -112.5 | 504990 | 477 |
| MR_1774415012_5B6AB53F | 504990 | 298 | -99.4 | 504990 | 25 | -105.3 | 504990 | 479 | -110.6 | 504990 | 477 |
| MR_1774415012_24B16FED | 504990 | 298 | -100.0 | 504990 | 25 | -104.1 | 504990 | 479 | -109.4 | 504990 | 477 |
| MR_1774415012_94E6D763 | 504990 | 298 | -100.3 | 504990 | 25 | -102.4 | 504990 | 479 | -112.9 | 504990 | 477 |
| MR_1774415012_595DA5ED | 504990 | 298 | -101.8 | 504990 | 25 | -104.0 | 504990 | 479 | -112.6 | 504990 | 477 |

> *... 2개 열 생략 (전체 14열)*

---
