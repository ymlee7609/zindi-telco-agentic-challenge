# Track A 문제 분석 — train[1960]~train[1969]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1960] ~ train[1969] (10개)

## 목차

1. [문제 1960: `1eacbeda-cfe...`](#1960) — single-answer, 정답: C19
2. [문제 1961: `a6bdb417-4fc...`](#1961) — single-answer, 정답: C2
3. [문제 1962: `dda52d39-496...`](#1962) — single-answer, 정답: C14
4. [문제 1963: `cd38b1f0-548...`](#1963) — single-answer, 정답: C6
5. [문제 1964: `5d373a10-c32...`](#1964) — single-answer, 정답: C7
6. [문제 1965: `d0a9511b-5fa...`](#1965) — single-answer, 정답: C6
7. [문제 1966: `07ac0f13-956...`](#1966) — single-answer, 정답: C20
8. [문제 1967: `21a33ab4-0cd...`](#1967) — single-answer, 정답: C20
9. [문제 1968: `2dc71a1e-d2b...`](#1968) — single-answer, 정답: C7
10. [문제 1969: `fcbba56b-a46...`](#1969) — single-answer, 정답: C9

---

### 문제 1960: `1eacbeda-cfe...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1eacbeda-cfe3-432a-9dfc-d99697d149ac` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Decrease A3 Offset threshold for 3255403_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1960] topology](images/train_1960.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255403_1
- `C2`: Add neighbor relationship between 3227300_2 and 3219887_4
- `C3`: Adjust the azimuth of 3255403_1 by 50 degrees
- `C4`: Lift the tilt angle  of 3219887_4 by 10 degrees
- `C5`: Press down the tilt angle of 3255403_1 by 6 degrees
- `C6`: Press down the tilt angle  of 3219887_4 by 10 degrees
- `C7`: Decrease transmission power for 3255403_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease transmission power for 3219887_4
- `C10`: Decrease A3 Offset threshold for 3219887_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219887_4
- `C12`: Add neighbor relationship between 3255403_1 and 3219887_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219887_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255403_1
- `C15`: Increase transmission power for 3219887_4
- `C16`: Increase transmission power for 3255403_1
- `C17`: Increase A3 Offset threshold for 3219887_4
- `C18`: Adjust the azimuth of 3219887_4 by 43 degrees
- `C19`: Decrease A3 Offset threshold for 3255403_1 **← 정답**
- `C20`: Check test server and transmission issues
- `C21`: Lift the tilt angle of 3255403_1 by 6 degrees
- `C22`: Increase A3 Offset threshold for 3255403_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.154 | MS1 | 121.4656612837 | 31.1446193165 | 234 | 504990 | -79.95 | 12.91 | 459.22 | 0.15 | 2.57 | 1600 |
| 2024-09-20 22:21:32.873 | MS1 | 121.4656738208 | 31.1446341119 | 234 | 504990 | -84.77 | 13.50 | 456.45 | 0.17 | 2.18 | 1595 |
| 2024-09-20 22:21:33.751 | MS1 | 121.4656588166 | 31.1446250021 | 234 | 504990 | -77.95 | 15.03 | 311.66 | 0.12 | 2.46 | 1600 |
| 2024-09-20 22:21:34.538 | MS1 | 121.4656652739 | 31.1446326249 | 234 | 504990 | -89.89 | -3.64 | 71.01 | 0.18 | 1.42 | 1593 |
| 2024-09-20 22:21:35.151 | MS1 | 121.4656660546 | 31.1446188881 | 234 | 504990 | -88.99 | -1.10 | 59.49 | 0.04 | 1.40 | 1582 |
| 2024-09-20 22:21:36.832 | MS1 | 121.4656668102 | 31.1446336522 | 234 | 504990 | -88.65 | -1.47 | 79.66 | 0.06 | 1.06 | 1575 |
| 2024-09-20 22:21:37.765 | MS1 | 121.4656680333 | 31.1446302980 | 234 | 504990 | -89.16 | -2.80 | 31.66 | 0.09 | 1.02 | 1578 |
| 2024-09-20 22:21:38.563 | MS1 | 121.4656754188 | 31.1446356130 | 234 | 504990 | -92.13 | -1.84 | 48.54 | 0.19 | 1.06 | 1564 |
| 2024-09-20 22:21:39.618 | MS1 | 121.4656655194 | 31.1446213193 | 742 | 504990 | -83.57 | 16.50 | 239.03 | 0.17 | 1.26 | 1581 |
| 2024-09-20 22:21:40.734 | MS1 | 121.4656735651 | 31.1446322730 | 742 | 504990 | -75.10 | 16.99 | 495.67 | 0.09 | 2.88 | 1579 |
| 2024-09-20 22:21:41.241 | MS1 | 121.4656765470 | 31.1446346539 | 742 | 504990 | -75.71 | 16.84 | 563.87 | 0.20 | 2.30 | 1581 |
| 2024-09-20 22:21:42.214 | MS1 | 121.4656760328 | 31.1446227263 | 742 | 504990 | -82.16 | 13.36 | 339.77 | 0.14 | 2.02 | 1576 |

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
| 3219887 | 4 | 121.4698207773 | 31.1510755955 | 252 | 14 | 0 | 18.9 | TDD | 742 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3220567 | 3 | 121.4650059375 | 31.1497380076 | 312 | 4 | 7 | 15.4 | TDD | 861 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3227300 | 2 | 121.4700404043 | 31.1473589167 | 343 | 2 | 1 | 31.9 | TDD | 851 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3255403 | 1 | 121.4745503203 | 31.1464943993 | 82 | 5 | 6 | 21.8 | TDD | 234 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.450 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.465 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.594 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.594 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.336 | NREventA3 | measId:2;ServCellPCI:266;Se... |
| 2024-09-20 22:21:38.576 | NRHandoverAttempt | SourcePCI:266;SourceNR-ARFC... |
| 2024-09-20 22:21:38.624 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.636 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.764 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.764 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255403 | 1 | 17.0014 | 16.4162 | -117.0338 | 6.1066 | 142.6182 | 0.0195 | 0.1890 |
| 2024_09_20 22:00 | 3227300 | 2 | 15.2298 | 10.8314 | -116.8353 | 13.0361 | 186.7013 | 0.0155 | 0.0014 |
| 2024_09_20 22:00 | 3220567 | 3 | 7.5853 | 5.0920 | -115.6593 | 12.1079 | 143.5642 | 0.0053 | 0.0154 |
| 2024_09_20 22:00 | 3219887 | 4 | 11.6558 | 9.1615 | -117.2658 | 15.2768 | 140.1383 | 0.0076 | 0.0036 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412977_5F2690C7 | 504990 | 742 | -83.9 | 504990 | 234 | -88.7 | 504990 | 851 | -89.3 | 504990 | 861 |
| MR_1774412977_58EBA5AE | 504990 | 742 | -85.8 | 504990 | 234 | -90.7 | 504990 | 851 | -88.9 | 504990 | 861 |
| MR_1774412977_72908CB6 | 504990 | 742 | -86.0 | 504990 | 234 | -90.4 | 504990 | 851 | -88.7 | 504990 | 861 |
| MR_1774412977_78D5E0F5 | 504990 | 234 | -90.6 | 504990 | 742 | -85.5 | 504990 | 851 | -91.0 | 504990 | 861 |
| MR_1774412977_06C58C3A | 504990 | 234 | -88.4 | 504990 | 742 | -85.2 | 504990 | 851 | -92.3 | 504990 | 861 |
| MR_1774412977_E0CEC29E | 504990 | 742 | -84.5 | 504990 | 234 | -88.3 | 504990 | 851 | -92.2 | 504990 | 861 |
| MR_1774412977_CE29A49D | 504990 | 234 | -91.6 | 504990 | 742 | -84.5 | 504990 | 851 | -90.4 | 504990 | 861 |
| MR_1774412977_54878182 | 504990 | 234 | -91.6 | 504990 | 742 | -86.1 | 504990 | 851 | -91.6 | 504990 | 861 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1961: `a6bdb417-4fc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a6bdb417-4fc7-4a59-bdde-e8d27d153115` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1961] topology](images/train_1961.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275811_3
- `C2`: Check test server and transmission issues **← 정답**
- `C3`: Add neighbor relationship between 3226531_4 and 3275811_3
- `C4`: Decrease A3 Offset threshold for 3226531_4
- `C5`: Press down the tilt angle  of 3275811_3 by 10 degrees
- `C6`: Adjust the azimuth of 3275811_3 by 50 degrees
- `C7`: Increase transmission power for 3275811_3
- `C8`: Adjust the azimuth of 3226531_4 by 3 degrees
- `C9`: Lift the tilt angle  of 3275811_3 by 10 degrees
- `C10`: Decrease transmission power for 3275811_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275811_3
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Lift the tilt angle of 3226531_4 by 9 degrees
- `C14`: Increase A3 Offset threshold for 3226531_4
- `C15`: Increase transmission power for 3226531_4
- `C16`: Add neighbor relationship between 3220115_1 and 3275811_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226531_4
- `C18`: Press down the tilt angle of 3226531_4 by 9 degrees
- `C19`: Increase A3 Offset threshold for 3275811_3
- `C20`: Decrease transmission power for 3226531_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226531_4
- `C22`: Decrease A3 Offset threshold for 3275811_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.792 | MS1 | 121.4656779617 | 31.1446342548 | 574 | 504990 | -91.57 | 14.11 | 389.89 | 0.11 | 2.98 | 1587 |
| 2024-09-20 22:21:32.820 | MS1 | 121.4656595223 | 31.1446269611 | 574 | 504990 | -90.48 | 16.03 | 352.32 | 0.00 | 2.46 | 1596 |
| 2024-09-20 22:21:33.649 | MS1 | 121.4656666756 | 31.1446297709 | 574 | 504990 | -88.71 | 13.65 | 317.80 | 0.02 | 2.17 | 1596 |
| 2024-09-20 22:21:34.625 | MS1 | 121.4656683693 | 31.1446349757 | 574 | 504990 | -91.74 | 17.39 | 86.96 | 0.18 | 2.22 | 386 |
| 2024-09-20 22:21:35.814 | MS1 | 121.4656597017 | 31.1446299266 | 574 | 504990 | -90.20 | 17.80 | 56.35 | 0.10 | 2.90 | 369 |
| 2024-09-20 22:21:36.401 | MS1 | 121.4656614191 | 31.1446269822 | 574 | 504990 | -85.85 | 12.64 | 78.55 | 0.04 | 2.63 | 343 |
| 2024-09-20 22:21:37.329 | MS1 | 121.4656604592 | 31.1446274327 | 574 | 504990 | -90.13 | 7.92 | 63.45 | 0.12 | 2.45 | 483 |
| 2024-09-20 22:21:38.424 | MS1 | 121.4656602361 | 31.1446302177 | 574 | 504990 | -89.46 | 11.60 | 58.76 | 0.17 | 2.39 | 485 |
| 2024-09-20 22:21:39.583 | MS1 | 121.4656642646 | 31.1446295723 | 574 | 504990 | -93.43 | 11.98 | 77.94 | 0.04 | 2.82 | 392 |
| 2024-09-20 22:21:40.285 | MS1 | 121.4656705621 | 31.1446196832 | 574 | 504990 | -89.25 | 8.29 | 480.49 | 0.03 | 2.17 | 1590 |
| 2024-09-20 22:21:41.714 | MS1 | 121.4656588760 | 31.1446233441 | 574 | 504990 | -92.56 | 12.72 | 410.32 | 0.05 | 2.28 | 1599 |
| 2024-09-20 22:21:42.960 | MS1 | 121.4656668182 | 31.1446213171 | 574 | 504990 | -89.79 | 10.66 | 523.05 | 0.07 | 2.01 | 1585 |

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
| 3220115 | 1 | 121.4707953881 | 31.1556069147 | 226 | 14 | 1 | 17.0 | TDD | 584 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3226531 | 4 | 121.4730516960 | 31.1513382041 | 226 | 7 | 4 | 43.7 | TDD | 574 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3243392 | 2 | 121.4711450056 | 31.1522897969 | 163 | 9 | 8 | 22.7 | TDD | 529 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3275811 | 3 | 121.4663487187 | 31.1457763684 | 44 | 2 | 7 | 31.6 | TDD | 818 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.192 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.210 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.314 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.314 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.052 | NREventA3 | measId:2;ServCellPCI:830;Se... |
| 2024-09-20 22:21:38.292 | NRHandoverAttempt | SourcePCI:830;SourceNR-ARFC... |
| 2024-09-20 22:21:38.327 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.340 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.478 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.478 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220115 | 1 | 16.4227 | 19.2892 | -115.4274 | 10.0196 | 162.9476 | 0.0049 | 0.0057 |
| 2024_09_20 22:00 | 3243392 | 2 | 11.2126 | 7.4851 | -114.6494 | 6.4060 | 199.2232 | 0.0071 | 0.0092 |
| 2024_09_20 22:00 | 3275811 | 3 | 14.6201 | 7.2164 | -117.3375 | 14.2390 | 119.0995 | 0.0172 | 0.0020 |
| 2024_09_20 22:00 | 3226531 | 4 | 17.1411 | 9.1867 | -115.3100 | 15.0935 | 81.7582 | 0.0107 | 0.0145 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414061_7C7DB6FF | 504990 | 574 | -91.9 | 504990 | 818 | -99.3 | 504990 | 584 | -101.9 | 504990 | 529 |
| MR_1774414061_B43A3FC7 | 504990 | 574 | -89.9 | 504990 | 818 | -99.9 | 504990 | 584 | -102.7 | 504990 | 529 |
| MR_1774414061_E9D5C6C9 | 504990 | 574 | -90.3 | 504990 | 818 | -98.2 | 504990 | 584 | -104.8 | 504990 | 529 |
| MR_1774414061_EAB6420D | 504990 | 574 | -92.5 | 504990 | 818 | -101.3 | 504990 | 584 | -105.0 | 504990 | 529 |
| MR_1774414061_6E6BC0A3 | 504990 | 574 | -92.2 | 504990 | 818 | -99.9 | 504990 | 584 | -103.3 | 504990 | 529 |
| MR_1774414061_34828995 | 504990 | 574 | -90.6 | 504990 | 818 | -102.0 | 504990 | 584 | -102.4 | 504990 | 529 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1962: `dda52d39-496...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dda52d39-4963-4e1e-929a-583077ab940e` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Lift the tilt angle  of 3279124_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1962] topology](images/train_1962.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229642_1
- `C2`: Decrease A3 Offset threshold for 3229642_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase A3 Offset threshold for 3272899_3
- `C5`: Adjust the azimuth of 3279124_4 by 50 degrees
- `C6`: Check test server and transmission issues
- `C7`: Press down the tilt angle  of 3279124_4 by 10 degrees
- `C8`: Lift the tilt angle of 3272899_3 by 4 degrees
- `C9`: Decrease transmission power for 3272899_3
- `C10`: Decrease A3 Offset threshold for 3272899_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272899_3
- `C12`: Increase transmission power for 3229642_1
- `C13`: Press down the tilt angle of 3272899_3 by 4 degrees
- `C14`: Lift the tilt angle  of 3279124_4 by 10 degrees **← 정답**
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229642_1
- `C16`: Increase transmission power for 3272899_3
- `C17`: Increase A3 Offset threshold for 3229642_1
- `C18`: Add neighbor relationship between 3272899_3 and 3229642_1
- `C19`: Add neighbor relationship between 3279124_4 and 3229642_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272899_3
- `C21`: Adjust the azimuth of 3272899_3 by 24 degrees
- `C22`: Decrease transmission power for 3229642_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.658 | MS1 | 121.4656746980 | 31.1446358687 | 4 | 504990 | -90.34 | 17.52 | 348.30 | 0.12 | 2.32 | 1584 |
| 2024-09-20 22:21:32.774 | MS1 | 121.4656659946 | 31.1446349140 | 4 | 504990 | -91.02 | 12.45 | 527.36 | 0.12 | 2.92 | 1560 |
| 2024-09-20 22:21:33.841 | MS1 | 121.4656627592 | 31.1446190608 | 4 | 504990 | -91.28 | 16.55 | 399.24 | 0.18 | 2.23 | 1598 |
| 2024-09-20 22:21:34.296 | MS1 | 121.4656605115 | 31.1446375559 | 4 | 504990 | -86.10 | 16.54 | 69.70 | 0.03 | 2.82 | 1588 |
| 2024-09-20 22:21:35.298 | MS1 | 121.4656723830 | 31.1446270492 | 4 | 504990 | -90.64 | 15.65 | 91.86 | 0.19 | 2.31 | 1568 |
| 2024-09-20 22:21:36.534 | MS1 | 121.4656621664 | 31.1446202027 | 4 | 504990 | -88.58 | 15.44 | 95.39 | 0.18 | 2.49 | 1596 |
| 2024-09-20 22:21:37.335 | MS1 | 121.4656594975 | 31.1446206235 | 4 | 504990 | -93.80 | 11.97 | 73.90 | 0.10 | 2.88 | 1594 |
| 2024-09-20 22:21:38.217 | MS1 | 121.4656607283 | 31.1446285271 | 4 | 504990 | -92.16 | 7.12 | 90.97 | 0.11 | 2.60 | 1567 |
| 2024-09-20 22:21:39.824 | MS1 | 121.4656727345 | 31.1446323385 | 4 | 504990 | -90.06 | 7.79 | 93.33 | 0.14 | 2.52 | 1580 |
| 2024-09-20 22:21:40.435 | MS1 | 121.4656628958 | 31.1446357177 | 4 | 504990 | -89.40 | 10.55 | 311.35 | 0.16 | 2.87 | 1598 |
| 2024-09-20 22:21:41.825 | MS1 | 121.4656733040 | 31.1446188352 | 4 | 504990 | -89.12 | 12.41 | 572.63 | 0.14 | 2.47 | 1596 |
| 2024-09-20 22:21:42.465 | MS1 | 121.4656763844 | 31.1446265858 | 4 | 504990 | -91.85 | 11.28 | 358.67 | 0.03 | 2.21 | 1572 |

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
| 3229642 | 1 | 121.4664061765 | 31.1457210203 | 261 | 14 | 10 | 21.7 | TDD | 171 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3243788 | 2 | 121.4755866059 | 31.1544034860 | 197 | 6 | 0 | 39.6 | TDD | 164 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3272899 | 3 | 121.4713510830 | 31.1555679511 | 228 | 3 | 1 | 30.0 | TDD | 4 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3279124 | 4 | 121.4707377158 | 31.1456662663 | 163 | 9 | 1 | 19.5 | TDD | 701 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.375 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.396 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.505 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.505 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.196 | NREventA3 | measId:2;ServCellPCI:697;Se... |
| 2024-09-20 22:21:38.436 | NRHandoverAttempt | SourcePCI:697;SourceNR-ARFC... |
| 2024-09-20 22:21:38.484 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.497 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.608 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.608 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229642 | 1 | 9.1796 | 8.4563 | -114.0566 | 10.9862 | 181.5812 | 0.0165 | 0.0187 |
| 2024_09_20 22:00 | 3243788 | 2 | 13.0561 | 13.9256 | -115.4352 | 6.0319 | 142.0956 | 0.0128 | 0.0036 |
| 2024_09_20 22:00 | 3272899 | 3 | 78.0449 | 75.4610 | -117.8925 | 9.4151 | 148.4819 | 0.0135 | 0.0017 |
| 2024_09_20 22:00 | 3279124 | 4 | 7.0306 | 12.2297 | -116.7995 | 19.4531 | 151.1279 | 0.0195 | 0.0172 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413167_F1474721 | 504990 | 4 | -87.8 | 504990 | 171 | -89.1 | 504990 | 701 | -95.0 | 504990 | 164 |
| MR_1774413167_F84D1A4E | 504990 | 4 | -87.7 | 504990 | 171 | -88.0 | 504990 | 701 | -93.4 | 504990 | 164 |
| MR_1774413167_641F47C7 | 504990 | 4 | -86.3 | 504990 | 171 | -90.0 | 504990 | 701 | -96.2 | 504990 | 164 |
| MR_1774413167_C2603D71 | 504990 | 4 | -88.0 | 504990 | 171 | -88.0 | 504990 | 701 | -95.3 | 504990 | 164 |
| MR_1774413167_612FB829 | 504990 | 4 | -85.9 | 504990 | 171 | -89.0 | 504990 | 701 | -95.3 | 504990 | 164 |
| MR_1774413167_9F74A4C8 | 504990 | 4 | -85.5 | 504990 | 171 | -88.1 | 504990 | 701 | -96.0 | 504990 | 164 |
| MR_1774413167_430DF3E1 | 504990 | 4 | -87.8 | 504990 | 171 | -89.0 | 504990 | 701 | -93.6 | 504990 | 164 |
| MR_1774413167_D9741A3C | 504990 | 4 | -84.5 | 504990 | 171 | -87.5 | 504990 | 701 | -95.5 | 504990 | 164 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1963: `cd38b1f0-548...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cd38b1f0-5480-4b85-9a3a-687f0c38ccb9` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease A3 Offset threshold for 3270205_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1963] topology](images/train_1963.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270205_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270205_3
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase transmission power for 3270205_3
- `C5`: Lift the tilt angle of 3270205_3 by 6 degrees
- `C6`: Decrease A3 Offset threshold for 3270205_3 **← 정답**
- `C7`: Adjust the azimuth of 3260272_2 by 50 degrees
- `C8`: Add neighbor relationship between 3269822_1 and 3260272_2
- `C9`: Increase A3 Offset threshold for 3270205_3
- `C10`: Decrease transmission power for 3270205_3
- `C11`: Press down the tilt angle  of 3260272_2 by 10 degrees
- `C12`: Add neighbor relationship between 3270205_3 and 3260272_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260272_2
- `C14`: Increase A3 Offset threshold for 3260272_2
- `C15`: Press down the tilt angle of 3270205_3 by 6 degrees
- `C16`: Increase transmission power for 3260272_2
- `C17`: Adjust the azimuth of 3270205_3 by 50 degrees
- `C18`: Lift the tilt angle  of 3260272_2 by 10 degrees
- `C19`: Decrease transmission power for 3260272_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260272_2
- `C21`: Decrease A3 Offset threshold for 3260272_2
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.738 | MS1 | 121.4656707632 | 31.1446302876 | 908 | 504990 | -80.40 | 16.40 | 516.17 | 0.15 | 2.51 | 1599 |
| 2024-09-20 22:21:32.702 | MS1 | 121.4656625602 | 31.1446328456 | 908 | 504990 | -76.50 | 12.43 | 541.31 | 0.02 | 2.02 | 1585 |
| 2024-09-20 22:21:33.648 | MS1 | 121.4656734406 | 31.1446270895 | 908 | 504990 | -83.31 | 15.12 | 551.98 | 0.14 | 2.37 | 1576 |
| 2024-09-20 22:21:34.856 | MS1 | 121.4656641937 | 31.1446245362 | 908 | 504990 | -88.84 | -2.62 | 43.49 | 0.06 | 1.18 | 1574 |
| 2024-09-20 22:21:35.378 | MS1 | 121.4656722464 | 31.1446347032 | 908 | 504990 | -83.18 | -3.64 | 30.22 | 0.10 | 1.48 | 1578 |
| 2024-09-20 22:21:36.417 | MS1 | 121.4656649552 | 31.1446243373 | 908 | 504990 | -88.42 | -3.42 | 55.01 | 0.03 | 1.34 | 1561 |
| 2024-09-20 22:21:37.388 | MS1 | 121.4656687544 | 31.1446236058 | 908 | 504990 | -85.01 | -2.78 | 73.88 | 0.05 | 1.28 | 1572 |
| 2024-09-20 22:21:38.801 | MS1 | 121.4656600968 | 31.1446206683 | 908 | 504990 | -84.64 | -2.13 | 49.46 | 0.11 | 1.35 | 1582 |
| 2024-09-20 22:21:39.855 | MS1 | 121.4656606989 | 31.1446213732 | 395 | 504990 | -84.06 | 14.90 | 259.99 | 0.00 | 1.22 | 1562 |
| 2024-09-20 22:21:40.824 | MS1 | 121.4656621216 | 31.1446329745 | 395 | 504990 | -84.67 | 15.99 | 424.54 | 0.12 | 2.53 | 1585 |
| 2024-09-20 22:21:41.909 | MS1 | 121.4656689309 | 31.1446217276 | 395 | 504990 | -82.52 | 13.77 | 470.14 | 0.16 | 2.08 | 1567 |
| 2024-09-20 22:21:42.528 | MS1 | 121.4656722564 | 31.1446301152 | 395 | 504990 | -84.66 | 13.76 | 389.84 | 0.16 | 2.81 | 1580 |

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
| 3260272 | 2 | 121.4672388711 | 31.1449841029 | 177 | 4 | 11 | 35.8 | TDD | 395 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3261825 | 4 | 121.4755608586 | 31.1460328808 | 200 | 7 | 11 | 40.6 | TDD | 563 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3269822 | 1 | 121.4737891966 | 31.1504043286 | 143 | 9 | 0 | 29.8 | TDD | 889 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3270205 | 3 | 121.4726779330 | 31.1476493154 | 97 | 4 | 4 | 26.8 | TDD | 908 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.877 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.901 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.042 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.042 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.727 | NREventA3 | measId:2;ServCellPCI:102;Se... |
| 2024-09-20 22:21:37.967 | NRHandoverAttempt | SourcePCI:102;SourceNR-ARFC... |
| 2024-09-20 22:21:38.010 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.025 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.130 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.130 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269822 | 1 | 5.6146 | 12.3054 | -114.3442 | 8.7008 | 122.0941 | 0.0053 | 0.0144 |
| 2024_09_20 22:00 | 3260272 | 2 | 10.4333 | 11.9739 | -115.7646 | 17.8464 | 84.6020 | 0.0006 | 0.0089 |
| 2024_09_20 22:00 | 3270205 | 3 | 7.6962 | 10.1214 | -114.0772 | 12.2466 | 150.1781 | 0.0115 | 0.1819 |
| 2024_09_20 22:00 | 3261825 | 4 | 14.5363 | 13.1092 | -117.6922 | 7.3724 | 175.9589 | 0.0067 | 0.0060 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413670_0CDD9845 | 504990 | 908 | -87.3 | 504990 | 395 | -85.1 | 504990 | 889 | -94.4 | 504990 | 563 |
| MR_1774413670_1C266C30 | 504990 | 395 | -84.5 | 504990 | 908 | -88.0 | 504990 | 889 | -92.0 | 504990 | 563 |
| MR_1774413670_72DA1278 | 504990 | 908 | -90.4 | 504990 | 395 | -82.6 | 504990 | 889 | -92.8 | 504990 | 563 |
| MR_1774413670_FC65DD73 | 504990 | 395 | -83.2 | 504990 | 908 | -90.3 | 504990 | 889 | -93.0 | 504990 | 563 |
| MR_1774413670_09FE5D14 | 504990 | 395 | -83.7 | 504990 | 908 | -89.8 | 504990 | 889 | -91.3 | 504990 | 563 |
| MR_1774413670_60AEA380 | 504990 | 395 | -82.3 | 504990 | 908 | -88.8 | 504990 | 889 | -93.4 | 504990 | 563 |
| MR_1774413670_8A6B4954 | 504990 | 395 | -83.3 | 504990 | 908 | -88.9 | 504990 | 889 | -94.2 | 504990 | 563 |
| MR_1774413670_255965D3 | 504990 | 908 | -89.9 | 504990 | 395 | -81.6 | 504990 | 889 | -93.7 | 504990 | 563 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1964: `5d373a10-c32...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5d373a10-c326-425b-bc8b-add6be3463f9` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Lift the tilt angle  of 3229395_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1964] topology](images/train_1964.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3236724_3 by 6 degrees
- `C2`: Decrease transmission power for 3236724_3
- `C3`: Decrease A3 Offset threshold for 3236724_3
- `C4`: Lift the tilt angle of 3236724_3 by 6 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236724_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236724_3
- `C7`: Lift the tilt angle  of 3229395_4 by 10 degrees **← 정답**
- `C8`: Increase A3 Offset threshold for 3230231_2
- `C9`: Increase transmission power for 3236724_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230231_2
- `C11`: Increase A3 Offset threshold for 3236724_3
- `C12`: Decrease transmission power for 3230231_2
- `C13`: Adjust the azimuth of 3236724_3 by 32 degrees
- `C14`: Decrease A3 Offset threshold for 3230231_2
- `C15`: Check test server and transmission issues
- `C16`: Press down the tilt angle  of 3229395_4 by 10 degrees
- `C17`: Increase transmission power for 3230231_2
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Add neighbor relationship between 3236724_3 and 3230231_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230231_2
- `C21`: Add neighbor relationship between 3229395_4 and 3230231_2
- `C22`: Adjust the azimuth of 3229395_4 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.520 | MS1 | 121.4656749861 | 31.1446242496 | 700 | 504990 | -90.22 | 14.92 | 317.41 | 0.07 | 2.55 | 1581 |
| 2024-09-20 22:21:32.973 | MS1 | 121.4656625175 | 31.1446247145 | 700 | 504990 | -91.42 | 15.06 | 330.69 | 0.05 | 2.11 | 1584 |
| 2024-09-20 22:21:33.532 | MS1 | 121.4656704657 | 31.1446295813 | 700 | 504990 | -88.81 | 14.22 | 542.97 | 0.16 | 2.77 | 1582 |
| 2024-09-20 22:21:34.167 | MS1 | 121.4656614885 | 31.1446331551 | 700 | 504990 | -91.34 | 15.91 | 56.55 | 0.06 | 2.48 | 1564 |
| 2024-09-20 22:21:35.581 | MS1 | 121.4656742722 | 31.1446324385 | 700 | 504990 | -90.28 | 13.18 | 74.89 | 0.09 | 2.25 | 1572 |
| 2024-09-20 22:21:36.738 | MS1 | 121.4656633242 | 31.1446319223 | 700 | 504990 | -90.83 | 16.58 | 91.03 | 0.15 | 2.68 | 1564 |
| 2024-09-20 22:21:37.303 | MS1 | 121.4656663000 | 31.1446341451 | 700 | 504990 | -93.69 | 8.23 | 90.83 | 0.11 | 2.14 | 1587 |
| 2024-09-20 22:21:38.257 | MS1 | 121.4656632568 | 31.1446226392 | 700 | 504990 | -93.66 | 9.58 | 81.59 | 0.12 | 2.49 | 1561 |
| 2024-09-20 22:21:39.241 | MS1 | 121.4656723935 | 31.1446193864 | 700 | 504990 | -91.59 | 8.52 | 65.24 | 0.01 | 2.18 | 1570 |
| 2024-09-20 22:21:40.898 | MS1 | 121.4656744152 | 31.1446328865 | 700 | 504990 | -89.00 | 12.35 | 411.40 | 0.19 | 2.24 | 1562 |
| 2024-09-20 22:21:41.316 | MS1 | 121.4656669492 | 31.1446236934 | 700 | 504990 | -91.00 | 8.24 | 463.57 | 0.12 | 2.92 | 1589 |
| 2024-09-20 22:21:42.394 | MS1 | 121.4656760256 | 31.1446266032 | 700 | 504990 | -90.02 | 7.57 | 559.12 | 0.04 | 2.89 | 1591 |

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
| 3229395 | 4 | 121.4664303769 | 31.1457432337 | 157 | 4 | 4 | 44.2 | TDD | 546 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3230231 | 2 | 121.4717629368 | 31.1450687868 | 267 | 13 | 11 | 47.5 | TDD | 650 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3236724 | 3 | 121.4721884808 | 31.1448582277 | 300 | 4 | 7 | 18.6 | TDD | 700 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3274777 | 1 | 121.4750553429 | 31.1538609266 | 214 | 10 | 1 | 46.0 | TDD | 505 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.499 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.599 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.599 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.298 | NREventA3 | measId:2;ServCellPCI:346;Se... |
| 2024-09-20 22:21:38.538 | NRHandoverAttempt | SourcePCI:346;SourceNR-ARFC... |
| 2024-09-20 22:21:38.574 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.586 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.723 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.723 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274777 | 1 | 18.6240 | 12.6223 | -117.8952 | 13.4196 | 126.5082 | 0.0042 | 0.0080 |
| 2024_09_20 22:00 | 3230231 | 2 | 16.7269 | 8.9305 | -114.3039 | 14.2996 | 164.5498 | 0.0076 | 0.0089 |
| 2024_09_20 22:00 | 3236724 | 3 | 83.5155 | 81.7786 | -115.1071 | 12.1391 | 121.9296 | 0.0060 | 0.0081 |
| 2024_09_20 22:00 | 3229395 | 4 | 16.6338 | 18.3179 | -116.3221 | 12.6506 | 136.9328 | 0.0196 | 0.0121 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412633_5ECB514C | 504990 | 700 | -90.6 | 504990 | 650 | -98.4 | 504990 | 546 | -106.5 | 504990 | 505 |
| MR_1774412633_1F1EDCDC | 504990 | 700 | -89.5 | 504990 | 650 | -99.3 | 504990 | 546 | -105.9 | 504990 | 505 |
| MR_1774412633_9802498D | 504990 | 700 | -93.3 | 504990 | 650 | -99.4 | 504990 | 546 | -106.8 | 504990 | 505 |
| MR_1774412633_30C02616 | 504990 | 700 | -92.8 | 504990 | 650 | -97.3 | 504990 | 546 | -104.5 | 504990 | 505 |
| MR_1774412633_6049AC75 | 504990 | 700 | -90.0 | 504990 | 650 | -97.7 | 504990 | 546 | -104.3 | 504990 | 505 |
| MR_1774412633_EB8E9AAC | 504990 | 700 | -89.7 | 504990 | 650 | -98.6 | 504990 | 546 | -106.3 | 504990 | 505 |
| MR_1774412633_6A86C8D6 | 504990 | 700 | -91.2 | 504990 | 650 | -99.6 | 504990 | 546 | -104.2 | 504990 | 505 |
| MR_1774412633_C29C1920 | 504990 | 700 | -93.2 | 504990 | 650 | -99.3 | 504990 | 546 | -106.5 | 504990 | 505 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1965: `d0a9511b-5fa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d0a9511b-5faf-4ed1-903b-1b513e3ae705` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1965] topology](images/train_1965.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3222673_1 by 10 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222673_1
- `C4`: Increase transmission power for 3222673_1
- `C5`: Decrease transmission power for 3222673_1
- `C6`: Check test server and transmission issues **← 정답**
- `C7`: Adjust the azimuth of 3222673_1 by 25 degrees
- `C8`: Add neighbor relationship between 3233724_4 and 3279308_2
- `C9`: Lift the tilt angle  of 3279308_2 by 10 degrees
- `C10`: Press down the tilt angle  of 3279308_2 by 10 degrees
- `C11`: Add neighbor relationship between 3222673_1 and 3279308_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279308_2
- `C13`: Increase transmission power for 3279308_2
- `C14`: Decrease A3 Offset threshold for 3222673_1
- `C15`: Increase A3 Offset threshold for 3222673_1
- `C16`: Press down the tilt angle of 3222673_1 by 10 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279308_2
- `C18`: Decrease transmission power for 3279308_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222673_1
- `C20`: Increase A3 Offset threshold for 3279308_2
- `C21`: Adjust the azimuth of 3279308_2 by 50 degrees
- `C22`: Decrease A3 Offset threshold for 3279308_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.539 | MS1 | 121.4656645959 | 31.1446332840 | 808 | 504990 | -86.29 | 17.02 | 446.01 | 0.19 | 2.27 | 1564 |
| 2024-09-20 22:21:32.245 | MS1 | 121.4656730650 | 31.1446324487 | 808 | 504990 | -87.83 | 15.30 | 517.66 | 0.01 | 2.83 | 1587 |
| 2024-09-20 22:21:33.843 | MS1 | 121.4656772454 | 31.1446282576 | 808 | 504990 | -86.05 | 13.73 | 314.52 | 0.02 | 2.16 | 1567 |
| 2024-09-20 22:21:34.398 | MS1 | 121.4656692098 | 31.1446222925 | 808 | 504990 | -85.23 | 14.78 | 88.16 | 0.09 | 2.00 | 308 |
| 2024-09-20 22:21:35.429 | MS1 | 121.4656679658 | 31.1446242016 | 808 | 504990 | -85.84 | 16.55 | 53.51 | 0.19 | 2.25 | 313 |
| 2024-09-20 22:21:36.132 | MS1 | 121.4656674319 | 31.1446356813 | 808 | 504990 | -85.34 | 17.88 | 64.11 | 0.06 | 2.27 | 493 |
| 2024-09-20 22:21:37.794 | MS1 | 121.4656586206 | 31.1446361519 | 808 | 504990 | -93.28 | 7.66 | 52.59 | 0.13 | 2.61 | 349 |
| 2024-09-20 22:21:38.269 | MS1 | 121.4656744453 | 31.1446249638 | 808 | 504990 | -89.11 | 8.61 | 60.69 | 0.16 | 2.48 | 399 |
| 2024-09-20 22:21:39.806 | MS1 | 121.4656776257 | 31.1446216057 | 808 | 504990 | -92.58 | 10.42 | 45.50 | 0.05 | 2.18 | 447 |
| 2024-09-20 22:21:40.826 | MS1 | 121.4656617056 | 31.1446262499 | 808 | 504990 | -91.98 | 11.85 | 581.42 | 0.07 | 2.09 | 1584 |
| 2024-09-20 22:21:41.757 | MS1 | 121.4656694210 | 31.1446235899 | 808 | 504990 | -89.41 | 11.95 | 322.62 | 0.10 | 2.55 | 1567 |
| 2024-09-20 22:21:42.673 | MS1 | 121.4656745268 | 31.1446196429 | 808 | 504990 | -93.90 | 8.53 | 426.35 | 0.19 | 2.12 | 1564 |

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
| 3218014 | 3 | 121.4646936132 | 31.1521660765 | 307 | 4 | 7 | 48.5 | TDD | 853 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3222673 | 1 | 121.4743084267 | 31.1529041526 | 247 | 10 | 8 | 34.6 | TDD | 808 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3233724 | 4 | 121.4646064721 | 31.1456015702 | 14 | 3 | 1 | 23.2 | TDD | 407 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3279308 | 2 | 121.4677877585 | 31.1529137398 | 347 | 10 | 1 | 26.5 | TDD | 131 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.409 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.425 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.537 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.537 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.243 | NREventA3 | measId:2;ServCellPCI:518;Se... |
| 2024-09-20 22:21:38.483 | NRHandoverAttempt | SourcePCI:518;SourceNR-ARFC... |
| 2024-09-20 22:21:38.517 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.527 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.634 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.634 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222673 | 1 | 9.5198 | 19.8197 | -114.5903 | 9.9680 | 85.9504 | 0.0153 | 0.0004 |
| 2024_09_20 22:00 | 3279308 | 2 | 11.6869 | 13.4386 | -116.8883 | 14.0669 | 171.0604 | 0.0139 | 0.0149 |
| 2024_09_20 22:00 | 3218014 | 3 | 16.8286 | 5.7821 | -116.4561 | 19.1801 | 114.9659 | 0.0033 | 0.0178 |
| 2024_09_20 22:00 | 3233724 | 4 | 17.4806 | 9.1347 | -117.6373 | 11.0560 | 90.6125 | 0.0052 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416570_68B03EEF | 504990 | 808 | -84.6 | 504990 | 131 | -90.7 | 504990 | 407 | -94.5 | 504990 | 853 |
| MR_1774416570_B750EDD6 | 504990 | 808 | -84.5 | 504990 | 131 | -90.2 | 504990 | 407 | -95.1 | 504990 | 853 |
| MR_1774416570_179FC8DA | 504990 | 808 | -85.8 | 504990 | 131 | -90.0 | 504990 | 407 | -96.5 | 504990 | 853 |
| MR_1774416570_330A7484 | 504990 | 808 | -83.5 | 504990 | 131 | -90.7 | 504990 | 407 | -93.4 | 504990 | 853 |
| MR_1774416570_07BCED30 | 504990 | 808 | -85.7 | 504990 | 131 | -89.9 | 504990 | 407 | -94.8 | 504990 | 853 |
| MR_1774416570_9D716C3D | 504990 | 808 | -86.1 | 504990 | 131 | -91.7 | 504990 | 407 | -93.5 | 504990 | 853 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1966: `07ac0f13-956...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `07ac0f13-9565-4b12-8384-7870698541d0` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease A3 Offset threshold for 3219944_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1966] topology](images/train_1966.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3277230_2 and 3278198_1
- `C2`: Check test server and transmission issues
- `C3`: Adjust the azimuth of 3278198_1 by 50 degrees
- `C4`: Add neighbor relationship between 3219944_3 and 3278198_1
- `C5`: Decrease A3 Offset threshold for 3278198_1
- `C6`: Lift the tilt angle  of 3278198_1 by 10 degrees
- `C7`: Decrease transmission power for 3219944_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278198_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219944_3
- `C10`: Lift the tilt angle of 3219944_3 by 10 degrees
- `C11`: Increase transmission power for 3278198_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278198_1
- `C13`: Press down the tilt angle  of 3278198_1 by 10 degrees
- `C14`: Increase transmission power for 3219944_3
- `C15`: Press down the tilt angle of 3219944_3 by 10 degrees
- `C16`: Increase A3 Offset threshold for 3278198_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219944_3
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Adjust the azimuth of 3219944_3 by 50 degrees
- `C20`: Decrease A3 Offset threshold for 3219944_3 **← 정답**
- `C21`: Decrease transmission power for 3278198_1
- `C22`: Increase A3 Offset threshold for 3219944_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.878 | MS1 | 121.4656702718 | 31.1446250832 | 714 | 504990 | -79.20 | 12.49 | 473.85 | 0.18 | 2.18 | 1562 |
| 2024-09-20 22:21:32.995 | MS1 | 121.4656628226 | 31.1446280453 | 714 | 504990 | -75.91 | 14.96 | 464.12 | 0.03 | 2.31 | 1578 |
| 2024-09-20 22:21:33.357 | MS1 | 121.4656631088 | 31.1446231785 | 714 | 504990 | -84.46 | 16.38 | 390.46 | 0.16 | 2.44 | 1598 |
| 2024-09-20 22:21:34.445 | MS1 | 121.4656654941 | 31.1446185069 | 714 | 504990 | -89.88 | -0.35 | 45.98 | 0.01 | 1.12 | 1576 |
| 2024-09-20 22:21:35.391 | MS1 | 121.4656779956 | 31.1446377109 | 714 | 504990 | -88.66 | -0.53 | 54.56 | 0.06 | 1.01 | 1595 |
| 2024-09-20 22:21:36.742 | MS1 | 121.4656665055 | 31.1446272405 | 714 | 504990 | -91.38 | -0.02 | 30.80 | 0.07 | 1.19 | 1585 |
| 2024-09-20 22:21:37.200 | MS1 | 121.4656701539 | 31.1446335463 | 714 | 504990 | -84.23 | -2.93 | 22.05 | 0.03 | 1.31 | 1598 |
| 2024-09-20 22:21:38.551 | MS1 | 121.4656713205 | 31.1446361074 | 714 | 504990 | -86.42 | -1.73 | 29.52 | 0.07 | 1.48 | 1591 |
| 2024-09-20 22:21:39.697 | MS1 | 121.4656704555 | 31.1446189895 | 632 | 504990 | -83.82 | 13.95 | 167.90 | 0.16 | 1.27 | 1562 |
| 2024-09-20 22:21:40.953 | MS1 | 121.4656653763 | 31.1446240822 | 632 | 504990 | -79.08 | 12.95 | 559.04 | 0.16 | 2.80 | 1583 |
| 2024-09-20 22:21:41.282 | MS1 | 121.4656685461 | 31.1446280220 | 632 | 504990 | -84.35 | 17.35 | 590.09 | 0.10 | 2.47 | 1562 |
| 2024-09-20 22:21:42.435 | MS1 | 121.4656724979 | 31.1446310895 | 632 | 504990 | -78.41 | 16.64 | 465.44 | 0.02 | 2.28 | 1598 |

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
| 3219944 | 3 | 121.4678881147 | 31.1515614651 | 311 | 14 | 7 | 21.2 | TDD | 714 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3270987 | 4 | 121.4693076258 | 31.1518218022 | 202 | 11 | 10 | 22.7 | TDD | 838 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3277230 | 2 | 121.4682022692 | 31.1505698532 | 324 | 9 | 11 | 44.4 | TDD | 17 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3278198 | 1 | 121.4683904170 | 31.1528737085 | 60 | 11 | 2 | 39.2 | TDD | 632 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.616 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.640 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.741 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.741 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.430 | NREventA3 | measId:2;ServCellPCI:873;Se... |
| 2024-09-20 22:21:38.670 | NRHandoverAttempt | SourcePCI:873;SourceNR-ARFC... |
| 2024-09-20 22:21:38.710 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.720 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.821 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.821 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278198 | 1 | 13.2379 | 7.6426 | -117.8765 | 18.0833 | 128.5068 | 0.0047 | 0.0161 |
| 2024_09_20 22:00 | 3277230 | 2 | 18.6960 | 18.5907 | -116.1119 | 17.3992 | 187.9308 | 0.0112 | 0.0173 |
| 2024_09_20 22:00 | 3219944 | 3 | 17.9743 | 12.2376 | -114.6424 | 8.7434 | 157.6462 | 0.0180 | 0.1711 |
| 2024_09_20 22:00 | 3270987 | 4 | 8.8705 | 12.0468 | -114.3482 | 12.4147 | 102.2798 | 0.0068 | 0.0173 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412195_FD08F0A1 | 504990 | 632 | -85.3 | 504990 | 714 | -91.4 | 504990 | 17 | -87.6 | 504990 | 838 |
| MR_1774412195_42E7EE98 | 504990 | 714 | -90.9 | 504990 | 632 | -85.4 | 504990 | 17 | -86.6 | 504990 | 838 |
| MR_1774412195_8C465786 | 504990 | 714 | -88.7 | 504990 | 632 | -83.9 | 504990 | 17 | -86.7 | 504990 | 838 |
| MR_1774412195_F7C79852 | 504990 | 714 | -89.8 | 504990 | 632 | -85.4 | 504990 | 17 | -86.7 | 504990 | 838 |
| MR_1774412195_E5346D5E | 504990 | 714 | -90.3 | 504990 | 632 | -86.7 | 504990 | 17 | -85.8 | 504990 | 838 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1967: `21a33ab4-0cd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `21a33ab4-0cd3-4be3-9565-dab9eeb04508` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1967] topology](images/train_1967.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3273090_2
- `C2`: Lift the tilt angle of 3266203_1 by 10 degrees
- `C3`: Adjust the azimuth of 3273090_2 by 50 degrees
- `C4`: Increase A3 Offset threshold for 3266203_1
- `C5`: Press down the tilt angle of 3266203_1 by 10 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266203_1
- `C7`: Press down the tilt angle  of 3273090_2 by 10 degrees
- `C8`: Increase A3 Offset threshold for 3273090_2
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Lift the tilt angle  of 3273090_2 by 10 degrees
- `C11`: Adjust the azimuth of 3266203_1 by 50 degrees
- `C12`: Add neighbor relationship between 3242199_3 and 3273090_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273090_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273090_2
- `C15`: Increase transmission power for 3273090_2
- `C16`: Increase transmission power for 3266203_1
- `C17`: Add neighbor relationship between 3266203_1 and 3273090_2
- `C18`: Decrease transmission power for 3266203_1
- `C19`: Decrease transmission power for 3273090_2
- `C20`: Check test server and transmission issues **← 정답**
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266203_1
- `C22`: Decrease A3 Offset threshold for 3266203_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.303 | MS1 | 121.4656778235 | 31.1446204540 | 58 | 504990 | -89.15 | 13.45 | 482.29 | 0.14 | 2.47 | 1595 |
| 2024-09-20 22:21:32.898 | MS1 | 121.4656743774 | 31.1446243887 | 58 | 504990 | -87.75 | 14.63 | 510.62 | 0.13 | 2.71 | 1600 |
| 2024-09-20 22:21:33.490 | MS1 | 121.4656644658 | 31.1446201919 | 58 | 504990 | -87.01 | 14.22 | 512.37 | 0.01 | 2.16 | 1587 |
| 2024-09-20 22:21:34.795 | MS1 | 121.4656754671 | 31.1446350578 | 58 | 504990 | -86.86 | 16.95 | 52.95 | 0.12 | 2.37 | 393 |
| 2024-09-20 22:21:35.839 | MS1 | 121.4656721740 | 31.1446300459 | 58 | 504990 | -88.69 | 12.96 | 75.27 | 0.13 | 2.24 | 426 |
| 2024-09-20 22:21:36.316 | MS1 | 121.4656604546 | 31.1446245388 | 58 | 504990 | -89.10 | 15.41 | 60.64 | 0.14 | 2.47 | 447 |
| 2024-09-20 22:21:37.466 | MS1 | 121.4656726635 | 31.1446276371 | 58 | 504990 | -90.78 | 8.70 | 96.91 | 0.03 | 2.62 | 432 |
| 2024-09-20 22:21:38.974 | MS1 | 121.4656716908 | 31.1446339767 | 58 | 504990 | -90.41 | 7.31 | 53.14 | 0.18 | 2.13 | 390 |
| 2024-09-20 22:21:39.619 | MS1 | 121.4656659024 | 31.1446312973 | 58 | 504990 | -90.85 | 11.91 | 63.17 | 0.18 | 2.53 | 354 |
| 2024-09-20 22:21:40.690 | MS1 | 121.4656609917 | 31.1446244269 | 58 | 504990 | -91.75 | 12.72 | 417.00 | 0.03 | 2.78 | 1575 |
| 2024-09-20 22:21:41.790 | MS1 | 121.4656703550 | 31.1446235226 | 58 | 504990 | -93.81 | 10.96 | 325.58 | 0.09 | 2.01 | 1586 |
| 2024-09-20 22:21:42.983 | MS1 | 121.4656700362 | 31.1446324506 | 58 | 504990 | -92.22 | 11.50 | 405.12 | 0.17 | 2.90 | 1567 |

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
| 3242199 | 3 | 121.4643768480 | 31.1491350610 | 42 | 15 | 5 | 48.9 | TDD | 221 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3260022 | 4 | 121.4734344114 | 31.1533261808 | 84 | 13 | 1 | 48.5 | TDD | 591 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3266203 | 1 | 121.4643131553 | 31.1467834118 | 41 | 5 | 7 | 22.7 | TDD | 58 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3273090 | 2 | 121.4681134235 | 31.1543654507 | 102 | 11 | 7 | 27.4 | TDD | 2 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.414 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.429 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.542 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.542 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.264 | NREventA3 | measId:2;ServCellPCI:511;Se... |
| 2024-09-20 22:21:38.504 | NRHandoverAttempt | SourcePCI:511;SourceNR-ARFC... |
| 2024-09-20 22:21:38.537 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.548 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.682 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.682 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266203 | 1 | 7.8505 | 7.9828 | -116.5258 | 19.8811 | 145.2602 | 0.0029 | 0.0045 |
| 2024_09_20 22:00 | 3273090 | 2 | 9.9879 | 12.0016 | -117.0860 | 8.2371 | 139.2147 | 0.0200 | 0.0191 |
| 2024_09_20 22:00 | 3242199 | 3 | 18.3225 | 7.4682 | -115.0073 | 14.6210 | 143.2532 | 0.0176 | 0.0066 |
| 2024_09_20 22:00 | 3260022 | 4 | 18.9006 | 15.2789 | -114.2166 | 8.5192 | 123.5014 | 0.0085 | 0.0085 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415068_0F9D5972 | 504990 | 58 | -85.1 | 504990 | 2 | -88.2 | 504990 | 221 | -93.4 | 504990 | 591 |
| MR_1774415068_CBED0C3F | 504990 | 58 | -88.2 | 504990 | 2 | -87.7 | 504990 | 221 | -96.2 | 504990 | 591 |
| MR_1774415068_55318034 | 504990 | 58 | -84.9 | 504990 | 2 | -86.1 | 504990 | 221 | -96.1 | 504990 | 591 |
| MR_1774415068_8D2685A2 | 504990 | 58 | -87.5 | 504990 | 2 | -86.7 | 504990 | 221 | -94.6 | 504990 | 591 |
| MR_1774415068_CE1F54F9 | 504990 | 58 | -85.6 | 504990 | 2 | -88.2 | 504990 | 221 | -94.3 | 504990 | 591 |
| MR_1774415068_C2EDBDB7 | 504990 | 58 | -88.4 | 504990 | 2 | -87.7 | 504990 | 221 | -96.8 | 504990 | 591 |
| MR_1774415068_79DE77AC | 504990 | 58 | -87.5 | 504990 | 2 | -85.7 | 504990 | 221 | -95.3 | 504990 | 591 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1968: `2dc71a1e-d2b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2dc71a1e-d2b3-4ab6-bb5d-c0686c990f6e` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3259738_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1968] topology](images/train_1968.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3229280_3 and 3244298_1
- `C2`: Increase transmission power for 3244298_1
- `C3`: Decrease A3 Offset threshold for 3244298_1
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Check test server and transmission issues
- `C6`: Add neighbor relationship between 3259738_4 and 3244298_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259738_4 **← 정답**
- `C8`: Increase A3 Offset threshold for 3244298_1
- `C9`: Decrease A3 Offset threshold for 3259738_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244298_1
- `C11`: Increase A3 Offset threshold for 3259738_4
- `C12`: Increase transmission power for 3259738_4
- `C13`: Press down the tilt angle  of 3244298_1 by 3 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244298_1
- `C15`: Adjust the azimuth of 3259738_4 by 43 degrees
- `C16`: Decrease transmission power for 3244298_1
- `C17`: Lift the tilt angle of 3259738_4 by 2 degrees
- `C18`: Lift the tilt angle  of 3244298_1 by 3 degrees
- `C19`: Decrease transmission power for 3259738_4
- `C20`: Press down the tilt angle of 3259738_4 by 2 degrees
- `C21`: Adjust the azimuth of 3244298_1 by 50 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259738_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.495 | MS1 | 121.4656620587 | 31.1446223391 | 733 | 504990 | -91.79 | 12.58 | 570.78 | 0.17 | 2.33 | 1582 |
| 2024-09-20 22:21:32.284 | MS1 | 121.4656763489 | 31.1446286958 | 733 | 504990 | -89.09 | 13.95 | 449.81 | 0.03 | 2.34 | 1600 |
| 2024-09-20 22:21:33.728 | MS1 | 121.4656774013 | 31.1446260686 | 733 | 504990 | -91.10 | 13.04 | 542.66 | 0.05 | 2.34 | 1571 |
| 2024-09-20 22:21:34.699 | MS1 | 121.4656751362 | 31.1446190612 | 733 | 504990 | -88.45 | 14.25 | 75.72 | 0.61 | 2.36 | 693 |
| 2024-09-20 22:21:35.475 | MS1 | 121.4656655645 | 31.1446264801 | 733 | 504990 | -89.77 | 15.97 | 63.58 | 0.64 | 2.82 | 651 |
| 2024-09-20 22:21:36.653 | MS1 | 121.4656751500 | 31.1446274841 | 733 | 504990 | -87.44 | 15.10 | 79.57 | 0.52 | 2.51 | 590 |
| 2024-09-20 22:21:37.813 | MS1 | 121.4656590806 | 31.1446356340 | 733 | 504990 | -90.66 | 10.37 | 89.69 | 0.53 | 2.40 | 659 |
| 2024-09-20 22:21:38.172 | MS1 | 121.4656672917 | 31.1446330391 | 733 | 504990 | -89.33 | 7.57 | 70.08 | 0.57 | 2.39 | 541 |
| 2024-09-20 22:21:39.620 | MS1 | 121.4656746508 | 31.1446264317 | 733 | 504990 | -90.64 | 7.85 | 56.32 | 0.65 | 2.12 | 697 |
| 2024-09-20 22:21:40.130 | MS1 | 121.4656733612 | 31.1446374386 | 733 | 504990 | -91.47 | 9.04 | 317.28 | 0.13 | 2.96 | 1578 |
| 2024-09-20 22:21:41.249 | MS1 | 121.4656764196 | 31.1446283168 | 733 | 504990 | -92.39 | 10.43 | 450.01 | 0.06 | 2.32 | 1560 |
| 2024-09-20 22:21:42.788 | MS1 | 121.4656695322 | 31.1446238804 | 733 | 504990 | -89.64 | 8.99 | 481.65 | 0.07 | 2.13 | 1582 |

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
| 3229280 | 3 | 121.4654952818 | 31.1487648182 | 181 | 4 | 10 | 30.3 | TDD | 284 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3244298 | 1 | 121.4730515020 | 31.1521799754 | 42 | 1 | 5 | 28.7 | TDD | 468 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3259738 | 4 | 121.4649391482 | 31.1552001085 | 220 | 0 | 5 | 33.8 | TDD | 733 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3260773 | 2 | 121.4714154451 | 31.1489783319 | 357 | 15 | 10 | 24.6 | TDD | 643 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.946 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.047 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.047 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.767 | NREventA3 | measId:2;ServCellPCI:728;Se... |
| 2024-09-20 22:21:38.007 | NRHandoverAttempt | SourcePCI:728;SourceNR-ARFC... |
| 2024-09-20 22:21:38.045 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.058 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.192 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.192 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244298 | 1 | 17.3683 | 9.7962 | -114.4507 | 14.9083 | 100.1010 | 0.0091 | 0.0130 |
| 2024_09_20 22:00 | 3260773 | 2 | 15.4829 | 10.0999 | -117.2154 | 16.2342 | 99.4399 | 0.0184 | 0.0138 |
| 2024_09_20 22:00 | 3229280 | 3 | 13.3801 | 10.8495 | -117.5867 | 19.1589 | 133.1405 | 0.0133 | 0.0175 |
| 2024_09_20 22:00 | 3259738 | 4 | 14.1479 | 8.3226 | -116.1400 | 17.7220 | 169.4738 | 0.0064 | 0.0142 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412607_2D5D268B | 504990 | 733 | -88.3 | 504990 | 468 | -92.8 | 504990 | 284 | -97.5 | 504990 | 643 |
| MR_1774412607_27AC4F04 | 504990 | 733 | -89.4 | 504990 | 468 | -95.7 | 504990 | 284 | -95.7 | 504990 | 643 |
| MR_1774412607_C5162DB7 | 504990 | 733 | -89.7 | 504990 | 468 | -95.4 | 504990 | 284 | -97.2 | 504990 | 643 |
| MR_1774412607_07EDECCD | 504990 | 733 | -86.7 | 504990 | 468 | -95.6 | 504990 | 284 | -96.8 | 504990 | 643 |
| MR_1774412607_82BCA605 | 504990 | 733 | -88.4 | 504990 | 468 | -95.4 | 504990 | 284 | -96.6 | 504990 | 643 |
| MR_1774412607_6CF5B07D | 504990 | 733 | -89.1 | 504990 | 468 | -93.3 | 504990 | 284 | -96.1 | 504990 | 643 |
| MR_1774412607_30C3A2AE | 504990 | 733 | -87.3 | 504990 | 468 | -95.1 | 504990 | 284 | -97.4 | 504990 | 643 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1969: `fcbba56b-a46...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fcbba56b-a468-4c4c-9760-7cb349b5702c` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Lift the tilt angle  of 3272584_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1969] topology](images/train_1969.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3228791_1 and 3231151_2
- `C2`: Decrease transmission power for 3231151_2
- `C3`: Adjust the azimuth of 3228791_1 by 34 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228791_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228791_1
- `C6`: Decrease A3 Offset threshold for 3228791_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231151_2
- `C8`: Increase A3 Offset threshold for 3228791_1
- `C9`: Lift the tilt angle  of 3272584_4 by 10 degrees **← 정답**
- `C10`: Increase transmission power for 3228791_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231151_2
- `C12`: Check test server and transmission issues
- `C13`: Increase A3 Offset threshold for 3231151_2
- `C14`: Increase transmission power for 3231151_2
- `C15`: Press down the tilt angle  of 3272584_4 by 10 degrees
- `C16`: Press down the tilt angle of 3228791_1 by 2 degrees
- `C17`: Add neighbor relationship between 3272584_4 and 3231151_2
- `C18`: Lift the tilt angle of 3228791_1 by 2 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease A3 Offset threshold for 3231151_2
- `C21`: Decrease transmission power for 3228791_1
- `C22`: Adjust the azimuth of 3272584_4 by 8 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.295 | MS1 | 121.4656693079 | 31.1446313841 | 192 | 504990 | -87.91 | 13.98 | 313.57 | 0.03 | 2.14 | 1575 |
| 2024-09-20 22:21:32.661 | MS1 | 121.4656762205 | 31.1446357887 | 192 | 504990 | -90.02 | 12.36 | 353.38 | 0.01 | 2.15 | 1572 |
| 2024-09-20 22:21:33.820 | MS1 | 121.4656669092 | 31.1446299495 | 192 | 504990 | -86.71 | 12.32 | 419.02 | 0.18 | 2.42 | 1592 |
| 2024-09-20 22:21:34.617 | MS1 | 121.4656646562 | 31.1446224208 | 192 | 504990 | -88.05 | 14.42 | 56.49 | 0.05 | 2.26 | 1563 |
| 2024-09-20 22:21:35.460 | MS1 | 121.4656622152 | 31.1446228260 | 192 | 504990 | -91.98 | 17.40 | 90.00 | 0.12 | 2.11 | 1597 |
| 2024-09-20 22:21:36.746 | MS1 | 121.4656732988 | 31.1446304441 | 192 | 504990 | -89.97 | 13.56 | 66.83 | 0.07 | 2.95 | 1563 |
| 2024-09-20 22:21:37.721 | MS1 | 121.4656628484 | 31.1446245154 | 192 | 504990 | -91.34 | 11.78 | 88.88 | 0.13 | 2.04 | 1569 |
| 2024-09-20 22:21:38.213 | MS1 | 121.4656593182 | 31.1446352190 | 192 | 504990 | -89.05 | 10.97 | 52.60 | 0.02 | 2.45 | 1587 |
| 2024-09-20 22:21:39.191 | MS1 | 121.4656580044 | 31.1446266822 | 192 | 504990 | -91.48 | 8.29 | 87.21 | 0.18 | 2.93 | 1599 |
| 2024-09-20 22:21:40.198 | MS1 | 121.4656582046 | 31.1446268340 | 192 | 504990 | -92.72 | 9.53 | 379.99 | 0.18 | 2.32 | 1574 |
| 2024-09-20 22:21:41.778 | MS1 | 121.4656652543 | 31.1446249940 | 192 | 504990 | -89.88 | 11.19 | 410.78 | 0.01 | 2.72 | 1573 |
| 2024-09-20 22:21:42.444 | MS1 | 121.4656750924 | 31.1446208149 | 192 | 504990 | -91.30 | 7.26 | 466.14 | 0.17 | 2.36 | 1565 |

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
| 3228791 | 1 | 121.4675991151 | 31.1533336734 | 225 | 0 | 5 | 27.7 | TDD | 192 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3231151 | 2 | 121.4734340784 | 31.1542272853 | 223 | 15 | 1 | 36.5 | TDD | 249 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3270610 | 3 | 121.4683565150 | 31.1487067896 | 302 | 2 | 7 | 49.5 | TDD | 861 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3272584 | 4 | 121.4692290632 | 31.1524328792 | 48 | 1 | 1 | 35.6 | TDD | 510 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.203 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.226 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.368 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.368 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.066 | NREventA3 | measId:2;ServCellPCI:851;Se... |
| 2024-09-20 22:21:38.306 | NRHandoverAttempt | SourcePCI:851;SourceNR-ARFC... |
| 2024-09-20 22:21:38.338 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.348 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.456 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.456 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228791 | 1 | 80.7654 | 89.3190 | -116.8653 | 18.8928 | 105.0706 | 0.0172 | 0.0094 |
| 2024_09_20 22:00 | 3231151 | 2 | 14.6211 | 11.8587 | -115.8369 | 7.1548 | 89.2439 | 0.0064 | 0.0136 |
| 2024_09_20 22:00 | 3270610 | 3 | 10.1403 | 8.5611 | -116.5876 | 9.6526 | 94.1847 | 0.0161 | 0.0131 |
| 2024_09_20 22:00 | 3272584 | 4 | 9.5278 | 19.5586 | -115.5257 | 5.1514 | 180.8093 | 0.0104 | 0.0176 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412104_AECE29C0 | 504990 | 192 | -89.1 | 504990 | 249 | -91.7 | 504990 | 510 | -96.3 | 504990 | 861 |
| MR_1774412104_E3357E19 | 504990 | 192 | -88.9 | 504990 | 249 | -92.0 | 504990 | 510 | -96.1 | 504990 | 861 |
| MR_1774412104_D667020B | 504990 | 192 | -89.2 | 504990 | 249 | -93.5 | 504990 | 510 | -96.1 | 504990 | 861 |
| MR_1774412104_C793DE16 | 504990 | 192 | -86.5 | 504990 | 249 | -90.4 | 504990 | 510 | -94.2 | 504990 | 861 |
| MR_1774412104_69905C8A | 504990 | 192 | -87.8 | 504990 | 249 | -93.2 | 504990 | 510 | -96.7 | 504990 | 861 |
| MR_1774412104_FD6835A2 | 504990 | 192 | -88.8 | 504990 | 249 | -91.2 | 504990 | 510 | -95.5 | 504990 | 861 |

> *... 2개 열 생략 (전체 14열)*

---
