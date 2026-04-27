# Track A 문제 분석 — train[1280]~train[1289]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1280] ~ train[1289] (10개)

## 목차

1. [문제 1280: `47171cba-abd...`](#1280) — single-answer, 정답: C14
2. [문제 1281: `82022ee8-5c7...`](#1281) — single-answer, 정답: C16
3. [문제 1282: `1e7d19f3-8a5...`](#1282) — single-answer, 정답: C15
4. [문제 1283: `83c8ab17-35c...`](#1283) — single-answer, 정답: C17
5. [문제 1284: `b5f8c707-4e7...`](#1284) — single-answer, 정답: C7
6. [문제 1285: `4b268492-ed1...`](#1285) — single-answer, 정답: C13
7. [문제 1286: `77edc8b4-716...`](#1286) — single-answer, 정답: C4
8. [문제 1287: `00a19bed-1dc...`](#1287) — single-answer, 정답: C15
9. [문제 1288: `55339c24-e4b...`](#1288) — single-answer, 정답: C8
10. [문제 1289: `f8fadb36-af9...`](#1289) — single-answer, 정답: C4

---

### 문제 1280: `47171cba-abd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `47171cba-abda-4da0-9440-fda861ac4221` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1280] topology](images/train_1280.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3258636_1
- `C2`: Lift the tilt angle  of 3212655_2 by 10 degrees
- `C3`: Adjust the azimuth of 3258636_1 by 50 degrees
- `C4`: Adjust the azimuth of 3212655_2 by 50 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease A3 Offset threshold for 3258636_1
- `C7`: Increase transmission power for 3212655_2
- `C8`: Decrease A3 Offset threshold for 3212655_2
- `C9`: Increase transmission power for 3258636_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258636_1
- `C11`: Increase A3 Offset threshold for 3212655_2
- `C12`: Decrease transmission power for 3258636_1
- `C13`: Add neighbor relationship between 3258636_1 and 3212655_2
- `C14`: Check test server and transmission issues **← 정답**
- `C15`: Press down the tilt angle  of 3212655_2 by 10 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212655_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258636_1
- `C18`: Decrease transmission power for 3212655_2
- `C19`: Add neighbor relationship between 3227225_4 and 3212655_2
- `C20`: Lift the tilt angle of 3258636_1 by 8 degrees
- `C21`: Press down the tilt angle of 3258636_1 by 8 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212655_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.556 | MS1 | 121.4656680960 | 31.1446281124 | 464 | 504990 | -86.65 | 13.99 | 343.09 | 0.12 | 2.52 | 1571 |
| 2024-09-20 22:21:32.946 | MS1 | 121.4656711091 | 31.1446220494 | 464 | 504990 | -90.77 | 12.89 | 311.17 | 0.07 | 2.12 | 1589 |
| 2024-09-20 22:21:33.283 | MS1 | 121.4656629277 | 31.1446351031 | 464 | 504990 | -90.95 | 16.97 | 368.49 | 0.03 | 2.22 | 1585 |
| 2024-09-20 22:21:34.162 | MS1 | 121.4656589371 | 31.1446322141 | 464 | 504990 | -87.46 | 12.33 | 73.10 | 0.06 | 2.51 | 461 |
| 2024-09-20 22:21:35.549 | MS1 | 121.4656700433 | 31.1446348449 | 464 | 504990 | -89.47 | 12.17 | 40.77 | 0.10 | 2.95 | 356 |
| 2024-09-20 22:21:36.143 | MS1 | 121.4656597918 | 31.1446333140 | 464 | 504990 | -86.23 | 16.11 | 99.08 | 0.05 | 2.97 | 396 |
| 2024-09-20 22:21:37.380 | MS1 | 121.4656776715 | 31.1446339914 | 464 | 504990 | -92.52 | 12.57 | 88.94 | 0.00 | 2.29 | 322 |
| 2024-09-20 22:21:38.768 | MS1 | 121.4656667004 | 31.1446280152 | 464 | 504990 | -90.71 | 10.47 | 72.42 | 0.15 | 2.45 | 352 |
| 2024-09-20 22:21:39.910 | MS1 | 121.4656720985 | 31.1446352829 | 464 | 504990 | -89.89 | 11.90 | 70.52 | 0.10 | 2.07 | 377 |
| 2024-09-20 22:21:40.540 | MS1 | 121.4656653888 | 31.1446278683 | 464 | 504990 | -92.15 | 7.23 | 417.58 | 0.15 | 2.35 | 1596 |
| 2024-09-20 22:21:41.670 | MS1 | 121.4656742151 | 31.1446202046 | 464 | 504990 | -92.57 | 11.03 | 544.25 | 0.10 | 2.94 | 1596 |
| 2024-09-20 22:21:42.568 | MS1 | 121.4656610259 | 31.1446234804 | 464 | 504990 | -92.34 | 8.78 | 501.58 | 0.01 | 2.28 | 1564 |

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
| 3212655 | 2 | 121.4640051584 | 31.1474179715 | 309 | 7 | 8 | 28.6 | TDD | 713 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3224264 | 3 | 121.4655471813 | 31.1469079727 | 302 | 9 | 6 | 30.1 | TDD | 902 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3227225 | 4 | 121.4716270661 | 31.1446505438 | 97 | 9 | 2 | 45.1 | TDD | 744 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3258636 | 1 | 121.4712554270 | 31.1506556324 | 105 | 5 | 4 | 44.8 | TDD | 464 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.592 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.611 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.737 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.737 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.414 | NREventA3 | measId:2;ServCellPCI:939;Se... |
| 2024-09-20 22:21:38.654 | NRHandoverAttempt | SourcePCI:939;SourceNR-ARFC... |
| 2024-09-20 22:21:38.688 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.699 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.808 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.808 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258636 | 1 | 12.0383 | 8.1626 | -115.7236 | 17.2028 | 190.7113 | 0.0019 | 0.0062 |
| 2024_09_20 22:00 | 3212655 | 2 | 16.9538 | 17.4973 | -116.6523 | 5.0428 | 167.4442 | 0.0028 | 0.0134 |
| 2024_09_20 22:00 | 3224264 | 3 | 5.8273 | 6.2410 | -114.1428 | 13.1476 | 100.5393 | 0.0017 | 0.0001 |
| 2024_09_20 22:00 | 3227225 | 4 | 12.0133 | 12.7453 | -114.0061 | 18.4919 | 106.8990 | 0.0171 | 0.0067 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416047_9F2AB73E | 504990 | 464 | -86.0 | 504990 | 713 | -90.0 | 504990 | 744 | -95.1 | 504990 | 902 |
| MR_1774416047_2DE31B2E | 504990 | 464 | -85.8 | 504990 | 713 | -91.0 | 504990 | 744 | -95.8 | 504990 | 902 |
| MR_1774416047_8C6808D7 | 504990 | 464 | -87.8 | 504990 | 713 | -93.0 | 504990 | 744 | -97.9 | 504990 | 902 |
| MR_1774416047_81CFF393 | 504990 | 464 | -86.2 | 504990 | 713 | -91.3 | 504990 | 744 | -97.1 | 504990 | 902 |
| MR_1774416047_27ABDD31 | 504990 | 464 | -89.4 | 504990 | 713 | -92.7 | 504990 | 744 | -94.4 | 504990 | 902 |
| MR_1774416047_32E88569 | 504990 | 464 | -86.9 | 504990 | 713 | -91.8 | 504990 | 744 | -97.3 | 504990 | 902 |
| MR_1774416047_BBBFE18C | 504990 | 464 | -86.8 | 504990 | 713 | -91.7 | 504990 | 744 | -94.9 | 504990 | 902 |
| MR_1774416047_5D4E0A5C | 504990 | 464 | -88.2 | 504990 | 713 | -91.7 | 504990 | 744 | -97.3 | 504990 | 902 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1281: `82022ee8-5c7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `82022ee8-5c71-4096-98a5-d5fde2b29f82` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Lift the tilt angle  of 3219881_2 by 4 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1281] topology](images/train_1281.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3213216_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237157_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213216_1
- `C4`: Press down the tilt angle  of 3219881_2 by 4 degrees
- `C5`: Decrease A3 Offset threshold for 3237157_3
- `C6`: Increase A3 Offset threshold for 3237157_3
- `C7`: Add neighbor relationship between 3213216_1 and 3237157_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213216_1
- `C9`: Increase A3 Offset threshold for 3213216_1
- `C10`: Adjust the azimuth of 3219881_2 by 1 degrees
- `C11`: Increase transmission power for 3237157_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237157_3
- `C13`: Decrease A3 Offset threshold for 3213216_1
- `C14`: Add neighbor relationship between 3219881_2 and 3237157_3
- `C15`: Decrease transmission power for 3213216_1
- `C16`: Lift the tilt angle  of 3219881_2 by 4 degrees **← 정답**
- `C17`: Decrease transmission power for 3237157_3
- `C18`: Lift the tilt angle of 3213216_1 by 3 degrees
- `C19`: Press down the tilt angle of 3213216_1 by 3 degrees
- `C20`: Check test server and transmission issues
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Adjust the azimuth of 3213216_1 by 44 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.535 | MS1 | 121.4656623130 | 31.1446296768 | 374 | 504990 | -91.05 | 16.29 | 542.05 | 0.13 | 2.54 | 1570 |
| 2024-09-20 22:21:32.418 | MS1 | 121.4656656624 | 31.1446291376 | 374 | 504990 | -91.98 | 12.91 | 512.64 | 0.15 | 2.71 | 1574 |
| 2024-09-20 22:21:33.901 | MS1 | 121.4656580517 | 31.1446333536 | 374 | 504990 | -90.12 | 14.54 | 313.16 | 0.12 | 2.40 | 1568 |
| 2024-09-20 22:21:34.744 | MS1 | 121.4656616905 | 31.1446226113 | 374 | 504990 | -87.05 | 15.14 | 62.96 | 0.07 | 2.52 | 1561 |
| 2024-09-20 22:21:35.831 | MS1 | 121.4656599140 | 31.1446272457 | 374 | 504990 | -88.79 | 12.91 | 48.03 | 0.11 | 2.31 | 1562 |
| 2024-09-20 22:21:36.960 | MS1 | 121.4656586206 | 31.1446187988 | 374 | 504990 | -86.04 | 13.23 | 87.21 | 0.16 | 2.79 | 1588 |
| 2024-09-20 22:21:37.240 | MS1 | 121.4656693436 | 31.1446182759 | 374 | 504990 | -90.74 | 9.79 | 70.24 | 0.20 | 2.40 | 1592 |
| 2024-09-20 22:21:38.784 | MS1 | 121.4656611330 | 31.1446315609 | 374 | 504990 | -91.51 | 7.56 | 81.66 | 0.18 | 2.82 | 1565 |
| 2024-09-20 22:21:39.314 | MS1 | 121.4656608775 | 31.1446204552 | 374 | 504990 | -91.12 | 12.51 | 58.31 | 0.16 | 2.57 | 1560 |
| 2024-09-20 22:21:40.828 | MS1 | 121.4656665688 | 31.1446348149 | 374 | 504990 | -93.04 | 7.96 | 525.13 | 0.00 | 2.52 | 1580 |
| 2024-09-20 22:21:41.279 | MS1 | 121.4656658487 | 31.1446218722 | 374 | 504990 | -89.18 | 11.65 | 561.52 | 0.20 | 2.32 | 1579 |
| 2024-09-20 22:21:42.230 | MS1 | 121.4656671997 | 31.1446240883 | 374 | 504990 | -92.86 | 8.90 | 321.81 | 0.03 | 2.55 | 1562 |

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
| 3213216 | 1 | 121.4672027464 | 31.1470816417 | 164 | 0 | 9 | 16.8 | TDD | 374 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3219881 | 2 | 121.4741306719 | 31.1530988130 | 77 | 13 | 4 | 36.4 | TDD | 198 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3237157 | 3 | 121.4695483086 | 31.1534941878 | 202 | 2 | 12 | 40.1 | TDD | 166 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3254816 | 4 | 121.4719561178 | 31.1479206054 | 343 | 15 | 2 | 43.4 | TDD | 143 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.351 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.374 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.497 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.497 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.245 | NREventA3 | measId:2;ServCellPCI:202;Se... |
| 2024-09-20 22:21:38.485 | NRHandoverAttempt | SourcePCI:202;SourceNR-ARFC... |
| 2024-09-20 22:21:38.532 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.545 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.687 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.687 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213216 | 1 | 83.5119 | 87.0342 | -117.4861 | 8.7156 | 199.4501 | 0.0123 | 0.0037 |
| 2024_09_20 22:00 | 3219881 | 2 | 8.1985 | 5.6295 | -115.5170 | 6.3132 | 162.0604 | 0.0200 | 0.0170 |
| 2024_09_20 22:00 | 3237157 | 3 | 6.7583 | 15.6921 | -114.8601 | 14.8842 | 192.7747 | 0.0080 | 0.0029 |
| 2024_09_20 22:00 | 3254816 | 4 | 14.4731 | 13.3717 | -114.7039 | 17.5699 | 184.6423 | 0.0075 | 0.0016 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416650_88597E2D | 504990 | 374 | -87.8 | 504990 | 166 | -90.4 | 504990 | 198 | -96.2 | 504990 | 143 |
| MR_1774416650_6FBE0AE8 | 504990 | 374 | -85.6 | 504990 | 166 | -90.0 | 504990 | 198 | -93.7 | 504990 | 143 |
| MR_1774416650_E5C2C4C3 | 504990 | 374 | -86.8 | 504990 | 166 | -92.6 | 504990 | 198 | -93.9 | 504990 | 143 |
| MR_1774416650_FCF2197E | 504990 | 374 | -85.1 | 504990 | 166 | -92.5 | 504990 | 198 | -94.9 | 504990 | 143 |
| MR_1774416650_E53F46BD | 504990 | 374 | -87.1 | 504990 | 166 | -91.8 | 504990 | 198 | -94.7 | 504990 | 143 |
| MR_1774416650_B3A9EE58 | 504990 | 374 | -86.6 | 504990 | 166 | -90.9 | 504990 | 198 | -97.5 | 504990 | 143 |
| MR_1774416650_765E03D2 | 504990 | 374 | -87.3 | 504990 | 166 | -91.4 | 504990 | 198 | -94.0 | 504990 | 143 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1282: `1e7d19f3-8a5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1e7d19f3-8a52-4009-b622-e43c3f7015d5` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1282] topology](images/train_1282.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3248028_3
- `C2`: Decrease transmission power for 3215778_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248028_3
- `C4`: Adjust the azimuth of 3248028_3 by 45 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248028_3
- `C6`: Decrease A3 Offset threshold for 3248028_3
- `C7`: Decrease A3 Offset threshold for 3215778_1
- `C8`: Add neighbor relationship between 3233766_2 and 3248028_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215778_1
- `C10`: Press down the tilt angle of 3215778_1 by 8 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215778_1
- `C12`: Increase transmission power for 3215778_1
- `C13`: Add neighbor relationship between 3215778_1 and 3248028_3
- `C14`: Check test server and transmission issues
- `C15`: Insufficient data; more data is needed for judgment. **← 정답**
- `C16`: Increase transmission power for 3248028_3
- `C17`: Lift the tilt angle of 3215778_1 by 8 degrees
- `C18`: Increase A3 Offset threshold for 3248028_3
- `C19`: Press down the tilt angle  of 3248028_3 by 8 degrees
- `C20`: Adjust the azimuth of 3215778_1 by 50 degrees
- `C21`: Lift the tilt angle  of 3248028_3 by 8 degrees
- `C22`: Increase A3 Offset threshold for 3215778_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.801 | MS1 | 121.4656640599 | 31.1446329114 | 440 | 504990 | -86.02 | 12.85 | 323.03 | 0.13 | 2.64 | 1560 |
| 2024-09-20 22:21:32.420 | MS1 | 121.4656766705 | 31.1446310825 | 440 | 504990 | -88.90 | 17.11 | 499.26 | 0.18 | 2.15 | 1582 |
| 2024-09-20 22:21:33.931 | MS1 | 121.4656641309 | 31.1446205452 | 440 | 504990 | -85.13 | 17.90 | 563.21 | 0.08 | 2.97 | 1569 |
| 2024-09-20 22:21:34.534 | MS1 | 121.4656618927 | 31.1446345187 | 440 | 504990 | -86.78 | 14.24 | 62.97 | 0.03 | 2.20 | 1561 |
| 2024-09-20 22:21:35.821 | MS1 | 121.4656758306 | 31.1446291245 | 440 | 504990 | -86.21 | 13.56 | 88.54 | 0.20 | 3.00 | 1567 |
| 2024-09-20 22:21:36.409 | MS1 | 121.4656732535 | 31.1446201955 | 440 | 504990 | -91.28 | 15.49 | 98.73 | 0.15 | 2.92 | 1581 |
| 2024-09-20 22:21:37.231 | MS1 | 121.4656756782 | 31.1446210088 | 440 | 504990 | -92.38 | 10.13 | 76.15 | 0.13 | 2.85 | 1569 |
| 2024-09-20 22:21:38.103 | MS1 | 121.4656625860 | 31.1446318540 | 440 | 504990 | -92.21 | 11.20 | 69.08 | 0.00 | 2.01 | 1599 |
| 2024-09-20 22:21:39.566 | MS1 | 121.4656591153 | 31.1446373518 | 440 | 504990 | -91.50 | 7.74 | 94.40 | 0.12 | 2.56 | 1584 |
| 2024-09-20 22:21:40.392 | MS1 | 121.4656776962 | 31.1446263285 | 440 | 504990 | -92.94 | 8.76 | 582.07 | 0.15 | 2.28 | 1587 |
| 2024-09-20 22:21:41.397 | MS1 | 121.4656606312 | 31.1446250113 | 440 | 504990 | -92.31 | 9.91 | 414.74 | 0.12 | 2.26 | 1595 |
| 2024-09-20 22:21:42.147 | MS1 | 121.4656728312 | 31.1446205599 | 440 | 504990 | -89.22 | 10.35 | 310.00 | 0.02 | 2.76 | 1575 |

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
| 3215778 | 1 | 121.4677220867 | 31.1478257652 | 149 | 2 | 10 | 45.5 | TDD | 440 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3219125 | 4 | 121.4696396966 | 31.1552641816 | 298 | 10 | 5 | 34.5 | TDD | 508 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3233766 | 2 | 121.4733375686 | 31.1500213354 | 73 | 14 | 11 | 39.2 | TDD | 665 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3248028 | 3 | 121.4685771995 | 31.1464346917 | 279 | 0 | 11 | 47.4 | TDD | 418 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.679 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.699 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.812 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.812 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.495 | NREventA3 | measId:2;ServCellPCI:512;Se... |
| 2024-09-20 22:21:38.735 | NRHandoverAttempt | SourcePCI:512;SourceNR-ARFC... |
| 2024-09-20 22:21:38.770 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.784 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.898 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.898 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3215778 | 1 | 77.6302 | 77.6100 | -115.4308 | 8.5197 | 94.9911 | 0.0111 | 0.0040 |
| 2024_09_19 22:00 | 3233766 | 2 | 90.6522 | 82.4150 | -116.6072 | 8.3731 | 112.5798 | 0.0164 | 0.0196 |
| 2024_09_19 22:00 | 3248028 | 3 | 90.8305 | 93.8109 | -115.5929 | 18.4243 | 173.3409 | 0.0004 | 0.0052 |
| 2024_09_19 22:00 | 3219125 | 4 | 78.3304 | 79.9940 | -115.7423 | 12.0509 | 87.1913 | 0.0183 | 0.0037 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414318_24423019 | 504990 | 440 | -87.4 | 504990 | 418 | -92.0 | 504990 | 665 | -95.3 | 504990 | 508 |
| MR_1774414318_07ACAFDD | 504990 | 440 | -85.5 | 504990 | 418 | -93.7 | 504990 | 665 | -98.4 | 504990 | 508 |
| MR_1774414318_F92D2354 | 504990 | 440 | -87.2 | 504990 | 418 | -94.6 | 504990 | 665 | -97.2 | 504990 | 508 |
| MR_1774414318_5457AB3B | 504990 | 440 | -85.8 | 504990 | 418 | -91.7 | 504990 | 665 | -96.9 | 504990 | 508 |
| MR_1774414318_F5393E88 | 504990 | 440 | -87.3 | 504990 | 418 | -94.6 | 504990 | 665 | -95.8 | 504990 | 508 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1283: `83c8ab17-35c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `83c8ab17-35cd-4115-a938-f94e49886147` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3213009_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1283] topology](images/train_1283.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3217161_4 and 3218838_2
- `C2`: Add neighbor relationship between 3213009_1 and 3218838_2
- `C3`: Adjust the azimuth of 3213009_1 by 5 degrees
- `C4`: Lift the tilt angle of 3213009_1 by 6 degrees
- `C5`: Check test server and transmission issues
- `C6`: Increase transmission power for 3213009_1
- `C7`: Press down the tilt angle  of 3218838_2 by 3 degrees
- `C8`: Increase A3 Offset threshold for 3218838_2
- `C9`: Decrease A3 Offset threshold for 3213009_1
- `C10`: Lift the tilt angle  of 3218838_2 by 3 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218838_2
- `C12`: Decrease transmission power for 3218838_2
- `C13`: Adjust the azimuth of 3218838_2 by 50 degrees
- `C14`: Decrease transmission power for 3213009_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218838_2
- `C16`: Increase A3 Offset threshold for 3213009_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213009_1 **← 정답**
- `C18`: Increase transmission power for 3218838_2
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Press down the tilt angle of 3213009_1 by 6 degrees
- `C21`: Decrease A3 Offset threshold for 3218838_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213009_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.190 | MS1 | 121.4656644528 | 31.1446248800 | 729 | 504990 | -88.35 | 15.95 | 507.39 | 0.08 | 2.10 | 1577 |
| 2024-09-20 22:21:32.811 | MS1 | 121.4656623917 | 31.1446223485 | 729 | 504990 | -86.44 | 15.53 | 590.40 | 0.03 | 2.89 | 1581 |
| 2024-09-20 22:21:33.829 | MS1 | 121.4656654576 | 31.1446208206 | 729 | 504990 | -86.43 | 17.37 | 576.89 | 0.05 | 2.14 | 1596 |
| 2024-09-20 22:21:34.805 | MS1 | 121.4656690865 | 31.1446235869 | 729 | 504990 | -86.71 | 13.48 | 55.79 | 0.56 | 2.98 | 643 |
| 2024-09-20 22:21:35.650 | MS1 | 121.4656697117 | 31.1446266291 | 729 | 504990 | -85.01 | 17.69 | 79.30 | 0.60 | 2.13 | 642 |
| 2024-09-20 22:21:36.160 | MS1 | 121.4656743416 | 31.1446301982 | 729 | 504990 | -90.89 | 13.70 | 48.00 | 0.70 | 2.83 | 620 |
| 2024-09-20 22:21:37.124 | MS1 | 121.4656735947 | 31.1446191185 | 729 | 504990 | -93.92 | 11.75 | 72.34 | 0.52 | 2.14 | 682 |
| 2024-09-20 22:21:38.623 | MS1 | 121.4656712102 | 31.1446244776 | 729 | 504990 | -93.19 | 8.74 | 83.32 | 0.70 | 2.31 | 696 |
| 2024-09-20 22:21:39.123 | MS1 | 121.4656674982 | 31.1446361544 | 729 | 504990 | -91.31 | 7.88 | 81.56 | 0.65 | 2.83 | 650 |
| 2024-09-20 22:21:40.685 | MS1 | 121.4656684000 | 31.1446228844 | 729 | 504990 | -92.14 | 10.81 | 469.65 | 0.11 | 2.16 | 1575 |
| 2024-09-20 22:21:41.235 | MS1 | 121.4656778008 | 31.1446231231 | 729 | 504990 | -89.21 | 8.57 | 575.08 | 0.07 | 2.78 | 1567 |
| 2024-09-20 22:21:42.799 | MS1 | 121.4656697508 | 31.1446269815 | 729 | 504990 | -91.78 | 8.62 | 597.56 | 0.19 | 2.81 | 1582 |

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
| 3213009 | 1 | 121.4692460331 | 31.1523495922 | 207 | 3 | 3 | 47.7 | TDD | 729 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3217161 | 4 | 121.4679994617 | 31.1555464037 | 227 | 10 | 4 | 16.9 | TDD | 941 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3218838 | 2 | 121.4651324050 | 31.1539229523 | 61 | 2 | 10 | 24.5 | TDD | 435 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3278461 | 3 | 121.4751316090 | 31.1459074557 | 357 | 10 | 0 | 20.2 | TDD | 85 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.297 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.318 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.419 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.419 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.114 | NREventA3 | measId:2;ServCellPCI:549;Se... |
| 2024-09-20 22:21:38.354 | NRHandoverAttempt | SourcePCI:549;SourceNR-ARFC... |
| 2024-09-20 22:21:38.388 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.403 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.545 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.545 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213009 | 1 | 5.8600 | 7.1173 | -115.8875 | 13.7225 | 115.0871 | 0.0116 | 0.0011 |
| 2024_09_20 22:00 | 3218838 | 2 | 5.9111 | 15.5304 | -114.8434 | 18.4569 | 90.3331 | 0.0104 | 0.0003 |
| 2024_09_20 22:00 | 3278461 | 3 | 10.5004 | 16.5596 | -116.2307 | 17.8794 | 105.1994 | 0.0060 | 0.0059 |
| 2024_09_20 22:00 | 3217161 | 4 | 7.5049 | 5.7104 | -115.8031 | 15.8636 | 94.7275 | 0.0112 | 0.0183 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416771_37C8C3CA | 504990 | 729 | -86.3 | 504990 | 435 | -87.4 | 504990 | 941 | -96.9 | 504990 | 85 |
| MR_1774416771_86527ABD | 504990 | 729 | -85.2 | 504990 | 435 | -88.2 | 504990 | 941 | -94.1 | 504990 | 85 |
| MR_1774416771_08C957CB | 504990 | 729 | -85.9 | 504990 | 435 | -85.3 | 504990 | 941 | -94.4 | 504990 | 85 |
| MR_1774416771_D06D20B1 | 504990 | 729 | -85.4 | 504990 | 435 | -87.2 | 504990 | 941 | -95.7 | 504990 | 85 |
| MR_1774416771_B64F415D | 504990 | 729 | -87.5 | 504990 | 435 | -86.6 | 504990 | 941 | -97.7 | 504990 | 85 |
| MR_1774416771_A6EDE594 | 504990 | 729 | -86.9 | 504990 | 435 | -88.2 | 504990 | 941 | -95.6 | 504990 | 85 |
| MR_1774416771_1CE13BA5 | 504990 | 729 | -87.5 | 504990 | 435 | -85.7 | 504990 | 941 | -97.6 | 504990 | 85 |
| MR_1774416771_34034FFD | 504990 | 729 | -87.4 | 504990 | 435 | -89.2 | 504990 | 941 | -94.7 | 504990 | 85 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1284: `b5f8c707-4e7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b5f8c707-4e74-46b5-b6d8-02e406cf4d70` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1284] topology](images/train_1284.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3229063_2
- `C2`: Increase transmission power for 3223156_3
- `C3`: Add neighbor relationship between 3229475_4 and 3223156_3
- `C4`: Add neighbor relationship between 3229063_2 and 3223156_3
- `C5`: Adjust the azimuth of 3229063_2 by 50 degrees
- `C6`: Increase A3 Offset threshold for 3223156_3
- `C7`: Insufficient data; more data is needed for judgment. **← 정답**
- `C8`: Decrease transmission power for 3223156_3
- `C9`: Lift the tilt angle  of 3223156_3 by 10 degrees
- `C10`: Decrease A3 Offset threshold for 3229063_2
- `C11`: Lift the tilt angle of 3229063_2 by 9 degrees
- `C12`: Check test server and transmission issues
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229063_2
- `C14`: Increase A3 Offset threshold for 3229063_2
- `C15`: Adjust the azimuth of 3223156_3 by 11 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229063_2
- `C17`: Press down the tilt angle  of 3223156_3 by 10 degrees
- `C18`: Press down the tilt angle of 3229063_2 by 9 degrees
- `C19`: Increase transmission power for 3229063_2
- `C20`: Decrease A3 Offset threshold for 3223156_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223156_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223156_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.526 | MS1 | 121.4656718736 | 31.1446351405 | 209 | 504990 | -89.64 | 13.26 | 321.10 | 0.20 | 2.19 | 1578 |
| 2024-09-20 22:21:32.517 | MS1 | 121.4656630487 | 31.1446216726 | 209 | 504990 | -86.32 | 12.68 | 545.72 | 0.14 | 2.55 | 1582 |
| 2024-09-20 22:21:33.739 | MS1 | 121.4656629159 | 31.1446235834 | 209 | 504990 | -87.14 | 12.38 | 303.55 | 0.19 | 2.35 | 1571 |
| 2024-09-20 22:21:34.632 | MS1 | 121.4656744456 | 31.1446332529 | 209 | 504990 | -88.58 | 13.83 | 86.41 | 0.08 | 2.52 | 1573 |
| 2024-09-20 22:21:35.729 | MS1 | 121.4656764563 | 31.1446241254 | 209 | 504990 | -91.25 | 17.85 | 81.03 | 0.08 | 2.32 | 1568 |
| 2024-09-20 22:21:36.685 | MS1 | 121.4656746533 | 31.1446348466 | 209 | 504990 | -91.36 | 12.20 | 49.91 | 0.07 | 2.01 | 1593 |
| 2024-09-20 22:21:37.224 | MS1 | 121.4656732212 | 31.1446253941 | 209 | 504990 | -93.83 | 10.62 | 102.30 | 0.07 | 2.08 | 1574 |
| 2024-09-20 22:21:38.641 | MS1 | 121.4656722960 | 31.1446279459 | 209 | 504990 | -89.06 | 9.95 | 70.94 | 0.17 | 2.39 | 1589 |
| 2024-09-20 22:21:39.353 | MS1 | 121.4656715647 | 31.1446317011 | 209 | 504990 | -90.24 | 11.49 | 89.13 | 0.07 | 2.65 | 1578 |
| 2024-09-20 22:21:40.955 | MS1 | 121.4656770503 | 31.1446187391 | 209 | 504990 | -93.63 | 12.59 | 582.60 | 0.16 | 2.54 | 1561 |
| 2024-09-20 22:21:41.177 | MS1 | 121.4656587808 | 31.1446314384 | 209 | 504990 | -92.14 | 7.49 | 360.77 | 0.08 | 2.95 | 1580 |
| 2024-09-20 22:21:42.954 | MS1 | 121.4656733629 | 31.1446290363 | 209 | 504990 | -92.23 | 7.01 | 306.21 | 0.04 | 2.45 | 1560 |

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
| 3223156 | 3 | 121.4748293534 | 31.1501198601 | 224 | 15 | 2 | 29.8 | TDD | 401 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3226988 | 1 | 121.4724125982 | 31.1521538111 | 150 | 3 | 9 | 44.4 | TDD | 296 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3229063 | 2 | 121.4747510531 | 31.1495883900 | 17 | 7 | 4 | 27.5 | TDD | 209 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3229475 | 4 | 121.4748996167 | 31.1557773859 | 114 | 4 | 0 | 24.4 | TDD | 95 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.072 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.091 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.240 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.240 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.914 | NREventA3 | measId:2;ServCellPCI:508;Se... |
| 2024-09-20 22:21:38.154 | NRHandoverAttempt | SourcePCI:508;SourceNR-ARFC... |
| 2024-09-20 22:21:38.202 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.213 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.313 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.313 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3226988 | 1 | 83.4057 | 84.0311 | -114.2275 | 6.4116 | 196.9867 | 0.0032 | 0.0129 |
| 2024_09_19 22:00 | 3229063 | 2 | 84.4700 | 86.1351 | -115.3256 | 12.7626 | 116.0687 | 0.0019 | 0.0046 |
| 2024_09_19 22:00 | 3223156 | 3 | 86.7208 | 84.7628 | -117.4926 | 16.8510 | 89.9930 | 0.0063 | 0.0179 |
| 2024_09_19 22:00 | 3229475 | 4 | 85.8889 | 84.9289 | -116.6221 | 11.1174 | 165.4925 | 0.0138 | 0.0177 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413490_365C2CCF | 504990 | 209 | -88.6 | 504990 | 401 | -97.2 | 504990 | 95 | -103.4 | 504990 | 296 |
| MR_1774413490_EA157A62 | 504990 | 209 | -89.1 | 504990 | 401 | -99.4 | 504990 | 95 | -101.7 | 504990 | 296 |
| MR_1774413490_10EE94E1 | 504990 | 209 | -89.2 | 504990 | 401 | -99.0 | 504990 | 95 | -103.1 | 504990 | 296 |
| MR_1774413490_CA4F8AC0 | 504990 | 209 | -86.7 | 504990 | 401 | -99.4 | 504990 | 95 | -101.1 | 504990 | 296 |
| MR_1774413490_A5138689 | 504990 | 209 | -89.4 | 504990 | 401 | -99.0 | 504990 | 95 | -102.7 | 504990 | 296 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1285: `4b268492-ed1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4b268492-ed1a-4ecd-8bfd-4a301c7b92b4` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244729_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1285] topology](images/train_1285.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3244729_2 by 4 degrees
- `C2`: Add neighbor relationship between 3225941_11 and 3253241_1
- `C3`: Increase transmission power for 3244729_2
- `C4`: Lift the tilt angle  of 3253241_1 by 4 degrees
- `C5`: Press down the tilt angle  of 3253241_1 by 4 degrees
- `C6`: Check test server and transmission issues
- `C7`: Increase A3 Offset threshold for 3244729_2
- `C8`: Decrease transmission power for 3244729_2
- `C9`: Lift the tilt angle of 3244729_2 by 4 degrees
- `C10`: Increase transmission power for 3253241_1
- `C11`: Decrease transmission power for 3253241_1
- `C12`: Adjust the azimuth of 3244729_2 by 39 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244729_2 **← 정답**
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253241_1
- `C15`: Decrease A3 Offset threshold for 3244729_2
- `C16`: Decrease A3 Offset threshold for 3253241_1
- `C17`: Increase A3 Offset threshold for 3253241_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Add neighbor relationship between 3244729_2 and 3253241_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253241_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244729_2
- `C22`: Adjust the azimuth of 3253241_1 by 11 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.603 | MS1 | 121.4656612123 | 31.1446360454 | 37 | 504990 | -93.89 | 13.55 | 468.49 | 0.11 | 2.47 | 1600 |
| 2024-09-20 22:21:32.126 | MS1 | 121.4656622707 | 31.1446243549 | 872 | 504990 | -94.10 | 13.83 | 320.09 | 0.15 | 2.59 | 1564 |
| 2024-09-20 22:21:33.885 | MS1 | 121.4656740901 | 31.1446289853 | 184 | 504990 | -93.56 | 9.31 | 308.06 | 0.14 | 2.07 | 1598 |
| 2024-09-20 22:21:34.708 | MS1 | 121.4656587610 | 31.1446194213 | 177 | 152650 | -87.87 | 6.91 | 92.75 | 0.10 | 1.69 | 923 |
| 2024-09-20 22:21:35.687 | MS1 | 121.4656580786 | 31.1446303060 | 776 | 152650 | -94.46 | 4.32 | 82.87 | 0.16 | 1.57 | 916 |
| 2024-09-20 22:21:36.435 | MS1 | 121.4656779584 | 31.1446287170 | 244 | 152650 | -93.04 | 6.76 | 48.78 | 0.20 | 1.58 | 925 |
| 2024-09-20 22:21:37.513 | MS1 | 121.4656721135 | 31.1446321737 | 92 | 152650 | -88.18 | 6.40 | 70.60 | 0.06 | 1.57 | 904 |
| 2024-09-20 22:21:38.967 | MS1 | 121.4656586536 | 31.1446189440 | 177 | 152650 | -95.92 | 5.66 | 85.87 | 0.16 | 1.62 | 973 |
| 2024-09-20 22:21:39.842 | MS1 | 121.4656689497 | 31.1446261987 | 776 | 152650 | -92.14 | 4.83 | 87.01 | 0.15 | 1.72 | 953 |
| 2024-09-20 22:21:40.324 | MS1 | 121.4656660598 | 31.1446323118 | 244 | 152650 | -87.25 | 5.16 | 80.56 | 0.06 | 2.97 | 1562 |
| 2024-09-20 22:21:41.339 | MS1 | 121.4656643005 | 31.1446272220 | 92 | 152650 | -91.87 | 2.61 | 57.34 | 0.14 | 2.37 | 1561 |
| 2024-09-20 22:21:42.374 | MS1 | 121.4656688598 | 31.1446345716 | 177 | 152650 | -95.42 | 3.72 | 54.79 | 0.16 | 2.26 | 1565 |

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
| 3220295 | 8 | 121.4680701480 | 31.1541969353 | 179 | 1 | 2 | 2.8 | FDD | 898 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3220963 | 3 | 121.4694654924 | 31.1486386407 | 83 | 6 | 12 | 6.4 | TDD | 872 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3223810 | 5 | 121.4695441843 | 31.1457153788 | 210 | 13 | 3 | 24.8 | TDD | 184 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3224870 | 7 | 121.4740111217 | 31.1500806782 | 131 | 15 | 11 | 0.3 | FDD | 640 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3225941 | 11 | 121.4713717651 | 31.1453849884 | 130 | 3 | 10 | 6.5 | FDD | 244 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3226226 | 12 | 121.4734678343 | 31.1471839100 | 269 | 13 | 7 | 0.5 | FDD | 341 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3231932 | 13 | 121.4745189240 | 31.1544719253 | 302 | 5 | 5 | 2.9 | FDD | 92 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3232586 | 10 | 121.4696266286 | 31.1476675548 | 148 | 0 | 9 | 4.5 | FDD | 177 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3240740 | 9 | 121.4733985373 | 31.1454747755 | 268 | 13 | 3 | 22.1 | FDD | 776 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3244729 | 2 | 121.4751001121 | 31.1449105027 | 307 | 4 | 7 | 6.4 | TDD | 37 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3253241 | 1 | 121.4709644552 | 31.1467091882 | 256 | 4 | 11 | 0.3 | TDD | 513 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3276503 | 6 | 121.4751026583 | 31.1524356232 | 23 | 3 | 2 | 20.4 | TDD | 987 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3276932 | 4 | 121.4665677750 | 31.1483541894 | 238 | 5 | 5 | 18.4 | TDD | 587 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.860 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.885 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.998 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.998 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.746 | NREventA2 | measId:1;ServCellPCI:54;Ser... |
| 2024-09-20 22:21:34.878 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.107 | NREventA5 | measId:3;ServCellPCI:54;Ser... |
| 2024-09-20 22:21:35.148 | NRHandoverAttempt | SourcePCI:54;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.179 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.191 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.294 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.294 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253241 | 1 | 11.4064 | 19.4044 | -114.7866 | 19.7118 | 143.5102 | 0.0077 | 0.0165 |
| 2024_09_20 22:00 | 3244729 | 2 | 8.0377 | 13.6383 | -116.7863 | 14.7668 | 108.9697 | 0.0035 | 0.0001 |
| 2024_09_20 22:00 | 3220963 | 3 | 12.1934 | 10.6267 | -116.7981 | 6.5587 | 161.5387 | 0.0056 | 0.0037 |
| 2024_09_20 22:00 | 3276932 | 4 | 6.3559 | 14.2441 | -116.5512 | 6.4201 | 197.9100 | 0.0062 | 0.0024 |
| 2024_09_20 22:00 | 3223810 | 5 | 12.5184 | 5.9695 | -115.2343 | 16.2931 | 103.1611 | 0.0055 | 0.0117 |
| 2024_09_20 22:00 | 3276503 | 6 | 7.2073 | 18.7635 | -114.1880 | 10.8334 | 99.8955 | 0.0142 | 0.0144 |
| 2024_09_20 22:00 | 3224870 | 7 | 13.0796 | 12.2317 | -115.2779 | 3.5042 | 33.0050 | 0.0137 | 0.0173 |
| 2024_09_20 22:00 | 3220295 | 8 | 15.9409 | 18.9239 | -115.5115 | 4.5566 | 57.0284 | 0.0049 | 0.0059 |
| 2024_09_20 22:00 | 3240740 | 9 | 6.3070 | 6.0512 | -115.0913 | 4.1922 | 56.6011 | 0.0052 | 0.0126 |
| 2024_09_20 22:00 | 3232586 | 10 | 18.4468 | 7.2097 | -115.7475 | 3.2646 | 22.8204 | 0.0018 | 0.0022 |
| 2024_09_20 22:00 | 3225941 | 11 | 16.5350 | 5.6092 | -114.3016 | 3.1009 | 54.3223 | 0.0179 | 0.0164 |
| 2024_09_20 22:00 | 3226226 | 12 | 7.5634 | 8.2083 | -116.3725 | 4.3319 | 59.3343 | 0.0162 | 0.0198 |
| 2024_09_20 22:00 | 3231932 | 13 | 14.0146 | 9.9537 | -114.8632 | 4.0486 | 57.7132 | 0.0134 | 0.0126 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415199_1551B714 | 504990 | 184 | -92.5 | 504990 | 513 | -91.7 | 504990 | 587 | -94.5 | 504990 | 987 |
| MR_1774415199_D3B50EF8 | 152650 | 177 | -86.5 | 152650 | 898 | -92.1 | 152650 | 640 | -100.6 | 152650 | 341 |
| MR_1774415199_2991F19E | 504990 | 184 | -95.1 | 504990 | 513 | -93.8 | 504990 | 587 | -93.2 | 504990 | 987 |
| MR_1774415199_1B457025 | 152650 | 177 | -87.4 | 152650 | 898 | -93.3 | 152650 | 640 | -97.9 | 152650 | 341 |
| MR_1774415199_F21FDDA7 | 152650 | 177 | -88.6 | 152650 | 898 | -90.9 | 152650 | 640 | -97.7 | 152650 | 341 |
| MR_1774415199_360A4B8C | 152650 | 177 | -87.0 | 152650 | 898 | -92.4 | 152650 | 640 | -100.4 | 152650 | 341 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1286: `77edc8b4-716...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `77edc8b4-7163-4085-a598-e416f66a9f05` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Add neighbor relationship between 3234958_1 and 3265844_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1286] topology](images/train_1286.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3265844_3
- `C2`: Adjust the azimuth of 3234958_1 by 50 degrees
- `C3`: Lift the tilt angle of 3234958_1 by 10 degrees
- `C4`: Add neighbor relationship between 3234958_1 and 3265844_3 **← 정답**
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234958_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265844_3
- `C7`: Decrease transmission power for 3234958_1
- `C8`: Increase transmission power for 3265844_3
- `C9`: Decrease transmission power for 3265844_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265844_3
- `C11`: Check test server and transmission issues
- `C12`: Press down the tilt angle  of 3265844_3 by 5 degrees
- `C13`: Lift the tilt angle  of 3265844_3 by 5 degrees
- `C14`: Decrease A3 Offset threshold for 3265844_3
- `C15`: Increase A3 Offset threshold for 3234958_1
- `C16`: Press down the tilt angle of 3234958_1 by 10 degrees
- `C17`: Decrease A3 Offset threshold for 3234958_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Adjust the azimuth of 3265844_3 by 16 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234958_1
- `C21`: Add neighbor relationship between 3247541_2 and 3265844_3
- `C22`: Increase transmission power for 3234958_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.931 | MS1 | 121.4656700144 | 31.1446369169 | 57 | 504990 | -80.98 | 14.87 | 488.32 | 0.09 | 2.23 | 1584 |
| 2024-09-20 22:21:32.302 | MS1 | 121.4656677011 | 31.1446233339 | 57 | 504990 | -75.68 | 16.29 | 512.02 | 0.11 | 2.36 | 1582 |
| 2024-09-20 22:21:33.980 | MS1 | 121.4656600727 | 31.1446312770 | 57 | 504990 | -84.89 | 15.55 | 427.94 | 0.06 | 2.39 | 1563 |
| 2024-09-20 22:21:34.303 | MS1 | 121.4656646742 | 31.1446250227 | 57 | 504990 | -94.24 | -0.98 | 46.80 | 0.01 | 1.15 | 1588 |
| 2024-09-20 22:21:35.513 | MS1 | 121.4656608863 | 31.1446199103 | 57 | 504990 | -90.00 | -1.72 | 42.11 | 0.10 | 1.07 | 1581 |
| 2024-09-20 22:21:36.347 | MS1 | 121.4656696968 | 31.1446224269 | 57 | 504990 | -90.19 | -0.56 | 76.71 | 0.11 | 1.47 | 1599 |
| 2024-09-20 22:21:37.487 | MS1 | 121.4656634414 | 31.1446256237 | 57 | 504990 | -92.77 | -0.90 | 38.66 | 0.08 | 1.32 | 1597 |
| 2024-09-20 22:21:38.517 | MS1 | 121.4656718780 | 31.1446366774 | 57 | 504990 | -77.75 | 15.15 | 412.35 | 0.17 | 1.30 | 1560 |
| 2024-09-20 22:21:39.316 | MS1 | 121.4656673936 | 31.1446371813 | 57 | 504990 | -82.79 | 14.58 | 526.60 | 0.06 | 1.25 | 1593 |
| 2024-09-20 22:21:40.796 | MS1 | 121.4656755555 | 31.1446249551 | 57 | 504990 | -76.57 | 17.66 | 389.00 | 0.09 | 2.40 | 1589 |
| 2024-09-20 22:21:41.627 | MS1 | 121.4656716195 | 31.1446322916 | 57 | 504990 | -80.65 | 12.14 | 570.49 | 0.01 | 2.16 | 1562 |
| 2024-09-20 22:21:42.622 | MS1 | 121.4656697835 | 31.1446330015 | 57 | 504990 | -80.57 | 16.74 | 406.01 | 0.02 | 2.48 | 1580 |

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
| 3234958 | 1 | 121.4672088465 | 31.1528981472 | 346 | 14 | 5 | 43.1 | TDD | 57 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3247541 | 2 | 121.4715563328 | 31.1441034753 | 202 | 12 | 6 | 38.5 | TDD | 123 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3265844 | 3 | 121.4745516566 | 31.1482643778 | 228 | 3 | 6 | 39.6 | TDD | 740 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3277726 | 4 | 121.4673446956 | 31.1544523904 | 18 | 1 | 8 | 25.6 | TDD | 111 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.236 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.252 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.375 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.375 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.089 | NREventA3 | measId:2;ServCellPCI:175;Se... |
| 2024-09-20 22:21:36.089 | NREventA3 | measId:2;ServCellPCI:175;Se... |
| 2024-09-20 22:21:37.089 | NREventA3 | measId:2;ServCellPCI:175;Se... |
| 2024-09-20 22:21:39.589 | NRRRCReestablishAttempt | PCI:175 |
| 2024-09-20 22:21:39.600 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.615 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.738 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.738 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234958 | 1 | 13.0148 | 10.4587 | -116.5874 | 17.1453 | 125.7222 | 0.0177 | 0.1353 |
| 2024_09_20 22:00 | 3247541 | 2 | 15.9896 | 12.4650 | -117.6366 | 19.9817 | 175.0727 | 0.0160 | 0.0111 |
| 2024_09_20 22:00 | 3265844 | 3 | 9.5103 | 16.2651 | -117.6004 | 17.1239 | 107.5861 | 0.0176 | 0.0006 |
| 2024_09_20 22:00 | 3277726 | 4 | 12.1758 | 9.0454 | -115.1063 | 10.2327 | 156.4206 | 0.0104 | 0.0078 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415633_BB687355 | 504990 | 57 | -94.3 | 504990 | 740 | -89.4 | 504990 | 123 | -92.8 | 504990 | 111 |
| MR_1774415633_16E6A827 | 504990 | 57 | -95.9 | 504990 | 740 | -88.1 | 504990 | 123 | -94.1 | 504990 | 111 |
| MR_1774415633_7234FB4D | 504990 | 57 | -95.5 | 504990 | 740 | -86.9 | 504990 | 123 | -94.0 | 504990 | 111 |
| MR_1774415633_74759059 | 504990 | 57 | -92.3 | 504990 | 740 | -90.6 | 504990 | 123 | -92.1 | 504990 | 111 |
| MR_1774415633_404D74D6 | 504990 | 740 | -90.1 | 504990 | 57 | -95.9 | 504990 | 123 | -95.1 | 504990 | 111 |
| MR_1774415633_8597C1FF | 504990 | 57 | -95.5 | 504990 | 740 | -87.5 | 504990 | 123 | -92.6 | 504990 | 111 |
| MR_1774415633_A081AE42 | 504990 | 740 | -87.4 | 504990 | 57 | -94.2 | 504990 | 123 | -93.2 | 504990 | 111 |
| MR_1774415633_3FB9EBB0 | 504990 | 740 | -89.9 | 504990 | 57 | -92.3 | 504990 | 123 | -95.0 | 504990 | 111 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1287: `00a19bed-1dc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `00a19bed-1dc9-47b4-a4b3-948b72771955` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1287] topology](images/train_1287.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3271681_4
- `C2`: Increase transmission power for 3271681_4
- `C3`: Lift the tilt angle  of 3271681_4 by 8 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256543_2
- `C5`: Adjust the azimuth of 3271681_4 by 50 degrees
- `C6`: Decrease A3 Offset threshold for 3256543_2
- `C7`: Add neighbor relationship between 3274356_1 and 3271681_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271681_4
- `C9`: Increase A3 Offset threshold for 3256543_2
- `C10`: Decrease transmission power for 3271681_4
- `C11`: Decrease transmission power for 3256543_2
- `C12`: Increase transmission power for 3256543_2
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Press down the tilt angle of 3256543_2 by 9 degrees
- `C15`: Check test server and transmission issues **← 정답**
- `C16`: Add neighbor relationship between 3256543_2 and 3271681_4
- `C17`: Adjust the azimuth of 3256543_2 by 50 degrees
- `C18`: Lift the tilt angle of 3256543_2 by 9 degrees
- `C19`: Decrease A3 Offset threshold for 3271681_4
- `C20`: Press down the tilt angle  of 3271681_4 by 8 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271681_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256543_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.410 | MS1 | 121.4656666754 | 31.1446263221 | 139 | 504990 | -86.14 | 15.91 | 501.80 | 0.05 | 2.90 | 1591 |
| 2024-09-20 22:21:32.579 | MS1 | 121.4656657325 | 31.1446345443 | 139 | 504990 | -85.90 | 14.62 | 494.46 | 0.08 | 2.92 | 1596 |
| 2024-09-20 22:21:33.101 | MS1 | 121.4656621413 | 31.1446343666 | 139 | 504990 | -86.64 | 13.65 | 382.46 | 0.06 | 2.29 | 1572 |
| 2024-09-20 22:21:34.807 | MS1 | 121.4656650180 | 31.1446279410 | 139 | 504990 | -91.09 | 14.80 | 60.72 | 0.05 | 2.75 | 389 |
| 2024-09-20 22:21:35.182 | MS1 | 121.4656594691 | 31.1446318739 | 139 | 504990 | -86.46 | 14.11 | 49.80 | 0.07 | 2.67 | 349 |
| 2024-09-20 22:21:36.867 | MS1 | 121.4656610735 | 31.1446318061 | 139 | 504990 | -87.78 | 14.13 | 60.21 | 0.02 | 2.07 | 415 |
| 2024-09-20 22:21:37.324 | MS1 | 121.4656582494 | 31.1446316949 | 139 | 504990 | -93.78 | 12.66 | 88.54 | 0.04 | 2.85 | 322 |
| 2024-09-20 22:21:38.667 | MS1 | 121.4656621382 | 31.1446212322 | 139 | 504990 | -90.11 | 9.68 | 51.78 | 0.08 | 2.92 | 402 |
| 2024-09-20 22:21:39.619 | MS1 | 121.4656659765 | 31.1446199124 | 139 | 504990 | -93.02 | 9.13 | 80.83 | 0.08 | 2.34 | 383 |
| 2024-09-20 22:21:40.349 | MS1 | 121.4656737671 | 31.1446360307 | 139 | 504990 | -91.32 | 9.15 | 577.35 | 0.07 | 2.52 | 1566 |
| 2024-09-20 22:21:41.316 | MS1 | 121.4656747775 | 31.1446377426 | 139 | 504990 | -91.48 | 10.59 | 522.89 | 0.10 | 2.92 | 1597 |
| 2024-09-20 22:21:42.680 | MS1 | 121.4656595635 | 31.1446356801 | 139 | 504990 | -93.85 | 10.74 | 599.96 | 0.06 | 2.85 | 1587 |

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
| 3256543 | 2 | 121.4667700294 | 31.1477905986 | 337 | 4 | 3 | 31.2 | TDD | 139 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3271681 | 4 | 121.4675200382 | 31.1500485926 | 62 | 5 | 6 | 33.1 | TDD | 231 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3274356 | 1 | 121.4690168121 | 31.1511551926 | 268 | 13 | 5 | 33.1 | TDD | 329 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3275777 | 3 | 121.4723137971 | 31.1512063199 | 206 | 5 | 0 | 32.7 | TDD | 93 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.744 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.761 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.893 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.893 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.640 | NREventA3 | measId:2;ServCellPCI:825;Se... |
| 2024-09-20 22:21:37.880 | NRHandoverAttempt | SourcePCI:825;SourceNR-ARFC... |
| 2024-09-20 22:21:37.925 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.939 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.068 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.068 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274356 | 1 | 7.5422 | 7.0263 | -115.3654 | 9.0174 | 137.8524 | 0.0061 | 0.0023 |
| 2024_09_20 22:00 | 3256543 | 2 | 16.9740 | 9.3556 | -116.0781 | 5.3103 | 154.1610 | 0.0085 | 0.0020 |
| 2024_09_20 22:00 | 3275777 | 3 | 11.7845 | 18.3652 | -117.0692 | 18.4805 | 126.7837 | 0.0063 | 0.0178 |
| 2024_09_20 22:00 | 3271681 | 4 | 18.7237 | 7.1564 | -117.4810 | 8.0914 | 153.3421 | 0.0187 | 0.0022 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414450_2B3EA506 | 504990 | 139 | -92.6 | 504990 | 231 | -98.9 | 504990 | 329 | -102.5 | 504990 | 93 |
| MR_1774414450_7A9F9F1E | 504990 | 139 | -90.4 | 504990 | 231 | -98.2 | 504990 | 329 | -102.8 | 504990 | 93 |
| MR_1774414450_6711F09F | 504990 | 139 | -91.4 | 504990 | 231 | -98.8 | 504990 | 329 | -101.4 | 504990 | 93 |
| MR_1774414450_68C273D3 | 504990 | 139 | -91.0 | 504990 | 231 | -99.2 | 504990 | 329 | -99.5 | 504990 | 93 |
| MR_1774414450_96B73CA3 | 504990 | 139 | -89.7 | 504990 | 231 | -98.6 | 504990 | 329 | -102.4 | 504990 | 93 |
| MR_1774414450_9BB5B5AE | 504990 | 139 | -89.2 | 504990 | 231 | -97.4 | 504990 | 329 | -101.5 | 504990 | 93 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1288: `55339c24-e4b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `55339c24-e4be-4d35-91b5-5454c3a259f5` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1288] topology](images/train_1288.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3265828_3
- `C2`: Press down the tilt angle  of 3265828_3 by 7 degrees
- `C3`: Adjust the azimuth of 3265828_3 by 50 degrees
- `C4`: Increase transmission power for 3265828_3
- `C5`: Add neighbor relationship between 3254511_1 and 3265828_3
- `C6`: Press down the tilt angle of 3212416_2 by 3 degrees
- `C7`: Check test server and transmission issues
- `C8`: Insufficient data; more data is needed for judgment. **← 정답**
- `C9`: Add neighbor relationship between 3212416_2 and 3265828_3
- `C10`: Decrease A3 Offset threshold for 3265828_3
- `C11`: Increase A3 Offset threshold for 3265828_3
- `C12`: Decrease A3 Offset threshold for 3212416_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265828_3
- `C14`: Increase transmission power for 3212416_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212416_2
- `C16`: Decrease transmission power for 3212416_2
- `C17`: Increase A3 Offset threshold for 3212416_2
- `C18`: Lift the tilt angle  of 3265828_3 by 7 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265828_3
- `C20`: Adjust the azimuth of 3212416_2 by 49 degrees
- `C21`: Lift the tilt angle of 3212416_2 by 3 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212416_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.118 | MS1 | 121.4656741404 | 31.1446188424 | 857 | 504990 | -91.23 | 12.58 | 596.65 | 0.17 | 2.88 | 1583 |
| 2024-09-20 22:21:32.483 | MS1 | 121.4656611928 | 31.1446189504 | 857 | 504990 | -90.03 | 14.18 | 350.37 | 0.02 | 2.25 | 1595 |
| 2024-09-20 22:21:33.434 | MS1 | 121.4656611749 | 31.1446234622 | 857 | 504990 | -85.38 | 12.08 | 602.39 | 0.07 | 2.84 | 1588 |
| 2024-09-20 22:21:34.598 | MS1 | 121.4656614954 | 31.1446293266 | 857 | 504990 | -85.02 | 14.55 | 68.96 | 0.08 | 2.81 | 1567 |
| 2024-09-20 22:21:35.258 | MS1 | 121.4656718746 | 31.1446181085 | 857 | 504990 | -87.59 | 13.31 | 90.22 | 0.00 | 2.52 | 1595 |
| 2024-09-20 22:21:36.435 | MS1 | 121.4656599448 | 31.1446203845 | 857 | 504990 | -91.12 | 13.84 | 67.49 | 0.05 | 2.22 | 1590 |
| 2024-09-20 22:21:37.403 | MS1 | 121.4656593274 | 31.1446259294 | 857 | 504990 | -92.08 | 12.94 | 70.42 | 0.12 | 2.96 | 1587 |
| 2024-09-20 22:21:38.152 | MS1 | 121.4656686668 | 31.1446258836 | 857 | 504990 | -93.51 | 7.75 | 77.85 | 0.14 | 2.48 | 1593 |
| 2024-09-20 22:21:39.906 | MS1 | 121.4656711168 | 31.1446333440 | 857 | 504990 | -91.13 | 10.51 | 62.27 | 0.16 | 2.35 | 1575 |
| 2024-09-20 22:21:40.725 | MS1 | 121.4656627970 | 31.1446223611 | 857 | 504990 | -89.35 | 7.87 | 578.77 | 0.15 | 2.69 | 1579 |
| 2024-09-20 22:21:41.208 | MS1 | 121.4656611894 | 31.1446238114 | 857 | 504990 | -91.64 | 10.35 | 357.18 | 0.11 | 2.44 | 1586 |
| 2024-09-20 22:21:42.777 | MS1 | 121.4656611800 | 31.1446240063 | 857 | 504990 | -90.67 | 9.06 | 451.71 | 0.19 | 2.51 | 1600 |

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
| 3212416 | 2 | 121.4640872093 | 31.1533900449 | 122 | 1 | 7 | 36.1 | TDD | 857 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3254511 | 1 | 121.4649673602 | 31.1533851678 | 334 | 1 | 5 | 44.4 | TDD | 680 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3264768 | 4 | 121.4719120546 | 31.1538927533 | 15 | 8 | 1 | 25.2 | TDD | 725 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3265828 | 3 | 121.4707649999 | 31.1519016232 | 70 | 4 | 2 | 44.9 | TDD | 173 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.257 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.280 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.389 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.389 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.102 | NREventA3 | measId:2;ServCellPCI:864;Se... |
| 2024-09-20 22:21:38.342 | NRHandoverAttempt | SourcePCI:864;SourceNR-ARFC... |
| 2024-09-20 22:21:38.384 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.395 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.507 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.507 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3254511 | 1 | 89.6731 | 83.5744 | -117.0405 | 12.8738 | 132.9415 | 0.0116 | 0.0099 |
| 2024_09_19 22:00 | 3212416 | 2 | 90.8895 | 88.7103 | -114.1601 | 11.7879 | 196.0674 | 0.0102 | 0.0162 |
| 2024_09_19 22:00 | 3265828 | 3 | 77.0329 | 92.3401 | -115.0368 | 5.7510 | 96.8277 | 0.0059 | 0.0061 |
| 2024_09_19 22:00 | 3264768 | 4 | 87.8819 | 77.2252 | -115.3764 | 5.2655 | 95.4956 | 0.0090 | 0.0047 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417218_B0AA0DFA | 504990 | 857 | -85.2 | 504990 | 173 | -86.2 | 504990 | 680 | -99.5 | 504990 | 725 |
| MR_1774417218_C37AC7DE | 504990 | 857 | -83.5 | 504990 | 173 | -84.3 | 504990 | 680 | -98.0 | 504990 | 725 |
| MR_1774417218_AAE6F6BA | 504990 | 857 | -86.8 | 504990 | 173 | -85.4 | 504990 | 680 | -99.5 | 504990 | 725 |
| MR_1774417218_BB8B3E6F | 504990 | 857 | -83.2 | 504990 | 173 | -84.7 | 504990 | 680 | -100.6 | 504990 | 725 |
| MR_1774417218_F286CDBF | 504990 | 857 | -84.5 | 504990 | 173 | -83.1 | 504990 | 680 | -97.8 | 504990 | 725 |
| MR_1774417218_A043DDEC | 504990 | 857 | -86.6 | 504990 | 173 | -86.4 | 504990 | 680 | -97.5 | 504990 | 725 |
| MR_1774417218_B21C1C2B | 504990 | 857 | -85.8 | 504990 | 173 | -85.0 | 504990 | 680 | -97.8 | 504990 | 725 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1289: `f8fadb36-af9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f8fadb36-af9e-43cd-81b4-d9f95a7bc645` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1289] topology](images/train_1289.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259699_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257395_1
- `C3`: Decrease A3 Offset threshold for 3257395_1
- `C4`: Insufficient data; more data is needed for judgment. **← 정답**
- `C5`: Press down the tilt angle  of 3259699_4 by 10 degrees
- `C6`: Adjust the azimuth of 3257395_1 by 50 degrees
- `C7`: Add neighbor relationship between 3257395_1 and 3259699_4
- `C8`: Lift the tilt angle  of 3259699_4 by 10 degrees
- `C9`: Check test server and transmission issues
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259699_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257395_1
- `C12`: Increase A3 Offset threshold for 3259699_4
- `C13`: Decrease A3 Offset threshold for 3259699_4
- `C14`: Decrease transmission power for 3259699_4
- `C15`: Adjust the azimuth of 3259699_4 by 50 degrees
- `C16`: Press down the tilt angle of 3257395_1 by 10 degrees
- `C17`: Lift the tilt angle of 3257395_1 by 10 degrees
- `C18`: Add neighbor relationship between 3247141_2 and 3259699_4
- `C19`: Increase transmission power for 3257395_1
- `C20`: Increase transmission power for 3259699_4
- `C21`: Decrease transmission power for 3257395_1
- `C22`: Increase A3 Offset threshold for 3257395_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.803 | MS1 | 121.4656706515 | 31.1446188821 | 240 | 504990 | -87.80 | 12.79 | 520.84 | 0.10 | 2.67 | 1576 |
| 2024-09-20 22:21:32.373 | MS1 | 121.4656617843 | 31.1446339743 | 240 | 504990 | -91.93 | 13.82 | 378.23 | 0.03 | 2.07 | 1560 |
| 2024-09-20 22:21:33.757 | MS1 | 121.4656632942 | 31.1446250128 | 240 | 504990 | -89.99 | 12.35 | 577.82 | 0.05 | 2.62 | 1571 |
| 2024-09-20 22:21:34.497 | MS1 | 121.4656703972 | 31.1446239228 | 240 | 504990 | -87.62 | 14.54 | 84.44 | 0.09 | 2.57 | 1578 |
| 2024-09-20 22:21:35.888 | MS1 | 121.4656765344 | 31.1446267510 | 240 | 504990 | -85.98 | 12.50 | 77.51 | 0.16 | 2.13 | 1580 |
| 2024-09-20 22:21:36.606 | MS1 | 121.4656676120 | 31.1446226362 | 240 | 504990 | -89.83 | 15.03 | 83.26 | 0.14 | 2.84 | 1592 |
| 2024-09-20 22:21:37.808 | MS1 | 121.4656644508 | 31.1446333921 | 240 | 504990 | -89.93 | 9.08 | 80.00 | 0.20 | 2.94 | 1566 |
| 2024-09-20 22:21:38.311 | MS1 | 121.4656647920 | 31.1446220590 | 240 | 504990 | -89.92 | 12.69 | 78.79 | 0.09 | 2.32 | 1590 |
| 2024-09-20 22:21:39.500 | MS1 | 121.4656725105 | 31.1446323927 | 240 | 504990 | -91.96 | 7.39 | 85.73 | 0.07 | 2.78 | 1577 |
| 2024-09-20 22:21:40.927 | MS1 | 121.4656683237 | 31.1446276685 | 240 | 504990 | -90.09 | 9.35 | 591.90 | 0.00 | 2.08 | 1560 |
| 2024-09-20 22:21:41.792 | MS1 | 121.4656745057 | 31.1446292372 | 240 | 504990 | -89.22 | 9.30 | 575.11 | 0.04 | 2.72 | 1595 |
| 2024-09-20 22:21:42.851 | MS1 | 121.4656606445 | 31.1446197103 | 240 | 504990 | -93.94 | 8.79 | 408.31 | 0.15 | 2.19 | 1575 |

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
| 3211229 | 3 | 121.4749165052 | 31.1440843157 | 291 | 7 | 7 | 47.1 | TDD | 876 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3247141 | 2 | 121.4734544848 | 31.1544247558 | 122 | 0 | 1 | 39.8 | TDD | 10 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3257395 | 1 | 121.4644844713 | 31.1466796280 | 358 | 4 | 0 | 31.0 | TDD | 240 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3259699 | 4 | 121.4704868127 | 31.1511587004 | 350 | 11 | 11 | 22.7 | TDD | 645 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.849 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.872 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.979 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.979 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.730 | NREventA3 | measId:2;ServCellPCI:107;Se... |
| 2024-09-20 22:21:37.970 | NRHandoverAttempt | SourcePCI:107;SourceNR-ARFC... |
| 2024-09-20 22:21:38.020 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.033 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.160 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.160 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3257395 | 1 | 85.1320 | 90.6052 | -115.4744 | 16.9634 | 165.5250 | 0.0175 | 0.0121 |
| 2024_09_19 22:00 | 3247141 | 2 | 83.7985 | 75.4587 | -114.2366 | 14.2812 | 157.1762 | 0.0162 | 0.0107 |
| 2024_09_19 22:00 | 3211229 | 3 | 90.7215 | 79.7455 | -114.6688 | 7.5663 | 123.7030 | 0.0125 | 0.0128 |
| 2024_09_19 22:00 | 3259699 | 4 | 94.2266 | 88.3792 | -116.7559 | 5.1022 | 109.0531 | 0.0199 | 0.0123 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414451_A49EC2E2 | 504990 | 240 | -87.6 | 504990 | 645 | -90.1 | 504990 | 10 | -104.5 | 504990 | 876 |
| MR_1774414451_5BB7534C | 504990 | 240 | -88.7 | 504990 | 645 | -89.6 | 504990 | 10 | -104.0 | 504990 | 876 |
| MR_1774414451_250565DA | 504990 | 240 | -86.6 | 504990 | 645 | -90.8 | 504990 | 10 | -103.5 | 504990 | 876 |
| MR_1774414451_9A1A3332 | 504990 | 240 | -89.3 | 504990 | 645 | -91.9 | 504990 | 10 | -100.9 | 504990 | 876 |
| MR_1774414451_CD199E87 | 504990 | 240 | -86.5 | 504990 | 645 | -90.9 | 504990 | 10 | -102.1 | 504990 | 876 |

> *... 2개 열 생략 (전체 14열)*

---
