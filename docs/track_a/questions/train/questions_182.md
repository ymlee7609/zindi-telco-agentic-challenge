# Track A 문제 분석 — train[1810]~train[1819]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1810] ~ train[1819] (10개)

## 목차

1. [문제 1810: `b2d6a5f4-bf0...`](#1810) — single-answer, 정답: C12
2. [문제 1811: `67f3e3d8-eaa...`](#1811) — single-answer, 정답: C9
3. [문제 1812: `e0d36f61-eb6...`](#1812) — single-answer, 정답: C17
4. [문제 1813: `b484065a-196...`](#1813) — single-answer, 정답: C10
5. [문제 1814: `353aafe9-f45...`](#1814) — single-answer, 정답: C7
6. [문제 1815: `e8d53b0d-fd8...`](#1815) — single-answer, 정답: C14
7. [문제 1816: `89e443af-c70...`](#1816) — single-answer, 정답: C3
8. [문제 1817: `c341c229-8b9...`](#1817) — multiple-answer, 정답: C20|C21
9. [문제 1818: `f9a5318c-31a...`](#1818) — single-answer, 정답: C16
10. [문제 1819: `8060787b-bca...`](#1819) — single-answer, 정답: C10

---

### 문제 1810: `b2d6a5f4-bf0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b2d6a5f4-bf03-4289-88e4-6f2450cdd7b6` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1810] topology](images/train_1810.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3228827_2 and 3216787_4
- `C2`: Increase A3 Offset threshold for 3228827_2
- `C3`: Increase transmission power for 3228827_2
- `C4`: Decrease transmission power for 3216787_4
- `C5`: Press down the tilt angle of 3228827_2 by 8 degrees
- `C6`: Increase transmission power for 3216787_4
- `C7`: Lift the tilt angle of 3228827_2 by 8 degrees
- `C8`: Add neighbor relationship between 3249367_1 and 3216787_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228827_2
- `C10`: Decrease A3 Offset threshold for 3228827_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216787_4
- `C12`: Check test server and transmission issues **← 정답**
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Adjust the azimuth of 3228827_2 by 50 degrees
- `C15`: Adjust the azimuth of 3216787_4 by 50 degrees
- `C16`: Lift the tilt angle  of 3216787_4 by 2 degrees
- `C17`: Increase A3 Offset threshold for 3216787_4
- `C18`: Press down the tilt angle  of 3216787_4 by 2 degrees
- `C19`: Decrease transmission power for 3228827_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228827_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216787_4
- `C22`: Decrease A3 Offset threshold for 3216787_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.570 | MS1 | 121.4656624443 | 31.1446364181 | 875 | 504990 | -85.73 | 12.37 | 458.87 | 0.04 | 2.98 | 1571 |
| 2024-09-20 22:21:32.961 | MS1 | 121.4656729823 | 31.1446379275 | 875 | 504990 | -85.08 | 12.98 | 382.37 | 0.10 | 2.54 | 1581 |
| 2024-09-20 22:21:33.148 | MS1 | 121.4656614633 | 31.1446274016 | 875 | 504990 | -88.45 | 13.51 | 588.60 | 0.09 | 2.09 | 1560 |
| 2024-09-20 22:21:34.148 | MS1 | 121.4656692225 | 31.1446188736 | 875 | 504990 | -86.99 | 12.31 | 47.56 | 0.18 | 2.24 | 395 |
| 2024-09-20 22:21:35.230 | MS1 | 121.4656729729 | 31.1446268100 | 875 | 504990 | -87.38 | 13.71 | 95.47 | 0.16 | 2.27 | 380 |
| 2024-09-20 22:21:36.822 | MS1 | 121.4656774650 | 31.1446347471 | 875 | 504990 | -85.84 | 16.60 | 87.53 | 0.05 | 2.52 | 416 |
| 2024-09-20 22:21:37.682 | MS1 | 121.4656711972 | 31.1446258520 | 875 | 504990 | -90.39 | 8.03 | 69.91 | 0.10 | 2.21 | 467 |
| 2024-09-20 22:21:38.317 | MS1 | 121.4656591057 | 31.1446359107 | 875 | 504990 | -90.10 | 8.40 | 100.12 | 0.01 | 2.65 | 490 |
| 2024-09-20 22:21:39.146 | MS1 | 121.4656759502 | 31.1446236742 | 875 | 504990 | -89.98 | 12.30 | 87.12 | 0.06 | 2.19 | 347 |
| 2024-09-20 22:21:40.165 | MS1 | 121.4656740898 | 31.1446364436 | 875 | 504990 | -91.62 | 9.54 | 412.97 | 0.16 | 2.73 | 1581 |
| 2024-09-20 22:21:41.360 | MS1 | 121.4656645959 | 31.1446291686 | 875 | 504990 | -90.57 | 9.70 | 455.54 | 0.07 | 2.67 | 1600 |
| 2024-09-20 22:21:42.367 | MS1 | 121.4656690558 | 31.1446216574 | 875 | 504990 | -89.33 | 8.80 | 502.21 | 0.06 | 2.40 | 1563 |

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
| 3216787 | 4 | 121.4701032390 | 31.1502745542 | 143 | 0 | 7 | 26.5 | TDD | 381 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3217098 | 3 | 121.4685879172 | 31.1460430468 | 266 | 6 | 8 | 37.4 | TDD | 131 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3228827 | 2 | 121.4744181553 | 31.1558094825 | 306 | 7 | 8 | 19.4 | TDD | 875 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3249367 | 1 | 121.4727510553 | 31.1447569320 | 351 | 0 | 2 | 34.3 | TDD | 969 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.052 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.076 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.224 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.224 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.854 | NREventA3 | measId:2;ServCellPCI:624;Se... |
| 2024-09-20 22:21:38.094 | NRHandoverAttempt | SourcePCI:624;SourceNR-ARFC... |
| 2024-09-20 22:21:38.126 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.141 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.290 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.290 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249367 | 1 | 8.5129 | 9.1729 | -115.4133 | 15.6522 | 96.5074 | 0.0155 | 0.0149 |
| 2024_09_20 22:00 | 3228827 | 2 | 16.5179 | 16.2669 | -114.4959 | 15.2616 | 146.4640 | 0.0130 | 0.0046 |
| 2024_09_20 22:00 | 3217098 | 3 | 6.4824 | 5.7298 | -117.2154 | 9.0106 | 112.6971 | 0.0015 | 0.0060 |
| 2024_09_20 22:00 | 3216787 | 4 | 18.3514 | 13.7325 | -117.7456 | 18.2219 | 176.0885 | 0.0050 | 0.0152 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416032_E0D9303C | 504990 | 875 | -86.6 | 504990 | 381 | -94.3 | 504990 | 969 | -96.4 | 504990 | 131 |
| MR_1774416032_DD77984D | 504990 | 875 | -87.2 | 504990 | 381 | -97.2 | 504990 | 969 | -95.9 | 504990 | 131 |
| MR_1774416032_A93BB538 | 504990 | 875 | -87.6 | 504990 | 381 | -94.2 | 504990 | 969 | -96.1 | 504990 | 131 |
| MR_1774416032_ABA83751 | 504990 | 875 | -86.6 | 504990 | 381 | -95.7 | 504990 | 969 | -96.0 | 504990 | 131 |
| MR_1774416032_207B70EF | 504990 | 875 | -85.6 | 504990 | 381 | -93.4 | 504990 | 969 | -96.9 | 504990 | 131 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1811: `67f3e3d8-eaa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `67f3e3d8-eaaa-4a7e-9993-8fbc7db04462` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261703_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1811] topology](images/train_1811.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3250323_4
- `C2`: Press down the tilt angle of 3261703_5 by 3 degrees
- `C3`: Decrease A3 Offset threshold for 3250323_4
- `C4`: Check test server and transmission issues
- `C5`: Press down the tilt angle  of 3250323_4 by 1 degrees
- `C6`: Add neighbor relationship between 3261703_5 and 3250323_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250323_4
- `C8`: Increase A3 Offset threshold for 3261703_5
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261703_5 **← 정답**
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Adjust the azimuth of 3250323_4 by 23 degrees
- `C12`: Lift the tilt angle of 3261703_5 by 3 degrees
- `C13`: Decrease transmission power for 3250323_4
- `C14`: Adjust the azimuth of 3261703_5 by 22 degrees
- `C15`: Add neighbor relationship between 3247933_8 and 3250323_4
- `C16`: Decrease A3 Offset threshold for 3261703_5
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261703_5
- `C18`: Decrease transmission power for 3261703_5
- `C19`: Increase transmission power for 3261703_5
- `C20`: Increase A3 Offset threshold for 3250323_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250323_4
- `C22`: Lift the tilt angle  of 3250323_4 by 1 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.382 | MS1 | 121.4656609752 | 31.1446227468 | 732 | 504990 | -93.68 | 11.75 | 322.22 | 0.17 | 2.31 | 1593 |
| 2024-09-20 22:21:32.566 | MS1 | 121.4656705846 | 31.1446316891 | 517 | 504990 | -93.74 | 10.59 | 395.14 | 0.03 | 2.48 | 1561 |
| 2024-09-20 22:21:33.263 | MS1 | 121.4656600154 | 31.1446229335 | 93 | 504990 | -93.98 | 9.83 | 431.15 | 0.06 | 2.42 | 1577 |
| 2024-09-20 22:21:34.413 | MS1 | 121.4656596675 | 31.1446193636 | 952 | 152650 | -91.57 | 4.80 | 76.10 | 0.17 | 1.54 | 901 |
| 2024-09-20 22:21:35.442 | MS1 | 121.4656622270 | 31.1446370881 | 847 | 152650 | -94.71 | 7.30 | 99.73 | 0.10 | 1.98 | 964 |
| 2024-09-20 22:21:36.638 | MS1 | 121.4656657364 | 31.1446258622 | 964 | 152650 | -89.92 | 3.51 | 84.00 | 0.03 | 1.54 | 924 |
| 2024-09-20 22:21:37.463 | MS1 | 121.4656680779 | 31.1446334285 | 645 | 152650 | -92.57 | 4.61 | 71.85 | 0.06 | 1.53 | 941 |
| 2024-09-20 22:21:38.280 | MS1 | 121.4656665962 | 31.1446364271 | 952 | 152650 | -91.67 | 7.82 | 50.64 | 0.18 | 1.97 | 932 |
| 2024-09-20 22:21:39.273 | MS1 | 121.4656689474 | 31.1446266654 | 847 | 152650 | -94.14 | 2.70 | 84.27 | 0.04 | 1.71 | 906 |
| 2024-09-20 22:21:40.507 | MS1 | 121.4656774482 | 31.1446267322 | 964 | 152650 | -93.00 | 4.15 | 64.52 | 0.16 | 2.86 | 1585 |
| 2024-09-20 22:21:41.120 | MS1 | 121.4656614753 | 31.1446235173 | 645 | 152650 | -96.98 | 5.58 | 74.08 | 0.02 | 2.11 | 1583 |
| 2024-09-20 22:21:42.800 | MS1 | 121.4656650281 | 31.1446197754 | 952 | 152650 | -94.33 | 4.97 | 79.99 | 0.04 | 2.87 | 1568 |

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
| 3226016 | 9 | 121.4747133779 | 31.1554794865 | 348 | 7 | 8 | 3.3 | FDD | 645 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3247933 | 8 | 121.4662568073 | 31.1450786170 | 112 | 1 | 0 | 27.9 | FDD | 964 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3248947 | 10 | 121.4651941487 | 31.1470305992 | 94 | 8 | 3 | 29.1 | FDD | 847 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3250323 | 4 | 121.4724075468 | 31.1528427412 | 192 | 0 | 0 | 29.0 | TDD | 980 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3259040 | 7 | 121.4736531872 | 31.1479745551 | 1 | 15 | 12 | 4.7 | FDD | 512 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3261703 | 5 | 121.4704547467 | 31.1447948847 | 290 | 1 | 10 | 15.2 | TDD | 732 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3262742 | 11 | 121.4640506687 | 31.1488837239 | 138 | 13 | 3 | 12.6 | FDD | 243 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3265999 | 6 | 121.4678507660 | 31.1554134928 | 212 | 2 | 9 | 19.3 | TDD | 93 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3271031 | 13 | 121.4726656989 | 31.1527067054 | 287 | 0 | 1 | 4.8 | FDD | 799 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3271930 | 12 | 121.4743419586 | 31.1446183755 | 32 | 0 | 5 | 28.0 | FDD | 952 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3273624 | 1 | 121.4709235408 | 31.1495836662 | 4 | 5 | 10 | 10.6 | TDD | 517 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3276606 | 2 | 121.4681471131 | 31.1476881381 | 35 | 4 | 1 | 25.4 | TDD | 38 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3278408 | 3 | 121.4751823837 | 31.1508486343 | 282 | 3 | 2 | 10.1 | TDD | 329 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.055 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.077 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.186 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.186 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.922 | NREventA2 | measId:1;ServCellPCI:405;Se... |
| 2024-09-20 22:21:35.043 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.288 | NREventA5 | measId:3;ServCellPCI:405;Se... |
| 2024-09-20 22:21:35.351 | NRHandoverAttempt | SourcePCI:405;SourceNR-ARFC... |
| 2024-09-20 22:21:35.386 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.396 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.539 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.539 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273624 | 1 | 14.8514 | 14.1060 | -116.2141 | 15.3484 | 163.6122 | 0.0069 | 0.0065 |
| 2024_09_20 22:00 | 3276606 | 2 | 16.6600 | 6.8583 | -114.1737 | 17.7991 | 91.8939 | 0.0088 | 0.0105 |
| 2024_09_20 22:00 | 3278408 | 3 | 11.3791 | 9.3415 | -116.8770 | 6.4008 | 190.3794 | 0.0059 | 0.0065 |
| 2024_09_20 22:00 | 3250323 | 4 | 18.0448 | 17.6861 | -114.4079 | 9.3569 | 91.1066 | 0.0062 | 0.0186 |
| 2024_09_20 22:00 | 3261703 | 5 | 16.6951 | 15.4468 | -117.9524 | 18.9835 | 161.1382 | 0.0051 | 0.0011 |
| 2024_09_20 22:00 | 3265999 | 6 | 19.6690 | 6.9391 | -115.7042 | 15.3300 | 105.9034 | 0.0049 | 0.0093 |
| 2024_09_20 22:00 | 3259040 | 7 | 6.0870 | 13.2094 | -115.1217 | 4.7859 | 22.8043 | 0.0079 | 0.0092 |
| 2024_09_20 22:00 | 3247933 | 8 | 10.3997 | 7.7343 | -117.9029 | 3.6865 | 35.6132 | 0.0082 | 0.0099 |
| 2024_09_20 22:00 | 3226016 | 9 | 11.6250 | 9.8789 | -117.1734 | 3.9882 | 32.7159 | 0.0107 | 0.0092 |
| 2024_09_20 22:00 | 3248947 | 10 | 9.4302 | 14.2987 | -114.4683 | 4.8651 | 22.4586 | 0.0050 | 0.0102 |
| 2024_09_20 22:00 | 3262742 | 11 | 5.2344 | 17.1778 | -117.7298 | 4.5625 | 36.1582 | 0.0155 | 0.0153 |
| 2024_09_20 22:00 | 3271930 | 12 | 10.8504 | 14.7882 | -114.1349 | 3.8011 | 46.0089 | 0.0160 | 0.0058 |
| 2024_09_20 22:00 | 3271031 | 13 | 15.8903 | 8.5999 | -116.1390 | 3.6530 | 37.0108 | 0.0038 | 0.0039 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414423_553822F4 | 504990 | 93 | -94.1 | 504990 | 980 | -92.3 | 504990 | 329 | -93.2 | 504990 | 38 |
| MR_1774414423_5522898A | 504990 | 93 | -92.9 | 504990 | 980 | -91.9 | 504990 | 329 | -94.4 | 504990 | 38 |
| MR_1774414423_A47D42FD | 152650 | 952 | -89.6 | 152650 | 799 | -98.0 | 152650 | 243 | -102.8 | 152650 | 512 |
| MR_1774414423_BC670F24 | 504990 | 93 | -95.3 | 504990 | 980 | -92.7 | 504990 | 329 | -91.3 | 504990 | 38 |
| MR_1774414423_A0A5A7C1 | 152650 | 952 | -92.6 | 152650 | 799 | -98.9 | 152650 | 243 | -103.6 | 152650 | 512 |
| MR_1774414423_297E4478 | 152650 | 952 | -91.7 | 152650 | 799 | -97.0 | 152650 | 243 | -103.8 | 152650 | 512 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1812: `e0d36f61-eb6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e0d36f61-eb6b-4ef3-83ea-8469794dae9d` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1812] topology](images/train_1812.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252018_1
- `C2`: Increase transmission power for 3252018_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252498_2
- `C5`: Add neighbor relationship between 3273169_3 and 3252018_1
- `C6`: Decrease A3 Offset threshold for 3252498_2
- `C7`: Press down the tilt angle  of 3252018_1 by 10 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252018_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252498_2
- `C10`: Adjust the azimuth of 3252018_1 by 50 degrees
- `C11`: Increase A3 Offset threshold for 3252498_2
- `C12`: Adjust the azimuth of 3252498_2 by 50 degrees
- `C13`: Decrease transmission power for 3252018_1
- `C14`: Add neighbor relationship between 3252498_2 and 3252018_1
- `C15`: Increase A3 Offset threshold for 3252018_1
- `C16`: Decrease A3 Offset threshold for 3252018_1
- `C17`: Check test server and transmission issues **← 정답**
- `C18`: Lift the tilt angle of 3252498_2 by 6 degrees
- `C19`: Increase transmission power for 3252498_2
- `C20`: Press down the tilt angle of 3252498_2 by 6 degrees
- `C21`: Decrease transmission power for 3252498_2
- `C22`: Lift the tilt angle  of 3252018_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.961 | MS1 | 121.4656675048 | 31.1446272578 | 641 | 504990 | -87.00 | 14.81 | 310.76 | 0.20 | 2.33 | 1565 |
| 2024-09-20 22:21:32.766 | MS1 | 121.4656716948 | 31.1446194699 | 641 | 504990 | -86.05 | 15.26 | 549.93 | 0.14 | 2.29 | 1592 |
| 2024-09-20 22:21:33.761 | MS1 | 121.4656623778 | 31.1446261850 | 641 | 504990 | -88.66 | 12.16 | 595.65 | 0.12 | 2.21 | 1595 |
| 2024-09-20 22:21:34.489 | MS1 | 121.4656616934 | 31.1446372007 | 641 | 504990 | -88.27 | 12.36 | 83.03 | 0.12 | 2.06 | 444 |
| 2024-09-20 22:21:35.609 | MS1 | 121.4656588763 | 31.1446211621 | 641 | 504990 | -89.99 | 12.89 | 89.00 | 0.17 | 2.43 | 414 |
| 2024-09-20 22:21:36.652 | MS1 | 121.4656639760 | 31.1446218941 | 641 | 504990 | -90.87 | 17.20 | 71.88 | 0.08 | 2.98 | 469 |
| 2024-09-20 22:21:37.375 | MS1 | 121.4656671055 | 31.1446197669 | 641 | 504990 | -92.33 | 12.18 | 92.53 | 0.02 | 2.56 | 346 |
| 2024-09-20 22:21:38.801 | MS1 | 121.4656737900 | 31.1446252670 | 641 | 504990 | -91.46 | 8.02 | 82.90 | 0.02 | 2.94 | 459 |
| 2024-09-20 22:21:39.492 | MS1 | 121.4656583790 | 31.1446187870 | 641 | 504990 | -89.37 | 10.30 | 52.09 | 0.06 | 2.19 | 364 |
| 2024-09-20 22:21:40.573 | MS1 | 121.4656698447 | 31.1446202145 | 641 | 504990 | -91.30 | 10.56 | 480.33 | 0.08 | 2.27 | 1567 |
| 2024-09-20 22:21:41.154 | MS1 | 121.4656602711 | 31.1446210601 | 641 | 504990 | -91.76 | 11.97 | 387.12 | 0.09 | 2.27 | 1560 |
| 2024-09-20 22:21:42.398 | MS1 | 121.4656603240 | 31.1446361436 | 641 | 504990 | -89.72 | 8.33 | 474.82 | 0.10 | 2.05 | 1597 |

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
| 3252018 | 1 | 121.4645984430 | 31.1533340101 | 114 | 15 | 1 | 15.7 | TDD | 880 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3252498 | 2 | 121.4688379702 | 31.1473110395 | 57 | 3 | 1 | 21.9 | TDD | 641 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3273169 | 3 | 121.4694250667 | 31.1461481964 | 99 | 10 | 6 | 41.7 | TDD | 530 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3273623 | 4 | 121.4702272514 | 31.1543416021 | 140 | 0 | 5 | 25.2 | TDD | 470 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.198 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.220 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.332 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.332 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.053 | NREventA3 | measId:2;ServCellPCI:423;Se... |
| 2024-09-20 22:21:38.293 | NRHandoverAttempt | SourcePCI:423;SourceNR-ARFC... |
| 2024-09-20 22:21:38.332 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.342 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.481 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.481 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252018 | 1 | 11.2071 | 15.7797 | -116.8410 | 10.1384 | 164.7433 | 0.0095 | 0.0154 |
| 2024_09_20 22:00 | 3252498 | 2 | 18.7525 | 19.2792 | -114.1612 | 10.5305 | 89.4205 | 0.0081 | 0.0194 |
| 2024_09_20 22:00 | 3273169 | 3 | 19.0091 | 10.7165 | -116.5345 | 7.3405 | 83.1881 | 0.0196 | 0.0149 |
| 2024_09_20 22:00 | 3273623 | 4 | 13.9571 | 17.2910 | -116.9165 | 13.3068 | 87.3309 | 0.0156 | 0.0118 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412912_2D7800CD | 504990 | 641 | -90.2 | 504990 | 880 | -93.7 | 504990 | 530 | -98.1 | 504990 | 470 |
| MR_1774412912_923D0D92 | 504990 | 641 | -88.2 | 504990 | 880 | -93.5 | 504990 | 530 | -97.6 | 504990 | 470 |
| MR_1774412912_A5B02CA7 | 504990 | 641 | -86.9 | 504990 | 880 | -95.4 | 504990 | 530 | -97.2 | 504990 | 470 |
| MR_1774412912_0DC533E2 | 504990 | 641 | -87.6 | 504990 | 880 | -93.3 | 504990 | 530 | -97.6 | 504990 | 470 |
| MR_1774412912_44B92145 | 504990 | 641 | -88.3 | 504990 | 880 | -94.8 | 504990 | 530 | -95.2 | 504990 | 470 |
| MR_1774412912_C8FE761A | 504990 | 641 | -90.1 | 504990 | 880 | -93.0 | 504990 | 530 | -96.6 | 504990 | 470 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1813: `b484065a-196...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b484065a-196a-4c49-9ba4-8b64fb782ef3` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1813] topology](images/train_1813.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3231031_3
- `C2`: Increase transmission power for 3231031_3
- `C3`: Add neighbor relationship between 3228739_2 and 3231031_3
- `C4`: Add neighbor relationship between 3266812_4 and 3231031_3
- `C5`: Check test server and transmission issues
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228739_2
- `C7`: Adjust the azimuth of 3231031_3 by 50 degrees
- `C8`: Decrease A3 Offset threshold for 3228739_2
- `C9`: Press down the tilt angle  of 3231031_3 by 10 degrees
- `C10`: Insufficient data; more data is needed for judgment. **← 정답**
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228739_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231031_3
- `C13`: Increase A3 Offset threshold for 3228739_2
- `C14`: Lift the tilt angle of 3228739_2 by 10 degrees
- `C15`: Lift the tilt angle  of 3231031_3 by 10 degrees
- `C16`: Increase A3 Offset threshold for 3231031_3
- `C17`: Increase transmission power for 3228739_2
- `C18`: Adjust the azimuth of 3228739_2 by 50 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231031_3
- `C20`: Decrease transmission power for 3228739_2
- `C21`: Press down the tilt angle of 3228739_2 by 10 degrees
- `C22`: Decrease A3 Offset threshold for 3231031_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.584 | MS1 | 121.4656627828 | 31.1446195578 | 535 | 504990 | -89.55 | 15.03 | 337.71 | 0.09 | 2.70 | 1583 |
| 2024-09-20 22:21:32.215 | MS1 | 121.4656712964 | 31.1446371066 | 535 | 504990 | -86.03 | 12.84 | 578.69 | 0.03 | 2.93 | 1574 |
| 2024-09-20 22:21:33.621 | MS1 | 121.4656739785 | 31.1446214342 | 535 | 504990 | -87.11 | 12.81 | 489.49 | 0.19 | 2.38 | 1560 |
| 2024-09-20 22:21:34.483 | MS1 | 121.4656717932 | 31.1446204045 | 535 | 504990 | -91.73 | 12.16 | 68.74 | 0.13 | 2.26 | 1562 |
| 2024-09-20 22:21:35.847 | MS1 | 121.4656637571 | 31.1446376240 | 535 | 504990 | -89.35 | 17.88 | 65.24 | 0.16 | 3.00 | 1572 |
| 2024-09-20 22:21:36.404 | MS1 | 121.4656694038 | 31.1446267717 | 535 | 504990 | -85.25 | 12.49 | 78.54 | 0.16 | 2.01 | 1568 |
| 2024-09-20 22:21:37.501 | MS1 | 121.4656745665 | 31.1446316192 | 535 | 504990 | -92.75 | 10.54 | 72.21 | 0.03 | 2.17 | 1596 |
| 2024-09-20 22:21:38.109 | MS1 | 121.4656770912 | 31.1446297578 | 535 | 504990 | -89.65 | 10.21 | 55.57 | 0.04 | 2.34 | 1595 |
| 2024-09-20 22:21:39.940 | MS1 | 121.4656658694 | 31.1446271703 | 535 | 504990 | -93.80 | 9.09 | 64.41 | 0.18 | 2.63 | 1591 |
| 2024-09-20 22:21:40.965 | MS1 | 121.4656592959 | 31.1446212322 | 535 | 504990 | -92.57 | 12.84 | 345.07 | 0.06 | 2.58 | 1583 |
| 2024-09-20 22:21:41.620 | MS1 | 121.4656661904 | 31.1446194413 | 535 | 504990 | -91.80 | 8.34 | 348.52 | 0.04 | 2.82 | 1592 |
| 2024-09-20 22:21:42.120 | MS1 | 121.4656653219 | 31.1446312824 | 535 | 504990 | -92.79 | 8.42 | 471.61 | 0.06 | 3.00 | 1566 |

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
| 3228739 | 2 | 121.4711283549 | 31.1469375957 | 9 | 12 | 11 | 40.0 | TDD | 535 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3231031 | 3 | 121.4697545526 | 31.1492839419 | 41 | 9 | 7 | 37.6 | TDD | 974 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3239187 | 1 | 121.4675344481 | 31.1517136449 | 80 | 8 | 8 | 47.7 | TDD | 112 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3266812 | 4 | 121.4752580781 | 31.1449783938 | 52 | 10 | 8 | 20.1 | TDD | 679 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.759 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.908 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.908 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.625 | NREventA3 | measId:2;ServCellPCI:261;Se... |
| 2024-09-20 22:21:37.865 | NRHandoverAttempt | SourcePCI:261;SourceNR-ARFC... |
| 2024-09-20 22:21:37.907 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.919 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.049 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.049 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3239187 | 1 | 84.9952 | 87.8951 | -115.6746 | 14.0745 | 172.7442 | 0.0177 | 0.0138 |
| 2024_09_19 22:00 | 3228739 | 2 | 83.7966 | 83.7679 | -115.5410 | 15.6453 | 120.2802 | 0.0108 | 0.0109 |
| 2024_09_19 22:00 | 3231031 | 3 | 85.6472 | 79.9440 | -115.3671 | 6.4684 | 92.8993 | 0.0032 | 0.0077 |
| 2024_09_19 22:00 | 3266812 | 4 | 81.2442 | 90.0695 | -115.3723 | 7.1838 | 132.3678 | 0.0124 | 0.0014 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414236_3EDEF0CD | 504990 | 535 | -89.9 | 504990 | 974 | -99.3 | 504990 | 679 | -105.0 | 504990 | 112 |
| MR_1774414236_2BC29A40 | 504990 | 535 | -91.8 | 504990 | 974 | -101.5 | 504990 | 679 | -104.8 | 504990 | 112 |
| MR_1774414236_B6997967 | 504990 | 535 | -91.8 | 504990 | 974 | -98.1 | 504990 | 679 | -104.4 | 504990 | 112 |
| MR_1774414236_791B8D54 | 504990 | 535 | -93.3 | 504990 | 974 | -98.5 | 504990 | 679 | -103.9 | 504990 | 112 |
| MR_1774414236_FF258304 | 504990 | 535 | -91.5 | 504990 | 974 | -98.2 | 504990 | 679 | -103.0 | 504990 | 112 |
| MR_1774414236_15E92118 | 504990 | 535 | -93.1 | 504990 | 974 | -97.6 | 504990 | 679 | -105.1 | 504990 | 112 |
| MR_1774414236_4CA2120D | 504990 | 535 | -92.9 | 504990 | 974 | -99.6 | 504990 | 679 | -104.9 | 504990 | 112 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1814: `353aafe9-f45...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `353aafe9-f453-472a-ae94-ccabf4278bf3` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279629_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1814] topology](images/train_1814.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3279629_4
- `C2`: Adjust the azimuth of 3279629_4 by 35 degrees
- `C3`: Check test server and transmission issues
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Lift the tilt angle  of 3269431_3 by 5 degrees
- `C6`: Decrease transmission power for 3269431_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279629_4 **← 정답**
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269431_3
- `C9`: Press down the tilt angle  of 3269431_3 by 5 degrees
- `C10`: Lift the tilt angle of 3279629_4 by 2 degrees
- `C11`: Increase A3 Offset threshold for 3279629_4
- `C12`: Increase A3 Offset threshold for 3269431_3
- `C13`: Increase transmission power for 3279629_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269431_3
- `C15`: Decrease A3 Offset threshold for 3269431_3
- `C16`: Decrease transmission power for 3279629_4
- `C17`: Press down the tilt angle of 3279629_4 by 2 degrees
- `C18`: Adjust the azimuth of 3269431_3 by 13 degrees
- `C19`: Add neighbor relationship between 3270373_7 and 3269431_3
- `C20`: Add neighbor relationship between 3279629_4 and 3269431_3
- `C21`: Increase transmission power for 3269431_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279629_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.332 | MS1 | 121.4656585498 | 31.1446204929 | 399 | 504990 | -95.38 | 9.06 | 337.21 | 0.05 | 2.98 | 1586 |
| 2024-09-20 22:21:32.980 | MS1 | 121.4656598402 | 31.1446202904 | 747 | 504990 | -94.69 | 14.96 | 404.64 | 0.19 | 2.29 | 1586 |
| 2024-09-20 22:21:33.323 | MS1 | 121.4656621685 | 31.1446314523 | 88 | 504990 | -95.46 | 11.26 | 486.23 | 0.00 | 2.76 | 1575 |
| 2024-09-20 22:21:34.320 | MS1 | 121.4656690347 | 31.1446203906 | 90 | 152650 | -90.93 | 5.24 | 90.44 | 0.17 | 1.68 | 925 |
| 2024-09-20 22:21:35.173 | MS1 | 121.4656600493 | 31.1446347808 | 8 | 152650 | -90.00 | 6.94 | 97.37 | 0.19 | 1.53 | 966 |
| 2024-09-20 22:21:36.693 | MS1 | 121.4656778629 | 31.1446183782 | 420 | 152650 | -93.78 | 5.09 | 59.86 | 0.08 | 1.59 | 909 |
| 2024-09-20 22:21:37.753 | MS1 | 121.4656715493 | 31.1446361646 | 394 | 152650 | -88.80 | 7.33 | 99.61 | 0.16 | 1.66 | 979 |
| 2024-09-20 22:21:38.285 | MS1 | 121.4656607873 | 31.1446190268 | 90 | 152650 | -89.48 | 7.59 | 87.09 | 0.19 | 1.90 | 958 |
| 2024-09-20 22:21:39.786 | MS1 | 121.4656584996 | 31.1446344771 | 8 | 152650 | -93.43 | 2.09 | 71.60 | 0.09 | 1.97 | 977 |
| 2024-09-20 22:21:40.956 | MS1 | 121.4656627007 | 31.1446241320 | 420 | 152650 | -94.21 | 7.90 | 69.04 | 0.19 | 2.08 | 1598 |
| 2024-09-20 22:21:41.950 | MS1 | 121.4656683397 | 31.1446368929 | 394 | 152650 | -96.32 | 6.23 | 84.31 | 0.07 | 2.07 | 1575 |
| 2024-09-20 22:21:42.541 | MS1 | 121.4656741216 | 31.1446190656 | 90 | 152650 | -96.05 | 5.94 | 96.41 | 0.19 | 2.49 | 1597 |

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
| 3214053 | 8 | 121.4675018217 | 31.1518221841 | 61 | 4 | 2 | 28.0 | FDD | 8 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3216832 | 12 | 121.4712836109 | 31.1523613147 | 270 | 12 | 11 | 17.0 | FDD | 90 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3218371 | 13 | 121.4683967211 | 31.1458982049 | 334 | 14 | 10 | 8.9 | FDD | 30 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3222949 | 1 | 121.4697779957 | 31.1470090873 | 57 | 4 | 6 | 14.6 | TDD | 964 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3228216 | 11 | 121.4667380588 | 31.1456497625 | 267 | 10 | 0 | 7.8 | FDD | 151 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3236372 | 9 | 121.4696775889 | 31.1440571412 | 99 | 14 | 2 | 18.9 | FDD | 394 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3241122 | 2 | 121.4719246535 | 31.1548540382 | 157 | 15 | 3 | 13.0 | TDD | 747 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3247678 | 10 | 121.4661835813 | 31.1509055390 | 296 | 4 | 4 | 17.9 | FDD | 950 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3265591 | 6 | 121.4713128067 | 31.1453737020 | 354 | 6 | 6 | 12.6 | TDD | 633 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3266150 | 5 | 121.4691447069 | 31.1450217120 | 28 | 10 | 7 | 13.7 | TDD | 88 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3269431 | 3 | 121.4642600205 | 31.1510636913 | 156 | 3 | 0 | 19.4 | TDD | 620 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3270373 | 7 | 121.4685714172 | 31.1458756621 | 255 | 12 | 0 | 15.1 | FDD | 420 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3279629 | 4 | 121.4675250839 | 31.1496945166 | 162 | 0 | 9 | 19.3 | TDD | 399 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.951 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.966 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.091 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.091 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.811 | NREventA2 | measId:1;ServCellPCI:344;Se... |
| 2024-09-20 22:21:34.943 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.176 | NREventA5 | measId:3;ServCellPCI:344;Se... |
| 2024-09-20 22:21:35.253 | NRHandoverAttempt | SourcePCI:344;SourceNR-ARFC... |
| 2024-09-20 22:21:35.299 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.309 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.438 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.438 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222949 | 1 | 5.1856 | 5.7097 | -117.6499 | 10.4131 | 192.5048 | 0.0043 | 0.0183 |
| 2024_09_20 22:00 | 3241122 | 2 | 16.9712 | 11.2476 | -114.5954 | 16.9302 | 154.5620 | 0.0011 | 0.0148 |
| 2024_09_20 22:00 | 3269431 | 3 | 11.3904 | 16.0103 | -115.9297 | 18.7959 | 192.7207 | 0.0179 | 0.0112 |
| 2024_09_20 22:00 | 3279629 | 4 | 16.9066 | 9.1890 | -114.1082 | 18.5070 | 140.3432 | 0.0080 | 0.0162 |
| 2024_09_20 22:00 | 3266150 | 5 | 15.6698 | 5.4405 | -114.3753 | 10.1060 | 136.6687 | 0.0113 | 0.0003 |
| 2024_09_20 22:00 | 3265591 | 6 | 6.4549 | 17.1515 | -116.4972 | 6.2933 | 120.3568 | 0.0166 | 0.0081 |
| 2024_09_20 22:00 | 3270373 | 7 | 11.3391 | 13.4298 | -114.6024 | 4.0723 | 51.5965 | 0.0062 | 0.0139 |
| 2024_09_20 22:00 | 3214053 | 8 | 11.3648 | 18.4126 | -114.1086 | 3.7173 | 51.2668 | 0.0016 | 0.0098 |
| 2024_09_20 22:00 | 3236372 | 9 | 19.1545 | 12.7729 | -115.2603 | 3.5723 | 58.3874 | 0.0019 | 0.0188 |
| 2024_09_20 22:00 | 3247678 | 10 | 13.3335 | 11.0611 | -115.0267 | 3.3167 | 45.0968 | 0.0033 | 0.0125 |
| 2024_09_20 22:00 | 3228216 | 11 | 12.5601 | 13.1978 | -116.3809 | 3.9202 | 47.7874 | 0.0131 | 0.0129 |
| 2024_09_20 22:00 | 3216832 | 12 | 17.6349 | 12.9574 | -116.7989 | 4.3161 | 40.3276 | 0.0096 | 0.0172 |
| 2024_09_20 22:00 | 3218371 | 13 | 10.9418 | 10.5542 | -115.3542 | 4.9381 | 22.3625 | 0.0153 | 0.0124 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416044_8870CE3C | 152650 | 90 | -92.4 | 152650 | 151 | -95.8 | 152650 | 950 | -100.6 | 152650 | 30 |
| MR_1774416044_70FF5C22 | 504990 | 88 | -96.0 | 504990 | 620 | -95.8 | 504990 | 964 | -99.6 | 504990 | 633 |
| MR_1774416044_74596868 | 152650 | 90 | -89.7 | 152650 | 151 | -95.7 | 152650 | 950 | -101.9 | 152650 | 30 |
| MR_1774416044_9A144596 | 504990 | 88 | -96.8 | 504990 | 620 | -92.5 | 504990 | 964 | -96.9 | 504990 | 633 |
| MR_1774416044_8F4F4728 | 504990 | 88 | -97.0 | 504990 | 620 | -92.4 | 504990 | 964 | -99.5 | 504990 | 633 |
| MR_1774416044_0E4649BD | 152650 | 90 | -91.1 | 152650 | 151 | -97.3 | 152650 | 950 | -100.3 | 152650 | 30 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1815: `e8d53b0d-fd8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e8d53b0d-fd8d-41ff-9979-53b80fdc797a` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278401_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1815] topology](images/train_1815.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3264663_5 by 2 degrees
- `C2`: Press down the tilt angle of 3278401_1 by 3 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase transmission power for 3278401_1
- `C5`: Increase transmission power for 3264663_5
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264663_5
- `C7`: Adjust the azimuth of 3278401_1 by 16 degrees
- `C8`: Increase A3 Offset threshold for 3264663_5
- `C9`: Check test server and transmission issues
- `C10`: Add neighbor relationship between 3265272_7 and 3264663_5
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264663_5
- `C12`: Adjust the azimuth of 3264663_5 by 0 degrees
- `C13`: Decrease A3 Offset threshold for 3278401_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278401_1 **← 정답**
- `C15`: Decrease transmission power for 3264663_5
- `C16`: Lift the tilt angle  of 3264663_5 by 2 degrees
- `C17`: Decrease transmission power for 3278401_1
- `C18`: Increase A3 Offset threshold for 3278401_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278401_1
- `C20`: Add neighbor relationship between 3278401_1 and 3264663_5
- `C21`: Lift the tilt angle of 3278401_1 by 3 degrees
- `C22`: Decrease A3 Offset threshold for 3264663_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.689 | MS1 | 121.4656758840 | 31.1446208483 | 740 | 504990 | -95.18 | 14.37 | 396.37 | 0.19 | 2.07 | 1590 |
| 2024-09-20 22:21:32.213 | MS1 | 121.4656701176 | 31.1446295474 | 370 | 504990 | -95.17 | 9.57 | 430.80 | 0.15 | 2.26 | 1584 |
| 2024-09-20 22:21:33.806 | MS1 | 121.4656595053 | 31.1446196043 | 904 | 504990 | -95.12 | 12.96 | 388.93 | 0.20 | 2.27 | 1598 |
| 2024-09-20 22:21:34.673 | MS1 | 121.4656701410 | 31.1446295462 | 472 | 152650 | -93.13 | 6.80 | 97.49 | 0.13 | 1.69 | 938 |
| 2024-09-20 22:21:35.581 | MS1 | 121.4656712849 | 31.1446230321 | 700 | 152650 | -90.07 | 6.04 | 88.25 | 0.02 | 1.88 | 979 |
| 2024-09-20 22:21:36.928 | MS1 | 121.4656700986 | 31.1446239400 | 555 | 152650 | -96.60 | 3.47 | 93.56 | 0.12 | 1.50 | 987 |
| 2024-09-20 22:21:37.148 | MS1 | 121.4656733083 | 31.1446204578 | 526 | 152650 | -87.81 | 3.21 | 66.05 | 0.08 | 1.70 | 965 |
| 2024-09-20 22:21:38.390 | MS1 | 121.4656583099 | 31.1446314417 | 472 | 152650 | -91.91 | 5.22 | 68.90 | 0.17 | 1.92 | 971 |
| 2024-09-20 22:21:39.845 | MS1 | 121.4656673054 | 31.1446370940 | 700 | 152650 | -94.00 | 5.66 | 81.26 | 0.15 | 1.97 | 944 |
| 2024-09-20 22:21:40.867 | MS1 | 121.4656734104 | 31.1446246742 | 555 | 152650 | -95.76 | 5.42 | 88.66 | 0.08 | 2.20 | 1589 |
| 2024-09-20 22:21:41.897 | MS1 | 121.4656691524 | 31.1446240644 | 526 | 152650 | -93.75 | 2.72 | 57.78 | 0.05 | 2.75 | 1597 |
| 2024-09-20 22:21:42.218 | MS1 | 121.4656722344 | 31.1446212277 | 472 | 152650 | -90.48 | 2.07 | 54.14 | 0.18 | 2.65 | 1600 |

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
| 3212727 | 8 | 121.4719312271 | 31.1454482410 | 297 | 8 | 4 | 26.3 | FDD | 526 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3212729 | 12 | 121.4648907380 | 31.1537833107 | 99 | 2 | 10 | 22.6 | FDD | 472 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3234377 | 13 | 121.4676817752 | 31.1477864890 | 97 | 0 | 3 | 29.9 | FDD | 700 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3246365 | 11 | 121.4674890192 | 31.1459477154 | 300 | 14 | 9 | 18.1 | FDD | 855 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3248605 | 2 | 121.4671318194 | 31.1478466932 | 82 | 7 | 7 | 22.4 | TDD | 904 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3253204 | 4 | 121.4643916603 | 31.1544743231 | 161 | 1 | 10 | 19.9 | TDD | 370 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3259703 | 6 | 121.4684311994 | 31.1445899287 | 312 | 5 | 4 | 7.6 | TDD | 668 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3259993 | 10 | 121.4730090781 | 31.1533087250 | 81 | 2 | 3 | 5.4 | FDD | 565 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3260675 | 9 | 121.4695793829 | 31.1459607934 | 193 | 7 | 10 | 17.9 | FDD | 756 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3264663 | 5 | 121.4699183484 | 31.1509730693 | 210 | 1 | 2 | 8.6 | TDD | 884 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3265272 | 7 | 121.4715275010 | 31.1456284552 | 114 | 5 | 0 | 6.1 | FDD | 555 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3272258 | 3 | 121.4705593605 | 31.1481127317 | 179 | 15 | 12 | 4.0 | TDD | 750 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3278401 | 1 | 121.4710954195 | 31.1545505264 | 189 | 2 | 8 | 10.8 | TDD | 740 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.986 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.005 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.115 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.115 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.858 | NREventA2 | measId:1;ServCellPCI:1004;S... |
| 2024-09-20 22:21:34.958 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.217 | NREventA5 | measId:3;ServCellPCI:1004;S... |
| 2024-09-20 22:21:35.262 | NRHandoverAttempt | SourcePCI:1004;SourceNR-ARF... |
| 2024-09-20 22:21:35.298 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.311 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.458 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.458 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278401 | 1 | 18.7007 | 6.1604 | -116.0057 | 8.4153 | 192.3416 | 0.0075 | 0.0002 |
| 2024_09_20 22:00 | 3248605 | 2 | 15.1944 | 15.1405 | -115.5819 | 17.2151 | 152.6619 | 0.0071 | 0.0026 |
| 2024_09_20 22:00 | 3272258 | 3 | 19.3701 | 10.2576 | -116.0291 | 8.0198 | 171.9552 | 0.0099 | 0.0052 |
| 2024_09_20 22:00 | 3253204 | 4 | 15.2690 | 16.4110 | -116.4655 | 6.9876 | 181.0942 | 0.0035 | 0.0017 |
| 2024_09_20 22:00 | 3264663 | 5 | 11.3813 | 17.5482 | -114.6242 | 19.1204 | 146.6317 | 0.0190 | 0.0069 |
| 2024_09_20 22:00 | 3259703 | 6 | 19.9341 | 8.0529 | -117.5608 | 16.4372 | 180.8256 | 0.0082 | 0.0135 |
| 2024_09_20 22:00 | 3265272 | 7 | 10.6473 | 11.3020 | -116.8070 | 4.5344 | 30.1185 | 0.0005 | 0.0169 |
| 2024_09_20 22:00 | 3212727 | 8 | 18.4867 | 15.6591 | -115.3352 | 4.5768 | 33.7290 | 0.0093 | 0.0035 |
| 2024_09_20 22:00 | 3260675 | 9 | 5.2615 | 12.0843 | -117.1645 | 4.2983 | 42.1237 | 0.0183 | 0.0138 |
| 2024_09_20 22:00 | 3259993 | 10 | 13.8731 | 7.1358 | -115.6240 | 3.8650 | 33.2789 | 0.0124 | 0.0064 |
| 2024_09_20 22:00 | 3246365 | 11 | 11.0284 | 8.4090 | -114.5429 | 3.9129 | 53.3896 | 0.0052 | 0.0138 |
| 2024_09_20 22:00 | 3212729 | 12 | 16.6355 | 5.8002 | -114.1938 | 4.0852 | 45.7333 | 0.0140 | 0.0109 |
| 2024_09_20 22:00 | 3234377 | 13 | 11.7861 | 14.2709 | -114.2794 | 4.3334 | 26.5103 | 0.0173 | 0.0114 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415764_FEE0ABF2 | 152650 | 472 | -93.9 | 152650 | 855 | -99.1 | 152650 | 756 | -102.3 | 152650 | 565 |
| MR_1774415764_D9EBE717 | 504990 | 904 | -94.9 | 504990 | 884 | -95.3 | 504990 | 750 | -98.9 | 504990 | 668 |
| MR_1774415764_0F393BD2 | 152650 | 472 | -92.5 | 152650 | 855 | -98.0 | 152650 | 756 | -101.1 | 152650 | 565 |
| MR_1774415764_8A3F8DB7 | 504990 | 904 | -93.7 | 504990 | 884 | -96.9 | 504990 | 750 | -100.9 | 504990 | 668 |
| MR_1774415764_5BBA8C7D | 504990 | 904 | -95.5 | 504990 | 884 | -97.5 | 504990 | 750 | -98.4 | 504990 | 668 |
| MR_1774415764_0BDF773E | 152650 | 472 | -95.1 | 152650 | 855 | -98.3 | 152650 | 756 | -102.6 | 152650 | 565 |
| MR_1774415764_BFD77AC2 | 152650 | 472 | -91.2 | 152650 | 855 | -96.5 | 152650 | 756 | -103.1 | 152650 | 565 |
| MR_1774415764_EF888C3E | 504990 | 904 | -93.2 | 504990 | 884 | -98.0 | 504990 | 750 | -98.8 | 504990 | 668 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1816: `89e443af-c70...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `89e443af-c709-4f9d-8d34-768e408c8b5d` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3270818_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1816] topology](images/train_1816.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Lift the tilt angle of 3270818_1 by 1 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270818_1 **← 정답**
- `C4`: Increase transmission power for 3270818_1
- `C5`: Decrease transmission power for 3270818_1
- `C6`: Lift the tilt angle  of 3258644_4 by 10 degrees
- `C7`: Adjust the azimuth of 3258644_4 by 50 degrees
- `C8`: Adjust the azimuth of 3270818_1 by 36 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270818_1
- `C10`: Decrease A3 Offset threshold for 3258644_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258644_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258644_4
- `C13`: Decrease transmission power for 3258644_4
- `C14`: Press down the tilt angle  of 3258644_4 by 10 degrees
- `C15`: Increase A3 Offset threshold for 3270818_1
- `C16`: Add neighbor relationship between 3270818_1 and 3258644_4
- `C17`: Increase A3 Offset threshold for 3258644_4
- `C18`: Decrease A3 Offset threshold for 3270818_1
- `C19`: Add neighbor relationship between 3231540_3 and 3258644_4
- `C20`: Increase transmission power for 3258644_4
- `C21`: Press down the tilt angle of 3270818_1 by 1 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.830 | MS1 | 121.4656696796 | 31.1446332554 | 792 | 504990 | -87.13 | 12.83 | 425.71 | 0.13 | 2.49 | 1571 |
| 2024-09-20 22:21:32.391 | MS1 | 121.4656692803 | 31.1446182331 | 792 | 504990 | -87.63 | 17.98 | 328.77 | 0.14 | 2.95 | 1595 |
| 2024-09-20 22:21:33.224 | MS1 | 121.4656647478 | 31.1446328072 | 792 | 504990 | -89.59 | 16.26 | 575.28 | 0.05 | 2.78 | 1579 |
| 2024-09-20 22:21:34.524 | MS1 | 121.4656634599 | 31.1446185044 | 792 | 504990 | -89.24 | 17.48 | 78.17 | 0.68 | 2.21 | 651 |
| 2024-09-20 22:21:35.670 | MS1 | 121.4656667247 | 31.1446204111 | 792 | 504990 | -86.57 | 17.94 | 44.00 | 0.52 | 2.84 | 690 |
| 2024-09-20 22:21:36.138 | MS1 | 121.4656760428 | 31.1446208411 | 792 | 504990 | -85.77 | 12.32 | 67.23 | 0.52 | 2.75 | 690 |
| 2024-09-20 22:21:37.879 | MS1 | 121.4656649792 | 31.1446369863 | 792 | 504990 | -93.36 | 7.72 | 54.55 | 0.66 | 2.65 | 589 |
| 2024-09-20 22:21:38.664 | MS1 | 121.4656585900 | 31.1446293900 | 792 | 504990 | -92.02 | 10.62 | 77.99 | 0.53 | 2.03 | 555 |
| 2024-09-20 22:21:39.403 | MS1 | 121.4656665654 | 31.1446350505 | 792 | 504990 | -91.81 | 10.98 | 83.11 | 0.59 | 2.02 | 680 |
| 2024-09-20 22:21:40.166 | MS1 | 121.4656753762 | 31.1446376021 | 792 | 504990 | -92.90 | 12.40 | 458.79 | 0.02 | 2.28 | 1568 |
| 2024-09-20 22:21:41.164 | MS1 | 121.4656768629 | 31.1446180409 | 792 | 504990 | -92.56 | 9.13 | 560.12 | 0.17 | 2.27 | 1570 |
| 2024-09-20 22:21:42.591 | MS1 | 121.4656704899 | 31.1446182714 | 792 | 504990 | -90.75 | 10.99 | 425.39 | 0.07 | 2.23 | 1575 |

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
| 3212801 | 2 | 121.4700811385 | 31.1443674507 | 288 | 7 | 0 | 21.2 | TDD | 776 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3231540 | 3 | 121.4663953844 | 31.1465821701 | 75 | 0 | 3 | 40.9 | TDD | 147 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3258644 | 4 | 121.4724136905 | 31.1508361959 | 16 | 7 | 11 | 42.0 | TDD | 910 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3270818 | 1 | 121.4710300537 | 31.1548076230 | 240 | 0 | 6 | 28.1 | TDD | 792 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.777 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.792 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.935 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.935 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.677 | NREventA3 | measId:2;ServCellPCI:24;Ser... |
| 2024-09-20 22:21:37.917 | NRHandoverAttempt | SourcePCI:24;SourceNR-ARFCN... |
| 2024-09-20 22:21:37.958 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.968 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.089 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.089 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270818 | 1 | 7.7435 | 16.1180 | -117.4552 | 12.4580 | 166.2188 | 0.0079 | 0.0159 |
| 2024_09_20 22:00 | 3212801 | 2 | 10.0237 | 8.8806 | -114.9114 | 7.3374 | 97.4403 | 0.0161 | 0.0087 |
| 2024_09_20 22:00 | 3231540 | 3 | 7.6537 | 19.1923 | -117.8619 | 8.8593 | 160.8334 | 0.0122 | 0.0186 |
| 2024_09_20 22:00 | 3258644 | 4 | 18.0405 | 5.0970 | -117.2500 | 14.4397 | 169.6273 | 0.0053 | 0.0014 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417080_313411F6 | 504990 | 792 | -90.2 | 504990 | 910 | -91.8 | 504990 | 147 | -96.5 | 504990 | 776 |
| MR_1774417080_3C57D2AE | 504990 | 792 | -88.5 | 504990 | 910 | -90.6 | 504990 | 147 | -97.0 | 504990 | 776 |
| MR_1774417080_7527DB1D | 504990 | 792 | -88.3 | 504990 | 910 | -91.0 | 504990 | 147 | -99.1 | 504990 | 776 |
| MR_1774417080_46848552 | 504990 | 792 | -88.2 | 504990 | 910 | -94.0 | 504990 | 147 | -98.3 | 504990 | 776 |
| MR_1774417080_76463FFE | 504990 | 792 | -88.4 | 504990 | 910 | -92.0 | 504990 | 147 | -97.4 | 504990 | 776 |
| MR_1774417080_7C085D9C | 504990 | 792 | -90.6 | 504990 | 910 | -93.4 | 504990 | 147 | -97.8 | 504990 | 776 |
| MR_1774417080_E261247D | 504990 | 792 | -90.6 | 504990 | 910 | -90.8 | 504990 | 147 | -96.0 | 504990 | 776 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1817: `c341c229-8b9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c341c229-8b9f-4f8b-b4d8-1d3492aa113d` |
| Tag | **multiple-answer** |
| 정답 | **C20|C21** |
| C20 의미 | Press down the tilt angle  of 3232896_4 by 3 degrees |
| C21 의미 | Decrease transmission power for 3232896_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1817] topology](images/train_1817.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250434_2
- `C2`: Add neighbor relationship between 3250434_2 and 3232896_4
- `C3`: Decrease A3 Offset threshold for 3250434_2
- `C4`: Increase A3 Offset threshold for 3250434_2
- `C5`: Check test server and transmission issues
- `C6`: Press down the tilt angle of 3250434_2 by 5 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250434_2
- `C9`: Increase transmission power for 3250434_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232896_4
- `C11`: Adjust the azimuth of 3250434_2 by 24 degrees
- `C12`: Increase A3 Offset threshold for 3232896_4
- `C13`: Decrease A3 Offset threshold for 3232896_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232896_4
- `C15`: Add neighbor relationship between 3274969_3 and 3232896_4
- `C16`: Lift the tilt angle  of 3232896_4 by 3 degrees
- `C17`: Lift the tilt angle of 3250434_2 by 5 degrees
- `C18`: Adjust the azimuth of 3232896_4 by 10 degrees
- `C19`: Increase transmission power for 3232896_4
- `C20`: Press down the tilt angle  of 3232896_4 by 3 degrees **← 정답**
- `C21`: Decrease transmission power for 3232896_4 **← 정답**
- `C22`: Decrease transmission power for 3250434_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.816 | MS1 | 121.4656706034 | 31.1446368857 | 730 | 504990 | -80.80 | 12.66 | 566.39 | 0.18 | 2.39 | 1588 |
| 2024-09-20 22:21:32.804 | MS1 | 121.4656746709 | 31.1446224208 | 730 | 504990 | -78.33 | 12.06 | 307.15 | 0.05 | 2.21 | 1577 |
| 2024-09-20 22:21:33.860 | MS1 | 121.4656686406 | 31.1446252129 | 730 | 504990 | -77.44 | 16.56 | 438.71 | 0.05 | 2.31 | 1566 |
| 2024-09-20 22:21:34.161 | MS1 | 121.4656702508 | 31.1446232482 | 730 | 504990 | -87.63 | 0.11 | 73.94 | 0.17 | 1.37 | 1596 |
| 2024-09-20 22:21:35.354 | MS1 | 121.4656613032 | 31.1446289233 | 730 | 504990 | -88.36 | 2.63 | 60.98 | 0.18 | 1.21 | 1600 |
| 2024-09-20 22:21:36.694 | MS1 | 121.4656672981 | 31.1446271885 | 730 | 504990 | -86.81 | 0.01 | 39.77 | 0.19 | 1.25 | 1574 |
| 2024-09-20 22:21:37.745 | MS1 | 121.4656767098 | 31.1446332544 | 730 | 504990 | -94.54 | 2.88 | 58.90 | 0.16 | 1.22 | 1563 |
| 2024-09-20 22:21:38.593 | MS1 | 121.4656728734 | 31.1446377372 | 730 | 504990 | -87.44 | 3.08 | 46.28 | 0.18 | 1.38 | 1571 |
| 2024-09-20 22:21:39.774 | MS1 | 121.4656693957 | 31.1446202101 | 730 | 504990 | -93.82 | 1.27 | 92.04 | 0.00 | 1.10 | 1580 |
| 2024-09-20 22:21:40.737 | MS1 | 121.4656580049 | 31.1446253880 | 730 | 504990 | -77.84 | 16.90 | 544.21 | 0.05 | 2.77 | 1566 |
| 2024-09-20 22:21:41.546 | MS1 | 121.4656677754 | 31.1446311312 | 730 | 504990 | -77.64 | 17.57 | 573.99 | 0.13 | 3.00 | 1562 |
| 2024-09-20 22:21:42.231 | MS1 | 121.4656683740 | 31.1446368202 | 730 | 504990 | -81.49 | 16.13 | 454.19 | 0.08 | 2.00 | 1566 |

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
| 3232896 | 4 | 121.4733990455 | 31.1529616087 | 208 | 1 | 8 | 43.1 | TDD | 119 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3250434 | 2 | 121.4706548663 | 31.1465946702 | 269 | 2 | 4 | 29.4 | TDD | 730 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3272192 | 1 | 121.4741419771 | 31.1498742744 | 186 | 7 | 7 | 30.1 | TDD | 985 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3274969 | 3 | 121.4654574270 | 31.1522867429 | 53 | 12 | 2 | 30.5 | TDD | 851 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.190 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.213 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.362 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.362 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272192 | 1 | 18.0944 | 12.2305 | -117.2190 | 7.3303 | 155.6282 | 0.0006 | 0.0157 |
| 2024_09_20 22:00 | 3250434 | 2 | 6.3535 | 12.1948 | -109.0108 | 11.2419 | 149.4839 | 0.0136 | 0.0126 |
| 2024_09_20 22:00 | 3274969 | 3 | 16.3028 | 7.5981 | -116.3052 | 5.7564 | 133.4002 | 0.0054 | 0.0123 |
| 2024_09_20 22:00 | 3232896 | 4 | 18.6121 | 19.5909 | -115.4746 | 17.6971 | 117.2298 | 0.0141 | 0.0019 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413111_C37CE267 | 504990 | 119 | -88.2 | 504990 | 730 | -83.7 | 504990 | 851 | -84.4 | 504990 | 985 |
| MR_1774413111_95DB493D | 504990 | 730 | -88.3 | 504990 | 119 | -85.0 | 504990 | 851 | -87.2 | 504990 | 985 |
| MR_1774413111_ADEF349F | 504990 | 730 | -86.0 | 504990 | 119 | -86.1 | 504990 | 851 | -87.4 | 504990 | 985 |
| MR_1774413111_CAB50B05 | 504990 | 119 | -86.0 | 504990 | 730 | -86.2 | 504990 | 851 | -85.1 | 504990 | 985 |
| MR_1774413111_CC979536 | 504990 | 119 | -86.9 | 504990 | 730 | -85.2 | 504990 | 851 | -84.6 | 504990 | 985 |
| MR_1774413111_C9D09062 | 504990 | 730 | -86.7 | 504990 | 119 | -83.4 | 504990 | 851 | -87.5 | 504990 | 985 |
| MR_1774413111_26C6A8B3 | 504990 | 119 | -88.4 | 504990 | 730 | -85.5 | 504990 | 851 | -84.6 | 504990 | 985 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1818: `f9a5318c-31a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f9a5318c-31a3-4cfa-8245-b6d9937253fa` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Add neighbor relationship between 3244731_2 and 3211146_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1818] topology](images/train_1818.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3211146_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211146_3
- `C3`: Adjust the azimuth of 3244731_2 by 50 degrees
- `C4`: Increase A3 Offset threshold for 3211146_3
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease transmission power for 3244731_2
- `C7`: Press down the tilt angle  of 3211146_3 by 5 degrees
- `C8`: Add neighbor relationship between 3210171_4 and 3211146_3
- `C9`: Decrease A3 Offset threshold for 3244731_2
- `C10`: Adjust the azimuth of 3211146_3 by 49 degrees
- `C11`: Press down the tilt angle of 3244731_2 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244731_2
- `C13`: Lift the tilt angle of 3244731_2 by 10 degrees
- `C14`: Increase transmission power for 3211146_3
- `C15`: Decrease A3 Offset threshold for 3211146_3
- `C16`: Add neighbor relationship between 3244731_2 and 3211146_3 **← 정답**
- `C17`: Increase transmission power for 3244731_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244731_2
- `C19`: Check test server and transmission issues
- `C20`: Lift the tilt angle  of 3211146_3 by 5 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211146_3
- `C22`: Increase A3 Offset threshold for 3244731_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.342 | MS1 | 121.4656585092 | 31.1446260071 | 28 | 504990 | -75.63 | 12.71 | 446.19 | 0.18 | 2.64 | 1565 |
| 2024-09-20 22:21:32.607 | MS1 | 121.4656716821 | 31.1446318123 | 28 | 504990 | -81.69 | 14.10 | 352.44 | 0.05 | 2.27 | 1588 |
| 2024-09-20 22:21:33.412 | MS1 | 121.4656719801 | 31.1446209698 | 28 | 504990 | -79.90 | 15.77 | 433.10 | 0.12 | 2.99 | 1563 |
| 2024-09-20 22:21:34.445 | MS1 | 121.4656701844 | 31.1446206880 | 28 | 504990 | -87.09 | -3.36 | 36.97 | 0.01 | 1.18 | 1578 |
| 2024-09-20 22:21:35.589 | MS1 | 121.4656626331 | 31.1446378327 | 28 | 504990 | -89.06 | -0.07 | 72.13 | 0.11 | 1.15 | 1580 |
| 2024-09-20 22:21:36.726 | MS1 | 121.4656773751 | 31.1446322638 | 28 | 504990 | -86.17 | -3.91 | 52.77 | 0.09 | 1.14 | 1572 |
| 2024-09-20 22:21:37.864 | MS1 | 121.4656628686 | 31.1446351696 | 28 | 504990 | -86.28 | -0.57 | 56.98 | 0.05 | 1.01 | 1569 |
| 2024-09-20 22:21:38.737 | MS1 | 121.4656591867 | 31.1446266117 | 28 | 504990 | -75.86 | 15.10 | 492.08 | 0.03 | 1.47 | 1579 |
| 2024-09-20 22:21:39.989 | MS1 | 121.4656768092 | 31.1446354379 | 28 | 504990 | -84.38 | 14.05 | 343.32 | 0.13 | 1.29 | 1580 |
| 2024-09-20 22:21:40.840 | MS1 | 121.4656598621 | 31.1446280000 | 28 | 504990 | -82.32 | 17.32 | 509.65 | 0.18 | 2.31 | 1598 |
| 2024-09-20 22:21:41.538 | MS1 | 121.4656701507 | 31.1446347300 | 28 | 504990 | -80.48 | 14.37 | 558.47 | 0.18 | 2.27 | 1585 |
| 2024-09-20 22:21:42.697 | MS1 | 121.4656760623 | 31.1446356935 | 28 | 504990 | -79.97 | 16.02 | 454.46 | 0.18 | 2.66 | 1578 |

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
| 3210171 | 4 | 121.4716314874 | 31.1500189630 | 17 | 11 | 2 | 45.2 | TDD | 871 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3211146 | 3 | 121.4719666540 | 31.1474915925 | 291 | 4 | 11 | 17.4 | TDD | 127 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3244731 | 2 | 121.4686798717 | 31.1529577419 | 90 | 15 | 8 | 28.6 | TDD | 28 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3247624 | 1 | 121.4714804926 | 31.1494516916 | 109 | 3 | 7 | 32.1 | TDD | 34 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.332 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.355 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.472 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.472 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.159 | NREventA3 | measId:2;ServCellPCI:753;Se... |
| 2024-09-20 22:21:36.159 | NREventA3 | measId:2;ServCellPCI:753;Se... |
| 2024-09-20 22:21:37.159 | NREventA3 | measId:2;ServCellPCI:753;Se... |
| 2024-09-20 22:21:39.659 | NRRRCReestablishAttempt | PCI:753 |
| 2024-09-20 22:21:39.670 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.684 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.807 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.807 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247624 | 1 | 14.5224 | 14.1793 | -115.5077 | 19.9849 | 172.2265 | 0.0130 | 0.0061 |
| 2024_09_20 22:00 | 3244731 | 2 | 6.9251 | 13.7902 | -114.2319 | 19.1148 | 88.6907 | 0.0076 | 0.1684 |
| 2024_09_20 22:00 | 3211146 | 3 | 18.0387 | 18.4459 | -115.5793 | 5.9048 | 113.8899 | 0.0024 | 0.0082 |
| 2024_09_20 22:00 | 3210171 | 4 | 9.3933 | 6.5718 | -114.7695 | 13.9728 | 96.4433 | 0.0183 | 0.0168 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413264_12F5D118 | 504990 | 127 | -81.9 | 504990 | 28 | -88.3 | 504990 | 871 | -85.6 | 504990 | 34 |
| MR_1774413264_CD160383 | 504990 | 28 | -86.1 | 504990 | 127 | -82.4 | 504990 | 871 | -85.3 | 504990 | 34 |
| MR_1774413264_2DDF73BE | 504990 | 127 | -81.2 | 504990 | 28 | -85.5 | 504990 | 871 | -86.8 | 504990 | 34 |
| MR_1774413264_2AA0671E | 504990 | 28 | -87.8 | 504990 | 127 | -81.6 | 504990 | 871 | -85.3 | 504990 | 34 |
| MR_1774413264_1325AB7D | 504990 | 127 | -82.6 | 504990 | 28 | -86.0 | 504990 | 871 | -84.8 | 504990 | 34 |
| MR_1774413264_C31BB97F | 504990 | 28 | -87.8 | 504990 | 127 | -84.6 | 504990 | 871 | -87.2 | 504990 | 34 |
| MR_1774413264_CE863B3A | 504990 | 127 | -84.8 | 504990 | 28 | -87.3 | 504990 | 871 | -86.1 | 504990 | 34 |
| MR_1774413264_ACEB978B | 504990 | 28 | -86.1 | 504990 | 127 | -81.0 | 504990 | 871 | -88.0 | 504990 | 34 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1819: `8060787b-bca...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8060787b-bcab-4dd6-b00d-1c23d9e00960` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1819] topology](images/train_1819.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3230086_3
- `C2`: Press down the tilt angle  of 3230086_3 by 10 degrees
- `C3`: Increase A3 Offset threshold for 3213290_2
- `C4`: Add neighbor relationship between 3274134_4 and 3230086_3
- `C5`: Decrease A3 Offset threshold for 3213290_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230086_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213290_2
- `C8`: Press down the tilt angle of 3213290_2 by 10 degrees
- `C9`: Decrease transmission power for 3230086_3
- `C10`: Check test server and transmission issues **← 정답**
- `C11`: Increase transmission power for 3213290_2
- `C12`: Lift the tilt angle of 3213290_2 by 10 degrees
- `C13`: Decrease transmission power for 3213290_2
- `C14`: Increase transmission power for 3230086_3
- `C15`: Add neighbor relationship between 3213290_2 and 3230086_3
- `C16`: Lift the tilt angle  of 3230086_3 by 10 degrees
- `C17`: Adjust the azimuth of 3230086_3 by 23 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Adjust the azimuth of 3213290_2 by 4 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230086_3
- `C21`: Decrease A3 Offset threshold for 3230086_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213290_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.312 | MS1 | 121.4656649957 | 31.1446312385 | 886 | 504990 | -91.20 | 17.34 | 481.72 | 0.04 | 2.55 | 1561 |
| 2024-09-20 22:21:32.315 | MS1 | 121.4656679523 | 31.1446261281 | 886 | 504990 | -90.68 | 16.44 | 471.19 | 0.08 | 2.36 | 1597 |
| 2024-09-20 22:21:33.608 | MS1 | 121.4656708405 | 31.1446275447 | 886 | 504990 | -89.96 | 13.77 | 376.41 | 0.00 | 2.40 | 1597 |
| 2024-09-20 22:21:34.380 | MS1 | 121.4656709949 | 31.1446208929 | 886 | 504990 | -88.64 | 12.50 | 58.43 | 0.17 | 2.13 | 467 |
| 2024-09-20 22:21:35.716 | MS1 | 121.4656650365 | 31.1446336279 | 886 | 504990 | -91.91 | 16.56 | 56.98 | 0.00 | 2.79 | 396 |
| 2024-09-20 22:21:36.421 | MS1 | 121.4656586769 | 31.1446219268 | 886 | 504990 | -85.70 | 14.78 | 84.91 | 0.16 | 2.23 | 301 |
| 2024-09-20 22:21:37.461 | MS1 | 121.4656760940 | 31.1446245351 | 886 | 504990 | -91.10 | 11.76 | 53.13 | 0.16 | 2.70 | 461 |
| 2024-09-20 22:21:38.100 | MS1 | 121.4656611697 | 31.1446237581 | 886 | 504990 | -93.52 | 8.92 | 59.16 | 0.08 | 2.46 | 485 |
| 2024-09-20 22:21:39.226 | MS1 | 121.4656713370 | 31.1446251747 | 886 | 504990 | -91.96 | 10.91 | 61.84 | 0.01 | 2.15 | 353 |
| 2024-09-20 22:21:40.183 | MS1 | 121.4656718900 | 31.1446234321 | 886 | 504990 | -91.37 | 10.99 | 357.84 | 0.07 | 2.62 | 1586 |
| 2024-09-20 22:21:41.603 | MS1 | 121.4656678540 | 31.1446234757 | 886 | 504990 | -93.34 | 10.21 | 315.88 | 0.11 | 2.39 | 1565 |
| 2024-09-20 22:21:42.939 | MS1 | 121.4656746422 | 31.1446340475 | 886 | 504990 | -93.52 | 11.43 | 540.70 | 0.17 | 2.00 | 1598 |

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
| 3213290 | 2 | 121.4665935689 | 31.1453305763 | 232 | 9 | 12 | 34.7 | TDD | 886 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3230086 | 3 | 121.4689305516 | 31.1517623808 | 224 | 13 | 4 | 49.1 | TDD | 861 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3263247 | 1 | 121.4643726302 | 31.1559067488 | 212 | 1 | 6 | 43.2 | TDD | 328 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3274134 | 4 | 121.4657462717 | 31.1542616714 | 346 | 2 | 6 | 39.9 | TDD | 846 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.969 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.990 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.140 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.140 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.859 | NREventA3 | measId:2;ServCellPCI:980;Se... |
| 2024-09-20 22:21:38.099 | NRHandoverAttempt | SourcePCI:980;SourceNR-ARFC... |
| 2024-09-20 22:21:38.132 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.144 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.253 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.253 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263247 | 1 | 7.7836 | 11.6014 | -116.9421 | 16.5786 | 131.9322 | 0.0172 | 0.0185 |
| 2024_09_20 22:00 | 3213290 | 2 | 13.8768 | 10.5773 | -114.9228 | 5.4548 | 118.9471 | 0.0078 | 0.0160 |
| 2024_09_20 22:00 | 3230086 | 3 | 5.0525 | 12.0166 | -114.8224 | 6.8993 | 130.2977 | 0.0078 | 0.0010 |
| 2024_09_20 22:00 | 3274134 | 4 | 14.8019 | 15.4640 | -115.7034 | 9.7256 | 80.8212 | 0.0078 | 0.0056 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413781_D11B88E7 | 504990 | 886 | -88.3 | 504990 | 861 | -98.6 | 504990 | 846 | -99.0 | 504990 | 328 |
| MR_1774413781_06CDF16F | 504990 | 886 | -89.3 | 504990 | 861 | -99.4 | 504990 | 846 | -100.0 | 504990 | 328 |
| MR_1774413781_2F16F9C2 | 504990 | 886 | -88.1 | 504990 | 861 | -96.6 | 504990 | 846 | -97.3 | 504990 | 328 |
| MR_1774413781_6C060A0B | 504990 | 886 | -86.8 | 504990 | 861 | -99.2 | 504990 | 846 | -97.0 | 504990 | 328 |
| MR_1774413781_1EB2A102 | 504990 | 886 | -86.9 | 504990 | 861 | -96.7 | 504990 | 846 | -97.2 | 504990 | 328 |
| MR_1774413781_64B8EF13 | 504990 | 886 | -88.8 | 504990 | 861 | -96.1 | 504990 | 846 | -96.0 | 504990 | 328 |
| MR_1774413781_F698D74A | 504990 | 886 | -90.5 | 504990 | 861 | -99.0 | 504990 | 846 | -99.4 | 504990 | 328 |
| MR_1774413781_2645F764 | 504990 | 886 | -87.1 | 504990 | 861 | -96.1 | 504990 | 846 | -97.8 | 504990 | 328 |

> *... 2개 열 생략 (전체 14열)*

---
