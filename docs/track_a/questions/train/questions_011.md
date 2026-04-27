# Track A 문제 분석 — train[100]~train[109]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[100] ~ train[109] (10개)

## 목차

1. [문제 100: `f3fc5160-540...`](#100) — multiple-answer, 정답: C6|C14
2. [문제 101: `50a1d441-f36...`](#101) — single-answer, 정답: C4
3. [문제 102: `43023753-993...`](#102) — single-answer, 정답: C17
4. [문제 103: `6662e89a-c17...`](#103) — single-answer, 정답: C2
5. [문제 104: `ab98c497-2bd...`](#104) — single-answer, 정답: C2
6. [문제 105: `6490ed45-c1f...`](#105) — single-answer, 정답: C21
7. [문제 106: `fc8bedbb-ed2...`](#106) — single-answer, 정답: C22
8. [문제 107: `9e15229f-a02...`](#107) — single-answer, 정답: C1
9. [문제 108: `fbcc235a-e24...`](#108) — single-answer, 정답: C21
10. [문제 109: `519d5f41-847...`](#109) — single-answer, 정답: C21

---

### 문제 100: `f3fc5160-540...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f3fc5160-5402-4ae1-be24-bdfb0cc464f4` |
| Tag | **multiple-answer** |
| 정답 | **C6|C14** |
| C6 의미 | Adjust the azimuth of 3277349_4 by 50 degrees |
| C14 의미 | Increase transmission power for 3277349_4 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[100] topology](images/train_0100.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3277349_4
- `C2`: Increase A3 Offset threshold for 3277349_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277349_4
- `C4`: Decrease transmission power for 3277349_4
- `C5`: Add neighbor relationship between 3277349_4 and 3254544_1
- `C6`: Adjust the azimuth of 3277349_4 by 50 degrees **← 정답**
- `C7`: Decrease transmission power for 3254544_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277349_4
- `C9`: Lift the tilt angle  of 3254544_1 by 4 degrees
- `C10`: Adjust the azimuth of 3254544_1 by 46 degrees
- `C11`: Lift the tilt angle of 3277349_4 by 10 degrees
- `C12`: Press down the tilt angle  of 3254544_1 by 4 degrees
- `C13`: Decrease A3 Offset threshold for 3254544_1
- `C14`: Increase transmission power for 3277349_4 **← 정답**
- `C15`: Add neighbor relationship between 3267372_3 and 3254544_1
- `C16`: Increase transmission power for 3254544_1
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254544_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254544_1
- `C20`: Press down the tilt angle of 3277349_4 by 10 degrees
- `C21`: Increase A3 Offset threshold for 3254544_1
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.230 | MS1 | 121.4656664283 | 31.1446347815 | 262 | 504990 | -91.83 | 13.47 | 507.16 | 0.10 | 2.80 | 1600 |
| 2024-09-20 22:21:32.176 | MS1 | 121.4656772596 | 31.1446278134 | 262 | 504990 | -86.47 | 13.30 | 363.59 | 0.12 | 2.73 | 1596 |
| 2024-09-20 22:21:33.105 | MS1 | 121.4656764122 | 31.1446215928 | 262 | 504990 | -93.25 | 12.09 | 551.01 | 0.16 | 2.28 | 1563 |
| 2024-09-20 22:21:34.927 | MS1 | 121.4656745087 | 31.1446279695 | 262 | 504990 | -103.70 | 1.79 | 35.14 | 0.02 | 1.40 | 1599 |
| 2024-09-20 22:21:35.455 | MS1 | 121.4656756123 | 31.1446298688 | 262 | 504990 | -109.11 | -1.92 | 63.38 | 0.13 | 1.12 | 1568 |
| 2024-09-20 22:21:36.234 | MS1 | 121.4656644026 | 31.1446308550 | 262 | 504990 | -102.52 | -0.54 | 49.40 | 0.03 | 1.12 | 1561 |
| 2024-09-20 22:21:37.848 | MS1 | 121.4656718573 | 31.1446349592 | 262 | 504990 | -101.75 | -0.95 | 56.38 | 0.08 | 1.36 | 1577 |
| 2024-09-20 22:21:38.443 | MS1 | 121.4656701814 | 31.1446197449 | 262 | 504990 | -107.36 | -0.85 | 20.60 | 0.02 | 1.12 | 1578 |
| 2024-09-20 22:21:39.705 | MS1 | 121.4656764001 | 31.1446322220 | 262 | 504990 | -107.20 | -1.14 | 78.81 | 0.09 | 1.35 | 1574 |
| 2024-09-20 22:21:40.465 | MS1 | 121.4656671298 | 31.1446368034 | 262 | 504990 | -86.04 | 13.75 | 425.22 | 0.11 | 2.98 | 1600 |
| 2024-09-20 22:21:41.988 | MS1 | 121.4656581445 | 31.1446316975 | 262 | 504990 | -92.51 | 15.70 | 587.39 | 0.08 | 2.99 | 1562 |
| 2024-09-20 22:21:42.967 | MS1 | 121.4656662210 | 31.1446339884 | 262 | 504990 | -93.14 | 12.89 | 529.28 | 0.06 | 2.59 | 1587 |

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
| 3250133 | 2 | 121.4647378894 | 31.1517108988 | 271 | 6 | 12 | 33.1 | TDD | 506 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3254544 | 1 | 121.4666404372 | 31.1554335573 | 138 | 3 | 9 | 23.9 | TDD | 208 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3267372 | 3 | 121.4654484792 | 31.1517847248 | 324 | 15 | 7 | 27.5 | TDD | 152 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3277349 | 4 | 121.4735726713 | 31.1520677173 | 277 | 14 | 2 | 30.9 | TDD | 262 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.345 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.366 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.494 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.494 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.724 | NREventA2 | measId:1;ServCellPCI:247;Se... |
| 2024-09-20 22:21:34.827 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254544 | 1 | 16.1474 | 12.8848 | -115.0749 | 19.6182 | 126.6915 | 0.0080 | 0.0131 |
| 2024_09_20 22:00 | 3250133 | 2 | 5.1039 | 5.5355 | -116.9955 | 14.2050 | 125.9646 | 0.0012 | 0.0111 |
| 2024_09_20 22:00 | 3267372 | 3 | 14.2638 | 9.1373 | -116.6657 | 12.1769 | 129.9626 | 0.0132 | 0.0119 |
| 2024_09_20 22:00 | 3277349 | 4 | 16.3321 | 8.6790 | -114.0803 | 17.8533 | 142.8222 | 0.1908 | 0.0016 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416528_BB7FADBB | 504990 | 262 | -104.0 | 504990 | 208 | -110.6 | 504990 | 152 | -119.7 | 504990 | 506 |
| MR_1774416528_30653732 | 504990 | 262 | -103.8 | 504990 | 208 | -112.0 | 504990 | 152 | -118.6 | 504990 | 506 |
| MR_1774416528_A6E31C6A | 504990 | 262 | -103.0 | 504990 | 208 | -111.1 | 504990 | 152 | -117.8 | 504990 | 506 |
| MR_1774416528_D2C52D30 | 504990 | 262 | -101.8 | 504990 | 208 | -110.6 | 504990 | 152 | -117.3 | 504990 | 506 |
| MR_1774416528_95339716 | 504990 | 262 | -102.7 | 504990 | 208 | -110.0 | 504990 | 152 | -118.1 | 504990 | 506 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 101: `50a1d441-f36...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `50a1d441-f366-4e10-9b2e-ac2efd44924d` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Decrease A3 Offset threshold for 3236077_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[101] topology](images/train_0101.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3234285_3
- `C2`: Decrease A3 Offset threshold for 3234285_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234285_3
- `C4`: Decrease A3 Offset threshold for 3236077_1 **← 정답**
- `C5`: Decrease transmission power for 3234285_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234285_3
- `C7`: Adjust the azimuth of 3236077_1 by 50 degrees
- `C8`: Press down the tilt angle  of 3234285_3 by 10 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Press down the tilt angle of 3236077_1 by 5 degrees
- `C11`: Increase A3 Offset threshold for 3234285_3
- `C12`: Check test server and transmission issues
- `C13`: Lift the tilt angle  of 3234285_3 by 10 degrees
- `C14`: Adjust the azimuth of 3234285_3 by 47 degrees
- `C15`: Decrease transmission power for 3236077_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236077_1
- `C17`: Add neighbor relationship between 3236077_1 and 3234285_3
- `C18`: Lift the tilt angle of 3236077_1 by 5 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236077_1
- `C20`: Increase A3 Offset threshold for 3236077_1
- `C21`: Add neighbor relationship between 3255451_2 and 3234285_3
- `C22`: Increase transmission power for 3236077_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.534 | MS1 | 121.4656586175 | 31.1446297964 | 620 | 504990 | -76.54 | 15.50 | 448.35 | 0.11 | 2.78 | 1597 |
| 2024-09-20 22:21:32.839 | MS1 | 121.4656722068 | 31.1446182585 | 620 | 504990 | -79.55 | 15.02 | 447.19 | 0.19 | 2.79 | 1579 |
| 2024-09-20 22:21:33.756 | MS1 | 121.4656646708 | 31.1446351647 | 620 | 504990 | -79.83 | 14.86 | 569.28 | 0.00 | 2.77 | 1597 |
| 2024-09-20 22:21:34.394 | MS1 | 121.4656656979 | 31.1446235092 | 620 | 504990 | -83.33 | -2.66 | 38.02 | 0.19 | 1.22 | 1574 |
| 2024-09-20 22:21:35.759 | MS1 | 121.4656655775 | 31.1446344736 | 620 | 504990 | -85.63 | -1.41 | 42.72 | 0.01 | 1.01 | 1586 |
| 2024-09-20 22:21:36.354 | MS1 | 121.4656649787 | 31.1446193705 | 620 | 504990 | -92.06 | -2.94 | 43.22 | 0.08 | 1.19 | 1572 |
| 2024-09-20 22:21:37.705 | MS1 | 121.4656716215 | 31.1446238968 | 620 | 504990 | -84.42 | -2.29 | 47.43 | 0.08 | 1.18 | 1583 |
| 2024-09-20 22:21:38.202 | MS1 | 121.4656729549 | 31.1446374330 | 620 | 504990 | -86.10 | -2.07 | 58.46 | 0.05 | 1.38 | 1577 |
| 2024-09-20 22:21:39.832 | MS1 | 121.4656700517 | 31.1446212567 | 787 | 504990 | -84.44 | 17.64 | 271.99 | 0.06 | 1.44 | 1578 |
| 2024-09-20 22:21:40.756 | MS1 | 121.4656678928 | 31.1446364903 | 787 | 504990 | -81.09 | 14.55 | 374.07 | 0.09 | 2.86 | 1571 |
| 2024-09-20 22:21:41.660 | MS1 | 121.4656699585 | 31.1446182102 | 787 | 504990 | -84.92 | 16.57 | 312.14 | 0.19 | 2.59 | 1583 |
| 2024-09-20 22:21:42.261 | MS1 | 121.4656617022 | 31.1446203177 | 787 | 504990 | -81.11 | 16.10 | 317.35 | 0.16 | 2.69 | 1594 |

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
| 3234285 | 3 | 121.4704940411 | 31.1495505736 | 267 | 11 | 8 | 32.8 | TDD | 787 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3236077 | 1 | 121.4757012274 | 31.1477396412 | 200 | 2 | 5 | 45.4 | TDD | 620 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3239132 | 4 | 121.4732693580 | 31.1472000100 | 306 | 13 | 8 | 23.6 | TDD | 692 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3255451 | 2 | 121.4736790844 | 31.1538616136 | 108 | 4 | 12 | 48.8 | TDD | 713 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.868 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.890 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.006 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.006 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.759 | NREventA3 | measId:2;ServCellPCI:875;Se... |
| 2024-09-20 22:21:37.999 | NRHandoverAttempt | SourcePCI:875;SourceNR-ARFC... |
| 2024-09-20 22:21:38.031 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.042 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.159 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.159 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236077 | 1 | 12.4001 | 19.2138 | -116.2225 | 10.7084 | 137.5468 | 0.0036 | 0.1345 |
| 2024_09_20 22:00 | 3255451 | 2 | 6.2218 | 11.1770 | -116.6183 | 10.8945 | 133.7404 | 0.0007 | 0.0118 |
| 2024_09_20 22:00 | 3234285 | 3 | 14.7322 | 18.3280 | -116.9492 | 13.3342 | 166.5522 | 0.0020 | 0.0034 |
| 2024_09_20 22:00 | 3239132 | 4 | 8.1901 | 10.4015 | -116.7447 | 6.3853 | 129.4756 | 0.0004 | 0.0167 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412724_39AACFD6 | 504990 | 787 | -78.9 | 504990 | 620 | -81.9 | 504990 | 713 | -89.1 | 504990 | 692 |
| MR_1774412724_F8DF679F | 504990 | 620 | -85.0 | 504990 | 787 | -77.6 | 504990 | 713 | -88.6 | 504990 | 692 |
| MR_1774412724_517A11BF | 504990 | 620 | -85.2 | 504990 | 787 | -77.3 | 504990 | 713 | -87.3 | 504990 | 692 |
| MR_1774412724_BFFBE733 | 504990 | 620 | -83.1 | 504990 | 787 | -78.0 | 504990 | 713 | -88.6 | 504990 | 692 |
| MR_1774412724_E239E82A | 504990 | 620 | -83.4 | 504990 | 787 | -75.9 | 504990 | 713 | -87.5 | 504990 | 692 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 102: `43023753-993...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `43023753-993d-479c-a179-e902bac6f360` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[102] topology](images/train_0102.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3264925_2 by 10 degrees
- `C2`: Increase A3 Offset threshold for 3273075_1
- `C3`: Check test server and transmission issues
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264925_2
- `C5`: Increase transmission power for 3264925_2
- `C6`: Increase A3 Offset threshold for 3264925_2
- `C7`: Adjust the azimuth of 3264925_2 by 50 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264925_2
- `C9`: Press down the tilt angle of 3264925_2 by 10 degrees
- `C10`: Add neighbor relationship between 3224712_3 and 3273075_1
- `C11`: Decrease transmission power for 3273075_1
- `C12`: Lift the tilt angle  of 3273075_1 by 10 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273075_1
- `C14`: Press down the tilt angle  of 3273075_1 by 10 degrees
- `C15`: Increase transmission power for 3273075_1
- `C16`: Decrease transmission power for 3264925_2
- `C17`: Insufficient data; more data is needed for judgment. **← 정답**
- `C18`: Decrease A3 Offset threshold for 3264925_2
- `C19`: Decrease A3 Offset threshold for 3273075_1
- `C20`: Add neighbor relationship between 3264925_2 and 3273075_1
- `C21`: Adjust the azimuth of 3273075_1 by 50 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273075_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.435 | MS1 | 121.4656776199 | 31.1446238742 | 4 | 504990 | -89.70 | 14.29 | 329.32 | 0.12 | 2.36 | 1588 |
| 2024-09-20 22:21:32.680 | MS1 | 121.4656605204 | 31.1446195608 | 4 | 504990 | -89.93 | 17.59 | 462.97 | 0.01 | 2.42 | 1586 |
| 2024-09-20 22:21:33.648 | MS1 | 121.4656590927 | 31.1446289409 | 4 | 504990 | -86.24 | 15.29 | 370.37 | 0.19 | 2.30 | 1599 |
| 2024-09-20 22:21:34.677 | MS1 | 121.4656718998 | 31.1446214822 | 4 | 504990 | -89.50 | 16.81 | 90.37 | 0.16 | 2.88 | 1563 |
| 2024-09-20 22:21:35.102 | MS1 | 121.4656638329 | 31.1446333025 | 4 | 504990 | -89.70 | 12.07 | 102.16 | 0.07 | 2.78 | 1574 |
| 2024-09-20 22:21:36.613 | MS1 | 121.4656744217 | 31.1446356609 | 4 | 504990 | -90.65 | 13.94 | 64.76 | 0.17 | 2.88 | 1583 |
| 2024-09-20 22:21:37.867 | MS1 | 121.4656664628 | 31.1446248346 | 4 | 504990 | -93.89 | 12.73 | 75.14 | 0.07 | 2.31 | 1569 |
| 2024-09-20 22:21:38.953 | MS1 | 121.4656633931 | 31.1446193497 | 4 | 504990 | -89.37 | 8.75 | 83.54 | 0.16 | 2.09 | 1593 |
| 2024-09-20 22:21:39.283 | MS1 | 121.4656702931 | 31.1446370961 | 4 | 504990 | -89.09 | 7.01 | 96.38 | 0.15 | 2.70 | 1585 |
| 2024-09-20 22:21:40.977 | MS1 | 121.4656632244 | 31.1446192010 | 4 | 504990 | -92.64 | 12.70 | 354.76 | 0.13 | 2.45 | 1583 |
| 2024-09-20 22:21:41.183 | MS1 | 121.4656710949 | 31.1446272361 | 4 | 504990 | -92.33 | 8.93 | 459.80 | 0.01 | 2.88 | 1587 |
| 2024-09-20 22:21:42.383 | MS1 | 121.4656652476 | 31.1446276017 | 4 | 504990 | -91.25 | 8.08 | 461.10 | 0.20 | 2.47 | 1585 |

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
| 3224712 | 3 | 121.4726720141 | 31.1486297016 | 221 | 15 | 10 | 19.4 | TDD | 774 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3250777 | 4 | 121.4726262083 | 31.1536111847 | 245 | 4 | 1 | 23.9 | TDD | 308 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3264925 | 2 | 121.4660940523 | 31.1479651832 | 111 | 13 | 1 | 19.8 | TDD | 4 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3273075 | 1 | 121.4722915582 | 31.1514140483 | 312 | 9 | 5 | 34.9 | TDD | 954 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.631 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.651 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.753 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.753 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.447 | NREventA3 | measId:2;ServCellPCI:629;Se... |
| 2024-09-20 22:21:38.687 | NRHandoverAttempt | SourcePCI:629;SourceNR-ARFC... |
| 2024-09-20 22:21:38.724 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.737 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.854 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.854 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3273075 | 1 | 81.6142 | 80.9202 | -116.6100 | 8.4589 | 192.0288 | 0.0124 | 0.0090 |
| 2024_09_19 22:00 | 3264925 | 2 | 77.8896 | 82.8861 | -114.9093 | 6.4049 | 123.0411 | 0.0040 | 0.0126 |
| 2024_09_19 22:00 | 3224712 | 3 | 86.8330 | 86.4002 | -117.3123 | 9.8599 | 189.6427 | 0.0092 | 0.0096 |
| 2024_09_19 22:00 | 3250777 | 4 | 84.3263 | 90.0526 | -116.4928 | 10.2160 | 171.5957 | 0.0031 | 0.0095 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412959_5714A89D | 504990 | 4 | -91.1 | 504990 | 954 | -92.0 | 504990 | 774 | -100.6 | 504990 | 308 |
| MR_1774412959_28A619A9 | 504990 | 4 | -89.9 | 504990 | 954 | -90.8 | 504990 | 774 | -100.8 | 504990 | 308 |
| MR_1774412959_9FFABBBD | 504990 | 4 | -87.9 | 504990 | 954 | -94.0 | 504990 | 774 | -99.4 | 504990 | 308 |
| MR_1774412959_A1C83F91 | 504990 | 4 | -87.6 | 504990 | 954 | -91.9 | 504990 | 774 | -100.5 | 504990 | 308 |
| MR_1774412959_1A7B5AF3 | 504990 | 4 | -89.4 | 504990 | 954 | -93.3 | 504990 | 774 | -100.4 | 504990 | 308 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 103: `6662e89a-c17...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6662e89a-c179-4e43-a19c-0f5918bad7b9` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Lift the tilt angle  of 3221209_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[103] topology](images/train_0103.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3243952_4
- `C2`: Lift the tilt angle  of 3221209_2 by 10 degrees **← 정답**
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223678_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243952_4
- `C5`: Increase transmission power for 3243952_4
- `C6`: Decrease transmission power for 3243952_4
- `C7`: Check test server and transmission issues
- `C8`: Press down the tilt angle  of 3221209_2 by 10 degrees
- `C9`: Increase transmission power for 3223678_3
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease transmission power for 3223678_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243952_4
- `C13`: Adjust the azimuth of 3223678_3 by 8 degrees
- `C14`: Press down the tilt angle of 3223678_3 by 6 degrees
- `C15`: Decrease A3 Offset threshold for 3223678_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223678_3
- `C17`: Add neighbor relationship between 3223678_3 and 3243952_4
- `C18`: Lift the tilt angle of 3223678_3 by 6 degrees
- `C19`: Add neighbor relationship between 3221209_2 and 3243952_4
- `C20`: Decrease A3 Offset threshold for 3243952_4
- `C21`: Increase A3 Offset threshold for 3223678_3
- `C22`: Adjust the azimuth of 3221209_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.337 | MS1 | 121.4656604879 | 31.1446195419 | 131 | 504990 | -86.22 | 14.82 | 548.50 | 0.19 | 2.96 | 1568 |
| 2024-09-20 22:21:32.557 | MS1 | 121.4656605148 | 31.1446305264 | 131 | 504990 | -90.00 | 12.13 | 437.17 | 0.01 | 2.90 | 1589 |
| 2024-09-20 22:21:33.898 | MS1 | 121.4656655924 | 31.1446197898 | 131 | 504990 | -89.24 | 16.56 | 554.73 | 0.18 | 2.64 | 1561 |
| 2024-09-20 22:21:34.152 | MS1 | 121.4656731962 | 31.1446356436 | 131 | 504990 | -88.28 | 17.33 | 62.59 | 0.19 | 2.30 | 1562 |
| 2024-09-20 22:21:35.354 | MS1 | 121.4656664769 | 31.1446339363 | 131 | 504990 | -85.95 | 14.46 | 62.19 | 0.03 | 2.36 | 1593 |
| 2024-09-20 22:21:36.485 | MS1 | 121.4656643229 | 31.1446185223 | 131 | 504990 | -89.78 | 14.35 | 70.14 | 0.17 | 2.81 | 1580 |
| 2024-09-20 22:21:37.655 | MS1 | 121.4656706393 | 31.1446366160 | 131 | 504990 | -92.43 | 8.10 | 77.35 | 0.13 | 2.29 | 1563 |
| 2024-09-20 22:21:38.376 | MS1 | 121.4656695332 | 31.1446287582 | 131 | 504990 | -92.56 | 7.01 | 97.97 | 0.17 | 2.44 | 1597 |
| 2024-09-20 22:21:39.209 | MS1 | 121.4656735950 | 31.1446332947 | 131 | 504990 | -91.39 | 7.40 | 83.59 | 0.09 | 2.18 | 1576 |
| 2024-09-20 22:21:40.186 | MS1 | 121.4656722580 | 31.1446326976 | 131 | 504990 | -90.17 | 8.57 | 412.57 | 0.18 | 2.18 | 1573 |
| 2024-09-20 22:21:41.303 | MS1 | 121.4656656983 | 31.1446192144 | 131 | 504990 | -89.60 | 8.26 | 575.03 | 0.10 | 2.90 | 1592 |
| 2024-09-20 22:21:42.599 | MS1 | 121.4656750066 | 31.1446198650 | 131 | 504990 | -89.49 | 8.18 | 468.88 | 0.06 | 2.59 | 1598 |

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
| 3221209 | 2 | 121.4734484799 | 31.1558042988 | 65 | 14 | 1 | 48.6 | TDD | 153 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3223678 | 3 | 121.4709649700 | 31.1515146919 | 221 | 4 | 9 | 29.8 | TDD | 131 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3243952 | 4 | 121.4720036411 | 31.1460938488 | 353 | 8 | 10 | 42.5 | TDD | 166 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3267232 | 1 | 121.4741403159 | 31.1534319053 | 81 | 6 | 7 | 27.0 | TDD | 177 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.984 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.005 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.120 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.120 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.838 | NREventA3 | measId:2;ServCellPCI:302;Se... |
| 2024-09-20 22:21:38.078 | NRHandoverAttempt | SourcePCI:302;SourceNR-ARFC... |
| 2024-09-20 22:21:38.122 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.135 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.254 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.254 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267232 | 1 | 14.9676 | 15.5951 | -115.0270 | 11.0699 | 91.2017 | 0.0050 | 0.0048 |
| 2024_09_20 22:00 | 3221209 | 2 | 7.5959 | 7.8400 | -117.2722 | 5.1396 | 163.4414 | 0.0133 | 0.0117 |
| 2024_09_20 22:00 | 3223678 | 3 | 79.6892 | 85.1654 | -116.5333 | 14.1231 | 155.8095 | 0.0059 | 0.0031 |
| 2024_09_20 22:00 | 3243952 | 4 | 12.6802 | 15.4651 | -116.0766 | 18.5375 | 101.7742 | 0.0189 | 0.0096 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414794_402A85C6 | 504990 | 131 | -87.6 | 504990 | 166 | -88.7 | 504990 | 153 | -98.6 | 504990 | 177 |
| MR_1774414794_492297CB | 504990 | 131 | -88.8 | 504990 | 166 | -92.0 | 504990 | 153 | -100.8 | 504990 | 177 |
| MR_1774414794_32FC34D1 | 504990 | 131 | -88.1 | 504990 | 166 | -90.1 | 504990 | 153 | -99.7 | 504990 | 177 |
| MR_1774414794_0AF1F4FC | 504990 | 131 | -88.2 | 504990 | 166 | -91.9 | 504990 | 153 | -100.6 | 504990 | 177 |
| MR_1774414794_D2A12866 | 504990 | 131 | -88.1 | 504990 | 166 | -91.3 | 504990 | 153 | -101.1 | 504990 | 177 |
| MR_1774414794_73783A03 | 504990 | 131 | -86.5 | 504990 | 166 | -88.9 | 504990 | 153 | -98.5 | 504990 | 177 |
| MR_1774414794_42DB1F3F | 504990 | 131 | -87.3 | 504990 | 166 | -89.2 | 504990 | 153 | -100.2 | 504990 | 177 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 104: `ab98c497-2bd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ab98c497-2bd0-4ad0-81de-20e1ef37c1f4` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[104] topology](images/train_0104.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3245698_2
- `C2`: Check test server and transmission issues **← 정답**
- `C3`: Decrease transmission power for 3245698_2
- `C4`: Increase A3 Offset threshold for 3245698_2
- `C5`: Decrease A3 Offset threshold for 3267327_4
- `C6`: Increase A3 Offset threshold for 3267327_4
- `C7`: Adjust the azimuth of 3245698_2 by 46 degrees
- `C8`: Increase transmission power for 3267327_4
- `C9`: Lift the tilt angle of 3267327_4 by 7 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245698_2
- `C12`: Decrease transmission power for 3267327_4
- `C13`: Adjust the azimuth of 3267327_4 by 50 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245698_2
- `C15`: Add neighbor relationship between 3241868_1 and 3245698_2
- `C16`: Press down the tilt angle  of 3245698_2 by 10 degrees
- `C17`: Lift the tilt angle  of 3245698_2 by 10 degrees
- `C18`: Decrease A3 Offset threshold for 3245698_2
- `C19`: Press down the tilt angle of 3267327_4 by 7 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267327_4
- `C21`: Add neighbor relationship between 3267327_4 and 3245698_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267327_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.250 | MS1 | 121.4656602288 | 31.1446232062 | 763 | 504990 | -90.83 | 16.97 | 463.29 | 0.11 | 2.66 | 1573 |
| 2024-09-20 22:21:32.881 | MS1 | 121.4656610693 | 31.1446311063 | 763 | 504990 | -91.59 | 12.41 | 599.75 | 0.02 | 2.05 | 1561 |
| 2024-09-20 22:21:33.997 | MS1 | 121.4656736769 | 31.1446367822 | 763 | 504990 | -86.26 | 17.08 | 584.21 | 0.03 | 2.53 | 1591 |
| 2024-09-20 22:21:34.512 | MS1 | 121.4656773027 | 31.1446299495 | 763 | 504990 | -88.40 | 15.21 | 84.09 | 0.14 | 2.79 | 483 |
| 2024-09-20 22:21:35.532 | MS1 | 121.4656769076 | 31.1446206170 | 763 | 504990 | -85.75 | 16.32 | 75.07 | 0.01 | 2.59 | 421 |
| 2024-09-20 22:21:36.732 | MS1 | 121.4656692153 | 31.1446266525 | 763 | 504990 | -87.25 | 15.26 | 77.02 | 0.08 | 2.29 | 486 |
| 2024-09-20 22:21:37.300 | MS1 | 121.4656711870 | 31.1446360124 | 763 | 504990 | -89.90 | 9.06 | 61.48 | 0.10 | 2.50 | 479 |
| 2024-09-20 22:21:38.568 | MS1 | 121.4656692774 | 31.1446340244 | 763 | 504990 | -89.86 | 8.96 | 84.88 | 0.20 | 2.83 | 354 |
| 2024-09-20 22:21:39.980 | MS1 | 121.4656665021 | 31.1446321896 | 763 | 504990 | -93.09 | 12.13 | 105.37 | 0.14 | 2.34 | 468 |
| 2024-09-20 22:21:40.827 | MS1 | 121.4656777491 | 31.1446227716 | 763 | 504990 | -89.62 | 12.35 | 478.38 | 0.12 | 2.54 | 1590 |
| 2024-09-20 22:21:41.593 | MS1 | 121.4656667205 | 31.1446244469 | 763 | 504990 | -90.01 | 8.54 | 483.01 | 0.01 | 2.72 | 1590 |
| 2024-09-20 22:21:42.130 | MS1 | 121.4656665674 | 31.1446331710 | 763 | 504990 | -90.62 | 9.03 | 547.94 | 0.02 | 2.30 | 1586 |

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
| 3241868 | 1 | 121.4655543923 | 31.1535444754 | 153 | 7 | 11 | 44.5 | TDD | 455 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3245698 | 2 | 121.4751774348 | 31.1508429420 | 279 | 15 | 4 | 38.2 | TDD | 315 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3261079 | 3 | 121.4751980834 | 31.1459903875 | 35 | 0 | 4 | 42.4 | TDD | 685 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3267327 | 4 | 121.4738421426 | 31.1497851152 | 165 | 4 | 1 | 44.7 | TDD | 763 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.277 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.392 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.392 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.112 | NREventA3 | measId:2;ServCellPCI:665;Se... |
| 2024-09-20 22:21:38.352 | NRHandoverAttempt | SourcePCI:665;SourceNR-ARFC... |
| 2024-09-20 22:21:38.386 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.398 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.504 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.504 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241868 | 1 | 12.0750 | 13.7357 | -116.7423 | 5.8130 | 132.9265 | 0.0135 | 0.0157 |
| 2024_09_20 22:00 | 3245698 | 2 | 14.7694 | 19.9038 | -114.0575 | 15.4498 | 159.4439 | 0.0104 | 0.0163 |
| 2024_09_20 22:00 | 3261079 | 3 | 15.8828 | 19.6904 | -114.0479 | 12.9381 | 120.8429 | 0.0104 | 0.0050 |
| 2024_09_20 22:00 | 3267327 | 4 | 17.3473 | 19.4514 | -116.9430 | 19.0065 | 97.4452 | 0.0117 | 0.0099 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416535_BE4655CE | 504990 | 763 | -88.6 | 504990 | 315 | -91.7 | 504990 | 455 | -100.3 | 504990 | 685 |
| MR_1774416535_0657F253 | 504990 | 763 | -86.5 | 504990 | 315 | -95.3 | 504990 | 455 | -101.8 | 504990 | 685 |
| MR_1774416535_CFA8A4E7 | 504990 | 763 | -90.3 | 504990 | 315 | -92.3 | 504990 | 455 | -100.7 | 504990 | 685 |
| MR_1774416535_A5707DA3 | 504990 | 763 | -88.6 | 504990 | 315 | -91.8 | 504990 | 455 | -98.8 | 504990 | 685 |
| MR_1774416535_DD6887E2 | 504990 | 763 | -89.4 | 504990 | 315 | -92.6 | 504990 | 455 | -101.2 | 504990 | 685 |
| MR_1774416535_45ECDF46 | 504990 | 763 | -87.9 | 504990 | 315 | -92.9 | 504990 | 455 | -102.0 | 504990 | 685 |
| MR_1774416535_894AD0E8 | 504990 | 763 | -88.6 | 504990 | 315 | -93.9 | 504990 | 455 | -101.9 | 504990 | 685 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 105: `6490ed45-c1f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6490ed45-c1f8-4a64-ab53-c98ac4b80ded` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease A3 Offset threshold for 3227863_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[105] topology](images/train_0105.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3227863_1 and 3273508_4
- `C2`: Increase transmission power for 3227863_1
- `C3`: Lift the tilt angle  of 3273508_4 by 5 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273508_4
- `C5`: Add neighbor relationship between 3275881_2 and 3273508_4
- `C6`: Increase A3 Offset threshold for 3273508_4
- `C7`: Press down the tilt angle of 3227863_1 by 6 degrees
- `C8`: Adjust the azimuth of 3273508_4 by 50 degrees
- `C9`: Increase A3 Offset threshold for 3227863_1
- `C10`: Increase transmission power for 3273508_4
- `C11`: Lift the tilt angle of 3227863_1 by 6 degrees
- `C12`: Press down the tilt angle  of 3273508_4 by 5 degrees
- `C13`: Adjust the azimuth of 3227863_1 by 50 degrees
- `C14`: Decrease transmission power for 3273508_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227863_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227863_1
- `C17`: Decrease transmission power for 3227863_1
- `C18`: Check test server and transmission issues
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease A3 Offset threshold for 3273508_4
- `C21`: Decrease A3 Offset threshold for 3227863_1 **← 정답**
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273508_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.464 | MS1 | 121.4656607793 | 31.1446370871 | 961 | 504990 | -76.77 | 14.87 | 349.47 | 0.17 | 2.75 | 1579 |
| 2024-09-20 22:21:32.275 | MS1 | 121.4656735801 | 31.1446315808 | 961 | 504990 | -84.60 | 17.48 | 480.56 | 0.13 | 2.96 | 1596 |
| 2024-09-20 22:21:33.325 | MS1 | 121.4656584629 | 31.1446230328 | 961 | 504990 | -77.42 | 17.10 | 493.40 | 0.18 | 2.51 | 1560 |
| 2024-09-20 22:21:34.297 | MS1 | 121.4656638981 | 31.1446372282 | 961 | 504990 | -90.36 | -2.02 | 62.53 | 0.07 | 1.14 | 1586 |
| 2024-09-20 22:21:35.350 | MS1 | 121.4656628068 | 31.1446307473 | 961 | 504990 | -87.64 | -0.23 | 75.55 | 0.09 | 1.15 | 1562 |
| 2024-09-20 22:21:36.105 | MS1 | 121.4656756013 | 31.1446320476 | 961 | 504990 | -91.41 | -2.20 | 77.49 | 0.16 | 1.09 | 1562 |
| 2024-09-20 22:21:37.732 | MS1 | 121.4656728555 | 31.1446241850 | 961 | 504990 | -84.37 | -1.92 | 71.41 | 0.04 | 1.42 | 1576 |
| 2024-09-20 22:21:38.395 | MS1 | 121.4656746048 | 31.1446239771 | 961 | 504990 | -89.06 | -2.86 | 39.21 | 0.00 | 1.40 | 1580 |
| 2024-09-20 22:21:39.564 | MS1 | 121.4656731266 | 31.1446335547 | 663 | 504990 | -75.73 | 17.76 | 170.44 | 0.01 | 1.35 | 1587 |
| 2024-09-20 22:21:40.151 | MS1 | 121.4656622578 | 31.1446236314 | 663 | 504990 | -80.16 | 14.00 | 414.33 | 0.02 | 2.68 | 1562 |
| 2024-09-20 22:21:41.539 | MS1 | 121.4656765049 | 31.1446225074 | 663 | 504990 | -79.32 | 12.35 | 454.35 | 0.10 | 2.54 | 1584 |
| 2024-09-20 22:21:42.518 | MS1 | 121.4656618086 | 31.1446238516 | 663 | 504990 | -81.24 | 12.83 | 375.46 | 0.08 | 2.54 | 1573 |

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
| 3227863 | 1 | 121.4756907281 | 31.1493696570 | 70 | 5 | 8 | 23.9 | TDD | 961 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3230596 | 3 | 121.4704716663 | 31.1514632404 | 59 | 2 | 6 | 44.5 | TDD | 628 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3273508 | 4 | 121.4699883407 | 31.1558680036 | 261 | 3 | 4 | 49.1 | TDD | 663 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3275881 | 2 | 121.4731032825 | 31.1551841744 | 38 | 3 | 1 | 25.4 | TDD | 515 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.202 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.227 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.329 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.329 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.067 | NREventA3 | measId:2;ServCellPCI:955;Se... |
| 2024-09-20 22:21:38.307 | NRHandoverAttempt | SourcePCI:955;SourceNR-ARFC... |
| 2024-09-20 22:21:38.354 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.364 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.499 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.499 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227863 | 1 | 16.2177 | 9.0761 | -115.5476 | 10.8255 | 170.2406 | 0.0077 | 0.1328 |
| 2024_09_20 22:00 | 3275881 | 2 | 11.9384 | 16.4417 | -115.3486 | 15.4686 | 154.8584 | 0.0053 | 0.0021 |
| 2024_09_20 22:00 | 3230596 | 3 | 19.5807 | 18.8560 | -117.6191 | 10.0203 | 137.3275 | 0.0059 | 0.0101 |
| 2024_09_20 22:00 | 3273508 | 4 | 7.2142 | 9.8750 | -115.4151 | 9.0381 | 164.4238 | 0.0100 | 0.0186 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414856_2804898E | 504990 | 663 | -84.0 | 504990 | 961 | -90.7 | 504990 | 515 | -86.3 | 504990 | 628 |
| MR_1774414856_317CAFEC | 504990 | 663 | -85.9 | 504990 | 961 | -90.3 | 504990 | 515 | -90.2 | 504990 | 628 |
| MR_1774414856_CB92345D | 504990 | 663 | -86.5 | 504990 | 961 | -89.2 | 504990 | 515 | -89.8 | 504990 | 628 |
| MR_1774414856_3FF0F1C8 | 504990 | 961 | -89.7 | 504990 | 663 | -86.4 | 504990 | 515 | -86.7 | 504990 | 628 |
| MR_1774414856_C8C5E224 | 504990 | 961 | -91.4 | 504990 | 663 | -83.9 | 504990 | 515 | -89.6 | 504990 | 628 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 106: `fc8bedbb-ed2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fc8bedbb-ed2d-44b9-97ea-5eb39fc97907` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Add neighbor relationship between 3214700_3 and 3243837_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[106] topology](images/train_0106.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3243837_2
- `C2`: Press down the tilt angle of 3214700_3 by 10 degrees
- `C3`: Lift the tilt angle of 3214700_3 by 10 degrees
- `C4`: Lift the tilt angle  of 3243837_2 by 5 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214700_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243837_2
- `C7`: Increase transmission power for 3214700_3
- `C8`: Increase A3 Offset threshold for 3214700_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243837_2
- `C10`: Increase transmission power for 3243837_2
- `C11`: Adjust the azimuth of 3243837_2 by 15 degrees
- `C12`: Increase A3 Offset threshold for 3243837_2
- `C13`: Adjust the azimuth of 3214700_3 by 48 degrees
- `C14`: Decrease transmission power for 3214700_3
- `C15`: Add neighbor relationship between 3247020_4 and 3243837_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214700_3
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Press down the tilt angle  of 3243837_2 by 5 degrees
- `C19`: Decrease A3 Offset threshold for 3243837_2
- `C20`: Check test server and transmission issues
- `C21`: Decrease A3 Offset threshold for 3214700_3
- `C22`: Add neighbor relationship between 3214700_3 and 3243837_2 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.228 | MS1 | 121.4656580659 | 31.1446195022 | 907 | 504990 | -76.67 | 14.11 | 388.51 | 0.02 | 2.43 | 1576 |
| 2024-09-20 22:21:32.452 | MS1 | 121.4656765753 | 31.1446326537 | 907 | 504990 | -76.99 | 16.43 | 483.93 | 0.16 | 2.23 | 1569 |
| 2024-09-20 22:21:33.678 | MS1 | 121.4656714849 | 31.1446193108 | 907 | 504990 | -83.49 | 17.51 | 498.76 | 0.03 | 2.24 | 1591 |
| 2024-09-20 22:21:34.910 | MS1 | 121.4656633251 | 31.1446298315 | 907 | 504990 | -89.98 | -0.63 | 65.02 | 0.13 | 1.14 | 1595 |
| 2024-09-20 22:21:35.462 | MS1 | 121.4656704434 | 31.1446188855 | 907 | 504990 | -86.38 | -1.76 | 31.84 | 0.18 | 1.18 | 1596 |
| 2024-09-20 22:21:36.807 | MS1 | 121.4656603287 | 31.1446348670 | 907 | 504990 | -93.83 | -2.45 | 68.61 | 0.15 | 1.25 | 1563 |
| 2024-09-20 22:21:37.423 | MS1 | 121.4656674278 | 31.1446276615 | 907 | 504990 | -89.97 | -3.00 | 54.57 | 0.05 | 1.34 | 1586 |
| 2024-09-20 22:21:38.954 | MS1 | 121.4656775145 | 31.1446287093 | 907 | 504990 | -76.43 | 13.36 | 492.70 | 0.08 | 1.45 | 1584 |
| 2024-09-20 22:21:39.357 | MS1 | 121.4656582897 | 31.1446321936 | 907 | 504990 | -84.48 | 13.47 | 605.55 | 0.11 | 1.49 | 1597 |
| 2024-09-20 22:21:40.815 | MS1 | 121.4656588686 | 31.1446295389 | 907 | 504990 | -77.35 | 16.57 | 385.82 | 0.15 | 2.49 | 1577 |
| 2024-09-20 22:21:41.357 | MS1 | 121.4656777632 | 31.1446323795 | 907 | 504990 | -77.32 | 15.00 | 498.23 | 0.00 | 2.23 | 1568 |
| 2024-09-20 22:21:42.621 | MS1 | 121.4656689685 | 31.1446190132 | 907 | 504990 | -77.23 | 13.00 | 595.94 | 0.17 | 2.19 | 1560 |

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
| 3214700 | 3 | 121.4694972456 | 31.1443937217 | 226 | 12 | 0 | 48.3 | TDD | 907 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3243837 | 2 | 121.4752356666 | 31.1525604886 | 241 | 3 | 6 | 50.0 | TDD | 121 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3247020 | 4 | 121.4663296680 | 31.1473221932 | 199 | 8 | 10 | 44.1 | TDD | 43 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3277552 | 1 | 121.4703884659 | 31.1478674988 | 20 | 13 | 8 | 36.0 | TDD | 560 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.338 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.358 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.469 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.469 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.206 | NREventA3 | measId:2;ServCellPCI:37;Ser... |
| 2024-09-20 22:21:36.206 | NREventA3 | measId:2;ServCellPCI:37;Ser... |
| 2024-09-20 22:21:37.206 | NREventA3 | measId:2;ServCellPCI:37;Ser... |
| 2024-09-20 22:21:39.706 | NRRRCReestablishAttempt | PCI:37 |
| 2024-09-20 22:21:39.721 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.734 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.877 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.877 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277552 | 1 | 9.8696 | 6.2942 | -114.3168 | 10.7737 | 179.4402 | 0.0059 | 0.0009 |
| 2024_09_20 22:00 | 3243837 | 2 | 8.4543 | 13.2421 | -114.0945 | 18.0887 | 107.7692 | 0.0156 | 0.0137 |
| 2024_09_20 22:00 | 3214700 | 3 | 6.0616 | 7.6221 | -115.5953 | 13.4878 | 184.1662 | 0.0106 | 0.1248 |
| 2024_09_20 22:00 | 3247020 | 4 | 15.7870 | 5.1491 | -114.3299 | 16.0817 | 149.8999 | 0.0082 | 0.0088 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417182_470A447D | 504990 | 121 | -85.7 | 504990 | 907 | -91.0 | 504990 | 43 | -91.6 | 504990 | 560 |
| MR_1774417182_2E14987A | 504990 | 121 | -85.8 | 504990 | 907 | -89.2 | 504990 | 43 | -93.2 | 504990 | 560 |
| MR_1774417182_8F92E5CC | 504990 | 907 | -88.8 | 504990 | 121 | -85.3 | 504990 | 43 | -92.1 | 504990 | 560 |
| MR_1774417182_99E60622 | 504990 | 907 | -91.6 | 504990 | 121 | -85.8 | 504990 | 43 | -93.5 | 504990 | 560 |
| MR_1774417182_BA81D919 | 504990 | 121 | -84.0 | 504990 | 907 | -89.0 | 504990 | 43 | -91.3 | 504990 | 560 |
| MR_1774417182_62F07BB6 | 504990 | 907 | -89.4 | 504990 | 121 | -84.8 | 504990 | 43 | -90.9 | 504990 | 560 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 107: `9e15229f-a02...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9e15229f-a021-40a9-8c29-61922fd47d7e` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[107] topology](images/train_0107.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment. **← 정답**
- `C2`: Press down the tilt angle of 3243178_4 by 10 degrees
- `C3`: Increase transmission power for 3243178_4
- `C4`: Increase A3 Offset threshold for 3243178_4
- `C5`: Adjust the azimuth of 3270870_3 by 50 degrees
- `C6`: Add neighbor relationship between 3243178_4 and 3270870_3
- `C7`: Increase A3 Offset threshold for 3270870_3
- `C8`: Adjust the azimuth of 3243178_4 by 24 degrees
- `C9`: Decrease transmission power for 3243178_4
- `C10`: Decrease A3 Offset threshold for 3243178_4
- `C11`: Press down the tilt angle  of 3270870_3 by 10 degrees
- `C12`: Decrease transmission power for 3270870_3
- `C13`: Lift the tilt angle of 3243178_4 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243178_4
- `C15`: Lift the tilt angle  of 3270870_3 by 10 degrees
- `C16`: Increase transmission power for 3270870_3
- `C17`: Decrease A3 Offset threshold for 3270870_3
- `C18`: Add neighbor relationship between 3241946_1 and 3270870_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243178_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270870_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270870_3
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.228 | MS1 | 121.4656693885 | 31.1446247215 | 774 | 504990 | -86.75 | 13.48 | 379.63 | 0.16 | 2.27 | 1599 |
| 2024-09-20 22:21:32.979 | MS1 | 121.4656772751 | 31.1446181267 | 774 | 504990 | -86.82 | 12.45 | 557.99 | 0.06 | 2.41 | 1574 |
| 2024-09-20 22:21:33.993 | MS1 | 121.4656683672 | 31.1446190725 | 774 | 504990 | -89.62 | 15.78 | 401.93 | 0.09 | 2.60 | 1570 |
| 2024-09-20 22:21:34.938 | MS1 | 121.4656670488 | 31.1446242232 | 774 | 504990 | -85.47 | 15.59 | 79.66 | 0.09 | 2.26 | 1571 |
| 2024-09-20 22:21:35.196 | MS1 | 121.4656744495 | 31.1446334237 | 774 | 504990 | -87.27 | 15.05 | 76.86 | 0.12 | 2.61 | 1574 |
| 2024-09-20 22:21:36.934 | MS1 | 121.4656749330 | 31.1446356064 | 774 | 504990 | -87.01 | 13.07 | 47.91 | 0.06 | 2.86 | 1585 |
| 2024-09-20 22:21:37.299 | MS1 | 121.4656721617 | 31.1446318243 | 774 | 504990 | -91.20 | 12.52 | 82.84 | 0.04 | 2.43 | 1581 |
| 2024-09-20 22:21:38.152 | MS1 | 121.4656641483 | 31.1446217337 | 774 | 504990 | -90.26 | 8.53 | 92.46 | 0.07 | 2.40 | 1574 |
| 2024-09-20 22:21:39.723 | MS1 | 121.4656704281 | 31.1446201268 | 774 | 504990 | -89.66 | 11.34 | 72.80 | 0.11 | 2.27 | 1586 |
| 2024-09-20 22:21:40.254 | MS1 | 121.4656605374 | 31.1446319917 | 774 | 504990 | -89.47 | 8.05 | 425.11 | 0.10 | 2.89 | 1572 |
| 2024-09-20 22:21:41.785 | MS1 | 121.4656641468 | 31.1446198926 | 774 | 504990 | -89.31 | 8.95 | 438.44 | 0.04 | 2.16 | 1564 |
| 2024-09-20 22:21:42.144 | MS1 | 121.4656647534 | 31.1446324264 | 774 | 504990 | -91.96 | 7.14 | 439.20 | 0.18 | 2.36 | 1560 |

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
| 3214099 | 2 | 121.4759631602 | 31.1462559786 | 129 | 0 | 6 | 38.5 | TDD | 44 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3241946 | 1 | 121.4744738653 | 31.1489388846 | 64 | 3 | 0 | 31.5 | TDD | 425 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3243178 | 4 | 121.4716486896 | 31.1440612905 | 252 | 7 | 2 | 42.4 | TDD | 774 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3270870 | 3 | 121.4670345248 | 31.1555962888 | 259 | 10 | 6 | 42.5 | TDD | 310 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.472 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.487 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.616 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.616 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.308 | NREventA3 | measId:2;ServCellPCI:705;Se... |
| 2024-09-20 22:21:38.548 | NRHandoverAttempt | SourcePCI:705;SourceNR-ARFC... |
| 2024-09-20 22:21:38.593 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.607 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.707 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.707 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3241946 | 1 | 80.1639 | 90.7926 | -115.6524 | 19.8545 | 124.7038 | 0.0153 | 0.0061 |
| 2024_09_19 22:00 | 3214099 | 2 | 78.8667 | 90.4906 | -116.4914 | 14.8444 | 163.7120 | 0.0073 | 0.0199 |
| 2024_09_19 22:00 | 3270870 | 3 | 90.0054 | 91.6397 | -117.3338 | 19.4737 | 125.8024 | 0.0024 | 0.0140 |
| 2024_09_19 22:00 | 3243178 | 4 | 76.2868 | 89.2347 | -116.1271 | 6.4181 | 139.6218 | 0.0109 | 0.0128 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414623_B64590C7 | 504990 | 774 | -85.4 | 504990 | 310 | -89.6 | 504990 | 425 | -95.8 | 504990 | 44 |
| MR_1774414623_791EDDC8 | 504990 | 774 | -84.9 | 504990 | 310 | -89.0 | 504990 | 425 | -95.9 | 504990 | 44 |
| MR_1774414623_73833A83 | 504990 | 774 | -84.9 | 504990 | 310 | -86.8 | 504990 | 425 | -98.8 | 504990 | 44 |
| MR_1774414623_C865E805 | 504990 | 774 | -87.2 | 504990 | 310 | -89.6 | 504990 | 425 | -97.3 | 504990 | 44 |
| MR_1774414623_DB9BAEF7 | 504990 | 774 | -83.7 | 504990 | 310 | -88.2 | 504990 | 425 | -98.2 | 504990 | 44 |
| MR_1774414623_AA019306 | 504990 | 774 | -86.3 | 504990 | 310 | -88.6 | 504990 | 425 | -97.6 | 504990 | 44 |
| MR_1774414623_8FEAC7E5 | 504990 | 774 | -84.0 | 504990 | 310 | -86.4 | 504990 | 425 | -96.0 | 504990 | 44 |
| MR_1774414623_E5526756 | 504990 | 774 | -87.4 | 504990 | 310 | -89.0 | 504990 | 425 | -97.9 | 504990 | 44 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 108: `fbcc235a-e24...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fbcc235a-e243-4061-a28d-f9066aa45b67` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Add neighbor relationship between 3258217_2 and 3275187_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[108] topology](images/train_0108.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3258217_2 by 50 degrees
- `C2`: Add neighbor relationship between 3266962_1 and 3275187_3
- `C3`: Increase transmission power for 3275187_3
- `C4`: Decrease A3 Offset threshold for 3275187_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258217_2
- `C6`: Lift the tilt angle of 3258217_2 by 3 degrees
- `C7`: Increase transmission power for 3258217_2
- `C8`: Press down the tilt angle of 3258217_2 by 3 degrees
- `C9`: Decrease A3 Offset threshold for 3258217_2
- `C10`: Check test server and transmission issues
- `C11`: Press down the tilt angle  of 3275187_3 by 5 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275187_3
- `C13`: Adjust the azimuth of 3275187_3 by 13 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275187_3
- `C15`: Decrease transmission power for 3275187_3
- `C16`: Increase A3 Offset threshold for 3258217_2
- `C17`: Decrease transmission power for 3258217_2
- `C18`: Increase A3 Offset threshold for 3275187_3
- `C19`: Lift the tilt angle  of 3275187_3 by 5 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Add neighbor relationship between 3258217_2 and 3275187_3 **← 정답**
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258217_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.853 | MS1 | 121.4656762048 | 31.1446294032 | 969 | 504990 | -79.57 | 17.83 | 497.26 | 0.15 | 2.37 | 1596 |
| 2024-09-20 22:21:32.112 | MS1 | 121.4656719137 | 31.1446255807 | 969 | 504990 | -82.21 | 12.80 | 327.06 | 0.13 | 2.88 | 1574 |
| 2024-09-20 22:21:33.459 | MS1 | 121.4656706328 | 31.1446353465 | 969 | 504990 | -76.38 | 14.17 | 512.50 | 0.13 | 2.25 | 1572 |
| 2024-09-20 22:21:34.261 | MS1 | 121.4656715005 | 31.1446308892 | 969 | 504990 | -94.59 | -0.12 | 45.43 | 0.10 | 1.37 | 1562 |
| 2024-09-20 22:21:35.803 | MS1 | 121.4656653306 | 31.1446302425 | 969 | 504990 | -85.89 | -0.33 | 58.24 | 0.03 | 1.30 | 1593 |
| 2024-09-20 22:21:36.812 | MS1 | 121.4656626514 | 31.1446280571 | 969 | 504990 | -92.27 | -0.03 | 35.96 | 0.04 | 1.17 | 1573 |
| 2024-09-20 22:21:37.549 | MS1 | 121.4656591862 | 31.1446332871 | 969 | 504990 | -88.68 | -1.50 | 72.62 | 0.02 | 1.24 | 1560 |
| 2024-09-20 22:21:38.812 | MS1 | 121.4656723598 | 31.1446349289 | 969 | 504990 | -84.26 | 14.65 | 467.08 | 0.18 | 1.03 | 1585 |
| 2024-09-20 22:21:39.692 | MS1 | 121.4656655509 | 31.1446361018 | 969 | 504990 | -77.80 | 17.24 | 506.35 | 0.17 | 1.31 | 1579 |
| 2024-09-20 22:21:40.574 | MS1 | 121.4656758767 | 31.1446266999 | 969 | 504990 | -76.82 | 16.58 | 317.81 | 0.06 | 2.87 | 1589 |
| 2024-09-20 22:21:41.266 | MS1 | 121.4656671176 | 31.1446218236 | 969 | 504990 | -82.69 | 14.81 | 556.41 | 0.17 | 2.32 | 1594 |
| 2024-09-20 22:21:42.745 | MS1 | 121.4656634687 | 31.1446303444 | 969 | 504990 | -83.70 | 12.63 | 521.90 | 0.01 | 2.99 | 1575 |

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
| 3211813 | 4 | 121.4744677012 | 31.1523214989 | 101 | 5 | 8 | 17.6 | TDD | 789 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3258217 | 2 | 121.4754942327 | 31.1504221756 | 317 | 1 | 4 | 34.9 | TDD | 969 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3266962 | 1 | 121.4683223695 | 31.1454816253 | 124 | 0 | 1 | 15.1 | TDD | 896 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3275187 | 3 | 121.4747276788 | 31.1551183649 | 229 | 3 | 1 | 43.5 | TDD | 506 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.612 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.629 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.773 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.773 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.443 | NREventA3 | measId:2;ServCellPCI:897;Se... |
| 2024-09-20 22:21:36.443 | NREventA3 | measId:2;ServCellPCI:897;Se... |
| 2024-09-20 22:21:37.443 | NREventA3 | measId:2;ServCellPCI:897;Se... |
| 2024-09-20 22:21:39.943 | NRRRCReestablishAttempt | PCI:897 |
| 2024-09-20 22:21:39.962 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.974 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:40.095 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.095 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266962 | 1 | 10.8264 | 6.0756 | -117.8460 | 7.4205 | 168.5618 | 0.0081 | 0.0173 |
| 2024_09_20 22:00 | 3258217 | 2 | 8.2620 | 16.8707 | -116.3416 | 19.6665 | 170.4214 | 0.0160 | 0.1015 |
| 2024_09_20 22:00 | 3275187 | 3 | 15.2006 | 11.6375 | -115.8964 | 14.7448 | 165.3382 | 0.0084 | 0.0168 |
| 2024_09_20 22:00 | 3211813 | 4 | 9.1361 | 19.5716 | -115.3121 | 11.1116 | 126.2576 | 0.0014 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416789_D2A80AE4 | 504990 | 969 | -93.3 | 504990 | 506 | -90.6 | 504990 | 896 | -98.0 | 504990 | 789 |
| MR_1774416789_00306F65 | 504990 | 969 | -95.2 | 504990 | 506 | -89.4 | 504990 | 896 | -100.7 | 504990 | 789 |
| MR_1774416789_BF1793B1 | 504990 | 969 | -92.8 | 504990 | 506 | -89.9 | 504990 | 896 | -100.7 | 504990 | 789 |
| MR_1774416789_AC1D086D | 504990 | 969 | -95.5 | 504990 | 506 | -89.0 | 504990 | 896 | -100.2 | 504990 | 789 |
| MR_1774416789_D93EEB3F | 504990 | 969 | -92.8 | 504990 | 506 | -90.1 | 504990 | 896 | -98.8 | 504990 | 789 |
| MR_1774416789_B5698121 | 504990 | 969 | -96.0 | 504990 | 506 | -88.5 | 504990 | 896 | -100.6 | 504990 | 789 |
| MR_1774416789_664CF19D | 504990 | 506 | -89.9 | 504990 | 969 | -95.0 | 504990 | 896 | -98.0 | 504990 | 789 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 109: `519d5f41-847...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `519d5f41-847e-4a3b-99a2-b9ad067eb0c4` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Lift the tilt angle  of 3223687_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[109] topology](images/train_0109.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3223687_2 and 3253455_3
- `C2`: Press down the tilt angle of 3272267_1 by 5 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253455_3
- `C4`: Decrease transmission power for 3253455_3
- `C5`: Decrease A3 Offset threshold for 3253455_3
- `C6`: Add neighbor relationship between 3272267_1 and 3253455_3
- `C7`: Adjust the azimuth of 3223687_2 by 50 degrees
- `C8`: Increase transmission power for 3253455_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272267_1
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease A3 Offset threshold for 3272267_1
- `C12`: Increase A3 Offset threshold for 3253455_3
- `C13`: Press down the tilt angle  of 3223687_2 by 10 degrees
- `C14`: Decrease transmission power for 3272267_1
- `C15`: Check test server and transmission issues
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253455_3
- `C17`: Increase A3 Offset threshold for 3272267_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272267_1
- `C19`: Lift the tilt angle of 3272267_1 by 5 degrees
- `C20`: Adjust the azimuth of 3272267_1 by 0 degrees
- `C21`: Lift the tilt angle  of 3223687_2 by 10 degrees **← 정답**
- `C22`: Increase transmission power for 3272267_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.594 | MS1 | 121.4656594183 | 31.1446217440 | 905 | 504990 | -86.87 | 13.81 | 425.66 | 0.03 | 2.64 | 1570 |
| 2024-09-20 22:21:32.610 | MS1 | 121.4656728128 | 31.1446233618 | 905 | 504990 | -89.46 | 13.25 | 331.47 | 0.11 | 2.51 | 1566 |
| 2024-09-20 22:21:33.550 | MS1 | 121.4656718092 | 31.1446373509 | 905 | 504990 | -91.89 | 14.31 | 551.22 | 0.02 | 2.74 | 1573 |
| 2024-09-20 22:21:34.242 | MS1 | 121.4656657263 | 31.1446236627 | 905 | 504990 | -91.07 | 17.32 | 104.22 | 0.02 | 2.37 | 1573 |
| 2024-09-20 22:21:35.690 | MS1 | 121.4656760629 | 31.1446279271 | 905 | 504990 | -91.51 | 17.01 | 73.74 | 0.15 | 2.33 | 1600 |
| 2024-09-20 22:21:36.848 | MS1 | 121.4656644181 | 31.1446319091 | 905 | 504990 | -87.26 | 12.62 | 61.14 | 0.15 | 2.28 | 1600 |
| 2024-09-20 22:21:37.109 | MS1 | 121.4656766943 | 31.1446288687 | 905 | 504990 | -92.77 | 8.41 | 72.16 | 0.07 | 2.36 | 1564 |
| 2024-09-20 22:21:38.309 | MS1 | 121.4656725916 | 31.1446343178 | 905 | 504990 | -91.44 | 12.93 | 68.03 | 0.04 | 2.41 | 1582 |
| 2024-09-20 22:21:39.974 | MS1 | 121.4656641407 | 31.1446335620 | 905 | 504990 | -91.02 | 12.87 | 62.80 | 0.18 | 2.61 | 1596 |
| 2024-09-20 22:21:40.562 | MS1 | 121.4656713054 | 31.1446259446 | 905 | 504990 | -92.62 | 12.83 | 466.30 | 0.19 | 2.35 | 1577 |
| 2024-09-20 22:21:41.989 | MS1 | 121.4656613956 | 31.1446318488 | 905 | 504990 | -91.56 | 10.52 | 447.81 | 0.20 | 2.01 | 1586 |
| 2024-09-20 22:21:42.901 | MS1 | 121.4656734218 | 31.1446352172 | 905 | 504990 | -91.16 | 8.20 | 375.86 | 0.11 | 2.67 | 1568 |

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
| 3223687 | 2 | 121.4652102679 | 31.1525877147 | 341 | 3 | 12 | 32.6 | TDD | 210 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3253455 | 3 | 121.4749171786 | 31.1520642033 | 122 | 8 | 2 | 41.8 | TDD | 479 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3267908 | 4 | 121.4726741372 | 31.1547612104 | 146 | 3 | 1 | 18.8 | TDD | 639 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3272267 | 1 | 121.4669833344 | 31.1536507826 | 187 | 4 | 3 | 15.1 | TDD | 905 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.055 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.072 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.202 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.202 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.885 | NREventA3 | measId:2;ServCellPCI:715;Se... |
| 2024-09-20 22:21:38.125 | NRHandoverAttempt | SourcePCI:715;SourceNR-ARFC... |
| 2024-09-20 22:21:38.160 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.170 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.286 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.286 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272267 | 1 | 77.3584 | 94.5812 | -114.9512 | 9.8103 | 167.1461 | 0.0163 | 0.0044 |
| 2024_09_20 22:00 | 3223687 | 2 | 14.4696 | 5.5482 | -114.8651 | 18.7526 | 122.8454 | 0.0091 | 0.0001 |
| 2024_09_20 22:00 | 3253455 | 3 | 6.1320 | 18.9480 | -115.2690 | 17.6988 | 101.5002 | 0.0101 | 0.0093 |
| 2024_09_20 22:00 | 3267908 | 4 | 15.1581 | 10.6057 | -116.5192 | 15.2362 | 178.3666 | 0.0152 | 0.0049 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413838_421CAD68 | 504990 | 905 | -92.6 | 504990 | 479 | -96.2 | 504990 | 210 | -105.9 | 504990 | 639 |
| MR_1774413838_94B7CDA0 | 504990 | 905 | -92.8 | 504990 | 479 | -96.0 | 504990 | 210 | -104.2 | 504990 | 639 |
| MR_1774413838_23E1F2C3 | 504990 | 905 | -91.4 | 504990 | 479 | -94.7 | 504990 | 210 | -103.3 | 504990 | 639 |
| MR_1774413838_4DCC562A | 504990 | 905 | -91.1 | 504990 | 479 | -94.1 | 504990 | 210 | -105.9 | 504990 | 639 |
| MR_1774413838_157B0A1A | 504990 | 905 | -90.8 | 504990 | 479 | -97.6 | 504990 | 210 | -103.8 | 504990 | 639 |
| MR_1774413838_A4EB4BDA | 504990 | 905 | -91.8 | 504990 | 479 | -94.1 | 504990 | 210 | -104.4 | 504990 | 639 |
| MR_1774413838_C8983396 | 504990 | 905 | -90.8 | 504990 | 479 | -96.6 | 504990 | 210 | -105.2 | 504990 | 639 |
| MR_1774413838_7BAB9AB1 | 504990 | 905 | -92.8 | 504990 | 479 | -94.8 | 504990 | 210 | -102.8 | 504990 | 639 |

> *... 2개 열 생략 (전체 14열)*

---
