# Track A 문제 분석 — train[1600]~train[1609]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1600] ~ train[1609] (10개)

## 목차

1. [문제 1600: `98a06428-9c6...`](#1600) — single-answer, 정답: C13
2. [문제 1601: `1e0872e7-992...`](#1601) — single-answer, 정답: C4
3. [문제 1602: `6b66bc95-5f6...`](#1602) — single-answer, 정답: C10
4. [문제 1603: `3da2bd9d-bb6...`](#1603) — single-answer, 정답: C6
5. [문제 1604: `07df0ec4-62b...`](#1604) — single-answer, 정답: C13
6. [문제 1605: `815c1a8e-b79...`](#1605) — multiple-answer, 정답: C3|C6|C9|C19
7. [문제 1606: `cdfd4c97-2a4...`](#1606) — single-answer, 정답: C22
8. [문제 1607: `bfb350b1-dd0...`](#1607) — single-answer, 정답: C22
9. [문제 1608: `0bb3bcc2-7af...`](#1608) — single-answer, 정답: C16
10. [문제 1609: `48b1aabe-b54...`](#1609) — multiple-answer, 정답: C1|C2

---

### 문제 1600: `98a06428-9c6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `98a06428-9c66-4513-892e-d6611110a06c` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease A3 Offset threshold for 3253199_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1600] topology](images/train_1600.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3253199_2
- `C2`: Add neighbor relationship between 3243899_3 and 3240288_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253199_2
- `C4`: Check test server and transmission issues
- `C5`: Lift the tilt angle of 3253199_2 by 6 degrees
- `C6`: Press down the tilt angle of 3253199_2 by 6 degrees
- `C7`: Press down the tilt angle  of 3240288_1 by 2 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase transmission power for 3253199_2
- `C10`: Decrease transmission power for 3253199_2
- `C11`: Increase transmission power for 3240288_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240288_1
- `C13`: Decrease A3 Offset threshold for 3253199_2 **← 정답**
- `C14`: Increase A3 Offset threshold for 3240288_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253199_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240288_1
- `C17`: Decrease transmission power for 3240288_1
- `C18`: Adjust the azimuth of 3253199_2 by 5 degrees
- `C19`: Adjust the azimuth of 3240288_1 by 50 degrees
- `C20`: Lift the tilt angle  of 3240288_1 by 2 degrees
- `C21`: Decrease A3 Offset threshold for 3240288_1
- `C22`: Add neighbor relationship between 3253199_2 and 3240288_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.716 | MS1 | 121.4656658683 | 31.1446199219 | 237 | 504990 | -75.26 | 17.66 | 447.57 | 0.06 | 2.25 | 1578 |
| 2024-09-20 22:21:32.468 | MS1 | 121.4656614111 | 31.1446242676 | 237 | 504990 | -82.73 | 14.75 | 591.88 | 0.14 | 2.48 | 1584 |
| 2024-09-20 22:21:33.741 | MS1 | 121.4656719448 | 31.1446273968 | 237 | 504990 | -83.52 | 15.38 | 361.26 | 0.04 | 2.92 | 1571 |
| 2024-09-20 22:21:34.236 | MS1 | 121.4656681019 | 31.1446336894 | 237 | 504990 | -92.94 | -0.02 | 24.94 | 0.16 | 1.49 | 1596 |
| 2024-09-20 22:21:35.291 | MS1 | 121.4656590693 | 31.1446321704 | 237 | 504990 | -90.63 | -2.57 | 49.52 | 0.14 | 1.30 | 1593 |
| 2024-09-20 22:21:36.785 | MS1 | 121.4656587861 | 31.1446260364 | 237 | 504990 | -85.81 | -2.71 | 48.01 | 0.15 | 1.25 | 1568 |
| 2024-09-20 22:21:37.116 | MS1 | 121.4656712591 | 31.1446222639 | 237 | 504990 | -87.69 | -0.89 | 72.74 | 0.19 | 1.36 | 1577 |
| 2024-09-20 22:21:38.288 | MS1 | 121.4656596290 | 31.1446237677 | 237 | 504990 | -92.04 | -2.77 | 49.15 | 0.19 | 1.30 | 1600 |
| 2024-09-20 22:21:39.938 | MS1 | 121.4656703757 | 31.1446296515 | 284 | 504990 | -75.76 | 16.78 | 174.68 | 0.13 | 1.37 | 1570 |
| 2024-09-20 22:21:40.557 | MS1 | 121.4656623284 | 31.1446347959 | 284 | 504990 | -84.31 | 16.24 | 413.94 | 0.16 | 2.82 | 1577 |
| 2024-09-20 22:21:41.412 | MS1 | 121.4656748871 | 31.1446376807 | 284 | 504990 | -82.69 | 15.42 | 374.29 | 0.13 | 2.51 | 1567 |
| 2024-09-20 22:21:42.354 | MS1 | 121.4656589516 | 31.1446362238 | 284 | 504990 | -82.75 | 13.35 | 300.74 | 0.07 | 2.07 | 1565 |

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
| 3240288 | 1 | 121.4724739495 | 31.1489885567 | 335 | 0 | 12 | 33.2 | TDD | 284 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3243899 | 3 | 121.4682048251 | 31.1445123752 | 327 | 2 | 4 | 32.4 | TDD | 414 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3247739 | 4 | 121.4677192607 | 31.1531405192 | 239 | 14 | 1 | 38.1 | TDD | 510 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3253199 | 2 | 121.4697927605 | 31.1458099717 | 257 | 3 | 4 | 22.6 | TDD | 237 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.151 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.281 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.281 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.000 | NREventA3 | measId:2;ServCellPCI:893;Se... |
| 2024-09-20 22:21:38.240 | NRHandoverAttempt | SourcePCI:893;SourceNR-ARFC... |
| 2024-09-20 22:21:38.282 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.292 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.399 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.399 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240288 | 1 | 14.0042 | 16.4001 | -116.8036 | 9.9666 | 143.5379 | 0.0178 | 0.0094 |
| 2024_09_20 22:00 | 3253199 | 2 | 6.3249 | 9.5125 | -114.9213 | 9.7959 | 163.7918 | 0.0057 | 0.1090 |
| 2024_09_20 22:00 | 3243899 | 3 | 14.5629 | 7.7326 | -115.3947 | 19.4762 | 87.3155 | 0.0112 | 0.0035 |
| 2024_09_20 22:00 | 3247739 | 4 | 6.0991 | 10.4691 | -117.5722 | 9.0905 | 172.3062 | 0.0044 | 0.0015 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416714_1A1E02EE | 504990 | 237 | -94.4 | 504990 | 284 | -88.1 | 504990 | 414 | -86.2 | 504990 | 510 |
| MR_1774416714_6936B9B6 | 504990 | 237 | -91.8 | 504990 | 284 | -87.2 | 504990 | 414 | -86.5 | 504990 | 510 |
| MR_1774416714_C09CF039 | 504990 | 237 | -92.2 | 504990 | 284 | -88.9 | 504990 | 414 | -90.0 | 504990 | 510 |
| MR_1774416714_C960673F | 504990 | 284 | -85.8 | 504990 | 237 | -93.1 | 504990 | 414 | -86.7 | 504990 | 510 |
| MR_1774416714_587AD620 | 504990 | 284 | -88.8 | 504990 | 237 | -92.2 | 504990 | 414 | -90.0 | 504990 | 510 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1601: `1e0872e7-992...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1e0872e7-992c-456e-b9fc-f73278856870` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Lift the tilt angle  of 3274147_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1601] topology](images/train_1601.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3278268_4 by 5 degrees
- `C2`: Lift the tilt angle of 3278268_4 by 5 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262865_2
- `C4`: Lift the tilt angle  of 3274147_3 by 10 degrees **← 정답**
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262865_2
- `C6`: Check test server and transmission issues
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Increase A3 Offset threshold for 3278268_4
- `C9`: Increase A3 Offset threshold for 3262865_2
- `C10`: Decrease transmission power for 3262865_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278268_4
- `C12`: Add neighbor relationship between 3274147_3 and 3262865_2
- `C13`: Adjust the azimuth of 3274147_3 by 50 degrees
- `C14`: Decrease A3 Offset threshold for 3262865_2
- `C15`: Increase transmission power for 3278268_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278268_4
- `C17`: Decrease A3 Offset threshold for 3278268_4
- `C18`: Add neighbor relationship between 3278268_4 and 3262865_2
- `C19`: Decrease transmission power for 3278268_4
- `C20`: Press down the tilt angle  of 3274147_3 by 10 degrees
- `C21`: Increase transmission power for 3262865_2
- `C22`: Adjust the azimuth of 3278268_4 by 14 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.462 | MS1 | 121.4656600210 | 31.1446210358 | 844 | 504990 | -88.80 | 16.49 | 572.72 | 0.18 | 2.68 | 1568 |
| 2024-09-20 22:21:32.847 | MS1 | 121.4656681374 | 31.1446289994 | 844 | 504990 | -87.21 | 15.64 | 436.78 | 0.01 | 2.36 | 1568 |
| 2024-09-20 22:21:33.539 | MS1 | 121.4656763182 | 31.1446349168 | 844 | 504990 | -87.17 | 17.67 | 325.77 | 0.19 | 2.87 | 1574 |
| 2024-09-20 22:21:34.441 | MS1 | 121.4656602035 | 31.1446284329 | 844 | 504990 | -87.82 | 15.83 | 90.60 | 0.15 | 2.65 | 1584 |
| 2024-09-20 22:21:35.732 | MS1 | 121.4656754377 | 31.1446314881 | 844 | 504990 | -88.09 | 17.88 | 96.62 | 0.15 | 2.86 | 1586 |
| 2024-09-20 22:21:36.104 | MS1 | 121.4656634320 | 31.1446182516 | 844 | 504990 | -85.11 | 17.41 | 72.22 | 0.06 | 2.91 | 1561 |
| 2024-09-20 22:21:37.366 | MS1 | 121.4656609610 | 31.1446184545 | 844 | 504990 | -93.00 | 11.12 | 106.65 | 0.06 | 2.31 | 1597 |
| 2024-09-20 22:21:38.717 | MS1 | 121.4656750051 | 31.1446215636 | 844 | 504990 | -92.39 | 10.91 | 64.52 | 0.02 | 2.68 | 1594 |
| 2024-09-20 22:21:39.552 | MS1 | 121.4656591820 | 31.1446341331 | 844 | 504990 | -92.03 | 12.03 | 80.66 | 0.05 | 2.65 | 1573 |
| 2024-09-20 22:21:40.719 | MS1 | 121.4656751301 | 31.1446346195 | 844 | 504990 | -93.93 | 10.81 | 568.78 | 0.01 | 2.45 | 1591 |
| 2024-09-20 22:21:41.172 | MS1 | 121.4656611678 | 31.1446221293 | 844 | 504990 | -92.98 | 8.46 | 587.96 | 0.17 | 2.55 | 1575 |
| 2024-09-20 22:21:42.198 | MS1 | 121.4656768953 | 31.1446200361 | 844 | 504990 | -92.44 | 12.54 | 295.94 | 0.11 | 2.30 | 1573 |

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
| 3262865 | 2 | 121.4727981745 | 31.1509117381 | 300 | 12 | 4 | 28.1 | TDD | 660 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3274147 | 3 | 121.4757109518 | 31.1525200084 | 40 | 3 | 11 | 48.8 | TDD | 588 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3276925 | 1 | 121.4696851602 | 31.1448516980 | 99 | 15 | 9 | 44.2 | TDD | 945 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3278268 | 4 | 121.4755295089 | 31.1531716514 | 239 | 4 | 10 | 29.9 | TDD | 844 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.407 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.427 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.549 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.549 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.243 | NREventA3 | measId:2;ServCellPCI:555;Se... |
| 2024-09-20 22:21:38.483 | NRHandoverAttempt | SourcePCI:555;SourceNR-ARFC... |
| 2024-09-20 22:21:38.531 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.546 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.690 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.690 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276925 | 1 | 9.9579 | 13.9136 | -115.6779 | 18.0156 | 91.7928 | 0.0180 | 0.0145 |
| 2024_09_20 22:00 | 3262865 | 2 | 15.4993 | 9.3085 | -117.1843 | 14.2794 | 169.5528 | 0.0037 | 0.0185 |
| 2024_09_20 22:00 | 3274147 | 3 | 12.8211 | 7.8473 | -115.9789 | 11.8865 | 122.2765 | 0.0199 | 0.0080 |
| 2024_09_20 22:00 | 3278268 | 4 | 81.0439 | 81.9644 | -114.0586 | 12.8319 | 178.8372 | 0.0056 | 0.0007 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412601_49460EB2 | 504990 | 844 | -87.5 | 504990 | 660 | -91.4 | 504990 | 588 | -97.7 | 504990 | 945 |
| MR_1774412601_73A7ED8B | 504990 | 844 | -88.8 | 504990 | 660 | -90.9 | 504990 | 588 | -96.4 | 504990 | 945 |
| MR_1774412601_D40E99E2 | 504990 | 844 | -88.6 | 504990 | 660 | -89.1 | 504990 | 588 | -96.7 | 504990 | 945 |
| MR_1774412601_E8FE99E0 | 504990 | 844 | -88.9 | 504990 | 660 | -91.5 | 504990 | 588 | -96.1 | 504990 | 945 |
| MR_1774412601_4C9963AD | 504990 | 844 | -89.0 | 504990 | 660 | -88.3 | 504990 | 588 | -95.5 | 504990 | 945 |
| MR_1774412601_40D8A4F5 | 504990 | 844 | -87.9 | 504990 | 660 | -91.4 | 504990 | 588 | -94.0 | 504990 | 945 |
| MR_1774412601_1999FDA2 | 504990 | 844 | -88.7 | 504990 | 660 | -91.8 | 504990 | 588 | -96.3 | 504990 | 945 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1602: `6b66bc95-5f6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6b66bc95-5f6d-4d7a-95ac-ba97234e1957` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Add neighbor relationship between 3228933_4 and 3225243_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1602] topology](images/train_1602.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225243_2
- `C2`: Decrease transmission power for 3228933_4
- `C3`: Adjust the azimuth of 3225243_2 by 10 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Add neighbor relationship between 3251823_1 and 3225243_2
- `C6`: Adjust the azimuth of 3228933_4 by 12 degrees
- `C7`: Lift the tilt angle of 3228933_4 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225243_2
- `C9`: Decrease A3 Offset threshold for 3225243_2
- `C10`: Add neighbor relationship between 3228933_4 and 3225243_2 **← 정답**
- `C11`: Press down the tilt angle of 3228933_4 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228933_4
- `C13`: Check test server and transmission issues
- `C14`: Decrease transmission power for 3225243_2
- `C15`: Increase A3 Offset threshold for 3225243_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228933_4
- `C17`: Increase transmission power for 3228933_4
- `C18`: Decrease A3 Offset threshold for 3228933_4
- `C19`: Increase A3 Offset threshold for 3228933_4
- `C20`: Increase transmission power for 3225243_2
- `C21`: Press down the tilt angle  of 3225243_2 by 2 degrees
- `C22`: Lift the tilt angle  of 3225243_2 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.999 | MS1 | 121.4656587626 | 31.1446201607 | 701 | 504990 | -79.28 | 16.95 | 296.86 | 0.07 | 2.49 | 1599 |
| 2024-09-20 22:21:32.123 | MS1 | 121.4656713389 | 31.1446369123 | 701 | 504990 | -77.69 | 13.87 | 530.16 | 0.02 | 2.51 | 1564 |
| 2024-09-20 22:21:33.852 | MS1 | 121.4656758411 | 31.1446316269 | 701 | 504990 | -84.37 | 13.83 | 469.87 | 0.09 | 2.22 | 1575 |
| 2024-09-20 22:21:34.261 | MS1 | 121.4656752632 | 31.1446284811 | 701 | 504990 | -90.97 | -3.21 | 46.34 | 0.14 | 1.22 | 1569 |
| 2024-09-20 22:21:35.528 | MS1 | 121.4656653592 | 31.1446269529 | 701 | 504990 | -91.77 | -1.53 | 46.14 | 0.18 | 1.33 | 1578 |
| 2024-09-20 22:21:36.708 | MS1 | 121.4656677681 | 31.1446368595 | 701 | 504990 | -89.49 | -1.60 | 54.19 | 0.05 | 1.24 | 1569 |
| 2024-09-20 22:21:37.984 | MS1 | 121.4656637667 | 31.1446329828 | 701 | 504990 | -91.06 | -3.28 | 26.01 | 0.08 | 1.40 | 1575 |
| 2024-09-20 22:21:38.667 | MS1 | 121.4656622688 | 31.1446354661 | 701 | 504990 | -82.26 | 17.13 | 494.52 | 0.08 | 1.32 | 1582 |
| 2024-09-20 22:21:39.865 | MS1 | 121.4656582409 | 31.1446249127 | 701 | 504990 | -83.47 | 16.27 | 314.28 | 0.14 | 1.50 | 1592 |
| 2024-09-20 22:21:40.370 | MS1 | 121.4656691036 | 31.1446228883 | 701 | 504990 | -75.01 | 12.39 | 483.94 | 0.19 | 2.76 | 1583 |
| 2024-09-20 22:21:41.800 | MS1 | 121.4656601465 | 31.1446268658 | 701 | 504990 | -84.50 | 14.72 | 550.60 | 0.08 | 2.48 | 1588 |
| 2024-09-20 22:21:42.634 | MS1 | 121.4656587551 | 31.1446269468 | 701 | 504990 | -83.15 | 12.96 | 359.40 | 0.17 | 2.03 | 1585 |

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
| 3217595 | 3 | 121.4712712095 | 31.1479372891 | 334 | 1 | 7 | 30.6 | TDD | 485 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3225243 | 2 | 121.4704557914 | 31.1558538855 | 210 | 1 | 7 | 21.2 | TDD | 375 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3228933 | 4 | 121.4662327118 | 31.1474072773 | 178 | 1 | 11 | 49.5 | TDD | 701 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3251823 | 1 | 121.4679563826 | 31.1528341778 | 21 | 1 | 1 | 34.4 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.052 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.074 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.205 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.205 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.861 | NREventA3 | measId:2;ServCellPCI:435;Se... |
| 2024-09-20 22:21:35.861 | NREventA3 | measId:2;ServCellPCI:435;Se... |
| 2024-09-20 22:21:36.861 | NREventA3 | measId:2;ServCellPCI:435;Se... |
| 2024-09-20 22:21:39.361 | NRRRCReestablishAttempt | PCI:435 |
| 2024-09-20 22:21:39.373 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.386 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.509 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.509 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251823 | 1 | 11.2491 | 9.8304 | -114.2853 | 7.4147 | 199.5122 | 0.0128 | 0.0153 |
| 2024_09_20 22:00 | 3225243 | 2 | 17.3573 | 17.9734 | -115.6497 | 5.4719 | 129.9120 | 0.0121 | 0.0045 |
| 2024_09_20 22:00 | 3217595 | 3 | 6.8251 | 16.0973 | -116.2147 | 18.1697 | 147.0808 | 0.0057 | 0.0110 |
| 2024_09_20 22:00 | 3228933 | 4 | 10.1944 | 5.1857 | -115.6939 | 6.7581 | 107.6665 | 0.0034 | 0.1349 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417034_C010CE37 | 504990 | 375 | -85.6 | 504990 | 701 | -92.3 | 504990 | 866 | -93.0 | 504990 | 485 |
| MR_1774417034_6D8461D3 | 504990 | 701 | -91.6 | 504990 | 375 | -86.6 | 504990 | 866 | -91.6 | 504990 | 485 |
| MR_1774417034_8E8EA7FC | 504990 | 701 | -92.0 | 504990 | 375 | -86.1 | 504990 | 866 | -93.4 | 504990 | 485 |
| MR_1774417034_C9966AA4 | 504990 | 375 | -87.6 | 504990 | 701 | -91.2 | 504990 | 866 | -90.2 | 504990 | 485 |
| MR_1774417034_040A71D4 | 504990 | 375 | -86.6 | 504990 | 701 | -91.3 | 504990 | 866 | -93.2 | 504990 | 485 |
| MR_1774417034_26FC359C | 504990 | 701 | -90.1 | 504990 | 375 | -86.9 | 504990 | 866 | -91.4 | 504990 | 485 |
| MR_1774417034_367F4FA6 | 504990 | 375 | -87.2 | 504990 | 701 | -91.5 | 504990 | 866 | -93.5 | 504990 | 485 |
| MR_1774417034_FC05FF98 | 504990 | 701 | -91.3 | 504990 | 375 | -85.4 | 504990 | 866 | -91.0 | 504990 | 485 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1603: `3da2bd9d-bb6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3da2bd9d-bb6c-4735-9333-42d77fcff97d` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Add neighbor relationship between 3249163_3 and 3231035_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1603] topology](images/train_1603.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3231035_2 by 4 degrees
- `C2`: Adjust the azimuth of 3249163_3 by 24 degrees
- `C3`: Decrease transmission power for 3231035_2
- `C4`: Press down the tilt angle  of 3231035_2 by 4 degrees
- `C5`: Decrease transmission power for 3249163_3
- `C6`: Add neighbor relationship between 3249163_3 and 3231035_2 **← 정답**
- `C7`: Check test server and transmission issues
- `C8`: Press down the tilt angle of 3249163_3 by 10 degrees
- `C9`: Increase A3 Offset threshold for 3249163_3
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase A3 Offset threshold for 3231035_2
- `C12`: Lift the tilt angle of 3249163_3 by 10 degrees
- `C13`: Adjust the azimuth of 3231035_2 by 21 degrees
- `C14`: Increase transmission power for 3231035_2
- `C15`: Add neighbor relationship between 3268769_4 and 3231035_2
- `C16`: Decrease A3 Offset threshold for 3249163_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249163_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231035_2
- `C19`: Increase transmission power for 3249163_3
- `C20`: Decrease A3 Offset threshold for 3231035_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249163_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231035_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.756 | MS1 | 121.4656763277 | 31.1446281980 | 907 | 504990 | -82.67 | 14.51 | 459.53 | 0.01 | 2.43 | 1573 |
| 2024-09-20 22:21:32.749 | MS1 | 121.4656753883 | 31.1446198330 | 907 | 504990 | -76.98 | 16.44 | 527.46 | 0.06 | 2.02 | 1586 |
| 2024-09-20 22:21:33.746 | MS1 | 121.4656687256 | 31.1446206970 | 907 | 504990 | -76.71 | 13.65 | 581.77 | 0.16 | 2.81 | 1600 |
| 2024-09-20 22:21:34.595 | MS1 | 121.4656637476 | 31.1446269335 | 907 | 504990 | -89.46 | -3.04 | 67.16 | 0.10 | 1.45 | 1598 |
| 2024-09-20 22:21:35.908 | MS1 | 121.4656641900 | 31.1446367094 | 907 | 504990 | -90.25 | -3.97 | 60.73 | 0.05 | 1.37 | 1573 |
| 2024-09-20 22:21:36.181 | MS1 | 121.4656732148 | 31.1446323192 | 907 | 504990 | -92.05 | -0.15 | 39.41 | 0.02 | 1.28 | 1568 |
| 2024-09-20 22:21:37.265 | MS1 | 121.4656645648 | 31.1446235644 | 907 | 504990 | -91.70 | -1.42 | 60.62 | 0.08 | 1.24 | 1581 |
| 2024-09-20 22:21:38.923 | MS1 | 121.4656659765 | 31.1446344569 | 907 | 504990 | -79.03 | 14.67 | 586.95 | 0.02 | 1.12 | 1582 |
| 2024-09-20 22:21:39.231 | MS1 | 121.4656620449 | 31.1446310997 | 907 | 504990 | -77.33 | 12.34 | 353.59 | 0.16 | 1.42 | 1590 |
| 2024-09-20 22:21:40.540 | MS1 | 121.4656737220 | 31.1446260828 | 907 | 504990 | -82.36 | 12.56 | 462.16 | 0.05 | 2.88 | 1578 |
| 2024-09-20 22:21:41.335 | MS1 | 121.4656629634 | 31.1446306460 | 907 | 504990 | -77.56 | 14.02 | 333.35 | 0.06 | 2.85 | 1600 |
| 2024-09-20 22:21:42.216 | MS1 | 121.4656777603 | 31.1446254819 | 907 | 504990 | -75.45 | 17.36 | 393.20 | 0.03 | 2.87 | 1579 |

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
| 3231035 | 2 | 121.4747891729 | 31.1465192769 | 235 | 2 | 11 | 25.0 | TDD | 361 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3240130 | 1 | 121.4704036260 | 31.1494033006 | 159 | 12 | 0 | 42.5 | TDD | 928 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3249163 | 3 | 121.4731646915 | 31.1543370599 | 189 | 12 | 0 | 33.4 | TDD | 907 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3268769 | 4 | 121.4740928190 | 31.1443801479 | 164 | 0 | 7 | 30.3 | TDD | 566 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.482 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.505 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.621 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.621 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.379 | NREventA3 | measId:2;ServCellPCI:45;Ser... |
| 2024-09-20 22:21:36.379 | NREventA3 | measId:2;ServCellPCI:45;Ser... |
| 2024-09-20 22:21:37.379 | NREventA3 | measId:2;ServCellPCI:45;Ser... |
| 2024-09-20 22:21:39.879 | NRRRCReestablishAttempt | PCI:45 |
| 2024-09-20 22:21:39.898 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.913 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:40.053 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.053 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240130 | 1 | 6.0222 | 11.0543 | -114.0109 | 14.0168 | 165.1694 | 0.0105 | 0.0150 |
| 2024_09_20 22:00 | 3231035 | 2 | 17.6829 | 11.2378 | -116.0543 | 17.6309 | 132.6906 | 0.0128 | 0.0032 |
| 2024_09_20 22:00 | 3249163 | 3 | 16.2175 | 18.6023 | -117.0514 | 16.1231 | 191.1848 | 0.0076 | 0.1055 |
| 2024_09_20 22:00 | 3268769 | 4 | 18.1221 | 15.3291 | -114.9142 | 16.2772 | 145.5015 | 0.0045 | 0.0070 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414528_AF9AC5E4 | 504990 | 361 | -83.8 | 504990 | 907 | -87.9 | 504990 | 566 | -89.6 | 504990 | 928 |
| MR_1774414528_F42FF1B2 | 504990 | 361 | -85.3 | 504990 | 907 | -89.9 | 504990 | 566 | -89.4 | 504990 | 928 |
| MR_1774414528_EF8DC58D | 504990 | 907 | -88.1 | 504990 | 361 | -81.9 | 504990 | 566 | -91.5 | 504990 | 928 |
| MR_1774414528_0EFE16B5 | 504990 | 907 | -87.9 | 504990 | 361 | -83.2 | 504990 | 566 | -89.5 | 504990 | 928 |
| MR_1774414528_14B2E7A4 | 504990 | 907 | -87.7 | 504990 | 361 | -81.7 | 504990 | 566 | -91.3 | 504990 | 928 |
| MR_1774414528_05EF0E3F | 504990 | 907 | -89.7 | 504990 | 361 | -84.0 | 504990 | 566 | -92.0 | 504990 | 928 |
| MR_1774414528_4CDC4BD4 | 504990 | 907 | -89.0 | 504990 | 361 | -85.5 | 504990 | 566 | -89.8 | 504990 | 928 |
| MR_1774414528_10A93BB7 | 504990 | 907 | -90.8 | 504990 | 361 | -85.2 | 504990 | 566 | -89.0 | 504990 | 928 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1604: `07df0ec4-62b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `07df0ec4-62b2-43db-8fc8-ebab4ddf2b04` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274785_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1604] topology](images/train_1604.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3274785_3 by 5 degrees
- `C2`: Lift the tilt angle  of 3229574_1 by 3 degrees
- `C3`: Decrease A3 Offset threshold for 3274785_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274785_3
- `C5`: Press down the tilt angle  of 3229574_1 by 3 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Add neighbor relationship between 3274785_3 and 3229574_1
- `C8`: Decrease transmission power for 3229574_1
- `C9`: Press down the tilt angle of 3274785_3 by 5 degrees
- `C10`: Increase A3 Offset threshold for 3274785_3
- `C11`: Increase transmission power for 3274785_3
- `C12`: Increase A3 Offset threshold for 3229574_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274785_3 **← 정답**
- `C14`: Check test server and transmission issues
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229574_1
- `C16`: Adjust the azimuth of 3274785_3 by 16 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229574_1
- `C18`: Decrease A3 Offset threshold for 3229574_1
- `C19`: Decrease transmission power for 3274785_3
- `C20`: Increase transmission power for 3229574_1
- `C21`: Adjust the azimuth of 3229574_1 by 25 degrees
- `C22`: Add neighbor relationship between 3275912_11 and 3229574_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.263 | MS1 | 121.4656665547 | 31.1446368497 | 14 | 504990 | -95.59 | 9.93 | 456.23 | 0.17 | 2.94 | 1575 |
| 2024-09-20 22:21:32.142 | MS1 | 121.4656772560 | 31.1446297216 | 251 | 504990 | -95.57 | 12.67 | 453.85 | 0.02 | 2.86 | 1577 |
| 2024-09-20 22:21:33.593 | MS1 | 121.4656763200 | 31.1446318687 | 472 | 504990 | -93.17 | 9.79 | 548.56 | 0.09 | 2.59 | 1567 |
| 2024-09-20 22:21:34.179 | MS1 | 121.4656774007 | 31.1446338436 | 407 | 152650 | -93.11 | 3.00 | 48.38 | 0.12 | 1.70 | 946 |
| 2024-09-20 22:21:35.619 | MS1 | 121.4656693325 | 31.1446336003 | 619 | 152650 | -89.84 | 2.21 | 100.38 | 0.16 | 1.52 | 960 |
| 2024-09-20 22:21:36.626 | MS1 | 121.4656595277 | 31.1446352307 | 314 | 152650 | -93.90 | 5.39 | 101.18 | 0.08 | 1.56 | 939 |
| 2024-09-20 22:21:37.118 | MS1 | 121.4656642041 | 31.1446197343 | 765 | 152650 | -90.70 | 3.65 | 62.63 | 0.11 | 1.64 | 909 |
| 2024-09-20 22:21:38.458 | MS1 | 121.4656629111 | 31.1446340232 | 407 | 152650 | -87.99 | 6.72 | 107.38 | 0.07 | 1.99 | 912 |
| 2024-09-20 22:21:39.900 | MS1 | 121.4656601035 | 31.1446195320 | 619 | 152650 | -88.92 | 5.12 | 55.98 | 0.02 | 1.54 | 982 |
| 2024-09-20 22:21:40.847 | MS1 | 121.4656750158 | 31.1446202428 | 314 | 152650 | -92.71 | 2.83 | 76.18 | 0.18 | 2.57 | 1586 |
| 2024-09-20 22:21:41.498 | MS1 | 121.4656723121 | 31.1446189777 | 765 | 152650 | -89.97 | 4.89 | 79.06 | 0.01 | 2.35 | 1564 |
| 2024-09-20 22:21:42.526 | MS1 | 121.4656703946 | 31.1446329726 | 407 | 152650 | -91.73 | 6.07 | 69.07 | 0.19 | 2.24 | 1562 |

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
| 3215140 | 12 | 121.4678113828 | 31.1491519850 | 164 | 2 | 12 | 1.5 | FDD | 765 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3220166 | 7 | 121.4711301637 | 31.1505824030 | 46 | 7 | 0 | 8.0 | FDD | 705 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3229574 | 1 | 121.4640738398 | 31.1444369635 | 107 | 0 | 4 | 9.1 | TDD | 68 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3229796 | 9 | 121.4741453165 | 31.1485993097 | 206 | 8 | 11 | 5.6 | FDD | 561 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3234899 | 5 | 121.4713487892 | 31.1517840978 | 139 | 9 | 1 | 18.6 | TDD | 251 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3244700 | 8 | 121.4689216765 | 31.1465188893 | 347 | 7 | 11 | 6.0 | FDD | 619 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3245920 | 6 | 121.4739883260 | 31.1443938613 | 4 | 15 | 5 | 6.8 | TDD | 413 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3246264 | 4 | 121.4705145922 | 31.1461557133 | 0 | 7 | 5 | 18.8 | TDD | 472 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3259929 | 13 | 121.4736327300 | 31.1473190473 | 23 | 5 | 11 | 15.9 | FDD | 606 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3265755 | 10 | 121.4674101928 | 31.1525004841 | 347 | 4 | 0 | 8.6 | FDD | 407 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3267646 | 2 | 121.4670623162 | 31.1494438697 | 304 | 5 | 2 | 16.5 | TDD | 109 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3274785 | 3 | 121.4702552571 | 31.1540666877 | 219 | 4 | 8 | 25.4 | TDD | 14 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3275912 | 11 | 121.4723864601 | 31.1452087128 | 251 | 12 | 6 | 9.2 | FDD | 314 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |

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
| 2024-09-20 22:21:31.193 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.209 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.351 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.351 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.025 | NREventA2 | measId:1;ServCellPCI:568;Se... |
| 2024-09-20 22:21:35.149 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.430 | NREventA5 | measId:3;ServCellPCI:568;Se... |
| 2024-09-20 22:21:35.493 | NRHandoverAttempt | SourcePCI:568;SourceNR-ARFC... |
| 2024-09-20 22:21:35.528 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.538 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.655 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.655 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229574 | 1 | 16.9136 | 14.4546 | -114.4338 | 9.4149 | 158.0903 | 0.0097 | 0.0159 |
| 2024_09_20 22:00 | 3267646 | 2 | 16.2053 | 17.7582 | -117.3522 | 6.8281 | 95.2069 | 0.0060 | 0.0070 |
| 2024_09_20 22:00 | 3274785 | 3 | 10.3652 | 14.0951 | -114.5266 | 9.8719 | 199.3287 | 0.0151 | 0.0019 |
| 2024_09_20 22:00 | 3246264 | 4 | 18.4106 | 17.9394 | -114.2906 | 13.6418 | 131.7633 | 0.0042 | 0.0097 |
| 2024_09_20 22:00 | 3234899 | 5 | 5.1153 | 16.7181 | -116.8639 | 9.8882 | 82.8719 | 0.0111 | 0.0043 |
| 2024_09_20 22:00 | 3245920 | 6 | 14.2525 | 19.0459 | -116.3200 | 17.1960 | 168.0690 | 0.0180 | 0.0100 |
| 2024_09_20 22:00 | 3220166 | 7 | 13.6598 | 9.7671 | -116.3459 | 3.1871 | 28.3014 | 0.0116 | 0.0106 |
| 2024_09_20 22:00 | 3244700 | 8 | 8.9508 | 19.1553 | -116.9098 | 4.5863 | 52.1948 | 0.0086 | 0.0010 |
| 2024_09_20 22:00 | 3229796 | 9 | 10.0756 | 6.6875 | -116.8296 | 3.3140 | 56.1434 | 0.0197 | 0.0126 |
| 2024_09_20 22:00 | 3265755 | 10 | 18.9461 | 9.2824 | -116.6597 | 4.4913 | 29.5579 | 0.0026 | 0.0101 |
| 2024_09_20 22:00 | 3275912 | 11 | 10.2557 | 5.1568 | -117.7647 | 4.2193 | 41.8296 | 0.0180 | 0.0027 |
| 2024_09_20 22:00 | 3215140 | 12 | 17.5283 | 17.0893 | -115.5950 | 4.1529 | 21.0118 | 0.0176 | 0.0070 |
| 2024_09_20 22:00 | 3259929 | 13 | 18.9980 | 6.3735 | -117.7971 | 3.6415 | 53.2367 | 0.0144 | 0.0026 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415643_25D0AA9F | 152650 | 407 | -92.8 | 152650 | 705 | -98.2 | 152650 | 606 | -102.2 | 152650 | 561 |
| MR_1774415643_F7B24F54 | 504990 | 472 | -92.7 | 504990 | 68 | -92.1 | 504990 | 109 | -92.8 | 504990 | 413 |
| MR_1774415643_84EDB056 | 504990 | 472 | -94.6 | 504990 | 68 | -90.0 | 504990 | 109 | -92.5 | 504990 | 413 |
| MR_1774415643_5466B75D | 504990 | 472 | -94.2 | 504990 | 68 | -90.3 | 504990 | 109 | -90.2 | 504990 | 413 |
| MR_1774415643_5C1DF9F8 | 152650 | 407 | -92.0 | 152650 | 705 | -97.1 | 152650 | 606 | -103.0 | 152650 | 561 |
| MR_1774415643_28BEC83A | 504990 | 472 | -93.3 | 504990 | 68 | -90.6 | 504990 | 109 | -92.8 | 504990 | 413 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1605: `815c1a8e-b79...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `815c1a8e-b795-453c-b8e8-d8b4e21bf75a` |
| Tag | **multiple-answer** |
| 정답 | **C3|C6|C9|C19** |
| C3 의미 | Press down the tilt angle  of 3268530_4 by 4 degrees |
| C6 의미 | Increase A3 Offset threshold for 3218188_5 |
| C9 의미 | Decrease transmission power for 3268530_4 |
| C19 의미 | Increase A3 Offset threshold for 3268530_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1605] topology](images/train_1605.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3268530_4 by 4 degrees
- `C2`: Add neighbor relationship between 3218188_5 and 3268530_4
- `C3`: Press down the tilt angle  of 3268530_4 by 4 degrees **← 정답**
- `C4`: Increase transmission power for 3268530_4
- `C5`: Decrease A3 Offset threshold for 3218188_5
- `C6`: Increase A3 Offset threshold for 3218188_5 **← 정답**
- `C7`: Adjust the azimuth of 3268530_4 by 8 degrees
- `C8`: Lift the tilt angle of 3218188_5 by 5 degrees
- `C9`: Decrease transmission power for 3268530_4 **← 정답**
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218188_5
- `C11`: Decrease transmission power for 3218188_5
- `C12`: Adjust the azimuth of 3218188_5 by 35 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Add neighbor relationship between 3267409_1 and 3268530_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268530_4
- `C16`: Increase transmission power for 3218188_5
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268530_4
- `C18`: Decrease A3 Offset threshold for 3268530_4
- `C19`: Increase A3 Offset threshold for 3268530_4 **← 정답**
- `C20`: Press down the tilt angle of 3218188_5 by 5 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218188_5
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.413 | MS1 | 121.4656612514 | 31.1446330908 | 508 | 504990 | -83.44 | 15.26 | 532.97 | 0.06 | 2.40 | 1592 |
| 2024-09-20 22:21:32.401 | MS1 | 121.4656667040 | 31.1446373470 | 508 | 504990 | -84.06 | 16.56 | 438.05 | 0.06 | 2.85 | 1595 |
| 2024-09-20 22:21:33.248 | MS1 | 121.4656695066 | 31.1446269732 | 508 | 504990 | -79.08 | 14.60 | 592.82 | 0.04 | 2.70 | 1600 |
| 2024-09-20 22:21:34.681 | MS1 | 121.4656726209 | 31.1446325862 | 463 | 504990 | -80.91 | 1.55 | 48.94 | 0.17 | 1.28 | 1569 |
| 2024-09-20 22:21:35.215 | MS1 | 121.4656757142 | 31.1446226740 | 463 | 504990 | -88.59 | 1.00 | 62.03 | 0.14 | 1.27 | 1593 |
| 2024-09-20 22:21:36.999 | MS1 | 121.4656680222 | 31.1446324159 | 508 | 504990 | -85.46 | 1.40 | 50.16 | 0.14 | 1.09 | 1586 |
| 2024-09-20 22:21:37.505 | MS1 | 121.4656625288 | 31.1446361469 | 508 | 504990 | -83.46 | 2.06 | 54.95 | 0.14 | 1.46 | 1580 |
| 2024-09-20 22:21:38.177 | MS1 | 121.4656643697 | 31.1446251830 | 463 | 504990 | -83.41 | 1.68 | 41.39 | 0.08 | 1.47 | 1565 |
| 2024-09-20 22:21:39.672 | MS1 | 121.4656668325 | 31.1446273030 | 463 | 504990 | -85.35 | 2.07 | 47.49 | 0.10 | 1.18 | 1576 |
| 2024-09-20 22:21:40.323 | MS1 | 121.4656581012 | 31.1446327093 | 463 | 504990 | -84.98 | 16.26 | 351.59 | 0.04 | 2.72 | 1575 |
| 2024-09-20 22:21:41.624 | MS1 | 121.4656705038 | 31.1446336987 | 463 | 504990 | -79.28 | 17.71 | 382.50 | 0.19 | 2.40 | 1560 |
| 2024-09-20 22:21:42.877 | MS1 | 121.4656690433 | 31.1446240493 | 463 | 504990 | -81.10 | 15.94 | 394.96 | 0.13 | 2.93 | 1593 |

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
| 3215319 | 3 | 121.4694669519 | 31.1489076130 | 250 | 5 | 8 | 34.0 | TDD | 273 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3218188 | 5 | 121.4756444071 | 31.1443768477 | 307 | 2 | 6 | 49.3 | TDD | 508 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3256642 | 2 | 121.4738440320 | 31.1451100152 | 261 | 6 | 6 | 30.0 | TDD | 463 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3267409 | 1 | 121.4745411202 | 31.1451551223 | 338 | 6 | 9 | 28.4 | TDD | 668 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3268530 | 4 | 121.4687656695 | 31.1508615984 | 195 | 2 | 12 | 24.3 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.147 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.167 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.277 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.277 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.030 | NREventA3 | measId:2;ServCellPCI:525;Se... |
| 2024-09-20 22:21:34.270 | NRHandoverAttempt | SourcePCI:525;SourceNR-ARFC... |
| 2024-09-20 22:21:34.316 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.330 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:34.463 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.463 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.030 | NREventA3 | measId:2;ServCellPCI:635;Se... |
| 2024-09-20 22:21:36.270 | NRHandoverAttempt | SourcePCI:635;SourceNR-ARFC... |
| 2024-09-20 22:21:36.316 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.329 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.472 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.472 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.030 | NREventA3 | measId:2;ServCellPCI:525;Se... |
| 2024-09-20 22:21:38.270 | NRHandoverAttempt | SourcePCI:525;SourceNR-ARFC... |
| 2024-09-20 22:21:38.316 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.331 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.450 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.450 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267409 | 1 | 11.9989 | 14.9153 | -116.7356 | 13.3048 | 191.1979 | 0.0173 | 0.0169 |
| 2024_09_20 22:00 | 3256642 | 2 | 12.8644 | 13.7420 | -117.4077 | 17.0715 | 198.6267 | 0.0029 | 0.0129 |
| 2024_09_20 22:00 | 3215319 | 3 | 9.5685 | 14.5146 | -117.4076 | 8.4908 | 177.3910 | 0.0003 | 0.0081 |
| 2024_09_20 22:00 | 3268530 | 4 | 16.6056 | 8.4526 | -116.6717 | 19.6614 | 134.2511 | 0.0094 | 0.0018 |
| 2024_09_20 22:00 | 3218188 | 5 | 12.5516 | 11.1380 | -117.7969 | 17.3276 | 175.1803 | 0.0149 | 0.0081 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413188_A8267903 | 504990 | 508 | -79.6 | 504990 | 463 | -81.6 | 504990 | 248 | -85.7 | 504990 | 668 |
| MR_1774413188_B1E3CA8A | 504990 | 463 | -80.4 | 504990 | 508 | -83.7 | 504990 | 248 | -83.9 | 504990 | 668 |
| MR_1774413188_D19EDAE9 | 504990 | 508 | -82.2 | 504990 | 463 | -82.5 | 504990 | 248 | -84.3 | 504990 | 668 |
| MR_1774413188_6B3E9A32 | 504990 | 508 | -81.5 | 504990 | 463 | -83.3 | 504990 | 248 | -85.3 | 504990 | 668 |
| MR_1774413188_8A271EF1 | 504990 | 463 | -82.8 | 504990 | 508 | -82.5 | 504990 | 248 | -86.2 | 504990 | 668 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1606: `cdfd4c97-2a4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cdfd4c97-2a4c-401c-9852-da49abc1e0fc` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271449_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1606] topology](images/train_1606.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3262599_6
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262599_6
- `C3`: Press down the tilt angle of 3271449_1 by 5 degrees
- `C4`: Decrease A3 Offset threshold for 3262599_6
- `C5`: Check test server and transmission issues
- `C6`: Lift the tilt angle  of 3262599_6 by 4 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271449_1
- `C8`: Decrease transmission power for 3271449_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262599_6
- `C10`: Adjust the azimuth of 3271449_1 by 24 degrees
- `C11`: Lift the tilt angle of 3271449_1 by 5 degrees
- `C12`: Decrease A3 Offset threshold for 3271449_1
- `C13`: Decrease transmission power for 3262599_6
- `C14`: Press down the tilt angle  of 3262599_6 by 4 degrees
- `C15`: Increase A3 Offset threshold for 3271449_1
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase transmission power for 3271449_1
- `C18`: Adjust the azimuth of 3262599_6 by 23 degrees
- `C19`: Add neighbor relationship between 3271449_1 and 3262599_6
- `C20`: Add neighbor relationship between 3225085_13 and 3262599_6
- `C21`: Increase A3 Offset threshold for 3262599_6
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271449_1 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.607 | MS1 | 121.4656638323 | 31.1446270578 | 33 | 504990 | -95.22 | 14.79 | 431.45 | 0.15 | 2.49 | 1597 |
| 2024-09-20 22:21:32.727 | MS1 | 121.4656768473 | 31.1446213994 | 306 | 504990 | -95.28 | 9.44 | 534.31 | 0.11 | 2.01 | 1574 |
| 2024-09-20 22:21:33.210 | MS1 | 121.4656759548 | 31.1446294168 | 330 | 504990 | -95.28 | 12.55 | 512.53 | 0.00 | 2.51 | 1576 |
| 2024-09-20 22:21:34.674 | MS1 | 121.4656676744 | 31.1446327895 | 736 | 152650 | -92.24 | 2.18 | 68.95 | 0.05 | 1.96 | 996 |
| 2024-09-20 22:21:35.959 | MS1 | 121.4656653963 | 31.1446308414 | 469 | 152650 | -91.57 | 4.35 | 65.82 | 0.08 | 1.65 | 981 |
| 2024-09-20 22:21:36.467 | MS1 | 121.4656653813 | 31.1446307837 | 119 | 152650 | -88.60 | 4.05 | 71.75 | 0.19 | 1.64 | 950 |
| 2024-09-20 22:21:37.464 | MS1 | 121.4656660873 | 31.1446210112 | 688 | 152650 | -92.39 | 3.15 | 95.45 | 0.15 | 1.50 | 962 |
| 2024-09-20 22:21:38.818 | MS1 | 121.4656709275 | 31.1446209108 | 736 | 152650 | -89.88 | 4.23 | 86.63 | 0.10 | 1.80 | 923 |
| 2024-09-20 22:21:39.764 | MS1 | 121.4656728986 | 31.1446352205 | 469 | 152650 | -94.11 | 4.64 | 61.97 | 0.06 | 1.64 | 993 |
| 2024-09-20 22:21:40.204 | MS1 | 121.4656735873 | 31.1446194305 | 119 | 152650 | -94.11 | 7.15 | 59.38 | 0.06 | 2.99 | 1576 |
| 2024-09-20 22:21:41.876 | MS1 | 121.4656648993 | 31.1446184750 | 688 | 152650 | -89.22 | 7.92 | 85.25 | 0.10 | 2.71 | 1562 |
| 2024-09-20 22:21:42.872 | MS1 | 121.4656701806 | 31.1446207909 | 736 | 152650 | -90.08 | 5.12 | 55.81 | 0.19 | 2.92 | 1560 |

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
| 3210772 | 8 | 121.4664067378 | 31.1532205095 | 166 | 3 | 12 | 20.5 | FDD | 289 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3211561 | 10 | 121.4690023462 | 31.1449513121 | 324 | 14 | 5 | 25.5 | FDD | 141 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3217474 | 3 | 121.4711000558 | 31.1542383729 | 353 | 0 | 12 | 20.2 | TDD | 330 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3220760 | 9 | 121.4707505305 | 31.1491856154 | 300 | 2 | 12 | 13.2 | FDD | 135 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3225085 | 13 | 121.4659363634 | 31.1554052090 | 248 | 5 | 6 | 16.7 | FDD | 119 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3226334 | 11 | 121.4681490203 | 31.1461019889 | 148 | 10 | 9 | 18.5 | FDD | 688 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3229363 | 7 | 121.4651565031 | 31.1489628965 | 22 | 1 | 1 | 0.3 | FDD | 736 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3242769 | 2 | 121.4727686656 | 31.1485677845 | 352 | 11 | 11 | 26.9 | TDD | 103 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3246166 | 12 | 121.4710394973 | 31.1550046991 | 274 | 9 | 10 | 5.4 | FDD | 469 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3248345 | 5 | 121.4724017859 | 31.1502671381 | 24 | 8 | 1 | 16.2 | TDD | 306 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3252612 | 4 | 121.4686136038 | 31.1444508206 | 142 | 12 | 0 | 24.8 | TDD | 427 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3262599 | 6 | 121.4726926413 | 31.1504786658 | 249 | 3 | 11 | 18.2 | TDD | 350 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3271449 | 1 | 121.4727565120 | 31.1487280418 | 212 | 4 | 10 | 19.2 | TDD | 33 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.606 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.630 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.754 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.754 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.495 | NREventA2 | measId:1;ServCellPCI:106;Se... |
| 2024-09-20 22:21:35.624 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.901 | NREventA5 | measId:3;ServCellPCI:106;Se... |
| 2024-09-20 22:21:35.947 | NRHandoverAttempt | SourcePCI:106;SourceNR-ARFC... |
| 2024-09-20 22:21:35.979 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.992 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.140 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.140 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271449 | 1 | 19.5118 | 12.9159 | -117.2361 | 14.9640 | 96.0382 | 0.0198 | 0.0010 |
| 2024_09_20 22:00 | 3242769 | 2 | 17.2979 | 14.7082 | -116.3506 | 16.0248 | 90.0177 | 0.0027 | 0.0104 |
| 2024_09_20 22:00 | 3217474 | 3 | 14.5107 | 6.8870 | -116.6516 | 13.1879 | 199.2333 | 0.0141 | 0.0012 |
| 2024_09_20 22:00 | 3252612 | 4 | 14.9745 | 16.6136 | -114.1263 | 6.8393 | 142.8025 | 0.0195 | 0.0151 |
| 2024_09_20 22:00 | 3248345 | 5 | 18.1727 | 13.8690 | -114.5879 | 17.2408 | 85.5614 | 0.0124 | 0.0093 |
| 2024_09_20 22:00 | 3262599 | 6 | 10.6439 | 6.5064 | -115.4450 | 11.4334 | 90.8203 | 0.0190 | 0.0089 |
| 2024_09_20 22:00 | 3229363 | 7 | 5.2762 | 16.2233 | -115.3039 | 3.5905 | 50.4512 | 0.0156 | 0.0100 |
| 2024_09_20 22:00 | 3210772 | 8 | 5.2027 | 18.0925 | -115.0768 | 3.7091 | 24.2505 | 0.0055 | 0.0121 |
| 2024_09_20 22:00 | 3220760 | 9 | 15.7954 | 6.9999 | -116.7626 | 4.2177 | 25.7721 | 0.0015 | 0.0010 |
| 2024_09_20 22:00 | 3211561 | 10 | 10.6750 | 17.6791 | -117.5149 | 3.4820 | 40.7615 | 0.0030 | 0.0033 |
| 2024_09_20 22:00 | 3226334 | 11 | 6.0658 | 10.8971 | -116.9686 | 4.2007 | 57.4255 | 0.0177 | 0.0070 |
| 2024_09_20 22:00 | 3246166 | 12 | 9.7926 | 6.0925 | -117.7351 | 3.0492 | 58.8707 | 0.0172 | 0.0015 |
| 2024_09_20 22:00 | 3225085 | 13 | 18.3870 | 7.9682 | -115.2769 | 4.7005 | 38.9080 | 0.0048 | 0.0049 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414094_E322728C | 152650 | 736 | -90.8 | 152650 | 135 | -97.7 | 152650 | 289 | -99.1 | 152650 | 141 |
| MR_1774414094_1B8E8002 | 152650 | 736 | -92.2 | 152650 | 135 | -98.8 | 152650 | 289 | -99.0 | 152650 | 141 |
| MR_1774414094_3B2B5CD2 | 504990 | 330 | -93.8 | 504990 | 350 | -95.6 | 504990 | 103 | -100.5 | 504990 | 427 |
| MR_1774414094_DE449A04 | 152650 | 736 | -92.8 | 152650 | 135 | -99.6 | 152650 | 289 | -99.8 | 152650 | 141 |
| MR_1774414094_2950E16E | 152650 | 736 | -92.8 | 152650 | 135 | -99.2 | 152650 | 289 | -98.4 | 152650 | 141 |
| MR_1774414094_F6C76723 | 504990 | 330 | -94.4 | 504990 | 350 | -93.5 | 504990 | 103 | -100.1 | 504990 | 427 |
| MR_1774414094_B3747BBE | 152650 | 736 | -92.9 | 152650 | 135 | -98.5 | 152650 | 289 | -100.4 | 152650 | 141 |
| MR_1774414094_3C5A20D5 | 504990 | 330 | -95.1 | 504990 | 350 | -93.5 | 504990 | 103 | -97.6 | 504990 | 427 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1607: `bfb350b1-dd0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bfb350b1-dd0c-4619-a286-c3611b15cd08` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1607] topology](images/train_1607.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258455_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258455_3
- `C3`: Increase A3 Offset threshold for 3221673_2
- `C4`: Add neighbor relationship between 3263488_1 and 3221673_2
- `C5`: Lift the tilt angle  of 3221673_2 by 10 degrees
- `C6`: Decrease A3 Offset threshold for 3221673_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221673_2
- `C8`: Adjust the azimuth of 3258455_3 by 50 degrees
- `C9`: Decrease A3 Offset threshold for 3258455_3
- `C10`: Press down the tilt angle of 3258455_3 by 10 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221673_2
- `C12`: Decrease transmission power for 3221673_2
- `C13`: Press down the tilt angle  of 3221673_2 by 10 degrees
- `C14`: Increase A3 Offset threshold for 3258455_3
- `C15`: Decrease transmission power for 3258455_3
- `C16`: Adjust the azimuth of 3221673_2 by 50 degrees
- `C17`: Increase transmission power for 3258455_3
- `C18`: Lift the tilt angle of 3258455_3 by 10 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase transmission power for 3221673_2
- `C21`: Add neighbor relationship between 3258455_3 and 3221673_2
- `C22`: Check test server and transmission issues **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.321 | MS1 | 121.4656701330 | 31.1446202023 | 79 | 504990 | -88.39 | 14.70 | 509.34 | 0.17 | 2.35 | 1588 |
| 2024-09-20 22:21:32.414 | MS1 | 121.4656583870 | 31.1446357474 | 79 | 504990 | -91.67 | 15.80 | 488.79 | 0.17 | 2.59 | 1569 |
| 2024-09-20 22:21:33.139 | MS1 | 121.4656587535 | 31.1446361144 | 79 | 504990 | -90.64 | 17.36 | 470.86 | 0.14 | 2.63 | 1579 |
| 2024-09-20 22:21:34.915 | MS1 | 121.4656613133 | 31.1446338624 | 79 | 504990 | -91.68 | 16.00 | 77.60 | 0.12 | 2.61 | 351 |
| 2024-09-20 22:21:35.995 | MS1 | 121.4656646039 | 31.1446349020 | 79 | 504990 | -89.03 | 17.46 | 66.61 | 0.05 | 2.40 | 355 |
| 2024-09-20 22:21:36.754 | MS1 | 121.4656603136 | 31.1446376607 | 79 | 504990 | -90.98 | 13.01 | 58.82 | 0.07 | 2.54 | 494 |
| 2024-09-20 22:21:37.169 | MS1 | 121.4656740984 | 31.1446182779 | 79 | 504990 | -89.99 | 9.79 | 63.79 | 0.18 | 2.26 | 397 |
| 2024-09-20 22:21:38.992 | MS1 | 121.4656650086 | 31.1446230917 | 79 | 504990 | -90.24 | 8.61 | 59.22 | 0.18 | 3.00 | 457 |
| 2024-09-20 22:21:39.226 | MS1 | 121.4656742728 | 31.1446368806 | 79 | 504990 | -89.16 | 9.10 | 96.21 | 0.09 | 2.94 | 396 |
| 2024-09-20 22:21:40.390 | MS1 | 121.4656603303 | 31.1446270779 | 79 | 504990 | -92.93 | 12.63 | 575.85 | 0.00 | 2.89 | 1578 |
| 2024-09-20 22:21:41.743 | MS1 | 121.4656732295 | 31.1446374993 | 79 | 504990 | -93.53 | 8.66 | 573.01 | 0.16 | 2.50 | 1594 |
| 2024-09-20 22:21:42.402 | MS1 | 121.4656695135 | 31.1446304071 | 79 | 504990 | -93.75 | 8.61 | 303.70 | 0.12 | 2.42 | 1566 |

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
| 3221673 | 2 | 121.4712834175 | 31.1517479386 | 3 | 13 | 10 | 17.4 | TDD | 595 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3231895 | 4 | 121.4757673516 | 31.1511395630 | 248 | 14 | 0 | 24.0 | TDD | 569 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3258455 | 3 | 121.4668791886 | 31.1489961929 | 286 | 9 | 9 | 25.2 | TDD | 79 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3263488 | 1 | 121.4670920485 | 31.1450574638 | 124 | 1 | 10 | 44.8 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.975 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.000 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.135 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.135 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.844 | NREventA3 | measId:2;ServCellPCI:572;Se... |
| 2024-09-20 22:21:38.084 | NRHandoverAttempt | SourcePCI:572;SourceNR-ARFC... |
| 2024-09-20 22:21:38.128 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.141 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.276 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.276 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263488 | 1 | 7.9313 | 7.6849 | -117.9171 | 10.2200 | 149.6156 | 0.0006 | 0.0049 |
| 2024_09_20 22:00 | 3221673 | 2 | 6.7935 | 12.4029 | -115.7566 | 5.0818 | 89.4125 | 0.0185 | 0.0065 |
| 2024_09_20 22:00 | 3258455 | 3 | 12.3564 | 5.9964 | -114.9384 | 11.6569 | 195.0260 | 0.0166 | 0.0051 |
| 2024_09_20 22:00 | 3231895 | 4 | 5.4909 | 7.1383 | -115.7288 | 10.6467 | 174.8705 | 0.0137 | 0.0148 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412822_45F9FEB6 | 504990 | 79 | -93.5 | 504990 | 595 | -98.8 | 504990 | 441 | -103.2 | 504990 | 569 |
| MR_1774412822_5588E365 | 504990 | 79 | -93.2 | 504990 | 595 | -99.2 | 504990 | 441 | -105.6 | 504990 | 569 |
| MR_1774412822_99A7D650 | 504990 | 79 | -93.4 | 504990 | 595 | -99.5 | 504990 | 441 | -105.4 | 504990 | 569 |
| MR_1774412822_0F82C406 | 504990 | 79 | -91.5 | 504990 | 595 | -100.5 | 504990 | 441 | -104.0 | 504990 | 569 |
| MR_1774412822_D40B5361 | 504990 | 79 | -92.3 | 504990 | 595 | -97.1 | 504990 | 441 | -103.1 | 504990 | 569 |
| MR_1774412822_27476B4A | 504990 | 79 | -89.8 | 504990 | 595 | -99.0 | 504990 | 441 | -104.8 | 504990 | 569 |
| MR_1774412822_545FF657 | 504990 | 79 | -89.8 | 504990 | 595 | -98.4 | 504990 | 441 | -102.8 | 504990 | 569 |
| MR_1774412822_0A8609C1 | 504990 | 79 | -93.0 | 504990 | 595 | -99.6 | 504990 | 441 | -106.2 | 504990 | 569 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1608: `0bb3bcc2-7af...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0bb3bcc2-7af0-4326-aa30-52e3fb9dc3d5` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1608] topology](images/train_1608.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3267284_1
- `C2`: Adjust the azimuth of 3250742_2 by 50 degrees
- `C3`: Add neighbor relationship between 3267284_1 and 3250742_2
- `C4`: Lift the tilt angle of 3267284_1 by 10 degrees
- `C5`: Decrease A3 Offset threshold for 3250742_2
- `C6`: Add neighbor relationship between 3247546_3 and 3250742_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250742_2
- `C8`: Increase A3 Offset threshold for 3267284_1
- `C9`: Decrease transmission power for 3250742_2
- `C10`: Increase transmission power for 3250742_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250742_2
- `C12`: Decrease transmission power for 3267284_1
- `C13`: Increase A3 Offset threshold for 3250742_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267284_1
- `C15`: Press down the tilt angle  of 3250742_2 by 3 degrees
- `C16`: Check test server and transmission issues **← 정답**
- `C17`: Press down the tilt angle of 3267284_1 by 10 degrees
- `C18`: Increase transmission power for 3267284_1
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Adjust the azimuth of 3267284_1 by 50 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267284_1
- `C22`: Lift the tilt angle  of 3250742_2 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.980 | MS1 | 121.4656735755 | 31.1446256102 | 464 | 504990 | -90.40 | 15.46 | 567.49 | 0.01 | 2.53 | 1560 |
| 2024-09-20 22:21:32.853 | MS1 | 121.4656778843 | 31.1446228529 | 464 | 504990 | -91.40 | 15.74 | 512.58 | 0.09 | 2.89 | 1568 |
| 2024-09-20 22:21:33.264 | MS1 | 121.4656702789 | 31.1446252765 | 464 | 504990 | -91.47 | 14.58 | 416.70 | 0.15 | 2.29 | 1584 |
| 2024-09-20 22:21:34.165 | MS1 | 121.4656692398 | 31.1446190912 | 464 | 504990 | -88.37 | 12.40 | 78.11 | 0.17 | 2.23 | 317 |
| 2024-09-20 22:21:35.399 | MS1 | 121.4656594631 | 31.1446359865 | 464 | 504990 | -89.22 | 14.98 | 53.62 | 0.18 | 2.67 | 465 |
| 2024-09-20 22:21:36.141 | MS1 | 121.4656710108 | 31.1446208664 | 464 | 504990 | -91.43 | 12.87 | 60.30 | 0.05 | 2.88 | 473 |
| 2024-09-20 22:21:37.285 | MS1 | 121.4656754303 | 31.1446277461 | 464 | 504990 | -91.74 | 8.59 | 93.43 | 0.20 | 2.56 | 462 |
| 2024-09-20 22:21:38.762 | MS1 | 121.4656670687 | 31.1446293318 | 464 | 504990 | -90.13 | 8.79 | 86.83 | 0.12 | 2.44 | 341 |
| 2024-09-20 22:21:39.471 | MS1 | 121.4656625782 | 31.1446289686 | 464 | 504990 | -90.22 | 9.98 | 87.23 | 0.04 | 2.01 | 427 |
| 2024-09-20 22:21:40.318 | MS1 | 121.4656753845 | 31.1446204526 | 464 | 504990 | -93.93 | 12.52 | 601.10 | 0.01 | 2.68 | 1597 |
| 2024-09-20 22:21:41.397 | MS1 | 121.4656594141 | 31.1446268422 | 464 | 504990 | -91.47 | 11.50 | 318.49 | 0.05 | 2.32 | 1572 |
| 2024-09-20 22:21:42.424 | MS1 | 121.4656606027 | 31.1446221563 | 464 | 504990 | -93.07 | 12.64 | 458.59 | 0.15 | 2.73 | 1563 |

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
| 3215000 | 4 | 121.4751307000 | 31.1546335560 | 34 | 3 | 3 | 28.6 | TDD | 358 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3247546 | 3 | 121.4671525795 | 31.1445232086 | 227 | 13 | 7 | 46.6 | TDD | 21 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3250742 | 2 | 121.4687559615 | 31.1537621180 | 146 | 1 | 2 | 32.0 | TDD | 635 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3267284 | 1 | 121.4677063178 | 31.1546746228 | 60 | 13 | 6 | 18.4 | TDD | 464 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.390 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.413 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.518 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.518 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.223 | NREventA3 | measId:2;ServCellPCI:758;Se... |
| 2024-09-20 22:21:38.463 | NRHandoverAttempt | SourcePCI:758;SourceNR-ARFC... |
| 2024-09-20 22:21:38.504 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.516 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.625 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.625 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267284 | 1 | 16.1704 | 15.0929 | -116.4746 | 9.7739 | 107.1802 | 0.0005 | 0.0171 |
| 2024_09_20 22:00 | 3250742 | 2 | 5.2890 | 9.1820 | -117.8501 | 10.3712 | 175.3054 | 0.0019 | 0.0076 |
| 2024_09_20 22:00 | 3247546 | 3 | 8.5875 | 10.1922 | -114.8350 | 8.8143 | 148.5981 | 0.0130 | 0.0070 |
| 2024_09_20 22:00 | 3215000 | 4 | 9.2353 | 7.7152 | -114.4515 | 19.6162 | 186.2633 | 0.0041 | 0.0145 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413187_C98053A6 | 504990 | 464 | -86.9 | 504990 | 635 | -93.0 | 504990 | 21 | -98.5 | 504990 | 358 |
| MR_1774413187_D842D9B5 | 504990 | 464 | -90.3 | 504990 | 635 | -91.8 | 504990 | 21 | -96.0 | 504990 | 358 |
| MR_1774413187_217207A1 | 504990 | 464 | -87.8 | 504990 | 635 | -93.9 | 504990 | 21 | -98.9 | 504990 | 358 |
| MR_1774413187_F592B3B0 | 504990 | 464 | -86.7 | 504990 | 635 | -90.3 | 504990 | 21 | -97.1 | 504990 | 358 |
| MR_1774413187_BB5F8FC8 | 504990 | 464 | -86.5 | 504990 | 635 | -91.8 | 504990 | 21 | -96.1 | 504990 | 358 |
| MR_1774413187_C3A28595 | 504990 | 464 | -86.4 | 504990 | 635 | -90.4 | 504990 | 21 | -99.4 | 504990 | 358 |
| MR_1774413187_71938DEA | 504990 | 464 | -88.8 | 504990 | 635 | -93.6 | 504990 | 21 | -99.5 | 504990 | 358 |
| MR_1774413187_6A3EE066 | 504990 | 464 | -89.2 | 504990 | 635 | -91.7 | 504990 | 21 | -98.6 | 504990 | 358 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1609: `48b1aabe-b54...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `48b1aabe-b547-42cb-a62b-ddda6352dd9c` |
| Tag | **multiple-answer** |
| 정답 | **C1|C2** |
| C1 의미 | Increase transmission power for 3249224_2 |
| C2 의미 | Adjust the azimuth of 3249224_2 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1609] topology](images/train_1609.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3249224_2 **← 정답**
- `C2`: Adjust the azimuth of 3249224_2 by 50 degrees **← 정답**
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease A3 Offset threshold for 3269341_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269341_3
- `C6`: Adjust the azimuth of 3269341_3 by 6 degrees
- `C7`: Decrease transmission power for 3249224_2
- `C8`: Increase A3 Offset threshold for 3249224_2
- `C9`: Check test server and transmission issues
- `C10`: Add neighbor relationship between 3249224_2 and 3269341_3
- `C11`: Increase transmission power for 3269341_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249224_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249224_2
- `C14`: Decrease transmission power for 3269341_3
- `C15`: Press down the tilt angle of 3249224_2 by 10 degrees
- `C16`: Lift the tilt angle  of 3269341_3 by 4 degrees
- `C17`: Decrease A3 Offset threshold for 3249224_2
- `C18`: Lift the tilt angle of 3249224_2 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3269341_3
- `C20`: Press down the tilt angle  of 3269341_3 by 4 degrees
- `C21`: Add neighbor relationship between 3271816_4 and 3269341_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269341_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.164 | MS1 | 121.4656736845 | 31.1446202735 | 145 | 504990 | -94.43 | 12.24 | 413.85 | 0.18 | 2.11 | 1567 |
| 2024-09-20 22:21:32.754 | MS1 | 121.4656666675 | 31.1446356784 | 145 | 504990 | -85.62 | 13.53 | 390.17 | 0.10 | 2.04 | 1598 |
| 2024-09-20 22:21:33.558 | MS1 | 121.4656716820 | 31.1446344225 | 145 | 504990 | -92.96 | 17.94 | 439.31 | 0.11 | 2.85 | 1562 |
| 2024-09-20 22:21:34.558 | MS1 | 121.4656639573 | 31.1446185638 | 145 | 504990 | -101.15 | -0.98 | 55.39 | 0.14 | 1.47 | 1573 |
| 2024-09-20 22:21:35.387 | MS1 | 121.4656747655 | 31.1446312955 | 145 | 504990 | -101.76 | -1.62 | 17.36 | 0.15 | 1.32 | 1586 |
| 2024-09-20 22:21:36.618 | MS1 | 121.4656735270 | 31.1446272594 | 145 | 504990 | -105.06 | -0.78 | 35.07 | 0.11 | 1.43 | 1588 |
| 2024-09-20 22:21:37.992 | MS1 | 121.4656676959 | 31.1446270857 | 145 | 504990 | -108.64 | 0.75 | 50.49 | 0.07 | 1.38 | 1566 |
| 2024-09-20 22:21:38.496 | MS1 | 121.4656734112 | 31.1446335724 | 145 | 504990 | -109.44 | 1.32 | 27.48 | 0.13 | 1.44 | 1573 |
| 2024-09-20 22:21:39.793 | MS1 | 121.4656764150 | 31.1446351370 | 145 | 504990 | -101.07 | -0.19 | 53.20 | 0.19 | 1.29 | 1578 |
| 2024-09-20 22:21:40.640 | MS1 | 121.4656602050 | 31.1446236103 | 145 | 504990 | -91.25 | 15.50 | 431.54 | 0.10 | 2.81 | 1562 |
| 2024-09-20 22:21:41.492 | MS1 | 121.4656633557 | 31.1446210125 | 145 | 504990 | -88.43 | 17.79 | 539.99 | 0.02 | 2.51 | 1566 |
| 2024-09-20 22:21:42.523 | MS1 | 121.4656659873 | 31.1446214802 | 145 | 504990 | -90.02 | 12.42 | 363.17 | 0.03 | 2.55 | 1598 |

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
| 3249224 | 2 | 121.4691876685 | 31.1445822047 | 341 | 9 | 8 | 33.3 | TDD | 145 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3250952 | 1 | 121.4707545070 | 31.1492374162 | 296 | 3 | 4 | 24.1 | TDD | 544 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3269341 | 3 | 121.4752030228 | 31.1536447947 | 228 | 3 | 6 | 27.5 | TDD | 654 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3271816 | 4 | 121.4727439071 | 31.1494304967 | 301 | 10 | 0 | 18.8 | TDD | 257 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.919 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.944 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.078 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.078 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.311 | NREventA2 | measId:1;ServCellPCI:413;Se... |
| 2024-09-20 22:21:34.426 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250952 | 1 | 13.3106 | 14.3931 | -117.0651 | 14.8233 | 145.1202 | 0.0106 | 0.0122 |
| 2024_09_20 22:00 | 3249224 | 2 | 12.7992 | 19.5416 | -116.9895 | 14.3474 | 199.9219 | 0.1227 | 0.0121 |
| 2024_09_20 22:00 | 3269341 | 3 | 8.2573 | 16.4720 | -117.4917 | 18.9977 | 145.2040 | 0.0134 | 0.0191 |
| 2024_09_20 22:00 | 3271816 | 4 | 9.4514 | 15.1662 | -117.5045 | 15.9999 | 163.6897 | 0.0008 | 0.0003 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413704_D51C20DA | 504990 | 145 | -100.9 | 504990 | 654 | -106.0 | 504990 | 257 | -110.1 | 504990 | 544 |
| MR_1774413704_F9D625B5 | 504990 | 145 | -100.3 | 504990 | 654 | -103.9 | 504990 | 257 | -110.2 | 504990 | 544 |
| MR_1774413704_919C96A4 | 504990 | 145 | -103.1 | 504990 | 654 | -104.7 | 504990 | 257 | -111.0 | 504990 | 544 |
| MR_1774413704_083DDAEC | 504990 | 145 | -100.5 | 504990 | 654 | -105.6 | 504990 | 257 | -111.5 | 504990 | 544 |
| MR_1774413704_89E2BFBD | 504990 | 145 | -100.2 | 504990 | 654 | -107.0 | 504990 | 257 | -110.5 | 504990 | 544 |

> *... 2개 열 생략 (전체 14열)*

---
