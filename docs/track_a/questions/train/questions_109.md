# Track A 문제 분석 — train[1080]~train[1089]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1080] ~ train[1089] (10개)

## 목차

1. [문제 1080: `1b6f0ad3-bd1...`](#1080) — single-answer, 정답: C1
2. [문제 1081: `b6c5fc16-99c...`](#1081) — single-answer, 정답: C18
3. [문제 1082: `56bc6e08-e08...`](#1082) — single-answer, 정답: C3
4. [문제 1083: `f7182e0d-ce7...`](#1083) — single-answer, 정답: C12
5. [문제 1084: `001aa737-558...`](#1084) — single-answer, 정답: C11
6. [문제 1085: `65f42f63-659...`](#1085) — single-answer, 정답: C19
7. [문제 1086: `6b39b611-26d...`](#1086) — single-answer, 정답: C10
8. [문제 1087: `360da34b-205...`](#1087) — multiple-answer, 정답: C8|C16
9. [문제 1088: `15b6fdcd-be8...`](#1088) — single-answer, 정답: C20
10. [문제 1089: `5c368419-b17...`](#1089) — single-answer, 정답: C8

---

### 문제 1080: `1b6f0ad3-bd1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1b6f0ad3-bd1d-4bb2-bec6-7884dcd6682e` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Add neighbor relationship between 3221175_1 and 3230789_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1080] topology](images/train_1080.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3221175_1 and 3230789_4 **← 정답**
- `C2`: Decrease transmission power for 3230789_4
- `C3`: Adjust the azimuth of 3230789_4 by 26 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease A3 Offset threshold for 3221175_1
- `C6`: Press down the tilt angle of 3221175_1 by 3 degrees
- `C7`: Press down the tilt angle  of 3230789_4 by 4 degrees
- `C8`: Lift the tilt angle of 3221175_1 by 3 degrees
- `C9`: Adjust the azimuth of 3221175_1 by 50 degrees
- `C10`: Add neighbor relationship between 3251012_2 and 3230789_4
- `C11`: Lift the tilt angle  of 3230789_4 by 4 degrees
- `C12`: Decrease transmission power for 3221175_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221175_1
- `C14`: Check test server and transmission issues
- `C15`: Increase transmission power for 3221175_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230789_4
- `C17`: Increase transmission power for 3230789_4
- `C18`: Decrease A3 Offset threshold for 3230789_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230789_4
- `C20`: Increase A3 Offset threshold for 3221175_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221175_1
- `C22`: Increase A3 Offset threshold for 3230789_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.595 | MS1 | 121.4656625091 | 31.1446290295 | 882 | 504990 | -84.07 | 15.34 | 331.85 | 0.02 | 2.70 | 1582 |
| 2024-09-20 22:21:32.763 | MS1 | 121.4656647299 | 31.1446248114 | 882 | 504990 | -76.43 | 13.99 | 598.50 | 0.09 | 2.26 | 1591 |
| 2024-09-20 22:21:33.207 | MS1 | 121.4656710341 | 31.1446262355 | 882 | 504990 | -83.14 | 12.01 | 460.63 | 0.18 | 2.73 | 1600 |
| 2024-09-20 22:21:34.324 | MS1 | 121.4656696918 | 31.1446187515 | 882 | 504990 | -90.72 | -1.07 | 47.64 | 0.10 | 1.09 | 1582 |
| 2024-09-20 22:21:35.189 | MS1 | 121.4656623244 | 31.1446243325 | 882 | 504990 | -86.16 | -1.37 | 51.94 | 0.12 | 1.05 | 1568 |
| 2024-09-20 22:21:36.863 | MS1 | 121.4656672839 | 31.1446243037 | 882 | 504990 | -93.13 | -2.55 | 68.83 | 0.20 | 1.48 | 1560 |
| 2024-09-20 22:21:37.153 | MS1 | 121.4656638296 | 31.1446289426 | 882 | 504990 | -85.83 | -0.17 | 63.45 | 0.04 | 1.06 | 1582 |
| 2024-09-20 22:21:38.732 | MS1 | 121.4656768385 | 31.1446322221 | 882 | 504990 | -84.49 | 13.72 | 560.16 | 0.03 | 1.45 | 1568 |
| 2024-09-20 22:21:39.700 | MS1 | 121.4656779872 | 31.1446218364 | 882 | 504990 | -76.99 | 17.74 | 380.62 | 0.15 | 1.40 | 1567 |
| 2024-09-20 22:21:40.361 | MS1 | 121.4656683065 | 31.1446378941 | 882 | 504990 | -84.12 | 12.70 | 524.51 | 0.05 | 2.32 | 1584 |
| 2024-09-20 22:21:41.923 | MS1 | 121.4656746922 | 31.1446188486 | 882 | 504990 | -77.93 | 12.40 | 309.42 | 0.19 | 2.76 | 1575 |
| 2024-09-20 22:21:42.886 | MS1 | 121.4656694018 | 31.1446236280 | 882 | 504990 | -82.40 | 16.87 | 485.03 | 0.20 | 2.23 | 1593 |

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
| 3221175 | 1 | 121.4722201439 | 31.1516303068 | 142 | 1 | 1 | 41.2 | TDD | 882 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3230789 | 4 | 121.4724876578 | 31.1452987405 | 237 | 1 | 0 | 39.0 | TDD | 446 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3232455 | 3 | 121.4650810054 | 31.1454206968 | 245 | 11 | 4 | 48.2 | TDD | 285 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3251012 | 2 | 121.4759169317 | 31.1513985194 | 313 | 12 | 1 | 20.2 | TDD | 435 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.856 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.879 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.024 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.024 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.666 | NREventA3 | measId:2;ServCellPCI:239;Se... |
| 2024-09-20 22:21:35.666 | NREventA3 | measId:2;ServCellPCI:239;Se... |
| 2024-09-20 22:21:36.666 | NREventA3 | measId:2;ServCellPCI:239;Se... |
| 2024-09-20 22:21:39.166 | NRRRCReestablishAttempt | PCI:239 |
| 2024-09-20 22:21:39.179 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.193 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.339 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.339 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221175 | 1 | 6.4686 | 5.1152 | -114.3308 | 6.5795 | 126.5432 | 0.0088 | 0.1739 |
| 2024_09_20 22:00 | 3251012 | 2 | 14.6841 | 10.9810 | -114.1324 | 18.7861 | 147.8015 | 0.0139 | 0.0136 |
| 2024_09_20 22:00 | 3232455 | 3 | 9.9996 | 7.8262 | -114.1956 | 10.7706 | 177.4351 | 0.0018 | 0.0178 |
| 2024_09_20 22:00 | 3230789 | 4 | 16.6487 | 6.6529 | -114.1530 | 16.8999 | 198.6201 | 0.0076 | 0.0006 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414783_CDC74720 | 504990 | 882 | -90.3 | 504990 | 446 | -84.2 | 504990 | 435 | -91.4 | 504990 | 285 |
| MR_1774414783_8C71ED1F | 504990 | 882 | -88.9 | 504990 | 446 | -85.2 | 504990 | 435 | -90.9 | 504990 | 285 |
| MR_1774414783_9B607630 | 504990 | 882 | -92.6 | 504990 | 446 | -86.0 | 504990 | 435 | -92.4 | 504990 | 285 |
| MR_1774414783_BDD0918C | 504990 | 882 | -90.4 | 504990 | 446 | -84.4 | 504990 | 435 | -90.8 | 504990 | 285 |
| MR_1774414783_0D9F3465 | 504990 | 446 | -84.7 | 504990 | 882 | -91.1 | 504990 | 435 | -92.3 | 504990 | 285 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1081: `b6c5fc16-99c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b6c5fc16-99c0-44a2-b3ba-94e4dc42dccc` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1081] topology](images/train_1081.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238620_1
- `C2`: Add neighbor relationship between 3275247_3 and 3238620_1
- `C3`: Lift the tilt angle of 3212840_2 by 5 degrees
- `C4`: Adjust the azimuth of 3238620_1 by 50 degrees
- `C5`: Increase transmission power for 3238620_1
- `C6`: Adjust the azimuth of 3212840_2 by 21 degrees
- `C7`: Decrease A3 Offset threshold for 3238620_1
- `C8`: Increase transmission power for 3212840_2
- `C9`: Decrease transmission power for 3212840_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Lift the tilt angle  of 3238620_1 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212840_2
- `C13`: Decrease A3 Offset threshold for 3212840_2
- `C14`: Press down the tilt angle  of 3238620_1 by 10 degrees
- `C15`: Add neighbor relationship between 3212840_2 and 3238620_1
- `C16`: Decrease transmission power for 3238620_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238620_1
- `C18`: Check test server and transmission issues **← 정답**
- `C19`: Press down the tilt angle of 3212840_2 by 5 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212840_2
- `C21`: Increase A3 Offset threshold for 3212840_2
- `C22`: Increase A3 Offset threshold for 3238620_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.302 | MS1 | 121.4656745048 | 31.1446273978 | 667 | 504990 | -87.24 | 17.16 | 501.59 | 0.18 | 2.15 | 1572 |
| 2024-09-20 22:21:32.250 | MS1 | 121.4656749993 | 31.1446313228 | 667 | 504990 | -88.41 | 13.33 | 368.78 | 0.07 | 2.92 | 1580 |
| 2024-09-20 22:21:33.654 | MS1 | 121.4656694068 | 31.1446270879 | 667 | 504990 | -86.26 | 17.32 | 396.28 | 0.08 | 2.50 | 1572 |
| 2024-09-20 22:21:34.198 | MS1 | 121.4656612692 | 31.1446300242 | 667 | 504990 | -89.21 | 13.12 | 90.92 | 0.17 | 2.38 | 413 |
| 2024-09-20 22:21:35.611 | MS1 | 121.4656690723 | 31.1446323669 | 667 | 504990 | -91.64 | 17.09 | 65.44 | 0.03 | 2.46 | 406 |
| 2024-09-20 22:21:36.236 | MS1 | 121.4656772993 | 31.1446204962 | 667 | 504990 | -86.52 | 14.41 | 100.28 | 0.20 | 2.42 | 358 |
| 2024-09-20 22:21:37.341 | MS1 | 121.4656749008 | 31.1446280067 | 667 | 504990 | -93.74 | 8.06 | 77.71 | 0.16 | 2.30 | 449 |
| 2024-09-20 22:21:38.512 | MS1 | 121.4656598025 | 31.1446244179 | 667 | 504990 | -93.26 | 10.98 | 94.47 | 0.00 | 2.49 | 400 |
| 2024-09-20 22:21:39.627 | MS1 | 121.4656609527 | 31.1446257451 | 667 | 504990 | -89.10 | 9.97 | 65.87 | 0.15 | 2.63 | 354 |
| 2024-09-20 22:21:40.455 | MS1 | 121.4656637602 | 31.1446212104 | 667 | 504990 | -91.52 | 8.55 | 495.98 | 0.07 | 2.77 | 1562 |
| 2024-09-20 22:21:41.362 | MS1 | 121.4656611960 | 31.1446206920 | 667 | 504990 | -93.64 | 11.86 | 491.06 | 0.18 | 2.05 | 1572 |
| 2024-09-20 22:21:42.395 | MS1 | 121.4656584601 | 31.1446375064 | 667 | 504990 | -90.43 | 9.45 | 307.09 | 0.13 | 2.56 | 1585 |

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
| 3212840 | 2 | 121.4664133981 | 31.1552696568 | 204 | 3 | 6 | 45.4 | TDD | 667 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3238620 | 1 | 121.4674008221 | 31.1543816403 | 250 | 15 | 11 | 38.2 | TDD | 884 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3239200 | 4 | 121.4678847981 | 31.1490898328 | 238 | 14 | 6 | 39.2 | TDD | 235 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3275247 | 3 | 121.4713070724 | 31.1466659367 | 98 | 13 | 3 | 45.4 | TDD | 612 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.577 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.598 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.710 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.710 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.398 | NREventA3 | measId:2;ServCellPCI:37;Ser... |
| 2024-09-20 22:21:38.638 | NRHandoverAttempt | SourcePCI:37;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.674 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.684 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.798 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.798 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238620 | 1 | 5.4587 | 12.9559 | -117.9040 | 6.8801 | 92.4043 | 0.0194 | 0.0059 |
| 2024_09_20 22:00 | 3212840 | 2 | 8.0087 | 15.7739 | -116.8838 | 5.1819 | 157.0085 | 0.0129 | 0.0144 |
| 2024_09_20 22:00 | 3275247 | 3 | 7.4541 | 10.4620 | -116.4496 | 17.6520 | 170.5583 | 0.0184 | 0.0011 |
| 2024_09_20 22:00 | 3239200 | 4 | 13.7532 | 18.0198 | -116.6970 | 17.3418 | 196.1302 | 0.0043 | 0.0103 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415601_AE8DF498 | 504990 | 667 | -88.6 | 504990 | 884 | -90.8 | 504990 | 612 | -100.9 | 504990 | 235 |
| MR_1774415601_A097DD5C | 504990 | 667 | -89.6 | 504990 | 884 | -90.7 | 504990 | 612 | -98.8 | 504990 | 235 |
| MR_1774415601_5223239D | 504990 | 667 | -88.7 | 504990 | 884 | -90.5 | 504990 | 612 | -98.5 | 504990 | 235 |
| MR_1774415601_FC0317F6 | 504990 | 667 | -89.7 | 504990 | 884 | -90.3 | 504990 | 612 | -99.1 | 504990 | 235 |
| MR_1774415601_EEAA4F9D | 504990 | 667 | -88.2 | 504990 | 884 | -90.2 | 504990 | 612 | -101.1 | 504990 | 235 |
| MR_1774415601_7F87752F | 504990 | 667 | -88.7 | 504990 | 884 | -89.2 | 504990 | 612 | -101.2 | 504990 | 235 |
| MR_1774415601_0FB86571 | 504990 | 667 | -90.1 | 504990 | 884 | -91.5 | 504990 | 612 | -101.2 | 504990 | 235 |
| MR_1774415601_BA846B0A | 504990 | 667 | -87.7 | 504990 | 884 | -90.2 | 504990 | 612 | -100.4 | 504990 | 235 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1082: `56bc6e08-e08...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `56bc6e08-e087-4116-8de1-610a5ff798f5` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease A3 Offset threshold for 3274802_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1082] topology](images/train_1082.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3274802_3 by 10 degrees
- `C2`: Press down the tilt angle  of 3236615_2 by 10 degrees
- `C3`: Decrease A3 Offset threshold for 3274802_3 **← 정답**
- `C4`: Decrease transmission power for 3236615_2
- `C5`: Increase A3 Offset threshold for 3274802_3
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase transmission power for 3236615_2
- `C8`: Decrease A3 Offset threshold for 3236615_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236615_2
- `C10`: Add neighbor relationship between 3223017_1 and 3236615_2
- `C11`: Increase transmission power for 3274802_3
- `C12`: Adjust the azimuth of 3236615_2 by 50 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236615_2
- `C14`: Check test server and transmission issues
- `C15`: Lift the tilt angle of 3274802_3 by 10 degrees
- `C16`: Lift the tilt angle  of 3236615_2 by 10 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274802_3
- `C18`: Add neighbor relationship between 3274802_3 and 3236615_2
- `C19`: Increase A3 Offset threshold for 3236615_2
- `C20`: Adjust the azimuth of 3274802_3 by 50 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274802_3
- `C22`: Decrease transmission power for 3274802_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.202 | MS1 | 121.4656656222 | 31.1446321561 | 947 | 504990 | -83.63 | 14.74 | 458.49 | 0.05 | 2.26 | 1593 |
| 2024-09-20 22:21:32.123 | MS1 | 121.4656657650 | 31.1446312118 | 947 | 504990 | -76.96 | 13.41 | 504.72 | 0.03 | 2.71 | 1574 |
| 2024-09-20 22:21:33.468 | MS1 | 121.4656650881 | 31.1446285928 | 947 | 504990 | -84.44 | 14.79 | 509.43 | 0.08 | 2.70 | 1575 |
| 2024-09-20 22:21:34.778 | MS1 | 121.4656741684 | 31.1446361268 | 947 | 504990 | -87.63 | -0.27 | 74.49 | 0.07 | 1.10 | 1576 |
| 2024-09-20 22:21:35.428 | MS1 | 121.4656592729 | 31.1446261484 | 947 | 504990 | -87.33 | -1.59 | 72.58 | 0.10 | 1.41 | 1597 |
| 2024-09-20 22:21:36.554 | MS1 | 121.4656626251 | 31.1446345960 | 947 | 504990 | -92.79 | -3.09 | 71.67 | 0.04 | 1.01 | 1586 |
| 2024-09-20 22:21:37.435 | MS1 | 121.4656757565 | 31.1446297943 | 947 | 504990 | -91.38 | -0.50 | 54.78 | 0.05 | 1.10 | 1589 |
| 2024-09-20 22:21:38.205 | MS1 | 121.4656754826 | 31.1446182730 | 947 | 504990 | -84.14 | -0.21 | 30.06 | 0.17 | 1.44 | 1597 |
| 2024-09-20 22:21:39.873 | MS1 | 121.4656626942 | 31.1446273503 | 945 | 504990 | -76.84 | 12.65 | 270.20 | 0.04 | 1.49 | 1577 |
| 2024-09-20 22:21:40.605 | MS1 | 121.4656675194 | 31.1446344738 | 945 | 504990 | -82.07 | 16.70 | 390.52 | 0.14 | 2.96 | 1591 |
| 2024-09-20 22:21:41.491 | MS1 | 121.4656692417 | 31.1446246289 | 945 | 504990 | -77.40 | 17.88 | 555.77 | 0.19 | 2.88 | 1574 |
| 2024-09-20 22:21:42.124 | MS1 | 121.4656742028 | 31.1446227494 | 945 | 504990 | -77.24 | 17.65 | 586.36 | 0.11 | 2.94 | 1594 |

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
| 3220004 | 4 | 121.4705204491 | 31.1487099531 | 235 | 12 | 11 | 39.8 | TDD | 963 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3223017 | 1 | 121.4676485893 | 31.1522512104 | 345 | 0 | 3 | 27.3 | TDD | 416 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3236615 | 2 | 121.4644774193 | 31.1500931397 | 7 | 11 | 7 | 23.8 | TDD | 945 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3274802 | 3 | 121.4725405631 | 31.1510409388 | 50 | 11 | 8 | 22.3 | TDD | 947 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.947 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.969 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.071 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.071 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.768 | NREventA3 | measId:2;ServCellPCI:34;Ser... |
| 2024-09-20 22:21:38.008 | NRHandoverAttempt | SourcePCI:34;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.039 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.050 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.197 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.197 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223017 | 1 | 6.0110 | 5.4145 | -114.6506 | 8.1994 | 135.7708 | 0.0039 | 0.0069 |
| 2024_09_20 22:00 | 3236615 | 2 | 5.4706 | 19.9914 | -114.8582 | 10.9446 | 133.2210 | 0.0039 | 0.0154 |
| 2024_09_20 22:00 | 3274802 | 3 | 18.1294 | 6.0141 | -115.5746 | 15.8874 | 84.0219 | 0.0178 | 0.1312 |
| 2024_09_20 22:00 | 3220004 | 4 | 16.4833 | 16.8556 | -116.4872 | 17.6953 | 138.1011 | 0.0188 | 0.0120 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417061_BF01A598 | 504990 | 947 | -88.5 | 504990 | 945 | -84.3 | 504990 | 416 | -84.5 | 504990 | 963 |
| MR_1774417061_5C1EBF73 | 504990 | 945 | -82.7 | 504990 | 947 | -87.5 | 504990 | 416 | -82.3 | 504990 | 963 |
| MR_1774417061_EFE25CAA | 504990 | 947 | -87.9 | 504990 | 945 | -83.6 | 504990 | 416 | -81.6 | 504990 | 963 |
| MR_1774417061_528D2B28 | 504990 | 945 | -83.9 | 504990 | 947 | -89.2 | 504990 | 416 | -84.6 | 504990 | 963 |
| MR_1774417061_38DF600C | 504990 | 947 | -87.6 | 504990 | 945 | -82.0 | 504990 | 416 | -82.9 | 504990 | 963 |
| MR_1774417061_37450EA8 | 504990 | 947 | -88.4 | 504990 | 945 | -82.5 | 504990 | 416 | -82.8 | 504990 | 963 |
| MR_1774417061_46F2AAFF | 504990 | 947 | -87.9 | 504990 | 945 | -83.3 | 504990 | 416 | -84.1 | 504990 | 963 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1083: `f7182e0d-ce7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f7182e0d-ce79-4228-b9ea-15b197d57c1a` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease A3 Offset threshold for 3274043_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1083] topology](images/train_1083.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274043_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274043_1
- `C3`: Increase A3 Offset threshold for 3274043_1
- `C4`: Decrease A3 Offset threshold for 3279493_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279493_3
- `C6`: Increase transmission power for 3279493_3
- `C7`: Decrease transmission power for 3274043_1
- `C8`: Decrease transmission power for 3279493_3
- `C9`: Increase transmission power for 3274043_1
- `C10`: Adjust the azimuth of 3279493_3 by 50 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279493_3
- `C12`: Decrease A3 Offset threshold for 3274043_1 **← 정답**
- `C13`: Adjust the azimuth of 3274043_1 by 50 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Press down the tilt angle of 3274043_1 by 10 degrees
- `C16`: Increase A3 Offset threshold for 3279493_3
- `C17`: Lift the tilt angle  of 3279493_3 by 9 degrees
- `C18`: Check test server and transmission issues
- `C19`: Add neighbor relationship between 3274043_1 and 3279493_3
- `C20`: Press down the tilt angle  of 3279493_3 by 9 degrees
- `C21`: Add neighbor relationship between 3233320_2 and 3279493_3
- `C22`: Lift the tilt angle of 3274043_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.163 | MS1 | 121.4656595737 | 31.1446186656 | 873 | 504990 | -79.97 | 17.48 | 549.18 | 0.06 | 2.88 | 1562 |
| 2024-09-20 22:21:32.617 | MS1 | 121.4656702539 | 31.1446219092 | 873 | 504990 | -76.20 | 17.91 | 507.72 | 0.15 | 2.76 | 1569 |
| 2024-09-20 22:21:33.166 | MS1 | 121.4656761800 | 31.1446359150 | 873 | 504990 | -76.68 | 12.14 | 450.13 | 0.03 | 2.96 | 1591 |
| 2024-09-20 22:21:34.445 | MS1 | 121.4656729560 | 31.1446337726 | 873 | 504990 | -85.02 | -2.21 | 64.73 | 0.10 | 1.10 | 1573 |
| 2024-09-20 22:21:35.465 | MS1 | 121.4656716665 | 31.1446362891 | 873 | 504990 | -84.77 | -1.56 | 31.26 | 0.14 | 1.11 | 1574 |
| 2024-09-20 22:21:36.988 | MS1 | 121.4656735421 | 31.1446374613 | 873 | 504990 | -88.07 | -2.51 | 63.87 | 0.10 | 1.34 | 1598 |
| 2024-09-20 22:21:37.218 | MS1 | 121.4656640900 | 31.1446288985 | 873 | 504990 | -90.40 | -2.50 | 52.41 | 0.14 | 1.45 | 1592 |
| 2024-09-20 22:21:38.636 | MS1 | 121.4656747697 | 31.1446242319 | 873 | 504990 | -86.64 | -2.05 | 66.56 | 0.04 | 1.10 | 1575 |
| 2024-09-20 22:21:39.857 | MS1 | 121.4656607052 | 31.1446281541 | 572 | 504990 | -83.74 | 17.09 | 247.83 | 0.06 | 1.08 | 1593 |
| 2024-09-20 22:21:40.733 | MS1 | 121.4656639121 | 31.1446253250 | 572 | 504990 | -76.82 | 17.22 | 429.89 | 0.08 | 2.52 | 1587 |
| 2024-09-20 22:21:41.884 | MS1 | 121.4656643647 | 31.1446322382 | 572 | 504990 | -75.86 | 14.50 | 416.32 | 0.12 | 2.28 | 1587 |
| 2024-09-20 22:21:42.108 | MS1 | 121.4656727179 | 31.1446248607 | 572 | 504990 | -75.56 | 12.54 | 590.47 | 0.08 | 2.22 | 1583 |

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
| 3233320 | 2 | 121.4650131727 | 31.1461526457 | 46 | 6 | 4 | 32.1 | TDD | 390 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3242500 | 4 | 121.4709942719 | 31.1449092537 | 137 | 3 | 5 | 25.9 | TDD | 126 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3274043 | 1 | 121.4650575746 | 31.1490757095 | 309 | 8 | 7 | 48.0 | TDD | 873 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3279493 | 3 | 121.4691262296 | 31.1485372166 | 308 | 4 | 2 | 43.9 | TDD | 572 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.000 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.025 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.145 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.145 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.861 | NREventA3 | measId:2;ServCellPCI:678;Se... |
| 2024-09-20 22:21:38.101 | NRHandoverAttempt | SourcePCI:678;SourceNR-ARFC... |
| 2024-09-20 22:21:38.149 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.160 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.306 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.306 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274043 | 1 | 15.0113 | 7.7726 | -114.0572 | 12.9702 | 138.4675 | 0.0186 | 0.1719 |
| 2024_09_20 22:00 | 3233320 | 2 | 12.5948 | 16.8234 | -114.3001 | 12.9230 | 109.6540 | 0.0144 | 0.0195 |
| 2024_09_20 22:00 | 3279493 | 3 | 9.4061 | 8.3846 | -115.0331 | 14.2581 | 110.7065 | 0.0033 | 0.0057 |
| 2024_09_20 22:00 | 3242500 | 4 | 5.0527 | 9.1669 | -116.8600 | 8.5336 | 131.5934 | 0.0126 | 0.0164 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413635_D85DA607 | 504990 | 873 | -84.4 | 504990 | 572 | -79.5 | 504990 | 390 | -86.3 | 504990 | 126 |
| MR_1774413635_1E38B171 | 504990 | 572 | -79.4 | 504990 | 873 | -83.2 | 504990 | 390 | -87.6 | 504990 | 126 |
| MR_1774413635_4C5D2B8B | 504990 | 873 | -85.5 | 504990 | 572 | -81.7 | 504990 | 390 | -86.9 | 504990 | 126 |
| MR_1774413635_3A6FEBCC | 504990 | 873 | -86.8 | 504990 | 572 | -81.6 | 504990 | 390 | -86.1 | 504990 | 126 |
| MR_1774413635_DE0C6DF4 | 504990 | 873 | -85.8 | 504990 | 572 | -81.3 | 504990 | 390 | -86.0 | 504990 | 126 |
| MR_1774413635_557A736A | 504990 | 572 | -80.4 | 504990 | 873 | -83.3 | 504990 | 390 | -85.5 | 504990 | 126 |
| MR_1774413635_A6D94F7F | 504990 | 873 | -85.3 | 504990 | 572 | -79.9 | 504990 | 390 | -87.3 | 504990 | 126 |
| MR_1774413635_C94AFADC | 504990 | 873 | -84.3 | 504990 | 572 | -82.6 | 504990 | 390 | -88.0 | 504990 | 126 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1084: `001aa737-558...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `001aa737-5588-4aff-b364-750cac3b7b8f` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Add neighbor relationship between 3237593_4 and 3262661_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1084] topology](images/train_1084.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3262661_1
- `C2`: Check test server and transmission issues
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262661_1
- `C4`: Decrease transmission power for 3237593_4
- `C5`: Lift the tilt angle  of 3262661_1 by 5 degrees
- `C6`: Increase transmission power for 3237593_4
- `C7`: Add neighbor relationship between 3253137_2 and 3262661_1
- `C8`: Adjust the azimuth of 3237593_4 by 50 degrees
- `C9`: Increase A3 Offset threshold for 3262661_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237593_4
- `C11`: Add neighbor relationship between 3237593_4 and 3262661_1 **← 정답**
- `C12`: Increase A3 Offset threshold for 3237593_4
- `C13`: Increase transmission power for 3262661_1
- `C14`: Press down the tilt angle  of 3262661_1 by 5 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262661_1
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237593_4
- `C18`: Lift the tilt angle of 3237593_4 by 10 degrees
- `C19`: Adjust the azimuth of 3262661_1 by 13 degrees
- `C20`: Press down the tilt angle of 3237593_4 by 10 degrees
- `C21`: Decrease A3 Offset threshold for 3262661_1
- `C22`: Decrease A3 Offset threshold for 3237593_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.836 | MS1 | 121.4656741029 | 31.1446334678 | 397 | 504990 | -82.52 | 13.18 | 458.56 | 0.12 | 2.27 | 1591 |
| 2024-09-20 22:21:32.565 | MS1 | 121.4656723375 | 31.1446356636 | 397 | 504990 | -81.71 | 15.36 | 376.49 | 0.02 | 2.97 | 1587 |
| 2024-09-20 22:21:33.918 | MS1 | 121.4656587926 | 31.1446270205 | 397 | 504990 | -79.99 | 14.92 | 557.15 | 0.14 | 2.99 | 1586 |
| 2024-09-20 22:21:34.306 | MS1 | 121.4656681267 | 31.1446265324 | 397 | 504990 | -91.88 | -2.29 | 41.35 | 0.01 | 1.47 | 1600 |
| 2024-09-20 22:21:35.824 | MS1 | 121.4656744339 | 31.1446235234 | 397 | 504990 | -85.74 | -1.04 | 68.04 | 0.00 | 1.02 | 1599 |
| 2024-09-20 22:21:36.337 | MS1 | 121.4656653939 | 31.1446315159 | 397 | 504990 | -93.08 | -2.42 | 34.09 | 0.07 | 1.09 | 1598 |
| 2024-09-20 22:21:37.714 | MS1 | 121.4656611205 | 31.1446215851 | 397 | 504990 | -93.62 | -3.17 | 61.72 | 0.09 | 1.42 | 1565 |
| 2024-09-20 22:21:38.841 | MS1 | 121.4656603383 | 31.1446190504 | 397 | 504990 | -79.30 | 12.93 | 545.92 | 0.09 | 1.48 | 1564 |
| 2024-09-20 22:21:39.373 | MS1 | 121.4656750300 | 31.1446301088 | 397 | 504990 | -83.69 | 12.66 | 484.54 | 0.01 | 1.49 | 1594 |
| 2024-09-20 22:21:40.621 | MS1 | 121.4656682533 | 31.1446342648 | 397 | 504990 | -84.14 | 12.88 | 529.58 | 0.05 | 2.11 | 1575 |
| 2024-09-20 22:21:41.658 | MS1 | 121.4656751325 | 31.1446260717 | 397 | 504990 | -81.05 | 17.78 | 446.01 | 0.00 | 2.47 | 1594 |
| 2024-09-20 22:21:42.782 | MS1 | 121.4656668252 | 31.1446260516 | 397 | 504990 | -81.38 | 14.00 | 592.03 | 0.09 | 2.15 | 1571 |

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
| 3215993 | 3 | 121.4678088145 | 31.1472947142 | 4 | 11 | 2 | 44.0 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3237593 | 4 | 121.4745560146 | 31.1536495908 | 329 | 14 | 12 | 47.9 | TDD | 397 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3253137 | 2 | 121.4658932797 | 31.1494899019 | 305 | 13 | 1 | 44.7 | TDD | 721 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3262661 | 1 | 121.4702843563 | 31.1482055947 | 241 | 1 | 4 | 44.4 | TDD | 832 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.349 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.494 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.494 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.196 | NREventA3 | measId:2;ServCellPCI:61;Ser... |
| 2024-09-20 22:21:36.196 | NREventA3 | measId:2;ServCellPCI:61;Ser... |
| 2024-09-20 22:21:37.196 | NREventA3 | measId:2;ServCellPCI:61;Ser... |
| 2024-09-20 22:21:39.696 | NRRRCReestablishAttempt | PCI:61 |
| 2024-09-20 22:21:39.710 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.725 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.850 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.850 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262661 | 1 | 17.6363 | 9.6925 | -117.2540 | 10.1726 | 94.5823 | 0.0070 | 0.0076 |
| 2024_09_20 22:00 | 3253137 | 2 | 10.4390 | 10.0064 | -116.3510 | 15.9507 | 86.9380 | 0.0197 | 0.0082 |
| 2024_09_20 22:00 | 3215993 | 3 | 7.8823 | 17.5148 | -117.9608 | 13.6750 | 152.7506 | 0.0178 | 0.0001 |
| 2024_09_20 22:00 | 3237593 | 4 | 5.2247 | 16.7772 | -114.8443 | 8.9732 | 86.3947 | 0.0004 | 0.1361 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414656_05DFD23A | 504990 | 397 | -93.7 | 504990 | 832 | -87.8 | 504990 | 721 | -88.3 | 504990 | 309 |
| MR_1774414656_8071B73F | 504990 | 832 | -87.5 | 504990 | 397 | -90.8 | 504990 | 721 | -88.3 | 504990 | 309 |
| MR_1774414656_1BF9FD71 | 504990 | 832 | -87.9 | 504990 | 397 | -92.5 | 504990 | 721 | -89.8 | 504990 | 309 |
| MR_1774414656_62B049F9 | 504990 | 832 | -86.8 | 504990 | 397 | -92.8 | 504990 | 721 | -88.3 | 504990 | 309 |
| MR_1774414656_C49E7E30 | 504990 | 397 | -91.1 | 504990 | 832 | -87.4 | 504990 | 721 | -87.6 | 504990 | 309 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1085: `65f42f63-659...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `65f42f63-6594-4ecc-8b34-79d8ed9bf139` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Lift the tilt angle  of 3259732_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1085] topology](images/train_1085.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232533_4
- `C3`: Increase transmission power for 3232533_4
- `C4`: Add neighbor relationship between 3259732_2 and 3232533_4
- `C5`: Adjust the azimuth of 3259732_2 by 50 degrees
- `C6`: Increase A3 Offset threshold for 3270190_1
- `C7`: Decrease transmission power for 3270190_1
- `C8`: Decrease transmission power for 3232533_4
- `C9`: Check test server and transmission issues
- `C10`: Press down the tilt angle  of 3259732_2 by 10 degrees
- `C11`: Increase transmission power for 3270190_1
- `C12`: Decrease A3 Offset threshold for 3270190_1
- `C13`: Increase A3 Offset threshold for 3232533_4
- `C14`: Adjust the azimuth of 3270190_1 by 16 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270190_1
- `C16`: Press down the tilt angle of 3270190_1 by 3 degrees
- `C17`: Add neighbor relationship between 3270190_1 and 3232533_4
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232533_4
- `C19`: Lift the tilt angle  of 3259732_2 by 10 degrees **← 정답**
- `C20`: Lift the tilt angle of 3270190_1 by 3 degrees
- `C21`: Decrease A3 Offset threshold for 3232533_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270190_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.382 | MS1 | 121.4656667814 | 31.1446237247 | 666 | 504990 | -88.11 | 14.06 | 535.83 | 0.15 | 2.54 | 1600 |
| 2024-09-20 22:21:32.284 | MS1 | 121.4656612684 | 31.1446310522 | 666 | 504990 | -85.94 | 14.54 | 430.11 | 0.09 | 2.27 | 1580 |
| 2024-09-20 22:21:33.820 | MS1 | 121.4656758632 | 31.1446211062 | 666 | 504990 | -90.63 | 14.78 | 470.75 | 0.07 | 2.68 | 1562 |
| 2024-09-20 22:21:34.285 | MS1 | 121.4656669999 | 31.1446301059 | 666 | 504990 | -85.64 | 14.67 | 60.02 | 0.01 | 2.91 | 1567 |
| 2024-09-20 22:21:35.477 | MS1 | 121.4656698711 | 31.1446263482 | 666 | 504990 | -89.94 | 12.48 | 88.43 | 0.13 | 2.32 | 1581 |
| 2024-09-20 22:21:36.477 | MS1 | 121.4656627337 | 31.1446354856 | 666 | 504990 | -90.99 | 13.13 | 95.17 | 0.12 | 2.55 | 1561 |
| 2024-09-20 22:21:37.128 | MS1 | 121.4656653764 | 31.1446234855 | 666 | 504990 | -91.46 | 11.58 | 64.03 | 0.09 | 2.78 | 1591 |
| 2024-09-20 22:21:38.661 | MS1 | 121.4656734169 | 31.1446347964 | 666 | 504990 | -89.56 | 12.95 | 92.60 | 0.14 | 2.35 | 1570 |
| 2024-09-20 22:21:39.304 | MS1 | 121.4656766506 | 31.1446227206 | 666 | 504990 | -91.41 | 8.36 | 61.56 | 0.12 | 2.30 | 1589 |
| 2024-09-20 22:21:40.651 | MS1 | 121.4656763115 | 31.1446256396 | 666 | 504990 | -92.94 | 12.08 | 378.02 | 0.13 | 2.33 | 1591 |
| 2024-09-20 22:21:41.788 | MS1 | 121.4656692289 | 31.1446313568 | 666 | 504990 | -91.64 | 11.74 | 581.92 | 0.06 | 2.91 | 1599 |
| 2024-09-20 22:21:42.444 | MS1 | 121.4656774486 | 31.1446295522 | 666 | 504990 | -89.29 | 8.53 | 312.96 | 0.01 | 2.71 | 1586 |

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
| 3232533 | 4 | 121.4657146182 | 31.1446094050 | 238 | 13 | 1 | 24.1 | TDD | 109 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3237776 | 3 | 121.4724175220 | 31.1540506132 | 132 | 14 | 3 | 49.4 | TDD | 50 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3259732 | 2 | 121.4753826421 | 31.1517061504 | 340 | 8 | 12 | 34.6 | TDD | 611 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3270190 | 1 | 121.4662431000 | 31.1526924457 | 167 | 0 | 3 | 48.6 | TDD | 666 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.498 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.516 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.647 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.647 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.308 | NREventA3 | measId:2;ServCellPCI:367;Se... |
| 2024-09-20 22:21:38.548 | NRHandoverAttempt | SourcePCI:367;SourceNR-ARFC... |
| 2024-09-20 22:21:38.581 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.595 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.735 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.735 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270190 | 1 | 88.2603 | 79.3081 | -114.2314 | 13.7583 | 114.5245 | 0.0059 | 0.0065 |
| 2024_09_20 22:00 | 3259732 | 2 | 7.9330 | 5.0308 | -116.0434 | 6.6171 | 145.5357 | 0.0009 | 0.0077 |
| 2024_09_20 22:00 | 3237776 | 3 | 8.1034 | 9.5714 | -117.7730 | 10.6591 | 197.5435 | 0.0189 | 0.0131 |
| 2024_09_20 22:00 | 3232533 | 4 | 14.6934 | 6.9217 | -114.4615 | 11.6398 | 141.5958 | 0.0185 | 0.0108 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413348_C1CADCD8 | 504990 | 666 | -86.4 | 504990 | 109 | -90.6 | 504990 | 611 | -99.2 | 504990 | 50 |
| MR_1774413348_A40A605A | 504990 | 666 | -84.3 | 504990 | 109 | -88.4 | 504990 | 611 | -99.7 | 504990 | 50 |
| MR_1774413348_2C985A0E | 504990 | 666 | -87.3 | 504990 | 109 | -88.8 | 504990 | 611 | -98.4 | 504990 | 50 |
| MR_1774413348_B1AF34FC | 504990 | 666 | -87.2 | 504990 | 109 | -87.7 | 504990 | 611 | -101.2 | 504990 | 50 |
| MR_1774413348_46850440 | 504990 | 666 | -85.6 | 504990 | 109 | -90.8 | 504990 | 611 | -97.9 | 504990 | 50 |
| MR_1774413348_609E827F | 504990 | 666 | -87.5 | 504990 | 109 | -87.4 | 504990 | 611 | -98.5 | 504990 | 50 |
| MR_1774413348_E1F7AF58 | 504990 | 666 | -83.9 | 504990 | 109 | -88.4 | 504990 | 611 | -100.7 | 504990 | 50 |
| MR_1774413348_5806EAC2 | 504990 | 666 | -87.5 | 504990 | 109 | -89.4 | 504990 | 611 | -100.2 | 504990 | 50 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1086: `6b39b611-26d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6b39b611-26d2-475e-bc2b-e8e24c8826fb` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease A3 Offset threshold for 3234941_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1086] topology](images/train_1086.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3254546_3 by 10 degrees
- `C2`: Press down the tilt angle of 3234941_1 by 10 degrees
- `C3`: Increase A3 Offset threshold for 3254546_3
- `C4`: Check test server and transmission issues
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254546_3
- `C6`: Add neighbor relationship between 3234941_1 and 3254546_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234941_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234941_1
- `C9`: Lift the tilt angle of 3234941_1 by 10 degrees
- `C10`: Decrease A3 Offset threshold for 3234941_1 **← 정답**
- `C11`: Decrease transmission power for 3234941_1
- `C12`: Decrease A3 Offset threshold for 3254546_3
- `C13`: Add neighbor relationship between 3226151_2 and 3254546_3
- `C14`: Increase A3 Offset threshold for 3234941_1
- `C15`: Increase transmission power for 3254546_3
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Adjust the azimuth of 3254546_3 by 50 degrees
- `C18`: Decrease transmission power for 3254546_3
- `C19`: Increase transmission power for 3234941_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254546_3
- `C21`: Lift the tilt angle  of 3254546_3 by 10 degrees
- `C22`: Adjust the azimuth of 3234941_1 by 29 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.770 | MS1 | 121.4656774597 | 31.1446207802 | 151 | 504990 | -75.25 | 16.58 | 315.60 | 0.03 | 2.70 | 1599 |
| 2024-09-20 22:21:32.941 | MS1 | 121.4656625574 | 31.1446309283 | 151 | 504990 | -77.75 | 16.53 | 424.32 | 0.09 | 2.31 | 1563 |
| 2024-09-20 22:21:33.253 | MS1 | 121.4656719649 | 31.1446379501 | 151 | 504990 | -84.46 | 15.93 | 334.15 | 0.06 | 2.34 | 1566 |
| 2024-09-20 22:21:34.517 | MS1 | 121.4656732594 | 31.1446230824 | 151 | 504990 | -92.99 | -1.24 | 36.70 | 0.02 | 1.14 | 1597 |
| 2024-09-20 22:21:35.826 | MS1 | 121.4656597951 | 31.1446228690 | 151 | 504990 | -90.64 | -3.41 | 58.38 | 0.14 | 1.02 | 1587 |
| 2024-09-20 22:21:36.360 | MS1 | 121.4656586991 | 31.1446272771 | 151 | 504990 | -89.31 | -1.98 | 52.90 | 0.18 | 1.13 | 1599 |
| 2024-09-20 22:21:37.386 | MS1 | 121.4656695904 | 31.1446273793 | 151 | 504990 | -87.47 | -1.76 | 28.59 | 0.08 | 1.16 | 1587 |
| 2024-09-20 22:21:38.398 | MS1 | 121.4656621956 | 31.1446263070 | 151 | 504990 | -86.27 | -3.98 | 40.15 | 0.05 | 1.35 | 1588 |
| 2024-09-20 22:21:39.505 | MS1 | 121.4656693442 | 31.1446371990 | 759 | 504990 | -75.11 | 15.40 | 258.74 | 0.01 | 1.01 | 1592 |
| 2024-09-20 22:21:40.871 | MS1 | 121.4656644879 | 31.1446233881 | 759 | 504990 | -75.24 | 14.37 | 556.42 | 0.03 | 2.16 | 1568 |
| 2024-09-20 22:21:41.903 | MS1 | 121.4656631899 | 31.1446352095 | 759 | 504990 | -79.99 | 14.58 | 589.22 | 0.04 | 2.27 | 1586 |
| 2024-09-20 22:21:42.632 | MS1 | 121.4656698174 | 31.1446288573 | 759 | 504990 | -76.55 | 14.97 | 373.81 | 0.05 | 2.26 | 1563 |

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
| 3226151 | 2 | 121.4721744633 | 31.1533431574 | 103 | 2 | 12 | 35.5 | TDD | 26 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3234941 | 1 | 121.4743997295 | 31.1556956940 | 185 | 11 | 9 | 47.2 | TDD | 151 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3242122 | 4 | 121.4687852624 | 31.1513818335 | 199 | 5 | 4 | 47.4 | TDD | 447 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3254546 | 3 | 121.4674127830 | 31.1517277106 | 272 | 9 | 3 | 48.4 | TDD | 759 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.453 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.477 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.612 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.612 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.340 | NREventA3 | measId:2;ServCellPCI:56;Ser... |
| 2024-09-20 22:21:38.580 | NRHandoverAttempt | SourcePCI:56;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.629 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.642 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.750 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.750 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234941 | 1 | 9.0558 | 16.8640 | -117.5372 | 11.7681 | 81.7329 | 0.0062 | 0.1729 |
| 2024_09_20 22:00 | 3226151 | 2 | 16.7599 | 13.0890 | -114.9325 | 14.4247 | 159.8805 | 0.0197 | 0.0037 |
| 2024_09_20 22:00 | 3254546 | 3 | 12.1636 | 15.5997 | -117.0783 | 17.7744 | 136.4787 | 0.0028 | 0.0119 |
| 2024_09_20 22:00 | 3242122 | 4 | 9.2522 | 15.4594 | -114.1980 | 17.9278 | 189.7618 | 0.0100 | 0.0099 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414646_7E1430F5 | 504990 | 759 | -88.8 | 504990 | 151 | -92.4 | 504990 | 26 | -89.5 | 504990 | 447 |
| MR_1774414646_715D9B56 | 504990 | 151 | -91.1 | 504990 | 759 | -89.5 | 504990 | 26 | -89.6 | 504990 | 447 |
| MR_1774414646_CB176809 | 504990 | 759 | -86.5 | 504990 | 151 | -94.9 | 504990 | 26 | -89.8 | 504990 | 447 |
| MR_1774414646_AF0C0A22 | 504990 | 759 | -86.5 | 504990 | 151 | -91.5 | 504990 | 26 | -91.3 | 504990 | 447 |
| MR_1774414646_0F364240 | 504990 | 151 | -91.5 | 504990 | 759 | -88.5 | 504990 | 26 | -91.1 | 504990 | 447 |
| MR_1774414646_A8EFD024 | 504990 | 759 | -87.8 | 504990 | 151 | -92.6 | 504990 | 26 | -90.5 | 504990 | 447 |
| MR_1774414646_9DE3CE49 | 504990 | 759 | -86.5 | 504990 | 151 | -95.0 | 504990 | 26 | -92.1 | 504990 | 447 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1087: `360da34b-205...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `360da34b-2054-4b96-98ae-ad92e5022305` |
| Tag | **multiple-answer** |
| 정답 | **C8|C16** |
| C8 의미 | Increase transmission power for 3255949_4 |
| C16 의미 | Adjust the azimuth of 3255949_4 by 33 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1087] topology](images/train_1087.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3265449_3 by 39 degrees
- `C2`: Press down the tilt angle  of 3265449_3 by 5 degrees
- `C3`: Decrease A3 Offset threshold for 3265449_3
- `C4`: Increase A3 Offset threshold for 3265449_3
- `C5`: Lift the tilt angle  of 3265449_3 by 5 degrees
- `C6`: Decrease transmission power for 3265449_3
- `C7`: Add neighbor relationship between 3242196_1 and 3265449_3
- `C8`: Increase transmission power for 3255949_4 **← 정답**
- `C9`: Check test server and transmission issues
- `C10`: Decrease A3 Offset threshold for 3255949_4
- `C11`: Lift the tilt angle of 3255949_4 by 10 degrees
- `C12`: Add neighbor relationship between 3255949_4 and 3265449_3
- `C13`: Decrease transmission power for 3255949_4
- `C14`: Press down the tilt angle of 3255949_4 by 10 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265449_3
- `C16`: Adjust the azimuth of 3255949_4 by 33 degrees **← 정답**
- `C17`: Increase A3 Offset threshold for 3255949_4
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255949_4
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255949_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265449_3
- `C22`: Increase transmission power for 3265449_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.299 | MS1 | 121.4656601503 | 31.1446249098 | 382 | 504990 | -94.18 | 16.23 | 300.44 | 0.16 | 2.91 | 1567 |
| 2024-09-20 22:21:32.636 | MS1 | 121.4656687654 | 31.1446290661 | 382 | 504990 | -88.50 | 12.70 | 419.25 | 0.13 | 2.90 | 1579 |
| 2024-09-20 22:21:33.971 | MS1 | 121.4656674635 | 31.1446239460 | 382 | 504990 | -85.46 | 12.51 | 496.11 | 0.12 | 2.63 | 1566 |
| 2024-09-20 22:21:34.459 | MS1 | 121.4656591427 | 31.1446296847 | 382 | 504990 | -104.53 | 1.67 | 66.47 | 0.09 | 1.22 | 1571 |
| 2024-09-20 22:21:35.186 | MS1 | 121.4656618554 | 31.1446199033 | 382 | 504990 | -101.66 | -1.91 | 60.50 | 0.14 | 1.22 | 1564 |
| 2024-09-20 22:21:36.903 | MS1 | 121.4656709640 | 31.1446288120 | 382 | 504990 | -106.91 | -0.69 | 82.77 | 0.05 | 1.15 | 1569 |
| 2024-09-20 22:21:37.792 | MS1 | 121.4656727992 | 31.1446247982 | 382 | 504990 | -103.31 | 1.43 | 39.03 | 0.07 | 1.43 | 1586 |
| 2024-09-20 22:21:38.628 | MS1 | 121.4656604180 | 31.1446222882 | 382 | 504990 | -104.84 | -1.88 | 49.22 | 0.14 | 1.12 | 1573 |
| 2024-09-20 22:21:39.468 | MS1 | 121.4656613726 | 31.1446293855 | 382 | 504990 | -100.56 | -1.80 | 57.24 | 0.02 | 1.37 | 1600 |
| 2024-09-20 22:21:40.763 | MS1 | 121.4656645315 | 31.1446314072 | 382 | 504990 | -85.57 | 13.30 | 584.59 | 0.10 | 2.49 | 1588 |
| 2024-09-20 22:21:41.990 | MS1 | 121.4656638629 | 31.1446320312 | 382 | 504990 | -92.39 | 13.44 | 296.21 | 0.18 | 2.89 | 1592 |
| 2024-09-20 22:21:42.166 | MS1 | 121.4656621866 | 31.1446327808 | 382 | 504990 | -88.29 | 16.50 | 450.62 | 0.02 | 2.08 | 1582 |

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
| 3217475 | 2 | 121.4715763319 | 31.1451218105 | 354 | 9 | 3 | 17.4 | TDD | 1000 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3242196 | 1 | 121.4743916357 | 31.1518150541 | 296 | 2 | 12 | 20.5 | TDD | 584 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3255949 | 4 | 121.4687540732 | 31.1490113480 | 178 | 10 | 12 | 19.4 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3265449 | 3 | 121.4699190755 | 31.1442531250 | 315 | 0 | 2 | 38.8 | TDD | 372 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.317 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.336 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.445 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.445 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.706 | NREventA2 | measId:1;ServCellPCI:462;Se... |
| 2024-09-20 22:21:34.817 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242196 | 1 | 5.9840 | 16.6527 | -114.6872 | 8.6082 | 121.6433 | 0.0004 | 0.0079 |
| 2024_09_20 22:00 | 3217475 | 2 | 7.5223 | 14.5875 | -115.7588 | 13.1788 | 92.5412 | 0.0129 | 0.0087 |
| 2024_09_20 22:00 | 3265449 | 3 | 11.4765 | 15.5606 | -117.6777 | 17.0577 | 179.1613 | 0.0035 | 0.0171 |
| 2024_09_20 22:00 | 3255949 | 4 | 17.3975 | 14.0600 | -117.4089 | 17.8357 | 188.2741 | 0.1493 | 0.0039 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414607_EADAD791 | 504990 | 382 | -105.8 | 504990 | 372 | -113.1 | 504990 | 584 | -117.6 | 504990 | 1000 |
| MR_1774414607_7AA673A7 | 504990 | 382 | -102.8 | 504990 | 372 | -111.8 | 504990 | 584 | -117.8 | 504990 | 1000 |
| MR_1774414607_E2DA4A3C | 504990 | 382 | -105.6 | 504990 | 372 | -114.2 | 504990 | 584 | -118.1 | 504990 | 1000 |
| MR_1774414607_8C3DB366 | 504990 | 382 | -104.9 | 504990 | 372 | -113.7 | 504990 | 584 | -120.1 | 504990 | 1000 |
| MR_1774414607_BAD268EF | 504990 | 382 | -105.1 | 504990 | 372 | -111.8 | 504990 | 584 | -117.8 | 504990 | 1000 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1088: `15b6fdcd-be8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `15b6fdcd-be81-4c4a-ba05-706dab956c0a` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3274294_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1088] topology](images/train_1088.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3263896_2 by 6 degrees
- `C2`: Adjust the azimuth of 3263896_2 by 50 degrees
- `C3`: Adjust the azimuth of 3274294_1 by 15 degrees
- `C4`: Add neighbor relationship between 3274294_1 and 3263896_2
- `C5`: Decrease A3 Offset threshold for 3263896_2
- `C6`: Decrease transmission power for 3274294_1
- `C7`: Press down the tilt angle of 3274294_1 by 2 degrees
- `C8`: Check test server and transmission issues
- `C9`: Increase A3 Offset threshold for 3263896_2
- `C10`: Increase transmission power for 3274294_1
- `C11`: Increase A3 Offset threshold for 3274294_1
- `C12`: Decrease transmission power for 3263896_2
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Increase transmission power for 3263896_2
- `C15`: Press down the tilt angle  of 3263896_2 by 6 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263896_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263896_2
- `C18`: Decrease A3 Offset threshold for 3274294_1
- `C19`: Lift the tilt angle of 3274294_1 by 2 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274294_1 **← 정답**
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274294_1
- `C22`: Add neighbor relationship between 3239072_3 and 3263896_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.109 | MS1 | 121.4656671325 | 31.1446324442 | 660 | 504990 | -89.96 | 15.93 | 570.00 | 0.02 | 2.70 | 1561 |
| 2024-09-20 22:21:32.970 | MS1 | 121.4656755340 | 31.1446213769 | 660 | 504990 | -85.24 | 12.71 | 496.24 | 0.01 | 2.79 | 1576 |
| 2024-09-20 22:21:33.234 | MS1 | 121.4656596001 | 31.1446297254 | 660 | 504990 | -89.03 | 14.82 | 466.15 | 0.05 | 2.56 | 1565 |
| 2024-09-20 22:21:34.248 | MS1 | 121.4656734875 | 31.1446279671 | 660 | 504990 | -87.43 | 17.68 | 52.82 | 0.56 | 2.64 | 608 |
| 2024-09-20 22:21:35.264 | MS1 | 121.4656727271 | 31.1446342697 | 660 | 504990 | -86.37 | 12.39 | 86.95 | 0.60 | 2.14 | 518 |
| 2024-09-20 22:21:36.988 | MS1 | 121.4656699676 | 31.1446207584 | 660 | 504990 | -86.01 | 17.53 | 83.78 | 0.64 | 2.94 | 531 |
| 2024-09-20 22:21:37.526 | MS1 | 121.4656583977 | 31.1446198165 | 660 | 504990 | -92.11 | 10.42 | 53.74 | 0.56 | 2.54 | 628 |
| 2024-09-20 22:21:38.206 | MS1 | 121.4656747092 | 31.1446359649 | 660 | 504990 | -91.27 | 7.76 | 56.89 | 0.62 | 2.32 | 531 |
| 2024-09-20 22:21:39.426 | MS1 | 121.4656684505 | 31.1446216726 | 660 | 504990 | -93.96 | 7.35 | 47.80 | 0.64 | 2.26 | 513 |
| 2024-09-20 22:21:40.442 | MS1 | 121.4656660932 | 31.1446363779 | 660 | 504990 | -92.45 | 7.68 | 526.71 | 0.16 | 2.84 | 1569 |
| 2024-09-20 22:21:41.314 | MS1 | 121.4656777418 | 31.1446347374 | 660 | 504990 | -91.76 | 10.27 | 477.60 | 0.05 | 2.92 | 1587 |
| 2024-09-20 22:21:42.495 | MS1 | 121.4656713002 | 31.1446304398 | 660 | 504990 | -89.94 | 8.32 | 499.04 | 0.10 | 2.36 | 1562 |

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
| 3234184 | 4 | 121.4713098394 | 31.1502210534 | 329 | 13 | 5 | 31.1 | TDD | 524 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3239072 | 3 | 121.4739093593 | 31.1523142947 | 200 | 6 | 11 | 16.9 | TDD | 908 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3263896 | 2 | 121.4650131273 | 31.1500429470 | 346 | 4 | 4 | 22.6 | TDD | 115 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3274294 | 1 | 121.4700028121 | 31.1543823551 | 186 | 0 | 12 | 44.1 | TDD | 660 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.388 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.405 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.506 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.506 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.288 | NREventA3 | measId:2;ServCellPCI:637;Se... |
| 2024-09-20 22:21:38.528 | NRHandoverAttempt | SourcePCI:637;SourceNR-ARFC... |
| 2024-09-20 22:21:38.558 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.573 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.715 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.715 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274294 | 1 | 17.5223 | 17.0359 | -116.4394 | 11.4099 | 162.8013 | 0.0033 | 0.0143 |
| 2024_09_20 22:00 | 3263896 | 2 | 9.5667 | 13.2332 | -114.4278 | 11.4106 | 185.3712 | 0.0005 | 0.0081 |
| 2024_09_20 22:00 | 3239072 | 3 | 11.9434 | 13.3773 | -115.8630 | 10.6785 | 134.0216 | 0.0180 | 0.0121 |
| 2024_09_20 22:00 | 3234184 | 4 | 16.6148 | 14.4973 | -117.6282 | 14.7686 | 157.4157 | 0.0187 | 0.0193 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413373_A3698290 | 504990 | 660 | -87.6 | 504990 | 115 | -95.1 | 504990 | 908 | -100.4 | 504990 | 524 |
| MR_1774413373_E9F91058 | 504990 | 660 | -85.9 | 504990 | 115 | -93.3 | 504990 | 908 | -102.4 | 504990 | 524 |
| MR_1774413373_C41114B5 | 504990 | 660 | -86.5 | 504990 | 115 | -93.9 | 504990 | 908 | -102.6 | 504990 | 524 |
| MR_1774413373_FE1095E0 | 504990 | 660 | -88.5 | 504990 | 115 | -94.8 | 504990 | 908 | -100.7 | 504990 | 524 |
| MR_1774413373_2557AE84 | 504990 | 660 | -86.4 | 504990 | 115 | -92.8 | 504990 | 908 | -101.2 | 504990 | 524 |
| MR_1774413373_972449B8 | 504990 | 660 | -88.8 | 504990 | 115 | -96.1 | 504990 | 908 | -102.9 | 504990 | 524 |
| MR_1774413373_1A359461 | 504990 | 660 | -86.0 | 504990 | 115 | -93.8 | 504990 | 908 | -101.2 | 504990 | 524 |
| MR_1774413373_BE043F9A | 504990 | 660 | -86.3 | 504990 | 115 | -94.0 | 504990 | 908 | -102.0 | 504990 | 524 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1089: `5c368419-b17...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5c368419-b17f-4dd0-a7bf-4cde5bd5e7e4` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1089] topology](images/train_1089.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3273130_4 by 10 degrees
- `C2`: Adjust the azimuth of 3273130_4 by 50 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273130_4
- `C4`: Adjust the azimuth of 3237066_3 by 50 degrees
- `C5`: Decrease transmission power for 3237066_3
- `C6`: Lift the tilt angle of 3273130_4 by 10 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237066_3
- `C8`: Check test server and transmission issues **← 정답**
- `C9`: Add neighbor relationship between 3234415_2 and 3237066_3
- `C10`: Lift the tilt angle  of 3237066_3 by 2 degrees
- `C11`: Increase transmission power for 3237066_3
- `C12`: Increase A3 Offset threshold for 3237066_3
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Add neighbor relationship between 3273130_4 and 3237066_3
- `C15`: Press down the tilt angle  of 3237066_3 by 2 degrees
- `C16`: Decrease A3 Offset threshold for 3273130_4
- `C17`: Decrease transmission power for 3273130_4
- `C18`: Increase A3 Offset threshold for 3273130_4
- `C19`: Increase transmission power for 3273130_4
- `C20`: Decrease A3 Offset threshold for 3237066_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237066_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273130_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.593 | MS1 | 121.4656638864 | 31.1446275733 | 270 | 504990 | -86.28 | 16.63 | 385.52 | 0.18 | 2.54 | 1592 |
| 2024-09-20 22:21:32.998 | MS1 | 121.4656681059 | 31.1446298392 | 270 | 504990 | -86.88 | 15.05 | 551.52 | 0.17 | 2.50 | 1593 |
| 2024-09-20 22:21:33.868 | MS1 | 121.4656700272 | 31.1446328664 | 270 | 504990 | -86.39 | 12.49 | 326.98 | 0.09 | 2.59 | 1577 |
| 2024-09-20 22:21:34.165 | MS1 | 121.4656665092 | 31.1446376684 | 270 | 504990 | -91.41 | 15.94 | 59.59 | 0.14 | 2.03 | 339 |
| 2024-09-20 22:21:35.174 | MS1 | 121.4656600478 | 31.1446255927 | 270 | 504990 | -85.17 | 15.28 | 81.70 | 0.05 | 2.01 | 446 |
| 2024-09-20 22:21:36.363 | MS1 | 121.4656638512 | 31.1446199532 | 270 | 504990 | -91.34 | 12.19 | 79.01 | 0.11 | 2.52 | 489 |
| 2024-09-20 22:21:37.902 | MS1 | 121.4656615044 | 31.1446332245 | 270 | 504990 | -90.32 | 9.00 | 60.41 | 0.16 | 2.81 | 349 |
| 2024-09-20 22:21:38.787 | MS1 | 121.4656613230 | 31.1446378014 | 270 | 504990 | -90.91 | 9.38 | 91.16 | 0.06 | 2.29 | 309 |
| 2024-09-20 22:21:39.920 | MS1 | 121.4656636513 | 31.1446336840 | 270 | 504990 | -91.12 | 9.59 | 62.85 | 0.19 | 2.63 | 444 |
| 2024-09-20 22:21:40.947 | MS1 | 121.4656622263 | 31.1446355882 | 270 | 504990 | -92.57 | 10.73 | 502.86 | 0.15 | 2.41 | 1581 |
| 2024-09-20 22:21:41.801 | MS1 | 121.4656664329 | 31.1446245732 | 270 | 504990 | -91.55 | 12.36 | 431.19 | 0.11 | 2.55 | 1565 |
| 2024-09-20 22:21:42.616 | MS1 | 121.4656610501 | 31.1446277733 | 270 | 504990 | -92.64 | 7.97 | 386.18 | 0.17 | 2.66 | 1582 |

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
| 3234415 | 2 | 121.4733766754 | 31.1549867348 | 150 | 14 | 3 | 33.8 | TDD | 90 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3237066 | 3 | 121.4722819773 | 31.1555881311 | 45 | 1 | 8 | 19.3 | TDD | 484 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3260511 | 1 | 121.4646519735 | 31.1557634148 | 219 | 13 | 1 | 19.5 | TDD | 793 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3273130 | 4 | 121.4678959546 | 31.1530350267 | 341 | 12 | 0 | 45.5 | TDD | 270 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.087 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.105 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.228 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.228 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.937 | NREventA3 | measId:2;ServCellPCI:565;Se... |
| 2024-09-20 22:21:38.177 | NRHandoverAttempt | SourcePCI:565;SourceNR-ARFC... |
| 2024-09-20 22:21:38.211 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.225 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.371 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.371 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260511 | 1 | 5.6265 | 10.7046 | -116.5842 | 10.2732 | 105.0670 | 0.0105 | 0.0135 |
| 2024_09_20 22:00 | 3234415 | 2 | 14.5426 | 13.2539 | -114.1977 | 15.2956 | 94.3634 | 0.0160 | 0.0175 |
| 2024_09_20 22:00 | 3237066 | 3 | 17.9198 | 18.4738 | -117.9866 | 6.8395 | 116.9453 | 0.0127 | 0.0084 |
| 2024_09_20 22:00 | 3273130 | 4 | 11.2181 | 10.4497 | -115.5762 | 8.0639 | 100.4815 | 0.0038 | 0.0191 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413994_067C496E | 504990 | 270 | -92.5 | 504990 | 484 | -97.8 | 504990 | 90 | -105.1 | 504990 | 793 |
| MR_1774413994_65F76CBB | 504990 | 270 | -92.3 | 504990 | 484 | -97.3 | 504990 | 90 | -105.7 | 504990 | 793 |
| MR_1774413994_BD4896D7 | 504990 | 270 | -92.0 | 504990 | 484 | -98.1 | 504990 | 90 | -103.9 | 504990 | 793 |
| MR_1774413994_31211960 | 504990 | 270 | -91.9 | 504990 | 484 | -100.2 | 504990 | 90 | -105.1 | 504990 | 793 |
| MR_1774413994_116B6424 | 504990 | 270 | -91.9 | 504990 | 484 | -99.7 | 504990 | 90 | -107.0 | 504990 | 793 |

> *... 2개 열 생략 (전체 14열)*

---
