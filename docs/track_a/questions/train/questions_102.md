# Track A 문제 분석 — train[1010]~train[1019]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1010] ~ train[1019] (10개)

## 목차

1. [문제 1010: `dd5f2bfd-8a2...`](#1010) — single-answer, 정답: C14
2. [문제 1011: `875c67db-401...`](#1011) — single-answer, 정답: C7
3. [문제 1012: `137c3dc7-dd9...`](#1012) — single-answer, 정답: C17
4. [문제 1013: `a8a8977f-ef0...`](#1013) — single-answer, 정답: C3
5. [문제 1014: `7f473b8c-46b...`](#1014) — single-answer, 정답: C13
6. [문제 1015: `5f76f81d-29d...`](#1015) — multiple-answer, 정답: C4|C9
7. [문제 1016: `76c5fa75-50a...`](#1016) — single-answer, 정답: C20
8. [문제 1017: `2d6423e1-649...`](#1017) — single-answer, 정답: C19
9. [문제 1018: `f9c240bc-b09...`](#1018) — single-answer, 정답: C12
10. [문제 1019: `d10d0af6-004...`](#1019) — single-answer, 정답: C14

---

### 문제 1010: `dd5f2bfd-8a2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dd5f2bfd-8a2e-4192-a491-1cea3f025e8d` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Add neighbor relationship between 3254940_1 and 3233859_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1010] topology](images/train_1010.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3233859_4
- `C2`: Adjust the azimuth of 3233859_4 by 16 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254940_1
- `C4`: Increase transmission power for 3254940_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease A3 Offset threshold for 3233859_4
- `C7`: Press down the tilt angle of 3254940_1 by 6 degrees
- `C8`: Increase transmission power for 3233859_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254940_1
- `C10`: Increase A3 Offset threshold for 3233859_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233859_4
- `C12`: Increase A3 Offset threshold for 3254940_1
- `C13`: Lift the tilt angle of 3254940_1 by 6 degrees
- `C14`: Add neighbor relationship between 3254940_1 and 3233859_4 **← 정답**
- `C15`: Lift the tilt angle  of 3233859_4 by 2 degrees
- `C16`: Decrease transmission power for 3254940_1
- `C17`: Press down the tilt angle  of 3233859_4 by 2 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233859_4
- `C19`: Adjust the azimuth of 3254940_1 by 34 degrees
- `C20`: Decrease A3 Offset threshold for 3254940_1
- `C21`: Check test server and transmission issues
- `C22`: Add neighbor relationship between 3270370_2 and 3233859_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.745 | MS1 | 121.4656601854 | 31.1446248866 | 216 | 504990 | -75.80 | 13.38 | 524.45 | 0.14 | 2.68 | 1589 |
| 2024-09-20 22:21:32.905 | MS1 | 121.4656631512 | 31.1446301957 | 216 | 504990 | -81.79 | 16.94 | 370.81 | 0.16 | 2.40 | 1568 |
| 2024-09-20 22:21:33.160 | MS1 | 121.4656595960 | 31.1446365952 | 216 | 504990 | -84.60 | 17.33 | 479.95 | 0.09 | 2.33 | 1560 |
| 2024-09-20 22:21:34.359 | MS1 | 121.4656595078 | 31.1446185632 | 216 | 504990 | -85.99 | -1.01 | 72.23 | 0.03 | 1.43 | 1583 |
| 2024-09-20 22:21:35.849 | MS1 | 121.4656724262 | 31.1446367291 | 216 | 504990 | -94.57 | -3.74 | 71.68 | 0.08 | 1.41 | 1591 |
| 2024-09-20 22:21:36.563 | MS1 | 121.4656604415 | 31.1446213935 | 216 | 504990 | -87.06 | -2.42 | 32.91 | 0.15 | 1.47 | 1577 |
| 2024-09-20 22:21:37.585 | MS1 | 121.4656602417 | 31.1446375088 | 216 | 504990 | -87.72 | -1.53 | 71.80 | 0.14 | 1.35 | 1576 |
| 2024-09-20 22:21:38.879 | MS1 | 121.4656771290 | 31.1446235793 | 216 | 504990 | -79.82 | 12.14 | 361.59 | 0.07 | 1.48 | 1590 |
| 2024-09-20 22:21:39.679 | MS1 | 121.4656775078 | 31.1446329555 | 216 | 504990 | -79.60 | 13.14 | 435.74 | 0.10 | 1.06 | 1561 |
| 2024-09-20 22:21:40.770 | MS1 | 121.4656633984 | 31.1446367609 | 216 | 504990 | -76.02 | 12.52 | 488.11 | 0.15 | 2.66 | 1598 |
| 2024-09-20 22:21:41.985 | MS1 | 121.4656720158 | 31.1446199359 | 216 | 504990 | -83.83 | 12.90 | 571.54 | 0.14 | 2.72 | 1560 |
| 2024-09-20 22:21:42.451 | MS1 | 121.4656771852 | 31.1446321088 | 216 | 504990 | -78.65 | 14.14 | 400.91 | 0.14 | 2.91 | 1590 |

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
| 3233859 | 4 | 121.4749984112 | 31.1551104271 | 233 | 1 | 1 | 23.4 | TDD | 855 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3243216 | 3 | 121.4735472324 | 31.1525474549 | 282 | 4 | 2 | 21.5 | TDD | 756 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3254940 | 1 | 121.4742872311 | 31.1457364907 | 295 | 3 | 7 | 47.1 | TDD | 216 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3270370 | 2 | 121.4658635731 | 31.1498563488 | 174 | 6 | 8 | 27.2 | TDD | 626 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.249 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.379 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.379 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.081 | NREventA3 | measId:2;ServCellPCI:960;Se... |
| 2024-09-20 22:21:36.081 | NREventA3 | measId:2;ServCellPCI:960;Se... |
| 2024-09-20 22:21:37.081 | NREventA3 | measId:2;ServCellPCI:960;Se... |
| 2024-09-20 22:21:39.581 | NRRRCReestablishAttempt | PCI:960 |
| 2024-09-20 22:21:39.593 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.605 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.740 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.740 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254940 | 1 | 12.8252 | 13.6832 | -114.0149 | 18.0419 | 175.4321 | 0.0161 | 0.1989 |
| 2024_09_20 22:00 | 3270370 | 2 | 8.8574 | 10.9780 | -114.0650 | 11.4106 | 144.1611 | 0.0190 | 0.0111 |
| 2024_09_20 22:00 | 3243216 | 3 | 13.5749 | 16.5572 | -114.3378 | 19.3454 | 166.6741 | 0.0003 | 0.0144 |
| 2024_09_20 22:00 | 3233859 | 4 | 15.6281 | 8.0417 | -116.8628 | 11.3700 | 117.2603 | 0.0087 | 0.0000 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417182_49E9C855 | 504990 | 216 | -86.9 | 504990 | 855 | -82.1 | 504990 | 626 | -81.2 | 504990 | 756 |
| MR_1774417182_EB64BC5E | 504990 | 855 | -82.6 | 504990 | 216 | -86.4 | 504990 | 626 | -81.6 | 504990 | 756 |
| MR_1774417182_9282D473 | 504990 | 216 | -87.6 | 504990 | 855 | -80.5 | 504990 | 626 | -81.0 | 504990 | 756 |
| MR_1774417182_2E742E83 | 504990 | 855 | -80.8 | 504990 | 216 | -84.7 | 504990 | 626 | -80.8 | 504990 | 756 |
| MR_1774417182_915458D9 | 504990 | 216 | -85.6 | 504990 | 855 | -83.3 | 504990 | 626 | -80.6 | 504990 | 756 |
| MR_1774417182_43404413 | 504990 | 216 | -87.0 | 504990 | 855 | -82.8 | 504990 | 626 | -81.7 | 504990 | 756 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1011: `875c67db-401...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `875c67db-4010-4c1e-bac2-90dd74db44ae` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3216043_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1011] topology](images/train_1011.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3216043_2
- `C2`: Check test server and transmission issues
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246463_3
- `C4`: Increase A3 Offset threshold for 3216043_2
- `C5`: Decrease transmission power for 3216043_2
- `C6`: Add neighbor relationship between 3229452_4 and 3246463_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216043_2 **← 정답**
- `C8`: Press down the tilt angle  of 3246463_3 by 6 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216043_2
- `C10`: Adjust the azimuth of 3216043_2 by 3 degrees
- `C11`: Decrease transmission power for 3246463_3
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Add neighbor relationship between 3216043_2 and 3246463_3
- `C14`: Decrease A3 Offset threshold for 3246463_3
- `C15`: Lift the tilt angle of 3216043_2 by 4 degrees
- `C16`: Lift the tilt angle  of 3246463_3 by 6 degrees
- `C17`: Decrease A3 Offset threshold for 3216043_2
- `C18`: Increase A3 Offset threshold for 3246463_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246463_3
- `C20`: Press down the tilt angle of 3216043_2 by 4 degrees
- `C21`: Adjust the azimuth of 3246463_3 by 45 degrees
- `C22`: Increase transmission power for 3246463_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.707 | MS1 | 121.4656758679 | 31.1446273120 | 764 | 504990 | -88.72 | 17.95 | 595.78 | 0.01 | 2.07 | 1574 |
| 2024-09-20 22:21:32.582 | MS1 | 121.4656758891 | 31.1446317862 | 764 | 504990 | -89.16 | 13.07 | 416.17 | 0.17 | 2.83 | 1593 |
| 2024-09-20 22:21:33.212 | MS1 | 121.4656763596 | 31.1446330026 | 764 | 504990 | -85.91 | 12.01 | 364.07 | 0.08 | 2.43 | 1576 |
| 2024-09-20 22:21:34.664 | MS1 | 121.4656672892 | 31.1446309412 | 764 | 504990 | -88.00 | 13.22 | 82.43 | 0.61 | 2.49 | 597 |
| 2024-09-20 22:21:35.631 | MS1 | 121.4656699625 | 31.1446311468 | 764 | 504990 | -89.93 | 14.46 | 68.10 | 0.69 | 2.51 | 583 |
| 2024-09-20 22:21:36.922 | MS1 | 121.4656717304 | 31.1446371591 | 764 | 504990 | -87.04 | 17.74 | 60.06 | 0.68 | 2.67 | 517 |
| 2024-09-20 22:21:37.783 | MS1 | 121.4656698982 | 31.1446340407 | 764 | 504990 | -93.40 | 9.00 | 79.50 | 0.63 | 2.16 | 671 |
| 2024-09-20 22:21:38.668 | MS1 | 121.4656712037 | 31.1446356122 | 764 | 504990 | -89.44 | 8.95 | 80.48 | 0.64 | 2.02 | 569 |
| 2024-09-20 22:21:39.699 | MS1 | 121.4656659334 | 31.1446202335 | 764 | 504990 | -89.07 | 10.73 | 60.94 | 0.65 | 2.78 | 526 |
| 2024-09-20 22:21:40.872 | MS1 | 121.4656602619 | 31.1446322484 | 764 | 504990 | -93.05 | 11.74 | 530.93 | 0.17 | 2.63 | 1593 |
| 2024-09-20 22:21:41.341 | MS1 | 121.4656587719 | 31.1446251798 | 764 | 504990 | -90.55 | 9.10 | 504.32 | 0.18 | 2.24 | 1594 |
| 2024-09-20 22:21:42.867 | MS1 | 121.4656611911 | 31.1446358359 | 764 | 504990 | -89.37 | 9.99 | 393.75 | 0.03 | 2.29 | 1592 |

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
| 3216043 | 2 | 121.4722780682 | 31.1449540069 | 270 | 0 | 7 | 41.0 | TDD | 764 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3229452 | 4 | 121.4718882198 | 31.1496174697 | 311 | 3 | 1 | 39.9 | TDD | 103 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3242169 | 1 | 121.4649174869 | 31.1488601629 | 332 | 1 | 2 | 17.8 | TDD | 83 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3246463 | 3 | 121.4716127160 | 31.1524023332 | 168 | 5 | 4 | 20.2 | TDD | 375 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.229 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.360 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.360 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.046 | NREventA3 | measId:2;ServCellPCI:956;Se... |
| 2024-09-20 22:21:38.286 | NRHandoverAttempt | SourcePCI:956;SourceNR-ARFC... |
| 2024-09-20 22:21:38.329 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.341 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.457 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.457 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242169 | 1 | 7.1242 | 14.5415 | -114.1389 | 13.6641 | 146.2831 | 0.0167 | 0.0104 |
| 2024_09_20 22:00 | 3216043 | 2 | 18.0756 | 19.4504 | -117.9193 | 12.0411 | 115.9264 | 0.0082 | 0.0019 |
| 2024_09_20 22:00 | 3246463 | 3 | 9.7029 | 11.9974 | -114.8879 | 10.0552 | 154.7922 | 0.0069 | 0.0050 |
| 2024_09_20 22:00 | 3229452 | 4 | 9.1977 | 8.3151 | -114.5531 | 15.7069 | 192.2602 | 0.0082 | 0.0143 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415233_B2F79CCB | 504990 | 764 | -88.9 | 504990 | 375 | -93.3 | 504990 | 103 | -100.4 | 504990 | 83 |
| MR_1774415233_DDEDFA38 | 504990 | 764 | -86.9 | 504990 | 375 | -92.4 | 504990 | 103 | -100.6 | 504990 | 83 |
| MR_1774415233_EA194D17 | 504990 | 764 | -87.2 | 504990 | 375 | -93.0 | 504990 | 103 | -98.1 | 504990 | 83 |
| MR_1774415233_67ACA0FC | 504990 | 764 | -87.0 | 504990 | 375 | -94.0 | 504990 | 103 | -100.9 | 504990 | 83 |
| MR_1774415233_E190D84E | 504990 | 764 | -88.7 | 504990 | 375 | -92.4 | 504990 | 103 | -100.3 | 504990 | 83 |
| MR_1774415233_4B714028 | 504990 | 764 | -86.8 | 504990 | 375 | -93.2 | 504990 | 103 | -99.9 | 504990 | 83 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1012: `137c3dc7-dd9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `137c3dc7-dd91-46db-ad91-139b8e132aca` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1012] topology](images/train_1012.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3242953_2 by 3 degrees
- `C2`: Press down the tilt angle of 3242953_2 by 3 degrees
- `C3`: Decrease transmission power for 3218562_3
- `C4`: Increase A3 Offset threshold for 3242953_2
- `C5`: Increase transmission power for 3218562_3
- `C6`: Decrease A3 Offset threshold for 3242953_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242953_2
- `C8`: Check test server and transmission issues
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218562_3
- `C10`: Press down the tilt angle  of 3218562_3 by 10 degrees
- `C11`: Add neighbor relationship between 3211269_1 and 3218562_3
- `C12`: Adjust the azimuth of 3242953_2 by 50 degrees
- `C13`: Add neighbor relationship between 3242953_2 and 3218562_3
- `C14`: Decrease transmission power for 3242953_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218562_3
- `C16`: Adjust the azimuth of 3218562_3 by 50 degrees
- `C17`: Insufficient data; more data is needed for judgment. **← 정답**
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242953_2
- `C19`: Increase A3 Offset threshold for 3218562_3
- `C20`: Decrease A3 Offset threshold for 3218562_3
- `C21`: Increase transmission power for 3242953_2
- `C22`: Lift the tilt angle  of 3218562_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.822 | MS1 | 121.4656609817 | 31.1446339311 | 388 | 504990 | -90.55 | 12.08 | 515.33 | 0.19 | 2.64 | 1571 |
| 2024-09-20 22:21:32.677 | MS1 | 121.4656676741 | 31.1446270719 | 388 | 504990 | -89.41 | 13.21 | 526.33 | 0.09 | 2.14 | 1586 |
| 2024-09-20 22:21:33.736 | MS1 | 121.4656623484 | 31.1446345326 | 388 | 504990 | -89.76 | 13.08 | 481.20 | 0.11 | 2.98 | 1599 |
| 2024-09-20 22:21:34.477 | MS1 | 121.4656673435 | 31.1446369870 | 388 | 504990 | -86.93 | 17.45 | 84.33 | 0.03 | 2.26 | 1579 |
| 2024-09-20 22:21:35.862 | MS1 | 121.4656679762 | 31.1446279413 | 388 | 504990 | -85.41 | 17.75 | 100.05 | 0.08 | 2.55 | 1600 |
| 2024-09-20 22:21:36.550 | MS1 | 121.4656763055 | 31.1446236710 | 388 | 504990 | -88.13 | 12.07 | 74.97 | 0.02 | 2.52 | 1595 |
| 2024-09-20 22:21:37.635 | MS1 | 121.4656728872 | 31.1446375400 | 388 | 504990 | -91.76 | 11.50 | 86.19 | 0.13 | 2.26 | 1571 |
| 2024-09-20 22:21:38.937 | MS1 | 121.4656724139 | 31.1446232976 | 388 | 504990 | -90.71 | 11.19 | 78.74 | 0.05 | 2.46 | 1592 |
| 2024-09-20 22:21:39.546 | MS1 | 121.4656636109 | 31.1446187425 | 388 | 504990 | -92.20 | 12.51 | 75.48 | 0.08 | 2.08 | 1590 |
| 2024-09-20 22:21:40.724 | MS1 | 121.4656623532 | 31.1446330924 | 388 | 504990 | -89.10 | 9.77 | 394.63 | 0.12 | 2.11 | 1586 |
| 2024-09-20 22:21:41.653 | MS1 | 121.4656648631 | 31.1446354838 | 388 | 504990 | -92.27 | 12.99 | 327.95 | 0.11 | 2.24 | 1573 |
| 2024-09-20 22:21:42.158 | MS1 | 121.4656686338 | 31.1446269533 | 388 | 504990 | -91.03 | 9.76 | 397.64 | 0.05 | 2.31 | 1583 |

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
| 3211269 | 1 | 121.4758694188 | 31.1556649655 | 52 | 10 | 3 | 24.8 | TDD | 275 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3218562 | 3 | 121.4689952703 | 31.1482059439 | 160 | 14 | 7 | 30.3 | TDD | 341 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3235008 | 4 | 121.4707991244 | 31.1487768425 | 61 | 3 | 10 | 24.8 | TDD | 159 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3242953 | 2 | 121.4696995289 | 31.1538684578 | 115 | 2 | 9 | 20.9 | TDD | 388 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.604 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.619 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.753 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.753 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.408 | NREventA3 | measId:2;ServCellPCI:298;Se... |
| 2024-09-20 22:21:38.648 | NRHandoverAttempt | SourcePCI:298;SourceNR-ARFC... |
| 2024-09-20 22:21:38.679 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.691 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.812 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.812 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3211269 | 1 | 86.8867 | 76.9019 | -116.0523 | 8.6293 | 195.3205 | 0.0147 | 0.0098 |
| 2024_09_19 22:00 | 3242953 | 2 | 91.5546 | 84.6809 | -117.3304 | 7.6873 | 126.1110 | 0.0153 | 0.0195 |
| 2024_09_19 22:00 | 3218562 | 3 | 87.4956 | 78.6580 | -115.8946 | 18.4066 | 171.8095 | 0.0106 | 0.0144 |
| 2024_09_19 22:00 | 3235008 | 4 | 83.4297 | 93.9792 | -116.5839 | 8.6912 | 163.4512 | 0.0103 | 0.0148 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413331_D66218C9 | 504990 | 388 | -86.4 | 504990 | 341 | -92.6 | 504990 | 275 | -94.6 | 504990 | 159 |
| MR_1774413331_193C139C | 504990 | 388 | -88.2 | 504990 | 341 | -93.5 | 504990 | 275 | -96.3 | 504990 | 159 |
| MR_1774413331_4171EE39 | 504990 | 388 | -86.3 | 504990 | 341 | -95.3 | 504990 | 275 | -93.7 | 504990 | 159 |
| MR_1774413331_28528362 | 504990 | 388 | -85.6 | 504990 | 341 | -93.7 | 504990 | 275 | -93.8 | 504990 | 159 |
| MR_1774413331_C1854980 | 504990 | 388 | -86.3 | 504990 | 341 | -92.0 | 504990 | 275 | -97.5 | 504990 | 159 |
| MR_1774413331_1FCF90CE | 504990 | 388 | -85.8 | 504990 | 341 | -91.7 | 504990 | 275 | -93.9 | 504990 | 159 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1013: `a8a8977f-ef0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a8a8977f-ef05-41f5-8d09-5a4fddde6523` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1013] topology](images/train_1013.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3237350_4 by 10 degrees
- `C2`: Add neighbor relationship between 3251067_1 and 3237350_4
- `C3`: Insufficient data; more data is needed for judgment. **← 정답**
- `C4`: Add neighbor relationship between 3216945_3 and 3237350_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237350_4
- `C6`: Increase A3 Offset threshold for 3237350_4
- `C7`: Increase transmission power for 3251067_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251067_1
- `C9`: Adjust the azimuth of 3237350_4 by 21 degrees
- `C10`: Increase A3 Offset threshold for 3251067_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251067_1
- `C12`: Decrease A3 Offset threshold for 3237350_4
- `C13`: Decrease transmission power for 3251067_1
- `C14`: Press down the tilt angle of 3251067_1 by 6 degrees
- `C15`: Check test server and transmission issues
- `C16`: Adjust the azimuth of 3251067_1 by 50 degrees
- `C17`: Lift the tilt angle of 3251067_1 by 6 degrees
- `C18`: Increase transmission power for 3237350_4
- `C19`: Decrease transmission power for 3237350_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237350_4
- `C21`: Decrease A3 Offset threshold for 3251067_1
- `C22`: Lift the tilt angle  of 3237350_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.854 | MS1 | 121.4656597985 | 31.1446201645 | 720 | 504990 | -91.16 | 15.47 | 353.54 | 0.17 | 2.24 | 1592 |
| 2024-09-20 22:21:32.444 | MS1 | 121.4656651083 | 31.1446328844 | 720 | 504990 | -91.81 | 13.43 | 512.41 | 0.12 | 2.56 | 1585 |
| 2024-09-20 22:21:33.838 | MS1 | 121.4656690371 | 31.1446314000 | 720 | 504990 | -91.19 | 12.51 | 575.56 | 0.16 | 2.46 | 1595 |
| 2024-09-20 22:21:34.544 | MS1 | 121.4656766158 | 31.1446346515 | 720 | 504990 | -88.56 | 13.05 | 88.87 | 0.03 | 2.67 | 1585 |
| 2024-09-20 22:21:35.390 | MS1 | 121.4656680251 | 31.1446202073 | 720 | 504990 | -88.08 | 13.21 | 54.03 | 0.10 | 2.18 | 1595 |
| 2024-09-20 22:21:36.406 | MS1 | 121.4656697136 | 31.1446203622 | 720 | 504990 | -89.04 | 17.91 | 63.62 | 0.12 | 2.45 | 1592 |
| 2024-09-20 22:21:37.951 | MS1 | 121.4656610151 | 31.1446254179 | 720 | 504990 | -89.25 | 8.09 | 98.63 | 0.10 | 2.76 | 1596 |
| 2024-09-20 22:21:38.443 | MS1 | 121.4656656956 | 31.1446268454 | 720 | 504990 | -93.99 | 12.11 | 58.18 | 0.18 | 2.98 | 1570 |
| 2024-09-20 22:21:39.965 | MS1 | 121.4656731841 | 31.1446327782 | 720 | 504990 | -92.38 | 8.81 | 74.62 | 0.15 | 2.45 | 1583 |
| 2024-09-20 22:21:40.759 | MS1 | 121.4656775009 | 31.1446321049 | 720 | 504990 | -91.35 | 8.61 | 553.42 | 0.19 | 2.41 | 1587 |
| 2024-09-20 22:21:41.818 | MS1 | 121.4656694043 | 31.1446181698 | 720 | 504990 | -90.97 | 8.23 | 305.76 | 0.09 | 2.33 | 1564 |
| 2024-09-20 22:21:42.952 | MS1 | 121.4656651173 | 31.1446259860 | 720 | 504990 | -91.79 | 11.58 | 518.49 | 0.14 | 2.85 | 1590 |

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
| 3216945 | 3 | 121.4681624055 | 31.1536892608 | 246 | 15 | 10 | 47.4 | TDD | 974 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3229014 | 2 | 121.4743871766 | 31.1489123346 | 105 | 2 | 5 | 49.6 | TDD | 93 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3237350 | 4 | 121.4692470041 | 31.1486828972 | 196 | 10 | 2 | 46.5 | TDD | 143 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3251067 | 1 | 121.4676023356 | 31.1519114699 | 14 | 4 | 9 | 23.4 | TDD | 720 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.491 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.515 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.664 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.664 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.375 | NREventA3 | measId:2;ServCellPCI:344;Se... |
| 2024-09-20 22:21:38.615 | NRHandoverAttempt | SourcePCI:344;SourceNR-ARFC... |
| 2024-09-20 22:21:38.654 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.664 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.811 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.811 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3251067 | 1 | 90.1981 | 94.0134 | -117.3002 | 18.5221 | 95.9373 | 0.0146 | 0.0112 |
| 2024_09_19 22:00 | 3229014 | 2 | 93.6124 | 85.4604 | -115.5572 | 12.8748 | 163.0320 | 0.0182 | 0.0184 |
| 2024_09_19 22:00 | 3216945 | 3 | 80.8787 | 92.7730 | -117.7249 | 13.8053 | 103.5901 | 0.0075 | 0.0013 |
| 2024_09_19 22:00 | 3237350 | 4 | 94.6039 | 94.5136 | -115.4093 | 17.5128 | 141.6898 | 0.0136 | 0.0079 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413193_2FE63E67 | 504990 | 720 | -89.7 | 504990 | 143 | -95.1 | 504990 | 974 | -95.7 | 504990 | 93 |
| MR_1774413193_D742FB15 | 504990 | 720 | -90.2 | 504990 | 143 | -98.5 | 504990 | 974 | -96.9 | 504990 | 93 |
| MR_1774413193_DF9AA67B | 504990 | 720 | -86.7 | 504990 | 143 | -97.0 | 504990 | 974 | -95.5 | 504990 | 93 |
| MR_1774413193_3C85D38B | 504990 | 720 | -88.9 | 504990 | 143 | -94.8 | 504990 | 974 | -97.5 | 504990 | 93 |
| MR_1774413193_E93082E2 | 504990 | 720 | -88.9 | 504990 | 143 | -97.5 | 504990 | 974 | -98.2 | 504990 | 93 |
| MR_1774413193_B3BBE287 | 504990 | 720 | -86.6 | 504990 | 143 | -97.3 | 504990 | 974 | -98.4 | 504990 | 93 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1014: `7f473b8c-46b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7f473b8c-46bb-47ae-88cf-932ea52f1f56` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1014] topology](images/train_1014.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3260405_3
- `C2`: Increase transmission power for 3260405_3
- `C3`: Lift the tilt angle of 3260405_3 by 10 degrees
- `C4`: Add neighbor relationship between 3260405_3 and 3223834_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223834_4
- `C6`: Check test server and transmission issues
- `C7`: Adjust the azimuth of 3223834_4 by 50 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260405_3
- `C9`: Increase A3 Offset threshold for 3260405_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260405_3
- `C11`: Decrease transmission power for 3260405_3
- `C12`: Add neighbor relationship between 3222939_1 and 3223834_4
- `C13`: Insufficient data; more data is needed for judgment. **← 정답**
- `C14`: Decrease A3 Offset threshold for 3223834_4
- `C15`: Increase transmission power for 3223834_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223834_4
- `C17`: Press down the tilt angle of 3260405_3 by 10 degrees
- `C18`: Press down the tilt angle  of 3223834_4 by 7 degrees
- `C19`: Increase A3 Offset threshold for 3223834_4
- `C20`: Adjust the azimuth of 3260405_3 by 50 degrees
- `C21`: Decrease transmission power for 3223834_4
- `C22`: Lift the tilt angle  of 3223834_4 by 7 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.210 | MS1 | 121.4656703020 | 31.1446232646 | 636 | 504990 | -85.32 | 14.12 | 568.08 | 0.13 | 2.06 | 1567 |
| 2024-09-20 22:21:32.639 | MS1 | 121.4656655467 | 31.1446248997 | 636 | 504990 | -85.44 | 15.26 | 309.48 | 0.18 | 2.81 | 1573 |
| 2024-09-20 22:21:33.234 | MS1 | 121.4656768823 | 31.1446319211 | 636 | 504990 | -89.32 | 12.66 | 365.52 | 0.01 | 2.34 | 1585 |
| 2024-09-20 22:21:34.394 | MS1 | 121.4656599646 | 31.1446205771 | 636 | 504990 | -91.96 | 15.93 | 73.29 | 0.10 | 2.45 | 1594 |
| 2024-09-20 22:21:35.496 | MS1 | 121.4656735444 | 31.1446191250 | 636 | 504990 | -86.36 | 13.58 | 87.56 | 0.00 | 2.26 | 1589 |
| 2024-09-20 22:21:36.597 | MS1 | 121.4656765145 | 31.1446205966 | 636 | 504990 | -89.39 | 12.23 | 68.87 | 0.19 | 2.93 | 1568 |
| 2024-09-20 22:21:37.725 | MS1 | 121.4656724449 | 31.1446368616 | 636 | 504990 | -90.13 | 11.64 | 65.25 | 0.00 | 2.51 | 1586 |
| 2024-09-20 22:21:38.480 | MS1 | 121.4656741762 | 31.1446340619 | 636 | 504990 | -92.89 | 10.46 | 74.27 | 0.06 | 2.67 | 1587 |
| 2024-09-20 22:21:39.961 | MS1 | 121.4656778641 | 31.1446233904 | 636 | 504990 | -90.08 | 11.95 | 67.82 | 0.00 | 2.66 | 1563 |
| 2024-09-20 22:21:40.192 | MS1 | 121.4656662487 | 31.1446333981 | 636 | 504990 | -91.27 | 12.04 | 450.63 | 0.19 | 2.33 | 1588 |
| 2024-09-20 22:21:41.465 | MS1 | 121.4656665027 | 31.1446277384 | 636 | 504990 | -92.99 | 8.30 | 492.22 | 0.06 | 2.55 | 1564 |
| 2024-09-20 22:21:42.583 | MS1 | 121.4656753055 | 31.1446310440 | 636 | 504990 | -90.02 | 12.03 | 402.42 | 0.02 | 2.24 | 1573 |

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
| 3213877 | 2 | 121.4710086255 | 31.1487082088 | 322 | 14 | 9 | 30.6 | TDD | 299 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3222939 | 1 | 121.4651448369 | 31.1553163593 | 40 | 11 | 11 | 50.0 | TDD | 851 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3223834 | 4 | 121.4719289912 | 31.1488865325 | 105 | 4 | 2 | 39.6 | TDD | 238 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3260405 | 3 | 121.4697442164 | 31.1556378887 | 284 | 9 | 8 | 35.4 | TDD | 636 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.579 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.598 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.728 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.728 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.417 | NREventA3 | measId:2;ServCellPCI:300;Se... |
| 2024-09-20 22:21:38.657 | NRHandoverAttempt | SourcePCI:300;SourceNR-ARFC... |
| 2024-09-20 22:21:38.704 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.714 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.833 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.833 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3222939 | 1 | 80.2195 | 76.3496 | -116.1923 | 6.3074 | 115.1406 | 0.0055 | 0.0105 |
| 2024_09_19 22:00 | 3213877 | 2 | 86.3507 | 81.5695 | -114.0167 | 14.1979 | 122.9161 | 0.0098 | 0.0157 |
| 2024_09_19 22:00 | 3260405 | 3 | 78.0584 | 87.8458 | -116.5671 | 18.0174 | 129.6730 | 0.0124 | 0.0033 |
| 2024_09_19 22:00 | 3223834 | 4 | 78.0452 | 81.5578 | -116.4039 | 15.4558 | 196.9677 | 0.0070 | 0.0122 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415661_3B277042 | 504990 | 636 | -91.4 | 504990 | 238 | -102.2 | 504990 | 851 | -100.0 | 504990 | 299 |
| MR_1774415661_74B65F99 | 504990 | 636 | -93.5 | 504990 | 238 | -102.1 | 504990 | 851 | -103.0 | 504990 | 299 |
| MR_1774415661_4F359359 | 504990 | 636 | -90.6 | 504990 | 238 | -100.7 | 504990 | 851 | -102.7 | 504990 | 299 |
| MR_1774415661_430CD579 | 504990 | 636 | -91.1 | 504990 | 238 | -101.1 | 504990 | 851 | -103.6 | 504990 | 299 |
| MR_1774415661_786C90B0 | 504990 | 636 | -91.3 | 504990 | 238 | -99.7 | 504990 | 851 | -103.6 | 504990 | 299 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1015: `5f76f81d-29d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5f76f81d-29dc-4748-a537-4ed7366d11a8` |
| Tag | **multiple-answer** |
| 정답 | **C4|C9** |
| C4 의미 | Adjust the azimuth of 3265327_3 by 50 degrees |
| C9 의미 | Increase transmission power for 3265327_3 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1015] topology](images/train_1015.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3224990_4 and 3220768_1
- `C2`: Press down the tilt angle of 3265327_3 by 8 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220768_1
- `C4`: Adjust the azimuth of 3265327_3 by 50 degrees **← 정답**
- `C5`: Decrease A3 Offset threshold for 3265327_3
- `C6`: Increase transmission power for 3220768_1
- `C7`: Decrease transmission power for 3265327_3
- `C8`: Decrease transmission power for 3220768_1
- `C9`: Increase transmission power for 3265327_3 **← 정답**
- `C10`: Press down the tilt angle  of 3220768_1 by 3 degrees
- `C11`: Decrease A3 Offset threshold for 3220768_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265327_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220768_1
- `C14`: Adjust the azimuth of 3220768_1 by 7 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Increase A3 Offset threshold for 3265327_3
- `C17`: Lift the tilt angle of 3265327_3 by 8 degrees
- `C18`: Lift the tilt angle  of 3220768_1 by 3 degrees
- `C19`: Increase A3 Offset threshold for 3220768_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265327_3
- `C21`: Check test server and transmission issues
- `C22`: Add neighbor relationship between 3265327_3 and 3220768_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.730 | MS1 | 121.4656655729 | 31.1446349987 | 587 | 504990 | -90.99 | 12.17 | 457.03 | 0.02 | 2.43 | 1566 |
| 2024-09-20 22:21:32.354 | MS1 | 121.4656688618 | 31.1446367019 | 587 | 504990 | -91.83 | 13.04 | 425.01 | 0.14 | 2.28 | 1577 |
| 2024-09-20 22:21:33.343 | MS1 | 121.4656684710 | 31.1446242424 | 587 | 504990 | -92.43 | 14.36 | 393.31 | 0.14 | 2.61 | 1579 |
| 2024-09-20 22:21:34.589 | MS1 | 121.4656725559 | 31.1446254659 | 587 | 504990 | -106.37 | 1.29 | 17.68 | 0.11 | 1.13 | 1568 |
| 2024-09-20 22:21:35.235 | MS1 | 121.4656605113 | 31.1446306398 | 587 | 504990 | -107.06 | -0.62 | 43.27 | 0.09 | 1.20 | 1587 |
| 2024-09-20 22:21:36.698 | MS1 | 121.4656698827 | 31.1446366557 | 587 | 504990 | -100.70 | -1.91 | 30.31 | 0.19 | 1.03 | 1580 |
| 2024-09-20 22:21:37.992 | MS1 | 121.4656705003 | 31.1446197265 | 587 | 504990 | -106.42 | 1.43 | 77.67 | 0.03 | 1.17 | 1587 |
| 2024-09-20 22:21:38.343 | MS1 | 121.4656586988 | 31.1446236417 | 587 | 504990 | -106.45 | 1.29 | 54.96 | 0.01 | 1.06 | 1593 |
| 2024-09-20 22:21:39.168 | MS1 | 121.4656649004 | 31.1446271417 | 587 | 504990 | -105.51 | 0.44 | 33.05 | 0.07 | 1.42 | 1562 |
| 2024-09-20 22:21:40.992 | MS1 | 121.4656647116 | 31.1446266413 | 587 | 504990 | -94.55 | 12.15 | 557.34 | 0.00 | 2.18 | 1581 |
| 2024-09-20 22:21:41.720 | MS1 | 121.4656760726 | 31.1446317040 | 587 | 504990 | -93.66 | 16.59 | 317.93 | 0.10 | 2.02 | 1564 |
| 2024-09-20 22:21:42.976 | MS1 | 121.4656601334 | 31.1446356162 | 587 | 504990 | -90.46 | 13.00 | 500.23 | 0.18 | 2.57 | 1576 |

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
| 3220768 | 1 | 121.4739764728 | 31.1527015065 | 228 | 1 | 3 | 48.4 | TDD | 905 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3224990 | 4 | 121.4664434764 | 31.1554223988 | 258 | 0 | 3 | 41.6 | TDD | 719 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3256025 | 2 | 121.4655582833 | 31.1527246905 | 161 | 9 | 7 | 32.2 | TDD | 394 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3265327 | 3 | 121.4662286815 | 31.1495730929 | 113 | 3 | 8 | 44.7 | TDD | 587 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.918 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.942 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.060 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.060 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.248 | NREventA2 | measId:1;ServCellPCI:1003;S... |
| 2024-09-20 22:21:34.365 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220768 | 1 | 18.3585 | 18.4880 | -115.9703 | 15.8928 | 112.5679 | 0.0017 | 0.0171 |
| 2024_09_20 22:00 | 3256025 | 2 | 13.7093 | 13.8056 | -114.4485 | 9.0863 | 167.8447 | 0.0078 | 0.0162 |
| 2024_09_20 22:00 | 3265327 | 3 | 5.0160 | 8.0575 | -115.9490 | 8.6140 | 125.3302 | 0.1681 | 0.0068 |
| 2024_09_20 22:00 | 3224990 | 4 | 7.2346 | 17.3911 | -115.0014 | 19.5852 | 182.8382 | 0.0087 | 0.0147 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415280_486B7A23 | 504990 | 587 | -106.3 | 504990 | 905 | -110.2 | 504990 | 719 | -116.1 | 504990 | 394 |
| MR_1774415280_10447C8F | 504990 | 587 | -107.5 | 504990 | 905 | -113.6 | 504990 | 719 | -117.6 | 504990 | 394 |
| MR_1774415280_EE8627FC | 504990 | 587 | -104.8 | 504990 | 905 | -109.9 | 504990 | 719 | -118.6 | 504990 | 394 |
| MR_1774415280_12B9954B | 504990 | 587 | -104.9 | 504990 | 905 | -112.5 | 504990 | 719 | -115.8 | 504990 | 394 |
| MR_1774415280_D906390C | 504990 | 587 | -105.8 | 504990 | 905 | -113.0 | 504990 | 719 | -117.3 | 504990 | 394 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1016: `76c5fa75-50a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `76c5fa75-50a5-446a-a463-dcfe5cfb778b` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3211256_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1016] topology](images/train_1016.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243596_2
- `C2`: Decrease A3 Offset threshold for 3211256_1
- `C3`: Increase transmission power for 3211256_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211256_1
- `C5`: Lift the tilt angle of 3211256_1 by 3 degrees
- `C6`: Lift the tilt angle  of 3243596_2 by 8 degrees
- `C7`: Adjust the azimuth of 3243596_2 by 22 degrees
- `C8`: Add neighbor relationship between 3211604_3 and 3243596_2
- `C9`: Decrease transmission power for 3211256_1
- `C10`: Increase A3 Offset threshold for 3211256_1
- `C11`: Decrease transmission power for 3243596_2
- `C12`: Add neighbor relationship between 3211256_1 and 3243596_2
- `C13`: Adjust the azimuth of 3211256_1 by 0 degrees
- `C14`: Increase A3 Offset threshold for 3243596_2
- `C15`: Check test server and transmission issues
- `C16`: Increase transmission power for 3243596_2
- `C17`: Press down the tilt angle  of 3243596_2 by 8 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243596_2
- `C19`: Press down the tilt angle of 3211256_1 by 3 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211256_1 **← 정답**
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease A3 Offset threshold for 3243596_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.223 | MS1 | 121.4656617577 | 31.1446337808 | 465 | 504990 | -91.70 | 16.04 | 340.20 | 0.17 | 2.35 | 1571 |
| 2024-09-20 22:21:32.253 | MS1 | 121.4656721265 | 31.1446276697 | 465 | 504990 | -91.97 | 13.81 | 307.59 | 0.08 | 2.98 | 1568 |
| 2024-09-20 22:21:33.806 | MS1 | 121.4656648026 | 31.1446243744 | 465 | 504990 | -89.61 | 15.06 | 592.20 | 0.05 | 2.22 | 1600 |
| 2024-09-20 22:21:34.315 | MS1 | 121.4656677436 | 31.1446286064 | 465 | 504990 | -89.19 | 16.56 | 89.82 | 0.61 | 2.80 | 549 |
| 2024-09-20 22:21:35.569 | MS1 | 121.4656675444 | 31.1446271602 | 465 | 504990 | -88.75 | 14.52 | 63.37 | 0.54 | 2.82 | 621 |
| 2024-09-20 22:21:36.383 | MS1 | 121.4656616601 | 31.1446363598 | 465 | 504990 | -91.00 | 14.26 | 99.75 | 0.54 | 2.08 | 640 |
| 2024-09-20 22:21:37.382 | MS1 | 121.4656721463 | 31.1446240787 | 465 | 504990 | -92.42 | 7.21 | 97.58 | 0.52 | 2.69 | 609 |
| 2024-09-20 22:21:38.615 | MS1 | 121.4656592896 | 31.1446238077 | 465 | 504990 | -92.20 | 8.96 | 86.75 | 0.66 | 2.57 | 628 |
| 2024-09-20 22:21:39.809 | MS1 | 121.4656593264 | 31.1446202305 | 465 | 504990 | -89.51 | 11.70 | 71.31 | 0.68 | 2.85 | 602 |
| 2024-09-20 22:21:40.761 | MS1 | 121.4656754631 | 31.1446342598 | 465 | 504990 | -90.62 | 10.99 | 431.27 | 0.07 | 2.64 | 1589 |
| 2024-09-20 22:21:41.688 | MS1 | 121.4656699458 | 31.1446207413 | 465 | 504990 | -92.13 | 7.82 | 548.37 | 0.17 | 2.07 | 1565 |
| 2024-09-20 22:21:42.940 | MS1 | 121.4656656146 | 31.1446340760 | 465 | 504990 | -91.14 | 9.07 | 381.20 | 0.01 | 2.58 | 1572 |

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
| 3211256 | 1 | 121.4734138436 | 31.1457713467 | 260 | 1 | 9 | 25.8 | TDD | 465 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3211604 | 3 | 121.4650182465 | 31.1535275985 | 96 | 13 | 2 | 44.6 | TDD | 332 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3235402 | 4 | 121.4676149809 | 31.1508831676 | 260 | 8 | 11 | 36.2 | TDD | 70 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3243596 | 2 | 121.4662641024 | 31.1558871697 | 161 | 6 | 1 | 48.1 | TDD | 10 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.424 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.444 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.563 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.563 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.253 | NREventA3 | measId:2;ServCellPCI:319;Se... |
| 2024-09-20 22:21:38.493 | NRHandoverAttempt | SourcePCI:319;SourceNR-ARFC... |
| 2024-09-20 22:21:38.530 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.540 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.641 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.641 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211256 | 1 | 18.4768 | 12.1594 | -114.5404 | 10.3188 | 150.6190 | 0.0049 | 0.0182 |
| 2024_09_20 22:00 | 3243596 | 2 | 17.5834 | 6.9386 | -117.9631 | 7.1002 | 97.7949 | 0.0174 | 0.0072 |
| 2024_09_20 22:00 | 3211604 | 3 | 12.3477 | 7.6240 | -116.6154 | 12.4648 | 133.5579 | 0.0065 | 0.0183 |
| 2024_09_20 22:00 | 3235402 | 4 | 14.6159 | 14.2764 | -114.4450 | 17.6980 | 173.3180 | 0.0122 | 0.0198 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417109_E945C8DA | 504990 | 465 | -87.3 | 504990 | 10 | -98.0 | 504990 | 332 | -99.1 | 504990 | 70 |
| MR_1774417109_6FB6B49D | 504990 | 465 | -87.2 | 504990 | 10 | -97.9 | 504990 | 332 | -98.9 | 504990 | 70 |
| MR_1774417109_BF845FCD | 504990 | 465 | -87.5 | 504990 | 10 | -98.6 | 504990 | 332 | -99.3 | 504990 | 70 |
| MR_1774417109_F12FD738 | 504990 | 465 | -88.5 | 504990 | 10 | -97.0 | 504990 | 332 | -95.5 | 504990 | 70 |
| MR_1774417109_F0991787 | 504990 | 465 | -87.6 | 504990 | 10 | -96.5 | 504990 | 332 | -97.4 | 504990 | 70 |
| MR_1774417109_CACB13E0 | 504990 | 465 | -89.4 | 504990 | 10 | -95.9 | 504990 | 332 | -96.3 | 504990 | 70 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1017: `2d6423e1-649...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2d6423e1-6499-4630-8399-d5a1cd3a5899` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3253052_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1017] topology](images/train_1017.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Press down the tilt angle  of 3243762_3 by 10 degrees
- `C3`: Increase transmission power for 3253052_2
- `C4`: Decrease transmission power for 3253052_2
- `C5`: Increase A3 Offset threshold for 3253052_2
- `C6`: Add neighbor relationship between 3234462_1 and 3243762_3
- `C7`: Add neighbor relationship between 3253052_2 and 3243762_3
- `C8`: Decrease A3 Offset threshold for 3253052_2
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Adjust the azimuth of 3243762_3 by 50 degrees
- `C11`: Increase transmission power for 3243762_3
- `C12`: Increase A3 Offset threshold for 3243762_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243762_3
- `C14`: Lift the tilt angle  of 3243762_3 by 10 degrees
- `C15`: Lift the tilt angle of 3253052_2 by 3 degrees
- `C16`: Decrease A3 Offset threshold for 3243762_3
- `C17`: Decrease transmission power for 3243762_3
- `C18`: Press down the tilt angle of 3253052_2 by 3 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253052_2 **← 정답**
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253052_2
- `C21`: Adjust the azimuth of 3253052_2 by 22 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243762_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.625 | MS1 | 121.4656710784 | 31.1446342708 | 281 | 504990 | -88.86 | 12.48 | 419.49 | 0.07 | 2.68 | 1600 |
| 2024-09-20 22:21:32.235 | MS1 | 121.4656770336 | 31.1446294979 | 281 | 504990 | -90.25 | 14.16 | 508.29 | 0.00 | 2.69 | 1585 |
| 2024-09-20 22:21:33.331 | MS1 | 121.4656673665 | 31.1446235228 | 281 | 504990 | -89.45 | 14.93 | 532.87 | 0.11 | 2.00 | 1565 |
| 2024-09-20 22:21:34.223 | MS1 | 121.4656744031 | 31.1446297762 | 281 | 504990 | -91.09 | 13.75 | 67.25 | 0.52 | 2.40 | 662 |
| 2024-09-20 22:21:35.341 | MS1 | 121.4656713842 | 31.1446309691 | 281 | 504990 | -89.78 | 13.53 | 53.58 | 0.52 | 2.14 | 541 |
| 2024-09-20 22:21:36.379 | MS1 | 121.4656691338 | 31.1446256076 | 281 | 504990 | -91.20 | 17.05 | 51.63 | 0.56 | 2.35 | 616 |
| 2024-09-20 22:21:37.969 | MS1 | 121.4656638058 | 31.1446338785 | 281 | 504990 | -91.97 | 11.21 | 100.82 | 0.68 | 2.89 | 606 |
| 2024-09-20 22:21:38.364 | MS1 | 121.4656677070 | 31.1446368775 | 281 | 504990 | -89.79 | 10.25 | 54.67 | 0.55 | 2.51 | 666 |
| 2024-09-20 22:21:39.811 | MS1 | 121.4656693194 | 31.1446216396 | 281 | 504990 | -92.35 | 9.13 | 95.93 | 0.56 | 2.86 | 604 |
| 2024-09-20 22:21:40.301 | MS1 | 121.4656723527 | 31.1446230564 | 281 | 504990 | -93.98 | 11.36 | 434.42 | 0.05 | 2.84 | 1564 |
| 2024-09-20 22:21:41.516 | MS1 | 121.4656583873 | 31.1446205102 | 281 | 504990 | -89.81 | 8.24 | 574.27 | 0.03 | 2.77 | 1580 |
| 2024-09-20 22:21:42.157 | MS1 | 121.4656640637 | 31.1446298368 | 281 | 504990 | -90.99 | 11.52 | 590.01 | 0.12 | 2.27 | 1597 |

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
| 3234462 | 1 | 121.4728068646 | 31.1501369996 | 130 | 13 | 7 | 48.6 | TDD | 128 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3243762 | 3 | 121.4687822662 | 31.1441239924 | 53 | 7 | 3 | 21.7 | TDD | 470 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3253052 | 2 | 121.4727615532 | 31.1503179972 | 249 | 0 | 12 | 45.9 | TDD | 281 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3260976 | 4 | 121.4641997611 | 31.1441514400 | 320 | 10 | 1 | 32.4 | TDD | 886 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.862 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.885 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.995 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.995 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.715 | NREventA3 | measId:2;ServCellPCI:491;Se... |
| 2024-09-20 22:21:37.955 | NRHandoverAttempt | SourcePCI:491;SourceNR-ARFC... |
| 2024-09-20 22:21:37.998 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.011 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.117 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.117 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234462 | 1 | 16.2696 | 15.0395 | -115.7726 | 14.2502 | 94.3486 | 0.0162 | 0.0037 |
| 2024_09_20 22:00 | 3253052 | 2 | 9.9053 | 19.8573 | -114.1676 | 17.0747 | 119.8093 | 0.0011 | 0.0058 |
| 2024_09_20 22:00 | 3243762 | 3 | 13.8779 | 10.5806 | -115.1683 | 17.3418 | 145.6133 | 0.0145 | 0.0181 |
| 2024_09_20 22:00 | 3260976 | 4 | 5.6114 | 8.1981 | -115.2421 | 18.3968 | 96.8939 | 0.0015 | 0.0163 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416243_C94FF930 | 504990 | 281 | -90.1 | 504990 | 470 | -101.5 | 504990 | 128 | -105.2 | 504990 | 886 |
| MR_1774416243_2AFAE7B9 | 504990 | 281 | -91.1 | 504990 | 470 | -98.9 | 504990 | 128 | -104.9 | 504990 | 886 |
| MR_1774416243_1DC30EC6 | 504990 | 281 | -89.5 | 504990 | 470 | -101.4 | 504990 | 128 | -103.8 | 504990 | 886 |
| MR_1774416243_A4E6155E | 504990 | 281 | -90.2 | 504990 | 470 | -99.8 | 504990 | 128 | -105.9 | 504990 | 886 |
| MR_1774416243_E17E24FC | 504990 | 281 | -91.5 | 504990 | 470 | -102.0 | 504990 | 128 | -105.3 | 504990 | 886 |
| MR_1774416243_5509733E | 504990 | 281 | -93.1 | 504990 | 470 | -99.3 | 504990 | 128 | -103.7 | 504990 | 886 |
| MR_1774416243_A69B08B4 | 504990 | 281 | -92.1 | 504990 | 470 | -99.7 | 504990 | 128 | -105.2 | 504990 | 886 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1018: `f9c240bc-b09...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f9c240bc-b095-450a-b6ac-ba8540b47a97` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1018] topology](images/train_1018.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3265276_2
- `C2`: Increase transmission power for 3223383_4
- `C3`: Adjust the azimuth of 3223383_4 by 50 degrees
- `C4`: Add neighbor relationship between 3265276_2 and 3223383_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223383_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265276_2
- `C7`: Add neighbor relationship between 3263730_3 and 3223383_4
- `C8`: Adjust the azimuth of 3265276_2 by 50 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Lift the tilt angle of 3265276_2 by 7 degrees
- `C11`: Decrease A3 Offset threshold for 3223383_4
- `C12`: Check test server and transmission issues **← 정답**
- `C13`: Decrease transmission power for 3223383_4
- `C14`: Increase A3 Offset threshold for 3265276_2
- `C15`: Press down the tilt angle  of 3223383_4 by 6 degrees
- `C16`: Decrease A3 Offset threshold for 3265276_2
- `C17`: Lift the tilt angle  of 3223383_4 by 6 degrees
- `C18`: Increase A3 Offset threshold for 3223383_4
- `C19`: Press down the tilt angle of 3265276_2 by 7 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223383_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265276_2
- `C22`: Increase transmission power for 3265276_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.656 | MS1 | 121.4656602030 | 31.1446184938 | 571 | 504990 | -88.72 | 17.35 | 400.57 | 0.05 | 2.05 | 1588 |
| 2024-09-20 22:21:32.613 | MS1 | 121.4656741002 | 31.1446344077 | 571 | 504990 | -89.37 | 12.07 | 483.29 | 0.04 | 2.16 | 1575 |
| 2024-09-20 22:21:33.815 | MS1 | 121.4656645028 | 31.1446359435 | 571 | 504990 | -86.41 | 14.64 | 367.15 | 0.08 | 2.08 | 1578 |
| 2024-09-20 22:21:34.536 | MS1 | 121.4656700434 | 31.1446292499 | 571 | 504990 | -85.28 | 15.62 | 74.82 | 0.07 | 2.11 | 315 |
| 2024-09-20 22:21:35.810 | MS1 | 121.4656697073 | 31.1446377018 | 571 | 504990 | -90.34 | 16.86 | 72.27 | 0.09 | 2.65 | 347 |
| 2024-09-20 22:21:36.612 | MS1 | 121.4656662344 | 31.1446301337 | 571 | 504990 | -86.55 | 15.44 | 82.81 | 0.18 | 2.71 | 419 |
| 2024-09-20 22:21:37.377 | MS1 | 121.4656645117 | 31.1446265057 | 571 | 504990 | -90.92 | 7.75 | 43.33 | 0.06 | 2.14 | 425 |
| 2024-09-20 22:21:38.671 | MS1 | 121.4656621431 | 31.1446207362 | 571 | 504990 | -92.40 | 11.03 | 99.56 | 0.12 | 2.98 | 301 |
| 2024-09-20 22:21:39.342 | MS1 | 121.4656682149 | 31.1446375975 | 571 | 504990 | -90.95 | 12.17 | 86.67 | 0.03 | 2.06 | 369 |
| 2024-09-20 22:21:40.970 | MS1 | 121.4656708067 | 31.1446200995 | 571 | 504990 | -91.26 | 8.93 | 543.29 | 0.11 | 2.23 | 1596 |
| 2024-09-20 22:21:41.755 | MS1 | 121.4656762432 | 31.1446212823 | 571 | 504990 | -93.98 | 8.70 | 419.44 | 0.06 | 2.73 | 1588 |
| 2024-09-20 22:21:42.577 | MS1 | 121.4656717238 | 31.1446206881 | 571 | 504990 | -93.80 | 10.12 | 501.60 | 0.15 | 2.59 | 1588 |

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
| 3223383 | 4 | 121.4652715837 | 31.1480377717 | 226 | 1 | 3 | 31.7 | TDD | 111 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3263124 | 1 | 121.4753107923 | 31.1522900433 | 174 | 4 | 0 | 36.1 | TDD | 73 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3263730 | 3 | 121.4678199993 | 31.1506106651 | 83 | 14 | 12 | 45.1 | TDD | 933 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3265276 | 2 | 121.4677593181 | 31.1471618935 | 51 | 1 | 1 | 37.6 | TDD | 571 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.273 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.288 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.411 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.411 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.102 | NREventA3 | measId:2;ServCellPCI:546;Se... |
| 2024-09-20 22:21:38.342 | NRHandoverAttempt | SourcePCI:546;SourceNR-ARFC... |
| 2024-09-20 22:21:38.374 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.385 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.521 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.521 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263124 | 1 | 15.5776 | 16.0975 | -115.6721 | 7.7051 | 145.0849 | 0.0098 | 0.0142 |
| 2024_09_20 22:00 | 3265276 | 2 | 5.4572 | 12.2441 | -115.4466 | 15.8450 | 148.7411 | 0.0141 | 0.0066 |
| 2024_09_20 22:00 | 3263730 | 3 | 17.6412 | 18.1727 | -116.4907 | 11.5162 | 189.6615 | 0.0152 | 0.0002 |
| 2024_09_20 22:00 | 3223383 | 4 | 11.2805 | 15.4648 | -117.5067 | 9.7834 | 88.2994 | 0.0185 | 0.0160 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416999_92E6579C | 504990 | 571 | -84.6 | 504990 | 111 | -90.2 | 504990 | 933 | -95.0 | 504990 | 73 |
| MR_1774416999_1FEC43CE | 504990 | 571 | -86.7 | 504990 | 111 | -91.7 | 504990 | 933 | -95.9 | 504990 | 73 |
| MR_1774416999_3D83B6B8 | 504990 | 571 | -87.1 | 504990 | 111 | -89.4 | 504990 | 933 | -97.5 | 504990 | 73 |
| MR_1774416999_F0DCCECD | 504990 | 571 | -84.5 | 504990 | 111 | -91.1 | 504990 | 933 | -98.6 | 504990 | 73 |
| MR_1774416999_11A7EB53 | 504990 | 571 | -86.6 | 504990 | 111 | -89.4 | 504990 | 933 | -97.7 | 504990 | 73 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1019: `d10d0af6-004...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d10d0af6-004e-466d-b30e-a6e9733fc41b` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease A3 Offset threshold for 3211669_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1019] topology](images/train_1019.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3211669_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212898_1
- `C3`: Lift the tilt angle of 3211669_3 by 10 degrees
- `C4`: Press down the tilt angle of 3211669_3 by 10 degrees
- `C5`: Decrease A3 Offset threshold for 3212898_1
- `C6`: Adjust the azimuth of 3212898_1 by 50 degrees
- `C7`: Check test server and transmission issues
- `C8`: Add neighbor relationship between 3225535_2 and 3212898_1
- `C9`: Adjust the azimuth of 3211669_3 by 50 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211669_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212898_1
- `C12`: Increase A3 Offset threshold for 3211669_3
- `C13`: Decrease transmission power for 3212898_1
- `C14`: Decrease A3 Offset threshold for 3211669_3 **← 정답**
- `C15`: Lift the tilt angle  of 3212898_1 by 7 degrees
- `C16`: Press down the tilt angle  of 3212898_1 by 7 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211669_3
- `C18`: Increase transmission power for 3211669_3
- `C19`: Increase A3 Offset threshold for 3212898_1
- `C20`: Add neighbor relationship between 3211669_3 and 3212898_1
- `C21`: Increase transmission power for 3212898_1
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.110 | MS1 | 121.4656749143 | 31.1446213055 | 485 | 504990 | -82.37 | 17.32 | 421.66 | 0.19 | 2.74 | 1575 |
| 2024-09-20 22:21:32.766 | MS1 | 121.4656632893 | 31.1446379687 | 485 | 504990 | -75.14 | 14.90 | 602.94 | 0.12 | 2.31 | 1578 |
| 2024-09-20 22:21:33.262 | MS1 | 121.4656723887 | 31.1446334261 | 485 | 504990 | -77.55 | 16.85 | 380.91 | 0.15 | 2.44 | 1592 |
| 2024-09-20 22:21:34.410 | MS1 | 121.4656623943 | 31.1446293727 | 485 | 504990 | -90.98 | -3.27 | 66.59 | 0.20 | 1.40 | 1596 |
| 2024-09-20 22:21:35.619 | MS1 | 121.4656775423 | 31.1446238312 | 485 | 504990 | -86.01 | -3.70 | 61.36 | 0.15 | 1.08 | 1591 |
| 2024-09-20 22:21:36.706 | MS1 | 121.4656694819 | 31.1446251227 | 485 | 504990 | -91.59 | -2.46 | 81.19 | 0.16 | 1.17 | 1564 |
| 2024-09-20 22:21:37.132 | MS1 | 121.4656714791 | 31.1446307605 | 485 | 504990 | -86.35 | -1.73 | 60.26 | 0.13 | 1.05 | 1587 |
| 2024-09-20 22:21:38.923 | MS1 | 121.4656587862 | 31.1446311508 | 485 | 504990 | -92.34 | -1.11 | 35.27 | 0.18 | 1.49 | 1582 |
| 2024-09-20 22:21:39.182 | MS1 | 121.4656708486 | 31.1446197413 | 401 | 504990 | -80.42 | 15.04 | 299.89 | 0.01 | 1.00 | 1596 |
| 2024-09-20 22:21:40.549 | MS1 | 121.4656722989 | 31.1446193187 | 401 | 504990 | -75.42 | 13.08 | 413.06 | 0.03 | 2.12 | 1593 |
| 2024-09-20 22:21:41.790 | MS1 | 121.4656611460 | 31.1446287031 | 401 | 504990 | -81.04 | 15.10 | 381.28 | 0.06 | 2.90 | 1560 |
| 2024-09-20 22:21:42.790 | MS1 | 121.4656639673 | 31.1446193945 | 401 | 504990 | -79.08 | 14.65 | 342.85 | 0.13 | 2.22 | 1595 |

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
| 3211669 | 3 | 121.4708515169 | 31.1460490757 | 330 | 7 | 10 | 33.5 | TDD | 485 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3212898 | 1 | 121.4744152412 | 31.1452319123 | 40 | 6 | 1 | 20.4 | TDD | 401 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3225535 | 2 | 121.4679041107 | 31.1474478091 | 181 | 13 | 6 | 21.3 | TDD | 425 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3269184 | 4 | 121.4674406576 | 31.1498534864 | 51 | 5 | 2 | 42.0 | TDD | 398 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.582 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.605 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.705 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.705 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.422 | NREventA3 | measId:2;ServCellPCI:257;Se... |
| 2024-09-20 22:21:38.662 | NRHandoverAttempt | SourcePCI:257;SourceNR-ARFC... |
| 2024-09-20 22:21:38.711 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.725 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.853 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.853 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212898 | 1 | 11.3800 | 14.9650 | -115.4058 | 6.5644 | 86.3189 | 0.0189 | 0.0132 |
| 2024_09_20 22:00 | 3225535 | 2 | 5.7265 | 9.5562 | -114.1169 | 19.5635 | 164.6261 | 0.0075 | 0.0046 |
| 2024_09_20 22:00 | 3211669 | 3 | 14.3136 | 16.3986 | -115.7703 | 16.6878 | 172.7749 | 0.0132 | 0.1275 |
| 2024_09_20 22:00 | 3269184 | 4 | 15.7306 | 10.8703 | -117.2857 | 15.9299 | 180.3128 | 0.0057 | 0.0137 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415737_3CCF7A5D | 504990 | 485 | -89.8 | 504990 | 401 | -86.3 | 504990 | 425 | -83.9 | 504990 | 398 |
| MR_1774415737_0731886D | 504990 | 485 | -91.7 | 504990 | 401 | -84.3 | 504990 | 425 | -84.7 | 504990 | 398 |
| MR_1774415737_462FBC0D | 504990 | 401 | -86.5 | 504990 | 485 | -91.1 | 504990 | 425 | -85.5 | 504990 | 398 |
| MR_1774415737_09C678FF | 504990 | 401 | -84.5 | 504990 | 485 | -89.7 | 504990 | 425 | -87.0 | 504990 | 398 |
| MR_1774415737_E7BC58C3 | 504990 | 401 | -86.0 | 504990 | 485 | -89.4 | 504990 | 425 | -86.4 | 504990 | 398 |
| MR_1774415737_BEFC1AC2 | 504990 | 485 | -89.5 | 504990 | 401 | -86.1 | 504990 | 425 | -87.0 | 504990 | 398 |
| MR_1774415737_832E9DAE | 504990 | 401 | -87.1 | 504990 | 485 | -89.9 | 504990 | 425 | -85.9 | 504990 | 398 |

> *... 2개 열 생략 (전체 14열)*

---
