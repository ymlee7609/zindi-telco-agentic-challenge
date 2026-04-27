# Track A 문제 분석 — train[1500]~train[1509]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1500] ~ train[1509] (10개)

## 목차

1. [문제 1500: `77c8c216-4ad...`](#1500) — single-answer, 정답: C18
2. [문제 1501: `47a85f94-15c...`](#1501) — multiple-answer, 정답: C6|C22
3. [문제 1502: `85e66374-f8b...`](#1502) — single-answer, 정답: C21
4. [문제 1503: `292d51b8-0c8...`](#1503) — single-answer, 정답: C10
5. [문제 1504: `59af787b-5d7...`](#1504) — single-answer, 정답: C12
6. [문제 1505: `be7c92f5-e75...`](#1505) — single-answer, 정답: C12
7. [문제 1506: `6920dec8-553...`](#1506) — single-answer, 정답: C11
8. [문제 1507: `35df8e14-7fc...`](#1507) — single-answer, 정답: C17
9. [문제 1508: `d9ab759f-793...`](#1508) — single-answer, 정답: C2
10. [문제 1509: `42c6d29e-20b...`](#1509) — single-answer, 정답: C11

---

### 문제 1500: `77c8c216-4ad...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `77c8c216-4ad0-4c87-91c8-2ca5dfc5b0b2` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Decrease A3 Offset threshold for 3218624_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1500] topology](images/train_1500.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3218624_3 and 3226155_1
- `C2`: Increase A3 Offset threshold for 3226155_1
- `C3`: Lift the tilt angle  of 3226155_1 by 10 degrees
- `C4`: Lift the tilt angle of 3218624_3 by 4 degrees
- `C5`: Increase transmission power for 3226155_1
- `C6`: Decrease A3 Offset threshold for 3226155_1
- `C7`: Press down the tilt angle of 3218624_3 by 4 degrees
- `C8`: Increase A3 Offset threshold for 3218624_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218624_3
- `C10`: Adjust the azimuth of 3218624_3 by 50 degrees
- `C11`: Press down the tilt angle  of 3226155_1 by 10 degrees
- `C12`: Decrease transmission power for 3226155_1
- `C13`: Check test server and transmission issues
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226155_1
- `C15`: Add neighbor relationship between 3274308_2 and 3226155_1
- `C16`: Adjust the azimuth of 3226155_1 by 50 degrees
- `C17`: Increase transmission power for 3218624_3
- `C18`: Decrease A3 Offset threshold for 3218624_3 **← 정답**
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226155_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218624_3
- `C21`: Decrease transmission power for 3218624_3
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.403 | MS1 | 121.4656609322 | 31.1446275550 | 147 | 504990 | -82.79 | 12.31 | 315.16 | 0.01 | 2.67 | 1591 |
| 2024-09-20 22:21:32.941 | MS1 | 121.4656760126 | 31.1446188399 | 147 | 504990 | -79.82 | 13.72 | 466.78 | 0.06 | 2.83 | 1579 |
| 2024-09-20 22:21:33.235 | MS1 | 121.4656750366 | 31.1446180751 | 147 | 504990 | -77.65 | 13.44 | 590.75 | 0.04 | 2.57 | 1590 |
| 2024-09-20 22:21:34.832 | MS1 | 121.4656765232 | 31.1446330546 | 147 | 504990 | -91.23 | -0.78 | 63.51 | 0.13 | 1.30 | 1569 |
| 2024-09-20 22:21:35.504 | MS1 | 121.4656717297 | 31.1446189894 | 147 | 504990 | -84.86 | -3.38 | 42.36 | 0.18 | 1.30 | 1588 |
| 2024-09-20 22:21:36.103 | MS1 | 121.4656653318 | 31.1446327946 | 147 | 504990 | -88.34 | -0.66 | 57.20 | 0.06 | 1.06 | 1583 |
| 2024-09-20 22:21:37.366 | MS1 | 121.4656688199 | 31.1446228044 | 147 | 504990 | -84.54 | -2.35 | 54.42 | 0.17 | 1.41 | 1596 |
| 2024-09-20 22:21:38.752 | MS1 | 121.4656658456 | 31.1446201351 | 147 | 504990 | -91.71 | -2.52 | 74.72 | 0.01 | 1.10 | 1576 |
| 2024-09-20 22:21:39.699 | MS1 | 121.4656626697 | 31.1446211831 | 96 | 504990 | -82.44 | 14.83 | 177.89 | 0.03 | 1.36 | 1584 |
| 2024-09-20 22:21:40.325 | MS1 | 121.4656627227 | 31.1446273875 | 96 | 504990 | -84.12 | 12.29 | 430.38 | 0.05 | 2.21 | 1572 |
| 2024-09-20 22:21:41.698 | MS1 | 121.4656706170 | 31.1446291315 | 96 | 504990 | -76.15 | 14.60 | 343.02 | 0.13 | 2.75 | 1570 |
| 2024-09-20 22:21:42.601 | MS1 | 121.4656673451 | 31.1446305740 | 96 | 504990 | -81.98 | 13.16 | 373.48 | 0.14 | 2.74 | 1588 |

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
| 3218624 | 3 | 121.4676715990 | 31.1558879810 | 138 | 3 | 7 | 19.9 | TDD | 147 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3226155 | 1 | 121.4678267687 | 31.1554873810 | 28 | 10 | 1 | 28.5 | TDD | 96 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3241127 | 4 | 121.4739226193 | 31.1559054032 | 93 | 12 | 9 | 18.5 | TDD | 982 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3274308 | 2 | 121.4683439597 | 31.1455156291 | 13 | 15 | 10 | 45.3 | TDD | 874 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.142 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.280 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.280 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.024 | NREventA3 | measId:2;ServCellPCI:554;Se... |
| 2024-09-20 22:21:38.264 | NRHandoverAttempt | SourcePCI:554;SourceNR-ARFC... |
| 2024-09-20 22:21:38.296 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.308 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.417 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.417 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226155 | 1 | 19.5362 | 8.8959 | -115.5259 | 10.8081 | 193.3715 | 0.0078 | 0.0109 |
| 2024_09_20 22:00 | 3274308 | 2 | 8.0708 | 15.3345 | -116.0559 | 13.9922 | 86.1007 | 0.0043 | 0.0103 |
| 2024_09_20 22:00 | 3218624 | 3 | 17.9883 | 10.2630 | -116.5974 | 8.4512 | 190.1716 | 0.0163 | 0.1335 |
| 2024_09_20 22:00 | 3241127 | 4 | 8.9107 | 13.9919 | -116.5068 | 9.1787 | 150.1278 | 0.0179 | 0.0170 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413752_CA4CB875 | 504990 | 147 | -92.7 | 504990 | 96 | -86.7 | 504990 | 874 | -84.9 | 504990 | 982 |
| MR_1774413752_71D56967 | 504990 | 147 | -91.8 | 504990 | 96 | -87.6 | 504990 | 874 | -86.3 | 504990 | 982 |
| MR_1774413752_BFE7EA03 | 504990 | 147 | -93.0 | 504990 | 96 | -85.6 | 504990 | 874 | -87.1 | 504990 | 982 |
| MR_1774413752_773CBC3A | 504990 | 147 | -91.0 | 504990 | 96 | -86.8 | 504990 | 874 | -88.6 | 504990 | 982 |
| MR_1774413752_7F9A8947 | 504990 | 96 | -85.9 | 504990 | 147 | -90.1 | 504990 | 874 | -85.3 | 504990 | 982 |
| MR_1774413752_880B05D9 | 504990 | 147 | -92.4 | 504990 | 96 | -87.6 | 504990 | 874 | -87.3 | 504990 | 982 |
| MR_1774413752_79836E63 | 504990 | 147 | -93.1 | 504990 | 96 | -87.5 | 504990 | 874 | -88.4 | 504990 | 982 |
| MR_1774413752_6B3506F3 | 504990 | 147 | -91.7 | 504990 | 96 | -87.3 | 504990 | 874 | -86.6 | 504990 | 982 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1501: `47a85f94-15c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `47a85f94-15c9-4e57-81ff-674a183bb1f6` |
| Tag | **multiple-answer** |
| 정답 | **C6|C22** |
| C6 의미 | Decrease transmission power for 3267519_1 |
| C22 의미 | Press down the tilt angle  of 3267519_1 by 1 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1501] topology](images/train_1501.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3267519_1 by 26 degrees
- `C2`: Decrease A3 Offset threshold for 3267519_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267519_1
- `C4`: Lift the tilt angle of 3261927_4 by 5 degrees
- `C5`: Add neighbor relationship between 3230957_2 and 3267519_1
- `C6`: Decrease transmission power for 3267519_1 **← 정답**
- `C7`: Increase A3 Offset threshold for 3267519_1
- `C8`: Press down the tilt angle of 3261927_4 by 5 degrees
- `C9`: Adjust the azimuth of 3261927_4 by 34 degrees
- `C10`: Decrease A3 Offset threshold for 3261927_4
- `C11`: Decrease transmission power for 3261927_4
- `C12`: Lift the tilt angle  of 3267519_1 by 1 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261927_4
- `C14`: Increase A3 Offset threshold for 3261927_4
- `C15`: Add neighbor relationship between 3261927_4 and 3267519_1
- `C16`: Check test server and transmission issues
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267519_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261927_4
- `C19`: Increase transmission power for 3261927_4
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase transmission power for 3267519_1
- `C22`: Press down the tilt angle  of 3267519_1 by 1 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.347 | MS1 | 121.4656593302 | 31.1446207401 | 22 | 504990 | -78.26 | 16.03 | 550.77 | 0.14 | 2.64 | 1584 |
| 2024-09-20 22:21:32.369 | MS1 | 121.4656688482 | 31.1446362597 | 22 | 504990 | -83.54 | 12.92 | 378.25 | 0.07 | 2.62 | 1588 |
| 2024-09-20 22:21:33.768 | MS1 | 121.4656711909 | 31.1446358054 | 22 | 504990 | -75.57 | 13.92 | 536.23 | 0.15 | 2.12 | 1592 |
| 2024-09-20 22:21:34.749 | MS1 | 121.4656668162 | 31.1446327384 | 22 | 504990 | -87.91 | 2.23 | 85.36 | 0.19 | 1.43 | 1582 |
| 2024-09-20 22:21:35.960 | MS1 | 121.4656653395 | 31.1446244991 | 22 | 504990 | -89.10 | 1.26 | 60.90 | 0.16 | 1.37 | 1579 |
| 2024-09-20 22:21:36.150 | MS1 | 121.4656597150 | 31.1446303969 | 22 | 504990 | -90.26 | 1.49 | 65.49 | 0.15 | 1.45 | 1561 |
| 2024-09-20 22:21:37.953 | MS1 | 121.4656606418 | 31.1446374969 | 22 | 504990 | -86.40 | 2.93 | 77.80 | 0.05 | 1.20 | 1566 |
| 2024-09-20 22:21:38.672 | MS1 | 121.4656673521 | 31.1446310883 | 22 | 504990 | -87.27 | 1.74 | 73.34 | 0.16 | 1.11 | 1588 |
| 2024-09-20 22:21:39.420 | MS1 | 121.4656762714 | 31.1446260364 | 22 | 504990 | -86.09 | 3.10 | 46.68 | 0.20 | 1.15 | 1593 |
| 2024-09-20 22:21:40.495 | MS1 | 121.4656655080 | 31.1446324004 | 22 | 504990 | -78.78 | 16.93 | 443.26 | 0.19 | 2.39 | 1563 |
| 2024-09-20 22:21:41.454 | MS1 | 121.4656758601 | 31.1446341542 | 22 | 504990 | -83.73 | 13.09 | 431.99 | 0.04 | 2.63 | 1595 |
| 2024-09-20 22:21:42.420 | MS1 | 121.4656706175 | 31.1446211927 | 22 | 504990 | -77.86 | 15.68 | 527.36 | 0.15 | 2.93 | 1564 |

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
| 3230957 | 2 | 121.4681172808 | 31.1458576547 | 54 | 0 | 1 | 24.7 | TDD | 684 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3259511 | 3 | 121.4720463495 | 31.1533774962 | 249 | 8 | 8 | 30.1 | TDD | 904 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3261927 | 4 | 121.4700219922 | 31.1486551785 | 257 | 1 | 6 | 45.8 | TDD | 22 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3267519 | 1 | 121.4754878101 | 31.1457661718 | 236 | 0 | 2 | 19.3 | TDD | 960 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.886 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.908 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.037 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.037 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267519 | 1 | 9.5188 | 11.8672 | -114.0645 | 19.8744 | 132.2232 | 0.0025 | 0.0152 |
| 2024_09_20 22:00 | 3230957 | 2 | 11.8962 | 13.3000 | -114.9499 | 5.0411 | 91.4780 | 0.0200 | 0.0096 |
| 2024_09_20 22:00 | 3259511 | 3 | 17.9577 | 19.0944 | -115.9673 | 13.7383 | 138.0493 | 0.0096 | 0.0104 |
| 2024_09_20 22:00 | 3261927 | 4 | 19.0747 | 9.5793 | -109.9413 | 18.2288 | 101.9126 | 0.0000 | 0.0195 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413755_CEE92218 | 504990 | 960 | -88.7 | 504990 | 22 | -85.4 | 504990 | 684 | -85.2 | 504990 | 904 |
| MR_1774413755_4C44458F | 504990 | 960 | -88.6 | 504990 | 22 | -84.3 | 504990 | 684 | -84.9 | 504990 | 904 |
| MR_1774413755_069D14C2 | 504990 | 22 | -88.1 | 504990 | 960 | -84.9 | 504990 | 684 | -85.7 | 504990 | 904 |
| MR_1774413755_939B0578 | 504990 | 22 | -88.2 | 504990 | 960 | -86.0 | 504990 | 684 | -84.2 | 504990 | 904 |
| MR_1774413755_46284578 | 504990 | 960 | -86.0 | 504990 | 22 | -86.5 | 504990 | 684 | -83.7 | 504990 | 904 |
| MR_1774413755_50F6601E | 504990 | 960 | -89.4 | 504990 | 22 | -84.2 | 504990 | 684 | -86.7 | 504990 | 904 |
| MR_1774413755_636CA533 | 504990 | 960 | -88.3 | 504990 | 22 | -82.8 | 504990 | 684 | -84.1 | 504990 | 904 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1502: `85e66374-f8b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `85e66374-f8bf-4013-ad9d-d98d92195567` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Add neighbor relationship between 3246007_3 and 3227008_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1502] topology](images/train_1502.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3246007_3
- `C2`: Decrease transmission power for 3227008_2
- `C3`: Decrease A3 Offset threshold for 3246007_3
- `C4`: Press down the tilt angle of 3246007_3 by 10 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227008_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246007_3
- `C7`: Adjust the azimuth of 3246007_3 by 50 degrees
- `C8`: Add neighbor relationship between 3252748_4 and 3227008_2
- `C9`: Increase A3 Offset threshold for 3227008_2
- `C10`: Increase transmission power for 3227008_2
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Adjust the azimuth of 3227008_2 by 7 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246007_3
- `C14`: Press down the tilt angle  of 3227008_2 by 5 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227008_2
- `C16`: Check test server and transmission issues
- `C17`: Lift the tilt angle  of 3227008_2 by 5 degrees
- `C18`: Decrease A3 Offset threshold for 3227008_2
- `C19`: Lift the tilt angle of 3246007_3 by 10 degrees
- `C20`: Increase transmission power for 3246007_3
- `C21`: Add neighbor relationship between 3246007_3 and 3227008_2 **← 정답**
- `C22`: Decrease transmission power for 3246007_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.407 | MS1 | 121.4656647168 | 31.1446345461 | 402 | 504990 | -78.55 | 17.74 | 511.60 | 0.06 | 2.33 | 1561 |
| 2024-09-20 22:21:32.466 | MS1 | 121.4656713166 | 31.1446316125 | 402 | 504990 | -78.76 | 14.36 | 561.97 | 0.18 | 2.18 | 1562 |
| 2024-09-20 22:21:33.411 | MS1 | 121.4656613366 | 31.1446249772 | 402 | 504990 | -76.21 | 16.61 | 352.96 | 0.10 | 2.01 | 1572 |
| 2024-09-20 22:21:34.164 | MS1 | 121.4656694093 | 31.1446368291 | 402 | 504990 | -86.99 | -3.32 | 39.63 | 0.06 | 1.18 | 1561 |
| 2024-09-20 22:21:35.583 | MS1 | 121.4656698688 | 31.1446379565 | 402 | 504990 | -86.57 | -0.04 | 58.55 | 0.16 | 1.19 | 1592 |
| 2024-09-20 22:21:36.185 | MS1 | 121.4656754333 | 31.1446339017 | 402 | 504990 | -91.80 | -0.50 | 32.91 | 0.17 | 1.08 | 1600 |
| 2024-09-20 22:21:37.553 | MS1 | 121.4656746752 | 31.1446263265 | 402 | 504990 | -89.29 | -0.15 | 53.97 | 0.08 | 1.13 | 1575 |
| 2024-09-20 22:21:38.934 | MS1 | 121.4656748593 | 31.1446190172 | 402 | 504990 | -84.12 | 15.17 | 580.12 | 0.05 | 1.11 | 1573 |
| 2024-09-20 22:21:39.863 | MS1 | 121.4656774377 | 31.1446314280 | 402 | 504990 | -83.68 | 15.53 | 520.21 | 0.13 | 1.05 | 1563 |
| 2024-09-20 22:21:40.772 | MS1 | 121.4656664578 | 31.1446243595 | 402 | 504990 | -84.95 | 17.33 | 307.76 | 0.18 | 2.60 | 1597 |
| 2024-09-20 22:21:41.516 | MS1 | 121.4656666837 | 31.1446359630 | 402 | 504990 | -79.81 | 14.14 | 357.73 | 0.03 | 2.93 | 1569 |
| 2024-09-20 22:21:42.875 | MS1 | 121.4656637369 | 31.1446274657 | 402 | 504990 | -79.07 | 12.95 | 577.21 | 0.04 | 2.97 | 1589 |

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
| 3227008 | 2 | 121.4693511413 | 31.1483870545 | 227 | 2 | 2 | 26.0 | TDD | 297 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3244789 | 1 | 121.4732782008 | 31.1506365952 | 258 | 0 | 1 | 38.8 | TDD | 632 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3246007 | 3 | 121.4686143061 | 31.1502667236 | 130 | 8 | 2 | 48.4 | TDD | 402 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3252748 | 4 | 121.4680226771 | 31.1509050558 | 63 | 13 | 4 | 49.7 | TDD | 51 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.657 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.678 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.802 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.802 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.477 | NREventA3 | measId:2;ServCellPCI:335;Se... |
| 2024-09-20 22:21:36.477 | NREventA3 | measId:2;ServCellPCI:335;Se... |
| 2024-09-20 22:21:37.477 | NREventA3 | measId:2;ServCellPCI:335;Se... |
| 2024-09-20 22:21:39.977 | NRRRCReestablishAttempt | PCI:335 |
| 2024-09-20 22:21:39.990 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:40.004 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:40.134 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.134 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244789 | 1 | 17.4926 | 13.3419 | -115.2187 | 13.6209 | 98.4117 | 0.0101 | 0.0110 |
| 2024_09_20 22:00 | 3227008 | 2 | 5.7720 | 5.8442 | -115.9293 | 19.7999 | 141.2050 | 0.0130 | 0.0046 |
| 2024_09_20 22:00 | 3246007 | 3 | 7.7960 | 18.2593 | -116.5377 | 6.0518 | 113.4694 | 0.0098 | 0.1335 |
| 2024_09_20 22:00 | 3252748 | 4 | 15.1995 | 15.2901 | -116.1190 | 11.2356 | 97.4309 | 0.0196 | 0.0064 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415644_7881B511 | 504990 | 297 | -83.5 | 504990 | 402 | -86.9 | 504990 | 51 | -82.2 | 504990 | 632 |
| MR_1774415644_48B4E1E9 | 504990 | 297 | -83.4 | 504990 | 402 | -88.9 | 504990 | 51 | -80.6 | 504990 | 632 |
| MR_1774415644_07FFCECF | 504990 | 297 | -82.3 | 504990 | 402 | -86.6 | 504990 | 51 | -83.6 | 504990 | 632 |
| MR_1774415644_85D40A12 | 504990 | 402 | -86.9 | 504990 | 297 | -81.2 | 504990 | 51 | -81.8 | 504990 | 632 |
| MR_1774415644_0CD1AB34 | 504990 | 297 | -81.8 | 504990 | 402 | -88.6 | 504990 | 51 | -83.3 | 504990 | 632 |
| MR_1774415644_72651122 | 504990 | 402 | -88.1 | 504990 | 297 | -83.0 | 504990 | 51 | -83.6 | 504990 | 632 |
| MR_1774415644_BBE83BD3 | 504990 | 402 | -86.2 | 504990 | 297 | -81.2 | 504990 | 51 | -80.5 | 504990 | 632 |
| MR_1774415644_E6320C84 | 504990 | 297 | -82.0 | 504990 | 402 | -87.7 | 504990 | 51 | -83.3 | 504990 | 632 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1503: `292d51b8-0c8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `292d51b8-0c82-4a1f-9274-48aea8d0666b` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Lift the tilt angle  of 3278529_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1503] topology](images/train_1503.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3278529_4 by 50 degrees
- `C2`: Increase A3 Offset threshold for 3232991_1
- `C3`: Lift the tilt angle of 3271500_3 by 2 degrees
- `C4`: Decrease transmission power for 3232991_1
- `C5`: Decrease A3 Offset threshold for 3271500_3
- `C6`: Decrease A3 Offset threshold for 3232991_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232991_1
- `C8`: Adjust the azimuth of 3271500_3 by 17 degrees
- `C9`: Press down the tilt angle of 3271500_3 by 2 degrees
- `C10`: Lift the tilt angle  of 3278529_4 by 10 degrees **← 정답**
- `C11`: Press down the tilt angle  of 3278529_4 by 10 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Increase A3 Offset threshold for 3271500_3
- `C14`: Increase transmission power for 3232991_1
- `C15`: Add neighbor relationship between 3271500_3 and 3232991_1
- `C16`: Increase transmission power for 3271500_3
- `C17`: Check test server and transmission issues
- `C18`: Decrease transmission power for 3271500_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232991_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271500_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271500_3
- `C22`: Add neighbor relationship between 3278529_4 and 3232991_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.430 | MS1 | 121.4656678507 | 31.1446378791 | 37 | 504990 | -88.42 | 12.68 | 601.10 | 0.10 | 2.92 | 1575 |
| 2024-09-20 22:21:32.999 | MS1 | 121.4656629730 | 31.1446245103 | 37 | 504990 | -89.63 | 15.33 | 401.80 | 0.09 | 2.71 | 1579 |
| 2024-09-20 22:21:33.564 | MS1 | 121.4656652731 | 31.1446346139 | 37 | 504990 | -88.33 | 12.11 | 430.24 | 0.14 | 2.18 | 1574 |
| 2024-09-20 22:21:34.904 | MS1 | 121.4656740414 | 31.1446187233 | 37 | 504990 | -87.63 | 12.59 | 67.37 | 0.18 | 2.21 | 1560 |
| 2024-09-20 22:21:35.560 | MS1 | 121.4656778686 | 31.1446235209 | 37 | 504990 | -88.30 | 15.69 | 70.65 | 0.17 | 2.67 | 1596 |
| 2024-09-20 22:21:36.593 | MS1 | 121.4656598930 | 31.1446269253 | 37 | 504990 | -86.70 | 17.20 | 79.10 | 0.16 | 2.43 | 1597 |
| 2024-09-20 22:21:37.211 | MS1 | 121.4656670091 | 31.1446359227 | 37 | 504990 | -90.94 | 8.38 | 73.60 | 0.04 | 2.86 | 1586 |
| 2024-09-20 22:21:38.167 | MS1 | 121.4656665922 | 31.1446349343 | 37 | 504990 | -90.37 | 11.59 | 86.93 | 0.17 | 2.71 | 1598 |
| 2024-09-20 22:21:39.640 | MS1 | 121.4656610389 | 31.1446324891 | 37 | 504990 | -90.72 | 7.80 | 47.33 | 0.04 | 2.40 | 1567 |
| 2024-09-20 22:21:40.468 | MS1 | 121.4656687272 | 31.1446364770 | 37 | 504990 | -92.14 | 10.11 | 435.50 | 0.09 | 2.83 | 1580 |
| 2024-09-20 22:21:41.620 | MS1 | 121.4656716186 | 31.1446236577 | 37 | 504990 | -93.67 | 12.47 | 410.92 | 0.17 | 2.89 | 1584 |
| 2024-09-20 22:21:42.624 | MS1 | 121.4656671080 | 31.1446265419 | 37 | 504990 | -93.43 | 9.91 | 566.70 | 0.13 | 2.98 | 1597 |

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
| 3232991 | 1 | 121.4655762268 | 31.1483197374 | 67 | 4 | 10 | 45.8 | TDD | 873 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3271500 | 3 | 121.4740780740 | 31.1475969354 | 265 | 0 | 12 | 33.4 | TDD | 37 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3276434 | 2 | 121.4669943545 | 31.1556357726 | 263 | 0 | 8 | 25.2 | TDD | 475 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3278529 | 4 | 121.4730280058 | 31.1479906185 | 74 | 10 | 9 | 15.4 | TDD | 807 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.229 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.252 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.361 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.361 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.114 | NREventA3 | measId:2;ServCellPCI:443;Se... |
| 2024-09-20 22:21:38.354 | NRHandoverAttempt | SourcePCI:443;SourceNR-ARFC... |
| 2024-09-20 22:21:38.385 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.396 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.511 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.511 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232991 | 1 | 17.4080 | 7.2576 | -116.7882 | 19.4364 | 185.6588 | 0.0017 | 0.0023 |
| 2024_09_20 22:00 | 3276434 | 2 | 5.0613 | 13.2570 | -115.9157 | 11.0375 | 180.7482 | 0.0021 | 0.0114 |
| 2024_09_20 22:00 | 3271500 | 3 | 92.4752 | 91.2635 | -115.3302 | 18.3024 | 99.3133 | 0.0139 | 0.0094 |
| 2024_09_20 22:00 | 3278529 | 4 | 14.0446 | 16.9899 | -116.8171 | 13.4141 | 96.2297 | 0.0095 | 0.0075 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414441_4594E78D | 504990 | 37 | -88.3 | 504990 | 873 | -93.1 | 504990 | 807 | -100.0 | 504990 | 475 |
| MR_1774414441_F753DE0D | 504990 | 37 | -89.0 | 504990 | 873 | -93.2 | 504990 | 807 | -98.6 | 504990 | 475 |
| MR_1774414441_9F5C4AE4 | 504990 | 37 | -88.4 | 504990 | 873 | -92.9 | 504990 | 807 | -100.2 | 504990 | 475 |
| MR_1774414441_760052F8 | 504990 | 37 | -86.9 | 504990 | 873 | -95.1 | 504990 | 807 | -97.0 | 504990 | 475 |
| MR_1774414441_5776F897 | 504990 | 37 | -88.3 | 504990 | 873 | -93.5 | 504990 | 807 | -98.2 | 504990 | 475 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1504: `59af787b-5d7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `59af787b-5d7f-4976-9836-5e5d93384506` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216648_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1504] topology](images/train_1504.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3216648_1
- `C2`: Increase transmission power for 3257543_4
- `C3`: Press down the tilt angle of 3216648_1 by 1 degrees
- `C4`: Check test server and transmission issues
- `C5`: Lift the tilt angle of 3216648_1 by 1 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257543_4
- `C7`: Increase transmission power for 3216648_1
- `C8`: Lift the tilt angle  of 3257543_4 by 3 degrees
- `C9`: Decrease A3 Offset threshold for 3257543_4
- `C10`: Adjust the azimuth of 3257543_4 by 50 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257543_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216648_1 **← 정답**
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Add neighbor relationship between 3258577_12 and 3257543_4
- `C15`: Decrease transmission power for 3257543_4
- `C16`: Decrease transmission power for 3216648_1
- `C17`: Add neighbor relationship between 3216648_1 and 3257543_4
- `C18`: Adjust the azimuth of 3216648_1 by 11 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216648_1
- `C20`: Press down the tilt angle  of 3257543_4 by 3 degrees
- `C21`: Decrease A3 Offset threshold for 3216648_1
- `C22`: Increase A3 Offset threshold for 3257543_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.188 | MS1 | 121.4656686286 | 31.1446205943 | 334 | 504990 | -93.44 | 12.46 | 458.86 | 0.10 | 2.20 | 1560 |
| 2024-09-20 22:21:32.367 | MS1 | 121.4656609864 | 31.1446272271 | 317 | 504990 | -95.63 | 14.52 | 425.25 | 0.03 | 2.02 | 1600 |
| 2024-09-20 22:21:33.747 | MS1 | 121.4656761212 | 31.1446377688 | 252 | 504990 | -94.31 | 10.19 | 340.79 | 0.18 | 2.67 | 1566 |
| 2024-09-20 22:21:34.181 | MS1 | 121.4656687430 | 31.1446350230 | 604 | 152650 | -91.53 | 3.81 | 51.11 | 0.01 | 1.84 | 963 |
| 2024-09-20 22:21:35.162 | MS1 | 121.4656671654 | 31.1446257078 | 175 | 152650 | -92.43 | 2.79 | 63.36 | 0.09 | 1.78 | 999 |
| 2024-09-20 22:21:36.275 | MS1 | 121.4656600410 | 31.1446314903 | 214 | 152650 | -92.18 | 6.38 | 72.58 | 0.01 | 1.56 | 977 |
| 2024-09-20 22:21:37.797 | MS1 | 121.4656583063 | 31.1446316445 | 719 | 152650 | -93.08 | 7.47 | 66.69 | 0.01 | 1.91 | 979 |
| 2024-09-20 22:21:38.855 | MS1 | 121.4656701594 | 31.1446257268 | 604 | 152650 | -93.20 | 7.69 | 87.00 | 0.06 | 1.57 | 947 |
| 2024-09-20 22:21:39.637 | MS1 | 121.4656695038 | 31.1446269045 | 175 | 152650 | -94.37 | 7.03 | 49.76 | 0.11 | 1.60 | 922 |
| 2024-09-20 22:21:40.753 | MS1 | 121.4656747702 | 31.1446229786 | 214 | 152650 | -89.59 | 3.93 | 72.25 | 0.00 | 2.22 | 1564 |
| 2024-09-20 22:21:41.585 | MS1 | 121.4656593747 | 31.1446371802 | 719 | 152650 | -87.78 | 4.88 | 43.37 | 0.06 | 2.79 | 1586 |
| 2024-09-20 22:21:42.316 | MS1 | 121.4656775777 | 31.1446246424 | 604 | 152650 | -90.08 | 3.26 | 67.98 | 0.10 | 2.93 | 1582 |

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
| 3216648 | 1 | 121.4649746409 | 31.1506136828 | 185 | 0 | 12 | 14.7 | TDD | 334 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3219821 | 2 | 121.4657286220 | 31.1502334143 | 201 | 2 | 0 | 21.7 | TDD | 252 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3221687 | 6 | 121.4671397160 | 31.1502331227 | 349 | 7 | 10 | 12.2 | TDD | 30 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3223759 | 3 | 121.4664329333 | 31.1552239861 | 195 | 5 | 8 | 20.1 | TDD | 121 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3224139 | 5 | 121.4733717211 | 31.1490236116 | 7 | 3 | 8 | 20.9 | TDD | 317 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3237645 | 8 | 121.4729899584 | 31.1511710215 | 241 | 9 | 6 | 27.3 | FDD | 846 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3252036 | 10 | 121.4654538159 | 31.1477817028 | 282 | 12 | 6 | 19.2 | FDD | 175 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3253837 | 11 | 121.4718631835 | 31.1479608368 | 166 | 4 | 6 | 17.3 | FDD | 212 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3254318 | 7 | 121.4688331444 | 31.1505906351 | 89 | 11 | 0 | 19.5 | FDD | 166 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3256228 | 13 | 121.4685150132 | 31.1531230126 | 75 | 5 | 3 | 5.8 | FDD | 604 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3257543 | 4 | 121.4714323363 | 31.1475930602 | 289 | 2 | 1 | 11.4 | TDD | 700 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3258096 | 9 | 121.4744682755 | 31.1489672451 | 11 | 3 | 3 | 11.7 | FDD | 719 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3258577 | 12 | 121.4655680733 | 31.1530198589 | 206 | 7 | 5 | 26.4 | FDD | 214 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |

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
| 2024-09-20 22:21:31.558 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.579 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.684 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.684 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.443 | NREventA2 | measId:1;ServCellPCI:750;Se... |
| 2024-09-20 22:21:35.567 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.854 | NREventA5 | measId:3;ServCellPCI:750;Se... |
| 2024-09-20 22:21:35.888 | NRHandoverAttempt | SourcePCI:750;SourceNR-ARFC... |
| 2024-09-20 22:21:35.911 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.923 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:36.047 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.047 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216648 | 1 | 8.7000 | 10.6329 | -116.0882 | 5.9627 | 134.4923 | 0.0004 | 0.0034 |
| 2024_09_20 22:00 | 3219821 | 2 | 19.0334 | 17.3370 | -115.1084 | 8.5619 | 170.4644 | 0.0183 | 0.0193 |
| 2024_09_20 22:00 | 3223759 | 3 | 18.3047 | 6.3550 | -115.0415 | 11.4203 | 139.4533 | 0.0009 | 0.0047 |
| 2024_09_20 22:00 | 3257543 | 4 | 15.3337 | 10.2082 | -117.9516 | 13.8984 | 128.6914 | 0.0122 | 0.0129 |
| 2024_09_20 22:00 | 3224139 | 5 | 17.0819 | 12.2328 | -117.0041 | 8.2607 | 88.1181 | 0.0144 | 0.0112 |
| 2024_09_20 22:00 | 3221687 | 6 | 9.3728 | 15.2734 | -115.9884 | 17.2461 | 172.3215 | 0.0173 | 0.0010 |
| 2024_09_20 22:00 | 3254318 | 7 | 12.1481 | 5.9368 | -114.4817 | 4.0062 | 57.5185 | 0.0096 | 0.0177 |
| 2024_09_20 22:00 | 3237645 | 8 | 15.9442 | 13.6995 | -117.2329 | 4.1955 | 22.6239 | 0.0030 | 0.0141 |
| 2024_09_20 22:00 | 3258096 | 9 | 19.2440 | 15.1703 | -115.8889 | 4.3918 | 42.1589 | 0.0111 | 0.0038 |
| 2024_09_20 22:00 | 3252036 | 10 | 18.5241 | 8.6157 | -115.5711 | 4.2848 | 21.5008 | 0.0176 | 0.0055 |
| 2024_09_20 22:00 | 3253837 | 11 | 7.5406 | 11.3013 | -117.0732 | 4.0986 | 59.0644 | 0.0052 | 0.0148 |
| 2024_09_20 22:00 | 3258577 | 12 | 18.4913 | 16.0786 | -116.6816 | 4.8997 | 48.5576 | 0.0000 | 0.0144 |
| 2024_09_20 22:00 | 3256228 | 13 | 11.5262 | 6.0510 | -117.8766 | 4.7641 | 51.9212 | 0.0070 | 0.0031 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414909_F0586A9A | 504990 | 252 | -96.1 | 504990 | 700 | -92.2 | 504990 | 30 | -100.4 | 504990 | 121 |
| MR_1774414909_2F95E738 | 504990 | 252 | -92.8 | 504990 | 700 | -91.1 | 504990 | 30 | -98.4 | 504990 | 121 |
| MR_1774414909_9D3FCA4A | 152650 | 604 | -93.0 | 152650 | 166 | -97.1 | 152650 | 846 | -102.3 | 152650 | 212 |
| MR_1774414909_2867B790 | 152650 | 604 | -91.4 | 152650 | 166 | -97.9 | 152650 | 846 | -101.2 | 152650 | 212 |
| MR_1774414909_6B047EF6 | 152650 | 604 | -90.3 | 152650 | 166 | -98.0 | 152650 | 846 | -103.3 | 152650 | 212 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1505: `be7c92f5-e75...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `be7c92f5-e75a-47b7-bea5-1b4fbc603195` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Lift the tilt angle  of 3232366_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1505] topology](images/train_1505.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase A3 Offset threshold for 3268030_4
- `C3`: Decrease transmission power for 3242284_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268030_4
- `C5`: Press down the tilt angle  of 3232366_1 by 10 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242284_3
- `C7`: Increase transmission power for 3268030_4
- `C8`: Increase transmission power for 3242284_3
- `C9`: Increase A3 Offset threshold for 3242284_3
- `C10`: Check test server and transmission issues
- `C11`: Decrease A3 Offset threshold for 3268030_4
- `C12`: Lift the tilt angle  of 3232366_1 by 10 degrees **← 정답**
- `C13`: Adjust the azimuth of 3232366_1 by 49 degrees
- `C14`: Add neighbor relationship between 3242284_3 and 3268030_4
- `C15`: Add neighbor relationship between 3232366_1 and 3268030_4
- `C16`: Adjust the azimuth of 3242284_3 by 8 degrees
- `C17`: Decrease transmission power for 3268030_4
- `C18`: Press down the tilt angle of 3242284_3 by 2 degrees
- `C19`: Lift the tilt angle of 3242284_3 by 2 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268030_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242284_3
- `C22`: Decrease A3 Offset threshold for 3242284_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.805 | MS1 | 121.4656615761 | 31.1446248889 | 443 | 504990 | -86.17 | 17.35 | 508.04 | 0.05 | 2.32 | 1598 |
| 2024-09-20 22:21:32.422 | MS1 | 121.4656639789 | 31.1446359885 | 443 | 504990 | -87.91 | 14.11 | 492.45 | 0.10 | 2.82 | 1560 |
| 2024-09-20 22:21:33.306 | MS1 | 121.4656659484 | 31.1446335768 | 443 | 504990 | -90.84 | 12.79 | 573.02 | 0.02 | 2.95 | 1579 |
| 2024-09-20 22:21:34.946 | MS1 | 121.4656670452 | 31.1446185954 | 443 | 504990 | -88.83 | 17.79 | 92.71 | 0.07 | 2.58 | 1564 |
| 2024-09-20 22:21:35.412 | MS1 | 121.4656655461 | 31.1446247205 | 443 | 504990 | -90.59 | 16.50 | 57.86 | 0.20 | 2.72 | 1571 |
| 2024-09-20 22:21:36.328 | MS1 | 121.4656706170 | 31.1446232751 | 443 | 504990 | -90.50 | 14.31 | 83.36 | 0.03 | 2.10 | 1594 |
| 2024-09-20 22:21:37.502 | MS1 | 121.4656588966 | 31.1446217155 | 443 | 504990 | -89.16 | 10.84 | 54.19 | 0.19 | 2.36 | 1591 |
| 2024-09-20 22:21:38.182 | MS1 | 121.4656691828 | 31.1446350725 | 443 | 504990 | -92.72 | 12.86 | 70.38 | 0.12 | 2.17 | 1593 |
| 2024-09-20 22:21:39.727 | MS1 | 121.4656734786 | 31.1446288149 | 443 | 504990 | -93.39 | 10.66 | 81.30 | 0.19 | 2.47 | 1576 |
| 2024-09-20 22:21:40.623 | MS1 | 121.4656696832 | 31.1446247844 | 443 | 504990 | -91.33 | 11.00 | 477.21 | 0.11 | 2.93 | 1576 |
| 2024-09-20 22:21:41.814 | MS1 | 121.4656672743 | 31.1446296046 | 443 | 504990 | -90.29 | 7.43 | 553.18 | 0.12 | 2.22 | 1593 |
| 2024-09-20 22:21:42.459 | MS1 | 121.4656769364 | 31.1446303087 | 443 | 504990 | -89.74 | 10.55 | 455.26 | 0.01 | 2.93 | 1572 |

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
| 3232366 | 1 | 121.4718936314 | 31.1541797681 | 347 | 11 | 3 | 23.6 | TDD | 320 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3242284 | 3 | 121.4710849849 | 31.1523231569 | 203 | 1 | 1 | 20.0 | TDD | 443 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3267477 | 2 | 121.4754341471 | 31.1546365852 | 263 | 6 | 0 | 29.6 | TDD | 594 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3268030 | 4 | 121.4656034965 | 31.1463303179 | 129 | 0 | 12 | 42.7 | TDD | 646 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.205 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.220 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.326 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.326 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.075 | NREventA3 | measId:2;ServCellPCI:138;Se... |
| 2024-09-20 22:21:38.315 | NRHandoverAttempt | SourcePCI:138;SourceNR-ARFC... |
| 2024-09-20 22:21:38.355 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.370 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.511 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.511 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232366 | 1 | 10.9129 | 13.8424 | -115.5000 | 16.4997 | 99.5427 | 0.0184 | 0.0122 |
| 2024_09_20 22:00 | 3267477 | 2 | 8.7390 | 7.0791 | -117.0492 | 18.6008 | 137.7842 | 0.0070 | 0.0028 |
| 2024_09_20 22:00 | 3242284 | 3 | 81.1929 | 83.0098 | -114.4526 | 5.0263 | 125.4975 | 0.0015 | 0.0154 |
| 2024_09_20 22:00 | 3268030 | 4 | 15.6298 | 9.4843 | -117.4458 | 12.3620 | 121.1093 | 0.0051 | 0.0080 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413691_A0F835D0 | 504990 | 443 | -87.1 | 504990 | 646 | -90.2 | 504990 | 320 | -98.8 | 504990 | 594 |
| MR_1774413691_E06D2918 | 504990 | 443 | -89.9 | 504990 | 646 | -91.2 | 504990 | 320 | -97.5 | 504990 | 594 |
| MR_1774413691_1D4FD02C | 504990 | 443 | -88.2 | 504990 | 646 | -92.8 | 504990 | 320 | -97.6 | 504990 | 594 |
| MR_1774413691_C4F4E10C | 504990 | 443 | -90.0 | 504990 | 646 | -89.4 | 504990 | 320 | -97.3 | 504990 | 594 |
| MR_1774413691_5EC52565 | 504990 | 443 | -90.5 | 504990 | 646 | -92.5 | 504990 | 320 | -96.8 | 504990 | 594 |
| MR_1774413691_A7B6C391 | 504990 | 443 | -88.7 | 504990 | 646 | -89.3 | 504990 | 320 | -99.6 | 504990 | 594 |
| MR_1774413691_9C1EDFA3 | 504990 | 443 | -88.9 | 504990 | 646 | -91.9 | 504990 | 320 | -97.3 | 504990 | 594 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1506: `6920dec8-553...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6920dec8-5533-49ba-b23a-c0b9fe311759` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271081_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1506] topology](images/train_1506.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3271081_1
- `C2`: Adjust the azimuth of 3225847_5 by 5 degrees
- `C3`: Increase transmission power for 3225847_5
- `C4`: Decrease transmission power for 3225847_5
- `C5`: Increase transmission power for 3271081_1
- `C6`: Add neighbor relationship between 3251779_8 and 3225847_5
- `C7`: Press down the tilt angle  of 3225847_5 by 4 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225847_5
- `C9`: Decrease A3 Offset threshold for 3225847_5
- `C10`: Add neighbor relationship between 3271081_1 and 3225847_5
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271081_1 **← 정답**
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225847_5
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271081_1
- `C14`: Lift the tilt angle of 3271081_1 by 5 degrees
- `C15`: Increase A3 Offset threshold for 3225847_5
- `C16`: Press down the tilt angle of 3271081_1 by 5 degrees
- `C17`: Decrease A3 Offset threshold for 3271081_1
- `C18`: Decrease transmission power for 3271081_1
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Lift the tilt angle  of 3225847_5 by 4 degrees
- `C21`: Check test server and transmission issues
- `C22`: Adjust the azimuth of 3271081_1 by 39 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.611 | MS1 | 121.4656705719 | 31.1446242156 | 385 | 504990 | -94.85 | 11.52 | 553.90 | 0.14 | 2.11 | 1561 |
| 2024-09-20 22:21:32.901 | MS1 | 121.4656770143 | 31.1446342053 | 941 | 504990 | -95.64 | 12.87 | 502.47 | 0.06 | 2.35 | 1594 |
| 2024-09-20 22:21:33.976 | MS1 | 121.4656755340 | 31.1446192225 | 995 | 504990 | -95.81 | 12.99 | 312.43 | 0.04 | 2.55 | 1562 |
| 2024-09-20 22:21:34.230 | MS1 | 121.4656583176 | 31.1446310771 | 18 | 152650 | -94.71 | 5.29 | 73.24 | 0.18 | 1.76 | 960 |
| 2024-09-20 22:21:35.858 | MS1 | 121.4656707490 | 31.1446314108 | 887 | 152650 | -92.79 | 3.12 | 103.79 | 0.04 | 1.59 | 950 |
| 2024-09-20 22:21:36.419 | MS1 | 121.4656751581 | 31.1446266124 | 701 | 152650 | -96.10 | 3.01 | 61.43 | 0.00 | 1.81 | 982 |
| 2024-09-20 22:21:37.801 | MS1 | 121.4656591064 | 31.1446302546 | 85 | 152650 | -90.02 | 4.95 | 94.02 | 0.02 | 1.66 | 970 |
| 2024-09-20 22:21:38.472 | MS1 | 121.4656724457 | 31.1446189443 | 18 | 152650 | -87.72 | 4.25 | 57.80 | 0.17 | 1.67 | 905 |
| 2024-09-20 22:21:39.399 | MS1 | 121.4656709996 | 31.1446217006 | 887 | 152650 | -89.24 | 7.37 | 92.15 | 0.19 | 1.72 | 932 |
| 2024-09-20 22:21:40.946 | MS1 | 121.4656704219 | 31.1446204381 | 701 | 152650 | -91.43 | 5.71 | 64.48 | 0.19 | 2.20 | 1594 |
| 2024-09-20 22:21:41.254 | MS1 | 121.4656661556 | 31.1446339542 | 85 | 152650 | -90.69 | 5.30 | 59.65 | 0.14 | 2.96 | 1565 |
| 2024-09-20 22:21:42.979 | MS1 | 121.4656654432 | 31.1446253518 | 18 | 152650 | -90.44 | 7.10 | 59.00 | 0.01 | 2.90 | 1563 |

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
| 3213195 | 3 | 121.4677854161 | 31.1535933749 | 85 | 15 | 5 | 21.0 | TDD | 134 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3224610 | 6 | 121.4716790507 | 31.1496423154 | 306 | 8 | 8 | 27.9 | TDD | 507 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3225847 | 5 | 121.4646209010 | 31.1502598933 | 166 | 3 | 9 | 16.3 | TDD | 368 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3228893 | 13 | 121.4706601329 | 31.1495354271 | 308 | 0 | 7 | 9.8 | FDD | 381 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3231813 | 12 | 121.4689767702 | 31.1553821729 | 40 | 7 | 8 | 27.3 | FDD | 635 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3233445 | 9 | 121.4646034964 | 31.1454173287 | 257 | 4 | 1 | 16.8 | FDD | 18 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3238773 | 4 | 121.4667252230 | 31.1498093409 | 231 | 2 | 11 | 17.7 | TDD | 941 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3245171 | 10 | 121.4702377360 | 31.1453944229 | 136 | 7 | 1 | 21.5 | FDD | 85 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3251779 | 8 | 121.4671967610 | 31.1474512155 | 89 | 12 | 7 | 4.9 | FDD | 701 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3261060 | 11 | 121.4700976888 | 31.1480823075 | 56 | 9 | 0 | 3.4 | FDD | 887 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3269536 | 2 | 121.4656604177 | 31.1539655148 | 195 | 0 | 9 | 6.9 | TDD | 995 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3271081 | 1 | 121.4724107524 | 31.1491561947 | 193 | 4 | 5 | 7.6 | TDD | 385 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3277087 | 7 | 121.4730058772 | 31.1488364784 | 166 | 13 | 9 | 18.1 | FDD | 901 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |

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
| 2024-09-20 22:21:31.275 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.290 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.407 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.407 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.157 | NREventA2 | measId:1;ServCellPCI:648;Se... |
| 2024-09-20 22:21:35.271 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.521 | NREventA5 | measId:3;ServCellPCI:648;Se... |
| 2024-09-20 22:21:35.590 | NRHandoverAttempt | SourcePCI:648;SourceNR-ARFC... |
| 2024-09-20 22:21:35.638 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.653 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.801 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.801 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271081 | 1 | 11.2554 | 9.4353 | -115.3565 | 14.5145 | 193.2700 | 0.0155 | 0.0017 |
| 2024_09_20 22:00 | 3269536 | 2 | 9.7393 | 14.5087 | -114.1457 | 10.9192 | 131.6833 | 0.0117 | 0.0146 |
| 2024_09_20 22:00 | 3213195 | 3 | 9.6029 | 10.2403 | -115.1768 | 5.2098 | 143.8600 | 0.0160 | 0.0157 |
| 2024_09_20 22:00 | 3238773 | 4 | 11.7457 | 16.4494 | -117.3784 | 5.3799 | 124.2955 | 0.0029 | 0.0000 |
| 2024_09_20 22:00 | 3225847 | 5 | 5.6540 | 6.2631 | -117.3915 | 8.0843 | 81.5867 | 0.0110 | 0.0165 |
| 2024_09_20 22:00 | 3224610 | 6 | 16.2034 | 13.8867 | -115.8554 | 7.3370 | 127.4672 | 0.0139 | 0.0140 |
| 2024_09_20 22:00 | 3277087 | 7 | 12.4121 | 5.9634 | -115.9400 | 3.5443 | 20.5507 | 0.0164 | 0.0168 |
| 2024_09_20 22:00 | 3251779 | 8 | 18.9712 | 12.0568 | -116.7039 | 3.2198 | 25.0563 | 0.0027 | 0.0159 |
| 2024_09_20 22:00 | 3233445 | 9 | 7.6838 | 14.0879 | -116.8011 | 4.7538 | 48.8101 | 0.0091 | 0.0056 |
| 2024_09_20 22:00 | 3245171 | 10 | 12.5181 | 15.7318 | -114.0621 | 4.8818 | 28.1998 | 0.0180 | 0.0119 |
| 2024_09_20 22:00 | 3261060 | 11 | 12.4725 | 16.4839 | -114.4623 | 4.1549 | 49.8288 | 0.0113 | 0.0067 |
| 2024_09_20 22:00 | 3231813 | 12 | 9.6157 | 11.4868 | -117.0331 | 4.0859 | 56.5958 | 0.0038 | 0.0025 |
| 2024_09_20 22:00 | 3228893 | 13 | 17.2389 | 16.6711 | -115.9954 | 3.2022 | 31.0957 | 0.0143 | 0.0108 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413504_BE0FC83D | 152650 | 18 | -96.5 | 152650 | 381 | -97.8 | 152650 | 635 | -106.7 | 152650 | 901 |
| MR_1774413504_5A559F1F | 152650 | 18 | -93.6 | 152650 | 381 | -97.0 | 152650 | 635 | -106.4 | 152650 | 901 |
| MR_1774413504_EE9252B2 | 504990 | 995 | -97.5 | 504990 | 368 | -93.6 | 504990 | 134 | -99.2 | 504990 | 507 |
| MR_1774413504_27414793 | 504990 | 995 | -94.6 | 504990 | 368 | -95.8 | 504990 | 134 | -100.0 | 504990 | 507 |
| MR_1774413504_09C95F36 | 504990 | 995 | -96.3 | 504990 | 368 | -93.8 | 504990 | 134 | -98.4 | 504990 | 507 |
| MR_1774413504_5CD24D77 | 152650 | 18 | -94.3 | 152650 | 381 | -96.9 | 152650 | 635 | -105.4 | 152650 | 901 |
| MR_1774413504_91EA0CA9 | 504990 | 995 | -97.7 | 504990 | 368 | -95.7 | 504990 | 134 | -100.0 | 504990 | 507 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1507: `35df8e14-7fc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `35df8e14-7fc7-4a50-a5f8-ee2cf2898ce6` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Decrease A3 Offset threshold for 3276464_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1507] topology](images/train_1507.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3274897_4 and 3257330_3
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Adjust the azimuth of 3276464_1 by 50 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257330_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276464_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257330_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276464_1
- `C8`: Decrease transmission power for 3257330_3
- `C9`: Decrease transmission power for 3276464_1
- `C10`: Increase transmission power for 3257330_3
- `C11`: Press down the tilt angle  of 3257330_3 by 10 degrees
- `C12`: Adjust the azimuth of 3257330_3 by 50 degrees
- `C13`: Increase A3 Offset threshold for 3257330_3
- `C14`: Lift the tilt angle  of 3257330_3 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3257330_3
- `C16`: Add neighbor relationship between 3276464_1 and 3257330_3
- `C17`: Decrease A3 Offset threshold for 3276464_1 **← 정답**
- `C18`: Increase transmission power for 3276464_1
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle of 3276464_1 by 10 degrees
- `C21`: Increase A3 Offset threshold for 3276464_1
- `C22`: Lift the tilt angle of 3276464_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.469 | MS1 | 121.4656761015 | 31.1446336996 | 888 | 504990 | -82.43 | 15.74 | 342.46 | 0.09 | 2.38 | 1591 |
| 2024-09-20 22:21:32.187 | MS1 | 121.4656695680 | 31.1446245617 | 888 | 504990 | -81.41 | 12.81 | 589.37 | 0.12 | 2.39 | 1568 |
| 2024-09-20 22:21:33.773 | MS1 | 121.4656613365 | 31.1446259299 | 888 | 504990 | -82.78 | 12.99 | 571.48 | 0.01 | 2.36 | 1575 |
| 2024-09-20 22:21:34.874 | MS1 | 121.4656599771 | 31.1446247095 | 888 | 504990 | -92.50 | -2.40 | 26.55 | 0.03 | 1.05 | 1570 |
| 2024-09-20 22:21:35.654 | MS1 | 121.4656657451 | 31.1446210993 | 888 | 504990 | -92.63 | -0.82 | 57.72 | 0.20 | 1.21 | 1570 |
| 2024-09-20 22:21:36.925 | MS1 | 121.4656691569 | 31.1446227643 | 888 | 504990 | -86.72 | -3.11 | 68.97 | 0.05 | 1.09 | 1597 |
| 2024-09-20 22:21:37.591 | MS1 | 121.4656736232 | 31.1446351543 | 888 | 504990 | -85.00 | -0.75 | 47.47 | 0.05 | 1.06 | 1583 |
| 2024-09-20 22:21:38.120 | MS1 | 121.4656632315 | 31.1446309960 | 888 | 504990 | -87.73 | -2.79 | 62.13 | 0.15 | 1.06 | 1582 |
| 2024-09-20 22:21:39.514 | MS1 | 121.4656732853 | 31.1446330624 | 661 | 504990 | -79.01 | 13.68 | 250.04 | 0.04 | 1.34 | 1585 |
| 2024-09-20 22:21:40.259 | MS1 | 121.4656710644 | 31.1446265608 | 661 | 504990 | -82.94 | 16.04 | 460.85 | 0.04 | 2.66 | 1562 |
| 2024-09-20 22:21:41.517 | MS1 | 121.4656712310 | 31.1446347773 | 661 | 504990 | -79.81 | 14.89 | 366.97 | 0.16 | 2.15 | 1591 |
| 2024-09-20 22:21:42.422 | MS1 | 121.4656624854 | 31.1446325987 | 661 | 504990 | -83.81 | 12.29 | 385.49 | 0.18 | 2.22 | 1588 |

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
| 3224102 | 2 | 121.4649987004 | 31.1557135130 | 322 | 14 | 8 | 45.1 | TDD | 403 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3257330 | 3 | 121.4651506220 | 31.1526313947 | 346 | 11 | 11 | 37.5 | TDD | 661 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3274897 | 4 | 121.4673229335 | 31.1440350333 | 147 | 8 | 9 | 22.4 | TDD | 566 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3276464 | 1 | 121.4684762810 | 31.1450533636 | 152 | 13 | 1 | 15.5 | TDD | 888 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.076 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.092 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.209 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.209 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.888 | NREventA3 | measId:2;ServCellPCI:726;Se... |
| 2024-09-20 22:21:38.128 | NRHandoverAttempt | SourcePCI:726;SourceNR-ARFC... |
| 2024-09-20 22:21:38.167 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.182 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.304 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.304 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276464 | 1 | 17.9139 | 13.7484 | -116.5480 | 11.3146 | 199.6062 | 0.0008 | 0.1257 |
| 2024_09_20 22:00 | 3224102 | 2 | 18.5296 | 12.7140 | -115.5293 | 5.9394 | 121.3953 | 0.0020 | 0.0184 |
| 2024_09_20 22:00 | 3257330 | 3 | 5.8296 | 7.0163 | -116.5971 | 18.3366 | 194.3313 | 0.0163 | 0.0173 |
| 2024_09_20 22:00 | 3274897 | 4 | 9.3369 | 5.4723 | -116.9240 | 13.6124 | 116.3541 | 0.0064 | 0.0173 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414192_192210AD | 504990 | 661 | -88.0 | 504990 | 888 | -92.5 | 504990 | 566 | -93.1 | 504990 | 403 |
| MR_1774414192_B2D761A0 | 504990 | 661 | -89.9 | 504990 | 888 | -92.9 | 504990 | 566 | -94.7 | 504990 | 403 |
| MR_1774414192_CD9D699A | 504990 | 888 | -94.0 | 504990 | 661 | -88.4 | 504990 | 566 | -91.6 | 504990 | 403 |
| MR_1774414192_6084F950 | 504990 | 661 | -89.3 | 504990 | 888 | -91.9 | 504990 | 566 | -91.9 | 504990 | 403 |
| MR_1774414192_F68C05F0 | 504990 | 888 | -93.6 | 504990 | 661 | -89.9 | 504990 | 566 | -93.4 | 504990 | 403 |
| MR_1774414192_86560213 | 504990 | 661 | -86.3 | 504990 | 888 | -92.1 | 504990 | 566 | -94.6 | 504990 | 403 |
| MR_1774414192_36069CFF | 504990 | 661 | -87.3 | 504990 | 888 | -93.2 | 504990 | 566 | -91.6 | 504990 | 403 |
| MR_1774414192_2DF93671 | 504990 | 661 | -88.5 | 504990 | 888 | -91.3 | 504990 | 566 | -93.6 | 504990 | 403 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1508: `d9ab759f-793...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d9ab759f-7935-41f8-8233-c37f34217979` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Add neighbor relationship between 3233858_1 and 3213276_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1508] topology](images/train_1508.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3233858_1 by 10 degrees
- `C2`: Add neighbor relationship between 3233858_1 and 3213276_3 **← 정답**
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213276_3
- `C4`: Decrease A3 Offset threshold for 3233858_1
- `C5`: Press down the tilt angle of 3233858_1 by 10 degrees
- `C6`: Lift the tilt angle  of 3213276_3 by 5 degrees
- `C7`: Adjust the azimuth of 3233858_1 by 50 degrees
- `C8`: Add neighbor relationship between 3265467_4 and 3213276_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233858_1
- `C10`: Decrease transmission power for 3233858_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233858_1
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213276_3
- `C14`: Increase A3 Offset threshold for 3213276_3
- `C15`: Press down the tilt angle  of 3213276_3 by 5 degrees
- `C16`: Increase transmission power for 3213276_3
- `C17`: Increase A3 Offset threshold for 3233858_1
- `C18`: Check test server and transmission issues
- `C19`: Decrease A3 Offset threshold for 3213276_3
- `C20`: Adjust the azimuth of 3213276_3 by 31 degrees
- `C21`: Decrease transmission power for 3213276_3
- `C22`: Increase transmission power for 3233858_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.668 | MS1 | 121.4656616079 | 31.1446347742 | 243 | 504990 | -76.09 | 13.74 | 520.84 | 0.01 | 2.19 | 1574 |
| 2024-09-20 22:21:32.894 | MS1 | 121.4656661651 | 31.1446271423 | 243 | 504990 | -84.16 | 12.28 | 413.20 | 0.07 | 2.89 | 1592 |
| 2024-09-20 22:21:33.498 | MS1 | 121.4656713242 | 31.1446202762 | 243 | 504990 | -78.12 | 16.90 | 449.12 | 0.20 | 2.50 | 1578 |
| 2024-09-20 22:21:34.441 | MS1 | 121.4656619872 | 31.1446264327 | 243 | 504990 | -93.27 | -3.56 | 63.26 | 0.15 | 1.25 | 1598 |
| 2024-09-20 22:21:35.390 | MS1 | 121.4656727680 | 31.1446235402 | 243 | 504990 | -90.58 | -1.89 | 46.08 | 0.02 | 1.40 | 1586 |
| 2024-09-20 22:21:36.172 | MS1 | 121.4656768075 | 31.1446254721 | 243 | 504990 | -89.29 | -2.03 | 58.35 | 0.14 | 1.23 | 1586 |
| 2024-09-20 22:21:37.863 | MS1 | 121.4656592813 | 31.1446319064 | 243 | 504990 | -86.02 | -0.72 | 29.94 | 0.14 | 1.09 | 1586 |
| 2024-09-20 22:21:38.551 | MS1 | 121.4656671430 | 31.1446228459 | 243 | 504990 | -82.38 | 14.33 | 589.15 | 0.02 | 1.35 | 1567 |
| 2024-09-20 22:21:39.949 | MS1 | 121.4656669681 | 31.1446343736 | 243 | 504990 | -81.45 | 15.68 | 594.14 | 0.04 | 1.23 | 1596 |
| 2024-09-20 22:21:40.787 | MS1 | 121.4656738475 | 31.1446237173 | 243 | 504990 | -79.84 | 13.44 | 567.86 | 0.09 | 2.53 | 1595 |
| 2024-09-20 22:21:41.428 | MS1 | 121.4656774397 | 31.1446214124 | 243 | 504990 | -75.30 | 15.91 | 305.49 | 0.14 | 2.03 | 1599 |
| 2024-09-20 22:21:42.438 | MS1 | 121.4656597031 | 31.1446187525 | 243 | 504990 | -82.48 | 16.89 | 350.93 | 0.10 | 2.14 | 1568 |

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
| 3213276 | 3 | 121.4708723934 | 31.1556203315 | 171 | 3 | 10 | 47.5 | TDD | 486 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3233858 | 1 | 121.4655707789 | 31.1475952874 | 298 | 13 | 2 | 35.4 | TDD | 243 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3253965 | 2 | 121.4693151795 | 31.1532905233 | 173 | 8 | 7 | 44.5 | TDD | 675 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3265467 | 4 | 121.4677556661 | 31.1511537753 | 165 | 1 | 6 | 36.2 | TDD | 359 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.399 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.415 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.564 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.564 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.263 | NREventA3 | measId:2;ServCellPCI:360;Se... |
| 2024-09-20 22:21:36.263 | NREventA3 | measId:2;ServCellPCI:360;Se... |
| 2024-09-20 22:21:37.263 | NREventA3 | measId:2;ServCellPCI:360;Se... |
| 2024-09-20 22:21:39.763 | NRRRCReestablishAttempt | PCI:360 |
| 2024-09-20 22:21:39.775 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.785 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.909 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.909 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233858 | 1 | 19.9435 | 9.8674 | -116.4799 | 8.7013 | 187.4237 | 0.0149 | 0.1334 |
| 2024_09_20 22:00 | 3253965 | 2 | 13.7995 | 8.0433 | -115.9592 | 19.3013 | 126.7573 | 0.0145 | 0.0020 |
| 2024_09_20 22:00 | 3213276 | 3 | 5.5523 | 19.7427 | -115.7248 | 18.2740 | 190.9368 | 0.0189 | 0.0127 |
| 2024_09_20 22:00 | 3265467 | 4 | 17.6541 | 5.6819 | -114.3315 | 8.2599 | 150.9218 | 0.0145 | 0.0077 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414634_E434C70F | 504990 | 486 | -88.8 | 504990 | 243 | -94.9 | 504990 | 359 | -88.9 | 504990 | 675 |
| MR_1774414634_1FB77332 | 504990 | 486 | -88.0 | 504990 | 243 | -94.0 | 504990 | 359 | -89.9 | 504990 | 675 |
| MR_1774414634_692630A1 | 504990 | 243 | -93.3 | 504990 | 486 | -86.8 | 504990 | 359 | -91.2 | 504990 | 675 |
| MR_1774414634_6ABFDA53 | 504990 | 486 | -88.1 | 504990 | 243 | -92.9 | 504990 | 359 | -88.8 | 504990 | 675 |
| MR_1774414634_BE50F1D7 | 504990 | 243 | -93.4 | 504990 | 486 | -89.6 | 504990 | 359 | -89.6 | 504990 | 675 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1509: `42c6d29e-20b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `42c6d29e-20b6-45b1-8fd7-35df5997a6b5` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3212653_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1509] topology](images/train_1509.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231373_2
- `C2`: Adjust the azimuth of 3212653_1 by 49 degrees
- `C3`: Increase A3 Offset threshold for 3212653_1
- `C4`: Increase A3 Offset threshold for 3231373_2
- `C5`: Lift the tilt angle of 3212653_1 by 3 degrees
- `C6`: Add neighbor relationship between 3212653_1 and 3231373_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212653_1
- `C8`: Decrease transmission power for 3231373_2
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Add neighbor relationship between 3216761_3 and 3231373_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212653_1 **← 정답**
- `C12`: Increase transmission power for 3212653_1
- `C13`: Press down the tilt angle  of 3231373_2 by 10 degrees
- `C14`: Increase transmission power for 3231373_2
- `C15`: Lift the tilt angle  of 3231373_2 by 10 degrees
- `C16`: Press down the tilt angle of 3212653_1 by 3 degrees
- `C17`: Adjust the azimuth of 3231373_2 by 50 degrees
- `C18`: Decrease A3 Offset threshold for 3231373_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231373_2
- `C20`: Decrease transmission power for 3212653_1
- `C21`: Check test server and transmission issues
- `C22`: Decrease A3 Offset threshold for 3212653_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.961 | MS1 | 121.4656591737 | 31.1446356105 | 712 | 504990 | -86.47 | 16.73 | 514.24 | 0.18 | 2.40 | 1592 |
| 2024-09-20 22:21:32.447 | MS1 | 121.4656596926 | 31.1446202418 | 712 | 504990 | -88.85 | 16.71 | 505.05 | 0.08 | 2.15 | 1600 |
| 2024-09-20 22:21:33.577 | MS1 | 121.4656657031 | 31.1446209304 | 712 | 504990 | -87.98 | 12.54 | 462.80 | 0.04 | 2.36 | 1561 |
| 2024-09-20 22:21:34.118 | MS1 | 121.4656676888 | 31.1446327691 | 712 | 504990 | -89.21 | 14.67 | 93.47 | 0.52 | 2.80 | 526 |
| 2024-09-20 22:21:35.593 | MS1 | 121.4656749304 | 31.1446377033 | 712 | 504990 | -91.68 | 14.79 | 60.90 | 0.64 | 2.02 | 631 |
| 2024-09-20 22:21:36.475 | MS1 | 121.4656752446 | 31.1446191211 | 712 | 504990 | -88.35 | 17.88 | 99.30 | 0.62 | 2.65 | 537 |
| 2024-09-20 22:21:37.972 | MS1 | 121.4656650446 | 31.1446282129 | 712 | 504990 | -89.47 | 7.02 | 81.58 | 0.64 | 2.37 | 614 |
| 2024-09-20 22:21:38.424 | MS1 | 121.4656624780 | 31.1446188114 | 712 | 504990 | -90.55 | 8.90 | 60.11 | 0.59 | 2.51 | 652 |
| 2024-09-20 22:21:39.440 | MS1 | 121.4656672558 | 31.1446271061 | 712 | 504990 | -93.72 | 11.49 | 90.15 | 0.54 | 2.81 | 507 |
| 2024-09-20 22:21:40.787 | MS1 | 121.4656719718 | 31.1446249463 | 712 | 504990 | -92.00 | 8.63 | 500.68 | 0.09 | 2.83 | 1597 |
| 2024-09-20 22:21:41.991 | MS1 | 121.4656744738 | 31.1446242061 | 712 | 504990 | -92.01 | 11.57 | 598.57 | 0.13 | 2.10 | 1575 |
| 2024-09-20 22:21:42.835 | MS1 | 121.4656743651 | 31.1446349939 | 712 | 504990 | -91.05 | 8.65 | 401.91 | 0.04 | 2.52 | 1571 |

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
| 3212653 | 1 | 121.4679234239 | 31.1551868760 | 239 | 2 | 10 | 26.5 | TDD | 712 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3216761 | 3 | 121.4690951734 | 31.1529606038 | 206 | 15 | 5 | 49.3 | TDD | 972 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3231373 | 2 | 121.4642420593 | 31.1503309755 | 3 | 10 | 11 | 27.2 | TDD | 371 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3262317 | 4 | 121.4741042858 | 31.1551298756 | 323 | 11 | 9 | 48.9 | TDD | 662 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.142 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.167 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.274 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.274 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.953 | NREventA3 | measId:2;ServCellPCI:973;Se... |
| 2024-09-20 22:21:38.193 | NRHandoverAttempt | SourcePCI:973;SourceNR-ARFC... |
| 2024-09-20 22:21:38.225 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.238 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.366 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.366 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212653 | 1 | 15.7819 | 18.8130 | -114.1331 | 10.8364 | 133.9220 | 0.0006 | 0.0188 |
| 2024_09_20 22:00 | 3231373 | 2 | 19.4630 | 14.1536 | -116.3824 | 19.1706 | 171.2840 | 0.0025 | 0.0126 |
| 2024_09_20 22:00 | 3216761 | 3 | 16.5326 | 14.0615 | -114.3300 | 16.7324 | 132.4914 | 0.0157 | 0.0166 |
| 2024_09_20 22:00 | 3262317 | 4 | 9.4446 | 15.1307 | -116.2473 | 18.8920 | 124.0411 | 0.0184 | 0.0200 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415534_05A03885 | 504990 | 712 | -87.2 | 504990 | 371 | -91.6 | 504990 | 972 | -99.0 | 504990 | 662 |
| MR_1774415534_6FA4B10A | 504990 | 712 | -87.3 | 504990 | 371 | -95.1 | 504990 | 972 | -100.2 | 504990 | 662 |
| MR_1774415534_EE1850EF | 504990 | 712 | -88.1 | 504990 | 371 | -95.0 | 504990 | 972 | -100.0 | 504990 | 662 |
| MR_1774415534_86488C23 | 504990 | 712 | -87.4 | 504990 | 371 | -92.7 | 504990 | 972 | -100.3 | 504990 | 662 |
| MR_1774415534_C01CE677 | 504990 | 712 | -89.9 | 504990 | 371 | -92.8 | 504990 | 972 | -97.5 | 504990 | 662 |

> *... 2개 열 생략 (전체 14열)*

---
