# Track A 문제 분석 — train[1110]~train[1119]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1110] ~ train[1119] (10개)

## 목차

1. [문제 1110: `ff942812-08e...`](#1110) — multiple-answer, 정답: C11|C21
2. [문제 1111: `1ca17ac7-ed6...`](#1111) — single-answer, 정답: C18
3. [문제 1112: `283ec8a3-4ed...`](#1112) — single-answer, 정답: C19
4. [문제 1113: `124753ab-418...`](#1113) — single-answer, 정답: C16
5. [문제 1114: `c9b13772-4c0...`](#1114) — multiple-answer, 정답: C1|C11|C12|C18
6. [문제 1115: `dd6abc67-cad...`](#1115) — single-answer, 정답: C7
7. [문제 1116: `2894db23-47d...`](#1116) — single-answer, 정답: C3
8. [문제 1117: `c25349fa-ec0...`](#1117) — single-answer, 정답: C16
9. [문제 1118: `237e2555-c5c...`](#1118) — single-answer, 정답: C2
10. [문제 1119: `fea290cb-1c8...`](#1119) — multiple-answer, 정답: C3|C14

---

### 문제 1110: `ff942812-08e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ff942812-08ef-480c-b120-18b5074a8d4a` |
| Tag | **multiple-answer** |
| 정답 | **C11|C21** |
| C11 의미 | Decrease transmission power for 3244554_3 |
| C21 의미 | Press down the tilt angle  of 3244554_3 by 3 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1110] topology](images/train_1110.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3223495_2 by 2 degrees
- `C2`: Increase transmission power for 3244554_3
- `C3`: Lift the tilt angle of 3223495_2 by 2 degrees
- `C4`: Decrease A3 Offset threshold for 3223495_2
- `C5`: Decrease transmission power for 3223495_2
- `C6`: Increase transmission power for 3223495_2
- `C7`: Check test server and transmission issues
- `C8`: Add neighbor relationship between 3223495_2 and 3244554_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223495_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244554_3
- `C11`: Decrease transmission power for 3244554_3 **← 정답**
- `C12`: Add neighbor relationship between 3211569_4 and 3244554_3
- `C13`: Adjust the azimuth of 3223495_2 by 21 degrees
- `C14`: Increase A3 Offset threshold for 3244554_3
- `C15`: Increase A3 Offset threshold for 3223495_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244554_3
- `C17`: Lift the tilt angle  of 3244554_3 by 3 degrees
- `C18`: Adjust the azimuth of 3244554_3 by 24 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223495_2
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Press down the tilt angle  of 3244554_3 by 3 degrees **← 정답**
- `C22`: Decrease A3 Offset threshold for 3244554_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.440 | MS1 | 121.4656635868 | 31.1446329501 | 490 | 504990 | -84.59 | 13.28 | 402.83 | 0.16 | 2.05 | 1596 |
| 2024-09-20 22:21:32.498 | MS1 | 121.4656689785 | 31.1446368536 | 490 | 504990 | -76.19 | 16.73 | 511.84 | 0.14 | 2.48 | 1562 |
| 2024-09-20 22:21:33.419 | MS1 | 121.4656746945 | 31.1446327891 | 490 | 504990 | -83.14 | 15.08 | 456.85 | 0.04 | 2.71 | 1600 |
| 2024-09-20 22:21:34.702 | MS1 | 121.4656705480 | 31.1446335993 | 490 | 504990 | -94.87 | 2.86 | 54.44 | 0.15 | 1.48 | 1563 |
| 2024-09-20 22:21:35.708 | MS1 | 121.4656733499 | 31.1446320626 | 490 | 504990 | -88.63 | 2.48 | 75.41 | 0.02 | 1.32 | 1560 |
| 2024-09-20 22:21:36.928 | MS1 | 121.4656674576 | 31.1446249327 | 490 | 504990 | -87.56 | 1.80 | 37.94 | 0.09 | 1.34 | 1567 |
| 2024-09-20 22:21:37.885 | MS1 | 121.4656643851 | 31.1446315086 | 490 | 504990 | -89.34 | 0.61 | 63.96 | 0.10 | 1.31 | 1597 |
| 2024-09-20 22:21:38.704 | MS1 | 121.4656766365 | 31.1446208167 | 490 | 504990 | -86.43 | 3.91 | 73.19 | 0.06 | 1.20 | 1570 |
| 2024-09-20 22:21:39.729 | MS1 | 121.4656654275 | 31.1446230893 | 490 | 504990 | -93.19 | 3.37 | 86.74 | 0.02 | 1.28 | 1570 |
| 2024-09-20 22:21:40.496 | MS1 | 121.4656677262 | 31.1446183825 | 490 | 504990 | -80.52 | 13.07 | 590.60 | 0.03 | 2.55 | 1597 |
| 2024-09-20 22:21:41.197 | MS1 | 121.4656705616 | 31.1446256025 | 490 | 504990 | -76.78 | 12.88 | 461.13 | 0.07 | 2.43 | 1576 |
| 2024-09-20 22:21:42.944 | MS1 | 121.4656735420 | 31.1446299074 | 490 | 504990 | -80.32 | 15.35 | 397.22 | 0.13 | 2.49 | 1576 |

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
| 3211569 | 4 | 121.4668015989 | 31.1442716725 | 298 | 12 | 7 | 48.6 | TDD | 413 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3222225 | 1 | 121.4703641822 | 31.1499871511 | 28 | 2 | 0 | 40.5 | TDD | 841 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3223495 | 2 | 121.4708696974 | 31.1535862651 | 185 | 0 | 3 | 42.4 | TDD | 490 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3244554 | 3 | 121.4645618770 | 31.1524999787 | 197 | 0 | 4 | 41.4 | TDD | 389 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.046 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.064 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.213 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.213 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222225 | 1 | 19.3986 | 19.7338 | -115.8244 | 7.0254 | 117.1976 | 0.0062 | 0.0068 |
| 2024_09_20 22:00 | 3223495 | 2 | 15.6293 | 7.8984 | -109.7421 | 9.1752 | 129.4715 | 0.0181 | 0.0107 |
| 2024_09_20 22:00 | 3244554 | 3 | 5.4231 | 12.3913 | -115.2708 | 15.5880 | 110.3245 | 0.0100 | 0.0107 |
| 2024_09_20 22:00 | 3211569 | 4 | 16.5475 | 12.4309 | -114.4524 | 8.8468 | 138.9256 | 0.0033 | 0.0110 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416799_9DA2CEED | 504990 | 490 | -94.6 | 504990 | 389 | -98.3 | 504990 | 413 | -97.7 | 504990 | 841 |
| MR_1774416799_750BA921 | 504990 | 389 | -93.6 | 504990 | 490 | -97.2 | 504990 | 413 | -97.8 | 504990 | 841 |
| MR_1774416799_6AB1F6E5 | 504990 | 490 | -94.2 | 504990 | 389 | -95.3 | 504990 | 413 | -98.6 | 504990 | 841 |
| MR_1774416799_F9055F41 | 504990 | 389 | -94.6 | 504990 | 490 | -94.8 | 504990 | 413 | -97.9 | 504990 | 841 |
| MR_1774416799_A0A030CB | 504990 | 389 | -94.9 | 504990 | 490 | -96.5 | 504990 | 413 | -98.7 | 504990 | 841 |
| MR_1774416799_415872CD | 504990 | 490 | -95.8 | 504990 | 389 | -95.8 | 504990 | 413 | -96.3 | 504990 | 841 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1111: `1ca17ac7-ed6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1ca17ac7-ed67-4bc4-b8d5-a4931d79e986` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Lift the tilt angle  of 3229246_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1111] topology](images/train_1111.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3274251_2
- `C2`: Decrease transmission power for 3234739_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274251_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274251_2
- `C5`: Add neighbor relationship between 3234739_4 and 3274251_2
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Adjust the azimuth of 3229246_1 by 46 degrees
- `C8`: Adjust the azimuth of 3234739_4 by 31 degrees
- `C9`: Increase transmission power for 3234739_4
- `C10`: Decrease A3 Offset threshold for 3234739_4
- `C11`: Press down the tilt angle of 3234739_4 by 3 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234739_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234739_4
- `C14`: Check test server and transmission issues
- `C15`: Increase A3 Offset threshold for 3234739_4
- `C16`: Press down the tilt angle  of 3229246_1 by 10 degrees
- `C17`: Add neighbor relationship between 3229246_1 and 3274251_2
- `C18`: Lift the tilt angle  of 3229246_1 by 10 degrees **← 정답**
- `C19`: Lift the tilt angle of 3234739_4 by 3 degrees
- `C20`: Decrease transmission power for 3274251_2
- `C21`: Increase transmission power for 3274251_2
- `C22`: Increase A3 Offset threshold for 3274251_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.784 | MS1 | 121.4656610989 | 31.1446185017 | 373 | 504990 | -88.76 | 13.42 | 377.14 | 0.14 | 2.62 | 1590 |
| 2024-09-20 22:21:32.758 | MS1 | 121.4656681583 | 31.1446204451 | 373 | 504990 | -90.47 | 17.61 | 556.72 | 0.16 | 2.16 | 1573 |
| 2024-09-20 22:21:33.846 | MS1 | 121.4656700336 | 31.1446189998 | 373 | 504990 | -91.69 | 16.84 | 525.47 | 0.11 | 2.01 | 1592 |
| 2024-09-20 22:21:34.764 | MS1 | 121.4656721398 | 31.1446252040 | 373 | 504990 | -89.33 | 17.51 | 105.20 | 0.03 | 2.85 | 1561 |
| 2024-09-20 22:21:35.268 | MS1 | 121.4656736888 | 31.1446364410 | 373 | 504990 | -86.88 | 17.38 | 94.72 | 0.09 | 2.75 | 1587 |
| 2024-09-20 22:21:36.124 | MS1 | 121.4656702296 | 31.1446372647 | 373 | 504990 | -87.46 | 17.24 | 92.45 | 0.16 | 2.93 | 1586 |
| 2024-09-20 22:21:37.885 | MS1 | 121.4656679355 | 31.1446207479 | 373 | 504990 | -89.26 | 7.50 | 91.55 | 0.15 | 2.54 | 1586 |
| 2024-09-20 22:21:38.404 | MS1 | 121.4656599740 | 31.1446249253 | 373 | 504990 | -92.55 | 10.99 | 78.45 | 0.15 | 2.48 | 1595 |
| 2024-09-20 22:21:39.618 | MS1 | 121.4656720179 | 31.1446206149 | 373 | 504990 | -93.76 | 9.72 | 74.40 | 0.09 | 2.29 | 1577 |
| 2024-09-20 22:21:40.571 | MS1 | 121.4656664135 | 31.1446362946 | 373 | 504990 | -91.61 | 8.20 | 308.95 | 0.19 | 2.08 | 1599 |
| 2024-09-20 22:21:41.512 | MS1 | 121.4656756172 | 31.1446219979 | 373 | 504990 | -92.01 | 7.00 | 586.86 | 0.13 | 2.58 | 1593 |
| 2024-09-20 22:21:42.219 | MS1 | 121.4656772036 | 31.1446367821 | 373 | 504990 | -93.54 | 8.31 | 586.36 | 0.06 | 2.43 | 1577 |

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
| 3229246 | 1 | 121.4730219868 | 31.1559560174 | 349 | 5 | 4 | 39.6 | TDD | 968 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3234739 | 4 | 121.4739291459 | 31.1453942314 | 233 | 1 | 10 | 29.0 | TDD | 373 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3273809 | 3 | 121.4734589043 | 31.1457309610 | 207 | 15 | 12 | 30.1 | TDD | 364 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3274251 | 2 | 121.4651938714 | 31.1479427135 | 127 | 10 | 9 | 23.2 | TDD | 562 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.367 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.383 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.519 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.519 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.167 | NREventA3 | measId:2;ServCellPCI:316;Se... |
| 2024-09-20 22:21:38.407 | NRHandoverAttempt | SourcePCI:316;SourceNR-ARFC... |
| 2024-09-20 22:21:38.456 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.469 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.595 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.595 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229246 | 1 | 14.1258 | 13.5409 | -114.8447 | 17.5053 | 139.4940 | 0.0073 | 0.0110 |
| 2024_09_20 22:00 | 3274251 | 2 | 13.5045 | 12.5390 | -117.5120 | 19.7621 | 163.5523 | 0.0112 | 0.0191 |
| 2024_09_20 22:00 | 3273809 | 3 | 9.6877 | 13.8332 | -114.4799 | 17.4956 | 163.0300 | 0.0079 | 0.0186 |
| 2024_09_20 22:00 | 3234739 | 4 | 78.0108 | 78.0024 | -117.6685 | 18.0478 | 176.4057 | 0.0014 | 0.0185 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416700_B7C8E2DB | 504990 | 373 | -87.4 | 504990 | 562 | -87.8 | 504990 | 968 | -99.2 | 504990 | 364 |
| MR_1774416700_88B75012 | 504990 | 373 | -88.5 | 504990 | 562 | -87.0 | 504990 | 968 | -97.6 | 504990 | 364 |
| MR_1774416700_7371D39C | 504990 | 373 | -87.6 | 504990 | 562 | -87.1 | 504990 | 968 | -97.2 | 504990 | 364 |
| MR_1774416700_F02EC51E | 504990 | 373 | -88.2 | 504990 | 562 | -85.0 | 504990 | 968 | -98.3 | 504990 | 364 |
| MR_1774416700_350EBD69 | 504990 | 373 | -88.8 | 504990 | 562 | -85.6 | 504990 | 968 | -98.6 | 504990 | 364 |
| MR_1774416700_EAE226AF | 504990 | 373 | -87.1 | 504990 | 562 | -88.0 | 504990 | 968 | -99.0 | 504990 | 364 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1112: `283ec8a3-4ed...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `283ec8a3-4ed1-4523-8f11-6c0dcc074da3` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1112] topology](images/train_1112.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259658_2
- `C2`: Increase A3 Offset threshold for 3263977_1
- `C3`: Press down the tilt angle of 3259658_2 by 10 degrees
- `C4`: Decrease transmission power for 3263977_1
- `C5`: Increase transmission power for 3259658_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263977_1
- `C7`: Lift the tilt angle  of 3263977_1 by 8 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Add neighbor relationship between 3259658_2 and 3263977_1
- `C10`: Increase A3 Offset threshold for 3259658_2
- `C11`: Increase transmission power for 3263977_1
- `C12`: Decrease A3 Offset threshold for 3259658_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263977_1
- `C14`: Lift the tilt angle of 3259658_2 by 10 degrees
- `C15`: Adjust the azimuth of 3263977_1 by 50 degrees
- `C16`: Decrease A3 Offset threshold for 3263977_1
- `C17`: Press down the tilt angle  of 3263977_1 by 8 degrees
- `C18`: Adjust the azimuth of 3259658_2 by 28 degrees
- `C19`: Check test server and transmission issues **← 정답**
- `C20`: Decrease transmission power for 3259658_2
- `C21`: Add neighbor relationship between 3257838_4 and 3263977_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259658_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.661 | MS1 | 121.4656687582 | 31.1446325830 | 195 | 504990 | -86.78 | 16.90 | 570.44 | 0.12 | 2.78 | 1586 |
| 2024-09-20 22:21:32.432 | MS1 | 121.4656724266 | 31.1446292582 | 195 | 504990 | -91.71 | 13.46 | 483.00 | 0.06 | 2.80 | 1597 |
| 2024-09-20 22:21:33.300 | MS1 | 121.4656656224 | 31.1446301741 | 195 | 504990 | -86.77 | 15.05 | 599.72 | 0.10 | 2.69 | 1565 |
| 2024-09-20 22:21:34.122 | MS1 | 121.4656637174 | 31.1446255472 | 195 | 504990 | -90.59 | 12.60 | 55.50 | 0.03 | 2.29 | 363 |
| 2024-09-20 22:21:35.133 | MS1 | 121.4656764188 | 31.1446330520 | 195 | 504990 | -91.06 | 12.69 | 106.75 | 0.12 | 2.94 | 500 |
| 2024-09-20 22:21:36.826 | MS1 | 121.4656616409 | 31.1446257496 | 195 | 504990 | -89.01 | 14.51 | 74.56 | 0.17 | 2.02 | 443 |
| 2024-09-20 22:21:37.792 | MS1 | 121.4656595624 | 31.1446202322 | 195 | 504990 | -93.80 | 8.46 | 64.79 | 0.04 | 2.76 | 453 |
| 2024-09-20 22:21:38.941 | MS1 | 121.4656720246 | 31.1446225224 | 195 | 504990 | -92.50 | 9.77 | 50.02 | 0.02 | 2.71 | 384 |
| 2024-09-20 22:21:39.544 | MS1 | 121.4656684684 | 31.1446319694 | 195 | 504990 | -92.47 | 8.39 | 77.47 | 0.05 | 2.55 | 353 |
| 2024-09-20 22:21:40.131 | MS1 | 121.4656730290 | 31.1446227533 | 195 | 504990 | -91.89 | 11.85 | 390.95 | 0.07 | 2.63 | 1581 |
| 2024-09-20 22:21:41.583 | MS1 | 121.4656657873 | 31.1446265793 | 195 | 504990 | -91.70 | 7.48 | 370.99 | 0.12 | 2.63 | 1587 |
| 2024-09-20 22:21:42.196 | MS1 | 121.4656759275 | 31.1446215319 | 195 | 504990 | -93.75 | 11.08 | 416.56 | 0.19 | 2.39 | 1590 |

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
| 3257838 | 4 | 121.4642435874 | 31.1451411510 | 58 | 6 | 9 | 41.3 | TDD | 591 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3259658 | 2 | 121.4678941986 | 31.1543187268 | 219 | 13 | 5 | 32.2 | TDD | 195 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3263977 | 1 | 121.4686093093 | 31.1510087349 | 58 | 6 | 5 | 31.7 | TDD | 680 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3264083 | 3 | 121.4725693460 | 31.1478655164 | 218 | 2 | 0 | 42.1 | TDD | 395 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.576 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.597 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.737 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.737 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.408 | NREventA3 | measId:2;ServCellPCI:333;Se... |
| 2024-09-20 22:21:38.648 | NRHandoverAttempt | SourcePCI:333;SourceNR-ARFC... |
| 2024-09-20 22:21:38.685 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.695 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.820 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.820 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263977 | 1 | 12.2310 | 10.2988 | -117.7121 | 14.2311 | 172.0941 | 0.0055 | 0.0038 |
| 2024_09_20 22:00 | 3259658 | 2 | 10.4256 | 16.1555 | -114.2155 | 11.9229 | 136.9786 | 0.0115 | 0.0103 |
| 2024_09_20 22:00 | 3264083 | 3 | 11.7582 | 18.7818 | -116.8652 | 11.8078 | 130.3801 | 0.0130 | 0.0030 |
| 2024_09_20 22:00 | 3257838 | 4 | 14.3374 | 7.8460 | -116.0275 | 15.3674 | 138.9983 | 0.0145 | 0.0087 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415737_3569B72B | 504990 | 195 | -90.3 | 504990 | 680 | -91.9 | 504990 | 591 | -103.7 | 504990 | 395 |
| MR_1774415737_8D499DD3 | 504990 | 195 | -92.2 | 504990 | 680 | -88.8 | 504990 | 591 | -105.4 | 504990 | 395 |
| MR_1774415737_E2F25F9E | 504990 | 195 | -90.1 | 504990 | 680 | -89.1 | 504990 | 591 | -103.3 | 504990 | 395 |
| MR_1774415737_97F25585 | 504990 | 195 | -89.4 | 504990 | 680 | -92.1 | 504990 | 591 | -102.9 | 504990 | 395 |
| MR_1774415737_EC2B38AE | 504990 | 195 | -91.6 | 504990 | 680 | -90.3 | 504990 | 591 | -104.8 | 504990 | 395 |
| MR_1774415737_6E7C40C3 | 504990 | 195 | -90.7 | 504990 | 680 | -89.9 | 504990 | 591 | -104.8 | 504990 | 395 |
| MR_1774415737_A8E371D2 | 504990 | 195 | -89.7 | 504990 | 680 | -88.9 | 504990 | 591 | -102.2 | 504990 | 395 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1113: `124753ab-418...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `124753ab-418f-4671-9a49-176f84ce79ab` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Add neighbor relationship between 3250449_4 and 3274969_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1113] topology](images/train_1113.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3250449_4
- `C2`: Increase transmission power for 3274969_1
- `C3`: Adjust the azimuth of 3250449_4 by 18 degrees
- `C4`: Decrease transmission power for 3274969_1
- `C5`: Decrease A3 Offset threshold for 3274969_1
- `C6`: Check test server and transmission issues
- `C7`: Increase transmission power for 3250449_4
- `C8`: Increase A3 Offset threshold for 3274969_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274969_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250449_4
- `C11`: Lift the tilt angle of 3250449_4 by 10 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease transmission power for 3250449_4
- `C14`: Lift the tilt angle  of 3274969_1 by 4 degrees
- `C15`: Adjust the azimuth of 3274969_1 by 28 degrees
- `C16`: Add neighbor relationship between 3250449_4 and 3274969_1 **← 정답**
- `C17`: Press down the tilt angle  of 3274969_1 by 4 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250449_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274969_1
- `C20`: Increase A3 Offset threshold for 3250449_4
- `C21`: Press down the tilt angle of 3250449_4 by 10 degrees
- `C22`: Add neighbor relationship between 3236425_3 and 3274969_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.252 | MS1 | 121.4656768929 | 31.1446211874 | 805 | 504990 | -76.77 | 17.97 | 371.02 | 0.11 | 2.42 | 1570 |
| 2024-09-20 22:21:32.289 | MS1 | 121.4656730160 | 31.1446293699 | 805 | 504990 | -83.77 | 14.91 | 524.50 | 0.10 | 2.96 | 1582 |
| 2024-09-20 22:21:33.200 | MS1 | 121.4656634654 | 31.1446362519 | 805 | 504990 | -75.76 | 16.00 | 510.62 | 0.03 | 2.85 | 1592 |
| 2024-09-20 22:21:34.951 | MS1 | 121.4656621201 | 31.1446229022 | 805 | 504990 | -90.81 | -3.24 | 38.32 | 0.06 | 1.33 | 1569 |
| 2024-09-20 22:21:35.290 | MS1 | 121.4656682672 | 31.1446254296 | 805 | 504990 | -85.07 | -0.85 | 71.48 | 0.09 | 1.47 | 1598 |
| 2024-09-20 22:21:36.627 | MS1 | 121.4656762451 | 31.1446361193 | 805 | 504990 | -86.37 | -0.82 | 78.54 | 0.15 | 1.48 | 1598 |
| 2024-09-20 22:21:37.383 | MS1 | 121.4656638047 | 31.1446300941 | 805 | 504990 | -89.07 | -2.28 | 49.51 | 0.01 | 1.40 | 1580 |
| 2024-09-20 22:21:38.385 | MS1 | 121.4656775683 | 31.1446334217 | 805 | 504990 | -75.37 | 13.08 | 412.06 | 0.03 | 1.25 | 1593 |
| 2024-09-20 22:21:39.456 | MS1 | 121.4656635869 | 31.1446352495 | 805 | 504990 | -75.44 | 16.03 | 467.35 | 0.14 | 1.23 | 1575 |
| 2024-09-20 22:21:40.285 | MS1 | 121.4656617169 | 31.1446186454 | 805 | 504990 | -78.09 | 17.63 | 593.68 | 0.02 | 2.43 | 1577 |
| 2024-09-20 22:21:41.627 | MS1 | 121.4656719038 | 31.1446181006 | 805 | 504990 | -80.80 | 12.46 | 312.43 | 0.03 | 2.22 | 1594 |
| 2024-09-20 22:21:42.357 | MS1 | 121.4656600395 | 31.1446263431 | 805 | 504990 | -79.31 | 14.59 | 528.49 | 0.13 | 2.23 | 1597 |

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
| 3224330 | 2 | 121.4699156911 | 31.1502550183 | 164 | 0 | 6 | 29.4 | TDD | 123 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3236425 | 3 | 121.4702945919 | 31.1511448844 | 203 | 0 | 1 | 22.6 | TDD | 156 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3250449 | 4 | 121.4753419433 | 31.1483839751 | 264 | 15 | 11 | 37.3 | TDD | 805 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3274969 | 1 | 121.4710743341 | 31.1462919143 | 278 | 2 | 2 | 20.2 | TDD | 97 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.914 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.934 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.069 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.069 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.742 | NREventA3 | measId:2;ServCellPCI:787;Se... |
| 2024-09-20 22:21:35.742 | NREventA3 | measId:2;ServCellPCI:787;Se... |
| 2024-09-20 22:21:36.742 | NREventA3 | measId:2;ServCellPCI:787;Se... |
| 2024-09-20 22:21:39.242 | NRRRCReestablishAttempt | PCI:787 |
| 2024-09-20 22:21:39.258 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.272 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.417 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.417 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274969 | 1 | 15.3084 | 8.6214 | -116.1524 | 7.9311 | 132.9165 | 0.0056 | 0.0184 |
| 2024_09_20 22:00 | 3224330 | 2 | 9.2863 | 11.5776 | -116.7604 | 7.7165 | 195.8948 | 0.0188 | 0.0078 |
| 2024_09_20 22:00 | 3236425 | 3 | 9.4157 | 9.2018 | -116.5302 | 16.3113 | 129.1706 | 0.0126 | 0.0017 |
| 2024_09_20 22:00 | 3250449 | 4 | 5.0965 | 7.3776 | -116.7115 | 19.8428 | 95.6426 | 0.0166 | 0.1184 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414028_ECDB7254 | 504990 | 97 | -88.3 | 504990 | 805 | -90.7 | 504990 | 156 | -86.8 | 504990 | 123 |
| MR_1774414028_3453788F | 504990 | 805 | -92.3 | 504990 | 97 | -87.5 | 504990 | 156 | -87.8 | 504990 | 123 |
| MR_1774414028_984CE667 | 504990 | 805 | -89.9 | 504990 | 97 | -87.1 | 504990 | 156 | -88.8 | 504990 | 123 |
| MR_1774414028_59232776 | 504990 | 97 | -88.1 | 504990 | 805 | -92.4 | 504990 | 156 | -89.4 | 504990 | 123 |
| MR_1774414028_CA77F6E6 | 504990 | 97 | -86.9 | 504990 | 805 | -91.6 | 504990 | 156 | -89.7 | 504990 | 123 |
| MR_1774414028_B3A67624 | 504990 | 805 | -89.1 | 504990 | 97 | -85.9 | 504990 | 156 | -90.2 | 504990 | 123 |
| MR_1774414028_B3303E6B | 504990 | 97 | -85.3 | 504990 | 805 | -92.7 | 504990 | 156 | -87.7 | 504990 | 123 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1114: `c9b13772-4c0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c9b13772-4c0e-443a-99cd-2debb0836f3a` |
| Tag | **multiple-answer** |
| 정답 | **C1|C11|C12|C18** |
| C1 의미 | Press down the tilt angle  of 3238848_3 by 5 degrees |
| C11 의미 | Decrease transmission power for 3238848_3 |
| C12 의미 | Increase A3 Offset threshold for 3238848_3 |
| C18 의미 | Increase A3 Offset threshold for 3217735_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1114] topology](images/train_1114.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3238848_3 by 5 degrees **← 정답**
- `C2`: Increase transmission power for 3238848_3
- `C3`: Lift the tilt angle of 3217735_4 by 2 degrees
- `C4`: Add neighbor relationship between 3256834_2 and 3238848_3
- `C5`: Lift the tilt angle  of 3238848_3 by 5 degrees
- `C6`: Increase transmission power for 3217735_4
- `C7`: Decrease A3 Offset threshold for 3217735_4
- `C8`: Adjust the azimuth of 3238848_3 by 8 degrees
- `C9`: Decrease A3 Offset threshold for 3238848_3
- `C10`: Check test server and transmission issues
- `C11`: Decrease transmission power for 3238848_3 **← 정답**
- `C12`: Increase A3 Offset threshold for 3238848_3 **← 정답**
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217735_4
- `C14`: Decrease transmission power for 3217735_4
- `C15`: Add neighbor relationship between 3217735_4 and 3238848_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238848_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217735_4
- `C18`: Increase A3 Offset threshold for 3217735_4 **← 정답**
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238848_3
- `C20`: Adjust the azimuth of 3217735_4 by 9 degrees
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Press down the tilt angle of 3217735_4 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.816 | MS1 | 121.4656685279 | 31.1446203928 | 154 | 504990 | -76.66 | 13.48 | 406.02 | 0.20 | 2.60 | 1597 |
| 2024-09-20 22:21:32.807 | MS1 | 121.4656722187 | 31.1446240871 | 154 | 504990 | -81.48 | 13.89 | 495.35 | 0.01 | 2.99 | 1599 |
| 2024-09-20 22:21:33.941 | MS1 | 121.4656757680 | 31.1446304824 | 154 | 504990 | -76.41 | 12.81 | 486.18 | 0.18 | 2.19 | 1599 |
| 2024-09-20 22:21:34.957 | MS1 | 121.4656688735 | 31.1446247028 | 512 | 504990 | -86.26 | 4.87 | 72.10 | 0.18 | 1.05 | 1583 |
| 2024-09-20 22:21:35.559 | MS1 | 121.4656725382 | 31.1446326622 | 512 | 504990 | -89.40 | 4.27 | 35.01 | 0.08 | 1.44 | 1566 |
| 2024-09-20 22:21:36.637 | MS1 | 121.4656627536 | 31.1446256591 | 154 | 504990 | -89.41 | 3.73 | 69.49 | 0.09 | 1.42 | 1591 |
| 2024-09-20 22:21:37.732 | MS1 | 121.4656653654 | 31.1446180322 | 154 | 504990 | -82.78 | 2.59 | 41.36 | 0.11 | 1.38 | 1579 |
| 2024-09-20 22:21:38.131 | MS1 | 121.4656628422 | 31.1446189144 | 512 | 504990 | -89.64 | 1.29 | 79.59 | 0.19 | 1.12 | 1569 |
| 2024-09-20 22:21:39.741 | MS1 | 121.4656590185 | 31.1446373103 | 512 | 504990 | -89.47 | 4.96 | 45.17 | 0.15 | 1.44 | 1592 |
| 2024-09-20 22:21:40.755 | MS1 | 121.4656750573 | 31.1446231046 | 512 | 504990 | -75.83 | 14.79 | 303.58 | 0.05 | 2.85 | 1575 |
| 2024-09-20 22:21:41.972 | MS1 | 121.4656682670 | 31.1446358219 | 512 | 504990 | -79.65 | 12.06 | 332.92 | 0.19 | 2.68 | 1595 |
| 2024-09-20 22:21:42.413 | MS1 | 121.4656641724 | 31.1446269332 | 512 | 504990 | -81.59 | 14.91 | 430.06 | 0.00 | 2.26 | 1581 |

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
| 3217735 | 4 | 121.4641699724 | 31.1558788660 | 182 | 0 | 7 | 38.3 | TDD | 154 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3225265 | 5 | 121.4689963327 | 31.1517523645 | 300 | 11 | 0 | 31.5 | TDD | 347 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3238848 | 3 | 121.4744106382 | 31.1538166161 | 211 | 3 | 1 | 40.1 | TDD | 133 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3256834 | 2 | 121.4730273398 | 31.1548500246 | 343 | 10 | 0 | 45.4 | TDD | 769 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3275470 | 1 | 121.4646936461 | 31.1544743651 | 73 | 11 | 4 | 37.8 | TDD | 512 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.229 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.247 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.371 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.371 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.051 | NREventA3 | measId:2;ServCellPCI:82;Ser... |
| 2024-09-20 22:21:34.291 | NRHandoverAttempt | SourcePCI:82;SourceNR-ARFCN... |
| 2024-09-20 22:21:34.336 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.351 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.482 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.482 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.051 | NREventA3 | measId:2;ServCellPCI:697;Se... |
| 2024-09-20 22:21:36.291 | NRHandoverAttempt | SourcePCI:697;SourceNR-ARFC... |
| 2024-09-20 22:21:36.326 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.340 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.457 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.457 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.051 | NREventA3 | measId:2;ServCellPCI:82;Ser... |
| 2024-09-20 22:21:38.291 | NRHandoverAttempt | SourcePCI:82;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.333 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.344 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.449 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.449 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275470 | 1 | 8.3019 | 10.3797 | -114.1778 | 11.8045 | 116.4620 | 0.0014 | 0.0055 |
| 2024_09_20 22:00 | 3256834 | 2 | 11.5553 | 16.8387 | -114.7705 | 11.6423 | 168.6108 | 0.0182 | 0.0070 |
| 2024_09_20 22:00 | 3238848 | 3 | 5.3407 | 7.5620 | -117.8964 | 14.7835 | 141.6522 | 0.0054 | 0.0097 |
| 2024_09_20 22:00 | 3217735 | 4 | 16.7090 | 6.1511 | -115.9146 | 15.9749 | 113.9050 | 0.0011 | 0.0185 |
| 2024_09_20 22:00 | 3225265 | 5 | 16.0956 | 17.9922 | -115.1611 | 15.9580 | 174.7442 | 0.0066 | 0.0127 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412977_2A091587 | 504990 | 512 | -86.0 | 504990 | 154 | -87.8 | 504990 | 133 | -90.4 | 504990 | 769 |
| MR_1774412977_DF71225D | 504990 | 512 | -86.1 | 504990 | 154 | -88.1 | 504990 | 133 | -90.9 | 504990 | 769 |
| MR_1774412977_7061FBAF | 504990 | 512 | -87.8 | 504990 | 154 | -85.8 | 504990 | 133 | -90.7 | 504990 | 769 |
| MR_1774412977_A20F7850 | 504990 | 512 | -86.1 | 504990 | 154 | -86.7 | 504990 | 133 | -88.3 | 504990 | 769 |
| MR_1774412977_CD087AF9 | 504990 | 512 | -86.1 | 504990 | 154 | -85.9 | 504990 | 133 | -90.1 | 504990 | 769 |
| MR_1774412977_13FB5356 | 504990 | 512 | -86.0 | 504990 | 154 | -86.9 | 504990 | 133 | -88.3 | 504990 | 769 |
| MR_1774412977_88D51174 | 504990 | 154 | -85.6 | 504990 | 512 | -87.9 | 504990 | 133 | -91.6 | 504990 | 769 |
| MR_1774412977_BF917F96 | 504990 | 512 | -87.6 | 504990 | 154 | -88.1 | 504990 | 133 | -89.8 | 504990 | 769 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1115: `dd6abc67-cad...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dd6abc67-cad6-498b-985a-a202f73de763` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease A3 Offset threshold for 3221159_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1115] topology](images/train_1115.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3221159_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229197_4
- `C3`: Lift the tilt angle of 3221159_1 by 9 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Check test server and transmission issues
- `C6`: Increase transmission power for 3221159_1
- `C7`: Decrease A3 Offset threshold for 3221159_1 **← 정답**
- `C8`: Add neighbor relationship between 3221907_3 and 3229197_4
- `C9`: Press down the tilt angle of 3221159_1 by 9 degrees
- `C10`: Lift the tilt angle  of 3229197_4 by 5 degrees
- `C11`: Add neighbor relationship between 3221159_1 and 3229197_4
- `C12`: Increase A3 Offset threshold for 3229197_4
- `C13`: Decrease transmission power for 3229197_4
- `C14`: Increase transmission power for 3229197_4
- `C15`: Adjust the azimuth of 3229197_4 by 50 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229197_4
- `C17`: Decrease transmission power for 3221159_1
- `C18`: Adjust the azimuth of 3221159_1 by 50 degrees
- `C19`: Press down the tilt angle  of 3229197_4 by 5 degrees
- `C20`: Decrease A3 Offset threshold for 3229197_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221159_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221159_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.724 | MS1 | 121.4656715682 | 31.1446370186 | 493 | 504990 | -78.77 | 14.50 | 421.24 | 0.15 | 2.39 | 1597 |
| 2024-09-20 22:21:32.452 | MS1 | 121.4656712740 | 31.1446183079 | 493 | 504990 | -81.80 | 16.40 | 602.94 | 0.04 | 2.98 | 1598 |
| 2024-09-20 22:21:33.885 | MS1 | 121.4656749352 | 31.1446310079 | 493 | 504990 | -75.18 | 13.10 | 335.39 | 0.02 | 2.18 | 1574 |
| 2024-09-20 22:21:34.251 | MS1 | 121.4656601251 | 31.1446352248 | 493 | 504990 | -84.97 | -1.89 | 36.31 | 0.11 | 1.27 | 1594 |
| 2024-09-20 22:21:35.282 | MS1 | 121.4656628947 | 31.1446368377 | 493 | 504990 | -88.05 | -3.65 | 34.84 | 0.18 | 1.08 | 1571 |
| 2024-09-20 22:21:36.460 | MS1 | 121.4656584353 | 31.1446249798 | 493 | 504990 | -83.16 | -2.39 | 50.81 | 0.12 | 1.09 | 1567 |
| 2024-09-20 22:21:37.554 | MS1 | 121.4656737200 | 31.1446351867 | 493 | 504990 | -85.00 | -0.56 | 78.31 | 0.20 | 1.02 | 1593 |
| 2024-09-20 22:21:38.406 | MS1 | 121.4656678570 | 31.1446200150 | 493 | 504990 | -88.62 | -2.76 | 33.96 | 0.18 | 1.44 | 1567 |
| 2024-09-20 22:21:39.532 | MS1 | 121.4656679551 | 31.1446248263 | 163 | 504990 | -77.97 | 17.63 | 213.22 | 0.11 | 1.32 | 1591 |
| 2024-09-20 22:21:40.539 | MS1 | 121.4656639312 | 31.1446180145 | 163 | 504990 | -80.53 | 12.32 | 297.76 | 0.03 | 2.58 | 1592 |
| 2024-09-20 22:21:41.814 | MS1 | 121.4656749635 | 31.1446353556 | 163 | 504990 | -84.26 | 16.91 | 457.35 | 0.05 | 2.90 | 1590 |
| 2024-09-20 22:21:42.707 | MS1 | 121.4656631955 | 31.1446319763 | 163 | 504990 | -75.76 | 12.39 | 514.78 | 0.12 | 2.12 | 1581 |

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
| 3210247 | 2 | 121.4731144671 | 31.1526727656 | 95 | 0 | 4 | 48.3 | TDD | 539 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3221159 | 1 | 121.4757524242 | 31.1507546935 | 174 | 7 | 3 | 31.7 | TDD | 493 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3221907 | 3 | 121.4732546723 | 31.1537996013 | 305 | 12 | 10 | 43.7 | TDD | 580 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3229197 | 4 | 121.4697709585 | 31.1491985286 | 283 | 3 | 7 | 25.1 | TDD | 163 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.181 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.196 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.324 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.324 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.059 | NREventA3 | measId:2;ServCellPCI:889;Se... |
| 2024-09-20 22:21:38.299 | NRHandoverAttempt | SourcePCI:889;SourceNR-ARFC... |
| 2024-09-20 22:21:38.338 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.349 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.484 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.484 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221159 | 1 | 12.1342 | 9.6657 | -117.4488 | 7.1269 | 159.7063 | 0.0022 | 0.1847 |
| 2024_09_20 22:00 | 3210247 | 2 | 17.5010 | 5.9583 | -115.3631 | 11.5545 | 135.4727 | 0.0112 | 0.0091 |
| 2024_09_20 22:00 | 3221907 | 3 | 11.7925 | 9.6604 | -114.9162 | 17.9657 | 123.7493 | 0.0185 | 0.0051 |
| 2024_09_20 22:00 | 3229197 | 4 | 5.2595 | 5.6851 | -114.1384 | 15.6546 | 185.7242 | 0.0065 | 0.0156 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417004_867010A0 | 504990 | 493 | -84.0 | 504990 | 163 | -81.5 | 504990 | 580 | -85.3 | 504990 | 539 |
| MR_1774417004_F0A9430A | 504990 | 493 | -84.0 | 504990 | 163 | -81.3 | 504990 | 580 | -85.6 | 504990 | 539 |
| MR_1774417004_14264BF7 | 504990 | 163 | -80.8 | 504990 | 493 | -85.0 | 504990 | 580 | -83.2 | 504990 | 539 |
| MR_1774417004_477A134D | 504990 | 493 | -84.1 | 504990 | 163 | -81.8 | 504990 | 580 | -83.8 | 504990 | 539 |
| MR_1774417004_93AA2442 | 504990 | 163 | -81.4 | 504990 | 493 | -83.7 | 504990 | 580 | -82.8 | 504990 | 539 |
| MR_1774417004_95368C88 | 504990 | 163 | -80.2 | 504990 | 493 | -86.0 | 504990 | 580 | -84.4 | 504990 | 539 |
| MR_1774417004_9B5EF7C0 | 504990 | 493 | -85.1 | 504990 | 163 | -82.2 | 504990 | 580 | -85.9 | 504990 | 539 |
| MR_1774417004_964A69F1 | 504990 | 163 | -80.0 | 504990 | 493 | -86.4 | 504990 | 580 | -85.0 | 504990 | 539 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1116: `2894db23-47d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2894db23-47d7-4d16-ba11-197e3efebb22` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3276059_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1116] topology](images/train_1116.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3276059_4 by 3 degrees
- `C2`: Check test server and transmission issues
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276059_4 **← 정답**
- `C4`: Adjust the azimuth of 3241026_1 by 50 degrees
- `C5`: Increase transmission power for 3241026_1
- `C6`: Decrease transmission power for 3241026_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276059_4
- `C8`: Lift the tilt angle of 3276059_4 by 3 degrees
- `C9`: Increase A3 Offset threshold for 3241026_1
- `C10`: Add neighbor relationship between 3276059_4 and 3241026_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241026_1
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Increase transmission power for 3276059_4
- `C14`: Decrease A3 Offset threshold for 3241026_1
- `C15`: Adjust the azimuth of 3276059_4 by 0 degrees
- `C16`: Decrease transmission power for 3276059_4
- `C17`: Increase A3 Offset threshold for 3276059_4
- `C18`: Press down the tilt angle  of 3241026_1 by 10 degrees
- `C19`: Lift the tilt angle  of 3241026_1 by 10 degrees
- `C20`: Add neighbor relationship between 3245056_2 and 3241026_1
- `C21`: Decrease A3 Offset threshold for 3276059_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241026_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.855 | MS1 | 121.4656723350 | 31.1446325520 | 415 | 504990 | -85.20 | 16.62 | 397.88 | 0.19 | 2.15 | 1593 |
| 2024-09-20 22:21:32.380 | MS1 | 121.4656766103 | 31.1446352726 | 415 | 504990 | -87.58 | 16.43 | 545.06 | 0.03 | 2.12 | 1581 |
| 2024-09-20 22:21:33.994 | MS1 | 121.4656684747 | 31.1446237709 | 415 | 504990 | -91.70 | 13.12 | 486.84 | 0.00 | 2.47 | 1560 |
| 2024-09-20 22:21:34.900 | MS1 | 121.4656654363 | 31.1446368986 | 415 | 504990 | -91.81 | 17.79 | 86.26 | 0.65 | 2.30 | 502 |
| 2024-09-20 22:21:35.273 | MS1 | 121.4656668077 | 31.1446318766 | 415 | 504990 | -88.56 | 12.60 | 92.74 | 0.55 | 2.42 | 672 |
| 2024-09-20 22:21:36.437 | MS1 | 121.4656699685 | 31.1446304949 | 415 | 504990 | -86.12 | 14.21 | 90.50 | 0.54 | 2.40 | 512 |
| 2024-09-20 22:21:37.107 | MS1 | 121.4656602801 | 31.1446317572 | 415 | 504990 | -93.14 | 9.11 | 77.17 | 0.57 | 2.88 | 563 |
| 2024-09-20 22:21:38.936 | MS1 | 121.4656734796 | 31.1446292690 | 415 | 504990 | -89.31 | 12.55 | 77.47 | 0.64 | 2.63 | 615 |
| 2024-09-20 22:21:39.497 | MS1 | 121.4656597174 | 31.1446292280 | 415 | 504990 | -93.65 | 10.40 | 70.33 | 0.63 | 2.15 | 533 |
| 2024-09-20 22:21:40.797 | MS1 | 121.4656734753 | 31.1446205513 | 415 | 504990 | -90.59 | 11.54 | 403.14 | 0.00 | 2.44 | 1595 |
| 2024-09-20 22:21:41.680 | MS1 | 121.4656719003 | 31.1446327728 | 415 | 504990 | -93.63 | 9.11 | 457.36 | 0.05 | 2.22 | 1580 |
| 2024-09-20 22:21:42.960 | MS1 | 121.4656615001 | 31.1446302687 | 415 | 504990 | -91.40 | 12.07 | 360.27 | 0.11 | 2.42 | 1600 |

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
| 3241026 | 1 | 121.4748930295 | 31.1553924965 | 45 | 15 | 4 | 22.4 | TDD | 808 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3245056 | 2 | 121.4656447049 | 31.1525218550 | 148 | 9 | 2 | 44.6 | TDD | 20 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3252119 | 3 | 121.4721329978 | 31.1503625125 | 266 | 7 | 9 | 16.6 | TDD | 717 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3276059 | 4 | 121.4758120589 | 31.1552085429 | 219 | 2 | 12 | 18.2 | TDD | 415 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.003 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.019 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.129 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.129 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.838 | NREventA3 | measId:2;ServCellPCI:630;Se... |
| 2024-09-20 22:21:38.078 | NRHandoverAttempt | SourcePCI:630;SourceNR-ARFC... |
| 2024-09-20 22:21:38.125 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.137 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.253 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.253 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241026 | 1 | 19.9877 | 14.2943 | -117.6031 | 13.5341 | 98.5467 | 0.0118 | 0.0031 |
| 2024_09_20 22:00 | 3245056 | 2 | 13.4157 | 18.9467 | -117.3480 | 13.4457 | 147.5700 | 0.0143 | 0.0006 |
| 2024_09_20 22:00 | 3252119 | 3 | 9.1133 | 8.3621 | -114.6968 | 5.3977 | 155.5901 | 0.0068 | 0.0119 |
| 2024_09_20 22:00 | 3276059 | 4 | 15.1291 | 19.3909 | -114.4676 | 5.9508 | 132.1487 | 0.0057 | 0.0070 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415748_0EC678B6 | 504990 | 415 | -90.6 | 504990 | 808 | -101.3 | 504990 | 20 | -104.2 | 504990 | 717 |
| MR_1774415748_E94B2D0F | 504990 | 415 | -93.2 | 504990 | 808 | -98.6 | 504990 | 20 | -102.3 | 504990 | 717 |
| MR_1774415748_8334CE9F | 504990 | 415 | -90.1 | 504990 | 808 | -100.2 | 504990 | 20 | -104.5 | 504990 | 717 |
| MR_1774415748_E4ED2893 | 504990 | 415 | -91.6 | 504990 | 808 | -102.2 | 504990 | 20 | -103.1 | 504990 | 717 |
| MR_1774415748_71268F38 | 504990 | 415 | -92.4 | 504990 | 808 | -101.6 | 504990 | 20 | -104.6 | 504990 | 717 |
| MR_1774415748_1CDE7A2F | 504990 | 415 | -91.2 | 504990 | 808 | -100.9 | 504990 | 20 | -104.9 | 504990 | 717 |
| MR_1774415748_BE1A2D89 | 504990 | 415 | -92.9 | 504990 | 808 | -102.0 | 504990 | 20 | -104.0 | 504990 | 717 |
| MR_1774415748_194044D0 | 504990 | 415 | -91.9 | 504990 | 808 | -102.2 | 504990 | 20 | -101.8 | 504990 | 717 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1117: `c25349fa-ec0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c25349fa-ec0d-48ee-8433-71df15e81a88` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Add neighbor relationship between 3261746_1 and 3217793_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1117] topology](images/train_1117.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217793_2
- `C2`: Increase transmission power for 3261746_1
- `C3`: Press down the tilt angle of 3261746_1 by 10 degrees
- `C4`: Check test server and transmission issues
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease transmission power for 3261746_1
- `C7`: Increase transmission power for 3217793_2
- `C8`: Add neighbor relationship between 3271555_4 and 3217793_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261746_1
- `C10`: Decrease transmission power for 3217793_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261746_1
- `C12`: Increase A3 Offset threshold for 3217793_2
- `C13`: Decrease A3 Offset threshold for 3261746_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217793_2
- `C15`: Lift the tilt angle of 3261746_1 by 10 degrees
- `C16`: Add neighbor relationship between 3261746_1 and 3217793_2 **← 정답**
- `C17`: Adjust the azimuth of 3217793_2 by 5 degrees
- `C18`: Adjust the azimuth of 3261746_1 by 35 degrees
- `C19`: Press down the tilt angle  of 3217793_2 by 5 degrees
- `C20`: Increase A3 Offset threshold for 3261746_1
- `C21`: Lift the tilt angle  of 3217793_2 by 5 degrees
- `C22`: Decrease A3 Offset threshold for 3217793_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.583 | MS1 | 121.4656693982 | 31.1446296473 | 176 | 504990 | -82.69 | 13.72 | 446.80 | 0.18 | 2.55 | 1567 |
| 2024-09-20 22:21:32.605 | MS1 | 121.4656646164 | 31.1446190192 | 176 | 504990 | -75.48 | 16.73 | 514.81 | 0.06 | 2.71 | 1580 |
| 2024-09-20 22:21:33.818 | MS1 | 121.4656690113 | 31.1446339137 | 176 | 504990 | -83.80 | 15.07 | 534.02 | 0.07 | 2.01 | 1599 |
| 2024-09-20 22:21:34.383 | MS1 | 121.4656696885 | 31.1446233810 | 176 | 504990 | -88.74 | -1.90 | 33.27 | 0.18 | 1.38 | 1596 |
| 2024-09-20 22:21:35.135 | MS1 | 121.4656726450 | 31.1446215397 | 176 | 504990 | -90.17 | -1.33 | 28.60 | 0.15 | 1.50 | 1563 |
| 2024-09-20 22:21:36.354 | MS1 | 121.4656663715 | 31.1446295742 | 176 | 504990 | -91.01 | -1.49 | 27.05 | 0.13 | 1.15 | 1580 |
| 2024-09-20 22:21:37.272 | MS1 | 121.4656596239 | 31.1446230331 | 176 | 504990 | -88.61 | -0.67 | 39.48 | 0.13 | 1.28 | 1565 |
| 2024-09-20 22:21:38.944 | MS1 | 121.4656771465 | 31.1446190206 | 176 | 504990 | -82.25 | 15.63 | 399.28 | 0.10 | 1.11 | 1567 |
| 2024-09-20 22:21:39.232 | MS1 | 121.4656618237 | 31.1446254062 | 176 | 504990 | -79.94 | 12.11 | 453.90 | 0.16 | 1.21 | 1576 |
| 2024-09-20 22:21:40.162 | MS1 | 121.4656645349 | 31.1446198238 | 176 | 504990 | -81.47 | 15.65 | 485.22 | 0.17 | 2.85 | 1599 |
| 2024-09-20 22:21:41.938 | MS1 | 121.4656698178 | 31.1446297499 | 176 | 504990 | -79.03 | 15.94 | 337.01 | 0.07 | 2.24 | 1581 |
| 2024-09-20 22:21:42.389 | MS1 | 121.4656774346 | 31.1446280141 | 176 | 504990 | -83.71 | 14.74 | 300.12 | 0.03 | 2.41 | 1575 |

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
| 3217793 | 2 | 121.4729650206 | 31.1528389547 | 222 | 3 | 7 | 35.8 | TDD | 272 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3261746 | 1 | 121.4717822745 | 31.1490304610 | 265 | 11 | 4 | 43.6 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3261972 | 3 | 121.4687290129 | 31.1480831686 | 218 | 15 | 8 | 31.5 | TDD | 182 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3271555 | 4 | 121.4652950054 | 31.1521161748 | 279 | 15 | 3 | 26.4 | TDD | 487 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.184 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.209 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.342 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.342 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.069 | NREventA3 | measId:2;ServCellPCI:671;Se... |
| 2024-09-20 22:21:36.069 | NREventA3 | measId:2;ServCellPCI:671;Se... |
| 2024-09-20 22:21:37.069 | NREventA3 | measId:2;ServCellPCI:671;Se... |
| 2024-09-20 22:21:39.569 | NRRRCReestablishAttempt | PCI:671 |
| 2024-09-20 22:21:39.583 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.593 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.742 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.742 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261746 | 1 | 18.6588 | 9.9713 | -115.3274 | 15.1493 | 151.4387 | 0.0191 | 0.1826 |
| 2024_09_20 22:00 | 3217793 | 2 | 8.0645 | 19.6476 | -114.4995 | 8.3813 | 185.2376 | 0.0010 | 0.0045 |
| 2024_09_20 22:00 | 3261972 | 3 | 16.0620 | 16.5381 | -114.0811 | 15.5949 | 184.5346 | 0.0098 | 0.0002 |
| 2024_09_20 22:00 | 3271555 | 4 | 8.6946 | 16.9816 | -117.5830 | 17.1696 | 170.7584 | 0.0025 | 0.0041 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416005_7694BD60 | 504990 | 176 | -87.4 | 504990 | 272 | -81.5 | 504990 | 487 | -87.2 | 504990 | 182 |
| MR_1774416005_2B986D56 | 504990 | 272 | -84.0 | 504990 | 176 | -88.8 | 504990 | 487 | -84.7 | 504990 | 182 |
| MR_1774416005_EB416971 | 504990 | 176 | -89.9 | 504990 | 272 | -84.6 | 504990 | 487 | -85.7 | 504990 | 182 |
| MR_1774416005_6DFE6840 | 504990 | 176 | -90.6 | 504990 | 272 | -82.1 | 504990 | 487 | -84.7 | 504990 | 182 |
| MR_1774416005_052CADBA | 504990 | 176 | -87.4 | 504990 | 272 | -82.7 | 504990 | 487 | -85.7 | 504990 | 182 |
| MR_1774416005_764A7E86 | 504990 | 272 | -81.9 | 504990 | 176 | -87.4 | 504990 | 487 | -84.1 | 504990 | 182 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1118: `237e2555-c5c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `237e2555-c5c1-4004-83e4-1d91e179d737` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Add neighbor relationship between 3220086_3 and 3246375_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1118] topology](images/train_1118.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3246375_2
- `C2`: Add neighbor relationship between 3220086_3 and 3246375_2 **← 정답**
- `C3`: Adjust the azimuth of 3220086_3 by 36 degrees
- `C4`: Decrease transmission power for 3220086_3
- `C5`: Increase transmission power for 3220086_3
- `C6`: Press down the tilt angle  of 3246375_2 by 4 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246375_2
- `C8`: Increase A3 Offset threshold for 3246375_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220086_3
- `C10`: Check test server and transmission issues
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220086_3
- `C12`: Lift the tilt angle of 3220086_3 by 9 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246375_2
- `C14`: Add neighbor relationship between 3279208_4 and 3246375_2
- `C15`: Lift the tilt angle  of 3246375_2 by 4 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease A3 Offset threshold for 3246375_2
- `C18`: Press down the tilt angle of 3220086_3 by 9 degrees
- `C19`: Adjust the azimuth of 3246375_2 by 20 degrees
- `C20`: Decrease A3 Offset threshold for 3220086_3
- `C21`: Increase A3 Offset threshold for 3220086_3
- `C22`: Increase transmission power for 3246375_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.977 | MS1 | 121.4656629817 | 31.1446367597 | 805 | 504990 | -79.81 | 14.49 | 363.10 | 0.07 | 2.39 | 1560 |
| 2024-09-20 22:21:32.162 | MS1 | 121.4656716729 | 31.1446277239 | 805 | 504990 | -76.17 | 15.48 | 483.71 | 0.04 | 2.19 | 1592 |
| 2024-09-20 22:21:33.124 | MS1 | 121.4656609977 | 31.1446370763 | 805 | 504990 | -82.19 | 12.44 | 463.55 | 0.05 | 2.94 | 1570 |
| 2024-09-20 22:21:34.389 | MS1 | 121.4656704331 | 31.1446363004 | 805 | 504990 | -91.79 | -0.13 | 72.07 | 0.08 | 1.05 | 1566 |
| 2024-09-20 22:21:35.869 | MS1 | 121.4656636179 | 31.1446203784 | 805 | 504990 | -94.29 | -1.81 | 35.48 | 0.09 | 1.16 | 1578 |
| 2024-09-20 22:21:36.807 | MS1 | 121.4656654255 | 31.1446239176 | 805 | 504990 | -93.58 | -3.95 | 42.11 | 0.09 | 1.13 | 1581 |
| 2024-09-20 22:21:37.357 | MS1 | 121.4656723479 | 31.1446180996 | 805 | 504990 | -89.92 | -0.55 | 39.78 | 0.05 | 1.19 | 1583 |
| 2024-09-20 22:21:38.248 | MS1 | 121.4656710807 | 31.1446306479 | 805 | 504990 | -78.17 | 17.71 | 561.38 | 0.13 | 1.50 | 1598 |
| 2024-09-20 22:21:39.107 | MS1 | 121.4656588562 | 31.1446276812 | 805 | 504990 | -75.74 | 13.10 | 452.24 | 0.01 | 1.05 | 1584 |
| 2024-09-20 22:21:40.253 | MS1 | 121.4656627936 | 31.1446343493 | 805 | 504990 | -77.67 | 15.37 | 492.21 | 0.11 | 2.30 | 1578 |
| 2024-09-20 22:21:41.128 | MS1 | 121.4656666656 | 31.1446260903 | 805 | 504990 | -83.22 | 14.45 | 314.52 | 0.19 | 2.64 | 1586 |
| 2024-09-20 22:21:42.955 | MS1 | 121.4656753736 | 31.1446229317 | 805 | 504990 | -82.04 | 13.41 | 436.42 | 0.06 | 2.30 | 1585 |

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
| 3220086 | 3 | 121.4725608125 | 31.1483319085 | 202 | 7 | 6 | 25.0 | TDD | 805 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3246375 | 2 | 121.4646656829 | 31.1532122647 | 154 | 2 | 7 | 25.4 | TDD | 539 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3265592 | 1 | 121.4650360439 | 31.1522378844 | 307 | 13 | 7 | 27.9 | TDD | 802 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3279208 | 4 | 121.4748739820 | 31.1503537211 | 294 | 4 | 11 | 25.7 | TDD | 703 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.029 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.052 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.182 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.182 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.910 | NREventA3 | measId:2;ServCellPCI:165;Se... |
| 2024-09-20 22:21:35.910 | NREventA3 | measId:2;ServCellPCI:165;Se... |
| 2024-09-20 22:21:36.910 | NREventA3 | measId:2;ServCellPCI:165;Se... |
| 2024-09-20 22:21:39.410 | NRRRCReestablishAttempt | PCI:165 |
| 2024-09-20 22:21:39.420 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.434 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.563 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.563 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265592 | 1 | 18.6827 | 9.8895 | -116.3680 | 9.0198 | 90.4123 | 0.0165 | 0.0116 |
| 2024_09_20 22:00 | 3246375 | 2 | 6.5766 | 15.2941 | -117.7690 | 18.0937 | 131.2050 | 0.0033 | 0.0173 |
| 2024_09_20 22:00 | 3220086 | 3 | 9.1915 | 14.6814 | -115.5413 | 15.6341 | 82.1106 | 0.0189 | 0.1196 |
| 2024_09_20 22:00 | 3279208 | 4 | 7.8274 | 9.0719 | -114.3577 | 15.4500 | 106.3823 | 0.0157 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414879_1A118208 | 504990 | 539 | -85.3 | 504990 | 805 | -90.1 | 504990 | 703 | -89.7 | 504990 | 802 |
| MR_1774414879_B64A67EF | 504990 | 805 | -90.7 | 504990 | 539 | -85.2 | 504990 | 703 | -90.0 | 504990 | 802 |
| MR_1774414879_3304DA23 | 504990 | 539 | -86.7 | 504990 | 805 | -92.2 | 504990 | 703 | -89.1 | 504990 | 802 |
| MR_1774414879_1A676C52 | 504990 | 805 | -91.6 | 504990 | 539 | -85.3 | 504990 | 703 | -90.1 | 504990 | 802 |
| MR_1774414879_B03D98E4 | 504990 | 805 | -91.7 | 504990 | 539 | -88.1 | 504990 | 703 | -90.4 | 504990 | 802 |
| MR_1774414879_403474D9 | 504990 | 805 | -92.1 | 504990 | 539 | -86.9 | 504990 | 703 | -89.6 | 504990 | 802 |
| MR_1774414879_1E01855A | 504990 | 539 | -87.6 | 504990 | 805 | -90.7 | 504990 | 703 | -90.1 | 504990 | 802 |
| MR_1774414879_CFC6A9D4 | 504990 | 805 | -93.6 | 504990 | 539 | -86.3 | 504990 | 703 | -91.2 | 504990 | 802 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1119: `fea290cb-1c8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fea290cb-1c8a-4fff-b742-210106b7273c` |
| Tag | **multiple-answer** |
| 정답 | **C3|C14** |
| C3 의미 | Adjust the azimuth of 3268910_2 by 50 degrees |
| C14 의미 | Increase transmission power for 3268910_2 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1119] topology](images/train_1119.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229279_3
- `C2`: Decrease transmission power for 3268910_2
- `C3`: Adjust the azimuth of 3268910_2 by 50 degrees **← 정답**
- `C4`: Increase transmission power for 3229279_3
- `C5`: Press down the tilt angle of 3268910_2 by 3 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268910_2
- `C7`: Decrease transmission power for 3229279_3
- `C8`: Adjust the azimuth of 3229279_3 by 38 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229279_3
- `C10`: Decrease A3 Offset threshold for 3229279_3
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Lift the tilt angle of 3268910_2 by 3 degrees
- `C13`: Lift the tilt angle  of 3229279_3 by 4 degrees
- `C14`: Increase transmission power for 3268910_2 **← 정답**
- `C15`: Add neighbor relationship between 3268910_2 and 3229279_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268910_2
- `C17`: Press down the tilt angle  of 3229279_3 by 4 degrees
- `C18`: Increase A3 Offset threshold for 3268910_2
- `C19`: Check test server and transmission issues
- `C20`: Decrease A3 Offset threshold for 3268910_2
- `C21`: Increase A3 Offset threshold for 3229279_3
- `C22`: Add neighbor relationship between 3271057_4 and 3229279_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.602 | MS1 | 121.4656698025 | 31.1446311193 | 1003 | 504990 | -91.81 | 15.40 | 300.71 | 0.09 | 2.12 | 1583 |
| 2024-09-20 22:21:32.419 | MS1 | 121.4656627285 | 31.1446268747 | 1003 | 504990 | -86.61 | 13.63 | 594.20 | 0.11 | 2.42 | 1565 |
| 2024-09-20 22:21:33.680 | MS1 | 121.4656766391 | 31.1446332396 | 1003 | 504990 | -88.21 | 13.60 | 438.77 | 0.11 | 2.30 | 1576 |
| 2024-09-20 22:21:34.725 | MS1 | 121.4656739709 | 31.1446183220 | 1003 | 504990 | -108.52 | 0.28 | 22.60 | 0.04 | 1.07 | 1581 |
| 2024-09-20 22:21:35.640 | MS1 | 121.4656750069 | 31.1446245830 | 1003 | 504990 | -106.60 | -1.61 | 21.23 | 0.17 | 1.33 | 1561 |
| 2024-09-20 22:21:36.151 | MS1 | 121.4656729723 | 31.1446281267 | 1003 | 504990 | -104.33 | -0.97 | 37.30 | 0.19 | 1.23 | 1562 |
| 2024-09-20 22:21:37.333 | MS1 | 121.4656707906 | 31.1446342393 | 1003 | 504990 | -108.18 | -1.84 | 48.24 | 0.14 | 1.20 | 1566 |
| 2024-09-20 22:21:38.469 | MS1 | 121.4656714846 | 31.1446210175 | 1003 | 504990 | -108.43 | 1.82 | 63.09 | 0.12 | 1.27 | 1599 |
| 2024-09-20 22:21:39.209 | MS1 | 121.4656689290 | 31.1446234689 | 1003 | 504990 | -105.21 | -0.15 | 60.05 | 0.02 | 1.32 | 1562 |
| 2024-09-20 22:21:40.372 | MS1 | 121.4656773261 | 31.1446245393 | 1003 | 504990 | -89.41 | 14.95 | 375.91 | 0.18 | 2.60 | 1562 |
| 2024-09-20 22:21:41.988 | MS1 | 121.4656766156 | 31.1446369295 | 1003 | 504990 | -85.13 | 13.69 | 493.91 | 0.02 | 2.28 | 1570 |
| 2024-09-20 22:21:42.511 | MS1 | 121.4656766449 | 31.1446362940 | 1003 | 504990 | -92.69 | 12.41 | 402.11 | 0.04 | 2.10 | 1579 |

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
| 3229279 | 3 | 121.4716009486 | 31.1474645697 | 279 | 1 | 12 | 29.6 | TDD | 541 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3268910 | 2 | 121.4701518602 | 31.1546263409 | 150 | 2 | 5 | 18.4 | TDD | 1003 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3270946 | 1 | 121.4682741597 | 31.1547805051 | 183 | 9 | 5 | 20.5 | TDD | 185 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3271057 | 4 | 121.4732085189 | 31.1529230489 | 153 | 9 | 1 | 15.1 | TDD | 727 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.418 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.438 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.587 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.587 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.794 | NREventA2 | measId:1;ServCellPCI:33;Ser... |
| 2024-09-20 22:21:34.926 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270946 | 1 | 15.8551 | 8.5330 | -115.7613 | 11.2393 | 171.1034 | 0.0147 | 0.0021 |
| 2024_09_20 22:00 | 3268910 | 2 | 11.9700 | 17.5957 | -116.4672 | 16.1980 | 107.6151 | 0.1621 | 0.0077 |
| 2024_09_20 22:00 | 3229279 | 3 | 15.6081 | 5.8896 | -115.2347 | 7.1288 | 186.7007 | 0.0144 | 0.0162 |
| 2024_09_20 22:00 | 3271057 | 4 | 19.5167 | 19.5888 | -115.2468 | 19.1827 | 187.4076 | 0.0195 | 0.0048 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414953_8F0E7F86 | 504990 | 1003 | -107.3 | 504990 | 541 | -112.4 | 504990 | 727 | -117.7 | 504990 | 185 |
| MR_1774414953_3DCE7ABF | 504990 | 1003 | -107.5 | 504990 | 541 | -112.8 | 504990 | 727 | -118.8 | 504990 | 185 |
| MR_1774414953_51353F66 | 504990 | 1003 | -110.1 | 504990 | 541 | -113.5 | 504990 | 727 | -118.1 | 504990 | 185 |
| MR_1774414953_1EA14F77 | 504990 | 1003 | -109.5 | 504990 | 541 | -112.2 | 504990 | 727 | -117.3 | 504990 | 185 |
| MR_1774414953_EC9BAC83 | 504990 | 1003 | -107.8 | 504990 | 541 | -110.6 | 504990 | 727 | -119.5 | 504990 | 185 |

> *... 2개 열 생략 (전체 14열)*

---
