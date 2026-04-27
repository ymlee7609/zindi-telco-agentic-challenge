# Track A 문제 분석 — train[200]~train[209]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[200] ~ train[209] (10개)

## 목차

1. [문제 200: `fd0c48ee-f62...`](#200) — single-answer, 정답: C9
2. [문제 201: `8445373e-4cc...`](#201) — single-answer, 정답: C2
3. [문제 202: `e2965b1b-c9d...`](#202) — single-answer, 정답: C20
4. [문제 203: `3510c180-5b9...`](#203) — single-answer, 정답: C9
5. [문제 204: `7ac1dc2c-d30...`](#204) — single-answer, 정답: C11
6. [문제 205: `3ad9803f-690...`](#205) — single-answer, 정답: C18
7. [문제 206: `b5f6b441-a89...`](#206) — single-answer, 정답: C7
8. [문제 207: `1fdd16f9-586...`](#207) — single-answer, 정답: C21
9. [문제 208: `9c7713be-b19...`](#208) — single-answer, 정답: C22
10. [문제 209: `66ed18f8-8c0...`](#209) — single-answer, 정답: C18

---

### 문제 200: `fd0c48ee-f62...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fd0c48ee-f62a-4be3-b781-b638e49d88cb` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease A3 Offset threshold for 3238701_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[200] topology](images/train_0200.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3211522_1 and 3213727_4
- `C2`: Adjust the azimuth of 3213727_4 by 50 degrees
- `C3`: Increase transmission power for 3238701_2
- `C4`: Decrease transmission power for 3213727_4
- `C5`: Adjust the azimuth of 3238701_2 by 50 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213727_4
- `C8`: Add neighbor relationship between 3238701_2 and 3213727_4
- `C9`: Decrease A3 Offset threshold for 3238701_2 **← 정답**
- `C10`: Lift the tilt angle  of 3213727_4 by 4 degrees
- `C11`: Decrease transmission power for 3238701_2
- `C12`: Lift the tilt angle of 3238701_2 by 10 degrees
- `C13`: Increase A3 Offset threshold for 3213727_4
- `C14`: Press down the tilt angle  of 3213727_4 by 4 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238701_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213727_4
- `C17`: Increase A3 Offset threshold for 3238701_2
- `C18`: Check test server and transmission issues
- `C19`: Press down the tilt angle of 3238701_2 by 10 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238701_2
- `C21`: Increase transmission power for 3213727_4
- `C22`: Decrease A3 Offset threshold for 3213727_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.290 | MS1 | 121.4656679476 | 31.1446294637 | 258 | 504990 | -81.57 | 16.76 | 395.24 | 0.14 | 2.39 | 1588 |
| 2024-09-20 22:21:32.420 | MS1 | 121.4656716890 | 31.1446235999 | 258 | 504990 | -81.05 | 16.89 | 416.80 | 0.05 | 2.80 | 1573 |
| 2024-09-20 22:21:33.832 | MS1 | 121.4656700556 | 31.1446314950 | 258 | 504990 | -77.15 | 13.37 | 597.61 | 0.18 | 2.27 | 1576 |
| 2024-09-20 22:21:34.787 | MS1 | 121.4656694875 | 31.1446188265 | 258 | 504990 | -84.54 | -3.32 | 63.21 | 0.05 | 1.03 | 1561 |
| 2024-09-20 22:21:35.819 | MS1 | 121.4656668141 | 31.1446359894 | 258 | 504990 | -85.91 | -1.10 | 54.68 | 0.18 | 1.38 | 1576 |
| 2024-09-20 22:21:36.477 | MS1 | 121.4656699297 | 31.1446343899 | 258 | 504990 | -92.75 | -3.96 | 77.83 | 0.16 | 1.24 | 1585 |
| 2024-09-20 22:21:37.290 | MS1 | 121.4656774265 | 31.1446249553 | 258 | 504990 | -92.35 | -0.61 | 46.72 | 0.07 | 1.38 | 1595 |
| 2024-09-20 22:21:38.359 | MS1 | 121.4656704112 | 31.1446223419 | 258 | 504990 | -91.33 | -1.85 | 33.34 | 0.03 | 1.46 | 1567 |
| 2024-09-20 22:21:39.935 | MS1 | 121.4656735448 | 31.1446297257 | 639 | 504990 | -80.27 | 12.96 | 226.65 | 0.07 | 1.07 | 1575 |
| 2024-09-20 22:21:40.903 | MS1 | 121.4656631443 | 31.1446299663 | 639 | 504990 | -81.17 | 15.03 | 518.55 | 0.06 | 2.82 | 1574 |
| 2024-09-20 22:21:41.822 | MS1 | 121.4656724513 | 31.1446356155 | 639 | 504990 | -75.81 | 13.47 | 398.57 | 0.04 | 2.12 | 1588 |
| 2024-09-20 22:21:42.122 | MS1 | 121.4656685071 | 31.1446367095 | 639 | 504990 | -76.92 | 13.56 | 557.50 | 0.10 | 2.48 | 1591 |

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
| 3211522 | 1 | 121.4747092072 | 31.1535476320 | 241 | 6 | 1 | 46.7 | TDD | 729 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3213727 | 4 | 121.4757093956 | 31.1533597077 | 5 | 2 | 7 | 40.6 | TDD | 639 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3238701 | 2 | 121.4653385776 | 31.1508381518 | 316 | 14 | 2 | 24.7 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3248364 | 3 | 121.4667176884 | 31.1532053584 | 336 | 13 | 1 | 44.4 | TDD | 469 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.149 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.174 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.301 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.301 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.955 | NREventA3 | measId:2;ServCellPCI:33;Ser... |
| 2024-09-20 22:21:38.195 | NRHandoverAttempt | SourcePCI:33;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.236 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.249 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.392 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.392 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211522 | 1 | 12.9605 | 18.6199 | -116.5350 | 5.8670 | 170.1826 | 0.0005 | 0.0070 |
| 2024_09_20 22:00 | 3238701 | 2 | 19.0529 | 12.0413 | -115.4284 | 18.0478 | 104.6185 | 0.0042 | 0.1189 |
| 2024_09_20 22:00 | 3248364 | 3 | 12.9701 | 12.5093 | -116.8712 | 6.7113 | 108.8357 | 0.0178 | 0.0009 |
| 2024_09_20 22:00 | 3213727 | 4 | 18.8090 | 11.0838 | -117.6447 | 17.3716 | 85.2479 | 0.0157 | 0.0159 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412698_2162DEB7 | 504990 | 639 | -76.6 | 504990 | 258 | -83.7 | 504990 | 729 | -79.0 | 504990 | 469 |
| MR_1774412698_F2F47B00 | 504990 | 258 | -83.7 | 504990 | 639 | -78.2 | 504990 | 729 | -80.2 | 504990 | 469 |
| MR_1774412698_416053C6 | 504990 | 258 | -85.5 | 504990 | 639 | -77.5 | 504990 | 729 | -78.1 | 504990 | 469 |
| MR_1774412698_59AB96C4 | 504990 | 258 | -83.0 | 504990 | 639 | -76.4 | 504990 | 729 | -81.8 | 504990 | 469 |
| MR_1774412698_C1FB7DAE | 504990 | 258 | -86.5 | 504990 | 639 | -77.2 | 504990 | 729 | -82.0 | 504990 | 469 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 201: `8445373e-4cc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8445373e-4cc4-4d0a-8aa4-8807c6aeba38` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[201] topology](images/train_0201.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3226959_2 by 3 degrees
- `C2`: Check test server and transmission issues **← 정답**
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275001_3
- `C4`: Add neighbor relationship between 3213967_1 and 3275001_3
- `C5`: Decrease A3 Offset threshold for 3226959_2
- `C6`: Decrease transmission power for 3275001_3
- `C7`: Adjust the azimuth of 3226959_2 by 11 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226959_2
- `C9`: Increase transmission power for 3226959_2
- `C10`: Decrease transmission power for 3226959_2
- `C11`: Press down the tilt angle of 3226959_2 by 3 degrees
- `C12`: Lift the tilt angle  of 3275001_3 by 4 degrees
- `C13`: Adjust the azimuth of 3275001_3 by 49 degrees
- `C14`: Increase A3 Offset threshold for 3226959_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226959_2
- `C16`: Add neighbor relationship between 3226959_2 and 3275001_3
- `C17`: Press down the tilt angle  of 3275001_3 by 4 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275001_3
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease A3 Offset threshold for 3275001_3
- `C21`: Increase transmission power for 3275001_3
- `C22`: Increase A3 Offset threshold for 3275001_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.150 | MS1 | 121.4656581368 | 31.1446269179 | 39 | 504990 | -91.73 | 17.62 | 339.22 | 0.09 | 2.47 | 1562 |
| 2024-09-20 22:21:32.942 | MS1 | 121.4656735088 | 31.1446221310 | 39 | 504990 | -85.96 | 13.91 | 420.80 | 0.14 | 2.83 | 1599 |
| 2024-09-20 22:21:33.506 | MS1 | 121.4656665636 | 31.1446327360 | 39 | 504990 | -85.14 | 12.86 | 303.46 | 0.11 | 2.82 | 1574 |
| 2024-09-20 22:21:34.666 | MS1 | 121.4656594064 | 31.1446233231 | 39 | 504990 | -85.32 | 13.89 | 84.15 | 0.11 | 2.17 | 400 |
| 2024-09-20 22:21:35.400 | MS1 | 121.4656735432 | 31.1446244824 | 39 | 504990 | -90.13 | 13.73 | 62.67 | 0.01 | 2.92 | 458 |
| 2024-09-20 22:21:36.488 | MS1 | 121.4656662452 | 31.1446307123 | 39 | 504990 | -89.42 | 14.22 | 65.97 | 0.06 | 2.92 | 371 |
| 2024-09-20 22:21:37.261 | MS1 | 121.4656633761 | 31.1446366552 | 39 | 504990 | -91.17 | 7.74 | 75.11 | 0.06 | 2.58 | 330 |
| 2024-09-20 22:21:38.961 | MS1 | 121.4656589672 | 31.1446278177 | 39 | 504990 | -92.27 | 12.00 | 55.18 | 0.06 | 2.28 | 392 |
| 2024-09-20 22:21:39.794 | MS1 | 121.4656715493 | 31.1446260002 | 39 | 504990 | -90.15 | 10.16 | 76.84 | 0.16 | 2.73 | 455 |
| 2024-09-20 22:21:40.395 | MS1 | 121.4656732907 | 31.1446325281 | 39 | 504990 | -90.08 | 9.66 | 302.93 | 0.11 | 2.46 | 1584 |
| 2024-09-20 22:21:41.812 | MS1 | 121.4656662771 | 31.1446297911 | 39 | 504990 | -91.61 | 9.37 | 455.78 | 0.00 | 2.96 | 1596 |
| 2024-09-20 22:21:42.347 | MS1 | 121.4656696949 | 31.1446345651 | 39 | 504990 | -93.00 | 8.44 | 564.77 | 0.10 | 2.12 | 1572 |

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
| 3213967 | 1 | 121.4689278823 | 31.1491626675 | 322 | 8 | 8 | 30.1 | TDD | 32 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3226959 | 2 | 121.4711218447 | 31.1540367925 | 195 | 1 | 3 | 47.0 | TDD | 39 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3244325 | 4 | 121.4683424531 | 31.1467467891 | 0 | 4 | 11 | 23.8 | TDD | 199 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3275001 | 3 | 121.4695456142 | 31.1476320029 | 277 | 1 | 10 | 26.5 | TDD | 541 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.636 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.661 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.764 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.764 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.456 | NREventA3 | measId:2;ServCellPCI:641;Se... |
| 2024-09-20 22:21:38.696 | NRHandoverAttempt | SourcePCI:641;SourceNR-ARFC... |
| 2024-09-20 22:21:38.732 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.745 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.872 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.872 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213967 | 1 | 6.6796 | 10.9040 | -116.4384 | 12.1756 | 149.6846 | 0.0104 | 0.0191 |
| 2024_09_20 22:00 | 3226959 | 2 | 7.7594 | 8.8185 | -116.5314 | 14.0919 | 111.0001 | 0.0110 | 0.0176 |
| 2024_09_20 22:00 | 3275001 | 3 | 11.6146 | 6.6314 | -116.1964 | 11.3251 | 151.4016 | 0.0129 | 0.0106 |
| 2024_09_20 22:00 | 3244325 | 4 | 17.0893 | 7.0587 | -116.7159 | 11.7092 | 107.0184 | 0.0031 | 0.0052 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415363_23185A61 | 504990 | 39 | -84.0 | 504990 | 541 | -87.4 | 504990 | 32 | -95.8 | 504990 | 199 |
| MR_1774415363_9B98C42B | 504990 | 39 | -86.1 | 504990 | 541 | -84.8 | 504990 | 32 | -97.4 | 504990 | 199 |
| MR_1774415363_462B293D | 504990 | 39 | -86.6 | 504990 | 541 | -85.9 | 504990 | 32 | -97.2 | 504990 | 199 |
| MR_1774415363_E3402982 | 504990 | 39 | -86.6 | 504990 | 541 | -86.2 | 504990 | 32 | -94.1 | 504990 | 199 |
| MR_1774415363_76F97C23 | 504990 | 39 | -85.6 | 504990 | 541 | -86.5 | 504990 | 32 | -96.6 | 504990 | 199 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 202: `e2965b1b-c9d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e2965b1b-c9d9-4e54-abf3-9b23ea906870` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3223801_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[202] topology](images/train_0202.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3276881_3 by 50 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223801_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276881_3
- `C4`: Decrease transmission power for 3276881_3
- `C5`: Increase A3 Offset threshold for 3223801_2
- `C6`: Press down the tilt angle  of 3276881_3 by 9 degrees
- `C7`: Add neighbor relationship between 3223801_2 and 3276881_3
- `C8`: Lift the tilt angle  of 3276881_3 by 9 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276881_3
- `C10`: Check test server and transmission issues
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Press down the tilt angle of 3223801_2 by 3 degrees
- `C13`: Adjust the azimuth of 3223801_2 by 43 degrees
- `C14`: Increase transmission power for 3223801_2
- `C15`: Lift the tilt angle of 3223801_2 by 3 degrees
- `C16`: Increase transmission power for 3276881_3
- `C17`: Decrease A3 Offset threshold for 3223801_2
- `C18`: Decrease transmission power for 3223801_2
- `C19`: Decrease A3 Offset threshold for 3276881_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223801_2 **← 정답**
- `C21`: Increase A3 Offset threshold for 3276881_3
- `C22`: Add neighbor relationship between 3247680_4 and 3276881_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.342 | MS1 | 121.4656593482 | 31.1446208168 | 471 | 504990 | -87.28 | 13.03 | 548.31 | 0.09 | 2.73 | 1581 |
| 2024-09-20 22:21:32.447 | MS1 | 121.4656702415 | 31.1446216899 | 471 | 504990 | -86.65 | 15.44 | 414.37 | 0.06 | 2.12 | 1582 |
| 2024-09-20 22:21:33.348 | MS1 | 121.4656601504 | 31.1446261132 | 471 | 504990 | -87.41 | 15.45 | 374.71 | 0.11 | 2.83 | 1577 |
| 2024-09-20 22:21:34.517 | MS1 | 121.4656620471 | 31.1446298715 | 471 | 504990 | -90.60 | 13.49 | 80.59 | 0.66 | 2.86 | 687 |
| 2024-09-20 22:21:35.894 | MS1 | 121.4656678026 | 31.1446206394 | 471 | 504990 | -88.40 | 17.72 | 96.09 | 0.56 | 2.01 | 567 |
| 2024-09-20 22:21:36.310 | MS1 | 121.4656708958 | 31.1446346647 | 471 | 504990 | -90.45 | 14.93 | 80.46 | 0.50 | 2.32 | 651 |
| 2024-09-20 22:21:37.893 | MS1 | 121.4656591489 | 31.1446344066 | 471 | 504990 | -93.20 | 9.41 | 64.45 | 0.50 | 2.55 | 696 |
| 2024-09-20 22:21:38.799 | MS1 | 121.4656627059 | 31.1446354639 | 471 | 504990 | -91.52 | 8.90 | 70.51 | 0.62 | 2.97 | 638 |
| 2024-09-20 22:21:39.362 | MS1 | 121.4656657730 | 31.1446314325 | 471 | 504990 | -93.87 | 10.11 | 93.63 | 0.63 | 2.27 | 664 |
| 2024-09-20 22:21:40.936 | MS1 | 121.4656603424 | 31.1446243233 | 471 | 504990 | -91.68 | 11.12 | 372.89 | 0.01 | 2.70 | 1575 |
| 2024-09-20 22:21:41.584 | MS1 | 121.4656739000 | 31.1446253669 | 471 | 504990 | -91.35 | 8.91 | 456.38 | 0.08 | 2.77 | 1589 |
| 2024-09-20 22:21:42.476 | MS1 | 121.4656594284 | 31.1446348653 | 471 | 504990 | -92.62 | 9.42 | 448.59 | 0.14 | 2.93 | 1568 |

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
| 3223801 | 2 | 121.4739342296 | 31.1473745938 | 206 | 0 | 11 | 37.3 | TDD | 471 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3232926 | 1 | 121.4741146245 | 31.1521853165 | 61 | 15 | 6 | 21.3 | TDD | 65 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3247680 | 4 | 121.4728324572 | 31.1442335195 | 94 | 5 | 12 | 18.8 | TDD | 1007 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3276881 | 3 | 121.4711788429 | 31.1449620070 | 52 | 6 | 4 | 30.4 | TDD | 398 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.841 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.861 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.976 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.976 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.727 | NREventA3 | measId:2;ServCellPCI:516;Se... |
| 2024-09-20 22:21:37.967 | NRHandoverAttempt | SourcePCI:516;SourceNR-ARFC... |
| 2024-09-20 22:21:38.014 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.028 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.142 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.142 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232926 | 1 | 14.3838 | 14.1471 | -117.6150 | 16.6108 | 126.4856 | 0.0108 | 0.0187 |
| 2024_09_20 22:00 | 3223801 | 2 | 6.1007 | 15.7232 | -117.0111 | 17.0439 | 110.4088 | 0.0156 | 0.0107 |
| 2024_09_20 22:00 | 3276881 | 3 | 19.9428 | 14.2287 | -114.9784 | 6.7204 | 147.8884 | 0.0023 | 0.0067 |
| 2024_09_20 22:00 | 3247680 | 4 | 18.9873 | 12.4977 | -116.1834 | 11.9480 | 115.8056 | 0.0131 | 0.0151 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415185_57F4F62D | 504990 | 471 | -89.7 | 504990 | 398 | -101.2 | 504990 | 1007 | -103.2 | 504990 | 65 |
| MR_1774415185_CA89E96F | 504990 | 471 | -89.4 | 504990 | 398 | -100.7 | 504990 | 1007 | -105.5 | 504990 | 65 |
| MR_1774415185_D4F37253 | 504990 | 471 | -90.2 | 504990 | 398 | -98.7 | 504990 | 1007 | -105.8 | 504990 | 65 |
| MR_1774415185_63837B3D | 504990 | 471 | -88.9 | 504990 | 398 | -102.2 | 504990 | 1007 | -105.1 | 504990 | 65 |
| MR_1774415185_92397D78 | 504990 | 471 | -90.0 | 504990 | 398 | -102.1 | 504990 | 1007 | -103.7 | 504990 | 65 |
| MR_1774415185_2B327A10 | 504990 | 471 | -89.6 | 504990 | 398 | -98.9 | 504990 | 1007 | -104.2 | 504990 | 65 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 203: `3510c180-5b9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3510c180-5b9b-4624-a6fb-921e3145f2f1` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Add neighbor relationship between 3269769_1 and 3257002_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[203] topology](images/train_0203.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269769_1
- `C2`: Decrease transmission power for 3257002_2
- `C3`: Adjust the azimuth of 3269769_1 by 50 degrees
- `C4`: Decrease A3 Offset threshold for 3257002_2
- `C5`: Add neighbor relationship between 3257337_4 and 3257002_2
- `C6`: Increase transmission power for 3269769_1
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Lift the tilt angle  of 3257002_2 by 4 degrees
- `C9`: Add neighbor relationship between 3269769_1 and 3257002_2 **← 정답**
- `C10`: Press down the tilt angle of 3269769_1 by 10 degrees
- `C11`: Decrease A3 Offset threshold for 3269769_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269769_1
- `C13`: Adjust the azimuth of 3257002_2 by 14 degrees
- `C14`: Decrease transmission power for 3269769_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257002_2
- `C16`: Lift the tilt angle of 3269769_1 by 10 degrees
- `C17`: Check test server and transmission issues
- `C18`: Increase transmission power for 3257002_2
- `C19`: Press down the tilt angle  of 3257002_2 by 4 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257002_2
- `C21`: Increase A3 Offset threshold for 3257002_2
- `C22`: Increase A3 Offset threshold for 3269769_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.846 | MS1 | 121.4656615823 | 31.1446293348 | 369 | 504990 | -80.29 | 17.90 | 583.33 | 0.09 | 2.55 | 1586 |
| 2024-09-20 22:21:32.332 | MS1 | 121.4656652663 | 31.1446342653 | 369 | 504990 | -76.92 | 16.37 | 308.91 | 0.10 | 2.31 | 1600 |
| 2024-09-20 22:21:33.171 | MS1 | 121.4656721279 | 31.1446363085 | 369 | 504990 | -82.38 | 12.91 | 357.34 | 0.07 | 2.26 | 1594 |
| 2024-09-20 22:21:34.371 | MS1 | 121.4656581640 | 31.1446336838 | 369 | 504990 | -85.62 | -2.76 | 35.78 | 0.16 | 1.04 | 1569 |
| 2024-09-20 22:21:35.276 | MS1 | 121.4656657777 | 31.1446322600 | 369 | 504990 | -92.09 | -3.14 | 44.12 | 0.15 | 1.42 | 1576 |
| 2024-09-20 22:21:36.193 | MS1 | 121.4656624864 | 31.1446181273 | 369 | 504990 | -88.83 | -0.22 | 61.77 | 0.13 | 1.02 | 1571 |
| 2024-09-20 22:21:37.633 | MS1 | 121.4656767228 | 31.1446181302 | 369 | 504990 | -88.36 | -0.65 | 32.78 | 0.00 | 1.37 | 1585 |
| 2024-09-20 22:21:38.188 | MS1 | 121.4656775793 | 31.1446307772 | 369 | 504990 | -80.74 | 12.09 | 476.40 | 0.04 | 1.29 | 1574 |
| 2024-09-20 22:21:39.448 | MS1 | 121.4656616470 | 31.1446308869 | 369 | 504990 | -77.24 | 12.51 | 400.48 | 0.18 | 1.43 | 1584 |
| 2024-09-20 22:21:40.908 | MS1 | 121.4656769949 | 31.1446340199 | 369 | 504990 | -79.18 | 16.50 | 483.03 | 0.12 | 2.92 | 1567 |
| 2024-09-20 22:21:41.447 | MS1 | 121.4656694490 | 31.1446347493 | 369 | 504990 | -82.73 | 15.09 | 540.21 | 0.04 | 2.72 | 1566 |
| 2024-09-20 22:21:42.651 | MS1 | 121.4656643398 | 31.1446287894 | 369 | 504990 | -79.77 | 13.16 | 588.59 | 0.02 | 2.16 | 1563 |

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
| 3232413 | 3 | 121.4737584848 | 31.1496179622 | 359 | 15 | 7 | 25.5 | TDD | 485 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3257002 | 2 | 121.4643181539 | 31.1537260204 | 159 | 3 | 5 | 21.1 | TDD | 130 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3257337 | 4 | 121.4724579687 | 31.1492306038 | 350 | 10 | 4 | 30.0 | TDD | 214 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3269769 | 1 | 121.4669429843 | 31.1451435151 | 28 | 10 | 12 | 33.9 | TDD | 369 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.635 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.767 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.767 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.424 | NREventA3 | measId:2;ServCellPCI:385;Se... |
| 2024-09-20 22:21:36.424 | NREventA3 | measId:2;ServCellPCI:385;Se... |
| 2024-09-20 22:21:37.424 | NREventA3 | measId:2;ServCellPCI:385;Se... |
| 2024-09-20 22:21:39.924 | NRRRCReestablishAttempt | PCI:385 |
| 2024-09-20 22:21:39.941 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.956 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:40.102 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.102 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269769 | 1 | 12.9637 | 7.8880 | -116.0895 | 17.5097 | 128.7747 | 0.0190 | 0.1769 |
| 2024_09_20 22:00 | 3257002 | 2 | 9.6664 | 12.9456 | -115.6533 | 9.0668 | 105.5994 | 0.0188 | 0.0070 |
| 2024_09_20 22:00 | 3232413 | 3 | 19.3467 | 17.0378 | -115.1665 | 14.7262 | 138.5437 | 0.0137 | 0.0069 |
| 2024_09_20 22:00 | 3257337 | 4 | 19.8515 | 16.5626 | -116.9523 | 19.2764 | 105.7456 | 0.0122 | 0.0031 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414878_CBC8306B | 504990 | 130 | -81.4 | 504990 | 369 | -86.0 | 504990 | 214 | -83.2 | 504990 | 485 |
| MR_1774414878_EF48FA2C | 504990 | 369 | -87.5 | 504990 | 130 | -81.2 | 504990 | 214 | -84.6 | 504990 | 485 |
| MR_1774414878_6C74D5FF | 504990 | 369 | -84.2 | 504990 | 130 | -78.5 | 504990 | 214 | -83.7 | 504990 | 485 |
| MR_1774414878_D80C95F0 | 504990 | 369 | -87.3 | 504990 | 130 | -77.9 | 504990 | 214 | -83.4 | 504990 | 485 |
| MR_1774414878_0C576FD6 | 504990 | 130 | -80.8 | 504990 | 369 | -85.7 | 504990 | 214 | -83.8 | 504990 | 485 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 204: `7ac1dc2c-d30...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7ac1dc2c-d306-4af4-a71f-bc402db34d7c` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[204] topology](images/train_0204.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264702_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234841_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264702_2
- `C4`: Decrease transmission power for 3234841_1
- `C5`: Increase A3 Offset threshold for 3234841_1
- `C6`: Press down the tilt angle  of 3234841_1 by 2 degrees
- `C7`: Add neighbor relationship between 3248556_4 and 3234841_1
- `C8`: Increase transmission power for 3234841_1
- `C9`: Press down the tilt angle of 3264702_2 by 3 degrees
- `C10`: Increase A3 Offset threshold for 3264702_2
- `C11`: Check test server and transmission issues **← 정답**
- `C12`: Adjust the azimuth of 3234841_1 by 50 degrees
- `C13`: Adjust the azimuth of 3264702_2 by 50 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease transmission power for 3264702_2
- `C16`: Increase transmission power for 3264702_2
- `C17`: Decrease A3 Offset threshold for 3264702_2
- `C18`: Lift the tilt angle of 3264702_2 by 3 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234841_1
- `C20`: Add neighbor relationship between 3264702_2 and 3234841_1
- `C21`: Lift the tilt angle  of 3234841_1 by 2 degrees
- `C22`: Decrease A3 Offset threshold for 3234841_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.667 | MS1 | 121.4656594024 | 31.1446269698 | 913 | 504990 | -89.29 | 17.54 | 447.22 | 0.18 | 2.22 | 1564 |
| 2024-09-20 22:21:32.377 | MS1 | 121.4656767987 | 31.1446227731 | 913 | 504990 | -88.57 | 16.31 | 453.44 | 0.16 | 2.81 | 1590 |
| 2024-09-20 22:21:33.965 | MS1 | 121.4656610623 | 31.1446283008 | 913 | 504990 | -85.13 | 17.59 | 496.83 | 0.12 | 2.96 | 1588 |
| 2024-09-20 22:21:34.684 | MS1 | 121.4656660476 | 31.1446220338 | 913 | 504990 | -90.33 | 13.29 | 69.66 | 0.11 | 2.91 | 355 |
| 2024-09-20 22:21:35.547 | MS1 | 121.4656599866 | 31.1446342067 | 913 | 504990 | -87.35 | 15.70 | 78.26 | 0.20 | 2.73 | 323 |
| 2024-09-20 22:21:36.397 | MS1 | 121.4656585979 | 31.1446241795 | 913 | 504990 | -87.63 | 12.17 | 86.51 | 0.13 | 2.52 | 377 |
| 2024-09-20 22:21:37.797 | MS1 | 121.4656646138 | 31.1446343533 | 913 | 504990 | -91.32 | 7.58 | 67.37 | 0.03 | 2.07 | 480 |
| 2024-09-20 22:21:38.631 | MS1 | 121.4656589364 | 31.1446330232 | 913 | 504990 | -90.04 | 12.65 | 51.66 | 0.05 | 2.32 | 473 |
| 2024-09-20 22:21:39.336 | MS1 | 121.4656759445 | 31.1446225999 | 913 | 504990 | -93.55 | 10.84 | 55.42 | 0.04 | 2.47 | 407 |
| 2024-09-20 22:21:40.366 | MS1 | 121.4656623419 | 31.1446352309 | 913 | 504990 | -91.19 | 8.92 | 453.62 | 0.15 | 2.33 | 1597 |
| 2024-09-20 22:21:41.213 | MS1 | 121.4656760988 | 31.1446322037 | 913 | 504990 | -89.52 | 8.22 | 344.73 | 0.02 | 2.62 | 1562 |
| 2024-09-20 22:21:42.272 | MS1 | 121.4656752549 | 31.1446294849 | 913 | 504990 | -90.06 | 12.39 | 376.71 | 0.04 | 2.11 | 1570 |

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
| 3217263 | 3 | 121.4735944386 | 31.1509117982 | 289 | 5 | 4 | 38.9 | TDD | 707 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3234841 | 1 | 121.4713646362 | 31.1540615612 | 342 | 0 | 11 | 43.3 | TDD | 512 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3248556 | 4 | 121.4728729833 | 31.1489790806 | 35 | 6 | 10 | 24.7 | TDD | 912 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3264702 | 2 | 121.4671674351 | 31.1530189432 | 257 | 1 | 9 | 33.4 | TDD | 913 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.195 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.219 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.368 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.368 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.038 | NREventA3 | measId:2;ServCellPCI:15;Ser... |
| 2024-09-20 22:21:38.278 | NRHandoverAttempt | SourcePCI:15;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.318 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.332 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.468 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.468 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234841 | 1 | 10.8388 | 12.1708 | -114.7947 | 6.0047 | 174.6451 | 0.0010 | 0.0108 |
| 2024_09_20 22:00 | 3264702 | 2 | 11.6611 | 13.7677 | -115.0151 | 16.4163 | 117.5605 | 0.0180 | 0.0117 |
| 2024_09_20 22:00 | 3217263 | 3 | 17.8864 | 12.1222 | -114.1163 | 10.9519 | 172.8795 | 0.0023 | 0.0116 |
| 2024_09_20 22:00 | 3248556 | 4 | 19.4551 | 17.6802 | -116.4861 | 17.3729 | 122.5417 | 0.0134 | 0.0176 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415718_D5C364A4 | 504990 | 913 | -90.1 | 504990 | 512 | -99.7 | 504990 | 912 | -104.2 | 504990 | 707 |
| MR_1774415718_9F6EFFEF | 504990 | 913 | -89.6 | 504990 | 512 | -99.5 | 504990 | 912 | -104.7 | 504990 | 707 |
| MR_1774415718_C99E1647 | 504990 | 913 | -90.7 | 504990 | 512 | -98.5 | 504990 | 912 | -103.8 | 504990 | 707 |
| MR_1774415718_ABAED141 | 504990 | 913 | -91.0 | 504990 | 512 | -96.2 | 504990 | 912 | -103.6 | 504990 | 707 |
| MR_1774415718_96FD266B | 504990 | 913 | -91.9 | 504990 | 512 | -99.7 | 504990 | 912 | -102.0 | 504990 | 707 |
| MR_1774415718_B47EDB43 | 504990 | 913 | -88.8 | 504990 | 512 | -97.3 | 504990 | 912 | -101.5 | 504990 | 707 |
| MR_1774415718_EADCC33F | 504990 | 913 | -90.2 | 504990 | 512 | -96.2 | 504990 | 912 | -104.6 | 504990 | 707 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 205: `3ad9803f-690...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3ad9803f-6907-439f-9033-7e45e7cd6060` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Add neighbor relationship between 3228097_1 and 3276946_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[205] topology](images/train_0205.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3228097_1
- `C2`: Press down the tilt angle of 3228097_1 by 4 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276946_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276946_4
- `C5`: Adjust the azimuth of 3228097_1 by 50 degrees
- `C6`: Check test server and transmission issues
- `C7`: Decrease A3 Offset threshold for 3228097_1
- `C8`: Decrease A3 Offset threshold for 3276946_4
- `C9`: Increase A3 Offset threshold for 3276946_4
- `C10`: Increase transmission power for 3276946_4
- `C11`: Adjust the azimuth of 3276946_4 by 7 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228097_1
- `C13`: Add neighbor relationship between 3229369_2 and 3276946_4
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Lift the tilt angle of 3228097_1 by 4 degrees
- `C16`: Decrease transmission power for 3228097_1
- `C17`: Press down the tilt angle  of 3276946_4 by 6 degrees
- `C18`: Add neighbor relationship between 3228097_1 and 3276946_4 **← 정답**
- `C19`: Decrease transmission power for 3276946_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228097_1
- `C21`: Increase A3 Offset threshold for 3228097_1
- `C22`: Lift the tilt angle  of 3276946_4 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.524 | MS1 | 121.4656745599 | 31.1446378636 | 288 | 504990 | -76.56 | 15.40 | 473.03 | 0.10 | 2.95 | 1569 |
| 2024-09-20 22:21:32.910 | MS1 | 121.4656646114 | 31.1446212366 | 288 | 504990 | -78.81 | 17.80 | 397.53 | 0.11 | 2.40 | 1575 |
| 2024-09-20 22:21:33.897 | MS1 | 121.4656666769 | 31.1446265013 | 288 | 504990 | -79.72 | 14.52 | 335.90 | 0.20 | 2.82 | 1566 |
| 2024-09-20 22:21:34.718 | MS1 | 121.4656728783 | 31.1446331591 | 288 | 504990 | -85.84 | -2.68 | 37.80 | 0.12 | 1.19 | 1588 |
| 2024-09-20 22:21:35.144 | MS1 | 121.4656661169 | 31.1446254148 | 288 | 504990 | -85.45 | -3.82 | 54.90 | 0.09 | 1.29 | 1580 |
| 2024-09-20 22:21:36.988 | MS1 | 121.4656675671 | 31.1446191466 | 288 | 504990 | -87.31 | -2.36 | 45.36 | 0.07 | 1.06 | 1566 |
| 2024-09-20 22:21:37.692 | MS1 | 121.4656679288 | 31.1446324199 | 288 | 504990 | -89.66 | -2.23 | 36.03 | 0.01 | 1.39 | 1586 |
| 2024-09-20 22:21:38.810 | MS1 | 121.4656699236 | 31.1446352156 | 288 | 504990 | -75.85 | 14.24 | 472.92 | 0.04 | 1.25 | 1582 |
| 2024-09-20 22:21:39.968 | MS1 | 121.4656704856 | 31.1446201022 | 288 | 504990 | -81.92 | 15.19 | 563.08 | 0.16 | 1.42 | 1590 |
| 2024-09-20 22:21:40.558 | MS1 | 121.4656776125 | 31.1446190392 | 288 | 504990 | -78.14 | 13.37 | 505.25 | 0.04 | 2.32 | 1569 |
| 2024-09-20 22:21:41.592 | MS1 | 121.4656619962 | 31.1446273784 | 288 | 504990 | -79.95 | 12.20 | 322.90 | 0.15 | 2.02 | 1581 |
| 2024-09-20 22:21:42.517 | MS1 | 121.4656711771 | 31.1446346284 | 288 | 504990 | -75.26 | 14.40 | 381.19 | 0.08 | 2.55 | 1585 |

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
| 3228097 | 1 | 121.4744620944 | 31.1556039437 | 325 | 3 | 8 | 29.0 | TDD | 288 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3229369 | 2 | 121.4667431531 | 31.1542928140 | 16 | 0 | 9 | 24.2 | TDD | 826 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3267645 | 3 | 121.4680878306 | 31.1452857511 | 20 | 1 | 4 | 21.9 | TDD | 861 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3276946 | 4 | 121.4729609422 | 31.1531935578 | 223 | 4 | 6 | 36.9 | TDD | 318 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.733 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.751 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.899 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.899 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.633 | NREventA3 | measId:2;ServCellPCI:402;Se... |
| 2024-09-20 22:21:35.633 | NREventA3 | measId:2;ServCellPCI:402;Se... |
| 2024-09-20 22:21:36.633 | NREventA3 | measId:2;ServCellPCI:402;Se... |
| 2024-09-20 22:21:39.133 | NRRRCReestablishAttempt | PCI:402 |
| 2024-09-20 22:21:39.149 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.164 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.314 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.314 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228097 | 1 | 17.3003 | 16.9939 | -114.1456 | 16.1731 | 180.9794 | 0.0152 | 0.1071 |
| 2024_09_20 22:00 | 3229369 | 2 | 18.6021 | 16.0248 | -116.1972 | 9.1124 | 193.5775 | 0.0069 | 0.0166 |
| 2024_09_20 22:00 | 3267645 | 3 | 6.9243 | 18.6123 | -117.6265 | 6.5359 | 86.1913 | 0.0037 | 0.0094 |
| 2024_09_20 22:00 | 3276946 | 4 | 12.0063 | 5.6055 | -114.9733 | 19.7301 | 108.2464 | 0.0068 | 0.0072 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414938_1BA64233 | 504990 | 288 | -87.4 | 504990 | 318 | -80.3 | 504990 | 826 | -88.6 | 504990 | 861 |
| MR_1774414938_C0F929A2 | 504990 | 318 | -82.9 | 504990 | 288 | -87.5 | 504990 | 826 | -87.5 | 504990 | 861 |
| MR_1774414938_C77160A5 | 504990 | 288 | -86.5 | 504990 | 318 | -79.5 | 504990 | 826 | -86.4 | 504990 | 861 |
| MR_1774414938_4564044D | 504990 | 288 | -86.0 | 504990 | 318 | -82.3 | 504990 | 826 | -87.3 | 504990 | 861 |
| MR_1774414938_0AD0E544 | 504990 | 288 | -87.4 | 504990 | 318 | -79.2 | 504990 | 826 | -89.3 | 504990 | 861 |
| MR_1774414938_9AB09C2C | 504990 | 318 | -82.0 | 504990 | 288 | -87.1 | 504990 | 826 | -87.1 | 504990 | 861 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 206: `b5f6b441-a89...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b5f6b441-a898-45dd-8e83-9cc47ae1303b` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3246390_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[206] topology](images/train_0206.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3256880_4 by 10 degrees
- `C2`: Decrease A3 Offset threshold for 3246390_3
- `C3`: Adjust the azimuth of 3246390_3 by 40 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246390_3
- `C6`: Press down the tilt angle of 3246390_3 by 4 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246390_3 **← 정답**
- `C8`: Increase transmission power for 3246390_3
- `C9`: Decrease transmission power for 3256880_4
- `C10`: Decrease A3 Offset threshold for 3256880_4
- `C11`: Lift the tilt angle  of 3256880_4 by 10 degrees
- `C12`: Increase A3 Offset threshold for 3246390_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256880_4
- `C14`: Add neighbor relationship between 3236946_1 and 3256880_4
- `C15`: Check test server and transmission issues
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256880_4
- `C17`: Add neighbor relationship between 3246390_3 and 3256880_4
- `C18`: Adjust the azimuth of 3256880_4 by 50 degrees
- `C19`: Increase transmission power for 3256880_4
- `C20`: Lift the tilt angle of 3246390_3 by 4 degrees
- `C21`: Decrease transmission power for 3246390_3
- `C22`: Increase A3 Offset threshold for 3256880_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.358 | MS1 | 121.4656734441 | 31.1446353839 | 861 | 504990 | -87.86 | 14.98 | 536.78 | 0.06 | 2.97 | 1587 |
| 2024-09-20 22:21:32.869 | MS1 | 121.4656645772 | 31.1446235160 | 861 | 504990 | -88.77 | 17.77 | 590.95 | 0.02 | 2.45 | 1570 |
| 2024-09-20 22:21:33.807 | MS1 | 121.4656613653 | 31.1446297387 | 861 | 504990 | -91.35 | 14.48 | 491.12 | 0.14 | 2.28 | 1584 |
| 2024-09-20 22:21:34.821 | MS1 | 121.4656620207 | 31.1446214305 | 861 | 504990 | -91.11 | 14.55 | 53.18 | 0.69 | 2.09 | 596 |
| 2024-09-20 22:21:35.752 | MS1 | 121.4656590814 | 31.1446254731 | 861 | 504990 | -89.47 | 14.43 | 55.22 | 0.68 | 2.88 | 641 |
| 2024-09-20 22:21:36.837 | MS1 | 121.4656663496 | 31.1446256726 | 861 | 504990 | -86.61 | 17.03 | 75.93 | 0.61 | 2.87 | 680 |
| 2024-09-20 22:21:37.677 | MS1 | 121.4656595131 | 31.1446205971 | 861 | 504990 | -93.14 | 11.81 | 72.61 | 0.67 | 2.58 | 561 |
| 2024-09-20 22:21:38.280 | MS1 | 121.4656693778 | 31.1446247327 | 861 | 504990 | -91.21 | 12.43 | 75.18 | 0.51 | 2.12 | 571 |
| 2024-09-20 22:21:39.492 | MS1 | 121.4656682182 | 31.1446351633 | 861 | 504990 | -89.84 | 9.74 | 73.55 | 0.68 | 2.64 | 585 |
| 2024-09-20 22:21:40.935 | MS1 | 121.4656684470 | 31.1446322248 | 861 | 504990 | -90.78 | 12.51 | 502.90 | 0.17 | 2.59 | 1574 |
| 2024-09-20 22:21:41.589 | MS1 | 121.4656717924 | 31.1446373034 | 861 | 504990 | -93.59 | 10.19 | 421.44 | 0.07 | 2.45 | 1600 |
| 2024-09-20 22:21:42.668 | MS1 | 121.4656656770 | 31.1446296062 | 861 | 504990 | -92.30 | 11.28 | 556.52 | 0.12 | 2.83 | 1589 |

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
| 3236946 | 1 | 121.4677727518 | 31.1526846702 | 322 | 14 | 7 | 18.6 | TDD | 168 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3237852 | 2 | 121.4747401199 | 31.1496146586 | 126 | 12 | 1 | 27.6 | TDD | 82 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3246390 | 3 | 121.4715584028 | 31.1516462527 | 256 | 1 | 2 | 44.9 | TDD | 861 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3256880 | 4 | 121.4677320717 | 31.1440421112 | 77 | 13 | 8 | 32.5 | TDD | 997 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.627 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.651 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.788 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.788 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.428 | NREventA3 | measId:2;ServCellPCI:274;Se... |
| 2024-09-20 22:21:38.668 | NRHandoverAttempt | SourcePCI:274;SourceNR-ARFC... |
| 2024-09-20 22:21:38.712 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.726 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.856 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.856 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236946 | 1 | 13.8115 | 14.9447 | -114.8991 | 17.7715 | 122.4130 | 0.0123 | 0.0161 |
| 2024_09_20 22:00 | 3237852 | 2 | 16.6243 | 5.2204 | -114.1015 | 9.4420 | 86.8664 | 0.0012 | 0.0180 |
| 2024_09_20 22:00 | 3246390 | 3 | 15.5704 | 17.7846 | -117.3125 | 6.2347 | 100.1519 | 0.0101 | 0.0108 |
| 2024_09_20 22:00 | 3256880 | 4 | 18.6535 | 11.1016 | -115.0714 | 15.1225 | 121.6328 | 0.0064 | 0.0020 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415836_FF49A5B5 | 504990 | 861 | -89.9 | 504990 | 997 | -94.9 | 504990 | 168 | -102.1 | 504990 | 82 |
| MR_1774415836_9F31E836 | 504990 | 861 | -92.0 | 504990 | 997 | -98.5 | 504990 | 168 | -103.8 | 504990 | 82 |
| MR_1774415836_54415D2C | 504990 | 861 | -89.4 | 504990 | 997 | -96.3 | 504990 | 168 | -103.8 | 504990 | 82 |
| MR_1774415836_1E13BEC3 | 504990 | 861 | -89.4 | 504990 | 997 | -95.5 | 504990 | 168 | -103.0 | 504990 | 82 |
| MR_1774415836_E7BE7C91 | 504990 | 861 | -91.7 | 504990 | 997 | -97.0 | 504990 | 168 | -104.5 | 504990 | 82 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 207: `1fdd16f9-586...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1fdd16f9-5863-4a4b-bb42-180de5786522` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Lift the tilt angle  of 3277643_4 by 6 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[207] topology](images/train_0207.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3277643_4 by 6 degrees
- `C2`: Increase A3 Offset threshold for 3253097_3
- `C3`: Check test server and transmission issues
- `C4`: Adjust the azimuth of 3277643_4 by 50 degrees
- `C5`: Lift the tilt angle of 3252617_2 by 3 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252617_2
- `C7`: Increase transmission power for 3253097_3
- `C8`: Decrease A3 Offset threshold for 3252617_2
- `C9`: Decrease transmission power for 3252617_2
- `C10`: Increase A3 Offset threshold for 3252617_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253097_3
- `C12`: Add neighbor relationship between 3252617_2 and 3253097_3
- `C13`: Adjust the azimuth of 3252617_2 by 32 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252617_2
- `C15`: Increase transmission power for 3252617_2
- `C16`: Press down the tilt angle of 3252617_2 by 3 degrees
- `C17`: Add neighbor relationship between 3277643_4 and 3253097_3
- `C18`: Decrease transmission power for 3253097_3
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253097_3
- `C21`: Lift the tilt angle  of 3277643_4 by 6 degrees **← 정답**
- `C22`: Decrease A3 Offset threshold for 3253097_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.508 | MS1 | 121.4656652934 | 31.1446274526 | 235 | 504990 | -86.73 | 16.63 | 503.79 | 0.18 | 3.00 | 1576 |
| 2024-09-20 22:21:32.219 | MS1 | 121.4656767506 | 31.1446317269 | 235 | 504990 | -91.96 | 16.07 | 541.32 | 0.02 | 2.23 | 1598 |
| 2024-09-20 22:21:33.257 | MS1 | 121.4656640751 | 31.1446325366 | 235 | 504990 | -91.08 | 14.26 | 355.45 | 0.03 | 2.64 | 1577 |
| 2024-09-20 22:21:34.842 | MS1 | 121.4656768354 | 31.1446188016 | 235 | 504990 | -85.21 | 13.45 | 65.42 | 0.12 | 2.38 | 1577 |
| 2024-09-20 22:21:35.616 | MS1 | 121.4656684682 | 31.1446365576 | 235 | 504990 | -88.11 | 17.38 | 94.56 | 0.07 | 2.51 | 1563 |
| 2024-09-20 22:21:36.722 | MS1 | 121.4656715320 | 31.1446256859 | 235 | 504990 | -88.61 | 14.32 | 83.89 | 0.14 | 2.59 | 1587 |
| 2024-09-20 22:21:37.946 | MS1 | 121.4656768176 | 31.1446340284 | 235 | 504990 | -92.52 | 7.32 | 54.63 | 0.17 | 2.59 | 1594 |
| 2024-09-20 22:21:38.135 | MS1 | 121.4656692029 | 31.1446193921 | 235 | 504990 | -93.70 | 10.41 | 89.41 | 0.12 | 2.12 | 1594 |
| 2024-09-20 22:21:39.733 | MS1 | 121.4656635058 | 31.1446368536 | 235 | 504990 | -92.37 | 11.90 | 74.61 | 0.13 | 2.52 | 1563 |
| 2024-09-20 22:21:40.160 | MS1 | 121.4656670712 | 31.1446338614 | 235 | 504990 | -90.75 | 7.88 | 322.22 | 0.04 | 2.19 | 1594 |
| 2024-09-20 22:21:41.734 | MS1 | 121.4656661484 | 31.1446266529 | 235 | 504990 | -90.42 | 9.40 | 335.14 | 0.06 | 2.01 | 1582 |
| 2024-09-20 22:21:42.421 | MS1 | 121.4656750741 | 31.1446379301 | 235 | 504990 | -93.94 | 10.29 | 381.66 | 0.04 | 2.84 | 1585 |

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
| 3252617 | 2 | 121.4756386694 | 31.1502553465 | 269 | 2 | 2 | 26.2 | TDD | 235 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3253097 | 3 | 121.4722761480 | 31.1542390799 | 22 | 5 | 0 | 21.4 | TDD | 14 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3265601 | 1 | 121.4710479165 | 31.1548942665 | 58 | 1 | 4 | 26.1 | TDD | 256 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3277643 | 4 | 121.4678376733 | 31.1505043241 | 114 | 13 | 12 | 19.5 | TDD | 758 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.306 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.324 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.458 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.458 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.178 | NREventA3 | measId:2;ServCellPCI:887;Se... |
| 2024-09-20 22:21:38.418 | NRHandoverAttempt | SourcePCI:887;SourceNR-ARFC... |
| 2024-09-20 22:21:38.468 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.480 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.593 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.593 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265601 | 1 | 18.2685 | 14.1755 | -116.1839 | 12.2916 | 168.4090 | 0.0009 | 0.0058 |
| 2024_09_20 22:00 | 3252617 | 2 | 82.1635 | 80.4524 | -115.4465 | 10.2178 | 115.9348 | 0.0046 | 0.0135 |
| 2024_09_20 22:00 | 3253097 | 3 | 17.1501 | 9.5605 | -114.8147 | 12.8601 | 157.7799 | 0.0094 | 0.0182 |
| 2024_09_20 22:00 | 3277643 | 4 | 6.2698 | 14.2484 | -117.8053 | 11.9310 | 97.6827 | 0.0012 | 0.0144 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414554_C09BD20B | 504990 | 235 | -83.6 | 504990 | 14 | -86.2 | 504990 | 758 | -89.9 | 504990 | 256 |
| MR_1774414554_D6BDC4D0 | 504990 | 235 | -85.7 | 504990 | 14 | -87.3 | 504990 | 758 | -90.4 | 504990 | 256 |
| MR_1774414554_20B24059 | 504990 | 235 | -83.4 | 504990 | 14 | -87.8 | 504990 | 758 | -89.7 | 504990 | 256 |
| MR_1774414554_0C5D5410 | 504990 | 235 | -86.2 | 504990 | 14 | -84.6 | 504990 | 758 | -91.3 | 504990 | 256 |
| MR_1774414554_4C49A877 | 504990 | 235 | -86.1 | 504990 | 14 | -85.7 | 504990 | 758 | -90.5 | 504990 | 256 |
| MR_1774414554_4A9FDC8C | 504990 | 235 | -83.6 | 504990 | 14 | -86.6 | 504990 | 758 | -90.7 | 504990 | 256 |
| MR_1774414554_E2AA04EA | 504990 | 235 | -86.2 | 504990 | 14 | -88.2 | 504990 | 758 | -92.8 | 504990 | 256 |
| MR_1774414554_ED60A5B6 | 504990 | 235 | -83.4 | 504990 | 14 | -88.1 | 504990 | 758 | -91.3 | 504990 | 256 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 208: `9c7713be-b19...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9c7713be-b199-4897-8a16-4c0d4d4fa254` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[208] topology](images/train_0208.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3266568_1
- `C2`: Increase A3 Offset threshold for 3266932_3
- `C3`: Press down the tilt angle of 3266932_3 by 10 degrees
- `C4`: Press down the tilt angle  of 3266568_1 by 7 degrees
- `C5`: Add neighbor relationship between 3252433_4 and 3266568_1
- `C6`: Check test server and transmission issues
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266932_3
- `C8`: Increase A3 Offset threshold for 3266568_1
- `C9`: Decrease A3 Offset threshold for 3266932_3
- `C10`: Increase transmission power for 3266932_3
- `C11`: Lift the tilt angle  of 3266568_1 by 7 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266932_3
- `C13`: Decrease A3 Offset threshold for 3266568_1
- `C14`: Add neighbor relationship between 3266932_3 and 3266568_1
- `C15`: Adjust the azimuth of 3266932_3 by 50 degrees
- `C16`: Lift the tilt angle of 3266932_3 by 10 degrees
- `C17`: Increase transmission power for 3266568_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266568_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266568_1
- `C20`: Adjust the azimuth of 3266568_1 by 3 degrees
- `C21`: Decrease transmission power for 3266932_3
- `C22`: Insufficient data; more data is needed for judgment. **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.301 | MS1 | 121.4656580232 | 31.1446264187 | 548 | 504990 | -88.09 | 13.80 | 510.81 | 0.08 | 2.31 | 1573 |
| 2024-09-20 22:21:32.243 | MS1 | 121.4656688768 | 31.1446361351 | 548 | 504990 | -89.33 | 12.36 | 410.69 | 0.05 | 2.59 | 1600 |
| 2024-09-20 22:21:33.143 | MS1 | 121.4656753395 | 31.1446208132 | 548 | 504990 | -88.21 | 13.44 | 322.34 | 0.08 | 2.15 | 1577 |
| 2024-09-20 22:21:34.314 | MS1 | 121.4656644148 | 31.1446219088 | 548 | 504990 | -85.39 | 16.79 | 56.58 | 0.18 | 2.07 | 1560 |
| 2024-09-20 22:21:35.412 | MS1 | 121.4656584719 | 31.1446361124 | 548 | 504990 | -89.34 | 13.29 | 88.39 | 0.05 | 2.47 | 1593 |
| 2024-09-20 22:21:36.148 | MS1 | 121.4656617128 | 31.1446321748 | 548 | 504990 | -90.03 | 16.11 | 105.65 | 0.03 | 2.02 | 1585 |
| 2024-09-20 22:21:37.815 | MS1 | 121.4656586935 | 31.1446295095 | 548 | 504990 | -93.75 | 11.50 | 63.31 | 0.10 | 2.11 | 1570 |
| 2024-09-20 22:21:38.746 | MS1 | 121.4656684281 | 31.1446364815 | 548 | 504990 | -90.77 | 8.67 | 75.00 | 0.11 | 2.47 | 1598 |
| 2024-09-20 22:21:39.221 | MS1 | 121.4656582302 | 31.1446301947 | 548 | 504990 | -91.54 | 11.61 | 75.99 | 0.12 | 2.81 | 1598 |
| 2024-09-20 22:21:40.104 | MS1 | 121.4656738170 | 31.1446219625 | 548 | 504990 | -93.31 | 12.62 | 349.78 | 0.14 | 2.89 | 1571 |
| 2024-09-20 22:21:41.313 | MS1 | 121.4656624383 | 31.1446217168 | 548 | 504990 | -89.22 | 12.85 | 558.16 | 0.02 | 2.68 | 1578 |
| 2024-09-20 22:21:42.449 | MS1 | 121.4656717705 | 31.1446224153 | 548 | 504990 | -92.66 | 9.73 | 383.17 | 0.11 | 2.71 | 1568 |

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
| 3247684 | 2 | 121.4698039201 | 31.1558167923 | 77 | 9 | 11 | 45.7 | TDD | 731 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3252433 | 4 | 121.4677118828 | 31.1457105404 | 310 | 1 | 9 | 36.2 | TDD | 365 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3266568 | 1 | 121.4700222030 | 31.1460582036 | 252 | 3 | 11 | 30.1 | TDD | 401 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3266932 | 3 | 121.4657016748 | 31.1441943297 | 160 | 2 | 11 | 22.8 | TDD | 548 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.081 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.188 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.188 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.885 | NREventA3 | measId:2;ServCellPCI:216;Se... |
| 2024-09-20 22:21:38.125 | NRHandoverAttempt | SourcePCI:216;SourceNR-ARFC... |
| 2024-09-20 22:21:38.159 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.170 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.306 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.306 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3266568 | 1 | 77.8747 | 79.4033 | -117.5000 | 19.7887 | 162.9093 | 0.0097 | 0.0185 |
| 2024_09_19 22:00 | 3247684 | 2 | 90.6321 | 86.0119 | -116.8974 | 6.2641 | 162.4309 | 0.0104 | 0.0055 |
| 2024_09_19 22:00 | 3266932 | 3 | 94.4872 | 76.9807 | -114.2574 | 15.3611 | 157.8439 | 0.0103 | 0.0128 |
| 2024_09_19 22:00 | 3252433 | 4 | 89.1713 | 77.8930 | -117.0255 | 14.5500 | 86.5839 | 0.0040 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416516_94ECB633 | 504990 | 548 | -87.1 | 504990 | 401 | -87.8 | 504990 | 365 | -94.6 | 504990 | 731 |
| MR_1774416516_41893E22 | 504990 | 548 | -84.7 | 504990 | 401 | -88.3 | 504990 | 365 | -93.5 | 504990 | 731 |
| MR_1774416516_003C9A06 | 504990 | 548 | -84.0 | 504990 | 401 | -90.3 | 504990 | 365 | -93.4 | 504990 | 731 |
| MR_1774416516_C6F5329A | 504990 | 548 | -84.5 | 504990 | 401 | -90.9 | 504990 | 365 | -94.7 | 504990 | 731 |
| MR_1774416516_27ABAD63 | 504990 | 548 | -84.6 | 504990 | 401 | -89.1 | 504990 | 365 | -93.8 | 504990 | 731 |
| MR_1774416516_282B92A1 | 504990 | 548 | -84.5 | 504990 | 401 | -87.9 | 504990 | 365 | -94.4 | 504990 | 731 |
| MR_1774416516_C982E1CA | 504990 | 548 | -85.0 | 504990 | 401 | -90.3 | 504990 | 365 | -92.5 | 504990 | 731 |
| MR_1774416516_CB94801D | 504990 | 548 | -87.2 | 504990 | 401 | -91.1 | 504990 | 365 | -94.3 | 504990 | 731 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 209: `66ed18f8-8c0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `66ed18f8-8c03-4433-8e94-3924f7b9edbc` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[209] topology](images/train_0209.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3262909_1 by 10 degrees
- `C2`: Decrease transmission power for 3230842_4
- `C3`: Increase A3 Offset threshold for 3262909_1
- `C4`: Increase transmission power for 3262909_1
- `C5`: Press down the tilt angle of 3262909_1 by 10 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230842_4
- `C7`: Decrease A3 Offset threshold for 3262909_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Adjust the azimuth of 3230842_4 by 50 degrees
- `C10`: Press down the tilt angle  of 3230842_4 by 3 degrees
- `C11`: Adjust the azimuth of 3262909_1 by 46 degrees
- `C12`: Increase A3 Offset threshold for 3230842_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262909_1
- `C14`: Add neighbor relationship between 3236091_3 and 3230842_4
- `C15`: Decrease transmission power for 3262909_1
- `C16`: Add neighbor relationship between 3262909_1 and 3230842_4
- `C17`: Lift the tilt angle  of 3230842_4 by 3 degrees
- `C18`: Check test server and transmission issues **← 정답**
- `C19`: Decrease A3 Offset threshold for 3230842_4
- `C20`: Increase transmission power for 3230842_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230842_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262909_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.640 | MS1 | 121.4656589358 | 31.1446252166 | 136 | 504990 | -90.12 | 16.94 | 407.79 | 0.02 | 2.90 | 1568 |
| 2024-09-20 22:21:32.655 | MS1 | 121.4656737481 | 31.1446253709 | 136 | 504990 | -88.39 | 16.47 | 331.98 | 0.17 | 2.69 | 1572 |
| 2024-09-20 22:21:33.421 | MS1 | 121.4656695149 | 31.1446280252 | 136 | 504990 | -88.43 | 14.66 | 388.83 | 0.13 | 2.87 | 1577 |
| 2024-09-20 22:21:34.349 | MS1 | 121.4656661737 | 31.1446364198 | 136 | 504990 | -88.79 | 14.99 | 78.29 | 0.14 | 2.36 | 326 |
| 2024-09-20 22:21:35.120 | MS1 | 121.4656749308 | 31.1446230270 | 136 | 504990 | -90.57 | 12.11 | 59.38 | 0.01 | 2.25 | 494 |
| 2024-09-20 22:21:36.957 | MS1 | 121.4656619642 | 31.1446254604 | 136 | 504990 | -86.68 | 15.59 | 65.53 | 0.00 | 2.56 | 499 |
| 2024-09-20 22:21:37.745 | MS1 | 121.4656681303 | 31.1446337804 | 136 | 504990 | -91.93 | 11.17 | 64.39 | 0.12 | 2.31 | 435 |
| 2024-09-20 22:21:38.545 | MS1 | 121.4656747398 | 31.1446354694 | 136 | 504990 | -92.74 | 7.86 | 97.23 | 0.18 | 2.99 | 391 |
| 2024-09-20 22:21:39.172 | MS1 | 121.4656676976 | 31.1446217458 | 136 | 504990 | -93.68 | 12.69 | 81.92 | 0.11 | 2.88 | 368 |
| 2024-09-20 22:21:40.796 | MS1 | 121.4656756947 | 31.1446230833 | 136 | 504990 | -89.56 | 10.44 | 579.99 | 0.04 | 2.75 | 1581 |
| 2024-09-20 22:21:41.315 | MS1 | 121.4656609512 | 31.1446262159 | 136 | 504990 | -89.62 | 8.30 | 378.95 | 0.12 | 2.12 | 1569 |
| 2024-09-20 22:21:42.975 | MS1 | 121.4656706034 | 31.1446240293 | 136 | 504990 | -93.91 | 11.24 | 332.85 | 0.08 | 2.54 | 1574 |

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
| 3230842 | 4 | 121.4666394168 | 31.1509210144 | 73 | 1 | 0 | 22.4 | TDD | 832 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3236091 | 3 | 121.4664182144 | 31.1460352143 | 208 | 5 | 7 | 30.4 | TDD | 843 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3262909 | 1 | 121.4678808518 | 31.1473120149 | 261 | 15 | 2 | 47.6 | TDD | 136 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3272611 | 2 | 121.4759560537 | 31.1552128703 | 207 | 11 | 5 | 24.7 | TDD | 145 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.627 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.645 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.788 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.788 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.429 | NREventA3 | measId:2;ServCellPCI:892;Se... |
| 2024-09-20 22:21:38.669 | NRHandoverAttempt | SourcePCI:892;SourceNR-ARFC... |
| 2024-09-20 22:21:38.702 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.714 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.817 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.817 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262909 | 1 | 11.7024 | 13.5615 | -116.7270 | 14.0111 | 111.5495 | 0.0141 | 0.0126 |
| 2024_09_20 22:00 | 3272611 | 2 | 5.5332 | 17.3742 | -117.2862 | 15.8463 | 86.1625 | 0.0089 | 0.0156 |
| 2024_09_20 22:00 | 3236091 | 3 | 6.1257 | 10.9006 | -117.7492 | 11.5357 | 192.9235 | 0.0051 | 0.0198 |
| 2024_09_20 22:00 | 3230842 | 4 | 13.3969 | 13.1314 | -117.3727 | 12.6767 | 96.9952 | 0.0198 | 0.0022 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413397_0EC28AAA | 504990 | 136 | -87.4 | 504990 | 832 | -89.1 | 504990 | 843 | -96.7 | 504990 | 145 |
| MR_1774413397_3EB5761D | 504990 | 136 | -90.6 | 504990 | 832 | -90.8 | 504990 | 843 | -99.1 | 504990 | 145 |
| MR_1774413397_C28955E6 | 504990 | 136 | -88.9 | 504990 | 832 | -92.2 | 504990 | 843 | -96.3 | 504990 | 145 |
| MR_1774413397_5CEC7F45 | 504990 | 136 | -89.0 | 504990 | 832 | -92.6 | 504990 | 843 | -98.6 | 504990 | 145 |
| MR_1774413397_2F66D812 | 504990 | 136 | -90.1 | 504990 | 832 | -89.1 | 504990 | 843 | -98.6 | 504990 | 145 |
| MR_1774413397_C01F80A4 | 504990 | 136 | -86.8 | 504990 | 832 | -89.2 | 504990 | 843 | -96.6 | 504990 | 145 |
| MR_1774413397_3031C075 | 504990 | 136 | -88.4 | 504990 | 832 | -91.1 | 504990 | 843 | -99.4 | 504990 | 145 |

> *... 2개 열 생략 (전체 14열)*

---
