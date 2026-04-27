# Track A 문제 분석 — train[1900]~train[1909]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1900] ~ train[1909] (10개)

## 목차

1. [문제 1900: `817a7ad9-2f8...`](#1900) — single-answer, 정답: C10
2. [문제 1901: `dbb1f7f9-e37...`](#1901) — single-answer, 정답: C14
3. [문제 1902: `74b589e5-ed1...`](#1902) — single-answer, 정답: C17
4. [문제 1903: `8ab23cb4-c30...`](#1903) — single-answer, 정답: C1
5. [문제 1904: `c5adb6b0-d14...`](#1904) — single-answer, 정답: C10
6. [문제 1905: `8820a8fd-b3b...`](#1905) — multiple-answer, 정답: C3|C12|C15|C20
7. [문제 1906: `9046da13-369...`](#1906) — single-answer, 정답: C21
8. [문제 1907: `3d3fb192-1e9...`](#1907) — single-answer, 정답: C13
9. [문제 1908: `7690d837-028...`](#1908) — single-answer, 정답: C10
10. [문제 1909: `d9d89d76-070...`](#1909) — single-answer, 정답: C12

---

### 문제 1900: `817a7ad9-2f8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `817a7ad9-2f8e-4343-84be-8f61d6fbcffe` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1900] topology](images/train_1900.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3237451_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237451_4
- `C3`: Lift the tilt angle of 3231321_2 by 10 degrees
- `C4`: Adjust the azimuth of 3237451_4 by 50 degrees
- `C5`: Increase transmission power for 3231321_2
- `C6`: Increase A3 Offset threshold for 3237451_4
- `C7`: Add neighbor relationship between 3231321_2 and 3237451_4
- `C8`: Press down the tilt angle of 3231321_2 by 10 degrees
- `C9`: Increase A3 Offset threshold for 3231321_2
- `C10`: Check test server and transmission issues **← 정답**
- `C11`: Decrease A3 Offset threshold for 3231321_2
- `C12`: Lift the tilt angle  of 3237451_4 by 10 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237451_4
- `C15`: Add neighbor relationship between 3254229_1 and 3237451_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231321_2
- `C17`: Increase transmission power for 3237451_4
- `C18`: Adjust the azimuth of 3231321_2 by 50 degrees
- `C19`: Press down the tilt angle  of 3237451_4 by 10 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231321_2
- `C21`: Decrease A3 Offset threshold for 3237451_4
- `C22`: Decrease transmission power for 3231321_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.465 | MS1 | 121.4656655631 | 31.1446266372 | 479 | 504990 | -91.60 | 12.44 | 459.78 | 0.03 | 2.85 | 1571 |
| 2024-09-20 22:21:32.781 | MS1 | 121.4656667969 | 31.1446202258 | 479 | 504990 | -91.92 | 14.89 | 366.81 | 0.19 | 2.46 | 1592 |
| 2024-09-20 22:21:33.454 | MS1 | 121.4656742127 | 31.1446332227 | 479 | 504990 | -87.04 | 14.17 | 568.00 | 0.04 | 2.32 | 1581 |
| 2024-09-20 22:21:34.496 | MS1 | 121.4656744543 | 31.1446255330 | 479 | 504990 | -91.25 | 14.21 | 76.90 | 0.01 | 2.62 | 381 |
| 2024-09-20 22:21:35.584 | MS1 | 121.4656772830 | 31.1446287432 | 479 | 504990 | -86.13 | 17.32 | 84.44 | 0.12 | 2.23 | 309 |
| 2024-09-20 22:21:36.232 | MS1 | 121.4656764335 | 31.1446304282 | 479 | 504990 | -86.96 | 16.12 | 66.99 | 0.02 | 2.72 | 468 |
| 2024-09-20 22:21:37.798 | MS1 | 121.4656690526 | 31.1446180993 | 479 | 504990 | -89.53 | 10.03 | 91.38 | 0.01 | 2.64 | 341 |
| 2024-09-20 22:21:38.473 | MS1 | 121.4656779996 | 31.1446331223 | 479 | 504990 | -89.90 | 8.49 | 80.20 | 0.14 | 2.13 | 388 |
| 2024-09-20 22:21:39.741 | MS1 | 121.4656593459 | 31.1446316312 | 479 | 504990 | -91.80 | 12.17 | 71.01 | 0.01 | 2.54 | 489 |
| 2024-09-20 22:21:40.397 | MS1 | 121.4656587058 | 31.1446280859 | 479 | 504990 | -91.70 | 9.18 | 420.87 | 0.11 | 2.63 | 1586 |
| 2024-09-20 22:21:41.137 | MS1 | 121.4656683796 | 31.1446231808 | 479 | 504990 | -92.25 | 8.81 | 485.81 | 0.04 | 2.40 | 1583 |
| 2024-09-20 22:21:42.437 | MS1 | 121.4656599121 | 31.1446338175 | 479 | 504990 | -92.62 | 10.10 | 442.58 | 0.04 | 2.73 | 1563 |

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
| 3231019 | 3 | 121.4673865209 | 31.1510168043 | 205 | 1 | 3 | 42.0 | TDD | 630 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3231321 | 2 | 121.4728749397 | 31.1536276187 | 82 | 13 | 2 | 32.9 | TDD | 479 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3237451 | 4 | 121.4671485845 | 31.1446379059 | 31 | 3 | 4 | 17.0 | TDD | 6 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3254229 | 1 | 121.4742654766 | 31.1521216887 | 172 | 7 | 2 | 42.5 | TDD | 297 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.428 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.447 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.566 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.566 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.262 | NREventA3 | measId:2;ServCellPCI:685;Se... |
| 2024-09-20 22:21:38.502 | NRHandoverAttempt | SourcePCI:685;SourceNR-ARFC... |
| 2024-09-20 22:21:38.549 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.563 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.706 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.706 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254229 | 1 | 6.1723 | 17.0681 | -116.2890 | 11.3214 | 152.5479 | 0.0089 | 0.0118 |
| 2024_09_20 22:00 | 3231321 | 2 | 17.6187 | 6.3662 | -116.3656 | 12.2162 | 88.2875 | 0.0105 | 0.0180 |
| 2024_09_20 22:00 | 3231019 | 3 | 14.9136 | 17.8621 | -114.8506 | 19.5774 | 84.1554 | 0.0056 | 0.0190 |
| 2024_09_20 22:00 | 3237451 | 4 | 19.7020 | 7.5498 | -116.9834 | 12.7244 | 150.6718 | 0.0039 | 0.0042 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413456_4A09212E | 504990 | 479 | -91.1 | 504990 | 6 | -94.8 | 504990 | 297 | -102.9 | 504990 | 630 |
| MR_1774413456_61DEC684 | 504990 | 479 | -91.4 | 504990 | 6 | -94.6 | 504990 | 297 | -102.0 | 504990 | 630 |
| MR_1774413456_00157736 | 504990 | 479 | -89.5 | 504990 | 6 | -95.5 | 504990 | 297 | -100.8 | 504990 | 630 |
| MR_1774413456_500EAD86 | 504990 | 479 | -91.2 | 504990 | 6 | -97.9 | 504990 | 297 | -100.9 | 504990 | 630 |
| MR_1774413456_5395E1A0 | 504990 | 479 | -92.3 | 504990 | 6 | -96.3 | 504990 | 297 | -99.8 | 504990 | 630 |
| MR_1774413456_F5115018 | 504990 | 479 | -93.1 | 504990 | 6 | -97.4 | 504990 | 297 | -102.5 | 504990 | 630 |
| MR_1774413456_1526D5D0 | 504990 | 479 | -89.7 | 504990 | 6 | -97.0 | 504990 | 297 | -100.5 | 504990 | 630 |
| MR_1774413456_CF1FDDEA | 504990 | 479 | -92.4 | 504990 | 6 | -95.7 | 504990 | 297 | -100.6 | 504990 | 630 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1901: `dbb1f7f9-e37...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dbb1f7f9-e37b-46ea-9c52-02e3b69b45ee` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease A3 Offset threshold for 3247740_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1901] topology](images/train_1901.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3247740_2
- `C2`: Increase A3 Offset threshold for 3274934_3
- `C3`: Increase transmission power for 3247740_2
- `C4`: Add neighbor relationship between 3228484_1 and 3274934_3
- `C5`: Decrease A3 Offset threshold for 3274934_3
- `C6`: Adjust the azimuth of 3247740_2 by 50 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247740_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274934_3
- `C9`: Add neighbor relationship between 3247740_2 and 3274934_3
- `C10`: Adjust the azimuth of 3274934_3 by 50 degrees
- `C11`: Increase transmission power for 3274934_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247740_2
- `C13`: Press down the tilt angle  of 3274934_3 by 10 degrees
- `C14`: Decrease A3 Offset threshold for 3247740_2 **← 정답**
- `C15`: Check test server and transmission issues
- `C16`: Press down the tilt angle of 3247740_2 by 4 degrees
- `C17`: Lift the tilt angle  of 3274934_3 by 10 degrees
- `C18`: Lift the tilt angle of 3247740_2 by 4 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease transmission power for 3274934_3
- `C21`: Decrease transmission power for 3247740_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274934_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.124 | MS1 | 121.4656745894 | 31.1446288331 | 988 | 504990 | -80.90 | 17.16 | 376.41 | 0.02 | 2.43 | 1571 |
| 2024-09-20 22:21:32.831 | MS1 | 121.4656737101 | 31.1446342555 | 988 | 504990 | -78.98 | 12.99 | 564.39 | 0.05 | 2.53 | 1598 |
| 2024-09-20 22:21:33.593 | MS1 | 121.4656691667 | 31.1446291980 | 988 | 504990 | -75.85 | 14.02 | 442.22 | 0.14 | 2.32 | 1599 |
| 2024-09-20 22:21:34.662 | MS1 | 121.4656587552 | 31.1446182853 | 988 | 504990 | -85.84 | -1.01 | 39.21 | 0.05 | 1.40 | 1593 |
| 2024-09-20 22:21:35.299 | MS1 | 121.4656737621 | 31.1446199973 | 988 | 504990 | -85.55 | -3.24 | 65.73 | 0.08 | 1.47 | 1561 |
| 2024-09-20 22:21:36.776 | MS1 | 121.4656591715 | 31.1446285034 | 988 | 504990 | -86.42 | -1.94 | 49.47 | 0.00 | 1.49 | 1594 |
| 2024-09-20 22:21:37.991 | MS1 | 121.4656746707 | 31.1446352408 | 988 | 504990 | -87.10 | -3.58 | 30.64 | 0.03 | 1.06 | 1571 |
| 2024-09-20 22:21:38.150 | MS1 | 121.4656614342 | 31.1446256391 | 988 | 504990 | -86.33 | -1.52 | 55.54 | 0.10 | 1.36 | 1572 |
| 2024-09-20 22:21:39.486 | MS1 | 121.4656655076 | 31.1446271961 | 710 | 504990 | -81.73 | 14.70 | 225.90 | 0.01 | 1.19 | 1573 |
| 2024-09-20 22:21:40.149 | MS1 | 121.4656727594 | 31.1446309607 | 710 | 504990 | -82.13 | 15.56 | 564.77 | 0.16 | 2.36 | 1572 |
| 2024-09-20 22:21:41.533 | MS1 | 121.4656674183 | 31.1446285590 | 710 | 504990 | -75.90 | 16.90 | 451.57 | 0.09 | 2.65 | 1573 |
| 2024-09-20 22:21:42.964 | MS1 | 121.4656618311 | 31.1446370236 | 710 | 504990 | -84.94 | 12.97 | 571.46 | 0.04 | 2.14 | 1575 |

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
| 3228484 | 1 | 121.4744164634 | 31.1449146653 | 267 | 0 | 11 | 24.7 | TDD | 907 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3247740 | 2 | 121.4667092412 | 31.1544950627 | 107 | 3 | 7 | 27.9 | TDD | 988 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3254013 | 4 | 121.4675217755 | 31.1502357395 | 127 | 14 | 2 | 20.8 | TDD | 831 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3274934 | 3 | 121.4685028282 | 31.1449727555 | 161 | 9 | 8 | 29.6 | TDD | 710 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.064 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.086 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.230 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.230 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.881 | NREventA3 | measId:2;ServCellPCI:122;Se... |
| 2024-09-20 22:21:38.121 | NRHandoverAttempt | SourcePCI:122;SourceNR-ARFC... |
| 2024-09-20 22:21:38.160 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.170 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.283 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.283 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228484 | 1 | 18.1362 | 7.3041 | -115.6244 | 5.4618 | 197.2520 | 0.0014 | 0.0064 |
| 2024_09_20 22:00 | 3247740 | 2 | 7.6813 | 5.2180 | -117.1639 | 8.0470 | 192.7276 | 0.0041 | 0.1286 |
| 2024_09_20 22:00 | 3274934 | 3 | 16.1721 | 8.7934 | -116.6822 | 18.1868 | 181.4290 | 0.0126 | 0.0011 |
| 2024_09_20 22:00 | 3254013 | 4 | 13.7602 | 12.0859 | -116.5680 | 18.5586 | 93.2187 | 0.0134 | 0.0134 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415955_E477BC38 | 504990 | 988 | -84.4 | 504990 | 710 | -81.8 | 504990 | 907 | -82.4 | 504990 | 831 |
| MR_1774415955_8C2FC508 | 504990 | 988 | -85.9 | 504990 | 710 | -78.9 | 504990 | 907 | -82.8 | 504990 | 831 |
| MR_1774415955_B35E2FE5 | 504990 | 710 | -80.0 | 504990 | 988 | -86.5 | 504990 | 907 | -82.6 | 504990 | 831 |
| MR_1774415955_194D9797 | 504990 | 710 | -79.0 | 504990 | 988 | -85.2 | 504990 | 907 | -81.4 | 504990 | 831 |
| MR_1774415955_29EDE338 | 504990 | 710 | -78.8 | 504990 | 988 | -87.0 | 504990 | 907 | -82.1 | 504990 | 831 |
| MR_1774415955_2308FD77 | 504990 | 710 | -80.2 | 504990 | 988 | -87.5 | 504990 | 907 | -83.2 | 504990 | 831 |
| MR_1774415955_E3D22A6A | 504990 | 710 | -81.5 | 504990 | 988 | -86.2 | 504990 | 907 | -85.2 | 504990 | 831 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1902: `74b589e5-ed1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `74b589e5-ed11-466d-8aed-345339504fa0` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3252726_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1902] topology](images/train_1902.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218417_3
- `C3`: Adjust the azimuth of 3218417_3 by 50 degrees
- `C4`: Decrease transmission power for 3252726_2
- `C5`: Add neighbor relationship between 3252726_2 and 3218417_3
- `C6`: Increase transmission power for 3252726_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252726_2
- `C8`: Decrease transmission power for 3218417_3
- `C9`: Check test server and transmission issues
- `C10`: Add neighbor relationship between 3267333_1 and 3218417_3
- `C11`: Lift the tilt angle of 3252726_2 by 4 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218417_3
- `C13`: Lift the tilt angle  of 3218417_3 by 6 degrees
- `C14`: Decrease A3 Offset threshold for 3252726_2
- `C15`: Increase A3 Offset threshold for 3252726_2
- `C16`: Press down the tilt angle of 3252726_2 by 4 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252726_2 **← 정답**
- `C18`: Press down the tilt angle  of 3218417_3 by 6 degrees
- `C19`: Increase A3 Offset threshold for 3218417_3
- `C20`: Decrease A3 Offset threshold for 3218417_3
- `C21`: Increase transmission power for 3218417_3
- `C22`: Adjust the azimuth of 3252726_2 by 1 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.646 | MS1 | 121.4656737530 | 31.1446320329 | 346 | 504990 | -86.14 | 17.09 | 364.22 | 0.12 | 2.24 | 1592 |
| 2024-09-20 22:21:32.475 | MS1 | 121.4656646344 | 31.1446299236 | 346 | 504990 | -86.72 | 16.00 | 594.63 | 0.17 | 2.24 | 1590 |
| 2024-09-20 22:21:33.451 | MS1 | 121.4656689634 | 31.1446327681 | 346 | 504990 | -87.47 | 12.04 | 364.49 | 0.17 | 2.28 | 1586 |
| 2024-09-20 22:21:34.644 | MS1 | 121.4656646057 | 31.1446272579 | 346 | 504990 | -88.09 | 14.65 | 82.28 | 0.56 | 2.93 | 628 |
| 2024-09-20 22:21:35.842 | MS1 | 121.4656696124 | 31.1446347591 | 346 | 504990 | -90.04 | 15.96 | 80.34 | 0.59 | 2.29 | 609 |
| 2024-09-20 22:21:36.283 | MS1 | 121.4656596274 | 31.1446241555 | 346 | 504990 | -86.66 | 16.17 | 73.39 | 0.52 | 2.97 | 506 |
| 2024-09-20 22:21:37.481 | MS1 | 121.4656646817 | 31.1446192723 | 346 | 504990 | -91.15 | 10.80 | 97.66 | 0.69 | 2.77 | 657 |
| 2024-09-20 22:21:38.639 | MS1 | 121.4656592119 | 31.1446365633 | 346 | 504990 | -90.07 | 10.00 | 78.16 | 0.64 | 2.40 | 638 |
| 2024-09-20 22:21:39.420 | MS1 | 121.4656602870 | 31.1446323783 | 346 | 504990 | -89.11 | 10.38 | 79.76 | 0.58 | 2.79 | 649 |
| 2024-09-20 22:21:40.737 | MS1 | 121.4656744331 | 31.1446288203 | 346 | 504990 | -89.40 | 10.45 | 330.00 | 0.11 | 2.62 | 1566 |
| 2024-09-20 22:21:41.865 | MS1 | 121.4656717328 | 31.1446339159 | 346 | 504990 | -89.63 | 11.05 | 439.17 | 0.10 | 2.32 | 1597 |
| 2024-09-20 22:21:42.965 | MS1 | 121.4656668302 | 31.1446289710 | 346 | 504990 | -91.10 | 11.55 | 409.49 | 0.06 | 2.79 | 1596 |

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
| 3218417 | 3 | 121.4698276002 | 31.1497623991 | 43 | 3 | 7 | 39.4 | TDD | 3 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3221028 | 4 | 121.4720951212 | 31.1509622475 | 170 | 9 | 0 | 15.6 | TDD | 981 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3252726 | 2 | 121.4661038346 | 31.1502554651 | 185 | 0 | 12 | 47.1 | TDD | 346 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3267333 | 1 | 121.4696274866 | 31.1495033844 | 350 | 11 | 3 | 21.2 | TDD | 393 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.128 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.144 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.265 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.265 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.931 | NREventA3 | measId:2;ServCellPCI:40;Ser... |
| 2024-09-20 22:21:38.171 | NRHandoverAttempt | SourcePCI:40;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.202 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.213 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.361 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.361 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267333 | 1 | 6.7448 | 16.0867 | -116.3639 | 19.9003 | 130.6851 | 0.0083 | 0.0149 |
| 2024_09_20 22:00 | 3252726 | 2 | 10.6467 | 11.0832 | -114.6667 | 7.6716 | 81.7782 | 0.0025 | 0.0148 |
| 2024_09_20 22:00 | 3218417 | 3 | 6.5653 | 9.0417 | -115.3164 | 6.8274 | 161.0045 | 0.0139 | 0.0013 |
| 2024_09_20 22:00 | 3221028 | 4 | 18.5185 | 13.9538 | -114.6130 | 18.0372 | 109.1296 | 0.0129 | 0.0137 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413929_7EE03CAF | 504990 | 346 | -89.6 | 504990 | 3 | -87.2 | 504990 | 393 | -97.5 | 504990 | 981 |
| MR_1774413929_6F02BC5A | 504990 | 346 | -87.1 | 504990 | 3 | -89.8 | 504990 | 393 | -98.6 | 504990 | 981 |
| MR_1774413929_4EC5F8E4 | 504990 | 346 | -89.9 | 504990 | 3 | -88.7 | 504990 | 393 | -99.0 | 504990 | 981 |
| MR_1774413929_C3952CF2 | 504990 | 346 | -87.7 | 504990 | 3 | -87.6 | 504990 | 393 | -97.2 | 504990 | 981 |
| MR_1774413929_E7B1A261 | 504990 | 346 | -87.8 | 504990 | 3 | -90.0 | 504990 | 393 | -98.2 | 504990 | 981 |
| MR_1774413929_AC1C6D03 | 504990 | 346 | -87.2 | 504990 | 3 | -89.0 | 504990 | 393 | -99.4 | 504990 | 981 |
| MR_1774413929_7090C0F3 | 504990 | 346 | -87.8 | 504990 | 3 | -89.5 | 504990 | 393 | -99.3 | 504990 | 981 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1903: `8ab23cb4-c30...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8ab23cb4-c307-4c44-8b2c-2e1567b38bfc` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Add neighbor relationship between 3255813_4 and 3231340_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1903] topology](images/train_1903.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3255813_4 and 3231340_2 **← 정답**
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255813_4
- `C3`: Decrease A3 Offset threshold for 3255813_4
- `C4`: Lift the tilt angle  of 3231340_2 by 4 degrees
- `C5`: Increase transmission power for 3231340_2
- `C6`: Add neighbor relationship between 3276259_1 and 3231340_2
- `C7`: Increase A3 Offset threshold for 3255813_4
- `C8`: Increase A3 Offset threshold for 3231340_2
- `C9`: Decrease transmission power for 3255813_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231340_2
- `C11`: Increase transmission power for 3255813_4
- `C12`: Adjust the azimuth of 3255813_4 by 46 degrees
- `C13`: Press down the tilt angle of 3255813_4 by 10 degrees
- `C14`: Decrease transmission power for 3231340_2
- `C15`: Check test server and transmission issues
- `C16`: Decrease A3 Offset threshold for 3231340_2
- `C17`: Lift the tilt angle of 3255813_4 by 10 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Press down the tilt angle  of 3231340_2 by 4 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255813_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231340_2
- `C22`: Adjust the azimuth of 3231340_2 by 34 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.396 | MS1 | 121.4656727454 | 31.1446195314 | 998 | 504990 | -76.33 | 13.69 | 480.82 | 0.10 | 2.93 | 1593 |
| 2024-09-20 22:21:32.987 | MS1 | 121.4656640576 | 31.1446237281 | 998 | 504990 | -79.90 | 16.13 | 338.07 | 0.02 | 2.38 | 1594 |
| 2024-09-20 22:21:33.864 | MS1 | 121.4656779303 | 31.1446233339 | 998 | 504990 | -77.15 | 16.61 | 565.01 | 0.19 | 2.81 | 1600 |
| 2024-09-20 22:21:34.444 | MS1 | 121.4656759268 | 31.1446256067 | 998 | 504990 | -93.58 | -0.97 | 51.61 | 0.00 | 1.30 | 1568 |
| 2024-09-20 22:21:35.659 | MS1 | 121.4656730478 | 31.1446201498 | 998 | 504990 | -91.57 | -0.82 | 42.78 | 0.06 | 1.47 | 1563 |
| 2024-09-20 22:21:36.487 | MS1 | 121.4656730529 | 31.1446371528 | 998 | 504990 | -89.07 | -3.53 | 47.18 | 0.18 | 1.23 | 1576 |
| 2024-09-20 22:21:37.382 | MS1 | 121.4656672611 | 31.1446189314 | 998 | 504990 | -85.73 | -0.81 | 58.40 | 0.19 | 1.46 | 1578 |
| 2024-09-20 22:21:38.396 | MS1 | 121.4656608620 | 31.1446365285 | 998 | 504990 | -78.13 | 14.89 | 594.68 | 0.16 | 1.30 | 1596 |
| 2024-09-20 22:21:39.830 | MS1 | 121.4656615061 | 31.1446297500 | 998 | 504990 | -84.06 | 13.15 | 366.91 | 0.07 | 1.43 | 1597 |
| 2024-09-20 22:21:40.399 | MS1 | 121.4656716295 | 31.1446211454 | 998 | 504990 | -81.15 | 17.01 | 347.85 | 0.14 | 2.91 | 1562 |
| 2024-09-20 22:21:41.950 | MS1 | 121.4656623925 | 31.1446243654 | 998 | 504990 | -75.36 | 15.88 | 370.59 | 0.02 | 2.32 | 1588 |
| 2024-09-20 22:21:42.669 | MS1 | 121.4656664033 | 31.1446271107 | 998 | 504990 | -84.33 | 17.67 | 302.04 | 0.10 | 2.23 | 1576 |

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
| 3231340 | 2 | 121.4707882605 | 31.1489980252 | 191 | 2 | 0 | 28.9 | TDD | 726 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3234534 | 3 | 121.4713569587 | 31.1499467880 | 270 | 15 | 3 | 15.6 | TDD | 566 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3255813 | 4 | 121.4754190076 | 31.1526648346 | 180 | 8 | 0 | 40.1 | TDD | 998 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3276259 | 1 | 121.4710838251 | 31.1545852746 | 344 | 10 | 11 | 28.0 | TDD | 137 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.915 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.931 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.060 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.060 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.775 | NREventA3 | measId:2;ServCellPCI:234;Se... |
| 2024-09-20 22:21:35.775 | NREventA3 | measId:2;ServCellPCI:234;Se... |
| 2024-09-20 22:21:36.775 | NREventA3 | measId:2;ServCellPCI:234;Se... |
| 2024-09-20 22:21:39.275 | NRRRCReestablishAttempt | PCI:234 |
| 2024-09-20 22:21:39.293 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.305 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.432 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.432 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276259 | 1 | 16.7484 | 19.3632 | -116.2831 | 8.1108 | 150.0982 | 0.0198 | 0.0170 |
| 2024_09_20 22:00 | 3231340 | 2 | 5.6004 | 19.8553 | -117.2788 | 17.9269 | 140.5730 | 0.0063 | 0.0069 |
| 2024_09_20 22:00 | 3234534 | 3 | 19.3334 | 8.3079 | -115.8745 | 16.0321 | 151.6052 | 0.0035 | 0.0043 |
| 2024_09_20 22:00 | 3255813 | 4 | 14.7287 | 8.4655 | -117.7954 | 14.2187 | 131.2172 | 0.0195 | 0.1848 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416874_3355CC62 | 504990 | 998 | -91.8 | 504990 | 726 | -86.5 | 504990 | 137 | -89.7 | 504990 | 566 |
| MR_1774416874_9F0FF8D9 | 504990 | 726 | -89.2 | 504990 | 998 | -93.0 | 504990 | 137 | -92.5 | 504990 | 566 |
| MR_1774416874_6BF96281 | 504990 | 998 | -94.5 | 504990 | 726 | -88.6 | 504990 | 137 | -91.9 | 504990 | 566 |
| MR_1774416874_3725EFC5 | 504990 | 726 | -88.3 | 504990 | 998 | -93.3 | 504990 | 137 | -89.9 | 504990 | 566 |
| MR_1774416874_1BB03C72 | 504990 | 998 | -95.1 | 504990 | 726 | -88.3 | 504990 | 137 | -90.5 | 504990 | 566 |
| MR_1774416874_0B74D103 | 504990 | 726 | -88.5 | 504990 | 998 | -93.5 | 504990 | 137 | -92.3 | 504990 | 566 |
| MR_1774416874_6EABF579 | 504990 | 726 | -87.2 | 504990 | 998 | -92.6 | 504990 | 137 | -89.8 | 504990 | 566 |
| MR_1774416874_16A91059 | 504990 | 998 | -93.7 | 504990 | 726 | -88.3 | 504990 | 137 | -91.4 | 504990 | 566 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1904: `c5adb6b0-d14...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c5adb6b0-d142-4800-96b4-e2aedceb90e5` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Lift the tilt angle  of 3271207_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1904] topology](images/train_1904.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3241817_1 and 3232652_2
- `C2`: Check test server and transmission issues
- `C3`: Decrease transmission power for 3241817_1
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease A3 Offset threshold for 3241817_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232652_2
- `C7`: Press down the tilt angle of 3241817_1 by 4 degrees
- `C8`: Increase A3 Offset threshold for 3241817_1
- `C9`: Lift the tilt angle of 3241817_1 by 4 degrees
- `C10`: Lift the tilt angle  of 3271207_4 by 10 degrees **← 정답**
- `C11`: Increase A3 Offset threshold for 3232652_2
- `C12`: Adjust the azimuth of 3271207_4 by 50 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241817_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241817_1
- `C15`: Add neighbor relationship between 3271207_4 and 3232652_2
- `C16`: Adjust the azimuth of 3241817_1 by 28 degrees
- `C17`: Increase transmission power for 3232652_2
- `C18`: Decrease A3 Offset threshold for 3232652_2
- `C19`: Decrease transmission power for 3232652_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232652_2
- `C21`: Press down the tilt angle  of 3271207_4 by 10 degrees
- `C22`: Increase transmission power for 3241817_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.442 | MS1 | 121.4656580444 | 31.1446221789 | 40 | 504990 | -87.36 | 14.28 | 470.03 | 0.03 | 2.01 | 1579 |
| 2024-09-20 22:21:32.268 | MS1 | 121.4656777600 | 31.1446364937 | 40 | 504990 | -85.02 | 15.23 | 387.85 | 0.07 | 2.17 | 1566 |
| 2024-09-20 22:21:33.636 | MS1 | 121.4656735904 | 31.1446286601 | 40 | 504990 | -87.10 | 16.05 | 298.08 | 0.15 | 2.49 | 1599 |
| 2024-09-20 22:21:34.659 | MS1 | 121.4656751726 | 31.1446375143 | 40 | 504990 | -88.19 | 16.49 | 80.65 | 0.04 | 2.76 | 1570 |
| 2024-09-20 22:21:35.855 | MS1 | 121.4656598345 | 31.1446257758 | 40 | 504990 | -88.37 | 15.88 | 47.21 | 0.03 | 2.80 | 1592 |
| 2024-09-20 22:21:36.938 | MS1 | 121.4656642441 | 31.1446343714 | 40 | 504990 | -90.86 | 16.16 | 89.68 | 0.16 | 2.22 | 1587 |
| 2024-09-20 22:21:37.958 | MS1 | 121.4656628975 | 31.1446203332 | 40 | 504990 | -93.86 | 10.85 | 82.91 | 0.05 | 2.98 | 1561 |
| 2024-09-20 22:21:38.898 | MS1 | 121.4656672218 | 31.1446287021 | 40 | 504990 | -89.34 | 8.94 | 70.13 | 0.01 | 2.14 | 1595 |
| 2024-09-20 22:21:39.496 | MS1 | 121.4656688773 | 31.1446200454 | 40 | 504990 | -92.48 | 8.51 | 59.66 | 0.18 | 2.12 | 1584 |
| 2024-09-20 22:21:40.206 | MS1 | 121.4656618480 | 31.1446378739 | 40 | 504990 | -89.17 | 11.20 | 448.97 | 0.05 | 2.53 | 1572 |
| 2024-09-20 22:21:41.529 | MS1 | 121.4656671005 | 31.1446218694 | 40 | 504990 | -90.92 | 12.10 | 449.31 | 0.18 | 2.74 | 1561 |
| 2024-09-20 22:21:42.616 | MS1 | 121.4656757574 | 31.1446181132 | 40 | 504990 | -92.52 | 9.23 | 293.84 | 0.05 | 2.23 | 1582 |

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
| 3232652 | 2 | 121.4671402787 | 31.1466109048 | 348 | 6 | 6 | 41.6 | TDD | 359 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3241817 | 1 | 121.4735652281 | 31.1442429115 | 245 | 3 | 10 | 15.4 | TDD | 40 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3254815 | 3 | 121.4683469371 | 31.1536873476 | 42 | 2 | 6 | 42.2 | TDD | 85 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3271207 | 4 | 121.4684320881 | 31.1493725431 | 97 | 15 | 0 | 34.5 | TDD | 503 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.352 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.372 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.482 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.482 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.216 | NREventA3 | measId:2;ServCellPCI:282;Se... |
| 2024-09-20 22:21:38.456 | NRHandoverAttempt | SourcePCI:282;SourceNR-ARFC... |
| 2024-09-20 22:21:38.494 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.508 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.635 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.635 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241817 | 1 | 75.5368 | 94.3947 | -114.2918 | 14.5925 | 108.3249 | 0.0157 | 0.0094 |
| 2024_09_20 22:00 | 3232652 | 2 | 5.3879 | 9.9818 | -114.7093 | 17.9865 | 130.3228 | 0.0035 | 0.0179 |
| 2024_09_20 22:00 | 3254815 | 3 | 10.6690 | 7.9487 | -115.2199 | 17.7354 | 84.4032 | 0.0072 | 0.0134 |
| 2024_09_20 22:00 | 3271207 | 4 | 12.5418 | 5.4258 | -116.4857 | 9.7369 | 106.4130 | 0.0165 | 0.0198 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413256_9442C719 | 504990 | 40 | -87.6 | 504990 | 359 | -97.8 | 504990 | 503 | -95.7 | 504990 | 85 |
| MR_1774413256_9A33315E | 504990 | 40 | -86.6 | 504990 | 359 | -96.9 | 504990 | 503 | -96.2 | 504990 | 85 |
| MR_1774413256_E75601BC | 504990 | 40 | -87.8 | 504990 | 359 | -98.5 | 504990 | 503 | -95.3 | 504990 | 85 |
| MR_1774413256_92D9A6DE | 504990 | 40 | -90.1 | 504990 | 359 | -96.8 | 504990 | 503 | -98.0 | 504990 | 85 |
| MR_1774413256_8F540A46 | 504990 | 40 | -88.9 | 504990 | 359 | -94.9 | 504990 | 503 | -95.5 | 504990 | 85 |
| MR_1774413256_97260A3C | 504990 | 40 | -87.6 | 504990 | 359 | -98.1 | 504990 | 503 | -98.3 | 504990 | 85 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1905: `8820a8fd-b3b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8820a8fd-b3b2-4375-a5a0-5d3c53298442` |
| Tag | **multiple-answer** |
| 정답 | **C3|C12|C15|C20** |
| C3 의미 | Increase A3 Offset threshold for 3270241_4 |
| C12 의미 | Increase A3 Offset threshold for 3264447_1 |
| C15 의미 | Press down the tilt angle  of 3270241_4 by 4 degrees |
| C20 의미 | Decrease transmission power for 3270241_4 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1905] topology](images/train_1905.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3270241_4
- `C2`: Lift the tilt angle of 3264447_1 by 3 degrees
- `C3`: Increase A3 Offset threshold for 3270241_4 **← 정답**
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270241_4
- `C5`: Press down the tilt angle of 3264447_1 by 3 degrees
- `C6`: Decrease A3 Offset threshold for 3264447_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270241_4
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Add neighbor relationship between 3215539_2 and 3270241_4
- `C10`: Adjust the azimuth of 3264447_1 by 21 degrees
- `C11`: Increase transmission power for 3264447_1
- `C12`: Increase A3 Offset threshold for 3264447_1 **← 정답**
- `C13`: Decrease A3 Offset threshold for 3270241_4
- `C14`: Lift the tilt angle  of 3270241_4 by 4 degrees
- `C15`: Press down the tilt angle  of 3270241_4 by 4 degrees **← 정답**
- `C16`: Add neighbor relationship between 3264447_1 and 3270241_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264447_1
- `C18`: Check test server and transmission issues
- `C19`: Adjust the azimuth of 3270241_4 by 31 degrees
- `C20`: Decrease transmission power for 3270241_4 **← 정답**
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264447_1
- `C22`: Decrease transmission power for 3264447_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.156 | MS1 | 121.4656774760 | 31.1446239505 | 161 | 504990 | -78.03 | 15.80 | 296.51 | 0.20 | 2.69 | 1597 |
| 2024-09-20 22:21:32.449 | MS1 | 121.4656598789 | 31.1446360779 | 161 | 504990 | -82.68 | 16.35 | 464.62 | 0.15 | 2.17 | 1590 |
| 2024-09-20 22:21:33.361 | MS1 | 121.4656704455 | 31.1446225023 | 161 | 504990 | -75.28 | 14.40 | 520.90 | 0.09 | 2.47 | 1570 |
| 2024-09-20 22:21:34.441 | MS1 | 121.4656593067 | 31.1446252439 | 614 | 504990 | -87.52 | 3.77 | 61.30 | 0.09 | 1.38 | 1574 |
| 2024-09-20 22:21:35.167 | MS1 | 121.4656582023 | 31.1446333034 | 614 | 504990 | -89.19 | 3.38 | 59.31 | 0.01 | 1.00 | 1597 |
| 2024-09-20 22:21:36.540 | MS1 | 121.4656773672 | 31.1446221463 | 161 | 504990 | -81.98 | 2.64 | 76.05 | 0.17 | 1.14 | 1576 |
| 2024-09-20 22:21:37.731 | MS1 | 121.4656624878 | 31.1446316795 | 161 | 504990 | -81.60 | 2.35 | 40.60 | 0.07 | 1.27 | 1582 |
| 2024-09-20 22:21:38.681 | MS1 | 121.4656742169 | 31.1446270624 | 614 | 504990 | -81.65 | 2.30 | 76.52 | 0.06 | 1.29 | 1581 |
| 2024-09-20 22:21:39.864 | MS1 | 121.4656609159 | 31.1446190534 | 614 | 504990 | -86.06 | 3.89 | 69.46 | 0.19 | 1.11 | 1598 |
| 2024-09-20 22:21:40.643 | MS1 | 121.4656713311 | 31.1446362405 | 614 | 504990 | -76.46 | 17.72 | 560.61 | 0.10 | 2.37 | 1584 |
| 2024-09-20 22:21:41.638 | MS1 | 121.4656584601 | 31.1446312649 | 614 | 504990 | -75.51 | 15.54 | 441.55 | 0.12 | 2.57 | 1567 |
| 2024-09-20 22:21:42.753 | MS1 | 121.4656635313 | 31.1446293827 | 614 | 504990 | -78.61 | 13.06 | 486.82 | 0.09 | 2.38 | 1579 |

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
| 3215539 | 2 | 121.4724333898 | 31.1483992764 | 278 | 11 | 0 | 25.0 | TDD | 803 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3228172 | 3 | 121.4691724601 | 31.1482578266 | 13 | 10 | 5 | 24.8 | TDD | 614 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3249626 | 5 | 121.4709192317 | 31.1481145896 | 215 | 14 | 8 | 22.7 | TDD | 302 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3264447 | 1 | 121.4748286702 | 31.1500834193 | 256 | 2 | 4 | 16.2 | TDD | 161 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3270241 | 4 | 121.4734404938 | 31.1555999256 | 180 | 3 | 3 | 32.6 | TDD | 646 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.013 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.036 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.149 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.149 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.894 | NREventA3 | measId:2;ServCellPCI:443;Se... |
| 2024-09-20 22:21:34.134 | NRHandoverAttempt | SourcePCI:443;SourceNR-ARFC... |
| 2024-09-20 22:21:34.165 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.177 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:34.302 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.302 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.894 | NREventA3 | measId:2;ServCellPCI:860;Se... |
| 2024-09-20 22:21:36.134 | NRHandoverAttempt | SourcePCI:860;SourceNR-ARFC... |
| 2024-09-20 22:21:36.169 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.180 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.314 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.314 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.894 | NREventA3 | measId:2;ServCellPCI:443;Se... |
| 2024-09-20 22:21:38.134 | NRHandoverAttempt | SourcePCI:443;SourceNR-ARFC... |
| 2024-09-20 22:21:38.182 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.197 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.332 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.332 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264447 | 1 | 6.1264 | 15.3641 | -116.1685 | 11.0349 | 99.6601 | 0.0064 | 0.0178 |
| 2024_09_20 22:00 | 3215539 | 2 | 9.6722 | 13.4635 | -115.8094 | 6.1165 | 84.9976 | 0.0088 | 0.0176 |
| 2024_09_20 22:00 | 3228172 | 3 | 12.6626 | 16.7294 | -115.5952 | 5.7064 | 114.9770 | 0.0065 | 0.0178 |
| 2024_09_20 22:00 | 3270241 | 4 | 14.3739 | 19.7762 | -117.5576 | 15.5558 | 133.7022 | 0.0134 | 0.0013 |
| 2024_09_20 22:00 | 3249626 | 5 | 14.3260 | 7.6167 | -115.2616 | 11.8382 | 165.9530 | 0.0106 | 0.0109 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414747_62E23633 | 504990 | 614 | -86.8 | 504990 | 161 | -84.0 | 504990 | 646 | -88.1 | 504990 | 803 |
| MR_1774414747_D4CD17D8 | 504990 | 614 | -87.4 | 504990 | 161 | -83.2 | 504990 | 646 | -84.8 | 504990 | 803 |
| MR_1774414747_48348D97 | 504990 | 614 | -88.7 | 504990 | 161 | -81.3 | 504990 | 646 | -86.6 | 504990 | 803 |
| MR_1774414747_1D92899F | 504990 | 614 | -89.4 | 504990 | 161 | -83.3 | 504990 | 646 | -85.0 | 504990 | 803 |
| MR_1774414747_B25BA70F | 504990 | 614 | -86.2 | 504990 | 161 | -83.5 | 504990 | 646 | -86.9 | 504990 | 803 |
| MR_1774414747_BEC38BBA | 504990 | 614 | -88.5 | 504990 | 161 | -84.6 | 504990 | 646 | -88.4 | 504990 | 803 |
| MR_1774414747_54FCDCED | 504990 | 614 | -88.4 | 504990 | 161 | -81.2 | 504990 | 646 | -86.2 | 504990 | 803 |
| MR_1774414747_29C11A89 | 504990 | 161 | -88.6 | 504990 | 614 | -83.3 | 504990 | 646 | -87.6 | 504990 | 803 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1906: `9046da13-369...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9046da13-369f-4fc7-8636-05c9c5f7bc9c` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Lift the tilt angle  of 3232745_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1906] topology](images/train_1906.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3230852_1
- `C2`: Lift the tilt angle of 3230852_1 by 3 degrees
- `C3`: Increase A3 Offset threshold for 3242539_2
- `C4`: Increase A3 Offset threshold for 3230852_1
- `C5`: Adjust the azimuth of 3232745_4 by 50 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230852_1
- `C7`: Decrease transmission power for 3242539_2
- `C8`: Add neighbor relationship between 3232745_4 and 3242539_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242539_2
- `C10`: Decrease A3 Offset threshold for 3242539_2
- `C11`: Decrease A3 Offset threshold for 3230852_1
- `C12`: Increase transmission power for 3242539_2
- `C13`: Press down the tilt angle  of 3232745_4 by 10 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease transmission power for 3230852_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230852_1
- `C17`: Check test server and transmission issues
- `C18`: Adjust the azimuth of 3230852_1 by 31 degrees
- `C19`: Add neighbor relationship between 3230852_1 and 3242539_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242539_2
- `C21`: Lift the tilt angle  of 3232745_4 by 10 degrees **← 정답**
- `C22`: Press down the tilt angle of 3230852_1 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.614 | MS1 | 121.4656636173 | 31.1446325447 | 250 | 504990 | -85.62 | 14.51 | 554.46 | 0.15 | 2.19 | 1576 |
| 2024-09-20 22:21:32.530 | MS1 | 121.4656715931 | 31.1446225898 | 250 | 504990 | -85.15 | 14.44 | 581.70 | 0.19 | 2.20 | 1588 |
| 2024-09-20 22:21:33.441 | MS1 | 121.4656763822 | 31.1446249245 | 250 | 504990 | -85.13 | 15.81 | 391.84 | 0.17 | 2.67 | 1578 |
| 2024-09-20 22:21:34.246 | MS1 | 121.4656667360 | 31.1446379823 | 250 | 504990 | -85.11 | 12.05 | 49.96 | 0.08 | 2.94 | 1585 |
| 2024-09-20 22:21:35.660 | MS1 | 121.4656708612 | 31.1446297088 | 250 | 504990 | -90.34 | 15.32 | 67.09 | 0.11 | 2.21 | 1585 |
| 2024-09-20 22:21:36.594 | MS1 | 121.4656710074 | 31.1446287767 | 250 | 504990 | -89.74 | 16.04 | 49.81 | 0.18 | 2.50 | 1590 |
| 2024-09-20 22:21:37.922 | MS1 | 121.4656665695 | 31.1446304756 | 250 | 504990 | -93.94 | 11.25 | 55.65 | 0.01 | 2.13 | 1567 |
| 2024-09-20 22:21:38.213 | MS1 | 121.4656760785 | 31.1446180237 | 250 | 504990 | -90.76 | 8.45 | 51.94 | 0.01 | 2.09 | 1597 |
| 2024-09-20 22:21:39.999 | MS1 | 121.4656637958 | 31.1446235045 | 250 | 504990 | -90.94 | 9.65 | 72.24 | 0.00 | 2.95 | 1590 |
| 2024-09-20 22:21:40.664 | MS1 | 121.4656591543 | 31.1446258616 | 250 | 504990 | -91.76 | 8.17 | 484.93 | 0.00 | 2.23 | 1597 |
| 2024-09-20 22:21:41.538 | MS1 | 121.4656767501 | 31.1446181798 | 250 | 504990 | -90.88 | 7.17 | 472.51 | 0.10 | 2.77 | 1579 |
| 2024-09-20 22:21:42.437 | MS1 | 121.4656652526 | 31.1446209896 | 250 | 504990 | -92.49 | 9.93 | 300.06 | 0.03 | 2.97 | 1579 |

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
| 3230852 | 1 | 121.4748890804 | 31.1494718250 | 269 | 2 | 3 | 17.9 | TDD | 250 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3232745 | 4 | 121.4698721654 | 31.1458912858 | 78 | 5 | 9 | 34.1 | TDD | 510 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3242539 | 2 | 121.4736368400 | 31.1456243679 | 97 | 12 | 2 | 41.4 | TDD | 987 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3250635 | 3 | 121.4744593355 | 31.1446394397 | 154 | 10 | 12 | 44.2 | TDD | 667 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.450 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.465 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.612 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.612 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.308 | NREventA3 | measId:2;ServCellPCI:79;Ser... |
| 2024-09-20 22:21:38.548 | NRHandoverAttempt | SourcePCI:79;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.589 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.602 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.703 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.703 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230852 | 1 | 81.6624 | 82.2079 | -114.9301 | 6.9668 | 91.2175 | 0.0078 | 0.0176 |
| 2024_09_20 22:00 | 3242539 | 2 | 11.1317 | 8.2231 | -115.1782 | 18.4509 | 103.9876 | 0.0092 | 0.0065 |
| 2024_09_20 22:00 | 3250635 | 3 | 8.9150 | 10.1961 | -116.1015 | 13.3495 | 135.3219 | 0.0114 | 0.0076 |
| 2024_09_20 22:00 | 3232745 | 4 | 10.5492 | 17.1018 | -115.0756 | 6.6576 | 166.3720 | 0.0047 | 0.0021 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416322_C9B18AC7 | 504990 | 250 | -86.8 | 504990 | 987 | -85.7 | 504990 | 510 | -98.4 | 504990 | 667 |
| MR_1774416322_ED070FB7 | 504990 | 250 | -86.1 | 504990 | 987 | -89.0 | 504990 | 510 | -96.7 | 504990 | 667 |
| MR_1774416322_DD008080 | 504990 | 250 | -86.9 | 504990 | 987 | -85.6 | 504990 | 510 | -97.2 | 504990 | 667 |
| MR_1774416322_21CD47B9 | 504990 | 250 | -87.0 | 504990 | 987 | -86.5 | 504990 | 510 | -95.1 | 504990 | 667 |
| MR_1774416322_351F8D6C | 504990 | 250 | -84.9 | 504990 | 987 | -88.0 | 504990 | 510 | -95.3 | 504990 | 667 |
| MR_1774416322_F1908FD5 | 504990 | 250 | -85.3 | 504990 | 987 | -88.1 | 504990 | 510 | -94.9 | 504990 | 667 |
| MR_1774416322_B7756150 | 504990 | 250 | -84.6 | 504990 | 987 | -87.4 | 504990 | 510 | -96.6 | 504990 | 667 |
| MR_1774416322_6A810CD4 | 504990 | 250 | -83.8 | 504990 | 987 | -89.2 | 504990 | 510 | -97.8 | 504990 | 667 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1907: `3d3fb192-1e9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3d3fb192-1e98-4d39-b723-d9813eeab9fc` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1907] topology](images/train_1907.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217997_2
- `C2`: Increase transmission power for 3232403_4
- `C3`: Decrease transmission power for 3232403_4
- `C4`: Decrease transmission power for 3217997_2
- `C5`: Decrease A3 Offset threshold for 3217997_2
- `C6`: Add neighbor relationship between 3239067_1 and 3232403_4
- `C7`: Press down the tilt angle  of 3232403_4 by 10 degrees
- `C8`: Lift the tilt angle of 3217997_2 by 5 degrees
- `C9`: Adjust the azimuth of 3217997_2 by 29 degrees
- `C10`: Increase transmission power for 3217997_2
- `C11`: Lift the tilt angle  of 3232403_4 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232403_4
- `C13`: Check test server and transmission issues **← 정답**
- `C14`: Increase A3 Offset threshold for 3232403_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217997_2
- `C16`: Add neighbor relationship between 3217997_2 and 3232403_4
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Adjust the azimuth of 3232403_4 by 11 degrees
- `C19`: Decrease A3 Offset threshold for 3232403_4
- `C20`: Increase A3 Offset threshold for 3217997_2
- `C21`: Press down the tilt angle of 3217997_2 by 5 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232403_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.236 | MS1 | 121.4656610098 | 31.1446357475 | 132 | 504990 | -87.36 | 15.96 | 507.97 | 0.03 | 2.95 | 1582 |
| 2024-09-20 22:21:32.914 | MS1 | 121.4656753095 | 31.1446187816 | 132 | 504990 | -85.69 | 12.10 | 380.06 | 0.16 | 2.41 | 1561 |
| 2024-09-20 22:21:33.408 | MS1 | 121.4656691169 | 31.1446367796 | 132 | 504990 | -90.47 | 14.50 | 438.04 | 0.10 | 2.82 | 1597 |
| 2024-09-20 22:21:34.306 | MS1 | 121.4656670190 | 31.1446319159 | 132 | 504990 | -87.26 | 14.92 | 79.61 | 0.18 | 2.10 | 314 |
| 2024-09-20 22:21:35.552 | MS1 | 121.4656713283 | 31.1446261106 | 132 | 504990 | -87.88 | 12.58 | 79.97 | 0.11 | 2.04 | 318 |
| 2024-09-20 22:21:36.252 | MS1 | 121.4656779730 | 31.1446261735 | 132 | 504990 | -91.79 | 13.80 | 96.92 | 0.16 | 2.25 | 455 |
| 2024-09-20 22:21:37.835 | MS1 | 121.4656729078 | 31.1446284860 | 132 | 504990 | -89.32 | 9.30 | 101.20 | 0.12 | 2.13 | 498 |
| 2024-09-20 22:21:38.850 | MS1 | 121.4656686396 | 31.1446288263 | 132 | 504990 | -92.94 | 8.79 | 94.58 | 0.18 | 2.10 | 359 |
| 2024-09-20 22:21:39.111 | MS1 | 121.4656738356 | 31.1446247366 | 132 | 504990 | -91.69 | 7.10 | 80.84 | 0.03 | 2.88 | 403 |
| 2024-09-20 22:21:40.744 | MS1 | 121.4656649808 | 31.1446217670 | 132 | 504990 | -91.29 | 11.45 | 553.38 | 0.12 | 2.75 | 1566 |
| 2024-09-20 22:21:41.949 | MS1 | 121.4656719504 | 31.1446181336 | 132 | 504990 | -92.43 | 10.58 | 392.17 | 0.04 | 2.76 | 1579 |
| 2024-09-20 22:21:42.756 | MS1 | 121.4656771494 | 31.1446361569 | 132 | 504990 | -89.35 | 9.73 | 570.05 | 0.03 | 2.15 | 1591 |

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
| 3217997 | 2 | 121.4698074059 | 31.1539033160 | 172 | 3 | 11 | 40.6 | TDD | 132 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3220514 | 3 | 121.4716986199 | 31.1458752515 | 44 | 6 | 6 | 18.1 | TDD | 53 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3232403 | 4 | 121.4719847436 | 31.1452455723 | 253 | 8 | 1 | 36.7 | TDD | 983 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3239067 | 1 | 121.4751433115 | 31.1538817905 | 259 | 1 | 4 | 19.2 | TDD | 474 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.012 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.032 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.168 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.168 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.855 | NREventA3 | measId:2;ServCellPCI:668;Se... |
| 2024-09-20 22:21:38.095 | NRHandoverAttempt | SourcePCI:668;SourceNR-ARFC... |
| 2024-09-20 22:21:38.144 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.156 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.263 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.263 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239067 | 1 | 6.8947 | 9.4761 | -114.5261 | 19.1973 | 82.1499 | 0.0152 | 0.0014 |
| 2024_09_20 22:00 | 3217997 | 2 | 5.0023 | 5.6755 | -117.2453 | 8.2974 | 92.1237 | 0.0019 | 0.0001 |
| 2024_09_20 22:00 | 3220514 | 3 | 11.1106 | 14.9214 | -114.4160 | 19.7417 | 88.0517 | 0.0061 | 0.0031 |
| 2024_09_20 22:00 | 3232403 | 4 | 9.8082 | 10.6157 | -115.0929 | 8.8560 | 107.8364 | 0.0144 | 0.0071 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413721_8A829274 | 504990 | 132 | -88.1 | 504990 | 983 | -91.3 | 504990 | 474 | -99.3 | 504990 | 53 |
| MR_1774413721_DF23092B | 504990 | 132 | -86.7 | 504990 | 983 | -92.7 | 504990 | 474 | -102.2 | 504990 | 53 |
| MR_1774413721_E64ECF4C | 504990 | 132 | -87.2 | 504990 | 983 | -91.7 | 504990 | 474 | -99.7 | 504990 | 53 |
| MR_1774413721_1ACA9665 | 504990 | 132 | -87.9 | 504990 | 983 | -93.6 | 504990 | 474 | -98.8 | 504990 | 53 |
| MR_1774413721_7E542722 | 504990 | 132 | -86.9 | 504990 | 983 | -91.9 | 504990 | 474 | -101.9 | 504990 | 53 |
| MR_1774413721_AB830BAF | 504990 | 132 | -87.8 | 504990 | 983 | -91.3 | 504990 | 474 | -99.2 | 504990 | 53 |
| MR_1774413721_11DE793E | 504990 | 132 | -87.5 | 504990 | 983 | -93.2 | 504990 | 474 | -98.9 | 504990 | 53 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1908: `7690d837-028...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7690d837-0283-4bd7-9983-1488a8c2af5a` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1908] topology](images/train_1908.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3233831_2 by 3 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263889_4
- `C3`: Increase A3 Offset threshold for 3233831_2
- `C4`: Adjust the azimuth of 3263889_4 by 50 degrees
- `C5`: Add neighbor relationship between 3233417_3 and 3263889_4
- `C6`: Press down the tilt angle of 3233831_2 by 3 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Lift the tilt angle  of 3263889_4 by 10 degrees
- `C9`: Decrease A3 Offset threshold for 3263889_4
- `C10`: Check test server and transmission issues **← 정답**
- `C11`: Decrease A3 Offset threshold for 3233831_2
- `C12`: Decrease transmission power for 3233831_2
- `C13`: Add neighbor relationship between 3233831_2 and 3263889_4
- `C14`: Decrease transmission power for 3263889_4
- `C15`: Increase transmission power for 3233831_2
- `C16`: Increase A3 Offset threshold for 3263889_4
- `C17`: Increase transmission power for 3263889_4
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263889_4
- `C19`: Adjust the azimuth of 3233831_2 by 50 degrees
- `C20`: Press down the tilt angle  of 3263889_4 by 10 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233831_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233831_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.641 | MS1 | 121.4656627227 | 31.1446254701 | 185 | 504990 | -86.83 | 15.00 | 402.51 | 0.01 | 2.28 | 1560 |
| 2024-09-20 22:21:32.303 | MS1 | 121.4656676632 | 31.1446198550 | 185 | 504990 | -88.24 | 15.18 | 437.89 | 0.16 | 2.94 | 1564 |
| 2024-09-20 22:21:33.305 | MS1 | 121.4656694320 | 31.1446208209 | 185 | 504990 | -90.61 | 15.24 | 389.27 | 0.16 | 2.37 | 1582 |
| 2024-09-20 22:21:34.176 | MS1 | 121.4656614810 | 31.1446327277 | 185 | 504990 | -86.48 | 13.45 | 62.79 | 0.09 | 2.54 | 304 |
| 2024-09-20 22:21:35.340 | MS1 | 121.4656652141 | 31.1446214857 | 185 | 504990 | -85.10 | 14.57 | 64.93 | 0.18 | 2.82 | 499 |
| 2024-09-20 22:21:36.333 | MS1 | 121.4656765157 | 31.1446355977 | 185 | 504990 | -89.85 | 15.60 | 57.32 | 0.16 | 2.04 | 441 |
| 2024-09-20 22:21:37.198 | MS1 | 121.4656649700 | 31.1446238634 | 185 | 504990 | -93.67 | 7.37 | 71.75 | 0.04 | 2.60 | 445 |
| 2024-09-20 22:21:38.679 | MS1 | 121.4656654620 | 31.1446271184 | 185 | 504990 | -89.00 | 12.57 | 76.47 | 0.12 | 2.04 | 467 |
| 2024-09-20 22:21:39.628 | MS1 | 121.4656678572 | 31.1446357063 | 185 | 504990 | -90.24 | 10.01 | 47.56 | 0.13 | 2.29 | 439 |
| 2024-09-20 22:21:40.137 | MS1 | 121.4656709981 | 31.1446209211 | 185 | 504990 | -92.27 | 7.95 | 325.01 | 0.03 | 2.34 | 1587 |
| 2024-09-20 22:21:41.988 | MS1 | 121.4656650905 | 31.1446192779 | 185 | 504990 | -89.62 | 10.55 | 346.67 | 0.12 | 2.42 | 1594 |
| 2024-09-20 22:21:42.594 | MS1 | 121.4656637487 | 31.1446324187 | 185 | 504990 | -93.82 | 10.06 | 577.15 | 0.16 | 2.71 | 1585 |

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
| 3233417 | 3 | 121.4724071366 | 31.1500510684 | 69 | 10 | 4 | 30.9 | TDD | 571 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3233831 | 2 | 121.4734324720 | 31.1506822866 | 88 | 1 | 2 | 41.7 | TDD | 185 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3244330 | 1 | 121.4657014828 | 31.1507535948 | 101 | 7 | 11 | 18.8 | TDD | 368 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3263889 | 4 | 121.4663593865 | 31.1494180106 | 303 | 14 | 0 | 22.3 | TDD | 134 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.823 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.842 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.982 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.982 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.716 | NREventA3 | measId:2;ServCellPCI:790;Se... |
| 2024-09-20 22:21:37.956 | NRHandoverAttempt | SourcePCI:790;SourceNR-ARFC... |
| 2024-09-20 22:21:37.989 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.999 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.144 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.144 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244330 | 1 | 5.5634 | 13.2102 | -116.0183 | 19.9646 | 126.8358 | 0.0082 | 0.0098 |
| 2024_09_20 22:00 | 3233831 | 2 | 18.1165 | 7.7397 | -114.7361 | 7.8019 | 112.3633 | 0.0100 | 0.0035 |
| 2024_09_20 22:00 | 3233417 | 3 | 11.9694 | 9.0707 | -114.3381 | 7.2575 | 122.5274 | 0.0120 | 0.0188 |
| 2024_09_20 22:00 | 3263889 | 4 | 10.1387 | 18.2682 | -115.5477 | 10.1029 | 126.5403 | 0.0026 | 0.0003 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415150_1539F1AC | 504990 | 185 | -87.6 | 504990 | 134 | -87.2 | 504990 | 571 | -95.5 | 504990 | 368 |
| MR_1774415150_EB96203C | 504990 | 185 | -88.4 | 504990 | 134 | -86.5 | 504990 | 571 | -96.9 | 504990 | 368 |
| MR_1774415150_48E2CCC4 | 504990 | 185 | -88.0 | 504990 | 134 | -88.1 | 504990 | 571 | -93.7 | 504990 | 368 |
| MR_1774415150_C959D17D | 504990 | 185 | -86.5 | 504990 | 134 | -86.7 | 504990 | 571 | -95.4 | 504990 | 368 |
| MR_1774415150_0D906747 | 504990 | 185 | -87.8 | 504990 | 134 | -84.9 | 504990 | 571 | -92.9 | 504990 | 368 |
| MR_1774415150_33CB8AB0 | 504990 | 185 | -88.2 | 504990 | 134 | -87.7 | 504990 | 571 | -93.8 | 504990 | 368 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1909: `d9d89d76-070...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d9d89d76-070f-4072-a5ed-062cbd569ce9` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260382_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1909] topology](images/train_1909.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3218245_2 by 46 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Lift the tilt angle of 3260382_1 by 4 degrees
- `C4`: Decrease A3 Offset threshold for 3260382_1
- `C5`: Increase A3 Offset threshold for 3218245_2
- `C6`: Increase transmission power for 3218245_2
- `C7`: Press down the tilt angle  of 3218245_2 by 2 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218245_2
- `C9`: Add neighbor relationship between 3211186_7 and 3218245_2
- `C10`: Increase A3 Offset threshold for 3260382_1
- `C11`: Adjust the azimuth of 3260382_1 by 47 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260382_1 **← 정답**
- `C13`: Check test server and transmission issues
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218245_2
- `C15`: Press down the tilt angle of 3260382_1 by 4 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260382_1
- `C17`: Decrease transmission power for 3218245_2
- `C18`: Decrease A3 Offset threshold for 3218245_2
- `C19`: Lift the tilt angle  of 3218245_2 by 2 degrees
- `C20`: Decrease transmission power for 3260382_1
- `C21`: Increase transmission power for 3260382_1
- `C22`: Add neighbor relationship between 3260382_1 and 3218245_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.782 | MS1 | 121.4656771544 | 31.1446275870 | 130 | 504990 | -94.47 | 14.19 | 396.93 | 0.19 | 2.38 | 1582 |
| 2024-09-20 22:21:32.133 | MS1 | 121.4656593508 | 31.1446209377 | 954 | 504990 | -94.62 | 9.13 | 369.09 | 0.06 | 2.69 | 1575 |
| 2024-09-20 22:21:33.800 | MS1 | 121.4656730627 | 31.1446236455 | 433 | 504990 | -94.96 | 9.51 | 562.03 | 0.18 | 2.18 | 1599 |
| 2024-09-20 22:21:34.142 | MS1 | 121.4656764839 | 31.1446223543 | 62 | 152650 | -95.87 | 3.28 | 62.30 | 0.04 | 1.88 | 980 |
| 2024-09-20 22:21:35.283 | MS1 | 121.4656626455 | 31.1446288214 | 851 | 152650 | -93.35 | 2.89 | 65.56 | 0.09 | 1.71 | 933 |
| 2024-09-20 22:21:36.656 | MS1 | 121.4656695261 | 31.1446259626 | 736 | 152650 | -96.85 | 2.16 | 85.13 | 0.15 | 1.74 | 939 |
| 2024-09-20 22:21:37.846 | MS1 | 121.4656742991 | 31.1446281037 | 758 | 152650 | -90.22 | 3.55 | 65.31 | 0.13 | 1.94 | 938 |
| 2024-09-20 22:21:38.566 | MS1 | 121.4656654228 | 31.1446229816 | 62 | 152650 | -90.22 | 4.07 | 67.70 | 0.08 | 1.77 | 928 |
| 2024-09-20 22:21:39.314 | MS1 | 121.4656717002 | 31.1446240490 | 851 | 152650 | -92.04 | 6.48 | 68.14 | 0.06 | 1.98 | 907 |
| 2024-09-20 22:21:40.280 | MS1 | 121.4656761087 | 31.1446258370 | 736 | 152650 | -89.51 | 2.55 | 64.98 | 0.09 | 2.14 | 1568 |
| 2024-09-20 22:21:41.105 | MS1 | 121.4656771605 | 31.1446208422 | 758 | 152650 | -96.60 | 2.62 | 79.97 | 0.00 | 2.01 | 1560 |
| 2024-09-20 22:21:42.891 | MS1 | 121.4656666976 | 31.1446227615 | 62 | 152650 | -95.23 | 5.47 | 67.42 | 0.08 | 2.49 | 1585 |

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
| 3211186 | 7 | 121.4711257227 | 31.1533912974 | 35 | 2 | 12 | 26.6 | FDD | 736 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3218245 | 2 | 121.4733404742 | 31.1493440189 | 188 | 2 | 10 | 3.5 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3220029 | 6 | 121.4708841821 | 31.1477395243 | 212 | 0 | 9 | 16.0 | TDD | 158 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3220916 | 9 | 121.4698687275 | 31.1460236138 | 353 | 7 | 4 | 18.2 | FDD | 851 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3228404 | 3 | 121.4702644374 | 31.1508677203 | 14 | 8 | 11 | 0.4 | TDD | 744 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3240389 | 4 | 121.4666383682 | 31.1492574256 | 55 | 2 | 0 | 19.0 | TDD | 433 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3254304 | 11 | 121.4645394966 | 31.1488971874 | 30 | 13 | 5 | 15.9 | FDD | 184 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3254808 | 10 | 121.4741605802 | 31.1486607248 | 163 | 5 | 12 | 17.3 | FDD | 758 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3260382 | 1 | 121.4688764597 | 31.1445209979 | 225 | 4 | 11 | 2.4 | TDD | 130 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3262227 | 8 | 121.4670571345 | 31.1459926152 | 106 | 6 | 2 | 25.2 | FDD | 777 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3271930 | 12 | 121.4749642974 | 31.1469683582 | 230 | 2 | 2 | 12.3 | FDD | 219 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3272960 | 13 | 121.4737847020 | 31.1487684742 | 43 | 7 | 4 | 10.8 | FDD | 62 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3277461 | 5 | 121.4671807681 | 31.1501483582 | 137 | 3 | 9 | 29.5 | TDD | 954 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.302 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.327 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.435 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.435 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.127 | NREventA2 | measId:1;ServCellPCI:206;Se... |
| 2024-09-20 22:21:35.263 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.536 | NREventA5 | measId:3;ServCellPCI:206;Se... |
| 2024-09-20 22:21:35.574 | NRHandoverAttempt | SourcePCI:206;SourceNR-ARFC... |
| 2024-09-20 22:21:35.618 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.632 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.766 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.766 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260382 | 1 | 5.9313 | 8.7022 | -114.7270 | 12.5803 | 81.5819 | 0.0147 | 0.0142 |
| 2024_09_20 22:00 | 3218245 | 2 | 12.5743 | 17.4035 | -114.1197 | 5.6976 | 91.7687 | 0.0056 | 0.0025 |
| 2024_09_20 22:00 | 3228404 | 3 | 11.4585 | 15.3455 | -115.9336 | 15.3188 | 97.6643 | 0.0043 | 0.0051 |
| 2024_09_20 22:00 | 3240389 | 4 | 9.4612 | 5.2887 | -115.3892 | 7.1405 | 189.9582 | 0.0179 | 0.0129 |
| 2024_09_20 22:00 | 3277461 | 5 | 8.7058 | 14.6042 | -114.9500 | 8.4887 | 88.0731 | 0.0119 | 0.0002 |
| 2024_09_20 22:00 | 3220029 | 6 | 19.1291 | 14.8635 | -114.0059 | 14.3024 | 99.2441 | 0.0132 | 0.0036 |
| 2024_09_20 22:00 | 3211186 | 7 | 16.3145 | 19.9455 | -115.1455 | 3.7517 | 36.4950 | 0.0109 | 0.0071 |
| 2024_09_20 22:00 | 3262227 | 8 | 12.8999 | 16.8218 | -115.9216 | 4.9702 | 33.1877 | 0.0161 | 0.0154 |
| 2024_09_20 22:00 | 3220916 | 9 | 12.1882 | 7.0594 | -114.7960 | 3.2198 | 52.0784 | 0.0186 | 0.0045 |
| 2024_09_20 22:00 | 3254808 | 10 | 16.7939 | 5.5697 | -114.0953 | 3.4274 | 44.8572 | 0.0125 | 0.0094 |
| 2024_09_20 22:00 | 3254304 | 11 | 18.8230 | 12.8748 | -115.9769 | 4.5456 | 28.8648 | 0.0169 | 0.0015 |
| 2024_09_20 22:00 | 3271930 | 12 | 9.3962 | 17.1569 | -116.5466 | 3.9084 | 37.8720 | 0.0177 | 0.0074 |
| 2024_09_20 22:00 | 3272960 | 13 | 7.0364 | 14.2474 | -115.9859 | 4.2581 | 22.8329 | 0.0143 | 0.0100 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412706_9220E15E | 152650 | 62 | -96.5 | 152650 | 184 | -100.4 | 152650 | 219 | -102.3 | 152650 | 777 |
| MR_1774412706_2C778BDD | 152650 | 62 | -96.6 | 152650 | 184 | -99.6 | 152650 | 219 | -105.5 | 152650 | 777 |
| MR_1774412706_4CC9616A | 152650 | 62 | -97.7 | 152650 | 184 | -102.0 | 152650 | 219 | -105.7 | 152650 | 777 |
| MR_1774412706_17E5B8A0 | 152650 | 62 | -94.8 | 152650 | 184 | -99.5 | 152650 | 219 | -104.1 | 152650 | 777 |
| MR_1774412706_08315C27 | 504990 | 433 | -96.5 | 504990 | 382 | -96.2 | 504990 | 158 | -93.1 | 504990 | 744 |
| MR_1774412706_0ABEE445 | 504990 | 433 | -95.9 | 504990 | 382 | -92.5 | 504990 | 158 | -92.8 | 504990 | 744 |
| MR_1774412706_96DF38E0 | 504990 | 433 | -96.7 | 504990 | 382 | -94.0 | 504990 | 158 | -95.1 | 504990 | 744 |
| MR_1774412706_864209E7 | 152650 | 62 | -95.8 | 152650 | 184 | -99.7 | 152650 | 219 | -104.8 | 152650 | 777 |

> *... 2개 열 생략 (전체 14열)*

---
