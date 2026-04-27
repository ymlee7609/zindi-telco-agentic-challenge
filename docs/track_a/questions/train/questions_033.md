# Track A 문제 분석 — train[320]~train[329]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[320] ~ train[329] (10개)

## 목차

1. [문제 320: `e9583506-e16...`](#320) — single-answer, 정답: C10
2. [문제 321: `a5952838-893...`](#321) — single-answer, 정답: C5
3. [문제 322: `6da63593-545...`](#322) — single-answer, 정답: C10
4. [문제 323: `d03c531d-5e2...`](#323) — single-answer, 정답: C7
5. [문제 324: `cec8a6f2-ea1...`](#324) — multiple-answer, 정답: C10|C18
6. [문제 325: `f0121c5b-4fd...`](#325) — single-answer, 정답: C20
7. [문제 326: `76451c5b-5a4...`](#326) — single-answer, 정답: C21
8. [문제 327: `2eeb2312-620...`](#327) — single-answer, 정답: C2
9. [문제 328: `0744f3f8-c76...`](#328) — single-answer, 정답: C20
10. [문제 329: `931eb354-210...`](#329) — single-answer, 정답: C22

---

### 문제 320: `e9583506-e16...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e9583506-e164-41ee-b32e-9f21a02564d5` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease A3 Offset threshold for 3246158_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[320] topology](images/train_0320.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3254108_1 by 10 degrees
- `C2`: Adjust the azimuth of 3246158_4 by 50 degrees
- `C3`: Add neighbor relationship between 3246158_4 and 3254108_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246158_4
- `C5`: Increase transmission power for 3254108_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254108_1
- `C7`: Add neighbor relationship between 3279248_3 and 3254108_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246158_4
- `C9`: Lift the tilt angle of 3246158_4 by 4 degrees
- `C10`: Decrease A3 Offset threshold for 3246158_4 **← 정답**
- `C11`: Lift the tilt angle  of 3254108_1 by 10 degrees
- `C12`: Decrease transmission power for 3254108_1
- `C13`: Adjust the azimuth of 3254108_1 by 50 degrees
- `C14`: Check test server and transmission issues
- `C15`: Increase A3 Offset threshold for 3246158_4
- `C16`: Decrease transmission power for 3246158_4
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Press down the tilt angle of 3246158_4 by 4 degrees
- `C19`: Increase A3 Offset threshold for 3254108_1
- `C20`: Decrease A3 Offset threshold for 3254108_1
- `C21`: Increase transmission power for 3246158_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254108_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.275 | MS1 | 121.4656675083 | 31.1446372140 | 669 | 504990 | -83.78 | 16.71 | 574.00 | 0.04 | 2.64 | 1599 |
| 2024-09-20 22:21:32.516 | MS1 | 121.4656616246 | 31.1446186764 | 669 | 504990 | -83.87 | 12.07 | 443.17 | 0.05 | 2.97 | 1594 |
| 2024-09-20 22:21:33.576 | MS1 | 121.4656626616 | 31.1446290798 | 669 | 504990 | -78.16 | 13.16 | 408.42 | 0.00 | 2.65 | 1599 |
| 2024-09-20 22:21:34.838 | MS1 | 121.4656642938 | 31.1446200466 | 669 | 504990 | -84.20 | -1.06 | 43.64 | 0.14 | 1.45 | 1580 |
| 2024-09-20 22:21:35.138 | MS1 | 121.4656684128 | 31.1446335467 | 669 | 504990 | -90.53 | -1.81 | 41.38 | 0.04 | 1.16 | 1563 |
| 2024-09-20 22:21:36.196 | MS1 | 121.4656745616 | 31.1446359159 | 669 | 504990 | -84.27 | -1.66 | 54.93 | 0.11 | 1.11 | 1567 |
| 2024-09-20 22:21:37.269 | MS1 | 121.4656594037 | 31.1446220889 | 669 | 504990 | -92.53 | -0.08 | 51.98 | 0.03 | 1.24 | 1573 |
| 2024-09-20 22:21:38.384 | MS1 | 121.4656617720 | 31.1446199957 | 669 | 504990 | -86.79 | -0.41 | 72.12 | 0.00 | 1.11 | 1576 |
| 2024-09-20 22:21:39.637 | MS1 | 121.4656623721 | 31.1446372099 | 395 | 504990 | -78.33 | 12.78 | 163.82 | 0.04 | 1.01 | 1577 |
| 2024-09-20 22:21:40.468 | MS1 | 121.4656596861 | 31.1446293110 | 395 | 504990 | -84.42 | 17.31 | 372.77 | 0.08 | 2.99 | 1598 |
| 2024-09-20 22:21:41.150 | MS1 | 121.4656736375 | 31.1446195742 | 395 | 504990 | -76.97 | 16.16 | 421.28 | 0.03 | 2.59 | 1569 |
| 2024-09-20 22:21:42.558 | MS1 | 121.4656696931 | 31.1446245196 | 395 | 504990 | -75.21 | 17.63 | 515.96 | 0.18 | 2.81 | 1594 |

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
| 3230042 | 2 | 121.4759270123 | 31.1523639788 | 84 | 13 | 2 | 22.0 | TDD | 325 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3246158 | 4 | 121.4753736104 | 31.1505695508 | 145 | 2 | 9 | 34.4 | TDD | 669 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3254108 | 1 | 121.4682005289 | 31.1480043153 | 355 | 15 | 2 | 22.6 | TDD | 395 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3279248 | 3 | 121.4671209331 | 31.1450746773 | 67 | 5 | 2 | 34.0 | TDD | 1005 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.769 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.794 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.929 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.929 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.644 | NREventA3 | measId:2;ServCellPCI:777;Se... |
| 2024-09-20 22:21:37.884 | NRHandoverAttempt | SourcePCI:777;SourceNR-ARFC... |
| 2024-09-20 22:21:37.922 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.934 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.045 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.045 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254108 | 1 | 17.5510 | 15.0864 | -117.8421 | 10.1891 | 138.7217 | 0.0134 | 0.0037 |
| 2024_09_20 22:00 | 3230042 | 2 | 5.3699 | 9.9766 | -116.1627 | 9.6502 | 174.8284 | 0.0187 | 0.0059 |
| 2024_09_20 22:00 | 3279248 | 3 | 16.8606 | 11.3732 | -115.5969 | 18.4046 | 192.0050 | 0.0153 | 0.0136 |
| 2024_09_20 22:00 | 3246158 | 4 | 19.9812 | 12.0203 | -116.7029 | 10.7480 | 126.6994 | 0.0127 | 0.1858 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416464_2678B3F6 | 504990 | 669 | -86.1 | 504990 | 395 | -77.3 | 504990 | 1005 | -80.4 | 504990 | 325 |
| MR_1774416464_A5CF9068 | 504990 | 395 | -79.6 | 504990 | 669 | -83.7 | 504990 | 1005 | -78.2 | 504990 | 325 |
| MR_1774416464_DDBD8375 | 504990 | 669 | -82.7 | 504990 | 395 | -80.4 | 504990 | 1005 | -79.7 | 504990 | 325 |
| MR_1774416464_2454CB2A | 504990 | 669 | -83.9 | 504990 | 395 | -79.0 | 504990 | 1005 | -78.2 | 504990 | 325 |
| MR_1774416464_91FC43CD | 504990 | 395 | -76.6 | 504990 | 669 | -85.5 | 504990 | 1005 | -78.1 | 504990 | 325 |
| MR_1774416464_D9BEAABD | 504990 | 395 | -79.7 | 504990 | 669 | -86.0 | 504990 | 1005 | -79.5 | 504990 | 325 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 321: `a5952838-893...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a5952838-8937-4c56-8203-74edb7eb0392` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[321] topology](images/train_0321.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3257614_2
- `C2`: Adjust the azimuth of 3249606_1 by 50 degrees
- `C3`: Lift the tilt angle of 3257614_2 by 7 degrees
- `C4`: Increase A3 Offset threshold for 3249606_1
- `C5`: Check test server and transmission issues **← 정답**
- `C6`: Decrease A3 Offset threshold for 3257614_2
- `C7`: Increase transmission power for 3257614_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249606_1
- `C9`: Lift the tilt angle  of 3249606_1 by 10 degrees
- `C10`: Decrease A3 Offset threshold for 3249606_1
- `C11`: Adjust the azimuth of 3257614_2 by 50 degrees
- `C12`: Press down the tilt angle of 3257614_2 by 7 degrees
- `C13`: Increase transmission power for 3249606_1
- `C14`: Add neighbor relationship between 3231954_4 and 3249606_1
- `C15`: Decrease transmission power for 3249606_1
- `C16`: Decrease transmission power for 3257614_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249606_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257614_2
- `C19`: Press down the tilt angle  of 3249606_1 by 10 degrees
- `C20`: Add neighbor relationship between 3257614_2 and 3249606_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257614_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.184 | MS1 | 121.4656755697 | 31.1446296733 | 451 | 504990 | -91.16 | 13.20 | 565.96 | 0.12 | 2.05 | 1597 |
| 2024-09-20 22:21:32.387 | MS1 | 121.4656611020 | 31.1446188607 | 451 | 504990 | -90.10 | 13.39 | 466.68 | 0.13 | 2.93 | 1596 |
| 2024-09-20 22:21:33.772 | MS1 | 121.4656709342 | 31.1446335034 | 451 | 504990 | -86.21 | 13.50 | 555.95 | 0.13 | 2.94 | 1567 |
| 2024-09-20 22:21:34.127 | MS1 | 121.4656709965 | 31.1446254140 | 451 | 504990 | -89.62 | 12.71 | 109.09 | 0.14 | 2.97 | 422 |
| 2024-09-20 22:21:35.443 | MS1 | 121.4656773708 | 31.1446356418 | 451 | 504990 | -88.90 | 12.60 | 70.48 | 0.12 | 2.10 | 330 |
| 2024-09-20 22:21:36.694 | MS1 | 121.4656736929 | 31.1446314063 | 451 | 504990 | -91.61 | 17.52 | 76.92 | 0.01 | 2.42 | 440 |
| 2024-09-20 22:21:37.316 | MS1 | 121.4656644581 | 31.1446216683 | 451 | 504990 | -91.47 | 9.26 | 73.35 | 0.18 | 2.65 | 477 |
| 2024-09-20 22:21:38.660 | MS1 | 121.4656732606 | 31.1446304343 | 451 | 504990 | -93.15 | 7.53 | 96.26 | 0.16 | 2.06 | 387 |
| 2024-09-20 22:21:39.978 | MS1 | 121.4656734673 | 31.1446311145 | 451 | 504990 | -90.03 | 10.35 | 87.21 | 0.05 | 2.97 | 402 |
| 2024-09-20 22:21:40.217 | MS1 | 121.4656701921 | 31.1446349713 | 451 | 504990 | -92.74 | 7.67 | 532.36 | 0.06 | 2.86 | 1572 |
| 2024-09-20 22:21:41.689 | MS1 | 121.4656762305 | 31.1446271076 | 451 | 504990 | -91.57 | 9.39 | 498.24 | 0.15 | 2.24 | 1566 |
| 2024-09-20 22:21:42.504 | MS1 | 121.4656708347 | 31.1446239834 | 451 | 504990 | -90.06 | 10.55 | 389.55 | 0.16 | 2.35 | 1565 |

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
| 3231954 | 4 | 121.4680780686 | 31.1541807259 | 6 | 2 | 7 | 31.8 | TDD | 477 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3249606 | 1 | 121.4748058561 | 31.1481358497 | 122 | 13 | 11 | 33.5 | TDD | 172 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3257614 | 2 | 121.4759891310 | 31.1530171385 | 138 | 6 | 7 | 25.6 | TDD | 451 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3270345 | 3 | 121.4667600373 | 31.1508820545 | 116 | 12 | 12 | 17.0 | TDD | 740 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.897 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.914 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.027 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.027 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.731 | NREventA3 | measId:2;ServCellPCI:248;Se... |
| 2024-09-20 22:21:37.971 | NRHandoverAttempt | SourcePCI:248;SourceNR-ARFC... |
| 2024-09-20 22:21:38.008 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.021 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.132 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.132 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249606 | 1 | 9.6127 | 17.9613 | -114.0757 | 7.5135 | 142.1193 | 0.0166 | 0.0152 |
| 2024_09_20 22:00 | 3257614 | 2 | 12.7820 | 18.5414 | -114.1975 | 19.2263 | 135.5065 | 0.0047 | 0.0046 |
| 2024_09_20 22:00 | 3270345 | 3 | 10.5898 | 11.7651 | -117.0841 | 7.4980 | 158.2191 | 0.0036 | 0.0057 |
| 2024_09_20 22:00 | 3231954 | 4 | 9.5782 | 12.8911 | -116.3830 | 5.8266 | 88.6106 | 0.0085 | 0.0084 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412095_83527A48 | 504990 | 451 | -90.6 | 504990 | 172 | -91.0 | 504990 | 477 | -99.3 | 504990 | 740 |
| MR_1774412095_7514ED49 | 504990 | 451 | -87.3 | 504990 | 172 | -89.2 | 504990 | 477 | -96.8 | 504990 | 740 |
| MR_1774412095_69869F62 | 504990 | 451 | -87.8 | 504990 | 172 | -89.1 | 504990 | 477 | -95.8 | 504990 | 740 |
| MR_1774412095_C6D975C2 | 504990 | 451 | -87.9 | 504990 | 172 | -92.3 | 504990 | 477 | -95.7 | 504990 | 740 |
| MR_1774412095_261290E1 | 504990 | 451 | -87.4 | 504990 | 172 | -90.4 | 504990 | 477 | -99.0 | 504990 | 740 |
| MR_1774412095_D45BC987 | 504990 | 451 | -87.7 | 504990 | 172 | -92.0 | 504990 | 477 | -98.5 | 504990 | 740 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 322: `6da63593-545...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6da63593-545a-4856-a009-8b9c50e87b13` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3244082_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[322] topology](images/train_0322.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274117_1
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease transmission power for 3274117_1
- `C4`: Increase A3 Offset threshold for 3274117_1
- `C5`: Press down the tilt angle of 3244082_3 by 5 degrees
- `C6`: Check test server and transmission issues
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244082_3
- `C8`: Decrease A3 Offset threshold for 3244082_3
- `C9`: Add neighbor relationship between 3252984_2 and 3274117_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244082_3 **← 정답**
- `C11`: Adjust the azimuth of 3274117_1 by 50 degrees
- `C12`: Lift the tilt angle of 3244082_3 by 5 degrees
- `C13`: Decrease transmission power for 3244082_3
- `C14`: Increase A3 Offset threshold for 3244082_3
- `C15`: Decrease A3 Offset threshold for 3274117_1
- `C16`: Increase transmission power for 3274117_1
- `C17`: Adjust the azimuth of 3244082_3 by 1 degrees
- `C18`: Increase transmission power for 3244082_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274117_1
- `C20`: Add neighbor relationship between 3244082_3 and 3274117_1
- `C21`: Press down the tilt angle  of 3274117_1 by 10 degrees
- `C22`: Lift the tilt angle  of 3274117_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.839 | MS1 | 121.4656627665 | 31.1446229916 | 430 | 504990 | -91.28 | 17.13 | 594.97 | 0.17 | 2.77 | 1573 |
| 2024-09-20 22:21:32.313 | MS1 | 121.4656731766 | 31.1446227431 | 430 | 504990 | -86.12 | 14.16 | 305.75 | 0.01 | 2.38 | 1561 |
| 2024-09-20 22:21:33.613 | MS1 | 121.4656590233 | 31.1446327550 | 430 | 504990 | -86.97 | 14.74 | 423.69 | 0.08 | 2.57 | 1588 |
| 2024-09-20 22:21:34.700 | MS1 | 121.4656618696 | 31.1446377600 | 430 | 504990 | -91.60 | 12.63 | 96.57 | 0.60 | 2.81 | 590 |
| 2024-09-20 22:21:35.517 | MS1 | 121.4656775918 | 31.1446339418 | 430 | 504990 | -88.71 | 15.73 | 77.64 | 0.65 | 2.19 | 627 |
| 2024-09-20 22:21:36.974 | MS1 | 121.4656686907 | 31.1446237241 | 430 | 504990 | -86.55 | 17.07 | 74.42 | 0.70 | 2.32 | 603 |
| 2024-09-20 22:21:37.410 | MS1 | 121.4656670257 | 31.1446232747 | 430 | 504990 | -90.81 | 7.79 | 100.80 | 0.66 | 2.79 | 676 |
| 2024-09-20 22:21:38.249 | MS1 | 121.4656681957 | 31.1446348301 | 430 | 504990 | -91.87 | 8.93 | 90.97 | 0.58 | 2.91 | 524 |
| 2024-09-20 22:21:39.185 | MS1 | 121.4656774772 | 31.1446376314 | 430 | 504990 | -92.50 | 7.85 | 88.22 | 0.65 | 2.15 | 565 |
| 2024-09-20 22:21:40.613 | MS1 | 121.4656675897 | 31.1446360911 | 430 | 504990 | -91.75 | 11.50 | 410.96 | 0.09 | 2.16 | 1563 |
| 2024-09-20 22:21:41.823 | MS1 | 121.4656614881 | 31.1446209040 | 430 | 504990 | -92.00 | 9.85 | 359.45 | 0.10 | 2.19 | 1598 |
| 2024-09-20 22:21:42.749 | MS1 | 121.4656739638 | 31.1446215332 | 430 | 504990 | -92.68 | 9.17 | 566.73 | 0.10 | 2.79 | 1589 |

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
| 3232996 | 4 | 121.4663867149 | 31.1504929442 | 163 | 1 | 5 | 23.1 | TDD | 94 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3244082 | 3 | 121.4742737369 | 31.1450246893 | 266 | 3 | 8 | 28.8 | TDD | 430 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3252984 | 2 | 121.4700793481 | 31.1441114691 | 236 | 0 | 6 | 16.5 | TDD | 796 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3274117 | 1 | 121.4667810676 | 31.1528234100 | 318 | 10 | 2 | 22.1 | TDD | 922 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.539 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.559 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.694 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.694 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.383 | NREventA3 | measId:2;ServCellPCI:283;Se... |
| 2024-09-20 22:21:38.623 | NRHandoverAttempt | SourcePCI:283;SourceNR-ARFC... |
| 2024-09-20 22:21:38.672 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.683 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.809 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.809 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274117 | 1 | 17.4111 | 11.6601 | -117.0549 | 11.9165 | 157.4499 | 0.0108 | 0.0198 |
| 2024_09_20 22:00 | 3252984 | 2 | 7.2680 | 5.4648 | -117.6500 | 17.6766 | 146.8453 | 0.0068 | 0.0194 |
| 2024_09_20 22:00 | 3244082 | 3 | 18.5452 | 17.9428 | -116.5888 | 19.8675 | 186.0526 | 0.0090 | 0.0044 |
| 2024_09_20 22:00 | 3232996 | 4 | 6.5340 | 9.7524 | -116.2920 | 7.0564 | 112.6377 | 0.0022 | 0.0159 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416688_869A0F3D | 504990 | 430 | -92.3 | 504990 | 922 | -92.2 | 504990 | 796 | -104.7 | 504990 | 94 |
| MR_1774416688_0FBFFC5C | 504990 | 430 | -90.9 | 504990 | 922 | -90.8 | 504990 | 796 | -105.0 | 504990 | 94 |
| MR_1774416688_E3E35CB7 | 504990 | 430 | -92.9 | 504990 | 922 | -93.0 | 504990 | 796 | -104.4 | 504990 | 94 |
| MR_1774416688_1830B722 | 504990 | 430 | -92.5 | 504990 | 922 | -92.9 | 504990 | 796 | -103.5 | 504990 | 94 |
| MR_1774416688_C7C1D8D4 | 504990 | 430 | -90.3 | 504990 | 922 | -94.0 | 504990 | 796 | -104.2 | 504990 | 94 |
| MR_1774416688_5DFCD826 | 504990 | 430 | -91.2 | 504990 | 922 | -93.1 | 504990 | 796 | -103.6 | 504990 | 94 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 323: `d03c531d-5e2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d03c531d-5e29-457f-bec3-394790311115` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Add neighbor relationship between 3238691_3 and 3219227_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[323] topology](images/train_0323.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3219227_1 by 5 degrees
- `C2`: Lift the tilt angle  of 3219227_1 by 5 degrees
- `C3`: Adjust the azimuth of 3219227_1 by 17 degrees
- `C4`: Check test server and transmission issues
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219227_1
- `C6`: Increase transmission power for 3219227_1
- `C7`: Add neighbor relationship between 3238691_3 and 3219227_1 **← 정답**
- `C8`: Increase A3 Offset threshold for 3238691_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219227_1
- `C10`: Add neighbor relationship between 3252017_4 and 3219227_1
- `C11`: Decrease transmission power for 3238691_3
- `C12`: Increase A3 Offset threshold for 3219227_1
- `C13`: Lift the tilt angle of 3238691_3 by 10 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238691_3
- `C16`: Adjust the azimuth of 3238691_3 by 50 degrees
- `C17`: Press down the tilt angle of 3238691_3 by 10 degrees
- `C18`: Decrease A3 Offset threshold for 3238691_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238691_3
- `C20`: Decrease transmission power for 3219227_1
- `C21`: Decrease A3 Offset threshold for 3219227_1
- `C22`: Increase transmission power for 3238691_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.635 | MS1 | 121.4656710086 | 31.1446351595 | 635 | 504990 | -80.83 | 13.04 | 546.38 | 0.06 | 2.99 | 1600 |
| 2024-09-20 22:21:32.666 | MS1 | 121.4656694434 | 31.1446216828 | 635 | 504990 | -81.36 | 14.23 | 328.26 | 0.15 | 2.80 | 1589 |
| 2024-09-20 22:21:33.595 | MS1 | 121.4656775087 | 31.1446318498 | 635 | 504990 | -83.15 | 14.54 | 502.96 | 0.13 | 2.50 | 1573 |
| 2024-09-20 22:21:34.471 | MS1 | 121.4656620178 | 31.1446206842 | 635 | 504990 | -87.25 | -2.69 | 59.23 | 0.12 | 1.45 | 1582 |
| 2024-09-20 22:21:35.641 | MS1 | 121.4656738165 | 31.1446331801 | 635 | 504990 | -91.47 | -1.39 | 40.31 | 0.04 | 1.24 | 1562 |
| 2024-09-20 22:21:36.745 | MS1 | 121.4656590471 | 31.1446233131 | 635 | 504990 | -86.67 | -2.34 | 39.01 | 0.12 | 1.14 | 1582 |
| 2024-09-20 22:21:37.971 | MS1 | 121.4656745845 | 31.1446358124 | 635 | 504990 | -91.24 | -0.63 | 29.12 | 0.09 | 1.35 | 1575 |
| 2024-09-20 22:21:38.417 | MS1 | 121.4656718201 | 31.1446236677 | 635 | 504990 | -79.97 | 16.54 | 466.78 | 0.11 | 1.35 | 1593 |
| 2024-09-20 22:21:39.691 | MS1 | 121.4656618968 | 31.1446225202 | 635 | 504990 | -81.22 | 12.60 | 428.08 | 0.10 | 1.18 | 1570 |
| 2024-09-20 22:21:40.462 | MS1 | 121.4656684112 | 31.1446325151 | 635 | 504990 | -79.59 | 16.52 | 460.92 | 0.16 | 2.25 | 1567 |
| 2024-09-20 22:21:41.498 | MS1 | 121.4656665175 | 31.1446252059 | 635 | 504990 | -83.85 | 13.76 | 451.71 | 0.15 | 2.89 | 1570 |
| 2024-09-20 22:21:42.174 | MS1 | 121.4656596322 | 31.1446306535 | 635 | 504990 | -81.80 | 13.88 | 315.76 | 0.13 | 2.81 | 1582 |

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
| 3219227 | 1 | 121.4670648401 | 31.1490303364 | 212 | 3 | 10 | 19.7 | TDD | 569 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3238691 | 3 | 121.4706123849 | 31.1476215477 | 128 | 6 | 12 | 47.0 | TDD | 635 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3252017 | 4 | 121.4715603144 | 31.1549538657 | 325 | 7 | 3 | 23.3 | TDD | 959 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3258554 | 2 | 121.4685939525 | 31.1448174928 | 135 | 7 | 2 | 18.6 | TDD | 162 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.282 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.298 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.430 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.430 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.153 | NREventA3 | measId:2;ServCellPCI:111;Se... |
| 2024-09-20 22:21:36.153 | NREventA3 | measId:2;ServCellPCI:111;Se... |
| 2024-09-20 22:21:37.153 | NREventA3 | measId:2;ServCellPCI:111;Se... |
| 2024-09-20 22:21:39.653 | NRRRCReestablishAttempt | PCI:111 |
| 2024-09-20 22:21:39.669 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.684 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.804 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.804 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219227 | 1 | 13.0267 | 17.9761 | -115.7508 | 14.0127 | 162.6912 | 0.0084 | 0.0064 |
| 2024_09_20 22:00 | 3258554 | 2 | 14.6737 | 17.8955 | -114.1467 | 8.0959 | 123.9945 | 0.0098 | 0.0113 |
| 2024_09_20 22:00 | 3238691 | 3 | 17.1263 | 6.9972 | -115.8554 | 6.3151 | 178.1890 | 0.0143 | 0.1967 |
| 2024_09_20 22:00 | 3252017 | 4 | 10.9765 | 14.9723 | -115.7319 | 11.2563 | 91.2803 | 0.0196 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414480_27C20909 | 504990 | 635 | -87.8 | 504990 | 569 | -80.5 | 504990 | 959 | -84.4 | 504990 | 162 |
| MR_1774414480_6C5D7897 | 504990 | 635 | -85.8 | 504990 | 569 | -81.1 | 504990 | 959 | -86.4 | 504990 | 162 |
| MR_1774414480_AB762A2A | 504990 | 569 | -81.4 | 504990 | 635 | -87.8 | 504990 | 959 | -84.8 | 504990 | 162 |
| MR_1774414480_32BB28A9 | 504990 | 635 | -86.7 | 504990 | 569 | -82.6 | 504990 | 959 | -83.0 | 504990 | 162 |
| MR_1774414480_EC54ABAA | 504990 | 635 | -86.3 | 504990 | 569 | -82.4 | 504990 | 959 | -86.3 | 504990 | 162 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 324: `cec8a6f2-ea1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cec8a6f2-ea1e-487b-ab12-d46f67ac80ae` |
| Tag | **multiple-answer** |
| 정답 | **C10|C18** |
| C10 의미 | Press down the tilt angle  of 3254222_1 by 4 degrees |
| C18 의미 | Decrease transmission power for 3254222_1 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[324] topology](images/train_0324.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3227397_3 and 3254222_1
- `C2`: Increase A3 Offset threshold for 3238546_4
- `C3`: Add neighbor relationship between 3238546_4 and 3254222_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254222_1
- `C5`: Decrease A3 Offset threshold for 3254222_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238546_4
- `C7`: Increase transmission power for 3238546_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238546_4
- `C9`: Adjust the azimuth of 3238546_4 by 32 degrees
- `C10`: Press down the tilt angle  of 3254222_1 by 4 degrees **← 정답**
- `C11`: Press down the tilt angle of 3238546_4 by 4 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254222_1
- `C13`: Lift the tilt angle  of 3254222_1 by 4 degrees
- `C14`: Lift the tilt angle of 3238546_4 by 4 degrees
- `C15`: Adjust the azimuth of 3254222_1 by 14 degrees
- `C16`: Decrease transmission power for 3238546_4
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease transmission power for 3254222_1 **← 정답**
- `C19`: Increase A3 Offset threshold for 3254222_1
- `C20`: Increase transmission power for 3254222_1
- `C21`: Check test server and transmission issues
- `C22`: Decrease A3 Offset threshold for 3238546_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.195 | MS1 | 121.4656656717 | 31.1446269842 | 740 | 504990 | -83.71 | 12.16 | 423.07 | 0.06 | 2.80 | 1581 |
| 2024-09-20 22:21:32.271 | MS1 | 121.4656756778 | 31.1446252187 | 740 | 504990 | -81.34 | 13.68 | 464.70 | 0.07 | 2.60 | 1592 |
| 2024-09-20 22:21:33.314 | MS1 | 121.4656676739 | 31.1446190944 | 740 | 504990 | -78.48 | 14.18 | 327.58 | 0.03 | 2.70 | 1583 |
| 2024-09-20 22:21:34.879 | MS1 | 121.4656752808 | 31.1446368519 | 740 | 504990 | -88.22 | 1.31 | 86.44 | 0.01 | 1.33 | 1597 |
| 2024-09-20 22:21:35.573 | MS1 | 121.4656732141 | 31.1446320420 | 740 | 504990 | -90.61 | 3.65 | 86.16 | 0.13 | 1.30 | 1562 |
| 2024-09-20 22:21:36.935 | MS1 | 121.4656658900 | 31.1446332362 | 740 | 504990 | -85.38 | 2.93 | 70.45 | 0.10 | 1.23 | 1578 |
| 2024-09-20 22:21:37.822 | MS1 | 121.4656723910 | 31.1446285694 | 740 | 504990 | -88.22 | 1.61 | 90.88 | 0.19 | 1.23 | 1570 |
| 2024-09-20 22:21:38.279 | MS1 | 121.4656582124 | 31.1446182809 | 740 | 504990 | -87.21 | 1.88 | 88.40 | 0.10 | 1.06 | 1582 |
| 2024-09-20 22:21:39.836 | MS1 | 121.4656617909 | 31.1446262730 | 740 | 504990 | -86.02 | 2.99 | 67.04 | 0.17 | 1.20 | 1561 |
| 2024-09-20 22:21:40.457 | MS1 | 121.4656779499 | 31.1446238106 | 740 | 504990 | -75.40 | 12.50 | 448.54 | 0.20 | 2.79 | 1579 |
| 2024-09-20 22:21:41.552 | MS1 | 121.4656742442 | 31.1446257445 | 740 | 504990 | -79.29 | 14.87 | 419.74 | 0.12 | 2.38 | 1560 |
| 2024-09-20 22:21:42.585 | MS1 | 121.4656753903 | 31.1446234931 | 740 | 504990 | -84.15 | 13.59 | 323.05 | 0.02 | 2.53 | 1571 |

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
| 3227397 | 3 | 121.4640090241 | 31.1441669748 | 347 | 1 | 7 | 27.0 | TDD | 371 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3238546 | 4 | 121.4664868330 | 31.1550139560 | 152 | 3 | 7 | 16.4 | TDD | 740 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3254222 | 1 | 121.4747138815 | 31.1519916672 | 212 | 2 | 0 | 35.7 | TDD | 283 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3279472 | 2 | 121.4702838114 | 31.1539139191 | 90 | 11 | 10 | 40.7 | TDD | 226 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.962 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.094 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.094 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254222 | 1 | 12.7284 | 6.5435 | -115.2704 | 14.7162 | 109.1444 | 0.0062 | 0.0087 |
| 2024_09_20 22:00 | 3279472 | 2 | 17.4791 | 11.1333 | -115.1128 | 5.2044 | 99.8048 | 0.0092 | 0.0030 |
| 2024_09_20 22:00 | 3227397 | 3 | 11.8205 | 14.6044 | -114.3154 | 5.0095 | 135.6714 | 0.0003 | 0.0166 |
| 2024_09_20 22:00 | 3238546 | 4 | 11.8309 | 12.3490 | -109.7004 | 16.2160 | 125.9474 | 0.0129 | 0.0075 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414671_E8DBD76B | 504990 | 740 | -87.2 | 504990 | 283 | -86.8 | 504990 | 371 | -91.8 | 504990 | 226 |
| MR_1774414671_0440EFC5 | 504990 | 740 | -88.0 | 504990 | 283 | -86.5 | 504990 | 371 | -92.1 | 504990 | 226 |
| MR_1774414671_3BACBBF1 | 504990 | 740 | -87.6 | 504990 | 283 | -85.7 | 504990 | 371 | -89.2 | 504990 | 226 |
| MR_1774414671_294F134E | 504990 | 740 | -87.6 | 504990 | 283 | -87.8 | 504990 | 371 | -90.0 | 504990 | 226 |
| MR_1774414671_3EBEEAD1 | 504990 | 283 | -90.0 | 504990 | 740 | -88.2 | 504990 | 371 | -91.4 | 504990 | 226 |
| MR_1774414671_45161D00 | 504990 | 740 | -89.2 | 504990 | 283 | -88.1 | 504990 | 371 | -91.3 | 504990 | 226 |
| MR_1774414671_2EA6DFB8 | 504990 | 283 | -89.8 | 504990 | 740 | -86.5 | 504990 | 371 | -91.3 | 504990 | 226 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 325: `f0121c5b-4fd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f0121c5b-4fd0-4e2f-adb7-3d7ac5eb94b2` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[325] topology](images/train_0325.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Press down the tilt angle of 3236126_3 by 2 degrees
- `C3`: Press down the tilt angle  of 3273461_2 by 10 degrees
- `C4`: Lift the tilt angle  of 3273461_2 by 10 degrees
- `C5`: Increase A3 Offset threshold for 3273461_2
- `C6`: Decrease transmission power for 3273461_2
- `C7`: Increase transmission power for 3236126_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236126_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273461_2
- `C10`: Decrease A3 Offset threshold for 3236126_3
- `C11`: Adjust the azimuth of 3273461_2 by 50 degrees
- `C12`: Add neighbor relationship between 3213118_4 and 3273461_2
- `C13`: Add neighbor relationship between 3236126_3 and 3273461_2
- `C14`: Increase transmission power for 3273461_2
- `C15`: Decrease A3 Offset threshold for 3273461_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236126_3
- `C17`: Lift the tilt angle of 3236126_3 by 2 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273461_2
- `C19`: Adjust the azimuth of 3236126_3 by 42 degrees
- `C20`: Check test server and transmission issues **← 정답**
- `C21`: Decrease transmission power for 3236126_3
- `C22`: Increase A3 Offset threshold for 3236126_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.476 | MS1 | 121.4656618503 | 31.1446307281 | 732 | 504990 | -86.69 | 13.76 | 559.83 | 0.04 | 2.33 | 1573 |
| 2024-09-20 22:21:32.639 | MS1 | 121.4656724664 | 31.1446226963 | 732 | 504990 | -89.39 | 12.66 | 573.25 | 0.16 | 2.39 | 1595 |
| 2024-09-20 22:21:33.347 | MS1 | 121.4656752735 | 31.1446375170 | 732 | 504990 | -87.97 | 13.51 | 571.91 | 0.10 | 2.24 | 1595 |
| 2024-09-20 22:21:34.503 | MS1 | 121.4656659396 | 31.1446187724 | 732 | 504990 | -90.78 | 17.82 | 72.52 | 0.01 | 2.93 | 327 |
| 2024-09-20 22:21:35.754 | MS1 | 121.4656632109 | 31.1446351183 | 732 | 504990 | -91.41 | 17.66 | 86.27 | 0.04 | 2.85 | 402 |
| 2024-09-20 22:21:36.263 | MS1 | 121.4656622462 | 31.1446357106 | 732 | 504990 | -91.59 | 17.52 | 93.04 | 0.19 | 2.45 | 413 |
| 2024-09-20 22:21:37.959 | MS1 | 121.4656745860 | 31.1446261463 | 732 | 504990 | -91.53 | 11.67 | 62.24 | 0.08 | 2.73 | 465 |
| 2024-09-20 22:21:38.131 | MS1 | 121.4656747174 | 31.1446304504 | 732 | 504990 | -89.01 | 7.37 | 72.72 | 0.07 | 2.79 | 311 |
| 2024-09-20 22:21:39.811 | MS1 | 121.4656635811 | 31.1446302557 | 732 | 504990 | -89.86 | 9.36 | 76.03 | 0.03 | 2.97 | 361 |
| 2024-09-20 22:21:40.107 | MS1 | 121.4656746642 | 31.1446312166 | 732 | 504990 | -90.42 | 7.98 | 549.95 | 0.04 | 2.02 | 1563 |
| 2024-09-20 22:21:41.446 | MS1 | 121.4656700257 | 31.1446322821 | 732 | 504990 | -93.10 | 7.54 | 465.18 | 0.14 | 2.58 | 1591 |
| 2024-09-20 22:21:42.591 | MS1 | 121.4656627966 | 31.1446211581 | 732 | 504990 | -92.94 | 7.87 | 415.22 | 0.10 | 2.37 | 1566 |

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
| 3213118 | 4 | 121.4645483991 | 31.1473147990 | 128 | 0 | 2 | 28.4 | TDD | 68 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3236126 | 3 | 121.4693228294 | 31.1546128728 | 155 | 0 | 7 | 47.3 | TDD | 732 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3244473 | 1 | 121.4745907816 | 31.1486945321 | 218 | 6 | 5 | 31.5 | TDD | 432 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3273461 | 2 | 121.4731362970 | 31.1531943603 | 66 | 12 | 6 | 46.7 | TDD | 339 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.085 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.106 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.236 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.236 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.954 | NREventA3 | measId:2;ServCellPCI:313;Se... |
| 2024-09-20 22:21:38.194 | NRHandoverAttempt | SourcePCI:313;SourceNR-ARFC... |
| 2024-09-20 22:21:38.229 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.239 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.381 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.381 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244473 | 1 | 7.3726 | 7.2142 | -114.1885 | 9.2322 | 186.9641 | 0.0095 | 0.0109 |
| 2024_09_20 22:00 | 3273461 | 2 | 19.2176 | 12.1813 | -114.0341 | 8.8012 | 197.5236 | 0.0112 | 0.0007 |
| 2024_09_20 22:00 | 3236126 | 3 | 5.1345 | 10.9624 | -114.5893 | 15.8580 | 123.2445 | 0.0173 | 0.0193 |
| 2024_09_20 22:00 | 3213118 | 4 | 11.1273 | 10.8276 | -117.8252 | 14.3271 | 168.7316 | 0.0085 | 0.0152 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413586_A79FF029 | 504990 | 732 | -89.6 | 504990 | 339 | -90.8 | 504990 | 68 | -100.7 | 504990 | 432 |
| MR_1774413586_0DF5A76C | 504990 | 732 | -88.8 | 504990 | 339 | -89.8 | 504990 | 68 | -101.5 | 504990 | 432 |
| MR_1774413586_AA596037 | 504990 | 732 | -89.0 | 504990 | 339 | -89.2 | 504990 | 68 | -102.5 | 504990 | 432 |
| MR_1774413586_7767F3E2 | 504990 | 732 | -89.4 | 504990 | 339 | -92.8 | 504990 | 68 | -103.0 | 504990 | 432 |
| MR_1774413586_66FDAE7B | 504990 | 732 | -88.9 | 504990 | 339 | -91.9 | 504990 | 68 | -101.1 | 504990 | 432 |
| MR_1774413586_4C70610B | 504990 | 732 | -89.9 | 504990 | 339 | -89.4 | 504990 | 68 | -100.2 | 504990 | 432 |
| MR_1774413586_E26766B6 | 504990 | 732 | -89.2 | 504990 | 339 | -91.4 | 504990 | 68 | -101.5 | 504990 | 432 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 326: `76451c5b-5a4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `76451c5b-5a42-44fb-add4-40c596eeff19` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3214871_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[326] topology](images/train_0326.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232994_1
- `C2`: Add neighbor relationship between 3214871_4 and 3232994_1
- `C3`: Lift the tilt angle  of 3232994_1 by 10 degrees
- `C4`: Increase A3 Offset threshold for 3214871_4
- `C5`: Lift the tilt angle of 3214871_4 by 5 degrees
- `C6`: Decrease transmission power for 3214871_4
- `C7`: Decrease A3 Offset threshold for 3232994_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232994_1
- `C9`: Press down the tilt angle of 3214871_4 by 5 degrees
- `C10`: Decrease transmission power for 3232994_1
- `C11`: Press down the tilt angle  of 3232994_1 by 10 degrees
- `C12`: Decrease A3 Offset threshold for 3214871_4
- `C13`: Adjust the azimuth of 3232994_1 by 50 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Adjust the azimuth of 3214871_4 by 30 degrees
- `C16`: Check test server and transmission issues
- `C17`: Increase transmission power for 3214871_4
- `C18`: Increase transmission power for 3232994_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214871_4
- `C20`: Increase A3 Offset threshold for 3232994_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214871_4 **← 정답**
- `C22`: Add neighbor relationship between 3266360_3 and 3232994_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.176 | MS1 | 121.4656727743 | 31.1446352349 | 423 | 504990 | -89.40 | 14.80 | 502.60 | 0.05 | 2.56 | 1598 |
| 2024-09-20 22:21:32.551 | MS1 | 121.4656604763 | 31.1446349443 | 423 | 504990 | -87.10 | 12.82 | 490.62 | 0.15 | 2.88 | 1590 |
| 2024-09-20 22:21:33.964 | MS1 | 121.4656723224 | 31.1446307436 | 423 | 504990 | -85.75 | 16.40 | 433.61 | 0.18 | 2.29 | 1568 |
| 2024-09-20 22:21:34.500 | MS1 | 121.4656747599 | 31.1446291604 | 423 | 504990 | -86.02 | 16.06 | 51.03 | 0.70 | 2.67 | 614 |
| 2024-09-20 22:21:35.687 | MS1 | 121.4656736584 | 31.1446332058 | 423 | 504990 | -85.99 | 12.07 | 82.77 | 0.56 | 2.42 | 665 |
| 2024-09-20 22:21:36.468 | MS1 | 121.4656603223 | 31.1446217468 | 423 | 504990 | -87.77 | 16.94 | 86.12 | 0.56 | 2.13 | 500 |
| 2024-09-20 22:21:37.506 | MS1 | 121.4656759411 | 31.1446274712 | 423 | 504990 | -90.37 | 8.98 | 66.78 | 0.66 | 2.74 | 546 |
| 2024-09-20 22:21:38.620 | MS1 | 121.4656642723 | 31.1446378263 | 423 | 504990 | -91.70 | 9.04 | 76.90 | 0.67 | 2.85 | 641 |
| 2024-09-20 22:21:39.648 | MS1 | 121.4656768362 | 31.1446218596 | 423 | 504990 | -91.93 | 7.80 | 74.29 | 0.56 | 2.71 | 692 |
| 2024-09-20 22:21:40.364 | MS1 | 121.4656635407 | 31.1446307969 | 423 | 504990 | -89.01 | 7.63 | 294.76 | 0.02 | 2.06 | 1564 |
| 2024-09-20 22:21:41.851 | MS1 | 121.4656772127 | 31.1446285059 | 423 | 504990 | -91.12 | 11.81 | 493.83 | 0.14 | 2.08 | 1578 |
| 2024-09-20 22:21:42.917 | MS1 | 121.4656653957 | 31.1446223292 | 423 | 504990 | -93.56 | 8.85 | 544.70 | 0.08 | 2.15 | 1596 |

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
| 3214871 | 4 | 121.4736023864 | 31.1485506107 | 270 | 2 | 2 | 38.9 | TDD | 423 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3232994 | 1 | 121.4677137969 | 31.1501322838 | 138 | 14 | 8 | 24.2 | TDD | 952 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3247394 | 2 | 121.4730676442 | 31.1494928668 | 322 | 4 | 5 | 38.9 | TDD | 657 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3266360 | 3 | 121.4660132676 | 31.1509968669 | 5 | 5 | 4 | 23.6 | TDD | 413 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.365 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.390 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.513 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.513 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.211 | NREventA3 | measId:2;ServCellPCI:11;Ser... |
| 2024-09-20 22:21:38.451 | NRHandoverAttempt | SourcePCI:11;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.501 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.512 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.617 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.617 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232994 | 1 | 19.0841 | 14.6608 | -117.3866 | 13.5078 | 196.1714 | 0.0168 | 0.0046 |
| 2024_09_20 22:00 | 3247394 | 2 | 19.7200 | 15.5457 | -117.3891 | 13.4337 | 88.4344 | 0.0090 | 0.0136 |
| 2024_09_20 22:00 | 3266360 | 3 | 13.4780 | 15.1110 | -115.8322 | 15.8355 | 110.8183 | 0.0024 | 0.0080 |
| 2024_09_20 22:00 | 3214871 | 4 | 10.1012 | 5.2522 | -115.9322 | 10.5283 | 142.1320 | 0.0195 | 0.0014 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413687_A7501036 | 504990 | 423 | -84.1 | 504990 | 952 | -94.3 | 504990 | 413 | -94.4 | 504990 | 657 |
| MR_1774413687_022E625F | 504990 | 423 | -87.7 | 504990 | 952 | -94.8 | 504990 | 413 | -93.0 | 504990 | 657 |
| MR_1774413687_2B9FB073 | 504990 | 423 | -85.9 | 504990 | 952 | -92.6 | 504990 | 413 | -95.9 | 504990 | 657 |
| MR_1774413687_6068BC18 | 504990 | 423 | -84.2 | 504990 | 952 | -92.3 | 504990 | 413 | -94.2 | 504990 | 657 |
| MR_1774413687_5010B921 | 504990 | 423 | -85.4 | 504990 | 952 | -91.8 | 504990 | 413 | -93.8 | 504990 | 657 |
| MR_1774413687_DC15AF2B | 504990 | 423 | -87.0 | 504990 | 952 | -93.7 | 504990 | 413 | -93.6 | 504990 | 657 |
| MR_1774413687_3B64B961 | 504990 | 423 | -85.1 | 504990 | 952 | -93.5 | 504990 | 413 | -92.5 | 504990 | 657 |
| MR_1774413687_37AEE0C3 | 504990 | 423 | -86.9 | 504990 | 952 | -94.8 | 504990 | 413 | -95.5 | 504990 | 657 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 327: `2eeb2312-620...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2eeb2312-620a-403b-a921-7561c9ff6ad5` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Lift the tilt angle  of 3253893_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[327] topology](images/train_0327.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3259832_3
- `C2`: Lift the tilt angle  of 3253893_1 by 10 degrees **← 정답**
- `C3`: Increase transmission power for 3259832_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259832_3
- `C5`: Add neighbor relationship between 3253893_1 and 3259832_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266129_2
- `C7`: Decrease A3 Offset threshold for 3259832_3
- `C8`: Press down the tilt angle  of 3253893_1 by 10 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266129_2
- `C10`: Increase transmission power for 3266129_2
- `C11`: Check test server and transmission issues
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259832_3
- `C13`: Decrease A3 Offset threshold for 3266129_2
- `C14`: Adjust the azimuth of 3253893_1 by 50 degrees
- `C15`: Lift the tilt angle of 3266129_2 by 3 degrees
- `C16`: Increase A3 Offset threshold for 3266129_2
- `C17`: Decrease transmission power for 3266129_2
- `C18`: Increase A3 Offset threshold for 3259832_3
- `C19`: Add neighbor relationship between 3266129_2 and 3259832_3
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Adjust the azimuth of 3266129_2 by 34 degrees
- `C22`: Press down the tilt angle of 3266129_2 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.271 | MS1 | 121.4656588241 | 31.1446298909 | 125 | 504990 | -87.49 | 15.34 | 344.36 | 0.15 | 2.12 | 1595 |
| 2024-09-20 22:21:32.331 | MS1 | 121.4656662489 | 31.1446277304 | 125 | 504990 | -88.15 | 13.36 | 417.80 | 0.15 | 2.25 | 1573 |
| 2024-09-20 22:21:33.575 | MS1 | 121.4656709518 | 31.1446352262 | 125 | 504990 | -90.07 | 13.80 | 337.86 | 0.06 | 2.04 | 1598 |
| 2024-09-20 22:21:34.154 | MS1 | 121.4656778322 | 31.1446188999 | 125 | 504990 | -90.37 | 12.83 | 89.38 | 0.04 | 2.00 | 1599 |
| 2024-09-20 22:21:35.657 | MS1 | 121.4656663444 | 31.1446253538 | 125 | 504990 | -89.15 | 13.17 | 91.23 | 0.12 | 2.68 | 1568 |
| 2024-09-20 22:21:36.912 | MS1 | 121.4656696709 | 31.1446331611 | 125 | 504990 | -90.91 | 16.24 | 76.08 | 0.06 | 2.41 | 1598 |
| 2024-09-20 22:21:37.410 | MS1 | 121.4656748214 | 31.1446184267 | 125 | 504990 | -93.09 | 12.76 | 42.77 | 0.12 | 2.91 | 1590 |
| 2024-09-20 22:21:38.306 | MS1 | 121.4656701128 | 31.1446308457 | 125 | 504990 | -90.10 | 8.80 | 60.94 | 0.10 | 2.87 | 1583 |
| 2024-09-20 22:21:39.512 | MS1 | 121.4656594554 | 31.1446248250 | 125 | 504990 | -91.09 | 10.15 | 76.81 | 0.09 | 2.66 | 1586 |
| 2024-09-20 22:21:40.452 | MS1 | 121.4656636856 | 31.1446355870 | 125 | 504990 | -93.53 | 12.87 | 508.10 | 0.05 | 2.16 | 1583 |
| 2024-09-20 22:21:41.659 | MS1 | 121.4656746389 | 31.1446199505 | 125 | 504990 | -92.42 | 8.12 | 585.03 | 0.09 | 2.23 | 1586 |
| 2024-09-20 22:21:42.111 | MS1 | 121.4656705180 | 31.1446312585 | 125 | 504990 | -93.49 | 10.46 | 603.13 | 0.01 | 2.18 | 1589 |

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
| 3253893 | 1 | 121.4715516998 | 31.1450881971 | 31 | 10 | 5 | 29.0 | TDD | 321 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3258836 | 4 | 121.4722742815 | 31.1551173063 | 127 | 5 | 12 | 23.8 | TDD | 271 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3259832 | 3 | 121.4752417653 | 31.1488264427 | 178 | 15 | 10 | 40.0 | TDD | 589 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3266129 | 2 | 121.4706665393 | 31.1530875656 | 241 | 2 | 5 | 15.1 | TDD | 125 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.434 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.452 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.573 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.573 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.253 | NREventA3 | measId:2;ServCellPCI:88;Ser... |
| 2024-09-20 22:21:38.493 | NRHandoverAttempt | SourcePCI:88;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.531 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.544 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.655 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.655 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253893 | 1 | 8.2054 | 10.2599 | -114.0704 | 6.1952 | 191.7194 | 0.0160 | 0.0033 |
| 2024_09_20 22:00 | 3266129 | 2 | 92.3962 | 76.0339 | -117.2469 | 19.3018 | 179.2681 | 0.0022 | 0.0136 |
| 2024_09_20 22:00 | 3259832 | 3 | 7.1817 | 17.1160 | -115.1301 | 5.5062 | 191.5640 | 0.0023 | 0.0013 |
| 2024_09_20 22:00 | 3258836 | 4 | 11.4225 | 14.3361 | -115.2806 | 9.1204 | 87.8406 | 0.0188 | 0.0146 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416538_6067F828 | 504990 | 125 | -91.4 | 504990 | 589 | -94.2 | 504990 | 321 | -101.2 | 504990 | 271 |
| MR_1774416538_77E901BB | 504990 | 125 | -89.7 | 504990 | 589 | -92.5 | 504990 | 321 | -98.8 | 504990 | 271 |
| MR_1774416538_04DEC1DC | 504990 | 125 | -89.4 | 504990 | 589 | -94.2 | 504990 | 321 | -100.7 | 504990 | 271 |
| MR_1774416538_FD10359E | 504990 | 125 | -91.6 | 504990 | 589 | -94.2 | 504990 | 321 | -100.8 | 504990 | 271 |
| MR_1774416538_3F794827 | 504990 | 125 | -92.4 | 504990 | 589 | -94.7 | 504990 | 321 | -98.6 | 504990 | 271 |
| MR_1774416538_3A280887 | 504990 | 125 | -89.6 | 504990 | 589 | -91.3 | 504990 | 321 | -99.6 | 504990 | 271 |
| MR_1774416538_6CCBFF73 | 504990 | 125 | -91.5 | 504990 | 589 | -91.6 | 504990 | 321 | -99.0 | 504990 | 271 |
| MR_1774416538_E4B942C1 | 504990 | 125 | -91.4 | 504990 | 589 | -91.5 | 504990 | 321 | -99.2 | 504990 | 271 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 328: `0744f3f8-c76...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0744f3f8-c767-4a32-8548-60769ab90e9a` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[328] topology](images/train_0328.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3262718_3
- `C2`: Lift the tilt angle  of 3262718_3 by 4 degrees
- `C3`: Press down the tilt angle of 3241038_1 by 10 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262718_3
- `C5`: Decrease transmission power for 3241038_1
- `C6`: Adjust the azimuth of 3262718_3 by 50 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262718_3
- `C8`: Increase transmission power for 3241038_1
- `C9`: Decrease A3 Offset threshold for 3262718_3
- `C10`: Decrease transmission power for 3262718_3
- `C11`: Check test server and transmission issues
- `C12`: Increase A3 Offset threshold for 3241038_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241038_1
- `C14`: Add neighbor relationship between 3241038_1 and 3262718_3
- `C15`: Increase A3 Offset threshold for 3262718_3
- `C16`: Adjust the azimuth of 3241038_1 by 50 degrees
- `C17`: Add neighbor relationship between 3260659_4 and 3262718_3
- `C18`: Lift the tilt angle of 3241038_1 by 10 degrees
- `C19`: Press down the tilt angle  of 3262718_3 by 4 degrees
- `C20`: Insufficient data; more data is needed for judgment. **← 정답**
- `C21`: Decrease A3 Offset threshold for 3241038_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241038_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.461 | MS1 | 121.4656715269 | 31.1446347593 | 816 | 504990 | -86.39 | 15.95 | 517.09 | 0.05 | 2.24 | 1564 |
| 2024-09-20 22:21:32.124 | MS1 | 121.4656594849 | 31.1446354698 | 816 | 504990 | -86.16 | 13.39 | 346.23 | 0.07 | 2.34 | 1580 |
| 2024-09-20 22:21:33.917 | MS1 | 121.4656603829 | 31.1446365742 | 816 | 504990 | -87.86 | 14.43 | 439.53 | 0.03 | 2.49 | 1595 |
| 2024-09-20 22:21:34.676 | MS1 | 121.4656707947 | 31.1446371526 | 816 | 504990 | -88.57 | 15.58 | 91.70 | 0.11 | 2.29 | 1593 |
| 2024-09-20 22:21:35.887 | MS1 | 121.4656768046 | 31.1446331434 | 816 | 504990 | -91.42 | 15.10 | 89.91 | 0.15 | 2.79 | 1572 |
| 2024-09-20 22:21:36.442 | MS1 | 121.4656686468 | 31.1446231880 | 816 | 504990 | -90.53 | 17.00 | 62.19 | 0.09 | 2.50 | 1582 |
| 2024-09-20 22:21:37.945 | MS1 | 121.4656669107 | 31.1446334807 | 816 | 504990 | -92.03 | 9.20 | 60.83 | 0.01 | 2.84 | 1578 |
| 2024-09-20 22:21:38.772 | MS1 | 121.4656713880 | 31.1446322588 | 816 | 504990 | -93.90 | 12.81 | 89.86 | 0.09 | 2.26 | 1587 |
| 2024-09-20 22:21:39.756 | MS1 | 121.4656636479 | 31.1446225387 | 816 | 504990 | -92.95 | 7.96 | 58.87 | 0.01 | 2.88 | 1574 |
| 2024-09-20 22:21:40.805 | MS1 | 121.4656642134 | 31.1446256698 | 816 | 504990 | -90.46 | 12.31 | 404.56 | 0.06 | 2.62 | 1583 |
| 2024-09-20 22:21:41.805 | MS1 | 121.4656702902 | 31.1446263796 | 816 | 504990 | -90.31 | 11.02 | 597.37 | 0.17 | 2.10 | 1573 |
| 2024-09-20 22:21:42.211 | MS1 | 121.4656677708 | 31.1446303758 | 816 | 504990 | -92.91 | 12.36 | 501.24 | 0.17 | 2.34 | 1563 |

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
| 3219607 | 2 | 121.4642955491 | 31.1515155269 | 106 | 6 | 6 | 47.3 | TDD | 220 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3241038 | 1 | 121.4700493034 | 31.1443077489 | 348 | 14 | 4 | 33.3 | TDD | 816 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3260659 | 4 | 121.4691760056 | 31.1493483875 | 306 | 12 | 8 | 39.7 | TDD | 919 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3262718 | 3 | 121.4703564391 | 31.1511887020 | 161 | 1 | 2 | 49.2 | TDD | 748 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.539 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.559 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.707 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.707 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.391 | NREventA3 | measId:2;ServCellPCI:151;Se... |
| 2024-09-20 22:21:38.631 | NRHandoverAttempt | SourcePCI:151;SourceNR-ARFC... |
| 2024-09-20 22:21:38.661 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.674 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.777 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.777 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3241038 | 1 | 94.3996 | 78.7820 | -116.2049 | 7.4591 | 154.4243 | 0.0135 | 0.0054 |
| 2024_09_19 22:00 | 3219607 | 2 | 85.1721 | 79.7685 | -116.8977 | 6.1264 | 112.3608 | 0.0192 | 0.0159 |
| 2024_09_19 22:00 | 3262718 | 3 | 81.4306 | 83.5243 | -116.0385 | 14.6708 | 105.0888 | 0.0118 | 0.0005 |
| 2024_09_19 22:00 | 3260659 | 4 | 76.4836 | 78.2251 | -117.3676 | 13.4077 | 167.9244 | 0.0187 | 0.0029 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413693_F5885287 | 504990 | 816 | -87.2 | 504990 | 748 | -94.9 | 504990 | 919 | -99.6 | 504990 | 220 |
| MR_1774413693_C59BB3E0 | 504990 | 816 | -88.0 | 504990 | 748 | -95.4 | 504990 | 919 | -101.2 | 504990 | 220 |
| MR_1774413693_6E3E3046 | 504990 | 816 | -89.5 | 504990 | 748 | -93.2 | 504990 | 919 | -98.3 | 504990 | 220 |
| MR_1774413693_C1B60920 | 504990 | 816 | -90.5 | 504990 | 748 | -94.4 | 504990 | 919 | -99.2 | 504990 | 220 |
| MR_1774413693_40DB5819 | 504990 | 816 | -88.8 | 504990 | 748 | -94.9 | 504990 | 919 | -99.1 | 504990 | 220 |
| MR_1774413693_1359A8C1 | 504990 | 816 | -89.3 | 504990 | 748 | -93.9 | 504990 | 919 | -98.3 | 504990 | 220 |
| MR_1774413693_7C135022 | 504990 | 816 | -90.4 | 504990 | 748 | -95.7 | 504990 | 919 | -101.2 | 504990 | 220 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 329: `931eb354-210...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `931eb354-2100-4a79-83a9-2763acd1126a` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3236147_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[329] topology](images/train_0329.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3236147_2 by 6 degrees
- `C2`: Press down the tilt angle of 3236147_2 by 6 degrees
- `C3`: Adjust the azimuth of 3236147_2 by 15 degrees
- `C4`: Add neighbor relationship between 3220266_1 and 3243211_4
- `C5`: Check test server and transmission issues
- `C6`: Increase transmission power for 3236147_2
- `C7`: Add neighbor relationship between 3236147_2 and 3243211_4
- `C8`: Decrease A3 Offset threshold for 3243211_4
- `C9`: Decrease A3 Offset threshold for 3236147_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236147_2
- `C11`: Press down the tilt angle  of 3243211_4 by 10 degrees
- `C12`: Increase A3 Offset threshold for 3236147_2
- `C13`: Lift the tilt angle  of 3243211_4 by 10 degrees
- `C14`: Decrease transmission power for 3243211_4
- `C15`: Increase A3 Offset threshold for 3243211_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243211_4
- `C17`: Decrease transmission power for 3236147_2
- `C18`: Adjust the azimuth of 3243211_4 by 50 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243211_4
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase transmission power for 3243211_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236147_2 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.999 | MS1 | 121.4656609690 | 31.1446308416 | 700 | 504990 | -88.53 | 13.80 | 425.35 | 0.02 | 2.36 | 1561 |
| 2024-09-20 22:21:32.780 | MS1 | 121.4656755657 | 31.1446277484 | 700 | 504990 | -91.43 | 12.64 | 496.12 | 0.18 | 2.74 | 1597 |
| 2024-09-20 22:21:33.449 | MS1 | 121.4656769045 | 31.1446366365 | 700 | 504990 | -86.98 | 15.66 | 395.15 | 0.02 | 2.96 | 1574 |
| 2024-09-20 22:21:34.918 | MS1 | 121.4656700434 | 31.1446198591 | 700 | 504990 | -85.75 | 16.86 | 89.77 | 0.64 | 2.04 | 615 |
| 2024-09-20 22:21:35.606 | MS1 | 121.4656735197 | 31.1446222490 | 700 | 504990 | -90.56 | 17.47 | 77.76 | 0.63 | 2.27 | 587 |
| 2024-09-20 22:21:36.361 | MS1 | 121.4656713199 | 31.1446324487 | 700 | 504990 | -88.86 | 15.74 | 90.94 | 0.59 | 2.05 | 645 |
| 2024-09-20 22:21:37.539 | MS1 | 121.4656602363 | 31.1446268691 | 700 | 504990 | -89.65 | 9.78 | 96.07 | 0.66 | 2.85 | 621 |
| 2024-09-20 22:21:38.472 | MS1 | 121.4656597429 | 31.1446355590 | 700 | 504990 | -92.53 | 12.69 | 67.41 | 0.51 | 2.69 | 551 |
| 2024-09-20 22:21:39.835 | MS1 | 121.4656608559 | 31.1446232168 | 700 | 504990 | -92.12 | 8.25 | 58.97 | 0.60 | 2.73 | 585 |
| 2024-09-20 22:21:40.873 | MS1 | 121.4656731208 | 31.1446301193 | 700 | 504990 | -93.88 | 9.77 | 302.98 | 0.08 | 2.71 | 1565 |
| 2024-09-20 22:21:41.390 | MS1 | 121.4656641309 | 31.1446187541 | 700 | 504990 | -91.87 | 10.17 | 361.03 | 0.13 | 2.43 | 1586 |
| 2024-09-20 22:21:42.628 | MS1 | 121.4656644825 | 31.1446195187 | 700 | 504990 | -91.53 | 8.06 | 476.20 | 0.03 | 2.29 | 1589 |

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
| 3220266 | 1 | 121.4713960954 | 31.1543008041 | 345 | 3 | 1 | 39.9 | TDD | 953 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3229374 | 3 | 121.4712659342 | 31.1557203149 | 111 | 2 | 11 | 19.5 | TDD | 837 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3236147 | 2 | 121.4662450651 | 31.1557773378 | 198 | 5 | 11 | 17.4 | TDD | 700 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3243211 | 4 | 121.4715601149 | 31.1467830220 | 70 | 12 | 1 | 41.5 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.411 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.428 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.551 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.551 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.242 | NREventA3 | measId:2;ServCellPCI:431;Se... |
| 2024-09-20 22:21:38.482 | NRHandoverAttempt | SourcePCI:431;SourceNR-ARFC... |
| 2024-09-20 22:21:38.512 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.522 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.664 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.664 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220266 | 1 | 17.1784 | 11.6658 | -117.7193 | 14.0357 | 147.1525 | 0.0081 | 0.0105 |
| 2024_09_20 22:00 | 3236147 | 2 | 11.0048 | 15.0805 | -114.1400 | 16.5336 | 155.3058 | 0.0099 | 0.0126 |
| 2024_09_20 22:00 | 3229374 | 3 | 16.4465 | 15.9036 | -117.7894 | 14.2718 | 137.1454 | 0.0168 | 0.0196 |
| 2024_09_20 22:00 | 3243211 | 4 | 9.4953 | 14.7610 | -115.8931 | 19.8807 | 147.0430 | 0.0054 | 0.0098 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417004_762BBFC7 | 504990 | 700 | -87.6 | 504990 | 382 | -90.4 | 504990 | 953 | -97.4 | 504990 | 837 |
| MR_1774417004_AA68DA35 | 504990 | 700 | -86.1 | 504990 | 382 | -89.7 | 504990 | 953 | -96.9 | 504990 | 837 |
| MR_1774417004_4728017C | 504990 | 700 | -84.9 | 504990 | 382 | -90.9 | 504990 | 953 | -95.8 | 504990 | 837 |
| MR_1774417004_4A36404D | 504990 | 700 | -86.3 | 504990 | 382 | -89.9 | 504990 | 953 | -96.3 | 504990 | 837 |
| MR_1774417004_6E1D3A84 | 504990 | 700 | -86.1 | 504990 | 382 | -90.8 | 504990 | 953 | -96.3 | 504990 | 837 |
| MR_1774417004_083126B2 | 504990 | 700 | -87.7 | 504990 | 382 | -88.2 | 504990 | 953 | -97.3 | 504990 | 837 |
| MR_1774417004_5CD70C0B | 504990 | 700 | -84.5 | 504990 | 382 | -87.8 | 504990 | 953 | -96.6 | 504990 | 837 |

> *... 2개 열 생략 (전체 14열)*

---
