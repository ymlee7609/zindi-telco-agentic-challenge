# Track A 문제 분석 — train[1480]~train[1489]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1480] ~ train[1489] (10개)

## 목차

1. [문제 1480: `096b584a-c7d...`](#1480) — single-answer, 정답: C15
2. [문제 1481: `dd518240-2da...`](#1481) — single-answer, 정답: C18
3. [문제 1482: `ae6a5d54-2bc...`](#1482) — single-answer, 정답: C8
4. [문제 1483: `6b8fe1cf-685...`](#1483) — single-answer, 정답: C20
5. [문제 1484: `c98edf06-d76...`](#1484) — single-answer, 정답: C17
6. [문제 1485: `2746e95c-4e5...`](#1485) — single-answer, 정답: C10
7. [문제 1486: `ce7a2d0a-917...`](#1486) — multiple-answer, 정답: C12|C19
8. [문제 1487: `a7550437-a38...`](#1487) — multiple-answer, 정답: C6|C20
9. [문제 1488: `f21e8dc6-a0c...`](#1488) — single-answer, 정답: C7
10. [문제 1489: `650cc6e2-9d0...`](#1489) — single-answer, 정답: C22

---

### 문제 1480: `096b584a-c7d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `096b584a-c7da-4613-8cd8-fd76d9660caa` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease A3 Offset threshold for 3249800_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1480] topology](images/train_1480.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3249800_4 by 50 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257094_2
- `C3`: Add neighbor relationship between 3249800_4 and 3257094_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Add neighbor relationship between 3270788_1 and 3257094_2
- `C6`: Decrease A3 Offset threshold for 3257094_2
- `C7`: Increase transmission power for 3257094_2
- `C8`: Press down the tilt angle of 3249800_4 by 10 degrees
- `C9`: Adjust the azimuth of 3257094_2 by 50 degrees
- `C10`: Decrease transmission power for 3257094_2
- `C11`: Increase A3 Offset threshold for 3249800_4
- `C12`: Increase A3 Offset threshold for 3257094_2
- `C13`: Lift the tilt angle  of 3257094_2 by 3 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249800_4
- `C15`: Decrease A3 Offset threshold for 3249800_4 **← 정답**
- `C16`: Check test server and transmission issues
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249800_4
- `C18`: Press down the tilt angle  of 3257094_2 by 3 degrees
- `C19`: Lift the tilt angle of 3249800_4 by 10 degrees
- `C20`: Decrease transmission power for 3249800_4
- `C21`: Increase transmission power for 3249800_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257094_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.648 | MS1 | 121.4656755173 | 31.1446283592 | 111 | 504990 | -79.99 | 16.51 | 327.10 | 0.18 | 2.10 | 1562 |
| 2024-09-20 22:21:32.493 | MS1 | 121.4656661730 | 31.1446181706 | 111 | 504990 | -79.17 | 12.87 | 506.12 | 0.16 | 2.35 | 1599 |
| 2024-09-20 22:21:33.914 | MS1 | 121.4656652582 | 31.1446242235 | 111 | 504990 | -79.58 | 13.67 | 422.80 | 0.19 | 2.11 | 1599 |
| 2024-09-20 22:21:34.530 | MS1 | 121.4656612576 | 31.1446232831 | 111 | 504990 | -92.93 | -1.26 | 33.37 | 0.04 | 1.23 | 1580 |
| 2024-09-20 22:21:35.614 | MS1 | 121.4656611711 | 31.1446244805 | 111 | 504990 | -86.82 | -3.47 | 45.95 | 0.06 | 1.12 | 1594 |
| 2024-09-20 22:21:36.451 | MS1 | 121.4656662098 | 31.1446263601 | 111 | 504990 | -88.24 | -2.69 | 52.54 | 0.09 | 1.30 | 1582 |
| 2024-09-20 22:21:37.893 | MS1 | 121.4656760351 | 31.1446284029 | 111 | 504990 | -85.16 | -3.89 | 60.93 | 0.16 | 1.05 | 1572 |
| 2024-09-20 22:21:38.822 | MS1 | 121.4656739637 | 31.1446378970 | 111 | 504990 | -89.66 | -0.32 | 68.18 | 0.04 | 1.39 | 1592 |
| 2024-09-20 22:21:39.512 | MS1 | 121.4656642304 | 31.1446326427 | 940 | 504990 | -79.16 | 15.97 | 168.37 | 0.09 | 1.30 | 1563 |
| 2024-09-20 22:21:40.984 | MS1 | 121.4656706244 | 31.1446295426 | 940 | 504990 | -82.85 | 13.29 | 414.76 | 0.17 | 2.63 | 1600 |
| 2024-09-20 22:21:41.708 | MS1 | 121.4656654167 | 31.1446215868 | 940 | 504990 | -75.43 | 13.34 | 360.64 | 0.14 | 2.83 | 1599 |
| 2024-09-20 22:21:42.901 | MS1 | 121.4656619415 | 31.1446325580 | 940 | 504990 | -83.06 | 12.22 | 474.86 | 0.11 | 2.48 | 1574 |

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
| 3223978 | 3 | 121.4669398632 | 31.1530057477 | 289 | 9 | 9 | 39.3 | TDD | 29 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3249800 | 4 | 121.4659275275 | 31.1539068863 | 339 | 11 | 5 | 41.0 | TDD | 111 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3257094 | 2 | 121.4660570714 | 31.1544234075 | 344 | 0 | 1 | 49.2 | TDD | 940 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3270788 | 1 | 121.4734883393 | 31.1459963560 | 312 | 11 | 7 | 44.5 | TDD | 979 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.107 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.129 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.268 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.268 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.952 | NREventA3 | measId:2;ServCellPCI:349;Se... |
| 2024-09-20 22:21:38.192 | NRHandoverAttempt | SourcePCI:349;SourceNR-ARFC... |
| 2024-09-20 22:21:38.230 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.245 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.353 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.353 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270788 | 1 | 15.6105 | 18.5083 | -116.7463 | 13.7204 | 139.0374 | 0.0188 | 0.0017 |
| 2024_09_20 22:00 | 3257094 | 2 | 19.3284 | 14.1603 | -117.6420 | 17.7613 | 194.8129 | 0.0029 | 0.0142 |
| 2024_09_20 22:00 | 3223978 | 3 | 18.2553 | 10.8766 | -117.3081 | 13.7979 | 84.3160 | 0.0003 | 0.0129 |
| 2024_09_20 22:00 | 3249800 | 4 | 14.2528 | 17.9668 | -115.4297 | 18.1745 | 149.6826 | 0.0082 | 0.1006 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416747_68CA977E | 504990 | 940 | -88.3 | 504990 | 111 | -91.2 | 504990 | 979 | -96.9 | 504990 | 29 |
| MR_1774416747_176D3E5F | 504990 | 940 | -89.2 | 504990 | 111 | -91.9 | 504990 | 979 | -96.9 | 504990 | 29 |
| MR_1774416747_4429764D | 504990 | 111 | -93.7 | 504990 | 940 | -85.8 | 504990 | 979 | -96.5 | 504990 | 29 |
| MR_1774416747_6F21F00B | 504990 | 111 | -91.7 | 504990 | 940 | -88.8 | 504990 | 979 | -97.0 | 504990 | 29 |
| MR_1774416747_CF0EB1EF | 504990 | 940 | -87.0 | 504990 | 111 | -94.2 | 504990 | 979 | -97.9 | 504990 | 29 |
| MR_1774416747_DC35C91F | 504990 | 111 | -91.2 | 504990 | 940 | -89.3 | 504990 | 979 | -98.2 | 504990 | 29 |
| MR_1774416747_C8440993 | 504990 | 940 | -86.4 | 504990 | 111 | -94.0 | 504990 | 979 | -98.0 | 504990 | 29 |
| MR_1774416747_1C12C7B2 | 504990 | 940 | -89.0 | 504990 | 111 | -93.9 | 504990 | 979 | -97.3 | 504990 | 29 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1481: `dd518240-2da...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dd518240-2daa-4746-a038-7a1d4919ada1` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1481] topology](images/train_1481.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3224512_3
- `C2`: Decrease transmission power for 3238915_2
- `C3`: Increase A3 Offset threshold for 3224512_3
- `C4`: Increase transmission power for 3224512_3
- `C5`: Increase transmission power for 3238915_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238915_2
- `C7`: Increase A3 Offset threshold for 3238915_2
- `C8`: Lift the tilt angle of 3224512_3 by 2 degrees
- `C9`: Add neighbor relationship between 3224512_3 and 3238915_2
- `C10`: Adjust the azimuth of 3224512_3 by 50 degrees
- `C11`: Decrease A3 Offset threshold for 3238915_2
- `C12`: Add neighbor relationship between 3223454_4 and 3238915_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224512_3
- `C14`: Adjust the azimuth of 3238915_2 by 50 degrees
- `C15`: Press down the tilt angle  of 3238915_2 by 3 degrees
- `C16`: Lift the tilt angle  of 3238915_2 by 3 degrees
- `C17`: Press down the tilt angle of 3224512_3 by 2 degrees
- `C18`: Insufficient data; more data is needed for judgment. **← 정답**
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238915_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224512_3
- `C21`: Decrease A3 Offset threshold for 3224512_3
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.348 | MS1 | 121.4656736114 | 31.1446203422 | 130 | 504990 | -86.23 | 13.89 | 512.04 | 0.08 | 2.18 | 1593 |
| 2024-09-20 22:21:32.628 | MS1 | 121.4656743051 | 31.1446345543 | 130 | 504990 | -85.40 | 13.40 | 485.53 | 0.17 | 2.15 | 1592 |
| 2024-09-20 22:21:33.513 | MS1 | 121.4656720218 | 31.1446192139 | 130 | 504990 | -86.39 | 16.64 | 499.87 | 0.09 | 2.88 | 1581 |
| 2024-09-20 22:21:34.261 | MS1 | 121.4656615130 | 31.1446215815 | 130 | 504990 | -85.22 | 15.49 | 86.09 | 0.19 | 2.71 | 1599 |
| 2024-09-20 22:21:35.857 | MS1 | 121.4656653664 | 31.1446221931 | 130 | 504990 | -91.72 | 15.32 | 88.16 | 0.06 | 2.98 | 1590 |
| 2024-09-20 22:21:36.558 | MS1 | 121.4656748675 | 31.1446291571 | 130 | 504990 | -90.64 | 14.26 | 83.15 | 0.18 | 2.57 | 1598 |
| 2024-09-20 22:21:37.259 | MS1 | 121.4656765287 | 31.1446292016 | 130 | 504990 | -93.58 | 10.33 | 63.46 | 0.05 | 2.77 | 1593 |
| 2024-09-20 22:21:38.570 | MS1 | 121.4656644714 | 31.1446349404 | 130 | 504990 | -91.56 | 8.15 | 75.38 | 0.16 | 2.42 | 1600 |
| 2024-09-20 22:21:39.667 | MS1 | 121.4656768846 | 31.1446364751 | 130 | 504990 | -89.10 | 11.52 | 75.30 | 0.12 | 2.78 | 1562 |
| 2024-09-20 22:21:40.902 | MS1 | 121.4656660590 | 31.1446184177 | 130 | 504990 | -92.67 | 12.82 | 349.42 | 0.11 | 2.40 | 1563 |
| 2024-09-20 22:21:41.919 | MS1 | 121.4656639016 | 31.1446297002 | 130 | 504990 | -92.38 | 8.69 | 552.41 | 0.19 | 2.11 | 1569 |
| 2024-09-20 22:21:42.180 | MS1 | 121.4656600537 | 31.1446281077 | 130 | 504990 | -89.12 | 9.33 | 394.72 | 0.01 | 2.05 | 1586 |

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
| 3223454 | 4 | 121.4748432547 | 31.1463368220 | 267 | 12 | 7 | 20.6 | TDD | 926 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3224512 | 3 | 121.4712211508 | 31.1482453517 | 341 | 0 | 12 | 27.5 | TDD | 130 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3238915 | 2 | 121.4721240652 | 31.1551574919 | 354 | 1 | 7 | 45.3 | TDD | 729 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3255950 | 1 | 121.4699476053 | 31.1515494513 | 92 | 4 | 0 | 49.6 | TDD | 984 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.430 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.453 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.575 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.575 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.327 | NREventA3 | measId:2;ServCellPCI:677;Se... |
| 2024-09-20 22:21:38.567 | NRHandoverAttempt | SourcePCI:677;SourceNR-ARFC... |
| 2024-09-20 22:21:38.607 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.621 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.769 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.769 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3255950 | 1 | 86.0831 | 81.2338 | -117.0957 | 12.1899 | 93.1995 | 0.0028 | 0.0188 |
| 2024_09_19 22:00 | 3238915 | 2 | 76.8665 | 93.2154 | -114.4539 | 11.4222 | 122.3585 | 0.0191 | 0.0060 |
| 2024_09_19 22:00 | 3224512 | 3 | 85.5233 | 79.1370 | -115.5130 | 17.9984 | 91.2423 | 0.0129 | 0.0159 |
| 2024_09_19 22:00 | 3223454 | 4 | 83.8514 | 81.7270 | -115.3212 | 9.8684 | 95.1665 | 0.0022 | 0.0084 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415781_202CCA2B | 504990 | 130 | -86.4 | 504990 | 729 | -85.6 | 504990 | 926 | -94.2 | 504990 | 984 |
| MR_1774415781_A3140D8B | 504990 | 130 | -85.0 | 504990 | 729 | -85.0 | 504990 | 926 | -92.7 | 504990 | 984 |
| MR_1774415781_33BC7B77 | 504990 | 130 | -85.0 | 504990 | 729 | -87.2 | 504990 | 926 | -94.8 | 504990 | 984 |
| MR_1774415781_B914A63A | 504990 | 130 | -84.7 | 504990 | 729 | -85.8 | 504990 | 926 | -94.5 | 504990 | 984 |
| MR_1774415781_8D3D0A75 | 504990 | 130 | -83.4 | 504990 | 729 | -86.3 | 504990 | 926 | -92.4 | 504990 | 984 |
| MR_1774415781_D9E9DD82 | 504990 | 130 | -84.6 | 504990 | 729 | -86.0 | 504990 | 926 | -95.5 | 504990 | 984 |
| MR_1774415781_A0C747C5 | 504990 | 130 | -85.0 | 504990 | 729 | -84.7 | 504990 | 926 | -94.7 | 504990 | 984 |
| MR_1774415781_6EE3DB56 | 504990 | 130 | -83.5 | 504990 | 729 | -87.9 | 504990 | 926 | -95.0 | 504990 | 984 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1482: `ae6a5d54-2bc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ae6a5d54-2bc4-47b3-b3dd-f5da359bf2e6` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1482] topology](images/train_1482.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3248128_1
- `C2`: Lift the tilt angle  of 3231986_3 by 10 degrees
- `C3`: Adjust the azimuth of 3231986_3 by 50 degrees
- `C4`: Lift the tilt angle of 3248128_1 by 10 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248128_1
- `C6`: Press down the tilt angle of 3248128_1 by 10 degrees
- `C7`: Decrease transmission power for 3248128_1
- `C8`: Insufficient data; more data is needed for judgment. **← 정답**
- `C9`: Decrease A3 Offset threshold for 3231986_3
- `C10`: Increase transmission power for 3248128_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231986_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248128_1
- `C13`: Add neighbor relationship between 3248128_1 and 3231986_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231986_3
- `C15`: Add neighbor relationship between 3244815_4 and 3231986_3
- `C16`: Decrease transmission power for 3231986_3
- `C17`: Adjust the azimuth of 3248128_1 by 50 degrees
- `C18`: Increase A3 Offset threshold for 3248128_1
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle  of 3231986_3 by 10 degrees
- `C21`: Increase A3 Offset threshold for 3231986_3
- `C22`: Increase transmission power for 3231986_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.928 | MS1 | 121.4656622922 | 31.1446296911 | 832 | 504990 | -89.05 | 14.16 | 411.57 | 0.04 | 2.05 | 1588 |
| 2024-09-20 22:21:32.753 | MS1 | 121.4656587231 | 31.1446371075 | 832 | 504990 | -87.84 | 14.58 | 412.83 | 0.15 | 2.61 | 1589 |
| 2024-09-20 22:21:33.702 | MS1 | 121.4656711487 | 31.1446322991 | 832 | 504990 | -87.74 | 16.24 | 314.57 | 0.17 | 2.66 | 1584 |
| 2024-09-20 22:21:34.505 | MS1 | 121.4656660708 | 31.1446250936 | 832 | 504990 | -91.51 | 16.43 | 67.97 | 0.09 | 2.47 | 1582 |
| 2024-09-20 22:21:35.182 | MS1 | 121.4656703036 | 31.1446237329 | 832 | 504990 | -91.05 | 15.55 | 67.47 | 0.03 | 2.18 | 1586 |
| 2024-09-20 22:21:36.339 | MS1 | 121.4656756586 | 31.1446284213 | 832 | 504990 | -85.56 | 15.49 | 56.27 | 0.10 | 2.05 | 1592 |
| 2024-09-20 22:21:37.578 | MS1 | 121.4656746620 | 31.1446317730 | 832 | 504990 | -90.19 | 10.05 | 54.75 | 0.07 | 2.79 | 1561 |
| 2024-09-20 22:21:38.914 | MS1 | 121.4656640114 | 31.1446361398 | 832 | 504990 | -92.53 | 12.94 | 65.88 | 0.12 | 2.70 | 1574 |
| 2024-09-20 22:21:39.308 | MS1 | 121.4656685629 | 31.1446207119 | 832 | 504990 | -92.72 | 9.16 | 69.49 | 0.10 | 2.96 | 1583 |
| 2024-09-20 22:21:40.977 | MS1 | 121.4656623379 | 31.1446285799 | 832 | 504990 | -92.55 | 11.31 | 406.13 | 0.12 | 2.77 | 1599 |
| 2024-09-20 22:21:41.224 | MS1 | 121.4656627406 | 31.1446255344 | 832 | 504990 | -90.28 | 9.70 | 371.07 | 0.19 | 2.21 | 1561 |
| 2024-09-20 22:21:42.770 | MS1 | 121.4656619631 | 31.1446372416 | 832 | 504990 | -89.03 | 11.49 | 469.25 | 0.06 | 2.49 | 1598 |

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
| 3211068 | 2 | 121.4695062944 | 31.1550242149 | 172 | 13 | 6 | 35.4 | TDD | 920 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3231986 | 3 | 121.4705217094 | 31.1465581741 | 295 | 9 | 6 | 47.5 | TDD | 774 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3244815 | 4 | 121.4722373987 | 31.1508589834 | 346 | 10 | 5 | 36.5 | TDD | 919 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3248128 | 1 | 121.4646420052 | 31.1485813694 | 262 | 14 | 4 | 37.3 | TDD | 832 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.233 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.363 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.363 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.017 | NREventA3 | measId:2;ServCellPCI:108;Se... |
| 2024-09-20 22:21:38.257 | NRHandoverAttempt | SourcePCI:108;SourceNR-ARFC... |
| 2024-09-20 22:21:38.289 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.301 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.418 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.418 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3248128 | 1 | 78.8661 | 84.2411 | -116.1069 | 19.8254 | 95.9437 | 0.0087 | 0.0154 |
| 2024_09_19 22:00 | 3211068 | 2 | 79.3693 | 86.0887 | -114.8060 | 8.0273 | 173.4855 | 0.0087 | 0.0159 |
| 2024_09_19 22:00 | 3231986 | 3 | 79.9600 | 76.9093 | -117.1268 | 13.7021 | 101.0782 | 0.0084 | 0.0179 |
| 2024_09_19 22:00 | 3244815 | 4 | 94.3470 | 79.4070 | -116.0707 | 12.6031 | 126.6446 | 0.0019 | 0.0000 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414989_69181FB6 | 504990 | 832 | -92.3 | 504990 | 774 | -100.0 | 504990 | 919 | -104.8 | 504990 | 920 |
| MR_1774414989_CF42A81B | 504990 | 832 | -91.0 | 504990 | 774 | -102.5 | 504990 | 919 | -103.4 | 504990 | 920 |
| MR_1774414989_FACE8A0E | 504990 | 832 | -90.6 | 504990 | 774 | -102.7 | 504990 | 919 | -102.0 | 504990 | 920 |
| MR_1774414989_3B611F81 | 504990 | 832 | -90.9 | 504990 | 774 | -102.2 | 504990 | 919 | -104.7 | 504990 | 920 |
| MR_1774414989_27B4AA98 | 504990 | 832 | -91.3 | 504990 | 774 | -102.5 | 504990 | 919 | -104.4 | 504990 | 920 |
| MR_1774414989_43CA8887 | 504990 | 832 | -90.4 | 504990 | 774 | -102.2 | 504990 | 919 | -104.7 | 504990 | 920 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1483: `6b8fe1cf-685...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6b8fe1cf-685f-48a7-92cd-b054d4574916` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease A3 Offset threshold for 3219570_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1483] topology](images/train_1483.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3270849_2
- `C2`: Decrease transmission power for 3219570_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270849_2
- `C4`: Press down the tilt angle  of 3270849_2 by 10 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Adjust the azimuth of 3219570_3 by 50 degrees
- `C7`: Increase transmission power for 3270849_2
- `C8`: Check test server and transmission issues
- `C9`: Increase transmission power for 3219570_3
- `C10`: Lift the tilt angle  of 3270849_2 by 10 degrees
- `C11`: Press down the tilt angle of 3219570_3 by 8 degrees
- `C12`: Add neighbor relationship between 3234666_1 and 3270849_2
- `C13`: Lift the tilt angle of 3219570_3 by 8 degrees
- `C14`: Add neighbor relationship between 3219570_3 and 3270849_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219570_3
- `C16`: Decrease A3 Offset threshold for 3270849_2
- `C17`: Decrease transmission power for 3270849_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219570_3
- `C19`: Adjust the azimuth of 3270849_2 by 50 degrees
- `C20`: Decrease A3 Offset threshold for 3219570_3 **← 정답**
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270849_2
- `C22`: Increase A3 Offset threshold for 3219570_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.594 | MS1 | 121.4656724398 | 31.1446256291 | 404 | 504990 | -78.80 | 14.10 | 594.09 | 0.03 | 2.93 | 1571 |
| 2024-09-20 22:21:32.683 | MS1 | 121.4656680835 | 31.1446229194 | 404 | 504990 | -83.33 | 13.27 | 514.63 | 0.01 | 2.16 | 1567 |
| 2024-09-20 22:21:33.832 | MS1 | 121.4656672344 | 31.1446287989 | 404 | 504990 | -75.35 | 13.85 | 320.25 | 0.03 | 3.00 | 1576 |
| 2024-09-20 22:21:34.373 | MS1 | 121.4656580364 | 31.1446266612 | 404 | 504990 | -84.33 | -0.92 | 53.95 | 0.13 | 1.24 | 1597 |
| 2024-09-20 22:21:35.586 | MS1 | 121.4656749287 | 31.1446277280 | 404 | 504990 | -89.26 | -0.21 | 64.96 | 0.18 | 1.10 | 1577 |
| 2024-09-20 22:21:36.775 | MS1 | 121.4656754564 | 31.1446214501 | 404 | 504990 | -88.94 | -2.60 | 55.21 | 0.17 | 1.29 | 1577 |
| 2024-09-20 22:21:37.292 | MS1 | 121.4656685886 | 31.1446378539 | 404 | 504990 | -85.85 | -0.71 | 39.22 | 0.18 | 1.18 | 1597 |
| 2024-09-20 22:21:38.613 | MS1 | 121.4656642569 | 31.1446374975 | 404 | 504990 | -86.99 | -1.57 | 35.58 | 0.12 | 1.12 | 1580 |
| 2024-09-20 22:21:39.994 | MS1 | 121.4656726082 | 31.1446226470 | 811 | 504990 | -83.80 | 13.86 | 267.36 | 0.08 | 1.36 | 1594 |
| 2024-09-20 22:21:40.529 | MS1 | 121.4656751309 | 31.1446188385 | 811 | 504990 | -82.64 | 13.32 | 517.83 | 0.09 | 2.64 | 1599 |
| 2024-09-20 22:21:41.961 | MS1 | 121.4656776524 | 31.1446215126 | 811 | 504990 | -84.04 | 12.24 | 355.80 | 0.14 | 2.79 | 1584 |
| 2024-09-20 22:21:42.783 | MS1 | 121.4656631644 | 31.1446203146 | 811 | 504990 | -78.39 | 16.26 | 491.10 | 0.02 | 2.22 | 1578 |

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
| 3219570 | 3 | 121.4750516900 | 31.1440279140 | 113 | 6 | 7 | 34.3 | TDD | 404 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3233669 | 4 | 121.4757927158 | 31.1526495989 | 99 | 12 | 8 | 42.8 | TDD | 77 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3234666 | 1 | 121.4669160338 | 31.1485424803 | 174 | 2 | 6 | 20.1 | TDD | 713 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3270849 | 2 | 121.4655885827 | 31.1503729310 | 313 | 7 | 2 | 39.7 | TDD | 811 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.909 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.018 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.018 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.772 | NREventA3 | measId:2;ServCellPCI:270;Se... |
| 2024-09-20 22:21:38.012 | NRHandoverAttempt | SourcePCI:270;SourceNR-ARFC... |
| 2024-09-20 22:21:38.046 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.060 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.189 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.189 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234666 | 1 | 14.3831 | 13.8740 | -115.8750 | 10.6373 | 128.9130 | 0.0034 | 0.0103 |
| 2024_09_20 22:00 | 3270849 | 2 | 15.6537 | 17.8724 | -114.5350 | 14.4585 | 116.7023 | 0.0086 | 0.0152 |
| 2024_09_20 22:00 | 3219570 | 3 | 6.1617 | 16.0944 | -116.3094 | 6.3598 | 140.1647 | 0.0009 | 0.1421 |
| 2024_09_20 22:00 | 3233669 | 4 | 15.4429 | 14.4872 | -117.4488 | 12.1441 | 164.8089 | 0.0130 | 0.0047 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412682_64CC2A0A | 504990 | 811 | -80.1 | 504990 | 404 | -84.4 | 504990 | 713 | -87.9 | 504990 | 77 |
| MR_1774412682_E94CBB47 | 504990 | 811 | -79.7 | 504990 | 404 | -85.5 | 504990 | 713 | -88.1 | 504990 | 77 |
| MR_1774412682_EE24428B | 504990 | 404 | -84.7 | 504990 | 811 | -81.7 | 504990 | 713 | -84.9 | 504990 | 77 |
| MR_1774412682_6AF60954 | 504990 | 811 | -79.5 | 504990 | 404 | -85.6 | 504990 | 713 | -84.4 | 504990 | 77 |
| MR_1774412682_C29D415D | 504990 | 811 | -79.0 | 504990 | 404 | -84.9 | 504990 | 713 | -86.6 | 504990 | 77 |
| MR_1774412682_A6C89245 | 504990 | 811 | -78.3 | 504990 | 404 | -85.2 | 504990 | 713 | -87.9 | 504990 | 77 |
| MR_1774412682_7E6B83D4 | 504990 | 811 | -78.6 | 504990 | 404 | -84.9 | 504990 | 713 | -86.0 | 504990 | 77 |
| MR_1774412682_4A42AF36 | 504990 | 404 | -84.9 | 504990 | 811 | -79.4 | 504990 | 713 | -87.8 | 504990 | 77 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1484: `c98edf06-d76...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c98edf06-d76d-48ab-94a3-ddbb1890a8df` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1484] topology](images/train_1484.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238161_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270429_1
- `C3`: Press down the tilt angle of 3238161_3 by 7 degrees
- `C4`: Lift the tilt angle of 3238161_3 by 7 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238161_3
- `C6`: Decrease transmission power for 3270429_1
- `C7`: Increase A3 Offset threshold for 3270429_1
- `C8`: Add neighbor relationship between 3238161_3 and 3270429_1
- `C9`: Increase transmission power for 3238161_3
- `C10`: Decrease transmission power for 3238161_3
- `C11`: Add neighbor relationship between 3259920_4 and 3270429_1
- `C12`: Decrease A3 Offset threshold for 3238161_3
- `C13`: Check test server and transmission issues
- `C14`: Adjust the azimuth of 3238161_3 by 50 degrees
- `C15`: Increase transmission power for 3270429_1
- `C16`: Adjust the azimuth of 3270429_1 by 50 degrees
- `C17`: Insufficient data; more data is needed for judgment. **← 정답**
- `C18`: Increase A3 Offset threshold for 3238161_3
- `C19`: Press down the tilt angle  of 3270429_1 by 10 degrees
- `C20`: Decrease A3 Offset threshold for 3270429_1
- `C21`: Lift the tilt angle  of 3270429_1 by 10 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270429_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.562 | MS1 | 121.4656590612 | 31.1446358874 | 980 | 504990 | -89.16 | 17.71 | 582.41 | 0.18 | 2.68 | 1589 |
| 2024-09-20 22:21:32.532 | MS1 | 121.4656637443 | 31.1446228859 | 980 | 504990 | -87.52 | 15.95 | 503.24 | 0.12 | 2.35 | 1583 |
| 2024-09-20 22:21:33.391 | MS1 | 121.4656685953 | 31.1446224054 | 980 | 504990 | -90.69 | 12.72 | 410.16 | 0.17 | 2.92 | 1574 |
| 2024-09-20 22:21:34.938 | MS1 | 121.4656686715 | 31.1446356951 | 980 | 504990 | -90.23 | 14.40 | 80.37 | 0.20 | 2.18 | 1599 |
| 2024-09-20 22:21:35.578 | MS1 | 121.4656650433 | 31.1446275426 | 980 | 504990 | -87.37 | 16.95 | 94.26 | 0.14 | 2.09 | 1583 |
| 2024-09-20 22:21:36.974 | MS1 | 121.4656744501 | 31.1446218867 | 980 | 504990 | -90.90 | 17.78 | 75.28 | 0.18 | 2.67 | 1585 |
| 2024-09-20 22:21:37.192 | MS1 | 121.4656581777 | 31.1446261658 | 980 | 504990 | -93.13 | 12.24 | 105.61 | 0.03 | 2.56 | 1590 |
| 2024-09-20 22:21:38.956 | MS1 | 121.4656591002 | 31.1446303018 | 980 | 504990 | -93.66 | 11.07 | 89.86 | 0.11 | 2.82 | 1574 |
| 2024-09-20 22:21:39.954 | MS1 | 121.4656634031 | 31.1446216566 | 980 | 504990 | -89.87 | 7.99 | 69.67 | 0.18 | 2.07 | 1584 |
| 2024-09-20 22:21:40.276 | MS1 | 121.4656582774 | 31.1446201630 | 980 | 504990 | -92.94 | 11.17 | 356.08 | 0.17 | 2.26 | 1566 |
| 2024-09-20 22:21:41.561 | MS1 | 121.4656670799 | 31.1446274346 | 980 | 504990 | -91.47 | 11.58 | 479.20 | 0.04 | 2.86 | 1595 |
| 2024-09-20 22:21:42.786 | MS1 | 121.4656710791 | 31.1446329677 | 980 | 504990 | -90.90 | 7.67 | 592.52 | 0.19 | 2.62 | 1567 |

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
| 3232183 | 2 | 121.4664650469 | 31.1456806380 | 335 | 12 | 11 | 25.0 | TDD | 882 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3238161 | 3 | 121.4717421202 | 31.1551636493 | 58 | 6 | 6 | 15.1 | TDD | 980 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3259920 | 4 | 121.4720277654 | 31.1510516399 | 183 | 6 | 4 | 25.6 | TDD | 753 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3270429 | 1 | 121.4744745254 | 31.1444648756 | 186 | 12 | 11 | 48.3 | TDD | 465 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.096 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.113 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.261 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.261 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.965 | NREventA3 | measId:2;ServCellPCI:761;Se... |
| 2024-09-20 22:21:38.205 | NRHandoverAttempt | SourcePCI:761;SourceNR-ARFC... |
| 2024-09-20 22:21:38.251 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.261 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.381 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.381 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3270429 | 1 | 87.8656 | 75.3419 | -117.5536 | 11.0531 | 174.3072 | 0.0010 | 0.0056 |
| 2024_09_19 22:00 | 3232183 | 2 | 78.5225 | 77.9130 | -114.0693 | 5.8695 | 141.2458 | 0.0157 | 0.0076 |
| 2024_09_19 22:00 | 3238161 | 3 | 93.5785 | 90.9620 | -115.5340 | 11.6704 | 141.6723 | 0.0076 | 0.0119 |
| 2024_09_19 22:00 | 3259920 | 4 | 90.3481 | 79.2069 | -114.2299 | 15.5574 | 171.1830 | 0.0052 | 0.0134 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414815_DAD81E14 | 504990 | 980 | -90.2 | 504990 | 465 | -90.0 | 504990 | 753 | -96.3 | 504990 | 882 |
| MR_1774414815_623C235F | 504990 | 980 | -88.7 | 504990 | 465 | -93.0 | 504990 | 753 | -95.8 | 504990 | 882 |
| MR_1774414815_3DD5A9BC | 504990 | 980 | -90.6 | 504990 | 465 | -92.1 | 504990 | 753 | -99.0 | 504990 | 882 |
| MR_1774414815_DA3198DB | 504990 | 980 | -91.3 | 504990 | 465 | -90.2 | 504990 | 753 | -97.2 | 504990 | 882 |
| MR_1774414815_CE8D78EF | 504990 | 980 | -90.4 | 504990 | 465 | -91.1 | 504990 | 753 | -98.5 | 504990 | 882 |
| MR_1774414815_38BC108C | 504990 | 980 | -90.3 | 504990 | 465 | -93.2 | 504990 | 753 | -96.4 | 504990 | 882 |
| MR_1774414815_88E376BA | 504990 | 980 | -89.7 | 504990 | 465 | -92.4 | 504990 | 753 | -95.2 | 504990 | 882 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1485: `2746e95c-4e5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2746e95c-4e51-4c3d-8c8d-6a9586b7b029` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Lift the tilt angle  of 3276555_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1485] topology](images/train_1485.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3228396_2 by 5 degrees
- `C2`: Adjust the azimuth of 3276555_4 by 50 degrees
- `C3`: Adjust the azimuth of 3228396_2 by 16 degrees
- `C4`: Check test server and transmission issues
- `C5`: Add neighbor relationship between 3228396_2 and 3239251_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239251_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228396_2
- `C8`: Decrease A3 Offset threshold for 3239251_3
- `C9`: Increase transmission power for 3239251_3
- `C10`: Lift the tilt angle  of 3276555_4 by 10 degrees **← 정답**
- `C11`: Lift the tilt angle of 3228396_2 by 5 degrees
- `C12`: Increase A3 Offset threshold for 3239251_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239251_3
- `C14`: Press down the tilt angle  of 3276555_4 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3228396_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228396_2
- `C18`: Decrease transmission power for 3239251_3
- `C19`: Add neighbor relationship between 3276555_4 and 3239251_3
- `C20`: Increase A3 Offset threshold for 3228396_2
- `C21`: Decrease transmission power for 3228396_2
- `C22`: Increase transmission power for 3228396_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.523 | MS1 | 121.4656669827 | 31.1446185579 | 71 | 504990 | -91.76 | 14.00 | 466.16 | 0.04 | 2.94 | 1561 |
| 2024-09-20 22:21:32.889 | MS1 | 121.4656695420 | 31.1446275751 | 71 | 504990 | -86.89 | 12.85 | 567.36 | 0.15 | 2.47 | 1588 |
| 2024-09-20 22:21:33.791 | MS1 | 121.4656753825 | 31.1446292433 | 71 | 504990 | -87.24 | 17.72 | 573.44 | 0.09 | 2.02 | 1578 |
| 2024-09-20 22:21:34.313 | MS1 | 121.4656594354 | 31.1446315095 | 71 | 504990 | -88.01 | 15.26 | 80.30 | 0.20 | 2.27 | 1589 |
| 2024-09-20 22:21:35.938 | MS1 | 121.4656590151 | 31.1446335051 | 71 | 504990 | -89.96 | 17.06 | 73.20 | 0.12 | 2.53 | 1576 |
| 2024-09-20 22:21:36.553 | MS1 | 121.4656701887 | 31.1446279640 | 71 | 504990 | -87.29 | 14.32 | 62.37 | 0.01 | 2.92 | 1582 |
| 2024-09-20 22:21:37.143 | MS1 | 121.4656662728 | 31.1446363481 | 71 | 504990 | -90.50 | 9.56 | 89.48 | 0.09 | 2.25 | 1596 |
| 2024-09-20 22:21:38.449 | MS1 | 121.4656650979 | 31.1446293806 | 71 | 504990 | -89.83 | 8.64 | 53.11 | 0.16 | 2.68 | 1594 |
| 2024-09-20 22:21:39.808 | MS1 | 121.4656692615 | 31.1446237662 | 71 | 504990 | -92.18 | 11.79 | 77.95 | 0.15 | 2.88 | 1579 |
| 2024-09-20 22:21:40.933 | MS1 | 121.4656599414 | 31.1446275446 | 71 | 504990 | -90.17 | 11.15 | 318.54 | 0.16 | 2.83 | 1572 |
| 2024-09-20 22:21:41.573 | MS1 | 121.4656655159 | 31.1446182855 | 71 | 504990 | -92.75 | 10.35 | 362.38 | 0.12 | 2.10 | 1560 |
| 2024-09-20 22:21:42.129 | MS1 | 121.4656612768 | 31.1446231061 | 71 | 504990 | -89.65 | 7.30 | 306.29 | 0.05 | 2.21 | 1573 |

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
| 3228396 | 2 | 121.4747305683 | 31.1482222049 | 261 | 3 | 11 | 37.4 | TDD | 71 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3239251 | 3 | 121.4699977839 | 31.1465249833 | 190 | 7 | 6 | 45.0 | TDD | 758 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3276555 | 4 | 121.4736594099 | 31.1545410079 | 133 | 7 | 5 | 33.5 | TDD | 407 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3279906 | 1 | 121.4683017073 | 31.1444253735 | 355 | 15 | 9 | 16.1 | TDD | 291 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.557 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.572 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.716 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.716 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.425 | NREventA3 | measId:2;ServCellPCI:871;Se... |
| 2024-09-20 22:21:38.665 | NRHandoverAttempt | SourcePCI:871;SourceNR-ARFC... |
| 2024-09-20 22:21:38.705 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.717 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.856 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.856 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279906 | 1 | 5.3579 | 19.4411 | -116.1147 | 12.4643 | 119.3361 | 0.0084 | 0.0001 |
| 2024_09_20 22:00 | 3228396 | 2 | 92.3591 | 76.5624 | -116.4329 | 13.6324 | 151.3117 | 0.0043 | 0.0020 |
| 2024_09_20 22:00 | 3239251 | 3 | 16.8140 | 16.6343 | -114.2990 | 11.9656 | 188.8815 | 0.0079 | 0.0097 |
| 2024_09_20 22:00 | 3276555 | 4 | 10.9093 | 18.6607 | -114.1192 | 14.8225 | 159.0595 | 0.0029 | 0.0173 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412094_6DBA9BF4 | 504990 | 71 | -89.6 | 504990 | 758 | -89.6 | 504990 | 407 | -102.6 | 504990 | 291 |
| MR_1774412094_F8E7C7CB | 504990 | 71 | -86.5 | 504990 | 758 | -92.4 | 504990 | 407 | -100.0 | 504990 | 291 |
| MR_1774412094_61ACBCE5 | 504990 | 71 | -87.3 | 504990 | 758 | -91.8 | 504990 | 407 | -101.1 | 504990 | 291 |
| MR_1774412094_42F42AF4 | 504990 | 71 | -86.2 | 504990 | 758 | -90.6 | 504990 | 407 | -102.4 | 504990 | 291 |
| MR_1774412094_817978B6 | 504990 | 71 | -86.8 | 504990 | 758 | -90.4 | 504990 | 407 | -100.6 | 504990 | 291 |
| MR_1774412094_8D5A9B23 | 504990 | 71 | -89.4 | 504990 | 758 | -90.9 | 504990 | 407 | -102.8 | 504990 | 291 |
| MR_1774412094_EF5F085F | 504990 | 71 | -87.9 | 504990 | 758 | -89.5 | 504990 | 407 | -102.3 | 504990 | 291 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1486: `ce7a2d0a-917...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ce7a2d0a-9173-48c7-bb69-9ad10479f6cc` |
| Tag | **multiple-answer** |
| 정답 | **C12|C19** |
| C12 의미 | Increase transmission power for 3237262_4 |
| C19 의미 | Adjust the azimuth of 3237262_4 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1486] topology](images/train_1486.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237262_4
- `C3`: Decrease transmission power for 3237262_4
- `C4`: Lift the tilt angle  of 3233656_3 by 3 degrees
- `C5`: Add neighbor relationship between 3237262_4 and 3233656_3
- `C6`: Decrease A3 Offset threshold for 3237262_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233656_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233656_3
- `C9`: Press down the tilt angle of 3237262_4 by 10 degrees
- `C10`: Add neighbor relationship between 3221566_1 and 3233656_3
- `C11`: Increase A3 Offset threshold for 3237262_4
- `C12`: Increase transmission power for 3237262_4 **← 정답**
- `C13`: Adjust the azimuth of 3233656_3 by 32 degrees
- `C14`: Decrease A3 Offset threshold for 3233656_3
- `C15`: Increase A3 Offset threshold for 3233656_3
- `C16`: Increase transmission power for 3233656_3
- `C17`: Lift the tilt angle of 3237262_4 by 10 degrees
- `C18`: Decrease transmission power for 3233656_3
- `C19`: Adjust the azimuth of 3237262_4 by 50 degrees **← 정답**
- `C20`: Press down the tilt angle  of 3233656_3 by 3 degrees
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237262_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.183 | MS1 | 121.4656623596 | 31.1446343807 | 707 | 504990 | -85.54 | 12.64 | 309.41 | 0.15 | 2.53 | 1591 |
| 2024-09-20 22:21:32.389 | MS1 | 121.4656699556 | 31.1446369059 | 707 | 504990 | -87.25 | 15.72 | 537.96 | 0.16 | 2.16 | 1587 |
| 2024-09-20 22:21:33.959 | MS1 | 121.4656601272 | 31.1446239791 | 707 | 504990 | -85.50 | 13.54 | 543.42 | 0.12 | 2.89 | 1593 |
| 2024-09-20 22:21:34.787 | MS1 | 121.4656633249 | 31.1446376797 | 707 | 504990 | -101.30 | 0.79 | 64.01 | 0.01 | 1.47 | 1595 |
| 2024-09-20 22:21:35.761 | MS1 | 121.4656629486 | 31.1446229575 | 707 | 504990 | -103.69 | -1.49 | 24.50 | 0.02 | 1.22 | 1585 |
| 2024-09-20 22:21:36.247 | MS1 | 121.4656775324 | 31.1446305032 | 707 | 504990 | -101.66 | -0.89 | 57.67 | 0.02 | 1.03 | 1572 |
| 2024-09-20 22:21:37.883 | MS1 | 121.4656638200 | 31.1446277324 | 707 | 504990 | -103.78 | -0.12 | 43.28 | 0.12 | 1.05 | 1593 |
| 2024-09-20 22:21:38.627 | MS1 | 121.4656736422 | 31.1446279143 | 707 | 504990 | -101.16 | 0.77 | 76.51 | 0.19 | 1.44 | 1583 |
| 2024-09-20 22:21:39.948 | MS1 | 121.4656764296 | 31.1446200741 | 707 | 504990 | -107.55 | 0.78 | 32.62 | 0.04 | 1.00 | 1568 |
| 2024-09-20 22:21:40.966 | MS1 | 121.4656679221 | 31.1446288737 | 707 | 504990 | -86.76 | 13.61 | 515.82 | 0.17 | 2.40 | 1565 |
| 2024-09-20 22:21:41.172 | MS1 | 121.4656590458 | 31.1446239812 | 707 | 504990 | -86.48 | 14.68 | 475.83 | 0.14 | 2.69 | 1583 |
| 2024-09-20 22:21:42.440 | MS1 | 121.4656583167 | 31.1446243732 | 707 | 504990 | -88.78 | 13.83 | 414.65 | 0.19 | 2.13 | 1577 |

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
| 3221566 | 1 | 121.4687808254 | 31.1465332241 | 250 | 4 | 12 | 48.8 | TDD | 200 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3233656 | 3 | 121.4653953757 | 31.1524501182 | 146 | 1 | 8 | 34.5 | TDD | 650 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3237262 | 4 | 121.4699638823 | 31.1479599507 | 285 | 10 | 2 | 31.0 | TDD | 707 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3273664 | 2 | 121.4691575842 | 31.1539673338 | 200 | 1 | 6 | 15.1 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.210 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.226 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.331 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.331 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.601 | NREventA2 | measId:1;ServCellPCI:785;Se... |
| 2024-09-20 22:21:34.737 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221566 | 1 | 7.5513 | 9.3980 | -117.7605 | 17.4626 | 139.0746 | 0.0107 | 0.0088 |
| 2024_09_20 22:00 | 3273664 | 2 | 10.1578 | 15.6898 | -116.1683 | 19.4270 | 172.9155 | 0.0048 | 0.0065 |
| 2024_09_20 22:00 | 3233656 | 3 | 13.0658 | 11.6586 | -114.5510 | 9.8517 | 133.4994 | 0.0060 | 0.0025 |
| 2024_09_20 22:00 | 3237262 | 4 | 17.4408 | 11.8269 | -116.8059 | 15.5108 | 146.1780 | 0.1302 | 0.0127 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416621_DAD40D0B | 504990 | 707 | -101.0 | 504990 | 650 | -106.3 | 504990 | 200 | -110.6 | 504990 | 129 |
| MR_1774416621_87AEA069 | 504990 | 707 | -101.2 | 504990 | 650 | -105.4 | 504990 | 200 | -111.1 | 504990 | 129 |
| MR_1774416621_026C290B | 504990 | 707 | -100.2 | 504990 | 650 | -106.3 | 504990 | 200 | -112.7 | 504990 | 129 |
| MR_1774416621_C6CBBA4D | 504990 | 707 | -99.3 | 504990 | 650 | -107.8 | 504990 | 200 | -109.9 | 504990 | 129 |
| MR_1774416621_A7280EB7 | 504990 | 707 | -103.0 | 504990 | 650 | -105.4 | 504990 | 200 | -110.2 | 504990 | 129 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1487: `a7550437-a38...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a7550437-a388-425b-ac24-da4a8d85f390` |
| Tag | **multiple-answer** |
| 정답 | **C6|C20** |
| C6 의미 | Press down the tilt angle  of 3216018_2 by 5 degrees |
| C20 의미 | Decrease transmission power for 3216018_2 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1487] topology](images/train_1487.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3234955_4
- `C2`: Decrease A3 Offset threshold for 3216018_2
- `C3`: Decrease transmission power for 3234955_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216018_2
- `C5`: Decrease A3 Offset threshold for 3234955_4
- `C6`: Press down the tilt angle  of 3216018_2 by 5 degrees **← 정답**
- `C7`: Check test server and transmission issues
- `C8`: Add neighbor relationship between 3234955_4 and 3216018_2
- `C9`: Adjust the azimuth of 3216018_2 by 11 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase A3 Offset threshold for 3216018_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234955_4
- `C13`: Lift the tilt angle  of 3216018_2 by 5 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216018_2
- `C15`: Press down the tilt angle of 3234955_4 by 5 degrees
- `C16`: Increase transmission power for 3234955_4
- `C17`: Increase transmission power for 3216018_2
- `C18`: Adjust the azimuth of 3234955_4 by 31 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234955_4
- `C20`: Decrease transmission power for 3216018_2 **← 정답**
- `C21`: Add neighbor relationship between 3247438_3 and 3216018_2
- `C22`: Lift the tilt angle of 3234955_4 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.777 | MS1 | 121.4656705888 | 31.1446290124 | 489 | 504990 | -75.12 | 14.68 | 415.94 | 0.07 | 2.15 | 1578 |
| 2024-09-20 22:21:32.626 | MS1 | 121.4656723578 | 31.1446269772 | 489 | 504990 | -76.42 | 14.54 | 560.07 | 0.14 | 2.76 | 1585 |
| 2024-09-20 22:21:33.852 | MS1 | 121.4656715759 | 31.1446290320 | 489 | 504990 | -75.70 | 14.27 | 563.46 | 0.16 | 2.29 | 1573 |
| 2024-09-20 22:21:34.839 | MS1 | 121.4656648096 | 31.1446199820 | 489 | 504990 | -88.73 | 0.44 | 82.29 | 0.10 | 1.02 | 1581 |
| 2024-09-20 22:21:35.428 | MS1 | 121.4656589867 | 31.1446320470 | 489 | 504990 | -88.43 | 3.22 | 58.08 | 0.16 | 1.05 | 1597 |
| 2024-09-20 22:21:36.813 | MS1 | 121.4656663552 | 31.1446260163 | 489 | 504990 | -86.80 | 0.23 | 85.27 | 0.07 | 1.17 | 1591 |
| 2024-09-20 22:21:37.126 | MS1 | 121.4656593725 | 31.1446292236 | 489 | 504990 | -93.94 | 1.94 | 73.35 | 0.01 | 1.08 | 1560 |
| 2024-09-20 22:21:38.567 | MS1 | 121.4656754611 | 31.1446218053 | 489 | 504990 | -87.96 | 3.90 | 61.32 | 0.14 | 1.45 | 1566 |
| 2024-09-20 22:21:39.917 | MS1 | 121.4656727579 | 31.1446190777 | 489 | 504990 | -94.67 | 0.16 | 72.09 | 0.17 | 1.31 | 1587 |
| 2024-09-20 22:21:40.631 | MS1 | 121.4656711616 | 31.1446207148 | 489 | 504990 | -75.21 | 12.16 | 351.99 | 0.15 | 2.70 | 1599 |
| 2024-09-20 22:21:41.485 | MS1 | 121.4656776073 | 31.1446245484 | 489 | 504990 | -77.64 | 16.84 | 432.16 | 0.10 | 2.88 | 1594 |
| 2024-09-20 22:21:42.976 | MS1 | 121.4656715412 | 31.1446195762 | 489 | 504990 | -79.81 | 14.99 | 300.49 | 0.10 | 2.60 | 1574 |

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
| 3216018 | 2 | 121.4735186179 | 31.1451183554 | 277 | 1 | 7 | 48.2 | TDD | 619 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3234955 | 4 | 121.4726347322 | 31.1489463353 | 265 | 2 | 4 | 45.9 | TDD | 489 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3242816 | 1 | 121.4648333229 | 31.1529447825 | 58 | 6 | 2 | 41.0 | TDD | 345 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3247438 | 3 | 121.4756561858 | 31.1474113552 | 69 | 9 | 6 | 31.8 | TDD | 388 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.766 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.784 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.906 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.906 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242816 | 1 | 12.4880 | 9.9940 | -115.0762 | 14.3966 | 93.4266 | 0.0084 | 0.0002 |
| 2024_09_20 22:00 | 3216018 | 2 | 15.2300 | 5.1892 | -114.8380 | 17.6519 | 136.7135 | 0.0116 | 0.0136 |
| 2024_09_20 22:00 | 3247438 | 3 | 7.4736 | 5.0556 | -117.6362 | 18.4300 | 129.0772 | 0.0119 | 0.0131 |
| 2024_09_20 22:00 | 3234955 | 4 | 10.9809 | 13.2797 | -108.9618 | 16.1793 | 119.9013 | 0.0107 | 0.0020 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415373_2F95B38B | 504990 | 619 | -87.2 | 504990 | 489 | -88.6 | 504990 | 388 | -88.8 | 504990 | 345 |
| MR_1774415373_9296AD21 | 504990 | 489 | -90.1 | 504990 | 619 | -86.4 | 504990 | 388 | -90.2 | 504990 | 345 |
| MR_1774415373_69781650 | 504990 | 489 | -89.3 | 504990 | 619 | -88.9 | 504990 | 388 | -92.1 | 504990 | 345 |
| MR_1774415373_D2D160BB | 504990 | 489 | -87.8 | 504990 | 619 | -86.3 | 504990 | 388 | -90.9 | 504990 | 345 |
| MR_1774415373_40ADCB45 | 504990 | 489 | -88.6 | 504990 | 619 | -88.8 | 504990 | 388 | -90.0 | 504990 | 345 |
| MR_1774415373_29278527 | 504990 | 489 | -89.0 | 504990 | 619 | -87.2 | 504990 | 388 | -90.2 | 504990 | 345 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1488: `f21e8dc6-a0c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f21e8dc6-a0c0-4452-b3dd-3347a629493f` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease A3 Offset threshold for 3277204_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1488] topology](images/train_1488.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3257504_4
- `C2`: Adjust the azimuth of 3257504_4 by 50 degrees
- `C3`: Increase A3 Offset threshold for 3277204_3
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257504_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257504_4
- `C7`: Decrease A3 Offset threshold for 3277204_3 **← 정답**
- `C8`: Check test server and transmission issues
- `C9`: Decrease A3 Offset threshold for 3257504_4
- `C10`: Press down the tilt angle  of 3257504_4 by 10 degrees
- `C11`: Lift the tilt angle  of 3257504_4 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277204_3
- `C13`: Add neighbor relationship between 3262019_2 and 3257504_4
- `C14`: Decrease transmission power for 3257504_4
- `C15`: Add neighbor relationship between 3277204_3 and 3257504_4
- `C16`: Increase transmission power for 3277204_3
- `C17`: Lift the tilt angle of 3277204_3 by 10 degrees
- `C18`: Increase transmission power for 3257504_4
- `C19`: Decrease transmission power for 3277204_3
- `C20`: Adjust the azimuth of 3277204_3 by 50 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277204_3
- `C22`: Press down the tilt angle of 3277204_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.759 | MS1 | 121.4656729681 | 31.1446282090 | 422 | 504990 | -75.15 | 16.51 | 376.80 | 0.18 | 2.69 | 1561 |
| 2024-09-20 22:21:32.159 | MS1 | 121.4656714134 | 31.1446338946 | 422 | 504990 | -81.12 | 13.12 | 300.36 | 0.16 | 2.17 | 1573 |
| 2024-09-20 22:21:33.931 | MS1 | 121.4656595259 | 31.1446194812 | 422 | 504990 | -78.15 | 15.31 | 349.67 | 0.08 | 2.34 | 1595 |
| 2024-09-20 22:21:34.315 | MS1 | 121.4656691928 | 31.1446186217 | 422 | 504990 | -92.18 | -3.58 | 59.75 | 0.10 | 1.20 | 1572 |
| 2024-09-20 22:21:35.427 | MS1 | 121.4656752886 | 31.1446318268 | 422 | 504990 | -92.43 | -2.42 | 75.63 | 0.04 | 1.33 | 1597 |
| 2024-09-20 22:21:36.949 | MS1 | 121.4656718425 | 31.1446186592 | 422 | 504990 | -90.02 | -2.59 | 46.35 | 0.10 | 1.18 | 1586 |
| 2024-09-20 22:21:37.980 | MS1 | 121.4656631793 | 31.1446237293 | 422 | 504990 | -88.04 | -1.49 | 49.96 | 0.18 | 1.23 | 1587 |
| 2024-09-20 22:21:38.731 | MS1 | 121.4656657455 | 31.1446326064 | 422 | 504990 | -90.30 | -1.23 | 46.98 | 0.20 | 1.06 | 1573 |
| 2024-09-20 22:21:39.824 | MS1 | 121.4656675786 | 31.1446259019 | 470 | 504990 | -78.55 | 16.72 | 295.52 | 0.19 | 1.32 | 1577 |
| 2024-09-20 22:21:40.335 | MS1 | 121.4656689750 | 31.1446256422 | 470 | 504990 | -75.81 | 16.46 | 503.02 | 0.08 | 2.53 | 1586 |
| 2024-09-20 22:21:41.942 | MS1 | 121.4656744141 | 31.1446241087 | 470 | 504990 | -82.76 | 16.17 | 535.70 | 0.15 | 2.68 | 1567 |
| 2024-09-20 22:21:42.852 | MS1 | 121.4656690471 | 31.1446275941 | 470 | 504990 | -80.61 | 13.40 | 477.52 | 0.12 | 2.60 | 1598 |

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
| 3236360 | 1 | 121.4644311736 | 31.1470001934 | 223 | 2 | 11 | 41.8 | TDD | 992 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3257504 | 4 | 121.4690685592 | 31.1533322521 | 97 | 9 | 11 | 46.6 | TDD | 470 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3262019 | 2 | 121.4703445300 | 31.1531469448 | 313 | 4 | 4 | 34.1 | TDD | 484 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3277204 | 3 | 121.4655436403 | 31.1463399433 | 322 | 5 | 4 | 25.4 | TDD | 422 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.255 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.271 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.374 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.374 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.108 | NREventA3 | measId:2;ServCellPCI:256;Se... |
| 2024-09-20 22:21:38.348 | NRHandoverAttempt | SourcePCI:256;SourceNR-ARFC... |
| 2024-09-20 22:21:38.397 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.409 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.527 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.527 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236360 | 1 | 19.9120 | 17.3464 | -116.7062 | 6.1616 | 151.4759 | 0.0195 | 0.0172 |
| 2024_09_20 22:00 | 3262019 | 2 | 13.4065 | 12.6036 | -116.2141 | 7.9763 | 118.3523 | 0.0120 | 0.0147 |
| 2024_09_20 22:00 | 3277204 | 3 | 6.9410 | 8.5742 | -114.2746 | 10.2203 | 140.3079 | 0.0160 | 0.1678 |
| 2024_09_20 22:00 | 3257504 | 4 | 16.6538 | 13.9089 | -117.1601 | 18.7854 | 198.1078 | 0.0034 | 0.0185 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413163_8C114B74 | 504990 | 422 | -92.9 | 504990 | 470 | -86.0 | 504990 | 484 | -88.0 | 504990 | 992 |
| MR_1774413163_6BF306EE | 504990 | 422 | -91.0 | 504990 | 470 | -85.4 | 504990 | 484 | -88.5 | 504990 | 992 |
| MR_1774413163_FACF6E90 | 504990 | 422 | -93.8 | 504990 | 470 | -85.2 | 504990 | 484 | -89.1 | 504990 | 992 |
| MR_1774413163_27B3A357 | 504990 | 470 | -85.0 | 504990 | 422 | -92.5 | 504990 | 484 | -85.7 | 504990 | 992 |
| MR_1774413163_D071463A | 504990 | 422 | -91.1 | 504990 | 470 | -86.9 | 504990 | 484 | -87.0 | 504990 | 992 |
| MR_1774413163_46066CE9 | 504990 | 422 | -92.8 | 504990 | 470 | -86.4 | 504990 | 484 | -86.0 | 504990 | 992 |
| MR_1774413163_17DA0F4A | 504990 | 470 | -84.8 | 504990 | 422 | -93.6 | 504990 | 484 | -88.8 | 504990 | 992 |
| MR_1774413163_EC337E01 | 504990 | 422 | -90.5 | 504990 | 470 | -88.7 | 504990 | 484 | -86.2 | 504990 | 992 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1489: `650cc6e2-9d0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `650cc6e2-9d02-4eec-a9e8-d55d25d6d61e` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1489] topology](images/train_1489.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3253018_1 by 10 degrees
- `C2`: Decrease transmission power for 3249471_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249471_3
- `C4`: Adjust the azimuth of 3249471_3 by 50 degrees
- `C5`: Lift the tilt angle of 3253018_1 by 10 degrees
- `C6`: Decrease transmission power for 3253018_1
- `C7`: Decrease A3 Offset threshold for 3249471_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249471_3
- `C9`: Increase A3 Offset threshold for 3253018_1
- `C10`: Increase transmission power for 3253018_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253018_1
- `C12`: Adjust the azimuth of 3253018_1 by 50 degrees
- `C13`: Lift the tilt angle  of 3249471_3 by 4 degrees
- `C14`: Decrease A3 Offset threshold for 3253018_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253018_1
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Press down the tilt angle  of 3249471_3 by 4 degrees
- `C18`: Add neighbor relationship between 3265721_4 and 3249471_3
- `C19`: Add neighbor relationship between 3253018_1 and 3249471_3
- `C20`: Increase A3 Offset threshold for 3249471_3
- `C21`: Increase transmission power for 3249471_3
- `C22`: Check test server and transmission issues **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.779 | MS1 | 121.4656671973 | 31.1446187771 | 193 | 504990 | -85.62 | 16.91 | 404.05 | 0.01 | 2.21 | 1580 |
| 2024-09-20 22:21:32.720 | MS1 | 121.4656614693 | 31.1446267864 | 193 | 504990 | -86.12 | 16.24 | 538.69 | 0.19 | 2.66 | 1572 |
| 2024-09-20 22:21:33.264 | MS1 | 121.4656622429 | 31.1446324791 | 193 | 504990 | -86.79 | 14.91 | 546.61 | 0.19 | 2.27 | 1583 |
| 2024-09-20 22:21:34.585 | MS1 | 121.4656640361 | 31.1446231308 | 193 | 504990 | -90.24 | 16.03 | 66.88 | 0.10 | 2.85 | 382 |
| 2024-09-20 22:21:35.289 | MS1 | 121.4656770591 | 31.1446366327 | 193 | 504990 | -89.12 | 14.24 | 74.79 | 0.02 | 2.06 | 410 |
| 2024-09-20 22:21:36.999 | MS1 | 121.4656622854 | 31.1446292712 | 193 | 504990 | -87.20 | 13.24 | 85.71 | 0.12 | 2.36 | 430 |
| 2024-09-20 22:21:37.266 | MS1 | 121.4656645730 | 31.1446207151 | 193 | 504990 | -93.32 | 11.20 | 59.95 | 0.17 | 2.27 | 362 |
| 2024-09-20 22:21:38.335 | MS1 | 121.4656640987 | 31.1446309925 | 193 | 504990 | -92.95 | 8.87 | 60.89 | 0.19 | 2.94 | 367 |
| 2024-09-20 22:21:39.752 | MS1 | 121.4656763126 | 31.1446352653 | 193 | 504990 | -92.00 | 12.21 | 69.14 | 0.12 | 2.35 | 395 |
| 2024-09-20 22:21:40.327 | MS1 | 121.4656588764 | 31.1446368761 | 193 | 504990 | -89.64 | 9.00 | 481.63 | 0.06 | 2.38 | 1582 |
| 2024-09-20 22:21:41.650 | MS1 | 121.4656669009 | 31.1446191788 | 193 | 504990 | -91.74 | 12.15 | 326.16 | 0.12 | 2.55 | 1571 |
| 2024-09-20 22:21:42.252 | MS1 | 121.4656732158 | 31.1446293772 | 193 | 504990 | -91.37 | 10.64 | 482.67 | 0.08 | 2.89 | 1574 |

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
| 3249471 | 3 | 121.4667133956 | 31.1548645418 | 89 | 2 | 6 | 34.3 | TDD | 339 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3253018 | 1 | 121.4726586951 | 31.1479600222 | 50 | 11 | 11 | 15.4 | TDD | 193 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3265721 | 4 | 121.4670242942 | 31.1553560355 | 257 | 14 | 6 | 28.8 | TDD | 284 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3277544 | 2 | 121.4658697095 | 31.1534890631 | 302 | 12 | 5 | 49.1 | TDD | 802 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.435 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.460 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.585 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.585 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.320 | NREventA3 | measId:2;ServCellPCI:322;Se... |
| 2024-09-20 22:21:38.560 | NRHandoverAttempt | SourcePCI:322;SourceNR-ARFC... |
| 2024-09-20 22:21:38.593 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.604 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.712 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.712 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253018 | 1 | 6.8863 | 16.4565 | -114.5140 | 11.1423 | 182.0373 | 0.0052 | 0.0052 |
| 2024_09_20 22:00 | 3277544 | 2 | 13.6151 | 19.1082 | -117.8898 | 11.4314 | 125.1130 | 0.0032 | 0.0053 |
| 2024_09_20 22:00 | 3249471 | 3 | 16.2032 | 17.5387 | -117.6709 | 18.2091 | 169.7482 | 0.0187 | 0.0119 |
| 2024_09_20 22:00 | 3265721 | 4 | 9.6031 | 12.9069 | -115.5894 | 6.6671 | 107.3942 | 0.0059 | 0.0010 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414173_887CC923 | 504990 | 193 | -90.4 | 504990 | 339 | -92.0 | 504990 | 284 | -100.9 | 504990 | 802 |
| MR_1774414173_C9139151 | 504990 | 193 | -90.0 | 504990 | 339 | -92.9 | 504990 | 284 | -104.2 | 504990 | 802 |
| MR_1774414173_61499C55 | 504990 | 193 | -91.1 | 504990 | 339 | -93.9 | 504990 | 284 | -101.8 | 504990 | 802 |
| MR_1774414173_F8A8FEE4 | 504990 | 193 | -91.5 | 504990 | 339 | -94.2 | 504990 | 284 | -100.7 | 504990 | 802 |
| MR_1774414173_FF697983 | 504990 | 193 | -88.4 | 504990 | 339 | -93.4 | 504990 | 284 | -103.7 | 504990 | 802 |
| MR_1774414173_140BC11D | 504990 | 193 | -90.0 | 504990 | 339 | -93.8 | 504990 | 284 | -103.2 | 504990 | 802 |
| MR_1774414173_86477D1D | 504990 | 193 | -89.8 | 504990 | 339 | -91.9 | 504990 | 284 | -101.2 | 504990 | 802 |

> *... 2개 열 생략 (전체 14열)*

---
