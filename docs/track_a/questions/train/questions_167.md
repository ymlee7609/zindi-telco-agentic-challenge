# Track A 문제 분석 — train[1660]~train[1669]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1660] ~ train[1669] (10개)

## 목차

1. [문제 1660: `e853d2c9-b16...`](#1660) — single-answer, 정답: C22
2. [문제 1661: `b22b5235-02a...`](#1661) — single-answer, 정답: C13
3. [문제 1662: `3e2ac3e3-bed...`](#1662) — multiple-answer, 정답: C3|C18
4. [문제 1663: `41cbed7e-f87...`](#1663) — multiple-answer, 정답: C5|C14
5. [문제 1664: `2d9658b0-0c4...`](#1664) — multiple-answer, 정답: C5|C6
6. [문제 1665: `37b08ea1-958...`](#1665) — single-answer, 정답: C18
7. [문제 1666: `796d5c24-c51...`](#1666) — single-answer, 정답: C4
8. [문제 1667: `fabbe292-29e...`](#1667) — single-answer, 정답: C3
9. [문제 1668: `95d86c05-b35...`](#1668) — single-answer, 정답: C20
10. [문제 1669: `9ab45ed2-be7...`](#1669) — single-answer, 정답: C19

---

### 문제 1660: `e853d2c9-b16...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e853d2c9-b164-42fd-8b94-49e9402781d5` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3256015_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1660] topology](images/train_1660.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3256015_1
- `C2`: Press down the tilt angle of 3256015_1 by 3 degrees
- `C3`: Adjust the azimuth of 3256015_1 by 34 degrees
- `C4`: Increase transmission power for 3237352_3
- `C5`: Press down the tilt angle  of 3237352_3 by 10 degrees
- `C6`: Decrease A3 Offset threshold for 3237352_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256015_1
- `C8`: Add neighbor relationship between 3271523_4 and 3237352_3
- `C9`: Adjust the azimuth of 3237352_3 by 50 degrees
- `C10`: Decrease transmission power for 3237352_3
- `C11`: Lift the tilt angle  of 3237352_3 by 10 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237352_3
- `C13`: Increase A3 Offset threshold for 3237352_3
- `C14`: Decrease transmission power for 3256015_1
- `C15`: Increase A3 Offset threshold for 3256015_1
- `C16`: Check test server and transmission issues
- `C17`: Add neighbor relationship between 3256015_1 and 3237352_3
- `C18`: Lift the tilt angle of 3256015_1 by 3 degrees
- `C19`: Increase transmission power for 3256015_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237352_3
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256015_1 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.707 | MS1 | 121.4656682697 | 31.1446354576 | 74 | 504990 | -91.78 | 14.23 | 465.77 | 0.10 | 2.38 | 1595 |
| 2024-09-20 22:21:32.122 | MS1 | 121.4656756259 | 31.1446306939 | 74 | 504990 | -88.55 | 13.45 | 346.10 | 0.14 | 2.31 | 1579 |
| 2024-09-20 22:21:33.769 | MS1 | 121.4656727429 | 31.1446334275 | 74 | 504990 | -90.38 | 14.74 | 508.09 | 0.14 | 2.50 | 1587 |
| 2024-09-20 22:21:34.777 | MS1 | 121.4656618882 | 31.1446281699 | 74 | 504990 | -87.52 | 14.91 | 84.17 | 0.64 | 2.22 | 663 |
| 2024-09-20 22:21:35.425 | MS1 | 121.4656701993 | 31.1446220710 | 74 | 504990 | -86.78 | 13.29 | 57.55 | 0.55 | 2.26 | 552 |
| 2024-09-20 22:21:36.990 | MS1 | 121.4656662900 | 31.1446347001 | 74 | 504990 | -86.96 | 16.97 | 89.90 | 0.58 | 2.51 | 556 |
| 2024-09-20 22:21:37.713 | MS1 | 121.4656686967 | 31.1446280837 | 74 | 504990 | -91.33 | 7.88 | 83.77 | 0.65 | 2.93 | 541 |
| 2024-09-20 22:21:38.428 | MS1 | 121.4656743391 | 31.1446339148 | 74 | 504990 | -91.17 | 9.24 | 60.42 | 0.55 | 2.81 | 547 |
| 2024-09-20 22:21:39.989 | MS1 | 121.4656722669 | 31.1446314469 | 74 | 504990 | -91.74 | 12.31 | 63.33 | 0.57 | 2.14 | 700 |
| 2024-09-20 22:21:40.610 | MS1 | 121.4656779610 | 31.1446294718 | 74 | 504990 | -90.50 | 9.36 | 338.27 | 0.12 | 2.60 | 1572 |
| 2024-09-20 22:21:41.268 | MS1 | 121.4656593158 | 31.1446358403 | 74 | 504990 | -90.40 | 7.61 | 494.25 | 0.11 | 2.63 | 1594 |
| 2024-09-20 22:21:42.171 | MS1 | 121.4656739034 | 31.1446273209 | 74 | 504990 | -92.68 | 12.18 | 537.62 | 0.15 | 2.24 | 1565 |

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
| 3225269 | 2 | 121.4724247182 | 31.1557685240 | 154 | 10 | 6 | 23.9 | TDD | 996 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3237352 | 3 | 121.4745338794 | 31.1514614277 | 82 | 14 | 9 | 31.1 | TDD | 525 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3256015 | 1 | 121.4728683693 | 31.1508240507 | 259 | 1 | 11 | 29.0 | TDD | 74 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3271523 | 4 | 121.4664416375 | 31.1540128708 | 95 | 8 | 0 | 30.2 | TDD | 410 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.099 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.120 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.262 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.262 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.964 | NREventA3 | measId:2;ServCellPCI:351;Se... |
| 2024-09-20 22:21:38.204 | NRHandoverAttempt | SourcePCI:351;SourceNR-ARFC... |
| 2024-09-20 22:21:38.242 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.254 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.380 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.380 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256015 | 1 | 17.9449 | 13.3862 | -117.2553 | 17.0711 | 190.4171 | 0.0147 | 0.0195 |
| 2024_09_20 22:00 | 3225269 | 2 | 6.2990 | 14.2869 | -115.0443 | 19.0976 | 158.6853 | 0.0104 | 0.0127 |
| 2024_09_20 22:00 | 3237352 | 3 | 10.9139 | 11.1538 | -116.6213 | 7.4038 | 157.6379 | 0.0168 | 0.0122 |
| 2024_09_20 22:00 | 3271523 | 4 | 19.5766 | 6.7161 | -115.9054 | 15.9899 | 97.1615 | 0.0162 | 0.0094 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413578_34FCB855 | 504990 | 74 | -86.1 | 504990 | 525 | -88.6 | 504990 | 410 | -101.4 | 504990 | 996 |
| MR_1774413578_B35D07E7 | 504990 | 74 | -89.5 | 504990 | 525 | -88.3 | 504990 | 410 | -101.7 | 504990 | 996 |
| MR_1774413578_0CF662BC | 504990 | 74 | -87.5 | 504990 | 525 | -91.3 | 504990 | 410 | -99.2 | 504990 | 996 |
| MR_1774413578_F3CBEE62 | 504990 | 74 | -88.1 | 504990 | 525 | -89.7 | 504990 | 410 | -99.9 | 504990 | 996 |
| MR_1774413578_61A8013A | 504990 | 74 | -88.0 | 504990 | 525 | -88.3 | 504990 | 410 | -99.6 | 504990 | 996 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1661: `b22b5235-02a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b22b5235-02a1-44a8-914f-554059a5166a` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Add neighbor relationship between 3235350_1 and 3243946_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1661] topology](images/train_1661.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3235350_1
- `C2`: Decrease transmission power for 3235350_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243946_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235350_1
- `C5`: Add neighbor relationship between 3230798_3 and 3243946_2
- `C6`: Check test server and transmission issues
- `C7`: Press down the tilt angle of 3235350_1 by 7 degrees
- `C8`: Adjust the azimuth of 3235350_1 by 16 degrees
- `C9`: Decrease A3 Offset threshold for 3243946_2
- `C10`: Lift the tilt angle of 3235350_1 by 7 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease transmission power for 3243946_2
- `C13`: Add neighbor relationship between 3235350_1 and 3243946_2 **← 정답**
- `C14`: Lift the tilt angle  of 3243946_2 by 4 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243946_2
- `C16`: Increase transmission power for 3235350_1
- `C17`: Press down the tilt angle  of 3243946_2 by 4 degrees
- `C18`: Increase A3 Offset threshold for 3243946_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235350_1
- `C20`: Adjust the azimuth of 3243946_2 by 16 degrees
- `C21`: Increase transmission power for 3243946_2
- `C22`: Increase A3 Offset threshold for 3235350_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.691 | MS1 | 121.4656677763 | 31.1446365866 | 299 | 504990 | -79.93 | 13.01 | 349.78 | 0.07 | 2.17 | 1569 |
| 2024-09-20 22:21:32.250 | MS1 | 121.4656752183 | 31.1446208920 | 299 | 504990 | -81.53 | 14.63 | 310.69 | 0.15 | 2.30 | 1566 |
| 2024-09-20 22:21:33.743 | MS1 | 121.4656728340 | 31.1446355208 | 299 | 504990 | -77.67 | 12.27 | 596.55 | 0.18 | 2.23 | 1567 |
| 2024-09-20 22:21:34.786 | MS1 | 121.4656696904 | 31.1446349391 | 299 | 504990 | -89.94 | -3.35 | 30.32 | 0.01 | 1.35 | 1563 |
| 2024-09-20 22:21:35.331 | MS1 | 121.4656720130 | 31.1446310149 | 299 | 504990 | -85.66 | -1.12 | 46.27 | 0.14 | 1.03 | 1581 |
| 2024-09-20 22:21:36.424 | MS1 | 121.4656723133 | 31.1446280331 | 299 | 504990 | -85.31 | -3.15 | 46.97 | 0.19 | 1.13 | 1574 |
| 2024-09-20 22:21:37.197 | MS1 | 121.4656613088 | 31.1446257306 | 299 | 504990 | -89.51 | -2.26 | 55.00 | 0.14 | 1.19 | 1580 |
| 2024-09-20 22:21:38.119 | MS1 | 121.4656593665 | 31.1446299555 | 299 | 504990 | -82.05 | 12.66 | 608.48 | 0.09 | 1.19 | 1583 |
| 2024-09-20 22:21:39.836 | MS1 | 121.4656666671 | 31.1446227217 | 299 | 504990 | -77.14 | 15.50 | 552.25 | 0.14 | 1.03 | 1569 |
| 2024-09-20 22:21:40.285 | MS1 | 121.4656631636 | 31.1446304694 | 299 | 504990 | -78.18 | 17.19 | 570.67 | 0.08 | 2.74 | 1594 |
| 2024-09-20 22:21:41.866 | MS1 | 121.4656659154 | 31.1446234130 | 299 | 504990 | -78.32 | 16.07 | 371.35 | 0.12 | 2.49 | 1568 |
| 2024-09-20 22:21:42.832 | MS1 | 121.4656671336 | 31.1446203881 | 299 | 504990 | -78.27 | 14.17 | 525.38 | 0.01 | 2.37 | 1588 |

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
| 3230706 | 4 | 121.4657991340 | 31.1446581824 | 64 | 4 | 1 | 24.6 | TDD | 182 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3230798 | 3 | 121.4732862783 | 31.1464031045 | 67 | 7 | 2 | 49.5 | TDD | 349 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3235350 | 1 | 121.4670465385 | 31.1537988856 | 171 | 5 | 7 | 35.7 | TDD | 299 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3243946 | 2 | 121.4651649803 | 31.1517184151 | 161 | 2 | 5 | 21.5 | TDD | 932 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.135 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.152 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.288 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.288 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.022 | NREventA3 | measId:2;ServCellPCI:363;Se... |
| 2024-09-20 22:21:36.022 | NREventA3 | measId:2;ServCellPCI:363;Se... |
| 2024-09-20 22:21:37.022 | NREventA3 | measId:2;ServCellPCI:363;Se... |
| 2024-09-20 22:21:39.522 | NRRRCReestablishAttempt | PCI:363 |
| 2024-09-20 22:21:39.536 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.547 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.696 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.696 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235350 | 1 | 18.4591 | 6.4316 | -115.8703 | 7.6137 | 106.4997 | 0.0086 | 0.1345 |
| 2024_09_20 22:00 | 3243946 | 2 | 19.1421 | 12.3836 | -117.1313 | 19.4713 | 159.2968 | 0.0014 | 0.0038 |
| 2024_09_20 22:00 | 3230798 | 3 | 10.4328 | 5.8026 | -116.7541 | 17.2214 | 174.2704 | 0.0190 | 0.0032 |
| 2024_09_20 22:00 | 3230706 | 4 | 18.2371 | 17.6262 | -116.6235 | 10.5477 | 127.5387 | 0.0138 | 0.0161 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414458_5538DB84 | 504990 | 299 | -90.1 | 504990 | 932 | -85.6 | 504990 | 349 | -95.9 | 504990 | 182 |
| MR_1774414458_0984255B | 504990 | 299 | -91.1 | 504990 | 932 | -84.1 | 504990 | 349 | -96.0 | 504990 | 182 |
| MR_1774414458_AA39FAB2 | 504990 | 299 | -88.3 | 504990 | 932 | -86.4 | 504990 | 349 | -96.6 | 504990 | 182 |
| MR_1774414458_D4C15672 | 504990 | 299 | -88.3 | 504990 | 932 | -83.2 | 504990 | 349 | -95.7 | 504990 | 182 |
| MR_1774414458_31579F17 | 504990 | 932 | -83.8 | 504990 | 299 | -89.0 | 504990 | 349 | -95.2 | 504990 | 182 |
| MR_1774414458_A05ECEEC | 504990 | 299 | -88.5 | 504990 | 932 | -86.1 | 504990 | 349 | -94.3 | 504990 | 182 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1662: `3e2ac3e3-bed...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3e2ac3e3-bed8-4f7c-aeea-ea1ec2a2ccb8` |
| Tag | **multiple-answer** |
| 정답 | **C3|C18** |
| C3 의미 | Adjust the azimuth of 3264746_1 by 38 degrees |
| C18 의미 | Increase transmission power for 3264746_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1662] topology](images/train_1662.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212428_2
- `C3`: Adjust the azimuth of 3264746_1 by 38 degrees **← 정답**
- `C4`: Increase A3 Offset threshold for 3212428_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212428_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264746_1
- `C7`: Add neighbor relationship between 3241432_4 and 3212428_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264746_1
- `C9`: Decrease transmission power for 3264746_1
- `C10`: Adjust the azimuth of 3212428_2 by 13 degrees
- `C11`: Increase transmission power for 3212428_2
- `C12`: Increase A3 Offset threshold for 3264746_1
- `C13`: Decrease A3 Offset threshold for 3212428_2
- `C14`: Lift the tilt angle of 3264746_1 by 10 degrees
- `C15`: Add neighbor relationship between 3264746_1 and 3212428_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease transmission power for 3212428_2
- `C18`: Increase transmission power for 3264746_1 **← 정답**
- `C19`: Decrease A3 Offset threshold for 3264746_1
- `C20`: Press down the tilt angle  of 3212428_2 by 5 degrees
- `C21`: Lift the tilt angle  of 3212428_2 by 5 degrees
- `C22`: Press down the tilt angle of 3264746_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.227 | MS1 | 121.4656696382 | 31.1446299793 | 562 | 504990 | -88.55 | 15.66 | 352.95 | 0.05 | 2.59 | 1578 |
| 2024-09-20 22:21:32.928 | MS1 | 121.4656766661 | 31.1446361366 | 562 | 504990 | -94.74 | 16.75 | 404.23 | 0.01 | 2.47 | 1575 |
| 2024-09-20 22:21:33.932 | MS1 | 121.4656690916 | 31.1446340458 | 562 | 504990 | -91.59 | 13.37 | 431.56 | 0.04 | 2.74 | 1589 |
| 2024-09-20 22:21:34.244 | MS1 | 121.4656740909 | 31.1446301501 | 562 | 504990 | -100.68 | -0.90 | 57.34 | 0.07 | 1.27 | 1574 |
| 2024-09-20 22:21:35.845 | MS1 | 121.4656774729 | 31.1446209217 | 562 | 504990 | -100.91 | -0.17 | 16.32 | 0.14 | 1.21 | 1588 |
| 2024-09-20 22:21:36.272 | MS1 | 121.4656595030 | 31.1446247640 | 562 | 504990 | -104.59 | 0.26 | 26.37 | 0.17 | 1.12 | 1599 |
| 2024-09-20 22:21:37.998 | MS1 | 121.4656676622 | 31.1446259549 | 562 | 504990 | -101.21 | -1.40 | 18.44 | 0.08 | 1.27 | 1597 |
| 2024-09-20 22:21:38.815 | MS1 | 121.4656712203 | 31.1446266525 | 562 | 504990 | -100.86 | -1.25 | 45.22 | 0.03 | 1.23 | 1569 |
| 2024-09-20 22:21:39.352 | MS1 | 121.4656691685 | 31.1446335766 | 562 | 504990 | -101.10 | 0.17 | 69.00 | 0.15 | 1.28 | 1570 |
| 2024-09-20 22:21:40.382 | MS1 | 121.4656614219 | 31.1446318301 | 562 | 504990 | -87.34 | 16.46 | 377.69 | 0.09 | 2.87 | 1573 |
| 2024-09-20 22:21:41.191 | MS1 | 121.4656627356 | 31.1446252106 | 562 | 504990 | -89.23 | 15.26 | 555.63 | 0.19 | 2.32 | 1587 |
| 2024-09-20 22:21:42.860 | MS1 | 121.4656651410 | 31.1446374779 | 562 | 504990 | -88.28 | 12.13 | 398.14 | 0.06 | 2.70 | 1568 |

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
| 3212428 | 2 | 121.4654973497 | 31.1468478425 | 163 | 1 | 3 | 19.2 | TDD | 570 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3241432 | 4 | 121.4676044614 | 31.1472794383 | 263 | 4 | 6 | 23.3 | TDD | 46 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3264746 | 1 | 121.4750746928 | 31.1546369649 | 257 | 12 | 3 | 44.0 | TDD | 562 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3267127 | 3 | 121.4750465650 | 31.1483527084 | 31 | 13 | 4 | 24.8 | TDD | 509 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.065 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.166 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.166 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.418 | NREventA2 | measId:1;ServCellPCI:157;Se... |
| 2024-09-20 22:21:34.532 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264746 | 1 | 9.0533 | 14.9635 | -117.5759 | 5.5160 | 111.8232 | 0.1318 | 0.0076 |
| 2024_09_20 22:00 | 3212428 | 2 | 14.2138 | 16.4339 | -116.7877 | 18.8747 | 125.4087 | 0.0114 | 0.0043 |
| 2024_09_20 22:00 | 3267127 | 3 | 16.7284 | 19.3106 | -114.9322 | 6.5753 | 88.9375 | 0.0041 | 0.0138 |
| 2024_09_20 22:00 | 3241432 | 4 | 13.8085 | 9.9080 | -115.8541 | 12.9204 | 178.6660 | 0.0054 | 0.0008 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413097_A71947B7 | 504990 | 562 | -100.7 | 504990 | 570 | -109.1 | 504990 | 46 | -111.5 | 504990 | 509 |
| MR_1774413097_CC3FD686 | 504990 | 562 | -99.7 | 504990 | 570 | -108.8 | 504990 | 46 | -110.6 | 504990 | 509 |
| MR_1774413097_A51AFA4C | 504990 | 562 | -99.0 | 504990 | 570 | -108.3 | 504990 | 46 | -109.9 | 504990 | 509 |
| MR_1774413097_64ADF17A | 504990 | 562 | -101.0 | 504990 | 570 | -109.9 | 504990 | 46 | -111.9 | 504990 | 509 |
| MR_1774413097_BAFC9E32 | 504990 | 562 | -102.7 | 504990 | 570 | -108.3 | 504990 | 46 | -110.4 | 504990 | 509 |
| MR_1774413097_BB4D91A1 | 504990 | 562 | -100.9 | 504990 | 570 | -109.8 | 504990 | 46 | -112.3 | 504990 | 509 |
| MR_1774413097_6B824296 | 504990 | 562 | -102.4 | 504990 | 570 | -107.9 | 504990 | 46 | -113.1 | 504990 | 509 |
| MR_1774413097_C350F50E | 504990 | 562 | -102.3 | 504990 | 570 | -108.4 | 504990 | 46 | -111.2 | 504990 | 509 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1663: `41cbed7e-f87...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `41cbed7e-f877-4fd4-88f8-bbc0137cbd0c` |
| Tag | **multiple-answer** |
| 정답 | **C5|C14** |
| C5 의미 | Adjust the azimuth of 3253223_3 by 50 degrees |
| C14 의미 | Increase transmission power for 3253223_3 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1663] topology](images/train_1663.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3253223_3
- `C2`: Increase transmission power for 3240152_4
- `C3`: Lift the tilt angle of 3253223_3 by 10 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Adjust the azimuth of 3253223_3 by 50 degrees **← 정답**
- `C6`: Adjust the azimuth of 3240152_4 by 27 degrees
- `C7`: Press down the tilt angle of 3253223_3 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3240152_4
- `C9`: Increase A3 Offset threshold for 3240152_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253223_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253223_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240152_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240152_4
- `C14`: Increase transmission power for 3253223_3 **← 정답**
- `C15`: Press down the tilt angle  of 3240152_4 by 5 degrees
- `C16`: Decrease transmission power for 3240152_4
- `C17`: Lift the tilt angle  of 3240152_4 by 5 degrees
- `C18`: Check test server and transmission issues
- `C19`: Add neighbor relationship between 3253223_3 and 3240152_4
- `C20`: Increase A3 Offset threshold for 3253223_3
- `C21`: Add neighbor relationship between 3247599_2 and 3240152_4
- `C22`: Decrease transmission power for 3253223_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.498 | MS1 | 121.4656589292 | 31.1446200510 | 161 | 504990 | -89.15 | 12.68 | 565.64 | 0.00 | 2.67 | 1569 |
| 2024-09-20 22:21:32.860 | MS1 | 121.4656770606 | 31.1446362808 | 161 | 504990 | -86.40 | 14.08 | 305.59 | 0.14 | 3.00 | 1591 |
| 2024-09-20 22:21:33.770 | MS1 | 121.4656730495 | 31.1446310329 | 161 | 504990 | -89.53 | 13.91 | 504.94 | 0.13 | 2.61 | 1587 |
| 2024-09-20 22:21:34.280 | MS1 | 121.4656753189 | 31.1446235151 | 161 | 504990 | -106.48 | -1.92 | 43.05 | 0.20 | 1.39 | 1578 |
| 2024-09-20 22:21:35.713 | MS1 | 121.4656652503 | 31.1446351375 | 161 | 504990 | -108.34 | -1.22 | 23.56 | 0.19 | 1.10 | 1584 |
| 2024-09-20 22:21:36.116 | MS1 | 121.4656661657 | 31.1446236542 | 161 | 504990 | -102.58 | 0.53 | 69.42 | 0.04 | 1.24 | 1596 |
| 2024-09-20 22:21:37.916 | MS1 | 121.4656603977 | 31.1446378924 | 161 | 504990 | -107.09 | 0.61 | 73.78 | 0.13 | 1.07 | 1574 |
| 2024-09-20 22:21:38.573 | MS1 | 121.4656669647 | 31.1446259632 | 161 | 504990 | -101.58 | 1.23 | 46.07 | 0.20 | 1.13 | 1579 |
| 2024-09-20 22:21:39.447 | MS1 | 121.4656593904 | 31.1446284436 | 161 | 504990 | -102.17 | -1.87 | 71.60 | 0.05 | 1.29 | 1579 |
| 2024-09-20 22:21:40.936 | MS1 | 121.4656612236 | 31.1446247730 | 161 | 504990 | -93.01 | 16.35 | 509.63 | 0.17 | 2.35 | 1569 |
| 2024-09-20 22:21:41.730 | MS1 | 121.4656697267 | 31.1446234251 | 161 | 504990 | -93.53 | 12.83 | 325.32 | 0.14 | 2.93 | 1591 |
| 2024-09-20 22:21:42.941 | MS1 | 121.4656598820 | 31.1446217604 | 161 | 504990 | -91.28 | 17.06 | 536.62 | 0.05 | 2.28 | 1586 |

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
| 3240152 | 4 | 121.4655096789 | 31.1536356295 | 152 | 2 | 0 | 45.5 | TDD | 571 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3247599 | 2 | 121.4757557239 | 31.1527883600 | 160 | 6 | 11 | 45.2 | TDD | 242 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3253223 | 3 | 121.4675505943 | 31.1457344105 | 286 | 13 | 0 | 36.5 | TDD | 161 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3269507 | 1 | 121.4750293557 | 31.1510231457 | 165 | 1 | 4 | 41.6 | TDD | 89 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.211 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.211 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.430 | NREventA2 | measId:1;ServCellPCI:857;Se... |
| 2024-09-20 22:21:34.570 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269507 | 1 | 19.4607 | 12.3292 | -115.5640 | 14.3062 | 114.3608 | 0.0128 | 0.0024 |
| 2024_09_20 22:00 | 3247599 | 2 | 6.1649 | 18.1574 | -116.2297 | 19.3190 | 145.6527 | 0.0101 | 0.0082 |
| 2024_09_20 22:00 | 3253223 | 3 | 19.9225 | 15.4646 | -117.4977 | 19.2864 | 124.0092 | 0.1858 | 0.0177 |
| 2024_09_20 22:00 | 3240152 | 4 | 7.1758 | 11.0832 | -116.4035 | 18.3437 | 168.3850 | 0.0063 | 0.0101 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414256_84C92CF9 | 504990 | 161 | -106.8 | 504990 | 571 | -113.5 | 504990 | 242 | -117.9 | 504990 | 89 |
| MR_1774414256_5506344D | 504990 | 161 | -107.4 | 504990 | 571 | -114.1 | 504990 | 242 | -117.8 | 504990 | 89 |
| MR_1774414256_646FEFDC | 504990 | 161 | -105.7 | 504990 | 571 | -112.0 | 504990 | 242 | -120.3 | 504990 | 89 |
| MR_1774414256_062A7890 | 504990 | 161 | -106.6 | 504990 | 571 | -113.7 | 504990 | 242 | -120.6 | 504990 | 89 |
| MR_1774414256_57994A11 | 504990 | 161 | -106.0 | 504990 | 571 | -114.1 | 504990 | 242 | -120.5 | 504990 | 89 |
| MR_1774414256_B52FCE64 | 504990 | 161 | -107.3 | 504990 | 571 | -113.3 | 504990 | 242 | -119.8 | 504990 | 89 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1664: `2d9658b0-0c4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2d9658b0-0c40-4be4-9128-fc770b404bad` |
| Tag | **multiple-answer** |
| 정답 | **C5|C6** |
| C5 의미 | Press down the tilt angle  of 3246896_3 by 5 degrees |
| C6 의미 | Decrease transmission power for 3246896_3 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1664] topology](images/train_1664.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Lift the tilt angle of 3230937_1 by 2 degrees
- `C3`: Increase A3 Offset threshold for 3230937_1
- `C4`: Increase transmission power for 3246896_3
- `C5`: Press down the tilt angle  of 3246896_3 by 5 degrees **← 정답**
- `C6`: Decrease transmission power for 3246896_3 **← 정답**
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246896_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230937_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230937_1
- `C10`: Decrease transmission power for 3230937_1
- `C11`: Increase transmission power for 3230937_1
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease A3 Offset threshold for 3230937_1
- `C14`: Adjust the azimuth of 3246896_3 by 13 degrees
- `C15`: Increase A3 Offset threshold for 3246896_3
- `C16`: Lift the tilt angle  of 3246896_3 by 5 degrees
- `C17`: Add neighbor relationship between 3225805_2 and 3246896_3
- `C18`: Add neighbor relationship between 3230937_1 and 3246896_3
- `C19`: Press down the tilt angle of 3230937_1 by 2 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246896_3
- `C21`: Decrease A3 Offset threshold for 3246896_3
- `C22`: Adjust the azimuth of 3230937_1 by 33 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.209 | MS1 | 121.4656603119 | 31.1446194069 | 696 | 504990 | -81.12 | 15.94 | 393.99 | 0.18 | 2.42 | 1564 |
| 2024-09-20 22:21:32.803 | MS1 | 121.4656738588 | 31.1446239643 | 696 | 504990 | -78.26 | 16.11 | 447.45 | 0.05 | 2.99 | 1577 |
| 2024-09-20 22:21:33.697 | MS1 | 121.4656626638 | 31.1446275720 | 696 | 504990 | -76.49 | 15.92 | 358.58 | 0.04 | 2.07 | 1569 |
| 2024-09-20 22:21:34.576 | MS1 | 121.4656602913 | 31.1446238155 | 696 | 504990 | -87.98 | 1.70 | 68.49 | 0.07 | 1.38 | 1585 |
| 2024-09-20 22:21:35.199 | MS1 | 121.4656668844 | 31.1446261084 | 696 | 504990 | -90.62 | 3.16 | 48.99 | 0.19 | 1.19 | 1595 |
| 2024-09-20 22:21:36.136 | MS1 | 121.4656604080 | 31.1446201117 | 696 | 504990 | -85.28 | 2.77 | 58.84 | 0.02 | 1.19 | 1582 |
| 2024-09-20 22:21:37.797 | MS1 | 121.4656585584 | 31.1446287246 | 696 | 504990 | -89.60 | 0.84 | 69.03 | 0.01 | 1.11 | 1588 |
| 2024-09-20 22:21:38.294 | MS1 | 121.4656757268 | 31.1446265286 | 696 | 504990 | -88.40 | 1.11 | 84.48 | 0.19 | 1.13 | 1560 |
| 2024-09-20 22:21:39.302 | MS1 | 121.4656655558 | 31.1446294557 | 696 | 504990 | -92.25 | 0.58 | 67.10 | 0.07 | 1.09 | 1569 |
| 2024-09-20 22:21:40.589 | MS1 | 121.4656694810 | 31.1446297218 | 696 | 504990 | -79.45 | 15.70 | 529.87 | 0.13 | 2.69 | 1576 |
| 2024-09-20 22:21:41.390 | MS1 | 121.4656733871 | 31.1446305358 | 696 | 504990 | -75.83 | 12.21 | 337.74 | 0.05 | 2.02 | 1599 |
| 2024-09-20 22:21:42.993 | MS1 | 121.4656718810 | 31.1446341481 | 696 | 504990 | -81.39 | 15.34 | 542.33 | 0.06 | 2.87 | 1569 |

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
| 3225805 | 2 | 121.4749777905 | 31.1534712774 | 30 | 1 | 5 | 47.0 | TDD | 82 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3230937 | 1 | 121.4706825555 | 31.1529244974 | 240 | 1 | 12 | 19.0 | TDD | 696 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3246896 | 3 | 121.4681978803 | 31.1526346249 | 182 | 3 | 8 | 32.8 | TDD | 128 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3264982 | 4 | 121.4744743060 | 31.1556979590 | 0 | 4 | 3 | 34.9 | TDD | 144 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.187 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.210 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.333 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.333 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230937 | 1 | 15.9227 | 15.4238 | -109.2504 | 18.3094 | 126.0263 | 0.0101 | 0.0169 |
| 2024_09_20 22:00 | 3225805 | 2 | 16.2669 | 7.9830 | -115.1869 | 5.3855 | 93.4260 | 0.0074 | 0.0065 |
| 2024_09_20 22:00 | 3246896 | 3 | 6.6893 | 18.8374 | -117.4584 | 7.1022 | 113.7659 | 0.0181 | 0.0088 |
| 2024_09_20 22:00 | 3264982 | 4 | 5.4522 | 16.2189 | -117.4663 | 15.6421 | 152.8245 | 0.0026 | 0.0003 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414701_64E23B76 | 504990 | 128 | -88.9 | 504990 | 696 | -82.8 | 504990 | 82 | -87.6 | 504990 | 144 |
| MR_1774414701_95C46D95 | 504990 | 696 | -86.3 | 504990 | 128 | -85.5 | 504990 | 82 | -84.7 | 504990 | 144 |
| MR_1774414701_6315AC45 | 504990 | 128 | -86.3 | 504990 | 696 | -85.0 | 504990 | 82 | -87.2 | 504990 | 144 |
| MR_1774414701_F3781D16 | 504990 | 696 | -86.1 | 504990 | 128 | -85.0 | 504990 | 82 | -87.5 | 504990 | 144 |
| MR_1774414701_2140756C | 504990 | 696 | -89.4 | 504990 | 128 | -83.0 | 504990 | 82 | -86.7 | 504990 | 144 |
| MR_1774414701_9FCA2DF7 | 504990 | 128 | -89.1 | 504990 | 696 | -85.9 | 504990 | 82 | -84.0 | 504990 | 144 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1665: `37b08ea1-958...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `37b08ea1-958a-4a01-95dc-3befac204033` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1665] topology](images/train_1665.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3236699_1
- `C2`: Check test server and transmission issues
- `C3`: Add neighbor relationship between 3270814_2 and 3236699_1
- `C4`: Decrease A3 Offset threshold for 3270814_2
- `C5`: Increase A3 Offset threshold for 3236699_1
- `C6`: Lift the tilt angle of 3270814_2 by 10 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236699_1
- `C8`: Adjust the azimuth of 3236699_1 by 50 degrees
- `C9`: Decrease transmission power for 3270814_2
- `C10`: Increase transmission power for 3270814_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270814_2
- `C12`: Press down the tilt angle of 3270814_2 by 10 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270814_2
- `C14`: Decrease A3 Offset threshold for 3236699_1
- `C15`: Increase A3 Offset threshold for 3270814_2
- `C16`: Increase transmission power for 3236699_1
- `C17`: Adjust the azimuth of 3270814_2 by 50 degrees
- `C18`: Insufficient data; more data is needed for judgment. **← 정답**
- `C19`: Lift the tilt angle  of 3236699_1 by 10 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236699_1
- `C21`: Add neighbor relationship between 3230088_3 and 3236699_1
- `C22`: Press down the tilt angle  of 3236699_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.566 | MS1 | 121.4656751433 | 31.1446315382 | 635 | 504990 | -87.58 | 14.52 | 324.80 | 0.05 | 2.91 | 1565 |
| 2024-09-20 22:21:32.252 | MS1 | 121.4656668524 | 31.1446342167 | 635 | 504990 | -86.98 | 13.51 | 319.02 | 0.06 | 2.45 | 1575 |
| 2024-09-20 22:21:33.699 | MS1 | 121.4656632950 | 31.1446360167 | 635 | 504990 | -86.29 | 16.28 | 339.77 | 0.10 | 2.40 | 1592 |
| 2024-09-20 22:21:34.794 | MS1 | 121.4656763215 | 31.1446335971 | 635 | 504990 | -89.28 | 13.07 | 71.46 | 0.15 | 2.23 | 1574 |
| 2024-09-20 22:21:35.955 | MS1 | 121.4656700765 | 31.1446286878 | 635 | 504990 | -85.87 | 15.72 | 93.47 | 0.11 | 2.78 | 1572 |
| 2024-09-20 22:21:36.636 | MS1 | 121.4656719123 | 31.1446309931 | 635 | 504990 | -90.86 | 13.55 | 75.53 | 0.03 | 2.80 | 1588 |
| 2024-09-20 22:21:37.476 | MS1 | 121.4656598386 | 31.1446231880 | 635 | 504990 | -90.92 | 8.87 | 102.10 | 0.02 | 2.71 | 1571 |
| 2024-09-20 22:21:38.141 | MS1 | 121.4656696937 | 31.1446321812 | 635 | 504990 | -90.65 | 12.88 | 74.47 | 0.03 | 2.69 | 1570 |
| 2024-09-20 22:21:39.917 | MS1 | 121.4656737362 | 31.1446239317 | 635 | 504990 | -90.41 | 10.81 | 63.82 | 0.10 | 2.69 | 1567 |
| 2024-09-20 22:21:40.411 | MS1 | 121.4656689499 | 31.1446230696 | 635 | 504990 | -90.82 | 11.81 | 562.64 | 0.06 | 2.66 | 1572 |
| 2024-09-20 22:21:41.785 | MS1 | 121.4656753091 | 31.1446268590 | 635 | 504990 | -92.10 | 10.53 | 367.75 | 0.03 | 2.99 | 1566 |
| 2024-09-20 22:21:42.580 | MS1 | 121.4656703685 | 31.1446189474 | 635 | 504990 | -90.97 | 9.70 | 569.09 | 0.16 | 2.16 | 1569 |

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
| 3212675 | 4 | 121.4750310029 | 31.1454765436 | 113 | 12 | 8 | 16.5 | TDD | 343 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3230088 | 3 | 121.4694750574 | 31.1445421900 | 327 | 10 | 8 | 27.3 | TDD | 509 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3236699 | 1 | 121.4716507277 | 31.1452675177 | 349 | 7 | 10 | 45.9 | TDD | 784 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3270814 | 2 | 121.4725890086 | 31.1465953104 | 198 | 9 | 11 | 22.6 | TDD | 635 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.224 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.334 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.334 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.050 | NREventA3 | measId:2;ServCellPCI:641;Se... |
| 2024-09-20 22:21:38.290 | NRHandoverAttempt | SourcePCI:641;SourceNR-ARFC... |
| 2024-09-20 22:21:38.335 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.348 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.479 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.479 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3236699 | 1 | 77.6611 | 84.0131 | -114.7344 | 9.9302 | 140.8053 | 0.0005 | 0.0139 |
| 2024_09_19 22:00 | 3270814 | 2 | 80.4906 | 75.4994 | -116.3355 | 11.6804 | 180.7016 | 0.0114 | 0.0055 |
| 2024_09_19 22:00 | 3230088 | 3 | 82.9373 | 81.2710 | -116.4453 | 14.9922 | 191.9105 | 0.0146 | 0.0069 |
| 2024_09_19 22:00 | 3212675 | 4 | 86.0253 | 86.5752 | -117.2702 | 15.2174 | 174.8091 | 0.0034 | 0.0141 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411981_61C76EDF | 504990 | 635 | -87.9 | 504990 | 784 | -93.1 | 504990 | 509 | -98.7 | 504990 | 343 |
| MR_1774411981_6223D0B1 | 504990 | 635 | -91.1 | 504990 | 784 | -93.9 | 504990 | 509 | -98.0 | 504990 | 343 |
| MR_1774411981_35B0A12D | 504990 | 635 | -89.7 | 504990 | 784 | -95.2 | 504990 | 509 | -97.5 | 504990 | 343 |
| MR_1774411981_2D55AC4C | 504990 | 635 | -87.7 | 504990 | 784 | -95.7 | 504990 | 509 | -98.8 | 504990 | 343 |
| MR_1774411981_CE14A03B | 504990 | 635 | -88.2 | 504990 | 784 | -93.7 | 504990 | 509 | -100.2 | 504990 | 343 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1666: `796d5c24-c51...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `796d5c24-c518-495a-87a5-cd8d65c1fbde` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1666] topology](images/train_1666.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3210217_1 by 50 degrees
- `C2`: Lift the tilt angle of 3210217_1 by 10 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210217_1
- `C4`: Check test server and transmission issues **← 정답**
- `C5`: Lift the tilt angle  of 3269111_4 by 8 degrees
- `C6`: Increase transmission power for 3210217_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210217_1
- `C8`: Press down the tilt angle  of 3269111_4 by 8 degrees
- `C9`: Decrease transmission power for 3269111_4
- `C10`: Decrease A3 Offset threshold for 3210217_1
- `C11`: Press down the tilt angle of 3210217_1 by 10 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease A3 Offset threshold for 3269111_4
- `C14`: Increase A3 Offset threshold for 3210217_1
- `C15`: Increase A3 Offset threshold for 3269111_4
- `C16`: Add neighbor relationship between 3210217_1 and 3269111_4
- `C17`: Increase transmission power for 3269111_4
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269111_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269111_4
- `C20`: Add neighbor relationship between 3210391_2 and 3269111_4
- `C21`: Decrease transmission power for 3210217_1
- `C22`: Adjust the azimuth of 3269111_4 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.240 | MS1 | 121.4656712520 | 31.1446199001 | 122 | 504990 | -87.78 | 14.13 | 451.12 | 0.16 | 2.97 | 1600 |
| 2024-09-20 22:21:32.554 | MS1 | 121.4656626603 | 31.1446251707 | 122 | 504990 | -88.24 | 17.05 | 324.74 | 0.19 | 2.67 | 1568 |
| 2024-09-20 22:21:33.619 | MS1 | 121.4656702822 | 31.1446322226 | 122 | 504990 | -86.21 | 13.25 | 471.07 | 0.09 | 2.62 | 1598 |
| 2024-09-20 22:21:34.216 | MS1 | 121.4656600515 | 31.1446235104 | 122 | 504990 | -88.39 | 12.40 | 61.74 | 0.17 | 2.71 | 417 |
| 2024-09-20 22:21:35.400 | MS1 | 121.4656643045 | 31.1446293589 | 122 | 504990 | -87.03 | 12.57 | 80.96 | 0.12 | 2.29 | 489 |
| 2024-09-20 22:21:36.218 | MS1 | 121.4656624246 | 31.1446209264 | 122 | 504990 | -86.34 | 14.27 | 98.90 | 0.11 | 2.12 | 321 |
| 2024-09-20 22:21:37.514 | MS1 | 121.4656620558 | 31.1446278761 | 122 | 504990 | -93.89 | 11.68 | 85.77 | 0.03 | 2.05 | 413 |
| 2024-09-20 22:21:38.934 | MS1 | 121.4656592657 | 31.1446236310 | 122 | 504990 | -90.11 | 10.21 | 68.36 | 0.10 | 2.13 | 457 |
| 2024-09-20 22:21:39.307 | MS1 | 121.4656741992 | 31.1446220657 | 122 | 504990 | -89.75 | 10.71 | 43.73 | 0.08 | 2.59 | 395 |
| 2024-09-20 22:21:40.255 | MS1 | 121.4656714397 | 31.1446345887 | 122 | 504990 | -92.19 | 10.41 | 364.51 | 0.19 | 2.78 | 1576 |
| 2024-09-20 22:21:41.347 | MS1 | 121.4656654710 | 31.1446316017 | 122 | 504990 | -90.69 | 9.59 | 499.01 | 0.12 | 2.67 | 1592 |
| 2024-09-20 22:21:42.361 | MS1 | 121.4656644447 | 31.1446327124 | 122 | 504990 | -91.97 | 7.04 | 576.63 | 0.07 | 2.60 | 1571 |

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
| 3210217 | 1 | 121.4670797015 | 31.1517529846 | 341 | 9 | 2 | 36.3 | TDD | 122 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3210391 | 2 | 121.4667326379 | 31.1517484251 | 5 | 12 | 8 | 43.6 | TDD | 755 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3214943 | 3 | 121.4678711007 | 31.1456915128 | 151 | 14 | 8 | 42.4 | TDD | 556 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3269111 | 4 | 121.4697670274 | 31.1538103139 | 96 | 6 | 6 | 47.5 | TDD | 645 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.771 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.792 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.917 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.917 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.661 | NREventA3 | measId:2;ServCellPCI:402;Se... |
| 2024-09-20 22:21:37.901 | NRHandoverAttempt | SourcePCI:402;SourceNR-ARFC... |
| 2024-09-20 22:21:37.945 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.955 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.068 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.068 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210217 | 1 | 13.2398 | 11.5091 | -116.6525 | 12.5396 | 144.4138 | 0.0145 | 0.0172 |
| 2024_09_20 22:00 | 3210391 | 2 | 9.1178 | 17.1024 | -115.2074 | 18.5341 | 110.7449 | 0.0068 | 0.0196 |
| 2024_09_20 22:00 | 3214943 | 3 | 18.8508 | 15.4321 | -116.4019 | 17.7619 | 177.4582 | 0.0115 | 0.0195 |
| 2024_09_20 22:00 | 3269111 | 4 | 18.4671 | 18.7776 | -116.9185 | 11.2884 | 171.0884 | 0.0021 | 0.0073 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414547_4531C18B | 504990 | 122 | -88.9 | 504990 | 645 | -89.8 | 504990 | 755 | -101.7 | 504990 | 556 |
| MR_1774414547_0FDEAFE4 | 504990 | 122 | -89.8 | 504990 | 645 | -87.6 | 504990 | 755 | -105.2 | 504990 | 556 |
| MR_1774414547_8BE4C42E | 504990 | 122 | -90.0 | 504990 | 645 | -89.0 | 504990 | 755 | -102.0 | 504990 | 556 |
| MR_1774414547_630133CF | 504990 | 122 | -88.5 | 504990 | 645 | -87.0 | 504990 | 755 | -103.6 | 504990 | 556 |
| MR_1774414547_FD0169E1 | 504990 | 122 | -89.5 | 504990 | 645 | -88.5 | 504990 | 755 | -105.0 | 504990 | 556 |
| MR_1774414547_4812C937 | 504990 | 122 | -87.1 | 504990 | 645 | -87.4 | 504990 | 755 | -105.2 | 504990 | 556 |
| MR_1774414547_884332B7 | 504990 | 122 | -88.8 | 504990 | 645 | -89.0 | 504990 | 755 | -104.8 | 504990 | 556 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1667: `fabbe292-29e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fabbe292-29e1-4d3e-a248-4fd74b5f4de6` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1667] topology](images/train_1667.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3243934_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Check test server and transmission issues **← 정답**
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243934_2
- `C5`: Decrease transmission power for 3246019_4
- `C6`: Lift the tilt angle of 3243934_2 by 10 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246019_4
- `C8`: Decrease transmission power for 3243934_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246019_4
- `C10`: Increase transmission power for 3246019_4
- `C11`: Adjust the azimuth of 3246019_4 by 50 degrees
- `C12`: Add neighbor relationship between 3243934_2 and 3246019_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243934_2
- `C14`: Lift the tilt angle  of 3246019_4 by 10 degrees
- `C15`: Increase A3 Offset threshold for 3246019_4
- `C16`: Add neighbor relationship between 3224265_3 and 3246019_4
- `C17`: Adjust the azimuth of 3243934_2 by 50 degrees
- `C18`: Increase transmission power for 3243934_2
- `C19`: Press down the tilt angle of 3243934_2 by 10 degrees
- `C20`: Decrease A3 Offset threshold for 3246019_4
- `C21`: Increase A3 Offset threshold for 3243934_2
- `C22`: Press down the tilt angle  of 3246019_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.683 | MS1 | 121.4656653560 | 31.1446213736 | 36 | 504990 | -85.13 | 16.64 | 531.62 | 0.19 | 2.92 | 1593 |
| 2024-09-20 22:21:32.369 | MS1 | 121.4656641218 | 31.1446197477 | 36 | 504990 | -87.30 | 17.41 | 494.27 | 0.19 | 2.70 | 1592 |
| 2024-09-20 22:21:33.499 | MS1 | 121.4656694849 | 31.1446203062 | 36 | 504990 | -85.78 | 13.36 | 532.81 | 0.17 | 2.79 | 1598 |
| 2024-09-20 22:21:34.595 | MS1 | 121.4656735492 | 31.1446275196 | 36 | 504990 | -85.20 | 14.74 | 73.63 | 0.09 | 2.04 | 452 |
| 2024-09-20 22:21:35.707 | MS1 | 121.4656746028 | 31.1446239741 | 36 | 504990 | -88.24 | 13.50 | 81.63 | 0.07 | 2.48 | 441 |
| 2024-09-20 22:21:36.597 | MS1 | 121.4656589742 | 31.1446346155 | 36 | 504990 | -91.32 | 16.10 | 62.69 | 0.15 | 2.17 | 311 |
| 2024-09-20 22:21:37.198 | MS1 | 121.4656766169 | 31.1446275010 | 36 | 504990 | -89.91 | 12.58 | 56.33 | 0.12 | 2.72 | 427 |
| 2024-09-20 22:21:38.593 | MS1 | 121.4656724838 | 31.1446286590 | 36 | 504990 | -92.63 | 7.51 | 42.72 | 0.16 | 2.96 | 338 |
| 2024-09-20 22:21:39.286 | MS1 | 121.4656769555 | 31.1446332101 | 36 | 504990 | -90.55 | 8.92 | 77.72 | 0.12 | 2.77 | 459 |
| 2024-09-20 22:21:40.293 | MS1 | 121.4656747232 | 31.1446269092 | 36 | 504990 | -91.03 | 8.29 | 475.28 | 0.12 | 2.46 | 1581 |
| 2024-09-20 22:21:41.235 | MS1 | 121.4656617731 | 31.1446369879 | 36 | 504990 | -93.88 | 12.77 | 457.86 | 0.16 | 2.51 | 1578 |
| 2024-09-20 22:21:42.311 | MS1 | 121.4656736313 | 31.1446199767 | 36 | 504990 | -89.92 | 10.13 | 330.67 | 0.12 | 2.15 | 1571 |

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
| 3224265 | 3 | 121.4660440989 | 31.1535013350 | 253 | 12 | 4 | 29.3 | TDD | 581 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3243832 | 1 | 121.4751690276 | 31.1517972399 | 154 | 1 | 7 | 28.9 | TDD | 803 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3243934 | 2 | 121.4733702921 | 31.1472125165 | 145 | 12 | 0 | 49.1 | TDD | 36 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3246019 | 4 | 121.4687242458 | 31.1485589363 | 138 | 14 | 11 | 48.2 | TDD | 661 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.953 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.974 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.096 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.096 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.809 | NREventA3 | measId:2;ServCellPCI:794;Se... |
| 2024-09-20 22:21:38.049 | NRHandoverAttempt | SourcePCI:794;SourceNR-ARFC... |
| 2024-09-20 22:21:38.091 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.106 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.208 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.208 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243832 | 1 | 12.7313 | 8.5798 | -115.0050 | 19.8450 | 151.8197 | 0.0191 | 0.0081 |
| 2024_09_20 22:00 | 3243934 | 2 | 10.6369 | 7.9797 | -114.4064 | 13.9747 | 85.7155 | 0.0127 | 0.0198 |
| 2024_09_20 22:00 | 3224265 | 3 | 9.3622 | 17.3531 | -115.5167 | 6.1664 | 141.0013 | 0.0186 | 0.0071 |
| 2024_09_20 22:00 | 3246019 | 4 | 18.6564 | 19.0235 | -117.5179 | 6.5244 | 179.9366 | 0.0138 | 0.0199 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414876_6C96F431 | 504990 | 36 | -84.9 | 504990 | 661 | -93.7 | 504990 | 581 | -100.2 | 504990 | 803 |
| MR_1774414876_F26E28AF | 504990 | 36 | -83.5 | 504990 | 661 | -93.0 | 504990 | 581 | -98.2 | 504990 | 803 |
| MR_1774414876_4C7DAF52 | 504990 | 36 | -84.9 | 504990 | 661 | -95.4 | 504990 | 581 | -97.0 | 504990 | 803 |
| MR_1774414876_9186A210 | 504990 | 36 | -87.0 | 504990 | 661 | -93.9 | 504990 | 581 | -96.7 | 504990 | 803 |
| MR_1774414876_9E9B192B | 504990 | 36 | -85.7 | 504990 | 661 | -96.8 | 504990 | 581 | -97.0 | 504990 | 803 |
| MR_1774414876_91978757 | 504990 | 36 | -85.0 | 504990 | 661 | -94.4 | 504990 | 581 | -99.7 | 504990 | 803 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1668: `95d86c05-b35...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `95d86c05-b35f-405c-ac37-fdf032c6394a` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1668] topology](images/train_1668.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3250687_2 by 9 degrees
- `C2`: Increase A3 Offset threshold for 3235651_1
- `C3`: Lift the tilt angle of 3235651_1 by 10 degrees
- `C4`: Decrease transmission power for 3235651_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235651_1
- `C6`: Lift the tilt angle  of 3250687_2 by 9 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease A3 Offset threshold for 3235651_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250687_2
- `C10`: Decrease A3 Offset threshold for 3250687_2
- `C11`: Increase A3 Offset threshold for 3250687_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235651_1
- `C13`: Add neighbor relationship between 3214113_4 and 3250687_2
- `C14`: Decrease transmission power for 3250687_2
- `C15`: Add neighbor relationship between 3235651_1 and 3250687_2
- `C16`: Increase transmission power for 3250687_2
- `C17`: Adjust the azimuth of 3250687_2 by 50 degrees
- `C18`: Press down the tilt angle of 3235651_1 by 10 degrees
- `C19`: Increase transmission power for 3235651_1
- `C20`: Check test server and transmission issues **← 정답**
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250687_2
- `C22`: Adjust the azimuth of 3235651_1 by 8 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.614 | MS1 | 121.4656672753 | 31.1446357047 | 42 | 504990 | -90.81 | 12.09 | 551.12 | 0.14 | 2.51 | 1585 |
| 2024-09-20 22:21:32.633 | MS1 | 121.4656673149 | 31.1446207902 | 42 | 504990 | -86.11 | 15.94 | 333.24 | 0.10 | 2.04 | 1564 |
| 2024-09-20 22:21:33.253 | MS1 | 121.4656702315 | 31.1446188290 | 42 | 504990 | -91.09 | 16.14 | 604.88 | 0.01 | 2.10 | 1592 |
| 2024-09-20 22:21:34.498 | MS1 | 121.4656690953 | 31.1446242881 | 42 | 504990 | -87.84 | 14.68 | 70.73 | 0.00 | 2.16 | 464 |
| 2024-09-20 22:21:35.279 | MS1 | 121.4656600403 | 31.1446279692 | 42 | 504990 | -86.99 | 17.51 | 88.57 | 0.10 | 2.54 | 365 |
| 2024-09-20 22:21:36.616 | MS1 | 121.4656697117 | 31.1446222964 | 42 | 504990 | -86.46 | 15.90 | 82.17 | 0.05 | 2.73 | 345 |
| 2024-09-20 22:21:37.668 | MS1 | 121.4656604590 | 31.1446276177 | 42 | 504990 | -91.12 | 12.38 | 45.23 | 0.16 | 2.62 | 322 |
| 2024-09-20 22:21:38.906 | MS1 | 121.4656594921 | 31.1446277047 | 42 | 504990 | -91.33 | 12.70 | 63.28 | 0.00 | 2.34 | 318 |
| 2024-09-20 22:21:39.408 | MS1 | 121.4656585295 | 31.1446352190 | 42 | 504990 | -89.45 | 7.88 | 93.16 | 0.15 | 2.77 | 498 |
| 2024-09-20 22:21:40.312 | MS1 | 121.4656673332 | 31.1446369701 | 42 | 504990 | -93.05 | 12.35 | 376.54 | 0.06 | 2.23 | 1569 |
| 2024-09-20 22:21:41.194 | MS1 | 121.4656663875 | 31.1446270401 | 42 | 504990 | -92.82 | 9.77 | 441.90 | 0.00 | 2.10 | 1586 |
| 2024-09-20 22:21:42.709 | MS1 | 121.4656644051 | 31.1446220585 | 42 | 504990 | -92.26 | 10.61 | 468.82 | 0.09 | 2.43 | 1572 |

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
| 3214113 | 4 | 121.4731623577 | 31.1444963531 | 284 | 9 | 7 | 37.5 | TDD | 197 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3235651 | 1 | 121.4648947430 | 31.1544654390 | 184 | 14 | 12 | 41.2 | TDD | 42 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3250687 | 2 | 121.4697353324 | 31.1537768793 | 31 | 7 | 1 | 42.0 | TDD | 371 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3273212 | 3 | 121.4643038988 | 31.1512913736 | 291 | 3 | 8 | 41.9 | TDD | 570 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.953 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.972 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.114 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.114 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.795 | NREventA3 | measId:2;ServCellPCI:815;Se... |
| 2024-09-20 22:21:38.035 | NRHandoverAttempt | SourcePCI:815;SourceNR-ARFC... |
| 2024-09-20 22:21:38.079 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.089 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.239 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.239 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235651 | 1 | 7.9756 | 5.8076 | -114.2490 | 10.8927 | 150.6028 | 0.0104 | 0.0033 |
| 2024_09_20 22:00 | 3250687 | 2 | 16.5952 | 16.8610 | -116.7609 | 9.5551 | 80.5042 | 0.0144 | 0.0100 |
| 2024_09_20 22:00 | 3273212 | 3 | 13.1802 | 9.0236 | -117.5292 | 11.4322 | 87.4680 | 0.0108 | 0.0180 |
| 2024_09_20 22:00 | 3214113 | 4 | 7.8167 | 13.5864 | -117.3782 | 11.7630 | 184.5686 | 0.0030 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415020_91FDBFB6 | 504990 | 42 | -88.3 | 504990 | 371 | -88.9 | 504990 | 197 | -103.0 | 504990 | 570 |
| MR_1774415020_F03BAEF4 | 504990 | 42 | -87.2 | 504990 | 371 | -90.0 | 504990 | 197 | -101.9 | 504990 | 570 |
| MR_1774415020_DEA2DC4F | 504990 | 42 | -87.0 | 504990 | 371 | -88.7 | 504990 | 197 | -101.5 | 504990 | 570 |
| MR_1774415020_79B8C8BE | 504990 | 42 | -86.1 | 504990 | 371 | -92.6 | 504990 | 197 | -101.1 | 504990 | 570 |
| MR_1774415020_75369B2C | 504990 | 42 | -87.3 | 504990 | 371 | -89.8 | 504990 | 197 | -102.5 | 504990 | 570 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1669: `9ab45ed2-be7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9ab45ed2-be77-4eb5-8e7f-5b0735a75453` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Add neighbor relationship between 3244679_2 and 3227950_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1669] topology](images/train_1669.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3227950_1 by 5 degrees
- `C2`: Add neighbor relationship between 3269932_4 and 3227950_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244679_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227950_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244679_2
- `C6`: Increase transmission power for 3227950_1
- `C7`: Increase transmission power for 3244679_2
- `C8`: Decrease A3 Offset threshold for 3244679_2
- `C9`: Decrease A3 Offset threshold for 3227950_1
- `C10`: Decrease transmission power for 3227950_1
- `C11`: Lift the tilt angle  of 3227950_1 by 4 degrees
- `C12`: Increase A3 Offset threshold for 3244679_2
- `C13`: Press down the tilt angle of 3244679_2 by 10 degrees
- `C14`: Adjust the azimuth of 3244679_2 by 50 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Press down the tilt angle  of 3227950_1 by 4 degrees
- `C17`: Check test server and transmission issues
- `C18`: Lift the tilt angle of 3244679_2 by 10 degrees
- `C19`: Add neighbor relationship between 3244679_2 and 3227950_1 **← 정답**
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227950_1
- `C21`: Increase A3 Offset threshold for 3227950_1
- `C22`: Decrease transmission power for 3244679_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.415 | MS1 | 121.4656586197 | 31.1446246688 | 267 | 504990 | -83.01 | 15.57 | 587.70 | 0.07 | 2.07 | 1578 |
| 2024-09-20 22:21:32.733 | MS1 | 121.4656693680 | 31.1446375110 | 267 | 504990 | -75.77 | 13.05 | 481.48 | 0.01 | 2.51 | 1567 |
| 2024-09-20 22:21:33.979 | MS1 | 121.4656651467 | 31.1446265091 | 267 | 504990 | -79.04 | 16.16 | 597.92 | 0.12 | 2.24 | 1571 |
| 2024-09-20 22:21:34.172 | MS1 | 121.4656675531 | 31.1446219159 | 267 | 504990 | -93.71 | -0.72 | 44.45 | 0.06 | 1.35 | 1595 |
| 2024-09-20 22:21:35.804 | MS1 | 121.4656661976 | 31.1446333010 | 267 | 504990 | -91.62 | -0.61 | 68.82 | 0.14 | 1.03 | 1584 |
| 2024-09-20 22:21:36.547 | MS1 | 121.4656718804 | 31.1446198847 | 267 | 504990 | -93.89 | -3.90 | 28.02 | 0.14 | 1.06 | 1588 |
| 2024-09-20 22:21:37.156 | MS1 | 121.4656615639 | 31.1446253237 | 267 | 504990 | -87.60 | -1.86 | 72.32 | 0.00 | 1.44 | 1579 |
| 2024-09-20 22:21:38.707 | MS1 | 121.4656717983 | 31.1446232747 | 267 | 504990 | -79.96 | 14.98 | 474.70 | 0.06 | 1.33 | 1563 |
| 2024-09-20 22:21:39.535 | MS1 | 121.4656649534 | 31.1446227223 | 267 | 504990 | -79.64 | 14.20 | 365.86 | 0.15 | 1.41 | 1575 |
| 2024-09-20 22:21:40.804 | MS1 | 121.4656592508 | 31.1446233979 | 267 | 504990 | -78.58 | 16.80 | 526.10 | 0.14 | 3.00 | 1585 |
| 2024-09-20 22:21:41.209 | MS1 | 121.4656595705 | 31.1446297427 | 267 | 504990 | -82.52 | 13.52 | 451.80 | 0.12 | 2.73 | 1581 |
| 2024-09-20 22:21:42.850 | MS1 | 121.4656692502 | 31.1446288056 | 267 | 504990 | -79.42 | 15.94 | 549.21 | 0.17 | 2.97 | 1573 |

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
| 3227950 | 1 | 121.4715512220 | 31.1537176938 | 214 | 2 | 10 | 35.8 | TDD | 47 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3244679 | 2 | 121.4662695540 | 31.1510918788 | 236 | 13 | 10 | 40.5 | TDD | 267 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3257032 | 3 | 121.4685209444 | 31.1442038403 | 95 | 10 | 11 | 48.6 | TDD | 285 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3269932 | 4 | 121.4692846031 | 31.1498507914 | 262 | 0 | 0 | 47.9 | TDD | 933 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.709 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.725 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:30.874 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.874 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.600 | NREventA3 | measId:2;ServCellPCI:414;Se... |
| 2024-09-20 22:21:35.600 | NREventA3 | measId:2;ServCellPCI:414;Se... |
| 2024-09-20 22:21:36.600 | NREventA3 | measId:2;ServCellPCI:414;Se... |
| 2024-09-20 22:21:39.100 | NRRRCReestablishAttempt | PCI:414 |
| 2024-09-20 22:21:39.117 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.130 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.277 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.277 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227950 | 1 | 11.6848 | 19.5125 | -115.2728 | 19.7647 | 117.5227 | 0.0004 | 0.0030 |
| 2024_09_20 22:00 | 3244679 | 2 | 7.3669 | 14.4795 | -114.9758 | 13.4940 | 84.9513 | 0.0068 | 0.1792 |
| 2024_09_20 22:00 | 3257032 | 3 | 14.7819 | 13.9773 | -117.6624 | 18.8085 | 182.3999 | 0.0092 | 0.0082 |
| 2024_09_20 22:00 | 3269932 | 4 | 16.5727 | 10.1357 | -117.0152 | 9.4814 | 109.7700 | 0.0066 | 0.0102 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415108_936AF489 | 504990 | 267 | -95.7 | 504990 | 47 | -88.7 | 504990 | 933 | -90.9 | 504990 | 285 |
| MR_1774415108_6BB5767C | 504990 | 267 | -94.4 | 504990 | 47 | -87.5 | 504990 | 933 | -92.5 | 504990 | 285 |
| MR_1774415108_3793375A | 504990 | 47 | -89.6 | 504990 | 267 | -93.0 | 504990 | 933 | -91.2 | 504990 | 285 |
| MR_1774415108_1A84162B | 504990 | 267 | -92.3 | 504990 | 47 | -89.1 | 504990 | 933 | -91.9 | 504990 | 285 |
| MR_1774415108_61787D04 | 504990 | 47 | -87.3 | 504990 | 267 | -94.0 | 504990 | 933 | -90.4 | 504990 | 285 |
| MR_1774415108_971F7C10 | 504990 | 267 | -92.7 | 504990 | 47 | -89.8 | 504990 | 933 | -90.1 | 504990 | 285 |
| MR_1774415108_ADCA94FF | 504990 | 267 | -93.9 | 504990 | 47 | -88.4 | 504990 | 933 | -91.1 | 504990 | 285 |
| MR_1774415108_A7690B58 | 504990 | 267 | -93.7 | 504990 | 47 | -90.6 | 504990 | 933 | -91.9 | 504990 | 285 |

> *... 2개 열 생략 (전체 14열)*

---
