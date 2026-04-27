# Track A 문제 분석 — train[1590]~train[1599]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1590] ~ train[1599] (10개)

## 목차

1. [문제 1590: `090cae2e-b35...`](#1590) — single-answer, 정답: C15
2. [문제 1591: `38d110fc-3da...`](#1591) — single-answer, 정답: C18
3. [문제 1592: `ceecfed5-81a...`](#1592) — single-answer, 정답: C9
4. [문제 1593: `cf154c69-1a1...`](#1593) — single-answer, 정답: C11
5. [문제 1594: `6b3ba005-13b...`](#1594) — single-answer, 정답: C21
6. [문제 1595: `6100a0f7-cfc...`](#1595) — single-answer, 정답: C20
7. [문제 1596: `31b432f3-bb1...`](#1596) — single-answer, 정답: C7
8. [문제 1597: `2643a7b3-62c...`](#1597) — single-answer, 정답: C17
9. [문제 1598: `5eaa2668-6d2...`](#1598) — single-answer, 정답: C16
10. [문제 1599: `9bd1cfd8-eb3...`](#1599) — single-answer, 정답: C17

---

### 문제 1590: `090cae2e-b35...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `090cae2e-b357-4c33-b1de-381e6ccdbfca` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Add neighbor relationship between 3231689_2 and 3222348_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1590] topology](images/train_1590.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3231689_2 by 8 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222348_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222348_3
- `C4`: Lift the tilt angle  of 3222348_3 by 3 degrees
- `C5`: Increase A3 Offset threshold for 3231689_2
- `C6`: Increase transmission power for 3231689_2
- `C7`: Press down the tilt angle of 3231689_2 by 8 degrees
- `C8`: Increase transmission power for 3222348_3
- `C9`: Decrease A3 Offset threshold for 3222348_3
- `C10`: Check test server and transmission issues
- `C11`: Decrease transmission power for 3231689_2
- `C12`: Increase A3 Offset threshold for 3222348_3
- `C13`: Adjust the azimuth of 3231689_2 by 50 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231689_2
- `C15`: Add neighbor relationship between 3231689_2 and 3222348_3 **← 정답**
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231689_2
- `C17`: Decrease transmission power for 3222348_3
- `C18`: Decrease A3 Offset threshold for 3231689_2
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Add neighbor relationship between 3252908_4 and 3222348_3
- `C21`: Press down the tilt angle  of 3222348_3 by 3 degrees
- `C22`: Adjust the azimuth of 3222348_3 by 41 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.410 | MS1 | 121.4656706344 | 31.1446277708 | 170 | 504990 | -81.33 | 15.39 | 314.12 | 0.06 | 2.96 | 1565 |
| 2024-09-20 22:21:32.238 | MS1 | 121.4656632592 | 31.1446210527 | 170 | 504990 | -75.59 | 16.02 | 379.21 | 0.06 | 2.28 | 1572 |
| 2024-09-20 22:21:33.377 | MS1 | 121.4656766697 | 31.1446347572 | 170 | 504990 | -77.91 | 14.10 | 452.52 | 0.18 | 2.74 | 1565 |
| 2024-09-20 22:21:34.933 | MS1 | 121.4656712865 | 31.1446315740 | 170 | 504990 | -89.08 | -1.32 | 51.16 | 0.00 | 1.22 | 1579 |
| 2024-09-20 22:21:35.987 | MS1 | 121.4656693010 | 31.1446259238 | 170 | 504990 | -86.19 | -3.22 | 53.99 | 0.07 | 1.26 | 1594 |
| 2024-09-20 22:21:36.884 | MS1 | 121.4656679826 | 31.1446235843 | 170 | 504990 | -85.07 | -3.44 | 26.79 | 0.03 | 1.37 | 1577 |
| 2024-09-20 22:21:37.269 | MS1 | 121.4656720872 | 31.1446294805 | 170 | 504990 | -87.76 | -1.41 | 35.69 | 0.10 | 1.43 | 1596 |
| 2024-09-20 22:21:38.689 | MS1 | 121.4656696600 | 31.1446336876 | 170 | 504990 | -81.17 | 12.91 | 571.74 | 0.17 | 1.17 | 1594 |
| 2024-09-20 22:21:39.404 | MS1 | 121.4656710063 | 31.1446279794 | 170 | 504990 | -80.53 | 14.17 | 591.54 | 0.11 | 1.19 | 1600 |
| 2024-09-20 22:21:40.600 | MS1 | 121.4656596018 | 31.1446302069 | 170 | 504990 | -79.42 | 15.85 | 542.01 | 0.04 | 2.80 | 1593 |
| 2024-09-20 22:21:41.693 | MS1 | 121.4656721983 | 31.1446271944 | 170 | 504990 | -80.33 | 17.11 | 369.09 | 0.03 | 2.60 | 1564 |
| 2024-09-20 22:21:42.576 | MS1 | 121.4656688728 | 31.1446288230 | 170 | 504990 | -83.82 | 14.70 | 486.19 | 0.00 | 2.85 | 1565 |

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
| 3222046 | 1 | 121.4652604744 | 31.1554875249 | 189 | 0 | 1 | 21.8 | TDD | 768 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3222348 | 3 | 121.4720408106 | 31.1461261491 | 296 | 0 | 5 | 35.3 | TDD | 418 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3231689 | 2 | 121.4701265446 | 31.1502860099 | 312 | 5 | 3 | 43.6 | TDD | 170 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3252908 | 4 | 121.4741407141 | 31.1515491595 | 72 | 14 | 2 | 16.2 | TDD | 51 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.523 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.538 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.640 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.640 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.392 | NREventA3 | measId:2;ServCellPCI:990;Se... |
| 2024-09-20 22:21:36.392 | NREventA3 | measId:2;ServCellPCI:990;Se... |
| 2024-09-20 22:21:37.392 | NREventA3 | measId:2;ServCellPCI:990;Se... |
| 2024-09-20 22:21:39.892 | NRRRCReestablishAttempt | PCI:990 |
| 2024-09-20 22:21:39.910 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.922 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:40.067 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.067 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222046 | 1 | 18.2538 | 18.1266 | -115.7327 | 17.6314 | 152.5806 | 0.0175 | 0.0143 |
| 2024_09_20 22:00 | 3231689 | 2 | 5.0961 | 19.1805 | -114.9671 | 15.1695 | 124.8354 | 0.0073 | 0.1649 |
| 2024_09_20 22:00 | 3222348 | 3 | 7.8114 | 19.3624 | -115.7362 | 8.5141 | 161.8332 | 0.0084 | 0.0163 |
| 2024_09_20 22:00 | 3252908 | 4 | 8.5162 | 18.9829 | -114.9929 | 15.3358 | 101.5028 | 0.0163 | 0.0171 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412471_DD0516A5 | 504990 | 418 | -85.4 | 504990 | 170 | -90.2 | 504990 | 51 | -90.9 | 504990 | 768 |
| MR_1774412471_D3B48093 | 504990 | 170 | -87.3 | 504990 | 418 | -86.4 | 504990 | 51 | -93.6 | 504990 | 768 |
| MR_1774412471_664BF3E9 | 504990 | 418 | -83.3 | 504990 | 170 | -90.7 | 504990 | 51 | -90.5 | 504990 | 768 |
| MR_1774412471_194D5D77 | 504990 | 418 | -86.8 | 504990 | 170 | -89.6 | 504990 | 51 | -93.6 | 504990 | 768 |
| MR_1774412471_A5C0DA82 | 504990 | 418 | -85.5 | 504990 | 170 | -88.2 | 504990 | 51 | -93.1 | 504990 | 768 |
| MR_1774412471_6E18BB69 | 504990 | 170 | -89.3 | 504990 | 418 | -83.2 | 504990 | 51 | -91.9 | 504990 | 768 |
| MR_1774412471_B029CAC6 | 504990 | 418 | -84.6 | 504990 | 170 | -88.2 | 504990 | 51 | -91.7 | 504990 | 768 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1591: `38d110fc-3da...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `38d110fc-3dab-4ac8-8eef-ebd57ea9bf41` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1591] topology](images/train_1591.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257134_1
- `C2`: Decrease A3 Offset threshold for 3212458_3
- `C3`: Add neighbor relationship between 3222494_4 and 3257134_1
- `C4`: Increase A3 Offset threshold for 3212458_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212458_3
- `C6`: Decrease transmission power for 3257134_1
- `C7`: Lift the tilt angle  of 3257134_1 by 6 degrees
- `C8`: Increase transmission power for 3257134_1
- `C9`: Decrease transmission power for 3212458_3
- `C10`: Lift the tilt angle of 3212458_3 by 10 degrees
- `C11`: Adjust the azimuth of 3212458_3 by 50 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212458_3
- `C13`: Press down the tilt angle  of 3257134_1 by 6 degrees
- `C14`: Check test server and transmission issues
- `C15`: Adjust the azimuth of 3257134_1 by 50 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257134_1
- `C17`: Press down the tilt angle of 3212458_3 by 10 degrees
- `C18`: Insufficient data; more data is needed for judgment. **← 정답**
- `C19`: Add neighbor relationship between 3212458_3 and 3257134_1
- `C20`: Decrease A3 Offset threshold for 3257134_1
- `C21`: Increase transmission power for 3212458_3
- `C22`: Increase A3 Offset threshold for 3257134_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.245 | MS1 | 121.4656738272 | 31.1446257719 | 619 | 504990 | -85.62 | 15.66 | 496.33 | 0.12 | 2.99 | 1580 |
| 2024-09-20 22:21:32.552 | MS1 | 121.4656777477 | 31.1446215883 | 619 | 504990 | -87.10 | 12.79 | 396.01 | 0.13 | 2.23 | 1579 |
| 2024-09-20 22:21:33.108 | MS1 | 121.4656679605 | 31.1446349725 | 619 | 504990 | -89.69 | 13.84 | 507.17 | 0.16 | 2.49 | 1581 |
| 2024-09-20 22:21:34.478 | MS1 | 121.4656701736 | 31.1446300848 | 619 | 504990 | -86.43 | 13.53 | 90.01 | 0.03 | 2.58 | 1587 |
| 2024-09-20 22:21:35.489 | MS1 | 121.4656687589 | 31.1446191359 | 619 | 504990 | -85.37 | 15.72 | 84.78 | 0.15 | 2.06 | 1567 |
| 2024-09-20 22:21:36.497 | MS1 | 121.4656725824 | 31.1446336763 | 619 | 504990 | -90.43 | 12.26 | 100.60 | 0.06 | 2.17 | 1578 |
| 2024-09-20 22:21:37.827 | MS1 | 121.4656693974 | 31.1446239118 | 619 | 504990 | -91.89 | 7.12 | 101.75 | 0.05 | 2.55 | 1587 |
| 2024-09-20 22:21:38.286 | MS1 | 121.4656649786 | 31.1446320218 | 619 | 504990 | -91.16 | 10.48 | 49.09 | 0.11 | 2.69 | 1583 |
| 2024-09-20 22:21:39.402 | MS1 | 121.4656623910 | 31.1446369847 | 619 | 504990 | -92.59 | 7.65 | 65.10 | 0.16 | 2.62 | 1572 |
| 2024-09-20 22:21:40.558 | MS1 | 121.4656584537 | 31.1446326018 | 619 | 504990 | -91.72 | 10.90 | 321.54 | 0.06 | 2.26 | 1597 |
| 2024-09-20 22:21:41.919 | MS1 | 121.4656587483 | 31.1446358832 | 619 | 504990 | -89.71 | 12.45 | 450.01 | 0.01 | 2.79 | 1574 |
| 2024-09-20 22:21:42.318 | MS1 | 121.4656748560 | 31.1446352350 | 619 | 504990 | -91.07 | 8.78 | 504.57 | 0.07 | 2.67 | 1598 |

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
| 3212458 | 3 | 121.4694429073 | 31.1534476388 | 309 | 10 | 1 | 46.3 | TDD | 619 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3221325 | 2 | 121.4720313284 | 31.1488328960 | 33 | 1 | 6 | 40.0 | TDD | 721 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3222494 | 4 | 121.4707123581 | 31.1549765720 | 152 | 15 | 4 | 48.4 | TDD | 910 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3257134 | 1 | 121.4669367208 | 31.1534447482 | 16 | 5 | 9 | 23.8 | TDD | 416 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.331 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.356 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.502 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.502 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.164 | NREventA3 | measId:2;ServCellPCI:948;Se... |
| 2024-09-20 22:21:38.404 | NRHandoverAttempt | SourcePCI:948;SourceNR-ARFC... |
| 2024-09-20 22:21:38.450 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.463 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.587 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.587 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3257134 | 1 | 78.6459 | 94.8064 | -115.7563 | 5.6551 | 157.7534 | 0.0118 | 0.0009 |
| 2024_09_19 22:00 | 3221325 | 2 | 82.9037 | 83.8962 | -115.4577 | 18.1040 | 98.9594 | 0.0148 | 0.0060 |
| 2024_09_19 22:00 | 3212458 | 3 | 81.4092 | 78.1819 | -116.4581 | 12.8040 | 135.8214 | 0.0132 | 0.0155 |
| 2024_09_19 22:00 | 3222494 | 4 | 82.4698 | 86.2964 | -117.6868 | 16.6231 | 187.4510 | 0.0058 | 0.0143 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414686_CE32FDCF | 504990 | 619 | -87.7 | 504990 | 416 | -90.5 | 504990 | 910 | -97.7 | 504990 | 721 |
| MR_1774414686_8F3D43C1 | 504990 | 619 | -87.5 | 504990 | 416 | -91.8 | 504990 | 910 | -95.1 | 504990 | 721 |
| MR_1774414686_6382193A | 504990 | 619 | -87.5 | 504990 | 416 | -91.7 | 504990 | 910 | -95.2 | 504990 | 721 |
| MR_1774414686_959A8813 | 504990 | 619 | -87.1 | 504990 | 416 | -91.6 | 504990 | 910 | -97.3 | 504990 | 721 |
| MR_1774414686_E9C0E996 | 504990 | 619 | -84.9 | 504990 | 416 | -91.0 | 504990 | 910 | -94.7 | 504990 | 721 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1592: `ceecfed5-81a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ceecfed5-81af-4042-b56e-781e2390a7b0` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3267895_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1592] topology](images/train_1592.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3276106_1 and 3267963_3
- `C2`: Decrease transmission power for 3267895_2
- `C3`: Adjust the azimuth of 3267963_3 by 20 degrees
- `C4`: Lift the tilt angle  of 3267963_3 by 10 degrees
- `C5`: Increase transmission power for 3267963_3
- `C6`: Increase A3 Offset threshold for 3267895_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267963_3
- `C8`: Decrease A3 Offset threshold for 3267895_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267895_2 **← 정답**
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267895_2
- `C11`: Add neighbor relationship between 3267895_2 and 3267963_3
- `C12`: Press down the tilt angle of 3267895_2 by 3 degrees
- `C13`: Decrease A3 Offset threshold for 3267963_3
- `C14`: Increase transmission power for 3267895_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267963_3
- `C16`: Check test server and transmission issues
- `C17`: Decrease transmission power for 3267963_3
- `C18`: Press down the tilt angle  of 3267963_3 by 10 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase A3 Offset threshold for 3267963_3
- `C21`: Lift the tilt angle of 3267895_2 by 3 degrees
- `C22`: Adjust the azimuth of 3267895_2 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.958 | MS1 | 121.4656778845 | 31.1446243031 | 628 | 504990 | -90.31 | 17.33 | 474.53 | 0.02 | 2.86 | 1566 |
| 2024-09-20 22:21:32.427 | MS1 | 121.4656719061 | 31.1446267158 | 628 | 504990 | -87.33 | 17.17 | 315.70 | 0.18 | 2.57 | 1592 |
| 2024-09-20 22:21:33.211 | MS1 | 121.4656662048 | 31.1446192502 | 628 | 504990 | -91.60 | 17.04 | 444.98 | 0.01 | 2.98 | 1583 |
| 2024-09-20 22:21:34.143 | MS1 | 121.4656594254 | 31.1446218868 | 628 | 504990 | -91.70 | 15.19 | 90.51 | 0.62 | 2.59 | 659 |
| 2024-09-20 22:21:35.934 | MS1 | 121.4656690090 | 31.1446306367 | 628 | 504990 | -89.71 | 13.91 | 74.22 | 0.69 | 2.40 | 662 |
| 2024-09-20 22:21:36.273 | MS1 | 121.4656672498 | 31.1446338216 | 628 | 504990 | -91.23 | 14.30 | 50.61 | 0.59 | 2.60 | 689 |
| 2024-09-20 22:21:37.979 | MS1 | 121.4656752661 | 31.1446227701 | 628 | 504990 | -90.29 | 7.46 | 101.23 | 0.58 | 2.97 | 536 |
| 2024-09-20 22:21:38.641 | MS1 | 121.4656627663 | 31.1446336198 | 628 | 504990 | -91.60 | 9.99 | 87.89 | 0.65 | 2.76 | 596 |
| 2024-09-20 22:21:39.842 | MS1 | 121.4656598707 | 31.1446299476 | 628 | 504990 | -91.10 | 11.63 | 78.38 | 0.59 | 2.78 | 670 |
| 2024-09-20 22:21:40.792 | MS1 | 121.4656591216 | 31.1446216337 | 628 | 504990 | -92.84 | 11.70 | 565.73 | 0.14 | 2.91 | 1587 |
| 2024-09-20 22:21:41.496 | MS1 | 121.4656642992 | 31.1446186552 | 628 | 504990 | -92.70 | 12.23 | 531.41 | 0.00 | 2.74 | 1597 |
| 2024-09-20 22:21:42.270 | MS1 | 121.4656661819 | 31.1446343928 | 628 | 504990 | -89.71 | 7.81 | 407.73 | 0.17 | 2.20 | 1595 |

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
| 3267895 | 2 | 121.4700494984 | 31.1518836874 | 202 | 0 | 9 | 48.8 | TDD | 628 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3267963 | 3 | 121.4661930331 | 31.1444613436 | 311 | 15 | 12 | 31.2 | TDD | 917 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3276106 | 1 | 121.4665908170 | 31.1522171460 | 180 | 2 | 3 | 48.3 | TDD | 218 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3279636 | 4 | 121.4658537184 | 31.1493202719 | 56 | 5 | 8 | 28.6 | TDD | 95 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.737 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.759 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.888 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.888 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.619 | NREventA3 | measId:2;ServCellPCI:277;Se... |
| 2024-09-20 22:21:37.859 | NRHandoverAttempt | SourcePCI:277;SourceNR-ARFC... |
| 2024-09-20 22:21:37.900 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.913 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.053 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.053 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276106 | 1 | 18.4121 | 10.2246 | -114.6906 | 5.7926 | 108.2665 | 0.0078 | 0.0032 |
| 2024_09_20 22:00 | 3267895 | 2 | 5.1793 | 6.5820 | -115.8006 | 18.2931 | 144.1307 | 0.0049 | 0.0118 |
| 2024_09_20 22:00 | 3267963 | 3 | 19.3962 | 7.6960 | -114.3648 | 19.6283 | 94.2464 | 0.0100 | 0.0130 |
| 2024_09_20 22:00 | 3279636 | 4 | 19.0775 | 10.1150 | -114.1197 | 8.6925 | 135.0492 | 0.0054 | 0.0143 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416262_84A41950 | 504990 | 628 | -89.8 | 504990 | 917 | -94.6 | 504990 | 218 | -102.9 | 504990 | 95 |
| MR_1774416262_2413A984 | 504990 | 628 | -90.3 | 504990 | 917 | -95.2 | 504990 | 218 | -102.7 | 504990 | 95 |
| MR_1774416262_2CC0709F | 504990 | 628 | -90.9 | 504990 | 917 | -96.1 | 504990 | 218 | -102.4 | 504990 | 95 |
| MR_1774416262_CA816C38 | 504990 | 628 | -91.2 | 504990 | 917 | -95.9 | 504990 | 218 | -104.7 | 504990 | 95 |
| MR_1774416262_68F824BB | 504990 | 628 | -92.1 | 504990 | 917 | -95.3 | 504990 | 218 | -102.7 | 504990 | 95 |
| MR_1774416262_47DD7EA3 | 504990 | 628 | -89.9 | 504990 | 917 | -98.5 | 504990 | 218 | -104.6 | 504990 | 95 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1593: `cf154c69-1a1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cf154c69-1a17-4f77-b610-9202485ef0b2` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3271186_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1593] topology](images/train_1593.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259576_4
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase A3 Offset threshold for 3259576_4
- `C4`: Increase transmission power for 3271186_2
- `C5`: Lift the tilt angle of 3271186_2 by 4 degrees
- `C6`: Decrease transmission power for 3271186_2
- `C7`: Add neighbor relationship between 3271186_2 and 3259576_4
- `C8`: Increase A3 Offset threshold for 3271186_2
- `C9`: Press down the tilt angle of 3271186_2 by 4 degrees
- `C10`: Adjust the azimuth of 3259576_4 by 50 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271186_2 **← 정답**
- `C12`: Increase transmission power for 3259576_4
- `C13`: Press down the tilt angle  of 3259576_4 by 8 degrees
- `C14`: Decrease A3 Offset threshold for 3271186_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271186_2
- `C16`: Lift the tilt angle  of 3259576_4 by 8 degrees
- `C17`: Decrease A3 Offset threshold for 3259576_4
- `C18`: Check test server and transmission issues
- `C19`: Decrease transmission power for 3259576_4
- `C20`: Adjust the azimuth of 3271186_2 by 18 degrees
- `C21`: Add neighbor relationship between 3263727_3 and 3259576_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259576_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.151 | MS1 | 121.4656622506 | 31.1446195467 | 835 | 504990 | -85.68 | 14.76 | 524.48 | 0.07 | 2.47 | 1564 |
| 2024-09-20 22:21:32.335 | MS1 | 121.4656663292 | 31.1446187753 | 835 | 504990 | -86.62 | 17.48 | 550.85 | 0.13 | 2.33 | 1590 |
| 2024-09-20 22:21:33.850 | MS1 | 121.4656630850 | 31.1446344227 | 835 | 504990 | -88.63 | 13.28 | 508.01 | 0.13 | 2.63 | 1583 |
| 2024-09-20 22:21:34.704 | MS1 | 121.4656765359 | 31.1446279152 | 835 | 504990 | -90.66 | 16.55 | 82.36 | 0.54 | 2.84 | 552 |
| 2024-09-20 22:21:35.694 | MS1 | 121.4656733894 | 31.1446191801 | 835 | 504990 | -91.25 | 14.37 | 69.88 | 0.55 | 2.29 | 699 |
| 2024-09-20 22:21:36.249 | MS1 | 121.4656703675 | 31.1446316418 | 835 | 504990 | -90.24 | 16.77 | 79.19 | 0.55 | 2.28 | 572 |
| 2024-09-20 22:21:37.166 | MS1 | 121.4656665203 | 31.1446310645 | 835 | 504990 | -89.30 | 9.38 | 81.51 | 0.56 | 2.09 | 530 |
| 2024-09-20 22:21:38.466 | MS1 | 121.4656612539 | 31.1446350558 | 835 | 504990 | -89.42 | 7.74 | 83.15 | 0.53 | 2.96 | 673 |
| 2024-09-20 22:21:39.794 | MS1 | 121.4656618547 | 31.1446305200 | 835 | 504990 | -90.58 | 11.42 | 75.05 | 0.53 | 2.16 | 577 |
| 2024-09-20 22:21:40.804 | MS1 | 121.4656685702 | 31.1446225738 | 835 | 504990 | -93.09 | 12.57 | 408.43 | 0.10 | 2.52 | 1583 |
| 2024-09-20 22:21:41.792 | MS1 | 121.4656733835 | 31.1446354300 | 835 | 504990 | -89.81 | 12.42 | 362.36 | 0.02 | 2.32 | 1586 |
| 2024-09-20 22:21:42.910 | MS1 | 121.4656773819 | 31.1446371987 | 835 | 504990 | -92.01 | 9.99 | 580.39 | 0.06 | 2.45 | 1587 |

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
| 3254052 | 1 | 121.4743396307 | 31.1442714137 | 149 | 2 | 5 | 44.5 | TDD | 315 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3259576 | 4 | 121.4688678706 | 31.1447386306 | 2 | 2 | 2 | 29.6 | TDD | 134 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3263727 | 3 | 121.4643034942 | 31.1465860648 | 266 | 4 | 10 | 37.4 | TDD | 291 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3271186 | 2 | 121.4742797663 | 31.1468043631 | 235 | 2 | 0 | 24.2 | TDD | 835 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.754 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.774 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.903 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.903 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.632 | NREventA3 | measId:2;ServCellPCI:596;Se... |
| 2024-09-20 22:21:37.872 | NRHandoverAttempt | SourcePCI:596;SourceNR-ARFC... |
| 2024-09-20 22:21:37.922 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.934 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.050 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.050 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254052 | 1 | 12.3339 | 19.3602 | -114.1258 | 12.5998 | 151.2134 | 0.0047 | 0.0103 |
| 2024_09_20 22:00 | 3271186 | 2 | 6.7184 | 8.0513 | -115.4538 | 7.2864 | 98.2205 | 0.0046 | 0.0011 |
| 2024_09_20 22:00 | 3263727 | 3 | 18.7377 | 8.0343 | -116.6114 | 6.6402 | 109.8155 | 0.0051 | 0.0115 |
| 2024_09_20 22:00 | 3259576 | 4 | 13.7837 | 16.6964 | -117.3466 | 17.6937 | 153.3130 | 0.0141 | 0.0200 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412241_E4B874C2 | 504990 | 835 | -90.9 | 504990 | 134 | -93.4 | 504990 | 291 | -105.8 | 504990 | 315 |
| MR_1774412241_9A3B59D6 | 504990 | 835 | -92.6 | 504990 | 134 | -90.9 | 504990 | 291 | -103.4 | 504990 | 315 |
| MR_1774412241_E750C57E | 504990 | 835 | -92.6 | 504990 | 134 | -90.9 | 504990 | 291 | -105.9 | 504990 | 315 |
| MR_1774412241_2B971858 | 504990 | 835 | -92.1 | 504990 | 134 | -92.5 | 504990 | 291 | -105.4 | 504990 | 315 |
| MR_1774412241_AA174D4E | 504990 | 835 | -91.4 | 504990 | 134 | -93.7 | 504990 | 291 | -105.1 | 504990 | 315 |
| MR_1774412241_255A0ABB | 504990 | 835 | -90.8 | 504990 | 134 | -92.3 | 504990 | 291 | -105.8 | 504990 | 315 |
| MR_1774412241_7B6F97FE | 504990 | 835 | -89.2 | 504990 | 134 | -92.2 | 504990 | 291 | -103.3 | 504990 | 315 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1594: `6b3ba005-13b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6b3ba005-13b5-4dd6-8732-1ad98fc4f5c5` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3226501_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1594] topology](images/train_1594.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3226501_1
- `C2`: Decrease A3 Offset threshold for 3226501_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227271_2
- `C4`: Press down the tilt angle of 3226501_1 by 5 degrees
- `C5`: Lift the tilt angle of 3226501_1 by 5 degrees
- `C6`: Increase transmission power for 3227271_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226501_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227271_2
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Press down the tilt angle  of 3227271_2 by 3 degrees
- `C11`: Check test server and transmission issues
- `C12`: Add neighbor relationship between 3217730_3 and 3227271_2
- `C13`: Decrease transmission power for 3226501_1
- `C14`: Increase A3 Offset threshold for 3227271_2
- `C15`: Lift the tilt angle  of 3227271_2 by 3 degrees
- `C16`: Adjust the azimuth of 3226501_1 by 18 degrees
- `C17`: Decrease transmission power for 3227271_2
- `C18`: Increase A3 Offset threshold for 3226501_1
- `C19`: Decrease A3 Offset threshold for 3227271_2
- `C20`: Adjust the azimuth of 3227271_2 by 50 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226501_1 **← 정답**
- `C22`: Add neighbor relationship between 3226501_1 and 3227271_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.383 | MS1 | 121.4656666225 | 31.1446265941 | 912 | 504990 | -88.08 | 17.78 | 425.74 | 0.04 | 2.79 | 1592 |
| 2024-09-20 22:21:32.704 | MS1 | 121.4656645531 | 31.1446261894 | 912 | 504990 | -91.61 | 15.13 | 446.05 | 0.19 | 2.68 | 1584 |
| 2024-09-20 22:21:33.541 | MS1 | 121.4656701465 | 31.1446355215 | 912 | 504990 | -90.74 | 13.39 | 391.37 | 0.07 | 2.21 | 1573 |
| 2024-09-20 22:21:34.824 | MS1 | 121.4656638425 | 31.1446197459 | 912 | 504990 | -85.27 | 14.53 | 66.75 | 0.68 | 2.88 | 673 |
| 2024-09-20 22:21:35.287 | MS1 | 121.4656706479 | 31.1446210685 | 912 | 504990 | -85.36 | 16.52 | 71.41 | 0.65 | 3.00 | 651 |
| 2024-09-20 22:21:36.963 | MS1 | 121.4656747818 | 31.1446270861 | 912 | 504990 | -88.48 | 16.91 | 97.36 | 0.65 | 2.88 | 565 |
| 2024-09-20 22:21:37.524 | MS1 | 121.4656755542 | 31.1446223935 | 912 | 504990 | -90.41 | 9.07 | 53.54 | 0.50 | 2.56 | 642 |
| 2024-09-20 22:21:38.427 | MS1 | 121.4656651852 | 31.1446180440 | 912 | 504990 | -89.86 | 12.87 | 94.27 | 0.55 | 2.36 | 693 |
| 2024-09-20 22:21:39.932 | MS1 | 121.4656768350 | 31.1446246571 | 912 | 504990 | -93.79 | 7.10 | 89.08 | 0.53 | 2.69 | 591 |
| 2024-09-20 22:21:40.597 | MS1 | 121.4656625951 | 31.1446338953 | 912 | 504990 | -89.69 | 11.38 | 364.07 | 0.17 | 2.06 | 1567 |
| 2024-09-20 22:21:41.880 | MS1 | 121.4656686494 | 31.1446259035 | 912 | 504990 | -91.26 | 11.97 | 395.99 | 0.03 | 2.15 | 1581 |
| 2024-09-20 22:21:42.599 | MS1 | 121.4656756235 | 31.1446226538 | 912 | 504990 | -92.90 | 10.14 | 586.28 | 0.07 | 2.94 | 1560 |

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
| 3217730 | 3 | 121.4720763562 | 31.1555575894 | 338 | 4 | 5 | 16.9 | TDD | 218 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3224841 | 4 | 121.4738455214 | 31.1506934320 | 137 | 5 | 1 | 24.5 | TDD | 743 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3226501 | 1 | 121.4753765353 | 31.1556651400 | 235 | 3 | 3 | 41.3 | TDD | 912 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3227271 | 2 | 121.4686658358 | 31.1557743194 | 60 | 1 | 10 | 41.0 | TDD | 89 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.371 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.387 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.509 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.509 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.175 | NREventA3 | measId:2;ServCellPCI:149;Se... |
| 2024-09-20 22:21:38.415 | NRHandoverAttempt | SourcePCI:149;SourceNR-ARFC... |
| 2024-09-20 22:21:38.448 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.460 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.591 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.591 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226501 | 1 | 16.3711 | 5.1208 | -116.1148 | 11.6678 | 114.0885 | 0.0051 | 0.0174 |
| 2024_09_20 22:00 | 3227271 | 2 | 11.6455 | 16.2867 | -114.9823 | 12.2666 | 89.2916 | 0.0028 | 0.0080 |
| 2024_09_20 22:00 | 3217730 | 3 | 17.0428 | 19.5513 | -115.4349 | 10.9331 | 174.1814 | 0.0123 | 0.0061 |
| 2024_09_20 22:00 | 3224841 | 4 | 10.4861 | 15.4536 | -116.9884 | 19.6055 | 101.4510 | 0.0025 | 0.0093 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414165_8FCC45D6 | 504990 | 912 | -86.3 | 504990 | 89 | -88.0 | 504990 | 218 | -93.6 | 504990 | 743 |
| MR_1774414165_B0A8E4A7 | 504990 | 912 | -83.5 | 504990 | 89 | -90.5 | 504990 | 218 | -92.4 | 504990 | 743 |
| MR_1774414165_8A201374 | 504990 | 912 | -83.9 | 504990 | 89 | -87.7 | 504990 | 218 | -92.8 | 504990 | 743 |
| MR_1774414165_FAB3B241 | 504990 | 912 | -83.6 | 504990 | 89 | -88.8 | 504990 | 218 | -94.8 | 504990 | 743 |
| MR_1774414165_F54BD771 | 504990 | 912 | -83.8 | 504990 | 89 | -89.5 | 504990 | 218 | -93.2 | 504990 | 743 |
| MR_1774414165_B4D16599 | 504990 | 912 | -86.1 | 504990 | 89 | -88.3 | 504990 | 218 | -95.9 | 504990 | 743 |
| MR_1774414165_78421561 | 504990 | 912 | -84.2 | 504990 | 89 | -88.8 | 504990 | 218 | -92.1 | 504990 | 743 |
| MR_1774414165_469C7335 | 504990 | 912 | -86.0 | 504990 | 89 | -89.9 | 504990 | 218 | -92.4 | 504990 | 743 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1595: `6100a0f7-cfc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6100a0f7-cfcc-4e19-b945-a63d19441fdd` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Lift the tilt angle  of 3216236_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1595] topology](images/train_1595.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease A3 Offset threshold for 3234605_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220002_2
- `C4`: Adjust the azimuth of 3234605_4 by 27 degrees
- `C5`: Adjust the azimuth of 3216236_3 by 50 degrees
- `C6`: Decrease transmission power for 3220002_2
- `C7`: Decrease A3 Offset threshold for 3220002_2
- `C8`: Increase A3 Offset threshold for 3220002_2
- `C9`: Increase A3 Offset threshold for 3234605_4
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Press down the tilt angle  of 3216236_3 by 10 degrees
- `C12`: Press down the tilt angle of 3234605_4 by 5 degrees
- `C13`: Add neighbor relationship between 3216236_3 and 3220002_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234605_4
- `C15`: Decrease transmission power for 3234605_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220002_2
- `C17`: Increase transmission power for 3220002_2
- `C18`: Lift the tilt angle of 3234605_4 by 5 degrees
- `C19`: Increase transmission power for 3234605_4
- `C20`: Lift the tilt angle  of 3216236_3 by 10 degrees **← 정답**
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234605_4
- `C22`: Add neighbor relationship between 3234605_4 and 3220002_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.993 | MS1 | 121.4656731446 | 31.1446191762 | 84 | 504990 | -91.41 | 14.20 | 374.01 | 0.20 | 2.14 | 1561 |
| 2024-09-20 22:21:32.381 | MS1 | 121.4656621836 | 31.1446194383 | 84 | 504990 | -90.03 | 16.74 | 461.48 | 0.13 | 2.00 | 1561 |
| 2024-09-20 22:21:33.292 | MS1 | 121.4656639045 | 31.1446265151 | 84 | 504990 | -86.17 | 14.21 | 299.83 | 0.14 | 2.49 | 1580 |
| 2024-09-20 22:21:34.106 | MS1 | 121.4656737587 | 31.1446214053 | 84 | 504990 | -89.06 | 13.38 | 97.94 | 0.15 | 2.07 | 1562 |
| 2024-09-20 22:21:35.842 | MS1 | 121.4656771751 | 31.1446224089 | 84 | 504990 | -85.44 | 15.40 | 103.93 | 0.16 | 2.53 | 1593 |
| 2024-09-20 22:21:36.965 | MS1 | 121.4656670631 | 31.1446262029 | 84 | 504990 | -88.98 | 14.45 | 77.21 | 0.18 | 2.62 | 1580 |
| 2024-09-20 22:21:37.528 | MS1 | 121.4656646255 | 31.1446186710 | 84 | 504990 | -93.43 | 10.87 | 80.80 | 0.00 | 2.61 | 1592 |
| 2024-09-20 22:21:38.598 | MS1 | 121.4656659788 | 31.1446284232 | 84 | 504990 | -93.37 | 9.18 | 77.49 | 0.18 | 2.65 | 1593 |
| 2024-09-20 22:21:39.339 | MS1 | 121.4656646082 | 31.1446185954 | 84 | 504990 | -93.21 | 8.78 | 56.45 | 0.12 | 2.89 | 1572 |
| 2024-09-20 22:21:40.938 | MS1 | 121.4656715961 | 31.1446319306 | 84 | 504990 | -92.89 | 8.59 | 404.41 | 0.04 | 2.78 | 1563 |
| 2024-09-20 22:21:41.244 | MS1 | 121.4656651346 | 31.1446267493 | 84 | 504990 | -91.92 | 11.77 | 566.41 | 0.05 | 2.52 | 1565 |
| 2024-09-20 22:21:42.369 | MS1 | 121.4656746176 | 31.1446240524 | 84 | 504990 | -89.69 | 7.55 | 403.32 | 0.15 | 2.65 | 1589 |

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
| 3216236 | 3 | 121.4662280030 | 31.1513917784 | 41 | 7 | 1 | 37.8 | TDD | 22 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3220002 | 2 | 121.4703340933 | 31.1487519925 | 310 | 9 | 9 | 39.1 | TDD | 845 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3234605 | 4 | 121.4692370800 | 31.1497322933 | 184 | 3 | 11 | 19.7 | TDD | 84 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3251096 | 1 | 121.4756413353 | 31.1513351290 | 74 | 10 | 5 | 35.5 | TDD | 708 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.931 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.953 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.088 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.088 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.806 | NREventA3 | measId:2;ServCellPCI:738;Se... |
| 2024-09-20 22:21:38.046 | NRHandoverAttempt | SourcePCI:738;SourceNR-ARFC... |
| 2024-09-20 22:21:38.081 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.096 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.204 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.204 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251096 | 1 | 10.1104 | 18.7297 | -114.2581 | 14.5196 | 134.8219 | 0.0110 | 0.0064 |
| 2024_09_20 22:00 | 3220002 | 2 | 15.8324 | 10.9540 | -117.4138 | 15.2799 | 163.3850 | 0.0141 | 0.0050 |
| 2024_09_20 22:00 | 3216236 | 3 | 14.1405 | 7.2620 | -115.6762 | 6.9818 | 122.7946 | 0.0131 | 0.0123 |
| 2024_09_20 22:00 | 3234605 | 4 | 91.3580 | 75.6508 | -115.6533 | 13.9949 | 198.1058 | 0.0052 | 0.0026 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414560_62DD8774 | 504990 | 84 | -89.0 | 504990 | 845 | -92.2 | 504990 | 22 | -103.2 | 504990 | 708 |
| MR_1774414560_1A93181E | 504990 | 84 | -87.4 | 504990 | 845 | -88.9 | 504990 | 22 | -99.6 | 504990 | 708 |
| MR_1774414560_290D721A | 504990 | 84 | -88.6 | 504990 | 845 | -91.5 | 504990 | 22 | -99.8 | 504990 | 708 |
| MR_1774414560_0FFB50F3 | 504990 | 84 | -89.6 | 504990 | 845 | -91.5 | 504990 | 22 | -102.0 | 504990 | 708 |
| MR_1774414560_C473BC40 | 504990 | 84 | -90.2 | 504990 | 845 | -89.5 | 504990 | 22 | -99.9 | 504990 | 708 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1596: `31b432f3-bb1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `31b432f3-bb1f-40c3-b065-c581bca2b822` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266754_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1596] topology](images/train_1596.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3233700_2
- `C2`: Add neighbor relationship between 3231376_12 and 3233700_2
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase transmission power for 3266754_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266754_1
- `C6`: Increase transmission power for 3233700_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266754_1 **← 정답**
- `C8`: Adjust the azimuth of 3233700_2 by 31 degrees
- `C9`: Decrease transmission power for 3233700_2
- `C10`: Increase A3 Offset threshold for 3266754_1
- `C11`: Check test server and transmission issues
- `C12`: Lift the tilt angle  of 3233700_2 by 2 degrees
- `C13`: Decrease transmission power for 3266754_1
- `C14`: Decrease A3 Offset threshold for 3233700_2
- `C15`: Add neighbor relationship between 3266754_1 and 3233700_2
- `C16`: Adjust the azimuth of 3266754_1 by 24 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233700_2
- `C18`: Lift the tilt angle of 3266754_1 by 3 degrees
- `C19`: Decrease A3 Offset threshold for 3266754_1
- `C20`: Press down the tilt angle  of 3233700_2 by 2 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233700_2
- `C22`: Press down the tilt angle of 3266754_1 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.254 | MS1 | 121.4656778582 | 31.1446272928 | 929 | 504990 | -94.30 | 14.30 | 468.23 | 0.19 | 2.34 | 1561 |
| 2024-09-20 22:21:32.252 | MS1 | 121.4656689025 | 31.1446268963 | 794 | 504990 | -94.62 | 9.22 | 533.85 | 0.12 | 2.39 | 1586 |
| 2024-09-20 22:21:33.413 | MS1 | 121.4656601172 | 31.1446273021 | 537 | 504990 | -93.53 | 12.23 | 409.04 | 0.01 | 2.39 | 1597 |
| 2024-09-20 22:21:34.567 | MS1 | 121.4656671739 | 31.1446304600 | 102 | 152650 | -88.36 | 6.99 | 102.76 | 0.07 | 1.69 | 992 |
| 2024-09-20 22:21:35.972 | MS1 | 121.4656761473 | 31.1446293912 | 441 | 152650 | -91.62 | 5.76 | 61.45 | 0.04 | 1.56 | 962 |
| 2024-09-20 22:21:36.666 | MS1 | 121.4656731108 | 31.1446217738 | 821 | 152650 | -88.59 | 5.85 | 92.74 | 0.15 | 1.58 | 992 |
| 2024-09-20 22:21:37.208 | MS1 | 121.4656590344 | 31.1446321458 | 784 | 152650 | -90.42 | 2.75 | 100.25 | 0.07 | 1.59 | 983 |
| 2024-09-20 22:21:38.388 | MS1 | 121.4656642505 | 31.1446262081 | 102 | 152650 | -88.58 | 5.69 | 53.24 | 0.07 | 1.58 | 916 |
| 2024-09-20 22:21:39.275 | MS1 | 121.4656728908 | 31.1446312225 | 441 | 152650 | -93.65 | 4.17 | 59.07 | 0.09 | 1.87 | 993 |
| 2024-09-20 22:21:40.119 | MS1 | 121.4656725302 | 31.1446355182 | 821 | 152650 | -88.56 | 5.31 | 59.37 | 0.17 | 2.80 | 1577 |
| 2024-09-20 22:21:41.151 | MS1 | 121.4656580392 | 31.1446245283 | 784 | 152650 | -93.65 | 2.29 | 79.74 | 0.06 | 2.74 | 1575 |
| 2024-09-20 22:21:42.850 | MS1 | 121.4656672472 | 31.1446270704 | 102 | 152650 | -87.58 | 5.63 | 51.63 | 0.12 | 2.93 | 1574 |

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
| 3217517 | 7 | 121.4656636485 | 31.1548844897 | 297 | 10 | 3 | 17.5 | FDD | 102 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3225883 | 11 | 121.4642554898 | 31.1475819259 | 263 | 12 | 1 | 19.4 | FDD | 784 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3229799 | 8 | 121.4702540863 | 31.1440061595 | 256 | 12 | 2 | 18.0 | FDD | 870 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3231376 | 12 | 121.4659354335 | 31.1466667262 | 107 | 10 | 11 | 17.6 | FDD | 821 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3232050 | 13 | 121.4651836589 | 31.1550628486 | 295 | 6 | 8 | 8.2 | FDD | 441 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3233700 | 2 | 121.4743354940 | 31.1449287228 | 237 | 1 | 4 | 13.3 | TDD | 686 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3237099 | 3 | 121.4707156094 | 31.1524778270 | 273 | 2 | 11 | 14.4 | TDD | 21 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3254207 | 5 | 121.4689980220 | 31.1508701531 | 13 | 14 | 6 | 8.5 | TDD | 537 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3266754 | 1 | 121.4726525494 | 31.1504400977 | 250 | 1 | 7 | 25.4 | TDD | 929 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3267459 | 4 | 121.4686206277 | 31.1498615058 | 121 | 3 | 4 | 15.7 | TDD | 118 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3268499 | 10 | 121.4730863055 | 31.1522566609 | 173 | 5 | 10 | 24.3 | FDD | 201 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3274302 | 9 | 121.4690838129 | 31.1444124292 | 50 | 12 | 8 | 2.5 | FDD | 200 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3275571 | 6 | 121.4734497319 | 31.1444605408 | 283 | 5 | 6 | 28.3 | TDD | 794 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.878 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.903 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.026 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.026 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.766 | NREventA2 | measId:1;ServCellPCI:1007;S... |
| 2024-09-20 22:21:34.874 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.174 | NREventA5 | measId:3;ServCellPCI:1007;S... |
| 2024-09-20 22:21:35.233 | NRHandoverAttempt | SourcePCI:1007;SourceNR-ARF... |
| 2024-09-20 22:21:35.278 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.288 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.405 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.405 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266754 | 1 | 13.6215 | 14.0626 | -114.4441 | 15.3868 | 99.7114 | 0.0067 | 0.0121 |
| 2024_09_20 22:00 | 3233700 | 2 | 18.5003 | 11.2080 | -117.8263 | 18.8143 | 96.0565 | 0.0079 | 0.0055 |
| 2024_09_20 22:00 | 3237099 | 3 | 5.4869 | 16.4303 | -115.3495 | 16.7548 | 85.0630 | 0.0075 | 0.0108 |
| 2024_09_20 22:00 | 3267459 | 4 | 8.2949 | 13.3397 | -115.9437 | 10.1544 | 104.0823 | 0.0060 | 0.0008 |
| 2024_09_20 22:00 | 3254207 | 5 | 9.6091 | 7.7560 | -115.8974 | 11.3209 | 131.0648 | 0.0112 | 0.0189 |
| 2024_09_20 22:00 | 3275571 | 6 | 5.1394 | 12.4805 | -117.1469 | 6.5864 | 117.5512 | 0.0105 | 0.0161 |
| 2024_09_20 22:00 | 3217517 | 7 | 18.4898 | 13.7004 | -114.6207 | 4.8584 | 25.2695 | 0.0187 | 0.0198 |
| 2024_09_20 22:00 | 3229799 | 8 | 16.9446 | 18.5595 | -115.3117 | 4.0972 | 27.4374 | 0.0039 | 0.0109 |
| 2024_09_20 22:00 | 3274302 | 9 | 19.3132 | 8.5674 | -115.5079 | 3.6471 | 39.3896 | 0.0024 | 0.0052 |
| 2024_09_20 22:00 | 3268499 | 10 | 8.9671 | 10.3010 | -115.8467 | 4.6869 | 25.4999 | 0.0189 | 0.0090 |
| 2024_09_20 22:00 | 3225883 | 11 | 18.3952 | 12.9776 | -117.0346 | 3.0566 | 28.2256 | 0.0196 | 0.0015 |
| 2024_09_20 22:00 | 3231376 | 12 | 8.1770 | 6.0205 | -117.5778 | 3.1729 | 48.1805 | 0.0075 | 0.0113 |
| 2024_09_20 22:00 | 3232050 | 13 | 5.9731 | 6.7363 | -116.1371 | 3.9685 | 24.3841 | 0.0031 | 0.0031 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412307_C34442AD | 152650 | 441 | -90.7 | 152650 | 201 | -95.3 | 152650 | 200 | -102.8 | 152650 | 870 |
| MR_1774412307_8E90C4C7 | 152650 | 441 | -91.4 | 152650 | 201 | -93.2 | 152650 | 200 | -102.5 | 152650 | 870 |
| MR_1774412307_18769371 | 152650 | 441 | -93.0 | 152650 | 201 | -95.0 | 152650 | 200 | -102.3 | 152650 | 870 |
| MR_1774412307_84B887E5 | 152650 | 441 | -92.3 | 152650 | 201 | -94.4 | 152650 | 200 | -101.1 | 152650 | 870 |
| MR_1774412307_1BB06E8D | 504990 | 537 | -94.4 | 504990 | 686 | -92.1 | 504990 | 21 | -99.1 | 504990 | 118 |
| MR_1774412307_AE568E77 | 152650 | 441 | -92.5 | 152650 | 201 | -95.3 | 152650 | 200 | -103.9 | 152650 | 870 |
| MR_1774412307_BAB12080 | 504990 | 537 | -95.1 | 504990 | 686 | -91.6 | 504990 | 21 | -100.4 | 504990 | 118 |
| MR_1774412307_3D09A012 | 152650 | 441 | -90.2 | 152650 | 201 | -95.2 | 152650 | 200 | -103.2 | 152650 | 870 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1597: `2643a7b3-62c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2643a7b3-62c2-4ca4-8b3c-23e7a2efa07a` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Lift the tilt angle  of 3258466_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1597] topology](images/train_1597.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Increase A3 Offset threshold for 3225467_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266172_1
- `C4`: Adjust the azimuth of 3266172_1 by 48 degrees
- `C5`: Add neighbor relationship between 3266172_1 and 3225467_4
- `C6`: Press down the tilt angle of 3266172_1 by 3 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225467_4
- `C8`: Add neighbor relationship between 3258466_3 and 3225467_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266172_1
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase transmission power for 3225467_4
- `C12`: Decrease transmission power for 3266172_1
- `C13`: Decrease A3 Offset threshold for 3225467_4
- `C14`: Lift the tilt angle of 3266172_1 by 3 degrees
- `C15`: Decrease transmission power for 3225467_4
- `C16`: Increase A3 Offset threshold for 3266172_1
- `C17`: Lift the tilt angle  of 3258466_3 by 10 degrees **← 정답**
- `C18`: Press down the tilt angle  of 3258466_3 by 10 degrees
- `C19`: Increase transmission power for 3266172_1
- `C20`: Adjust the azimuth of 3258466_3 by 50 degrees
- `C21`: Decrease A3 Offset threshold for 3266172_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225467_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.754 | MS1 | 121.4656620557 | 31.1446318974 | 40 | 504990 | -89.89 | 16.63 | 314.92 | 0.15 | 2.97 | 1582 |
| 2024-09-20 22:21:32.159 | MS1 | 121.4656608653 | 31.1446335553 | 40 | 504990 | -87.14 | 15.71 | 538.70 | 0.02 | 2.29 | 1594 |
| 2024-09-20 22:21:33.267 | MS1 | 121.4656595365 | 31.1446295500 | 40 | 504990 | -86.51 | 14.77 | 439.70 | 0.07 | 2.53 | 1576 |
| 2024-09-20 22:21:34.691 | MS1 | 121.4656672358 | 31.1446325195 | 40 | 504990 | -90.70 | 13.53 | 69.23 | 0.10 | 2.15 | 1565 |
| 2024-09-20 22:21:35.266 | MS1 | 121.4656691687 | 31.1446236042 | 40 | 504990 | -90.35 | 12.81 | 56.70 | 0.17 | 2.46 | 1581 |
| 2024-09-20 22:21:36.225 | MS1 | 121.4656680879 | 31.1446211030 | 40 | 504990 | -87.74 | 13.26 | 55.44 | 0.10 | 2.19 | 1590 |
| 2024-09-20 22:21:37.453 | MS1 | 121.4656634024 | 31.1446212578 | 40 | 504990 | -91.54 | 11.17 | 97.49 | 0.15 | 2.58 | 1573 |
| 2024-09-20 22:21:38.105 | MS1 | 121.4656727339 | 31.1446261588 | 40 | 504990 | -91.50 | 11.62 | 81.94 | 0.11 | 2.56 | 1589 |
| 2024-09-20 22:21:39.544 | MS1 | 121.4656747431 | 31.1446316874 | 40 | 504990 | -89.71 | 7.11 | 95.23 | 0.12 | 2.24 | 1591 |
| 2024-09-20 22:21:40.774 | MS1 | 121.4656598058 | 31.1446297744 | 40 | 504990 | -92.56 | 7.74 | 511.21 | 0.14 | 2.64 | 1570 |
| 2024-09-20 22:21:41.986 | MS1 | 121.4656759404 | 31.1446190659 | 40 | 504990 | -90.74 | 9.07 | 535.17 | 0.10 | 2.93 | 1590 |
| 2024-09-20 22:21:42.646 | MS1 | 121.4656634207 | 31.1446333889 | 40 | 504990 | -93.42 | 12.17 | 552.93 | 0.05 | 2.23 | 1580 |

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
| 3225467 | 4 | 121.4688186924 | 31.1537314696 | 265 | 13 | 3 | 44.4 | TDD | 688 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3258466 | 3 | 121.4657821926 | 31.1463327659 | 94 | 5 | 12 | 48.1 | TDD | 837 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3266172 | 1 | 121.4673760722 | 31.1533631326 | 237 | 1 | 2 | 42.5 | TDD | 40 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3275123 | 2 | 121.4645336077 | 31.1472319884 | 112 | 13 | 8 | 43.6 | TDD | 857 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.082 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.102 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.208 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.208 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.968 | NREventA3 | measId:2;ServCellPCI:372;Se... |
| 2024-09-20 22:21:38.208 | NRHandoverAttempt | SourcePCI:372;SourceNR-ARFC... |
| 2024-09-20 22:21:38.248 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.260 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.362 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.362 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266172 | 1 | 82.7132 | 86.9950 | -116.2154 | 15.3555 | 188.0383 | 0.0114 | 0.0038 |
| 2024_09_20 22:00 | 3275123 | 2 | 15.1413 | 7.0728 | -117.5676 | 19.7821 | 150.8121 | 0.0038 | 0.0088 |
| 2024_09_20 22:00 | 3258466 | 3 | 13.8797 | 10.0309 | -117.8070 | 6.7587 | 136.6586 | 0.0157 | 0.0103 |
| 2024_09_20 22:00 | 3225467 | 4 | 7.7724 | 16.4417 | -114.4812 | 13.0897 | 179.7052 | 0.0036 | 0.0109 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415131_7BEDD18A | 504990 | 40 | -91.3 | 504990 | 688 | -89.8 | 504990 | 837 | -96.3 | 504990 | 857 |
| MR_1774415131_68E611DA | 504990 | 40 | -89.8 | 504990 | 688 | -90.1 | 504990 | 837 | -95.6 | 504990 | 857 |
| MR_1774415131_4025738E | 504990 | 40 | -92.6 | 504990 | 688 | -92.4 | 504990 | 837 | -97.2 | 504990 | 857 |
| MR_1774415131_74F282FE | 504990 | 40 | -89.3 | 504990 | 688 | -90.4 | 504990 | 837 | -96.0 | 504990 | 857 |
| MR_1774415131_C9C4B661 | 504990 | 40 | -91.5 | 504990 | 688 | -92.6 | 504990 | 837 | -95.2 | 504990 | 857 |
| MR_1774415131_8A476276 | 504990 | 40 | -89.5 | 504990 | 688 | -91.8 | 504990 | 837 | -95.5 | 504990 | 857 |
| MR_1774415131_0CE0EEF2 | 504990 | 40 | -89.6 | 504990 | 688 | -89.7 | 504990 | 837 | -98.4 | 504990 | 857 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1598: `5eaa2668-6d2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5eaa2668-6d2f-45b7-ac1c-e1e9d63bc460` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272720_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1598] topology](images/train_1598.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3272720_2 by 23 degrees
- `C2`: Press down the tilt angle  of 3227677_5 by 3 degrees
- `C3`: Increase transmission power for 3272720_2
- `C4`: Add neighbor relationship between 3232844_7 and 3227677_5
- `C5`: Decrease transmission power for 3227677_5
- `C6`: Adjust the azimuth of 3227677_5 by 47 degrees
- `C7`: Check test server and transmission issues
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272720_2
- `C9`: Decrease A3 Offset threshold for 3272720_2
- `C10`: Increase A3 Offset threshold for 3227677_5
- `C11`: Increase A3 Offset threshold for 3272720_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227677_5
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Press down the tilt angle of 3272720_2 by 3 degrees
- `C15`: Lift the tilt angle of 3272720_2 by 3 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272720_2 **← 정답**
- `C17`: Lift the tilt angle  of 3227677_5 by 3 degrees
- `C18`: Add neighbor relationship between 3272720_2 and 3227677_5
- `C19`: Decrease A3 Offset threshold for 3227677_5
- `C20`: Increase transmission power for 3227677_5
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227677_5
- `C22`: Decrease transmission power for 3272720_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.242 | MS1 | 121.4656691368 | 31.1446265629 | 770 | 504990 | -94.74 | 11.31 | 428.51 | 0.11 | 2.86 | 1591 |
| 2024-09-20 22:21:32.985 | MS1 | 121.4656696488 | 31.1446234663 | 512 | 504990 | -93.75 | 13.86 | 346.11 | 0.12 | 2.39 | 1591 |
| 2024-09-20 22:21:33.293 | MS1 | 121.4656608286 | 31.1446340328 | 557 | 504990 | -94.05 | 10.74 | 306.86 | 0.07 | 2.36 | 1588 |
| 2024-09-20 22:21:34.138 | MS1 | 121.4656724721 | 31.1446370604 | 181 | 152650 | -93.84 | 5.72 | 84.11 | 0.12 | 1.50 | 999 |
| 2024-09-20 22:21:35.680 | MS1 | 121.4656665324 | 31.1446256837 | 286 | 152650 | -87.99 | 6.67 | 96.63 | 0.13 | 1.70 | 999 |
| 2024-09-20 22:21:36.751 | MS1 | 121.4656765723 | 31.1446190186 | 228 | 152650 | -91.02 | 3.39 | 89.44 | 0.16 | 1.86 | 966 |
| 2024-09-20 22:21:37.351 | MS1 | 121.4656673709 | 31.1446281904 | 398 | 152650 | -93.87 | 6.80 | 80.95 | 0.12 | 1.69 | 991 |
| 2024-09-20 22:21:38.188 | MS1 | 121.4656604634 | 31.1446210685 | 181 | 152650 | -92.25 | 4.28 | 65.95 | 0.02 | 1.78 | 946 |
| 2024-09-20 22:21:39.402 | MS1 | 121.4656646824 | 31.1446350125 | 286 | 152650 | -87.62 | 5.81 | 58.33 | 0.10 | 1.96 | 947 |
| 2024-09-20 22:21:40.294 | MS1 | 121.4656735132 | 31.1446294848 | 228 | 152650 | -88.88 | 6.86 | 66.75 | 0.13 | 2.89 | 1593 |
| 2024-09-20 22:21:41.901 | MS1 | 121.4656644057 | 31.1446212915 | 398 | 152650 | -89.50 | 2.79 | 50.48 | 0.13 | 2.49 | 1572 |
| 2024-09-20 22:21:42.364 | MS1 | 121.4656674315 | 31.1446302707 | 181 | 152650 | -95.38 | 4.55 | 86.99 | 0.18 | 2.94 | 1561 |

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
| 3216013 | 8 | 121.4697392918 | 31.1527154033 | 5 | 2 | 10 | 16.2 | FDD | 638 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3219365 | 1 | 121.4727455603 | 31.1549417851 | 0 | 10 | 8 | 0.2 | TDD | 512 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3227677 | 5 | 121.4759361568 | 31.1520053860 | 183 | 3 | 1 | 4.0 | TDD | 888 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3231565 | 9 | 121.4725818528 | 31.1502787981 | 336 | 15 | 9 | 26.5 | FDD | 398 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3232844 | 7 | 121.4671496653 | 31.1494005573 | 211 | 3 | 0 | 22.0 | FDD | 228 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3234788 | 4 | 121.4640846480 | 31.1479735688 | 141 | 4 | 5 | 8.0 | TDD | 821 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3252203 | 11 | 121.4747659247 | 31.1463511599 | 40 | 3 | 10 | 6.0 | FDD | 726 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3259337 | 12 | 121.4701581863 | 31.1458976245 | 222 | 0 | 8 | 25.8 | FDD | 126 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3265165 | 10 | 121.4642309781 | 31.1501956413 | 310 | 10 | 4 | 26.8 | FDD | 181 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3267308 | 3 | 121.4735390882 | 31.1552470624 | 131 | 2 | 3 | 26.6 | TDD | 557 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3272720 | 2 | 121.4645786382 | 31.1466214343 | 132 | 1 | 9 | 9.6 | TDD | 770 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3272860 | 13 | 121.4750205857 | 31.1488610901 | 294 | 4 | 7 | 20.2 | FDD | 286 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3273061 | 6 | 121.4727846507 | 31.1479207148 | 261 | 10 | 11 | 29.5 | TDD | 765 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.814 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.837 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.954 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.954 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.647 | NREventA2 | measId:1;ServCellPCI:765;Se... |
| 2024-09-20 22:21:34.785 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.079 | NREventA5 | measId:3;ServCellPCI:765;Se... |
| 2024-09-20 22:21:35.135 | NRHandoverAttempt | SourcePCI:765;SourceNR-ARFC... |
| 2024-09-20 22:21:35.181 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.195 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.314 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.314 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219365 | 1 | 5.4359 | 8.1529 | -115.5661 | 15.5307 | 154.1391 | 0.0092 | 0.0182 |
| 2024_09_20 22:00 | 3272720 | 2 | 12.7307 | 13.7809 | -116.6589 | 13.2922 | 125.1672 | 0.0154 | 0.0127 |
| 2024_09_20 22:00 | 3267308 | 3 | 17.4647 | 17.4597 | -114.2114 | 10.1956 | 141.4415 | 0.0014 | 0.0043 |
| 2024_09_20 22:00 | 3234788 | 4 | 5.4579 | 5.3303 | -115.5808 | 9.2927 | 150.8345 | 0.0091 | 0.0192 |
| 2024_09_20 22:00 | 3227677 | 5 | 5.1190 | 10.6851 | -114.6838 | 11.5639 | 158.5189 | 0.0009 | 0.0161 |
| 2024_09_20 22:00 | 3273061 | 6 | 9.8221 | 18.9856 | -114.3343 | 13.7696 | 147.9764 | 0.0001 | 0.0154 |
| 2024_09_20 22:00 | 3232844 | 7 | 14.6221 | 15.1541 | -117.3360 | 3.8681 | 24.8752 | 0.0170 | 0.0016 |
| 2024_09_20 22:00 | 3216013 | 8 | 6.8542 | 5.9584 | -114.9995 | 3.7151 | 57.3230 | 0.0053 | 0.0168 |
| 2024_09_20 22:00 | 3231565 | 9 | 8.7290 | 8.7473 | -117.7243 | 3.3535 | 43.2101 | 0.0128 | 0.0191 |
| 2024_09_20 22:00 | 3265165 | 10 | 17.5034 | 12.0767 | -115.2152 | 4.3914 | 21.9497 | 0.0124 | 0.0107 |
| 2024_09_20 22:00 | 3252203 | 11 | 9.3031 | 13.2791 | -115.4510 | 3.3905 | 51.7084 | 0.0069 | 0.0143 |
| 2024_09_20 22:00 | 3259337 | 12 | 14.0536 | 13.2232 | -114.8295 | 3.2139 | 28.6498 | 0.0025 | 0.0020 |
| 2024_09_20 22:00 | 3272860 | 13 | 5.9875 | 9.6899 | -114.8836 | 3.5591 | 37.5354 | 0.0174 | 0.0114 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415819_E769634F | 504990 | 557 | -95.0 | 504990 | 888 | -89.8 | 504990 | 765 | -101.3 | 504990 | 821 |
| MR_1774415819_7F638791 | 152650 | 181 | -92.0 | 152650 | 726 | -98.9 | 152650 | 126 | -106.1 | 152650 | 638 |
| MR_1774415819_FBDA7C17 | 152650 | 181 | -93.0 | 152650 | 726 | -102.1 | 152650 | 126 | -104.4 | 152650 | 638 |
| MR_1774415819_C4BBA06C | 152650 | 181 | -94.7 | 152650 | 726 | -102.4 | 152650 | 126 | -103.1 | 152650 | 638 |
| MR_1774415819_80679566 | 504990 | 557 | -94.4 | 504990 | 888 | -90.5 | 504990 | 765 | -103.0 | 504990 | 821 |
| MR_1774415819_24B780A4 | 504990 | 557 | -94.8 | 504990 | 888 | -87.9 | 504990 | 765 | -102.6 | 504990 | 821 |
| MR_1774415819_C53E4CF2 | 504990 | 557 | -94.6 | 504990 | 888 | -89.6 | 504990 | 765 | -102.6 | 504990 | 821 |
| MR_1774415819_C12F8DDD | 152650 | 181 | -93.6 | 152650 | 726 | -101.6 | 152650 | 126 | -104.6 | 152650 | 638 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1599: `9bd1cfd8-eb3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9bd1cfd8-eb39-47d8-bb3c-b7583846c4c0` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Lift the tilt angle  of 3235874_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1599] topology](images/train_1599.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3273416_2
- `C2`: Adjust the azimuth of 3235874_1 by 50 degrees
- `C3`: Check test server and transmission issues
- `C4`: Decrease A3 Offset threshold for 3273416_2
- `C5`: Increase transmission power for 3238818_4
- `C6`: Press down the tilt angle  of 3235874_1 by 10 degrees
- `C7`: Increase A3 Offset threshold for 3238818_4
- `C8`: Decrease transmission power for 3273416_2
- `C9`: Decrease transmission power for 3238818_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238818_4
- `C11`: Press down the tilt angle of 3238818_4 by 5 degrees
- `C12`: Add neighbor relationship between 3238818_4 and 3273416_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273416_2
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238818_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273416_2
- `C17`: Lift the tilt angle  of 3235874_1 by 10 degrees **← 정답**
- `C18`: Lift the tilt angle of 3238818_4 by 5 degrees
- `C19`: Increase transmission power for 3273416_2
- `C20`: Decrease A3 Offset threshold for 3238818_4
- `C21`: Add neighbor relationship between 3235874_1 and 3273416_2
- `C22`: Adjust the azimuth of 3238818_4 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.396 | MS1 | 121.4656718926 | 31.1446249110 | 507 | 504990 | -87.56 | 15.96 | 387.80 | 0.07 | 2.19 | 1565 |
| 2024-09-20 22:21:32.918 | MS1 | 121.4656659962 | 31.1446264754 | 507 | 504990 | -85.82 | 15.58 | 406.39 | 0.03 | 2.37 | 1581 |
| 2024-09-20 22:21:33.341 | MS1 | 121.4656766829 | 31.1446276916 | 507 | 504990 | -91.95 | 15.51 | 495.11 | 0.10 | 2.63 | 1585 |
| 2024-09-20 22:21:34.210 | MS1 | 121.4656714453 | 31.1446277352 | 507 | 504990 | -85.34 | 14.33 | 68.61 | 0.14 | 2.99 | 1568 |
| 2024-09-20 22:21:35.233 | MS1 | 121.4656638333 | 31.1446341279 | 507 | 504990 | -91.75 | 15.44 | 77.71 | 0.17 | 2.71 | 1568 |
| 2024-09-20 22:21:36.624 | MS1 | 121.4656627963 | 31.1446317794 | 507 | 504990 | -87.24 | 15.38 | 58.57 | 0.08 | 2.10 | 1588 |
| 2024-09-20 22:21:37.677 | MS1 | 121.4656661107 | 31.1446304605 | 507 | 504990 | -90.21 | 8.64 | 89.44 | 0.09 | 2.66 | 1573 |
| 2024-09-20 22:21:38.237 | MS1 | 121.4656778703 | 31.1446330336 | 507 | 504990 | -89.06 | 8.31 | 75.28 | 0.08 | 2.17 | 1584 |
| 2024-09-20 22:21:39.743 | MS1 | 121.4656650155 | 31.1446257378 | 507 | 504990 | -89.51 | 9.59 | 54.27 | 0.06 | 2.33 | 1597 |
| 2024-09-20 22:21:40.300 | MS1 | 121.4656625887 | 31.1446263202 | 507 | 504990 | -93.52 | 7.19 | 532.37 | 0.08 | 2.72 | 1587 |
| 2024-09-20 22:21:41.471 | MS1 | 121.4656680198 | 31.1446284609 | 507 | 504990 | -89.21 | 8.31 | 300.00 | 0.14 | 2.88 | 1581 |
| 2024-09-20 22:21:42.181 | MS1 | 121.4656734930 | 31.1446343509 | 507 | 504990 | -90.41 | 9.42 | 318.40 | 0.17 | 2.99 | 1575 |

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
| 3215010 | 3 | 121.4665142571 | 31.1540323865 | 246 | 1 | 0 | 46.3 | TDD | 801 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3235874 | 1 | 121.4648659283 | 31.1540086967 | 328 | 7 | 3 | 37.0 | TDD | 161 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3238818 | 4 | 121.4653216686 | 31.1522282596 | 175 | 2 | 0 | 47.8 | TDD | 507 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3273416 | 2 | 121.4695956166 | 31.1553933271 | 271 | 10 | 3 | 23.4 | TDD | 43 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.803 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.821 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.944 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.944 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.652 | NREventA3 | measId:2;ServCellPCI:677;Se... |
| 2024-09-20 22:21:37.892 | NRHandoverAttempt | SourcePCI:677;SourceNR-ARFC... |
| 2024-09-20 22:21:37.937 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.952 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.083 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.083 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235874 | 1 | 10.1863 | 13.9063 | -114.8851 | 19.6473 | 106.7167 | 0.0133 | 0.0085 |
| 2024_09_20 22:00 | 3273416 | 2 | 7.1047 | 15.7037 | -114.6340 | 19.0954 | 106.9312 | 0.0005 | 0.0097 |
| 2024_09_20 22:00 | 3215010 | 3 | 7.9684 | 17.7902 | -115.2013 | 18.0587 | 130.5604 | 0.0010 | 0.0119 |
| 2024_09_20 22:00 | 3238818 | 4 | 75.0024 | 87.8454 | -114.7392 | 13.2994 | 104.3842 | 0.0050 | 0.0102 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414740_11CD2936 | 504990 | 507 | -86.0 | 504990 | 43 | -93.8 | 504990 | 161 | -93.7 | 504990 | 801 |
| MR_1774414740_7CE9F605 | 504990 | 507 | -83.5 | 504990 | 43 | -93.8 | 504990 | 161 | -92.4 | 504990 | 801 |
| MR_1774414740_D1BA3293 | 504990 | 507 | -85.7 | 504990 | 43 | -92.0 | 504990 | 161 | -91.9 | 504990 | 801 |
| MR_1774414740_6840482B | 504990 | 507 | -86.7 | 504990 | 43 | -91.6 | 504990 | 161 | -93.8 | 504990 | 801 |
| MR_1774414740_DE18BBC7 | 504990 | 507 | -84.1 | 504990 | 43 | -92.7 | 504990 | 161 | -92.5 | 504990 | 801 |

> *... 2개 열 생략 (전체 14열)*

---
