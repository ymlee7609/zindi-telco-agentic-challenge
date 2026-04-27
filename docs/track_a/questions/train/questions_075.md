# Track A 문제 분석 — train[740]~train[749]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[740] ~ train[749] (10개)

## 목차

1. [문제 740: `32272d98-4b6...`](#740) — single-answer, 정답: C20
2. [문제 741: `82c132df-421...`](#741) — single-answer, 정답: C8
3. [문제 742: `c38dc81f-64f...`](#742) — single-answer, 정답: C10
4. [문제 743: `37745902-9ef...`](#743) — single-answer, 정답: C2
5. [문제 744: `48371fec-0c6...`](#744) — single-answer, 정답: C3
6. [문제 745: `1511bef9-87c...`](#745) — single-answer, 정답: C18
7. [문제 746: `3281b6fa-2d6...`](#746) — single-answer, 정답: C11
8. [문제 747: `721f7718-154...`](#747) — single-answer, 정답: C2
9. [문제 748: `8e7392fe-56a...`](#748) — single-answer, 정답: C17
10. [문제 749: `8d1d8be4-d33...`](#749) — single-answer, 정답: C16

---

### 문제 740: `32272d98-4b6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `32272d98-4b6c-4f33-bf4e-830afa5f841f` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[740] topology](images/train_0740.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3270238_4
- `C2`: Increase A3 Offset threshold for 3251578_3
- `C3`: Increase transmission power for 3251578_3
- `C4`: Increase transmission power for 3270238_4
- `C5`: Decrease A3 Offset threshold for 3251578_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251578_3
- `C7`: Add neighbor relationship between 3251578_3 and 3270238_4
- `C8`: Decrease A3 Offset threshold for 3270238_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270238_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251578_3
- `C11`: Adjust the azimuth of 3251578_3 by 50 degrees
- `C12`: Lift the tilt angle  of 3270238_4 by 7 degrees
- `C13`: Add neighbor relationship between 3210869_1 and 3270238_4
- `C14`: Decrease transmission power for 3270238_4
- `C15`: Check test server and transmission issues
- `C16`: Press down the tilt angle  of 3270238_4 by 7 degrees
- `C17`: Press down the tilt angle of 3251578_3 by 8 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270238_4
- `C19`: Decrease transmission power for 3251578_3
- `C20`: Insufficient data; more data is needed for judgment. **← 정답**
- `C21`: Adjust the azimuth of 3270238_4 by 50 degrees
- `C22`: Lift the tilt angle of 3251578_3 by 8 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.925 | MS1 | 121.4656635125 | 31.1446280936 | 726 | 504990 | -88.75 | 16.59 | 498.28 | 0.07 | 2.15 | 1575 |
| 2024-09-20 22:21:32.352 | MS1 | 121.4656766907 | 31.1446200813 | 726 | 504990 | -86.47 | 14.27 | 419.69 | 0.07 | 2.09 | 1586 |
| 2024-09-20 22:21:33.380 | MS1 | 121.4656647163 | 31.1446237731 | 726 | 504990 | -90.36 | 13.60 | 459.00 | 0.14 | 2.11 | 1565 |
| 2024-09-20 22:21:34.625 | MS1 | 121.4656666406 | 31.1446373178 | 726 | 504990 | -91.37 | 14.01 | 50.76 | 0.08 | 2.69 | 1563 |
| 2024-09-20 22:21:35.597 | MS1 | 121.4656701822 | 31.1446297995 | 726 | 504990 | -90.06 | 14.47 | 70.39 | 0.07 | 2.50 | 1573 |
| 2024-09-20 22:21:36.763 | MS1 | 121.4656610680 | 31.1446344495 | 726 | 504990 | -91.32 | 12.74 | 71.23 | 0.01 | 2.23 | 1565 |
| 2024-09-20 22:21:37.212 | MS1 | 121.4656735680 | 31.1446375980 | 726 | 504990 | -91.70 | 10.28 | 72.58 | 0.03 | 2.63 | 1579 |
| 2024-09-20 22:21:38.970 | MS1 | 121.4656598762 | 31.1446355326 | 726 | 504990 | -89.75 | 7.59 | 88.48 | 0.12 | 2.03 | 1572 |
| 2024-09-20 22:21:39.970 | MS1 | 121.4656673144 | 31.1446325924 | 726 | 504990 | -91.77 | 11.32 | 86.53 | 0.09 | 2.04 | 1560 |
| 2024-09-20 22:21:40.112 | MS1 | 121.4656663104 | 31.1446366210 | 726 | 504990 | -89.43 | 9.20 | 594.24 | 0.18 | 2.35 | 1582 |
| 2024-09-20 22:21:41.364 | MS1 | 121.4656655175 | 31.1446208419 | 726 | 504990 | -89.49 | 12.61 | 405.46 | 0.19 | 2.87 | 1563 |
| 2024-09-20 22:21:42.340 | MS1 | 121.4656657289 | 31.1446200539 | 726 | 504990 | -93.53 | 9.08 | 433.79 | 0.01 | 2.02 | 1591 |

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
| 3210869 | 1 | 121.4692270619 | 31.1517767267 | 43 | 10 | 3 | 22.3 | TDD | 266 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3242039 | 2 | 121.4643789915 | 31.1527912940 | 172 | 7 | 0 | 33.5 | TDD | 811 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3251578 | 3 | 121.4704143307 | 31.1547174087 | 134 | 7 | 7 | 24.2 | TDD | 726 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3270238 | 4 | 121.4650874959 | 31.1498039621 | 35 | 3 | 10 | 40.0 | TDD | 763 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.230 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.336 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.336 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.024 | NREventA3 | measId:2;ServCellPCI:822;Se... |
| 2024-09-20 22:21:38.264 | NRHandoverAttempt | SourcePCI:822;SourceNR-ARFC... |
| 2024-09-20 22:21:38.300 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.311 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.419 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.419 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3210869 | 1 | 91.4115 | 80.3135 | -117.3272 | 6.4725 | 163.9403 | 0.0195 | 0.0145 |
| 2024_09_19 22:00 | 3242039 | 2 | 81.1116 | 84.1031 | -116.0242 | 7.7451 | 162.0091 | 0.0175 | 0.0109 |
| 2024_09_19 22:00 | 3251578 | 3 | 79.2598 | 88.1729 | -116.2501 | 5.9527 | 87.0133 | 0.0090 | 0.0035 |
| 2024_09_19 22:00 | 3270238 | 4 | 94.6952 | 77.8273 | -115.9909 | 15.2786 | 182.1069 | 0.0076 | 0.0133 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415658_C773C643 | 504990 | 726 | -92.9 | 504990 | 763 | -98.8 | 504990 | 266 | -103.4 | 504990 | 811 |
| MR_1774415658_7B3FA84F | 504990 | 726 | -90.8 | 504990 | 763 | -101.2 | 504990 | 266 | -105.4 | 504990 | 811 |
| MR_1774415658_B79DCA38 | 504990 | 726 | -89.9 | 504990 | 763 | -98.5 | 504990 | 266 | -102.1 | 504990 | 811 |
| MR_1774415658_9CFE90FD | 504990 | 726 | -90.7 | 504990 | 763 | -100.5 | 504990 | 266 | -102.0 | 504990 | 811 |
| MR_1774415658_A4FA9F47 | 504990 | 726 | -89.9 | 504990 | 763 | -99.7 | 504990 | 266 | -105.2 | 504990 | 811 |
| MR_1774415658_F4660EBA | 504990 | 726 | -93.3 | 504990 | 763 | -101.2 | 504990 | 266 | -105.2 | 504990 | 811 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 741: `82c132df-421...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `82c132df-4211-4c98-973e-4008fdb11c52` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Lift the tilt angle  of 3257959_1 by 6 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[741] topology](images/train_0741.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3232810_4
- `C2`: Press down the tilt angle  of 3257959_1 by 6 degrees
- `C3`: Decrease A3 Offset threshold for 3278348_2
- `C4`: Increase transmission power for 3278348_2
- `C5`: Increase transmission power for 3232810_4
- `C6`: Decrease A3 Offset threshold for 3232810_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232810_4
- `C8`: Lift the tilt angle  of 3257959_1 by 6 degrees **← 정답**
- `C9`: Decrease transmission power for 3278348_2
- `C10`: Decrease transmission power for 3232810_4
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232810_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278348_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278348_2
- `C15`: Lift the tilt angle of 3278348_2 by 5 degrees
- `C16`: Check test server and transmission issues
- `C17`: Increase A3 Offset threshold for 3278348_2
- `C18`: Adjust the azimuth of 3257959_1 by 50 degrees
- `C19`: Press down the tilt angle of 3278348_2 by 5 degrees
- `C20`: Add neighbor relationship between 3278348_2 and 3232810_4
- `C21`: Add neighbor relationship between 3257959_1 and 3232810_4
- `C22`: Adjust the azimuth of 3278348_2 by 46 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.387 | MS1 | 121.4656625560 | 31.1446253372 | 843 | 504990 | -86.52 | 15.86 | 336.82 | 0.12 | 2.94 | 1593 |
| 2024-09-20 22:21:32.433 | MS1 | 121.4656772453 | 31.1446234748 | 843 | 504990 | -91.45 | 16.95 | 586.86 | 0.19 | 2.06 | 1564 |
| 2024-09-20 22:21:33.378 | MS1 | 121.4656645482 | 31.1446205398 | 843 | 504990 | -90.83 | 14.26 | 459.67 | 0.15 | 2.24 | 1568 |
| 2024-09-20 22:21:34.649 | MS1 | 121.4656751479 | 31.1446202414 | 843 | 504990 | -89.74 | 14.31 | 59.52 | 0.07 | 2.15 | 1571 |
| 2024-09-20 22:21:35.854 | MS1 | 121.4656718350 | 31.1446348754 | 843 | 504990 | -89.37 | 12.42 | 63.10 | 0.03 | 2.72 | 1583 |
| 2024-09-20 22:21:36.559 | MS1 | 121.4656674334 | 31.1446367619 | 843 | 504990 | -88.46 | 15.97 | 60.94 | 0.13 | 2.25 | 1587 |
| 2024-09-20 22:21:37.213 | MS1 | 121.4656692459 | 31.1446260766 | 843 | 504990 | -93.17 | 11.93 | 75.43 | 0.10 | 2.98 | 1571 |
| 2024-09-20 22:21:38.377 | MS1 | 121.4656594444 | 31.1446299885 | 843 | 504990 | -91.85 | 9.76 | 76.63 | 0.14 | 2.18 | 1569 |
| 2024-09-20 22:21:39.728 | MS1 | 121.4656717482 | 31.1446360999 | 843 | 504990 | -93.25 | 12.33 | 82.59 | 0.03 | 2.04 | 1570 |
| 2024-09-20 22:21:40.149 | MS1 | 121.4656656924 | 31.1446270866 | 843 | 504990 | -89.95 | 12.58 | 525.22 | 0.01 | 2.80 | 1570 |
| 2024-09-20 22:21:41.250 | MS1 | 121.4656589791 | 31.1446267715 | 843 | 504990 | -91.29 | 10.68 | 521.52 | 0.16 | 2.91 | 1574 |
| 2024-09-20 22:21:42.876 | MS1 | 121.4656667600 | 31.1446301216 | 843 | 504990 | -91.30 | 12.41 | 465.65 | 0.00 | 2.31 | 1593 |

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
| 3232810 | 4 | 121.4693307620 | 31.1510859451 | 120 | 4 | 4 | 24.4 | TDD | 105 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3257959 | 1 | 121.4663848029 | 31.1525126765 | 354 | 10 | 2 | 31.8 | TDD | 929 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3261929 | 3 | 121.4739367364 | 31.1545071790 | 26 | 12 | 5 | 21.6 | TDD | 805 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3278348 | 2 | 121.4750698682 | 31.1524948141 | 180 | 4 | 12 | 32.1 | TDD | 843 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.389 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.504 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.504 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.196 | NREventA3 | measId:2;ServCellPCI:90;Ser... |
| 2024-09-20 22:21:38.436 | NRHandoverAttempt | SourcePCI:90;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.476 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.488 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.620 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.620 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257959 | 1 | 15.1239 | 16.3954 | -116.1672 | 18.0548 | 179.3295 | 0.0074 | 0.0003 |
| 2024_09_20 22:00 | 3278348 | 2 | 80.4756 | 94.0436 | -117.6390 | 16.6777 | 174.5585 | 0.0187 | 0.0060 |
| 2024_09_20 22:00 | 3261929 | 3 | 13.3275 | 9.4239 | -116.2304 | 6.7291 | 187.5161 | 0.0005 | 0.0200 |
| 2024_09_20 22:00 | 3232810 | 4 | 7.7246 | 16.9330 | -114.8000 | 7.0445 | 122.8688 | 0.0142 | 0.0159 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416113_AB94D231 | 504990 | 843 | -88.3 | 504990 | 105 | -93.2 | 504990 | 929 | -99.0 | 504990 | 805 |
| MR_1774416113_F6741FF6 | 504990 | 843 | -91.6 | 504990 | 105 | -92.5 | 504990 | 929 | -98.6 | 504990 | 805 |
| MR_1774416113_742C3E60 | 504990 | 843 | -91.2 | 504990 | 105 | -94.1 | 504990 | 929 | -98.6 | 504990 | 805 |
| MR_1774416113_934E88AA | 504990 | 843 | -90.7 | 504990 | 105 | -93.3 | 504990 | 929 | -98.4 | 504990 | 805 |
| MR_1774416113_1AC5E12B | 504990 | 843 | -89.8 | 504990 | 105 | -93.3 | 504990 | 929 | -99.3 | 504990 | 805 |
| MR_1774416113_DBD10D95 | 504990 | 843 | -89.0 | 504990 | 105 | -91.4 | 504990 | 929 | -97.7 | 504990 | 805 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 742: `c38dc81f-64f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c38dc81f-64f6-49ac-acf5-2a9b6038f213` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Add neighbor relationship between 3246240_1 and 3242244_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[742] topology](images/train_0742.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3246240_1 by 50 degrees
- `C2`: Increase transmission power for 3242244_3
- `C3`: Decrease transmission power for 3242244_3
- `C4`: Check test server and transmission issues
- `C5`: Increase A3 Offset threshold for 3246240_1
- `C6`: Adjust the azimuth of 3242244_3 by 35 degrees
- `C7`: Decrease A3 Offset threshold for 3246240_1
- `C8`: Press down the tilt angle of 3246240_1 by 10 degrees
- `C9`: Lift the tilt angle of 3246240_1 by 10 degrees
- `C10`: Add neighbor relationship between 3246240_1 and 3242244_3 **← 정답**
- `C11`: Lift the tilt angle  of 3242244_3 by 2 degrees
- `C12`: Decrease A3 Offset threshold for 3242244_3
- `C13`: Increase A3 Offset threshold for 3242244_3
- `C14`: Increase transmission power for 3246240_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242244_3
- `C16`: Decrease transmission power for 3246240_1
- `C17`: Add neighbor relationship between 3226355_4 and 3242244_3
- `C18`: Press down the tilt angle  of 3242244_3 by 2 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246240_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242244_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246240_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.115 | MS1 | 121.4656645230 | 31.1446324428 | 465 | 504990 | -83.91 | 14.29 | 398.16 | 0.09 | 2.30 | 1578 |
| 2024-09-20 22:21:32.536 | MS1 | 121.4656632294 | 31.1446262499 | 465 | 504990 | -82.61 | 17.65 | 496.51 | 0.15 | 2.90 | 1562 |
| 2024-09-20 22:21:33.316 | MS1 | 121.4656592102 | 31.1446284941 | 465 | 504990 | -80.48 | 13.74 | 352.87 | 0.17 | 2.56 | 1591 |
| 2024-09-20 22:21:34.995 | MS1 | 121.4656605352 | 31.1446357729 | 465 | 504990 | -88.14 | -1.07 | 71.40 | 0.15 | 1.24 | 1571 |
| 2024-09-20 22:21:35.705 | MS1 | 121.4656614461 | 31.1446269588 | 465 | 504990 | -85.95 | -3.40 | 59.98 | 0.02 | 1.07 | 1561 |
| 2024-09-20 22:21:36.297 | MS1 | 121.4656721098 | 31.1446334525 | 465 | 504990 | -91.55 | -0.10 | 40.87 | 0.03 | 1.20 | 1595 |
| 2024-09-20 22:21:37.186 | MS1 | 121.4656655284 | 31.1446225420 | 465 | 504990 | -91.57 | -3.52 | 33.16 | 0.03 | 1.04 | 1599 |
| 2024-09-20 22:21:38.249 | MS1 | 121.4656733280 | 31.1446276174 | 465 | 504990 | -75.06 | 14.46 | 572.43 | 0.18 | 1.24 | 1578 |
| 2024-09-20 22:21:39.717 | MS1 | 121.4656776396 | 31.1446225956 | 465 | 504990 | -81.95 | 12.10 | 532.39 | 0.14 | 1.45 | 1585 |
| 2024-09-20 22:21:40.837 | MS1 | 121.4656614793 | 31.1446357339 | 465 | 504990 | -83.68 | 15.00 | 580.35 | 0.20 | 2.34 | 1600 |
| 2024-09-20 22:21:41.274 | MS1 | 121.4656649881 | 31.1446267234 | 465 | 504990 | -83.29 | 15.65 | 576.69 | 0.19 | 2.73 | 1587 |
| 2024-09-20 22:21:42.547 | MS1 | 121.4656749153 | 31.1446336498 | 465 | 504990 | -82.17 | 17.10 | 451.61 | 0.12 | 2.12 | 1568 |

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
| 3226355 | 4 | 121.4750253934 | 31.1517936994 | 236 | 0 | 1 | 33.9 | TDD | 239 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3242244 | 3 | 121.4744639469 | 31.1457886896 | 226 | 1 | 3 | 15.3 | TDD | 38 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3246240 | 1 | 121.4735749499 | 31.1445345706 | 16 | 13 | 0 | 18.6 | TDD | 465 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3247239 | 2 | 121.4681188485 | 31.1471945153 | 136 | 2 | 0 | 17.0 | TDD | 941 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.136 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.160 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.275 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.275 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.000 | NREventA3 | measId:2;ServCellPCI:769;Se... |
| 2024-09-20 22:21:36.000 | NREventA3 | measId:2;ServCellPCI:769;Se... |
| 2024-09-20 22:21:37.000 | NREventA3 | measId:2;ServCellPCI:769;Se... |
| 2024-09-20 22:21:39.500 | NRRRCReestablishAttempt | PCI:769 |
| 2024-09-20 22:21:39.517 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.531 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.666 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.666 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246240 | 1 | 12.4093 | 9.8734 | -117.2848 | 11.5228 | 120.0362 | 0.0043 | 0.1817 |
| 2024_09_20 22:00 | 3247239 | 2 | 8.5799 | 11.9342 | -117.2860 | 5.2034 | 188.1327 | 0.0011 | 0.0102 |
| 2024_09_20 22:00 | 3242244 | 3 | 10.7799 | 5.5492 | -115.1213 | 13.2770 | 88.1023 | 0.0032 | 0.0189 |
| 2024_09_20 22:00 | 3226355 | 4 | 10.5732 | 17.0063 | -116.2878 | 5.5514 | 146.8623 | 0.0151 | 0.0138 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415390_E9DDDD30 | 504990 | 465 | -87.5 | 504990 | 38 | -85.0 | 504990 | 239 | -89.7 | 504990 | 941 |
| MR_1774415390_8D8EC51C | 504990 | 465 | -90.1 | 504990 | 38 | -82.1 | 504990 | 239 | -90.1 | 504990 | 941 |
| MR_1774415390_35ED4C3B | 504990 | 38 | -81.7 | 504990 | 465 | -90.0 | 504990 | 239 | -90.1 | 504990 | 941 |
| MR_1774415390_F0B9D188 | 504990 | 38 | -84.7 | 504990 | 465 | -87.9 | 504990 | 239 | -92.1 | 504990 | 941 |
| MR_1774415390_F092F3A4 | 504990 | 465 | -87.5 | 504990 | 38 | -84.2 | 504990 | 239 | -90.5 | 504990 | 941 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 743: `37745902-9ef...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `37745902-9ef2-4610-8f1f-ee0c24e71403` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[743] topology](images/train_0743.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3233818_2 by 8 degrees
- `C2`: Insufficient data; more data is needed for judgment. **← 정답**
- `C3`: Decrease transmission power for 3219029_3
- `C4`: Increase transmission power for 3219029_3
- `C5`: Decrease A3 Offset threshold for 3233818_2
- `C6`: Check test server and transmission issues
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219029_3
- `C8`: Increase A3 Offset threshold for 3233818_2
- `C9`: Increase transmission power for 3233818_2
- `C10`: Press down the tilt angle of 3219029_3 by 10 degrees
- `C11`: Increase A3 Offset threshold for 3219029_3
- `C12`: Add neighbor relationship between 3219029_3 and 3233818_2
- `C13`: Lift the tilt angle of 3219029_3 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219029_3
- `C15`: Press down the tilt angle  of 3233818_2 by 8 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233818_2
- `C17`: Add neighbor relationship between 3276316_1 and 3233818_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233818_2
- `C19`: Adjust the azimuth of 3233818_2 by 18 degrees
- `C20`: Adjust the azimuth of 3219029_3 by 50 degrees
- `C21`: Decrease A3 Offset threshold for 3219029_3
- `C22`: Decrease transmission power for 3233818_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.498 | MS1 | 121.4656711687 | 31.1446268509 | 794 | 504990 | -91.39 | 12.22 | 525.78 | 0.03 | 2.65 | 1581 |
| 2024-09-20 22:21:32.364 | MS1 | 121.4656664706 | 31.1446374812 | 794 | 504990 | -87.69 | 13.78 | 587.97 | 0.06 | 2.20 | 1578 |
| 2024-09-20 22:21:33.682 | MS1 | 121.4656649959 | 31.1446212144 | 794 | 504990 | -88.84 | 17.46 | 552.58 | 0.10 | 2.29 | 1564 |
| 2024-09-20 22:21:34.411 | MS1 | 121.4656668940 | 31.1446266501 | 794 | 504990 | -86.30 | 17.10 | 64.40 | 0.19 | 2.86 | 1572 |
| 2024-09-20 22:21:35.618 | MS1 | 121.4656611537 | 31.1446236422 | 794 | 504990 | -85.04 | 13.89 | 80.34 | 0.19 | 2.60 | 1571 |
| 2024-09-20 22:21:36.401 | MS1 | 121.4656641396 | 31.1446300405 | 794 | 504990 | -85.24 | 15.98 | 91.81 | 0.15 | 2.81 | 1576 |
| 2024-09-20 22:21:37.152 | MS1 | 121.4656728696 | 31.1446271579 | 794 | 504990 | -90.87 | 7.82 | 65.13 | 0.09 | 2.48 | 1582 |
| 2024-09-20 22:21:38.863 | MS1 | 121.4656588422 | 31.1446182117 | 794 | 504990 | -92.76 | 7.09 | 45.38 | 0.18 | 2.80 | 1578 |
| 2024-09-20 22:21:39.319 | MS1 | 121.4656622872 | 31.1446327416 | 794 | 504990 | -93.03 | 9.09 | 86.89 | 0.08 | 2.32 | 1564 |
| 2024-09-20 22:21:40.586 | MS1 | 121.4656628149 | 31.1446258525 | 794 | 504990 | -90.21 | 12.11 | 309.09 | 0.06 | 2.85 | 1584 |
| 2024-09-20 22:21:41.576 | MS1 | 121.4656650099 | 31.1446267400 | 794 | 504990 | -92.77 | 8.99 | 302.99 | 0.11 | 2.13 | 1572 |
| 2024-09-20 22:21:42.871 | MS1 | 121.4656725268 | 31.1446336051 | 794 | 504990 | -92.21 | 10.60 | 329.27 | 0.13 | 2.40 | 1560 |

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
| 3219029 | 3 | 121.4694904596 | 31.1528617413 | 138 | 9 | 4 | 18.2 | TDD | 794 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3232436 | 4 | 121.4681203204 | 31.1494462245 | 306 | 11 | 3 | 34.3 | TDD | 380 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3233818 | 2 | 121.4711520701 | 31.1471970619 | 259 | 5 | 10 | 27.5 | TDD | 970 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3276316 | 1 | 121.4687119688 | 31.1490755388 | 167 | 7 | 11 | 40.9 | TDD | 233 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.105 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.129 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.232 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.232 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.919 | NREventA3 | measId:2;ServCellPCI:971;Se... |
| 2024-09-20 22:21:38.159 | NRHandoverAttempt | SourcePCI:971;SourceNR-ARFC... |
| 2024-09-20 22:21:38.201 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.211 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.352 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.352 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3276316 | 1 | 86.5032 | 87.4154 | -115.9111 | 13.6023 | 147.4226 | 0.0125 | 0.0094 |
| 2024_09_19 22:00 | 3233818 | 2 | 90.4250 | 94.3189 | -116.0669 | 16.2512 | 185.7429 | 0.0155 | 0.0102 |
| 2024_09_19 22:00 | 3219029 | 3 | 88.9762 | 86.8682 | -114.7014 | 19.1800 | 102.0958 | 0.0027 | 0.0022 |
| 2024_09_19 22:00 | 3232436 | 4 | 87.7229 | 93.2561 | -116.8977 | 8.8686 | 136.2582 | 0.0106 | 0.0169 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414948_681BEA84 | 504990 | 794 | -84.9 | 504990 | 970 | -87.8 | 504990 | 233 | -98.3 | 504990 | 380 |
| MR_1774414948_77ED41B3 | 504990 | 794 | -86.0 | 504990 | 970 | -90.4 | 504990 | 233 | -96.2 | 504990 | 380 |
| MR_1774414948_187A1754 | 504990 | 794 | -85.5 | 504990 | 970 | -90.9 | 504990 | 233 | -96.6 | 504990 | 380 |
| MR_1774414948_89CA6A64 | 504990 | 794 | -87.0 | 504990 | 970 | -90.8 | 504990 | 233 | -97.9 | 504990 | 380 |
| MR_1774414948_E7E9E5EA | 504990 | 794 | -85.8 | 504990 | 970 | -88.5 | 504990 | 233 | -95.1 | 504990 | 380 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 744: `48371fec-0c6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `48371fec-0c6f-407b-ac42-d29e54400a99` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[744] topology](images/train_0744.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3245270_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245270_1
- `C3`: Insufficient data; more data is needed for judgment. **← 정답**
- `C4`: Add neighbor relationship between 3220885_4 and 3237932_2
- `C5`: Adjust the azimuth of 3237932_2 by 50 degrees
- `C6`: Check test server and transmission issues
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237932_2
- `C8`: Increase transmission power for 3245270_1
- `C9`: Decrease transmission power for 3237932_2
- `C10`: Adjust the azimuth of 3245270_1 by 50 degrees
- `C11`: Press down the tilt angle of 3245270_1 by 10 degrees
- `C12`: Lift the tilt angle of 3245270_1 by 10 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245270_1
- `C14`: Decrease transmission power for 3245270_1
- `C15`: Increase A3 Offset threshold for 3245270_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237932_2
- `C17`: Decrease A3 Offset threshold for 3237932_2
- `C18`: Lift the tilt angle  of 3237932_2 by 4 degrees
- `C19`: Increase transmission power for 3237932_2
- `C20`: Press down the tilt angle  of 3237932_2 by 4 degrees
- `C21`: Increase A3 Offset threshold for 3237932_2
- `C22`: Add neighbor relationship between 3245270_1 and 3237932_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.129 | MS1 | 121.4656728118 | 31.1446250746 | 785 | 504990 | -91.24 | 13.45 | 419.81 | 0.09 | 2.23 | 1560 |
| 2024-09-20 22:21:32.970 | MS1 | 121.4656662453 | 31.1446184180 | 785 | 504990 | -90.04 | 15.13 | 395.69 | 0.19 | 2.47 | 1563 |
| 2024-09-20 22:21:33.522 | MS1 | 121.4656769286 | 31.1446187012 | 785 | 504990 | -85.21 | 15.80 | 484.29 | 0.12 | 2.54 | 1566 |
| 2024-09-20 22:21:34.302 | MS1 | 121.4656662426 | 31.1446200809 | 785 | 504990 | -89.46 | 15.77 | 60.33 | 0.19 | 2.32 | 1591 |
| 2024-09-20 22:21:35.760 | MS1 | 121.4656602435 | 31.1446292855 | 785 | 504990 | -87.63 | 13.28 | 73.55 | 0.19 | 2.46 | 1563 |
| 2024-09-20 22:21:36.546 | MS1 | 121.4656731071 | 31.1446353260 | 785 | 504990 | -86.04 | 16.00 | 64.72 | 0.19 | 2.70 | 1569 |
| 2024-09-20 22:21:37.312 | MS1 | 121.4656736400 | 31.1446188641 | 785 | 504990 | -91.77 | 10.48 | 66.74 | 0.19 | 2.84 | 1563 |
| 2024-09-20 22:21:38.375 | MS1 | 121.4656635758 | 31.1446227043 | 785 | 504990 | -93.16 | 11.13 | 49.07 | 0.06 | 2.13 | 1567 |
| 2024-09-20 22:21:39.172 | MS1 | 121.4656752826 | 31.1446323425 | 785 | 504990 | -90.73 | 9.03 | 57.91 | 0.04 | 2.64 | 1600 |
| 2024-09-20 22:21:40.409 | MS1 | 121.4656770403 | 31.1446376836 | 785 | 504990 | -93.62 | 7.22 | 421.74 | 0.02 | 2.94 | 1579 |
| 2024-09-20 22:21:41.688 | MS1 | 121.4656628091 | 31.1446329218 | 785 | 504990 | -90.54 | 8.72 | 329.73 | 0.04 | 2.31 | 1562 |
| 2024-09-20 22:21:42.768 | MS1 | 121.4656688394 | 31.1446206251 | 785 | 504990 | -91.76 | 12.84 | 354.73 | 0.14 | 2.32 | 1568 |

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
| 3220885 | 4 | 121.4743507873 | 31.1479341462 | 210 | 4 | 2 | 44.4 | TDD | 617 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3237556 | 3 | 121.4664546369 | 31.1470646730 | 298 | 10 | 8 | 48.6 | TDD | 513 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3237932 | 2 | 121.4724602462 | 31.1500531728 | 310 | 2 | 6 | 26.8 | TDD | 383 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3245270 | 1 | 121.4663466195 | 31.1479291947 | 64 | 8 | 4 | 28.5 | TDD | 785 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.962 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.979 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.108 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.108 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.846 | NREventA3 | measId:2;ServCellPCI:470;Se... |
| 2024-09-20 22:21:38.086 | NRHandoverAttempt | SourcePCI:470;SourceNR-ARFC... |
| 2024-09-20 22:21:38.126 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.141 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.287 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.287 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3245270 | 1 | 89.7149 | 90.4405 | -116.8937 | 5.4635 | 198.4297 | 0.0150 | 0.0100 |
| 2024_09_19 22:00 | 3237932 | 2 | 87.8084 | 84.1344 | -117.4123 | 10.5687 | 166.7264 | 0.0018 | 0.0096 |
| 2024_09_19 22:00 | 3237556 | 3 | 75.5015 | 75.2062 | -114.9828 | 15.6195 | 88.1387 | 0.0117 | 0.0009 |
| 2024_09_19 22:00 | 3220885 | 4 | 93.6257 | 82.1436 | -116.5986 | 9.8449 | 153.2910 | 0.0124 | 0.0169 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414267_658A69FD | 504990 | 785 | -88.8 | 504990 | 383 | -94.0 | 504990 | 617 | -99.2 | 504990 | 513 |
| MR_1774414267_4BCCC855 | 504990 | 785 | -91.0 | 504990 | 383 | -96.1 | 504990 | 617 | -100.6 | 504990 | 513 |
| MR_1774414267_12691E00 | 504990 | 785 | -89.1 | 504990 | 383 | -93.0 | 504990 | 617 | -98.0 | 504990 | 513 |
| MR_1774414267_9ED3BC7B | 504990 | 785 | -88.6 | 504990 | 383 | -94.8 | 504990 | 617 | -98.7 | 504990 | 513 |
| MR_1774414267_80208D63 | 504990 | 785 | -89.6 | 504990 | 383 | -93.2 | 504990 | 617 | -97.6 | 504990 | 513 |
| MR_1774414267_B05A17EE | 504990 | 785 | -89.6 | 504990 | 383 | -94.4 | 504990 | 617 | -100.2 | 504990 | 513 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 745: `1511bef9-87c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1511bef9-87c3-4669-a74e-d2c68f00a498` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[745] topology](images/train_0745.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3266490_4 and 3267781_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266490_4
- `C3`: Lift the tilt angle  of 3267781_1 by 5 degrees
- `C4`: Decrease A3 Offset threshold for 3267781_1
- `C5`: Press down the tilt angle of 3266490_4 by 6 degrees
- `C6`: Adjust the azimuth of 3267781_1 by 50 degrees
- `C7`: Press down the tilt angle  of 3267781_1 by 5 degrees
- `C8`: Decrease transmission power for 3266490_4
- `C9`: Lift the tilt angle of 3266490_4 by 6 degrees
- `C10`: Increase transmission power for 3266490_4
- `C11`: Adjust the azimuth of 3266490_4 by 50 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266490_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267781_1
- `C14`: Increase A3 Offset threshold for 3267781_1
- `C15`: Add neighbor relationship between 3221209_3 and 3267781_1
- `C16`: Decrease transmission power for 3267781_1
- `C17`: Increase A3 Offset threshold for 3266490_4
- `C18`: Insufficient data; more data is needed for judgment. **← 정답**
- `C19`: Check test server and transmission issues
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267781_1
- `C21`: Increase transmission power for 3267781_1
- `C22`: Decrease A3 Offset threshold for 3266490_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.178 | MS1 | 121.4656678454 | 31.1446283006 | 647 | 504990 | -91.47 | 13.03 | 597.03 | 0.15 | 2.78 | 1573 |
| 2024-09-20 22:21:32.653 | MS1 | 121.4656759965 | 31.1446187763 | 647 | 504990 | -89.77 | 17.02 | 448.03 | 0.06 | 2.40 | 1578 |
| 2024-09-20 22:21:33.424 | MS1 | 121.4656734062 | 31.1446244595 | 647 | 504990 | -91.20 | 15.74 | 489.39 | 0.01 | 2.81 | 1561 |
| 2024-09-20 22:21:34.301 | MS1 | 121.4656656591 | 31.1446320047 | 647 | 504990 | -88.29 | 13.28 | 47.59 | 0.01 | 2.54 | 1581 |
| 2024-09-20 22:21:35.732 | MS1 | 121.4656730912 | 31.1446358846 | 647 | 504990 | -87.80 | 13.00 | 70.75 | 0.13 | 2.63 | 1591 |
| 2024-09-20 22:21:36.537 | MS1 | 121.4656609028 | 31.1446347725 | 647 | 504990 | -91.58 | 14.63 | 71.28 | 0.09 | 2.76 | 1595 |
| 2024-09-20 22:21:37.638 | MS1 | 121.4656709558 | 31.1446312522 | 647 | 504990 | -89.17 | 12.02 | 62.69 | 0.14 | 2.27 | 1563 |
| 2024-09-20 22:21:38.941 | MS1 | 121.4656762789 | 31.1446275300 | 647 | 504990 | -92.67 | 7.64 | 98.77 | 0.04 | 2.02 | 1568 |
| 2024-09-20 22:21:39.995 | MS1 | 121.4656747042 | 31.1446240618 | 647 | 504990 | -91.79 | 7.88 | 92.19 | 0.11 | 2.53 | 1560 |
| 2024-09-20 22:21:40.661 | MS1 | 121.4656626655 | 31.1446255649 | 647 | 504990 | -91.08 | 9.17 | 439.17 | 0.19 | 2.54 | 1578 |
| 2024-09-20 22:21:41.885 | MS1 | 121.4656604473 | 31.1446372961 | 647 | 504990 | -91.99 | 9.41 | 502.20 | 0.12 | 2.46 | 1565 |
| 2024-09-20 22:21:42.559 | MS1 | 121.4656732530 | 31.1446302558 | 647 | 504990 | -91.22 | 10.73 | 448.95 | 0.13 | 2.12 | 1599 |

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
| 3221209 | 3 | 121.4710979786 | 31.1480005240 | 253 | 14 | 11 | 42.4 | TDD | 702 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3231364 | 2 | 121.4716182795 | 31.1525725683 | 340 | 14 | 9 | 46.2 | TDD | 661 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3266490 | 4 | 121.4700656047 | 31.1538491378 | 292 | 5 | 0 | 26.4 | TDD | 647 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3267781 | 1 | 121.4719114749 | 31.1549247504 | 12 | 3 | 9 | 42.2 | TDD | 44 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.828 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.845 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.957 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.957 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.700 | NREventA3 | measId:2;ServCellPCI:638;Se... |
| 2024-09-20 22:21:37.940 | NRHandoverAttempt | SourcePCI:638;SourceNR-ARFC... |
| 2024-09-20 22:21:37.972 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.983 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.128 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.128 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3267781 | 1 | 75.3398 | 81.7105 | -116.2720 | 7.7419 | 137.9225 | 0.0194 | 0.0089 |
| 2024_09_19 22:00 | 3231364 | 2 | 77.1777 | 85.7476 | -117.0404 | 13.5045 | 82.8870 | 0.0181 | 0.0187 |
| 2024_09_19 22:00 | 3221209 | 3 | 77.1078 | 76.5708 | -115.4873 | 14.3749 | 179.9746 | 0.0054 | 0.0181 |
| 2024_09_19 22:00 | 3266490 | 4 | 78.5395 | 76.5760 | -116.5499 | 8.0104 | 193.8829 | 0.0102 | 0.0037 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415208_07B77926 | 504990 | 647 | -89.9 | 504990 | 44 | -92.0 | 504990 | 702 | -94.5 | 504990 | 661 |
| MR_1774415208_1AF86078 | 504990 | 647 | -89.2 | 504990 | 44 | -90.5 | 504990 | 702 | -96.5 | 504990 | 661 |
| MR_1774415208_E8099AC5 | 504990 | 647 | -87.5 | 504990 | 44 | -90.8 | 504990 | 702 | -95.2 | 504990 | 661 |
| MR_1774415208_BF403403 | 504990 | 647 | -86.9 | 504990 | 44 | -90.2 | 504990 | 702 | -96.6 | 504990 | 661 |
| MR_1774415208_E7056368 | 504990 | 647 | -89.0 | 504990 | 44 | -92.1 | 504990 | 702 | -95.8 | 504990 | 661 |
| MR_1774415208_ADCEB7F8 | 504990 | 647 | -87.9 | 504990 | 44 | -90.6 | 504990 | 702 | -95.7 | 504990 | 661 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 746: `3281b6fa-2d6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3281b6fa-2d6b-4141-8739-d1e151903728` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Add neighbor relationship between 3265760_1 and 3212602_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[746] topology](images/train_0746.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase transmission power for 3212602_2
- `C3`: Lift the tilt angle  of 3212602_2 by 2 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212602_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265760_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212602_2
- `C7`: Decrease transmission power for 3212602_2
- `C8`: Decrease transmission power for 3265760_1
- `C9`: Check test server and transmission issues
- `C10`: Press down the tilt angle  of 3212602_2 by 2 degrees
- `C11`: Add neighbor relationship between 3265760_1 and 3212602_2 **← 정답**
- `C12`: Press down the tilt angle of 3265760_1 by 10 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265760_1
- `C14`: Adjust the azimuth of 3212602_2 by 42 degrees
- `C15`: Increase A3 Offset threshold for 3265760_1
- `C16`: Adjust the azimuth of 3265760_1 by 50 degrees
- `C17`: Lift the tilt angle of 3265760_1 by 10 degrees
- `C18`: Increase transmission power for 3265760_1
- `C19`: Decrease A3 Offset threshold for 3265760_1
- `C20`: Add neighbor relationship between 3223948_4 and 3212602_2
- `C21`: Increase A3 Offset threshold for 3212602_2
- `C22`: Decrease A3 Offset threshold for 3212602_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.891 | MS1 | 121.4656624074 | 31.1446312762 | 136 | 504990 | -80.36 | 14.02 | 604.53 | 0.04 | 2.02 | 1592 |
| 2024-09-20 22:21:32.732 | MS1 | 121.4656675192 | 31.1446202793 | 136 | 504990 | -81.26 | 16.33 | 296.01 | 0.03 | 2.30 | 1584 |
| 2024-09-20 22:21:33.240 | MS1 | 121.4656751037 | 31.1446241513 | 136 | 504990 | -82.71 | 16.37 | 350.02 | 0.13 | 2.89 | 1579 |
| 2024-09-20 22:21:34.432 | MS1 | 121.4656779604 | 31.1446225658 | 136 | 504990 | -87.15 | -0.03 | 59.06 | 0.02 | 1.12 | 1600 |
| 2024-09-20 22:21:35.986 | MS1 | 121.4656648640 | 31.1446360762 | 136 | 504990 | -93.38 | -1.70 | 48.16 | 0.04 | 1.42 | 1573 |
| 2024-09-20 22:21:36.617 | MS1 | 121.4656743899 | 31.1446276096 | 136 | 504990 | -86.49 | -0.63 | 60.10 | 0.20 | 1.29 | 1591 |
| 2024-09-20 22:21:37.328 | MS1 | 121.4656759978 | 31.1446227980 | 136 | 504990 | -91.10 | -1.86 | 33.63 | 0.01 | 1.31 | 1575 |
| 2024-09-20 22:21:38.807 | MS1 | 121.4656619057 | 31.1446290574 | 136 | 504990 | -80.60 | 17.66 | 421.56 | 0.15 | 1.33 | 1590 |
| 2024-09-20 22:21:39.600 | MS1 | 121.4656685398 | 31.1446246281 | 136 | 504990 | -79.41 | 17.54 | 487.27 | 0.19 | 1.22 | 1576 |
| 2024-09-20 22:21:40.494 | MS1 | 121.4656739553 | 31.1446210119 | 136 | 504990 | -82.06 | 16.98 | 440.07 | 0.04 | 2.25 | 1573 |
| 2024-09-20 22:21:41.221 | MS1 | 121.4656767415 | 31.1446220409 | 136 | 504990 | -76.16 | 15.68 | 352.45 | 0.17 | 2.43 | 1581 |
| 2024-09-20 22:21:42.406 | MS1 | 121.4656583262 | 31.1446205964 | 136 | 504990 | -84.04 | 15.60 | 420.04 | 0.06 | 2.32 | 1578 |

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
| 3212602 | 2 | 121.4752639146 | 31.1483190545 | 288 | 0 | 12 | 30.2 | TDD | 116 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3223948 | 4 | 121.4734471927 | 31.1483721156 | 177 | 12 | 9 | 32.2 | TDD | 231 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3225892 | 3 | 121.4640704879 | 31.1549916762 | 130 | 4 | 11 | 25.0 | TDD | 566 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3265760 | 1 | 121.4708806960 | 31.1479445370 | 65 | 8 | 10 | 48.4 | TDD | 136 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.033 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.048 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.149 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.149 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.886 | NREventA3 | measId:2;ServCellPCI:92;Ser... |
| 2024-09-20 22:21:35.886 | NREventA3 | measId:2;ServCellPCI:92;Ser... |
| 2024-09-20 22:21:36.886 | NREventA3 | measId:2;ServCellPCI:92;Ser... |
| 2024-09-20 22:21:39.386 | NRRRCReestablishAttempt | PCI:92 |
| 2024-09-20 22:21:39.402 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.413 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.543 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.543 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265760 | 1 | 9.3119 | 6.1550 | -114.1006 | 14.3595 | 103.6481 | 0.0027 | 0.1734 |
| 2024_09_20 22:00 | 3212602 | 2 | 19.2709 | 10.6369 | -117.8235 | 17.5426 | 118.1082 | 0.0122 | 0.0047 |
| 2024_09_20 22:00 | 3225892 | 3 | 7.6325 | 5.1795 | -115.1140 | 18.6505 | 185.2076 | 0.0115 | 0.0154 |
| 2024_09_20 22:00 | 3223948 | 4 | 16.1049 | 19.7483 | -114.2413 | 16.2817 | 146.1442 | 0.0038 | 0.0181 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416555_6471C6AE | 504990 | 116 | -80.5 | 504990 | 136 | -88.2 | 504990 | 231 | -82.3 | 504990 | 566 |
| MR_1774416555_6915BF26 | 504990 | 136 | -86.6 | 504990 | 116 | -83.0 | 504990 | 231 | -83.3 | 504990 | 566 |
| MR_1774416555_33A8C77E | 504990 | 136 | -86.4 | 504990 | 116 | -83.9 | 504990 | 231 | -81.6 | 504990 | 566 |
| MR_1774416555_64D9061E | 504990 | 136 | -85.6 | 504990 | 116 | -81.5 | 504990 | 231 | -83.4 | 504990 | 566 |
| MR_1774416555_66A56782 | 504990 | 136 | -86.9 | 504990 | 116 | -82.0 | 504990 | 231 | -84.5 | 504990 | 566 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 747: `721f7718-154...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `721f7718-1548-46ae-b009-61cc5683280d` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278189_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[747] topology](images/train_0747.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3221760_1 by 6 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278189_5 **← 정답**
- `C3`: Add neighbor relationship between 3278189_5 and 3221760_1
- `C4`: Adjust the azimuth of 3278189_5 by 43 degrees
- `C5`: Increase A3 Offset threshold for 3278189_5
- `C6`: Check test server and transmission issues
- `C7`: Adjust the azimuth of 3221760_1 by 37 degrees
- `C8`: Add neighbor relationship between 3258271_11 and 3221760_1
- `C9`: Decrease A3 Offset threshold for 3278189_5
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221760_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease transmission power for 3221760_1
- `C13`: Press down the tilt angle of 3278189_5 by 6 degrees
- `C14`: Increase transmission power for 3278189_5
- `C15`: Lift the tilt angle of 3278189_5 by 6 degrees
- `C16`: Decrease transmission power for 3278189_5
- `C17`: Decrease A3 Offset threshold for 3221760_1
- `C18`: Increase A3 Offset threshold for 3221760_1
- `C19`: Lift the tilt angle  of 3221760_1 by 6 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278189_5
- `C21`: Increase transmission power for 3221760_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221760_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.329 | MS1 | 121.4656636065 | 31.1446255761 | 272 | 504990 | -95.59 | 12.64 | 386.69 | 0.19 | 2.55 | 1569 |
| 2024-09-20 22:21:32.551 | MS1 | 121.4656690489 | 31.1446249173 | 718 | 504990 | -95.97 | 11.22 | 369.44 | 0.04 | 2.59 | 1564 |
| 2024-09-20 22:21:33.808 | MS1 | 121.4656760478 | 31.1446262173 | 398 | 504990 | -93.55 | 13.74 | 598.00 | 0.07 | 2.65 | 1573 |
| 2024-09-20 22:21:34.247 | MS1 | 121.4656747876 | 31.1446312640 | 714 | 152650 | -90.35 | 2.96 | 51.57 | 0.17 | 1.89 | 936 |
| 2024-09-20 22:21:35.201 | MS1 | 121.4656682537 | 31.1446255075 | 213 | 152650 | -89.58 | 5.31 | 51.83 | 0.06 | 1.80 | 910 |
| 2024-09-20 22:21:36.858 | MS1 | 121.4656604417 | 31.1446352563 | 211 | 152650 | -94.00 | 4.36 | 63.06 | 0.16 | 1.64 | 939 |
| 2024-09-20 22:21:37.282 | MS1 | 121.4656749009 | 31.1446341767 | 739 | 152650 | -94.36 | 4.55 | 61.27 | 0.07 | 1.91 | 979 |
| 2024-09-20 22:21:38.417 | MS1 | 121.4656760865 | 31.1446315765 | 714 | 152650 | -89.84 | 4.15 | 86.11 | 0.02 | 1.77 | 940 |
| 2024-09-20 22:21:39.845 | MS1 | 121.4656715723 | 31.1446329978 | 213 | 152650 | -90.59 | 6.16 | 92.51 | 0.05 | 1.92 | 967 |
| 2024-09-20 22:21:40.355 | MS1 | 121.4656614349 | 31.1446234237 | 211 | 152650 | -91.72 | 5.29 | 73.03 | 0.11 | 2.15 | 1565 |
| 2024-09-20 22:21:41.543 | MS1 | 121.4656580646 | 31.1446274611 | 739 | 152650 | -94.05 | 5.79 | 81.79 | 0.20 | 2.90 | 1572 |
| 2024-09-20 22:21:42.853 | MS1 | 121.4656770818 | 31.1446212100 | 714 | 152650 | -88.18 | 5.05 | 70.08 | 0.17 | 2.34 | 1600 |

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
| 3212007 | 9 | 121.4753376897 | 31.1497653408 | 349 | 3 | 1 | 5.0 | FDD | 812 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3221760 | 1 | 121.4742081444 | 31.1549892409 | 178 | 5 | 11 | 18.1 | TDD | 96 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3224655 | 10 | 121.4734274805 | 31.1497194570 | 177 | 6 | 11 | 16.7 | FDD | 911 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3234025 | 7 | 121.4712272795 | 31.1475168557 | 57 | 1 | 1 | 18.2 | FDD | 739 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3235339 | 12 | 121.4644863949 | 31.1477000975 | 353 | 10 | 3 | 3.9 | FDD | 148 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3236255 | 4 | 121.4667624300 | 31.1545563254 | 37 | 2 | 12 | 12.5 | TDD | 718 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3243473 | 2 | 121.4718749339 | 31.1492604799 | 246 | 5 | 5 | 7.3 | TDD | 448 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3258271 | 11 | 121.4690249999 | 31.1456860361 | 279 | 1 | 8 | 7.3 | FDD | 211 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3265569 | 3 | 121.4651202477 | 31.1463713463 | 264 | 9 | 9 | 10.9 | TDD | 398 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3265907 | 6 | 121.4755861462 | 31.1559081697 | 214 | 10 | 1 | 8.0 | TDD | 255 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3269365 | 8 | 121.4659451305 | 31.1551734763 | 211 | 8 | 10 | 22.1 | FDD | 714 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3272796 | 13 | 121.4733187853 | 31.1455065093 | 161 | 9 | 11 | 11.3 | FDD | 213 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3278189 | 5 | 121.4688543461 | 31.1481812306 | 174 | 4 | 12 | 16.7 | TDD | 272 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.885 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.902 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.005 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.005 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.785 | NREventA2 | measId:1;ServCellPCI:537;Se... |
| 2024-09-20 22:21:34.930 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.183 | NREventA5 | measId:3;ServCellPCI:537;Se... |
| 2024-09-20 22:21:35.244 | NRHandoverAttempt | SourcePCI:537;SourceNR-ARFC... |
| 2024-09-20 22:21:35.293 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.304 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.437 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.437 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221760 | 1 | 6.3999 | 6.8653 | -114.3974 | 15.4445 | 166.5125 | 0.0156 | 0.0139 |
| 2024_09_20 22:00 | 3243473 | 2 | 16.2512 | 17.7134 | -115.3257 | 16.1250 | 138.8269 | 0.0050 | 0.0143 |
| 2024_09_20 22:00 | 3265569 | 3 | 9.4324 | 16.8366 | -116.7472 | 15.2907 | 128.8031 | 0.0076 | 0.0114 |
| 2024_09_20 22:00 | 3236255 | 4 | 10.7064 | 9.9690 | -117.1431 | 9.8209 | 163.0552 | 0.0187 | 0.0139 |
| 2024_09_20 22:00 | 3278189 | 5 | 18.5424 | 8.3311 | -116.9849 | 6.4979 | 183.1644 | 0.0040 | 0.0139 |
| 2024_09_20 22:00 | 3265907 | 6 | 13.1960 | 10.2606 | -114.5844 | 10.0111 | 178.5535 | 0.0135 | 0.0163 |
| 2024_09_20 22:00 | 3234025 | 7 | 19.7607 | 18.4884 | -116.1874 | 4.0645 | 27.3282 | 0.0122 | 0.0132 |
| 2024_09_20 22:00 | 3269365 | 8 | 11.1936 | 16.7448 | -115.4818 | 3.9347 | 46.2604 | 0.0125 | 0.0160 |
| 2024_09_20 22:00 | 3212007 | 9 | 8.8162 | 19.9520 | -116.2185 | 4.3035 | 36.7730 | 0.0111 | 0.0146 |
| 2024_09_20 22:00 | 3224655 | 10 | 10.2827 | 15.5311 | -115.1384 | 3.4833 | 54.2054 | 0.0060 | 0.0027 |
| 2024_09_20 22:00 | 3258271 | 11 | 8.7503 | 18.7164 | -115.0934 | 4.3500 | 49.6447 | 0.0038 | 0.0132 |
| 2024_09_20 22:00 | 3235339 | 12 | 18.3701 | 17.0398 | -116.5707 | 3.4694 | 28.6699 | 0.0060 | 0.0003 |
| 2024_09_20 22:00 | 3272796 | 13 | 5.3366 | 10.6536 | -114.2378 | 4.9546 | 48.5867 | 0.0027 | 0.0043 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414466_48CECC47 | 504990 | 398 | -93.5 | 504990 | 96 | -93.5 | 504990 | 255 | -102.2 | 504990 | 448 |
| MR_1774414466_4974A44C | 152650 | 714 | -89.5 | 152650 | 812 | -99.3 | 152650 | 148 | -101.6 | 152650 | 911 |
| MR_1774414466_1EB61384 | 152650 | 714 | -91.4 | 152650 | 812 | -97.6 | 152650 | 148 | -100.2 | 152650 | 911 |
| MR_1774414466_A21778C3 | 504990 | 398 | -91.9 | 504990 | 96 | -95.1 | 504990 | 255 | -100.2 | 504990 | 448 |
| MR_1774414466_CB859514 | 504990 | 398 | -91.9 | 504990 | 96 | -95.3 | 504990 | 255 | -100.6 | 504990 | 448 |
| MR_1774414466_CBA144F9 | 152650 | 714 | -89.8 | 152650 | 812 | -96.5 | 152650 | 148 | -103.1 | 152650 | 911 |
| MR_1774414466_C54B457E | 152650 | 714 | -91.3 | 152650 | 812 | -98.6 | 152650 | 148 | -102.1 | 152650 | 911 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 748: `8e7392fe-56a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8e7392fe-56a6-417c-9777-409a9b47ffd5` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[748] topology](images/train_0748.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3270699_1 and 3245596_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245596_3
- `C3`: Decrease A3 Offset threshold for 3245596_3
- `C4`: Increase transmission power for 3245596_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278412_2
- `C6`: Press down the tilt angle  of 3245596_3 by 1 degrees
- `C7`: Decrease transmission power for 3278412_2
- `C8`: Increase A3 Offset threshold for 3245596_3
- `C9`: Lift the tilt angle  of 3245596_3 by 1 degrees
- `C10`: Increase transmission power for 3278412_2
- `C11`: Check test server and transmission issues
- `C12`: Add neighbor relationship between 3278412_2 and 3245596_3
- `C13`: Adjust the azimuth of 3245596_3 by 32 degrees
- `C14`: Lift the tilt angle of 3278412_2 by 5 degrees
- `C15`: Press down the tilt angle of 3278412_2 by 5 degrees
- `C16`: Decrease A3 Offset threshold for 3278412_2
- `C17`: Insufficient data; more data is needed for judgment. **← 정답**
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278412_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245596_3
- `C20`: Decrease transmission power for 3245596_3
- `C21`: Adjust the azimuth of 3278412_2 by 14 degrees
- `C22`: Increase A3 Offset threshold for 3278412_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.624 | MS1 | 121.4656761097 | 31.1446298071 | 988 | 504990 | -85.11 | 17.90 | 567.66 | 0.18 | 2.92 | 1576 |
| 2024-09-20 22:21:32.399 | MS1 | 121.4656626637 | 31.1446301609 | 988 | 504990 | -89.11 | 17.11 | 532.24 | 0.13 | 2.65 | 1576 |
| 2024-09-20 22:21:33.402 | MS1 | 121.4656614195 | 31.1446199997 | 988 | 504990 | -87.55 | 14.22 | 534.54 | 0.13 | 2.93 | 1570 |
| 2024-09-20 22:21:34.923 | MS1 | 121.4656757991 | 31.1446199728 | 988 | 504990 | -86.65 | 16.82 | 62.77 | 0.20 | 2.12 | 1579 |
| 2024-09-20 22:21:35.762 | MS1 | 121.4656753292 | 31.1446236153 | 988 | 504990 | -88.55 | 15.35 | 96.26 | 0.17 | 2.63 | 1565 |
| 2024-09-20 22:21:36.928 | MS1 | 121.4656695123 | 31.1446354204 | 988 | 504990 | -85.79 | 13.10 | 66.37 | 0.14 | 2.09 | 1585 |
| 2024-09-20 22:21:37.869 | MS1 | 121.4656775497 | 31.1446341424 | 988 | 504990 | -91.00 | 12.41 | 77.78 | 0.08 | 2.41 | 1588 |
| 2024-09-20 22:21:38.884 | MS1 | 121.4656583337 | 31.1446191267 | 988 | 504990 | -91.64 | 8.10 | 69.60 | 0.05 | 2.64 | 1563 |
| 2024-09-20 22:21:39.265 | MS1 | 121.4656588019 | 31.1446226620 | 988 | 504990 | -93.94 | 9.92 | 72.39 | 0.18 | 2.66 | 1595 |
| 2024-09-20 22:21:40.932 | MS1 | 121.4656720800 | 31.1446340435 | 988 | 504990 | -92.33 | 8.07 | 359.59 | 0.11 | 2.16 | 1581 |
| 2024-09-20 22:21:41.980 | MS1 | 121.4656706593 | 31.1446262009 | 988 | 504990 | -92.39 | 12.57 | 332.10 | 0.15 | 2.74 | 1597 |
| 2024-09-20 22:21:42.196 | MS1 | 121.4656595640 | 31.1446229880 | 988 | 504990 | -92.12 | 8.79 | 402.16 | 0.14 | 2.27 | 1564 |

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
| 3245596 | 3 | 121.4704568249 | 31.1511725650 | 180 | 0 | 0 | 18.7 | TDD | 413 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3270699 | 1 | 121.4645131215 | 31.1471398140 | 150 | 8 | 5 | 24.7 | TDD | 227 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3276992 | 4 | 121.4742848072 | 31.1480046894 | 179 | 14 | 4 | 33.9 | TDD | 998 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3278412 | 2 | 121.4654492284 | 31.1484403633 | 191 | 1 | 7 | 27.5 | TDD | 988 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.061 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.079 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.227 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.227 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.924 | NREventA3 | measId:2;ServCellPCI:321;Se... |
| 2024-09-20 22:21:38.164 | NRHandoverAttempt | SourcePCI:321;SourceNR-ARFC... |
| 2024-09-20 22:21:38.200 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.213 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.327 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.327 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3270699 | 1 | 80.8046 | 80.4496 | -117.0397 | 18.6552 | 115.7120 | 0.0170 | 0.0105 |
| 2024_09_19 22:00 | 3278412 | 2 | 87.7389 | 78.3245 | -117.0882 | 9.9602 | 159.0994 | 0.0005 | 0.0168 |
| 2024_09_19 22:00 | 3245596 | 3 | 83.5998 | 79.4536 | -114.1298 | 13.1667 | 83.8182 | 0.0131 | 0.0166 |
| 2024_09_19 22:00 | 3276992 | 4 | 85.0776 | 79.6188 | -116.8588 | 16.8685 | 99.3526 | 0.0100 | 0.0199 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416761_B56FFB7D | 504990 | 988 | -88.3 | 504990 | 413 | -87.9 | 504990 | 227 | -99.9 | 504990 | 998 |
| MR_1774416761_5738C5A7 | 504990 | 988 | -87.8 | 504990 | 413 | -87.0 | 504990 | 227 | -98.2 | 504990 | 998 |
| MR_1774416761_1DC137BC | 504990 | 988 | -85.1 | 504990 | 413 | -87.5 | 504990 | 227 | -100.9 | 504990 | 998 |
| MR_1774416761_263C69CF | 504990 | 988 | -85.5 | 504990 | 413 | -87.3 | 504990 | 227 | -99.4 | 504990 | 998 |
| MR_1774416761_4D3785AD | 504990 | 988 | -85.8 | 504990 | 413 | -88.5 | 504990 | 227 | -101.6 | 504990 | 998 |
| MR_1774416761_881D9A3B | 504990 | 988 | -87.9 | 504990 | 413 | -88.5 | 504990 | 227 | -99.1 | 504990 | 998 |
| MR_1774416761_9DC33E94 | 504990 | 988 | -85.1 | 504990 | 413 | -86.9 | 504990 | 227 | -97.7 | 504990 | 998 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 749: `8d1d8be4-d33...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8d1d8be4-d336-4db7-ae78-71234b60f382` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3266056_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[749] topology](images/train_0749.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3266056_2
- `C2`: Press down the tilt angle of 3266056_2 by 5 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221291_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221291_1
- `C5`: Increase A3 Offset threshold for 3266056_2
- `C6`: Increase transmission power for 3221291_1
- `C7`: Decrease transmission power for 3266056_2
- `C8`: Decrease transmission power for 3221291_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Lift the tilt angle  of 3221291_1 by 3 degrees
- `C11`: Decrease A3 Offset threshold for 3266056_2
- `C12`: Adjust the azimuth of 3221291_1 by 50 degrees
- `C13`: Lift the tilt angle of 3266056_2 by 5 degrees
- `C14`: Adjust the azimuth of 3266056_2 by 9 degrees
- `C15`: Add neighbor relationship between 3266056_2 and 3221291_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266056_2 **← 정답**
- `C17`: Press down the tilt angle  of 3221291_1 by 3 degrees
- `C18`: Check test server and transmission issues
- `C19`: Add neighbor relationship between 3267399_3 and 3221291_1
- `C20`: Decrease A3 Offset threshold for 3221291_1
- `C21`: Increase A3 Offset threshold for 3221291_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266056_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.772 | MS1 | 121.4656677765 | 31.1446191248 | 61 | 504990 | -89.33 | 12.88 | 514.07 | 0.09 | 2.41 | 1575 |
| 2024-09-20 22:21:32.869 | MS1 | 121.4656709724 | 31.1446184848 | 61 | 504990 | -86.89 | 17.03 | 294.79 | 0.11 | 2.82 | 1578 |
| 2024-09-20 22:21:33.307 | MS1 | 121.4656632770 | 31.1446263353 | 61 | 504990 | -88.52 | 15.83 | 595.04 | 0.03 | 2.83 | 1586 |
| 2024-09-20 22:21:34.882 | MS1 | 121.4656757309 | 31.1446327472 | 61 | 504990 | -89.41 | 14.23 | 85.17 | 0.58 | 2.01 | 651 |
| 2024-09-20 22:21:35.723 | MS1 | 121.4656677145 | 31.1446198459 | 61 | 504990 | -89.39 | 14.95 | 67.58 | 0.58 | 2.96 | 609 |
| 2024-09-20 22:21:36.578 | MS1 | 121.4656733554 | 31.1446346266 | 61 | 504990 | -88.53 | 13.67 | 73.10 | 0.52 | 2.91 | 644 |
| 2024-09-20 22:21:37.331 | MS1 | 121.4656764878 | 31.1446290118 | 61 | 504990 | -91.44 | 8.27 | 70.59 | 0.55 | 2.46 | 649 |
| 2024-09-20 22:21:38.578 | MS1 | 121.4656643178 | 31.1446290902 | 61 | 504990 | -89.07 | 7.36 | 101.01 | 0.56 | 2.14 | 529 |
| 2024-09-20 22:21:39.640 | MS1 | 121.4656594084 | 31.1446251391 | 61 | 504990 | -91.84 | 7.65 | 54.47 | 0.57 | 2.42 | 668 |
| 2024-09-20 22:21:40.986 | MS1 | 121.4656630927 | 31.1446247787 | 61 | 504990 | -93.81 | 9.57 | 378.25 | 0.02 | 2.40 | 1575 |
| 2024-09-20 22:21:41.902 | MS1 | 121.4656713313 | 31.1446232979 | 61 | 504990 | -91.23 | 10.34 | 437.83 | 0.02 | 2.03 | 1598 |
| 2024-09-20 22:21:42.774 | MS1 | 121.4656605643 | 31.1446368848 | 61 | 504990 | -89.81 | 12.47 | 565.20 | 0.09 | 2.39 | 1592 |

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
| 3221291 | 1 | 121.4754655992 | 31.1501370057 | 10 | 1 | 11 | 43.1 | TDD | 696 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3231580 | 4 | 121.4747941091 | 31.1486404623 | 66 | 14 | 11 | 36.8 | TDD | 742 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3266056 | 2 | 121.4703293678 | 31.1523775778 | 198 | 3 | 2 | 40.0 | TDD | 61 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3267399 | 3 | 121.4718009572 | 31.1445016482 | 53 | 1 | 10 | 47.4 | TDD | 400 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.369 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.384 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.520 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.520 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.219 | NREventA3 | measId:2;ServCellPCI:406;Se... |
| 2024-09-20 22:21:38.459 | NRHandoverAttempt | SourcePCI:406;SourceNR-ARFC... |
| 2024-09-20 22:21:38.500 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.514 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.616 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.616 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221291 | 1 | 7.0732 | 14.9981 | -115.8893 | 16.7494 | 194.7013 | 0.0087 | 0.0055 |
| 2024_09_20 22:00 | 3266056 | 2 | 10.9260 | 19.6807 | -117.7748 | 11.7532 | 119.8738 | 0.0126 | 0.0135 |
| 2024_09_20 22:00 | 3267399 | 3 | 11.1242 | 15.8301 | -116.7862 | 6.9094 | 186.6858 | 0.0138 | 0.0191 |
| 2024_09_20 22:00 | 3231580 | 4 | 12.3510 | 18.0943 | -117.1993 | 15.6403 | 120.5956 | 0.0099 | 0.0060 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412042_046C1CD9 | 504990 | 61 | -90.7 | 504990 | 696 | -90.2 | 504990 | 400 | -96.8 | 504990 | 742 |
| MR_1774412042_BCF1507B | 504990 | 61 | -88.2 | 504990 | 696 | -91.2 | 504990 | 400 | -96.3 | 504990 | 742 |
| MR_1774412042_97C3BDC0 | 504990 | 61 | -89.1 | 504990 | 696 | -89.4 | 504990 | 400 | -94.7 | 504990 | 742 |
| MR_1774412042_9EC567F6 | 504990 | 61 | -90.2 | 504990 | 696 | -91.3 | 504990 | 400 | -94.9 | 504990 | 742 |
| MR_1774412042_B7EB332D | 504990 | 61 | -88.6 | 504990 | 696 | -88.6 | 504990 | 400 | -97.8 | 504990 | 742 |

> *... 2개 열 생략 (전체 14열)*

---
