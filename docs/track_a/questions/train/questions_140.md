# Track A 문제 분석 — train[1390]~train[1399]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1390] ~ train[1399] (10개)

## 목차

1. [문제 1390: `5fe0bd5a-46a...`](#1390) — single-answer, 정답: C1
2. [문제 1391: `438e6349-17d...`](#1391) — single-answer, 정답: C16
3. [문제 1392: `48ad85db-333...`](#1392) — single-answer, 정답: C3
4. [문제 1393: `54e639db-abc...`](#1393) — single-answer, 정답: C6
5. [문제 1394: `383a2bc3-8ef...`](#1394) — single-answer, 정답: C6
6. [문제 1395: `6d4e67ed-b15...`](#1395) — single-answer, 정답: C4
7. [문제 1396: `ab4fe0a4-c67...`](#1396) — single-answer, 정답: C9
8. [문제 1397: `f5e88f71-875...`](#1397) — single-answer, 정답: C6
9. [문제 1398: `3c4f1ae3-bbc...`](#1398) — single-answer, 정답: C17
10. [문제 1399: `5e098e1a-591...`](#1399) — single-answer, 정답: C5

---

### 문제 1390: `5fe0bd5a-46a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5fe0bd5a-46a3-4793-bcdf-62a751e533c4` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Add neighbor relationship between 3258598_1 and 3276119_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1390] topology](images/train_1390.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3258598_1 and 3276119_3 **← 정답**
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258598_1
- `C3`: Increase A3 Offset threshold for 3276119_3
- `C4`: Decrease transmission power for 3258598_1
- `C5`: Decrease transmission power for 3276119_3
- `C6`: Increase transmission power for 3258598_1
- `C7`: Press down the tilt angle of 3258598_1 by 10 degrees
- `C8`: Check test server and transmission issues
- `C9`: Adjust the azimuth of 3276119_3 by 39 degrees
- `C10`: Increase transmission power for 3276119_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276119_3
- `C12`: Press down the tilt angle  of 3276119_3 by 4 degrees
- `C13`: Lift the tilt angle  of 3276119_3 by 4 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258598_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276119_3
- `C16`: Lift the tilt angle of 3258598_1 by 10 degrees
- `C17`: Decrease A3 Offset threshold for 3276119_3
- `C18`: Decrease A3 Offset threshold for 3258598_1
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase A3 Offset threshold for 3258598_1
- `C21`: Add neighbor relationship between 3264304_4 and 3276119_3
- `C22`: Adjust the azimuth of 3258598_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.886 | MS1 | 121.4656661970 | 31.1446215793 | 315 | 504990 | -81.74 | 14.23 | 574.19 | 0.19 | 2.00 | 1571 |
| 2024-09-20 22:21:32.973 | MS1 | 121.4656767722 | 31.1446278650 | 315 | 504990 | -76.63 | 16.55 | 556.41 | 0.14 | 2.85 | 1589 |
| 2024-09-20 22:21:33.933 | MS1 | 121.4656595564 | 31.1446378880 | 315 | 504990 | -77.47 | 14.84 | 527.22 | 0.12 | 2.95 | 1586 |
| 2024-09-20 22:21:34.281 | MS1 | 121.4656719392 | 31.1446359478 | 315 | 504990 | -94.99 | -1.70 | 55.59 | 0.10 | 1.14 | 1587 |
| 2024-09-20 22:21:35.923 | MS1 | 121.4656683509 | 31.1446253002 | 315 | 504990 | -85.89 | -2.83 | 64.20 | 0.15 | 1.28 | 1588 |
| 2024-09-20 22:21:36.227 | MS1 | 121.4656658122 | 31.1446295240 | 315 | 504990 | -92.12 | -3.88 | 61.66 | 0.05 | 1.27 | 1568 |
| 2024-09-20 22:21:37.515 | MS1 | 121.4656599856 | 31.1446339925 | 315 | 504990 | -93.91 | -1.98 | 56.33 | 0.13 | 1.32 | 1573 |
| 2024-09-20 22:21:38.504 | MS1 | 121.4656618773 | 31.1446357907 | 315 | 504990 | -76.24 | 17.07 | 482.29 | 0.16 | 1.27 | 1570 |
| 2024-09-20 22:21:39.596 | MS1 | 121.4656627290 | 31.1446368799 | 315 | 504990 | -80.16 | 16.05 | 450.80 | 0.03 | 1.26 | 1599 |
| 2024-09-20 22:21:40.602 | MS1 | 121.4656710660 | 31.1446270158 | 315 | 504990 | -78.29 | 14.73 | 506.04 | 0.16 | 2.19 | 1568 |
| 2024-09-20 22:21:41.381 | MS1 | 121.4656717871 | 31.1446324014 | 315 | 504990 | -84.98 | 17.32 | 536.96 | 0.14 | 2.20 | 1597 |
| 2024-09-20 22:21:42.227 | MS1 | 121.4656707503 | 31.1446262689 | 315 | 504990 | -82.31 | 13.13 | 546.41 | 0.20 | 2.63 | 1584 |

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
| 3251792 | 2 | 121.4641379954 | 31.1533699152 | 65 | 4 | 8 | 49.7 | TDD | 819 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3258598 | 1 | 121.4652678370 | 31.1559180878 | 235 | 15 | 7 | 22.6 | TDD | 315 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3264304 | 4 | 121.4685003632 | 31.1467376312 | 193 | 6 | 10 | 19.6 | TDD | 527 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3276119 | 3 | 121.4753139682 | 31.1447597192 | 230 | 2 | 1 | 38.4 | TDD | 878 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.100 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.201 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.201 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.928 | NREventA3 | measId:2;ServCellPCI:375;Se... |
| 2024-09-20 22:21:35.928 | NREventA3 | measId:2;ServCellPCI:375;Se... |
| 2024-09-20 22:21:36.928 | NREventA3 | measId:2;ServCellPCI:375;Se... |
| 2024-09-20 22:21:39.428 | NRRRCReestablishAttempt | PCI:375 |
| 2024-09-20 22:21:39.439 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.451 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.586 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.586 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258598 | 1 | 9.6369 | 17.7014 | -115.7340 | 8.3141 | 137.5323 | 0.0168 | 0.1572 |
| 2024_09_20 22:00 | 3251792 | 2 | 13.4175 | 17.9779 | -114.4299 | 6.6334 | 198.0233 | 0.0057 | 0.0061 |
| 2024_09_20 22:00 | 3276119 | 3 | 18.4727 | 14.4888 | -117.4821 | 11.4524 | 176.8539 | 0.0146 | 0.0198 |
| 2024_09_20 22:00 | 3264304 | 4 | 8.4553 | 8.9677 | -114.9838 | 10.6923 | 165.2836 | 0.0064 | 0.0196 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413490_AA6E4788 | 504990 | 315 | -97.0 | 504990 | 878 | -88.7 | 504990 | 527 | -93.9 | 504990 | 819 |
| MR_1774413490_A2C12DA4 | 504990 | 315 | -95.8 | 504990 | 878 | -91.3 | 504990 | 527 | -94.4 | 504990 | 819 |
| MR_1774413490_3D480BE1 | 504990 | 878 | -88.7 | 504990 | 315 | -95.3 | 504990 | 527 | -97.6 | 504990 | 819 |
| MR_1774413490_C5F98F13 | 504990 | 315 | -94.2 | 504990 | 878 | -89.8 | 504990 | 527 | -96.1 | 504990 | 819 |
| MR_1774413490_54CFD27C | 504990 | 315 | -93.1 | 504990 | 878 | -90.7 | 504990 | 527 | -94.2 | 504990 | 819 |
| MR_1774413490_5A8F318D | 504990 | 878 | -90.7 | 504990 | 315 | -95.3 | 504990 | 527 | -94.4 | 504990 | 819 |
| MR_1774413490_DE6ABC07 | 504990 | 878 | -92.4 | 504990 | 315 | -95.9 | 504990 | 527 | -96.4 | 504990 | 819 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1391: `438e6349-17d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `438e6349-17d4-4cd5-abe0-38ec34575157` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Lift the tilt angle  of 3218258_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1391] topology](images/train_1391.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3275447_1
- `C2`: Increase A3 Offset threshold for 3275447_1
- `C3`: Increase transmission power for 3275447_1
- `C4`: Add neighbor relationship between 3247360_3 and 3275447_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275447_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247360_3
- `C7`: Increase A3 Offset threshold for 3247360_3
- `C8`: Press down the tilt angle of 3247360_3 by 1 degrees
- `C9`: Lift the tilt angle of 3247360_3 by 1 degrees
- `C10`: Increase transmission power for 3247360_3
- `C11`: Decrease A3 Offset threshold for 3247360_3
- `C12`: Add neighbor relationship between 3218258_2 and 3275447_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275447_1
- `C14`: Adjust the azimuth of 3247360_3 by 6 degrees
- `C15`: Decrease transmission power for 3275447_1
- `C16`: Lift the tilt angle  of 3218258_2 by 10 degrees **← 정답**
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247360_3
- `C18`: Adjust the azimuth of 3218258_2 by 27 degrees
- `C19`: Check test server and transmission issues
- `C20`: Decrease transmission power for 3247360_3
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Press down the tilt angle  of 3218258_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.856 | MS1 | 121.4656596962 | 31.1446195281 | 443 | 504990 | -87.00 | 12.51 | 564.01 | 0.05 | 2.78 | 1574 |
| 2024-09-20 22:21:32.505 | MS1 | 121.4656739807 | 31.1446199854 | 443 | 504990 | -85.23 | 14.44 | 394.85 | 0.20 | 2.35 | 1586 |
| 2024-09-20 22:21:33.911 | MS1 | 121.4656660495 | 31.1446208292 | 443 | 504990 | -91.89 | 15.08 | 538.73 | 0.11 | 2.24 | 1581 |
| 2024-09-20 22:21:34.937 | MS1 | 121.4656595260 | 31.1446378354 | 443 | 504990 | -91.08 | 12.81 | 61.60 | 0.08 | 2.37 | 1575 |
| 2024-09-20 22:21:35.741 | MS1 | 121.4656777585 | 31.1446265725 | 443 | 504990 | -90.17 | 12.38 | 74.43 | 0.12 | 2.36 | 1575 |
| 2024-09-20 22:21:36.617 | MS1 | 121.4656598806 | 31.1446318496 | 443 | 504990 | -89.30 | 12.81 | 87.97 | 0.00 | 2.62 | 1590 |
| 2024-09-20 22:21:37.332 | MS1 | 121.4656648911 | 31.1446288686 | 443 | 504990 | -93.78 | 8.69 | 84.36 | 0.11 | 2.18 | 1587 |
| 2024-09-20 22:21:38.489 | MS1 | 121.4656600021 | 31.1446232036 | 443 | 504990 | -90.68 | 10.49 | 61.98 | 0.06 | 2.92 | 1588 |
| 2024-09-20 22:21:39.777 | MS1 | 121.4656774452 | 31.1446247436 | 443 | 504990 | -92.08 | 11.16 | 105.02 | 0.17 | 2.52 | 1591 |
| 2024-09-20 22:21:40.425 | MS1 | 121.4656582889 | 31.1446224367 | 443 | 504990 | -91.92 | 10.20 | 555.16 | 0.16 | 2.50 | 1563 |
| 2024-09-20 22:21:41.534 | MS1 | 121.4656690968 | 31.1446368828 | 443 | 504990 | -91.75 | 10.59 | 346.40 | 0.03 | 2.22 | 1592 |
| 2024-09-20 22:21:42.811 | MS1 | 121.4656676096 | 31.1446280310 | 443 | 504990 | -90.73 | 9.40 | 554.11 | 0.05 | 2.19 | 1578 |

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
| 3218258 | 2 | 121.4734957991 | 31.1479729697 | 86 | 12 | 0 | 24.4 | TDD | 962 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3223719 | 4 | 121.4721238047 | 31.1466299891 | 340 | 9 | 11 | 44.7 | TDD | 789 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3247360 | 3 | 121.4740148796 | 31.1523315913 | 217 | 0 | 5 | 30.0 | TDD | 443 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3275447 | 1 | 121.4702111998 | 31.1518090763 | 182 | 12 | 0 | 20.4 | TDD | 920 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.030 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.054 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.177 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.177 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.920 | NREventA3 | measId:2;ServCellPCI:177;Se... |
| 2024-09-20 22:21:38.160 | NRHandoverAttempt | SourcePCI:177;SourceNR-ARFC... |
| 2024-09-20 22:21:38.196 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.211 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.335 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.335 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275447 | 1 | 19.6072 | 15.5678 | -116.3219 | 7.7840 | 197.5751 | 0.0035 | 0.0163 |
| 2024_09_20 22:00 | 3218258 | 2 | 8.0394 | 6.7890 | -115.4758 | 14.0455 | 185.2818 | 0.0027 | 0.0021 |
| 2024_09_20 22:00 | 3247360 | 3 | 84.8964 | 91.3584 | -116.4562 | 19.2783 | 165.2602 | 0.0063 | 0.0099 |
| 2024_09_20 22:00 | 3223719 | 4 | 19.7945 | 9.4272 | -115.7710 | 9.8099 | 148.6592 | 0.0183 | 0.0082 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415966_7DCD8A69 | 504990 | 443 | -89.3 | 504990 | 920 | -94.0 | 504990 | 962 | -101.5 | 504990 | 789 |
| MR_1774415966_15CB91F7 | 504990 | 443 | -92.0 | 504990 | 920 | -94.1 | 504990 | 962 | -102.6 | 504990 | 789 |
| MR_1774415966_3908123D | 504990 | 443 | -89.3 | 504990 | 920 | -92.8 | 504990 | 962 | -102.1 | 504990 | 789 |
| MR_1774415966_79382489 | 504990 | 443 | -91.8 | 504990 | 920 | -93.7 | 504990 | 962 | -101.1 | 504990 | 789 |
| MR_1774415966_4EB89737 | 504990 | 443 | -91.9 | 504990 | 920 | -93.8 | 504990 | 962 | -104.3 | 504990 | 789 |
| MR_1774415966_FC4A8B39 | 504990 | 443 | -92.2 | 504990 | 920 | -94.2 | 504990 | 962 | -101.2 | 504990 | 789 |
| MR_1774415966_381A3B79 | 504990 | 443 | -92.4 | 504990 | 920 | -93.9 | 504990 | 962 | -103.4 | 504990 | 789 |
| MR_1774415966_BCEF26DC | 504990 | 443 | -92.8 | 504990 | 920 | -92.7 | 504990 | 962 | -101.3 | 504990 | 789 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1392: `48ad85db-333...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `48ad85db-333d-49a7-b936-52a8e6e03043` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Lift the tilt angle  of 3262767_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1392] topology](images/train_1392.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Adjust the azimuth of 3274060_4 by 18 degrees
- `C3`: Lift the tilt angle  of 3262767_2 by 10 degrees **← 정답**
- `C4`: Press down the tilt angle  of 3262767_2 by 10 degrees
- `C5`: Decrease transmission power for 3232620_3
- `C6`: Press down the tilt angle of 3274060_4 by 6 degrees
- `C7`: Decrease A3 Offset threshold for 3274060_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232620_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232620_3
- `C10`: Increase A3 Offset threshold for 3232620_3
- `C11`: Increase A3 Offset threshold for 3274060_4
- `C12`: Adjust the azimuth of 3262767_2 by 50 degrees
- `C13`: Add neighbor relationship between 3262767_2 and 3232620_3
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274060_4
- `C16`: Decrease transmission power for 3274060_4
- `C17`: Increase transmission power for 3274060_4
- `C18`: Add neighbor relationship between 3274060_4 and 3232620_3
- `C19`: Decrease A3 Offset threshold for 3232620_3
- `C20`: Lift the tilt angle of 3274060_4 by 6 degrees
- `C21`: Increase transmission power for 3232620_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274060_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.512 | MS1 | 121.4656696224 | 31.1446220321 | 47 | 504990 | -85.72 | 17.46 | 437.52 | 0.14 | 2.62 | 1589 |
| 2024-09-20 22:21:32.294 | MS1 | 121.4656680500 | 31.1446232681 | 47 | 504990 | -91.31 | 16.41 | 432.26 | 0.08 | 2.78 | 1569 |
| 2024-09-20 22:21:33.495 | MS1 | 121.4656583256 | 31.1446379285 | 47 | 504990 | -90.66 | 13.67 | 567.08 | 0.01 | 2.11 | 1587 |
| 2024-09-20 22:21:34.658 | MS1 | 121.4656756179 | 31.1446346233 | 47 | 504990 | -90.78 | 16.24 | 56.80 | 0.00 | 2.23 | 1584 |
| 2024-09-20 22:21:35.148 | MS1 | 121.4656615103 | 31.1446320983 | 47 | 504990 | -90.79 | 14.84 | 73.43 | 0.16 | 2.11 | 1567 |
| 2024-09-20 22:21:36.832 | MS1 | 121.4656710470 | 31.1446246698 | 47 | 504990 | -91.45 | 14.76 | 60.27 | 0.15 | 2.27 | 1579 |
| 2024-09-20 22:21:37.458 | MS1 | 121.4656587461 | 31.1446344022 | 47 | 504990 | -90.39 | 7.34 | 103.24 | 0.08 | 2.22 | 1572 |
| 2024-09-20 22:21:38.891 | MS1 | 121.4656696730 | 31.1446226581 | 47 | 504990 | -89.88 | 12.59 | 102.07 | 0.08 | 2.67 | 1597 |
| 2024-09-20 22:21:39.622 | MS1 | 121.4656624131 | 31.1446258062 | 47 | 504990 | -89.08 | 12.40 | 94.87 | 0.08 | 2.75 | 1594 |
| 2024-09-20 22:21:40.593 | MS1 | 121.4656608512 | 31.1446326481 | 47 | 504990 | -93.86 | 10.25 | 327.01 | 0.07 | 2.06 | 1575 |
| 2024-09-20 22:21:41.663 | MS1 | 121.4656751396 | 31.1446365048 | 47 | 504990 | -89.58 | 7.93 | 565.32 | 0.13 | 2.17 | 1596 |
| 2024-09-20 22:21:42.822 | MS1 | 121.4656633930 | 31.1446322029 | 47 | 504990 | -92.40 | 11.12 | 404.10 | 0.11 | 2.27 | 1591 |

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
| 3232620 | 3 | 121.4694275672 | 31.1543517132 | 89 | 11 | 10 | 35.3 | TDD | 621 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3262767 | 2 | 121.4683346284 | 31.1545281445 | 350 | 9 | 5 | 45.5 | TDD | 35 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3265368 | 1 | 121.4694141825 | 31.1450102799 | 273 | 6 | 1 | 46.2 | TDD | 162 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3274060 | 4 | 121.4640386465 | 31.1466541340 | 163 | 1 | 5 | 23.1 | TDD | 47 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.327 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.477 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.477 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.157 | NREventA3 | measId:2;ServCellPCI:618;Se... |
| 2024-09-20 22:21:38.397 | NRHandoverAttempt | SourcePCI:618;SourceNR-ARFC... |
| 2024-09-20 22:21:38.443 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.457 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.586 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.586 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265368 | 1 | 12.3345 | 7.5184 | -114.2913 | 13.3950 | 193.4728 | 0.0152 | 0.0009 |
| 2024_09_20 22:00 | 3262767 | 2 | 15.9923 | 12.4098 | -116.1593 | 7.6347 | 167.6627 | 0.0012 | 0.0032 |
| 2024_09_20 22:00 | 3232620 | 3 | 16.2324 | 19.8008 | -115.7616 | 18.0063 | 135.4029 | 0.0007 | 0.0044 |
| 2024_09_20 22:00 | 3274060 | 4 | 86.5337 | 80.3338 | -115.7690 | 10.6754 | 195.1044 | 0.0140 | 0.0198 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416473_9CC31843 | 504990 | 47 | -92.5 | 504990 | 621 | -97.2 | 504990 | 35 | -99.1 | 504990 | 162 |
| MR_1774416473_8DF95FE2 | 504990 | 47 | -92.5 | 504990 | 621 | -98.0 | 504990 | 35 | -100.6 | 504990 | 162 |
| MR_1774416473_31B9DF46 | 504990 | 47 | -89.7 | 504990 | 621 | -96.8 | 504990 | 35 | -100.5 | 504990 | 162 |
| MR_1774416473_CC6A2326 | 504990 | 47 | -91.9 | 504990 | 621 | -99.1 | 504990 | 35 | -99.6 | 504990 | 162 |
| MR_1774416473_B4546C60 | 504990 | 47 | -89.1 | 504990 | 621 | -98.7 | 504990 | 35 | -101.0 | 504990 | 162 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1393: `54e639db-abc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `54e639db-abcc-4078-a201-aae3d1f993db` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Add neighbor relationship between 3264009_2 and 3220881_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1393] topology](images/train_1393.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3264009_2
- `C2`: Adjust the azimuth of 3220881_1 by 34 degrees
- `C3`: Lift the tilt angle of 3264009_2 by 6 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264009_2
- `C5`: Check test server and transmission issues
- `C6`: Add neighbor relationship between 3264009_2 and 3220881_1 **← 정답**
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264009_2
- `C8`: Adjust the azimuth of 3264009_2 by 50 degrees
- `C9`: Increase transmission power for 3220881_1
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Add neighbor relationship between 3218051_3 and 3220881_1
- `C12`: Decrease transmission power for 3264009_2
- `C13`: Increase A3 Offset threshold for 3220881_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220881_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220881_1
- `C16`: Decrease transmission power for 3220881_1
- `C17`: Press down the tilt angle  of 3220881_1 by 2 degrees
- `C18`: Press down the tilt angle of 3264009_2 by 6 degrees
- `C19`: Decrease A3 Offset threshold for 3220881_1
- `C20`: Lift the tilt angle  of 3220881_1 by 2 degrees
- `C21`: Increase A3 Offset threshold for 3264009_2
- `C22`: Increase transmission power for 3264009_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.791 | MS1 | 121.4656716319 | 31.1446241181 | 810 | 504990 | -78.66 | 15.05 | 367.95 | 0.02 | 2.01 | 1581 |
| 2024-09-20 22:21:32.668 | MS1 | 121.4656687207 | 31.1446243149 | 810 | 504990 | -81.34 | 13.44 | 468.08 | 0.00 | 2.51 | 1574 |
| 2024-09-20 22:21:33.681 | MS1 | 121.4656686750 | 31.1446330547 | 810 | 504990 | -82.10 | 14.80 | 520.56 | 0.10 | 2.08 | 1563 |
| 2024-09-20 22:21:34.743 | MS1 | 121.4656694966 | 31.1446307442 | 810 | 504990 | -94.48 | -3.00 | 63.68 | 0.11 | 1.32 | 1592 |
| 2024-09-20 22:21:35.746 | MS1 | 121.4656583910 | 31.1446204778 | 810 | 504990 | -90.19 | -0.85 | 65.95 | 0.10 | 1.35 | 1585 |
| 2024-09-20 22:21:36.655 | MS1 | 121.4656660837 | 31.1446190173 | 810 | 504990 | -91.81 | -1.26 | 51.34 | 0.09 | 1.27 | 1586 |
| 2024-09-20 22:21:37.272 | MS1 | 121.4656742376 | 31.1446277186 | 810 | 504990 | -92.98 | -1.01 | 42.10 | 0.10 | 1.02 | 1598 |
| 2024-09-20 22:21:38.384 | MS1 | 121.4656629385 | 31.1446269156 | 810 | 504990 | -75.46 | 13.42 | 562.61 | 0.13 | 1.21 | 1589 |
| 2024-09-20 22:21:39.136 | MS1 | 121.4656642444 | 31.1446293687 | 810 | 504990 | -79.67 | 17.24 | 383.30 | 0.07 | 1.46 | 1568 |
| 2024-09-20 22:21:40.945 | MS1 | 121.4656629201 | 31.1446344582 | 810 | 504990 | -77.71 | 12.18 | 413.43 | 0.19 | 2.04 | 1587 |
| 2024-09-20 22:21:41.958 | MS1 | 121.4656701741 | 31.1446337383 | 810 | 504990 | -79.77 | 13.69 | 313.60 | 0.16 | 2.94 | 1562 |
| 2024-09-20 22:21:42.371 | MS1 | 121.4656728458 | 31.1446303861 | 810 | 504990 | -76.01 | 17.55 | 415.85 | 0.00 | 2.94 | 1562 |

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
| 3212415 | 4 | 121.4651397311 | 31.1448559062 | 170 | 13 | 5 | 46.7 | TDD | 394 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3218051 | 3 | 121.4724894876 | 31.1492304853 | 227 | 9 | 12 | 30.1 | TDD | 108 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3220881 | 1 | 121.4644609697 | 31.1536152615 | 207 | 1 | 3 | 20.1 | TDD | 57 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3264009 | 2 | 121.4758230925 | 31.1527423848 | 314 | 5 | 10 | 28.5 | TDD | 810 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.024 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.040 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.142 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.142 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.868 | NREventA3 | measId:2;ServCellPCI:865;Se... |
| 2024-09-20 22:21:35.868 | NREventA3 | measId:2;ServCellPCI:865;Se... |
| 2024-09-20 22:21:36.868 | NREventA3 | measId:2;ServCellPCI:865;Se... |
| 2024-09-20 22:21:39.368 | NRRRCReestablishAttempt | PCI:865 |
| 2024-09-20 22:21:39.379 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.394 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.531 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.531 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220881 | 1 | 6.3945 | 17.3540 | -114.4126 | 15.8342 | 86.1005 | 0.0147 | 0.0006 |
| 2024_09_20 22:00 | 3264009 | 2 | 8.0511 | 10.9343 | -114.4731 | 7.2181 | 107.2997 | 0.0178 | 0.1190 |
| 2024_09_20 22:00 | 3218051 | 3 | 7.0209 | 15.8587 | -115.9746 | 9.3279 | 147.9227 | 0.0175 | 0.0047 |
| 2024_09_20 22:00 | 3212415 | 4 | 12.9330 | 11.3832 | -116.5308 | 11.5415 | 111.7127 | 0.0133 | 0.0192 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414194_9337DBC4 | 504990 | 810 | -95.1 | 504990 | 57 | -88.8 | 504990 | 108 | -96.8 | 504990 | 394 |
| MR_1774414194_801EB01C | 504990 | 57 | -88.6 | 504990 | 810 | -95.3 | 504990 | 108 | -99.2 | 504990 | 394 |
| MR_1774414194_354F129F | 504990 | 57 | -91.0 | 504990 | 810 | -92.6 | 504990 | 108 | -99.6 | 504990 | 394 |
| MR_1774414194_2842BB77 | 504990 | 810 | -94.4 | 504990 | 57 | -87.9 | 504990 | 108 | -97.5 | 504990 | 394 |
| MR_1774414194_41C8969C | 504990 | 57 | -88.0 | 504990 | 810 | -92.7 | 504990 | 108 | -98.6 | 504990 | 394 |
| MR_1774414194_5E23C19F | 504990 | 57 | -88.2 | 504990 | 810 | -92.7 | 504990 | 108 | -96.4 | 504990 | 394 |
| MR_1774414194_F0F6D789 | 504990 | 57 | -91.9 | 504990 | 810 | -96.1 | 504990 | 108 | -99.4 | 504990 | 394 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1394: `383a2bc3-8ef...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `383a2bc3-8ef9-4c5d-878b-2c9c6923611e` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223670_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1394] topology](images/train_1394.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3222919_3
- `C2`: Add neighbor relationship between 3223670_6 and 3222919_3
- `C3`: Press down the tilt angle  of 3222919_3 by 2 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223670_6
- `C5`: Decrease A3 Offset threshold for 3223670_6
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223670_6 **← 정답**
- `C7`: Add neighbor relationship between 3272964_10 and 3222919_3
- `C8`: Adjust the azimuth of 3223670_6 by 49 degrees
- `C9`: Lift the tilt angle of 3223670_6 by 2 degrees
- `C10`: Increase transmission power for 3223670_6
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222919_3
- `C12`: Increase A3 Offset threshold for 3223670_6
- `C13`: Check test server and transmission issues
- `C14`: Lift the tilt angle  of 3222919_3 by 2 degrees
- `C15`: Increase transmission power for 3222919_3
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease transmission power for 3223670_6
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222919_3
- `C19`: Decrease transmission power for 3222919_3
- `C20`: Press down the tilt angle of 3223670_6 by 2 degrees
- `C21`: Adjust the azimuth of 3222919_3 by 27 degrees
- `C22`: Decrease A3 Offset threshold for 3222919_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.376 | MS1 | 121.4656639674 | 31.1446333531 | 477 | 504990 | -93.60 | 12.40 | 298.00 | 0.16 | 2.91 | 1561 |
| 2024-09-20 22:21:32.900 | MS1 | 121.4656772519 | 31.1446295037 | 240 | 504990 | -93.28 | 13.79 | 552.51 | 0.04 | 2.12 | 1587 |
| 2024-09-20 22:21:33.432 | MS1 | 121.4656589043 | 31.1446344292 | 148 | 504990 | -94.56 | 13.44 | 434.60 | 0.14 | 2.16 | 1598 |
| 2024-09-20 22:21:34.363 | MS1 | 121.4656664842 | 31.1446354009 | 241 | 152650 | -91.65 | 7.56 | 76.39 | 0.12 | 1.86 | 973 |
| 2024-09-20 22:21:35.207 | MS1 | 121.4656637209 | 31.1446311919 | 910 | 152650 | -96.94 | 4.95 | 77.55 | 0.00 | 1.56 | 969 |
| 2024-09-20 22:21:36.469 | MS1 | 121.4656597029 | 31.1446195225 | 293 | 152650 | -95.52 | 2.41 | 62.75 | 0.20 | 1.77 | 987 |
| 2024-09-20 22:21:37.117 | MS1 | 121.4656733169 | 31.1446317003 | 517 | 152650 | -93.70 | 4.23 | 49.03 | 0.03 | 1.95 | 980 |
| 2024-09-20 22:21:38.777 | MS1 | 121.4656717416 | 31.1446294603 | 241 | 152650 | -89.60 | 6.63 | 71.46 | 0.17 | 1.55 | 994 |
| 2024-09-20 22:21:39.314 | MS1 | 121.4656605188 | 31.1446241034 | 910 | 152650 | -89.32 | 5.28 | 67.64 | 0.18 | 1.72 | 906 |
| 2024-09-20 22:21:40.302 | MS1 | 121.4656702629 | 31.1446194031 | 293 | 152650 | -92.40 | 5.16 | 70.30 | 0.06 | 2.08 | 1598 |
| 2024-09-20 22:21:41.859 | MS1 | 121.4656680099 | 31.1446366179 | 517 | 152650 | -92.55 | 7.65 | 92.19 | 0.14 | 2.77 | 1574 |
| 2024-09-20 22:21:42.272 | MS1 | 121.4656728035 | 31.1446216849 | 241 | 152650 | -89.62 | 4.30 | 76.54 | 0.01 | 2.14 | 1565 |

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
| 3210309 | 7 | 121.4717712133 | 31.1483537126 | 181 | 1 | 8 | 0.8 | FDD | 864 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3213021 | 12 | 121.4644665818 | 31.1456634809 | 123 | 0 | 4 | 24.6 | FDD | 270 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3214300 | 13 | 121.4643129893 | 31.1490423823 | 264 | 12 | 3 | 26.6 | FDD | 241 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3218123 | 2 | 121.4719713711 | 31.1505143286 | 182 | 13 | 2 | 0.3 | TDD | 240 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3222919 | 3 | 121.4704570245 | 31.1503588514 | 243 | 0 | 8 | 23.2 | TDD | 563 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3223670 | 6 | 121.4672760480 | 31.1555215547 | 236 | 1 | 2 | 10.8 | TDD | 477 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3237695 | 8 | 121.4664112571 | 31.1440544060 | 63 | 15 | 1 | 2.2 | FDD | 545 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3238459 | 1 | 121.4699673227 | 31.1480724611 | 212 | 15 | 4 | 12.1 | TDD | 879 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3240635 | 4 | 121.4722886605 | 31.1549352504 | 157 | 9 | 9 | 17.8 | TDD | 148 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3241879 | 5 | 121.4692856737 | 31.1503873157 | 259 | 12 | 0 | 4.8 | TDD | 508 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3243637 | 11 | 121.4658392187 | 31.1533354829 | 223 | 15 | 4 | 0.2 | FDD | 910 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3272964 | 10 | 121.4692640149 | 31.1552513345 | 165 | 8 | 1 | 26.4 | FDD | 293 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3273007 | 9 | 121.4756794680 | 31.1559002464 | 144 | 5 | 2 | 12.8 | FDD | 517 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |

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
| 2024-09-20 22:21:30.832 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.856 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.974 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.974 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.723 | NREventA2 | measId:1;ServCellPCI:108;Se... |
| 2024-09-20 22:21:34.858 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.072 | NREventA5 | measId:3;ServCellPCI:108;Se... |
| 2024-09-20 22:21:35.113 | NRHandoverAttempt | SourcePCI:108;SourceNR-ARFC... |
| 2024-09-20 22:21:35.136 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.147 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.263 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.263 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238459 | 1 | 13.2987 | 17.3941 | -115.1081 | 10.5605 | 87.3785 | 0.0025 | 0.0191 |
| 2024_09_20 22:00 | 3218123 | 2 | 7.5110 | 13.4744 | -117.6993 | 10.6056 | 187.7491 | 0.0123 | 0.0099 |
| 2024_09_20 22:00 | 3222919 | 3 | 6.9418 | 8.3125 | -116.2791 | 5.4786 | 195.7039 | 0.0176 | 0.0017 |
| 2024_09_20 22:00 | 3240635 | 4 | 18.5642 | 18.6439 | -115.5633 | 19.5870 | 115.4464 | 0.0135 | 0.0114 |
| 2024_09_20 22:00 | 3241879 | 5 | 19.9363 | 17.6562 | -115.2866 | 18.1254 | 161.5004 | 0.0169 | 0.0101 |
| 2024_09_20 22:00 | 3223670 | 6 | 13.6856 | 10.8720 | -117.7801 | 5.1654 | 187.3264 | 0.0101 | 0.0183 |
| 2024_09_20 22:00 | 3210309 | 7 | 16.5339 | 19.3062 | -117.0976 | 3.6368 | 29.7301 | 0.0010 | 0.0155 |
| 2024_09_20 22:00 | 3237695 | 8 | 13.2902 | 6.8486 | -115.1568 | 4.4879 | 37.5158 | 0.0103 | 0.0196 |
| 2024_09_20 22:00 | 3273007 | 9 | 11.7061 | 11.4059 | -114.0553 | 4.0279 | 39.9683 | 0.0092 | 0.0097 |
| 2024_09_20 22:00 | 3272964 | 10 | 12.2753 | 7.2504 | -116.8039 | 3.1412 | 49.4669 | 0.0162 | 0.0019 |
| 2024_09_20 22:00 | 3243637 | 11 | 9.6619 | 19.8992 | -114.0354 | 3.6301 | 49.4184 | 0.0198 | 0.0159 |
| 2024_09_20 22:00 | 3213021 | 12 | 16.5221 | 11.9830 | -117.9587 | 3.9202 | 50.1185 | 0.0080 | 0.0028 |
| 2024_09_20 22:00 | 3214300 | 13 | 5.2203 | 16.1978 | -114.8076 | 3.5414 | 36.7166 | 0.0080 | 0.0025 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413299_7AA8686F | 504990 | 148 | -92.8 | 504990 | 563 | -90.6 | 504990 | 879 | -102.3 | 504990 | 508 |
| MR_1774413299_EE5D9FB2 | 152650 | 241 | -92.6 | 152650 | 270 | -97.7 | 152650 | 545 | -101.0 | 152650 | 864 |
| MR_1774413299_1B306CE7 | 504990 | 148 | -95.7 | 504990 | 563 | -92.1 | 504990 | 879 | -103.2 | 504990 | 508 |
| MR_1774413299_C86CC8EC | 504990 | 148 | -93.2 | 504990 | 563 | -92.9 | 504990 | 879 | -101.1 | 504990 | 508 |
| MR_1774413299_D3628E18 | 152650 | 241 | -92.0 | 152650 | 270 | -99.4 | 152650 | 545 | -101.4 | 152650 | 864 |
| MR_1774413299_4B720A28 | 504990 | 148 | -94.5 | 504990 | 563 | -92.5 | 504990 | 879 | -103.3 | 504990 | 508 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1395: `6d4e67ed-b15...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6d4e67ed-b152-4c58-ba58-ec7987dc69a4` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1395] topology](images/train_1395.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3248119_1
- `C2`: Press down the tilt angle  of 3267055_3 by 10 degrees
- `C3`: Decrease transmission power for 3248119_1
- `C4`: Check test server and transmission issues **← 정답**
- `C5`: Increase A3 Offset threshold for 3267055_3
- `C6`: Adjust the azimuth of 3248119_1 by 50 degrees
- `C7`: Add neighbor relationship between 3248119_1 and 3267055_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267055_3
- `C9`: Increase transmission power for 3248119_1
- `C10`: Decrease transmission power for 3267055_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248119_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267055_3
- `C13`: Add neighbor relationship between 3236253_4 and 3267055_3
- `C14`: Lift the tilt angle of 3248119_1 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3267055_3
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Adjust the azimuth of 3267055_3 by 8 degrees
- `C18`: Increase A3 Offset threshold for 3248119_1
- `C19`: Increase transmission power for 3267055_3
- `C20`: Press down the tilt angle of 3248119_1 by 10 degrees
- `C21`: Lift the tilt angle  of 3267055_3 by 10 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248119_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.831 | MS1 | 121.4656631762 | 31.1446234724 | 168 | 504990 | -91.86 | 15.23 | 305.49 | 0.16 | 2.22 | 1577 |
| 2024-09-20 22:21:32.622 | MS1 | 121.4656639185 | 31.1446351754 | 168 | 504990 | -90.91 | 17.94 | 514.16 | 0.03 | 2.12 | 1598 |
| 2024-09-20 22:21:33.243 | MS1 | 121.4656755512 | 31.1446312210 | 168 | 504990 | -90.14 | 16.86 | 596.93 | 0.01 | 2.67 | 1578 |
| 2024-09-20 22:21:34.471 | MS1 | 121.4656652086 | 31.1446246515 | 168 | 504990 | -88.69 | 17.08 | 90.63 | 0.17 | 2.63 | 330 |
| 2024-09-20 22:21:35.865 | MS1 | 121.4656700050 | 31.1446181409 | 168 | 504990 | -90.46 | 13.25 | 67.44 | 0.18 | 2.42 | 315 |
| 2024-09-20 22:21:36.455 | MS1 | 121.4656661354 | 31.1446349230 | 168 | 504990 | -87.58 | 12.60 | 54.31 | 0.09 | 2.64 | 323 |
| 2024-09-20 22:21:37.160 | MS1 | 121.4656714325 | 31.1446290250 | 168 | 504990 | -93.00 | 10.34 | 81.20 | 0.04 | 2.39 | 322 |
| 2024-09-20 22:21:38.955 | MS1 | 121.4656700996 | 31.1446313695 | 168 | 504990 | -92.64 | 11.82 | 79.63 | 0.04 | 2.25 | 352 |
| 2024-09-20 22:21:39.152 | MS1 | 121.4656699786 | 31.1446372302 | 168 | 504990 | -91.02 | 10.94 | 85.49 | 0.20 | 2.83 | 340 |
| 2024-09-20 22:21:40.685 | MS1 | 121.4656670495 | 31.1446182821 | 168 | 504990 | -93.27 | 8.98 | 453.79 | 0.06 | 2.27 | 1577 |
| 2024-09-20 22:21:41.555 | MS1 | 121.4656706076 | 31.1446358184 | 168 | 504990 | -89.20 | 8.66 | 543.42 | 0.15 | 2.98 | 1578 |
| 2024-09-20 22:21:42.130 | MS1 | 121.4656632865 | 31.1446293106 | 168 | 504990 | -89.63 | 9.34 | 352.34 | 0.12 | 2.37 | 1574 |

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
| 3225770 | 2 | 121.4657972593 | 31.1452115194 | 293 | 2 | 5 | 23.7 | TDD | 299 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3236253 | 4 | 121.4744812289 | 31.1501757491 | 335 | 11 | 11 | 18.2 | TDD | 653 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3248119 | 1 | 121.4659861211 | 31.1554129104 | 6 | 10 | 10 | 45.7 | TDD | 168 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3267055 | 3 | 121.4675691307 | 31.1530448350 | 183 | 14 | 8 | 35.8 | TDD | 820 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.902 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.918 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.041 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.041 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.728 | NREventA3 | measId:2;ServCellPCI:976;Se... |
| 2024-09-20 22:21:37.968 | NRHandoverAttempt | SourcePCI:976;SourceNR-ARFC... |
| 2024-09-20 22:21:38.001 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.015 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.137 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.137 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248119 | 1 | 5.0972 | 17.2474 | -116.6561 | 15.1303 | 177.4995 | 0.0199 | 0.0185 |
| 2024_09_20 22:00 | 3225770 | 2 | 7.2242 | 13.9753 | -114.2896 | 15.7609 | 105.4873 | 0.0102 | 0.0083 |
| 2024_09_20 22:00 | 3267055 | 3 | 19.8229 | 8.8066 | -116.5375 | 8.2561 | 148.5018 | 0.0081 | 0.0108 |
| 2024_09_20 22:00 | 3236253 | 4 | 9.8744 | 13.8528 | -117.7821 | 16.8359 | 123.3087 | 0.0138 | 0.0080 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412096_729BEED1 | 504990 | 168 | -88.0 | 504990 | 820 | -95.2 | 504990 | 653 | -94.3 | 504990 | 299 |
| MR_1774412096_3F17FF01 | 504990 | 168 | -88.0 | 504990 | 820 | -94.5 | 504990 | 653 | -96.9 | 504990 | 299 |
| MR_1774412096_074D7740 | 504990 | 168 | -87.0 | 504990 | 820 | -96.1 | 504990 | 653 | -97.7 | 504990 | 299 |
| MR_1774412096_BB5C11FD | 504990 | 168 | -89.8 | 504990 | 820 | -96.5 | 504990 | 653 | -97.8 | 504990 | 299 |
| MR_1774412096_E012DAAF | 504990 | 168 | -88.5 | 504990 | 820 | -94.4 | 504990 | 653 | -96.4 | 504990 | 299 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1396: `ab4fe0a4-c67...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ab4fe0a4-c674-4538-a386-1ef78794d8bc` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Lift the tilt angle  of 3238198_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1396] topology](images/train_1396.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3224831_3
- `C2`: Adjust the azimuth of 3224831_3 by 9 degrees
- `C3`: Press down the tilt angle  of 3238198_1 by 10 degrees
- `C4`: Decrease transmission power for 3231505_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224831_3
- `C6`: Increase A3 Offset threshold for 3231505_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224831_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231505_2
- `C9`: Lift the tilt angle  of 3238198_1 by 10 degrees **← 정답**
- `C10`: Increase transmission power for 3231505_2
- `C11`: Add neighbor relationship between 3224831_3 and 3231505_2
- `C12`: Decrease A3 Offset threshold for 3231505_2
- `C13`: Increase A3 Offset threshold for 3224831_3
- `C14`: Increase transmission power for 3224831_3
- `C15`: Add neighbor relationship between 3238198_1 and 3231505_2
- `C16`: Decrease transmission power for 3224831_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231505_2
- `C18`: Adjust the azimuth of 3238198_1 by 50 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Check test server and transmission issues
- `C21`: Lift the tilt angle of 3224831_3 by 2 degrees
- `C22`: Press down the tilt angle of 3224831_3 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.100 | MS1 | 121.4656731774 | 31.1446295811 | 749 | 504990 | -89.33 | 15.86 | 431.31 | 0.04 | 2.81 | 1580 |
| 2024-09-20 22:21:32.246 | MS1 | 121.4656622227 | 31.1446266396 | 749 | 504990 | -86.68 | 15.51 | 387.01 | 0.11 | 2.67 | 1586 |
| 2024-09-20 22:21:33.724 | MS1 | 121.4656764816 | 31.1446360196 | 749 | 504990 | -91.13 | 13.71 | 444.60 | 0.12 | 2.55 | 1592 |
| 2024-09-20 22:21:34.856 | MS1 | 121.4656663898 | 31.1446326601 | 749 | 504990 | -88.76 | 14.10 | 82.00 | 0.06 | 2.43 | 1587 |
| 2024-09-20 22:21:35.139 | MS1 | 121.4656691834 | 31.1446323664 | 749 | 504990 | -85.66 | 12.29 | 74.64 | 0.05 | 2.93 | 1564 |
| 2024-09-20 22:21:36.829 | MS1 | 121.4656708906 | 31.1446348979 | 749 | 504990 | -88.09 | 15.50 | 98.78 | 0.04 | 2.34 | 1574 |
| 2024-09-20 22:21:37.454 | MS1 | 121.4656666477 | 31.1446267993 | 749 | 504990 | -92.14 | 7.17 | 78.51 | 0.13 | 2.86 | 1593 |
| 2024-09-20 22:21:38.321 | MS1 | 121.4656761043 | 31.1446216092 | 749 | 504990 | -91.18 | 12.00 | 89.48 | 0.10 | 2.16 | 1561 |
| 2024-09-20 22:21:39.101 | MS1 | 121.4656696078 | 31.1446183815 | 749 | 504990 | -89.40 | 10.84 | 87.81 | 0.08 | 2.92 | 1563 |
| 2024-09-20 22:21:40.344 | MS1 | 121.4656751655 | 31.1446192603 | 749 | 504990 | -90.22 | 12.89 | 392.99 | 0.10 | 2.27 | 1560 |
| 2024-09-20 22:21:41.265 | MS1 | 121.4656639876 | 31.1446366831 | 749 | 504990 | -93.95 | 8.03 | 455.71 | 0.08 | 2.62 | 1588 |
| 2024-09-20 22:21:42.604 | MS1 | 121.4656717407 | 31.1446347527 | 749 | 504990 | -92.61 | 9.48 | 432.35 | 0.19 | 2.18 | 1586 |

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
| 3224831 | 3 | 121.4716518680 | 31.1491211197 | 238 | 1 | 12 | 19.7 | TDD | 749 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3225114 | 4 | 121.4756519833 | 31.1446198573 | 137 | 8 | 3 | 26.5 | TDD | 759 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3231505 | 2 | 121.4751302742 | 31.1528815109 | 162 | 12 | 5 | 27.1 | TDD | 796 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3238198 | 1 | 121.4647815566 | 31.1532828924 | 11 | 13 | 12 | 27.2 | TDD | 879 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.536 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.555 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.686 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.686 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.423 | NREventA3 | measId:2;ServCellPCI:621;Se... |
| 2024-09-20 22:21:38.663 | NRHandoverAttempt | SourcePCI:621;SourceNR-ARFC... |
| 2024-09-20 22:21:38.698 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.710 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.831 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.831 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238198 | 1 | 17.7639 | 13.8244 | -116.7841 | 18.4480 | 105.5672 | 0.0133 | 0.0095 |
| 2024_09_20 22:00 | 3231505 | 2 | 11.8061 | 19.5913 | -114.2356 | 19.6341 | 106.7397 | 0.0169 | 0.0144 |
| 2024_09_20 22:00 | 3224831 | 3 | 75.8753 | 93.9521 | -114.1438 | 19.4155 | 150.1466 | 0.0034 | 0.0047 |
| 2024_09_20 22:00 | 3225114 | 4 | 5.8210 | 10.6026 | -117.9271 | 16.8268 | 120.1669 | 0.0036 | 0.0023 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415977_473C21CA | 504990 | 749 | -88.0 | 504990 | 796 | -88.8 | 504990 | 879 | -103.0 | 504990 | 759 |
| MR_1774415977_ADCD3B4D | 504990 | 749 | -88.7 | 504990 | 796 | -89.5 | 504990 | 879 | -102.7 | 504990 | 759 |
| MR_1774415977_CCD71ACB | 504990 | 749 | -89.6 | 504990 | 796 | -91.4 | 504990 | 879 | -103.4 | 504990 | 759 |
| MR_1774415977_C8E2F251 | 504990 | 749 | -87.7 | 504990 | 796 | -90.1 | 504990 | 879 | -102.1 | 504990 | 759 |
| MR_1774415977_6637210A | 504990 | 749 | -88.9 | 504990 | 796 | -90.8 | 504990 | 879 | -102.2 | 504990 | 759 |
| MR_1774415977_95173884 | 504990 | 749 | -87.7 | 504990 | 796 | -89.8 | 504990 | 879 | -101.4 | 504990 | 759 |
| MR_1774415977_A5BF8248 | 504990 | 749 | -88.9 | 504990 | 796 | -89.4 | 504990 | 879 | -102.1 | 504990 | 759 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1397: `f5e88f71-875...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f5e88f71-8756-4d85-bb1a-88c21e92ebed` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263611_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1397] topology](images/train_1397.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3228605_5 by 26 degrees
- `C2`: Decrease A3 Offset threshold for 3263611_2
- `C3`: Add neighbor relationship between 3263611_2 and 3228605_5
- `C4`: Press down the tilt angle  of 3228605_5 by 2 degrees
- `C5`: Increase A3 Offset threshold for 3228605_5
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263611_2 **← 정답**
- `C7`: Adjust the azimuth of 3263611_2 by 43 degrees
- `C8`: Increase transmission power for 3228605_5
- `C9`: Add neighbor relationship between 3231041_13 and 3228605_5
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228605_5
- `C11`: Check test server and transmission issues
- `C12`: Decrease transmission power for 3263611_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228605_5
- `C14`: Increase A3 Offset threshold for 3263611_2
- `C15`: Increase transmission power for 3263611_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Lift the tilt angle  of 3228605_5 by 2 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263611_2
- `C19`: Decrease transmission power for 3228605_5
- `C20`: Press down the tilt angle of 3263611_2 by 1 degrees
- `C21`: Decrease A3 Offset threshold for 3228605_5
- `C22`: Lift the tilt angle of 3263611_2 by 1 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.185 | MS1 | 121.4656639515 | 31.1446332544 | 621 | 504990 | -93.92 | 14.12 | 345.07 | 0.10 | 2.20 | 1589 |
| 2024-09-20 22:21:32.803 | MS1 | 121.4656745317 | 31.1446345960 | 451 | 504990 | -93.66 | 13.20 | 426.85 | 0.20 | 2.85 | 1575 |
| 2024-09-20 22:21:33.625 | MS1 | 121.4656752365 | 31.1446374348 | 370 | 504990 | -94.63 | 9.76 | 541.35 | 0.02 | 2.08 | 1583 |
| 2024-09-20 22:21:34.609 | MS1 | 121.4656757690 | 31.1446257789 | 465 | 152650 | -96.31 | 4.77 | 65.98 | 0.19 | 1.56 | 948 |
| 2024-09-20 22:21:35.345 | MS1 | 121.4656650104 | 31.1446336691 | 166 | 152650 | -87.66 | 7.18 | 67.62 | 0.20 | 1.87 | 969 |
| 2024-09-20 22:21:36.236 | MS1 | 121.4656714556 | 31.1446211761 | 127 | 152650 | -96.58 | 6.86 | 57.15 | 0.08 | 1.74 | 946 |
| 2024-09-20 22:21:37.534 | MS1 | 121.4656662672 | 31.1446240640 | 796 | 152650 | -92.91 | 7.18 | 52.44 | 0.12 | 1.55 | 962 |
| 2024-09-20 22:21:38.594 | MS1 | 121.4656599154 | 31.1446339687 | 465 | 152650 | -93.35 | 7.18 | 98.66 | 0.02 | 1.94 | 973 |
| 2024-09-20 22:21:39.157 | MS1 | 121.4656737129 | 31.1446319778 | 166 | 152650 | -93.35 | 6.74 | 45.76 | 0.05 | 1.73 | 933 |
| 2024-09-20 22:21:40.904 | MS1 | 121.4656584081 | 31.1446332230 | 127 | 152650 | -94.39 | 5.05 | 66.51 | 0.01 | 2.59 | 1561 |
| 2024-09-20 22:21:41.709 | MS1 | 121.4656687640 | 31.1446371974 | 796 | 152650 | -87.43 | 6.84 | 77.13 | 0.12 | 2.20 | 1562 |
| 2024-09-20 22:21:42.932 | MS1 | 121.4656654635 | 31.1446346209 | 465 | 152650 | -94.50 | 4.69 | 71.55 | 0.10 | 2.99 | 1579 |

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
| 3214064 | 3 | 121.4672496778 | 31.1445703501 | 135 | 11 | 8 | 3.6 | TDD | 109 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3221623 | 1 | 121.4669024820 | 31.1477173809 | 348 | 8 | 0 | 17.3 | TDD | 451 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3225027 | 12 | 121.4651496081 | 31.1474928156 | 133 | 15 | 10 | 20.6 | FDD | 796 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3228605 | 5 | 121.4656959277 | 31.1535303131 | 206 | 1 | 2 | 18.7 | TDD | 221 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3229790 | 6 | 121.4649345045 | 31.1496055418 | 175 | 11 | 1 | 14.5 | TDD | 543 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3231041 | 13 | 121.4675682429 | 31.1486484883 | 211 | 11 | 0 | 0.3 | FDD | 127 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3233336 | 4 | 121.4686594097 | 31.1479789215 | 169 | 11 | 0 | 10.5 | TDD | 370 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3245483 | 11 | 121.4655529787 | 31.1524037426 | 159 | 14 | 11 | 2.4 | FDD | 405 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3255778 | 9 | 121.4744983350 | 31.1468407767 | 178 | 7 | 6 | 16.8 | FDD | 465 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3260809 | 8 | 121.4732186173 | 31.1501961130 | 152 | 2 | 5 | 23.2 | FDD | 331 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3263611 | 2 | 121.4734079753 | 31.1465927866 | 211 | 0 | 12 | 19.6 | TDD | 621 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3278855 | 7 | 121.4675498303 | 31.1476054135 | 181 | 6 | 2 | 10.6 | FDD | 166 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3279584 | 10 | 121.4752737100 | 31.1490242782 | 263 | 15 | 5 | 28.1 | FDD | 244 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |

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
| 2024-09-20 22:21:31.312 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.329 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.459 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.459 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.124 | NREventA2 | measId:1;ServCellPCI:145;Se... |
| 2024-09-20 22:21:35.251 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.541 | NREventA5 | measId:3;ServCellPCI:145;Se... |
| 2024-09-20 22:21:35.601 | NRHandoverAttempt | SourcePCI:145;SourceNR-ARFC... |
| 2024-09-20 22:21:35.648 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.659 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.765 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.765 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221623 | 1 | 9.5010 | 15.4974 | -114.2597 | 6.2669 | 141.9655 | 0.0056 | 0.0049 |
| 2024_09_20 22:00 | 3263611 | 2 | 19.1585 | 8.4100 | -117.1471 | 19.3843 | 169.4650 | 0.0030 | 0.0133 |
| 2024_09_20 22:00 | 3214064 | 3 | 18.5670 | 7.3395 | -114.1286 | 12.8768 | 184.1982 | 0.0120 | 0.0188 |
| 2024_09_20 22:00 | 3233336 | 4 | 17.4257 | 10.1721 | -116.6483 | 8.5520 | 158.3745 | 0.0009 | 0.0112 |
| 2024_09_20 22:00 | 3228605 | 5 | 5.1380 | 7.2696 | -116.1065 | 8.8816 | 194.9671 | 0.0031 | 0.0096 |
| 2024_09_20 22:00 | 3229790 | 6 | 14.5878 | 12.1117 | -115.1435 | 10.9164 | 131.8554 | 0.0031 | 0.0029 |
| 2024_09_20 22:00 | 3278855 | 7 | 11.6975 | 7.8538 | -116.1060 | 3.6080 | 53.3508 | 0.0149 | 0.0033 |
| 2024_09_20 22:00 | 3260809 | 8 | 15.6497 | 15.5098 | -116.8912 | 3.5756 | 31.9206 | 0.0097 | 0.0017 |
| 2024_09_20 22:00 | 3255778 | 9 | 7.1362 | 11.5527 | -115.2577 | 3.8820 | 27.4437 | 0.0039 | 0.0051 |
| 2024_09_20 22:00 | 3279584 | 10 | 14.4774 | 14.1643 | -117.4453 | 4.0599 | 36.6758 | 0.0124 | 0.0179 |
| 2024_09_20 22:00 | 3245483 | 11 | 9.8832 | 9.5026 | -117.2138 | 4.3267 | 50.5385 | 0.0107 | 0.0011 |
| 2024_09_20 22:00 | 3225027 | 12 | 7.9869 | 12.4792 | -117.0563 | 3.0399 | 57.3415 | 0.0152 | 0.0089 |
| 2024_09_20 22:00 | 3231041 | 13 | 7.0303 | 7.2698 | -114.7002 | 4.1023 | 38.9196 | 0.0041 | 0.0186 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417005_D6ECC99A | 504990 | 370 | -96.6 | 504990 | 221 | -92.0 | 504990 | 543 | -92.2 | 504990 | 109 |
| MR_1774417005_4319D801 | 152650 | 465 | -97.1 | 152650 | 244 | -100.3 | 152650 | 331 | -102.8 | 152650 | 405 |
| MR_1774417005_5FE44D7E | 504990 | 370 | -96.5 | 504990 | 221 | -92.6 | 504990 | 543 | -95.2 | 504990 | 109 |
| MR_1774417005_8E752A8E | 152650 | 465 | -97.1 | 152650 | 244 | -101.5 | 152650 | 331 | -103.0 | 152650 | 405 |
| MR_1774417005_437E9E40 | 152650 | 465 | -95.4 | 152650 | 244 | -100.6 | 152650 | 331 | -105.7 | 152650 | 405 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1398: `3c4f1ae3-bbc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3c4f1ae3-bbc2-4b59-bb97-0c5b818ef9e4` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1398] topology](images/train_1398.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3265372_2
- `C2`: Lift the tilt angle of 3277945_1 by 10 degrees
- `C3`: Add neighbor relationship between 3277945_1 and 3265372_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265372_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277945_1
- `C6`: Add neighbor relationship between 3229843_3 and 3265372_2
- `C7`: Decrease A3 Offset threshold for 3277945_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265372_2
- `C9`: Lift the tilt angle  of 3265372_2 by 9 degrees
- `C10`: Increase transmission power for 3277945_1
- `C11`: Increase transmission power for 3265372_2
- `C12`: Decrease transmission power for 3277945_1
- `C13`: Adjust the azimuth of 3265372_2 by 50 degrees
- `C14`: Decrease transmission power for 3265372_2
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277945_1
- `C17`: Check test server and transmission issues **← 정답**
- `C18`: Increase A3 Offset threshold for 3265372_2
- `C19`: Adjust the azimuth of 3277945_1 by 47 degrees
- `C20`: Press down the tilt angle of 3277945_1 by 10 degrees
- `C21`: Increase A3 Offset threshold for 3277945_1
- `C22`: Press down the tilt angle  of 3265372_2 by 9 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.231 | MS1 | 121.4656648163 | 31.1446259588 | 167 | 504990 | -90.69 | 15.48 | 603.70 | 0.07 | 2.04 | 1579 |
| 2024-09-20 22:21:32.950 | MS1 | 121.4656660179 | 31.1446182836 | 167 | 504990 | -91.39 | 15.26 | 452.19 | 0.15 | 2.97 | 1560 |
| 2024-09-20 22:21:33.698 | MS1 | 121.4656592610 | 31.1446210315 | 167 | 504990 | -89.13 | 17.86 | 416.59 | 0.20 | 2.82 | 1583 |
| 2024-09-20 22:21:34.580 | MS1 | 121.4656722557 | 31.1446343034 | 167 | 504990 | -90.42 | 12.43 | 64.41 | 0.19 | 2.84 | 422 |
| 2024-09-20 22:21:35.536 | MS1 | 121.4656704440 | 31.1446189599 | 167 | 504990 | -91.42 | 12.13 | 100.37 | 0.13 | 2.05 | 303 |
| 2024-09-20 22:21:36.213 | MS1 | 121.4656593448 | 31.1446256833 | 167 | 504990 | -86.24 | 16.30 | 88.53 | 0.07 | 2.70 | 386 |
| 2024-09-20 22:21:37.324 | MS1 | 121.4656746812 | 31.1446342508 | 167 | 504990 | -90.44 | 12.56 | 56.83 | 0.06 | 2.06 | 302 |
| 2024-09-20 22:21:38.319 | MS1 | 121.4656647087 | 31.1446233598 | 167 | 504990 | -91.44 | 7.42 | 59.57 | 0.11 | 2.94 | 435 |
| 2024-09-20 22:21:39.413 | MS1 | 121.4656695741 | 31.1446344091 | 167 | 504990 | -92.73 | 10.91 | 65.94 | 0.09 | 2.01 | 456 |
| 2024-09-20 22:21:40.888 | MS1 | 121.4656696068 | 31.1446214004 | 167 | 504990 | -91.37 | 11.48 | 492.61 | 0.09 | 2.42 | 1580 |
| 2024-09-20 22:21:41.121 | MS1 | 121.4656715139 | 31.1446351726 | 167 | 504990 | -90.06 | 12.79 | 582.36 | 0.15 | 2.39 | 1561 |
| 2024-09-20 22:21:42.239 | MS1 | 121.4656773253 | 31.1446263855 | 167 | 504990 | -93.48 | 11.97 | 515.13 | 0.07 | 2.52 | 1563 |

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
| 3229843 | 3 | 121.4683362911 | 31.1478304207 | 183 | 4 | 3 | 43.8 | TDD | 863 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3232414 | 4 | 121.4715557953 | 31.1489311645 | 183 | 14 | 3 | 28.2 | TDD | 399 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3265372 | 2 | 121.4645519880 | 31.1513848943 | 83 | 8 | 7 | 16.8 | TDD | 523 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3277945 | 1 | 121.4667754317 | 31.1539081387 | 233 | 15 | 4 | 37.2 | TDD | 167 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.042 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.057 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.206 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.206 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.857 | NREventA3 | measId:2;ServCellPCI:770;Se... |
| 2024-09-20 22:21:38.097 | NRHandoverAttempt | SourcePCI:770;SourceNR-ARFC... |
| 2024-09-20 22:21:38.137 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.151 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.265 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.265 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277945 | 1 | 16.6432 | 15.4101 | -117.3011 | 14.4099 | 188.8493 | 0.0156 | 0.0058 |
| 2024_09_20 22:00 | 3265372 | 2 | 19.8524 | 18.0278 | -117.2647 | 12.2132 | 142.2734 | 0.0090 | 0.0066 |
| 2024_09_20 22:00 | 3229843 | 3 | 6.0714 | 16.3143 | -116.0374 | 5.5338 | 119.5207 | 0.0140 | 0.0118 |
| 2024_09_20 22:00 | 3232414 | 4 | 18.7342 | 19.8554 | -114.5380 | 19.2279 | 181.3774 | 0.0189 | 0.0064 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416074_6194F782 | 504990 | 167 | -89.7 | 504990 | 523 | -94.4 | 504990 | 863 | -98.3 | 504990 | 399 |
| MR_1774416074_0A45BC34 | 504990 | 167 | -92.0 | 504990 | 523 | -94.6 | 504990 | 863 | -99.2 | 504990 | 399 |
| MR_1774416074_3A88BD1E | 504990 | 167 | -89.0 | 504990 | 523 | -94.7 | 504990 | 863 | -99.4 | 504990 | 399 |
| MR_1774416074_A72CAA67 | 504990 | 167 | -90.2 | 504990 | 523 | -93.9 | 504990 | 863 | -99.0 | 504990 | 399 |
| MR_1774416074_9D890954 | 504990 | 167 | -88.7 | 504990 | 523 | -92.6 | 504990 | 863 | -98.2 | 504990 | 399 |
| MR_1774416074_70925462 | 504990 | 167 | -90.3 | 504990 | 523 | -94.7 | 504990 | 863 | -97.5 | 504990 | 399 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1399: `5e098e1a-591...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5e098e1a-5919-43cf-b37f-fa340c60bdaf` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250252_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1399] topology](images/train_1399.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3250252_4
- `C2`: Increase A3 Offset threshold for 3264572_5
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264572_5
- `C4`: Add neighbor relationship between 3244301_11 and 3264572_5
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250252_4 **← 정답**
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264572_5
- `C7`: Press down the tilt angle  of 3264572_5 by 6 degrees
- `C8`: Adjust the azimuth of 3264572_5 by 15 degrees
- `C9`: Increase A3 Offset threshold for 3250252_4
- `C10`: Lift the tilt angle of 3250252_4 by 4 degrees
- `C11`: Adjust the azimuth of 3250252_4 by 14 degrees
- `C12`: Decrease A3 Offset threshold for 3264572_5
- `C13`: Increase transmission power for 3264572_5
- `C14`: Decrease transmission power for 3250252_4
- `C15`: Check test server and transmission issues
- `C16`: Press down the tilt angle of 3250252_4 by 4 degrees
- `C17`: Lift the tilt angle  of 3264572_5 by 6 degrees
- `C18`: Decrease transmission power for 3264572_5
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Add neighbor relationship between 3250252_4 and 3264572_5
- `C21`: Increase transmission power for 3250252_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250252_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.348 | MS1 | 121.4656694902 | 31.1446259603 | 616 | 504990 | -95.78 | 9.89 | 570.33 | 0.09 | 2.82 | 1597 |
| 2024-09-20 22:21:32.753 | MS1 | 121.4656697229 | 31.1446247861 | 960 | 504990 | -94.02 | 10.17 | 591.94 | 0.12 | 2.50 | 1589 |
| 2024-09-20 22:21:33.646 | MS1 | 121.4656678819 | 31.1446300199 | 69 | 504990 | -95.53 | 9.37 | 527.06 | 0.15 | 2.27 | 1600 |
| 2024-09-20 22:21:34.997 | MS1 | 121.4656751278 | 31.1446210673 | 34 | 152650 | -91.19 | 5.79 | 64.07 | 0.02 | 1.72 | 922 |
| 2024-09-20 22:21:35.620 | MS1 | 121.4656778544 | 31.1446281360 | 264 | 152650 | -93.77 | 7.22 | 94.85 | 0.02 | 1.60 | 971 |
| 2024-09-20 22:21:36.612 | MS1 | 121.4656741750 | 31.1446205033 | 212 | 152650 | -88.32 | 6.68 | 79.94 | 0.16 | 1.73 | 920 |
| 2024-09-20 22:21:37.616 | MS1 | 121.4656762238 | 31.1446320681 | 648 | 152650 | -94.97 | 2.42 | 74.36 | 0.05 | 1.78 | 959 |
| 2024-09-20 22:21:38.821 | MS1 | 121.4656598707 | 31.1446315413 | 34 | 152650 | -90.41 | 2.03 | 82.61 | 0.14 | 1.93 | 943 |
| 2024-09-20 22:21:39.129 | MS1 | 121.4656736311 | 31.1446264493 | 264 | 152650 | -94.47 | 3.86 | 73.87 | 0.14 | 1.57 | 983 |
| 2024-09-20 22:21:40.364 | MS1 | 121.4656591560 | 31.1446254667 | 212 | 152650 | -95.87 | 3.02 | 55.79 | 0.05 | 2.88 | 1596 |
| 2024-09-20 22:21:41.387 | MS1 | 121.4656720274 | 31.1446367573 | 648 | 152650 | -91.02 | 2.82 | 78.05 | 0.15 | 2.91 | 1569 |
| 2024-09-20 22:21:42.648 | MS1 | 121.4656704026 | 31.1446252292 | 34 | 152650 | -92.71 | 5.21 | 81.66 | 0.16 | 2.93 | 1560 |

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
| 3214626 | 10 | 121.4675165543 | 31.1473476743 | 300 | 14 | 12 | 13.1 | FDD | 648 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3216443 | 13 | 121.4673838600 | 31.1459277765 | 128 | 7 | 1 | 13.9 | FDD | 414 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3241166 | 6 | 121.4660774707 | 31.1543410266 | 161 | 11 | 1 | 5.9 | TDD | 788 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3244301 | 11 | 121.4751171437 | 31.1555076534 | 21 | 4 | 2 | 4.9 | FDD | 212 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3244651 | 3 | 121.4741526044 | 31.1488013045 | 250 | 10 | 12 | 15.7 | TDD | 69 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3246241 | 2 | 121.4714787868 | 31.1462384666 | 264 | 10 | 1 | 9.9 | TDD | 995 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3248431 | 8 | 121.4683464598 | 31.1488311665 | 330 | 15 | 10 | 13.9 | FDD | 227 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3250252 | 4 | 121.4668548792 | 31.1487419824 | 208 | 3 | 4 | 9.3 | TDD | 616 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3253173 | 7 | 121.4755762144 | 31.1457793838 | 189 | 3 | 8 | 16.2 | FDD | 34 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3257805 | 12 | 121.4660078230 | 31.1518128102 | 335 | 0 | 10 | 4.5 | FDD | 56 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3260052 | 9 | 121.4659739836 | 31.1555056686 | 271 | 0 | 3 | 2.9 | FDD | 264 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3264572 | 5 | 121.4680249772 | 31.1540562346 | 177 | 5 | 0 | 11.1 | TDD | 815 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3276861 | 1 | 121.4754109744 | 31.1523732399 | 338 | 7 | 8 | 6.1 | TDD | 960 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.641 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.665 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.779 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.779 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.454 | NREventA2 | measId:1;ServCellPCI:693;Se... |
| 2024-09-20 22:21:35.587 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.832 | NREventA5 | measId:3;ServCellPCI:693;Se... |
| 2024-09-20 22:21:35.887 | NRHandoverAttempt | SourcePCI:693;SourceNR-ARFC... |
| 2024-09-20 22:21:35.921 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.935 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.084 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.084 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276861 | 1 | 9.1178 | 13.4682 | -115.0683 | 12.9464 | 198.1495 | 0.0070 | 0.0192 |
| 2024_09_20 22:00 | 3246241 | 2 | 13.3756 | 15.4935 | -114.3976 | 12.0268 | 135.1099 | 0.0064 | 0.0008 |
| 2024_09_20 22:00 | 3244651 | 3 | 19.8963 | 15.5677 | -114.3025 | 9.8401 | 103.8913 | 0.0020 | 0.0066 |
| 2024_09_20 22:00 | 3250252 | 4 | 12.2695 | 5.2394 | -116.1501 | 12.6906 | 133.8668 | 0.0040 | 0.0145 |
| 2024_09_20 22:00 | 3264572 | 5 | 13.9590 | 8.9913 | -114.6007 | 5.6243 | 102.4287 | 0.0098 | 0.0084 |
| 2024_09_20 22:00 | 3241166 | 6 | 5.8085 | 9.3530 | -114.7304 | 7.4992 | 102.1202 | 0.0176 | 0.0034 |
| 2024_09_20 22:00 | 3253173 | 7 | 10.8986 | 15.9110 | -116.4906 | 3.1983 | 20.1471 | 0.0005 | 0.0181 |
| 2024_09_20 22:00 | 3248431 | 8 | 17.8052 | 10.4813 | -117.4908 | 3.8634 | 28.1644 | 0.0143 | 0.0086 |
| 2024_09_20 22:00 | 3260052 | 9 | 19.2879 | 15.1467 | -114.5693 | 4.0089 | 45.4143 | 0.0123 | 0.0047 |
| 2024_09_20 22:00 | 3214626 | 10 | 19.5953 | 8.4550 | -114.6404 | 3.7911 | 36.3207 | 0.0046 | 0.0192 |
| 2024_09_20 22:00 | 3244301 | 11 | 8.3679 | 15.5625 | -114.9963 | 3.2106 | 47.7931 | 0.0190 | 0.0174 |
| 2024_09_20 22:00 | 3257805 | 12 | 19.4536 | 19.0610 | -115.6260 | 4.8059 | 20.7694 | 0.0163 | 0.0027 |
| 2024_09_20 22:00 | 3216443 | 13 | 12.0603 | 19.9505 | -117.2925 | 4.0790 | 52.6213 | 0.0136 | 0.0111 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412114_663694BF | 152650 | 34 | -89.3 | 152650 | 56 | -95.5 | 152650 | 414 | -98.4 | 152650 | 227 |
| MR_1774412114_355A8632 | 504990 | 69 | -94.7 | 504990 | 815 | -93.0 | 504990 | 788 | -99.1 | 504990 | 995 |
| MR_1774412114_59D84DF0 | 504990 | 69 | -93.8 | 504990 | 815 | -92.7 | 504990 | 788 | -97.2 | 504990 | 995 |
| MR_1774412114_845D3562 | 504990 | 69 | -96.4 | 504990 | 815 | -92.8 | 504990 | 788 | -98.0 | 504990 | 995 |
| MR_1774412114_D10CC5A4 | 152650 | 34 | -90.6 | 152650 | 56 | -96.8 | 152650 | 414 | -98.5 | 152650 | 227 |
| MR_1774412114_41BA553B | 152650 | 34 | -90.7 | 152650 | 56 | -95.4 | 152650 | 414 | -99.0 | 152650 | 227 |
| MR_1774412114_A03B65ED | 152650 | 34 | -92.3 | 152650 | 56 | -96.0 | 152650 | 414 | -99.9 | 152650 | 227 |
| MR_1774412114_FD6EED63 | 152650 | 34 | -92.1 | 152650 | 56 | -97.9 | 152650 | 414 | -99.0 | 152650 | 227 |

> *... 2개 열 생략 (전체 14열)*

---
