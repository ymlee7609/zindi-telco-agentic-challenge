# Track A 문제 분석 — train[800]~train[809]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[800] ~ train[809] (10개)

## 목차

1. [문제 800: `82121d7c-018...`](#800) — single-answer, 정답: C18
2. [문제 801: `aa3b6baa-ccf...`](#801) — single-answer, 정답: C21
3. [문제 802: `1e971c2d-4b5...`](#802) — single-answer, 정답: C21
4. [문제 803: `43c8c63b-3b0...`](#803) — single-answer, 정답: C7
5. [문제 804: `3170d47f-7e7...`](#804) — multiple-answer, 정답: C5|C7
6. [문제 805: `886c8ccd-5e8...`](#805) — single-answer, 정답: C20
7. [문제 806: `dad41dd7-dda...`](#806) — single-answer, 정답: C12
8. [문제 807: `9eb137e0-97e...`](#807) — multiple-answer, 정답: C8|C13
9. [문제 808: `5e14ff8b-af8...`](#808) — single-answer, 정답: C5
10. [문제 809: `7935ca0b-d37...`](#809) — single-answer, 정답: C17

---

### 문제 800: `82121d7c-018...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `82121d7c-0186-4988-81c5-022e98d314b9` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[800] topology](images/train_0800.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3266176_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266176_1
- `C3`: Press down the tilt angle of 3266176_1 by 10 degrees
- `C4`: Decrease A3 Offset threshold for 3253390_2
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase A3 Offset threshold for 3266176_1
- `C7`: Decrease transmission power for 3253390_2
- `C8`: Lift the tilt angle  of 3253390_2 by 10 degrees
- `C9`: Press down the tilt angle  of 3253390_2 by 10 degrees
- `C10`: Add neighbor relationship between 3237689_4 and 3253390_2
- `C11`: Decrease transmission power for 3266176_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266176_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253390_2
- `C14`: Adjust the azimuth of 3253390_2 by 50 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253390_2
- `C16`: Increase transmission power for 3266176_1
- `C17`: Add neighbor relationship between 3266176_1 and 3253390_2
- `C18`: Check test server and transmission issues **← 정답**
- `C19`: Increase A3 Offset threshold for 3253390_2
- `C20`: Adjust the azimuth of 3266176_1 by 50 degrees
- `C21`: Lift the tilt angle of 3266176_1 by 10 degrees
- `C22`: Increase transmission power for 3253390_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.360 | MS1 | 121.4656637573 | 31.1446310990 | 520 | 504990 | -85.78 | 14.54 | 536.95 | 0.16 | 2.39 | 1581 |
| 2024-09-20 22:21:32.977 | MS1 | 121.4656741310 | 31.1446244691 | 520 | 504990 | -88.19 | 15.28 | 365.08 | 0.18 | 2.74 | 1583 |
| 2024-09-20 22:21:33.250 | MS1 | 121.4656670572 | 31.1446289769 | 520 | 504990 | -89.33 | 14.54 | 440.26 | 0.03 | 2.10 | 1566 |
| 2024-09-20 22:21:34.292 | MS1 | 121.4656759007 | 31.1446306068 | 520 | 504990 | -85.77 | 14.96 | 59.84 | 0.00 | 2.12 | 486 |
| 2024-09-20 22:21:35.772 | MS1 | 121.4656617696 | 31.1446299048 | 520 | 504990 | -91.89 | 13.59 | 75.38 | 0.13 | 2.48 | 465 |
| 2024-09-20 22:21:36.759 | MS1 | 121.4656720617 | 31.1446363073 | 520 | 504990 | -88.17 | 14.14 | 76.67 | 0.19 | 2.82 | 492 |
| 2024-09-20 22:21:37.478 | MS1 | 121.4656767326 | 31.1446294192 | 520 | 504990 | -90.08 | 12.28 | 87.81 | 0.11 | 2.46 | 402 |
| 2024-09-20 22:21:38.321 | MS1 | 121.4656699051 | 31.1446351575 | 520 | 504990 | -92.04 | 7.62 | 76.68 | 0.10 | 2.80 | 410 |
| 2024-09-20 22:21:39.384 | MS1 | 121.4656617291 | 31.1446284354 | 520 | 504990 | -89.47 | 9.30 | 70.91 | 0.07 | 2.30 | 475 |
| 2024-09-20 22:21:40.774 | MS1 | 121.4656738911 | 31.1446373258 | 520 | 504990 | -92.53 | 10.50 | 311.66 | 0.08 | 2.88 | 1568 |
| 2024-09-20 22:21:41.587 | MS1 | 121.4656706214 | 31.1446359951 | 520 | 504990 | -90.00 | 12.13 | 518.80 | 0.09 | 2.03 | 1591 |
| 2024-09-20 22:21:42.195 | MS1 | 121.4656647187 | 31.1446357398 | 520 | 504990 | -91.68 | 10.66 | 429.24 | 0.19 | 2.61 | 1576 |

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
| 3237689 | 4 | 121.4747998147 | 31.1538525709 | 61 | 0 | 9 | 27.5 | TDD | 455 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3247014 | 3 | 121.4678936135 | 31.1521970302 | 276 | 2 | 8 | 30.8 | TDD | 366 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3253390 | 2 | 121.4717722849 | 31.1498007529 | 59 | 9 | 8 | 18.9 | TDD | 96 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3266176 | 1 | 121.4744956536 | 31.1483336927 | 140 | 13 | 4 | 44.2 | TDD | 520 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.349 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.366 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.499 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.499 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.172 | NREventA3 | measId:2;ServCellPCI:424;Se... |
| 2024-09-20 22:21:38.412 | NRHandoverAttempt | SourcePCI:424;SourceNR-ARFC... |
| 2024-09-20 22:21:38.455 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.468 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.607 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.607 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266176 | 1 | 6.3074 | 18.6343 | -114.3004 | 15.4775 | 103.6394 | 0.0013 | 0.0129 |
| 2024_09_20 22:00 | 3253390 | 2 | 6.3741 | 6.4909 | -117.3530 | 17.6759 | 147.9367 | 0.0031 | 0.0083 |
| 2024_09_20 22:00 | 3247014 | 3 | 10.1521 | 13.2631 | -117.0190 | 16.3129 | 163.1474 | 0.0012 | 0.0016 |
| 2024_09_20 22:00 | 3237689 | 4 | 11.0621 | 10.6633 | -116.6760 | 18.1088 | 136.8386 | 0.0108 | 0.0104 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415528_4E2D2EBB | 504990 | 520 | -84.6 | 504990 | 96 | -90.2 | 504990 | 455 | -90.2 | 504990 | 366 |
| MR_1774415528_B713290B | 504990 | 520 | -85.2 | 504990 | 96 | -90.8 | 504990 | 455 | -92.8 | 504990 | 366 |
| MR_1774415528_3C205C84 | 504990 | 520 | -86.2 | 504990 | 96 | -87.8 | 504990 | 455 | -93.3 | 504990 | 366 |
| MR_1774415528_9B0BC2A5 | 504990 | 520 | -85.9 | 504990 | 96 | -88.2 | 504990 | 455 | -91.1 | 504990 | 366 |
| MR_1774415528_E5463A7E | 504990 | 520 | -87.1 | 504990 | 96 | -90.3 | 504990 | 455 | -91.2 | 504990 | 366 |
| MR_1774415528_767EBDAC | 504990 | 520 | -86.8 | 504990 | 96 | -89.8 | 504990 | 455 | -90.4 | 504990 | 366 |
| MR_1774415528_83B2EEA1 | 504990 | 520 | -85.6 | 504990 | 96 | -88.0 | 504990 | 455 | -91.7 | 504990 | 366 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 801: `aa3b6baa-ccf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `aa3b6baa-ccf6-4243-a77c-df41d61139c4` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[801] topology](images/train_0801.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3241310_4 and 3273426_2
- `C2`: Increase transmission power for 3256408_1
- `C3`: Lift the tilt angle  of 3273426_2 by 10 degrees
- `C4`: Add neighbor relationship between 3256408_1 and 3273426_2
- `C5`: Adjust the azimuth of 3273426_2 by 50 degrees
- `C6`: Decrease transmission power for 3273426_2
- `C7`: Decrease A3 Offset threshold for 3273426_2
- `C8`: Lift the tilt angle of 3256408_1 by 10 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256408_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256408_1
- `C11`: Increase A3 Offset threshold for 3273426_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Increase A3 Offset threshold for 3256408_1
- `C14`: Press down the tilt angle  of 3273426_2 by 10 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273426_2
- `C16`: Decrease A3 Offset threshold for 3256408_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273426_2
- `C18`: Adjust the azimuth of 3256408_1 by 44 degrees
- `C19`: Press down the tilt angle of 3256408_1 by 10 degrees
- `C20`: Increase transmission power for 3273426_2
- `C21`: Check test server and transmission issues **← 정답**
- `C22`: Decrease transmission power for 3256408_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.326 | MS1 | 121.4656616479 | 31.1446229100 | 400 | 504990 | -87.59 | 12.66 | 597.36 | 0.19 | 2.28 | 1594 |
| 2024-09-20 22:21:32.487 | MS1 | 121.4656769932 | 31.1446262781 | 400 | 504990 | -86.44 | 17.01 | 425.71 | 0.05 | 2.75 | 1595 |
| 2024-09-20 22:21:33.939 | MS1 | 121.4656684469 | 31.1446288889 | 400 | 504990 | -86.50 | 12.34 | 455.69 | 0.19 | 2.66 | 1593 |
| 2024-09-20 22:21:34.383 | MS1 | 121.4656584962 | 31.1446256108 | 400 | 504990 | -90.20 | 13.04 | 62.61 | 0.12 | 2.76 | 370 |
| 2024-09-20 22:21:35.838 | MS1 | 121.4656757122 | 31.1446217746 | 400 | 504990 | -90.04 | 17.33 | 50.40 | 0.14 | 2.67 | 409 |
| 2024-09-20 22:21:36.991 | MS1 | 121.4656623278 | 31.1446348436 | 400 | 504990 | -91.69 | 13.51 | 85.38 | 0.18 | 2.47 | 334 |
| 2024-09-20 22:21:37.660 | MS1 | 121.4656702559 | 31.1446234116 | 400 | 504990 | -89.94 | 7.40 | 93.17 | 0.02 | 2.21 | 490 |
| 2024-09-20 22:21:38.675 | MS1 | 121.4656738689 | 31.1446244944 | 400 | 504990 | -90.93 | 8.17 | 96.51 | 0.11 | 2.33 | 405 |
| 2024-09-20 22:21:39.224 | MS1 | 121.4656690524 | 31.1446320342 | 400 | 504990 | -91.77 | 8.32 | 63.09 | 0.11 | 2.17 | 339 |
| 2024-09-20 22:21:40.441 | MS1 | 121.4656617759 | 31.1446374125 | 400 | 504990 | -90.55 | 10.65 | 575.01 | 0.13 | 2.70 | 1561 |
| 2024-09-20 22:21:41.881 | MS1 | 121.4656691202 | 31.1446329199 | 400 | 504990 | -91.42 | 9.23 | 372.43 | 0.11 | 2.72 | 1587 |
| 2024-09-20 22:21:42.717 | MS1 | 121.4656680934 | 31.1446222694 | 400 | 504990 | -94.00 | 10.22 | 528.36 | 0.12 | 2.38 | 1574 |

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
| 3230852 | 3 | 121.4663646045 | 31.1521871796 | 261 | 0 | 6 | 49.6 | TDD | 550 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3241310 | 4 | 121.4727244393 | 31.1533956438 | 228 | 2 | 8 | 31.9 | TDD | 575 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3256408 | 1 | 121.4726555230 | 31.1458506564 | 302 | 9 | 8 | 21.7 | TDD | 400 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3273426 | 2 | 121.4667376690 | 31.1473127856 | 125 | 12 | 10 | 22.3 | TDD | 188 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.014 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.031 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.164 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.164 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.908 | NREventA3 | measId:2;ServCellPCI:26;Ser... |
| 2024-09-20 22:21:38.148 | NRHandoverAttempt | SourcePCI:26;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.191 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.202 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.343 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.343 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256408 | 1 | 14.5659 | 12.5928 | -114.4434 | 16.2135 | 112.3161 | 0.0024 | 0.0023 |
| 2024_09_20 22:00 | 3273426 | 2 | 9.4830 | 11.7065 | -115.9228 | 7.1201 | 196.7910 | 0.0108 | 0.0080 |
| 2024_09_20 22:00 | 3230852 | 3 | 7.5283 | 16.4941 | -114.6032 | 5.5610 | 185.9049 | 0.0037 | 0.0067 |
| 2024_09_20 22:00 | 3241310 | 4 | 7.0703 | 14.0064 | -117.0863 | 18.2966 | 176.9079 | 0.0167 | 0.0048 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416836_F8A3375A | 504990 | 400 | -90.8 | 504990 | 188 | -94.5 | 504990 | 575 | -103.9 | 504990 | 550 |
| MR_1774416836_82223C1B | 504990 | 400 | -89.7 | 504990 | 188 | -95.4 | 504990 | 575 | -102.6 | 504990 | 550 |
| MR_1774416836_27E5884A | 504990 | 400 | -90.8 | 504990 | 188 | -95.7 | 504990 | 575 | -102.3 | 504990 | 550 |
| MR_1774416836_464AA3C7 | 504990 | 400 | -92.0 | 504990 | 188 | -93.7 | 504990 | 575 | -105.1 | 504990 | 550 |
| MR_1774416836_F406B4E3 | 504990 | 400 | -89.3 | 504990 | 188 | -93.6 | 504990 | 575 | -105.0 | 504990 | 550 |
| MR_1774416836_7EFA67A7 | 504990 | 400 | -91.2 | 504990 | 188 | -93.5 | 504990 | 575 | -105.4 | 504990 | 550 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 802: `1e971c2d-4b5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1e971c2d-4b5f-47de-ba45-a3d726148976` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3275498_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[802] topology](images/train_0802.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3252331_3 and 3222866_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275498_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222866_2
- `C4`: Press down the tilt angle of 3275498_1 by 5 degrees
- `C5`: Add neighbor relationship between 3275498_1 and 3222866_2
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Lift the tilt angle  of 3222866_2 by 5 degrees
- `C8`: Increase A3 Offset threshold for 3275498_1
- `C9`: Decrease transmission power for 3275498_1
- `C10`: Increase transmission power for 3275498_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222866_2
- `C12`: Press down the tilt angle  of 3222866_2 by 5 degrees
- `C13`: Decrease transmission power for 3222866_2
- `C14`: Increase transmission power for 3222866_2
- `C15`: Increase A3 Offset threshold for 3222866_2
- `C16`: Check test server and transmission issues
- `C17`: Adjust the azimuth of 3275498_1 by 40 degrees
- `C18`: Adjust the azimuth of 3222866_2 by 50 degrees
- `C19`: Decrease A3 Offset threshold for 3275498_1
- `C20`: Lift the tilt angle of 3275498_1 by 5 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275498_1 **← 정답**
- `C22`: Decrease A3 Offset threshold for 3222866_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.812 | MS1 | 121.4656763771 | 31.1446299794 | 696 | 504990 | -91.69 | 13.46 | 445.82 | 0.19 | 2.81 | 1597 |
| 2024-09-20 22:21:32.636 | MS1 | 121.4656735258 | 31.1446285201 | 696 | 504990 | -85.90 | 13.73 | 310.69 | 0.10 | 2.34 | 1587 |
| 2024-09-20 22:21:33.604 | MS1 | 121.4656614073 | 31.1446341912 | 696 | 504990 | -89.32 | 15.51 | 473.03 | 0.13 | 2.43 | 1599 |
| 2024-09-20 22:21:34.240 | MS1 | 121.4656701956 | 31.1446240517 | 696 | 504990 | -86.76 | 12.30 | 64.13 | 0.68 | 2.10 | 671 |
| 2024-09-20 22:21:35.638 | MS1 | 121.4656668941 | 31.1446211696 | 696 | 504990 | -91.02 | 15.52 | 81.45 | 0.65 | 2.02 | 625 |
| 2024-09-20 22:21:36.199 | MS1 | 121.4656642931 | 31.1446378947 | 696 | 504990 | -87.13 | 16.74 | 72.66 | 0.56 | 2.84 | 628 |
| 2024-09-20 22:21:37.867 | MS1 | 121.4656716963 | 31.1446210847 | 696 | 504990 | -90.81 | 9.28 | 46.54 | 0.57 | 2.49 | 569 |
| 2024-09-20 22:21:38.359 | MS1 | 121.4656595183 | 31.1446339805 | 696 | 504990 | -92.38 | 12.67 | 96.59 | 0.62 | 2.87 | 549 |
| 2024-09-20 22:21:39.341 | MS1 | 121.4656608290 | 31.1446362173 | 696 | 504990 | -92.38 | 11.90 | 56.49 | 0.68 | 2.73 | 628 |
| 2024-09-20 22:21:40.863 | MS1 | 121.4656742172 | 31.1446299179 | 696 | 504990 | -93.19 | 12.71 | 544.49 | 0.19 | 2.99 | 1561 |
| 2024-09-20 22:21:41.327 | MS1 | 121.4656599304 | 31.1446349500 | 696 | 504990 | -93.64 | 11.37 | 453.90 | 0.03 | 2.01 | 1585 |
| 2024-09-20 22:21:42.767 | MS1 | 121.4656716257 | 31.1446362755 | 696 | 504990 | -89.72 | 10.63 | 361.57 | 0.19 | 2.16 | 1560 |

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
| 3222866 | 2 | 121.4652669723 | 31.1499086891 | 117 | 2 | 7 | 27.4 | TDD | 345 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3252331 | 3 | 121.4689039595 | 31.1452519690 | 87 | 13 | 12 | 31.0 | TDD | 323 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3268833 | 4 | 121.4656423180 | 31.1472109478 | 106 | 4 | 7 | 49.8 | TDD | 923 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3275498 | 1 | 121.4728304792 | 31.1440348069 | 315 | 1 | 4 | 45.5 | TDD | 696 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.457 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.477 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.596 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.596 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.339 | NREventA3 | measId:2;ServCellPCI:533;Se... |
| 2024-09-20 22:21:38.579 | NRHandoverAttempt | SourcePCI:533;SourceNR-ARFC... |
| 2024-09-20 22:21:38.617 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.631 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.747 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.747 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275498 | 1 | 7.5728 | 12.8787 | -114.0856 | 8.7154 | 158.9619 | 0.0059 | 0.0075 |
| 2024_09_20 22:00 | 3222866 | 2 | 7.3564 | 9.7224 | -115.8791 | 16.7829 | 174.9655 | 0.0191 | 0.0095 |
| 2024_09_20 22:00 | 3252331 | 3 | 18.1491 | 16.0550 | -117.6066 | 5.3041 | 195.8823 | 0.0008 | 0.0043 |
| 2024_09_20 22:00 | 3268833 | 4 | 6.1069 | 19.0740 | -117.4988 | 14.1398 | 184.5325 | 0.0197 | 0.0038 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416085_A77267A9 | 504990 | 696 | -85.6 | 504990 | 345 | -94.6 | 504990 | 323 | -99.8 | 504990 | 923 |
| MR_1774416085_089D8B34 | 504990 | 696 | -86.2 | 504990 | 345 | -93.8 | 504990 | 323 | -99.1 | 504990 | 923 |
| MR_1774416085_7E7C0418 | 504990 | 696 | -85.2 | 504990 | 345 | -92.7 | 504990 | 323 | -100.1 | 504990 | 923 |
| MR_1774416085_571B3CE0 | 504990 | 696 | -85.3 | 504990 | 345 | -93.4 | 504990 | 323 | -98.8 | 504990 | 923 |
| MR_1774416085_55C452C2 | 504990 | 696 | -86.3 | 504990 | 345 | -95.8 | 504990 | 323 | -99.4 | 504990 | 923 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 803: `43c8c63b-3b0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `43c8c63b-3b07-4afe-be76-655c1a72414d` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[803] topology](images/train_0803.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3259870_1
- `C2`: Check test server and transmission issues
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261364_2
- `C4`: Increase A3 Offset threshold for 3261364_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259870_1
- `C6`: Adjust the azimuth of 3261364_2 by 50 degrees
- `C7`: Insufficient data; more data is needed for judgment. **← 정답**
- `C8`: Increase transmission power for 3259870_1
- `C9`: Adjust the azimuth of 3259870_1 by 29 degrees
- `C10`: Lift the tilt angle of 3261364_2 by 10 degrees
- `C11`: Add neighbor relationship between 3261364_2 and 3259870_1
- `C12`: Press down the tilt angle  of 3259870_1 by 10 degrees
- `C13`: Add neighbor relationship between 3244913_4 and 3259870_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259870_1
- `C15`: Increase transmission power for 3261364_2
- `C16`: Increase A3 Offset threshold for 3259870_1
- `C17`: Decrease transmission power for 3261364_2
- `C18`: Lift the tilt angle  of 3259870_1 by 10 degrees
- `C19`: Decrease A3 Offset threshold for 3259870_1
- `C20`: Press down the tilt angle of 3261364_2 by 10 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261364_2
- `C22`: Decrease A3 Offset threshold for 3261364_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.418 | MS1 | 121.4656661454 | 31.1446213456 | 204 | 504990 | -91.67 | 17.74 | 563.81 | 0.15 | 2.63 | 1579 |
| 2024-09-20 22:21:32.260 | MS1 | 121.4656602031 | 31.1446365213 | 204 | 504990 | -88.82 | 14.18 | 468.79 | 0.20 | 2.07 | 1576 |
| 2024-09-20 22:21:33.174 | MS1 | 121.4656670950 | 31.1446342341 | 204 | 504990 | -91.71 | 13.38 | 358.53 | 0.18 | 2.77 | 1588 |
| 2024-09-20 22:21:34.976 | MS1 | 121.4656590772 | 31.1446266668 | 204 | 504990 | -90.96 | 14.13 | 79.68 | 0.12 | 2.09 | 1595 |
| 2024-09-20 22:21:35.828 | MS1 | 121.4656754314 | 31.1446278728 | 204 | 504990 | -90.83 | 12.17 | 61.93 | 0.11 | 2.12 | 1579 |
| 2024-09-20 22:21:36.121 | MS1 | 121.4656729949 | 31.1446215888 | 204 | 504990 | -85.62 | 12.81 | 79.74 | 0.13 | 2.70 | 1595 |
| 2024-09-20 22:21:37.508 | MS1 | 121.4656620394 | 31.1446195117 | 204 | 504990 | -93.52 | 8.94 | 78.77 | 0.19 | 2.36 | 1566 |
| 2024-09-20 22:21:38.415 | MS1 | 121.4656694673 | 31.1446339918 | 204 | 504990 | -92.82 | 8.28 | 88.18 | 0.17 | 2.29 | 1583 |
| 2024-09-20 22:21:39.443 | MS1 | 121.4656608918 | 31.1446251746 | 204 | 504990 | -91.33 | 9.58 | 65.54 | 0.03 | 2.61 | 1587 |
| 2024-09-20 22:21:40.218 | MS1 | 121.4656741632 | 31.1446227155 | 204 | 504990 | -92.91 | 9.42 | 497.71 | 0.12 | 2.93 | 1588 |
| 2024-09-20 22:21:41.164 | MS1 | 121.4656754805 | 31.1446309752 | 204 | 504990 | -91.00 | 10.51 | 342.14 | 0.01 | 2.46 | 1563 |
| 2024-09-20 22:21:42.486 | MS1 | 121.4656750625 | 31.1446368780 | 204 | 504990 | -91.32 | 10.73 | 416.98 | 0.08 | 2.36 | 1582 |

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
| 3218455 | 3 | 121.4660639812 | 31.1469878757 | 130 | 9 | 8 | 20.4 | TDD | 510 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3244913 | 4 | 121.4715184399 | 31.1449417703 | 94 | 6 | 1 | 47.0 | TDD | 95 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3259870 | 1 | 121.4645149533 | 31.1481327526 | 135 | 7 | 1 | 39.4 | TDD | 134 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3261364 | 2 | 121.4649072180 | 31.1501276779 | 25 | 14 | 6 | 28.9 | TDD | 204 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.126 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.150 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.261 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.261 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.023 | NREventA3 | measId:2;ServCellPCI:582;Se... |
| 2024-09-20 22:21:38.263 | NRHandoverAttempt | SourcePCI:582;SourceNR-ARFC... |
| 2024-09-20 22:21:38.298 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.312 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.435 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.435 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3259870 | 1 | 94.3518 | 78.4851 | -117.7543 | 7.8420 | 105.2432 | 0.0169 | 0.0056 |
| 2024_09_19 22:00 | 3261364 | 2 | 88.6935 | 87.3211 | -115.9143 | 10.1852 | 104.8172 | 0.0099 | 0.0018 |
| 2024_09_19 22:00 | 3218455 | 3 | 85.3735 | 85.4768 | -114.2580 | 7.8430 | 105.7245 | 0.0151 | 0.0081 |
| 2024_09_19 22:00 | 3244913 | 4 | 76.5568 | 86.1189 | -116.1817 | 5.3302 | 80.4968 | 0.0004 | 0.0036 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416548_D2DC5E2C | 504990 | 204 | -89.2 | 504990 | 134 | -100.4 | 504990 | 95 | -106.1 | 504990 | 510 |
| MR_1774416548_2C702663 | 504990 | 204 | -89.9 | 504990 | 134 | -99.5 | 504990 | 95 | -106.6 | 504990 | 510 |
| MR_1774416548_D0932B84 | 504990 | 204 | -91.9 | 504990 | 134 | -100.4 | 504990 | 95 | -104.5 | 504990 | 510 |
| MR_1774416548_9C35F5A4 | 504990 | 204 | -90.6 | 504990 | 134 | -99.7 | 504990 | 95 | -105.9 | 504990 | 510 |
| MR_1774416548_74C5A990 | 504990 | 204 | -91.1 | 504990 | 134 | -101.2 | 504990 | 95 | -103.4 | 504990 | 510 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 804: `3170d47f-7e7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3170d47f-7e70-4090-a7e2-a1b1071c934e` |
| Tag | **multiple-answer** |
| 정답 | **C5|C7** |
| C5 의미 | Adjust the azimuth of 3221395_3 by 45 degrees |
| C7 의미 | Increase transmission power for 3221395_3 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[804] topology](images/train_0804.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221250_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221395_3
- `C3`: Decrease A3 Offset threshold for 3221395_3
- `C4`: Lift the tilt angle  of 3221250_4 by 5 degrees
- `C5`: Adjust the azimuth of 3221395_3 by 45 degrees **← 정답**
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221395_3
- `C7`: Increase transmission power for 3221395_3 **← 정답**
- `C8`: Increase transmission power for 3221250_4
- `C9`: Decrease transmission power for 3221395_3
- `C10`: Add neighbor relationship between 3221395_3 and 3221250_4
- `C11`: Press down the tilt angle  of 3221250_4 by 5 degrees
- `C12`: Lift the tilt angle of 3221395_3 by 10 degrees
- `C13`: Adjust the azimuth of 3221250_4 by 19 degrees
- `C14`: Increase A3 Offset threshold for 3221250_4
- `C15`: Increase A3 Offset threshold for 3221395_3
- `C16`: Decrease transmission power for 3221250_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221250_4
- `C18`: Check test server and transmission issues
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease A3 Offset threshold for 3221250_4
- `C21`: Press down the tilt angle of 3221395_3 by 10 degrees
- `C22`: Add neighbor relationship between 3247415_1 and 3221250_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.291 | MS1 | 121.4656755081 | 31.1446182336 | 603 | 504990 | -85.81 | 12.20 | 358.84 | 0.09 | 2.80 | 1598 |
| 2024-09-20 22:21:32.801 | MS1 | 121.4656754507 | 31.1446196099 | 603 | 504990 | -92.42 | 17.35 | 465.47 | 0.08 | 2.54 | 1587 |
| 2024-09-20 22:21:33.325 | MS1 | 121.4656729687 | 31.1446227277 | 603 | 504990 | -90.19 | 12.80 | 479.02 | 0.17 | 2.75 | 1586 |
| 2024-09-20 22:21:34.485 | MS1 | 121.4656708267 | 31.1446333275 | 603 | 504990 | -108.28 | -0.63 | 58.68 | 0.14 | 1.45 | 1583 |
| 2024-09-20 22:21:35.476 | MS1 | 121.4656651090 | 31.1446252658 | 603 | 504990 | -107.18 | 0.59 | 73.32 | 0.08 | 1.38 | 1588 |
| 2024-09-20 22:21:36.754 | MS1 | 121.4656700072 | 31.1446269838 | 603 | 504990 | -104.26 | 0.52 | 62.56 | 0.03 | 1.31 | 1577 |
| 2024-09-20 22:21:37.654 | MS1 | 121.4656762801 | 31.1446316679 | 603 | 504990 | -102.65 | -1.11 | 60.12 | 0.16 | 1.31 | 1583 |
| 2024-09-20 22:21:38.674 | MS1 | 121.4656664449 | 31.1446279312 | 603 | 504990 | -103.94 | 0.12 | 39.21 | 0.08 | 1.21 | 1600 |
| 2024-09-20 22:21:39.444 | MS1 | 121.4656617718 | 31.1446188339 | 603 | 504990 | -102.24 | 1.32 | 53.93 | 0.01 | 1.09 | 1589 |
| 2024-09-20 22:21:40.930 | MS1 | 121.4656591627 | 31.1446231686 | 603 | 504990 | -92.23 | 15.03 | 422.78 | 0.11 | 2.83 | 1568 |
| 2024-09-20 22:21:41.355 | MS1 | 121.4656584788 | 31.1446254609 | 603 | 504990 | -85.87 | 17.17 | 425.73 | 0.08 | 2.75 | 1561 |
| 2024-09-20 22:21:42.954 | MS1 | 121.4656603809 | 31.1446187238 | 603 | 504990 | -89.28 | 17.17 | 489.07 | 0.07 | 2.37 | 1576 |

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
| 3221250 | 4 | 121.4650770443 | 31.1513544032 | 157 | 3 | 10 | 31.5 | TDD | 325 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3221395 | 3 | 121.4703695990 | 31.1465687967 | 289 | 10 | 6 | 48.9 | TDD | 603 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3247415 | 1 | 121.4691861038 | 31.1514832457 | 94 | 0 | 8 | 18.0 | TDD | 504 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3266841 | 2 | 121.4690117387 | 31.1533755213 | 64 | 9 | 5 | 24.6 | TDD | 842 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.898 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.918 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.035 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.035 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.293 | NREventA2 | measId:1;ServCellPCI:657;Se... |
| 2024-09-20 22:21:34.439 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247415 | 1 | 10.1867 | 19.3740 | -117.8093 | 7.6503 | 170.7223 | 0.0046 | 0.0043 |
| 2024_09_20 22:00 | 3266841 | 2 | 6.4106 | 6.4867 | -114.5174 | 5.7607 | 160.5324 | 0.0008 | 0.0166 |
| 2024_09_20 22:00 | 3221395 | 3 | 15.6835 | 10.8787 | -117.0628 | 14.1579 | 170.4214 | 0.1519 | 0.0111 |
| 2024_09_20 22:00 | 3221250 | 4 | 17.5263 | 19.4527 | -114.8153 | 8.3707 | 194.7556 | 0.0154 | 0.0091 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416966_99E37CA1 | 504990 | 603 | -109.0 | 504990 | 325 | -109.9 | 504990 | 504 | -115.0 | 504990 | 842 |
| MR_1774416966_1FCC4F52 | 504990 | 603 | -106.9 | 504990 | 325 | -110.7 | 504990 | 504 | -115.4 | 504990 | 842 |
| MR_1774416966_AD657CB8 | 504990 | 603 | -109.9 | 504990 | 325 | -113.1 | 504990 | 504 | -114.0 | 504990 | 842 |
| MR_1774416966_80523415 | 504990 | 603 | -108.1 | 504990 | 325 | -113.0 | 504990 | 504 | -114.5 | 504990 | 842 |
| MR_1774416966_75DA7FED | 504990 | 603 | -109.7 | 504990 | 325 | -109.5 | 504990 | 504 | -116.2 | 504990 | 842 |
| MR_1774416966_CD403688 | 504990 | 603 | -106.6 | 504990 | 325 | -112.4 | 504990 | 504 | -113.1 | 504990 | 842 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 805: `886c8ccd-5e8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `886c8ccd-5e8b-47b6-b521-2052d681b1ea` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3216376_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[805] topology](images/train_0805.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3216376_3 by 2 degrees
- `C2`: Adjust the azimuth of 3216376_3 by 43 degrees
- `C3`: Lift the tilt angle of 3216376_3 by 2 degrees
- `C4`: Increase transmission power for 3224874_4
- `C5`: Increase transmission power for 3216376_3
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease transmission power for 3224874_4
- `C8`: Lift the tilt angle  of 3224874_4 by 6 degrees
- `C9`: Add neighbor relationship between 3219691_2 and 3224874_4
- `C10`: Adjust the azimuth of 3224874_4 by 50 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224874_4
- `C12`: Add neighbor relationship between 3216376_3 and 3224874_4
- `C13`: Increase A3 Offset threshold for 3224874_4
- `C14`: Decrease A3 Offset threshold for 3216376_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224874_4
- `C16`: Decrease A3 Offset threshold for 3224874_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216376_3
- `C18`: Check test server and transmission issues
- `C19`: Increase A3 Offset threshold for 3216376_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216376_3 **← 정답**
- `C21`: Decrease transmission power for 3216376_3
- `C22`: Press down the tilt angle  of 3224874_4 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.741 | MS1 | 121.4656676660 | 31.1446250504 | 643 | 504990 | -85.09 | 17.06 | 456.50 | 0.01 | 2.62 | 1567 |
| 2024-09-20 22:21:32.830 | MS1 | 121.4656605292 | 31.1446352997 | 643 | 504990 | -87.66 | 17.24 | 513.91 | 0.06 | 2.49 | 1561 |
| 2024-09-20 22:21:33.786 | MS1 | 121.4656694708 | 31.1446300155 | 643 | 504990 | -88.29 | 14.89 | 568.60 | 0.13 | 2.48 | 1588 |
| 2024-09-20 22:21:34.157 | MS1 | 121.4656695257 | 31.1446275538 | 643 | 504990 | -85.21 | 17.35 | 96.82 | 0.61 | 2.93 | 547 |
| 2024-09-20 22:21:35.721 | MS1 | 121.4656734904 | 31.1446362815 | 643 | 504990 | -89.30 | 17.25 | 51.22 | 0.52 | 2.57 | 551 |
| 2024-09-20 22:21:36.129 | MS1 | 121.4656719222 | 31.1446240402 | 643 | 504990 | -89.19 | 15.92 | 60.15 | 0.63 | 2.45 | 629 |
| 2024-09-20 22:21:37.264 | MS1 | 121.4656756087 | 31.1446273032 | 643 | 504990 | -92.57 | 7.50 | 99.66 | 0.70 | 2.40 | 569 |
| 2024-09-20 22:21:38.237 | MS1 | 121.4656692002 | 31.1446280556 | 643 | 504990 | -90.14 | 12.28 | 51.48 | 0.70 | 2.87 | 510 |
| 2024-09-20 22:21:39.636 | MS1 | 121.4656608007 | 31.1446345822 | 643 | 504990 | -90.67 | 11.18 | 93.17 | 0.65 | 2.34 | 540 |
| 2024-09-20 22:21:40.412 | MS1 | 121.4656649657 | 31.1446202237 | 643 | 504990 | -92.27 | 11.73 | 506.17 | 0.19 | 2.65 | 1596 |
| 2024-09-20 22:21:41.852 | MS1 | 121.4656773301 | 31.1446351888 | 643 | 504990 | -91.60 | 8.28 | 296.65 | 0.06 | 2.39 | 1565 |
| 2024-09-20 22:21:42.986 | MS1 | 121.4656745652 | 31.1446371374 | 643 | 504990 | -90.58 | 7.33 | 364.26 | 0.11 | 2.82 | 1577 |

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
| 3211943 | 1 | 121.4656395782 | 31.1510154474 | 265 | 7 | 1 | 43.8 | TDD | 273 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3216376 | 3 | 121.4752684431 | 31.1551622068 | 261 | 1 | 2 | 29.8 | TDD | 643 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3219691 | 2 | 121.4705183565 | 31.1497453842 | 111 | 10 | 9 | 45.3 | TDD | 690 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3224874 | 4 | 121.4680713409 | 31.1468108044 | 25 | 1 | 10 | 29.2 | TDD | 62 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.316 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.333 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.474 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.474 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.163 | NREventA3 | measId:2;ServCellPCI:219;Se... |
| 2024-09-20 22:21:38.403 | NRHandoverAttempt | SourcePCI:219;SourceNR-ARFC... |
| 2024-09-20 22:21:38.436 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.449 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.580 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.580 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211943 | 1 | 10.2736 | 12.1594 | -116.5436 | 10.7110 | 85.4064 | 0.0102 | 0.0041 |
| 2024_09_20 22:00 | 3219691 | 2 | 19.7819 | 9.6457 | -114.5650 | 6.1808 | 187.5765 | 0.0165 | 0.0175 |
| 2024_09_20 22:00 | 3216376 | 3 | 16.0229 | 16.9474 | -115.9030 | 16.6204 | 187.7745 | 0.0044 | 0.0039 |
| 2024_09_20 22:00 | 3224874 | 4 | 8.5264 | 16.1681 | -117.6024 | 12.4681 | 167.0511 | 0.0112 | 0.0125 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413198_D824B8B9 | 504990 | 643 | -85.7 | 504990 | 62 | -91.6 | 504990 | 690 | -92.5 | 504990 | 273 |
| MR_1774413198_915C055B | 504990 | 643 | -84.6 | 504990 | 62 | -90.5 | 504990 | 690 | -92.6 | 504990 | 273 |
| MR_1774413198_398BA5B2 | 504990 | 643 | -87.2 | 504990 | 62 | -90.4 | 504990 | 690 | -93.2 | 504990 | 273 |
| MR_1774413198_3F7EE3A8 | 504990 | 643 | -86.2 | 504990 | 62 | -90.8 | 504990 | 690 | -94.0 | 504990 | 273 |
| MR_1774413198_90264BA7 | 504990 | 643 | -84.5 | 504990 | 62 | -90.3 | 504990 | 690 | -95.4 | 504990 | 273 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 806: `dad41dd7-dda...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dad41dd7-dda2-4586-8129-8eedbd488b29` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244380_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[806] topology](images/train_0806.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Adjust the azimuth of 3244380_6 by 36 degrees
- `C3`: Increase A3 Offset threshold for 3244380_6
- `C4`: Adjust the azimuth of 3279378_2 by 16 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279378_2
- `C6`: Decrease transmission power for 3279378_2
- `C7`: Decrease transmission power for 3244380_6
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244380_6
- `C9`: Lift the tilt angle of 3244380_6 by 1 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase A3 Offset threshold for 3279378_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244380_6 **← 정답**
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279378_2
- `C14`: Lift the tilt angle  of 3279378_2 by 4 degrees
- `C15`: Increase transmission power for 3244380_6
- `C16`: Increase transmission power for 3279378_2
- `C17`: Add neighbor relationship between 3238240_8 and 3279378_2
- `C18`: Add neighbor relationship between 3244380_6 and 3279378_2
- `C19`: Decrease A3 Offset threshold for 3244380_6
- `C20`: Press down the tilt angle  of 3279378_2 by 4 degrees
- `C21`: Decrease A3 Offset threshold for 3279378_2
- `C22`: Press down the tilt angle of 3244380_6 by 1 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.500 | MS1 | 121.4656778077 | 31.1446194118 | 438 | 504990 | -94.23 | 12.90 | 341.50 | 0.06 | 2.73 | 1590 |
| 2024-09-20 22:21:32.699 | MS1 | 121.4656718019 | 31.1446368579 | 674 | 504990 | -94.33 | 10.28 | 448.19 | 0.17 | 2.18 | 1561 |
| 2024-09-20 22:21:33.520 | MS1 | 121.4656612024 | 31.1446293558 | 116 | 504990 | -93.27 | 13.89 | 398.37 | 0.11 | 2.27 | 1579 |
| 2024-09-20 22:21:34.701 | MS1 | 121.4656602984 | 31.1446375218 | 99 | 152650 | -94.22 | 6.08 | 91.60 | 0.11 | 1.91 | 948 |
| 2024-09-20 22:21:35.507 | MS1 | 121.4656730084 | 31.1446307077 | 725 | 152650 | -95.73 | 7.16 | 56.72 | 0.01 | 1.76 | 915 |
| 2024-09-20 22:21:36.336 | MS1 | 121.4656615243 | 31.1446280206 | 546 | 152650 | -94.79 | 3.92 | 97.48 | 0.07 | 1.98 | 924 |
| 2024-09-20 22:21:37.172 | MS1 | 121.4656773822 | 31.1446196248 | 450 | 152650 | -93.11 | 3.75 | 70.68 | 0.19 | 1.69 | 988 |
| 2024-09-20 22:21:38.779 | MS1 | 121.4656690402 | 31.1446211303 | 99 | 152650 | -89.94 | 5.21 | 87.04 | 0.08 | 1.98 | 938 |
| 2024-09-20 22:21:39.430 | MS1 | 121.4656605490 | 31.1446252172 | 725 | 152650 | -88.89 | 5.31 | 97.64 | 0.10 | 1.71 | 902 |
| 2024-09-20 22:21:40.499 | MS1 | 121.4656751529 | 31.1446244152 | 546 | 152650 | -92.60 | 2.73 | 84.86 | 0.15 | 2.79 | 1580 |
| 2024-09-20 22:21:41.259 | MS1 | 121.4656708618 | 31.1446333975 | 450 | 152650 | -91.32 | 7.66 | 56.57 | 0.11 | 2.65 | 1596 |
| 2024-09-20 22:21:42.739 | MS1 | 121.4656679844 | 31.1446222013 | 99 | 152650 | -90.13 | 3.31 | 92.71 | 0.02 | 2.66 | 1560 |

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
| 3211065 | 4 | 121.4680529770 | 31.1484508605 | 55 | 4 | 0 | 1.4 | TDD | 947 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3227653 | 5 | 121.4675630490 | 31.1459414086 | 47 | 0 | 4 | 7.0 | TDD | 116 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3228816 | 13 | 121.4714957785 | 31.1505218354 | 249 | 9 | 3 | 12.1 | FDD | 663 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3230198 | 12 | 121.4642057679 | 31.1446707372 | 305 | 14 | 2 | 2.5 | FDD | 725 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3238240 | 8 | 121.4711926258 | 31.1471382048 | 132 | 8 | 3 | 22.8 | FDD | 546 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3244380 | 6 | 121.4651796193 | 31.1509507853 | 212 | 0 | 1 | 9.1 | TDD | 438 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3246707 | 10 | 121.4699988275 | 31.1468651501 | 116 | 14 | 3 | 17.3 | FDD | 294 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3248826 | 11 | 121.4695868744 | 31.1543141075 | 345 | 5 | 2 | 29.1 | FDD | 145 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3249926 | 7 | 121.4733228903 | 31.1481088555 | 253 | 4 | 8 | 18.6 | FDD | 450 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3258857 | 1 | 121.4648585226 | 31.1447464332 | 345 | 13 | 9 | 18.4 | TDD | 674 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3266198 | 9 | 121.4717472931 | 31.1522416904 | 75 | 15 | 11 | 7.7 | FDD | 99 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3268803 | 3 | 121.4736130015 | 31.1488245339 | 70 | 15 | 6 | 17.3 | TDD | 366 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3279378 | 2 | 121.4725140622 | 31.1455766815 | 277 | 3 | 9 | 8.5 | TDD | 678 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.084 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.100 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.211 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.211 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.969 | NREventA2 | measId:1;ServCellPCI:756;Se... |
| 2024-09-20 22:21:35.102 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.335 | NREventA5 | measId:3;ServCellPCI:756;Se... |
| 2024-09-20 22:21:35.370 | NRHandoverAttempt | SourcePCI:756;SourceNR-ARFC... |
| 2024-09-20 22:21:35.416 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.430 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.554 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.554 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258857 | 1 | 16.9835 | 16.0832 | -117.4687 | 6.4911 | 194.1625 | 0.0124 | 0.0170 |
| 2024_09_20 22:00 | 3279378 | 2 | 11.9287 | 16.4090 | -114.1701 | 5.3415 | 156.8902 | 0.0140 | 0.0140 |
| 2024_09_20 22:00 | 3268803 | 3 | 13.1869 | 17.1696 | -116.9212 | 13.2091 | 174.4879 | 0.0138 | 0.0183 |
| 2024_09_20 22:00 | 3211065 | 4 | 17.5111 | 17.4791 | -114.0892 | 19.3564 | 192.0799 | 0.0039 | 0.0188 |
| 2024_09_20 22:00 | 3227653 | 5 | 7.8126 | 5.2895 | -117.4346 | 8.3344 | 167.8942 | 0.0024 | 0.0033 |
| 2024_09_20 22:00 | 3244380 | 6 | 16.2108 | 15.0901 | -115.9402 | 18.9721 | 147.2034 | 0.0185 | 0.0162 |
| 2024_09_20 22:00 | 3249926 | 7 | 15.1409 | 5.4822 | -116.2039 | 3.8599 | 23.8691 | 0.0022 | 0.0135 |
| 2024_09_20 22:00 | 3238240 | 8 | 14.9080 | 11.9488 | -116.6088 | 4.7217 | 48.6891 | 0.0045 | 0.0137 |
| 2024_09_20 22:00 | 3266198 | 9 | 12.0401 | 17.1631 | -116.5289 | 3.1848 | 47.5753 | 0.0042 | 0.0118 |
| 2024_09_20 22:00 | 3246707 | 10 | 6.4901 | 12.6746 | -116.5443 | 4.5088 | 28.6252 | 0.0111 | 0.0044 |
| 2024_09_20 22:00 | 3248826 | 11 | 14.7576 | 18.3559 | -115.9934 | 4.0464 | 26.8899 | 0.0199 | 0.0122 |
| 2024_09_20 22:00 | 3230198 | 12 | 16.5362 | 8.7423 | -114.1790 | 3.6796 | 55.2488 | 0.0027 | 0.0197 |
| 2024_09_20 22:00 | 3228816 | 13 | 5.5211 | 16.5223 | -115.0292 | 3.9455 | 42.8978 | 0.0133 | 0.0114 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413487_96489E6E | 152650 | 99 | -94.2 | 152650 | 294 | -100.0 | 152650 | 663 | -105.4 | 152650 | 145 |
| MR_1774413487_4ABDC860 | 152650 | 99 | -92.4 | 152650 | 294 | -100.6 | 152650 | 663 | -103.5 | 152650 | 145 |
| MR_1774413487_897426F4 | 152650 | 99 | -95.3 | 152650 | 294 | -100.2 | 152650 | 663 | -103.8 | 152650 | 145 |
| MR_1774413487_842DF288 | 504990 | 116 | -92.3 | 504990 | 678 | -91.9 | 504990 | 947 | -95.9 | 504990 | 366 |
| MR_1774413487_91DFCD31 | 152650 | 99 | -92.7 | 152650 | 294 | -100.1 | 152650 | 663 | -105.7 | 152650 | 145 |
| MR_1774413487_BB9514EE | 152650 | 99 | -95.8 | 152650 | 294 | -97.3 | 152650 | 663 | -105.4 | 152650 | 145 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 807: `9eb137e0-97e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9eb137e0-97e2-4d1d-8247-b927d187eb7e` |
| Tag | **multiple-answer** |
| 정답 | **C8|C13** |
| C8 의미 | Adjust the azimuth of 3230844_1 by 50 degrees |
| C13 의미 | Increase transmission power for 3230844_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[807] topology](images/train_0807.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3234995_2
- `C2`: Increase A3 Offset threshold for 3230844_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234995_2
- `C4`: Lift the tilt angle of 3230844_1 by 10 degrees
- `C5`: Press down the tilt angle of 3230844_1 by 10 degrees
- `C6`: Decrease A3 Offset threshold for 3234995_2
- `C7`: Increase transmission power for 3234995_2
- `C8`: Adjust the azimuth of 3230844_1 by 50 degrees **← 정답**
- `C9`: Lift the tilt angle  of 3234995_2 by 5 degrees
- `C10`: Decrease transmission power for 3234995_2
- `C11`: Decrease transmission power for 3230844_1
- `C12`: Press down the tilt angle  of 3234995_2 by 5 degrees
- `C13`: Increase transmission power for 3230844_1 **← 정답**
- `C14`: Decrease A3 Offset threshold for 3230844_1
- `C15`: Adjust the azimuth of 3234995_2 by 9 degrees
- `C16`: Add neighbor relationship between 3244785_3 and 3234995_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230844_1
- `C18`: Check test server and transmission issues
- `C19`: Add neighbor relationship between 3230844_1 and 3234995_2
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230844_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234995_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.458 | MS1 | 121.4656744106 | 31.1446350652 | 226 | 504990 | -94.37 | 14.45 | 550.75 | 0.16 | 2.80 | 1577 |
| 2024-09-20 22:21:32.519 | MS1 | 121.4656637180 | 31.1446283542 | 226 | 504990 | -90.07 | 12.60 | 454.68 | 0.19 | 2.57 | 1566 |
| 2024-09-20 22:21:33.838 | MS1 | 121.4656729945 | 31.1446265939 | 226 | 504990 | -93.06 | 16.68 | 553.73 | 0.18 | 2.68 | 1574 |
| 2024-09-20 22:21:34.604 | MS1 | 121.4656695191 | 31.1446256129 | 226 | 504990 | -108.82 | 1.05 | 24.39 | 0.16 | 1.29 | 1586 |
| 2024-09-20 22:21:35.215 | MS1 | 121.4656731234 | 31.1446315751 | 226 | 504990 | -101.88 | 1.95 | 26.57 | 0.08 | 1.42 | 1583 |
| 2024-09-20 22:21:36.788 | MS1 | 121.4656712890 | 31.1446260913 | 226 | 504990 | -107.43 | -1.40 | 26.29 | 0.03 | 1.46 | 1595 |
| 2024-09-20 22:21:37.156 | MS1 | 121.4656702102 | 31.1446301162 | 226 | 504990 | -104.25 | -0.87 | 25.29 | 0.18 | 1.40 | 1570 |
| 2024-09-20 22:21:38.309 | MS1 | 121.4656695629 | 31.1446341624 | 226 | 504990 | -103.54 | -1.59 | 42.13 | 0.02 | 1.03 | 1584 |
| 2024-09-20 22:21:39.341 | MS1 | 121.4656690590 | 31.1446214284 | 226 | 504990 | -106.06 | -0.05 | 19.54 | 0.04 | 1.28 | 1600 |
| 2024-09-20 22:21:40.947 | MS1 | 121.4656735897 | 31.1446263504 | 226 | 504990 | -92.22 | 12.38 | 383.73 | 0.03 | 2.42 | 1588 |
| 2024-09-20 22:21:41.300 | MS1 | 121.4656637659 | 31.1446302605 | 226 | 504990 | -93.41 | 14.03 | 361.91 | 0.19 | 2.02 | 1574 |
| 2024-09-20 22:21:42.350 | MS1 | 121.4656651652 | 31.1446377860 | 226 | 504990 | -89.45 | 13.05 | 455.66 | 0.16 | 2.52 | 1595 |

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
| 3230844 | 1 | 121.4719394662 | 31.1543596619 | 136 | 14 | 4 | 42.2 | TDD | 226 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3233482 | 4 | 121.4651098221 | 31.1539056924 | 29 | 15 | 6 | 22.2 | TDD | 642 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3234995 | 2 | 121.4721421690 | 31.1462233250 | 263 | 2 | 5 | 31.9 | TDD | 484 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3244785 | 3 | 121.4707955174 | 31.1489236139 | 52 | 3 | 2 | 21.1 | TDD | 119 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.647 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.662 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.762 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.762 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.968 | NREventA2 | measId:1;ServCellPCI:287;Se... |
| 2024-09-20 22:21:35.081 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230844 | 1 | 5.3409 | 13.9517 | -116.4660 | 7.1973 | 136.9111 | 0.1709 | 0.0042 |
| 2024_09_20 22:00 | 3234995 | 2 | 8.9761 | 10.0703 | -114.7210 | 17.0761 | 184.1911 | 0.0026 | 0.0110 |
| 2024_09_20 22:00 | 3244785 | 3 | 8.9403 | 9.7550 | -116.9109 | 17.8853 | 168.8462 | 0.0018 | 0.0165 |
| 2024_09_20 22:00 | 3233482 | 4 | 14.4419 | 8.9390 | -115.7699 | 13.2713 | 101.2308 | 0.0087 | 0.0112 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416964_123BC085 | 504990 | 226 | -109.1 | 504990 | 484 | -113.5 | 504990 | 119 | -122.0 | 504990 | 642 |
| MR_1774416964_DF90BD19 | 504990 | 226 | -107.6 | 504990 | 484 | -114.5 | 504990 | 119 | -118.4 | 504990 | 642 |
| MR_1774416964_304E96DA | 504990 | 226 | -107.6 | 504990 | 484 | -112.3 | 504990 | 119 | -119.2 | 504990 | 642 |
| MR_1774416964_C6B51BDA | 504990 | 226 | -108.7 | 504990 | 484 | -115.2 | 504990 | 119 | -119.2 | 504990 | 642 |
| MR_1774416964_0BC9A3EB | 504990 | 226 | -109.0 | 504990 | 484 | -113.0 | 504990 | 119 | -121.7 | 504990 | 642 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 808: `5e14ff8b-af8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5e14ff8b-af83-4c55-9208-c24330294621` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Add neighbor relationship between 3217600_2 and 3268107_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[808] topology](images/train_0808.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3217600_2
- `C2`: Increase A3 Offset threshold for 3217600_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268107_4
- `C4`: Adjust the azimuth of 3268107_4 by 31 degrees
- `C5`: Add neighbor relationship between 3217600_2 and 3268107_4 **← 정답**
- `C6`: Check test server and transmission issues
- `C7`: Increase A3 Offset threshold for 3268107_4
- `C8`: Increase transmission power for 3268107_4
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Add neighbor relationship between 3274619_1 and 3268107_4
- `C11`: Increase transmission power for 3217600_2
- `C12`: Adjust the azimuth of 3217600_2 by 50 degrees
- `C13`: Lift the tilt angle of 3217600_2 by 6 degrees
- `C14`: Decrease A3 Offset threshold for 3268107_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217600_2
- `C16`: Press down the tilt angle of 3217600_2 by 6 degrees
- `C17`: Lift the tilt angle  of 3268107_4 by 3 degrees
- `C18`: Decrease A3 Offset threshold for 3217600_2
- `C19`: Press down the tilt angle  of 3268107_4 by 3 degrees
- `C20`: Decrease transmission power for 3268107_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268107_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217600_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.662 | MS1 | 121.4656604846 | 31.1446324646 | 123 | 504990 | -80.53 | 14.97 | 403.38 | 0.15 | 2.24 | 1568 |
| 2024-09-20 22:21:32.795 | MS1 | 121.4656591868 | 31.1446190748 | 123 | 504990 | -82.22 | 14.28 | 346.31 | 0.16 | 2.45 | 1560 |
| 2024-09-20 22:21:33.384 | MS1 | 121.4656623226 | 31.1446199554 | 123 | 504990 | -83.27 | 16.38 | 298.67 | 0.07 | 2.11 | 1600 |
| 2024-09-20 22:21:34.353 | MS1 | 121.4656760404 | 31.1446354377 | 123 | 504990 | -94.20 | -0.51 | 34.91 | 0.14 | 1.33 | 1599 |
| 2024-09-20 22:21:35.522 | MS1 | 121.4656612182 | 31.1446357855 | 123 | 504990 | -90.14 | -3.00 | 29.37 | 0.07 | 1.22 | 1566 |
| 2024-09-20 22:21:36.971 | MS1 | 121.4656770681 | 31.1446330446 | 123 | 504990 | -86.42 | -0.49 | 32.88 | 0.08 | 1.46 | 1597 |
| 2024-09-20 22:21:37.494 | MS1 | 121.4656644617 | 31.1446189750 | 123 | 504990 | -87.03 | -0.77 | 76.28 | 0.19 | 1.42 | 1575 |
| 2024-09-20 22:21:38.985 | MS1 | 121.4656748427 | 31.1446240511 | 123 | 504990 | -84.34 | 12.78 | 386.47 | 0.00 | 1.02 | 1564 |
| 2024-09-20 22:21:39.371 | MS1 | 121.4656725220 | 31.1446346776 | 123 | 504990 | -75.73 | 16.63 | 541.53 | 0.12 | 1.07 | 1597 |
| 2024-09-20 22:21:40.350 | MS1 | 121.4656771343 | 31.1446356782 | 123 | 504990 | -75.60 | 16.11 | 582.05 | 0.08 | 2.93 | 1589 |
| 2024-09-20 22:21:41.472 | MS1 | 121.4656619208 | 31.1446327023 | 123 | 504990 | -76.85 | 16.10 | 552.19 | 0.03 | 2.40 | 1564 |
| 2024-09-20 22:21:42.147 | MS1 | 121.4656698017 | 31.1446241246 | 123 | 504990 | -81.57 | 17.71 | 564.98 | 0.17 | 2.66 | 1566 |

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
| 3217600 | 2 | 121.4703508400 | 31.1525490117 | 332 | 4 | 12 | 31.7 | TDD | 123 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3242882 | 3 | 121.4695718554 | 31.1545398681 | 51 | 5 | 4 | 36.5 | TDD | 637 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3268107 | 4 | 121.4744138231 | 31.1469578120 | 284 | 1 | 7 | 32.6 | TDD | 134 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3274619 | 1 | 121.4651651771 | 31.1496521497 | 140 | 1 | 6 | 22.1 | TDD | 817 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.132 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.152 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.269 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.269 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.005 | NREventA3 | measId:2;ServCellPCI:73;Ser... |
| 2024-09-20 22:21:36.005 | NREventA3 | measId:2;ServCellPCI:73;Ser... |
| 2024-09-20 22:21:37.005 | NREventA3 | measId:2;ServCellPCI:73;Ser... |
| 2024-09-20 22:21:39.505 | NRRRCReestablishAttempt | PCI:73 |
| 2024-09-20 22:21:39.516 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.531 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.671 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.671 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274619 | 1 | 11.9459 | 11.1105 | -114.2134 | 19.7261 | 179.5799 | 0.0077 | 0.0036 |
| 2024_09_20 22:00 | 3217600 | 2 | 13.2962 | 17.9690 | -117.4873 | 16.3761 | 81.9950 | 0.0092 | 0.1114 |
| 2024_09_20 22:00 | 3242882 | 3 | 12.0002 | 10.3291 | -116.9940 | 5.1642 | 99.2497 | 0.0129 | 0.0003 |
| 2024_09_20 22:00 | 3268107 | 4 | 8.8030 | 5.2031 | -115.9799 | 12.3841 | 91.6551 | 0.0169 | 0.0002 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414934_65DD9F21 | 504990 | 134 | -90.2 | 504990 | 123 | -92.2 | 504990 | 817 | -93.8 | 504990 | 637 |
| MR_1774414934_162B0D45 | 504990 | 123 | -95.4 | 504990 | 134 | -90.4 | 504990 | 817 | -92.0 | 504990 | 637 |
| MR_1774414934_5066CD33 | 504990 | 123 | -93.5 | 504990 | 134 | -89.1 | 504990 | 817 | -93.2 | 504990 | 637 |
| MR_1774414934_3C86992E | 504990 | 134 | -90.5 | 504990 | 123 | -95.9 | 504990 | 817 | -93.4 | 504990 | 637 |
| MR_1774414934_A16B8520 | 504990 | 123 | -95.8 | 504990 | 134 | -88.6 | 504990 | 817 | -91.4 | 504990 | 637 |
| MR_1774414934_A98821AB | 504990 | 123 | -92.9 | 504990 | 134 | -88.3 | 504990 | 817 | -94.5 | 504990 | 637 |
| MR_1774414934_072016C1 | 504990 | 123 | -95.2 | 504990 | 134 | -88.4 | 504990 | 817 | -94.0 | 504990 | 637 |
| MR_1774414934_413C2676 | 504990 | 134 | -90.3 | 504990 | 123 | -94.7 | 504990 | 817 | -91.8 | 504990 | 637 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 809: `7935ca0b-d37...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7935ca0b-d372-4b8e-a19c-2aa1ccbe6f54` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Decrease A3 Offset threshold for 3276488_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[809] topology](images/train_0809.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276488_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276488_3
- `C3`: Decrease transmission power for 3237035_1
- `C4`: Press down the tilt angle  of 3237035_1 by 10 degrees
- `C5`: Lift the tilt angle  of 3237035_1 by 10 degrees
- `C6`: Increase transmission power for 3237035_1
- `C7`: Decrease A3 Offset threshold for 3237035_1
- `C8`: Add neighbor relationship between 3276488_3 and 3237035_1
- `C9`: Check test server and transmission issues
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237035_1
- `C11`: Decrease transmission power for 3276488_3
- `C12`: Increase A3 Offset threshold for 3237035_1
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Adjust the azimuth of 3276488_3 by 50 degrees
- `C15`: Adjust the azimuth of 3237035_1 by 50 degrees
- `C16`: Add neighbor relationship between 3213277_4 and 3237035_1
- `C17`: Decrease A3 Offset threshold for 3276488_3 **← 정답**
- `C18`: Increase transmission power for 3276488_3
- `C19`: Increase A3 Offset threshold for 3276488_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237035_1
- `C21`: Lift the tilt angle of 3276488_3 by 6 degrees
- `C22`: Press down the tilt angle of 3276488_3 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.405 | MS1 | 121.4656685340 | 31.1446199091 | 234 | 504990 | -75.16 | 17.52 | 406.70 | 0.02 | 2.99 | 1579 |
| 2024-09-20 22:21:32.665 | MS1 | 121.4656751385 | 31.1446184651 | 234 | 504990 | -77.76 | 15.92 | 427.69 | 0.08 | 2.29 | 1564 |
| 2024-09-20 22:21:33.941 | MS1 | 121.4656638625 | 31.1446368202 | 234 | 504990 | -83.41 | 13.02 | 596.55 | 0.04 | 2.23 | 1592 |
| 2024-09-20 22:21:34.798 | MS1 | 121.4656732859 | 31.1446254378 | 234 | 504990 | -92.33 | -2.11 | 62.96 | 0.16 | 1.13 | 1581 |
| 2024-09-20 22:21:35.892 | MS1 | 121.4656772180 | 31.1446305276 | 234 | 504990 | -89.31 | -1.42 | 71.32 | 0.05 | 1.41 | 1590 |
| 2024-09-20 22:21:36.699 | MS1 | 121.4656587589 | 31.1446348578 | 234 | 504990 | -90.14 | -1.47 | 41.08 | 0.13 | 1.44 | 1594 |
| 2024-09-20 22:21:37.415 | MS1 | 121.4656611144 | 31.1446265236 | 234 | 504990 | -90.80 | -3.66 | 63.97 | 0.15 | 1.01 | 1600 |
| 2024-09-20 22:21:38.831 | MS1 | 121.4656734811 | 31.1446235111 | 234 | 504990 | -84.76 | -2.72 | 68.50 | 0.06 | 1.25 | 1600 |
| 2024-09-20 22:21:39.723 | MS1 | 121.4656779288 | 31.1446292017 | 688 | 504990 | -75.06 | 13.34 | 297.38 | 0.18 | 1.25 | 1564 |
| 2024-09-20 22:21:40.684 | MS1 | 121.4656667280 | 31.1446301619 | 688 | 504990 | -82.03 | 15.20 | 538.89 | 0.16 | 2.21 | 1582 |
| 2024-09-20 22:21:41.623 | MS1 | 121.4656694505 | 31.1446212969 | 688 | 504990 | -79.69 | 15.27 | 537.43 | 0.04 | 2.67 | 1568 |
| 2024-09-20 22:21:42.213 | MS1 | 121.4656623658 | 31.1446280239 | 688 | 504990 | -75.72 | 13.24 | 358.71 | 0.18 | 2.31 | 1591 |

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
| 3213277 | 4 | 121.4664873816 | 31.1538280116 | 231 | 12 | 5 | 19.6 | TDD | 223 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3237035 | 1 | 121.4675659907 | 31.1496555981 | 293 | 12 | 3 | 46.0 | TDD | 688 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3276488 | 3 | 121.4673077835 | 31.1537837843 | 128 | 4 | 11 | 39.5 | TDD | 234 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3279916 | 2 | 121.4641200450 | 31.1481559108 | 241 | 11 | 4 | 23.7 | TDD | 321 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.320 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.338 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.469 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.469 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.127 | NREventA3 | measId:2;ServCellPCI:640;Se... |
| 2024-09-20 22:21:38.367 | NRHandoverAttempt | SourcePCI:640;SourceNR-ARFC... |
| 2024-09-20 22:21:38.403 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.414 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.525 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.525 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237035 | 1 | 17.5139 | 8.3749 | -114.5122 | 18.9799 | 150.0266 | 0.0108 | 0.0049 |
| 2024_09_20 22:00 | 3279916 | 2 | 6.8376 | 12.7775 | -115.5689 | 8.6708 | 96.5827 | 0.0188 | 0.0162 |
| 2024_09_20 22:00 | 3276488 | 3 | 16.8112 | 19.0268 | -117.2489 | 15.3070 | 124.4575 | 0.0130 | 0.1651 |
| 2024_09_20 22:00 | 3213277 | 4 | 7.1663 | 16.9768 | -114.7442 | 12.2782 | 125.8612 | 0.0020 | 0.0138 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416678_45F721FC | 504990 | 688 | -87.7 | 504990 | 234 | -93.8 | 504990 | 223 | -90.6 | 504990 | 321 |
| MR_1774416678_33C6F4D0 | 504990 | 234 | -90.6 | 504990 | 688 | -87.8 | 504990 | 223 | -89.6 | 504990 | 321 |
| MR_1774416678_1ACBEA76 | 504990 | 688 | -88.2 | 504990 | 234 | -90.8 | 504990 | 223 | -92.3 | 504990 | 321 |
| MR_1774416678_565B7CCB | 504990 | 234 | -92.4 | 504990 | 688 | -87.5 | 504990 | 223 | -91.8 | 504990 | 321 |
| MR_1774416678_F3FE03A4 | 504990 | 688 | -89.6 | 504990 | 234 | -90.3 | 504990 | 223 | -89.5 | 504990 | 321 |
| MR_1774416678_BD3DFE00 | 504990 | 688 | -88.8 | 504990 | 234 | -93.6 | 504990 | 223 | -89.7 | 504990 | 321 |
| MR_1774416678_751A5F14 | 504990 | 234 | -91.3 | 504990 | 688 | -89.6 | 504990 | 223 | -91.6 | 504990 | 321 |
| MR_1774416678_29646753 | 504990 | 234 | -91.4 | 504990 | 688 | -87.6 | 504990 | 223 | -91.1 | 504990 | 321 |

> *... 2개 열 생략 (전체 14열)*

---
