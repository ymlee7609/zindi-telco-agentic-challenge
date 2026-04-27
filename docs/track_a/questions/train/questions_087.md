# Track A 문제 분석 — train[860]~train[869]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[860] ~ train[869] (10개)

## 목차

1. [문제 860: `5e3c6be9-af0...`](#860) — single-answer, 정답: C1
2. [문제 861: `d2433566-a8c...`](#861) — multiple-answer, 정답: C6|C18
3. [문제 862: `0822a3c3-b84...`](#862) — single-answer, 정답: C10
4. [문제 863: `fa53284c-f4e...`](#863) — single-answer, 정답: C16
5. [문제 864: `fa14fb54-cc1...`](#864) — single-answer, 정답: C8
6. [문제 865: `98582184-e9f...`](#865) — multiple-answer, 정답: C4|C18
7. [문제 866: `38e29454-c4b...`](#866) — single-answer, 정답: C11
8. [문제 867: `b973a6dc-3a5...`](#867) — single-answer, 정답: C14
9. [문제 868: `583e284f-d01...`](#868) — single-answer, 정답: C13
10. [문제 869: `5453d424-725...`](#869) — single-answer, 정답: C15

---

### 문제 860: `5e3c6be9-af0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5e3c6be9-af01-463d-8f9c-a3907d3920b7` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Lift the tilt angle  of 3261124_2 by 9 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[860] topology](images/train_0860.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3261124_2 by 9 degrees **← 정답**
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Adjust the azimuth of 3270815_4 by 13 degrees
- `C4`: Decrease A3 Offset threshold for 3270815_4
- `C5`: Increase transmission power for 3273640_1
- `C6`: Add neighbor relationship between 3261124_2 and 3273640_1
- `C7`: Press down the tilt angle of 3270815_4 by 3 degrees
- `C8`: Decrease transmission power for 3273640_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270815_4
- `C10`: Press down the tilt angle  of 3261124_2 by 9 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270815_4
- `C12`: Decrease A3 Offset threshold for 3273640_1
- `C13`: Lift the tilt angle of 3270815_4 by 3 degrees
- `C14`: Decrease transmission power for 3270815_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273640_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273640_1
- `C17`: Add neighbor relationship between 3270815_4 and 3273640_1
- `C18`: Adjust the azimuth of 3261124_2 by 50 degrees
- `C19`: Increase A3 Offset threshold for 3270815_4
- `C20`: Increase transmission power for 3270815_4
- `C21`: Check test server and transmission issues
- `C22`: Increase A3 Offset threshold for 3273640_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.768 | MS1 | 121.4656603144 | 31.1446307276 | 542 | 504990 | -91.29 | 12.47 | 312.23 | 0.00 | 2.27 | 1566 |
| 2024-09-20 22:21:32.154 | MS1 | 121.4656733573 | 31.1446217790 | 542 | 504990 | -86.11 | 13.46 | 369.91 | 0.17 | 2.86 | 1585 |
| 2024-09-20 22:21:33.373 | MS1 | 121.4656703525 | 31.1446337821 | 542 | 504990 | -85.39 | 17.23 | 341.01 | 0.20 | 2.99 | 1576 |
| 2024-09-20 22:21:34.845 | MS1 | 121.4656775439 | 31.1446322311 | 542 | 504990 | -87.37 | 13.56 | 69.70 | 0.10 | 2.20 | 1572 |
| 2024-09-20 22:21:35.194 | MS1 | 121.4656613747 | 31.1446203515 | 542 | 504990 | -91.63 | 12.05 | 68.16 | 0.03 | 2.89 | 1570 |
| 2024-09-20 22:21:36.318 | MS1 | 121.4656645516 | 31.1446303737 | 542 | 504990 | -87.31 | 13.95 | 78.28 | 0.15 | 2.36 | 1590 |
| 2024-09-20 22:21:37.443 | MS1 | 121.4656734136 | 31.1446247417 | 542 | 504990 | -89.02 | 11.09 | 102.46 | 0.19 | 2.64 | 1583 |
| 2024-09-20 22:21:38.185 | MS1 | 121.4656714214 | 31.1446265614 | 542 | 504990 | -92.31 | 10.34 | 57.38 | 0.01 | 2.60 | 1588 |
| 2024-09-20 22:21:39.711 | MS1 | 121.4656647153 | 31.1446181641 | 542 | 504990 | -92.34 | 9.00 | 85.51 | 0.04 | 2.47 | 1562 |
| 2024-09-20 22:21:40.652 | MS1 | 121.4656622236 | 31.1446281787 | 542 | 504990 | -90.70 | 7.87 | 414.61 | 0.08 | 2.59 | 1570 |
| 2024-09-20 22:21:41.948 | MS1 | 121.4656705379 | 31.1446180350 | 542 | 504990 | -91.66 | 8.11 | 325.21 | 0.16 | 2.33 | 1576 |
| 2024-09-20 22:21:42.564 | MS1 | 121.4656692557 | 31.1446209502 | 542 | 504990 | -91.52 | 11.22 | 334.68 | 0.08 | 2.22 | 1581 |

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
| 3261124 | 2 | 121.4682714901 | 31.1533054008 | 50 | 10 | 4 | 19.6 | TDD | 526 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3270815 | 4 | 121.4725928382 | 31.1540033014 | 199 | 2 | 11 | 16.2 | TDD | 542 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3273640 | 1 | 121.4726368494 | 31.1520376165 | 348 | 8 | 6 | 21.7 | TDD | 298 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3276959 | 3 | 121.4687880269 | 31.1538428028 | 289 | 8 | 6 | 34.6 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.545 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.566 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.701 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.701 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.426 | NREventA3 | measId:2;ServCellPCI:714;Se... |
| 2024-09-20 22:21:38.666 | NRHandoverAttempt | SourcePCI:714;SourceNR-ARFC... |
| 2024-09-20 22:21:38.710 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.725 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.834 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.834 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273640 | 1 | 18.8715 | 5.1721 | -117.6364 | 13.4202 | 115.3800 | 0.0021 | 0.0066 |
| 2024_09_20 22:00 | 3261124 | 2 | 17.4692 | 18.1367 | -116.5365 | 8.3002 | 120.4521 | 0.0090 | 0.0174 |
| 2024_09_20 22:00 | 3276959 | 3 | 6.6683 | 13.7428 | -117.8502 | 14.9951 | 82.2747 | 0.0056 | 0.0034 |
| 2024_09_20 22:00 | 3270815 | 4 | 91.5796 | 78.6721 | -116.5619 | 12.5939 | 110.6574 | 0.0123 | 0.0117 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412258_E155FD91 | 504990 | 542 | -89.3 | 504990 | 298 | -90.3 | 504990 | 526 | -101.1 | 504990 | 382 |
| MR_1774412258_201B3CAE | 504990 | 542 | -86.7 | 504990 | 298 | -93.1 | 504990 | 526 | -102.8 | 504990 | 382 |
| MR_1774412258_8D1B4822 | 504990 | 542 | -87.3 | 504990 | 298 | -90.7 | 504990 | 526 | -99.8 | 504990 | 382 |
| MR_1774412258_804AF69B | 504990 | 542 | -88.7 | 504990 | 298 | -91.1 | 504990 | 526 | -101.5 | 504990 | 382 |
| MR_1774412258_FE856C16 | 504990 | 542 | -88.7 | 504990 | 298 | -92.4 | 504990 | 526 | -101.0 | 504990 | 382 |
| MR_1774412258_8EE716D4 | 504990 | 542 | -85.8 | 504990 | 298 | -90.0 | 504990 | 526 | -102.1 | 504990 | 382 |
| MR_1774412258_9EA0EEC6 | 504990 | 542 | -88.5 | 504990 | 298 | -92.5 | 504990 | 526 | -102.6 | 504990 | 382 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 861: `d2433566-a8c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d2433566-a8c7-44b0-84fb-8241ac7e7c3d` |
| Tag | **multiple-answer** |
| 정답 | **C6|C18** |
| C6 의미 | Increase transmission power for 3214418_2 |
| C18 의미 | Adjust the azimuth of 3214418_2 by 25 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[861] topology](images/train_0861.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3258511_1
- `C2`: Increase A3 Offset threshold for 3258511_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214418_2
- `C4`: Lift the tilt angle  of 3258511_1 by 5 degrees
- `C5`: Adjust the azimuth of 3258511_1 by 38 degrees
- `C6`: Increase transmission power for 3214418_2 **← 정답**
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214418_2
- `C8`: Press down the tilt angle  of 3258511_1 by 5 degrees
- `C9`: Decrease transmission power for 3258511_1
- `C10`: Check test server and transmission issues
- `C11`: Increase transmission power for 3258511_1
- `C12`: Add neighbor relationship between 3214418_2 and 3258511_1
- `C13`: Decrease A3 Offset threshold for 3214418_2
- `C14`: Add neighbor relationship between 3261998_3 and 3258511_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Lift the tilt angle of 3214418_2 by 10 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258511_1
- `C18`: Adjust the azimuth of 3214418_2 by 25 degrees **← 정답**
- `C19`: Decrease transmission power for 3214418_2
- `C20`: Increase A3 Offset threshold for 3214418_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258511_1
- `C22`: Press down the tilt angle of 3214418_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.512 | MS1 | 121.4656632722 | 31.1446241568 | 682 | 504990 | -92.43 | 16.16 | 503.74 | 0.08 | 2.44 | 1564 |
| 2024-09-20 22:21:32.807 | MS1 | 121.4656761774 | 31.1446234639 | 682 | 504990 | -85.04 | 12.95 | 346.55 | 0.15 | 2.85 | 1568 |
| 2024-09-20 22:21:33.450 | MS1 | 121.4656754642 | 31.1446301614 | 682 | 504990 | -87.07 | 12.98 | 411.05 | 0.03 | 2.11 | 1586 |
| 2024-09-20 22:21:34.215 | MS1 | 121.4656636224 | 31.1446266452 | 682 | 504990 | -108.11 | -0.14 | 72.35 | 0.06 | 1.47 | 1579 |
| 2024-09-20 22:21:35.471 | MS1 | 121.4656678066 | 31.1446251182 | 682 | 504990 | -107.68 | -0.04 | 50.26 | 0.09 | 1.22 | 1588 |
| 2024-09-20 22:21:36.743 | MS1 | 121.4656648877 | 31.1446336216 | 682 | 504990 | -108.70 | 0.89 | 31.18 | 0.02 | 1.40 | 1579 |
| 2024-09-20 22:21:37.664 | MS1 | 121.4656651214 | 31.1446366472 | 682 | 504990 | -104.72 | 1.36 | 34.96 | 0.01 | 1.18 | 1584 |
| 2024-09-20 22:21:38.613 | MS1 | 121.4656663476 | 31.1446244427 | 682 | 504990 | -108.90 | 0.07 | 15.58 | 0.09 | 1.18 | 1567 |
| 2024-09-20 22:21:39.496 | MS1 | 121.4656612152 | 31.1446379764 | 682 | 504990 | -106.52 | -0.52 | 68.60 | 0.04 | 1.11 | 1593 |
| 2024-09-20 22:21:40.317 | MS1 | 121.4656751027 | 31.1446305552 | 682 | 504990 | -90.63 | 15.60 | 446.71 | 0.06 | 2.46 | 1578 |
| 2024-09-20 22:21:41.159 | MS1 | 121.4656675966 | 31.1446267413 | 682 | 504990 | -90.73 | 15.91 | 502.48 | 0.04 | 2.66 | 1577 |
| 2024-09-20 22:21:42.535 | MS1 | 121.4656610048 | 31.1446225414 | 682 | 504990 | -85.54 | 15.92 | 422.14 | 0.15 | 2.33 | 1591 |

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
| 3214418 | 2 | 121.4679780983 | 31.1463320177 | 254 | 5 | 3 | 33.6 | TDD | 682 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3258511 | 1 | 121.4672864738 | 31.1544715236 | 150 | 4 | 12 | 22.7 | TDD | 401 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3261998 | 3 | 121.4640594902 | 31.1482987719 | 234 | 0 | 12 | 46.3 | TDD | 108 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3264035 | 4 | 121.4721352607 | 31.1500048612 | 340 | 4 | 0 | 19.6 | TDD | 21 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.424 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.528 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.528 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.741 | NREventA2 | measId:1;ServCellPCI:962;Se... |
| 2024-09-20 22:21:34.859 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258511 | 1 | 6.3090 | 19.8587 | -115.1035 | 9.7940 | 131.1583 | 0.0140 | 0.0010 |
| 2024_09_20 22:00 | 3214418 | 2 | 18.6054 | 6.1388 | -116.7427 | 11.0520 | 94.3609 | 0.1553 | 0.0009 |
| 2024_09_20 22:00 | 3261998 | 3 | 6.2683 | 19.2841 | -117.5602 | 17.7314 | 85.5083 | 0.0182 | 0.0032 |
| 2024_09_20 22:00 | 3264035 | 4 | 19.5689 | 13.1506 | -116.1362 | 12.6781 | 141.1354 | 0.0100 | 0.0016 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414587_CA7C8C8F | 504990 | 682 | -109.7 | 504990 | 401 | -114.8 | 504990 | 108 | -117.1 | 504990 | 21 |
| MR_1774414587_8BEBF71F | 504990 | 682 | -109.7 | 504990 | 401 | -113.2 | 504990 | 108 | -117.4 | 504990 | 21 |
| MR_1774414587_7297D4DD | 504990 | 682 | -109.5 | 504990 | 401 | -112.8 | 504990 | 108 | -116.8 | 504990 | 21 |
| MR_1774414587_0ACCDBAA | 504990 | 682 | -108.9 | 504990 | 401 | -112.3 | 504990 | 108 | -116.0 | 504990 | 21 |
| MR_1774414587_AD54BE0B | 504990 | 682 | -106.1 | 504990 | 401 | -114.2 | 504990 | 108 | -117.1 | 504990 | 21 |
| MR_1774414587_AC28B9D7 | 504990 | 682 | -109.7 | 504990 | 401 | -112.8 | 504990 | 108 | -118.5 | 504990 | 21 |
| MR_1774414587_F0B00E1B | 504990 | 682 | -107.4 | 504990 | 401 | -114.4 | 504990 | 108 | -119.3 | 504990 | 21 |
| MR_1774414587_EE1AA2ED | 504990 | 682 | -106.1 | 504990 | 401 | -112.6 | 504990 | 108 | -117.0 | 504990 | 21 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 862: `0822a3c3-b84...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0822a3c3-b84c-4359-bcb5-a153ea0dbfc8` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[862] topology](images/train_0862.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3245791_3 by 8 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245791_3
- `C3`: Decrease A3 Offset threshold for 3226387_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226387_4
- `C5`: Increase A3 Offset threshold for 3226387_4
- `C6`: Decrease A3 Offset threshold for 3245791_3
- `C7`: Adjust the azimuth of 3226387_4 by 50 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245791_3
- `C9`: Adjust the azimuth of 3245791_3 by 50 degrees
- `C10`: Insufficient data; more data is needed for judgment. **← 정답**
- `C11`: Decrease transmission power for 3245791_3
- `C12`: Increase transmission power for 3245791_3
- `C13`: Decrease transmission power for 3226387_4
- `C14`: Add neighbor relationship between 3249845_1 and 3226387_4
- `C15`: Add neighbor relationship between 3245791_3 and 3226387_4
- `C16`: Press down the tilt angle of 3245791_3 by 8 degrees
- `C17`: Increase transmission power for 3226387_4
- `C18`: Lift the tilt angle  of 3226387_4 by 10 degrees
- `C19`: Press down the tilt angle  of 3226387_4 by 10 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226387_4
- `C21`: Increase A3 Offset threshold for 3245791_3
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.326 | MS1 | 121.4656750362 | 31.1446205898 | 885 | 504990 | -85.14 | 15.64 | 310.43 | 0.17 | 2.32 | 1587 |
| 2024-09-20 22:21:32.248 | MS1 | 121.4656668213 | 31.1446358102 | 885 | 504990 | -90.72 | 17.11 | 422.28 | 0.14 | 2.51 | 1597 |
| 2024-09-20 22:21:33.109 | MS1 | 121.4656727466 | 31.1446319832 | 885 | 504990 | -89.72 | 14.78 | 398.06 | 0.18 | 2.98 | 1582 |
| 2024-09-20 22:21:34.535 | MS1 | 121.4656591701 | 31.1446201957 | 885 | 504990 | -90.42 | 15.60 | 91.33 | 0.13 | 2.57 | 1599 |
| 2024-09-20 22:21:35.515 | MS1 | 121.4656773118 | 31.1446313980 | 885 | 504990 | -88.93 | 17.38 | 91.42 | 0.13 | 2.00 | 1576 |
| 2024-09-20 22:21:36.292 | MS1 | 121.4656610153 | 31.1446319431 | 885 | 504990 | -89.04 | 14.20 | 107.44 | 0.06 | 2.86 | 1577 |
| 2024-09-20 22:21:37.127 | MS1 | 121.4656671497 | 31.1446272364 | 885 | 504990 | -90.53 | 12.35 | 51.93 | 0.02 | 2.50 | 1571 |
| 2024-09-20 22:21:38.961 | MS1 | 121.4656708688 | 31.1446208933 | 885 | 504990 | -92.51 | 8.25 | 43.59 | 0.08 | 2.93 | 1594 |
| 2024-09-20 22:21:39.953 | MS1 | 121.4656617444 | 31.1446205856 | 885 | 504990 | -92.38 | 12.57 | 97.85 | 0.19 | 2.88 | 1592 |
| 2024-09-20 22:21:40.895 | MS1 | 121.4656654147 | 31.1446354632 | 885 | 504990 | -89.54 | 11.94 | 375.68 | 0.00 | 2.25 | 1569 |
| 2024-09-20 22:21:41.130 | MS1 | 121.4656715858 | 31.1446282180 | 885 | 504990 | -92.09 | 9.66 | 298.66 | 0.06 | 2.59 | 1564 |
| 2024-09-20 22:21:42.329 | MS1 | 121.4656778977 | 31.1446229458 | 885 | 504990 | -89.50 | 11.02 | 550.91 | 0.00 | 2.31 | 1585 |

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
| 3226387 | 4 | 121.4640422986 | 31.1531907856 | 105 | 15 | 6 | 37.2 | TDD | 588 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3245791 | 3 | 121.4693368255 | 31.1493010219 | 320 | 5 | 10 | 31.0 | TDD | 885 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3249845 | 1 | 121.4702662170 | 31.1443005712 | 73 | 15 | 2 | 37.0 | TDD | 671 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3259273 | 2 | 121.4752096484 | 31.1559529965 | 274 | 8 | 6 | 20.7 | TDD | 676 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.116 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.138 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.276 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.276 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.934 | NREventA3 | measId:2;ServCellPCI:243;Se... |
| 2024-09-20 22:21:38.174 | NRHandoverAttempt | SourcePCI:243;SourceNR-ARFC... |
| 2024-09-20 22:21:38.209 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.220 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.362 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.362 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3249845 | 1 | 92.3625 | 75.9314 | -117.1604 | 10.8854 | 124.2176 | 0.0091 | 0.0138 |
| 2024_09_19 22:00 | 3259273 | 2 | 82.6365 | 84.7679 | -116.4334 | 19.3139 | 141.0153 | 0.0198 | 0.0064 |
| 2024_09_19 22:00 | 3245791 | 3 | 87.2748 | 93.3629 | -115.4866 | 9.2230 | 102.3180 | 0.0079 | 0.0129 |
| 2024_09_19 22:00 | 3226387 | 4 | 91.6506 | 94.8287 | -114.5634 | 11.4859 | 132.9104 | 0.0054 | 0.0022 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412201_021B98BD | 504990 | 885 | -90.3 | 504990 | 588 | -101.6 | 504990 | 671 | -104.4 | 504990 | 676 |
| MR_1774412201_991CBCD4 | 504990 | 885 | -91.0 | 504990 | 588 | -98.2 | 504990 | 671 | -103.3 | 504990 | 676 |
| MR_1774412201_EF883BFC | 504990 | 885 | -91.2 | 504990 | 588 | -101.6 | 504990 | 671 | -104.9 | 504990 | 676 |
| MR_1774412201_FE022FF1 | 504990 | 885 | -90.7 | 504990 | 588 | -99.7 | 504990 | 671 | -104.5 | 504990 | 676 |
| MR_1774412201_1887ABCD | 504990 | 885 | -90.1 | 504990 | 588 | -98.5 | 504990 | 671 | -103.9 | 504990 | 676 |
| MR_1774412201_55B876C9 | 504990 | 885 | -91.2 | 504990 | 588 | -101.2 | 504990 | 671 | -103.1 | 504990 | 676 |
| MR_1774412201_BF050BCC | 504990 | 885 | -91.1 | 504990 | 588 | -98.3 | 504990 | 671 | -105.7 | 504990 | 676 |
| MR_1774412201_843A4BD2 | 504990 | 885 | -91.6 | 504990 | 588 | -101.6 | 504990 | 671 | -105.6 | 504990 | 676 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 863: `fa53284c-f4e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fa53284c-f4e1-4ec6-81b8-0c787fcef5a1` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3274092_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[863] topology](images/train_0863.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3261489_3
- `C2`: Adjust the azimuth of 3274092_4 by 15 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Add neighbor relationship between 3269588_1 and 3261489_3
- `C5`: Lift the tilt angle of 3274092_4 by 4 degrees
- `C6`: Press down the tilt angle  of 3261489_3 by 3 degrees
- `C7`: Decrease transmission power for 3261489_3
- `C8`: Increase transmission power for 3261489_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261489_3
- `C10`: Decrease transmission power for 3274092_4
- `C11`: Adjust the azimuth of 3261489_3 by 50 degrees
- `C12`: Increase transmission power for 3274092_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261489_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274092_4
- `C15`: Lift the tilt angle  of 3261489_3 by 3 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274092_4 **← 정답**
- `C17`: Press down the tilt angle of 3274092_4 by 4 degrees
- `C18`: Check test server and transmission issues
- `C19`: Increase A3 Offset threshold for 3274092_4
- `C20`: Decrease A3 Offset threshold for 3274092_4
- `C21`: Increase A3 Offset threshold for 3261489_3
- `C22`: Add neighbor relationship between 3274092_4 and 3261489_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.510 | MS1 | 121.4656619567 | 31.1446308140 | 853 | 504990 | -90.92 | 13.83 | 422.33 | 0.06 | 2.95 | 1561 |
| 2024-09-20 22:21:32.566 | MS1 | 121.4656662877 | 31.1446378480 | 853 | 504990 | -89.83 | 13.10 | 376.15 | 0.19 | 2.96 | 1598 |
| 2024-09-20 22:21:33.661 | MS1 | 121.4656606899 | 31.1446355522 | 853 | 504990 | -91.70 | 14.35 | 479.37 | 0.18 | 2.19 | 1598 |
| 2024-09-20 22:21:34.409 | MS1 | 121.4656605180 | 31.1446312034 | 853 | 504990 | -87.90 | 15.10 | 71.47 | 0.69 | 2.22 | 595 |
| 2024-09-20 22:21:35.826 | MS1 | 121.4656772247 | 31.1446209957 | 853 | 504990 | -91.14 | 13.11 | 71.43 | 0.55 | 2.74 | 582 |
| 2024-09-20 22:21:36.294 | MS1 | 121.4656630683 | 31.1446369446 | 853 | 504990 | -87.58 | 15.77 | 57.73 | 0.51 | 2.58 | 546 |
| 2024-09-20 22:21:37.200 | MS1 | 121.4656699863 | 31.1446334651 | 853 | 504990 | -93.58 | 12.62 | 97.94 | 0.61 | 2.61 | 507 |
| 2024-09-20 22:21:38.776 | MS1 | 121.4656702823 | 31.1446232044 | 853 | 504990 | -91.41 | 8.62 | 104.30 | 0.52 | 2.28 | 580 |
| 2024-09-20 22:21:39.388 | MS1 | 121.4656765186 | 31.1446364149 | 853 | 504990 | -92.66 | 12.11 | 92.46 | 0.51 | 2.78 | 532 |
| 2024-09-20 22:21:40.363 | MS1 | 121.4656665404 | 31.1446242819 | 853 | 504990 | -89.80 | 12.49 | 489.47 | 0.12 | 2.21 | 1598 |
| 2024-09-20 22:21:41.488 | MS1 | 121.4656590480 | 31.1446368751 | 853 | 504990 | -90.04 | 11.87 | 555.33 | 0.10 | 2.78 | 1598 |
| 2024-09-20 22:21:42.660 | MS1 | 121.4656759613 | 31.1446330172 | 853 | 504990 | -92.57 | 11.62 | 353.79 | 0.08 | 2.61 | 1573 |

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
| 3261489 | 3 | 121.4726560959 | 31.1544447410 | 103 | 2 | 5 | 29.5 | TDD | 539 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3269588 | 1 | 121.4726184532 | 31.1519757230 | 335 | 0 | 2 | 46.0 | TDD | 448 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3270992 | 2 | 121.4693347012 | 31.1542191863 | 283 | 7 | 5 | 18.1 | TDD | 617 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3274092 | 4 | 121.4729949095 | 31.1479556380 | 227 | 2 | 7 | 22.5 | TDD | 853 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.481 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.502 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.607 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.607 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.281 | NREventA3 | measId:2;ServCellPCI:206;Se... |
| 2024-09-20 22:21:38.521 | NRHandoverAttempt | SourcePCI:206;SourceNR-ARFC... |
| 2024-09-20 22:21:38.570 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.585 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.734 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.734 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269588 | 1 | 6.1595 | 6.8647 | -114.3839 | 7.3577 | 197.3090 | 0.0147 | 0.0057 |
| 2024_09_20 22:00 | 3270992 | 2 | 8.3145 | 6.4896 | -114.2281 | 8.5446 | 102.9235 | 0.0177 | 0.0075 |
| 2024_09_20 22:00 | 3261489 | 3 | 10.2694 | 14.7995 | -115.9250 | 8.6872 | 89.4724 | 0.0170 | 0.0134 |
| 2024_09_20 22:00 | 3274092 | 4 | 13.3535 | 15.5616 | -114.4646 | 17.2517 | 193.4733 | 0.0038 | 0.0124 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412010_B4BD07E3 | 504990 | 853 | -88.2 | 504990 | 539 | -93.2 | 504990 | 448 | -94.1 | 504990 | 617 |
| MR_1774412010_148A938D | 504990 | 853 | -89.5 | 504990 | 539 | -93.2 | 504990 | 448 | -95.1 | 504990 | 617 |
| MR_1774412010_BC945C3E | 504990 | 853 | -86.0 | 504990 | 539 | -92.7 | 504990 | 448 | -95.4 | 504990 | 617 |
| MR_1774412010_33747277 | 504990 | 853 | -87.0 | 504990 | 539 | -91.7 | 504990 | 448 | -92.3 | 504990 | 617 |
| MR_1774412010_F2F0F445 | 504990 | 853 | -88.3 | 504990 | 539 | -91.7 | 504990 | 448 | -95.0 | 504990 | 617 |
| MR_1774412010_93CFAB18 | 504990 | 853 | -89.1 | 504990 | 539 | -90.7 | 504990 | 448 | -94.9 | 504990 | 617 |
| MR_1774412010_97AE4171 | 504990 | 853 | -89.5 | 504990 | 539 | -93.7 | 504990 | 448 | -94.0 | 504990 | 617 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 864: `fa14fb54-cc1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fa14fb54-cc12-4446-99a1-539acc946cd3` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease A3 Offset threshold for 3264264_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[864] topology](images/train_0864.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3228187_3 and 3254024_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254024_2
- `C3`: Add neighbor relationship between 3264264_4 and 3254024_2
- `C4`: Decrease transmission power for 3254024_2
- `C5`: Lift the tilt angle of 3264264_4 by 10 degrees
- `C6`: Increase transmission power for 3254024_2
- `C7`: Increase A3 Offset threshold for 3254024_2
- `C8`: Decrease A3 Offset threshold for 3264264_4 **← 정답**
- `C9`: Check test server and transmission issues
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264264_4
- `C11`: Increase A3 Offset threshold for 3264264_4
- `C12`: Decrease transmission power for 3264264_4
- `C13`: Decrease A3 Offset threshold for 3254024_2
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264264_4
- `C16`: Adjust the azimuth of 3254024_2 by 7 degrees
- `C17`: Lift the tilt angle  of 3254024_2 by 7 degrees
- `C18`: Press down the tilt angle of 3264264_4 by 10 degrees
- `C19`: Adjust the azimuth of 3264264_4 by 34 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254024_2
- `C21`: Increase transmission power for 3264264_4
- `C22`: Press down the tilt angle  of 3254024_2 by 7 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.405 | MS1 | 121.4656671824 | 31.1446217245 | 868 | 504990 | -79.12 | 15.56 | 465.03 | 0.16 | 2.55 | 1587 |
| 2024-09-20 22:21:32.517 | MS1 | 121.4656708433 | 31.1446191093 | 868 | 504990 | -82.06 | 12.96 | 520.28 | 0.06 | 2.25 | 1564 |
| 2024-09-20 22:21:33.126 | MS1 | 121.4656627629 | 31.1446270037 | 868 | 504990 | -84.79 | 13.55 | 514.33 | 0.02 | 2.52 | 1567 |
| 2024-09-20 22:21:34.848 | MS1 | 121.4656696947 | 31.1446333642 | 868 | 504990 | -90.42 | -3.68 | 54.78 | 0.04 | 1.04 | 1565 |
| 2024-09-20 22:21:35.596 | MS1 | 121.4656692263 | 31.1446197644 | 868 | 504990 | -91.83 | -0.88 | 55.32 | 0.06 | 1.39 | 1588 |
| 2024-09-20 22:21:36.725 | MS1 | 121.4656735856 | 31.1446236816 | 868 | 504990 | -83.35 | -0.67 | 52.79 | 0.19 | 1.48 | 1574 |
| 2024-09-20 22:21:37.971 | MS1 | 121.4656591136 | 31.1446264411 | 868 | 504990 | -83.15 | -1.00 | 37.54 | 0.02 | 1.07 | 1580 |
| 2024-09-20 22:21:38.954 | MS1 | 121.4656762228 | 31.1446300994 | 868 | 504990 | -92.45 | -1.03 | 48.89 | 0.16 | 1.01 | 1577 |
| 2024-09-20 22:21:39.490 | MS1 | 121.4656659293 | 31.1446233430 | 865 | 504990 | -80.81 | 12.50 | 291.90 | 0.18 | 1.21 | 1575 |
| 2024-09-20 22:21:40.885 | MS1 | 121.4656644655 | 31.1446192471 | 865 | 504990 | -81.31 | 13.04 | 321.87 | 0.10 | 2.69 | 1598 |
| 2024-09-20 22:21:41.967 | MS1 | 121.4656599858 | 31.1446181163 | 865 | 504990 | -79.50 | 14.20 | 484.55 | 0.02 | 2.89 | 1577 |
| 2024-09-20 22:21:42.730 | MS1 | 121.4656706453 | 31.1446223943 | 865 | 504990 | -75.83 | 14.84 | 538.40 | 0.03 | 2.63 | 1595 |

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
| 3228187 | 3 | 121.4735259954 | 31.1558952109 | 243 | 3 | 10 | 48.2 | TDD | 921 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3254024 | 2 | 121.4661455861 | 31.1508158505 | 191 | 5 | 4 | 28.7 | TDD | 865 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3264264 | 4 | 121.4681121507 | 31.1482532538 | 176 | 13 | 5 | 27.8 | TDD | 868 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3278775 | 1 | 121.4701819480 | 31.1532562405 | 156 | 15 | 8 | 19.0 | TDD | 80 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.781 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.806 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.910 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.910 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.608 | NREventA3 | measId:2;ServCellPCI:679;Se... |
| 2024-09-20 22:21:37.848 | NRHandoverAttempt | SourcePCI:679;SourceNR-ARFC... |
| 2024-09-20 22:21:37.880 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.894 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:37.997 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:37.997 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278775 | 1 | 12.0297 | 18.8468 | -117.8784 | 6.4370 | 187.4621 | 0.0162 | 0.0056 |
| 2024_09_20 22:00 | 3254024 | 2 | 16.2027 | 19.9843 | -116.0436 | 12.4406 | 162.7672 | 0.0175 | 0.0022 |
| 2024_09_20 22:00 | 3228187 | 3 | 12.8179 | 7.5074 | -117.6911 | 13.0174 | 137.9864 | 0.0129 | 0.0144 |
| 2024_09_20 22:00 | 3264264 | 4 | 9.3256 | 9.0727 | -115.9206 | 7.2153 | 172.3557 | 0.0109 | 0.1775 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413153_8E3CE8E1 | 504990 | 868 | -90.7 | 504990 | 865 | -87.6 | 504990 | 921 | -88.8 | 504990 | 80 |
| MR_1774413153_F39B5D99 | 504990 | 868 | -89.3 | 504990 | 865 | -88.1 | 504990 | 921 | -87.7 | 504990 | 80 |
| MR_1774413153_1323821E | 504990 | 868 | -92.2 | 504990 | 865 | -85.9 | 504990 | 921 | -87.6 | 504990 | 80 |
| MR_1774413153_488F34C8 | 504990 | 865 | -86.5 | 504990 | 868 | -91.2 | 504990 | 921 | -89.2 | 504990 | 80 |
| MR_1774413153_313B3891 | 504990 | 865 | -86.5 | 504990 | 868 | -88.6 | 504990 | 921 | -88.4 | 504990 | 80 |
| MR_1774413153_FD781879 | 504990 | 868 | -92.0 | 504990 | 865 | -86.1 | 504990 | 921 | -87.4 | 504990 | 80 |
| MR_1774413153_AEB54412 | 504990 | 868 | -92.2 | 504990 | 865 | -86.0 | 504990 | 921 | -88.9 | 504990 | 80 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 865: `98582184-e9f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `98582184-e9f8-4ecd-b38d-99b67e5ebd33` |
| Tag | **multiple-answer** |
| 정답 | **C4|C18** |
| C4 의미 | Adjust the azimuth of 3258328_3 by 50 degrees |
| C18 의미 | Increase transmission power for 3258328_3 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[865] topology](images/train_0865.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3242433_2
- `C2`: Add neighbor relationship between 3258328_3 and 3242433_2
- `C3`: Lift the tilt angle of 3258328_3 by 10 degrees
- `C4`: Adjust the azimuth of 3258328_3 by 50 degrees **← 정답**
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258328_3
- `C6`: Check test server and transmission issues
- `C7`: Press down the tilt angle  of 3242433_2 by 4 degrees
- `C8`: Lift the tilt angle  of 3242433_2 by 4 degrees
- `C9`: Press down the tilt angle of 3258328_3 by 10 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258328_3
- `C11`: Increase A3 Offset threshold for 3258328_3
- `C12`: Decrease transmission power for 3258328_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242433_2
- `C14`: Increase transmission power for 3242433_2
- `C15`: Add neighbor relationship between 3223174_4 and 3242433_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease A3 Offset threshold for 3258328_3
- `C18`: Increase transmission power for 3258328_3 **← 정답**
- `C19`: Adjust the azimuth of 3242433_2 by 10 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242433_2
- `C21`: Decrease A3 Offset threshold for 3242433_2
- `C22`: Decrease transmission power for 3242433_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.271 | MS1 | 121.4656754406 | 31.1446344270 | 311 | 504990 | -87.52 | 16.21 | 474.98 | 0.17 | 2.42 | 1560 |
| 2024-09-20 22:21:32.422 | MS1 | 121.4656712910 | 31.1446368571 | 311 | 504990 | -88.09 | 13.80 | 577.96 | 0.17 | 2.41 | 1586 |
| 2024-09-20 22:21:33.726 | MS1 | 121.4656675006 | 31.1446308124 | 311 | 504990 | -90.19 | 17.35 | 541.82 | 0.14 | 2.86 | 1574 |
| 2024-09-20 22:21:34.726 | MS1 | 121.4656631074 | 31.1446231357 | 311 | 504990 | -108.97 | -1.90 | 38.10 | 0.17 | 1.49 | 1593 |
| 2024-09-20 22:21:35.845 | MS1 | 121.4656692803 | 31.1446234726 | 311 | 504990 | -106.66 | 1.65 | 70.84 | 0.12 | 1.04 | 1561 |
| 2024-09-20 22:21:36.444 | MS1 | 121.4656635341 | 31.1446345935 | 311 | 504990 | -109.97 | -0.03 | 37.64 | 0.19 | 1.18 | 1587 |
| 2024-09-20 22:21:37.150 | MS1 | 121.4656740718 | 31.1446230709 | 311 | 504990 | -104.21 | -0.65 | 49.99 | 0.13 | 1.17 | 1562 |
| 2024-09-20 22:21:38.453 | MS1 | 121.4656586334 | 31.1446263175 | 311 | 504990 | -104.29 | -1.87 | 27.61 | 0.08 | 1.19 | 1563 |
| 2024-09-20 22:21:39.592 | MS1 | 121.4656755328 | 31.1446206675 | 311 | 504990 | -108.89 | -1.65 | 67.07 | 0.02 | 1.25 | 1590 |
| 2024-09-20 22:21:40.988 | MS1 | 121.4656620808 | 31.1446202761 | 311 | 504990 | -85.74 | 16.45 | 429.74 | 0.14 | 2.20 | 1568 |
| 2024-09-20 22:21:41.386 | MS1 | 121.4656740135 | 31.1446371455 | 311 | 504990 | -86.66 | 13.56 | 321.02 | 0.01 | 2.07 | 1565 |
| 2024-09-20 22:21:42.147 | MS1 | 121.4656622289 | 31.1446361267 | 311 | 504990 | -86.48 | 14.51 | 564.07 | 0.20 | 2.91 | 1569 |

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
| 3216398 | 1 | 121.4726910084 | 31.1458742725 | 176 | 11 | 7 | 34.9 | TDD | 649 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3223174 | 4 | 121.4720437482 | 31.1475812642 | 270 | 0 | 4 | 22.2 | TDD | 703 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3242433 | 2 | 121.4688375265 | 31.1442692477 | 287 | 1 | 4 | 17.5 | TDD | 476 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3258328 | 3 | 121.4714893108 | 31.1495000731 | 153 | 14 | 7 | 32.4 | TDD | 311 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.116 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.140 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.285 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.285 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.471 | NREventA2 | measId:1;ServCellPCI:165;Se... |
| 2024-09-20 22:21:34.617 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216398 | 1 | 14.3832 | 6.8627 | -116.5270 | 10.5626 | 165.6838 | 0.0070 | 0.0016 |
| 2024_09_20 22:00 | 3242433 | 2 | 17.9472 | 5.6428 | -116.4903 | 18.1692 | 136.1971 | 0.0058 | 0.0096 |
| 2024_09_20 22:00 | 3258328 | 3 | 18.5257 | 12.0642 | -114.8983 | 18.5241 | 139.1938 | 0.1350 | 0.0009 |
| 2024_09_20 22:00 | 3223174 | 4 | 8.7245 | 10.2058 | -117.2255 | 10.7781 | 158.3762 | 0.0132 | 0.0001 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412399_5C74CE0E | 504990 | 311 | -110.8 | 504990 | 476 | -113.9 | 504990 | 703 | -120.3 | 504990 | 649 |
| MR_1774412399_AD9D58BC | 504990 | 311 | -107.7 | 504990 | 476 | -114.5 | 504990 | 703 | -119.5 | 504990 | 649 |
| MR_1774412399_0C186128 | 504990 | 311 | -108.4 | 504990 | 476 | -114.6 | 504990 | 703 | -121.0 | 504990 | 649 |
| MR_1774412399_5359E3D6 | 504990 | 311 | -109.7 | 504990 | 476 | -113.5 | 504990 | 703 | -119.3 | 504990 | 649 |
| MR_1774412399_BC9EE53E | 504990 | 311 | -110.8 | 504990 | 476 | -111.6 | 504990 | 703 | -120.7 | 504990 | 649 |
| MR_1774412399_7AA6F0BB | 504990 | 311 | -109.9 | 504990 | 476 | -113.4 | 504990 | 703 | -121.2 | 504990 | 649 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 866: `38e29454-c4b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `38e29454-c4b9-4487-a8d7-c210f0c6e7bd` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232492_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[866] topology](images/train_0866.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3244745_3 by 5 degrees
- `C2`: Increase A3 Offset threshold for 3244745_3
- `C3`: Lift the tilt angle  of 3244745_3 by 5 degrees
- `C4`: Adjust the azimuth of 3244745_3 by 48 degrees
- `C5`: Decrease A3 Offset threshold for 3244745_3
- `C6`: Increase A3 Offset threshold for 3232492_5
- `C7`: Add neighbor relationship between 3232492_5 and 3244745_3
- `C8`: Adjust the azimuth of 3232492_5 by 36 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244745_3
- `C10`: Decrease transmission power for 3244745_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232492_5 **← 정답**
- `C12`: Decrease A3 Offset threshold for 3232492_5
- `C13`: Lift the tilt angle of 3232492_5 by 2 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244745_3
- `C15`: Add neighbor relationship between 3266284_10 and 3244745_3
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase transmission power for 3232492_5
- `C18`: Press down the tilt angle of 3232492_5 by 2 degrees
- `C19`: Check test server and transmission issues
- `C20`: Increase transmission power for 3244745_3
- `C21`: Decrease transmission power for 3232492_5
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232492_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.231 | MS1 | 121.4656677445 | 31.1446184655 | 541 | 504990 | -93.70 | 14.73 | 315.27 | 0.14 | 2.46 | 1562 |
| 2024-09-20 22:21:32.216 | MS1 | 121.4656756138 | 31.1446250071 | 862 | 504990 | -93.61 | 12.68 | 592.26 | 0.03 | 2.72 | 1560 |
| 2024-09-20 22:21:33.526 | MS1 | 121.4656750114 | 31.1446283323 | 142 | 504990 | -95.93 | 14.29 | 554.41 | 0.12 | 2.34 | 1593 |
| 2024-09-20 22:21:34.574 | MS1 | 121.4656645806 | 31.1446336388 | 456 | 152650 | -92.51 | 6.29 | 76.25 | 0.13 | 1.98 | 944 |
| 2024-09-20 22:21:35.532 | MS1 | 121.4656712921 | 31.1446376345 | 136 | 152650 | -90.17 | 6.08 | 86.11 | 0.11 | 1.56 | 973 |
| 2024-09-20 22:21:36.586 | MS1 | 121.4656633321 | 31.1446363963 | 843 | 152650 | -94.86 | 5.66 | 87.18 | 0.08 | 1.67 | 962 |
| 2024-09-20 22:21:37.923 | MS1 | 121.4656613640 | 31.1446316677 | 88 | 152650 | -92.97 | 6.51 | 79.12 | 0.01 | 1.61 | 990 |
| 2024-09-20 22:21:38.759 | MS1 | 121.4656701369 | 31.1446187884 | 456 | 152650 | -94.88 | 4.27 | 83.16 | 0.06 | 1.75 | 969 |
| 2024-09-20 22:21:39.761 | MS1 | 121.4656630128 | 31.1446299802 | 136 | 152650 | -94.63 | 5.64 | 70.01 | 0.14 | 1.96 | 971 |
| 2024-09-20 22:21:40.488 | MS1 | 121.4656638612 | 31.1446281052 | 843 | 152650 | -90.45 | 2.96 | 88.97 | 0.14 | 2.53 | 1591 |
| 2024-09-20 22:21:41.509 | MS1 | 121.4656699011 | 31.1446272973 | 88 | 152650 | -90.12 | 7.84 | 73.26 | 0.18 | 2.67 | 1579 |
| 2024-09-20 22:21:42.599 | MS1 | 121.4656603714 | 31.1446362174 | 456 | 152650 | -96.77 | 3.17 | 67.87 | 0.05 | 2.01 | 1565 |

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
| 3210301 | 4 | 121.4735693160 | 31.1507812628 | 3 | 1 | 7 | 19.9 | TDD | 316 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3226552 | 6 | 121.4753218082 | 31.1520939723 | 270 | 12 | 12 | 29.0 | TDD | 862 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3232492 | 5 | 121.4744400023 | 31.1556906138 | 178 | 1 | 9 | 15.7 | TDD | 541 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3233227 | 7 | 121.4724139783 | 31.1479786160 | 81 | 15 | 9 | 17.8 | FDD | 456 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3244745 | 3 | 121.4751025823 | 31.1539875910 | 173 | 5 | 5 | 5.7 | TDD | 848 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3247947 | 12 | 121.4713268178 | 31.1557750743 | 233 | 5 | 4 | 2.6 | FDD | 972 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3247959 | 8 | 121.4699747925 | 31.1541136504 | 330 | 7 | 6 | 6.9 | FDD | 136 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3248784 | 11 | 121.4644645398 | 31.1512965564 | 185 | 6 | 7 | 19.3 | FDD | 427 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3250406 | 13 | 121.4755026436 | 31.1472734657 | 327 | 2 | 10 | 8.3 | FDD | 88 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3266284 | 10 | 121.4729855575 | 31.1546804799 | 320 | 12 | 0 | 1.9 | FDD | 843 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3269777 | 2 | 121.4661279094 | 31.1547373891 | 263 | 2 | 1 | 3.5 | TDD | 750 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3276338 | 9 | 121.4744690437 | 31.1459385410 | 38 | 2 | 5 | 26.4 | FDD | 587 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3277672 | 1 | 121.4747613849 | 31.1553176018 | 233 | 10 | 4 | 3.2 | TDD | 142 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.949 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.965 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.092 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.092 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.831 | NREventA2 | measId:1;ServCellPCI:83;Ser... |
| 2024-09-20 22:21:34.978 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.179 | NREventA5 | measId:3;ServCellPCI:83;Ser... |
| 2024-09-20 22:21:35.219 | NRHandoverAttempt | SourcePCI:83;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.246 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.256 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.376 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.376 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277672 | 1 | 18.6395 | 19.2325 | -115.2721 | 6.8236 | 107.3422 | 0.0034 | 0.0103 |
| 2024_09_20 22:00 | 3269777 | 2 | 16.7181 | 6.7330 | -117.9718 | 12.8999 | 192.1555 | 0.0163 | 0.0004 |
| 2024_09_20 22:00 | 3244745 | 3 | 5.2460 | 11.1569 | -117.2191 | 7.5644 | 190.2505 | 0.0161 | 0.0144 |
| 2024_09_20 22:00 | 3210301 | 4 | 5.3460 | 12.8384 | -114.3879 | 7.9066 | 186.5897 | 0.0185 | 0.0116 |
| 2024_09_20 22:00 | 3232492 | 5 | 7.8971 | 12.9726 | -116.3753 | 16.7034 | 177.1944 | 0.0089 | 0.0070 |
| 2024_09_20 22:00 | 3226552 | 6 | 5.1078 | 6.2106 | -114.9704 | 13.5083 | 135.5080 | 0.0078 | 0.0039 |
| 2024_09_20 22:00 | 3233227 | 7 | 5.5576 | 17.8938 | -116.7498 | 4.7843 | 42.7817 | 0.0135 | 0.0102 |
| 2024_09_20 22:00 | 3247959 | 8 | 18.3601 | 12.0290 | -117.2164 | 4.2852 | 31.4476 | 0.0174 | 0.0053 |
| 2024_09_20 22:00 | 3276338 | 9 | 12.9299 | 13.4900 | -117.4144 | 3.1195 | 51.5629 | 0.0114 | 0.0161 |
| 2024_09_20 22:00 | 3266284 | 10 | 18.2299 | 8.6594 | -114.7816 | 4.3743 | 41.0793 | 0.0028 | 0.0165 |
| 2024_09_20 22:00 | 3248784 | 11 | 15.0116 | 16.8280 | -117.0767 | 3.1890 | 57.9313 | 0.0093 | 0.0171 |
| 2024_09_20 22:00 | 3247947 | 12 | 16.1748 | 13.3303 | -116.8063 | 3.5035 | 31.7175 | 0.0040 | 0.0053 |
| 2024_09_20 22:00 | 3250406 | 13 | 16.0042 | 6.2203 | -114.8718 | 4.6366 | 28.1502 | 0.0071 | 0.0108 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414946_821E8317 | 152650 | 456 | -90.5 | 152650 | 587 | -101.5 | 152650 | 427 | -99.1 | 152650 | 972 |
| MR_1774414946_3E772E61 | 504990 | 142 | -97.7 | 504990 | 848 | -96.6 | 504990 | 750 | -101.2 | 504990 | 316 |
| MR_1774414946_511B807C | 504990 | 142 | -96.7 | 504990 | 848 | -96.2 | 504990 | 750 | -100.6 | 504990 | 316 |
| MR_1774414946_4415E9D5 | 152650 | 456 | -90.8 | 152650 | 587 | -101.3 | 152650 | 427 | -100.2 | 152650 | 972 |
| MR_1774414946_1C8C3395 | 504990 | 142 | -97.3 | 504990 | 848 | -96.6 | 504990 | 750 | -100.1 | 504990 | 316 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 867: `b973a6dc-3a5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b973a6dc-3a54-4c76-a990-55da5040b021` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226915_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[867] topology](images/train_0867.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3226883_12 and 3221578_4
- `C2`: Adjust the azimuth of 3221578_4 by 35 degrees
- `C3`: Check test server and transmission issues
- `C4`: Decrease A3 Offset threshold for 3221578_4
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Press down the tilt angle of 3226915_2 by 3 degrees
- `C7`: Decrease transmission power for 3221578_4
- `C8`: Lift the tilt angle  of 3221578_4 by 3 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226915_2
- `C10`: Decrease A3 Offset threshold for 3226915_2
- `C11`: Increase A3 Offset threshold for 3221578_4
- `C12`: Increase transmission power for 3226915_2
- `C13`: Increase transmission power for 3221578_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226915_2 **← 정답**
- `C15`: Press down the tilt angle  of 3221578_4 by 3 degrees
- `C16`: Add neighbor relationship between 3226915_2 and 3221578_4
- `C17`: Adjust the azimuth of 3226915_2 by 32 degrees
- `C18`: Lift the tilt angle of 3226915_2 by 3 degrees
- `C19`: Decrease transmission power for 3226915_2
- `C20`: Increase A3 Offset threshold for 3226915_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221578_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221578_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.237 | MS1 | 121.4656747918 | 31.1446245009 | 808 | 504990 | -93.62 | 11.94 | 402.53 | 0.18 | 2.27 | 1600 |
| 2024-09-20 22:21:32.480 | MS1 | 121.4656697992 | 31.1446346067 | 423 | 504990 | -95.37 | 13.17 | 338.80 | 0.19 | 2.17 | 1595 |
| 2024-09-20 22:21:33.698 | MS1 | 121.4656747857 | 31.1446257401 | 662 | 504990 | -95.57 | 9.30 | 327.94 | 0.19 | 2.11 | 1578 |
| 2024-09-20 22:21:34.750 | MS1 | 121.4656583850 | 31.1446236994 | 293 | 152650 | -94.92 | 2.73 | 81.70 | 0.18 | 1.78 | 961 |
| 2024-09-20 22:21:35.416 | MS1 | 121.4656752467 | 31.1446323617 | 907 | 152650 | -95.77 | 2.21 | 83.28 | 0.18 | 1.58 | 971 |
| 2024-09-20 22:21:36.584 | MS1 | 121.4656744275 | 31.1446278738 | 602 | 152650 | -87.46 | 2.72 | 85.88 | 0.15 | 1.54 | 978 |
| 2024-09-20 22:21:37.995 | MS1 | 121.4656705070 | 31.1446317128 | 411 | 152650 | -89.10 | 7.49 | 77.00 | 0.02 | 1.62 | 953 |
| 2024-09-20 22:21:38.446 | MS1 | 121.4656715347 | 31.1446339626 | 293 | 152650 | -94.97 | 2.25 | 80.48 | 0.02 | 1.53 | 967 |
| 2024-09-20 22:21:39.423 | MS1 | 121.4656716573 | 31.1446351455 | 907 | 152650 | -87.46 | 2.48 | 72.21 | 0.19 | 1.60 | 999 |
| 2024-09-20 22:21:40.805 | MS1 | 121.4656761372 | 31.1446217599 | 602 | 152650 | -91.11 | 5.39 | 62.52 | 0.13 | 2.24 | 1563 |
| 2024-09-20 22:21:41.275 | MS1 | 121.4656687941 | 31.1446181507 | 411 | 152650 | -88.27 | 5.57 | 60.34 | 0.19 | 2.73 | 1571 |
| 2024-09-20 22:21:42.955 | MS1 | 121.4656664579 | 31.1446241853 | 293 | 152650 | -87.46 | 4.61 | 67.13 | 0.09 | 2.01 | 1570 |

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
| 3216031 | 10 | 121.4702423224 | 31.1479379475 | 28 | 15 | 4 | 21.8 | FDD | 49 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3221578 | 4 | 121.4646415251 | 31.1511426180 | 207 | 2 | 0 | 18.9 | TDD | 136 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3224244 | 8 | 121.4646951580 | 31.1494350982 | 269 | 0 | 12 | 3.6 | FDD | 907 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3225939 | 5 | 121.4755137918 | 31.1488951119 | 92 | 2 | 0 | 0.1 | TDD | 12 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3226883 | 12 | 121.4711203937 | 31.1475122895 | 118 | 4 | 8 | 20.1 | FDD | 602 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3226915 | 2 | 121.4657902500 | 31.1558401215 | 213 | 3 | 11 | 0.2 | TDD | 808 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3234747 | 7 | 121.4729426732 | 31.1461623375 | 350 | 1 | 8 | 16.0 | FDD | 293 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3249044 | 6 | 121.4752269356 | 31.1538976376 | 128 | 0 | 8 | 4.9 | TDD | 662 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3254974 | 1 | 121.4691656429 | 31.1466608764 | 78 | 6 | 7 | 18.0 | TDD | 423 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3261091 | 11 | 121.4719278848 | 31.1538981381 | 265 | 1 | 7 | 24.6 | FDD | 342 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3267666 | 9 | 121.4727648270 | 31.1456090454 | 67 | 5 | 10 | 8.4 | FDD | 621 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3268012 | 13 | 121.4756782893 | 31.1534006229 | 14 | 8 | 6 | 25.3 | FDD | 411 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3268694 | 3 | 121.4688321770 | 31.1535198375 | 0 | 10 | 6 | 5.3 | TDD | 40 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.412 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.551 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.551 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.238 | NREventA2 | measId:1;ServCellPCI:479;Se... |
| 2024-09-20 22:21:35.339 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.544 | NREventA5 | measId:3;ServCellPCI:479;Se... |
| 2024-09-20 22:21:35.592 | NRHandoverAttempt | SourcePCI:479;SourceNR-ARFC... |
| 2024-09-20 22:21:35.627 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.640 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.747 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.747 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254974 | 1 | 19.1601 | 11.8368 | -116.9633 | 7.9244 | 134.6289 | 0.0177 | 0.0026 |
| 2024_09_20 22:00 | 3226915 | 2 | 6.7446 | 14.0950 | -114.5598 | 15.7706 | 195.8233 | 0.0181 | 0.0117 |
| 2024_09_20 22:00 | 3268694 | 3 | 10.7022 | 6.5199 | -114.8613 | 13.2629 | 147.9113 | 0.0028 | 0.0000 |
| 2024_09_20 22:00 | 3221578 | 4 | 5.6357 | 13.4885 | -115.6932 | 11.6476 | 164.7470 | 0.0107 | 0.0097 |
| 2024_09_20 22:00 | 3225939 | 5 | 19.2248 | 18.9016 | -114.5011 | 15.0612 | 85.8760 | 0.0078 | 0.0121 |
| 2024_09_20 22:00 | 3249044 | 6 | 15.6787 | 11.6913 | -117.2281 | 19.6736 | 100.3084 | 0.0137 | 0.0073 |
| 2024_09_20 22:00 | 3234747 | 7 | 15.4427 | 17.8049 | -115.8749 | 4.2701 | 28.5469 | 0.0167 | 0.0188 |
| 2024_09_20 22:00 | 3224244 | 8 | 9.6225 | 13.1952 | -116.1267 | 3.7877 | 26.3328 | 0.0058 | 0.0068 |
| 2024_09_20 22:00 | 3267666 | 9 | 7.6371 | 19.0470 | -117.4609 | 4.6739 | 56.6256 | 0.0030 | 0.0197 |
| 2024_09_20 22:00 | 3216031 | 10 | 5.2779 | 13.2781 | -117.8621 | 4.1987 | 21.4148 | 0.0042 | 0.0039 |
| 2024_09_20 22:00 | 3261091 | 11 | 7.8009 | 13.1190 | -114.5369 | 4.8654 | 31.8197 | 0.0110 | 0.0179 |
| 2024_09_20 22:00 | 3226883 | 12 | 8.4348 | 15.8856 | -117.1814 | 4.1006 | 36.2804 | 0.0124 | 0.0092 |
| 2024_09_20 22:00 | 3268012 | 13 | 12.9888 | 13.1883 | -116.6173 | 4.2464 | 50.7338 | 0.0080 | 0.0099 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415958_00264AC6 | 504990 | 662 | -97.3 | 504990 | 136 | -93.7 | 504990 | 40 | -96.1 | 504990 | 12 |
| MR_1774415958_63F6B420 | 504990 | 662 | -94.5 | 504990 | 136 | -93.8 | 504990 | 40 | -93.9 | 504990 | 12 |
| MR_1774415958_EE99B8FD | 152650 | 293 | -93.8 | 152650 | 342 | -100.9 | 152650 | 49 | -105.1 | 152650 | 621 |
| MR_1774415958_6FA36684 | 152650 | 293 | -96.5 | 152650 | 342 | -103.1 | 152650 | 49 | -102.7 | 152650 | 621 |
| MR_1774415958_BC3EC7AC | 504990 | 662 | -94.3 | 504990 | 136 | -93.6 | 504990 | 40 | -97.6 | 504990 | 12 |
| MR_1774415958_4A13BD09 | 152650 | 293 | -92.9 | 152650 | 342 | -103.1 | 152650 | 49 | -106.7 | 152650 | 621 |
| MR_1774415958_3DAE6402 | 152650 | 293 | -95.3 | 152650 | 342 | -101.9 | 152650 | 49 | -106.2 | 152650 | 621 |
| MR_1774415958_16882E2A | 504990 | 662 | -94.1 | 504990 | 136 | -92.4 | 504990 | 40 | -97.6 | 504990 | 12 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 868: `583e284f-d01...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `583e284f-d011-401e-830b-3902e8a25e22` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3257813_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[868] topology](images/train_0868.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3257813_1
- `C2`: Decrease transmission power for 3237949_4
- `C3`: Increase transmission power for 3257813_1
- `C4`: Adjust the azimuth of 3257813_1 by 0 degrees
- `C5`: Lift the tilt angle  of 3237949_4 by 5 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237949_4
- `C7`: Press down the tilt angle  of 3237949_4 by 5 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237949_4
- `C9`: Increase A3 Offset threshold for 3237949_4
- `C10`: Decrease A3 Offset threshold for 3237949_4
- `C11`: Add neighbor relationship between 3239921_2 and 3237949_4
- `C12`: Add neighbor relationship between 3257813_1 and 3237949_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257813_1 **← 정답**
- `C14`: Increase A3 Offset threshold for 3257813_1
- `C15`: Press down the tilt angle of 3257813_1 by 6 degrees
- `C16`: Decrease transmission power for 3257813_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257813_1
- `C18`: Check test server and transmission issues
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase transmission power for 3237949_4
- `C21`: Adjust the azimuth of 3237949_4 by 50 degrees
- `C22`: Lift the tilt angle of 3257813_1 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.478 | MS1 | 121.4656642032 | 31.1446264910 | 760 | 504990 | -90.64 | 16.76 | 451.18 | 0.17 | 2.01 | 1568 |
| 2024-09-20 22:21:32.306 | MS1 | 121.4656619961 | 31.1446368362 | 760 | 504990 | -85.27 | 14.46 | 294.46 | 0.06 | 2.14 | 1593 |
| 2024-09-20 22:21:33.962 | MS1 | 121.4656641047 | 31.1446216932 | 760 | 504990 | -91.49 | 15.58 | 518.72 | 0.04 | 2.15 | 1587 |
| 2024-09-20 22:21:34.571 | MS1 | 121.4656655151 | 31.1446235529 | 760 | 504990 | -86.00 | 17.26 | 73.11 | 0.54 | 2.47 | 649 |
| 2024-09-20 22:21:35.533 | MS1 | 121.4656606854 | 31.1446242070 | 760 | 504990 | -90.71 | 12.78 | 79.03 | 0.64 | 2.84 | 664 |
| 2024-09-20 22:21:36.945 | MS1 | 121.4656779860 | 31.1446326579 | 760 | 504990 | -88.96 | 13.92 | 49.92 | 0.59 | 2.81 | 646 |
| 2024-09-20 22:21:37.365 | MS1 | 121.4656701912 | 31.1446372704 | 760 | 504990 | -89.08 | 10.06 | 57.05 | 0.67 | 2.93 | 504 |
| 2024-09-20 22:21:38.733 | MS1 | 121.4656597816 | 31.1446282398 | 760 | 504990 | -92.96 | 9.30 | 102.42 | 0.51 | 2.94 | 531 |
| 2024-09-20 22:21:39.502 | MS1 | 121.4656694177 | 31.1446284682 | 760 | 504990 | -92.43 | 12.87 | 53.62 | 0.68 | 2.02 | 519 |
| 2024-09-20 22:21:40.388 | MS1 | 121.4656617803 | 31.1446339817 | 760 | 504990 | -92.64 | 10.69 | 581.43 | 0.17 | 2.14 | 1579 |
| 2024-09-20 22:21:41.108 | MS1 | 121.4656735798 | 31.1446187119 | 760 | 504990 | -93.17 | 7.84 | 364.76 | 0.19 | 2.24 | 1565 |
| 2024-09-20 22:21:42.614 | MS1 | 121.4656767530 | 31.1446349045 | 760 | 504990 | -91.77 | 12.53 | 558.06 | 0.09 | 2.12 | 1591 |

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
| 3220277 | 3 | 121.4707001622 | 31.1474853654 | 114 | 1 | 11 | 26.1 | TDD | 966 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3237949 | 4 | 121.4754656618 | 31.1541744426 | 21 | 4 | 3 | 18.1 | TDD | 440 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3239921 | 2 | 121.4701547255 | 31.1546900162 | 144 | 6 | 12 | 20.4 | TDD | 624 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3257813 | 1 | 121.4707585507 | 31.1536077801 | 206 | 4 | 8 | 36.7 | TDD | 760 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.900 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.916 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.036 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.036 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.769 | NREventA3 | measId:2;ServCellPCI:844;Se... |
| 2024-09-20 22:21:38.009 | NRHandoverAttempt | SourcePCI:844;SourceNR-ARFC... |
| 2024-09-20 22:21:38.043 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.057 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.172 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.172 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257813 | 1 | 17.4518 | 14.3277 | -117.5824 | 18.3842 | 175.1596 | 0.0071 | 0.0092 |
| 2024_09_20 22:00 | 3239921 | 2 | 5.7488 | 10.7690 | -115.6216 | 13.8972 | 119.0783 | 0.0037 | 0.0016 |
| 2024_09_20 22:00 | 3220277 | 3 | 16.0703 | 17.5210 | -117.6590 | 16.5664 | 186.7163 | 0.0095 | 0.0045 |
| 2024_09_20 22:00 | 3237949 | 4 | 15.7661 | 9.3740 | -117.8602 | 13.4359 | 102.6872 | 0.0071 | 0.0157 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417222_8F079A82 | 504990 | 760 | -87.6 | 504990 | 440 | -89.7 | 504990 | 624 | -98.4 | 504990 | 966 |
| MR_1774417222_9074EB26 | 504990 | 760 | -86.7 | 504990 | 440 | -92.5 | 504990 | 624 | -97.4 | 504990 | 966 |
| MR_1774417222_53FFF028 | 504990 | 760 | -84.8 | 504990 | 440 | -92.6 | 504990 | 624 | -99.3 | 504990 | 966 |
| MR_1774417222_86816BC8 | 504990 | 760 | -85.1 | 504990 | 440 | -90.1 | 504990 | 624 | -98.0 | 504990 | 966 |
| MR_1774417222_508A00AE | 504990 | 760 | -87.2 | 504990 | 440 | -92.2 | 504990 | 624 | -98.9 | 504990 | 966 |
| MR_1774417222_2040A352 | 504990 | 760 | -86.4 | 504990 | 440 | -90.0 | 504990 | 624 | -97.5 | 504990 | 966 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 869: `5453d424-725...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5453d424-725d-4db2-98b6-c1c569093fe4` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[869] topology](images/train_0869.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3212537_3 and 3226862_2
- `C2`: Add neighbor relationship between 3275860_4 and 3226862_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275860_4
- `C4`: Decrease transmission power for 3275860_4
- `C5`: Press down the tilt angle  of 3226862_2 by 10 degrees
- `C6`: Decrease A3 Offset threshold for 3275860_4
- `C7`: Lift the tilt angle  of 3226862_2 by 10 degrees
- `C8`: Increase A3 Offset threshold for 3275860_4
- `C9`: Decrease A3 Offset threshold for 3226862_2
- `C10`: Press down the tilt angle of 3275860_4 by 8 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226862_2
- `C12`: Decrease transmission power for 3226862_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226862_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275860_4
- `C15`: Insufficient data; more data is needed for judgment. **← 정답**
- `C16`: Lift the tilt angle of 3275860_4 by 8 degrees
- `C17`: Adjust the azimuth of 3275860_4 by 50 degrees
- `C18`: Check test server and transmission issues
- `C19`: Increase transmission power for 3275860_4
- `C20`: Increase A3 Offset threshold for 3226862_2
- `C21`: Adjust the azimuth of 3226862_2 by 50 degrees
- `C22`: Increase transmission power for 3226862_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.203 | MS1 | 121.4656587807 | 31.1446321550 | 167 | 504990 | -91.91 | 16.52 | 505.87 | 0.09 | 2.53 | 1600 |
| 2024-09-20 22:21:32.374 | MS1 | 121.4656618946 | 31.1446256423 | 167 | 504990 | -87.72 | 15.79 | 295.19 | 0.15 | 2.31 | 1591 |
| 2024-09-20 22:21:33.644 | MS1 | 121.4656694321 | 31.1446292477 | 167 | 504990 | -86.28 | 12.39 | 298.50 | 0.14 | 2.73 | 1562 |
| 2024-09-20 22:21:34.547 | MS1 | 121.4656622181 | 31.1446217316 | 167 | 504990 | -87.20 | 13.05 | 56.03 | 0.14 | 2.75 | 1572 |
| 2024-09-20 22:21:35.352 | MS1 | 121.4656589704 | 31.1446323699 | 167 | 504990 | -91.14 | 15.10 | 87.72 | 0.11 | 2.96 | 1595 |
| 2024-09-20 22:21:36.460 | MS1 | 121.4656648197 | 31.1446262390 | 167 | 504990 | -88.60 | 14.76 | 73.68 | 0.10 | 2.81 | 1582 |
| 2024-09-20 22:21:37.582 | MS1 | 121.4656600836 | 31.1446203683 | 167 | 504990 | -91.17 | 10.00 | 74.18 | 0.01 | 2.32 | 1597 |
| 2024-09-20 22:21:38.315 | MS1 | 121.4656714710 | 31.1446238373 | 167 | 504990 | -90.49 | 12.33 | 60.76 | 0.05 | 2.07 | 1572 |
| 2024-09-20 22:21:39.360 | MS1 | 121.4656646475 | 31.1446332452 | 167 | 504990 | -92.73 | 10.65 | 71.67 | 0.09 | 2.65 | 1571 |
| 2024-09-20 22:21:40.670 | MS1 | 121.4656704684 | 31.1446220335 | 167 | 504990 | -93.64 | 10.10 | 340.63 | 0.01 | 2.61 | 1587 |
| 2024-09-20 22:21:41.684 | MS1 | 121.4656603346 | 31.1446194561 | 167 | 504990 | -89.80 | 8.25 | 572.15 | 0.05 | 2.09 | 1592 |
| 2024-09-20 22:21:42.139 | MS1 | 121.4656704856 | 31.1446376734 | 167 | 504990 | -92.83 | 7.04 | 383.39 | 0.00 | 2.70 | 1560 |

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
| 3212537 | 3 | 121.4738053870 | 31.1468571822 | 5 | 14 | 8 | 41.4 | TDD | 390 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3226862 | 2 | 121.4753699883 | 31.1464487455 | 142 | 14 | 8 | 33.7 | TDD | 100 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3269297 | 1 | 121.4712434237 | 31.1538221508 | 26 | 8 | 0 | 46.2 | TDD | 123 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3275860 | 4 | 121.4711265779 | 31.1487408260 | 99 | 5 | 0 | 34.6 | TDD | 167 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.248 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.269 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.399 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.399 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.069 | NREventA3 | measId:2;ServCellPCI:782;Se... |
| 2024-09-20 22:21:38.309 | NRHandoverAttempt | SourcePCI:782;SourceNR-ARFC... |
| 2024-09-20 22:21:38.342 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.356 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.476 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.476 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3269297 | 1 | 80.9911 | 78.2952 | -115.5852 | 8.9182 | 160.1062 | 0.0060 | 0.0098 |
| 2024_09_19 22:00 | 3226862 | 2 | 78.4510 | 81.2139 | -115.0791 | 9.2195 | 144.6405 | 0.0023 | 0.0080 |
| 2024_09_19 22:00 | 3212537 | 3 | 87.8032 | 84.4935 | -115.0146 | 17.9107 | 169.7210 | 0.0157 | 0.0065 |
| 2024_09_19 22:00 | 3275860 | 4 | 89.6043 | 79.5158 | -117.5369 | 12.9567 | 172.2239 | 0.0025 | 0.0110 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413756_6FF68ED9 | 504990 | 167 | -88.1 | 504990 | 100 | -93.5 | 504990 | 390 | -96.7 | 504990 | 123 |
| MR_1774413756_DA8B1D58 | 504990 | 167 | -88.0 | 504990 | 100 | -95.3 | 504990 | 390 | -98.8 | 504990 | 123 |
| MR_1774413756_1E4ABB70 | 504990 | 167 | -86.0 | 504990 | 100 | -93.4 | 504990 | 390 | -95.2 | 504990 | 123 |
| MR_1774413756_91F7AE94 | 504990 | 167 | -87.6 | 504990 | 100 | -93.1 | 504990 | 390 | -96.0 | 504990 | 123 |
| MR_1774413756_5F441B79 | 504990 | 167 | -87.4 | 504990 | 100 | -94.8 | 504990 | 390 | -96.3 | 504990 | 123 |
| MR_1774413756_A93EE8CC | 504990 | 167 | -86.6 | 504990 | 100 | -95.7 | 504990 | 390 | -95.2 | 504990 | 123 |
| MR_1774413756_D0A0C032 | 504990 | 167 | -87.9 | 504990 | 100 | -95.2 | 504990 | 390 | -98.7 | 504990 | 123 |

> *... 2개 열 생략 (전체 14열)*

---
