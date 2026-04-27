# Track A 문제 분석 — train[1350]~train[1359]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1350] ~ train[1359] (10개)

## 목차

1. [문제 1350: `ef5c0f48-6d3...`](#1350) — single-answer, 정답: C5
2. [문제 1351: `3872104f-e2f...`](#1351) — multiple-answer, 정답: C5|C9
3. [문제 1352: `f5cf52b1-61b...`](#1352) — single-answer, 정답: C1
4. [문제 1353: `f43318ef-30c...`](#1353) — multiple-answer, 정답: C10|C16
5. [문제 1354: `690d447a-caa...`](#1354) — single-answer, 정답: C13
6. [문제 1355: `72e1da3b-026...`](#1355) — single-answer, 정답: C12
7. [문제 1356: `aba71a6b-19d...`](#1356) — single-answer, 정답: C13
8. [문제 1357: `113d606d-1c1...`](#1357) — single-answer, 정답: C15
9. [문제 1358: `a15f7b3d-803...`](#1358) — multiple-answer, 정답: C5|C15
10. [문제 1359: `24098cee-e35...`](#1359) — single-answer, 정답: C9

---

### 문제 1350: `ef5c0f48-6d3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ef5c0f48-6d3d-484e-9a8e-f4bfc32806d9` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Lift the tilt angle  of 3272751_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1350] topology](images/train_1350.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3269144_1
- `C2`: Decrease A3 Offset threshold for 3269144_1
- `C3`: Add neighbor relationship between 3269144_1 and 3211828_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269144_1
- `C5`: Lift the tilt angle  of 3272751_4 by 10 degrees **← 정답**
- `C6`: Decrease A3 Offset threshold for 3211828_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211828_3
- `C8`: Add neighbor relationship between 3272751_4 and 3211828_3
- `C9`: Adjust the azimuth of 3272751_4 by 37 degrees
- `C10`: Increase A3 Offset threshold for 3211828_3
- `C11`: Press down the tilt angle  of 3272751_4 by 10 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease transmission power for 3211828_3
- `C14`: Check test server and transmission issues
- `C15`: Increase transmission power for 3211828_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269144_1
- `C17`: Adjust the azimuth of 3269144_1 by 29 degrees
- `C18`: Increase transmission power for 3269144_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211828_3
- `C20`: Lift the tilt angle of 3269144_1 by 2 degrees
- `C21`: Press down the tilt angle of 3269144_1 by 2 degrees
- `C22`: Decrease transmission power for 3269144_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.368 | MS1 | 121.4656632242 | 31.1446220095 | 177 | 504990 | -87.82 | 13.07 | 472.10 | 0.17 | 2.76 | 1598 |
| 2024-09-20 22:21:32.184 | MS1 | 121.4656600211 | 31.1446324724 | 177 | 504990 | -89.91 | 17.24 | 345.18 | 0.20 | 2.87 | 1570 |
| 2024-09-20 22:21:33.480 | MS1 | 121.4656696414 | 31.1446241965 | 177 | 504990 | -85.16 | 15.03 | 340.34 | 0.18 | 2.97 | 1562 |
| 2024-09-20 22:21:34.636 | MS1 | 121.4656667161 | 31.1446327581 | 177 | 504990 | -87.95 | 17.91 | 70.83 | 0.04 | 2.30 | 1560 |
| 2024-09-20 22:21:35.138 | MS1 | 121.4656609666 | 31.1446323406 | 177 | 504990 | -87.25 | 17.26 | 63.70 | 0.07 | 2.16 | 1568 |
| 2024-09-20 22:21:36.794 | MS1 | 121.4656651852 | 31.1446376390 | 177 | 504990 | -88.76 | 17.51 | 99.13 | 0.11 | 2.21 | 1570 |
| 2024-09-20 22:21:37.645 | MS1 | 121.4656670992 | 31.1446338247 | 177 | 504990 | -91.07 | 8.97 | 61.29 | 0.11 | 2.08 | 1578 |
| 2024-09-20 22:21:38.769 | MS1 | 121.4656714065 | 31.1446243046 | 177 | 504990 | -90.85 | 11.65 | 58.03 | 0.11 | 2.48 | 1571 |
| 2024-09-20 22:21:39.687 | MS1 | 121.4656586842 | 31.1446201783 | 177 | 504990 | -91.47 | 8.29 | 74.63 | 0.01 | 2.77 | 1561 |
| 2024-09-20 22:21:40.250 | MS1 | 121.4656673432 | 31.1446306736 | 177 | 504990 | -89.46 | 12.06 | 467.25 | 0.04 | 2.38 | 1567 |
| 2024-09-20 22:21:41.622 | MS1 | 121.4656612188 | 31.1446267525 | 177 | 504990 | -93.84 | 10.50 | 585.73 | 0.00 | 2.67 | 1580 |
| 2024-09-20 22:21:42.368 | MS1 | 121.4656765261 | 31.1446268376 | 177 | 504990 | -92.04 | 10.11 | 500.52 | 0.08 | 2.85 | 1565 |

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
| 3211828 | 3 | 121.4658706111 | 31.1508847074 | 145 | 15 | 10 | 25.2 | TDD | 127 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3232264 | 2 | 121.4700768568 | 31.1452826106 | 330 | 4 | 5 | 19.9 | TDD | 731 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3269144 | 1 | 121.4688327653 | 31.1551531448 | 223 | 0 | 7 | 37.0 | TDD | 177 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3272751 | 4 | 121.4745470365 | 31.1544687209 | 7 | 5 | 0 | 37.6 | TDD | 927 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.344 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.369 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.500 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.500 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.236 | NREventA3 | measId:2;ServCellPCI:951;Se... |
| 2024-09-20 22:21:38.476 | NRHandoverAttempt | SourcePCI:951;SourceNR-ARFC... |
| 2024-09-20 22:21:38.524 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.536 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.641 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.641 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269144 | 1 | 77.8651 | 88.8865 | -117.1783 | 10.4827 | 188.3446 | 0.0089 | 0.0149 |
| 2024_09_20 22:00 | 3232264 | 2 | 19.8549 | 15.0676 | -115.4068 | 12.4598 | 97.4782 | 0.0029 | 0.0170 |
| 2024_09_20 22:00 | 3211828 | 3 | 18.8890 | 13.6572 | -116.7979 | 17.6269 | 156.5631 | 0.0021 | 0.0016 |
| 2024_09_20 22:00 | 3272751 | 4 | 19.6515 | 10.8915 | -114.3640 | 14.3504 | 84.2590 | 0.0093 | 0.0017 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412042_60B3F2B1 | 504990 | 177 | -88.7 | 504990 | 127 | -92.2 | 504990 | 927 | -97.8 | 504990 | 731 |
| MR_1774412042_6C359DFB | 504990 | 177 | -89.6 | 504990 | 127 | -92.0 | 504990 | 927 | -95.1 | 504990 | 731 |
| MR_1774412042_48BCC149 | 504990 | 177 | -87.5 | 504990 | 127 | -92.0 | 504990 | 927 | -97.1 | 504990 | 731 |
| MR_1774412042_0578D790 | 504990 | 177 | -88.8 | 504990 | 127 | -93.1 | 504990 | 927 | -97.1 | 504990 | 731 |
| MR_1774412042_173119CC | 504990 | 177 | -89.2 | 504990 | 127 | -95.3 | 504990 | 927 | -97.2 | 504990 | 731 |
| MR_1774412042_52F19615 | 504990 | 177 | -89.3 | 504990 | 127 | -93.9 | 504990 | 927 | -95.3 | 504990 | 731 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1351: `3872104f-e2f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3872104f-e2f4-401a-bdab-e06be91d9626` |
| Tag | **multiple-answer** |
| 정답 | **C5|C9** |
| C5 의미 | Press down the tilt angle  of 3222492_4 by 5 degrees |
| C9 의미 | Decrease transmission power for 3222492_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1351] topology](images/train_1351.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3234296_1
- `C2`: Add neighbor relationship between 3234296_1 and 3222492_4
- `C3`: Increase A3 Offset threshold for 3222492_4
- `C4`: Adjust the azimuth of 3222492_4 by 7 degrees
- `C5`: Press down the tilt angle  of 3222492_4 by 5 degrees **← 정답**
- `C6`: Decrease A3 Offset threshold for 3234296_1
- `C7`: Check test server and transmission issues
- `C8`: Increase transmission power for 3222492_4
- `C9`: Decrease transmission power for 3222492_4 **← 정답**
- `C10`: Increase A3 Offset threshold for 3234296_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234296_1
- `C12`: Add neighbor relationship between 3216846_2 and 3222492_4
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Adjust the azimuth of 3234296_1 by 32 degrees
- `C15`: Decrease A3 Offset threshold for 3222492_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234296_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222492_4
- `C18`: Lift the tilt angle  of 3222492_4 by 5 degrees
- `C19`: Lift the tilt angle of 3234296_1 by 4 degrees
- `C20`: Press down the tilt angle of 3234296_1 by 4 degrees
- `C21`: Increase transmission power for 3234296_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222492_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.480 | MS1 | 121.4656670244 | 31.1446286589 | 469 | 504990 | -75.01 | 16.04 | 327.71 | 0.15 | 2.79 | 1592 |
| 2024-09-20 22:21:32.471 | MS1 | 121.4656596167 | 31.1446313429 | 469 | 504990 | -82.20 | 16.27 | 362.30 | 0.05 | 2.41 | 1573 |
| 2024-09-20 22:21:33.865 | MS1 | 121.4656773079 | 31.1446280329 | 469 | 504990 | -76.68 | 13.48 | 387.00 | 0.12 | 2.31 | 1569 |
| 2024-09-20 22:21:34.637 | MS1 | 121.4656748198 | 31.1446191059 | 469 | 504990 | -90.34 | 2.96 | 57.89 | 0.19 | 1.29 | 1570 |
| 2024-09-20 22:21:35.766 | MS1 | 121.4656697666 | 31.1446336097 | 469 | 504990 | -94.98 | 0.29 | 82.97 | 0.08 | 1.11 | 1580 |
| 2024-09-20 22:21:36.821 | MS1 | 121.4656591773 | 31.1446183811 | 469 | 504990 | -91.96 | 0.94 | 51.09 | 0.16 | 1.35 | 1578 |
| 2024-09-20 22:21:37.135 | MS1 | 121.4656692334 | 31.1446197397 | 469 | 504990 | -86.64 | 1.88 | 42.58 | 0.12 | 1.27 | 1563 |
| 2024-09-20 22:21:38.940 | MS1 | 121.4656761443 | 31.1446374062 | 469 | 504990 | -93.61 | 1.44 | 68.60 | 0.06 | 1.28 | 1587 |
| 2024-09-20 22:21:39.635 | MS1 | 121.4656688955 | 31.1446322208 | 469 | 504990 | -93.02 | 0.19 | 65.97 | 0.07 | 1.32 | 1568 |
| 2024-09-20 22:21:40.636 | MS1 | 121.4656714874 | 31.1446328535 | 469 | 504990 | -83.01 | 12.52 | 460.79 | 0.19 | 2.96 | 1569 |
| 2024-09-20 22:21:41.209 | MS1 | 121.4656645046 | 31.1446198874 | 469 | 504990 | -84.23 | 17.07 | 519.78 | 0.04 | 2.41 | 1589 |
| 2024-09-20 22:21:42.539 | MS1 | 121.4656595444 | 31.1446232611 | 469 | 504990 | -76.47 | 12.61 | 505.05 | 0.12 | 2.52 | 1575 |

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
| 3216846 | 2 | 121.4732120161 | 31.1556293130 | 75 | 9 | 0 | 46.6 | TDD | 601 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3222492 | 4 | 121.4680516225 | 31.1528571393 | 187 | 4 | 6 | 23.6 | TDD | 343 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3234296 | 1 | 121.4739807107 | 31.1548493677 | 247 | 3 | 7 | 34.4 | TDD | 469 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3259881 | 3 | 121.4685799802 | 31.1474156314 | 257 | 15 | 3 | 40.5 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.117 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.132 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.234 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.234 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234296 | 1 | 17.0503 | 17.9822 | -109.7705 | 11.2564 | 101.6051 | 0.0195 | 0.0186 |
| 2024_09_20 22:00 | 3216846 | 2 | 13.0494 | 16.2569 | -116.0034 | 7.4085 | 93.1412 | 0.0047 | 0.0150 |
| 2024_09_20 22:00 | 3259881 | 3 | 7.2573 | 11.4493 | -116.6828 | 10.8726 | 87.2515 | 0.0155 | 0.0180 |
| 2024_09_20 22:00 | 3222492 | 4 | 5.7010 | 7.1202 | -117.7658 | 12.4762 | 171.4746 | 0.0016 | 0.0088 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416952_1C197D23 | 504990 | 343 | -88.8 | 504990 | 469 | -89.2 | 504990 | 601 | -91.0 | 504990 | 309 |
| MR_1774416952_60EDC8EA | 504990 | 469 | -89.7 | 504990 | 343 | -87.9 | 504990 | 601 | -88.7 | 504990 | 309 |
| MR_1774416952_8278A2A5 | 504990 | 469 | -88.9 | 504990 | 343 | -89.7 | 504990 | 601 | -90.4 | 504990 | 309 |
| MR_1774416952_552EC410 | 504990 | 343 | -91.4 | 504990 | 469 | -89.0 | 504990 | 601 | -87.9 | 504990 | 309 |
| MR_1774416952_0DBE4CC5 | 504990 | 343 | -88.8 | 504990 | 469 | -89.5 | 504990 | 601 | -90.5 | 504990 | 309 |
| MR_1774416952_1F767B29 | 504990 | 343 | -89.6 | 504990 | 469 | -89.8 | 504990 | 601 | -88.8 | 504990 | 309 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1352: `f5cf52b1-61b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f5cf52b1-61b4-4492-bae5-714eca8032c5` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Decrease A3 Offset threshold for 3257827_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1352] topology](images/train_1352.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3257827_4 **← 정답**
- `C2`: Increase transmission power for 3223604_3
- `C3`: Increase transmission power for 3257827_4
- `C4`: Decrease transmission power for 3223604_3
- `C5`: Add neighbor relationship between 3257827_4 and 3223604_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223604_3
- `C7`: Decrease transmission power for 3257827_4
- `C8`: Adjust the azimuth of 3223604_3 by 50 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257827_4
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Add neighbor relationship between 3252608_2 and 3223604_3
- `C12`: Lift the tilt angle  of 3223604_3 by 10 degrees
- `C13`: Increase A3 Offset threshold for 3257827_4
- `C14`: Increase A3 Offset threshold for 3223604_3
- `C15`: Decrease A3 Offset threshold for 3223604_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223604_3
- `C17`: Press down the tilt angle  of 3223604_3 by 10 degrees
- `C18`: Adjust the azimuth of 3257827_4 by 8 degrees
- `C19`: Press down the tilt angle of 3257827_4 by 10 degrees
- `C20`: Lift the tilt angle of 3257827_4 by 10 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257827_4
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.810 | MS1 | 121.4656601895 | 31.1446290072 | 165 | 504990 | -80.23 | 16.45 | 453.77 | 0.17 | 2.94 | 1577 |
| 2024-09-20 22:21:32.559 | MS1 | 121.4656731335 | 31.1446189969 | 165 | 504990 | -84.36 | 15.81 | 394.95 | 0.18 | 2.25 | 1560 |
| 2024-09-20 22:21:33.329 | MS1 | 121.4656652441 | 31.1446292485 | 165 | 504990 | -81.51 | 12.93 | 428.84 | 0.06 | 2.66 | 1600 |
| 2024-09-20 22:21:34.222 | MS1 | 121.4656705911 | 31.1446344439 | 165 | 504990 | -86.89 | -2.02 | 62.02 | 0.05 | 1.25 | 1569 |
| 2024-09-20 22:21:35.594 | MS1 | 121.4656587915 | 31.1446238759 | 165 | 504990 | -89.88 | -3.50 | 72.24 | 0.02 | 1.16 | 1577 |
| 2024-09-20 22:21:36.924 | MS1 | 121.4656670357 | 31.1446259125 | 165 | 504990 | -90.11 | -3.20 | 65.22 | 0.10 | 1.41 | 1563 |
| 2024-09-20 22:21:37.917 | MS1 | 121.4656642687 | 31.1446324790 | 165 | 504990 | -91.87 | -3.62 | 59.14 | 0.18 | 1.04 | 1591 |
| 2024-09-20 22:21:38.808 | MS1 | 121.4656660575 | 31.1446202054 | 165 | 504990 | -86.54 | -3.40 | 69.43 | 0.10 | 1.48 | 1590 |
| 2024-09-20 22:21:39.859 | MS1 | 121.4656695444 | 31.1446317822 | 780 | 504990 | -79.49 | 15.62 | 288.79 | 0.02 | 1.20 | 1573 |
| 2024-09-20 22:21:40.476 | MS1 | 121.4656759907 | 31.1446184246 | 780 | 504990 | -84.17 | 17.79 | 475.56 | 0.17 | 2.08 | 1565 |
| 2024-09-20 22:21:41.232 | MS1 | 121.4656651175 | 31.1446369059 | 780 | 504990 | -80.51 | 14.18 | 339.38 | 0.15 | 2.52 | 1592 |
| 2024-09-20 22:21:42.524 | MS1 | 121.4656732690 | 31.1446313812 | 780 | 504990 | -81.52 | 12.02 | 587.94 | 0.16 | 2.99 | 1591 |

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
| 3223604 | 3 | 121.4656119809 | 31.1462397507 | 98 | 0 | 2 | 49.9 | TDD | 780 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3252608 | 2 | 121.4679092471 | 31.1510509539 | 234 | 9 | 6 | 15.2 | TDD | 43 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3257827 | 4 | 121.4675590178 | 31.1557362905 | 180 | 11 | 4 | 46.2 | TDD | 165 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3260516 | 1 | 121.4650814500 | 31.1489205970 | 227 | 6 | 7 | 40.9 | TDD | 242 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.266 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.291 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.411 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.411 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.166 | NREventA3 | measId:2;ServCellPCI:611;Se... |
| 2024-09-20 22:21:38.406 | NRHandoverAttempt | SourcePCI:611;SourceNR-ARFC... |
| 2024-09-20 22:21:38.447 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.458 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.559 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.559 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260516 | 1 | 5.7730 | 14.8002 | -116.7521 | 16.9414 | 120.0485 | 0.0145 | 0.0053 |
| 2024_09_20 22:00 | 3252608 | 2 | 12.2336 | 14.9635 | -115.3065 | 6.7858 | 127.1985 | 0.0123 | 0.0056 |
| 2024_09_20 22:00 | 3223604 | 3 | 18.9326 | 5.2405 | -114.4074 | 14.9279 | 130.5847 | 0.0158 | 0.0087 |
| 2024_09_20 22:00 | 3257827 | 4 | 7.5906 | 16.3743 | -117.4510 | 5.5722 | 91.1394 | 0.0001 | 0.1019 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412909_7E1EAC09 | 504990 | 165 | -87.1 | 504990 | 780 | -80.5 | 504990 | 43 | -89.2 | 504990 | 242 |
| MR_1774412909_CA91C354 | 504990 | 165 | -86.3 | 504990 | 780 | -81.2 | 504990 | 43 | -87.5 | 504990 | 242 |
| MR_1774412909_35F6C45D | 504990 | 780 | -83.1 | 504990 | 165 | -86.4 | 504990 | 43 | -89.5 | 504990 | 242 |
| MR_1774412909_A0DC67F6 | 504990 | 165 | -86.1 | 504990 | 780 | -79.8 | 504990 | 43 | -86.2 | 504990 | 242 |
| MR_1774412909_285072D3 | 504990 | 165 | -87.3 | 504990 | 780 | -80.7 | 504990 | 43 | -87.6 | 504990 | 242 |
| MR_1774412909_FDD8D03B | 504990 | 165 | -88.6 | 504990 | 780 | -81.9 | 504990 | 43 | -86.1 | 504990 | 242 |
| MR_1774412909_A79C025A | 504990 | 165 | -86.6 | 504990 | 780 | -80.0 | 504990 | 43 | -87.0 | 504990 | 242 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1353: `f43318ef-30c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f43318ef-30c8-4920-9155-11044eade085` |
| Tag | **multiple-answer** |
| 정답 | **C10|C16** |
| C10 의미 | Increase transmission power for 3213217_4 |
| C16 의미 | Adjust the azimuth of 3213217_4 by 18 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1353] topology](images/train_1353.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3213217_4 by 10 degrees
- `C2`: Add neighbor relationship between 3213217_4 and 3274137_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274137_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213217_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213217_4
- `C6`: Increase A3 Offset threshold for 3213217_4
- `C7`: Lift the tilt angle  of 3274137_2 by 3 degrees
- `C8`: Decrease transmission power for 3274137_2
- `C9`: Add neighbor relationship between 3219610_3 and 3274137_2
- `C10`: Increase transmission power for 3213217_4 **← 정답**
- `C11`: Check test server and transmission issues
- `C12`: Increase A3 Offset threshold for 3274137_2
- `C13`: Decrease transmission power for 3213217_4
- `C14`: Decrease A3 Offset threshold for 3213217_4
- `C15`: Lift the tilt angle of 3213217_4 by 10 degrees
- `C16`: Adjust the azimuth of 3213217_4 by 18 degrees **← 정답**
- `C17`: Press down the tilt angle  of 3274137_2 by 3 degrees
- `C18`: Increase transmission power for 3274137_2
- `C19`: Adjust the azimuth of 3274137_2 by 39 degrees
- `C20`: Decrease A3 Offset threshold for 3274137_2
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274137_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.540 | MS1 | 121.4656581145 | 31.1446183482 | 292 | 504990 | -89.75 | 13.06 | 304.69 | 0.12 | 2.02 | 1581 |
| 2024-09-20 22:21:32.637 | MS1 | 121.4656595187 | 31.1446227321 | 292 | 504990 | -90.63 | 16.20 | 487.34 | 0.19 | 2.04 | 1586 |
| 2024-09-20 22:21:33.904 | MS1 | 121.4656667720 | 31.1446257217 | 292 | 504990 | -86.25 | 13.06 | 446.84 | 0.09 | 2.29 | 1583 |
| 2024-09-20 22:21:34.903 | MS1 | 121.4656731868 | 31.1446257455 | 292 | 504990 | -109.35 | 0.66 | 40.23 | 0.07 | 1.33 | 1599 |
| 2024-09-20 22:21:35.809 | MS1 | 121.4656652353 | 31.1446330335 | 292 | 504990 | -102.94 | -1.44 | 46.56 | 0.19 | 1.36 | 1577 |
| 2024-09-20 22:21:36.670 | MS1 | 121.4656776476 | 31.1446222480 | 292 | 504990 | -101.28 | -0.59 | 25.53 | 0.09 | 1.01 | 1592 |
| 2024-09-20 22:21:37.849 | MS1 | 121.4656662847 | 31.1446199634 | 292 | 504990 | -108.17 | -1.29 | 77.47 | 0.13 | 1.35 | 1564 |
| 2024-09-20 22:21:38.337 | MS1 | 121.4656590734 | 31.1446334686 | 292 | 504990 | -103.66 | 0.68 | 54.85 | 0.06 | 1.34 | 1577 |
| 2024-09-20 22:21:39.471 | MS1 | 121.4656766151 | 31.1446337166 | 292 | 504990 | -101.36 | -0.63 | 75.18 | 0.12 | 1.21 | 1571 |
| 2024-09-20 22:21:40.348 | MS1 | 121.4656715114 | 31.1446349442 | 292 | 504990 | -93.62 | 12.91 | 561.80 | 0.14 | 2.62 | 1585 |
| 2024-09-20 22:21:41.234 | MS1 | 121.4656615561 | 31.1446335651 | 292 | 504990 | -87.67 | 12.00 | 524.76 | 0.07 | 2.33 | 1591 |
| 2024-09-20 22:21:42.190 | MS1 | 121.4656722490 | 31.1446268075 | 292 | 504990 | -93.01 | 14.04 | 368.83 | 0.08 | 2.43 | 1560 |

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
| 3213217 | 4 | 121.4722014453 | 31.1451088271 | 283 | 14 | 0 | 33.3 | TDD | 292 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3217266 | 1 | 121.4679175437 | 31.1459515187 | 216 | 13 | 11 | 47.6 | TDD | 448 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3219610 | 3 | 121.4688903844 | 31.1549639437 | 128 | 5 | 6 | 39.8 | TDD | 274 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3274137 | 2 | 121.4695844683 | 31.1557033886 | 158 | 1 | 10 | 47.9 | TDD | 914 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.954 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.975 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.103 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.103 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.309 | NREventA2 | measId:1;ServCellPCI:982;Se... |
| 2024-09-20 22:21:34.424 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217266 | 1 | 16.9428 | 19.7952 | -116.9491 | 16.5401 | 150.5743 | 0.0019 | 0.0070 |
| 2024_09_20 22:00 | 3274137 | 2 | 6.9335 | 11.0949 | -115.6406 | 6.4537 | 196.8946 | 0.0032 | 0.0117 |
| 2024_09_20 22:00 | 3219610 | 3 | 19.8943 | 15.7561 | -115.9959 | 13.0930 | 106.8536 | 0.0087 | 0.0101 |
| 2024_09_20 22:00 | 3213217 | 4 | 8.5560 | 6.8483 | -115.4002 | 17.2329 | 103.4892 | 0.1279 | 0.0010 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412553_97DE012D | 504990 | 292 | -108.4 | 504990 | 914 | -112.3 | 504990 | 274 | -117.1 | 504990 | 448 |
| MR_1774412553_900F889F | 504990 | 292 | -107.8 | 504990 | 914 | -114.2 | 504990 | 274 | -119.4 | 504990 | 448 |
| MR_1774412553_DD643D50 | 504990 | 292 | -109.7 | 504990 | 914 | -113.3 | 504990 | 274 | -119.6 | 504990 | 448 |
| MR_1774412553_AF5C9023 | 504990 | 292 | -108.7 | 504990 | 914 | -112.8 | 504990 | 274 | -119.5 | 504990 | 448 |
| MR_1774412553_908F8AEE | 504990 | 292 | -109.0 | 504990 | 914 | -115.1 | 504990 | 274 | -119.2 | 504990 | 448 |
| MR_1774412553_384E4E7C | 504990 | 292 | -111.2 | 504990 | 914 | -113.9 | 504990 | 274 | -119.5 | 504990 | 448 |
| MR_1774412553_5AE1B4D6 | 504990 | 292 | -107.7 | 504990 | 914 | -115.5 | 504990 | 274 | -117.5 | 504990 | 448 |
| MR_1774412553_E5D0CF76 | 504990 | 292 | -110.9 | 504990 | 914 | -113.8 | 504990 | 274 | -119.8 | 504990 | 448 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1354: `690d447a-caa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `690d447a-caa7-4b28-b9f4-88d8a91a4369` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease A3 Offset threshold for 3246230_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1354] topology](images/train_1354.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3277261_1
- `C2`: Adjust the azimuth of 3277261_1 by 50 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246230_2
- `C4`: Decrease transmission power for 3277261_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277261_1
- `C6`: Add neighbor relationship between 3246230_2 and 3277261_1
- `C7`: Add neighbor relationship between 3260337_3 and 3277261_1
- `C8`: Adjust the azimuth of 3246230_2 by 50 degrees
- `C9`: Press down the tilt angle  of 3277261_1 by 3 degrees
- `C10`: Lift the tilt angle of 3246230_2 by 10 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246230_2
- `C12`: Press down the tilt angle of 3246230_2 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3246230_2 **← 정답**
- `C14`: Lift the tilt angle  of 3277261_1 by 3 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277261_1
- `C16`: Decrease A3 Offset threshold for 3277261_1
- `C17`: Increase A3 Offset threshold for 3246230_2
- `C18`: Increase transmission power for 3246230_2
- `C19`: Increase transmission power for 3277261_1
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease transmission power for 3246230_2
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.375 | MS1 | 121.4656725704 | 31.1446283564 | 126 | 504990 | -84.90 | 15.31 | 466.28 | 0.15 | 2.46 | 1568 |
| 2024-09-20 22:21:32.841 | MS1 | 121.4656766534 | 31.1446242874 | 126 | 504990 | -75.13 | 17.93 | 580.72 | 0.06 | 2.77 | 1574 |
| 2024-09-20 22:21:33.776 | MS1 | 121.4656580624 | 31.1446206811 | 126 | 504990 | -80.08 | 12.02 | 313.12 | 0.03 | 2.98 | 1598 |
| 2024-09-20 22:21:34.175 | MS1 | 121.4656602211 | 31.1446199298 | 126 | 504990 | -83.61 | -1.44 | 57.73 | 0.01 | 1.36 | 1574 |
| 2024-09-20 22:21:35.685 | MS1 | 121.4656643958 | 31.1446219748 | 126 | 504990 | -90.56 | -2.67 | 42.41 | 0.14 | 1.32 | 1565 |
| 2024-09-20 22:21:36.617 | MS1 | 121.4656686970 | 31.1446353150 | 126 | 504990 | -88.35 | -2.40 | 56.70 | 0.02 | 1.01 | 1585 |
| 2024-09-20 22:21:37.300 | MS1 | 121.4656664018 | 31.1446187034 | 126 | 504990 | -91.48 | -2.85 | 44.21 | 0.17 | 1.45 | 1578 |
| 2024-09-20 22:21:38.561 | MS1 | 121.4656587290 | 31.1446211135 | 126 | 504990 | -83.65 | -0.62 | 67.19 | 0.07 | 1.06 | 1576 |
| 2024-09-20 22:21:39.624 | MS1 | 121.4656765140 | 31.1446249146 | 194 | 504990 | -79.95 | 13.96 | 284.73 | 0.03 | 1.32 | 1574 |
| 2024-09-20 22:21:40.163 | MS1 | 121.4656584895 | 31.1446270987 | 194 | 504990 | -83.16 | 12.93 | 523.76 | 0.17 | 2.81 | 1565 |
| 2024-09-20 22:21:41.535 | MS1 | 121.4656665426 | 31.1446255916 | 194 | 504990 | -77.70 | 15.23 | 536.10 | 0.11 | 2.40 | 1590 |
| 2024-09-20 22:21:42.630 | MS1 | 121.4656756846 | 31.1446249111 | 194 | 504990 | -79.84 | 13.37 | 414.25 | 0.14 | 2.13 | 1578 |

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
| 3222244 | 4 | 121.4645930705 | 31.1495648033 | 197 | 8 | 2 | 19.3 | TDD | 919 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3246230 | 2 | 121.4646943829 | 31.1529889938 | 48 | 12 | 11 | 44.1 | TDD | 126 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3260337 | 3 | 121.4669029778 | 31.1470902389 | 312 | 8 | 9 | 44.6 | TDD | 406 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3277261 | 1 | 121.4720901655 | 31.1520118945 | 283 | 1 | 8 | 35.6 | TDD | 194 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.833 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.856 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.986 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.986 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.728 | NREventA3 | measId:2;ServCellPCI:476;Se... |
| 2024-09-20 22:21:37.968 | NRHandoverAttempt | SourcePCI:476;SourceNR-ARFC... |
| 2024-09-20 22:21:38.015 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.029 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.176 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.176 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277261 | 1 | 8.3354 | 18.6075 | -115.7728 | 15.8298 | 89.8659 | 0.0093 | 0.0139 |
| 2024_09_20 22:00 | 3246230 | 2 | 5.1832 | 12.1059 | -114.2659 | 13.0883 | 192.2281 | 0.0093 | 0.1886 |
| 2024_09_20 22:00 | 3260337 | 3 | 15.3250 | 9.5372 | -114.8758 | 8.2515 | 133.0528 | 0.0025 | 0.0139 |
| 2024_09_20 22:00 | 3222244 | 4 | 11.3058 | 18.0307 | -114.9076 | 15.1507 | 150.2718 | 0.0161 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416107_7533EF6D | 504990 | 194 | -78.7 | 504990 | 126 | -83.8 | 504990 | 406 | -88.2 | 504990 | 919 |
| MR_1774416107_9A933F5F | 504990 | 194 | -77.3 | 504990 | 126 | -85.5 | 504990 | 406 | -86.9 | 504990 | 919 |
| MR_1774416107_D1CB21C3 | 504990 | 194 | -76.9 | 504990 | 126 | -85.4 | 504990 | 406 | -85.7 | 504990 | 919 |
| MR_1774416107_9EA3D0D5 | 504990 | 126 | -84.1 | 504990 | 194 | -77.4 | 504990 | 406 | -85.1 | 504990 | 919 |
| MR_1774416107_DA35F6D6 | 504990 | 126 | -85.2 | 504990 | 194 | -77.4 | 504990 | 406 | -86.5 | 504990 | 919 |
| MR_1774416107_44F2A692 | 504990 | 126 | -84.7 | 504990 | 194 | -76.8 | 504990 | 406 | -86.6 | 504990 | 919 |
| MR_1774416107_FD4090B6 | 504990 | 126 | -82.0 | 504990 | 194 | -78.4 | 504990 | 406 | -86.8 | 504990 | 919 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1355: `72e1da3b-026...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `72e1da3b-0263-4f01-a5d0-1a30397b3266` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1355] topology](images/train_1355.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3222029_2 by 7 degrees
- `C2`: Increase transmission power for 3222029_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250461_3
- `C4`: Decrease A3 Offset threshold for 3250461_3
- `C5`: Decrease transmission power for 3222029_2
- `C6`: Check test server and transmission issues
- `C7`: Adjust the azimuth of 3250461_3 by 50 degrees
- `C8`: Increase A3 Offset threshold for 3222029_2
- `C9`: Increase A3 Offset threshold for 3250461_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222029_2
- `C11`: Decrease A3 Offset threshold for 3222029_2
- `C12`: Insufficient data; more data is needed for judgment. **← 정답**
- `C13`: Press down the tilt angle  of 3222029_2 by 7 degrees
- `C14`: Lift the tilt angle of 3250461_3 by 10 degrees
- `C15`: Increase transmission power for 3250461_3
- `C16`: Adjust the azimuth of 3222029_2 by 50 degrees
- `C17`: Add neighbor relationship between 3232941_4 and 3222029_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222029_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250461_3
- `C20`: Add neighbor relationship between 3250461_3 and 3222029_2
- `C21`: Press down the tilt angle of 3250461_3 by 10 degrees
- `C22`: Decrease transmission power for 3250461_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.527 | MS1 | 121.4656665468 | 31.1446321383 | 204 | 504990 | -86.25 | 16.15 | 487.31 | 0.02 | 2.67 | 1596 |
| 2024-09-20 22:21:32.827 | MS1 | 121.4656600480 | 31.1446359813 | 204 | 504990 | -87.06 | 15.43 | 497.59 | 0.19 | 2.68 | 1598 |
| 2024-09-20 22:21:33.691 | MS1 | 121.4656763378 | 31.1446240443 | 204 | 504990 | -86.68 | 13.83 | 361.11 | 0.10 | 2.04 | 1563 |
| 2024-09-20 22:21:34.818 | MS1 | 121.4656667477 | 31.1446287004 | 204 | 504990 | -85.28 | 13.99 | 80.02 | 0.19 | 2.05 | 1569 |
| 2024-09-20 22:21:35.850 | MS1 | 121.4656763198 | 31.1446181024 | 204 | 504990 | -88.47 | 12.82 | 88.05 | 0.14 | 2.99 | 1574 |
| 2024-09-20 22:21:36.284 | MS1 | 121.4656611636 | 31.1446221260 | 204 | 504990 | -90.42 | 14.46 | 51.38 | 0.19 | 2.02 | 1596 |
| 2024-09-20 22:21:37.260 | MS1 | 121.4656727207 | 31.1446215904 | 204 | 504990 | -91.61 | 8.03 | 73.58 | 0.18 | 2.78 | 1583 |
| 2024-09-20 22:21:38.443 | MS1 | 121.4656588217 | 31.1446296337 | 204 | 504990 | -90.74 | 7.37 | 85.09 | 0.12 | 2.10 | 1590 |
| 2024-09-20 22:21:39.763 | MS1 | 121.4656701952 | 31.1446237109 | 204 | 504990 | -90.28 | 11.85 | 83.96 | 0.18 | 2.13 | 1584 |
| 2024-09-20 22:21:40.363 | MS1 | 121.4656714413 | 31.1446375628 | 204 | 504990 | -92.74 | 9.63 | 504.10 | 0.02 | 2.30 | 1562 |
| 2024-09-20 22:21:41.325 | MS1 | 121.4656647135 | 31.1446284282 | 204 | 504990 | -93.60 | 7.51 | 526.49 | 0.02 | 2.12 | 1598 |
| 2024-09-20 22:21:42.624 | MS1 | 121.4656772778 | 31.1446285556 | 204 | 504990 | -92.96 | 7.80 | 470.33 | 0.06 | 2.65 | 1594 |

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
| 3222029 | 2 | 121.4671590117 | 31.1504549067 | 307 | 5 | 6 | 25.4 | TDD | 700 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3232941 | 4 | 121.4735794977 | 31.1533440488 | 258 | 13 | 9 | 23.3 | TDD | 116 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3242899 | 1 | 121.4700833168 | 31.1441336474 | 220 | 0 | 6 | 41.2 | TDD | 393 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3250461 | 3 | 121.4739027915 | 31.1479994445 | 163 | 14 | 5 | 19.4 | TDD | 204 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.294 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.316 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.453 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.453 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.116 | NREventA3 | measId:2;ServCellPCI:328;Se... |
| 2024-09-20 22:21:38.356 | NRHandoverAttempt | SourcePCI:328;SourceNR-ARFC... |
| 2024-09-20 22:21:38.398 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.412 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.559 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.559 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3242899 | 1 | 81.4065 | 85.4993 | -115.5419 | 7.9254 | 138.4816 | 0.0151 | 0.0054 |
| 2024_09_19 22:00 | 3222029 | 2 | 84.3074 | 83.7180 | -114.8593 | 5.7166 | 153.2420 | 0.0002 | 0.0014 |
| 2024_09_19 22:00 | 3250461 | 3 | 86.7199 | 80.6587 | -116.4716 | 12.6799 | 81.2839 | 0.0024 | 0.0180 |
| 2024_09_19 22:00 | 3232941 | 4 | 90.2458 | 90.0960 | -115.1692 | 17.8000 | 147.4501 | 0.0139 | 0.0060 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414782_D0F1BA1F | 504990 | 204 | -85.2 | 504990 | 700 | -86.4 | 504990 | 116 | -98.0 | 504990 | 393 |
| MR_1774414782_755BCE27 | 504990 | 204 | -86.3 | 504990 | 700 | -86.1 | 504990 | 116 | -100.5 | 504990 | 393 |
| MR_1774414782_0174C7D0 | 504990 | 204 | -84.0 | 504990 | 700 | -84.6 | 504990 | 116 | -97.6 | 504990 | 393 |
| MR_1774414782_8F21A7D1 | 504990 | 204 | -84.2 | 504990 | 700 | -87.6 | 504990 | 116 | -97.7 | 504990 | 393 |
| MR_1774414782_703BF9B4 | 504990 | 204 | -83.4 | 504990 | 700 | -87.3 | 504990 | 116 | -97.6 | 504990 | 393 |
| MR_1774414782_02C27443 | 504990 | 204 | -84.5 | 504990 | 700 | -84.8 | 504990 | 116 | -98.0 | 504990 | 393 |
| MR_1774414782_8356E57C | 504990 | 204 | -84.3 | 504990 | 700 | -85.5 | 504990 | 116 | -97.3 | 504990 | 393 |
| MR_1774414782_D5DAF0D4 | 504990 | 204 | -86.8 | 504990 | 700 | -87.7 | 504990 | 116 | -97.0 | 504990 | 393 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1356: `aba71a6b-19d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `aba71a6b-19d6-46b0-8385-5cac5777bff1` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1356] topology](images/train_1356.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3258249_2 by 10 degrees
- `C2`: Press down the tilt angle  of 3271896_4 by 10 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271896_4
- `C4`: Decrease transmission power for 3258249_2
- `C5`: Increase transmission power for 3258249_2
- `C6`: Decrease transmission power for 3271896_4
- `C7`: Increase A3 Offset threshold for 3271896_4
- `C8`: Lift the tilt angle  of 3271896_4 by 10 degrees
- `C9`: Add neighbor relationship between 3258249_2 and 3271896_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258249_2
- `C11`: Increase A3 Offset threshold for 3258249_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271896_4
- `C13`: Insufficient data; more data is needed for judgment. **← 정답**
- `C14`: Adjust the azimuth of 3271896_4 by 32 degrees
- `C15`: Decrease A3 Offset threshold for 3271896_4
- `C16`: Add neighbor relationship between 3276750_3 and 3271896_4
- `C17`: Increase transmission power for 3271896_4
- `C18`: Check test server and transmission issues
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258249_2
- `C20`: Decrease A3 Offset threshold for 3258249_2
- `C21`: Lift the tilt angle of 3258249_2 by 10 degrees
- `C22`: Adjust the azimuth of 3258249_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.641 | MS1 | 121.4656693068 | 31.1446377989 | 579 | 504990 | -89.05 | 15.30 | 551.55 | 0.10 | 2.01 | 1586 |
| 2024-09-20 22:21:32.462 | MS1 | 121.4656596903 | 31.1446331371 | 579 | 504990 | -89.56 | 14.83 | 326.23 | 0.02 | 2.45 | 1580 |
| 2024-09-20 22:21:33.204 | MS1 | 121.4656644974 | 31.1446321266 | 579 | 504990 | -88.45 | 12.19 | 351.63 | 0.03 | 2.10 | 1593 |
| 2024-09-20 22:21:34.202 | MS1 | 121.4656708448 | 31.1446339817 | 579 | 504990 | -87.15 | 12.18 | 55.89 | 0.01 | 2.05 | 1598 |
| 2024-09-20 22:21:35.893 | MS1 | 121.4656665114 | 31.1446225609 | 579 | 504990 | -91.74 | 15.80 | 76.74 | 0.17 | 2.42 | 1597 |
| 2024-09-20 22:21:36.831 | MS1 | 121.4656623955 | 31.1446331334 | 579 | 504990 | -89.61 | 14.32 | 53.91 | 0.15 | 2.48 | 1582 |
| 2024-09-20 22:21:37.193 | MS1 | 121.4656678802 | 31.1446242559 | 579 | 504990 | -90.16 | 10.75 | 74.27 | 0.10 | 2.34 | 1597 |
| 2024-09-20 22:21:38.669 | MS1 | 121.4656706303 | 31.1446373016 | 579 | 504990 | -91.62 | 7.17 | 65.71 | 0.20 | 2.40 | 1591 |
| 2024-09-20 22:21:39.746 | MS1 | 121.4656706697 | 31.1446320260 | 579 | 504990 | -92.60 | 9.73 | 71.61 | 0.02 | 2.16 | 1583 |
| 2024-09-20 22:21:40.507 | MS1 | 121.4656776535 | 31.1446331493 | 579 | 504990 | -89.36 | 10.14 | 475.05 | 0.14 | 2.36 | 1579 |
| 2024-09-20 22:21:41.914 | MS1 | 121.4656719836 | 31.1446213575 | 579 | 504990 | -93.43 | 12.64 | 472.08 | 0.06 | 2.36 | 1560 |
| 2024-09-20 22:21:42.881 | MS1 | 121.4656598711 | 31.1446355170 | 579 | 504990 | -92.85 | 8.08 | 305.50 | 0.16 | 2.82 | 1589 |

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
| 3252581 | 1 | 121.4683541371 | 31.1502735410 | 22 | 3 | 7 | 15.4 | TDD | 626 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3258249 | 2 | 121.4649199352 | 31.1496466061 | 257 | 14 | 12 | 23.0 | TDD | 579 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3271896 | 4 | 121.4680765670 | 31.1452939404 | 220 | 10 | 7 | 18.3 | TDD | 910 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3276750 | 3 | 121.4725374282 | 31.1441493564 | 83 | 10 | 8 | 37.5 | TDD | 357 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.845 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.865 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.000 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.000 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.719 | NREventA3 | measId:2;ServCellPCI:367;Se... |
| 2024-09-20 22:21:37.959 | NRHandoverAttempt | SourcePCI:367;SourceNR-ARFC... |
| 2024-09-20 22:21:38.001 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.014 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.155 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.155 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3252581 | 1 | 78.8433 | 89.8274 | -116.1040 | 5.6070 | 171.2483 | 0.0109 | 0.0039 |
| 2024_09_19 22:00 | 3258249 | 2 | 82.9111 | 90.7852 | -116.7050 | 8.6908 | 137.6822 | 0.0159 | 0.0007 |
| 2024_09_19 22:00 | 3276750 | 3 | 85.6360 | 86.0534 | -115.8521 | 10.1837 | 171.9377 | 0.0096 | 0.0170 |
| 2024_09_19 22:00 | 3271896 | 4 | 86.6077 | 94.2603 | -117.2008 | 7.4974 | 118.5220 | 0.0087 | 0.0066 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415079_457AB494 | 504990 | 579 | -89.0 | 504990 | 910 | -92.9 | 504990 | 357 | -94.6 | 504990 | 626 |
| MR_1774415079_CA00ACA0 | 504990 | 579 | -85.6 | 504990 | 910 | -92.8 | 504990 | 357 | -95.9 | 504990 | 626 |
| MR_1774415079_75C05F05 | 504990 | 579 | -87.5 | 504990 | 910 | -93.2 | 504990 | 357 | -97.9 | 504990 | 626 |
| MR_1774415079_897E3197 | 504990 | 579 | -87.9 | 504990 | 910 | -93.5 | 504990 | 357 | -96.6 | 504990 | 626 |
| MR_1774415079_DE1D9D50 | 504990 | 579 | -86.4 | 504990 | 910 | -94.5 | 504990 | 357 | -94.4 | 504990 | 626 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1357: `113d606d-1c1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `113d606d-1c1e-4288-a06b-6208a2d4d394` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1357] topology](images/train_1357.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239837_4
- `C2`: Lift the tilt angle of 3236140_3 by 10 degrees
- `C3`: Adjust the azimuth of 3239837_4 by 50 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236140_3
- `C5`: Add neighbor relationship between 3236140_3 and 3239837_4
- `C6`: Press down the tilt angle of 3236140_3 by 10 degrees
- `C7`: Adjust the azimuth of 3236140_3 by 24 degrees
- `C8`: Decrease transmission power for 3239837_4
- `C9`: Increase transmission power for 3236140_3
- `C10`: Decrease A3 Offset threshold for 3239837_4
- `C11`: Check test server and transmission issues
- `C12`: Decrease A3 Offset threshold for 3236140_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239837_4
- `C14`: Increase transmission power for 3239837_4
- `C15`: Insufficient data; more data is needed for judgment. **← 정답**
- `C16`: Increase A3 Offset threshold for 3239837_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236140_3
- `C18`: Increase A3 Offset threshold for 3236140_3
- `C19`: Add neighbor relationship between 3230018_1 and 3239837_4
- `C20`: Lift the tilt angle  of 3239837_4 by 10 degrees
- `C21`: Decrease transmission power for 3236140_3
- `C22`: Press down the tilt angle  of 3239837_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.820 | MS1 | 121.4656643311 | 31.1446244124 | 876 | 504990 | -90.71 | 14.07 | 490.31 | 0.11 | 2.17 | 1567 |
| 2024-09-20 22:21:32.614 | MS1 | 121.4656657967 | 31.1446334724 | 876 | 504990 | -86.89 | 14.12 | 412.84 | 0.08 | 2.41 | 1598 |
| 2024-09-20 22:21:33.980 | MS1 | 121.4656737248 | 31.1446253624 | 876 | 504990 | -88.57 | 17.74 | 406.11 | 0.13 | 2.37 | 1590 |
| 2024-09-20 22:21:34.644 | MS1 | 121.4656761764 | 31.1446358547 | 876 | 504990 | -86.71 | 15.88 | 65.69 | 0.03 | 2.50 | 1592 |
| 2024-09-20 22:21:35.368 | MS1 | 121.4656755032 | 31.1446362601 | 876 | 504990 | -87.48 | 12.17 | 88.35 | 0.08 | 2.99 | 1586 |
| 2024-09-20 22:21:36.892 | MS1 | 121.4656628677 | 31.1446240979 | 876 | 504990 | -85.66 | 14.57 | 58.23 | 0.11 | 2.33 | 1568 |
| 2024-09-20 22:21:37.621 | MS1 | 121.4656665950 | 31.1446197162 | 876 | 504990 | -93.09 | 9.70 | 98.23 | 0.10 | 2.63 | 1595 |
| 2024-09-20 22:21:38.150 | MS1 | 121.4656633046 | 31.1446219973 | 876 | 504990 | -90.30 | 7.53 | 57.82 | 0.07 | 2.88 | 1584 |
| 2024-09-20 22:21:39.965 | MS1 | 121.4656760687 | 31.1446236044 | 876 | 504990 | -90.38 | 7.16 | 82.66 | 0.02 | 2.15 | 1568 |
| 2024-09-20 22:21:40.636 | MS1 | 121.4656643707 | 31.1446282131 | 876 | 504990 | -93.12 | 7.69 | 342.76 | 0.10 | 2.39 | 1595 |
| 2024-09-20 22:21:41.552 | MS1 | 121.4656739391 | 31.1446227160 | 876 | 504990 | -91.60 | 7.89 | 364.24 | 0.07 | 2.15 | 1564 |
| 2024-09-20 22:21:42.726 | MS1 | 121.4656704766 | 31.1446215729 | 876 | 504990 | -90.52 | 7.05 | 471.76 | 0.17 | 2.32 | 1584 |

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
| 3230018 | 1 | 121.4725836139 | 31.1481919395 | 291 | 6 | 7 | 45.3 | TDD | 168 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3236140 | 3 | 121.4656401116 | 31.1491136675 | 204 | 12 | 3 | 36.2 | TDD | 876 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3239837 | 4 | 121.4748422744 | 31.1537401179 | 21 | 13 | 9 | 20.6 | TDD | 485 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3265146 | 2 | 121.4644971685 | 31.1492806476 | 177 | 9 | 7 | 44.7 | TDD | 731 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.403 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.422 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.530 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.530 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.249 | NREventA3 | measId:2;ServCellPCI:80;Ser... |
| 2024-09-20 22:21:38.489 | NRHandoverAttempt | SourcePCI:80;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.526 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.538 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.666 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.666 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3230018 | 1 | 75.9826 | 78.6281 | -115.5831 | 17.1922 | 110.8291 | 0.0125 | 0.0053 |
| 2024_09_19 22:00 | 3265146 | 2 | 93.5526 | 85.7356 | -115.8002 | 16.6485 | 196.2884 | 0.0129 | 0.0102 |
| 2024_09_19 22:00 | 3236140 | 3 | 79.8838 | 84.7500 | -116.0480 | 19.6327 | 195.7174 | 0.0158 | 0.0051 |
| 2024_09_19 22:00 | 3239837 | 4 | 87.6023 | 90.5641 | -115.8822 | 17.0266 | 105.7195 | 0.0082 | 0.0093 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416198_9271859C | 504990 | 876 | -86.8 | 504990 | 485 | -90.8 | 504990 | 168 | -98.8 | 504990 | 731 |
| MR_1774416198_3E39E432 | 504990 | 876 | -86.3 | 504990 | 485 | -92.6 | 504990 | 168 | -98.0 | 504990 | 731 |
| MR_1774416198_520DD8D7 | 504990 | 876 | -86.0 | 504990 | 485 | -92.4 | 504990 | 168 | -95.9 | 504990 | 731 |
| MR_1774416198_703FC1B6 | 504990 | 876 | -84.8 | 504990 | 485 | -91.5 | 504990 | 168 | -96.9 | 504990 | 731 |
| MR_1774416198_B2DBCC3F | 504990 | 876 | -87.8 | 504990 | 485 | -89.5 | 504990 | 168 | -96.2 | 504990 | 731 |
| MR_1774416198_87CB2C58 | 504990 | 876 | -86.3 | 504990 | 485 | -91.9 | 504990 | 168 | -96.9 | 504990 | 731 |
| MR_1774416198_FB73A81A | 504990 | 876 | -87.1 | 504990 | 485 | -93.1 | 504990 | 168 | -96.6 | 504990 | 731 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1358: `a15f7b3d-803...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a15f7b3d-8037-4f32-97c4-668f890687c9` |
| Tag | **multiple-answer** |
| 정답 | **C5|C15** |
| C5 의미 | Increase transmission power for 3255050_2 |
| C15 의미 | Adjust the azimuth of 3255050_2 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1358] topology](images/train_1358.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255050_2
- `C2`: Decrease transmission power for 3255050_2
- `C3`: Decrease A3 Offset threshold for 3255050_2
- `C4`: Lift the tilt angle  of 3255165_3 by 3 degrees
- `C5`: Increase transmission power for 3255050_2 **← 정답**
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Lift the tilt angle of 3255050_2 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3255165_3
- `C9`: Increase A3 Offset threshold for 3255050_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255165_3
- `C11`: Increase transmission power for 3255165_3
- `C12`: Check test server and transmission issues
- `C13`: Press down the tilt angle of 3255050_2 by 10 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255050_2
- `C15`: Adjust the azimuth of 3255050_2 by 50 degrees **← 정답**
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255165_3
- `C17`: Add neighbor relationship between 3255050_2 and 3255165_3
- `C18`: Press down the tilt angle  of 3255165_3 by 3 degrees
- `C19`: Add neighbor relationship between 3231322_4 and 3255165_3
- `C20`: Decrease transmission power for 3255165_3
- `C21`: Adjust the azimuth of 3255165_3 by 47 degrees
- `C22`: Increase A3 Offset threshold for 3255165_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.499 | MS1 | 121.4656625123 | 31.1446295578 | 419 | 504990 | -89.25 | 16.35 | 427.94 | 0.16 | 2.56 | 1581 |
| 2024-09-20 22:21:32.275 | MS1 | 121.4656700191 | 31.1446248710 | 419 | 504990 | -91.60 | 14.67 | 595.73 | 0.14 | 2.93 | 1573 |
| 2024-09-20 22:21:33.696 | MS1 | 121.4656776917 | 31.1446218942 | 419 | 504990 | -87.91 | 16.87 | 401.80 | 0.18 | 2.19 | 1599 |
| 2024-09-20 22:21:34.692 | MS1 | 121.4656633718 | 31.1446216267 | 419 | 504990 | -100.75 | -1.37 | 49.58 | 0.09 | 1.26 | 1586 |
| 2024-09-20 22:21:35.532 | MS1 | 121.4656738609 | 31.1446331527 | 419 | 504990 | -102.40 | -0.12 | 47.53 | 0.01 | 1.25 | 1571 |
| 2024-09-20 22:21:36.588 | MS1 | 121.4656701952 | 31.1446209533 | 419 | 504990 | -105.07 | -1.40 | 42.82 | 0.01 | 1.10 | 1594 |
| 2024-09-20 22:21:37.910 | MS1 | 121.4656602468 | 31.1446220391 | 419 | 504990 | -106.07 | -1.03 | 63.39 | 0.11 | 1.49 | 1588 |
| 2024-09-20 22:21:38.606 | MS1 | 121.4656694346 | 31.1446224201 | 419 | 504990 | -102.87 | 1.53 | 83.08 | 0.03 | 1.49 | 1590 |
| 2024-09-20 22:21:39.316 | MS1 | 121.4656681154 | 31.1446330485 | 419 | 504990 | -109.96 | 0.49 | 75.62 | 0.08 | 1.11 | 1585 |
| 2024-09-20 22:21:40.780 | MS1 | 121.4656748814 | 31.1446269857 | 419 | 504990 | -89.45 | 13.51 | 310.36 | 0.12 | 2.13 | 1583 |
| 2024-09-20 22:21:41.674 | MS1 | 121.4656664361 | 31.1446319324 | 419 | 504990 | -87.87 | 14.26 | 319.79 | 0.10 | 2.02 | 1594 |
| 2024-09-20 22:21:42.876 | MS1 | 121.4656679837 | 31.1446202623 | 419 | 504990 | -85.85 | 15.86 | 567.92 | 0.10 | 2.87 | 1581 |

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
| 3223276 | 1 | 121.4753144093 | 31.1506548290 | 301 | 3 | 5 | 24.6 | TDD | 840 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3231322 | 4 | 121.4641573723 | 31.1538357682 | 209 | 13 | 4 | 38.0 | TDD | 95 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3255050 | 2 | 121.4742724245 | 31.1536455257 | 290 | 9 | 1 | 32.9 | TDD | 419 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3255165 | 3 | 121.4699623220 | 31.1544209890 | 154 | 2 | 5 | 15.8 | TDD | 1003 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.956 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.980 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.103 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.103 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.279 | NREventA2 | measId:1;ServCellPCI:295;Se... |
| 2024-09-20 22:21:34.426 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223276 | 1 | 10.4973 | 15.0631 | -114.2156 | 5.5411 | 189.6367 | 0.0002 | 0.0053 |
| 2024_09_20 22:00 | 3255050 | 2 | 17.5242 | 5.8894 | -114.7674 | 18.9794 | 103.9536 | 0.1700 | 0.0162 |
| 2024_09_20 22:00 | 3255165 | 3 | 18.2121 | 17.6562 | -115.5001 | 16.6255 | 98.4413 | 0.0091 | 0.0041 |
| 2024_09_20 22:00 | 3231322 | 4 | 17.7560 | 14.6886 | -117.1645 | 5.6511 | 139.1922 | 0.0134 | 0.0145 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415247_07DFF7D9 | 504990 | 419 | -99.1 | 504990 | 1003 | -104.5 | 504990 | 95 | -110.3 | 504990 | 840 |
| MR_1774415247_D5798A4D | 504990 | 419 | -102.6 | 504990 | 1003 | -103.5 | 504990 | 95 | -110.9 | 504990 | 840 |
| MR_1774415247_2DE6332E | 504990 | 419 | -99.5 | 504990 | 1003 | -103.2 | 504990 | 95 | -112.8 | 504990 | 840 |
| MR_1774415247_455D5242 | 504990 | 419 | -100.1 | 504990 | 1003 | -103.8 | 504990 | 95 | -113.5 | 504990 | 840 |
| MR_1774415247_C1C091F4 | 504990 | 419 | -100.9 | 504990 | 1003 | -105.3 | 504990 | 95 | -111.1 | 504990 | 840 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1359: `24098cee-e35...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `24098cee-e356-464e-b6ed-e98b69b383a4` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3261010_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1359] topology](images/train_1359.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3270143_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270143_1
- `C3`: Decrease A3 Offset threshold for 3261010_4
- `C4`: Decrease transmission power for 3261010_4
- `C5`: Press down the tilt angle of 3261010_4 by 5 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270143_1
- `C7`: Decrease A3 Offset threshold for 3270143_1
- `C8`: Lift the tilt angle of 3261010_4 by 5 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261010_4 **← 정답**
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261010_4
- `C11`: Add neighbor relationship between 3252201_2 and 3270143_1
- `C12`: Check test server and transmission issues
- `C13`: Increase transmission power for 3261010_4
- `C14`: Adjust the azimuth of 3270143_1 by 50 degrees
- `C15`: Press down the tilt angle  of 3270143_1 by 10 degrees
- `C16`: Lift the tilt angle  of 3270143_1 by 10 degrees
- `C17`: Add neighbor relationship between 3261010_4 and 3270143_1
- `C18`: Increase A3 Offset threshold for 3270143_1
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase A3 Offset threshold for 3261010_4
- `C21`: Adjust the azimuth of 3261010_4 by 2 degrees
- `C22`: Decrease transmission power for 3270143_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.271 | MS1 | 121.4656644118 | 31.1446203152 | 125 | 504990 | -87.99 | 15.27 | 393.45 | 0.00 | 2.33 | 1566 |
| 2024-09-20 22:21:32.787 | MS1 | 121.4656587459 | 31.1446210910 | 125 | 504990 | -89.69 | 14.86 | 320.20 | 0.16 | 2.07 | 1587 |
| 2024-09-20 22:21:33.633 | MS1 | 121.4656752742 | 31.1446292040 | 125 | 504990 | -90.41 | 15.99 | 488.50 | 0.20 | 2.28 | 1595 |
| 2024-09-20 22:21:34.234 | MS1 | 121.4656594627 | 31.1446322517 | 125 | 504990 | -91.34 | 13.30 | 61.99 | 0.55 | 2.35 | 697 |
| 2024-09-20 22:21:35.115 | MS1 | 121.4656758145 | 31.1446239376 | 125 | 504990 | -86.45 | 12.47 | 77.18 | 0.64 | 2.64 | 557 |
| 2024-09-20 22:21:36.844 | MS1 | 121.4656761420 | 31.1446281437 | 125 | 504990 | -91.05 | 13.03 | 80.31 | 0.52 | 2.39 | 639 |
| 2024-09-20 22:21:37.623 | MS1 | 121.4656664535 | 31.1446275834 | 125 | 504990 | -92.38 | 11.71 | 99.21 | 0.52 | 2.10 | 588 |
| 2024-09-20 22:21:38.897 | MS1 | 121.4656667361 | 31.1446265883 | 125 | 504990 | -90.09 | 9.23 | 72.62 | 0.62 | 2.78 | 625 |
| 2024-09-20 22:21:39.901 | MS1 | 121.4656721918 | 31.1446333767 | 125 | 504990 | -89.16 | 9.43 | 45.38 | 0.67 | 2.24 | 640 |
| 2024-09-20 22:21:40.409 | MS1 | 121.4656655608 | 31.1446287022 | 125 | 504990 | -90.26 | 7.87 | 333.56 | 0.14 | 2.80 | 1572 |
| 2024-09-20 22:21:41.195 | MS1 | 121.4656660036 | 31.1446311344 | 125 | 504990 | -89.69 | 8.92 | 470.44 | 0.11 | 2.01 | 1576 |
| 2024-09-20 22:21:42.785 | MS1 | 121.4656656917 | 31.1446247761 | 125 | 504990 | -90.76 | 8.75 | 321.78 | 0.06 | 2.83 | 1585 |

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
| 3252201 | 2 | 121.4687778888 | 31.1501101129 | 27 | 12 | 0 | 16.8 | TDD | 386 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3261010 | 4 | 121.4706783433 | 31.1555054899 | 200 | 3 | 3 | 41.4 | TDD | 125 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3270143 | 1 | 121.4650942760 | 31.1487797334 | 318 | 4 | 2 | 45.1 | TDD | 856 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3277724 | 3 | 121.4717251543 | 31.1494549046 | 125 | 15 | 12 | 19.6 | TDD | 546 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.845 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.867 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.990 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.990 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.711 | NREventA3 | measId:2;ServCellPCI:537;Se... |
| 2024-09-20 22:21:37.951 | NRHandoverAttempt | SourcePCI:537;SourceNR-ARFC... |
| 2024-09-20 22:21:37.986 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.997 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.108 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.108 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270143 | 1 | 12.6610 | 8.7235 | -114.1354 | 9.5449 | 188.2741 | 0.0066 | 0.0120 |
| 2024_09_20 22:00 | 3252201 | 2 | 16.7728 | 14.3470 | -114.7529 | 12.0445 | 131.3836 | 0.0034 | 0.0187 |
| 2024_09_20 22:00 | 3277724 | 3 | 6.1598 | 11.0857 | -116.2260 | 18.1698 | 140.9850 | 0.0077 | 0.0192 |
| 2024_09_20 22:00 | 3261010 | 4 | 11.1150 | 8.0279 | -116.1592 | 19.8721 | 194.4580 | 0.0086 | 0.0116 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414329_57C533EC | 504990 | 125 | -91.8 | 504990 | 856 | -96.7 | 504990 | 386 | -98.8 | 504990 | 546 |
| MR_1774414329_925E1648 | 504990 | 125 | -91.9 | 504990 | 856 | -98.4 | 504990 | 386 | -97.6 | 504990 | 546 |
| MR_1774414329_D596189E | 504990 | 125 | -90.7 | 504990 | 856 | -95.2 | 504990 | 386 | -99.7 | 504990 | 546 |
| MR_1774414329_AC54D9EF | 504990 | 125 | -92.0 | 504990 | 856 | -96.9 | 504990 | 386 | -95.9 | 504990 | 546 |
| MR_1774414329_20774AE7 | 504990 | 125 | -90.6 | 504990 | 856 | -98.0 | 504990 | 386 | -96.2 | 504990 | 546 |
| MR_1774414329_CFD3127F | 504990 | 125 | -90.2 | 504990 | 856 | -96.2 | 504990 | 386 | -99.3 | 504990 | 546 |
| MR_1774414329_844242AF | 504990 | 125 | -92.6 | 504990 | 856 | -98.0 | 504990 | 386 | -98.2 | 504990 | 546 |

> *... 2개 열 생략 (전체 14열)*

---
