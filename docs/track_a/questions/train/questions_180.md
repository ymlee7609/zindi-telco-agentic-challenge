# Track A 문제 분석 — train[1790]~train[1799]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1790] ~ train[1799] (10개)

## 목차

1. [문제 1790: `996097d2-751...`](#1790) — single-answer, 정답: C4
2. [문제 1791: `0f3bd4bd-000...`](#1791) — single-answer, 정답: C1
3. [문제 1792: `a9440d5b-ee5...`](#1792) — single-answer, 정답: C21
4. [문제 1793: `d6eece11-e1f...`](#1793) — single-answer, 정답: C10
5. [문제 1794: `fb927094-bdc...`](#1794) — single-answer, 정답: C21
6. [문제 1795: `dae5e223-b0e...`](#1795) — multiple-answer, 정답: C4|C9
7. [문제 1796: `e155f6ef-dac...`](#1796) — single-answer, 정답: C10
8. [문제 1797: `e35ecf6b-39a...`](#1797) — multiple-answer, 정답: C2|C3
9. [문제 1798: `18720a20-fda...`](#1798) — single-answer, 정답: C20
10. [문제 1799: `02b0c4d4-6b6...`](#1799) — single-answer, 정답: C7

---

### 문제 1790: `996097d2-751...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `996097d2-7519-4992-afa0-ee0539c8d509` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1790] topology](images/train_1790.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3244022_2
- `C2`: Adjust the azimuth of 3235004_4 by 34 degrees
- `C3`: Add neighbor relationship between 3246241_3 and 3244022_2
- `C4`: Insufficient data; more data is needed for judgment. **← 정답**
- `C5`: Check test server and transmission issues
- `C6`: Decrease transmission power for 3235004_4
- `C7`: Increase transmission power for 3244022_2
- `C8`: Increase transmission power for 3235004_4
- `C9`: Increase A3 Offset threshold for 3235004_4
- `C10`: Lift the tilt angle of 3235004_4 by 2 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235004_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244022_2
- `C13`: Adjust the azimuth of 3244022_2 by 50 degrees
- `C14`: Press down the tilt angle  of 3244022_2 by 2 degrees
- `C15`: Add neighbor relationship between 3235004_4 and 3244022_2
- `C16`: Press down the tilt angle of 3235004_4 by 2 degrees
- `C17`: Decrease transmission power for 3244022_2
- `C18`: Decrease A3 Offset threshold for 3244022_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244022_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235004_4
- `C21`: Decrease A3 Offset threshold for 3235004_4
- `C22`: Lift the tilt angle  of 3244022_2 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.508 | MS1 | 121.4656707710 | 31.1446305604 | 406 | 504990 | -91.53 | 14.73 | 489.32 | 0.17 | 2.87 | 1574 |
| 2024-09-20 22:21:32.476 | MS1 | 121.4656757657 | 31.1446215532 | 406 | 504990 | -87.94 | 14.06 | 425.42 | 0.05 | 2.80 | 1586 |
| 2024-09-20 22:21:33.436 | MS1 | 121.4656660623 | 31.1446218738 | 406 | 504990 | -87.54 | 16.22 | 396.26 | 0.14 | 2.10 | 1591 |
| 2024-09-20 22:21:34.551 | MS1 | 121.4656675162 | 31.1446283590 | 406 | 504990 | -90.85 | 15.18 | 77.85 | 0.15 | 2.72 | 1578 |
| 2024-09-20 22:21:35.959 | MS1 | 121.4656710698 | 31.1446315671 | 406 | 504990 | -91.10 | 16.05 | 68.95 | 0.02 | 2.59 | 1571 |
| 2024-09-20 22:21:36.417 | MS1 | 121.4656718503 | 31.1446305496 | 406 | 504990 | -86.35 | 17.78 | 81.90 | 0.18 | 2.55 | 1589 |
| 2024-09-20 22:21:37.457 | MS1 | 121.4656593689 | 31.1446201390 | 406 | 504990 | -91.13 | 12.39 | 82.65 | 0.08 | 2.90 | 1577 |
| 2024-09-20 22:21:38.884 | MS1 | 121.4656718351 | 31.1446279590 | 406 | 504990 | -92.68 | 8.52 | 97.78 | 0.17 | 2.42 | 1576 |
| 2024-09-20 22:21:39.229 | MS1 | 121.4656674632 | 31.1446253022 | 406 | 504990 | -90.84 | 10.77 | 92.56 | 0.06 | 2.66 | 1560 |
| 2024-09-20 22:21:40.351 | MS1 | 121.4656622861 | 31.1446351937 | 406 | 504990 | -91.21 | 7.84 | 448.41 | 0.12 | 2.78 | 1580 |
| 2024-09-20 22:21:41.532 | MS1 | 121.4656662725 | 31.1446245326 | 406 | 504990 | -89.21 | 9.27 | 309.14 | 0.15 | 2.91 | 1585 |
| 2024-09-20 22:21:42.541 | MS1 | 121.4656755320 | 31.1446360977 | 406 | 504990 | -90.73 | 8.72 | 321.29 | 0.17 | 2.71 | 1593 |

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
| 3235004 | 4 | 121.4726868221 | 31.1541778265 | 178 | 1 | 0 | 23.3 | TDD | 406 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3244022 | 2 | 121.4743183338 | 31.1481627488 | 66 | 1 | 7 | 22.4 | TDD | 59 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3246241 | 3 | 121.4716545593 | 31.1542213348 | 103 | 1 | 0 | 41.0 | TDD | 524 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3268311 | 1 | 121.4665702266 | 31.1467559626 | 282 | 0 | 9 | 45.7 | TDD | 952 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.032 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.047 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.161 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.161 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.910 | NREventA3 | measId:2;ServCellPCI:606;Se... |
| 2024-09-20 22:21:38.150 | NRHandoverAttempt | SourcePCI:606;SourceNR-ARFC... |
| 2024-09-20 22:21:38.196 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.210 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.350 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.350 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3268311 | 1 | 85.2626 | 86.4665 | -116.3306 | 11.1377 | 195.8711 | 0.0030 | 0.0166 |
| 2024_09_19 22:00 | 3244022 | 2 | 94.8769 | 86.1319 | -116.4309 | 17.1092 | 99.7798 | 0.0132 | 0.0181 |
| 2024_09_19 22:00 | 3246241 | 3 | 85.3242 | 88.0093 | -114.3660 | 7.5680 | 165.8569 | 0.0008 | 0.0098 |
| 2024_09_19 22:00 | 3235004 | 4 | 94.8504 | 92.4348 | -115.9556 | 5.4575 | 103.5859 | 0.0096 | 0.0091 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412520_114C1B36 | 504990 | 406 | -89.6 | 504990 | 59 | -92.2 | 504990 | 524 | -98.8 | 504990 | 952 |
| MR_1774412520_A0B89538 | 504990 | 406 | -89.7 | 504990 | 59 | -92.2 | 504990 | 524 | -98.0 | 504990 | 952 |
| MR_1774412520_52D92B45 | 504990 | 406 | -90.6 | 504990 | 59 | -91.4 | 504990 | 524 | -99.1 | 504990 | 952 |
| MR_1774412520_853F8C82 | 504990 | 406 | -88.9 | 504990 | 59 | -91.0 | 504990 | 524 | -100.7 | 504990 | 952 |
| MR_1774412520_029FDAE5 | 504990 | 406 | -89.3 | 504990 | 59 | -91.0 | 504990 | 524 | -101.1 | 504990 | 952 |
| MR_1774412520_F0E5C096 | 504990 | 406 | -91.7 | 504990 | 59 | -90.6 | 504990 | 524 | -98.9 | 504990 | 952 |
| MR_1774412520_7CE84A36 | 504990 | 406 | -91.3 | 504990 | 59 | -90.4 | 504990 | 524 | -101.5 | 504990 | 952 |
| MR_1774412520_F0DC7032 | 504990 | 406 | -92.7 | 504990 | 59 | -91.1 | 504990 | 524 | -100.2 | 504990 | 952 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1791: `0f3bd4bd-000...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0f3bd4bd-000a-41d4-8074-18025176f7b4` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3236764_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1791] topology](images/train_1791.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236764_1 **← 정답**
- `C2`: Increase A3 Offset threshold for 3227756_2
- `C3`: Adjust the azimuth of 3227756_2 by 50 degrees
- `C4`: Decrease transmission power for 3236764_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227756_2
- `C6`: Decrease A3 Offset threshold for 3227756_2
- `C7`: Lift the tilt angle of 3236764_1 by 3 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase transmission power for 3227756_2
- `C10`: Add neighbor relationship between 3236764_1 and 3227756_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236764_1
- `C12`: Press down the tilt angle  of 3227756_2 by 7 degrees
- `C13`: Lift the tilt angle  of 3227756_2 by 7 degrees
- `C14`: Press down the tilt angle of 3236764_1 by 3 degrees
- `C15`: Decrease transmission power for 3227756_2
- `C16`: Decrease A3 Offset threshold for 3236764_1
- `C17`: Add neighbor relationship between 3210343_3 and 3227756_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227756_2
- `C19`: Check test server and transmission issues
- `C20`: Increase transmission power for 3236764_1
- `C21`: Adjust the azimuth of 3236764_1 by 21 degrees
- `C22`: Increase A3 Offset threshold for 3236764_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.288 | MS1 | 121.4656663679 | 31.1446275083 | 296 | 504990 | -88.27 | 13.24 | 406.89 | 0.20 | 2.46 | 1599 |
| 2024-09-20 22:21:32.613 | MS1 | 121.4656612619 | 31.1446285418 | 296 | 504990 | -86.57 | 15.64 | 407.71 | 0.20 | 2.04 | 1574 |
| 2024-09-20 22:21:33.150 | MS1 | 121.4656708472 | 31.1446375513 | 296 | 504990 | -88.29 | 15.72 | 447.02 | 0.14 | 2.84 | 1560 |
| 2024-09-20 22:21:34.637 | MS1 | 121.4656666194 | 31.1446283479 | 296 | 504990 | -90.27 | 13.38 | 72.51 | 0.61 | 2.98 | 598 |
| 2024-09-20 22:21:35.970 | MS1 | 121.4656659557 | 31.1446210974 | 296 | 504990 | -87.11 | 13.43 | 58.69 | 0.54 | 2.13 | 649 |
| 2024-09-20 22:21:36.263 | MS1 | 121.4656762018 | 31.1446187623 | 296 | 504990 | -87.07 | 12.60 | 64.54 | 0.66 | 2.99 | 698 |
| 2024-09-20 22:21:37.606 | MS1 | 121.4656593287 | 31.1446196315 | 296 | 504990 | -93.61 | 9.12 | 70.16 | 0.51 | 2.13 | 601 |
| 2024-09-20 22:21:38.995 | MS1 | 121.4656643747 | 31.1446207090 | 296 | 504990 | -92.36 | 11.50 | 85.30 | 0.58 | 2.35 | 534 |
| 2024-09-20 22:21:39.496 | MS1 | 121.4656773783 | 31.1446231212 | 296 | 504990 | -93.21 | 11.53 | 89.47 | 0.53 | 2.57 | 604 |
| 2024-09-20 22:21:40.525 | MS1 | 121.4656587054 | 31.1446310312 | 296 | 504990 | -90.45 | 7.69 | 556.88 | 0.19 | 2.44 | 1597 |
| 2024-09-20 22:21:41.629 | MS1 | 121.4656743692 | 31.1446340026 | 296 | 504990 | -92.28 | 12.15 | 572.67 | 0.16 | 2.70 | 1565 |
| 2024-09-20 22:21:42.105 | MS1 | 121.4656624593 | 31.1446363449 | 296 | 504990 | -92.72 | 10.09 | 493.55 | 0.09 | 2.70 | 1582 |

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
| 3210343 | 3 | 121.4744562298 | 31.1546693681 | 70 | 13 | 11 | 27.3 | TDD | 408 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3227756 | 2 | 121.4730581301 | 31.1512549806 | 13 | 6 | 4 | 24.5 | TDD | 232 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3236764 | 1 | 121.4721626116 | 31.1556268028 | 186 | 2 | 5 | 35.0 | TDD | 296 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3238147 | 4 | 121.4662298569 | 31.1447642527 | 317 | 8 | 1 | 18.8 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.514 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.533 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.634 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.634 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.379 | NREventA3 | measId:2;ServCellPCI:298;Se... |
| 2024-09-20 22:21:38.619 | NRHandoverAttempt | SourcePCI:298;SourceNR-ARFC... |
| 2024-09-20 22:21:38.649 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.663 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.791 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.791 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236764 | 1 | 11.8393 | 9.5059 | -115.4359 | 18.8955 | 114.4063 | 0.0033 | 0.0075 |
| 2024_09_20 22:00 | 3227756 | 2 | 16.6618 | 11.3776 | -116.1483 | 19.4754 | 181.1811 | 0.0096 | 0.0054 |
| 2024_09_20 22:00 | 3210343 | 3 | 11.9477 | 19.0451 | -115.1116 | 14.9294 | 93.0542 | 0.0027 | 0.0094 |
| 2024_09_20 22:00 | 3238147 | 4 | 13.6272 | 19.6093 | -117.3402 | 17.6056 | 88.4611 | 0.0069 | 0.0067 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416331_5EA7709E | 504990 | 296 | -92.0 | 504990 | 232 | -95.5 | 504990 | 408 | -100.8 | 504990 | 176 |
| MR_1774416331_7C03454F | 504990 | 296 | -90.4 | 504990 | 232 | -99.2 | 504990 | 408 | -99.8 | 504990 | 176 |
| MR_1774416331_8568ED56 | 504990 | 296 | -88.7 | 504990 | 232 | -98.3 | 504990 | 408 | -100.3 | 504990 | 176 |
| MR_1774416331_8F5B4D58 | 504990 | 296 | -90.1 | 504990 | 232 | -98.0 | 504990 | 408 | -98.2 | 504990 | 176 |
| MR_1774416331_D896CDB4 | 504990 | 296 | -88.5 | 504990 | 232 | -97.8 | 504990 | 408 | -98.9 | 504990 | 176 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1792: `a9440d5b-ee5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a9440d5b-ee5c-42aa-ab48-5df5ca8e8e6a` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1792] topology](images/train_1792.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3230417_1 by 10 degrees
- `C2`: Decrease A3 Offset threshold for 3230417_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230417_1
- `C4`: Increase transmission power for 3233240_3
- `C5`: Increase A3 Offset threshold for 3233240_3
- `C6`: Decrease transmission power for 3230417_1
- `C7`: Adjust the azimuth of 3230417_1 by 37 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233240_3
- `C9`: Press down the tilt angle  of 3233240_3 by 4 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233240_3
- `C11`: Increase transmission power for 3230417_1
- `C12`: Decrease A3 Offset threshold for 3233240_3
- `C13`: Add neighbor relationship between 3250216_4 and 3233240_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230417_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Lift the tilt angle  of 3233240_3 by 4 degrees
- `C17`: Add neighbor relationship between 3230417_1 and 3233240_3
- `C18`: Decrease transmission power for 3233240_3
- `C19`: Press down the tilt angle of 3230417_1 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3230417_1
- `C21`: Check test server and transmission issues **← 정답**
- `C22`: Adjust the azimuth of 3233240_3 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.719 | MS1 | 121.4656597591 | 31.1446338676 | 973 | 504990 | -85.91 | 16.85 | 472.56 | 0.16 | 2.61 | 1589 |
| 2024-09-20 22:21:32.164 | MS1 | 121.4656615992 | 31.1446270554 | 973 | 504990 | -86.25 | 16.02 | 588.82 | 0.18 | 2.93 | 1596 |
| 2024-09-20 22:21:33.729 | MS1 | 121.4656632661 | 31.1446336605 | 973 | 504990 | -90.34 | 12.19 | 420.49 | 0.15 | 2.15 | 1569 |
| 2024-09-20 22:21:34.486 | MS1 | 121.4656610271 | 31.1446343452 | 973 | 504990 | -85.60 | 16.91 | 71.42 | 0.00 | 2.98 | 357 |
| 2024-09-20 22:21:35.335 | MS1 | 121.4656610790 | 31.1446322377 | 973 | 504990 | -88.22 | 17.89 | 67.20 | 0.12 | 2.37 | 330 |
| 2024-09-20 22:21:36.995 | MS1 | 121.4656591924 | 31.1446230229 | 973 | 504990 | -85.29 | 17.10 | 81.77 | 0.16 | 2.61 | 387 |
| 2024-09-20 22:21:37.950 | MS1 | 121.4656602386 | 31.1446379253 | 973 | 504990 | -91.21 | 12.09 | 59.24 | 0.13 | 2.46 | 442 |
| 2024-09-20 22:21:38.595 | MS1 | 121.4656703290 | 31.1446328085 | 973 | 504990 | -93.41 | 10.67 | 60.66 | 0.09 | 2.50 | 446 |
| 2024-09-20 22:21:39.143 | MS1 | 121.4656602515 | 31.1446366830 | 973 | 504990 | -91.54 | 7.95 | 89.90 | 0.18 | 2.28 | 364 |
| 2024-09-20 22:21:40.580 | MS1 | 121.4656670059 | 31.1446240630 | 973 | 504990 | -89.31 | 9.40 | 421.05 | 0.20 | 2.47 | 1571 |
| 2024-09-20 22:21:41.385 | MS1 | 121.4656581818 | 31.1446347842 | 973 | 504990 | -93.21 | 7.88 | 554.52 | 0.13 | 2.96 | 1560 |
| 2024-09-20 22:21:42.393 | MS1 | 121.4656709638 | 31.1446190847 | 973 | 504990 | -90.19 | 7.71 | 375.64 | 0.17 | 2.96 | 1571 |

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
| 3230417 | 1 | 121.4678447733 | 31.1472394322 | 253 | 13 | 11 | 19.1 | TDD | 973 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3233240 | 3 | 121.4713213697 | 31.1526247745 | 217 | 2 | 5 | 37.0 | TDD | 148 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3250216 | 4 | 121.4643886010 | 31.1440348610 | 338 | 10 | 3 | 44.4 | TDD | 797 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3258064 | 2 | 121.4659094579 | 31.1490434200 | 347 | 8 | 6 | 39.5 | TDD | 738 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.167 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.188 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.292 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.292 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.030 | NREventA3 | measId:2;ServCellPCI:831;Se... |
| 2024-09-20 22:21:38.270 | NRHandoverAttempt | SourcePCI:831;SourceNR-ARFC... |
| 2024-09-20 22:21:38.310 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.324 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.451 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.451 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230417 | 1 | 6.0171 | 16.8737 | -115.1846 | 18.6543 | 184.8229 | 0.0175 | 0.0075 |
| 2024_09_20 22:00 | 3258064 | 2 | 15.6032 | 13.5136 | -115.3179 | 9.5055 | 196.1529 | 0.0008 | 0.0151 |
| 2024_09_20 22:00 | 3233240 | 3 | 7.9326 | 6.9403 | -116.3902 | 16.4467 | 145.7653 | 0.0072 | 0.0082 |
| 2024_09_20 22:00 | 3250216 | 4 | 19.9991 | 11.9774 | -117.2460 | 11.8455 | 145.7229 | 0.0138 | 0.0036 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413608_55BC8518 | 504990 | 973 | -85.1 | 504990 | 148 | -91.7 | 504990 | 797 | -93.1 | 504990 | 738 |
| MR_1774413608_4FBB52CD | 504990 | 973 | -84.3 | 504990 | 148 | -92.5 | 504990 | 797 | -93.3 | 504990 | 738 |
| MR_1774413608_D5AF1ACE | 504990 | 973 | -84.6 | 504990 | 148 | -92.4 | 504990 | 797 | -92.6 | 504990 | 738 |
| MR_1774413608_7C096217 | 504990 | 973 | -86.1 | 504990 | 148 | -92.2 | 504990 | 797 | -90.1 | 504990 | 738 |
| MR_1774413608_4E3B574B | 504990 | 973 | -87.1 | 504990 | 148 | -90.5 | 504990 | 797 | -91.4 | 504990 | 738 |
| MR_1774413608_42B8D406 | 504990 | 973 | -84.7 | 504990 | 148 | -90.2 | 504990 | 797 | -91.3 | 504990 | 738 |
| MR_1774413608_C8636488 | 504990 | 973 | -84.2 | 504990 | 148 | -91.8 | 504990 | 797 | -91.2 | 504990 | 738 |
| MR_1774413608_5CB12147 | 504990 | 973 | -86.3 | 504990 | 148 | -93.8 | 504990 | 797 | -93.8 | 504990 | 738 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1793: `d6eece11-e1f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d6eece11-e1f6-432c-be6d-068ba5aa4fca` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Add neighbor relationship between 3239306_4 and 3210262_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1793] topology](images/train_1793.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3230128_1 and 3210262_2
- `C2`: Lift the tilt angle  of 3210262_2 by 2 degrees
- `C3`: Decrease transmission power for 3239306_4
- `C4`: Adjust the azimuth of 3210262_2 by 47 degrees
- `C5`: Check test server and transmission issues
- `C6`: Increase transmission power for 3210262_2
- `C7`: Adjust the azimuth of 3239306_4 by 50 degrees
- `C8`: Increase A3 Offset threshold for 3210262_2
- `C9`: Increase A3 Offset threshold for 3239306_4
- `C10`: Add neighbor relationship between 3239306_4 and 3210262_2 **← 정답**
- `C11`: Decrease transmission power for 3210262_2
- `C12`: Decrease A3 Offset threshold for 3210262_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239306_4
- `C14`: Decrease A3 Offset threshold for 3239306_4
- `C15`: Increase transmission power for 3239306_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239306_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210262_2
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210262_2
- `C20`: Press down the tilt angle  of 3210262_2 by 2 degrees
- `C21`: Press down the tilt angle of 3239306_4 by 10 degrees
- `C22`: Lift the tilt angle of 3239306_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.729 | MS1 | 121.4656623051 | 31.1446249027 | 757 | 504990 | -78.00 | 16.34 | 389.95 | 0.10 | 2.74 | 1593 |
| 2024-09-20 22:21:32.143 | MS1 | 121.4656637389 | 31.1446333906 | 757 | 504990 | -79.80 | 16.42 | 420.19 | 0.07 | 2.95 | 1572 |
| 2024-09-20 22:21:33.933 | MS1 | 121.4656695964 | 31.1446296991 | 757 | 504990 | -75.81 | 12.29 | 434.72 | 0.12 | 2.18 | 1582 |
| 2024-09-20 22:21:34.352 | MS1 | 121.4656657539 | 31.1446253964 | 757 | 504990 | -86.40 | -3.92 | 65.53 | 0.15 | 1.10 | 1587 |
| 2024-09-20 22:21:35.895 | MS1 | 121.4656588601 | 31.1446328784 | 757 | 504990 | -89.82 | -0.01 | 42.17 | 0.04 | 1.16 | 1589 |
| 2024-09-20 22:21:36.160 | MS1 | 121.4656589746 | 31.1446217561 | 757 | 504990 | -87.05 | -0.58 | 42.47 | 0.09 | 1.23 | 1599 |
| 2024-09-20 22:21:37.739 | MS1 | 121.4656689203 | 31.1446286267 | 757 | 504990 | -94.89 | -2.13 | 48.63 | 0.02 | 1.27 | 1587 |
| 2024-09-20 22:21:38.780 | MS1 | 121.4656667632 | 31.1446277775 | 757 | 504990 | -77.63 | 13.60 | 325.43 | 0.11 | 1.49 | 1588 |
| 2024-09-20 22:21:39.734 | MS1 | 121.4656645397 | 31.1446243895 | 757 | 504990 | -83.55 | 15.99 | 391.49 | 0.18 | 1.29 | 1597 |
| 2024-09-20 22:21:40.743 | MS1 | 121.4656653345 | 31.1446229686 | 757 | 504990 | -82.04 | 14.42 | 562.83 | 0.02 | 2.08 | 1593 |
| 2024-09-20 22:21:41.309 | MS1 | 121.4656721972 | 31.1446300650 | 757 | 504990 | -82.52 | 17.71 | 433.22 | 0.11 | 2.63 | 1599 |
| 2024-09-20 22:21:42.721 | MS1 | 121.4656613319 | 31.1446319131 | 757 | 504990 | -83.50 | 14.97 | 585.74 | 0.01 | 2.10 | 1589 |

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
| 3210262 | 2 | 121.4742597667 | 31.1502980490 | 279 | 0 | 12 | 33.4 | TDD | 11 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3214233 | 3 | 121.4701635027 | 31.1525227130 | 164 | 4 | 5 | 16.5 | TDD | 228 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3230128 | 1 | 121.4696916602 | 31.1480387729 | 72 | 13 | 11 | 43.2 | TDD | 280 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3239306 | 4 | 121.4746977165 | 31.1542684371 | 10 | 12 | 5 | 16.3 | TDD | 757 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.449 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.470 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.603 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.603 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.286 | NREventA3 | measId:2;ServCellPCI:981;Se... |
| 2024-09-20 22:21:36.286 | NREventA3 | measId:2;ServCellPCI:981;Se... |
| 2024-09-20 22:21:37.286 | NREventA3 | measId:2;ServCellPCI:981;Se... |
| 2024-09-20 22:21:39.786 | NRRRCReestablishAttempt | PCI:981 |
| 2024-09-20 22:21:39.806 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.820 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.944 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.944 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230128 | 1 | 15.1974 | 19.3713 | -114.4218 | 9.4124 | 92.6060 | 0.0177 | 0.0101 |
| 2024_09_20 22:00 | 3210262 | 2 | 9.1823 | 13.3910 | -115.9554 | 12.6796 | 182.1490 | 0.0101 | 0.0145 |
| 2024_09_20 22:00 | 3214233 | 3 | 17.5184 | 12.7829 | -115.6590 | 18.5017 | 129.3105 | 0.0172 | 0.0040 |
| 2024_09_20 22:00 | 3239306 | 4 | 19.7795 | 9.9404 | -114.0569 | 15.4730 | 113.6130 | 0.0191 | 0.1997 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415166_3B1EE3F3 | 504990 | 11 | -83.8 | 504990 | 757 | -85.3 | 504990 | 280 | -84.1 | 504990 | 228 |
| MR_1774415166_DD537C7F | 504990 | 757 | -87.2 | 504990 | 11 | -83.9 | 504990 | 280 | -86.2 | 504990 | 228 |
| MR_1774415166_AE7F9E60 | 504990 | 757 | -84.8 | 504990 | 11 | -82.2 | 504990 | 280 | -86.5 | 504990 | 228 |
| MR_1774415166_0270FCCA | 504990 | 757 | -85.6 | 504990 | 11 | -81.2 | 504990 | 280 | -87.3 | 504990 | 228 |
| MR_1774415166_4F3D62A6 | 504990 | 757 | -85.4 | 504990 | 11 | -80.9 | 504990 | 280 | -86.8 | 504990 | 228 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1794: `fb927094-bdc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fb927094-bdc3-415c-8a43-590e75356e0e` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Lift the tilt angle  of 3232425_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1794] topology](images/train_1794.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3235398_2
- `C2`: Increase transmission power for 3235398_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216642_4
- `C4`: Press down the tilt angle  of 3232425_1 by 10 degrees
- `C5`: Increase A3 Offset threshold for 3235398_2
- `C6`: Press down the tilt angle of 3216642_4 by 5 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235398_2
- `C8`: Decrease A3 Offset threshold for 3216642_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216642_4
- `C10`: Check test server and transmission issues
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235398_2
- `C12`: Add neighbor relationship between 3232425_1 and 3235398_2
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease A3 Offset threshold for 3235398_2
- `C15`: Decrease transmission power for 3216642_4
- `C16`: Increase transmission power for 3216642_4
- `C17`: Adjust the azimuth of 3232425_1 by 50 degrees
- `C18`: Add neighbor relationship between 3216642_4 and 3235398_2
- `C19`: Lift the tilt angle of 3216642_4 by 5 degrees
- `C20`: Increase A3 Offset threshold for 3216642_4
- `C21`: Lift the tilt angle  of 3232425_1 by 10 degrees **← 정답**
- `C22`: Adjust the azimuth of 3216642_4 by 18 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.180 | MS1 | 121.4656740555 | 31.1446335770 | 343 | 504990 | -89.68 | 15.52 | 317.66 | 0.17 | 2.20 | 1599 |
| 2024-09-20 22:21:32.250 | MS1 | 121.4656628236 | 31.1446224026 | 343 | 504990 | -90.95 | 12.49 | 397.27 | 0.03 | 2.27 | 1568 |
| 2024-09-20 22:21:33.563 | MS1 | 121.4656657665 | 31.1446376949 | 343 | 504990 | -85.19 | 17.31 | 311.81 | 0.11 | 2.64 | 1588 |
| 2024-09-20 22:21:34.967 | MS1 | 121.4656613106 | 31.1446323390 | 343 | 504990 | -89.19 | 14.50 | 59.66 | 0.13 | 2.51 | 1599 |
| 2024-09-20 22:21:35.387 | MS1 | 121.4656617668 | 31.1446316275 | 343 | 504990 | -91.34 | 12.24 | 73.52 | 0.01 | 2.18 | 1589 |
| 2024-09-20 22:21:36.221 | MS1 | 121.4656669907 | 31.1446196234 | 343 | 504990 | -91.97 | 14.67 | 71.48 | 0.04 | 2.72 | 1571 |
| 2024-09-20 22:21:37.581 | MS1 | 121.4656671159 | 31.1446214257 | 343 | 504990 | -89.36 | 10.28 | 82.37 | 0.07 | 2.31 | 1589 |
| 2024-09-20 22:21:38.667 | MS1 | 121.4656667174 | 31.1446309316 | 343 | 504990 | -92.32 | 10.18 | 59.98 | 0.09 | 2.99 | 1564 |
| 2024-09-20 22:21:39.401 | MS1 | 121.4656640787 | 31.1446374569 | 343 | 504990 | -93.38 | 11.06 | 93.09 | 0.04 | 2.46 | 1581 |
| 2024-09-20 22:21:40.545 | MS1 | 121.4656747141 | 31.1446286596 | 343 | 504990 | -90.03 | 12.45 | 365.18 | 0.01 | 2.57 | 1579 |
| 2024-09-20 22:21:41.854 | MS1 | 121.4656610238 | 31.1446205815 | 343 | 504990 | -89.33 | 9.08 | 304.64 | 0.05 | 2.78 | 1582 |
| 2024-09-20 22:21:42.399 | MS1 | 121.4656727062 | 31.1446360797 | 343 | 504990 | -93.12 | 12.58 | 409.09 | 0.18 | 2.91 | 1586 |

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
| 3216642 | 4 | 121.4758527507 | 31.1486176915 | 227 | 2 | 2 | 47.7 | TDD | 343 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3232425 | 1 | 121.4717236124 | 31.1554209016 | 79 | 12 | 10 | 35.3 | TDD | 216 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3235398 | 2 | 121.4723544893 | 31.1557698921 | 346 | 10 | 6 | 32.0 | TDD | 641 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3262831 | 3 | 121.4656898455 | 31.1537835530 | 147 | 3 | 3 | 26.2 | TDD | 923 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.104 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.121 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.247 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.247 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.990 | NREventA3 | measId:2;ServCellPCI:579;Se... |
| 2024-09-20 22:21:38.230 | NRHandoverAttempt | SourcePCI:579;SourceNR-ARFC... |
| 2024-09-20 22:21:38.274 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.286 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.386 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.386 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232425 | 1 | 10.8822 | 12.8865 | -114.0807 | 10.2634 | 92.6694 | 0.0150 | 0.0071 |
| 2024_09_20 22:00 | 3235398 | 2 | 16.3176 | 17.3356 | -114.3397 | 14.5106 | 172.9168 | 0.0152 | 0.0161 |
| 2024_09_20 22:00 | 3262831 | 3 | 10.2850 | 16.5591 | -116.9846 | 14.2893 | 88.3964 | 0.0198 | 0.0174 |
| 2024_09_20 22:00 | 3216642 | 4 | 94.3035 | 78.0916 | -115.3270 | 7.8982 | 112.8971 | 0.0031 | 0.0200 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416394_6B33D9C8 | 504990 | 343 | -87.7 | 504990 | 641 | -88.6 | 504990 | 216 | -100.4 | 504990 | 923 |
| MR_1774416394_7D9C80B4 | 504990 | 343 | -87.9 | 504990 | 641 | -89.2 | 504990 | 216 | -100.2 | 504990 | 923 |
| MR_1774416394_83E5FE22 | 504990 | 343 | -88.4 | 504990 | 641 | -91.8 | 504990 | 216 | -102.8 | 504990 | 923 |
| MR_1774416394_0EB8B4F2 | 504990 | 343 | -88.2 | 504990 | 641 | -92.1 | 504990 | 216 | -102.3 | 504990 | 923 |
| MR_1774416394_8884587A | 504990 | 343 | -90.2 | 504990 | 641 | -89.5 | 504990 | 216 | -100.1 | 504990 | 923 |
| MR_1774416394_5D1DABC3 | 504990 | 343 | -90.8 | 504990 | 641 | -90.6 | 504990 | 216 | -101.6 | 504990 | 923 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1795: `dae5e223-b0e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dae5e223-b0e2-4f24-83b0-c963136e7f2b` |
| Tag | **multiple-answer** |
| 정답 | **C4|C9** |
| C4 의미 | Decrease transmission power for 3234854_3 |
| C9 의미 | Press down the tilt angle  of 3234854_3 by 4 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1795] topology](images/train_1795.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease transmission power for 3246026_1
- `C3`: Adjust the azimuth of 3234854_3 by 27 degrees
- `C4`: Decrease transmission power for 3234854_3 **← 정답**
- `C5`: Increase A3 Offset threshold for 3246026_1
- `C6`: Decrease A3 Offset threshold for 3234854_3
- `C7`: Lift the tilt angle  of 3234854_3 by 4 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Press down the tilt angle  of 3234854_3 by 4 degrees **← 정답**
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234854_3
- `C11`: Add neighbor relationship between 3275971_4 and 3234854_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246026_1
- `C13`: Press down the tilt angle of 3246026_1 by 1 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246026_1
- `C15`: Increase A3 Offset threshold for 3234854_3
- `C16`: Increase transmission power for 3234854_3
- `C17`: Lift the tilt angle of 3246026_1 by 1 degrees
- `C18`: Decrease A3 Offset threshold for 3246026_1
- `C19`: Add neighbor relationship between 3246026_1 and 3234854_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234854_3
- `C21`: Adjust the azimuth of 3246026_1 by 19 degrees
- `C22`: Increase transmission power for 3246026_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.124 | MS1 | 121.4656655606 | 31.1446251357 | 248 | 504990 | -83.10 | 17.37 | 560.88 | 0.04 | 2.29 | 1567 |
| 2024-09-20 22:21:32.107 | MS1 | 121.4656644871 | 31.1446348939 | 248 | 504990 | -81.01 | 17.50 | 297.04 | 0.13 | 2.46 | 1584 |
| 2024-09-20 22:21:33.876 | MS1 | 121.4656624410 | 31.1446351555 | 248 | 504990 | -83.40 | 16.83 | 323.48 | 0.00 | 2.56 | 1566 |
| 2024-09-20 22:21:34.244 | MS1 | 121.4656669988 | 31.1446195456 | 248 | 504990 | -87.43 | 2.18 | 58.75 | 0.04 | 1.12 | 1561 |
| 2024-09-20 22:21:35.288 | MS1 | 121.4656628364 | 31.1446349944 | 248 | 504990 | -88.33 | 0.09 | 61.28 | 0.10 | 1.06 | 1567 |
| 2024-09-20 22:21:36.225 | MS1 | 121.4656708243 | 31.1446221226 | 248 | 504990 | -93.20 | 0.81 | 73.31 | 0.00 | 1.14 | 1571 |
| 2024-09-20 22:21:37.395 | MS1 | 121.4656589180 | 31.1446301857 | 248 | 504990 | -94.68 | 0.94 | 78.35 | 0.02 | 1.35 | 1560 |
| 2024-09-20 22:21:38.278 | MS1 | 121.4656618512 | 31.1446185977 | 248 | 504990 | -94.60 | 2.01 | 39.26 | 0.12 | 1.34 | 1563 |
| 2024-09-20 22:21:39.627 | MS1 | 121.4656699484 | 31.1446308370 | 248 | 504990 | -91.31 | 2.84 | 64.93 | 0.03 | 1.38 | 1578 |
| 2024-09-20 22:21:40.215 | MS1 | 121.4656649375 | 31.1446335785 | 248 | 504990 | -75.99 | 13.93 | 361.35 | 0.03 | 2.29 | 1570 |
| 2024-09-20 22:21:41.741 | MS1 | 121.4656655034 | 31.1446210722 | 248 | 504990 | -81.96 | 13.64 | 511.43 | 0.06 | 2.64 | 1582 |
| 2024-09-20 22:21:42.869 | MS1 | 121.4656774095 | 31.1446318360 | 248 | 504990 | -78.69 | 15.22 | 318.09 | 0.17 | 2.07 | 1572 |

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
| 3234854 | 3 | 121.4755472432 | 31.1468668779 | 282 | 2 | 3 | 30.6 | TDD | 901 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3246026 | 1 | 121.4723836179 | 31.1506086537 | 243 | 0 | 2 | 17.6 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3247742 | 2 | 121.4724961586 | 31.1487341447 | 267 | 1 | 0 | 25.4 | TDD | 107 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3275971 | 4 | 121.4716222675 | 31.1509729059 | 281 | 6 | 1 | 21.3 | TDD | 446 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.408 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.424 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.573 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.573 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246026 | 1 | 13.1383 | 8.9721 | -109.3544 | 5.2901 | 98.0768 | 0.0074 | 0.0025 |
| 2024_09_20 22:00 | 3247742 | 2 | 13.5332 | 18.3887 | -114.4031 | 18.6966 | 86.9259 | 0.0024 | 0.0100 |
| 2024_09_20 22:00 | 3234854 | 3 | 6.3724 | 9.3057 | -115.2066 | 18.6062 | 166.5599 | 0.0028 | 0.0083 |
| 2024_09_20 22:00 | 3275971 | 4 | 15.0461 | 9.9989 | -117.2805 | 14.9100 | 89.0251 | 0.0173 | 0.0012 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416490_461A6E4B | 504990 | 901 | -87.2 | 504990 | 248 | -87.2 | 504990 | 446 | -88.5 | 504990 | 107 |
| MR_1774416490_D799E87A | 504990 | 248 | -88.6 | 504990 | 901 | -84.3 | 504990 | 446 | -85.2 | 504990 | 107 |
| MR_1774416490_444B0F90 | 504990 | 901 | -89.2 | 504990 | 248 | -84.3 | 504990 | 446 | -86.0 | 504990 | 107 |
| MR_1774416490_2861B2EA | 504990 | 248 | -88.8 | 504990 | 901 | -86.3 | 504990 | 446 | -85.6 | 504990 | 107 |
| MR_1774416490_A483E31A | 504990 | 248 | -87.6 | 504990 | 901 | -83.9 | 504990 | 446 | -86.9 | 504990 | 107 |
| MR_1774416490_7891ABE7 | 504990 | 901 | -85.8 | 504990 | 248 | -85.9 | 504990 | 446 | -87.3 | 504990 | 107 |
| MR_1774416490_F380F94C | 504990 | 901 | -88.4 | 504990 | 248 | -84.8 | 504990 | 446 | -86.4 | 504990 | 107 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1796: `e155f6ef-dac...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e155f6ef-dac3-4750-be52-18bb76d55377` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238496_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1796] topology](images/train_1796.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3238496_4
- `C2`: Decrease transmission power for 3238496_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248888_5
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248888_5
- `C5`: Decrease A3 Offset threshold for 3248888_5
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238496_4
- `C7`: Adjust the azimuth of 3238496_4 by 40 degrees
- `C8`: Increase A3 Offset threshold for 3248888_5
- `C9`: Add neighbor relationship between 3238496_4 and 3248888_5
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238496_4 **← 정답**
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease A3 Offset threshold for 3238496_4
- `C13`: Increase transmission power for 3238496_4
- `C14`: Press down the tilt angle of 3238496_4 by 2 degrees
- `C15`: Increase transmission power for 3248888_5
- `C16`: Adjust the azimuth of 3248888_5 by 30 degrees
- `C17`: Check test server and transmission issues
- `C18`: Press down the tilt angle  of 3248888_5 by 2 degrees
- `C19`: Add neighbor relationship between 3259534_8 and 3248888_5
- `C20`: Lift the tilt angle  of 3248888_5 by 2 degrees
- `C21`: Decrease transmission power for 3248888_5
- `C22`: Lift the tilt angle of 3238496_4 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.119 | MS1 | 121.4656746350 | 31.1446224731 | 630 | 504990 | -95.40 | 11.34 | 591.05 | 0.19 | 2.83 | 1594 |
| 2024-09-20 22:21:32.821 | MS1 | 121.4656621235 | 31.1446261566 | 298 | 504990 | -95.75 | 10.71 | 468.00 | 0.01 | 2.61 | 1579 |
| 2024-09-20 22:21:33.161 | MS1 | 121.4656598937 | 31.1446205755 | 475 | 504990 | -95.72 | 14.81 | 345.11 | 0.10 | 2.68 | 1591 |
| 2024-09-20 22:21:34.449 | MS1 | 121.4656668827 | 31.1446227747 | 900 | 152650 | -87.47 | 2.92 | 97.20 | 0.12 | 1.91 | 947 |
| 2024-09-20 22:21:35.426 | MS1 | 121.4656745705 | 31.1446261911 | 540 | 152650 | -88.57 | 3.28 | 54.64 | 0.17 | 1.60 | 978 |
| 2024-09-20 22:21:36.709 | MS1 | 121.4656703979 | 31.1446196276 | 486 | 152650 | -96.22 | 2.56 | 88.07 | 0.18 | 1.56 | 903 |
| 2024-09-20 22:21:37.479 | MS1 | 121.4656699056 | 31.1446351188 | 523 | 152650 | -92.00 | 7.68 | 85.32 | 0.03 | 1.70 | 998 |
| 2024-09-20 22:21:38.822 | MS1 | 121.4656658742 | 31.1446278474 | 900 | 152650 | -89.50 | 2.60 | 71.98 | 0.05 | 1.60 | 913 |
| 2024-09-20 22:21:39.102 | MS1 | 121.4656626593 | 31.1446339557 | 540 | 152650 | -87.94 | 4.05 | 91.88 | 0.05 | 1.99 | 948 |
| 2024-09-20 22:21:40.399 | MS1 | 121.4656642403 | 31.1446290063 | 486 | 152650 | -89.99 | 6.14 | 67.35 | 0.12 | 2.27 | 1567 |
| 2024-09-20 22:21:41.328 | MS1 | 121.4656693010 | 31.1446292405 | 523 | 152650 | -89.82 | 3.81 | 49.65 | 0.17 | 2.69 | 1576 |
| 2024-09-20 22:21:42.340 | MS1 | 121.4656659116 | 31.1446358298 | 900 | 152650 | -91.47 | 7.39 | 97.68 | 0.01 | 2.86 | 1583 |

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
| 3238496 | 4 | 121.4748709450 | 31.1475679149 | 210 | 2 | 8 | 7.9 | TDD | 630 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3240830 | 10 | 121.4721085682 | 31.1558970879 | 337 | 9 | 8 | 22.3 | FDD | 554 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3241700 | 7 | 121.4745551090 | 31.1484679620 | 144 | 7 | 0 | 14.2 | FDD | 900 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3242114 | 9 | 121.4667951293 | 31.1440189568 | 269 | 2 | 11 | 16.6 | FDD | 1000 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3243991 | 6 | 121.4671577164 | 31.1506399550 | 25 | 1 | 6 | 19.6 | TDD | 475 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3246551 | 13 | 121.4675232360 | 31.1523533268 | 259 | 10 | 2 | 10.8 | FDD | 540 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3248888 | 5 | 121.4672162938 | 31.1505486518 | 163 | 0 | 8 | 20.1 | TDD | 407 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3253264 | 2 | 121.4677598578 | 31.1554300608 | 5 | 10 | 6 | 19.6 | TDD | 298 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3254045 | 12 | 121.4754465163 | 31.1522713325 | 346 | 3 | 7 | 1.0 | FDD | 603 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3259534 | 8 | 121.4657317050 | 31.1549914688 | 89 | 7 | 12 | 27.9 | FDD | 486 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3259930 | 1 | 121.4644076653 | 31.1507405529 | 101 | 9 | 3 | 19.2 | TDD | 34 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3269754 | 11 | 121.4742547028 | 31.1538440623 | 60 | 6 | 10 | 29.9 | FDD | 523 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3278250 | 3 | 121.4692211654 | 31.1555376235 | 37 | 2 | 7 | 18.0 | TDD | 942 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.044 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.068 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.192 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.192 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.922 | NREventA2 | measId:1;ServCellPCI:32;Ser... |
| 2024-09-20 22:21:35.046 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.310 | NREventA5 | measId:3;ServCellPCI:32;Ser... |
| 2024-09-20 22:21:35.345 | NRHandoverAttempt | SourcePCI:32;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.389 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.401 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.551 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.551 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259930 | 1 | 17.2882 | 5.4961 | -114.9403 | 9.8474 | 167.9220 | 0.0149 | 0.0009 |
| 2024_09_20 22:00 | 3253264 | 2 | 16.9175 | 6.4781 | -117.6136 | 5.2878 | 188.1583 | 0.0140 | 0.0125 |
| 2024_09_20 22:00 | 3278250 | 3 | 16.3122 | 18.1368 | -116.4789 | 5.9516 | 176.8304 | 0.0135 | 0.0038 |
| 2024_09_20 22:00 | 3238496 | 4 | 10.9989 | 19.4198 | -115.6901 | 11.2836 | 175.5378 | 0.0177 | 0.0153 |
| 2024_09_20 22:00 | 3248888 | 5 | 13.5463 | 6.6832 | -117.0233 | 19.4125 | 196.0756 | 0.0175 | 0.0133 |
| 2024_09_20 22:00 | 3243991 | 6 | 16.5311 | 9.8753 | -114.5755 | 10.9453 | 120.5666 | 0.0005 | 0.0181 |
| 2024_09_20 22:00 | 3241700 | 7 | 16.7131 | 19.7510 | -114.1273 | 3.4324 | 46.7028 | 0.0123 | 0.0160 |
| 2024_09_20 22:00 | 3259534 | 8 | 8.4022 | 14.3746 | -116.5975 | 4.7219 | 55.9876 | 0.0095 | 0.0010 |
| 2024_09_20 22:00 | 3242114 | 9 | 17.9692 | 9.4926 | -115.0537 | 3.9355 | 24.2224 | 0.0072 | 0.0080 |
| 2024_09_20 22:00 | 3240830 | 10 | 8.5942 | 19.4684 | -115.3186 | 4.4396 | 49.4003 | 0.0051 | 0.0124 |
| 2024_09_20 22:00 | 3269754 | 11 | 14.3887 | 15.8004 | -116.9854 | 3.6122 | 52.2164 | 0.0017 | 0.0106 |
| 2024_09_20 22:00 | 3254045 | 12 | 6.7643 | 16.4762 | -116.2452 | 3.7549 | 48.4910 | 0.0097 | 0.0172 |
| 2024_09_20 22:00 | 3246551 | 13 | 10.2933 | 7.0544 | -115.1548 | 3.9140 | 42.8855 | 0.0048 | 0.0155 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416416_AA94C78A | 504990 | 475 | -95.2 | 504990 | 407 | -93.6 | 504990 | 34 | -102.3 | 504990 | 942 |
| MR_1774416416_2AAFD288 | 504990 | 475 | -96.3 | 504990 | 407 | -91.7 | 504990 | 34 | -102.7 | 504990 | 942 |
| MR_1774416416_51CDEC26 | 152650 | 900 | -89.1 | 152650 | 554 | -92.4 | 152650 | 1000 | -93.9 | 152650 | 603 |
| MR_1774416416_6D176A17 | 152650 | 900 | -85.9 | 152650 | 554 | -91.1 | 152650 | 1000 | -93.1 | 152650 | 603 |
| MR_1774416416_B2D6BB11 | 504990 | 475 | -97.2 | 504990 | 407 | -92.4 | 504990 | 34 | -100.8 | 504990 | 942 |
| MR_1774416416_BB771A6E | 504990 | 475 | -96.0 | 504990 | 407 | -92.8 | 504990 | 34 | -102.1 | 504990 | 942 |
| MR_1774416416_85636A59 | 152650 | 900 | -86.7 | 152650 | 554 | -93.9 | 152650 | 1000 | -96.8 | 152650 | 603 |
| MR_1774416416_7EFC9B12 | 152650 | 900 | -85.6 | 152650 | 554 | -91.6 | 152650 | 1000 | -93.6 | 152650 | 603 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1797: `e35ecf6b-39a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e35ecf6b-39ad-45e4-92e3-bac6471c656b` |
| Tag | **multiple-answer** |
| 정답 | **C2|C3** |
| C2 의미 | Adjust the azimuth of 3274851_4 by 50 degrees |
| C3 의미 | Increase transmission power for 3274851_4 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1797] topology](images/train_1797.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Adjust the azimuth of 3274851_4 by 50 degrees **← 정답**
- `C3`: Increase transmission power for 3274851_4 **← 정답**
- `C4`: Check test server and transmission issues
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213263_1
- `C6`: Adjust the azimuth of 3213263_1 by 39 degrees
- `C7`: Decrease transmission power for 3274851_4
- `C8`: Press down the tilt angle  of 3213263_1 by 3 degrees
- `C9`: Lift the tilt angle  of 3213263_1 by 3 degrees
- `C10`: Press down the tilt angle of 3274851_4 by 10 degrees
- `C11`: Lift the tilt angle of 3274851_4 by 10 degrees
- `C12`: Increase A3 Offset threshold for 3274851_4
- `C13`: Decrease A3 Offset threshold for 3213263_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274851_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213263_1
- `C16`: Decrease transmission power for 3213263_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274851_4
- `C18`: Add neighbor relationship between 3274851_4 and 3213263_1
- `C19`: Increase transmission power for 3213263_1
- `C20`: Increase A3 Offset threshold for 3213263_1
- `C21`: Decrease A3 Offset threshold for 3274851_4
- `C22`: Add neighbor relationship between 3225246_3 and 3213263_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.762 | MS1 | 121.4656688209 | 31.1446358867 | 791 | 504990 | -89.84 | 12.38 | 402.62 | 0.10 | 2.20 | 1590 |
| 2024-09-20 22:21:32.693 | MS1 | 121.4656717138 | 31.1446308273 | 791 | 504990 | -86.99 | 15.14 | 547.62 | 0.14 | 2.45 | 1598 |
| 2024-09-20 22:21:33.792 | MS1 | 121.4656717606 | 31.1446225280 | 791 | 504990 | -88.08 | 14.78 | 400.30 | 0.13 | 2.37 | 1594 |
| 2024-09-20 22:21:34.790 | MS1 | 121.4656630217 | 31.1446289722 | 791 | 504990 | -108.22 | -1.21 | 49.81 | 0.05 | 1.00 | 1590 |
| 2024-09-20 22:21:35.461 | MS1 | 121.4656671793 | 31.1446234746 | 791 | 504990 | -108.96 | 1.36 | 66.26 | 0.05 | 1.19 | 1589 |
| 2024-09-20 22:21:36.807 | MS1 | 121.4656777533 | 31.1446275195 | 791 | 504990 | -101.50 | 1.84 | 62.88 | 0.15 | 1.29 | 1565 |
| 2024-09-20 22:21:37.136 | MS1 | 121.4656764255 | 31.1446292109 | 791 | 504990 | -105.94 | 0.66 | 32.14 | 0.14 | 1.34 | 1596 |
| 2024-09-20 22:21:38.284 | MS1 | 121.4656590918 | 31.1446216533 | 791 | 504990 | -103.16 | -0.82 | 69.54 | 0.08 | 1.02 | 1560 |
| 2024-09-20 22:21:39.749 | MS1 | 121.4656615887 | 31.1446232981 | 791 | 504990 | -105.67 | -1.97 | 56.38 | 0.09 | 1.13 | 1597 |
| 2024-09-20 22:21:40.270 | MS1 | 121.4656598260 | 31.1446362699 | 791 | 504990 | -90.32 | 13.26 | 484.22 | 0.19 | 2.04 | 1583 |
| 2024-09-20 22:21:41.887 | MS1 | 121.4656668364 | 31.1446225725 | 791 | 504990 | -90.14 | 12.14 | 297.37 | 0.13 | 2.44 | 1589 |
| 2024-09-20 22:21:42.934 | MS1 | 121.4656667293 | 31.1446329483 | 791 | 504990 | -85.34 | 17.46 | 508.78 | 0.11 | 2.41 | 1585 |

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
| 3213263 | 1 | 121.4740346957 | 31.1478443107 | 285 | 0 | 8 | 41.1 | TDD | 188 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3222619 | 2 | 121.4688403508 | 31.1449895339 | 189 | 0 | 5 | 39.1 | TDD | 917 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3225246 | 3 | 121.4652238962 | 31.1552870881 | 75 | 13 | 9 | 19.3 | TDD | 310 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3274851 | 4 | 121.4656363318 | 31.1465233250 | 128 | 1 | 10 | 34.6 | TDD | 791 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.940 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.961 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.066 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.066 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.319 | NREventA2 | measId:1;ServCellPCI:611;Se... |
| 2024-09-20 22:21:34.457 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213263 | 1 | 11.8420 | 18.0436 | -115.5134 | 11.5965 | 99.5913 | 0.0103 | 0.0179 |
| 2024_09_20 22:00 | 3222619 | 2 | 12.1926 | 15.3135 | -116.0967 | 18.0602 | 115.5504 | 0.0181 | 0.0151 |
| 2024_09_20 22:00 | 3225246 | 3 | 14.6614 | 16.9492 | -114.3830 | 8.6253 | 112.9145 | 0.0016 | 0.0178 |
| 2024_09_20 22:00 | 3274851 | 4 | 13.3553 | 9.3239 | -117.0452 | 14.7896 | 110.0780 | 0.1849 | 0.0089 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413486_8885CB5C | 504990 | 791 | -108.2 | 504990 | 188 | -113.9 | 504990 | 310 | -119.0 | 504990 | 917 |
| MR_1774413486_A996DBDD | 504990 | 791 | -106.5 | 504990 | 188 | -116.3 | 504990 | 310 | -121.2 | 504990 | 917 |
| MR_1774413486_89234705 | 504990 | 791 | -106.8 | 504990 | 188 | -113.1 | 504990 | 310 | -118.5 | 504990 | 917 |
| MR_1774413486_E7B94C09 | 504990 | 791 | -107.7 | 504990 | 188 | -116.7 | 504990 | 310 | -120.1 | 504990 | 917 |
| MR_1774413486_7FB756B2 | 504990 | 791 | -106.9 | 504990 | 188 | -113.2 | 504990 | 310 | -121.8 | 504990 | 917 |
| MR_1774413486_6A83D99A | 504990 | 791 | -108.2 | 504990 | 188 | -113.8 | 504990 | 310 | -120.0 | 504990 | 917 |
| MR_1774413486_53298CE0 | 504990 | 791 | -109.6 | 504990 | 188 | -115.4 | 504990 | 310 | -118.2 | 504990 | 917 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1798: `18720a20-fda...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `18720a20-fda4-4e32-a899-ac01c712e2ce` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215590_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1798] topology](images/train_1798.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3211638_12 and 3249749_3
- `C2`: Add neighbor relationship between 3215590_1 and 3249749_3
- `C3`: Press down the tilt angle of 3215590_1 by 1 degrees
- `C4`: Decrease transmission power for 3249749_3
- `C5`: Lift the tilt angle of 3215590_1 by 1 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215590_1
- `C7`: Press down the tilt angle  of 3249749_3 by 0 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249749_3
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Increase A3 Offset threshold for 3249749_3
- `C11`: Adjust the azimuth of 3249749_3 by 12 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249749_3
- `C13`: Increase transmission power for 3249749_3
- `C14`: Check test server and transmission issues
- `C15`: Decrease transmission power for 3215590_1
- `C16`: Adjust the azimuth of 3215590_1 by 37 degrees
- `C17`: Decrease A3 Offset threshold for 3215590_1
- `C18`: Decrease A3 Offset threshold for 3249749_3
- `C19`: Lift the tilt angle  of 3249749_3 by 0 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215590_1 **← 정답**
- `C21`: Increase A3 Offset threshold for 3215590_1
- `C22`: Increase transmission power for 3215590_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.541 | MS1 | 121.4656701137 | 31.1446214666 | 350 | 504990 | -94.93 | 9.79 | 346.18 | 0.14 | 2.87 | 1564 |
| 2024-09-20 22:21:32.141 | MS1 | 121.4656739851 | 31.1446346091 | 62 | 504990 | -93.79 | 11.37 | 497.94 | 0.16 | 2.91 | 1597 |
| 2024-09-20 22:21:33.678 | MS1 | 121.4656608455 | 31.1446197904 | 283 | 504990 | -93.80 | 13.18 | 493.95 | 0.01 | 2.94 | 1563 |
| 2024-09-20 22:21:34.792 | MS1 | 121.4656714763 | 31.1446312968 | 567 | 152650 | -87.53 | 3.99 | 49.39 | 0.00 | 1.90 | 963 |
| 2024-09-20 22:21:35.696 | MS1 | 121.4656649952 | 31.1446215963 | 292 | 152650 | -95.04 | 6.25 | 65.93 | 0.14 | 1.98 | 946 |
| 2024-09-20 22:21:36.900 | MS1 | 121.4656736313 | 31.1446307765 | 796 | 152650 | -92.89 | 2.55 | 75.91 | 0.16 | 1.77 | 983 |
| 2024-09-20 22:21:37.876 | MS1 | 121.4656702050 | 31.1446240754 | 677 | 152650 | -95.27 | 3.35 | 100.34 | 0.17 | 1.65 | 930 |
| 2024-09-20 22:21:38.372 | MS1 | 121.4656680368 | 31.1446235660 | 567 | 152650 | -89.35 | 7.41 | 87.85 | 0.13 | 1.60 | 954 |
| 2024-09-20 22:21:39.470 | MS1 | 121.4656729547 | 31.1446223924 | 292 | 152650 | -93.14 | 6.17 | 66.50 | 0.02 | 1.83 | 970 |
| 2024-09-20 22:21:40.489 | MS1 | 121.4656670804 | 31.1446325970 | 796 | 152650 | -96.73 | 6.60 | 80.16 | 0.09 | 2.98 | 1592 |
| 2024-09-20 22:21:41.760 | MS1 | 121.4656647634 | 31.1446327740 | 677 | 152650 | -87.41 | 5.91 | 71.14 | 0.17 | 2.33 | 1595 |
| 2024-09-20 22:21:42.558 | MS1 | 121.4656716853 | 31.1446339911 | 567 | 152650 | -96.37 | 3.80 | 70.58 | 0.10 | 2.55 | 1579 |

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
| 3211638 | 12 | 121.4725780273 | 31.1539661919 | 118 | 5 | 6 | 28.6 | FDD | 796 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3215590 | 1 | 121.4651720146 | 31.1499313552 | 138 | 0 | 8 | 7.6 | TDD | 350 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3219230 | 5 | 121.4712078983 | 31.1500075093 | 203 | 0 | 7 | 3.3 | TDD | 283 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3222750 | 6 | 121.4748082653 | 31.1445588587 | 86 | 1 | 1 | 27.5 | TDD | 62 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3225716 | 2 | 121.4756844241 | 31.1551557383 | 158 | 10 | 3 | 15.2 | TDD | 644 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3238909 | 7 | 121.4753044194 | 31.1487595251 | 121 | 4 | 7 | 19.4 | FDD | 292 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3246862 | 10 | 121.4672314581 | 31.1557227376 | 307 | 2 | 1 | 4.6 | FDD | 813 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3249749 | 3 | 121.4678570869 | 31.1503300261 | 186 | 0 | 6 | 4.9 | TDD | 747 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3250419 | 4 | 121.4674326471 | 31.1499737299 | 218 | 2 | 7 | 13.4 | TDD | 696 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3260777 | 11 | 121.4734218907 | 31.1551813587 | 132 | 13 | 0 | 27.4 | FDD | 567 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3261813 | 8 | 121.4682219038 | 31.1511531947 | 128 | 9 | 11 | 22.2 | FDD | 677 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3263380 | 9 | 121.4687064992 | 31.1487260490 | 255 | 12 | 9 | 2.1 | FDD | 873 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3275250 | 13 | 121.4750082953 | 31.1490838563 | 69 | 3 | 10 | 19.0 | FDD | 830 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |

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
| 2024-09-20 22:21:31.554 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.570 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.714 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.714 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.433 | NREventA2 | measId:1;ServCellPCI:44;Ser... |
| 2024-09-20 22:21:35.553 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.853 | NREventA5 | measId:3;ServCellPCI:44;Ser... |
| 2024-09-20 22:21:35.900 | NRHandoverAttempt | SourcePCI:44;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.931 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.943 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:36.054 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.054 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215590 | 1 | 14.6335 | 6.1792 | -115.1341 | 14.5629 | 191.9202 | 0.0068 | 0.0105 |
| 2024_09_20 22:00 | 3225716 | 2 | 16.9476 | 18.6264 | -114.2612 | 5.7797 | 100.9887 | 0.0032 | 0.0041 |
| 2024_09_20 22:00 | 3249749 | 3 | 18.5722 | 11.2845 | -117.4529 | 12.8019 | 136.2882 | 0.0119 | 0.0171 |
| 2024_09_20 22:00 | 3250419 | 4 | 11.9757 | 7.8784 | -114.1347 | 11.0660 | 177.5631 | 0.0023 | 0.0070 |
| 2024_09_20 22:00 | 3219230 | 5 | 10.6934 | 9.4977 | -116.9964 | 19.8499 | 136.6171 | 0.0073 | 0.0078 |
| 2024_09_20 22:00 | 3222750 | 6 | 11.5231 | 8.9148 | -115.3662 | 18.5484 | 174.2488 | 0.0144 | 0.0147 |
| 2024_09_20 22:00 | 3238909 | 7 | 5.1908 | 10.1862 | -116.3078 | 3.3037 | 41.8293 | 0.0059 | 0.0054 |
| 2024_09_20 22:00 | 3261813 | 8 | 12.2340 | 17.9719 | -115.0297 | 3.1537 | 43.3933 | 0.0080 | 0.0051 |
| 2024_09_20 22:00 | 3263380 | 9 | 5.0847 | 6.4127 | -116.3168 | 3.1277 | 43.1625 | 0.0074 | 0.0156 |
| 2024_09_20 22:00 | 3246862 | 10 | 6.4639 | 9.5023 | -116.3624 | 3.1195 | 50.0692 | 0.0141 | 0.0072 |
| 2024_09_20 22:00 | 3260777 | 11 | 15.9694 | 18.1064 | -115.0777 | 3.8585 | 50.9999 | 0.0049 | 0.0005 |
| 2024_09_20 22:00 | 3211638 | 12 | 9.1778 | 6.3714 | -117.3957 | 3.1081 | 23.4948 | 0.0075 | 0.0072 |
| 2024_09_20 22:00 | 3275250 | 13 | 18.4138 | 7.3094 | -115.0124 | 4.5263 | 59.9048 | 0.0188 | 0.0027 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415767_0A322574 | 504990 | 283 | -92.0 | 504990 | 747 | -94.6 | 504990 | 644 | -100.1 | 504990 | 696 |
| MR_1774415767_EC3C48E6 | 504990 | 283 | -94.5 | 504990 | 747 | -96.5 | 504990 | 644 | -100.1 | 504990 | 696 |
| MR_1774415767_623801CD | 152650 | 567 | -87.0 | 152650 | 813 | -93.8 | 152650 | 873 | -93.4 | 152650 | 830 |
| MR_1774415767_22A06DF0 | 504990 | 283 | -92.2 | 504990 | 747 | -95.4 | 504990 | 644 | -101.1 | 504990 | 696 |
| MR_1774415767_DE889B19 | 152650 | 567 | -88.6 | 152650 | 813 | -90.7 | 152650 | 873 | -93.1 | 152650 | 830 |
| MR_1774415767_BF52A9B9 | 152650 | 567 | -86.5 | 152650 | 813 | -90.7 | 152650 | 873 | -91.9 | 152650 | 830 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1799: `02b0c4d4-6b6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `02b0c4d4-6b63-4e4f-b88d-abd7a6c2fe29` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Add neighbor relationship between 3260279_3 and 3225299_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1799] topology](images/train_1799.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3225299_4 by 6 degrees
- `C2`: Increase transmission power for 3260279_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225299_4
- `C4`: Increase A3 Offset threshold for 3260279_3
- `C5`: Adjust the azimuth of 3260279_3 by 5 degrees
- `C6`: Press down the tilt angle  of 3225299_4 by 3 degrees
- `C7`: Add neighbor relationship between 3260279_3 and 3225299_4 **← 정답**
- `C8`: Decrease transmission power for 3225299_4
- `C9`: Decrease A3 Offset threshold for 3225299_4
- `C10`: Press down the tilt angle of 3260279_3 by 8 degrees
- `C11`: Decrease A3 Offset threshold for 3260279_3
- `C12`: Increase transmission power for 3225299_4
- `C13`: Add neighbor relationship between 3275390_1 and 3225299_4
- `C14`: Increase A3 Offset threshold for 3225299_4
- `C15`: Lift the tilt angle  of 3225299_4 by 3 degrees
- `C16`: Check test server and transmission issues
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260279_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225299_4
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Lift the tilt angle of 3260279_3 by 8 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260279_3
- `C22`: Decrease transmission power for 3260279_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.924 | MS1 | 121.4656613927 | 31.1446274935 | 247 | 504990 | -80.40 | 14.85 | 371.31 | 0.18 | 2.55 | 1561 |
| 2024-09-20 22:21:32.527 | MS1 | 121.4656615176 | 31.1446183724 | 247 | 504990 | -81.76 | 15.04 | 575.46 | 0.18 | 2.30 | 1590 |
| 2024-09-20 22:21:33.929 | MS1 | 121.4656605308 | 31.1446217511 | 247 | 504990 | -82.84 | 15.28 | 584.53 | 0.10 | 2.60 | 1573 |
| 2024-09-20 22:21:34.368 | MS1 | 121.4656718812 | 31.1446193816 | 247 | 504990 | -88.17 | -0.98 | 44.98 | 0.09 | 1.47 | 1577 |
| 2024-09-20 22:21:35.406 | MS1 | 121.4656751384 | 31.1446295911 | 247 | 504990 | -91.96 | -1.10 | 68.78 | 0.20 | 1.11 | 1581 |
| 2024-09-20 22:21:36.641 | MS1 | 121.4656581068 | 31.1446353200 | 247 | 504990 | -86.38 | -3.05 | 51.88 | 0.02 | 1.47 | 1567 |
| 2024-09-20 22:21:37.444 | MS1 | 121.4656748698 | 31.1446374180 | 247 | 504990 | -93.31 | -1.15 | 23.32 | 0.03 | 1.02 | 1563 |
| 2024-09-20 22:21:38.379 | MS1 | 121.4656770929 | 31.1446216851 | 247 | 504990 | -80.54 | 14.66 | 476.71 | 0.02 | 1.08 | 1595 |
| 2024-09-20 22:21:39.891 | MS1 | 121.4656651783 | 31.1446190929 | 247 | 504990 | -78.17 | 14.10 | 443.22 | 0.18 | 1.24 | 1592 |
| 2024-09-20 22:21:40.631 | MS1 | 121.4656703809 | 31.1446360088 | 247 | 504990 | -81.07 | 16.52 | 357.88 | 0.04 | 2.38 | 1599 |
| 2024-09-20 22:21:41.575 | MS1 | 121.4656586443 | 31.1446277706 | 247 | 504990 | -79.92 | 12.22 | 498.15 | 0.03 | 2.02 | 1565 |
| 2024-09-20 22:21:42.195 | MS1 | 121.4656647596 | 31.1446235768 | 247 | 504990 | -82.84 | 14.46 | 319.74 | 0.14 | 2.65 | 1598 |

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
| 3225299 | 4 | 121.4702401985 | 31.1524737392 | 201 | 1 | 6 | 34.7 | TDD | 503 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3234212 | 2 | 121.4700303811 | 31.1538229071 | 325 | 1 | 6 | 24.3 | TDD | 634 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3260279 | 3 | 121.4676779924 | 31.1469667223 | 211 | 5 | 12 | 16.3 | TDD | 247 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3275390 | 1 | 121.4757876955 | 31.1483424072 | 7 | 11 | 9 | 27.9 | TDD | 304 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.548 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.573 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.696 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.696 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.414 | NREventA3 | measId:2;ServCellPCI:928;Se... |
| 2024-09-20 22:21:36.414 | NREventA3 | measId:2;ServCellPCI:928;Se... |
| 2024-09-20 22:21:37.414 | NREventA3 | measId:2;ServCellPCI:928;Se... |
| 2024-09-20 22:21:39.914 | NRRRCReestablishAttempt | PCI:928 |
| 2024-09-20 22:21:39.924 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.936 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:40.083 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.083 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275390 | 1 | 7.8540 | 18.7261 | -116.5929 | 12.8462 | 156.3244 | 0.0123 | 0.0065 |
| 2024_09_20 22:00 | 3234212 | 2 | 17.0758 | 16.3267 | -114.2504 | 13.4395 | 195.5482 | 0.0069 | 0.0171 |
| 2024_09_20 22:00 | 3260279 | 3 | 15.3431 | 11.3994 | -117.2548 | 10.3885 | 140.7123 | 0.0047 | 0.1382 |
| 2024_09_20 22:00 | 3225299 | 4 | 5.9296 | 19.4997 | -117.4814 | 5.8322 | 146.4080 | 0.0035 | 0.0121 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414697_504DAE61 | 504990 | 247 | -88.8 | 504990 | 503 | -84.9 | 504990 | 304 | -90.6 | 504990 | 634 |
| MR_1774414697_B21E47C3 | 504990 | 503 | -82.9 | 504990 | 247 | -86.8 | 504990 | 304 | -91.5 | 504990 | 634 |
| MR_1774414697_1EE1068D | 504990 | 247 | -86.3 | 504990 | 503 | -82.6 | 504990 | 304 | -90.0 | 504990 | 634 |
| MR_1774414697_57D52A9C | 504990 | 503 | -82.0 | 504990 | 247 | -88.1 | 504990 | 304 | -89.9 | 504990 | 634 |
| MR_1774414697_B50931BB | 504990 | 247 | -88.6 | 504990 | 503 | -82.6 | 504990 | 304 | -92.2 | 504990 | 634 |
| MR_1774414697_1F95082D | 504990 | 247 | -89.0 | 504990 | 503 | -82.6 | 504990 | 304 | -92.6 | 504990 | 634 |
| MR_1774414697_4FE2FB36 | 504990 | 503 | -83.9 | 504990 | 247 | -89.4 | 504990 | 304 | -93.7 | 504990 | 634 |
| MR_1774414697_3666F5CF | 504990 | 247 | -88.2 | 504990 | 503 | -85.1 | 504990 | 304 | -93.5 | 504990 | 634 |

> *... 2개 열 생략 (전체 14열)*

---
