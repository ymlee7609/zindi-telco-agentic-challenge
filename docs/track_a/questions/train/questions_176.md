# Track A 문제 분석 — train[1750]~train[1759]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1750] ~ train[1759] (10개)

## 목차

1. [문제 1750: `492fcadd-b18...`](#1750) — single-answer, 정답: C14
2. [문제 1751: `141873ba-3e6...`](#1751) — single-answer, 정답: C17
3. [문제 1752: `e7083cd5-528...`](#1752) — single-answer, 정답: C7
4. [문제 1753: `cc6eb1dd-66f...`](#1753) — multiple-answer, 정답: C9|C19
5. [문제 1754: `ceeda3b5-d62...`](#1754) — single-answer, 정답: C15
6. [문제 1755: `c85b90b8-c26...`](#1755) — single-answer, 정답: C16
7. [문제 1756: `90365692-242...`](#1756) — single-answer, 정답: C6
8. [문제 1757: `cb8ce2cc-6a7...`](#1757) — single-answer, 정답: C9
9. [문제 1758: `dbd63231-d60...`](#1758) — single-answer, 정답: C20
10. [문제 1759: `1dcbb8a8-979...`](#1759) — single-answer, 정답: C9

---

### 문제 1750: `492fcadd-b18...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `492fcadd-b18b-4523-8c6b-4e560cf94ffa` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1750] topology](images/train_1750.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264325_4
- `C2`: Lift the tilt angle of 3253353_2 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253353_2
- `C4`: Increase A3 Offset threshold for 3264325_4
- `C5`: Press down the tilt angle  of 3264325_4 by 10 degrees
- `C6`: Decrease transmission power for 3253353_2
- `C7`: Increase A3 Offset threshold for 3253353_2
- `C8`: Lift the tilt angle  of 3264325_4 by 10 degrees
- `C9`: Add neighbor relationship between 3253353_2 and 3264325_4
- `C10`: Decrease A3 Offset threshold for 3253353_2
- `C11`: Increase transmission power for 3253353_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264325_4
- `C13`: Add neighbor relationship between 3275226_1 and 3264325_4
- `C14`: Check test server and transmission issues **← 정답**
- `C15`: Decrease transmission power for 3264325_4
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Adjust the azimuth of 3253353_2 by 32 degrees
- `C18`: Decrease A3 Offset threshold for 3264325_4
- `C19`: Press down the tilt angle of 3253353_2 by 10 degrees
- `C20`: Increase transmission power for 3264325_4
- `C21`: Adjust the azimuth of 3264325_4 by 50 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253353_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.198 | MS1 | 121.4656761595 | 31.1446220736 | 74 | 504990 | -86.63 | 15.17 | 358.22 | 0.03 | 2.93 | 1594 |
| 2024-09-20 22:21:32.959 | MS1 | 121.4656738783 | 31.1446374438 | 74 | 504990 | -85.64 | 16.40 | 398.85 | 0.07 | 2.09 | 1566 |
| 2024-09-20 22:21:33.699 | MS1 | 121.4656641710 | 31.1446284302 | 74 | 504990 | -89.94 | 17.12 | 401.80 | 0.07 | 2.40 | 1594 |
| 2024-09-20 22:21:34.232 | MS1 | 121.4656691423 | 31.1446222863 | 74 | 504990 | -90.58 | 12.32 | 86.83 | 0.17 | 2.55 | 376 |
| 2024-09-20 22:21:35.718 | MS1 | 121.4656684618 | 31.1446188426 | 74 | 504990 | -86.26 | 15.36 | 67.02 | 0.19 | 2.00 | 451 |
| 2024-09-20 22:21:36.745 | MS1 | 121.4656698131 | 31.1446186561 | 74 | 504990 | -91.01 | 16.62 | 52.85 | 0.12 | 2.25 | 315 |
| 2024-09-20 22:21:37.324 | MS1 | 121.4656596661 | 31.1446216848 | 74 | 504990 | -93.63 | 10.00 | 72.02 | 0.19 | 2.03 | 363 |
| 2024-09-20 22:21:38.570 | MS1 | 121.4656731156 | 31.1446199719 | 74 | 504990 | -93.74 | 8.12 | 74.35 | 0.12 | 2.24 | 408 |
| 2024-09-20 22:21:39.226 | MS1 | 121.4656759960 | 31.1446183866 | 74 | 504990 | -91.80 | 12.47 | 76.91 | 0.19 | 2.27 | 476 |
| 2024-09-20 22:21:40.879 | MS1 | 121.4656722107 | 31.1446316250 | 74 | 504990 | -91.54 | 11.14 | 537.62 | 0.16 | 2.08 | 1584 |
| 2024-09-20 22:21:41.868 | MS1 | 121.4656770991 | 31.1446294605 | 74 | 504990 | -91.65 | 7.10 | 459.46 | 0.01 | 2.48 | 1587 |
| 2024-09-20 22:21:42.819 | MS1 | 121.4656582017 | 31.1446371496 | 74 | 504990 | -89.59 | 7.14 | 463.76 | 0.03 | 2.22 | 1595 |

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
| 3253353 | 2 | 121.4741052235 | 31.1527178747 | 254 | 9 | 8 | 24.7 | TDD | 74 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3263877 | 3 | 121.4698231191 | 31.1451728247 | 186 | 1 | 9 | 17.2 | TDD | 77 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3264325 | 4 | 121.4711884247 | 31.1539310618 | 325 | 14 | 10 | 20.9 | TDD | 902 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3275226 | 1 | 121.4697697977 | 31.1515365762 | 232 | 3 | 3 | 16.9 | TDD | 80 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.990 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.015 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.144 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.144 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.861 | NREventA3 | measId:2;ServCellPCI:751;Se... |
| 2024-09-20 22:21:38.101 | NRHandoverAttempt | SourcePCI:751;SourceNR-ARFC... |
| 2024-09-20 22:21:38.145 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.156 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.282 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.282 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275226 | 1 | 11.3521 | 19.6056 | -114.0848 | 19.2870 | 99.3571 | 0.0196 | 0.0140 |
| 2024_09_20 22:00 | 3253353 | 2 | 6.0259 | 13.2106 | -114.2702 | 7.6108 | 126.5304 | 0.0065 | 0.0148 |
| 2024_09_20 22:00 | 3263877 | 3 | 7.6446 | 14.8703 | -117.0505 | 17.3327 | 131.5860 | 0.0195 | 0.0041 |
| 2024_09_20 22:00 | 3264325 | 4 | 16.1411 | 5.3373 | -115.3989 | 18.5317 | 114.3508 | 0.0070 | 0.0189 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416690_17244CF8 | 504990 | 74 | -91.2 | 504990 | 902 | -98.5 | 504990 | 80 | -99.6 | 504990 | 77 |
| MR_1774416690_40812268 | 504990 | 74 | -89.3 | 504990 | 902 | -99.0 | 504990 | 80 | -101.0 | 504990 | 77 |
| MR_1774416690_A8DCC082 | 504990 | 74 | -92.5 | 504990 | 902 | -99.0 | 504990 | 80 | -100.8 | 504990 | 77 |
| MR_1774416690_2C2A9ED3 | 504990 | 74 | -89.3 | 504990 | 902 | -97.6 | 504990 | 80 | -101.8 | 504990 | 77 |
| MR_1774416690_B0DED79A | 504990 | 74 | -90.0 | 504990 | 902 | -98.1 | 504990 | 80 | -100.3 | 504990 | 77 |
| MR_1774416690_44050DC4 | 504990 | 74 | -90.9 | 504990 | 902 | -100.7 | 504990 | 80 | -101.8 | 504990 | 77 |
| MR_1774416690_C6290017 | 504990 | 74 | -92.1 | 504990 | 902 | -98.7 | 504990 | 80 | -101.3 | 504990 | 77 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1751: `141873ba-3e6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `141873ba-3e69-4d3f-ad9e-d0cd6e5092a3` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Decrease A3 Offset threshold for 3235821_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1751] topology](images/train_1751.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3235821_2 by 1 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231134_4
- `C3`: Increase transmission power for 3235821_2
- `C4`: Adjust the azimuth of 3231134_4 by 50 degrees
- `C5`: Adjust the azimuth of 3235821_2 by 50 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231134_4
- `C7`: Decrease A3 Offset threshold for 3231134_4
- `C8`: Press down the tilt angle  of 3231134_4 by 6 degrees
- `C9`: Increase A3 Offset threshold for 3235821_2
- `C10`: Add neighbor relationship between 3235821_2 and 3231134_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235821_2
- `C12`: Lift the tilt angle  of 3231134_4 by 6 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease transmission power for 3235821_2
- `C15`: Check test server and transmission issues
- `C16`: Press down the tilt angle of 3235821_2 by 1 degrees
- `C17`: Decrease A3 Offset threshold for 3235821_2 **← 정답**
- `C18`: Increase transmission power for 3231134_4
- `C19`: Decrease transmission power for 3231134_4
- `C20`: Add neighbor relationship between 3269797_3 and 3231134_4
- `C21`: Increase A3 Offset threshold for 3231134_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235821_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.649 | MS1 | 121.4656689806 | 31.1446258713 | 131 | 504990 | -83.43 | 12.01 | 457.46 | 0.05 | 2.60 | 1579 |
| 2024-09-20 22:21:32.406 | MS1 | 121.4656765229 | 31.1446318633 | 131 | 504990 | -83.48 | 12.92 | 334.48 | 0.06 | 2.64 | 1591 |
| 2024-09-20 22:21:33.133 | MS1 | 121.4656674213 | 31.1446294939 | 131 | 504990 | -81.99 | 15.48 | 565.85 | 0.07 | 2.99 | 1565 |
| 2024-09-20 22:21:34.598 | MS1 | 121.4656581980 | 31.1446357167 | 131 | 504990 | -86.16 | -0.55 | 28.27 | 0.08 | 1.24 | 1571 |
| 2024-09-20 22:21:35.344 | MS1 | 121.4656748415 | 31.1446367864 | 131 | 504990 | -91.22 | -0.10 | 33.53 | 0.16 | 1.18 | 1598 |
| 2024-09-20 22:21:36.940 | MS1 | 121.4656759152 | 31.1446263126 | 131 | 504990 | -92.95 | -1.32 | 28.85 | 0.01 | 1.28 | 1578 |
| 2024-09-20 22:21:37.455 | MS1 | 121.4656747702 | 31.1446185674 | 131 | 504990 | -88.93 | -2.24 | 70.15 | 0.09 | 1.41 | 1561 |
| 2024-09-20 22:21:38.208 | MS1 | 121.4656604839 | 31.1446340229 | 131 | 504990 | -88.61 | -1.23 | 73.46 | 0.11 | 1.13 | 1577 |
| 2024-09-20 22:21:39.177 | MS1 | 121.4656672044 | 31.1446286301 | 830 | 504990 | -79.10 | 12.05 | 198.75 | 0.15 | 1.02 | 1573 |
| 2024-09-20 22:21:40.938 | MS1 | 121.4656651228 | 31.1446221704 | 830 | 504990 | -76.32 | 14.59 | 412.83 | 0.16 | 2.16 | 1560 |
| 2024-09-20 22:21:41.658 | MS1 | 121.4656588586 | 31.1446197351 | 830 | 504990 | -77.39 | 12.03 | 555.50 | 0.19 | 2.64 | 1599 |
| 2024-09-20 22:21:42.940 | MS1 | 121.4656622611 | 31.1446195739 | 830 | 504990 | -84.44 | 17.02 | 406.31 | 0.18 | 2.29 | 1600 |

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
| 3231134 | 4 | 121.4707945311 | 31.1480561235 | 175 | 4 | 7 | 26.1 | TDD | 830 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3235821 | 2 | 121.4743307507 | 31.1523461614 | 317 | 0 | 1 | 25.3 | TDD | 131 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3244854 | 1 | 121.4739228650 | 31.1508249708 | 193 | 4 | 9 | 45.9 | TDD | 770 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3269797 | 3 | 121.4736060519 | 31.1522921292 | 143 | 0 | 11 | 31.5 | TDD | 939 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.946 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.968 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.088 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.088 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.775 | NREventA3 | measId:2;ServCellPCI:753;Se... |
| 2024-09-20 22:21:38.015 | NRHandoverAttempt | SourcePCI:753;SourceNR-ARFC... |
| 2024-09-20 22:21:38.053 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.068 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.200 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.200 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244854 | 1 | 10.2825 | 19.4001 | -114.6167 | 16.1120 | 87.5026 | 0.0110 | 0.0166 |
| 2024_09_20 22:00 | 3235821 | 2 | 5.2215 | 8.6015 | -114.2475 | 17.0635 | 147.8706 | 0.0034 | 0.1620 |
| 2024_09_20 22:00 | 3269797 | 3 | 5.8301 | 19.8936 | -116.1698 | 10.0488 | 158.2483 | 0.0155 | 0.0068 |
| 2024_09_20 22:00 | 3231134 | 4 | 8.9759 | 19.0193 | -115.1365 | 9.9481 | 197.9049 | 0.0065 | 0.0119 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414714_91DEA20E | 504990 | 830 | -82.3 | 504990 | 131 | -84.7 | 504990 | 939 | -85.1 | 504990 | 770 |
| MR_1774414714_61C15154 | 504990 | 131 | -84.2 | 504990 | 830 | -81.6 | 504990 | 939 | -85.8 | 504990 | 770 |
| MR_1774414714_CC785380 | 504990 | 131 | -86.7 | 504990 | 830 | -83.7 | 504990 | 939 | -85.0 | 504990 | 770 |
| MR_1774414714_B4786B16 | 504990 | 830 | -83.6 | 504990 | 131 | -87.2 | 504990 | 939 | -85.6 | 504990 | 770 |
| MR_1774414714_8AC20C50 | 504990 | 131 | -85.8 | 504990 | 830 | -83.6 | 504990 | 939 | -83.6 | 504990 | 770 |
| MR_1774414714_E4E5CA69 | 504990 | 131 | -86.8 | 504990 | 830 | -82.4 | 504990 | 939 | -85.6 | 504990 | 770 |
| MR_1774414714_5D1692A6 | 504990 | 131 | -84.3 | 504990 | 830 | -82.9 | 504990 | 939 | -86.1 | 504990 | 770 |
| MR_1774414714_7D88BDD2 | 504990 | 131 | -87.3 | 504990 | 830 | -81.5 | 504990 | 939 | -84.7 | 504990 | 770 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1752: `e7083cd5-528...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e7083cd5-528a-4cb8-a194-67b4ec836b90` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Lift the tilt angle  of 3226688_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1752] topology](images/train_1752.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3211437_2
- `C2`: Increase A3 Offset threshold for 3211437_2
- `C3`: Add neighbor relationship between 3226688_4 and 3230310_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211437_2
- `C5`: Adjust the azimuth of 3226688_4 by 50 degrees
- `C6`: Add neighbor relationship between 3211437_2 and 3230310_1
- `C7`: Lift the tilt angle  of 3226688_4 by 10 degrees **← 정답**
- `C8`: Decrease A3 Offset threshold for 3211437_2
- `C9`: Press down the tilt angle  of 3226688_4 by 10 degrees
- `C10`: Decrease transmission power for 3230310_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211437_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230310_1
- `C14`: Press down the tilt angle of 3211437_2 by 2 degrees
- `C15`: Lift the tilt angle of 3211437_2 by 2 degrees
- `C16`: Increase transmission power for 3230310_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230310_1
- `C18`: Check test server and transmission issues
- `C19`: Increase A3 Offset threshold for 3230310_1
- `C20`: Adjust the azimuth of 3211437_2 by 12 degrees
- `C21`: Decrease A3 Offset threshold for 3230310_1
- `C22`: Decrease transmission power for 3211437_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.254 | MS1 | 121.4656753235 | 31.1446276764 | 297 | 504990 | -88.63 | 17.36 | 432.47 | 0.15 | 2.27 | 1594 |
| 2024-09-20 22:21:32.742 | MS1 | 121.4656581799 | 31.1446286242 | 297 | 504990 | -86.51 | 17.14 | 579.52 | 0.04 | 2.52 | 1586 |
| 2024-09-20 22:21:33.861 | MS1 | 121.4656586054 | 31.1446221424 | 297 | 504990 | -89.94 | 13.09 | 492.50 | 0.15 | 2.86 | 1598 |
| 2024-09-20 22:21:34.684 | MS1 | 121.4656717970 | 31.1446238102 | 297 | 504990 | -87.24 | 17.75 | 64.55 | 0.06 | 2.62 | 1579 |
| 2024-09-20 22:21:35.714 | MS1 | 121.4656699857 | 31.1446298887 | 297 | 504990 | -90.22 | 13.51 | 71.96 | 0.05 | 2.47 | 1599 |
| 2024-09-20 22:21:36.974 | MS1 | 121.4656653135 | 31.1446295515 | 297 | 504990 | -90.89 | 16.61 | 68.13 | 0.02 | 2.59 | 1584 |
| 2024-09-20 22:21:37.433 | MS1 | 121.4656755390 | 31.1446266060 | 297 | 504990 | -90.88 | 8.25 | 78.68 | 0.03 | 2.13 | 1560 |
| 2024-09-20 22:21:38.546 | MS1 | 121.4656687772 | 31.1446328300 | 297 | 504990 | -93.07 | 10.61 | 86.41 | 0.09 | 2.08 | 1596 |
| 2024-09-20 22:21:39.154 | MS1 | 121.4656698478 | 31.1446344255 | 297 | 504990 | -92.74 | 10.91 | 102.20 | 0.05 | 2.07 | 1572 |
| 2024-09-20 22:21:40.902 | MS1 | 121.4656609754 | 31.1446196997 | 297 | 504990 | -91.38 | 10.65 | 366.34 | 0.06 | 2.39 | 1594 |
| 2024-09-20 22:21:41.727 | MS1 | 121.4656705157 | 31.1446342309 | 297 | 504990 | -91.29 | 9.50 | 379.89 | 0.20 | 2.78 | 1599 |
| 2024-09-20 22:21:42.338 | MS1 | 121.4656597265 | 31.1446262156 | 297 | 504990 | -91.16 | 7.14 | 434.78 | 0.16 | 2.93 | 1599 |

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
| 3211437 | 2 | 121.4647214832 | 31.1551537970 | 188 | 1 | 9 | 20.3 | TDD | 297 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3226688 | 4 | 121.4673360916 | 31.1468422616 | 306 | 7 | 6 | 49.9 | TDD | 119 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3230310 | 1 | 121.4744961492 | 31.1487030232 | 4 | 8 | 11 | 33.5 | TDD | 647 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3264037 | 3 | 121.4722258246 | 31.1473980372 | 316 | 6 | 6 | 49.8 | TDD | 26 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.620 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.635 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.763 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.763 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.486 | NREventA3 | measId:2;ServCellPCI:402;Se... |
| 2024-09-20 22:21:38.726 | NRHandoverAttempt | SourcePCI:402;SourceNR-ARFC... |
| 2024-09-20 22:21:38.776 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.790 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.902 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.902 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230310 | 1 | 16.8088 | 10.1205 | -116.6243 | 5.1061 | 196.9027 | 0.0102 | 0.0188 |
| 2024_09_20 22:00 | 3211437 | 2 | 90.8522 | 83.4842 | -117.0752 | 7.3299 | 112.9588 | 0.0021 | 0.0084 |
| 2024_09_20 22:00 | 3264037 | 3 | 8.3475 | 12.0530 | -117.8180 | 17.1999 | 192.8796 | 0.0145 | 0.0138 |
| 2024_09_20 22:00 | 3226688 | 4 | 18.8283 | 14.3801 | -115.6970 | 15.8177 | 181.6568 | 0.0117 | 0.0195 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414412_A2424122 | 504990 | 297 | -87.1 | 504990 | 647 | -93.2 | 504990 | 119 | -94.6 | 504990 | 26 |
| MR_1774414412_BFAD235E | 504990 | 297 | -87.3 | 504990 | 647 | -93.5 | 504990 | 119 | -95.3 | 504990 | 26 |
| MR_1774414412_4539AC4F | 504990 | 297 | -85.3 | 504990 | 647 | -94.0 | 504990 | 119 | -95.2 | 504990 | 26 |
| MR_1774414412_8629BD63 | 504990 | 297 | -87.1 | 504990 | 647 | -95.0 | 504990 | 119 | -96.0 | 504990 | 26 |
| MR_1774414412_8111DC38 | 504990 | 297 | -88.2 | 504990 | 647 | -92.3 | 504990 | 119 | -94.6 | 504990 | 26 |
| MR_1774414412_79553F49 | 504990 | 297 | -86.8 | 504990 | 647 | -92.5 | 504990 | 119 | -94.9 | 504990 | 26 |
| MR_1774414412_A1D193CF | 504990 | 297 | -86.1 | 504990 | 647 | -94.5 | 504990 | 119 | -96.8 | 504990 | 26 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1753: `cc6eb1dd-66f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cc6eb1dd-66f7-4093-8bd6-5dd56cfab608` |
| Tag | **multiple-answer** |
| 정답 | **C9|C19** |
| C9 의미 | Increase transmission power for 3231361_3 |
| C19 의미 | Adjust the azimuth of 3231361_3 by 28 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1753] topology](images/train_1753.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3270840_2
- `C2`: Press down the tilt angle of 3231361_3 by 9 degrees
- `C3`: Increase A3 Offset threshold for 3231361_3
- `C4`: Press down the tilt angle  of 3270840_2 by 5 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270840_2
- `C6`: Add neighbor relationship between 3238453_1 and 3270840_2
- `C7`: Add neighbor relationship between 3231361_3 and 3270840_2
- `C8`: Lift the tilt angle of 3231361_3 by 9 degrees
- `C9`: Increase transmission power for 3231361_3 **← 정답**
- `C10`: Adjust the azimuth of 3270840_2 by 2 degrees
- `C11`: Decrease transmission power for 3231361_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270840_2
- `C13`: Increase transmission power for 3270840_2
- `C14`: Lift the tilt angle  of 3270840_2 by 5 degrees
- `C15`: Check test server and transmission issues
- `C16`: Decrease transmission power for 3270840_2
- `C17`: Increase A3 Offset threshold for 3270840_2
- `C18`: Decrease A3 Offset threshold for 3231361_3
- `C19`: Adjust the azimuth of 3231361_3 by 28 degrees **← 정답**
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231361_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231361_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.950 | MS1 | 121.4656658566 | 31.1446198373 | 750 | 504990 | -91.07 | 15.39 | 521.51 | 0.08 | 2.21 | 1599 |
| 2024-09-20 22:21:32.869 | MS1 | 121.4656763365 | 31.1446293616 | 750 | 504990 | -93.13 | 14.77 | 513.68 | 0.07 | 2.44 | 1588 |
| 2024-09-20 22:21:33.746 | MS1 | 121.4656711397 | 31.1446194976 | 750 | 504990 | -93.74 | 13.48 | 465.83 | 0.07 | 2.13 | 1570 |
| 2024-09-20 22:21:34.498 | MS1 | 121.4656738970 | 31.1446312005 | 750 | 504990 | -105.07 | 1.06 | 34.07 | 0.16 | 1.20 | 1567 |
| 2024-09-20 22:21:35.128 | MS1 | 121.4656761216 | 31.1446267314 | 750 | 504990 | -100.43 | -0.72 | 47.44 | 0.01 | 1.48 | 1580 |
| 2024-09-20 22:21:36.880 | MS1 | 121.4656766119 | 31.1446371831 | 750 | 504990 | -104.94 | 0.26 | 23.53 | 0.09 | 1.32 | 1566 |
| 2024-09-20 22:21:37.834 | MS1 | 121.4656716647 | 31.1446350955 | 750 | 504990 | -107.24 | -1.19 | 67.84 | 0.10 | 1.11 | 1596 |
| 2024-09-20 22:21:38.711 | MS1 | 121.4656652692 | 31.1446231237 | 750 | 504990 | -105.96 | 0.44 | 50.81 | 0.19 | 1.40 | 1575 |
| 2024-09-20 22:21:39.761 | MS1 | 121.4656637186 | 31.1446346327 | 750 | 504990 | -109.27 | 1.56 | 48.61 | 0.01 | 1.30 | 1585 |
| 2024-09-20 22:21:40.519 | MS1 | 121.4656628837 | 31.1446271967 | 750 | 504990 | -85.97 | 16.21 | 406.49 | 0.15 | 2.93 | 1573 |
| 2024-09-20 22:21:41.564 | MS1 | 121.4656656742 | 31.1446370031 | 750 | 504990 | -92.46 | 12.05 | 327.70 | 0.00 | 2.15 | 1563 |
| 2024-09-20 22:21:42.876 | MS1 | 121.4656744957 | 31.1446289416 | 750 | 504990 | -87.38 | 17.48 | 501.95 | 0.02 | 2.41 | 1576 |

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
| 3231361 | 3 | 121.4693369328 | 31.1443406900 | 303 | 2 | 1 | 40.6 | TDD | 750 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3237162 | 4 | 121.4680601371 | 31.1558894178 | 161 | 9 | 0 | 31.8 | TDD | 247 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3238453 | 1 | 121.4654932107 | 31.1463617348 | 153 | 7 | 12 | 38.8 | TDD | 338 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3270840 | 2 | 121.4721195801 | 31.1542172177 | 208 | 3 | 9 | 41.4 | TDD | 107 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.043 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.064 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.170 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.170 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.396 | NREventA2 | measId:1;ServCellPCI:384;Se... |
| 2024-09-20 22:21:34.522 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238453 | 1 | 6.5248 | 16.1281 | -116.1787 | 8.5652 | 197.4387 | 0.0083 | 0.0049 |
| 2024_09_20 22:00 | 3270840 | 2 | 19.3739 | 18.1453 | -117.7381 | 17.6623 | 109.4926 | 0.0178 | 0.0111 |
| 2024_09_20 22:00 | 3231361 | 3 | 16.1311 | 13.0656 | -114.0428 | 14.2325 | 147.8764 | 0.1465 | 0.0136 |
| 2024_09_20 22:00 | 3237162 | 4 | 18.4347 | 8.4029 | -116.7110 | 17.6373 | 172.0277 | 0.0064 | 0.0199 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414623_7E220FCD | 504990 | 750 | -103.7 | 504990 | 107 | -111.7 | 504990 | 338 | -115.5 | 504990 | 247 |
| MR_1774414623_A0FDC213 | 504990 | 750 | -104.9 | 504990 | 107 | -110.7 | 504990 | 338 | -113.8 | 504990 | 247 |
| MR_1774414623_C1091BF6 | 504990 | 750 | -105.3 | 504990 | 107 | -109.9 | 504990 | 338 | -114.6 | 504990 | 247 |
| MR_1774414623_C695A2B6 | 504990 | 750 | -107.0 | 504990 | 107 | -113.0 | 504990 | 338 | -113.5 | 504990 | 247 |
| MR_1774414623_F4C20D26 | 504990 | 750 | -106.5 | 504990 | 107 | -109.1 | 504990 | 338 | -114.0 | 504990 | 247 |
| MR_1774414623_2A38979A | 504990 | 750 | -105.4 | 504990 | 107 | -111.8 | 504990 | 338 | -114.6 | 504990 | 247 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1754: `ceeda3b5-d62...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ceeda3b5-d625-417e-b299-bcc9b8de4202` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244906_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1754] topology](images/train_1754.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3244906_1
- `C2`: Decrease transmission power for 3244906_1
- `C3`: Check test server and transmission issues
- `C4`: Decrease transmission power for 3275855_5
- `C5`: Add neighbor relationship between 3214803_13 and 3275855_5
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244906_1
- `C7`: Increase transmission power for 3275855_5
- `C8`: Lift the tilt angle of 3244906_1 by 4 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275855_5
- `C10`: Adjust the azimuth of 3244906_1 by 24 degrees
- `C11`: Adjust the azimuth of 3275855_5 by 11 degrees
- `C12`: Add neighbor relationship between 3244906_1 and 3275855_5
- `C13`: Press down the tilt angle  of 3275855_5 by 4 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244906_1 **← 정답**
- `C16`: Increase A3 Offset threshold for 3244906_1
- `C17`: Increase transmission power for 3244906_1
- `C18`: Press down the tilt angle of 3244906_1 by 4 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275855_5
- `C20`: Increase A3 Offset threshold for 3275855_5
- `C21`: Decrease A3 Offset threshold for 3275855_5
- `C22`: Lift the tilt angle  of 3275855_5 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.368 | MS1 | 121.4656741608 | 31.1446222566 | 716 | 504990 | -93.29 | 13.36 | 537.37 | 0.03 | 2.79 | 1580 |
| 2024-09-20 22:21:32.347 | MS1 | 121.4656684842 | 31.1446282063 | 703 | 504990 | -94.34 | 10.41 | 323.83 | 0.18 | 2.33 | 1600 |
| 2024-09-20 22:21:33.910 | MS1 | 121.4656660255 | 31.1446262538 | 76 | 504990 | -95.42 | 11.80 | 418.16 | 0.10 | 2.49 | 1595 |
| 2024-09-20 22:21:34.677 | MS1 | 121.4656660111 | 31.1446226759 | 142 | 152650 | -89.52 | 3.14 | 90.26 | 0.18 | 1.54 | 969 |
| 2024-09-20 22:21:35.568 | MS1 | 121.4656635835 | 31.1446206731 | 13 | 152650 | -90.34 | 4.93 | 58.98 | 0.07 | 1.68 | 945 |
| 2024-09-20 22:21:36.218 | MS1 | 121.4656618661 | 31.1446352594 | 986 | 152650 | -90.71 | 4.21 | 101.49 | 0.15 | 1.81 | 989 |
| 2024-09-20 22:21:37.945 | MS1 | 121.4656662028 | 31.1446237119 | 583 | 152650 | -87.80 | 4.07 | 93.48 | 0.04 | 1.73 | 994 |
| 2024-09-20 22:21:38.356 | MS1 | 121.4656714811 | 31.1446195471 | 142 | 152650 | -90.58 | 7.58 | 66.94 | 0.04 | 1.95 | 907 |
| 2024-09-20 22:21:39.200 | MS1 | 121.4656736042 | 31.1446289913 | 13 | 152650 | -96.02 | 2.01 | 73.53 | 0.07 | 1.83 | 973 |
| 2024-09-20 22:21:40.169 | MS1 | 121.4656706036 | 31.1446274074 | 986 | 152650 | -96.08 | 5.41 | 59.35 | 0.07 | 2.05 | 1564 |
| 2024-09-20 22:21:41.812 | MS1 | 121.4656719721 | 31.1446331308 | 583 | 152650 | -93.68 | 3.31 | 58.83 | 0.14 | 2.39 | 1600 |
| 2024-09-20 22:21:42.392 | MS1 | 121.4656614116 | 31.1446270952 | 142 | 152650 | -96.50 | 6.89 | 87.39 | 0.04 | 2.38 | 1579 |

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
| 3210785 | 8 | 121.4698927532 | 31.1493232020 | 172 | 1 | 0 | 5.7 | FDD | 201 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3213316 | 3 | 121.4750231939 | 31.1551496728 | 325 | 11 | 12 | 21.3 | TDD | 817 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3214803 | 13 | 121.4724572103 | 31.1533635711 | 67 | 12 | 2 | 19.6 | FDD | 986 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3217460 | 10 | 121.4742506253 | 31.1504300575 | 152 | 11 | 8 | 24.9 | FDD | 13 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3217632 | 7 | 121.4739749020 | 31.1468607316 | 110 | 10 | 10 | 21.7 | FDD | 583 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3218753 | 2 | 121.4644335096 | 31.1440392636 | 209 | 14 | 8 | 25.7 | TDD | 76 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3227951 | 11 | 121.4658423970 | 31.1447081172 | 180 | 8 | 5 | 27.6 | FDD | 142 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3237383 | 4 | 121.4682821496 | 31.1551119616 | 19 | 0 | 1 | 0.4 | TDD | 914 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3244906 | 1 | 121.4743026094 | 31.1552112711 | 239 | 3 | 11 | 25.1 | TDD | 716 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3261160 | 6 | 121.4721542361 | 31.1498045332 | 61 | 15 | 5 | 29.2 | TDD | 703 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3273525 | 9 | 121.4646910718 | 31.1525355414 | 321 | 3 | 4 | 12.1 | FDD | 554 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3275855 | 5 | 121.4754854822 | 31.1527848319 | 215 | 3 | 4 | 28.2 | TDD | 541 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3277590 | 12 | 121.4702222839 | 31.1445232143 | 86 | 5 | 9 | 27.7 | FDD | 79 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |

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
| 2024-09-20 22:21:31.483 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.505 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.633 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.633 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.373 | NREventA2 | measId:1;ServCellPCI:559;Se... |
| 2024-09-20 22:21:35.499 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.738 | NREventA5 | measId:3;ServCellPCI:559;Se... |
| 2024-09-20 22:21:35.802 | NRHandoverAttempt | SourcePCI:559;SourceNR-ARFC... |
| 2024-09-20 22:21:35.848 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.861 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.006 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.006 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244906 | 1 | 13.1436 | 16.0797 | -117.6756 | 9.6876 | 140.1406 | 0.0011 | 0.0090 |
| 2024_09_20 22:00 | 3218753 | 2 | 9.9095 | 17.6627 | -117.5156 | 12.2694 | 115.1482 | 0.0114 | 0.0090 |
| 2024_09_20 22:00 | 3213316 | 3 | 17.7960 | 8.8180 | -117.1833 | 17.9206 | 119.2885 | 0.0044 | 0.0058 |
| 2024_09_20 22:00 | 3237383 | 4 | 8.6219 | 8.1408 | -115.8421 | 12.2920 | 150.3597 | 0.0082 | 0.0044 |
| 2024_09_20 22:00 | 3275855 | 5 | 9.6633 | 9.1889 | -114.8282 | 19.2344 | 143.7719 | 0.0010 | 0.0012 |
| 2024_09_20 22:00 | 3261160 | 6 | 14.2477 | 12.0283 | -116.9891 | 6.9760 | 93.3653 | 0.0030 | 0.0034 |
| 2024_09_20 22:00 | 3217632 | 7 | 11.1958 | 14.2175 | -114.6681 | 4.0714 | 24.1552 | 0.0053 | 0.0097 |
| 2024_09_20 22:00 | 3210785 | 8 | 5.7085 | 17.9316 | -114.3483 | 3.3496 | 26.7867 | 0.0004 | 0.0029 |
| 2024_09_20 22:00 | 3273525 | 9 | 8.7926 | 11.4281 | -117.2423 | 3.1236 | 26.5661 | 0.0006 | 0.0097 |
| 2024_09_20 22:00 | 3217460 | 10 | 13.3003 | 19.6676 | -117.0620 | 4.2865 | 53.8440 | 0.0155 | 0.0118 |
| 2024_09_20 22:00 | 3227951 | 11 | 12.2905 | 13.1194 | -115.1164 | 4.5953 | 59.3924 | 0.0011 | 0.0170 |
| 2024_09_20 22:00 | 3277590 | 12 | 15.0160 | 8.6795 | -117.0814 | 3.4658 | 21.1843 | 0.0191 | 0.0094 |
| 2024_09_20 22:00 | 3214803 | 13 | 7.9128 | 15.4270 | -114.2120 | 3.7611 | 34.9766 | 0.0047 | 0.0113 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414807_1C0DEE2C | 504990 | 76 | -93.8 | 504990 | 541 | -90.2 | 504990 | 817 | -104.1 | 504990 | 914 |
| MR_1774414807_A2A3D448 | 152650 | 142 | -91.1 | 152650 | 79 | -95.4 | 152650 | 554 | -102.5 | 152650 | 201 |
| MR_1774414807_69DA8CC9 | 152650 | 142 | -91.5 | 152650 | 79 | -97.8 | 152650 | 554 | -102.0 | 152650 | 201 |
| MR_1774414807_BC88250C | 504990 | 76 | -95.5 | 504990 | 541 | -89.3 | 504990 | 817 | -101.1 | 504990 | 914 |
| MR_1774414807_E669D4E1 | 152650 | 142 | -88.9 | 152650 | 79 | -96.5 | 152650 | 554 | -102.9 | 152650 | 201 |
| MR_1774414807_3AC0F8D0 | 504990 | 76 | -94.9 | 504990 | 541 | -92.5 | 504990 | 817 | -103.1 | 504990 | 914 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1755: `c85b90b8-c26...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c85b90b8-c26d-40f7-96ef-c4af37629467` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease A3 Offset threshold for 3250668_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1755] topology](images/train_1755.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3265287_1
- `C2`: Press down the tilt angle  of 3265287_1 by 7 degrees
- `C3`: Decrease transmission power for 3265287_1
- `C4`: Adjust the azimuth of 3265287_1 by 27 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265287_1
- `C6`: Lift the tilt angle  of 3265287_1 by 7 degrees
- `C7`: Lift the tilt angle of 3250668_3 by 9 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265287_1
- `C9`: Increase transmission power for 3250668_3
- `C10`: Add neighbor relationship between 3275898_2 and 3265287_1
- `C11`: Adjust the azimuth of 3250668_3 by 50 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250668_3
- `C13`: Check test server and transmission issues
- `C14`: Increase transmission power for 3265287_1
- `C15`: Decrease transmission power for 3250668_3
- `C16`: Decrease A3 Offset threshold for 3250668_3 **← 정답**
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250668_3
- `C18`: Press down the tilt angle of 3250668_3 by 9 degrees
- `C19`: Increase A3 Offset threshold for 3250668_3
- `C20`: Increase A3 Offset threshold for 3265287_1
- `C21`: Add neighbor relationship between 3250668_3 and 3265287_1
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.882 | MS1 | 121.4656630784 | 31.1446272565 | 316 | 504990 | -83.99 | 12.65 | 557.81 | 0.03 | 2.35 | 1575 |
| 2024-09-20 22:21:32.478 | MS1 | 121.4656771425 | 31.1446341558 | 316 | 504990 | -78.31 | 12.26 | 360.79 | 0.15 | 2.68 | 1570 |
| 2024-09-20 22:21:33.658 | MS1 | 121.4656752747 | 31.1446202353 | 316 | 504990 | -82.24 | 17.95 | 326.31 | 0.05 | 2.31 | 1567 |
| 2024-09-20 22:21:34.419 | MS1 | 121.4656654222 | 31.1446374125 | 316 | 504990 | -90.27 | -3.18 | 50.82 | 0.08 | 1.41 | 1575 |
| 2024-09-20 22:21:35.368 | MS1 | 121.4656671608 | 31.1446364803 | 316 | 504990 | -84.94 | -2.12 | 24.48 | 0.12 | 1.21 | 1583 |
| 2024-09-20 22:21:36.221 | MS1 | 121.4656630802 | 31.1446215431 | 316 | 504990 | -83.38 | -3.05 | 45.41 | 0.06 | 1.39 | 1560 |
| 2024-09-20 22:21:37.154 | MS1 | 121.4656689000 | 31.1446252563 | 316 | 504990 | -85.13 | -1.57 | 43.47 | 0.17 | 1.31 | 1597 |
| 2024-09-20 22:21:38.538 | MS1 | 121.4656607123 | 31.1446379998 | 316 | 504990 | -92.01 | -2.45 | 58.50 | 0.02 | 1.19 | 1560 |
| 2024-09-20 22:21:39.585 | MS1 | 121.4656727589 | 31.1446378291 | 113 | 504990 | -83.90 | 16.82 | 221.61 | 0.20 | 1.14 | 1583 |
| 2024-09-20 22:21:40.497 | MS1 | 121.4656743691 | 31.1446227986 | 113 | 504990 | -79.28 | 14.87 | 520.57 | 0.11 | 2.18 | 1597 |
| 2024-09-20 22:21:41.272 | MS1 | 121.4656714644 | 31.1446202435 | 113 | 504990 | -84.88 | 12.96 | 573.05 | 0.08 | 2.72 | 1565 |
| 2024-09-20 22:21:42.801 | MS1 | 121.4656630258 | 31.1446360836 | 113 | 504990 | -76.07 | 14.88 | 411.25 | 0.11 | 2.18 | 1599 |

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
| 3238322 | 4 | 121.4672484467 | 31.1452334175 | 119 | 2 | 0 | 41.6 | TDD | 25 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3250668 | 3 | 121.4688414650 | 31.1478583281 | 151 | 4 | 2 | 42.1 | TDD | 316 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3265287 | 1 | 121.4705320408 | 31.1480207486 | 204 | 2 | 3 | 49.3 | TDD | 113 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3275898 | 2 | 121.4654111815 | 31.1524059532 | 238 | 10 | 9 | 16.4 | TDD | 897 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.587 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.605 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.751 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.751 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.411 | NREventA3 | measId:2;ServCellPCI:633;Se... |
| 2024-09-20 22:21:38.651 | NRHandoverAttempt | SourcePCI:633;SourceNR-ARFC... |
| 2024-09-20 22:21:38.688 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.700 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.823 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.823 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265287 | 1 | 8.1179 | 6.5075 | -115.4380 | 13.9757 | 120.3538 | 0.0180 | 0.0125 |
| 2024_09_20 22:00 | 3275898 | 2 | 11.7864 | 12.7854 | -117.6009 | 6.3449 | 141.1471 | 0.0060 | 0.0085 |
| 2024_09_20 22:00 | 3250668 | 3 | 13.1521 | 6.4057 | -115.0276 | 7.5116 | 123.0124 | 0.0149 | 0.1634 |
| 2024_09_20 22:00 | 3238322 | 4 | 8.4527 | 11.9021 | -115.1751 | 14.6577 | 105.9339 | 0.0087 | 0.0183 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412040_D79A3D3B | 504990 | 316 | -89.6 | 504990 | 113 | -83.6 | 504990 | 897 | -89.9 | 504990 | 25 |
| MR_1774412040_B48F2878 | 504990 | 316 | -91.7 | 504990 | 113 | -85.1 | 504990 | 897 | -90.6 | 504990 | 25 |
| MR_1774412040_2CF5A9AA | 504990 | 316 | -91.8 | 504990 | 113 | -83.6 | 504990 | 897 | -90.9 | 504990 | 25 |
| MR_1774412040_9842680A | 504990 | 113 | -83.5 | 504990 | 316 | -91.3 | 504990 | 897 | -89.2 | 504990 | 25 |
| MR_1774412040_51B2B8EF | 504990 | 113 | -85.1 | 504990 | 316 | -89.6 | 504990 | 897 | -89.9 | 504990 | 25 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1756: `90365692-242...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `90365692-2426-47ed-a25f-800f82e5bbe3` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1756] topology](images/train_1756.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255207_3
- `C2`: Press down the tilt angle of 3239872_1 by 5 degrees
- `C3`: Decrease transmission power for 3255207_3
- `C4`: Add neighbor relationship between 3264776_2 and 3255207_3
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Check test server and transmission issues **← 정답**
- `C7`: Lift the tilt angle of 3239872_1 by 5 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255207_3
- `C9`: Increase transmission power for 3255207_3
- `C10`: Decrease transmission power for 3239872_1
- `C11`: Increase A3 Offset threshold for 3239872_1
- `C12`: Adjust the azimuth of 3239872_1 by 50 degrees
- `C13`: Increase transmission power for 3239872_1
- `C14`: Decrease A3 Offset threshold for 3239872_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239872_1
- `C16`: Decrease A3 Offset threshold for 3255207_3
- `C17`: Adjust the azimuth of 3255207_3 by 50 degrees
- `C18`: Press down the tilt angle  of 3255207_3 by 10 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239872_1
- `C20`: Lift the tilt angle  of 3255207_3 by 10 degrees
- `C21`: Add neighbor relationship between 3239872_1 and 3255207_3
- `C22`: Increase A3 Offset threshold for 3255207_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.331 | MS1 | 121.4656714323 | 31.1446197312 | 392 | 504990 | -89.90 | 13.50 | 545.62 | 0.09 | 2.76 | 1581 |
| 2024-09-20 22:21:32.545 | MS1 | 121.4656721526 | 31.1446321070 | 392 | 504990 | -91.51 | 15.91 | 342.77 | 0.15 | 2.10 | 1581 |
| 2024-09-20 22:21:33.253 | MS1 | 121.4656718845 | 31.1446268706 | 392 | 504990 | -87.79 | 16.02 | 444.59 | 0.19 | 2.24 | 1581 |
| 2024-09-20 22:21:34.972 | MS1 | 121.4656691171 | 31.1446317325 | 392 | 504990 | -87.00 | 14.04 | 86.97 | 0.14 | 2.48 | 340 |
| 2024-09-20 22:21:35.909 | MS1 | 121.4656621758 | 31.1446323829 | 392 | 504990 | -91.32 | 15.00 | 54.03 | 0.15 | 2.84 | 327 |
| 2024-09-20 22:21:36.636 | MS1 | 121.4656757210 | 31.1446299574 | 392 | 504990 | -88.29 | 14.47 | 90.88 | 0.03 | 2.46 | 367 |
| 2024-09-20 22:21:37.604 | MS1 | 121.4656681253 | 31.1446211024 | 392 | 504990 | -90.65 | 7.92 | 84.52 | 0.17 | 2.54 | 360 |
| 2024-09-20 22:21:38.879 | MS1 | 121.4656676437 | 31.1446268282 | 392 | 504990 | -89.79 | 8.85 | 56.51 | 0.07 | 2.03 | 491 |
| 2024-09-20 22:21:39.932 | MS1 | 121.4656611608 | 31.1446360430 | 392 | 504990 | -91.88 | 12.03 | 93.29 | 0.06 | 2.04 | 355 |
| 2024-09-20 22:21:40.985 | MS1 | 121.4656627438 | 31.1446207155 | 392 | 504990 | -92.85 | 7.13 | 321.94 | 0.09 | 2.14 | 1597 |
| 2024-09-20 22:21:41.317 | MS1 | 121.4656699368 | 31.1446300780 | 392 | 504990 | -90.32 | 12.41 | 482.20 | 0.03 | 2.42 | 1589 |
| 2024-09-20 22:21:42.969 | MS1 | 121.4656630963 | 31.1446343276 | 392 | 504990 | -89.59 | 8.24 | 555.90 | 0.03 | 2.43 | 1598 |

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
| 3239872 | 1 | 121.4739130581 | 31.1489250754 | 120 | 2 | 12 | 40.3 | TDD | 392 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3241102 | 4 | 121.4653081030 | 31.1550902663 | 210 | 6 | 9 | 29.7 | TDD | 53 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3255207 | 3 | 121.4722635224 | 31.1547381362 | 22 | 9 | 7 | 28.8 | TDD | 21 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3264776 | 2 | 121.4705976644 | 31.1483102939 | 179 | 4 | 9 | 33.0 | TDD | 698 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.881 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.900 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.006 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.006 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.737 | NREventA3 | measId:2;ServCellPCI:624;Se... |
| 2024-09-20 22:21:37.977 | NRHandoverAttempt | SourcePCI:624;SourceNR-ARFC... |
| 2024-09-20 22:21:38.007 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.019 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.168 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.168 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239872 | 1 | 6.8418 | 18.7451 | -115.8637 | 12.2210 | 120.3480 | 0.0058 | 0.0076 |
| 2024_09_20 22:00 | 3264776 | 2 | 19.6074 | 16.3540 | -114.6923 | 8.0681 | 98.5163 | 0.0196 | 0.0078 |
| 2024_09_20 22:00 | 3255207 | 3 | 7.0039 | 8.8684 | -115.9332 | 13.0213 | 194.3189 | 0.0087 | 0.0066 |
| 2024_09_20 22:00 | 3241102 | 4 | 18.3196 | 17.1177 | -114.9939 | 15.5381 | 179.0775 | 0.0184 | 0.0103 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414716_AF69DD6C | 504990 | 392 | -88.6 | 504990 | 21 | -88.3 | 504990 | 698 | -97.4 | 504990 | 53 |
| MR_1774414716_AFCDAE73 | 504990 | 392 | -88.2 | 504990 | 21 | -87.0 | 504990 | 698 | -95.5 | 504990 | 53 |
| MR_1774414716_BC038F13 | 504990 | 392 | -85.4 | 504990 | 21 | -86.8 | 504990 | 698 | -97.4 | 504990 | 53 |
| MR_1774414716_7E761887 | 504990 | 392 | -88.8 | 504990 | 21 | -89.7 | 504990 | 698 | -97.0 | 504990 | 53 |
| MR_1774414716_CCFFCDF4 | 504990 | 392 | -88.9 | 504990 | 21 | -88.3 | 504990 | 698 | -97.9 | 504990 | 53 |
| MR_1774414716_787D871F | 504990 | 392 | -88.1 | 504990 | 21 | -88.4 | 504990 | 698 | -98.0 | 504990 | 53 |
| MR_1774414716_8A52632E | 504990 | 392 | -87.1 | 504990 | 21 | -88.7 | 504990 | 698 | -97.1 | 504990 | 53 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1757: `cb8ce2cc-6a7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cb8ce2cc-6a72-457e-9b83-8bad172a67a3` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221410_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1757] topology](images/train_1757.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3221410_2 and 3256630_4
- `C2`: Add neighbor relationship between 3247632_10 and 3256630_4
- `C3`: Decrease A3 Offset threshold for 3256630_4
- `C4`: Lift the tilt angle  of 3256630_4 by 3 degrees
- `C5`: Increase A3 Offset threshold for 3256630_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256630_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221410_2
- `C8`: Adjust the azimuth of 3221410_2 by 19 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221410_2 **← 정답**
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Adjust the azimuth of 3256630_4 by 29 degrees
- `C12`: Press down the tilt angle of 3221410_2 by 1 degrees
- `C13`: Decrease transmission power for 3221410_2
- `C14`: Increase A3 Offset threshold for 3221410_2
- `C15`: Lift the tilt angle of 3221410_2 by 1 degrees
- `C16`: Increase transmission power for 3221410_2
- `C17`: Increase transmission power for 3256630_4
- `C18`: Decrease A3 Offset threshold for 3221410_2
- `C19`: Check test server and transmission issues
- `C20`: Decrease transmission power for 3256630_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256630_4
- `C22`: Press down the tilt angle  of 3256630_4 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.288 | MS1 | 121.4656761079 | 31.1446244965 | 452 | 504990 | -94.72 | 9.36 | 336.15 | 0.02 | 2.86 | 1566 |
| 2024-09-20 22:21:32.657 | MS1 | 121.4656622599 | 31.1446262286 | 241 | 504990 | -94.85 | 12.48 | 427.38 | 0.13 | 2.38 | 1587 |
| 2024-09-20 22:21:33.513 | MS1 | 121.4656677587 | 31.1446368275 | 96 | 504990 | -93.75 | 12.04 | 477.07 | 0.12 | 2.38 | 1588 |
| 2024-09-20 22:21:34.412 | MS1 | 121.4656593460 | 31.1446335770 | 603 | 152650 | -93.42 | 7.20 | 94.21 | 0.19 | 1.72 | 936 |
| 2024-09-20 22:21:35.873 | MS1 | 121.4656621832 | 31.1446182822 | 133 | 152650 | -95.27 | 2.15 | 65.96 | 0.02 | 1.98 | 918 |
| 2024-09-20 22:21:36.747 | MS1 | 121.4656621180 | 31.1446355556 | 206 | 152650 | -96.73 | 7.85 | 69.74 | 0.01 | 1.83 | 911 |
| 2024-09-20 22:21:37.768 | MS1 | 121.4656737861 | 31.1446223848 | 81 | 152650 | -95.89 | 6.06 | 79.28 | 0.02 | 1.69 | 987 |
| 2024-09-20 22:21:38.547 | MS1 | 121.4656586559 | 31.1446364987 | 603 | 152650 | -87.38 | 6.68 | 79.79 | 0.12 | 1.77 | 976 |
| 2024-09-20 22:21:39.736 | MS1 | 121.4656746573 | 31.1446233411 | 133 | 152650 | -91.88 | 7.28 | 48.74 | 0.11 | 1.74 | 921 |
| 2024-09-20 22:21:40.810 | MS1 | 121.4656623783 | 31.1446252047 | 206 | 152650 | -91.10 | 2.44 | 57.90 | 0.09 | 2.48 | 1566 |
| 2024-09-20 22:21:41.680 | MS1 | 121.4656623354 | 31.1446291315 | 81 | 152650 | -87.59 | 7.02 | 83.84 | 0.08 | 2.51 | 1568 |
| 2024-09-20 22:21:42.814 | MS1 | 121.4656638910 | 31.1446249962 | 603 | 152650 | -87.77 | 4.04 | 93.75 | 0.12 | 2.12 | 1591 |

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
| 3210861 | 13 | 121.4642547970 | 31.1544959432 | 286 | 0 | 9 | 8.8 | FDD | 603 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3215904 | 6 | 121.4757290973 | 31.1511752528 | 4 | 9 | 8 | 24.0 | TDD | 241 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3221410 | 2 | 121.4756425351 | 31.1478496946 | 268 | 1 | 9 | 2.5 | TDD | 452 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3224357 | 1 | 121.4737244916 | 31.1471342765 | 287 | 7 | 7 | 6.9 | TDD | 96 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3224630 | 8 | 121.4694189965 | 31.1442558100 | 120 | 6 | 12 | 9.5 | FDD | 330 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3226012 | 3 | 121.4655366995 | 31.1497403976 | 356 | 2 | 9 | 2.7 | TDD | 647 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3226859 | 7 | 121.4708325063 | 31.1458753531 | 166 | 3 | 2 | 17.9 | FDD | 133 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3247632 | 10 | 121.4732072817 | 31.1521200992 | 265 | 0 | 3 | 28.1 | FDD | 206 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3256330 | 9 | 121.4747656079 | 31.1496319736 | 307 | 1 | 11 | 1.1 | FDD | 300 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3256630 | 4 | 121.4726702404 | 31.1510861944 | 194 | 1 | 4 | 27.1 | TDD | 811 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3263485 | 12 | 121.4726711909 | 31.1478344378 | 170 | 7 | 3 | 17.0 | FDD | 598 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3265053 | 11 | 121.4668114670 | 31.1509380807 | 65 | 14 | 6 | 21.2 | FDD | 81 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3277841 | 5 | 121.4683427701 | 31.1525745781 | 175 | 8 | 0 | 6.8 | TDD | 559 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.029 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.047 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.170 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.170 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.843 | NREventA2 | measId:1;ServCellPCI:294;Se... |
| 2024-09-20 22:21:34.956 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.236 | NREventA5 | measId:3;ServCellPCI:294;Se... |
| 2024-09-20 22:21:35.279 | NRHandoverAttempt | SourcePCI:294;SourceNR-ARFC... |
| 2024-09-20 22:21:35.299 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.312 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.459 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.459 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224357 | 1 | 12.3622 | 18.1160 | -116.1333 | 8.3464 | 140.0819 | 0.0112 | 0.0181 |
| 2024_09_20 22:00 | 3221410 | 2 | 11.3578 | 8.3998 | -116.2626 | 6.1517 | 105.9544 | 0.0108 | 0.0058 |
| 2024_09_20 22:00 | 3226012 | 3 | 19.9740 | 11.7205 | -115.5143 | 6.9590 | 120.2230 | 0.0037 | 0.0030 |
| 2024_09_20 22:00 | 3256630 | 4 | 8.7450 | 8.0368 | -115.1234 | 8.5583 | 130.5531 | 0.0030 | 0.0052 |
| 2024_09_20 22:00 | 3277841 | 5 | 7.1003 | 7.5479 | -114.1805 | 5.3926 | 106.9129 | 0.0020 | 0.0049 |
| 2024_09_20 22:00 | 3215904 | 6 | 7.9016 | 19.0738 | -117.2094 | 5.2392 | 82.1122 | 0.0148 | 0.0148 |
| 2024_09_20 22:00 | 3226859 | 7 | 15.2215 | 7.5837 | -117.3904 | 4.7353 | 55.4009 | 0.0128 | 0.0032 |
| 2024_09_20 22:00 | 3224630 | 8 | 19.3330 | 11.0932 | -115.4095 | 4.1781 | 26.1772 | 0.0028 | 0.0002 |
| 2024_09_20 22:00 | 3256330 | 9 | 17.2962 | 14.0622 | -117.9390 | 4.9088 | 29.7079 | 0.0182 | 0.0071 |
| 2024_09_20 22:00 | 3247632 | 10 | 8.5513 | 10.4503 | -115.8472 | 3.9036 | 49.3165 | 0.0069 | 0.0095 |
| 2024_09_20 22:00 | 3265053 | 11 | 13.6876 | 9.9557 | -115.2231 | 4.4898 | 21.2404 | 0.0097 | 0.0070 |
| 2024_09_20 22:00 | 3263485 | 12 | 16.9532 | 16.4994 | -115.2067 | 4.1217 | 46.3729 | 0.0042 | 0.0109 |
| 2024_09_20 22:00 | 3210861 | 13 | 19.9715 | 18.7336 | -116.5340 | 3.7437 | 27.8216 | 0.0152 | 0.0145 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413822_B3D62847 | 504990 | 96 | -93.7 | 504990 | 811 | -94.6 | 504990 | 559 | -95.0 | 504990 | 647 |
| MR_1774413822_E1D97D72 | 504990 | 96 | -93.0 | 504990 | 811 | -93.8 | 504990 | 559 | -92.0 | 504990 | 647 |
| MR_1774413822_6AFC20D1 | 504990 | 96 | -94.0 | 504990 | 811 | -92.1 | 504990 | 559 | -92.8 | 504990 | 647 |
| MR_1774413822_EC273A3B | 504990 | 96 | -92.3 | 504990 | 811 | -91.0 | 504990 | 559 | -94.0 | 504990 | 647 |
| MR_1774413822_C16A859A | 504990 | 96 | -92.0 | 504990 | 811 | -91.3 | 504990 | 559 | -91.3 | 504990 | 647 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1758: `dbd63231-d60...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dbd63231-d604-4562-9a45-e9f90239b567` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1758] topology](images/train_1758.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3266975_4
- `C2`: Increase A3 Offset threshold for 3266975_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266975_4
- `C4`: Increase transmission power for 3266975_4
- `C5`: Decrease A3 Offset threshold for 3260909_1
- `C6`: Adjust the azimuth of 3266975_4 by 50 degrees
- `C7`: Add neighbor relationship between 3219414_2 and 3266975_4
- `C8`: Increase A3 Offset threshold for 3260909_1
- `C9`: Adjust the azimuth of 3260909_1 by 12 degrees
- `C10`: Lift the tilt angle  of 3266975_4 by 10 degrees
- `C11`: Decrease transmission power for 3260909_1
- `C12`: Add neighbor relationship between 3260909_1 and 3266975_4
- `C13`: Check test server and transmission issues
- `C14`: Lift the tilt angle of 3260909_1 by 2 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260909_1
- `C16`: Increase transmission power for 3260909_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260909_1
- `C18`: Press down the tilt angle  of 3266975_4 by 10 degrees
- `C19`: Decrease A3 Offset threshold for 3266975_4
- `C20`: Insufficient data; more data is needed for judgment. **← 정답**
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266975_4
- `C22`: Press down the tilt angle of 3260909_1 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.207 | MS1 | 121.4656641113 | 31.1446372583 | 232 | 504990 | -89.59 | 16.84 | 474.44 | 0.10 | 2.29 | 1583 |
| 2024-09-20 22:21:32.462 | MS1 | 121.4656709864 | 31.1446337007 | 232 | 504990 | -85.18 | 12.51 | 503.00 | 0.03 | 2.17 | 1563 |
| 2024-09-20 22:21:33.502 | MS1 | 121.4656748117 | 31.1446275117 | 232 | 504990 | -86.63 | 16.30 | 476.19 | 0.12 | 2.29 | 1591 |
| 2024-09-20 22:21:34.895 | MS1 | 121.4656617976 | 31.1446340387 | 232 | 504990 | -89.64 | 14.85 | 80.48 | 0.05 | 2.21 | 1562 |
| 2024-09-20 22:21:35.276 | MS1 | 121.4656760578 | 31.1446258488 | 232 | 504990 | -86.28 | 16.48 | 87.62 | 0.13 | 2.91 | 1571 |
| 2024-09-20 22:21:36.824 | MS1 | 121.4656609023 | 31.1446206819 | 232 | 504990 | -85.20 | 12.64 | 78.56 | 0.04 | 2.87 | 1589 |
| 2024-09-20 22:21:37.717 | MS1 | 121.4656591647 | 31.1446229656 | 232 | 504990 | -89.54 | 12.81 | 84.72 | 0.09 | 2.01 | 1596 |
| 2024-09-20 22:21:38.791 | MS1 | 121.4656676623 | 31.1446212479 | 232 | 504990 | -92.58 | 7.45 | 68.83 | 0.15 | 2.12 | 1580 |
| 2024-09-20 22:21:39.814 | MS1 | 121.4656745831 | 31.1446327747 | 232 | 504990 | -89.62 | 8.61 | 52.44 | 0.13 | 2.68 | 1581 |
| 2024-09-20 22:21:40.524 | MS1 | 121.4656659858 | 31.1446220421 | 232 | 504990 | -90.70 | 7.58 | 364.29 | 0.09 | 2.19 | 1564 |
| 2024-09-20 22:21:41.601 | MS1 | 121.4656676550 | 31.1446228448 | 232 | 504990 | -92.80 | 8.91 | 314.43 | 0.10 | 2.29 | 1571 |
| 2024-09-20 22:21:42.435 | MS1 | 121.4656744619 | 31.1446252558 | 232 | 504990 | -89.55 | 11.03 | 302.47 | 0.15 | 2.35 | 1585 |

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
| 3219414 | 2 | 121.4753173428 | 31.1459279346 | 67 | 12 | 5 | 15.3 | TDD | 312 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3229172 | 3 | 121.4680289782 | 31.1511510214 | 338 | 8 | 9 | 34.3 | TDD | 3 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3260909 | 1 | 121.4708079736 | 31.1512956711 | 201 | 0 | 2 | 33.0 | TDD | 232 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3266975 | 4 | 121.4745730815 | 31.1461631557 | 115 | 9 | 0 | 21.8 | TDD | 878 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.498 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.516 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.621 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.621 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.349 | NREventA3 | measId:2;ServCellPCI:247;Se... |
| 2024-09-20 22:21:38.589 | NRHandoverAttempt | SourcePCI:247;SourceNR-ARFC... |
| 2024-09-20 22:21:38.628 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.643 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.776 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.776 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3260909 | 1 | 78.4772 | 75.5288 | -117.4369 | 6.4128 | 171.4053 | 0.0102 | 0.0047 |
| 2024_09_19 22:00 | 3219414 | 2 | 80.5641 | 91.3808 | -116.5751 | 16.8112 | 193.2575 | 0.0054 | 0.0161 |
| 2024_09_19 22:00 | 3229172 | 3 | 85.1588 | 92.6732 | -114.4993 | 12.9497 | 81.9322 | 0.0071 | 0.0186 |
| 2024_09_19 22:00 | 3266975 | 4 | 93.8083 | 87.7134 | -116.7607 | 13.5476 | 143.9329 | 0.0147 | 0.0073 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416680_D6DBF3B4 | 504990 | 232 | -88.2 | 504990 | 878 | -94.3 | 504990 | 312 | -102.1 | 504990 | 3 |
| MR_1774416680_3A74F2B6 | 504990 | 232 | -88.7 | 504990 | 878 | -92.9 | 504990 | 312 | -100.4 | 504990 | 3 |
| MR_1774416680_07147197 | 504990 | 232 | -90.8 | 504990 | 878 | -93.3 | 504990 | 312 | -102.2 | 504990 | 3 |
| MR_1774416680_A5BA2DC7 | 504990 | 232 | -90.6 | 504990 | 878 | -92.4 | 504990 | 312 | -100.1 | 504990 | 3 |
| MR_1774416680_F1337BDB | 504990 | 232 | -88.4 | 504990 | 878 | -95.4 | 504990 | 312 | -103.4 | 504990 | 3 |
| MR_1774416680_08B096F5 | 504990 | 232 | -91.6 | 504990 | 878 | -94.2 | 504990 | 312 | -100.0 | 504990 | 3 |
| MR_1774416680_78FFDCC4 | 504990 | 232 | -87.7 | 504990 | 878 | -92.1 | 504990 | 312 | -100.2 | 504990 | 3 |
| MR_1774416680_16E63181 | 504990 | 232 | -87.7 | 504990 | 878 | -94.2 | 504990 | 312 | -102.8 | 504990 | 3 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1759: `1dcbb8a8-979...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1dcbb8a8-979c-4c31-a382-7c6ff8ea05e3` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235697_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1759] topology](images/train_1759.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3235267_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235267_4
- `C3`: Decrease A3 Offset threshold for 3235697_5
- `C4`: Increase A3 Offset threshold for 3235267_4
- `C5`: Increase A3 Offset threshold for 3235697_5
- `C6`: Press down the tilt angle of 3235697_5 by 1 degrees
- `C7`: Lift the tilt angle of 3235697_5 by 1 degrees
- `C8`: Increase transmission power for 3235697_5
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235697_5 **← 정답**
- `C10`: Lift the tilt angle  of 3235267_4 by 4 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Press down the tilt angle  of 3235267_4 by 4 degrees
- `C13`: Increase transmission power for 3235267_4
- `C14`: Add neighbor relationship between 3246740_11 and 3235267_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235267_4
- `C16`: Check test server and transmission issues
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235697_5
- `C18`: Add neighbor relationship between 3235697_5 and 3235267_4
- `C19`: Decrease transmission power for 3235697_5
- `C20`: Adjust the azimuth of 3235267_4 by 24 degrees
- `C21`: Decrease transmission power for 3235267_4
- `C22`: Adjust the azimuth of 3235697_5 by 16 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.915 | MS1 | 121.4656729427 | 31.1446375914 | 817 | 504990 | -95.72 | 13.95 | 479.03 | 0.00 | 2.43 | 1563 |
| 2024-09-20 22:21:32.633 | MS1 | 121.4656631157 | 31.1446359580 | 320 | 504990 | -95.49 | 9.06 | 512.93 | 0.04 | 2.03 | 1581 |
| 2024-09-20 22:21:33.660 | MS1 | 121.4656584002 | 31.1446324967 | 167 | 504990 | -95.20 | 11.31 | 446.15 | 0.13 | 2.61 | 1571 |
| 2024-09-20 22:21:34.665 | MS1 | 121.4656650301 | 31.1446223638 | 118 | 152650 | -94.09 | 4.06 | 91.74 | 0.17 | 1.86 | 981 |
| 2024-09-20 22:21:35.335 | MS1 | 121.4656747071 | 31.1446193304 | 686 | 152650 | -87.15 | 7.42 | 60.96 | 0.07 | 1.95 | 966 |
| 2024-09-20 22:21:36.578 | MS1 | 121.4656616136 | 31.1446331132 | 722 | 152650 | -93.50 | 2.08 | 69.63 | 0.08 | 1.72 | 950 |
| 2024-09-20 22:21:37.686 | MS1 | 121.4656611381 | 31.1446197192 | 204 | 152650 | -89.84 | 5.09 | 93.21 | 0.20 | 1.98 | 985 |
| 2024-09-20 22:21:38.833 | MS1 | 121.4656588330 | 31.1446243041 | 118 | 152650 | -91.75 | 7.97 | 63.65 | 0.12 | 1.65 | 929 |
| 2024-09-20 22:21:39.307 | MS1 | 121.4656627605 | 31.1446185937 | 686 | 152650 | -93.19 | 7.33 | 50.81 | 0.19 | 1.60 | 953 |
| 2024-09-20 22:21:40.317 | MS1 | 121.4656599573 | 31.1446248368 | 722 | 152650 | -87.47 | 5.33 | 64.75 | 0.05 | 2.43 | 1572 |
| 2024-09-20 22:21:41.412 | MS1 | 121.4656726581 | 31.1446269881 | 204 | 152650 | -95.02 | 2.74 | 82.05 | 0.16 | 2.56 | 1570 |
| 2024-09-20 22:21:42.621 | MS1 | 121.4656713784 | 31.1446289404 | 118 | 152650 | -91.01 | 3.26 | 74.64 | 0.12 | 2.30 | 1598 |

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
| 3213421 | 3 | 121.4667185287 | 31.1533057678 | 271 | 11 | 4 | 25.1 | TDD | 680 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3214965 | 9 | 121.4695551397 | 31.1493639281 | 198 | 9 | 9 | 6.9 | FDD | 686 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3234350 | 2 | 121.4657822004 | 31.1451735126 | 2 | 8 | 6 | 25.5 | TDD | 167 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3235267 | 4 | 121.4677678152 | 31.1481653572 | 183 | 2 | 9 | 18.0 | TDD | 362 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3235697 | 5 | 121.4680923225 | 31.1502031506 | 184 | 0 | 11 | 11.9 | TDD | 817 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3238607 | 12 | 121.4651946885 | 31.1518461645 | 177 | 6 | 5 | 10.2 | FDD | 118 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3240807 | 7 | 121.4641965101 | 31.1542043267 | 303 | 1 | 4 | 21.4 | FDD | 770 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3246740 | 11 | 121.4647758036 | 31.1559888499 | 3 | 7 | 6 | 13.7 | FDD | 722 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3247516 | 10 | 121.4645276851 | 31.1501890491 | 59 | 0 | 6 | 19.9 | FDD | 494 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3255396 | 6 | 121.4695124319 | 31.1555374313 | 173 | 2 | 1 | 15.5 | TDD | 731 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3266976 | 8 | 121.4643093789 | 31.1526247708 | 8 | 5 | 8 | 19.2 | FDD | 204 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3273532 | 1 | 121.4701895298 | 31.1493584430 | 45 | 0 | 11 | 23.2 | TDD | 320 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3276902 | 13 | 121.4722972548 | 31.1446693348 | 91 | 7 | 12 | 28.1 | FDD | 477 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |

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
| 2024-09-20 22:21:31.287 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.303 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.423 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.423 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.150 | NREventA2 | measId:1;ServCellPCI:528;Se... |
| 2024-09-20 22:21:35.292 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.493 | NREventA5 | measId:3;ServCellPCI:528;Se... |
| 2024-09-20 22:21:35.537 | NRHandoverAttempt | SourcePCI:528;SourceNR-ARFC... |
| 2024-09-20 22:21:35.576 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.589 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.716 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.716 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273532 | 1 | 8.2631 | 11.0915 | -115.4447 | 19.4975 | 185.8973 | 0.0166 | 0.0082 |
| 2024_09_20 22:00 | 3234350 | 2 | 12.0800 | 16.8855 | -116.6106 | 6.0695 | 159.4091 | 0.0091 | 0.0179 |
| 2024_09_20 22:00 | 3213421 | 3 | 8.3707 | 12.9706 | -117.3217 | 13.7719 | 92.5823 | 0.0057 | 0.0052 |
| 2024_09_20 22:00 | 3235267 | 4 | 17.4815 | 18.9370 | -114.1033 | 17.3584 | 180.2581 | 0.0083 | 0.0090 |
| 2024_09_20 22:00 | 3235697 | 5 | 6.4347 | 15.4760 | -114.5828 | 15.3925 | 182.3534 | 0.0020 | 0.0034 |
| 2024_09_20 22:00 | 3255396 | 6 | 10.7020 | 9.5279 | -116.7840 | 17.4253 | 199.4341 | 0.0175 | 0.0072 |
| 2024_09_20 22:00 | 3240807 | 7 | 17.5984 | 13.5706 | -114.4174 | 3.5372 | 39.5041 | 0.0083 | 0.0058 |
| 2024_09_20 22:00 | 3266976 | 8 | 5.6140 | 18.8848 | -117.2535 | 3.5069 | 46.0014 | 0.0069 | 0.0144 |
| 2024_09_20 22:00 | 3214965 | 9 | 7.3206 | 13.8176 | -117.1813 | 4.0695 | 35.0286 | 0.0099 | 0.0104 |
| 2024_09_20 22:00 | 3247516 | 10 | 5.2106 | 8.3519 | -115.9277 | 4.8284 | 31.2429 | 0.0154 | 0.0165 |
| 2024_09_20 22:00 | 3246740 | 11 | 11.7614 | 16.4924 | -117.2046 | 3.7399 | 38.1860 | 0.0198 | 0.0016 |
| 2024_09_20 22:00 | 3238607 | 12 | 14.4780 | 8.2985 | -117.7975 | 4.2380 | 23.7127 | 0.0169 | 0.0047 |
| 2024_09_20 22:00 | 3276902 | 13 | 16.0847 | 19.8486 | -117.1190 | 3.3971 | 41.0338 | 0.0166 | 0.0138 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416563_635A0A4F | 152650 | 118 | -92.5 | 152650 | 494 | -98.0 | 152650 | 477 | -99.5 | 152650 | 770 |
| MR_1774416563_2FB5C07E | 152650 | 118 | -94.4 | 152650 | 494 | -98.0 | 152650 | 477 | -99.9 | 152650 | 770 |
| MR_1774416563_6A0FBFA9 | 504990 | 167 | -94.3 | 504990 | 362 | -95.2 | 504990 | 680 | -95.6 | 504990 | 731 |
| MR_1774416563_EB5D1477 | 504990 | 167 | -96.1 | 504990 | 362 | -93.7 | 504990 | 680 | -96.6 | 504990 | 731 |
| MR_1774416563_2AF7AF9D | 152650 | 118 | -92.3 | 152650 | 494 | -97.7 | 152650 | 477 | -100.5 | 152650 | 770 |

> *... 2개 열 생략 (전체 14열)*

---
