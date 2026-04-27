# Track A 문제 분석 — train[870]~train[879]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[870] ~ train[879] (10개)

## 목차

1. [문제 870: `39ef1ab2-808...`](#870) — single-answer, 정답: C15
2. [문제 871: `52408889-259...`](#871) — multiple-answer, 정답: C5|C7
3. [문제 872: `cac99de7-da4...`](#872) — single-answer, 정답: C16
4. [문제 873: `b5ab27d6-369...`](#873) — single-answer, 정답: C13
5. [문제 874: `40c65260-700...`](#874) — single-answer, 정답: C21
6. [문제 875: `7effd118-172...`](#875) — single-answer, 정답: C16
7. [문제 876: `c7ecc466-3c7...`](#876) — single-answer, 정답: C7
8. [문제 877: `6daaa66a-a5c...`](#877) — single-answer, 정답: C12
9. [문제 878: `bb6cae6c-61a...`](#878) — single-answer, 정답: C9
10. [문제 879: `bde467bd-fca...`](#879) — single-answer, 정답: C11

---

### 문제 870: `39ef1ab2-808...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `39ef1ab2-808e-4b5c-bef9-17e6998cab29` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease A3 Offset threshold for 3217041_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[870] topology](images/train_0870.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3217041_3 by 1 degrees
- `C2`: Add neighbor relationship between 3217041_3 and 3216240_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217041_3
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Check test server and transmission issues
- `C6`: Decrease transmission power for 3217041_3
- `C7`: Increase transmission power for 3216240_4
- `C8`: Increase transmission power for 3217041_3
- `C9`: Adjust the azimuth of 3217041_3 by 13 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217041_3
- `C11`: Adjust the azimuth of 3216240_4 by 50 degrees
- `C12`: Add neighbor relationship between 3239994_2 and 3216240_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216240_4
- `C14`: Decrease A3 Offset threshold for 3216240_4
- `C15`: Decrease A3 Offset threshold for 3217041_3 **← 정답**
- `C16`: Increase A3 Offset threshold for 3216240_4
- `C17`: Lift the tilt angle of 3217041_3 by 1 degrees
- `C18`: Lift the tilt angle  of 3216240_4 by 10 degrees
- `C19`: Decrease transmission power for 3216240_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216240_4
- `C21`: Increase A3 Offset threshold for 3217041_3
- `C22`: Press down the tilt angle  of 3216240_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.532 | MS1 | 121.4656703683 | 31.1446332586 | 820 | 504990 | -82.31 | 14.39 | 535.60 | 0.01 | 2.61 | 1598 |
| 2024-09-20 22:21:32.840 | MS1 | 121.4656741539 | 31.1446377123 | 820 | 504990 | -77.95 | 17.86 | 515.95 | 0.04 | 2.40 | 1580 |
| 2024-09-20 22:21:33.689 | MS1 | 121.4656612514 | 31.1446340810 | 820 | 504990 | -81.94 | 17.87 | 505.30 | 0.12 | 2.50 | 1560 |
| 2024-09-20 22:21:34.624 | MS1 | 121.4656688503 | 31.1446341954 | 820 | 504990 | -84.75 | -2.74 | 61.92 | 0.03 | 1.02 | 1585 |
| 2024-09-20 22:21:35.954 | MS1 | 121.4656732163 | 31.1446201065 | 820 | 504990 | -84.92 | -1.81 | 42.67 | 0.17 | 1.09 | 1599 |
| 2024-09-20 22:21:36.360 | MS1 | 121.4656648291 | 31.1446298074 | 820 | 504990 | -88.38 | -0.40 | 45.72 | 0.06 | 1.41 | 1573 |
| 2024-09-20 22:21:37.106 | MS1 | 121.4656618423 | 31.1446356901 | 820 | 504990 | -86.62 | -2.00 | 35.46 | 0.14 | 1.21 | 1583 |
| 2024-09-20 22:21:38.660 | MS1 | 121.4656762436 | 31.1446260224 | 820 | 504990 | -85.14 | -0.85 | 32.37 | 0.19 | 1.18 | 1598 |
| 2024-09-20 22:21:39.961 | MS1 | 121.4656617250 | 31.1446275131 | 943 | 504990 | -82.22 | 15.90 | 255.93 | 0.19 | 1.42 | 1579 |
| 2024-09-20 22:21:40.567 | MS1 | 121.4656674206 | 31.1446225919 | 943 | 504990 | -76.36 | 17.32 | 311.56 | 0.10 | 2.66 | 1576 |
| 2024-09-20 22:21:41.366 | MS1 | 121.4656709960 | 31.1446238838 | 943 | 504990 | -77.91 | 17.03 | 398.63 | 0.12 | 2.53 | 1562 |
| 2024-09-20 22:21:42.786 | MS1 | 121.4656595530 | 31.1446192986 | 943 | 504990 | -77.73 | 16.20 | 485.69 | 0.05 | 2.79 | 1580 |

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
| 3216240 | 4 | 121.4657323522 | 31.1553766691 | 110 | 8 | 2 | 37.1 | TDD | 943 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3217041 | 3 | 121.4706801343 | 31.1535937201 | 193 | 0 | 3 | 17.8 | TDD | 820 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3239994 | 2 | 121.4666197384 | 31.1497749501 | 264 | 15 | 6 | 36.9 | TDD | 892 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3247947 | 1 | 121.4748138915 | 31.1551724957 | 139 | 5 | 12 | 22.1 | TDD | 404 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.062 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.077 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.225 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.225 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.908 | NREventA3 | measId:2;ServCellPCI:394;Se... |
| 2024-09-20 22:21:38.148 | NRHandoverAttempt | SourcePCI:394;SourceNR-ARFC... |
| 2024-09-20 22:21:38.190 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.202 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.315 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.315 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247947 | 1 | 9.8089 | 10.3169 | -115.3325 | 5.0119 | 160.7667 | 0.0090 | 0.0047 |
| 2024_09_20 22:00 | 3239994 | 2 | 10.8079 | 14.9629 | -117.6947 | 6.2181 | 150.3485 | 0.0186 | 0.0022 |
| 2024_09_20 22:00 | 3217041 | 3 | 10.3438 | 6.6179 | -115.6365 | 14.0676 | 124.8275 | 0.0075 | 0.1384 |
| 2024_09_20 22:00 | 3216240 | 4 | 16.3124 | 8.1279 | -116.9201 | 7.9083 | 199.6456 | 0.0046 | 0.0161 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413112_3B731CC1 | 504990 | 943 | -78.4 | 504990 | 820 | -84.8 | 504990 | 892 | -79.5 | 504990 | 404 |
| MR_1774413112_C8A59F35 | 504990 | 943 | -78.8 | 504990 | 820 | -84.8 | 504990 | 892 | -79.4 | 504990 | 404 |
| MR_1774413112_9107E0E9 | 504990 | 820 | -83.5 | 504990 | 943 | -78.6 | 504990 | 892 | -81.3 | 504990 | 404 |
| MR_1774413112_24FE515B | 504990 | 943 | -81.3 | 504990 | 820 | -85.2 | 504990 | 892 | -80.0 | 504990 | 404 |
| MR_1774413112_CBC63C01 | 504990 | 820 | -85.1 | 504990 | 943 | -80.1 | 504990 | 892 | -79.3 | 504990 | 404 |
| MR_1774413112_50F3DEE7 | 504990 | 820 | -85.2 | 504990 | 943 | -80.5 | 504990 | 892 | -81.5 | 504990 | 404 |
| MR_1774413112_7452D857 | 504990 | 820 | -86.5 | 504990 | 943 | -80.3 | 504990 | 892 | -80.5 | 504990 | 404 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 871: `52408889-259...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `52408889-2593-4fcf-a73e-ecdc6397c29f` |
| Tag | **multiple-answer** |
| 정답 | **C5|C7** |
| C5 의미 | Decrease transmission power for 3256541_3 |
| C7 의미 | Press down the tilt angle  of 3256541_3 by 5 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[871] topology](images/train_0871.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease A3 Offset threshold for 3256541_3
- `C3`: Increase transmission power for 3256541_3
- `C4`: Decrease transmission power for 3269842_4
- `C5`: Decrease transmission power for 3256541_3 **← 정답**
- `C6`: Adjust the azimuth of 3256541_3 by 13 degrees
- `C7`: Press down the tilt angle  of 3256541_3 by 5 degrees **← 정답**
- `C8`: Lift the tilt angle of 3269842_4 by 4 degrees
- `C9`: Decrease A3 Offset threshold for 3269842_4
- `C10`: Increase transmission power for 3269842_4
- `C11`: Lift the tilt angle  of 3256541_3 by 5 degrees
- `C12`: Increase A3 Offset threshold for 3256541_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256541_3
- `C14`: Add neighbor relationship between 3269842_4 and 3256541_3
- `C15`: Press down the tilt angle of 3269842_4 by 4 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269842_4
- `C17`: Adjust the azimuth of 3269842_4 by 38 degrees
- `C18`: Increase A3 Offset threshold for 3269842_4
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269842_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256541_3
- `C22`: Add neighbor relationship between 3215825_1 and 3256541_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.888 | MS1 | 121.4656651159 | 31.1446326651 | 407 | 504990 | -79.50 | 16.48 | 382.40 | 0.13 | 2.67 | 1568 |
| 2024-09-20 22:21:32.602 | MS1 | 121.4656609026 | 31.1446312963 | 407 | 504990 | -79.58 | 17.78 | 410.93 | 0.11 | 2.76 | 1576 |
| 2024-09-20 22:21:33.259 | MS1 | 121.4656714351 | 31.1446250800 | 407 | 504990 | -81.96 | 17.88 | 529.58 | 0.16 | 2.74 | 1571 |
| 2024-09-20 22:21:34.632 | MS1 | 121.4656657816 | 31.1446281002 | 407 | 504990 | -87.34 | 0.62 | 74.40 | 0.18 | 1.13 | 1594 |
| 2024-09-20 22:21:35.956 | MS1 | 121.4656694458 | 31.1446241337 | 407 | 504990 | -91.50 | 3.12 | 59.48 | 0.09 | 1.37 | 1594 |
| 2024-09-20 22:21:36.152 | MS1 | 121.4656716052 | 31.1446204836 | 407 | 504990 | -94.73 | 1.34 | 53.07 | 0.12 | 1.10 | 1587 |
| 2024-09-20 22:21:37.895 | MS1 | 121.4656611436 | 31.1446203873 | 407 | 504990 | -90.56 | 2.77 | 48.48 | 0.13 | 1.13 | 1589 |
| 2024-09-20 22:21:38.668 | MS1 | 121.4656614721 | 31.1446302198 | 407 | 504990 | -91.84 | 3.58 | 72.17 | 0.20 | 1.43 | 1583 |
| 2024-09-20 22:21:39.922 | MS1 | 121.4656623319 | 31.1446376623 | 407 | 504990 | -85.95 | 1.54 | 51.81 | 0.11 | 1.49 | 1569 |
| 2024-09-20 22:21:40.332 | MS1 | 121.4656617269 | 31.1446367026 | 407 | 504990 | -76.88 | 14.13 | 313.40 | 0.16 | 2.24 | 1562 |
| 2024-09-20 22:21:41.869 | MS1 | 121.4656723142 | 31.1446223509 | 407 | 504990 | -83.54 | 12.97 | 509.38 | 0.20 | 2.46 | 1594 |
| 2024-09-20 22:21:42.196 | MS1 | 121.4656753562 | 31.1446190035 | 407 | 504990 | -75.29 | 12.86 | 559.87 | 0.19 | 2.61 | 1593 |

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
| 3215825 | 1 | 121.4660135422 | 31.1528950203 | 209 | 15 | 12 | 30.0 | TDD | 400 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3227890 | 2 | 121.4688755046 | 31.1501975987 | 69 | 7 | 11 | 18.2 | TDD | 205 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3256541 | 3 | 121.4709194488 | 31.1506747770 | 204 | 3 | 10 | 36.1 | TDD | 374 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3269842 | 4 | 121.4666817312 | 31.1536863447 | 148 | 3 | 6 | 22.1 | TDD | 407 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.188 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.204 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.354 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.354 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215825 | 1 | 14.8148 | 9.2259 | -117.0434 | 9.4955 | 160.3728 | 0.0102 | 0.0173 |
| 2024_09_20 22:00 | 3227890 | 2 | 17.9664 | 11.7121 | -114.1627 | 14.2685 | 187.6431 | 0.0019 | 0.0045 |
| 2024_09_20 22:00 | 3256541 | 3 | 9.2257 | 10.4194 | -116.2141 | 15.8831 | 103.5601 | 0.0084 | 0.0146 |
| 2024_09_20 22:00 | 3269842 | 4 | 12.1804 | 18.3896 | -109.0369 | 14.4050 | 130.7886 | 0.0051 | 0.0155 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413493_D1587373 | 504990 | 407 | -87.2 | 504990 | 374 | -84.6 | 504990 | 400 | -85.2 | 504990 | 205 |
| MR_1774413493_62CC5F04 | 504990 | 407 | -87.2 | 504990 | 374 | -81.9 | 504990 | 400 | -83.6 | 504990 | 205 |
| MR_1774413493_0A1A239A | 504990 | 407 | -88.4 | 504990 | 374 | -85.3 | 504990 | 400 | -86.1 | 504990 | 205 |
| MR_1774413493_BF5B2496 | 504990 | 407 | -86.1 | 504990 | 374 | -83.7 | 504990 | 400 | -85.5 | 504990 | 205 |
| MR_1774413493_894E11EB | 504990 | 407 | -86.8 | 504990 | 374 | -83.3 | 504990 | 400 | -86.5 | 504990 | 205 |
| MR_1774413493_82F40F0E | 504990 | 407 | -86.6 | 504990 | 374 | -84.8 | 504990 | 400 | -86.8 | 504990 | 205 |
| MR_1774413493_10DF5F70 | 504990 | 407 | -85.6 | 504990 | 374 | -83.2 | 504990 | 400 | -85.5 | 504990 | 205 |
| MR_1774413493_850BD5A6 | 504990 | 374 | -86.2 | 504990 | 407 | -84.6 | 504990 | 400 | -84.5 | 504990 | 205 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 872: `cac99de7-da4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cac99de7-da44-4c91-9cb0-06ae0e1ab765` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Lift the tilt angle  of 3223102_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[872] topology](images/train_0872.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241731_2
- `C2`: Add neighbor relationship between 3223102_4 and 3241731_2
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Add neighbor relationship between 3250729_1 and 3241731_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250729_1
- `C6`: Decrease A3 Offset threshold for 3250729_1
- `C7`: Press down the tilt angle of 3250729_1 by 3 degrees
- `C8`: Adjust the azimuth of 3250729_1 by 0 degrees
- `C9`: Increase A3 Offset threshold for 3241731_2
- `C10`: Decrease transmission power for 3250729_1
- `C11`: Lift the tilt angle of 3250729_1 by 3 degrees
- `C12`: Press down the tilt angle  of 3223102_4 by 10 degrees
- `C13`: Increase A3 Offset threshold for 3250729_1
- `C14`: Adjust the azimuth of 3223102_4 by 50 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250729_1
- `C16`: Lift the tilt angle  of 3223102_4 by 10 degrees **← 정답**
- `C17`: Check test server and transmission issues
- `C18`: Increase transmission power for 3241731_2
- `C19`: Increase transmission power for 3250729_1
- `C20`: Decrease transmission power for 3241731_2
- `C21`: Decrease A3 Offset threshold for 3241731_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241731_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.942 | MS1 | 121.4656628660 | 31.1446342764 | 49 | 504990 | -89.82 | 17.64 | 384.48 | 0.10 | 2.11 | 1596 |
| 2024-09-20 22:21:32.395 | MS1 | 121.4656725604 | 31.1446232441 | 49 | 504990 | -91.65 | 15.84 | 309.14 | 0.08 | 2.43 | 1584 |
| 2024-09-20 22:21:33.796 | MS1 | 121.4656710264 | 31.1446318630 | 49 | 504990 | -86.84 | 17.26 | 497.18 | 0.02 | 2.89 | 1590 |
| 2024-09-20 22:21:34.468 | MS1 | 121.4656730463 | 31.1446371190 | 49 | 504990 | -85.21 | 15.87 | 71.63 | 0.19 | 2.49 | 1588 |
| 2024-09-20 22:21:35.755 | MS1 | 121.4656690866 | 31.1446324326 | 49 | 504990 | -89.10 | 13.50 | 89.49 | 0.14 | 2.92 | 1584 |
| 2024-09-20 22:21:36.234 | MS1 | 121.4656702458 | 31.1446261487 | 49 | 504990 | -89.23 | 13.20 | 60.54 | 0.05 | 2.26 | 1585 |
| 2024-09-20 22:21:37.658 | MS1 | 121.4656598280 | 31.1446181279 | 49 | 504990 | -91.93 | 8.32 | 100.69 | 0.10 | 2.40 | 1568 |
| 2024-09-20 22:21:38.996 | MS1 | 121.4656677879 | 31.1446361660 | 49 | 504990 | -90.68 | 11.34 | 59.16 | 0.09 | 2.90 | 1582 |
| 2024-09-20 22:21:39.173 | MS1 | 121.4656672028 | 31.1446340180 | 49 | 504990 | -91.50 | 9.10 | 102.05 | 0.00 | 2.27 | 1570 |
| 2024-09-20 22:21:40.826 | MS1 | 121.4656690308 | 31.1446181013 | 49 | 504990 | -92.99 | 7.87 | 521.11 | 0.08 | 2.89 | 1574 |
| 2024-09-20 22:21:41.278 | MS1 | 121.4656776442 | 31.1446199276 | 49 | 504990 | -92.98 | 9.76 | 511.04 | 0.04 | 2.86 | 1596 |
| 2024-09-20 22:21:42.116 | MS1 | 121.4656751691 | 31.1446225814 | 49 | 504990 | -89.20 | 8.50 | 292.29 | 0.08 | 2.68 | 1592 |

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
| 3223102 | 4 | 121.4746204387 | 31.1514778998 | 335 | 11 | 1 | 39.1 | TDD | 839 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3231791 | 3 | 121.4655573402 | 31.1460642437 | 149 | 10 | 6 | 35.3 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3241731 | 2 | 121.4652524898 | 31.1502165149 | 319 | 10 | 3 | 17.0 | TDD | 447 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3250729 | 1 | 121.4680440076 | 31.1531891268 | 193 | 2 | 12 | 21.2 | TDD | 49 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.582 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.709 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.709 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.462 | NREventA3 | measId:2;ServCellPCI:410;Se... |
| 2024-09-20 22:21:38.702 | NRHandoverAttempt | SourcePCI:410;SourceNR-ARFC... |
| 2024-09-20 22:21:38.736 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.748 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.869 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.869 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250729 | 1 | 90.6341 | 90.0527 | -115.9457 | 17.7803 | 117.1487 | 0.0090 | 0.0198 |
| 2024_09_20 22:00 | 3241731 | 2 | 6.9845 | 17.4043 | -117.6563 | 17.0966 | 82.1302 | 0.0181 | 0.0133 |
| 2024_09_20 22:00 | 3231791 | 3 | 8.1984 | 8.9966 | -117.6109 | 10.5956 | 153.9458 | 0.0010 | 0.0101 |
| 2024_09_20 22:00 | 3223102 | 4 | 12.5762 | 9.8816 | -114.6639 | 9.1840 | 149.8263 | 0.0164 | 0.0173 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413488_DF2210C5 | 504990 | 49 | -86.1 | 504990 | 447 | -85.1 | 504990 | 839 | -98.0 | 504990 | 382 |
| MR_1774413488_762D6209 | 504990 | 49 | -87.1 | 504990 | 447 | -85.2 | 504990 | 839 | -97.3 | 504990 | 382 |
| MR_1774413488_39B36664 | 504990 | 49 | -86.8 | 504990 | 447 | -84.9 | 504990 | 839 | -97.4 | 504990 | 382 |
| MR_1774413488_B466F66A | 504990 | 49 | -83.9 | 504990 | 447 | -84.9 | 504990 | 839 | -95.0 | 504990 | 382 |
| MR_1774413488_4F078971 | 504990 | 49 | -83.9 | 504990 | 447 | -87.4 | 504990 | 839 | -94.7 | 504990 | 382 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 873: `b5ab27d6-369...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b5ab27d6-369c-4a5c-88b8-5f435f1c10d1` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[873] topology](images/train_0873.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3276975_4 and 3236705_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276975_4
- `C3`: Increase A3 Offset threshold for 3276975_4
- `C4`: Decrease transmission power for 3276975_4
- `C5`: Adjust the azimuth of 3276975_4 by 50 degrees
- `C6`: Adjust the azimuth of 3236705_2 by 50 degrees
- `C7`: Decrease A3 Offset threshold for 3236705_2
- `C8`: Increase transmission power for 3276975_4
- `C9`: Press down the tilt angle of 3276975_4 by 10 degrees
- `C10`: Press down the tilt angle  of 3236705_2 by 4 degrees
- `C11`: Increase A3 Offset threshold for 3236705_2
- `C12`: Increase transmission power for 3236705_2
- `C13`: Insufficient data; more data is needed for judgment. **← 정답**
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276975_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236705_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236705_2
- `C17`: Add neighbor relationship between 3242261_3 and 3236705_2
- `C18`: Check test server and transmission issues
- `C19`: Lift the tilt angle  of 3236705_2 by 4 degrees
- `C20`: Decrease A3 Offset threshold for 3276975_4
- `C21`: Decrease transmission power for 3236705_2
- `C22`: Lift the tilt angle of 3276975_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.589 | MS1 | 121.4656756903 | 31.1446279270 | 828 | 504990 | -86.70 | 15.63 | 329.99 | 0.19 | 2.23 | 1586 |
| 2024-09-20 22:21:32.964 | MS1 | 121.4656612216 | 31.1446217223 | 828 | 504990 | -88.13 | 16.59 | 442.68 | 0.01 | 2.11 | 1597 |
| 2024-09-20 22:21:33.913 | MS1 | 121.4656707502 | 31.1446193591 | 828 | 504990 | -89.05 | 16.66 | 538.56 | 0.18 | 2.47 | 1597 |
| 2024-09-20 22:21:34.255 | MS1 | 121.4656731351 | 31.1446357154 | 828 | 504990 | -87.36 | 17.85 | 74.24 | 0.04 | 2.74 | 1583 |
| 2024-09-20 22:21:35.387 | MS1 | 121.4656644836 | 31.1446357618 | 828 | 504990 | -86.68 | 16.84 | 59.73 | 0.10 | 2.46 | 1567 |
| 2024-09-20 22:21:36.706 | MS1 | 121.4656696938 | 31.1446325385 | 828 | 504990 | -87.93 | 12.51 | 79.19 | 0.10 | 2.26 | 1567 |
| 2024-09-20 22:21:37.514 | MS1 | 121.4656612515 | 31.1446262519 | 828 | 504990 | -93.33 | 12.06 | 66.03 | 0.05 | 2.85 | 1591 |
| 2024-09-20 22:21:38.356 | MS1 | 121.4656659057 | 31.1446331439 | 828 | 504990 | -92.98 | 7.25 | 83.24 | 0.15 | 2.31 | 1583 |
| 2024-09-20 22:21:39.223 | MS1 | 121.4656640182 | 31.1446288453 | 828 | 504990 | -92.86 | 7.39 | 46.41 | 0.19 | 2.40 | 1566 |
| 2024-09-20 22:21:40.596 | MS1 | 121.4656706015 | 31.1446308790 | 828 | 504990 | -91.56 | 8.75 | 324.15 | 0.18 | 2.81 | 1568 |
| 2024-09-20 22:21:41.115 | MS1 | 121.4656731866 | 31.1446249276 | 828 | 504990 | -91.65 | 7.89 | 406.27 | 0.12 | 2.29 | 1595 |
| 2024-09-20 22:21:42.795 | MS1 | 121.4656654055 | 31.1446333095 | 828 | 504990 | -90.66 | 11.34 | 522.67 | 0.00 | 2.46 | 1584 |

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
| 3215765 | 1 | 121.4749064290 | 31.1483512404 | 175 | 4 | 10 | 47.3 | TDD | 307 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3236705 | 2 | 121.4752943859 | 31.1521268868 | 175 | 3 | 11 | 15.7 | TDD | 380 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3242261 | 3 | 121.4755937036 | 31.1535910607 | 165 | 2 | 8 | 44.7 | TDD | 101 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3276975 | 4 | 121.4712818205 | 31.1538015923 | 300 | 12 | 6 | 22.7 | TDD | 828 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.854 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.872 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.986 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.986 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.654 | NREventA3 | measId:2;ServCellPCI:40;Ser... |
| 2024-09-20 22:21:37.894 | NRHandoverAttempt | SourcePCI:40;SourceNR-ARFCN... |
| 2024-09-20 22:21:37.940 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.954 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.084 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.084 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3215765 | 1 | 88.5065 | 75.3964 | -115.7239 | 6.8430 | 95.8951 | 0.0046 | 0.0123 |
| 2024_09_19 22:00 | 3236705 | 2 | 78.2574 | 75.1931 | -117.2836 | 18.3328 | 192.0859 | 0.0002 | 0.0088 |
| 2024_09_19 22:00 | 3242261 | 3 | 90.7816 | 87.5029 | -116.0374 | 8.3990 | 118.7672 | 0.0065 | 0.0165 |
| 2024_09_19 22:00 | 3276975 | 4 | 84.3424 | 85.8007 | -117.7949 | 6.8707 | 90.3657 | 0.0135 | 0.0153 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415530_47D20011 | 504990 | 828 | -86.6 | 504990 | 380 | -91.8 | 504990 | 101 | -100.8 | 504990 | 307 |
| MR_1774415530_F8086F62 | 504990 | 828 | -88.2 | 504990 | 380 | -89.2 | 504990 | 101 | -102.4 | 504990 | 307 |
| MR_1774415530_9DBFEC27 | 504990 | 828 | -86.5 | 504990 | 380 | -91.8 | 504990 | 101 | -100.6 | 504990 | 307 |
| MR_1774415530_B09EF2EF | 504990 | 828 | -87.0 | 504990 | 380 | -92.3 | 504990 | 101 | -99.3 | 504990 | 307 |
| MR_1774415530_62148E98 | 504990 | 828 | -87.6 | 504990 | 380 | -90.5 | 504990 | 101 | -102.2 | 504990 | 307 |
| MR_1774415530_00E7872F | 504990 | 828 | -87.6 | 504990 | 380 | -91.4 | 504990 | 101 | -99.3 | 504990 | 307 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 874: `40c65260-700...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `40c65260-7005-4c9a-9404-597bd91e520a` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[874] topology](images/train_0874.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3262901_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase A3 Offset threshold for 3277015_1
- `C4`: Add neighbor relationship between 3262901_2 and 3277015_1
- `C5`: Add neighbor relationship between 3261356_3 and 3277015_1
- `C6`: Press down the tilt angle of 3262901_2 by 10 degrees
- `C7`: Lift the tilt angle  of 3277015_1 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277015_1
- `C9`: Increase transmission power for 3277015_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277015_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262901_2
- `C12`: Adjust the azimuth of 3277015_1 by 50 degrees
- `C13`: Increase A3 Offset threshold for 3262901_2
- `C14`: Adjust the azimuth of 3262901_2 by 50 degrees
- `C15`: Lift the tilt angle of 3262901_2 by 10 degrees
- `C16`: Decrease transmission power for 3277015_1
- `C17`: Decrease transmission power for 3262901_2
- `C18`: Increase transmission power for 3262901_2
- `C19`: Decrease A3 Offset threshold for 3277015_1
- `C20`: Press down the tilt angle  of 3277015_1 by 10 degrees
- `C21`: Check test server and transmission issues **← 정답**
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262901_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.429 | MS1 | 121.4656706954 | 31.1446306404 | 203 | 504990 | -88.38 | 12.42 | 494.22 | 0.09 | 2.89 | 1576 |
| 2024-09-20 22:21:32.759 | MS1 | 121.4656642811 | 31.1446254801 | 203 | 504990 | -86.57 | 14.69 | 318.61 | 0.05 | 2.94 | 1584 |
| 2024-09-20 22:21:33.944 | MS1 | 121.4656656287 | 31.1446316334 | 203 | 504990 | -85.63 | 12.65 | 391.48 | 0.09 | 2.05 | 1572 |
| 2024-09-20 22:21:34.122 | MS1 | 121.4656720388 | 31.1446342137 | 203 | 504990 | -90.47 | 17.13 | 89.54 | 0.03 | 2.94 | 444 |
| 2024-09-20 22:21:35.754 | MS1 | 121.4656697011 | 31.1446301185 | 203 | 504990 | -91.14 | 17.00 | 64.91 | 0.05 | 2.54 | 449 |
| 2024-09-20 22:21:36.263 | MS1 | 121.4656757229 | 31.1446316229 | 203 | 504990 | -87.87 | 16.72 | 80.91 | 0.17 | 2.36 | 329 |
| 2024-09-20 22:21:37.184 | MS1 | 121.4656597283 | 31.1446216298 | 203 | 504990 | -90.19 | 9.67 | 60.49 | 0.19 | 2.95 | 463 |
| 2024-09-20 22:21:38.390 | MS1 | 121.4656698314 | 31.1446324483 | 203 | 504990 | -89.60 | 9.18 | 83.39 | 0.16 | 2.73 | 478 |
| 2024-09-20 22:21:39.838 | MS1 | 121.4656602766 | 31.1446334649 | 203 | 504990 | -91.46 | 10.40 | 98.24 | 0.08 | 2.86 | 387 |
| 2024-09-20 22:21:40.436 | MS1 | 121.4656675234 | 31.1446351939 | 203 | 504990 | -91.74 | 9.81 | 355.94 | 0.06 | 2.77 | 1595 |
| 2024-09-20 22:21:41.391 | MS1 | 121.4656686738 | 31.1446258952 | 203 | 504990 | -90.62 | 8.69 | 552.13 | 0.07 | 2.92 | 1561 |
| 2024-09-20 22:21:42.241 | MS1 | 121.4656723789 | 31.1446335565 | 203 | 504990 | -89.52 | 9.47 | 580.34 | 0.15 | 2.02 | 1596 |

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
| 3261356 | 3 | 121.4666903486 | 31.1473202020 | 138 | 12 | 10 | 22.4 | TDD | 148 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3262901 | 2 | 121.4651595351 | 31.1530216248 | 75 | 14 | 3 | 22.1 | TDD | 203 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3275443 | 4 | 121.4642021162 | 31.1454244447 | 65 | 8 | 3 | 35.5 | TDD | 362 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3277015 | 1 | 121.4726932173 | 31.1442938018 | 344 | 12 | 3 | 33.2 | TDD | 98 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.917 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.938 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.074 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.074 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.795 | NREventA3 | measId:2;ServCellPCI:924;Se... |
| 2024-09-20 22:21:38.035 | NRHandoverAttempt | SourcePCI:924;SourceNR-ARFC... |
| 2024-09-20 22:21:38.077 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.089 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.231 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.231 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277015 | 1 | 6.3152 | 12.8552 | -116.8943 | 10.6400 | 166.2863 | 0.0127 | 0.0146 |
| 2024_09_20 22:00 | 3262901 | 2 | 14.2658 | 17.6437 | -117.9162 | 9.4296 | 196.4517 | 0.0013 | 0.0101 |
| 2024_09_20 22:00 | 3261356 | 3 | 13.0311 | 14.0024 | -114.4894 | 19.0959 | 185.4924 | 0.0090 | 0.0065 |
| 2024_09_20 22:00 | 3275443 | 4 | 15.0356 | 13.3027 | -116.0423 | 8.4220 | 196.8986 | 0.0178 | 0.0072 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414546_B44E7202 | 504990 | 203 | -90.5 | 504990 | 98 | -91.4 | 504990 | 148 | -106.0 | 504990 | 362 |
| MR_1774414546_16A65CDE | 504990 | 203 | -89.8 | 504990 | 98 | -92.9 | 504990 | 148 | -104.6 | 504990 | 362 |
| MR_1774414546_7488959F | 504990 | 203 | -91.1 | 504990 | 98 | -89.6 | 504990 | 148 | -104.0 | 504990 | 362 |
| MR_1774414546_6E047D1B | 504990 | 203 | -88.5 | 504990 | 98 | -91.0 | 504990 | 148 | -102.1 | 504990 | 362 |
| MR_1774414546_6B117BA3 | 504990 | 203 | -91.7 | 504990 | 98 | -89.8 | 504990 | 148 | -104.3 | 504990 | 362 |
| MR_1774414546_C532F663 | 504990 | 203 | -88.6 | 504990 | 98 | -93.0 | 504990 | 148 | -106.1 | 504990 | 362 |
| MR_1774414546_DF9C9B1A | 504990 | 203 | -91.3 | 504990 | 98 | -90.3 | 504990 | 148 | -104.3 | 504990 | 362 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 875: `7effd118-172...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7effd118-1720-4178-8956-96dea9f0c6f1` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3264274_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[875] topology](images/train_0875.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3264274_3
- `C2`: Decrease A3 Offset threshold for 3245973_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245973_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264274_3
- `C5`: Add neighbor relationship between 3264274_3 and 3245973_2
- `C6`: Increase A3 Offset threshold for 3264274_3
- `C7`: Adjust the azimuth of 3264274_3 by 48 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245973_2
- `C9`: Decrease transmission power for 3264274_3
- `C10`: Adjust the azimuth of 3245973_2 by 50 degrees
- `C11`: Decrease transmission power for 3245973_2
- `C12`: Check test server and transmission issues
- `C13`: Add neighbor relationship between 3239481_1 and 3245973_2
- `C14`: Increase transmission power for 3264274_3
- `C15`: Press down the tilt angle  of 3245973_2 by 10 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264274_3 **← 정답**
- `C17`: Press down the tilt angle of 3264274_3 by 2 degrees
- `C18`: Lift the tilt angle of 3264274_3 by 2 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase transmission power for 3245973_2
- `C21`: Lift the tilt angle  of 3245973_2 by 10 degrees
- `C22`: Increase A3 Offset threshold for 3245973_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.895 | MS1 | 121.4656722953 | 31.1446378631 | 721 | 504990 | -86.73 | 16.12 | 551.60 | 0.09 | 2.56 | 1593 |
| 2024-09-20 22:21:32.519 | MS1 | 121.4656628239 | 31.1446375246 | 721 | 504990 | -91.30 | 13.04 | 312.53 | 0.11 | 2.51 | 1572 |
| 2024-09-20 22:21:33.313 | MS1 | 121.4656691361 | 31.1446194094 | 721 | 504990 | -85.57 | 16.43 | 442.03 | 0.15 | 2.59 | 1570 |
| 2024-09-20 22:21:34.799 | MS1 | 121.4656768017 | 31.1446370555 | 721 | 504990 | -90.99 | 14.59 | 53.87 | 0.59 | 2.72 | 551 |
| 2024-09-20 22:21:35.699 | MS1 | 121.4656750492 | 31.1446205868 | 721 | 504990 | -88.61 | 12.35 | 78.70 | 0.63 | 2.44 | 677 |
| 2024-09-20 22:21:36.487 | MS1 | 121.4656764671 | 31.1446377975 | 721 | 504990 | -88.37 | 12.17 | 56.24 | 0.56 | 2.59 | 608 |
| 2024-09-20 22:21:37.376 | MS1 | 121.4656617619 | 31.1446286542 | 721 | 504990 | -92.68 | 11.34 | 84.11 | 0.59 | 2.77 | 669 |
| 2024-09-20 22:21:38.485 | MS1 | 121.4656616319 | 31.1446370127 | 721 | 504990 | -93.06 | 11.90 | 69.27 | 0.55 | 2.54 | 666 |
| 2024-09-20 22:21:39.981 | MS1 | 121.4656626207 | 31.1446329328 | 721 | 504990 | -93.04 | 11.65 | 70.74 | 0.54 | 2.96 | 669 |
| 2024-09-20 22:21:40.523 | MS1 | 121.4656704801 | 31.1446196021 | 721 | 504990 | -93.63 | 9.61 | 511.41 | 0.19 | 2.18 | 1581 |
| 2024-09-20 22:21:41.822 | MS1 | 121.4656593354 | 31.1446183960 | 721 | 504990 | -91.81 | 7.94 | 593.56 | 0.14 | 2.33 | 1566 |
| 2024-09-20 22:21:42.239 | MS1 | 121.4656586929 | 31.1446375199 | 721 | 504990 | -92.51 | 12.02 | 356.77 | 0.01 | 2.74 | 1586 |

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
| 3239481 | 1 | 121.4658068749 | 31.1543939400 | 198 | 14 | 12 | 30.5 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3245973 | 2 | 121.4710484591 | 31.1520538433 | 75 | 11 | 0 | 43.1 | TDD | 345 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3264274 | 3 | 121.4710658217 | 31.1540103666 | 254 | 1 | 10 | 23.2 | TDD | 721 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3264902 | 4 | 121.4684556116 | 31.1532159102 | 245 | 15 | 7 | 15.9 | TDD | 30 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.451 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.468 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.593 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.593 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.275 | NREventA3 | measId:2;ServCellPCI:490;Se... |
| 2024-09-20 22:21:38.515 | NRHandoverAttempt | SourcePCI:490;SourceNR-ARFC... |
| 2024-09-20 22:21:38.564 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.575 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.678 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.678 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239481 | 1 | 9.5742 | 13.3345 | -116.7776 | 6.3174 | 163.3804 | 0.0153 | 0.0196 |
| 2024_09_20 22:00 | 3245973 | 2 | 9.2208 | 6.3761 | -117.8029 | 16.4176 | 103.4179 | 0.0198 | 0.0192 |
| 2024_09_20 22:00 | 3264274 | 3 | 9.5277 | 17.5450 | -115.5567 | 5.8525 | 117.1774 | 0.0192 | 0.0006 |
| 2024_09_20 22:00 | 3264902 | 4 | 5.0685 | 5.9898 | -115.8094 | 10.8259 | 162.3531 | 0.0083 | 0.0050 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416180_B58CC51A | 504990 | 721 | -89.8 | 504990 | 345 | -93.6 | 504990 | 248 | -101.5 | 504990 | 30 |
| MR_1774416180_6CF11DAA | 504990 | 721 | -92.1 | 504990 | 345 | -95.5 | 504990 | 248 | -101.0 | 504990 | 30 |
| MR_1774416180_CC8F2270 | 504990 | 721 | -91.0 | 504990 | 345 | -92.9 | 504990 | 248 | -99.6 | 504990 | 30 |
| MR_1774416180_CE92C8CA | 504990 | 721 | -91.2 | 504990 | 345 | -95.2 | 504990 | 248 | -100.0 | 504990 | 30 |
| MR_1774416180_C72BEC20 | 504990 | 721 | -91.8 | 504990 | 345 | -92.5 | 504990 | 248 | -101.0 | 504990 | 30 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 876: `c7ecc466-3c7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c7ecc466-3c77-48d1-8f6c-b513b09af199` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease A3 Offset threshold for 3229263_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[876] topology](images/train_0876.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Add neighbor relationship between 3229263_1 and 3272344_4
- `C3`: Lift the tilt angle of 3229263_1 by 10 degrees
- `C4`: Increase transmission power for 3229263_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272344_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272344_4
- `C7`: Decrease A3 Offset threshold for 3229263_1 **← 정답**
- `C8`: Adjust the azimuth of 3272344_4 by 42 degrees
- `C9`: Decrease A3 Offset threshold for 3272344_4
- `C10`: Increase A3 Offset threshold for 3229263_1
- `C11`: Lift the tilt angle  of 3272344_4 by 10 degrees
- `C12`: Increase transmission power for 3272344_4
- `C13`: Add neighbor relationship between 3211865_3 and 3272344_4
- `C14`: Decrease transmission power for 3229263_1
- `C15`: Decrease transmission power for 3272344_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229263_1
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase A3 Offset threshold for 3272344_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229263_1
- `C20`: Adjust the azimuth of 3229263_1 by 50 degrees
- `C21`: Press down the tilt angle of 3229263_1 by 10 degrees
- `C22`: Press down the tilt angle  of 3272344_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.442 | MS1 | 121.4656735720 | 31.1446375758 | 78 | 504990 | -79.86 | 16.69 | 571.60 | 0.05 | 2.16 | 1586 |
| 2024-09-20 22:21:32.284 | MS1 | 121.4656581961 | 31.1446316026 | 78 | 504990 | -77.12 | 13.93 | 419.03 | 0.08 | 2.48 | 1594 |
| 2024-09-20 22:21:33.673 | MS1 | 121.4656592331 | 31.1446248546 | 78 | 504990 | -82.87 | 15.46 | 447.03 | 0.13 | 2.94 | 1592 |
| 2024-09-20 22:21:34.465 | MS1 | 121.4656667883 | 31.1446307099 | 78 | 504990 | -83.93 | -1.22 | 26.09 | 0.02 | 1.42 | 1583 |
| 2024-09-20 22:21:35.131 | MS1 | 121.4656588642 | 31.1446298635 | 78 | 504990 | -91.01 | -0.74 | 60.10 | 0.01 | 1.40 | 1599 |
| 2024-09-20 22:21:36.459 | MS1 | 121.4656676737 | 31.1446260674 | 78 | 504990 | -87.49 | -0.18 | 59.01 | 0.16 | 1.03 | 1589 |
| 2024-09-20 22:21:37.564 | MS1 | 121.4656592110 | 31.1446347326 | 78 | 504990 | -85.37 | -1.61 | 45.38 | 0.15 | 1.36 | 1569 |
| 2024-09-20 22:21:38.736 | MS1 | 121.4656756912 | 31.1446183266 | 78 | 504990 | -88.29 | -1.08 | 61.34 | 0.09 | 1.45 | 1583 |
| 2024-09-20 22:21:39.782 | MS1 | 121.4656719676 | 31.1446330412 | 799 | 504990 | -78.47 | 13.98 | 162.73 | 0.09 | 1.02 | 1598 |
| 2024-09-20 22:21:40.765 | MS1 | 121.4656591827 | 31.1446371223 | 799 | 504990 | -77.13 | 15.07 | 322.93 | 0.14 | 2.38 | 1570 |
| 2024-09-20 22:21:41.960 | MS1 | 121.4656759789 | 31.1446250286 | 799 | 504990 | -78.12 | 16.12 | 411.70 | 0.12 | 2.11 | 1596 |
| 2024-09-20 22:21:42.346 | MS1 | 121.4656588172 | 31.1446294975 | 799 | 504990 | -84.15 | 12.85 | 568.33 | 0.17 | 2.04 | 1565 |

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
| 3211865 | 3 | 121.4702089593 | 31.1472218897 | 38 | 8 | 11 | 21.0 | TDD | 342 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3229263 | 1 | 121.4689562799 | 31.1481573638 | 336 | 11 | 11 | 47.4 | TDD | 78 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3261753 | 2 | 121.4701251768 | 31.1517697364 | 254 | 8 | 3 | 35.5 | TDD | 165 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3272344 | 4 | 121.4680130474 | 31.1442619846 | 322 | 4 | 10 | 41.2 | TDD | 799 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.802 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.827 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.958 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.958 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.655 | NREventA3 | measId:2;ServCellPCI:579;Se... |
| 2024-09-20 22:21:37.895 | NRHandoverAttempt | SourcePCI:579;SourceNR-ARFC... |
| 2024-09-20 22:21:37.945 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.957 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.077 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.077 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229263 | 1 | 6.4910 | 11.5264 | -116.6702 | 5.4037 | 141.9534 | 0.0005 | 0.1979 |
| 2024_09_20 22:00 | 3261753 | 2 | 18.2831 | 16.3581 | -116.7716 | 6.5321 | 92.2910 | 0.0016 | 0.0113 |
| 2024_09_20 22:00 | 3211865 | 3 | 14.2957 | 7.7961 | -116.2849 | 9.3322 | 80.0574 | 0.0173 | 0.0068 |
| 2024_09_20 22:00 | 3272344 | 4 | 17.1316 | 18.8981 | -116.2762 | 5.9953 | 178.7406 | 0.0076 | 0.0106 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416654_2AD63319 | 504990 | 799 | -79.4 | 504990 | 78 | -85.8 | 504990 | 342 | -80.5 | 504990 | 165 |
| MR_1774416654_1C21AE3D | 504990 | 78 | -84.6 | 504990 | 799 | -77.7 | 504990 | 342 | -79.6 | 504990 | 165 |
| MR_1774416654_933AE30F | 504990 | 799 | -78.7 | 504990 | 78 | -84.2 | 504990 | 342 | -81.3 | 504990 | 165 |
| MR_1774416654_E1DDCEED | 504990 | 78 | -84.6 | 504990 | 799 | -78.1 | 504990 | 342 | -80.3 | 504990 | 165 |
| MR_1774416654_4953ADD5 | 504990 | 799 | -79.6 | 504990 | 78 | -83.7 | 504990 | 342 | -82.1 | 504990 | 165 |
| MR_1774416654_F0E2E475 | 504990 | 799 | -79.3 | 504990 | 78 | -85.9 | 504990 | 342 | -82.9 | 504990 | 165 |
| MR_1774416654_D27874AD | 504990 | 799 | -78.0 | 504990 | 78 | -85.5 | 504990 | 342 | -81.3 | 504990 | 165 |
| MR_1774416654_90A460BA | 504990 | 799 | -77.0 | 504990 | 78 | -83.4 | 504990 | 342 | -80.6 | 504990 | 165 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 877: `6daaa66a-a5c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6daaa66a-a5ce-4d4a-9336-79b57ef2fce9` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Lift the tilt angle  of 3227953_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[877] topology](images/train_0877.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3227953_2 by 10 degrees
- `C2`: Check test server and transmission issues
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261478_4
- `C4`: Decrease A3 Offset threshold for 3261478_4
- `C5`: Adjust the azimuth of 3266669_1 by 5 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261478_4
- `C7`: Increase A3 Offset threshold for 3261478_4
- `C8`: Decrease transmission power for 3261478_4
- `C9`: Add neighbor relationship between 3266669_1 and 3261478_4
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Add neighbor relationship between 3227953_2 and 3261478_4
- `C12`: Lift the tilt angle  of 3227953_2 by 10 degrees **← 정답**
- `C13`: Decrease A3 Offset threshold for 3266669_1
- `C14`: Increase transmission power for 3261478_4
- `C15`: Increase transmission power for 3266669_1
- `C16`: Press down the tilt angle of 3266669_1 by 2 degrees
- `C17`: Lift the tilt angle of 3266669_1 by 2 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266669_1
- `C19`: Increase A3 Offset threshold for 3266669_1
- `C20`: Decrease transmission power for 3266669_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266669_1
- `C22`: Adjust the azimuth of 3227953_2 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.185 | MS1 | 121.4656687851 | 31.1446182759 | 24 | 504990 | -88.49 | 17.48 | 482.72 | 0.10 | 2.55 | 1577 |
| 2024-09-20 22:21:32.613 | MS1 | 121.4656639366 | 31.1446326456 | 24 | 504990 | -87.61 | 12.91 | 560.37 | 0.16 | 2.33 | 1562 |
| 2024-09-20 22:21:33.463 | MS1 | 121.4656591202 | 31.1446227964 | 24 | 504990 | -87.52 | 12.08 | 333.65 | 0.05 | 2.81 | 1568 |
| 2024-09-20 22:21:34.668 | MS1 | 121.4656714775 | 31.1446290148 | 24 | 504990 | -88.91 | 17.15 | 107.47 | 0.05 | 2.48 | 1572 |
| 2024-09-20 22:21:35.911 | MS1 | 121.4656629506 | 31.1446206152 | 24 | 504990 | -85.43 | 14.78 | 60.64 | 0.06 | 2.57 | 1584 |
| 2024-09-20 22:21:36.865 | MS1 | 121.4656613761 | 31.1446278553 | 24 | 504990 | -89.92 | 17.77 | 71.22 | 0.14 | 2.61 | 1565 |
| 2024-09-20 22:21:37.253 | MS1 | 121.4656651323 | 31.1446320370 | 24 | 504990 | -91.93 | 9.86 | 77.13 | 0.01 | 2.11 | 1562 |
| 2024-09-20 22:21:38.886 | MS1 | 121.4656649225 | 31.1446322439 | 24 | 504990 | -92.15 | 11.21 | 91.33 | 0.13 | 2.50 | 1560 |
| 2024-09-20 22:21:39.190 | MS1 | 121.4656741013 | 31.1446210912 | 24 | 504990 | -90.73 | 7.48 | 104.51 | 0.14 | 2.04 | 1568 |
| 2024-09-20 22:21:40.458 | MS1 | 121.4656697682 | 31.1446355854 | 24 | 504990 | -93.48 | 12.49 | 330.94 | 0.08 | 2.81 | 1571 |
| 2024-09-20 22:21:41.847 | MS1 | 121.4656607041 | 31.1446202798 | 24 | 504990 | -93.26 | 8.81 | 482.92 | 0.12 | 2.84 | 1588 |
| 2024-09-20 22:21:42.301 | MS1 | 121.4656699851 | 31.1446192750 | 24 | 504990 | -91.64 | 8.49 | 509.73 | 0.10 | 2.96 | 1580 |

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
| 3227953 | 2 | 121.4733355523 | 31.1531786130 | 37 | 7 | 4 | 30.7 | TDD | 810 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3252501 | 3 | 121.4681546701 | 31.1483618100 | 105 | 3 | 3 | 34.4 | TDD | 996 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3261478 | 4 | 121.4739364145 | 31.1559407079 | 209 | 10 | 4 | 46.2 | TDD | 400 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3266669 | 1 | 121.4720925416 | 31.1559514775 | 201 | 1 | 6 | 28.9 | TDD | 24 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.464 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.481 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.611 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.611 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.327 | NREventA3 | measId:2;ServCellPCI:332;Se... |
| 2024-09-20 22:21:38.567 | NRHandoverAttempt | SourcePCI:332;SourceNR-ARFC... |
| 2024-09-20 22:21:38.613 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.623 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.750 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.750 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266669 | 1 | 85.8792 | 94.7526 | -114.8976 | 16.9499 | 165.6610 | 0.0063 | 0.0158 |
| 2024_09_20 22:00 | 3227953 | 2 | 15.0152 | 5.4343 | -117.1107 | 5.6294 | 98.7756 | 0.0050 | 0.0103 |
| 2024_09_20 22:00 | 3252501 | 3 | 14.4801 | 18.1394 | -114.8588 | 6.8491 | 82.1973 | 0.0146 | 0.0115 |
| 2024_09_20 22:00 | 3261478 | 4 | 5.3896 | 11.9011 | -117.7301 | 12.9954 | 178.8659 | 0.0177 | 0.0199 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415334_0B036EA6 | 504990 | 24 | -87.4 | 504990 | 400 | -93.0 | 504990 | 810 | -93.2 | 504990 | 996 |
| MR_1774415334_135B299C | 504990 | 24 | -84.4 | 504990 | 400 | -93.8 | 504990 | 810 | -95.1 | 504990 | 996 |
| MR_1774415334_AD1ABE92 | 504990 | 24 | -84.3 | 504990 | 400 | -94.0 | 504990 | 810 | -94.4 | 504990 | 996 |
| MR_1774415334_D0C357CD | 504990 | 24 | -84.4 | 504990 | 400 | -91.8 | 504990 | 810 | -94.1 | 504990 | 996 |
| MR_1774415334_76BCFDBF | 504990 | 24 | -85.0 | 504990 | 400 | -92.7 | 504990 | 810 | -95.7 | 504990 | 996 |
| MR_1774415334_AEAC363C | 504990 | 24 | -86.7 | 504990 | 400 | -91.9 | 504990 | 810 | -93.2 | 504990 | 996 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 878: `bb6cae6c-61a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bb6cae6c-61a8-42d4-91b1-2c90cd9e1d56` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Add neighbor relationship between 3266961_4 and 3272427_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[878] topology](images/train_0878.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3266961_4
- `C2`: Press down the tilt angle of 3266961_4 by 9 degrees
- `C3`: Increase A3 Offset threshold for 3266961_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266961_4
- `C5`: Add neighbor relationship between 3232058_2 and 3272427_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272427_1
- `C7`: Decrease transmission power for 3266961_4
- `C8`: Press down the tilt angle  of 3272427_1 by 5 degrees
- `C9`: Add neighbor relationship between 3266961_4 and 3272427_1 **← 정답**
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase A3 Offset threshold for 3272427_1
- `C12`: Lift the tilt angle of 3266961_4 by 9 degrees
- `C13`: Decrease A3 Offset threshold for 3266961_4
- `C14`: Decrease transmission power for 3272427_1
- `C15`: Adjust the azimuth of 3272427_1 by 28 degrees
- `C16`: Check test server and transmission issues
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266961_4
- `C18`: Decrease A3 Offset threshold for 3272427_1
- `C19`: Increase transmission power for 3272427_1
- `C20`: Lift the tilt angle  of 3272427_1 by 5 degrees
- `C21`: Adjust the azimuth of 3266961_4 by 50 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272427_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.918 | MS1 | 121.4656674271 | 31.1446325396 | 622 | 504990 | -83.89 | 15.92 | 425.62 | 0.14 | 2.55 | 1586 |
| 2024-09-20 22:21:32.280 | MS1 | 121.4656701387 | 31.1446187125 | 622 | 504990 | -78.05 | 13.52 | 466.57 | 0.08 | 2.99 | 1567 |
| 2024-09-20 22:21:33.736 | MS1 | 121.4656776848 | 31.1446203005 | 622 | 504990 | -75.77 | 13.44 | 337.37 | 0.10 | 2.28 | 1569 |
| 2024-09-20 22:21:34.816 | MS1 | 121.4656644656 | 31.1446341589 | 622 | 504990 | -94.38 | -2.19 | 50.54 | 0.15 | 1.48 | 1571 |
| 2024-09-20 22:21:35.856 | MS1 | 121.4656640729 | 31.1446363713 | 622 | 504990 | -90.32 | -3.69 | 45.37 | 0.05 | 1.08 | 1585 |
| 2024-09-20 22:21:36.591 | MS1 | 121.4656673998 | 31.1446193187 | 622 | 504990 | -87.71 | -0.38 | 59.71 | 0.14 | 1.48 | 1595 |
| 2024-09-20 22:21:37.844 | MS1 | 121.4656664082 | 31.1446371270 | 622 | 504990 | -89.12 | -1.52 | 34.73 | 0.10 | 1.19 | 1567 |
| 2024-09-20 22:21:38.706 | MS1 | 121.4656759532 | 31.1446199824 | 622 | 504990 | -84.33 | 16.36 | 334.87 | 0.10 | 1.04 | 1565 |
| 2024-09-20 22:21:39.598 | MS1 | 121.4656636415 | 31.1446223426 | 622 | 504990 | -77.60 | 15.61 | 476.01 | 0.09 | 1.31 | 1571 |
| 2024-09-20 22:21:40.907 | MS1 | 121.4656721838 | 31.1446374037 | 622 | 504990 | -82.58 | 12.22 | 485.66 | 0.00 | 2.85 | 1577 |
| 2024-09-20 22:21:41.186 | MS1 | 121.4656724830 | 31.1446246927 | 622 | 504990 | -75.22 | 16.91 | 593.63 | 0.16 | 2.96 | 1570 |
| 2024-09-20 22:21:42.669 | MS1 | 121.4656657326 | 31.1446376424 | 622 | 504990 | -75.06 | 13.67 | 322.20 | 0.04 | 2.55 | 1560 |

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
| 3232058 | 2 | 121.4725343791 | 31.1484195933 | 164 | 15 | 9 | 47.7 | TDD | 266 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3239249 | 3 | 121.4712020275 | 31.1512996797 | 317 | 15 | 0 | 41.0 | TDD | 810 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3266961 | 4 | 121.4643836245 | 31.1522086459 | 222 | 7 | 9 | 25.0 | TDD | 622 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3272427 | 1 | 121.4706914114 | 31.1461387454 | 223 | 3 | 8 | 17.6 | TDD | 209 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.042 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.064 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.195 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.195 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.874 | NREventA3 | measId:2;ServCellPCI:637;Se... |
| 2024-09-20 22:21:35.874 | NREventA3 | measId:2;ServCellPCI:637;Se... |
| 2024-09-20 22:21:36.874 | NREventA3 | measId:2;ServCellPCI:637;Se... |
| 2024-09-20 22:21:39.374 | NRRRCReestablishAttempt | PCI:637 |
| 2024-09-20 22:21:39.386 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.400 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.543 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.543 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272427 | 1 | 16.3257 | 9.7764 | -117.5541 | 16.8843 | 168.1139 | 0.0080 | 0.0061 |
| 2024_09_20 22:00 | 3232058 | 2 | 10.7496 | 19.6244 | -116.7695 | 9.1640 | 93.9559 | 0.0164 | 0.0088 |
| 2024_09_20 22:00 | 3239249 | 3 | 12.3632 | 9.6660 | -115.8144 | 15.2643 | 99.3794 | 0.0017 | 0.0151 |
| 2024_09_20 22:00 | 3266961 | 4 | 11.9414 | 17.6207 | -117.4071 | 12.5817 | 155.2415 | 0.0031 | 0.1318 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415235_1BA5D84E | 504990 | 622 | -96.2 | 504990 | 209 | -88.1 | 504990 | 266 | -91.5 | 504990 | 810 |
| MR_1774415235_455167D2 | 504990 | 209 | -90.4 | 504990 | 622 | -94.1 | 504990 | 266 | -91.1 | 504990 | 810 |
| MR_1774415235_891B36A2 | 504990 | 209 | -89.4 | 504990 | 622 | -93.2 | 504990 | 266 | -92.5 | 504990 | 810 |
| MR_1774415235_2ABA56B5 | 504990 | 209 | -90.4 | 504990 | 622 | -93.5 | 504990 | 266 | -91.4 | 504990 | 810 |
| MR_1774415235_7975F534 | 504990 | 622 | -95.9 | 504990 | 209 | -89.1 | 504990 | 266 | -92.4 | 504990 | 810 |
| MR_1774415235_F791A357 | 504990 | 622 | -93.9 | 504990 | 209 | -91.2 | 504990 | 266 | -92.1 | 504990 | 810 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 879: `bde467bd-fca...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bde467bd-fcac-4eb6-a115-f215ffcaebf1` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Lift the tilt angle  of 3239641_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[879] topology](images/train_0879.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Add neighbor relationship between 3239641_3 and 3266529_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232845_4
- `C4`: Press down the tilt angle of 3232845_4 by 3 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232845_4
- `C6`: Add neighbor relationship between 3232845_4 and 3266529_2
- `C7`: Decrease transmission power for 3266529_2
- `C8`: Increase transmission power for 3266529_2
- `C9`: Lift the tilt angle of 3232845_4 by 3 degrees
- `C10`: Adjust the azimuth of 3232845_4 by 0 degrees
- `C11`: Lift the tilt angle  of 3239641_3 by 10 degrees **← 정답**
- `C12`: Check test server and transmission issues
- `C13`: Adjust the azimuth of 3239641_3 by 46 degrees
- `C14`: Increase transmission power for 3232845_4
- `C15`: Decrease A3 Offset threshold for 3232845_4
- `C16`: Press down the tilt angle  of 3239641_3 by 10 degrees
- `C17`: Increase A3 Offset threshold for 3232845_4
- `C18`: Decrease A3 Offset threshold for 3266529_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266529_2
- `C20`: Decrease transmission power for 3232845_4
- `C21`: Increase A3 Offset threshold for 3266529_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266529_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.975 | MS1 | 121.4656718843 | 31.1446246788 | 639 | 504990 | -91.99 | 15.50 | 542.38 | 0.08 | 2.13 | 1577 |
| 2024-09-20 22:21:32.142 | MS1 | 121.4656632489 | 31.1446336342 | 639 | 504990 | -91.16 | 17.92 | 506.78 | 0.10 | 2.34 | 1598 |
| 2024-09-20 22:21:33.980 | MS1 | 121.4656762339 | 31.1446206638 | 639 | 504990 | -89.81 | 17.07 | 459.62 | 0.17 | 2.65 | 1577 |
| 2024-09-20 22:21:34.368 | MS1 | 121.4656744190 | 31.1446278932 | 639 | 504990 | -90.99 | 14.80 | 75.79 | 0.01 | 2.27 | 1564 |
| 2024-09-20 22:21:35.103 | MS1 | 121.4656627498 | 31.1446225820 | 639 | 504990 | -89.10 | 16.69 | 72.86 | 0.14 | 2.88 | 1565 |
| 2024-09-20 22:21:36.210 | MS1 | 121.4656639906 | 31.1446270573 | 639 | 504990 | -89.29 | 14.13 | 48.38 | 0.16 | 2.67 | 1589 |
| 2024-09-20 22:21:37.613 | MS1 | 121.4656640889 | 31.1446200844 | 639 | 504990 | -93.30 | 8.03 | 85.60 | 0.18 | 2.69 | 1588 |
| 2024-09-20 22:21:38.457 | MS1 | 121.4656757162 | 31.1446250776 | 639 | 504990 | -90.02 | 11.07 | 54.93 | 0.20 | 2.74 | 1567 |
| 2024-09-20 22:21:39.132 | MS1 | 121.4656607944 | 31.1446242877 | 639 | 504990 | -91.94 | 8.61 | 61.31 | 0.09 | 2.76 | 1562 |
| 2024-09-20 22:21:40.202 | MS1 | 121.4656674763 | 31.1446184049 | 639 | 504990 | -89.50 | 10.26 | 568.68 | 0.01 | 2.32 | 1599 |
| 2024-09-20 22:21:41.367 | MS1 | 121.4656761615 | 31.1446197373 | 639 | 504990 | -91.98 | 11.59 | 496.07 | 0.04 | 2.09 | 1597 |
| 2024-09-20 22:21:42.966 | MS1 | 121.4656666977 | 31.1446340837 | 639 | 504990 | -92.21 | 9.00 | 456.79 | 0.06 | 2.66 | 1566 |

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
| 3232845 | 4 | 121.4755434719 | 31.1516933451 | 230 | 2 | 7 | 27.5 | TDD | 639 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3239641 | 3 | 121.4663759796 | 31.1451855950 | 102 | 2 | 12 | 40.9 | TDD | 814 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3247099 | 1 | 121.4641496500 | 31.1446820471 | 33 | 1 | 1 | 26.8 | TDD | 73 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3266529 | 2 | 121.4688287252 | 31.1480615964 | 264 | 10 | 7 | 16.9 | TDD | 651 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.575 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.598 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.725 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.725 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.441 | NREventA3 | measId:2;ServCellPCI:440;Se... |
| 2024-09-20 22:21:38.681 | NRHandoverAttempt | SourcePCI:440;SourceNR-ARFC... |
| 2024-09-20 22:21:38.726 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.739 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.858 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.858 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247099 | 1 | 17.5693 | 17.1068 | -116.2932 | 15.9971 | 157.5179 | 0.0145 | 0.0029 |
| 2024_09_20 22:00 | 3266529 | 2 | 15.2475 | 17.9881 | -114.1679 | 8.7802 | 86.1549 | 0.0126 | 0.0025 |
| 2024_09_20 22:00 | 3239641 | 3 | 14.8429 | 19.0969 | -114.4005 | 17.0890 | 83.9560 | 0.0089 | 0.0023 |
| 2024_09_20 22:00 | 3232845 | 4 | 83.6896 | 92.6533 | -114.7763 | 7.2863 | 199.1701 | 0.0113 | 0.0036 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414916_DBE35A2C | 504990 | 639 | -89.8 | 504990 | 651 | -98.1 | 504990 | 814 | -98.4 | 504990 | 73 |
| MR_1774414916_73D81A88 | 504990 | 639 | -91.8 | 504990 | 651 | -96.1 | 504990 | 814 | -97.6 | 504990 | 73 |
| MR_1774414916_B9A38403 | 504990 | 639 | -89.5 | 504990 | 651 | -96.8 | 504990 | 814 | -98.5 | 504990 | 73 |
| MR_1774414916_E898E8F9 | 504990 | 639 | -92.2 | 504990 | 651 | -97.5 | 504990 | 814 | -99.4 | 504990 | 73 |
| MR_1774414916_FE356EDD | 504990 | 639 | -89.3 | 504990 | 651 | -96.1 | 504990 | 814 | -99.3 | 504990 | 73 |
| MR_1774414916_1A8C9124 | 504990 | 639 | -90.2 | 504990 | 651 | -99.4 | 504990 | 814 | -100.2 | 504990 | 73 |
| MR_1774414916_D516263E | 504990 | 639 | -91.4 | 504990 | 651 | -99.2 | 504990 | 814 | -97.6 | 504990 | 73 |

> *... 2개 열 생략 (전체 14열)*

---
