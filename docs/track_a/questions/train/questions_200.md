# Track A 문제 분석 — train[1990]~train[1999]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1990] ~ train[1999] (10개)

## 목차

1. [문제 1990: `e9680d05-9c5...`](#1990) — single-answer, 정답: C22
2. [문제 1991: `76a4928e-0e9...`](#1991) — single-answer, 정답: C8
3. [문제 1992: `e9fe0c0f-3fd...`](#1992) — multiple-answer, 정답: C2|C14|C20|C21
4. [문제 1993: `96464463-9c5...`](#1993) — single-answer, 정답: C16
5. [문제 1994: `9133bac1-234...`](#1994) — single-answer, 정답: C13
6. [문제 1995: `a6873872-65a...`](#1995) — single-answer, 정답: C11
7. [문제 1996: `4c0f4f75-161...`](#1996) — single-answer, 정답: C18
8. [문제 1997: `7b3003fb-9bf...`](#1997) — single-answer, 정답: C19
9. [문제 1998: `bbbf0187-a42...`](#1998) — single-answer, 정답: C21
10. [문제 1999: `6a686272-80c...`](#1999) — single-answer, 정답: C8

---

### 문제 1990: `e9680d05-9c5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e9680d05-9c5b-4081-9209-46f8fd0bfbb1` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Add neighbor relationship between 3241141_1 and 3211811_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1990] topology](images/train_1990.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3211811_2 by 6 degrees
- `C2`: Decrease A3 Offset threshold for 3211811_2
- `C3`: Decrease transmission power for 3241141_1
- `C4`: Increase A3 Offset threshold for 3211811_2
- `C5`: Add neighbor relationship between 3259156_4 and 3211811_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241141_1
- `C7`: Increase transmission power for 3211811_2
- `C8`: Decrease A3 Offset threshold for 3241141_1
- `C9`: Adjust the azimuth of 3211811_2 by 44 degrees
- `C10`: Check test server and transmission issues
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Press down the tilt angle of 3241141_1 by 10 degrees
- `C13`: Increase transmission power for 3241141_1
- `C14`: Adjust the azimuth of 3241141_1 by 50 degrees
- `C15`: Lift the tilt angle  of 3211811_2 by 6 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211811_2
- `C17`: Increase A3 Offset threshold for 3241141_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241141_1
- `C19`: Decrease transmission power for 3211811_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211811_2
- `C21`: Lift the tilt angle of 3241141_1 by 10 degrees
- `C22`: Add neighbor relationship between 3241141_1 and 3211811_2 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.646 | MS1 | 121.4656707405 | 31.1446355057 | 129 | 504990 | -80.00 | 17.24 | 461.52 | 0.18 | 2.41 | 1574 |
| 2024-09-20 22:21:32.624 | MS1 | 121.4656598869 | 31.1446285456 | 129 | 504990 | -82.05 | 16.03 | 456.34 | 0.15 | 2.66 | 1574 |
| 2024-09-20 22:21:33.526 | MS1 | 121.4656777825 | 31.1446258911 | 129 | 504990 | -82.58 | 12.10 | 535.81 | 0.19 | 2.87 | 1597 |
| 2024-09-20 22:21:34.973 | MS1 | 121.4656739858 | 31.1446262197 | 129 | 504990 | -88.03 | -1.93 | 35.68 | 0.00 | 1.11 | 1565 |
| 2024-09-20 22:21:35.605 | MS1 | 121.4656744302 | 31.1446209180 | 129 | 504990 | -88.20 | -0.44 | 39.23 | 0.17 | 1.32 | 1565 |
| 2024-09-20 22:21:36.199 | MS1 | 121.4656608072 | 31.1446326526 | 129 | 504990 | -90.73 | -2.05 | 36.66 | 0.06 | 1.28 | 1572 |
| 2024-09-20 22:21:37.803 | MS1 | 121.4656627236 | 31.1446356391 | 129 | 504990 | -92.13 | -1.22 | 69.88 | 0.09 | 1.13 | 1584 |
| 2024-09-20 22:21:38.381 | MS1 | 121.4656776221 | 31.1446204155 | 129 | 504990 | -83.26 | 12.43 | 589.44 | 0.00 | 1.48 | 1560 |
| 2024-09-20 22:21:39.544 | MS1 | 121.4656682866 | 31.1446365094 | 129 | 504990 | -82.80 | 15.31 | 397.54 | 0.03 | 1.14 | 1583 |
| 2024-09-20 22:21:40.802 | MS1 | 121.4656731340 | 31.1446340907 | 129 | 504990 | -79.54 | 17.02 | 325.81 | 0.14 | 2.29 | 1589 |
| 2024-09-20 22:21:41.469 | MS1 | 121.4656608272 | 31.1446202802 | 129 | 504990 | -75.64 | 16.26 | 306.80 | 0.18 | 2.59 | 1577 |
| 2024-09-20 22:21:42.415 | MS1 | 121.4656741746 | 31.1446360618 | 129 | 504990 | -80.09 | 12.22 | 559.47 | 0.11 | 2.12 | 1563 |

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
| 3211811 | 2 | 121.4659372065 | 31.1524158867 | 138 | 4 | 2 | 23.6 | TDD | 202 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3241141 | 1 | 121.4757469701 | 31.1521895014 | 137 | 8 | 8 | 35.4 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3246146 | 3 | 121.4657996016 | 31.1504731470 | 190 | 4 | 4 | 45.9 | TDD | 468 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3259156 | 4 | 121.4677979287 | 31.1479240311 | 4 | 5 | 9 | 37.2 | TDD | 825 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.549 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.564 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.697 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.697 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.414 | NREventA3 | measId:2;ServCellPCI:276;Se... |
| 2024-09-20 22:21:36.414 | NREventA3 | measId:2;ServCellPCI:276;Se... |
| 2024-09-20 22:21:37.414 | NREventA3 | measId:2;ServCellPCI:276;Se... |
| 2024-09-20 22:21:39.914 | NRRRCReestablishAttempt | PCI:276 |
| 2024-09-20 22:21:39.927 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.937 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:40.081 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.081 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241141 | 1 | 8.0099 | 14.9220 | -115.7500 | 14.8331 | 92.3709 | 0.0196 | 0.1218 |
| 2024_09_20 22:00 | 3211811 | 2 | 11.5017 | 15.3730 | -115.9456 | 17.6399 | 158.6707 | 0.0044 | 0.0025 |
| 2024_09_20 22:00 | 3246146 | 3 | 10.0608 | 9.7801 | -114.1094 | 6.5264 | 82.1066 | 0.0125 | 0.0149 |
| 2024_09_20 22:00 | 3259156 | 4 | 14.1225 | 19.5424 | -115.7932 | 6.5819 | 114.6638 | 0.0145 | 0.0058 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416730_273C6F5B | 504990 | 129 | -86.9 | 504990 | 202 | -83.4 | 504990 | 825 | -83.3 | 504990 | 468 |
| MR_1774416730_84678959 | 504990 | 202 | -83.5 | 504990 | 129 | -87.7 | 504990 | 825 | -85.1 | 504990 | 468 |
| MR_1774416730_5733401C | 504990 | 202 | -83.3 | 504990 | 129 | -89.4 | 504990 | 825 | -85.8 | 504990 | 468 |
| MR_1774416730_FA9345D1 | 504990 | 129 | -87.0 | 504990 | 202 | -83.3 | 504990 | 825 | -85.2 | 504990 | 468 |
| MR_1774416730_F5D0035F | 504990 | 129 | -87.3 | 504990 | 202 | -85.1 | 504990 | 825 | -82.1 | 504990 | 468 |
| MR_1774416730_B9AB73F3 | 504990 | 129 | -87.0 | 504990 | 202 | -83.0 | 504990 | 825 | -83.6 | 504990 | 468 |
| MR_1774416730_9B4FC318 | 504990 | 202 | -83.0 | 504990 | 129 | -88.8 | 504990 | 825 | -83.9 | 504990 | 468 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1991: `76a4928e-0e9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `76a4928e-0e9b-492f-bcd1-b5544aaaf55d` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Lift the tilt angle  of 3213747_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1991] topology](images/train_1991.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3260398_3 by 3 degrees
- `C2`: Decrease A3 Offset threshold for 3210981_4
- `C3`: Decrease transmission power for 3260398_3
- `C4`: Adjust the azimuth of 3213747_2 by 50 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210981_4
- `C6`: Press down the tilt angle  of 3213747_2 by 10 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260398_3
- `C8`: Lift the tilt angle  of 3213747_2 by 10 degrees **← 정답**
- `C9`: Increase transmission power for 3210981_4
- `C10`: Add neighbor relationship between 3213747_2 and 3210981_4
- `C11`: Add neighbor relationship between 3260398_3 and 3210981_4
- `C12`: Adjust the azimuth of 3260398_3 by 23 degrees
- `C13`: Increase A3 Offset threshold for 3260398_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260398_3
- `C15`: Increase A3 Offset threshold for 3210981_4
- `C16`: Check test server and transmission issues
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210981_4
- `C18`: Decrease transmission power for 3210981_4
- `C19`: Increase transmission power for 3260398_3
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Press down the tilt angle of 3260398_3 by 3 degrees
- `C22`: Decrease A3 Offset threshold for 3260398_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.989 | MS1 | 121.4656672512 | 31.1446246074 | 358 | 504990 | -91.07 | 12.57 | 439.62 | 0.08 | 2.95 | 1561 |
| 2024-09-20 22:21:32.580 | MS1 | 121.4656589952 | 31.1446377456 | 358 | 504990 | -90.24 | 13.25 | 438.14 | 0.16 | 2.30 | 1591 |
| 2024-09-20 22:21:33.122 | MS1 | 121.4656666803 | 31.1446376440 | 358 | 504990 | -90.89 | 14.87 | 554.01 | 0.13 | 2.33 | 1576 |
| 2024-09-20 22:21:34.707 | MS1 | 121.4656680780 | 31.1446277290 | 358 | 504990 | -90.34 | 12.14 | 89.54 | 0.16 | 2.71 | 1564 |
| 2024-09-20 22:21:35.655 | MS1 | 121.4656743630 | 31.1446191763 | 358 | 504990 | -86.44 | 12.34 | 88.24 | 0.17 | 2.15 | 1597 |
| 2024-09-20 22:21:36.375 | MS1 | 121.4656606000 | 31.1446371725 | 358 | 504990 | -89.86 | 16.42 | 71.00 | 0.16 | 2.94 | 1590 |
| 2024-09-20 22:21:37.851 | MS1 | 121.4656653413 | 31.1446317147 | 358 | 504990 | -91.19 | 9.61 | 85.06 | 0.01 | 2.77 | 1563 |
| 2024-09-20 22:21:38.729 | MS1 | 121.4656605231 | 31.1446281177 | 358 | 504990 | -89.25 | 7.37 | 94.13 | 0.18 | 2.33 | 1563 |
| 2024-09-20 22:21:39.479 | MS1 | 121.4656618760 | 31.1446281480 | 358 | 504990 | -93.37 | 12.04 | 68.02 | 0.12 | 2.26 | 1596 |
| 2024-09-20 22:21:40.676 | MS1 | 121.4656595143 | 31.1446203142 | 358 | 504990 | -93.75 | 9.13 | 575.56 | 0.11 | 2.23 | 1573 |
| 2024-09-20 22:21:41.150 | MS1 | 121.4656593255 | 31.1446335188 | 358 | 504990 | -92.35 | 7.73 | 353.50 | 0.12 | 2.98 | 1590 |
| 2024-09-20 22:21:42.272 | MS1 | 121.4656684918 | 31.1446304639 | 358 | 504990 | -93.99 | 12.89 | 505.04 | 0.14 | 2.41 | 1579 |

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
| 3210981 | 4 | 121.4697338348 | 31.1467621578 | 21 | 8 | 12 | 47.8 | TDD | 966 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3213747 | 2 | 121.4685660525 | 31.1459997770 | 351 | 9 | 10 | 37.0 | TDD | 753 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3226629 | 1 | 121.4707890245 | 31.1545896327 | 357 | 2 | 8 | 16.3 | TDD | 168 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3260398 | 3 | 121.4667144398 | 31.1533963831 | 163 | 0 | 3 | 44.6 | TDD | 358 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.950 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.086 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.086 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.768 | NREventA3 | measId:2;ServCellPCI:679;Se... |
| 2024-09-20 22:21:38.008 | NRHandoverAttempt | SourcePCI:679;SourceNR-ARFC... |
| 2024-09-20 22:21:38.047 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.060 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.179 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.179 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226629 | 1 | 14.5660 | 16.7046 | -115.5923 | 19.5779 | 198.1989 | 0.0012 | 0.0130 |
| 2024_09_20 22:00 | 3213747 | 2 | 15.7606 | 13.0171 | -117.7930 | 18.1764 | 108.0082 | 0.0106 | 0.0097 |
| 2024_09_20 22:00 | 3260398 | 3 | 87.1000 | 77.4235 | -116.1459 | 9.3468 | 110.4743 | 0.0191 | 0.0048 |
| 2024_09_20 22:00 | 3210981 | 4 | 16.6620 | 6.0909 | -115.2885 | 17.8666 | 173.6659 | 0.0031 | 0.0082 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413592_1DAAF7A9 | 504990 | 358 | -91.3 | 504990 | 966 | -96.1 | 504990 | 753 | -97.3 | 504990 | 168 |
| MR_1774413592_89550BDB | 504990 | 358 | -92.0 | 504990 | 966 | -97.9 | 504990 | 753 | -97.8 | 504990 | 168 |
| MR_1774413592_5B128E02 | 504990 | 358 | -91.8 | 504990 | 966 | -98.1 | 504990 | 753 | -97.6 | 504990 | 168 |
| MR_1774413592_915585A1 | 504990 | 358 | -91.0 | 504990 | 966 | -96.5 | 504990 | 753 | -98.2 | 504990 | 168 |
| MR_1774413592_62463877 | 504990 | 358 | -89.3 | 504990 | 966 | -97.5 | 504990 | 753 | -96.7 | 504990 | 168 |
| MR_1774413592_80313084 | 504990 | 358 | -91.5 | 504990 | 966 | -99.1 | 504990 | 753 | -97.6 | 504990 | 168 |
| MR_1774413592_2F90A9C4 | 504990 | 358 | -89.4 | 504990 | 966 | -95.7 | 504990 | 753 | -99.1 | 504990 | 168 |
| MR_1774413592_D0C1E5AF | 504990 | 358 | -89.6 | 504990 | 966 | -99.2 | 504990 | 753 | -99.6 | 504990 | 168 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1992: `e9fe0c0f-3fd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e9fe0c0f-3fd8-47b2-a39d-ab3c957055c1` |
| Tag | **multiple-answer** |
| 정답 | **C2|C14|C20|C21** |
| C2 의미 | Press down the tilt angle  of 3235210_2 by 3 degrees |
| C14 의미 | Decrease transmission power for 3235210_2 |
| C20 의미 | Increase A3 Offset threshold for 3235210_2 |
| C21 의미 | Increase A3 Offset threshold for 3248794_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1992] topology](images/train_1992.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3248794_4 by 3 degrees
- `C2`: Press down the tilt angle  of 3235210_2 by 3 degrees **← 정답**
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235210_2
- `C4`: Press down the tilt angle of 3248794_4 by 3 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248794_4
- `C7`: Increase transmission power for 3248794_4
- `C8`: Lift the tilt angle  of 3235210_2 by 3 degrees
- `C9`: Decrease transmission power for 3248794_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248794_4
- `C11`: Adjust the azimuth of 3235210_2 by 8 degrees
- `C12`: Increase transmission power for 3235210_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235210_2
- `C14`: Decrease transmission power for 3235210_2 **← 정답**
- `C15`: Add neighbor relationship between 3248794_4 and 3235210_2
- `C16`: Check test server and transmission issues
- `C17`: Add neighbor relationship between 3247210_3 and 3235210_2
- `C18`: Decrease A3 Offset threshold for 3235210_2
- `C19`: Adjust the azimuth of 3248794_4 by 39 degrees
- `C20`: Increase A3 Offset threshold for 3235210_2 **← 정답**
- `C21`: Increase A3 Offset threshold for 3248794_4 **← 정답**
- `C22`: Decrease A3 Offset threshold for 3248794_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.696 | MS1 | 121.4656580522 | 31.1446184263 | 723 | 504990 | -79.04 | 13.06 | 463.40 | 0.01 | 2.64 | 1573 |
| 2024-09-20 22:21:32.154 | MS1 | 121.4656596210 | 31.1446185804 | 723 | 504990 | -82.45 | 13.93 | 475.37 | 0.18 | 2.61 | 1565 |
| 2024-09-20 22:21:33.225 | MS1 | 121.4656747278 | 31.1446213639 | 723 | 504990 | -78.31 | 17.76 | 479.52 | 0.00 | 2.20 | 1584 |
| 2024-09-20 22:21:34.880 | MS1 | 121.4656601231 | 31.1446205389 | 316 | 504990 | -81.73 | 3.86 | 50.98 | 0.03 | 1.37 | 1590 |
| 2024-09-20 22:21:35.983 | MS1 | 121.4656693832 | 31.1446298763 | 316 | 504990 | -85.46 | 2.97 | 63.89 | 0.09 | 1.40 | 1571 |
| 2024-09-20 22:21:36.551 | MS1 | 121.4656767080 | 31.1446309561 | 723 | 504990 | -86.11 | 3.21 | 45.56 | 0.18 | 1.05 | 1562 |
| 2024-09-20 22:21:37.828 | MS1 | 121.4656762254 | 31.1446291617 | 723 | 504990 | -85.95 | 2.54 | 51.22 | 0.15 | 1.45 | 1597 |
| 2024-09-20 22:21:38.207 | MS1 | 121.4656772689 | 31.1446236473 | 316 | 504990 | -83.51 | 4.12 | 77.34 | 0.09 | 1.09 | 1566 |
| 2024-09-20 22:21:39.721 | MS1 | 121.4656656900 | 31.1446322933 | 316 | 504990 | -88.95 | 1.75 | 62.73 | 0.19 | 1.12 | 1570 |
| 2024-09-20 22:21:40.456 | MS1 | 121.4656588546 | 31.1446277765 | 316 | 504990 | -81.25 | 15.98 | 439.06 | 0.17 | 2.89 | 1582 |
| 2024-09-20 22:21:41.562 | MS1 | 121.4656655064 | 31.1446349955 | 316 | 504990 | -76.51 | 12.21 | 527.59 | 0.12 | 2.09 | 1560 |
| 2024-09-20 22:21:42.802 | MS1 | 121.4656698233 | 31.1446200878 | 316 | 504990 | -75.05 | 16.64 | 469.23 | 0.10 | 2.01 | 1578 |

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
| 3222667 | 1 | 121.4739920198 | 31.1480919966 | 128 | 11 | 11 | 37.8 | TDD | 837 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3235210 | 2 | 121.4757549342 | 31.1452915362 | 274 | 2 | 8 | 21.9 | TDD | 550 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3245406 | 5 | 121.4647268569 | 31.1533877560 | 58 | 2 | 0 | 27.9 | TDD | 316 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3247210 | 3 | 121.4755229164 | 31.1524627031 | 319 | 6 | 3 | 18.1 | TDD | 784 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3248794 | 4 | 121.4663030377 | 31.1506214179 | 224 | 1 | 5 | 22.8 | TDD | 723 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.067 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.082 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.223 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.223 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.884 | NREventA3 | measId:2;ServCellPCI:491;Se... |
| 2024-09-20 22:21:34.124 | NRHandoverAttempt | SourcePCI:491;SourceNR-ARFC... |
| 2024-09-20 22:21:34.160 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.175 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.291 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.291 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.884 | NREventA3 | measId:2;ServCellPCI:321;Se... |
| 2024-09-20 22:21:36.124 | NRHandoverAttempt | SourcePCI:321;SourceNR-ARFC... |
| 2024-09-20 22:21:36.170 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.185 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.311 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.311 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.884 | NREventA3 | measId:2;ServCellPCI:491;Se... |
| 2024-09-20 22:21:38.124 | NRHandoverAttempt | SourcePCI:491;SourceNR-ARFC... |
| 2024-09-20 22:21:38.170 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.184 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.314 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.314 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222667 | 1 | 19.9153 | 16.2859 | -116.9435 | 8.3608 | 199.7346 | 0.0028 | 0.0194 |
| 2024_09_20 22:00 | 3235210 | 2 | 12.9504 | 16.5930 | -116.9127 | 8.5261 | 155.2480 | 0.0051 | 0.0131 |
| 2024_09_20 22:00 | 3247210 | 3 | 6.4401 | 14.4397 | -117.6717 | 5.7637 | 198.4706 | 0.0012 | 0.0019 |
| 2024_09_20 22:00 | 3248794 | 4 | 15.4963 | 16.0975 | -117.0142 | 8.7755 | 175.4318 | 0.0110 | 0.0194 |
| 2024_09_20 22:00 | 3245406 | 5 | 16.7022 | 18.1467 | -117.4409 | 16.4218 | 163.4903 | 0.0094 | 0.0093 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414966_4F15B4C2 | 504990 | 723 | -80.9 | 504990 | 316 | -78.9 | 504990 | 550 | -83.4 | 504990 | 784 |
| MR_1774414966_9A952FC5 | 504990 | 723 | -83.6 | 504990 | 316 | -80.6 | 504990 | 550 | -82.9 | 504990 | 784 |
| MR_1774414966_F5F3C8AC | 504990 | 316 | -80.6 | 504990 | 723 | -80.0 | 504990 | 550 | -84.1 | 504990 | 784 |
| MR_1774414966_3AC7B507 | 504990 | 723 | -80.4 | 504990 | 316 | -79.2 | 504990 | 550 | -83.8 | 504990 | 784 |
| MR_1774414966_0555A08C | 504990 | 723 | -80.1 | 504990 | 316 | -81.4 | 504990 | 550 | -80.6 | 504990 | 784 |
| MR_1774414966_1038B9C6 | 504990 | 316 | -81.4 | 504990 | 723 | -79.6 | 504990 | 550 | -82.0 | 504990 | 784 |
| MR_1774414966_1FBB9253 | 504990 | 723 | -82.3 | 504990 | 316 | -80.6 | 504990 | 550 | -80.5 | 504990 | 784 |
| MR_1774414966_F846D864 | 504990 | 316 | -80.6 | 504990 | 723 | -80.1 | 504990 | 550 | -83.8 | 504990 | 784 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1993: `96464463-9c5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `96464463-9c55-4d8c-b9b8-0a4bf304eb8f` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1993] topology](images/train_1993.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259328_3
- `C2`: Adjust the azimuth of 3262884_1 by 48 degrees
- `C3`: Press down the tilt angle  of 3259328_3 by 10 degrees
- `C4`: Decrease transmission power for 3262884_1
- `C5`: Decrease A3 Offset threshold for 3262884_1
- `C6`: Decrease transmission power for 3259328_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259328_3
- `C8`: Lift the tilt angle of 3262884_1 by 10 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262884_1
- `C10`: Add neighbor relationship between 3266372_4 and 3259328_3
- `C11`: Press down the tilt angle of 3262884_1 by 10 degrees
- `C12`: Increase A3 Offset threshold for 3259328_3
- `C13`: Lift the tilt angle  of 3259328_3 by 10 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262884_1
- `C16`: Check test server and transmission issues **← 정답**
- `C17`: Decrease A3 Offset threshold for 3259328_3
- `C18`: Increase transmission power for 3262884_1
- `C19`: Add neighbor relationship between 3262884_1 and 3259328_3
- `C20`: Increase A3 Offset threshold for 3262884_1
- `C21`: Increase transmission power for 3259328_3
- `C22`: Adjust the azimuth of 3259328_3 by 11 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.419 | MS1 | 121.4656642433 | 31.1446253776 | 672 | 504990 | -85.90 | 14.28 | 316.26 | 0.14 | 2.79 | 1577 |
| 2024-09-20 22:21:32.626 | MS1 | 121.4656766894 | 31.1446292869 | 672 | 504990 | -85.86 | 13.36 | 512.24 | 0.15 | 2.50 | 1565 |
| 2024-09-20 22:21:33.311 | MS1 | 121.4656739214 | 31.1446351585 | 672 | 504990 | -90.21 | 15.75 | 331.89 | 0.10 | 2.30 | 1581 |
| 2024-09-20 22:21:34.342 | MS1 | 121.4656719939 | 31.1446360694 | 672 | 504990 | -86.22 | 14.90 | 55.96 | 0.11 | 2.05 | 446 |
| 2024-09-20 22:21:35.869 | MS1 | 121.4656630372 | 31.1446351170 | 672 | 504990 | -88.01 | 13.41 | 102.47 | 0.04 | 2.48 | 447 |
| 2024-09-20 22:21:36.137 | MS1 | 121.4656658043 | 31.1446211751 | 672 | 504990 | -86.14 | 13.58 | 66.34 | 0.02 | 2.56 | 343 |
| 2024-09-20 22:21:37.736 | MS1 | 121.4656683896 | 31.1446376373 | 672 | 504990 | -91.94 | 9.24 | 51.58 | 0.05 | 2.42 | 499 |
| 2024-09-20 22:21:38.251 | MS1 | 121.4656717080 | 31.1446377970 | 672 | 504990 | -93.32 | 7.73 | 80.50 | 0.19 | 2.45 | 356 |
| 2024-09-20 22:21:39.493 | MS1 | 121.4656737916 | 31.1446298699 | 672 | 504990 | -89.87 | 7.52 | 71.11 | 0.00 | 2.51 | 388 |
| 2024-09-20 22:21:40.497 | MS1 | 121.4656601851 | 31.1446365448 | 672 | 504990 | -89.73 | 10.34 | 400.19 | 0.01 | 2.75 | 1575 |
| 2024-09-20 22:21:41.203 | MS1 | 121.4656761334 | 31.1446211612 | 672 | 504990 | -90.34 | 12.15 | 593.81 | 0.01 | 2.89 | 1587 |
| 2024-09-20 22:21:42.904 | MS1 | 121.4656607668 | 31.1446270085 | 672 | 504990 | -89.27 | 9.63 | 321.85 | 0.15 | 2.62 | 1560 |

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
| 3259328 | 3 | 121.4664970969 | 31.1446552049 | 258 | 12 | 5 | 40.7 | TDD | 420 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3262884 | 1 | 121.4741017818 | 31.1466555825 | 206 | 14 | 7 | 38.6 | TDD | 672 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3266372 | 4 | 121.4742402082 | 31.1459904830 | 241 | 7 | 2 | 34.9 | TDD | 877 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3267312 | 2 | 121.4692758631 | 31.1452437744 | 210 | 1 | 8 | 35.2 | TDD | 483 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.023 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.038 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.164 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.164 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.859 | NREventA3 | measId:2;ServCellPCI:995;Se... |
| 2024-09-20 22:21:38.099 | NRHandoverAttempt | SourcePCI:995;SourceNR-ARFC... |
| 2024-09-20 22:21:38.136 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.149 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.287 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.287 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262884 | 1 | 17.4748 | 10.0222 | -116.6448 | 15.5493 | 118.2087 | 0.0015 | 0.0024 |
| 2024_09_20 22:00 | 3267312 | 2 | 13.6775 | 14.9967 | -114.3320 | 5.2702 | 146.8001 | 0.0065 | 0.0046 |
| 2024_09_20 22:00 | 3259328 | 3 | 17.1915 | 6.7601 | -116.7023 | 11.0224 | 107.6596 | 0.0174 | 0.0052 |
| 2024_09_20 22:00 | 3266372 | 4 | 14.5129 | 12.6774 | -114.7970 | 7.6967 | 103.2457 | 0.0140 | 0.0120 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415348_8CD2D85B | 504990 | 672 | -88.0 | 504990 | 420 | -88.1 | 504990 | 877 | -94.1 | 504990 | 483 |
| MR_1774415348_B580D881 | 504990 | 672 | -87.4 | 504990 | 420 | -88.3 | 504990 | 877 | -93.3 | 504990 | 483 |
| MR_1774415348_239B59D7 | 504990 | 672 | -86.6 | 504990 | 420 | -89.6 | 504990 | 877 | -93.2 | 504990 | 483 |
| MR_1774415348_69DD491D | 504990 | 672 | -86.1 | 504990 | 420 | -86.9 | 504990 | 877 | -91.1 | 504990 | 483 |
| MR_1774415348_8FE73B8D | 504990 | 672 | -86.5 | 504990 | 420 | -89.0 | 504990 | 877 | -91.4 | 504990 | 483 |
| MR_1774415348_5AFED47D | 504990 | 672 | -84.9 | 504990 | 420 | -89.0 | 504990 | 877 | -93.2 | 504990 | 483 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1994: `9133bac1-234...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9133bac1-2343-4f7c-92a6-e0e32ad5f52d` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1994] topology](images/train_1994.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266484_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216441_1
- `C3`: Adjust the azimuth of 3266484_3 by 15 degrees
- `C4`: Press down the tilt angle  of 3266484_3 by 10 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216441_1
- `C6`: Decrease A3 Offset threshold for 3216441_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266484_3
- `C8`: Increase transmission power for 3266484_3
- `C9`: Decrease transmission power for 3216441_1
- `C10`: Add neighbor relationship between 3216441_1 and 3266484_3
- `C11`: Lift the tilt angle  of 3266484_3 by 10 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Check test server and transmission issues **← 정답**
- `C14`: Decrease transmission power for 3266484_3
- `C15`: Decrease A3 Offset threshold for 3266484_3
- `C16`: Add neighbor relationship between 3233970_4 and 3266484_3
- `C17`: Increase transmission power for 3216441_1
- `C18`: Lift the tilt angle of 3216441_1 by 10 degrees
- `C19`: Press down the tilt angle of 3216441_1 by 10 degrees
- `C20`: Adjust the azimuth of 3216441_1 by 50 degrees
- `C21`: Increase A3 Offset threshold for 3216441_1
- `C22`: Increase A3 Offset threshold for 3266484_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.310 | MS1 | 121.4656647723 | 31.1446325097 | 336 | 504990 | -89.39 | 12.76 | 428.97 | 0.03 | 2.07 | 1598 |
| 2024-09-20 22:21:32.259 | MS1 | 121.4656728633 | 31.1446338479 | 336 | 504990 | -85.79 | 17.64 | 534.66 | 0.18 | 2.21 | 1569 |
| 2024-09-20 22:21:33.998 | MS1 | 121.4656643255 | 31.1446304143 | 336 | 504990 | -89.24 | 13.67 | 448.54 | 0.08 | 2.31 | 1597 |
| 2024-09-20 22:21:34.243 | MS1 | 121.4656764926 | 31.1446268471 | 336 | 504990 | -88.74 | 15.71 | 92.51 | 0.05 | 2.70 | 327 |
| 2024-09-20 22:21:35.491 | MS1 | 121.4656626145 | 31.1446312727 | 336 | 504990 | -85.74 | 15.20 | 55.18 | 0.20 | 2.57 | 446 |
| 2024-09-20 22:21:36.177 | MS1 | 121.4656747883 | 31.1446351981 | 336 | 504990 | -90.36 | 13.17 | 82.86 | 0.13 | 2.10 | 408 |
| 2024-09-20 22:21:37.160 | MS1 | 121.4656734062 | 31.1446181802 | 336 | 504990 | -89.64 | 7.80 | 48.96 | 0.18 | 2.09 | 375 |
| 2024-09-20 22:21:38.951 | MS1 | 121.4656675213 | 31.1446200690 | 336 | 504990 | -93.52 | 7.06 | 67.50 | 0.14 | 2.89 | 488 |
| 2024-09-20 22:21:39.202 | MS1 | 121.4656686480 | 31.1446285423 | 336 | 504990 | -89.73 | 8.07 | 105.43 | 0.10 | 2.20 | 419 |
| 2024-09-20 22:21:40.779 | MS1 | 121.4656756780 | 31.1446212018 | 336 | 504990 | -91.61 | 9.83 | 392.73 | 0.19 | 2.32 | 1575 |
| 2024-09-20 22:21:41.559 | MS1 | 121.4656585364 | 31.1446365851 | 336 | 504990 | -89.17 | 10.05 | 326.56 | 0.06 | 2.18 | 1588 |
| 2024-09-20 22:21:42.153 | MS1 | 121.4656762650 | 31.1446190777 | 336 | 504990 | -90.70 | 9.72 | 558.11 | 0.09 | 2.15 | 1596 |

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
| 3216441 | 1 | 121.4722496440 | 31.1525362896 | 108 | 8 | 5 | 39.9 | TDD | 336 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3233970 | 4 | 121.4697432483 | 31.1508893217 | 243 | 8 | 3 | 18.7 | TDD | 532 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3261851 | 2 | 121.4671785237 | 31.1495213954 | 24 | 0 | 7 | 28.2 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3266484 | 3 | 121.4750919187 | 31.1524748410 | 211 | 11 | 8 | 42.1 | TDD | 564 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.912 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.933 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.034 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.034 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.753 | NREventA3 | measId:2;ServCellPCI:598;Se... |
| 2024-09-20 22:21:37.993 | NRHandoverAttempt | SourcePCI:598;SourceNR-ARFC... |
| 2024-09-20 22:21:38.041 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.054 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.167 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.167 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216441 | 1 | 12.9644 | 19.4727 | -114.7796 | 17.4944 | 89.5173 | 0.0066 | 0.0132 |
| 2024_09_20 22:00 | 3261851 | 2 | 15.0929 | 18.3008 | -114.6757 | 8.2518 | 167.1956 | 0.0127 | 0.0142 |
| 2024_09_20 22:00 | 3266484 | 3 | 5.4017 | 7.4463 | -117.2468 | 15.8820 | 156.2241 | 0.0026 | 0.0081 |
| 2024_09_20 22:00 | 3233970 | 4 | 18.6353 | 9.9131 | -117.7694 | 18.6029 | 186.1398 | 0.0148 | 0.0146 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413833_8CFDDC46 | 504990 | 336 | -87.2 | 504990 | 564 | -94.9 | 504990 | 532 | -97.7 | 504990 | 129 |
| MR_1774413833_19A597D0 | 504990 | 336 | -87.0 | 504990 | 564 | -94.4 | 504990 | 532 | -97.9 | 504990 | 129 |
| MR_1774413833_5F2E56B2 | 504990 | 336 | -90.2 | 504990 | 564 | -95.4 | 504990 | 532 | -98.4 | 504990 | 129 |
| MR_1774413833_4CBDD9A4 | 504990 | 336 | -89.4 | 504990 | 564 | -96.6 | 504990 | 532 | -97.0 | 504990 | 129 |
| MR_1774413833_520B6B24 | 504990 | 336 | -90.5 | 504990 | 564 | -95.5 | 504990 | 532 | -98.2 | 504990 | 129 |
| MR_1774413833_226DEE4A | 504990 | 336 | -89.9 | 504990 | 564 | -97.6 | 504990 | 532 | -96.4 | 504990 | 129 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1995: `a6873872-65a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a6873872-65ab-412f-8348-4c57c73e3df3` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Add neighbor relationship between 3214906_3 and 3227993_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1995] topology](images/train_1995.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3227993_4 by 6 degrees
- `C2`: Increase A3 Offset threshold for 3227993_4
- `C3`: Increase transmission power for 3214906_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214906_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227993_4
- `C6`: Decrease transmission power for 3227993_4
- `C7`: Adjust the azimuth of 3227993_4 by 24 degrees
- `C8`: Increase A3 Offset threshold for 3214906_3
- `C9`: Add neighbor relationship between 3256508_1 and 3227993_4
- `C10`: Decrease transmission power for 3214906_3
- `C11`: Add neighbor relationship between 3214906_3 and 3227993_4 **← 정답**
- `C12`: Lift the tilt angle of 3214906_3 by 10 degrees
- `C13`: Press down the tilt angle  of 3227993_4 by 6 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214906_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227993_4
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease A3 Offset threshold for 3227993_4
- `C18`: Adjust the azimuth of 3214906_3 by 50 degrees
- `C19`: Press down the tilt angle of 3214906_3 by 10 degrees
- `C20`: Increase transmission power for 3227993_4
- `C21`: Check test server and transmission issues
- `C22`: Decrease A3 Offset threshold for 3214906_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.305 | MS1 | 121.4656715449 | 31.1446219423 | 766 | 504990 | -76.42 | 16.54 | 433.61 | 0.14 | 2.92 | 1566 |
| 2024-09-20 22:21:32.116 | MS1 | 121.4656732921 | 31.1446355557 | 766 | 504990 | -83.44 | 17.37 | 497.67 | 0.07 | 2.94 | 1565 |
| 2024-09-20 22:21:33.259 | MS1 | 121.4656757781 | 31.1446245452 | 766 | 504990 | -82.73 | 16.29 | 446.81 | 0.15 | 2.59 | 1568 |
| 2024-09-20 22:21:34.308 | MS1 | 121.4656620090 | 31.1446266613 | 766 | 504990 | -95.00 | -2.20 | 42.34 | 0.11 | 1.29 | 1584 |
| 2024-09-20 22:21:35.461 | MS1 | 121.4656697347 | 31.1446371607 | 766 | 504990 | -89.53 | -3.79 | 55.88 | 0.11 | 1.37 | 1563 |
| 2024-09-20 22:21:36.304 | MS1 | 121.4656663413 | 31.1446361842 | 766 | 504990 | -90.70 | -2.12 | 31.31 | 0.11 | 1.07 | 1569 |
| 2024-09-20 22:21:37.137 | MS1 | 121.4656668021 | 31.1446295032 | 766 | 504990 | -90.94 | -0.64 | 44.54 | 0.19 | 1.33 | 1586 |
| 2024-09-20 22:21:38.251 | MS1 | 121.4656631527 | 31.1446366505 | 766 | 504990 | -81.74 | 12.18 | 453.70 | 0.17 | 1.37 | 1577 |
| 2024-09-20 22:21:39.948 | MS1 | 121.4656751893 | 31.1446353556 | 766 | 504990 | -84.73 | 13.12 | 546.75 | 0.13 | 1.20 | 1573 |
| 2024-09-20 22:21:40.977 | MS1 | 121.4656725363 | 31.1446304569 | 766 | 504990 | -79.10 | 14.60 | 337.45 | 0.05 | 2.53 | 1586 |
| 2024-09-20 22:21:41.631 | MS1 | 121.4656712827 | 31.1446356552 | 766 | 504990 | -78.13 | 17.11 | 529.51 | 0.09 | 2.72 | 1569 |
| 2024-09-20 22:21:42.581 | MS1 | 121.4656607199 | 31.1446274739 | 766 | 504990 | -78.39 | 13.84 | 537.08 | 0.11 | 2.09 | 1563 |

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
| 3214906 | 3 | 121.4674064293 | 31.1473935678 | 55 | 9 | 11 | 44.7 | TDD | 766 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3227993 | 4 | 121.4684394867 | 31.1529969023 | 172 | 4 | 10 | 30.0 | TDD | 167 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3256508 | 1 | 121.4653540804 | 31.1449139764 | 67 | 4 | 10 | 47.0 | TDD | 200 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3270514 | 2 | 121.4675533800 | 31.1470647833 | 263 | 5 | 1 | 33.9 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.397 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.413 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.536 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.536 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.214 | NREventA3 | measId:2;ServCellPCI:737;Se... |
| 2024-09-20 22:21:36.214 | NREventA3 | measId:2;ServCellPCI:737;Se... |
| 2024-09-20 22:21:37.214 | NREventA3 | measId:2;ServCellPCI:737;Se... |
| 2024-09-20 22:21:39.714 | NRRRCReestablishAttempt | PCI:737 |
| 2024-09-20 22:21:39.728 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.740 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.869 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.869 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256508 | 1 | 19.9071 | 16.8558 | -114.6032 | 9.1780 | 120.3705 | 0.0132 | 0.0010 |
| 2024_09_20 22:00 | 3270514 | 2 | 10.8414 | 13.0895 | -115.7725 | 13.3683 | 95.7364 | 0.0161 | 0.0162 |
| 2024_09_20 22:00 | 3214906 | 3 | 11.2308 | 5.0791 | -116.4170 | 5.3819 | 132.0313 | 0.0158 | 0.1316 |
| 2024_09_20 22:00 | 3227993 | 4 | 15.9475 | 15.6439 | -115.9582 | 10.4525 | 175.1846 | 0.0178 | 0.0085 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415073_3908429E | 504990 | 766 | -96.8 | 504990 | 167 | -88.3 | 504990 | 200 | -100.1 | 504990 | 355 |
| MR_1774415073_68802914 | 504990 | 766 | -95.6 | 504990 | 167 | -89.1 | 504990 | 200 | -101.1 | 504990 | 355 |
| MR_1774415073_9946725B | 504990 | 167 | -91.3 | 504990 | 766 | -97.0 | 504990 | 200 | -100.8 | 504990 | 355 |
| MR_1774415073_82DDD661 | 504990 | 766 | -95.8 | 504990 | 167 | -91.5 | 504990 | 200 | -98.8 | 504990 | 355 |
| MR_1774415073_F976E0DD | 504990 | 766 | -94.5 | 504990 | 167 | -90.9 | 504990 | 200 | -99.3 | 504990 | 355 |
| MR_1774415073_EAD908D6 | 504990 | 766 | -94.7 | 504990 | 167 | -90.0 | 504990 | 200 | -100.6 | 504990 | 355 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1996: `4c0f4f75-161...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4c0f4f75-1612-49d5-bbf9-be6306707757` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Lift the tilt angle  of 3217598_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1996] topology](images/train_1996.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3273980_3
- `C2`: Adjust the azimuth of 3238525_2 by 45 degrees
- `C3`: Decrease A3 Offset threshold for 3273980_3
- `C4`: Decrease A3 Offset threshold for 3238525_2
- `C5`: Decrease transmission power for 3238525_2
- `C6`: Press down the tilt angle  of 3217598_1 by 10 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273980_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238525_2
- `C9`: Adjust the azimuth of 3217598_1 by 32 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238525_2
- `C11`: Lift the tilt angle of 3238525_2 by 4 degrees
- `C12`: Check test server and transmission issues
- `C13`: Increase transmission power for 3238525_2
- `C14`: Press down the tilt angle of 3238525_2 by 4 degrees
- `C15`: Increase A3 Offset threshold for 3238525_2
- `C16`: Increase transmission power for 3273980_3
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Lift the tilt angle  of 3217598_1 by 10 degrees **← 정답**
- `C19`: Add neighbor relationship between 3238525_2 and 3273980_3
- `C20`: Add neighbor relationship between 3217598_1 and 3273980_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273980_3
- `C22`: Decrease transmission power for 3273980_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.433 | MS1 | 121.4656671748 | 31.1446325934 | 749 | 504990 | -87.99 | 13.74 | 572.30 | 0.18 | 2.87 | 1560 |
| 2024-09-20 22:21:32.565 | MS1 | 121.4656663282 | 31.1446331684 | 749 | 504990 | -89.18 | 12.48 | 451.91 | 0.18 | 2.13 | 1577 |
| 2024-09-20 22:21:33.337 | MS1 | 121.4656736627 | 31.1446332155 | 749 | 504990 | -90.15 | 15.49 | 460.76 | 0.11 | 2.22 | 1560 |
| 2024-09-20 22:21:34.379 | MS1 | 121.4656752138 | 31.1446326818 | 749 | 504990 | -86.33 | 16.54 | 96.10 | 0.04 | 2.37 | 1591 |
| 2024-09-20 22:21:35.815 | MS1 | 121.4656626045 | 31.1446204319 | 749 | 504990 | -91.77 | 16.54 | 60.52 | 0.02 | 2.40 | 1578 |
| 2024-09-20 22:21:36.506 | MS1 | 121.4656661792 | 31.1446275200 | 749 | 504990 | -85.86 | 17.65 | 88.10 | 0.14 | 2.14 | 1573 |
| 2024-09-20 22:21:37.380 | MS1 | 121.4656635012 | 31.1446235962 | 749 | 504990 | -92.05 | 9.36 | 67.06 | 0.05 | 2.24 | 1567 |
| 2024-09-20 22:21:38.141 | MS1 | 121.4656739874 | 31.1446305058 | 749 | 504990 | -92.84 | 9.43 | 70.54 | 0.04 | 2.28 | 1578 |
| 2024-09-20 22:21:39.259 | MS1 | 121.4656689739 | 31.1446189059 | 749 | 504990 | -89.35 | 10.58 | 70.15 | 0.15 | 2.38 | 1563 |
| 2024-09-20 22:21:40.821 | MS1 | 121.4656731321 | 31.1446271769 | 749 | 504990 | -90.34 | 8.16 | 388.31 | 0.02 | 2.07 | 1590 |
| 2024-09-20 22:21:41.601 | MS1 | 121.4656710221 | 31.1446372388 | 749 | 504990 | -91.13 | 7.28 | 306.45 | 0.12 | 2.89 | 1593 |
| 2024-09-20 22:21:42.383 | MS1 | 121.4656747002 | 31.1446339934 | 749 | 504990 | -90.90 | 11.02 | 345.09 | 0.03 | 2.78 | 1585 |

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
| 3217598 | 1 | 121.4703351103 | 31.1516321088 | 295 | 14 | 12 | 38.5 | TDD | 968 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3221691 | 4 | 121.4640429218 | 31.1495322299 | 164 | 0 | 3 | 44.1 | TDD | 885 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3238525 | 2 | 121.4663982730 | 31.1528019890 | 139 | 3 | 6 | 23.2 | TDD | 749 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3273980 | 3 | 121.4690767528 | 31.1493072850 | 244 | 10 | 2 | 48.8 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.876 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.891 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.032 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.032 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.698 | NREventA3 | measId:2;ServCellPCI:679;Se... |
| 2024-09-20 22:21:37.938 | NRHandoverAttempt | SourcePCI:679;SourceNR-ARFC... |
| 2024-09-20 22:21:37.988 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.999 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.106 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.106 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217598 | 1 | 15.0315 | 11.7766 | -117.3581 | 12.5072 | 95.0783 | 0.0072 | 0.0081 |
| 2024_09_20 22:00 | 3238525 | 2 | 88.2686 | 75.8700 | -117.4737 | 15.1799 | 158.5881 | 0.0018 | 0.0177 |
| 2024_09_20 22:00 | 3273980 | 3 | 6.9740 | 14.6085 | -114.8109 | 10.7537 | 166.5464 | 0.0022 | 0.0112 |
| 2024_09_20 22:00 | 3221691 | 4 | 15.2674 | 11.0349 | -116.7330 | 12.6978 | 166.1309 | 0.0007 | 0.0073 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412664_9C16BD98 | 504990 | 749 | -86.2 | 504990 | 355 | -91.5 | 504990 | 968 | -102.1 | 504990 | 885 |
| MR_1774412664_3CBD3426 | 504990 | 749 | -85.0 | 504990 | 355 | -91.8 | 504990 | 968 | -100.1 | 504990 | 885 |
| MR_1774412664_041BDD1E | 504990 | 749 | -85.8 | 504990 | 355 | -88.3 | 504990 | 968 | -101.0 | 504990 | 885 |
| MR_1774412664_1CE3C163 | 504990 | 749 | -85.1 | 504990 | 355 | -91.6 | 504990 | 968 | -101.5 | 504990 | 885 |
| MR_1774412664_D97500D1 | 504990 | 749 | -87.8 | 504990 | 355 | -89.8 | 504990 | 968 | -101.9 | 504990 | 885 |
| MR_1774412664_9EFBF433 | 504990 | 749 | -84.3 | 504990 | 355 | -91.9 | 504990 | 968 | -101.2 | 504990 | 885 |
| MR_1774412664_1E5E13B1 | 504990 | 749 | -86.9 | 504990 | 355 | -88.9 | 504990 | 968 | -100.3 | 504990 | 885 |
| MR_1774412664_FDC0A378 | 504990 | 749 | -86.7 | 504990 | 355 | -88.8 | 504990 | 968 | -99.7 | 504990 | 885 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1997: `7b3003fb-9bf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7b3003fb-9bf3-41b7-9eeb-306aa46d8726` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3238999_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1997] topology](images/train_1997.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236210_3
- `C2`: Add neighbor relationship between 3219821_2 and 3236210_3
- `C3`: Decrease transmission power for 3236210_3
- `C4`: Decrease transmission power for 3238999_1
- `C5`: Check test server and transmission issues
- `C6`: Lift the tilt angle of 3238999_1 by 2 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236210_3
- `C8`: Adjust the azimuth of 3238999_1 by 9 degrees
- `C9`: Increase A3 Offset threshold for 3238999_1
- `C10`: Adjust the azimuth of 3236210_3 by 50 degrees
- `C11`: Increase transmission power for 3236210_3
- `C12`: Press down the tilt angle  of 3236210_3 by 10 degrees
- `C13`: Press down the tilt angle of 3238999_1 by 2 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease A3 Offset threshold for 3238999_1
- `C16`: Add neighbor relationship between 3238999_1 and 3236210_3
- `C17`: Increase A3 Offset threshold for 3236210_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238999_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238999_1 **← 정답**
- `C20`: Increase transmission power for 3238999_1
- `C21`: Decrease A3 Offset threshold for 3236210_3
- `C22`: Lift the tilt angle  of 3236210_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.773 | MS1 | 121.4656715703 | 31.1446359178 | 305 | 504990 | -88.74 | 13.82 | 510.92 | 0.15 | 2.15 | 1577 |
| 2024-09-20 22:21:32.325 | MS1 | 121.4656749158 | 31.1446291545 | 305 | 504990 | -88.93 | 13.90 | 311.57 | 0.02 | 2.86 | 1592 |
| 2024-09-20 22:21:33.503 | MS1 | 121.4656670536 | 31.1446190895 | 305 | 504990 | -87.97 | 16.30 | 367.55 | 0.18 | 2.19 | 1561 |
| 2024-09-20 22:21:34.747 | MS1 | 121.4656605536 | 31.1446284268 | 305 | 504990 | -89.17 | 14.52 | 47.15 | 0.56 | 2.05 | 677 |
| 2024-09-20 22:21:35.360 | MS1 | 121.4656662295 | 31.1446321051 | 305 | 504990 | -91.37 | 14.86 | 70.95 | 0.62 | 2.02 | 502 |
| 2024-09-20 22:21:36.730 | MS1 | 121.4656639287 | 31.1446355538 | 305 | 504990 | -86.38 | 14.72 | 78.97 | 0.58 | 2.23 | 510 |
| 2024-09-20 22:21:37.775 | MS1 | 121.4656695914 | 31.1446371751 | 305 | 504990 | -89.21 | 8.56 | 82.82 | 0.63 | 2.05 | 588 |
| 2024-09-20 22:21:38.241 | MS1 | 121.4656741194 | 31.1446344909 | 305 | 504990 | -89.96 | 8.55 | 59.62 | 0.52 | 2.10 | 521 |
| 2024-09-20 22:21:39.239 | MS1 | 121.4656610851 | 31.1446275537 | 305 | 504990 | -91.94 | 12.51 | 58.44 | 0.56 | 2.68 | 657 |
| 2024-09-20 22:21:40.616 | MS1 | 121.4656692687 | 31.1446231072 | 305 | 504990 | -89.12 | 11.15 | 583.71 | 0.04 | 2.30 | 1577 |
| 2024-09-20 22:21:41.179 | MS1 | 121.4656613779 | 31.1446373353 | 305 | 504990 | -93.14 | 11.43 | 379.68 | 0.07 | 2.82 | 1588 |
| 2024-09-20 22:21:42.215 | MS1 | 121.4656668336 | 31.1446233710 | 305 | 504990 | -92.20 | 11.33 | 553.12 | 0.03 | 2.41 | 1600 |

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
| 3219821 | 2 | 121.4697375019 | 31.1470351836 | 121 | 7 | 1 | 22.1 | TDD | 641 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3236210 | 3 | 121.4648803491 | 31.1475880219 | 330 | 5 | 0 | 49.8 | TDD | 492 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3238999 | 1 | 121.4720794726 | 31.1520987247 | 207 | 0 | 7 | 36.6 | TDD | 305 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3246447 | 4 | 121.4663318968 | 31.1452747729 | 347 | 9 | 2 | 17.1 | TDD | 362 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.028 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.154 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.154 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.845 | NREventA3 | measId:2;ServCellPCI:456;Se... |
| 2024-09-20 22:21:38.085 | NRHandoverAttempt | SourcePCI:456;SourceNR-ARFC... |
| 2024-09-20 22:21:38.125 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.139 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.257 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.257 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238999 | 1 | 17.6320 | 17.5360 | -114.9890 | 16.6474 | 196.5180 | 0.0005 | 0.0080 |
| 2024_09_20 22:00 | 3219821 | 2 | 13.5379 | 16.0849 | -117.3068 | 13.0204 | 140.7359 | 0.0100 | 0.0069 |
| 2024_09_20 22:00 | 3236210 | 3 | 10.0626 | 7.4817 | -117.6817 | 14.5427 | 187.1538 | 0.0126 | 0.0098 |
| 2024_09_20 22:00 | 3246447 | 4 | 6.9549 | 10.0783 | -116.9779 | 10.7079 | 160.9626 | 0.0160 | 0.0096 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416402_5B36F128 | 504990 | 305 | -87.4 | 504990 | 492 | -90.2 | 504990 | 641 | -98.4 | 504990 | 362 |
| MR_1774416402_796A9982 | 504990 | 305 | -89.0 | 504990 | 492 | -90.9 | 504990 | 641 | -96.2 | 504990 | 362 |
| MR_1774416402_1C3530CB | 504990 | 305 | -90.5 | 504990 | 492 | -89.0 | 504990 | 641 | -97.4 | 504990 | 362 |
| MR_1774416402_C23CF046 | 504990 | 305 | -88.1 | 504990 | 492 | -90.1 | 504990 | 641 | -96.9 | 504990 | 362 |
| MR_1774416402_CA24EB7C | 504990 | 305 | -88.5 | 504990 | 492 | -91.1 | 504990 | 641 | -99.8 | 504990 | 362 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1998: `bbbf0187-a42...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bbbf0187-a422-40c0-83b9-93e232cfb17f` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Lift the tilt angle  of 3211044_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1998] topology](images/train_1998.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264819_3
- `C2`: Decrease transmission power for 3238922_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238922_2
- `C4`: Decrease A3 Offset threshold for 3264819_3
- `C5`: Adjust the azimuth of 3211044_4 by 50 degrees
- `C6`: Adjust the azimuth of 3238922_2 by 48 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Increase transmission power for 3238922_2
- `C9`: Press down the tilt angle  of 3211044_4 by 10 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238922_2
- `C11`: Check test server and transmission issues
- `C12`: Press down the tilt angle of 3238922_2 by 6 degrees
- `C13`: Decrease transmission power for 3264819_3
- `C14`: Increase A3 Offset threshold for 3264819_3
- `C15`: Increase transmission power for 3264819_3
- `C16`: Add neighbor relationship between 3238922_2 and 3264819_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264819_3
- `C18`: Add neighbor relationship between 3211044_4 and 3264819_3
- `C19`: Increase A3 Offset threshold for 3238922_2
- `C20`: Decrease A3 Offset threshold for 3238922_2
- `C21`: Lift the tilt angle  of 3211044_4 by 10 degrees **← 정답**
- `C22`: Lift the tilt angle of 3238922_2 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.955 | MS1 | 121.4656700722 | 31.1446373198 | 667 | 504990 | -85.01 | 16.80 | 310.74 | 0.07 | 2.15 | 1598 |
| 2024-09-20 22:21:32.811 | MS1 | 121.4656765231 | 31.1446369392 | 667 | 504990 | -87.79 | 12.37 | 505.88 | 0.08 | 2.71 | 1582 |
| 2024-09-20 22:21:33.462 | MS1 | 121.4656587520 | 31.1446323790 | 667 | 504990 | -91.21 | 14.00 | 552.20 | 0.06 | 2.95 | 1598 |
| 2024-09-20 22:21:34.762 | MS1 | 121.4656688306 | 31.1446324243 | 667 | 504990 | -89.11 | 12.66 | 83.58 | 0.11 | 2.17 | 1569 |
| 2024-09-20 22:21:35.975 | MS1 | 121.4656656558 | 31.1446302738 | 667 | 504990 | -90.80 | 16.94 | 68.02 | 0.15 | 2.66 | 1565 |
| 2024-09-20 22:21:36.991 | MS1 | 121.4656672101 | 31.1446355659 | 667 | 504990 | -85.62 | 15.30 | 86.01 | 0.19 | 2.32 | 1561 |
| 2024-09-20 22:21:37.509 | MS1 | 121.4656702662 | 31.1446237722 | 667 | 504990 | -90.35 | 10.28 | 75.40 | 0.02 | 2.04 | 1579 |
| 2024-09-20 22:21:38.526 | MS1 | 121.4656765192 | 31.1446328351 | 667 | 504990 | -92.57 | 7.70 | 56.83 | 0.14 | 2.96 | 1587 |
| 2024-09-20 22:21:39.652 | MS1 | 121.4656759905 | 31.1446326144 | 667 | 504990 | -93.04 | 8.00 | 71.32 | 0.13 | 2.84 | 1565 |
| 2024-09-20 22:21:40.332 | MS1 | 121.4656605384 | 31.1446358897 | 667 | 504990 | -92.96 | 12.19 | 567.69 | 0.01 | 2.21 | 1583 |
| 2024-09-20 22:21:41.647 | MS1 | 121.4656741383 | 31.1446200011 | 667 | 504990 | -91.53 | 10.67 | 504.54 | 0.18 | 2.18 | 1561 |
| 2024-09-20 22:21:42.380 | MS1 | 121.4656755099 | 31.1446256690 | 667 | 504990 | -90.50 | 9.38 | 514.53 | 0.20 | 2.10 | 1589 |

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
| 3211044 | 4 | 121.4653125467 | 31.1484828424 | 67 | 12 | 3 | 34.7 | TDD | 957 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3238922 | 2 | 121.4733362706 | 31.1441244232 | 226 | 4 | 11 | 20.1 | TDD | 667 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3243799 | 1 | 121.4703999785 | 31.1542833055 | 328 | 10 | 8 | 37.4 | TDD | 754 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3264819 | 3 | 121.4641913758 | 31.1441731943 | 171 | 6 | 2 | 39.7 | TDD | 780 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.006 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.022 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.136 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.136 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.893 | NREventA3 | measId:2;ServCellPCI:43;Ser... |
| 2024-09-20 22:21:38.133 | NRHandoverAttempt | SourcePCI:43;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.173 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.187 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.320 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.320 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243799 | 1 | 10.7809 | 9.3927 | -116.4952 | 9.6556 | 99.0574 | 0.0035 | 0.0066 |
| 2024_09_20 22:00 | 3238922 | 2 | 90.1668 | 86.7207 | -114.6378 | 10.8043 | 106.0863 | 0.0148 | 0.0019 |
| 2024_09_20 22:00 | 3264819 | 3 | 6.0884 | 8.8500 | -117.4280 | 18.7180 | 166.6542 | 0.0052 | 0.0167 |
| 2024_09_20 22:00 | 3211044 | 4 | 9.4868 | 11.2235 | -116.4300 | 9.8214 | 183.4271 | 0.0140 | 0.0084 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413372_39D26F0A | 504990 | 667 | -89.2 | 504990 | 780 | -96.3 | 504990 | 957 | -101.2 | 504990 | 754 |
| MR_1774413372_799EF56E | 504990 | 667 | -89.7 | 504990 | 780 | -98.9 | 504990 | 957 | -98.2 | 504990 | 754 |
| MR_1774413372_C1B05C2E | 504990 | 667 | -89.1 | 504990 | 780 | -98.6 | 504990 | 957 | -101.5 | 504990 | 754 |
| MR_1774413372_00FF3C39 | 504990 | 667 | -88.1 | 504990 | 780 | -97.4 | 504990 | 957 | -98.8 | 504990 | 754 |
| MR_1774413372_8CFE3BB7 | 504990 | 667 | -87.6 | 504990 | 780 | -97.8 | 504990 | 957 | -99.0 | 504990 | 754 |
| MR_1774413372_1CB36A65 | 504990 | 667 | -89.2 | 504990 | 780 | -94.9 | 504990 | 957 | -99.4 | 504990 | 754 |
| MR_1774413372_752B17EB | 504990 | 667 | -89.9 | 504990 | 780 | -95.9 | 504990 | 957 | -101.3 | 504990 | 754 |
| MR_1774413372_9B610756 | 504990 | 667 | -89.3 | 504990 | 780 | -98.4 | 504990 | 957 | -100.5 | 504990 | 754 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1999: `6a686272-80c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6a686272-80c5-4a77-ba51-192998460176` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Lift the tilt angle  of 3268575_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1999] topology](images/train_1999.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3230521_4
- `C2`: Increase transmission power for 3230521_4
- `C3`: Adjust the azimuth of 3266352_3 by 3 degrees
- `C4`: Decrease A3 Offset threshold for 3266352_3
- `C5`: Lift the tilt angle of 3266352_3 by 3 degrees
- `C6`: Add neighbor relationship between 3268575_2 and 3230521_4
- `C7`: Add neighbor relationship between 3266352_3 and 3230521_4
- `C8`: Lift the tilt angle  of 3268575_2 by 10 degrees **← 정답**
- `C9`: Press down the tilt angle  of 3268575_2 by 10 degrees
- `C10`: Decrease transmission power for 3266352_3
- `C11`: Adjust the azimuth of 3268575_2 by 50 degrees
- `C12`: Decrease A3 Offset threshold for 3230521_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266352_3
- `C14`: Increase transmission power for 3266352_3
- `C15`: Increase A3 Offset threshold for 3266352_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266352_3
- `C17`: Press down the tilt angle of 3266352_3 by 3 degrees
- `C18`: Increase A3 Offset threshold for 3230521_4
- `C19`: Check test server and transmission issues
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230521_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230521_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.375 | MS1 | 121.4656727451 | 31.1446292677 | 166 | 504990 | -91.67 | 14.01 | 517.04 | 0.02 | 2.60 | 1566 |
| 2024-09-20 22:21:32.639 | MS1 | 121.4656633462 | 31.1446208884 | 166 | 504990 | -91.91 | 17.67 | 340.67 | 0.16 | 2.90 | 1563 |
| 2024-09-20 22:21:33.195 | MS1 | 121.4656636048 | 31.1446284289 | 166 | 504990 | -89.77 | 13.91 | 365.12 | 0.18 | 2.76 | 1568 |
| 2024-09-20 22:21:34.238 | MS1 | 121.4656687924 | 31.1446363464 | 166 | 504990 | -89.19 | 17.84 | 96.10 | 0.14 | 2.39 | 1598 |
| 2024-09-20 22:21:35.862 | MS1 | 121.4656665561 | 31.1446328313 | 166 | 504990 | -89.70 | 13.46 | 78.72 | 0.10 | 2.45 | 1569 |
| 2024-09-20 22:21:36.195 | MS1 | 121.4656744915 | 31.1446365318 | 166 | 504990 | -85.35 | 13.99 | 73.23 | 0.14 | 2.13 | 1586 |
| 2024-09-20 22:21:37.295 | MS1 | 121.4656716466 | 31.1446183796 | 166 | 504990 | -89.79 | 7.42 | 91.05 | 0.14 | 2.02 | 1585 |
| 2024-09-20 22:21:38.502 | MS1 | 121.4656653751 | 31.1446335497 | 166 | 504990 | -90.83 | 10.21 | 96.48 | 0.00 | 2.71 | 1592 |
| 2024-09-20 22:21:39.833 | MS1 | 121.4656737031 | 31.1446225162 | 166 | 504990 | -93.02 | 8.63 | 57.70 | 0.12 | 2.80 | 1588 |
| 2024-09-20 22:21:40.999 | MS1 | 121.4656741774 | 31.1446375049 | 166 | 504990 | -92.84 | 7.22 | 453.38 | 0.13 | 2.91 | 1576 |
| 2024-09-20 22:21:41.950 | MS1 | 121.4656608403 | 31.1446349539 | 166 | 504990 | -93.33 | 9.86 | 567.32 | 0.02 | 2.88 | 1575 |
| 2024-09-20 22:21:42.912 | MS1 | 121.4656745914 | 31.1446278462 | 166 | 504990 | -92.23 | 9.42 | 498.48 | 0.01 | 2.96 | 1571 |

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
| 3225664 | 1 | 121.4699314939 | 31.1502192989 | 90 | 4 | 5 | 29.2 | TDD | 145 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3230521 | 4 | 121.4735769357 | 31.1499205399 | 10 | 15 | 8 | 20.7 | TDD | 475 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3266352 | 3 | 121.4752694974 | 31.1479431098 | 251 | 1 | 5 | 35.1 | TDD | 166 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3268575 | 2 | 121.4669896902 | 31.1450480551 | 350 | 0 | 6 | 38.7 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.307 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.326 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.426 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.426 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.122 | NREventA3 | measId:2;ServCellPCI:925;Se... |
| 2024-09-20 22:21:38.362 | NRHandoverAttempt | SourcePCI:925;SourceNR-ARFC... |
| 2024-09-20 22:21:38.392 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.403 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.527 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.527 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225664 | 1 | 14.6465 | 5.2883 | -117.3151 | 19.9091 | 198.7354 | 0.0049 | 0.0117 |
| 2024_09_20 22:00 | 3268575 | 2 | 6.0679 | 9.0387 | -114.3241 | 8.5480 | 187.1303 | 0.0078 | 0.0110 |
| 2024_09_20 22:00 | 3266352 | 3 | 77.0144 | 85.7644 | -117.5209 | 10.7015 | 119.1682 | 0.0164 | 0.0115 |
| 2024_09_20 22:00 | 3230521 | 4 | 17.6846 | 14.4977 | -117.3529 | 17.0522 | 87.7466 | 0.0081 | 0.0186 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415830_CE9F41F2 | 504990 | 166 | -89.7 | 504990 | 475 | -89.6 | 504990 | 355 | -101.5 | 504990 | 145 |
| MR_1774415830_2215EC7F | 504990 | 166 | -88.2 | 504990 | 475 | -91.4 | 504990 | 355 | -101.3 | 504990 | 145 |
| MR_1774415830_4EF1A25E | 504990 | 166 | -87.2 | 504990 | 475 | -89.9 | 504990 | 355 | -102.1 | 504990 | 145 |
| MR_1774415830_0488B9CC | 504990 | 166 | -89.3 | 504990 | 475 | -91.1 | 504990 | 355 | -99.1 | 504990 | 145 |
| MR_1774415830_034B36E6 | 504990 | 166 | -89.0 | 504990 | 475 | -92.4 | 504990 | 355 | -100.9 | 504990 | 145 |
| MR_1774415830_B595901D | 504990 | 166 | -89.4 | 504990 | 475 | -90.5 | 504990 | 355 | -102.8 | 504990 | 145 |
| MR_1774415830_41AEA3EA | 504990 | 166 | -89.6 | 504990 | 475 | -91.1 | 504990 | 355 | -101.9 | 504990 | 145 |

> *... 2개 열 생략 (전체 14열)*

---
