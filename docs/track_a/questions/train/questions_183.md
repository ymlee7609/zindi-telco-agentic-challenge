# Track A 문제 분석 — train[1820]~train[1829]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1820] ~ train[1829] (10개)

## 목차

1. [문제 1820: `787b6231-a64...`](#1820) — single-answer, 정답: C19
2. [문제 1821: `5fe35268-565...`](#1821) — single-answer, 정답: C20
3. [문제 1822: `572eb5b6-b40...`](#1822) — single-answer, 정답: C21
4. [문제 1823: `6ba37d0e-dfb...`](#1823) — single-answer, 정답: C11
5. [문제 1824: `61060449-38a...`](#1824) — single-answer, 정답: C18
6. [문제 1825: `5d554e93-620...`](#1825) — single-answer, 정답: C22
7. [문제 1826: `e0a394de-2dd...`](#1826) — single-answer, 정답: C20
8. [문제 1827: `bffbef23-286...`](#1827) — single-answer, 정답: C17
9. [문제 1828: `7517a457-982...`](#1828) — single-answer, 정답: C8
10. [문제 1829: `745594d1-8d5...`](#1829) — single-answer, 정답: C5

---

### 문제 1820: `787b6231-a64...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `787b6231-a64d-40d8-a4f3-3f6d0afa06ae` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Lift the tilt angle  of 3247251_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1820] topology](images/train_1820.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245514_4
- `C2`: Decrease transmission power for 3237102_2
- `C3`: Increase A3 Offset threshold for 3245514_4
- `C4`: Decrease transmission power for 3245514_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237102_2
- `C6`: Press down the tilt angle  of 3247251_1 by 10 degrees
- `C7`: Add neighbor relationship between 3237102_2 and 3245514_4
- `C8`: Decrease A3 Offset threshold for 3237102_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245514_4
- `C10`: Adjust the azimuth of 3237102_2 by 9 degrees
- `C11`: Lift the tilt angle of 3237102_2 by 5 degrees
- `C12`: Increase transmission power for 3237102_2
- `C13`: Press down the tilt angle of 3237102_2 by 5 degrees
- `C14`: Add neighbor relationship between 3247251_1 and 3245514_4
- `C15`: Increase A3 Offset threshold for 3237102_2
- `C16`: Increase transmission power for 3245514_4
- `C17`: Check test server and transmission issues
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Lift the tilt angle  of 3247251_1 by 10 degrees **← 정답**
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237102_2
- `C21`: Adjust the azimuth of 3247251_1 by 49 degrees
- `C22`: Decrease A3 Offset threshold for 3245514_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.173 | MS1 | 121.4656660197 | 31.1446232935 | 26 | 504990 | -85.72 | 13.07 | 589.49 | 0.19 | 2.07 | 1598 |
| 2024-09-20 22:21:32.651 | MS1 | 121.4656623275 | 31.1446239967 | 26 | 504990 | -89.13 | 15.27 | 586.21 | 0.05 | 2.74 | 1571 |
| 2024-09-20 22:21:33.670 | MS1 | 121.4656764744 | 31.1446235743 | 26 | 504990 | -89.42 | 15.64 | 576.80 | 0.19 | 2.14 | 1588 |
| 2024-09-20 22:21:34.534 | MS1 | 121.4656615212 | 31.1446214285 | 26 | 504990 | -85.05 | 15.70 | 65.45 | 0.03 | 2.17 | 1584 |
| 2024-09-20 22:21:35.595 | MS1 | 121.4656775719 | 31.1446215389 | 26 | 504990 | -86.59 | 12.53 | 70.42 | 0.04 | 2.99 | 1588 |
| 2024-09-20 22:21:36.291 | MS1 | 121.4656612078 | 31.1446259868 | 26 | 504990 | -90.07 | 12.20 | 66.51 | 0.09 | 2.56 | 1591 |
| 2024-09-20 22:21:37.343 | MS1 | 121.4656589535 | 31.1446239433 | 26 | 504990 | -91.92 | 9.02 | 90.82 | 0.11 | 2.95 | 1587 |
| 2024-09-20 22:21:38.905 | MS1 | 121.4656670442 | 31.1446192453 | 26 | 504990 | -93.33 | 12.49 | 59.08 | 0.15 | 2.45 | 1561 |
| 2024-09-20 22:21:39.435 | MS1 | 121.4656683043 | 31.1446260819 | 26 | 504990 | -89.44 | 7.00 | 71.46 | 0.18 | 2.93 | 1572 |
| 2024-09-20 22:21:40.157 | MS1 | 121.4656636623 | 31.1446375901 | 26 | 504990 | -93.54 | 12.71 | 400.87 | 0.14 | 2.10 | 1577 |
| 2024-09-20 22:21:41.822 | MS1 | 121.4656707927 | 31.1446291983 | 26 | 504990 | -89.03 | 10.53 | 311.73 | 0.04 | 2.93 | 1571 |
| 2024-09-20 22:21:42.772 | MS1 | 121.4656769701 | 31.1446231200 | 26 | 504990 | -91.87 | 7.84 | 396.07 | 0.18 | 2.69 | 1574 |

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
| 3237102 | 2 | 121.4755873052 | 31.1451435353 | 275 | 2 | 9 | 46.9 | TDD | 26 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3245514 | 4 | 121.4727829689 | 31.1530998635 | 265 | 12 | 0 | 27.9 | TDD | 503 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3247251 | 1 | 121.4712058113 | 31.1460111658 | 101 | 15 | 4 | 42.0 | TDD | 993 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3270706 | 3 | 121.4684853407 | 31.1469904717 | 151 | 4 | 11 | 38.0 | TDD | 996 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.900 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.917 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.061 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.061 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.749 | NREventA3 | measId:2;ServCellPCI:835;Se... |
| 2024-09-20 22:21:37.989 | NRHandoverAttempt | SourcePCI:835;SourceNR-ARFC... |
| 2024-09-20 22:21:38.031 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.044 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.169 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.169 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247251 | 1 | 6.7934 | 18.0893 | -115.1671 | 7.1888 | 150.1175 | 0.0105 | 0.0198 |
| 2024_09_20 22:00 | 3237102 | 2 | 88.9869 | 86.2443 | -114.7098 | 19.9828 | 140.4436 | 0.0151 | 0.0004 |
| 2024_09_20 22:00 | 3270706 | 3 | 18.3251 | 7.2247 | -117.6552 | 10.7634 | 95.7525 | 0.0012 | 0.0150 |
| 2024_09_20 22:00 | 3245514 | 4 | 8.3416 | 19.8403 | -116.0724 | 8.1498 | 116.4255 | 0.0139 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413651_B0C6D0D9 | 504990 | 26 | -83.5 | 504990 | 503 | -95.5 | 504990 | 993 | -95.3 | 504990 | 996 |
| MR_1774413651_813133FF | 504990 | 26 | -86.5 | 504990 | 503 | -96.3 | 504990 | 993 | -97.8 | 504990 | 996 |
| MR_1774413651_8DDCA27A | 504990 | 26 | -84.0 | 504990 | 503 | -94.6 | 504990 | 993 | -99.1 | 504990 | 996 |
| MR_1774413651_7D626E71 | 504990 | 26 | -85.1 | 504990 | 503 | -96.9 | 504990 | 993 | -96.1 | 504990 | 996 |
| MR_1774413651_AE542097 | 504990 | 26 | -83.5 | 504990 | 503 | -95.2 | 504990 | 993 | -96.6 | 504990 | 996 |
| MR_1774413651_C47DE8D4 | 504990 | 26 | -86.4 | 504990 | 503 | -96.9 | 504990 | 993 | -99.1 | 504990 | 996 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1821: `5fe35268-565...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5fe35268-5657-401b-92b6-507a615004db` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3249474_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1821] topology](images/train_1821.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3236172_1 by 10 degrees
- `C2`: Increase A3 Offset threshold for 3236172_1
- `C3`: Press down the tilt angle of 3249474_3 by 6 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236172_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249474_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236172_1
- `C7`: Press down the tilt angle  of 3236172_1 by 10 degrees
- `C8`: Lift the tilt angle of 3249474_3 by 6 degrees
- `C9`: Decrease A3 Offset threshold for 3236172_1
- `C10`: Add neighbor relationship between 3245445_2 and 3236172_1
- `C11`: Decrease A3 Offset threshold for 3249474_3
- `C12`: Add neighbor relationship between 3249474_3 and 3236172_1
- `C13`: Decrease transmission power for 3249474_3
- `C14`: Increase transmission power for 3236172_1
- `C15`: Adjust the azimuth of 3236172_1 by 50 degrees
- `C16`: Adjust the azimuth of 3249474_3 by 27 degrees
- `C17`: Check test server and transmission issues
- `C18`: Increase A3 Offset threshold for 3249474_3
- `C19`: Increase transmission power for 3249474_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249474_3 **← 정답**
- `C21`: Decrease transmission power for 3236172_1
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.320 | MS1 | 121.4656733328 | 31.1446319705 | 701 | 504990 | -90.94 | 16.75 | 493.79 | 0.17 | 2.64 | 1571 |
| 2024-09-20 22:21:32.905 | MS1 | 121.4656613351 | 31.1446355578 | 701 | 504990 | -91.10 | 12.66 | 423.22 | 0.03 | 2.38 | 1589 |
| 2024-09-20 22:21:33.184 | MS1 | 121.4656594175 | 31.1446285070 | 701 | 504990 | -91.20 | 15.78 | 583.30 | 0.06 | 2.65 | 1575 |
| 2024-09-20 22:21:34.538 | MS1 | 121.4656670423 | 31.1446234451 | 701 | 504990 | -86.08 | 12.53 | 81.11 | 0.64 | 2.73 | 689 |
| 2024-09-20 22:21:35.737 | MS1 | 121.4656748617 | 31.1446246112 | 701 | 504990 | -85.17 | 12.39 | 80.40 | 0.62 | 2.79 | 580 |
| 2024-09-20 22:21:36.163 | MS1 | 121.4656686723 | 31.1446299961 | 701 | 504990 | -87.16 | 17.46 | 81.61 | 0.61 | 2.76 | 500 |
| 2024-09-20 22:21:37.146 | MS1 | 121.4656747174 | 31.1446188363 | 701 | 504990 | -93.37 | 11.84 | 75.09 | 0.60 | 2.38 | 651 |
| 2024-09-20 22:21:38.779 | MS1 | 121.4656716336 | 31.1446242758 | 701 | 504990 | -89.55 | 12.45 | 93.63 | 0.65 | 2.35 | 510 |
| 2024-09-20 22:21:39.128 | MS1 | 121.4656686909 | 31.1446235367 | 701 | 504990 | -90.85 | 11.19 | 75.14 | 0.61 | 2.31 | 520 |
| 2024-09-20 22:21:40.665 | MS1 | 121.4656699488 | 31.1446273824 | 701 | 504990 | -90.65 | 10.71 | 566.16 | 0.15 | 2.03 | 1581 |
| 2024-09-20 22:21:41.400 | MS1 | 121.4656757858 | 31.1446195356 | 701 | 504990 | -91.98 | 12.00 | 380.67 | 0.08 | 2.35 | 1598 |
| 2024-09-20 22:21:42.926 | MS1 | 121.4656739554 | 31.1446246271 | 701 | 504990 | -90.69 | 9.64 | 322.91 | 0.01 | 2.11 | 1581 |

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
| 3236172 | 1 | 121.4662685853 | 31.1466847160 | 274 | 8 | 8 | 46.0 | TDD | 744 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3239965 | 4 | 121.4646199401 | 31.1478074870 | 244 | 10 | 4 | 36.4 | TDD | 598 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3245445 | 2 | 121.4742390198 | 31.1449943022 | 104 | 10 | 2 | 19.6 | TDD | 905 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3249474 | 3 | 121.4755736186 | 31.1537703479 | 250 | 4 | 12 | 43.3 | TDD | 701 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.594 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.711 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.711 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.397 | NREventA3 | measId:2;ServCellPCI:940;Se... |
| 2024-09-20 22:21:38.637 | NRHandoverAttempt | SourcePCI:940;SourceNR-ARFC... |
| 2024-09-20 22:21:38.677 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.689 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.821 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.821 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236172 | 1 | 15.0130 | 14.5081 | -117.1722 | 14.2485 | 142.1267 | 0.0067 | 0.0051 |
| 2024_09_20 22:00 | 3245445 | 2 | 17.1013 | 10.9110 | -114.0954 | 7.2840 | 94.6037 | 0.0147 | 0.0177 |
| 2024_09_20 22:00 | 3249474 | 3 | 19.0638 | 15.3859 | -117.9120 | 12.4984 | 148.9384 | 0.0173 | 0.0133 |
| 2024_09_20 22:00 | 3239965 | 4 | 13.9988 | 19.0748 | -114.4575 | 11.0056 | 131.1846 | 0.0040 | 0.0052 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412716_5846797E | 504990 | 701 | -86.1 | 504990 | 744 | -86.2 | 504990 | 905 | -94.0 | 504990 | 598 |
| MR_1774412716_42547F70 | 504990 | 701 | -87.7 | 504990 | 744 | -88.2 | 504990 | 905 | -91.5 | 504990 | 598 |
| MR_1774412716_E3B06B5F | 504990 | 701 | -85.4 | 504990 | 744 | -87.5 | 504990 | 905 | -94.2 | 504990 | 598 |
| MR_1774412716_4A5A01F4 | 504990 | 701 | -85.3 | 504990 | 744 | -86.6 | 504990 | 905 | -94.5 | 504990 | 598 |
| MR_1774412716_17B20B97 | 504990 | 701 | -87.4 | 504990 | 744 | -87.0 | 504990 | 905 | -90.9 | 504990 | 598 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1822: `572eb5b6-b40...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `572eb5b6-b407-408c-9b81-f21366db4b50` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Add neighbor relationship between 3242532_3 and 3279234_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1822] topology](images/train_1822.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3279234_2
- `C2`: Press down the tilt angle  of 3279234_2 by 3 degrees
- `C3`: Add neighbor relationship between 3276461_1 and 3279234_2
- `C4`: Check test server and transmission issues
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279234_2
- `C6`: Increase transmission power for 3242532_3
- `C7`: Adjust the azimuth of 3242532_3 by 30 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242532_3
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279234_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242532_3
- `C12`: Lift the tilt angle  of 3279234_2 by 3 degrees
- `C13`: Decrease transmission power for 3242532_3
- `C14`: Increase transmission power for 3279234_2
- `C15`: Press down the tilt angle of 3242532_3 by 7 degrees
- `C16`: Increase A3 Offset threshold for 3242532_3
- `C17`: Decrease A3 Offset threshold for 3242532_3
- `C18`: Decrease A3 Offset threshold for 3279234_2
- `C19`: Lift the tilt angle of 3242532_3 by 7 degrees
- `C20`: Adjust the azimuth of 3279234_2 by 2 degrees
- `C21`: Add neighbor relationship between 3242532_3 and 3279234_2 **← 정답**
- `C22`: Decrease transmission power for 3279234_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.290 | MS1 | 121.4656698278 | 31.1446364748 | 613 | 504990 | -84.70 | 14.44 | 527.06 | 0.17 | 2.46 | 1567 |
| 2024-09-20 22:21:32.264 | MS1 | 121.4656623489 | 31.1446260520 | 613 | 504990 | -77.89 | 17.20 | 457.14 | 0.02 | 2.39 | 1560 |
| 2024-09-20 22:21:33.656 | MS1 | 121.4656580321 | 31.1446225399 | 613 | 504990 | -75.55 | 12.48 | 352.21 | 0.09 | 2.94 | 1569 |
| 2024-09-20 22:21:34.753 | MS1 | 121.4656616478 | 31.1446318309 | 613 | 504990 | -86.14 | -1.97 | 29.72 | 0.13 | 1.49 | 1583 |
| 2024-09-20 22:21:35.539 | MS1 | 121.4656775225 | 31.1446263605 | 613 | 504990 | -88.43 | -1.03 | 64.57 | 0.11 | 1.44 | 1561 |
| 2024-09-20 22:21:36.589 | MS1 | 121.4656746397 | 31.1446305916 | 613 | 504990 | -85.52 | -0.19 | 60.65 | 0.05 | 1.30 | 1590 |
| 2024-09-20 22:21:37.214 | MS1 | 121.4656749568 | 31.1446360605 | 613 | 504990 | -92.42 | -1.30 | 65.24 | 0.11 | 1.38 | 1594 |
| 2024-09-20 22:21:38.965 | MS1 | 121.4656761007 | 31.1446355022 | 613 | 504990 | -75.32 | 12.81 | 379.24 | 0.10 | 1.05 | 1572 |
| 2024-09-20 22:21:39.759 | MS1 | 121.4656734128 | 31.1446318056 | 613 | 504990 | -77.56 | 13.54 | 462.04 | 0.18 | 1.14 | 1597 |
| 2024-09-20 22:21:40.705 | MS1 | 121.4656594122 | 31.1446192936 | 613 | 504990 | -82.38 | 17.16 | 302.49 | 0.04 | 2.92 | 1563 |
| 2024-09-20 22:21:41.692 | MS1 | 121.4656696622 | 31.1446308165 | 613 | 504990 | -79.43 | 14.43 | 501.52 | 0.01 | 2.32 | 1562 |
| 2024-09-20 22:21:42.887 | MS1 | 121.4656653265 | 31.1446356575 | 613 | 504990 | -79.72 | 15.48 | 552.37 | 0.13 | 2.22 | 1567 |

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
| 3237356 | 4 | 121.4699595463 | 31.1443764579 | 157 | 1 | 0 | 45.4 | TDD | 743 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3242532 | 3 | 121.4711090111 | 31.1458058398 | 226 | 3 | 5 | 35.6 | TDD | 613 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3276461 | 1 | 121.4655534744 | 31.1557769192 | 354 | 13 | 12 | 37.5 | TDD | 57 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3279234 | 2 | 121.4684113037 | 31.1528426182 | 198 | 1 | 10 | 28.8 | TDD | 908 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.264 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.368 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.368 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.086 | NREventA3 | measId:2;ServCellPCI:16;Ser... |
| 2024-09-20 22:21:36.086 | NREventA3 | measId:2;ServCellPCI:16;Ser... |
| 2024-09-20 22:21:37.086 | NREventA3 | measId:2;ServCellPCI:16;Ser... |
| 2024-09-20 22:21:39.586 | NRRRCReestablishAttempt | PCI:16 |
| 2024-09-20 22:21:39.597 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.609 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.730 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.730 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276461 | 1 | 10.3126 | 7.9624 | -115.7960 | 16.7427 | 166.8856 | 0.0010 | 0.0005 |
| 2024_09_20 22:00 | 3279234 | 2 | 10.4791 | 14.0517 | -114.6356 | 16.6878 | 96.2043 | 0.0083 | 0.0029 |
| 2024_09_20 22:00 | 3242532 | 3 | 5.8453 | 8.4446 | -116.5519 | 7.5065 | 90.9805 | 0.0151 | 0.1297 |
| 2024_09_20 22:00 | 3237356 | 4 | 8.7734 | 8.3711 | -116.6002 | 19.6748 | 114.1745 | 0.0128 | 0.0068 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415850_BAB28E74 | 504990 | 613 | -84.4 | 504990 | 908 | -79.7 | 504990 | 57 | -87.2 | 504990 | 743 |
| MR_1774415850_8B685D3B | 504990 | 613 | -87.2 | 504990 | 908 | -80.2 | 504990 | 57 | -88.0 | 504990 | 743 |
| MR_1774415850_11281A84 | 504990 | 908 | -83.2 | 504990 | 613 | -84.8 | 504990 | 57 | -87.0 | 504990 | 743 |
| MR_1774415850_5BB77ABF | 504990 | 613 | -86.9 | 504990 | 908 | -82.7 | 504990 | 57 | -87.4 | 504990 | 743 |
| MR_1774415850_DBD9C7C6 | 504990 | 613 | -84.9 | 504990 | 908 | -81.7 | 504990 | 57 | -86.9 | 504990 | 743 |
| MR_1774415850_B3E452AC | 504990 | 613 | -85.8 | 504990 | 908 | -82.6 | 504990 | 57 | -88.0 | 504990 | 743 |
| MR_1774415850_DDD7D9BE | 504990 | 613 | -87.8 | 504990 | 908 | -79.8 | 504990 | 57 | -87.7 | 504990 | 743 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1823: `6ba37d0e-dfb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6ba37d0e-dfbf-4143-9d65-bc71ef47b7b0` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220347_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1823] topology](images/train_1823.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3220347_4
- `C2`: Adjust the azimuth of 3230800_1 by 40 degrees
- `C3`: Increase A3 Offset threshold for 3230800_1
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Add neighbor relationship between 3226119_9 and 3230800_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230800_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230800_1
- `C8`: Lift the tilt angle  of 3230800_1 by 1 degrees
- `C9`: Decrease A3 Offset threshold for 3220347_4
- `C10`: Increase transmission power for 3220347_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220347_4 **← 정답**
- `C12`: Decrease transmission power for 3230800_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220347_4
- `C14`: Press down the tilt angle  of 3230800_1 by 1 degrees
- `C15`: Decrease A3 Offset threshold for 3230800_1
- `C16`: Increase transmission power for 3230800_1
- `C17`: Add neighbor relationship between 3220347_4 and 3230800_1
- `C18`: Check test server and transmission issues
- `C19`: Adjust the azimuth of 3220347_4 by 46 degrees
- `C20`: Decrease transmission power for 3220347_4
- `C21`: Press down the tilt angle of 3220347_4 by 5 degrees
- `C22`: Lift the tilt angle of 3220347_4 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.668 | MS1 | 121.4656704595 | 31.1446191018 | 308 | 504990 | -93.50 | 11.81 | 370.80 | 0.05 | 2.49 | 1584 |
| 2024-09-20 22:21:32.502 | MS1 | 121.4656691263 | 31.1446260414 | 694 | 504990 | -93.21 | 14.87 | 385.33 | 0.19 | 2.55 | 1599 |
| 2024-09-20 22:21:33.601 | MS1 | 121.4656657159 | 31.1446371812 | 713 | 504990 | -95.67 | 13.60 | 325.13 | 0.17 | 2.09 | 1587 |
| 2024-09-20 22:21:34.173 | MS1 | 121.4656665324 | 31.1446255925 | 407 | 152650 | -91.82 | 5.55 | 79.83 | 0.11 | 1.73 | 937 |
| 2024-09-20 22:21:35.318 | MS1 | 121.4656590219 | 31.1446274204 | 636 | 152650 | -88.03 | 5.50 | 45.40 | 0.03 | 1.70 | 941 |
| 2024-09-20 22:21:36.659 | MS1 | 121.4656645599 | 31.1446227665 | 202 | 152650 | -96.91 | 7.97 | 95.72 | 0.17 | 1.85 | 961 |
| 2024-09-20 22:21:37.550 | MS1 | 121.4656742994 | 31.1446205006 | 631 | 152650 | -95.89 | 7.37 | 93.00 | 0.11 | 1.90 | 977 |
| 2024-09-20 22:21:38.345 | MS1 | 121.4656723904 | 31.1446304727 | 407 | 152650 | -92.34 | 5.21 | 98.55 | 0.14 | 1.55 | 942 |
| 2024-09-20 22:21:39.523 | MS1 | 121.4656613500 | 31.1446230591 | 636 | 152650 | -95.08 | 6.47 | 80.48 | 0.01 | 1.97 | 982 |
| 2024-09-20 22:21:40.389 | MS1 | 121.4656674813 | 31.1446208702 | 202 | 152650 | -90.24 | 4.81 | 81.37 | 0.12 | 2.58 | 1576 |
| 2024-09-20 22:21:41.445 | MS1 | 121.4656584361 | 31.1446290035 | 631 | 152650 | -89.79 | 3.38 | 73.39 | 0.20 | 2.73 | 1595 |
| 2024-09-20 22:21:42.585 | MS1 | 121.4656674319 | 31.1446346488 | 407 | 152650 | -88.46 | 3.06 | 89.23 | 0.18 | 2.92 | 1565 |

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
| 3220347 | 4 | 121.4676534847 | 31.1474430528 | 257 | 0 | 10 | 29.6 | TDD | 308 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3226119 | 9 | 121.4664729340 | 31.1506411774 | 84 | 5 | 1 | 14.1 | FDD | 202 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3226296 | 2 | 121.4645464059 | 31.1453169601 | 143 | 14 | 5 | 1.3 | TDD | 713 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3227955 | 8 | 121.4685458245 | 31.1544564362 | 25 | 6 | 8 | 20.5 | FDD | 803 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3230800 | 1 | 121.4688293313 | 31.1525210221 | 159 | 1 | 9 | 4.4 | TDD | 224 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3232987 | 5 | 121.4664915525 | 31.1548781526 | 56 | 2 | 4 | 11.1 | TDD | 694 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3239455 | 3 | 121.4686736156 | 31.1503549565 | 75 | 1 | 10 | 2.4 | TDD | 298 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3241890 | 6 | 121.4697697139 | 31.1524039457 | 185 | 11 | 5 | 22.7 | TDD | 539 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3247318 | 13 | 121.4743929776 | 31.1463575328 | 325 | 14 | 10 | 23.9 | FDD | 636 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3256269 | 12 | 121.4658956588 | 31.1524700369 | 104 | 10 | 7 | 8.9 | FDD | 631 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3272577 | 10 | 121.4663111115 | 31.1453238207 | 350 | 2 | 9 | 4.4 | FDD | 623 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3272635 | 7 | 121.4742871244 | 31.1452452855 | 277 | 12 | 12 | 13.9 | FDD | 407 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3274488 | 11 | 121.4737198308 | 31.1494974707 | 181 | 1 | 12 | 13.1 | FDD | 533 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |

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
| 2024-09-20 22:21:31.308 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.325 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.439 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.439 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.164 | NREventA2 | measId:1;ServCellPCI:937;Se... |
| 2024-09-20 22:21:35.292 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.511 | NREventA5 | measId:3;ServCellPCI:937;Se... |
| 2024-09-20 22:21:35.574 | NRHandoverAttempt | SourcePCI:937;SourceNR-ARFC... |
| 2024-09-20 22:21:35.607 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.617 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.761 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.761 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230800 | 1 | 7.0502 | 14.3803 | -114.8428 | 16.0009 | 192.6508 | 0.0151 | 0.0191 |
| 2024_09_20 22:00 | 3226296 | 2 | 6.7684 | 9.4439 | -114.2929 | 10.6195 | 183.8320 | 0.0000 | 0.0016 |
| 2024_09_20 22:00 | 3239455 | 3 | 7.4615 | 12.9040 | -116.9527 | 9.3857 | 116.6358 | 0.0163 | 0.0110 |
| 2024_09_20 22:00 | 3220347 | 4 | 8.3806 | 15.0014 | -114.8145 | 11.0137 | 91.3294 | 0.0029 | 0.0059 |
| 2024_09_20 22:00 | 3232987 | 5 | 6.3687 | 7.1372 | -117.8898 | 12.6865 | 112.1203 | 0.0040 | 0.0136 |
| 2024_09_20 22:00 | 3241890 | 6 | 17.1793 | 19.6883 | -116.8035 | 18.4303 | 143.2351 | 0.0028 | 0.0015 |
| 2024_09_20 22:00 | 3272635 | 7 | 15.2095 | 7.7602 | -115.0164 | 4.8635 | 54.0221 | 0.0113 | 0.0121 |
| 2024_09_20 22:00 | 3227955 | 8 | 8.1526 | 13.6024 | -114.5366 | 4.2647 | 52.9355 | 0.0037 | 0.0093 |
| 2024_09_20 22:00 | 3226119 | 9 | 14.0797 | 10.1299 | -114.5843 | 4.6789 | 54.6030 | 0.0134 | 0.0021 |
| 2024_09_20 22:00 | 3272577 | 10 | 14.2992 | 15.4442 | -116.0407 | 4.1813 | 36.3917 | 0.0187 | 0.0114 |
| 2024_09_20 22:00 | 3274488 | 11 | 18.1961 | 18.0138 | -117.6200 | 3.7458 | 54.5451 | 0.0198 | 0.0185 |
| 2024_09_20 22:00 | 3256269 | 12 | 16.8484 | 18.1100 | -114.4623 | 4.7327 | 56.8502 | 0.0007 | 0.0028 |
| 2024_09_20 22:00 | 3247318 | 13 | 12.6914 | 18.3395 | -116.4589 | 4.1253 | 29.1848 | 0.0125 | 0.0127 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416992_1FA0240A | 152650 | 407 | -92.2 | 152650 | 803 | -98.6 | 152650 | 533 | -99.4 | 152650 | 623 |
| MR_1774416992_6F2BC651 | 152650 | 407 | -91.8 | 152650 | 803 | -98.2 | 152650 | 533 | -100.3 | 152650 | 623 |
| MR_1774416992_05E38080 | 504990 | 713 | -96.4 | 504990 | 224 | -94.7 | 504990 | 539 | -93.6 | 504990 | 298 |
| MR_1774416992_81E68CDC | 504990 | 713 | -97.2 | 504990 | 224 | -93.8 | 504990 | 539 | -95.5 | 504990 | 298 |
| MR_1774416992_A39E33DC | 504990 | 713 | -95.2 | 504990 | 224 | -91.9 | 504990 | 539 | -97.0 | 504990 | 298 |
| MR_1774416992_E599BED1 | 504990 | 713 | -94.3 | 504990 | 224 | -94.5 | 504990 | 539 | -95.3 | 504990 | 298 |
| MR_1774416992_26FBF9DE | 152650 | 407 | -92.1 | 152650 | 803 | -98.8 | 152650 | 533 | -102.6 | 152650 | 623 |
| MR_1774416992_6D13F32A | 504990 | 713 | -95.4 | 504990 | 224 | -93.7 | 504990 | 539 | -95.3 | 504990 | 298 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1824: `61060449-38a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `61060449-38a3-4121-84f2-e97b232d640f` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Add neighbor relationship between 3235487_4 and 3228066_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1824] topology](images/train_1824.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3235487_4 by 10 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228066_3
- `C3`: Lift the tilt angle  of 3228066_3 by 5 degrees
- `C4`: Check test server and transmission issues
- `C5`: Press down the tilt angle  of 3228066_3 by 5 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228066_3
- `C7`: Adjust the azimuth of 3228066_3 by 18 degrees
- `C8`: Increase transmission power for 3235487_4
- `C9`: Decrease transmission power for 3228066_3
- `C10`: Increase A3 Offset threshold for 3228066_3
- `C11`: Decrease A3 Offset threshold for 3228066_3
- `C12`: Add neighbor relationship between 3251163_1 and 3228066_3
- `C13`: Adjust the azimuth of 3235487_4 by 50 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235487_4
- `C15`: Press down the tilt angle of 3235487_4 by 10 degrees
- `C16`: Decrease transmission power for 3235487_4
- `C17`: Increase A3 Offset threshold for 3235487_4
- `C18`: Add neighbor relationship between 3235487_4 and 3228066_3 **← 정답**
- `C19`: Decrease A3 Offset threshold for 3235487_4
- `C20`: Increase transmission power for 3228066_3
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235487_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.912 | MS1 | 121.4656728237 | 31.1446254404 | 947 | 504990 | -78.87 | 14.83 | 586.68 | 0.12 | 3.00 | 1587 |
| 2024-09-20 22:21:32.765 | MS1 | 121.4656648597 | 31.1446266901 | 947 | 504990 | -81.62 | 15.11 | 425.57 | 0.16 | 2.32 | 1591 |
| 2024-09-20 22:21:33.597 | MS1 | 121.4656728651 | 31.1446262160 | 947 | 504990 | -80.32 | 13.68 | 587.44 | 0.14 | 2.17 | 1599 |
| 2024-09-20 22:21:34.670 | MS1 | 121.4656734110 | 31.1446228491 | 947 | 504990 | -91.19 | -3.54 | 50.58 | 0.13 | 1.17 | 1592 |
| 2024-09-20 22:21:35.976 | MS1 | 121.4656639419 | 31.1446298899 | 947 | 504990 | -87.99 | -1.76 | 66.18 | 0.11 | 1.40 | 1595 |
| 2024-09-20 22:21:36.772 | MS1 | 121.4656657561 | 31.1446266980 | 947 | 504990 | -93.14 | -3.67 | 52.03 | 0.10 | 1.38 | 1579 |
| 2024-09-20 22:21:37.891 | MS1 | 121.4656746923 | 31.1446312477 | 947 | 504990 | -89.22 | -0.61 | 64.58 | 0.07 | 1.05 | 1583 |
| 2024-09-20 22:21:38.352 | MS1 | 121.4656655970 | 31.1446360847 | 947 | 504990 | -75.68 | 13.42 | 425.38 | 0.01 | 1.37 | 1599 |
| 2024-09-20 22:21:39.202 | MS1 | 121.4656584935 | 31.1446242368 | 947 | 504990 | -78.04 | 15.10 | 469.07 | 0.01 | 1.29 | 1600 |
| 2024-09-20 22:21:40.328 | MS1 | 121.4656640385 | 31.1446207048 | 947 | 504990 | -80.16 | 16.50 | 489.54 | 0.13 | 2.02 | 1590 |
| 2024-09-20 22:21:41.259 | MS1 | 121.4656745034 | 31.1446270087 | 947 | 504990 | -83.79 | 17.48 | 317.25 | 0.03 | 2.09 | 1592 |
| 2024-09-20 22:21:42.910 | MS1 | 121.4656694763 | 31.1446305079 | 947 | 504990 | -82.80 | 12.35 | 372.21 | 0.18 | 2.07 | 1586 |

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
| 3228066 | 3 | 121.4698060160 | 31.1491249607 | 236 | 3 | 9 | 19.9 | TDD | 291 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3235487 | 4 | 121.4699272650 | 31.1443100090 | 73 | 13 | 3 | 17.1 | TDD | 947 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3251163 | 1 | 121.4738216869 | 31.1509558257 | 273 | 13 | 6 | 15.0 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3265506 | 2 | 121.4732295384 | 31.1551994455 | 290 | 15 | 6 | 18.0 | TDD | 117 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.341 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.488 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.488 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.151 | NREventA3 | measId:2;ServCellPCI:988;Se... |
| 2024-09-20 22:21:36.151 | NREventA3 | measId:2;ServCellPCI:988;Se... |
| 2024-09-20 22:21:37.151 | NREventA3 | measId:2;ServCellPCI:988;Se... |
| 2024-09-20 22:21:39.651 | NRRRCReestablishAttempt | PCI:988 |
| 2024-09-20 22:21:39.671 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.681 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.825 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.825 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251163 | 1 | 10.0749 | 9.1657 | -114.8112 | 15.1814 | 151.0515 | 0.0170 | 0.0080 |
| 2024_09_20 22:00 | 3265506 | 2 | 19.2010 | 5.5314 | -117.4289 | 19.7218 | 153.1419 | 0.0200 | 0.0181 |
| 2024_09_20 22:00 | 3228066 | 3 | 9.2552 | 8.8245 | -117.8121 | 16.5682 | 109.2633 | 0.0024 | 0.0020 |
| 2024_09_20 22:00 | 3235487 | 4 | 5.6888 | 17.6520 | -114.8406 | 8.6261 | 154.5650 | 0.0075 | 0.1651 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416888_7081A179 | 504990 | 291 | -85.4 | 504990 | 947 | -89.7 | 504990 | 129 | -93.5 | 504990 | 117 |
| MR_1774416888_92827E86 | 504990 | 947 | -92.7 | 504990 | 291 | -85.3 | 504990 | 129 | -91.4 | 504990 | 117 |
| MR_1774416888_8F0110F2 | 504990 | 291 | -86.8 | 504990 | 947 | -92.3 | 504990 | 129 | -90.1 | 504990 | 117 |
| MR_1774416888_207B946D | 504990 | 947 | -89.6 | 504990 | 291 | -85.8 | 504990 | 129 | -90.7 | 504990 | 117 |
| MR_1774416888_CC8F0D89 | 504990 | 291 | -85.1 | 504990 | 947 | -93.0 | 504990 | 129 | -92.1 | 504990 | 117 |
| MR_1774416888_0B196EBD | 504990 | 291 | -86.4 | 504990 | 947 | -92.5 | 504990 | 129 | -92.7 | 504990 | 117 |
| MR_1774416888_E6D341F4 | 504990 | 291 | -87.0 | 504990 | 947 | -92.5 | 504990 | 129 | -90.5 | 504990 | 117 |
| MR_1774416888_ACB44426 | 504990 | 947 | -93.1 | 504990 | 291 | -86.9 | 504990 | 129 | -92.1 | 504990 | 117 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1825: `5d554e93-620...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5d554e93-620c-46d3-b540-fb9aa0ffd495` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1825] topology](images/train_1825.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260621_4
- `C2`: Press down the tilt angle of 3260621_4 by 10 degrees
- `C3`: Decrease A3 Offset threshold for 3260621_4
- `C4`: Increase A3 Offset threshold for 3276023_2
- `C5`: Press down the tilt angle  of 3276023_2 by 10 degrees
- `C6`: Add neighbor relationship between 3217794_1 and 3276023_2
- `C7`: Adjust the azimuth of 3260621_4 by 36 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260621_4
- `C9`: Add neighbor relationship between 3260621_4 and 3276023_2
- `C10`: Decrease A3 Offset threshold for 3276023_2
- `C11`: Decrease transmission power for 3276023_2
- `C12`: Lift the tilt angle of 3260621_4 by 10 degrees
- `C13`: Adjust the azimuth of 3276023_2 by 50 degrees
- `C14`: Increase transmission power for 3260621_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276023_2
- `C16`: Decrease transmission power for 3260621_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276023_2
- `C18`: Increase A3 Offset threshold for 3260621_4
- `C19`: Lift the tilt angle  of 3276023_2 by 10 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase transmission power for 3276023_2
- `C22`: Check test server and transmission issues **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.561 | MS1 | 121.4656617535 | 31.1446258259 | 374 | 504990 | -86.06 | 16.01 | 507.85 | 0.19 | 2.84 | 1575 |
| 2024-09-20 22:21:32.753 | MS1 | 121.4656628037 | 31.1446286263 | 374 | 504990 | -88.25 | 16.73 | 352.74 | 0.03 | 2.38 | 1595 |
| 2024-09-20 22:21:33.909 | MS1 | 121.4656671167 | 31.1446301693 | 374 | 504990 | -86.64 | 12.10 | 365.17 | 0.15 | 2.28 | 1561 |
| 2024-09-20 22:21:34.281 | MS1 | 121.4656669415 | 31.1446268032 | 374 | 504990 | -89.84 | 13.25 | 92.76 | 0.15 | 2.31 | 464 |
| 2024-09-20 22:21:35.641 | MS1 | 121.4656644490 | 31.1446233150 | 374 | 504990 | -85.99 | 16.22 | 92.68 | 0.16 | 2.54 | 419 |
| 2024-09-20 22:21:36.267 | MS1 | 121.4656685599 | 31.1446273546 | 374 | 504990 | -85.14 | 12.68 | 96.51 | 0.14 | 2.57 | 334 |
| 2024-09-20 22:21:37.918 | MS1 | 121.4656664480 | 31.1446257333 | 374 | 504990 | -89.49 | 12.72 | 58.56 | 0.09 | 2.33 | 450 |
| 2024-09-20 22:21:38.102 | MS1 | 121.4656724303 | 31.1446319250 | 374 | 504990 | -92.43 | 8.52 | 61.99 | 0.13 | 2.17 | 373 |
| 2024-09-20 22:21:39.127 | MS1 | 121.4656601665 | 31.1446264869 | 374 | 504990 | -89.05 | 8.62 | 64.09 | 0.10 | 2.33 | 302 |
| 2024-09-20 22:21:40.264 | MS1 | 121.4656669048 | 31.1446331190 | 374 | 504990 | -92.43 | 9.50 | 514.55 | 0.16 | 2.50 | 1599 |
| 2024-09-20 22:21:41.776 | MS1 | 121.4656760002 | 31.1446273048 | 374 | 504990 | -91.76 | 7.13 | 541.52 | 0.14 | 2.45 | 1565 |
| 2024-09-20 22:21:42.133 | MS1 | 121.4656768465 | 31.1446377630 | 374 | 504990 | -90.37 | 10.26 | 297.15 | 0.03 | 2.13 | 1562 |

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
| 3217794 | 1 | 121.4691541567 | 31.1497587431 | 168 | 13 | 12 | 32.1 | TDD | 25 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3247577 | 3 | 121.4692067491 | 31.1533287875 | 77 | 13 | 8 | 25.5 | TDD | 1001 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3260621 | 4 | 121.4653905142 | 31.1489285811 | 213 | 13 | 3 | 36.3 | TDD | 374 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3276023 | 2 | 121.4729673947 | 31.1451960829 | 214 | 8 | 9 | 45.5 | TDD | 13 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.146 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.168 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.311 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.311 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.985 | NREventA3 | measId:2;ServCellPCI:524;Se... |
| 2024-09-20 22:21:38.225 | NRHandoverAttempt | SourcePCI:524;SourceNR-ARFC... |
| 2024-09-20 22:21:38.262 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.273 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.377 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.377 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217794 | 1 | 5.2197 | 14.5356 | -116.3148 | 9.4200 | 182.0210 | 0.0095 | 0.0182 |
| 2024_09_20 22:00 | 3276023 | 2 | 7.9693 | 5.9771 | -117.6850 | 5.8364 | 124.2518 | 0.0059 | 0.0181 |
| 2024_09_20 22:00 | 3247577 | 3 | 5.8624 | 18.3611 | -117.3871 | 7.4864 | 126.5580 | 0.0104 | 0.0135 |
| 2024_09_20 22:00 | 3260621 | 4 | 13.4142 | 8.8516 | -117.2950 | 17.0311 | 131.0471 | 0.0147 | 0.0135 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416234_24959245 | 504990 | 374 | -89.8 | 504990 | 13 | -91.6 | 504990 | 25 | -95.7 | 504990 | 1001 |
| MR_1774416234_9F79ED7C | 504990 | 374 | -91.0 | 504990 | 13 | -91.8 | 504990 | 25 | -96.7 | 504990 | 1001 |
| MR_1774416234_2B7D5CCC | 504990 | 374 | -88.6 | 504990 | 13 | -94.9 | 504990 | 25 | -97.9 | 504990 | 1001 |
| MR_1774416234_66E87F37 | 504990 | 374 | -90.2 | 504990 | 13 | -92.7 | 504990 | 25 | -96.2 | 504990 | 1001 |
| MR_1774416234_C0D44769 | 504990 | 374 | -88.7 | 504990 | 13 | -94.9 | 504990 | 25 | -95.6 | 504990 | 1001 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1826: `e0a394de-2dd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e0a394de-2dd7-4e93-b5f4-dbd42c0d6fd9` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1826] topology](images/train_1826.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3248426_3 by 10 degrees
- `C2`: Adjust the azimuth of 3248426_3 by 50 degrees
- `C3`: Add neighbor relationship between 3259475_2 and 3248426_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248426_3
- `C5`: Decrease A3 Offset threshold for 3248426_3
- `C6`: Press down the tilt angle of 3259475_2 by 10 degrees
- `C7`: Increase transmission power for 3259475_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248426_3
- `C9`: Increase A3 Offset threshold for 3259475_2
- `C10`: Check test server and transmission issues
- `C11`: Lift the tilt angle  of 3248426_3 by 10 degrees
- `C12`: Decrease transmission power for 3248426_3
- `C13`: Add neighbor relationship between 3253197_4 and 3248426_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259475_2
- `C15`: Decrease A3 Offset threshold for 3259475_2
- `C16`: Increase A3 Offset threshold for 3248426_3
- `C17`: Adjust the azimuth of 3259475_2 by 50 degrees
- `C18`: Decrease transmission power for 3259475_2
- `C19`: Lift the tilt angle of 3259475_2 by 10 degrees
- `C20`: Insufficient data; more data is needed for judgment. **← 정답**
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259475_2
- `C22`: Increase transmission power for 3248426_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.662 | MS1 | 121.4656724835 | 31.1446223605 | 985 | 504990 | -88.26 | 13.77 | 409.86 | 0.13 | 2.98 | 1597 |
| 2024-09-20 22:21:32.168 | MS1 | 121.4656664428 | 31.1446374894 | 985 | 504990 | -89.74 | 13.91 | 423.77 | 0.14 | 2.17 | 1581 |
| 2024-09-20 22:21:33.257 | MS1 | 121.4656741493 | 31.1446271560 | 985 | 504990 | -88.15 | 14.20 | 548.95 | 0.18 | 2.75 | 1600 |
| 2024-09-20 22:21:34.231 | MS1 | 121.4656699441 | 31.1446359888 | 985 | 504990 | -86.83 | 15.76 | 78.68 | 0.12 | 2.93 | 1595 |
| 2024-09-20 22:21:35.173 | MS1 | 121.4656696205 | 31.1446266023 | 985 | 504990 | -91.56 | 15.41 | 83.63 | 0.02 | 2.62 | 1565 |
| 2024-09-20 22:21:36.140 | MS1 | 121.4656596465 | 31.1446347769 | 985 | 504990 | -85.52 | 12.85 | 60.65 | 0.12 | 2.17 | 1567 |
| 2024-09-20 22:21:37.831 | MS1 | 121.4656652182 | 31.1446262757 | 985 | 504990 | -89.16 | 10.61 | 100.21 | 0.12 | 2.83 | 1570 |
| 2024-09-20 22:21:38.925 | MS1 | 121.4656616345 | 31.1446272733 | 985 | 504990 | -90.80 | 7.25 | 88.57 | 0.02 | 2.27 | 1570 |
| 2024-09-20 22:21:39.462 | MS1 | 121.4656658865 | 31.1446318080 | 985 | 504990 | -93.35 | 7.92 | 50.41 | 0.01 | 2.07 | 1579 |
| 2024-09-20 22:21:40.410 | MS1 | 121.4656690710 | 31.1446301113 | 985 | 504990 | -91.14 | 11.90 | 391.51 | 0.11 | 2.76 | 1599 |
| 2024-09-20 22:21:41.959 | MS1 | 121.4656667908 | 31.1446321342 | 985 | 504990 | -89.31 | 10.03 | 528.44 | 0.11 | 2.96 | 1600 |
| 2024-09-20 22:21:42.525 | MS1 | 121.4656586023 | 31.1446287491 | 985 | 504990 | -91.04 | 9.71 | 425.75 | 0.14 | 2.23 | 1574 |

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
| 3248426 | 3 | 121.4678547868 | 31.1441297873 | 191 | 8 | 5 | 32.1 | TDD | 673 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3250433 | 1 | 121.4730493923 | 31.1448847854 | 307 | 6 | 2 | 43.6 | TDD | 880 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3253197 | 4 | 121.4742631108 | 31.1531289874 | 326 | 0 | 11 | 27.7 | TDD | 614 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3259475 | 2 | 121.4679009338 | 31.1514867075 | 114 | 10 | 0 | 45.2 | TDD | 985 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.228 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.250 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.353 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.353 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.105 | NREventA3 | measId:2;ServCellPCI:994;Se... |
| 2024-09-20 22:21:38.345 | NRHandoverAttempt | SourcePCI:994;SourceNR-ARFC... |
| 2024-09-20 22:21:38.380 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.392 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.515 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.515 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3250433 | 1 | 89.4027 | 75.6772 | -117.0849 | 7.9325 | 118.4162 | 0.0099 | 0.0027 |
| 2024_09_19 22:00 | 3259475 | 2 | 84.5566 | 85.6397 | -116.7367 | 13.8560 | 135.3159 | 0.0120 | 0.0019 |
| 2024_09_19 22:00 | 3248426 | 3 | 76.6531 | 87.6882 | -114.3596 | 18.8415 | 114.1150 | 0.0036 | 0.0038 |
| 2024_09_19 22:00 | 3253197 | 4 | 83.6403 | 77.9654 | -114.4792 | 11.6895 | 116.7337 | 0.0196 | 0.0178 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414437_2BE0A49C | 504990 | 985 | -85.3 | 504990 | 673 | -94.8 | 504990 | 614 | -95.2 | 504990 | 880 |
| MR_1774414437_9A4170C6 | 504990 | 985 | -85.5 | 504990 | 673 | -93.4 | 504990 | 614 | -96.8 | 504990 | 880 |
| MR_1774414437_5BCAE4A6 | 504990 | 985 | -85.8 | 504990 | 673 | -92.3 | 504990 | 614 | -97.3 | 504990 | 880 |
| MR_1774414437_D1F3D8BF | 504990 | 985 | -87.3 | 504990 | 673 | -92.9 | 504990 | 614 | -97.9 | 504990 | 880 |
| MR_1774414437_3F9B5BED | 504990 | 985 | -86.2 | 504990 | 673 | -91.9 | 504990 | 614 | -96.9 | 504990 | 880 |
| MR_1774414437_5E0F804A | 504990 | 985 | -88.0 | 504990 | 673 | -94.0 | 504990 | 614 | -95.5 | 504990 | 880 |
| MR_1774414437_71EA895E | 504990 | 985 | -85.7 | 504990 | 673 | -94.7 | 504990 | 614 | -95.2 | 504990 | 880 |
| MR_1774414437_C983C058 | 504990 | 985 | -86.6 | 504990 | 673 | -92.4 | 504990 | 614 | -98.2 | 504990 | 880 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1827: `bffbef23-286...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bffbef23-286a-43d8-9424-65b3ae43c2d4` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Add neighbor relationship between 3255964_1 and 3279252_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1827] topology](images/train_1827.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3279252_2
- `C2`: Adjust the azimuth of 3255964_1 by 36 degrees
- `C3`: Increase transmission power for 3279252_2
- `C4`: Decrease transmission power for 3255964_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255964_1
- `C6`: Decrease transmission power for 3279252_2
- `C7`: Increase transmission power for 3255964_1
- `C8`: Press down the tilt angle  of 3279252_2 by 3 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255964_1
- `C10`: Increase A3 Offset threshold for 3279252_2
- `C11`: Increase A3 Offset threshold for 3255964_1
- `C12`: Check test server and transmission issues
- `C13`: Lift the tilt angle  of 3279252_2 by 3 degrees
- `C14`: Decrease A3 Offset threshold for 3255964_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Adjust the azimuth of 3279252_2 by 30 degrees
- `C17`: Add neighbor relationship between 3255964_1 and 3279252_2 **← 정답**
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279252_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279252_2
- `C20`: Lift the tilt angle of 3255964_1 by 10 degrees
- `C21`: Add neighbor relationship between 3212478_4 and 3279252_2
- `C22`: Press down the tilt angle of 3255964_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.481 | MS1 | 121.4656776233 | 31.1446222035 | 280 | 504990 | -80.30 | 17.36 | 370.29 | 0.10 | 2.37 | 1577 |
| 2024-09-20 22:21:32.915 | MS1 | 121.4656736193 | 31.1446295199 | 280 | 504990 | -84.97 | 16.24 | 405.83 | 0.12 | 2.08 | 1576 |
| 2024-09-20 22:21:33.783 | MS1 | 121.4656618998 | 31.1446339705 | 280 | 504990 | -84.50 | 13.26 | 330.50 | 0.07 | 2.85 | 1572 |
| 2024-09-20 22:21:34.202 | MS1 | 121.4656760510 | 31.1446372018 | 280 | 504990 | -89.62 | -1.17 | 45.96 | 0.19 | 1.28 | 1569 |
| 2024-09-20 22:21:35.332 | MS1 | 121.4656609534 | 31.1446238764 | 280 | 504990 | -88.89 | -2.34 | 66.59 | 0.01 | 1.48 | 1589 |
| 2024-09-20 22:21:36.536 | MS1 | 121.4656747770 | 31.1446222588 | 280 | 504990 | -85.75 | -3.98 | 60.25 | 0.15 | 1.48 | 1588 |
| 2024-09-20 22:21:37.745 | MS1 | 121.4656594138 | 31.1446378523 | 280 | 504990 | -91.06 | -0.46 | 54.52 | 0.20 | 1.36 | 1567 |
| 2024-09-20 22:21:38.692 | MS1 | 121.4656724436 | 31.1446224264 | 280 | 504990 | -78.11 | 15.19 | 579.05 | 0.03 | 1.31 | 1583 |
| 2024-09-20 22:21:39.616 | MS1 | 121.4656654948 | 31.1446338148 | 280 | 504990 | -80.15 | 12.49 | 388.46 | 0.05 | 1.50 | 1564 |
| 2024-09-20 22:21:40.996 | MS1 | 121.4656665309 | 31.1446344736 | 280 | 504990 | -84.37 | 17.03 | 552.60 | 0.06 | 2.64 | 1587 |
| 2024-09-20 22:21:41.482 | MS1 | 121.4656778450 | 31.1446294930 | 280 | 504990 | -83.48 | 16.41 | 434.17 | 0.07 | 2.39 | 1577 |
| 2024-09-20 22:21:42.536 | MS1 | 121.4656669794 | 31.1446367459 | 280 | 504990 | -83.35 | 17.86 | 479.98 | 0.08 | 2.74 | 1582 |

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
| 3212478 | 4 | 121.4721302370 | 31.1546973955 | 354 | 15 | 12 | 37.7 | TDD | 983 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3255964 | 1 | 121.4680001658 | 31.1516917439 | 160 | 7 | 10 | 39.7 | TDD | 280 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3264492 | 3 | 121.4656039781 | 31.1521192066 | 55 | 11 | 7 | 22.9 | TDD | 646 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3279252 | 2 | 121.4728250127 | 31.1452698561 | 234 | 1 | 2 | 18.7 | TDD | 263 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.359 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.375 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.500 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.500 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.221 | NREventA3 | measId:2;ServCellPCI:590;Se... |
| 2024-09-20 22:21:36.221 | NREventA3 | measId:2;ServCellPCI:590;Se... |
| 2024-09-20 22:21:37.221 | NREventA3 | measId:2;ServCellPCI:590;Se... |
| 2024-09-20 22:21:39.721 | NRRRCReestablishAttempt | PCI:590 |
| 2024-09-20 22:21:39.737 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.747 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.896 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.896 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255964 | 1 | 17.3540 | 15.5697 | -117.0325 | 19.1006 | 188.6768 | 0.0043 | 0.1663 |
| 2024_09_20 22:00 | 3279252 | 2 | 7.4211 | 12.1835 | -117.1236 | 14.2307 | 158.4624 | 0.0127 | 0.0049 |
| 2024_09_20 22:00 | 3264492 | 3 | 10.6658 | 13.5375 | -117.8915 | 18.9309 | 185.8307 | 0.0097 | 0.0196 |
| 2024_09_20 22:00 | 3212478 | 4 | 19.3054 | 16.2566 | -117.8449 | 8.6300 | 86.5885 | 0.0050 | 0.0185 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417198_51FA42F3 | 504990 | 263 | -85.9 | 504990 | 280 | -89.4 | 504990 | 983 | -95.4 | 504990 | 646 |
| MR_1774417198_6EE97876 | 504990 | 263 | -83.6 | 504990 | 280 | -89.2 | 504990 | 983 | -95.8 | 504990 | 646 |
| MR_1774417198_E4870E31 | 504990 | 263 | -83.3 | 504990 | 280 | -90.4 | 504990 | 983 | -96.1 | 504990 | 646 |
| MR_1774417198_783B50CD | 504990 | 280 | -91.5 | 504990 | 263 | -84.9 | 504990 | 983 | -94.3 | 504990 | 646 |
| MR_1774417198_9DF1650A | 504990 | 263 | -84.7 | 504990 | 280 | -89.5 | 504990 | 983 | -95.2 | 504990 | 646 |
| MR_1774417198_F93C9041 | 504990 | 280 | -90.9 | 504990 | 263 | -84.2 | 504990 | 983 | -92.9 | 504990 | 646 |
| MR_1774417198_1A11030D | 504990 | 263 | -84.8 | 504990 | 280 | -90.1 | 504990 | 983 | -93.8 | 504990 | 646 |
| MR_1774417198_BB9DF31B | 504990 | 263 | -82.8 | 504990 | 280 | -90.1 | 504990 | 983 | -95.2 | 504990 | 646 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1828: `7517a457-982...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7517a457-982c-4fe8-9197-64c9186766c3` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1828] topology](images/train_1828.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267046_3
- `C2`: Increase A3 Offset threshold for 3267046_3
- `C3`: Decrease transmission power for 3267046_3
- `C4`: Increase transmission power for 3249510_1
- `C5`: Decrease A3 Offset threshold for 3267046_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249510_1
- `C7`: Adjust the azimuth of 3249510_1 by 43 degrees
- `C8`: Insufficient data; more data is needed for judgment. **← 정답**
- `C9`: Add neighbor relationship between 3267046_3 and 3249510_1
- `C10`: Adjust the azimuth of 3267046_3 by 50 degrees
- `C11`: Press down the tilt angle  of 3249510_1 by 10 degrees
- `C12`: Check test server and transmission issues
- `C13`: Decrease A3 Offset threshold for 3249510_1
- `C14`: Press down the tilt angle of 3267046_3 by 8 degrees
- `C15`: Increase transmission power for 3267046_3
- `C16`: Lift the tilt angle  of 3249510_1 by 10 degrees
- `C17`: Decrease transmission power for 3249510_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249510_1
- `C19`: Increase A3 Offset threshold for 3249510_1
- `C20`: Lift the tilt angle of 3267046_3 by 8 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267046_3
- `C22`: Add neighbor relationship between 3273718_2 and 3249510_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.174 | MS1 | 121.4656706386 | 31.1446306539 | 669 | 504990 | -90.87 | 12.03 | 500.89 | 0.15 | 2.85 | 1596 |
| 2024-09-20 22:21:32.962 | MS1 | 121.4656636484 | 31.1446275156 | 669 | 504990 | -91.59 | 16.10 | 475.63 | 0.11 | 2.58 | 1564 |
| 2024-09-20 22:21:33.309 | MS1 | 121.4656750568 | 31.1446334965 | 669 | 504990 | -88.64 | 12.01 | 533.95 | 0.11 | 2.42 | 1592 |
| 2024-09-20 22:21:34.144 | MS1 | 121.4656688116 | 31.1446192873 | 669 | 504990 | -86.64 | 16.40 | 95.05 | 0.08 | 2.61 | 1571 |
| 2024-09-20 22:21:35.654 | MS1 | 121.4656769425 | 31.1446322325 | 669 | 504990 | -89.87 | 17.20 | 89.09 | 0.16 | 2.56 | 1586 |
| 2024-09-20 22:21:36.399 | MS1 | 121.4656643839 | 31.1446354100 | 669 | 504990 | -89.48 | 17.74 | 79.69 | 0.08 | 2.82 | 1569 |
| 2024-09-20 22:21:37.682 | MS1 | 121.4656589529 | 31.1446377639 | 669 | 504990 | -89.60 | 12.22 | 87.62 | 0.20 | 2.22 | 1585 |
| 2024-09-20 22:21:38.515 | MS1 | 121.4656734790 | 31.1446358922 | 669 | 504990 | -92.08 | 8.02 | 80.35 | 0.20 | 2.70 | 1598 |
| 2024-09-20 22:21:39.167 | MS1 | 121.4656768125 | 31.1446254301 | 669 | 504990 | -89.60 | 9.89 | 59.63 | 0.07 | 2.25 | 1571 |
| 2024-09-20 22:21:40.858 | MS1 | 121.4656708883 | 31.1446185402 | 669 | 504990 | -92.35 | 9.64 | 405.52 | 0.13 | 2.22 | 1599 |
| 2024-09-20 22:21:41.273 | MS1 | 121.4656632051 | 31.1446267489 | 669 | 504990 | -91.09 | 9.99 | 475.37 | 0.16 | 2.92 | 1571 |
| 2024-09-20 22:21:42.564 | MS1 | 121.4656775973 | 31.1446367918 | 669 | 504990 | -89.72 | 11.05 | 419.12 | 0.02 | 2.99 | 1590 |

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
| 3247406 | 4 | 121.4684953139 | 31.1523588201 | 166 | 5 | 12 | 25.1 | TDD | 838 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3249510 | 1 | 121.4673682552 | 31.1453266585 | 287 | 9 | 7 | 35.6 | TDD | 928 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3267046 | 3 | 121.4666373645 | 31.1471514460 | 321 | 2 | 5 | 33.0 | TDD | 669 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3273718 | 2 | 121.4745944677 | 31.1508921783 | 44 | 1 | 4 | 30.3 | TDD | 444 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.891 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.914 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.046 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.046 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.702 | NREventA3 | measId:2;ServCellPCI:224;Se... |
| 2024-09-20 22:21:37.942 | NRHandoverAttempt | SourcePCI:224;SourceNR-ARFC... |
| 2024-09-20 22:21:37.973 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.984 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.088 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.088 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3249510 | 1 | 82.0666 | 93.9401 | -116.9494 | 17.5504 | 138.4154 | 0.0133 | 0.0145 |
| 2024_09_19 22:00 | 3273718 | 2 | 88.4286 | 88.5753 | -116.9220 | 11.7834 | 173.1707 | 0.0191 | 0.0178 |
| 2024_09_19 22:00 | 3267046 | 3 | 83.4781 | 76.5432 | -117.0860 | 13.1946 | 181.0583 | 0.0176 | 0.0040 |
| 2024_09_19 22:00 | 3247406 | 4 | 77.5984 | 76.3086 | -115.4990 | 16.6608 | 97.4565 | 0.0071 | 0.0018 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414127_72667576 | 504990 | 669 | -86.4 | 504990 | 928 | -93.2 | 504990 | 444 | -96.9 | 504990 | 838 |
| MR_1774414127_2CC37D56 | 504990 | 669 | -87.5 | 504990 | 928 | -91.2 | 504990 | 444 | -96.8 | 504990 | 838 |
| MR_1774414127_4EF3FDF8 | 504990 | 669 | -85.7 | 504990 | 928 | -92.2 | 504990 | 444 | -98.2 | 504990 | 838 |
| MR_1774414127_E791B765 | 504990 | 669 | -86.2 | 504990 | 928 | -93.9 | 504990 | 444 | -97.5 | 504990 | 838 |
| MR_1774414127_F4439BCE | 504990 | 669 | -85.4 | 504990 | 928 | -94.0 | 504990 | 444 | -97.3 | 504990 | 838 |
| MR_1774414127_4D088A58 | 504990 | 669 | -86.4 | 504990 | 928 | -94.0 | 504990 | 444 | -98.1 | 504990 | 838 |
| MR_1774414127_89139CC9 | 504990 | 669 | -84.7 | 504990 | 928 | -90.6 | 504990 | 444 | -99.0 | 504990 | 838 |
| MR_1774414127_3CD46050 | 504990 | 669 | -87.0 | 504990 | 928 | -93.0 | 504990 | 444 | -97.2 | 504990 | 838 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1829: `745594d1-8d5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `745594d1-8d54-4071-be81-d60caad5bca4` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Decrease A3 Offset threshold for 3232040_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1829] topology](images/train_1829.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Press down the tilt angle  of 3267726_2 by 8 degrees
- `C3`: Add neighbor relationship between 3270627_3 and 3267726_2
- `C4`: Increase transmission power for 3232040_1
- `C5`: Decrease A3 Offset threshold for 3232040_1 **← 정답**
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232040_1
- `C7`: Lift the tilt angle of 3232040_1 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232040_1
- `C9`: Decrease A3 Offset threshold for 3267726_2
- `C10`: Increase A3 Offset threshold for 3232040_1
- `C11`: Press down the tilt angle of 3232040_1 by 10 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267726_2
- `C13`: Decrease transmission power for 3232040_1
- `C14`: Check test server and transmission issues
- `C15`: Increase A3 Offset threshold for 3267726_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267726_2
- `C17`: Adjust the azimuth of 3232040_1 by 50 degrees
- `C18`: Lift the tilt angle  of 3267726_2 by 8 degrees
- `C19`: Increase transmission power for 3267726_2
- `C20`: Decrease transmission power for 3267726_2
- `C21`: Add neighbor relationship between 3232040_1 and 3267726_2
- `C22`: Adjust the azimuth of 3267726_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.708 | MS1 | 121.4656696194 | 31.1446281021 | 640 | 504990 | -82.45 | 12.91 | 549.32 | 0.17 | 2.88 | 1574 |
| 2024-09-20 22:21:32.140 | MS1 | 121.4656626831 | 31.1446356223 | 640 | 504990 | -83.95 | 13.38 | 463.52 | 0.17 | 2.97 | 1593 |
| 2024-09-20 22:21:33.544 | MS1 | 121.4656719272 | 31.1446199496 | 640 | 504990 | -79.95 | 13.43 | 560.91 | 0.12 | 2.78 | 1594 |
| 2024-09-20 22:21:34.949 | MS1 | 121.4656659552 | 31.1446220186 | 640 | 504990 | -91.27 | -0.05 | 57.13 | 0.19 | 1.31 | 1583 |
| 2024-09-20 22:21:35.202 | MS1 | 121.4656691900 | 31.1446358898 | 640 | 504990 | -86.75 | -2.97 | 45.96 | 0.14 | 1.35 | 1598 |
| 2024-09-20 22:21:36.840 | MS1 | 121.4656637108 | 31.1446197997 | 640 | 504990 | -86.00 | -3.23 | 44.14 | 0.01 | 1.35 | 1569 |
| 2024-09-20 22:21:37.989 | MS1 | 121.4656610023 | 31.1446303142 | 640 | 504990 | -83.38 | -2.79 | 69.35 | 0.03 | 1.35 | 1561 |
| 2024-09-20 22:21:38.518 | MS1 | 121.4656665524 | 31.1446372248 | 640 | 504990 | -88.47 | -0.30 | 64.74 | 0.05 | 1.50 | 1591 |
| 2024-09-20 22:21:39.797 | MS1 | 121.4656710047 | 31.1446228567 | 449 | 504990 | -81.07 | 12.39 | 262.73 | 0.02 | 1.45 | 1595 |
| 2024-09-20 22:21:40.162 | MS1 | 121.4656628255 | 31.1446357354 | 449 | 504990 | -78.21 | 14.12 | 415.34 | 0.03 | 2.86 | 1598 |
| 2024-09-20 22:21:41.529 | MS1 | 121.4656632548 | 31.1446244225 | 449 | 504990 | -76.03 | 13.86 | 443.88 | 0.18 | 2.88 | 1586 |
| 2024-09-20 22:21:42.980 | MS1 | 121.4656746748 | 31.1446220425 | 449 | 504990 | -81.05 | 17.36 | 447.30 | 0.19 | 2.55 | 1591 |

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
| 3232040 | 1 | 121.4753809345 | 31.1551327968 | 155 | 13 | 12 | 36.0 | TDD | 640 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3267726 | 2 | 121.4714220121 | 31.1443385232 | 87 | 4 | 0 | 34.6 | TDD | 449 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3270627 | 3 | 121.4710465890 | 31.1488633925 | 132 | 8 | 11 | 45.4 | TDD | 181 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3271514 | 4 | 121.4722784293 | 31.1512106884 | 44 | 15 | 8 | 19.2 | TDD | 262 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.322 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.442 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.442 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.160 | NREventA3 | measId:2;ServCellPCI:233;Se... |
| 2024-09-20 22:21:38.400 | NRHandoverAttempt | SourcePCI:233;SourceNR-ARFC... |
| 2024-09-20 22:21:38.436 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.446 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.587 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.587 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232040 | 1 | 12.7308 | 18.9748 | -116.6953 | 19.7010 | 98.3430 | 0.0100 | 0.1642 |
| 2024_09_20 22:00 | 3267726 | 2 | 5.7527 | 8.3791 | -114.0568 | 6.9949 | 177.8517 | 0.0094 | 0.0161 |
| 2024_09_20 22:00 | 3270627 | 3 | 7.1348 | 16.6369 | -114.9086 | 7.2503 | 194.4930 | 0.0098 | 0.0187 |
| 2024_09_20 22:00 | 3271514 | 4 | 15.9236 | 6.1245 | -114.0079 | 6.7676 | 143.1778 | 0.0180 | 0.0048 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412233_14611491 | 504990 | 449 | -83.9 | 504990 | 640 | -90.8 | 504990 | 181 | -87.7 | 504990 | 262 |
| MR_1774412233_5899F9BE | 504990 | 640 | -89.7 | 504990 | 449 | -86.3 | 504990 | 181 | -88.5 | 504990 | 262 |
| MR_1774412233_74E96ABB | 504990 | 640 | -91.3 | 504990 | 449 | -86.8 | 504990 | 181 | -85.6 | 504990 | 262 |
| MR_1774412233_CDDB914B | 504990 | 640 | -90.0 | 504990 | 449 | -85.0 | 504990 | 181 | -85.4 | 504990 | 262 |
| MR_1774412233_0F5057FB | 504990 | 640 | -90.1 | 504990 | 449 | -87.3 | 504990 | 181 | -85.6 | 504990 | 262 |

> *... 2개 열 생략 (전체 14열)*

---
