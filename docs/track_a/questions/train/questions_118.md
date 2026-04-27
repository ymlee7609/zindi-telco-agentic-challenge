# Track A 문제 분석 — train[1170]~train[1179]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1170] ~ train[1179] (10개)

## 목차

1. [문제 1170: `4719108e-04f...`](#1170) — single-answer, 정답: C11
2. [문제 1171: `082dc7af-2f7...`](#1171) — single-answer, 정답: C1
3. [문제 1172: `1be127b0-19a...`](#1172) — single-answer, 정답: C18
4. [문제 1173: `df185f76-8e6...`](#1173) — single-answer, 정답: C17
5. [문제 1174: `7b22fd7c-baf...`](#1174) — single-answer, 정답: C4
6. [문제 1175: `9f2c26dd-f3a...`](#1175) — single-answer, 정답: C20
7. [문제 1176: `cde7fe21-58c...`](#1176) — single-answer, 정답: C11
8. [문제 1177: `827db385-d42...`](#1177) — single-answer, 정답: C17
9. [문제 1178: `59bdf520-fee...`](#1178) — single-answer, 정답: C10
10. [문제 1179: `1a465575-625...`](#1179) — single-answer, 정답: C11

---

### 문제 1170: `4719108e-04f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4719108e-04f4-4123-8c43-9d480bd97cfe` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease A3 Offset threshold for 3213338_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1170] topology](images/train_1170.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3213338_1 and 3229054_2
- `C2`: Check test server and transmission issues
- `C3`: Adjust the azimuth of 3229054_2 by 50 degrees
- `C4`: Increase transmission power for 3213338_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229054_2
- `C6`: Add neighbor relationship between 3242228_3 and 3229054_2
- `C7`: Adjust the azimuth of 3213338_1 by 13 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213338_1
- `C9`: Lift the tilt angle of 3213338_1 by 10 degrees
- `C10`: Increase transmission power for 3229054_2
- `C11`: Decrease A3 Offset threshold for 3213338_1 **← 정답**
- `C12`: Decrease transmission power for 3213338_1
- `C13`: Decrease transmission power for 3229054_2
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Lift the tilt angle  of 3229054_2 by 10 degrees
- `C16`: Decrease A3 Offset threshold for 3229054_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213338_1
- `C18`: Press down the tilt angle of 3213338_1 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3213338_1
- `C20`: Press down the tilt angle  of 3229054_2 by 10 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229054_2
- `C22`: Increase A3 Offset threshold for 3229054_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.738 | MS1 | 121.4656735284 | 31.1446189042 | 681 | 504990 | -79.47 | 16.66 | 332.80 | 0.18 | 2.62 | 1592 |
| 2024-09-20 22:21:32.582 | MS1 | 121.4656769072 | 31.1446375142 | 681 | 504990 | -76.60 | 14.29 | 558.88 | 0.02 | 2.37 | 1565 |
| 2024-09-20 22:21:33.937 | MS1 | 121.4656686874 | 31.1446273768 | 681 | 504990 | -80.09 | 13.56 | 573.16 | 0.03 | 2.16 | 1593 |
| 2024-09-20 22:21:34.301 | MS1 | 121.4656664939 | 31.1446197614 | 681 | 504990 | -85.68 | -0.59 | 47.47 | 0.02 | 1.26 | 1592 |
| 2024-09-20 22:21:35.710 | MS1 | 121.4656717679 | 31.1446266940 | 681 | 504990 | -89.18 | -2.00 | 56.98 | 0.13 | 1.08 | 1578 |
| 2024-09-20 22:21:36.304 | MS1 | 121.4656671590 | 31.1446276926 | 681 | 504990 | -89.84 | -1.25 | 59.58 | 0.19 | 1.00 | 1588 |
| 2024-09-20 22:21:37.322 | MS1 | 121.4656587769 | 31.1446214147 | 681 | 504990 | -92.16 | -0.09 | 39.01 | 0.06 | 1.06 | 1576 |
| 2024-09-20 22:21:38.134 | MS1 | 121.4656610586 | 31.1446365941 | 681 | 504990 | -84.61 | -1.72 | 57.30 | 0.14 | 1.04 | 1596 |
| 2024-09-20 22:21:39.881 | MS1 | 121.4656681349 | 31.1446346618 | 255 | 504990 | -82.11 | 16.41 | 249.05 | 0.10 | 1.48 | 1596 |
| 2024-09-20 22:21:40.594 | MS1 | 121.4656586764 | 31.1446340065 | 255 | 504990 | -82.38 | 16.52 | 496.21 | 0.03 | 2.35 | 1586 |
| 2024-09-20 22:21:41.361 | MS1 | 121.4656772705 | 31.1446307116 | 255 | 504990 | -76.52 | 15.90 | 435.42 | 0.14 | 2.08 | 1567 |
| 2024-09-20 22:21:42.629 | MS1 | 121.4656654032 | 31.1446185274 | 255 | 504990 | -79.65 | 13.90 | 525.16 | 0.12 | 2.65 | 1597 |

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
| 3213338 | 1 | 121.4691316546 | 31.1463674375 | 253 | 6 | 1 | 28.3 | TDD | 681 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3229054 | 2 | 121.4667226314 | 31.1557941061 | 83 | 8 | 8 | 49.7 | TDD | 255 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3242228 | 3 | 121.4714312512 | 31.1474471762 | 44 | 1 | 5 | 45.4 | TDD | 543 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3257379 | 4 | 121.4707744707 | 31.1485724830 | 111 | 13 | 5 | 44.0 | TDD | 719 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.012 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.032 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.157 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.157 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.824 | NREventA3 | measId:2;ServCellPCI:57;Ser... |
| 2024-09-20 22:21:38.064 | NRHandoverAttempt | SourcePCI:57;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.103 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.115 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.264 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.264 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213338 | 1 | 15.8336 | 13.6296 | -115.5609 | 18.3722 | 140.3310 | 0.0166 | 0.1546 |
| 2024_09_20 22:00 | 3229054 | 2 | 18.2119 | 14.4562 | -115.3606 | 14.9321 | 176.0440 | 0.0142 | 0.0153 |
| 2024_09_20 22:00 | 3242228 | 3 | 15.9184 | 15.1254 | -115.5778 | 11.1723 | 123.4098 | 0.0104 | 0.0131 |
| 2024_09_20 22:00 | 3257379 | 4 | 19.4981 | 14.3961 | -115.1192 | 5.6881 | 118.2703 | 0.0002 | 0.0008 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415757_564BC7C8 | 504990 | 681 | -85.6 | 504990 | 255 | -82.7 | 504990 | 543 | -90.1 | 504990 | 719 |
| MR_1774415757_CAE07883 | 504990 | 255 | -80.1 | 504990 | 681 | -87.1 | 504990 | 543 | -90.1 | 504990 | 719 |
| MR_1774415757_03A17D3B | 504990 | 255 | -82.1 | 504990 | 681 | -84.2 | 504990 | 543 | -88.2 | 504990 | 719 |
| MR_1774415757_0F246746 | 504990 | 681 | -84.5 | 504990 | 255 | -81.3 | 504990 | 543 | -89.9 | 504990 | 719 |
| MR_1774415757_821AC462 | 504990 | 681 | -86.4 | 504990 | 255 | -83.3 | 504990 | 543 | -89.2 | 504990 | 719 |
| MR_1774415757_84B63487 | 504990 | 681 | -84.7 | 504990 | 255 | -80.9 | 504990 | 543 | -87.7 | 504990 | 719 |
| MR_1774415757_33FC5B8A | 504990 | 681 | -85.3 | 504990 | 255 | -83.1 | 504990 | 543 | -89.7 | 504990 | 719 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1171: `082dc7af-2f7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `082dc7af-2f7c-40cc-9ae2-df3af849940a` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1171] topology](images/train_1171.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment. **← 정답**
- `C2`: Decrease A3 Offset threshold for 3234404_4
- `C3`: Increase A3 Offset threshold for 3234404_4
- `C4`: Press down the tilt angle  of 3234404_4 by 8 degrees
- `C5`: Adjust the azimuth of 3234404_4 by 50 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210537_3
- `C7`: Increase transmission power for 3234404_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234404_4
- `C9`: Decrease A3 Offset threshold for 3210537_3
- `C10`: Check test server and transmission issues
- `C11`: Adjust the azimuth of 3210537_3 by 5 degrees
- `C12`: Increase A3 Offset threshold for 3210537_3
- `C13`: Decrease transmission power for 3234404_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234404_4
- `C15`: Decrease transmission power for 3210537_3
- `C16`: Add neighbor relationship between 3223893_2 and 3234404_4
- `C17`: Increase transmission power for 3210537_3
- `C18`: Lift the tilt angle of 3210537_3 by 10 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210537_3
- `C20`: Lift the tilt angle  of 3234404_4 by 8 degrees
- `C21`: Add neighbor relationship between 3210537_3 and 3234404_4
- `C22`: Press down the tilt angle of 3210537_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.303 | MS1 | 121.4656772927 | 31.1446254783 | 398 | 504990 | -88.97 | 15.14 | 440.31 | 0.03 | 2.77 | 1571 |
| 2024-09-20 22:21:32.616 | MS1 | 121.4656653295 | 31.1446320301 | 398 | 504990 | -86.99 | 16.76 | 388.33 | 0.02 | 2.48 | 1563 |
| 2024-09-20 22:21:33.170 | MS1 | 121.4656765464 | 31.1446186348 | 398 | 504990 | -91.52 | 17.12 | 338.24 | 0.19 | 2.10 | 1597 |
| 2024-09-20 22:21:34.156 | MS1 | 121.4656687235 | 31.1446203431 | 398 | 504990 | -87.80 | 12.36 | 96.10 | 0.18 | 2.14 | 1579 |
| 2024-09-20 22:21:35.887 | MS1 | 121.4656714540 | 31.1446353353 | 398 | 504990 | -86.85 | 17.48 | 79.69 | 0.15 | 2.80 | 1587 |
| 2024-09-20 22:21:36.923 | MS1 | 121.4656744465 | 31.1446253023 | 398 | 504990 | -86.47 | 17.68 | 58.48 | 0.09 | 2.82 | 1582 |
| 2024-09-20 22:21:37.237 | MS1 | 121.4656617580 | 31.1446336662 | 398 | 504990 | -89.24 | 9.03 | 66.90 | 0.08 | 2.82 | 1583 |
| 2024-09-20 22:21:38.214 | MS1 | 121.4656703304 | 31.1446182962 | 398 | 504990 | -91.44 | 8.90 | 94.01 | 0.11 | 2.03 | 1597 |
| 2024-09-20 22:21:39.591 | MS1 | 121.4656736704 | 31.1446184623 | 398 | 504990 | -91.38 | 10.33 | 92.61 | 0.09 | 2.93 | 1568 |
| 2024-09-20 22:21:40.447 | MS1 | 121.4656715168 | 31.1446286480 | 398 | 504990 | -89.67 | 11.21 | 481.39 | 0.05 | 2.07 | 1585 |
| 2024-09-20 22:21:41.115 | MS1 | 121.4656658449 | 31.1446192416 | 398 | 504990 | -91.34 | 11.87 | 442.24 | 0.03 | 2.37 | 1589 |
| 2024-09-20 22:21:42.161 | MS1 | 121.4656720209 | 31.1446273935 | 398 | 504990 | -92.72 | 8.94 | 332.33 | 0.05 | 2.29 | 1600 |

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
| 3210471 | 1 | 121.4759646634 | 31.1525728697 | 284 | 12 | 10 | 16.9 | TDD | 329 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3210537 | 3 | 121.4655168315 | 31.1443930925 | 35 | 15 | 12 | 23.5 | TDD | 398 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3223893 | 2 | 121.4742852960 | 31.1548025881 | 187 | 15 | 4 | 29.9 | TDD | 452 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3234404 | 4 | 121.4737823871 | 31.1440952330 | 143 | 7 | 11 | 20.0 | TDD | 391 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.024 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.043 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.186 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.186 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.899 | NREventA3 | measId:2;ServCellPCI:644;Se... |
| 2024-09-20 22:21:38.139 | NRHandoverAttempt | SourcePCI:644;SourceNR-ARFC... |
| 2024-09-20 22:21:38.181 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.195 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.316 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.316 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3210471 | 1 | 94.6358 | 84.1139 | -116.6134 | 7.7079 | 149.0851 | 0.0142 | 0.0093 |
| 2024_09_19 22:00 | 3223893 | 2 | 90.8167 | 85.4349 | -115.6282 | 17.4353 | 123.6499 | 0.0098 | 0.0005 |
| 2024_09_19 22:00 | 3210537 | 3 | 87.7964 | 78.1162 | -115.4752 | 8.0748 | 137.8162 | 0.0196 | 0.0097 |
| 2024_09_19 22:00 | 3234404 | 4 | 76.9751 | 83.9907 | -115.2635 | 6.2664 | 150.3103 | 0.0191 | 0.0046 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414110_FD60E32A | 504990 | 398 | -87.1 | 504990 | 391 | -94.4 | 504990 | 452 | -96.5 | 504990 | 329 |
| MR_1774414110_895CE276 | 504990 | 398 | -87.6 | 504990 | 391 | -93.8 | 504990 | 452 | -95.5 | 504990 | 329 |
| MR_1774414110_FF925B60 | 504990 | 398 | -88.9 | 504990 | 391 | -93.7 | 504990 | 452 | -95.7 | 504990 | 329 |
| MR_1774414110_93EDB8EE | 504990 | 398 | -87.4 | 504990 | 391 | -96.6 | 504990 | 452 | -95.3 | 504990 | 329 |
| MR_1774414110_FF9489F2 | 504990 | 398 | -86.0 | 504990 | 391 | -96.8 | 504990 | 452 | -96.3 | 504990 | 329 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1172: `1be127b0-19a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1be127b0-19aa-4685-9236-765e9113706b` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242288_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1172] topology](images/train_1172.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3223056_6 by 4 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease A3 Offset threshold for 3242288_4
- `C4`: Increase A3 Offset threshold for 3223056_6
- `C5`: Decrease transmission power for 3223056_6
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223056_6
- `C7`: Add neighbor relationship between 3242288_4 and 3223056_6
- `C8`: Check test server and transmission issues
- `C9`: Adjust the azimuth of 3223056_6 by 38 degrees
- `C10`: Lift the tilt angle  of 3223056_6 by 4 degrees
- `C11`: Add neighbor relationship between 3241184_7 and 3223056_6
- `C12`: Increase A3 Offset threshold for 3242288_4
- `C13`: Increase transmission power for 3242288_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223056_6
- `C15`: Press down the tilt angle of 3242288_4 by 2 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242288_4
- `C17`: Decrease A3 Offset threshold for 3223056_6
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242288_4 **← 정답**
- `C19`: Increase transmission power for 3223056_6
- `C20`: Decrease transmission power for 3242288_4
- `C21`: Lift the tilt angle of 3242288_4 by 2 degrees
- `C22`: Adjust the azimuth of 3242288_4 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.623 | MS1 | 121.4656623717 | 31.1446207776 | 466 | 504990 | -94.53 | 9.22 | 336.72 | 0.16 | 2.69 | 1563 |
| 2024-09-20 22:21:32.114 | MS1 | 121.4656719377 | 31.1446329822 | 914 | 504990 | -93.35 | 10.37 | 478.35 | 0.03 | 2.55 | 1599 |
| 2024-09-20 22:21:33.805 | MS1 | 121.4656624702 | 31.1446184278 | 97 | 504990 | -95.62 | 10.23 | 340.44 | 0.19 | 2.49 | 1586 |
| 2024-09-20 22:21:34.921 | MS1 | 121.4656641554 | 31.1446275747 | 919 | 152650 | -89.46 | 5.84 | 88.25 | 0.19 | 1.65 | 908 |
| 2024-09-20 22:21:35.591 | MS1 | 121.4656743314 | 31.1446373736 | 793 | 152650 | -88.62 | 3.01 | 67.71 | 0.16 | 1.54 | 929 |
| 2024-09-20 22:21:36.699 | MS1 | 121.4656604286 | 31.1446346486 | 192 | 152650 | -90.60 | 7.89 | 73.52 | 0.17 | 1.75 | 991 |
| 2024-09-20 22:21:37.160 | MS1 | 121.4656699159 | 31.1446348229 | 804 | 152650 | -91.43 | 3.61 | 61.57 | 0.07 | 1.59 | 910 |
| 2024-09-20 22:21:38.373 | MS1 | 121.4656662186 | 31.1446272882 | 919 | 152650 | -88.47 | 3.57 | 92.35 | 0.02 | 1.90 | 951 |
| 2024-09-20 22:21:39.319 | MS1 | 121.4656746725 | 31.1446267703 | 793 | 152650 | -90.38 | 6.28 | 95.86 | 0.04 | 1.79 | 960 |
| 2024-09-20 22:21:40.736 | MS1 | 121.4656712609 | 31.1446366111 | 192 | 152650 | -88.93 | 5.86 | 50.26 | 0.06 | 2.95 | 1564 |
| 2024-09-20 22:21:41.556 | MS1 | 121.4656582272 | 31.1446352711 | 804 | 152650 | -89.50 | 2.58 | 69.65 | 0.08 | 2.67 | 1599 |
| 2024-09-20 22:21:42.102 | MS1 | 121.4656664604 | 31.1446231343 | 919 | 152650 | -89.34 | 3.90 | 54.09 | 0.09 | 2.78 | 1574 |

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
| 3213228 | 8 | 121.4641900350 | 31.1542215999 | 39 | 0 | 0 | 4.2 | FDD | 762 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3213830 | 1 | 121.4681503898 | 31.1516309425 | 14 | 4 | 2 | 1.8 | TDD | 896 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3219658 | 13 | 121.4707288731 | 31.1532227691 | 240 | 1 | 7 | 25.9 | FDD | 730 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3220855 | 2 | 121.4666840214 | 31.1503208973 | 26 | 10 | 1 | 18.2 | TDD | 97 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3223056 | 6 | 121.4650191391 | 31.1552326069 | 215 | 4 | 10 | 3.4 | TDD | 536 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3223296 | 11 | 121.4706012646 | 31.1448570528 | 318 | 1 | 6 | 10.6 | FDD | 919 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3241184 | 7 | 121.4651198903 | 31.1516304634 | 318 | 3 | 9 | 6.7 | FDD | 192 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3241334 | 3 | 121.4690932576 | 31.1532667647 | 175 | 3 | 0 | 23.5 | TDD | 742 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3242288 | 4 | 121.4698389170 | 31.1480831254 | 232 | 0 | 2 | 21.6 | TDD | 466 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3249165 | 9 | 121.4734175315 | 31.1454646934 | 78 | 11 | 4 | 3.4 | FDD | 804 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3262537 | 10 | 121.4648675078 | 31.1491830944 | 37 | 10 | 3 | 5.4 | FDD | 752 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3265848 | 12 | 121.4754668328 | 31.1557861665 | 21 | 4 | 8 | 18.6 | FDD | 793 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3271006 | 5 | 121.4713188660 | 31.1441504638 | 73 | 9 | 5 | 22.6 | TDD | 914 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.819 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.834 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.952 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.952 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.639 | NREventA2 | measId:1;ServCellPCI:572;Se... |
| 2024-09-20 22:21:34.782 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.010 | NREventA5 | measId:3;ServCellPCI:572;Se... |
| 2024-09-20 22:21:35.083 | NRHandoverAttempt | SourcePCI:572;SourceNR-ARFC... |
| 2024-09-20 22:21:35.105 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.117 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.243 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.243 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213830 | 1 | 19.0244 | 10.0160 | -116.9955 | 16.9590 | 114.3450 | 0.0025 | 0.0093 |
| 2024_09_20 22:00 | 3220855 | 2 | 13.6100 | 10.4190 | -115.6869 | 10.5379 | 162.7704 | 0.0196 | 0.0071 |
| 2024_09_20 22:00 | 3241334 | 3 | 12.4286 | 10.0108 | -117.1203 | 19.7500 | 126.7060 | 0.0095 | 0.0171 |
| 2024_09_20 22:00 | 3242288 | 4 | 14.7348 | 7.9038 | -116.8856 | 9.5479 | 82.7532 | 0.0016 | 0.0012 |
| 2024_09_20 22:00 | 3271006 | 5 | 11.1876 | 17.1943 | -115.7875 | 9.7240 | 127.3929 | 0.0032 | 0.0148 |
| 2024_09_20 22:00 | 3223056 | 6 | 5.1418 | 10.3720 | -116.4860 | 8.7209 | 106.1319 | 0.0009 | 0.0135 |
| 2024_09_20 22:00 | 3241184 | 7 | 8.4537 | 8.4890 | -114.8720 | 3.7570 | 28.6239 | 0.0003 | 0.0160 |
| 2024_09_20 22:00 | 3213228 | 8 | 8.7421 | 13.4362 | -116.3391 | 4.0470 | 20.4359 | 0.0170 | 0.0007 |
| 2024_09_20 22:00 | 3249165 | 9 | 10.7589 | 12.1557 | -117.9356 | 4.8686 | 40.9178 | 0.0008 | 0.0170 |
| 2024_09_20 22:00 | 3262537 | 10 | 17.7634 | 15.8087 | -116.8196 | 3.4674 | 41.6306 | 0.0185 | 0.0014 |
| 2024_09_20 22:00 | 3223296 | 11 | 11.6343 | 15.4576 | -114.3433 | 4.6346 | 33.2395 | 0.0089 | 0.0021 |
| 2024_09_20 22:00 | 3265848 | 12 | 14.1673 | 15.5476 | -115.5094 | 4.3986 | 31.8586 | 0.0011 | 0.0187 |
| 2024_09_20 22:00 | 3219658 | 13 | 12.3118 | 14.7389 | -116.7221 | 3.0150 | 47.3192 | 0.0155 | 0.0180 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415366_FF5D8C1A | 152650 | 919 | -91.3 | 152650 | 730 | -93.2 | 152650 | 752 | -99.8 | 152650 | 762 |
| MR_1774415366_5E636A84 | 504990 | 97 | -96.0 | 504990 | 536 | -96.8 | 504990 | 742 | -101.2 | 504990 | 896 |
| MR_1774415366_63784C7A | 504990 | 97 | -96.0 | 504990 | 536 | -96.0 | 504990 | 742 | -101.9 | 504990 | 896 |
| MR_1774415366_4785F353 | 504990 | 97 | -96.5 | 504990 | 536 | -97.7 | 504990 | 742 | -102.6 | 504990 | 896 |
| MR_1774415366_3A0FBB70 | 152650 | 919 | -88.7 | 152650 | 730 | -90.6 | 152650 | 752 | -100.2 | 152650 | 762 |
| MR_1774415366_C2926E8D | 152650 | 919 | -89.2 | 152650 | 730 | -90.6 | 152650 | 752 | -97.0 | 152650 | 762 |
| MR_1774415366_0F140A10 | 504990 | 97 | -96.3 | 504990 | 536 | -95.8 | 504990 | 742 | -103.1 | 504990 | 896 |
| MR_1774415366_494E28D4 | 152650 | 919 | -89.0 | 152650 | 730 | -93.1 | 152650 | 752 | -97.5 | 152650 | 762 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1173: `df185f76-8e6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `df185f76-8e6e-47b9-9496-b8358256f09d` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1173] topology](images/train_1173.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3221125_1
- `C2`: Increase A3 Offset threshold for 3267558_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221125_1
- `C4`: Adjust the azimuth of 3221125_1 by 50 degrees
- `C5`: Decrease A3 Offset threshold for 3267558_4
- `C6`: Press down the tilt angle  of 3267558_4 by 10 degrees
- `C7`: Lift the tilt angle of 3221125_1 by 10 degrees
- `C8`: Adjust the azimuth of 3267558_4 by 50 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267558_4
- `C10`: Add neighbor relationship between 3238851_2 and 3267558_4
- `C11`: Lift the tilt angle  of 3267558_4 by 10 degrees
- `C12`: Decrease transmission power for 3221125_1
- `C13`: Decrease transmission power for 3267558_4
- `C14`: Decrease A3 Offset threshold for 3221125_1
- `C15`: Add neighbor relationship between 3221125_1 and 3267558_4
- `C16`: Increase transmission power for 3221125_1
- `C17`: Check test server and transmission issues **← 정답**
- `C18`: Press down the tilt angle of 3221125_1 by 10 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221125_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267558_4
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Increase transmission power for 3267558_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.674 | MS1 | 121.4656714916 | 31.1446262525 | 176 | 504990 | -90.28 | 12.68 | 483.11 | 0.12 | 2.86 | 1573 |
| 2024-09-20 22:21:32.394 | MS1 | 121.4656760715 | 31.1446334434 | 176 | 504990 | -86.69 | 14.20 | 345.77 | 0.04 | 2.67 | 1572 |
| 2024-09-20 22:21:33.742 | MS1 | 121.4656736037 | 31.1446313290 | 176 | 504990 | -89.78 | 16.75 | 374.66 | 0.00 | 2.29 | 1595 |
| 2024-09-20 22:21:34.631 | MS1 | 121.4656744664 | 31.1446193988 | 176 | 504990 | -85.99 | 12.16 | 57.91 | 0.14 | 2.74 | 327 |
| 2024-09-20 22:21:35.488 | MS1 | 121.4656735308 | 31.1446238944 | 176 | 504990 | -86.90 | 14.10 | 102.50 | 0.08 | 2.98 | 390 |
| 2024-09-20 22:21:36.818 | MS1 | 121.4656720965 | 31.1446357041 | 176 | 504990 | -90.47 | 17.83 | 97.65 | 0.09 | 2.25 | 494 |
| 2024-09-20 22:21:37.809 | MS1 | 121.4656677809 | 31.1446193873 | 176 | 504990 | -89.71 | 9.97 | 78.08 | 0.01 | 2.40 | 468 |
| 2024-09-20 22:21:38.973 | MS1 | 121.4656676578 | 31.1446200778 | 176 | 504990 | -89.74 | 7.84 | 80.96 | 0.14 | 2.65 | 418 |
| 2024-09-20 22:21:39.199 | MS1 | 121.4656617375 | 31.1446345255 | 176 | 504990 | -91.58 | 11.98 | 68.64 | 0.18 | 2.71 | 446 |
| 2024-09-20 22:21:40.687 | MS1 | 121.4656696276 | 31.1446229212 | 176 | 504990 | -93.91 | 8.63 | 329.24 | 0.07 | 2.99 | 1600 |
| 2024-09-20 22:21:41.998 | MS1 | 121.4656734516 | 31.1446190638 | 176 | 504990 | -91.02 | 10.16 | 320.72 | 0.00 | 2.62 | 1563 |
| 2024-09-20 22:21:42.238 | MS1 | 121.4656732506 | 31.1446338637 | 176 | 504990 | -93.59 | 11.86 | 312.05 | 0.04 | 2.40 | 1591 |

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
| 3221125 | 1 | 121.4704771104 | 31.1447596340 | 349 | 12 | 11 | 15.7 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3238851 | 2 | 121.4728773902 | 31.1498341542 | 188 | 11 | 0 | 44.2 | TDD | 123 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3267558 | 4 | 121.4693220453 | 31.1551082000 | 273 | 14 | 1 | 31.0 | TDD | 1003 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3272464 | 3 | 121.4759811914 | 31.1460423427 | 279 | 2 | 8 | 45.9 | TDD | 941 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.196 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.214 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.355 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.355 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.043 | NREventA3 | measId:2;ServCellPCI:127;Se... |
| 2024-09-20 22:21:38.283 | NRHandoverAttempt | SourcePCI:127;SourceNR-ARFC... |
| 2024-09-20 22:21:38.329 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.341 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.461 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.461 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221125 | 1 | 17.1569 | 19.1226 | -117.6305 | 8.5690 | 170.6382 | 0.0041 | 0.0056 |
| 2024_09_20 22:00 | 3238851 | 2 | 10.6924 | 10.4806 | -117.7609 | 7.7112 | 103.9906 | 0.0177 | 0.0106 |
| 2024_09_20 22:00 | 3272464 | 3 | 14.9383 | 9.7280 | -115.8638 | 11.5891 | 92.6890 | 0.0124 | 0.0085 |
| 2024_09_20 22:00 | 3267558 | 4 | 13.3633 | 5.6211 | -116.8868 | 10.9798 | 83.9513 | 0.0030 | 0.0127 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413346_E267A7BB | 504990 | 176 | -86.9 | 504990 | 1003 | -85.7 | 504990 | 123 | -91.3 | 504990 | 941 |
| MR_1774413346_A40C242D | 504990 | 176 | -85.5 | 504990 | 1003 | -87.3 | 504990 | 123 | -91.9 | 504990 | 941 |
| MR_1774413346_5C170B64 | 504990 | 176 | -85.2 | 504990 | 1003 | -86.4 | 504990 | 123 | -92.3 | 504990 | 941 |
| MR_1774413346_9EB77C65 | 504990 | 176 | -84.3 | 504990 | 1003 | -88.7 | 504990 | 123 | -94.4 | 504990 | 941 |
| MR_1774413346_956B3C35 | 504990 | 176 | -86.7 | 504990 | 1003 | -87.1 | 504990 | 123 | -91.3 | 504990 | 941 |
| MR_1774413346_6C4F8808 | 504990 | 176 | -85.4 | 504990 | 1003 | -85.8 | 504990 | 123 | -91.3 | 504990 | 941 |
| MR_1774413346_C053DE64 | 504990 | 176 | -84.7 | 504990 | 1003 | -88.9 | 504990 | 123 | -93.4 | 504990 | 941 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1174: `7b22fd7c-baf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7b22fd7c-baf1-4030-9a6b-f387445a12b8` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1174] topology](images/train_1174.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3210774_3
- `C2`: Increase transmission power for 3210774_3
- `C3`: Lift the tilt angle  of 3240542_4 by 10 degrees
- `C4`: Check test server and transmission issues **← 정답**
- `C5`: Increase A3 Offset threshold for 3210774_3
- `C6`: Decrease A3 Offset threshold for 3240542_4
- `C7`: Add neighbor relationship between 3210774_3 and 3240542_4
- `C8`: Lift the tilt angle of 3210774_3 by 4 degrees
- `C9`: Adjust the azimuth of 3240542_4 by 50 degrees
- `C10`: Decrease transmission power for 3210774_3
- `C11`: Increase transmission power for 3240542_4
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Increase A3 Offset threshold for 3240542_4
- `C14`: Add neighbor relationship between 3262815_2 and 3240542_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210774_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240542_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240542_4
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210774_3
- `C19`: Press down the tilt angle of 3210774_3 by 4 degrees
- `C20`: Press down the tilt angle  of 3240542_4 by 10 degrees
- `C21`: Adjust the azimuth of 3210774_3 by 50 degrees
- `C22`: Decrease transmission power for 3240542_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.817 | MS1 | 121.4656600750 | 31.1446346177 | 707 | 504990 | -86.08 | 17.83 | 337.82 | 0.05 | 2.97 | 1578 |
| 2024-09-20 22:21:32.324 | MS1 | 121.4656735709 | 31.1446339835 | 707 | 504990 | -86.59 | 12.78 | 562.88 | 0.07 | 2.25 | 1575 |
| 2024-09-20 22:21:33.369 | MS1 | 121.4656602656 | 31.1446197701 | 707 | 504990 | -88.26 | 12.76 | 504.31 | 0.08 | 2.43 | 1580 |
| 2024-09-20 22:21:34.382 | MS1 | 121.4656720934 | 31.1446289009 | 707 | 504990 | -86.63 | 15.20 | 69.45 | 0.02 | 2.18 | 426 |
| 2024-09-20 22:21:35.287 | MS1 | 121.4656660582 | 31.1446361249 | 707 | 504990 | -88.59 | 12.39 | 84.71 | 0.10 | 2.99 | 315 |
| 2024-09-20 22:21:36.906 | MS1 | 121.4656743610 | 31.1446245716 | 707 | 504990 | -90.24 | 15.24 | 63.77 | 0.02 | 2.49 | 424 |
| 2024-09-20 22:21:37.823 | MS1 | 121.4656686477 | 31.1446225062 | 707 | 504990 | -91.51 | 11.23 | 72.88 | 0.05 | 2.97 | 435 |
| 2024-09-20 22:21:38.557 | MS1 | 121.4656652052 | 31.1446202491 | 707 | 504990 | -93.09 | 10.76 | 86.67 | 0.02 | 2.89 | 423 |
| 2024-09-20 22:21:39.112 | MS1 | 121.4656772773 | 31.1446278663 | 707 | 504990 | -92.28 | 12.11 | 54.59 | 0.11 | 2.83 | 324 |
| 2024-09-20 22:21:40.500 | MS1 | 121.4656697900 | 31.1446295288 | 707 | 504990 | -93.11 | 11.93 | 492.07 | 0.13 | 2.85 | 1570 |
| 2024-09-20 22:21:41.780 | MS1 | 121.4656759732 | 31.1446247612 | 707 | 504990 | -91.84 | 10.90 | 323.09 | 0.01 | 2.22 | 1573 |
| 2024-09-20 22:21:42.180 | MS1 | 121.4656585008 | 31.1446245772 | 707 | 504990 | -91.88 | 7.42 | 331.67 | 0.12 | 2.91 | 1580 |

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
| 3210774 | 3 | 121.4752122049 | 31.1465007703 | 67 | 1 | 5 | 42.1 | TDD | 707 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3233049 | 1 | 121.4686463380 | 31.1558267908 | 38 | 15 | 3 | 39.2 | TDD | 560 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3240542 | 4 | 121.4645216370 | 31.1464320091 | 234 | 7 | 7 | 35.8 | TDD | 351 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3262815 | 2 | 121.4685741132 | 31.1461826495 | 110 | 1 | 10 | 44.4 | TDD | 11 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.177 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.201 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.303 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.303 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.061 | NREventA3 | measId:2;ServCellPCI:200;Se... |
| 2024-09-20 22:21:38.301 | NRHandoverAttempt | SourcePCI:200;SourceNR-ARFC... |
| 2024-09-20 22:21:38.349 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.363 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.501 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.501 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233049 | 1 | 18.2298 | 9.2218 | -114.7585 | 9.6013 | 122.3236 | 0.0030 | 0.0145 |
| 2024_09_20 22:00 | 3262815 | 2 | 18.5078 | 7.2738 | -116.5452 | 8.7625 | 194.2095 | 0.0089 | 0.0125 |
| 2024_09_20 22:00 | 3210774 | 3 | 12.5807 | 18.0247 | -115.2483 | 8.1972 | 106.7912 | 0.0000 | 0.0132 |
| 2024_09_20 22:00 | 3240542 | 4 | 9.3980 | 19.2869 | -114.0336 | 17.0427 | 151.6787 | 0.0174 | 0.0188 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413952_D5ACCB66 | 504990 | 707 | -86.0 | 504990 | 351 | -96.8 | 504990 | 11 | -97.0 | 504990 | 560 |
| MR_1774413952_B4B3DCAB | 504990 | 707 | -85.9 | 504990 | 351 | -96.6 | 504990 | 11 | -95.0 | 504990 | 560 |
| MR_1774413952_7B2FC849 | 504990 | 707 | -88.0 | 504990 | 351 | -95.1 | 504990 | 11 | -95.7 | 504990 | 560 |
| MR_1774413952_64C44042 | 504990 | 707 | -88.4 | 504990 | 351 | -97.4 | 504990 | 11 | -94.0 | 504990 | 560 |
| MR_1774413952_20423EC9 | 504990 | 707 | -88.2 | 504990 | 351 | -97.1 | 504990 | 11 | -94.8 | 504990 | 560 |
| MR_1774413952_1062C2DA | 504990 | 707 | -88.4 | 504990 | 351 | -95.4 | 504990 | 11 | -94.8 | 504990 | 560 |
| MR_1774413952_EC21CC6C | 504990 | 707 | -86.9 | 504990 | 351 | -95.5 | 504990 | 11 | -96.2 | 504990 | 560 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1175: `9f2c26dd-f3a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9f2c26dd-f3a0-49bf-a044-0c2464c498a3` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1175] topology](images/train_1175.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3219522_4 by 5 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272413_1
- `C3`: Adjust the azimuth of 3219522_4 by 50 degrees
- `C4`: Decrease transmission power for 3272413_1
- `C5`: Increase transmission power for 3219522_4
- `C6`: Lift the tilt angle of 3272413_1 by 5 degrees
- `C7`: Increase A3 Offset threshold for 3219522_4
- `C8`: Decrease A3 Offset threshold for 3219522_4
- `C9`: Decrease transmission power for 3219522_4
- `C10`: Add neighbor relationship between 3213396_2 and 3219522_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219522_4
- `C12`: Press down the tilt angle  of 3219522_4 by 5 degrees
- `C13`: Adjust the azimuth of 3272413_1 by 50 degrees
- `C14`: Decrease A3 Offset threshold for 3272413_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219522_4
- `C16`: Increase transmission power for 3272413_1
- `C17`: Add neighbor relationship between 3272413_1 and 3219522_4
- `C18`: Increase A3 Offset threshold for 3272413_1
- `C19`: Check test server and transmission issues
- `C20`: Insufficient data; more data is needed for judgment. **← 정답**
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272413_1
- `C22`: Press down the tilt angle of 3272413_1 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.760 | MS1 | 121.4656696381 | 31.1446378892 | 585 | 504990 | -85.13 | 16.47 | 593.81 | 0.09 | 2.57 | 1600 |
| 2024-09-20 22:21:32.963 | MS1 | 121.4656777677 | 31.1446304526 | 585 | 504990 | -88.68 | 17.37 | 421.02 | 0.08 | 2.80 | 1584 |
| 2024-09-20 22:21:33.738 | MS1 | 121.4656645008 | 31.1446284597 | 585 | 504990 | -87.60 | 15.15 | 492.53 | 0.11 | 2.02 | 1577 |
| 2024-09-20 22:21:34.303 | MS1 | 121.4656748390 | 31.1446200873 | 585 | 504990 | -91.90 | 13.73 | 86.01 | 0.10 | 2.60 | 1582 |
| 2024-09-20 22:21:35.715 | MS1 | 121.4656721737 | 31.1446373801 | 585 | 504990 | -90.78 | 12.63 | 78.40 | 0.17 | 2.19 | 1583 |
| 2024-09-20 22:21:36.660 | MS1 | 121.4656696805 | 31.1446304620 | 585 | 504990 | -87.39 | 17.80 | 78.56 | 0.13 | 2.39 | 1568 |
| 2024-09-20 22:21:37.993 | MS1 | 121.4656649512 | 31.1446340793 | 585 | 504990 | -89.42 | 12.84 | 77.56 | 0.01 | 2.28 | 1589 |
| 2024-09-20 22:21:38.559 | MS1 | 121.4656764646 | 31.1446205404 | 585 | 504990 | -90.04 | 7.69 | 61.71 | 0.01 | 2.38 | 1570 |
| 2024-09-20 22:21:39.138 | MS1 | 121.4656708968 | 31.1446267503 | 585 | 504990 | -89.24 | 11.29 | 97.22 | 0.12 | 2.60 | 1570 |
| 2024-09-20 22:21:40.124 | MS1 | 121.4656663048 | 31.1446297120 | 585 | 504990 | -91.05 | 12.09 | 428.92 | 0.12 | 2.16 | 1565 |
| 2024-09-20 22:21:41.380 | MS1 | 121.4656693217 | 31.1446190817 | 585 | 504990 | -89.15 | 10.12 | 405.86 | 0.17 | 2.91 | 1565 |
| 2024-09-20 22:21:42.268 | MS1 | 121.4656714415 | 31.1446315102 | 585 | 504990 | -89.46 | 8.55 | 545.36 | 0.03 | 2.10 | 1577 |

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
| 3213396 | 2 | 121.4707263492 | 31.1468847553 | 107 | 12 | 4 | 28.4 | TDD | 99 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3219522 | 4 | 121.4685231896 | 31.1459485006 | 177 | 1 | 4 | 19.1 | TDD | 763 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3225511 | 3 | 121.4654895859 | 31.1541605899 | 187 | 4 | 5 | 49.7 | TDD | 358 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3272413 | 1 | 121.4703725674 | 31.1516019442 | 88 | 4 | 10 | 22.8 | TDD | 585 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.904 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.924 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.042 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.042 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.714 | NREventA3 | measId:2;ServCellPCI:240;Se... |
| 2024-09-20 22:21:37.954 | NRHandoverAttempt | SourcePCI:240;SourceNR-ARFC... |
| 2024-09-20 22:21:37.986 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.000 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.147 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.147 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3272413 | 1 | 88.5251 | 77.0337 | -114.7709 | 17.7811 | 111.1432 | 0.0169 | 0.0102 |
| 2024_09_19 22:00 | 3213396 | 2 | 91.0254 | 84.2420 | -116.7543 | 15.7523 | 82.0033 | 0.0172 | 0.0012 |
| 2024_09_19 22:00 | 3225511 | 3 | 81.7124 | 78.6736 | -115.6402 | 15.1667 | 87.3612 | 0.0037 | 0.0197 |
| 2024_09_19 22:00 | 3219522 | 4 | 84.4692 | 80.4798 | -117.2319 | 9.4772 | 174.3988 | 0.0198 | 0.0197 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413151_BC3D0940 | 504990 | 585 | -91.0 | 504990 | 763 | -98.1 | 504990 | 99 | -100.6 | 504990 | 358 |
| MR_1774413151_84463F04 | 504990 | 585 | -90.6 | 504990 | 763 | -99.5 | 504990 | 99 | -100.8 | 504990 | 358 |
| MR_1774413151_6D18164E | 504990 | 585 | -93.4 | 504990 | 763 | -99.2 | 504990 | 99 | -101.6 | 504990 | 358 |
| MR_1774413151_8FB08AF0 | 504990 | 585 | -93.3 | 504990 | 763 | -101.0 | 504990 | 99 | -103.5 | 504990 | 358 |
| MR_1774413151_4B37A799 | 504990 | 585 | -93.1 | 504990 | 763 | -98.3 | 504990 | 99 | -101.2 | 504990 | 358 |
| MR_1774413151_EAC55151 | 504990 | 585 | -91.9 | 504990 | 763 | -98.9 | 504990 | 99 | -103.8 | 504990 | 358 |
| MR_1774413151_DF6B2B1C | 504990 | 585 | -91.2 | 504990 | 763 | -99.1 | 504990 | 99 | -101.7 | 504990 | 358 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1176: `cde7fe21-58c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cde7fe21-58c6-41f6-82e5-88565270afd7` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1176] topology](images/train_1176.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3274311_1 by 10 degrees
- `C2`: Add neighbor relationship between 3274311_1 and 3251006_4
- `C3`: Lift the tilt angle  of 3251006_4 by 9 degrees
- `C4`: Adjust the azimuth of 3251006_4 by 50 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251006_4
- `C6`: Decrease A3 Offset threshold for 3274311_1
- `C7`: Increase A3 Offset threshold for 3274311_1
- `C8`: Lift the tilt angle of 3274311_1 by 10 degrees
- `C9`: Decrease transmission power for 3251006_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251006_4
- `C11`: Insufficient data; more data is needed for judgment. **← 정답**
- `C12`: Press down the tilt angle  of 3251006_4 by 9 degrees
- `C13`: Increase transmission power for 3274311_1
- `C14`: Decrease A3 Offset threshold for 3251006_4
- `C15`: Increase A3 Offset threshold for 3251006_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274311_1
- `C17`: Decrease transmission power for 3274311_1
- `C18`: Add neighbor relationship between 3277067_2 and 3251006_4
- `C19`: Check test server and transmission issues
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274311_1
- `C21`: Increase transmission power for 3251006_4
- `C22`: Adjust the azimuth of 3274311_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.698 | MS1 | 121.4656765007 | 31.1446368408 | 225 | 504990 | -89.63 | 15.71 | 461.91 | 0.14 | 2.86 | 1567 |
| 2024-09-20 22:21:32.676 | MS1 | 121.4656676967 | 31.1446316815 | 225 | 504990 | -85.19 | 12.01 | 310.50 | 0.07 | 2.61 | 1586 |
| 2024-09-20 22:21:33.731 | MS1 | 121.4656737434 | 31.1446203333 | 225 | 504990 | -88.68 | 13.78 | 314.06 | 0.02 | 2.55 | 1585 |
| 2024-09-20 22:21:34.560 | MS1 | 121.4656625463 | 31.1446305068 | 225 | 504990 | -89.05 | 15.55 | 80.19 | 0.20 | 2.17 | 1582 |
| 2024-09-20 22:21:35.357 | MS1 | 121.4656618412 | 31.1446269676 | 225 | 504990 | -90.71 | 13.10 | 85.64 | 0.13 | 2.40 | 1596 |
| 2024-09-20 22:21:36.923 | MS1 | 121.4656762112 | 31.1446221979 | 225 | 504990 | -90.10 | 17.97 | 59.10 | 0.06 | 2.05 | 1581 |
| 2024-09-20 22:21:37.952 | MS1 | 121.4656591373 | 31.1446325890 | 225 | 504990 | -92.30 | 11.42 | 51.60 | 0.03 | 2.46 | 1581 |
| 2024-09-20 22:21:38.844 | MS1 | 121.4656751357 | 31.1446276991 | 225 | 504990 | -90.23 | 11.65 | 84.89 | 0.15 | 2.90 | 1568 |
| 2024-09-20 22:21:39.819 | MS1 | 121.4656640012 | 31.1446187509 | 225 | 504990 | -90.13 | 9.96 | 82.24 | 0.14 | 2.09 | 1574 |
| 2024-09-20 22:21:40.245 | MS1 | 121.4656639974 | 31.1446274202 | 225 | 504990 | -93.51 | 8.55 | 530.37 | 0.10 | 2.57 | 1567 |
| 2024-09-20 22:21:41.448 | MS1 | 121.4656670767 | 31.1446337423 | 225 | 504990 | -89.70 | 12.55 | 499.21 | 0.14 | 2.08 | 1583 |
| 2024-09-20 22:21:42.687 | MS1 | 121.4656755195 | 31.1446310851 | 225 | 504990 | -89.37 | 8.45 | 576.55 | 0.04 | 2.01 | 1579 |

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
| 3223349 | 3 | 121.4681772622 | 31.1534146833 | 346 | 5 | 10 | 41.9 | TDD | 147 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3251006 | 4 | 121.4740424172 | 31.1533490094 | 307 | 8 | 6 | 25.0 | TDD | 30 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3274311 | 1 | 121.4685545591 | 31.1444238423 | 36 | 10 | 2 | 42.1 | TDD | 225 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3277067 | 2 | 121.4672258425 | 31.1480554010 | 217 | 6 | 1 | 21.1 | TDD | 154 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.889 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.908 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.049 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.049 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.728 | NREventA3 | measId:2;ServCellPCI:143;Se... |
| 2024-09-20 22:21:37.968 | NRHandoverAttempt | SourcePCI:143;SourceNR-ARFC... |
| 2024-09-20 22:21:38.017 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.027 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.175 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.175 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3274311 | 1 | 76.6523 | 90.4081 | -115.8585 | 6.7206 | 118.6834 | 0.0090 | 0.0137 |
| 2024_09_19 22:00 | 3277067 | 2 | 88.1320 | 80.1077 | -117.8160 | 15.8304 | 115.8216 | 0.0161 | 0.0126 |
| 2024_09_19 22:00 | 3223349 | 3 | 80.1720 | 91.5367 | -115.9877 | 10.9265 | 147.8575 | 0.0015 | 0.0180 |
| 2024_09_19 22:00 | 3251006 | 4 | 75.3673 | 92.1518 | -116.0353 | 8.9015 | 121.6395 | 0.0157 | 0.0154 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415055_0CB25A5B | 504990 | 225 | -88.9 | 504990 | 30 | -91.9 | 504990 | 154 | -100.1 | 504990 | 147 |
| MR_1774415055_22F091E4 | 504990 | 225 | -88.9 | 504990 | 30 | -93.0 | 504990 | 154 | -99.5 | 504990 | 147 |
| MR_1774415055_84024C6A | 504990 | 225 | -90.5 | 504990 | 30 | -94.5 | 504990 | 154 | -101.7 | 504990 | 147 |
| MR_1774415055_A46AFAE0 | 504990 | 225 | -89.4 | 504990 | 30 | -94.2 | 504990 | 154 | -102.0 | 504990 | 147 |
| MR_1774415055_F40BF474 | 504990 | 225 | -89.2 | 504990 | 30 | -93.0 | 504990 | 154 | -101.7 | 504990 | 147 |
| MR_1774415055_E34EFCBE | 504990 | 225 | -87.3 | 504990 | 30 | -91.4 | 504990 | 154 | -102.4 | 504990 | 147 |
| MR_1774415055_ECD900AE | 504990 | 225 | -88.0 | 504990 | 30 | -94.2 | 504990 | 154 | -99.4 | 504990 | 147 |
| MR_1774415055_3AA16B7D | 504990 | 225 | -90.4 | 504990 | 30 | -94.9 | 504990 | 154 | -101.1 | 504990 | 147 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1177: `827db385-d42...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `827db385-d427-448f-9919-62573646bd0c` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Lift the tilt angle  of 3275533_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1177] topology](images/train_1177.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3275533_3 by 10 degrees
- `C2`: Increase transmission power for 3256602_2
- `C3`: Add neighbor relationship between 3256602_2 and 3260336_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256602_2
- `C5`: Increase A3 Offset threshold for 3260336_4
- `C6`: Press down the tilt angle of 3256602_2 by 6 degrees
- `C7`: Increase transmission power for 3260336_4
- `C8`: Decrease transmission power for 3260336_4
- `C9`: Decrease A3 Offset threshold for 3256602_2
- `C10`: Adjust the azimuth of 3275533_3 by 20 degrees
- `C11`: Check test server and transmission issues
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease A3 Offset threshold for 3260336_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260336_4
- `C15`: Increase A3 Offset threshold for 3256602_2
- `C16`: Lift the tilt angle of 3256602_2 by 6 degrees
- `C17`: Lift the tilt angle  of 3275533_3 by 10 degrees **← 정답**
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260336_4
- `C19`: Add neighbor relationship between 3275533_3 and 3260336_4
- `C20`: Adjust the azimuth of 3256602_2 by 41 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256602_2
- `C22`: Decrease transmission power for 3256602_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.128 | MS1 | 121.4656740847 | 31.1446198964 | 441 | 504990 | -88.80 | 12.94 | 504.24 | 0.16 | 2.41 | 1594 |
| 2024-09-20 22:21:32.736 | MS1 | 121.4656683120 | 31.1446275837 | 441 | 504990 | -88.32 | 17.76 | 386.46 | 0.17 | 2.19 | 1571 |
| 2024-09-20 22:21:33.149 | MS1 | 121.4656703197 | 31.1446346088 | 441 | 504990 | -86.84 | 16.60 | 359.81 | 0.02 | 2.03 | 1580 |
| 2024-09-20 22:21:34.177 | MS1 | 121.4656730404 | 31.1446220039 | 441 | 504990 | -90.74 | 14.53 | 76.41 | 0.05 | 2.43 | 1571 |
| 2024-09-20 22:21:35.642 | MS1 | 121.4656627432 | 31.1446261745 | 441 | 504990 | -90.35 | 16.52 | 98.82 | 0.16 | 2.58 | 1590 |
| 2024-09-20 22:21:36.987 | MS1 | 121.4656597818 | 31.1446188204 | 441 | 504990 | -88.20 | 12.35 | 71.30 | 0.11 | 2.14 | 1598 |
| 2024-09-20 22:21:37.616 | MS1 | 121.4656775420 | 31.1446359283 | 441 | 504990 | -92.73 | 11.59 | 55.77 | 0.04 | 2.26 | 1578 |
| 2024-09-20 22:21:38.262 | MS1 | 121.4656733004 | 31.1446185404 | 441 | 504990 | -89.51 | 9.68 | 99.55 | 0.16 | 2.79 | 1562 |
| 2024-09-20 22:21:39.262 | MS1 | 121.4656675239 | 31.1446192124 | 441 | 504990 | -91.86 | 8.29 | 86.11 | 0.11 | 2.78 | 1564 |
| 2024-09-20 22:21:40.167 | MS1 | 121.4656590254 | 31.1446239725 | 441 | 504990 | -93.71 | 10.85 | 508.88 | 0.15 | 2.83 | 1564 |
| 2024-09-20 22:21:41.886 | MS1 | 121.4656753642 | 31.1446361926 | 441 | 504990 | -92.04 | 8.24 | 515.64 | 0.04 | 2.10 | 1564 |
| 2024-09-20 22:21:42.910 | MS1 | 121.4656640063 | 31.1446227501 | 441 | 504990 | -91.47 | 9.30 | 438.27 | 0.15 | 2.20 | 1575 |

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
| 3226755 | 1 | 121.4641303250 | 31.1527477219 | 231 | 8 | 1 | 43.9 | TDD | 824 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3256602 | 2 | 121.4649899798 | 31.1556244558 | 136 | 4 | 9 | 32.2 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3260336 | 4 | 121.4748397685 | 31.1480287441 | 267 | 13 | 5 | 44.0 | TDD | 369 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3275533 | 3 | 121.4705738540 | 31.1445432031 | 190 | 10 | 3 | 37.8 | TDD | 490 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.278 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.295 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.444 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.444 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.106 | NREventA3 | measId:2;ServCellPCI:293;Se... |
| 2024-09-20 22:21:38.346 | NRHandoverAttempt | SourcePCI:293;SourceNR-ARFC... |
| 2024-09-20 22:21:38.393 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.405 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.537 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.537 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226755 | 1 | 8.3853 | 6.6641 | -115.5912 | 13.6140 | 143.3174 | 0.0186 | 0.0036 |
| 2024_09_20 22:00 | 3256602 | 2 | 79.0779 | 86.4451 | -114.8966 | 12.7269 | 184.5675 | 0.0124 | 0.0094 |
| 2024_09_20 22:00 | 3275533 | 3 | 8.1318 | 8.5390 | -114.8924 | 10.8925 | 87.8560 | 0.0180 | 0.0012 |
| 2024_09_20 22:00 | 3260336 | 4 | 7.9007 | 6.5028 | -114.0204 | 19.8285 | 161.7973 | 0.0101 | 0.0039 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417154_1BA64807 | 504990 | 441 | -92.3 | 504990 | 369 | -96.6 | 504990 | 490 | -99.6 | 504990 | 824 |
| MR_1774417154_D878CBBF | 504990 | 441 | -89.8 | 504990 | 369 | -97.6 | 504990 | 490 | -100.4 | 504990 | 824 |
| MR_1774417154_E29674D2 | 504990 | 441 | -91.5 | 504990 | 369 | -98.4 | 504990 | 490 | -100.7 | 504990 | 824 |
| MR_1774417154_321F72C4 | 504990 | 441 | -90.5 | 504990 | 369 | -99.2 | 504990 | 490 | -102.8 | 504990 | 824 |
| MR_1774417154_669203F3 | 504990 | 441 | -91.5 | 504990 | 369 | -98.9 | 504990 | 490 | -99.5 | 504990 | 824 |
| MR_1774417154_F03B2C9E | 504990 | 441 | -91.1 | 504990 | 369 | -96.9 | 504990 | 490 | -101.4 | 504990 | 824 |
| MR_1774417154_7F89D118 | 504990 | 441 | -89.6 | 504990 | 369 | -97.3 | 504990 | 490 | -100.0 | 504990 | 824 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1178: `59bdf520-fee...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `59bdf520-fee8-47c6-8061-0ce3f01e0c8d` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1178] topology](images/train_1178.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3225440_3 by 50 degrees
- `C2`: Increase A3 Offset threshold for 3251145_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225440_3
- `C4`: Adjust the azimuth of 3251145_4 by 32 degrees
- `C5`: Add neighbor relationship between 3217837_2 and 3251145_4
- `C6`: Increase A3 Offset threshold for 3225440_3
- `C7`: Decrease transmission power for 3225440_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225440_3
- `C9`: Increase transmission power for 3251145_4
- `C10`: Check test server and transmission issues **← 정답**
- `C11`: Decrease A3 Offset threshold for 3225440_3
- `C12`: Press down the tilt angle  of 3251145_4 by 10 degrees
- `C13`: Lift the tilt angle of 3225440_3 by 3 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251145_4
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Press down the tilt angle of 3225440_3 by 3 degrees
- `C17`: Decrease transmission power for 3251145_4
- `C18`: Lift the tilt angle  of 3251145_4 by 10 degrees
- `C19`: Add neighbor relationship between 3225440_3 and 3251145_4
- `C20`: Increase transmission power for 3225440_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251145_4
- `C22`: Decrease A3 Offset threshold for 3251145_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.442 | MS1 | 121.4656721445 | 31.1446236909 | 53 | 504990 | -91.93 | 12.66 | 583.26 | 0.18 | 2.25 | 1590 |
| 2024-09-20 22:21:32.530 | MS1 | 121.4656736898 | 31.1446342827 | 53 | 504990 | -86.03 | 13.55 | 492.04 | 0.16 | 2.91 | 1581 |
| 2024-09-20 22:21:33.858 | MS1 | 121.4656709492 | 31.1446205970 | 53 | 504990 | -85.36 | 14.71 | 507.84 | 0.18 | 2.24 | 1583 |
| 2024-09-20 22:21:34.206 | MS1 | 121.4656713064 | 31.1446359818 | 53 | 504990 | -91.91 | 15.93 | 77.22 | 0.18 | 2.81 | 483 |
| 2024-09-20 22:21:35.135 | MS1 | 121.4656630528 | 31.1446245890 | 53 | 504990 | -88.96 | 17.65 | 98.34 | 0.03 | 2.02 | 413 |
| 2024-09-20 22:21:36.553 | MS1 | 121.4656610966 | 31.1446281308 | 53 | 504990 | -88.44 | 14.47 | 85.69 | 0.11 | 2.10 | 411 |
| 2024-09-20 22:21:37.193 | MS1 | 121.4656707884 | 31.1446181234 | 53 | 504990 | -91.08 | 12.84 | 80.83 | 0.14 | 2.03 | 330 |
| 2024-09-20 22:21:38.171 | MS1 | 121.4656772852 | 31.1446258861 | 53 | 504990 | -91.97 | 12.49 | 79.20 | 0.11 | 2.37 | 334 |
| 2024-09-20 22:21:39.321 | MS1 | 121.4656688524 | 31.1446245543 | 53 | 504990 | -92.35 | 7.21 | 95.69 | 0.16 | 2.17 | 346 |
| 2024-09-20 22:21:40.932 | MS1 | 121.4656615625 | 31.1446249663 | 53 | 504990 | -92.84 | 10.55 | 575.56 | 0.04 | 2.24 | 1569 |
| 2024-09-20 22:21:41.984 | MS1 | 121.4656728615 | 31.1446183346 | 53 | 504990 | -91.52 | 8.04 | 304.03 | 0.11 | 2.88 | 1588 |
| 2024-09-20 22:21:42.298 | MS1 | 121.4656681759 | 31.1446351235 | 53 | 504990 | -91.48 | 12.49 | 384.90 | 0.03 | 2.32 | 1592 |

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
| 3217837 | 2 | 121.4755622859 | 31.1553609028 | 71 | 4 | 3 | 48.0 | TDD | 260 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3222425 | 1 | 121.4649765071 | 31.1465536350 | 132 | 13 | 0 | 45.7 | TDD | 209 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3225440 | 3 | 121.4718641738 | 31.1515473281 | 83 | 0 | 5 | 42.4 | TDD | 53 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3251145 | 4 | 121.4682768121 | 31.1469701977 | 256 | 10 | 12 | 25.5 | TDD | 677 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.509 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.533 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.641 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.641 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.388 | NREventA3 | measId:2;ServCellPCI:888;Se... |
| 2024-09-20 22:21:38.628 | NRHandoverAttempt | SourcePCI:888;SourceNR-ARFC... |
| 2024-09-20 22:21:38.676 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.687 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.805 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.805 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222425 | 1 | 9.8401 | 16.9507 | -115.7509 | 10.8265 | 166.2957 | 0.0143 | 0.0194 |
| 2024_09_20 22:00 | 3217837 | 2 | 14.7792 | 7.9753 | -117.2182 | 15.1485 | 153.7898 | 0.0032 | 0.0039 |
| 2024_09_20 22:00 | 3225440 | 3 | 6.0308 | 7.2420 | -114.3002 | 14.8706 | 133.4358 | 0.0124 | 0.0142 |
| 2024_09_20 22:00 | 3251145 | 4 | 15.7279 | 6.3777 | -117.9398 | 10.8622 | 162.3749 | 0.0059 | 0.0077 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414418_2877803F | 504990 | 53 | -91.6 | 504990 | 677 | -91.1 | 504990 | 260 | -97.3 | 504990 | 209 |
| MR_1774414418_943ABBB7 | 504990 | 53 | -91.4 | 504990 | 677 | -92.5 | 504990 | 260 | -98.4 | 504990 | 209 |
| MR_1774414418_9D631EBE | 504990 | 53 | -91.9 | 504990 | 677 | -93.5 | 504990 | 260 | -99.1 | 504990 | 209 |
| MR_1774414418_36165B28 | 504990 | 53 | -90.6 | 504990 | 677 | -90.2 | 504990 | 260 | -96.4 | 504990 | 209 |
| MR_1774414418_4C679DFA | 504990 | 53 | -93.7 | 504990 | 677 | -91.3 | 504990 | 260 | -96.2 | 504990 | 209 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1179: `1a465575-625...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1a465575-6258-43a5-bd0c-2bdf216591aa` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277598_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1179] topology](images/train_1179.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase transmission power for 3270055_2
- `C3`: Decrease A3 Offset threshold for 3270055_2
- `C4`: Increase transmission power for 3277598_3
- `C5`: Add neighbor relationship between 3277598_3 and 3270055_2
- `C6`: Check test server and transmission issues
- `C7`: Decrease A3 Offset threshold for 3277598_3
- `C8`: Lift the tilt angle  of 3270055_2 by 2 degrees
- `C9`: Adjust the azimuth of 3277598_3 by 44 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270055_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277598_3 **← 정답**
- `C12`: Add neighbor relationship between 3231442_13 and 3270055_2
- `C13`: Increase A3 Offset threshold for 3277598_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277598_3
- `C15`: Press down the tilt angle of 3277598_3 by 3 degrees
- `C16`: Press down the tilt angle  of 3270055_2 by 2 degrees
- `C17`: Decrease transmission power for 3277598_3
- `C18`: Lift the tilt angle of 3277598_3 by 3 degrees
- `C19`: Decrease transmission power for 3270055_2
- `C20`: Increase A3 Offset threshold for 3270055_2
- `C21`: Adjust the azimuth of 3270055_2 by 40 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270055_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.276 | MS1 | 121.4656624269 | 31.1446196635 | 810 | 504990 | -94.30 | 13.57 | 379.13 | 0.20 | 2.43 | 1561 |
| 2024-09-20 22:21:32.700 | MS1 | 121.4656743302 | 31.1446266580 | 444 | 504990 | -94.50 | 14.53 | 514.80 | 0.02 | 2.57 | 1568 |
| 2024-09-20 22:21:33.488 | MS1 | 121.4656581272 | 31.1446254642 | 213 | 504990 | -93.31 | 13.76 | 465.03 | 0.06 | 2.44 | 1589 |
| 2024-09-20 22:21:34.582 | MS1 | 121.4656604132 | 31.1446206893 | 148 | 152650 | -95.97 | 2.43 | 55.01 | 0.05 | 1.69 | 938 |
| 2024-09-20 22:21:35.675 | MS1 | 121.4656661357 | 31.1446363643 | 166 | 152650 | -92.24 | 3.25 | 79.40 | 0.18 | 1.77 | 925 |
| 2024-09-20 22:21:36.538 | MS1 | 121.4656673582 | 31.1446278236 | 828 | 152650 | -96.00 | 5.59 | 81.27 | 0.11 | 1.83 | 996 |
| 2024-09-20 22:21:37.704 | MS1 | 121.4656710121 | 31.1446201741 | 1000 | 152650 | -94.10 | 6.55 | 54.95 | 0.19 | 1.69 | 965 |
| 2024-09-20 22:21:38.994 | MS1 | 121.4656603306 | 31.1446185061 | 148 | 152650 | -90.50 | 3.34 | 56.52 | 0.06 | 1.78 | 925 |
| 2024-09-20 22:21:39.728 | MS1 | 121.4656716969 | 31.1446265257 | 166 | 152650 | -91.67 | 2.29 | 92.47 | 0.04 | 1.85 | 907 |
| 2024-09-20 22:21:40.376 | MS1 | 121.4656676431 | 31.1446339357 | 828 | 152650 | -91.17 | 3.86 | 92.28 | 0.07 | 2.13 | 1560 |
| 2024-09-20 22:21:41.345 | MS1 | 121.4656686501 | 31.1446275721 | 1000 | 152650 | -88.05 | 8.00 | 62.90 | 0.05 | 2.02 | 1584 |
| 2024-09-20 22:21:42.829 | MS1 | 121.4656583344 | 31.1446237329 | 148 | 152650 | -95.46 | 2.94 | 87.18 | 0.08 | 2.69 | 1585 |

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
| 3215369 | 6 | 121.4672701495 | 31.1454215898 | 305 | 3 | 2 | 27.6 | TDD | 415 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3218635 | 4 | 121.4676792389 | 31.1532230008 | 282 | 10 | 10 | 23.9 | TDD | 213 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3226814 | 9 | 121.4738040745 | 31.1514884992 | 234 | 12 | 7 | 8.7 | FDD | 1000 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3231442 | 13 | 121.4735839626 | 31.1533767451 | 93 | 10 | 5 | 0.2 | FDD | 828 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3234029 | 12 | 121.4663076943 | 31.1456876628 | 81 | 8 | 11 | 24.5 | FDD | 55 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3241520 | 5 | 121.4669191220 | 31.1499505461 | 327 | 1 | 5 | 11.7 | TDD | 444 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3242311 | 1 | 121.4708514520 | 31.1527152083 | 86 | 10 | 6 | 25.0 | TDD | 676 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3247995 | 8 | 121.4689719784 | 31.1444790748 | 295 | 14 | 7 | 26.1 | FDD | 166 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3263921 | 7 | 121.4645129249 | 31.1479245793 | 80 | 15 | 2 | 11.9 | FDD | 867 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3270055 | 2 | 121.4725189127 | 31.1495027197 | 270 | 1 | 3 | 17.3 | TDD | 548 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3270535 | 11 | 121.4664598592 | 31.1442715919 | 160 | 15 | 11 | 16.3 | FDD | 148 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3275545 | 10 | 121.4667909019 | 31.1470588059 | 18 | 1 | 5 | 19.5 | FDD | 202 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3277598 | 3 | 121.4724184873 | 31.1441038154 | 231 | 1 | 0 | 23.5 | TDD | 810 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.535 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.550 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.662 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.662 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.413 | NREventA2 | measId:1;ServCellPCI:177;Se... |
| 2024-09-20 22:21:35.544 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.780 | NREventA5 | measId:3;ServCellPCI:177;Se... |
| 2024-09-20 22:21:35.824 | NRHandoverAttempt | SourcePCI:177;SourceNR-ARFC... |
| 2024-09-20 22:21:35.852 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.867 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.980 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.980 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242311 | 1 | 11.1510 | 19.3498 | -115.4240 | 14.7356 | 175.2523 | 0.0036 | 0.0108 |
| 2024_09_20 22:00 | 3270055 | 2 | 14.2979 | 17.4146 | -114.0959 | 17.0382 | 193.2535 | 0.0026 | 0.0101 |
| 2024_09_20 22:00 | 3277598 | 3 | 5.6762 | 9.9526 | -116.5486 | 8.0939 | 199.7123 | 0.0080 | 0.0035 |
| 2024_09_20 22:00 | 3218635 | 4 | 10.8708 | 18.5087 | -116.9701 | 19.8833 | 199.4981 | 0.0092 | 0.0061 |
| 2024_09_20 22:00 | 3241520 | 5 | 11.5337 | 17.7020 | -116.1014 | 7.7815 | 108.6426 | 0.0098 | 0.0111 |
| 2024_09_20 22:00 | 3215369 | 6 | 11.6397 | 17.3000 | -116.2832 | 18.3283 | 192.0089 | 0.0089 | 0.0087 |
| 2024_09_20 22:00 | 3263921 | 7 | 15.2691 | 11.1819 | -117.2363 | 4.9648 | 34.1078 | 0.0180 | 0.0137 |
| 2024_09_20 22:00 | 3247995 | 8 | 17.4842 | 11.3234 | -114.6818 | 3.3444 | 31.2267 | 0.0122 | 0.0142 |
| 2024_09_20 22:00 | 3226814 | 9 | 12.6709 | 14.4078 | -117.0580 | 4.0197 | 44.8635 | 0.0148 | 0.0149 |
| 2024_09_20 22:00 | 3275545 | 10 | 13.0405 | 6.4326 | -115.4583 | 4.9583 | 22.0867 | 0.0123 | 0.0165 |
| 2024_09_20 22:00 | 3270535 | 11 | 5.7041 | 6.5799 | -116.4442 | 4.1240 | 28.0111 | 0.0035 | 0.0110 |
| 2024_09_20 22:00 | 3234029 | 12 | 10.6527 | 7.5886 | -114.5918 | 4.0869 | 24.2683 | 0.0068 | 0.0153 |
| 2024_09_20 22:00 | 3231442 | 13 | 11.6275 | 8.8471 | -114.3030 | 4.1307 | 38.8610 | 0.0120 | 0.0100 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415403_48F9D1E7 | 152650 | 148 | -95.4 | 152650 | 202 | -104.3 | 152650 | 867 | -105.0 | 152650 | 55 |
| MR_1774415403_B39174CA | 504990 | 213 | -94.6 | 504990 | 548 | -88.7 | 504990 | 676 | -102.2 | 504990 | 415 |
| MR_1774415403_A8873D8C | 152650 | 148 | -96.2 | 152650 | 202 | -103.9 | 152650 | 867 | -105.0 | 152650 | 55 |
| MR_1774415403_54540249 | 152650 | 148 | -96.9 | 152650 | 202 | -103.9 | 152650 | 867 | -107.6 | 152650 | 55 |
| MR_1774415403_5516F386 | 152650 | 148 | -94.2 | 152650 | 202 | -102.2 | 152650 | 867 | -107.0 | 152650 | 55 |

> *... 2개 열 생략 (전체 14열)*

---
