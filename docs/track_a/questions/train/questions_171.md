# Track A 문제 분석 — train[1700]~train[1709]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1700] ~ train[1709] (10개)

## 목차

1. [문제 1700: `14ef85c6-5cf...`](#1700) — single-answer, 정답: C1
2. [문제 1701: `f379ef2d-98b...`](#1701) — single-answer, 정답: C4
3. [문제 1702: `5af487d8-1f9...`](#1702) — multiple-answer, 정답: C12|C16
4. [문제 1703: `86c868d7-ec5...`](#1703) — single-answer, 정답: C8
5. [문제 1704: `3ea62385-716...`](#1704) — single-answer, 정답: C12
6. [문제 1705: `db0eb654-07c...`](#1705) — single-answer, 정답: C16
7. [문제 1706: `58a05c0f-c02...`](#1706) — single-answer, 정답: C16
8. [문제 1707: `3fadc6d0-80a...`](#1707) — single-answer, 정답: C1
9. [문제 1708: `c4b0253a-5b6...`](#1708) — single-answer, 정답: C14
10. [문제 1709: `bc3f34f2-279...`](#1709) — single-answer, 정답: C3

---

### 문제 1700: `14ef85c6-5cf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `14ef85c6-5cfb-4362-a773-4abfe0579aec` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243945_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1700] topology](images/train_1700.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243945_1 **← 정답**
- `C2`: Lift the tilt angle  of 3250536_2 by 5 degrees
- `C3`: Decrease A3 Offset threshold for 3243945_1
- `C4`: Adjust the azimuth of 3243945_1 by 49 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250536_2
- `C6`: Adjust the azimuth of 3250536_2 by 2 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250536_2
- `C8`: Press down the tilt angle  of 3250536_2 by 5 degrees
- `C9`: Decrease A3 Offset threshold for 3250536_2
- `C10`: Check test server and transmission issues
- `C11`: Increase transmission power for 3243945_1
- `C12`: Increase A3 Offset threshold for 3250536_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243945_1
- `C14`: Press down the tilt angle of 3243945_1 by 4 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Lift the tilt angle of 3243945_1 by 4 degrees
- `C17`: Increase transmission power for 3250536_2
- `C18`: Increase A3 Offset threshold for 3243945_1
- `C19`: Decrease transmission power for 3250536_2
- `C20`: Add neighbor relationship between 3230703_9 and 3250536_2
- `C21`: Add neighbor relationship between 3243945_1 and 3250536_2
- `C22`: Decrease transmission power for 3243945_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.944 | MS1 | 121.4656712568 | 31.1446244075 | 196 | 504990 | -94.92 | 14.12 | 501.22 | 0.15 | 2.91 | 1560 |
| 2024-09-20 22:21:32.278 | MS1 | 121.4656731195 | 31.1446233011 | 22 | 504990 | -93.64 | 10.27 | 500.11 | 0.11 | 2.52 | 1580 |
| 2024-09-20 22:21:33.548 | MS1 | 121.4656598557 | 31.1446221862 | 248 | 504990 | -93.09 | 10.99 | 418.12 | 0.07 | 2.20 | 1569 |
| 2024-09-20 22:21:34.537 | MS1 | 121.4656646375 | 31.1446267590 | 652 | 152650 | -95.12 | 4.78 | 101.60 | 0.05 | 1.65 | 947 |
| 2024-09-20 22:21:35.275 | MS1 | 121.4656620287 | 31.1446219456 | 954 | 152650 | -91.22 | 3.11 | 48.55 | 0.13 | 1.88 | 991 |
| 2024-09-20 22:21:36.313 | MS1 | 121.4656750713 | 31.1446333937 | 491 | 152650 | -94.16 | 3.99 | 73.95 | 0.17 | 1.73 | 942 |
| 2024-09-20 22:21:37.402 | MS1 | 121.4656597685 | 31.1446211061 | 921 | 152650 | -92.58 | 2.68 | 91.32 | 0.17 | 1.79 | 1000 |
| 2024-09-20 22:21:38.783 | MS1 | 121.4656716289 | 31.1446366083 | 652 | 152650 | -91.48 | 5.17 | 94.03 | 0.16 | 1.97 | 921 |
| 2024-09-20 22:21:39.131 | MS1 | 121.4656741970 | 31.1446277055 | 954 | 152650 | -88.95 | 3.94 | 94.46 | 0.03 | 1.59 | 910 |
| 2024-09-20 22:21:40.965 | MS1 | 121.4656672208 | 31.1446286134 | 491 | 152650 | -90.76 | 3.80 | 69.53 | 0.13 | 2.58 | 1590 |
| 2024-09-20 22:21:41.533 | MS1 | 121.4656738714 | 31.1446336065 | 921 | 152650 | -87.43 | 7.32 | 61.93 | 0.01 | 2.25 | 1563 |
| 2024-09-20 22:21:42.526 | MS1 | 121.4656716936 | 31.1446285900 | 652 | 152650 | -89.48 | 3.36 | 70.69 | 0.08 | 2.75 | 1569 |

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
| 3210075 | 6 | 121.4650202112 | 31.1540784988 | 51 | 9 | 8 | 27.8 | TDD | 509 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3220658 | 4 | 121.4700940480 | 31.1549397672 | 54 | 9 | 6 | 8.1 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3220938 | 8 | 121.4743016892 | 31.1470206334 | 242 | 7 | 8 | 7.4 | FDD | 105 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3230570 | 5 | 121.4655004638 | 31.1512789951 | 19 | 1 | 2 | 9.8 | TDD | 220 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3230703 | 9 | 121.4650970205 | 31.1470595495 | 284 | 15 | 1 | 17.0 | FDD | 491 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3232691 | 12 | 121.4653700958 | 31.1530396025 | 308 | 9 | 1 | 21.1 | FDD | 921 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3243945 | 1 | 121.4691867447 | 31.1483179029 | 268 | 3 | 6 | 11.0 | TDD | 196 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3246163 | 7 | 121.4754984035 | 31.1475894865 | 56 | 10 | 5 | 25.0 | FDD | 838 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3247121 | 3 | 121.4658772517 | 31.1558333862 | 2 | 8 | 1 | 9.3 | TDD | 22 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3249812 | 13 | 121.4649293486 | 31.1470989510 | 181 | 11 | 2 | 13.3 | FDD | 954 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3250536 | 2 | 121.4725658823 | 31.1446588701 | 272 | 5 | 11 | 4.3 | TDD | 818 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3252151 | 11 | 121.4699554613 | 31.1456480660 | 279 | 6 | 0 | 10.4 | FDD | 308 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3253341 | 10 | 121.4642005047 | 31.1498404850 | 37 | 11 | 3 | 26.4 | FDD | 652 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |

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
| 2024-09-20 22:21:30.994 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.019 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.144 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.144 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.816 | NREventA2 | measId:1;ServCellPCI:284;Se... |
| 2024-09-20 22:21:34.920 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.142 | NREventA5 | measId:3;ServCellPCI:284;Se... |
| 2024-09-20 22:21:35.216 | NRHandoverAttempt | SourcePCI:284;SourceNR-ARFC... |
| 2024-09-20 22:21:35.244 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.254 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.380 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.380 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243945 | 1 | 9.0646 | 14.4290 | -115.2585 | 17.9709 | 184.2290 | 0.0151 | 0.0057 |
| 2024_09_20 22:00 | 3250536 | 2 | 10.5318 | 8.2508 | -114.3436 | 10.8340 | 106.6720 | 0.0117 | 0.0139 |
| 2024_09_20 22:00 | 3247121 | 3 | 19.2159 | 18.7516 | -115.8577 | 8.2808 | 183.7959 | 0.0121 | 0.0084 |
| 2024_09_20 22:00 | 3220658 | 4 | 13.6811 | 17.6366 | -116.4898 | 16.2710 | 146.5593 | 0.0092 | 0.0125 |
| 2024_09_20 22:00 | 3230570 | 5 | 12.2945 | 13.3960 | -117.7889 | 7.5746 | 192.1689 | 0.0021 | 0.0155 |
| 2024_09_20 22:00 | 3210075 | 6 | 13.6528 | 17.1867 | -117.4085 | 10.3532 | 105.6340 | 0.0058 | 0.0128 |
| 2024_09_20 22:00 | 3246163 | 7 | 9.8304 | 7.3040 | -115.7532 | 3.9473 | 44.7374 | 0.0150 | 0.0153 |
| 2024_09_20 22:00 | 3220938 | 8 | 16.9389 | 17.6813 | -114.3096 | 3.3537 | 35.6863 | 0.0000 | 0.0016 |
| 2024_09_20 22:00 | 3230703 | 9 | 7.6497 | 19.9379 | -114.2100 | 4.8616 | 34.6108 | 0.0124 | 0.0161 |
| 2024_09_20 22:00 | 3253341 | 10 | 19.8128 | 10.8045 | -116.1912 | 4.6775 | 44.0686 | 0.0089 | 0.0114 |
| 2024_09_20 22:00 | 3252151 | 11 | 13.0825 | 13.0555 | -115.5200 | 3.2197 | 30.0909 | 0.0129 | 0.0108 |
| 2024_09_20 22:00 | 3232691 | 12 | 10.1890 | 12.8561 | -115.2595 | 3.3021 | 56.5900 | 0.0048 | 0.0130 |
| 2024_09_20 22:00 | 3249812 | 13 | 10.6179 | 19.4597 | -115.1725 | 4.4450 | 40.4284 | 0.0158 | 0.0181 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415760_FA32A06B | 152650 | 954 | -91.4 | 152650 | 308 | -91.9 | 152650 | 105 | -97.6 | 152650 | 838 |
| MR_1774415760_57A97DC3 | 504990 | 248 | -92.9 | 504990 | 818 | -90.3 | 504990 | 509 | -93.9 | 504990 | 220 |
| MR_1774415760_75775704 | 152650 | 954 | -93.2 | 152650 | 308 | -91.8 | 152650 | 105 | -97.0 | 152650 | 838 |
| MR_1774415760_52071B4A | 152650 | 954 | -89.9 | 152650 | 308 | -93.1 | 152650 | 105 | -96.9 | 152650 | 838 |
| MR_1774415760_4731AA1E | 504990 | 248 | -95.1 | 504990 | 818 | -87.9 | 504990 | 509 | -97.4 | 504990 | 220 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1701: `f379ef2d-98b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f379ef2d-98b9-4ed4-88cc-b7c2ea8fafc8` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Add neighbor relationship between 3268250_2 and 3248762_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1701] topology](images/train_1701.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268250_2
- `C2`: Increase transmission power for 3248762_3
- `C3`: Decrease A3 Offset threshold for 3248762_3
- `C4`: Add neighbor relationship between 3268250_2 and 3248762_3 **← 정답**
- `C5`: Add neighbor relationship between 3220868_4 and 3248762_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248762_3
- `C7`: Decrease transmission power for 3248762_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268250_2
- `C9`: Check test server and transmission issues
- `C10`: Adjust the azimuth of 3248762_3 by 13 degrees
- `C11`: Lift the tilt angle of 3268250_2 by 1 degrees
- `C12`: Adjust the azimuth of 3268250_2 by 50 degrees
- `C13`: Decrease A3 Offset threshold for 3268250_2
- `C14`: Press down the tilt angle  of 3248762_3 by 6 degrees
- `C15`: Decrease transmission power for 3268250_2
- `C16`: Increase A3 Offset threshold for 3248762_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248762_3
- `C18`: Increase A3 Offset threshold for 3268250_2
- `C19`: Increase transmission power for 3268250_2
- `C20`: Press down the tilt angle of 3268250_2 by 1 degrees
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Lift the tilt angle  of 3248762_3 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.435 | MS1 | 121.4656616516 | 31.1446251369 | 442 | 504990 | -82.25 | 13.86 | 340.15 | 0.01 | 2.91 | 1573 |
| 2024-09-20 22:21:32.662 | MS1 | 121.4656677733 | 31.1446189580 | 442 | 504990 | -80.18 | 15.32 | 528.82 | 0.05 | 2.95 | 1599 |
| 2024-09-20 22:21:33.591 | MS1 | 121.4656693385 | 31.1446248072 | 442 | 504990 | -78.97 | 17.12 | 469.28 | 0.04 | 2.31 | 1594 |
| 2024-09-20 22:21:34.156 | MS1 | 121.4656694812 | 31.1446232748 | 442 | 504990 | -86.76 | -1.14 | 42.94 | 0.15 | 1.33 | 1591 |
| 2024-09-20 22:21:35.791 | MS1 | 121.4656597831 | 31.1446311837 | 442 | 504990 | -90.74 | -2.67 | 65.02 | 0.14 | 1.19 | 1595 |
| 2024-09-20 22:21:36.999 | MS1 | 121.4656626975 | 31.1446361039 | 442 | 504990 | -93.83 | -3.94 | 68.96 | 0.02 | 1.22 | 1599 |
| 2024-09-20 22:21:37.512 | MS1 | 121.4656587743 | 31.1446313796 | 442 | 504990 | -86.65 | -3.54 | 51.34 | 0.15 | 1.11 | 1583 |
| 2024-09-20 22:21:38.155 | MS1 | 121.4656745620 | 31.1446273654 | 442 | 504990 | -81.06 | 17.06 | 356.75 | 0.05 | 1.08 | 1592 |
| 2024-09-20 22:21:39.392 | MS1 | 121.4656614510 | 31.1446348482 | 442 | 504990 | -82.25 | 14.52 | 353.28 | 0.05 | 1.41 | 1561 |
| 2024-09-20 22:21:40.827 | MS1 | 121.4656607506 | 31.1446239832 | 442 | 504990 | -79.75 | 15.69 | 524.91 | 0.17 | 2.13 | 1574 |
| 2024-09-20 22:21:41.620 | MS1 | 121.4656704996 | 31.1446334302 | 442 | 504990 | -75.35 | 12.83 | 492.61 | 0.03 | 2.83 | 1599 |
| 2024-09-20 22:21:42.619 | MS1 | 121.4656679803 | 31.1446330610 | 442 | 504990 | -83.34 | 15.91 | 523.70 | 0.15 | 2.23 | 1588 |

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
| 3220868 | 4 | 121.4682513971 | 31.1450176294 | 16 | 10 | 5 | 25.9 | TDD | 494 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3248762 | 3 | 121.4749862299 | 31.1538980069 | 234 | 4 | 8 | 36.7 | TDD | 586 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3259032 | 1 | 121.4660994694 | 31.1476203737 | 80 | 10 | 1 | 33.0 | TDD | 944 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3268250 | 2 | 121.4736358462 | 31.1494098422 | 30 | 0 | 12 | 22.7 | TDD | 442 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.209 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.232 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.376 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.376 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.039 | NREventA3 | measId:2;ServCellPCI:864;Se... |
| 2024-09-20 22:21:36.039 | NREventA3 | measId:2;ServCellPCI:864;Se... |
| 2024-09-20 22:21:37.039 | NREventA3 | measId:2;ServCellPCI:864;Se... |
| 2024-09-20 22:21:39.539 | NRRRCReestablishAttempt | PCI:864 |
| 2024-09-20 22:21:39.551 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.561 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.704 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.704 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259032 | 1 | 19.7313 | 11.1840 | -114.8163 | 15.1932 | 168.8771 | 0.0172 | 0.0049 |
| 2024_09_20 22:00 | 3268250 | 2 | 7.4916 | 8.3696 | -117.5327 | 13.7063 | 116.9011 | 0.0076 | 0.1037 |
| 2024_09_20 22:00 | 3248762 | 3 | 14.9233 | 15.1667 | -114.8162 | 17.3634 | 106.6783 | 0.0017 | 0.0036 |
| 2024_09_20 22:00 | 3220868 | 4 | 17.1015 | 5.1568 | -115.8636 | 15.5317 | 86.1264 | 0.0165 | 0.0146 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413215_4B976BBB | 504990 | 442 | -88.5 | 504990 | 586 | -80.7 | 504990 | 494 | -89.2 | 504990 | 944 |
| MR_1774413215_6CEFB63B | 504990 | 586 | -80.4 | 504990 | 442 | -86.3 | 504990 | 494 | -88.5 | 504990 | 944 |
| MR_1774413215_B7562B4E | 504990 | 586 | -84.2 | 504990 | 442 | -87.7 | 504990 | 494 | -88.0 | 504990 | 944 |
| MR_1774413215_D3F60DEF | 504990 | 442 | -86.0 | 504990 | 586 | -82.6 | 504990 | 494 | -90.2 | 504990 | 944 |
| MR_1774413215_A600D85D | 504990 | 586 | -82.0 | 504990 | 442 | -85.2 | 504990 | 494 | -89.5 | 504990 | 944 |
| MR_1774413215_1D48EC0D | 504990 | 442 | -84.9 | 504990 | 586 | -83.9 | 504990 | 494 | -87.6 | 504990 | 944 |
| MR_1774413215_F1E0B36A | 504990 | 586 | -82.1 | 504990 | 442 | -87.9 | 504990 | 494 | -86.9 | 504990 | 944 |
| MR_1774413215_56EE32B8 | 504990 | 442 | -86.0 | 504990 | 586 | -81.4 | 504990 | 494 | -90.3 | 504990 | 944 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1702: `5af487d8-1f9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5af487d8-1f90-4abb-b611-458ac2714b0b` |
| Tag | **multiple-answer** |
| 정답 | **C12|C16** |
| C12 의미 | Press down the tilt angle  of 3234397_1 by 4 degrees |
| C16 의미 | Decrease transmission power for 3234397_1 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1702] topology](images/train_1702.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3234397_1 by 4 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234397_1
- `C3`: Add neighbor relationship between 3233583_4 and 3234397_1
- `C4`: Add neighbor relationship between 3219677_3 and 3234397_1
- `C5`: Increase A3 Offset threshold for 3234397_1
- `C6`: Increase transmission power for 3233583_4
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233583_4
- `C9`: Decrease A3 Offset threshold for 3233583_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233583_4
- `C11`: Adjust the azimuth of 3233583_4 by 6 degrees
- `C12`: Press down the tilt angle  of 3234397_1 by 4 degrees **← 정답**
- `C13`: Decrease A3 Offset threshold for 3234397_1
- `C14`: Increase A3 Offset threshold for 3233583_4
- `C15`: Press down the tilt angle of 3233583_4 by 4 degrees
- `C16`: Decrease transmission power for 3234397_1 **← 정답**
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234397_1
- `C18`: Adjust the azimuth of 3234397_1 by 26 degrees
- `C19`: Lift the tilt angle of 3233583_4 by 4 degrees
- `C20`: Increase transmission power for 3234397_1
- `C21`: Decrease transmission power for 3233583_4
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.656 | MS1 | 121.4656642683 | 31.1446223212 | 247 | 504990 | -78.80 | 12.64 | 379.29 | 0.16 | 2.52 | 1566 |
| 2024-09-20 22:21:32.855 | MS1 | 121.4656597413 | 31.1446347202 | 247 | 504990 | -75.30 | 15.34 | 577.63 | 0.11 | 2.26 | 1579 |
| 2024-09-20 22:21:33.480 | MS1 | 121.4656764661 | 31.1446273661 | 247 | 504990 | -80.29 | 15.43 | 442.07 | 0.20 | 2.70 | 1590 |
| 2024-09-20 22:21:34.420 | MS1 | 121.4656682874 | 31.1446197961 | 247 | 504990 | -90.49 | 2.41 | 41.65 | 0.14 | 1.01 | 1568 |
| 2024-09-20 22:21:35.101 | MS1 | 121.4656738028 | 31.1446295803 | 247 | 504990 | -89.42 | 2.03 | 53.19 | 0.08 | 1.30 | 1569 |
| 2024-09-20 22:21:36.366 | MS1 | 121.4656750145 | 31.1446374293 | 247 | 504990 | -86.43 | 1.09 | 46.30 | 0.05 | 1.24 | 1597 |
| 2024-09-20 22:21:37.778 | MS1 | 121.4656614076 | 31.1446214075 | 247 | 504990 | -92.33 | 1.50 | 67.36 | 0.12 | 1.35 | 1584 |
| 2024-09-20 22:21:38.790 | MS1 | 121.4656701236 | 31.1446294908 | 247 | 504990 | -88.99 | 2.35 | 60.22 | 0.19 | 1.30 | 1588 |
| 2024-09-20 22:21:39.557 | MS1 | 121.4656638698 | 31.1446370711 | 247 | 504990 | -90.72 | 1.60 | 91.68 | 0.15 | 1.27 | 1577 |
| 2024-09-20 22:21:40.172 | MS1 | 121.4656645020 | 31.1446205653 | 247 | 504990 | -80.29 | 13.67 | 362.63 | 0.03 | 2.20 | 1562 |
| 2024-09-20 22:21:41.928 | MS1 | 121.4656599941 | 31.1446363188 | 247 | 504990 | -77.88 | 14.22 | 364.56 | 0.10 | 2.24 | 1589 |
| 2024-09-20 22:21:42.669 | MS1 | 121.4656582950 | 31.1446360590 | 247 | 504990 | -77.58 | 16.29 | 383.99 | 0.01 | 2.38 | 1569 |

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
| 3219677 | 3 | 121.4710837022 | 31.1461150913 | 262 | 8 | 8 | 29.5 | TDD | 717 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3233583 | 4 | 121.4712762886 | 31.1485232833 | 237 | 1 | 6 | 36.0 | TDD | 247 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3234397 | 1 | 121.4725825525 | 31.1540577564 | 186 | 2 | 3 | 35.6 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3276669 | 2 | 121.4735958656 | 31.1441813278 | 287 | 10 | 7 | 21.1 | TDD | 571 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.329 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.349 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.452 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.452 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234397 | 1 | 8.8037 | 17.9538 | -115.0963 | 5.8974 | 145.7709 | 0.0100 | 0.0035 |
| 2024_09_20 22:00 | 3276669 | 2 | 7.3280 | 17.8323 | -116.1421 | 12.3050 | 135.8587 | 0.0155 | 0.0002 |
| 2024_09_20 22:00 | 3219677 | 3 | 18.8056 | 17.5053 | -116.1675 | 11.3727 | 118.4491 | 0.0168 | 0.0097 |
| 2024_09_20 22:00 | 3233583 | 4 | 12.8906 | 14.1165 | -108.6420 | 15.1466 | 160.1315 | 0.0075 | 0.0128 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416697_CBE24EF8 | 504990 | 258 | -90.5 | 504990 | 247 | -88.9 | 504990 | 717 | -94.5 | 504990 | 571 |
| MR_1774416697_FCB2FC14 | 504990 | 258 | -92.0 | 504990 | 247 | -86.7 | 504990 | 717 | -93.3 | 504990 | 571 |
| MR_1774416697_20A26D90 | 504990 | 247 | -89.6 | 504990 | 258 | -86.0 | 504990 | 717 | -93.7 | 504990 | 571 |
| MR_1774416697_FBA47DED | 504990 | 258 | -91.5 | 504990 | 247 | -89.0 | 504990 | 717 | -91.4 | 504990 | 571 |
| MR_1774416697_6BB78795 | 504990 | 258 | -91.4 | 504990 | 247 | -85.9 | 504990 | 717 | -94.4 | 504990 | 571 |
| MR_1774416697_4F2F0BDD | 504990 | 258 | -88.7 | 504990 | 247 | -86.4 | 504990 | 717 | -92.4 | 504990 | 571 |
| MR_1774416697_FC02521E | 504990 | 247 | -91.4 | 504990 | 258 | -85.6 | 504990 | 717 | -94.6 | 504990 | 571 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1703: `86c868d7-ec5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `86c868d7-ec58-4ef8-8ecd-8f432680cd06` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3212704_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1703] topology](images/train_1703.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3212704_2 and 3240100_3
- `C2`: Adjust the azimuth of 3212704_2 by 17 degrees
- `C3`: Add neighbor relationship between 3255651_1 and 3240100_3
- `C4`: Increase transmission power for 3240100_3
- `C5`: Decrease transmission power for 3240100_3
- `C6`: Increase A3 Offset threshold for 3240100_3
- `C7`: Decrease A3 Offset threshold for 3240100_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212704_2 **← 정답**
- `C9`: Increase transmission power for 3212704_2
- `C10`: Adjust the azimuth of 3240100_3 by 50 degrees
- `C11`: Check test server and transmission issues
- `C12`: Decrease A3 Offset threshold for 3212704_2
- `C13`: Press down the tilt angle  of 3240100_3 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240100_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240100_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212704_2
- `C17`: Lift the tilt angle of 3212704_2 by 2 degrees
- `C18`: Press down the tilt angle of 3212704_2 by 2 degrees
- `C19`: Decrease transmission power for 3212704_2
- `C20`: Increase A3 Offset threshold for 3212704_2
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Lift the tilt angle  of 3240100_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.736 | MS1 | 121.4656717519 | 31.1446250968 | 285 | 504990 | -88.76 | 12.04 | 472.20 | 0.07 | 2.75 | 1560 |
| 2024-09-20 22:21:32.281 | MS1 | 121.4656586670 | 31.1446239840 | 285 | 504990 | -90.99 | 14.12 | 403.66 | 0.06 | 2.47 | 1591 |
| 2024-09-20 22:21:33.983 | MS1 | 121.4656684714 | 31.1446346200 | 285 | 504990 | -86.01 | 14.32 | 451.14 | 0.18 | 2.80 | 1584 |
| 2024-09-20 22:21:34.539 | MS1 | 121.4656768235 | 31.1446209710 | 285 | 504990 | -86.69 | 17.05 | 62.51 | 0.54 | 2.17 | 647 |
| 2024-09-20 22:21:35.467 | MS1 | 121.4656594739 | 31.1446343985 | 285 | 504990 | -91.67 | 12.90 | 57.63 | 0.66 | 2.96 | 599 |
| 2024-09-20 22:21:36.216 | MS1 | 121.4656748146 | 31.1446206034 | 285 | 504990 | -90.78 | 13.01 | 62.87 | 0.52 | 2.61 | 565 |
| 2024-09-20 22:21:37.435 | MS1 | 121.4656685978 | 31.1446333988 | 285 | 504990 | -93.87 | 9.60 | 74.54 | 0.51 | 2.09 | 662 |
| 2024-09-20 22:21:38.578 | MS1 | 121.4656753764 | 31.1446361820 | 285 | 504990 | -89.20 | 7.85 | 64.02 | 0.68 | 2.66 | 569 |
| 2024-09-20 22:21:39.881 | MS1 | 121.4656593292 | 31.1446260196 | 285 | 504990 | -91.15 | 9.03 | 95.93 | 0.54 | 2.61 | 556 |
| 2024-09-20 22:21:40.261 | MS1 | 121.4656615783 | 31.1446180247 | 285 | 504990 | -93.34 | 12.02 | 523.65 | 0.10 | 2.87 | 1574 |
| 2024-09-20 22:21:41.932 | MS1 | 121.4656758746 | 31.1446294684 | 285 | 504990 | -92.47 | 8.89 | 507.60 | 0.19 | 2.79 | 1586 |
| 2024-09-20 22:21:42.296 | MS1 | 121.4656743440 | 31.1446330144 | 285 | 504990 | -92.82 | 7.91 | 375.27 | 0.13 | 2.25 | 1575 |

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
| 3212704 | 2 | 121.4727498382 | 31.1509986042 | 241 | 0 | 6 | 38.2 | TDD | 285 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3240100 | 3 | 121.4683547820 | 31.1450331836 | 23 | 3 | 8 | 40.4 | TDD | 566 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3255651 | 1 | 121.4696050885 | 31.1493775198 | 337 | 9 | 5 | 27.5 | TDD | 793 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3267497 | 4 | 121.4732889472 | 31.1487667238 | 75 | 2 | 12 | 32.5 | TDD | 639 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.016 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.035 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.144 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.144 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.888 | NREventA3 | measId:2;ServCellPCI:377;Se... |
| 2024-09-20 22:21:38.128 | NRHandoverAttempt | SourcePCI:377;SourceNR-ARFC... |
| 2024-09-20 22:21:38.174 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.189 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.307 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.307 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255651 | 1 | 16.9131 | 10.6439 | -116.1207 | 8.1496 | 170.6185 | 0.0012 | 0.0002 |
| 2024_09_20 22:00 | 3212704 | 2 | 10.9710 | 16.4907 | -116.2752 | 10.3743 | 83.1799 | 0.0131 | 0.0087 |
| 2024_09_20 22:00 | 3240100 | 3 | 13.7506 | 16.9987 | -116.8440 | 18.9806 | 133.3728 | 0.0151 | 0.0198 |
| 2024_09_20 22:00 | 3267497 | 4 | 16.1012 | 17.4414 | -114.0130 | 13.3260 | 162.5641 | 0.0057 | 0.0064 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415426_B1F6D309 | 504990 | 285 | -85.4 | 504990 | 566 | -93.0 | 504990 | 793 | -94.3 | 504990 | 639 |
| MR_1774415426_1C496E18 | 504990 | 285 | -85.4 | 504990 | 566 | -91.7 | 504990 | 793 | -94.1 | 504990 | 639 |
| MR_1774415426_09C1DF8B | 504990 | 285 | -84.7 | 504990 | 566 | -91.6 | 504990 | 793 | -94.0 | 504990 | 639 |
| MR_1774415426_F8B41335 | 504990 | 285 | -87.8 | 504990 | 566 | -94.2 | 504990 | 793 | -94.4 | 504990 | 639 |
| MR_1774415426_6C6C79E3 | 504990 | 285 | -88.2 | 504990 | 566 | -92.1 | 504990 | 793 | -94.9 | 504990 | 639 |
| MR_1774415426_5DA5B7B0 | 504990 | 285 | -86.0 | 504990 | 566 | -91.6 | 504990 | 793 | -92.5 | 504990 | 639 |
| MR_1774415426_D78C89EC | 504990 | 285 | -88.2 | 504990 | 566 | -91.2 | 504990 | 793 | -93.4 | 504990 | 639 |
| MR_1774415426_98412204 | 504990 | 285 | -87.9 | 504990 | 566 | -91.0 | 504990 | 793 | -93.3 | 504990 | 639 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1704: `3ea62385-716...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3ea62385-7162-43f2-b404-123420158966` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278769_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1704] topology](images/train_1704.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259690_5
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278769_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259690_5
- `C4`: Decrease transmission power for 3278769_2
- `C5`: Lift the tilt angle  of 3259690_5 by 0 degrees
- `C6`: Adjust the azimuth of 3259690_5 by 47 degrees
- `C7`: Press down the tilt angle  of 3259690_5 by 0 degrees
- `C8`: Decrease A3 Offset threshold for 3259690_5
- `C9`: Add neighbor relationship between 3231553_8 and 3259690_5
- `C10`: Press down the tilt angle of 3278769_2 by 5 degrees
- `C11`: Check test server and transmission issues
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278769_2 **← 정답**
- `C13`: Increase transmission power for 3259690_5
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Add neighbor relationship between 3278769_2 and 3259690_5
- `C16`: Decrease A3 Offset threshold for 3278769_2
- `C17`: Increase A3 Offset threshold for 3259690_5
- `C18`: Decrease transmission power for 3259690_5
- `C19`: Lift the tilt angle of 3278769_2 by 5 degrees
- `C20`: Adjust the azimuth of 3278769_2 by 1 degrees
- `C21`: Increase A3 Offset threshold for 3278769_2
- `C22`: Increase transmission power for 3278769_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.236 | MS1 | 121.4656640326 | 31.1446276462 | 546 | 504990 | -94.79 | 14.65 | 417.37 | 0.17 | 2.03 | 1579 |
| 2024-09-20 22:21:32.309 | MS1 | 121.4656628768 | 31.1446262229 | 769 | 504990 | -93.15 | 14.57 | 538.48 | 0.03 | 2.67 | 1565 |
| 2024-09-20 22:21:33.891 | MS1 | 121.4656636753 | 31.1446379194 | 310 | 504990 | -93.03 | 9.39 | 526.39 | 0.08 | 2.11 | 1561 |
| 2024-09-20 22:21:34.892 | MS1 | 121.4656739824 | 31.1446362502 | 994 | 152650 | -87.90 | 3.68 | 92.49 | 0.03 | 1.67 | 905 |
| 2024-09-20 22:21:35.569 | MS1 | 121.4656672407 | 31.1446200635 | 752 | 152650 | -88.69 | 4.53 | 103.15 | 0.08 | 1.92 | 901 |
| 2024-09-20 22:21:36.669 | MS1 | 121.4656710259 | 31.1446301329 | 455 | 152650 | -93.02 | 2.16 | 60.46 | 0.16 | 1.91 | 939 |
| 2024-09-20 22:21:37.251 | MS1 | 121.4656721475 | 31.1446192803 | 905 | 152650 | -94.10 | 4.88 | 51.63 | 0.16 | 1.55 | 911 |
| 2024-09-20 22:21:38.727 | MS1 | 121.4656764811 | 31.1446239619 | 994 | 152650 | -89.17 | 7.49 | 88.05 | 0.17 | 1.87 | 944 |
| 2024-09-20 22:21:39.142 | MS1 | 121.4656680741 | 31.1446278238 | 752 | 152650 | -88.51 | 5.06 | 59.01 | 0.14 | 1.94 | 915 |
| 2024-09-20 22:21:40.446 | MS1 | 121.4656699505 | 31.1446376148 | 455 | 152650 | -89.97 | 5.15 | 72.55 | 0.05 | 2.80 | 1597 |
| 2024-09-20 22:21:41.838 | MS1 | 121.4656689084 | 31.1446210364 | 905 | 152650 | -94.35 | 7.16 | 55.53 | 0.14 | 2.50 | 1590 |
| 2024-09-20 22:21:42.212 | MS1 | 121.4656639848 | 31.1446238724 | 994 | 152650 | -92.80 | 5.99 | 71.48 | 0.13 | 2.27 | 1573 |

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
| 3216421 | 11 | 121.4687051545 | 31.1446934509 | 312 | 5 | 3 | 26.6 | FDD | 882 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3229967 | 10 | 121.4660184172 | 31.1470076823 | 104 | 15 | 4 | 29.1 | FDD | 752 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3231553 | 8 | 121.4692654625 | 31.1479891094 | 310 | 15 | 7 | 1.1 | FDD | 455 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3233599 | 12 | 121.4743882604 | 31.1477496623 | 6 | 15 | 7 | 10.1 | FDD | 820 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3239320 | 9 | 121.4725658373 | 31.1542240260 | 187 | 15 | 2 | 23.2 | FDD | 905 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3244146 | 7 | 121.4723876561 | 31.1458719992 | 268 | 8 | 0 | 21.0 | FDD | 994 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3248395 | 6 | 121.4720518130 | 31.1516164832 | 41 | 14 | 4 | 12.6 | TDD | 310 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3252334 | 3 | 121.4677550116 | 31.1485752623 | 27 | 4 | 1 | 17.0 | TDD | 390 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3259405 | 13 | 121.4691717116 | 31.1549670230 | 270 | 9 | 2 | 21.8 | FDD | 184 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3259690 | 5 | 121.4713390799 | 31.1514420736 | 262 | 0 | 9 | 2.6 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3262335 | 4 | 121.4750826842 | 31.1511068653 | 303 | 4 | 2 | 9.6 | TDD | 846 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3270634 | 1 | 121.4742311011 | 31.1460057355 | 198 | 12 | 6 | 11.1 | TDD | 769 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3278769 | 2 | 121.4684517640 | 31.1466272001 | 229 | 3 | 1 | 15.1 | TDD | 546 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.838 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.959 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.959 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.669 | NREventA2 | measId:1;ServCellPCI:931;Se... |
| 2024-09-20 22:21:34.789 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.065 | NREventA5 | measId:3;ServCellPCI:931;Se... |
| 2024-09-20 22:21:35.124 | NRHandoverAttempt | SourcePCI:931;SourceNR-ARFC... |
| 2024-09-20 22:21:35.164 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.177 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.277 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.277 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270634 | 1 | 19.4100 | 19.7466 | -114.9050 | 10.8434 | 153.4895 | 0.0019 | 0.0004 |
| 2024_09_20 22:00 | 3278769 | 2 | 18.4787 | 6.8116 | -114.4151 | 7.9208 | 87.7982 | 0.0137 | 0.0145 |
| 2024_09_20 22:00 | 3252334 | 3 | 18.2232 | 10.6673 | -114.7709 | 15.8822 | 178.7187 | 0.0159 | 0.0108 |
| 2024_09_20 22:00 | 3262335 | 4 | 12.0321 | 6.2032 | -114.2145 | 13.7445 | 158.5657 | 0.0007 | 0.0025 |
| 2024_09_20 22:00 | 3259690 | 5 | 6.3343 | 13.0445 | -114.4732 | 11.8258 | 112.6449 | 0.0159 | 0.0039 |
| 2024_09_20 22:00 | 3248395 | 6 | 18.4465 | 8.0025 | -114.0130 | 10.3902 | 114.4603 | 0.0136 | 0.0136 |
| 2024_09_20 22:00 | 3244146 | 7 | 18.1432 | 19.2828 | -114.9860 | 3.0079 | 50.4272 | 0.0006 | 0.0095 |
| 2024_09_20 22:00 | 3231553 | 8 | 16.4633 | 12.9476 | -114.5406 | 3.0326 | 20.9458 | 0.0019 | 0.0054 |
| 2024_09_20 22:00 | 3239320 | 9 | 17.4226 | 15.0482 | -114.0028 | 3.6917 | 26.6269 | 0.0193 | 0.0123 |
| 2024_09_20 22:00 | 3229967 | 10 | 9.0071 | 18.0913 | -116.7656 | 4.4109 | 42.5332 | 0.0154 | 0.0131 |
| 2024_09_20 22:00 | 3216421 | 11 | 13.0617 | 15.1096 | -115.0196 | 3.3948 | 43.2492 | 0.0115 | 0.0177 |
| 2024_09_20 22:00 | 3233599 | 12 | 10.5949 | 13.1993 | -114.8964 | 3.9378 | 56.6712 | 0.0011 | 0.0007 |
| 2024_09_20 22:00 | 3259405 | 13 | 12.3782 | 6.6524 | -117.5163 | 4.1032 | 23.5194 | 0.0190 | 0.0003 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414762_8D0D62FF | 504990 | 310 | -94.6 | 504990 | 176 | -87.9 | 504990 | 846 | -98.0 | 504990 | 390 |
| MR_1774414762_314E9DE3 | 152650 | 994 | -86.9 | 152650 | 184 | -93.0 | 152650 | 820 | -97.5 | 152650 | 882 |
| MR_1774414762_7B465B2E | 152650 | 994 | -87.2 | 152650 | 184 | -94.8 | 152650 | 820 | -96.4 | 152650 | 882 |
| MR_1774414762_E7314F32 | 152650 | 994 | -86.4 | 152650 | 184 | -93.9 | 152650 | 820 | -98.6 | 152650 | 882 |
| MR_1774414762_AFE44C1F | 504990 | 310 | -93.4 | 504990 | 176 | -87.5 | 504990 | 846 | -96.7 | 504990 | 390 |
| MR_1774414762_D766EC51 | 152650 | 994 | -89.7 | 152650 | 184 | -95.5 | 152650 | 820 | -98.2 | 152650 | 882 |
| MR_1774414762_D2AD815C | 504990 | 310 | -94.1 | 504990 | 176 | -87.1 | 504990 | 846 | -97.8 | 504990 | 390 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1705: `db0eb654-07c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `db0eb654-07ce-4b29-af11-846b769ff196` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3274985_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1705] topology](images/train_1705.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211041_1
- `C2`: Check test server and transmission issues
- `C3`: Lift the tilt angle of 3274985_3 by 4 degrees
- `C4`: Adjust the azimuth of 3211041_1 by 50 degrees
- `C5`: Adjust the azimuth of 3274985_3 by 11 degrees
- `C6`: Increase transmission power for 3211041_1
- `C7`: Increase A3 Offset threshold for 3211041_1
- `C8`: Decrease transmission power for 3211041_1
- `C9`: Add neighbor relationship between 3242262_2 and 3211041_1
- `C10`: Increase A3 Offset threshold for 3274985_3
- `C11`: Decrease A3 Offset threshold for 3274985_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211041_1
- `C13`: Increase transmission power for 3274985_3
- `C14`: Add neighbor relationship between 3274985_3 and 3211041_1
- `C15`: Decrease transmission power for 3274985_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274985_3 **← 정답**
- `C17`: Press down the tilt angle  of 3211041_1 by 10 degrees
- `C18`: Decrease A3 Offset threshold for 3211041_1
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274985_3
- `C21`: Lift the tilt angle  of 3211041_1 by 10 degrees
- `C22`: Press down the tilt angle of 3274985_3 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.357 | MS1 | 121.4656609389 | 31.1446356591 | 316 | 504990 | -91.71 | 14.30 | 377.36 | 0.10 | 2.03 | 1574 |
| 2024-09-20 22:21:32.401 | MS1 | 121.4656740484 | 31.1446263260 | 316 | 504990 | -90.56 | 13.22 | 467.34 | 0.17 | 2.70 | 1581 |
| 2024-09-20 22:21:33.553 | MS1 | 121.4656765513 | 31.1446211951 | 316 | 504990 | -86.15 | 17.07 | 507.43 | 0.07 | 2.19 | 1564 |
| 2024-09-20 22:21:34.175 | MS1 | 121.4656633082 | 31.1446273630 | 316 | 504990 | -90.74 | 12.99 | 46.18 | 0.66 | 2.51 | 582 |
| 2024-09-20 22:21:35.774 | MS1 | 121.4656591028 | 31.1446244605 | 316 | 504990 | -89.33 | 13.96 | 55.52 | 0.54 | 2.72 | 627 |
| 2024-09-20 22:21:36.812 | MS1 | 121.4656742289 | 31.1446184351 | 316 | 504990 | -90.47 | 16.85 | 50.14 | 0.59 | 2.20 | 645 |
| 2024-09-20 22:21:37.229 | MS1 | 121.4656775938 | 31.1446346138 | 316 | 504990 | -90.28 | 10.02 | 91.86 | 0.66 | 2.97 | 603 |
| 2024-09-20 22:21:38.121 | MS1 | 121.4656600096 | 31.1446300433 | 316 | 504990 | -92.19 | 11.64 | 54.07 | 0.67 | 2.62 | 582 |
| 2024-09-20 22:21:39.550 | MS1 | 121.4656623628 | 31.1446206743 | 316 | 504990 | -93.59 | 10.59 | 101.48 | 0.55 | 2.67 | 528 |
| 2024-09-20 22:21:40.511 | MS1 | 121.4656628812 | 31.1446311339 | 316 | 504990 | -89.53 | 11.84 | 424.79 | 0.15 | 2.81 | 1599 |
| 2024-09-20 22:21:41.971 | MS1 | 121.4656745905 | 31.1446321937 | 316 | 504990 | -89.46 | 9.98 | 393.68 | 0.03 | 2.53 | 1563 |
| 2024-09-20 22:21:42.853 | MS1 | 121.4656688927 | 31.1446233668 | 316 | 504990 | -93.18 | 11.09 | 509.65 | 0.08 | 2.18 | 1568 |

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
| 3211041 | 1 | 121.4680886309 | 31.1459129063 | 288 | 3 | 9 | 40.5 | TDD | 594 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3234654 | 4 | 121.4640578716 | 31.1526941194 | 312 | 10 | 12 | 28.5 | TDD | 459 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3242262 | 2 | 121.4718472891 | 31.1452968893 | 321 | 12 | 1 | 19.0 | TDD | 427 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3274985 | 3 | 121.4701632645 | 31.1545596696 | 190 | 3 | 0 | 23.3 | TDD | 316 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.237 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.258 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.400 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.400 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.128 | NREventA3 | measId:2;ServCellPCI:175;Se... |
| 2024-09-20 22:21:38.368 | NRHandoverAttempt | SourcePCI:175;SourceNR-ARFC... |
| 2024-09-20 22:21:38.399 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.412 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.522 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.522 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211041 | 1 | 17.6626 | 6.6269 | -114.6812 | 16.6706 | 98.8472 | 0.0167 | 0.0096 |
| 2024_09_20 22:00 | 3242262 | 2 | 16.3514 | 11.9974 | -117.2104 | 18.3863 | 159.3913 | 0.0142 | 0.0184 |
| 2024_09_20 22:00 | 3274985 | 3 | 5.3321 | 10.1415 | -116.6283 | 19.8930 | 166.4583 | 0.0058 | 0.0057 |
| 2024_09_20 22:00 | 3234654 | 4 | 17.3967 | 16.8297 | -117.0164 | 5.8184 | 158.0566 | 0.0061 | 0.0032 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414510_9F1A061C | 504990 | 316 | -91.3 | 504990 | 594 | -94.6 | 504990 | 427 | -99.0 | 504990 | 459 |
| MR_1774414510_E1A45451 | 504990 | 316 | -89.9 | 504990 | 594 | -92.7 | 504990 | 427 | -101.1 | 504990 | 459 |
| MR_1774414510_D05265E6 | 504990 | 316 | -92.2 | 504990 | 594 | -95.6 | 504990 | 427 | -101.9 | 504990 | 459 |
| MR_1774414510_2F539070 | 504990 | 316 | -91.2 | 504990 | 594 | -94.6 | 504990 | 427 | -101.5 | 504990 | 459 |
| MR_1774414510_55A3ADA1 | 504990 | 316 | -90.4 | 504990 | 594 | -96.0 | 504990 | 427 | -99.7 | 504990 | 459 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1706: `58a05c0f-c02...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `58a05c0f-c02c-441e-94f1-dee172bfde21` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3214109_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1706] topology](images/train_1706.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3214109_3
- `C2`: Lift the tilt angle of 3214109_3 by 5 degrees
- `C3`: Add neighbor relationship between 3214109_3 and 3254997_4
- `C4`: Increase A3 Offset threshold for 3214109_3
- `C5`: Decrease A3 Offset threshold for 3254997_4
- `C6`: Add neighbor relationship between 3234777_1 and 3254997_4
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214109_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254997_4
- `C10`: Increase A3 Offset threshold for 3254997_4
- `C11`: Press down the tilt angle of 3214109_3 by 5 degrees
- `C12`: Adjust the azimuth of 3214109_3 by 33 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254997_4
- `C14`: Increase transmission power for 3254997_4
- `C15`: Adjust the azimuth of 3254997_4 by 50 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214109_3 **← 정답**
- `C17`: Check test server and transmission issues
- `C18`: Decrease transmission power for 3254997_4
- `C19`: Press down the tilt angle  of 3254997_4 by 10 degrees
- `C20`: Increase transmission power for 3214109_3
- `C21`: Decrease A3 Offset threshold for 3214109_3
- `C22`: Lift the tilt angle  of 3254997_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.520 | MS1 | 121.4656590535 | 31.1446219082 | 139 | 504990 | -85.82 | 14.31 | 549.16 | 0.13 | 2.19 | 1593 |
| 2024-09-20 22:21:32.147 | MS1 | 121.4656592650 | 31.1446191681 | 139 | 504990 | -85.47 | 16.01 | 545.14 | 0.05 | 2.98 | 1593 |
| 2024-09-20 22:21:33.614 | MS1 | 121.4656714335 | 31.1446290198 | 139 | 504990 | -88.12 | 12.65 | 363.35 | 0.07 | 2.27 | 1588 |
| 2024-09-20 22:21:34.293 | MS1 | 121.4656720243 | 31.1446330565 | 139 | 504990 | -87.84 | 16.38 | 106.63 | 0.65 | 2.03 | 539 |
| 2024-09-20 22:21:35.122 | MS1 | 121.4656651645 | 31.1446267562 | 139 | 504990 | -86.52 | 16.08 | 58.47 | 0.58 | 2.88 | 627 |
| 2024-09-20 22:21:36.385 | MS1 | 121.4656646904 | 31.1446201664 | 139 | 504990 | -86.19 | 12.82 | 72.32 | 0.59 | 2.16 | 578 |
| 2024-09-20 22:21:37.553 | MS1 | 121.4656698494 | 31.1446312874 | 139 | 504990 | -91.27 | 12.33 | 95.62 | 0.68 | 2.69 | 612 |
| 2024-09-20 22:21:38.139 | MS1 | 121.4656656383 | 31.1446285707 | 139 | 504990 | -90.91 | 7.94 | 88.41 | 0.54 | 2.53 | 547 |
| 2024-09-20 22:21:39.923 | MS1 | 121.4656633933 | 31.1446378048 | 139 | 504990 | -92.74 | 9.24 | 92.47 | 0.58 | 2.49 | 535 |
| 2024-09-20 22:21:40.843 | MS1 | 121.4656777027 | 31.1446323617 | 139 | 504990 | -89.40 | 12.87 | 450.86 | 0.06 | 2.78 | 1592 |
| 2024-09-20 22:21:41.777 | MS1 | 121.4656639499 | 31.1446251690 | 139 | 504990 | -93.89 | 10.20 | 528.01 | 0.06 | 2.75 | 1573 |
| 2024-09-20 22:21:42.251 | MS1 | 121.4656669351 | 31.1446276460 | 139 | 504990 | -92.37 | 12.07 | 383.55 | 0.10 | 2.37 | 1568 |

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
| 3214109 | 3 | 121.4698506092 | 31.1495256150 | 249 | 1 | 6 | 49.8 | TDD | 139 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3234777 | 1 | 121.4703180282 | 31.1538383251 | 91 | 14 | 10 | 33.2 | TDD | 360 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3254997 | 4 | 121.4735365723 | 31.1502252868 | 35 | 8 | 1 | 31.1 | TDD | 799 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3272682 | 2 | 121.4703271072 | 31.1479942220 | 117 | 8 | 11 | 24.2 | TDD | 554 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.960 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.978 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.119 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.119 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.850 | NREventA3 | measId:2;ServCellPCI:977;Se... |
| 2024-09-20 22:21:38.090 | NRHandoverAttempt | SourcePCI:977;SourceNR-ARFC... |
| 2024-09-20 22:21:38.123 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.136 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.272 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.272 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234777 | 1 | 12.2366 | 12.9641 | -114.9237 | 5.6686 | 186.4332 | 0.0170 | 0.0199 |
| 2024_09_20 22:00 | 3272682 | 2 | 15.7276 | 9.5093 | -115.3367 | 11.7417 | 123.1185 | 0.0063 | 0.0196 |
| 2024_09_20 22:00 | 3214109 | 3 | 8.1412 | 19.6829 | -116.4069 | 6.4740 | 123.8540 | 0.0198 | 0.0180 |
| 2024_09_20 22:00 | 3254997 | 4 | 5.2146 | 5.4129 | -116.9272 | 14.0979 | 120.4726 | 0.0051 | 0.0033 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412073_FBDBBAF1 | 504990 | 139 | -86.3 | 504990 | 799 | -87.3 | 504990 | 360 | -96.4 | 504990 | 554 |
| MR_1774412073_D519BDB9 | 504990 | 139 | -87.4 | 504990 | 799 | -88.2 | 504990 | 360 | -94.5 | 504990 | 554 |
| MR_1774412073_3F510558 | 504990 | 139 | -88.4 | 504990 | 799 | -88.7 | 504990 | 360 | -97.9 | 504990 | 554 |
| MR_1774412073_DEC32F08 | 504990 | 139 | -88.5 | 504990 | 799 | -89.9 | 504990 | 360 | -94.7 | 504990 | 554 |
| MR_1774412073_559B1929 | 504990 | 139 | -85.1 | 504990 | 799 | -86.3 | 504990 | 360 | -98.2 | 504990 | 554 |
| MR_1774412073_56FFF17E | 504990 | 139 | -86.8 | 504990 | 799 | -88.6 | 504990 | 360 | -96.8 | 504990 | 554 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1707: `3fadc6d0-80a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3fadc6d0-80a7-4b06-848b-0715d9826d6c` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Decrease A3 Offset threshold for 3266387_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1707] topology](images/train_1707.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3266387_4 **← 정답**
- `C2`: Add neighbor relationship between 3266387_4 and 3260287_2
- `C3`: Increase transmission power for 3260287_2
- `C4`: Decrease transmission power for 3260287_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260287_2
- `C6`: Increase A3 Offset threshold for 3260287_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266387_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266387_4
- `C10`: Add neighbor relationship between 3237138_1 and 3260287_2
- `C11`: Increase transmission power for 3266387_4
- `C12`: Decrease A3 Offset threshold for 3260287_2
- `C13`: Press down the tilt angle  of 3260287_2 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260287_2
- `C15`: Press down the tilt angle of 3266387_4 by 10 degrees
- `C16`: Lift the tilt angle  of 3260287_2 by 10 degrees
- `C17`: Increase A3 Offset threshold for 3266387_4
- `C18`: Lift the tilt angle of 3266387_4 by 10 degrees
- `C19`: Adjust the azimuth of 3266387_4 by 21 degrees
- `C20`: Decrease transmission power for 3266387_4
- `C21`: Adjust the azimuth of 3260287_2 by 50 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.530 | MS1 | 121.4656581661 | 31.1446374076 | 931 | 504990 | -81.87 | 17.40 | 555.60 | 0.16 | 2.42 | 1581 |
| 2024-09-20 22:21:32.467 | MS1 | 121.4656674304 | 31.1446268685 | 931 | 504990 | -83.44 | 15.08 | 369.64 | 0.03 | 2.16 | 1576 |
| 2024-09-20 22:21:33.905 | MS1 | 121.4656633718 | 31.1446256761 | 931 | 504990 | -83.57 | 17.18 | 528.45 | 0.19 | 2.61 | 1579 |
| 2024-09-20 22:21:34.992 | MS1 | 121.4656614107 | 31.1446310915 | 931 | 504990 | -84.62 | -3.36 | 41.29 | 0.19 | 1.12 | 1564 |
| 2024-09-20 22:21:35.165 | MS1 | 121.4656647839 | 31.1446330730 | 931 | 504990 | -83.80 | -3.18 | 56.75 | 0.15 | 1.37 | 1572 |
| 2024-09-20 22:21:36.572 | MS1 | 121.4656722216 | 31.1446296854 | 931 | 504990 | -88.63 | -1.94 | 78.75 | 0.03 | 1.41 | 1599 |
| 2024-09-20 22:21:37.920 | MS1 | 121.4656678063 | 31.1446338646 | 931 | 504990 | -89.02 | -0.27 | 59.33 | 0.15 | 1.13 | 1579 |
| 2024-09-20 22:21:38.957 | MS1 | 121.4656755937 | 31.1446350515 | 931 | 504990 | -86.16 | -3.24 | 70.51 | 0.18 | 1.13 | 1587 |
| 2024-09-20 22:21:39.284 | MS1 | 121.4656596786 | 31.1446285418 | 674 | 504990 | -79.90 | 16.08 | 263.98 | 0.02 | 1.27 | 1589 |
| 2024-09-20 22:21:40.867 | MS1 | 121.4656697531 | 31.1446327344 | 674 | 504990 | -78.40 | 17.59 | 463.00 | 0.14 | 2.51 | 1571 |
| 2024-09-20 22:21:41.465 | MS1 | 121.4656777416 | 31.1446359231 | 674 | 504990 | -76.60 | 15.30 | 447.81 | 0.05 | 2.22 | 1600 |
| 2024-09-20 22:21:42.197 | MS1 | 121.4656587839 | 31.1446263035 | 674 | 504990 | -79.98 | 16.04 | 362.01 | 0.12 | 2.61 | 1599 |

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
| 3237138 | 1 | 121.4733250924 | 31.1518868822 | 263 | 9 | 7 | 49.8 | TDD | 504 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3246193 | 3 | 121.4670605076 | 31.1542421838 | 258 | 12 | 2 | 41.8 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3260287 | 2 | 121.4651957294 | 31.1477317302 | 264 | 6 | 0 | 40.3 | TDD | 674 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3266387 | 4 | 121.4704852862 | 31.1507490514 | 235 | 14 | 5 | 22.9 | TDD | 931 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.656 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.680 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.814 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.814 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.492 | NREventA3 | measId:2;ServCellPCI:249;Se... |
| 2024-09-20 22:21:38.732 | NRHandoverAttempt | SourcePCI:249;SourceNR-ARFC... |
| 2024-09-20 22:21:38.776 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.791 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.929 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.929 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237138 | 1 | 9.4105 | 5.5753 | -115.5079 | 13.3531 | 130.2871 | 0.0037 | 0.0194 |
| 2024_09_20 22:00 | 3260287 | 2 | 12.9664 | 5.8680 | -117.2021 | 16.9064 | 191.7435 | 0.0063 | 0.0016 |
| 2024_09_20 22:00 | 3246193 | 3 | 6.4266 | 13.2553 | -115.7364 | 15.6396 | 186.5092 | 0.0102 | 0.0148 |
| 2024_09_20 22:00 | 3266387 | 4 | 9.1583 | 13.4131 | -117.6142 | 15.8764 | 102.4869 | 0.0020 | 0.1148 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415748_E693A3A7 | 504990 | 674 | -78.2 | 504990 | 931 | -83.4 | 504990 | 504 | -85.6 | 504990 | 258 |
| MR_1774415748_1C843BB0 | 504990 | 674 | -80.0 | 504990 | 931 | -83.9 | 504990 | 504 | -84.8 | 504990 | 258 |
| MR_1774415748_915D47C1 | 504990 | 931 | -84.7 | 504990 | 674 | -77.6 | 504990 | 504 | -84.6 | 504990 | 258 |
| MR_1774415748_38FE9EAB | 504990 | 931 | -83.9 | 504990 | 674 | -78.7 | 504990 | 504 | -84.9 | 504990 | 258 |
| MR_1774415748_2C785F86 | 504990 | 931 | -85.0 | 504990 | 674 | -77.0 | 504990 | 504 | -86.9 | 504990 | 258 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1708: `c4b0253a-5b6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c4b0253a-5b60-4af9-b8dc-c39f40910edc` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3261266_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1708] topology](images/train_1708.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3261266_1 by 1 degrees
- `C2`: Press down the tilt angle  of 3216340_2 by 10 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Adjust the azimuth of 3261266_1 by 50 degrees
- `C5`: Adjust the azimuth of 3216340_2 by 50 degrees
- `C6`: Lift the tilt angle of 3261266_1 by 1 degrees
- `C7`: Add neighbor relationship between 3256298_3 and 3216340_2
- `C8`: Increase transmission power for 3261266_1
- `C9`: Add neighbor relationship between 3261266_1 and 3216340_2
- `C10`: Decrease A3 Offset threshold for 3261266_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216340_2
- `C12`: Decrease transmission power for 3261266_1
- `C13`: Increase A3 Offset threshold for 3216340_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261266_1 **← 정답**
- `C15`: Lift the tilt angle  of 3216340_2 by 10 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261266_1
- `C17`: Increase transmission power for 3216340_2
- `C18`: Decrease A3 Offset threshold for 3216340_2
- `C19`: Increase A3 Offset threshold for 3261266_1
- `C20`: Decrease transmission power for 3216340_2
- `C21`: Check test server and transmission issues
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216340_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.486 | MS1 | 121.4656596485 | 31.1446277059 | 496 | 504990 | -91.79 | 14.50 | 465.22 | 0.11 | 2.94 | 1560 |
| 2024-09-20 22:21:32.154 | MS1 | 121.4656693712 | 31.1446284626 | 496 | 504990 | -90.61 | 14.36 | 532.66 | 0.20 | 2.81 | 1581 |
| 2024-09-20 22:21:33.886 | MS1 | 121.4656636660 | 31.1446378601 | 496 | 504990 | -87.53 | 17.12 | 318.77 | 0.18 | 2.00 | 1577 |
| 2024-09-20 22:21:34.405 | MS1 | 121.4656632360 | 31.1446321548 | 496 | 504990 | -89.10 | 13.71 | 65.03 | 0.53 | 2.44 | 535 |
| 2024-09-20 22:21:35.230 | MS1 | 121.4656738255 | 31.1446229290 | 496 | 504990 | -90.76 | 15.94 | 84.19 | 0.55 | 2.60 | 580 |
| 2024-09-20 22:21:36.482 | MS1 | 121.4656710671 | 31.1446271082 | 496 | 504990 | -88.60 | 15.00 | 103.30 | 0.58 | 2.07 | 689 |
| 2024-09-20 22:21:37.466 | MS1 | 121.4656734440 | 31.1446205399 | 496 | 504990 | -89.88 | 10.52 | 71.56 | 0.54 | 2.84 | 619 |
| 2024-09-20 22:21:38.402 | MS1 | 121.4656604006 | 31.1446249495 | 496 | 504990 | -89.99 | 10.41 | 88.07 | 0.69 | 2.60 | 507 |
| 2024-09-20 22:21:39.905 | MS1 | 121.4656699567 | 31.1446354746 | 496 | 504990 | -91.74 | 9.90 | 80.57 | 0.66 | 2.35 | 607 |
| 2024-09-20 22:21:40.211 | MS1 | 121.4656725270 | 31.1446292108 | 496 | 504990 | -92.64 | 10.71 | 309.93 | 0.17 | 2.10 | 1577 |
| 2024-09-20 22:21:41.282 | MS1 | 121.4656722905 | 31.1446365807 | 496 | 504990 | -89.88 | 10.15 | 309.00 | 0.02 | 2.48 | 1584 |
| 2024-09-20 22:21:42.346 | MS1 | 121.4656711391 | 31.1446249734 | 496 | 504990 | -93.13 | 8.64 | 500.54 | 0.07 | 2.31 | 1566 |

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
| 3216340 | 2 | 121.4667557168 | 31.1446407371 | 354 | 7 | 0 | 47.7 | TDD | 874 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3252488 | 4 | 121.4728928414 | 31.1464390115 | 345 | 5 | 8 | 36.1 | TDD | 975 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3256298 | 3 | 121.4656966533 | 31.1475172469 | 110 | 8 | 0 | 31.4 | TDD | 506 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3261266 | 1 | 121.4674642468 | 31.1509457171 | 144 | 0 | 4 | 17.8 | TDD | 496 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.155 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.177 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.304 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.304 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.021 | NREventA3 | measId:2;ServCellPCI:996;Se... |
| 2024-09-20 22:21:38.261 | NRHandoverAttempt | SourcePCI:996;SourceNR-ARFC... |
| 2024-09-20 22:21:38.311 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.322 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.439 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.439 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261266 | 1 | 18.6334 | 16.1213 | -116.0747 | 7.2084 | 175.7213 | 0.0080 | 0.0058 |
| 2024_09_20 22:00 | 3216340 | 2 | 5.4240 | 8.4134 | -116.5294 | 15.1339 | 185.9679 | 0.0138 | 0.0142 |
| 2024_09_20 22:00 | 3256298 | 3 | 15.3250 | 7.2777 | -114.3235 | 8.2808 | 178.9690 | 0.0047 | 0.0178 |
| 2024_09_20 22:00 | 3252488 | 4 | 10.6382 | 5.0879 | -116.4603 | 5.5485 | 94.0008 | 0.0143 | 0.0041 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417165_B465DF6D | 504990 | 496 | -87.4 | 504990 | 874 | -94.1 | 504990 | 506 | -97.6 | 504990 | 975 |
| MR_1774417165_1EB68570 | 504990 | 496 | -90.2 | 504990 | 874 | -92.2 | 504990 | 506 | -95.0 | 504990 | 975 |
| MR_1774417165_854F8577 | 504990 | 496 | -88.4 | 504990 | 874 | -93.0 | 504990 | 506 | -95.9 | 504990 | 975 |
| MR_1774417165_89EFC640 | 504990 | 496 | -88.5 | 504990 | 874 | -95.7 | 504990 | 506 | -97.7 | 504990 | 975 |
| MR_1774417165_A430C520 | 504990 | 496 | -88.0 | 504990 | 874 | -92.0 | 504990 | 506 | -98.1 | 504990 | 975 |
| MR_1774417165_B7EA753E | 504990 | 496 | -88.7 | 504990 | 874 | -95.3 | 504990 | 506 | -95.1 | 504990 | 975 |
| MR_1774417165_2E36576D | 504990 | 496 | -89.5 | 504990 | 874 | -94.1 | 504990 | 506 | -95.9 | 504990 | 975 |
| MR_1774417165_6D0D98BB | 504990 | 496 | -91.0 | 504990 | 874 | -95.1 | 504990 | 506 | -94.9 | 504990 | 975 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1709: `bc3f34f2-279...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bc3f34f2-279d-4eff-9335-a7e458277905` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266525_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1709] topology](images/train_1709.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3237401_6 by 2 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266525_3 **← 정답**
- `C4`: Decrease A3 Offset threshold for 3237401_6
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237401_6
- `C6`: Decrease A3 Offset threshold for 3266525_3
- `C7`: Increase A3 Offset threshold for 3237401_6
- `C8`: Decrease transmission power for 3266525_3
- `C9`: Increase A3 Offset threshold for 3266525_3
- `C10`: Add neighbor relationship between 3266525_3 and 3237401_6
- `C11`: Press down the tilt angle of 3266525_3 by 0 degrees
- `C12`: Adjust the azimuth of 3237401_6 by 39 degrees
- `C13`: Lift the tilt angle of 3266525_3 by 0 degrees
- `C14`: Add neighbor relationship between 3227548_11 and 3237401_6
- `C15`: Adjust the azimuth of 3266525_3 by 3 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266525_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237401_6
- `C18`: Check test server and transmission issues
- `C19`: Decrease transmission power for 3237401_6
- `C20`: Increase transmission power for 3237401_6
- `C21`: Press down the tilt angle  of 3237401_6 by 2 degrees
- `C22`: Increase transmission power for 3266525_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.228 | MS1 | 121.4656753038 | 31.1446278900 | 941 | 504990 | -93.16 | 12.43 | 560.26 | 0.10 | 2.51 | 1574 |
| 2024-09-20 22:21:32.785 | MS1 | 121.4656656354 | 31.1446259299 | 625 | 504990 | -94.04 | 11.15 | 357.22 | 0.08 | 2.74 | 1594 |
| 2024-09-20 22:21:33.278 | MS1 | 121.4656745801 | 31.1446250273 | 609 | 504990 | -93.01 | 11.39 | 599.05 | 0.01 | 2.83 | 1563 |
| 2024-09-20 22:21:34.466 | MS1 | 121.4656722965 | 31.1446251748 | 866 | 152650 | -93.45 | 5.95 | 63.83 | 0.18 | 1.93 | 990 |
| 2024-09-20 22:21:35.184 | MS1 | 121.4656751777 | 31.1446180855 | 111 | 152650 | -95.68 | 5.68 | 68.28 | 0.18 | 1.80 | 994 |
| 2024-09-20 22:21:36.131 | MS1 | 121.4656768512 | 31.1446283674 | 402 | 152650 | -88.18 | 2.11 | 60.96 | 0.03 | 1.50 | 923 |
| 2024-09-20 22:21:37.535 | MS1 | 121.4656587927 | 31.1446356923 | 120 | 152650 | -94.67 | 7.83 | 96.69 | 0.14 | 1.61 | 940 |
| 2024-09-20 22:21:38.544 | MS1 | 121.4656670854 | 31.1446280151 | 866 | 152650 | -93.57 | 2.04 | 60.13 | 0.13 | 1.54 | 903 |
| 2024-09-20 22:21:39.562 | MS1 | 121.4656637481 | 31.1446378588 | 111 | 152650 | -87.26 | 4.64 | 102.35 | 0.09 | 1.50 | 997 |
| 2024-09-20 22:21:40.715 | MS1 | 121.4656611714 | 31.1446208191 | 402 | 152650 | -95.56 | 6.85 | 63.40 | 0.05 | 2.83 | 1567 |
| 2024-09-20 22:21:41.110 | MS1 | 121.4656720569 | 31.1446306916 | 120 | 152650 | -93.22 | 3.21 | 77.46 | 0.02 | 2.28 | 1594 |
| 2024-09-20 22:21:42.127 | MS1 | 121.4656634758 | 31.1446266237 | 866 | 152650 | -94.65 | 6.57 | 50.93 | 0.20 | 2.92 | 1583 |

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
| 3212816 | 9 | 121.4686419606 | 31.1504966972 | 202 | 10 | 0 | 26.3 | FDD | 589 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3227548 | 11 | 121.4709988183 | 31.1487910877 | 119 | 14 | 4 | 15.4 | FDD | 402 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3236710 | 4 | 121.4675866178 | 31.1445849050 | 268 | 9 | 0 | 29.3 | TDD | 79 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3237401 | 6 | 121.4731071182 | 31.1496759546 | 193 | 2 | 9 | 7.2 | TDD | 536 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3239698 | 2 | 121.4660933080 | 31.1504544252 | 313 | 11 | 1 | 9.4 | TDD | 424 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3244235 | 8 | 121.4718612742 | 31.1479903299 | 237 | 11 | 1 | 19.9 | FDD | 427 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3244307 | 1 | 121.4741458142 | 31.1454589375 | 135 | 5 | 3 | 27.0 | TDD | 609 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3247434 | 7 | 121.4665175545 | 31.1544479554 | 92 | 9 | 5 | 4.5 | FDD | 866 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3248398 | 10 | 121.4684701486 | 31.1524491589 | 130 | 3 | 11 | 28.5 | FDD | 111 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3264919 | 13 | 121.4701919109 | 31.1458057093 | 76 | 7 | 8 | 27.0 | FDD | 120 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3266525 | 3 | 121.4701779362 | 31.1557195334 | 202 | 0 | 8 | 3.0 | TDD | 941 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3274087 | 5 | 121.4680525110 | 31.1542731464 | 46 | 13 | 12 | 7.0 | TDD | 625 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3279737 | 12 | 121.4699365200 | 31.1440082028 | 157 | 13 | 6 | 11.2 | FDD | 310 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |

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
| 2024-09-20 22:21:31.116 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.134 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.258 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.258 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.957 | NREventA2 | measId:1;ServCellPCI:708;Se... |
| 2024-09-20 22:21:35.096 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.378 | NREventA5 | measId:3;ServCellPCI:708;Se... |
| 2024-09-20 22:21:35.444 | NRHandoverAttempt | SourcePCI:708;SourceNR-ARFC... |
| 2024-09-20 22:21:35.470 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.481 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.581 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.581 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244307 | 1 | 16.8461 | 16.9862 | -117.9450 | 14.6791 | 164.5334 | 0.0080 | 0.0128 |
| 2024_09_20 22:00 | 3239698 | 2 | 16.7638 | 9.0358 | -116.6646 | 6.2616 | 133.2637 | 0.0018 | 0.0055 |
| 2024_09_20 22:00 | 3266525 | 3 | 19.2676 | 18.1255 | -115.5560 | 9.0913 | 187.1679 | 0.0073 | 0.0015 |
| 2024_09_20 22:00 | 3236710 | 4 | 13.2363 | 11.9139 | -115.9692 | 17.1047 | 153.5859 | 0.0152 | 0.0107 |
| 2024_09_20 22:00 | 3274087 | 5 | 6.9284 | 16.7183 | -115.6319 | 14.3573 | 150.3264 | 0.0071 | 0.0024 |
| 2024_09_20 22:00 | 3237401 | 6 | 16.6591 | 15.9669 | -117.1791 | 7.1436 | 154.3389 | 0.0095 | 0.0003 |
| 2024_09_20 22:00 | 3247434 | 7 | 15.4581 | 15.0378 | -115.0523 | 3.2126 | 25.7080 | 0.0006 | 0.0116 |
| 2024_09_20 22:00 | 3244235 | 8 | 8.3364 | 5.6650 | -117.2255 | 3.3348 | 41.7303 | 0.0026 | 0.0044 |
| 2024_09_20 22:00 | 3212816 | 9 | 12.9253 | 9.2797 | -116.1010 | 4.1775 | 46.0836 | 0.0145 | 0.0118 |
| 2024_09_20 22:00 | 3248398 | 10 | 18.9502 | 18.0937 | -117.2126 | 3.9252 | 32.3267 | 0.0052 | 0.0124 |
| 2024_09_20 22:00 | 3227548 | 11 | 19.9078 | 12.9321 | -115.8378 | 3.8418 | 41.3313 | 0.0075 | 0.0030 |
| 2024_09_20 22:00 | 3279737 | 12 | 6.1178 | 7.2505 | -115.2888 | 4.4107 | 28.9849 | 0.0039 | 0.0162 |
| 2024_09_20 22:00 | 3264919 | 13 | 17.2334 | 10.3156 | -116.3243 | 4.3918 | 44.2274 | 0.0065 | 0.0129 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415962_662F6B1B | 152650 | 866 | -93.4 | 152650 | 427 | -99.0 | 152650 | 589 | -100.8 | 152650 | 310 |
| MR_1774415962_6303054C | 152650 | 866 | -93.0 | 152650 | 427 | -98.2 | 152650 | 589 | -100.3 | 152650 | 310 |
| MR_1774415962_92BA65EF | 152650 | 866 | -93.7 | 152650 | 427 | -99.1 | 152650 | 589 | -100.9 | 152650 | 310 |
| MR_1774415962_5576AF62 | 152650 | 866 | -94.3 | 152650 | 427 | -97.4 | 152650 | 589 | -101.9 | 152650 | 310 |
| MR_1774415962_BBE00DEE | 504990 | 609 | -92.5 | 504990 | 536 | -95.6 | 504990 | 424 | -95.3 | 504990 | 79 |

> *... 2개 열 생략 (전체 14열)*

---
