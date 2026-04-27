# Track A 문제 분석 — train[20]~train[29]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[20] ~ train[29] (10개)

## 목차

1. [문제 20: `30724e42-218...`](#20) — single-answer, 정답: C2
2. [문제 21: `dc9300b6-c02...`](#21) — single-answer, 정답: C15
3. [문제 22: `d73c6263-12a...`](#22) — single-answer, 정답: C12
4. [문제 23: `b1ff830f-72e...`](#23) — single-answer, 정답: C18
5. [문제 24: `e15982ba-fbb...`](#24) — single-answer, 정답: C18
6. [문제 25: `1a205126-0de...`](#25) — multiple-answer, 정답: C3|C4
7. [문제 26: `8980bdc4-38c...`](#26) — single-answer, 정답: C16
8. [문제 27: `d1d84ece-b08...`](#27) — single-answer, 정답: C15
9. [문제 28: `7516c555-271...`](#28) — single-answer, 정답: C8
10. [문제 29: `c4e6f7d5-153...`](#29) — single-answer, 정답: C4

---

### 문제 20: `30724e42-218...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `30724e42-2186-44df-9fce-eccec04e0470` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Add neighbor relationship between 3241057_2 and 3266648_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[20] topology](images/train_0020.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Add neighbor relationship between 3241057_2 and 3266648_3 **← 정답**
- `C3`: Add neighbor relationship between 3262691_1 and 3266648_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266648_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241057_2
- `C6`: Lift the tilt angle  of 3266648_3 by 4 degrees
- `C7`: Decrease transmission power for 3241057_2
- `C8`: Press down the tilt angle  of 3266648_3 by 4 degrees
- `C9`: Increase A3 Offset threshold for 3266648_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266648_3
- `C11`: Decrease A3 Offset threshold for 3241057_2
- `C12`: Adjust the azimuth of 3266648_3 by 40 degrees
- `C13`: Increase transmission power for 3241057_2
- `C14`: Press down the tilt angle of 3241057_2 by 10 degrees
- `C15`: Check test server and transmission issues
- `C16`: Decrease transmission power for 3266648_3
- `C17`: Decrease A3 Offset threshold for 3266648_3
- `C18`: Increase transmission power for 3266648_3
- `C19`: Adjust the azimuth of 3241057_2 by 50 degrees
- `C20`: Lift the tilt angle of 3241057_2 by 10 degrees
- `C21`: Increase A3 Offset threshold for 3241057_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241057_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.145 | MS1 | 121.4656583588 | 31.1446327259 | 441 | 504990 | -76.15 | 17.46 | 394.65 | 0.14 | 2.81 | 1588 |
| 2024-09-20 22:21:32.997 | MS1 | 121.4656755882 | 31.1446227431 | 441 | 504990 | -76.41 | 13.56 | 513.61 | 0.13 | 2.25 | 1586 |
| 2024-09-20 22:21:33.757 | MS1 | 121.4656581384 | 31.1446230021 | 441 | 504990 | -75.75 | 17.10 | 542.29 | 0.11 | 2.69 | 1599 |
| 2024-09-20 22:21:34.575 | MS1 | 121.4656652590 | 31.1446348358 | 441 | 504990 | -90.42 | -2.75 | 26.79 | 0.11 | 1.44 | 1569 |
| 2024-09-20 22:21:35.213 | MS1 | 121.4656673521 | 31.1446210180 | 441 | 504990 | -92.83 | -0.52 | 69.28 | 0.02 | 1.47 | 1587 |
| 2024-09-20 22:21:36.466 | MS1 | 121.4656580321 | 31.1446335310 | 441 | 504990 | -90.02 | -2.43 | 29.50 | 0.03 | 1.09 | 1569 |
| 2024-09-20 22:21:37.147 | MS1 | 121.4656604655 | 31.1446192545 | 441 | 504990 | -92.36 | -0.47 | 41.23 | 0.16 | 1.43 | 1573 |
| 2024-09-20 22:21:38.620 | MS1 | 121.4656683275 | 31.1446198225 | 441 | 504990 | -84.10 | 12.66 | 580.14 | 0.16 | 1.29 | 1597 |
| 2024-09-20 22:21:39.359 | MS1 | 121.4656580932 | 31.1446319019 | 441 | 504990 | -76.44 | 12.93 | 354.25 | 0.02 | 1.14 | 1591 |
| 2024-09-20 22:21:40.297 | MS1 | 121.4656689537 | 31.1446249037 | 441 | 504990 | -79.61 | 13.64 | 422.02 | 0.15 | 2.10 | 1584 |
| 2024-09-20 22:21:41.320 | MS1 | 121.4656747746 | 31.1446206442 | 441 | 504990 | -83.97 | 16.94 | 314.86 | 0.10 | 2.88 | 1561 |
| 2024-09-20 22:21:42.420 | MS1 | 121.4656764122 | 31.1446353194 | 441 | 504990 | -80.39 | 16.53 | 502.34 | 0.03 | 2.81 | 1591 |

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
| 3241057 | 2 | 121.4662260688 | 31.1493206202 | 325 | 6 | 11 | 37.6 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3259677 | 4 | 121.4660505067 | 31.1502871373 | 212 | 7 | 3 | 35.7 | TDD | 543 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3262691 | 1 | 121.4701040182 | 31.1480156796 | 229 | 6 | 11 | 38.2 | TDD | 655 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3266648 | 3 | 121.4670579423 | 31.1507912909 | 231 | 3 | 2 | 17.4 | TDD | 221 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.418 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.443 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.587 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.587 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.223 | NREventA3 | measId:2;ServCellPCI:524;Se... |
| 2024-09-20 22:21:36.223 | NREventA3 | measId:2;ServCellPCI:524;Se... |
| 2024-09-20 22:21:37.223 | NREventA3 | measId:2;ServCellPCI:524;Se... |
| 2024-09-20 22:21:39.723 | NRRRCReestablishAttempt | PCI:524 |
| 2024-09-20 22:21:39.736 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.749 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.893 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.893 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262691 | 1 | 7.2971 | 13.1900 | -117.7416 | 8.6800 | 92.8487 | 0.0046 | 0.0176 |
| 2024_09_20 22:00 | 3241057 | 2 | 7.9739 | 5.8535 | -117.8349 | 6.6302 | 198.6515 | 0.0182 | 0.1190 |
| 2024_09_20 22:00 | 3266648 | 3 | 16.4199 | 17.0169 | -116.3946 | 10.9307 | 108.7164 | 0.0016 | 0.0102 |
| 2024_09_20 22:00 | 3259677 | 4 | 10.2724 | 7.7475 | -115.3156 | 10.5340 | 106.9053 | 0.0199 | 0.0118 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413914_0FEEF358 | 504990 | 441 | -89.8 | 504990 | 221 | -83.7 | 504990 | 655 | -93.7 | 504990 | 543 |
| MR_1774413914_E6EE4933 | 504990 | 441 | -90.9 | 504990 | 221 | -86.5 | 504990 | 655 | -93.8 | 504990 | 543 |
| MR_1774413914_D1D5A1EC | 504990 | 441 | -88.5 | 504990 | 221 | -84.8 | 504990 | 655 | -93.0 | 504990 | 543 |
| MR_1774413914_F01E2E08 | 504990 | 441 | -89.1 | 504990 | 221 | -85.3 | 504990 | 655 | -95.5 | 504990 | 543 |
| MR_1774413914_6AA44AE3 | 504990 | 221 | -82.7 | 504990 | 441 | -89.8 | 504990 | 655 | -94.2 | 504990 | 543 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 21: `dc9300b6-c02...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dc9300b6-c02a-4b09-8d7f-778d73051b5e` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3221808_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[21] topology](images/train_0021.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3247802_3
- `C2`: Add neighbor relationship between 3270386_1 and 3247802_3
- `C3`: Check test server and transmission issues
- `C4`: Adjust the azimuth of 3221808_2 by 9 degrees
- `C5`: Press down the tilt angle  of 3247802_3 by 10 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Adjust the azimuth of 3247802_3 by 50 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247802_3
- `C9`: Lift the tilt angle  of 3247802_3 by 10 degrees
- `C10`: Decrease transmission power for 3247802_3
- `C11`: Add neighbor relationship between 3221808_2 and 3247802_3
- `C12`: Increase transmission power for 3247802_3
- `C13`: Increase transmission power for 3221808_2
- `C14`: Press down the tilt angle of 3221808_2 by 1 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221808_2 **← 정답**
- `C16`: Increase A3 Offset threshold for 3221808_2
- `C17`: Decrease A3 Offset threshold for 3221808_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247802_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221808_2
- `C20`: Decrease transmission power for 3221808_2
- `C21`: Increase A3 Offset threshold for 3247802_3
- `C22`: Lift the tilt angle of 3221808_2 by 1 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.901 | MS1 | 121.4656765338 | 31.1446184425 | 148 | 504990 | -88.88 | 15.11 | 378.98 | 0.09 | 2.08 | 1567 |
| 2024-09-20 22:21:32.275 | MS1 | 121.4656737740 | 31.1446225209 | 148 | 504990 | -91.06 | 15.33 | 522.22 | 0.18 | 2.34 | 1574 |
| 2024-09-20 22:21:33.736 | MS1 | 121.4656701029 | 31.1446376501 | 148 | 504990 | -90.78 | 13.79 | 565.74 | 0.10 | 2.06 | 1585 |
| 2024-09-20 22:21:34.837 | MS1 | 121.4656609216 | 31.1446314823 | 148 | 504990 | -89.36 | 17.89 | 74.31 | 0.67 | 2.24 | 555 |
| 2024-09-20 22:21:35.915 | MS1 | 121.4656609542 | 31.1446341526 | 148 | 504990 | -89.05 | 12.47 | 59.01 | 0.70 | 2.33 | 516 |
| 2024-09-20 22:21:36.664 | MS1 | 121.4656685686 | 31.1446180595 | 148 | 504990 | -91.88 | 15.59 | 73.03 | 0.70 | 2.44 | 626 |
| 2024-09-20 22:21:37.585 | MS1 | 121.4656675032 | 31.1446241163 | 148 | 504990 | -93.43 | 10.80 | 69.34 | 0.68 | 2.25 | 613 |
| 2024-09-20 22:21:38.972 | MS1 | 121.4656734506 | 31.1446180324 | 148 | 504990 | -92.07 | 9.07 | 66.06 | 0.55 | 2.01 | 681 |
| 2024-09-20 22:21:39.750 | MS1 | 121.4656703385 | 31.1446243283 | 148 | 504990 | -89.81 | 12.65 | 71.25 | 0.69 | 2.75 | 591 |
| 2024-09-20 22:21:40.338 | MS1 | 121.4656716846 | 31.1446304436 | 148 | 504990 | -93.44 | 12.05 | 602.26 | 0.06 | 2.35 | 1561 |
| 2024-09-20 22:21:41.685 | MS1 | 121.4656707715 | 31.1446198417 | 148 | 504990 | -94.00 | 12.86 | 572.29 | 0.14 | 2.55 | 1581 |
| 2024-09-20 22:21:42.804 | MS1 | 121.4656585529 | 31.1446196854 | 148 | 504990 | -90.91 | 9.74 | 474.11 | 0.11 | 2.21 | 1569 |

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
| 3221808 | 2 | 121.4748310486 | 31.1556969028 | 206 | 0 | 5 | 22.8 | TDD | 148 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3235866 | 4 | 121.4702996751 | 31.1477545900 | 186 | 14 | 11 | 37.1 | TDD | 151 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3247802 | 3 | 121.4682894571 | 31.1507439247 | 93 | 10 | 9 | 17.3 | TDD | 4 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3270386 | 1 | 121.4656105659 | 31.1555096354 | 263 | 2 | 0 | 46.5 | TDD | 480 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.218 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.242 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.364 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.364 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.042 | NREventA3 | measId:2;ServCellPCI:769;Se... |
| 2024-09-20 22:21:38.282 | NRHandoverAttempt | SourcePCI:769;SourceNR-ARFC... |
| 2024-09-20 22:21:38.320 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.331 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.439 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.439 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270386 | 1 | 11.5847 | 11.8605 | -117.0436 | 15.5738 | 140.2592 | 0.0066 | 0.0109 |
| 2024_09_20 22:00 | 3221808 | 2 | 13.0800 | 16.5636 | -116.2849 | 10.1810 | 138.0655 | 0.0039 | 0.0170 |
| 2024_09_20 22:00 | 3247802 | 3 | 16.7003 | 7.6390 | -114.9263 | 10.4061 | 89.1972 | 0.0185 | 0.0008 |
| 2024_09_20 22:00 | 3235866 | 4 | 18.5656 | 8.6695 | -114.6983 | 12.0065 | 92.1337 | 0.0194 | 0.0139 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415884_F344C949 | 504990 | 148 | -89.5 | 504990 | 4 | -97.6 | 504990 | 480 | -100.0 | 504990 | 151 |
| MR_1774415884_8A40C4D2 | 504990 | 148 | -90.3 | 504990 | 4 | -95.7 | 504990 | 480 | -98.3 | 504990 | 151 |
| MR_1774415884_32C2C937 | 504990 | 148 | -90.2 | 504990 | 4 | -95.7 | 504990 | 480 | -101.4 | 504990 | 151 |
| MR_1774415884_AC51DECA | 504990 | 148 | -89.7 | 504990 | 4 | -95.0 | 504990 | 480 | -100.7 | 504990 | 151 |
| MR_1774415884_8CF82FB9 | 504990 | 148 | -88.4 | 504990 | 4 | -97.8 | 504990 | 480 | -100.3 | 504990 | 151 |
| MR_1774415884_A65464C0 | 504990 | 148 | -89.6 | 504990 | 4 | -97.2 | 504990 | 480 | -100.6 | 504990 | 151 |
| MR_1774415884_6B69CB02 | 504990 | 148 | -90.8 | 504990 | 4 | -97.6 | 504990 | 480 | -101.1 | 504990 | 151 |
| MR_1774415884_5B168B04 | 504990 | 148 | -87.6 | 504990 | 4 | -98.7 | 504990 | 480 | -100.4 | 504990 | 151 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 22: `d73c6263-12a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d73c6263-12aa-45df-8410-cb8b6ab4064c` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease A3 Offset threshold for 3248921_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[22] topology](images/train_0022.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3222923_1 by 10 degrees
- `C2`: Adjust the azimuth of 3222923_1 by 50 degrees
- `C3`: Adjust the azimuth of 3248921_3 by 46 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248921_3
- `C5`: Increase A3 Offset threshold for 3248921_3
- `C6`: Lift the tilt angle of 3248921_3 by 10 degrees
- `C7`: Check test server and transmission issues
- `C8`: Increase transmission power for 3222923_1
- `C9`: Add neighbor relationship between 3253027_2 and 3222923_1
- `C10`: Increase A3 Offset threshold for 3222923_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222923_1
- `C12`: Decrease A3 Offset threshold for 3248921_3 **← 정답**
- `C13`: Decrease transmission power for 3222923_1
- `C14`: Decrease transmission power for 3248921_3
- `C15`: Increase transmission power for 3248921_3
- `C16`: Press down the tilt angle  of 3222923_1 by 10 degrees
- `C17`: Press down the tilt angle of 3248921_3 by 10 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248921_3
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222923_1
- `C21`: Add neighbor relationship between 3248921_3 and 3222923_1
- `C22`: Decrease A3 Offset threshold for 3222923_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.509 | MS1 | 121.4656761097 | 31.1446281666 | 300 | 504990 | -76.80 | 17.77 | 476.91 | 0.14 | 2.37 | 1598 |
| 2024-09-20 22:21:32.431 | MS1 | 121.4656588432 | 31.1446315340 | 300 | 504990 | -76.14 | 15.59 | 339.72 | 0.00 | 2.40 | 1585 |
| 2024-09-20 22:21:33.175 | MS1 | 121.4656618577 | 31.1446349514 | 300 | 504990 | -76.20 | 16.51 | 410.24 | 0.19 | 2.82 | 1593 |
| 2024-09-20 22:21:34.815 | MS1 | 121.4656739047 | 31.1446333681 | 300 | 504990 | -91.96 | -0.85 | 44.29 | 0.00 | 1.01 | 1586 |
| 2024-09-20 22:21:35.972 | MS1 | 121.4656656173 | 31.1446210396 | 300 | 504990 | -83.08 | -0.46 | 58.54 | 0.14 | 1.15 | 1579 |
| 2024-09-20 22:21:36.685 | MS1 | 121.4656751701 | 31.1446339391 | 300 | 504990 | -85.09 | -2.08 | 58.57 | 0.14 | 1.28 | 1599 |
| 2024-09-20 22:21:37.708 | MS1 | 121.4656731234 | 31.1446353369 | 300 | 504990 | -90.63 | -3.62 | 30.56 | 0.09 | 1.07 | 1585 |
| 2024-09-20 22:21:38.716 | MS1 | 121.4656682851 | 31.1446338955 | 300 | 504990 | -84.08 | -3.51 | 61.58 | 0.09 | 1.16 | 1600 |
| 2024-09-20 22:21:39.176 | MS1 | 121.4656623600 | 31.1446306193 | 225 | 504990 | -84.36 | 15.64 | 289.12 | 0.16 | 1.27 | 1568 |
| 2024-09-20 22:21:40.960 | MS1 | 121.4656753073 | 31.1446264812 | 225 | 504990 | -80.55 | 16.54 | 307.00 | 0.15 | 2.91 | 1571 |
| 2024-09-20 22:21:41.760 | MS1 | 121.4656596264 | 31.1446248263 | 225 | 504990 | -75.41 | 14.17 | 353.09 | 0.11 | 2.26 | 1599 |
| 2024-09-20 22:21:42.241 | MS1 | 121.4656647032 | 31.1446213780 | 225 | 504990 | -77.48 | 13.39 | 451.53 | 0.19 | 2.87 | 1599 |

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
| 3222923 | 1 | 121.4739724477 | 31.1445787336 | 121 | 11 | 2 | 27.5 | TDD | 225 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3248921 | 3 | 121.4711494192 | 31.1458853077 | 301 | 7 | 1 | 25.4 | TDD | 300 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3253027 | 2 | 121.4718979552 | 31.1448680496 | 75 | 15 | 5 | 30.4 | TDD | 11 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3275004 | 4 | 121.4652057423 | 31.1494398025 | 257 | 4 | 9 | 22.1 | TDD | 812 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.122 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.138 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.281 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.281 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.960 | NREventA3 | measId:2;ServCellPCI:22;Ser... |
| 2024-09-20 22:21:38.200 | NRHandoverAttempt | SourcePCI:22;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.240 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.254 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.399 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.399 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222923 | 1 | 9.1459 | 6.1639 | -117.2244 | 15.6596 | 193.9431 | 0.0033 | 0.0186 |
| 2024_09_20 22:00 | 3253027 | 2 | 8.2448 | 8.4842 | -117.8498 | 18.1061 | 119.5027 | 0.0158 | 0.0102 |
| 2024_09_20 22:00 | 3248921 | 3 | 19.9897 | 11.4610 | -117.8498 | 13.1508 | 189.6068 | 0.0182 | 0.1758 |
| 2024_09_20 22:00 | 3275004 | 4 | 18.8569 | 14.8924 | -114.5937 | 9.4876 | 82.5283 | 0.0130 | 0.0193 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413740_54E9D08A | 504990 | 300 | -91.1 | 504990 | 225 | -86.4 | 504990 | 11 | -89.3 | 504990 | 812 |
| MR_1774413740_302FF488 | 504990 | 300 | -92.1 | 504990 | 225 | -87.0 | 504990 | 11 | -88.6 | 504990 | 812 |
| MR_1774413740_1BF05C0A | 504990 | 300 | -91.7 | 504990 | 225 | -87.6 | 504990 | 11 | -87.9 | 504990 | 812 |
| MR_1774413740_57E065EB | 504990 | 225 | -87.9 | 504990 | 300 | -90.1 | 504990 | 11 | -90.9 | 504990 | 812 |
| MR_1774413740_4F44469B | 504990 | 300 | -91.5 | 504990 | 225 | -85.2 | 504990 | 11 | -87.8 | 504990 | 812 |
| MR_1774413740_1AFAB576 | 504990 | 300 | -93.1 | 504990 | 225 | -85.2 | 504990 | 11 | -88.2 | 504990 | 812 |
| MR_1774413740_56586A1B | 504990 | 225 | -86.0 | 504990 | 300 | -93.1 | 504990 | 11 | -91.5 | 504990 | 812 |
| MR_1774413740_DEB2FBC9 | 504990 | 225 | -88.8 | 504990 | 300 | -90.7 | 504990 | 11 | -91.2 | 504990 | 812 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 23: `b1ff830f-72e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b1ff830f-72e1-4fca-9afb-702c68e231a7` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[23] topology](images/train_0023.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3216342_1
- `C2`: Increase A3 Offset threshold for 3256343_2
- `C3`: Press down the tilt angle  of 3256343_2 by 10 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease A3 Offset threshold for 3216342_1
- `C6`: Lift the tilt angle  of 3256343_2 by 10 degrees
- `C7`: Press down the tilt angle of 3216342_1 by 3 degrees
- `C8`: Decrease transmission power for 3216342_1
- `C9`: Increase transmission power for 3216342_1
- `C10`: Add neighbor relationship between 3216342_1 and 3256343_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256343_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216342_1
- `C13`: Lift the tilt angle of 3216342_1 by 3 degrees
- `C14`: Add neighbor relationship between 3257345_4 and 3256343_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216342_1
- `C16`: Increase transmission power for 3256343_2
- `C17`: Decrease transmission power for 3256343_2
- `C18`: Check test server and transmission issues **← 정답**
- `C19`: Adjust the azimuth of 3256343_2 by 50 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256343_2
- `C21`: Adjust the azimuth of 3216342_1 by 50 degrees
- `C22`: Decrease A3 Offset threshold for 3256343_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.672 | MS1 | 121.4656695088 | 31.1446324754 | 129 | 504990 | -85.66 | 14.70 | 543.93 | 0.12 | 2.56 | 1587 |
| 2024-09-20 22:21:32.893 | MS1 | 121.4656729475 | 31.1446379712 | 129 | 504990 | -85.49 | 13.58 | 358.81 | 0.15 | 2.11 | 1586 |
| 2024-09-20 22:21:33.553 | MS1 | 121.4656741724 | 31.1446229920 | 129 | 504990 | -87.28 | 14.26 | 523.02 | 0.12 | 2.23 | 1582 |
| 2024-09-20 22:21:34.508 | MS1 | 121.4656667744 | 31.1446351236 | 129 | 504990 | -90.17 | 13.83 | 72.64 | 0.08 | 2.49 | 300 |
| 2024-09-20 22:21:35.972 | MS1 | 121.4656691920 | 31.1446315558 | 129 | 504990 | -91.61 | 12.33 | 73.99 | 0.09 | 2.51 | 323 |
| 2024-09-20 22:21:36.741 | MS1 | 121.4656708251 | 31.1446235507 | 129 | 504990 | -89.21 | 17.68 | 79.14 | 0.11 | 2.17 | 461 |
| 2024-09-20 22:21:37.159 | MS1 | 121.4656776465 | 31.1446268914 | 129 | 504990 | -91.96 | 8.68 | 102.13 | 0.09 | 2.73 | 457 |
| 2024-09-20 22:21:38.928 | MS1 | 121.4656684079 | 31.1446372452 | 129 | 504990 | -91.75 | 10.20 | 100.41 | 0.14 | 2.79 | 381 |
| 2024-09-20 22:21:39.710 | MS1 | 121.4656659932 | 31.1446352295 | 129 | 504990 | -93.81 | 9.69 | 62.60 | 0.06 | 2.59 | 410 |
| 2024-09-20 22:21:40.785 | MS1 | 121.4656712368 | 31.1446285121 | 129 | 504990 | -91.55 | 11.63 | 297.08 | 0.14 | 2.79 | 1596 |
| 2024-09-20 22:21:41.824 | MS1 | 121.4656686905 | 31.1446351297 | 129 | 504990 | -89.17 | 7.60 | 597.27 | 0.04 | 2.43 | 1583 |
| 2024-09-20 22:21:42.140 | MS1 | 121.4656587449 | 31.1446377883 | 129 | 504990 | -93.53 | 9.17 | 404.39 | 0.16 | 2.72 | 1577 |

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
| 3216342 | 1 | 121.4742762137 | 31.1470997314 | 117 | 0 | 3 | 40.1 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3234550 | 3 | 121.4651036672 | 31.1487253352 | 57 | 1 | 3 | 35.3 | TDD | 886 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3256343 | 2 | 121.4709827760 | 31.1475610500 | 115 | 13 | 11 | 26.4 | TDD | 547 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3257345 | 4 | 121.4695989876 | 31.1532039674 | 314 | 15 | 2 | 28.8 | TDD | 70 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.305 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.321 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.442 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.442 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.118 | NREventA3 | measId:2;ServCellPCI:304;Se... |
| 2024-09-20 22:21:38.358 | NRHandoverAttempt | SourcePCI:304;SourceNR-ARFC... |
| 2024-09-20 22:21:38.390 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.400 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.539 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.539 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216342 | 1 | 9.7519 | 6.7732 | -116.8288 | 16.2623 | 187.9065 | 0.0051 | 0.0114 |
| 2024_09_20 22:00 | 3256343 | 2 | 7.1612 | 17.3031 | -115.3509 | 12.9039 | 109.9502 | 0.0174 | 0.0033 |
| 2024_09_20 22:00 | 3234550 | 3 | 14.7003 | 12.3978 | -117.2243 | 12.2452 | 89.1498 | 0.0027 | 0.0032 |
| 2024_09_20 22:00 | 3257345 | 4 | 14.5550 | 5.7798 | -114.2748 | 17.9001 | 179.1998 | 0.0181 | 0.0084 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414436_279D497A | 504990 | 129 | -88.6 | 504990 | 547 | -97.1 | 504990 | 70 | -103.5 | 504990 | 886 |
| MR_1774414436_7703ADA5 | 504990 | 129 | -91.2 | 504990 | 547 | -99.0 | 504990 | 70 | -103.4 | 504990 | 886 |
| MR_1774414436_DFBD6003 | 504990 | 129 | -91.9 | 504990 | 547 | -97.3 | 504990 | 70 | -101.0 | 504990 | 886 |
| MR_1774414436_B431F707 | 504990 | 129 | -88.7 | 504990 | 547 | -99.3 | 504990 | 70 | -100.5 | 504990 | 886 |
| MR_1774414436_B43E2F22 | 504990 | 129 | -89.8 | 504990 | 547 | -97.5 | 504990 | 70 | -103.2 | 504990 | 886 |
| MR_1774414436_231FE23C | 504990 | 129 | -89.3 | 504990 | 547 | -97.7 | 504990 | 70 | -102.8 | 504990 | 886 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 24: `e15982ba-fbb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e15982ba-fbb6-45bc-8524-4b8b0ae5e34c` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3269819_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[24] topology](images/train_0024.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3268172_3 by 50 degrees
- `C2`: Decrease A3 Offset threshold for 3269819_1
- `C3`: Increase A3 Offset threshold for 3269819_1
- `C4`: Lift the tilt angle of 3269819_1 by 5 degrees
- `C5`: Decrease A3 Offset threshold for 3268172_3
- `C6`: Check test server and transmission issues
- `C7`: Increase transmission power for 3269819_1
- `C8`: Decrease transmission power for 3269819_1
- `C9`: Press down the tilt angle of 3269819_1 by 5 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268172_3
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease transmission power for 3268172_3
- `C13`: Add neighbor relationship between 3274634_4 and 3268172_3
- `C14`: Increase transmission power for 3268172_3
- `C15`: Lift the tilt angle  of 3268172_3 by 4 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269819_1
- `C17`: Press down the tilt angle  of 3268172_3 by 4 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269819_1 **← 정답**
- `C19`: Adjust the azimuth of 3269819_1 by 4 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268172_3
- `C21`: Increase A3 Offset threshold for 3268172_3
- `C22`: Add neighbor relationship between 3269819_1 and 3268172_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.806 | MS1 | 121.4656679230 | 31.1446322382 | 977 | 504990 | -87.30 | 16.18 | 580.10 | 0.01 | 2.35 | 1572 |
| 2024-09-20 22:21:32.306 | MS1 | 121.4656740454 | 31.1446184300 | 977 | 504990 | -91.47 | 16.20 | 336.18 | 0.13 | 2.74 | 1570 |
| 2024-09-20 22:21:33.472 | MS1 | 121.4656680175 | 31.1446314059 | 977 | 504990 | -90.16 | 14.20 | 597.81 | 0.04 | 2.52 | 1568 |
| 2024-09-20 22:21:34.600 | MS1 | 121.4656608675 | 31.1446213485 | 977 | 504990 | -90.92 | 14.10 | 80.68 | 0.68 | 2.18 | 570 |
| 2024-09-20 22:21:35.314 | MS1 | 121.4656690143 | 31.1446205067 | 977 | 504990 | -91.19 | 15.35 | 86.51 | 0.68 | 2.50 | 618 |
| 2024-09-20 22:21:36.415 | MS1 | 121.4656773958 | 31.1446307922 | 977 | 504990 | -88.76 | 14.31 | 88.10 | 0.55 | 2.17 | 520 |
| 2024-09-20 22:21:37.664 | MS1 | 121.4656700609 | 31.1446210147 | 977 | 504990 | -90.53 | 12.98 | 104.80 | 0.66 | 2.06 | 691 |
| 2024-09-20 22:21:38.267 | MS1 | 121.4656612716 | 31.1446248010 | 977 | 504990 | -92.88 | 7.42 | 96.19 | 0.57 | 2.69 | 697 |
| 2024-09-20 22:21:39.235 | MS1 | 121.4656601219 | 31.1446266899 | 977 | 504990 | -90.83 | 11.20 | 51.43 | 0.68 | 2.76 | 544 |
| 2024-09-20 22:21:40.642 | MS1 | 121.4656761662 | 31.1446368303 | 977 | 504990 | -91.26 | 12.48 | 596.13 | 0.01 | 2.59 | 1578 |
| 2024-09-20 22:21:41.208 | MS1 | 121.4656762364 | 31.1446184152 | 977 | 504990 | -89.74 | 12.93 | 583.29 | 0.16 | 2.51 | 1599 |
| 2024-09-20 22:21:42.711 | MS1 | 121.4656712880 | 31.1446247943 | 977 | 504990 | -91.76 | 10.38 | 579.08 | 0.03 | 2.55 | 1566 |

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
| 3268172 | 3 | 121.4742188581 | 31.1486392259 | 62 | 3 | 1 | 23.9 | TDD | 428 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3269819 | 1 | 121.4753880903 | 31.1526331574 | 222 | 4 | 11 | 27.3 | TDD | 977 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3274634 | 4 | 121.4643249267 | 31.1489440933 | 35 | 12 | 10 | 15.2 | TDD | 551 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3277985 | 2 | 121.4643344731 | 31.1482993308 | 358 | 15 | 7 | 24.0 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.628 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.649 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.780 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.780 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.444 | NREventA3 | measId:2;ServCellPCI:181;Se... |
| 2024-09-20 22:21:38.684 | NRHandoverAttempt | SourcePCI:181;SourceNR-ARFC... |
| 2024-09-20 22:21:38.727 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.739 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.848 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.848 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269819 | 1 | 17.1834 | 6.8271 | -115.6071 | 19.2551 | 107.8226 | 0.0115 | 0.0129 |
| 2024_09_20 22:00 | 3277985 | 2 | 13.0856 | 11.8799 | -115.3579 | 16.8182 | 189.4762 | 0.0182 | 0.0170 |
| 2024_09_20 22:00 | 3268172 | 3 | 5.1126 | 15.5716 | -116.4632 | 8.2065 | 166.0457 | 0.0064 | 0.0190 |
| 2024_09_20 22:00 | 3274634 | 4 | 19.1583 | 12.9323 | -117.7103 | 5.3511 | 136.4912 | 0.0071 | 0.0115 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412658_D258516C | 504990 | 977 | -92.6 | 504990 | 428 | -90.8 | 504990 | 551 | -100.0 | 504990 | 355 |
| MR_1774412658_F9F2CC05 | 504990 | 977 | -89.1 | 504990 | 428 | -91.4 | 504990 | 551 | -100.6 | 504990 | 355 |
| MR_1774412658_077D7929 | 504990 | 977 | -92.9 | 504990 | 428 | -90.5 | 504990 | 551 | -98.3 | 504990 | 355 |
| MR_1774412658_8A46BF51 | 504990 | 977 | -91.9 | 504990 | 428 | -91.6 | 504990 | 551 | -101.3 | 504990 | 355 |
| MR_1774412658_C4686C02 | 504990 | 977 | -89.3 | 504990 | 428 | -93.0 | 504990 | 551 | -98.9 | 504990 | 355 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 25: `1a205126-0de...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1a205126-0dec-4ba7-abeb-53b88a9f2f88` |
| Tag | **multiple-answer** |
| 정답 | **C3|C4** |
| C3 의미 | Decrease transmission power for 3232166_1 |
| C4 의미 | Press down the tilt angle  of 3232166_1 by 2 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[25] topology](images/train_0025.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232166_1
- `C2`: Press down the tilt angle of 3278379_4 by 3 degrees
- `C3`: Decrease transmission power for 3232166_1 **← 정답**
- `C4`: Press down the tilt angle  of 3232166_1 by 2 degrees **← 정답**
- `C5`: Increase transmission power for 3232166_1
- `C6`: Add neighbor relationship between 3211374_2 and 3232166_1
- `C7`: Increase A3 Offset threshold for 3232166_1
- `C8`: Add neighbor relationship between 3278379_4 and 3232166_1
- `C9`: Increase transmission power for 3278379_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278379_4
- `C11`: Lift the tilt angle of 3278379_4 by 3 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232166_1
- `C13`: Decrease transmission power for 3278379_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278379_4
- `C15`: Adjust the azimuth of 3232166_1 by 13 degrees
- `C16`: Increase A3 Offset threshold for 3278379_4
- `C17`: Decrease A3 Offset threshold for 3278379_4
- `C18`: Lift the tilt angle  of 3232166_1 by 2 degrees
- `C19`: Decrease A3 Offset threshold for 3232166_1
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Adjust the azimuth of 3278379_4 by 17 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.829 | MS1 | 121.4656684174 | 31.1446225034 | 422 | 504990 | -80.31 | 12.53 | 431.49 | 0.07 | 2.19 | 1599 |
| 2024-09-20 22:21:32.800 | MS1 | 121.4656698122 | 31.1446248220 | 422 | 504990 | -78.48 | 14.49 | 315.67 | 0.09 | 2.56 | 1583 |
| 2024-09-20 22:21:33.267 | MS1 | 121.4656589209 | 31.1446320230 | 422 | 504990 | -75.57 | 13.94 | 334.58 | 0.04 | 2.58 | 1565 |
| 2024-09-20 22:21:34.450 | MS1 | 121.4656716905 | 31.1446211925 | 422 | 504990 | -93.81 | 1.25 | 55.49 | 0.18 | 1.00 | 1572 |
| 2024-09-20 22:21:35.243 | MS1 | 121.4656589916 | 31.1446345341 | 422 | 504990 | -92.28 | 1.09 | 34.99 | 0.16 | 1.32 | 1581 |
| 2024-09-20 22:21:36.995 | MS1 | 121.4656648819 | 31.1446268817 | 422 | 504990 | -90.41 | 2.93 | 64.05 | 0.08 | 1.38 | 1574 |
| 2024-09-20 22:21:37.839 | MS1 | 121.4656675990 | 31.1446263664 | 422 | 504990 | -85.23 | 2.86 | 60.69 | 0.16 | 1.32 | 1575 |
| 2024-09-20 22:21:38.772 | MS1 | 121.4656776309 | 31.1446357119 | 422 | 504990 | -92.21 | 2.75 | 84.06 | 0.18 | 1.03 | 1594 |
| 2024-09-20 22:21:39.429 | MS1 | 121.4656725041 | 31.1446307021 | 422 | 504990 | -87.40 | 2.28 | 53.93 | 0.17 | 1.23 | 1563 |
| 2024-09-20 22:21:40.545 | MS1 | 121.4656681187 | 31.1446248322 | 422 | 504990 | -84.74 | 13.62 | 354.69 | 0.14 | 2.34 | 1582 |
| 2024-09-20 22:21:41.965 | MS1 | 121.4656747465 | 31.1446355574 | 422 | 504990 | -81.27 | 14.95 | 429.07 | 0.06 | 2.76 | 1590 |
| 2024-09-20 22:21:42.125 | MS1 | 121.4656727442 | 31.1446211533 | 422 | 504990 | -78.64 | 12.37 | 406.94 | 0.17 | 2.06 | 1564 |

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
| 3211374 | 2 | 121.4742043854 | 31.1524328528 | 327 | 1 | 7 | 29.0 | TDD | 338 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3232166 | 1 | 121.4703491967 | 31.1531163658 | 192 | 1 | 6 | 18.1 | TDD | 185 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3237104 | 3 | 121.4706227072 | 31.1537481341 | 153 | 3 | 9 | 35.9 | TDD | 267 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3278379 | 4 | 121.4690232965 | 31.1529299308 | 216 | 1 | 2 | 35.4 | TDD | 422 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.628 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.645 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.763 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.763 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232166 | 1 | 19.3667 | 17.6201 | -115.7743 | 14.6879 | 193.6819 | 0.0194 | 0.0050 |
| 2024_09_20 22:00 | 3211374 | 2 | 6.7045 | 12.0162 | -117.0614 | 19.9814 | 125.2018 | 0.0043 | 0.0080 |
| 2024_09_20 22:00 | 3237104 | 3 | 7.0860 | 9.4529 | -114.9829 | 12.5342 | 124.9910 | 0.0084 | 0.0195 |
| 2024_09_20 22:00 | 3278379 | 4 | 10.1886 | 5.5262 | -108.3757 | 15.7949 | 182.8701 | 0.0139 | 0.0146 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415450_9FAE2A37 | 504990 | 422 | -92.1 | 504990 | 185 | -89.6 | 504990 | 338 | -91.6 | 504990 | 267 |
| MR_1774415450_20601A45 | 504990 | 422 | -94.6 | 504990 | 185 | -88.4 | 504990 | 338 | -92.4 | 504990 | 267 |
| MR_1774415450_F5E6713C | 504990 | 422 | -95.7 | 504990 | 185 | -89.6 | 504990 | 338 | -92.9 | 504990 | 267 |
| MR_1774415450_F1DF0F18 | 504990 | 185 | -95.1 | 504990 | 422 | -92.2 | 504990 | 338 | -89.8 | 504990 | 267 |
| MR_1774415450_D747F436 | 504990 | 185 | -94.8 | 504990 | 422 | -89.3 | 504990 | 338 | -90.2 | 504990 | 267 |
| MR_1774415450_A4543E62 | 504990 | 422 | -95.3 | 504990 | 185 | -88.6 | 504990 | 338 | -89.8 | 504990 | 267 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 26: `8980bdc4-38c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8980bdc4-38ce-48a1-863f-65659daa3834` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease A3 Offset threshold for 3240163_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[26] topology](images/train_0026.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3240163_2 by 6 degrees
- `C2`: Adjust the azimuth of 3235071_1 by 50 degrees
- `C3`: Press down the tilt angle  of 3235071_1 by 10 degrees
- `C4`: Decrease transmission power for 3240163_2
- `C5`: Decrease A3 Offset threshold for 3235071_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240163_2
- `C7`: Adjust the azimuth of 3240163_2 by 50 degrees
- `C8`: Add neighbor relationship between 3215128_4 and 3235071_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240163_2
- `C11`: Increase A3 Offset threshold for 3240163_2
- `C12`: Check test server and transmission issues
- `C13`: Add neighbor relationship between 3240163_2 and 3235071_1
- `C14`: Decrease transmission power for 3235071_1
- `C15`: Increase transmission power for 3235071_1
- `C16`: Decrease A3 Offset threshold for 3240163_2 **← 정답**
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235071_1
- `C18`: Increase transmission power for 3240163_2
- `C19`: Increase A3 Offset threshold for 3235071_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235071_1
- `C21`: Lift the tilt angle of 3240163_2 by 6 degrees
- `C22`: Lift the tilt angle  of 3235071_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.900 | MS1 | 121.4656632502 | 31.1446314648 | 83 | 504990 | -81.51 | 14.45 | 321.41 | 0.17 | 2.88 | 1590 |
| 2024-09-20 22:21:32.115 | MS1 | 121.4656641895 | 31.1446257502 | 83 | 504990 | -78.71 | 12.62 | 300.44 | 0.07 | 2.36 | 1593 |
| 2024-09-20 22:21:33.828 | MS1 | 121.4656738091 | 31.1446325055 | 83 | 504990 | -77.09 | 17.10 | 593.27 | 0.16 | 2.22 | 1595 |
| 2024-09-20 22:21:34.684 | MS1 | 121.4656660709 | 31.1446377394 | 83 | 504990 | -91.20 | -2.88 | 54.64 | 0.19 | 1.36 | 1573 |
| 2024-09-20 22:21:35.377 | MS1 | 121.4656591790 | 31.1446237813 | 83 | 504990 | -85.04 | -2.98 | 41.20 | 0.17 | 1.23 | 1586 |
| 2024-09-20 22:21:36.480 | MS1 | 121.4656734706 | 31.1446277725 | 83 | 504990 | -88.00 | -2.97 | 40.38 | 0.10 | 1.25 | 1590 |
| 2024-09-20 22:21:37.982 | MS1 | 121.4656772125 | 31.1446222060 | 83 | 504990 | -92.61 | -3.96 | 70.02 | 0.20 | 1.20 | 1578 |
| 2024-09-20 22:21:38.487 | MS1 | 121.4656730913 | 31.1446259131 | 83 | 504990 | -87.32 | -0.02 | 51.34 | 0.04 | 1.25 | 1571 |
| 2024-09-20 22:21:39.322 | MS1 | 121.4656779075 | 31.1446342981 | 304 | 504990 | -75.22 | 15.96 | 214.14 | 0.10 | 1.48 | 1567 |
| 2024-09-20 22:21:40.973 | MS1 | 121.4656680120 | 31.1446298532 | 304 | 504990 | -79.62 | 16.84 | 317.51 | 0.15 | 2.23 | 1565 |
| 2024-09-20 22:21:41.449 | MS1 | 121.4656724305 | 31.1446338889 | 304 | 504990 | -77.99 | 13.38 | 488.13 | 0.18 | 2.75 | 1586 |
| 2024-09-20 22:21:42.136 | MS1 | 121.4656762492 | 31.1446317797 | 304 | 504990 | -81.31 | 13.10 | 498.29 | 0.15 | 2.91 | 1565 |

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
| 3215128 | 4 | 121.4754072881 | 31.1488946009 | 209 | 14 | 11 | 49.3 | TDD | 971 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3235071 | 1 | 121.4673831754 | 31.1551167095 | 290 | 10 | 9 | 37.5 | TDD | 304 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3235835 | 3 | 121.4756096754 | 31.1473428064 | 284 | 6 | 10 | 22.5 | TDD | 675 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3240163 | 2 | 121.4711190042 | 31.1440377247 | 219 | 3 | 8 | 30.9 | TDD | 83 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.254 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.272 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.386 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.386 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.079 | NREventA3 | measId:2;ServCellPCI:571;Se... |
| 2024-09-20 22:21:38.319 | NRHandoverAttempt | SourcePCI:571;SourceNR-ARFC... |
| 2024-09-20 22:21:38.365 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.376 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.517 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.517 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235071 | 1 | 8.6307 | 15.9925 | -117.8313 | 8.3624 | 125.6349 | 0.0171 | 0.0179 |
| 2024_09_20 22:00 | 3240163 | 2 | 7.1078 | 14.4519 | -116.6353 | 19.3623 | 94.6639 | 0.0009 | 0.1745 |
| 2024_09_20 22:00 | 3235835 | 3 | 5.9150 | 15.7514 | -115.8575 | 10.7183 | 155.2835 | 0.0085 | 0.0006 |
| 2024_09_20 22:00 | 3215128 | 4 | 10.5225 | 14.2866 | -114.1944 | 17.3403 | 134.1682 | 0.0065 | 0.0003 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416757_ADFCD780 | 504990 | 83 | -90.0 | 504990 | 304 | -84.7 | 504990 | 971 | -90.3 | 504990 | 675 |
| MR_1774416757_9FE9B723 | 504990 | 304 | -86.5 | 504990 | 83 | -90.9 | 504990 | 971 | -87.5 | 504990 | 675 |
| MR_1774416757_2617EF6D | 504990 | 83 | -92.8 | 504990 | 304 | -86.8 | 504990 | 971 | -88.6 | 504990 | 675 |
| MR_1774416757_A930AE44 | 504990 | 83 | -90.6 | 504990 | 304 | -87.5 | 504990 | 971 | -90.1 | 504990 | 675 |
| MR_1774416757_FC8DB38C | 504990 | 83 | -91.2 | 504990 | 304 | -86.8 | 504990 | 971 | -89.3 | 504990 | 675 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 27: `d1d84ece-b08...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d1d84ece-b085-4c71-a931-00728e0cbd03` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Lift the tilt angle  of 3271204_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[27] topology](images/train_0027.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3271204_4 by 50 degrees
- `C2`: Decrease A3 Offset threshold for 3224021_3
- `C3`: Press down the tilt angle of 3224021_3 by 4 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222661_2
- `C5`: Increase transmission power for 3224021_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222661_2
- `C7`: Decrease transmission power for 3224021_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224021_3
- `C9`: Adjust the azimuth of 3224021_3 by 43 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224021_3
- `C12`: Press down the tilt angle  of 3271204_4 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3222661_2
- `C14`: Check test server and transmission issues
- `C15`: Lift the tilt angle  of 3271204_4 by 10 degrees **← 정답**
- `C16`: Add neighbor relationship between 3224021_3 and 3222661_2
- `C17`: Decrease transmission power for 3222661_2
- `C18`: Increase A3 Offset threshold for 3222661_2
- `C19`: Lift the tilt angle of 3224021_3 by 4 degrees
- `C20`: Increase transmission power for 3222661_2
- `C21`: Add neighbor relationship between 3271204_4 and 3222661_2
- `C22`: Increase A3 Offset threshold for 3224021_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.599 | MS1 | 121.4656676843 | 31.1446307500 | 923 | 504990 | -91.79 | 14.93 | 350.36 | 0.05 | 2.61 | 1571 |
| 2024-09-20 22:21:32.683 | MS1 | 121.4656692950 | 31.1446240570 | 923 | 504990 | -87.27 | 17.58 | 439.71 | 0.09 | 2.90 | 1560 |
| 2024-09-20 22:21:33.677 | MS1 | 121.4656639086 | 31.1446190406 | 923 | 504990 | -91.07 | 14.52 | 564.33 | 0.10 | 2.77 | 1599 |
| 2024-09-20 22:21:34.496 | MS1 | 121.4656764447 | 31.1446355075 | 923 | 504990 | -86.63 | 12.35 | 64.55 | 0.14 | 2.82 | 1595 |
| 2024-09-20 22:21:35.522 | MS1 | 121.4656621889 | 31.1446315957 | 923 | 504990 | -88.03 | 14.51 | 52.06 | 0.01 | 2.63 | 1592 |
| 2024-09-20 22:21:36.248 | MS1 | 121.4656764833 | 31.1446354134 | 923 | 504990 | -87.84 | 14.61 | 81.44 | 0.11 | 2.41 | 1566 |
| 2024-09-20 22:21:37.269 | MS1 | 121.4656625730 | 31.1446181183 | 923 | 504990 | -90.80 | 9.10 | 52.01 | 0.02 | 2.28 | 1587 |
| 2024-09-20 22:21:38.119 | MS1 | 121.4656599064 | 31.1446319378 | 923 | 504990 | -93.88 | 9.75 | 94.42 | 0.14 | 2.04 | 1585 |
| 2024-09-20 22:21:39.725 | MS1 | 121.4656723363 | 31.1446296056 | 923 | 504990 | -93.42 | 10.31 | 85.42 | 0.12 | 2.08 | 1576 |
| 2024-09-20 22:21:40.420 | MS1 | 121.4656623723 | 31.1446293139 | 923 | 504990 | -89.27 | 10.91 | 451.37 | 0.18 | 2.43 | 1568 |
| 2024-09-20 22:21:41.824 | MS1 | 121.4656642258 | 31.1446235477 | 923 | 504990 | -91.10 | 11.46 | 548.60 | 0.17 | 2.56 | 1585 |
| 2024-09-20 22:21:42.691 | MS1 | 121.4656712191 | 31.1446297049 | 923 | 504990 | -92.42 | 7.60 | 316.55 | 0.17 | 2.10 | 1566 |

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
| 3222661 | 2 | 121.4674791824 | 31.1511550111 | 271 | 8 | 10 | 27.2 | TDD | 603 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3224021 | 3 | 121.4655339196 | 31.1542901295 | 136 | 1 | 11 | 47.2 | TDD | 923 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3229252 | 1 | 121.4752166034 | 31.1477517140 | 302 | 3 | 8 | 42.7 | TDD | 148 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3271204 | 4 | 121.4706643777 | 31.1501088108 | 312 | 14 | 0 | 25.2 | TDD | 541 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.040 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.065 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.194 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.194 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.919 | NREventA3 | measId:2;ServCellPCI:797;Se... |
| 2024-09-20 22:21:38.159 | NRHandoverAttempt | SourcePCI:797;SourceNR-ARFC... |
| 2024-09-20 22:21:38.196 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.209 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.349 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.349 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229252 | 1 | 10.3747 | 18.8978 | -115.0912 | 8.7623 | 195.8706 | 0.0085 | 0.0184 |
| 2024_09_20 22:00 | 3222661 | 2 | 11.5854 | 6.3636 | -116.9304 | 13.7382 | 192.1603 | 0.0071 | 0.0181 |
| 2024_09_20 22:00 | 3224021 | 3 | 85.6759 | 93.9185 | -114.8500 | 19.6603 | 86.8240 | 0.0064 | 0.0071 |
| 2024_09_20 22:00 | 3271204 | 4 | 18.5741 | 6.5099 | -115.9338 | 15.7609 | 150.2293 | 0.0018 | 0.0074 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415087_61F0770E | 504990 | 923 | -87.5 | 504990 | 603 | -95.3 | 504990 | 541 | -99.3 | 504990 | 148 |
| MR_1774415087_CB4A66C2 | 504990 | 923 | -85.2 | 504990 | 603 | -95.1 | 504990 | 541 | -96.6 | 504990 | 148 |
| MR_1774415087_A2319487 | 504990 | 923 | -88.1 | 504990 | 603 | -95.4 | 504990 | 541 | -98.7 | 504990 | 148 |
| MR_1774415087_CD5180E2 | 504990 | 923 | -85.4 | 504990 | 603 | -96.4 | 504990 | 541 | -97.7 | 504990 | 148 |
| MR_1774415087_0E6AABFD | 504990 | 923 | -86.2 | 504990 | 603 | -95.0 | 504990 | 541 | -98.1 | 504990 | 148 |
| MR_1774415087_3CFAFE12 | 504990 | 923 | -86.6 | 504990 | 603 | -95.7 | 504990 | 541 | -96.5 | 504990 | 148 |
| MR_1774415087_D9751CF4 | 504990 | 923 | -85.8 | 504990 | 603 | -97.7 | 504990 | 541 | -98.8 | 504990 | 148 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 28: `7516c555-271...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7516c555-2713-46d5-bac4-3cabb656387d` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[28] topology](images/train_0028.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3215895_4 and 3256824_2
- `C2`: Check test server and transmission issues
- `C3`: Add neighbor relationship between 3239914_3 and 3256824_2
- `C4`: Press down the tilt angle of 3215895_4 by 4 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215895_4
- `C6`: Increase A3 Offset threshold for 3215895_4
- `C7`: Adjust the azimuth of 3215895_4 by 50 degrees
- `C8`: Insufficient data; more data is needed for judgment. **← 정답**
- `C9`: Increase transmission power for 3215895_4
- `C10`: Adjust the azimuth of 3256824_2 by 50 degrees
- `C11`: Increase transmission power for 3256824_2
- `C12`: Decrease transmission power for 3215895_4
- `C13`: Decrease transmission power for 3256824_2
- `C14`: Increase A3 Offset threshold for 3256824_2
- `C15`: Decrease A3 Offset threshold for 3215895_4
- `C16`: Lift the tilt angle of 3215895_4 by 4 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215895_4
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256824_2
- `C19`: Lift the tilt angle  of 3256824_2 by 6 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256824_2
- `C21`: Press down the tilt angle  of 3256824_2 by 6 degrees
- `C22`: Decrease A3 Offset threshold for 3256824_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.314 | MS1 | 121.4656772942 | 31.1446369660 | 807 | 504990 | -89.23 | 13.87 | 386.40 | 0.17 | 2.55 | 1588 |
| 2024-09-20 22:21:32.911 | MS1 | 121.4656708837 | 31.1446378390 | 807 | 504990 | -91.33 | 15.10 | 514.41 | 0.17 | 2.82 | 1583 |
| 2024-09-20 22:21:33.858 | MS1 | 121.4656711048 | 31.1446295881 | 807 | 504990 | -88.87 | 17.54 | 294.66 | 0.01 | 2.26 | 1598 |
| 2024-09-20 22:21:34.592 | MS1 | 121.4656629002 | 31.1446320578 | 807 | 504990 | -85.54 | 13.36 | 74.67 | 0.09 | 2.31 | 1569 |
| 2024-09-20 22:21:35.831 | MS1 | 121.4656599705 | 31.1446329641 | 807 | 504990 | -89.73 | 12.95 | 76.52 | 0.01 | 2.04 | 1584 |
| 2024-09-20 22:21:36.441 | MS1 | 121.4656767450 | 31.1446359581 | 807 | 504990 | -90.33 | 13.63 | 68.23 | 0.13 | 2.49 | 1587 |
| 2024-09-20 22:21:37.279 | MS1 | 121.4656769401 | 31.1446284184 | 807 | 504990 | -93.64 | 10.81 | 66.68 | 0.17 | 2.62 | 1574 |
| 2024-09-20 22:21:38.899 | MS1 | 121.4656728485 | 31.1446376430 | 807 | 504990 | -89.34 | 11.62 | 97.20 | 0.05 | 2.78 | 1565 |
| 2024-09-20 22:21:39.416 | MS1 | 121.4656711661 | 31.1446182097 | 807 | 504990 | -90.32 | 7.09 | 61.12 | 0.06 | 2.58 | 1593 |
| 2024-09-20 22:21:40.263 | MS1 | 121.4656595333 | 31.1446244465 | 807 | 504990 | -91.83 | 8.62 | 453.87 | 0.07 | 2.25 | 1594 |
| 2024-09-20 22:21:41.793 | MS1 | 121.4656652120 | 31.1446202031 | 807 | 504990 | -90.93 | 11.35 | 551.62 | 0.04 | 2.11 | 1593 |
| 2024-09-20 22:21:42.126 | MS1 | 121.4656688259 | 31.1446352247 | 807 | 504990 | -90.63 | 8.01 | 574.34 | 0.13 | 2.73 | 1597 |

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
| 3215895 | 4 | 121.4759134474 | 31.1514859035 | 160 | 3 | 7 | 16.9 | TDD | 807 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3230476 | 1 | 121.4747926025 | 31.1523181909 | 262 | 14 | 8 | 18.5 | TDD | 264 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3239914 | 3 | 121.4680298352 | 31.1497493943 | 74 | 1 | 9 | 18.7 | TDD | 675 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3256824 | 2 | 121.4696486293 | 31.1504847480 | 289 | 3 | 3 | 44.7 | TDD | 163 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.317 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.335 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.463 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.463 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.158 | NREventA3 | measId:2;ServCellPCI:395;Se... |
| 2024-09-20 22:21:38.398 | NRHandoverAttempt | SourcePCI:395;SourceNR-ARFC... |
| 2024-09-20 22:21:38.441 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.451 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.575 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.575 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3230476 | 1 | 87.8895 | 79.0398 | -114.3686 | 7.2590 | 101.4241 | 0.0030 | 0.0074 |
| 2024_09_19 22:00 | 3256824 | 2 | 88.1992 | 86.7600 | -115.8587 | 8.3501 | 96.0444 | 0.0121 | 0.0028 |
| 2024_09_19 22:00 | 3239914 | 3 | 80.1435 | 84.1709 | -114.4303 | 13.8523 | 187.1353 | 0.0151 | 0.0142 |
| 2024_09_19 22:00 | 3215895 | 4 | 85.1853 | 88.1536 | -117.6093 | 5.4829 | 152.6993 | 0.0143 | 0.0079 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413819_26790C1B | 504990 | 807 | -85.1 | 504990 | 163 | -91.5 | 504990 | 675 | -93.9 | 504990 | 264 |
| MR_1774413819_68109257 | 504990 | 807 | -86.2 | 504990 | 163 | -90.1 | 504990 | 675 | -95.1 | 504990 | 264 |
| MR_1774413819_5EF96B30 | 504990 | 807 | -86.6 | 504990 | 163 | -91.9 | 504990 | 675 | -95.1 | 504990 | 264 |
| MR_1774413819_2F180130 | 504990 | 807 | -83.9 | 504990 | 163 | -91.8 | 504990 | 675 | -94.6 | 504990 | 264 |
| MR_1774413819_25949293 | 504990 | 807 | -85.3 | 504990 | 163 | -88.7 | 504990 | 675 | -92.6 | 504990 | 264 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 29: `c4e6f7d5-153...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c4e6f7d5-153b-46fd-b91e-d2b22ffa4c97` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252252_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[29] topology](images/train_0029.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease transmission power for 3255322_5
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252252_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252252_1 **← 정답**
- `C5`: Decrease transmission power for 3252252_1
- `C6`: Check test server and transmission issues
- `C7`: Adjust the azimuth of 3255322_5 by 33 degrees
- `C8`: Increase A3 Offset threshold for 3255322_5
- `C9`: Add neighbor relationship between 3252252_1 and 3255322_5
- `C10`: Add neighbor relationship between 3211546_9 and 3255322_5
- `C11`: Decrease A3 Offset threshold for 3252252_1
- `C12`: Press down the tilt angle of 3252252_1 by 4 degrees
- `C13`: Press down the tilt angle  of 3255322_5 by 2 degrees
- `C14`: Increase transmission power for 3255322_5
- `C15`: Decrease A3 Offset threshold for 3255322_5
- `C16`: Increase A3 Offset threshold for 3252252_1
- `C17`: Increase transmission power for 3252252_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255322_5
- `C19`: Adjust the azimuth of 3252252_1 by 6 degrees
- `C20`: Lift the tilt angle  of 3255322_5 by 2 degrees
- `C21`: Lift the tilt angle of 3252252_1 by 4 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255322_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.154 | MS1 | 121.4656683881 | 31.1446268572 | 578 | 504990 | -93.00 | 13.51 | 346.50 | 0.01 | 2.82 | 1597 |
| 2024-09-20 22:21:32.995 | MS1 | 121.4656687485 | 31.1446334222 | 421 | 504990 | -95.87 | 13.82 | 568.94 | 0.17 | 2.67 | 1593 |
| 2024-09-20 22:21:33.886 | MS1 | 121.4656728522 | 31.1446195739 | 414 | 504990 | -93.69 | 10.79 | 570.07 | 0.15 | 2.47 | 1571 |
| 2024-09-20 22:21:34.214 | MS1 | 121.4656608816 | 31.1446202604 | 339 | 152650 | -91.67 | 2.09 | 63.02 | 0.06 | 1.66 | 959 |
| 2024-09-20 22:21:35.929 | MS1 | 121.4656743282 | 31.1446299122 | 145 | 152650 | -88.99 | 7.48 | 67.19 | 0.10 | 1.65 | 942 |
| 2024-09-20 22:21:36.272 | MS1 | 121.4656679262 | 31.1446325692 | 363 | 152650 | -93.07 | 2.32 | 54.61 | 0.08 | 1.96 | 931 |
| 2024-09-20 22:21:37.174 | MS1 | 121.4656650469 | 31.1446216185 | 445 | 152650 | -90.75 | 7.60 | 96.05 | 0.18 | 1.95 | 1000 |
| 2024-09-20 22:21:38.914 | MS1 | 121.4656706324 | 31.1446315656 | 339 | 152650 | -88.88 | 2.46 | 80.12 | 0.10 | 1.88 | 977 |
| 2024-09-20 22:21:39.207 | MS1 | 121.4656678590 | 31.1446303519 | 145 | 152650 | -88.26 | 4.23 | 62.65 | 0.11 | 1.97 | 919 |
| 2024-09-20 22:21:40.751 | MS1 | 121.4656736905 | 31.1446257760 | 363 | 152650 | -91.53 | 5.85 | 81.93 | 0.12 | 2.67 | 1587 |
| 2024-09-20 22:21:41.592 | MS1 | 121.4656758727 | 31.1446217650 | 445 | 152650 | -96.40 | 2.58 | 86.94 | 0.11 | 2.58 | 1592 |
| 2024-09-20 22:21:42.241 | MS1 | 121.4656633919 | 31.1446307452 | 339 | 152650 | -89.42 | 6.22 | 77.31 | 0.15 | 2.13 | 1594 |

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
| 3211546 | 9 | 121.4720948054 | 31.1457476573 | 138 | 4 | 8 | 2.6 | FDD | 363 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3212465 | 8 | 121.4688822692 | 31.1523674007 | 134 | 7 | 8 | 13.5 | FDD | 709 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3224270 | 12 | 121.4690802155 | 31.1556233485 | 128 | 15 | 12 | 7.0 | FDD | 88 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3227602 | 2 | 121.4708655819 | 31.1519668103 | 211 | 6 | 7 | 2.3 | TDD | 228 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3229060 | 11 | 121.4671337474 | 31.1456800070 | 86 | 11 | 10 | 11.2 | FDD | 339 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3240585 | 10 | 121.4671818604 | 31.1472829825 | 66 | 10 | 12 | 1.0 | FDD | 145 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3248565 | 3 | 121.4730495218 | 31.1502022827 | 25 | 0 | 10 | 9.7 | TDD | 421 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3252252 | 1 | 121.4709604512 | 31.1510074704 | 209 | 3 | 0 | 8.4 | TDD | 578 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3255307 | 6 | 121.4670855220 | 31.1450713450 | 145 | 3 | 10 | 23.7 | TDD | 414 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3255322 | 5 | 121.4699961241 | 31.1526267674 | 172 | 1 | 5 | 15.5 | TDD | 941 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3259671 | 4 | 121.4743969758 | 31.1471959971 | 291 | 14 | 6 | 14.3 | TDD | 615 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3276097 | 7 | 121.4693367427 | 31.1554610730 | 272 | 9 | 6 | 29.2 | FDD | 261 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3278128 | 13 | 121.4682257400 | 31.1512794332 | 316 | 9 | 1 | 7.4 | FDD | 445 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |

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
| 2024-09-20 22:21:31.458 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.476 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.594 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.594 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.281 | NREventA2 | measId:1;ServCellPCI:85;Ser... |
| 2024-09-20 22:21:35.399 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.664 | NREventA5 | measId:3;ServCellPCI:85;Ser... |
| 2024-09-20 22:21:35.700 | NRHandoverAttempt | SourcePCI:85;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.725 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.740 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.880 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.880 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252252 | 1 | 13.3915 | 16.7819 | -116.2959 | 8.9872 | 108.4168 | 0.0062 | 0.0141 |
| 2024_09_20 22:00 | 3227602 | 2 | 6.8811 | 13.9182 | -117.5511 | 19.6639 | 97.8765 | 0.0103 | 0.0139 |
| 2024_09_20 22:00 | 3248565 | 3 | 12.1802 | 10.9996 | -114.4961 | 16.2343 | 124.0366 | 0.0077 | 0.0108 |
| 2024_09_20 22:00 | 3259671 | 4 | 6.0176 | 7.9086 | -116.9123 | 8.8059 | 154.4338 | 0.0097 | 0.0153 |
| 2024_09_20 22:00 | 3255322 | 5 | 13.1943 | 10.5739 | -116.9640 | 19.7411 | 151.1440 | 0.0113 | 0.0023 |
| 2024_09_20 22:00 | 3255307 | 6 | 11.7569 | 13.1901 | -115.7279 | 14.6455 | 91.5047 | 0.0006 | 0.0190 |
| 2024_09_20 22:00 | 3276097 | 7 | 7.1374 | 16.6972 | -114.9934 | 4.7667 | 58.7770 | 0.0123 | 0.0036 |
| 2024_09_20 22:00 | 3212465 | 8 | 12.1038 | 12.0713 | -117.4586 | 3.5804 | 38.2821 | 0.0145 | 0.0008 |
| 2024_09_20 22:00 | 3211546 | 9 | 8.2467 | 18.7473 | -116.4409 | 3.3477 | 49.7285 | 0.0067 | 0.0142 |
| 2024_09_20 22:00 | 3240585 | 10 | 14.9002 | 6.9978 | -115.5187 | 4.7114 | 30.6236 | 0.0005 | 0.0144 |
| 2024_09_20 22:00 | 3229060 | 11 | 17.4791 | 5.9378 | -116.7845 | 3.4882 | 25.4761 | 0.0182 | 0.0106 |
| 2024_09_20 22:00 | 3224270 | 12 | 16.2404 | 8.6057 | -117.9642 | 4.2471 | 44.2449 | 0.0004 | 0.0042 |
| 2024_09_20 22:00 | 3278128 | 13 | 13.8425 | 13.0323 | -114.0213 | 3.9234 | 39.4620 | 0.0191 | 0.0179 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414098_75292769 | 152650 | 339 | -93.5 | 152650 | 261 | -96.3 | 152650 | 709 | -102.4 | 152650 | 88 |
| MR_1774414098_F9A8CFBA | 152650 | 339 | -91.8 | 152650 | 261 | -96.1 | 152650 | 709 | -104.7 | 152650 | 88 |
| MR_1774414098_7E9FA737 | 152650 | 339 | -91.8 | 152650 | 261 | -95.2 | 152650 | 709 | -103.4 | 152650 | 88 |
| MR_1774414098_B78C28CA | 504990 | 414 | -91.8 | 504990 | 941 | -97.0 | 504990 | 615 | -98.0 | 504990 | 228 |
| MR_1774414098_E2E5D8B0 | 504990 | 414 | -92.3 | 504990 | 941 | -95.9 | 504990 | 615 | -95.9 | 504990 | 228 |
| MR_1774414098_13B5C125 | 152650 | 339 | -90.8 | 152650 | 261 | -96.0 | 152650 | 709 | -104.1 | 152650 | 88 |
| MR_1774414098_5F462A3E | 504990 | 414 | -95.6 | 504990 | 941 | -96.1 | 504990 | 615 | -98.5 | 504990 | 228 |

> *... 2개 열 생략 (전체 14열)*

---
