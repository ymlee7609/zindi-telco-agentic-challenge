# Track A 문제 분석 — train[1940]~train[1949]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1940] ~ train[1949] (10개)

## 목차

1. [문제 1940: `381417e1-e71...`](#1940) — single-answer, 정답: C19
2. [문제 1941: `22083de8-a0e...`](#1941) — single-answer, 정답: C19
3. [문제 1942: `5281e18b-5d7...`](#1942) — single-answer, 정답: C19
4. [문제 1943: `7c19866a-9e6...`](#1943) — multiple-answer, 정답: C1|C6|C14|C18
5. [문제 1944: `b546f48a-64e...`](#1944) — multiple-answer, 정답: C16|C20
6. [문제 1945: `f36c997d-9c4...`](#1945) — multiple-answer, 정답: C11|C14|C16|C21
7. [문제 1946: `fb1cc9b5-ac1...`](#1946) — single-answer, 정답: C3
8. [문제 1947: `979a12c3-59b...`](#1947) — single-answer, 정답: C18
9. [문제 1948: `200b8d7c-914...`](#1948) — single-answer, 정답: C13
10. [문제 1949: `9d931a42-ee1...`](#1949) — single-answer, 정답: C11

---

### 문제 1940: `381417e1-e71...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `381417e1-e717-4fc3-b619-b140af21ad53` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3263894_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1940] topology](images/train_1940.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263894_3
- `C3`: Increase A3 Offset threshold for 3263894_3
- `C4`: Increase A3 Offset threshold for 3212398_2
- `C5`: Decrease transmission power for 3212398_2
- `C6`: Decrease transmission power for 3263894_3
- `C7`: Lift the tilt angle  of 3212398_2 by 10 degrees
- `C8`: Add neighbor relationship between 3278379_4 and 3212398_2
- `C9`: Adjust the azimuth of 3263894_3 by 38 degrees
- `C10`: Check test server and transmission issues
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212398_2
- `C12`: Lift the tilt angle of 3263894_3 by 5 degrees
- `C13`: Adjust the azimuth of 3212398_2 by 50 degrees
- `C14`: Press down the tilt angle of 3263894_3 by 5 degrees
- `C15`: Press down the tilt angle  of 3212398_2 by 10 degrees
- `C16`: Decrease A3 Offset threshold for 3212398_2
- `C17`: Decrease A3 Offset threshold for 3263894_3
- `C18`: Increase transmission power for 3263894_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263894_3 **← 정답**
- `C20`: Increase transmission power for 3212398_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212398_2
- `C22`: Add neighbor relationship between 3263894_3 and 3212398_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.865 | MS1 | 121.4656720122 | 31.1446196551 | 700 | 504990 | -89.66 | 13.66 | 393.43 | 0.03 | 2.79 | 1588 |
| 2024-09-20 22:21:32.106 | MS1 | 121.4656668728 | 31.1446374990 | 700 | 504990 | -87.48 | 13.30 | 560.43 | 0.13 | 2.10 | 1588 |
| 2024-09-20 22:21:33.256 | MS1 | 121.4656613351 | 31.1446191254 | 700 | 504990 | -86.03 | 14.06 | 361.86 | 0.04 | 2.88 | 1573 |
| 2024-09-20 22:21:34.571 | MS1 | 121.4656733535 | 31.1446368431 | 700 | 504990 | -89.93 | 15.50 | 79.53 | 0.65 | 2.45 | 666 |
| 2024-09-20 22:21:35.783 | MS1 | 121.4656751170 | 31.1446372437 | 700 | 504990 | -85.12 | 15.39 | 88.46 | 0.62 | 2.20 | 673 |
| 2024-09-20 22:21:36.653 | MS1 | 121.4656642301 | 31.1446366606 | 700 | 504990 | -87.04 | 17.18 | 85.78 | 0.62 | 2.46 | 664 |
| 2024-09-20 22:21:37.990 | MS1 | 121.4656597684 | 31.1446207081 | 700 | 504990 | -91.10 | 10.03 | 68.45 | 0.57 | 2.75 | 500 |
| 2024-09-20 22:21:38.351 | MS1 | 121.4656682853 | 31.1446342889 | 700 | 504990 | -90.01 | 9.03 | 60.96 | 0.70 | 2.82 | 558 |
| 2024-09-20 22:21:39.430 | MS1 | 121.4656771768 | 31.1446294430 | 700 | 504990 | -89.48 | 11.11 | 87.15 | 0.70 | 2.04 | 622 |
| 2024-09-20 22:21:40.374 | MS1 | 121.4656649720 | 31.1446377027 | 700 | 504990 | -93.58 | 12.27 | 535.27 | 0.12 | 2.38 | 1596 |
| 2024-09-20 22:21:41.953 | MS1 | 121.4656762901 | 31.1446268636 | 700 | 504990 | -92.23 | 12.42 | 377.95 | 0.06 | 2.31 | 1597 |
| 2024-09-20 22:21:42.218 | MS1 | 121.4656589682 | 31.1446349033 | 700 | 504990 | -89.13 | 7.39 | 595.60 | 0.02 | 2.97 | 1595 |

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
| 3212398 | 2 | 121.4703996300 | 31.1534524480 | 19 | 8 | 8 | 35.7 | TDD | 827 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3230148 | 1 | 121.4703520635 | 31.1446951874 | 236 | 2 | 1 | 39.8 | TDD | 792 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3263894 | 3 | 121.4747161290 | 31.1531107050 | 184 | 4 | 1 | 17.9 | TDD | 700 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3278379 | 4 | 121.4740993304 | 31.1520561611 | 122 | 7 | 9 | 39.1 | TDD | 415 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.347 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.370 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.477 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.477 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.233 | NREventA3 | measId:2;ServCellPCI:58;Ser... |
| 2024-09-20 22:21:38.473 | NRHandoverAttempt | SourcePCI:58;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.510 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.524 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.673 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.673 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230148 | 1 | 19.0184 | 5.7892 | -115.1616 | 9.1853 | 94.9960 | 0.0106 | 0.0154 |
| 2024_09_20 22:00 | 3212398 | 2 | 5.9860 | 13.5013 | -115.9060 | 7.3359 | 183.2364 | 0.0163 | 0.0029 |
| 2024_09_20 22:00 | 3263894 | 3 | 17.6230 | 8.2175 | -116.9112 | 8.2001 | 104.7697 | 0.0194 | 0.0171 |
| 2024_09_20 22:00 | 3278379 | 4 | 16.8472 | 10.1991 | -114.2245 | 15.0718 | 141.1540 | 0.0170 | 0.0046 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415295_6C8B9031 | 504990 | 700 | -89.7 | 504990 | 827 | -94.7 | 504990 | 415 | -99.0 | 504990 | 792 |
| MR_1774415295_41BE453E | 504990 | 700 | -89.3 | 504990 | 827 | -93.2 | 504990 | 415 | -100.9 | 504990 | 792 |
| MR_1774415295_C2911F29 | 504990 | 700 | -88.3 | 504990 | 827 | -94.0 | 504990 | 415 | -100.6 | 504990 | 792 |
| MR_1774415295_E48A1F73 | 504990 | 700 | -89.9 | 504990 | 827 | -93.7 | 504990 | 415 | -97.6 | 504990 | 792 |
| MR_1774415295_AA49FBD1 | 504990 | 700 | -90.2 | 504990 | 827 | -92.1 | 504990 | 415 | -99.3 | 504990 | 792 |
| MR_1774415295_1E3316F2 | 504990 | 700 | -89.5 | 504990 | 827 | -92.9 | 504990 | 415 | -100.4 | 504990 | 792 |
| MR_1774415295_AF12E256 | 504990 | 700 | -91.5 | 504990 | 827 | -92.2 | 504990 | 415 | -100.3 | 504990 | 792 |
| MR_1774415295_DEBCBC9F | 504990 | 700 | -88.7 | 504990 | 827 | -91.6 | 504990 | 415 | -101.0 | 504990 | 792 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1941: `22083de8-a0e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `22083de8-a0e0-4491-b92d-5af3d53e1e9c` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3266832_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1941] topology](images/train_1941.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255354_1
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Adjust the azimuth of 3266832_2 by 45 degrees
- `C4`: Adjust the azimuth of 3255354_1 by 50 degrees
- `C5`: Lift the tilt angle  of 3255354_1 by 10 degrees
- `C6`: Add neighbor relationship between 3252732_4 and 3255354_1
- `C7`: Press down the tilt angle  of 3255354_1 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3266832_2
- `C9`: Decrease transmission power for 3266832_2
- `C10`: Lift the tilt angle of 3266832_2 by 3 degrees
- `C11`: Increase transmission power for 3266832_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266832_2
- `C13`: Check test server and transmission issues
- `C14`: Add neighbor relationship between 3266832_2 and 3255354_1
- `C15`: Decrease A3 Offset threshold for 3255354_1
- `C16`: Decrease transmission power for 3255354_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255354_1
- `C18`: Increase A3 Offset threshold for 3266832_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266832_2 **← 정답**
- `C20`: Increase A3 Offset threshold for 3255354_1
- `C21`: Increase transmission power for 3255354_1
- `C22`: Press down the tilt angle of 3266832_2 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.489 | MS1 | 121.4656692648 | 31.1446250525 | 668 | 504990 | -86.47 | 13.67 | 299.76 | 0.12 | 2.55 | 1581 |
| 2024-09-20 22:21:32.672 | MS1 | 121.4656759738 | 31.1446224046 | 668 | 504990 | -85.58 | 12.72 | 516.38 | 0.02 | 2.84 | 1579 |
| 2024-09-20 22:21:33.784 | MS1 | 121.4656652035 | 31.1446296432 | 668 | 504990 | -90.95 | 14.39 | 453.32 | 0.16 | 2.74 | 1574 |
| 2024-09-20 22:21:34.341 | MS1 | 121.4656711226 | 31.1446354426 | 668 | 504990 | -90.76 | 15.32 | 97.14 | 0.58 | 2.05 | 691 |
| 2024-09-20 22:21:35.544 | MS1 | 121.4656604410 | 31.1446196122 | 668 | 504990 | -87.47 | 12.87 | 58.04 | 0.60 | 2.64 | 538 |
| 2024-09-20 22:21:36.823 | MS1 | 121.4656767962 | 31.1446324127 | 668 | 504990 | -85.33 | 14.77 | 94.27 | 0.64 | 2.77 | 518 |
| 2024-09-20 22:21:37.555 | MS1 | 121.4656613266 | 31.1446379342 | 668 | 504990 | -90.52 | 10.92 | 73.70 | 0.56 | 2.83 | 664 |
| 2024-09-20 22:21:38.221 | MS1 | 121.4656731815 | 31.1446194529 | 668 | 504990 | -90.05 | 7.88 | 73.79 | 0.51 | 2.03 | 538 |
| 2024-09-20 22:21:39.612 | MS1 | 121.4656597858 | 31.1446296239 | 668 | 504990 | -89.39 | 8.17 | 50.37 | 0.53 | 2.70 | 512 |
| 2024-09-20 22:21:40.636 | MS1 | 121.4656673438 | 31.1446296784 | 668 | 504990 | -89.64 | 11.30 | 408.33 | 0.00 | 2.96 | 1584 |
| 2024-09-20 22:21:41.499 | MS1 | 121.4656619488 | 31.1446196934 | 668 | 504990 | -91.08 | 9.67 | 504.49 | 0.14 | 2.42 | 1565 |
| 2024-09-20 22:21:42.612 | MS1 | 121.4656659134 | 31.1446215059 | 668 | 504990 | -92.13 | 12.60 | 594.90 | 0.16 | 2.29 | 1582 |

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
| 3252732 | 4 | 121.4683632827 | 31.1457534201 | 278 | 5 | 3 | 45.6 | TDD | 398 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3255354 | 1 | 121.4702537654 | 31.1501486929 | 82 | 14 | 8 | 28.3 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3266832 | 2 | 121.4710668664 | 31.1544350288 | 250 | 2 | 10 | 26.5 | TDD | 668 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3279628 | 3 | 121.4680741453 | 31.1475294818 | 253 | 11 | 5 | 37.3 | TDD | 58 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.186 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.210 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.351 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.351 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.066 | NREventA3 | measId:2;ServCellPCI:263;Se... |
| 2024-09-20 22:21:38.306 | NRHandoverAttempt | SourcePCI:263;SourceNR-ARFC... |
| 2024-09-20 22:21:38.347 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.359 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.467 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.467 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255354 | 1 | 19.7308 | 5.7688 | -116.5761 | 12.3044 | 123.1394 | 0.0101 | 0.0026 |
| 2024_09_20 22:00 | 3266832 | 2 | 15.6102 | 14.2319 | -117.1540 | 10.1685 | 198.8833 | 0.0092 | 0.0144 |
| 2024_09_20 22:00 | 3279628 | 3 | 6.6322 | 10.3704 | -114.3210 | 18.4545 | 126.3776 | 0.0051 | 0.0013 |
| 2024_09_20 22:00 | 3252732 | 4 | 14.4022 | 12.4817 | -115.3967 | 17.5766 | 150.6532 | 0.0080 | 0.0016 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414512_8417F67A | 504990 | 668 | -92.7 | 504990 | 258 | -99.0 | 504990 | 398 | -99.8 | 504990 | 58 |
| MR_1774414512_00EE48B3 | 504990 | 668 | -89.7 | 504990 | 258 | -97.1 | 504990 | 398 | -99.4 | 504990 | 58 |
| MR_1774414512_6532D8C3 | 504990 | 668 | -91.4 | 504990 | 258 | -96.2 | 504990 | 398 | -99.4 | 504990 | 58 |
| MR_1774414512_DBF0FEC7 | 504990 | 668 | -91.5 | 504990 | 258 | -96.7 | 504990 | 398 | -101.1 | 504990 | 58 |
| MR_1774414512_F5288B99 | 504990 | 668 | -92.1 | 504990 | 258 | -96.9 | 504990 | 398 | -100.9 | 504990 | 58 |
| MR_1774414512_32D33755 | 504990 | 668 | -92.4 | 504990 | 258 | -97.8 | 504990 | 398 | -98.4 | 504990 | 58 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1942: `5281e18b-5d7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5281e18b-5d7b-4e6c-8d5a-d96fb054a8f5` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216855_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1942] topology](images/train_1942.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3216855_5
- `C2`: Increase transmission power for 3216855_5
- `C3`: Lift the tilt angle of 3216855_5 by 3 degrees
- `C4`: Lift the tilt angle  of 3213586_1 by 2 degrees
- `C5`: Check test server and transmission issues
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213586_1
- `C7`: Decrease A3 Offset threshold for 3213586_1
- `C8`: Add neighbor relationship between 3216855_5 and 3213586_1
- `C9`: Press down the tilt angle of 3216855_5 by 3 degrees
- `C10`: Decrease transmission power for 3213586_1
- `C11`: Increase A3 Offset threshold for 3213586_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213586_1
- `C13`: Adjust the azimuth of 3216855_5 by 49 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Add neighbor relationship between 3242929_13 and 3213586_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216855_5
- `C17`: Decrease transmission power for 3216855_5
- `C18`: Decrease A3 Offset threshold for 3216855_5
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216855_5 **← 정답**
- `C20`: Adjust the azimuth of 3213586_1 by 29 degrees
- `C21`: Increase transmission power for 3213586_1
- `C22`: Press down the tilt angle  of 3213586_1 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.747 | MS1 | 121.4656586706 | 31.1446181028 | 50 | 504990 | -93.21 | 10.49 | 395.34 | 0.12 | 2.30 | 1600 |
| 2024-09-20 22:21:32.937 | MS1 | 121.4656709202 | 31.1446325895 | 903 | 504990 | -93.27 | 13.65 | 486.80 | 0.14 | 2.45 | 1584 |
| 2024-09-20 22:21:33.388 | MS1 | 121.4656762523 | 31.1446363191 | 510 | 504990 | -93.06 | 9.22 | 533.81 | 0.17 | 2.36 | 1585 |
| 2024-09-20 22:21:34.590 | MS1 | 121.4656761393 | 31.1446286109 | 947 | 152650 | -89.03 | 6.24 | 50.44 | 0.01 | 1.81 | 940 |
| 2024-09-20 22:21:35.747 | MS1 | 121.4656692791 | 31.1446315811 | 865 | 152650 | -91.74 | 6.89 | 74.69 | 0.06 | 1.64 | 936 |
| 2024-09-20 22:21:36.544 | MS1 | 121.4656645146 | 31.1446192843 | 56 | 152650 | -93.38 | 7.68 | 91.58 | 0.13 | 1.85 | 933 |
| 2024-09-20 22:21:37.281 | MS1 | 121.4656605621 | 31.1446198370 | 928 | 152650 | -87.13 | 3.25 | 68.83 | 0.00 | 1.56 | 914 |
| 2024-09-20 22:21:38.283 | MS1 | 121.4656688654 | 31.1446348677 | 947 | 152650 | -93.38 | 5.45 | 95.13 | 0.07 | 1.63 | 959 |
| 2024-09-20 22:21:39.521 | MS1 | 121.4656623528 | 31.1446187592 | 865 | 152650 | -94.49 | 3.60 | 88.38 | 0.15 | 1.96 | 923 |
| 2024-09-20 22:21:40.729 | MS1 | 121.4656598596 | 31.1446362776 | 56 | 152650 | -94.16 | 7.55 | 82.15 | 0.12 | 2.42 | 1582 |
| 2024-09-20 22:21:41.432 | MS1 | 121.4656723940 | 31.1446341895 | 928 | 152650 | -90.21 | 6.37 | 76.99 | 0.08 | 2.79 | 1594 |
| 2024-09-20 22:21:42.166 | MS1 | 121.4656615585 | 31.1446208262 | 947 | 152650 | -89.37 | 5.16 | 61.81 | 0.01 | 2.32 | 1593 |

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
| 3213586 | 1 | 121.4726219532 | 31.1463402342 | 283 | 1 | 4 | 14.4 | TDD | 166 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3216855 | 5 | 121.4729455270 | 31.1536412008 | 166 | 2 | 1 | 24.6 | TDD | 50 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3220985 | 9 | 121.4701103919 | 31.1528162708 | 296 | 9 | 11 | 17.9 | FDD | 352 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3236895 | 11 | 121.4758926021 | 31.1514519842 | 129 | 14 | 2 | 9.4 | FDD | 49 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3238675 | 10 | 121.4726168461 | 31.1527945597 | 10 | 5 | 11 | 10.0 | FDD | 936 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3240479 | 6 | 121.4693111656 | 31.1440787403 | 306 | 6 | 10 | 2.9 | TDD | 510 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3241726 | 12 | 121.4750232965 | 31.1457112222 | 318 | 3 | 8 | 23.3 | FDD | 947 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3242929 | 13 | 121.4726877366 | 31.1527765359 | 44 | 13 | 11 | 25.2 | FDD | 56 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3251924 | 4 | 121.4735890297 | 31.1557299301 | 248 | 4 | 0 | 1.5 | TDD | 874 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3257443 | 3 | 121.4712561708 | 31.1530126898 | 7 | 7 | 7 | 18.6 | TDD | 455 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3261446 | 8 | 121.4727562094 | 31.1512115848 | 123 | 7 | 8 | 27.3 | FDD | 865 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3266015 | 7 | 121.4668188987 | 31.1475941762 | 21 | 5 | 7 | 12.5 | FDD | 928 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3267279 | 2 | 121.4698879859 | 31.1533966214 | 120 | 0 | 4 | 4.4 | TDD | 903 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.147 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.166 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.289 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.289 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.996 | NREventA2 | measId:1;ServCellPCI:368;Se... |
| 2024-09-20 22:21:35.107 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.387 | NREventA5 | measId:3;ServCellPCI:368;Se... |
| 2024-09-20 22:21:35.436 | NRHandoverAttempt | SourcePCI:368;SourceNR-ARFC... |
| 2024-09-20 22:21:35.470 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.481 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.614 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.614 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213586 | 1 | 9.6507 | 17.5346 | -117.5050 | 12.9178 | 146.2196 | 0.0125 | 0.0191 |
| 2024_09_20 22:00 | 3267279 | 2 | 16.6968 | 13.4871 | -116.7662 | 9.0147 | 95.6412 | 0.0195 | 0.0112 |
| 2024_09_20 22:00 | 3257443 | 3 | 13.5691 | 9.7627 | -114.9461 | 11.6968 | 96.4879 | 0.0147 | 0.0086 |
| 2024_09_20 22:00 | 3251924 | 4 | 15.7957 | 15.2175 | -115.0211 | 5.2017 | 133.4448 | 0.0179 | 0.0118 |
| 2024_09_20 22:00 | 3216855 | 5 | 5.5248 | 19.4602 | -117.8219 | 7.8719 | 195.5201 | 0.0121 | 0.0040 |
| 2024_09_20 22:00 | 3240479 | 6 | 8.6482 | 15.5376 | -116.8144 | 17.7225 | 149.7372 | 0.0174 | 0.0183 |
| 2024_09_20 22:00 | 3266015 | 7 | 18.7788 | 9.4287 | -116.8013 | 4.5516 | 20.7258 | 0.0112 | 0.0132 |
| 2024_09_20 22:00 | 3261446 | 8 | 8.4848 | 18.3230 | -116.0888 | 4.9947 | 29.9690 | 0.0070 | 0.0021 |
| 2024_09_20 22:00 | 3220985 | 9 | 18.9071 | 12.1315 | -114.5827 | 4.3272 | 31.7268 | 0.0050 | 0.0143 |
| 2024_09_20 22:00 | 3238675 | 10 | 18.8062 | 9.5429 | -114.6363 | 4.9664 | 42.8620 | 0.0174 | 0.0165 |
| 2024_09_20 22:00 | 3236895 | 11 | 19.5797 | 5.2348 | -115.8823 | 4.1462 | 22.6182 | 0.0121 | 0.0068 |
| 2024_09_20 22:00 | 3241726 | 12 | 13.4207 | 18.0162 | -114.9300 | 4.3550 | 32.3010 | 0.0151 | 0.0200 |
| 2024_09_20 22:00 | 3242929 | 13 | 15.2489 | 16.5296 | -114.5174 | 4.5594 | 43.2188 | 0.0112 | 0.0112 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414516_D366BFCB | 504990 | 510 | -92.6 | 504990 | 166 | -93.9 | 504990 | 874 | -96.9 | 504990 | 455 |
| MR_1774414516_10C8D18B | 504990 | 510 | -94.6 | 504990 | 166 | -90.7 | 504990 | 874 | -98.6 | 504990 | 455 |
| MR_1774414516_79A3AC82 | 504990 | 510 | -91.3 | 504990 | 166 | -91.2 | 504990 | 874 | -95.0 | 504990 | 455 |
| MR_1774414516_8CEED6A5 | 504990 | 510 | -92.9 | 504990 | 166 | -91.1 | 504990 | 874 | -98.4 | 504990 | 455 |
| MR_1774414516_BC2A0A99 | 152650 | 947 | -91.0 | 152650 | 936 | -96.0 | 152650 | 49 | -97.3 | 152650 | 352 |
| MR_1774414516_F2B0E320 | 152650 | 947 | -87.9 | 152650 | 936 | -94.5 | 152650 | 49 | -95.1 | 152650 | 352 |
| MR_1774414516_D6C60328 | 152650 | 947 | -88.4 | 152650 | 936 | -96.4 | 152650 | 49 | -97.6 | 152650 | 352 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1943: `7c19866a-9e6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7c19866a-9e68-4910-94b0-d23e876109eb` |
| Tag | **multiple-answer** |
| 정답 | **C1|C6|C14|C18** |
| C1 의미 | Increase A3 Offset threshold for 3233381_5 |
| C6 의미 | Decrease transmission power for 3279698_3 |
| C14 의미 | Increase A3 Offset threshold for 3279698_3 |
| C18 의미 | Press down the tilt angle  of 3279698_3 by 5 degrees |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1943] topology](images/train_1943.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3233381_5 **← 정답**
- `C2`: Decrease A3 Offset threshold for 3279698_3
- `C3`: Decrease transmission power for 3233381_5
- `C4`: Press down the tilt angle of 3233381_5 by 4 degrees
- `C5`: Increase transmission power for 3279698_3
- `C6`: Decrease transmission power for 3279698_3 **← 정답**
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233381_5
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Add neighbor relationship between 3233381_5 and 3279698_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279698_3
- `C11`: Lift the tilt angle  of 3279698_3 by 5 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279698_3
- `C13`: Lift the tilt angle of 3233381_5 by 4 degrees
- `C14`: Increase A3 Offset threshold for 3279698_3 **← 정답**
- `C15`: Adjust the azimuth of 3279698_3 by 27 degrees
- `C16`: Check test server and transmission issues
- `C17`: Add neighbor relationship between 3266622_1 and 3279698_3
- `C18`: Press down the tilt angle  of 3279698_3 by 5 degrees **← 정답**
- `C19`: Adjust the azimuth of 3233381_5 by 4 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233381_5
- `C21`: Increase transmission power for 3233381_5
- `C22`: Decrease A3 Offset threshold for 3233381_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.946 | MS1 | 121.4656587038 | 31.1446325526 | 374 | 504990 | -81.80 | 14.73 | 494.49 | 0.04 | 2.67 | 1569 |
| 2024-09-20 22:21:32.908 | MS1 | 121.4656751105 | 31.1446183966 | 374 | 504990 | -83.17 | 17.15 | 451.35 | 0.14 | 2.03 | 1583 |
| 2024-09-20 22:21:33.843 | MS1 | 121.4656704409 | 31.1446215212 | 374 | 504990 | -76.55 | 13.18 | 508.79 | 0.06 | 2.43 | 1575 |
| 2024-09-20 22:21:34.392 | MS1 | 121.4656721407 | 31.1446227429 | 244 | 504990 | -88.71 | 4.89 | 33.13 | 0.02 | 1.01 | 1573 |
| 2024-09-20 22:21:35.318 | MS1 | 121.4656724773 | 31.1446257922 | 244 | 504990 | -86.68 | 3.81 | 67.77 | 0.05 | 1.11 | 1567 |
| 2024-09-20 22:21:36.570 | MS1 | 121.4656740635 | 31.1446216189 | 374 | 504990 | -81.54 | 2.98 | 46.38 | 0.02 | 1.35 | 1567 |
| 2024-09-20 22:21:37.389 | MS1 | 121.4656777742 | 31.1446225505 | 374 | 504990 | -87.05 | 3.50 | 63.75 | 0.01 | 1.28 | 1580 |
| 2024-09-20 22:21:38.123 | MS1 | 121.4656643854 | 31.1446320152 | 244 | 504990 | -82.45 | 2.00 | 44.88 | 0.11 | 1.01 | 1566 |
| 2024-09-20 22:21:39.882 | MS1 | 121.4656690737 | 31.1446214253 | 244 | 504990 | -88.66 | 3.68 | 41.54 | 0.14 | 1.32 | 1571 |
| 2024-09-20 22:21:40.486 | MS1 | 121.4656581162 | 31.1446249747 | 244 | 504990 | -78.18 | 16.35 | 572.08 | 0.00 | 2.94 | 1572 |
| 2024-09-20 22:21:41.164 | MS1 | 121.4656649233 | 31.1446335513 | 244 | 504990 | -83.26 | 12.58 | 294.13 | 0.15 | 2.95 | 1593 |
| 2024-09-20 22:21:42.393 | MS1 | 121.4656643759 | 31.1446347307 | 244 | 504990 | -79.75 | 15.75 | 488.58 | 0.19 | 2.02 | 1590 |

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
| 3214843 | 2 | 121.4699661854 | 31.1533711573 | 106 | 5 | 10 | 49.2 | TDD | 775 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3233381 | 5 | 121.4702125481 | 31.1540337747 | 198 | 2 | 1 | 30.3 | TDD | 374 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3237120 | 4 | 121.4742401294 | 31.1460504507 | 319 | 2 | 12 | 23.9 | TDD | 244 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3266622 | 1 | 121.4732315543 | 31.1480219181 | 125 | 1 | 9 | 40.5 | TDD | 646 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3279698 | 3 | 121.4670592628 | 31.1489042165 | 222 | 2 | 11 | 25.5 | TDD | 1007 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.034 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.052 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.166 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.166 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.878 | NREventA3 | measId:2;ServCellPCI:521;Se... |
| 2024-09-20 22:21:34.118 | NRHandoverAttempt | SourcePCI:521;SourceNR-ARFC... |
| 2024-09-20 22:21:34.156 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.171 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.299 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.299 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.878 | NREventA3 | measId:2;ServCellPCI:798;Se... |
| 2024-09-20 22:21:36.118 | NRHandoverAttempt | SourcePCI:798;SourceNR-ARFC... |
| 2024-09-20 22:21:36.167 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.180 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.295 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.295 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.878 | NREventA3 | measId:2;ServCellPCI:521;Se... |
| 2024-09-20 22:21:38.118 | NRHandoverAttempt | SourcePCI:521;SourceNR-ARFC... |
| 2024-09-20 22:21:38.152 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.163 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.264 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.264 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266622 | 1 | 5.6554 | 6.7188 | -116.5551 | 9.6072 | 134.9828 | 0.0059 | 0.0184 |
| 2024_09_20 22:00 | 3214843 | 2 | 7.6504 | 5.2999 | -115.9454 | 10.0886 | 93.7216 | 0.0044 | 0.0018 |
| 2024_09_20 22:00 | 3279698 | 3 | 18.1112 | 18.6447 | -116.9788 | 12.1033 | 101.2377 | 0.0039 | 0.0169 |
| 2024_09_20 22:00 | 3237120 | 4 | 5.6474 | 6.7558 | -114.2588 | 11.4049 | 161.5203 | 0.0153 | 0.0195 |
| 2024_09_20 22:00 | 3233381 | 5 | 12.8243 | 13.8784 | -116.7651 | 13.5057 | 99.9073 | 0.0059 | 0.0191 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416784_98A94E4B | 504990 | 244 | -89.9 | 504990 | 374 | -88.9 | 504990 | 1007 | -96.8 | 504990 | 646 |
| MR_1774416784_B995C266 | 504990 | 374 | -87.0 | 504990 | 244 | -89.4 | 504990 | 1007 | -96.3 | 504990 | 646 |
| MR_1774416784_58F02DE1 | 504990 | 374 | -90.5 | 504990 | 244 | -89.0 | 504990 | 1007 | -96.6 | 504990 | 646 |
| MR_1774416784_D4D882E1 | 504990 | 244 | -90.7 | 504990 | 374 | -87.5 | 504990 | 1007 | -98.1 | 504990 | 646 |
| MR_1774416784_F7810298 | 504990 | 244 | -88.3 | 504990 | 374 | -89.1 | 504990 | 1007 | -98.0 | 504990 | 646 |
| MR_1774416784_F1C5DF3E | 504990 | 374 | -89.9 | 504990 | 244 | -89.7 | 504990 | 1007 | -97.4 | 504990 | 646 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1944: `b546f48a-64e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b546f48a-64e0-4b6d-b9a4-a5e69044f5b4` |
| Tag | **multiple-answer** |
| 정답 | **C16|C20** |
| C16 의미 | Press down the tilt angle  of 3215898_4 by 3 degrees |
| C20 의미 | Decrease transmission power for 3215898_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1944] topology](images/train_1944.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3210416_2
- `C2`: Lift the tilt angle  of 3215898_4 by 3 degrees
- `C3`: Press down the tilt angle of 3210416_2 by 4 degrees
- `C4`: Check test server and transmission issues
- `C5`: Increase A3 Offset threshold for 3215898_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210416_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215898_4
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210416_2
- `C10`: Increase transmission power for 3210416_2
- `C11`: Adjust the azimuth of 3215898_4 by 2 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215898_4
- `C13`: Increase A3 Offset threshold for 3210416_2
- `C14`: Increase transmission power for 3215898_4
- `C15`: Decrease A3 Offset threshold for 3210416_2
- `C16`: Press down the tilt angle  of 3215898_4 by 3 degrees **← 정답**
- `C17`: Add neighbor relationship between 3210416_2 and 3215898_4
- `C18`: Lift the tilt angle of 3210416_2 by 4 degrees
- `C19`: Adjust the azimuth of 3210416_2 by 33 degrees
- `C20`: Decrease transmission power for 3215898_4 **← 정답**
- `C21`: Decrease A3 Offset threshold for 3215898_4
- `C22`: Add neighbor relationship between 3210757_3 and 3215898_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.406 | MS1 | 121.4656605393 | 31.1446211833 | 902 | 504990 | -81.54 | 17.23 | 525.08 | 0.18 | 2.41 | 1585 |
| 2024-09-20 22:21:32.364 | MS1 | 121.4656597847 | 31.1446283478 | 902 | 504990 | -80.22 | 12.64 | 537.55 | 0.01 | 2.73 | 1577 |
| 2024-09-20 22:21:33.762 | MS1 | 121.4656607620 | 31.1446277807 | 902 | 504990 | -83.56 | 13.99 | 506.12 | 0.14 | 2.78 | 1587 |
| 2024-09-20 22:21:34.408 | MS1 | 121.4656632608 | 31.1446225812 | 902 | 504990 | -93.52 | 1.55 | 70.71 | 0.16 | 1.43 | 1570 |
| 2024-09-20 22:21:35.912 | MS1 | 121.4656626680 | 31.1446328547 | 902 | 504990 | -86.98 | 1.92 | 57.24 | 0.08 | 1.17 | 1579 |
| 2024-09-20 22:21:36.210 | MS1 | 121.4656674822 | 31.1446349212 | 902 | 504990 | -86.98 | 0.13 | 74.44 | 0.19 | 1.31 | 1590 |
| 2024-09-20 22:21:37.604 | MS1 | 121.4656649172 | 31.1446230426 | 902 | 504990 | -91.25 | 3.48 | 74.90 | 0.18 | 1.34 | 1560 |
| 2024-09-20 22:21:38.664 | MS1 | 121.4656627558 | 31.1446188804 | 902 | 504990 | -89.90 | 1.01 | 68.14 | 0.02 | 1.04 | 1596 |
| 2024-09-20 22:21:39.132 | MS1 | 121.4656737477 | 31.1446215691 | 902 | 504990 | -93.46 | 3.63 | 32.25 | 0.10 | 1.17 | 1566 |
| 2024-09-20 22:21:40.268 | MS1 | 121.4656778038 | 31.1446231451 | 902 | 504990 | -75.65 | 16.60 | 328.69 | 0.18 | 2.73 | 1579 |
| 2024-09-20 22:21:41.148 | MS1 | 121.4656749575 | 31.1446198425 | 902 | 504990 | -83.03 | 14.45 | 363.82 | 0.03 | 2.95 | 1578 |
| 2024-09-20 22:21:42.828 | MS1 | 121.4656644520 | 31.1446374082 | 902 | 504990 | -75.18 | 16.21 | 453.08 | 0.04 | 2.39 | 1586 |

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
| 3210416 | 2 | 121.4709617266 | 31.1534936285 | 240 | 2 | 10 | 44.8 | TDD | 902 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3210757 | 3 | 121.4684688131 | 31.1538204048 | 167 | 4 | 12 | 23.6 | TDD | 358 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3215898 | 4 | 121.4754841921 | 31.1462039990 | 261 | 1 | 12 | 37.2 | TDD | 255 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3249185 | 1 | 121.4724517350 | 31.1497394576 | 153 | 5 | 3 | 42.2 | TDD | 614 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.837 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.855 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.979 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.979 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249185 | 1 | 6.1113 | 15.8694 | -117.4230 | 16.2445 | 180.7223 | 0.0095 | 0.0063 |
| 2024_09_20 22:00 | 3210416 | 2 | 11.9106 | 13.3317 | -109.4748 | 5.0345 | 162.2433 | 0.0177 | 0.0130 |
| 2024_09_20 22:00 | 3210757 | 3 | 12.8241 | 16.8391 | -115.4895 | 19.5139 | 142.9345 | 0.0126 | 0.0186 |
| 2024_09_20 22:00 | 3215898 | 4 | 13.7239 | 19.4810 | -114.4876 | 5.7129 | 195.9315 | 0.0089 | 0.0190 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412346_4697FA95 | 504990 | 902 | -93.3 | 504990 | 255 | -93.5 | 504990 | 358 | -95.1 | 504990 | 614 |
| MR_1774412346_5391079D | 504990 | 902 | -92.0 | 504990 | 255 | -94.5 | 504990 | 358 | -97.3 | 504990 | 614 |
| MR_1774412346_33EB20BD | 504990 | 902 | -93.6 | 504990 | 255 | -93.4 | 504990 | 358 | -94.9 | 504990 | 614 |
| MR_1774412346_363C3335 | 504990 | 255 | -94.6 | 504990 | 902 | -94.9 | 504990 | 358 | -96.0 | 504990 | 614 |
| MR_1774412346_0A8F7B99 | 504990 | 902 | -93.9 | 504990 | 255 | -94.3 | 504990 | 358 | -97.7 | 504990 | 614 |
| MR_1774412346_A24BAD59 | 504990 | 902 | -92.4 | 504990 | 255 | -95.9 | 504990 | 358 | -95.6 | 504990 | 614 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1945: `f36c997d-9c4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f36c997d-9c46-426d-80c8-5a40740a51ea` |
| Tag | **multiple-answer** |
| 정답 | **C11|C14|C16|C21** |
| C11 의미 | Press down the tilt angle  of 3239430_5 by 6 degrees |
| C14 의미 | Decrease transmission power for 3239430_5 |
| C16 의미 | Increase A3 Offset threshold for 3239430_5 |
| C21 의미 | Increase A3 Offset threshold for 3279646_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1945] topology](images/train_1945.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3279646_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279646_4
- `C3`: Decrease A3 Offset threshold for 3239430_5
- `C4`: Check test server and transmission issues
- `C5`: Add neighbor relationship between 3279646_4 and 3239430_5
- `C6`: Lift the tilt angle of 3279646_4 by 5 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239430_5
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239430_5
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279646_4
- `C11`: Press down the tilt angle  of 3239430_5 by 6 degrees **← 정답**
- `C12`: Press down the tilt angle of 3279646_4 by 5 degrees
- `C13`: Increase transmission power for 3279646_4
- `C14`: Decrease transmission power for 3239430_5 **← 정답**
- `C15`: Decrease transmission power for 3279646_4
- `C16`: Increase A3 Offset threshold for 3239430_5 **← 정답**
- `C17`: Adjust the azimuth of 3279646_4 by 27 degrees
- `C18`: Increase transmission power for 3239430_5
- `C19`: Adjust the azimuth of 3239430_5 by 10 degrees
- `C20`: Add neighbor relationship between 3273523_3 and 3239430_5
- `C21`: Increase A3 Offset threshold for 3279646_4 **← 정답**
- `C22`: Lift the tilt angle  of 3239430_5 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.138 | MS1 | 121.4656627044 | 31.1446289540 | 940 | 504990 | -76.51 | 16.01 | 337.42 | 0.03 | 2.51 | 1594 |
| 2024-09-20 22:21:32.607 | MS1 | 121.4656632523 | 31.1446210028 | 940 | 504990 | -78.43 | 15.25 | 384.89 | 0.00 | 2.79 | 1560 |
| 2024-09-20 22:21:33.295 | MS1 | 121.4656686173 | 31.1446213535 | 940 | 504990 | -79.80 | 15.35 | 555.93 | 0.13 | 2.41 | 1577 |
| 2024-09-20 22:21:34.791 | MS1 | 121.4656655673 | 31.1446306273 | 199 | 504990 | -89.94 | 1.39 | 35.79 | 0.15 | 1.38 | 1567 |
| 2024-09-20 22:21:35.324 | MS1 | 121.4656587489 | 31.1446213653 | 199 | 504990 | -82.26 | 1.68 | 26.19 | 0.08 | 1.25 | 1588 |
| 2024-09-20 22:21:36.403 | MS1 | 121.4656615100 | 31.1446321600 | 940 | 504990 | -85.08 | 3.09 | 69.30 | 0.02 | 1.09 | 1584 |
| 2024-09-20 22:21:37.810 | MS1 | 121.4656663433 | 31.1446218492 | 940 | 504990 | -84.41 | 4.29 | 28.73 | 0.03 | 1.37 | 1594 |
| 2024-09-20 22:21:38.128 | MS1 | 121.4656743847 | 31.1446229090 | 199 | 504990 | -89.42 | 2.73 | 26.59 | 0.17 | 1.08 | 1574 |
| 2024-09-20 22:21:39.252 | MS1 | 121.4656728897 | 31.1446193005 | 199 | 504990 | -82.02 | 4.33 | 69.13 | 0.18 | 1.12 | 1595 |
| 2024-09-20 22:21:40.451 | MS1 | 121.4656763772 | 31.1446277395 | 199 | 504990 | -75.44 | 14.39 | 302.30 | 0.02 | 2.23 | 1583 |
| 2024-09-20 22:21:41.298 | MS1 | 121.4656676327 | 31.1446369134 | 199 | 504990 | -77.54 | 15.69 | 362.86 | 0.12 | 2.83 | 1582 |
| 2024-09-20 22:21:42.766 | MS1 | 121.4656689294 | 31.1446296404 | 199 | 504990 | -83.77 | 15.72 | 468.62 | 0.02 | 2.29 | 1588 |

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
| 3227364 | 1 | 121.4686285879 | 31.1444153151 | 164 | 4 | 6 | 33.2 | TDD | 199 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3239430 | 5 | 121.4657482252 | 31.1530565919 | 171 | 3 | 0 | 44.8 | TDD | 497 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3243404 | 2 | 121.4648923148 | 31.1495968346 | 236 | 14 | 2 | 25.8 | TDD | 327 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3273523 | 3 | 121.4720403300 | 31.1532405679 | 195 | 10 | 6 | 48.8 | TDD | 233 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3279646 | 4 | 121.4741170927 | 31.1468149946 | 280 | 3 | 2 | 25.0 | TDD | 940 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.799 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.818 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.968 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.968 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.640 | NREventA3 | measId:2;ServCellPCI:818;Se... |
| 2024-09-20 22:21:33.880 | NRHandoverAttempt | SourcePCI:818;SourceNR-ARFC... |
| 2024-09-20 22:21:33.926 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:33.941 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.068 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.068 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.640 | NREventA3 | measId:2;ServCellPCI:811;Se... |
| 2024-09-20 22:21:35.880 | NRHandoverAttempt | SourcePCI:811;SourceNR-ARFC... |
| 2024-09-20 22:21:35.922 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.932 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:36.046 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.046 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.640 | NREventA3 | measId:2;ServCellPCI:818;Se... |
| 2024-09-20 22:21:37.880 | NRHandoverAttempt | SourcePCI:818;SourceNR-ARFC... |
| 2024-09-20 22:21:37.927 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.938 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.042 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.042 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227364 | 1 | 15.8789 | 18.3542 | -115.1813 | 16.3275 | 173.9517 | 0.0076 | 0.0144 |
| 2024_09_20 22:00 | 3243404 | 2 | 6.4073 | 10.2150 | -115.3348 | 11.9206 | 172.6342 | 0.0083 | 0.0131 |
| 2024_09_20 22:00 | 3273523 | 3 | 8.1228 | 19.0477 | -114.7017 | 17.6931 | 199.6013 | 0.0121 | 0.0061 |
| 2024_09_20 22:00 | 3279646 | 4 | 11.8990 | 5.5013 | -114.2433 | 5.7904 | 129.6346 | 0.0065 | 0.0166 |
| 2024_09_20 22:00 | 3239430 | 5 | 13.3565 | 5.5035 | -116.8001 | 17.7873 | 161.0114 | 0.0192 | 0.0065 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413239_C23E83C7 | 504990 | 199 | -88.2 | 504990 | 940 | -89.0 | 504990 | 497 | -91.2 | 504990 | 233 |
| MR_1774413239_9D2A9AEE | 504990 | 199 | -91.7 | 504990 | 940 | -90.2 | 504990 | 497 | -91.5 | 504990 | 233 |
| MR_1774413239_971A2CD3 | 504990 | 940 | -90.5 | 504990 | 199 | -87.2 | 504990 | 497 | -88.3 | 504990 | 233 |
| MR_1774413239_0115CCB3 | 504990 | 199 | -90.0 | 504990 | 940 | -88.7 | 504990 | 497 | -89.3 | 504990 | 233 |
| MR_1774413239_75250B76 | 504990 | 940 | -90.8 | 504990 | 199 | -87.3 | 504990 | 497 | -91.2 | 504990 | 233 |
| MR_1774413239_BAB75EF8 | 504990 | 940 | -91.4 | 504990 | 199 | -90.5 | 504990 | 497 | -91.9 | 504990 | 233 |
| MR_1774413239_43F6AA3B | 504990 | 199 | -90.2 | 504990 | 940 | -88.9 | 504990 | 497 | -89.8 | 504990 | 233 |
| MR_1774413239_0CE0950F | 504990 | 940 | -90.4 | 504990 | 199 | -89.5 | 504990 | 497 | -88.6 | 504990 | 233 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1946: `fb1cc9b5-ac1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fb1cc9b5-ac13-4043-9e9f-9765342babf9` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease A3 Offset threshold for 3276553_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1946] topology](images/train_1946.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3251435_3
- `C2`: Decrease A3 Offset threshold for 3251435_3
- `C3`: Decrease A3 Offset threshold for 3276553_2 **← 정답**
- `C4`: Increase transmission power for 3276553_2
- `C5`: Add neighbor relationship between 3230053_4 and 3251435_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251435_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276553_2
- `C8`: Check test server and transmission issues
- `C9`: Press down the tilt angle  of 3251435_3 by 10 degrees
- `C10`: Adjust the azimuth of 3276553_2 by 50 degrees
- `C11`: Increase A3 Offset threshold for 3276553_2
- `C12`: Press down the tilt angle of 3276553_2 by 3 degrees
- `C13`: Lift the tilt angle  of 3251435_3 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251435_3
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease transmission power for 3251435_3
- `C17`: Decrease transmission power for 3276553_2
- `C18`: Add neighbor relationship between 3276553_2 and 3251435_3
- `C19`: Adjust the azimuth of 3251435_3 by 50 degrees
- `C20`: Increase transmission power for 3251435_3
- `C21`: Lift the tilt angle of 3276553_2 by 3 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276553_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.262 | MS1 | 121.4656645393 | 31.1446318564 | 1 | 504990 | -79.42 | 15.78 | 444.92 | 0.18 | 2.60 | 1577 |
| 2024-09-20 22:21:32.500 | MS1 | 121.4656627639 | 31.1446355187 | 1 | 504990 | -77.24 | 14.68 | 409.53 | 0.20 | 2.64 | 1582 |
| 2024-09-20 22:21:33.482 | MS1 | 121.4656595057 | 31.1446256167 | 1 | 504990 | -78.66 | 15.97 | 590.23 | 0.07 | 2.90 | 1583 |
| 2024-09-20 22:21:34.599 | MS1 | 121.4656765592 | 31.1446312266 | 1 | 504990 | -87.90 | -1.31 | 48.35 | 0.06 | 1.25 | 1596 |
| 2024-09-20 22:21:35.477 | MS1 | 121.4656754100 | 31.1446202129 | 1 | 504990 | -88.46 | -0.57 | 63.10 | 0.05 | 1.33 | 1587 |
| 2024-09-20 22:21:36.109 | MS1 | 121.4656590750 | 31.1446194430 | 1 | 504990 | -92.66 | -3.40 | 28.13 | 0.01 | 1.09 | 1581 |
| 2024-09-20 22:21:37.255 | MS1 | 121.4656692913 | 31.1446355433 | 1 | 504990 | -88.02 | -0.46 | 43.27 | 0.06 | 1.49 | 1598 |
| 2024-09-20 22:21:38.717 | MS1 | 121.4656756564 | 31.1446254445 | 1 | 504990 | -90.88 | -2.58 | 45.70 | 0.20 | 1.47 | 1595 |
| 2024-09-20 22:21:39.114 | MS1 | 121.4656752876 | 31.1446200716 | 117 | 504990 | -82.89 | 17.67 | 237.13 | 0.02 | 1.49 | 1584 |
| 2024-09-20 22:21:40.160 | MS1 | 121.4656771342 | 31.1446284876 | 117 | 504990 | -81.51 | 13.61 | 579.51 | 0.02 | 2.55 | 1592 |
| 2024-09-20 22:21:41.161 | MS1 | 121.4656707583 | 31.1446371984 | 117 | 504990 | -79.07 | 12.29 | 418.26 | 0.10 | 2.02 | 1585 |
| 2024-09-20 22:21:42.644 | MS1 | 121.4656777572 | 31.1446292466 | 117 | 504990 | -75.85 | 12.58 | 414.14 | 0.10 | 2.06 | 1573 |

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
| 3230053 | 4 | 121.4716334729 | 31.1450043514 | 224 | 4 | 1 | 40.1 | TDD | 719 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3245549 | 1 | 121.4656432856 | 31.1453376899 | 139 | 1 | 4 | 33.3 | TDD | 344 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3251435 | 3 | 121.4730145813 | 31.1492490921 | 358 | 8 | 11 | 44.4 | TDD | 117 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3276553 | 2 | 121.4707664228 | 31.1457255656 | 354 | 0 | 2 | 22.5 | TDD | 1 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.532 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.548 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.682 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.682 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.368 | NREventA3 | measId:2;ServCellPCI:642;Se... |
| 2024-09-20 22:21:38.608 | NRHandoverAttempt | SourcePCI:642;SourceNR-ARFC... |
| 2024-09-20 22:21:38.638 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.648 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.749 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.749 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245549 | 1 | 19.8040 | 8.5262 | -115.6641 | 15.1729 | 144.8349 | 0.0034 | 0.0152 |
| 2024_09_20 22:00 | 3276553 | 2 | 5.5056 | 10.5279 | -115.0680 | 16.3793 | 158.0659 | 0.0018 | 0.1663 |
| 2024_09_20 22:00 | 3251435 | 3 | 8.9237 | 17.4115 | -116.4714 | 10.5652 | 139.2429 | 0.0191 | 0.0025 |
| 2024_09_20 22:00 | 3230053 | 4 | 17.8699 | 16.0072 | -116.4862 | 8.2661 | 118.3561 | 0.0173 | 0.0135 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412198_4C959CB1 | 504990 | 1 | -86.6 | 504990 | 117 | -80.2 | 504990 | 719 | -80.8 | 504990 | 344 |
| MR_1774412198_AA0C857C | 504990 | 1 | -87.2 | 504990 | 117 | -79.8 | 504990 | 719 | -80.1 | 504990 | 344 |
| MR_1774412198_C1FC6640 | 504990 | 1 | -89.1 | 504990 | 117 | -81.1 | 504990 | 719 | -82.8 | 504990 | 344 |
| MR_1774412198_E36D67EE | 504990 | 117 | -83.0 | 504990 | 1 | -88.3 | 504990 | 719 | -81.9 | 504990 | 344 |
| MR_1774412198_ED2B4028 | 504990 | 117 | -81.1 | 504990 | 1 | -86.4 | 504990 | 719 | -82.2 | 504990 | 344 |
| MR_1774412198_2D80C3F9 | 504990 | 1 | -88.2 | 504990 | 117 | -81.5 | 504990 | 719 | -80.7 | 504990 | 344 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1947: `979a12c3-59b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `979a12c3-59b1-45fb-a936-93bcc4ef264c` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249160_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1947] topology](images/train_1947.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249160_5
- `C2`: Lift the tilt angle  of 3250309_3 by 2 degrees
- `C3`: Add neighbor relationship between 3225514_7 and 3250309_3
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250309_3
- `C6`: Decrease transmission power for 3250309_3
- `C7`: Decrease A3 Offset threshold for 3250309_3
- `C8`: Press down the tilt angle of 3249160_5 by 2 degrees
- `C9`: Add neighbor relationship between 3249160_5 and 3250309_3
- `C10`: Lift the tilt angle of 3249160_5 by 2 degrees
- `C11`: Increase transmission power for 3250309_3
- `C12`: Increase A3 Offset threshold for 3249160_5
- `C13`: Press down the tilt angle  of 3250309_3 by 2 degrees
- `C14`: Increase transmission power for 3249160_5
- `C15`: Check test server and transmission issues
- `C16`: Decrease A3 Offset threshold for 3249160_5
- `C17`: Adjust the azimuth of 3249160_5 by 4 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249160_5 **← 정답**
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250309_3
- `C20`: Increase A3 Offset threshold for 3250309_3
- `C21`: Adjust the azimuth of 3250309_3 by 46 degrees
- `C22`: Decrease transmission power for 3249160_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.789 | MS1 | 121.4656750288 | 31.1446218969 | 470 | 504990 | -93.70 | 9.51 | 543.94 | 0.01 | 2.66 | 1586 |
| 2024-09-20 22:21:32.213 | MS1 | 121.4656727254 | 31.1446346763 | 699 | 504990 | -93.76 | 10.47 | 451.71 | 0.12 | 2.88 | 1579 |
| 2024-09-20 22:21:33.417 | MS1 | 121.4656747151 | 31.1446331902 | 533 | 504990 | -95.26 | 13.17 | 322.17 | 0.14 | 2.65 | 1588 |
| 2024-09-20 22:21:34.712 | MS1 | 121.4656730841 | 31.1446250737 | 187 | 152650 | -92.52 | 7.89 | 54.75 | 0.06 | 1.70 | 968 |
| 2024-09-20 22:21:35.646 | MS1 | 121.4656676172 | 31.1446222183 | 631 | 152650 | -92.80 | 7.27 | 94.33 | 0.20 | 1.98 | 993 |
| 2024-09-20 22:21:36.827 | MS1 | 121.4656739582 | 31.1446343658 | 809 | 152650 | -95.78 | 7.30 | 60.38 | 0.09 | 1.57 | 956 |
| 2024-09-20 22:21:37.386 | MS1 | 121.4656734639 | 31.1446269540 | 346 | 152650 | -87.97 | 5.22 | 48.16 | 0.13 | 1.95 | 990 |
| 2024-09-20 22:21:38.749 | MS1 | 121.4656738960 | 31.1446300434 | 187 | 152650 | -96.23 | 3.26 | 99.03 | 0.02 | 1.91 | 911 |
| 2024-09-20 22:21:39.367 | MS1 | 121.4656604264 | 31.1446184025 | 631 | 152650 | -91.17 | 6.34 | 72.89 | 0.01 | 1.56 | 905 |
| 2024-09-20 22:21:40.754 | MS1 | 121.4656677927 | 31.1446233911 | 809 | 152650 | -89.09 | 6.49 | 91.18 | 0.09 | 2.06 | 1594 |
| 2024-09-20 22:21:41.247 | MS1 | 121.4656699798 | 31.1446212573 | 346 | 152650 | -96.78 | 5.29 | 62.81 | 0.13 | 2.63 | 1589 |
| 2024-09-20 22:21:42.842 | MS1 | 121.4656586452 | 31.1446284073 | 187 | 152650 | -95.49 | 2.90 | 65.31 | 0.05 | 2.84 | 1600 |

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
| 3212043 | 1 | 121.4705152420 | 31.1523483113 | 9 | 8 | 9 | 3.5 | TDD | 614 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3215069 | 11 | 121.4661245609 | 31.1448855312 | 109 | 6 | 3 | 19.7 | FDD | 346 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3223567 | 13 | 121.4752864607 | 31.1527404303 | 229 | 6 | 12 | 25.5 | FDD | 509 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3225514 | 7 | 121.4690095599 | 31.1499154420 | 290 | 0 | 9 | 27.6 | FDD | 809 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3226600 | 2 | 121.4741496626 | 31.1494942480 | 89 | 2 | 4 | 17.7 | TDD | 847 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3230861 | 10 | 121.4685023717 | 31.1507285550 | 24 | 3 | 12 | 22.8 | FDD | 631 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3237934 | 6 | 121.4681627966 | 31.1472543612 | 210 | 3 | 10 | 27.6 | TDD | 699 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3239596 | 9 | 121.4728993255 | 31.1463662929 | 210 | 8 | 6 | 19.0 | FDD | 821 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3244244 | 12 | 121.4754278028 | 31.1490260674 | 189 | 4 | 1 | 3.9 | FDD | 187 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3249160 | 5 | 121.4724065968 | 31.1448206320 | 272 | 2 | 11 | 0.8 | TDD | 470 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3250309 | 3 | 121.4679362064 | 31.1529956102 | 147 | 1 | 9 | 22.9 | TDD | 530 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3257519 | 4 | 121.4705046244 | 31.1479657984 | 215 | 14 | 3 | 1.1 | TDD | 533 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3266704 | 8 | 121.4740600822 | 31.1456238822 | 206 | 4 | 12 | 29.6 | FDD | 816 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |

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
| 2024-09-20 22:21:31.183 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.202 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.303 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.303 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.022 | NREventA2 | measId:1;ServCellPCI:713;Se... |
| 2024-09-20 22:21:35.159 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.456 | NREventA5 | measId:3;ServCellPCI:713;Se... |
| 2024-09-20 22:21:35.497 | NRHandoverAttempt | SourcePCI:713;SourceNR-ARFC... |
| 2024-09-20 22:21:35.538 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.550 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.692 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.692 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212043 | 1 | 5.3215 | 14.2269 | -115.8703 | 6.8506 | 85.5223 | 0.0184 | 0.0036 |
| 2024_09_20 22:00 | 3226600 | 2 | 5.0141 | 14.7497 | -114.1856 | 16.3887 | 177.7906 | 0.0191 | 0.0102 |
| 2024_09_20 22:00 | 3250309 | 3 | 15.2876 | 17.8016 | -117.8945 | 8.7696 | 147.7034 | 0.0143 | 0.0104 |
| 2024_09_20 22:00 | 3257519 | 4 | 10.7781 | 15.3933 | -115.3202 | 10.4188 | 94.7286 | 0.0007 | 0.0056 |
| 2024_09_20 22:00 | 3249160 | 5 | 6.6580 | 6.4290 | -114.8657 | 9.9820 | 83.4913 | 0.0119 | 0.0096 |
| 2024_09_20 22:00 | 3237934 | 6 | 10.1349 | 12.9407 | -114.5835 | 7.9405 | 120.1930 | 0.0059 | 0.0170 |
| 2024_09_20 22:00 | 3225514 | 7 | 11.4679 | 12.1180 | -114.6687 | 3.5158 | 29.7069 | 0.0002 | 0.0158 |
| 2024_09_20 22:00 | 3266704 | 8 | 9.8940 | 18.8829 | -114.7238 | 4.7590 | 44.4764 | 0.0102 | 0.0113 |
| 2024_09_20 22:00 | 3239596 | 9 | 16.6900 | 19.2198 | -114.5217 | 3.6006 | 22.5997 | 0.0070 | 0.0184 |
| 2024_09_20 22:00 | 3230861 | 10 | 18.7121 | 17.4357 | -115.1906 | 4.5696 | 33.0179 | 0.0198 | 0.0072 |
| 2024_09_20 22:00 | 3215069 | 11 | 12.1654 | 7.5545 | -117.1874 | 4.2935 | 44.8164 | 0.0073 | 0.0073 |
| 2024_09_20 22:00 | 3244244 | 12 | 8.6962 | 9.0890 | -117.0265 | 3.8412 | 46.8144 | 0.0138 | 0.0109 |
| 2024_09_20 22:00 | 3223567 | 13 | 9.5898 | 17.6097 | -117.4626 | 4.8054 | 25.5774 | 0.0021 | 0.0109 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413262_9F0663AC | 152650 | 187 | -91.6 | 152650 | 821 | -97.9 | 152650 | 816 | -101.7 | 152650 | 509 |
| MR_1774413262_16C93AA6 | 152650 | 187 | -91.7 | 152650 | 821 | -96.9 | 152650 | 816 | -99.2 | 152650 | 509 |
| MR_1774413262_583A4C41 | 504990 | 533 | -94.8 | 504990 | 530 | -90.1 | 504990 | 847 | -95.3 | 504990 | 614 |
| MR_1774413262_D9767197 | 152650 | 187 | -94.1 | 152650 | 821 | -94.9 | 152650 | 816 | -99.8 | 152650 | 509 |
| MR_1774413262_F778D9AE | 152650 | 187 | -93.0 | 152650 | 821 | -96.9 | 152650 | 816 | -101.4 | 152650 | 509 |
| MR_1774413262_B11A846B | 504990 | 533 | -96.2 | 504990 | 530 | -90.1 | 504990 | 847 | -96.1 | 504990 | 614 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1948: `200b8d7c-914...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `200b8d7c-914a-400c-8173-282daee77f36` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Lift the tilt angle  of 3215194_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1948] topology](images/train_1948.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Add neighbor relationship between 3215194_4 and 3215541_1
- `C3`: Increase transmission power for 3215541_1
- `C4`: Decrease transmission power for 3251352_2
- `C5`: Decrease transmission power for 3215541_1
- `C6`: Adjust the azimuth of 3215194_4 by 50 degrees
- `C7`: Press down the tilt angle  of 3215194_4 by 10 degrees
- `C8`: Press down the tilt angle of 3251352_2 by 5 degrees
- `C9`: Decrease A3 Offset threshold for 3215541_1
- `C10`: Decrease A3 Offset threshold for 3251352_2
- `C11`: Increase A3 Offset threshold for 3251352_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215541_1
- `C13`: Lift the tilt angle  of 3215194_4 by 10 degrees **← 정답**
- `C14`: Adjust the azimuth of 3251352_2 by 5 degrees
- `C15`: Lift the tilt angle of 3251352_2 by 5 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215541_1
- `C17`: Increase A3 Offset threshold for 3215541_1
- `C18`: Check test server and transmission issues
- `C19`: Increase transmission power for 3251352_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251352_2
- `C21`: Add neighbor relationship between 3251352_2 and 3215541_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251352_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.422 | MS1 | 121.4656663683 | 31.1446348211 | 905 | 504990 | -87.23 | 16.37 | 310.75 | 0.09 | 2.36 | 1583 |
| 2024-09-20 22:21:32.108 | MS1 | 121.4656759372 | 31.1446198570 | 905 | 504990 | -88.15 | 12.69 | 520.09 | 0.02 | 2.11 | 1569 |
| 2024-09-20 22:21:33.491 | MS1 | 121.4656584297 | 31.1446272076 | 905 | 504990 | -89.20 | 12.34 | 511.95 | 0.09 | 2.66 | 1575 |
| 2024-09-20 22:21:34.106 | MS1 | 121.4656679730 | 31.1446212871 | 905 | 504990 | -88.97 | 12.97 | 105.07 | 0.03 | 2.01 | 1599 |
| 2024-09-20 22:21:35.383 | MS1 | 121.4656608569 | 31.1446348811 | 905 | 504990 | -86.07 | 16.75 | 81.69 | 0.12 | 2.96 | 1586 |
| 2024-09-20 22:21:36.862 | MS1 | 121.4656643581 | 31.1446191844 | 905 | 504990 | -86.32 | 14.68 | 86.56 | 0.09 | 2.08 | 1589 |
| 2024-09-20 22:21:37.510 | MS1 | 121.4656705635 | 31.1446245596 | 905 | 504990 | -92.39 | 7.88 | 92.43 | 0.02 | 2.75 | 1590 |
| 2024-09-20 22:21:38.223 | MS1 | 121.4656676521 | 31.1446289429 | 905 | 504990 | -91.47 | 8.23 | 99.82 | 0.14 | 2.11 | 1567 |
| 2024-09-20 22:21:39.152 | MS1 | 121.4656625780 | 31.1446239024 | 905 | 504990 | -89.51 | 10.75 | 67.03 | 0.06 | 2.67 | 1596 |
| 2024-09-20 22:21:40.136 | MS1 | 121.4656767640 | 31.1446340030 | 905 | 504990 | -89.67 | 12.53 | 601.54 | 0.01 | 2.94 | 1572 |
| 2024-09-20 22:21:41.296 | MS1 | 121.4656695275 | 31.1446376440 | 905 | 504990 | -91.59 | 9.34 | 381.63 | 0.06 | 2.85 | 1593 |
| 2024-09-20 22:21:42.269 | MS1 | 121.4656651703 | 31.1446371350 | 905 | 504990 | -93.93 | 11.22 | 499.62 | 0.07 | 2.09 | 1590 |

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
| 3210658 | 3 | 121.4640828649 | 31.1474080909 | 17 | 13 | 9 | 33.7 | TDD | 771 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3215194 | 4 | 121.4647607675 | 31.1511534582 | 32 | 1 | 1 | 17.1 | TDD | 620 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3215541 | 1 | 121.4714712616 | 31.1478955250 | 15 | 10 | 0 | 22.8 | TDD | 728 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3251352 | 2 | 121.4756592612 | 31.1537693115 | 218 | 4 | 0 | 31.0 | TDD | 905 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.138 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.156 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.303 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.303 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.971 | NREventA3 | measId:2;ServCellPCI:448;Se... |
| 2024-09-20 22:21:38.211 | NRHandoverAttempt | SourcePCI:448;SourceNR-ARFC... |
| 2024-09-20 22:21:38.244 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.257 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.383 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.383 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215541 | 1 | 12.3176 | 15.7128 | -116.2236 | 18.3822 | 111.6906 | 0.0120 | 0.0101 |
| 2024_09_20 22:00 | 3251352 | 2 | 85.7372 | 84.5167 | -115.4839 | 9.9605 | 97.9671 | 0.0077 | 0.0018 |
| 2024_09_20 22:00 | 3210658 | 3 | 15.9852 | 18.2953 | -115.0942 | 14.0608 | 195.1327 | 0.0033 | 0.0080 |
| 2024_09_20 22:00 | 3215194 | 4 | 14.2200 | 8.6902 | -115.2332 | 7.8268 | 93.5105 | 0.0172 | 0.0035 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416352_B5E44003 | 504990 | 905 | -84.8 | 504990 | 728 | -90.9 | 504990 | 620 | -102.5 | 504990 | 771 |
| MR_1774416352_932F4E94 | 504990 | 905 | -86.6 | 504990 | 728 | -92.3 | 504990 | 620 | -102.3 | 504990 | 771 |
| MR_1774416352_761C4EFA | 504990 | 905 | -86.8 | 504990 | 728 | -91.1 | 504990 | 620 | -100.4 | 504990 | 771 |
| MR_1774416352_FEBA6747 | 504990 | 905 | -86.4 | 504990 | 728 | -93.8 | 504990 | 620 | -100.6 | 504990 | 771 |
| MR_1774416352_31E945D6 | 504990 | 905 | -85.9 | 504990 | 728 | -93.1 | 504990 | 620 | -101.3 | 504990 | 771 |
| MR_1774416352_9CF1DDFE | 504990 | 905 | -85.2 | 504990 | 728 | -92.3 | 504990 | 620 | -100.8 | 504990 | 771 |
| MR_1774416352_A4C1E19C | 504990 | 905 | -87.2 | 504990 | 728 | -93.3 | 504990 | 620 | -99.2 | 504990 | 771 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1949: `9d931a42-ee1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9d931a42-ee11-4255-81dc-162d973c083f` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264987_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1949] topology](images/train_1949.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3255485_1
- `C2`: Decrease transmission power for 3255485_1
- `C3`: Increase transmission power for 3264987_2
- `C4`: Press down the tilt angle of 3264987_2 by 4 degrees
- `C5`: Adjust the azimuth of 3264987_2 by 6 degrees
- `C6`: Decrease transmission power for 3264987_2
- `C7`: Increase transmission power for 3255485_1
- `C8`: Check test server and transmission issues
- `C9`: Adjust the azimuth of 3255485_1 by 0 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255485_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264987_2 **← 정답**
- `C12`: Press down the tilt angle  of 3255485_1 by 3 degrees
- `C13`: Add neighbor relationship between 3264987_2 and 3255485_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264987_2
- `C15`: Add neighbor relationship between 3233502_13 and 3255485_1
- `C16`: Increase A3 Offset threshold for 3264987_2
- `C17`: Lift the tilt angle of 3264987_2 by 4 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease A3 Offset threshold for 3255485_1
- `C20`: Decrease A3 Offset threshold for 3264987_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255485_1
- `C22`: Lift the tilt angle  of 3255485_1 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.280 | MS1 | 121.4656617335 | 31.1446359583 | 786 | 504990 | -95.05 | 11.73 | 603.60 | 0.17 | 2.89 | 1584 |
| 2024-09-20 22:21:32.430 | MS1 | 121.4656768977 | 31.1446195757 | 568 | 504990 | -93.51 | 14.54 | 410.60 | 0.04 | 2.88 | 1578 |
| 2024-09-20 22:21:33.147 | MS1 | 121.4656758862 | 31.1446280544 | 218 | 504990 | -95.33 | 11.14 | 408.85 | 0.03 | 2.71 | 1598 |
| 2024-09-20 22:21:34.475 | MS1 | 121.4656634626 | 31.1446210821 | 940 | 152650 | -93.66 | 2.77 | 59.56 | 0.00 | 1.54 | 979 |
| 2024-09-20 22:21:35.154 | MS1 | 121.4656746063 | 31.1446310155 | 62 | 152650 | -94.01 | 7.38 | 57.25 | 0.05 | 1.86 | 925 |
| 2024-09-20 22:21:36.255 | MS1 | 121.4656749657 | 31.1446270819 | 894 | 152650 | -92.08 | 2.16 | 70.81 | 0.11 | 1.76 | 976 |
| 2024-09-20 22:21:37.572 | MS1 | 121.4656757121 | 31.1446347923 | 456 | 152650 | -91.47 | 7.43 | 94.16 | 0.12 | 1.94 | 948 |
| 2024-09-20 22:21:38.677 | MS1 | 121.4656759824 | 31.1446207972 | 940 | 152650 | -95.79 | 5.25 | 70.87 | 0.12 | 1.64 | 929 |
| 2024-09-20 22:21:39.391 | MS1 | 121.4656701646 | 31.1446287120 | 62 | 152650 | -88.28 | 7.33 | 63.33 | 0.11 | 1.58 | 923 |
| 2024-09-20 22:21:40.377 | MS1 | 121.4656721411 | 31.1446182715 | 894 | 152650 | -91.53 | 3.83 | 84.58 | 0.11 | 2.30 | 1586 |
| 2024-09-20 22:21:41.798 | MS1 | 121.4656720749 | 31.1446260218 | 456 | 152650 | -89.45 | 6.29 | 58.66 | 0.14 | 2.84 | 1598 |
| 2024-09-20 22:21:42.626 | MS1 | 121.4656726210 | 31.1446376315 | 940 | 152650 | -87.43 | 7.77 | 49.00 | 0.00 | 2.52 | 1595 |

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
| 3211408 | 3 | 121.4658825358 | 31.1492230374 | 278 | 2 | 12 | 15.6 | TDD | 242 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3216318 | 6 | 121.4691008291 | 31.1445269424 | 175 | 1 | 8 | 16.1 | TDD | 218 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3222394 | 8 | 121.4716622658 | 31.1452479128 | 148 | 10 | 5 | 20.4 | FDD | 456 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3231518 | 10 | 121.4719051068 | 31.1508106427 | 145 | 14 | 0 | 23.7 | FDD | 149 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3233502 | 13 | 121.4686076270 | 31.1472719075 | 336 | 1 | 4 | 5.7 | FDD | 894 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3255485 | 1 | 121.4734023697 | 31.1491517032 | 236 | 3 | 2 | 2.3 | TDD | 75 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3258888 | 11 | 121.4702939552 | 31.1442659021 | 74 | 15 | 4 | 3.1 | FDD | 920 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3259488 | 4 | 121.4661019562 | 31.1508720217 | 305 | 15 | 4 | 19.1 | TDD | 980 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3263322 | 12 | 121.4643183136 | 31.1455533693 | 166 | 13 | 3 | 2.1 | FDD | 62 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3264987 | 2 | 121.4735354289 | 31.1516069025 | 218 | 3 | 5 | 15.2 | TDD | 786 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3267122 | 9 | 121.4685341047 | 31.1466794994 | 47 | 2 | 11 | 14.3 | FDD | 940 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3268165 | 7 | 121.4657192819 | 31.1492257029 | 329 | 15 | 8 | 18.5 | FDD | 34 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3274882 | 5 | 121.4693903631 | 31.1553415002 | 113 | 5 | 11 | 14.6 | TDD | 568 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.675 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.692 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.793 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.793 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.499 | NREventA2 | measId:1;ServCellPCI:955;Se... |
| 2024-09-20 22:21:35.643 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.933 | NREventA5 | measId:3;ServCellPCI:955;Se... |
| 2024-09-20 22:21:35.976 | NRHandoverAttempt | SourcePCI:955;SourceNR-ARFC... |
| 2024-09-20 22:21:36.017 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.032 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.139 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.139 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255485 | 1 | 12.7122 | 14.5952 | -116.3211 | 6.1553 | 171.3960 | 0.0158 | 0.0094 |
| 2024_09_20 22:00 | 3264987 | 2 | 12.5092 | 17.0030 | -116.2068 | 15.0485 | 186.0132 | 0.0084 | 0.0034 |
| 2024_09_20 22:00 | 3211408 | 3 | 8.1480 | 7.3011 | -115.9769 | 7.0928 | 118.9202 | 0.0004 | 0.0137 |
| 2024_09_20 22:00 | 3259488 | 4 | 19.1977 | 10.9232 | -114.7376 | 18.3865 | 188.2406 | 0.0175 | 0.0171 |
| 2024_09_20 22:00 | 3274882 | 5 | 12.8245 | 18.8165 | -115.8587 | 15.0479 | 196.4800 | 0.0009 | 0.0120 |
| 2024_09_20 22:00 | 3216318 | 6 | 13.0517 | 8.4104 | -115.7776 | 7.6103 | 141.9017 | 0.0145 | 0.0145 |
| 2024_09_20 22:00 | 3268165 | 7 | 11.7807 | 7.4286 | -115.2383 | 3.2263 | 27.9247 | 0.0052 | 0.0049 |
| 2024_09_20 22:00 | 3222394 | 8 | 15.6979 | 15.1587 | -114.2072 | 4.2246 | 44.1826 | 0.0160 | 0.0118 |
| 2024_09_20 22:00 | 3267122 | 9 | 9.1046 | 13.0433 | -115.1613 | 3.6198 | 43.6023 | 0.0133 | 0.0069 |
| 2024_09_20 22:00 | 3231518 | 10 | 15.0222 | 11.7311 | -114.6826 | 3.1508 | 58.8693 | 0.0053 | 0.0098 |
| 2024_09_20 22:00 | 3258888 | 11 | 18.8670 | 6.9932 | -116.3596 | 4.3007 | 41.6132 | 0.0200 | 0.0005 |
| 2024_09_20 22:00 | 3263322 | 12 | 8.1513 | 16.8760 | -117.2821 | 3.6008 | 52.7786 | 0.0002 | 0.0116 |
| 2024_09_20 22:00 | 3233502 | 13 | 9.0088 | 18.2324 | -115.3215 | 4.1785 | 22.8108 | 0.0195 | 0.0002 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412433_5CF6FA38 | 504990 | 218 | -96.3 | 504990 | 75 | -96.7 | 504990 | 980 | -101.1 | 504990 | 242 |
| MR_1774412433_E0E9B4C5 | 152650 | 940 | -94.6 | 152650 | 920 | -97.6 | 152650 | 34 | -102.7 | 152650 | 149 |
| MR_1774412433_60DD638B | 152650 | 940 | -94.1 | 152650 | 920 | -98.3 | 152650 | 34 | -103.5 | 152650 | 149 |
| MR_1774412433_87A5A7CA | 504990 | 218 | -93.9 | 504990 | 75 | -97.0 | 504990 | 980 | -97.5 | 504990 | 242 |
| MR_1774412433_41775975 | 152650 | 940 | -92.2 | 152650 | 920 | -95.4 | 152650 | 34 | -104.2 | 152650 | 149 |

> *... 2개 열 생략 (전체 14열)*

---
