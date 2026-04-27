# Track A 문제 분석 — train[1300]~train[1309]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1300] ~ train[1309] (10개)

## 목차

1. [문제 1300: `1f65da35-9c4...`](#1300) — single-answer, 정답: C14
2. [문제 1301: `8f7047aa-65a...`](#1301) — single-answer, 정답: C15
3. [문제 1302: `f6296c25-c55...`](#1302) — single-answer, 정답: C10
4. [문제 1303: `472277e1-e4f...`](#1303) — single-answer, 정답: C19
5. [문제 1304: `e578de97-7ff...`](#1304) — single-answer, 정답: C18
6. [문제 1305: `bc7c8362-f83...`](#1305) — single-answer, 정답: C21
7. [문제 1306: `1ffcdf1e-15c...`](#1306) — single-answer, 정답: C5
8. [문제 1307: `0ea9a70e-f33...`](#1307) — single-answer, 정답: C3
9. [문제 1308: `ef748e40-b24...`](#1308) — multiple-answer, 정답: C19|C22
10. [문제 1309: `377a0d30-18b...`](#1309) — single-answer, 정답: C18

---

### 문제 1300: `1f65da35-9c4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1f65da35-9c47-41c8-864b-ad0493e4c41e` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease A3 Offset threshold for 3262095_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1300] topology](images/train_1300.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3262095_1 by 50 degrees
- `C2`: Press down the tilt angle of 3262095_1 by 10 degrees
- `C3`: Increase transmission power for 3262095_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247936_3
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease transmission power for 3262095_1
- `C7`: Press down the tilt angle  of 3247936_3 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262095_1
- `C9`: Decrease A3 Offset threshold for 3247936_3
- `C10`: Adjust the azimuth of 3247936_3 by 50 degrees
- `C11`: Decrease transmission power for 3247936_3
- `C12`: Add neighbor relationship between 3262095_1 and 3247936_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262095_1
- `C14`: Decrease A3 Offset threshold for 3262095_1 **← 정답**
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247936_3
- `C16`: Check test server and transmission issues
- `C17`: Add neighbor relationship between 3272562_2 and 3247936_3
- `C18`: Lift the tilt angle of 3262095_1 by 10 degrees
- `C19`: Lift the tilt angle  of 3247936_3 by 10 degrees
- `C20`: Increase transmission power for 3247936_3
- `C21`: Increase A3 Offset threshold for 3262095_1
- `C22`: Increase A3 Offset threshold for 3247936_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.705 | MS1 | 121.4656611027 | 31.1446296124 | 513 | 504990 | -83.33 | 16.50 | 594.82 | 0.05 | 2.25 | 1572 |
| 2024-09-20 22:21:32.881 | MS1 | 121.4656679254 | 31.1446310496 | 513 | 504990 | -75.93 | 15.03 | 377.06 | 0.17 | 2.20 | 1576 |
| 2024-09-20 22:21:33.846 | MS1 | 121.4656760441 | 31.1446366944 | 513 | 504990 | -76.30 | 14.14 | 544.21 | 0.04 | 2.96 | 1567 |
| 2024-09-20 22:21:34.766 | MS1 | 121.4656712279 | 31.1446185609 | 513 | 504990 | -86.61 | -0.54 | 54.90 | 0.17 | 1.02 | 1583 |
| 2024-09-20 22:21:35.691 | MS1 | 121.4656691628 | 31.1446264544 | 513 | 504990 | -84.08 | -2.29 | 72.25 | 0.16 | 1.14 | 1577 |
| 2024-09-20 22:21:36.754 | MS1 | 121.4656663169 | 31.1446280551 | 513 | 504990 | -84.89 | -0.40 | 70.78 | 0.16 | 1.41 | 1580 |
| 2024-09-20 22:21:37.280 | MS1 | 121.4656742076 | 31.1446216649 | 513 | 504990 | -83.19 | -2.11 | 55.79 | 0.08 | 1.45 | 1561 |
| 2024-09-20 22:21:38.257 | MS1 | 121.4656642697 | 31.1446263462 | 513 | 504990 | -88.23 | -1.20 | 57.61 | 0.11 | 1.27 | 1566 |
| 2024-09-20 22:21:39.496 | MS1 | 121.4656604942 | 31.1446327882 | 805 | 504990 | -79.93 | 17.62 | 217.50 | 0.00 | 1.07 | 1571 |
| 2024-09-20 22:21:40.389 | MS1 | 121.4656726810 | 31.1446213055 | 805 | 504990 | -75.75 | 14.75 | 321.36 | 0.02 | 2.20 | 1580 |
| 2024-09-20 22:21:41.540 | MS1 | 121.4656749366 | 31.1446320117 | 805 | 504990 | -78.64 | 12.18 | 603.21 | 0.05 | 2.74 | 1572 |
| 2024-09-20 22:21:42.390 | MS1 | 121.4656641545 | 31.1446371490 | 805 | 504990 | -78.06 | 14.16 | 570.73 | 0.14 | 2.90 | 1560 |

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
| 3247936 | 3 | 121.4675346353 | 31.1443819967 | 184 | 4 | 5 | 25.5 | TDD | 805 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3262095 | 1 | 121.4673499235 | 31.1490018517 | 304 | 13 | 12 | 32.5 | TDD | 513 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3272562 | 2 | 121.4714927404 | 31.1472286826 | 126 | 8 | 5 | 27.3 | TDD | 506 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3276181 | 4 | 121.4673643092 | 31.1450618192 | 54 | 3 | 7 | 18.6 | TDD | 634 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.308 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.323 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.446 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.446 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.148 | NREventA3 | measId:2;ServCellPCI:168;Se... |
| 2024-09-20 22:21:38.388 | NRHandoverAttempt | SourcePCI:168;SourceNR-ARFC... |
| 2024-09-20 22:21:38.418 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.428 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.531 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.531 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262095 | 1 | 12.4304 | 19.8930 | -115.7954 | 6.3462 | 86.6005 | 0.0168 | 0.1554 |
| 2024_09_20 22:00 | 3272562 | 2 | 12.8669 | 14.4037 | -114.8832 | 6.1787 | 169.6179 | 0.0038 | 0.0158 |
| 2024_09_20 22:00 | 3247936 | 3 | 17.8880 | 5.7140 | -117.3826 | 15.3660 | 185.4983 | 0.0063 | 0.0170 |
| 2024_09_20 22:00 | 3276181 | 4 | 15.5133 | 5.9641 | -114.0409 | 19.3496 | 92.5149 | 0.0134 | 0.0162 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412809_218A4B6A | 504990 | 513 | -87.4 | 504990 | 805 | -80.8 | 504990 | 506 | -91.4 | 504990 | 634 |
| MR_1774412809_A47D9707 | 504990 | 513 | -87.1 | 504990 | 805 | -80.1 | 504990 | 506 | -92.5 | 504990 | 634 |
| MR_1774412809_F9F98600 | 504990 | 805 | -82.6 | 504990 | 513 | -85.3 | 504990 | 506 | -88.8 | 504990 | 634 |
| MR_1774412809_6B8A11F6 | 504990 | 513 | -85.0 | 504990 | 805 | -81.0 | 504990 | 506 | -90.7 | 504990 | 634 |
| MR_1774412809_BDDC9C60 | 504990 | 805 | -79.3 | 504990 | 513 | -85.2 | 504990 | 506 | -92.3 | 504990 | 634 |
| MR_1774412809_82CE8F83 | 504990 | 805 | -79.2 | 504990 | 513 | -84.8 | 504990 | 506 | -89.0 | 504990 | 634 |
| MR_1774412809_E22571F8 | 504990 | 513 | -85.3 | 504990 | 805 | -80.3 | 504990 | 506 | -92.0 | 504990 | 634 |
| MR_1774412809_D4959779 | 504990 | 805 | -82.3 | 504990 | 513 | -84.7 | 504990 | 506 | -89.5 | 504990 | 634 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1301: `8f7047aa-65a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8f7047aa-65a1-4660-9b31-0a018aa7cb79` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Lift the tilt angle  of 3211799_2 by 6 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1301] topology](images/train_1301.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3236636_4
- `C2`: Increase transmission power for 3274754_3
- `C3`: Press down the tilt angle of 3274754_3 by 1 degrees
- `C4`: Adjust the azimuth of 3211799_2 by 50 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236636_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274754_3
- `C7`: Decrease A3 Offset threshold for 3236636_4
- `C8`: Increase A3 Offset threshold for 3274754_3
- `C9`: Decrease transmission power for 3274754_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236636_4
- `C11`: Increase A3 Offset threshold for 3236636_4
- `C12`: Add neighbor relationship between 3274754_3 and 3236636_4
- `C13`: Add neighbor relationship between 3211799_2 and 3236636_4
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Lift the tilt angle  of 3211799_2 by 6 degrees **← 정답**
- `C16`: Press down the tilt angle  of 3211799_2 by 6 degrees
- `C17`: Increase transmission power for 3236636_4
- `C18`: Decrease A3 Offset threshold for 3274754_3
- `C19`: Adjust the azimuth of 3274754_3 by 50 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274754_3
- `C21`: Check test server and transmission issues
- `C22`: Lift the tilt angle of 3274754_3 by 1 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.132 | MS1 | 121.4656777088 | 31.1446197157 | 708 | 504990 | -88.12 | 17.02 | 359.13 | 0.05 | 2.54 | 1560 |
| 2024-09-20 22:21:32.631 | MS1 | 121.4656656174 | 31.1446264215 | 708 | 504990 | -85.19 | 13.04 | 531.08 | 0.05 | 2.16 | 1574 |
| 2024-09-20 22:21:33.209 | MS1 | 121.4656708002 | 31.1446246247 | 708 | 504990 | -87.08 | 16.09 | 445.43 | 0.14 | 2.87 | 1585 |
| 2024-09-20 22:21:34.190 | MS1 | 121.4656610801 | 31.1446252982 | 708 | 504990 | -88.62 | 14.41 | 43.53 | 0.06 | 2.62 | 1569 |
| 2024-09-20 22:21:35.937 | MS1 | 121.4656655058 | 31.1446198818 | 708 | 504990 | -89.98 | 15.30 | 95.12 | 0.03 | 2.01 | 1562 |
| 2024-09-20 22:21:36.365 | MS1 | 121.4656683971 | 31.1446319776 | 708 | 504990 | -91.49 | 15.61 | 45.99 | 0.15 | 2.01 | 1592 |
| 2024-09-20 22:21:37.326 | MS1 | 121.4656602486 | 31.1446327706 | 708 | 504990 | -90.45 | 8.41 | 69.38 | 0.01 | 2.83 | 1563 |
| 2024-09-20 22:21:38.822 | MS1 | 121.4656736154 | 31.1446181110 | 708 | 504990 | -89.74 | 11.65 | 57.82 | 0.14 | 2.55 | 1565 |
| 2024-09-20 22:21:39.398 | MS1 | 121.4656612027 | 31.1446285100 | 708 | 504990 | -89.25 | 8.04 | 61.77 | 0.16 | 2.08 | 1564 |
| 2024-09-20 22:21:40.570 | MS1 | 121.4656653568 | 31.1446377913 | 708 | 504990 | -90.53 | 12.41 | 492.95 | 0.07 | 2.56 | 1589 |
| 2024-09-20 22:21:41.852 | MS1 | 121.4656723822 | 31.1446257544 | 708 | 504990 | -92.84 | 10.60 | 484.13 | 0.08 | 2.29 | 1591 |
| 2024-09-20 22:21:42.259 | MS1 | 121.4656612734 | 31.1446252002 | 708 | 504990 | -90.16 | 10.01 | 430.93 | 0.03 | 2.52 | 1594 |

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
| 3211799 | 2 | 121.4684418544 | 31.1461916599 | 42 | 8 | 1 | 17.4 | TDD | 369 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3236636 | 4 | 121.4692728263 | 31.1530164529 | 150 | 4 | 3 | 35.2 | TDD | 679 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3244734 | 1 | 121.4685513512 | 31.1516247787 | 255 | 14 | 12 | 27.3 | TDD | 376 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3274754 | 3 | 121.4651110676 | 31.1558027151 | 128 | 0 | 9 | 18.9 | TDD | 708 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.124 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.146 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.294 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.294 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.966 | NREventA3 | measId:2;ServCellPCI:910;Se... |
| 2024-09-20 22:21:38.206 | NRHandoverAttempt | SourcePCI:910;SourceNR-ARFC... |
| 2024-09-20 22:21:38.250 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.265 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.374 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.374 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244734 | 1 | 7.3757 | 8.2706 | -116.5303 | 5.6753 | 132.5877 | 0.0048 | 0.0172 |
| 2024_09_20 22:00 | 3211799 | 2 | 6.7597 | 15.2033 | -117.4837 | 16.3284 | 98.4808 | 0.0119 | 0.0135 |
| 2024_09_20 22:00 | 3274754 | 3 | 78.2171 | 82.1847 | -116.4293 | 8.1965 | 159.6247 | 0.0020 | 0.0184 |
| 2024_09_20 22:00 | 3236636 | 4 | 13.6742 | 17.7361 | -116.4682 | 15.1855 | 193.9515 | 0.0042 | 0.0124 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416928_347D9137 | 504990 | 708 | -88.3 | 504990 | 679 | -89.3 | 504990 | 369 | -101.4 | 504990 | 376 |
| MR_1774416928_C59CF893 | 504990 | 708 | -88.8 | 504990 | 679 | -90.7 | 504990 | 369 | -97.4 | 504990 | 376 |
| MR_1774416928_FA952FE4 | 504990 | 708 | -90.5 | 504990 | 679 | -89.6 | 504990 | 369 | -100.4 | 504990 | 376 |
| MR_1774416928_1FC1C869 | 504990 | 708 | -88.5 | 504990 | 679 | -89.0 | 504990 | 369 | -100.5 | 504990 | 376 |
| MR_1774416928_10A5705C | 504990 | 708 | -90.0 | 504990 | 679 | -89.3 | 504990 | 369 | -98.1 | 504990 | 376 |
| MR_1774416928_33F5FC90 | 504990 | 708 | -89.3 | 504990 | 679 | -89.9 | 504990 | 369 | -99.1 | 504990 | 376 |
| MR_1774416928_EDFC2EBE | 504990 | 708 | -89.1 | 504990 | 679 | -91.0 | 504990 | 369 | -100.7 | 504990 | 376 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1302: `f6296c25-c55...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f6296c25-c556-45c1-8393-e4b0035c004f` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1302] topology](images/train_1302.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215806_2
- `C2`: Add neighbor relationship between 3252386_3 and 3215806_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215806_2
- `C4`: Decrease transmission power for 3252386_3
- `C5`: Add neighbor relationship between 3242157_4 and 3215806_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252386_3
- `C7`: Adjust the azimuth of 3215806_2 by 48 degrees
- `C8`: Decrease transmission power for 3215806_2
- `C9`: Increase transmission power for 3215806_2
- `C10`: Insufficient data; more data is needed for judgment. **← 정답**
- `C11`: Press down the tilt angle of 3252386_3 by 6 degrees
- `C12`: Increase A3 Offset threshold for 3215806_2
- `C13`: Increase A3 Offset threshold for 3252386_3
- `C14`: Decrease A3 Offset threshold for 3215806_2
- `C15`: Press down the tilt angle  of 3215806_2 by 6 degrees
- `C16`: Lift the tilt angle of 3252386_3 by 6 degrees
- `C17`: Adjust the azimuth of 3252386_3 by 50 degrees
- `C18`: Check test server and transmission issues
- `C19`: Lift the tilt angle  of 3215806_2 by 6 degrees
- `C20`: Increase transmission power for 3252386_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252386_3
- `C22`: Decrease A3 Offset threshold for 3252386_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.696 | MS1 | 121.4656599039 | 31.1446286241 | 28 | 504990 | -91.42 | 13.36 | 408.98 | 0.18 | 2.27 | 1579 |
| 2024-09-20 22:21:32.325 | MS1 | 121.4656642959 | 31.1446196187 | 28 | 504990 | -85.65 | 14.44 | 421.69 | 0.01 | 2.46 | 1572 |
| 2024-09-20 22:21:33.622 | MS1 | 121.4656668687 | 31.1446362015 | 28 | 504990 | -85.88 | 16.30 | 518.78 | 0.12 | 2.61 | 1576 |
| 2024-09-20 22:21:34.443 | MS1 | 121.4656772436 | 31.1446379718 | 28 | 504990 | -91.74 | 16.30 | 57.83 | 0.06 | 2.04 | 1588 |
| 2024-09-20 22:21:35.920 | MS1 | 121.4656745623 | 31.1446253726 | 28 | 504990 | -90.07 | 12.24 | 96.30 | 0.02 | 2.01 | 1576 |
| 2024-09-20 22:21:36.489 | MS1 | 121.4656650565 | 31.1446289666 | 28 | 504990 | -89.74 | 16.26 | 40.32 | 0.07 | 2.13 | 1596 |
| 2024-09-20 22:21:37.483 | MS1 | 121.4656678980 | 31.1446180930 | 28 | 504990 | -91.57 | 12.55 | 66.94 | 0.14 | 2.71 | 1574 |
| 2024-09-20 22:21:38.318 | MS1 | 121.4656740196 | 31.1446216438 | 28 | 504990 | -90.13 | 9.73 | 74.27 | 0.04 | 2.35 | 1571 |
| 2024-09-20 22:21:39.386 | MS1 | 121.4656611022 | 31.1446333286 | 28 | 504990 | -91.53 | 7.71 | 73.11 | 0.00 | 2.32 | 1578 |
| 2024-09-20 22:21:40.926 | MS1 | 121.4656743434 | 31.1446286348 | 28 | 504990 | -93.89 | 11.93 | 510.80 | 0.03 | 2.77 | 1564 |
| 2024-09-20 22:21:41.880 | MS1 | 121.4656612735 | 31.1446351637 | 28 | 504990 | -90.08 | 10.07 | 429.05 | 0.04 | 2.28 | 1561 |
| 2024-09-20 22:21:42.587 | MS1 | 121.4656672547 | 31.1446317437 | 28 | 504990 | -92.23 | 8.48 | 398.47 | 0.09 | 2.53 | 1581 |

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
| 3215806 | 2 | 121.4729262197 | 31.1475315311 | 293 | 2 | 4 | 49.2 | TDD | 347 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3242157 | 4 | 121.4674066255 | 31.1547409468 | 195 | 9 | 11 | 33.9 | TDD | 45 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3252386 | 3 | 121.4746022639 | 31.1484330538 | 315 | 5 | 4 | 15.1 | TDD | 28 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3259139 | 1 | 121.4665308926 | 31.1517808928 | 127 | 3 | 8 | 43.2 | TDD | 657 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.224 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.239 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.384 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.384 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.116 | NREventA3 | measId:2;ServCellPCI:631;Se... |
| 2024-09-20 22:21:38.356 | NRHandoverAttempt | SourcePCI:631;SourceNR-ARFC... |
| 2024-09-20 22:21:38.391 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.402 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.548 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.548 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3259139 | 1 | 91.7346 | 83.4284 | -114.5928 | 7.7187 | 178.9565 | 0.0164 | 0.0103 |
| 2024_09_19 22:00 | 3215806 | 2 | 77.3882 | 89.9012 | -117.6539 | 7.6104 | 120.9309 | 0.0142 | 0.0142 |
| 2024_09_19 22:00 | 3252386 | 3 | 88.5520 | 92.5906 | -115.1067 | 13.7289 | 88.0198 | 0.0106 | 0.0034 |
| 2024_09_19 22:00 | 3242157 | 4 | 76.9561 | 87.4837 | -117.4160 | 15.1437 | 105.1633 | 0.0161 | 0.0141 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414512_27A59F91 | 504990 | 28 | -92.7 | 504990 | 347 | -95.5 | 504990 | 45 | -99.4 | 504990 | 657 |
| MR_1774414512_914D58C2 | 504990 | 28 | -92.0 | 504990 | 347 | -97.5 | 504990 | 45 | -99.4 | 504990 | 657 |
| MR_1774414512_8E5813E9 | 504990 | 28 | -92.9 | 504990 | 347 | -96.8 | 504990 | 45 | -101.9 | 504990 | 657 |
| MR_1774414512_1C1EFE3F | 504990 | 28 | -93.1 | 504990 | 347 | -96.0 | 504990 | 45 | -99.4 | 504990 | 657 |
| MR_1774414512_754D3756 | 504990 | 28 | -90.8 | 504990 | 347 | -96.9 | 504990 | 45 | -100.0 | 504990 | 657 |
| MR_1774414512_BE962871 | 504990 | 28 | -93.0 | 504990 | 347 | -95.6 | 504990 | 45 | -99.4 | 504990 | 657 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1303: `472277e1-e4f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `472277e1-e4fa-4a0e-9d09-660d483499e6` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Decrease A3 Offset threshold for 3215959_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1303] topology](images/train_1303.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3234276_3 by 4 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234276_3
- `C3`: Decrease A3 Offset threshold for 3234276_3
- `C4`: Increase A3 Offset threshold for 3215959_4
- `C5`: Add neighbor relationship between 3214235_2 and 3234276_3
- `C6`: Decrease transmission power for 3215959_4
- `C7`: Press down the tilt angle  of 3234276_3 by 4 degrees
- `C8`: Increase A3 Offset threshold for 3234276_3
- `C9`: Lift the tilt angle of 3215959_4 by 6 degrees
- `C10`: Add neighbor relationship between 3215959_4 and 3234276_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234276_3
- `C12`: Adjust the azimuth of 3215959_4 by 22 degrees
- `C13`: Check test server and transmission issues
- `C14`: Press down the tilt angle of 3215959_4 by 6 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Increase transmission power for 3234276_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215959_4
- `C18`: Decrease transmission power for 3234276_3
- `C19`: Decrease A3 Offset threshold for 3215959_4 **← 정답**
- `C20`: Increase transmission power for 3215959_4
- `C21`: Adjust the azimuth of 3234276_3 by 50 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215959_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.689 | MS1 | 121.4656614873 | 31.1446275460 | 854 | 504990 | -75.88 | 12.77 | 390.54 | 0.17 | 2.40 | 1577 |
| 2024-09-20 22:21:32.576 | MS1 | 121.4656594130 | 31.1446188621 | 854 | 504990 | -78.04 | 16.45 | 376.05 | 0.12 | 2.68 | 1586 |
| 2024-09-20 22:21:33.523 | MS1 | 121.4656712342 | 31.1446370356 | 854 | 504990 | -82.32 | 14.66 | 592.47 | 0.07 | 2.73 | 1561 |
| 2024-09-20 22:21:34.481 | MS1 | 121.4656679276 | 31.1446186012 | 854 | 504990 | -85.19 | -3.84 | 39.37 | 0.14 | 1.00 | 1578 |
| 2024-09-20 22:21:35.669 | MS1 | 121.4656614116 | 31.1446210310 | 854 | 504990 | -85.92 | -3.92 | 36.87 | 0.01 | 1.12 | 1561 |
| 2024-09-20 22:21:36.899 | MS1 | 121.4656715409 | 31.1446180117 | 854 | 504990 | -85.55 | -2.61 | 41.94 | 0.12 | 1.21 | 1592 |
| 2024-09-20 22:21:37.126 | MS1 | 121.4656695889 | 31.1446319515 | 854 | 504990 | -90.96 | -0.24 | 55.13 | 0.08 | 1.26 | 1588 |
| 2024-09-20 22:21:38.817 | MS1 | 121.4656628369 | 31.1446298298 | 854 | 504990 | -83.36 | -2.06 | 44.71 | 0.11 | 1.40 | 1569 |
| 2024-09-20 22:21:39.928 | MS1 | 121.4656722182 | 31.1446210069 | 925 | 504990 | -79.63 | 13.36 | 227.70 | 0.08 | 1.32 | 1561 |
| 2024-09-20 22:21:40.238 | MS1 | 121.4656742317 | 31.1446344550 | 925 | 504990 | -81.61 | 13.01 | 542.02 | 0.02 | 2.10 | 1576 |
| 2024-09-20 22:21:41.613 | MS1 | 121.4656637588 | 31.1446294360 | 925 | 504990 | -75.18 | 12.42 | 325.09 | 0.17 | 2.52 | 1571 |
| 2024-09-20 22:21:42.331 | MS1 | 121.4656741240 | 31.1446320209 | 925 | 504990 | -81.22 | 16.12 | 389.75 | 0.12 | 2.18 | 1592 |

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
| 3214235 | 2 | 121.4701632757 | 31.1548267951 | 306 | 2 | 6 | 15.0 | TDD | 268 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3215959 | 4 | 121.4679744346 | 31.1540724131 | 170 | 4 | 5 | 38.2 | TDD | 854 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3234276 | 3 | 121.4713416979 | 31.1502255871 | 348 | 2 | 4 | 33.5 | TDD | 925 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3273387 | 1 | 121.4707920023 | 31.1519857704 | 1 | 15 | 10 | 39.0 | TDD | 602 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.995 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.017 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.146 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.146 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.802 | NREventA3 | measId:2;ServCellPCI:945;Se... |
| 2024-09-20 22:21:38.042 | NRHandoverAttempt | SourcePCI:945;SourceNR-ARFC... |
| 2024-09-20 22:21:38.077 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.089 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.235 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.235 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273387 | 1 | 18.3078 | 16.2602 | -114.7348 | 19.7514 | 83.3211 | 0.0197 | 0.0022 |
| 2024_09_20 22:00 | 3214235 | 2 | 11.0721 | 14.0091 | -115.9887 | 18.4629 | 112.8930 | 0.0189 | 0.0079 |
| 2024_09_20 22:00 | 3234276 | 3 | 10.7532 | 10.4576 | -115.0697 | 17.6293 | 89.6591 | 0.0016 | 0.0091 |
| 2024_09_20 22:00 | 3215959 | 4 | 8.1171 | 12.7103 | -116.0441 | 13.9007 | 120.7755 | 0.0129 | 0.1054 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416170_83D4D6D2 | 504990 | 925 | -80.9 | 504990 | 854 | -86.7 | 504990 | 268 | -80.9 | 504990 | 602 |
| MR_1774416170_6219F8CC | 504990 | 925 | -79.5 | 504990 | 854 | -86.0 | 504990 | 268 | -79.6 | 504990 | 602 |
| MR_1774416170_0C3F4DEC | 504990 | 925 | -80.8 | 504990 | 854 | -86.8 | 504990 | 268 | -80.8 | 504990 | 602 |
| MR_1774416170_3BBBF820 | 504990 | 854 | -86.4 | 504990 | 925 | -79.2 | 504990 | 268 | -80.3 | 504990 | 602 |
| MR_1774416170_97E77BB1 | 504990 | 854 | -85.4 | 504990 | 925 | -81.2 | 504990 | 268 | -80.8 | 504990 | 602 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1304: `e578de97-7ff...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e578de97-7ff1-4348-8736-07d88419ebd0` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Add neighbor relationship between 3252354_1 and 3271645_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1304] topology](images/train_1304.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3252354_1 by 50 degrees
- `C2`: Decrease transmission power for 3271645_2
- `C3`: Add neighbor relationship between 3278769_3 and 3271645_2
- `C4`: Press down the tilt angle  of 3271645_2 by 2 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252354_1
- `C6`: Lift the tilt angle  of 3271645_2 by 2 degrees
- `C7`: Increase transmission power for 3271645_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271645_2
- `C9`: Press down the tilt angle of 3252354_1 by 9 degrees
- `C10`: Lift the tilt angle of 3252354_1 by 9 degrees
- `C11`: Decrease A3 Offset threshold for 3271645_2
- `C12`: Decrease transmission power for 3252354_1
- `C13`: Check test server and transmission issues
- `C14`: Decrease A3 Offset threshold for 3252354_1
- `C15`: Increase A3 Offset threshold for 3271645_2
- `C16`: Increase transmission power for 3252354_1
- `C17`: Increase A3 Offset threshold for 3252354_1
- `C18`: Add neighbor relationship between 3252354_1 and 3271645_2 **← 정답**
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271645_2
- `C21`: Adjust the azimuth of 3271645_2 by 27 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252354_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.501 | MS1 | 121.4656634391 | 31.1446200462 | 960 | 504990 | -77.56 | 14.85 | 482.40 | 0.13 | 2.27 | 1594 |
| 2024-09-20 22:21:32.251 | MS1 | 121.4656708698 | 31.1446305779 | 960 | 504990 | -84.54 | 17.57 | 380.64 | 0.18 | 2.72 | 1567 |
| 2024-09-20 22:21:33.321 | MS1 | 121.4656606240 | 31.1446213822 | 960 | 504990 | -81.50 | 13.60 | 416.40 | 0.11 | 2.80 | 1567 |
| 2024-09-20 22:21:34.769 | MS1 | 121.4656595650 | 31.1446346569 | 960 | 504990 | -88.85 | -2.93 | 76.92 | 0.05 | 1.37 | 1588 |
| 2024-09-20 22:21:35.270 | MS1 | 121.4656702798 | 31.1446182144 | 960 | 504990 | -85.11 | -3.10 | 29.11 | 0.12 | 1.50 | 1595 |
| 2024-09-20 22:21:36.923 | MS1 | 121.4656636662 | 31.1446318507 | 960 | 504990 | -85.04 | -0.49 | 46.83 | 0.09 | 1.43 | 1569 |
| 2024-09-20 22:21:37.609 | MS1 | 121.4656630325 | 31.1446329191 | 960 | 504990 | -93.01 | -1.49 | 43.80 | 0.15 | 1.11 | 1575 |
| 2024-09-20 22:21:38.328 | MS1 | 121.4656621866 | 31.1446340457 | 960 | 504990 | -77.79 | 12.92 | 574.36 | 0.13 | 1.00 | 1578 |
| 2024-09-20 22:21:39.422 | MS1 | 121.4656583533 | 31.1446181504 | 960 | 504990 | -77.29 | 12.37 | 414.71 | 0.01 | 1.34 | 1569 |
| 2024-09-20 22:21:40.764 | MS1 | 121.4656581158 | 31.1446317784 | 960 | 504990 | -81.70 | 13.94 | 391.46 | 0.02 | 2.72 | 1590 |
| 2024-09-20 22:21:41.713 | MS1 | 121.4656718850 | 31.1446309341 | 960 | 504990 | -77.98 | 15.80 | 358.56 | 0.17 | 2.82 | 1562 |
| 2024-09-20 22:21:42.705 | MS1 | 121.4656751675 | 31.1446309176 | 960 | 504990 | -81.47 | 14.67 | 299.97 | 0.13 | 2.31 | 1563 |

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
| 3252354 | 1 | 121.4640273835 | 31.1489153195 | 39 | 6 | 9 | 25.4 | TDD | 960 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3265680 | 4 | 121.4749684246 | 31.1523724283 | 207 | 12 | 2 | 19.9 | TDD | 513 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3271645 | 2 | 121.4711940182 | 31.1516001600 | 241 | 0 | 4 | 40.6 | TDD | 329 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3278769 | 3 | 121.4740755671 | 31.1488447250 | 129 | 6 | 12 | 39.3 | TDD | 27 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.227 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.337 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.337 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.077 | NREventA3 | measId:2;ServCellPCI:668;Se... |
| 2024-09-20 22:21:36.077 | NREventA3 | measId:2;ServCellPCI:668;Se... |
| 2024-09-20 22:21:37.077 | NREventA3 | measId:2;ServCellPCI:668;Se... |
| 2024-09-20 22:21:39.577 | NRRRCReestablishAttempt | PCI:668 |
| 2024-09-20 22:21:39.597 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.610 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.739 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.739 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252354 | 1 | 5.0360 | 10.0984 | -117.4439 | 11.3821 | 88.3492 | 0.0011 | 0.1587 |
| 2024_09_20 22:00 | 3271645 | 2 | 18.7382 | 11.8652 | -115.3149 | 11.8626 | 177.7632 | 0.0122 | 0.0171 |
| 2024_09_20 22:00 | 3278769 | 3 | 14.9938 | 10.2252 | -116.2813 | 15.0655 | 151.6583 | 0.0077 | 0.0195 |
| 2024_09_20 22:00 | 3265680 | 4 | 14.6486 | 15.3011 | -114.5097 | 13.4455 | 81.5736 | 0.0043 | 0.0069 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415977_E97DC8F1 | 504990 | 329 | -84.1 | 504990 | 960 | -90.8 | 504990 | 27 | -88.1 | 504990 | 513 |
| MR_1774415977_8996FCC8 | 504990 | 329 | -82.6 | 504990 | 960 | -90.7 | 504990 | 27 | -89.0 | 504990 | 513 |
| MR_1774415977_84853939 | 504990 | 329 | -83.7 | 504990 | 960 | -90.8 | 504990 | 27 | -86.0 | 504990 | 513 |
| MR_1774415977_6B188454 | 504990 | 329 | -85.1 | 504990 | 960 | -87.3 | 504990 | 27 | -87.2 | 504990 | 513 |
| MR_1774415977_ACA166A5 | 504990 | 960 | -87.3 | 504990 | 329 | -86.0 | 504990 | 27 | -88.3 | 504990 | 513 |
| MR_1774415977_37EA929B | 504990 | 329 | -83.0 | 504990 | 960 | -87.9 | 504990 | 27 | -87.2 | 504990 | 513 |
| MR_1774415977_77AF077F | 504990 | 329 | -85.5 | 504990 | 960 | -87.0 | 504990 | 27 | -88.2 | 504990 | 513 |
| MR_1774415977_71D5DAD0 | 504990 | 960 | -90.2 | 504990 | 329 | -83.0 | 504990 | 27 | -88.6 | 504990 | 513 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1305: `bc7c8362-f83...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bc7c8362-f83d-43b7-8f88-d2d343944e0f` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1305] topology](images/train_1305.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3247109_1
- `C2`: Check test server and transmission issues
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247109_1
- `C4`: Press down the tilt angle  of 3247109_1 by 6 degrees
- `C5`: Increase transmission power for 3235510_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247109_1
- `C7`: Adjust the azimuth of 3235510_3 by 50 degrees
- `C8`: Decrease A3 Offset threshold for 3247109_1
- `C9`: Add neighbor relationship between 3235510_3 and 3247109_1
- `C10`: Press down the tilt angle of 3235510_3 by 10 degrees
- `C11`: Decrease transmission power for 3235510_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235510_3
- `C13`: Decrease transmission power for 3247109_1
- `C14`: Increase transmission power for 3247109_1
- `C15`: Add neighbor relationship between 3259588_2 and 3247109_1
- `C16`: Lift the tilt angle  of 3247109_1 by 6 degrees
- `C17`: Lift the tilt angle of 3235510_3 by 10 degrees
- `C18`: Decrease A3 Offset threshold for 3235510_3
- `C19`: Adjust the azimuth of 3247109_1 by 19 degrees
- `C20`: Increase A3 Offset threshold for 3235510_3
- `C21`: Insufficient data; more data is needed for judgment. **← 정답**
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235510_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.694 | MS1 | 121.4656580424 | 31.1446349080 | 974 | 504990 | -89.76 | 12.96 | 449.89 | 0.01 | 2.86 | 1582 |
| 2024-09-20 22:21:32.119 | MS1 | 121.4656726745 | 31.1446216677 | 974 | 504990 | -85.30 | 16.79 | 470.28 | 0.05 | 2.15 | 1591 |
| 2024-09-20 22:21:33.503 | MS1 | 121.4656699632 | 31.1446223243 | 974 | 504990 | -85.44 | 17.45 | 583.14 | 0.08 | 2.07 | 1589 |
| 2024-09-20 22:21:34.963 | MS1 | 121.4656723313 | 31.1446257347 | 974 | 504990 | -85.18 | 14.15 | 77.58 | 0.10 | 2.85 | 1579 |
| 2024-09-20 22:21:35.436 | MS1 | 121.4656617396 | 31.1446328947 | 974 | 504990 | -89.60 | 17.93 | 58.42 | 0.03 | 2.02 | 1577 |
| 2024-09-20 22:21:36.917 | MS1 | 121.4656612881 | 31.1446285033 | 974 | 504990 | -91.87 | 15.68 | 89.01 | 0.06 | 2.14 | 1580 |
| 2024-09-20 22:21:37.850 | MS1 | 121.4656702337 | 31.1446345693 | 974 | 504990 | -89.89 | 12.69 | 102.55 | 0.03 | 2.84 | 1562 |
| 2024-09-20 22:21:38.585 | MS1 | 121.4656746216 | 31.1446259963 | 974 | 504990 | -90.12 | 11.65 | 51.71 | 0.11 | 2.14 | 1574 |
| 2024-09-20 22:21:39.162 | MS1 | 121.4656635510 | 31.1446363433 | 974 | 504990 | -89.55 | 9.24 | 51.98 | 0.14 | 2.52 | 1582 |
| 2024-09-20 22:21:40.534 | MS1 | 121.4656670320 | 31.1446305444 | 974 | 504990 | -93.75 | 8.06 | 567.76 | 0.14 | 2.13 | 1586 |
| 2024-09-20 22:21:41.233 | MS1 | 121.4656763986 | 31.1446271037 | 974 | 504990 | -89.49 | 11.82 | 319.61 | 0.10 | 2.06 | 1572 |
| 2024-09-20 22:21:42.277 | MS1 | 121.4656744120 | 31.1446302933 | 974 | 504990 | -92.02 | 9.52 | 387.29 | 0.11 | 2.08 | 1564 |

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
| 3235510 | 3 | 121.4714429693 | 31.1481819795 | 354 | 7 | 1 | 43.4 | TDD | 974 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3247109 | 1 | 121.4703756251 | 31.1470899927 | 220 | 2 | 8 | 33.9 | TDD | 384 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3256398 | 4 | 121.4724832080 | 31.1486529775 | 189 | 11 | 11 | 18.4 | TDD | 370 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3259588 | 2 | 121.4682328725 | 31.1520255488 | 309 | 3 | 0 | 16.4 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.606 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.721 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.721 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.398 | NREventA3 | measId:2;ServCellPCI:304;Se... |
| 2024-09-20 22:21:38.638 | NRHandoverAttempt | SourcePCI:304;SourceNR-ARFC... |
| 2024-09-20 22:21:38.686 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.697 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.800 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.800 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3247109 | 1 | 90.0468 | 82.5634 | -116.1051 | 5.2268 | 99.8175 | 0.0154 | 0.0108 |
| 2024_09_19 22:00 | 3259588 | 2 | 91.4535 | 85.4133 | -114.6177 | 5.2970 | 83.7871 | 0.0119 | 0.0083 |
| 2024_09_19 22:00 | 3235510 | 3 | 75.5741 | 77.7374 | -115.9170 | 9.6620 | 194.6184 | 0.0130 | 0.0028 |
| 2024_09_19 22:00 | 3256398 | 4 | 88.2480 | 84.9051 | -116.8496 | 14.1736 | 175.3201 | 0.0053 | 0.0155 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417144_6FCDCF87 | 504990 | 974 | -83.3 | 504990 | 384 | -94.1 | 504990 | 866 | -94.4 | 504990 | 370 |
| MR_1774417144_70E803C4 | 504990 | 974 | -84.3 | 504990 | 384 | -93.0 | 504990 | 866 | -95.0 | 504990 | 370 |
| MR_1774417144_536E1736 | 504990 | 974 | -83.4 | 504990 | 384 | -92.4 | 504990 | 866 | -96.5 | 504990 | 370 |
| MR_1774417144_D81C4AC3 | 504990 | 974 | -83.8 | 504990 | 384 | -91.7 | 504990 | 866 | -96.6 | 504990 | 370 |
| MR_1774417144_A7632EEB | 504990 | 974 | -83.8 | 504990 | 384 | -94.6 | 504990 | 866 | -95.4 | 504990 | 370 |
| MR_1774417144_486FD1F6 | 504990 | 974 | -84.8 | 504990 | 384 | -90.9 | 504990 | 866 | -94.5 | 504990 | 370 |
| MR_1774417144_5587D621 | 504990 | 974 | -87.0 | 504990 | 384 | -91.5 | 504990 | 866 | -96.5 | 504990 | 370 |
| MR_1774417144_238561D2 | 504990 | 974 | -85.6 | 504990 | 384 | -91.0 | 504990 | 866 | -97.0 | 504990 | 370 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1306: `1ffcdf1e-15c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1ffcdf1e-15c2-4cba-8c3e-20401b6d1cfb` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1306] topology](images/train_1306.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3266568_2 by 10 degrees
- `C2`: Add neighbor relationship between 3266568_2 and 3262588_1
- `C3`: Decrease A3 Offset threshold for 3266568_2
- `C4`: Decrease A3 Offset threshold for 3262588_1
- `C5`: Check test server and transmission issues **← 정답**
- `C6`: Increase A3 Offset threshold for 3262588_1
- `C7`: Decrease transmission power for 3262588_1
- `C8`: Increase A3 Offset threshold for 3266568_2
- `C9`: Add neighbor relationship between 3249074_3 and 3262588_1
- `C10`: Adjust the azimuth of 3266568_2 by 50 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Adjust the azimuth of 3262588_1 by 50 degrees
- `C13`: Lift the tilt angle of 3266568_2 by 10 degrees
- `C14`: Increase transmission power for 3266568_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262588_1
- `C16`: Decrease transmission power for 3266568_2
- `C17`: Lift the tilt angle  of 3262588_1 by 10 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266568_2
- `C19`: Press down the tilt angle  of 3262588_1 by 10 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262588_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266568_2
- `C22`: Increase transmission power for 3262588_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.979 | MS1 | 121.4656623940 | 31.1446251743 | 633 | 504990 | -87.17 | 14.16 | 562.04 | 0.12 | 2.21 | 1565 |
| 2024-09-20 22:21:32.895 | MS1 | 121.4656744372 | 31.1446318327 | 633 | 504990 | -91.72 | 12.15 | 402.47 | 0.02 | 2.51 | 1578 |
| 2024-09-20 22:21:33.996 | MS1 | 121.4656723764 | 31.1446201614 | 633 | 504990 | -88.93 | 15.85 | 594.75 | 0.07 | 2.61 | 1562 |
| 2024-09-20 22:21:34.815 | MS1 | 121.4656694169 | 31.1446263224 | 633 | 504990 | -85.76 | 14.41 | 54.59 | 0.07 | 2.01 | 378 |
| 2024-09-20 22:21:35.516 | MS1 | 121.4656647767 | 31.1446291271 | 633 | 504990 | -86.61 | 12.66 | 86.87 | 0.17 | 2.63 | 350 |
| 2024-09-20 22:21:36.204 | MS1 | 121.4656655786 | 31.1446240184 | 633 | 504990 | -85.31 | 16.98 | 64.64 | 0.06 | 2.89 | 438 |
| 2024-09-20 22:21:37.530 | MS1 | 121.4656585912 | 31.1446336415 | 633 | 504990 | -91.32 | 12.52 | 62.30 | 0.18 | 2.99 | 345 |
| 2024-09-20 22:21:38.902 | MS1 | 121.4656752764 | 31.1446330670 | 633 | 504990 | -92.02 | 10.70 | 60.48 | 0.01 | 2.45 | 396 |
| 2024-09-20 22:21:39.998 | MS1 | 121.4656631476 | 31.1446244406 | 633 | 504990 | -91.89 | 9.17 | 77.68 | 0.18 | 2.89 | 326 |
| 2024-09-20 22:21:40.439 | MS1 | 121.4656688473 | 31.1446267129 | 633 | 504990 | -92.90 | 8.75 | 369.58 | 0.03 | 2.80 | 1569 |
| 2024-09-20 22:21:41.928 | MS1 | 121.4656606550 | 31.1446356864 | 633 | 504990 | -90.51 | 11.44 | 571.01 | 0.07 | 2.67 | 1596 |
| 2024-09-20 22:21:42.148 | MS1 | 121.4656680092 | 31.1446346607 | 633 | 504990 | -93.75 | 12.71 | 331.05 | 0.07 | 2.01 | 1563 |

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
| 3236299 | 4 | 121.4667834961 | 31.1464778790 | 182 | 7 | 8 | 16.5 | TDD | 264 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3249074 | 3 | 121.4717460217 | 31.1513836077 | 304 | 2 | 8 | 17.7 | TDD | 512 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3262588 | 1 | 121.4722005648 | 31.1513479375 | 24 | 13 | 4 | 22.8 | TDD | 880 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3266568 | 2 | 121.4673467771 | 31.1447199620 | 119 | 13 | 0 | 46.3 | TDD | 633 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.515 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.634 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.634 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.383 | NREventA3 | measId:2;ServCellPCI:629;Se... |
| 2024-09-20 22:21:38.623 | NRHandoverAttempt | SourcePCI:629;SourceNR-ARFC... |
| 2024-09-20 22:21:38.659 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.672 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.784 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.784 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262588 | 1 | 12.1440 | 9.2612 | -117.5279 | 7.4253 | 137.3715 | 0.0021 | 0.0122 |
| 2024_09_20 22:00 | 3266568 | 2 | 19.7456 | 11.3904 | -116.7812 | 9.6514 | 96.0716 | 0.0065 | 0.0139 |
| 2024_09_20 22:00 | 3249074 | 3 | 18.2111 | 5.9185 | -115.3084 | 13.6148 | 167.2138 | 0.0075 | 0.0037 |
| 2024_09_20 22:00 | 3236299 | 4 | 19.7701 | 19.9047 | -116.5861 | 16.8182 | 159.1677 | 0.0177 | 0.0008 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416677_F65977F6 | 504990 | 633 | -86.0 | 504990 | 880 | -94.8 | 504990 | 512 | -93.9 | 504990 | 264 |
| MR_1774416677_EAE2A548 | 504990 | 633 | -85.9 | 504990 | 880 | -93.2 | 504990 | 512 | -93.8 | 504990 | 264 |
| MR_1774416677_A10FB5D0 | 504990 | 633 | -84.4 | 504990 | 880 | -97.0 | 504990 | 512 | -96.1 | 504990 | 264 |
| MR_1774416677_006A15EB | 504990 | 633 | -87.5 | 504990 | 880 | -96.5 | 504990 | 512 | -95.1 | 504990 | 264 |
| MR_1774416677_0157A94C | 504990 | 633 | -87.4 | 504990 | 880 | -95.8 | 504990 | 512 | -94.2 | 504990 | 264 |
| MR_1774416677_E0A17885 | 504990 | 633 | -87.6 | 504990 | 880 | -95.5 | 504990 | 512 | -93.7 | 504990 | 264 |
| MR_1774416677_29595DBA | 504990 | 633 | -85.5 | 504990 | 880 | -93.9 | 504990 | 512 | -95.1 | 504990 | 264 |
| MR_1774416677_2AF7D6A7 | 504990 | 633 | -87.7 | 504990 | 880 | -95.7 | 504990 | 512 | -94.0 | 504990 | 264 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1307: `0ea9a70e-f33...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0ea9a70e-f330-4ca4-bde2-52fff6a26cf8` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1307] topology](images/train_1307.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217804_1
- `C2`: Add neighbor relationship between 3217804_1 and 3215519_2
- `C3`: Insufficient data; more data is needed for judgment. **← 정답**
- `C4`: Increase transmission power for 3215519_2
- `C5`: Decrease transmission power for 3215519_2
- `C6`: Press down the tilt angle of 3217804_1 by 10 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215519_2
- `C8`: Decrease A3 Offset threshold for 3215519_2
- `C9`: Decrease A3 Offset threshold for 3217804_1
- `C10`: Decrease transmission power for 3217804_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215519_2
- `C12`: Lift the tilt angle of 3217804_1 by 10 degrees
- `C13`: Press down the tilt angle  of 3215519_2 by 10 degrees
- `C14`: Check test server and transmission issues
- `C15`: Lift the tilt angle  of 3215519_2 by 10 degrees
- `C16`: Increase transmission power for 3217804_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217804_1
- `C18`: Increase A3 Offset threshold for 3215519_2
- `C19`: Adjust the azimuth of 3215519_2 by 10 degrees
- `C20`: Adjust the azimuth of 3217804_1 by 50 degrees
- `C21`: Add neighbor relationship between 3241203_3 and 3215519_2
- `C22`: Increase A3 Offset threshold for 3217804_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.689 | MS1 | 121.4656681007 | 31.1446275384 | 448 | 504990 | -85.87 | 12.17 | 515.74 | 0.17 | 2.39 | 1574 |
| 2024-09-20 22:21:32.497 | MS1 | 121.4656699850 | 31.1446251390 | 448 | 504990 | -91.35 | 16.52 | 389.70 | 0.13 | 2.08 | 1563 |
| 2024-09-20 22:21:33.976 | MS1 | 121.4656626353 | 31.1446332107 | 448 | 504990 | -86.32 | 15.75 | 486.66 | 0.15 | 2.71 | 1583 |
| 2024-09-20 22:21:34.719 | MS1 | 121.4656645479 | 31.1446180039 | 448 | 504990 | -86.45 | 15.67 | 75.91 | 0.02 | 2.23 | 1579 |
| 2024-09-20 22:21:35.607 | MS1 | 121.4656731407 | 31.1446215462 | 448 | 504990 | -86.02 | 13.28 | 70.41 | 0.14 | 2.79 | 1585 |
| 2024-09-20 22:21:36.322 | MS1 | 121.4656662861 | 31.1446242906 | 448 | 504990 | -89.09 | 13.26 | 81.24 | 0.08 | 2.12 | 1599 |
| 2024-09-20 22:21:37.816 | MS1 | 121.4656591234 | 31.1446284310 | 448 | 504990 | -91.55 | 8.22 | 86.90 | 0.10 | 2.69 | 1594 |
| 2024-09-20 22:21:38.608 | MS1 | 121.4656730320 | 31.1446260812 | 448 | 504990 | -93.84 | 8.97 | 66.77 | 0.01 | 2.81 | 1562 |
| 2024-09-20 22:21:39.779 | MS1 | 121.4656610069 | 31.1446271075 | 448 | 504990 | -92.77 | 12.97 | 76.15 | 0.15 | 2.38 | 1585 |
| 2024-09-20 22:21:40.527 | MS1 | 121.4656779620 | 31.1446308141 | 448 | 504990 | -90.65 | 8.54 | 440.19 | 0.04 | 2.44 | 1599 |
| 2024-09-20 22:21:41.349 | MS1 | 121.4656675031 | 31.1446350515 | 448 | 504990 | -92.44 | 10.25 | 391.38 | 0.05 | 2.67 | 1597 |
| 2024-09-20 22:21:42.797 | MS1 | 121.4656721491 | 31.1446238229 | 448 | 504990 | -89.50 | 12.40 | 454.60 | 0.01 | 2.42 | 1563 |

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
| 3215519 | 2 | 121.4743055447 | 31.1549973903 | 225 | 15 | 5 | 42.4 | TDD | 600 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3217804 | 1 | 121.4650103142 | 31.1443930963 | 10 | 1 | 7 | 30.6 | TDD | 448 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3241203 | 3 | 121.4640618231 | 31.1448107826 | 57 | 10 | 4 | 46.0 | TDD | 470 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3279427 | 4 | 121.4758060688 | 31.1477339814 | 178 | 15 | 4 | 15.2 | TDD | 799 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.227 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.250 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.376 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.376 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.057 | NREventA3 | measId:2;ServCellPCI:786;Se... |
| 2024-09-20 22:21:38.297 | NRHandoverAttempt | SourcePCI:786;SourceNR-ARFC... |
| 2024-09-20 22:21:38.328 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.343 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.485 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.485 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3217804 | 1 | 93.0336 | 88.1479 | -114.0531 | 10.8839 | 100.7169 | 0.0123 | 0.0059 |
| 2024_09_19 22:00 | 3215519 | 2 | 91.0914 | 88.4686 | -114.5317 | 12.9983 | 151.0128 | 0.0168 | 0.0184 |
| 2024_09_19 22:00 | 3241203 | 3 | 85.8728 | 94.2440 | -115.8100 | 16.4415 | 189.9905 | 0.0033 | 0.0129 |
| 2024_09_19 22:00 | 3279427 | 4 | 77.6004 | 88.0758 | -114.9808 | 14.2727 | 89.2297 | 0.0012 | 0.0115 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413806_BA5418E0 | 504990 | 448 | -85.3 | 504990 | 600 | -91.1 | 504990 | 470 | -94.9 | 504990 | 799 |
| MR_1774413806_33EE7BB6 | 504990 | 448 | -87.2 | 504990 | 600 | -91.6 | 504990 | 470 | -95.1 | 504990 | 799 |
| MR_1774413806_5370FF75 | 504990 | 448 | -86.9 | 504990 | 600 | -89.0 | 504990 | 470 | -95.7 | 504990 | 799 |
| MR_1774413806_93D6D00F | 504990 | 448 | -88.4 | 504990 | 600 | -88.4 | 504990 | 470 | -95.2 | 504990 | 799 |
| MR_1774413806_E0D2717F | 504990 | 448 | -87.4 | 504990 | 600 | -89.0 | 504990 | 470 | -96.3 | 504990 | 799 |
| MR_1774413806_56BF989E | 504990 | 448 | -86.6 | 504990 | 600 | -90.8 | 504990 | 470 | -95.9 | 504990 | 799 |
| MR_1774413806_02ED4B0F | 504990 | 448 | -86.2 | 504990 | 600 | -88.7 | 504990 | 470 | -94.8 | 504990 | 799 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1308: `ef748e40-b24...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ef748e40-b248-49d4-9170-1dac96445b8d` |
| Tag | **multiple-answer** |
| 정답 | **C19|C22** |
| C19 의미 | Increase transmission power for 3233716_2 |
| C22 의미 | Adjust the azimuth of 3233716_2 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1308] topology](images/train_1308.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Check test server and transmission issues
- `C3`: Decrease transmission power for 3242848_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233716_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242848_1
- `C6`: Decrease transmission power for 3233716_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233716_2
- `C8`: Increase A3 Offset threshold for 3242848_1
- `C9`: Add neighbor relationship between 3211787_4 and 3242848_1
- `C10`: Increase A3 Offset threshold for 3233716_2
- `C11`: Press down the tilt angle  of 3242848_1 by 3 degrees
- `C12`: Add neighbor relationship between 3233716_2 and 3242848_1
- `C13`: Increase transmission power for 3242848_1
- `C14`: Decrease A3 Offset threshold for 3242848_1
- `C15`: Press down the tilt angle of 3233716_2 by 4 degrees
- `C16`: Adjust the azimuth of 3242848_1 by 44 degrees
- `C17`: Decrease A3 Offset threshold for 3233716_2
- `C18`: Lift the tilt angle  of 3242848_1 by 3 degrees
- `C19`: Increase transmission power for 3233716_2 **← 정답**
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242848_1
- `C21`: Lift the tilt angle of 3233716_2 by 4 degrees
- `C22`: Adjust the azimuth of 3233716_2 by 50 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.726 | MS1 | 121.4656699698 | 31.1446195857 | 562 | 504990 | -88.28 | 14.25 | 485.86 | 0.07 | 2.63 | 1590 |
| 2024-09-20 22:21:32.991 | MS1 | 121.4656664170 | 31.1446222373 | 562 | 504990 | -90.24 | 12.74 | 538.83 | 0.12 | 2.52 | 1587 |
| 2024-09-20 22:21:33.954 | MS1 | 121.4656758030 | 31.1446318378 | 562 | 504990 | -92.20 | 17.80 | 434.09 | 0.20 | 2.85 | 1572 |
| 2024-09-20 22:21:34.130 | MS1 | 121.4656617066 | 31.1446279910 | 562 | 504990 | -106.74 | -1.96 | 34.08 | 0.07 | 1.12 | 1581 |
| 2024-09-20 22:21:35.583 | MS1 | 121.4656624175 | 31.1446363269 | 562 | 504990 | -106.48 | 0.42 | 70.05 | 0.04 | 1.49 | 1595 |
| 2024-09-20 22:21:36.655 | MS1 | 121.4656623097 | 31.1446336557 | 562 | 504990 | -109.36 | -1.33 | 59.65 | 0.11 | 1.27 | 1579 |
| 2024-09-20 22:21:37.972 | MS1 | 121.4656749575 | 31.1446345673 | 562 | 504990 | -109.52 | -1.91 | 52.67 | 0.15 | 1.31 | 1587 |
| 2024-09-20 22:21:38.236 | MS1 | 121.4656778259 | 31.1446182313 | 562 | 504990 | -108.82 | -0.91 | 50.57 | 0.15 | 1.16 | 1562 |
| 2024-09-20 22:21:39.951 | MS1 | 121.4656653862 | 31.1446185108 | 562 | 504990 | -104.96 | -0.75 | 29.61 | 0.12 | 1.36 | 1589 |
| 2024-09-20 22:21:40.287 | MS1 | 121.4656642873 | 31.1446318713 | 562 | 504990 | -88.76 | 13.90 | 315.83 | 0.06 | 2.35 | 1565 |
| 2024-09-20 22:21:41.629 | MS1 | 121.4656644646 | 31.1446243137 | 562 | 504990 | -93.49 | 12.55 | 499.64 | 0.06 | 2.39 | 1581 |
| 2024-09-20 22:21:42.754 | MS1 | 121.4656706791 | 31.1446360389 | 562 | 504990 | -89.95 | 17.69 | 600.29 | 0.04 | 2.73 | 1560 |

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
| 3211787 | 4 | 121.4693462012 | 31.1521099702 | 310 | 13 | 12 | 43.8 | TDD | 318 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3232012 | 3 | 121.4656523121 | 31.1475111854 | 154 | 4 | 3 | 17.1 | TDD | 1004 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3233716 | 2 | 121.4731756525 | 31.1550443606 | 285 | 3 | 6 | 21.0 | TDD | 562 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3242848 | 1 | 121.4690711191 | 31.1487107755 | 171 | 0 | 8 | 25.5 | TDD | 120 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.977 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.992 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.096 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.096 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.313 | NREventA2 | measId:1;ServCellPCI:970;Se... |
| 2024-09-20 22:21:34.461 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242848 | 1 | 7.5436 | 18.1693 | -115.5300 | 7.6796 | 139.4107 | 0.0196 | 0.0025 |
| 2024_09_20 22:00 | 3233716 | 2 | 12.5307 | 13.8521 | -116.3266 | 19.5328 | 155.3947 | 0.1649 | 0.0074 |
| 2024_09_20 22:00 | 3232012 | 3 | 19.7336 | 18.1456 | -117.1103 | 10.4111 | 165.8264 | 0.0081 | 0.0089 |
| 2024_09_20 22:00 | 3211787 | 4 | 9.2450 | 11.7533 | -116.3265 | 13.3826 | 134.9246 | 0.0034 | 0.0185 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414407_5C5C6B9A | 504990 | 562 | -107.8 | 504990 | 120 | -110.4 | 504990 | 318 | -116.6 | 504990 | 1004 |
| MR_1774414407_61E3CC17 | 504990 | 562 | -106.1 | 504990 | 120 | -109.2 | 504990 | 318 | -119.6 | 504990 | 1004 |
| MR_1774414407_86418546 | 504990 | 562 | -106.7 | 504990 | 120 | -111.8 | 504990 | 318 | -117.3 | 504990 | 1004 |
| MR_1774414407_1B511941 | 504990 | 562 | -105.2 | 504990 | 120 | -111.9 | 504990 | 318 | -116.6 | 504990 | 1004 |
| MR_1774414407_008F0C4A | 504990 | 562 | -108.5 | 504990 | 120 | -111.9 | 504990 | 318 | -117.3 | 504990 | 1004 |
| MR_1774414407_92D5B706 | 504990 | 562 | -108.5 | 504990 | 120 | -112.5 | 504990 | 318 | -119.9 | 504990 | 1004 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1309: `377a0d30-18b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `377a0d30-18b9-487a-bc14-56b8b8aa6ba0` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1309] topology](images/train_1309.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222406_2
- `C2`: Increase A3 Offset threshold for 3222406_2
- `C3`: Add neighbor relationship between 3277521_4 and 3222406_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222406_2
- `C5`: Decrease A3 Offset threshold for 3264011_1
- `C6`: Decrease A3 Offset threshold for 3222406_2
- `C7`: Lift the tilt angle  of 3222406_2 by 10 degrees
- `C8`: Increase A3 Offset threshold for 3264011_1
- `C9`: Adjust the azimuth of 3264011_1 by 50 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Press down the tilt angle  of 3222406_2 by 10 degrees
- `C12`: Increase transmission power for 3222406_2
- `C13`: Press down the tilt angle of 3264011_1 by 8 degrees
- `C14`: Add neighbor relationship between 3264011_1 and 3222406_2
- `C15`: Lift the tilt angle of 3264011_1 by 8 degrees
- `C16`: Decrease transmission power for 3222406_2
- `C17`: Adjust the azimuth of 3222406_2 by 50 degrees
- `C18`: Check test server and transmission issues **← 정답**
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264011_1
- `C20`: Increase transmission power for 3264011_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264011_1
- `C22`: Decrease transmission power for 3264011_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.720 | MS1 | 121.4656706411 | 31.1446246487 | 776 | 504990 | -88.85 | 14.73 | 365.65 | 0.18 | 2.52 | 1566 |
| 2024-09-20 22:21:32.678 | MS1 | 121.4656598971 | 31.1446268687 | 776 | 504990 | -90.34 | 17.06 | 312.69 | 0.13 | 2.75 | 1565 |
| 2024-09-20 22:21:33.987 | MS1 | 121.4656627598 | 31.1446295250 | 776 | 504990 | -86.87 | 13.44 | 413.77 | 0.17 | 2.17 | 1598 |
| 2024-09-20 22:21:34.948 | MS1 | 121.4656758749 | 31.1446257560 | 776 | 504990 | -90.34 | 15.90 | 82.67 | 0.19 | 2.84 | 395 |
| 2024-09-20 22:21:35.738 | MS1 | 121.4656658448 | 31.1446183532 | 776 | 504990 | -91.33 | 14.03 | 95.50 | 0.03 | 2.22 | 455 |
| 2024-09-20 22:21:36.223 | MS1 | 121.4656684359 | 31.1446294929 | 776 | 504990 | -85.76 | 13.82 | 59.65 | 0.11 | 2.79 | 356 |
| 2024-09-20 22:21:37.644 | MS1 | 121.4656671063 | 31.1446285779 | 776 | 504990 | -91.86 | 7.30 | 52.87 | 0.09 | 2.76 | 333 |
| 2024-09-20 22:21:38.753 | MS1 | 121.4656762372 | 31.1446188254 | 776 | 504990 | -92.35 | 11.13 | 91.51 | 0.10 | 2.94 | 451 |
| 2024-09-20 22:21:39.444 | MS1 | 121.4656585081 | 31.1446236650 | 776 | 504990 | -90.84 | 9.47 | 83.62 | 0.19 | 2.17 | 393 |
| 2024-09-20 22:21:40.625 | MS1 | 121.4656713714 | 31.1446185128 | 776 | 504990 | -90.44 | 8.41 | 489.87 | 0.14 | 2.35 | 1578 |
| 2024-09-20 22:21:41.619 | MS1 | 121.4656759548 | 31.1446209061 | 776 | 504990 | -93.26 | 11.91 | 574.49 | 0.01 | 2.45 | 1568 |
| 2024-09-20 22:21:42.840 | MS1 | 121.4656617914 | 31.1446324957 | 776 | 504990 | -93.52 | 8.29 | 369.19 | 0.06 | 2.77 | 1599 |

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
| 3222406 | 2 | 121.4685483201 | 31.1545216162 | 350 | 14 | 6 | 47.6 | TDD | 48 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3247970 | 3 | 121.4722264967 | 31.1506039050 | 272 | 2 | 6 | 31.8 | TDD | 836 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3264011 | 1 | 121.4754831519 | 31.1544519473 | 298 | 7 | 12 | 24.3 | TDD | 776 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3277521 | 4 | 121.4690544423 | 31.1473398803 | 316 | 7 | 4 | 44.1 | TDD | 207 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.398 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.418 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.520 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.520 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.289 | NREventA3 | measId:2;ServCellPCI:86;Ser... |
| 2024-09-20 22:21:38.529 | NRHandoverAttempt | SourcePCI:86;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.576 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.586 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.705 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.705 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264011 | 1 | 11.0760 | 16.5145 | -114.2752 | 18.8996 | 101.9292 | 0.0140 | 0.0054 |
| 2024_09_20 22:00 | 3222406 | 2 | 9.0824 | 7.9881 | -116.3250 | 12.8670 | 176.2645 | 0.0069 | 0.0051 |
| 2024_09_20 22:00 | 3247970 | 3 | 12.6054 | 16.6633 | -117.8599 | 6.7791 | 184.6762 | 0.0105 | 0.0009 |
| 2024_09_20 22:00 | 3277521 | 4 | 14.8430 | 13.5873 | -117.4273 | 12.5547 | 110.3701 | 0.0195 | 0.0041 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414430_5CF87B83 | 504990 | 776 | -91.7 | 504990 | 48 | -99.4 | 504990 | 207 | -99.8 | 504990 | 836 |
| MR_1774414430_00003A91 | 504990 | 776 | -92.3 | 504990 | 48 | -99.3 | 504990 | 207 | -101.1 | 504990 | 836 |
| MR_1774414430_3C3BB090 | 504990 | 776 | -88.9 | 504990 | 48 | -97.2 | 504990 | 207 | -102.6 | 504990 | 836 |
| MR_1774414430_7A5C3FD8 | 504990 | 776 | -90.6 | 504990 | 48 | -98.5 | 504990 | 207 | -100.0 | 504990 | 836 |
| MR_1774414430_8A34452C | 504990 | 776 | -89.9 | 504990 | 48 | -98.1 | 504990 | 207 | -100.6 | 504990 | 836 |

> *... 2개 열 생략 (전체 14열)*

---
